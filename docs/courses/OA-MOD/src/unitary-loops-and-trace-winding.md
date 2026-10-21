# Unitary loops and trace winding

Let \(M\) be a type \(\mathrm{II}_1\) factor with normalized normal trace \(\tau\). Give its unitary group \(U(M)\) the operator norm topology. We will prove


\[
\pi_1(U(M),1)\cong (\mathbb R,+).
\]


The isomorphism measures a loop by its trace winding. For a projection \(p\), the loop that rotates \(pH\) once and fixes its orthogonal complement has value \(\tau(p)\). The delicate point is that this statement concerns unitaries in \(M\) itself. We prove the passage from these loops to stable matrix loops before using Bott periodicity.

We use the [comparison theorem and halving of projections](https://github.com/KokunoYumeto/open-math-courses-public/blob/main/docs/courses/foundations-of-von-neumann-algebras/src/projections-and-types-of-von-neumann-algebras.md), Theorem 5.5 and Proposition 13.3; [existence of the normal trace](https://github.com/KokunoYumeto/open-math-courses-public/blob/main/docs/courses/OA-FOUND-REMAINDER/supplements/traces-on-von-neumann-algebras-part-a-def-v-2-1-to-def-v-2-17.md), Theorem 5.2; [bounded polar decomposition](https://github.com/KokunoYumeto/open-math-courses-public/blob/main/docs/courses/foundations-of-von-neumann-algebras/src/the-double-commutant-theorem.md); and [Bott periodicity](https://github.com/KokunoYumeto/open-math-courses-public/blob/main/docs/courses/KT-OPK/src/KT-OPK-10.md#4-the-boundary-proves-periodicity-and-fixes-its-sign), Theorem 4.1. Their proofs are in the linked programme lessons. Continuous functional calculus, including inverse square roots, is proved in [Bounded operator kernel](https://github.com/KokunoYumeto/open-math-courses-public/blob/main/docs/courses/OA-MOD/src/bounded-operator-kernel.md). All continuity in this lesson is norm continuity. No separability assumption is made.

## 1. Projection sizes and dense invertibles

**Lemma 1.1.** In a finite factor with faithful finite trace \(\rho\), two projections are equivalent exactly when their traces agree. In a type \(\mathrm{II}_1\) factor with normalized trace, every number in \([0,1]\) is the trace of a projection. Invertible elements are norm dense in every finite factor.

**Proof.** Equivalent projections have equal trace. Comparison in a factor says that one projection is equivalent to a subprojection of the other. If the two traces agree, the unmatched projection has trace zero and is zero by faithfulness. This proves the first assertion.

Halving repeatedly divides the identity into \(2^j\) equivalent projections of trace \(2^{-j}\), with each partition refining the preceding one. Order the pieces so that the two children of a piece are consecutive. The sum of the first \(\lfloor 2^j t\rfloor\) pieces gives an increasing sequence \(e_j\) with trace tending to \(t\), for \(0\leq t<1\). Its supremum is a projection with trace \(t\) by normality. Use the identity for \(t=1\). The same construction works below any nonzero projection, with its trace as the total size: every such corner has no nonzero abelian projection, so the halving theorem applies there as well.

For the last assertion, write \(a=v|a|\). The support projections \(v^*v\) and \(vv^*\) have equal trace, so their complements are equivalent. Choose a partial isometry between those complements and add it to \(v\), obtaining a unitary \(u\) with \(a=u|a|\). Then


\[
a_\epsilon=u(|a|+\epsilon 1)
\]


is invertible and \(\|a_\epsilon-a\|=\epsilon\). There is no claim that the choice of \(u\) depends continuously on \(a\). \(\square\)

For later use, write \(\rho_m=\operatorname{Tr}_m\otimes\rho\), with the ordinary, unnormalized matrix trace. This is a faithful finite trace on \(M_m(M)\): positivity and faithfulness follow by applying it to \(x^*x\), whose trace is \(\sum_{i,j}\rho(x_{ij}^*x_{ij})\); cyclicity follows by interchanging the two finite indices. The center of a matrix algebra over a factor is scalar, as commuting with the matrix units first forces a scalar diagonal matrix and commuting with diagonal copies of the factor then forces a scalar entry. Thus projection comparison by trace applies in these matrix algebras too.

## 2. Approximating a family of columns

For a unital C*-algebra \(A\), call a column \(a=(a_1,\ldots,a_r)^T\) *generating* if \(a^*a=\sum_j a_j^*a_j\) is invertible. This condition allows the normalization \(a(a^*a)^{-1/2}\).

**Lemma 2.1.** Suppose invertibles are dense in \(A\). Let \(X\) be a finite polyhedron of dimension at most \(d\). Every continuous map \(X\to A^{d+1}\) can be uniformly approximated by a map whose column is generating at every point.

**Proof.** Fix an error tolerance. Subdivide a finite triangulation finely enough that each coordinate varies by less than a chosen \(\delta>0\) on every vertex star of its barycentric subdivision. Such subdivisions exist: in dimension \(d>0\), the diameter of each simplex after barycentric subdivision is at most \(d/(d+1)\) times the old maximum diameter, because its vertices are barycenters of nested faces. Iteration makes the mesh tend to zero; a vertex star has diameter at most twice the mesh. Dimension zero is immediate.

Color a vertex in the final barycentric subdivision by the dimension of the face whose barycenter it is. There are \(d+1\) colors. Each simplex has at most one vertex of each color. Let \(\lambda_v\) be the piecewise affine barycentric coordinate of vertex \(v\), extended by zero off its star. Set


\[
F_v=\{x:\lambda_v(x)\geq 1/(d+1)\}.
\]


These closed sets cover \(X\): at most \(d+1\) barycentric coordinates are positive at any point and their sum is one. Choose a continuous scalar function \(\chi_v\), depending only on \(\lambda_v\), which is zero for \(\lambda_v\leq 1/(2(d+1))\), is one on \(F_v\), and lies in \([0,1]\). Supports belonging to distinct vertices of the same color are disjoint, since no simplex contains both vertices.

For a vertex \(v\) of color \(j\), choose an invertible \(c_v\in A\) within \(\delta\) of \(a_j(v)\). Define


\[
b_j(x)=a_j(x)+
\sum_{v\text{ of color }j}
\chi_v(x)(c_v-a_j(x)).
\]


At most one summand is nonzero at a point. Hence \(\|b_j-a_j\|_\infty<2\delta\), and the column error is at most \(2\sqrt{d+1}\,\delta\). On \(F_v\), coordinate \(b_j\) is the invertible element \(c_v\). Thus at each point at least one \(b_j^*b_j\) is bounded below by a positive scalar times the identity. The sum is invertible. Its inverse varies continuously and is bounded on compact \(X\). Taking \(\delta\) sufficiently small proves the assertion. \(\square\)

The proof also works with more than \(d+1\) coordinates, leaving the surplus coordinates unchanged. It uses finitely many independent choices of invertibles; it does not choose a continuous polar decomposition of the original entries.

## 3. Contracting spheres of unit columns

Let


\[
S_n(A)=\{v\in A^n:v^*v=1\},
\qquad e_n=(0,\ldots,0,1)^T.
\]


**Lemma 3.1.** If invertibles are dense in \(A\), every map \(S^k\to S_n(A)\) is freely null-homotopic when \(n\geq k+2\).

**Proof.** Apply Lemma 2.1 to the first \(n-1\) coordinates of the map. Make their column generating, with total perturbation smaller than \(1/4\), and leave the last coordinate unchanged. Interpolate linearly from the original column to the perturbed column, normalizing throughout. This is legitimate: if \(v^*v=1\) and \(\|a-v\|<\eta=1/4\), then


\[
\|a^*a-1\|\leq 2\eta+\eta^2<1.
\]


For the resulting column, the first \(n-1\) entries are generating. Interpolate the last entry to \(1\), keeping the first entries fixed and normalizing; the positive contribution of the first entries guarantees invertibility at every stage. Finally shrink those first entries to zero while keeping the last entry equal to \(1\), again normalizing. The endpoint is the constant column \(e_n\). Compactness makes every inverse square root in these homotopies continuous. \(\square\)

We need contractions that fix a base point, and lifts that fix boundary values. The following explicit formula provides both.

For nearby unit columns \(v,w\), put \(p=vv^*\), \(q=ww^*\), and


\[
\begin{aligned}
B(w,v)&=wv^*+(1-q)(1-p),\\
L(w,v)&=B(w,v)
\bigl(B(w,v)^*B(w,v)\bigr)^{-1/2}.
\end{aligned}
\]


Here \(B(v,v)=1\), and
\(\|B(w,v)-1\|\leq 3\|w-v\|\), since \(\|q-p\|\leq2\|w-v\|\). In particular \(B\) is invertible whenever \(\|w-v\|<1/4\). Also \(Bv=w\) and \(B^*w=v\). Thus \((B^*B)v=v\), functional calculus gives \((B^*B)^{-1/2}v=v\), and


\[
L(w,v)v=w,\qquad L(v,v)=1.
\]


These unitaries depend continuously on the pair \((w,v)\).

**Lemma 3.2 (relative lifting).** Let \(X\) be compact and let \(h:X\times[0,1]\to S_n(A)\) be continuous. If \(V_0:X\to U_n(A)\) has last column \(h(x,0)\), there is a continuous \(V:X\times[0,1]\to U_n(A)\) with \(V(x,0)=V_0(x)\) and last column \(h(x,s)\). Wherever \(h(x,s)\) is independent of \(s\), this lift can be kept equal to \(V_0(x)\).

**Proof.** Uniform continuity supplies a finite time partition \(0=s_0<\cdots<s_l=1\) on each of whose intervals \(\|h(x,s)-h(x,s_i)\|<1/4\), uniformly in \(x\). Inductively set


\[
V(x,s)=L(h(x,s),h(x,s_i))V(x,s_i).
\]


The formulas agree at subdivision points. They have the required last column and stay fixed on every prescribed constant column, by \(L(v,v)=1\). \(\square\)

Consequently the null-homotopies in Lemma 3.1 may be made based at \(e_n\). Indeed, let \(H(x,s)\) be the given contraction and let \(x_0\) be the base point. Lift the path \(H(x_0,s)\), starting at the identity, to a unitary path \(R(s)\). Then \(R(s)^*H(x,s)\) fixes \(e_n\) at \(x_0\), starts at the original based map, and ends at the constant \(e_n\). Hence


\[
\pi_1(S_n(A),e_n)=0\ (n\geq3),
\qquad
\pi_2(S_n(A),e_n)=0\ (n\geq4).
\]


## 4. Removing matrix stabilization

**Proposition 4.1.** If invertibles are dense in \(A\), the map


\[
\pi_1(U_{n-1}(A),1)
\longrightarrow\pi_1(U_n(A),1),
\qquad u\longmapsto\operatorname{diag}(u,1),
\]


is an isomorphism for \(n\geq4\).

**Proof.** For surjectivity, take a based loop in \(U_n(A)\). Its last column is a based loop in \(S_n(A)\), which has a based contraction by Section 3. Lift that contraction with the original unitary loop as initial lift. Relative lifting fixes its endpoints at the identity. The final loop has last column \(e_n\), so, by unitarity, it is \(\operatorname{diag}(u,1)\) for a loop \(u\in U_{n-1}(A)\).

For injectivity, suppose such a block loop bounds a unitary disk \(F:D^2\to U_n(A)\). Its last column is constant \(e_n\) on the boundary and therefore defines a based sphere in \(S_n(A)\). Here \(D^2/\partial D^2\) is a sphere: in polar coordinates the map
\((r,\theta)\mapsto(\sin(\pi r)\cos\theta,\sin(\pi r)\sin\theta,\cos(\pi r))\)
gives a continuous bijection from that compact quotient onto the sphere, hence a homeomorphism. Since \(\pi_2(S_n(A))=0\), contract the column disk to \(e_n\) while fixing its boundary. Lift this homotopy starting at \(F\); the lift fixes the original unitary boundary. The final disk fixes \(e_n\) and lies in \(\operatorname{diag}(U_{n-1}(A),1)\), proving injectivity. \(\square\)

Thus all stabilization maps on \(\pi_1(U_m(A))\) are isomorphisms once \(m\geq3\). We now apply this to a corner of \(M\), rather than assuming any self-similarity of the factor.

Choose three orthogonal equivalent projections \(p_1,p_2,p_3\) of trace \(1/3\) with sum \(1\), using Lemma 1.1 in successive corners. Put \(p=p_1\), \(N=pMp\), and choose partial isometries \(v_i\) from \(p\) onto \(p_i\), with \(v_1=p\). Then


\[
\Phi:M_3(N)\longrightarrow M,
\qquad
\Phi((a_{ij}))=\sum_{i,j=1}^3v_i a_{ij}v_j^*
\]


is a unital *-isomorphism. Multiplication uses \(v_i^*v_j=\delta_{ij}p\); its inverse has entries \(v_i^*xv_j\). These formulas prove multiplicativity, preservation of adjoints, and both inverse identities. The center calculation for matrices shows that \(N\) is a factor, and \(3\tau|_N\) is a faithful normalized finite trace. Lemma 1.1 therefore makes invertibles dense in \(N\).

Under \(\Phi\), the stabilization of \(U_m(M)\) becomes the inclusion of \(U_{3m}(N)\) into \(U_{3m+3}(N)\), adding three identity coordinates. Proposition 4.1 applies at every intervening size. It follows that


\[
\pi_1(U(M),1)
\xrightarrow{\ \cong\ }
\varinjlim_m\pi_1(U_m(M),1).
\tag{4.1}
\]


The corner \(N\) need not be isomorphic to \(M\). No assumption on the Murray–von Neumann fundamental group of the factor has entered this proof.

## 5. Bott periodicity and the real dimension group

Write \(SM=C_0((0,1),M)\). The group on the right of (4.1) is \(K_1(SM)\). To see the identification precisely, an invertible matrix over the unitization of \(SM\) is an invertible path whose two endpoint values are the same scalar matrix \(c\). Multiplication by \(c^{-1}\) makes it based. Scalar invertible matrices are path connected, by polar decomposition followed by a logarithm of the finite-dimensional unitary, so this normalization does not change its K-class. It works for homotopies too, with their continuously varying endpoint matrices. Polar normalization \(a\mapsto a(a^*a)^{-1/2}\) then identifies invertible based loops with unitary based loops, also for homotopies and stabilization.

The group operations agree. Pointwise multiplication of two based loops is based-homotopic to their concatenation: apply \((s,t)\mapsto u(s)v(t)\) to paths in the square from \((0,0)\) to \((1,1)\), deforming the diagonal to the bottom and right edges by linear interpolation of their parametrizations. The matrix rotation in [K-theory of invertibles, Theorem 2.2](https://github.com/KokunoYumeto/open-math-courses-public/blob/main/docs/courses/KT-OPK/src/KT-OPK-06.md#2-the-rotation-that-makes-addition-commute) identifies pointwise multiplication with stabilized block sum.

[Bott periodicity, Theorem 4.1](https://github.com/KokunoYumeto/open-math-courses-public/blob/main/docs/courses/KT-OPK/src/KT-OPK-10.md#4-the-boundary-proves-periodicity-and-fixes-its-sign) identifies this stable loop group with \(K_0(M)\). Its map sends a projection class \([e]\) to the class of


\[
\ell_e(t)=1-e+e^{2\pi it}e.
\]


For completeness, compute the latter group. Projections over \(M\), stabilized by zero blocks, are classified by their numbers \(\tau_m(e)\): move two projections into the same matrix algebra and apply Lemma 1.1. Every nonnegative real number occurs, by taking a finite sum of identity blocks and one projection of the required remaining trace in \([0,1)\). Block sum adds these numbers. Thus the projection monoid is \((\mathbb R_{\geq0},+)\), and its group completion is \((\mathbb R,+)\): the difference of two nonnegative numbers gives every real number, and equality of such differences is exactly the relation \(a+d=b+c\) defining the group completion.

Combining this computation, Bott periodicity, and (4.1) proves that \(\pi_1(U(M),1)\) is isomorphic to \(\mathbb R\). We next give its explicit formula and sign.

## 6. The winding integral

For a piecewise continuously differentiable based unitary loop \(u\), define


\[
W_\tau(u)=\frac{1}{2\pi i}
\int_0^1\tau(u(t)^*u'(t))\,dt.
\tag{6.1}
\]


It is real, since differentiating \(u^*u=1\) makes \(u^*u'\) skew-adjoint and a positive functional satisfies \(\tau(x^*)=\overline{\tau(x)}\).

**Lemma 6.1.** Formula (6.1) extends to a well-defined homomorphism on the fundamental group of norm-continuous loops. It is unchanged by stabilization when matrix traces are unnormalized.

**Proof.** Every continuous unitary loop has a piecewise smooth representative. Subdivide it until successive values are sufficiently close. Join them by
\(u(t_j)\exp(s\log(u(t_j)^*u(t_{j+1})))\).
The logarithm is the convergent power-series logarithm near the identity; it is skew-adjoint on nearby unitaries. These joins approximate the original path uniformly. Any two uniformly close unitary paths with the same endpoint values are homotopic relative to those endpoints by


\[
H(s,t)=u(t)\exp\bigl(s\log(u(t)^*v(t))\bigr).
\tag{6.2}
\]


This also shows that different sufficiently fine polygonal replacements have the same homotopy class.

For piecewise continuously differentiable \(u,v\) close enough for (6.2), that homotopy is smooth in \(s\) and piecewise continuously differentiable in \(t\), with continuous mixed derivatives on each piece. Differentiation and the trace identity give


\[
\partial_s\tau(H^{-1}\partial_tH)
=\partial_t\tau(H^{-1}\partial_sH).
\]


Indeed the difference of the two sides is the trace of the commutator of \(H^{-1}\partial_tH\) and \(H^{-1}\partial_sH\). Integrate on the finitely many pieces in \(t\). Interior boundary terms cancel by continuity, and the endpoint terms vanish because \(H(s,0)=H(s,1)=1\). Hence \(W_\tau(u)=W_\tau(v)\).

Now take an arbitrary continuous based homotopy between two piecewise differentiable loops. Uniform continuity gives finitely many nearby time slices. Replace the intermediate slices by sufficiently close piecewise smooth loops, leaving the first and last unchanged. Consecutive replacements are close enough for (6.2), so the preceding calculation proves equality of the integrals. It proves independence of the representative for any continuous loop as well.

For products, the identity
\((uv)^{-1}(uv)'=v^{-1}u^{-1}u'v+v^{-1}v'\)
and cyclicity of the trace give additivity. Section 5 identifies this with the fundamental-group operation. Adding an identity block contributes zero to the integral, proving the stabilization assertion. \(\square\)

**Theorem 6.2.** For every type \(\mathrm{II}_1\) factor, the map


\[
W_\tau:\pi_1(U(M),1)\longrightarrow\mathbb R
\]


is an isomorphism. In particular a norm-continuous based loop is null-homotopic if and only if its trace winding is zero.

**Proof.** For a projection \(e\in M_m(M)\), direct differentiation gives


\[
W_{\tau_m}(\ell_e)=\tau_m(e).
\]


Thus the stable winding homomorphism, composed with the Bott map, is precisely the trace isomorphism \(K_0(M)\to\mathbb R\) proved in Section 5. Both Bott periodicity and the unstabilized-to-stable map (4.1) are isomorphisms, so the same is true of \(W_\tau\). \(\square\)

## 7. Normalizations and examples

A projection of trace \(r\in[0,1]\) gives a loop of winding \(r\). Every real number is obtained by concatenating finitely many such loops and their reverses. The scalar loop \(e^{2\pi it}1\) has winding \(1\); the scalar circle therefore injects on fundamental groups as \(\mathbb Z\subset\mathbb R\).

For projections \(p,q\in M\), the pointwise loop \(\ell_p\ell_q^{-1}\) is null-homotopic exactly when \(\tau(p)=\tau(q)\). The projections need not commute: additivity of the winding integral only uses cyclicity of the trace. By comparison, the condition is also exactly \(p\sim q\).

In the three-by-three corner decomposition of Section 4, with \(\tau_N=3\tau|_N\), cyclicity gives


\[
\tau(\Phi(a))=
\frac13(\operatorname{Tr}_3\otimes\tau_N)(a).
\]


Indeed off-diagonal entries have trace zero because \(v_j^*v_i=0\) for \(i\ne j\), and the trace of a diagonal entry is \(\tau(a_{ii})\). Consequently winding in \(M\) is one third of the unnormalized matrix winding over \(N\). Using a normalized matrix trace during stabilization would lose this factor.

The topology matters. The theorem above uses the operator norm at every step, especially for the logarithmic joins and the uniform inverse-square-root estimates. It is not a statement about the strong operator topology. The group \(\pi_1(U(M))\) is also a different invariant from the Murray–von Neumann fundamental group, which compares isomorphism classes of corners and amplifications of \(M\).

*Mathematical exposition by GPT-6 Astra (OpenAI), October 2026, at Ultra. CC0 1.0.*
