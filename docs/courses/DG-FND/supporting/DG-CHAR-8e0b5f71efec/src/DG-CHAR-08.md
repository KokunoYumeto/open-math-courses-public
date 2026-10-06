# Projective bundles, Gysin sequences and line classes

DG-CHAR-08 · Differential geometry foundations

The Thom class gives an exact sequence for the complement of a vector bundle's zero section. We use that sequence to calculate real and complex projective cohomology, including the sign of the complex generator and the Hopf example. A singular-chain comparison then proves the projective-bundle module theorem over arbitrary Hausdorff bases. Continuous partitions supply the separate metric tools needed for flag splitting and line-bundle pullback models. The final arguments establish the tensor and Hom formulas and identify the real line Euler class with orientation transport.

Cohomology is ordinary singular cohomology; chains are finite sums of singular simplices, and groups in negative degrees are zero. Vector-bundle rank is constant in each assertion. Bases are Hausdorff. Where partitions, metrics or classifying maps are needed, paracompactness is explicitly required. The algebra assumes the usual number systems and the axiom of choice. Complex fibre orientations list each real basis vector followed by its imaginary multiple; Hermitian metrics are conjugate-linear in the first argument.

The earlier programme lessons are [Local tools for bundles and transport](../../../src/local-tools-for-bundles-and-transport.md), [Integral Thom classes and Euler indices](DG-CHAR-06.md), and [Manifold duality and the Euler characteristic](DG-CHAR-07.md). Numeric labels such as 0.1–0.4 refer to the opening lesson. Labels K, E, U, X, O, T and N refer to the chain, exactness, coefficient, product/cap, orientation, Thom and zero-index proofs in DG-CHAR-06; its L.1 proves the determinant identities. References to DG-CHAR-07 F.2 and D.1 identify its block determinant and field chain-splitting proofs. S, Q, P, R, I, W, M and Z label the eight sections here. External readings supply construction material; every result used is proved here or at those exact earlier programme locators.

## 1. The Euler exact sequence and its normalization

Let \(V\to B\) be a real vector bundle of constant finite rank \(r\), with total space \(E\), projection \(\pi\), zero section \(s\), and complement \(E^\times=E\setminus s(B)\). The base \(B\) is Hausdorff. Write \(j:E^\times\hookrightarrow E\) and \(\pi^\times=\pi j\). Cohomology means ordinary singular cohomology. Its cochain differential is denoted by \(d\), and all groups in negative degrees are zero.

For an oriented bundle we use its integral Thom class \(u\) and integral Euler class \(e=s^*J(u)\), as proved and defined in DG-CHAR-06 T.3–T.4. Here \(J\) forgets the relative condition. Cohomology with coefficients in an abelian group \(G\) is acted on by integral cohomology on both sides. Explicitly, for a degree-\(p\) integer cochain \(a\) and degree-\(q\) \(G\)-cochain \(b\), the value of \(a\smile b\) on an ordered \((p+q)\)-simplex is the integer \(a\) on its first \(p\)-face acting on the value of \(b\) on its last \(q\)-face; reverse these roles for \(b\smile a\). The face cancellations in K.5 prove the Leibniz rule for these products too: they use only addition, multiplication of integers and their action on \(G\). The successive-block formula likewise proves associativity whenever one factor has coefficients in \(G\) and the others in \(\mathbb Z\).

In the unoriented case take \(G=\mathbb F_2\), the mod-two Thom class \(u_2\), and \(e_2=s^*J(u_2)\). Every argument below is then performed over that field. We write \(u,e\) for the relevant classes when the two cases can be treated together.

### From the relative pair to the base

**Theorem S.1 (Euler exact sequence).** Suppose \(r>0\). For the oriented bundle and every abelian coefficient group \(G\), there is an exact sequence
\[
\cdots\longrightarrow H^{m-r}(B;G)
\xrightarrow{\ a\mapsto a\smile e\ }H^m(B;G)
\xrightarrow{\ (\pi^\times)^*\ }H^m(E^\times;G)
\xrightarrow{\ \partial_V\ }H^{m-r+1}(B;G)
\xrightarrow{\ \smile e\ }H^{m+1}(B;G)
\longrightarrow\cdots .
\tag{S.1}
\]
The same sequence holds with \(e_2\) and coefficients \(\mathbb F_2\) for every real bundle. These sequences commute with coefficient homomorphisms and pullback bundles, with the pulled-back orientation in the integral case. They also commute with orientation-preserving bundle isomorphisms.

**Proof.** Scalar multiplication gives the homotopy
\[
H:E\times[0,1]\longrightarrow E,\qquad H(v,t)=tv.
\]
It is continuous in every local bundle chart, so it is continuous on the total space. At \(t=0\) it is \(s\pi\), at \(t=1\) it is the identity, and \(\pi s\) is the identity of \(B\). The exact prism homotopy K.1 therefore shows that
\[
\pi^*:H^m(B;G)\longrightarrow H^m(E;G)
\quad\text{has inverse }s^*.
\tag{S.2}
\]
No metric or locally finite trivializing cover is needed for this homotopy.

T.3 supplies the isomorphism
\[
\Phi_G:H^{m-r}(B;G)\longrightarrow H^m(E,E^\times;G),
\qquad \Phi_G(a)=\pi^*a\smile u .
\tag{S.3}
\]
In the oriented case this is the product of the \(G\)-valued class with the integral Thom class. Its arbitrary Hausdorff-base and arbitrary-\(G\) scope is part of the earlier proof, not an assumption about the topology of \(B\).

The pair exact sequence E.1 contains
\[
\cdots\to H^m(E,E^\times;G)
\xrightarrow{J}H^m(E;G)
\xrightarrow{j^*}H^m(E^\times;G)
\xrightarrow{\delta}H^{m+1}(E,E^\times;G)\to\cdots .
\tag{S.4}
\]
The definition of the Euler class and (S.2) imply
\(J(u)=\pi^*e\): applying the inverse \(s^*\) to both classes gives \(e\).
The naturality and associative face formulas for the cup product now give
\[
J\Phi_G(a)=\pi^*a\smile J(u)
=\pi^*(a\smile e).
\tag{S.5}
\]
Also \(j^*\pi^*=(\pi^\times)^*\) by the definition of pullback on singular simplices. Define
\[
\partial_V=\Phi_G^{-1}\delta .
\tag{S.6}
\]
Replace the four terms in (S.4) involving \(E\) or the pair by the isomorphic base groups (S.2)–(S.3). Identity (S.5) identifies the first map, the pullback identity identifies the second, and (S.6) identifies the third. Transport through isomorphisms preserves equality of each kernel and preceding image. This gives every term, degree and map of (S.1).

For a coefficient homomorphism, applying it to a cochain commutes with \(d\), pullback and integer multiplication. In the explicit connecting construction of E.1 it sends a lifted cochain to a lift of its image. Thus (S.4) and (S.3) commute with coefficient change. For a pullback bundle, the induced total-space map sends nonzero vectors to nonzero vectors, so it is a map of pairs. The pair connecting map commutes with this pullback by E.1, and T.4 says that the Thom class pulls back to the prescribed Thom class. These facts also apply to an orientation-preserving bundle isomorphism and show that (S.2), (S.3), (S.5) and (S.6) commute with the stated maps. Over \(\mathbb F_2\) no orientation choice enters any of these identities. □

Rank zero has a separate literal description. In that case \(E=B\), \(E^\times=\varnothing\), \(u=e=1\), and \(J\) is the identity on \(H^m(B;G)\). Sequence (S.4) alternates this identity with zero groups and maps. This is exact directly; no sphere of negative dimension or choice of a negative point generator is used.

### The connecting-map sign

**Lemma S.2 (left module rule).** For an oriented bundle of positive rank, \(b\in H^k(B;\mathbb Z)\) and \(y\in H^m(E^\times;G)\),
\[
\partial_V\bigl((\pi^\times)^*b\smile y\bigr)
=(-1)^k b\smile\partial_V(y).
\tag{S.7}
\]
The same formula holds modulo two without an orientation, with the sign equal to \(1\).

**Proof.** Represent \(b,y\) by cocycles \(b_0,y_0\). Extend \(y_0\) to a cochain \(\widetilde y_0\) on \(E\) by assigning zero to every basis singular simplex not contained in \(E^\times\). This is a well-defined \(G\)-valued cochain, because singular chains are free on their actual parameterized simplices. Since \(dy_0=0\), the cochain \(d\widetilde y_0\) vanishes on \(E^\times\) and represents \(\delta y\) in the relative complex.

The cochain \(\pi^*b_0\smile\widetilde y_0\) restricts to a representative of \((\pi^\times)^*b\smile y\). The Leibniz rule gives the exact relative cochain identity
\[
d(\pi^*b_0\smile\widetilde y_0)
=(-1)^k\pi^*b_0\smile d\widetilde y_0 ,
\tag{S.8}
\]
since \(d\pi^*b_0=0\). Consequently
\(\delta((\pi^\times)^*b\smile y)=(-1)^k\pi^*b\smile\delta y\).
If \(a\) is a base class with coefficients in \(G\), associativity and pullback naturality give
\[
\Phi_G(b\smile a)
=\pi^*b\smile\pi^*a\smile u
=\pi^*b\smile\Phi_G(a).
\tag{S.9}
\]
Apply the inverse \(\Phi_G^{-1}\) to (S.8) in cohomology and then use (S.9). This proves (S.7), including when one of the target degrees is negative and the corresponding group is zero. The same cochain computation works over \(\mathbb F_2\). The sign thus belongs to the normalization (S.6); it has not been chosen by analogy with a differently normalized integration map. □

### Metrics and two-sheeted covers

**Lemma S.3 (sphere form of the sequence).** If \(V\) has a continuous positive definite fibre metric, its unit sphere bundle \(S(V)\) has the exact sequence (S.1), with \(\pi^\times\) replaced by its projection to \(B\). The connecting map is the transport of (S.6) under the explicit radial retraction.

**Proof.** The fibre norm is continuous and positive on \(E^\times\). Define
\[
\rho(v)=v/\|v\|,\qquad
F_t(v)=\bigl(1-t+t/\|v\|\bigr)v
\quad(v\ne0,\ 0\leq t\leq1).
\tag{S.10}
\]
The scalar coefficient is strictly positive, so \(F_t(v)\ne0\) at every time. Bundle charts show joint continuity. At \(t=0\) the map is the identity; at \(t=1\) it is the inclusion followed by \(\rho\); and if \(\|v\|=1\), the point is fixed throughout. Thus this is a deformation retraction onto \(S(V)\) that preserves the projection to \(B\). K.1 makes the inclusion pullback a cohomology isomorphism with inverse \(\rho^*\). Substituting that isomorphism into (S.1) gives the asserted sequence and maps, and preserves exactness. This assertion assumes a metric only when using the sphere form; S.1 did not assume that one exists. □

**Corollary S.4 (two-sheeted-cover sequence).** Let \(p:P\to B\) be a two-sheeted covering of a Hausdorff space. Let \(\tau:P\to P\) interchange the two points in each fibre, and put
\[
L=(P\times\mathbb R)/\bigl((x,t)\sim(\tau x,-t)\bigr).
\tag{S.11}
\]
This is a real line bundle with a canonical metric. There is an exact sequence
\[
\cdots\to H^{m-1}(B;\mathbb F_2)
\xrightarrow{\ \smile e_2(L)\ }H^m(B;\mathbb F_2)
\xrightarrow{\ p^*\ }H^m(P;\mathbb F_2)
\xrightarrow{\ \partial_L\ }H^m(B;\mathbb F_2)
\xrightarrow{\ \smile e_2(L)\ }H^{m+1}(B;\mathbb F_2)\to\cdots .
\tag{S.12}
\]

**Proof.** On an evenly covered open set \(U\), the two sheets are mapped homeomorphically to \(U\). Interchanging them is continuous, so \(\tau\) is a continuous involution globally. Choose one sheet over \(U\). Give the class \([x,t]\) coordinate \(t\) if \(x\) is on that sheet and coordinate \(-t\) if it is on the other. These formulas identify \(L|_U\) with \(U\times\mathbb R\). To check the topology explicitly, the quotient map in (S.11) is open: the inverse image of the image of an open set is its union with its image under \((x,t)\mapsto(\tau x,-t)\). On the selected sheet times \(\mathbb R\) the quotient is a continuous bijective open map onto \(L|_U\). Its inverse is therefore continuous and gives the stated bundle chart. On overlaps the coordinate changes are multiplication by a sign, locally constant because membership in either open sheet is locally constant. These are linear homeomorphisms, so the charts define a line bundle. Its total space is Hausdorff: different base points separate downstairs, and two different points over the same base point separate in one of the open bundle charts.

The norm \(\|[x,t]\|=|t|\) is independent of the representative and is a continuous fibre norm in these charts. The map
\[
h:P\longrightarrow S(L),\qquad h(x)=[x,1]
\tag{S.13}
\]
is bijective. Every unit representative has \(t=1\) or \(t=-1\), and \([x,-1]=[\tau x,1]\); no two distinct \(x\)'s have the same representative with coordinate \(1\). The map and its inverse are continuous on the two sheets in each chart. Thus \(h\) is a homeomorphism and the sphere projection composed with \(h\) is \(p\). Apply S.1 over \(\mathbb F_2\) with rank one, and S.3 with this metric. Identification by \(h\) gives precisely (S.12). □

The notation \(w_1(L)\) will be defined and compared with this class in Z.1–Z.3. S.4 uses only the already defined mod-two Euler class in (S.12).
## 2. Continuous partitions and bundle tools

A family of subsets of a space is **locally finite** if each point has an open neighbourhood meeting only finitely many members. An open cover \(\mathcal V\) **refines** an open cover \(\mathcal U\) if each member of \(\mathcal V\) is contained in a member of \(\mathcal U\). In this component a space is **paracompact Hausdorff** if it is Hausdorff and every open cover has a locally finite open refinement. A space is **normal** if two disjoint closed sets have disjoint open neighbourhoods. The support of a continuous function is the closure of the set on which it is nonzero.

### Separation and shrinking

**Lemma Q.1 (normality and refinements with closures).** A paracompact Hausdorff space \(X\) is normal. If \(x\in U\) and \(U\) is open, there is an open \(W\) with
\[
x\in W\subset\overline W\subset U.
\tag{Q.1}
\]
Every open cover has a locally finite open refinement whose members' closures also refine the original cover. If \(F\subset U\), with \(F\) closed and \(U\) open, there is an open \(W\) satisfying
\[
F\subset W\subset\overline W\subset U.
\tag{Q.2}
\]

**Proof.** We first record two facts about local finiteness. If an open set \(O\) misses a set \(A\), it also misses \(\overline A\): a point of \(O\cap\overline A\) would have the neighbourhood \(O\) meeting \(A\). Therefore the closures of a locally finite family are locally finite. The union of a locally finite family of closed sets is closed. Indeed near any point only finitely many of them occur; a point outside their union has a smaller neighbourhood avoiding that finite union. This proves that the complement of the whole union is open.

Let \(F\) be closed and \(x\notin F\). For each \(y\in F\), the Hausdorff property gives disjoint open sets \(O_y\ni y\) and \(W_y\ni x\). In particular \(x\notin\overline{O_y}\). Refine
\[
\{X\setminus F\}\ \cup\ \{O_y:y\in F\}
\]
by a locally finite open cover \(\mathcal R\), choosing for each member a containing member of the displayed cover. Let \(\mathcal R_F\) consist of the members that meet \(F\). Such a member cannot be contained in \(X\setminus F\), so it is contained in some \(O_y\), and its closure misses \(x\). Consequently
\[
A=\bigcup_{R\in\mathcal R_F}\overline R
\]
is closed, misses \(x\), and contains the open neighbourhood \(\bigcup_{R\in\mathcal R_F}R\) of \(F\). Thus \(X\setminus A\) and this last union separate \(x\) and \(F\). Applying this to \(F=X\setminus U\) gives an open neighbourhood \(W\) of \(x\) disjoint from an open neighbourhood of \(F\). Its closure misses that neighbourhood of \(F\), proving (Q.1).

Given an open cover \(\mathcal U\), choose, at each point, an open neighbourhood whose closure lies in one member of \(\mathcal U\), using (Q.1). Take a locally finite open refinement of these neighbourhoods. The closure of each new member lies in the closure of its assigned neighbourhood and hence in the assigned member of \(\mathcal U\). This proves the refinement assertion.

Now let \(A,B\) be disjoint closed subsets of \(X\). Apply this assertion to \(\{X\setminus A,X\setminus B\}\), obtaining a locally finite open cover \(\mathcal R\) with closures subordinate. Every \(R\) that meets \(A\) has its closure in \(X\setminus B\). The union \(C\) of the closures of these members is closed, contains an open neighbourhood \(O\) of \(A\), and misses \(B\). Then \(O\) and \(X\setminus C\) are disjoint open neighbourhoods of \(A,B\). This proves normality. Finally separate the disjoint closed sets \(F\) and \(X\setminus U\) by disjoint opens \(W,O\). Since \(O\) misses \(W\), it misses \(\overline W\). It contains \(X\setminus U\), so \(\overline W\subset U\), which is (Q.2). □

### Continuous separating functions

**Lemma Q.2 (the separating-function construction).** In a normal space \(X\), disjoint closed sets \(A,B\) admit a continuous function \(f:X\to[0,1]\) with \(f|_A=0\) and \(f|_B=1\).

**Proof.** Normality implies the shrinking assertion (Q.2), by its last proof, without any use of paracompactness. Set \(U_1=X\setminus B\), and choose \(U_0\) open with \(A\subset U_0\subset\overline U_0\subset U_1\). Let \(D\) be the dyadic numbers in \([0,1]\). Recursively insert open sets \(U_t\) for the dyadics of denominator \(2,4,8,\ldots\). If \(t\) is inserted between two consecutive previously chosen values \(a<b\), shrink the closed set \(\overline U_a\) inside \(U_b\) to obtain
\[
\overline U_a\subset U_t\subset\overline U_t\subset U_b.
\]
At each finite stage these inclusions imply, for all already chosen \(s<t\),
\[
\overline U_s\subset U_t.
\tag{Q.3}
\]
Induction constructs the family with (Q.3) for every \(s<t\) in \(D\).

Define
\[
f(x)=\inf\{t\in D:x\in U_t\},
\tag{Q.4}
\]
where the infimum of the empty set in this formula is \(1\). The usual least-lower-bound property of the real numbers makes this a number in \([0,1]\). Points of \(A\) lie in \(U_0\), hence have value zero. Points of \(B\) lie in none of the \(U_t\), hence have value one.

For \(0<a\leq1\), the definition of infimum gives
\[
\{f<a\}=\bigcup_{\substack{t\in D\\t<a}}U_t.
\tag{Q.5}
\]
For \(0\leq a<1\), we also have
\[
\{f>a\}=\bigcup_{\substack{t\in D\\t>a}}
\bigl(X\setminus\overline U_t\bigr).
\tag{Q.6}
\]
To check (Q.6), if \(x\notin\overline U_t\), then it lies in no \(U_s\) with \(s\leq t\), by (Q.3). Thus \(f(x)\geq t>a\). Conversely, if \(f(x)>a\), choose dyadics \(a<t<u<f(x)\). Such choices exist: taking \(2^{-N}\) smaller than one third of the positive interval length yields two dyadic grid points inside that interval. Since \(x\notin U_u\) and \(\overline U_t\subset U_u\), the point \(x\) lies in \(X\setminus\overline U_t\). This proves the reverse inclusion.

The right sides of (Q.5) and (Q.6) are open. For thresholds outside the indicated ranges the same inverse images are either empty or all of \(X\). Open intervals are intersections of two such open rays, and arbitrary open subsets of \([0,1]\) are unions of intervals relative to \([0,1]\). Therefore all open inverse images under \(f\) are open; \(f\) is continuous. □

### The partition theorem

**Theorem Q.3 (continuous partitions of unity).** For every open cover \(\mathcal U\) of a paracompact Hausdorff space \(X\), there are continuous functions \(\lambda_\alpha:X\to[0,1]\) with locally finite supports, each support contained in a member of \(\mathcal U\), such that
\[
\sum_\alpha\lambda_\alpha(x)=1\qquad(x\in X).
\tag{Q.7}
\]
Conversely, a Hausdorff space with this property is paracompact. In particular every compact Hausdorff space has this property.

**Proof.** Use Q.1 to choose a locally finite open cover \(\mathcal R\) with each \(\overline R\) in a selected member of \(\mathcal U\). Apply Q.1 once more to obtain a locally finite open cover \(\mathcal V\) with each \(\overline V\) in a selected member \(R(V)\) of \(\mathcal R\). For \(R\in\mathcal R\), set
\[
F_R=\bigcup_{\substack{V\in\mathcal V\\R(V)=R}}\overline V.
\tag{Q.8}
\]
This is closed, since the closures of \(\mathcal V\) are locally finite. It is contained in \(R\). The sets \(F_R\) cover \(X\), because the sets \(V\) do. The family \((F_R)\) is locally finite since \(F_R\subset R\).

For a nonempty \(F_R\), use (Q.2) to choose an open \(W_R\) with \(F_R\subset W_R\subset\overline W_R\subset R\). By Q.2 there is a continuous \(\psi_R:X\to[0,1]\) equal to one on \(F_R\) and zero on \(X\setminus W_R\). Namely apply that lemma to those disjoint closed sets and subtract its function from one. Its support lies in \(\overline W_R\subset R\). If \(F_R\) is empty, set \(\psi_R=0\). Since \(\mathcal R\) is locally finite, these supports are locally finite. The sum
\[
S(x)=\sum_{R\in\mathcal R}\psi_R(x)
\]
is continuous: in a neighbourhood of each point it is a fixed finite sum of continuous functions. It is at least one at every point, because some \(F_R\) contains that point. Define \(\lambda_R=\psi_R/S\). These functions are continuous, take values in \([0,1]\), have the same supports as \(\psi_R\), and sum to one. Their supports lie in \(\mathcal U\)'s selected members, proving the first assertion.

Conversely, the open sets \(\{\lambda_\alpha>0\}\) cover \(X\), refine \(\mathcal U\), and are locally finite because they lie in the locally finite supports. This is the defining refinement property. Finally an open cover of a compact space has a finite subcover, and that finite cover is itself a locally finite refinement. A compact Hausdorff space is therefore paracompact by definition, so the first assertion applies to it. □

### Metrics, complements and compact fibres

**Lemma Q.4 (continuous bundle metrics and complements).** Every finite-rank real or complex vector bundle on a paracompact Hausdorff base has a continuous positive definite Euclidean or Hermitian metric. If \(W\subset V\) is a vector subbundle, its metric orthogonal complements form a vector subbundle and
\[
V=W\oplus W^\perp.
\tag{Q.9}
\]
The constructions require no differentiable structure on the base.

**Proof.** Let \(U_\alpha\) be trivializing opens. Pull the standard fibre inner product back through each trivialization, obtaining a continuous local form \(h_\alpha\). Take the partition of Q.3 subordinate to that cover, assigning each of its functions to one such trivialization. Multiply the assigned local form by the function and extend by zero outside the trivializing open. This extension is continuous: at a point outside that open the point lies outside the closed support of the function, so the extension vanishes on a neighbourhood. The locally finite sum
\[
h_x(v,w)=\sum_\alpha\lambda_\alpha(x)\,h_{\alpha,x}(v,w)
\tag{Q.10}
\]
is continuous in local bundle coordinates, symmetric or Hermitian as appropriate. A nonzero vector has strictly positive squared length in each local form defined at its base point, and at least one weight there is positive. Thus \(h_x(v,v)>0\). The Hermitian convention here is conjugate-linear in the first argument.

It remains to verify that the pointwise complements really are a bundle. If the local rank of \(W\) is zero, its complement is all of \(V\) and its projection is zero. If it equals the rank of \(V\), the complement is the zero bundle and the projection is the identity. These cases need no inverse of an empty matrix. In the remaining cases, use a local trivialization of \(V\), write its metric as a positive definite matrix \(H(x)\), and the columns of a local frame of \(W\) as an \(r\)-by-\(k\) matrix \(T(x)\). With transpose in the real case and conjugate transpose in the complex case, define
\[
P(x)=T(x)\bigl(T(x)^*H(x)T(x)\bigr)^{-1}T(x)^*H(x).
\tag{Q.11}
\]
The middle matrix is invertible: if \(a\ne0\), then \(Ta\ne0\) and
\(a^*T^*HTa=h_x(Ta,Ta)>0\), so its kernel is zero. The basis-exchange proof in opening lesson 0.2 works over \(\mathbb C\) too: it uses only solving for a vector whose scalar coefficient is nonzero. For a square \(k\)-by-\(k\) matrix with zero kernel, its \(k\) columns are independent. Successively exchange them into the standard spanning list, as in that proof; after all \(k\) exchanges they are a spanning list as well. The map is therefore onto and has a linear inverse. Continuity of the inverse follows from the local Neumann-series inverse argument of opening lesson 0.4. For a complex matrix apply that real argument to its matrix on real and imaginary coordinates; the inverse commutes with multiplication by \(i\), because the original matrix does, so it is the required complex inverse.

Formula (Q.11) is continuous, satisfies \(PT=T\), and satisfies \(P^2=P\) by direct multiplication. Furthermore
\[
T^*H(v-Pv)=0.
\]
Thus \(Pv\in W\) and \(v-Pv\) is perpendicular to \(W\), so \(P\) is the orthogonal projection. The two summands have zero intersection, since a vector perpendicular to itself has squared norm zero; this proves (Q.9) fibrewise.

At a fixed base point \(x_0\), choose a basis \(v_1,\ldots,v_{r-k}\) of \(\ker P(x_0)\), expressed as constant vectors in the chosen trivialization. The continuous vectors \((1-P(x))v_j\), together with the columns of \(T(x)\), give a square matrix that is invertible at \(x_0\). Local inversion as just proved makes it invertible on a neighbourhood of \(x_0\). Its last columns lie in \(\ker P(x)\). Since the first columns span \(W_x\) and the full matrix is a basis, the last columns span exactly its complementary summand. Their coordinate inverse is continuous by the same local inversion argument. They therefore give a genuine bundle chart for \(W^\perp\). Addition \(W\oplus W^\perp\to V\) is continuous in bundle charts, and its inverse is the continuous map \(v\mapsto(Pv,(1-P)v)\). Thus (Q.9) is a bundle isomorphism, proving the assertion. □

**Lemma Q.5 (compact-fibre total spaces).** A locally trivial fibre bundle with compact Hausdorff fibre \(F\) over a paracompact Hausdorff base \(B\) has paracompact Hausdorff total space.

**Proof.** Points over different base points are separated by preimages of disjoint base neighbourhoods. Two distinct points over the same base point have coordinates \((b,f_1),(b,f_2)\) in a common bundle chart \(U\times F\). Choose disjoint open fibre neighbourhoods \(O_1,O_2\) of \(f_1,f_2\); the open sets \(U\times O_1,U\times O_2\) separate them in the total space. Thus the total space is Hausdorff.

Let \(\mathcal O\) be an open cover of the total space. Fix \(b\) and a trivialization near \(b\). For each \(f\in F\), some member of \(\mathcal O\) contains \((b,f)\). The definition of the product topology supplies an open rectangle \(U_f\times W_f\) containing \((b,f)\) and contained in that member, inside the fixed trivialization. Compactness of \(F\) selects finitely many \(W_f\)'s that cover \(F\). Intersect their finitely many \(U_f\)'s, obtaining an open base neighbourhood \(U_b\) on which those same finitely many rectangles cover every fibre and refine \(\mathcal O\).

Take a locally finite open refinement \((R_\alpha)\) of the base cover \((U_b)\), assigning a containing \(U_b\) to each \(R_\alpha\). In its assigned trivialization use the finitely many sets \(R_\alpha\times W_f\). They form an open refinement of \(\mathcal O\) covering the total space. Near a given total-space point, the inverse image of a base neighbourhood meets only finitely many \(R_\alpha\)'s, and each contributes only finitely many of these sets. This refinement is therefore locally finite. That is the defining paracompactness property. If the fibre is empty, the total space is empty and the assertion is immediate. □

### A countable collection of trivializing opens

**Lemma Q.6 (countable trivializations with a subordinate partition).** Given an open cover \((U_\alpha)\) of a paracompact Hausdorff space, there is a countable open cover \((V_k)_{k\geq1}\) such that every \(V_k\) is a disjoint union of open subsets, each contained in a member of the original cover. There are continuous functions \(\mu_k\) with locally finite supports contained in \(V_k\) and \(\sum_k\mu_k=1\). If the original opens trivialize a fixed finite-rank bundle, every \(V_k\) also trivializes that bundle.

**Proof.** Choose a subordinate partition \((\lambda_\beta)\) from Q.3, retaining for each index an assigned original open. For each finite nonempty set \(S\) of partition indices, put
\[
V_S=\left\{x:
\min_{\beta\in S}\lambda_\beta(x)>0,\quad
\min_{\beta\in S}\lambda_\beta(x)>
\sup_{\gamma\notin S}\lambda_\gamma(x)\right\},
\tag{Q.12}
\]
where the supremum includes zero. The supremum is locally the maximum of zero and finitely many continuous functions, since the supports are locally finite. The finite minimum and maximum are continuous: for two functions this follows from
\(\min(a,b)=(a+b-|a-b|)/2\) and \(\max(a,b)=(a+b+|a-b|)/2\), and induction handles a finite list. Thus \(V_S\) is open. It is contained in the assigned \(U_\alpha\) of any \(\beta\in S\), since \(\lambda_\beta>0\) there.

If \(S,T\) have the same cardinality and are different, choose \(\beta\in S\setminus T\) and \(\gamma\in T\setminus S\). At a point of \(V_S\) we would have \(\lambda_\beta>\lambda_\gamma\), whereas at a point of \(V_T\) we would have the opposite inequality. Hence \(V_S\cap V_T=\varnothing\). Set
\[
V_k=\bigcup_{|S|=k}V_S.
\tag{Q.13}
\]
This is the asserted disjoint open union. At a given point, the set \(S\) of positive partition values is finite, nonempty, and has positive minimum; all values outside it are zero. That point lies in \(V_S\), so the \(V_k\)'s cover \(X\).

Apply Q.3 to this countable cover. It gives a possibly differently indexed locally finite partition \((\eta_\delta)\), with the support of each term assigned to some \(V_{k(\delta)}\). Define
\[
\mu_k=\sum_{k(\delta)=k}\eta_\delta.
\tag{Q.14}
\]
These are continuous locally finite sums. Their supports are contained in the union of the corresponding supports of \(\eta_\delta\): that union is closed by local finiteness, and contains the set where \(\mu_k\ne0\). It lies in \(V_k\), so no extra boundary point is introduced by grouping. Only finitely many \(\eta_\delta\) supports meet a sufficiently small neighbourhood of each point, hence only finitely many grouped supports do. Finally \(\sum_k\mu_k=\sum_\delta\eta_\delta=1\).

If the original cover trivializes a bundle, choose one such chart on each \(V_S\), by restricting any assigned original chart. For a fixed \(k\), these charts combine into a trivialization on \(V_k\): its pieces are disjoint and open, so both the combined map and its inverse are continuous, as can be checked on those open pieces. The fibre rank is fixed, so their target is the common product \(V_k\times\mathbb F^r\). This proves the last assertion. □
## 3. Finite attachments and their singular groups

### The topology of a finite attachment

**Lemma P.1 (finite attachment quotient).** Let \(Y\) be compact Hausdorff, let \(q\geq1\), and let finitely many maps \(f_\alpha:S^{q-1}\to Y\) be continuous. Form
\[
X=\left(Y\amalg\coprod_{\alpha=1}^{c}D^q_\alpha\right)/
\bigl(z\sim f_\alpha(z)\text{ for }z\in\partial D^q_\alpha\bigr).
\tag{P.1}
\]
Then \(X\) is compact Hausdorff, the included \(Y\) is a closed subspace with its original topology, and \(X\setminus Y\) is the disjoint union of the open disk interiors with their usual topology. If \(Q\) denotes the quotient map in (P.1), then \(Q\times\operatorname{id}_{[0,1]}\) is a quotient map. Its restriction over an open subset of \(X\times[0,1]\) is a quotient map as well.

**Proof.** Write \(K=Y\amalg\coprod_\alpha D^q_\alpha\). The disks are compact by the bounded closed Euclidean-set theorem of opening lesson 0.1. A finite disjoint union of compact spaces is compact, since an open cover has a finite subcover on each of its finitely many pieces. It is Hausdorff: points on different pieces are separated by the pieces, and points on one piece separate there.

We recall two elementary compactness facts needed for the quotient. A compact subset \(C\) of a Hausdorff space is closed. For a point outside \(C\), choose disjoint neighbourhoods of it and each point of \(C\); finitely many neighbourhoods of points of \(C\) cover \(C\), and the intersection of the corresponding finitely many neighbourhoods of the outside point avoids \(C\). The product of two compact spaces is compact. Indeed refine an open cover of the product by rectangles. For each point of the first factor, finitely many rectangles cover the second factor above that point; intersect their first-factor neighbourhoods. Finitely many of these intersections cover the first factor, and the corresponding finitely many rectangles then cover the product. A closed subset of a compact space is compact: extend any of its open covers by the open complement, select a finite subcover of the whole space, and then omit the complement. A continuous image of a compact space is compact because inverse images of an open cover give an open cover of its domain. These facts and the product argument also apply to closed subsets of compact Hausdorff spaces and their finite products.

Let \(A=\coprod_\alpha\partial D^q_\alpha\subset K\), and combine the attaching maps into \(f:A\to Y\). The equivalence relation \(\mathcal R\subset K\times K\) in (P.1) consists exactly of the diagonal, the graph of \(f\), its transpose, and the pairs \((a,a')\in A\times A\) with \(f(a)=f(a')\). Each is closed. The diagonal is closed by the Hausdorff property. The graph is a compact image of \(A\) in the Hausdorff product \(K\times K\), hence closed; the same applies to its transpose. The last set is closed in the closed subset \(A\times A\), since it is the inverse image of the closed diagonal of \(Y\times Y\). Thus \(\mathcal R\) is closed.

If \(C\subset K\) is closed, its saturation under this relation is
\[
\operatorname{Sat}(C)
=\operatorname{pr}_2\bigl((C\times K)\cap\mathcal R\bigr).
\tag{P.2}
\]
The set being projected is compact, and its image is a compact subset of Hausdorff \(K\), so the saturation is closed. Since \(Q^{-1}Q(C)=\operatorname{Sat}(C)\), the definition of the quotient topology says that \(Q(C)\) is closed. Therefore \(Q\) is a closed map.

Distinct equivalence classes \(C_1,C_2\) are disjoint closed subsets of \(K\): a class is the inverse image of \(\mathcal R\) under \(y\mapsto(x,y)\) for a fixed representative \(x\). Compact Hausdorff \(K\) is normal by Q.1 and Q.3. Choose disjoint open neighbourhoods \(O_1,O_2\) of \(C_1,C_2\). The sets
\[
W_i=K\setminus\operatorname{Sat}(K\setminus O_i)
\]
are open, saturated, contain \(C_i\), and are contained in \(O_i\). They are disjoint. Their images under \(Q\) are open, since their full inverse images are the \(W_i\), and separate the two quotient points. Hence \(X\) is Hausdorff. It is compact as the continuous image of \(K\).

No two distinct points of \(Y\) are identified. Its map into \(X\) is therefore a continuous injection from a compact space to a Hausdorff space. It is a homeomorphism to its image: any closed subset of \(Y\) is compact and has closed image. That image itself is compact and hence closed in \(X\). Every point in a disk interior is alone in its equivalence class. An open subset of a disk interior is open in \(K\), is saturated, and consequently has open image in \(X\). Thus the disk interiors give the asserted open disjoint pieces of \(X\setminus Y\).

Finally \(K\times[0,1]\) is compact and \(X\times[0,1]\) is Hausdorff. The continuous surjection \(Q\times\operatorname{id}\) is closed by the same compact-image argument, so it is a quotient map: a set with closed full inverse image is the image of that closed inverse image, and hence is closed. A quotient map restricted over an open set remains quotient. To verify this last assertion, if a subset of the open target has open inverse image relative to the restricted domain, that inverse image is open in the full domain because the restricted domain is open. The original quotient criterion then makes the subset open in the full target and hence in the open target. The reverse implication is continuity. □

### Relative cell groups without a cellular comparison theorem

**Lemma P.2 (relative groups of a finite attachment).** For (P.1), any abelian group \(G\), and \(q\geq1\),
\[
H_i(X,Y;G)=
\begin{cases}G^{\,c},&i=q,\\0,&i\ne q,\end{cases}
\qquad
H^i(X,Y;G)=
\begin{cases}G^{\,c},&i=q,\\0,&i\ne q.\end{cases}
\tag{P.3}
\]
The direct sums have one term for each attached disk.

**Proof.** Let \(N\subset X\) contain \(Y\) and, in each disk, the image of the collar \(\{z:|z|>1/2\}\). Its inverse image under \(Q\) is the union of \(Y\) and these collars, open in the disjoint union \(K\); therefore \(N\) is open in \(X\). It contains \(Y\).

On the collar write \(z=ru\), \(r>1/2\), \(|u|=1\), and define
\[
h_t(ru)=\bigl((1-t)r+t\bigr)u .
\tag{P.4}
\]
Keep \(Y\) fixed. On a disk boundary this formula fixes \(u\), and thus respects its identification with \(f_\alpha(u)\). It descends to a map \(N\times[0,1]\to N\). This descended map is continuous: before descent its formulas are continuous on each piece of \(Q^{-1}N\times[0,1]\), agree on the identifications, and \(Q\times\operatorname{id}\) restricted over \(N\times[0,1]\) is quotient by P.1. The radius in (P.4) remains above \(1/2\), and at \(t=1\) reaches the boundary. Hence it is a deformation retraction of \(N\) onto \(Y\).

The prism homotopy K.1 makes \(H_*(N,Y;G)\) and \(H^*(N,Y;G)\) zero. The exact triple sequences E.1 for \(Y\subset N\subset X\) then show that replacing \(Y\) by \(N\) is an isomorphism on relative homology and cohomology: the groups on either side of the replacement map in those sequences are zero. Since \(Y\) is closed in \(X\) and lies in the open set \(N\), excision E.2 removes it. We obtain the pair
\[
(X\setminus Y,N\setminus Y)
\cong\coprod_{\alpha=1}^{c}
\bigl(\mathring D^q,\{z:1/2<|z|<1\}\bigr).
\tag{P.5}
\]
The first space of each pair contracts to its origin along line segments. Its second space deformation retracts to the sphere of radius \(3/4\), by replacing the radius \(r\) at time \(t\) by \((1-t)r+3t/4\). That radius stays strictly between \(1/2\) and \(1\). Multiplication by \(4/3\) identifies the resulting sphere with \(S^{q-1}\).

The reduced pair sequences and the sphere calculation E.5 now give a single copy of \(G\) in relative degree \(q\) and zero in all other degrees, for homology and cohomology. Explicitly, contractibility of the first space makes its reduced groups zero, so the relative group in degree \(i\geq1\) equals the reduced sphere group in degree \(i-1\). In degree zero the relative homology is zero because the second space meets the unique path component of the first. The degree-zero relative cohomology is zero because a constant function on the first space that vanishes on the nonempty second space is zero. When \(q=1\), the sphere has two points and its reduced degree-zero group is \(G\); this gives the required relative degree-one group, so that case is included.

A singular simplex in a disjoint union of open pieces lies in one piece: its connected domain has connected image, and two distinct open pieces would separate that image. Connectedness of the simplex is proved in E.5 by its line segments. Thus the chain complex of the finite disjoint union in (P.5) is the direct sum of the complexes of those pairs. Its dual cochain complex is the finite product, which equals the finite direct sum. Combining the one-disk calculations proves (P.3). □

### The consequences used for projective spaces

A finite cell complex here starts with finitely many points and repeatedly attaches finitely many disks, in nondecreasing dimensions, through maps of their boundary spheres to the preceding stage. Its \(q\)-skeleton contains the cells of dimensions at most \(q\). P.1 proves at every stage that the space is compact Hausdorff and the earlier skeleton is closed.

**Corollary P.3 (dimension and even-cell calculations).** A finite cell complex of dimension \(d\) has
\[
H_i(X;G)=H^i(X;G)=0\qquad(i>d)
\tag{P.6}
\]
for every abelian group \(G\). Over a field, the dimension of its top cohomology is at most the number of \(d\)-cells. If all cells have even dimension, its integral homology is free, with one generator for each cell in its dimension and zero in odd degrees. Attaching \(q\)-cells preserves the homology and cohomology groups in degrees strictly below \(q-1\).

**Proof.** The finite zero-skeleton has one copy of \(G\) per point in degree zero and no higher groups, by the point computation and disjoint-union calculation in E.1 and P.2. Suppose cells of dimension \(q>0\) are attached to \(X_{q-1}\). The relative groups in the pair sequence are zero except in degree \(q\), by P.2. If the old groups vanish above \(q-1\), exactness therefore forces the new groups to vanish above \(q\). This argument applies to homology and cohomology and proves (P.6) by induction.

For dimension zero, the asserted top bound is exactly the finite-point calculation just given. For positive dimension, the exact segment for the top cohomology is
\[
H^d(X_d,X_{d-1};k)\longrightarrow H^d(X_d;k)
\longrightarrow H^d(X_{d-1};k)=0.
\tag{P.7}
\]
Thus \(H^d(X_d;k)\) is a quotient of one copy of \(k\) per \(d\)-cell. The images of those coordinate generators span the quotient, which proves the dimension bound.

If cells occur only in even dimensions, suppose the next attachment has dimension \(2a\). The preceding skeleton has dimension at most \(2a-2\). Its homology in degrees \(2a\) and \(2a-1\) is zero, so exactness identifies the new degree-\(2a\) homology with the relative free group \(\mathbb Z^{\,c_{2a}}\) and leaves the new degree-\((2a-1)\) group zero. In smaller degrees both neighbouring relative terms vanish, so the old groups are unchanged. Starting with the free group on the zero-cells proves the even-cell assertion.

Finally, for a \(q\)-cell attachment and a degree \(i<q-1\), the relative groups in degrees \(i\) and \(i+1\) both vanish. The pair homology sequence therefore makes \(H_i(X_{q-1};G)\to H_i(X_q;G)\) an isomorphism. The corresponding cohomology segment gives an isomorphism in the opposite direction. This proves the stated preservation in low degrees. □
## 4. Projective spaces and the Euler generators

Write \(\mathbb F=\mathbb R\) or \(\mathbb C\), and \(d=\dim_{\mathbb R}\mathbb F\), so \(d=1\) or \(2\). We use the standard Euclidean norm, and \(v^*\) means transpose or conjugate transpose. Coordinates of \(\mathbb F^{n+1}\) have indices \(0,\ldots,n\).

### The spaces and their tautological lines

**Lemma R.1 (finite projective topology).** The space \(\mathbb F P^n\) of lines in \(\mathbb F^{n+1}\), with the quotient topology from nonzero vectors, is a compact Hausdorff smooth real \(dn\)-manifold. For \(n>0\) it is path connected. Its tautological line bundle \(\gamma_{\mathbb F}\) has unit sphere bundle
\[
S(\gamma_{\mathbb F})\cong S^{d(n+1)-1}.
\tag{R.1}
\]
There is one cell in each dimension \(0,d,\ldots,dn\); the inclusions \(\mathbb F P^{n-1}\subset\mathbb F P^n\) are closed and pull the tautological line back to the corresponding smaller tautological line.

**Proof.** For \(v\ne0\), form the matrix
\[
P(v)=\frac{vv^*}{v^*v}.
\tag{R.2}
\]
It is unchanged by multiplying \(v\) by a nonzero scalar. It is an idempotent matrix with image exactly \(\mathbb Fv\): multiplication sends \(w\) to \(v(v^*w)/(v^*v)\), sends \(v\) to itself, and has all values in that line. Consequently two matrices \(P(v),P(w)\) are equal exactly when the represented lines are equal.

Let \(\mathcal P_n\) be their set, with the subspace topology in the finite-dimensional real vector space of matrices. It is Hausdorff. It is compact, since (R.2) maps the compact unit sphere continuously onto it. The sphere map is a closed surjection: a closed subset of the sphere is compact and has compact, hence closed, image in the Hausdorff target. As in P.1, it is therefore quotient. The map from all nonzero vectors is also quotient. Indeed if a subset of \(\mathcal P_n\) has open inverse image there, its inverse image on the sphere is open, so the subset is open by the sphere quotient property. The reverse implication is continuity. Thus \(\mathcal P_n\) has precisely the specified line quotient topology, proving compactness and Hausdorffness of \(\mathbb F P^n\).

On the open set \(U_j=\{P:P_{jj}>0\}\), the representing line has nonzero \(j\)-th coordinate. Its representative with \(j\)-th coordinate equal to one has the other coordinates
\[
z_i=\frac{P_{ij}}{P_{jj}}=\frac{v_i}{v_j}\qquad(i\ne j).
\tag{R.3}
\]
These are continuous functions of \(P\). Conversely, inserting one in the \(j\)-th position of \((z_i)_{i\ne j}\) gives a vector \(w_j(z)\), and \(z\mapsto P(w_j(z))\) is a continuous inverse. This is a chart \(U_j\cong\mathbb F^n\). On chart overlaps the changes of coordinates divide the relevant coordinates by a nonzero coordinate. They and their inverses are smooth as real maps. These finitely many charts cover the space and give a smooth manifold without boundary. A countable basis in each Euclidean chart gives a countable basis of the manifold. For \(n>0\), each \(U_j\) is path connected by the line segments in its coordinate space, and all contain the line represented by \((1,\ldots,1)\). Paths to that common point show that their union is path connected. For \(n=0\), the space is a single point.

The tautological total space is
\[
E_\gamma=\{(P,v)\in\mathcal P_n\times\mathbb F^{n+1}:Pv=v\}.
\tag{R.4}
\]
On \(U_j\), its bundle chart is \((P,t)\mapsto(P,t\,w_j(P))\); the inverse recovers the scalar as the \(j\)-th coordinate \(v_j\). Both maps are continuous, so these are genuine line-bundle charts. The standard norm on the second factor restricts to a fibre metric. The map from the unit sphere to its sphere bundle is
\[
v\longmapsto(P(v),v),
\]
with continuous inverse given by its second coordinate. This proves (R.1).

Appending a zero last coordinate embeds \(\mathbb F P^{n-1}\) as the closed locus \(P_{nn}=0\) in \(\mathbb F P^n\). Formula (R.4) directly identifies the pullback line with the smaller tautological line. For \(n\geq1\), define a characteristic map from the real \(dn\)-disk by
\[
\chi_n(z)=\left[z_0:\cdots:z_{n-1}:\sqrt{1-|z|^2}\right],
\qquad z\in\mathbb F^n,\quad |z|\leq1 .
\tag{R.5}
\]
Its representing vector is nonzero everywhere, so the map is continuous. On the boundary it is the line \([z:0]\) in \(\mathbb F P^{n-1}\). In the interior, the last coordinate is positive real, and the affine coordinates are
\[
\frac{z}{\sqrt{1-|z|^2}}.
\]
This is a homeomorphism to \(\mathbb F^n\), with inverse \(w\mapsto w/\sqrt{1+|w|^2}\). Equivalently every line with nonzero last coordinate has a unique unit representative with last coordinate positive real. Thus (R.5), together with the inclusion of the smaller projective space, gives a continuous bijection from the attachment quotient in P.1 to \(\mathbb F P^n\). Its compact source and Hausdorff target make it a homeomorphism, since images of closed sets are compact and hence closed. Beginning with the single point \(\mathbb F P^0\), this gives exactly one cell in dimensions \(0,d,\ldots,dn\). □

### Complex orientations and dual lines

**Lemma R.2 (complex orientation and dual sign).** The complex charts of \(\mathbb C P^n\) give it an orientation. A complex vector space is oriented by the real ordered basis
\[
v_1,iv_1,\ldots,v_r,iv_r
\tag{R.6}
\]
of a complex basis. These orientations are independent of the chosen complex basis. A complex line bundle has the corresponding orientation as a real rank-two bundle. If a complex line \(L\) has a Hermitian metric, then
\[
e((L^*)_{\mathbb R})=-e(L_{\mathbb R}).
\tag{R.7}
\]
Also \(e(\overline L_{\mathbb R})=-e(L_{\mathbb R})\), where \(\overline L\) is the conjugate complex line. In particular the dual formula applies on a paracompact Hausdorff base by Q.4.

**Proof.** Write a complex change-of-basis matrix as \(A=B+iC\). In the order listing all real coordinates and then all imaginary coordinates, its real matrix is
\[
A_{\mathbb R}=\begin{pmatrix}B&-C\\C&B\end{pmatrix}.
\]
Over \(\mathbb C\), the invertible coordinate change
\((x,y)\mapsto(x+iy,x-iy)\), with inverse
\((z,w)\mapsto((z+w)/2,(z-w)/(2i))\), conjugates this matrix to
\(\operatorname{diag}(A,\overline A)\). The determinant permutation, multiplicativity and block-triangular arguments of DG-CHAR-06 L.1 and DG-CHAR-07 F.2 use only finite sums, products and commutativity of scalars, so their same derivations apply over \(\mathbb C\). They give
\[
\det_{\mathbb R}(A_{\mathbb R})
=\det_{\mathbb C}(A)\det_{\mathbb C}(\overline A)
=|\det_{\mathbb C}A|^2>0.
\tag{R.8}
\]
The second equality follows term by term from the permutation formula and complex conjugation. The determinant is nonzero because \(A\) is invertible. Changing from the grouped real/imaginary order to the interleaved order (R.6) conjugates by the same permutation matrix on the source and target, so it does not change this determinant. This proves independence of (R.6) and the complex-bundle orientation rule.

The chart changes in R.1 over \(\mathbb C\) have complex-linear derivatives. To check this without an analytic convention, the reciprocal map has derivative \(h\mapsto-h/z^2\) at \(z\ne0\), because
\[
\frac1{z+h}-\frac1z+\frac{h}{z^2}
=\frac{h^2}{z^2(z+h)},
\]
whose absolute value divided by \(|h|\) tends to zero. Multiplication of complex numbers is real bilinear, so its derivative follows by expanding the product, with the product of increments as the quadratic remainder. The product and chain rules of opening lesson 0.3 therefore give complex-linear derivatives for each coordinate quotient. Differentiating the inverse chart change by the chain rule shows that these derivatives are invertible. Equation (R.8) makes their real determinants positive, so the complex charts define the asserted manifold orientation.

Use the Hermitian convention of Q.4: the form is conjugate-linear in its first argument. The map
\[
\Psi:L\longrightarrow L^*,\qquad
w\longmapsto\bigl(v\longmapsto h(w,v)\bigr)
\tag{R.9}
\]
is conjugate-linear on each fibre. It is a continuous real bundle isomorphism, as is seen in a local complex frame: for a positive continuous metric coefficient \(a\), its coordinate is \(w\mapsto a\overline w\), with continuous inverse \(z\mapsto\overline z/a\). Its real determinant is \(-a^2<0\), so it reverses the complex orientation of a line. The naturality and orientation-reversal rule for the Thom and Euler classes in T.4 therefore give (R.7). The dual line charts used here are obtained by taking coordinate linear functionals dual to each frame; their transition scalars are inverses of the original ones.

The conjugate line has the same underlying real fibres, with complex multiplication \(a\cdot_{\overline L}v=\overline a\,v\). The identity of the underlying real bundles is conjugate-linear between the complex structures and has coordinate conjugation in their respective complex frames. It reverses the real orientation of a line. Applying the same T.4 rule proves the conjugate formula. □

### The real generator

**Theorem R.3 (finite real projective cohomology).** Put \(a=e_2(\gamma_{\mathbb R})\). Then
\[
H^*(\mathbb R P^n;\mathbb F_2)
\cong \mathbb F_2[a]/(a^{n+1}),\qquad |a|=1.
\tag{R.10}
\]
Its homology over \(\mathbb F_2\) is one dimensional in degrees \(0,\ldots,n\) and zero otherwise. Restriction from a larger finite projective space sends its indicated Euler generator and all its powers to the corresponding classes in the smaller space.

**Proof.** For \(n=0\) the space is a point, so its positive-degree groups vanish and the asserted presentation holds with \(a=0\). Suppose \(n\geq1\). R.1 identifies the unit sphere bundle of the real tautological line with \(S^n\). The mod-two sequence S.1 and S.3 therefore applies with rank one and Euler class \(a\).

The sphere and the base are path connected. The base assertion was proved in R.1. For the sphere one can connect unit vectors \(u,v\) by normalizing their straight segment unless \(v=-u\); in that case choose a vector \(z\) outside the line of \(u\), subtract \(\langle z,u\rangle u\), and normalize the nonzero result to a unit vector perpendicular to \(u\). Such a \(z\) exists in dimension at least two by finite basis extension. Concatenating the two normalized segments through that perpendicular vector gives a path. Hence the map on degree-zero cohomology from the base to the sphere is the identity on the constant functions \(\mathbb F_2\), by E.1. Exactness forces the following map \(H^0(S^n;\mathbb F_2)\to H^0(\mathbb R P^n;\mathbb F_2)\) to be zero. It follows that multiplication by \(a\) from \(H^0\) to \(H^1\) is injective.

For \(1\leq j<n\), the sphere groups adjoining the multiplication map
\[
H^{j-1}(\mathbb R P^n;\mathbb F_2)
\xrightarrow{\ \smile a\ }
H^j(\mathbb R P^n;\mathbb F_2)
\tag{R.11}
\]
give an isomorphism: for \(j=1\), injectivity is the preceding degree-zero argument and surjectivity follows from \(H^1(S^n)=0\); for \(j>1\), both adjoining positive-degree sphere groups vanish by E.5. At \(j=n>1\), the preceding group \(H^{n-1}(S^n)\) is still zero, so (R.11) is injective. When \(n=1\), its injectivity is again the degree-zero argument.

There is one top cell in R.1, so P.3 bounds the dimension of \(H^n\) by one. The injective last multiplication produces the nonzero class \(a^n\) there, so it is a basis. Inductively \(1,a,\ldots,a^n\) are bases in the indicated degrees. Groups above \(n\) vanish by P.3. Multiplication of powers is associative by K.5, and degree forces \(a^{n+1}=0\). The homomorphism from the displayed polynomial quotient sends its one basis element in each degree to the corresponding basis just found, so it is a ring isomorphism.

The field evaluation theorem after U.3 identifies cohomology with the full dual of homology. A vector space with one-dimensional full dual is itself one dimensional: a nonzero functional implies that the space is nonzero, while two independent vectors would extend to a basis and give two independent coordinate functionals. A vector space with zero full dual is zero by the same basis-extension argument applied to any putative nonzero vector. This proves the homology assertion without a cellular differential computation. Finally R.1 identifies the restricted tautological bundles; Euler naturality T.4 and cup naturality then give the restriction assertion. □

### The integral complex generator and its normalization

**Theorem R.4 (finite complex projective cohomology).** Put
\[
x=-e((\gamma_{\mathbb C})_{\mathbb R}).
\tag{R.12}
\]
Then
\[
H^*(\mathbb C P^n;\mathbb Z)
\cong\mathbb Z[x]/(x^{n+1}),\qquad |x|=2.
\tag{R.13}
\]
The integral homology is \(\mathbb Z\) in degrees \(0,2,\ldots,2n\) and zero otherwise. For any abelian group \(G\), the operation sending \(g\in G\) to \(g\,x^i\) identifies \(G\) with \(H^{2i}(\mathbb C P^n;G)\), for \(0\leq i\leq n\), and all other cohomology groups are zero. For the complex orientation,
\[
\langle x^n,[\mathbb C P^n]\rangle=1.
\tag{R.14}
\]
Restrictions preserve the displayed generator and its powers.

**Proof.** R.2 orients the underlying real rank-two tautological bundle. Its sphere bundle is \(S^{2n+1}\) by R.1. For \(n\geq1\), S.1 and S.3 give the integral Gysin sequence with Euler class \(e=-x\). Its segment in degree one makes \(H^1(\mathbb C P^n;\mathbb Z)=0\): the preceding base group has negative degree and the next group is \(H^1(S^{2n+1};\mathbb Z)=0\). For \(2\leq j\leq2n\), both adjoining sphere groups in positive degrees \(j-1,j\) are zero. Thus
\[
\smile e:H^{j-2}(\mathbb C P^n;\mathbb Z)
\xrightarrow{\ \cong\ }H^j(\mathbb C P^n;\mathbb Z).
\tag{R.15}
\]
The base is path connected, so \(H^0=\mathbb Z\) with generator one. Induction gives zero odd groups and generators \(e^i\), equivalently \(x^i\), in even degrees through \(2n\). The cell structure of R.1 and P.3 give vanishing above \(2n\). Exactly as for R.10, these bases and multiplication of powers prove (R.13). For \(n=0\), the point calculation proves it directly.

The cells all have even dimensions, one in each even degree through \(2n\). Their integral homology is consequently as stated by P.3. In the cohomological universal coefficient sequence U.3 the adjacent Ext term is zero: each integral homology group is free or zero, and a free presentation with zero kernel has zero Ext by the definition there. Evaluation therefore gives
\[
H^q(\mathbb C P^n;G)
\cong\operatorname{Hom}_{\mathbb Z}
       (H_q(\mathbb C P^n;\mathbb Z),G).
\tag{R.16}
\]
For \(q=2i\), the integral generator \(x^i\) is a generator of the full dual of the infinite cyclic homology group, so it evaluates as \(1\) on one choice of its generator. Changing coefficients by \(\mathbb Z\to G,\ 1\mapsto g\), therefore realizes every homomorphism in (R.16), uniquely. This is the meaning of \(g\,x^i\); \(G\) need not be a ring. In all other degrees the homology and Ext terms give zero.

It remains to specify the sign geometrically. The tautological line has its inherited Hermitian metric, so R.2 identifies \(x\) with the Euler class of its complex dual. Over \(\mathbb C P^n\), take the ordered direct sum of \(n\) copies of this dual line, and the section whose components are the coordinate functionals
\[
\lambda_j(v_0,\ldots,v_n)=v_j,\qquad 0\leq j<n,
\]
restricted to the represented line. All these functionals vanish on exactly the line \([0:\cdots:0:1]\). On the last affine chart, use the tautological frame \((z_0,\ldots,z_{n-1},1)\), and the corresponding dual frames. The section's coordinates are exactly \((z_0,\ldots,z_{n-1})\). Its real derivative at that zero is the identity in the complex-oriented base and ordered complex-oriented fibre coordinates. Thus its local index is \(+1\) by N.1.

The base is compact and has the smooth orientation established in R.1–R.2. The zero formula N.2 applies to this isolated, nondegenerate zero and gives Euler evaluation one. By the ordered direct-sum rule T.4, the Euler class of the sum is \(x^n\): its ordering is the interleaved complex orientation used throughout. This proves (R.14) for \(n\geq1\). For \(n=0\), the base is its canonically positive point and \(x^0=1\), so the same equality is the point evaluation. In particular \(x\) evaluates to one on \(\mathbb C P^1\). The tautological restriction statement in R.1 and Euler/cup naturality prove the final assertion. □

### The Hopf example

**Corollary R.5 (the Hopf sphere bundle).** The unit sphere bundle of \(\gamma_{\mathbb C}\) over \(\mathbb C P^1\) is the map \(S^3\to\mathbb C P^1\cong S^2\) sending a unit vector to its complex line. With \(x\) as in R.12, its Euler class is \(-x\), multiplication by that class is an isomorphism \(H^0(S^2;\mathbb Z)\to H^2(S^2;\mathbb Z)\), and the normalization S.6 gives an isomorphism
\[
\partial_\gamma:H^3(S^3;\mathbb Z)\xrightarrow{\ \cong\ }H^2(S^2;\mathbb Z).
\tag{R.17}
\]
The sphere-bundle projection has no continuous section.

**Proof.** R.1 identifies its total space and projection. To identify the base explicitly, send
\[
[w:1]\longmapsto
\frac{(2\operatorname{Re}w,\,2\operatorname{Im}w,\,1-|w|^2)}
     {1+|w|^2},\qquad [1:0]\longmapsto(0,0,-1).
\tag{R.18}
\]
The three coordinates have squared norm one by expansion. Away from the south pole the inverse is
\(w=(X+iY)/(1+Z)\). At infinity use the second projective coordinate \(\eta=1/w\); the formula becomes
\[
\frac{(2\operatorname{Re}\eta,\,-2\operatorname{Im}\eta,\,|\eta|^2-1)}
     {1+|\eta|^2}.
\]
It extends continuously, and indeed smoothly, at \(\eta=0\), with inverse coordinate \(\eta=(X-iY)/(1-Z)\) away from the north pole. These formulas show bijectivity and continuity of the map on both projective charts. Compactness and Hausdorffness make it a homeomorphism. The displayed inverse expressions in the two stereographic charts are smooth, so it is a diffeomorphism.

At \(w=0\), the ordered real coordinate derivatives of (R.18) are \(2e_1,2e_2\), and the outward normal is \(e_3\); their ordered determinant is positive. The real derivative is invertible everywhere because this is a diffeomorphism, and its sign is continuous and cannot change on the connected base. Thus it identifies the complex orientation with the outward orientation of \(S^2\).

The Euler class is \(-x\) by definition, and R.4 shows that it generates \(H^2\), so its multiplication from \(H^0\) is an isomorphism. In the Gysin sequence, the segment around (R.17) has the adjoining groups \(H^3(\mathbb C P^1;\mathbb Z)\) and \(H^4(\mathbb C P^1;\mathbb Z)\), both zero. Exactness gives (R.17); the other groups of the total space are those of \(S^3\) by E.5.

A section of the sphere-bundle projection would assign a unit vector in each tautological fibre and therefore be a nowhere-zero continuous section of that real rank-two bundle. T.4 would force its Euler class to vanish, contrary to \(-x\ne0\). Hence no section exists. □
## 5. Infinite projective spaces and pullback models for lines

Let \(\mathbb F^{(\mathbb N)}\) denote the vector space of sequences in \(\mathbb F\) with finite support, indexed by \(0,1,\ldots\). Define
\[
\mathbb F P^\infty=\bigcup_{n\geq0}\mathbb F P^n
\tag{I.1}
\]
using the coordinate inclusions of R.1. Give this set the **weak topology**: a subset \(A\) is closed exactly when \(A\cap\mathbb F P^n\) is closed in every finite stage. This is a topology, since finite unions and arbitrary intersections satisfy the same tests; equivalently, openness is tested on every stage. In particular a map out of this space is continuous if and only if all its finite-stage restrictions are continuous.

### The finite-stage compactness property

**Lemma I.1 (topology and compact containment).** The space \(\mathbb F P^\infty\) is Hausdorff. Each finite stage is closed, has its original topology as a subspace, and includes continuously. Every compact subset lies in some finite stage. Every singular simplex and every finite singular chain in the infinite space therefore lies in a finite stage, with its usual finite-stage topology.

**Proof.** For each pair of indices \(i,j\), define the scalar coordinate \(P_{ij}\) of a line by the projection matrix formula (R.2), extending all coordinates beyond a representing vector's finite support by zero. It is well defined because that formula is invariant under nonzero scalar multiplication. Its restriction to each finite stage is continuous, so \(P_{ij}\) is continuous by the definition of the weak topology.

Two distinct lines lie in a common finite stage and have distinct projection matrices there by R.1. Some coordinate function therefore separates them. Choose disjoint open neighbourhoods of its two different scalar values; their inverse images separate the two lines. This proves Hausdorffness.

The inclusion of a finite stage is continuous by the same topology definition. It is injective and has compact domain by R.1. The compact-to-Hausdorff argument of P.1 makes it a homeomorphism to its image. That image is closed because it is compact in a Hausdorff space. Alternatively it is the simultaneous zero locus of \(P_{jj}\) for \(j>n\): a represented line has no nonzero coordinates beyond \(n\) exactly under these conditions.

Suppose a compact set \(C\) were contained in no finite stage. Select \(z_1\in C\), and let \(m_1\) be its least stage index. Having chosen \(z_k\) with least stage index \(m_k\), choose \(z_{k+1}\in C\setminus\mathbb F P^{m_k}\), which is possible by the supposition, and let \(m_{k+1}\) be its least stage index. Then \(m_{k+1}>m_k\). Consequently
\[
A=\{z_1,z_2,\ldots\}
\tag{I.2}
\]
meets each fixed finite stage in a finite set. Every subset \(A'\subset A\) has the same property. Finite subsets of a Hausdorff space are closed: a singleton is closed by separation from each outside point, and finite unions preserve closedness. Thus \(A'\cap\mathbb F P^n\) is closed for every \(n\), and the weak topology says that every \(A'\) is closed in the infinite space.

In particular \(A\) is closed in \(C\), hence compact by P.1. Also every subset of \(A\) is closed and its complement in \(A\) is closed, so every subset is open in \(A\). Its infinitely many singleton subsets form an open cover with no finite subcover, contradicting compactness. This proves compact containment.

The standard simplex is closed and bounded in a Euclidean space, hence compact by opening lesson 0.1. Its continuous image is compact by P.1, so every singular simplex has image in a finite stage. Because that stage has its original subspace topology, corestricting the simplex to it is continuous: inverse images of its relatively open sets are inverse images of corresponding open sets in the infinite space. A chain has only finitely many simplex terms, so a single sufficiently large stage contains all of them. □

### A bundle defined by its actual coordinate charts

**Lemma I.2 (the infinite tautological line).** There is a continuous line bundle \(\gamma_{\mathbb F}^\infty\) on \(\mathbb F P^\infty\) whose fibre is the represented line in \(\mathbb F^{(\mathbb N)}\). Its restrictions to the finite stages are exactly the bundles in R.1. It has a continuous Euclidean or Hermitian metric, and in the complex case its underlying real rank-two bundle has the canonical orientation of R.2.

**Proof.** Put
\[
U_j=\{P:P_{jj}>0\}.
\tag{I.3}
\]
These opens cover the space, since a nonzero representing vector has a nonzero coordinate. On \(U_j\) the line has the unique representative \(w_j\) with coordinate \(j\) equal to one. Its scalar coordinate functions are \(P_{ij}/P_{jj}\). On \(U_j\cap U_k\) put
\[
c_{kj}(P)=\frac{P_{kj}}{P_{jj}}=\frac{v_k}{v_j}.
\tag{I.4}
\]
These functions are continuous and nonzero. Direct scalar multiplication gives
\(c_{jj}=1\), \(c_{jk}c_{kj}=1\), and
\(c_{\ell k}c_{kj}=c_{\ell j}\) on the appropriate overlaps.

Take the disjoint union of the spaces \(U_j\times\mathbb F\), and identify
\[
(P,t,j)\sim(P,c_{kj}(P)t,k).
\tag{I.5}
\]
The three identities just proved make this an equivalence relation. Give its quotient \(E\) the quotient topology. Its projection to the base is continuous, because it is the continuous projection on every disjoint piece. The image of \(U_j\times\mathbb F\) is the full inverse image of \(U_j\), and it is open: its inverse image in every piece is \((U_j\cap U_k)\times\mathbb F\).

The map \(U_j\times\mathbb F\to E\) is injective and continuous. Its inverse on this open image has, on piece \(k\), the formula
\[
(P,s,k)\longmapsto(P,c_{jk}(P)s).
\tag{I.6}
\]
These maps are continuous and agree on the identifications. The restriction of a quotient over an open target remains quotient by the direct criterion proved in P.1, so (I.6) descends continuously. Thus these are actual bundle charts. Addition and scalar multiplication are continuous in these charts and agree across their linear transitions. The total space is Hausdorff: different base points separate by projection, and different vectors over one point separate in one of the product charts. Under the set map sending \((P,t,j)\) to \(t w_j(P)\), its fibre is precisely the represented line. This description of the fibres does not presume a product topology on an infinite-dimensional ambient space.

On the \(j\)-th chart give that vector squared norm
\[
\|t w_j\|^2=\frac{|t|^2}{P_{jj}}.
\tag{I.7}
\]
Since \(P_{kk}=|c_{kj}|^2P_{jj}\), equations (I.5) and (I.7) agree on overlaps. They define a continuous positive definite fibre metric. In the complex case its Hermitian form is \(\overline t s/P_{jj}\), with the convention of Q.4. The complex scalar transitions preserve real orientation by R.2.

On a finite stage, these same transition functions and charts are those of (R.4). The identity on represented vectors is therefore a bundle isomorphism between the restriction and the finite tautological bundle, as both it and its inverse are the identity maps in the corresponding charts. □

### Singular groups and the rings in the infinite union

**Theorem I.3 (infinite projective groups and rings).** With the bundles of I.2, set
\[
a=e_2(\gamma_{\mathbb R}^\infty),\qquad
x=-e((\gamma_{\mathbb C}^\infty)_{\mathbb R}).
\tag{I.8}
\]
Then
\[
H^*(\mathbb R P^\infty;\mathbb F_2)=\mathbb F_2[a],
\quad |a|=1,\qquad
H^*(\mathbb C P^\infty;\mathbb Z)=\mathbb Z[x],
\quad |x|=2.
\tag{I.9}
\]
The real mod-two homology has one copy of \(\mathbb F_2\) in each nonnegative degree. The complex integral homology has one copy of \(\mathbb Z\) in each nonnegative even degree and zero in odd degrees. For any abelian group \(G\),
\[
H^{2i}(\mathbb C P^\infty;G)\cong G,\quad
g\longmapsto g\,x^i,\qquad
H^{2i+1}(\mathbb C P^\infty;G)=0.
\tag{I.10}
\]
Restriction to every finite stage sends the named Euler classes and their powers to the classes of R.3–R.4. In any fixed degree the restriction is an isomorphism once the stage dimension is sufficiently large.

**Proof.** First the singular homology of either infinite space is the directed limit of the singular homologies of its finite stages, for any coefficient group. Here is the complete element argument for this instance. A cycle is a finite chain, hence is a chain in some finite stage by I.1. Its boundary computed there is zero because the singular chain inclusion is injective: distinct maps to the stage remain distinct after inclusion, and the coefficient groups on those simplex generators are unchanged. Hence every infinite-space class comes from a finite-stage class. If a finite-stage cycle bounds in the infinite space, a finite bounding chain lies in a larger finite stage by I.1; the equality of its boundary with that cycle holds there as well. The same reasoning applied to a difference says that two finite-stage cycles represent the same infinite class exactly when they do so at some larger stage. These are exactly the defining identifications of the directed limit.

For complex projective space the integral finite-stage groups are given by R.4. Attaching the next cell of dimension \(2(n+1)\) preserves homology in degrees below \(2(n+1)-1\), by P.3. Thus in any fixed degree \(q\), once \(2n\geq q\), all subsequent inclusions induce isomorphisms in that degree. The directed limit is therefore \(\mathbb Z\) in nonnegative even degrees and zero in odd degrees.

For real projective space use \(\mathbb F_2\). In fixed degree \(q\), the groups in stages \(n\geq q\) have dimension one by R.3. The restriction on cohomology is an isomorphism since it sends \(a^q\) to \(a^q\). The field evaluation isomorphism following U.3 is natural, so this cohomology map is the full linear dual of the inclusion's map on homology. A map between one-dimensional vector spaces with nonzero dual is nonzero and therefore invertible: in chosen bases both are multiplication by the same nonzero scalar. Hence the homology maps are isomorphisms once \(n\geq q\). Their limit gives the asserted real homology. Negative degrees throughout are zero by the chain conventions.

The complex integral homology groups just computed are free. The Ext term in U.3 is therefore zero, and natural evaluation gives
\[
H^q(\mathbb C P^\infty;G)
 \cong \operatorname{Hom}_{\mathbb Z}
       (H_q(\mathbb C P^\infty;\mathbb Z),G).
\tag{I.11}
\]
Naturality identifies restriction to a sufficiently large stage with precomposition by its homology inclusion, which we just proved is an isomorphism. Thus restriction in that fixed degree is an isomorphism for all \(G\), without any assertion about inverse limits of cochains. In the real case the field evaluation theorem gives the same conclusion from the stabilized mod-two homology.

The base spaces are Hausdorff by I.1, and the complex line is oriented by I.2, so the Euler classes in (I.8) exist by T.3–T.4. I.2 identifies the restricted bundles, so T.4 gives the stated restrictions on Euler classes; cup naturality gives the restrictions on all powers. Choose a finite stage with dimension at least a given degree. The finite calculation and the restriction isomorphism show that \(a^q\) generates real degree \(q\), and \(x^i\) generates complex degree \(2i\). No positive power is zero, since its restriction to a sufficiently large finite stage is nonzero. Associativity of cup products K.5 now gives (I.9): polynomial multiplication has precisely these products, and the homomorphism is bijective separately in each degree. The graded rings here are direct sums of their homogeneous groups, so their elements have finitely many homogeneous components; no formal power series assertion is made.

Finally (I.11) and natural change of coefficients identify \(g\,x^i\) with the homomorphism sending a generator of the degree-\(2i\) homology to \(g\), just as in R.4. This proves (I.10). □

### Existence of classifying maps for line bundles

**Lemma I.4 (a line as a tautological pullback).** Let \(B\) be paracompact Hausdorff, and let \(L\to B\) be a real or complex line bundle. There is a continuous map
\[
f:B\longrightarrow\mathbb F P^\infty
\tag{I.12}
\]
and a bundle isomorphism \(L\cong f^*\gamma_{\mathbb F}^\infty\). The construction is locally contained in a finite projective stage. It requires no countability hypothesis on \(B\).

**Proof.** Apply Q.6 to a trivializing cover of \(L\). Obtain countably many trivializing opens \(V_k\), indexed by positive integers, and functions \(\mu_k\geq0\) with locally finite supports contained in \(V_k\), whose sum is one. Fix a bundle coordinate \(\phi_k:L|_{V_k}\to\mathbb F\), so \(v\mapsto(\pi(v),\phi_k(v))\) is a trivialization. Define
\[
F_k(v)=
\begin{cases}
\mu_k(\pi(v))\phi_k(v),&\pi(v)\in V_k,\\
0,&\pi(v)\notin V_k.
\end{cases}
\tag{I.13}
\]
It is continuous. On the inverse image of \(V_k\) this follows from the displayed product; at a base point outside \(V_k\), the complement of the closed support of \(\mu_k\) is a neighbourhood on which the extension vanishes. Each \(F_k\) is linear on fibres.

Near any base point only finitely many supports occur. Thus the sequence
\[
F(v)=(F_1(v),F_2(v),\ldots)
\tag{I.14}
\]
has finite support, and on a suitable base neighbourhood all of its values lie in one fixed \(\mathbb F^{N+1}\). For a nonzero \(v\in L_b\), some \(\mu_k(b)>0\); in that chart \(\phi_k(v)\ne0\), so \(F_k(v)\ne0\). Hence \(F\) is injective on every fibre. Define \(f(b)\) to be the line \(F(L_b)\), with component \(F_k\) assigned coordinate \(k-1\) of \(\mathbb F^{(\mathbb N)}\).

To check continuity of \(f\), shrink a neighbourhood of any point both to a trivializing open for \(L\) and to an open meeting only finitely many of the supports. The frame with local coordinate one is a continuous nonzero section \(s\) there. The coordinates \(F_k(s(b))\) form a continuous nonzero vector in a fixed finite-dimensional space. Its line varies continuously by R.1, and the inclusion of that finite stage into the weak union is continuous by I.1. Thus \(f\) is continuous on a neighbourhood of every point, and hence globally: inverse images of opens are unions of their open intersections with this neighbourhood cover.

The set map
\[
v\longmapsto(\pi(v),F(v))
\tag{I.15}
\]
is a fibrewise linear bijection to the pullback of the bundle defined in I.2. It is an actual bundle isomorphism. On the base open \(\{\mu_k>0\}\), the image line lies in the chart \(U_{k-1}\); the scalar coordinate of (I.15) in that universal chart is precisely \(F_k(v)=\mu_k\phi_k(v)\). Both this expression and its inverse \(\phi_k(v)=F_k(v)/\mu_k\) are continuous there. These opens cover \(B\), so the isomorphism and its inverse are continuous everywhere. When \(B\) is empty the unique map and empty bundle give the assertion directly. □
## 6. Line operations and the complex first class

### Actual bundles for the algebraic operations

**Lemma W.1 (tensor, dual and Hom charts for lines).** Real or complex line bundles on a Hausdorff base have continuous tensor, dual, conjugate (in the complex case) and Hom bundles, defined fibrewise by those algebraic operations. They commute with pullback. There are natural bundle isomorphisms
\[
L^*\otimes M\longrightarrow\operatorname{Hom}_{\mathbb F}(L,M),
\qquad
\lambda\otimes v\longmapsto(w\mapsto\lambda(w)v),
\tag{W.1}
\]
and
\[
L\otimes\underline{\mathbb F}\cong L,\qquad
L^*\otimes L\cong\underline{\mathbb F},
\tag{W.2}
\]
where the second is evaluation. The first isomorphism in (W.2) sends \(v\otimes t\) to \(tv\).

**Proof.** For one-dimensional vector spaces with nonzero vectors \(u,v\), every element of their algebraic tensor product is a scalar multiple of \(u\otimes v\), because
\[
(au)\otimes(bv)=ab(u\otimes v)
\]
and elementary tensors span by definition. The bilinear coordinate function \((au,bv)\mapsto ab\) descends to a linear functional on the tensor product: it respects exactly its defining bilinear relations. It sends \(u\otimes v\) to one, so that vector is nonzero and the tensor product has dimension one. Every linear functional on a line is determined by its value on a nonzero vector, and every linear map between two lines is determined by the image of such a vector. These observations also give the one-dimensional coordinates for dual and Hom spaces.

Choose simultaneous bundle trivializations for \(L,M\) by intersecting their trivializing opens. Suppose on an overlap their scalar coordinates change by \(t_\beta=g_{\beta\alpha}t_\alpha\) and \(s_\beta=h_{\beta\alpha}s_\alpha\), where \(g,h\) are continuous and nonzero. The tensor coordinate changes by \(g_{\beta\alpha}h_{\beta\alpha}\). The dual coordinate changes by \(g_{\beta\alpha}^{-1}\), since the scalar value of a functional on a vector is independent of chart. A Hom coordinate is the scalar \(r\) in the equation \(s=rt\); it changes by \(h_{\beta\alpha}g_{\beta\alpha}^{-1}\). In the complex conjugate line use the conjugates of the original vector coordinates; their transitions are \(\overline{g_{\beta\alpha}}\).

All these transition functions are continuous and nonzero and satisfy the cocycle identity, because the original ones do and the scalar factors commute. The chart-gluing proof of I.2 applies verbatim to these functions on this open cover: take the quotient of the disjoint products, note that each chart image is open, and construct its continuous inverse on every overlapping piece by the transition function. This gives continuous line bundles with the stated fibres and their fibrewise operations. The argument used no special property of the projective cover in I.2.

In these coordinates, (W.1) is the identity between the scalar tensor coordinate and the Hom coordinate, since \(w\mapsto\lambda(w)v\) has scalar coefficient equal to the product of the scalar coordinates of \(\lambda,v\). Its formula is independent of chart, so it and its inverse are continuous. Evaluation in (W.2) is likewise the product scalar coordinate with transition \(g^{-1}g=1\), hence defines the trivial line isomorphism. The other isomorphism has scalar coordinate unchanged, so is continuous with continuous inverse \(v\mapsto v\otimes1\).

A pullback has, on inverse images of the original opens, the same charts with transitions composed with the base map. Taking products, inverses or conjugates of scalar transitions commutes with that composition. Thus the fibrewise identifications of pullback with each named operation have identity coordinate maps in these charts and are bundle isomorphisms. This proves all the assertions. □

### The two degree-two test cycles

Let \(X=\mathbb C P^\infty\), let \(p=[1:0:\cdots]\), and include the standard \(\mathbb C P^1\) through its first two coordinates. Define
\[
j_1:\mathbb C P^1\longrightarrow X\times X,\quad z\longmapsto(z,p),
\qquad
j_2:\mathbb C P^1\longrightarrow X\times X,\quad z\longmapsto(p,z).
\tag{W.3}
\]

**Lemma W.2 (degree-two detection on the product).** The integral homology of \(X\times X\) satisfies \(H_1=0\) and \(H_2\cong\mathbb Z^2\). Its degree-two basis is
\[
(j_1)_*[\mathbb C P^1],\qquad (j_2)_*[\mathbb C P^1].
\tag{W.4}
\]
Consequently
\[
(j_1^*,j_2^*):H^2(X\times X;\mathbb Z)
 \longrightarrow H^2(\mathbb C P^1;\mathbb Z)^2
\tag{W.5}
\]
is an isomorphism.

**Proof.** The homology of the free singular chain complex \(C=C_*(X;\mathbb Z)\) is free, by I.3. U.2 therefore provides chain maps
\[
i:D\to C,\qquad \pi:C\to D,\qquad \pi i=1,\qquad
1-i\pi=\partial h+h\partial,
\tag{W.6}
\]
where \(D=\bigoplus_{k\geq0}\mathbb Z[2k]\) has zero differential. The notation \(\mathbb Z[2k]\) denotes one copy of \(\mathbb Z\) in degree \(2k\) and zero elsewhere. Choose the generator in degree zero to be the point cycle \(p\). Choose the degree-two generator to be an integral fundamental cycle of \(\mathbb C P^1\), included in \(X\). This is a generator by R.4's evaluation \(\langle x,[\mathbb C P^1]\rangle=1\) and I.3's homology stabilization. U.2 permits these prescribed representatives.

Put \(P=i\pi\). The maps \(i\otimes i\) and \(\pi\otimes\pi\) are inverse up to chain homotopy. To verify the nontrivial composition explicitly, for homogeneous \(c\in C_a\) and \(d\in C\) put
\[
K(c\otimes d)=h(c)\otimes d+(-1)^aP(c)\otimes h(d).
\tag{W.7}
\]
Using the tensor differential
\(\partial(c\otimes d)=\partial c\otimes d+(-1)^a c\otimes\partial d\),
the first term of \(\partial K+K\partial\) contributes
\((1-P)c\otimes d\): its two terms containing \(h(c)\otimes\partial d\) have opposite signs. The second term contributes \(P(c)\otimes(1-P)d\): the terms with \(P(\partial c)\otimes h(d)\) cancel because \(P\) is a chain map. Their sum is
\[
\partial K+K\partial=1-P\otimes P.
\tag{W.8}
\]
The other composition is the identity since \(\pi i=1\). All sums on an input chain are finite; in each total degree there are only finitely many nonnegative pairs of factor degrees. Thus this construction is valid without a finite-dimensionality assumption on \(X\).

X.3 gives the complete singular product chain equivalence between \(C_*(X\times X;\mathbb Z)\) and \(C\otimes C\). Combining it with (W.6)–(W.8) identifies the product homology with \(D\otimes D\), which has zero differential. Degree one is zero. Degree two has exactly the two summands of bidegrees \((2,0)\) and \((0,2)\), each \(\mathbb Z\).

To identify their cycles, use the shuffle map \(\mathcal S\) of X.2. For a chain tensored with a point, there is exactly one shuffle, of sign positive. Its map is that same simplex in one coordinate and the fixed point in the other. Thus the two selected degree-two generators map to exactly the cycles in (W.4), not merely some unspecified basis.

Finally U.3 gives natural evaluation
\[
H^2(X\times X;\mathbb Z)
 \cong\operatorname{Hom}(H_2(X\times X;\mathbb Z),\mathbb Z),
\]
because its adjacent Ext term is \(\operatorname{Ext}(H_1,\mathbb Z)=0\). On \(\mathbb C P^1\) evaluation is also an isomorphism by R.4. Under these identifications, (W.5) assigns the two values on the basis (W.4), hence is an isomorphism. □

### Complex line formulas with the Euler normalization

For a complex line on a Hausdorff space define its first class by
\[
c_1(L)=e(L_{\mathbb R})\in H^2(B;\mathbb Z),
\tag{W.9}
\]
using its complex orientation. Thus \(c_1(\gamma_{\mathbb C}^\infty)=-x\) for the generator normalized in R.4 and I.3.

**Theorem W.3 (dual, conjugate, tensor and Hom).** Complex lines \(L,M\) on a paracompact Hausdorff base satisfy
\[
\begin{aligned}
c_1(L^*)&=-c_1(L),&
c_1(\overline L)&=-c_1(L),\\
c_1(L\otimes M)&=c_1(L)+c_1(M),&
c_1(\operatorname{Hom}_{\mathbb C}(L,M))
 &=c_1(M)-c_1(L).
\end{aligned}
\tag{W.10}
\]
The class is natural under pullback and is zero for the trivial line.

**Proof.** Naturality follows from the Euler naturality in T.4 and the complex orientation rule R.2: a complex linear bundle isomorphism preserves that real orientation. The trivial line has the nowhere-zero section one, so its Euler class vanishes by T.4. Q.4 provides a Hermitian metric on \(L\), and R.2 proves the dual and conjugate equalities with exactly this Euler normalization.

It remains to prove the tensor formula. On \(X\times X\) let \(L_1,L_2\) be the pullbacks of the infinite tautological line under the two projections. The space is Hausdorff by I.1: two distinct pairs differ in a coordinate, and inverse images of disjoint opens in that coordinate separate them. These continuous complex lines and their tensor product exist by I.2 and W.1. Their oriented Euler classes therefore exist on this base by T.3–T.4, without a paracompactness claim about the product.

Restricted along \(j_1\), the first line is the tautological line on \(\mathbb C P^1\); the second is the fixed line over \(p\), and hence is a trivial bundle, explicitly trivialized by the vector \((1,0,\ldots)\) in that fixed fibre. By \(v\otimes t\mapsto tv\) in W.1, the restricted tensor product is the first line. Thus
\[
j_1^*c_1(L_1\otimes L_2)
 =j_1^*\bigl(c_1(L_1)+c_1(L_2)\bigr).
\]
The same argument along \(j_2\), interchanging the two factors and using the scalar multiplication identification, gives equality of the other restrictions. W.2 detects degree-two classes from these two restrictions, so
\[
c_1(L_1\otimes L_2)=c_1(L_1)+c_1(L_2)
\quad\hbox{on }X\times X.
\tag{W.11}
\]

For the given \(L,M\) on \(B\), I.4 supplies maps \(f,g:B\to X\) and pullback isomorphisms. The paired map \(F=(f,g)\) is continuous: inverse images of product-basic opens are intersections of the corresponding two open inverse images. Pull (W.11) back by \(F\). W.1 identifies \(F^*(L_1\otimes L_2)\) with \(L\otimes M\), and Euler naturality identifies the other two terms with \(c_1(L)\) and \(c_1(M)\). This proves tensor additivity. Finally the isomorphism (W.1), tensor additivity and the dual sign yield
\[
c_1(\operatorname{Hom}_{\mathbb C}(L,M))
=c_1(L^*\otimes M)=-c_1(L)+c_1(M).
\]
All statements on an empty base are equalities in zero groups. □
## 7. Projective bundles and splitting into lines

### Projective bundle charts and the fibre generators

**Lemma M.1 (projectivization and its tautological line).** Let \(V\to B\) be a real or complex vector bundle of constant positive rank \(r\) on a Hausdorff base. The space \(P(V)\) of one-dimensional subspaces in its fibres is a Hausdorff fibre bundle over \(B\), with fibre \(F=\mathbb F P^{r-1}\). Its topology agrees with the quotient of the nonzero vectors in \(V\) by multiplication by nonzero scalars. It carries the tautological line subbundle \(S\subset p^*V\), where \(p:P(V)\to B\). Set
\[
z=
\begin{cases}
e_2(S)\in H^1(P(V);\mathbb F_2),&\mathbb F=\mathbb R,\\
-e(S_{\mathbb R})\in H^2(P(V);\mathbb Z),&\mathbb F=\mathbb C,
\end{cases}
\qquad
d=
\begin{cases}1,&\mathbb F=\mathbb R,\\2,&\mathbb F=\mathbb C.\end{cases}
\tag{M.1}
\]
On a trivialization \(p^{-1}U\cong U\times F\), the line \(S\) is the pullback of the finite tautological line under the fibre projection. Thus \(z\) is the pullback of the class in R.3 or R.4. In particular its powers \(1,z,\ldots,z^{r-1}\) restrict to the specified cohomology basis on every fibre.

**Proof.** Choose local frames for \(V\). In a frame, a fibre line is a point of \(F\), so the proposed chart is \(U\times F\). A frame change with continuous invertible matrix \(A(b)\) changes its projection matrix by
\[
P\longmapsto
\frac{A(b)P A(b)^*}{\operatorname{tr}(A(b)P A(b)^*)}.
\tag{M.2}
\]
Indeed for \(P=vv^*/(v^*v)\) the right side is the projection onto the line of \(A(b)v\). Its denominator equals \(|A(b)v|^2/|v|^2>0\). Formula (M.2) is continuous in \(b,P\), and its inverse uses \(A(b)^{-1}\). Continuity of the inverse matrices follows from opening lesson 0.4, applied to real matrices or to the underlying real matrices in the complex case as in Q.4. The transitions satisfy the cocycle law since they send a line to its image under the product of the frame changes. Gluing these product charts by the open-chart quotient argument in I.2, now with fibre \(F\), gives a genuine locally trivial bundle.

The vector-to-line quotient \(q:\mathbb F^r\setminus0\to F\) is open. If \(O\) is open in its domain, the full inverse image of \(q(O)\) is \(\bigcup_{\lambda\ne0}\lambda O\), open since multiplication by a nonzero scalar is a homeomorphism. The quotient criterion of R.1 therefore makes \(q(O)\) open. The product map \(\operatorname{id}_U\times q\) is open: it sends every basic open rectangle to an open rectangle, and arbitrary opens are unions of such rectangles. It is also continuous and surjective, so it is quotient. The local vector-to-line maps consequently give a global continuous open surjection \(V\setminus0\to P(V)\). Its fibres are exactly the scalar orbits. This proves the stated quotient topology.

Different base points separate by projection to the Hausdorff base. Two different lines over the same point separate in a common product chart, since \(F\) is Hausdorff by R.1. Thus \(P(V)\) is Hausdorff. In the pullback vector bundle, the subset consisting of vectors in the represented line is, on this product chart, \(U\) times the tautological bundle of R.1. Its local line charts are exactly the products of those in (R.4) with \(U\). Frame transitions send those vectors linearly to the same intrinsic vectors of \(V\), so the line charts agree and make a line subbundle \(S\).

Its complex orientation is R.2's canonical one. T.3–T.4 therefore define the classes in (M.1) and identify their restriction to a product chart with the pullback of the corresponding finite Euler class. R.3–R.4 prove the asserted fibre bases. No metric on \(V\) has been used. □

### A chain map which realizes the proposed module map

Use coefficients \(\kappa=\mathbb F_2\) in the real case and \(\kappa=\mathbb Z\) in the complex case. Choose cocycles
\[
c_i\in C^{di}(P(V);\kappa),\qquad [c_i]=z^i,\quad 0\leq i<r,
\tag{M.3}
\]
taking \(c_0\) to be the constant degree-zero cochain one. For any open \(U\subset B\), put
\[
D_m(U)=\bigoplus_{i=0}^{r-1}C_{m-di}(U;\kappa),
\tag{M.4}
\]
with negative chain groups zero and the ordinary boundary on each summand. The finite direct sum has no additional shift sign. With the right-cap convention of X.6, define
\[
T_U:C_m(p^{-1}U;\kappa)\longrightarrow D_m(U),
\qquad
T_U(a)=\bigl(p_*R_{c_i|_{p^{-1}U}}a\bigr)_{i=0}^{r-1}.
\tag{M.5}
\]

**Lemma M.2 (the local chain comparison).** Each \(T_U\) is a chain map. These maps commute with inclusion of open subsets and preserve the corresponding small-chain subcomplexes. If \(V|_U\) is trivial, \(T_U\) induces an isomorphism on homology.

**Proof.** For a closed cochain, X.6 proves \(\partial R_{c_i}=R_{c_i}\partial\) with this right-cap convention, and \(p_*\) is a chain map. Thus every component of (M.5) commutes with the boundaries in (M.4). Its value on a simplex uses a face of that simplex followed by \(p\). If the original simplex lies over a smaller open set, that face and its projection lie there as well. This proves both compatibility with open inclusions and preservation of small-chain subcomplexes.

Suppose \(p^{-1}U=U\times F\) in a trivialization. Write \(z_F\) for the finite projective generator. Choose cocycles \(v_i\in C^{di}(F;\kappa)\) for \(z_F^i\), with \(v_0=1\). M.1 and cup naturality give
\[
[c_i|_{U\times F}]=[\operatorname{pr}_F^*v_i].
\tag{M.6}
\]
For \(i>0\) their difference is a coboundary, by the definition of equal cohomology classes. The cap coboundary homotopy in X.6 shows that replacing one representative by the other does not change the induced homology map in (M.5). For \(i=0\) both cochains are identically one, so no negative-degree primitive is needed.

For these fibre-pulled representatives the Alexander–Whitney formula X.1 gives the exact chain identity
\[
p_*R_{\operatorname{pr}_F^*v_i}
   =(1\otimes v_i)\mathcal A .
\tag{M.7}
\]
On an \(m\)-simplex \(\sigma=(\sigma_U,\sigma_F)\), both sides are
\(v_i(\sigma_F[m-di,\ldots,m])\,\sigma_U[0,\ldots,m-di]\), or zero if \(m<di\). On the right, \(v_i\) is zero on fibre degrees other than \(di\), so only this term of the Alexander–Whitney sum remains.

In the complex case, R.4 gives free integral fibre homology with a generator in each degree \(0,2,\ldots,2(r-1)\). Choose cycles \(\beta_i\) representing its generators so that \(v_i(\beta_i)=1\). Such a choice exists because \(z_F^i\) generates the full integral dual in that degree, as proved in R.4. In the real case, R.3 and the field evaluation theorem after U.3 give exactly the same choice over \(\mathbb F_2\), in degrees \(0,\ldots,r-1\). In either case choose \(\beta_0\) to be one point.

Let \(H\) be the graded free \(\kappa\)-module on these generators with zero differential. U.2 gives a chain equivalence \(H\rightleftarrows C_*(F;\kappa)\) with homotopy \(h\), prescribing the selected cycles. Over \(\mathbb F_2\) use the same boundary/cycle/complement decomposition with vector-space bases; its full field version is proved in DG-CHAR-07 D.1. Tensor with \(C_*(U;\kappa)\). The homotopy on a homogeneous tensor \(a\otimes b\), with \(a\) of degree \(s\), is
\[
a\otimes b\longmapsto(-1)^s a\otimes h(b).
\tag{M.8}
\]
The two terms involving \(\partial a\otimes h(b)\) cancel in \(\partial K+K\partial\); the remaining terms are \(a\otimes(\partial h+h\partial)b\). Thus it really is a tensor chain homotopy. It identifies the homology of the tensor product with that of \(C_*(U;\kappa)\otimes H\), namely
\[
\bigoplus_{i=0}^{r-1}H_{m-di}(U;\kappa)
\quad\hbox{in degree }m.
\tag{M.9}
\]
Here a representative for its \(i\)-th component is \(a\otimes\beta_i\), with \(a\) a cycle of degree \(m-di\). The differential on \(C_*(U)\otimes H\) is just \(\partial a\otimes\beta_i\), so this identification follows directly by taking cycles and boundaries in the finite direct sum.

Use the shuffle map \(\mathcal S\) to send these tensors to product chains. X.3 gives \(\mathcal A\mathcal S\) homotopic to the identity. Composing with the chain map \(1\otimes v_j\), whose target has the ordinary boundary of (M.4), shows that (M.7) sends the homology class of \(\mathcal S(a\otimes\beta_i)\) to \([a]\) in component \(j=i\), and to zero in other components. This is because \(\beta_i\) has degree \(di\), and \(v_i(\beta_i)=1\). X.3 and the tensor equivalence just proved show that these classes account for all product homology. Thus (M.5) is an isomorphism on homology over a trivializing open. □

### Globalization on an arbitrary Hausdorff base

**Theorem M.3 (projective-bundle module theorem).** For a rank-\(r>0\) real bundle on a Hausdorff base,
\[
\bigoplus_{i=0}^{r-1}H^{m-i}(B;\mathbb F_2)
 \longrightarrow H^m(P(V);\mathbb F_2),
\qquad
(b_i)\longmapsto\sum_i p^*b_i\smile z^i
\tag{M.10}
\]
is an isomorphism. For a complex bundle, every abelian group \(G\) has the corresponding isomorphism
\[
\bigoplus_{i=0}^{r-1}H^{m-2i}(B;G)
 \longrightarrow H^m(P(V);G),
\qquad
(b_i)\longmapsto\sum_i p^*b_i\smile z^i,
\tag{M.11}
\]
where the cup product uses the natural scalar pairing \(G\times\mathbb Z\to G\).
These maps respect the left action of the base cohomology ring. In particular \(1,z,\ldots,z^{r-1}\) is a free module basis over the base ring for real mod-two or complex integral cohomology, and \(p^*\) is injective with every stated coefficient group.

**Proof.** We first prove that \(T_B\) in (M.5) is a homology isomorphism. It is one on any trivializing open by M.2, and on any open subset of such an open by the same proof.

For two opens \(U,W\), the small-chain Mayer–Vietoris sequence is obtained from the short exact sequence
\[
0\longrightarrow C_*(p^{-1}(U\cap W))
 \longrightarrow C_*(p^{-1}U)\oplus C_*(p^{-1}W)
 \longrightarrow C_*^{\{p^{-1}U,p^{-1}W\}}(p^{-1}(U\cup W))
 \longrightarrow0,
\tag{M.12}
\]
where the first map is \((a,-a)\) and the second is addition. Its exactness and the equivalence of the small complex with the full complex are proved in K.3 and E.3. Use the indicated coefficient ring \(\kappa\). There is a second short exact sequence obtained by the finite direct sums and reindexings in (M.4), on the base opens. The maps \(T\) take (M.12) to that sequence because they are chain maps compatible with opens and small chains. Therefore their induced maps commute with the connecting homomorphisms: an element's lift and its boundary in the first sequence are sent to a lift and its boundary in the second, which is the construction of the connecting maps in E.1. The small-to-full inclusions on the base are also equivalences by K.3, summand by summand.

If \(T_U,T_W,T_{U\cap W}\) are homology isomorphisms, the two Mayer–Vietoris sequences and the five-position exact-sequence chase proved before T.2 make \(T_{U\cup W}\) an isomorphism in every degree. Induction now treats any finite union of trivializing opens. Explicitly, when adding the last open \(W\) to a union of \(k-1\) such opens, its intersection with that union is the union of at most \(k-1\) intersections with \(W\). Each intersection is an open subset of a trivializing open, so the induction hypothesis applies there as well. The empty union has zero complexes and starts the induction if needed.

For a general trivializing cover, a cycle in \(D_m(B)\) consists of finitely many finite chains, one in each of the \(r\) summands. The union of all their simplex images is compact: each is a continuous image of a compact simplex, and a finite union of compact sets is compact by the open-cover definition. Finitely many trivializing opens cover that union. Write \(U\) for their union. The same chains are cycles in \(D_m(U)\), because chain inclusions are injective. The finite-union isomorphism gives a cycle in \(C_m(p^{-1}U)\) whose image is homologous to the given target cycle there. Its inclusion gives the required preimage in the global homology. This proves surjectivity.

For injectivity, let a cycle \(a\) in \(C_m(P(V))\) have \(T_B(a)=\partial b\) in \(D_m(B)\). The finitely many projected images of the simplices in \(a\), together with all images of the finitely many simplices in \(b\), form a compact subset of \(B\). Cover it by finitely many trivializing opens and let \(U\) be their union. Then \(a\) is a cycle in \(p^{-1}U\), and its \(T_U\) image is the boundary of the same \(b\) in \(D(U)\). The finite-union injectivity makes \(a\) a boundary in \(p^{-1}U\), hence also in \(P(V)\). Thus \(T_B\) is a homology isomorphism. This argument uses neither a partition of unity nor a locally finite cover of \(B\).

In the complex case both chain complexes are free abelian. The cohomological coefficient comparison U.4 therefore says that precomposition with \(T_B\) gives an isomorphism on cohomology with every abelian group \(G\). In the real case natural evaluation after U.3 identifies cohomology over \(\mathbb F_2\) with the full dual of homology, so it gives the same conclusion for that field.

The cochain complex dual to \(D(B)\), with coefficients \(G\), is the finite direct sum of \(C^{m-di}(B;G)\) in degree \(m\). Its differential is the usual cochain differential in each component, by the ordinary boundary convention in (M.4). Hence its cohomology is the direct sum on the left of (M.10) or (M.11). On representative cochains \(b_i\), precomposition with (M.5) has value
\[
\sum_i b_i(p_*R_{c_i}a)
 =\sum_i (p^*b_i\smile c_i)(a).
\tag{M.13}
\]
This is the exact cap/cup evaluation identity X.6; it uses only multiplication of an element of \(G\) by an integer, or multiplication in \(\mathbb F_2\). Thus the isomorphism just proved is precisely the one stated.

Finally, for a base ring class \(\alpha\), cup associativity K.5 and pullback naturality give
\[
p^*\alpha\smile(p^*b_i\smile z^i)
 =p^*(\alpha\smile b_i)\smile z^i.
\]
This proves compatibility with the left module action, including the integer action on the cohomology with coefficients \(G\). The \(i=0\) summand of either isomorphism is exactly \(p^*\), so a class killed by \(p^*\) has a tuple with zero image and must itself be zero. This proves injectivity.

For \(r=1\) the fibre is a point and the formulas have only that \(i=0\) summand; the same proof applies. A rank-zero vector bundle has empty projectivization and no asserted injective pullback. It is excluded from this theorem and handled separately in the flag construction below. □

### Full splitting after an injective pullback

**Theorem M.4 (flag splitting on a paracompact Hausdorff base).** Let \(V\to B\) be a finite-rank real or complex vector bundle of constant rank \(r\) on a paracompact Hausdorff space. There is a paracompact Hausdorff space \(\operatorname{Flag}(V)\), a continuous map \(f:\operatorname{Flag}(V)\to B\), and line bundles \(L_1,\ldots,L_r\) with
\[
f^*V\cong L_1\oplus\cdots\oplus L_r.
\tag{M.14}
\]
The map \(f^*\) on singular cohomology is injective with \(\mathbb F_2\) coefficients in the real case and with every abelian coefficient group in the complex case. The space can be constructed as a finite sequence of projectivizations, whose points choose an ordered orthogonal splitting of each fibre for a chosen metric.

**Proof.** If \(r=0\), take \(\operatorname{Flag}(V)=B\), \(f=\operatorname{id}\), and the empty direct sum. If \(r=1\), take the same base and map and let \(L_1=V\). These give the assertions immediately.

Suppose \(r\geq2\). Choose a continuous Euclidean or Hermitian metric on \(V\) by Q.4. Put \(B_1=P(V)\) with projection \(p_1\). It has compact Hausdorff fibre \(\mathbb F P^{r-1}\) by R.1 and M.1, so Q.5 makes \(B_1\) paracompact Hausdorff. On it, the tautological line \(S_1\) is a line subbundle of \(p_1^*V\). The pulled-back metric is continuous and positive in local coordinates. Q.4 gives an actual orthogonal complement subbundle \(Q_1\) of rank \(r-1\), and a continuous bundle isomorphism
\[
p_1^*V=S_1\oplus Q_1.
\tag{M.15}
\]

If \(Q_1\) has rank greater than one, put \(B_2=P(Q_1)\) with projection \(p_2:B_2\to B_1\). As before its fibre is compact Hausdorff, Q.5 makes its total space paracompact Hausdorff, and Q.4 splits \(p_2^*Q_1\) into its tautological line \(S_2\) and a rank-\((r-2)\) complement \(Q_2\). Pulling (M.15) back gives two line summands and this remaining complement. Pullback of a direct sum is the direct sum of pullbacks: on each common product chart this map and its inverse are the identity on the ordered vector coordinates, so it is a bundle isomorphism.

Continue for \(r-1\) projectivizations. At stage \(j\), \(Q_j\) has rank \(r-j\), and its induced metric is the restriction of the earlier positive metric. The same argument proves that each \(B_j\) is paracompact Hausdorff and that each displayed complement is a continuous subbundle. After the last stage, \(Q_{r-1}\) is itself a line. Define \(\operatorname{Flag}(V)=B_{r-1}\) and \(f=p_1\circ\cdots\circ p_{r-1}\), with composition understood from the last space to \(B\). Let \(L_j\) be the pullback of the line chosen at stage \(j\), and let \(L_r=Q_{r-1}\). The iterated bundle isomorphisms give (M.14). Fibrewise, each new line lies in the orthogonal complement of the preceding choices, so these choices are precisely ordered orthogonal line splittings. Their successive partial sums form full flags of subspaces.

By M.3, each \(p_j^*\) is injective for the stated coefficients, since every projectivized rank is positive. A composition of injective maps is injective: if the composite kills a class, injectivity of the last applied map removes it, and repeating removes all factors. Since cohomological pullback reverses the order of composition, this applies to \(f^*=p_{r-1}^*\cdots p_1^*\). Thus \(f^*\) has the required injectivity. □
## 8. Real line classes and orientation transport

Throughout, coefficients for the line class are \(\mathbb F_2\). An orientation of a real line is one of its two positive rays: two nonzero vectors represent the same orientation when their ratio is positive.

### Transport and its singular cocycle

**Lemma Z.1 (orientation transport and a degree-one class).** The orientations of the fibres of a real line bundle \(L\to B\) form a two-sheeted covering \(O(L)\to B\). Every path transports an initial orientation to a unique final orientation; transport composes under concatenation, reverses under path reversal, and is unchanged under homotopies fixing endpoints. Choosing an orientation \(o_b\) at each point defines a singular cocycle
\[
a_L(\sigma)=
\begin{cases}
0,&\text{transport along }\sigma\text{ takes }o_{\sigma(0)}
       \text{ to }o_{\sigma(1)},\\
1,&\text{it takes }o_{\sigma(0)}\text{ to the opposite orientation},
\end{cases}
\tag{Z.1}
\]
for singular one-simplices \(\sigma\). Its class
\[
w_1(L)=[a_L]\in H^1(B;\mathbb F_2)
\tag{Z.2}
\]
is independent of those pointwise choices and natural under pullback.

**Proof.** In a real line chart, an orientation is the sign of the nonzero scalar coordinate. On an overlap with transition \(g(b)\ne0\), its sign changes by \(\operatorname{sgn}g(b)\). That function is continuous with values in the discrete two-point set, since its positive and negative inverse images are open. These transitions glue the products \(U\times\{+,-\}\) into a covering. Each product has two disjoint open sheets projecting homeomorphically to \(U\), and the open-chart quotient argument of I.2 proves that these are the actual local charts. This also agrees with the quotient of \(L\setminus0\) by positive scalar multiplication: in a line chart the sign quotient is continuous and open, since saturating an open set by positive scalars is open, exactly as in M.1.

For a path \(\alpha:[0,1]\to B\), pull a covering-trivializing open cover back to the interval. The compact metric cover bound proved at the start of K.3 gives a partition
\(0=t_0<\cdots<t_N=1\) such that each closed subinterval maps into one such open. Starting with the chosen sheet over \(\alpha(0)\), lift the first subinterval by the inverse of its sheet chart. At an endpoint choose the sheet containing that endpoint lift, and repeat. This gives a continuous lift on the whole interval. For completeness, the finite closed-piece pasting used here follows from the closed-set criterion for continuity: the inverse image of a closed target set is closed on each of the finitely many closed subintervals, hence is a finite union of sets closed in the full interval.

Uniqueness holds on each subinterval. In a sheet chart, the sign of a lift is a continuous map from a connected interval to a discrete two-point set and is therefore constant. Connectedness of intervals follows from the intermediate-value result in opening lesson 0.0. The starting value fixes that constant. Induction over the subintervals proves uniqueness globally. Concatenating two lifts and reversing a lift consequently give transport under concatenation and reversal. In particular a constant path has constant lift.

Here is the required endpoint homotopy assertion with no general lifting theorem assumed. Let \(H:[0,1]^2\to B\) be a homotopy of two paths with their endpoints fixed. The inverse-image covering cover of the compact square has the same compact metric cover bound K.3. Subdivide into a finite square grid whose closed cells have diameter smaller than that bound. Every cell maps into one covering chart. Fix orientations at its finitely many image vertices, taking the same chosen orientation whenever image points coincide. Assign to each oriented grid edge the bit recording whether transport takes the chosen orientation at its start to that at its end. Reversing an edge has the same bit over \(\mathbb F_2\), because the inverse of either sign is itself.

Within a single cell, use its covering chart's constant positive sheet as a local reference. An edge bit is the sum of the two endpoint bits relative to that reference. The sum around its four sides is therefore zero. Sum over all cells. Every interior edge occurs twice and cancels in \(\mathbb F_2\); the four outer boundary transports remain. The two vertical sides map to constant paths and contribute zero. Therefore the transports along the two horizontal paths agree. This proves invariance under a homotopy fixing endpoints.

Now choose \(o_b\) for all \(b\), and extend (Z.1) linearly to singular one-chains. For a singular two-simplex \(\tau\), the path through its edges \(01\) and \(12\) is homotopic, fixing endpoints, to the edge \(02\): inside the convex standard triangle take the straight-line interpolation of those two parametrized paths, and compose it with \(\tau\). Concatenation and the homotopy assertion give
\[
a_L(\tau[01])+a_L(\tau[12])=a_L(\tau[02]).
\tag{Z.3}
\]
Thus \(\delta a_L=0\), since the alternating boundary sign is the same as addition over \(\mathbb F_2\).

If different pointwise orientations are chosen, write \(o'_b=(-1)^{u(b)}o_b\) for the resulting degree-zero cochain \(u\). The new transport bit is
\[
a'_L(\sigma)=a_L(\sigma)+u(\sigma(0))+u(\sigma(1))
           =a_L(\sigma)+(\delta u)(\sigma).
\tag{Z.4}
\]
This proves independence of the cohomology class. Under a pullback, the orientation charts and their path transports are pulled back as well. Choose at a point of the new base the chosen orientation at its image; (Z.1) then gives the pulled-back cocycle exactly. This proves naturality. Bundle isomorphisms likewise identify the charts and transports, so the class depends only on the bundle. □

### Why loops detect every degree-one class

Use the interval circle
\[
C=[0,1]/(0\sim1),\qquad q:[0,1]\to C,\qquad *=q(0)=q(1).
\tag{Z.5}
\]
It is the attachment of one one-cell to one point. By P.1 it is compact Hausdorff. It is homeomorphic to the usual unit circle: on successive quarter intervals interpolate linearly between \(e_1,e_2,-e_1,-e_2,e_1\), and normalize the nonzero resulting vector. The map is continuous with equal endpoint values. In each open quadrant, a ray meets the corresponding line segment once, since the sum of the absolute coordinates on that segment is one. Thus the induced map from \(C\) to the unit circle is bijective. Compactness and Hausdorffness make it a homeomorphism by P.1.

**Lemma Z.2 (loop generation and the circle generator).** The homology \(H_1(X;\mathbb F_2)\) of any space is generated by the singular cycles that are paths with equal endpoints. The single singular one-simplex \(q\) in (Z.5) is a generator of \(H_1(C;\mathbb F_2)\cong\mathbb F_2\). Consequently every degree-one cohomology class with \(\mathbb F_2\) coefficients is determined by its evaluations on maps \(C\to X\).

**Proof.** We first give the chain relations needed for generation. If paths \(\alpha,\beta\) have matching endpoints, write \(\gamma=\alpha*\beta\) for the concatenation that runs each path in half the unit interval. On the standard triangle with barycentric coordinates \((t_0,t_1,t_2)\), the map
\[
(t_0,t_1,t_2)\longmapsto\gamma(t_1/2+t_2)
\tag{Z.6}
\]
is a singular two-simplex. Its edges \(01,12,02\) are respectively \(\alpha,\beta,\gamma\). Therefore
\[
\alpha+\beta-\gamma\in\operatorname{im}\partial_2.
\tag{Z.7}
\]
These are integral chain identities as well. If \(\overline\alpha(s)=\alpha(1-s)\), the two-simplex
\((t_0,t_1,t_2)\mapsto\alpha(t_1)\) has edges \(\alpha,\overline\alpha\), and the constant path at \(\alpha(0)\). Its boundary is \(\alpha+\overline\alpha\) minus that constant path. A constant one-simplex itself is the boundary of the constant two-simplex, because its three alternating faces sum to one copy. Hence
\[
\overline\alpha\equiv-\alpha\pmod{\operatorname{im}\partial_2}.
\tag{Z.8}
\]

Let \(c\) be a mod-two one-cycle, a finite sum of paths. There are finitely many endpoints. In each of their path components choose a point \(b\), and for each endpoint \(v\) choose a path \(\lambda_v\) from that point to \(v\). Such paths exist by the definition of a path component; transitivity follows by concatenation and symmetry by reversal. Replace each summand \(\sigma\), from \(s\) to \(t\), by the loop
\[
\ell_\sigma=(\lambda_s*\sigma)*\overline{\lambda_t}.
\tag{Z.9}
\]
Twice applying (Z.7) and once applying (Z.8) shows
\(\ell_\sigma\equiv\lambda_s+\sigma-\lambda_t\) modulo boundaries. On summing, the coefficient of every \(\lambda_v\) is zero because \(\partial c=0\) says that the total endpoint coefficient at \(v\) is zero. Thus \(c\) is homologous to the sum of these loops. Their endpoints agree, so each factors continuously through \(q\), by its quotient property.

We verify the normalization of \(q\), including that it is not a boundary. The pair \(([0,1],\{0,1\})\) has relative first homology \(\mathbb F_2\): the interval contracts, and its pair sequence E.1 identifies that group with the kernel of the summation map \(H_0(\{0,1\})\to H_0([0,1])\). The identity interval simplex has boundary \([1]-[0]\), which generates that kernel, so its relative class is a generator.

The map of pairs
\[
q:([0,1],\{0,1\})\longrightarrow(C,\{*\})
\tag{Z.10}
\]
induces an isomorphism in relative homology. To see this directly, replace the endpoint set in the interval by the open collars \([0,1/4)\cup(3/4,1]\), and replace \(\{*\}\) in \(C\) by their image. Each collar neighbourhood deformation retracts onto the indicated subspace, with the two interval collars contracting to their respective endpoints and their quotient image contracting to \(*\). Continuity of the descended latter homotopy is the quotient-times-interval argument in P.1–P.2. Exact triples E.1 therefore make these replacements isomorphisms. Excision E.2 next removes \(\{0,1\}\) and \(\{*\}\). The remaining pairs are identified by the restriction of \(q\), namely the identity identification of
\[
((0,1),(0,1/4)\cup(3/4,1)).
\]
All comparison maps commute with \(q\), so (Z.10) is an isomorphism on relative homology.

The space \(C\) is path connected, since it is the continuous image of the path-connected interval. Thus \(H_0(\{*\})\to H_0(C)\) is an isomorphism, and \(H_1(\{*\})=0\), by E.1. The pair sequence now identifies \(H_1(C)\) with \(H_1(C,\{*\})\). The cycle \(q\) maps to the nonzero relative generator just proved. Hence it generates \(H_1(C)\cong\mathbb F_2\).

Finally the field evaluation theorem after U.3 gives
\(H^1(X;\mathbb F_2)\cong\operatorname{Hom}_{\mathbb F_2}(H_1(X;\mathbb F_2),\mathbb F_2)\).
Since the homology is generated by the cycles coming from \(q\) under maps \(C\to X\), their evaluations determine every degree-one class. □

### Agreement with the line Euler class

**Theorem Z.3 (the mod-two Euler class is orientation transport).** For a real line on a Hausdorff base,
\[
e_2(L)=w_1(L)\in H^1(B;\mathbb F_2).
\tag{Z.11}
\]
Equivalently, its evaluation on any loop is zero if that loop preserves orientation and one if it reverses orientation. For a two-sheeted cover, the Euler class of its sign line in S.4 therefore measures its sheet interchange.

**Proof.** By Z.2 it suffices to check evaluations on maps \(\ell:C\to B\). Euler naturality T.4 and Z.1's naturality reduce this to the pulled-back line on \(C\), tested on the generator \(q\). The compact Hausdorff circle is paracompact by Q.3, so Q.4 gives that line a continuous metric. Its unit sphere bundle is a two-sheeted cover canonically isomorphic to its orientation cover: in a line coordinate with metric coefficient \(a(b)>0\), the two orientations correspond to the two vectors \(\pm1/\sqrt{a(b)}\). These maps and their inverses are continuous in the cover charts.

Lift \(q\) to this unit cover starting at one unit vector over \(*\), using Z.1's path-lifting proof. Let \(\epsilon\) be its orientation-transport bit. If \(\epsilon=0\), the endpoint vector is the starting vector. The lifted path descends to a continuous section over \(C\), because its two endpoints agree and \(q\) is quotient. It is a nowhere-zero section of the line, so T.4 gives \(e_2(L)=0\). Its value on \(q\) agrees with \(\epsilon\).

If \(\epsilon=1\), the lifted path connects the two distinct unit vectors over \(*\). The whole unit cover is then path connected. Indeed any point of \(C\) can be joined to \(*\) by the image of a subinterval of \(q\); lifting the reverse of that path from either of its unit vectors joins it to one of the vectors over \(*\). Those two vectors are already joined by the lift of \(q\). This proves the claimed path connectedness of the total space.

In this case the degree-zero pullback from \(C\) to the unit cover is an isomorphism \(\mathbb F_2\to\mathbb F_2\), since both are path connected and degree-zero cocycles are the constant functions, as proved in E.1. The rank-one mod-two Gysin sequence S.1 and S.3 contains
\[
H^0(C;\mathbb F_2)\longrightarrow H^0(S(L);\mathbb F_2)
 \longrightarrow H^0(C;\mathbb F_2)
 \xrightarrow{\ \smile e_2(L)\ }H^1(C;\mathbb F_2).
\tag{Z.12}
\]
Exactness and the first isomorphism make the second arrow zero and the last arrow injective. Consequently \(e_2(L)\ne0\). The field evaluation theorem and Z.2 make \(H^1(C;\mathbb F_2)\) one dimensional and identify its nonzero element with the functional taking value one on \(q\). Thus \(e_2(L)\) again evaluates to \(\epsilon\). This proves (Z.11).

For the last assertion, let \(E\to B\) be the two-sheeted cover and \(L=E\times_{\{\pm1\}}\mathbb R\) its sign line as in S.4. The map
\[
E\longrightarrow O(L),\qquad
u\longmapsto\text{the positive ray of }[u,1]
\tag{Z.13}
\]
is well defined on \(E\), is bijective on each fibre, and sends the other sheet to the opposite orientation because \([\tau u,1]=[u,-1]\). In a covering chart it and its inverse are the identity maps between the two labels, so it is an isomorphism of covers. Their path lifts and transport bits are therefore the same. The established equality gives the assertion. □

### Real tensor, dual and Hom identities

**Corollary Z.4 (real line formulas).** Real line bundles \(L,M\) on a Hausdorff base satisfy
\[
w_1(L\otimes M)=w_1(L)+w_1(M),\qquad
w_1(L^*)=w_1(L),\qquad
w_1(\operatorname{Hom}_{\mathbb R}(L,M))=w_1(L)+w_1(M).
\tag{Z.14}
\]
A trivial real line has zero first class. All these formulas also hold with \(w_1\) replaced by \(e_2\). In particular the generators \(a\) of R.3 and I.3 are the first orientation classes of their tautological lines.

**Proof.** At each base point choose orientations of \(L,M\), and orient their tensor line by \(u\otimes v\) for positive representatives. Changing either positive representative by a positive scalar leaves that orientation unchanged, so it is well defined. On overlaps, W.1 gives the product of the two scalar transition functions for the tensor bundle. Along a path, the transported sign is therefore the product of the two signs, and its bit is their sum. With the compatible pointwise choices, (Z.1) gives the cochain identity
\[
a_{L\otimes M}=a_L+a_M.
\]
It descends to the first equality of (Z.14).

Orient the dual at a point by a functional taking a positive value on a positive representative of the original line. Its transition sign is the inverse of the original sign by W.1, and either sign is its own inverse. Thus its transport cocycle is the same and \(w_1(L^*)=w_1(L)\). W.1's isomorphism \(L^*\otimes M\cong\operatorname{Hom}_{\mathbb R}(L,M)\) and the tensor formula give the Hom equality. The constant positive section of a trivial line supplies orientations preserved along every path, so its cocycle is zero. Z.3 replaces each first class by the corresponding mod-two Euler class, and its application to the tautological lines gives the last statement. □
## Free construction sources

The following exact freely accessible author versions supplied the construction readings. The chapter proves the consumed results, including the prerequisites left external in those readings.

- Allen Hatcher, free author electronic [Chapter 0 of *Algebraic Topology*](https://pi.math.cornell.edu/~hatcher/AT/ATch0.pdf), printed pages 5–7: finite attachments and the real and complex projective characteristic maps.
- Hatcher, free author electronic [Chapter 1](https://pi.math.cornell.edu/~hatcher/AT/ATch1.pdf), printed pages 29–31 and 60–62: covering charts, path lifting and endpoint homotopies. Z supplies the complete orientation cocycle and singular loop-detection arguments.
- Hatcher, free author electronic [Chapter 2](https://pi.math.cornell.edu/~hatcher/AT/ATch2.pdf), Lemma 2.34 on printed pages 137–138 and projective calculations on page 144: finite relative-cell groups. P proves quotient, collar, excision and dimension assertions directly from singular chains.
- Hatcher, free author electronic [Chapter 3](https://pi.math.cornell.edu/~hatcher/AT/ATch3.pdf), printed pages 220–222: the real and complex projective rings. R and I prove the stated calculations using Gysin, finite-cell bounds and natural coefficient comparison.
- Hatcher, free author electronic [additional Chapter 4 topics](https://pi.math.cornell.edu/~hatcher/AT/ATch4.4.pdf) particularly Example 4D.5 and the pair/Thom diagram on page 444: the Gysin construction and projective calculations.
- Hatcher, free author [expanded Appendix to *Algebraic Topology*](https://pi.math.cornell.edu/~hatcher/AT/ATapp.pdf), its own printed pages 1–3, especially Proposition A.1: weak topology and compact containment. These page numbers refer to the expanded author file.
- Hatcher, free author [*Vector Bundles and K-Theory*, version 2.2](https://pi.math.cornell.edu/~hatcher/VBKT/VB.pdf) 29–31, 35–37, 78–81 and 86–87: metrics, scalar gluing, countable trivializations, existence of line pullback models, the projective/flag route and line-class identities. The local proofs include continuous separation and partitions, all bundle charts and inverses, the arbitrary Hausdorff-base module comparison, and the full Euler/transport normalization.

Original exposition: GPT-6 Astra (OpenAI), October 2026, CC0 1.0. Human construction sources are credited above. No source prose, diagrams or source PDFs are reproduced.
