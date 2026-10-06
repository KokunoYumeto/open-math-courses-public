# Conic subanalytic images and isotropic dimension

A vector-bundle projection is usually nonproper. Its image can still be subanalytic when the set is conic: rescale each nonzero vector into a bounded fibre disk, apply the proper-image theorem there, and then recover the original sizes. The recovery must distinguish strictly positive scaling from scaling by zero. A zero vector can belong to a linear image even when no zero vector belonged to the original set.

This lesson proves that argument for analytic vector bundles, including maps whose rank changes. It also explains why the canonical one-form gives the usual isotropic condition on a conic set and why its dimension is at most the dimension of the base.

Use the real analytic, finite-dimensional, Hausdorff, countable-at-infinity manifold conventions of Subanalytic sets and limiting tangent directions. Its subanalytic regularity, dimension and singular one-form results are explicit prerequisites. The proper-closure image lemma below is proved directly from the local semianalytic-lift definition, before it is applied to the bundle maps. These geometric statements use no coefficient ring. For subanalytic geometry, see Edward Bierstone and Pierre D. Milman, [*Semianalytic and subanalytic sets*](https://www.numdam.org/item/PMIHES_1988__67__5_0/). The isotropic cotangent viewpoint is developed by Masaki Kashiwara and Pierre Schapira in [*Microlocal Study of Sheaves*](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf), Astérisque 128 (1985).

## Source account: compact lifts, conic images and isotropic dimension {#source-account}

Bierstone and Milman, [*Semianalytic and subanalytic sets*](https://www.numdam.org/item/PMIHES_1988__67__5_0/), Publications Mathématiques de l’IHÉS 67 (1988), Definition 3.1 and the surrounding discussion on p. 16, give the local relatively compact semianalytic projection definition and the basic set operations. The proper-closure image proof P1–P2 below applies that definition directly: compactness supplies finitely many lift neighborhoods over a target ball, and analytic graph equations produce relatively compact lifted images. The actual input set stays in those graph domains; its closure is used for compactness alone. This explains the nonclosed image assertion without replacing it by an image of the closure.

The saturation and bundle-image arguments then use two explicit domains: bounded shrinking parameters and inverse shrinking for enlargement. Properness is checked on each selected domain's closure. A sphere slice extends a punctured cone across zero without inserting zero vectors, while a closed disk slice treats a general linear bundle image. Strictly positive rescaling preserves exactly the kernel-created zero outputs already in the bounded image. These steps include changing rank and rank zero. They expand the compressed conic-projection observation at the start of Kashiwara and Schapira's [*Microlocal Study of Sheaves*](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf), Astérisque 128 (1985), Proposition 8.2.3, p. 144; that passage does not itself give these saturation-domain proofs.

For the cotangent conclusion, Astérisque 128, Definition 8.2.1 and Proposition 8.2.2, p. 144, formulate canonical-form isotropy and its inheritance by conic subanalytic subsets. The source's subset proof uses a Whitney stratification. Here the already named singular one-form restriction theorem supplies the singular-set meaning; the smooth-locus equivalence is proved using the fibre Euler field and the stated sign of the symplectic form. The dimension bound then follows from the symplectic annihilator calculation. Bierstone–Milman, Remark 3.5, p. 17, identifies subanalytic dimension through smooth points. Its Theorem 7.2, pp. 37–38, gives fixed-dimensional regularity through further results on squared distance and analytic loci; reading that reduction does not close all those prerequisite proofs.

The teaching order is occupied fibres, compact lift domains, two kinds of saturation, changing-rank images, and the Euler-field calculation. The seven solved problems test the exact missing endpoints, failed properness, nonclosed images and zero-fibre behavior used in that order. This is a comparison of the admitted source mechanisms and the arguments written here, not an expression comparison with an unread treatment. Independently expressed programme text is dedicated under CC0 1.0 Universal; the credited human works retain their own terms. Complement, regularity, dimension and singular-form foundations remain the explicit programme inputs, separate from this source-account repair.

## Positive conicity and two different saturations

Let \(\tau:E\to X\) be an analytic vector bundle, with zero section \(0_X\). Write \(\dot E=E\setminus0_X\). A subset \(A\subset E\) is **positive-conic** when

\[
\lambda A=A\qquad\text{for every }\lambda>0.
\tag{1}
\]

This condition says nothing about negative scalars or about adding zero vectors. For any subset \(B\subset E\), define separately

\[
S_{>0}(B)=\{\lambda b:\lambda>0,\ b\in B\},\qquad
S_{\ge0}(B)=\{\lambda b:\lambda\ge0,\ b\in B\}.
\tag{2}
\]

If \(B_x\) is empty, both saturations have an empty fibre at \(x\). If it is nonempty, \(S_{\ge0}(B)_x\) contains zero, whereas \(S_{>0}(B)_x\) contains zero exactly when \(B_x\) already does. Multiplying a nonzero vector by a positive scalar cannot produce zero.

All proofs below are local on the base, so a fibre norm will mean the Euclidean norm in an analytic local trivialization. We do not need to choose a global analytic bundle metric.

## Why properness on the selected closure suffices {#proper-closure-image-proof}

The compactness required below has a direct description in the definition of a subanalytic set. Locally such a set is the projection of a relatively compact semianalytic set, where semianalytic means locally a finite Boolean combination of analytic equalities and inequalities. An analytic graph and an intersection with a coordinate ball preserve those conditions.

**Proper-closure image lemma.** Let \(f:P\to Q\) be analytic between finite-dimensional analytic manifolds. If \(A\subset P\) is subanalytic and \(f|_{\overline A}\) is proper, then \(f(A)\) is subanalytic. The set \(A\) need not be closed, and the conclusion concerns its actual image.

**Proof.** Fix \(q_0\in Q\). Choose a coordinate ball \(V\) about \(q_0\) whose closure is compact in a target coordinate chart. Properness makes

\[
K=\overline A\cap f^{-1}(\overline V)
\tag{P1}
\]

compact. At every point of \(K\), choose an open coordinate neighborhood \(W_i\) and a semianalytic set \(B_i\subset P\times Z_i\), relatively compact in that ambient product, with projection \(A\cap W_i\), as the subanalytic definition permits. Here \(Z_i\) is an auxiliary analytic manifold. Inside \(W_i\), choose a smaller coordinate ball \(U_i\) with \(\overline{U_i}\subset W_i\). Compactness allows finitely many such \(U_i\) to cover \(K\).

Use the graph of \(f\) to form

\[
\begin{aligned}
D_i=\{(q,p,z):{}&q\in V,\ p\in U_i,\ (p,z)\in B_i,\ q=f(p)\},\\
f(A)\cap V={}&\bigcup_i\operatorname{pr}_Q(D_i).
\end{aligned}
\tag{P2}
\]

Each \(D_i\) is semianalytic: its extra conditions are analytic graph equations and coordinate-ball inequalities. It is relatively compact. Indeed, its closure lies in the product of the compact target \(\overline V\), the compact \(\overline{U_i}\) inside \(W_i\), and the compact auxiliary projection of \(\overline{B_i}\). The graph equation persists at every limit; since \(\overline V\) lies inside the target chart, these limits remain in the domain on which that equation is analytic. Thus each projection in (P2) is subanalytic by definition, and their finite union is subanalytic.

To check the equality, any \(p\in A\) with \(f(p)\in V\) belongs to \(K\), hence to some \(U_i\), and its lift in \(B_i\) gives a point of \(D_i\). Conversely every point of \(D_i\) has \(p\in A\), so its target lies in \(f(A)\cap V\). This proves the equality and the local assertion at every \(q_0\). \(\square\)

This proof explains the role of the closure: it supplies a finite compact cover of all possible lifts near a target point. It is never inserted into the image equality. The deeper complement, regular-locus, dimension and singular one-form theorems used later remain separate inputs.

## Saturation with a proper closure

**Saturation theorem.** If \(B\subset E\) is subanalytic and \(\tau|_{\overline B}:\overline B\to X\) is proper, both sets in (2) are subanalytic.

**Proof.** Let \(\mu:\mathbb R\times E\to E\) be analytic multiplication, \(\mu(t,e)=te\), and let \(p:\mathbb R\times E\to E\) be projection. Separate shrinking from enlargement:

\[
D=\{(t,e):0<t\le1,\ te\in B\}.
\tag{3}
\]

The set \(D\) is subanalytic by analytic inverse image and intersection. There are exact identities

\[
\begin{aligned}
S_{>0}(B)&=\mu((0,1]\times B)\cup p(D),\\
S_{\ge0}(B)&=\mu([0,1]\times B)\cup p(D).
\end{aligned}
\tag{4}
\]

For \(0<\lambda\le1\), the first shrinking image gives \(\lambda b\). For \(\lambda\ge1\), set \(t=1/\lambda\), so \(t(\lambda b)=b\) and \(\lambda b\in p(D)\). Conversely a point in \(p(D)\) equals \(t^{-1}b\) for some positive \(t\le1\). Allowing \(t=0\) only in the second shrinking term gives exactly the extra zero vectors of \(S_{\ge0}\).

We check the two properness claims rather than assuming \(\mu\) or \(p\) globally proper. The closure of either shrinking domain lies in \([0,1]\times\overline B\). If \(K\subset E\) is compact, its base projection \(\tau(K)\) is compact, and

\[
[0,1]\times\bigl(\overline B\cap\tau^{-1}(\tau(K))\bigr)
\tag{5}
\]

is compact. The inverse image of \(K\) under \(\mu\), restricted to the closure of the shrinking domain, is a closed subset of (5). Thus \(\mu\) is proper on that closure.

For the enlargement term, \(\overline D\subset[0,1]\times E\). For compact \(K\subset E\), the inverse image under \(p|_{\overline D}\) is the closed set \(\overline D\cap([0,1]\times K)\), hence compact. Here no bound on the size of the vector in \(D\) is necessary: fixing a compact output set already provides it. Both images in each line of (4) are therefore subanalytic by the proper-closure image theorem. Finite union completes the proof. \(\square\)

In (4), the sets being imaged contain \(B\), rather than \(\overline B\). Closures justify properness of the maps; inserting them into the image formulas would add vectors that need not lie in either saturation.

## Extending a conic set across the zero section

**Extension theorem.** Let \(A\subset\dot E\) be positive-conic and subanalytic as a subset of \(\dot E\). Then the same subset \(A\), with no added zero vectors, is subanalytic in \(E\).

**Proof.** In a rank-\(m>0\) trivialization, take the unit sphere bundle \(H=\{\|e\|=1\}\) and put \(B=A\cap H\). The set \(B\) is subanalytic away from zero. It is also subanalytic in the whole bundle: near each zero vector, a small fibre disk misses \(H\), while every nonzero point is already in the given subanalytic ambient.

The closure of \(B\) lies in the unit sphere bundle. Over any compact base set, that sphere bundle is compact, so \(\overline B\) is proper over the base. Every nonzero vector of \(A\) rescales to a unit vector in \(B\), and conicity supplies the converse. Therefore

\[
A=S_{>0}(B).
\tag{6}
\]

The saturation theorem proves the result, including at zero-section limit points. A rank-zero bundle has \(\dot E=\varnothing\), so its only such subset is empty. Since subanalyticity is local, these local proofs cover the bundle. \(\square\)

The hypothesis \(A\subset\dot E\) is precise. An arbitrary subset of the zero section is not made subanalytic by the fact that the punctured part is empty. To add a zero-section subset \(Z\subset X\), one must separately know that \(Z\) is subanalytic; then \(A\cup0_Z\) is subanalytic by finite union.

## Linear images, including changing rank

**Linear-image theorem.** Let \(E,E'\to X\) be analytic vector bundles and \(f:E\to E'\) an analytic bundle morphism, linear in the fibres and covering the identity of \(X\). If \(A\subset E\) is conic and subanalytic, then \(f(A)\) is conic and subanalytic. Its closure or properness is not asserted.

**Proof.** Work in local trivializations. Let \(D=\{\|e\|\le1\}\) be the closed unit disk bundle in \(E\), and put

\[
A_0=A\cap D,\qquad B=f(A_0).
\tag{7}
\]

Every fibre of \(D\) is compact, and its projection to the local base is proper. For a compact set \(K\subset E'\), the closure \(\overline{A_0}\) intersected with \(f^{-1}(K)\) is a closed subset of the compact disk bundle over \(\tau'(K)\). Thus \(f\) is proper on \(\overline{A_0}\), proving \(B\) subanalytic.

We also need the closure of \(B\) to be proper over the base. The restriction \(f|_D\) is proper by the same argument, so its image \(f(D)\) is closed in \(E'\). Moreover, over compact \(L\subset X\),

\[
f(D)\cap(\tau')^{-1}(L)=f(D\cap\tau^{-1}(L))
\tag{8}
\]

is compact. Hence \(f(D)\to X\) is proper. The closed subset \(\overline B\subset f(D)\) is proper over \(X\) as well.

For any \(a\in A\), choose \(c>0\) so that \(ca\in D\). Conicity gives \(ca\in A_0\), and linearity gives \(f(a)=c^{-1}f(ca)\). Conversely every positive multiple of \(f(a_0)\), with \(a_0\in A_0\), is \(f(ca_0)\) for an element of \(A\). Thus

\[
f(A)=S_{>0}(B).
\tag{9}
\]

This equality includes zero outputs created by the kernel of \(f\): they already occur in \(B\). The saturation theorem finishes. No constant-rank condition on \(f\) was used. \(\square\)

An open fibre disk has a proper closure, but its own projection is not proper in positive rank. The closed disk in this proof makes each compactness claim direct. Neither (7) nor (9) adds target zero vectors whose original fibres had no kernel lift.

**Conic projection.** The base projection \(\tau(A)\) of a conic subanalytic set is subanalytic.

**Proof.** Regard \(X\) as the rank-zero vector bundle and apply the linear-image theorem to \(\tau\). More directly, conicity gives \(\tau(A)=\tau(A\cap D)\), and \(\tau\) is proper on the closure of \(A\cap D\). Both proofs include base points whose only input vector is zero. \(\square\)

## The canonical form and the dimension bound

On \(T^*X\), use coordinates \((x_1,\ldots,x_n;\xi_1,\ldots,\xi_n)\) and write

\[
\alpha=\sum_i\xi_i\,dx_i,\qquad
\omega=d\alpha=\sum_i d\xi_i\wedge dx_i,\qquad
R=\sum_i\xi_i\,\partial_{\xi_i}.
\tag{10}
\]

The coordinate-independent \(R\) is the fibre Euler field, the infinitesimal generator of positive scaling. The identity

\[
\iota_R\omega=\alpha
\tag{11}
\]

fixes the sign used here. Using \(-d\alpha\) as the symplectic convention changes that displayed sign but changes neither of the vanishing conditions below.

A conic subanalytic \(\Lambda\subset T^*X\) is **isotropic** when \(\alpha|_\Lambda=0\), using the singular-set restriction from the preceding lesson. Equivalently, the analytic cone test there checks \(\alpha_p\) on every point-normal cone of \(\Lambda\).

**Smooth-locus equivalence and dimension.** Such a set is isotropic if and only if the pullback of \(\omega\) to \(\Lambda_{\mathrm{reg}}\) is zero. In this case

\[
\dim\Lambda\le\dim X=n.
\tag{12}
\]

**Proof.** Positive scaling is an analytic diffeomorphism preserving \(\Lambda\), so it preserves its regular locus. Consequently \(R_p\in T_p\Lambda_{\mathrm{reg}}\); at a zero covector this field is simply zero. If the pullback of \(\alpha\) vanishes, its exterior derivative vanishes as well, giving the forward implication. Conversely, if \(\omega\) is zero on this tangent space, (11) gives \(\alpha_p(v)=\omega_p(R_p,v)=0\) for every regular tangent vector \(v\). This is exactly \(\alpha|_\Lambda=0\).

For the dimension bound, put \(W=T_p\Lambda_{\mathrm{reg}}\) in the symplectic vector space \(T_pT^*X\) of dimension \(2n\). Vanishing of \(\omega\) on \(W\) gives \(W\subset W^\omega\). Nondegeneracy of \(\omega\) gives \(\dim W^\omega=2n-\dim W\): the map to \(W^*\) defined by the pairing is onto and has kernel \(W^\omega\). Therefore \(2\dim W\le2n\). Take the supremum over the regular locus, which is the subanalytic dimension definition. \(\square\)

The conic condition is used in the reverse implication through the Euler tangent vector. For a general submanifold of a cotangent bundle, symplectic isotropy does not by itself make the canonical one-form vanish.

## Exercises with solutions

### A ray does not acquire its endpoint under positive scaling

*Difficulty: Introductory.*

In \(E=\mathbb R^2\), let \(B=\{(1,2)\}\). Determine both saturations in (2), and explain why neither is the full line through \((1,2)\). What happens in a fibre where \(B\) is empty?

**Solution.** Strictly positive scaling gives \(\{(r,2r):r>0\}\), while nonnegative scaling gives \(\{(r,2r):r\ge0\}\). Negative multiples belong to neither. The first omits the origin and the second contains it. An empty fibre contributes no vector even at scalar zero, since there is no \(b\) to multiply. Thus \(S_{\ge0}(B)\) adds zero only over the actual base projection of \(B\).

### An arbitrary zero-section subset remains arbitrary

*Difficulty: Intermediate.*

In \(E=\mathbb R_x\times\mathbb R_v\), consider \(A=\{(1/m,0):m\ge1\}\). Its punctured part is empty. Show that \(A\) is positive-conic but not subanalytic in \(E\), and locate the hypothesis that prevents misuse of the extension theorem.

**Solution.** Positive fibre scaling fixes every point of \(A\), so (1) holds. Each point is an isolated connected component, and infinitely many approach the ambient point \((0,0)\). The connected components are therefore not locally finite, contradicting the subanalytic component theorem. The extension theorem starts with a subset of \(\dot E\) itself, not a subset of \(E\) with an arbitrarily chosen zero-section part. Applied to the empty punctured part, it only proves that the empty subset is subanalytic. A rank-zero bundle has the same distinction: conicity alone puts no restriction on its subsets, while the punctured extension hypothesis forces the subset to be empty.

### Unbounded generators can produce a non-subanalytic saturation

*Difficulty: Advanced.*

Let \(B=\{(r,1,\sin r):r>0\}\subset\mathbb R^3\), over a one-point base. Show that \(B\) is subanalytic, but neither of its saturations is subanalytic in \(\mathbb R^3\). Identify the failed properness hypothesis.

**Solution.** The equations \(y=1\), \(z=\sin x\) and inequality \(x>0\) make \(B\) semianalytic, hence subanalytic. Intersect either saturation with the analytic conditions \(x=1\), \(z=0\). A point of that intersection must have \(\lambda r=1\), \(\lambda\sin r=0\), with \(\lambda>0\); allowing \(\lambda=0\) cannot give \(x=1\). Therefore the intersection is

\[
\{(1,1/(m\pi),0):m\ge1\}.
\tag{13}
\]

These singleton components accumulate at \((1,0,0)\), so the intersection is not subanalytic. Finite intersection with analytic sets would preserve subanalyticity, giving the contradiction. The closure of \(B\) is unbounded and noncompact, so its map to the one-point base is not proper. Being subanalytic before saturation does not supply that bound.

### A closed cone can have a nonclosed linear image

*Difficulty: Intermediate.*

Let

\[
A=\{(a,b,c)\in\mathbb R^3:a\ge0,\ c\ge0,\ ac\ge b^2\},
\qquad f(a,b,c)=(a,b).
\tag{14}
\]

Verify that \(A\) is closed, conic and subanalytic. Compute \(f(A)\) and show that it is not closed. Why does this respect the linear-image theorem?

**Solution.** The three polynomial weak inequalities define a closed semialgebraic set, hence a subanalytic set. Positive scaling preserves them, with the last inequality scaled by the square of the scalar. For \(a>0\), every \(b\) occurs by taking \(c=b^2/a\). If \(a=0\), the last inequality forces \(b=0\). Thus

\[
f(A)=\{(a,b):a>0\}\cup\{(0,0)\}.
\tag{15}
\]

This is subanalytic and conic, but it omits \((0,1)\), the limit of \((1/j,1)\). Those points have lifts \((1/j,1,j)\in A\), whose last coordinate escapes to infinity. The theorem proves subanalyticity by a bounded cutoff and saturation, and does not assert properness of \(f\) on the full cone or closedness of its image.

### A changing-rank map creates exactly one zero fibre

*Difficulty: Intermediate.*

For the analytic line bundles over \(X=\mathbb R\), take \(f(x,v)=(x,xv)\) and \(A=\{(x,v):v>0\}\). Compute its image. Explain how (9) retains the kernel fibre without adding zero elsewhere.

**Solution.** At \(x\ne0\), an output \(w=xv\) has the same sign as \(x\), and every such \(w\) occurs. At \(x=0\), every input gives \(w=0\). Hence

\[
f(A)=\{(x,w):xw>0\}\cup\{(0,0)\}.
\tag{16}
\]

It is semianalytic and conic. The rank is one away from \(x=0\) and zero there. In a bounded input disk, positive \(v\) over zero still maps to \((0,0)\), so \(B\) in (7) already contains that output. At every other base point, \(B\) has no zero output, and strictly positive saturation cannot create one. Nonnegative saturation would incorrectly add the entire target zero section, since the base projection of \(B\) is all of \(X\).

### The Euler tangent vector is essential

*Difficulty: Intermediate.*

In \(T^*\mathbb R\) with \(\alpha=\xi\,dx\), compare the section \(L=\{\xi=1\}\) and the positive cotangent fibre \(P=\{x=0,\xi>0\}\). Compute the pullbacks of \(\alpha\) and \(d\alpha\). Which is isotropic under the conic definition?

**Solution.** Both are one-dimensional manifolds, so their pulled-back two-form \(d\alpha\) is zero. On \(L\), \(\alpha\) pulls back to \(dx\), which is nonzero. The Euler field \(\xi\partial_\xi\) is not tangent to \(L\), and \(L\) is not conic. On \(P\), the coordinate \(x\) is fixed, so \(\alpha\) pulls back to zero; \(P\) is conic and its Euler field is tangent. Thus \(P\) satisfies the conic isotropic definition. The example distinguishes ordinary symplectic isotropy from canonical-form vanishing when the conic hypothesis is absent.

### A compact closure does not add endpoints to the image

*Difficulty: Introductory.*

For \(A=\{(x,t):0<t<1,\ t^2<x<1\}\subset\mathbb R^2\), compare the images of \(A\) and \(\overline A\) under \(f(x,t)=x\). Explain the use of the closure in the proper-closure image lemma.

**Solution.** Every point of \(A\) has \(0<x<1\). Conversely, for any such \(x\), choose \(t=\sqrt{x}/2\); then \(0<t<1\) and \(t^2<x\), so \(f(A)=(0,1)\). The closure is \(\{(x,t):0\le t\le1,\ t^2\le x\le1\}\), a compact set, and its image is \([0,1]\). Properness on the closure is automatic by compactness, but replacing the domain by its closure would change the requested image. The lifts in (P2) retain the strict inequalities of \(A\), so their target remains \((0,1)\).

## References and subsequent use

Bierstone and Milman develop the local semianalytic-lift framework and the deeper subanalytic regularity theory. Kashiwara and Schapira develop the isotropic and conormal geometry. The proofs here use a finite compact lift cover, two explicit saturation domains, and the Euler vector field to obtain the stated bundle and cotangent conclusions. The canonical-form cone test and singular restriction remain the exact programme inputs linked above; the full regularity and dimension foundations retain their stated prerequisite status.

These results now permit conic cotangent images to remain subanalytic without assuming that their full projections are proper. The next arguments will combine that fact with canonical-form pullback and surjective detection to study isotropic cotangent correspondences and discrete critical values.
