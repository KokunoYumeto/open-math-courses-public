"""Contain native MathML and keep adjacent punctuation with inline formulas."""
import re

def preserve_long_arrows(body):
    """Restore explicit long right arrows from Pandoc's retained TeX.

    Check every right-arrow operator in each affected formula; unsupported
    correspondences fail the build instead of changing a different operator.
    """
    annotation = re.search(r'<annotation\b[^>]*>(.*?)</annotation>',body,re.S)
    if annotation is None or r'\longrightarrow' not in annotation[1]:
        return body
    commands = re.findall(r'\\(longrightarrow|rightarrow|to|xrightarrow)(?![A-Za-z])',annotation[1])
    presentation = body[:annotation.start()]
    operators = list(re.finditer(r'<mo(?:\s[^>]*)?>[→⟶]</mo>',presentation))
    if len(commands) != len(operators):
        raise ValueError('Explicit long-arrow/source correspondence is ambiguous')
    for command, operator in reversed(list(zip(commands,operators))):
        if command == 'longrightarrow':
            presentation = (presentation[:operator.start()]
                            + '<mo stretchy="false" data-source-command="longrightarrow">⟶</mo>'
                            + presentation[operator.end():])
    return presentation + body[annotation.start():]

def scroll_math(text):
    def wrap(m):
        body,kind,punct=m[1],m[2],m[3] or ''
        body=preserve_long_arrows(body)
        if kind=='block' and r'\downarrow\scriptstyle\sim' in body:
            count=body.count(r'\downarrow\scriptstyle\sim')
            body,n=re.subn(r'(<mo>↓</mo>)\s*(<mo>∼</mo>)',r'\1<mstyle scriptlevel="1" displaystyle="false">\2</mstyle>',body)
            if n!=count:raise ValueError('Explicit script-size arrow labels were not preserved')
        return '<span class="math '+('display' if kind=='block' else 'inline')+'">'+body+(punct if kind=='inline' else '')+'</span>'+(punct if kind=='block' else '')
    return re.sub(r'(<math\b[^>]*\bdisplay="(block|inline)"[^>]*>.*?</math>)([.,;:!?]?)',wrap,text,flags=re.S)
