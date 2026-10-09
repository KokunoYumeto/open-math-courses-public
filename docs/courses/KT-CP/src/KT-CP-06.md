# Pontryagin duality and the dual action

*Written by GPT-6.1 Sol (OpenAI), October 2026. Fourier prerequisite reconciliation by GPT-6 Astra (OpenAI). Self-checked by the writing AI. Public domain (CC0).*

Let \(G\) be a locally compact Hausdorff abelian group and let \((A,G,\alpha)\) be a C*-dynamical system. No separability, countability or unitality assumption is imposed. By Lesson 4, its full and reduced crossed products agree. We write \(B=A\rtimes_\alpha G\), retaining the conventions
\[
U_s\pi(a)U_s^*=\pi(\alpha_s(a)),\qquad
(\widetilde\pi(a)\xi)(t)=\pi(\alpha_{t^{-1}}(a))\xi(t),\qquad
(\lambda_s\xi)(t)=\xi(s^{-1}t).
\tag{6.1}
\]
Abelian groups are unimodular. Haar measure is fixed throughout; in discrete examples we use counting measure.

The dual action multiplies a coefficient at \(s\) by a character evaluated at \(s\). This operation becomes translation after Fourier transformation. We prove the C*-algebra identification and the action, distinguish fixed points from multiplier coefficients, and compute the action on a compact-operator model.

## The harmonic-analysis prerequisites

A **character** is a continuous homomorphism \(\chi:G\to\mathbb T\). The characters form the abelian group \(\widehat G\) under pointwise multiplication, with the compact-open topology. Thus \(\chi_i\to\chi\) means uniform convergence on each compact subset of \(G\). We use the pairing
\[
\langle s,\chi\rangle=\chi(s),\qquad
\mathcal F_+f(\chi)=\int_G f(s)\chi(s)\,ds.
\tag{6.2}
\]
The positive sign in (6.2) is part of our convention. For \(G=\mathbb R\), the character labelled by \(\eta\in\mathbb R\) is \(t\mapsto e^{2\pi it\eta}\).

The programme course *Harmonic analysis on locally compact abelian groups* supplies the general harmonic analysis used here. The relevant lessons have been written. Their statements apply to arbitrary locally compact Hausdorff abelian groups and retain nets and the local almost-everywhere convention when Haar measure is not sigma-finite.

- [*Characters and the dual group*](https://kokunoyumeto.github.io/open-math-courses-public/courses/HA-LCA/src/characters-and-the-dual-group.html#ha-lca-02-theorem-2-1), Theorems 2.1, 3.1 and 5.2, Corollary 3.2: the compact-convergence topology and its compactness criterion; compact groups have discrete duals, discrete groups have compact duals, and the elementary duals are identified topologically.
- [*The dual group as the Gelfand spectrum of \(L^1(G)\)*](https://kokunoyumeto.github.io/open-math-courses-public/courses/HA-LCA/src/the-dual-group-as-the-gelfand-spectrum-of-l1.html#ha-lca-03-lemma-1-1), Theorem 2.1, Corollary 2.2 and Theorems 3.1–3.2: the characters of \(L^1(G)\) are exactly integrations against continuous group characters; their spectrum topology is compact convergence. Fourier transforms belong to \(C_0(\widehat G)\), and their range is uniformly dense there.
- [*The Fourier inversion theorem and the dual Haar measure*](https://kokunoyumeto.github.io/open-math-courses-public/courses/HA-LCA/src/the-fourier-inversion-theorem-and-the-dual-haar-measure.html#ha-lca-07-theorem-2-1), Theorem 2.1 and Propositions 3.1–3.3: the fixed primal Haar measure determines the dual Haar normalization and the Fourier inversion formula. Lebesgue measure is self-dual for the pairing \(e^{2\pi i x\cdot\xi}\); compact mass-one and discrete counting measures are dual to each other.
- [*The Plancherel theorem*](https://kokunoyumeto.github.io/open-math-courses-public/courses/HA-LCA/src/the-plancherel-theorem.html#ha-lca-08-theorem-1-1), Theorem 1.1, Proposition 2.1 and Corollary 4.1: the Fourier transform extends to a surjective \(L^2\) isometry, and the normalized characters of a compact group form a complete orthonormal family.
- [*The Pontryagin duality theorem*](https://kokunoyumeto.github.io/open-math-courses-public/courses/HA-LCA/src/the-pontryagin-duality-theorem.html#ha-lca-09-theorem-2-1), Theorem 2.1, Proposition 3.1 and Theorem 4.1: evaluation identifies \(G\) topologically with its double dual, and the two normalized Fourier transforms compose to inversion.

The inversion statements have different domains. [HA-LCA-07, Theorem 2.1](https://kokunoyumeto.github.io/open-math-courses-public/courses/HA-LCA/src/the-fourier-inversion-theorem-and-the-dual-haar-measure.html#ha-lca-07-theorem-2-1) first proves pointwise inversion on \(B^1(G)=B(G)\cap L^1(G)\), where \(B(G)\) is the Fourier–Stieltjes algebra. [HA-LCA-09, Theorem 4.1](https://kokunoyumeto.github.io/open-math-courses-public/courses/HA-LCA/src/the-pontryagin-duality-theorem.html#ha-lca-09-theorem-4-1) treats a general \(f\in L^1(G)\) only when its Fourier transform is also integrable: the inverse integral gives a continuous representative agreeing with \(f\) almost everywhere, and agrees everywhere when \(f\) is continuous. The inverse in [HA-LCA-08, Theorem 1.1](https://kokunoyumeto.github.io/open-math-courses-public/courses/HA-LCA/src/the-plancherel-theorem.html#ha-lca-08-theorem-1-1) is an \(L^2\) inverse, not a pointwise integral assertion for every integrable function. [HA-LCA-03, Theorem 2.1](https://kokunoyumeto.github.io/open-math-courses-public/courses/HA-LCA/src/the-dual-group-as-the-gelfand-spectrum-of-l1.html#ha-lca-03-theorem-2-1) also supplies local compactness through the homeomorphism with the character space of the Banach algebra.

The programme uses the negative Fourier sign. Our positive transform (6.2) is its composition with inversion on the dual group. Inversion preserves Haar measure because an abelian group is unimodular. Hence the same Plancherel theorem gives
\[
\mathcal F_+:L^2(G)\longrightarrow L^2(\widehat G)
\quad\text{unitary}.
\tag{6.4}
\]
The evaluation isomorphism keeps the positive pairing:
\[
G\longrightarrow\widehat{\widehat G},\qquad
s\longmapsto[\chi\mapsto\chi(s)].
\tag{6.3}
\]
Thus no change of Haar normalization or additional countability hypothesis is hidden in the sign conversion. We also use the [locally compact Stone–Weierstrass theorem, HA-LCA-PRE-APPROX Theorem 3.2](https://kokunoyumeto.github.io/open-math-courses-public/courses/HA-LCA/prerequisites/src/uniform-approximation.html#ha-lca-pre-approx-theorem-3-2) and [automatic boundedness of Banach-algebra characters, Proposition 10.3(1)](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/banach-algebras-spectrum-holomorphic-functional-calculus-and-gelfand-theory.html#OA-FND-BN-17). The latter applies without an identity or a prior continuity assumption on the character.

## Characters and the group C*-algebra

**Lemma 6.1.** Every nonzero multiplicative linear functional \(\ell\) on the convolution algebra \(L^1(G)\) has the form
\[
\ell(f)=\int_G f(s)\chi(s)\,ds
\tag{6.5}
\]
for a unique \(\chi\in\widehat G\). Conversely, every expression (6.5) is a nonzero multiplicative *-functional.

**Proof.** Write \(L_sh(t)=h(s^{-1}t)\), and choose \(h\) with \(\ell(h)\ne0\). Commutativity of \(G\) gives
\[
(L_sh)*k=h*(L_sk),\qquad
\ell(L_sh)\ell(k)=\ell(h)\ell(L_sk).
\tag{6.6}
\]
Set \(\chi(s)=\ell(L_sh)/\ell(h)\). Equation (6.6) proves \(\ell(L_sk)=\chi(s)\ell(k)\) for every \(k\), including those with \(\ell(k)=0\). Applying this twice shows \(\chi(sr)=\chi(s)\chi(r)\), and \(\chi(e)=1\). Norm continuity of translations on \(L^1(G)\) gives continuity of \(\chi\). Moreover
\[
|\chi(s)|\leq\frac{\|\ell\|\,\|h\|_1}{|\ell(h)|}
\quad(s\in G).
\tag{6.7}
\]
Apply this uniform bound to all positive and negative powers of \(s\). It forces \(|\chi(s)|=1\).

For \(f\in C_c(G)\), the Bochner integral identity \(f*h=\int f(s)L_sh\,ds\) and boundedness of \(\ell\) give
\[
\ell(f)\ell(h)=\ell(f*h)
=\ell(h)\int_G f(s)\chi(s)\,ds.
\]
Divide by \(\ell(h)\) and extend by \(L^1\) density. This proves (6.5). Uniqueness follows because two different continuous characters differ on an open set, where a compactly supported test function distinguishes their integrals.

Conversely, Fubini and \(\chi(sr)=\chi(s)\chi(r)\) prove multiplicativity. The involution \(f^*(s)=\overline{f(s^{-1})}\), invariance of Haar measure under inversion, and \(\chi(s^{-1})=\overline{\chi(s)}\) prove preservation of *. A nonnegative nonzero compactly supported function multiplied by \(\overline\chi\) gives a nonzero value. ∎

**Theorem 6.2.** Formula (6.2) extends to an isometric *-isomorphism
\[
C^*(G)=C_r^*(G)\ \cong\ C_0(\widehat G).
\tag{6.8}
\]
Its spectrum is \(\widehat G\) with the compact-open topology.

**Proof.** For \(f,v\in C_c(G)\), Fubini and the substitution \(t=sr\) show
\[
\mathcal F_+(f*v)(\chi)
=\mathcal F_+f(\chi)\mathcal F_+v(\chi).
\tag{6.9}
\]
Consequently the Plancherel unitary conjugates \(\lambda(f)\) to multiplication by \(\mathcal F_+f\). One first checks this on \(C_c(G)\subset L^2(G)\), then extends by density and the \(L^1\) operator bound. Since Haar measure on \(\widehat G\) has full support, the multiplication norm of a continuous function is its supremum norm: a neighborhood of a point where the function nearly attains its supremum contains a compact set of positive finite measure on which to test the multiplication operator. Thus
\[
\|f\|_r=\|\mathcal F_+f\|_\infty=\|f\|_{C^*(G)}.
\tag{6.10}
\]
The last equality is amenability from Lesson 4. The involution calculation in Lemma 6.1 shows that \(\mathcal F_+\) preserves *. Riemann–Lebesgue places its image in \(C_0(\widehat G)\), so (6.10) gives an isometric homomorphism of the completed C*-algebra.

We check surjectivity rather than inferring it from pointwise injectivity. The transforms of \(C_c(G)\) form a self-adjoint algebra by (6.9). They vanish at no point: for a given \(\chi\), take \(f=\overline\chi\,p\), where \(p\geq0\) is compactly supported and \(\int p=1\); then \(\mathcal F_+f(\chi)=1\). They separate points: if \(\chi(s_0)\ne\eta(s_0)\), choose such a \(p\) supported in a sufficiently small neighborhood of \(s_0\). The integral of \(p(s)(\chi(s)-\eta(s))\) is then nonzero by continuity. The [locally compact Stone–Weierstrass theorem](https://kokunoyumeto.github.io/open-math-courses-public/courses/HA-LCA/prerequisites/src/uniform-approximation.html#ha-lca-pre-approx-theorem-3-2) gives density in \(C_0(\widehat G)\). The isometric completed image is closed, hence is all of it.

The spectrum statement follows from this isomorphism and the [spectrum of \(C_0(X)\), Example 11.4](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/banach-algebras-spectrum-holomorphic-functional-calculus-and-gelfand-theory.html#OA-FND-BN-19). Evaluation at \(\chi\) restricts to precisely the functional of Lemma 6.1. ∎

In particular, the scalar isomorphisms in Lesson 5 are instances of (6.8). With counting measure on \(\mathbb Z\),
\[
\mathcal F_+f(z)=\sum_{k\in\mathbb Z}f(k)z^k,
\qquad C^*(\mathbb Z)\cong C(\mathbb T).
\tag{6.11}
\]
For normalized Haar measure on \(\mathbb T\), \(C^*(\mathbb T)\cong c_0(\mathbb Z)\); for Lebesgue measure on \(\mathbb R\), \(C^*(\mathbb R)\cong C_0(\mathbb R)\). The group unitary \(u_s\in M(C^*(G))\) becomes the bounded multiplier \(\chi\mapsto\chi(s)\). It generally does not belong to \(C_0(\widehat G)\).

## Constructing the dual action

**Theorem 6.3.** The formula
\[
(\widehat\alpha_\chi f)(s)=\chi(s)f(s),\qquad f\in C_c(G,A),
\tag{6.12}
\]
extends uniquely to a strongly continuous action of \(\widehat G\) on \(B\). Its strict extension to \(M(B)\) satisfies
\[
\widehat\alpha_\chi(i_A(a))=i_A(a),\qquad
\widehat\alpha_\chi(i_G(s))=\chi(s)i_G(s).
\tag{6.13}
\]

**Proof.** In the convolution formula, the two character factors multiply as \(\chi(r)\chi(r^{-1}s)=\chi(s)\); thus (6.12) preserves convolution. In the involution formula the scalar factor is \(\overline{\chi(s^{-1})}=\chi(s)\), so it preserves *. Its inverse is multiplication by \(\overline\chi\).

If \((\pi,U)\) is a covariant pair, then \((\pi,\chi U)\), with \((\chi U)_s=\chi(s)U_s\), is another covariant pair and
\[
(\pi\rtimes U)(\widehat\alpha_\chi f)
=(\pi\rtimes(\chi U))(f).
\tag{6.14}
\]
Twisting by \(\chi\) bijects all covariant pairs. Taking their norm supremum shows that (6.12) is isometric in the full norm. It therefore extends to an automorphism of \(B\); the group law holds first on the dense convolution algebra and then on \(B\).

For \(f\) supported in the compact set \(K\),
\[
\|\widehat\alpha_\chi(f)-\widehat\alpha_\eta(f)\|_B
\leq\|\widehat\alpha_\chi(f)-\widehat\alpha_\eta(f)\|_1
\leq\sup_{s\in K}|\chi(s)-\eta(s)|\,\|f\|_1.
\tag{6.15}
\]
Compact-open convergence gives norm continuity on this dense subalgebra. For a general \(b\), approximation by \(f\) bounds the remaining two error terms by \(2\|b-f\|\), proving strong continuity.

An automorphism has a unique strict multiplier extension. Apply it to the left multiplier formulas \(i_A(a)f(s)=af(s)\) and \((i_G(r)f)(s)=\alpha_r(f(r^{-1}s))\) from Lesson 1. Equation (6.12) yields (6.13); equality on the dense essential ideal determines the multipliers. ∎

“Strongly continuous” here means point-norm continuous on \(B\). It does not assert point-norm continuity on all of \(M(B)\). Nor does (6.13) assert that \(i_A(A)\subset B\) when \(G\) is nondiscrete.

**Proposition 6.4.** On the regular representation space \(L^2(G,H)\), multiplication by characters,
\[
(M_\chi\xi)(t)=\chi(t)\xi(t),
\tag{6.16}
\]
is a strongly continuous unitary representation of \(\widehat G\) implementing \(\widehat\alpha\). The same formula gives an adjointable unitary on the regular Hilbert \(A\)-module \(L^2(G,A)\), continuous on each module vector.

**Proof.** Its adjoint is \(M_{\overline\chi}\); it commutes with \(\widetilde\pi(a)\). Direct substitution gives
\[
M_\chi\lambda_sM_\chi^*\xi(t)
=\chi(t)\overline{\chi(s^{-1}t)}\xi(s^{-1}t)
=\chi(s)\lambda_s\xi(t).
\tag{6.17}
\]
Integration proves implementation of (6.12). On vectors of compact support \(K\),
\[
\|(M_\chi-M_\eta)\xi\|_2
\leq\sup_K|\chi-\eta|\,\|\xi\|_2.
\tag{6.18}
\]
Density and the uniform bound two prove strong continuity. On the module, the same estimate follows by ordering the \(A\)-valued integral of \(\xi(t)^*\xi(t)\); it proves vector continuity on completion. Adjointability and (6.17) are unchanged. ∎

For the scalar algebra, Fourier coordinates make the action particularly explicit:
\[
\mathcal F_+(\widehat\alpha_\chi f)(\eta)
=\mathcal F_+f(\chi\eta).
\tag{6.19}
\]
Thus on \(C_0(\mathbb R)\) the real dual parameter \(\eta\) acts by \(h(\xi)\mapsto h(\xi+\eta)\). On \(c_0(\mathbb Z)=C^*(\mathbb T)\), the integer \(m\) acts by \(h(k)\mapsto h(k+m)\). These signs follow from (6.2), not from an unspecified translation convention.

## Fixed points and invariant ideals

**Theorem 6.5.** If \(G\) is discrete abelian, the fixed-point algebra \(B^{\widehat\alpha}\) is \(i_A(A)\subset B\). Normalized Haar averaging over the compact group \(\widehat G\) is the faithful conditional expectation
\[
E(b)=\int_{\widehat G}\widehat\alpha_\chi(b)\,d\chi,
\qquad
E\left(\sum_{s\in F}a_su_s\right)=a_e.
\tag{6.20}
\]
It agrees with the canonical expectation of Lesson 3.

**Proof.** Pontryagin duality separates points: for \(s\ne e\), some \(\eta\in\widehat G\) has \(\eta(s)\ne1\). Haar invariance gives
\[
\int_{\widehat G}\chi(s)\,d\chi
=\eta(s)\int_{\widehat G}\chi(s)\,d\chi,
\]
so this integral is zero. At \(s=e\) it is one. Applying this to finite crossed-product polynomials proves (6.20). Since such polynomials are dense and \(i_A(A)\) is closed, \(E(B)\subset i_A(A)\). Equation (6.13) shows that \(E\) fixes \(i_A(A)\), so its range is exactly that algebra. Haar invariance shows that its range is also exactly the fixed-point algebra.

The Bochner average is contractive and positive; it is completely positive by averaging at every matrix level. It is idempotent and \(A\)-bimodular because the action fixes \(A\). Hence it is a conditional expectation. For faithfulness, let \(b\geq0\) with \(E(b)=0\). For every state \(\varphi\) of \(B\), the nonnegative continuous function \(\chi\mapsto\varphi(\widehat\alpha_\chi(b))\) has integral zero. Full support of Haar measure forces it to vanish everywhere, and at the identity it gives \(\varphi(b)=0\). States separate the positive cone, so \(b=0\). Finally, agreement on the dense polynomials identifies this map with Lesson 3's expectation. ∎

The discrete hypothesis matters. For the trivial real action on \(A=\mathbb C\), the crossed product is \(C_0(\mathbb R)\), and (6.19) shows that its fixed-point algebra is zero: a translation-invariant function is constant, and a constant vanishing at infinity is zero. The fixed copy of \(\mathbb C\) lies instead in its multiplier algebra. There is no normalized Haar probability on the noncompact dual to use in (6.20).

If \(I\triangleleft A\) is \(\alpha\)-invariant, Lesson 1 identifies \(I\rtimes G\) with an ideal of \(B\). Formula (6.12) preserves \(C_c(G,I)\) and therefore its closure. This proves the forward direction of
\[
I\longmapsto I\rtimes G:
\{\alpha\text{-invariant ideals of }A\}
\longleftrightarrow
\{\widehat\alpha\text{-invariant ideals of }B\}.
\tag{6.21}
\]
The full bijection is Blackadar, *Operator Algebras*, Theorem II.10.5.4, printed p. 226. Its converse will be proved in Lesson 8 using Takai duality. In the nondiscrete case it cannot be justified by casually writing \(J\cap A\): the coefficient algebra is embedded in \(M(B)\), not generally in \(B\).

## Fourier and gauge examples

For a homeomorphism \(h:X\to X\), the integer action on \(C_0(X)\) is \(\alpha_n(a)=a\circ h^{-n}\). Its dual circle action fixes the coefficients and sends \(u\) to \(zu\). On the rotation algebra of Lesson 1, with coordinate unitary \(v\) and rotation \(h(w)=\omega w\),
\[
uvu^*=\overline\omega v,\qquad
\widehat\alpha_z(u)=zu,\qquad \widehat\alpha_z(v)=v.
\tag{6.22}
\]
The gauge parameter is independent of the spatial rotation parameter \(\omega\).

For \(G=\mathbb Z/n\mathbb Z\), write \(\chi_m(j)=e^{2\pi ijm/n}\). Counting measure gives
\[
\mathcal F_+f(m)=\sum_{j=0}^{n-1}f(j)e^{2\pi ijm/n},\qquad
C^*(G)\cong\mathbb C^n.
\tag{6.23}
\]
The transform into the dual \(L^2\) space uses measure \(n^{-1}\) times counting measure and is unitary. If both coordinate spaces use counting measure, the unitary matrix instead has entries \(n^{-1/2}e^{2\pi ijm/n}\). The C*-algebra map (6.23) remains unscaled. A dual parameter \(k\) cyclically shifts the coordinate function by \(h(m)\mapsto h(m+k)\). For an arbitrary finite abelian group, replace these exponentials by its characters; (6.8) gives \(\mathbb C^{\widehat G}\), and (6.19) gives the same coordinate permutation.

## Exercises with complete solutions

**Exercise 1.** In \(C(\mathbb T)\rtimes_\alpha\mathbb Z\), compute the dual action on \(au^k\). For the rotation action in (6.22), check directly that the defining relation is preserved and identify the fixed-point algebra.

**Solution.** The character of \(\mathbb Z\) labelled by \(z\in\mathbb T\) is \(k\mapsto z^k\). Equations (6.12)–(6.13) give \(\widehat\alpha_z(au^k)=z^kau^k\). In particular, \((zu)v(zu)^*=uvu^*=\overline\omega v\), so the rotation relation is preserved. Averaging kills every nonzero degree and fixes degree zero. Theorem 6.5 therefore identifies the fixed-point algebra with the entire coefficient copy of \(C(\mathbb T)\); no finite-polynomial assumption on a fixed element is needed.

**Exercise 2.** Let \(\chi_i\to\chi\) in the compact-open topology. Prove norm convergence \(\widehat\alpha_{\chi_i}(b)\to\widehat\alpha_\chi(b)\) for every \(b\in B\) and strong convergence \(M_{\chi_i}\to M_\chi\) on the regular space. Explain why neither statement requires a sequential topology.

**Solution.** Given \(\varepsilon>0\), choose \(f\in C_c(G,A)\) with \(\|b-f\|<\varepsilon\), and let \(K=\operatorname{supp}f\). Isometry and (6.15) give
\[
\|\widehat\alpha_{\chi_i}(b)-\widehat\alpha_\chi(b)\|
\leq2\varepsilon+\sup_K|\chi_i-\chi|\,\|f\|_1.
\]
The last term tends to zero; then let \(\varepsilon\downarrow0\). For a vector \(\xi\), approximate it in \(L^2\) by a compactly supported vector \(\xi_0\). The corresponding estimate is \(2\|\xi-\xi_0\|+\sup_{\operatorname{supp}\xi_0}|\chi_i-\chi|\,\|\xi_0\|\). It proves strong convergence, and the same estimate proves module-vector convergence. Each proof uses the definition of convergence of a net, so no countable neighborhood base is involved.

**Exercise 3.** For a discrete abelian \(G\), verify the averaging formula for arbitrary Haar normalization on the dual, and recover each Fourier coefficient of \(b\in B\) by a weighted average.

**Solution.** If the dual Haar mass is \(c>0\), divide the integral by \(c\) to obtain \(E\). Its value on polynomials is still \(a_e\) by character orthogonality. For counting measure on \(G\), define
\[
P_s(b)=c^{-1}\int_{\widehat G}\overline{\chi(s)}\widehat\alpha_\chi(b)\,d\chi.
\tag{6.24}
\]
On a polynomial this is \(a_su_s\). In general \(P_s\) is contractive and its range lies in the closed subspace \(i_A(A)u_s\): right multiplication by the multiplier unitary \(u_s\) is an isometry, so that subspace is closed. Density now gives \(P_s(b)=a_su_s\) for a unique \(a_s\in A\). Equivalently \(a_s=E(bu_s^*)\), because both expressions agree on dense polynomials. This is the coefficient formula of Lesson 3. The existence of all these coefficients does not imply norm convergence of the unordered Fourier series.

**Exercise 4.** For left translation \((\mathrm{lt}_sa)(x)=a(s^{-1}x)\), prove
\[
C_0(G)\rtimes_{\mathrm{lt}}G\cong\mathcal K(L^2(G))
\tag{6.25}
\]
for the abelian group of this lesson, and identify the dual action on the right.

**Solution.** Let \(M(a)\) multiply functions on \(L^2(G)\), and let \(\lambda\) be left translation. Full support of Haar measure makes \(M\) faithful, and the pair is covariant. For a jointly compactly supported continuous function \(f(t)(x)\), its integrated operator has kernel
\[
((M\rtimes\lambda)(f)\xi)(x)
=\int_G f(t)(x)\xi(t^{-1}x)\,dt
=\int_G K_f(x,y)\xi(y)\,dy,
\qquad K_f(x,y)=f(xy^{-1})(x).
\tag{6.26}
\]
The change of variables preserves Haar measure because \(G\) is abelian and unimodular. The map \((x,y)\mapsto(xy^{-1},x)\) is a homeomorphism, so every \(C_c(G\times G)\) kernel occurs. Such a joint function does define a norm-continuous compactly supported map \(t\mapsto f(t)\in C_0(G)\), as follows by approximating compactly supported joint functions uniformly by finite sums of products of compactly supported functions in each variable. Conversely these finite sums are dense in \(C_c(G,C_0(G))\) for its \(L^1\) norm, by compact-range approximation and coefficient cutoffs.

All compactly supported continuous kernels give compact operators. Indeed approximate a kernel, on fixed compact rectangles, by finite sums \(p(x)q(y)\). The associated operators have finite rank, and the operator norm of the error is at most its \(L^2\) kernel norm, hence at most the uniform error times the square root of the two finite Haar masses. Conversely the kernels \(p(x)\overline{q(y)}\), with \(p,q\in C_c(G)\), give rank-one operators whose span is dense in \(\mathcal K(L^2(G))\). Thus the image closure is precisely the compact operators.

It remains to prove injectivity. By the absorption result of Lesson 2, the regular representation induced from the faithful coefficient representation \(M\) is unitarily equivalent to \((M\otimes1,\lambda\otimes\lambda)\). On \(L^2(G\times G)\) define the unitary
\[
(W\xi)(x,y)=\xi(x,xy).
\tag{6.27}
\]
Left invariance in the second coordinate proves unitarity. It leaves \(M(a)\otimes1\) unchanged and gives
\[
W(\lambda_s\otimes\lambda_s)W^*=\lambda_s\otimes1:
\quad
\xi(s^{-1}x,(s^{-1}x)^{-1}s^{-1}xy)=\xi(s^{-1}x,y).
\]
Consequently \(M\rtimes\lambda\), amplified by the identity on \(L^2(G)\), is faithful in the reduced norm. The amplification is isometric; amenability identifies the full norm with that norm. This proves (6.25).

Finally \(M_\chi\) commutes with \(M(a)\) and satisfies (6.17), so under (6.25) the dual action is \(\operatorname{Ad}M_\chi\). On kernels it is
\[
K(x,y)\longmapsto\chi(x)\overline{\chi(y)}K(x,y)
=\chi(xy^{-1})K(x,y),
\tag{6.28}
\]
which is exactly (6.12) through (6.26). Character multiplication is a strongly continuous unitary representation, but it need not be continuous in operator norm. The implemented action is nevertheless norm continuous on the compact operators, first on rank-one operators by vector continuity and then by density.

## What this lesson does not prove

Local compactness of the dual, Riemann–Lebesgue, scalar Plancherel and Pontryagin duality use the five exact written programme proof providers identified above, in arbitrary locally compact generality. The complete Stone–Weierstrass and Banach-algebra character proofs are linked above with their precise hypotheses; Example 11.4 supplies the spectrum identification for functions vanishing at infinity. The C*-algebra isomorphism, dual-action construction and continuity, discrete fixed-point theorem, and abelian translation compact-operator model are proved here. The invariant-ideal converse (6.21) is reserved for the owned Takai proof in Lesson 8. Lesson 7 proves the translation theorem for arbitrary locally compact groups through Green imprimitivity; the abelian proof above does not establish that wider generality.

Blackadar, *Operator Algebras*, Proposition II.10.2.7 and §§II.10.5.1–II.10.5.4, provide the C*-theorem locators. The positive-character dual action and its module implementation also appear in Connes, *Noncommutative Geometry*, Chapter II, Appendix C, Proposition 4. [Author's electronic edition](https://alainconnes.org/wp-content/uploads/book94bigpdf.pdf). Schulz-Baldes and Stoiber, [*Harmonic analysis in operator algebras and its applications to index theory and topological solid state systems*](https://arxiv.org/pdf/2206.07781v2), arXiv:2206.07781v2, §1.6, provides another dual-action convention, with a conjugate character in its C*-definition. Our convention is explicitly fixed in (6.12) and used throughout the calculations. The next two lessons develop induction and the second crossed product, rather than using the name “duality” as a substitute for their proofs.

B. Blackadar, *Operator Algebras: Theory of C*-Algebras and von Neumann Algebras*. [Author's revised edition, 2017](https://bruceblackadar.com/Mathematics/Cycr.pdf).
