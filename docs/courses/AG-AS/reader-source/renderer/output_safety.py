"""Non-destructive output isolation for reader and standalone course builds."""
from pathlib import Path
import stat


def isolated_path(path: Path, protected=()) -> Path:
    # Inspect the lexical ancestors before resolve() can hide a symlink/junction.
    path = path.absolute()
    for part in (path, *path.parents):
        try:
            info = part.lstat()
        except FileNotFoundError:
            continue
        if (stat.S_ISLNK(info.st_mode)
                or getattr(info, 'st_file_attributes', 0)
                & getattr(stat, 'FILE_ATTRIBUTE_REPARSE_POINT', 0x400)):
            raise ValueError('reader output must not traverse a symlink or reparse point')
    resolved = path.resolve()
    for input_path in protected:
        input_path = Path(input_path).resolve()
        if resolved.is_relative_to(input_path) or input_path.is_relative_to(resolved):
            raise ValueError('reader output overlaps a protected input')
    return resolved


def fresh_directory(path: Path, protected=()) -> Path:
    path = isolated_path(path, protected)
    if path.exists() and (not path.is_dir() or next(path.iterdir(), None) is not None):
        raise ValueError('reader output must be a fresh empty directory; existing bytes are preserved')
    return path
