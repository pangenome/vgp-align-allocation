#!/bin/zsh
# Build the ACCESS-CI allocation request PDFs.
# Pipeline: markdown -> HTML (pandoc, math disabled) -> inline SVG figures -> PDF (Chrome).
# Same mechanism as ~/git/writing/grants/NSF-26-509/build.sh.
#
#   ./build.sh              build every document, draft markers visible
#   ./build.sh --final      strip all DRAFT NOTE blocks (submission build)
#   ./build.sh main perf    build only the named documents
#
# The -tex_math_dollars flag is mandatory: without it pandoc reads "$" amounts as math.
set -e
cd "$(dirname "$0")"

SRC=galaxy-2026
FINAL=0
DOCS=()
for arg in "$@"; do
  case "$arg" in
    --final) FINAL=1 ;;
    *) DOCS+=("$arg") ;;
  esac
done
if [[ ${#DOCS[@]} -eq 0 ]]; then
  DOCS=(main progress perf abstract references special-requirements)
fi

# ACCESS page limits. 0 = no limit.
typeset -A LIMIT
LIMIT=(main 10 progress 3 perf 5 abstract 0 references 0 special-requirements 1)

CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
[[ -x "$CHROME" ]] || { echo "Chrome not found at $CHROME" >&2; exit 1; }

mkdir -p build
STATUS=0

for doc in "${DOCS[@]}"; do
  [[ -f "$SRC/$doc.md" ]] || { echo "  skip $doc (no $SRC/$doc.md)"; continue; }

  pandoc "$SRC/$doc.md" --from gfm-tex_math_dollars --to html5 --standalone \
    -c ../access.css -o "build/$doc.html"

  # Mark up draft notes, and inline figure SVGs as true vector art.
  FINAL=$FINAL python3 - "build/$doc.html" <<'PY'
import re, os, sys
path = sys.argv[1]
final = os.environ.get("FINAL") == "1"
html = open(path, encoding="utf-8").read()

# A draft note is a <p> opening with "[TODO" or a <blockquote> containing
# "REVIEW NOTE". In a final build both are deleted outright.
todo_p = re.compile(r'<p>\s*\[TODO.*?</p>', re.S)
todo_bq = re.compile(r'<blockquote>(?:(?!</blockquote>).)*?REVIEW NOTE.*?</blockquote>', re.S)
n = len(todo_p.findall(html)) + len(todo_bq.findall(html))
if final:
    html = todo_p.sub('', html)
    html = todo_bq.sub('', html)
else:
    html = todo_p.sub(lambda m: '<div class="todo">' + m.group(0) + '</div>', html)
    html = todo_bq.sub(lambda m: '<div class="todo">' + m.group(0) + '</div>', html)

def inline(m):
    src = os.path.join(os.path.dirname(path), m.group(1))
    if not os.path.exists(src):
        return m.group(0)
    svg = open(src, encoding="utf-8").read()
    svg = svg[svg.index("<svg"):]                                 # drop any XML prolog
    svg = re.sub(r'\s(width|height)="[^"]*"', '', svg, count=2)   # let CSS size via viewBox
    return svg
html = re.sub(r'<img src="((?:\.\./)?(?:assets|figures)/[^"]+\.svg)"[^>]*>', inline, html)

open(path, "w", encoding="utf-8").write(html)
print(f"    draft notes: {n} {'removed' if final else 'marked'}; "
      f"svg inlined: {len(re.findall(r'<svg', html))}")
PY

  "$CHROME" --headless=new --disable-gpu --no-pdf-header-footer \
    --print-to-pdf="build/$doc.pdf" "file://$PWD/build/$doc.html" 2>/dev/null

  LIM=${LIMIT[$doc]:-0} python3 - "build/$doc.pdf" "$doc" <<'PY' || STATUS=1
import re, os, sys
pdf, doc = sys.argv[1], sys.argv[2]
n = len(re.findall(rb'/Type\s*/Page[^s]', open(pdf, 'rb').read()))
lim = int(os.environ.get("LIM", "0"))
if lim and n > lim:
    print(f"  {doc}.pdf -> {n} pages  ** OVER the {lim}-page limit **")
    sys.exit(1)
print(f"  {doc}.pdf -> {n} page(s)" + (f"  (limit {lim})" if lim else ""))
PY
done

[[ $FINAL -eq 1 ]] && echo "FINAL build: draft notes stripped." \
                   || echo "DRAFT build: draft notes visible. Use --final for submission."
exit $STATUS
