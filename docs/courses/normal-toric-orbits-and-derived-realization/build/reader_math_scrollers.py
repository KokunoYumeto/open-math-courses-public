"""Add an overflow container without changing any native MathML body."""
import re
def scroll_math(text):
    return re.sub(r'(<math\b[^>]*\bdisplay="(block|inline)"[^>]*>.*?</math>)',
                  lambda m:'<span class="math '+('display' if m[2]=='block' else 'inline')+'">'+m[1]+'</span>',
                  text,flags=re.S)
