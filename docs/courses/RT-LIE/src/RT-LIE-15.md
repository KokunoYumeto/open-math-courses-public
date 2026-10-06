# The centre of the enveloping algebra and Harish-Chandra's theorem

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

A central operator has a scalar value on each highest-weight module. Those values are polynomial functions of the highest weight, but their symmetry is centred at \(-\rho\). We shall identify the entire centre by proving the polynomial restriction theorem needed for surjectivity, then comparing leading terms in the PBW filtration.

Throughout, \(\mathfrak g\) is a finite-dimensional complex semisimple Lie algebra, with
\[
\mathfrak g=\mathfrak n^-\oplus\mathfrak h\oplus\mathfrak n^+,
\qquad \rho=\frac12\sum_{\alpha\in\Phi^+}\alpha.
\]
Write \(U=U(\mathfrak g)\), \(Z=Z(U)\), and \(W\) for the Weyl group. The root and reflection constructions come from [The root space decomposition of a semisimple Lie algebra](RT-LIE-07.md) and [Root systems and their Weyl groups](RT-LIE-08.md). We use triangular PBW and equivariant symmetrization from [The universal enveloping algebra and the Poincaré–Birkhoff–Witt theorem](RT-LIE-13.md), Propositions 4.2 and 5.1. The Verma modules \(M(\lambda)\), their quotients \(L(\lambda)\), nonzero simple-root singular vectors, and the finite-dimensional modules \(L(\lambda)\) for every dominant integral \(\lambda\) were proved in [Weights, Verma modules and the theorem of the highest weight](RT-LIE-14.md).

Our two polynomial algebras have different domains: \(S(\mathfrak h)\) consists of polynomial functions on \(\mathfrak h^*\), whereas \(S(\mathfrak h^*)\) consists of polynomial functions on \(\mathfrak h\). Killing-form identifications will relate them explicitly.

## 1. Projection and central characters

The augmentations \(\epsilon_\pm:U(\mathfrak n^\pm)\to\mathbb C\) send all Lie generators to zero. In triangular PBW coordinates define
\[
\xi(a_-pa_+)=\epsilon_-(a_-)\epsilon_+(a_+)p,
\qquad p\in U(\mathfrak h)=S(\mathfrak h).
\tag{1.1}
\]
This is a linear, filtration-preserving projection. Equivalently,
\[
U=S(\mathfrak h)\oplus
\bigl(\mathfrak n^-U+U\mathfrak n^+\bigr).
\tag{1.2}
\]
Indeed, PBW words with a nonempty negative or positive block span the second summand: a nonempty block starts with a negative generator or ends with a positive generator. Conversely the negative augmentation ideal is \(\mathfrak n^-U(\mathfrak n^-)\), and the positive one is \(U(\mathfrak n^+)\mathfrak n^+\); multiplication in the triangular decomposition gives exactly those words. The remaining words are the Cartan block.

If \(v_\lambda\) is a highest vector in any nonzero highest-weight module, a word with a positive block kills it, and a word with a negative block and no positive block lowers its weight. Hence the component of \(uv_\lambda\) of weight \(\lambda\) is
\[
\xi(u)(\lambda)v_\lambda.
\tag{1.3}
\]
Here evaluating a Cartan monomial at \(\lambda\) means replacing each \(H\in\mathfrak h\) by \(\lambda(H)\).

**Proposition 1.1.** Every nonzero highest-weight module with highest weight \(\lambda\in\mathfrak h^*\) has central character
\[
\chi_\lambda:Z\longrightarrow\mathbb C,
\qquad \chi_\lambda(z)=\xi(z)(\lambda).
\tag{1.4}
\]
The restriction \(\xi:Z\to S(\mathfrak h)\) is a unital algebra homomorphism.

**Proof.** A central \(z\) commutes with \(\mathfrak h\), so \(zv_\lambda\) has weight \(\lambda\). The top space is one-dimensional because the module is a quotient of \(M(\lambda)\). Equation (1.3) gives \(zv_\lambda=\xi(z)(\lambda)v_\lambda\). Centrality then gives the same scalar on every \(uv_\lambda\), which span the module. Scalars multiply, so \(\chi_\lambda\) is a character.

For \(z,z'\in Z\), apply this calculation in \(M(\lambda)\) for every complex \(\lambda\). It gives
\[
\xi(zz')(\lambda)=\xi(z)(\lambda)\xi(z')(\lambda).
\]
A polynomial zero at every point of \(\mathbb C^r\) is zero: induct on the variables, using the fact that a nonzero one-variable polynomial has finitely many roots. Thus \(\xi(zz')=\xi(z)\xi(z')\). Linearity and \(\xi(1)=1\) finish the proof. No finite-dimensional Schur lemma is needed. \(\square\)

The projection on all of \(U\) is not multiplicative: in \(\mathfrak{sl}_2\), \(\xi(e)=\xi(f)=0\), but \(\xi(ef)=h\), since \(ef=fe+h\).

## 2. Why the symmetry is shifted

For a polynomial \(p\) on \(\mathfrak h^*\), put
\[
(\tau_{-\rho}p)(\nu)=p(\nu-\rho),\qquad
\gamma=\tau_{-\rho}\circ\xi\bigm|_Z.
\tag{2.1}
\]
Thus the convention, including its sign, is
\[
\chi_\lambda(z)=\gamma(z)(\lambda+\rho),
\qquad w\mathbin{\cdot}\lambda=w(\lambda+\rho)-\rho.
\tag{2.2}
\]

We need a small density fact. Let \(\omega_1,\ldots,\omega_r\) be the fundamental weights. A polynomial vanishing on
\[
\Lambda^+=\left\{\sum_i n_i\omega_i:n_i\in\mathbb Z_{\ge0}\right\}
\tag{2.3}
\]
is zero. In fundamental-weight coordinates this is the nonnegative integer grid. Hold all but one coordinate fixed at grid values; the polynomial in the remaining coordinate has infinitely many zeros. Its coefficients consequently vanish on the smaller grid, and induction proves the assertion. Translation of this grid is equally dense for polynomial identities. Rank zero has only constants and the same assertion.

**Proposition 2.1.** The image of \(\gamma\) is contained in \(S(\mathfrak h)^W\).

**Proof.** Fix a simple root \(\alpha_i\), its normalized triple \(e_i,f_i,h_i\), and \(\lambda\in\Lambda^+\). Put \(n_i=\lambda(h_i)\). The nonzero vector
\[
f_i^{n_i+1}v_\lambda\in M(\lambda)
\]
is singular by the preceding lesson. Its weight is
\[
\lambda-(n_i+1)\alpha_i
=s_i(\lambda+\rho)-\rho=s_i\mathbin{\cdot}\lambda,
\tag{2.4}
\]
since \(\rho(h_i)=1\). It generates a nonzero highest-weight submodule. A central \(z\) has scalar \(\chi_\lambda(z)\) on \(M(\lambda)\), and scalar \(\chi_{s_i\cdot\lambda}(z)\) on that submodule, by Proposition 1.1. These scalars are equal. We need only the nonzero singular vector and its cyclic module, not an additional assertion that the whole corresponding Verma module embeds.

Consequently
\[
\gamma(z)(\lambda+\rho)=\gamma(z)\bigl(s_i(\lambda+\rho)\bigr).
\]
Both sides are polynomials, and \(\rho+\Lambda^+\) is dense by the grid argument. They agree everywhere. Simple reflections generate \(W\), proving the proposition. \(\square\)

## 3. Polynomial restriction, with its full proof

Write \(\mathbb C[\mathfrak g]=S(\mathfrak g^*)\). A polynomial \(F\) is infinitesimally invariant when
\[
dF_X([x,X])=0\qquad(x,X\in\mathfrak g).
\tag{3.1}
\]
This is the usual adjoint invariance condition; choosing the opposite sign for the induced action on functions gives the same invariant subspace.

**Theorem 3.1 (Chevalley restriction).** Restriction to \(\mathfrak h\) is an isomorphism of graded algebras
\[
\operatorname{Res}:\mathbb C[\mathfrak g]^{\mathfrak g}
\xrightarrow{\ \sim\ }\mathbb C[\mathfrak h]^W.
\tag{3.2}
\]

**First, the image has Weyl symmetry.** A root vector \(x_\alpha\) has nilpotent adjoint action on \(\mathfrak g\), by the finite root strings. Therefore \(\exp(t\operatorname{ad}x_\alpha)\) is a polynomial in \(t\). Condition (3.1), applied at each point on its orbit, gives
\[
\frac d{dt}F\bigl(\exp(t\operatorname{ad}x_\alpha)X\bigr)=0.
\]
Thus \(F\) is unchanged by this exponential. The three root exponentials
\[
\exp(\operatorname{ad}e_i)\exp(-\operatorname{ad}f_i)
\exp(\operatorname{ad}e_i)
\tag{3.3}
\]
act on \(\mathfrak h\) as \(s_i\): this is the conjugation computation of Lemma 4.3 of the preceding lesson, applied to the adjoint representation. Hence \(\operatorname{Res}F\) is fixed by each \(s_i\), and by \(W\).

**Second, restriction is injective.** Choose \(H_0\in\mathfrak h\) with \(\alpha(H_0)\ne0\) for every root; a finite union of proper linear hyperplanes cannot fill a complex vector space. List nonzero root vectors \(x_1,\ldots,x_m\), one for each root, and form the polynomial map
\[
\Psi(t,H)=
\exp(t_1\operatorname{ad}x_1)\cdots
\exp(t_m\operatorname{ad}x_m)H.
\tag{3.4}
\]
Its source \(\mathbb C^m\times\mathfrak h\) and target \(\mathfrak g\) have equal dimension. At \((0,H_0)\), its differential sends a Cartan displacement \(K\) to \(K\), and the \(j\)-th parameter displacement to
\[
[x_j,H_0]=-\alpha_j(H_0)x_j.
\]
The root decomposition shows that this differential is invertible.

Here is the precise polynomial consequence. Suppose \(\operatorname{Res}F=0\). Exponential invariance gives \(F(\Psi(t,H))=F(H)=0\) identically. If \(F\ne0\), expand \(F(H_0+Y)\) and take its lowest nonzero homogeneous part \(F_d(Y)\). In coordinates centred at \((0,H_0)\), write \(\Psi-H_0=Aq+\) terms of degree at least two, where \(A\) is invertible. The lowest part of \(F\circ\Psi\) is \(F_d(Aq)\), which cannot vanish because invertible linear substitution is an automorphism of the polynomial ring. This contradicts \(F\circ\Psi=0\). Thus \(F=0\). This argument supplies the needed density of root conjugates directly.

**Third, enough powers span each degree.** Fix \(d\ge0\). The powers \(\lambda^d\), viewed as homogeneous polynomial functions \(H\mapsto\lambda(H)^d\), for \(\lambda\in\Lambda^+\), span \(S^d(\mathfrak h^*)\). To see this, let a linear functional \(a\) on that finite-dimensional space vanish on all of them. Then
\[
\lambda\longmapsto a(\lambda^d)
\]
is a polynomial zero on the grid (2.3), hence zero everywhere. In a coordinate expansion
\[
\left(\sum_i c_i\omega_i\right)^d
=\sum_{|b|=d}\frac{d!}{b_1!\cdots b_r!}
c_1^{b_1}\cdots c_r^{b_r}\,
\omega_1^{b_1}\cdots\omega_r^{b_r},
\]
every multinomial coefficient is nonzero. Comparing its coefficients gives \(a(\omega_1^{b_1}\cdots\omega_r^{b_r})=0\) for every monomial, so \(a=0\). A proper subspace would have a nonzero annihilating functional, proving the spanning assertion. For \(d=0\), every power is the constant one.

The averaging projection \(p\mapsto |W|^{-1}\sum_{w\in W}w p\) is onto the invariant subspace. Its value on \(\lambda^d\) is a nonzero constant multiple of
\[
O_{\lambda,d}(H)=\sum_{\nu\in W\lambda}\nu(H)^d,
\tag{3.5}
\]
where the sum lists distinct orbit points. Thus these orbit-power sums, with \(\lambda\) dominant integral, span \(S^d(\mathfrak h^*)^W\).

**Finally, lift each orbit-power sum.** Let \(R_\lambda:\mathfrak g\to\operatorname{End}L(\lambda)\) be the finite-dimensional representation for \(\lambda\in\Lambda^+\). The polynomial
\[
T_{\lambda,d}(X)=\operatorname{Tr}\bigl(R_\lambda(X)^d\bigr)
\tag{3.6}
\]
is invariant. For \(d\ge1\), its derivative in the direction \([x,X]\) is the trace of
\[
[R_\lambda(x),R_\lambda(X)^d],
\]
because expanding the derivative of the power telescopes to this commutator. Its trace is zero. For \(d=0\), it is the constant \(\dim L(\lambda)\), so invariance also holds.

On \(\mathfrak h\), simultaneous diagonalization gives
\[
\operatorname{Res}T_{\lambda,d}
=\sum_{\nu}\dim L(\lambda)_\nu\,\nu^d
=O_{\lambda,d}+
\sum_{\substack{\mu\in\Lambda^+\\\mu<\lambda}}
m_{\lambda\mu}O_{\mu,d}.
\tag{3.7}
\]
The last sum is finite. Weyl multiplicities are constant, every integral orbit has a unique dominant representative, and that representative is still a weight, hence at most \(\lambda\). The top orbit has multiplicity one. All these assertions were proved in the preceding lesson.

We must justify inversion rather than appeal to an infinite triangular matrix. For fixed \(\lambda\), the set
\[
D_\lambda=\{\mu\in\Lambda^+:\mu\le\lambda\}
\]
is finite. Use the positive definite real root inner product and write \(\lambda-\mu=\sum_i c_i\alpha_i\) with nonnegative integers \(c_i\). Dominance gives
\[
\|\lambda\|^2-\|\mu\|^2
=\sum_i c_i(\lambda+\mu,\alpha_i)\ge0.
\tag{3.8}
\]
The weight lattice is discrete, so this bounds \(D_\lambda\) inside a finite lattice ball. Moreover \(\mu<\lambda\) implies \(D_\mu\subsetneq D_\lambda\). Inducting on \(|D_\lambda|\), equation (3.7) therefore writes \(O_{\lambda,d}\) as the restriction of a finite integer linear combination of the polynomials \(T_{\mu,d}\). Since (3.5) spans all invariants of degree \(d\), restriction is surjective in every degree. Together with injectivity and the obvious compatibility with products and degrees, this proves (3.2). \(\square\)

For rank zero, \(\mathfrak g=0\), both rings are \(\mathbb C\), and restriction is the identity; the preceding proof has its empty-variable interpretation.

The Killing form \(\kappa\) gives equivariant identifications \(\mathfrak g\cong\mathfrak g^*\) and \(\mathfrak h\cong\mathfrak h^*\). Root spaces are orthogonal to \(\mathfrak h\), and \(\kappa|_{\mathfrak h}\) is nondegenerate. Consequently (3.2) is equivalently
\[
\operatorname{res}:S(\mathfrak g)^{\mathfrak g}
\xrightarrow{\ \sim\ }S(\mathfrak h)^W,
\tag{3.9}
\]
where \(\operatorname{res}\) sets every root-space variable to zero. For instance, the function on \(\mathfrak g\) attached to \(x\in\mathfrak g\) is \(X\mapsto\kappa(x,X)\); its restriction is attached to the Cartan projection of \(x\). This checks that (3.9) has precisely the projection used by the PBW leading-term calculation.

## 4. Passing from symbols to central elements

Give \(U\) the PBW filtration \(F_dU\). If \(z\in Z\) has degree \(d\) and leading symbol \(p\in S^d(\mathfrak g)\), then \(p\) is adjoint-invariant. Indeed the commutator derivation \([x,-]\) induces on symbols the adjoint derivation of \(S(\mathfrak g)\); \([x,z]=0\) gives \(x\cdot p=0\).

In triangular PBW coordinates, the degree-\(d\) part of \(\xi(z)\) is \(\operatorname{res}p\). A word containing a root variable projects to zero in either calculation; a pure Cartan word projects to itself. Translation by \(-\rho\) changes only lower-degree terms. Hence
\[
\bigl[\gamma(z)\bigr]_d=\operatorname{res}p.
\tag{4.1}
\]
The notation on the left means the homogeneous part of degree \(d\), even if it were zero.

**Theorem 4.1 (Harish-Chandra).** The map
\[
\gamma:Z(U(\mathfrak g))\xrightarrow{\ \sim\ }S(\mathfrak h)^W
\tag{4.2}
\]
is a filtered algebra isomorphism. Its associated graded map is Chevalley restriction under PBW.

**Proof.** It is an algebra homomorphism into the stated target by Propositions 1.1 and 2.1.

If \(z\ne0\), its leading symbol \(p\ne0\) is invariant. Injectivity of (3.9) gives \(\operatorname{res}p\ne0\), and (4.1) gives \(\gamma(z)\ne0\). This proves injectivity and equality of degrees.

For surjectivity, take an invariant polynomial \(q\) of degree \(d\), and let \(q_d\) be its highest homogeneous part. The Weyl action preserves degrees, so \(q_d\) is invariant. By (3.9), there is \(p_d\in S^d(\mathfrak g)^{\mathfrak g}\) restricting to \(q_d\). Equivariant symmetrization gives the central element \(z_d=\operatorname{sym}(p_d)\). Equation (4.1) shows that \(q-\gamma(z_d)\) has degree at most \(d-1\), and Proposition 2.1 shows it is still invariant. Induction on degree constructs its central preimage. Constants have their own constant preimages, so the induction terminates. It also keeps every preimage in \(F_dU\).

The same argument shows \(\operatorname{gr}Z=S(\mathfrak g)^{\mathfrak g}\): every invariant homogeneous symbol has a central symmetrized lift, and every central symbol is invariant. Thus (4.1) identifies the associated graded map with (3.9), as asserted. \(\square\)

In particular, a central element acting as zero on every Verma module is zero. Its \(\xi\)-polynomial vanishes at every \(\lambda\), hence is zero; then its \(\gamma\)-polynomial is zero, and injectivity applies. The proof supplies both the PBW and density steps behind this assertion.

Symmetrization itself remains a vector-space isomorphism on invariants, rather than the algebra map (4.2). Its lower-degree corrections are exactly what the induction accommodates.

## 5. Central characters and shifted orbits

**Lemma 5.1.** For any finite linear group \(G\) on a complex vector space, invariant polynomials distinguish distinct \(G\)-orbits.

**Proof.** Let \(A,B\) be disjoint orbits. Choose a linear functional \(\ell\) taking distinct values at all points of the finite set \(A\cup B\): the excluded functionals lie in finitely many proper hyperplanes. One-variable Lagrange interpolation produces a polynomial \(p\) with \(p(\ell(a))=1\) for \(a\in A\), and \(p(\ell(b))=0\) for \(b\in B\). Average the polynomial \(p\circ\ell\) over \(G\). The result is invariant and retains values one on \(A\) and zero on \(B\). \(\square\)

**Corollary 5.2 (central-character linkage).** For all complex \(\lambda,\mu\in\mathfrak h^*\),
\[
\chi_\lambda=\chi_\mu
\quad\Longleftrightarrow\quad
\mu+\rho\in W(\lambda+\rho)
\quad\Longleftrightarrow\quad
\mu\in W\mathbin{\cdot}\lambda.
\tag{5.1}
\]
Thus \(L(\lambda)\) and \(L(\mu)\), or their Verma modules, have the same central character precisely in this case.

**Proof.** Equation (2.2) identifies the two characters with evaluation at \(\lambda+\rho\) and \(\mu+\rho\) on the range of \(\gamma\). By Theorem 4.1, that range is the entire invariant ring. Points in one orbit give the same evaluation. Points in distinct orbits give different evaluations by Lemma 5.1. \(\square\)

Here “linkage” records equality of central characters; an assertion about extensions or composition factors would require further work. For dominant integral \(\lambda,\mu\), both shifted weights are strictly dominant. The uniqueness of a chamber representative gives \(\chi_\lambda=\chi_\mu\) only when \(\lambda=\mu\).

## 6. The form and the Casimir normalization

Let \(B\) be any nondegenerate invariant symmetric bilinear form on \(\mathfrak g\). Its restriction to \(\mathfrak h\) is nondegenerate. Indeed invariance makes \(\mathfrak h\) orthogonal to all root spaces, and makes two root spaces orthogonal unless their roots sum to zero. Nondegeneracy on the full direct sum therefore gives nondegeneracy on \(\mathfrak h\) and on each opposite-root pairing.

For \(\eta\in\mathfrak h^*\), define \(t_\eta\in\mathfrak h\) by \(B(t_\eta,H)=\eta(H)\), and put
\[
(\eta,\zeta)_B=B(t_\eta,t_\zeta).
\]
This is the inverse-form pairing; it need not be a positive real form for arbitrary complex \(B\). Choose dual Cartan bases \(H_a,H^a\), and opposite root vectors \(E_\alpha,F_\alpha\) with \(B(E_\alpha,F_\alpha)=1\) for every positive root. The dual-basis Casimir from the PBW lesson is
\[
\Omega_B=\sum_a H_aH^a+
\sum_{\alpha>0}(E_\alpha F_\alpha+F_\alpha E_\alpha)\in Z.
\tag{6.1}
\]
For \(H\in\mathfrak h\), invariance gives
\[
B([E_\alpha,F_\alpha],H)
=B(E_\alpha,[F_\alpha,H])=\alpha(H).
\]
Thus \([E_\alpha,F_\alpha]=t_\alpha\). Ordering (6.1) with raising operators on the right gives
\[
\Omega_B=\sum_a H_aH^a+2\sum_{\alpha>0}F_\alpha E_\alpha
+\sum_{\alpha>0}t_\alpha.
\tag{6.2}
\]

**Proposition 6.1.** On every highest-weight module of highest weight \(\lambda\),
\[
\chi_\lambda(\Omega_B)=(\lambda,\lambda+2\rho)_B,
\qquad
\gamma(\Omega_B)(\nu)=(\nu,\nu)_B-(\rho,\rho)_B.
\tag{6.3}
\]

**Proof.** In (6.2), the terms \(F_\alpha E_\alpha\) kill the highest vector. The Cartan sum evaluates to \((\lambda,\lambda)_B\), and \(\lambda(t_\alpha)=(\lambda,\alpha)_B\). Summing the positive roots gives the first equality. Centrality extends it to the module. Substitution \(\lambda=\nu-\rho\) gives the second. \(\square\)

For \(\mathfrak{sl}_2\), fix \([h,e]=2e,[h,f]=-2f,[e,f]=h\). Write \(t(\nu)=\nu(h)\), so \(\rho(h)=1\) and the Weyl action is \(t\mapsto-t\). The Killing form has \(\kappa(h,h)=8,\kappa(e,f)=4\). Therefore
\[
C:=8\Omega_\kappa=h^2+2h+4fe,\qquad
\xi(C)=h^2+2h,\qquad \gamma(C)=t^2-1.
\tag{6.4}
\]
The distinction between the element \(h\) of \(S(\mathfrak h)\) and its polynomial value \(t\) is only notation. Since every even polynomial in \(t\) is a polynomial in \(t^2-1\), Theorem 4.1 gives
\[
Z(U(\mathfrak{sl}_2))=\mathbb C[C].
\tag{6.5}
\]
There is no polynomial relation on \(C\), since \(t^2-1\) is algebraically independent. With \(m=\lambda(h)\), the scalar of \(C\) is \(m(m+2)\), and its central-character class is
\[
\{m,-m-2\}.
\tag{6.6}
\]
This is a singleton when \(m=-1\). In spin notation \(m=2j\), the Killing-form Casimir \(\Omega_\kappa\) has scalar \(j(j+1)/2\); the commonly used operator with scalar \(j(j+1)\) is \(2\Omega_\kappa=C/4\).

## 7. Higher moments and a useful boundary

Use the inverse Killing pairing on weights. For \(N\ge1\), define the invariant polynomial
\[
F_{2N}(\nu)=\sum_{\alpha\in\Phi}(\nu,\alpha)_\kappa^{2N}.
\tag{7.1}
\]
It is the function \(\operatorname{Tr}((\operatorname{ad}t_\nu)^{2N})\), since the nonzero adjoint weights are the roots. Theorem 4.1 supplies a unique central element \(z_N\) such that
\[
\gamma(z_N)=F_{2N}-F_{2N}(\rho),\qquad
\chi_\lambda(z_N)=F_{2N}(\lambda+\rho)-F_{2N}(\rho).
\tag{7.2}
\]
These elements are obtained by the proved isomorphism; no general Duflo theorem is needed here.

To check the normalization in Deligne–de Man's moment description, let
\[
M_\eta=\sum_{\alpha>0}\delta_{\,12(\eta,\alpha)_\kappa},
\qquad L_\lambda=M_{\lambda+\rho}-M_\rho,
\tag{7.3}
\]
where \(\delta_x\) is a unit point mass. Opposite roots contribute equally to each even power, so directly from these definitions,
\[
\chi_\lambda(z_N)=
2\,12^{-2N}\int x^{2N}\,dL_\lambda(x).
\tag{7.4}
\]
This is the central-character mechanism in Deligne and de Man, *La série exceptionnelle de groupes de Lie II*, pp. 578–579, formulas (1)–(4). Their further interpolation in the exceptional-series parameter is not needed for, or asserted by, (7.4). Their dimension product is also outside this moment calculation.

For \(N=1\), the definition of the Killing form gives
\[
F_2(\nu)=\operatorname{Tr}((\operatorname{ad}t_\nu)^2)
=\kappa(t_\nu,t_\nu)=(\nu,\nu)_\kappa.
\]
Equation (6.3) and uniqueness under \(\gamma\) then identify \(z_1=\Omega_\kappa\), exactly with this normalization.

Adjoint moments need not generate all central characters. In \(\mathfrak{sl}_3\), for \(H=\operatorname{diag}(x,y,z)\) with \(x+y+z=0\),
\[
\operatorname{Tr}((\operatorname{ad}H)^3)
=\sum_{i\ne j}(x_i-x_j)^3=0,
\quad
\operatorname{Tr}(H^3)=x^3+y^3+z^3=3xyz.
\tag{7.5}
\]
The second polynomial is a nonzero Weyl-invariant cubic, while every even adjoint moment is unchanged by negation. Through Killing identification, the cubic is a polynomial on \(\mathfrak h^*\), and has a central preimage under \(\gamma\).

More concretely, with \(\omega_1=(2,-1,-1)/3\), \(\omega_2=(1,1,-2)/3\), and \(\rho=(1,0,-1)\), the shifted weights are
\[
\omega_1+\rho=(5,-1,-4)/3,\qquad
\omega_2+\rho=(4,1,-5)/3.
\tag{7.6}
\]
The second is a permutation of the negative of the first, and is not a permutation of the first. All even root moments agree on the pair, but their coordinate cubic sums are \(20/9\) and \(-20/9\). Thus the central characters differ. The normalization factor introduced by Killing identification rescales both nonzero cubic values equally and does not affect separation.

This also explains why the full proof in Section 3 uses traces in all irreducible representations. Restricting that construction to the adjoint representation would lose the required invariant cubic in this example.

## 8. Exercises with complete solutions

### Exercise 8.1 — Generate the rank-one centre (easy)

For the relations and element \(C\) of (6.4), determine the centre of \(U(\mathfrak{sl}_2)\), including whether \(C\) satisfies any polynomial relation.

**Solution.** Theorem 4.1 identifies the centre with the invariants of \(t\mapsto-t\). If \(p(t)=\sum a_k t^k\), then \(p(-t)=p(t)\) forces every odd coefficient to vanish, so the invariant ring is \(\mathbb C[t^2]\). Since \(\gamma(C)=t^2-1\), every invariant is \(q(\gamma(C))\) for a polynomial \(q\). Surjectivity and injectivity imply that every central element is the same \(q(C)\). If \(q(C)=0\), then \(q(t^2-1)=0\). A nonzero polynomial \(q\) of degree \(d\) would give a polynomial of degree \(2d\) with the same nonzero leading coefficient. Hence \(q=0\), proving that the centre is a polynomial algebra freely generated by \(C\).

### Exercise 8.2 — Locate the shift (medium)

Compute the projection and shifted image of \(C= h^2+2h+4fe\). Verify its eigenvalue on a highest-weight module, and compare it with the Killing-form Casimir.

**Solution.** The term \(fe\) has negative and positive blocks, so projects to zero. The remaining terms give \(\xi(C)(m)=m^2+2m\). Translation is by minus \(\rho(h)=1\), hence
\[
\gamma(C)(t)=(t-1)^2+2(t-1)=t^2-1.
\]
This is fixed by \(t\mapsto-t\). On the highest vector of weight \(m\), \(e\) kills the vector and \(h\) acts by \(m\), giving \(m(m+2)\). Centrality gives that value on the whole module. Formula (6.1) with the Killing dual bases gives \(\Omega_\kappa=h^2/8+(ef+fe)/4=C/8\). Its eigenvalue is \(m(m+2)/8\), not \(m(m+2)\). Replacing \(m\) by \(2j\) gives \(j(j+1)/2\).

### Exercise 8.3 — Recover linkage from the centre (medium)

Prove (5.1) for arbitrary complex highest weights, and describe all rank-one classes, including the singular shifted weight.

**Solution.** The action formula is \(\chi_\lambda(z)=\gamma(z)(\lambda+\rho)\). If the shifted weights are in the same Weyl orbit, invariance of \(\gamma(z)\) makes every value agree. Conversely, if the orbits are distinct, choose a linear functional separating all their points, interpolate a polynomial equal to one on the first orbit and zero on the second, and average over \(W\), as in Lemma 5.1. Theorem 4.1 gives a central preimage of this separating polynomial, whose two character values differ. Equality of characters therefore forces equality of shifted orbits.

In rank one the shifted coordinate is \(m+1\). Its orbit is \(\{m+1,-m-1\}\); subtracting one gives \(\{m,-m-2\}\). At \(m=-1\) the shifted coordinate is zero and its orbit has one point. For all other complex \(m\) the class has two points. No integrality or finite-dimensional hypothesis was used.

### Exercise 8.4 — Make injectivity explicit (hard)

Suppose a central element \(z\) acts by zero on every Verma module. Prove \(z=0\), and deduce injectivity of \(\gamma\).

**Solution.** Proposition 1.1 says \(\xi(z)(\lambda)=0\) for every \(\lambda\), so polynomial density gives \(\xi(z)=0\), hence \(\gamma(z)=0\). Suppose nevertheless \(z\ne0\), with PBW degree \(d\). Its nonzero leading symbol \(p\in S^d(\mathfrak g)\) is invariant because all commutators \([x,z]\) vanish. Equation (4.1) says \(\operatorname{res}p=0\).

Identify \(p\) with a polynomial \(F\) on \(\mathfrak g\) by the Killing form. It is invariant and zero on \(\mathfrak h\). For the map \(\Psi\) of (3.4), root exponential invariance gives \(F\circ\Psi=0\). The derivative at \((0,H_0)\) is an isomorphism, with root entries \(-\alpha(H_0)x_\alpha\) and the identity Cartan block. If \(F\) were nonzero, its first nonzero homogeneous term after translation to \(H_0\) would remain nonzero after substitution of this invertible linear part. It would be the first nonzero term of \(F\circ\Psi\), a contradiction. Thus \(F=0\), hence \(p=0\), contradicting its choice.

We have proved \(z=0\). Finally, \(\gamma(z)=0\) implies \(\xi(z)=0\) by inverse translation, so \(z\) acts by zero on every Verma module by Proposition 1.1. The proved assertion then gives \(z=0\), establishing injectivity without assuming it in the argument.

## 9. Polynomial generators for the Weyl invariants

**Theorem 9.1.** Let \(\mathfrak g\) be a finite-dimensional complex semisimple Lie algebra, let \(\mathfrak h\) be a Cartan subalgebra of dimension \(r\), and let \(W\) be its Weyl group. There are homogeneous positive-degree polynomials \(q_1,\ldots,q_r\) on \(\mathfrak h\) such that
\[
\mathbb C[\mathfrak h]^W=\mathbb C[q_1,\ldots,q_r]
\]
and the \(q_i\) are algebraically independent. The equivariant Killing identification gives the same assertion for \(S(\mathfrak h)^W\). For rank zero, the list is empty and the ring is \(\mathbb C\).

The proof does not invoke the Chevalley–Shephard–Todd theorem, the Nullstellensatz, a theorem about regular local rings, or algebraic dimension theory. The basic facts about complex eigenvalues and factorization of a polynomial over \(\mathbb C\) are used explicitly.

### 9.1. Orbit sums and fundamental characters

Write \(P=\bigoplus_{i=1}^r\mathbb Z\omega_i\) for the weight lattice, with fundamental weights \(\omega_i\), and \(P^+=\sum_i\mathbb Z_{\ge0}\omega_i\). These are RT-LIE-14, §1, equations (1.2)–(1.4). The order is \(\mu\le\lambda\) if \(\lambda-\mu\) is a nonnegative integral combination of simple roots.

**Lemma 9.1 (dominant orbit representative).** Every integral weight orbit has exactly one dominant member.

**Proof.** Choose a vector \(v\) in the open dominant chamber of the real weight space. On a finite orbit, take \(\eta\) maximizing \((v,\eta)\). If \((\eta,\alpha_i)<0\), then
\[
(v,s_i\eta-\eta)
=-\langle\eta,\alpha_i^\vee\rangle(v,\alpha_i)>0,
\]
contradicting maximality. Thus \(\eta\) is dominant.

For uniqueness, first take dominant \(\lambda\) and a reduced word \(w=s_{i_1}\cdots s_{i_\ell}\). Set \(u_j=s_{i_1}\cdots s_{i_{j-1}}\). Every \(u_j\alpha_{i_j}\) is positive: the prefix of length \(j\) is reduced, and the root-sign criterion in RT-LIE-08, equations (4.3)–(4.5), says that appending \(s_{i_j}\) increases length exactly when that root is positive. Telescoping gives
\[
\lambda-w\lambda
=\sum_{j=1}^{\ell}
\langle\lambda,\alpha_{i_j}^{\vee}\rangle\,u_j\alpha_{i_j}\in Q^+.
\tag{9.1}
\]
The coefficients are nonnegative integers because \(\lambda\) is dominant integral. If both \(\lambda\) and \(\mu=w\lambda\) are dominant, apply (9.1) to \(\lambda,w\) and to \(\mu,w^{-1}\). Then both \(\lambda-\mu\) and \(\mu-\lambda\) lie in \(Q^+\), so independence of the simple roots implies equality. \(\square\)

Put
\[
B=\mathbb C[P]=\mathbb C[z_1^{\pm1},\ldots,z_r^{\pm1}],
\qquad z_i=e^{\omega_i},\qquad D=B^W.
\]
The action is \(w(e^\lambda)=e^{w\lambda}\). The invariant Laurent polynomials have the vector-space basis
\[
\sigma_\lambda=\sum_{\nu\in W\lambda}e^\nu,\qquad \lambda\in P^+,
\tag{9.2}
\]
where each sum lists distinct orbit points. Indeed invariance means precisely that the finite list of Laurent coefficients is constant on every orbit.

Let \(\chi_i=\operatorname{ch}L(\omega_i)\). RT-LIE-14, Theorems 2.1, 3.1 and 4.1, give finite characters, \(W\)-invariant multiplicities, top multiplicity one, and all weights below the highest weight.

**Proposition 9.2.** The fundamental characters freely generate the invariant group algebra:
\[
D=\mathbb C[\chi_1,\ldots,\chi_r].
\tag{9.3}
\]

**Proof.** For \(\lambda=\sum_i n_i\omega_i\in P^+\), form \(c_\lambda=\prod_i\chi_i^{n_i}\). Every exponent occurring in this product is at most \(\lambda\). Its coefficient at \(e^\lambda\) is one: to reach \(\lambda\), every chosen weight in every factor must be its top weight, since a sum of nonnegative simple-root differences can vanish only when all differences vanish. The product is \(W\)-invariant. Its other dominant exponents are weights of that product and therefore strictly below \(\lambda\). Consequently
\[
c_\lambda=\sigma_\lambda+
\sum_{\substack{\mu\in P^+\\\mu<\lambda}}a_{\lambda\mu}\sigma_\mu,
\qquad a_{\lambda\mu}\in\mathbb Z_{\ge0},
\tag{9.4}
\]
with a finite sum.

The set \(D_\lambda=\{\mu\in P^+:\mu\le\lambda\}\) is finite, as proved explicitly in RT-LIE-15, §3, equation (3.8). For completeness, if \(\lambda-\mu=\sum_i c_i\alpha_i\), dominance gives
\[
\|\lambda\|^2-\|\mu\|^2
=\sum_i c_i(\lambda+\mu,\alpha_i)\ge0;
\]
a bounded ball contains only finitely many points of \(P\). Also \(\mu<\lambda\) gives \(D_\mu\subsetneq D_\lambda\). Induction on \(|D_\lambda|\), using (9.4), expresses every \(\sigma_\lambda\) in the \(\chi_i\). This proves generation.

If a nonzero polynomial relation among the \(\chi_i\) existed, its distinct monomials would correspond to distinct dominant weights \(\lambda=\sum_i n_i\omega_i\). In the finite set of these weights choose a maximal member \(\lambda_0\) for the partial order. Its term contributes its nonzero coefficient to \(\sigma_{\lambda_0}\). No other term can contribute to that orbit sum: (9.4) would require \(\lambda_0\le\lambda\), contradicting maximality unless \(\lambda=\lambda_0\). This contradicts the relation. Thus the generators are algebraically independent. \(\square\)

The \(\chi_i\) here are formal characters in a Laurent algebra. Their use does not require integration of a Lie algebra representation to a specified algebraic group.

### 9.2. Elementary finite algebra lemmas

The following arguments will be used both on the torus and on its linear tangent space.

**Lemma 9.3 (finite module by orbit polynomials).** If a finite group \(G\) acts on a commutative \(\mathbb C\)-algebra \(R\), and \(R\) is generated as a \(\mathbb C\)-algebra by \(a_1,\ldots,a_s\), then \(R\) is a finite module over \(R^G\).

**Proof.** For each generator,
\[
\prod_{g\in G}(T-g a_j)
\tag{9.5}
\]
is a monic degree-\(|G|\) polynomial with coefficients in \(R^G\). Reduction by these identities expresses every generator monomial as an \(R^G\)-linear combination of the finitely many monomials \(a_1^{b_1}\cdots a_s^{b_s}\), \(0\le b_j<|G|\). \(\square\)

For \(B\), use the \(2r\) generators \(z_i,z_i^{-1}\). For \(\mathbb C[\mathfrak h]\), use \(r\) linear coordinates. No general theorem about integral extensions is needed.

**Lemma 9.4 (finite residue fields).** If \(E\) is a nonzero finite-dimensional commutative unital \(\mathbb C\)-algebra, its maximal ideals are exactly the kernels of its unital \(\mathbb C\)-algebra maps to \(\mathbb C\).

**Proof.** A proper ideal of maximal vector-space dimension exists, and is maximal. For any maximal ideal \(\mathfrak a\), the quotient \(K=E/\mathfrak a\) is a field: for any nonzero class \(u\), the ideal it generates is the whole quotient, giving an inverse. It is finite-dimensional over \(\mathbb C\). Every \(u\in K\) satisfies a nonzero polynomial over \(\mathbb C\), by linear dependence of its powers. Factoring that polynomial into linear factors, the field property forces \(u\) to equal one of its complex roots. Thus \(K=\mathbb C\). Conversely a unital map to \(\mathbb C\) contains the constants in its image, so is onto and has maximal kernel. \(\square\)

**Lemma 9.5 (unique character gives nilpotence).** Suppose the algebra \(E\) of Lemma 9.4 has only one unital \(\mathbb C\)-algebra map \(\varepsilon:E\to\mathbb C\). If \(b_1,\ldots,b_s\in\ker\varepsilon\), then every product of \(N=\dim_\mathbb C E\) of these elements is zero.

**Proof.** Consider their multiplication operators, together with a vector-space basis of all multiplication operators \(M_a\), \(a\in E\). This is a finite commuting family. Any finite commuting family of complex matrices has a common eigenvector: choose an eigenspace for the first matrix; it is preserved by every other matrix; restrict to it, choose an eigenspace for the second, and continue. The last resulting nonzero space contains a common eigenvector. The quotient by its line again has commuting operators. Induction on the vector-space dimension gives an invariant full flag, and hence simultaneous upper triangular matrices.

At each diagonal position the assignment \(a\mapsto (M_a)_{jj}\) is a unital \(\mathbb C\)-algebra map, since multiplication operators respect sums, scalars, products and the unit, and diagonal entries multiply for upper triangular matrices. It must therefore be \(\varepsilon\). Each \(M_{b_i}\) is strictly upper triangular. A product of \(N\) strictly upper triangular \(N\)-by-\(N\) matrices is zero: a potentially nonzero entry would require a strictly increasing chain of \(N+1\) indices among \(N\) indices. Hence the multiplication operator of the corresponding product is zero. Apply it to \(1\in E\) to obtain the asserted zero element. \(\square\)

**Lemma 9.6 (separating finite orbits).** Invariant polynomials separate distinct finite orbits of a finite linear group on a complex vector space. Invariant Laurent polynomials also separate distinct orbits of the action of \(W\) on \(T=(\mathbb C^\times)^r\) defined by its lattice action.

**Proof.** For two disjoint finite orbits, choose an ordinary linear polynomial \(\ell\) in the coordinates taking distinct values on their union. Such a choice exists because the bad choices form a finite union of proper hyperplanes. A finite union of proper hyperplanes cannot fill a complex vector space: their defining nonzero linear polynomials have a nonzero product, and a nonzero polynomial cannot vanish everywhere, by induction on the number of variables and the one-variable root bound. Lagrange interpolation gives \(p\) with \(p(\ell)=0\) on the first orbit and \(1\) on the second. Average \(p(\ell)\) over the group. Its values remain \(0\) and \(1\). In the linear case the average is polynomial; in the torus case it is Laurent polynomial because all lattice automorphisms preserve \(B\). This is the linear proof of RT-LIE-15, Lemma 5.1, with the torus extension justified explicitly. \(\square\)

**Lemma 9.7 (Reynolds contraction and quotient).** Write \(D=R^G\), and let \(K\) be an ideal of \(D\). Then
\[
D\cap KR=K,\qquad (R/KR)^G\cong D/K.
\tag{9.6}
\]

**Proof.** The averaging projection \(\mathcal R(a)=|G|^{-1}\sum_g ga\) is \(D\)-linear. If \(d=\sum_j k_j a_j\in D\cap KR\), then \(d=\mathcal R(d)=\sum_jk_j\mathcal R(a_j)\in K\). The reverse inclusion is immediate. If a class \(\bar a\in R/KR\) is invariant, then \(\mathcal R(a)-a\in KR\), since every \(ga-a\) lies in that ideal. Thus every invariant quotient class has an invariant lift. The kernel of the resulting map \(D\to(R/KR)^G\) is the contraction just computed. \(\square\)

### 9.3. The torus identity and its completion

Let
\[
\mathfrak m=(z_1-1,\ldots,z_r-1)\subset B,\qquad
t_i=\chi_i-\chi_i(1),\qquad
M=(t_1,\ldots,t_r)\subset D.
\tag{9.7}
\]
Here \(\chi_i(1)=\dim L(\omega_i)\). By Proposition 9.2, \(D=\mathbb C[t_1,\ldots,t_r]\) and \(D/M=\mathbb C\).

By Lemma 9.3, \(B\) is a finite \(D\)-module. Thus \(E=B/MB\) is a finite-dimensional nonzero \(\mathbb C\)-algebra; evaluation at the torus identity shows it is nonzero.

A character of \(E\) lifts to a character of \(B\). Such a character assigns nonzero complex numbers to each invertible \(z_i\), and is therefore evaluation at a point \(p\in T\). The relations defining \(MB\) say \(\chi_i(p)=\chi_i(1)\). Since the \(\chi_i\) generate \(D\), every invariant Laurent polynomial has equal values at \(p\) and \(1\). Lemma 9.6 forces \(p\) into the orbit of \(1\). This orbit is the singleton \(\{1\}\), because every lattice automorphism fixes evaluation of all lattice symbols at one. Hence \(E\) has exactly one character.

Lemma 9.5, applied to the images of \(z_i-1\), gives
\[
\mathfrak m^N\subset MB\subset\mathfrak m,\qquad
N=\dim_\mathbb C(B/MB).
\tag{9.8}
\]
The second inclusion follows also directly from \(\chi_i(1)-\chi_i(1)=0\). Taking powers yields
\[
\mathfrak m^{Nk}\subset M^kB\subset\mathfrak m^k
\quad(k\ge1).
\tag{9.9}
\]

Define a completion by the indicated inverse limit of quotient rings. The cofinal inclusions (9.9) identify
\[
\varprojlim_k B/M^kB\ \cong\ \varprojlim_k B/\mathfrak m^k.
\tag{9.10}
\]
Here no completeness theorem is being assumed: a compatible sequence modulo \(\mathfrak m^j\) determines its residue modulo \(M^kB\) by using its component with \(j=Nk\); the reverse map uses \(M^kB\subset\mathfrak m^k\). The two composites are identity because they preserve every fixed residue after passing to a sufficiently high index. These maps are \(W\)-equivariant.

Invariants commute with an inverse limit: a compatible sequence is fixed precisely when each component is fixed. Lemma 9.7 with \(K=M^k\) therefore gives
\[
\widehat D_M
:=\varprojlim_k D/M^k
\ \cong\
\left(\varprojlim_k B/\mathfrak m^k\right)^W.
\tag{9.11}
\]

Put \(u_i=z_i-1\). For every \(k\),
\[
B/\mathfrak m^k
\cong\mathbb C[u_1,\ldots,u_r]/(u_1,\ldots,u_r)^k,
\]
because each \(1+u_i\) has the finite geometric-series inverse modulo that power. Consequently the completed torus algebra is \(\mathbb C[[u_1,\ldots,u_r]]\).

The formal substitutions
\[
z_i=\exp(x_i),\qquad
u_i=\exp(x_i)-1,\qquad
x_i=\log(1+u_i)
\tag{9.12}
\]
are mutually inverse continuous isomorphisms of power-series rings. The series have zero constant term where required, so substitution is defined coefficient by coefficient; \(\exp\) and \(\log\) are inverse formal series in characteristic zero. For example their compositions have derivative one and constant term zero, hence are the identity, since differentiation of formal series and the usual chain rule hold coefficientwise.

They also linearize the \(W\)-action. If \(w\omega_i=\sum_j a_{ji}\omega_j\), with integers \(a_{ji}\), then
\[
wz_i=\prod_j z_j^{a_{ji}},
\qquad
wx_i=\sum_j a_{ji}x_j.
\tag{9.13}
\]
The second equality follows by substituting the exponentials into the first and using \(\exp(a+b)=\exp(a)\exp(b)\), valid for commuting formal series; integer powers, including negative ones, are covered. Take \(x_i(H)=\omega_i(H)\), so this is exactly the action on linear functions on \(\mathfrak h\). Therefore
\[
\widehat D_M\cong\mathbb C[[\mathfrak h]]^W.
\tag{9.14}
\]
On the other hand, \(D=\mathbb C[t_1,\ldots,t_r]\) makes its \(M\)-adic completion explicitly \(\mathbb C[[t_1,\ldots,t_r]]\). We have proved
\[
\mathbb C[[\mathfrak h]]^W
\cong\mathbb C[[t_1,\ldots,t_r]]
\tag{9.15}
\]
as augmented complete \(\mathbb C\)-algebras. This is a formal statement, with no analytic exponential or quotient-space smoothness assumption.

### 9.4. The graded polynomial invariants

Put \(S=\mathbb C[\mathfrak h]=\mathbb C[x_1,\ldots,x_r]\), \(A=S^W\), and \(J=A_+=\bigoplus_{d>0}A_d\).

**Lemma 9.8.** The algebra \(A\) is finitely generated by homogeneous positive-degree elements.

**Proof.** The polynomial ring \(S\) is Noetherian by the complete monomial proof of RT-LIE-13, Lemma 3.2. Thus \(I=JS\) has finitely many ideal generators. Each of those is a finite sum of multiples of elements of \(J\). Collecting the finitely many elements of \(J\) occurring in these sums gives finite generators of \(I\). Replacing them by all their homogeneous components gives finitely many homogeneous \(f_1,\ldots,f_s\in J\) still generating \(I\): the new components are themselves invariants of positive degree and belong to \(I\), while the old generators are sums of them.

For homogeneous \(f\in A_d\), \(d>0\), write \(f=\sum_j f_j b_j\) in \(S\). Taking homogeneous components of degree \(d\), we may take \(b_j\) homogeneous of degree \(d-\deg f_j<d\), omitting negative degrees. Averaging gives \(f=\sum_j f_j\mathcal R(b_j)\). Each coefficient is invariant of lower degree. Induction on \(d\), starting with \(A_0=\mathbb C\), proves \(A=\mathbb C[f_1,\ldots,f_s]\). \(\square\)

In particular \(J=(f_1,\ldots,f_s)\) as an ideal of \(A\): a polynomial in these positive-degree generators with zero degree-zero component has zero constant term and belongs to that ideal.

Lemma 9.3 also makes \(S\) a finite \(A\)-module. Therefore \(E_0=S/JS\) is finite-dimensional and nonzero. Its characters are evaluations at points of \(\mathfrak h\): images of the polynomial coordinates specify a point and determine the map. Such a character annihilates all positive-degree invariant polynomials. Its point \(p\) therefore has the same invariant evaluations as \(0\), since the degree-zero invariants are constants. Lemma 9.6 forces \(p=0\). Thus \(E_0\) has only its zero-evaluation character.

Applying Lemma 9.5 to the coordinate images gives, for \(\mathfrak n=(x_1,\ldots,x_r)\subset S\),
\[
\mathfrak n^{N_0}\subset JS\subset\mathfrak n,\qquad
\mathfrak n^{N_0k}\subset J^kS\subset\mathfrak n^k,
\quad N_0=\dim_\mathbb C E_0.
\tag{9.16}
\]
The same cofinal-limit argument and Reynolds contraction as in §3 yield
\[
\widehat A_J
:=\varprojlim_k A/J^k
\cong
\left(\varprojlim_k S/\mathfrak n^k\right)^W
=\mathbb C[[\mathfrak h]]^W.
\tag{9.17}
\]
Combining this with (9.15) gives
\[
\widehat A_J\cong\mathbb C[[t_1,\ldots,t_r]].
\tag{9.18}
\]

### 9.5. Completion does not change the first-order quotient

We prove the precise fact needed to recover homogeneous generators from (9.18).

**Lemma 9.9.** Let \(C\) be a commutative \(\mathbb C\)-algebra and \(K=(a_1,\ldots,a_s)\) a finitely generated ideal with \(C/K=\mathbb C\). Put \(C^\wedge=\varprojlim_l C/K^l\), and \(F_n=\ker(C^\wedge\to C/K^n)\). Then
\[
F_n=K^nC^\wedge=F_1^n,\qquad
K/K^2\cong F_1/F_1^2.
\tag{9.19}
\]
Moreover \(F_1\) is the unique maximal ideal of \(C^\wedge\).

**Proof.** Interpret elements of \(C\) in the completion by their compatible residues; injectivity of that map is not needed. The finite list of length-\(n\) monomials in the \(a_i\) generates \(K^n\). Denote it by \(a^I\).

Take \(f\in F_n\). Starting at \(l=n\), construct approximations to \(f\) as follows. If the current approximation has error in \(F_l\), its residue modulo \(K^{l+1}\) is represented by an element \(e_l\in K^l\). Express
\[
e_l=\sum_{|I|=n}a^I b_{I,l},\qquad b_{I,l}\in K^{l-n},
\]
using \(K^l=K^nK^{l-n}\). Add \(e_l\) to the approximation. Its new error belongs to \(F_{l+1}\). For each fixed \(I\), the series \(\sum_{l\ge n}b_{I,l}\) converges in the inverse limit: for a fixed quotient, all sufficiently late terms vanish there. Call its limit \(b_I\). The approximation errors vanish in every fixed quotient, so
\[
f=\sum_{|I|=n}a^I b_I\in K^nC^\wedge.
\]
Conversely every such product vanishes modulo \(K^n\), proving the first equality. For \(n=1\), \(F_1\) is the ideal generated by the images of the finitely many \(a_i\); its \(n\)-th power is therefore exactly the ideal generated by the length-\(n\) monomials. This proves \(F_n=F_1^n\).

Projection to \(C/K^2\) now identifies \(F_1/F_2\) with \(K/K^2\). It is onto because every element of \(K\) has its own compatible image in the completion; its kernel is exactly \(F_2\). With \(F_2=F_1^2\), this is (9.19).

Finally \(C^\wedge/F_1=\mathbb C\), so \(F_1\) is maximal. An element with nonzero image \(c\in\mathbb C\) has the form \(c+h\), \(h\in F_1\), and inverse
\[
c^{-1}\sum_{j\ge0}(-h/c)^j.
\]
This converges because \(h^j\in F_j\); multiplication and the finite geometric-series identity verify it is an inverse in every quotient. Elements of \(F_1\) cannot be units because their images in \(\mathbb C\) are zero. Hence every element outside \(F_1\) is a unit and \(F_1\) is the unique maximal ideal. \(\square\)

Apply this lemma with \(C=A\) and \(K=J\), whose finite generators were proved in Lemma 9.8. The formal power-series ring in (9.18) likewise has unique maximal ideal \((t_1,\ldots,t_r)\), by the same constant-term inverse argument. Any algebra isomorphism maps the unique maximal ideals and their squares to one another. Its first-order quotient is the vector space with basis the linear classes of \(t_i\), since all terms of degree at least two lie in \((t)^2\). Thus
\[
\dim_\mathbb C J/J^2=r.
\tag{9.20}
\]

### 9.6. Homogeneous generators and algebraic independence

The ideal \(J\) and its square are graded, so their finite-dimensional quotient \(J/J^2\) is graded. Choose a homogeneous vector-space basis and lift its elements to homogeneous \(q_1,\ldots,q_r\in J\). Each has strictly positive degree.

**Lemma 9.10.** These elements generate \(A\).

**Proof.** Induct on the ordinary polynomial degree \(d\). For homogeneous \(f\in A_d\), \(d>0\), its class in \(J/J^2\) is a linear combination of those classes of \(q_i\) having degree \(d\); coefficients of other degrees are zero because the quotient is graded and the selected basis is homogeneous. Thus
\[
f-\sum_{\deg q_i=d}c_iq_i\in (J^2)_d.
\]
By definition this last element is a finite sum of products of two elements of \(J\). Taking degree \(d\) components writes it as a finite sum of products of homogeneous positive-degree invariants, both of degree less than \(d\). The induction hypothesis expresses both factors as polynomials in the \(q_i\). Constants provide degree zero. This proves \(A=\mathbb C[q_1,\ldots,q_r]\). \(\square\)

**Lemma 9.11.** The \(q_i\) are algebraically independent.

**Proof.** Use (9.18) to view their images as formal series \(Q_i(t)\in\mathbb C[[t_1,\ldots,t_r]]\). Their constant terms are zero because they belong to \(J\). Lemma 9.9 and the choice of their classes in \(J/J^2\) imply that their linear terms form an invertible \(r\)-by-\(r\) matrix:
\[
Q_i(t)=\sum_jL_{ij}t_j+\text{terms of total degree at least two},
\qquad \det L\ne0.
\tag{9.21}
\]

For a nonzero polynomial \(F(Y_1,\ldots,Y_r)\), let \(F_d\) be its lowest nonzero homogeneous part in ordinary total \(Y\)-degree. After substitution \(Y_i=Q_i(t)\), its lowest \(t\)-degree part is \(F_d(Lt)\). This is nonzero because an invertible linear substitution is an automorphism of a polynomial ring. Hence \(F(Q_1,\ldots,Q_r)\ne0\) as a formal series. If \(F(q_1,\ldots,q_r)\) were zero in \(A\), its image in the completion would be zero, contradicting this calculation. Thus no polynomial relation exists. \(\square\)

This last argument removes the need for a transcendence-degree or dimension argument. Its linear part is in the abstract parameters \(t_i\) of the completed invariant ring; it is not a claim that the ordinary derivatives of \(q_i\) on \(\mathfrak h\) at zero are independent.

Lemmas 9.10–9.11 prove Theorem 9.1 for \(\mathbb C[\mathfrak h]^W\). The \(W\)-equivariant nondegenerate Killing identification \(\mathfrak h\cong\mathfrak h^*\), verified in Section 3, equation (3.9), identifies its homogeneous generators with homogeneous generators of \(S(\mathfrak h)^W\) of the same degrees. This is the symmetric-algebra convention used throughout this lesson.

### 9.7. Rank zero, products and scope

If \(r=0\), \(P=0\), \(W=1\), and \(B=D=S=A=\mathbb C\). The two augmentation ideals are zero. Their completions are \(\mathbb C\), their first-order quotients are zero, and the empty list freely generates \(\mathbb C\).

The proof never assumes the root system is irreducible. In a direct sum of semisimple components the weight lattice and Cartan space are direct sums, and the Weyl group is the product, so all steps apply with the union of their fundamental weights. More explicitly, for two components \(S=S_1\otimes_\mathbb C S_2\); the product Reynolds projection is \(\mathcal R_1\otimes\mathcal R_2\), whose image is \(S_1^{W_1}\otimes S_2^{W_2}\). Therefore the union of the homogeneous generator lists gives the polynomial algebra with \(r_1+r_2\) generators. Injectivity of the polynomial presentation follows also from the tensor product of their monomial bases.

This proves polynomiality for the Weyl action of any finite-dimensional complex semisimple Lie algebra, including reducible and zero algebras. It does not assert the converse of the CST theorem or a theorem for arbitrary complex reflection groups. No generator-degree classification, exponents formula, or choice of distinguished generators is included.

Through the already proved graded Chevalley restriction isomorphism, the adjoint polynomial invariants also become a polynomial algebra. Through the already proved Harish-Chandra isomorphism, the centre of the enveloping algebra is a polynomial algebra on \(r\) elements; its chosen central generators need not be homogeneous for the PBW filtration. These consequences require no additional polynomiality theorem.

The proof uses the finite-character and highest-weight results of Lesson 14, the reduced-root-sign criterion of Lesson 08, and the finite-variable Hilbert basis proof of Lesson 13, Lemma 3.2. For comparison, Etingof, *Representations of Lie Groups*, §10.2, Theorem 10.6, printed p. 57 (PDF p. 58), states the broader complex reflection-group theorem; §11.1, Lemma 11.1, printed p. 58 (PDF p. 59), gives the invariant finite-generation argument. All Weyl polynomiality and completion steps used here have been proved above.

For comparison, see Etingof, [*Representations of Lie Groups*, MIT OpenCourseWare (2023)](https://ocw.mit.edu/courses/18-757-representations-of-lie-groups-fall-2023/mit18_757_f23_lec_full.pdf), §10.1, Theorem 10.1, and §14.1, Theorem 14.1; Kirillov, [*Introduction to Lie Groups and Lie Algebras*, author-hosted notes](https://www.math.stonybrook.edu/~kirillov/liegroups/liegroups.pdf), §8.8, Theorems 8.50, 8.52 and 8.54; and Deligne and de Man, [*La série exceptionnelle de groupes de Lie II*, freely accessible IAS PDF](https://publications.ias.edu/sites/default/files/76_LaSerie.pdf), C. R. Acad. Sci. Paris Sér. I 323 (1996), pp. 578–579, formulas (1)–(4). The central eigenvalue description prepares the later lesson *Weyl's character formula and the multiplicity formulas*.
