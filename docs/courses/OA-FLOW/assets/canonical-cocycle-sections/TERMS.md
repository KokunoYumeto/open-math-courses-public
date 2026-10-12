# Original figure sources and verification

The original plotting code, mathematical figure design, diagnostics and rendered illustrations in this directory are dedicated under CC0-1.0 to the extent of rights held. They are independently constructed from the equations in the three adjacent lessons. No source-publication image, extracted page, copied illustration or font file is included.

Run `python render.py` to reproduce the three original SVG/PNG pairs and `diagnostics.json`. Run `python render_support_continuity.py` for `support-continuity.svg`, `support-continuity.png` and `support-continuity.json`. The dependencies are Python, NumPy and Matplotlib. The renderer uses the runtime's DejaVu Sans; that existing font retains its own terms. SVGs retain text references to the font. No author or public attribution name is inferred from a local account path.

The figures show these exact mathematical objects:

- `weight-coordinates`: the two entries of `diag(3,1) e^p`, the strict spectral-cut thresholds, and the proved tail `4/(2*pi*a)` (WC13 and WC diagnostics).
- `canonical-section`: the actual phase `0.7(2*z*q-q^2)` with dual translation `(z,q) -> (z+s,q+s)`, and the decreasing diagonal strips that obstruct a normal joint extension (CS26–27).
- `support-continuity`: the exact scalar densities `h_n(p)=exp(p)/n`, their bounded resolvents, and the vector spectral measures on `[log(n)-1, log(n)]` whose unit mass escapes when the support drops from one to zero (WCH14a–c). The vector measures are distinct from the canonical core trace.
- `weight-change`: the exact balanced matrix-entry formula, the piecewise affine maps `T_n` that preserve every cell, and the proved resolvent/displacement/section-distance bounds (WCH10–11, WCH22–33). Its Cantor image is explicitly a finite-stage outer approximation; the text proves the infinite-set measure and estimates.

The numeric phase residual and map-vertex checks are reproducibility diagnostics. They do not replace the full symbolic, domain, normality or measure arguments in the lessons. Earlier pixel inspection records in `../INPUTS.json` identify their inspected PNG hashes. Each renderer also records the hashes of its own figure outputs in its diagnostic data.
