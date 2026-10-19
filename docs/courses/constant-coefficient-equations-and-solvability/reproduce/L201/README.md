# Holomorphic boundary illustrations

These two original figures accompany *Resolving singular directions at a holomorphic boundary*. They include editable-text SVGs, PNGs, exact parameter data and reproducible Python source.

The boundary-patch figure shows the imaginary unit circle patch centered at the negative of a selected unit covector and the opposite cone of possible frequencies. The strip figure plots the exact complementary multipliers `1/(1+exp(2 xi))` and `1/(1+exp(-2 xi))`. The lesson captions distinguish these bounds and multiplier values from an actual input wavefront set.

Run `python holomorphic-boundary-figures.py` with Python, NumPy and Matplotlib. The program writes figures to `figures/` and requires existing figure bytes to match the reproduced output. Use `--overwrite` to regenerate the figures after editing their parameters. The original program, data and illustrations use the CC0 terms in `LICENSE.txt`.
