"""Contain native MathML and keep adjacent punctuation with inline formulas."""
import re
def scroll_math(text):
    def wrap(m):
        body,kind,punct=m[1],m[2],m[3] or ''
        if kind=='block' and r'\downarrow\scriptstyle\sim' in body:
            count=body.count(r'\downarrow\scriptstyle\sim')
            body,n=re.subn(r'(<mo>↓</mo>)\s*(<mo>∼</mo>)',r'\1<mstyle scriptlevel="1" displaystyle="false">\2</mstyle>',body)
            if n!=count:raise ValueError('Explicit script-size arrow labels were not preserved')
        return '<span class="math '+('display' if kind=='block' else 'inline')+'">'+body+(punct if kind=='inline' else '')+'</span>'+(punct if kind=='block' else '')
    return re.sub(r'(<math\b[^>]*\bdisplay="(block|inline)"[^>]*>.*?</math>)([.,;:!?]?)',wrap,text,flags=re.S)
