# Manifold duality and the Euler characteristic

DG-CHAR-07 · Differential geometry foundations

Compactly supported cohomology turns local orientation data into manifold duality. We construct that duality, including the connecting-map sign, and prove finite homology and coefficient independence for compact manifolds. Normal neighbourhoods then identify a submanifold's dual class with its normal Thom class. The final product and diagonal calculation proves that the tangent Euler number equals the Euler characteristic, integrally when oriented and modulo two in general.

Manifolds are smooth, Hausdorff, second countable and without boundary. A closed manifold means a compact manifold without boundary; a closed embedded submanifold means that its image is a closed subset of the ambient manifold. These two uses of “closed” are distinguished in each assertion. All chains are finite ordinary singular chains. The algebra assumes the usual integers and real numbers and the axiom of choice; the earlier coefficient section derives basis extension from that axiom.

The earlier programme lessons are [Local tools for bundles and transport](../../../src/local-tools-for-bundles-and-transport.md) and [Integral Thom classes and Euler indices](DG-CHAR-06.md). Numeric labels such as 0.1, 1.2, 2.1 and 3.1 refer to the opening lesson's compactness, local inverse, ODE and partition proofs. Labels K, E, U, X, O, T and N refer respectively to DG-CHAR-06's chain, exactness, coefficient, product/cap, orientation, Thom and zero-index proofs. Its L.1 proves the determinant identities. Labels B, G, J, C, F and D belong to the six sections of this chapter. Every result used below is proved here or at those exact earlier programme locators.

## 1. Compact supports and manifold duality

Let \(R\) be a commutative ring with identity. Chains have coefficients in \(R\), and cochains are \(R\)-linear functionals on these chains, equivalently integer-linear functions from integral chains to \(R\). Unless stated otherwise, \(M\) is a Hausdorff, second-countable smooth \(n\)-manifold without boundary with a chosen real orientation. The coefficients \(R=\mathbb F_2\) also permit \(M\) without a real orientation. All the chains in this chapter are ordinary singular chains. Negative-degree ordinary chain and cochain groups are zero.

For a compact set \(K\subset M\), write
\[
H_q(M\mid K;R)=H_q(M,M\setminus K;R),\qquad
H^q(M\mid K;R)=H^q(M,M\setminus K;R).
\tag{B.1}
\]
Compact subsets are closed by the elementary Hausdorff argument in DG-CHAR-06, before E.7. Its O.4 supplies integral local orientation classes and their unique compact-support extensions; take their coefficient images in \(R\). They are still uniquely characterized by their local values, because E.7 and E.8 hold with every coefficient group. Thus no injectivity of change of coefficients is being assumed. Write these extensions as
\[
\mu_K\in H_n(M\mid K;R).
\tag{B.2}
\]
With coefficients \(\mathbb F_2\), each local group has its unique nonzero generator by E.5. Coordinate changes preserve it by O.3, since both integral signs become \(1\). The translated-cube coherence proof in O.4 and E.8 therefore construct (B.2) without an orientation, just as in N.4. In either case, if \(K\subset L\), then \(\mu_L\) maps to \(\mu_K\), by uniqueness in E.7. For compact \(M\), put \([M]_R=\mu_M\).

### Directed groups and cochains with compact support

**Lemma B.1 (compact support and passage to unions).** Set
\[
C_c^q(M;R)=\bigcup_{K\subset M\ {\rm compact}}
 C^q(M,M\setminus K;R),\qquad
H_c^q(M;R)=H^q(C_c^*(M;R)).
\tag{B.3}
\]
The union consists of subcomplexes of the same cochain complex. There are natural isomorphisms
\[
H_c^q(M;R)
 \cong \underset{K\ {\rm compact}}{\operatorname{colim}}
 H^q(M\mid K;R).
\tag{B.4}
\]
An open inclusion \(j:U\hookrightarrow M\) has a natural extension map
\(j_!:H_c^q(U;R)\to H_c^q(M;R)\).
If \(M=\bigcup_{i\geq1}U_i\) is an increasing union of open sets, then
\[
\underset{i}{\operatorname{colim}}\,H_c^q(U_i;R)
 \cong H_c^q(M;R),\qquad
\underset{i}{\operatorname{colim}}\,H_q(U_i;R)
 \cong H_q(M;R).
\tag{B.5}
\]
For compact \(M\), compactly supported cohomology equals ordinary cohomology.

**Proof.** We first give the precise directed-group construction. A partially ordered set is directed if any two indices have a common upper bound. Suppose abelian groups \(G_i\) have homomorphisms \(f_{ij}:G_i\to G_j\) for \(i\leq j\), with identity and composition laws. Declare \((i,a)\) and \((j,b)\) equivalent when their images agree at some common later index. Reflexivity and symmetry are immediate. For transitivity, take a common upper bound for the two indices at which the two given equalities hold, and apply the transition maps to those equalities. Addition is performed after moving both representatives to a common index. Moving further does not change its equivalence class; moving representatives first gives the same result after passing to an upper bound of the finitely many indices involved. Associativity and commutativity follow from those of that one group. The class of zero and the class of \(-a\) give the identity and inverse. This constructs the colimit. A representative is zero exactly when it becomes zero at some later index.

A cofinal collection of indices, meaning one with a member above each original index, gives the same colimit. Every element can be moved to a member of the collection, proving surjectivity. An equality already witnessed at any index can be moved to a still later member of the collection, proving injectivity. The collection is directed with its inherited order: move a common upper bound to a member of the collection.

We will also use exactness of directed limits of compatible exact sequences. For three consecutive groups \(A_i\to B_i\to C_i\), an element of the limit of the \(B_i\)'s that maps to zero can first be moved to an index where its image in \(C_i\) is zero. Exactness at that index lifts it from \(A_i\). The opposite inclusion follows from the zero composite at every index. This proves exactness at every position, and applies to long exact sequences as well.

Compact sets are directed by union. If \(K\subset L\), a cochain vanishing on every simplex in \(M\setminus K\) also vanishes on every simplex in \(M\setminus L\). These are literal inclusions of cochain complexes, giving (B.3). A cocycle in their union is a cocycle in one of them. If it is a boundary in the union, its bounding cochain belongs to a possibly different compact-support complex; their union is a common compact support witnessing the equality. This proves (B.4). Notice the precise vanishing condition: the cochain vanishes on simplices whose entire image lies in \(M\setminus K\). No vanishing is asserted for a large simplex that meets both \(K\) and its complement.

For compact \(K\subset U\), excision E.2 applied to \(M\setminus U\) gives the canonical restriction isomorphism
\[
H^q(M\mid K;R)\longrightarrow H^q(U\mid K;R).
\tag{B.6}
\]
Indeed, \(M\setminus U\) is closed and contained in the open set \(M\setminus K\). Define extension at \(K\) by the inverse of (B.6), and then use (B.4). Restriction commutes with enlarging supports, so its inverse does too. Restriction also composes for nested open inclusions, and hence these extension maps compose. This constructs \(j_!\) on cohomology. Extending arbitrary cochains by zero has not been used as a chain map.

If \(M=\bigcup_i U_i\) increasingly, every compact set is contained in some \(U_i\): finitely many members of the cover suffice, and one contains the finitely many chosen members. Hence every class on the right of the first map in (B.5) comes from some \(U_i\), using (B.6). If a representative from \(U_i\) becomes zero on \(M\), the zero criterion in (B.4) witnesses this on a compact support \(L\subset M\) containing its original support. Choose \(U_j\) containing \(L\) and with \(j\geq i\). Inverse excision at \(L\) witnesses the same vanishing on \(U_j\). This proves injectivity. For homology, a cycle is a finite chain, so its image is compact and lies in some \(U_i\). If it bounds in \(M\), the finite bounding chain is contained in a possibly later \(U_j\). These observations prove both directions of the homology assertion. Finally, for compact \(M\), the support \(K=M\) is a final index and its cochain complex is the entire ordinary cochain complex. □

### The duality map with the right cap convention

For a cochain \(a\) of degree \(q\geq0\), define on an \(m\)-simplex
\[
R_a\sigma
 =a\bigl(\sigma[m-q,\ldots,m]\bigr)\,
       \sigma[0,\ldots,m-q]\quad (m\geq q),
\qquad R_a\sigma=0\quad(m<q).
\tag{B.7}
\]
This is the convention of DG-CHAR-06 X.6. It works for \(R\)-valued cochains and \(R\)-chains: the ordered cup expansion K.5 uses only addition and multiplication in the coefficient ring. For clarity, its boundary calculation with these coefficients is as follows. If \(m\geq q+1\), evaluate against any \(R\)-valued cochain \(b\) of degree \(m-q-1\). The ordered face formula gives \(b(R_ac)=(b\smile a)(c)\), and the cup differential rule gives
\[
\begin{aligned}
b(\partial R_ac-R_a\partial c)
 &=(db\smile a-d(b\smile a))(c)\\
 &=(-1)^{m-q}(b\smile da)(c)
 =(-1)^{m-q}b(R_{da}c).
\end{aligned}
\]
Basis cochains with value \(1\) at a selected simplex and \(0\) elsewhere distinguish \(R\)-chains. Therefore
\[
\partial R_a c-R_a\partial c=(-1)^{m-q}R_{da}c.
\tag{B.8}
\]
For \(m\leq q\), all terms have negative degree and are zero. This proves the identity with the coefficients used here, without assuming that an arbitrary \(R\)-valued cochain comes by extension of an integral one.

**Lemma B.2 (well-defined duality and naturality).** For a compact-support cocycle \(a\) vanishing on \(M\setminus K\), choose a relative cycle \(c\) representing \(\mu_K\). The formula
\[
D_M^q[a]=[R_a c]\in H_{n-q}(M;R)
\tag{B.9}
\]
defines a homomorphism \(D_M^q:H_c^q(M;R)\to H_{n-q}(M;R)\).
It is natural for open inclusions, in the form
\[
j_*D_U^q=D_M^q j_!.
\tag{B.10}
\]
For compact \(M\), and classes \(a\in H^q(M;R)\),
\(b\in H^{n-q}(M;R)\), it satisfies
\[
\langle b,D_M^q a\rangle
 =\langle b\smile a,[M]_R\rangle.
\tag{B.11}
\]

**Proof.** Since \(da=0\), (B.8) says that \(R_a\) commutes with the unshifted chain differentials. Since \(a\) vanishes on all simplices in \(M\setminus K\), its cap vanishes on such chains. Thus \(R_a\partial c=0\), and \(R_ac\) is a cycle. Replacing \(c\) by \(c+\partial h+v\), with \(v\) in \(M\setminus K\), changes \(R_ac\) by the boundary \(\partial R_a h\).

If \(q\geq1\) and \(a\) is changed by \(db\) with \(b\) vanishing on \(M\setminus K\), (B.8) applied to \(b\) gives
\[
R_{db}c=(-1)^{n-q+1}\partial R_b c,
\]
because \(R_b\partial c=0\). There are no degree-zero coboundaries from negative-degree ordinary cochains. This proves independence of both choices.

If \(K\subset L\), the class \(\mu_L\) restricts to \(\mu_K\). Representatives therefore differ by a relative boundary and a chain outside \(K\), and the preceding calculation shows that (B.9) is unchanged. Additivity follows by using a common compact support and the linearity in \(a\). Lemma B.1 now gives the asserted map on \(H_c^q\). For negative \(q\), its domain is zero; for \(q>n\), (B.7) gives zero.

For (B.10), take a class supported on a compact \(K\subset U\). The excision isomorphism on relative homology sends the class \(\mu_K\) constructed in \(U\) to the class constructed in \(M\). Their local values coincide; E.7 proves the equality. Consequently a representative \(c\) may be chosen in \(U\). A relative cocycle on \(M\) representing the inverse-excision extension restricts on \(U\) to the prescribed class. Replacing its restriction by the originally chosen cocycle changes the cap by the boundary already calculated. Since face maps commute with inclusion, (B.10) follows on this representative. Finally (B.11) is the direct face identity \(b(R_ac)=(b\smile a)(c)\), evaluated on a representative of \([M]_R\). The order is \(b\smile a\). □

### Gluing, including the connecting-map sign

**Lemma B.3 (compact-support gluing).** If \(M=U\cup V\) with \(U,V\) open and \(W=U\cap V\), compactly supported cohomology has an exact sequence
\[
\cdots\longrightarrow H_c^q(W;R)
 \xrightarrow{(j_!,j_!)}
 H_c^q(U;R)\oplus H_c^q(V;R)
 \xrightarrow{\,j_!-j_!\,}
 H_c^q(M;R)
 \xrightarrow{\delta} H_c^{q+1}(W;R)
 \longrightarrow\cdots.
\tag{B.12}
\]
Use the homology Mayer–Vietoris sequence E.3 with maps
\(c\mapsto(c,-c)\), addition, and connecting map
\([c_U+c_V]\mapsto[\partial c_U]\).
The duality maps commute with the nonconnecting arrows if their signs on the middle pair are \(D_U,-D_V\). The connecting maps satisfy
\[
D_W^{q+1}\delta
 =(-1)^{n-q}\,\partial D_M^q.
\tag{B.13}
\]
Consequently, if the duality maps are isomorphisms in all degrees on \(U,V,W\), they are isomorphisms in all degrees on \(M\).

**Proof.** Choose compact sets \(K\subset U\), \(L\subset V\), and write
\[
A=M\setminus K,\quad B=M\setminus L,\quad
F_*=C_*(M;\mathbb Z),\quad
Q^*=\operatorname{Hom}_{\mathbb Z}
 \bigl(F_*/(C_*(A;\mathbb Z)+C_*(B;\mathbb Z)),R\bigr).
\]
The letter \(B\) in this proof denotes the displayed open complement; numbered labels continue to denote the statements of this chapter. There is a short exact sequence of cochain complexes
\[
0\longrightarrow Q^*
 \xrightarrow{\psi\mapsto(\psi,\psi)}
 C^*(M,A;R)\oplus C^*(M,B;R)
 \xrightarrow{(a,b)\mapsto a-b}
 C^*(M,A\cap B;R)
 \longrightarrow0.
\tag{B.14}
\]
The kernel assertion is immediate: \(a=b\) must vanish on both simplex subgroups. To verify surjectivity, given \(\phi\) in the last complex, define on every simplex \(\sigma\)
\[
a(\sigma)=
\begin{cases}
0,&\operatorname{im}\sigma\subset A,\\
\phi(\sigma),&\operatorname{im}\sigma\not\subset A,
\end{cases}
\qquad b=a-\phi.
\]
Then \(a\) vanishes on \(A\). If \(\sigma\) lies in \(B\), either it also lies in \(A\), when \(\phi(\sigma)=0\), or \(a(\sigma)=\phi(\sigma)\). In both cases \(b(\sigma)=0\). These assignments are extended linearly on the simplex basis and prove degreewise surjectivity. No compatibility of this splitting with the differential is needed.

The natural quotient map
\[
F_*/(C_*(A)+C_*(B))
 \longrightarrow F_*/C_*(A\cup B)
\]
is a chain homotopy equivalence by the explicit maps and homotopies in E.4. Dualizing those identities gives an isomorphism
\[
H^q(M\mid K\cap L;R)\longrightarrow H^q(Q^*).
\tag{B.15}
\]
In particular this isomorphism is induced by the inclusion of actual relative cochains into \(Q^*\). Apply the exact-sequence construction E.1 to (B.14), and use (B.15). The three cohomology terms now have supports \(K\cap L\), \(K,L\), and \(K\cup L\), respectively. Excision (B.6) identifies the first terms with the corresponding groups in \(W,U,V\).

Let \((K,L)\) increase in the directed set of such compact pairs. This gives compatible exact sequences, since every map before taking cohomology is a restriction or inclusion and the connecting construction E.1 is natural. The supports \(K\cup L\) are cofinal among compact supports of \(M\). Indeed, cover a given compact set by finitely many coordinate balls whose closed balls lie in \(U\) or in \(V\), using the smaller chart balls of the opening lesson 3.B. Take \(K\) to be the union of the closed balls assigned to \(U\), and \(L\) the union of those assigned to \(V\). The supports \(K\cap L\) are cofinal among compact supports of \(W\): for any compact \(C\subset W\), choose \(K=L=C\). On the separate \(U,V\) terms, either compact can be enlarged independently of the other. Formula (B.4), excision, and the exactness of directed limits proved in B.1 yield (B.12).

Here is an explicit check that indexing by pairs introduces no extra identifications or missing ones. The displayed cofinal choices represent every compact-support class at some pair. If a pair representative vanishes after enlarging its union support to a compact \(N\subset M\), choose a pair whose union contains \(N\) and then enlarge it by the original pair, component by component. This witnesses the vanishing in the pair-indexed system. For an intersection support, enlarge both members of the original pair by the compact support \(N\subset W\) witnessing the vanishing. Its intersection then contains \(N\). For each separate term, enlarge that member by its witnessing compact support. These are exactly the zero criteria in B.1; applying them to differences also treats equality of two representatives. Thus all the limit identifications just used are isomorphisms.

The nonconnecting squares now follow from (B.10). On an intersection class, the diagonal \((j_!,j_!)\) followed by \((D_U,-D_V)\) equals the homology map \((j_*,-j_*)\) applied to \(D_W\). On a pair of classes, addition of the two signed duality images equals \(D_M\) of their difference of extensions.

We compute the remaining square. For \(0\leq q<n\), represent a class in \(H^q(M\mid K\cup L;R)\) by a cocycle \(\phi\), and lift it as \(\phi=a-b\) in (B.14). Then
\[
\psi=da=db\in Q^{q+1}
\tag{B.16}
\]
represents its connecting class. Choose a relative cycle \(\alpha\) representing \(\mu_{K\cup L}\). The three open sets
\[
U\setminus L,\qquad W,\qquad V\setminus K
\tag{B.17}
\]
cover \(M\). To check this, a point in both \(U,V\) lies in \(W\); a point in \(U\setminus V\) is outside \(L\); and a point in \(V\setminus U\) is outside \(K\). Applying K.3 to this cover, while retaining its support-preserving homotopy, allows us to replace \(\alpha\) by an equivalent relative cycle small for this cover. It can be written
\[
\alpha=x+y+z
\tag{B.18}
\]
with \(x\) in \(U\setminus L\), \(y\) in \(W\), and \(z\) in \(V\setminus K\). Assign a simplex lying in several members to any one of them. This gives finite chains with the indicated supports, and \(\partial\alpha\) is still in \(M\setminus(K\cup L)=A\cap B\).

The chain \(x+y\) represents \(\mu_K\), since the omitted chain \(z\) lies in \(A\). The chain \(y\) represents \(\mu_{K\cap L}\), since \(x\) and \(z\) lie outside \(K\cap L\). In addition, the stronger chain statement
\[
\partial y=\partial\alpha-\partial x-\partial z
 \in C_*(A;R)+C_*(B;R)
\tag{B.19}
\]
holds. This statement is needed because \(\psi\) is a cocycle in \(Q^*\), rather than necessarily an actual cochain vanishing on every simplex in \(A\cup B\).

We justify using \(R_\psi y\) for the duality image of the connecting class. By (B.15), there is a relative cocycle \(\chi\) vanishing on \(C_*(A\cup B)\), and a cochain \(\eta\in Q^q\), with \(\psi-\chi=d\eta\). By (B.19), \(R_\eta\partial y=0\). Hence (B.8) shows
\[
R_\psi y-R_\chi y=(-1)^{n-q}\partial R_\eta y.
\]
All these chains lie in \(W\), since they are faces of \(y\). The cap with \(\chi\) is the duality image of the class represented by \(\chi\), using \(y\) as its relative fundamental cycle. Thus
\[
D_W^{q+1}\delta[\phi]=[R_\psi y].
\tag{B.20}
\]
This also shows directly that the latter chain is a cycle; alternatively use \(d\psi=0\) and (B.19) in (B.8).

The cycle representing \(D_M^q[\phi]\) is \(R_\phi\alpha\). Split it into its \(U\) part \(R_\phi x\) and its \(V\) part \(R_\phi(y+z)\). Its homology connecting image is
\[
[\partial R_\phi x].
\tag{B.21}
\]
This boundary is a chain in \(W\): it is simultaneously a chain in \(U\) and the negative of the boundary of the indicated \(V\) part, and intersections of the corresponding free simplex subgroups are exactly the simplex subgroup of \(W\).

Since \(x\) and its faces lie outside \(L\), \(b\) vanishes on them. Since \(da=db=\psi\) vanishes on \(B=M\setminus L\), all the following identities hold on the displayed chains. As \(d\phi=0\), (B.8) gives
\[
\partial R_\phi x=R_\phi\partial x=R_a\partial x.
\tag{B.22}
\]
Furthermore \(\partial(x+y)=\partial\alpha-\partial z\) lies in \(A\), so
\[
R_a\partial y=-R_a\partial x.
\tag{B.23}
\]
Applying (B.8) to \(a\) and the degree-\(n\) chain \(y\) now gives, modulo boundaries in \(W\),
\[
\begin{aligned}
R_\psi y
 &=(-1)^{n-q}\bigl(\partial R_a y-R_a\partial y\bigr)\\
 &\equiv(-1)^{n-q+1}R_a\partial y\\
 &=(-1)^{n-q}\partial R_\phi x.
\end{aligned}
\tag{B.24}
\]
Together, (B.20)–(B.24) prove (B.13). For \(q=n\) both sides have target \(H_{-1}=0\). For \(q>n\) this is also so, and for \(q<0\) the domain cohomology group is zero. Thus the identity holds in every degree.

Finally compare five consecutive positions of (B.12), beginning with \(H_c^q(W)\), to the homology exact sequence in degrees \(n-q,n-q-1\). Set \(\varepsilon=(-1)^{n-q}\). Use the vertical maps
\[
D_W^q,\quad (D_U^q,-D_V^q),\quad D_M^q,\quad
\varepsilon D_W^{q+1},\quad
\varepsilon(D_U^{q+1},-D_V^{q+1}).
\tag{B.25}
\]
Every square commutes by the preceding calculations, including the connecting square since \(\varepsilon^2=1\). If duality is known on \(U,V,W\), the first, second, fourth and fifth vertical maps are isomorphisms. The full five-position exact-sequence chase proved immediately before DG-CHAR-06 T.2 makes the third map an isomorphism. This proves the gluing assertion. □

### The local computation and the manifold theorem

**Lemma B.4 (convex coordinate domains).** Give a nonempty convex open subset \(V\subset\mathbb R^n\) its coordinate orientation. For every \(q\), the map
\[
D_V^q:H_c^q(V;R)\longrightarrow H_{n-q}(V;R)
\tag{B.26}
\]
is an isomorphism. The same assertion uses the unique local generators with coefficients \(\mathbb F_2\).

**Proof.** Every compact \(K\subset V\) is contained in a nonempty compact convex set \(L\subset V\). For nonempty \(K\), cover it by the interiors of finitely many closed Euclidean balls \(C_1,\ldots,C_s\) contained in \(V\). Such balls exist at each point because \(V\) is open, and compactness gives a finite subcover. Define
\[
L=\left\{\sum_{i=1}^s t_i x_i:
 t_i\geq0,\ \sum_i t_i=1,\ x_i\in C_i\right\}.
\tag{B.27}
\]
This is a continuous image of the compact product
\(\Delta^{s-1}\times C_1\times\cdots\times C_s\), so it is compact by the elementary finite-product compactness in the opening lesson 0.1. It contains every \(C_i\), by choosing \(t_i=1\). It is contained in \(V\), by convexity of \(V\). It is convex: for two displayed sums and a number \(t\in[0,1]\), their convex combination has weights \(t t_i+(1-t)t_i'\). For a positive such weight, combine \(x_i,x_i'\) with their normalized nonnegative weights inside the convex set \(C_i\); for zero weight, choose any point of \(C_i\). This gives another expression of the form (B.27). For \(K=\varnothing\), choose any point of \(V\) as \(L\). This proof also works for \(n=0\), when \(V\) is a point.

Consequently nonempty compact convex supports in \(V\) are cofinal among all compact supports. They form a directed family: apply the same construction to the union of any two of them. If \(L\) is in that family and \(x\in L\), excision E.2 and E.6 give
\[
H_i(V\mid L;\mathbb Z)
 \cong H_i(\mathbb R^n\mid L;\mathbb Z)
 \cong H_i(\mathbb R^n\mid\{x\};\mathbb Z).
\tag{B.28}
\]
For excision the complement of \(V\) is closed and lies in the open complement of \(L\). The last group is \(\mathbb Z\) for \(i=n\) and zero otherwise, by E.5. In degree \(n\), the integral compact-support fundamental class maps to the positive local generator by O.4, so it is a generator of the first group in (B.28).

Apply U.3 to the integral relative chain complex, which is free on those simplices not contained in \(V\setminus L\). All its homology groups are free or zero by (B.28), so its Ext terms vanish, as proved before U.3. Therefore
\[
H^q(V\mid L;R)=0\quad(q\ne n),\qquad
H^n(V\mid L;R)\xrightarrow{\ a\mapsto\langle a,\mu_L\rangle\ }R
\ \text{is an isomorphism}.
\tag{B.29}
\]
Here evaluation can equivalently be made on the integral fundamental generator or on its coefficient image. If \(L\subset L'\), the transition map in cohomology preserves this evaluation, because the homology map sends \(\mu_{L'}\) to \(\mu_L\). Cofinality and (B.4) show that \(H_c^q(V;R)\) is \(R\) in degree \(n\), with the same evaluation identification, and zero otherwise.

The straight-line homotopy from \(V\) to a chosen point stays in \(V\). The prism proof K.1 and the point calculation after E.1 show that \(H_i(V;R)\) is \(R\) in degree zero and zero in every other degree. Its degree-zero identification is the augmentation summing coefficients. For \(q=n\), (B.7) on an \(n\)-simplex gives
\[
\operatorname{aug}(R_a c)=a(c).
\tag{B.30}
\]
Thus (B.26) is the identity of \(R\) under the two evaluation and augmentation identifications. In all other degrees both groups are zero. This proves the assertion, including dimension zero. Reducing the positive integral classes modulo two is exactly the indicated local-generator convention, so the same calculation proves that case. □

**Theorem B.5 (Poincaré duality).** For \(M\) and coefficients as specified above, right cap with the compatible fundamental classes gives isomorphisms in every integer degree:
\[
D_M^q:H_c^q(M;R)\xrightarrow{\ \cong\ }H_{n-q}(M;R).
\tag{B.31}
\]
If \(M\) is compact, this is right cap with its ordinary fundamental class:
\[
H^q(M;R)\xrightarrow{\ \cong\ }H_{n-q}(M;R).
\tag{B.32}
\]

**Proof.** The empty manifold has zero groups, so the assertion holds. First consider open subsets of \(\mathbb R^n\) with the coordinate orientation. Any finite union of convex open sets satisfies duality, by induction on the number of sets. The empty union is the base case, and a nonempty single convex set is B.4. For an \(s\)-set union, separate its last member \(V\) from the union \(U\) of the preceding ones. The intersection \(U\cap V\) is a union of at most \(s-1\) convex open intersections, each possibly empty. Duality holds on \(U\), \(V\), and \(U\cap V\) by the induction hypothesis. Lemma B.3 proves it on their union.

Every open subset \(\Omega\subset\mathbb R^n\) has a countable cover by Euclidean open balls contained in \(\Omega\). This is the coordinate-ball construction in the opening lesson 3.B applied to the identity coordinate chart on \(\Omega\); its countability proof is included there. Write \(\Omega\) as the increasing union of the first finitely many balls. Each finite union has duality by the preceding paragraph. Naturality (B.10) makes these isomorphisms a compatible system. Passing to limits in (B.5) gives an isomorphism on \(\Omega\). Explicitly the compatible inverses also commute with transition maps, by applying inverses to the commuting equations, and induce an inverse on the directed limits. Thus no extra preservation-of-isomorphisms theorem is required.

These conclusions transfer through an orientation-preserving coordinate diffeomorphism. Indeed it maps the chosen local generator to the chosen local generator by O.3, and therefore maps all compact fundamental classes to the corresponding ones by E.7. Pullback of cochains commutes with taking the ordered faces in (B.7). The cap formula on a representative gives the corresponding equality of duality maps. The diffeomorphism and its inverse preserve compact supports, so the induced maps on both sides are isomorphisms. With coefficients \(\mathbb F_2\), every coordinate diffeomorphism preserves the chosen local generators, and the same argument applies.

For \(n>0\), choose a countable cover of \(M\) by coordinate balls, using opening lesson 3.B. Use oriented charts in the oriented case; a chart can be made orientation preserving by reversing its first coordinate when necessary. Each finite union of these balls satisfies duality, again by induction. If \(V\) is the last chart ball and \(U\) the preceding union, \(U\cap V\) is an open subset of a single coordinate chart. Duality on it has already been proved for arbitrary Euclidean open subsets and transferred by the chart. The other two opens satisfy duality by induction and B.4, so B.3 proves duality on the finite union. Finally use (B.5), (B.10), and the compatible inverses to pass to the countable increasing union \(M\).

For \(n=0\), every point is an open coordinate chart, so \(M\) is discrete. A compact subset is finite, since its cover by singleton opens has a finite subcover. Conversely every finite subset is compact. A simplex has connected domain, so its image in a discrete space is a single point, as established in E.5. Chains are therefore direct sums of point complexes, and compact-support cochains are direct sums of point cochain complexes. The point calculation after E.1 makes both homology and compactly supported cohomology direct sums of copies of \(R\) in degree zero and zero in every other degree. The duality map multiplies the summand at a point by its chosen orientation sign, or by \(1\) with coefficients \(\mathbb F_2\). These are invertible multipliers, so it is an isomorphism. This treats any chosen signs on zero-dimensional components explicitly.

We have proved (B.31) in all cases. For compact \(M\), B.1 identifies compactly supported and ordinary cohomology, and B.2 identifies the map with cap by \([M]_R\), proving (B.32). □

### Finiteness and the field pairing for compact manifolds

**Corollary B.6 (finiteness and perfect field pairings).** Suppose \(M\) is compact and oriented. Every \(H_i(M;\mathbb Z)\) is a finitely generated abelian group, and it is zero for \(i>n\). Over any field \(k\), every \(H_i(M;k)\) and \(H^i(M;k)\) is finite dimensional and zero outside degrees \(0,\ldots,n\). For every \(q\), the pairing
\[
H^{n-q}(M;k)\times H^q(M;k)\longrightarrow k,\qquad
(b,a)\longmapsto\langle b\smile a,[M]_k\rangle
\tag{B.33}
\]
identifies either space with the linear dual of the other. The field assertions also hold for a compact manifold without a chosen orientation when \(k=\mathbb F_2\).

**Proof.** Choose a finite singular cycle \(c\) representing the integral fundamental class. For fixed \(q\) with \(0\leq q\leq n\), every chain \(R_a c\) is a linear combination of the finitely many front \((n-q)\)-faces of the simplices occurring in \(c\). Let \(F\) be the free abelian group on the distinct such faces, a subgroup of the corresponding singular chain group. Its cycle subgroup \(F\cap\ker\partial\) is free with a finite basis: the proof U.1 applied to the finite ordered basis of \(F\) chooses at most one new basis element at each stage, and there are only finitely many stages. Duality B.5 says that every class in \(H_{n-q}(M;\mathbb Z)\) is represented by some \(R_a c\). The homomorphism from that finitely generated cycle subgroup onto homology is therefore surjective. Images of its finite generators generate homology. If \(i>n\), apply B.5 to \(q=n-i<0\); the cohomology group is zero. This proves the integral assertion without a triangulation or a finite cell decomposition.

For field coefficients use a finite representative of \([M]_k\), using the unoriented mod-two class where applicable. Every cap again lies in a finite span \(F\) of front faces. A subspace of the span of \(N\) independent coordinate vectors has a basis of at most \(N\) elements: if every vector has zero first coordinate, remove that coordinate and induct on \(N\); otherwise choose a vector with nonzero first coordinate, subtract its suitable multiple from every vector to kill that coordinate, and apply induction to the resulting subspace in the remaining \(N-1\) coordinates. The chosen vector and the inductive basis are independent, since the chosen vector has nonzero first coordinate, and span by the subtraction operation. This proves the stated bound, beginning with \(N=0\). Hence the cycle subspace of \(F\), and its homology quotient, are finite dimensional. Duality gives vanishing above degree \(n\) and also identifies cohomology with finite-dimensional homology in complementary degrees.

For completeness of the pairing claim, the field evaluation statement proved after U.3 gives
\[
H^{n-q}(M;k)\cong
\operatorname{Hom}_k(H_{n-q}(M;k),k).
\tag{B.34}
\]
Let \(h_1,\ldots,h_s\) be a basis of this finite-dimensional homology group. Let \(a_i\) be its preimages under \(D_M^q\), and let \(b_i\) be the cohomology classes corresponding under (B.34) to the dual coordinate functionals. Then B.2 gives
\[
\langle b_i\smile a_j,[M]_k\rangle=\delta_{ij}.
\]
The \(a_i\)'s and \(b_i\)'s are bases of their respective spaces, since both maps used to construct them are isomorphisms. This matrix calculation proves that (B.33) identifies either space with the full linear dual of the other. When the groups are zero the assertion means the unique isomorphism between zero spaces. If the order of the cup factors is reversed, X.5 supplies the single factor \((-1)^{q(n-q)}\), an invertible scalar, so the reversed pairing is perfect too. This proves all the field assertions. □

The integral finite-generation assertion here uses an integral orientation. G.3 proves finite integral homology without that assumption, C.3 proves coefficient independence, J.3 constructs general tubes, and D.3–D.4 prove the diagonal and tangent Euler-number formulas.

## 2. Euclidean embeddings, normal neighbourhoods and finite homology

### A finite coordinate embedding

**Lemma G.1 (compact Euclidean embedding).** A compact smooth \(m\)-manifold \(M\) admits a smooth embedding in \(\mathbb R^N\) for some finite \(N\).

**Proof.** The empty manifold has its unique embedding in any Euclidean space, so suppose \(M\ne\varnothing\). Choose finitely many coordinate charts
\(\phi_i:U_i\to\mathbb R^m\), \(1\leq i\leq k\), covering \(M\).
The partition construction of the opening lesson 3.1 gives smooth functions
\(\rho_i\geq0\) with
\[
\sum_{i=1}^k\rho_i=1,\qquad
\operatorname{supp}\rho_i\subset U_i.
\tag{G.1}
\]
If the construction first gives a locally finite refinement, it has only finitely many nonempty supports on compact \(M\): each point has a neighbourhood meeting finitely many supports, and a finite collection of those neighbourhoods covers \(M\). Add the refinement functions assigned to each \(U_i\). A finite union of their closed supports is still contained in \(U_i\), so this gives (G.1).

Define \(F_i:M\to\mathbb R^m\) by \(F_i=\rho_i\phi_i\) on \(U_i\) and by zero outside \(U_i\). This is smooth. At a point outside \(U_i\), the closed set \(\operatorname{supp}\rho_i\) does not contain the point, so a neighbourhood misses that support and \(F_i\) is identically zero there. Put
\[
F=(F_1,\ldots,F_k,\rho_1,\ldots,\rho_k):
M\longrightarrow\mathbb R^{k(m+1)}.
\tag{G.2}
\]
If \(F(x)=F(y)\), choose \(i\) with \(\rho_i(x)>0\), which exists by (G.1). The last coordinate blocks give \(\rho_i(y)=\rho_i(x)>0\), so \(x,y\in U_i\). The first blocks then imply \(\phi_i(x)=\phi_i(y)\), hence \(x=y\). Thus \(F\) is injective.

If \(v\in T_xM\) and \(dF_xv=0\), its last blocks give \(d\rho_i(v)=0\) for every \(i\). Choose an \(i\) with \(\rho_i(x)>0\). The derivative of its first block is
\[
d(F_i)_xv=d\rho_i(v)\phi_i(x)+\rho_i(x)d\phi_i(v)
          =\rho_i(x)d\phi_i(v).
\]
It is zero only when \(v=0\), since \(d\phi_i\) is invertible. Hence \(F\) is an immersion. The same argument applies for \(m=0\), where the tangent space is zero.

Finally \(F\) is a homeomorphism onto its image. A closed subset of compact \(M\) is compact, its image under \(F\) is compact, and compact subsets of a Hausdorff space are closed, all by opening lesson 0.1. Thus \(F\), as a continuous bijection onto its image, has a continuous inverse. The constant-rank theorem of opening lesson 1.4 gives a graph chart for the immersion near each point. The homeomorphism property lets us restrict to a neighbourhood open in the image that is contained in this graph chart; such a neighbourhood is the intersection of the image with an ambient open set. There are therefore no additional local branches. These are precisely submanifold charts for the image, proving that \(F\) is a smooth embedding. □

### A tube with a positive variable radius

Let \(Y\subset\mathbb R^N\) be a smooth embedded \(m\)-manifold. Define its Euclidean normal bundle as a set by
\[
\nu Y=\{(y,v)\in Y\times\mathbb R^N:
                 v\perp T_yY\},\qquad \pi(y,v)=y.
\tag{G.3}
\]
The following proof includes its smooth bundle structure.

**Theorem G.2 (Euclidean normal tube).** The set \(\nu Y\) is a smooth vector bundle of rank \(c=N-m\). There is a smooth positive function \(\delta:Y\to(0,\infty)\) such that
\[
E(y,v)=y+v
\tag{G.4}
\]
is a diffeomorphism from
\[
V_\delta=\{(y,v)\in\nu Y:\|v\|<\delta(y)\}
\tag{G.5}
\]
onto an open neighbourhood \(U\) of \(Y\) in \(\mathbb R^N\).
There is also a diffeomorphism from the whole bundle \(\nu Y\) onto \(U\) fixing its zero section and inducing the identity on the normal quotient there. The neighbourhood \(U\) admits a smooth retraction onto \(Y\), and a deformation retraction along the normal fibres. No compactness or closedness assumption on \(Y\) is needed.

**Proof.** In a local parametrization \(f:O\subset\mathbb R^m\to Y\), let \(T(y)\) be the \(N\)-by-\(m\) matrix of its tangent coordinate vectors. Its columns are independent. The Gram matrix \(T^{\mathsf T}T\) is invertible, since
\[
a^{\mathsf T}T^{\mathsf T}Ta=\|Ta\|^2
\]
is positive for \(a\ne0\). Injectivity and invertibility for a square matrix follow from the finite basis argument in opening lesson 0.2 or the determinant lemma DG-CHAR-06 L.1. The inverse depends smoothly on \(y\): apply the parameter implicit theorem, opening lesson 1.3, to each system
\((T^{\mathsf T}T)a=e_j\); its derivative in \(a\) is the invertible Gram matrix, and the locally supplied solution is the unique inverse column. The local smooth inverses therefore agree on overlaps.

The matrix
\[
P_y=T(y)(T(y)^{\mathsf T}T(y))^{-1}T(y)^{\mathsf T}
\tag{G.6}
\]
is smooth, symmetric, and satisfies \(P_y^2=P_y\). It is the identity on the tangent columns, and its kernel consists exactly of vectors orthogonal to all those columns. Thus
\(\mathbb R^N=T_yY\oplus\ker P_y\), and \(\ker P_y\) has dimension \(c\).
Choose a basis \(w_1,\ldots,w_c\) of this kernel at a fixed point \(y_0\), and set \(b_j(y)=(I-P_y)w_j\). At \(y_0\) these vectors are independent. Their Gram determinant is nonzero there and stays nonzero nearby, by continuity of the determinant polynomial L.1. They therefore form a basis of \(\ker P_y\) on a smaller chart. If \(B(y)\) is their column matrix, the coefficients of a normal vector \(v\) are
\[
(B(y)^{\mathsf T}B(y))^{-1}B(y)^{\mathsf T}v,
\]
which are smooth by the same implicit argument.

Consequently \((u,t)\mapsto(f(u),\sum_jt_jb_j(f(u)))\) and this coefficient formula give mutually inverse local trivializations of (G.3). Their transition functions are smooth and linear in \(t\). These charts agree with the subspace topology in \(Y\times\mathbb R^N\); the displayed inverse is continuous in that topology. Their derivatives are injective: the base component first detects the \(u\)-direction, and the independent \(b_j\)'s then detect the fibre direction. The constant-rank theorem as in G.1 gives the corresponding embedded smooth structure. This proves the bundle assertion. For \(c=0\), use the empty frame; the assertions reduce to the zero bundle.

At \((y,0)\), these charts identify the tangent space of the bundle with
\(T_yY\oplus\nu_yY\), and
\[
dE_{(y,0)}(u,v)=u+v.
\tag{G.7}
\]
This is a linear isomorphism onto \(\mathbb R^N\). By the inverse function theorem, opening lesson 1.2, \(E\) is a diffeomorphism on a neighbourhood of \((y,0)\). For sufficiently small \(s>0\), that neighbourhood contains
\[
W_s(y)=\{(z,w)\in\nu Y:\|z-y\|<s,\ \|w\|<s\}.
\tag{G.8}
\]
This follows directly from the subspace topology near \((y,0)\) in \(\mathbb R^N\times\mathbb R^N\). Restriction to \(W_s(y)\) is a diffeomorphism onto an open set.

Define
\[
r(y)=\sup\{s\in(0,1]:
 E|_{W_s(y)}\text{ is a diffeomorphism onto an open set}\}.
\tag{G.9}
\]
It is positive and at most \(1\). The set in (G.9) is downward closed. Hence every \(s<r(y)\) has the required property: choose a member strictly greater than \(s\) and restrict its diffeomorphism to \(W_s(y)\).

We verify continuity without assuming that the supremum itself belongs to that set. Write \(d=\|y-y'\|\). If \(d<r(y)\) and \(0<s<r(y)-d\), then
\[
W_s(y')\subset W_{s+d}(y),
\]
where \(s+d<r(y)\). The triangle inequality proves this inclusion for the base points, and the fibre bound is smaller as well. Restriction of the diffeomorphism on the right proves that \(s\) is allowed in (G.9) for \(y'\). Taking suprema gives \(r(y')\geq r(y)-d\). If \(d\geq r(y)\), that same lower bound is automatic since \(r(y')>0\). Interchanging \(y,y'\) yields
\[
|r(y)-r(y')|\leq\|y-y'\|.
\tag{G.10}
\]
In particular \(r\) is continuous.

Let \(V=\{(y,v):\|v\|<r(y)/2\}\). The map \(E\) is a local diffeomorphism on \(V\), since any \((y,v)\in V\) lies in \(W_s(y)\) for some \(s<r(y)\). It is injective on \(V\). To prove this, suppose
\(y+v=y'+v'\), and interchange the two pairs if necessary to have \(r(y')\leq r(y)\). Then
\[
\|y-y'\|=\|v'-v\|
 \leq\|v\|+\|v'\|
 <\tfrac12r(y)+\tfrac12r(y')\leq r(y).
\tag{G.11}
\]
Both vector lengths are also strictly less than \(r(y)\). Choose \(s<r(y)\) larger than these three lengths. Then both pairs belong to \(W_s(y)\), where \(E\) is injective, so they are equal. An injective local diffeomorphism maps open sets to open sets, since each point has a local diffeomorphic chart. Its local smooth inverses agree on overlaps by injectivity. Therefore \(E\) is a diffeomorphism from \(V\) onto an open neighbourhood of \(Y\).

To obtain a smooth radius, cover \(Y\) by open sets \(A_y\) on which
\(r(z)>r(y)/2\). Choose a locally finite smooth partition \((\lambda_i)\) subordinate to a refinement, with each support in some \(A_{y_i}\), using opening lesson 3.1. Define
\[
\delta(z)=\sum_i\lambda_i(z)\frac{r(y_i)}8.
\tag{G.12}
\]
Local finiteness makes this a smooth function. It is positive since the weights sum to one and each constant is positive. If \(\lambda_i(z)>0\), then \(r(y_i)<2r(z)\), so
\(0<\delta(z)<r(z)/4\). Thus \(V_\delta\) is an open subset of \(V\), and (G.4) restricts to a diffeomorphism onto the open neighbourhood \(U=E(V_\delta)\).

There is a diffeomorphism from the whole bundle to \(V_\delta\) given by
\[
\Psi(y,v)=\left(y,\frac{v}{\sqrt{1+\|v\|^2/\delta(y)^2}}\right).
\tag{G.13}
\]
Its image has vector length strictly less than \(\delta(y)\). Its inverse on \(V_\delta\) is
\[
(y,w)\longmapsto
\left(y,\frac{w}{\sqrt{1-\|w\|^2/\delta(y)^2}}\right).
\tag{G.14}
\]
Substitution verifies both compositions. The square root on \((0,\infty)\) exists uniquely by the intermediate value theorem applied to \(t^2\) on \(t>0\), and is smooth by the inverse function theorem since its derivative there is \(2t\ne0\); these are opening lessons 0.0 and 1.2. The positive square roots and denominators therefore make both maps smooth, including at zero. On a fibre their derivative at zero is the identity; on the zero section they fix the base. Thus \(E\Psi\) is the claimed whole-bundle diffeomorphism, with normal quotient derivative the identity by (G.7).

Finally the map \(\pi E^{-1}:U\to Y\) is a smooth retraction. The maps
\[
H_t(E(y,v))=E(y,(1-t)v),\qquad 0\leq t\leq1,
\tag{G.15}
\]
stay inside \(U\) because each radius is fixed on its fibre. They start at the identity, end at that retraction followed by inclusion, and fix \(Y\) pointwise. This proves the deformation assertion. □

### Finite homology without an orientability assumption

We use the following elementary consequences of DG-CHAR-06 U.1. A subgroup \(J\) of a finitely generated abelian group \(A\) is finitely generated: choose a surjection \(\mathbb Z^s\to A\), take the inverse image of \(J\), and apply U.1 with the finite ordered basis of \(\mathbb Z^s\). That proof chooses at most one new generator per basis position, so the inverse image is finitely generated. Its images generate \(J\). A quotient is generated by the images of a finite generating family. Finally, in an exact sequence \(0\to A\to B\to C\to0\) with \(A,C\) finitely generated, choose lifts in \(B\) of generators of \(C\) and add generators from \(A\). For any \(b\in B\), subtract a linear combination of the lifts with the same image in \(C\); the remainder lies in the image of \(A\). Hence that combined finite family generates \(B\).

**Theorem G.3 (finite integral homology of compact manifolds).** For any compact smooth manifold \(M\), including an unoriented one, all \(H_i(M;\mathbb Z)\) are finitely generated, and they vanish for all sufficiently large \(i\).

**Proof.** Embed \(M\) as \(Y\subset\mathbb R^N\) by G.1, and choose an open tubular neighbourhood \(U\) and retraction \(p:U\to Y\) by G.2. The empty case has zero groups and requires no choices. Cover nonempty compact \(Y\) by finitely many Euclidean open balls \(B_1,\ldots,B_s\) contained in \(U\), and set
\(\Omega=\bigcup_iB_i\). Such a cover is obtained by choosing an ambient ball inside \(U\) around each point and taking a finite subcover of \(Y\). Then \(Y\subset\Omega\subset U\), and \(p|_\Omega:\Omega\to Y\) is a retraction.

A union of \(s\) convex open subsets of a Euclidean space has finitely generated integral homology in every degree and has zero homology in degrees greater than \(s-1\). Here and in the induction remove empty members, or regard the empty union as having all groups zero. A nonempty single convex open set contracts along line segments, so its homology is \(\mathbb Z\) in degree zero and zero otherwise, by K.1 and the point computation after E.1. Suppose the assertion is known for fewer than \(s\) sets. Separate the final convex set \(B\) from the preceding union \(A\). Their intersection is a union of at most \(s-1\) convex opens, namely the intersections of \(B\) with the preceding members. By induction both \(A\) and \(A\cap B\) have finitely generated homology. The exact segment of E.3
\[
H_i(A;\mathbb Z)\oplus H_i(B;\mathbb Z)
\longrightarrow H_i(A\cup B;\mathbb Z)
\longrightarrow H_{i-1}(A\cap B;\mathbb Z)
\tag{G.16}
\]
makes its middle group fit into a short exact sequence whose kernel is an image of the first group and whose quotient is a subgroup of the last group. More explicitly, the kernel of the second arrow is the image of the first, and the quotient by this kernel is the image of the second. The elementary subgroup, quotient and extension facts just proved give finite generation. If \(i>s-1\), the first group is zero by induction and the convex calculation, and the last group is zero because \(i-1>s-2\). Exactness gives zero for the middle group. This proves the induction.

Apply this result to \(\Omega\). Inclusion \(j:Y\hookrightarrow\Omega\) and the retraction satisfy \(p_*j_*=\operatorname{id}\) on homology, since the underlying maps compose to the identity. Thus \(p_*\) is surjective. Its target \(H_i(Y;\mathbb Z)\) is a quotient of the finitely generated \(H_i(\Omega;\mathbb Z)\), and vanishes whenever that group vanishes. The diffeomorphism \(M\cong Y\) identifies their singular chain complexes and proves the assertions for \(M\). This argument gives the finite bound \(i>s-1\); it does not assert that this chosen cover has \(s=n+1\). □

### A consequence for normal Euler classes

**Corollary G.4 (normal Euler class of a closed Euclidean submanifold).** Suppose \(Y\subset\mathbb R^N\) is closed as a subset and has positive codimension \(c\). If its normal bundle is oriented, its integral Euler class is zero. Without an orientation, its Euler class with coefficients in \(\mathbb F_2\) is zero.

**Proof.** Use the whole-bundle tube \(\Phi=E\Psi:\nu Y\to U\) from G.2. It identifies the zero section with \(Y\), so it is an isomorphism of pairs
\[
(\nu Y,\nu Y\setminus Y)\cong(U,U\setminus Y).
\]
The Thom class of DG-CHAR-06 T.3, integral in the oriented case and mod two otherwise, gives a class \(u_U\) in \(H^c(U,U\setminus Y;R)\), with \(R=\mathbb Z\) or \(\mathbb F_2\) accordingly. Since \(Y\) is closed, \(\mathbb R^N\setminus Y\) is open, and the closed set \(\mathbb R^N\setminus U\) is contained in it. Excision E.2 therefore makes restriction an isomorphism
\[
H^c(\mathbb R^N,\mathbb R^N\setminus Y;R)
\xrightarrow{\ \cong\ }H^c(U,U\setminus Y;R).
\tag{G.17}
\]
Let \(\widetilde u\) be the inverse image of \(u_U\). Forgetting the relative condition sends it to \(H^c(\mathbb R^N;R)=0\), since \(c>0\) and Euclidean space contracts to a point by K.1. Restrict that zero absolute class to \(Y\). By functoriality of cochains it is the same as first restricting \(\widetilde u\) to \(U\), forgetting the relative condition, and then pulling back along \(Y\hookrightarrow U\). Under \(\Phi\) this is the zero-section pullback of the absolute image of the Thom class, exactly the Euler definition T.4. Hence the Euler class is zero.

The closedness assumption was used to check excision, although G.2 itself did not require it. The positive-codimension assumption was used to make absolute cohomology of \(\mathbb R^N\) vanish. No rank-zero vanishing is asserted. □

## 3. A normal tube in an arbitrary ambient manifold

The ambient manifold \(N\) is Hausdorff, second countable, smooth, of dimension \(n\), and has no boundary. The earlier programme opening lesson supplies partitions, finite-dimensional calculus, local inversion and the complete local ODE theorem. All chains used after the construction are the singular chains of DG-CHAR-06.

### A smooth metric and a compatible distance

**Lemma J.1 (metric and distance).** There is a smoothly varying positive definite inner product \(g_x\) on every \(T_xN\). There is a metric \(d\) on \(N\) inducing its given topology and satisfying
\[
d(c(a),c(b))\leq L_g(c)
 :=\int_a^b\sqrt{g_{c(t)}(c'(t),c'(t))}\,dt
\tag{J.1}
\]
for every piecewise smooth curve \(c:[a,b]\to N\), where the integral means the sum over its finitely many smooth pieces. The metric \(d\) may be chosen bounded by \(1\), also when \(N\) is disconnected.

**Proof.** Choose coordinate charts \(\phi_i:U_i\to\mathbb R^n\) and a subordinate locally finite smooth partition \((\rho_i)\), by opening lesson 3.1. On \(U_i\), pull back the Euclidean inner product by \(d\phi_i\), multiply by \(\rho_i\), and extend the resulting bilinear form by zero outside \(U_i\). This extension is smooth: outside the closed support of \(\rho_i\) it is zero on a neighbourhood. The locally finite sum
\[
g_x(u,v)=\sum_i\rho_i(x)
 \langle d\phi_i(u),d\phi_i(v)\rangle
\tag{J.2}
\]
is a smooth symmetric bilinear form. A nonzero \(u\) has nonzero image under any chart derivative, and at least one \(\rho_i(x)\) is positive. Thus \(g_x(u,u)>0\). This construction is intrinsic because it uses actual tangent maps; writing it in another chart uses only the chain rule.

We record the local estimates needed for distance. In a chart, choose a closed coordinate ball contained in the chart domain. For \(n>0\), the continuous function
\((x,u)\mapsto g_x(u,u)\) on the product of this ball with the Euclidean unit sphere has a positive minimum \(\lambda\) and a finite maximum \(\Lambda\), by opening lesson 0.1. Homogeneity gives, on that ball,
\[
\lambda |v|^2\leq g_x(v,v)\leq\Lambda |v|^2.
\tag{J.3}
\]
For \(n=0\), the same inequality holds with \(\lambda=\Lambda=1\), since the only tangent vector is zero. Thus no minimum over an empty sphere is required. The square root of a positive smooth function is smooth by the intermediate value and inverse-function argument already given after (G.14). The integrands in (J.1) are continuous, also at zero velocity, so their integrals exist by opening lesson 0.3.

Say that two points are related when a finite concatenation of smooth coordinate paths joins them. This is an equivalence relation. Its classes are open, since a sufficiently small coordinate ball around any point can be joined to its centre by coordinate line segments. Each class is path connected: concatenate the finitely many paths in its definition. A path image is connected by the interval and continuous-image argument in DG-CHAR-06 E.5. The union of the path images from one fixed point is connected too: in a separation of that union, each connected image would have to lie in the part containing their common point, leaving the other part empty. Thus each class is connected. Its complement is the union of the other open classes. Hence these classes are exactly the connected components of \(N\): a connected subset meeting two classes would be separated by their relatively open unions.

For two points in the same component, let \(D(x,y)\) be the infimum of lengths of piecewise smooth curves joining them. The set is nonempty by the preceding paragraph, and its elements are finite nonnegative numbers. Reversing a curve preserves length, and affine reparametrization of its pieces preserves length; the latter follows by the chain rule and the affine change of variable in the Riemann integral, or directly by scaling its Riemann sums. Concatenating two such parametrized curves adds their lengths. Consequently \(D\) is symmetric, is zero on the diagonal, and satisfies the triangle inequality: choose two curves with lengths within \(\varepsilon/2\) of the two infima, concatenate, and then let \(\varepsilon\) decrease to zero.

To prove positivity and the topology assertion, centre coordinates at \(x\) and choose a closed coordinate ball of radius \(r>0\) contained in the chart, with bounds (J.3). Any piecewise smooth path starting at \(x\) and leaving the open ball has an initial segment ending on its radius-\(r\) sphere and staying in the closed ball. Indeed the first exit time exists by continuity, and its endpoint is on the boundary because the closed ball is still inside the coordinate chart. The coordinate fundamental theorem and the norm integral estimate in opening lesson 0.3 give for that segment
\[
L_g(c)\geq\sqrt{\lambda}\int |(\phi c)'(t)|\,dt
 \geq\sqrt{\lambda}\,|\phi(c(t_{\rm exit}))-\phi(x)|
 =\sqrt{\lambda}\,r.
\tag{J.4}
\]
The same estimate holds when the segment crosses finitely many smooth pieces, by summing their integrals and using the triangle inequality. For distinct \(x,y\), choose the ball small enough to exclude \(y\). Every joining path then has length at least the positive quantity in (J.4), proving \(D(x,y)>0\).

If \(y\) is inside that ball, the straight coordinate segment from \(x\) to \(y\) gives the upper bound
\[
D(x,y)\leq\sqrt{\Lambda}\,|\phi(y)-\phi(x)|.
\tag{J.5}
\]
Conversely (J.4) implies that \(D(x,y)<\sqrt{\lambda}r\) forces \(y\) to belong to the ball. These two estimates show that \(D\) induces the original topology on each component. In dimension zero the components are single points and the conclusion is immediate.

Finally set
\[
d(x,y)=
\begin{cases}
\min\{1,D(x,y)\},&x,y\text{ in the same component},\\
1,&x,y\text{ in different components}.
\end{cases}
\tag{J.6}
\]
For three points in one component, its triangle inequality follows from that of \(D\) and
\(\min(1,a+b)\leq\min(1,a)+\min(1,b)\) for \(a,b\geq0\).
If the first and third points are in different components, at least one of the two legs through the middle point has distance \(1\). If the endpoints are in one component and the middle point is in another, the two legs sum to \(2\). These cases prove the remaining triangle inequalities. Positivity and symmetry are already established. Balls of radius less than \(1\) stay inside a component, and (J.4)–(J.5) prove the topology claim. Finally the endpoints of any curve lie in a single component, and \(d\leq D\leq L_g(c)\) gives (J.1). □

### A locally defined exponential with a length bound

**Lemma J.2 (metric exponential).** For the metric \(g\) of J.1, there is an open neighbourhood \(\mathcal D\) of the zero section in \(TN\) and a smooth map
\[
\operatorname{Exp}:\mathcal D\longrightarrow N
\tag{J.7}
\]
with the following properties. It fixes the zero section. If \((x,v)\in\mathcal D\), then \((x,tv)\in\mathcal D\) for \(0\leq t\leq1\). The curve
\(t\mapsto\operatorname{Exp}_x(tv)\) has initial velocity \(v\), has constant \(g\)-speed \(\|v\|_g\), and joins \(x\) to \(\operatorname{Exp}_x(v)\). In particular
\[
d(x,\operatorname{Exp}_x(v))\leq\|v\|_g.
\tag{J.8}
\]
At the zero vector over \(x\), the tangent map is
\[
d\operatorname{Exp}_{(x,0)}(u,v)=u+v
\tag{J.9}
\]
under the canonical zero-section and vertical decomposition \(T_{(x,0)}TN\cong T_xN\oplus T_xN\).

**Proof.** In local coordinates, write \(g=(g_{ij}(x))\) and its inverse as \((g^{ij}(x))\). The inverse is smooth by the Gram-inverse implicit-function argument of G.2; the same proof applies to any smooth positive definite matrix. Define the scalar function
\[
L(x,v)=\tfrac12\sum_{i,j}g_{ij}(x)v^iv^j.
\]
For a twice differentiable coordinate path, put
\[
\mathcal E_i=\frac{d}{dt}L_{v^i}-L_{x^i}.
\tag{J.10}
\]
Direct differentiation gives
\[
\mathcal E_i
 =\sum_jg_{ij}\ddot x^j
   +\sum_{k,j}\partial_k g_{ij}\dot x^k\dot x^j
   -\tfrac12\sum_{j,k}\partial_i g_{jk}\dot x^j\dot x^k.
\]
Thus \(\mathcal E=0\) is the smooth second-order system
\[
\ddot x^\ell=\sum_{j,k}A^\ell_{jk}(x)\dot x^j\dot x^k,\qquad
A^\ell_{jk}
 =\tfrac12\sum_i g^{\ell i}
  \bigl(\partial_i g_{jk}-\partial_j g_{ik}-\partial_k g_{ij}\bigr).
\tag{J.11}
\]
These \(A^\ell_{jk}\) are acceleration coefficients. This convention agrees with the sign of Michor's displayed geodesic equation; it is the negative of the convention in which the Christoffel term is added to \(\ddot x\).

We verify that the equation is independent of coordinates. Let \(x=x(y)\), write \(J^i_a=\partial x^i/\partial y^a\), and put \(v^i=\sum_aJ^i_aw^a\). The transformed function is
\(\widetilde L(y,w)=L(x(y),J(y)w)\). The chain and product rules give
\[
\widetilde L_{w^a}=\sum_iJ^i_aL_{v^i},\qquad
\widetilde L_{y^a}
 =\sum_iJ^i_aL_{x^i}
  +\sum_{i,b}(\partial_aJ^i_b)w^bL_{v^i}.
\]
Along a path \(y(t)\) with \(w=\dot y\), subtraction yields
\[
\frac{d}{dt}\widetilde L_{w^a}-\widetilde L_{y^a}
 =\sum_iJ^i_a\mathcal E_i
   +\sum_{i,b}(\partial_bJ^i_a-\partial_aJ^i_b)w^bL_{v^i}
 =\sum_iJ^i_a\mathcal E_i.
\tag{J.12}
\]
The last equality uses equality of mixed derivatives of the smooth coordinate change. To recall its elementary proof, the four-corner difference
\[
f(z+he_a+ke_b)-f(z+he_a)-f(z+ke_b)+f(z)
\]
is, by two applications of the coordinate fundamental theorem 0.3, the iterated integral of \(\partial_b\partial_a f\) over the corresponding rectangle, with the \(a\) direction integrated outside, and also the iterated integral of \(\partial_a\partial_b f\) with the directions reversed. Divide each expression by \(hk\) and let positive \(h,k\) tend to zero. Continuity of the two derivatives makes their respective averages tend to their values at \(z\), proving equality. This proof needs no interchange-of-integrals theorem.

The Jacobian \(J\) is invertible, so (J.12) makes \(\mathcal E=0\) equivalent to its equation in the new chart. Rewrite (J.11) as the first-order system
\[
\dot x=v,\qquad \dot v^\ell=\sum_{j,k}A^\ell_{jk}(x)v^jv^k.
\tag{J.13}
\]
Opening lesson 2.1 provides unique local solutions with smooth dependence on initial position, velocity and time. The coordinate calculation and uniqueness identify solutions on overlapping charts. Joining overlapping solution intervals therefore gives a unique solution \(\gamma_{x,v}\) on the union of all intervals to which it extends from its initial datum \(\gamma(0)=x,\dot\gamma(0)=v\). This union is an interval containing zero, and solutions fit together smoothly there.

We give the time-domain argument needed for (J.7). If a solution is defined on an interval containing \([0,1]\), its lifted path \((\gamma(t),\dot\gamma(t))\) for \(0\leq t\leq1\) is compact. Each local ODE rectangle in the proof of 2.1 supplies a smaller open set of initial states and a positive time \(\varepsilon_i\) valid for every initial state in that set. Finitely many such smaller sets cover the lifted path. Take a subdivision of \([0,1]\) whose step sizes are strictly less than the minimum of these finitely many positive times. At every reference subdivision point choose one smaller set containing that state. The local theorem covers the next step, and uniqueness identifies its solution with the reference solution. At each step the local solution depends smoothly on its incoming data. Shrink a neighbourhood of the original initial vector so that its first endpoint lies in the smaller set chosen for the next step, then repeat for the finitely many steps. Continuity at each step permits each shrinking. The resulting finite compositions give solutions on the entire time interval for that neighbourhood of initial vectors, and their endpoints depend smoothly on those vectors. Using the same local formulas around any intermediate time proves smoothness there as well. The solution extends a little past each endpoint by the local theorem, so using closed time intervals imposes no endpoint exception.

Let \(\mathcal D\) be the set of initial vectors whose solution exists through time \(1\). The preceding argument shows that it is open and that \(\operatorname{Exp}_x(v)=\gamma_{x,v}(1)\) is smooth. When \(v=0\), (J.13) has the constant solution, defined for all time. Hence \(\mathcal D\) contains the zero section and \(\operatorname{Exp}_x(0)=x\).

The quadratic dependence on velocity in (J.11) gives the scaling law
\[
\gamma_{x,sv}(t)=\gamma_{x,v}(st)
\tag{J.14}
\]
where the right side is defined: differentiating it twice supplies one factor \(s^2\), and its initial velocity is \(sv\); uniqueness then gives the equality. In particular, for \(v\in\mathcal D\) and \(0\leq s\leq1\), the right side exists for \(0\leq t\leq1\), proving radial stability of \(\mathcal D\). It also gives
\(\operatorname{Exp}_x(tv)=\gamma_{x,v}(t)\) for \(0\leq t\leq1\).

For any tangent vector \(v\), its local solution \(\gamma_{x,v}\) exists for sufficiently small positive and negative times. Thus for all sufficiently small real \(h\), (J.14) defines the solution with initial vector \(hv\) through time \(1\), and
\[
\operatorname{Exp}_x(hv)=\gamma_{x,v}(h).
\]
Differentiation at \(h=0\) gives the identity on the vertical tangent space. Differentiating \(\operatorname{Exp}_x(0)=x\) along the zero section gives the identity on its tangent space. At zero a vector-bundle coordinate change has derivative \((u,v)\mapsto(Ju,Jv)\): the derivative of its fibre-linear transition in the base direction is multiplied by the zero fibre vector and vanishes. This proves the canonical decomposition and (J.9).

Finally, along any solution of (J.10), use the quadratic identity
\(\sum_i v^iL_{v^i}=2L\) to calculate
\[
\begin{aligned}
\sum_i v^i\mathcal E_i
 &=\frac{d}{dt}\left(\sum_i v^iL_{v^i}\right)
       -\sum_i\dot v^iL_{v^i}-\sum_i v^iL_{x^i}\\
 &=\frac{d}{dt}(2L)-\frac{dL}{dt}
 =\frac{dL}{dt}.
\end{aligned}
\tag{J.15}
\]
The left side is zero, so \(g(\dot\gamma,\dot\gamma)=2L\) is constant, including across coordinate overlaps since \(L\) is an intrinsic scalar. Its square root is the constant \(\|v\|_g\). The length of \(\gamma_{x,v}\) on \([0,1]\) is therefore \(\|v\|_g\), and (J.1) gives (J.8). If \(n=0\), the equation is the constant point path and every assertion holds with zero tangent vectors. □

### The normal bundle and a globally injective restriction

**Theorem J.3 (general normal tube).** Let \(Y\hookrightarrow N\) be a smooth embedded submanifold, possibly noncompact and not necessarily closed. Its normal quotient bundle
\[
\nu Y=TN|_Y/TY
\tag{J.16}
\]
has an open neighbourhood of its zero section diffeomorphic to an open neighbourhood of \(Y\) in \(N\). In fact the diffeomorphism can be chosen with domain the whole normal bundle, fixing \(Y\) and inducing the identity on the normal quotient at the zero section. The image admits a smooth retraction and a deformation retraction onto \(Y\).

If \(Y\) is closed in \(N\), the chosen tube also gives relative (co)homology isomorphisms, natural in the abelian coefficient group, between
\[
(N,N\setminus Y)\quad\text{and}\quad(\nu Y,\nu Y\setminus Y).
\tag{J.17}
\]

**Proof.** Fix \(g,d,\operatorname{Exp}\) from J.1–J.2. Identify the quotient (J.16) with the metric orthogonal complement of \(TY\) in \(TN|_Y\). Here are the smoothness details. In an ambient chart let \(G(z)\) be the metric matrix, and let \(T(z)\) be the matrix of a local tangent frame of \(Y\). The matrix
\[
P_z=T(z)(T(z)^{\mathsf T}G(z)T(z))^{-1}T(z)^{\mathsf T}G(z)
\tag{J.18}
\]
is a smooth projection onto \(T_zY\). The Gram matrix is positive definite, and its inverse is smooth by the earlier implicit-function proof. The kernel is the \(g_z\)-orthogonal complement. Projecting a fixed basis of that kernel at a chosen point by \(I-P_z\) gives a normal frame nearby: its metric Gram determinant remains nonzero by continuity. If \(B(z)\) is this frame, its coordinate inverse on normal vectors is
\[
(B(z)^{\mathsf T}G(z)B(z))^{-1}B(z)^{\mathsf T}G(z).
\]
These are smooth fibre coordinates, and their transitions are linear. The projections agree as geometric projections in overlapping ambient charts, by the uniqueness of the orthogonal decomposition. Each quotient class has the unique normal representative \((I-P_z)v\); adding a tangent vector to \(v\) leaves this representative unchanged. This constructs the smooth bundle identification with (J.16).

The embedded submanifold \(Y\) inherits its topology from \(N\), and hence is Hausdorff and second countable; intersecting a countable ambient basis with \(Y\) gives a countable basis, as proved in the opening lesson's countability argument. Its normal bundle has the ordinary subspace topology in \(TN|_Y\) in the local frames just displayed.

On the open domain supplied by J.2, restrict \(\operatorname{Exp}\) to normal vectors and call the restriction \(E\). At the zero vector over \(y\), its derivative is
\[
dE_{(y,0)}(u,v)=u+v,\qquad u\in T_yY,\quad v\perp_g T_yY.
\tag{J.19}
\]
It is an isomorphism onto \(T_yN\). The inverse function theorem therefore makes \(E\) a diffeomorphism on some neighbourhood of \((y,0)\) in the normal bundle.

For \(s>0\), set
\[
W_s(y)=\{(z,w)\in\nu Y:d(y,z)<s,\ \|w\|_g<s\}.
\tag{J.20}
\]
For sufficiently small \(s\), this lies in the preceding inverse-function neighbourhood. To verify this uniform statement over its base points, take a normal frame over a smaller relatively compact coordinate neighbourhood of \(y\) in \(Y\). In that frame an open neighbourhood of \((y,0)\) contains a product of a smaller base neighbourhood with a fixed coefficient ball. On a still smaller compact base closure, positive definiteness and the compact-unit-sphere argument of (J.3) bound the metric fibre norm below by a positive constant times the coefficient norm. For rank zero there are no fibre coordinates and this bound is automatic. Since \(d\) induces the ambient topology and \(Y\) is embedded, a sufficiently small \(d\)-ball about \(y\), intersected with \(Y\), lies in that smaller base neighbourhood. Taking \(s\) below this radius and below the corresponding fibre bound proves the assertion. In particular no closedness of \(Y\) is used.

Define \(r(y)\) to be the supremum of all \(s\in(0,1]\) for which \(W_s(y)\) is contained in the domain of \(E\) and
\(E|_{W_s(y)}\) is a diffeomorphism onto an open subset of \(N\). This is positive. Every \(s<r(y)\) has that property, by restriction from a larger admissible value, exactly as in (G.9). If \(d(y,y')=a\) and \(0<s<r(y)-a\), the triangle inequality gives
\[
W_s(y')\subset W_{s+a}(y).
\]
The fibre bound in the first set is smaller as well. Restricting the known diffeomorphism on the right proves \(r(y')\geq s\), and taking the supremum gives \(r(y')\geq r(y)-a\). When \(a\geq r(y)\) this lower bound is automatic. Interchanging the points proves
\[
|r(y)-r(y')|\leq d(y,y').
\tag{J.21}
\]
Thus \(r\) is continuous on \(Y\), without assuming that its supremum is an admissible radius.

Let \(V=\{(y,v):\|v\|_g<r(y)/2\}\). Every point of \(V\) is in the domain of \(E\), and \(E\) is a local diffeomorphism there, by the defining property at a suitable radius strictly below \(r(y)\). Suppose
\(E(y,v)=E(z,w)\) for two points of \(V\), and arrange \(r(z)\leq r(y)\). The length bound (J.8) gives
\[
\begin{aligned}
d(y,z)
 &\leq d(y,E(y,v))+d(E(z,w),z)\\
 &\leq\|v\|_g+\|w\|_g\\
 &<\tfrac12r(y)+\tfrac12r(z)\leq r(y).
\end{aligned}
\tag{J.22}
\]
Both vector norms are also strictly less than \(r(y)\). Choose \(s<r(y)\) greater than these two norms and \(d(y,z)\). Both pairs belong to \(W_s(y)\), where \(E\) is injective. They must therefore be equal. An injective local diffeomorphism is a diffeomorphism onto an open image, by the local-inverse argument in G.2. Hence \(E|_V\) is globally a diffeomorphism onto a neighbourhood of \(Y\).

Apply the positive smooth-minorant construction (G.12) on \(Y\), with this continuous function \(r\). It gives a smooth \(\delta>0\) with \(\delta<r/4\). Thus \(E\) maps
\[
V_\delta=\{(y,v):\|v\|_g<\delta(y)\}
\]
diffeomorphically onto an open neighbourhood \(U\) of \(Y\). The fibre maps (G.13)–(G.14), with the metric norm in place of the Euclidean normal norm, are smooth mutually inverse maps from the whole normal bundle to \(V_\delta\). Their smoothness follows because the squared metric norm is a smooth fibrewise quadratic function. They fix zero and have identity vertical derivative there. Composing with \(E\) gives a whole-bundle tube with derivative (J.19) at zero, and therefore the identity on the abstract quotient (J.16).

Projection after \(E^{-1}:U\to V_\delta\) is a smooth retraction to \(Y\). The formula
\[
H_t(E(y,v))=E(y,(1-t)v),\qquad 0\leq t\leq1,
\tag{J.23}
\]
stays inside \(U\), fixes \(Y\), and deforms the identity to the retraction followed by inclusion. This proves all the geometric assertions.

For the final assertion suppose \(Y\) is closed. The set \(N\setminus U\) is closed and lies inside the open set \(N\setminus Y\). Excision DG-CHAR-06 E.2 identifies the relative (co)homology of \((N,N\setminus Y)\) with that of \((U,U\setminus Y)\), for every abelian coefficient group. The whole-bundle tube is a diffeomorphism of the latter pair with \((\nu Y,\nu Y\setminus Y)\), so its induced chain maps and cochain maps give (J.17). Closedness is required here to check the excision hypothesis, and was not required for the geometric tube. □

## 4. Coefficients and Euler characteristic

### Integer presentation matrices

**Lemma C.1 (finite abelian decomposition).** Every finitely generated abelian group \(A\) has an isomorphism
\[
A\cong \mathbb Z^b\oplus
       \bigoplus_{j=1}^s\mathbb Z/d_j\mathbb Z,
\qquad b,s\geq0,\quad 2\leq d_1\mid d_2\mid\cdots\mid d_s.
\tag{C.1}
\]
The list of finite summands may be empty. Only existence is asserted and needed here.

**Proof.** Choose generators \(a_1,\ldots,a_p\) and send the standard basis of \(\mathbb Z^p\) to them. This is a surjective homomorphism onto \(A\). Its kernel \(J\) is free on at most \(p\) generators, by the proof of DG-CHAR-06 U.1 applied to the finite ordered basis of \(\mathbb Z^p\). Indeed that proof selects at most one basis vector at each of the \(p\) stages. Choose a basis of \(J\) with \(q\leq p\) elements. Its inclusion is an injective integer matrix
\[
B:\mathbb Z^q\longrightarrow\mathbb Z^p,\qquad
A\cong\mathbb Z^p/\operatorname{im}B.
\tag{C.2}
\]
For the quotient identification, send a coset of a vector to its image under the original generator map. It is well defined because the subgroup being quotiented is exactly the kernel, is injective for the same reason, and is onto because the generators span \(A\). If \(q=0\), this already gives the free decomposition. If \(p=0\), the group is zero.

We prove the required diagonal reduction for any finite rectangular integer matrix, so it can be applied successively to its smaller blocks. The allowed operations interchange two rows or two columns, multiply a row or column by \(-1\), or add an integer multiple of one row or column to a different one. Each is an automorphism over \(\mathbb Z\): swaps and sign changes undo themselves, and the inverse of an addition is subtraction of the same multiple. Thus the accumulated row and column operations give matrices \(P,Q\) with integer inverses, and change \(B\) to \(PBQ\).

For a nonzero block, move a nonzero entry to its upper left corner and change its sign if necessary so that this pivot \(d\) is positive. To clear the first column, divide an entry \(b_{i1}\) by \(d\), using integer division proved in U.1:
\[
b_{i1}=k d+r,\qquad 0\leq r<d.
\]
Subtract \(k\) times row \(1\) from row \(i\). The entry becomes \(r\). If \(r>0\), interchange rows \(1\) and \(i\); the new positive pivot is strictly smaller, and restart clearing the first column. If \(r=0\), that entry is cleared and proceed to the next row. Once the first column is cleared below the pivot, perform the corresponding column operations to clear the first row to its right. A nonzero remainder again becomes a strictly smaller pivot by a column swap, after which the clearing process restarts. A zero remainder is cleared without altering the already zero entries below the first column, since they are multiplied by the column operation's scalar.

If the first row and column are now zero off the positive pivot, inspect the remaining block. If some entry \(b_{ij}\), \(i,j>1\), is not divisible by \(d\), add column \(j\) to column \(1\). Its first entry stays \(d\), since \(b_{1j}=0\), and its \(i\)-th entry becomes \(b_{ij}\). Integer division in that row produces a nonzero remainder less than \(d\). Swapping it into the pivot position strictly decreases the pivot and restarts the process.

This procedure terminates. Every restart strictly decreases a positive integer, and between restarts only finitely many row or column entries are processed. If the extra divisibility test fails, it too forces a strict decrease. At termination the first row and column are zero off a positive pivot \(d\), and \(d\) divides every entry of the remaining block. Now apply the construction to that smaller block, leaving the first row and column fixed. Its row and column operations are integer linear combinations, so every entry remains divisible by \(d\). Its eventual first pivot is therefore a multiple of \(d\). Induction on the smaller number of rows and columns produces a rectangular diagonal matrix with positive diagonal entries
\[
d_1\mid d_2\mid\cdots\mid d_t
\tag{C.3}
\]
followed by a zero block. A zero block requires no further operations. A pivot equal to \(1\) is allowed throughout this matrix reduction.

For the injective matrix in (C.2), there can be no zero column after these operations: a zero column would send a nonzero standard basis vector to zero, contradicting injectivity, which multiplication by \(P,Q\) preserves. Hence \(t=q\). Since \(Q\) is onto, \(\operatorname{im}(PBQ)=P(\operatorname{im}B)\). The map \([v]\mapsto[Pv]\), with inverse \([w]\mapsto[P^{-1}w]\), is consequently a well-defined isomorphism between the two quotient groups. In the diagonal quotient, take the first \(q\) coordinates modulo their respective \(d_j\)'s and leave the remaining \(p-q\) coordinates unrestricted. This coordinate map is onto by choosing integer representatives of the residues, and its kernel is exactly the diagonal image. It therefore gives an isomorphism with
\[
\mathbb Z^{p-q}\oplus
\bigoplus_{j=1}^q\mathbb Z/d_j\mathbb Z.
\]
Discard the summands with \(d_j=1\), since their quotient groups are zero. The divisibility relation on the retained positive entries still holds, and every retained entry is at least \(2\). This proves (C.1). □

### The two coefficient contributions of a finite cyclic summand

**Lemma C.2 (Hom and Ext over a field).** Let \(k\) be a field, viewed also as an abelian group, and let \(A\) have a chosen decomposition (C.1). Put
\[
t_k(A)=\#\{j\colon d_j\,1_k=0\}.
\tag{C.4}
\]
Then, with the natural \(k\)-vector space structures,
\[
\dim_k\operatorname{Hom}_{\mathbb Z}(A,k)=b+t_k(A),
\qquad
\dim_k\operatorname{Ext}(A,k)=t_k(A).
\tag{C.5}
\]
In particular the two dimensions are finite. For \(k=\mathbb Q\), the first dimension is \(b\) and the second is zero.

**Proof.** An integer-linear map \(\mathbb Z\to k\) is determined by the image of \(1\), and every element of \(k\) is possible, so this Hom space is \(k\). The Ext group of a free group is zero by the free presentation in the definition preceding U.3.

An integer-linear map \(\mathbb Z/d\mathbb Z\to k\) is similarly determined by an element \(a\in k\), now with \(d a=0\). If \(d1_k\ne0\), multiplication by this scalar is invertible because \(k\) is a field, so \(a=0\). If \(d1_k=0\), every \(a\in k\) is permitted. Thus
\[
\operatorname{Hom}_{\mathbb Z}(\mathbb Z/d\mathbb Z,k)
 \cong\ker(d:k\to k).
\tag{C.6}
\]
For Ext use the explicit free presentation
\[
0\longrightarrow\mathbb Z
 \xrightarrow{\times d}\mathbb Z
 \longrightarrow\mathbb Z/d\mathbb Z
 \longrightarrow0.
\]
In the presentation definition U.3, restriction of a homomorphism from the middle \(\mathbb Z\) to the left one is multiplication by \(d\) on its value at \(1\). Therefore
\[
\operatorname{Ext}(\mathbb Z/d\mathbb Z,k)\cong k/dk.
\tag{C.7}
\]
This is zero if \(d1_k\ne0\), and is \(k\) if \(d1_k=0\), precisely the same dimension as (C.6).

Hom takes a finite direct sum in its first argument to the finite direct sum of the corresponding Hom spaces: restriction to summands and summation of their values give inverse maps. The same assertion for Ext follows directly from its presentation definition. Take the direct sum of the finitely many free presentations. Its two Hom spaces are the corresponding finite direct sums, the restriction map acts separately on each summand, and the quotient by its image is the direct sum of the individual quotients. The presentation-independence proof before U.3 identifies this computation with Ext of \(A\).

All these identifications are \(k\)-linear, with the scalar acting by multiplication on the values of a homomorphism. Adding their dimensions proves (C.5). In \(\mathbb Q\), no positive integer has zero image; multiplication by it is invertible, so every finite summand contributes zero. □

### Independence of the Euler characteristic

**Theorem C.3 (coefficient-independent Euler characteristic).** For every compact smooth manifold \(M\), with or without an orientation, and every field \(k\), the groups \(H_i(M;k)\) are finite dimensional and zero for all sufficiently large \(i\). The integer
\[
\chi_k(M)=\sum_{i\geq0}(-1)^i\dim_k H_i(M;k)
\tag{C.8}
\]
is independent of \(k\), and equals
\[
\chi(M):=\sum_{i\geq0}(-1)^i\dim_{\mathbb Q}H_i(M;\mathbb Q).
\tag{C.9}
\]
This integer is invariant under homotopy equivalences between compact smooth manifolds and is the sum of the corresponding integers over their finitely many connected components.

**Proof.** Theorem G.3 proves that the integral homology groups are finitely generated and zero above some finite degree \(B\). For each \(i\geq0\), choose a decomposition of \(H_i(M;\mathbb Z)\) as in C.1. Let \(b_i\) be the number of free summands and let \(t_i=t_k(H_i(M;\mathbb Z))\) for this decomposition. Set \(b_i=t_i=0\) when \(i<0\) or \(i>B\).

The singular chain complex over \(\mathbb Z\) is free. Its cohomological universal-coefficient theorem, fully proved in U.3, gives
\[
0\longrightarrow\operatorname{Ext}(H_{i-1}(M;\mathbb Z),k)
\longrightarrow H^i(M;k)
\longrightarrow\operatorname{Hom}_{\mathbb Z}(H_i(M;\mathbb Z),k)
\longrightarrow0.
\tag{C.10}
\]
These maps are \(k\)-linear. Evaluation is linear in cochain values. On its kernel the U.3 construction identifies a cocycle with a homomorphism on boundaries, modulo restrictions from the preceding chain group; scalar multiplication of its values commutes with those restrictions and with the factorization through the differential. Thus the kernel identification with Ext is linear too.

The two end spaces in (C.10) are finite dimensional by C.2. In a short exact sequence of vector spaces with finite-dimensional end spaces, choose a basis of the left space and lift a basis of the right space to the middle. Their combined images span: subtract a combination of the lifts to make the right image zero, and then use exactness on the left. They are independent: mapping a relation to the right first makes all lift coefficients zero, and injectivity on the left makes the remaining coefficients zero. Hence the dimension of the middle is the sum of the two end dimensions. Applied here, this gives
\[
\dim_k H^i(M;k)=b_i+t_i+t_{i-1}.
\tag{C.11}
\]
In particular these cohomology groups vanish for \(i>B+1\).

The field evaluation theorem proved after U.3, applied to the chain complex with coefficients \(k\), identifies \(H^i(M;k)\) with the full linear dual of \(H_i(M;k)\), without first assuming finite dimension. To explain that these are the same cochains as in (C.10), both descriptions assign an arbitrary value of \(k\) to each integral basis simplex and extend by \(k\)-linearity on \(k\)-chains; their differentials have the same integer face formulas.

A vector space whose full dual has finite dimension \(r\) has finite dimension at most \(r\). Otherwise one can successively choose \(r+1\) independent vectors. The basis-extension proof after U.3 extends them to a basis, and their \(r+1\) coordinate functionals are independent elements of the dual, a contradiction. In finite dimension a basis and its coordinate functionals show that the dual has the same dimension. Therefore (C.11) also equals \(\dim_k H_i(M;k)\). This proves finite dimension and vanishing above \(B+1\), including for arbitrary fields on an unoriented manifold.

We may now sum over all \(i\geq0\), because every summand is zero after a finite index. The two torsion sums cancel exactly:
\[
\begin{aligned}
\chi_k(M)
 &=\sum_{i\geq0}(-1)^i(b_i+t_i+t_{i-1})\\
 &=\sum_{i\geq0}(-1)^i b_i
   +\sum_{i\geq0}(-1)^i t_i
   -\sum_{j\geq0}(-1)^j t_j\\
 &=\sum_{i\geq0}(-1)^i b_i.
\end{aligned}
\tag{C.12}
\]
The \(i=B+1\) term is included: it can contain \(t_B\), even though integral homology is already zero in degree \(B+1\). Omitting that last possible coefficient contribution would invalidate the cancellation.

For \(k=\mathbb Q\), C.2 makes all \(t_i\) zero, so the same argument identifies
\(\dim_{\mathbb Q}H_i(M;\mathbb Q)=b_i\). Equation (C.12) is consequently (C.9), proving independence of the field and of all decomposition choices. No uniqueness assertion for the individual finite cyclic factors is needed.

The prism homotopy proof DG-CHAR-06 K.1 makes homotopic maps induce equal homology maps. If maps in two directions compose to maps homotopic to the identities, their induced maps are inverse isomorphisms. They preserve every rational homology dimension, so they preserve (C.9).

Finally, the connected components of a manifold are open, by the coordinate-path argument in J.1. Compactness gives a finite subcover from this component cover, so there are only finitely many nonempty components. A singular simplex has connected domain and its image is connected, as proved in DG-CHAR-06 E.5. Hence it lies in one component, and the singular chain complex is the direct sum of the component complexes, with differential preserving each summand. Kernels and images of that direct-sum differential are the corresponding sums, so homology is their direct sum. Dimensions add, and the finite sum in (C.9) proves componentwise additivity. The empty manifold has zero chains and \(\chi=0\). □

Here is a small chain example displaying why both torsion degrees occur. Take the free complex whose only nonzero differential is multiplication by \(6\) from degree \(1\) to degree \(0\). Its integral homology is \(\mathbb Z/6\mathbb Z\) in degree zero and zero otherwise: multiplication by \(6\) is injective on \(\mathbb Z\), and its cokernel is the displayed quotient. With coefficients in a field \(k\), if \(6\,1_k\ne0\), that differential is an isomorphism and both homology groups are zero. If \(6\,1_k=0\), the differential is zero and the two homology groups are both \(k\). The alternating sum is zero in both cases, since the two one-dimensional contributions in the second case occur in consecutive degrees. This is a direct calculation of this complex, not a claim that every such complex is a manifold's chain complex.

## 5. Thom classes as submanifold dual classes

Manifolds are smooth, Hausdorff, second countable and without boundary. The coefficient ring \(R\) is a commutative unital ring when integral orientations are specified. Without those orientations take \(R=\mathbb F_2\). Integral Thom and fundamental classes are sent to \(R\) by the coefficient homomorphism. The uniqueness of compact local fundamental classes with any abelian coefficients was proved in DG-CHAR-06 E.7–E.8, and their compatibility with orientation was established in O.4.

### A relative cap map that retains a second relative subset

**Lemma F.1 (two-subset right cap).** Let \(A,B\) be open subsets of a space \(X\). The right cap convention gives a pairing
\[
H^r(X,A;R)\otimes_R H_m(X,A\cup B;R)
\longrightarrow H_{m-r}(X,B;R),\qquad
(u,z)\longmapsto R_u z.
\tag{F.1}
\]
It is natural for maps carrying each named subset into its counterpart. It is compatible with enlargement of either relative subset and with coefficient homomorphisms. With \(B=\varnothing\), it is the relative-to-absolute map of DG-CHAR-06 X.6.

**Proof.** Put \(F=C_*(X;R)\) and \(S=C_*(A;R)+C_*(B;R)\). The natural quotient map
\[
q:F/S\longrightarrow C_*(X,A\cup B;R)
\tag{F.2}
\]
is a chain homotopy equivalence. This is the open-subset small-chain comparison proved in DG-CHAR-06 E.4: apply the support-preserving small-chain deformation K.3 to \(A\cup B\), with cover \(A,B\), and extend its homotopy by zero on the other basis simplices of \(X\). The resulting deformation sends \(C_*(A\cup B)\) into \(S\) and fixes \(S\). Its maps and homotopies descend to the two quotients, proving the assertion. The integer maps in that proof apply with coefficients in \(R\).

Choose a relative cocycle \(u\) vanishing on \(C_*(A;R)\). For an \(m\)-simplex the cap is
\[
R_u\sigma=u(\sigma[m-r,\ldots,m])\,\sigma[0,\ldots,m-r].
\tag{F.3}
\]
It is zero when \(m<r\). A simplex in \(A\) is killed, since its back face is in \(A\). A simplex in \(B\) is sent to a chain in \(B\), since its front face is in \(B\). Thus \(R_u\) induces a map
\[
F/S\longrightarrow C_{*-r}(X,B;R).
\tag{F.4}
\]
The right-cap boundary identity X.6 makes this map commute with the unshifted differentials. Define (F.1) by first applying \(q_*^{-1}\), then the homology map of (F.4).

If \(u\) changes by \(dv\) with \(v\) a relative cochain, the explicit cap homotopy in X.27 also kills chains in \(A\) and preserves chains in \(B\). It therefore descends to (F.4) and proves independence of the representative. For degree zero there are no such nonzero coboundaries. Linearity follows from (F.3).

The quotient map \(q\), as opposed to a chosen inverse at chain level, is natural: a map of the named triples sends both summands of \(S\) into their counterparts. Its inverse on homology is consequently natural too, because inverting isomorphisms in a commuting square preserves commutation. Formula (F.3) gives cap naturality directly by composing the two face restrictions with the map. The same observations apply to inclusions obtained by enlarging the named subsets and to coefficient homomorphisms. When \(B\) is empty, \(S=C_*(A)\) and \(q\) is the identity quotient, so this recovers X.6. □

### The local normalization of a normal Thom cap

**Lemma F.2 (Thom cap of a compact zero section).** Let \(\pi:E\to Y\) be a smooth real rank-\(c\) vector bundle over a compact \(m\)-manifold. Orient \(Y\) and the bundle, and give \(E\) the base-first, fibre-second orientation. Alternatively work throughout modulo two. Let \(s:Y\to E\) be its zero section, identified with the subset \(Y\subset E\). Then
\[
\pi_*R_{u_E}\mu_Y^E=[Y]
\quad\hbox{in }H_m(Y;R),
\qquad
R_{u_E}\mu_Y^E=s_*[Y]
\quad\hbox{in }H_m(E;R).
\tag{F.5}
\]
Here \(u_E\in H^c(E,E\setminus Y;R)\) is the Thom class and
\(\mu_Y^E\in H_{m+c}(E,E\setminus Y;R)\) is the compact local fundamental class of the oriented total space along its zero section.

**Proof.** The total space is a manifold in its bundle charts. It is Hausdorff: points over different base points are separated by inverse images of disjoint base neighbourhoods, and points over the same base point are separated inside one bundle chart. A finite chart-and-trivialization cover of the compact base, and countable coordinate bases in each product with \(\mathbb R^c\), give a countable basis of the total space. The zero section is closed because its complement is open in every trivialization, and is compact because it is the continuous image of \(Y\).

We check the orientation convention. Equivalently, the prescribed total local generator is the ordered product of the prescribed base local generator and the positive fibre generator. This description also records any sign attached to a zero-dimensional base point. In positive-dimensional oriented base charts and positive bundle frames the transition has the form
\((x,v)\mapsto(f(x),A(x)v)\). Its derivative is block triangular, with diagonal blocks \(Df\) and \(A\), both of positive determinant. The determinant is their product, as follows from the permutation formula in DG-CHAR-06 L.1: a nonzero permutation term in a block triangular matrix must match each diagonal block to itself. Hence these charts give a consistent orientation of \(E\). In product coordinates its positive local generator is the shuffle product of the positive base and fibre generators, in that order. Indeed O.1 defines the positive cube generator by the same ordered iterated shuffles; the shuffle association identity X.2 identifies the two expressions.

The class on the left of the first formula in (F.5) exists by X.6 and O.4. Denote it by \(\theta\). For each \(y\in Y\), we will show that its image in \(H_m(Y,Y\setminus\{y\};R)\) is the prescribed local generator. E.7 then gives \(\theta=[Y]\), since restriction to all points is injective in top degree for the compact support \(Y\).

Write \(E_y=\pi^{-1}(y)\) for the entire fibre, and use the open subsets
\[
A=E\setminus Y,\qquad B=E\setminus E_y.
\]
Their union is \(E\setminus\{s(y)\}\). Naturality of F.1 gives the commuting calculation
\[
\theta\big|_y
=\pi_*R_{u_E}\mu_{\{s(y)\}}^E
\quad\hbox{in }H_m(Y,Y\setminus\{y\};R),
\tag{F.6}
\]
where on the right the cap target is \(H_m(E,E\setminus E_y;R)\). In detail, the map from the cap with second relative subset empty to the cap with second relative subset \(B\) sends \(\mu_Y^E\) to \(\mu_{\{s(y)\}}^E\), by the defining point restrictions of the compact classes. Projection is a map of pairs
\((E,E\setminus E_y)\to(Y,Y\setminus\{y\})\), and therefore its composition is exactly restriction of \(\theta\).

Choose an oriented coordinate neighbourhood \(O\) of \(y\) that trivializes the bundle with a positive fibre frame. Excision identifies the local-point homology of \(E\) with that of \(E|_O\cong O\times\mathbb R^c\): the closed complement of this open neighbourhood lies in the open complement of \(s(y)\). Similarly,
\[
H_m(E|_O,E|_{O\setminus\{y\}};R)
\longrightarrow H_m(E,E\setminus E_y;R)
\]
is an excision isomorphism, since its removed closed subset lies in the open set \(E\setminus E_y\). The corresponding base excision isomorphism identifies the local groups at \(y\). F.1 is natural for these inclusions.

On this trivial bundle the Thom class is the pullback of the positive fibre class by T.1. Take a relative fibre cocycle \(v\) evaluating to one on the oriented cube cycle \(Q_c\). Formula T.5 is the exact identity
\[
\pi_*R_{\operatorname{pr}_{\mathbb R^c}^*v}
=(1\otimes v)\mathcal A,
\tag{F.7}
\]
where \(\mathcal A\) is the front/back product chain map. It remains valid with base-relative subset \(O\setminus\{y\}\): both sides send a chain over that subset into that subset. They kill the fibre-relative subset because \(v\) vanishes there. Thus they descend to the small product quotient in (F.2).

Translate and scale a positive coordinate cube about \(y\) to obtain a relative base cycle \(Q_m\), as in O.1. If \(m=0\), use the point cycle with its specified orientation sign; all the following maps are linear in that sign. The local generator in the product is represented by
\(\mathcal S(Q_m\otimes Q_c)\), where \(\mathcal S\) is the shuffle. The relative homotopy \(\mathcal A\mathcal S\simeq1\) of X.3–X.4 descends for the two open punctured subsets used here. Consequently (F.7) sends that local homology class to
\[
[Q_m]\,v(Q_c)=[Q_m].
\tag{F.8}
\]
There is no factor from interchanging the coordinates: the base generator precedes the fibre generator throughout, and the right cap evaluates the fibre factor last. Replacing the local Thom cocycle by its cohomologous pullback does not change this conclusion, by F.1. Equations (F.6)–(F.8) prove the required local value of \(\theta\) at every point, establishing the first equality in (F.5).

The fibre homotopy \((y,v)\mapsto(y,tv)\) connects \(s\pi\) to the identity of \(E\), while \(\pi s\) is the identity of \(Y\). The prism theorem K.1 makes \(s_*,\pi_*\) inverse homology isomorphisms. Applying \(s_*\) to the first equality gives the second. Rank zero is included: the normal class is the unit, the two cap maps are identities, and the point in the zero-dimensional fibre has its canonical positive generator. □

### Relative dual classes, restriction and evaluation

**Theorem F.3 (dual class and self-intersection).** Let \(i:Y\hookrightarrow N\) be a closed embedded submanifold of codimension \(c\). An orientation of its normal bundle determines a relative class and its absolute image
\[
\widehat\eta_Y\in H^c(N,N\setminus Y;\mathbb Z),
\qquad
\eta_Y\in H^c(N;\mathbb Z).
\tag{F.9}
\]
The relative class is obtained by transferring the normal Thom class through a tube and excision. It is independent of the tube when the induced map on the normal quotient is the identity. Its coefficient images give the classes over any commutative ring \(R\); modulo two the normal orientation is unnecessary. In all cases,
\[
i^*\eta_Y=e(\nu Y).
\tag{F.10}
\]

Suppose additionally that \(N\) is compact and oriented and \(Y\) is oriented, and choose the normal orientation so that a positive tangent basis of \(Y\), followed by a positive normal basis, is positive in \(N\). If \(\dim Y=0\), interpret this convention by the ordered product of its signed local point generator and the normal generator. In codimension zero require \(i\) to preserve the given orientations and use the canonical orientation of the zero bundle. Then
\[
R_{\eta_Y}[N]=i_*[Y],
\qquad
\langle a\smile\eta_Y,[N]\rangle
=\langle i^*a,[Y]\rangle
\quad(a\in H^{\dim Y}(N;R)).
\tag{F.11}
\]
The same formulas hold without orientation choices over \(\mathbb F_2\).

**Proof.** The whole-bundle tube J.3 is a diffeomorphism \(j:\nu Y\to U\subset N\) fixing the zero section and inducing the identity on the normal quotient. Because \(Y\) is closed, excision gives an isomorphism
\[
j^*:H^c(N,N\setminus Y;R)
\xrightarrow{\ \cong\ }
H^c(\nu Y,\nu Y\setminus Y;R).
\tag{F.12}
\]
Define \(\widehat\eta_Y\) as the inverse image of the Thom class, first integrally when oriented, or over \(\mathbb F_2\) otherwise. Forgetting the relative subset gives \(\eta_Y\). Naturality of coefficient change follows from the same definition and the uniqueness of the Thom class.

Here is the independence of the tube, with its local sign checked. For two such tubes \(j_0,j_1\), their transition \(j_0^{-1}j_1\) is defined near each point of the zero section. It fixes that section and induces the identity on the normal quotient. Fix \(y\) and use coordinates and one normal frame near it. On a sufficiently small ball of its fibre the transition has the form
\[
v\longmapsto (b(v),h(v)),\qquad b(0)=y,\quad h(0)=0,\quad Dh(0)=I.
\tag{F.13}
\]
The last derivative is the identity precisely because both tubes induce the identity on the normal quotient. Shrink the ball so that its base coordinates lie in one convex coordinate neighbourhood and
\[
|h(v)-v|<\tfrac12|v|\qquad(v\ne0).
\]
This follows from differentiability at zero with derivative \(I\). Straightly move the coordinate \(b(v)\) to \(y\), and simultaneously move \(h(v)\) to \(v\). At every intermediate time the normal component is within \(|v|/2\) of \(v\), and hence nonzero for \(v\ne0\). This gives a homotopy of punctured pairs from (F.13) to the inclusion \(v\mapsto(y,v)\). Restriction to a small fibre ball is an excision isomorphism on the local relative group. K.1 therefore shows that both tubes give exactly the same positive fibre cohomology class, rather than its negative. Pulling the class defined through \(j_0\) back through \(j_1\) consequently has the prescribed Thom restriction on every fibre. Thom uniqueness T.3 proves equality of the two relative classes in (F.9).

The composition of \(j\) with the zero section is \(i\). Thus restriction of the absolute image in (F.12) back to \(Y\) is precisely zero-section pullback of the Thom class, which is the Euler definition T.4. This proves (F.10), also in rank zero and modulo two.

For (F.11), closedness in compact \(N\) makes \(Y\) compact. The specified normal orientation exists when \(c>0\): in a local normal frame, keep or negate one frame vector to make the ordered tangent/normal generator equal the ambient generator. The required sign is locally constant because the frame determinant is continuous and nonzero. On overlaps the base and ambient orientations agree, so the block determinant rule makes the resulting normal transition determinant positive. This also accommodates a signed zero-dimensional base point. When \(c=0\), the stated orientation-preservation hypothesis supplies the same compatibility with the canonical zero bundle.

Give the normal total space the base-first orientation of F.2. The derivative of \(j\) along the zero section preserves it: it is the inclusion on the tangent summand and identity on the normal quotient, so its determinant in these ordered splittings is positive. It preserves orientation everywhere. Indeed every point \((y,v)\) is joined inside its fibre to \((y,0)\); the determinant of a diffeomorphism is continuous and never zero along that path, so its sign cannot change. The last assertion follows from the intermediate value theorem in opening lesson 0.0.

Let \(\mu_Y^N\) be the image of \([N]\) in \(H_{\dim N}(N,N\setminus Y;R)\). Under the tube it is the image of \(\mu_Y^{\nu Y}\). To see this without assuming a compatibility theorem, restrict both classes to every point of \(Y\). The positive derivative gives the same local generator by O.3, so uniqueness E.7–E.8 makes the compact classes equal.

Apply right-cap naturality first to passage from absolute chains of \(N\) to chains relative to \(N\setminus Y\), and then to the tube inclusion:
\[
R_{\eta_Y}[N]
=R_{\widehat\eta_Y}\mu_Y^N
=j_*R_{u_{\nu Y}}\mu_Y^{\nu Y}
=j_*s_*[Y]
=i_*[Y].
\tag{F.14}
\]
The first cap uses an absolute representative of the same relative cocycle; X.6 makes it kill the relative denominator, so the first equality is an identity of the induced maps. The third equality is F.2. Finally the exact cap evaluation formula X.26 and cochain pullback give
\[
\langle a\smile\eta_Y,[N]\rangle
=\langle a,R_{\eta_Y}[N]\rangle
=\langle a,i_*[Y]\rangle
=\langle i^*a,[Y]\rangle.
\]
This proves the evaluation formula. Over \(\mathbb F_2\), all local signs have the same coefficient image and the identical argument applies. □

Equation (F.10) is the self-intersection identity: the absolute dual class, restricted to the submanifold it represents, is the Euler class of that submanifold's normal bundle. It does not require transverse intersection of the submanifold with itself. The mod-two class here is the mod-two Euler class as defined in DG-CHAR-06; an identification with a characteristic class defined in a later lesson is not assumed.

## 6. The diagonal class and the tangent Euler number

The earlier programme convention is
\[
a\times b=\operatorname{pr}_1^*a\smile\operatorname{pr}_2^*b.
\]
The ordered tangent space of a product lists the first factor before the second. The coefficient field is denoted by \(k\). A closed manifold here means a compact manifold without boundary; all manifolds remain smooth, Hausdorff and second countable.

### The field product theorem with its actual maps

**Lemma D.1 (field products).** For spaces \(X,Y\), the singular shuffle cross product gives a natural isomorphism
\[
\bigoplus_{p+q=d}H_p(X;k)\otimes_k H_q(Y;k)
\xrightarrow{\ \cong\ }H_d(X\times Y;k).
\tag{D.1}
\]
If the homology groups of both factors are finite dimensional in each degree, their cohomological external products likewise give
\[
\bigoplus_{p+q=d}H^p(X;k)\otimes_k H^q(Y;k)
\xrightarrow{\ \cong\ }H^d(X\times Y;k).
\tag{D.2}
\]
They have the normalization
\[
\langle a\times b,x\times y\rangle
=\langle a,x\rangle\langle b,y\rangle
\tag{D.3}
\]
when the two respective degrees match; the evaluation is zero when they do not match but the total degrees match. For homogeneous classes,
\[
(a\times b)\smile(a'\times b')
=(-1)^{|b||a'|}(a\smile a')\times(b\smile b').
\tag{D.4}
\]

**Proof.** We first prove the algebra for any nonnegative chain complex \(C\) of \(k\)-vector spaces. Put \(Z_j=\ker\partial_j\) and \(B_j=\operatorname{im}\partial_{j+1}\). The basis-extension argument after DG-CHAR-06 U.3 gives complements
\[
Z_j=B_j\oplus\widetilde H_j,\qquad C_j=Z_j\oplus L_j.
\tag{D.5}
\]
The quotient identifies \(\widetilde H_j\) with \(H_j(C)\). Moreover
\(\partial:L_j\to B_{j-1}\) is an isomorphism: its kernel is \(L_j\cap Z_j=0\), and every boundary has a preimage whose \(L_j\) component is still a preimage.

Regard \(H(C)\) as a complex with zero differential. Let \(i:H(C)\to C\) be the chosen representative inclusion, and let \(p:C\to H(C)\) be the projection with kernel \(B\oplus L\). They are chain maps and \(pi=1\). Define \(h:C_j\to C_{j+1}\) to be the inverse of \(\partial:L_{j+1}\to B_j\) on \(B_j\), and zero on \(\widetilde H_j\oplus L_j\). On each of the three summands in (D.5), direct evaluation gives
\[
\partial h+h\partial=1-ip.
\tag{D.6}
\]
On \(B_j\) the term \(\partial h\) is the identity; on \(L_j\) the term \(h\partial\) is the identity; and both sides are zero on \(\widetilde H_j\).

For a second complex \(C'\), use maps \(i',p',h'\) of the same kind and the tensor differential
\(\partial(c\otimes d)=\partial c\otimes d+(-1)^{|c|}c\otimes\partial d\).
Writing \(P=ip\), define a degree-one operator by
\[
K(c\otimes d)=h(c)\otimes d+(-1)^{|c|}P(c)\otimes h'(d).
\tag{D.7}
\]
The first term gives
\(\partial(h\otimes1)+(h\otimes1)\partial=(1-P)\otimes1\):
the two terms containing \(h(c)\otimes\partial d\) have coefficients
\((-1)^{|c|+1}\) and \((-1)^{|c|}\), which cancel. For the second term, the two terms involving \(\partial P(c)=P(\partial c)\) have coefficients
\((-1)^{|c|}\) and \((-1)^{|c|-1}\), which cancel. Its remaining two terms are
\(P(c)\otimes(\partial h'+h'\partial)d=P(c)\otimes(1-i'p')d\).
Thus
\[
\partial K+K\partial=1-(ip)\otimes(i'p').
\tag{D.8}
\]
Together with \((p\otimes p')(i\otimes i')=1\), this proves that the tensor complex is chain homotopy equivalent to \(H(C)\otimes H(C')\), with its zero differential. In degree \(d\) the latter is the finite sum over \(p+q=d\) of the indicated tensor spaces. The induced map back to homology sends \([c]\otimes[d]\) to \([c\otimes d]\). This formula is independent of the chosen complements: changing a cycle by a boundary changes the tensor by a boundary, using the tensor differential and the fact that the other factor is a cycle. It also proves naturality for chain maps.

Now apply the result to singular chains. The maps \(\mathcal A,\mathcal S\) and both inverse homotopies in X.1–X.3 are integer formulas on basis simplices. They remain valid over \(k\), giving
\[
C_*(X\times Y;k)\simeq C_*(X;k)\otimes_k C_*(Y;k).
\]
Composing with the preceding tensor equivalence proves (D.1), with the actual shuffle as its forward map. All spaces are allowed because these are the already proved singular maps, rather than maps from a cellular complex.

The field evaluation theorem after U.3 identifies cohomology with the full linear dual of homology. If the factor homologies are finite dimensional in each degree, choose a finite basis in each relevant degree. The elementary tensors of the two bases form a basis of the tensor product: bilinearity shows spanning, and tensoring the coordinate functionals shows independence. Their paired coordinate functionals form the dual basis. Since only finitely many bidegrees occur in degree \(d\), the dual of the direct sum in (D.1) is therefore the direct sum of the tensors of the factor duals. This proves the vector-space dimensions and candidate maps in (D.2).

To identify the actual external product with that map, represent \(a,b\) by cocycles. Its cochain is \((a\otimes b)\mathcal A\), by X.4. For cycles \(c,d\), the inverse homotopy \(\mathcal A\mathcal S\simeq1\) gives
\[
((a\otimes b)\mathcal A)(\mathcal S(c\otimes d))
=(a\otimes b)(c\otimes d)
\]
at the level of evaluations on homology: applying the cocycle to the homotopy boundary gives zero. The right side is the product of the evaluations in matching bidegrees and is zero otherwise. This is (D.3). It identifies the product classes with the dual tensor basis, proving (D.2) with precisely the stated map.

Finally expand each external product as the two ordered pullbacks. Cup associativity follows directly from the three successive face blocks in K.5. Commute only the middle pair, \(\operatorname{pr}_2^*b\) and \(\operatorname{pr}_1^*a'\), using X.5, and obtain the sign \((-1)^{|b||a'|}\). Naturality of the cup product then combines the two first-factor terms and the two second-factor terms. This is (D.4). □

### Fundamental products and the slant convention

**Lemma D.2 (product and slant normalizations).** For closed oriented manifolds \(M^m,N^n\), the product orientation satisfies
\[
[M\times N]=[M]\times[N].
\tag{D.9}
\]
This holds over the integers and their coefficient images, and modulo two without orientations.

For a degree-\((q+r)\) class \(\beta\in H^{q+r}(X\times Y;k)\) and a homology class \(z\in H_r(Y;k)\), \(q,r\geq0\), define the right-factor slant class \(\beta/z\in H^q(X;k)\) by the cochain formula
\[
(\beta/z)(c)=\beta\bigl(\mathcal S(c\otimes z)\bigr),
\tag{D.10}
\]
using cycle and cocycle representatives on the right. This is well defined on classes. For homogeneous \(a,b\),
\[
(a\times b)/z=
\begin{cases}
\langle b,z\rangle a,&|b|=r,\\
0,&|b|\ne r,
\end{cases}
\tag{D.11}
\]
whenever the slant degree is nonnegative.

**Proof.** A finite product of compact spaces is compact by opening lesson 0.1; product charts and product countable bases make \(M\times N\) a manifold with the stated dimension. Restrict the class \([M]\times[N]\) to any point \((x,y)\). Naturality of the relative shuffle in X.4 identifies it with the product of the two local point generators. The relative denominator is the union
\[
(M\setminus\{x\})\times N\ \cup\ M\times(N\setminus\{y\}),
\]
which is exactly the complement of \((x,y)\), and both subsets are open. In positive local coordinates the two point generators are the ordered cube cycles of O.1. Their shuffle product is the positive cube generator in the concatenated coordinate order, by shuffle associativity X.2. For a zero-dimensional factor with a signed point orientation, multiply its canonical point cycle by that sign; bilinearity gives the corresponding product sign. Thus every point restriction is the product orientation generator. Uniqueness E.7–E.8 proves (D.9). The same proof works with coefficient images and modulo two.

We now prove the slant assertions. If \(\beta\) is a cocycle and \(z\) a cycle, the tensor boundary formula implies
\[
(d(\beta/z))(c)=\beta\mathcal S(\partial c\otimes z)
=\beta\partial\mathcal S(c\otimes z)=0.
\]
If \(\beta\) changes by \(d\lambda\), its slant changes by \(d(\lambda/z)\), by the same boundary formula with \(\partial z=0\). If \(q=0\), the putative negative-degree cochain \(\lambda/z\) is zero, and this calculation says the change itself is zero.

If \(z\) changes by \(\partial w\), use that \(\beta\) is a cocycle on the boundary of \(\mathcal S(c\otimes w)\), for a degree-\(q\) chain \(c\). It gives
\[
\beta\mathcal S(c\otimes\partial w)
=(-1)^{q+1}\beta\mathcal S(\partial c\otimes w).
\tag{D.12}
\]
For \(q\geq1\) this is the coboundary of the degree-\((q-1)\) cochain
\((-1)^{q+1}\beta/w\). For \(q=0\) the right side is zero, since \(\partial c=0\). This proves representative independence. Formula (D.10) is linear and is compatible with maps of the two spaces by naturality of the shuffle.

For a cycle \(c\) in the slant degree, (D.3) evaluates (D.10) as
\(\langle a,c\rangle\langle b,z\rangle\) in the matching bidegree and as zero otherwise. Injectivity of field cohomology evaluation after U.3 identifies its class with the right side of (D.11), even when the factor homologies are not finite dimensional. This proves the claimed slant normalization. □

### The diagonal with every sign specified

**Theorem D.3 (signed diagonal class).** Let \(M\) be a closed oriented \(n\)-manifold, not necessarily connected. In dimension zero use the canonical positive orientation of each point. Let
\(\Delta:M\hookrightarrow M\times M\) be the diagonal. Identify its normal quotient with \(TM\) by
\[
[(v,w)]\longmapsto w-v,
\qquad
t\longmapsto[(0,t)]
\tag{D.13}
\]
for the inverse, and transport the tangent orientation through this identification. Let \(U\in H^n(M\times M;k)\) be the coefficient image of its absolute dual class from F.3. Choose a basis \(a_{p,1},\ldots,a_{p,b_p}\) of \(H^p(M;k)\) for each \(p\), and its cup-pairing dual basis \(b_{p,1},\ldots,b_{p,b_p}\) in \(H^{n-p}(M;k)\), defined by
\[
\langle a_{p,i}\smile b_{p,j},[M]\rangle=\delta_{ij}.
\tag{D.14}
\]
Then
\[
U=\sum_{p=0}^n\sum_{i=1}^{b_p}(-1)^p\,a_{p,i}\times b_{p,i},
\qquad
\Delta^*U=e(TM)_k.
\tag{D.15}
\]
The formulas hold over \(\mathbb F_2\) without orientations, with every sign interpreted in that field. Under the slant convention D.2, \(U/[M]=1\in H^0(M;k)\).

**Proof.** The diagonal map is an injective immersion: its derivative sends \(v\) to \((v,v)\), and projection onto the first factor is an inverse on its image. It is a homeomorphism onto that image, since that projection is continuous. The local constant-rank theorem in the opening lesson then makes it an embedded submanifold. Its image is closed: if \(x\ne y\), disjoint neighbourhoods of \(x,y\) give a product neighbourhood of \((x,y)\) that misses the diagonal.

The linear map \((v,w)\mapsto w-v\) has the diagonal tangent space as its kernel and is onto. Thus it induces the isomorphism and explicit inverse in (D.13). These maps commute with changes of tangent coordinates, so they define a smooth bundle isomorphism. At each diagonal point, the ordered diagonal tangent vectors and the chosen normal lifts give the block matrix
\[
\begin{pmatrix}I&0\\ I&I\end{pmatrix}
\tag{D.16}
\]
relative to the product tangent coordinates. Its determinant is \(1\), by the block triangular determinant calculation in F.2. Therefore this normal orientation is exactly the tangent-first normal orientation required in F.3. For \(n=0\), the use of positive point orientations ensures the same statement with the canonical zero-bundle orientation. F.3 now gives
\[
\langle z\smile U,[M\times M]\rangle
=\langle\Delta^*z,[M]\rangle,
\qquad
\Delta^*U=e(TM)_k.
\tag{D.17}
\]
The second equality uses Euler naturality T.4 under the bundle isomorphism (D.13).

B.6 supplies the finite perfect cup pairing on \(M\); the field evaluation theorem identifies the cohomology and homology dimensions. Also B.5 implies \(H^p(M;k)=0\) for \(p>n\), since its dual homology degree \(n-p\) is negative. Thus the bases and dual bases in (D.14) exist and only finitely many terms occur. The same assertions apply to \(M\times M\).

Let \(V\) denote the proposed sum in (D.15). To identify it with \(U\), it suffices by the perfect middle-degree pairing on \(M\times M\) to evaluate \(z\smile V\) on its fundamental class for every \(z\in H^n(M\times M;k)\). By D.1 such \(z\)'s are spanned by products \(x\times y\) with \(|x|=n-p\) and \(|y|=p\). Equations (D.3), (D.4) and (D.9) make all terms of \(V\) with index different from \(p\) evaluate to zero. The remaining evaluation is
\[
\begin{aligned}
\langle(x\times y)\smile V,[M\times M]\rangle
&=\sum_i(-1)^{p+p^2}
   \langle x\smile a_{p,i},[M]\rangle
   \langle y\smile b_{p,i},[M]\rangle\\
&=\sum_i
   \langle x\smile a_{p,i},[M]\rangle
   \langle y\smile b_{p,i},[M]\rangle\\
&=\langle x\smile y,[M]\rangle.
\end{aligned}
\tag{D.18}
\]
For the last equality, expand
\(y=\sum_i\langle y\smile b_{p,i},[M]\rangle a_{p,i}\),
which follows directly from (D.14). The two signs cancel because \(p+p^2=p(p+1)\) is even. Finally,
\(\Delta^*(x\times y)=x\smile y\), since both projections composed with \(\Delta\) are the identity and cup products are natural. Thus (D.18) equals the right side of (D.17). Perfect pairing implies \(V=U\).

The argument has not assumed that \(H^0(M;k)\) is one dimensional. It uses the entire cohomology of all components, so it applies unchanged to disconnected manifolds. For clarity about the last assertion, D.11 kills all terms in \(U/[M]\) except those with \(p=0\), and yields
\[
U/[M]=\sum_i\langle b_{0,i},[M]\rangle a_{0,i}.
\]
But the coefficient of \(a_{0,i}\) in the expansion of the unit \(1\in H^0(M;k)\) is
\(\langle1\smile b_{0,i},[M]\rangle=\langle b_{0,i},[M]\rangle\).
This proves \(U/[M]=1\), also when there are several components or none. All calculations remain valid in characteristic two with its unsigned local generators. □

### From the diagonal to Euler characteristic

**Theorem D.4 (tangent Euler number).** A closed oriented \(n\)-manifold satisfies
\[
\langle e(TM),[M]\rangle=\chi(M)\quad\hbox{in }\mathbb Z.
\tag{D.19}
\]
In dimension zero this uses the canonical positive point orientations. Every closed manifold, without an orientation assumption, satisfies
\[
\langle e_2(TM),[M]_2\rangle=\chi(M)\pmod2.
\tag{D.20}
\]
Here \(e_2\) is the mod-two Euler class already defined in DG-CHAR-06. If a smooth tangent section has only finitely many zeros and all are nondegenerate, its integral sum of local indices is \(\chi(M)\) in the oriented case, and the parity of its number of zeros is \(\chi(M)\bmod2\) in general.

**Proof.** First use \(k=\mathbb Q\) in D.3 and pull its diagonal formula back along \(\Delta\). Evaluation on \([M]\) and (D.14) give
\[
\langle e(TM)_{\mathbb Q},[M]_{\mathbb Q}\rangle
=\sum_{p=0}^n(-1)^p b_p
=\chi(M).
\tag{D.21}
\]
The last equality is C.3, together with the field evaluation identification of homology and cohomology dimensions. At the chain level, applying the homomorphism \(\mathbb Z\to\mathbb Q\) to a cocycle and a cycle commutes with their evaluation. Thom uniqueness and its Euler definition T.4 likewise make the rational Euler class the coefficient image of the integral one. Hence the left side of (D.21) is the rational image of the integer on the left of (D.19). The inclusion \(\mathbb Z\to\mathbb Q\) is injective, so equality in (D.21) proves (D.19) integrally. No integral Künneth splitting or integral dual basis is asserted.

Next use \(k=\mathbb F_2\) in D.3. The same pullback and evaluation give the image in \(\mathbb F_2\) of
\(\sum_p(-1)^p\dim_{\mathbb F_2}H^p(M;\mathbb F_2)\).
The integer in this expression is \(\chi(M)\) by C.3; reducing it modulo two proves (D.20). This is why coefficient independence was proved before this step.

In dimension zero the manifold is a finite set of points, by compactness and the open-component argument in C.3. Its tangent bundle has rank zero, with Thom and Euler class the canonical unit. The point-complex calculation after E.1 gives one homology generator in degree zero per point and no higher homology. Evaluation on the sum of the positive point classes and the definition of \(\chi\) both give the number of points. The empty manifold gives zero on both sides. Thus no orientation of a zero-dimensional vector space is chosen contrary to the canonical rank-zero convention.

Finally DG-CHAR-06 N.1–N.2 identify the sum of the local indices of the specified section with the integral Euler evaluation, and N.4 gives the corresponding mod-two count without orientation. Apply (D.19)–(D.20) to obtain the last assertion. These earlier results apply because each zero is isolated by its invertible derivative, and the stated finite zero set satisfies their compact-support hypotheses. □

As one immediate check, if \(n\) is odd and \(M\) is oriented, B.6 gives \(b_p=b_{n-p}\). The paired terms in (D.21) have opposite signs and there is no middle integer degree \(n/2\). Hence \(\chi(M)=0\) and its tangent Euler number is zero. This conclusion uses the proved pairing, rather than a vector-field existence assertion.

## Free construction sources

These exact freely accessible author versions supplied the mathematical reading. The consumed arguments, including the steps assigned as exercises or omitted in a source, are proved in this chapter or the earlier programme lessons.

- Allen Hatcher, free author electronic [Chapter 3 of *Algebraic Topology*](https://pi.math.cornell.edu/~hatcher/AT/ATch3.pdf), printed pages 240–250: compact supports, duality, connecting maps and field pairings.
- Marco Gualtieri, free author [*Geometry and Topology I*, 2012 lecture notes](https://www.math.toronto.edu/mgualt/courses/MAT425F-2013/docs/1300-2012-notes.pdf), Theorem 3.49, Proposition 3.54 and Theorem 3.56 on printed pages 34 and 37–38: compact embedding and Euclidean normal neighbourhoods.
- Peter W. Michor, free author draft [*Topics in Differential Geometry*](https://www.mat.univie.ac.at/~michor/dgbook.pdf), Sections 22.1–22.4, 22.6–22.7, 23.1 and 23.5: positive metrics, length, geodesic coefficients, local exponential maps and distance. Section J supplies the complete coordinate-invariance, time-domain and globally injective tube arguments used here.
- William Stein, [“Finitely generated abelian groups,” Harvard Math 129 lecture notes, 2004](https://people.math.harvard.edu/archive/129_spring_04/ant/html/node9.html): finite integer matrix reduction and quotient decomposition. Section C includes unit pivots and the complete adjacent-degree coefficient calculation.
- Chris Wendl, free author [*Topology I–III*, HU Berlin lecture notes](https://www2.mathematik.hu-berlin.de/~wendl/Sommer2025/Topologie3/lecturenotes.pdf), printed pages 465–468 and 472, and Exercise 53.2 on pages 475–476: Thom/fundamental comparison and the diagonal-intersection problem. Sections F and D give complete proofs with the chapter's base-first orientation and right cap.
- Hatcher, free author electronic [additional Chapter 3 topics](https://pi.math.cornell.edu/~hatcher/AT/ATch3.4.pdf), printed pages 274–276: tensor complexes and the field product theorem. D.1 proves the field contraction with the actual singular product maps.

Original exposition: GPT-6 Astra (OpenAI), October 2026, CC0 1.0. Human source authors are credited above. No source prose, diagrams or source PDFs are reproduced.
