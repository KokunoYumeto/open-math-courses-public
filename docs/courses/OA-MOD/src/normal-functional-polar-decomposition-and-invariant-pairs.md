# Normal-functional polar decomposition and invariant pairs

**Self-checked by the writing AI.**

A normal complex functional has a positive absolute value and a partial isometry in the algebra. For a functional with faithful positive real part, that partial isometry is unitary. Equality of the absolute values of the functional and its adjoint then says that this unitary commutes with the positive functional. This turns a polar-decomposition test into a modular-invariance test.

The owning source target is Takesaki, *Theory of Operator Algebras II*, Exercise VIII.3(3). For the exact prerequisite in Takesaki I, Theorem III.4.2(i) and the terminology of Definition 4.3 we use the existing programme polar-decomposition proof identified below. The Jordan-decomposition part III.4.2(ii) has a separate scope and receives no proof credit here.

Inputs are CP-01/06's norming-functional Hahn–Banach contract and isometric predual duality, CP-07's positive-functional Cauchy–Schwarz and normality, CP-12/WS's support and faithful corner, BK-07's bounded-operator polar decomposition, NW-11/CP-12's bounded normal-weight-to-predual identification, CZ-05/07/08/09/11's centralizers and density rules, PT-06's supported invariant-weight density theorem, and SK's spectral calculus. The Hahn–Banach input retains its own transitive provider status. Neither a trace on the algebra nor boundedness of the relative density is assumed.

Our convention is

\[
 (v\omega)(x)=\omega(xv),\qquad
 \eta^*(x)=\overline{\eta(x^*)}.
 \tag{NF.1}
\]

All functionals in this lesson are complex-linear. Positive functionals are evaluated on all of \(M\), unlike an unbounded weight's finite linear extension.

## Two solved norm-attainment checks with support control

**Positivity lemma.** If a bounded complex-linear \(f\) on a unital C*-algebra satisfies \(f(h)=\|f\|\) for a positive contraction \(h\), then \(f\) is positive.

**Proof.** Put \(c=\|f\|\). Functional calculus gives \(\|h+z(1-h)\|\leq1\) for \(|z|\leq1\): every scalar spectral value is a convex combination of 1 and \(z\). Consequently
\(|c+zf(1-h)|\leq c\). Choosing the phase of \(z\) shows \(f(1-h)=0\), so \(f(1)=c\). If \(c=0\), the claim is immediate. For self-adjoint \(x\), the unitary \(e^{itx}\) satisfies
\(f(e^{itx})=c+itf(x)+O(t^2)\). The inequality
\(\operatorname{Re}f(e^{itx})\leq c\), for both signs of \(t\), forces \(\operatorname{Im}f(x)=0\). If \(0\leq x\leq1\), then \(f(1-x)\leq c\), so \(f(x)\geq0\). Scaling proves positivity on every positive element. \(\square\)

**Projection lemma.** Let \(\eta\) attain its norm at a contraction \(a\), with \(\eta(a)=\|\eta\|\). If \(a=ae\) for a projection \(e\), then \(\eta(x(1-e))=0\) for every \(x\in M\).

**Proof.** The cross terms vanish in the product with its adjoint, giving

\[
 \|a+zx(1-e)\|^2
 =\|aa^*+|z|^2x(1-e)x^*\|
 \leq1+|z|^2\|x\|^2.
 \tag{NF.2}
\]

Let \(z\) have a phase making \(z\eta(x(1-e))\) nonnegative real. With \(r=|z|>0\),
\(\|\eta\|+r|\eta(x(1-e))|\leq\|\eta\|\sqrt{1+r^2\|x\|^2}\).
Divide the increment by \(r\) and let \(r\downarrow0\). The right increment tends to zero, proving the claim. The zero functional also satisfies it. \(\square\)

These solved checks explain positivity and support at a norm-attaining contraction. They are learner exercises; they do not replace or create another owner of the programme polar theorem used next.

## The programme polar decomposition and its support convention

Read [The polar decomposition of a normal functional](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/polar-decomposition-of-functionals-and-weak-compactness-in-preduals.html#oa-fnd-pd-03), **Theorem 2.2, parts (1), (3) and (4), and Definition 2.3**, in *Foundations of von Neumann algebras*. That existing programme lesson contains the full proof for arbitrary complex normal functionals on any von Neumann algebra. It was written by Claude Opus 5.5 (Anthropic), September 2026, and released under CC0. We use its exact theorem here rather than claim a second owner of its proof.

With \(\eta\) in place of the provider's \(\varphi\), and the same module
convention (NF.1), it gives the unique pair \((v,\omega)\) with
\(\omega\in M_*^+\) and \(v\in M\) a partial isometry satisfying

\[
 \eta(x)=\omega(xv),\qquad v^*v=s(\omega),
 \qquad\|\eta\|=\omega(1)=\|\omega\|.
 \tag{NF.3}
\]

Definition 2.3 names \(\omega=|\eta|\). If \(p=v^*v\) and \(q=vv^*\),
part (3) and the provider's Lemma 1.4 say that \(p\) is the least projection
with \(\eta(px)=\eta(x)\) for all \(x\), and \(q\) is the least with
\(\eta(xq)=\eta(x)\). They are respectively the right and left supports
in this module convention; the side in the evaluation formula must not be
used to reverse their names.

The normalization matters even for a nonfaithful functional. For the zero
functional, the norm clause forces \(\omega=0\), and
\(v^*v=s(\omega)=0\) forces \(v=0\). No faithful state, trace,
separability or bounded density is part of the imported theorem.

## The adjoint modulus and its centralizer test

Part (4) of the same programme theorem supplies the adjoint pair.
With \(\omega_v(x)=\omega(v^*xv)\), it is \((v^*,\omega_v)\), and its
positive functional has support \(q=vv^*\). Thus the imported identity is

\[
 \eta^*(x)=\omega(v^*x)=\omega_v(xv^*),
 \qquad |\eta^*|(x)=\omega(v^*xv).
 \tag{NF.7}
\]

The initial projection for \(v^*\) is \(q\), exactly as required by the
provider's normalization. We now apply this formula to the centralizer.

If both support projections of \(\eta\) are 1, write \(v=u\), a unitary, and \(\omega=|\eta|\), faithful. Then

\[
 |\eta|=|\eta^*|
 \quad\Longleftrightarrow\quad
 \omega\circ\operatorname{Ad}(u^*)=\omega
 \quad\Longleftrightarrow\quad u\in M_\omega.
 \tag{NF.8}
\]

For the second equivalence, replace \(x\) by \(xu^*\) in the conjugation identity to get \(\omega(u^*x)=\omega(xu^*)\) for all \(x\). CZ-05's cyclicity criterion puts \(u^*\), and hence \(u\), in the centralizer. Conversely, cyclicity gives invariance under conjugation by the unitary. Every finite ideal here is all of \(M\), because \(\omega\) is a bounded positive functional. This is an exact centralizer test, rather than a conclusion about two automorphism groups having equal formulas.

## Invariant positive pairs have equal conjugate moduli

**Theorem, Exercise VIII.3(3).** Let \(\varphi,\psi\in M_*^+\), with \(\varphi\) faithful. Then

\[
 \psi\circ\sigma_t^\varphi=\psi\quad(t\in\mathbb R)
 \quad\Longleftrightarrow\quad
 |\varphi+i\psi|=|\varphi-i\psi|.
 \tag{NF.9}
\]

No faithfulness of \(\psi\) or boundedness of its relative affiliated density is required.

**From equal moduli to invariance.** Put \(\eta=\varphi+i\psi\), so \(\eta^*=\varphi-i\psi\). If \(p,q\) are the supports from NF-02, then
\(\eta(1-p)=\eta(1-q)=0\). Taking real parts gives
\(\varphi(1-p)=\varphi(1-q)=0\). Faithfulness forces \(p=q=1\). Thus \(\eta(x)=\omega(xu)\), with \(\omega\) faithful and \(u\) unitary. NF-03 puts \(u\) in \(M_\omega\). Define the commuting self-adjoint centralizer elements

\[
 h=\tfrac12(u+u^*),\qquad k=\tfrac1{2i}(u-u^*).
 \tag{NF.10}
\]

The functional identities are \(\varphi(x)=\omega(xh)\), \(\psi(x)=\omega(xk)\). Positivity of \(\varphi\) forces \(h\geq0\): a nonzero spectral projection \(e=1_{(-\infty,-\delta]}(h)\), \(\delta>0\), would give
\(\varphi(e)=\omega(eh)\leq-\delta\omega(e)<0\). The same argument gives \(k\geq0\). Bounded centralizer cyclicity now identifies

\[
 \varphi=\omega_h,\qquad\psi=\omega_k.
 \tag{NF.11}
\]

These are identities on all of \(M\). Faithfulness of \(\varphi\) makes \(h\) injective by CZ-08's exact support rule; its inverse need not be bounded. CZ-11 gives
\(\sigma_t^\varphi=\operatorname{Ad}(h^{it})\sigma_t^\omega\).
Both factors preserve \(\omega\), and \(k\) is fixed by the first because it commutes with \(h\), and by the second because it is in \(M_\omega\). Therefore, for every \(x\in M\),
\(\psi(\sigma_t^\varphi(x))=\omega(k\sigma_t^\varphi(x))=\omega(\sigma_t^\varphi(kx))=\psi(x)\).

**From invariance to equal moduli.** PT-06 gives \(\psi=\varphi_\ell\) with \(\ell\geq0\) affiliated with \(M_\varphi\), possibly singular and unbounded. Use spectral calculus to set

\[
 g=(1+\ell^2)^{1/2},\qquad
 u=(1+i\ell)g^{-1},\qquad \omega=\varphi_g.
 \tag{NF.12}
\]

The product defining \(u\) denotes the bounded spectral function
\((1+i\lambda)/\sqrt{1+\lambda^2}\). Its modulus is 1 for every finite \(\lambda\geq0\), so \(u\) is unitary in \(M_\varphi\). The operator \(g\geq1\) is injective with its full spectral domain, and CZ-08 constructs faithful normal semifinite \(\omega\).

We must show that \(\omega\) is a bounded functional and identify the complex products. Put \(p_n=1_{[0,n]}(\ell)\). These projections increase strongly to 1 and are fixed by \(\sigma^\varphi\). They are also in \(M_\omega\): \(g\) is a strictly increasing spectral function of \(\ell\), so they are its spectral projections, and CZ-09 applies. On their corners the density operators are bounded, and scalar spectral order \(g\leq1+\ell\) gives

\[
 \omega(p_n)\leq\varphi(p_n)+\psi(p_n)
 \leq\varphi(1)+\psi(1).
 \tag{NF.13}
\]

CZ-07/08 identify each restriction with its bounded density. Normality and \(p_n\uparrow1\) give \(\omega(1)<\infty\). WG's finite-weight extension gives a bounded positive functional; NW-11 and CP-12 identify it as ultraweakly continuous. Thus \(\omega\in M_*^+\), with \(\|\omega\|\leq\varphi(1)+\psi(1)\).

For \(y=p_nxp_n\), bounded centralizer cyclicity in this corner gives

\[
 \omega(yu)=\varphi(y(1+i\ell))
             =\varphi(y)+i\psi(y).
 \tag{NF.14}
\]

Here \(\ell p_n\) and \(gp_n\) are bounded elements; \(\varphi\) on the corner is a bounded functional. Thus every expression is a defined finite linear value. The uniformly bounded net \(p_nxp_n\) tends sigma-strongly* to \(x\). Normality of the three bounded functionals and fixed multiplication by \(u\) pass (NF.14) to all \(x\):
\(\eta(x)=\omega(xu)\).
The unitary \(u\) also lies in \(M_\omega\): it commutes with \(g\), and CZ-11 gives \(\sigma_t^\omega(u)=u\). Hence
\(\eta^*(x)=\omega(u^*x)=\omega(xu^*)\).
Both \((u,\omega)\) and \((u^*,\omega)\) are normalized polar pairs with support 1. NF-02 proves \(|\eta|=\omega=|\eta^*|\), as required. On the zero algebra all the assertions are trivial. \(\square\)

## Three examples and solved checks

**An unbounded relative density between bounded functionals.** On \(\ell^\infty(\mathbb N)\), with indices beginning at 1, let
\(\varphi(x)=\sum_{n\geq1}2^{-n}x_n\) and
\(\psi(x)=\sum_{n\geq1}n2^{-n}x_n\).
These are bounded normal positive functionals, with masses 1 and 2; \(\varphi\) is faithful. The elementary geometric series and its derivative give the masses. Their modular groups are trivial, and \(\ell_n=n\) is the unbounded affiliated relative density. The exact modulus is

\[
 |\varphi+i\psi|(x)=|\varphi-i\psi|(x)
       =\sum_{n\geq1}2^{-n}\sqrt{1+n^2}\,x_n,
 \qquad u_n=\frac{1+in}{\sqrt{1+n^2}}.
 \tag{NF.15}
\]

Its mass is at most 3, since \(\sqrt{1+n^2}\leq1+n\). The real part of \(u\) is positive and injective, yet has no uniform positive lower bound. Thus imposing bounded \(\ell\), or bounded inverse of that real part, would exclude an actual case of the source theorem.

**A noncommuting matrix test.** On \(M_2(\mathbb C)\), use
\(\varphi(x)=\operatorname{Tr}(dx)\), \(\psi(x)=\operatorname{Tr}(ex)\), where
\(d=\operatorname{diag}(1,4)\) and \(e=\left[\begin{smallmatrix}1&1\\1&2\end{smallmatrix}\right]\).
Both are faithful positive functionals. For \(A=d+ie\), the two modulus densities are \((A^*A)^{1/2}\) and \((AA^*)^{1/2}\), by operator polar decomposition and finite trace cyclicity. Their squares are

\[
 A^*A=\begin{bmatrix}3&3-3i\\3+3i&21\end{bmatrix},\qquad
 AA^*=\begin{bmatrix}3&3+3i\\3-3i&21\end{bmatrix}.
 \tag{NF.16}
\]

They differ, so uniqueness of positive square roots implies unequal modulus functionals. Independently, \(\sigma_t^\varphi(e)=d^{it}ed^{-it}\) has 12-entry \(4^{-it}\). At \(t=\pi/\log4\) it is \(-1\), rather than 1. Thus \(\psi\) is not invariant, exactly as (NF.9) predicts. The conjugate signs and the order of the two operator products both matter.

**Problem: the zero numerator and the missing support.** What happens for \(\psi=0\)? Why cannot one omit the initial support requirement in (NF.3)?

**Solution.** In NF-04, \(\ell=0\), \(g=1\), \(u=1\), \(\omega=\varphi\), so both moduli are \(\varphi\). For a nonfaithful \(\omega\), the identity \(\eta(x)=\omega(xv)\) cannot detect an arbitrary extra partial isometry on the complementary support. On \(M_2\), take \(\omega(x)=x_{11}\). Both \(v=E_{11}\) and \(v=1\) give \(\eta=\omega\), but only \(E_{11}\) has initial projection \(s(\omega)=E_{11}\). The normalization therefore makes the polar factor unique; NF-04's faithful real part removes that complementary support entirely.

## Source, prerequisite and illustration scope

NF-02 imports the exact existing complex normal-functional polar theorem, with both minimal supports, uniqueness and norm normalization, from the programme's Theorem 2.2 and Definition 2.3. NF-01 contains solved norm-attainment checks. NF-03 applies the same provider's transported adjoint modulus to the centralizer; NF-04 supplies both directions of the full arbitrary-algebra source exercise. Its possibly zero numerator and unbounded relative density remain visible.

The original reproducible figure retained with this tranche shows the unitary spectral phase in (NF.12), the discrete integrable modulus in (NF.15), and the conjugate off-diagonal signs in (NF.16). Finite samples and limiting endpoints are identified; captions carry exact proof locators and human-source citations. It has author mathematical and visual review.

Exercises VIII.3(4)–(5) and (9) are not solved in this lesson. The original arguments here rely on their named prerequisites, which are not proved in this lesson.
