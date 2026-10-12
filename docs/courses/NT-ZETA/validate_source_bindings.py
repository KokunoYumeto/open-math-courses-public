"""Check the zeta course's source identities, downloads and figure identities.

Run with Python 3 from the extracted NT-ZETA directory. No third-party packages
or network access are needed. This verifies bytes, not mathematical proofs.
Original validation code: OpenAI GPT-6 Astra, Ultra; CC0 1.0, October 2026.
"""
import hashlib
import json
from pathlib import Path, PurePosixPath


def safe_relative(value):
    if not isinstance(value, str) or not value or '\\' in value or ':' in value:
        raise ValueError('Invalid relative path')
    path = PurePosixPath(value)
    if path.is_absolute() or any(p in ('', '.', '..') for p in value.split('/')):
        raise ValueError('Unsafe relative path: ' + value)
    return value


def validate(document, read):
    """Read exact named bytes through read(relative_path); never change records."""
    if document.get('id') != 'NT-ZETA' or not document.get('units'):
        raise ValueError('Wrong or empty course manifest')
    ids, sources = set(), set()
    figures = 0
    for unit in document['units']:
        identity = unit['id']
        name = safe_relative(unit['source'])
        if identity in ids or name in sources or name != identity + '.md' or '/' in name:
            raise ValueError('Duplicate or inconsistent lesson identity: ' + identity)
        ids.add(identity)
        sources.add(name)
        source = read('src/' + name)
        if hashlib.sha256(source).hexdigest() != unit['sha256'].lower():
            raise ValueError('Stale source hash: ' + identity)
        if source != read('downloads/' + name):
            raise ValueError('Download differs from canonical source: ' + identity)
        for asset in unit.get('assets', []):
            path = safe_relative(asset['source'])
            content = read(path)
            if hashlib.sha256(content).hexdigest() != asset['source_sha256'].lower():
                raise ValueError('Stale figure identity: ' + path)
            if len(content) != asset['bytes']:
                raise ValueError('Stale figure size: ' + path)
            figures += 1
    for path in document.get('figure_sources', []):
        read(safe_relative(path))
    return {'lessons': len(ids), 'figure_bindings': figures,
            'source_download_pairs_equal': True, 'proofs_certified': False}


if __name__ == '__main__':
    root = Path(__file__).resolve().parent
    document = json.loads((root / 'course.json').read_bytes())
    print(json.dumps(validate(document, lambda p: (root / p).read_bytes()), indent=2))
