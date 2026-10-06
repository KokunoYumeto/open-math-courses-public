# Reproducing the compact-division figures

The original proof, explanatory text, coordinate ledger, plotting source and six figure files are CC0. The source book pages are private verification evidence and are not part of this component.

Use Python with Matplotlib and NumPy. To reproduce into a fresh directory without changing the checked originals:

```text
python -B -X utf8 make_figures.py --output-dir <fresh-output-directory>
```

The source generates three PNG files, their SVG counterparts and `geometry.json`. CF-A depicts the exact rectangle, supporting plane, disk carrier and gap in the proof's Figure CF-A. CF-B depicts the three actual roots, both equal-modulus factors, safe radius and two explicitly distinguished lower bounds. CF-C diagrams both distribution pairings for the double root with the exact Fourier and transpose signs. Each figure caption identifies its proof locators. None of the pictures is a numerical substitute for a universal theorem.
