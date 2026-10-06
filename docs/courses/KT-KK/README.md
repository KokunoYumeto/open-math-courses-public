# Kasparov’s KK-theory

This draft edition contains 21 of 23 planned lessons: 01–18 and 20–22, plus companions on matrix positivity, noncompact induction foundations and cohomological Thom foundations. The other two lessons are still being written. Asymptotic composition, scalar comparison, KK-to-E functor, both Bott products, simultaneous suspension, half-exactness and both six-term sequences proved; all four exercises solved. The stronger universal property and nuclear comparison are unused stated results. Deformation asymptotic classes, direct K-theory map, tangent-groupoid closed index comparison and both Euclidean inverse E Bott products proved; four exercises solved. Each lesson states its hypotheses and earlier proof dependencies. Lesson15 proves the assigned closed-manifold KK symbol and embedding index theorem in both Clifford degrees. Lesson16 proves wrong-way maps for possibly nonproper K-oriented maps, their composition, homotopy and projection formulas, and the global Thom/Dirac comparison. Lesson20 proves assembly construction/naturality, the finite-group case and the covering Dirac/Mishchenko comparison; lattice assembly and general trace-image integrality remain explicitly unproved and unused. Lesson07 proves its scalar Fredholm pictures and separable extension comparison; its broader arbitrary-source compact-homology comparison is stated without proof and is not used as a premise.

The lesson text, solutions, companions and original figures use CC0 1.0. Reading references retain their authors’ terms. MathJax and fonts retain the supplied notices.

## Reading and downloads

The HTML readers, cumulative PDF and LaTeX contain the same 21 lessons and three companions. The editable source ZIP contains their Markdown, individual and cumulative LaTeX, figure sources, notices and builder. Earlier supporting programme lessons are accessible through the reader links and in the repository; they are not included in this ZIP. This is an editable source download, not an offline copy of the prerequisite programme.

## Reproduce

Run `python build_sources.py` with Pandoc installed. The builder uses the ordered lesson and supplement list in `course.json`, preserving the supplied figure assets. Run LuaLaTeX twice on `KT-KK.tex` to produce the cumulative PDF. The document uses standard packages including amsmath, amssymb, graphicx and hyperref.

The `assets` folder contains SVG diagrams and rendered PNGs. The `figures` folder contains the radial metric plot and wrong-way diagrams as PNG, SVG and Python sources, together with the cotangent and index-comparison PNGs and their Python sources; NumPy and Matplotlib are needed only to regenerate that plot.
