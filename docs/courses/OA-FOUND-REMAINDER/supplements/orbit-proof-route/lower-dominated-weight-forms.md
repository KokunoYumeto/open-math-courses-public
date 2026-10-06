<span id="comparing-weights-through-their-finite-energy-vectors"></span>
# Comparing weights through their finite-energy vectors

<span id="oa-mod-dw-01--conventions-and-the-exact-comparison-problem"></span>
<span id="OA-MOD-DW-01"></span>
<span id="oa-mod-dw-01"></span>
## OA-MOD-DW-01 — Conventions and the exact comparison problem

Inner products are linear in the first variable. Fix a weight \(\varphi:M_+\to[0,\infty]\), and write

\[
\mathfrak n_\varphi=\{x:\varphi(x^*x)<\infty\},\qquad
\mathfrak m_\varphi=\operatorname{span}\{y^*x:x,y\in\mathfrak n_\varphi\}.
\]

The construction in OA-MOD-WG supplies a positive linear extension of \(\varphi\) to \(\mathfrak m_\varphi\), a Hilbert space \(H_\varphi\), a dense-range map \(\Lambda_\varphi\), and a unital representation \(\pi_\varphi\) with

\[
\langle\Lambda_\varphi(x),\Lambda_\varphi(y)\rangle=\varphi(y^*x),\qquad
\pi_\varphi(a)\Lambda_\varphi(x)=\Lambda_\varphi(ax).
\]

In particular \(\mathfrak m_\varphi^+=\mathfrak m_\varphi\cap M_+=\{a\in M_+:\varphi(a)<\infty\}\), and every element of \(\mathfrak m_\varphi\) is a complex linear combination of this cone. These are algebraic domains, not norm closures.

Let \(\mathcal D_\varphi\) be the cone of positive linear forms \(\ell:\mathfrak m_\varphi\to\mathbb C\) such that, for some finite \(c\geq0\),

\[
0\leq\ell(a)\leq c\varphi(a)\quad(a\in\mathfrak m_\varphi^+).
\]

Positivity refers to the inherited cone above. It does not assert that \(\ell\) is bounded for the operator norm, or that it has already been extended to a normal weight on all of \(M_+\). The order on these forms is positivity of their difference on this cone.

<span id="oa-mod-dw-02--a-factorization-inside-the-algebra"></span>
<span id="OA-MOD-DW-02"></span>
<span id="oa-mod-dw-02"></span>
## OA-MOD-DW-02 — A factorization inside the algebra

**Lemma.** If \(x,y\in M\) and \(y^*y\leq x^*x\), there is a unique contraction \(v\in M\) which vanishes on \(\overline{xH}^{\perp}\) and satisfies \(y=vx\), in any faithful concrete realization \(M\subseteq B(H)\).

**Proof.** On \(xH\) define \(x\xi\mapsto y\xi\). The inequality says both that this is well defined and that its norm is at most one. Extend it continuously to \(\overline{xH}\), and set it equal to zero on the orthogonal complement. This proves existence and uniqueness in \(B(H)\). Every unitary \(u\in M'\) preserves \(\overline{xH}\); because \(x,y\) commute with \(u\), both \(v\) and \(uvu^*\) have the prescribed properties. Thus \(v\) commutes with every unitary of \(M'\). Every element of a unital C*-algebra is a linear combination of unitaries: a self-adjoint contraction \(b\) is the real part of \(b+i(1-b^2)^{1/2}\). Consequently \(v\in M''=M\). This uses bounded continuous functional calculus and the bicommutant theorem, recorded foundation contracts. \(\square\)

For \(a,b\geq0\) put \(d=a+b\) and \(p=s(d)\), the projection onto \(\overline{dH}\). Applying the lemma to \(a^{1/2},d^{1/2}\) and \(b^{1/2},d^{1/2}\) gives contractions \(v,w\in M\) with

\[
a^{1/2}=vd^{1/2},\quad b^{1/2}=wd^{1/2},\quad v=vp,\quad w=wp,\quad v^*v+w^*w=p.
\]

To verify the last identity, its quadratic form agrees with that of \(p\) on \(d^{1/2}H\), by \(a+b=d\); continuity extends the equality to \(pH\). Both sides vanish on \((1-p)H\). This argument needs neither an inverse of \(d\) nor a positive lower bound for it.

<span id="oa-mod-dw-03--the-commutant-correspondence"></span>
<span id="OA-MOD-DW-03"></span>
<span id="oa-mod-dw-03"></span>
## OA-MOD-DW-03 — The commutant correspondence

**Theorem.** There is an additive, positively homogeneous order isomorphism

\[
\pi_\varphi(M)'_+\longleftrightarrow\mathcal D_\varphi,\qquad T\longmapsto\ell_T,
\]

uniquely characterized by

\[
\ell_T(y^*x)=\langle T\Lambda_\varphi(x),\Lambda_\varphi(y)\rangle
\quad(x,y\in\mathfrak n_\varphi).
\]

Moreover \(T\leq cI\) if and only if \(\ell_T\leq c\varphi\) on \(\mathfrak m_\varphi^+\). Thus the least admissible comparison constant is \(\|T\|\). The assertion includes the zero Hilbert space, where both cones consist only of zero.

**Proof, from forms to operators.** For \(\ell\in\mathcal D_\varphi\), positivity applied to \((x+zy)^*(x+zy)\), for every \(z\in\mathbb C\), gives

\[
|\ell(y^*x)|^2\leq\ell(x^*x)\ell(y^*y)
\leq c^2\|\Lambda_\varphi(x)\|^2\|\Lambda_\varphi(y)\|^2.
\]

For completeness, when \(\ell(y^*y)>0\), minimize this quadratic polynomial in \(z\); when that diagonal term is zero, varying the magnitude and phase of \(z\) forces the cross term to vanish. The inequality shows that the expression is independent of null representatives and defines a bounded sesquilinear form on \(\Lambda_\varphi(\mathfrak n_\varphi)\). It extends uniquely to \(H_\varphi\). The Hilbert-space representation theorem for bounded sesquilinear forms gives a unique positive operator \(T\) with \(0\leq T\leq cI\).

For \(a\in M\) and \(x,y\in\mathfrak n_\varphi\), associativity gives

\[
\begin{aligned}
\langle T\pi_\varphi(a)\Lambda_\varphi(x),\Lambda_\varphi(y)\rangle
&=\ell(y^*ax)\\
&=\langle T\Lambda_\varphi(x),\pi_\varphi(a^*)\Lambda_\varphi(y)\rangle\\
&=\langle\pi_\varphi(a)T\Lambda_\varphi(x),\Lambda_\varphi(y)\rangle.
\end{aligned}
\]

The test vectors form a dense subspace, so \(T\pi_\varphi(a)=\pi_\varphi(a)T\). This proves membership in the commutant without any appeal to a modular group.

**Proof, from operators to forms.** Fix \(T\in\pi_\varphi(M)'_+\). For finite-weight positive \(a\), define

\[
f_T(a)=\langle T\Lambda_\varphi(a^{1/2}),\Lambda_\varphi(a^{1/2})\rangle.
\]

We must prove additivity; merely writing a formula on products would not prove independence of their decompositions. Let \(a,b\in\mathfrak m_\varphi^+\), and use \(d,p,v,w\) from OA-MOD-DW-02. Here \(d^{1/2}\in\mathfrak n_\varphi\). Put \(\zeta=\Lambda_\varphi(d^{1/2})\). Then \(\pi_\varphi(p)\zeta=\zeta\) and

\[
\begin{aligned}
f_T(a)+f_T(b)
&=\langle T\pi_\varphi(v)\zeta,\pi_\varphi(v)\zeta\rangle
 +\langle T\pi_\varphi(w)\zeta,\pi_\varphi(w)\zeta\rangle\\
&=\langle T\zeta,\pi_\varphi(v^*v+w^*w)\zeta\rangle
=f_T(d).
\end{aligned}
\]

Homogeneity follows from the square root of a scalar. Thus \(f_T\) extends to a real linear form on \(\mathfrak m_{\varphi,\mathrm{sa}}\): assign \(f_T(a)-f_T(b)\) to \(a-b\). If \(a-b=a'-b'\), the equality \(a+b'=a'+b\) and additivity prove independence. Complexification gives a positive linear form \(\ell_T\) on \(\mathfrak m_\varphi\). Also

\[
0\leq f_T(a)\leq\|T\|\varphi(a).
\]

If \(x\in\mathfrak n_\varphi\), take its polar decomposition \(x=u|x|\) in \(M\). Then \(\Lambda_\varphi(x)=\pi_\varphi(u)\Lambda_\varphi(|x|)\), and \(u^*u\) fixes \(|x|\). Commutation with \(T\) yields

\[
\langle T\Lambda_\varphi(x),\Lambda_\varphi(x)\rangle=f_T(x^*x).
\]

Polarization now proves the formula for \(y^*x\). Uniqueness holds because these products span \(\mathfrak m_\varphi\), and their GNS vectors are dense. The two constructions are inverse. Addition and scalar multiplication follow from the defining pairings. Finally positivity of \(\ell_{T_2}-\ell_{T_1}\) is equivalent to nonnegativity of the quadratic form of \(T_2-T_1\) on a dense subspace, hence on all of \(H_\varphi\). Apply this to \(cI-T\) to obtain the bound and the optimal constant. \(\square\)

<span id="oa-mod-dw-04--comparing-two-weights-and-the-precise-target-space"></span>
<span id="OA-MOD-DW-04"></span>
<span id="oa-mod-dw-04"></span>
## OA-MOD-DW-04 — Comparing two weights and the precise target space

**Theorem.** Let \(\psi\) be another weight on \(M\), with \(\psi\leq c\varphi\) on \(M_+\) for a finite \(c>0\). There is a unique bounded map

\[
C_{\psi\mid\varphi}:H_\varphi\longrightarrow H_\psi,
\qquad C_{\psi\mid\varphi}\Lambda_\varphi(x)=\Lambda_\psi(x)
\quad(x\in\mathfrak n_\varphi),
\]

with norm at most \(\sqrt c\). It intertwines the representations, and

\[
T_{\psi\mid\varphi}=C_{\psi\mid\varphi}^*C_{\psi\mid\varphi}\in\pi_\varphi(M)'_+,
\quad
\psi(y^*x)=\langle T_{\psi\mid\varphi}\Lambda_\varphi(x),\Lambda_\varphi(y)\rangle.
\]

The range closure is exactly
\(K=\overline{\Lambda_\psi(\mathfrak n_\varphi)}\subseteq H_\psi\).
If \(C=UT^{1/2}\) is its polar decomposition, then \(U\) is a unitary from \(s(T)H_\varphi\) onto \(K\), and is zero on \(\ker T\). These two subspaces reduce the corresponding representations, and \(U\) intertwines their restrictions.

**Proof.** Domination gives \(\mathfrak n_\varphi\subseteq\mathfrak n_\psi\) and
\(\|\Lambda_\psi(x)\|^2\leq c\|\Lambda_\varphi(x)\|^2\). Consequently the displayed assignment is well defined even for nonfaithful weights and extends from a dense domain. Its range closure is \(K\) by construction. On the dense GNS domain,

\[
C\pi_\varphi(a)\Lambda_\varphi(x)
=\Lambda_\psi(ax)=\pi_\psi(a)C\Lambda_\varphi(x).
\]

Boundedness extends this identity to all vectors. Taking adjoints and using the identity for \(a^*\) shows that \(C^*\) intertwines in the reverse direction, so \(C^*C\) commutes with \(\pi_\varphi(M)\). The pairing formula is immediate. It agrees with OA-MOD-DW-03 applied to \(\psi|_{\mathfrak m_\varphi}\).

The closed subspaces \(\ker C\) and \(K\) are invariant under the representations and their adjoints. Therefore their orthogonal projections commute with these representations. Since \(T^{1/2}\) also commutes with \(\pi_\varphi(M)\), the equality
\(U\pi_\varphi(a)T^{1/2}\xi=\pi_\psi(a)UT^{1/2}\xi\)
holds first on \(\operatorname{ran}T^{1/2}\), and then by continuity on its closure \(s(T)H_\varphi\). Both sides vanish on its orthogonal complement. The initial and final subspaces of a polar decomposition give the claimed unitary. \(\square\)

Do not replace \(K\) by \(H_\psi\) in this level of generality. If \(\varphi\) is zero at zero and infinite at every nonzero positive element, then \(\mathfrak n_\varphi=\{0\}\), while every weight \(\psi\) satisfies \(\psi\leq\varphi\). The comparison map is zero even when \(H_\psi\neq0\). This also shows why restriction to a finite domain need not determine the whole weight.

