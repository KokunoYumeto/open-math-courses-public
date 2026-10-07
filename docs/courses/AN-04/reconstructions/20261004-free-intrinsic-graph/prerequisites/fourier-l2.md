# Fourier transforms on the complete square-integrable space

This companion selects AN03-P001, *Fourier transforms, finite spectra and
convex separation*, Section 7.1 and the pairing and multiplier arguments
of Section 7.3. It preserves both inverse maps and their exact factors.
The connecting distributional argument below is supplied in this selection.

This is a separate modified selection from the earlier AN-03 programme.
Original principal author and publisher: AN-03 course-writing
task / AN-03 local course project, 2026. Earlier modification: AN-03 course-writing task and OpenAI Codex.
Selection and the explicitly identified connecting arguments: GPT-6 Astra
(OpenAI), Ultra, 4 October 2026.

Original text: CC0.

## L0. Exact earlier inputs

[Measure and the complete square-integrable space](measure-and-l2.md)
proves the completed Lebesgue measure, convergence theorems, \(L^1,L^2\)
inequalities, \(L^2\) completeness, compact smooth density and simultaneous
\(L^1\cap L^2\) density. Its M8 proves agreement with the integrals in the
earlier [Schwartz Fourier proofs, U001 Q3–Q4](../../20261004-free-stationary-phase/quadratic-stationary-phase.md#q3-schwartz-estimates-and-the-signs-in-the-fourier-rules)
and [Schwartz Parseval proof, U001 Appendix A.2](../../20261004-free-stationary-phase/stationary-phase-and-critical-manifolds.md#a-2-plancherel-and-the-pairing-calculation).
In the retained text below, Theorem 1.1 means that inversion proof and
Theorem 2.1 means that Parseval proof. Thus the original AN03 paragraph
labels identify fully supplied earlier proofs.

We write \(Ff(\xi)=\int e^{-ix\cdot\xi}f(x)\,dx\) and
\(Gh(x)=(2\pi)^{-d}\int e^{ix\cdot\xi}h(\xi)\,d\xi\) initially on Schwartz
functions.

## L1. Both inverse maps

Suppose first that \(d\geq1\). Compact smooth functions are dense in \(L^2\), by the explicit truncation, grid and smooth box-layer proof in M7, and belong to the Schwartz space. For \(f\in L^2\), choose Schwartz \(f_j\to f\) in \(L^2\). Theorem 2.1 gives the exact difference identity
\[
 \|Ff_j-Ff_k\|_2=(2\pi)^{d/2}\|f_j-f_k\|_2.
                                                               \tag{FL1}
\]
Completeness makes this a convergent sequence. If \(\widetilde f_j\to f\) is another such sequence, its difference from \(f_j\) tends to zero in \(L^2\), so (FL1) gives the same output. Define \(Ff\) as that limit. Linearity follows by approximating each summand and taking limits; the norm identity follows from continuity of the norm.

For Schwartz \(h\), Theorem 1.1 gives \(F(Gh)=h\), and Theorem 2.1 applied to \(Gh\) gives \(\|Gh\|_2=(2\pi)^{-d/2}\|h\|_2\). Thus the same construction extends \(G\) to \(L^2\). Applying continuity to \(GFf_j=f_j\) and \(FGh_j=h_j\) proves, on the original entire spaces,
\[
 \begin{split}
 F,G&:L^2(\mathbb R^d)\longrightarrow L^2(\mathbb R^d),\\
 GF&=I,\qquad FG=I,\\
 \|Ff\|_2&=(2\pi)^{d/2}\|f\|_2,\qquad
 \|Gh\|_2=(2\pi)^{-d/2}\|h\|_2 .
 \end{split}                                                   \tag{FL2}
\]
These are bijections with their original norms. In dimension zero the measure is the point mass on the one point \(\mathbb R^0\), the space is \(\mathbb C\), and both maps are the identity with \((2\pi)^0=1\). No assertion that this point is null is used in that case.

## L2. Ordinary integrals and distributions

For \(f\in L^1\cap L^2\), choose the simultaneous approximants from M7.
The ordinary Fourier integrals satisfy
\[
 \sup_\xi|Fv_j(\xi)-F_{\rm integral}f(\xi)|\le\|v_j-f\|_1,\qquad
 \sup_x|Gv_j(x)-G_{\rm integral}f(x)|
       \le(2\pi)^{-d}\|v_j-f\|_1. \tag{L1}
\]
Their \(L^2\) limits are the maps of L1. The completeness proof M6,
applied to a subsequence with summable differences, supplies a pointwise
almost-everywhere convergent subsequence with that same \(L^2\) limit:
the pointwise tail is dominated by its summable absolute differences.
The uniform limit in (L1) therefore equals the \(L^2\) limit almost
everywhere. Both extensions agree with their ordinary integrals.

Every \(f\in L^2\) defines a tempered distribution by
\(\langle f,\phi\rangle=\int f\phi\): Cauchy–Schwarz bounds this by
\(\|f\|_2\|\phi\|_2\), and the dyadic estimate in M8 bounds
\(\|\phi\|_2\) by a Schwartz seminorm. If Schwartz \(f_j\to f\) in
\(L^2\), Fubini for the absolutely integrable Schwartz product gives
\[
 \int Ff_j(\xi)\phi(\xi)\,d\xi
       =\int f_j(x)F\phi(x)\,dx.
\]
Both sides converge by Cauchy–Schwarz, since \(F\phi\) is Schwartz and
\(Ff_j\to Ff\) in \(L^2\). Hence
\[
 \langle Ff,\phi\rangle=\langle f,F\phi\rangle. \tag{L2}
\]
This is precisely the distributional transpose convention in U001 A.2.
The identical calculation with \(G\) includes its factor \((2\pi)^{-d}\).
There is no change of Fourier convention between the distributional
and \(L^2\) arguments of the graph lesson.

## L3. Pairing and measurable multipliers

Approximating both inputs by Schwartz functions in \(L^2\), Theorem 2.1 and Cauchy–Schwarz prove
\[
 \langle u,v\rangle
   =(2\pi)^{-d}\int_{\mathbb R^d}
                     Fu(\xi)\overline{Fv(\xi)}\,d\xi .
                                                               \tag{FL5}
\]
The inner product is linear in the first variable. Each pairing difference tends to zero by the sum of the two Cauchy–Schwarz bounds, so the original factor persists.

If \(b\) is a measurable scalar frequency function with
\(\|b\|_\infty\leq B\), multiplication by \(b\) respects the completed null classes and maps \(L^2\) to itself with norm at most \(B\). Hence
\[
 \begin{split}
 T_b&=G\,M_b\,F,\qquad M_bh=bh,\\
 \|T_bf\|_2
 &\leq(2\pi)^{-d/2}B(2\pi)^{d/2}\|f\|_2=B\|f\|_2,\\
 \langle T_bu,v\rangle
 &=(2\pi)^{-d}\int b(\xi)Fu(\xi)\overline{Fv(\xi)}\,d\xi
   =\langle u,T_{\overline b}v\rangle .
 \end{split}                                                   \tag{FL6}
\]
This proves the actual adjoint \(T_b^*=T_{\overline b}\). It uses the constructed inverse maps, not an assumed representation of an \(L^p\) dual space. For Schwartz \(f\), \(bFf\in L^1\cap L^2\), so \(T_bf\) is exactly the original inverse integral. These statements apply in the elliptic chapter with \(d=n\geq1\); its arbitrary value of the symbol at zero changes no frequency integral.

For a bounded measurable scalar \(b\) and Schwartz \(f\), the last
ordinary-integral assertion follows from L2: \(bFf\) is in \(L^1\cap L^2\).
A matrix multiplier in finite dimension follows by applying the scalar
construction to its finitely many entries; its norm estimate follows
pointwise from its chosen operator norm before integration. In particular,
indicators of measurable dyadic annuli and multiplication by \(e^{ih}\)
for real measurable \(h\) are legitimate. The latter preserves the
Fourier \(L^2\) norm because \(|e^{ih}|=1\).

The free human sources of the new measure and completeness inputs are
listed in the [measure companion](measure-and-l2.md#free-source-comparisons).
The already selected free human source chain for Schwartz inversion and
Parseval remains the one of U001. Every used programme argument is linked
above or proved here; these readings replace none of them.
