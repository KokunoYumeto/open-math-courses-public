"""Rebuild selected sources and exact prerequisite routes using local inputs."""
from pathlib import Path
import hashlib
import json
import re
import subprocess
from renderer_core import render
from reader_math_scrollers import scroll_math


def rebuild(root):
    rows=json.loads((root/'readings.json').read_text(encoding='utf-8'))['readings']
    for entry in rows:
        data=(root/entry['source']).read_bytes()
        if 'links' not in entry:
            template=(root/'build/reader-template.html').read_text(encoding='utf-8')
            if Path(entry['reader']).parent!=Path('.'):
                template=template.replace('href="reader.css"','href="../reader.css"').replace('href="index.html"','href="../index.html"')
            temp=root/'build/current-template.html'
            temp.write_text(template,encoding='utf-8')
            source=re.sub(r'\\tag\{([^}]+)\}',lambda m:r'\qquad\text{('+m[1]+')}',data.decode('utf-8'))
            try:
                run=subprocess.run(['pandoc','--from=markdown+tex_math_single_backslash','--to=html5',
                    '--mathml','--template',str(temp),'--metadata','title='+entry['title']],
                    input=source,capture_output=True,text=True,encoding='utf-8')
                if run.returncode or run.stderr.strip():
                    raise RuntimeError(run.stderr)
                (root/entry['reader']).write_text(scroll_math(run.stdout),encoding='utf-8')
            finally:
                temp.unlink()
            continue
        if entry.get('sha256') and hashlib.sha256(data).hexdigest()!=entry['sha256']:
            raise ValueError('Selected source changed: '+entry['source'])
        page,count=render(data.decode('utf-8'),entry['title'],entry.get('links',{}))
        if entry.get('math_expressions') is not None and count!=entry['math_expressions']:
            raise ValueError('Formula count changed')
        page=page.replace('>Sheaf proof readings</a>','>Constructible duality and infinite twists</a>')
        if Path(entry['reader']).parent!=Path('.'):
            page=page.replace('href="reader.css"','href="../reader.css"').replace('href="index.html"','href="../index.html"')
        output=root/entry['reader']
        output.parent.mkdir(parents=True,exist_ok=True)
        output.write_bytes(scroll_math(page).encode('utf-8'))
    return len(rows)


if __name__=='__main__':
    print(json.dumps({'readers':rebuild(Path(__file__).resolve().parents[1])}))
