# Involutive subsets of subanalytic isotropic sets

Involutivity says that Hamiltonian directions forced by vanishing secants remain tangent to a set. Isotropy puts an upper bound on dimension. When an involutive set lies inside a subanalytic isotropic set, these two requirements leave no room for a hidden lower-dimensional residue: the subset becomes subanalytic and Lagrangian, even though its subanalyticity was not assumed.

We work on \(P=T^*X\), where \(X\) is a real analytic \(n\)-manifold, Hausdorff and countable at infinity. Use \(\alpha=\sum_i\xi_i dx_i\) and \(\omega=d\alpha=\sum_i d\xi_i\wedge dx_i\). Positive conicity means invariance under positive fibre dilation. Isotropy for a subanalytic cotangent set means that its canonical one-form vanishes in the singular one-form sense developed in Isotropic cotangent transport and discrete critical values.

Kashiwara and Schapira, [*Microlocal Study of Sheaves*, Astérisque 128 (1985)](https://www.numdam.org/item/AST_1985__128__1_0/), treat conic isotropy and the selection of Lagrangian pieces. We work with regular components and singular residues of a locally closed isotropic containing set. The local flow construction and tangent-field argument below turn the secant condition into invariance. For bounded sheaf complexes over arbitrary commutative rings, microsupport involutivity supplies this geometric argument with an involutive closed set. That sheaf-theoretic proof uses the directional identity and an empty-cone contradiction; it does not depend on the subanalytic recovery theorem below.

## Exact inputs and the scope of the argument {#geometric-proof-inputs}

The flow argument uses finite-dimensional coordinate calculus, completeness of the continuous-path space, compactness, integration of continuous functions, and the inverse function theorem. Its existence, uniqueness, differentiable dependence and closed-set invariance steps are proved below. No theorem about microsupport is an input: involutivity is an explicit hypothesis on the subset.

The final two subanalytic arguments have further precise inputs. A subanalytic set has a relatively open subanalytic regular locus, and the complement has strictly smaller dimension; its connected components are subanalytic and form an **ambient locally finite** family. Closures, finite Boolean operations and locally finite unions preserve subanalyticity, and analytic curve selection gives the singular one-form calculus. These foundational subanalytic results remain prerequisites, recorded in Finite conormal closures and generic base directions. Naming them does not supply their proofs.

Given those inputs, the companion cotangent reading proves that canonical-form vanishing restricts to subanalytic subsets and passes to closures, and that positive-conic canonical-form isotropy gives symplectic isotropy. The dimension bound follows directly: an isotropic tangent space \(W\) satisfies \(W\subset W^\omega\), while nondegeneracy gives \(\dim W^\omega=2n-\dim W\). Hence \(\dim W\le n\); taking the supremum over the regular locus gives the subanalytic dimension bound. These are the exact geometric consequences used below. The resulting theorem is proved relative to the stated inputs, with their remaining foundational work visible.

## Secants and the Hamiltonian sign

For a locally closed subset \(S\subset P\), the point and two-set normal cones are

\[
C_p(S)=\left\{\lim_k\frac{s_k-p}{h_k}:s_k\in S,\ s_k\to p,\ h_k\downarrow0\right\},
\qquad
C_p(S,S)=\left\{\lim_k\frac{s_k-t_k}{h_k}:s_k,t_k\in S,\ s_k,t_k\to p,\ h_k\downarrow0\right\}.
\tag{1}
\]

Only convergent quotients enter. Coordinates identify these limits with tangent vectors; the normal-geometry coordinate comparison makes the definitions invariant. The first set in the ordered pair contributes with a plus sign.

Define the Hamiltonian isomorphism \(H:T^*P\to TP\) by

\[
H\left(\sum_i a_i dx_i+b_i d\xi_i\right)
=\sum_i b_i\partial_{x_i}-a_i\partial_{\xi_i},
\qquad \iota_{H\theta}\omega=-\theta.
\tag{2}
\]

The subset \(S\) is **involutive at \(p\in S\)** if

\[
C_p(S,S)\subset\ker\theta
\quad\Longrightarrow\quad
-H\theta\in C_p(S)
\quad\text{for every }\theta\in T_p^*P.
\tag{3}
\]

It is involutive if this holds at all its points. Applying (3) to both \(\theta\) and \(-\theta\) also puts \(H\theta\) in \(C_p(S)\). This does not change the sign convention in (2).

For a smooth submanifold \(S\), both cones in (1) equal \(T_pS\). Since \(H\) takes the annihilator of \(T_pS\) to its symplectic orthogonal, (3) is equivalent to

\[
(T_pS)^\omega\subset T_pS.
\tag{4}
\]

Thus a smooth involutive manifold is coisotropic. A smooth isotropic manifold satisfies the reverse inclusion. Both together imply equality and dimension \(n\).

## The precise flow prerequisite

If \(S\) is involutive and **closed in an open subset** \(U\subset P\), and \(\varphi\in C^2(U;\mathbb R)\) vanishes on \(S\), then every maximal Hamiltonian trajectory through a point of \(S\) remains in \(S\) as long as it exists in \(U\). Its equations are

\[
\dot x_i=\partial_{\xi_i}\varphi,\qquad
\dot\xi_i=-\partial_{x_i}\varphi.
\tag{5}
\]

We now prove this statement, including both time directions. There is no completeness or global compactness hypothesis on the field or the set. A critical point of \(\varphi\) gives a constant trajectory.

### Differentiating two moving endpoints {#secants-and-vanishing-functions}

Work in a convex coordinate ball. For a \(C^1\) map \(f\), two endpoints \(s_j,t_j\to p\) satisfy

\[
\begin{aligned}
f(s_j)-f(t_j)&=df_p(s_j-t_j)+r_j,\\
|r_j|&\le \sup_{z\in[s_j,t_j]}\|df_z-df_p\|\,|s_j-t_j|.
\end{aligned}
\tag{F1}
\]

If \((s_j-t_j)/h_j\) converges, dividing the remainder by \(h_j\) makes it tend to zero. Applying this to a coordinate change and its inverse proves that both cones in (1) transform by its derivative. The cones are also unchanged by restricting to an ambient open neighborhood of \(p\). Thus the coordinate computations below prove intrinsic assertions.

If \(f=\varphi\) vanishes on \(S\), the left side of (F1) is zero for endpoints in \(S\), so \(d\varphi_p\) annihilates \(C_p(S,S)\). The estimate uses the distance **between** the endpoints; separate Taylor remainders at \(p\) would not control division by \(h_j\). Testing (3) with both signs of \(d\varphi_p\) puts both signs of the Hamiltonian vector in \(C_p(S)\).

### Constructing the local flow and its differential {#local-c1-flow}

Let \(V\) be a \(C^1\) vector field on an open subset of \(\mathbb R^m\). Take \(\overline B(p,2r)\) inside the domain and bounds \(M\ge |V|\), \(L\ge\|DV\|\) on this ball. Choose \(T>0\) with \(TM<r\) and \(TL<1\); when one bound is zero its inequality imposes no restriction. For \(z\in B(p,r)\), the map

\[
(\mathcal P_z c)(t)=z+\int_0^t V(c(s))\,ds,
\qquad -T\le t\le T
\tag{F2}
\]

preserves the complete uniform-norm space of continuous paths taking values in \(\overline B(p,2r)\). It is a contraction of constant \(TL\). Starting with any path, successive iterates have differences bounded by a geometric series, so they converge uniformly. The integral passes to the limit and gives a fixed point \(\Phi(\cdot,z)\). The same contraction inequality proves uniqueness within this ball. The integral equation gives \(\partial_t\Phi=V(\Phi)\); subdividing a common existence interval gives uniqueness on that whole interval.

For nearby initial points the two equations give

\[
\|\Phi(\cdot,z+h)-\Phi(\cdot,z)\|_\infty
\le \frac{|h|}{1-TL}.
\tag{F3}
\]

To prove the differentiability needed for the later openness argument, solve the matrix equation

\[
U_z(t)=I+\int_0^t DV(\Phi(s,z))U_z(s)\,ds.
\tag{F4}
\]

This is another contraction of constant \(TL\), now on all continuous matrix-valued functions. Its solutions are bounded by \((1-TL)^{-1}\). They depend continuously on \(z\): subtracting two equations bounds their difference by \(TL\) times that difference plus a term tending uniformly to zero, using (F3) and uniform continuity of \(DV\).

Write \(\delta_h(t)=\Phi(t,z+h)-\Phi(t,z)\). Uniform continuity of \(DV\), the mean-value integral and (F3) give, uniformly in \(s\),

\[
\begin{aligned}
V(\Phi(s,z+h))-V(\Phi(s,z))-DV(\Phi(s,z))\delta_h(s)&=o(|h|),\\
\|\delta_h-U_zh\|_\infty&\le TL\|\delta_h-U_zh\|_\infty+o(|h|).
\end{aligned}
\tag{F5}
\]

The second line follows by subtracting (F4), multiplied by \(h\), from the two trajectory equations. Therefore \(D_z\Phi(t,z)=U_z(t)\), continuously in \((t,z)\). Together with the time derivative, this proves joint \(C^1\) regularity. Uniqueness gives the local composition law \(\Phi(t,\Phi(s,z))=\Phi(t+s,z)\). Local solutions glue uniquely to the maximal open interval through zero. Coordinate changes preserve the equation, so the construction also works on manifolds. A zero of \(V\) has the unique constant trajectory.

### A closed set containing its tangent field {#closed-set-tangent-invariance}

Suppose \(S\) is closed in an open manifold \(U\), and \(V\) is a \(C^1\) field on \(U\) with \(V(q)\in C_q(S)\) at every \(q\in S\). We prove that a trajectory starting in \(S\) stays there for all its nonnegative existence times.

First work near its initial point \(p\). Choose a coordinate ball \(\overline B(p,3r)\subset U\) and restrict to a short interval on which the trajectory \(x(t)\) lies in \(B(p,r)\). The set \(K=S\cap\overline B(p,3r)\) is nonempty and compact. Every nearest point \(y\in K\) to \(x(t)\) satisfies

\[
|x(t)-y|\le |x(t)-p|<r,
\qquad |y-p|<2r.
\tag{F6}
\]

Thus the nearest point never meets the artificial boundary of the cutoff ball. The tangent-cone hypothesis gives points of \(S\) with

\[
y_j=y+h_jV(y)+o(h_j),\qquad h_j\downarrow0;
\quad y_j\in K\text{ for all sufficiently large }j.
\tag{F7}
\]

Minimality gives \(|x-y_j|^2\ge |x-y|^2\). Subtract and divide by \(h_j\), then take the limit:

\[
\langle x-y,V(y)\rangle\le0.
\tag{F8}
\]

Let \(g(t)=\operatorname{dist}(x(t),K)^2\). At a fixed time keep this same nearest point \(y\) as a competitor at time \(t+h\). The trajectory equation and a Lipschitz constant \(L\) for \(V\) on the convex cutoff ball yield

\[
\begin{aligned}
D^+g(t)&:=\limsup_{h\downarrow0}\frac{g(t+h)-g(t)}h\\
&\le2\langle x(t)-y,V(x(t))\rangle\\
&\le2\langle x(t)-y,V(x(t))-V(y)\rangle
\le2L g(t).
\end{aligned}
\tag{F9}
\]

This controls all positive increments. The sequence in the tangent cone was used to establish the fixed inequality (F8), before taking the upper limit in (F9).

The continuous function

\[
f(t)=e^{-2Lt}g(t)\quad\text{satisfies}\quad D^+f(t)\le0.
\tag{F10}
\]

Here is the comparison argument without any differentiation almost everywhere. If \(f(b)>f(a)\), choose \(0<\varepsilon<(f(b)-f(a))/(b-a)\). The continuous function \(f(t)-\varepsilon t\) has a minimum on \([a,b]\) at some \(c<b\), because its value at \(b\) is larger than its value at \(a\). All sufficiently small positive difference quotients at \(c\) are nonnegative. This contradicts their upper limit being at most \(-\varepsilon\). Hence \(f\) is nonincreasing. Since \(g(0)=0\) and \(g\ge0\), the distance stays zero. Closedness of \(K\) gives \(x(t)\in S\) on this short interval.

For any positive time \(T\) in the maximal existence interval, take the supremum of the times up to \(T\) for which the whole initial segment stays in \(S\). A finite endpoint before \(T\) lies in \(S\) by continuity and closedness in \(U\); the local argument restarted there extends the segment, a contradiction. It therefore reaches \(T\). This proves forward invariance on the entire existence interval, without a globally compact invariant set.

### Applying the result in both Hamiltonian directions {#hamiltonian-invariance-proved}

For the function in (5), the secant calculation and involutivity give

\[
V=H(d\varphi)\in C^1(U;TU),\qquad
V(q),-V(q)\in C_q(S)\quad(q\in S).
\tag{F11}
\]

Apply the preceding proof to \(V\) and to \(-V\). Uniqueness identifies the latter trajectory with negative time for the former. This proves (5) in both time directions through every initial point of \(S\), including critical points. The condition is closedness **in the actual flow domain**. For example, the punctured zero section in \(T^*\mathbb R\) is locally Lagrangian, but translation by \(H(d\xi)=\partial_x\) can pass through its missing point if the ambient domain includes that point. Choose a domain in which the set is closed before applying the theorem.

## A closed involutive subset of a smooth isotropic manifold

Let \(N\subset P\) be a smooth locally closed isotropic submanifold. Let \(S\subset N\) be a subset closed in \(N\), and suppose \(S\) is involutive as a locally closed subset of \(P\). Then \(S\) is open in \(N\). At every point of nonempty \(S\), the local dimension of \(N\) and \(S\) is \(n\).

Here isotropic for \(N\) means \(\omega|_{TN}=0\). The assertion holds in this smooth symplectic form, and hence also for the regular locus of a conic isotropic cotangent set.

**Proof.** Fix \(p\in S\). Since \(S\subset N\), straightening \(N\) gives

\[
C_p(S,S)\subset T_pN,\qquad C_p(S)\subset T_pN.
\tag{6}
\]

For every covector \(\theta\) annihilating \(T_pN\), equations (3) and (6) imply \(H\theta\in T_pN\). Therefore

\[
(T_pN)^\omega\subset T_pN.
\tag{7}
\]

Isotropy gives \(T_pN\subset(T_pN)^\omega\). Thus equality holds, and \(\dim T_pN=n\). Shrink to a smooth local piece of \(N\) of this dimension. It is itself Lagrangian; no enlargement of \(N\) is needed.

Choose an open neighborhood \(U\) of \(p\) where \(N\) is closed and is cut out by smooth independent functions \(\varphi_1,\ldots,\varphi_n\). Since \(S\) is closed in \(N\), it is closed in this \(U\). Each \(\varphi_i\) vanishes on \(S\), so its local Hamiltonian flow preserves \(S\).

Along \(N\), the differentials \(d\varphi_i\) form a basis of its conormal space. Equation (2) and the Lagrangian equality take them to a basis of \(TN\). Thus the Hamiltonian fields also preserve \(N\). For their local flows \(\Phi_i^{t_i}\), consider

\[
F(t_1,\ldots,t_n)
=\Phi_n^{t_n}\circ\cdots\circ\Phi_1^{t_1}(p).
\tag{8}
\]

For sufficiently small times all stages remain in \(U\), and flow invariance puts their endpoints in \(S\). The differential at zero sends the \(i\)-th coordinate vector to \(H_{\varphi_i}(p)\), so it is an isomorphism to \(T_pN\). The inverse function theorem makes the image of a small time neighborhood a neighborhood of \(p\) in \(N\). It lies in \(S\), proving openness. The dimension assertion follows there. If \(n=0\), the same conclusion follows from the zero-dimensional local neighborhood. \(\square\)

The dimension assertion is pointwise where \(S\) is nonempty. An empty subset is always open and has no point at which to assert dimension \(n\). Also, the dimension in this cotangent setting is the dimension of the **base** \(X\), half the symplectic ambient dimension \(2n\).

## No involutive subset can hide below half dimension

Let \(A\subset T^*X\) be a locally closed positive-conic subanalytic isotropic set with

\[
\dim A<n.
\tag{9}
\]

If \(V\subset A\) is locally closed in \(T^*X\) and involutive, then \(V=\varnothing\). No subanalyticity, conicity, or global closedness in \(A\) is assumed for \(V\).

**Proof.** Induct on \(\dim A\). The empty containing set is immediate. If \(p\in V\cap A_{\mathrm{reg}}\), choose a sufficiently small ambient neighborhood where \(A\) is a closed analytic submanifold and where \(V\) is closed. This is possible by regularity and local closedness. The regular piece of \(A\) is symplectically isotropic: positive conicity and canonical-form vanishing imply \(\omega|_{TA_{\mathrm{reg}}}=0\), as proved by the Euler-field argument in the cotangent reading. The smooth result would force its dimension to be \(n\), contradicting (9). Thus

\[
V\cap A_{\mathrm{reg}}=\varnothing.
\tag{10}
\]

Set \(A_1=A\setminus A_{\mathrm{reg}}\). This is subanalytic, closed in \(A\), and hence locally closed. It is positive-conic because regularity is preserved by each dilation diffeomorphism. Canonical-form vanishing passes to this subanalytic subset, so it is isotropic. Its dimension is strictly smaller by the dimension prerequisite (2) of the preceding lesson. We have \(V\subset A_1\), with the same local closedness and involutivity as before. Induction proves that it is empty. \(\square\)

The argument does not assume that \(V\) has regular points. It uses regularity only on the subanalytic containing set and descends through its singular residues.

## Subanalyticity forced by an isotropic containing set

Let \(\Lambda\subset\Lambda_0\subset T^*X\) be locally closed positive-conic subsets. Assume:

1. \(\Lambda_0\) is subanalytic and isotropic;
2. \(\Lambda\) is closed in \(\Lambda_0\);
3. \(\Lambda\) is involutive.

Then \(\Lambda\) is subanalytic and **Lagrangian**, meaning isotropic and involutive. The theorem does not assume \(\Lambda\) subanalytic.

**Proof.** Put

\[
R=(\Lambda_0)_{\mathrm{reg}},\qquad B=\Lambda\cap R.
\tag{11}
\]

The smooth result shows that \(B\) is open in \(R\). In applying it locally, \(R\) agrees with \(\Lambda_0\), so \(B\) is a local open restriction of the involutive set \(\Lambda\); involutivity is unchanged. Relative closedness of \(\Lambda\) also makes \(B\) closed in \(R\). Consequently \(B\) is a union of connected components of \(R\).

The components of a subanalytic set are subanalytic and ambient locally finite. Any subfamily is still locally finite; its union is subanalytic by the local finite-union calculus. Thus \(B\) is subanalytic. Relative closedness gives

\[
\overline B\cap\Lambda_0\subset\Lambda.
\tag{12}
\]

We prove the reverse inclusion. Consider the possible leftover

\[
V=\Lambda\setminus\overline B.
\tag{13}
\]

It is an open restriction of the locally closed involutive set \(\Lambda\), so it is locally closed and involutive. Equation (11) gives

\[
V\subset\Lambda_0\setminus R.
\tag{14}
\]

The dimension argument above gives \(\dim\Lambda_0\le n\). If \(\Lambda_0\ne\varnothing\), its singular residue is subanalytic, positive-conic and isotropic, and has dimension strictly less than \(\dim\Lambda_0\), hence strictly less than \(n\). The previous result makes \(V\) empty. The empty \(\Lambda_0\) case is immediate. Therefore

\[
\Lambda=\overline B\cap\Lambda_0.
\tag{15}
\]

Closure and intersection preserve subanalyticity, so \(\Lambda\) is subanalytic. Canonical-form vanishing on \(\Lambda_0\) passes to its subanalytic subset \(\Lambda\), proving isotropy. Involutivity was assumed. These are exactly the stated Lagrangian conditions. \(\square\)

Formula (15) identifies what has been recovered: the selected regular components, together with precisely their limits that lie in the given locally closed containing set. Limits outside \(\Lambda_0\) are not inserted. A globally closed containing set is not required.

## Exercises with complete solutions

### A truncated zero section loses a Hamiltonian direction

*Difficulty: Introductory.*

In \(T^*\mathbb R\), let \(S=\{(x;0):x\ge0\}\). Compute both cones at \(p=(0;0)\) and test (3).

**Solution.** The point cone is \(C_p(S)=\{a\partial_x:a\ge0\}\). The two-set cone is the full line \(\mathbb R\partial_x\): differences of two nonnegative base points can have either sign. Take \(\theta=d\xi\), which annihilates this line. Equation (2) gives \(H\theta=\partial_x\), so \(-H\theta=-\partial_x\notin C_p(S)\). Hence \(S\) is not involutive at its endpoint. It is closed in the isotropic zero section, but the failed direction prevents application of the openness theorem.

### The smooth dimension bound needs no normal-form enlargement

*Difficulty: Intermediate.*

Let \(S\) be involutive and contained in a smooth isotropic \(m\)-manifold \(N\subset T^*X\). Show at any \(p\in S\) that \(m=n\), using only cones and symplectic linear algebra. Does this argument need relative closedness?

**Solution.** Inclusion gives both cones in (6). Every \(\theta\in(T_pN)^\perp\) annihilates the two-set cone, so involutivity puts \(H\theta\) in \(T_pN\). The image of this annihilator under \(H\) is \((T_pN)^\omega\), of dimension \(2n-m\). Thus \(2n-m\le m\). Isotropy gives \(m\le n\), so \(m=n\), and both tangent subspaces are equal. This pointwise argument needs no relative closedness. Closedness in a local ambient neighborhood is needed for the Hamiltonian-flow invariance step that subsequently proves openness of \(S\).

### Which components of a discrete conormal may be retained?

*Difficulty: Intermediate.*

Let \(\Lambda_0=T_{\mathbb Z}^*\mathbb R\). For an arbitrary subset \(J\subset\mathbb Z\), set \(\Lambda=\bigcup_{m\in J}T_m^*\mathbb R\). Verify the theorem's hypotheses and its conclusion. What changes if one retains only a half-fibre at some integer?

**Solution.** The family of integer fibres is ambient locally finite. Each fibre is a smooth closed conormal line, with zero canonical form and Lagrangian tangent space; hence it is involutive. Near each point of \(\Lambda\), no other integer fibre occurs, so \(\Lambda\) is locally closed and involutive. Any subfamily is closed in the full locally finite union \(\Lambda_0\), and both sets are positive-conic. The theorem applies; directly, the same local finiteness makes \(\Lambda\) subanalytic and Lagrangian. No finiteness condition on \(J\) is required.

For the half-fibre \(\{(m;\xi):\xi\ge0\}\), at \(\xi=0\) the point cone is the positive \(\partial_\xi\) ray and the two-set cone is its full line. A base covector \(dx\) annihilates that line, while \(H(dx)=-\partial_\xi\) is absent from the point cone. Applying (3) also to \(-dx\) forces that missing sign. Thus the retained half-fibre is not involutive at zero.

### A singular containing set cannot support an isolated involutive point

*Difficulty: Intermediate.*

In \(T^*\mathbb R\), let \(\Lambda_0=\{\xi=0\}\cup\{x=0\}\) and \(\Lambda=\{(0;0)\}\). Check relative closedness and conicity, and locate the failed hypothesis in the main theorem.

**Solution.** The containing crossing is closed, subanalytic and positive-conic. Its regular pieces are the punctured horizontal and vertical lines, on which the canonical form vanishes; hence it is isotropic. The singleton is closed in it and positive-conic. At the singleton both cones are \(\{0\}\). Every cotangent covector annihilates the two-set cone, but any nonzero \(\theta\) has \(H\theta\ne0\), which cannot belong to the point cone. Involutivity fails. Formula (15) would give an empty subset because the singleton meets no regular component. The lower-dimensional residue is exactly what involutivity rules out.

### A locally closed conormal requires intersection with the containing set

*Difficulty: Advanced.*

Let \(N=\{(x,0):x>0\}\subset\mathbb R^2\), \(\Lambda_0=T_N^*\mathbb R^2\), and \(\Lambda=\Lambda_0\). Verify the hypotheses and compare \(\Lambda\) with the two expressions \(\overline{\Lambda}\) and \(\overline{\Lambda}\cap\Lambda_0\).

**Solution.** The base \(N\) is an analytic submanifold, closed in the open region \(x>0\). Its conormal is \(\{x>0,y=0,a=0\}\), with \(b\) arbitrary in the covector \(a\,dx+b\,dy\). It is locally closed, subanalytic and positive-conic. It is smoothly Lagrangian, so it is isotropic and involutive, and is closed in itself. All hypotheses hold.

Its ambient closure adds \(\{x=0,y=0,a=0\}\), including every finite \(b\). Those points are outside \(\Lambda_0\). Since here every point of \(\Lambda_0\) is regular, \(B=\Lambda_0\), and the exact recovery formula is \(\Lambda=\overline B\cap\Lambda_0\). Omitting the intersection would change the subset and its projected base.

### The finite family of flow directions fills the Lagrangian

*Difficulty: Advanced.*

In \(T^*\mathbb R^n\), take the zero section \(L=\{\xi=0\}\). Write the functions and flow composition in (8) explicitly. Deduce that a closed involutive subset of \(L\) is a union of its connected components. Explain the local version when the ambient open set has a restricted existence interval.

**Solution.** Set \(\varphi_i=\xi_i\). Equation (2) gives \(H_{\varphi_i}=\partial_{x_i}\), whose flow is translation by \(t_i e_i\) in the base, keeping \(\xi\) fixed. At \(p=(x;0)\), the composition is \(F(t)=(x+t;0)\). If a subset \(S\) is closed and involutive, each of these flows preserves it, so all sufficiently small \(t\) give points in \(S\). It is therefore open in \(L\), as well as closed. It is a union of connected components; since this particular \(L\) is connected, it is either empty or the whole zero section.

In a smaller ambient open set, translations are used only for the short times during which every stage remains in that set. This still fills a local neighborhood in \(L\) and proves openness. Extending beyond the maximal existence interval is unnecessary and is not asserted.

### Why a continuous tangent field is insufficient

*Difficulty: Intermediate.*

On \(\mathbb R\), let \(S=\{0\}\) and \(V(x)=2\sqrt{|x|}\). Check that both signs of \(V\) belong to the point tangent cone along \(S\), yet an actual trajectory starting in \(S\) can leave it. Locate the missing hypothesis in the proof.

**Solution.** At the only point of \(S\), the tangent cone is \(\{0\}\) and \(V(0)=0\). Nevertheless,

\[
x(t)=\begin{cases}0,&t\le0,\\t^2,&t\ge0\end{cases}
\quad\text{satisfies}\quad x'(t)=2\sqrt{|x(t)|},\qquad x(0)=0.
\tag{F12}
\]

The curve is \(C^1\) at zero and leaves \(S\) for every positive time. The constant curve is another solution. The field is continuous but not locally Lipschitz at zero: \(|V(h)-V(0)|/|h|=2/\sqrt{|h|}\) is unbounded. Thus neither the contraction uniqueness argument nor the Lipschitz estimate in (F9) applies. A \(C^2\) Hamiltonian supplies a \(C^1\) field, which excludes this example.

## The resulting Lagrangian notion

For a conic subanalytic cotangent set, Lagrangian means canonical-form isotropy together with the singular involutivity test (3). At its regular points this is the usual dimension-\(n\) Lagrangian condition. The theorem shows how a subset initially lacking subanalytic regularity acquires it from a subanalytic isotropic containing set, while retaining the exact local closedness and Hamiltonian information.
