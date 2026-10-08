"""Rebuild all readers, the collected Markdown and the download with Python and Pandoc."""
from pathlib import Path
import json, re, subprocess, zipfile
from reader_math_scrollers import scroll_math
from reader_empty_sets import repair_empty_set_glyphs

root = Path(__file__).resolve().parents[1]
readings = json.loads((root/'readings.json').read_text(encoding='utf8'))['readings']
sources = []
for entry in readings:
    source = (root/entry['source']).read_text(encoding='utf8')
    sources.append(source.strip())
    normalized = re.sub(r'(\]\()\.\./', r'\1', source)
    normalized = re.sub(r'\\tag\{([^}]+)\}', lambda m:r'\qquad\text{('+m[1]+')}', normalized)
    run = subprocess.run(['pandoc','--from=markdown+tex_math_single_backslash','--to=html5','--mathml',
        '--template',str(root/'build/reader-template.html'),'--metadata','title='+entry['title']],
        input=normalized,capture_output=True,text=True,encoding='utf8',check=True)
    if run.stderr.strip(): raise RuntimeError(run.stderr)
    rendered = scroll_math(repair_empty_set_glyphs(run.stdout))
    rendered = re.sub(r'(<table\b.*?</table>)',r'<div class="table-scroll" tabindex="0" role="region" aria-label="Prerequisite comparison">\1</div>',rendered,flags=re.S)
    (root/entry['reader']).write_text(rendered,encoding='utf8')
(root/'reading.md').write_text('\n\n\n'.join(sources)+'\n',encoding='utf8')
members = {'LICENSE.txt','PROVENANCE.json','README.md','reader.css','reading.md','readings.json',
    'build/build_reader.py','build/reader-template.html','build/reader_math_scrollers.py','build/reader_empty_sets.py'}
members.update(entry['source'] for entry in readings)
members.update(entry['reader'] for entry in readings)
with zipfile.ZipFile(root/'nearby-cycles-reading.zip','w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as archive:
    for name in sorted(members):
        info=zipfile.ZipInfo(name,date_time=(2026,10,5,0,0,0))
        info.compress_type=zipfile.ZIP_DEFLATED
        info.external_attr=0o100644<<16
        archive.writestr(info,(root/name).read_bytes())
print(json.dumps({'readers':len(readings),'zip_members':len(members)}))
