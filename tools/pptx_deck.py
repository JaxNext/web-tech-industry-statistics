#!/usr/bin/env python3
"""Local PPTX deck toolkit (Python 3.9+, standard library only).

Encodes the template-editing pipeline that is easy to get wrong:
    unpack -> keep slides -> edit text -> swap fonts -> pack -> QA

Why not the plugin scripts directly?
  The pptx skill's pack.py uses `str | None` annotations, so it needs 3.10+.
  `pack` below is a plain zip writer and runs on any Python 3.9+.

Usage:
  python3 tools/pptx_deck.py unpack       <in.pptx> <dir>
  python3 tools/pptx_deck.py status       <dir> [--src <in.pptx>]
  python3 tools/pptx_deck.py pack         <dir> <out.pptx>
  python3 tools/pptx_deck.py dump         <in.pptx|dir>
  python3 tools/pptx_deck.py keep         <dir> <slide_nums,...>
  python3 tools/pptx_deck.py set-text     <dir> <slide.xml> <n> <new text>
  python3 tools/pptx_deck.py replace-text <dir> <slide.xml> <old> <new>
  python3 tools/pptx_deck.py fonts        <dir> <latin> <east_asian>
  python3 tools/pptx_deck.py check        <in.pptx|dir>

Typical run:
  T="Jax-DF'26-Shenzhen.pptx"
  python3 tools/pptx_deck.py unpack "$T" build/
  python3 tools/pptx_deck.py keep   build/ 17,8,15,26,9,30,29
  python3 tools/pptx_deck.py replace-text build/ slide8.xml "Example with slide title" "一个悖论"
  python3 tools/pptx_deck.py fonts  build/ Roboto "Noto Sans SC"
  python3 tools/pptx_deck.py pack   build/ out.pptx
  python3 tools/pptx_deck.py check  out.pptx
  python3 tools/pptx_deck.py dump   out.pptx
"""

import argparse
import hashlib
import html
import json
import posixpath
import re
import sys
import zipfile
from pathlib import Path
from xml.dom import minidom

TEXT_RUN = re.compile(r"<a:t>(.*?)</a:t>", re.S)
SLD_ID = re.compile(r"<p:sldId\b[^>]*/>")

# Fingerprint file written by `unpack`, checked by `status`.
CACHE_META = ".cache-source.json"


# --- reading a deck from either a .pptx or an unpacked directory ---------

class Reader:
    def __init__(self, src):
        self.src = Path(src)
        self._zip = zipfile.ZipFile(self.src) if self.src.is_file() else None

    def names(self):
        if self._zip:
            return self._zip.namelist()
        return sorted(
            p.relative_to(self.src).as_posix()
            for p in self.src.rglob("*")
            if p.is_file()
        )

    def read(self, name):
        if self._zip:
            return self._zip.read(name).decode("utf-8")
        return (self.src / name).read_text(encoding="utf-8")

    def close(self):
        if self._zip:
            self._zip.close()


def _rels_map(rels_xml):
    """Relationship Id -> Target, tolerant of attribute order."""
    out = {}
    for tag in re.findall(r"<Relationship\b[^>]*/?>", rels_xml):
        i = re.search(r'Id="([^"]+)"', tag)
        t = re.search(r'Target="([^"]+)"', tag)
        if i and t:
            out[i.group(1)] = t.group(1)
    return out


def deck_order(r):
    """Slide file names (slideN.xml) in presentation order."""
    rid2target = _rels_map(r.read("ppt/_rels/presentation.xml.rels"))
    order = []
    for rid in re.findall(r'<p:sldId\b[^>]*?r:id="(rId\d+)"', r.read("ppt/presentation.xml")):
        target = rid2target.get(rid, "")
        if target.startswith("slides/"):
            order.append(target.replace("slides/", ""))
    return order


def slide_text(xml):
    return [html.unescape(t) for t in TEXT_RUN.findall(xml)]


def _esc(s):
    return html.escape(s, quote=False)


def _rewrite_runs(xml, transform):
    """Rebuild a slide by passing (unescaped text, match) through transform.

    transform returns the replacement markup, or None to keep the original run.
    """
    out, last, hits = [], 0, 0
    for m in TEXT_RUN.finditer(xml):
        out.append(xml[last:m.start()])
        repl = transform(html.unescape(m.group(1)))
        if repl is None:
            out.append(m.group(0))
        else:
            hits += 1
            out.append(repl)
        last = m.end()
    out.append(xml[last:])
    return "".join(out), hits


# --- commands -----------------------------------------------------------

def cmd_unpack(args):
    dst = Path(args.dst)
    dst.mkdir(parents=True, exist_ok=True)
    src = Path(args.src)
    with zipfile.ZipFile(src) as z:
        z.extractall(dst)
        count = len(z.namelist())
    meta = {
        "source": src.name,
        "size": src.stat().st_size,
        "sha1": hashlib.sha1(src.read_bytes()).hexdigest(),
    }
    (dst / CACHE_META).write_text(json.dumps(meta, indent=2), encoding="utf-8")
    print(f"unpacked {count} parts -> {dst}")


def cmd_status(args):
    """Report whether an unpacked dir still matches its source .pptx."""
    d = Path(args.dir)
    meta_p = d / CACHE_META
    if not meta_p.exists():
        sys.exit(f"{d} has no {CACHE_META} — unpack it with `unpack` first")
    meta = json.loads(meta_p.read_text(encoding="utf-8"))
    src = Path(args.src) if args.src else d.parent / meta["source"]
    if not src.exists():
        sys.exit(f"source not found: {src} (pass --src explicitly)")

    sha1 = hashlib.sha1(src.read_bytes()).hexdigest()
    if sha1 == meta["sha1"]:
        print(f"FRESH  {d} matches {src.name} (sha1 {sha1[:12]})")
        return
    print(
        f"STALE  {d} was unpacked from a different {src.name}\n"
        f"       cached  size={meta['size']:,} sha1={meta['sha1'][:12]}\n"
        f"       current size={src.stat().st_size:,} sha1={sha1[:12]}\n"
        f"       re-run: unpack {src} {d}"
    )
    sys.exit(1)


def cmd_pack(args):
    src = Path(args.dir)
    files = [p for p in src.rglob("*") if p.is_file()]
    # [Content_Types].xml first is conventional and avoids reader quirks
    files.sort(key=lambda p: (p.name != "[Content_Types].xml", str(p)))
    with zipfile.ZipFile(args.out, "w", zipfile.ZIP_DEFLATED) as z:
        for p in files:
            z.write(p, p.relative_to(src).as_posix())
    print(f"packed {len(files)} parts -> {args.out}")


def cmd_dump(args):
    r = Reader(args.src)
    try:
        order = deck_order(r)
        print(f"deck: {args.src}  ({len(order)} slides)")
        for i, name in enumerate(order, 1):
            print(f"\n[Slide {i}] {name}")
            for t in slide_text(r.read(f"ppt/slides/{name}")):
                if t.strip():
                    print("   ", t)
    finally:
        r.close()


def cmd_keep(args):
    d = Path(args.dir)
    pres_p = d / "ppt" / "presentation.xml"
    pres = pres_p.read_text(encoding="utf-8")
    if "<p:sldIdLst/>" in pres:
        pres = pres.replace("<p:sldIdLst/>", "<p:sldIdLst></p:sldIdLst>")

    rid2target = _rels_map((d / "ppt" / "_rels" / "presentation.xml.rels").read_text(encoding="utf-8"))
    slide2rid = {
        t.replace("slides/", ""): rid
        for rid, t in rid2target.items()
        if t.startswith("slides/")
    }
    entries = {}
    for tag in SLD_ID.findall(pres):
        rid = re.search(r'r:id="([^"]+)"', tag)
        if rid:
            entries[rid.group(1)] = tag

    wanted = []
    for n in [s.strip() for s in args.slides.split(",") if s.strip()]:
        name = f"slide{n}.xml"
        if name not in slide2rid:
            sys.exit(f"slide {n} not present in template")
        rid = slide2rid[name]
        if rid not in entries:
            sys.exit(f"slide {n} has no sldId entry")
        wanted.append(entries[rid])

    block = "  <p:sldIdLst>\n" + "".join(f"    {e}\n" for e in wanted) + "  </p:sldIdLst>"
    new_pres, hits = re.subn(r"<p:sldIdLst>.*?</p:sldIdLst>", block, pres, flags=re.S)
    if hits != 1:
        sys.exit(f"expected one sldIdLst, found {hits}")
    pres_p.write_text(new_pres, encoding="utf-8")
    print(f"kept {len(wanted)} slides in order: {args.slides}")


def cmd_set_text(args):
    p = Path(args.dir) / "ppt" / "slides" / args.slide
    xml = p.read_text(encoding="utf-8")
    runs = list(TEXT_RUN.finditer(xml))
    if not 1 <= args.n <= len(runs):
        sys.exit(f"{args.slide} has {len(runs)} text runs; index {args.n} out of range")
    m = runs[args.n - 1]
    xml = xml[:m.start()] + f"<a:t>{_esc(args.text)}</a:t>" + xml[m.end():]
    p.write_text(xml, encoding="utf-8")
    print(f"{args.slide}: run #{args.n} -> {args.text}")


def cmd_replace_text(args):
    p = Path(args.dir) / "ppt" / "slides" / args.slide
    xml = p.read_text(encoding="utf-8")
    new_xml, hits = _rewrite_runs(
        xml, lambda t: f"<a:t>{_esc(args.new)}</a:t>" if t == args.old else None
    )
    if hits == 0:
        sys.exit(f"no text run equal to {args.old!r} in {args.slide}")
    p.write_text(new_xml, encoding="utf-8")
    print(f"{args.slide}: replaced {hits} run(s): {args.old!r} -> {args.new!r}")


def _swap_typeface(xml, tag, new):
    """Replace a:latin / a:ea typefaces, leaving theme refs (+mj-lt) alone."""
    def f(m):
        return m.group(0) if m.group(1).startswith("+") else f'{tag} typeface="{new}"'
    return re.sub(rf'{tag} typeface="([^"]*)"', f, xml)


def cmd_fonts(args):
    root = Path(args.dir) / "ppt"
    touched = 0
    for sub in ("slides", "slideLayouts", "slideMasters", "notesSlides"):
        folder = root / sub
        if not folder.is_dir():
            continue
        for p in sorted(folder.glob("*.xml")):
            xml = p.read_text(encoding="utf-8")
            new = _swap_typeface(_swap_typeface(xml, "a:latin", args.latin), "a:ea", args.east_asian)
            if new != xml:
                p.write_text(new, encoding="utf-8")
                touched += 1
    print(f"fonts: latin={args.latin} ea={args.east_asian} ({touched} files updated)")


def cmd_check(args):
    r = Reader(args.src)
    problems = []
    try:
        names = set(r.names())
        for name in sorted(names):
            if not name.endswith((".xml", ".rels")):
                continue
            try:
                minidom.parseString(r.read(name).encode("utf-8"))
            except Exception as e:
                problems.append(f"{name}: not well-formed ({e})")

        for name in sorted(names):
            if not name.endswith(".rels"):
                continue
            base = posixpath.dirname(posixpath.dirname(name))
            for tgt in _rels_map(r.read(name)).values():
                if tgt.startswith(("http:", "https:", "file:", "/", "#")):
                    continue
                resolved = posixpath.normpath(posixpath.join(base, tgt))
                if resolved not in names:
                    problems.append(f"{name}: missing target {resolved}")
    finally:
        r.close()

    if problems:
        for p in problems:
            print("BAD", p)
        sys.exit(1)
    print("check: OK (XML well-formed, all relationship targets exist)")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("unpack"); p.add_argument("src"); p.add_argument("dst"); p.set_defaults(fn=cmd_unpack)
    p = sub.add_parser("status"); p.add_argument("dir"); p.add_argument("--src"); p.set_defaults(fn=cmd_status)
    p = sub.add_parser("pack"); p.add_argument("dir"); p.add_argument("out"); p.set_defaults(fn=cmd_pack)
    p = sub.add_parser("dump"); p.add_argument("src"); p.set_defaults(fn=cmd_dump)
    p = sub.add_parser("keep"); p.add_argument("dir"); p.add_argument("slides"); p.set_defaults(fn=cmd_keep)
    p = sub.add_parser("set-text"); p.add_argument("dir"); p.add_argument("slide"); p.add_argument("n", type=int); p.add_argument("text"); p.set_defaults(fn=cmd_set_text)
    p = sub.add_parser("replace-text"); p.add_argument("dir"); p.add_argument("slide"); p.add_argument("old"); p.add_argument("new"); p.set_defaults(fn=cmd_replace_text)
    p = sub.add_parser("fonts"); p.add_argument("dir"); p.add_argument("latin"); p.add_argument("east_asian"); p.set_defaults(fn=cmd_fonts)
    p = sub.add_parser("check"); p.add_argument("src"); p.set_defaults(fn=cmd_check)

    args = ap.parse_args()
    args.fn(args)


if __name__ == "__main__":
    main()
