"""Rebuild the analytic preparation, division, curve and exercise readings with Python 3 and Pandoc."""
from pathlib import Path
import subprocess,json,re
from reader_math_scrollers import scroll_math
root=Path(__file__).resolve().parents[1]
readings=json.loads((root/"readings.json").read_text(encoding="utf-8"))["readings"]
sibling_readers={Path(entry["source"]).name:entry["reader"] for entry in readings}

def normalize_links(source):
    def destination(match):
        target=match[1]
        path,mark,fragment=target.partition("#")
        # Bare sibling reading links open the reader; explicit source links stay editable.
        if path in sibling_readers:
            path=sibling_readers[path]
        elif path.startswith("../"):
            path=path[3:]
        return "]("+path+mark+fragment+")"
    return re.sub(r"\]\(([^\s)]+)\)",destination,source)

for entry in readings:
    output=root/entry["reader"]
    source=(root/entry["source"]).read_text(encoding="utf-8")
    normalized=normalize_links(source)
    normalized=re.sub(r'\\tag\{([^}]+)\}',lambda m:r'\qquad\text{('+m[1]+')}',normalized)
    run=subprocess.run(["pandoc","--from=markdown+tex_math_single_backslash","--to=html5","--mathml","--template",str(root/"build/reader-template.html"),"--metadata","title="+entry["title"],"--output",str(output)],input=normalized,capture_output=True,text=True,encoding="utf-8")
    if run.returncode or run.stderr.strip():raise RuntimeError(run.stderr)
    output.write_text(scroll_math(output.read_text(encoding="utf-8")),encoding="utf-8")
