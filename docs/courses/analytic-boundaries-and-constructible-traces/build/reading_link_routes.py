"""Project source-relative parent links without erasing course boundaries.

Portable readings use course-relative links unless a destination starts with
``../``. Those links are relative to the editable source, usually in src/.
"""
import posixpath
import re
from urllib.parse import urlsplit, urlunsplit


def project_parent_links(text, source, reader):
    def replace(match):
        destination = match.group(2)
        parts = urlsplit(destination)
        if parts.scheme or parts.netloc or not parts.path.startswith('../'):
            return match.group(0)
        target = posixpath.normpath(posixpath.join(posixpath.dirname(source), parts.path))
        relative = posixpath.relpath(target, posixpath.dirname(reader) or '.')
        return match.group(1) + urlunsplit(('', '', relative, parts.query, parts.fragment)) + match.group(3)

    return re.sub(r'(\]\()([^\s)]+)(\))', replace, text)
