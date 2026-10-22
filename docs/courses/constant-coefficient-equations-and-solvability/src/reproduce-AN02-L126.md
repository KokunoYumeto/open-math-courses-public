# Reproduce Compact supports, a closed submanifold and the normal circle

[Read the complete lesson](../AN02-L126.html). The argument below uses the stated ordinary CD034 and selected tubular/Thom hypotheses. It proves the real compact closed–open sequence, its actual integration comparison and the annular normal-circle calculation. The complete earlier CO046 alternative is retained with its historical notation. [L127](../AN02-L127.html) separately supplies normalized form duality and its unshifted right-cap identification. L128 separately constructs the rational coefficient comparison and rational connecting map. 

## Exact original files and terms

The downloads contain the mathematical text, diagrams, exact coordinates and reproducible renderer. The original text and diagrams retain their CC0 dedication; MathJax and the supplied fonts retain their component licence notices. Human references and proof locators accompany the mathematical arguments.

Read the [complete supplied proof in its current reader presentation](../proof-AN02-L126.html). This complete supplied source contains both its formal argument and all learner examples and solutions. The original downloads below remain exact.

- [closed-open-forms-and-the-normal-circle.md](../reproduce/L126/closed-open-forms-and-the-normal-circle.md) — 37006 bytes; SHA256 `6ACD5535541CE3B5366AC894790FEF875E09F7BC60D557CF9441A4D4C6A07CDA`.
- [make_figures.py](../reproduce/L126/make_figures.py) — 5715 bytes; SHA256 `B5E83432AA048721D46CD391A397397C6883473CE23AF638D5ACD39396246932`.
- [README.md](../reproduce/L126/README.md) — 848 bytes; SHA256 `39F834D048710F2352E190E4D32AD4E3657EA7A4CB55835EEB24373C33E72CEB`.
- [LICENSE-original.txt](../reproduce/L126/LICENSE-original.txt) — 228 bytes; SHA256 `1E3FE7B1326967B8D5F2B28ED3B049920E7E511EB5977CFB2D4CAEA599BA4A31`.
- [figures/geometry.json](../reproduce/L126/figures/geometry.json) — 1567 bytes; SHA256 `F3306228C6A0C9F0797AEC52AC627443430CFB7EDE9099BA5D6EDE77DDF08293`.
- [figures/kernel-complex-to-open-support.png](../reproduce/L126/figures/kernel-complex-to-open-support.png) — 145441 bytes; SHA256 `39CE42439F3E5D11E8334EE26E2D80649333A41E33EC183BDDA746B5D36129B9`.
- [figures/kernel-complex-to-open-support.svg](../reproduce/L126/figures/kernel-complex-to-open-support.svg) — 55549 bytes; SHA256 `E428B9C55452FECA2F0EB11B4FFA1E04B57B21C85D9697DE5B269B407F745C8D`.
- [figures/radial-cutoff-and-normal-first-sign.png](../reproduce/L126/figures/radial-cutoff-and-normal-first-sign.png) — 136314 bytes; SHA256 `7156A01961E60CABF86164EE2CDCAE1C35EEF4F22F704C56F981ACAD9C24C9A2`.
- [figures/radial-cutoff-and-normal-first-sign.svg](../reproduce/L126/figures/radial-cutoff-and-normal-first-sign.svg) — 61314 bytes; SHA256 `D7CC121B14AD20EDB969E6F6C27C8431AC09A30EE73EB58FA174C31F57D437CD`.
- [original-CO046-alternative/closed-open-forms-and-the-normal-circle.md](../reproduce/L126/original-CO046-alternative/closed-open-forms-and-the-normal-circle.md) — 37005 bytes; SHA256 `9FCAF1A2859A17AB4918BCD925F6FF393E1B91E605039F775114B073664AED1B`.
- [original-CO046-alternative/make_figures.py](../reproduce/L126/original-CO046-alternative/make_figures.py) — 5715 bytes; SHA256 `B5E83432AA048721D46CD391A397397C6883473CE23AF638D5ACD39396246932`.
- [original-CO046-alternative/README.md](../reproduce/L126/original-CO046-alternative/README.md) — 848 bytes; SHA256 `39F834D048710F2352E190E4D32AD4E3657EA7A4CB55835EEB24373C33E72CEB`.
- [original-CO046-alternative/LICENSE-original.txt](../reproduce/L126/original-CO046-alternative/LICENSE-original.txt) — 228 bytes; SHA256 `1E3FE7B1326967B8D5F2B28ED3B049920E7E511EB5977CFB2D4CAEA599BA4A31`.
- [original-CO046-alternative/figures/geometry.json](../reproduce/L126/original-CO046-alternative/figures/geometry.json) — 1567 bytes; SHA256 `F3306228C6A0C9F0797AEC52AC627443430CFB7EDE9099BA5D6EDE77DDF08293`.
- [original-CO046-alternative/figures/kernel-complex-to-open-support.png](../reproduce/L126/original-CO046-alternative/figures/kernel-complex-to-open-support.png) — 145441 bytes; SHA256 `39CE42439F3E5D11E8334EE26E2D80649333A41E33EC183BDDA746B5D36129B9`.
- [original-CO046-alternative/figures/kernel-complex-to-open-support.svg](../reproduce/L126/original-CO046-alternative/figures/kernel-complex-to-open-support.svg) — 55549 bytes; SHA256 `E428B9C55452FECA2F0EB11B4FFA1E04B57B21C85D9697DE5B269B407F745C8D`.
- [original-CO046-alternative/figures/radial-cutoff-and-normal-first-sign.png](../reproduce/L126/original-CO046-alternative/figures/radial-cutoff-and-normal-first-sign.png) — 136314 bytes; SHA256 `7156A01961E60CABF86164EE2CDCAE1C35EEF4F22F704C56F981ACAD9C24C9A2`.
- [original-CO046-alternative/figures/radial-cutoff-and-normal-first-sign.svg](../reproduce/L126/original-CO046-alternative/figures/radial-cutoff-and-normal-first-sign.svg) — 61314 bytes; SHA256 `D7CC121B14AD20EDB969E6F6C27C8431AC09A30EE73EB58FA174C31F57D437CD`.

## Fresh native reproduction

Keep make_figures.py in a fresh directory and run:

```text
python -B -X utf8 make_figures.py --output fresh-figures
```

The renderer writes native PNG, SVG and exact geometry records. Check the complete original captions, coordinates, conventions and proof locators. The schematic and sampled figures explain the written proof. Different software or font versions may change rendering bytes.

The statements use the specified orientation, Thom and comparison hypotheses. Integral descent, rational-form spanning, the particular affine C8 representative, coefficient conventions and component constancy require their additional arguments. Exposition: GPT-6.1 Sol (OpenAI), Ultra, October 2026; CC0-1.0. [L124](../AN02-L124.html) gives the projective-exhaustion context; [L125](../AN02-L125.html) proves the geometric finite-chain H statement.
