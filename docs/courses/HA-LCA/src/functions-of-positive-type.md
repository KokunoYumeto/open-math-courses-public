# Functions of positive type

**Lesson HA-LCA-04.** Self-checked by the writing AI.

A positive-type function records all the inner products among translates of one vector. Conversely, positivity of those inner products constructs the vector and its representation. We will prove this both for continuous functions and for bounded measurable classes, then identify which normalized functions cannot be decomposed into two others.

Here \(G\) is an arbitrary locally compact Hausdorff group, not necessarily abelian or unimodular. We use the complete locally determined left Haar domain \((G,\Sigma,\mu)\) proved in [the general Haar reading](../prerequisites/src/nonabelian-haar-integration.md#ha-lca-pre-nonabelian-haar-theorem-3-1). Equality almost everywhere means equality on that domain; equivalently, its exceptional set is null on every compact set. There is no sigma-finiteness or separability assumption.

Our freely accessible source is B. Bekka, P. de la Harpe and A. Valette's [author draft dated 23 February 2007](https://perso.univ-rennes1.fr/bachir.bekka/KazhdanTotal.pdf): C.1.1–C.1.4, C.4.1–C.4.16, C.5.1–C.5.5, Exercises C.6.1, C.6.4, C.6.7 and C.6.10, and the integrated-representation discussion in F.4. Its external proof references are not used. In particular, the integral-class construction and representation correspondence are proved below from exact earlier programme results.

The freely sourced prerequisite components retain their stated licences. This lesson's new exposition is CC0; it reproduces no source prose or figures.

## 1. Representations and the convolution algebra

Inner products are linear in the first variable. A **unitary representation** is a homomorphism \(a\mapsto\pi(a)\) into the unitary operators on a Hilbert space \(\mathcal H\), such that \(a\mapsto\pi(a)v\) is norm-continuous for every \(v\). It is **cyclic** with vector \(\xi\) if the span of \(\{\pi(a)\xi:a\in G\}\) is dense. It is **irreducible** if \(\mathcal H\ne\{0\}\) and its only closed invariant subspaces are \(0,\mathcal H\).

The modular convention and algebra operations are
\[
 \mu(Ea)=\Delta(a)\mu(E),\qquad
 (f*g)(x)=\int_G f(y)g(y^{-1}x)\,d\mu(y),\qquad
 f^*(x)=\Delta(x)^{-1}\overline{f(x^{-1})}.              \tag{1}
\]
The full-domain substitutions, associativity, isometric involution and bound
\(\|f*g\|_1\le\|f\|_1\|g\|_1\) were proved in the earlier [modular theorem](../prerequisites/src/nonabelian-haar-integration.md#ha-lca-pre-nonabelian-haar-theorem-4-1) and [Banach-star algebra theorem](../prerequisites/src/nonabelian-haar-integration.md#ha-lca-pre-nonabelian-haar-theorem-6-1). Write \(L_af(x)=f(a^{-1}x)\).

We use the earlier [two-sided approximate identity](../prerequisites/src/nonabelian-haar-integration.md#ha-lca-pre-nonabelian-haar-corollary-6-2): nonnegative \(u_U\in C_c(G)\), indexed by shrinking symmetric neighbourhoods of \(e\), with
\[
 u_U=u_U^*,\quad \int u_U=1,\quad
 \operatorname{supp}u_U\subset U,\quad
 u_U*f\to f,\quad f*u_U\to f\quad\hbox{in }L^1.          \tag{2}
\]

<a id="ha-lca-04-proposition-1-1"></a>
### Proposition 1.1. Hilbert-space structure of unitary representations

Every unitary representation is an orthogonal Hilbert sum of cyclic representations. For a nonzero representation, irreducibility is equivalent to its bounded commutant being exactly \(\mathbb C I\). In the abelian case every irreducible unitary representation is one-dimensional and is given by a continuous character \(G\to\mathbb T\).

**Proof.** These statements have complete earlier proofs in [the cyclic-decomposition proposition](../prerequisites/src/hilbert-spaces-and-unitary-representations.md#ha-lca-pre-hilbert-proposition-7-1) and [the Schur theorem](../prerequisites/src/hilbert-spaces-and-unitary-representations.md#ha-lca-pre-hilbert-theorem-7-2). Their hypotheses are exactly the strong continuity and arbitrary Hilbert dimension used here. To specify the mechanisms, an invariant closed subspace has invariant orthogonal complement, since all \(\pi(a)^{-1}\) also belong to the representation. A maximal orthogonal family of cyclic subspaces exhausts the space; otherwise any nonzero vector in its orthogonal complement supplies a further member. The Hilbert sum and maximal-family argument are proved in the cited proposition. For Schur's theorem, the cited proof constructs nontrivial invariant closed ranges from a nonscalar self-adjoint operator by its continuous positive and negative parts, using the fully proved [continuous calculus and square-root results](../prerequisites/src/hilbert-spaces-and-unitary-representations.md#ha-lca-pre-hilbert-theorem-3-2). It uses no unproved spectral decomposition. Finally, if \(G\) is abelian, each \(\pi(a)\) belongs to the commutant and hence is scalar; every subspace is then invariant, forcing dimension one. Strong continuity makes the resulting scalar homomorphism continuous. \(\square\)

<a id="ha-lca-04-lemma-1-2"></a>
### Lemma 1.2. The full \(L^1\) representation correspondence

For a unitary representation \(\pi\), the operators determined by
\[
 \langle\pi(f)v,w\rangle=\int_G f(a)\langle\pi(a)v,w\rangle\,d\mu(a) \tag{3}
\]
form a contractive nondegenerate star representation of \(L^1(G)\). Conversely, every nondegenerate algebraic star homomorphism
\(\rho:L^1(G)\to\mathcal B(\mathcal H)\) arises in this way from a unique strongly continuous unitary representation. Here nondegenerate means that the span of \(\rho(L^1)\mathcal H\) is dense, and an algebraic star homomorphism is complex linear and preserves products and adjoints. Its contractivity need not be assumed.

The forward correspondence preserves commutants and the closed cyclic spans of individual vectors.

**Proof.** The complete [integrated-representation theorem](../prerequisites/src/nonabelian-haar-integration.md#ha-lca-pre-nonabelian-haar-theorem-7-2) proves all the forward assertions, including construction of (3) by bounded forms, the star identity with the modular convention (1), nondegeneracy, commutants and cyclic spans.

We supply the converse. First \(\rho\) is contractive. Use the earlier [unitization](../prerequisites/src/banach-spectrum.md#ha-lca-pre-banach-theorem-3-4) \(A^+=L^1(G)\oplus\mathbb C1\), with norm \(\|f+z1\|=\|f\|_1+|z|\), and extend \(\rho\) algebraically to the unital map
\(\rho^+(f+z1)=\rho(f)+zI\). Unital algebra homomorphisms preserve inverses, so
\(\sigma_{\mathcal B(\mathcal H)}(\rho^+(b))\subseteq\sigma_{A^+}(b)\): if \(b-z1\) has inverse \(c\), then \(\rho^+(c)\) is the inverse of \(\rho^+(b)-zI\). For \(\mathcal H\ne0\), the earlier [operator norm and self-adjoint radius theorem](../prerequisites/src/hilbert-spaces-and-unitary-representations.md#ha-lca-pre-hilbert-proposition-3-1) and [Banach spectral bound](../prerequisites/src/banach-spectrum.md#ha-lca-pre-banach-theorem-2-2) imply
\[
 \|\rho(f)\|^2
 =r\big(\rho(f)^*\rho(f)\big)
 =r\big(\rho^+(f^**f)\big)
 \le r_{A^+}(f^**f)\le\|f^**f\|_1\le\|f\|_1^2.         \tag{4}
\]
For the zero Hilbert space contractivity and the claimed correspondence are immediate. Thus we may assume \(\mathcal H\ne0\).

For \(f,g\in L^1\) and \(a\in G\),
\[
 (L_ag)^**(L_af)=g^**f.                                \tag{5}
\]
For \(C_c\) functions, \((L_ag)^*(y)=\Delta(a)g^*(ya)\). Substitute \(t=ya\) into its convolution with \(L_af\); the measure multiplier is \(\Delta(a)^{-1}\), and \(a^{-1}y^{-1}x=t^{-1}x\). The factors cancel, proving (5). The \(C_c\) density, translation continuity and bounded algebra operations proved in [the general Haar reading](../prerequisites/src/nonabelian-haar-integration.md#ha-lca-pre-nonabelian-haar-proposition-5-2) extend this identity to \(L^1\).

On the dense linear subspace \(D=\operatorname{span}\rho(L^1)\mathcal H\), define
\[
 U_a\left(\sum_{j=1}^n\rho(f_j)v_j\right)
       =\sum_{j=1}^n\rho(L_af_j)v_j.                    \tag{6}
\]
Its squared norm is
\[
 \sum_{i,j}\left\langle
   \rho\big((L_af_j)^**(L_af_i)\big)v_i,v_j\right\rangle
 =\sum_{i,j}\langle\rho(f_j^**f_i)v_i,v_j\rangle
 =\left\|\sum_i\rho(f_i)v_i\right\|^2.
\]
This proves that the value of (6) is independent of the chosen expression, and that it is an isometry. The maps \(U_{a^{-1}}\) and \(U_a\) are inverse on \(D\), so the earlier [extension theorem](../prerequisites/src/hilbert-spaces-and-unitary-representations.md#ha-lca-pre-hilbert-theorem-1-2) extends them to mutually inverse unitaries. The identities \(L_aL_b=L_{ab}\) give \(U_aU_b=U_{ab}\). By (4) and \(L^1\) translation continuity, \(U_a v\to v\) as \(a\to e\) for \(v\in D\). Approximating any vector by a vector in \(D\), and using \(\|U_a\|=1\), extends continuity to all vectors. The group law then gives continuity at every \(a\).

It remains to verify that integration of \(U\) returns \(\rho\). We will use the following scalar consequence of the earlier [full-domain convolution pairing](../prerequisites/src/nonabelian-haar-integration.md#ha-lca-pre-nonabelian-haar-theorem-6-1). For any bounded functional \(\ell\) on \(L^1\),
\[
 \int_G g(a)\ell(L_af)\,d\mu(a)=\ell(g*f).               \tag{7}
\]
Indeed, the proved [\(L^1\) dual representation](../prerequisites/src/dual-balls-and-compact-convexity.md#ha-lca-pre-dual-convex-theorem-1-2) writes \(\ell(h)=\int hq\), with \(q\in L^\infty\). Left substitution gives
\(\ell(L_af)=\int f(b)q(ab)\,d\mu(b)\). The cited convolution pairing gives (7); its absolute bound is \(\|q\|_\infty\|g\|_1\|f\|_1\), and its proof includes the full measurable domain.

For \(v,w\in\mathcal H\), take \(\ell(h)=\langle\rho(h)v,w\rangle\), bounded by (4). Formula (6), then (7), shows
\[
 \left\langle U(g)\rho(f)v,w\right\rangle
 =\int g(a)\langle\rho(L_af)v,w\rangle\,d\mu(a)
 =\langle\rho(g*f)v,w\rangle
 =\langle\rho(g)\rho(f)v,w\rangle.
\]
Thus \(U(g)=\rho(g)\) on \(D\) and hence on \(\mathcal H\). Finally, any unitary representation integrating to \(\rho\) satisfies
\(U_a\rho(f)=\rho(L_af)\) by the covariance assertion in the forward theorem. This determines it on the dense subspace \(D\), proving uniqueness. \(\square\)

## 2. Two forms of positivity

A function \(\varphi:G\to\mathbb C\) is **matrix positive** if
\[
 \sum_{i,j=1}^n c_i\overline{c_j}\,
                \varphi(x_j^{-1}x_i)\ \ge0             \tag{8}
\]
for every finite family \(x_i\in G,\ c_i\in\mathbb C\). The inequality asserts that the sum is real and nonnegative. A class \(q\in L^\infty(G)\) is **integral positive** if
\(\int(f^**f)q\,d\mu\ge0\) for every \(f\in L^1(G)\).

<a id="ha-lca-04-lemma-2-0"></a>
### Lemma 2.0. The continuous kernel construction

Every continuous matrix-positive function has a cyclic unitary realization
\(\varphi(a)=\langle\pi(a)\xi,\xi\rangle\). It satisfies
\(\varphi(e)=\|\xi\|^2\), \(|\varphi(a)|\le\varphi(e)\), and
\(\varphi(a^{-1})=\overline{\varphi(a)}\). The realization is unique up to the unique unitary that carries the cyclic vector to the cyclic vector and intertwines the representations.

**Proof.** Let \(V\) be the vector space of finite formal sums \(\sum_i c_i\delta_{x_i}\), and define
\[
 B\left(\sum_i c_i\delta_{x_i},\sum_j d_j\delta_{y_j}\right)
    =\sum_{i,j}c_i\overline{d_j}\varphi(y_j^{-1}x_i).
\]
This is well-defined on finite-support functions by combining repeated indices. It is sesquilinear and nonnegative on the diagonal by (8). The earlier [positive-form lemma](../prerequisites/src/hilbert-spaces-and-unitary-representations.md#ha-lca-pre-hilbert-lemma-1-1) proves its Hermitian symmetry, Cauchy–Schwarz inequality, and the fact that its zero-length vectors form a subspace orthogonal to all of \(V\). Quotient by that subspace and take the [Hilbert completion](../prerequisites/src/hilbert-spaces-and-unitary-representations.md#ha-lca-pre-hilbert-theorem-1-2).

The maps \(\delta_x\mapsto\delta_{ax}\) preserve \(B\), since \((ay)^{-1}(ax)=y^{-1}x\), and have inverses with \(a^{-1}\). They descend and extend to unitaries \(\pi(a)\), with the group law. Put \(\xi=[\delta_e]\). Its translates are all the \([\delta_x]\), so it is cyclic, and
\(\langle\pi(a)\xi,\xi\rangle=\varphi(a)\). Unitarity and Cauchy–Schwarz give the stated bound and Hermitian symmetry.

For any \(x\in G\),
\[
 \|\pi(a)[\delta_x]-[\delta_x]\|^2
       =2\varphi(e)-2\operatorname{Re}\varphi(x^{-1}ax)\longrightarrow0
                      \quad(a\to e),
\]
by continuity of \(\varphi\). Finite linear combinations have the same continuity, and approximation with the common unitary bound extends it to the entire completion. Thus \(\pi\) is strongly continuous.

If \((\rho,\mathcal K,\eta)\) is another cyclic realization, then
\(\langle\rho(x)\eta,\rho(y)\eta\rangle=\varphi(y^{-1}x)\).
Consequently \(\sum c_i\pi(x_i)\xi\mapsto\sum c_i\rho(x_i)\eta\) preserves squared norms and inner products. It is well-defined, extends to an isometry and is onto because its image contains a dense cyclic span and the range of an isometry from a complete space is closed. On the dense span it intertwines each group operator and sends \(\xi\) to \(\eta\), so it does so everywhere. These same prescribed values force uniqueness. If \(\varphi=0\), both cyclic spaces are the zero space and the argument still applies. \(\square\)

<a id="ha-lca-04-lemma-2-1"></a>
### Lemma 2.1. Integral pairing and continuous positivity

For \(q\in L^\infty\), put \(\Lambda_q(h)=\int hq\). Then, for \(f,g\in L^1\),
\[
 \Lambda_q(g^**f)
   =\int_G\int_G f(x)\overline{g(y)}q(y^{-1}x)\,d\mu(x)d\mu(y). \tag{9}
\]
The double integral is well-defined on classes, is absolutely convergent, and has absolute value at most \(\|q\|_\infty\|f\|_1\|g\|_1\).

A bounded continuous function is integral positive if and only if it is matrix positive. Matrix positivity itself forces a continuous function to be bounded.

**Proof.** The earlier [convolution pairing theorem](../prerequisites/src/nonabelian-haar-integration.md#ha-lca-pre-nonabelian-haar-theorem-6-1) gives
\[
 \Lambda_q(g^**f)=\iint g^*(t)f(x)q(tx)\,d\mu(t)d\mu(x).
\]
Set \(t=y^{-1}\). The [inversion substitution](../prerequisites/src/nonabelian-haar-integration.md#ha-lca-pre-nonabelian-haar-theorem-4-1) multiplies \(d\mu(y)\) by \(\Delta(y)^{-1}\), while
\(g^*(y^{-1})=\Delta(y)\overline{g(y)}\). Their cancellation gives (9).
For full precision on the domain, choose Borel representatives of \(f,g\) supported in a common open sigma-compact subgroup, as proved in [the localization lemma](../prerequisites/src/nonabelian-haar-integration.md#ha-lca-pre-nonabelian-haar-lemma-5-1). On this subgroup \(q\) has a Borel representative off a Borel null envelope. The same lemma proves that the inverse-product map \((y,x)\mapsto y^{-1}x\) pulls such an envelope back to a product-null set. The earlier full-Borel Fubini theorem therefore applies; the absolute majorant is \(\|q\|_\infty|f(x)||g(y)|\). This also proves independence from every choice of representative.

If \(\varphi\) is continuous and matrix positive, Lemma 2.0 bounds it and constructs \((\pi,\xi)\). Equation (3) and the star identity give
\[
 \Lambda_\varphi(f^**f)
 =\langle\pi(f)^*\pi(f)\xi,\xi\rangle
 =\|\pi(f)\xi\|^2\ge0.
\]
Conversely suppose \(\varphi\) is bounded, continuous and integral positive. For the finite data of (8), put \(f_U=\sum_i c_iL_{x_i}u_U\). Formula (9), followed by the left substitutions \(x=x_i a,\ y=x_j b\), gives
\[
 0\le\Lambda_\varphi(f_U^**f_U)
 =\sum_{i,j}c_i\overline{c_j}
     \iint u_U(a)u_U(b)\varphi(b^{-1}x_j^{-1}x_i a)\,d\mu(a)d\mu(b).
\]
For each of the finitely many pairs \(i,j\), continuity at \((a,b)=(e,e)\) makes the last function uniformly within any prescribed error of
\(\varphi(x_j^{-1}x_i)\) when both \(a,b\) lie in a sufficiently small neighbourhood. The nonnegative product weights have total mass one and are supported there for small \(U\). Therefore the displayed sum tends to the sum in (8), which must be real and nonnegative. \(\square\)

<a id="ha-lca-04-proposition-2-2"></a>
### Proposition 2.2. Coefficients and \(L^2\) autocorrelations

Every diagonal coefficient \(a\mapsto\langle\pi(a)v,v\rangle\) of a unitary representation is continuous and matrix positive. For \(f\in L^2(G)\), put \(\widetilde f(x)=\overline{f(x^{-1})}\). Then the pointwise absolutely convergent integral
\[
 (f*\widetilde f)(a)=\int_G f(y)\overline{f(a^{-1}y)}\,d\mu(y) \tag{10}
\]
is continuous, positive type, vanishes at infinity, and has value \(\|f\|_2^2\) at \(e\).

**Proof.** Strong continuity gives continuity of a coefficient. The sum in (8) is
\(\|\sum_i c_i\pi(x_i)v\|^2\), by unitarity, and is nonnegative.

Let \(\lambda(a)h(y)=h(a^{-1}y)\) be the strongly continuous left regular representation, proved in [the regular-representation proposition](../prerequisites/src/nonabelian-haar-integration.md#ha-lca-pre-nonabelian-haar-proposition-7-1). Cauchy–Schwarz makes (10) absolutely convergent for every \(a\), bounded by \(\|f\|_2^2\), and identifies it as
\[
 (f*\widetilde f)(a)
       =\langle\lambda(a)\overline f,\overline f\rangle.  \tag{11}
\]
The conjugated vector in this formula fixes the linear-first inner-product convention. Thus continuity, positivity and the value at \(e\) follow.

Choose \(f_n\in C_c(G)\) with \(f_n\to f\) in \(L^2\), using the proved [density theorem](../prerequisites/src/nonabelian-haar-integration.md#ha-lca-pre-nonabelian-haar-lemma-5-1). The coefficient difference in (11) is bounded uniformly in \(a\) by
\[
 \|f_n-f\|_2(\|f_n\|_2+\|f\|_2).
\]
For \(f_n\) its support is contained in the compact set
\(\operatorname{supp}f_n(\operatorname{supp}f_n)^{-1}\), and it is continuous by (11). Thus these approximants lie in \(C_c(G)\). Their uniform limit belongs to \(C_0(G)\) by the earlier [uniform completeness result](../prerequisites/src/finite-radon-representation.md#ha-lca-pre-radon-lemma-1-5), proving the last assertion. \(\square\)

## 3. The GNS construction for a measurable class

<a id="ha-lca-04-theorem-3-1"></a>
### Theorem 3.1. Integral-positive GNS

Let \(q\in L^\infty(G)\) be integral positive. There is a cyclic strongly continuous unitary representation \((\pi_q,\mathcal H_q,\xi_q)\) such that
\[
 q(a)=\langle\pi_q(a)\xi_q,\xi_q\rangle
                         \quad\hbox{almost everywhere}. \tag{12}
\]
It is unique in the cyclic-vector-preserving intertwining sense of Lemma 2.0.

**Proof.** Write \(\Lambda=\Lambda_q\), \(M=\|q\|_\infty\), and define on \(L^1\)
\[
 B(f,g)=\Lambda(g^**f).
\]
It is a positive sesquilinear form by the hypothesis. By the earlier [positive-form and completion theorems](../prerequisites/src/hilbert-spaces-and-unitary-representations.md#ha-lca-pre-hilbert-lemma-1-1), its null quotient completes to a Hilbert space \(\mathcal H\); denote the dense quotient vectors by \([f]\). The algebra norm bound gives
\[
 \|[f]\|^2=B(f,f)\le M\|f\|_1^2.                       \tag{13}
\]

Formula (9) and left substitution in both variables show
\(B(L_af,L_ag)=B(f,g)\). Hence \([f]\mapsto[L_af]\) defines isometries with inverses on the quotient, extending to unitaries \(\pi(a)\) on the completion. The identities for translations give the group law. By (13) and [\(L^1\) translation continuity](../prerequisites/src/nonabelian-haar-integration.md#ha-lca-pre-nonabelian-haar-proposition-5-2),
\[
 \|\pi(a)[f]-[f]\|\le\sqrt M\,\|L_af-f\|_1\longrightarrow0.
\]
Density and the unitary norm bound extend this to all vectors, proving strong continuity.

We next construct the cyclic vector, rather than assuming a unit for \(L^1\). From (2),
\[
 \langle[f],[u_U]\rangle=\Lambda(u_U*f)\longrightarrow\Lambda(f),
 \qquad \|[u_U]\|^2\le M.
\]
Cauchy–Schwarz and passage to the limit give
\[
 |\Lambda(f)|\le\sqrt M\,\|[f]\|.                        \tag{14}
\]
Thus \([f]\mapsto\Lambda(f)\) is well-defined, linear and bounded, and extends to the completion. The earlier [Hilbert representation theorem](../prerequisites/src/hilbert-spaces-and-unitary-representations.md#ha-lca-pre-hilbert-theorem-2-3) gives a unique \(\xi\in\mathcal H\) with
\[
 \Lambda(f)=\langle[f],\xi\rangle,\qquad \|\xi\|\le\sqrt M. \tag{15}
\]
The same displayed limit shows \([u_U]\to\xi\) weakly. Indeed, it gives all inner products against the dense quotient subspace; for any other test vector, its norm distance to that subspace, multiplied by the common bound \(\sqrt M+\|\xi\|\), controls the error.

Integrate the already constructed \(\pi\) as in (3). We claim that
\[
 \pi(h)[g]=[h*g]\qquad(h,g\in L^1).                     \tag{16}
\]
For a quotient test vector \([k]\), the left side paired with \([k]\) is
\(\int h(a)B(L_ag,k)\,d\mu(a)\). Formula (9) and the substitution \(x=ay\) turn this into
\[
 \iiint h(a)g(y)\overline{k(z)}q(z^{-1}ay)\,
                          d\mu(a)d\mu(y)d\mu(z).
\]
Expanding \(B(h*g,k)\) by (9) and then the convolution formula yields exactly the same integral. Here all three \(L^1\) functions have Borel representatives supported in one open sigma-compact subgroup by the earlier localization lemma. On that subgroup replace \(q\) by a bounded Borel representative off a Borel null envelope \(N\). For fixed \(y,z\), the set of \(a\) for which \(z^{-1}ay\in N\) is \(zNy^{-1}\), which is Haar null by the proved left and right null-set invariance. The full-Borel Tonelli theorem, applied successively on the subgroup, shows that this change affects a product-null set only. The absolute integral is at most
\(M\|h\|_1\|g\|_1\|k\|_1\).
Thus every exchange and substitution above is justified. Equality of pairings with the dense quotient subspace proves (16).

For fixed \(f\), (16) and (2) give
\[
 \pi(f)[u_U]=[f*u_U]\longrightarrow[f]\quad\hbox{in norm},
\]
using (13). On the other hand bounded operators preserve weak convergence: pairing \(\pi(f)[u_U]\) with \(v\) is pairing \([u_U]\) with \(\pi(f)^*v\). Hence the same net converges weakly to \(\pi(f)\xi\). Norm convergence implies weak convergence by Cauchy–Schwarz, and equality of all inner products makes weak limits unique. Therefore
\[
                    \pi(f)\xi=[f].                    \tag{17}
\]
The vectors on the right are dense. The equality of group and integrated cyclic spans in the earlier [integrated-representation theorem](../prerequisites/src/nonabelian-haar-integration.md#ha-lca-pre-nonabelian-haar-theorem-7-2) therefore proves that \(\xi\) is cyclic for \(\pi\).

Set \(\varphi(a)=\langle\pi(a)\xi,\xi\rangle\). It is bounded, continuous and matrix positive by Proposition 2.2. Equations (3), (15) and (17) give
\[
 \int f\varphi\,d\mu=\langle\pi(f)\xi,\xi\rangle
                   =\Lambda(f)=\int fq\,d\mu
                         \quad(f\in L^1).
\]
Uniqueness in the earlier [\(L^1\) dual theorem](../prerequisites/src/dual-balls-and-compact-convexity.md#ha-lca-pre-dual-convex-theorem-1-2) gives \(\varphi=q\) as \(L^\infty\) classes, proving (12).

Two continuous functions agreeing almost everywhere are identical by the earlier [continuous-representative lemma](../prerequisites/src/dual-balls-and-compact-convexity.md#ha-lca-pre-dual-convex-corollary-1-3). Therefore any two cyclic realizations of the class have exactly the same continuous coefficient; Lemma 2.0 supplies their unique prescribed unitary equivalence. When \(M=0\), (13) makes the quotient and its completion zero, and the argument yields the zero realization. \(\square\)

<a id="ha-lca-04-corollary-3-2"></a>
### Corollary 3.2. The canonical continuous representative

Every integral-positive class has exactly one continuous representative \(\varphi\), and that representative is matrix positive. Conversely, every continuous matrix-positive function defines an integral-positive class. For this representative,
\[
 \|\varphi\|_{\mathrm{ess}\,\infty}
 =\|\varphi\|_\infty=\varphi(e)=\|\xi_\varphi\|^2,\qquad
 \varphi(a^{-1})=\overline{\varphi(a)}.                  \tag{18}
\]
In particular \(\varphi(e)=0\) implies \(\varphi=0\).

**Proof.** Theorem 3.1 gives existence and Lemma 2.1 gives the converse. The full-support continuous-representative lemma gives uniqueness and equality of essential and uniform norms. Lemma 2.0 gives \(|\varphi(a)|\le\varphi(e)=\|\xi_\varphi\|^2\), with equality of the bound attained at \(e\), and also gives the Hermitian identity. These prove every equality in (18) and its zero case. \(\square\)

We now call either the class or its canonical representative a **function of positive type**, explicitly using the continuous representative whenever a point value is taken.

<a id="ha-lca-04-lemma-3-3"></a>
### Lemma 3.3. Both difference inequalities

Let \(\varphi\) be of positive type and \(c=\varphi(e)\). For \(x,y\in G\),
\[
 \begin{split}
 |\varphi(x)-\varphi(y)|^2
    &\le2c\big(c-\operatorname{Re}\varphi(y^{-1}x)\big),\\
 |\varphi(x)-\varphi(y)|^2
    &\le2c\big(c-\operatorname{Re}\varphi(yx^{-1})\big).
 \end{split}                                           \tag{19}
\]
Consequently \(\varphi\) is uniformly continuous under both left and right translation.

**Proof.** In the GNS realization, Cauchy–Schwarz gives
\[
 |\langle(\pi(x)-\pi(y))\xi,\xi\rangle|^2
 \le c\,\|(\pi(x)-\pi(y))\xi\|^2
 =2c\big(c-\operatorname{Re}\varphi(y^{-1}x)\big).
\]
Also \(\varphi(x)=\langle\xi,\pi(x^{-1})\xi\rangle\). Apply Cauchy–Schwarz to the difference of these expressions; the squared vector difference is
\(2c-2\operatorname{Re}\varphi(yx^{-1})\), giving the second inequality. No factors have been interchanged.

Set \(y=xa\) in the first inequality. Its right side tends to zero as \(a\to e\), independently of \(x\). Set \(y=ax\) in the second for the analogous left-translation assertion. Hermitian symmetry makes the real part at \(a^{-1}\) equal to that at \(a\). If \(c=0\), the function is zero and all assertions still hold. \(\square\)

## 4. Convexity and irreducibility

Let \(P(G)\) be the cone of positive-type functions, and put
\[
 P_1(G)=\{\varphi\in P(G):\varphi(e)=1\},\qquad
 P_0(G)=\{\varphi\in P(G):\varphi(e)\le1\}.              \tag{20}
\]
Nonnegative sums preserve each matrix inequality, so these are convex where applicable. Their weak-star topology is the topology of the pairings
\(\varphi\mapsto\int f\varphi\), \(f\in L^1(G)\), under the proved identification \(L^\infty=(L^1)^*\). A point of a convex set is extreme when it has no expression as a strict convex combination of two different points of that set.

<a id="ha-lca-04-theorem-4-1"></a>
### Theorem 4.1. Extreme normalized functions

A function \(\varphi\in P_1(G)\) is extreme in \(P_1(G)\) if and only if its cyclic GNS representation is irreducible.

**Proof.** We first construct the operator associated to a positive summand. Suppose \(\psi\in P(G)\) and \(\varphi-\psi\in P(G)\). On the dense cyclic span
\[
 D_\varphi=\operatorname{span}\{\pi_\varphi(x)\xi_\varphi:x\in G\}
\]
define the candidate form
\[
 B_\psi\left(\sum_i c_i\pi_\varphi(x_i)\xi_\varphi,
             \sum_j d_j\pi_\varphi(y_j)\xi_\varphi\right)
        =\sum_{i,j}c_i\overline{d_j}\psi(y_j^{-1}x_i).   \tag{21}
\]
Initially view it as a form on formal sums. Matrix positivity of \(\psi\) and of \(\varphi-\psi\) gives
\[
 0\le B_\psi(v,v)\le\|v\|^2.
\]
If a formal sum represents the zero vector in \(D_\varphi\), its \(B_\psi\) length is zero; the positive-form Cauchy–Schwarz inequality makes its pairing with every formal sum zero. Thus (21) is well-defined on \(D_\varphi\), and
\(|B_\psi(v,w)|\le\|v\|\|w\|\). It extends continuously to all pairs of vectors in \(\mathcal H_\varphi\). The earlier [bounded-form theorem](../prerequisites/src/hilbert-spaces-and-unitary-representations.md#ha-lca-pre-hilbert-proposition-2-4) supplies a bounded positive operator \(T\) with \(0\le T\le I\) and
\[
 B_\psi(v,w)=\langle Tv,w\rangle.
\]
Replacing all \(x_i,y_j\) in (21) by \(ax_i,ay_j\) leaves it unchanged. By density this gives
\(\pi_\varphi(a)^*T\pi_\varphi(a)=T\), so \(T\) belongs to the commutant. Taking \(v=\pi_\varphi(a)\xi_\varphi,\ w=\xi_\varphi\) gives
\[
 \psi(a)=\langle T\pi_\varphi(a)\xi_\varphi,\xi_\varphi\rangle. \tag{22}
\]

If \(\pi_\varphi\) is irreducible, Proposition 1.1 gives \(T=sI\), with \(0\le s\le1\). Thus every such summand \(\psi\) equals \(s\varphi\). In a strict convex decomposition
\(\varphi=t\varphi_1+(1-t)\varphi_2\), with \(\varphi_i\in P_1\) and \(0<t<1\), apply this to \(\psi=t\varphi_1\). Evaluation at \(e\) gives \(s=t\), so \(\varphi_1=\varphi\), and then \(\varphi_2=\varphi\). Hence \(\varphi\) is extreme.

Conversely, if \(\pi_\varphi\) is reducible, let \(W\) be a nonzero proper closed invariant subspace and \(P\) its orthogonal projection. The orthogonal-complement and projection results in [the Hilbert reading](../prerequisites/src/hilbert-spaces-and-unitary-representations.md#ha-lca-pre-hilbert-corollary-2-2) show that both \(W,W^\perp\) are invariant and \(P\) commutes with every \(\pi_\varphi(a)\). Write \(\xi_\varphi=v+w\), where \(v=P\xi_\varphi\), \(w=(I-P)\xi_\varphi\). Both vectors are nonzero: if one vanished, the cyclic span would lie in the other proper subspace. Set \(s=\|v\|^2\); then \(0<s<1\) and \(\|w\|^2=1-s\). The functions
\[
 \varphi_1(a)=s^{-1}\langle\pi_\varphi(a)v,v\rangle,\qquad
 \varphi_2(a)=(1-s)^{-1}\langle\pi_\varphi(a)w,w\rangle
\]
belong to \(P_1\) by Proposition 2.2, and orthogonality gives
\(\varphi=s\varphi_1+(1-s)\varphi_2\).

This decomposition is nontrivial. If \(\varphi_1=\varphi\), then for every \(a\),
\[
 \langle\pi_\varphi(a)\xi_\varphi,v\rangle
 =\langle\pi_\varphi(a)v,v\rangle
 =s\langle\pi_\varphi(a)\xi_\varphi,\xi_\varphi\rangle.
\]
Density of the cyclic span implies \(v=s\xi_\varphi\). Applying \(P\) gives \(v=sv\), contrary to \(v\ne0\) and \(s<1\). Thus \(\varphi_1\ne\varphi\); the displayed strict convex decomposition disproves extremality. \(\square\)

<a id="ha-lca-04-lemma-4-2"></a>
### Lemma 4.2. The compact-convex theorem used here

Every nonempty weak-star compact convex subset \(K\) of \((L^1(G))^*\) has extreme points and is their weak-star closed convex hull. If \(K\subseteq B_1\), \(0\in K\), and its nonzero extreme points all have norm one, then every norm-one member of \(K\) is a weak-star limit of convex combinations of those nonzero extreme points.

The set \(P_1(G)\) need not itself be weak-star closed or compact.

**Proof.** The first two assertions are the exact conclusions of the earlier [compact-face theorem and extreme-point theorem](../prerequisites/src/dual-balls-and-compact-convexity.md#ha-lca-pre-dual-convex-lemma-3-1), whose complete proof continues in [Theorem 3.2](../prerequisites/src/dual-balls-and-compact-convexity.md#ha-lca-pre-dual-convex-theorem-3-2). The normalized assertion is [Corollary 3.3](../prerequisites/src/dual-balls-and-compact-convexity.md#ha-lca-pre-dual-convex-corollary-3-3). Its proof divides finite extreme combinations by their total nonzero mass; weak-star lower semicontinuity of the norm proves that this mass tends to one. These proofs apply to arbitrary nets and require no separability.

For the final assertion take \(G=\mathbb T\). Its characters \(\varphi_n(z)=z^n\), \(n\ge1\), belong to \(P_1\), as coefficients of one-dimensional unitary representations. The earlier [circle dual calculation](characters-and-the-dual-group.md#ha-lca-02-corollary-3-2) identifies the dual with the discrete group \(\mathbb Z\). The earlier [Fourier \(C_0\) theorem](the-dual-group-as-the-gelfand-spectrum-of-l1.md#ha-lca-03-corollary-2-2) says that, for every \(f\in L^1(\mathbb T)\), its Fourier transform vanishes at infinity on this dual. Compact subsets of a discrete space are finite, since the singleton open cover has a finite subcover precisely for finite sets. Thus
\[
 \int_{\mathbb T} f(z)z^n\,d\mu(z)
      =\widehat f(\varphi_{-n})\longrightarrow0.
\]
Hence \(\varphi_n\to0\) weak-star, while \(0\notin P_1\). This shows that \(P_1\) is not always closed. A compact subset of the Hausdorff weak-star dual is closed, so it is not always compact either. \(\square\)

<a id="ha-lca-04-theorem-4-3"></a>
### Theorem 4.3. The compact positive ball and its boundary

The set \(P_0(G)\) is weak-star compact and convex, and
\[
 \operatorname{Ext}P_0(G)=\operatorname{Ext}P_1(G)\cup\{0\}. \tag{23}
\]
Every point of \(P_1(G)\) is a weak-star limit of finite convex combinations of points of \(\operatorname{Ext}P_1(G)\).

**Proof.** By Theorem 3.1, Lemma 2.1 and Corollary 3.2, the set of classes represented by \(P_0\) is exactly
\[
 \{q\in L^\infty:\|q\|_\infty\le1,\ 
                         \Lambda_q(f^**f)\in[0,\infty)\ \text{for every }f\in L^1\}.
                                                               \tag{24}
\]
For each \(f\), the map \(q\mapsto\Lambda_q(f^**f)\) is a weak-star continuous evaluation, since \(f^**f\in L^1\). The real half-line \([0,\infty)\) is a closed subset of \(\mathbb C\). Therefore (24) is closed in the weak-star compact dual ball proved in [the dual-ball theorem](../prerequisites/src/dual-balls-and-compact-convexity.md#ha-lca-pre-dual-convex-theorem-2-1), and is compact. Convexity follows either from (24) or from addition of the matrix inequalities.

If \(0=t\varphi+(1-t)\psi\) with \(0<t<1\) and \(\varphi,\psi\in P_0\), equality of classes is equality of the continuous representatives. Evaluation at \(e\) is a sum of nonnegative terms and forces \(\varphi(e)=\psi(e)=0\), whence \(\varphi=\psi=0\) by Corollary 3.2. Thus zero is extreme.

If \(\varphi\in\operatorname{Ext}P_1\) and \(\varphi=t\psi+(1-t)\eta\) is a strict convex decomposition in \(P_0\), then
\[
 1=t\psi(e)+(1-t)\eta(e),\qquad 0\le\psi(e),\eta(e)\le1.
\]
Both values must equal one. The decomposition therefore lies in \(P_1\), where extremality forces \(\psi=\eta=\varphi\). This proves
\(\operatorname{Ext}P_1\subseteq\operatorname{Ext}P_0\).

For a nonzero \(\varphi\in P_0\) with \(a=\varphi(e)<1\), the number \(a\) is positive, \(\varphi/a\in P_1\), and
\[
 \varphi=a(\varphi/a)+(1-a)0
\]
is a nontrivial strict convex decomposition in \(P_0\). Hence any nonzero extreme point of \(P_0\) belongs to \(P_1\). It must be extreme there, since any decomposition in \(P_1\) is also one in \(P_0\). This proves (23).

By (18), every nonzero extreme point of \(P_0\) has norm one. Apply the normalized conclusion of Lemma 4.2 to the compact convex set \(K=P_0\). Its norm-one members are precisely \(P_1\), and its nonzero extreme points are precisely \(\operatorname{Ext}P_1\). This gives the asserted density. The argument takes compactness in \(P_0\) before normalization. \(\square\)

## 5. Abelian groups

<a id="ha-lca-04-corollary-5-1"></a>
### Corollary 5.1. The extreme points are the characters

If \(G\) is abelian, then
\[
 \operatorname{Ext}P_1(G)=\widehat G,\qquad
 \operatorname{Ext}P_0(G)=\widehat G\cup\{0\}.           \tag{25}
\]
Every normalized positive-type function is consequently a weak-star limit of finite convex combinations of characters.

**Proof.** Theorem 4.1 identifies extreme normalized functions with coefficients of their irreducible cyclic representations. By Proposition 1.1 those representations are one-dimensional, with
\(\pi(a)z=\chi(a)z\) for a continuous character \(\chi\). Their cyclic vectors have norm one, so the coefficient is exactly \(\chi(a)\). Conversely a one-dimensional character representation is irreducible because its only vector subspaces are \(0\) and \(\mathbb C\), and its unit vector is cyclic. Theorem 4.1 makes its coefficient extreme. Equation (23) gives the second equality in (25), and Theorem 4.3 gives the final approximation assertion. \(\square\)

## 6. Examples

<a id="ha-lca-04-example-6-1"></a>
### Example 6.1. Four functions on the real line

For \(a\in\mathbb R\), all of
\[
 e^{-|x|},\qquad e^{-x^2},\qquad \cos(ax),\qquad
                      (1-|x|)_+
\]
belong to \(P_1(\mathbb R)\).

**Proof.** Use the earlier [Lebesgue normalization of Haar measure on \(\mathbb R\)](characters-and-the-dual-group.md#ha-lca-02-lemma-3-3). Let
\(u(t)=\sqrt2\,e^{-t}1_{[0,\infty)}(t)\).
The [elementary exponential integral and substitution rules](../prerequisites/src/real-variable-calculations.md#ha-lca-pre-real-lemma-1-3), followed by monotone convergence over bounded intervals, give \(\|u\|_2^2=2\int_0^\infty e^{-2t}\,dt=1\). For every real \(x\),
\[
 (u*\widetilde u)(x)
   =2e^x\int_{\max(0,x)}^\infty e^{-2t}\,dt
   =e^{x-2\max(0,x)}=e^{-|x|}.
\]
Thus Proposition 2.2 proves the first example.

For the Gaussian, put \(v(t)=(4/\pi)^{1/4}e^{-2t^2}\). The earlier [Gaussian integral](../prerequisites/src/real-variable-calculations.md#ha-lca-pre-real-theorem-2-1) gives
\(\int_{\mathbb R}e^{-4t^2}\,dt=\sqrt\pi/2\), so \(\|v\|_2=1\). Completing the square and using translation invariance,
\[
 (v*\widetilde v)(x)
 =\frac{2}{\sqrt\pi}\int_{\mathbb R}
                   e^{-2t^2-2(t-x)^2}\,dt
 =\frac{2}{\sqrt\pi}e^{-x^2}
                   \int_{\mathbb R}e^{-4(t-x/2)^2}\,dt
 =e^{-x^2}.
\]
This is again Proposition 2.2.

The functions \(x\mapsto e^{iax}\) and \(x\mapsto e^{-iax}\) are continuous characters by the earlier [real-line character calculation](characters-and-the-dual-group.md#ha-lca-02-theorem-3-1). Their equal-weight average is \(\cos(ax)\), by the proved exponential and trigonometric identities in [the elementary calculus reading](../prerequisites/src/banach-spectrum.md#ha-lca-pre-banach-lemma-1-3). Positive-type functions form a convex cone, so this average lies in \(P_1\).

Finally \(w=1_{[-1/2,1/2]}\) has \(L^2\) norm one, and
\[
 (w*\widetilde w)(x)
   =\mu\big([-1/2,1/2]\cap[x-1/2,x+1/2]\big)
   =(1-|x|)_+.
\]
The interval measure formula gives the last equality, including endpoints, which have measure zero. Proposition 2.2 finishes the proof. \(\square\)

<a id="ha-lca-04-example-6-2"></a>
### Example 6.2. A geometric coefficient on \(\mathbb Z\)

If \(0<r<1\), the function \(n\mapsto r^{|n|}\) belongs to \(P_1(\mathbb Z)\).

**Proof.** On \(\ell^2(\mathbb Z)\) let \(U(k)u(n)=u(n-k)\), the left regular representation for [counting Haar measure](the-dual-group-as-the-gelfand-spectrum-of-l1.md#ha-lca-03-lemma-5-1). Define
\[
 u(n)=
 \begin{cases}
 \sqrt{1-r^2}\,r^n,& n\ge0,\\
 0,& n<0.
 \end{cases}
\]
The finite identity
\((1-r^2)\sum_{n=0}^N r^{2n}=1-r^{2N+2}\)
and \(r^{2N+2}\to0\) give \(\|u\|_2=1\). The limit follows, for example, by writing \(r^m=e^{m\log r}\) with \(\log r<0\), using the earlier [exponential and logarithm results](../prerequisites/src/real-variable-calculations.md#ha-lca-pre-real-lemma-1-2).
For \(k\ge0\),
\[
 \langle U(k)u,u\rangle
 =(1-r^2)\sum_{n\ge k}r^{n-k+n}
 =r^k.
\]
For negative \(k\), unitarity makes the coefficient the complex conjugate of the one at \(-k\); these values are real, so it is \(r^{|k|}\). Proposition 2.2 proves the assertion. \(\square\)

<a id="ha-lca-04-example-6-3"></a>
### Example 6.3. An open subgroup, without normality

If \(H\) is an open subgroup of \(G\), its indicator \(1_H\) belongs to \(P_1(G)\).

**Proof.** The coset space \(G/H\) is discrete, since every left coset is open. Form \(\ell^2(G/H)\), with the arbitrary-index Hilbert sum constructed in [the direct-sum theorem](../prerequisites/src/hilbert-spaces-and-unitary-representations.md#ha-lca-pre-hilbert-theorem-4-3). Its unit vectors are \(\delta_{xH}\). The rule
\[
 \pi(a)\delta_{xH}=\delta_{axH}
\]
permutes this orthonormal family, preserves finite-sum norms, and extends to a unitary with inverse \(\pi(a^{-1})\). Its group law holds on the basis and hence on the completion. The stabilizer of \(\delta_{xH}\) is \(xHx^{-1}\), which is open. Thus its orbit is constant for \(a\) near \(e\). The same is true for a finite sum after intersecting finitely many such neighbourhoods. Finite sums are dense in the Hilbert sum, so the common unitary norm bound proves strong continuity for every vector. Finally,
\[
 \langle\pi(a)\delta_H,\delta_H\rangle
       =\begin{cases}1,&a\in H,\\0,&a\notin H.\end{cases}
\]
The vector \(\delta_H\) has norm one and is cyclic, because all coset basis vectors are its translates. Proposition 2.2 proves the claim. No quotient group structure or normality of \(H\) is used. \(\square\)

<a id="ha-lca-04-example-6-4"></a>
### Example 6.4. An interval indicator fails positivity

The bounded class \(1_{[-1,1]}\) on \(\mathbb R\) is not integral positive.

**Proof.** If it had a continuous representative \(h\), then \(h=1\) throughout \((-1,1)\) and \(h=0\) throughout \((1,\infty)\). To justify either assertion, if it failed at an interior point, continuity would give a nonempty open interval on which \(h\) differs from the asserted constant by a fixed positive amount; that interval has positive Lebesgue measure, contradicting almost-everywhere equality. The two one-sided values at \(1\) contradict continuity. Corollary 3.2 therefore excludes integral positivity.

There is also an explicit negative test. Choose \(u\in C_c(\mathbb R)\), \(u\ge0\), supported in \((-1/16,1/16)\) with \(\int u=1\), using the earlier compact-cutoff and full-support results. Put
\[
 f=L_0u-\sqrt2\,L_{3/4}u+L_{3/2}u.
\]
In (9), whenever the two translated bumps have the same centre or adjacent centres, their argument difference has absolute value less than \(1\); for the pair of centres \(0,3/2\) its absolute value is greater than \(1\). Thus the nine terms of the double integral have the matrix
\[
 A=\begin{pmatrix}1&1&0\\1&1&1\\0&1&1\end{pmatrix}
\]
and coefficient vector \((1,-\sqrt2,1)\). Consequently
\[
 \int_{\mathbb R}(f^**f)(x)1_{[-1,1]}(x)\,dx
          =4-4\sqrt2<0.
\]
This directly violates integral positivity and does not depend on how the interval's endpoints are represented. \(\square\)

## 7. Exercises with complete solutions

<a id="ha-lca-04-exercise-7-1"></a>
### Exercise 7.1. Products

Show that the pointwise product of two positive-type functions is of positive type.

**Proof.** Use the canonical continuous representatives
\(\varphi(a)=\langle\pi(a)\xi,\xi\rangle\) and
\(\psi(a)=\langle\rho(a)\eta,\eta\rangle\). The earlier [Hilbert tensor-product construction](../prerequisites/src/hilbert-spaces-and-unitary-representations.md#ha-lca-pre-hilbert-proposition-7-3) proves that \(\pi\otimes\rho\) is strongly continuous on the completed tensor space and that
\[
 \langle(\pi\otimes\rho)(a)(\xi\otimes\eta),\xi\otimes\eta\rangle
       =\varphi(a)\psi(a).
\]
Proposition 2.2 proves positivity, and Lemma 2.1 gives the integral formulation as well. The value at \(e\) is \(\varphi(e)\psi(e)\), so a product of two members of \(P_1\) again belongs to \(P_1\). \(\square\)

<a id="ha-lca-04-exercise-7-2"></a>
### Exercise 7.2. The right difference inequality

For \(\varphi\in P_1(G)\), prove
\[
 |\varphi(x)-\varphi(y)|^2
                       \le2-2\operatorname{Re}\varphi(yx^{-1}).
\]
Explain why the order of the factors is valid without commutativity.

**Proof.** Take its GNS vector \(\xi\), with \(\|\xi\|=1\). Unitarity rewrites the difference as
\(\langle\xi,\pi(x^{-1})\xi-\pi(y^{-1})\xi\rangle\).
Cauchy–Schwarz bounds its squared modulus by the squared norm of the second argument. Expanding that norm gives
\[
 2-2\operatorname{Re}\langle\pi(x^{-1})\xi,\pi(y^{-1})\xi\rangle
 =2-2\operatorname{Re}\langle\pi(yx^{-1})\xi,\xi\rangle.
\]
The last equality moves \(\pi(y^{-1})\) from the second argument by its adjoint \(\pi(y)\), producing the ordered product \(yx^{-1}\) exactly. \(\square\)

<a id="ha-lca-04-exercise-7-3"></a>
### Exercise 7.3. Sums and limits

Show that nonnegative finite linear combinations of positive-type functions are positive type. Show that a pointwise limit which is continuous is positive type; in particular this holds for a limit uniform on each compact set.

**Proof.** For a finite sum \(\sum_k t_k\varphi_k\), \(t_k\ge0\), each matrix sum in (8) is the same nonnegative combination of nonnegative real sums. The function is continuous, so Lemma 2.0 bounds it and Lemma 2.1 gives integral positivity.

If \(\varphi_d(x)\to\varphi(x)\) at every point, the finite sum in (8) converges to the corresponding sum for \(\varphi\). The closed set \([0,\infty)\subset\mathbb C\) contains the limit, so \(\varphi\) is matrix positive. If the limit is continuous, Lemmas 2.0–2.1 give the desired conclusion.

To verify the continuity assertion under compact uniform convergence, fix \(x\in G\) and a compact neighbourhood \(K\) of \(x\), whose existence is proved by the earlier [locally compact shrinking lemma](../prerequisites/src/finite-radon-representation.md#ha-lca-pre-radon-lemma-1-3). Given \(\varepsilon>0\), choose one \(d\) with \(\sup_K|\varphi-\varphi_d|<\varepsilon/3\). Continuity of \(\varphi_d\) gives a neighbourhood of \(x\) inside \(K\) on which
\(|\varphi_d(y)-\varphi_d(x)|<\varepsilon/3\). The three-term triangle inequality yields \(|\varphi(y)-\varphi(x)|<\varepsilon\) there. Thus the limit is continuous, as required. \(\square\)

<a id="ha-lca-04-exercise-7-4"></a>
### Exercise 7.4. A representation for \(r^{|n|}\)

Exhibit a representation and unit vector giving the coefficient \(n\mapsto r^{|n|}\), \(0<r<1\), and compute the coefficient.

**Proof.** Let \(\mathcal H=\ell^2(\mathbb Z)\), let \(S\) be the bilateral shift \((Su)(j)=u(j-1)\), and set
\(\pi(n)=S^n\). The change of integer index in the sum of squared moduli proves that \(S\) is unitary, with inverse \((S^{-1}u)(j)=u(j+1)\). The group is discrete, so every orbit map is continuous.

Choose \(u(j)=\sqrt{1-r^2}\,r^j\) for \(j\ge0\) and zero otherwise. The geometric sum gives \(\|u\|^2=1\). For \(n\ge0\),
\[
 \langle S^nu,u\rangle
 =(1-r^2)\sum_{j=n}^{\infty}r^{j-n}r^j
 =(1-r^2)r^n\sum_{m=0}^{\infty}r^{2m}=r^n.
\]
For \(n<0\), the identity
\(\langle S^nu,u\rangle=\overline{\langle S^{-n}u,u\rangle}\)
gives \(r^{-n}\). Thus the coefficient is \(r^{|n|}\) for every integer, and Proposition 2.2 proves positive type. \(\square\)

<a id="ha-lca-04-exercise-7-5"></a>
### Exercise 7.5. Equality at the identity forces periods

For an LCA group written additively, show that \(\varphi(a)=\varphi(0)\) implies \(\varphi(x+a)=\varphi(x)\) for every \(x\). More generally, on any locally compact group, describe
\[
 H_\varphi=\{a:\varphi(a)=\varphi(e)\}.
\]

**Proof.** Write \(\varphi(a)=\langle\pi(a)\xi,\xi\rangle\), with \(c=\|\xi\|^2=\varphi(e)\). Then
\[
 \|\pi(a)\xi-\xi\|^2=2c-2\operatorname{Re}\varphi(a).
\]
If \(\varphi(a)=c\), the right side is zero, so \(\pi(a)\xi=\xi\). Conversely, that fixed-vector identity implies \(\varphi(a)=c\). Thus \(H_\varphi\) is exactly the stabilizer of \(\xi\). It contains the identity and is closed under products and inverses by the representation law; it is closed topologically as the inverse image of \(\{\xi\}\) under the continuous orbit map. For \(h,k\in H_\varphi\),
\[
 \varphi(hxk)
 =\langle\pi(h)\pi(x)\pi(k)\xi,\xi\rangle
 =\langle\pi(x)\xi,\pi(h^{-1})\xi\rangle
 =\varphi(x).
\]
Hence \(\varphi\) is constant on every double coset \(H_\varphi xH_\varphi\). In the abelian additive notation, take \(h=0,k=a\) to obtain the asserted period. If \(\xi=0\), the function is zero and its stabilizer is all of \(G\), consistent with the proof. \(\square\)

## Exact proof dependencies

This lesson uses the full earlier proofs of Hilbert completion, bounded forms, adjoints, continuous self-adjoint calculus, arbitrary Hilbert sums, Schur's lemma and tensor products in [the Hilbert reading](../prerequisites/src/hilbert-spaces-and-unitary-representations.md). It uses the full Haar domain, modular substitutions, sigma-compact localization, convolution and approximate identities in [the general Haar reading](../prerequisites/src/nonabelian-haar-integration.md). The [duality and convexity reading](../prerequisites/src/dual-balls-and-compact-convexity.md) supplies \(L^1\) duality, weak-star compactness and the extreme-point theorem. The exact result locators are placed at their uses above. All representation, GNS and positive-type conclusions asserted here are proved here or in those exact earlier results.

The free author draft's kernel and continuous GNS proofs inform Lemma 2.0; its C.5.1–C.5.2 inform the dominated-form and irreducibility argument; its C.5.4–C.5.5 inform compactness and normalization. Its integral-positivity lemma C.5.3 and the converse assertion in F.4 are proved here without importing their external references. The real-line and geometric examples are computed directly from the checked earlier integration results and the coefficient construction.
