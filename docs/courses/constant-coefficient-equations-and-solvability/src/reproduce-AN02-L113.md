# Reproduce the shrinking-cone figures

The two original figures in [Fundamental solutions in shrinking cones](fundamental-solutions-in-shrinking-cones.md) show the exact closed cone sections and the exact transport directions used in the proof. They show support enclosures and inverse directions, with no numerical fundamental solution or assertion of exact support.

## Download the six supplied files

Keep the supplied files unchanged. Download each named file from the links below. For a fresh replay, copy only the renderer into an empty scratch directory. It writes five output files beside its own location.

- [cone-transport.png](../reproduce/L113/assets/cone-transport.png) — 67320 bytes. SHA-256: `2983B0E67ABF4BDFC3766E74BB9D3A1A3506EA07F89A73C773C525359142EF20`.
- [cone-transport.svg](../reproduce/L113/assets/cone-transport.svg) — 48009 bytes. SHA-256: `91C645BB6AFBA43BBE1C358AAC86CE4CA4C97E08E3F1FDEFE6976FEE9E82691B`.
- [decreasing-cones.geometry.json](../reproduce/L113/assets/decreasing-cones.geometry.json) — 2396 bytes. SHA-256: `8C4B0E4CC553A7129855E71D036BFF78E798F2909D948033B51A027F7B51D0B0`.
- [render_decreasing_cones.py](../reproduce/L113/assets/render_decreasing_cones.py) — 4118 bytes. SHA-256: `D7A531ECA5A2E58DFC0F5F462E5B4653C0914B1898FDC8A5CC71FB1B273640BC`.
- [shrinking-cones.png](../reproduce/L113/assets/shrinking-cones.png) — 61635 bytes. SHA-256: `E033F79F5BE41FD388926316F8DBB9A677D0BECF1F27DA2CD44D0E66A49CE6DD`.
- [shrinking-cones.svg](../reproduce/L113/assets/shrinking-cones.svg) — 45586 bytes. SHA-256: `64A7180848B9694F7477F7655AD01E4EFC56332A1DF270B00DC215FDF9AD3938`.

## Run a fresh replay

The renderer requires Python, Matplotlib and NumPy. From the scratch directory containing the renderer, run:

```text
python -X utf8 render_decreasing_cones.py
```

It creates `decreasing-cones.geometry.json`, `shrinking-cones.png`, `shrinking-cones.svg`, `cone-transport.png` and `cone-transport.svg`. Compare these five outputs with the supplied files; the unchanged renderer is the sixth package file.

The observed replay used Python 3.13.9, Matplotlib 3.10.9 and NumPy 2.4.4 with Matplotlib’s bundled DejaVu Sans font. All six files matched byte for byte in that environment. Both PNGs and both SVGs matched exactly; the SVG Date and hash salt are fixed by the supplied renderer. No date or identifier normalization was needed for this comparison. Other library or font versions can change rendered bytes. The geometry JSON records the mathematical coordinates separately from the drawing libraries. This record establishes reproducibility in the observed environment, with no claim of byte identity across every software version.

## Check the objects shown

The shrinking-cone PNG has 1168×880 native pixels. Its horizontal coordinate is t and its vertical coordinate is y; all real x are unrestricted. For j=1,2,4,8 the section clipped at y=4 has vertices (0,0), (−4/j,4), (4/j,4). Both sloping faces and the vertex are included. The intersection is the vertical ray t=0, y≥0. See DC2–DC4 and the complete Figure 1 caption.

The transport PNG has 1168×912 native pixels. Here j=2, the start is (t,y)=(0,0.8), and displacement is (−s/ξ,s). The arrows use ξ=±2 and ±4 and end at s=2.4. Boundary directions |ξ|=j are included. For ξ=1 the first boundary contact is (−0.8,1.6), after which the displayed dashed ray leaves the cone. See DC9–DC10 and the complete Figure 2 caption. The transport is for the transpose Q=P(−D), as stated in the lesson.

## Credits and reading scope

The renderer, geometry and diagrams are original GPT-6.1 Sol (OpenAI) work, October 2026, CC0. Matplotlib and its font components retain their own terms. The lesson gives precise freely readable Enqvist and Crétier source locators and the exact internal Fourier and Banach provider scopes. Its complete specialized arguments, three examples and five solutions accompany the figures. The bounded independent AI review covers that accepted lesson and its figures; recursive prerequisite closure and whole-course review remain incomplete.
