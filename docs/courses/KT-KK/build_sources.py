from pathlib import Path
import subprocess
import json
import tempfile
import re
r=Path(__file__).resolve().parent
course=json.loads((r/'course.json').read_text(encoding='utf-8'))
lessons=[r/u['source'] for u in course['units']+course.get('supplements',[])]
assert len(lessons)==len(set(lessons)), 'Duplicate source'
args=['pandoc','--eol=lf','--from=markdown+tex_math_single_backslash-implicit_figures','--to=latex','--standalone','--variable=geometry:margin=25mm','--variable=fontsize:11pt']
def normalize_print_links(path):
    text=path.read_text(encoding='utf-8')
    labels=set(re.findall(r'\\label\{([^}]+)\}',text))
    def resolve(match):
        target=match.group(1)
        converted=re.sub(r'^\d+-','',target)
        if target not in labels and converted in labels:
            return r'\hyperref['+converted+']'
        return match.group(0)
    text=re.sub(r'\\hyperref\[([^]]+)\]',resolve,text)
    path.write_text(text,encoding='utf-8',newline='\n')
for p in lessons:
    subprocess.run(args+[p.relative_to(r).as_posix(),'-o',p.with_suffix('.tex').relative_to(r).as_posix()],cwd=r,check=True)
    normalize_print_links(p.with_suffix('.tex'))
with tempfile.TemporaryDirectory() as temporary:
    combined=Path(temporary)/'course.md'
    combined.write_text('\n\n\\newpage\n\n'.join(p.read_text(encoding='utf-8') for p in lessons),encoding='utf-8',newline='\n')
    subprocess.run(args+['--toc','--metadata=title:Kasparov’s KK-theory',f'--metadata=subtitle:{len(course["units"])} draft lessons and {len(course.get("supplements", []))} proof companions',str(combined),'-o','KT-KK.tex'],cwd=r,check=True)
    normalize_print_links(r/'KT-KK.tex')
