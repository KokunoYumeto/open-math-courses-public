# The function-field case: Drinfeld and L. Lafforgue

*Draft lesson. Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Public domain (CC0).*

For a function field, places are points of a curve and integral lattices glue into vector bundles. This changes the language of automorphic forms without changing their arithmetic meaning. We use this dictionary to prove a complete vanishing result for the projective line, then compare it with the Galois side. The deep correspondence theorems are stated, with their scope distinguished from the elementary arguments proved here.

Let \(X\) be a smooth projective geometrically connected curve over \(k=\mathbf F_q\), let \(F=k(X)\), and let \(\mathbf A\) be its ring of adèles. At a closed point \(v\), write \(R_v=\mathcal O_{X,v}\), \(F_v\) for the completion and \(\mathcal O_v\) for its valuation ring. Put \(\mathcal O=\prod_v\mathcal O_v\). The dictionary and the finite-cover argument are proved below. For coherent cohomology we use the earlier programme proofs in *Čech cohomology*, Theorem 3.2, *Cohomology of affine schemes and Serre's criterion*, Theorems 2.2 and 3.1, and *Coherent sheaves on projective schemes: Serre's theorems*, Theorem 2.2. These prove the affine-cover calculation and finite-dimensionality used here. The correspondence statements are taken from the freely accessible texts of L. and V. Lafforgue specified below.

## 1. Bundles and the constant term

Weil's dictionary identifies

\[
GL_n(F)\backslash GL_n(\mathbf A)/GL_n(\mathcal O)
\]

with isomorphism classes of rank-\(n\) vector bundles on \(X\). Here is the lattice construction, including why completed local data give an algebraic bundle.

For \(g=(g_v)\in GL_n(\mathbf A)\), put \(\Lambda_v=g_v\mathcal O_v^n\). These lattices equal \(\mathcal O_v^n\) outside a finite set \(S\). Since \(F\) is dense in its completion \(F_v\), approximate the entries of \(g_v\) by a matrix \(h_v\in M_n(F)\) closely enough that
\[
g_v^{-1}h_v\in I_n+\mathfrak m_vM_n(\mathcal O_v)
\subset GL_n(\mathcal O_v).
\]
Thus \(h_v\in GL_n(F)\) and \(h_v\mathcal O_v^n=\Lambda_v\). The local ring \(R_v\) is a DVR, and \(F\cap\mathcal O_v=R_v\); hence
\[
F^n\cap\Lambda_v=h_vR_v^n.
\tag{1.1}
\]
The DVR assertion and the finite torsion-free module argument are proved in *Projective cohomology and smooth affine models*, Lemma 6.C and §6.

Trivialize on \(U_0=X\setminus S\). For each \(v\in S\), choose an open \(U_v\) containing \(v\), excluding the other points of \(S\) and every other zero or pole of the finitely many entries needed for \(h_v,h_v^{-1}\). On \(U_v\setminus\{v\}\) both matrices are regular. Glue a free bundle on \(U_v\) to the trivial bundle on \(U_0\) by the matrix \(h_v\). On \(U_v\cap U_w\), the transition is \(h_w^{-1}h_v\); the matrix products satisfy the cocycle equation. A section, in the common rational frame, is therefore exactly a rational vector integral in \(\Lambda_v\) at every point of its open domain. Formula (1.1) shows that the resulting completed stalk is \(\Lambda_v\). It also shows independence of the approximating matrices and opens: two such constructions have identical local fractional modules inside \(F^n\).

Conversely, a basis of a bundle's generic fibre trivializes it on a nonempty open: spread the finitely many basis sections and their inverse frame to that open. Its complement is a finite set of closed points. At each remaining point a local frame gives an \(R_v\)-lattice, whose completion is \(g_v\mathcal O_v^n\); choose \(g_v=I_n\) elsewhere. The preceding construction recovers the bundle because its stalks recover those lattices. An isomorphism of two bundles is generically a matrix \(a\in GL_n(F)\) and carries each completed lattice to the other. Conversely, such a matrix carries their \(R_v\)-lattices to one another by (1.1), so it extends to an isomorphism. Finally, two matrices give the same local lattice precisely when they differ on the right by \(GL_n(\mathcal O_v)\). This proves the double-coset dictionary. Frenkel's freely accessible preprint, §3.2, gives its geometric interpretation.

An unramified automorphic function can therefore be written \(f(E)\). For \(GL_2\), cusp forms satisfy

\[
\int_{F\backslash\mathbf A}f\left(
\begin{pmatrix}1&u\\0&1\end{pmatrix}g\right)\,du=0
\qquad(g\in GL_2(\mathbf A)).
\]

The additive quotient is compact; the principal-parts calculation below proves this at the same time as the extension formula. Normalize its Haar measure to have total mass one. This is the upper-triangular constant term with left rational invariance and right integral invariance. In [Stacks, Tag 03VR] the invariances and unipotent action are on the opposite sides. Replacing the source function \(h(g)\) by \(f(g)=h(g^{-1})\), and replacing the integration variable by its negative, gives exactly our convention.

Fix line bundles \(L,M\). Upper-triangular gluing data with these diagonal bundles describe extensions

\[
0\longrightarrow L\longrightarrow E\longrightarrow M\longrightarrow0.
\]

Their equivalence classes, fixing the two ends, are

\[
\operatorname{Ext}^1(M,L)=H^1(X,L\otimes M^{-1}).
\]

To prove the cohomology identification, choose a finite affine cover trivializing the ends. The sequence splits on each member: its quotient module is free, so lift a basis. Differences of splittings are sections of \(A=L\otimes M^{-1}\), satisfying the Čech cocycle equation. Conversely these cocycles glue \(L\oplus M\) to an extension. Changing splittings adds a coboundary; extension isomorphisms fixing the ends give exactly those changes. The affine-cover theorem quoted above identifies this quotient with \(H^1(X,A)\). The same proof works for a vector-bundle quotient \(Q\), replacing \(A\) by \(\mathcal H om(Q,L)\).

We can also identify the adèlic quotient explicitly. Choose a rational frame of \(A\), and write its completed lattice as \(A_v=c_v\mathcal O_v\subset F_v\). Let \(\mathcal K_A\) be the sheaf of rational sections, with value \(F\) on each nonempty open. It is flasque, since its restriction maps are identities. There is an exact sequence
\[
0\longrightarrow A\longrightarrow\mathcal K_A
\longrightarrow\bigoplus_{v\in|X|}i_{v*}(F_v/A_v)
\longrightarrow0.
\tag{1.2}
\]
Here \(i_v\) includes the closed point. At \(v\), the quotient is \(F/A_{R_v}\), and density identifies this with \(F_v/A_v\): every principal part has a rational representative, and its kernel is precisely the local lattice. At every other stalk the corresponding skyscraper is zero. Rational sections have only finitely many poles, so the map lands in the direct sum. These observations prove exactness stalkwise. On a Noetherian open, a section of the direct sum has finite support, and restriction just discards points. Consequently this sheaf is flasque too. The long exact sequence gives
\[
H^1(X,A)=\mathbf A\big/\left(F+\prod_v A_v\right).
\tag{1.3}
\]
Indeed quotienting the restricted product by its lattices gives exactly the finite-support principal parts in (1.2). The quotient is finite because coherent cohomology is finite-dimensional over the finite field \(k\).

For diagonal representatives \(g=\operatorname{diag}(\ell_v,m_v)_v\) of \(L,M\), the local lattice of \(A\) is \((\ell_v/m_v)\mathcal O_v\). A generic splitting of an extension and an integral splitting at \(v\) differ by an element \(u_v\in F_v\). They agree integrally at almost all points, so \(u\) is an adèle. Changing the generic splitting adds an element of \(F\); changing integral splittings adds \(\prod_v A_v\). Conversely the upper-triangular lattices of \(n(u)g\) glue to that extension by the proved dictionary. This identifies (1.3) with the extension classes, including the rational and integral equivalences used in the constant term.

Taking \(A=\mathcal O_X\) in (1.3) makes \(\mathbf A/(F+\mathcal O)\) finite. The group \(\mathcal O\) is compact, since each \(\mathcal O_v\) is the inverse limit of the finite rings \(R_v/\mathfrak m_v^r\). The diagonal \(F\) is discrete: a rational function integral everywhere is in \(k\), as proved below, and requiring positive valuation at one point removes every nonzero constant. A discrete subgroup of a Hausdorff topological group is closed: choose a neighbourhood whose difference meets the subgroup only at zero; every translate then meets the subgroup in at most one point, which also excludes any new closure point. Thus \(\mathbf A/F\) is a Hausdorff quotient, covered by finitely many translates of the compact image of \(\mathcal O\), and is compact.

**Lemma 1.1 (constant-term vanishing).** Suppose \(E\) has a line subbundle \(L\), with line-bundle quotient \(M\), and

\[
H^1(X,L\otimes M^{-1})=0.
\]

Every unramified cusp form on \(GL_2(\mathbf A)\) vanishes at \(E\).

*Proof.* The extension group is zero, so \(E\cong L\oplus M\). Choose a diagonal adèle \(g\) representing the two summands. For every \(u\in\mathbf A\), the upper-triangular adèle in the constant term represents an extension of \(M\) by \(L\). Every such extension splits, so every underlying bundle is isomorphic to \(E\). Rational and integral invariance make the integrand the constant value \(f(E)\). The integral equals \(f(E)\) under our normalization, and cuspidality makes it zero. \(\square\)

The argument does not require counting bundles with automorphism weights: all extension classes have already collapsed to a single underlying bundle. Nor does it assert that every split bundle on every curve has zero value. The cohomology condition is essential.

## 2. A splitting theorem from maximal line subbundles

We first record the small cohomology calculation that drives the proof. Use the affine cover of \(\mathbf P^1_k\) with coordinates \(t\) and \(t^{-1}\). With compatible frames for \(\mathcal O(n)\), the first Čech cohomology is

\[
H^1(\mathbf P^1,\mathcal O(n))
=k[t,t^{-1}]\big/\bigl(k[t]+t^n k[t^{-1}]\bigr).
\]

When \(n\leq-2\), the surviving monomials are \(t^{n+1},\ldots,t^{-1}\); when \(n\geq-1\), there are none. A global section is a polynomial whose exponents lie between zero and \(n\). Hence

\[
h^0(\mathcal O(n))=\max(n+1,0),\qquad
h^1(\mathcal O(n))=\max(-n-1,0).
\]

These calculations hold over any field. The cover is affine with affine intersection, so Čech cohomology computes coherent cohomology here.

Every line bundle on \(\mathbf P^1_k\) is \(\mathcal O(n)\) for a unique integer \(n\). For completeness, choose a nonzero rational section and take its divisor. A closed point of the affine line is defined by an irreducible polynomial \(P(t)\); the divisor of \(P\) is that point minus \((\deg P)\infty\). Thus every divisor is linearly equivalent to its degree times \(\infty\). Uniqueness follows from the degree of a principal divisor being zero.

**Theorem 2.1 (Grothendieck splitting theorem, 1957).** Every vector bundle \(E\) on \(\mathbf P^1_k\) is isomorphic to

\[
\mathcal O(a_1)\oplus\cdots\oplus\mathcal O(a_r).
\]

The multiset of integers is uniquely determined by \(E\).

*Proof.* We prove existence by induction on \(r\). For positive rank, there is a largest integer \(a\) for which \(H^0(E(-a))\ne0\). Here is both existence and boundedness, without assuming a splitting theorem. A nonzero rational section has finitely many poles; twisting by their effective divisor makes it regular, so some twist has a section. Conversely, choose a rational basis of the dual bundle. After clearing all poles by one effective divisor \(D\), this gives a generically injective map

\[
E\longrightarrow\mathcal O(D)^r\cong\mathcal O(m)^r.
\]

Its kernel is zero because a vector bundle on an integral curve has no torsion subsheaf. Therefore \(H^0(E(-a))\) injects into \(H^0(\mathcal O(m-a)^r)\), which vanishes for \(a>m\).

A nonzero section in the maximal twist gives \(\mathcal O(a)\to E\). Saturate its image. On a smooth curve a torsion-free sheaf is locally free; the saturation is a line subbundle \(L\), and its quotient in \(E\) is a vector bundle. If the original section has a zero divisor \(D'\), then \(L\cong\mathcal O(a)(D')\cong\mathcal O(a+\deg D')\). Maximality of \(a\) forces \(D'=0\). We obtain

\[
0\longrightarrow\mathcal O(a)\longrightarrow E\longrightarrow Q\longrightarrow0.
\]

By induction \(Q=\bigoplus_i\mathcal O(b_i)\). Twist the sequence by \(\mathcal O(-a-1)\). Both \(H^0(E(-a-1))\) and \(H^1(\mathcal O(-1))\) vanish. The long exact sequence therefore gives \(H^0(Q(-a-1))=0\). The explicit line-bundle calculation implies \(b_i\leq a\) for every \(i\).

Finally,

\[
\operatorname{Ext}^1(Q,\mathcal O(a))
=\bigoplus_i H^1(\mathcal O(a-b_i))=0.
\]

The sequence splits, completing the induction.

For uniqueness, let \(h_E(m)=\dim H^0(E(m))\). A splitting gives

\[
h_E(m)-h_E(m-1)=\#\{i:a_i+m\geq0\}.
\]

The difference of these counts at consecutive integers recovers the number of summands of each degree. Since \(h_E\) depends only on \(E\), so does the multiset. \(\square\)

The proof uses the cohomology of \(\mathcal O(-1)\) at a specific point: it prevents the quotient from having a summand of degree larger than the maximal line subbundle. Merely taking a maximal line subbundle and declaring the extension split would miss this step.

## 3. The automorphic and Galois vanishing statements

**Corollary 3.1.** For \(F=\mathbf F_q(t)\), every \(GL_2(\mathcal O)\)-invariant cusp form vanishes identically.

*Proof.* Every rank-two bundle is \(\mathcal O(a)\oplus\mathcal O(b)\) with \(a\geq b\). Take \(L=\mathcal O(a)\), \(M=\mathcal O(b)\). Then \(H^1(LM^{-1})=H^1(\mathcal O(a-b))=0\). Lemma 1.1 gives vanishing at every bundle, and Weil's dictionary gives vanishing at every double coset. \(\square\)

This statement concerns everywhere unramified cusp forms. It does not exclude cusp forms with ramification at selected points of the projective line.

**Proposition 3.2.** Over \(\overline{\mathbf F}_q\), the projective line has no connected finite étale cover of degree greater than one. Consequently an everywhere unramified continuous irreducible \(\overline{\mathbf Q}_\ell\)-representation of \(G_{\mathbf F_q(t)}\), defined over a finite extension of \(\mathbf Q_\ell\), has dimension one; here \(\ell\ne\operatorname{char}(k)\).

*Proof.* First work over any algebraically closed field. Let \(f:Y\to\mathbf P^1\) be connected, finite étale, of degree \(d\). Its source is a smooth proper curve. A connected smooth curve over this field is integral: its regular local rings are domains, so different irreducible components cannot meet; the finitely many components are therefore open and closed. Every global regular function on \(Y\) is constant. Indeed it defines a map \(Y\to\mathbf A^1\subset\mathbf P^1\). The map to \(\mathbf P^1\) is proper: its graph is closed because \(\mathbf P^1\) is separated, and the projection from \(Y\times\mathbf P^1\) is a base change of the proper map \(Y\to\operatorname{Spec}k\). Its image is thus closed and irreducible. If the function were nonconstant, the image would be all of \(\mathbf P^1\), contradicting omission of infinity. Hence
\[
H^0(Y,\mathcal O_Y)=k.
\tag{3.1}
\]

The finite étale algebra \(E=f_*\mathcal O_Y\) is a vector bundle of rank \(d\). Its trace pairing
\[
E\otimes E\longrightarrow\mathcal O_{\mathbf P^1},
\qquad a\otimes b\longmapsto\operatorname{Tr}(ab)
\tag{3.2}
\]
is perfect. To check this at a geometric point, a finite étale fibre is a product of \(d\) copies of its algebraically closed residue field. Multiplication is coordinatewise, and its trace pairing is \(\sum_{j=1}^d a_jb_j\). Its determinant is one. A matrix between equal-rank free local modules whose determinant is nonzero modulo the maximal ideal is invertible, proving perfection everywhere. Thus \(E\cong E^\vee\), even when the characteristic divides \(d\).

By Theorem 2.1 write \(E=\bigoplus_j\mathcal O(a_j)\). Uniqueness of the splitting and self-duality give equality of the multisets \(\{a_j\}=\{-a_j\}\). On the other hand, (3.1) gives
\[
1=h^0(\mathbf P^1,E)=\sum_j\max(a_j+1,0).
\tag{3.3}
\]
A positive \(a_j\) would contribute at least two. There can therefore be no positive degree, and symmetry rules out every negative degree too. All \(a_j=0\), so (3.3) says \(d=1\). A finite étale algebra of rank one equals the base algebra: its unit is a basis on every fibre and hence locally a basis. Thus the cover is an isomorphism.

Next let \(k=\mathbf F_q\) and allow any finite étale cover \(Y\to\mathbf P^1_k\). After base change to \(\bar k\), each connected component is a copy of \(\mathbf P^1_{\bar k}\) over the base, by what we have just proved. All these isomorphisms and their inverses descend to some finite extension \(K/k\): on the two affine charts their ring maps involve only finitely many algebraic coefficients. Let \(S\) be the finite set of components over \(K\) and \(\Gamma=\operatorname{Gal}(K/k)\). The descent action permutes \(S\). A map from one copy of \(\mathbf P^1_K\) to another **over** \(\mathbf P^1_K\) is forced to be the identity on the base coordinate. Thus the action on each chart algebra \(K[t]^S\) is precisely coefficientwise Galois action combined with that permutation.

Put \(B=(K^S)^\Gamma\). On an orbit of \(S\), choose \(s\) with stabilizer \(H\subset\Gamma\). An invariant tuple is determined by its coordinate at \(s\), which lies in \(K^H\); all other coordinates are its conjugates. Consequently \(B\) is a product of finite separable extensions \(K^H/k\). Also
\[
B\otimes_kK\cong K^S:
\]
on each orbit this is the familiar separable splitting of \(K^H\otimes_kK\), obtained by factoring its primitive element's distinct conjugates and applying the Chinese remainder theorem. Polynomial coefficients can be compared separately, so
\[
(K[t]^S)^\Gamma=B\otimes_k k[t],\qquad
(K[t^{-1}]^S)^\Gamma=B\otimes_k k[t^{-1}].
\tag{3.4}
\]
For any \(k\)-algebra \(C\), \((C\otimes_kK)^\Gamma=C\): expand an element in a \(k\)-basis of \(C\) and use \(K^\Gamma=k\) for each coefficient. Apply this to the original cover's finite chart algebras. Formula (3.4), with the identical calculation on \(k[t,t^{-1}]\), identifies and glues them to give
\[
Y\cong\mathbf P^1_k\times_k\operatorname{Spec}B.
\tag{3.5}
\]
This proves finite-cover descent here directly. In particular, connected covers are exactly the constant-field covers \(\mathbf P^1_{\mathbf F_{q^r}}\). Maps between them are the maps of their finite fields. Equivalently the category of finite covers, with its geometric fibre functor, is the category of finite continuous \(G_k\)-sets. By the definition of the étale fundamental group as the automorphism group of that functor,
\[
\pi_1(\mathbf P^1_k)\cong G_k\cong\widehat{\mathbf Z}.
\tag{3.6}
\]
The last isomorphism follows because the finite extensions of \(\mathbf F_q\) are \(\mathbf F_{q^r}\), with cyclic Galois group generated by \(x\mapsto x^q\), and taking their inverse limit gives \(\widehat{\mathbf Z}\).

We spell out why killing all inertia puts a finite Galois quotient among these covers. For a finite separable extension \(L/F\), normalize each chart \(R=k[t]\) or \(k[t^{-1}]\) in \(L\). Its integral closure is finite: scale a primitive field generator to an integral element \(\theta\). The order \(R[\theta]\) is a finite free lattice with nondegenerate field trace pairing. To see nondegeneracy, extend scalars to an algebraic closure of \(F\): the primitive element's separable polynomial factors into distinct linear factors, so the Chinese remainder theorem identifies the algebra with a product of fields and its trace pairing with the coordinate dot product. Every integral element \(b\) of \(L\) lies in the order's trace-dual lattice, since \(\operatorname{Tr}(b\theta^j)\) is both integral over \(R\) and in \(F\), hence in the integrally closed ring \(R\). The trace-dual lattice is finite free, and its submodules are finite because \(R\) is Noetherian. Integral closure commutes with localization: multiply an integral equation's root by a large enough power of a denominator to obtain a monic equation over \(R\). The two finite normalizations therefore glue.

For clarity, the normal local rings of this normalization are DVRs. In a one-dimensional Noetherian normal local domain \(A\) with maximal ideal \(\mathfrak m\), choose \(0\ne a\in\mathfrak m\). Some power \(\mathfrak m^r\) lies in \(aA\). For the least such \(r\), choose \(b\in\mathfrak m^{r-1}\setminus aA\) and put \(x=b/a\). Then \(x\notin A\) but \(x\mathfrak m\subset A\). If \(x\mathfrak m\subset\mathfrak m\), a finite generating set of \(\mathfrak m\) and the determinant trick give a monic polynomial for \(x\): write multiplication by \(x\) as a matrix on those generators and apply its characteristic polynomial to a nonzero generator. Normality would give \(x\in A\), a contradiction. Thus \(x\mathfrak m\) contains a unit, and \(\mathfrak m=x^{-1}A\) is principal. The DVR characterization quoted above applies. Localizing the finite normal algebra consequently gives these DVRs, so it is a Dedekind ring.

At a closed point with local DVR \(R_v\), the resulting algebra is finite and torsion-free, hence free. Its completion is the product of the integer rings of the completed fields at the points above \(v\). Factor the parameter ideal in this Dedekind ring into powers of its distinct maximal ideals, apply the Chinese remainder theorem at every power, and take the inverse limit. Finite free modules commute with this completion. Each factor is the completed local DVR, hence the valuation ring of the corresponding completed field.

If the quotient kills inertia, each such local field extension is unramified. Here inertia is the kernel of the local action on the maximal unramified extension. The proved equivalence in *Unramified and totally ramified extensions*, Theorem 2.1 identifies its finite extensions with finite separable residue extensions and constructs their integer rings by a monic polynomial whose derivative is a unit. Thus the completed integer algebras are finite étale. Their special fibres are products of finite separable fields. Completion preserves the original special fibre, so the same holds before completion. The original finite free algebra is étale: its relative differentials vanish on these fibres and at the separable generic fibre, hence vanish by Nakayama. Finite presentation and flatness now give the criterion proved in *Étale morphisms and their local structure*, Lemma 1.2 and Theorem 1.3. This proves that the normalization is a finite étale cover at every point. In the Galois case it is a connected constant-field cover by (3.5).

Finally, a continuous representation over a finite extension of \(\mathbf Q_\ell\) has compact image and a stable integral lattice. Begin with any lattice: compactness bounds all its translates inside one larger lattice, and their sum is a stable finitely generated lattice containing the original one. Every reduction modulo a power of the coefficient uniformizer is a finite Galois quotient killing inertia. Its connected cover is constant-field, so every reduction is trivial on \(G_{\bar k(t)}\). Intersection of all powers of the uniformizer is zero; the representation itself therefore factors through \(G_k\).

The image of the procyclic group is generated topologically by one operator \(A\). Over an algebraically closed coefficient field, \(A\) has an eigenline. All integer powers of \(A\), and then all their limits, preserve that line. Irreducibility forces it to be the entire space. In particular there is no irreducible two-dimensional representation. \(\square\)

**Corollary 3.3 (all ranks).** For \(F=\mathbf F_q(t)\) and every \(n\ge2\), an everywhere unramified cusp function on \(GL_n(F)\backslash GL_n(\mathbf A)/GL_n(\mathcal O)\) is zero. No central-character condition is required. On the Galois side there is no everywhere unramified irreducible representation of dimension \(n\ge2\) under the coefficient and continuity hypotheses of Proposition 3.2.

*Proof.* By the splitting theorem, write any bundle as \(E=\bigoplus_{j=1}^n\mathcal O(a_j)\), with \(a_1\ge\cdots\ge a_n\). Set \(L=\mathcal O(a_1)\) and \(Q=\bigoplus_{j=2}^n\mathcal O(a_j)\). Choose diagonal lattice representatives \(g=\operatorname{diag}(g_L,g_Q)\). The unipotent radical of the proper parabolic of block type \((1,n-1)\) consists of
\[
n(u)=\begin{pmatrix}1&u\\0&I_{n-1}\end{pmatrix},\qquad
u\in\mathbf A^{n-1}.
\]
Its rational quotient is \((F\backslash\mathbf A)^{n-1}\), with product measure of total mass one. The first coordinate of the lattice \(n(u)g\) gives \(L\), and projection onto the remaining coordinates gives \(Q\). Thus every integrand in this constant term represents an extension of \(Q\) by \(L\). Its class lies in
\[
\operatorname{Ext}^1(Q,L)
=\bigoplus_{j=2}^nH^1(\mathcal O(a_1-a_j))=0,
\]
because every \(a_1-a_j\ge0\). Every underlying bundle in the integral is therefore isomorphic to \(E=L\oplus Q\). The constant term equals the constant value \(f(E)\), and cuspidality makes it zero. Since \(E\) was arbitrary, \(f=0\). Proposition 3.2 already proves the Galois assertion in every dimension greater than one: its eigenline argument does not depend on rank two. Rank one has no proper parabolic and is excluded. \(\square\)

## 4. What survives on a curve of positive genus

The same constant-term argument bounds where cusp forms can be supported. Let \(g\) be the genus of \(X\).

We first justify the curve formulas at the finite-field scope needed here. The earlier *Dualizing sheaves and Serre duality for projective schemes*, Theorem 4.2 and Proposition 8.2 proves
\[
H^1(X,A)\cong H^0(X,\omega_X\otimes A^{-1})^\vee,
\qquad \omega_X=\Omega_{X/k},
\tag{4.1}
\]
for every line bundle \(A\) on a smooth projective curve over any field. Smoothness gives the Cohen–Macaulay and equidimensional hypotheses of that proof. The following calculation supplies Riemann–Roch and the canonical degree without a further imported theorem.

Coherent cohomology commutes with field extension here: a finite affine cover with affine intersections computes it, and tensoring its complex with the extension field is exact. Over \(\bar k\), two affine opens cover the curve. To construct them, choose a hyperplane section in a projective embedding, then another hyperplane avoiding its finitely many points; this is possible over the infinite field \(\bar k\). Their complements and intersection are affine. Hence cohomology vanishes above degree one, also over \(k\) by faithful scalar extension. The regular-function argument in Proposition 3.2 applies to \(X_{\bar k}\); geometric connectedness and the same scalar-extension calculation therefore give \(H^0(X,\mathcal O_X)=k\). Define \(g=h^1(X,\mathcal O_X)\).

A rational section identifies any line bundle with \(\mathcal O_X(D)\): its orders in the local DVR frames form a finite divisor, and the fractional modules \(\varpi_v^{-\operatorname{ord}_vD}R_v\) recover the bundle. For every closed point \(v\),
\[
0\longrightarrow\mathcal O_X(D)\longrightarrow\mathcal O_X(D+v)
\longrightarrow i_{v*}\kappa(v)\longrightarrow0.
\tag{4.2}
\]
The last sheaf is flasque and has \(k\)-dimension \([\kappa(v):k]\) in degree zero. Finite-dimensionality and the long exact sequence make Euler characteristic additive. Adding or subtracting the points of \(D\) gives
\[
\chi(X,A)=\deg A+1-g.
\tag{4.3}
\]
This also proves that the divisor degree is independent of the chosen rational section. A nonzero regular section has an effective divisor, so a line bundle of negative degree has no such section. Apply (4.1) to \(A=\mathcal O_X\) and \(A=\omega_X\): it gives \(h^0(\omega_X)=g\) and \(h^1(\omega_X)=1\). Formula (4.3) now gives \(\deg\omega_X=2g-2\).

For a vector bundle \(E\), saturate any rational line in its generic fibre. At each DVR this is the intersection with that line inside a free module; its quotient is torsion-free and hence free. The intersections glue to a line subbundle with vector-bundle quotient \(Q\). Locally split exact sequences give \(\det E=\det L\otimes\det Q\), so degrees add. Induction on rank, additivity of Euler characteristic, and (4.3) prove
\[
\chi(X,E)=\deg E+\operatorname{rank}(E)(1-g).
\tag{4.4}
\]
Thus all the cohomological inputs to the support and finiteness argument below have actual proofs here or in the earlier duality lesson.

**Proposition 4.1.** If a rank-two bundle \(E\) has a line subbundle \(L\) with

\[
2\deg L-\deg E>2g-2,
\]

then every unramified cusp form vanishes at \(E\). Up to tensoring by line bundles, the bundles at which an unramified cusp form can be nonzero belong to a finite set of isomorphism classes over \(\mathbf F_q\).

*Proof.* Put \(M=E/L\). The degree of \(LM^{-1}\) is \(2\deg L-\deg E\). Serre duality identifies its \(H^1\) with the dual of

\[
H^0(X,\omega_X\otimes L^{-1}M).
\]

The latter line bundle has negative degree under the displayed hypothesis. A nonzero section of a line bundle has an effective zero divisor and hence nonnegative degree, so this space vanishes. Lemma 1.1 applies.

We give the boundedness argument needed for the finiteness assertion. Fix an \(\mathbf F_q\)-defined line bundle \(H\) of positive degree \(d\), for example an ample bundle. Tensoring by powers of \(H\) lets us arrange

\[
0\leq e=\deg E<2d.
\]

For a bundle with potentially nonzero cusp value, every line subbundle satisfies \(\deg L\leq(e+2g-2)/2\). There is also a line subbundle of uniformly bounded degree below. Riemann–Roch gives

\[
\chi(E\otimes H^m)=e+2md+2(1-g).
\]

Choose one integer \(m\geq0\) making this positive for every \(e\) in the chosen interval. Since \(h^0\geq\chi\), there is a nonzero section of \(E\otimes H^m\). Saturating it and undoing the twist gives a line subbundle \(L\subset E\) with \(\deg L\geq-md\).

Thus such an \(E\) fits into an extension of two line bundles \(L,M\) whose degrees range over finite intervals. There are finitely many line bundles of any fixed degree \(a\) over \(\mathbf F_q\). Indeed choose \(b\) with \(a+bd>g-1\). Riemann–Roch gives a nonzero section of \(L\otimes H^b\), so it is \(\mathcal O(D)\) for an effective divisor of degree \(a+bd\). A curve over a finite field has finitely many closed points of degree at most this bound: such points occur in the finite sets \(X(\mathbf F_{q^r})\) for bounded \(r\). There are therefore finitely many such effective divisors, and hence finitely many \(L\). For each pair \((L,M)\), the finite-dimensional \(\mathbf F_q\)-vector space \(H^1(LM^{-1})\) has finitely many elements. Every possible \(E\) is represented among these finitely many extensions. This proves finiteness using Riemann–Roch and divisors alone. \(\square\)

## 5. A rational L-function that can be calculated completely

Take \(E_0/\mathbf F_5\) given by \(y^2=x^3-x\), and form the constant elliptic curve over \(\mathbf F_5(t)\). For \(x=0,1,2,3,4\), the right-hand side is respectively \(0,0,1,4,0\). The numbers of affine points over these coordinates are \(1,1,2,2,1\). Including infinity gives eight points, so

\[
a_5=5+1-8=-2,\qquad
P(T)=1-a_5T+5T^2=1+2T+5T^2.
\]

Let \(\alpha,\beta\) have sum \(-2\) and product \(5\). At a closed point of degree \(d\), the fibre Frobenius eigenvalues are \(\alpha^d,\beta^d\). The global Euler product is therefore

\[
L(E_0/\mathbf F_5(t),T)
=Z(\mathbf P^1,\alpha T)Z(\mathbf P^1,\beta T).
\]

Here \(Z(\mathbf P^1,U)=((1-U)(1-5U))^{-1}\). This identity follows from \(\#\mathbf P^1(\mathbf F_{5^m})=1+5^m\) and the exponential definition of zeta. Hence

\[
L(E_0/\mathbf F_5(t),T)
=\frac{1}{(1+2T+5T^2)(1+10T+125T^2)}.
\]

This rational function has poles. The curve is constant, so its first cohomology contributes invariant sections and top-degree cohomology as well as the middle cohomology of the base curve. Polynomiality requires additional hypotheses, such as eliminating those invariant contributions.

Here is the precise general rationality input. For a separated scheme \(Y\) of finite type over \(\mathbf F_q\), a constructible \(\mathbf Q_\ell\)-sheaf \(\mathcal F\), and \(\ell\ne p\), the Grothendieck trace formula gives

\[
L(Y,\mathcal F,T)=
\prod_i\det\left(1-T\operatorname{Frob}_q^{\mathrm{geom}}
\mid H_c^i(Y_{\overline{\mathbf F}_q},\mathcal F)\right)^{(-1)^{i+1}}.
\tag{5.1}
\]

Only finitely many finite-dimensional cohomology groups occur, so the right side is rational. The Euler product on the left uses geometric Frobenius on the stalk at a closed point of degree \(d\), with \(T^d\) in its local factor. For an elliptic curve over \(F\), take the first-cohomology local system \(\mathcal F\) on its good-reduction open set \(j:U\hookrightarrow X\) and the constructible sheaf \(j_*\mathcal F\) on \(X\); the stalks at the missing points give the inertia-invariant local factors.

We recall why the trace formula implies (5.1). The coefficient of \(T^m\) in \(T\,d\log L/dT\) is
\(\sum_{d\mid m}d\sum_{\deg x=d}\operatorname{Tr}((\operatorname{Frob}_x^{\mathrm{geom}})^{m/d}\mid\mathcal F_{\bar x})\).
This is the sum of stalk traces over \(Y(\mathbf F_{q^m})\). The trace formula makes it the alternating sum of the traces of \((\operatorname{Frob}_q^{\mathrm{geom}})^m\) on \(H_c^i\). Expanding the logarithmic derivative of the determinant product gives exactly that sum. Both series have constant term one, and logarithmic differentiation is injective on \(1+T\mathbf Q_\ell[[T]]\), proving the equality. The trace formula and finite-dimensionality are proved in the earlier *The trace formula in all dimensions*, Theorem 5.1; the Euler-product passage is also proved in *L-functions, rationality and the functional equation*, Theorem 2.1. For a finite coefficient extension \(E/\mathbf Q_\ell\), these statements use constructible adic sheaves with an integral model, exactly the coefficients of the elliptic-curve example.

## 6. The correspondence theorems and their boundary

Fix \(\ell\ne\operatorname{char}(k)\) and an abstract field isomorphism \(\iota:\overline{\mathbf Q}_\ell\to\mathbf C\) for comparing eigenvalues. Geometric Frobenius is the inverse of arithmetic Frobenius \(x\mapsto x^{q_v}\). The two sources below use different Frobenius and Hecke conventions, which we state explicitly.

First fix the raw Hecke operators. At a place \(v\), put \(K_v=GL_n(\mathcal O_v)\), give it Haar mass one, and let
\[
H_{i,v}=1_{K_v\operatorname{diag}(\varpi_v I_i,I_{n-i})K_v},
\qquad 0\le i\le n.
\tag{6.2}
\]
Here \(H_{0,v}=1_{K_v}\) is the convolution identity, and \(H_{n,v}\) is invertible under convolution. On our right-invariant adelic functions use
\[
R(H)f(g)=\int H(a)f(ga)\,da.
\]
If \(z_1,\ldots,z_n\) are the normalized Satake eigenvalues, the minuscule Satake calculation gives
\[
R(H_{i,v})f=q_v^{i(n-i)/2}e_i(z_1,\ldots,z_n)f,
\qquad
T_{i,v}=q_v^{-i(n-i)/2}H_{i,v}.
\tag{6.3}
\]
Thus \(T_{i,v}\) is the character operator for \(\bigwedge^i\). Here is the minuscule calculation in our convention. Write \(q=q_v\), \(\varpi=\varpi_v\), and give the upper-unipotent group \(N(\mathcal O_v)\) mass one. The normalized transform is
\[
S(H)(t)=\delta_B(t)^{1/2}\int_{N(F_v)}H(tu)\,du.
\]
For \(t=\operatorname{diag}(\varpi^{\lambda_1},\ldots,\varpi^{\lambda_n})\), membership of \(tu\) in the double coset of \(H_i\) says its lattice \(\Lambda\) satisfies \(\varpi\mathcal O_v^n\subset\Lambda\subset\mathcal O_v^n\), with colength \(i\). The diagonal entries of \(tu\) and \(\varpi(tu)^{-1}\) therefore force \(0\le\lambda_j\le1\); the determinant forces \(\sum_j\lambda_j=i\). Put \(\epsilon_j=\lambda_j\). Such lattices are exactly the lifts of the \((n-i)\)-dimensional residue subspaces with echelon pivots at the indices \(b\) for which \(\epsilon_b=0\). Their unique reduced echelon vectors are
\[
e_b+\sum_{a<b,\,\epsilon_a=1}c_{ab}e_a,
\qquad c_{ab}\in\kappa(v).
\]
Together with \(\varpi e_a\) at the remaining indices, they give every lattice of this type. Thus their number is \(q^c\), where
\(c=\#\{(a,b):a<b,\epsilon_a=1,\epsilon_b=0\}\).
They are represented by upper-unipotent matrices with entries \(\varpi^{-1}\widetilde c_{ab}\) at these pairs. Two matrices represent the same lattice precisely when their ratio lies in \(N(\mathcal O_v)\); each such right coset has measure one. The integral is consequently \(q^c\). If \(c'\) counts the opposite pairs \(\epsilon_a=0,\epsilon_b=1\), then
\[
\delta_B(t)^{1/2}=q^{-(c-c')/2},\qquad
c+c'=i(n-i).
\]
Every coefficient is therefore \(q^{i(n-i)/2}\), and
\(S(H_i)=q^{i(n-i)/2}\sum_{|J|=i}\prod_{j\in J}z_j\), proving (6.3). This agrees with [Frenkel, §2.3, (2.7)–(2.8), p.31]. For a general dual-group representation \(V\), \(T_{V,v}\) denotes the operator corresponding to its character under normalized Satake, as in *The Satake isomorphism for unramified groups and unramified L-factors*.

**Theorem 6.1 (Drinfeld, 1978–1989; L. Lafforgue, 2002).** There is a unique bijection between isomorphism classes of cuspidal automorphic representations of \(GL_n(\mathbf A)\) with finite-order central character and continuous irreducible \(n\)-dimensional \(\overline{\mathbf Q}_\ell\)-representations of \(G_F\), defined over a finite extension of \(\mathbf Q_\ell\), unramified outside finitely many places, and with finite-order determinant. Corresponding objects are unramified at exactly the same places. At each such \(v\), the eigenvalues of geometric Frobenius, transported by \(\iota\), are the unitary-normalized Satake eigenvalues for our right action. Rank one is class field theory; Drinfeld proved rank two and L. Lafforgue all ranks. The exact free locator is [L. Lafforgue, Théorème VI.9(i), p.158]. His local factor is defined using inverse Frobenius in Chapter VI, §1(a), p.152.

The author's Hecke convention also needs translation. His displayed kernel on p.23 is \(\sum_{\gamma\in GL_n(F)}H(g'^{-1}\gamma g)\), the case \(P=GL_n\) of that formula. Acting on a left-rational-invariant function and unfolding gives \(\int H(g'^{-1}g)f(g')\,dg'\). Set \(g'=ga\); this is \(R(\check H)f(g)\), where \(\check H(a)=H(a^{-1})\). Thus his normalized Hecke multiset is the inverse of ours, by (6.4)–(6.5). His definition of correspondence matches it with his arithmetic-Frobenius multiset [pp.152,158]. Inverting Frobenius gives exactly the geometric-Frobenius matching asserted here. Both inversions are needed to compare the same parameter.

**Theorem 6.2 (V. Lafforgue, 2018).** First let \(G\) be split connected reductive, with its split model over \(X\). Let \(N\subset X\) be a finite level subscheme, \(Z\) the centre, and \(\Xi\subset\operatorname{Bun}_Z(\mathbf F_q)\) a subgroup of finite index. There is a canonical decomposition of the finite-dimensional space of compactly supported cuspidal functions

\[
C_c^{\mathrm{cusp}}(\operatorname{Bun}_{G,N}(\mathbf F_q)/\Xi,
\overline{\mathbf Q}_\ell)=\bigoplus_\sigma\mathcal H_\sigma.
\tag{6.1}
\]

The indices are \(\widehat G\)-conjugacy classes of continuous parameters
\(\sigma:\pi_1(X\setminus N,\bar\eta)\to\widehat G(\overline{\mathbf Q}_\ell)\)
defined over finite extensions of \(\mathbf Q_\ell\). Semisimplicity means that whenever the image lies in a parabolic subgroup, it lies in a Levi subgroup of that parabolic; in characteristic zero this is equivalent to reductivity of its Zariski closure. The nonzero summands are generalized eigenspaces for the commutative excursion algebra. In the author's arithmetic-Frobenius convention, his normalized spherical Hecke operator \(T^{\mathrm{arith}}_{V,v}\), for a representation \(V\) of \(\widehat G\), has eigenvalue
\[
\operatorname{Tr}\bigl(\sigma(\operatorname{Frob}^{\mathrm{arith}}_v)\mid V\bigr)
\qquad(v\notin N).
\]
See [V. Lafforgue, §1.4 for arithmetic Frobenius; §2, p.7 for the central quotient; Definition 5.1, §6 and Theorem 8.4, pp.10–11,19–20].

The construction also applies to nonsplit connected reductive \(G/F\), after choosing a model and excluding its bad places from the unramified comparison. Parameters then take values in \({}^LG\) with their prescribed Galois projection. The bundle/adèle comparison uses the disjoint union of adelic quotients of the pure inner forms indexed by
\[
\ker^1(F,G)=\ker\left(H^1(F,G)\longrightarrow\prod_v H^1(F_v,G)\right),
\]
rather than a single adelic quotient; the central quotient and level are imposed on these spaces. This qualification is explicit in [V. Lafforgue, immediately after (8.9), p.20]. The result supplies automorphic-to-Galois parameters and Hecke compatibility; it does not assert that every parameter occurs, a bijection, or a packet multiplicity formula.

Here is the operator comparison for \(GL_n\), including its direction. Define \(\check H(a)=H(a^{-1})\). Inverting the double coset in (6.2) and permuting its diagonal entries gives
\[
\check H_{i,v}=H_{n,v}^{-1}*H_{n-i,v},\qquad
\check T_{i,v}=T_{n,v}^{-1}*T_{n-i,v}.
\tag{6.4}
\]
Indeed the inverse diagonal matrix is \(\varpi_v^{-1}I_n\) times a permutation of \(\operatorname{diag}(\varpi_v I_{n-i},I_i)\). Convolution with \(H_{n,v}^{-1}=1_{\varpi_v^{-1}I_nK_v}\) is that central translation, with no volume factor because \(K_v\) has mass one. The normalization powers agree since \(i(n-i)=(n-i)i\). The eigenvalue of \(R(\check T_{i,v})\) is therefore
\[
\frac{e_{n-i}(z)}{e_n(z)}=e_i(z_1^{-1},\ldots,z_n^{-1}).
\tag{6.5}
\]
The central determinant factor \(e_n(z)^{-1}\) is essential, including at \(i=n\). This is the character identity \((\bigwedge^i V)^\vee=\det(V)^{-1}\otimes\bigwedge^{n-i}V\).

Changing sides is a separate operation. For a function \(h\) on \(K\backslash GL_n(\mathbf A)/GL_n(F)\), set \(Jh(g)=h(g^{-1})\). Direct substitution gives
\[
J\left(\int H(a)h(a^{-1}x)\,da\right)=R(H)Jh,
\qquad
J\left(\int H(a)h(ax)\,da\right)=R(\check H)Jh.
\tag{6.6}
\]
For the second identity, \((ga^{-1})^{-1}=ag^{-1}\); changing \(a\) to \(a^{-1}\) is allowed by inversion-invariance of Haar measure on \(GL_n\). The first identity follows from \((ga)^{-1}=a^{-1}g^{-1}\). Thus changing sides alone does not decide whether to invert the Hecke function.

V. Lafforgue's modification direction decides it. In his full paper, Construction 1.8 trivializes the **target** \(\mathcal G_1\) of \(\mathcal G_0\to\mathcal G_1\); the source, transported by that map, gives the affine-Grassmannian point. His positive coweight orbit is \(K_v\varpi_v^\lambda K_v/K_v\) [V. Lafforgue, arXiv:1209.5352v10, Construction 1.8 and the orbit definition after Remark 1.11, pp.44–45]. For \(\lambda=(1^i,0^{n-i})\), the source lattice is a sublattice of the target, with length-\(i\) quotient. Fixing the output source bundle \(E(g)\), his Hecke operator sums over the target superlattices \(E(ga^{-1})\), \(a\in K_v\operatorname{diag}(\varpi_v I_i,I)K_v\). The pullback is from the target and the pushforward to the source [ICM report, §5, pp.10–11]. Because each right \(K_v\)-coset has mass one, this sum is \(R(\check H_{i,v})\), rather than \(R(H_{i,v})\). On the opposite quotient it is the second action in (6.6). Accordingly,
\[
T^{\mathrm{arith}}_{\wedge^i,v}
=R(\check T_{i,v}).
\tag{6.7}
\]

If \(z\) is the Satake class for our right action, (6.5) and Theorem 6.2 identify the eigenvalue multiset of \(\sigma(\operatorname{Frob}^{\mathrm{arith}}_v)\) with \(z^{-1}\). Taking geometric Frobenius in the **same** parameter inverts that multiset again and gives \(z\), as in Theorem 6.1. Thus both the Hecke inversion and the Frobenius inversion have been included in the comparison. One can also form \(\sigma^\vee(g)={}^{t}\sigma(g)^{-1}\), but its matrix identity by itself does not perform the operator comparison, and no extra dualization is needed after both convention changes just computed. Writing only “Frobenius” or only “normalized Hecke operator” would hide these choices.

The finite-order conditions in Theorem 6.1 remove unrestricted twists along the degree character. Dropping them changes the formulation. Nor can one replace Theorem 6.2 by a general-group bijection: the parameterization and the determination of packets are different assertions.

Hecke operators can be interpreted as modifications of bundles. Section 1 proves the vector-bundle dictionary on the fixed curve, and the minuscule calculation above describes its local lattice modifications. Families of general-group modifications, their geometric realization and automorphic sheaves are developed in *From adèles to bundles* and the geometric Langlands course. The elementary vanishing arguments above do not prove a shtuka correspondence.

## 7. Exercises

**Exercise 7.1 (basic).** For \(F=\mathbf F_q(t)\), identify the unramified \(GL_1\) double quotient with \(\mathbf Z\), and explain how the degree arises from valuations.

**Exercise 7.2 (intermediate).** For a split rank-two bundle on \(\mathbf P^1\), choose the summand needed for Lemma 1.1 and prove vanishing, keeping track of the direction of the degree inequality.

**Exercise 7.3 (intermediate).** Prove that a connected finite étale cover of \(\mathbf P^1_{\overline k}\) has degree one. Deduce the arithmetic fundamental group and the absence of unramified irreducible representations of dimension two.

**Exercise 7.4 (advanced).** Prove the positive-genus support bound and finiteness modulo line-bundle twists. Explain why an upper bound on destabilizing line degrees alone does not yet prove finiteness.

## 8. Solutions

**Solution 7.1.** The divisor map sends an idèle \((a_v)\) to \(\sum_vv(a_v)[v]\). It is surjective: a uniformizer in any one component gives that closed point. Its kernel is \(\prod_v\mathcal O_v^\times\). Quotienting by \(F^\times\) further identifies principal divisors with zero, so the quotient is \(\operatorname{Pic}(\mathbf P^1)\). The divisor calculation in Section 2 identifies this group with \(\mathbf Z\), by degree. Explicitly the degree is \(\sum_vv(a_v)\deg(v)\). With the convention that the bundle of the lattice \(a_v\mathcal O_v\) is \(\mathcal O(-\sum_vv(a_v)[v])\), this formula is the negative bundle degree; choosing the inverse lattice reverses that sign. In either convention the quotient is canonically the divisor-class group, with the stated sign translation.

**Solution 7.2.** Write \(E=\mathcal O(a)\oplus\mathcal O(b)\), \(a\geq b\). The higher-degree summand must be used as \(L\). Then \(LM^{-1}=\mathcal O(a-b)\) has zero first cohomology. The constant term is the constant value of the cusp form at \(E\), so that value is zero. Choosing the lower-degree summand would give \(\mathcal O(b-a)\), which can have nonzero first cohomology and would not justify the inference.

**Solution 7.3.** For a connected finite étale \(f:Y\to\mathbf P^1_{\bar k}\), properness and connected smoothness give \(H^0(Y,\mathcal O_Y)=\bar k\), by the regular-function argument in Proposition 3.2. The rank-\(d\) bundle \(f_*\mathcal O_Y\) has a perfect trace pairing, so it is self-dual. Its splitting degrees occur with their negatives. Since its space of global sections has dimension one, none can be positive; symmetry excludes negative degrees too. Every summand is \(\mathcal O\), so that dimension equals \(d\), forcing \(d=1\). Over \(k=\mathbf F_q\), a finite cover becomes a disjoint union of these copies. Galois descent only permutes them: a copy has no nonidentity automorphism over the base. The invariant chart algebras computed in (3.4) make the cover a constant-field cover. Hence the arithmetic fundamental group is \(G_k=\widehat{\mathbf Z}\). An everywhere unramified Galois representation factors through it by the normalization and stable-lattice arguments in Proposition 3.2. A topological generator has an eigenline over the algebraically closed coefficient field, and its powers and their limits preserve that line. Irreducibility forces dimension one, excluding dimension two. The geometric cover calculation, the finite-field descent, and the passage from unramified Galois quotients to covers are all needed.

**Solution 7.4.** Serre duality kills \(H^1(LM^{-1})\) when its degree exceeds \(2g-2\), yielding the upper bound by Lemma 1.1. Normalize \(\deg E\) into \(0,2d)\) by twisting with a fixed positive-degree line bundle. Riemann–Roch applied to one sufficiently large common twist gives a line subbundle of degree at least \(-md\). Combining this lower bound with the upper bound leaves finitely many possible degrees for \(L,M\). For each degree \(a\), another common twist makes each line bundle effective. There are finitely many effective divisors of the resulting fixed degree over the finite field, so there are finitely many line bundles. Each extension space is a finite vector space. This exhausts the bundles under consideration. Without the first Riemann–Roch lower bound, an unbounded sequence of line-bundle degrees would remain and the counting argument would fail.

## Proof dependencies and correspondence scope

- **Coherent cohomology and duality:** the affine vanishing and affine-cover comparison are proved in [*Cohomology of affine schemes and Serre's criterion*, Theorems 2.2 and 3.1, using *Čech cohomology*, Theorem 3.2. Finite-dimensionality for our projective curves is *Coherent sheaves on projective schemes: Serre's theorems*, Theorem 2.2. For smooth projective curves over any field, the duality (4.1) is proved in *Dualizing sheaves and Serre duality for projective schemes*, Theorem 4.2 and Proposition 8.2. Section 4 derives the canonical degree and Riemann–Roch, including vector bundles and nonrational closed points, from these earlier proofs.
- **Unramified local extensions:** over a complete discretely valued field, finite unramified extensions correspond to finite separable residue extensions, with an integral primitive-element presentation having unit derivative. The needed proof is *Unramified and totally ramified extensions*, Theorem 2.1. The finite-presentation flat/unramified criterion is proved in *Étale morphisms and their local structure*, Lemma 1.2 and Theorem 1.3. Proposition 3.2 supplies the finite normalization and constant-field descent arguments used for the Galois vanishing statement.
- **Cohomological trace and elliptic-curve factors:** for separated finite-type schemes over \(\mathbf F_q\) and constructible \(E\)-sheaves with an integral model, \(E/\mathbf Q_\ell\) finite and \(\ell\ne p\), the trace formula and finite-dimensionality are proved in *The trace formula in all dimensions*, Theorem 5.1. The elliptic-curve eigenvalues have sum \(q+1-\#E(\mathbf F_q)\) and product \(q\) by the actual point-count and cup-pairing calculation in *Cycle classes and the Lefschetz fixed-point formula for curves*, §6. Our Section 5 calculates the resulting constant-curve rational function and proves the determinant deduction from the trace formula.
- **Correspondences:** Theorems 6.1 and 6.2 are stated here with their full scope and precise locators in the free texts of L. and V. Lafforgue. Their shtuka and excursion-operator proofs are not supplied by the elementary arguments in this lesson.
- **Geometric Hecke constructions:** V. Lafforgue's target trivialization and positive-coweight orbit definition are the geometric input to the lattice-direction comparison [arXiv:1209.5352v10, Construction 1.8, Remark 1.11 and the subsequent orbit definition, pp.44–45]; the pullback and pushforward directions are in his ICM report, §5, pp.10–11. The fixed-curve vector-bundle dictionary, the minuscule scaling (6.3), and the inversion and side-change formulas (6.4)–(6.7) are proved here. Families of general-group modifications and geometric Satake are outside these proofs.

## References

- [Frenkel] E. Frenkel, *Lectures on the Langlands program and conformal field theory*, freely accessible preprint, arXiv:hep-th/0512172v1, 15 December 2005, §2.3, (2.7)–(2.8), p.31; §2.4, Theorem 1, p.31; and §3.2, pp.35–36. [Exact free version](https://arxiv.org/abs/hep-th/0512172v1).
- [Stacks] *The Stacks Project*, [03VR, automorphic forms and sheaves](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/trace.html#trace-section-automorphic), and [03UU, L-functions](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/trace.html#trace-section-L-function), in the freely accessible AI Integrated Stacks Project edition, which retains upstream tags. This edition and the official Stacks text are separate works with their own licences. The proofs written in this lesson are original CC0 exposition; no licensed source text is reproduced.
- [L. Lafforgue] L. Lafforgue, *Chtoucas de Drinfeld et correspondance de Langlands*, 2002, freely accessible author's full text, the Hecke-kernel formula on p.23, Chapter VI, §1(a),(d), pp.152,157–158, especially Théorème VI.9(i), p.158. [Free full text](https://www.laurentlafforgue.org/math/fulltext.pdf).
- [V. Lafforgue] V. Lafforgue, *Shtukas for reductive groups and Langlands correspondence for function fields*, arXiv:1803.03791v1, 10 March 2018, Definition 5.1, §6, Theorem 8.4 and the extension following (8.9), pp.10–11,19–20. [Exact free report](https://arxiv.org/abs/1803.03791v1). His full free preprint, *Chtoucas pour les groupes réductifs et paramétrisation de Langlands globale*, arXiv:1209.5352v10, 10 January 2018, supplies Construction 1.8 and the orbit definition following Remark 1.11, pp.44–45. [Exact free full version](https://arxiv.org/abs/1209.5352v10).
- [Gaitsgory] D. Gaitsgory, *Local and global Langlands conjecture(s) over function fields*, arXiv:2509.24902v1, submitted 29 September 2025, manuscript dated 30 September 2025, Introduction and §1.1. This free preprint for the ICM 2026 plenary address offers further reading on the categorical formulation. [Exact free version](https://arxiv.org/abs/2509.24902v1).
