"""Rebuild the the attributed readings with Python 3 and Pandoc."""
from pathlib import Path
import subprocess,json,re
from reader_math_scrollers import scroll_math
from reading_link_routes import project_parent_links
root=Path(__file__).resolve().parents[1]
for entry in json.loads((root/"readings.json").read_text(encoding="utf-8"))["readings"]:
    output=root/entry["reader"]
    source=(root/entry["source"]).read_text(encoding="utf-8")
    normalized=project_parent_links(source,entry["source"],entry["reader"])
    for source_href, reader_href in entry.get("reader_links", {}).items():
        projected=project_parent_links("]("+source_href+")",entry["source"],entry["reader"])[2:-1]
        normalized=normalized.replace("]("+projected+")", "]("+reader_href+")")
    normalized=re.sub(r'\\tag\{([^}]+)\}',lambda m:r'\qquad\text{('+m[1]+')}',normalized)
    run=subprocess.run(["pandoc","--from=markdown+tex_math_single_backslash","--to=html5","--mathml","--template",str(root/"build/reader-template.html"),"--metadata","title="+entry["title"],"--output",str(output)],input=normalized,capture_output=True,text=True,encoding="utf-8")
    if run.returncode or run.stderr.strip():raise RuntimeError(run.stderr)
    output.write_text(scroll_math(output.read_text(encoding="utf-8")),encoding="utf-8")
