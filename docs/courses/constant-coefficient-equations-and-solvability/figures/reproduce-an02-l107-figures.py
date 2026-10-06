"""Run the retained original L107 plotting source in an isolated output folder.

Original wrapper, GPT-6.1 Sol (OpenAI), Ultra; CC0.
Requires NumPy, SymPy and Matplotlib in the current Python environment.
The mathematical proof is in AN02-L107.html beside the course figure directory.
"""
from pathlib import Path
import shutil
import subprocess
import sys

HERE = Path(__file__).resolve().parent
SOURCE = HERE / 'an02-l107-elliptic-make-figures.py'
OUTPUT = HERE / 'an02-l107-reproduced'

def main():
    OUTPUT.mkdir(exist_ok=False)
    # The original script binds its own historical basename in its checks.
    # Copying its exact bytes under that basename makes it independently runnable.
    shutil.copyfile(SOURCE, OUTPUT / 'make_figures.py')
    subprocess.run([sys.executable, str(OUTPUT / 'make_figures.py')], cwd=OUTPUT, check=True)
    mapping = {'threshold-regions.png': 'an02-l107-elliptic-threshold-regions.png',
               'threshold-regions.svg': 'an02-l107-elliptic-threshold-regions.svg',
               'scale-intervals.png': 'an02-l107-elliptic-scale-intervals.png',
               'scale-intervals.svg': 'an02-l107-elliptic-scale-intervals.svg',
               'figure-validation.json': 'an02-l107-elliptic-figure-validation.json'}
    for original, supplied in mapping.items():
        shutil.copyfile(OUTPUT / original, OUTPUT / supplied)
    print('Generated figures and exact checks in ' + OUTPUT.name)

if __name__ == '__main__': main()
