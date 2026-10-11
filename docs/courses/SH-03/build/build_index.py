"""Build the course reading guide from src/index.md. Requires Python and Pandoc."""
from pathlib import Path
import json, posixpath, subprocess
from urllib.parse import urlsplit, urlunsplit

ROOT=Path(__file__).resolve().parents[1]
source=(ROOT/'src/index.md').read_text(encoding='utf-8')
document=json.loads(subprocess.run(['pandoc','--from','markdown','--to','json'],
                    input=source,capture_output=True,text=True,encoding='utf-8',check=True).stdout)
def project_links(value):
    if isinstance(value,dict):
        if value.get('t') in ('Link','Image'):
            target=value['c'][-1][0];url=urlsplit(target)
            if url.path and not url.scheme and not url.netloc:
                value['c'][-1][0]=urlunsplit(('', '', posixpath.normpath(posixpath.join('src',url.path)),url.query,url.fragment))
        for child in value.values():project_links(child)
    elif isinstance(value,list):
        for child in value:project_links(child)
project_links(document)
body=subprocess.run(['pandoc','--from','json','--to','html5','--wrap','none'],
                    input=json.dumps(document),capture_output=True,text=True,encoding='utf-8',check=True).stdout
head='''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Constructible and perverse sheaves · Open Mathematics Courses</title><link rel="stylesheet" href="../../assets/site.css"></head>
<body><header class="site-header"><div class="header-inner"><a class="brand" href="../../index.html">Open Mathematics Courses</a><nav><a href="../../licensing.html">Licensing</a></nav></div></header><main id="main">
'''
(ROOT/'index.html').write_text(head+body+'</main></body></html>\n',encoding='utf-8',newline='\n')
print('Course reading guide built from src/index.md.')
