# Reproduce the local Fourier quotient diagrams

Read the complete learner and formal proof. The reader retains LP0–LP10, every LP1–LP27 equation, three worked examples, six complete solutions and all three figures with their full captions. Return to the L011 local-annihilator receiver.

## Exact original downloads

All eleven files below retain their original bytes. Keep the renderer, original proof, original README and licence at the root of a fresh scratch directory and the seven figure/geometry files in `figures/`.

- [local-polynomial-annihilator-proof.md](../reproduce/L123/local-polynomial-annihilator-proof.md) — 26956 bytes; SHA256 `4272787FD760CC61926DBAF883B642DE902271507E4009F63E3864015867169C`.
- [make_figures.py](../reproduce/L123/make_figures.py) — 8171 bytes; SHA256 `4583CA03AA65ED58D0FDA7315E74EC83771F07EA8DBCD0BD22ABD249F0EB910A`.
- [README-reproduce.md](../reproduce/L123/README-reproduce.md) — 2309 bytes; SHA256 `80C815D9C8E2F201BBE28B0A980CD3A151F823D57DB171816D22594B52FA262B`.
- [LICENSE-ORIGINAL.txt](../reproduce/L123/LICENSE-ORIGINAL.txt) — 549 bytes; SHA256 `76B0CD8C9C2F0F37B7F6F13C08318093D4FFA5E3FFCE39333E77CA95375DA953`.
- [geometry.json](../reproduce/L123/figures/geometry.json) — 2469 bytes; SHA256 `B0FA501D91C6270CDF015D976AAD896335C6CDDE00BAA57260D3C7DB75158407`.
- [local-quotient-global-pole.png](../reproduce/L123/figures/local-quotient-global-pole.png) — 129997 bytes; SHA256 `CF7226B6CB871F4B48DE1BE818DD59ADA652D0EAAF6F1317619812587A16630B`.
- [local-quotient-global-pole.svg](../reproduce/L123/figures/local-quotient-global-pole.svg) — 73912 bytes; SHA256 `896AD6DD9F9D82517E4ADCD9C58E8A2C1C16F7A1B52A5016D682024B95D61D56`.
- [moments-to-local-quotient.png](../reproduce/L123/figures/moments-to-local-quotient.png) — 187089 bytes; SHA256 `7C17663DC52A9B1AD7303C91A644DBC30623A20C23BD2B6F56531A348BF1587B`.
- [moments-to-local-quotient.svg](../reproduce/L123/figures/moments-to-local-quotient.svg) — 100322 bytes; SHA256 `A1BBF53CCEDBFD4F47DA13528FE3AFCAFCA73B7CA66694B17E7A0A4AA67814D4`.
- [root-circle-and-analytic-unit.png](../reproduce/L123/figures/root-circle-and-analytic-unit.png) — 171091 bytes; SHA256 `1107CCE748F676299CBF2008FC88E476495695394E7EF34A4E0658DF48FC25D3`.
- [root-circle-and-analytic-unit.svg](../reproduce/L123/figures/root-circle-and-analytic-unit.svg) — 85949 bytes; SHA256 `E254D859E843BCA9DC385B01FD21961BDDE3132E3FD9E36DE84B0C36FD969223`.

## Fresh reproduction

The unchanged renderer requires Python, NumPy and Matplotlib. Choose an empty output directory:

```text
python -B -X utf8 make_figures.py --output fresh-figures
```

Compare all three PNGs, three SVGs and geometry.json with the supplied originals. The exact-map schematic keeps every phase, factorial and formal-transpose sign. The root diagram keeps the two inner roots with multiplicity, the extra root at −1, the contour radius 1/2 and inner radius 1/4. The final real slice retains the global pole and distinguishes the sharp complex-disk bound 4/3 from the general contour bound 8/3. Each complete caption states its proof locators and sample or schematic scope. Different software or fonts may change image bytes; the geometry states the exact mathematical objects.

## Credits, terms and boundary

[Original CC0 notice](../reproduce/L123/LICENSE-ORIGINAL.txt) and Reader credits retain GPT-6.1 Sol (OpenAI), Ultra and the human mathematical credit to Hörmander’s polynomial/exponential-polynomial annihilator context. The original LP10 paragraph retains all exact programme locators. L011 retains Malgrange’s density source. Source credit is not a proof closure or a licence for book expression. No external book prose, image or private review record is supplied. Matplotlib, DejaVu Sans and the existing MathJax reader retain their applicable component terms; no font binary is included.

The theorem proves a convergent quotient germ near zero. An entire quotient, compact inverse and ordinary support-hull alternative remain separately explained in L122. L011’s continuation needs every irreducible factor to vanish at zero. Lower foundations, compact singular-support hulls, general topology and course closure retain their stated scope.
