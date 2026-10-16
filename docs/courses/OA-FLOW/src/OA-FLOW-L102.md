# Spectral fibers of circle translation

Write \(\mathbb T=\mathbb R/\mathbb Z\), equip it with normalized Haar measure, and put \(u(s)=e^{2\pi is}\). Translation on \(L^\infty(\mathbb T)\) has precisely one scalar degree of freedom in each integer frequency. We prove this as a statement about equivalence classes, with explicit normal projections and convergent Fourier approximations.

*Original expression: CC0-1.0 to the extent of rights held.*

<a id="oa-flow.circle.translation"></a>

## Translation and its Fourier coefficients

Let \(M=L^\infty(\mathbb T)\), acting by multiplication on \(L^2(\mathbb T)\), and define
\[
 (\alpha_t f)(s)=f(s+t),\qquad
 \widehat f(n)=\int_{\mathbb T}f(s)e^{-2\pi ins}\,ds.
 \tag{C1}
\]
Translation preserves null sets, so the definition is independent of the representative. It preserves multiplication, adjoints and the essential supremum norm, and \(\alpha_{-t}\) is its inverse.

We record why this is a von Neumann algebra in the stated representation. The map \(f\mapsto M_f\) is isometric: the upper norm bound is immediate, and indicators of sets where \(|f|>r\) give the lower bound for every \(r<\|f\|_\infty\). If \(B\in B(L^2(\mathbb T))\) commutes with all bounded multipliers, let \(h=B1\). Then \(Bg=gh\) for every bounded \(g\). For a measurable set \(A\),
\[
 \|1_Ah\|_2=\|B1_A\|_2\leq\|B\|\mu(A)^{1/2}.
\]
If \(|h|>\|B\|+\epsilon\) on a set of positive measure, this inequality on that set is impossible. Thus \(h\in L^\infty\) and \(\|h\|_\infty\leq\|B\|\). Bounded truncations are dense in \(L^2\), so \(B=M_h\) on the whole Hilbert space. The multiplier algebra is therefore its own commutant; commutation equations are weak-operator closed, so it is a von Neumann algebra. This proof works on any finite measure space.

Under the pairing \(\langle f,g\rangle=\int fg\), its preadjoint is \(g(r)\mapsto g(r-t)\). This follows by Haar substitution. [L24, translations](OA-FLOW-L24.md#oa-flow.grp.translations) proves norm continuity of this action on \(L^1\), hence point-ultraweak continuity of \(\alpha\). For the multiplication representation the same pairing describes all normal functionals: a vector coefficient is \(\int f\xi\overline\eta\), and Cauchy–Schwarz puts its density in \(L^1\); every \(g\in L^1\) factors as \(g=\xi\overline\eta\) with \(\xi,\eta\in L^2\), by taking square roots of \(|g|\) and its measurable phase. Summable vector coefficients have \(L^1\) sums, by [CP4–6](OA-FLOW-CP.md#oa-flow.cp.4). Thus these statements concern the actual normal topology.

Haar substitution also gives
\[
 \widehat{\alpha_t f}(k)=e^{2\pi ikt}\widehat f(k).
 \tag{C2}
\]
If \(\alpha_t f=e^{2\pi int}f\) for every \(t\), then
\((e^{2\pi ikt}-e^{2\pi int})\widehat f(k)=0\). When \(k\ne n\), take \(t=1/(2(k-n))\) modulo one to make the two phases unequal. Hence all coefficients except the \(n\)-th vanish. Since \(f\in L^2(\mathbb T)\), completeness of the orthonormal family \(u^k\), proved in [CC0](OA-FLOW-CC.md#oa-flow.cc.0), gives
\[
 M_n:=\{f:\alpha_t f=e^{2\pi int}f\text{ for every }t\}
      =\mathbb C u^n.
 \tag{C3}
\]
The reverse inclusion is immediate from (C1). In particular the fixed algebra is the scalars.

<a id="oa-flow.circle.projections"></a>

## Normal projections and bounded Fejér approximation

By [AT5](OA-FLOW-AT.md#oa-flow.at.5), the scalar integral
\[
 P_n f=\int_{\mathbb T}e^{-2\pi int}\alpha_t(f)\,dt
 \tag{C4}
\]
defines a normal contraction, where the integral is evaluated against normal functionals. Changing \(t\) to \(t+h\) shows \(\alpha_h(P_nf)=e^{2\pi inh}P_nf\), and (C4) is the identity on \(M_n\). Applying the normal coefficient functional \(\widehat{\phantom f}(n)\) and using (C2) proves
\[
 P_nf=\widehat f(n)u^n.
 \tag{C5}
\]
Thus \(P_n\) is a normal rank-one projection and \(P_nP_k=0\) for \(n\ne k\). No pointwise identity simultaneously outside one exceptional null set for every translation is needed.

For \(N\geq1\), use the kernels already proved in CC0:
\[
 F_N(t)=\frac1N\left|\sum_{j=0}^{N-1}e^{2\pi ijt}\right|^2
       =\sum_{|j|<N}\left(1-\frac{|j|}{N}\right)e^{2\pi ijt}.
 \tag{C6}
\]
They are nonnegative, have integral one, and their integrals outside every neighborhood of zero tend to zero. Consequently
\[
 Q_Nf=\int_{\mathbb T}F_N(t)\alpha_t(f)\,dt
 =\sum_{|n|<N}\left(1-\frac{|n|}{N}\right)\widehat f(n)u^n,
 \qquad \|Q_Nf\|_\infty\leq\|f\|_\infty.
 \tag{C7}
\]
The equality follows from the finite expansion and the symmetry of the coefficients.

These approximants converge to \(f\) in \(L^1\) and \(L^2\), and ultraweakly in \(L^\infty\). For \(p=1,2\), translation is continuous in \(L^p\), by L24 and CC0. For a class \(h\in L^p\), bounded-map compatibility and the integral norm inequality give
\[
 \|Q_Nh-h\|_p\leq
 \int F_N(t)\|\alpha_t h-h\|_p\,dt.
 \tag{C8}
\]
Near zero the integrand's norm factor is arbitrarily small; elsewhere it is at most \(2\|h\|_p\), and the kernel mass tends to zero. The same proof with the continuous scalar function \(t\mapsto\omega(\alpha_t f)\) gives ultraweak convergence for \(f\in M\). For a continuous \(f\), uniform continuity makes the estimate valid in the supremum norm as well. Thus (C7) supplies both uniqueness of Fourier coefficients and a bounded family of trigonometric polynomial approximations.

<a id="oa-flow.circle.multipliers"></a>

## One unitary generates the multiplication algebra

Let \(M_z\) be multiplication by \(z(s)=e^{2\pi is}\). Its integer powers are the trigonometric monomial multipliers. For any \(f\in L^\infty(\mathbb T)\), (C7) gives polynomials \(Q_Nf\) with the common supremum bound \(\|f\|_\infty\), converging to \(f\) in \(L^2\). For bounded \(g\),
\[
 \|(Q_Nf-f)g\|_2\leq\|g\|_\infty\|Q_Nf-f\|_2\longrightarrow0.
 \tag{C8a}
\]
For arbitrary \(g\in L^2\), approximate by bounded truncations and use the common operator bound \(2\|f\|_\infty\) for the difference. Thus \(M_{Q_Nf}\to M_f\) strongly. Every such multiplier belongs to \(W^*(M_z)\), since bicommutants are strongly closed: a strong limit commutes with each fixed operator commuting with the approximants. Conversely the multiplier algebra is a von Neumann algebra containing \(M_z\), by the commutant proof above. We conclude
\[
 W^*(M_z)=\{M_f:f\in L^\infty(\mathbb T)\}.
 \tag{C8b}
\]
The coefficient calculation after (C1) also proves that this identification and its inverse preserve the ultraweak topology.

<a id="oa-flow.circle.sign"></a>

## Reversing the direction of translation

If instead \(\beta_t f(s)=f(s-t)\), then \(\beta_t=\alpha_{-t}\). Its degree-\(n\) fiber is therefore \(\mathbb C u^{-n}\), with projection
\[
 P_n^\beta f=\widehat f(-n)u^{-n}.
 \tag{C9}
\]
This follows by substituting \(-t\) in (C4), or directly from (C2). It explains why the sign of a fiber must be tied to the stated action and pairing.

These computations give the translation model in Takesaki, *Theory of Operator Algebras II*, Exercise XI.1.2, p.330.
