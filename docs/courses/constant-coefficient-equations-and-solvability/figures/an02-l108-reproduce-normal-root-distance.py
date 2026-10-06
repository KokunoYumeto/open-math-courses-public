"""Reproduce the exact normal-root figure with its published asset names.

Requires Python, NumPy and Matplotlib. The accompanying original plotting
source is byte-preserved and writes normal-root-distance.png/.svg and
geometry.json. This wrapper renders in a temporary directory, checks every
output, then copies the checked outputs beside itself with their unique names.
"""
from pathlib import Path
import hashlib
import shutil
import subprocess
import sys
import tempfile

HERE = Path(__file__).resolve().parent
SOURCE = HERE / 'an02-l108-render-normal-root-distance.py'
SOURCE_SHA = 'C3F442D348EBCEE3D7E966A3245C87F79D8D3E0CB6A6588ABFA3E51AFE0FAD8A'
EXPECTED = {'normal-root-distance.png': '546B4A2933CEFC60B5A1ABECB52B9BF43F8FC411771F611BF3DCD1FAE339CB29', 'normal-root-distance.svg': '0B1D425B60697FD184D22F0E12E430F7898FFEFB5FBB062C017981A9E649C25E', 'geometry.json': '81E74FFFB1BE67B8C1A7DDC385842C6DBE08934F473EB20CFC629B55FF582BA8'}
NAMES = {'normal-root-distance.png': 'an02-l108-normal-root-distance.png', 'normal-root-distance.svg': 'an02-l108-normal-root-distance.svg', 'geometry.json': 'an02-l108-normal-root-geometry.json'}

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()

def main():
    if sha(SOURCE) != SOURCE_SHA:
        raise SystemExit('The accompanying original plotting source differs from the expected version.')
    with tempfile.TemporaryDirectory(prefix='an02-normal-root-') as tmp:
        temp = Path(tmp)
        script = temp / SOURCE.name
        shutil.copyfile(SOURCE, script)
        subprocess.run([sys.executable, str(script)], check=True)
        for original, expected in EXPECTED.items():
            if sha(temp / original) != expected:
                raise SystemExit('Reproduction differs for ' + original + '; no published assets were replaced.')
        for original, renamed in NAMES.items():
            shutil.copyfile(temp / original, HERE / renamed)
    print('Both figure formats and exact geometry reproduced with the expected hashes.')

if __name__ == '__main__':
    main()
