# Hermitian metrics and Griffiths positivity

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

A holomorphic vector bundle can be positive in two ways. Algebraically, it is *ample* if the tautological line bundle on its projectivization is ample. Differentially, it is *Griffiths-positive* if it carries a Hermitian metric whose curvature is positive in every pair of nonzero tangent and fiber directions. A Griffiths-positive bundle is ample, and Griffiths asked in 1969 whether the converse holds on smooth projective varieties [Griffiths, Problem (0.9)]. [OpenAI-GP] answers this in the negative, already in rank two on the quadric surface \(\mathbb P^1\times\mathbb P^1\). This course gives the proof.

This lesson sets up the two notions and states the theorem. The main tool for the metric side is a criterion: the dual of a Griffiths-positive metric has a plurisubharmonic squared norm on the total space of the dual bundle.

- Hermitian metrics in holomorphic frames, and frames that are normal at a point (Lemma 1.1).
- Griffiths positivity (Definition 2.1).
- The dual norm criterion (Proposition 3.1).
- Ample vector bundles (Section 4).
- The theorem and the plan of its proof (Section 5).

The lesson follows [OpenAI-GP, Sections 1 and 4]. Plurisubharmonic functions are those of the lesson [Compactness and complex-line positivity](course:AN-01/reader/AN01-U024) (course *Distributions, kernels and analytic singularities*): upper semicontinuous functions whose restrictions to complex lines are subharmonic; a \(C^2\) function is plurisubharmonic exactly when its complex Hessian is positive semidefinite (the Levi criterion, Theorem 1.1 there).

## 1. Hermitian metrics and normal frames

Let \(E\) be a holomorphic vector bundle of rank \(r\) on a complex manifold \(X\) of dimension \(n\). A *smooth Hermitian metric* \(h\) is a smooth choice of Hermitian inner products on the fibers. In a holomorphic frame \(e=(e_1,\dots,e_r)\) over an open set \(U\) with coordinates \(z_1,\dots,z_n\), a vector \(v=\sum_\alpha v_\alpha e_\alpha\) has
\[
\|v\|^2=v^*h(z)\,v ,
\]
where \(v\) also denotes the column of coefficients and \(h(z)\) is a smooth function with values in the positive definite Hermitian \(r\times r\) matrices. If \(e'=eT\) is another holomorphic frame, with \(T\) a holomorphic invertible matrix function, then the matrix in the frame \(e'\) is \(T^*hT\).

**Lemma 1.1** (normal frames). For every point \(x_0\in X\) there is a holomorphic frame near \(x_0\) in which \(h(x_0)=I\) and all first derivatives of \(h\) vanish at \(x_0\).

**Proof.** Choose coordinates with \(x_0=0\) and a holomorphic frame. A constant change of frame makes \(h(0)=I\). Write \(h_j=\partial h/\partial z_j(0)\); since \(h\) is Hermitian, \(\partial h/\partial\bar z_j(0)=h_j^*\). Put \(T(z)=I-\sum_jz_jh_j\), invertible near \(0\). Then
\[
\begin{aligned}
T^*hT&=h-\sum_jz_jh\,h_j\\
&\quad-\sum_j\bar z_jh_j^*h+O(|z|^2) .
\end{aligned}
\]
Its derivative in \(z_j\) at \(0\) is \(h_j-h_j=0\), and its derivative in \(\bar z_j\) is \(h_j^*-h_j^*=0\). \(\blacksquare\)

If \(e\) and \(e'=eT\) are both normal at \(x_0\), then \(T(x_0)\) is unitary and the first derivatives of \(T\) at \(x_0\) vanish: the holomorphic \(T\) has \(\partial T/\partial\bar z_j=0\), and the derivative of \(T^*hT\) in \(z_j\) at \(x_0\) is \(T(x_0)^*\,\partial T/\partial z_j(x_0)\). Consequently the second derivatives satisfy
\[
\begin{aligned}
&\frac{\partial^2(T^*hT)}{\partial z_j\partial\bar z_k}(x_0)\\
&\quad=T(x_0)^*\,\frac{\partial^2h}{\partial z_j\partial\bar z_k}(x_0)\,T(x_0) .
\end{aligned}
\]

## 2. Griffiths positivity

**Definition 2.1.** A smooth Hermitian metric \(h\) on \(E\) is *strictly Griffiths-positive* if for every \(x_0\in X\) and a holomorphic frame normal at \(x_0\),
\[
\sum_{j,k}\xi_j\bar\xi_k\,v^*\Bigl(-\frac{\partial^2h}{\partial z_j\partial\bar z_k}(x_0)\Bigr)v>0
\]
for all nonzero \(\xi\in\mathbb C^n\) and \(v\in\mathbb C^r\). It is *Griffiths-semipositive* if \(\ge0\) holds.

By the formula at the end of Section 1, the condition does not depend on the normal frame: changing it replaces \(v\) by \(T(x_0)v\). In a normal frame, the matrix-valued form \(-\sum_{j,k}\frac{\partial^2h}{\partial z_j\partial\bar z_k}(x_0)\,dz_j\wedge d\bar z_k\) is the curvature of the Chern connection of \(h\) at \(x_0\), up to the factor \(i\) of the convention of [OpenAI-GP, Section 1]; the definition is the usual one, but nothing below uses the Chern connection.

For a line bundle with \(h=e^{-\varphi}\) in a holomorphic frame, the condition says that \(\varphi\) is strictly plurisubharmonic (Exercise 6.1). The tautological quotient \(\mathcal O_{\mathbb P^1}(1)\), with the metric induced from \(\mathbb C^2\), is strictly Griffiths-positive (Exercise 6.2).

## 3. The dual norm criterion

The dual bundle \(E^\vee\) carries the dual metric \(\|w\|=\sup_{v\ne0}|w(v)|/\|v\|\). In the dual frame \(e^1,\dots,e^r\) of a holomorphic frame \(e\), with \(w=\sum_\alpha w_\alpha e^\alpha\) and \(w(v)=\sum_\alpha w_\alpha v_\alpha\),
\[
\|w\|^2=w^T\,h^{-1}\,\bar w=w^*\,\overline{h^{-1}}\,w ,
\]
by the Cauchy–Schwarz inequality for the inner product given by \(h\) (Exercise 6.3). So the matrix of the dual metric in the dual frame is \(g=\overline{h^{-1}}\). If \(e\) is normal at \(x_0\), so is its dual frame: \(g(x_0)=I\) and the first derivatives of \(g\) vanish there.

**Proposition 3.1** (dual norm criterion; [OpenAI-GP, Section 4]). If \(h\) is Griffiths-semipositive, then the function \(w\mapsto\|w\|^2\) is plurisubharmonic on the total space of \(E^\vee\).

**Proof.** The function is smooth, so by the Levi criterion it suffices to show that its restriction to every holomorphic disk is subharmonic. A holomorphic disk in the total space is \(\zeta\mapsto(x(\zeta),w(\zeta))\), with \(x\) holomorphic in \(X\) and \(w(\zeta)\) in the fiber over \(x(\zeta)\); in a dual holomorphic frame, \(w\) is a holomorphic column vector. Fix \(\zeta_0\), put \(x_0=x(\zeta_0)\), and use the dual of a frame normal at \(x_0\). With \(u(\zeta)=w^*g(x(\zeta))w\),
\[
\begin{aligned}
&\frac{\partial^2u}{\partial\zeta\partial\bar\zeta}(\zeta_0)=\Bigl|\frac{\partial w}{\partial\zeta}\Bigr|^2\\
&\quad+w^*\Bigl(\sum_{j,k}\xi_j\bar\xi_k\frac{\partial^2g}{\partial z_j\partial\bar z_k}(x_0)\Bigr)w ,
\end{aligned}
\]
where \(\xi=x'(\zeta_0)\), because \(g(x_0)=I\), its first derivatives vanish, and \(w\) is holomorphic. Since \(h\) and its first derivatives at \(x_0\) are \(I\) and \(0\), the second derivatives of \(h^{-1}\) at \(x_0\) are those of \(-h\). So \(\frac{\partial^2g}{\partial z_j\partial\bar z_k}(x_0)=-\overline{\frac{\partial^2h}{\partial z_k\partial\bar z_j}(x_0)}\), and with \(v=\bar w\),
\[
\begin{aligned}
&w^*\Bigl(\sum_{j,k}\xi_j\bar\xi_k\frac{\partial^2g}{\partial z_j\partial\bar z_k}\Bigr)w\\
&\quad=\overline{\sum_{j,k}\xi_k\bar\xi_j\,v^*\Bigl(-\frac{\partial^2h}{\partial z_k\partial\bar z_j}\Bigr)v}\ge0 .
\end{aligned}
\]
So \(u\) has nonnegative Laplacian at every point and is subharmonic. \(\blacksquare\)

The same computation shows that a Griffiths-positive metric makes the squared norms of all holomorphic sections of \(E^\vee\) plurisubharmonic. Only the squared norm on the total space is used below; it is a function that is a positive definite Hermitian quadratic form on each fiber.

## 4. Ample vector bundles

For a vector bundle \(V\) on a scheme \(S\), let \(\mathbb P(V)\) be the projective bundle of one-dimensional quotients of the fibers, with projection \(\pi\colon\mathbb P(V)\to S\) and tautological quotient \(\pi^*V\to\mathcal O_{\mathbb P(V)}(1)\) (Theorem 4.1 of [Projective space, relative Proj and maps to projective space](course:AG-SS/projective-space-relative-proj-and-maps-to-projective-space), course *Sheaves and schemes*). For a line bundle \(L\), \(\mathbb P(V\otimes L)=\mathbb P(V)\) with \(\mathcal O_{\mathbb P(V\otimes L)}(1)=\mathcal O_{\mathbb P(V)}(1)\otimes\pi^*L\).

**Definition 4.1** ([Ha66, Section 3]). A vector bundle \(V\) on a projective variety is *ample* if \(\mathcal O_{\mathbb P(V)}(1)\) is an ample line bundle on \(\mathbb P(V)\).

For a line bundle this is ordinary ampleness. If some power \(\mathcal O_{\mathbb P(V)}(n)\), \(n\ge1\), is very ample, then \(V\) is ample (Proposition 1.2 of [Ample invertible sheaves](course:AG-MO/ample-invertible-sheaves), course *Morphisms of schemes*, with Theorem 4.2 there). That a Griffiths-positive bundle is ample is classical [Griffiths]; it is not used in this course.

## 5. The theorem

Let \(S=\mathbb P^1\times\mathbb P^1\), with projections \(p_1,p_2\), \(\mathcal O_S(r,t)=p_1^*\mathcal O(r)\otimes p_2^*\mathcal O(t)\), and \(P=\mathcal O_S(1,1)\). Let \(f_m\colon S\to S\) raise the homogeneous coordinates in each factor to the \(m\)th power,
\[
\begin{aligned}
&f_m\bigl([z_0:z_1],[w_0:w_1]\bigr)\\
&\quad=\bigl([z_0^m:z_1^m],[w_0^m:w_1^m]\bigr) .
\end{aligned}
\]
It is finite of degree \(m^2\), and \(f_m^*\mathcal O_S(r,t)\cong\mathcal O_S(mr,mt)\).

**Theorem 5.1** ([OpenAI-GP, Theorem 1.1]). There is an algebraic vector bundle \(G\) of rank two on \(S\) such that \(E_m=f_m^*G\otimes P\) is ample for every \(m\ge1\), and there is an integer \(m_0\) such that \(E_m\) has no smooth strictly Griffiths-positive Hermitian metric for every \(m\ge m_0\).

So Griffiths' conjecture fails in rank two on the quadric surface. The proof has four parts, one per lesson.

- [A bundle glued along three graphs](a-bundle-glued-along-three-graphs.md) constructs \(G\) from the graphs of three projective transformations of \(\mathbb P^1\), chosen so that their lifts to \(\mathbb C^2\) have finite relative orders while their product expands.
- [Ampleness of the power family](ampleness-of-the-power-family.md) proves that \(\mathcal O_{\mathbb P(E_m)}(n)\) is very ample for every even \(n\) with \(n-1\ge3m\).
- [A quadratic limit of dual norms](a-quadratic-limit-of-dual-norms.md) shows that positive metrics on infinitely many \(E_m\) would produce, in the limit, a nonzero plurisubharmonic function on the total space of \(G^\vee\) that is quadratic on every fiber.
- [An invariant measure and the proof](an-invariant-measure-and-the-proof.md) shows that such a function would give a nonzero measure on \(\mathbb P^1\) invariant under two transformations that have no common invariant measure, and proves the theorem.

The value of \(m_0\) is obtained by compactness and is not effective.

**Context.** This paragraph is background and is not used. For line bundles the two notions agree, and on curves ampleness is characterized by the positivity of the degrees of all quotient bundles; on curves every ample bundle carries a Griffiths-positive metric (Umemura; Campana and Flenner). Berndtsson proved that \(E\otimes\det E\) is Nakano-positive for ample \(E\), and Liu, Sun and Yang treated symmetric powers; these do not give a metric on \(E\) itself [OpenAI-GP, Section 1]. Independently of the theorem of this course, Du and Xie constructed a rank-two ample bundle on the abelian surface \(C\times C\), where \(C\) is the elliptic curve \(y^2=x^3-x\), with no smooth Griffiths-semipositive metric [Du–Xie 2026a, Theorem 1.1], and characterized Griffiths positivity on smooth projective varieties by a convex condition on first jets of sections of positive twists [Du–Xie 2026b]. Liu and Wan constructed, on every Hirzebruch surface, stable ample rank-two bundles with no smooth strongly pseudoconvex Finsler metric of semipositive Kobayashi curvature, which answers a problem of Kobayashi in the negative [Liu–Wan 2026, Theorem 1.1]. Another conjecture of Griffiths, that every positive polynomial in the Chern forms of a Griffiths-positive metric is a positive form, fails as well: for every \(r\geq9\), Du constructed a Griffiths-positive metric on \(\mathcal O_{\mathbb P^r}(1)^{\oplus r}\) whose top Chern form is negative on a nonempty open set [Du 2026, Theorem 1.1].

## 6. Exercises

**6.1.** Let \(L\) be a line bundle with metric \(h=e^{-\varphi}\) in a holomorphic frame. Show that \(h\) is strictly Griffiths-positive exactly when the complex Hessian of \(\varphi\) is positive definite at every point.

**6.2.** On \(\mathbb P^1\), the tautological line bundle \(\mathcal O(-1)\subset\mathbb P^1\times\mathbb C^2\) has the frame \(e(z)=(1,z)\) over \(\{[1:z]\}\), with \(\|e\|^2=1+|z|^2\). Show that the dual metric on \(\mathcal O(1)\) is strictly Griffiths-positive, and that the squared norm on the total space of \(\mathcal O(-1)\) is the pullback of \(|w_0|^2+|w_1|^2\) under the map to \(\mathbb C^2\).

**6.3.** Prove the formula \(\|w\|^2=w^T h^{-1}\bar w\) for the dual metric.

**6.4.** Show that the Hermitian metric \(h(z)=\begin{pmatrix}1&\bar z\\z&1+2|z|^2\end{pmatrix}\) on the trivial bundle of rank two over the unit disk is positive definite, find a frame normal at \(0\), and decide whether \(h\) is Griffiths-positive at \(0\).

**6.5.** Let \(V=\mathcal O\oplus\mathcal O(1)\) on \(\mathbb P^1\). Show that \(V\) is not ample, by finding a curve in \(\mathbb P(V)\) on which \(\mathcal O_{\mathbb P(V)}(1)\) is trivial.

## 7. Solutions

**6.1.** A holomorphic change of frame by a nonvanishing holomorphic function \(f\) multiplies \(h\) by \(|f|^2\), which changes \(\varphi\) by the pluriharmonic function \(-\log|f|^2\) and does not change its complex Hessian. Near a point, take \(f=c\,e^{q}\) with a constant \(c\) and a holomorphic polynomial \(q\) of degree one such that \(\psi=\varphi-\log|f|^2\) vanishes with its first derivatives at the point; this is possible because \(\varphi\) is real, so its linear part is \(2\operatorname{Re}\) of a holomorphic linear form. Then \(h=e^{-\psi}\) is normal there, \(e^{-\psi}=1-\psi+O(|z|^3)\), and \(-\partial_j\bar\partial_ke^{-\psi}=\partial_j\bar\partial_k\psi=\partial_j\bar\partial_k\varphi\) at the point.

**6.2.** The dual frame \(e^\vee\) of \(\mathcal O(1)\) has \(\|e^\vee\|^2=1/(1+|z|^2)\), which is \(1-|z|^2+O(|z|^4)\), already normal at \(z=0\), with \(-\partial\bar\partial(1/(1+|z|^2))(0)=1>0\); the group of unitary transformations of \(\mathbb C^2\) acts transitively on \(\mathbb P^1\) and preserves the metric, so the same holds at every point. A point of the total space of \(\mathcal O(-1)\) over \([1:z]\) is \(w\,e(z)=(w,wz)\in\mathbb C^2\), and \(|w|^2(1+|z|^2)=|w|^2+|wz|^2\).

**6.3.** Write \(v=h^{-1/2}u\), so that \(\|v\|^2=|u|^2\) and \(w(v)=w^Th^{-1/2}u\). The supremum of \(|w^Th^{-1/2}u|^2/|u|^2\) is the squared length of the row vector \(w^Th^{-1/2}\), which is \(w^Th^{-1/2}(h^{-1/2})^*\bar w=w^Th^{-1}\bar w\). Since \(h^{-1}\) is Hermitian, this equals \(w^*\,\overline{h^{-1}}\,w\).

**6.4.** The determinant is \(1+2|z|^2-|z|^2=1+|z|^2>0\) and the diagonal entries are positive, so \(h\) is positive definite. Write \(h=I+zN+\bar zN^*+|z|^2M\) with \(N=\begin{pmatrix}0&0\\1&0\end{pmatrix}\) and \(M=\operatorname{diag}(0,2)\). With \(T=I-zN\) as in Lemma 1.1, expanding \((I-\bar zN^*)\,h\,(I-zN)\) and using \(N^2=0\) gives a matrix \(I+|z|^2(M-N^*N)+O(|z|^3)\), normal at \(0\), with \(N^*N=\operatorname{diag}(1,0)\). So in this frame \(-\partial_z\partial_{\bar z}\) of the matrix at \(0\) is \(\operatorname{diag}(1,-2)\): positive on the first frame vector and negative on the second. So \(h\) is not Griffiths-semipositive at \(0\).

**6.5.** The quotient \(V\to\mathcal O\) defines a section \(\sigma\colon\mathbb P^1\to\mathbb P(V)\) with \(\sigma^*\mathcal O_{\mathbb P(V)}(1)=\mathcal O\) (Theorem 4.1 of the lesson on projective space). An ample line bundle restricts to an ample line bundle on the curve \(\sigma(\mathbb P^1)\cong\mathbb P^1\), and the trivial bundle on \(\mathbb P^1\) is not ample.

## References

- [OpenAI-GP] OpenAI, *Ample rank-two bundles on the quadric surface without Griffiths-positive metrics*, OpenAI Math Release preprint, 24 September 2026, Sections 1 and 4. https://github.com/openai/math/tree/main/preprints/ample-rank-two-bundles-on-the-quadric-surface-without-griffiths-positive-metrics-September-24-2026
- [Griffiths] P. A. Griffiths, *Hermitian differential geometry, Chern classes, and positive vector bundles*, in: Global Analysis (Papers in Honor of K. Kodaira), 1969, 185–251, Problem (0.9). https://publications.ias.edu/node/185
- [Du–Xie 2026a] Y.-H. Du and S.-Y. Xie, *Ample vector bundles without Griffiths-semipositive metrics*, arXiv:2609.26504 (September 2026), Theorem 1.1. https://arxiv.org/abs/2609.26504
- [Du–Xie 2026b] Y.-H. Du and S.-Y. Xie, *A first-jet characterization of Griffiths positivity*, arXiv:2609.26528 (September 2026). https://arxiv.org/abs/2609.26528
- [Liu–Wan 2026] K. Liu and X. Wan, *Stable ample vector bundles without semipositive Kobayashi curvature*, arXiv:2609.37309 (September 2026), Theorem 1.1. https://arxiv.org/abs/2609.37309
- [Du 2026] Y.-H. Du, *Griffiths positivity does not imply positivity of the top Chern form*, arXiv:2610.05931 (October 2026), Theorem 1.1. https://arxiv.org/abs/2610.05931
- [Ha66] R. Hartshorne, *Ample vector bundles*, Publ. Math. IHÉS 29 (1966), 63–94, Section 3. https://www.numdam.org/item/PMIHES_1966__29__63_0/
