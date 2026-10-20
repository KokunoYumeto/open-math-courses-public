"""Build all twelve hash-bound course readers from editable sources."""
from pathlib import Path, PurePosixPath
from collections import Counter
import argparse, hashlib, json, re, sys
from bs4 import BeautifulSoup

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE/'renderer'))
from course_reader import render_markdown_math
from course_assets import read_unit_assets, figure_provenance, asset_output_path
from output_safety import fresh_directory, isolated_path

def sha(raw):return hashlib.sha256(raw).hexdigest()

def relative(value):
    if not isinstance(value,str) or not value or '\\' in value or ':' in value:
        raise ValueError('A canonical relative path is required')
    p=PurePosixPath(value)
    if p.is_absolute() or any(x in ('','.','..') for x in value.split('/')):
        raise ValueError('An input or output path escapes its declared root')
    return p

def input_bytes(root,row):
    path=root.joinpath(*relative(row['path']).parts)
    if not path.exists() and row.get('repository_path'):
        if root.parent.name!='courses' or not row['repository_path'].startswith('docs/assets/'):
            raise ValueError('Shared assets must be included in the source archive')
        site=root.parent.parent
        path=site.joinpath(*relative(row['repository_path'].removeprefix('docs/')).parts)
        if not path.resolve().is_relative_to((site/'assets').resolve()):
            raise ValueError('Shared asset is outside the declared repository asset directory')
    if any(p.is_symlink() for p in (path,*path.parents)):
        raise ValueError('Symbolic-link inputs are not accepted')
    raw=path.read_bytes()
    if sha(raw)!=row['sha256']:
        raise ValueError('Input hash differs: '+row['path'])
    return raw

def heads(text):
    return [(i,m[1],m[2]) for i,line in enumerate(text.splitlines(),1)
            if (m:=re.match(r'^(#{1,6})\s+(.+)$',line))]

def validate_math_environment_arguments(tex):
    if re.search(r'\\(?:lhook|joinrel)\b',tex):
        raise ValueError('Use the supported hookrightarrow macro for an injection arrow')
    if re.search(r'\\begin\{(?:gathered|aligned)\}\s*\[(?![tbc]\])',tex):
        raise ValueError('A leading bracket in gathered/aligned needs an empty group before it; otherwise it is consumed as a position argument')


def render_unit(unit,files,aliases,links,assets=None,verify_identity=True):
    raw=files[unit['source']]
    if sha(raw)!=unit['source_sha256']:
        raise ValueError('Lesson source does not match its catalogue')
    source=raw.decode('utf-8')
    projected=re.sub(r'\$\$.*?\$\$',lambda m:'\n\n'+m[0]+'\n\n',source,flags=re.S)
    if re.findall(r'\$\$.*?\$\$',source,re.S)!=re.findall(r'\$\$.*?\$\$',projected,re.S):
        raise ValueError('Display separation changed TeX content')
    before,after=heads(source),heads(projected)
    if [(h[1],h[2]) for h in before]!=[(h[1],h[2]) for h in after]:
        raise ValueError('Source heading order changed')
    lines={a[0]:b[0] for a,b in zip(before,after)}
    rows=aliases[unit['id']]['rows']
    if aliases[unit['id']]['source_sha256'].lower()!=sha(raw):
        raise ValueError('Heading aliases are not bound to this source')
    body=render_markdown_math(projected,local_links=links,
        heading_anchors=[{'line':lines[r['line']],'ids':r['ids']} for r in rows],
        footnote_bindings=unit.get('footnote_bindings',[]),assets=assets)
    if assets is not None:
        for row in assets.records:
            body=body.replace('src="'+asset_output_path(assets.course_id,assets.unit_id,row).split('/',2)[2]+'"','src="'+row['source']+'"')
    layout=files['reader-source/'+unit['layout']].decode('utf-8')
    if sha(layout.encode())!=unit['layout_sha256']:
        raise ValueError('Layout does not match its declared identity')
    if layout.count('{{LESSON_BODY}}')!=1:
        raise ValueError('Layout must contain exactly one lesson body slot')
    dom=BeautifulSoup(layout.replace('{{LESSON_BODY}}','\n'+body+'\n'),'html.parser')
    for math_node in dom.select('[data-tex]'):
        validate_math_environment_arguments(math_node['data-tex'])
    repaired=[]
    for pre in list(dom.select('article pre')):
        text=pre.get_text();digest=sha(text.encode())
        if digest not in unit['literal_math_paragraphs']:
            raise ValueError('Unexpected literal code paragraph in a mathematical lesson')
        fixed=BeautifulSoup(render_markdown_math(text,local_links=links),'html.parser')
        if fixed.select('pre,h1,h2,h3,h4,h5,h6'):
            raise ValueError('Mathematical paragraph changed heading structure')
        for node in list(fixed.contents):pre.insert_before(node)
        pre.decompose();repaired.append(digest)
    if Counter(repaired)!=Counter(unit['literal_math_paragraphs']):
        raise ValueError('The declared mathematical paragraph set differs')
    hs=dom.select_one('article.lesson').find_all(re.compile('^h[1-6]$'))
    if len(hs)!=len(before) or len(hs)!=unit['expected_headings']:
        raise ValueError('Heading coverage differs')
    ids=[e['id'] for e in dom.select('[id]')]
    if len(ids)!=len(set(ids)):raise ValueError('Duplicate rendered anchor')
    seen=set(ids)
    for row in unit['extra_anchors']:
        if row['id'] in seen:raise ValueError('Historical mathematical anchor collides')
        hs[row['before_heading']].insert_before(dom.new_tag('span',attrs={'id':row['id'],'class':'anchor-alias'}))
        seen.add(row['id'])
    if any(a['href'][1:] not in seen for a in dom.select('a[href^="#"]')):
        raise ValueError('Local proof link has no target')
    count=len(dom.select('article [data-tex]'))
    if count!=unit['expected_math']:raise ValueError('Formula coverage differs')
    result=str(dom).encode('utf-8')
    if verify_identity and sha(result)!=unit['reader_sha256']:
        raise ValueError('Rebuilt reader differs from the declared edition: '+unit['id'])
    return result,{'id':unit['id'],'source_sha256':sha(raw),'reader_sha256':sha(result),
                   'headings':len(hs),'formulas':count,'exact_current_edition':True}

def build(root,output):
    config=json.loads((HERE/'build-inputs.json').read_bytes())
    if config['schema']!='AG-AS-source-reader/v1':raise ValueError('Unsupported build catalogue')
    rows=config['files']
    if len({r['path'] for r in rows})!=len(rows):raise ValueError('Duplicate input path')
    files={r['path']:input_bytes(root,r) for r in rows}
    aliases=json.loads(files['heading-aliases.json'])
    components=json.loads(files['components.json'])['components']
    course_units={u['id']:u for u in json.loads(files['course.json'])['units']}
    results=[];readers={}
    for unit in config['units']:
        component,=[c for c in components if c['id']==unit['id']]
        if component['sha256'].lower()!=unit['source_sha256']:
            raise ValueError('Component identity differs from the source')
        source_lines=files[unit['source']].decode().splitlines(keepends=True)
        for span in component.get('independent_replacement_sections',[]):
            text=''.join(source_lines[span['first_line']-1:span['last_line']])
            if sha(text.encode())!=span['replacement_sha256']:
                raise ValueError('Credited mathematical passage differs: '+span['name'])
            if not span.get('writing_ai'):raise ValueError('Mathematical passage has no writing credit')
            for key in ('source_notes_authorship','proof_addition_authorship'):
                if key in span and not span[key].get('writing_ai'):
                    raise ValueError('Additional mathematical authorship is missing')
        raw,result=render_unit(unit,files,aliases,config['local_links'],read_unit_assets(root,'AG-AS',course_units[unit['id']]))
        readers['courses/AG-AS/'+unit['reader']]=raw;results.append(result)
    out=fresh_directory(output,protected=(root,));out.mkdir(parents=True,exist_ok=True)
    for row in rows:
        target=isolated_path(out.joinpath(*relative(row['output']).parts),protected=(root,))
        if not target.is_relative_to(out):raise ValueError('Output escapes its root')
        target.parent.mkdir(parents=True,exist_ok=True)
        if target.exists() and target.read_bytes()!=files[row['path']]:raise ValueError('Output collision')
        target.write_bytes(files[row['path']])
    for path,raw in readers.items():
        dest=out.joinpath(*relative(path).parts);dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(raw)
    catalogue=out/'courses/AG-AS/reader-source/build-inputs.json'
    catalogue.parent.mkdir(parents=True,exist_ok=True);catalogue.write_bytes((HERE/'build-inputs.json').read_bytes())
    report={'schema':'AG-AS-reader-build/v1','units':results,'input_files_checked':len(rows),
            'primary_and_additional_mathematical_credits_preserved':True,
            'mathematical_correctness_or_independent_review_certified':False}
    (out/'build-result.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    return report

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,required=True,help='A fresh empty output directory')
    args=parser.parse_args()
    print(json.dumps(build(HERE.parent,args.output),indent=2))
