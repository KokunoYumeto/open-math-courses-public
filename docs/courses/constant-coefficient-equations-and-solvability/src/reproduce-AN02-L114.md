# Reproduce the Schwartz evolution and delay figures

The two original figures in [Root growth and Cauchy evolution in Schwartz spaces](root-growth-and-cauchy-evolution-in-schwartz-spaces.md) show the exact time-root signs and the exact support points of the causal delay inverse. The complete proofs, six solved exercises and full captions accompany them.

## Download the original files

Keep this directory structure in an empty scratch directory: `build_and_check.py` at its root, with the five figure files in `figures/`. The renderer creates the figure directory itself during a fresh run. Each download below has its original bytes.

- [build_and_check.py](../reproduce/L114/build_and_check.py) — 9010 bytes. SHA-256: `5D9C85BA679C89ED0BD7F1E5A50A4547BB8F9D6D363AE13C58E1677313589C5C`.
- [delay-convolution-support-032.png](../reproduce/L114/figures/delay-convolution-support-032.png) — 117037 bytes. SHA-256: `4F86DF306AF189B65F0A187618E9094B49090DE62B056C2A95F29ED639E5B6A6`.
- [delay-convolution-support-032.svg](../reproduce/L114/figures/delay-convolution-support-032.svg) — 79545 bytes. SHA-256: `F9F2AE02C581A9467C25C814537CD3CAC5AA3EAA949EFD48A8AD49C942A00BC7`.
- [geometry.json](../reproduce/L114/figures/geometry.json) — 1218 bytes. SHA-256: `27E5F7657328A9DE8E107BE195FDA18D888EAD2A91D55DD53A081D14A8D0B175`.
- [time-root-growth-032.png](../reproduce/L114/figures/time-root-growth-032.png) — 118991 bytes. SHA-256: `8FB382CA5FBB5C1D52867BEE18E83D1DB9AAE7B25672B427EB8D9050921D0F64`.
- [time-root-growth-032.svg](../reproduce/L114/figures/time-root-growth-032.svg) — 55422 bytes. SHA-256: `2CA86874D88D12422070A51DF34C636CEF89E5568BC37A9BE40462A661E1E907`.

## Run the supplied program

The unchanged program requires Python, NumPy, SymPy, SciPy and Matplotlib. In the empty scratch directory containing only the downloaded program, run:

```text
python -X utf8 build_and_check.py
```

It writes the two PNGs, two SVGs and `figures/geometry.json`, and produces `checks.json` with exact symbolic identities, independent heat integrals and numerical checks of the proved matrix bound. It also creates an empty `src/` directory. No other material is needed. The optional manuscript-copy branch is inactive when no `manuscript.md` is present.

The observed fresh replay used Python 3.13.9, NumPy 2.4.4, SymPy 1.13.1, SciPy 1.17.1 and Matplotlib 3.10.9, with Matplotlib’s bundled DejaVu Sans font. The supplied program and all five figure outputs matched byte for byte in that environment; both PNGs also matched decoded RGBA pixels. The SVG date is omitted and the hash salt is fixed by the supplied program. No date or identifier normalization was used. Other software or font versions can change rendering bytes. The geometry JSON records the exact mathematical expressions and support points independently of the drawing libraries.

## Check the objects and signs

Figure 1 has 1768×1071 native pixels. It samples 801 real frequencies from −4 to 4, with horizontal coordinate ξ and vertical coordinate Im z. The forward heat curve is Im z=ξ², the logarithmic multiplier curve is Im z=−log(1+ξ²), and backward heat is Im z=−ξ². The conversion is λ=iz, so Re λ=−Im z. Negative imaginary roots grow in positive time. The displayed continuous curves interpolate numerical samples of these exact expressions. See equations (35), (37), (42) and the full Figure 1 caption.

Figure 2 has 1598×1088 native pixels, with horizontal coordinate x and vertical coordinate t. Its first five exact support points are (t,x)=(k,0), k=0,1,2,3,4, with spatial derivative orders 2k. The full support is the discrete set {(k,0): k≥0}. The shaded cone t≥|x| contains this support; the distribution does not have the whole cone as support. No distribution values are plotted. See equations (43)–(46), Exercise 6 and the full Figure 2 caption.

## Credits and proof scope

The program, geometry and diagrams are original GPT-6.1 Sol (OpenAI), Ultra work, October 2026, dedicated under CC0. Matplotlib and font components retain their own terms. The human mathematical sources include work by Laurent Schwartz, Jan Kisyński and I. G. Petrovskii, with precise reading qualifications in the lesson. The original 1938 Petrovskii article is historical bibliographic attribution only and supplies no required proof.

Fourier, Fréchet and algebraic providers retain the exact declared scopes. The lesson proves the autonomous finite-dimensional logarithmic evolution theorem and its scalar nowherezero leading-time specialization, including characteristic heat and the explicit delay inverse. The general compact-kernel convolution support and reciprocal theorem remains a separate unproved task.
