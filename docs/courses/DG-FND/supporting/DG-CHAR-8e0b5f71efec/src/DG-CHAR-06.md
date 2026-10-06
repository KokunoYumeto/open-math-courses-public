# Integral Thom classes and Euler indices

DG-CHAR-06 · Differential geometry foundations

An orientation fixes a sign on each local homology group. We construct those signs from ordered cube chains, prove that they fit together on an oriented manifold, and use them to construct the integral Thom class of a vector bundle. The Thom isomorphism is proved over any Hausdorff base, with arbitrary abelian coefficient groups in the oriented case. Modulo two, no orientation is required. The final section evaluates Euler classes by local zeros and computes the tangent Euler class of a sphere.

The chapter includes the singular-chain, product and coefficient arguments needed for these constructions. Its algebra uses the integers, real numbers and the axiom of choice in the well-ordering form stated in Section 4. All chains are finite sums; cochains may assign values to every simplex. Manifolds are smooth, Hausdorff, second countable and without boundary.

The earlier programme prerequisite is [Local tools for bundles and transport](../../../src/local-tools-for-bundles-and-transport.md): Lemmas 0.0–0.4 for real estimates, compactness, finite bases, calculus and geometric decay; [Theorem 1.2 and Corollary 1.3](../../../src/local-tools-for-bundles-and-transport.md#1-contraction-and-local-inversion) for local inversion and level sets; and [Lemma 3.B](../../../src/local-tools-for-bundles-and-transport.md#3-smooth-weights-with-controlled-support) for coordinate balls with compact closures. Every other result used in the proofs is established in this chapter. Lettered statement and equation labels distinguish the algebraic and geometric constructions.

## 1. Determinants and coordinate signs

For a permutation \(\sigma\) of \(\{1,\ldots,n\}\), let \(N(\sigma)\) be the number of pairs \(i<j\) for which \(\sigma(i)>\sigma(j)\), and set \(\epsilon(\sigma)=(-1)^{N(\sigma)}\). The empty permutation has sign \(1\). For a real \(n\)-by-\(n\) matrix set
\[
\det A=\sum_{\sigma}\epsilon(\sigma)\prod_{j=1}^n a_{\sigma(j),j}.
\tag{L.1}
\]
The empty determinant is \(1\).

**Lemma L.1 (determinant identities).** The determinant is the unique alternating multilinear function of the columns with value \(1\) on the ordered standard basis. For square matrices,
\[
\det(AB)=\det A\,\det B,\qquad
\det(A^{\mathsf T})=\det A.
\tag{L.2}
\]
A matrix is invertible exactly when its determinant is nonzero. The determinant of a triangular matrix is the product of its diagonal entries. A permutation matrix has its permutation's sign, a real orthogonal matrix has determinant \(1\) or \(-1\), and the determinant is a continuous polynomial in the entries.

**Proof.** We first justify the sign rules. Swapping two adjacent positions in a list of distinct numbers changes its inversion count by an odd number: their mutual comparison changes by one, while for any other position the sum of its two comparisons with them is unchanged. If a list is not increasing, it has an adjacent decreasing pair. Swapping that pair decreases its inversion count by one. Repeating finitely many times sorts the list, showing that every permutation is a product of adjacent swaps and that the parity of any such product is its defined sign. Swapping positions \(i<j\) can be performed by \(2(j-i)-1\) adjacent swaps, so any transposition changes the sign. Composing with an adjacent swap therefore reverses sign, and decomposing a permutation into such swaps gives
\[
\epsilon(\sigma\tau)=\epsilon(\sigma)\epsilon(\tau).
\tag{L.3}
\]
In particular \(\epsilon(\sigma^{-1})=\epsilon(\sigma)\).

Every term of (L.1) contains one entry from each column, proving linearity in each column separately. Reordering columns reindexes the permutations in that sum and multiplies their signs by the column permutation's sign, by (L.3). Thus interchanging two columns negates the determinant. If two columns are equal, this interchange fixes the matrix and negates its determinant, so the determinant is zero over the real field. A zero column gives zero by multilinearity. Substituting the standard basis columns into (L.1) leaves only the identity permutation, with value \(1\).

Conversely, let \(D\) be any alternating multilinear function of \(n\) column vectors. Expand each column in the standard basis. Terms with repeated basis vectors vanish, since their value equals its negative after interchanging the two repeated entries. Every remaining term is a permutation of the standard basis; reordering it gives that permutation's sign times \(D(e_1,\ldots,e_n)\). Therefore
\[
D(v_1,\ldots,v_n)
=D(e_1,\ldots,e_n)\det[v_1\ \cdots\ v_n].
\tag{L.4}
\]
This proves the claimed uniqueness. Apply (L.4) to
\(D(v_1,\ldots,v_n)=\det[Av_1\ \cdots\ Av_n]\).
It is alternating multilinear, and its value on the standard basis is \(\det A\). Taking the \(v_j\)'s to be the columns of \(B\) proves the product identity in (L.2).

For the transpose, its determinant sum is
\(\sum_\sigma\epsilon(\sigma)\prod_j a_{j,\sigma(j)}\).
Reindex the product by \(i=\sigma(j)\) and the sum by \(\sigma^{-1}\). Using (L.3) gives exactly (L.1) for \(A\), proving the second identity.

If \(A\) is invertible, its product with its inverse has determinant \(1\), so \(\det A\ne0\). If its columns are dependent, one column is a linear combination of the others; multilinearity and repeated-column vanishing give \(\det A=0\). Thus nonzero determinant makes the columns independent. The finite-dimensional basis argument in opening-lesson Lemma 0.2 says that \(n\) independent vectors in \(\mathbb R^n\) form a basis; sending that basis back to the standard one gives the inverse map. This proves the converse.

For an upper triangular matrix, a nonzero term in (L.1) requires \(\sigma(j)\leq j\) for every \(j\). Since \(\sum_j\sigma(j)=\sum_jj\), all these inequalities must be equalities. Only the identity term remains, giving the diagonal product. Transposition proves the lower triangular case. The determinant of a permutation matrix follows directly by taking its columns to be the permuted standard basis. If \(Q^{\mathsf T}Q=I\), (L.2) gives \((\det Q)^2=1\), so \(\det Q=\pm1\). Finally (L.1) is a finite sum of products of entries and hence is a polynomial, continuous by the real sum and product rules proved in the opening lesson. All arguments also cover \(n=0\) with the empty conventions. □

## 2. Singular chains and cup products

### Chains and the prism identity

Put
\[
\Delta^n=\{(t_0,\ldots,t_n)\in\mathbb R^{n+1}:t_i\geq0,\ \sum_i t_i=1\}.
\]
Its ordered vertices are \(e_0,\ldots,e_n\). A continuous singular \(n\)-simplex in a space \(X\) is a continuous map \(\sigma:\Delta^n\to X\). Write \(C_n(X)\) for the free abelian group on these maps: elements are finite formal integer sums. Distinct parametrizations are distinct generators, including degenerate maps. In particular, permuting vertices is not an equality with a sign in this chain group.

For a manifold \(M\), a **smooth simplex** is a map extending smoothly to an open neighbourhood of \(\Delta^n\) in its affine span. The free subgroup on these maps is \(C_n^\infty(M)\). Affine face restrictions remain smooth: the inverse image of an extension domain under the affine face map is an open neighbourhood of the smaller simplex.

Let \(\varepsilon_i:\Delta^{n-1}\to\Delta^n\) be the affine inclusion whose ordered vertices omit \(e_i\). Define
\[
\partial\sigma=\sum_{i=0}^n(-1)^i\sigma\varepsilon_i\quad(n\geq1),
\qquad \partial:C_0(X)\to0.
\tag{K.1}
\]
These rules also define the boundary in the smooth subgroup.

**Lemma K.1 (boundary and homotopy).** The boundary squares to zero. Composition by a continuous map is a chain map; composition by a smooth map preserves the smooth chain subgroups. If \(F:X\times[0,1]\to Y\) is a homotopy from \(f_0\) to \(f_1\), there is an explicitly defined homomorphism \(P:C_n(X)\to C_{n+1}(Y)\) satisfying
\[
\partial P+P\partial=(f_1)_\#-(f_0)_\#.
\tag{K.2}
\]
For smooth manifolds and a smooth homotopy, it preserves smooth chains.

**Proof.** Each restriction omitting two distinct positions \(i<j\) occurs in \(\partial^2\sigma\) with coefficients \((-1)^{i+j-1}\) and \((-1)^{i+j}\); these cancel. In degrees one and zero the assertion follows from \(\partial C_0=0\). Composition commutes with each face restriction, so \(f_\#\partial=\partial f_\#\), and it preserves smooth extensions when \(f\) is smooth.

For the homotopy, put \(v_i=(e_i,0)\), \(w_i=(e_i,1)\) in \(\Delta^n\times[0,1]\). For each \(i\), let \(p_i:\Delta^{n+1}\to\Delta^n\times[0,1]\) be the affine map with ordered vertices
\[
[v_0,\ldots,v_i,w_i,\ldots,w_n].
\]
Every such affine image lies in the product, by convexity. Define
\[
P\sigma=\sum_{i=0}^n(-1)^i
F\circ(\sigma\times\operatorname{id})\circ p_i.
\tag{K.3}
\]
The formula alone suffices; no assertion about triangulating this product is needed.

We verify every boundary term. In \(\partial P\sigma\), deleting a bottom vertex \(v_j\), \(j\leq i\), has coefficient \((-1)^{i+j}\). Deleting a top vertex \(w_j\), \(j\geq i\), has coefficient \((-1)^{i+j+1}\), because it occupies position \(j+1\). For \(i>0\), the face deleting \(v_i\) from the \(i\)-th term has the same vertex list as the face deleting \(w_{i-1}\) from the \((i-1)\)-st term; their coefficients are \(1\) and \(-1\). All these joining faces cancel. The two unpaired faces are the all-top simplex from \(i=0\), with coefficient \(1\), and the all-bottom simplex from \(i=n\), with coefficient \(-1\).

The remaining terms are the side faces. If \(j<i\), deleting \(v_j\) is the prism term of index \(i-1\) for the face of \(\sigma\) omitting \(e_j\). Its coefficient in \(P\partial\sigma\) is \((-1)^{j+i-1}\), the opposite of its boundary coefficient. If \(j>i\), deleting \(w_j\) is the prism term of index \(i\) for that same face; its coefficient in \(P\partial\sigma\) is \((-1)^{j+i}\), again the opposite. This accounts for all terms and proves (K.2). For \(n=0\), (K.3) is the path \(t\mapsto F(\sigma(e_0),t)\), whose boundary is its endpoint difference, so the formula also holds there.

A smooth homotopy means a map extending smoothly to an open neighbourhood of \(M\times[0,1]\) in \(M\times\mathbb R\). This permits a neighbourhood whose width depends on the point of \(M\). If \(\sigma\) has a smooth extension, composition with each \(p_i\) and that homotopy extension is defined on an open neighbourhood of \(\Delta^{n+1}\): the preimage of the extension domain is open and contains this compact simplex. Thus every summand in (K.3) is smooth. □

### Subdivision with support control

An affine simplex in a convex subset \(Y\) of Euclidean space is denoted \([y_0,\ldots,y_n]\); repetitions are allowed. Its image is the convex hull of its vertices. Let \(L_n(Y)\) be the free group on such affine maps. For this paragraph only, augment the complex by \(L_{-1}(Y)=\mathbb Z[\varnothing]\), with \(\partial[y]=[\varnothing]\) and \(\partial[\varnothing]=0\). For \(b\in Y\), define the cone
\[
c_b[y_0,\ldots,y_n]=[b,y_0,\ldots,y_n],
\qquad c_b[\varnothing]=[b].
\]
Deleting the first vertex and then all the other vertices gives the identity
\[
\partial c_b+c_b\partial=\operatorname{id}
\tag{K.4}
\]
on the augmented complex. In degree \(-1\), it says \(\partial[b]=[\varnothing]\).

**Lemma K.2 (subdivision and its chain homotopy).** There are operators \(S:C_n(X)\to C_n(X)\) and \(T:C_n(X)\to C_{n+1}(X)\) with
\[
\partial S=S\partial,\qquad
\partial T+T\partial=\operatorname{id}-S.
\tag{K.5}
\]
Each simplex occurring in \(S\sigma\) or \(T\sigma\) has image contained in \(\sigma(\Delta^n)\). These operators preserve smooth chains. Each affine simplex occurring in \(S^m\operatorname{id}_{\Delta^n}\), with \(n\geq1\), has diameter at most
\[
\left(\frac n{n+1}\right)^m\operatorname{diam}(\Delta^n).
\tag{K.6}
\]

**Proof.** First work with affine maps \(\lambda=[y_0,\ldots,y_n]\) in a convex set. Write \(b_\lambda=(y_0+\cdots+y_n)/(n+1)\). Set \(S[\varnothing]=[\varnothing]\) and define recursively
\[
S\lambda=c_{b_\lambda}S\partial\lambda.
\tag{K.7}
\]
In degree zero this is \(S[y]=[y]\). Suppose \(\partial S=S\partial\) in lower degrees. Applying (K.4) gives
\[
\partial S\lambda
=S\partial\lambda-c_{b_\lambda}\partial S\partial\lambda
=S\partial\lambda-c_{b_\lambda}S\partial^2\lambda
=S\partial\lambda.
\]
This proves the chain-map identity by induction, including the augmentation.

Set \(T[\varnothing]=0\). In nonnegative degrees define
\[
T\lambda
=c_{b_\lambda}\bigl(\lambda-S\lambda-T\partial\lambda\bigr).
\tag{K.8}
\]
The expression in parentheses is a cycle: its boundary is
\[
\partial\lambda-S\partial\lambda-\partial T\partial\lambda=0
\]
by the lower-degree identity \(\partial T+T\partial=\operatorname{id}-S\). Thus (K.4) proves
\[
\partial T\lambda=\lambda-S\lambda-T\partial\lambda.
\]
The induction starts in degree \(-1\), where both sides of the homotopy identity vanish; (K.8) gives \(T[y]=0\) in degree zero. We may now discard the augmentation, since \(T\) was zero there.

Every vertex appearing in (K.7) or (K.8) lies in the convex hull of the original vertices, by induction. The constructions commute with affine maps, since such maps preserve vertex averages, face lists and cones. Therefore, for a general singular simplex, define
\[
S\sigma=\sigma_\#(S\operatorname{id}_{\Delta^n}),\qquad
T\sigma=\sigma_\#(T\operatorname{id}_{\Delta^n}).
\tag{K.9}
\]
The identities on the model simplex transfer to these formulas. For example, affine naturality on each face makes
\[
\sigma_\#S\partial\operatorname{id}_{\Delta^n}=S\partial\sigma,
\qquad
\sigma_\#T\partial\operatorname{id}_{\Delta^n}=T\partial\sigma,
\]
so (K.5) follows. All model affine maps have image in \(\Delta^n\), giving the claimed support control. Composing the smooth extension of \(\sigma\) with an affine map extends each resulting simplex smoothly to an open neighbourhood, proving smoothness.

To check diameter, the vertices of each summand generated by (K.7) are averages of nested nonempty subsets of the original vertex list. For subsets \(A\subset B\) of sizes \(a<b\), their averages satisfy
\[
b_B=\frac ab b_A+\frac{b-a}{b}b_{B\setminus A}.
\]
Consequently
\[
|b_B-b_A|\leq\frac{b-a}{b}\operatorname{diam}(\lambda(\Delta^n))
\leq\frac n{n+1}\operatorname{diam}(\lambda(\Delta^n)).
\tag{K.10}
\]
The same holds with zero distance if \(A=B\). The diameter of a convex hull of finitely many points is the largest distance between its vertices: if \(x=\sum_i s_i y_i\), \(z=\sum_j t_jy_j\), then
\[
|x-z|=\left|\sum_{i,j}s_it_j(y_i-y_j)\right|
\leq\sum_{i,j}s_it_j\max_{k,l}|y_k-y_l|
=\max_{k,l}|y_k-y_l|.
\]
Thus (K.10) bounds the diameter of each subdivided simplex, even for degenerate affine maps. Iterate it to obtain (K.6). The finite lists of signed summands produced by the recursion may be retained before combining identical generators; the bound holds for every entry of these lists. □

### A chain retraction onto small simplices

For an open cover \(\mathcal U\) of \(X\), a simplex is **\(\mathcal U\)-small** if its image is contained in one cover member. The subgroup \(C_n^{\mathcal U}(X)\) generated by these simplices is a subcomplex, since their faces are small. For a manifold, use \(C_n^{\infty,\mathcal U}(M)\) for its smooth version.

**Theorem K.3 (small-chain equivalence).** The inclusion \(i:C_*^{\mathcal U}(X)\to C_*(X)\) has a chain-map retraction \(\rho\) and a degree-one homomorphism \(D\) such that
\[
\rho i=\operatorname{id},\qquad
\operatorname{id}-i\rho=\partial D+D\partial.
\tag{K.11}
\]
Both constructions restrict to smooth chains. They preserve chains lying in any fixed subset of \(X\).

**Proof.** First, every open cover of a compact metric space \(K\) has a number \(\eta>0\) such that each nonempty subset of diameter less than \(\eta\) lies in one cover member. For each \(x\in K\), choose \(r_x>0\) with the relative ball \(B_K(x,2r_x)\) in some cover member. Finitely many balls \(B_K(x,r_x)\) cover \(K\). Let \(\eta\) be the minimum of their radii. A set of diameter less than \(\eta\) that meets one of these balls is contained in its doubled ball, by the triangle inequality. This proves the assertion.

Apply it to the inverse-image cover of the compact simplex \(\Delta^n\) under \(\sigma\). By (K.6) and geometric decay, sufficiently many subdivisions make the image of every generated affine summand lie in a cover member after composition with \(\sigma\). For \(n=0\), it is already a point in a cover member. Let \(\ell(\sigma)\) be the least number of subdivisions with this property, tested on the full generated list before cancellations. Once the property holds it holds at every larger depth, since subdivision stays inside each simplex image.

Choose depths recursively by dimension:
\[
m(\sigma)=
\begin{cases}
0,& n=0,\\
\max\bigl(\ell(\sigma),\,m(\sigma\varepsilon_0),\ldots,
m(\sigma\varepsilon_n)\bigr),& n>0.
\end{cases}
\tag{K.12}
\]
They are finite. Every face has depth at most that of its parent, \(S^{m(\sigma)}\sigma\) is small, and a small simplex has depth zero by induction on its faces. This definition supplies the face inequality explicitly, without assuming that cancellation in a chain detects geometric smallness.

For a fixed integer \(m\geq0\), put
\[
D_m=\sum_{k=0}^{m-1}TS^k,\qquad D_0=0.
\]
Using (K.5), the sum telescopes:
\[
\partial D_m+D_m\partial
=\sum_{k=0}^{m-1}(\operatorname{id}-S)S^k
=\operatorname{id}-S^m.
\tag{K.13}
\]
On each generator define \(D\sigma=D_{m(\sigma)}\sigma\), and extend linearly. Define, initially as a map into all chains,
\[
i\rho=\operatorname{id}-\partial D-D\partial.
\tag{K.14}
\]
This expression commutes with \(\partial\), since applying \(\partial\) on either side gives \(\partial-\partial D\partial\). Its image is small. Indeed, writing \(\tau_j=\sigma\varepsilon_j\), equations (K.13)–(K.14) give
\[
i\rho(\sigma)=S^{m(\sigma)}\sigma+
\sum_j(-1)^j
\bigl(D_{m(\sigma)}-D_{m(\tau_j)}\bigr)\tau_j.
\tag{K.15}
\]
Every term in the difference is \(TS^k\tau_j\) with \(k\geq m(\tau_j)\), since \(m(\tau_j)\leq m(\sigma)\). The chain \(S^k\tau_j\) is small, and \(T\) preserves smallness by its support property. Thus every term on the right is small. In degree zero the formula simply says \(\rho\sigma=\sigma\).

Equation (K.14) therefore defines a chain map \(\rho\) with the desired codomain. On a small simplex and every one of its faces, \(m=0\), so \(D=0\) and \(\rho\) is the identity. This proves (K.11). Every constituent \(S,T,\partial\) is supported in the original simplex image and preserves smoothness; the same is true of \(D,\rho\). The values of \(m\) depend only on the given map and its faces, so the construction on all continuous simplices restricts to exactly this construction on smooth simplices. □

### Cochains, local contraction and cup products

For an abelian group \(G\), define
\[
C^q(X;G)=\operatorname{Hom}_{\mathbb Z}(C_q(X),G),
\qquad (d_su)(c)=u(\partial c).
\tag{K.16}
\]
Thus a cochain is any assignment of values to simplices; continuity of the assignment is not required. Since \(\partial^2=0\), \(d_s^2=0\). The analogous definitions on smooth or small chains will use superscripts \(\infty\) or \(\mathcal U\), respectively. Their cohomology is denoted by the corresponding \(H^q\).

**Lemma K.4 (cochain homotopies and local cohomology).** Chain-homotopic maps induce equal maps on these cohomology groups. Restriction to small chains is a cohomology isomorphism, for every \(G\). On a nonempty open set smoothly diffeomorphic to a convex open set, both ordinary and smooth singular cohomology are \(G\) in degree zero, represented by constant cochains, and zero in positive degrees.

**Proof.** If chain maps \(a,b\) satisfy \(a-b=\partial P+P\partial\), precomposition by \(P\) defines a cochain homotopy \(K\) of degree \(-1\). Evaluating on a chain gives
\[
a^*-b^*=d_sK+Kd_s.
\tag{K.17}
\]
For a closed cochain \(u\), the difference is \(d_sKu\), so the cohomology maps agree. Applying this to (K.11), the restriction \(i^*\) and precomposition \(\rho^*\) induce inverse maps. Indeed, \(i^*\rho^*=(\rho i)^*=\operatorname{id}\), while
\[
\operatorname{id}-\rho^*i^*=d_sD^*+D^*d_s,
\qquad D^*u=uD.
\]
This holds for every abelian coefficient group, with no exactness assertion about a general dualization functor.

For a single-point space, there is one simplex \(z_n\) in each degree, and
\[
\partial z_n=
\begin{cases}
0,&n\text{ odd},\\
z_{n-1},&n>0\text{ even}.
\end{cases}
\]
The cochain complex is consequently \(G\xrightarrow{0}G\xrightarrow{\operatorname{id}}G\xrightarrow{0}G\xrightarrow{\operatorname{id}}\cdots\), starting in degree zero. Its cohomology has the asserted values.

For a convex open set \(V\), choose \(a\in V\), let \(j:\{a\}\to V\) be inclusion and \(p:V\to\{a\}\) the constant map. Then \(pj=\operatorname{id}\), while \(jp\) is homotopic to the identity by \(H(x,t)=a+t(x-a)\). This homotopy is smooth on the open set of pairs \((x,t)\) whose image lies in \(V\); that set contains \(V\times[0,1]\). Lemma K.1 and (K.17) show that \(p^*,j^*\) are inverse isomorphisms for both ordinary and smooth cohomology. In degree zero, \(p^*\) gives exactly the constant cochains. Coordinate diffeomorphisms preserve both constructions and transfer the result to the original open set. □

For products take \(G=R\), where \(R\) is any commutative unital ring. For a simplex \(\sigma\), let \(\sigma[a_0,\ldots,a_k]\) mean its composition with the affine map whose vertices are \(e_{a_0},\ldots,e_{a_k}\).

**Lemma K.5 (singular cup product).** The formula
\[
(u\smile v)(\sigma)
=u(\sigma[0,\ldots,q])\,v(\sigma[q,\ldots,q+s]),
\qquad u\in C^q,\quad v\in C^s,
\tag{K.18}
\]
defines an associative unital product on cochains with
\[
d_s(u\smile v)=d_su\smile v+(-1)^q u\smile d_sv.
\tag{K.19}
\]
It induces a product on cohomology. Pullbacks, restriction to smooth chains and restriction to small chains preserve it. The latter restriction is a ring isomorphism on cohomology.

**Proof.** On a simplex of dimension \(q+s+t\), either bracketing of a triple product evaluates the three factors on \([0,\ldots,q]\), \([q,\ldots,q+s]\) and \([q+s,\ldots,q+s+t]\), in that order. Associativity in \(R\) proves associativity. The degree-zero cochain with value \(1\) at every vertex is the unit.

To prove (K.19), evaluate on a \((q+s+1)\)-simplex. The first term on its right is the alternating sum over deletions from positions \(0,\ldots,q+1\) in the first factor, whose second factor begins at position \(q+1\). The second term is the alternating sum over deletions from positions \(q,\ldots,q+s+1\) in the second factor, whose first factor ends at position \(q\); its total deletion sign at position \(j\) is \((-1)^j\). The deletion \(q+1\) in the first sum and the deletion \(q\) in the second give the same product with opposite signs. All remaining terms are precisely the evaluations of \(u\smile v\) on the alternating faces of \(\sigma\). This proves the formula also when \(q=0\) or \(s=0\).

Products of cocycles are closed by (K.19). Replacing a cocycle by itself plus an exact cochain changes the product by an exact cochain, using (K.19) with the other factor closed. Thus the product is well defined in cohomology. Every stated pullback or restriction commutes with the face maps used in (K.18). Faces of a small simplex are small, so the formula also defines the small-cochain product. Lemma K.4 makes its restriction isomorphism bijective, hence a ring isomorphism. No multiplicativity of the chain retraction \(\rho\) is needed. □

## 3. Relative groups, excision and compact supports

Use the chain groups and boundary of K.1. For an abelian group \(G\), \(C_q(X;G)\) means finite formal sums of singular \(q\)-simplices with coefficients in \(G\). It is the direct sum of copies of \(G\) indexed by those simplices. The relative group \(C_q(X,A;G)\) is its quotient by the simplices whose images lie in \(A\); it is the direct sum indexed by the remaining simplices. Integral relative cochains with values in \(G\) mean
\[
C^q(X,A;G)=\operatorname{Hom}_{\mathbb Z}(C_q(X,A;\mathbb Z),G),
\qquad d_s u=u\partial.
\tag{E.1}
\]
These cochains identify with the absolute cochains that vanish on chains in \(A\): a homomorphism on the quotient composes with the quotient map to such a cochain, and every such cochain factors uniquely through the quotient. The factorization commutes with differential because the boundary preserves chains in \(A\). All sums of chains are finite; cochains can be arbitrary assignments on the simplex basis.

The statements below also apply to smooth chains in a smooth manifold. For a subset \(A\) of that manifold, a smooth chain in \(A\) means an ambient smooth chain whose simplex images lie in \(A\). In every homotopy assertion the maps and homotopies are smooth in the extension sense of K.1. This convention does not require an arbitrary subset to be a manifold.

The prism identity of K.1 descends to relative chains for a homotopy of pairs, since every prism on a simplex in the subspace remains in the target subspace. Its integral-coefficient identity also holds with coefficients in \(G\), by the same finite integer sums. It gives homotopy invariance of both relative homology and relative cohomology, the latter by precomposition as in K.4.

### The algebra underlying exact sequences

**Lemma E.1 (exact sequence of complexes).** A degreewise exact sequence of chain complexes
\[
0\longrightarrow A_*\xrightarrow{i}B_*\xrightarrow{p}C_*\longrightarrow0
\tag{E.2}
\]
gives a natural long exact sequence
\[
\cdots\longrightarrow H_q(A)\xrightarrow{i_*}H_q(B)
\xrightarrow{p_*}H_q(C)\xrightarrow{\delta}H_{q-1}(A)
\longrightarrow\cdots.
\tag{E.3}
\]
The cochain version gives a natural long exact sequence with the degree raised by its connecting map.

**Proof.** If \(c\in C_q\) is a cycle, choose \(b\in B_q\) with \(pb=c\). Then \(p\partial b=\partial c=0\), so there is a unique \(a\in A_{q-1}\) with \(ia=\partial b\). Moreover \(i\partial a=\partial^2b=0\), so \(\partial a=0\). Define \(\delta[c]=[a]\).

Changing \(b\) to another lift replaces it by \(b+ia'\), and replaces \(a\) by \(a+\partial a'\). Changing \(c\) by \(\partial c'\), and lifting \(c'\) to \(b'\), permits changing \(b\) to \(b+\partial b'\), which leaves \(\partial b\) unchanged. Thus \(\delta\) is well defined. Lifts of sums can be chosen as sums of lifts, so it is a homomorphism.

The three consecutive composites are zero: \(pi=0\); a cycle \(b\) has \(\partial b=0\), so \(\delta p_*[b]=0\); and \(ia=\partial b\) is a boundary, so \(i_*\delta[c]=0\).

For the reverse inclusions, first suppose \(b\) is a cycle and \(pb=\partial c'\). Lift \(c'\) to \(b'\). Then \(b-\partial b'\) belongs to \(\ker p\), so equals \(ia\), and injectivity of \(i\) makes \(a\) a cycle. Hence \([b]\) is in the image of \(i_*\). Next suppose \(\delta[c]=0\). In the defining lifts, \(a=\partial a'\) for some \(a'\). The lift \(b-ia'\) is then a cycle projecting to \(c\), so \([c]\) is in the image of \(p_*\). Finally, if \(a\) is a cycle with \(ia=\partial b\), then \(pb\) is a cycle and the connecting construction sends \([pb]\) to \([a]\). This proves exactness at all repeating positions.

A commuting map between two sequences (E.2) takes the chosen lifts and their boundaries to valid lifts and boundaries in the target sequence. Thus the connecting maps, as well as the other maps, commute with it. This proves naturality. For cochain complexes, replace the chain group in degree \(q\) by the cochain group in degree \(-q\) and apply the same proof; the resulting connecting map raises cochain degree by one. The proof works for integer-graded complexes, so this reindexing imposes no boundedness condition. □

In particular,
\[
0\to C_*(A;G)\to C_*(X;G)\to C_*(X,A;G)\to0
\tag{E.4}
\]
is exact on the simplex bases and yields the pair sequence. With integral chains it splits as a sequence of abelian groups in each degree by separating the two sets of basis simplices. Applying \(\operatorname{Hom}(-,G)\) is therefore exact here: a homomorphism on the subspace basis extends by zero, and the other kernel and image identities follow from factorization through the quotient. This gives the cohomological pair sequence. The same argument applied to
\[
0\to C_*(A,B;G)\to C_*(X,B;G)\to C_*(X,A;G)\to0
\tag{E.5}
\]
for \(B\subset A\subset X\) gives the homology and cohomology triple sequences.

For reduced homology add the augmentation \(C_0(X;G)\to G\), which sums coefficients, in degree \(-1\). For a nonempty space \(X\), it is onto. The boundary of a path is its terminal point minus its initial point. These relations identify any two points in the same path component, while the homomorphism summing coefficients separately on each path component annihilates every path boundary. Choosing one point in each component proves that these are exactly the relations. Thus ordinary \(H_0(X;G)\) is one copy of \(G\) for each path component, with finite support, and reduced \(H_0\) is the kernel of its sum map. For smooth chains the identical statement uses the equivalence relation generated by smooth paths; a finite concatenation can be represented by a sum of its smooth path simplices, so the concatenation itself need not be smooth. The point complex has one simplex in every degree and differential the identity in positive even degrees and zero in odd degrees; its reduced complex is acyclic. Homotopy invariance therefore makes a contractible nonempty space reduced-acyclic, using a smooth contraction in the smooth version.

Reduced cochains add \(G\) in degree \(-1\), mapping \(g\) to the constant zero-cochain of value \(g\). Their degree-zero cohomology consists of functions constant on the corresponding path classes modulo globally constant functions; no continuity condition on cochains is imposed. Their other nonnegative cohomology groups agree with unreduced cohomology. For nonempty \(A\), augment (E.4) in degree \(-1\) by \(0\to G\xrightarrow{1}G\to0\to0\). This gives the reduced pair sequences in both theories, with the ordinary relative groups.

### Excision from the proved small-chain homotopy

**Theorem E.2 (excision).** Suppose \(Z\subset A\subset X\) and \(\overline Z\subset\operatorname{int}_X A\). Inclusion
\[
(X\setminus Z,A\setminus Z)\longrightarrow(X,A)
\tag{E.6}
\]
induces homology and cohomology isomorphisms with every abelian coefficient group.

**Proof.** The two open sets
\[
U=\operatorname{int}_X A,\qquad V=X\setminus\overline Z
\]
cover \(X\). The small integral chain group is \(C_*(U)+C_*(V)\). Its intersection with \(C_*(A)\) is \(C_*(U)+C_*(A\cap V)\): this follows by inspecting each basis simplex. A basis simplex in the small group lies in \(U\) or \(V\); if it also lies in \(A\), the former type lies in \(U\subset A\), and the latter lies in \(A\cap V\). Hence the quotient of small chains by the small chains in \(A\) identifies, by the canonical inclusion of the \(V\) summand, with
\[
C_*(V)/C_*(A\cap V).
\tag{E.7}
\]

The chain retraction and homotopy of K.3 preserve every subspace: each summand in their values stays in the original simplex image. They therefore descend to a chain homotopy equivalence between (E.7) and \(C_*(X,A)\). Restrict the same cover to \(X\setminus Z\). Its members are \(U\setminus Z\) and \(V\), and the identical basis calculation gives precisely (E.7) again after quotienting by small chains in \(A\setminus Z\). The canonical maps from the common quotient to the two relative complexes commute with (E.6). Both are chain homotopy equivalences by K.3, so (E.6) induces an isomorphism in homology.

All these homotopies are finite integral sums on basis simplices, so the identities hold with coefficients in any \(G\). Precomposing integral cochains with them gives inverse cohomology maps and cochain homotopies, by the calculation in K.4. This proves the cohomology assertion without assuming that dualization preserves arbitrary exact sequences. The affine subdivision operations preserve smoothness by K.2–K.3, so the same proof applies to the smooth version. □

### Gluing over two open sets and over two closed supports

**Lemma E.3 (Mayer–Vietoris).** If \(X=U\cup V\) with \(U,V\) open, there is a natural exact sequence
\[
\cdots\to H_q(U\cap V;G)\to
H_q(U;G)\oplus H_q(V;G)\to H_q(X;G)
\to H_{q-1}(U\cap V;G)\to\cdots,
\tag{E.8}
\]
and the contravariant cohomology sequence. The same statements hold for pairs with any fixed subspace \(A\subset X\), using the intersections of \(A\) with the indicated opens. If \(U\cap V\ne\varnothing\), the absolute sequences also have reduced versions.

**Proof.** On integral chains use
\[
0\to C_*(U\cap V)\xrightarrow{c\mapsto(c,-c)}
C_*(U)\oplus C_*(V)\xrightarrow{(a,b)\mapsto a+b}
C_*^{\{U,V\}}(X)\to0.
\tag{E.9}
\]
The first map is injective, and the last is onto by the definition of small chains. If \(a+b=0\), equality in the free group on all simplices says \(a=-b\) is supported on the intersection of the two basis sets, namely the simplices in \(U\cap V\). This proves middle exactness. A splitting of the last map is obtained by assigning each small basis simplex to its \(U\) copy if it lies in \(U\), and otherwise to its \(V\) copy. It need not be a chain map.

Thus (E.9) stays exact with coefficients in \(G\) and after integral dualization to cochains with values in \(G\). Lemma E.1 and the equivalence K.3 give (E.8) and its cohomological version. The connecting map in homology takes a small cycle \(a+b\), with \(a\) in \(U\), \(b\) in \(V\), to \([\partial a]=[-\partial b]\) on the intersection; this follows directly from the lifting rule of E.1.

For the relative version, remove from every basis set the simplices in \(A\). The same three-way partition of the remaining small simplex basis proves the degreewise split exact sequence. The support-preserving homotopy K.3 descends to the quotient by \(A\), proving the claimed relative sequences. For the reduced version, extend (E.9) in degree \(-1\) by
\[
0\to G\xrightarrow{g\mapsto(g,-g)}G\oplus G
\xrightarrow{(g,h)\mapsto g+h}G\to0.
\]
It is split exact and commutes with augmentations. Dualizing the integral augmented sequence gives the reduced cochain version. Naturality follows from E.1 and the canonical inclusions; no choice of splitting enters the induced maps. □

For a closed subset \(K\) of a space \(M\), write
\[
H_q(M\mid K;G)=H_q(M,M\setminus K;G).
\tag{E.10}
\]
The vertical bar is notation for a relative group, not a new homology theory.

**Lemma E.4 (two supports).** For closed subsets \(K,L\subset M\), there is a natural long exact sequence
\[
\cdots\to H_q(M\mid K\cup L;G)
\xrightarrow{x\mapsto(x,x)}
H_q(M\mid K;G)\oplus H_q(M\mid L;G)
\xrightarrow{(x,y)\mapsto x-y}
H_q(M\mid K\cap L;G)\to\cdots.
\tag{E.11}
\]

**Proof.** Put \(A=M\setminus K\) and \(B=M\setminus L\). As subgroups of the same free simplex group \(C_q(M)\),
\[
C_q(A)\cap C_q(B)=C_q(A\cap B).
\]
There is a short exact sequence of complexes
\[
0\to \frac{C_*(M)}{C_*(A\cap B)}
\longrightarrow
\frac{C_*(M)}{C_*(A)}\oplus\frac{C_*(M)}{C_*(B)}
\longrightarrow
\frac{C_*(M)}{C_*(A)+C_*(B)}
\to0,
\tag{E.12}
\]
with diagonal and difference maps. Its exactness can be checked without a diagram lemma. An element maps to zero under the diagonal exactly when its representative belongs to both subgroups, proving injectivity. If \(x-y=a+b\) with \(a\in C_*(A)\), \(b\in C_*(B)\), the pair of quotient classes of \(x,y\) is the diagonal image of \(x-a=y+b\). Finally every class in the last quotient is the image of a pair \((x,0)\). The same checks on the simplex basis give a degreewise splitting and establish (E.12) with coefficients in any \(G\).

The last quotient is chain homotopy equivalent to \(C_*(M)/C_*(A\cup B)\). Here are the necessary chain maps, since merely replacing that denominator would not be a chain identity. Set
\[
F=C_*(M),\quad T=C_*(A\cup B),\quad S=C_*(A)+C_*(B).
\]
The opens \(A,B\) cover their union. K.3 gives a homotopy \(D_T:T_q\to T_{q+1}\) with \(1-\partial D_T-D_T\partial\) taking values in \(S\), and \(D_T=0\) on \(S\). Extend \(D_T\) to \(D:F_q\to F_{q+1}\) by making it zero on every basis simplex not contained in \(A\cup B\). Define \(P=1-\partial D-D\partial\). This is a chain map, maps \(T\) into \(S\), and equals the identity on \(S\). Thus it induces a map
\[
\overline P:F/T\longrightarrow F/S.
\]
Let \(q:F/S\to F/T\) be the quotient map. The identity \(1-P=\partial D+D\partial\), first modulo \(S\) and then modulo \(T\), proves that \(\overline Pq\) and \(q\overline P\) are chain homotopic to the respective identities. The homotopies are well defined because \(D(S)\subset S\) and \(D(T)\subset T\).

Applying E.1 to (E.12) and this equivalence yields (E.11), since \(A\cap B=M\setminus(K\cup L)\) and \(A\cup B=M\setminus(K\cap L)\). The first two maps are the canonical diagonal and difference restrictions. Naturality of the connecting map follows from the natural quotient map \(q\) and E.1; the auxiliary inverse \(\overline P\) is only used to prove that \(q\) is a homology isomorphism. All homotopies remain valid with coefficients in \(G\) and in the smooth-chain version. □

### The local groups of Euclidean space

**Lemma E.5 (sphere and punctured-space groups).** For \(m\geq0\), reduced homology and reduced cohomology of \(S^m\), with any abelian coefficients \(G\), equal \(G\) in degree \(m\) and zero in every other degree. For \(n\geq0\), both homology and cohomology of
\[
(\mathbb R^n,\mathbb R^n\setminus\{0\})
\tag{E.13}
\]
equal \(G\) in degree \(n\) and zero otherwise. These assertions also hold for smooth chains and cochains.

**Proof.** The sphere \(S^0\) has two points. A simplex has connected domain, so its image in this discrete two-point space is a single point: connectedness of the simplex follows from its straight-line paths, and a continuous image of a connected space is connected because inverse images of a separation would separate the domain. The chain complex is consequently the direct sum of two point complexes. Its reduced \(H_0\) is \(\{(g,-g):g\in G\}\), and its reduced \(H^0\) is \((G\oplus G)/\{(g,g):g\in G\}\), each isomorphic to \(G\); all other reduced groups vanish.

For \(m\geq1\), cover \(S^m\subset\mathbb R^m\times\mathbb R\) by the complements \(U,V\) of its north and south poles. Each is diffeomorphic to \(\mathbb R^m\). For example
\[
u\longmapsto
\left(\frac{2u}{1+|u|^2},\frac{|u|^2-1}{1+|u|^2}\right)
\tag{E.14}
\]
parametrizes the complement of the north pole, with inverse \((y,t)\mapsto y/(1-t)\); substitution verifies both inverse identities. Reflection in the last coordinate gives the other chart. Thus each open is smoothly contractible.

Their intersection is diffeomorphic to \(S^{m-1}\times(-1,1)\), by
\[
(v,t)\longmapsto(\sqrt{1-t^2}\,v,t).
\]
The inverse normalizes the first \(m\) coordinates and records the last coordinate. Both are smooth on their domains. Contracting the second factor to zero is a smooth deformation retraction to \(S^{m-1}\). The intersection is nonempty. The charts join every point in either open to a chosen intersection point by a smooth path. The sum of two such path simplices has as its boundary the difference of any two given endpoints. Thus reduced degree-zero homology, and reduced degree-zero cohomology, of the union vanish in both versions; no smoothing of a concatenated path is needed.

Reduced E.3 and the vanishing for the contractible opens therefore give, for \(j\geq1\),
\[
\widetilde H_j(S^m;G)\cong\widetilde H_{j-1}(S^{m-1};G),
\qquad
\widetilde H^j(S^m;G)\cong\widetilde H^{j-1}(S^{m-1};G).
\]
The reduced degree-zero groups of the union vanish; negative reduced groups vanish for any nonempty space since the augmentation is onto and the constant-cochain inclusion is injective. Induction from \(m=0\) proves the sphere assertion in every degree.

For \(n\geq1\), the complement of zero in \(\mathbb R^n\) smoothly deformation retracts to its unit sphere through
\[
H(x,t)=\left((1-t)+\frac{t}{|x|}\right)x.
\tag{E.15}
\]
The scalar stays positive for \(0\leq t\leq1\), and the formula extends smoothly to an open neighbourhood of this parameter domain. Its full domain with positive scalar is open, so a uniform extra interval in \(t\) is unnecessary. The reduced pair sequences of E.1, contractibility of \(\mathbb R^n\), and the sphere computation give (E.13). In degree zero the relative groups vanish because the nonempty punctured space maps onto \(H_0(\mathbb R^n;G)=G\) and constants restrict injectively. For \(n=0\), the pair is a point relative to the empty space and the point calculation gives the assertion. □

**Corollary E.6 (a compact convex support).** Let \(K\subset\mathbb R^n\) be nonempty, compact and convex, and let \(x\in K\). The natural map
\[
H_q(\mathbb R^n\mid K;G)\longrightarrow
H_q(\mathbb R^n\mid\{x\};G)
\tag{E.16}
\]
is an isomorphism. These groups vanish except in degree \(n\), where they are isomorphic to \(G\).

**Proof.** For \(n=0\), both pairs in (E.16) are the point relative to the empty set and the map is the identity. Suppose \(n>0\). Translate \(x\) to zero, and choose \(R>\sup_{a\in K}|a|\), which exists by compactness. The sphere of radius \(R\) lies in both complements. The formula
\[
H(v,t)=\left((1-t)+\frac{tR}{|v|}\right)v
\tag{E.17}
\]
deformation retracts each complement to that sphere. For \(\mathbb R^n\setminus\{0\}\) this follows as in E.5. For \(v\notin K\) with \(|v|\leq R\), its path travels outward along the ray through \(v\). It cannot enter \(K\): if \(\lambda v\in K\) for \(\lambda\geq1\), convexity and \(0\in K\) would put \(v=\lambda^{-1}(\lambda v)+(1-\lambda^{-1})0\) in \(K\), a contradiction. For \(|v|>R\), the path stays at norm at least \(R\), so also stays outside \(K\). The formula fixes the radius-\(R\) sphere.

Consequently the inclusion of the first complement into the second is a homotopy equivalence, with the common radial retraction as inverse through that sphere. The natural reduced pair sequences identify (E.16), for positive degree \(q\), with the induced map of reduced homology groups of the complements in degree \(q-1\); these are isomorphisms. The degree-zero groups are zero by the same argument as in E.5. Smoothness of (E.17) on the open complements proves the smooth version too. □

### Compact supports and coherent local classes

Let \(M\) be a Hausdorff, second-countable smooth \(n\)-manifold without boundary. Compact subsets are closed: for a point outside a compact set, separate it from each point of the compact set by disjoint open sets, take a finite subcover on the compact side, and intersect the finitely many neighbourhoods on the other side. Thus (E.10) applies to compact supports.

**Theorem E.7 (detection on compact supports).** For every compact \(K\subset M\),
\[
H_q(M\mid K;G)=0\quad(q>n),
\qquad
H_n(M\mid K;G)\longrightarrow
\prod_{x\in K}H_n(M\mid\{x\};G)
\ \text{is injective}.
\tag{E.18}
\]
The product map consists of the natural restrictions to individual points. Both statements hold for ordinary and smooth homology.

**Proof.** For an empty support all relative chain groups are zero. We first work in \(\mathbb R^n\).

For a nonempty compact convex support, both claims follow from E.6, using any one of its points for injectivity. They also hold for a finite union of compact convex sets. To prove this by induction on their number \(m\), separate the last set \(L\) from the preceding union \(K'\). The intersection \(K'\cap L\) is a union of at most \(m-1\) compact convex sets, so induction applies to it as well as to \(K'\) and \(L\). For \(q>n\), sequence (E.11) places \(H_q(\mathbb R^n\mid K'\cup L;G)\) between the zero groups \(H_{q+1}(\mathbb R^n\mid K'\cap L;G)\) and \(H_q(\mathbb R^n\mid K';G)\oplus H_q(\mathbb R^n\mid L;G)\). In degree \(n\) it makes the map to the two pieces injective. A class whose restrictions to every point vanish has zero restriction to each piece by induction, and hence is zero. This proves both assertions for finite unions.

Now take an arbitrary nonempty compact \(K\subset\mathbb R^n\). Represent a relative class by a finite chain \(z\) with \(\partial z\) supported in the complement of \(K\). Let \(C\) be the union of the images of the finitely many simplices occurring in \(\partial z\), so \(C\) is compact and disjoint from \(K\). If \(C\ne\varnothing\), its distance from \(K\) is positive: the continuous distance function on the compact product \(C\times K\) attains a minimum, and a zero minimum would give an intersection. If \(C=\varnothing\), no distance restriction is needed. Choose finitely many closed balls, each centred at a point of \(K\), whose interiors cover \(K\) and which all avoid \(C\). Their union \(N\) is compact and disjoint from \(C\). The same chain \(z\) defines a class over \(N\), mapping to the original class over \(K\).

If its degree is greater than \(n\), the finite-union case makes the class over \(N\) zero, proving the vanishing over \(K\). In degree \(n\), suppose the original class has zero restriction at every point of \(K\). For each chosen ball \(B\), restriction of the class over \(N\) to \(B\) has zero restriction at the centre of \(B\), which belongs to \(K\). By E.6 the restriction to \(B\) is zero. It follows that the class over \(N\) restricts to zero at every point of \(N\). The finite-union case makes that class zero, proving injectivity for \(K\). For \(n=0\), nonempty \(K\subset\mathbb R^0\) is a point and was already treated, so the ball and distance step is needed only for \(n>0\).

If a compact support \(K\subset M\) is contained in a single coordinate neighbourhood \(W\), excision identifies its relative groups first with those of \(W\) and then, through the coordinate chart, with the support groups in \(\mathbb R^n\). To check the first excision hypothesis, use \(Z=M\setminus W\) and \(A=M\setminus K\); \(Z\) is closed, is disjoint from \(K\), and is contained in the open set \(A\). In coordinates, the image of \(K\) is compact and lies in the open chart image, so the identical check permits extension from that image to all of \(\mathbb R^n\). These excision maps commute with restrictions to points. Thus the preceding result applies to every compact support contained in a chart.

Finally cover an arbitrary compact \(K\subset M\) by finitely many coordinate balls \(B_i\) with compact closures inside their coordinate neighbourhoods, as supplied by local-tools Lemma 3.B. Put \(K_i=K\cap\overline{B_i}\); these are compact, each lies in a chart, and their union is \(K\). Induct on the number of such compact pieces. At the last step, \((K_1\cup\cdots\cup K_{m-1})\cap K_m\) is a union of at most \(m-1\) compact pieces, each still contained in a chart. The exact-sequence argument used for finite convex unions therefore applies with the induction hypotheses just established. It proves (E.18) for all compact \(K\).

Every argument used finite chains, the exact sequence E.4, excision E.2 and the explicit smooth radial homotopy E.6. Those are valid in the smooth version too, so the proof applies there without invoking a triangulation or a smoothing theorem. □

The notation \(H_q(M\mid A;G)=H_q(M,M\setminus A;G)\) also makes sense for a subset \(A\) that is not closed, and will be used in the following definition only. A family
\[
\alpha_x\in H_n(M\mid\{x\};G)\qquad(x\in M)
\]
is **locally coherent** if each point has an open neighbourhood \(U\) and a class \(a_U\in H_n(M\mid U;G)\) whose image at every \(y\in U\) is \(\alpha_y\). This is a condition on a family of relative classes; no covering-space theory is presumed.

**Theorem E.8 (gluing a coherent family).** For a locally coherent family \((\alpha_x)\) and a compact set \(K\subset M\), there is a unique
\[
\alpha_K\in H_n(M\mid K;G)
\quad\text{with restriction }\alpha_x\text{ for every }x\in K.
\tag{E.19}
\]
Consequently, when \(M\) is compact, a locally coherent choice of integral generators at its points gives a unique integral fundamental class, meaning an element of \(H_n(M;\mathbb Z)\) with those prescribed local generators. The result holds for ordinary and smooth homology with their respective coherence conditions.

**Proof.** Uniqueness is (E.18). By local coherence and the coordinate-ball construction, there is a finite cover of \(K\) by open coordinate balls \(B_i\) such that each compact closure \(\overline{B_i}\) lies in some coherence neighbourhood \(U_i\). Put \(K_i=K\cap\overline{B_i}\). Restriction of the given class \(a_{U_i}\) to \(K_i\) gives a class having the required point values there, since \(K_i\subset U_i\).

Suppose classes with the required point values have been constructed on \(A=K_1\cup\cdots\cup K_{i-1}\) and on \(B=K_i\). Their restrictions to \(A\cap B\) agree by the uniqueness assertion of E.7, because they have the same point values on that compact intersection. Their pair is therefore in the kernel of the difference map in (E.11). Exactness supplies a class on \(A\cup B\) restricting to the two given classes. Its point values are the prescribed values on the union. Induction constructs \(\alpha_K\). All supports in this induction are compact and hence closed, as required for E.4.

For \(K=M\), relative chains for \(M\mid M\) are the absolute chains, so (E.19) is precisely the asserted fundamental class. The proof uses no choice of sign beyond the locally coherent generators supplied in the hypothesis; compatibility of those signs with the differential-geometric orientation is a separate statement. □

## 4. Free complexes and arbitrary coefficients

We work over the integers. A free abelian group with basis \(S\) consists of finite integer linear combinations of elements of \(S\). We use the axiom of choice, in its well-ordering form. A chain complex may be indexed by all integers; its differential lowers degree by one and squares to zero.

### Freeness and splitting

**Lemma U.1 (subgroups and lifts).** Every subgroup of a free abelian group is free. A surjection of abelian groups onto a free abelian group admits a homomorphic section.

**Proof.** First, a nonzero subgroup of \(\mathbb Z\) has a least positive element \(d\). For any integer \(a\), the set of nonnegative integers \(a-qd\), with \(q\in\mathbb Z\), is nonempty: taking \(q=-(|a|+1)\) gives a positive value because \(d\geq1\). Choose its least element \(r\). If \(r\geq d\), then \(r-d\) is a smaller member, a contradiction. Thus \(a=qd+r\), with \(0\leq r<d\). When \(a\) lies in the subgroup, the remainder is still in it, so the minimality of \(d\) forces \(r=0\). Hence the subgroup is \(d\mathbb Z\). The zero subgroup is free on the empty basis.

Let \(J\subset F\), where the basis of \(F\) is well ordered as \((e_\alpha)_{\alpha<\kappa}\). Write \(F_\beta\) for the span of the basis elements with index less than \(\beta\), and \(J_\beta=J\cap F_\beta\). The coefficient of \(e_\beta\) maps \(J_{\beta+1}\) to a subgroup of \(\mathbb Z\), with kernel \(J_\beta\). If its image is nonzero, choose \(v_\beta\in J_{\beta+1}\) with coefficient equal to the least positive generator \(d_\beta\). Subtracting a multiple of \(v_\beta\) from any element of \(J_{\beta+1}\) removes that coefficient. Moreover no nonzero multiple of \(v_\beta\) lies in \(J_\beta\). Hence
\[
J_{\beta+1}=J_\beta\oplus\mathbb Z v_\beta
\]
in this case, and \(J_{\beta+1}=J_\beta\) in the zero-image case.

At a limit ordinal \(\lambda\), every element of \(F_\lambda\) has finite support, and that support is contained in some \(F_\beta\) with \(\beta<\lambda\). Therefore \(J_\lambda=\bigcup_{\beta<\lambda}J_\beta\). Transfinite induction now shows that the selected \(v_\beta\)'s form a basis at every stage: spanning and independence follow from the direct sum at a successor stage, and every finite relation or element occurs before a limit stage. Their union is a basis for \(J\).

Finally, if \(q:A\to F\) is onto and \(F\) is free, choose one preimage in \(A\) for each basis element of \(F\). Extending these choices by finite integer linear combinations gives a homomorphism \(s:F\to A\) with \(qs=1\). □

**Lemma U.2 (a free homology model).** Let \(C_*\) be a complex of free abelian groups whose homology groups are free. There are chain maps
\[
i:H_*(C)\longrightarrow C_*,
\qquad
\pi:C_*\longrightarrow H_*(C),
\qquad \pi i=1,
\]
where the homology groups on the left and right have zero differential, and a homomorphism \(h:C_n\to C_{n+1}\) satisfying
\[
1-i\pi=\partial h+h\partial.
\tag{U.1}
\]
The cycle chosen to represent any specified basis element of homology can be prescribed in advance.

**Proof.** Put \(Z_n=\ker\partial_n\) and \(B_n=\operatorname{im}\partial_{n+1}\). Lemma U.1 makes both free. The surjection \(\partial_n:C_n\to B_{n-1}\) has a section, with image \(L_n\), and therefore
\[
C_n=Z_n\oplus L_n,\qquad
\partial_n:L_n\longrightarrow B_{n-1}\ \text{is an isomorphism}.
\]
Since \(H_n=Z_n/B_n\) is free, its quotient map also has a section \(i_n:H_n\to Z_n\). Such a section is obtained by choosing cycle representatives of a homology basis, so any specified representatives can be used. Thus
\[
C_n=B_n\oplus i_n(H_n)\oplus L_n.
\tag{U.2}
\]
Define \(\pi\) to be projection onto the middle summand followed by \(i_n^{-1}\), and define \(i\) by these sections. Both are chain maps and \(\pi i=1\).

Define \(h_n\) on the first summand \(B_n\) to be the inverse of \(\partial_{n+1}:L_{n+1}\to B_n\), and make it zero on the other two summands. On \(B_n\), \(\partial h=1\) and \(h\partial=0\). On \(L_n\), \(h\partial=1\) and \(\partial h=0\). Both operators vanish on \(i_n(H_n)\). This proves (U.1) on every summand. In particular, a free acyclic complex is contractible. □

### The coefficient obstruction and evaluation

For an abelian group \(H\), choose a free presentation
\[
0\longrightarrow J\xrightarrow{j}F\longrightarrow H\longrightarrow0.
\]
Such a presentation exists: take a free group on a generating set, or on the set of all elements of \(H\), and use its kernel; the kernel is free by U.1. Define
\[
\operatorname{Ext}(H,G)
=\operatorname{Hom}(J,G)\big/
\{\,\phi j:\phi\in\operatorname{Hom}(F,G)\,\}.
\tag{U.3}
\]
We next verify the independence and naturality needed to use this definition.

A homomorphism \(f:H\to H'\) lifts to a homomorphism \(\widetilde f:F\to F'\), by choosing a lift of the image of each basis element. Its restriction maps \(J\) into \(J'\). Precomposition with that restriction induces a map from the quotient defining \(\operatorname{Ext}(H',G)\) to the one defining \(\operatorname{Ext}(H,G)\): a map extending to \(F'\) pulls back to one extending to \(F\).

Two lifts of \(f\) differ by a homomorphism \(\ell:F\to J'\), because their images in \(H'\) are equal. For \(\psi:J'\to G\), the two restrictions differ after applying \(\psi\) by \((\psi\ell)|_J\), which extends to \(F\) and is zero in the quotient (U.3). Thus the induced map does not depend on the lift. Composing two lifts lifts the composite, so the induced maps compose contravariantly and the identity induces the identity. Apply this observation to the identity of \(H\) with two different free presentations: maps in the two directions give inverse canonical isomorphisms. This proves presentation independence. Postcomposition with a homomorphism \(G\to G'\) also respects the defining quotient and commutes with these maps. If \(H\) is free, the presentation with \(F=H\) and \(J=0\) shows that \(\operatorname{Ext}(H,G)=0\).

**Theorem U.3 (cohomology with arbitrary coefficients).** For a free abelian chain complex \(C_*\) and an abelian group \(G\), there is a natural short exact sequence
\[
0\longrightarrow\operatorname{Ext}(H_{n-1}(C),G)
\longrightarrow H^n(\operatorname{Hom}(C_*,G))
\xrightarrow{\mathrm{ev}}\operatorname{Hom}(H_n(C),G)
\longrightarrow0.
\tag{U.4}
\]
The evaluation map sends a cohomology class to its evaluation on cycle classes. The sequence splits as a sequence of groups; no natural choice of splitting is asserted.

**Proof.** A cocycle \(u:C_n\to G\) vanishes on \(B_n\), since \(u\partial_{n+1}=0\). It therefore induces a homomorphism on \(Z_n/B_n=H_n\). A coboundary \(v\partial_n\) vanishes on \(Z_n\), so this homomorphism depends only on the cohomology class. This defines \(\mathrm{ev}\).

By U.1, the surjection \(C_n\to B_{n-1}\) splits, so \(Z_n\) is a direct summand of \(C_n\). Choose a projection \(p_n:C_n\to Z_n\) that is the identity on \(Z_n\). For \(\lambda:H_n\to G\), composing \(p_n\), the quotient \(Z_n\to H_n\), and \(\lambda\) gives a cocycle whose evaluation is \(\lambda\). This construction is additive in \(\lambda\) once the projection is fixed. It proves surjectivity and a group splitting.

If a cocycle has zero evaluation, then it vanishes on all of \(Z_n\), and hence factors uniquely as \(u=v\partial_n\) for a homomorphism \(v:B_{n-1}\to G\). Two such maps \(v\) represent the same cohomology class precisely when their difference is the restriction of a homomorphism \(C_{n-1}\to G\). The images of restriction from \(C_{n-1}\) and from \(Z_{n-1}\) to \(B_{n-1}\) are equal: every map on \(Z_{n-1}\) extends to \(C_{n-1}\), since \(C_{n-1}\to B_{n-2}\) splits by U.1. Thus the kernel of evaluation is
\[
\operatorname{Hom}(B_{n-1},G)\big/
\operatorname{im}\big(\operatorname{Hom}(Z_{n-1},G)
\to\operatorname{Hom}(B_{n-1},G)\big).
\]
The free presentation \(0\to B_{n-1}\to Z_{n-1}\to H_{n-1}\to0\) identifies this quotient with (U.3), proving exactness.

For a chain map \(f:C\to C'\), restrictions of \(f\) map cycles to cycles and boundaries to boundaries, giving a map between those free presentations. Evaluation plainly commutes with these maps. On the kernel, a factorization \(u'=v'\partial'\) pulls back to \(u'f=(v'f|_B)\partial\). This is exactly the map on (U.3). The presentation-independence argument above therefore proves naturality of the entire sequence, without using the chosen projections. Postcomposition in \(G\) is equally compatible. □

In particular, if \(H_{n-1}(C)=0\), evaluation in (U.4) is an isomorphism. We also need the field version for vector spaces of arbitrary dimension. Basis extension follows from the same well-ordering axiom used above: start with an independent family \(S\) in a vector space \(V\), well order the vectors of \(V\), and at each successive stage adjoin the current vector exactly when it is outside the span of the vectors already selected together with \(S\). At a limit stage take the union. Independence persists, since each linear relation is finite and therefore occurs at a previous stage; adding a vector outside the preceding span cannot create a relation. Every vector belongs to the resulting span, since it was either adjoined at its stage or was already in that span. The resulting family is a basis containing \(S\). Starting with the empty family gives a basis for any subspace, and applying the same argument in the larger space extends it.

Over a field \(k\), evaluation is consequently an isomorphism in every degree for a complex of vector spaces: choose a basis of the boundary subspace, extend it to one of the cycle subspace, and then extend that to the chain space. A functional on homology extends to a cocycle by zero on the complementary basis. A cocycle vanishing on cycles factors through boundaries in the preceding degree, and that functional extends to the preceding chain space by basis extension, so it is a coboundary. These arguments apply equally to functionals with values in any \(k\)-vector space \(G\), since a choice of values on a basis extends uniquely by finite linear combinations. Evaluation commutes with chain maps and with maps of coefficient spaces by its defining formula. This proves the field assertion, including its naturality, directly.

**Corollary U.4 (dualizing a homology isomorphism).** A chain map between free abelian complexes that induces isomorphisms on homology induces isomorphisms on cohomology with every abelian coefficient group.

**Proof.** The natural sequences (U.4) form a commuting diagram. Their left and right vertical maps are isomorphisms: the left by presentation-independent functoriality of Ext and the right by precomposition on Hom.

For completeness, in a commuting diagram of short exact sequences, isomorphisms on the left and right imply an isomorphism in the middle as follows. A middle element mapping to zero has zero image on the right, so comes from a left element; injectivity of the target left inclusion and of the left vertical map makes it zero. Given a target middle element, lift its right image to the source right group, then lift that to the source middle group. The difference in the target middle group lies in the target left image; lift this difference through the left isomorphism and add its image in the source middle group. This proves surjectivity. Applying this argument to (U.4) proves the assertion. □

### Tensoring an explicit contraction

For free chain complexes \(A,D\), their tensor complex has degree-\(n\) group \(\bigoplus_{p+q=n}A_p\otimes D_q\) and differential
\[
\partial(a\otimes d)=\partial a\otimes d+(-1)^p a\otimes\partial d,
\qquad a\in A_p.
\tag{U.5}
\]
For free groups, the tensor group can be defined as the free group on pairs of basis elements, with the evident bilinear extension; this also verifies its bilinear universal property. The cross terms in \(\partial^2\) have opposite signs, so (U.5) squares to zero.

**Lemma U.5 (tensor contraction).** Suppose chain maps \(i:H\to D\), \(\pi:D\to H\) and a degree-one map \(h\) satisfy \(\pi i=1\) and \(1-i\pi=\partial h+h\partial\). Then \(1\otimes i\) and \(1\otimes\pi\) are inverse chain homotopy equivalences after tensoring with \(A\).

**Proof.** The tensor maps commute with (U.5). Their composite on \(A\otimes H\) is the identity. On \(A\otimes D\), set
\[
\mathcal H(a\otimes d)=(-1)^p a\otimes h(d),\qquad a\in A_p.
\]
In \(\partial\mathcal H+\mathcal H\partial\), the two terms containing \(\partial a\otimes h(d)\) have signs \((-1)^p\) and \((-1)^{p-1}\), and cancel. The remaining terms are
\[
a\otimes(\partial h+h\partial)d
=(1-(1\otimes i)(1\otimes\pi))(a\otimes d).
\]
This is the required homotopy. The same calculation works for any coefficient group in the first factor, since it uses only integer addition and signs. □

When \(H=\mathbb Z\) in degree \(r\) with zero differential, \(A\otimes H\) has group \(A_j\) in degree \(j+r\), with its original differential \(\partial_A\). This is an explicit reindexing convention, without an additional suspension sign. It is the convention used for the right-cap maps in the ensuing Thom argument.

## 5. Chain products and cap evaluation

Use the ordinary, unnormalized singular chains of K.1: ordered parametrizations and degenerate simplices remain distinct generators. Write \(\sigma_X,\sigma_Y\) for the coordinate maps of a simplex \(\sigma:\Delta^n\to X\times Y\). A face \([i_0,\ldots,i_k]\) retains that indicated vertex order. Tensor differentials have the sign (U.5).

### The two chain maps

Define the front/back map
\[
\mathcal A\sigma
=\sum_{i=0}^n \sigma_X[0,\ldots,i]\otimes\sigma_Y[i,\ldots,n].
\tag{X.1}
\]
It takes \(C_n(X\times Y)\) to \(\bigoplus_{p+q=n}C_p(X)\otimes C_q(Y)\).

For simplices \(c:\Delta^p\to X\), \(d:\Delta^q\to Y\), a shuffle word contains \(p\) letters \(H\) and \(q\) letters \(V\), preserving the order of the \(H\)'s and the order of the \(V\)'s. Read the word as a path from \((0,0)\) to \((p,q)\), with \(H\) increasing the first coordinate and \(V\) the second. Let \(\ell_w:\Delta^{p+q}\to\Delta^p\times\Delta^q\) be the affine map whose ordered vertices are the pairs of vertices at the successive path positions. Let \(N(w)\) be the number of pairs in which a \(V\) precedes an \(H\). Define
\[
\mathcal S(c\otimes d)
=\sum_w(-1)^{N(w)}(c\times d)\ell_w.
\tag{X.2}
\]
For \(p=0\) or \(q=0\) there is one such word, with sign \(+1\).

**Lemma X.1 (the front/back identity).** The map \(\mathcal A\) is a chain map and is natural under maps in the two factors.

**Proof.** Naturality is immediate from restriction to the same ordered faces. To check the boundary, abbreviate a face of \(\sigma_X\) by \(x[\cdots]\) and one of \(\sigma_Y\) by \(y[\cdots]\). The first-factor boundary of (X.1) consists of
\[
\sum_{i=1}^n\sum_{j=0}^i(-1)^j
x[0,\ldots,\widehat j,\ldots,i]\otimes y[i,\ldots,n].
\tag{X.3}
\]
The second-factor boundary, including the tensor sign, consists of
\[
\sum_{i=0}^{n-1}\sum_{k=i}^n(-1)^k
x[0,\ldots,i]\otimes y[i,\ldots,\widehat k,\ldots,n].
\tag{X.4}
\]
For \(j<i\), the term in (X.3) is the front/back summand in the face of \(\sigma\) omitting \(j\), split at the original vertex \(i\), with its boundary sign \((-1)^j\). For \(k>i\), the term in (X.4) is the corresponding summand in the face omitting \(k\), split at \(i\), with sign \((-1)^k\). These are all summands of \(\mathcal A\partial\sigma\), because the omitted vertex is either before or after its retained splitting vertex.

The remaining terms in (X.3), with \(j=i\), are
\[
(-1)^i x[0,\ldots,i-1]\otimes y[i,\ldots,n],\quad 1\leq i\leq n.
\]
The remaining terms in (X.4), with \(k=i\), are the same tensors after replacing \(i\) by \(i-1\), and have the opposite sign. They cancel. This proves \(\partial\mathcal A=\mathcal A\partial\). In degree zero both boundaries vanish. No degeneracy was discarded. □

**Lemma X.2 (shuffle boundary, geometry and signs).** The map \(\mathcal S\) is a natural chain map. Its affine model simplices cover \(\Delta^p\times\Delta^q\) with disjoint interiors, meeting along faces. With the usual ordered coordinates on the two factors, the determinant sign of \(\ell_w\) is \((-1)^{N(w)}\). The shuffle product is associative, and exchange of the two factors satisfies
\[
T_*\mathcal S(c\otimes d)=(-1)^{pq}\mathcal S(d\otimes c),
\qquad T(x,y)=(y,x).
\tag{X.5}
\]

**Proof.** Naturality follows from the definition by composition. We check each type of face in the boundary of (X.2).

Deleting an internal path vertex between unlike successive steps gives the same face from the word with those two steps interchanged. That interchange changes \(N(w)\) by one, while the deleted vertex has the same position in the two words. These two boundary terms cancel.

If the two steps are \(HH\), deleting the vertex at path position \((i,j)\) gives a shuffle in the first-factor face omitting its \(i\)-th vertex. The deleted vertex has position \(k=i+j\) in the full word. Removing one of the two consecutive \(H\)'s reduces \(N\) by \(j\), the number of preceding \(V\)'s. Thus the boundary sign of the full face is
\[
(-1)^{N(w)+k}=(-1)^{N(w')+j+i+j}
=(-1)^{N(w')+i},
\]
exactly its shuffle sign times the first-factor boundary sign. Conversely, every shuffle of an internal first-factor face has exactly this preimage, obtained by replacing its jump past the omitted vertex by two consecutive \(H\)'s.

If the two steps are \(VV\), deleting \((i,j)\) gives the second-factor face omitting vertex \(j\). The removed \(V\) precedes \(p-i\) horizontal steps, so \(N(w)=N(w')+p-i\). Its full boundary sign is
\[
(-1)^{N(w)+k}=(-1)^{N(w')+p-i+i+j}
=(-1)^{N(w')+p+j}.
\]
This is the shuffle sign, the tensor sign \((-1)^p\), and the second-factor boundary sign \((-1)^j\). Again the correspondence is bijective.

At the initial vertex, deleting it removes an initial \(H\) or \(V\). An initial \(H\) contributes no inversions, giving first-factor face sign \(+1\); an initial \(V\) contributes \(p\), giving tensor sign \((-1)^p\) times the second-factor face sign \(+1\). At the terminal vertex, removing a final \(H\) removes \(q\) inversions, and the face sign \((-1)^{p+q}\) leaves \((-1)^p\), the last first-factor face sign. Removing a final \(V\) removes no inversions, leaving \((-1)^{p+q}\), the tensor sign times the last second-factor face sign. These cases include words using only one letter. There are no other faces. Hence
\[
\partial\mathcal S(c\otimes d)
=\mathcal S(\partial c\otimes d)
+(-1)^p\mathcal S(c\otimes\partial d).
\tag{X.6}
\]

For the geometry, use barycentric coordinates \((t_0,\ldots,t_p)\) on the first factor and put \(s_i=t_i+\cdots+t_p\), \(1\leq i\leq p\). The first simplex is described by
\[
1\geq s_1\geq\cdots\geq s_p\geq0.
\]
At its vertex \(a\), precisely \(s_1,\ldots,s_a\) equal one. Use corresponding coordinates \(z_j\) on the second factor. A word \(w\) orders all the \(s_i,z_j\), respecting their orders within each factor. Its affine simplex is exactly the region in which this combined list is weakly decreasing. Indeed, if its ordered coordinate values are \(a_1\geq\cdots\geq a_{p+q}\), the barycentric coefficients of its successive path vertices are
\[
1-a_1,\ a_1-a_2,\ \ldots,\ a_{p+q-1}-a_{p+q},\ a_{p+q}.
\tag{X.7}
\]
They are nonnegative and sum to one, and substitution reconstructs every coordinate. Any point admits a merge of its two already ordered coordinate lists, so these regions cover the product. Strict inequalities specify exactly one word. If two orders differ, any point satisfying both makes all coordinates whose relative orders differ equal. In (X.7), the intervening barycentric coefficients are then zero. The vertices still permitted are precisely the prefix coordinate sets shared by the two words; their convex hull is a face of each simplex. Conversely those common vertices satisfy both sets of inequalities. This proves the face-intersection statement.

The change from \(t_1,\ldots,t_p\) to \(s_1,\ldots,s_p\) is triangular with diagonal one, and similarly in the second factor. In cumulative coordinates, the vertex-difference matrix of \(\ell_w\) has columns that are the successive partial sums of the coordinate vectors in word order. Its determinant equals that of the permutation placing those vectors in word order, because the partial-sum matrix is triangular with diagonal one. That permutation has \(N(w)\) inversions. Thus \(\det\ell_w=(-1)^{N(w)}\) in the standard ordered coordinates, proving the orientation assertion.

For three simplices, either parenthesization of iterated shuffles is indexed by the same words in three types of letters, preserving the order of each type. In either case, the ordered vertices are the same triples of partial counts. The total sign counts inversions between the first and second types, first and third types, and second and third types. The two parenthesizations count each such pair exactly once, so their signs and affine maps agree. This proves associativity on chains. Exchanging the two types in a two-factor word replaces \(N(w)\) by \(pq-N(w)\), proving (X.5). □

### Actual inverse homotopies

We use affine chains in a convex set only as universal models. An affine \(k\)-simplex is specified by its ordered list of \(k+1\) vertices; repeated vertices are retained. For a fixed vertex \(b\), the operation \(K_b\) that prepends \(b\) satisfies
\[
\partial K_b+K_b\partial=1-\pi_b
\tag{X.8}
\]
on the unaugmented affine chain complex, where \(\pi_b\) sends each vertex to \(b\) and is zero in positive degrees. This is the augmented cone identity already proved in (K.4): in degree zero its boundary is \([v]-[b]\), and in positive degrees all other deletion terms cancel in pairs.

For two convex model sets \(P,Q\), tensor their affine chain complexes. Their degree-zero projections are \(\pi_P,\pi_Q\), and their cone operators are \(K_P,K_Q\). The degree-one map
\[
\mathcal K(c_p\otimes d_q)
=K_Pc_p\otimes d_q+(-1)^p\pi_Pc_p\otimes K_Qd_q
\tag{X.9}
\]
satisfies
\[
\partial\mathcal K+\mathcal K\partial=1-\pi_P\otimes\pi_Q.
\tag{X.10}
\]
For the first summand the terms involving \(\partial d\) cancel and leave \((1-\pi_P)c\otimes d\). For the second, the terms involving \(\partial c\) have opposite signs and leave \(\pi_Pc\otimes(1-\pi_Q)d\). Their sum gives (X.10). In particular, this operator fills every positive-degree cycle and every degree-zero cycle with total augmentation zero.

**Theorem X.3 (product chain equivalence).** The maps \(\mathcal A,\mathcal S\) are inverse up to natural chain homotopies:
\[
1-\mathcal S\mathcal A=\partial H+H\partial,\qquad
1-\mathcal A\mathcal S=\partial J+J\partial.
\tag{X.11}
\]
They and the homotopies preserve the product subspaces \(A\times Y\) and \(X\times B\) and their corresponding tensor subgroups. For smooth maps between manifolds they also preserve smooth chains.

**Proof.** We construct both homotopies by finite induction in degree, using only affine chains in products of standard simplices.

First take the universal diagonal \(\delta_n:\Delta^n\to\Delta^n\times\Delta^n\). In degree zero \(\mathcal S\mathcal A\delta_0=\delta_0\), so put \(h_0=0\). Assuming the model chains \(h_k\) defined for \(k<n\), set
\[
z_n=\delta_n-\mathcal S\mathcal A\delta_n
-\sum_{i=0}^n(-1)^i(\varepsilon_i\times\varepsilon_i)_*h_{n-1}.
\tag{X.12}
\]
Here \(\varepsilon_i:\Delta^{n-1}\to\Delta^n\) is the affine face map. This is an affine chain in the convex set \(\Delta^n\times\Delta^n\). It is a cycle. To see this explicitly, the first two terms have boundary \((1-\mathcal S\mathcal A)\partial\delta_n\), by X.1–X.2. By the lower-degree induction identity, the boundary of the last sum is the same chain minus the sum applying the lower homotopy to \(\partial^2\delta_n\). That latter sum is zero by the double face-deletion identity K.1. Thus \(\partial z_n=0\).

Choose the first product vertex as cone apex and put \(h_n=Kz_n\). For \(n>0\), (X.8) gives \(\partial h_n=z_n\). For a general simplex \(\sigma=(\sigma_X,\sigma_Y)\), define
\[
H\sigma=(\sigma_X\times\sigma_Y)_*h_n.
\tag{X.13}
\]
The lower-face terms in (X.12) push forward to \(H\partial\sigma\), since restriction of each coordinate map to a face is composition with that face map. Equations (X.12)–(X.13) prove the first identity of (X.11) in every degree.

For the tensor homotopy, use the universal generator \(e_p\otimes e_q\), where \(e_p:\Delta^p\to\Delta^p\) and \(e_q:\Delta^q\to\Delta^q\) are identities. Proceed by induction on \(p+q\), starting with \(j_{0,0}=0\). Suppose \(J\) is defined in smaller total degrees by pushforward of its universal models. Form
\[
w_{p,q}
=e_p\otimes e_q-\mathcal A\mathcal S(e_p\otimes e_q)
-J\partial(e_p\otimes e_q).
\tag{X.14}
\]
The last term uses only those previously defined lower-degree models. Every factor in this tensor chain is affine. Since \(1-\mathcal A\mathcal S\) is a chain map and the induction identity holds on the boundary, the same calculation as above gives \(\partial w_{p,q}=0\). For positive total degree use (X.9) and set \(j_{p,q}=\mathcal K w_{p,q}\); it has boundary \(w_{p,q}\). The degree-zero residual is zero. Define
\[
J(c\otimes d)=(c_*\otimes d_*)j_{p,q}
\tag{X.15}
\]
and extend linearly. Face restrictions and the tensor differential now make (X.14) exactly the second identity of (X.11) after pushforward.

The formulas are natural under maps in the two factors, because all model chains are fixed and only the final pushforwards use \(X,Y\). Every simplex in (X.13) maps into \(\sigma_X(\Delta^n)\times\sigma_Y(\Delta^n)\). Every tensor factor in (X.15) maps into the corresponding original factor image. Thus if the first coordinate image lies in \(A\), or the second in \(B\), all the constructed terms have that property. The same is immediate for (X.1)–(X.2), proving the product-subspace assertion.

Finally, the models used in (X.12)–(X.15) remain affine at every stage: face maps, the front/back maps, shuffle maps and affine cones all have this property. A smooth simplex in the sense of K.1 extends to an open neighbourhood of its standard simplex. The product of two such extensions is smooth on an open neighbourhood of the product. Composing it with any affine model simplex therefore extends smoothly to an open neighbourhood of that simplex. This proves preservation of smooth chains. It does not assert that coning an arbitrary smooth simplex directly to a point is smooth at the cone apex. □

### Relative products and their signs

**Theorem X.4 (product pairs).** Suppose \(A\subset X\) and \(B\subset Y\) are open. There is a natural chain homotopy equivalence
\[
C_*(X,A)\otimes C_*(Y,B)
\ \simeq\
C_*(X\times Y,A\times Y\cup X\times B).
\tag{X.16}
\]
The statement is also valid if one of \(A,B\) is empty, with no openness assumption on the other. It induces the corresponding homology and cohomology comparisons with arbitrary coefficient groups. In the cohomology comparison the left complex is \(\operatorname{Hom}_{\mathbb Z}(C_*(X,A)\otimes C_*(Y,B),G)\). For cohomology with a commutative unital ring \(R\), the external product \(u\times v\) is represented, before the last small-chain comparison, by
\[
(u\times v)(\sigma)
=u(\sigma_X[0,\ldots,p])\,v(\sigma_Y[p,\ldots,p+q]),
\qquad \deg u=p,\quad\deg v=q.
\tag{X.17}
\]
When the relative conditions are forgotten this is exactly
\(\operatorname{pr}_X^*u\smile\operatorname{pr}_Y^*v\).

**Proof.** In the tensor complex, quotient by
\[
C_*(A)\otimes C_*(Y)+C_*(X)\otimes C_*(B).
\tag{X.18}
\]
Its quotient identifies with \(C_*(X,A)\otimes C_*(Y,B)\): each is free on pairs of basis simplices for which the first simplex is not in \(A\) and the second is not in \(B\). On the product-chain side quotient by
\[
C_*(A\times Y)+C_*(X\times B).
\tag{X.19}
\]
By the product-subspace assertion in X.3, both chain maps and both homotopies descend to these quotients. They remain inverse chain homotopy equivalences.

If \(A,B\) are open, the two product subspaces in (X.19) are open and cover their union. The quotient comparison constructed in the proof of Lemma E.4, equations (E.12) and the following extended homotopy, proves that the natural map from the quotient by (X.19) to the relative complex on the right of (X.16) is a chain homotopy equivalence. That proof used only the small-chain homotopy for two opens in their union, extended by zero on the remaining basis simplices, and therefore applies to these opens. If one relative subspace is empty, (X.19) already is the chain group of the remaining product subspace, so no replacement is needed.

These are actual integral chain homotopies; applying integer linear combinations with any coefficient group or precomposing cochains with them gives the asserted comparisons, as in K.4. The quotient map and all original chain maps are natural, so their cohomology inverses are natural even though an auxiliary small-chain retraction need not be.

For relative cocycles \(u,v\), regard them as cochains on \(X,Y\) vanishing on \(A,B\). The cochain \(u\otimes v\), evaluated on the tensor group in bidegree \((p,q)\) and zero in other bidegrees, is a cocycle: (U.5) gives its coboundary as \(du\otimes v+(-1)^p u\otimes dv\). It vanishes on (X.18). Composing with \(\mathcal A\) gives (X.17), which vanishes on (X.19). Changing either factor by a coboundary changes the resulting cochain by a coboundary, by the same tensor differential calculation. The cohomology inverse of the natural last quotient map therefore defines the relative external product.

Forgetting the relative conditions commutes with the maps just used, and (X.17) is the front/back cup formula of K.5. This proves the final assertion. The product extends to one \(G\)-valued factor and one integral factor by integer multiplication on \(G\); the proof uses the same bilinear differential identity. □

**Corollary X.5 (exchange and cup commutativity).** For external products of degrees \(p,q\) with coefficients in a commutative unital ring,
\[
T^*(v\times u)=(-1)^{pq}u\times v.
\tag{X.20}
\]
This holds under the relative hypotheses of X.4 as well. Consequently the cup product is graded commutative in ordinary cohomology:
\[
[u]\smile[v]=(-1)^{pq}[v]\smile[u].
\tag{X.21}
\]

**Proof.** The signed tensor exchange
\[
\tau(c_i\otimes d_j)=(-1)^{ij}d_j\otimes c_i
\tag{X.22}
\]
is a chain map. For the term containing \(\partial c\), its signs on the two sides of \(\partial\tau=\tau\partial\) are \((-1)^{ij+j}\) and \((-1)^{(i-1)j}\), which agree. For the term containing \(\partial d\), they are \((-1)^{ij}\) and \((-1)^{i+i(j-1)}\), which also agree. Equation (X.5) says
\[
T_*\mathcal S_{X,Y}=\mathcal S_{Y,X}\tau.
\tag{X.23}
\]
On cohomology, precomposition with \(\mathcal S\) is the inverse of precomposition with \(\mathcal A\), by X.3. Pull (X.20) back by this isomorphism. The left side becomes \((v\otimes u)\tau\), and the right side becomes \((-1)^{pq}(u\otimes v)\). These are equal: both vanish on bidegrees other than \((p,q)\), and there the equality is the sign in (X.22) and commutativity of the coefficients. This proves (X.20). The same maps and homotopies descend to the relative quotients of X.4, and the natural small-chain quotient comparison commutes with \(T\), proving its relative version.

For a space \(X\), the diagonal \(\Delta:X\to X\times X\) satisfies \(T\Delta=\Delta\). Equation (X.17) pulled back along \(\Delta\) is exactly \(u\smile v\). Applying \(\Delta^*\) to (X.20) gives (X.21). This asserts commutativity in cohomology, not in the singular cochain algebra. □

### The right cap map used for Thom classes

Let \(u\) be an integral cochain of degree \(r\geq0\). For a singular \(m\)-simplex, \(m\geq r\), set
\[
R_u\sigma
=u(\sigma[m-r,\ldots,m])\,\sigma[0,\ldots,m-r].
\tag{X.24}
\]
For \(m<r\) set \(R_u=0\). This maps chains with integer coefficients, or with any abelian coefficients \(G\), to chains of degree \(m-r\), multiplying their coefficients by the integer in (X.24).

**Lemma X.6 (right cap identity).** With the convention (X.24), on degree-\(m\) chains,
\[
\partial R_u-R_u\partial=(-1)^{m-r}R_{d_su}.
\tag{X.25}
\]
If \(u\) is a cocycle this is a degree-\(r\) lowering map commuting with the unshifted differentials. If \(u\) vanishes on the chains in a subspace \(A\), it descends from \(C_*(X,A;G)\) to \(C_{*-r}(X;G)\). Its induced homology map depends only on the relative cohomology class of \(u\).

For any cochain \(a\) of degree \(m-r\) with compatible coefficients,
\[
a(R_u c)=(a\smile u)(c).
\tag{X.26}
\]

**Proof.** Equation (X.26) follows immediately from the two ordered face blocks in the cup formula. To derive (X.25), first work with integral chains and \(m\geq r+1\). Evaluate its left side on an arbitrary integer cochain \(a\) of degree \(m-r-1\). Equations (X.26) and the cup differential rule of K.5 give
\[
\begin{aligned}
a(\partial R_u c-R_u\partial c)
&=(d_sa\smile u)(c)-d_s(a\smile u)(c)\\
&=-(-1)^{m-r-1}(a\smile d_su)(c)\\
&=(-1)^{m-r}a(R_{d_su}c).
\end{aligned}
\]
Integer cochains distinguish integral chains: a nonzero coefficient of a basis simplex is detected by the cochain that is one on that simplex and zero on every other one. Thus equality of these evaluations proves (X.25) for integral chains. All its operators are given by integer sums on basis simplices, so the identity holds with arbitrary coefficient group \(G\) too. For \(m=r\), the two terms on the left and the term on the right all take values in a negative degree and are zero. For \(m<r\) they are likewise zero. This proves the identity in all degrees.

If \(d_su=0\), (X.25) gives commutation with boundaries. On a simplex lying in \(A\), the back face in (X.24) also lies in \(A\), so the coefficient is zero. This proves the relative descent.

Suppose \(r\geq1\) and \(u\) is changed by a relative coboundary \(d_sv\), where \(\deg v=r-1\) and \(v\) vanishes on chains in \(A\). On degree \(m\) set
\[
h_m=(-1)^{m-r+1}R_v.
\]
Using (X.25) for \(v\), with its degree \(r-1\), gives
\[
\partial h_m+h_{m-1}\partial
=(-1)^{m-r+1}(\partial R_v-R_v\partial)
=R_{d_sv}.
\tag{X.27}
\]
The map \(h\) descends to relative chains by the same back-face argument. It is therefore the required homotopy between the two cap maps. In degree \(r=0\) there are no negative-degree relative cochains, so a change by a coboundary is zero. This completes the independence proof. □

## 6. Positive local generators and fundamental classes

Write \(H_*(X\mid K;G)=H_*(X,X\setminus K;G)\). Unless coefficients are displayed they are integers. We treat ordinary singular chains and the smooth chains defined in K.1 separately when necessary; the affine representatives below belong to both. All manifolds in this component are smooth, Hausdorff, second countable and without boundary.

### The ordered local generator

Let \(\ell:\Delta^1\to\mathbb R\) be \(\ell(t_0,t_1)=-t_0+t_1\). Thus its initial point is \(-1\), its terminal point is \(1\), and
\[
\partial\ell=[1]-[-1].
\tag{O.1}
\]
For \(r>0\), let \(Q_r\) be the iterated shuffle product of \(r\) copies of \(\ell\), in the listed coordinate order, using X.2. It is a finite signed sum of affine \(r\)-simplices covering the cube \([-1,1]^r\). Its boundary is supported on the boundary of that cube by the shuffle boundary identity. For \(r=0\), let \(Q_0\) be the positively weighted point.

**Lemma O.1 (positive Euclidean generator).** The relative class
\[
g_r=[Q_r]\in H_r(\mathbb R^r\mid\{0\})
\tag{O.2}
\]
generates this group, which is infinite cyclic. The other homology groups of this pair vanish. The same assertions hold for smooth singular chains, and inclusion of smooth into ordinary chains sends the displayed generator to the displayed generator. There is a unique integral cohomology class \(u_r\) in degree \(r\) evaluating to one on \(g_r\).

**Proof.** In dimension one, the pair sequence from E.1 identifies the boundary map from \(H_1(\mathbb R,\mathbb R\setminus0)\) with the kernel of
\[
H_0(\mathbb R\setminus0)\longrightarrow H_0(\mathbb R).
\]
Indeed the positive-degree homology of \(\mathbb R\) vanishes by its straight contraction. The negative and positive half-lines are each contractible, and every path in their union stays in one half-line by the intermediate value theorem. Thus their zero-dimensional group is \(\mathbb Z\oplus\mathbb Z\), and the displayed map is addition. Its kernel is freely generated by \([1]-[-1]\). Equation (O.1) proves that \([\ell]\) is the corresponding generator. This also proves all other relative groups vanish, including degree zero. The argument applies verbatim to smooth chains: all the indicated contractions and paths can be taken smooth.

The relative complex of the line is free on the simplices not lying in its punctured subspace. By U.2 it has a chain homotopy equivalence with \(\mathbb Z\) in degree one, whose inclusion sends \(1\) to the prescribed cycle \(\ell\). Tensoring this equivalence with another free complex preserves it by U.5. Apply this repeatedly and then use the relative product equivalence X.4. The relative subspaces \(\mathbb R\setminus0\) are open, and their product union consists precisely of the points at which at least one coordinate is nonzero. Hence it is \(\mathbb R^r\setminus0\). The tensor of the prescribed cycles is sent by the iterated shuffle to \(Q_r\). The resulting homotopy equivalence with \(\mathbb Z\) in degree \(r\) proves both its generator assertion and the vanishing in other degrees.

X.3–X.4 preserve smooth chains; their denominator replacement uses the smooth version of K.3. Thus this proof also gives the smooth assertion. For \(r=0\), the pair is a point relative to the empty set; the point-complex calculation after E.1 gives exactly the assertion. Finally U.3, with the preceding homology group zero, identifies integral degree-\(r\) cohomology with the homomorphisms from this infinite cyclic homology group. Evaluation one determines precisely one such homomorphism. □

For an ordered real vector space, transport \(g_r\) by an ordered linear coordinate map. For a point \(x\in\mathbb R^r\), write \(g_x\) for the image of \(g_r\) under translation by \(x\). Scaling all coordinates by a positive constant leaves this class unchanged: the positive scalar interpolation to \(1\) is a homotopy of punctured pairs. The next result gives the full coordinate rule, rather than just this special case.

### Linear and smooth coordinate changes

**Lemma O.2 (linear sign).** An invertible real linear map \(A:\mathbb R^r\to\mathbb R^r\) sends \(g_r\) to
\[
A_*g_r=\operatorname{sgn}(\det A)\,g_r.
\tag{O.3}
\]

**Proof.** First we prove that every positive-determinant matrix can be joined to the identity through invertible matrices. On its ordered columns \(a_j\), define successively
\[
w_j=a_j-\sum_{i<j}(q_i\cdot a_j)q_i,\qquad q_j=w_j/|w_j|.
\]
Induction makes the preceding \(q_i\)'s orthonormal, so \(w_j\) is orthogonal to them. It is nonzero, since otherwise the independent column \(a_j\) would lie in the span of its predecessors. Thus these formulas give an orthogonal matrix \(Q\) and \(A=QR\), where \(R_{ij}=q_i\cdot a_j\) for \(i\leq j\), its lower entries vanish and \(R_{jj}=|w_j|>0\). This proves the required Gram–Schmidt assertion using only the opening lesson's inner-product algebra. The interpolation \((1-t)R+tI\) remains upper triangular with positive diagonal, so multiplying it by \(Q\) joins \(A\) to \(Q\) through invertible matrices. Since \(\det R>0\), a positive determinant for \(A\) gives \(\det Q=1\).

Here is an explicit reduction of such a \(Q\) by plane rotations. For any unit pair \((a,b)\), the matrix
\[
\begin{pmatrix}a&b\\-b&a\end{pmatrix}
\tag{O.4}
\]
has determinant one. It has a path from the identity: normalize the straight segment from \((1,0)\) to \((a,b)\), which never passes through zero unless \((a,b)=(-1,0)\). In that exceptional case use two normalized segments, through \((0,1)\). Each segment is smooth on a neighbourhood of its closed parameter interval.

Given the unit first column of \(Q\), successively consider its entries in coordinates \(1,i\), for \(i=r,r-1,\ldots,2\). If they are both zero, do nothing. Otherwise put \(s=(v_1^2+v_i^2)^{1/2}\), \(a=v_1/s\), \(b=v_i/s\), and left multiply by (O.4) in that plane. The entries become \(s,0\), and coordinates already eliminated remain zero. The final first column is \(e_1\). Orthogonality then makes the first row \(e_1^{\mathsf T}\) too, and the remaining block is orthogonal with determinant one. Induction on \(r\), with \(r=1\) immediate, reduces that block by the same operations. Each operation has the indicated path from the identity; composing their finitely many paths proves that \(Q\), and hence \(A\), is connected to the identity through invertible matrices.

Every matrix along this path maps nonzero vectors to nonzero vectors. The pair homotopy identity following K.1 therefore makes its induced map on the relative homology group the identity. This proves (O.3) for positive determinant.

Let \(J\) reflect the first coordinate. Its action on the line generator is negative: its boundary class is \([-1]-[1]\), and the boundary isomorphism in O.1 determines the relative class. Naturality of the shuffle product shows that reflection of the first factor sends \(g_r\) to \(-g_r\). For negative-determinant \(A\), the matrix \(AJ\) has positive determinant and \(A=(AJ)J\). This proves (O.3). The finite smooth pieces of the matrix paths prove the same statement on smooth chains. In dimension zero there is only the identity linear map and its determinant is \(1\). □

**Lemma O.3 (smooth local sign).** Let \(f:U\to V\) be a smooth diffeomorphism between open subsets of \(\mathbb R^r\), and let \(x\in U\). Under excision and the translation conventions just fixed, its map on local homology at \(x\) and \(f(x)\) is multiplication by
\[
\operatorname{sgn}\det Df(x).
\tag{O.5}
\]

**Proof.** Dimension zero is immediate, so assume \(r>0\). Translate source and target so that \(x=0=f(x)\). Put \(A=Df(0)\), which is invertible by differentiating \(f^{-1}f=1\). For \(t\in[0,1]\) and \(y\) in a small ball about zero, define
\[
F(t,y)=\int_0^1 Df(sty)y\,ds.
\tag{O.6}
\]
The segment from \(0\) to \(ty\) lies in \(U\) after shrinking that ball. Here smoothness of the parameter integral can be checked using only the opening lesson's Lemmas 0.1 and 0.3. For the smooth integrand \(G(s,z)=Df(sty)y\), where \(z=(t,y)\), restrict \(z\) to a compact box in its open domain. The fundamental theorem expresses each parameter difference quotient of \(G\) as the average of its corresponding derivative along a short parameter segment. Uniform continuity of that derivative on the compact product makes these quotients converge uniformly in \(s,z\). Lemma 0.3 passes this uniform limit through the integral over \(s\), giving \(\partial_z\int G\,ds=\int\partial_zG\,ds\), with continuous derivative. Repeating this for every derivative proves smoothness of \(F\), including at \(t=0\). The one-dimensional fundamental theorem also gives
\[
F(t,y)=t^{-1}f(ty)\quad(t>0),\qquad F(0,y)=Ay.
\tag{O.7}
\]
The same integral formula extends to an open neighbourhood of the closed parameter interval after shrinking the ball once more, so it is also a smooth homotopy in the sense used for smooth chains.

Let \(c=1/\|A^{-1}\|>0\); the opening lesson's operator-norm estimate gives \(|Ay|\geq c|y|\). Continuity of \(Df\) allows a ball on which \(\|Df(z)-A\|<c/2\). Equation (O.6) consequently gives
\[
|F(t,y)-Ay|\leq(c/2)|y|,
\qquad |F(t,y)|\geq(c/2)|y|.
\tag{O.8}
\]
Thus \(F(t,y)\ne0\) whenever \(y\ne0\). It is a homotopy of pairs from \(A\) to \(f\), with source this small ball punctured at zero and target \(\mathbb R^r\) punctured at zero. The image need not stay in a prescribed smaller target chart; the target here is all of coordinate space.

Excision E.2 identifies the local relative groups of the ball, \(U\), \(V\), and their ambient coordinate spaces with the corresponding groups at zero. To check its hypothesis, the complement of any open neighbourhood of zero is closed and contained in the open punctured space. Naturality of these inclusions and pair homotopy therefore identifies \(f_*\) with \(A_*\). Apply O.2. In dimension zero the statement is immediate. □

### Coherence and fundamental classes

In positive dimension, a smooth orientation is an atlas whose coordinate transitions have positive determinant. Use its charts, excision and the local classes \(g_x\) to specify a generator \(o_x\in H_r(M\mid\{x\})\) at every point. Lemma O.3 proves that overlapping oriented charts specify the same generator. In dimension zero, specify a sign \(\epsilon_x\in\{1,-1\}\) at each point and put \(o_x=\epsilon_x[x]\). This convention includes both orientations of a point.

**Theorem O.4 (oriented integral fundamental classes).** This family \((o_x)\) is locally coherent in the sense preceding E.8, for both ordinary and smooth chains. Therefore every compact \(K\subset M\) has a unique class
\[
[M]_K\in H_r(M\mid K)
\tag{O.9}
\]
restricting to \(o_x\) at all \(x\in K\). These classes are compatible as compact supports are enlarged. For compact \(M\), the class \([M]=[M]_M\in H_r(M)\) is its integral fundamental class.

**Proof.** We first prove coherence without presupposing chart integration. In an oriented chart, choose a closed coordinate ball \(L\) compactly contained in the chart range. Translate its centre to zero. Choose a positive number \(R\) such that \(L\) lies in the interior of \([-R,R]^r\). The scaled cube chain \(Q_{r,R}\) is a relative cycle supported on \(L\) in the sense that its boundary lies outside \(L\); its interior is allowed to extend outside \(L\).

Its class in \(H_r(\mathbb R^r\mid\{x\})\) is \(g_x\) for every \(x\in L\). To see the sign explicitly, translate the cube through \(tx\), \(0\leq t\leq1\). A boundary point \(z\) of the original cube satisfies
\[
\big|z-(1-t)x\big|_\infty\geq R-|x|_\infty>0.
\]
Thus the moving boundary never meets \(x\). The prism identity applied to the cube chain shows that its relative class at \(x\) equals that of the cube centred at \(x\). The latter is the positive generator by translation and positive scaling. This argument uses only affine chains and a smooth translation homotopy.

Excision E.2 transfers the cube's class in \(H_r(\mathbb R^r\mid L)\) to the coordinate chart and then to \(M\). This remains valid if the large test cube itself is not inside the chart: the inclusion of the chart into coordinate space is an isomorphism on the relative groups supported on the compact set \(L\). Explicitly the chart complement is closed and disjoint from \(L\), hence contained in the open complement of \(L\), as required by excision. Composing with the map to the relative group supported on the interior of \(L\) proves local coherence for the points of that interior. Such interiors form neighbourhoods of all points. In dimension zero, each one-point chart supplies its chosen signed point cycle, so coherence is immediate.

Theorem E.8 now proves the existence and uniqueness of (O.9). If \(K'\subset K\), its image in \(H_r(M\mid K')\) has the specified point restrictions and equals \([M]_{K'}\) by that uniqueness. The smooth construction maps to the ordinary one: their local generators agree by O.1, so E.7's pointwise detection identifies their images. For compact \(M\), the complement of \(M\) is empty, giving the asserted absolute class. □

## 7. Thom classes over arbitrary Hausdorff bases

Let \(p:E\to B\) be a locally trivial real vector bundle of fixed finite rank \(r\geq0\) over a Hausdorff space \(B\). Write \(Z\) for its zero section, \(E^\times=E\setminus Z\), and \(E_A=p^{-1}(A)\) for any subspace \(A\subset B\). The complement \(E^\times\) is open, as is checked in each trivialization. An orientation means a choice of oriented linear trivializations with positive-determinant transition matrices. Rank zero has its canonical orientation.

There are two coefficient settings. For an oriented bundle take \(R=\mathbb Z\). For any bundle take \(R=\mathbb F_2\), the two-element field. In the second case the local generator is the coefficient image of O.1 and is independent of linear coordinate changes: their signs in O.2 all become \(1\). Let \(G\) be any \(R\)-module. In particular, for the integral setting \(G\) is any abelian group. Singular chains, cochains and relative quotients have the conventions of K, E and X.

A Thom class means a class \(u_E\in H^r(E,E^\times;R)\) restricting on every fibre to the positive local class of O.1 in the oriented case, or to its nonzero mod-two image in the other case. The positivity requirement fixes the integral sign separately on every fibre.

For a relative cocycle \(u\) representing such a class, define
\[
T_u=p_*R_u:C_m(E,E^\times;G)\longrightarrow C_{m-r}(B;G).
\tag{T.1}
\]
Here \(R_u\) is the right cap map (X.24); its coefficients multiply \(G\) through its \(R\)-module structure. The proof of (X.25) is an integer coefficient identity on formal faces and cochain values, so it also holds with values in \(R\) acting on \(G\). It follows that \(T_u\) commutes with the unshifted differentials, is defined on relative chains, and its induced map depends only on the relative class of \(u\). We use \(C_*(B;G)[r]\) to mean \(C_{m-r}(B;G)\) in degree \(m\), with that unchanged differential.

### The trivial bundle, with the actual cap map

**Lemma T.1 (trivial Thom isomorphism).** For \(E=B\times\mathbb R^r\) and the specified product orientation, there is exactly one Thom class, namely the pullback of \(u_r\) from the fibre. Its cap map gives
\[
H_m(E,E^\times;G)\ \xrightarrow[\ T_u\ ]{\ \cong\ }\
H_{m-r}(B;G).
\tag{T.2}
\]
The cohomology of this pair vanishes below \(r\). Its degree-\(r\) cohomology over \(R\) is identified, by fibre restriction, with functions from the path components of \(B\) to \(R\); the Thom class corresponds to the constant function \(1\).

**Proof.** Let \(D=C_*(\mathbb R^r,\mathbb R^r\setminus0;\mathbb Z)\). Lemma O.1 and U.2 give maps \(i:\mathbb Z[r]\to D\), \(\pi:D\to\mathbb Z[r]\) and \(h\) such that \(i(1)=Q_r\), \(\pi i=1\), and \(1-i\pi=\partial h+h\partial\). The relative product equivalence X.4, with the empty relative subset in the base factor, and U.5 give a chain homotopy equivalence
\[
C_*(B\times\mathbb R^r,B\times(\mathbb R^r\setminus0);\mathbb Z)
\simeq C_*(B;\mathbb Z)\otimes D
\simeq C_*(B;\mathbb Z)[r].
\tag{T.3}
\]
The maps in the second equivalence send a base simplex tensored with the fibre generator to the corresponding reindexed base simplex. Integer chain homotopies remain valid after applying coefficients in \(G\).

We verify that the map in the statement is this isomorphism, rather than leave an unidentified isomorphism in (T.3). Choose an integral relative cocycle \(v\) representing \(u_r\), so \(v(Q_r)=1\). Regard \(v\) as a chain map \(D\to\mathbb Z[r]\), zero outside degree \(r\). Since \(vi=1\), the contraction just given implies
\[
v-\pi=vh\partial,\qquad
1-iv=\partial(h-ivh)+(h-ivh)\partial.
\tag{T.4}
\]
For the first formula compose \(1-i\pi=\partial h+h\partial\) with \(v\) and use \(v\partial=0\). For the second use \(\partial i=0\) and substitute the first formula. Hence \(i,v\) themselves are inverse chain homotopy equivalences. The same statements hold after reduction to \(R\).

Put \(u=\operatorname{pr}_{\mathbb R^r}^*v\), with reduction to \(R\) if necessary. Its relative class restricts to the specified generator in each fibre. On a product-space simplex \(\sigma\) of degree \(m\), the front/back map has terms indexed by all splitting vertices. Applying \(1\otimes v\) retains only the splitting vertex \(m-r\). Consequently
\[
(1\otimes v)\mathcal A\sigma
=v\bigl(\sigma_{\mathbb R^r}[m-r,\ldots,m]\bigr)
  \sigma_B[0,\ldots,m-r]
=p_*R_u\sigma.
\tag{T.5}
\]
Both sides are zero for \(m<r\). This equality is on unnormalized chains; it never assumes that \(v\) vanishes on degenerate simplices. Equations (T.4), U.5 and X.4 prove (T.2), with every \(G\).

Dualizing the actual homotopies in (T.3), or equivalently using K.4, identifies cohomology with the reindexed cohomology of \(B\). In degree \(r\) this is \(H^0(B;R)\). A zero-cocycle assigns a value to each point and has equal values at the two endpoints of every path; conversely those equalities are precisely its cocycle equations. There are no zero-dimensional coboundaries. Thus this group is the set of functions on path components, without a claim of topological local constancy on an arbitrary space. Evaluation on the cycle \(\{b\}\times Q_r\) shows that its value at \(b\) is exactly fibre restriction. This proves the final assertions and uniqueness of the Thom class. For rank zero, \(u\) is the constant zero-cocycle \(1\), (T.1) is the identity, and the same proof applies. □

### Gluing over a finite trivializing cover

We use the relative Mayer–Vietoris complexes proved in E.3. For two open subsets \(U,V\) covering \(B\), these may be written
\[
0\longrightarrow C_*(E_{U\cap V},E_{U\cap V}^\times;G)
\longrightarrow C_*(E_U,E_U^\times;G)\oplus
 C_*(E_V,E_V^\times;G)
\longrightarrow C_*^{\,U,V}(E,E^\times;G)
\longrightarrow0.
\tag{T.6}
\]
The first map is \(c\mapsto(c,-c)\), the second is addition, and the last complex is generated by relative simplices lying in one of \(E_U,E_V\). Exactness follows on simplex bases as in E.3. K.3 gives a chain homotopy equivalence from this small relative complex to the full relative complex; the support-preserving homotopy also preserves \(E^\times\). The same construction applies to the base cover. These are degreewise split sequences, so dualizing with coefficients gives the cohomology Mayer–Vietoris sequence as well.

We record the exact-sequence argument used below. In a commuting diagram
\[
A_1\to A_2\to A_3\to A_4\to A_5
\]
over another exact row \(B_1\to\cdots\to B_5\), if the vertical maps at positions \(1,2,4,5\) are isomorphisms, the middle one is an isomorphism. For injectivity, an element of \(A_3\) mapping to zero has zero image in \(A_4\), hence comes from \(a_2\). The image of \(a_2\) in \(B_2\) comes from \(b_1\); lift \(b_1\) through \(A_1\to B_1\) and subtract its image from \(a_2\). Injectivity at \(A_2\) then makes the difference zero, so the original \(A_3\) element was zero. For surjectivity, start with \(b_3\), lift its image in \(B_4\) to \(a_4\), and use injectivity at \(A_5\) to see that \(a_4\) comes from some \(a_3\). The difference between \(b_3\) and the image of \(a_3\) comes from \(B_2\); lift that through \(A_2\) and correct \(a_3\). This proves the assertion with all needed existence and exactness steps.

**Lemma T.2 (finite-cover Thom class).** If \(E\to B\) has a finite trivializing cover, it has a unique Thom class in the appropriate coefficient setting above. The map (T.2) is an isomorphism for every \(G\), and \(H^k(E,E^\times;R)=0\) for \(k<r\). More generally, a degree-\(r\) class is determined by its restrictions to all fibres.

**Proof.** Induct on the number of members of the chosen finite cover; the empty base is immediate, and a single member is T.1. Write \(B=U\cup V\), with \(U\) the union of all but the last member and \(V\) the last member. The bundle on \(U\) has the shorter finite cover. The bundle on \(V\), and on \(W=U\cap V\), is trivial, since the latter inherits the trivialization on \(V\).

For \(k<r\), the cohomology Mayer–Vietoris sequence has zero groups at the two sides of \(H^k(E,E^\times;R)\):
the preceding group is \(H^{k-1}(E_W,E_W^\times;R)\), and the following one is the direct sum of the degree-\(k\) groups over \(U,V\). T.1 and induction make them zero, including negative degrees. Hence the middle group is zero.

In degree \(r\), the preceding intersection group still vanishes. Restriction therefore injects \(H^r(E,E^\times;R)\) into the direct sum of the groups over \(U,V\), with image the pairs agreeing on \(W\). By induction and T.1 the degree-\(r\) groups on \(U,V,W\) are detected by their fibre restrictions. Thus degree-\(r\) classes on \(B\) are detected by those restrictions too.

The two already constructed Thom classes on \(U,V\) restrict to the same class on \(W\): both have the specified value on each fibre, and T.1 detects classes there. In the integral case the orientations agree on overlaps by the positive transition condition and O.2; in the mod-two case all transition signs reduce to one. Exactness now supplies a unique class \(u_B\) restricting to those two classes. It is the required Thom class.

Choose a relative cocycle \(u\) representing it. On each term of (T.6), right cap with its restriction followed by \(p_*\) has image in the corresponding base-cover term: a face of a simplex lying over an open set still lies over that set. These maps commute with the two arrows in (T.6), and commute with differential by X.6. They therefore give a morphism from (T.6) to the base-cover sequence reindexed by \(r\).

The induced maps commute also with the connecting homomorphisms. Explicitly the connecting class is obtained by lifting a small cycle to a pair of chains, taking its boundary, and reading this boundary in the intersection complex. Applying \(p_*R_u\) before or after these steps gives the same chains, since it commutes with the lifts' sum, their boundaries and the intersection inclusion. There is no extra sign: both reindexed complexes here use the unchanged differential of (T.1).

On the \(U,V,W\) homology groups these maps are the Thom cap isomorphisms by induction and T.1. The five-position exact-sequence argument above gives an isomorphism on the small-cover term in every degree. Its inclusion into the full pair, and the corresponding inclusion on the base, induce isomorphisms by K.3 and commute with the actual cap maps. Hence (T.2) holds on the full complexes. This argument is valid with every \(G\). Changing a representative of \(u\) does not change its induced cap map, by the explicit homotopy in X.6. □

Notice that this proof imposes no paracompactness or local contractibility on \(B\). It also does not assert that a bundle with a finite trivializing cover is trivial. The use of the intersection \(W\) is legitimate because it lies inside the one trivializing set \(V\).

### Finite chains give the general case

**Theorem T.3 (Thom existence, uniqueness and isomorphisms).** Every oriented real rank-\(r\) vector bundle over a Hausdorff base has a unique integral Thom class with its specified fibre signs. Every real vector bundle over a Hausdorff base has a unique mod-two Thom class. In the respective coefficient setting, cap with it gives (T.2) for every \(R\)-module \(G\), and
\[
\Phi_G:H^q(B;G)\longrightarrow H^{q+r}(E,E^\times;G),
\qquad
\Phi_G(a)=p^*a\smile u_E
\tag{T.7}
\]
is an isomorphism. The target cohomology vanishes in degrees below \(r\).

**Proof.** For every compact \(C\subset B\), the restricted bundle over \(C\) has a finite trivializing cover: restrict the original cover and use compactness. Lemma T.2 gives its Thom class \(u_C\) and cap isomorphisms \(T_C\). If \(C\subset D\) are compact, the restriction of \(u_D\) to \(E_C\) has the same fibre values as \(u_C\), so the detection statement in T.2 gives equality. The cap maps on homology consequently commute with inclusions, by their chain naturality and their independence of cocycle representatives.

Every finite singular chain of \(B\) has compact image, and every finite singular chain in \(E\) has compact projected image in \(B\). This follows because a standard simplex is compact, its continuous image is compact, and a finite union of compact subsets is compact. Compact subsets of a Hausdorff space are closed, as proved in the opening lesson, and finite unions of them remain compact. At the chain level we therefore have filtered unions
\[
C_*(B;G)=\bigcup_{C\subset B\ {\rm compact}}C_*(C;G),
\qquad
C_*(E,E^\times;G)=
\bigcup_{C\subset B\ {\rm compact}}C_*(E_C,E_C^\times;G).
\tag{T.8}
\]
The relative inclusions are injective on these complexes: they are inclusions of the free simplex index sets after removing the simplices lying entirely in \(E^\times\), with coefficients in \(G\).

Homology has the corresponding finite-chain property. A cycle lies in one such subcomplex. If it becomes a boundary in the full complex, a finite bounding chain lies in another compact projected subcomplex, and their union is a single compact set on which it already bounds. These two observations prove both surjectivity and injectivity of the homology map from the filtered union of classes; no exactness theorem about limits is being assumed.

The compatible \(T_C\)'s now define isomorphisms
\[
\mathcal T_G:H_m(E,E^\times;G)\longrightarrow H_{m-r}(B;G).
\tag{T.9}
\]
For surjectivity represent a target class by a cycle in a compact \(C\) and use \(T_C^{-1}\). For injectivity represent a source class over \(C\). If its image bounds globally, a finite bounding base chain lies over a compact \(D\) containing \(C\). The isomorphism \(T_D\) makes the original class zero over \(D\), and hence globally. In particular the relative homology over \(R\) vanishes below \(r\).

We now construct the global cohomology class, without identifying cohomology with an inverse limit over compact subsets. Let
\[
\lambda:H_r(E,E^\times;R)
\xrightarrow{\mathcal T_R}H_0(B;R)
\xrightarrow{\epsilon}R,
\tag{T.10}
\]
where \(\epsilon\) adds the coefficients of a zero-cycle. It is well defined because the boundary of each one-simplex has coefficient sum zero. For \(R=\mathbb Z\), U.3 and \(H_{r-1}(E,E^\times;\mathbb Z)=0\) make evaluation an isomorphism from degree-\(r\) cohomology to the dual of this homology group. For \(R=\mathbb F_2\), the field evaluation proof after U.3 gives the same assertion. Thus exactly one class \(u_E\) evaluates as \(\lambda\).

Its restriction to \(E_C\) is \(u_C\). Indeed (T.9) is compatible with inclusion, so (T.10) restricts to \(\epsilon T_C\). For a degree-\(r\) relative cycle \(z\) on \(E_C\), the cap formula gives
\[
\epsilon\,p_*R_{u_C}(z)=u_C(z):
\tag{T.11}
\]
on a simplex the remaining front face is just its first vertex, with coefficient \(u_C\) evaluated on the whole simplex. Evaluation is injective in this degree on \(E_C\), by T.2's lower homology vanishing and the same coefficient argument. Equation (T.11) proves equality of the two restricted cohomology classes. In particular the restriction to a single fibre is the required generator.

If another global class has those fibre values, T.2 identifies its restriction with \(u_C\) on every compact \(C\). Every degree-\(r\) cycle has such a compact projected support, so its evaluations agree with \(\lambda\). Injectivity of global evaluation proves uniqueness.

Choose a relative cocycle representing \(u_E\). On each compact \(C\) its cohomology class equals \(u_C\); the cap homotopy X.6 therefore identifies its induced map with \(T_C\), also on chains with coefficients in any \(G\). Every homology class has compact projected support, so its global cap map is exactly (T.9). This proves the asserted homology isomorphism with the actual map (T.1).

It remains to prove (T.7), including arbitrary coefficients. In the integral case \(T_{u_E}:C_*(E,E^\times;\mathbb Z)\to C_*(B;\mathbb Z)[r]\) is a homology isomorphism between free abelian complexes. Corollary U.4 says its dual with every abelian coefficient group \(G\) is a cohomology isomorphism. In the field case both complexes are vector-space complexes; the field evaluation proof following U.3 says the same for every \(\mathbb F_2\)-vector space \(G\). More explicitly, the cycle, boundary and complementary basis decompositions used there work with \(G\)-valued functionals just as with scalar functionals; homology isomorphisms therefore induce isomorphisms on their \(G\)-valued Hom groups and on cohomology.

The dual map is precisely (T.7). For a base cochain \(a\), equation (X.26) gives on every relative chain
\[
a\bigl(p_*R_{u_E}c\bigr)
=(p^*a\smile u_E)(c).
\tag{T.12}
\]
The right side vanishes on \(E^\times\), as required. The reindexing introduces no sign, since all differentials have retained the convention in (T.1). The same dual argument shows that the relative cohomology groups below \(r\) are zero. This completes the proof, including \(r=0\), when all groups and maps reduce to the canonical unit convention. □

### Naturality and the elementary Euler properties

For an oriented bundle define its Euler class by
\[
e(E)=s_0^*j^*u_E\in H^r(B;\mathbb Z),
\tag{T.13}
\]
where \(j^*\) forgets the relative condition and \(s_0:B\to E\) is the zero section. The same formula defines a mod-two Euler class without an orientation. No identification with Stiefel–Whitney or Chern classes is made at this point.

**Theorem T.4 (pullback, sums and Euler classes).** Thom classes are natural under pullback with the induced orientation, and their integral sign reverses when the orientation reverses. The Euler classes satisfy
\[
e(f^*E)=f^*e(E),\qquad
e(E_1\oplus E_2)=e(E_1)\smile e(E_2).
\tag{T.14}
\]
The direct sum uses the first bundle's coordinates followed by the second's. Integral Euler classes change sign under orientation reversal, have \(2e(E)=0\) in odd rank, and vanish if \(E\) has a nowhere-zero section. The corresponding naturality, product and nonzero-section assertions hold modulo two.

**Proof.** For a continuous \(f:A\to B\) between Hausdorff spaces, the pullback bundle is
\[
f^*E=\{(a,v)\in A\times E:f(a)=p(v)\}.
\]
A trivialization over \(U\subset B\) gives one over \(f^{-1}(U)\), by retaining its fibre coordinates. Thus this is a vector bundle and its map \(\widetilde f:f^*E\to E\) is a linear isomorphism on each fibre. Its pulled-back relative Thom class has the prescribed fibre values, so uniqueness in T.3 gives \(u_{f^*E}=\widetilde f^*u_E\). The zero sections and relative-forgetting maps commute with these pullbacks, proving the first identity in (T.14). Negating all prescribed integral fibre generators negates the unique Thom class, and therefore also its Euler class.

For the direct sum, use the external relative product from X.4:
\[
u_{E_1}\times u_{E_2}\in
H^{r+s}(E_1\times E_2,\,
E_1^\times\times E_2\ \cup\ E_1\times E_2^\times;R).
\tag{T.15}
\]
Both relative subsets are open. Pull this class back by the map from \(E_1\oplus E_2\) to \(E_1\times E_2\). A nonzero direct-sum vector has at least one nonzero component, so this is a map of the required relative pairs.

On a fibre the product class evaluates to one on \(Q_{r+s}\). Indeed associativity of X.2 gives \(Q_{r+s}=\mathcal S(Q_r\otimes Q_s)\), with the indicated coordinate order. X.3 makes \(\mathcal A\mathcal S\) induce the identity on tensor homology. The cochain \(u_r\otimes u_s\) therefore evaluates on this class as \(u_r(Q_r)u_s(Q_s)=1\). By O.1 and U.3 this is precisely its positive fibre class; the same computation holds over \(\mathbb F_2\). The uniqueness in T.3 identifies the pullback of (T.15) with \(u_{E_1\oplus E_2}\). After forgetting relative conditions, X.17 identifies the external product with the cup product of the two projection pullbacks. Restricting to the zero section proves the second identity of (T.14).

Let \(N:E\to E\) be fibre negation. Its linear determinant sign is \((-1)^r\), so O.2 and uniqueness give \(N^*u_E=(-1)^r u_E\) integrally. Since \(Ns_0=s_0\), pulling back to the zero section gives \(e(E)=(-1)^r e(E)\), which proves the odd-rank assertion.

Finally let \(s:B\to E^\times\) be a nowhere-zero section. The absolute class \(j^*u_E\) restricts to zero on \(E^\times\): a representative relative cocycle is zero on all chains in that subspace. Consequently \(s^*j^*u_E=0\). The homotopy \(s_t(b)=t\,s(b)\), \(0\leq t\leq1\), is a homotopy of maps into \(E\) from \(s_0\) to \(s\). It need not stay in \(E^\times\), since it is being applied to the absolute class. The prism cochain homotopy K.1 identifies the two pullbacks of that class, proving \(e(E)=0\). No fibre metric or normalization of \(s\) is used. All these arguments except the integral sign statement also apply over \(\mathbb F_2\). □

## 8. Euler indices and the sphere

Let \(M\) be an oriented smooth manifold of dimension \(r>0\), and \(E\to M\) an oriented smooth real bundle of rank \(r\). Let \(s\) be a smooth section and suppose \(x\) is an isolated zero. Choose a neighbourhood \(U\) containing no other zero. The section is a map of pairs
\[
s:(U,U\setminus\{x\})\longrightarrow(E,E^\times).
\]
The pullback \(s^*u_E\) is therefore a degree-\(r\) integral relative class. Excision identifies \(H_r(U\mid\{x\})\) with the local group of \(M\). Define
\[
\operatorname{ind}_x(s)
=\langle s^*u_E,o_x\rangle\in\mathbb Z,
\tag{N.1}
\]
where \(o_x\) is the positive local generator in O.4. Restricting to smaller neighbourhoods leaves this value unchanged, by naturality of relative evaluation and excision. Thus it does not depend on the chosen \(U\).

**Lemma N.1 (nondegenerate local zero).** In oriented base coordinates and an oriented bundle frame near \(x\), let \(f\) be the coefficient vector of \(s\). If \(Df(x)\) is invertible, the zero is isolated and
\[
\operatorname{ind}_x(s)=\operatorname{sgn}\det Df(x).
\tag{N.2}
\]

**Proof.** The inverse function theorem in the opening lesson, Theorem 1.2, makes \(f\) a diffeomorphism near \(x\) onto a neighbourhood of zero. In particular its zero is isolated there. On the chosen trivialization the Thom class is the pullback of the fibre class \(u_r\), by T.1 and the uniqueness in T.3. The relative pullback by the section is consequently the relative pullback of \(u_r\) by \(f\). Lemma O.3 sends the positive base local homology generator to \(\operatorname{sgn}\det Df(x)\) times the positive fibre generator. Evaluation, together with \(u_r(g_r)=1\), proves (N.2).

The determinant sign is independent of these oriented choices. For another oriented frame, the new coefficient map is \(A(y)f(y)\) with \(A(y)\) invertible and of positive determinant. At the zero its derivative is \(A(x)Df(x)\), since the term differentiating \(A\) multiplies \(f(x)=0\). An oriented change of base coordinates multiplies on the right by the derivative of its inverse, also of positive determinant. Both changes preserve the sign. □

**Theorem N.2 (isolated-zero formula).** Suppose \(M\) is compact and \(s\) has only isolated zeros. Then it has finitely many zeros and
\[
\langle e(E),[M]\rangle
=\sum_{x:\,s(x)=0}\operatorname{ind}_x(s).
\tag{N.3}
\]

**Proof.** The zero set \(K\) is closed: in a bundle chart it is the inverse image of zero under a continuous coefficient map. It is compact as a closed subset of \(M\). Each zero has an open neighbourhood containing no other zero. These neighbourhoods form a cover of \(K\), so a finite subcover proves \(K\) is finite.

The section defines a global relative pullback
\[
\alpha=s^*u_E\in H^r(M,M\setminus K;\mathbb Z).
\tag{N.4}
\]
Its image in absolute cohomology is \(e(E)\): the homotopy \(t\,s\) to the zero section makes their pullbacks of the absolute Thom image equal, exactly as in the proof of T.4.

Choose pairwise disjoint open coordinate neighbourhoods \(U_x\) of the finitely many points of \(K\), with each containing only its designated zero. Such choices exist by the Hausdorff property: for each unordered pair choose disjoint neighbourhoods of its two points, and intersect the finitely many neighbourhoods assigned to each point; then shrink each into an oriented chart. Excision E.2 gives
\[
H_r(M,M\setminus K)
\cong
\bigoplus_{x\in K}H_r(U_x,U_x\setminus\{x\}).
\tag{N.5}
\]
For completeness, after excision the pair is the disjoint union of those pairs. A singular simplex has image in one of these open components: any two of its points can be joined inside the simplex by a segment, whose image is a path; a path cannot meet two disjoint open components covering its image, since that would separate the interval. To see this last point from the intermediate value theorem, the indicator of one nonempty part of a partition of the interval into two nonempty open sets would be a continuous real function taking \(0\) and \(1\) but not \(1/2\). Thus the chain and relative chain groups split on their simplex bases into the displayed finite direct sum, and differential preserves each summand. Taking homology gives (N.5).

The class \([M]\) maps to \([M]_K\), by the uniqueness in O.4. Its image in the \(x\)-summand of (N.5) is \(o_x\), again by its local characterization. Restricting (N.4) to that summand gives the class in (N.1). Evaluation and the absolute-to-relative naturality of the pairing therefore give
\[
\langle e(E),[M]\rangle
=\langle\alpha,[M]_K\rangle
=\sum_{x\in K}\langle s^*u_E,o_x\rangle.
\]
This is (N.3). If \(K\) is empty, T.4 gives \(e(E)=0\), and the empty sum is zero. □

**Corollary N.3 (the signed tangent Euler number of a sphere).** For the unit sphere \(S^r\subset\mathbb R^{r+1}\), \(r\geq1\), orient its tangent spaces by the outward-normal-first convention and give its tangent bundle that same orientation. Then
\[
\langle e(TS^r),[S^r]\rangle=1+(-1)^r.
\tag{N.6}
\]
For \(S^0\) with both point orientations positive, the corresponding rank-zero pairing is \(2\).

**Proof.** The sphere is a compact smooth manifold: it is closed and bounded, and the derivative of \(x\mapsto|x|^2\) is nonzero on its level \(1\), so the opening lesson's implicit function theorem gives its local charts. Its tangent space is the kernel of \(h\mapsto2x\cdot h\). Declaring an ordered tangent basis positive when preceded by the outward vector \(x\) it is positive in \(\mathbb R^{r+1}\) gives compatible local orientations.

Fix a unit vector \(a\). The smooth field
\[
s(x)=a-(a\cdot x)x
\tag{N.7}
\]
is tangent, since its scalar product with \(x\) is zero. It vanishes precisely at \(a\) and \(-a\): at a zero \(a=(a\cdot x)x\), and taking norms forces \(|a\cdot x|=1\), hence \(x=\pm a\). Conversely both points are zeros.

For a tangent vector \(h\) at either zero, \(a\cdot h=0\), and differentiating (N.7) gives
\[
Ds_x(h)=-(a\cdot x)h.
\tag{N.8}
\]
This ambient derivative computes the derivative of the section in a local tangent frame at a zero. Indeed, writing the ambient vector as a frame matrix times its coefficient vector, the derivative of the frame matrix is multiplied by the zero coefficient and contributes nothing. Since the orientations of the tangent bundle and of the base tangent space agree, its determinant sign is \((-1)^r\) at \(a\) and \(+1\) at \(-a\). Both derivatives are invertible, so N.1 and N.2 give (N.6).

For \(r=0\), the sphere is two points. Its zero-rank tangent bundle has Euler class \(1\) by T.3 and (T.13), and its chosen positive fundamental cycle is the sum of the two points. Evaluation is \(2\). □

**Theorem N.4 (zero indices modulo two).** Let \(M\) be any compact smooth \(r\)-manifold without boundary, \(r>0\), and \(E\to M\) any smooth real rank-\(r\) vector bundle. Neither need be oriented. If a smooth section has only isolated zeros, there is a canonical mod-two fundamental class \([M]_2\), and
\[
\langle e(E;\mathbb F_2),[M]_2\rangle
=\sum_{x:\,s(x)=0}\operatorname{ind}_{x,2}(s)
\quad\text{in }\mathbb F_2.
\tag{N.9}
\]
At a nondegenerate zero the local index is \(1\).

**Proof.** The group \(H_r(M,M\setminus\{x\};\mathbb F_2)\) has a unique nonzero element, by E.5 and excision. In coordinates it is the coefficient image of \(g_r\). Lemma O.3 shows that every transition acts by a sign integrally, hence by \(1\) modulo two; no orientation restriction is needed. The translated-cube argument in O.4 gives local coherence with these coefficients. Theorem E.8, which holds for every coefficient group, supplies their unique global fundamental class \([M]_2\).

Use the mod-two Thom class of T.3. Define \(\operatorname{ind}_{x,2}(s)\) by pulling it back to the local pair and evaluating on that nonzero local generator. The zero set is finite by the same compactness argument as in N.2. Its pulled-back relative Thom class forgets to the mod-two Euler class, since scalar multiplication gives the homotopy to the zero section. The excision and finite disjoint-union argument (N.5) is a simplex-basis argument with any coefficients. It sends \([M]_2\) to the nonzero generator in each local summand. Evaluation therefore gives (N.9).

At a nondegenerate zero, any coordinate chart and any bundle frame give a local coefficient diffeomorphism by the inverse function theorem. Its action on local homology is the determinant sign by O.3, whose coefficient image is \(1\). Pulling back the fibre Thom generator therefore evaluates to \(1\). This proves the final assertion without choosing orientations. □

**Corollary N.5 (sphere class, nonzero fields and Euler characteristic).** For \(r\geq1\), evaluation on the outward oriented \([S^r]\) identifies \(H^r(S^r;\mathbb Z)\) with \(\mathbb Z\). If \(a\) denotes the class evaluating to \(1\), then
\[
e(TS^r)=(1+(-1)^r)a.
\tag{N.10}
\]
In particular \(e(TS^2)=2a\) and \(S^2\) has no continuous nowhere-zero tangent field. Every odd-dimensional sphere has an explicit smooth unit tangent field. The number in (N.6) equals the Euler characteristic computed from the sphere homology.

**Proof.** Remove one point \(x\) from \(S^r\). The stereographic coordinates in E.5 identify the complement with \(\mathbb R^r\), so it is contractible. The pair exact sequence E.1 therefore makes
\[
H_r(S^r;\mathbb Z)\longrightarrow
H_r(S^r,S^r\setminus\{x\};\mathbb Z)
\]
an isomorphism. For \(r=1\), the last step uses that the inclusion of the connected punctured sphere into the connected sphere induces an isomorphism on \(H_0\); for \(r>1\), the neighbouring positive-degree groups of the complement vanish. The fundamental class maps to the positive local generator by O.4 and hence generates \(H_r(S^r;\mathbb Z)\).

Theorem U.3 now makes evaluation an isomorphism in degree \(r\): for \(r>1\) the preceding homology group is zero by E.5, while for \(r=1\) it is \(\mathbb Z\), whose Ext group is zero by (U.3). Combine this isomorphism with N.3 to obtain (N.10). Its value \(2a\) is nonzero in the infinite cyclic group for \(S^2\). A continuous nowhere-zero tangent section would give zero Euler class by T.4, a contradiction.

For \(r=2k+1\), write the ambient \(\mathbb R^{r+1}\) as \(k+1\) ordered coordinate planes and define \(J(u,v)=(-v,u)\) in each plane. Direct calculation gives \(x\cdot Jx=0\) and \(|Jx|=|x|\). Hence \(x\mapsto Jx\) is a smooth tangent field of unit length on the sphere.

Finally define the Euler characteristic here by the alternating sum of the dimensions of rational homology, which is finite for these spaces by E.5. For \(r\geq1\) the only nonzero groups are \(\mathbb Q\) in degrees \(0,r\), so the sum is \(1+(-1)^r\). For \(S^0\), \(H_0\) has dimension two and all higher groups vanish, giving \(2\), in agreement with the positive-point convention in N.3. No Euler-characteristic theorem for other manifolds is being assumed. □

## Free construction sources

The following exact free author versions supplied construction material. The arguments used by this chapter are written out above, including the auxiliary algebra and chain identities. External references do not replace those proofs.

- Jiří Lebl, *Basic Analysis II*, [author source version 6.3](https://api.github.com/repos/jirilebl/ra/zipball/v6.3), determinant subsection of the linear-algebra review. Section 1 gives the permutation-sign, alternating-multilinear, product, transpose and invertibility arguments in full.
- Allen Hatcher, *Algebraic Topology*, free author electronic [Chapter 2](https://pi.math.cornell.edu/~hatcher/AT/ATch2.pdf) 149–150 and 152–153: singular chains, homotopy, subdivision, excision and Mayer–Vietoris.
- Hatcher, the same free author electronic [Chapter 3](https://pi.math.cornell.edu/~hatcher/AT/ATch3.pdf) 206–207 and 233–239: cochains, coefficient algebra, cup products, local orientations and compact-support gluing.
- Hatcher, free author electronic [additional Chapter 3 topics](https://pi.math.cornell.edu/~hatcher/AT/ATch3.4.pdf), printed pages 277–280: products of chains. Section 5 supplies the chain identities and the inverse homotopies.
- Hatcher, free author electronic [additional Chapter 4 topics](https://pi.math.cornell.edu/~hatcher/AT/ATch4.4.pdf), Section 4.D, printed pages 432–434 and 440–444: local-to-global constructions and the Thom isomorphism. Section 7 gives the complete finite-cover and compact-chain argument used here.
- Hatcher, [free author manuscript *Vector Bundles and K-Theory*, version 2.2](https://pi.math.cornell.edu/~hatcher/VBKT/VB.pdf), Section 3.2, printed pages 88 and 91–92: the Euler class defined from the Thom class and its elementary properties.

Original exposition: GPT-6 Astra (OpenAI), October 2026, CC0 1.0. Human source authors are credited above. No source prose, diagrams or source PDFs are reproduced.
