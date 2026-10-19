"""CommonMark and editable TeX rendering for Hilbert and Picard schemes.

Original programme build software: CC0 1.0 Universal.
"""
from __future__ import annotations
import hashlib
import html
import json
import re
from html.parser import HTMLParser
from pathlib import Path, PurePosixPath, PureWindowsPath
from urllib.parse import parse_qsl, unquote, urlsplit
from markdown_it import MarkdownIt
ID = re.compile('[A-Za-z0-9][A-Za-z0-9_.-]{0,100}\\Z')
PRIVATE_PATH = re.compile('(?:\\b[A-Za-z]:[\\\\/]|\\b[A-Za-z]:(?!//)[^\\s\\"<>]*[\\\\/]|\\b[A-Za-z]:[\\w-]+\\.[\\w-]+\\b|file://|/(?:Users|home)/|\\\\\\\\[A-Za-z0-9_.-]+\\\\)', re.I)
WEB_URL = re.compile('\\bhttps?://[^\\s<>\\"\']+', re.I)
LOCAL_URL_PAYLOAD = re.compile('(?:\\b[A-Za-z]:[\\\\/]|file://|\\\\)', re.I)
MATH_UNEQUIVOCAL_PATH = re.compile('(?:\\bfile:[\\\\/]|/(?:Users|home)/)', re.I)
MATH_UNC_HEAD = re.compile('(?<!\\\\)\\\\\\\\(?!\\\\)([A-Za-z0-9_.-]+)\\\\([A-Za-z]*)')
MATH_DRIVE_PATH = re.compile('(?:\\b[A-Za-z]:/|\\b[A-Za-z]:[^\\s{}$<>]*\\.[A-Za-z0-9]{1,12}\\b)', re.I)
MATH_DRIVE_START = re.compile('\\b[A-Za-z]:([A-Za-z0-9_.-]*)\\\\')
TEX_CONTROL_WORD = re.compile('\\\\([A-Za-z]+)')
TEX_MAP_OPERATOR = re.compile('(?:to|mapsto|.*arrow)\\Z')
TEX_RELATIONS = set('in ni not notin le leq ge geq neq ne equiv cong sim simeq subset subseteq supset supseteq parallel perp'.split())
TEX_RELATIONS |= set('prec succ preceq succeq ll gg approx propto mid vdash dashv models lhd rhd unlhd unrhd sqsubset sqsubseteq sqsupset sqsupseteq lesssim gtrsim leqslant geqslant subsetneq supsetneq'.split())
TEX_MATH_LEXEMES = set('mathcal mathbb mathfrak mathscr mathrm mathsf mathtt mathbf mathit operatorname to rightarrow leftarrow mapsto hookrightarrow longrightarrow longleftarrow longmapsto colon quad qquad Delta Gamma Sigma Omega Hom Spec ell overline underline Ker Im wedge rho widehat widetilde hat tilde bar alpha beta gamma delta epsilon varepsilon zeta eta theta vartheta iota kappa lambda mu nu xi omicron pi varpi varrho sigma varsigma tau upsilon phi varphi chi psi omega Theta Lambda Xi Pi Upsilon Phi Psi infty sum prod coprod int iint iiint oint bigcap bigcup bigoplus bigotimes bigvee bigwedge sup inf lim limsup liminf max min exists forall langle rangle lceil rceil lfloor rfloor left right middle sin cos tan cot sinh cosh tanh log ln exp det dim ker hom arg deg Pr times cdot circ otimes oplus odot ast star cup cap vee pm mp div xrightarrow xleftarrow setminus dot ddot rtimes ltimes boxtimes boxplus boxminus boxdot ominus oslash uplus sqcup sqcap bullet amalg'.split()) | TEX_RELATIONS

def public_web_url(value: str, *, _depth=0) -> bool:
    if _depth > 8:
        return False
    try:
        parsed = urlsplit(value)
        decoded = unquote(value)
        if parsed.scheme.lower() not in {'http', 'https'} or not parsed.hostname or parsed.username is not None or (parsed.password is not None) or any((char.isspace() or ord(char) < 32 for char in value)) or any((char in parsed.netloc for char in '\\%')) or LOCAL_URL_PAYLOAD.search(decoded) or any((private_reference(part, _depth=_depth + 1) for component in (parsed.query, parsed.fragment) for pair in parse_qsl(component, keep_blank_values=True, max_num_fields=1024) for part in pair)):
            return False
        parsed.port
        return not any((ord(char) < 32 or ord(char) == 127 for char in decoded))
    except ValueError:
        return False

def private_reference(value: str, *, _depth=0, _pattern=PRIVATE_PATH) -> bool:
    invalid_url = False

    def scrub(match):
        nonlocal invalid_url
        candidate = match.group().rstrip('.,;:!?)]}')
        if public_web_url(candidate, _depth=_depth):
            return ' '
        invalid_url = True
        return match.group()
    scrubbed = WEB_URL.sub(scrub, value)
    return invalid_url or bool(_pattern.search(scrubbed))

def math_private_reference(value: str) -> bool:
    if private_reference(value, _pattern=MATH_UNEQUIVOCAL_PATH):
        return True
    if private_reference(value, _pattern=MATH_DRIVE_PATH):
        return True
    scan = WEB_URL.sub(' ', value)
    for unc in MATH_UNC_HEAD.finditer(scan):
        host, control = unc.groups()
        following = scan[unc.end():unc.end() + 1]
        row_end = control == 'end' and bool(re.match('\\{(?:matrix|pmatrix|bmatrix|Bmatrix|vmatrix|Vmatrix|smallmatrix|aligned|alignedat|gathered|cases|array)\\}', scan[unc.end():]))
        operand = TEX_CONTROL_WORD.match(scan, unc.end())
        relation_operand = following.isspace() or following.isdigit() or (operand is not None and operand.group(1) in TEX_MATH_LEXEMES and (scan[operand.end():operand.end() + 1] in ('_', '^', '{', ' ', '\\', '')))
        row_syntax = control in TEX_RELATIONS and relation_operand or (host in ('-', '+') and control in TEX_MATH_LEXEMES and (following.isspace() or following in ('{', '^', '_'))) or row_end
        if not (row_syntax and in_math_row_container(scan[:unc.start()])):
            return True
    for drive in MATH_DRIVE_START.finditer(scan):
        if drive.group(1):
            control = TEX_CONTROL_WORD.match(scan, drive.end() - 1)
            text_test = control and control.group(1) == 'text' and (scan[control.end():control.end() + 1] == '{') and (len(drive.group(1)) == 1 or (re.fullmatch('[A-Za-z]_[A-Za-z0-9]', drive.group(1)) and in_math_membership_set(scan[:drive.start() + 1])))
            if not (control and (control.group(1) in TEX_MATH_LEXEMES or text_test)):
                return True
            continue
        cursor = drive.end() - 1
        controls = []
        while (control := TEX_CONTROL_WORD.match(scan, cursor)) is not None:
            controls.append(control.group(1))
            cursor = control.end()
        following = scan[cursor:cursor + 1]
        suffix = re.match('[A-Za-z0-9_.-]+\\\\([A-Za-z]+|[^A-Za-z])', scan[cursor:])
        if suffix and (not (controls and controls[0] in TEX_MATH_LEXEMES and (suffix.group(1) in TEX_MATH_LEXEMES or suffix.group(1) in '|,;! '))):
            return True
        if len(controls) > 1:
            structured = following in ('{', '(', '[', '^', '_')
            mapping = any((TEX_MAP_OPERATOR.fullmatch(c) or c in TEX_RELATIONS for c in controls[1:-1]))
            mapping = mapping or (following.isspace() and bool(TEX_MAP_OPERATOR.fullmatch(controls[-1])) and bool(re.match('\\s+[A-Za-z0-9({]', scan[cursor:])))
            mapping = mapping or (controls[-1] in {'otimes', 'oplus', 'times', 'boxtimes', 'cup', 'cap'} and in_math_row_container(scan[:drive.start()], require_row=False) and bool(re.match('\\s+[A-Za-z][A-Za-z0-9]*(?:_[A-Za-z0-9])?\\s*\\\\(?:to|longrightarrow|rightarrow|hookrightarrow)\\b', scan[cursor:])))
            mapping = mapping or (controls[-1] in TEX_RELATIONS and bool(re.match('\\s+[A-Za-z0-9({]', scan[cursor:])) and in_math_membership_set(scan[:drive.start() + 1]))
            if not all((c in TEX_MATH_LEXEMES for c in controls)) or not (structured or mapping):
                return True
        elif controls and controls[0] not in TEX_MATH_LEXEMES:
            if following not in ('{', '(', '[', '^', '_', '+', '-', '=', '|') and (not (following.isdigit() and re.match('\\d+[+*=^_-]', scan[cursor:]))):
                return True
    return False

def in_math_membership_set(prefix: str) -> bool:
    groups, sets, pending = ([], [], False)
    text_commands = {'text', 'textrm', 'texttt', 'textnormal', 'textsf', 'textbf', 'textit', 'mbox', 'hbox', 'operatorname'}
    token = re.compile('\\\\([A-Za-z]+)|\\\\.|[{}:]|\\s+|[^\\s\\\\{}:]+')
    cursor = 0
    while cursor < len(prefix):
        match = token.match(prefix, cursor)
        if match is None:
            return False
        cursor = match.end()
        if match.group().isspace():
            continue
        command = match.group(1)
        spelling = match.group()
        if command:
            if command == 'verb':
                delimiter_at = match.end()
                if prefix[delimiter_at:delimiter_at + 1] == '*':
                    delimiter_at += 1
                delimiter = prefix[delimiter_at:delimiter_at + 1]
                if not delimiter or delimiter.isspace():
                    return False
                end = prefix.find(delimiter, delimiter_at + 1)
                if end < 0:
                    return False
                cursor = end + 1
            elif command == 'in' and sets and (not any(groups)) and (len(groups) == sets[-1][0]):
                sets[-1][1] = True
            pending = command in text_commands
        elif spelling == '{':
            groups.append(pending)
            pending = False
        elif spelling == '}':
            if not groups:
                return False
            groups.pop()
            if sets and sets[-1][0] > len(groups):
                return False
            pending = False
        else:
            if not any(groups):
                if spelling == '\\{':
                    sets.append([len(groups), False, False])
                elif spelling == '\\}':
                    if not sets or sets[-1][0] != len(groups):
                        return False
                    sets.pop()
                elif spelling == ':' and sets and (len(groups) == sets[-1][0]):
                    sets[-1][2] = True
            pending = False
    return bool(sets and (not any(groups)) and (len(groups) == sets[-1][0]) and sets[-1][1] and (not sets[-1][2]))

def in_math_row_container(prefix: str, *, require_row=True) -> bool:
    envs, groups, pending = ([], [], None)
    row_envs = {'matrix', 'pmatrix', 'bmatrix', 'Bmatrix', 'vmatrix', 'Vmatrix', 'smallmatrix', 'aligned', 'alignedat', 'gathered', 'cases', 'array'}
    text_commands = {'text', 'textrm', 'texttt', 'textnormal', 'textsf', 'textbf', 'textit', 'mbox', 'hbox'}
    token = re.compile('\\\\(begin|end)\\{([^{}]+)\\}|\\\\([A-Za-z]+)|\\\\.|[{}]')
    cursor = 0
    while (match := token.search(prefix, cursor)) is not None:
        cursor = match.end()
        if match.group(1) == 'begin':
            envs.append(match.group(2))
            pending = None
        elif match.group(1) == 'end':
            if not envs or envs[-1] != match.group(2):
                return False
            envs.pop()
            pending = None
        elif match.group(3):
            command = match.group(3)
            if command == 'verb':
                delimiter_at = match.end()
                if prefix[delimiter_at:delimiter_at + 1] == '*':
                    delimiter_at += 1
                delimiter = prefix[delimiter_at:delimiter_at + 1]
                if not delimiter or delimiter.isspace():
                    return False
                end = prefix.find(delimiter, delimiter_at + 1)
                if end < 0:
                    return False
                cursor = end + 1
                pending = None
                continue
            pending = 'text' if command in text_commands else 'row' if command == 'substack' else None
        elif match.group() == '{':
            groups.append(pending)
            pending = None
        elif match.group() == '}':
            if groups:
                groups.pop()
            pending = None
        else:
            pending = None
    return 'text' not in groups and (not require_row or 'row' in groups or any((env in row_envs for env in envs)))

def public_text(value: object, field: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f'nonempty text required: {field}')
    if private_reference(value):
        raise ValueError(f'private/local path in {field}')
    return value

def web_math_projection(raw: str) -> tuple[str, str | None]:
    match = re.fullmatch('(\\\\\\[|\\$\\$)(\\s*\\\\begin\\{(aligned|gathered)\\})([\\s\\S]*?)(\\\\tag\\{[^{}]+\\})(\\s*)(\\\\end\\{\\3\\})(\\s*)(\\\\\\]|\\$\\$)', raw)
    if not match or (match[1] == '\\[') != (match[9] == '\\]'):
        return (raw, None)
    if '\\tag' in match[4] or '\\begin' in match[4] or '\\end' in match[4]:
        return (raw, None)
    projected = match[1] + match[2] + match[4] + match[7] + match[6] + match[5] + match[8] + match[9]
    return (projected, 'whole-display-tag-outside-subenvironment-v1')

def identifier(value: object, field: str) -> str:
    value = public_text(value, field)
    if not ID.fullmatch(value) or PureWindowsPath(value).is_reserved() or value.endswith('.'):
        raise ValueError(f'unsafe identifier: {field}')
    return value

def render_markdown_math(source: str, *, local_links=None, mathematical_ids=(), heading_anchors=None) -> str:
    md = MarkdownIt('commonmark', {'html': False}).enable('table')
    delimiters = (('$$', '$$'), ('\\[', '\\]'), ('\\(', '\\)'), ('$', '$'))

    def math_inline(state, silent):
        start = state.pos
        for opener, closer in delimiters:
            if not state.src.startswith(opener, start):
                continue
            end = state.src.find(closer, start + len(opener))
            while end >= 0 and end > 0 and (state.src[end - 1] == '\\'):
                end = state.src.find(closer, end + len(closer))
            if end < 0 or (opener == '$' and '\n\n' in state.src[start:end]):
                return False
            if not silent:
                token = state.push('course_math', '', 0)
                token.content = state.src[start:end + len(closer)]
            state.pos = end + len(closer)
            return True
        return False

    def math_block(state, start, end, silent):
        if state.sCount[start] - state.blkIndent >= 4:
            return False
        begin = state.bMarks[start] + state.tShift[start]
        first = state.src[begin:state.eMarks[start]]
        for opener, closer in delimiters[:2]:
            if not first.startswith(opener):
                continue
            raw = first
            stop = start
            while True:
                found = raw.find(closer, len(opener))
                if found >= 0:
                    if raw[found + len(closer):].strip():
                        return False
                    break
                stop += 1
                if stop >= end:
                    return False
                raw += '\n' + state.src[state.bMarks[stop] + state.tShift[stop]:state.eMarks[stop]]
            if silent:
                return True
            token = state.push('course_math', '', 0)
            token.content = raw
            token.block = True
            token.map = [start, stop + 1]
            state.line = stop + 1
            return True
        return False

    def operator_star(state, silent):
        start = state.pos
        if state.src[start:start + 1] != '*' or (start > 0 and state.src[start - 1] == '*') or (not re.match('-[A-Za-z]', state.src[start + 1:])):
            return False
        if not silent:
            state.push('text', '', 0).content = '*'
        state.pos += 1
        return True

    def render_math(tokens, index, options, env):
        raw = tokens[index].content
        if math_private_reference(raw):
            raise ValueError('local source reference in mathematics')
        projected, adaptation = web_math_projection(raw)
        attributes = '' if adaptation is None else ' data-render-adaptation="' + adaptation + '" data-render-tex="' + html.escape(projected, quote=True) + '" title="Display-only adjustment: the unchanged whole-display label is outside aligned/gathered; original TeX is retained in data-tex."'
        display = ' math-display' if raw.startswith(('\\[', '$$')) else ''
        return f'<span class="math{display}" data-tex="{html.escape(raw, quote=True)}"{attributes}>{html.escape(projected)}</span>' + ('\n' if tokens[index].block else '')
    md.inline.ruler.before('escape', 'course_math', math_inline)
    md.inline.ruler.before('emphasis', 'course_operator_star', operator_star)
    md.block.ruler.after('fence', 'course_math', math_block)
    md.renderer.rules['course_math'] = render_math

    def heading_open(tokens, index, options, env):
        opening = md.renderer.renderToken(tokens, index, options, env)
        aliases = tokens[index].meta.get('course_aliases', [])
        return opening + ''.join((f'<span id="{html.escape(a, quote=True)}"></span>' for a in aliases))
    md.renderer.rules['heading_open'] = heading_open
    tokens = md.parse(source)
    in_cell = False
    for token in tokens:
        if token.type in ('th_open', 'td_open'):
            in_cell = True
        elif token.type in ('th_close', 'td_close'):
            in_cell = False
        elif in_cell and token.type == 'inline':
            cell = token.content
            if cell.count('\\(') != cell.count('\\)') or cell.count('$') % 2:
                raise ValueError('a formula in a table cell is cut by a column separator')
    bound_headings, bound_ids = ({}, set())
    heading_lines = {t.map[0] + 1 for t in tokens if t.type == 'heading_open'}
    if heading_anchors is not None:
        if not isinstance(heading_anchors, list):
            raise ValueError('heading anchors must be an explicit list')
        for row in heading_anchors:
            if not isinstance(row, dict) or set(row) != {'line', 'ids'}:
                raise ValueError('invalid heading anchor schema')
            line, ids = (row['line'], row['ids'])
            if type(line) is not int or line not in heading_lines or line in bound_headings or (not isinstance(ids, list)) or (not ids):
                raise ValueError('heading anchor must bind one actual source heading')
            for value in ids:
                identifier(value, 'heading anchor')
                if value.lower() in bound_ids:
                    raise ValueError('duplicate heading anchor or case alias')
                bound_ids.add(value.lower())
            bound_headings[line] = ids
    seen_headings = set()
    declared_ids = sorted(set(mathematical_ids) | {i for ids in bound_headings.values() for i in ids}, key=len, reverse=True)
    if len({value.lower() for value in declared_ids}) != len(declared_ids):
        raise ValueError('declared mathematical IDs have colliding aliases')
    stable_headings = {}
    reserved = {alias for value in declared_ids for alias in (value, value.lower())}
    for index, token in enumerate(tokens):
        if token.type != 'heading_open':
            continue
        inline = tokens[index + 1]
        visible = ''.join((child.content if child.type in {'text', 'code_inline'} else ' ' if child.type in {'softbreak', 'hardbreak'} else '' for child in inline.children or [])).strip()
        declared = next((value for value in declared_ids if visible == value or (visible.startswith(value) and visible[len(value):len(value) + 1] in ' \t\n:—–')), None)
        stable = re.match('^([A-Z][A-Z0-9]+-[A-Z0-9]+-\\d+)(?=$|[\\s:—–])', visible)
        stable_id = declared or (stable.group(1) if stable else None)
        bound = bound_headings.get(token.map[0] + 1)
        if bound:
            if stable_id and stable_id not in bound:
                raise ValueError('heading anchor contradicts the visible native ID')
            stable_id = bound[0]
        if stable_id:
            stable_headings[index] = stable_id
            reserved.update((stable_id, stable_id.lower()))
    for index, token in enumerate(tokens):
        if token.type == 'heading_open':
            title = tokens[index + 1].content
            slug = re.sub('[^\\w-]+', '-', title.lower()).strip('-') or 'heading'
            stable_id = stable_headings.get(index)
            bound = bound_headings.get(token.map[0] + 1, [])
            if stable_id:
                slug = stable_id
            unique, counter = (slug, 2)
            own_reserved = {a for i in bound for a in (i, i.lower())} if bound else {stable_id, stable_id.lower()} if stable_id else set()
            if bound and own_reserved & seen_headings:
                raise ValueError('bound heading anchor collides with an earlier heading')
            while unique in seen_headings or (stable_id and unique.lower() in seen_headings) or {unique, unique.lower()} & reserved - own_reserved:
                unique = slug + '-' + str(counter)
                counter += 1
            seen_headings.add(unique)
            token.attrSet('id', unique)
            aliases = list(dict.fromkeys((a for i in [unique] + bound for a in (i, i.lower()) if a != unique))) if stable_id else []
            seen_headings.update(aliases)
            token.meta['course_aliases'] = aliases
    for token in tokens:
        if token.type not in {'inline', 'course_math'} and private_reference(token.content):
            raise ValueError('local source reference in teaching text')
        for child in token.children or []:
            if child.type != 'course_math' and private_reference(child.content):
                raise ValueError('local source reference in teaching text')
            if child.type == 'image':
                raise ValueError('This edition uses editable text and TeX mathematics; an image needs a separate asset renderer.')
            if child.type == 'link_open':
                if any((private_reference(str(value)) for name, value in child.attrs.items() if name != 'href')):
                    raise ValueError('private/local course link attribute')
                href = child.attrGet('href') or ''
                if public_web_url(href):
                    continue
                if PRIVATE_PATH.search(href):
                    raise ValueError('private/local course link')
                if href.startswith(('mailto:', '#')):
                    continue
                parsed = urlsplit(href)
                key = 'course:' + parsed.path if parsed.scheme == 'course' else parsed.path
                if parsed.scheme not in ('', 'course') or parsed.netloc or parsed.query or (local_links is None) or (key not in local_links):
                    raise ValueError('course links must be public URLs, local anchors or explicit catalog unit links')
                target = local_links[key]
                if parsed.fragment:
                    target += '#' + parsed.fragment
                child.attrSet('href', target)
    return md.renderer.render(tokens, md.options, {})
