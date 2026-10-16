# Modulation, reciprocal tails and the full Fourier generator

The real-line Fourier algebra gives a concrete norm-continuous group and reciprocal multipliers for unbounded generators. We construct reciprocal tails by an absolutely convergent series of compact frequency pieces, then identify the full generator domain by an integral identity.

*Original expression: CC0-1.0 to the extent of rights held.*

<a id="oa-flow.recip.modulation"></a>

## Modulation and filtered orbits

Use the positive transform of [RF1](OA-FLOW-RF.md#rf-1) and [AF0](OA-FLOW-AF.md#af-0):
\[
 f(q)=\widehat a(q)=\int_{\mathbb R}a(t)e^{itq}\,dt,\qquad
 A(\mathbb R)=\widehat{L^1(\mathbb R)},\qquad \|f\|_A=\|a\|_1.
 \tag{R1}
\]
Fourier uniqueness makes this norm unambiguous. Completeness and the algebra bound follow from [SC7](OA-FLOW-SC.md#sc-07) and the convolution proof in RF1. In particular \(\|f\|_\infty\leq\|f\|_A\), so point evaluations are bounded and separate elements.

Define \((\rho_s f)(q)=e^{isq}f(q)\). Substitution gives
\[
 \rho_s\widehat a=\widehat{L_sa},\qquad (L_sa)(t)=a(t-s).
 \tag{R2}
\]
Translation preserves the \(L^1\) norm and is norm continuous by [L24](OA-FLOW-L24.md#oa-flow.grp.translations). Thus \(\rho\) is a strongly continuous group of surjective isometries of the Banach space \(A(\mathbb R)\).

For an action \(\alpha\) in either [BS0 setting](OA-FLOW-BS.md#bs-0), write \(\alpha_f=\int a(t)\alpha_t\,dt\), with the complete norm or specified-dual integral of [BS1](OA-FLOW-BS.md#bs-1). The substitution \(u=s+t\) proves
\[
 \alpha_s\alpha_f=\alpha_{\rho_s f},\qquad
 \|\alpha_s\alpha_f-\alpha_f\|\leq C_\alpha\|\rho_s f-f\|_A\longrightarrow0.
 \tag{R3}
\]
Every filtered vector therefore has a norm-continuous orbit, including in the dual setting. The negative Fourier convention gives the same operators after reflecting the kernel.

<a id="oa-flow.recip.tail"></a>

## Reciprocal tails from a summable annular decomposition

**Theorem.** If \(\psi\) is smooth on \(\mathbb R\) and \(\psi(q)=1/q\) for \(|q|\geq\varepsilon>0\), then \(\psi\in A(\mathbb R)\).

Choose a smooth cutoff \(\chi\), equal to one on \([-1,1]\), supported in \([-2,2]\), by RF1. Put
\[
 \eta(u)=\chi(u/2)-\chi(u),\qquad
 H(u)=\eta(u)/u,
 \tag{R4}
\]
extending \(H\) by zero near zero. Both functions are smooth and compactly supported; \(\eta\) vanishes for \(|u|\leq1\) and for \(|u|\geq4\). RF1 supplies \(H\in A(\mathbb R)\).

For \(a>0\), if \(F=\widehat k\), a change of variable gives
\[
 F(q/a)=\widehat{\,a k(a\,\cdot)\,}(q),\qquad
 \|F(\,\cdot/a)\|_A=\|F\|_A.
 \tag{R5}
\]
Frequency translation multiplies \(k\) by a unit-modulus scalar function and also preserves this norm. Fix \(R\geq\varepsilon\). The series
\[
 \sum_{j=0}^{\infty}\frac1{2^jR}H\!\left(\frac q{2^jR}\right)
 \tag{R6}
\]
converges absolutely in the Banach space \(A(\mathbb R)\), since the sum of its term norms is at most \(2\|H\|_A/R\). It also converges uniformly. For \(q\ne0\), its partial sum through \(j=N\) is
\[
 \frac{\chi(q/(2^{N+1}R))-\chi(q/R)}q.
\]
At \(q=0\) all terms are zero. Taking the limit shows that (R6) is exactly \((1-\chi(q/R))/q\), with its smooth zero value near zero. Hence
\[
 \psi(q)=\psi(q)\chi(q/R)
       +\sum_{j=0}^{\infty}\frac1{2^jR}H\!\left(\frac q{2^jR}\right)\in A(\mathbb R).
 \tag{R7}
\]
The first term is smooth and compactly supported, and RF1 proves its membership. The equality holds because \(\psi(q)=1/q\) wherever \(1-\chi(q/R)\ne0\). This proves the theorem without a weak-derivative or distributional Fourier theorem.

In particular, if \(\theta\in C_c^\infty(\mathbb R)\) equals one near \(p\), then
\[
 b_p(q)=\frac{1-\theta(q)}{i(q-p)}
 \tag{R8}
\]
extends smoothly through \(p\) by zero and belongs to \(A(\mathbb R)\): translate the preceding theorem and multiply by \(1/i\). It satisfies \(i(q-p)b_p=1-\theta\) everywhere.

**Exercise.** If a smooth \(\zeta\) vanishes near zero and equals one outside \((-\varepsilon,\varepsilon)\), show that \(\zeta(q)/q\in A(\mathbb R)\).

**Solution.** Extend the quotient by zero near zero. It is smooth and agrees with \(1/q\) outside the indicated interval, so (R7) applies. \(\square\)

<a id="oa-flow.recip.domain"></a>

## The complete modulation-generator domain

Let \(D_\rho\) be the full norm generator of \(\rho\), as constructed in [L94](OA-FLOW-L94.md#oa-flow.gen.norm). Then
\[
 D(D_\rho)=\{f\in A(\mathbb R):q\mapsto iqf(q)\in A(\mathbb R)\},
 \qquad (D_\rho f)(q)=iqf(q).
 \tag{R9}
\]
Necessity follows by applying bounded evaluation to the norm difference quotient. For sufficiency suppose \(g(q)=iqf(q)\) belongs to \(A(\mathbb R)\). The norm-continuous orbit \(u\mapsto\rho_u g\) has its oriented Banach integral by [L24](OA-FLOW-L24.md#oa-flow.grp.vectorintegration). Evaluating it at \(q\) gives the scalar identity
\[
 (\rho_t f-f)(q)=\int_0^t e^{iuq}iqf(q)\,du
              =\left(\int_0^t\rho_u g\,du\right)(q).
\]
Evaluations separate elements, so the equality holds in \(A(\mathbb R)\). Dividing by \(t\) and using norm continuity gives
\[
 \left\|t^{-1}(\rho_t f-f)-g\right\|_A
 \leq\sup_{|u|\leq|t|}\|\rho_u g-g\|_A\longrightarrow0.
 \tag{R10}
\]
This proves both domain inclusions.

Every smooth compactly supported \(f\) lies in this domain because \(qf(q)\) is also smooth and compactly supported. The reciprocal \(b_p\) in (R8) need not do so: its coordinate multiple tends to \(1/i\), whereas every element of \(A(\mathbb R)\) vanishes at infinity. Indeed [RF3](OA-FLOW-RF.md#rf-3) gives compactly supported \(e_n\) with \(e_nf\to f\) in \(A\)-norm; the supremum-norm bound then makes \(f\) a uniform limit of compactly supported continuous functions. For every \(f\in A(\mathbb R)\), however,
\[
 iqb_p(q)f(q)=(1-\theta(q))f(q)+ip\,b_p(q)f(q)\in A(\mathbb R),
 \tag{R11}
\]
so \(b_pf\in D(D_\rho)\). This product-domain statement is what the resolvent arguments require.

The corresponding mathematical source is Takesaki, *Theory of Operator Algebras II*, XI.1, equations (20)–(21) and Lemma 1.21, printed p.327 ([edition](https://doi.org/10.1007/978-3-662-10451-4)). The earlier RF1 proof supplies smooth Fourier inversion; (R4)–(R7) give the reciprocal construction used here.
