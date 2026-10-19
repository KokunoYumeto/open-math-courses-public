# Cartan subalgebras and their conjugacy

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

A generic element singles out the subalgebra on which its adjoint action has eigenvalue zero. Nilpotence and a normalizer condition characterize that subalgebra without a choice of coordinates. In a complex semisimple algebra it is precisely a maximal commuting family of semisimple elements. We will then move these families by inner automorphisms: each family sweeps out a set containing a Zariski-open subset of the whole algebra, and two such sets must meet.

All Lie algebras are finite-dimensional over \(\mathbb C\). Sections 1 and 2 begin with general Lie algebras; the conjugacy theorem concerns semisimple ones. We use Engel's and Lie's theorems from [Nilpotent and solvable Lie algebras: Engel's and Lie's theorems](RT-LIE-02.md), the Killing form, inner derivations and Jordan decomposition from [The Killing form and Cartan's criteria](RT-LIE-03.md), and the maximal toral centralizer and root decomposition from [The root space decomposition of a semisimple Lie algebra](RT-LIE-07.md). The algebraic geometry background is *Algebraic Geometry Bridge*. The precise additional geometry imports are stated in Section 3.

## 1. Which zero space is being minimized?

For an endomorphism \(D\) of an \(N\)-dimensional space, its **Fitting nullspace** is \(\ker D^N\). On the complementary Fitting summand \(\operatorname{im}D^N\), the operator is invertible. To see this, decompose into generalized eigenspaces: the zero eigenspace is killed by \(D^N\), whereas every nonzero eigenvalue makes \(D\) invertible. This also proves that the nullspace dimension is the multiplicity of zero in the characteristic polynomial.

Write
\[
\mathfrak g_0(x)=\ker(\operatorname{ad}x)^N,
\qquad n(x)=\dim\mathfrak g_0(x),
\qquad r_F(\mathfrak g)=\min_{x\in\mathfrak g}n(x).
\tag{1.1}
\]
An element attaining this minimum is **Fitting-regular**. Whenever this lesson says simply *regular*, it means Fitting-regular. A second convention, common in Lie theory, minimizes the dimension of the ordinary centralizer \(C_{\mathfrak g}(x)=\ker\operatorname{ad}x\). We call that **centralizer-regular** here. The two conventions need not coincide.

For example, in \(\mathfrak{sl}_2\), the nonzero nilpotent matrix \(e=E_{12}\) has centralizer \(\mathbb Ce\), of the smallest possible dimension. But \(\operatorname{ad}e\) is nilpotent, so \(\mathfrak g_0(e)=\mathfrak g\). It is centralizer-regular and is not Fitting-regular. The distinction will be worked out for every Jordan type in \(\mathfrak{sl}_3\) in Exercise 6.2.

**Lemma 1.1.** The regular elements form a nonempty Zariski-open subset of \(\mathfrak g\).

**Proof.** In linear coordinates on \(\mathfrak g\), write
\[
\det(t1-\operatorname{ad}x)=\sum_{j=0}^{N}c_j(x)t^j,
\qquad c_N=1.
\tag{1.2}
\]
Each \(c_j\) is a polynomial. Put \(r=r_F(\mathfrak g)\). Every polynomial (1.2) is divisible by \(t^r\); therefore \(c_j\) vanishes at every point for \(j<r\). Such a polynomial is identically zero over \(\mathbb C\), as induction on the number of variables reduces this to the finite number of roots of a nonzero polynomial in one variable. Some element attains the minimum, so \(c_r\) is not identically zero. Exactly the elements with \(c_r(x)\ne0\) are regular. This is the nonempty principal open set \(D(c_r)\). \(\square\)

For a nonzero algebra, \(r_F\ge1\), since \([x,x]=0\); at \(x=0\), the whole space is the nullspace. For the zero algebra we take \(N=r_F=0\), the characteristic polynomial is 1, and its sole element is regular. All subsequent assertions include this case.

The **normalizer** of a subalgebra \(\mathfrak a\) is
\[
N_{\mathfrak g}(\mathfrak a)
=\{z\in\mathfrak g:[z,\mathfrak a]\subseteq\mathfrak a\}.
\]
A **Cartan subalgebra** is a nilpotent subalgebra equal to its normalizer. Nilpotence refers to its own lower central series; it does not mean that all its elements act nilpotently on the ambient algebra.

We will repeatedly use the following derivation calculation. If \(D\) is a derivation, \(u\) is a generalized \(a\)-eigenvector and \(v\) is a generalized \(b\)-eigenvector, then
\[
(D-(a+b)1)^m[u,v]
=\sum_{i=0}^{m}\binom mi
[(D-a1)^iu,(D-b1)^{m-i}v].
\tag{1.3}
\]
The case \(m=1\) is the derivation rule, and induction gives the formula. For sufficiently large \(m\), every summand is zero. Thus generalized eigenspace brackets add eigenvalues. In particular, for \(D=\operatorname{ad}x\), its zero summand \(H=\mathfrak g_0(x)\) is a subalgebra, and every element of \(H\) preserves both \(H\) and the sum \(V\) of the nonzero summands under its adjoint action. The space \(V\) need not be a subalgebra.

**Proposition 1.2.** For every regular \(x\) in a complex Lie algebra, \(\mathfrak g_0(x)\) is a Cartan subalgebra.

**Proof.** Set \(H=\mathfrak g_0(x)\), \(V=\operatorname{im}(\operatorname{ad}x)^N\), and \(r=\dim H\). Equation (1.3) gives the invariant decomposition \(\mathfrak g=H\oplus V\) for the adjoint action of every \(b\in H\). Also \(x\in H\).

Fix \(b\in H\). The determinant of \(\operatorname{ad}(x+sb)|_V\) is a polynomial in \(s\) nonzero at \(s=0\). Except for finitely many \(s\), this restriction is invertible. For each such \(s\), all generalized zero eigenvectors of \(\operatorname{ad}(x+sb)\) belong to \(H\). Regularity of \(x\) says that their dimension is at least \(r\), so it must equal \(r\). Consequently
\[
\det(t1_H-\operatorname{ad}(x+sb)|_H)=t^r
\tag{1.4}
\]
for infinitely many \(s\). Every coefficient is a polynomial in \(s\), so (1.4) holds identically. The coefficient of \(t^{r-j}\) has degree at most \(j\) in \(s\); its leading coefficient is the corresponding characteristic coefficient of \(\operatorname{ad}b|_H\). All these coefficients vanish for \(j\ge1\). Hence the characteristic polynomial of \(\operatorname{ad}b|_H\) is \(t^r\), and Cayley–Hamilton makes this operator nilpotent. Engel's theorem now makes \(H\) nilpotent.

If \(z\) normalizes \(H\), then \([x,z]\in H\). A power of \(\operatorname{ad}x\) kills that bracket, so a further power kills \(z\). Thus \(z\in H\). The reverse inclusion in the normalizer holds because \(H\) is a subalgebra. Therefore \(N_{\mathfrak g}(H)=H\). \(\square\)

This construction already proves existence of Cartan subalgebras in every complex finite-dimensional Lie algebra. No semisimplicity has been used.

## 2. Recovering the toral definition in the semisimple case

The next lemma lets us start with an arbitrary nilpotent self-normalizing subalgebra, rather than assume it contains an element already known to be globally regular.

**Lemma 2.1.** If \(\mathfrak a\) is a Cartan subalgebra, there exists \(a\in\mathfrak a\) such that \(\mathfrak g_0(a)=\mathfrak a\).

**Proof.** Apply Lie's theorem to the representation of the nilpotent, hence solvable, algebra \(\mathfrak a\) on \(\mathfrak g\). An invariant full flag has diagonal characters \(\chi_1,\ldots,\chi_N\in\mathfrak a^*\). Choose \(a\in\mathfrak a\) for which \(\chi_i(a)\ne0\) whenever \(\chi_i\ne0\). This is possible because a finite union of proper linear hyperplanes cannot cover a complex vector space: the product of their nonzero defining linear forms is a nonzero polynomial.

Put \(W=\mathfrak g_0(a)\). Nilpotence of \(\mathfrak a\) implies \((\operatorname{ad}a)^m\mathfrak a=0\) for sufficiently large \(m\), so \(\mathfrak a\subseteq W\). Formula (1.3) shows that every \(\operatorname{ad}b\), \(b\in\mathfrak a\), preserves \(W\). Intersect the invariant full flag with \(W\). Its nonzero one-dimensional successive quotients have exactly those characters \(\chi_i\) for which \(\chi_i(a)=0\): this follows either by the generalized eigenspace decomposition on each flag term or by its polynomial spectral projections. Our choice of \(a\) makes each such character identically zero. Therefore every \(\operatorname{ad}b|_W\) is nilpotent.

On \(W/\mathfrak a\) these operators are still nilpotent. If the quotient were nonzero, Engel's common-zero-vector theorem would give \(z\in W\setminus\mathfrak a\) with \([b,z]\in\mathfrak a\) for every \(b\in\mathfrak a\). That would put \(z\) in the normalizer, contrary to the Cartan condition. Hence \(W=\mathfrak a\). \(\square\)

**Theorem 2.2.** In a complex semisimple Lie algebra, Cartan subalgebras are exactly maximal toral subalgebras.

**Proof.** First let \(\mathfrak a\) be a Cartan subalgebra and choose \(a\) as in Lemma 2.1. Put \(D=\operatorname{ad}a\). Invariance of the Killing form \(\kappa\) gives
\[
\kappa(Du,v)=-\kappa(u,Dv).
\tag{2.1}
\]
If \(u\) belongs to its generalized zero summand and \(v\) to a nonzero generalized \(\lambda\)-summand, choose \(m\) with \(D^mu=0\). On the latter summand \(D\) is invertible, so write \(v=D^mw\) there. Then (2.1) gives \(\kappa(u,v)=(-1)^m\kappa(D^mu,w)=0\). Thus \(\mathfrak a\) is orthogonal to every other summand. Nondegeneracy of \(\kappa\) on \(\mathfrak g\) implies nondegeneracy of its restriction to \(\mathfrak a\).

Triangularize the action of \(\mathfrak a\) on \(\mathfrak g\) by Lie's theorem. The action of \([\mathfrak a,\mathfrak a]\) is strictly upper triangular. Products of those matrices with the upper triangular matrices for \(\mathfrak a\) have trace zero. Hence
\(\kappa(\mathfrak a,[\mathfrak a,\mathfrak a])=0\). The nondegenerate restriction forces \([\mathfrak a,\mathfrak a]=0\).

For \(x\in\mathfrak a\), take its intrinsic commuting Jordan parts \(x_s,x_n\). Since \(x\) commutes with every \(y\in\mathfrak a\), their adjoint operators, which are polynomials in \(\operatorname{ad}x\), also commute with \(\operatorname{ad}y\). The zero centre gives \([x_s,y]=[x_n,y]=0\). Thus both parts belong to \(C_{\mathfrak g}(\mathfrak a)\subseteq N_{\mathfrak g}(\mathfrak a)=\mathfrak a\). For every \(y\in\mathfrak a\), the commuting product \(\operatorname{ad}x_n\operatorname{ad}y\) is nilpotent: its \(m\)-th power contains \((\operatorname{ad}x_n)^m=0\). Consequently \(\kappa(x_n,y)=0\). Nondegeneracy on \(\mathfrak a\) gives \(x_n=0\). Every element of \(\mathfrak a\) is semisimple, so \(\mathfrak a\) is toral. A larger toral algebra would centralize it and lie in its normalizer. It is therefore maximal toral.

Conversely, let \(\mathfrak h\) be maximal toral. The root decomposition already proved in the prerequisite is
\[
\mathfrak g=\mathfrak h\oplus
\bigoplus_{\alpha\in\Phi}\mathfrak g_\alpha,
\qquad C_{\mathfrak g}(\mathfrak h)=\mathfrak h.
\tag{2.2}
\]
It is abelian, hence nilpotent. If \(z=z_0+\sum z_\alpha\) normalizes it, then \([H,z]=\sum\alpha(H)z_\alpha\) belongs to \(\mathfrak h\) for every \(H\in\mathfrak h\). Since each \(\alpha\ne0\), all \(z_\alpha\) vanish. Thus \(z\in\mathfrak h\), proving self-normalization. \(\square\)

**Corollary 2.3.** Every regular element of a complex semisimple Lie algebra is semisimple, and it belongs to a unique Cartan subalgebra, namely \(\mathfrak g_0(x)=C_{\mathfrak g}(x)\).

**Proof.** Proposition 1.2 and Theorem 2.2 make \(\mathfrak g_0(x)\) toral. It contains \(x\), so \(x\) is semisimple and its generalized zero space is its ordinary centralizer. If another Cartan subalgebra \(\mathfrak h\) contains \(x\), its elements commute with \(x\), so \(\mathfrak h\subseteq C_{\mathfrak g}(x)\). Maximal torality forces equality. \(\square\)

For any Cartan subalgebra define
\[
\mathfrak h^\circ
=\{x\in\mathfrak h:\alpha(x)\ne0
\text{ for every }\alpha\in\Phi\}.
\tag{2.3}
\]
This is a nonempty Zariski-open subset. The root decomposition gives
\[
\mathfrak g_0(x)=C_{\mathfrak g}(x)=\mathfrak h,
\qquad
\mathfrak g=\mathfrak h\oplus[\mathfrak g,x]
\quad(x\in\mathfrak h^\circ),
\tag{2.4}
\]
since \([v,x]=-\alpha(x)v\) on \(\mathfrak g_\alpha\). We have not yet identified \(\dim\mathfrak h\) with the global minimum \(r_F\); the density argument will do so for every Cartan subalgebra.

## 3. The algebraic group generated by nilpotent exponentials

An affine algebraic group over \(\mathbb C\) is a group described by polynomial equations, with regular multiplication and inversion. The Zariski topology has polynomial zero sets as its closed sets. A variety is **irreducible** if it is not a union of two proper closed subsets; equivalently, any two nonempty open subsets meet. Affine space is irreducible: if two proper polynomial zero sets covered it, a product of nonzero polynomials vanishing on the two sets would vanish everywhere, which is impossible. A **constructible** set is a finite union of locally closed sets, and a morphism is **dominant** when its image is dense.

Here are the geometry imports, stated at their actual hypotheses. Their linked proofs use [the invariant-differential isomorphism, Theorem 6.2](../../AG-GS/AG-GS-01.html#6-translating-geometry-from-the-identity), [the tangent-dimension and field-descent lemmas](../../AG-GS/AG-GS-02.html#3-one-local-ring-controls-smoothness), and [the canonical flat closed component structure, Theorem 4.2](../../AG-FSE/flat-morphisms.html#4-flat-closed-subschemes).

- A finite-type affine group scheme over a characteristic-zero field is smooth [Milne, Theorem 3.23]; the programme proof is [Lie algebras and smoothness of group schemes, Theorem 4.3](../../AG-GS/AG-GS-02.html#4-why-characteristic-zero-forces-smoothness). Its identity component is a closed subgroup, and each connected component is irreducible [Milne, Proposition 1.34 and Corollary 1.35]; see [Group schemes over a field, Theorems 2.2–2.3](../../AG-GS/AG-GS-03.html#2-connectedness-compactness-and-the-identity-component). These apply in particular over \(\mathbb C\).
- For morphisms between smooth complex algebraic varieties, surjectivity of the differential at every point is equivalent to smoothness; smooth morphisms are open [Milne, Appendix A.71 and A.69]. For the sufficient differential criterion, use [Projective cohomology and smooth affine models, Lemma 3.A](../../AG-RG/AG-RG-S02.html#smooth-map-differential); openness is proved in [Smooth morphisms, Proposition 1.2](../../AG-FSE/smooth-morphisms.html#1-smooth-charts-and-their-relative-dimension) and [Flat morphisms, Theorem 3.2](../../AG-FSE/flat-morphisms.html#3-what-flatness-does-to-the-topology). For necessity, take a tangent vector at the image point with coefficients in the source residue field. It is a morphism from the spectrum of that field’s dual numbers to the target, whose reduction is the image of the specified source point. Formal smoothness lifts this morphism through that source point. The lift is a source tangent vector mapping to the prescribed vector, proving surjectivity. The full-rank condition is open, since local matrices of the differential have regular entries and rank is detected by minors.
- A quasi-compact morphism of schemes locally of finite presentation takes locally constructible sets to locally constructible sets [Stacks, Tag 054K]. In particular, a finite-type morphism of complex varieties has constructible image. The affine algebra statement is: for a finitely presented ring map \(R\to S\), the image of a constructible subset of \(\operatorname{Spec}S\) in \(\operatorname{Spec}R\) is constructible [Stacks, Tag 00FE]. Both statements are proved in [Quasi-finite morphisms and Chevalley, Theorem 5.1](../../AG-MO/quasi-finite-morphisms-and-chevalley.html#5-chevalley-by-noetherian-approximation), with the Noetherian argument in [Theorem 4.2](../../AG-MO/quasi-finite-morphisms-and-chevalley.html#4-why-a-dominant-finite-type-map-contains-an-open).

The two tags link to [054K in AI Integrated Stacks Project](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-theorem-chevalley) and [00FE in AI Integrated Stacks Project](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-theorem-chevalley). The [official Stacks project](https://stacks.math.columbia.edu/) is the underlying source. AI Integrated Stacks Project is an edition with AI-proposed corrections and AI-written additions, not reviewed by the Stacks project's maintainers. No algebraic-group conjugacy theorem is imported into the Lie-algebra proof.

**Lemma 3.1 (the density step).** Let \(f:X\to Y\) be a finite-type morphism between smooth complex varieties, with \(Y\) irreducible. If \(df\) is surjective at one point, then \(f\) is dominant and its image contains a nonempty Zariski-open subset of \(Y\).

**Proof.** The differential remains surjective on a nonempty open neighborhood of that point. Restricting to this neighborhood gives a smooth morphism by the cited differential criterion. Its image is nonempty and open, hence dense in the irreducible \(Y\), proving dominance.

Chevalley's constructibility theorem applies to \(f\). To spell out the passage from density to an open set, write its image as a finite union \(\bigcup_i(U_i\cap Z_i)\), with \(U_i\) open and \(Z_i\) closed in \(Y\). The finite union of the closures of these pieces is \(Y\). Irreducibility forces at least one piece to have closure \(Y\). For that piece \(Z_i=Y\), so it is the nonempty open set \(U_i\) contained in the image. \(\square\)

We now take \(\mathfrak g\) semisimple. In a basis, its automorphisms are the invertible matrices \(A\) satisfying
\[
A[u,v]=[Au,Av]
\quad\text{for all basis vectors }u,v.
\tag{3.1}
\]
These are finitely many polynomial equations inside \(\operatorname{GL}(\mathfrak g)\). Composition and inverse preserve them, so they define an affine algebraic group \(\operatorname{Aut}(\mathfrak g)\), also viewed as a group scheme by the same equations. Its tangent vectors at the identity have the form \(1+\varepsilon D\), \(\varepsilon^2=0\). Substitution in (3.1) gives exactly
\[
D[u,v]=[Du,v]+[u,Dv].
\]
Thus its tangent Lie algebra is \(\operatorname{Der}(\mathfrak g)=\operatorname{ad}\mathfrak g\), by the inner-derivation theorem previously proved. The zero centre makes \(\operatorname{ad}:\mathfrak g\to\operatorname{Der}(\mathfrak g)\) an isomorphism. Smoothness now gives
\[
\dim\operatorname{Aut}(\mathfrak g)^\circ=\dim\mathfrak g=N.
\tag{3.2}
\]

If \(D\) is a nilpotent derivation, its exponential is the finite polynomial
\[
\exp(sD)=\sum_{j\ge0}\frac{s^jD^j}{j!}.
\tag{3.3}
\]
Induction on the derivation rule gives
\(D^m[u,v]=\sum_{i=0}^m\binom mi[D^iu,D^{m-i}v]\).
Comparing each coefficient of \(s\) proves that (3.3) preserves brackets. Its inverse is \(\exp(-sD)\), and \(\exp(sD)\exp(tD)=\exp((s+t)D)\), by finite polynomial multiplication. Hence it defines a one-parameter subgroup, a morphism \(\mathbb A^1\to\operatorname{Aut}(\mathfrak g)\). Its connected image contains the identity and lies in the identity component.

Define \(\operatorname{Int}(\mathfrak g)\) to be the subgroup of complex automorphisms generated by \(\exp(\operatorname{ad}z)\) for all ad-nilpotent \(z\in\mathfrak g\). Scalar multiples of \(z\) are included, so it contains every point of each curve (3.3) with \(D=\operatorname{ad}z\).

**Theorem 3.2.**
\[
\operatorname{Int}(\mathfrak g)
=\operatorname{Aut}(\mathfrak g)^\circ(\mathbb C).
\tag{3.4}
\]
In particular, the inner automorphisms form the complex points of a connected affine algebraic group.

**Proof.** The one-parameter curves already give the inclusion from left to right. To prove the other, fix a maximal toral subalgebra \(\mathfrak h_0\). Every nonzero root vector is ad-nilpotent: its adjoint action shifts weights by its nonzero root, so a common sufficiently long iteration leaves the finite set of weights in the root decomposition.

Let \(S\) be the linear span of all \(\sigma(e)\), where \(e\) is a root vector for \(\mathfrak h_0\) and \(\sigma\in\operatorname{Int}(\mathfrak g)\). It contains every root space and is stable under \(\operatorname{Int}(\mathfrak g)\). For opposite root vectors \(e,f\), the polynomial curve \(\exp(s\operatorname{ad}f)e\) has all its values in \(S\). All its coefficients therefore belong to \(S\): evaluation at sufficiently many distinct scalars gives an invertible Vandermonde system for those coefficients. In particular \([f,e]\in S\). Opposite root brackets span \(\mathfrak h_0\), since they are nonzero multiples of the Killing-dual root vectors and the roots span \(\mathfrak h_0^*\). It follows that \(S=\mathfrak g\).

Choose a basis \(z_1,\ldots,z_N\) from the spanning set of actual conjugates of root vectors. Each \(z_i\) is ad-nilpotent. The polynomial map
\[
P:\mathbb A^N\longrightarrow\operatorname{Aut}(\mathfrak g)^\circ,
\qquad
(s_1,\ldots,s_N)\longmapsto
\prod_{i=1}^{N}\exp(s_i\operatorname{ad}z_i)
\tag{3.5}
\]
has differential at zero
\((s_i)\mapsto\operatorname{ad}(\sum_i s_i z_i)\). This is an isomorphism onto the tangent space in (3.2). Lemma 3.1 gives a nonempty open subset \(O\) of the identity component contained in \(P(\mathbb A^N)\), hence contained in \(\operatorname{Int}(\mathfrak g)\).

For any complex point \(g\) of the identity component, the two nonempty open sets \(O\) and \(gO\) meet, by irreducibility. Choose \(o_1=go_2\) in their intersection, with \(o_1,o_2\in O\). Then \(g=o_1o_2^{-1}\) belongs to \(\operatorname{Int}(\mathfrak g)\). This proves (3.4). For \(\mathfrak g=0\), the group and the empty product are both the identity, giving the same conclusion. \(\square\)

The proof establishes equality with the subgroup generated by the finite nilpotent exponentials themselves. Taking a Zariski closure of that subgroup would not by itself establish the required equality.

## 4. Each Cartan subalgebra reaches a dense open set

For a Cartan subalgebra \(\mathfrak h\), use the nonempty open set \(\mathfrak h^\circ\) from (2.3). Consider
\[
\varphi_{\mathfrak h}:
\operatorname{Int}(\mathfrak g)\times\mathfrak h^\circ
\longrightarrow\mathfrak g,
\qquad (\sigma,x)\longmapsto\sigma(x).
\tag{4.1}
\]
Here \(\operatorname{Int}(\mathfrak g)\) denotes the algebraic group identified in Theorem 3.2. Both source and target are smooth complex varieties. The evaluation map is regular. At \((1,x)\), its differential is
\[
d\varphi_{\mathfrak h}|_{(1,x)}:
\mathfrak g\oplus\mathfrak h\longrightarrow\mathfrak g,
\qquad (y,H)\longmapsto[y,x]+H.
\tag{4.2}
\]
The first summand uses the tangent identification \(y\mapsto\operatorname{ad}y\); differentiating evaluation gives the displayed bracket. Equation (2.4) makes (4.2) surjective. Lemma 3.1 therefore proves that the image of (4.1) contains a nonempty Zariski-open subset \(O_{\mathfrak h}\) of \(\mathfrak g\).

**Proposition 4.1.** Every Cartan subalgebra has dimension \(r_F(\mathfrak g)\), and
\[
\mathfrak h\cap\mathfrak g_{\mathrm{reg}}
=\mathfrak h^\circ.
\tag{4.3}
\]

**Proof.** The nonempty open set \(\mathfrak g_{\mathrm{reg}}=D(c_r)\) from Lemma 1.1 meets \(O_{\mathfrak h}\), because affine space is irreducible. A point of the intersection is \(\sigma(x)\) for \(x\in\mathfrak h^\circ\). Automorphisms intertwine adjoint operators, so
\[
r_F=n(\sigma(x))=n(x)=\dim\mathfrak h.
\tag{4.4}
\]
For any \(x\in\mathfrak h\), the root decomposition and semisimplicity give
\[
n(x)=\dim\mathfrak h+
\#\{\alpha\in\Phi:\alpha(x)=0\},
\tag{4.5}
\]
since root spaces are one-dimensional. Equality with the global minimum occurs exactly when no root vanishes, proving (4.3). \(\square\)

We may now call \(\mathfrak h^\circ\) the set \(\mathfrak h_{\mathrm{reg}}\). The common dimension is the **rank** of the semisimple algebra.

**Theorem 4.2 (Chevalley's conjugacy theorem).** Any two Cartan subalgebras of a complex semisimple Lie algebra are conjugate under \(\operatorname{Int}(\mathfrak g)\).

**Proof.** Let \(\mathfrak h,\mathfrak h'\) be Cartan subalgebras. The nonempty open sets \(O_{\mathfrak h}\) and \(O_{\mathfrak h'}\) meet. Write a point of their intersection as
\(y=\sigma(x)=\tau(x')\), where \(x\in\mathfrak h_{\mathrm{reg}}\) and \(x'\in\mathfrak h'_{\mathrm{reg}}\). The generalized zero space is transported by an automorphism, because
\(\operatorname{ad}(\sigma x)=\sigma\operatorname{ad}(x)\sigma^{-1}\). Thus
\[
\sigma(\mathfrak h)=\mathfrak g_0(y)
=\tau(\mathfrak h').
\]
The inner automorphism \(\tau^{-1}\sigma\) carries \(\mathfrak h\) onto \(\mathfrak h'\). \(\square\)

This proof does not assert that either saturation in (4.1) equals all of \(\mathfrak g\). Nilpotent elements already show why that stronger assertion would fail. Containing a dense open subset is enough to make the two saturations intersect.

## 5. What no longer depends on the chosen Cartan subalgebra

**Corollary 5.1.** The root systems defined by two Cartan subalgebras of a complex semisimple Lie algebra are isomorphic, and its rank is an invariant of the algebra.

**Proof.** Choose \(\sigma\in\operatorname{Int}(\mathfrak g)\) with \(\sigma\mathfrak h=\mathfrak h'\). The linear dual isomorphism
\[
\mathfrak h^*\longrightarrow(\mathfrak h')^*,
\qquad \alpha\longmapsto\alpha\circ\sigma^{-1}
\tag{5.1}
\]
sends roots to roots. Indeed, for \(v\in\mathfrak g_\alpha\) and \(H'\in\mathfrak h'\),
\[
[H',\sigma v]
=\sigma[\sigma^{-1}H',v]
=(\alpha\circ\sigma^{-1})(H')\sigma v.
\]
Applying \(\sigma^{-1}\) gives the converse and proves a bijection of root spaces. Adjoint matrices are conjugated, so their trace pairing, the Killing form, is preserved. The dual form and its Euclidean restriction to the real root span are therefore preserved by (5.1). Consequently all Cartan integers, reflections and root-system structure are preserved. The ranks agree also directly by \(\dim\mathfrak h=\dim\mathfrak h'\). The isomorphism exists; a choice of transporter has not supplied a distinguished unique identification. \(\square\)

For \(\mathfrak{sl}_n\), the Cartan statement can also be seen by linear algebra. An element is intrinsically semisimple exactly when its defining matrix is diagonalizable: one direction follows from diagonalizing its commutator action; the other follows from preservation of Jordan decomposition in the defining faithful representation, proved in [Complete reducibility: Casimir elements and Weyl's theorem](RT-LIE-04.md). Hence a Cartan subalgebra is a commuting family of diagonalizable traceless matrices. A common eigenbasis diagonalizes all of them, placing it inside the traceless diagonal algebra. Maximal torality forces equality.

The change-of-basis matrix can be taken in \(\operatorname{SL}_n\): rescale one basis vector to make its determinant 1, without changing the diagonal algebra. Such conjugation is inner in the definition of Section 3. For completeness, for \(n\ge2\), \(\operatorname{SL}_n(\mathbb C)\) is generated by the elementary transvections \(1+tE_{ij}\), \(i\ne j\). Row additions, with signed row interchanges when needed, reduce an invertible matrix to a diagonal one. The needed two-coordinate operations are products of transvections:
\[
w(t)=
\begin{pmatrix}1&t\\0&1\end{pmatrix}
\begin{pmatrix}1&0\\-t^{-1}&1\end{pmatrix}
\begin{pmatrix}1&t\\0&1\end{pmatrix}
=\begin{pmatrix}0&t\\-t^{-1}&0\end{pmatrix},
\quad
w(t)w(-1)=\begin{pmatrix}t&0\\0&t^{-1}\end{pmatrix}
\quad(t\ne0).
\tag{5.2}
\]
The first matrix supplies a signed interchange. A determinant-one diagonal matrix is a product of the second matrices on pairs of coordinates: pair each of the first \(n-1\) coordinates with the last. This proves the generation claim. Finally, conjugation by \(1+tE_{ij}=\exp(tE_{ij})\) is \(\exp(t\operatorname{ad}E_{ij})\), as follows by differentiating conjugation or by finite multiplication of the two exponentials. Thus all these conjugations belong to \(\operatorname{Int}(\mathfrak{sl}_n)\). For \(n=1\), the Lie algebra is zero and all assertions are immediate.

For a matrix \(x\) with distinct eigenvalues, its centralizer is the diagonal algebra in its eigenbasis, and its generalized adjoint zero space is the same algebra. The trace condition makes the rank of \(\mathfrak{sl}_n\) equal to \(n-1\). Repeated eigenvalues enlarge that generalized zero space, even when their eigenspaces have only one Jordan block.

The complex ground field is essential. In \(\mathfrak{sl}_2(\mathbb R)\), both \(\mathbb RH\), with \(H=\operatorname{diag}(1,-1)\), and \(\mathbb RJ\), with \(J=\left(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\right)\), are Cartan subalgebras: over \(\mathbb C\) each generator has two distinct eigenvalues, giving a one-dimensional centralizer. If \(z\) normalizes its line, \((\operatorname{ad}x)^2z=0\); semisimplicity of \(\operatorname{ad}x\) then gives \([x,z]=0\), so the normalizer is the same line. The Killing form is \(4\operatorname{tr}(XY)\). It has value 8 on \(H\) and \(-8\) on \(J\). A real automorphism preserves that form, so it cannot carry the positive line onto the negative line. They are not conjugate even under all real automorphisms.

They exhaust the real classes. The centralizer and dimension argument in Exercise 6.1 works over \(\mathbb R\), so a real Cartan subalgebra is a line \(\mathbb Rx\), with \(\det x\ne0\); a nonzero nilpotent line has a larger normalizer. If \(\det x<0\), its two distinct real eigenvalues give the diagonal line. If \(\det x=b^2>0\), then \(x^2=-b^2 1\), and for any nonzero real \(v\), the vectors \(v,xv/b\) are independent. In that basis \(x=bJ\), giving the other line. These changes of basis can be made determinant one. In the diagonal case rescale an eigenvector. In the elliptic case replace the chosen generator by its negative if necessary to make the basis positively oriented, then rescale both basis vectors by the same positive scalar to make the determinant 1. Formula (5.2) works over \(\mathbb R\) as well. Thus there are exactly two classes under conjugation by real \(\operatorname{SL}_2\), and they remain distinct under all real automorphisms.

## 6. Exercises with complete solutions

**Exercise 6.1 (easy).** Show directly that all Cartan subalgebras of \(\mathfrak{sl}_2(\mathbb C)\) are conjugate by inner automorphisms, without using Theorem 4.2.

**Solution.** For a nonzero traceless \(2\times2\) matrix \(x\), its centralizer in \(\mathfrak{sl}_2\) is \(\mathbb Cx\). To verify this, \(x\) is nonscalar, so some vector \(v\) makes \(v,xv\) independent. Otherwise every line would be invariant, and applying \(x\) to two basis vectors and their sum would make \(x\) scalar. An operator commuting with \(x\) is determined by its value \(pv+qxv\) on \(v\); on the whole basis it therefore equals \(p1+qx\). Tracelessness gives \(p=0\).

A two-dimensional nilpotent Lie algebra is abelian: its centre is nonzero by Engel, and if the centre is one-dimensional, the one-dimensional quotient leaves just one noncentral basis vector, so every bracket is still zero. Thus a nilpotent two-dimensional subalgebra of \(\mathfrak{sl}_2\) would be abelian, contradicting the centralizer calculation. The whole \(\mathfrak{sl}_2\) is not nilpotent, since \(\operatorname{ad}H\) has nonzero eigenvalues. The zero subalgebra has normalizer the whole algebra. A Cartan subalgebra must consequently be a line \(\mathbb Cx\).

The identity \(x^2=-\det(x)1\) splits the possibilities. If \(\det x=0\), then \(x\) is nonzero nilpotent and a Jordan basis conjugates its line to \(\mathbb Ce\). This line has larger normalizer, since \([H,e]=2e\), so it is not Cartan. If \(\det x\ne0\), the eigenvalues are the distinct numbers \(\lambda,-\lambda\), \(\lambda\ne0\), and an eigenbasis conjugates its line to \(\mathbb CH\). This line is self-normalizing: for \(z=aH+be+cf\), the condition \([z,H]\in\mathbb CH\) gives \(b=c=0\). It is abelian, hence Cartan.

Rescale one eigenvector to give the change-of-basis matrix determinant 1. Equation (5.2) and row reduction express it as a product of transvections. Their conjugations are finite exponentials of ad-nilpotent elements, so the transporter is inner as defined here. Every Cartan line is thus inner-conjugate to \(\mathbb CH\).

**Exercise 6.2 (medium).** Determine the regular elements of \(\mathfrak{sl}_3(\mathbb C)\) and their generalized adjoint zero spaces. Also identify the centralizer-regular elements, so that the two conventions can be compared.

**Solution.** Decompose the defining space into generalized eigenspaces,
\(\mathbb C^3=\bigoplus_\lambda V_\lambda\), with \(m_\lambda=\dim V_\lambda\), and write \(x|_{V_\lambda}=\lambda1+N_\lambda\). On \(\operatorname{Hom}(V_\mu,V_\lambda)\),
\[
\operatorname{ad}x=(\lambda-\mu)1+K,
\qquad K(Z)=N_\lambda Z-ZN_\mu.
\tag{6.1}
\]
The two multiplication operators in \(K\) commute and are nilpotent. Expanding their difference to the power \(m_\lambda+m_\mu-1\) shows that \(K\) is nilpotent. If \(\lambda\ne\mu\), (6.1) is invertible by a finite geometric series. If \(\lambda=\mu\), it is nilpotent. Therefore
\[
\mathfrak g_0(x)
=\left(\bigoplus_\lambda\operatorname{End}(V_\lambda)\right)
\cap\mathfrak{sl}_3,
\qquad
n(x)=\sum_\lambda m_\lambda^2-1.
\tag{6.2}
\]
The trace condition subtracts one dimension because the trace functional is nonzero on the block-diagonal algebra. These are block-diagonal spaces for the generalized eigenspace decomposition, regardless of the Jordan blocks inside each \(V_\lambda\).

Here is the exhaustive list up to matrix conjugacy. A subscript in \(J_k(a)\) is the size of a Jordan block. In the two-eigenvalue rows, \(a\ne0\), so \(a\) and \(-2a\) are distinct.

| Jordan type of \(x\) | \(\mathfrak g_0(x)\) | \(n(x)\) | \(\dim C_{\mathfrak g}(x)\) |
|---|---|---:|---:|
| Three distinct eigenvalues with sum zero | Traceless diagonal matrices in an eigenbasis | 2 | 2 |
| \(\operatorname{diag}(a,a,-2a)\) | \(\{\operatorname{diag}(A,c):\operatorname{tr}A+c=0\}\) | 4 | 4 |
| \(J_2(a)\oplus(-2a)\) | The same block-diagonal space | 4 | 2 |
| \(J_3(0)=N\) | \(\mathfrak{sl}_3\) | 8 | 2 |
| \(J_2(0)\oplus0\) | \(\mathfrak{sl}_3\) | 8 | 4 |
| \(0\) | \(\mathfrak{sl}_3\) | 8 | 8 |

To justify every centralizer entry, different-eigenvalue blocks of a commuting matrix vanish by the invertibility in (6.1). A scalar two-dimensional block has arbitrary \(2\times2\) centralizer. A single size-two Jordan block has centralizer \(\mathbb C1+\mathbb CN\), by the cyclic-basis argument from Exercise 6.1. Adding the scalar block and imposing trace zero gives the dimensions 4 and 2 in the second and third rows.

For a size-three Jordan block, a cyclic vector shows that every commuting matrix is \(p1+qN+rN^2\): its value on that vector determines its values on the cyclic basis. Trace zero removes \(p\), giving dimension 2. For the size-two block plus zero, take \(N=E_{12}\). Direct multiplication gives
\[
C_{\mathfrak{sl}_3}(N)
=\left\{
\begin{pmatrix}a&b&c\\0&a&0\\0&d&-2a\end{pmatrix}
:a,b,c,d\in\mathbb C\right\},
\tag{6.3}
\]
of dimension 4. The zero matrix commutes with the entire algebra. This proves all six entries.

The smallest Fitting dimension is 2. Thus the regular elements in the lesson's convention are exactly the matrices with three distinct eigenvalues; they are semisimple, and their generalized zero spaces are Cartan subalgebras. The smallest ordinary centralizer dimension is also 2, but its minimizers include two additional types: \(J_2(a)\oplus(-2a)\) and \(J_3(0)\). Their generalized zero spaces have dimensions 4 and 8 and are not Cartan subalgebras. This explains why Proposition 1.2 cannot be applied with the centralizer definition substituted into its hypothesis.

One polynomial describes the first locus. The characteristic polynomial of a traceless \(3\times3\) matrix is
\[
\det(t1-x)=t^3-\tfrac12\operatorname{tr}(x^2)t
-\tfrac13\operatorname{tr}(x^3).
\]
Indeed, the second and third elementary symmetric functions of its eigenvalues are \(-\tfrac12\sum\lambda_i^2\) and \(\tfrac13\sum\lambda_i^3\), by \(\sum\lambda_i=0\). The product of squared pairwise differences is
\[
\Delta(x)=\tfrac12(\operatorname{tr}x^2)^3
-3(\operatorname{tr}x^3)^2.
\tag{6.4}
\]
This follows by expanding \(\prod_{i<j}(\lambda_i-\lambda_j)^2\) with \(\lambda_3=-\lambda_1-\lambda_2\); both sides give the same polynomial. Thus the Fitting-regular locus is precisely \(D(\Delta)\). Formula (6.2) remains valid on its complement and describes all the enlarged zero spaces there.

**Exercise 6.3 (medium).** Prove \(\mathfrak g=\mathfrak h\oplus[\mathfrak g,x]\) for a Cartan subalgebra \(\mathfrak h\) of a complex semisimple algebra and \(x\in\mathfrak h\) regular.

**Solution.** Proposition 4.1 says that \(\alpha(x)\ne0\) for every root. For an arbitrary vector \(v=H+\sum_\alpha v_\alpha\) in its root decomposition, set
\[
y=-\sum_\alpha\frac{v_\alpha}{\alpha(x)}.
\]
Then \([y,x]=\sum_\alpha v_\alpha\), so \(v=H+[y,x]\). Conversely every bracket \([z,x]\) has zero \(\mathfrak h\)-component, since \([\mathfrak h,x]=0\) and brackets on a root space are \(-\alpha(x)\) times that space. Thus the sum is direct. This also computes the surjective differential in (4.2), including its sign.

**Exercise 6.4 (hard).** Prove the following proposition in both its parts: the Fitting nullspace of a regular element of any complex Lie algebra is Cartan; in a complex semisimple algebra, Cartan subalgebras are exactly maximal toral subalgebras.

**Solution.** Let \(x\) be regular and put \(H=\ker(\operatorname{ad}x)^N\), \(V=\operatorname{im}(\operatorname{ad}x)^N\). The binomial derivation formula (1.3) proves \([H,H]\subseteq H\) and \([H,V]\subseteq V\). For \(b\in H\), the operator \(\operatorname{ad}(x+sb)|_V\) is invertible away from finitely many scalars \(s\). At those scalars, minimality of \(\dim H\) forces the characteristic polynomial on \(H\) to be \(t^{\dim H}\). Polynomial dependence extends this identity to every \(s\); the highest \(s\)-coefficients of the characteristic coefficients give \(\det(t1_H-\operatorname{ad}b|_H)=t^{\dim H}\). Engel makes \(H\) nilpotent. If \(z\) normalizes \(H\), then \([x,z]\in H\), so \((\operatorname{ad}x)^{N+1}z=0\), and hence \(z\in H\) by the stabilized Fitting decomposition. Thus \(H\) is self-normalizing.

Now let \(\mathfrak a\) be any Cartan subalgebra of semisimple \(\mathfrak g\). Lemma 2.1, whose proof uses only Lie's flag and Engel on a quotient, supplies \(a\in\mathfrak a\) with \(\mathfrak g_0(a)=\mathfrak a\). The Killing form pairs that generalized zero summand orthogonally with every nonzero summand: if \(D=\operatorname{ad}a\), \(D^mu=0\), and \(v=D^mw\) in a nonzero summand, then \(\kappa(u,v)=(-1)^m\kappa(D^mu,w)=0\). Its restriction to \(\mathfrak a\) is therefore nondegenerate.

Triangularity of the adjoint action of the solvable \(\mathfrak a\) makes the action of \([\mathfrak a,\mathfrak a]\) strictly triangular, giving \(\kappa(\mathfrak a,[\mathfrak a,\mathfrak a])=0\). Thus \(\mathfrak a\) is abelian. The Jordan parts of \(x\in\mathfrak a\) centralize \(\mathfrak a\) and lie in its normalizer, hence in \(\mathfrak a\). For its nilpotent part, \(\operatorname{ad}x_n\operatorname{ad}y\) is a commuting nilpotent product for every \(y\in\mathfrak a\); all its traces vanish. Nondegeneracy gives \(x_n=0\). Therefore \(\mathfrak a\) is toral, and self-normalization makes it maximal toral.

Conversely a maximal toral \(\mathfrak h\) has the root decomposition (2.2). It is abelian and hence nilpotent. A normalizing vector's nonzero root components must vanish, since each nonzero root has some \(H\) with \(\alpha(H)\ne0\). Its normalizer is exactly \(\mathfrak h\). This proves the second part without invoking Theorem 2.2 or conjugacy as an unproved step.

## 7. What this lesson does not prove

Engel, Lie, the semisimple inner-derivation and Jordan theorems, and the maximal-toral root decomposition are the previously proved imports named at the start. The defining-representation Jordan compatibility used for \(\mathfrak{sl}_n\) is the precise additional import from the complete-reducibility lesson, Theorem 5.1.

The general algebraic geometry theorems in Section 3 are proved in the linked programme lessons: Cartier smoothness, identity components, the differential criterion and openness for smooth morphisms, and Chevalley constructibility. Their stated hypotheses are retained, and those proof providers are prerequisites rather than results reproved in this lesson. Lemma 3.1 proves the particular density consequence; Theorem 3.2 proves the required group identity, rather than importing it. The bridge course provides Zariski topology and affine-variety background, not a claimed proof of all these algebraic-group results.

All new Lie-algebra assertions, the conjugacy theorem and every exercise are proved here. General Leibniz algebras, group-scheme maximal tori over arbitrary fields and compact-group conjugacy are source comparisons or later topics, not prerequisites for this proof. No compact real form, Serre presentation or Chevalley basis has been assumed. A reader who accepts Corollary 5.1 may postpone this lesson until after the Serre-presentation lesson; the proof given here has no dependency on that later construction.

## References

- **[Kirillov]** A. Kirillov Jr., *Introduction to Lie Groups and Lie Algebras*, author-hosted notes, §§6.5 and 6.7, pp.97–98 and102–104, especially Definitions 6.48–6.49 and Corollary 6.54. These use the same generalized-zero regularity. The notes also give an analytic conjugacy argument; our proof uses constructible images and polynomial nilpotent exponentials. [Author's notes](https://www.math.stonybrook.edu/~kirillov/liegroups/liegroups.pdf).
- **[Milne]** J. S. Milne, *Algebraic Groups: The Theory of Group Schemes of Finite Type over a Field*, corrected 2021 text, published 2022: Proposition 1.34 and Corollary 1.35, p.17; Theorem 3.23, p.71; Appendix A.69 and A.71, p.586. For the group analogues, §17b, especially Theorem 17.10, p.355, and §17j, pp.376–382, especially Theorem 17.87, p.380. Over an arbitrary field the latter gives conjugacy only after a finite separable extension, not necessarily over the original field. [Author's corrected 2021 edition](https://www.jmilne.org/math/Books/iAG2022.pdf).
- **[Brenner]** H. Brenner, *Algebraische Kurven*, Osnabrück 2025–2026, Lecture 3, Zariski topology, and Lecture 4, irreducible affine algebraic sets. These are original sources for the algebraic-geometry bridge background. [Original course](https://de.wikiversity.org/wiki/Kurs:Algebraische_Kurven_(Osnabr%C3%BCck_2025-2026)).
- **[Stacks]** The Stacks project, Tags 054K and 00FE, as linked to the AI Integrated Stacks Project English reader in Section 3. These concern constructible images; they are different from Chevalley's Cartan-conjugacy theorem proved in Theorem 4.2.
