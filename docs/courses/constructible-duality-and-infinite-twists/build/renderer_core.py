"""Rebuild the frozen sheaf readings. Requires Python, Pandoc, BeautifulSoup.

No network access, producer workspaces or external mathematical sources are used.
Run as build/build_reader.py inside the downloaded course directory.
"""
from pathlib import Path
import hashlib
import html
import json
import re
import subprocess
from bs4 import BeautifulSoup


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def walk(value, visit):
    if isinstance(value, dict):
        visit(value)
        for child in value.values():
            walk(child, visit)
    elif isinstance(value, list):
        for child in value:
            walk(child, visit)


def convert(args, text):
    result = subprocess.run(['pandoc', *args], input=text, text=True,
                            encoding='utf-8', capture_output=True)
    if result.returncode or result.stderr.strip():
        raise RuntimeError(result.stderr)
    return result.stdout


def render(body, title, links):
    doc = json.loads(convert(['-f','markdown+tex_math_single_backslash','-t','json'], body))
    count = 0
    def amend(node):
        nonlocal count
        if node.get('t') in ('Link','Image'):
            url = node['c'][-1][0]
            node['c'][-1][0] = links.get(url, url)
        elif node.get('t') in ('RawBlock','RawInline') and node['c'][0]=='html':
            fragment = BeautifulSoup(node['c'][1], 'html.parser')
            for img in fragment.find_all('img',src=True):
                img['src'] = links.get(img['src'],img['src'])
            node['c'][1] = str(fragment)
        elif node.get('t')=='Math':
            count += 1
            text = re.sub(r'\\tag\{([^}]+)\}',lambda m:r'\qquad\text{('+m[1]+')}',node['c'][1])
            text = text.replace(r'\varprojlim',r'\underset{\leftarrow}{\lim}').replace(r'\varinjlim',r'\underset{\rightarrow}{\lim}')
            text = re.sub(r'\{\\rm\s+([^{}]*)\}',lambda m:r'{\mathrm{'+m[1]+'}}',text)
            node['c'][1] = text.replace(r'\hbox',r'\text').replace('``',r'\text{“}').replace("''",r'\text{”}')
    walk(doc,amend)
    rendered = convert(['-f','json','-t','html5','--mathml'],json.dumps(doc))
    page = '<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+html.escape(title)+'</title><link rel="stylesheet" href="reader.css"></head><body><nav><a href="index.html">Sheaf proof readings</a></nav><main>'+rendered+'</main></body></html>'
    soup = BeautifulSoup(page,'html.parser')
    # Pandoc can collapse an explicit long implication to the short glyph.
    # Repair only unambiguous formulas; do not guess inside mixed-arrow formulas.
    for formula in soup.find_all('math'):
        annotation = formula.find('annotation', attrs={'encoding':'application/x-tex'})
        tex = annotation.get_text() if annotation else ''
        if r'\longrightarrow' in tex:
            commands = re.findall(r'\\(longrightarrow|rightarrow|to|xrightarrow)(?![A-Za-z])', tex)
            operators = [m for m in formula.find_all('mo') if m.get_text() in ('→','⟶')]
            if len(commands) != len(operators):
                raise ValueError('Long-arrow/source correspondence is ambiguous')
            for command, operator in zip(commands, operators):
                if command == 'longrightarrow':
                    operator.string = '⟶'
                    operator['stretchy'] = 'false'
                    operator['data-source-command'] = command
        long_count = len(re.findall(r'\\Longrightarrow\b', tex))
        short = formula.find_all('mo', string='⇒')
        if (long_count and len(short)==long_count
                and not re.search(r'\\(?:Rightarrow|implies)\b|⇒', tex)):
            for arrow in short:
                arrow.string = '⟹'
        long_both = len(re.findall(r'\\Longleftrightarrow\b', tex))
        short_both = formula.find_all('mo', string='⇔')
        if (long_both and len(short_both)==long_both
                and not re.search(r'\\(?:Leftrightarrow|iff)\b|⇔', tex)):
            for arrow in short_both:
                arrow.string = '⟺'
        map_commands = re.findall(r'\\(longmapsto|mapsto)(?![A-Za-z])', tex)
        map_operators = [m for m in formula.find_all('mo') if m.get_text() in ('↦','⟼')]
        if 'longmapsto' in map_commands:
            if len(map_commands) != len(map_operators):
                raise ValueError('Mapsto/source correspondence is ambiguous')
            for command, operator in zip(map_commands, map_operators):
                if command == 'longmapsto':
                    operator.string = '⟼'
                    operator['stretchy'] = 'false'
                    operator['data-source-command'] = command
    # Keep an inline coefficient and its immediate module suffix together,
    # without suppressing ordinary prose wrapping outside this small phrase.
    for formula in soup.find_all('math', display='inline'):
        tail = formula.next_sibling
        if isinstance(tail, str):
            suffix = re.match(r'-modules?\b', tail)
            if suffix:
                wrapper = soup.new_tag('span', attrs={'class':'math-with-suffix',
                    'style':'white-space:nowrap'})
                formula.wrap(wrapper)
                wrapper.append(suffix[0])
                tail.replace_with(str(tail)[len(suffix[0]):])
    for heading in soup.find_all(re.compile('^h[1-6]$')):
        identity = re.match(r'(SH02-[A-Z0-9-]+)',heading.get_text())
        if identity and not soup.find(id=identity[1]):
            heading.insert_before(soup.new_tag('span',id=identity[1]))
    if len(soup.find_all('math')) != count or soup.find('merror'):
        raise ValueError('MathML projection failed: '+title)
    return str(soup), count


def rebuild(root):
    manifest = json.loads((root/'build/manifest.json').read_text(encoding='utf-8'))
    def local(name):
        path = (root/name).resolve()
        if not path.is_relative_to(root.resolve()):
            raise ValueError('Build input escapes course directory')
        return path
    for row in manifest['readings']+manifest['assets']:
        if digest(local(row['source'])) != row['sha256']:
            raise ValueError('Frozen source differs: '+row['source'])
    expressions = 0
    for row in manifest['readings']:
        result, count = render(local(row['source']).read_text(encoding='utf-8'),row['title'],row['links'])
        if count != row['math_expressions']:
            raise ValueError('Unexpected formula count: '+row['reader'])
        local(row['reader']).write_bytes(result.encode('utf-8'))
        expressions += count
    return {'readers':len(manifest['readings']),'math_expressions':expressions}


if __name__=='__main__':
    print(json.dumps(rebuild(Path(__file__).resolve().parents[1])))
