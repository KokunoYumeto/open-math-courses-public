"""Build the selected mathematical readings using Python 3 and Pandoc."""
from pathlib import Path
import argparse, json, re, subprocess
from bs4 import BeautifulSoup

root = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser()
parser.add_argument('--pandoc', default='pandoc', help='Pandoc executable or absolute path')
args = parser.parse_args()

def render_group(value):
    pieces=[];i=0
    while i<len(value):
        if value[i]=='\\':
            match=re.match(r'\\(?:[A-Za-z]+|[\s\S])',value[i:]);token=match[0];pieces.append(token);i+=len(token)
        elif value[i]=='{':
            depth=1;j=i+1
            while j<len(value) and depth:
                if value[j]=='\\':
                    match=re.match(r'\\(?:[A-Za-z]+|[\s\S])',value[j:]);j+=len(match[0]);continue
                if value[j]=='{':depth+=1
                elif value[j]=='}':depth-=1
                j+=1
            assert depth==0,value
            pieces.append('{'+render_group(value[i+1:j-1])+'}');i=j
        else:pieces.append(value[i]);i+=1
    if r'\over' in pieces or r'\choose' in pieces:
        positions=[j for j,x in enumerate(pieces) if x in (r'\over',r'\choose')]
        assert len(positions)==1,value
        j=positions[0];command=r'\frac' if pieces[j]==r'\over' else r'\binom'
        return command+'{'+''.join(pieces[:j])+'}{'+''.join(pieces[j+1:])+'}'
    if r'\rm' in pieces:
        j=pieces.index(r'\rm')
        return ''.join(pieces[:j])+r'\mathrm{'+''.join(pieces[j+1:]).lstrip()+'}'
    return ''.join(pieces)

def display_math(match):
    value=match[0];body=value[2:-2]
    body=render_group(body).replace(r'\hbox',r'\text').replace(r'\begin{split}',r'\begin{aligned}').replace(r'\end{split}',r'\end{aligned}')
    gap_number=iter(range(10000))
    body=re.sub(r'\\hspace\{[^}]+\}',lambda m:r'\text{AN03HSPACE'+str(next(gap_number))+'}',body)
    body=re.sub(r'\\tag\{([^}]+)\}',lambda m:r'\qquad\text{('+m[1]+')}',body)
    return value[:2]+body+value[-2:]

for entry in [r for r in json.loads((root / 'readings.json').read_text(encoding='utf-8'))['readings'] if r.get('HTML_source_equality_claimed',False)]:
    source = (root / entry['source']).read_text(encoding='utf-8')
    display_source = re.sub(r'\\\([\s\S]*?\\\)|\\\[[\s\S]*?\\\]', display_math, source)
    run = subprocess.run([args.pandoc, '--from=markdown+tex_math_single_backslash', '--to=html5',
                          '--mathml', '--template', str(root / 'build/reader-template.html'),
                          '--metadata', 'title=' + entry['title']],
                         input=display_source, text=True, encoding='utf-8', capture_output=True)
    if run.returncode or run.stderr.strip():
        raise RuntimeError(run.stderr)
    soup = BeautifulSoup(run.stdout, 'html.parser')
    
    original_maths=re.findall(r'\\\([\s\S]*?\\\)|\\\[[\s\S]*?\\\]',source)
    rendered_maths=soup.find_all('math')
    assert len(original_maths)==len(rendered_maths), (entry['id'],len(original_maths),len(rendered_maths))
    for original, mathematical in zip(original_maths, rendered_maths):
        mathematical.find('annotation').string=original[2:-2]
        widths=re.findall(r'\\hspace\{([^}]+)\}',original)
        for gap in mathematical.find_all('mtext'):
            label=gap.get_text()
            if re.fullmatch('AN03HSPACE[0-9]+',label):
                gap.replace_with(soup.new_tag('mspace',width=widths[int(label[10:])] ))
    for mathematical in rendered_maths:
        wrapper=soup.new_tag('span',attrs={'class':['math','display' if mathematical.get('display')=='block' else 'inline']})
        mathematical.wrap(wrapper)
    aside=soup.find('aside'); aside.clear()
    aside.append('Component license: '+entry['license']+'. Original contributor notices remain in the source. OpenAI Codex, GPT-6.1 Sol, Ultra effort; author self-checking, with no independent-review claim. ')
    notice_link=soup.new_tag('a',href='component-notices/SELECTION_TITLE_PAGE.md'); notice_link.string='Authors and component terms'; aside.append(notice_link)
    nav = soup.find('nav')
    nav.clear()
    for label, href in [('Bott and Weyl traces','index.html'),('Learn first','supporting-proofs.html'),('Markdown',entry['source']),('TeX',entry.get('tex','tex/'+Path(entry['source']).stem+'.tex')),('PDF',entry.get('pdf','pdf/'+Path(entry['source']).stem+'.pdf')),('Credits and terms','credits.html')]:
        if href is None: continue
        if list(nav.children): nav.append(' · ')
        link = soup.new_tag('a', href=href); link.string=label; nav.append(link)
    source_headings = re.findall(r'^#{1,6} (.+)$', source, re.M)
    html_headings = soup.article.find_all(re.compile('^h[1-6]$'))
    assert len(source_headings)==len(html_headings), (entry['id'],len(source_headings),len(html_headings))
    existing_ids={x.get('id') for x in soup.find_all(id=True)}
    for record in entry.get('heading_aliases',[]):
        positions=[i for i,value in enumerate(source_headings) if re.sub(r'\s*\{#[^}]+\}\s*$','',value)==record['heading']]
        if not positions: continue
        heading=html_headings[positions[0]]
        for identity in record['ids']:
            if identity in existing_ids: continue
            alias=soup.new_tag('span',id=identity); heading.insert_before(alias); existing_ids.add(identity)
    for element in soup.find_all(['a', 'img']):
        attr = 'src' if element.name == 'img' else 'href'
        value = element.get(attr)
        if not value or value.startswith(('http:', 'https:', 'mailto:', '#')):
            continue
        if value.startswith('../figures/'):
            value = value[3:]
        elif value.startswith('../src/'):
            value=value[7:].replace('.md','.html')
        elif value.startswith('../supplements/'):
            value=value[3:]
        elif re.match(r'^[^/]+\.md(?:#|$)', value):
            value = re.sub(r'\.md(?=#|$)', '.html', value)
        element[attr] = value
    routes=json.loads((root/'link-routes.json').read_text(encoding='utf-8'))
    for link in soup.find_all('a',href=True):
        value=link['href'];base,sep,fragment=value.partition('#')
        if base in routes:
            mapped=routes[base]
            link['href']=mapped+('#'+fragment if sep and '#' not in mapped else '')
    contents=soup.new_tag('details')
    summary=soup.new_tag('summary');summary.string='Contents';contents.append(summary)
    items=soup.new_tag('ul')
    for heading in soup.article.find_all(['h2','h3']):
        item=soup.new_tag('li');link=soup.new_tag('a',href='#'+heading['id'])
        link.string=heading.get_text(' ',strip=True);item.append(link);items.append(item)
    contents.append(items);soup.article.insert_before(contents)
    # Stable equation anchors make the unchanged labelled formulas directly linkable.
    for mathematical in soup.find_all('math'):
        annotation=mathematical.find('annotation')
        tag=re.search(r'\\tag\{([^}]+)\}',annotation.get_text() if annotation else '')
        if tag:
            mathematical['id']='eq-'+tag[1]
    (root / entry['reader']).write_text(str(soup), encoding='utf-8')
