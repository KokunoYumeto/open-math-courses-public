"""Narrow, source-annotation-bound empty-set presentation repair."""
import re
import html

def repair_empty_set_glyphs(document, report=None):
    """Correct only diameter glyphs paired with an explicit empty-set command.

    Require every relevant source token to be an explicit empty-set command
    and its count to match the MathML symbols. Mixed meanings fail closed.
    Keep TeX annotations, tags, attributes and all other bytes unchanged.
    """
    formula_index = -1
    def amend(match):
        nonlocal formula_index
        formula_index += 1
        original = match[0]
        annotations = list(re.finditer(r'<annotation\b[^>]*\bencoding=[\"\']application/x-tex[\"\'][^>]*>(.*?)</annotation>', original, re.S))
        if len(annotations) != 1:
            return original
        annotation = annotations[0]
        tex = html.unescape(annotation[1])
        if not re.search(r'\\(?:varnothing|emptyset)(?![A-Za-z])', tex):
            return original
        presentation = original[:annotation.start()]
        if '\u2300' not in html.unescape(presentation):
            return original
        tokens = list(re.finditer(r'\\(varnothing|emptyset|diameter)(?![A-Za-z])|[\u2205\u2300]', tex))
        symbols = list(re.finditer(r'<(mi|mo)\b[^>]*>\s*(\u2205|\u2300|&#(?:8709|8960);|&#x(?:2205|2300);)\s*</\1>', presentation, re.I))
        # TeX constructions such as overset can reorder their arguments in
        # MathML. With mixed symbol meanings, positional matching alone is not
        # evidence of correspondence. A reader build must stop for inspection.
        if any(t[1] not in ('varnothing', 'emptyset') for t in tokens):
            raise ValueError('Mixed empty-set/diameter source correspondence is ambiguous at formula '+str(formula_index))
        if len(tokens) != len(symbols):
            raise ValueError('Empty-set/source correspondence is ambiguous at formula '+str(formula_index))
        changes = []
        for token, symbol in zip(tokens, symbols):
            command = token[1] or token[0]
            value = html.unescape(symbol[2])
            if command in ('varnothing','emptyset') and value == '\u2300':
                changes.append((symbol.start(2), symbol.end(2), command, symbol[2]))
        for start, end, _, _ in reversed(changes):
            presentation = presentation[:start]+'\u2205'+presentation[end:]
        if changes and report is not None:
            report.append({'formula_index_zero_based':formula_index, 'tex':tex,
                           'changes':[{'command':command,'before':old,'after':'\u2205'} for _,_,command,old in changes]})
        return presentation+original[annotation.start():]
    return re.sub(r'<math\b[^>]*>.*?</math>', amend, document, flags=re.S)

