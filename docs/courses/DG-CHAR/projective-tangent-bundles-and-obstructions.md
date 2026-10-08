# Projective tangent bundles and their obstructions

*Written by GPT-6.1 Sol (OpenAI), at Ultra, October 2026; the rotation-group starting example by Claude Opus 5.5 (Anthropic). Self-checked by the writing AI. Independently authored material dedicated under CC0.*

This chapter asks three different geometric questions. Can a tangent bundle have a frame? How much normal rank would an immersion need? Can the manifold occur as a boundary? A characteristic class enters each question in a different way: as a class of the tangent bundle, as a coefficient of its multiplicative inverse, or as a number evaluated on a fundamental class. Keeping those three operations separate prevents a vanishing calculation from being mistaken for a construction.

The first calculation identifies the tangent bundle of real projective space. We then use its inverse class to test normal rank, before returning to the stronger problem of constructing actual frames. The final part constructs fundamental classes and uses them to test boundaries. Every test has its own hypotheses and its own conclusion.

We use singular homology and cohomology with coefficients in \(\mathbb F _2\), except in the explicit real algebras. A smooth manifold is Hausdorff and second countable. “Closed” means compact without boundary. The preceding [bundle chapter](DG-CHAR-01.html) proves metrics, complements and bundle constructions; the [Thom chapter](DG-CHAR-06.html) proves the chain, excision and Mayer–Vietoris facts used below. The [Gysin chapter](DG-CHAR-08.html) proves
\[
H^*(\mathbb {RP}^{n};\mathbb F _2)=\mathbb F _2[a]/(a^{n+1}),\qquad a=w_1(\gamma).
\]
Here \(\gamma\) is the tautological real line bundle. The [squares chapter](DG-CHAR-05.html) constructs the Stiefel–Whitney classes and proves their axioms, including the Whitney product formula. These are proved inputs, rather than hypotheses about a hypothetical system of classes.

### A rotation group supplies a starting example

The rotation group \(SO(3)\) consists of the orthogonal three-by-three matrices of determinant one. It has a tangent frame that can be written down directly. Section 2 constructs a diffeomorphism \(\mathbb {RP}^3\to SO(3)\) from quaternion conjugation, in its subsection on why the four-dimensional example is \(SO(3)\), and the local inverses given there are smooth maps on open sets of the space \(M_3(\mathbb R)\) of real three-by-three matrices. Consequently each tangent space \(T_RSO(3)\) is a three-dimensional subspace of \(M_3(\mathbb R)\), and it contains the velocity of every smooth curve in \(SO(3)\) through \(R\).

Let \(\rho_1(t),\rho_2(t),\rho_3(t)\) be the rotations through the angle \(t\) about the three coordinate axes, and put \(A_i=\rho_i'(0)\). For the third axis,
\[
\rho_3(t)=\begin{pmatrix}\cos t&-\sin t&0\\ \sin t&\cos t&0\\ 0&0&1\end{pmatrix},
\qquad
A_3=\begin{pmatrix}0&-1&0\\ 1&0&0\\ 0&0&0\end{pmatrix}.
\]
The matrices \(A_1,A_2,A_3\) form a basis of the real skew-symmetric three-by-three matrices. For \(R\in SO(3)\) put
\[
X_i(R)=RA_i\qquad(1\leq i\leq3).
\]
The curve \(t\mapsto R\rho_i(t)\) stays in \(SO(3)\) and has velocity \(RA_i\) at \(t=0\), so \(X_i(R)\in T_RSO(3)\). Multiplication by the invertible matrix \(R\) is injective, so \(RA_1,RA_2,RA_3\) are linearly independent; since the tangent space has dimension three, they form a basis of it. Each \(X_i\) is the restriction of the smooth map \(R\mapsto RA_i\) of \(M_3(\mathbb R)\), hence a smooth vector field. Thus \(X_1,X_2,X_3\) is a frame of \(TSO(3)\), and the diffeomorphism of Section 2 carries it to a frame of \(T\mathbb {RP}^3\).

Any obstruction to a frame must therefore vanish on \(\mathbb {RP}^3\). The positive-degree Stiefel–Whitney classes, computed in Theorem 1.1 and Corollary 1.2 below, do vanish there, because \(3+1\) is a power of two. On \(\mathbb {RP}^4\) they do not all vanish, because \(4+1\) is not, so \(\mathbb {RP}^4\) has no frame. Vanishing classes are only a necessary condition for a frame; Section 2 constructs actual frames from bilinear multiplications.

## 1. The tangent bundle as a bundle of linear maps

At a line \(L\subset\mathbb R^{n+1}\), nearby lines are the graphs of maps \(A:L\to L^\perp\). These are the Grassmannian charts proved in the [classification chapter](DG-CHAR-03.html). Differentiating the graph coordinate at \(A=0\) identifies
\[
T_L\mathbb {RP}^{n}=\operatorname {Hom}(L,L^\perp).
\tag{1.1}
\]
This identification is intrinsic: a curve of lines, represented by a nonzero curve \(x(t)\), is sent to the map taking \(x(0)\) to the orthogonal projection of \(x'(0)\) onto \(L^\perp\). Replacing \(x(t)\) by \(c(t)x(t)\) multiplies both its input and projected output by \(c(0)\); the term \(c'(0)x(0)\) projects to zero. Thus the map does not depend on the representative. The graph charts show smooth dependence and give the inverse on each tangent space. Consequently
\[
T\mathbb {RP}^{n}\cong\operatorname {Hom}(\gamma,\gamma^\perp).
\]

**Theorem 1.1.** For every \(n\geq0\),
\[
T\mathbb {RP}^{n}\oplus\varepsilon^1\cong(n+1)\gamma,
\qquad
w(T\mathbb {RP}^{n})=(1+a)^{n+1}.
\tag{1.2}
\]

**Proof.** The identity of each line gives a canonical frame of \(\operatorname {Hom}(\gamma,\gamma)\). Distributivity of \(\operatorname {Hom}\), followed by \(\gamma\oplus\gamma^\perp=\varepsilon^{n+1}\), gives
\[
T\mathbb {RP}^{n}\oplus\varepsilon^1
\cong\operatorname {Hom}(\gamma,\varepsilon^{n+1})
\cong(n+1)\gamma^*.
\]
The Euclidean metric identifies the real line \(\gamma\) with its dual by \(v\mapsto\langle v,-\rangle\). The Whitney formula and \(w(\gamma)=1+a\) now give (1.2). For \(n=0\), the tangent bundle has rank zero and both sides of the bundle formula have rank one. ∎

Write \(N=\sum_{j\in J}2^j\) in binary. In characteristic two,
\[
(1+t)^N=\prod_{j\in J}(1+t^{2^j}).
\tag{1.3}
\]
Indeed, squaring a polynomial doubles its exponents and leaves its coefficients fixed; iterate this identity and multiply the binary factors. Each exponent obtained by choosing a subset of \(J\) occurs exactly once, because binary expansion is unique.

**Corollary 1.2.** The total class \(w(T\mathbb {RP}^{n})\) equals \(1\) if and only if \(n+1\) is a power of two.

**Proof.** If \(n+1=2^j\), (1.3) gives \(1+a^{n+1}=1\) in the truncated ring. If its binary expansion has at least two terms, the smallest term \(2^j\) is strictly less than \(n+1\). The coefficient of \(a^{2^j}\) is one, and this power survives. ∎

This is a necessary condition for parallelizability: a trivial tangent bundle has total class one. The converse has not been proved by this calculation. In particular it provides no tangent frame on \(\mathbb {RP}^{15}\).

## 3. Normal bundles and immersion bounds

The completed graded ring \(\prod_{i\geq0}H^i(X;\mathbb F _2)\) permits infinite series. Multiplication in each degree is a finite sum. An element \(1+b_1+b_2+\cdots\), with \(b_i\) in degree \(i\), has a unique inverse \(1+c_1+c_2+\cdots\), determined recursively by
\[
c_m=\sum_{i=1}^m b_i c_{m-i},\qquad c_0=1.
\tag{3.1}
\]
The degree-\(m\) coefficient of their product is then zero for \(m>0\). Uniqueness follows by the same recursion. This convention avoids requiring an infinite series to lie in the direct-sum cohomology ring. On a finite-dimensional projective space all sufficiently high degrees vanish, so the inverse is a finite polynomial.

Suppose \(f:M^n\to\mathbb R^{n+k}\) is an immersion, meaning that every derivative \(D f_x\) is injective. A nonzero \(n\)-minor stays nonzero locally, and solving in those columns gives local frames of its image. Thus \(D f(TM)\) is a smooth subbundle of the trivial bundle. Its orthogonal complement \(\nu_f\) has rank \(k\), even if the image of \(f\) has self-intersections. The derivative and complement give
\[
TM\oplus\nu_f\cong\varepsilon^{n+k},\qquad
w(\nu_f)=w(TM)^{-1}.
\tag{3.2}
\]
Consequently the component of the inverse in every degree greater than \(k\) must vanish. This is the Whitney duality restriction for immersions.

**Theorem 3.1.** If \(N=2^r\), \(r\geq0\), and \(\mathbb {RP}^{N}\) immerses in \(\mathbb R^{N+k}\), then \(k\geq N-1\).

**Proof.** In \(\mathbb F _2[a]/(a^{N+1})\),
\[
w(T\mathbb {RP}^{N})^{-1}
=(1+a)^{N-1}
=1+a+\cdots+a^{N-1}.
\]
For the first equality, multiply by \((1+a)^{N+1}\): the result is \((1+a)^{2N}=1+a^{2N}=1\), since \(2N\geq N+1\). For the second, all the binary digits of \(N-1\) are one, so (1.3) contains every exponent from zero to \(N-1\). The surviving nonzero class \(a^{N-1}\) in the normal bundle forces its rank to be at least \(N-1\). If \(N=1\) this says \(k\geq0\), as it should. ∎

In particular \(w(T\mathbb {RP}^4)=1+a+a^4\) and its inverse is \(1+a+a^2+a^3\). An immersion therefore requires ambient dimension at least seven. The proof gives a necessary bound; constructing an immersion is a separate problem.

### Reading the inverse class as a rank budget

For any \(n\geq0\), let \(m\) be the least power of two with \(m\geq n+1\). In the ring \(\mathbb F _2[a]/(a^{n+1})\), the tangent formula gives
\[
w(T\mathbb {RP}^{n})^{-1}=(1+a)^{m-n-1}.
\tag{R.1}
\]
Indeed its product with \((1+a)^{n+1}\) is \((1+a)^m=1+a^m=1\). This is also the unique inverse produced by recursion (3.1). If \(m=n+1\), its exponent is zero. Otherwise \(m/2<n+1<m\), so \(0<m-n-1\leq n\). The leading coefficient of the displayed polynomial is one and survives truncation. An immersion in \(\mathbb R^{n+k}\) therefore requires
\[
k\geq m-n-1.
\tag{R.2}
\]
This proves a bound for every projective dimension; Theorem 3.1 is its power-of-two specialization. It asserts no existence of an immersion at the bound.

For \(n=9\), the next binary power is \(m=16\). The inverse is
\((1+a)^6=1+a^2+a^4+a^6\), so six normal directions are necessary. For \(n=10\), the same binary power gives
\((1+a)^5=1+a+a^4+a^5\), so the necessary normal rank drops to five. The dimensions increased, but this particular obstruction became weaker: its size is controlled by the binary gap to the next power. Both calculations require an ambient dimension of at least fifteen, by this test alone.

For \(n=15\), the gap is zero and the inverse class is one. This test supplies no positive lower bound on normal rank. The tangent class is also one, but neither calculation constructs a frame. To construct one we need geometric data, such as the bilinear multiplication in the next part. To obstruct a boundary we need evaluation on a fundamental class, supplied in the final part. These are three distinct uses of the same characteristic data.

## 2. Bilinear multiplication gives actual frames

**Theorem 2.1.** Suppose \(n\geq1\) and a real bilinear map
\[
B:\mathbb R^n\times\mathbb R^n\longrightarrow\mathbb R^n
\]
satisfies \(B(x,y)=0\Rightarrow x=0\text{ or }y=0\). Then \(\mathbb {RP}^{n-1}\) is parallelizable and \(n\) is a power of two. Neither associativity nor an identity element is required.

**Proof.** Fix a nonzero vector \(b_0\) and complete it to a basis \(b_0,\ldots,b_{n-1}\). The linear map \(C(x)=B(x,b_0)\) is injective and therefore invertible. It induces a smooth diffeomorphism
\[
h:\mathbb {RP}^{n-1}\longrightarrow\mathbb {RP}^{n-1},\qquad h(L)=C(L),
\]
whose inverse is induced by \(C^{-1}\). Put \(\eta_L=C(L)\). For \(1\leq i<n\), define a linear map
\[
A_i(L):\eta_L\longrightarrow\eta_L^\perp,
\qquad C(x)\longmapsto\operatorname {proj}_{\eta_L^\perp}B(x,b_i),\quad x\in L.
\tag{2.1}
\]
It is well-defined and linear because \(C|_L\) is invertible. Local nonzero sections of \(L\) show that it depends smoothly on \(L\). If a linear combination of these maps is zero, then, for a fixed nonzero \(x\in L\),
\[
B\left(x,\sum_{i=1}^{n-1}t_i b_i\right)\in\mathbb R B(x,b_0).
\]
The map \(y\mapsto B(x,y)\) is invertible. Hence \(\sum_{i\geq1}t_i b_i\in\mathbb R b_0\), forcing every \(t_i=0\). The \(A_i\) therefore form a frame of \(h^*T\mathbb {RP}^{n-1}\), by (1.1). Transport this frame through \(h^{-1}\); the tangent bundle itself is trivial. Corollary 1.2 gives the claim about \(n\). For \(n=1\) the empty frame trivializes the zero-dimensional tangent bundle. ∎

There is a shorter proof of the numerical restriction alone. The fibrewise map
\[
\gamma\otimes\varepsilon^n\longrightarrow\varepsilon^n,
\qquad x\otimes y\longmapsto B(x,y)
\]
is an isomorphism over \(\mathbb {RP}^{n-1}\). Thus \(n\gamma\) is trivial and \((1+a)^n=1\). The binary argument again makes \(n\) a power of two. This shorter argument gives stable triviality; (2.1) supplies the actual tangent frame.

### Normed examples in dimensions four and eight

For completeness we construct the two algebras that give the required examples. On \(\mathbb H=\mathbb C^2\), define
\[
(a,b)(c,d)=(ac-\overline d\,b,\; da+b\overline c),
\quad \overline{(a,b)}=(\overline a,-b),
\quad |(a,b)|^2=|a|^2+|b|^2.
\tag{2.2}
\]
The real-linear injection
\[
M(a,b)=\begin{pmatrix}a&-b\\\overline b&\overline a\end{pmatrix}
\]
satisfies \(M(qr)=M(q)M(r)\), as multiplication of its four entries verifies. Also \(M(\overline q)=M(q)^*\) and \(M(q)^*M(q)=|q|^2 I\). Matrix associativity proves associativity of (2.2), and the last identity proves
\[
|qr|=|q|\,|r|.
\]
The unit is \((1,0)\). Conjugation reverses multiplication, by taking matrix adjoints. Define \(\operatorname {Re}(q)=\tfrac12\operatorname {tr}M(q)\). The trace is real here, and matrix trace gives \(\operatorname {Re}(pq)=\operatorname {Re}(qp)\). Moreover \(\operatorname {Re}(q\overline r)\) is the ordinary Euclidean inner product; this follows immediately by expanding (2.2).

Now put \(\mathbb O=\mathbb H^2\), with multiplication, conjugation and squared norm given by the same formulas (2.2), interpreted in \(\mathbb H\). The multiplication is real bilinear and has unit \((1,0)\). Its norm is multiplicative even though we make no associativity assertion for \(\mathbb O\). To see this, expand the squared norms of \(ac-\overline d b\) and \(da+b\overline c\). Their diagonal terms add to
\[
(|a|^2+|b|^2)(|c|^2+|d|^2).
\]
Their cross terms are
\[
-2\operatorname {Re}(ac\overline b d)
\quad\text{and}\quad
2\operatorname {Re}(da c\overline b).
\]
They cancel, since quaternion multiplication is associative and its real part is invariant under cyclic rearrangement. Thus \(|xy|=|x|\,|y|\) in \(\mathbb O\). Both algebras have no zero divisors, and Theorem 2.1 yields frames on \(\mathbb {RP}^3\) and \(\mathbb {RP}^7\).

These frames can be written directly. In either algebra, take an orthonormal real basis \(1,e_1,\ldots,e_{n-1}\). Polarizing norm multiplicativity in the second factor gives
\[
\langle xy,xz\rangle=|x|^2\langle y,z\rangle.
\]
At \(L=\mathbb R x\), the maps \(x\mapsto xe_i\) belong to \(\operatorname {Hom}(L,L^\perp)\), and their outputs are pairwise orthogonal nonzero vectors. Real bilinearity makes these linear maps independent of the choice of generator of \(L\). They form the promised smooth frames.

### Why the four-dimensional example is \(SO(3)\)

Let \(\operatorname {Im}\mathbb H\) be the three-dimensional space of quaternions with real part zero. Each unit quaternion defines
\[
R_q(v)=qv\overline q\quad(v\in\operatorname {Im}\mathbb H).
\]
Norm multiplicativity and cyclic invariance of the real part show that \(R_q\) is orthogonal and preserves this space. Its determinant is \(+1\): it depends continuously on \(q\), the unit sphere \(S^3\) is path connected, and \(R_1=I\). The map \(q\mapsto R_q\) is a group homomorphism. Its kernel is \(\{1,-1\}\), since direct multiplication with the three imaginary coordinate units shows that a quaternion commuting with all of them is real.

It is onto. Every matrix in \(SO(3)\) has a unit fixed vector: its nonreal eigenvalues occur in conjugate pairs, its real eigenvalues are \(\pm1\), and its determinant is one. On the perpendicular plane it acts by a rotation through some angle \(\theta\). Directly from (2.2), multiplication of imaginary vectors has the form \(uv=-\langle u,v\rangle+u\times v\), using the oriented orthonormal basis of imaginary coordinate units. Expanding the conjugation by
\(q=\cos(\theta/2)+u\sin(\theta/2)\) fixes the axis \(u\) and rotates its perpendicular plane by \(\theta\). Hence it gives the specified matrix.

We obtain a continuous bijection \(\mathbb {RP}^3=S^3/\{\pm1\}\to SO(3)\), which is a homeomorphism because its source is compact and its target Hausdorff. It is also a diffeomorphism. Near the identity matrix, its inverse chooses the representative with positive real coordinate:
\[
q_0=\frac{\sqrt{1+\operatorname {tr}R}}2,
\qquad
(q_1,q_2,q_3)=\frac{(R_{32}-R_{23},R_{13}-R_{31},R_{21}-R_{12})}{4q_0}.
\]
These are smooth wherever \(q_0>0\), and the conjugation formula verifies them. Group translations provide smooth inverse charts at every other point.

## 4. Fundamental classes from finite chart gluing

We now supply the homological foundation for characteristic numbers. This section uses the fully proved singular-chain excision, relative Mayer–Vietoris and sphere homology from the [Thom chapter](DG-CHAR-06.html). No CW structure on the manifold is needed.

For a manifold \(M\) without boundary and \(x\in M\), excision and a chart give
\[
H_i(M,M-\{x\})=H_i(\mathbb R^d,\mathbb R^d-\{0\})
=\begin{cases}\mathbb F _2&i=d,\\0&i\ne d.\end{cases}
\tag{4.1}
\]
The unique nonzero local class will be denoted \(\mu_x\). The local values of a relative chain can be compared on a small closed ball avoiding the compact support of its boundary. The same chain defines a class relative to that ball, and the ball's top relative group maps isomorphically to the local group at every one of its points. Its local values are therefore constant there. For a class relative to a compact set, apply this comparison at the points of that set where its local values are defined.

**Lemma 4.1.** If \(K\subset M^d\) is compact, then \(H_i(M,M-K)=0\) for \(i>d\). There is a unique class \(\mu_K\in H_d(M,M-K)\) restricting to \(\mu_x\) at every \(x\in K\). More generally a top-degree relative class whose restriction is zero at every point of \(K\) is zero.

**Proof.** Start with a nonempty compact convex set \(P\subset\mathbb R^d\). For any \(x\in P\), both \(\mathbb R^d-P\) and \(\mathbb R^d-\{x\}\) retract onto a sufficiently large sphere centered at \(x\). The homotopy moves each radius linearly to the sphere's radius. Convexity ensures that a point outside \(P\) remains outside when moving outward; a point beyond the large sphere remains outside when moving inward to that sphere. Thus inclusion of these complements is a homotopy equivalence, and
\(H_i(\mathbb R^d,\mathbb R^d-P)\to H_i(\mathbb R^d,\mathbb R^d-\{x\})\)
is an isomorphism. This proves the lemma for \(P\). The empty set has zero relative groups and requires the zero class. When \(d=0\), the chart is a point and the same assertion follows directly.

Suppose the assertions hold for compact sets \(A,B,A\cap B\). Relative Mayer–Vietoris, applied to the open complements, gives
\[
0\longrightarrow H_d(M,M-(A\cup B))
\longrightarrow H_d(M,M-A)\oplus H_d(M,M-B)
\longrightarrow H_d(M,M-(A\cap B)).
\tag{4.2}
\]
The initial zero comes from the vanishing group in degree \(d+1\). Higher-degree exact segments prove the same vanishing for \(A\cup B\). The two prescribed classes agree on the intersection by uniqueness, hence lift by exactness to a class on the union. The injection proves uniqueness and detection by point restrictions. Induction now proves the lemma for finite unions of compact convex sets in one chart: intersections of their constituent sets are still compact convex sets, and the empty intersections cause no problem.

For an arbitrary compact \(K\) in a chart, represent a relative class by a finite chain \(z\) in that chart, with \(\partial z\) supported away from \(K\); excision permits this representative. The compact support of \(\partial z\) has positive distance from \(K\), unless it is empty, in which case any sufficiently small radius works. Cover \(K\) by finitely many closed balls centered in \(K\), with radius small enough to avoid \(\partial z\). Their union \(P\) contains \(K\), and \(z\) defines a class relative to \(P\). The proved vanishing for \(P\) gives vanishing for \(K\) in degrees above \(d\). In degree \(d\), if the class has zero local value on \(K\), its restriction to each chosen ball is zero: its value at the center is zero and point restriction on that ball is an isomorphism. Detection for the union makes the class relative to \(P\) zero, and therefore the original class is zero. Finally a closed ball containing \(K\) gives a top class whose image relative to \(K\) has all local values one. We may use a chart with image \(\mathbb R^d\); every ordinary coordinate ball is diffeomorphic to \(\mathbb R^d\).

For general compact \(K\), choose finitely many smaller chart neighbourhoods covering it, with closures contained in their charts. The compact sets \(K_j=K\cap\overline V_j\) cover \(K\). Induct on the number of charts using (4.2). The intersection of the last piece with the previous union is a union of fewer compact chart pieces, so the same induction applies there. This proves all assertions. ∎

**Corollary 4.2.** Every closed \(d\)-manifold has a unique class \([M]\in H_d(M;\mathbb F _2)\) with local value one at every point, and it has no homology in degrees greater than \(d\).

**Proof.** Apply Lemma 4.1 with \(K=M\). For a disconnected compact manifold the finitely many open components are compact, and the class is the sum of their fundamental classes. ∎

### A collar and the relative class

We record a collar construction to handle the boundary without an unstated geometric premise. Let \(W\) be a compact \(d\)-manifold with boundary \(M\). Attach the external product \(M\times[0,1]\) along \(M\times\{0\}\), obtaining \(W'\). Boundary charts show that this is again a manifold with boundary, whose boundary is \(M\times\{1\}\).

Choose a finite partition of unity \(\phi_1,\ldots,\phi_s\) on \(M\), each supported compactly inside a boundary coordinate patch. Such functions exist by the partition proof in the bundle chapter. Write \(\psi_j=\sum_{i\leq j}\phi_i\). Let \(W_j\) be \(W\) together with the external segments of lengths \(\psi_j(x)\). In the \(j\)-th patch, half-space coordinates give an internal product with heights \(-1\leq t\leq0\), and the attached collar gives heights \(0\leq t\leq\psi_{j-1}(x)\). Stretch this combined interval by
\[
(x,t)\longmapsto
\left(x,-1+(t+1)\frac{1+\psi_j(x)}{1+\psi_{j-1}(x)}\right).
\tag{4.3}
\]
Outside this patch and below height \(-1\), take the identity. The map agrees with the identity at height \(-1\) and wherever \(\phi_j=0\); compact containment of its support therefore makes the definitions continuous at the sides of the patch. Reversing the ratio gives a continuous inverse. Thus it is a homeomorphism \(W_{j-1}\to W_j\). Their composition identifies \(W\) with \(W'\) and sends its boundary to \(M\times\{1\}\). Pulling back the evident product neighbourhood there gives a collar of \(M\) in \(W\). Rescale it as \(c:M\times[0,2]\to W\), with boundary height zero and with an open product neighbourhood at all heights below two.

Set \(N=W-M\) and \(K=W-c(M\times[0,1))\). This is a compact subset of \(N\). Replacing \(M\) by its open collar neighbourhood in a relative homology pair induces an isomorphism, because the collar retracts onto \(M\) and the long exact sequences of pairs apply. Excision of \(M\) then gives
\[
H_d(W,M)\cong H_d(N,N-K).
\tag{4.4}
\]
Lemma 4.1 supplies the right-hand class with local value one on \(K\). Transport it through (4.4) to define \([W,M]\). Its local values at interior points form a locally constant function, by the small-ball argument preceding Lemma 4.1. Every component of \(N\) meets \(K\): collar points join their height-one points by a vertical interval, and points outside the collar already lie in \(K\). Thus all interior local values are one. Conversely these values determine the relative class, by (4.4) and the detection assertion of the lemma.

**Lemma 4.3.** The connecting map sends \([W,M]\) to \([M]\):
\[
\partial[W,M]=[M]\in H_{d-1}(M;\mathbb F _2).
\tag{4.5}
\]

**Proof.** Check local value at any point of \(M\). In its boundary chart take a product box \(Q=D^{d-1}\times[0,1]\), with its bottom face in \(M\). Let \(C=W-\operatorname {int}_W Q\); here the relative interior in \(W\) includes the interior of the bottom face. There is a commutative square
\[
\begin{array}{ccc}
H_d(W,M)&\longrightarrow&H_d(W,M\cup C)\\
\partial\downarrow&&\downarrow\partial_{\rm triple}\\
H_{d-1}(M)&\longrightarrow&H_{d-1}(M,M\cap C).
\end{array}
\]
At the chain level, both routes take the boundary of the same relative chain and then discard its part in \(C\). On the right, excision identifies the groups with \(H_d(Q,\partial Q)\) and \(H_{d-1}(D^{d-1},\partial D^{d-1})\). One may first enlarge \(C\) a little beyond the top and side faces: coordinate collars retract these enlarged pairs onto the displayed box pairs, and ordinary open-set excision then applies. The top class maps to the generator of \(H_d(Q,\partial Q)\), since restriction to an interior point is an isomorphism for this box and the original local value is one. The triple connecting homomorphism is represented by taking the chain boundary. After ignoring the top and side faces, this boundary restricts to the generator of
\(H_{d-1}(D^{d-1},\partial D^{d-1})\) on the bottom face. Explicitly, represent a box by the sum of the standard simplices obtained by ordering its coordinates; internal faces cancel in pairs over \(\mathbb F _2\), and its bottom face occurs once with its own such sum. This is also the interval external-product computation proved in the Thom chapter. Naturality of the pair and triple connecting maps shows that this bottom-face class is the restriction of \(\partial[W,M]\). Its local value is therefore one at every boundary point. Corollary 4.2 and its detection assertion imply (4.5). The case \(d=1\) uses a point as the bottom face and has exactly the same interval boundary computation. Empty boundary means both sides of (4.5) are zero. ∎

## 5. Characteristic numbers vanish on boundaries

For a closed \(n\)-manifold and nonnegative integers \(r_1,\ldots,r_n\) with \(\sum i r_i=n\), define the Stiefel–Whitney number
\[
\left\langle\prod_{i=1}^{n}w_i(TM)^{r_i},[M]\right\rangle\in\mathbb F _2.
\tag{5.1}
\]
The pairing evaluates a cocycle on a cycle. It is independent of representatives, because cocycles vanish on boundaries and coboundaries vanish on cycles. For \(n=0\), the empty product evaluates to the parity of the number of points.

**Theorem 5.1.** If \(M=\partial W\) for a compact smooth manifold \(W\), every number (5.1) is zero.

**Proof.** Along the boundary, the differential of its inclusion identifies \(TM\) as a subbundle of \(TW|_M\). Boundary coordinates provide local outward-pointing transverse vectors. A smooth partition of unity combines them into a global outward-pointing vector: in a boundary coordinate its normal component has the same strictly negative sign for every term, so it cannot vanish or become tangent. The smooth bump and metric constructions in the bundle chapter apply to boundary charts by restricting their Euclidean bumps to the half-space. Orthogonally projecting the vector off \(TM\), using such a metric, gives a nowhere-zero normal vector. Therefore
\[
TW|_M\cong TM\oplus\varepsilon^1.
\]
Naturality and Whitney imply \(w_i(TM)=\iota^*w_i(TW)\). The degree-\(n\) product in (5.1) is thus \(\iota^*b\) for a class \(b\in H^n(W)\). By (4.5) and exactness of the pair sequence,
\[
\iota_*[M]=\iota_*\partial[W,M]=0.
\]
Evaluation is natural, so
\(\langle\iota^*b,[M]\rangle=\langle b,\iota_*[M]\rangle=0\).
This proves the theorem in every dimension, including zero. ∎

On \(\mathbb {RP}^n\), the nonzero top class \(a^n\) evaluates to one: top homology has its fundamental generator by Corollary 4.2, and field cohomology is its dual by the universal-coefficient proof in the Thom chapter. Hence every characteristic number is computed by taking the coefficient of \(a^n\) in its product of classes.

If \(n>0\) is even, then \(w_n=(n+1)a^n=a^n\), so \(\mathbb {RP}^n\) cannot bound a compact smooth manifold. If \(n\) is odd, \((1+a)^{n+1}\) contains only even powers; all odd-index classes vanish. Every product of total odd degree contains an odd-index factor, so all its characteristic numbers vanish. Theorem 5.1 proves only the implication from bounding to vanishing; a general converse belongs to the later Thom-bordism argument.

For these odd projective spaces a filling is available directly. Regard \(\mathbb R^{2k}\) as \(\mathbb C^k\) and let \(L=\gamma_{\mathbb C}^{\otimes2}\) over \(\mathbb {CP}^{k-1}\). The map from the unit sphere \(S^{2k-1}\) to \(S(L)\), sending a unit vector \(v\) to \(v\otimes v\) in the fibre over \(\mathbb Cv\), identifies exactly \(v\) and \(-v\). Every unit square tensor has these two square roots, and local complex-line coordinates give smooth inverse charts after this quotient. Thus
\[
S(L)\cong\mathbb {RP}^{2k-1}.
\]
The disk bundle \(D(L)\) is a compact smooth manifold with this boundary. This supplies a filling without invoking the general converse.

## 6. Exercises with solutions

**Exercise 6.1 — Easy.** Compute the total classes of \(\mathbb {RP}^4\) and \(\mathbb {RP}^5\), and determine which is orientable.

**Solution.** Formula (1.3), with truncation in degrees five and six respectively, gives
\[
w(\mathbb {RP}^4)=1+a+a^4,\qquad
w(\mathbb {RP}^5)=1+a^2+a^4.
\]
The first determinant line has nonzero \(w_1=a\), so \(\mathbb {RP}^4\) is nonorientable. The second has \(w_1=0\). The determinant-line criterion and the real-line classification proved in the preceding chapters give orientability of \(\mathbb {RP}^5\). These spaces have the explicit CW structures already proved. An explicit nonzero field on \(\mathbb {RP}^5\) is the linear map \(x\mapsto Jx\) from \(\mathbb Rx\) to its perpendicular complement, where \(J\) is multiplication by \(i\) on \(\mathbb C^3\). It does not trivialize the whole tangent bundle, whose \(w_2\) is nonzero.

**Exercise 6.2 — Medium.** Prove Whitney duality for an immersion and compute the complete normal-class restrictions for immersions of \(\mathbb {RP}^9\).

**Solution.** The derivative and its orthogonal complement give (3.2); uniqueness of (3.1) proves the duality assertion. For \(n=9\),
\[
w(T\mathbb {RP}^9)=(1+a)^{10}=1+a^2+a^8
\]
in the ring truncated at \(a^{10}\). Its inverse is
\[
1+a^2+a^4+a^6,
\]
as multiplication cancels every positive coefficient through degree nine. Thus a normal bundle requires rank at least six, and every such immersion requires ambient dimension at least fifteen. No existence follows from the class calculation.

**Exercise 6.3 — Medium.** Recover the power-of-two restriction from stable bundles alone, then explain what establishes the stronger frame conclusion.

**Solution.** Bilinearity defines the isomorphism \(n\gamma\to\varepsilon^n\) described after Theorem 2.1. The lowest nonzero binary bit of \(n\), if smaller than \(n\), gives a surviving positive coefficient of \((1+a)^n\); hence \(n\) is a power of two. Stable tangent triviality by itself supplies no cancellation of the added line. For the actual frame use the projective diffeomorphism induced by \(x\mapsto B(x,b_0)\) and the projected maps (2.1); their independence follows from injectivity of left multiplication by each nonzero \(x\).

**Exercise 6.4 — Medium.** If a rank-\(m\) bundle on a paracompact Hausdorff base admits \(k\) everywhere independent sections, show that its classes in degrees greater than \(m-k\) vanish. Deduce a bound on the number of independent fields on \(\mathbb {RP}^n\) when \(n+1=2^r u\), with \(u>1\) odd.

**Solution.** A metric is available on the paracompact Hausdorff base. The sections span a trivial rank-\(k\) subbundle: in any local frame an invertible \(k\)-minor stays invertible on a neighbourhood and gives coordinates on their image. Its orthogonal complement has rank \(m-k\). The Whitney formula identifies the bundle's total class with that of this complement, whose classes above degree \(m-k\) vanish by the rank axiom.

For the projective space put \(N=n+1=2^r u\). Formula (1.3) says that the exponents with nonzero coefficient in \((1+a)^N\) are exactly the sums of subsets of the one-bits of \(N\). The smallest one-bit is \(2^r\). Every proper subset omits a sum of at least \(2^r\), and omitting just that bit gives the largest proper exponent
\[
q=N-2^r=n+1-2^r.
\]
Since \(u>1\) is odd, \(q>0\); also \(q\leq n\). Its coefficient is one, so
\[
w_q(T\mathbb {RP}^n)=a^q\ne0
\]
in \(\mathbb F_2[a]/(a^{n+1})\). If there are \(k\) independent tangent fields, the general rank assertion gives \(q\leq n-k\). Therefore
\[
k\leq n-q=2^r-1.
\]
This is a necessary bound on the number of independent fields.

The lowest one-bit also has nonzero coefficient. Since \(2^r\leq n\), the same rank argument gives \(n-k\geq2^r\), or \(k\leq n-2^r\). This remains a valid weaker bound; using the largest surviving degree above improves it.

**Exercise 6.5 — Hard.** Prove the boundary-number theorem directly at the chain level, and explain its consequence for two disjoint copies of a manifold.

**Solution.** Choose a relative fundamental chain \(c\) for \((W,M)\), so \(\partial c\) is a chain in \(M\) representing \([M]\), by Lemma 4.3. Choose a cocycle \(\beta\) representing the extending characteristic product in \(W\). Its restriction to \(M\) is a representative of the desired product. Its evaluation is
\[
\beta(\partial c)=(\delta\beta)(c)=0.
\]
This proves Theorem 5.1 using the fully constructed relative class. For \(M\sqcup M\), each number adds the same value twice and is zero in \(\mathbb F _2\); the cylinder \(M\times[0,1]\) supplies its filling. Conversely, the vanishing for an arbitrary manifold has not yet produced a filling.

**Exercise 6.6 — Hard.** Verify the explicit odd-projective filling and determine the characteristic numbers of \(\mathbb {RP}^4\).

**Solution.** On a unit local frame \(e\) of the tautological complex line, a unit vector is \(ze\), \(|z|=1\), and its square is \(z^2(e\otimes e)\). The map \(z\mapsto z^2\) has precisely the two preimages \(z,-z\). On arcs shorter than a semicircle it has a smooth inverse, so its quotient induces a diffeomorphism of the unit circle bundles claimed in Section5. The base is compact and disk fibres are compact; finitely many bundle charts and smaller compact base sets show the disk bundle is compact. Fibre boundary charts and interior charts make it a smooth manifold with boundary equal to its unit bundle. For \(\mathbb {RP}^4\), the degree-four products are
\(w_4,w_3w_1,w_2^2,w_2w_1^2,w_1^4\).
Their evaluations are respectively \(1,0,0,0,1\), because \(w=1+a+a^4\) and \(\langle a^4,[\mathbb {RP}^4]\rangle=1\). In particular this space does not bound.

## Sources and scope

Freely accessible comparisons are Allen Hatcher, *Vector Bundles and K-Theory*, version 2.2 (2017), [author PDF](https://pi.math.cornell.edu/~hatcher/VBKT/VB.pdf), Section 1.1, for projective tangent stabilization and the normed-algebra frame examples, and his *Algebraic Topology*, [author PDF](https://pi.math.cornell.edu/~hatcher/AT/AT.pdf), Lemma 3.27 and Proposition 3.42, for compact-set fundamental classes and collars. The graph-coordinate identification, full bilinear-frame argument, inverse-class bounds and local boundary-chain calculation are proved here.

John Milnor's [1957 lectures, with notes by James Stasheff](https://webhomes.maths.ed.ac.uk/~v1ranick/papers/milnorcc.pdf), Chapters II–III, give further reading on tangent bundles and vector fields. The stabilization, bilinear-frame restriction, inverse-class bounds and boundary-number arguments are proved here. David Michael Roberts's freely available [*Algebraic Topology* notes](https://github.com/DavidMichaelRoberts/AlgebraicTopology2019) (2019), Lecture 19, describe \(SO(3)\) as the quotient of \(SU(2)\), the group of unit quaternions, by its centre \(\{\pm I\}\).

The class tests are necessary conditions for a frame or immersion, with actual frames proved in the stated bilinear-algebra cases. The boundary-number implication is proved here in full; its all-dimensional converse is proved in the separate [unoriented-bordism companion](DG-CHAR-13E.html). No classification of all parallelizable projective spaces or construction of an immersion from a vanishing class is asserted. This edition was checked by the writing AI; independent review remains separate.
