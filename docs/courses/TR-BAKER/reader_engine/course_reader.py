"""Frozen, allowlisted course projections: CommonMark lessons with TeX mathematics to HTML.

Rendering utilities from the Open Research Courses R5C renderer (21 September 2026).
Usage and software provenance are documented in README.md.
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
from output_safety import fresh_directory, isolated_path
from course_assets import (asset_semantic_fields, read_unit_assets,
                           install_course_image_rule, copy_unit_assets, figure_provenance)

ID = re.compile(r"[A-Za-z0-9][A-Za-z0-9_.-]{0,100}\Z")
HASH = re.compile(r"[0-9A-F]{64}\Z")
PRIVATE_PATH = re.compile(r"(?:\b[A-Za-z]:[\\/]|\b[A-Za-z]:(?!//)[^\s\"<>]*[\\/]|\b[A-Za-z]:[\w-]+\.[\w-]+\b|file:" r"//|/(?:Users|home)/|\\\\[A-Za-z0-9_.-]+\\)", re.I)
WEB_URL = re.compile(r"\bhttps?://[^\s<>\"']+", re.I)
LOCAL_URL_PAYLOAD = re.compile(r"(?:\b[A-Za-z]:[\\/]|file:" r"//|\\)", re.I)
MATH_UNEQUIVOCAL_PATH = re.compile(
    r'(?:\bfile:[\\/]|/(?:Users|home)/)', re.I)
MATH_UNC_HEAD = re.compile(r'(?<!\\)\\\\(?!\\)([A-Za-z0-9_.-]+)\\([A-Za-z]*)')
MATH_DRIVE_PATH = re.compile(
    r'(?:\b[A-Za-z]:/|\b[A-Za-z]:[^\s{}$<>]*\.[A-Za-z0-9]{1,12}\b)', re.I)
MATH_DRIVE_START = re.compile(r'\b[A-Za-z]:([A-Za-z0-9_.-]*)\\')
TEX_CONTROL_WORD = re.compile(r'\\([A-Za-z]+)')
TEX_MAP_OPERATOR = re.compile(r'(?:to|mapsto|.*arrow)\Z')
TEX_RELATIONS = set('in ni not notin le leq ge geq neq ne equiv cong sim simeq subset subseteq supset supseteq parallel perp'.split())
# Relation symbols supported in course mathematics.
TEX_RELATIONS |= set('prec succ preceq succeq ll gg approx propto mid vdash dashv models lhd rhd unlhd unrhd '
                     'sqsubset sqsubseteq sqsupset sqsupseteq lesssim gtrsim leqslant geqslant subsetneq supsetneq'.split())
# Only disambiguates bare/composed controls with no argument syntax. Ordinary
# controls with explicit arguments are lexed generally, not from this set.
TEX_MATH_LEXEMES = set(('mathcal mathbb mathfrak mathscr mathrm mathsf mathtt '
    'mathbf mathit operatorname to rightarrow leftarrow mapsto hookrightarrow '
    'longrightarrow longleftarrow longmapsto colon quad qquad Delta Gamma Sigma '
    'Omega Hom Spec ell overline underline Ker Im wedge rho widehat widetilde '
    'hat tilde bar alpha beta gamma delta epsilon varepsilon zeta eta theta '
    'vartheta iota kappa lambda mu nu xi omicron pi varpi varrho sigma varsigma '
    'tau upsilon phi varphi chi psi omega Theta Lambda Xi Pi Upsilon Phi Psi '
    'infty sum prod coprod int iint iiint oint bigcap bigcup bigoplus bigotimes '
    'bigvee bigwedge sup inf lim limsup liminf max min exists forall '
    'langle rangle lceil rceil lfloor rfloor left right middle '
    'sin cos tan cot sinh cosh tanh log ln exp det dim ker hom arg deg Pr '
    'times cdot circ otimes oplus odot ast star cup cap vee pm mp div '
    'xrightarrow xleftarrow setminus dot ddot rtimes ltimes '
    # Binary operators supported in course mathematics.
    'boxtimes boxplus boxminus boxdot ominus oslash uplus sqcup sqcap bullet amalg').split()) | TEX_RELATIONS
PROOF_STATES = {"not_started", "open", "proof_closed"}
COURSE_STATES = {"specified", "drafting", "partially_audited", "complete"}
UNIT_STATES = {"drafted", "proof_closed", "audited"}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def public_web_url(value: str, *, _depth=0) -> bool:
    """Recognize web citations, not filesystem paths that resemble their routes.

    This classifies links only; it does not fetch or certify remote content.
    A university's /users/ directory is not a local /Users""" """/ path. Embedded
    credentials, local-file payloads and malformed authorities remain invalid.
    """
    if _depth > 8:
        return False
    try:
        parsed = urlsplit(value)
        decoded = unquote(value)
        if (parsed.scheme.lower() not in {'http', 'https'} or not parsed.hostname
                or parsed.username is not None or parsed.password is not None
                or any(char.isspace() or ord(char) < 32 for char in value)
                or any(char in parsed.netloc for char in '\\%')
                or LOCAL_URL_PAYLOAD.search(decoded)
                or any(private_reference(part, _depth=_depth+1)
                       for component in (parsed.query, parsed.fragment)
                       for pair in parse_qsl(component, keep_blank_values=True, max_num_fields=1024)
                       for part in pair)):
            return False
        # Access validates a port instead of accepting an unusable authority.
        parsed.port
        return not any(ord(char) < 32 or ord(char) == 127 for char in decoded)
    except ValueError:
        return False


def private_reference(value: str, *, _depth=0, _pattern=PRIVATE_PATH) -> bool:
    """Check text/attributes without mistaking complete web URLs for paths."""
    invalid_url = False
    def scrub(match):
        nonlocal invalid_url
        # Sentence punctuation is not a URL authority. The original text is
        # never changed; this temporary value is only a privacy classification.
        candidate = match.group().rstrip('.,;:!?)]}')
        if public_web_url(candidate, _depth=_depth):
            return ' '
        invalid_url = True
        return match.group()
    scrubbed = WEB_URL.sub(scrub, value)
    return invalid_url or bool(_pattern.search(scrubbed))


def math_private_reference(value: str) -> bool:
    """Classify paths using control tokens and bounded ambiguity disambiguation.

    Control words end at the first non-ASCII letter, including '_' and digits.
    A colon followed by a control word/symbol is mathematical syntax unless
    there is additional path evidence. Unstructured multi-segment backslash
    chains are rejected; braced/scripted controls and map notation are not.
    File-shaped references are checked first, including command-looking paths.
    Bare/composed controls without argument syntax use a small mathematical
    lexicon for disambiguation; an unknown bare drive token is rejected.
    D:""" """\\alpha is still ambiguous and is read as TeX, not certified as an absence
    of private material. This is not a
    TeX-expansion sandbox or a substitute for the independent export audit.
    """
    if private_reference(value, _pattern=MATH_UNEQUIVOCAL_PATH):
        return True
    if private_reference(value, _pattern=MATH_DRIVE_PATH):
        return True
    # A complete public URL is checked separately by private_reference. Do not
    # reinterpret its route/query as mathematical drive notation.
    scan = WEB_URL.sub(' ', value)
    for unc in MATH_UNC_HEAD.finditer(scan):
        host, control = unc.groups()
        following = scan[unc.end():unc.end()+1]
        # A final differential row can end immediately at its environment:
        # \begin{pmatrix}dh\\df\end{pmatrix}. The source is mathematical
        # syntax, not a UNC share named "end". Text/literal groups and file
        # suffixes still pass through the independent checks above/below.
        row_end = (control == 'end' and bool(re.match(
            r'\{(?:matrix|pmatrix|bmatrix|Bmatrix|vmatrix|Vmatrix|smallmatrix|aligned|alignedat|gathered|cases|array)\}',
            scan[unc.end():])))
        # Vendored-copy addition: a relation after a row break may be followed
        # directly by a digit or by a known mathematical control word with TeX
        # structure (row break, then 1\leq\ell_i inside \substack), not only by
        # a space. File-shaped continuations such as \in\Book.pdf stay rejected,
        # and the explicit row-container requirement below still applies.
        operand = TEX_CONTROL_WORD.match(scan, unc.end())
        relation_operand = (following.isspace() or following.isdigit() or (
            operand is not None and operand.group(1) in TEX_MATH_LEXEMES
            and scan[operand.end():operand.end()+1] in ('_', '^', '{', ' ', '\\', '')))
        row_syntax = ((control in TEX_RELATIONS and relation_operand) or
                      (host in ('-', '+') and control in TEX_MATH_LEXEMES and
                       (following.isspace() or following in ('{', '^', '_'))) or row_end)
        if not (row_syntax and in_math_row_container(scan[:unc.start()])):
            return True
    for drive in MATH_DRIVE_START.finditer(scan):
        if drive.group(1):  # C:Corpus\Book, not f:X/Y or f:\SomeMacro{X}.
            control = TEX_CONTROL_WORD.match(scan, drive.end()-1)
            text_test = (control and control.group(1) == 'text' and
                         scan[control.end():control.end()+1] == '{' and
                         (len(drive.group(1)) == 1 or
                          (re.fullmatch(r'[A-Za-z]_[A-Za-z0-9]', drive.group(1)) and
                           in_math_membership_set(scan[:drive.start()+1]))))
            if not (control and (control.group(1) in TEX_MATH_LEXEMES or text_test)):
                return True
            continue  # V:H_\psi\to K or {x:x\in M}; other candidates still checked.
        cursor = drive.end() - 1
        controls = []
        while (control := TEX_CONTROL_WORD.match(scan, cursor)) is not None:
            controls.append(control.group(1))
            cursor = control.end()
        following = scan[cursor:cursor+1]
        # Digits, underscores and hyphens can end a control word but remain
        # part of a real path segment. Do not discard its remaining separators.
        suffix = re.match(r'[A-Za-z0-9_.-]+\\([A-Za-z]+|[^A-Za-z])', scan[cursor:])
        if suffix and not (controls and controls[0] in TEX_MATH_LEXEMES and
                (suffix.group(1) in TEX_MATH_LEXEMES or suffix.group(1) in '|,;! ')):
            return True
        if len(controls) > 1:
            structured = following in ('{', '(', '[', '^', '_')
            mapping = any(TEX_MAP_OPERATOR.fullmatch(c) or c in TEX_RELATIONS for c in controls[1:-1])
            mapping = mapping or (following.isspace() and
                bool(TEX_MAP_OPERATOR.fullmatch(controls[-1])) and
                bool(re.match(r'\s+[A-Za-z0-9({]', scan[cursor:])))
            # A tensor/product domain may end its control-word run before a
            # plain operand: d:\Omega\otimes B\to A. Require both the explicit
            # binary operator and a bounded operand-to-arrow continuation; an
            # arbitrary directory chain or literal text gets no exemption.
            mapping = mapping or (
                controls[-1] in {'otimes', 'oplus', 'times', 'boxtimes', 'cup', 'cap'}
                and in_math_row_container(scan[:drive.start()], require_row=False)
                and bool(re.match(r'\s+[A-Za-z][A-Za-z0-9]*(?:_[A-Za-z0-9])?\s*\\(?:to|longrightarrow|rightarrow|hookrightarrow)\b', scan[cursor:])))
            # Vendored-copy addition: the predicate of a set builder may begin with a control word and a
            # relation, as in \{r\in\mathbb Q:\omega\in C_r\}. Require the set's first colon (its left side
            # has \in), a run of known TeX words ending in a relation, then a space and an operand.
            mapping = mapping or (
                controls[-1] in TEX_RELATIONS
                and bool(re.match(r'\s+[A-Za-z0-9({]', scan[cursor:]))
                and in_math_membership_set(scan[:drive.start() + 1]))
            if not all(c in TEX_MATH_LEXEMES for c in controls) or not (structured or mapping):
                return True
        elif controls and controls[0] not in TEX_MATH_LEXEMES:
            # Explicit TeX argument/script/operator structure admits new control
            # words without adding each one to a hand-maintained allowlist.
            if following not in ('{', '(', '[', '^', '_', '+', '-', '=', '|') and not (
                    following.isdigit() and re.match(r'\d+[+*=^_-]', scan[cursor:])):
                return True
    return False


def in_math_membership_set(prefix: str) -> bool:
    """Recognize a first set-builder colon outside text and literal syntax.

    Only disambiguates a scripted symbol followed by a textual predicate.
    It does not exempt the whole set or any later path candidate.
    """
    groups, sets, pending = [], [], False
    text_commands = {'text', 'textrm', 'texttt', 'textnormal', 'textsf',
                     'textbf', 'textit', 'mbox', 'hbox', 'operatorname'}
    token = re.compile(r'\\([A-Za-z]+)|\\.|[{}:]|\s+|[^\s\\{}:]+')
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
                if prefix[delimiter_at:delimiter_at+1] == '*':
                    delimiter_at += 1
                delimiter = prefix[delimiter_at:delimiter_at+1]
                if not delimiter or delimiter.isspace():
                    return False
                end = prefix.find(delimiter, delimiter_at+1)
                if end < 0:
                    return False
                cursor = end+1
            elif (command == 'in' and sets and not any(groups) and
                  len(groups) == sets[-1][0]):
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
                if spelling == r'\{':
                    sets.append([len(groups), False, False])
                elif spelling == r'\}':
                    if not sets or sets[-1][0] != len(groups):
                        return False
                    sets.pop()
                elif spelling == ':' and sets and len(groups) == sets[-1][0]:
                    sets[-1][2] = True
            pending = False
    return bool(sets and not any(groups) and len(groups) == sets[-1][0]
                and sets[-1][1] and not sets[-1][2])


def in_math_row_container(prefix: str, *, require_row=True) -> bool:
    """Recognize explicit row syntax, never treat text groups as mathematics.

    This classifies a TeX row break followed by e.g. Au\\in or -\\tau.
    It neither executes TeX nor exempts file-shaped or arbitrary UNC paths.
    """
    envs, groups, pending = [], [], None
    row_envs = {'matrix','pmatrix','bmatrix','Bmatrix','vmatrix','Vmatrix',
                'smallmatrix','aligned','alignedat','gathered','cases','array'}
    text_commands = {'text','textrm','texttt','textnormal','textsf','textbf','textit','mbox','hbox'}
    token = re.compile(r'\\(begin|end)\{([^{}]+)\}|\\([A-Za-z]+)|\\.|[{}]')
    cursor = 0
    while (match := token.search(prefix, cursor)) is not None:
        cursor = match.end()
        if match.group(1) == 'begin':
            envs.append(match.group(2)); pending = None
        elif match.group(1) == 'end':
            if not envs or envs[-1] != match.group(2):
                return False
            envs.pop(); pending = None
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
                # The prefix ends immediately before the candidate UNC path.
                # An unclosed literal here means that path is literal text,
                # not a mathematical row, even inside a matrix environment.
                if end < 0:
                    return False
                cursor = end + 1
                pending = None
                continue
            pending = 'text' if command in text_commands else ('row' if command == 'substack' else None)
        elif match.group() == '{':
            groups.append(pending); pending = None
        elif match.group() == '}':
            if groups:
                groups.pop()
            pending = None
        else:
            pending = None
    return 'text' not in groups and (not require_row or 'row' in groups or any(env in row_envs for env in envs))


def public_text(value: object, field: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"nonempty text required: {field}")
    if private_reference(value):
        raise ValueError(f"private/local path in {field}")
    return value


def web_math_projection(raw: str) -> tuple[str, str | None]:
    """Move one whole-display tag outside aligned/gathered, retaining source.

    Those subordinate environments do not accept a tag. Only the single
    trailing label moves; equations, alignment, line breaks and label spelling
    are unchanged. Multiple/internal tags or nested environments are not guessed.
    """
    match = re.fullmatch(r'(\\\[|\$\$)(\s*\\begin\{(aligned|gathered)\})([\s\S]*?)(\\tag\{[^{}]+\})(\s*)(\\end\{\3\})(\s*)(\\\]|\$\$)', raw)
    if not match or (match[1] == r'\[') != (match[9] == r'\]'):
        return raw, None
    if r'\tag' in match[4] or r'\begin' in match[4] or r'\end' in match[4]:
        return raw, None
    projected = match[1] + match[2] + match[4] + match[7] + match[6] + match[5] + match[8] + match[9]
    return projected, 'whole-display-tag-outside-subenvironment-v1'


def identifier(value: object, field: str) -> str:
    value = public_text(value, field)
    if not ID.fullmatch(value) or PureWindowsPath(value).is_reserved() or value.endswith('.'):
        raise ValueError(f"unsafe identifier: {field}")
    return value


def bound_file(root: Path, relative: object, expected_hash: object) -> Path:
    if not isinstance(relative, str) or "\\" in relative:
        raise ValueError("source name must be a relative POSIX path")
    rel = PurePosixPath(relative)
    if rel.is_absolute() or any(p in {"..", "."} for p in rel.parts) or not rel.parts:
        raise ValueError("source path escapes frozen input")
    if any(not ID.fullmatch(p) for p in rel.parts):
        raise ValueError("unsafe source path component")
    if not isinstance(expected_hash, str) or not HASH.fullmatch(expected_hash):
        raise ValueError("missing exact source SHA-256")
    path = root.joinpath(*rel.parts)
    if any(p.is_symlink() for p in [path, *path.parents] if p != root.parent):
        raise ValueError("symlink source not accepted")
    if not path.resolve().is_relative_to(root.resolve()) or not path.is_file():
        raise ValueError("source missing or outside frozen input")
    if digest(path) != expected_hash:
        raise ValueError("frozen course source hash mismatch")
    return path


def read_reader_assets(root: Path, rows: object) -> list[dict]:
    """Bind explicitly declared course-local CSS/JS; never discover assets.

    Paths are relative to this course's root, in assets/. This validates the
    declaration and bytes, not the behaviour or licence of the supplied code.
    """
    if not isinstance(rows, list) or len(rows) > 16:
        raise ValueError("reader_assets must be a bounded explicit list")
    result, seen = [], set()
    extensions = {"stylesheet": ".css", "script": ".js"}
    for row in rows:
        if not isinstance(row, dict) or set(row) != {"source", "sha256", "license", "kind"}:
            raise ValueError("reader asset must contain exactly source, sha256, license and kind")
        kind = row["kind"]
        if not isinstance(kind, str) or kind not in extensions:
            raise ValueError("unsupported reader asset kind")
        source = row["source"]
        if (not isinstance(source, str) or not source.startswith("assets/")
                or not source.endswith(extensions[kind])
                or any(part in {"", ".", ".."} for part in source.split("/"))):
            raise ValueError("reader asset requires a canonical course-local assets path")
        for part in source.split("/"):
            identifier(part, "reader asset path")
        if source.casefold() in seen:
            raise ValueError("duplicate reader asset path")
        seen.add(source.casefold())
        public_text(row["license"], "reader asset licence")
        bound_file(root, source, row["sha256"])
        result.append(dict(row))
    return result


def render_markdown_math(source: str, *, local_links=None, mathematical_ids=(), heading_anchors=None, assets=None) -> str:
    """Parse math in Markdown context, never by replacement inside HTML."""
    # Vendored-copy addition: tables. The "commonmark" preset has the table rule switched off, so a
    # Markdown table came out as a paragraph of pipe characters.
    md = MarkdownIt("commonmark", {"html": False}).enable("table")
    delimiters = (("$$", "$$"), (r"\[", r"\]"), (r"\(", r"\)"), ("$", "$"))

    def math_inline(state, silent):
        start = state.pos
        for opener, closer in delimiters:
            if not state.src.startswith(opener, start):
                continue
            end = state.src.find(closer, start + len(opener))
            while end >= 0 and end > 0 and state.src[end-1] == '\\':
                end = state.src.find(closer, end + len(closer))
            if end < 0 or (opener == '$' and '\n\n' in state.src[start:end]):
                return False
            if not silent:
                token = state.push('course_math', '', 0)
                token.content = state.src[start:end+len(closer)]
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
                    if raw[found+len(closer):].strip():
                        return False
                    break
                stop += 1
                if stop >= end:
                    return False
                raw += '\n' + state.src[state.bMarks[stop]+state.tShift[stop]:state.eMarks[stop]]
            if silent:
                return True
            token = state.push('course_math', '', 0)
            token.content = raw
            token.block = True
            token.map = [start, stop+1]
            state.line = stop+1
            return True
        return False

    def operator_star(state, silent):
        # In this mathematical dialect *-homomorphism / C*-algebra carry a
        # literal involution marker, not an opening Markdown emphasis marker.
        # Keep code, explicit math, **strong**, and ordinary *emphasis* intact.
        start = state.pos
        if (state.src[start:start+1] != '*' or
                (start > 0 and state.src[start-1] == '*') or
                not re.match(r'-[A-Za-z]', state.src[start+1:])):
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
        attributes = '' if adaptation is None else (' data-render-adaptation="' + adaptation + '" data-render-tex="' + html.escape(projected, quote=True) + '"')
        display = ' math-display' if raw.startswith((r'\[', '$$')) else ''
        return f'<span class="math{display}" data-tex="{html.escape(raw, quote=True)}"{attributes}>{html.escape(projected)}</span>' + ('\n' if tokens[index].block else '')

    md.inline.ruler.before('escape', 'course_math', math_inline)
    md.inline.ruler.before('emphasis', 'course_operator_star', operator_star)
    md.block.ruler.after('fence', 'course_math', math_block,
                         {'alt': ['paragraph', 'reference', 'blockquote', 'list']})
    md.renderer.rules['course_math'] = render_math
    def heading_open(tokens, index, options, env):
        opening = md.renderer.renderToken(tokens, index, options, env)
        aliases = tokens[index].meta.get('course_aliases', [])
        return opening + ''.join(f'<span id="{html.escape(a, quote=True)}"></span>' for a in aliases)

    md.renderer.rules['heading_open'] = heading_open
    if assets is not None:
        install_course_image_rule(md, assets)
    tokens = md.parse(source)
    if assets is not None:
        assets.validate_tokens(tokens)
    # Vendored-copy addition: a table row is split into cells before its formulas are read, so a "|" inside
    # a formula would cut the formula in two. Refuse such a row instead of rendering a broken table.
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
    # Some producers bind native IDs to source headings without putting the ID
    # into the visible title. Honor the exact hash-bound source-line map; never
    # manufacture a heading or insert an ID into the authored Markdown.
    bound_headings, bound_ids = {}, set()
    heading_lines = {t.map[0] + 1 for t in tokens if t.type == 'heading_open'}
    if heading_anchors is not None:
        if not isinstance(heading_anchors, list):
            raise ValueError('heading anchors must be an explicit list')
        for row in heading_anchors:
            if not isinstance(row, dict) or set(row) != {'line', 'ids'}:
                raise ValueError('invalid heading anchor schema')
            line, ids = row['line'], row['ids']
            if (type(line) is not int or line not in heading_lines or line in bound_headings
                    or not isinstance(ids, list) or not ids):
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
        inline = tokens[index+1]
        # Formatting delimiters are not part of a visible mathematical ID.
        visible = ''.join(child.content if child.type in {'text', 'code_inline'}
                          else ' ' if child.type in {'softbreak', 'hardbreak'} else ''
                          for child in inline.children or []).strip()
        declared = next((value for value in declared_ids
                         if visible == value or (visible.startswith(value)
                             and visible[len(value):len(value)+1] in ' \t\n:—–')), None)
        stable = re.match(r'^([A-Z][A-Z0-9]+-[A-Z0-9]+-\d+)(?=$|[\s:—–])', visible)
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
            title = tokens[index+1].content
            slug = re.sub(r'[^\w-]+', '-', title.lower()).strip('-') or 'heading'
            stable_id = stable_headings.get(index)
            bound = bound_headings.get(token.map[0] + 1, [])
            if stable_id:
                slug = stable_id
            unique, counter = slug, 2
            own_reserved = {a for i in bound for a in (i, i.lower())} if bound else ({stable_id, stable_id.lower()} if stable_id else set())
            if bound and own_reserved & seen_headings:
                raise ValueError('bound heading anchor collides with an earlier heading')
            while (unique in seen_headings or (stable_id and unique.lower() in seen_headings)
                   or ({unique, unique.lower()} & (reserved - own_reserved))):
                unique = slug + '-' + str(counter)
                counter += 1
            seen_headings.add(unique)
            token.attrSet('id', unique)
            aliases = list(dict.fromkeys(a for i in ([unique] + bound) for a in (i, i.lower()) if a != unique)) if stable_id else []
            seen_headings.update(aliases)
            token.meta['course_aliases'] = aliases
    for token in tokens:
        # Mathematics may legitimately contain F:\mathcal. Other visible text,
        # code, metadata and links cannot carry machine-local paths.
        if token.type not in {'inline', 'course_math'} and private_reference(token.content):
            raise ValueError('local source reference in teaching text')
        for child in token.children or []:
            if child.type != 'course_math' and private_reference(child.content):
                raise ValueError('local source reference in teaching text')
            if child.type == "image":
                if assets is None:
                    raise ValueError("course image requires explicit independently authored asset admission")
                assets.validate_image(child)
            if child.type == "link_open":
                if any(private_reference(str(value)) for name, value in child.attrs.items()
                       if name != 'href'):
                    raise ValueError("private/local course link attribute")
                href = child.attrGet("href") or ""
                if public_web_url(href):
                    continue
                if PRIVATE_PATH.search(href):
                    raise ValueError("private/local course link")
                if href.startswith(("mailto:", "#")):
                    continue
                parsed = urlsplit(href)
                key = 'course:' + parsed.path if parsed.scheme == 'course' else parsed.path
                if (parsed.scheme not in ('', 'course') or parsed.netloc or parsed.query
                        or local_links is None or key not in local_links):
                    raise ValueError("course links must be public URLs, local anchors or explicit catalog unit links")
                target = local_links[key]
                if parsed.fragment:
                    target += '#' + parsed.fragment
                child.attrSet('href', target)
    return md.renderer.render(tokens, md.options, {})


class CourseLinkIndex(HTMLParser):
    """Collect actual emitted targets, not source-heading guesses."""
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids, self.links = set(), []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            if attrs['id'] in self.ids:
                raise ValueError('duplicate rendered course anchor')
            self.ids.add(attrs['id'])
        if tag == 'a' and 'href' in attrs:
            self.links.append(attrs['href'])


def validate_course_links(course, sources, all_courses=None):
    """Validate forward/backward cross-unit references after every unit is parsed."""
    pages = {'index.html': CourseLinkIndex()}
    for unit in course['units']:
        index = CourseLinkIndex()
        index.feed(sources[(course['id'], unit['id'])]['html'])
        pages[unit['id'] + '.html'] = index
    local_pages = list(pages)
    for row in course.get('linked_files', []):
        pages[row['href']] = CourseLinkIndex()
    for other in all_courses or []:
        for unit in other['units']:
            index = CourseLinkIndex()
            index.feed(sources[(other['id'], unit['id'])]['html'])
            pages['../' + other['id'] + '/' + unit['id'] + '.html'] = index
    for name in local_pages:
        page = pages[name]
        for href in page.links:
            if public_web_url(href) or href.startswith('mailto:'):
                continue
            parsed = urlsplit(href)
            target = parsed.path or name
            if target not in pages:
                raise ValueError('course link targets a unit outside the frozen catalog')
            if parsed.fragment and unquote(parsed.fragment) not in pages[target].ids:
                raise ValueError('course link targets a missing unit anchor')


def semantic_digest(cid, unit):
    """Bind audited claims, not only the text which happens to carry them."""
    metadata = {"course_id": cid, "unit_id": unit['id'], "source_sha256": unit['source_sha256'],
                "mathematical_item_ids": unit.get('mathematical_item_ids', []), "dependencies": unit.get('dependencies', [])}
    for key in ('heading_anchors', 'link_aliases', 'correction_notice'):
        if key in unit:
            metadata[key] = unit[key]
    metadata.update(asset_semantic_fields(unit))
    return hashlib.sha256(json.dumps(metadata, sort_keys=True, ensure_ascii=False, separators=(',', ':')).encode()).hexdigest().upper()


def read_mathematical_review(root, cid, unit):
    """A bounded conditional review is evidence, never an admission substitute."""
    fields = ('review_receipt', 'review_receipt_sha256')
    if not any(key in unit for key in fields):
        return None
    rp = bound_file(root, unit.get(fields[0]), unit.get(fields[1]))
    receipt = json.loads(rp.read_text(encoding='utf-8'))
    allowed = {'schema', 'course_id', 'unit_id', 'source_sha256', 'semantic_sha256',
               'verdict', 'independent_review', 'scope', 'open_obligations',
               'open_local_findings', 'resolved_local_findings', 'audit_report_sha256'}
    if not isinstance(receipt, dict) or set(receipt) != allowed:
        raise ValueError('mathematical review must contain only the complete public schema')
    if receipt.get('schema') != 'stacks-course-conditional-review/v1':
        raise ValueError('unsupported mathematical review schema')
    if (receipt.get('course_id') != cid or receipt.get('unit_id') != unit['id']
            or receipt.get('source_sha256') != unit['source_sha256']
            or receipt.get('semantic_sha256') != semantic_digest(cid, unit)):
        raise ValueError('mathematical review does not bind exact unit/coverage/dependencies')
    if receipt.get('verdict') != 'conditional_pass' or receipt.get('independent_review') is not True:
        raise ValueError('unsupported mathematical review verdict')
    if receipt.get('open_local_findings') != 0 or type(receipt.get('open_local_findings')) is not int:
        raise ValueError('conditional review retains local findings')
    resolved = receipt.get('resolved_local_findings')
    if type(resolved) is not int or resolved < 0 or not HASH.fullmatch(receipt.get('audit_report_sha256', '')):
        raise ValueError('invalid mathematical review evidence identity')
    obligations = receipt.get('open_obligations')
    if not isinstance(obligations, list) or not obligations:
        raise ValueError('conditional review must expose open obligations')
    if (unit.get('proof_status') != 'open' or unit.get('status') != 'drafted'
            or unit.get('admission', 'not_admitted') != 'not_admitted'):
        raise ValueError('conditional review cannot close or admit the unit')
    return {'status': 'conditional_pass', 'receipt_sha256': digest(rp),
            'audit_report_sha256': receipt['audit_report_sha256'],
            'open_local_findings': 0, 'resolved_local_findings': resolved,
            'scope': public_text(receipt.get('scope'), 'mathematical review scope'),
            'open_obligations': [public_text(x, 'open review obligation') for x in obligations]}


def read_source_snapshot(root, course):
    """Bind a selected course snapshot without importing its producer workspace."""
    fields = ('snapshot_receipt', 'snapshot_receipt_sha256')
    if not any(key in course for key in fields):
        return None
    path = bound_file(root, course.get(fields[0]), course.get(fields[1]))
    receipt = json.loads(path.read_text(encoding='utf-8'))
    allowed = {'schema', 'course_id', 'archive_sha256', 'archive_bytes',
               'course_metadata_sha256', 'item_index_sha256', 'license',
               'license_file', 'license_file_sha256', 'units', 'note'}
    if isinstance(receipt, dict) and receipt.get('schema') == 'stacks-course-source-snapshot/v2':
        allowed.add('additional_units')
    if not isinstance(receipt, dict) or set(receipt) != allowed:
        raise ValueError('source snapshot must contain only the complete public schema')
    if receipt['schema'] not in {'stacks-course-source-snapshot/v1', 'stacks-course-source-snapshot/v2'} or receipt['course_id'] != course['id']:
        raise ValueError('source snapshot course mismatch')
    for key in ('archive_sha256', 'course_metadata_sha256', 'item_index_sha256'):
        if not HASH.fullmatch(receipt.get(key, '')):
            raise ValueError('invalid source snapshot identity')
    if type(receipt['archive_bytes']) is not int or receipt['archive_bytes'] <= 0:
        raise ValueError('invalid source snapshot archive size')
    bound_file(root, receipt['license_file'], receipt['license_file_sha256'])
    expected = {u['id']: u for u in course['units']}
    rows = receipt['units']
    additions = receipt.get('additional_units', [])
    if not isinstance(rows, list) or not isinstance(additions, list) or len(rows) + len(additions) != len(expected):
        raise ValueError('source snapshot unit coverage mismatch')
    seen = set()
    for row in rows:
        if not isinstance(row, dict) or set(row) != {'id', 'source', 'source_sha256', 'bytes', 'archive_member'}:
            raise ValueError('invalid source snapshot unit schema')
        uid = row['id']
        if uid in seen or uid not in expected:
            raise ValueError('source snapshot duplicate or unknown unit')
        seen.add(uid)
        unit = expected[uid]
        if any(row[key] != unit[key] for key in ('source', 'source_sha256')):
            raise ValueError('source snapshot does not bind exact unit bytes')
        source = bound_file(root, row['source'], row['source_sha256'])
        if type(row['bytes']) is not int or row['bytes'] != source.stat().st_size:
            raise ValueError('source snapshot unit size mismatch')
        member = public_text(row['archive_member'], 'archive member')
        rel = PurePosixPath(member)
        if '\\' in member or rel.is_absolute() or '..' in rel.parts or rel.as_posix() != member:
            raise ValueError('unsafe source snapshot member')
    for row in additions:
        if not isinstance(row, dict) or set(row) != {'id', 'source', 'source_sha256', 'bytes', 'origin'}:
            raise ValueError('invalid additional snapshot unit schema')
        uid = row['id']
        if uid in seen or uid not in expected or row['origin'] != 'independent_manager_contribution':
            raise ValueError('invalid additional snapshot unit origin or identity')
        seen.add(uid)
        unit = expected[uid]
        if any(row[key] != unit[key] for key in ('source', 'source_sha256')):
            raise ValueError('additional snapshot unit binding mismatch')
        source = bound_file(root, row['source'], row['source_sha256'])
        if type(row['bytes']) is not int or row['bytes'] != source.stat().st_size:
            raise ValueError('additional snapshot unit size mismatch')
    result = {'receipt_sha256': digest(path), 'archive_sha256': receipt['archive_sha256'],
            'archive_bytes': receipt['archive_bytes'], 'unit_count': len(rows),
            'license': public_text(receipt['license'], 'course license'),
            'note': public_text(receipt['note'], 'source snapshot note')}
    if additions:
        result['additional_manager_units'] = len(additions)
    return result


LINKED_FILE_TYPES = {'.svg': 'image/svg+xml', '.tex': 'text/x-tex', '.zip': 'application/zip'}
LINKED_FILE_FIELDS = {'path', 'source', 'source_sha256', 'media_type', 'bytes'}


def read_linked_files(root: Path, cid: str, units):
    """Bind the non-lesson files that lessons link to, by exact bytes.

    Each unit may list `linked_files` rows: the lesson-relative Markdown target
    (`path`), the frozen file (`source`, relative to the catalog), its SHA-256,
    media type and size. Only listed files become valid link targets; they are
    published beside the course as `files/<name>`. Nothing is discovered.
    """
    rows, by_path, by_name = [], {}, {}
    for unit in units:
        values = unit.get('linked_files', [])
        if not isinstance(values, list):
            raise ValueError('linked files must be an explicit list')
        lesson = PurePosixPath(unit.get('source', ''))
        for row in values:
            if not isinstance(row, dict) or set(row) != LINKED_FILE_FIELDS:
                raise ValueError('linked file must contain exactly the public linked-file schema')
            href, source = row['path'], row['source']
            if (not isinstance(href, str) or '\\' in href or ':' in href or '?' in href
                    or '#' in href or '%' in href or len(href) > 512):
                raise ValueError('unsafe linked-file path')
            parts = list(lesson.parts[:-1])
            for part in href.split('/'):
                if part == '..':
                    if not parts:
                        raise ValueError('linked file escapes the frozen catalog root')
                    parts.pop()
                elif part in ('', '.'):
                    raise ValueError('noncanonical linked-file path')
                else:
                    parts.append(part)
            if '/'.join(parts) != source:
                raise ValueError('linked file must match its exact lesson-relative Markdown path')
            suffix = PurePosixPath(source).suffix.lower()
            if LINKED_FILE_TYPES.get(suffix) != row['media_type']:
                raise ValueError('unsupported linked-file type')
            bound = bound_file(root, source, row['source_sha256'])
            if type(row['bytes']) is not int or bound.stat().st_size != row['bytes']:
                raise ValueError('linked file size mismatch')
            name = identifier(PurePosixPath(source).name, 'linked file name')
            target = 'files/' + name
            previous = by_path.get(href)
            if previous is not None:
                if previous['source'] != source:
                    raise ValueError('one lesson path names two linked files')
                continue
            if by_name.get(name.casefold(), source) != source:
                raise ValueError('duplicate or case-colliding linked-file name')
            by_name[name.casefold()] = source
            record = {'path': href, 'href': target, 'source': source,
                      'source_sha256': row['source_sha256'], 'media_type': row['media_type'],
                      'bytes': row['bytes']}
            by_path[href] = record
            rows.append(record)
    return rows


def read_catalog(path: Path):
    """Read manager-frozen metadata; never enumerate producer directories."""
    if not path.is_file():
        raise ValueError("explicit frozen course catalog is required")
    raw = json.loads(path.read_text(encoding="utf-8"))
    if raw.get("schema") != "stacks-course-catalog/v1" or not isinstance(raw.get("courses"), list):
        raise ValueError("unknown course catalog schema")
    courses, seen, sources = [], set(), {}
    explicit_course_links = {}
    # Vendored-copy addition: a lesson file name (link alias) that belongs to exactly one
    # course may be linked from another course, as when one producer's lessons are split
    # into several topic courses. It resolves to that course's unit page. Names that occur
    # in more than one course stay local to their own course.
    alias_owners = {}
    for item in raw['courses']:
        other_id = identifier(item.get('id'), 'course id')
        for unit in item.get('units', []):
            other_unit = identifier(unit.get('id'), 'unit id')
            explicit_course_links[f'course:{other_id}/{other_unit}'] = f'../{other_id}/{other_unit}.html'
            for alias in unit.get('link_aliases', []) if isinstance(unit.get('link_aliases', []), list) else []:
                if isinstance(alias, str):
                    alias_owners.setdefault(alias.casefold(), set()).add((other_id, other_unit, alias))
    for item in raw["courses"]:
        if any(key in item for key in ('review_receipt', 'review_receipt_sha256')):
            raise ValueError('conditional mathematical review is unit-only')
        cid = identifier(item.get("id"), "course id")
        if cid.casefold() in seen:
            raise ValueError("duplicate course id")
        seen.add(cid.casefold())
        course = {"id": cid}
        for key in ("title", "track", "description", "coverage_note"):
            course[key] = public_text(item.get(key), key)
        course["status"] = item.get("status")
        if course["status"] not in COURSE_STATES:
            raise ValueError("invalid course status")
        course["prerequisites"] = [public_text(x, "prerequisite") for x in item.get("prerequisites", [])]
        if "reader_assets" in item:
            course["reader_assets"] = read_reader_assets(path.parent / cid, item["reader_assets"])
        if not isinstance(item.get("units"), list):
            raise ValueError("explicit unit list required, including empty lists")
        course["units"] = []
        unit_ids = set()
        filenames = [identifier(unit.get('id'), 'unit id') + '.html' for unit in item['units']]
        local_links = {name: name for name in ['index.html', *filenames]}
        local_links.update(explicit_course_links)
        local_links.update({'./' + name: name for name in ['index.html', *filenames]})
        # Exact separately licensed proof editions may have their own readable
        # surface. Bind every route to its frozen source, rather than resolving
        # a similarly named but different upstream lesson.
        for proof in item.get('proof_reader_links', []):
            if set(proof) != {'alias', 'source', 'source_sha256', 'url', 'license'}:
                raise ValueError('invalid exact proof-reader route')
            alias = proof['alias']
            if not isinstance(alias, str) or PRIVATE_PATH.search(alias) or not alias.endswith('.md'):
                raise ValueError('unsafe proof-reader alias')
            bound_file(path.parent, proof['source'], proof['source_sha256'])
            if not public_web_url(proof['url']) or proof['license'] not in {'GFDL-1.2-only', 'CC0-1.0'}:
                raise ValueError('invalid proof-reader URL or license')
            local_links[alias] = proof['url']
        alias_keys = {n.casefold() for n in local_links}
        for unit in item['units']:
            aliases = unit.get('link_aliases', [])
            if not isinstance(aliases, list):
                raise ValueError('unit link aliases must be a list')
            for alias in aliases:
                if (not isinstance(alias, str) or not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9_-]*\.md', alias)
                        or alias.casefold() in alias_keys):
                    raise ValueError('unsafe or duplicate unit link alias')
                alias_keys.add(alias.casefold())
                local_links[alias] = local_links['./' + alias] = unit['id'] + '.html'
        for key, owners in alias_owners.items():
            if len(owners) != 1 or key in alias_keys:
                continue
            other_id, other_unit, alias = next(iter(owners))
            if other_id.casefold() == cid.casefold():
                continue
            local_links[alias] = local_links['./' + alias] = f'../{other_id}/{other_unit}.html'
        linked_files = read_linked_files(path.parent, cid, item['units'])
        for row in linked_files:
            if row['path'].casefold() in alias_keys:
                raise ValueError('linked-file path collides with a lesson link')
            local_links[row['path']] = row['href']
        for unit in item["units"]:
            uid = identifier(unit.get("id"), "unit id")
            if uid.casefold() == 'index' or uid.casefold() in unit_ids:
                raise ValueError("duplicate unit id within course")
            unit_ids.add(uid.casefold())
            if unit.get("format") != "commonmark-math/v1":
                raise ValueError("unsupported format: add a lossless adapter before import")
            state, proof = unit.get("status"), unit.get("proof_status")
            if state not in UNIT_STATES or proof not in PROOF_STATES:
                raise ValueError("invalid unit/proof status")
            if state in {'proof_closed', 'audited'} and proof != 'proof_closed':
                raise ValueError('contradictory proof status')
            for key in ('mathematical_item_ids', 'dependencies'):
                values = unit.get(key, [])
                if not isinstance(values, list) or len(values) != len(set(values)):
                    raise ValueError('invalid or duplicate '+key)
                for value in values:
                    public_text(value, key)
            if unit.get('formalization', 'not_formalized') != 'not_formalized' or unit.get('translation', 'not_started') != 'not_started':
                raise ValueError('positive formalization/translation claims require an evidence adapter before import')
            source = bound_file(path.parent, unit.get("source"), unit.get("source_sha256"))
            if source.suffix.lower() != ".md":
                raise ValueError("only explicitly supported lesson sources are accepted")
            assets = read_unit_assets(path.parent, cid, unit)
            text = source.read_text(encoding="utf-8")
            rendered = render_markdown_math(text, local_links=local_links,
                                            mathematical_ids=unit.get('mathematical_item_ids', []),
                                            heading_anchors=unit.get('heading_anchors'), assets=assets)
            admission = unit.get("admission", "not_admitted")
            receipt_hash = None
            if admission == "admitted":
                rp = bound_file(path.parent, unit.get("admission_receipt"), unit.get("admission_receipt_sha256"))
                receipt = json.loads(rp.read_text(encoding="utf-8"))
                if receipt.get("course_id") != cid or receipt.get("unit_id") != uid or receipt.get("source_sha256") != unit["source_sha256"]:
                    raise ValueError("admission receipt is not bound to this unit")
                if receipt.get('semantic_sha256') != semantic_digest(cid, unit):
                    raise ValueError('admission does not bind exact coverage/dependencies')
                if receipt.get("decision") != "admit" or not all(receipt.get(x) is True for x in ("source_correspondence", "proof_audit", "expression_audit")):
                    raise ValueError("admission audit evidence incomplete")
                if state != "audited" or proof != "proof_closed":
                    raise ValueError("admitted unit lacks closed/audited state")
                receipt_hash = digest(rp)
            elif admission != "not_admitted" or state == "audited":
                raise ValueError("invalid or unsupported admission claim")
            review = read_mathematical_review(path.parent, cid, unit)
            correction = public_text(unit['correction_notice'], 'known correction') if 'correction_notice' in unit else None
            if correction and (admission != 'not_admitted' or proof != 'open'):
                raise ValueError('known unresolved correction contradicts admitted or closed state')
            projection = {
                "id": uid, "title": public_text(unit.get("title"), "unit title"),
                "status": state, "proof_status": proof, "admission": admission,
                "formalization": public_text(unit.get("formalization", "not_formalized"), "formalization"),
                "translation": public_text(unit.get("translation", "not_started"), "translation"),
                "dependencies": [public_text(x, "dependency") for x in unit.get("dependencies", [])],
                "mathematical_item_ids": [public_text(x, "mathematical item") for x in unit.get("mathematical_item_ids", [])],
                "source_sha256": unit["source_sha256"], "admission_receipt_sha256": receipt_hash,
                "mathematical_review": review,
                "semantic_sha256": semantic_digest(cid, unit),
                "href": f"courses/{cid}/{uid}.html",
            }
            sources[(cid, uid)] = {"text": text, "html": rendered, "assets": assets}
            if assets.records:
                projection['assets'] = assets.records
            for key in ('heading_anchors', 'link_aliases'):
                if key in unit:
                    projection[key] = unit[key]
            if correction:
                projection['correction_notice'] = correction
            course["units"].append(projection)
        course['linked_files'] = linked_files
        course['source_snapshot'] = read_source_snapshot(path.parent, item)
        course["closure_receipt_sha256"] = None
        if course["status"] == "complete":
            # Whole-course closure is independent of how many units happen to exist.
            cp = bound_file(path.parent, item.get("closure_receipt"), item.get("closure_receipt_sha256"))
            closure = json.loads(cp.read_text(encoding="utf-8"))
            inventory_path = bound_file(path.parent, item.get('target_inventory'), item.get('target_inventory_sha256'))
            inventory = json.loads(inventory_path.read_text(encoding='utf-8'))
            obligations = closure.get("target_item_ids", [])
            if inventory.get('course_id') != cid or inventory.get('target_item_ids') != obligations or closure.get('target_inventory_sha256') != digest(inventory_path):
                raise ValueError('closure does not bind independently fixed target inventory')
            if closure.get("course_id") != cid or not obligations or len(obligations) != len(set(obligations)):
                raise ValueError("complete course lacks an exact nonempty target inventory")
            if not all(closure.get(k) is True for k in ("inventory_complete", "generality_audit", "dependency_closure", "independent_audit")):
                raise ValueError("whole-course closure audits incomplete")
            rows = closure.get("dispositions", [])
            if len(rows) != len(obligations) or {r.get("item_id") for r in rows} != set(obligations):
                raise ValueError("course target inventory not covered exactly once")
            units_by_id = {u["id"]: u for u in course["units"]}
            for row in rows:
                state = row.get("disposition")
                if state in {"authored", "stronger_with_verified_specialization"}:
                    target = units_by_id.get(row.get("unit_id"))
                    if not target or target["admission"] != "admitted" or row["item_id"] not in target["mathematical_item_ids"]:
                        raise ValueError("course item lacks a bound admitted unit")
                    if state == "stronger_with_verified_specialization" and row.get("specialization_checked") is not True:
                        raise ValueError("stronger theorem lacks specialization proof")
                elif state == "exact_open_import":
                    if row.get("exact_correspondence") is not True or not row.get("license") or not HASH.fullmatch(row.get("import_sha256", "")):
                        raise ValueError("open import lacks exact semantic/license/byte identity")
                    public_text(row.get("citation"), "open import citation")
                elif state in {"duplicate", "nonmathematical"}:
                    public_text(row.get("justification"), "exclusion justification")
                else:
                    raise ValueError("open, weaker or unsupported item disposition")
            course["closure_receipt_sha256"] = digest(cp)
        course["href"] = f"courses/{cid}/index.html"
        course["unit_count"] = len(course["units"])
        course["admitted_unit_count"] = sum(u["admission"] == "admitted" for u in course["units"])
        courses.append(course)
    for course in courses:
        validate_course_links(course, sources, courses)
    return {"schema": "stacks-reader-courses/v1", "snapshot": public_text(raw.get("snapshot"), "snapshot"), "catalog_sha256": digest(path), "courses": courses}, sources
