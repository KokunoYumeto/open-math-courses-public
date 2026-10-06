"""Reproduce the three original CC0 proof schematics beside this script."""
from pathlib import Path
import fitz
for source in [Path(__file__).with_name(name+'.svg') for name in ('normalization-gauss-proof-bridge','normalization-countable-traits-counterexample','component-ampleness-return')]:
    svg=fitz.open(stream=source.read_bytes(),filetype='svg')
    pdf=fitz.open('pdf',svg.convert_to_pdf())
    pdf[0].get_pixmap(matrix=fitz.Matrix(1,1),alpha=False).save(source.with_suffix('.png'))
