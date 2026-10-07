# Jacobi fields, conjugate points and the Morse index theorem

A Jacobi field records the first-order change of a geodesic. The index form records the second-order change of its energy. We connect these two descriptions through a finite space of interpolating Jacobi fields, prove the Morse and spectral index formulas, and keep track of endpoint and torsion terms.

All manifolds are smooth, Hausdorff and second countable. Piecewise smooth paths and fields are continuous and, on each closed interval in a finite subdivision, are restrictions of smooth maps on a neighbourhood of that interval. A variation has one fixed subdivision on which it is smooth in both parameters in this same sense. The curvature convention is
\[
R(X,Y)Z=\nabla_X\nabla_YZ-\nabla_Y\nabla_XZ-\nabla_{[X,Y]}Z.
\]
Primes denote covariant differentiation along the central curve. Only A.1 and B.2 allow an arbitrary affine connection; all energy, length and index assertions use a positive definite Riemannian metric and its Levi-Civita connection.

## A. Variations with all endpoint terms

**Theorem A.1 (Jacobi fields for a connection with torsion).** Let \(\gamma:[a,b]\to M\) be an affinely parametrized geodesic for a smooth affine connection, with \(T=\dot\gamma\) and torsion \(\mathcal T\). The variational field of any family of such geodesics satisfies
\[
J''+\bigl(\mathcal T(J,T)\bigr)'+R(J,T)T=0.
\tag{A.1}
\]
Every pair \(J(a),J'(a)\) determines exactly one solution on the entire interval. These solutions form a vector space of dimension \(2\dim M\), and each is realized by a smooth geodesic variation on that interval. For a Levi-Civita connection the equation reduces to \(J''+R(J,T)T=0\).

**Proof.** For a smooth map \(F(s,t)\), put \(V=\partial_sF\) and \(T=\partial_tF\), as sections of its pullback tangent bundle. [Linear connections B.2–B.3](linear-and-affine-connections.md#theorem-b-2) and D.3 give
\[
D_sT-D_tV=\mathcal T(V,T),\qquad
D_sD_tT-D_tD_sT=R(V,T)T.
\tag{A.2}
\]
These identities hold at critical points of \(F\) too. If each \(t\)-curve is geodesic, \(D_tT=0\). Substitute the first identity into the second and restrict to \(s=0\); this is (A.1).

Use a parallel frame along \(\gamma\), whose existence and smoothness follow from [Connections D.2](connections-and-parallel-transport.md#theorem-d-2). In that frame (A.1) is a linear second-order system \(j''+C(t)j'+D(t)j=0\) with smooth coefficients. On the compact interval they are bounded. Writing \(z=(j,j')\) gives \(z'=A(t)z\), with \(\|A(t)\|\leq M\). [Local tools 2.1](local-tools-for-bundles-and-transport.md#2-differential-equations-and-their-parameters) gives local existence, uniqueness and smooth dependence. To check that this linear solution lasts for the whole interval, on any subinterval of length \(\delta\) with \(M\delta<1/2\), its integral equation gives
\[
\sup|z|\leq |z(t_0)|+M\delta\sup|z|,\qquad \sup|z|\leq2|z(t_0)|.
\]
The bound holds on every shorter interval of existence. It keeps the graph in a bounded compact set as a finite endpoint is approached, so the continuation assertion of [Local tools 2.1](local-tools-for-bundles-and-transport.md#2-differential-equations-and-their-parameters) extends the solution. Finitely many such intervals reach both endpoints. The same bound locally uniform in parameters proves no loss of interval when the coefficients and data vary nearby. Linearity and uniqueness identify the solution space with its \(2\dim M\) initial coordinates.

For realization, write \(u=J(a)\), \(w=J'(a)\), \(v=T(a)\). Choose a smooth curve \(\sigma(s)\) through \(\gamma(a)\) with velocity \(u\). Let \(P_s\) be parallel transport along \(\sigma\), and prescribe the initial velocity
\[
v(s)=P_s\bigl(v+s(w+\mathcal T(u,v))\bigr).
\tag{A.3}
\]
Then \(v(0)=v\) and \(D_sv(0)=w+\mathcal T(u,v)\). [Geodesics A.1](geodesics-normal-coordinates-and-curvature.md#theorem-a-1) gives the smooth geodesic flow on an open domain in time and initial data. That domain contains the compact time segment with initial datum \(v\). A finite product-neighbourhood cover supplies one neighbourhood of \(v\) on which every time in the segment is allowed. For sufficiently small \(s\), start the flow at \(v(s)\), with time shifted by \(a\). Its variation field has value \(u\) at \(a\). By (A.2), its derivative there is \(D_sv(0)-\mathcal T(u,v)=w\). The first part and uniqueness therefore identify it with \(J\). For the Levi-Civita connection torsion vanishes by [Riemannian connections A.1](riemannian-connections-and-convex-neighbourhoods.md#theorem-a-1). □

**Lemma A.2 (realizing fields and removing corners).** Every piecewise smooth field \(V\) along a compact piecewise smooth curve \(c\) is the field of a piecewise smooth variation. If \(V\) vanishes at the endpoints, the variation can fix the endpoints. A continuous piecewise smooth field along a smooth curve can be approximated by smooth fields with the same endpoint values so that, in a fixed smooth frame,
\[
\sup|V_\varepsilon-V|\longrightarrow0,\qquad
\int_a^b|V_\varepsilon'-V'|^2\,dt\longrightarrow0.
\tag{A.4}
\]
For normal fields along a nonconstant geodesic the approximation can stay normal.

**Proof.** [Geodesics A.1–A.2](geodesics-normal-coordinates-and-curvature.md#theorem-a-1) gives the smooth exponential map on an open neighbourhood of the zero section. Compactness of the image of \(c\) and boundedness of \(V\), on finitely many pieces and charts, give one \(\varepsilon>0\) for which
\[
F(s,t)=\exp_{c(t)}(sV(t)),\qquad |s|<\varepsilon,
\tag{A.5}
\]
is defined for every \(t\). [Geodesics B.1](geodesics-normal-coordinates-and-curvature.md#theorem-b-1) proves that its \(s\)-derivative at zero is \(V(t)\). The map is continuous across the fixed nodes and smooth on each piece. Where \(V=0\), it leaves the point fixed.

Here is an explicit smoothing argument for (A.4). Choose a smooth frame on the interval, for example a parallel frame, and work with the component vector \(v(t)\). At an interior break \(c\), the two smooth pieces have smooth extensions \(v_-\) and \(v_+\) to a neighbourhood of \(c\), with \(v_-(c)=v_+(c)\). Choose a smooth transition function \(\chi:\mathbb R\to[0,1]\) equal to zero near \((-\infty,-1]\) and one near \([1,\infty)\). Such a function follows explicitly from the flat factor of [Local tools 0.5](local-tools-for-bundles-and-transport.md#0-analytic-and-linear-foundations) by taking
\(\eta(x+1)/(\eta(x+1)+\eta(1-x))\).
On \([c-\varepsilon,c+\varepsilon]\) replace \(v\) by
\[
(1-\chi((t-c)/\varepsilon))v_-(t)
 +\chi((t-c)/\varepsilon)v_+(t).
\]
Outside these small disjoint intervals keep \(v\). The replacement is smooth at the joins. Bounded first derivatives of the extensions and their agreement at \(c\) give
\(|v_+(t)-v_-(t)|\leq C\varepsilon\). Thus the new vector differs by \(O(\varepsilon)\) and its derivative is bounded independently of \(\varepsilon\): the factor \(1/\varepsilon\) from \(\chi'\) is multiplied by that difference. The derivative error has bounded size and support of total length \(O(\varepsilon)\), proving its squared-integral convergence. Endpoints are untouched. Passing from ordinary to covariant derivatives adds a bounded matrix times the uniformly small component difference, so (A.4) holds for those derivatives too. Use a parallel orthonormal frame with the last vector tangent to a nonconstant geodesic and smooth only the normal components to preserve normality. All estimates also hold simultaneously for any finite list of fields. □

**Theorem A.3 (first variations and their critical curves).** For a variation \(F\) of a piecewise smooth curve \(c:[a,b]\to M\), define
\[
E(s)=\frac12\int_a^b|\partial_tF(s,t)|^2\,dt,\qquad
L(s)=\int_a^b|\partial_tF(s,t)|\,dt.
\]
Let \(a=t_0<\cdots<t_N=b\) be a common subdivision, \(V=\partial_sF|_0\), \(T=\dot c\), and let superscripts \(-,+\) denote one-sided values at a node. Then
\[
E'(0)=[\langle V,T\rangle]_a^b
 +\sum_{i=1}^{N-1}\langle V(t_i),T_i^--T_i^+\rangle
 -\sum_{i=0}^{N-1}\int_{t_i}^{t_{i+1}}\langle V,T'\rangle\,dt.
\tag{A.6}
\]
If the speed is positive on each closed piece, put \(u=T/|T|\). Then
\[
L'(0)=[\langle V,u\rangle]_a^b
 +\sum_{i=1}^{N-1}\langle V(t_i),u_i^--u_i^+\rangle
 -\sum_{i=0}^{N-1}\int_{t_i}^{t_{i+1}}\langle V,u'\rangle\,dt.
\tag{A.7}
\]
Fixed-endpoint critical curves of energy are exactly affinely parametrized geodesics, including constant ones. Fixed-endpoint critical regular curves of length become geodesics under increasing arc-length parametrization.

**Proof.** Metric compatibility and (A.2), with zero torsion, give
\[
\partial_s\frac{|T|^2}{2}=\langle D_tV,T\rangle,\qquad
\partial_s|T|=\langle D_tV,T/|T|\rangle.
\]
Differentiate the finitely many compact-interval integrals, justified by the uniform difference-quotient estimate of [Local tools 0.3](local-tools-for-bundles-and-transport.md#0-analytic-and-linear-foundations). In the length case the positive minimum of the central speed keeps the nearby denominators away from zero. Integration by parts on each piece gives (A.6)–(A.7); the inner endpoints sum to the displayed jumps because \(V\) is continuous.

If the energy derivative vanishes for every endpoint-fixed variation, take fields supported in one piece. A.2 realizes them. If \(T'\) were nonzero at a point, a nonnegative smooth bump there multiplied by \(T'\) would have a strictly positive integral against \(T'\), contradicting (A.6). Cutoffs are supplied by [Local tools 0.5](local-tools-for-bundles-and-transport.md#0-analytic-and-linear-foundations). Thus \(T'=0\) on each piece. Fields with an arbitrary prescribed value at a single node, constructed with the same cutoffs and a smooth local frame, now force \(T_i^-=T_i^+\). The pieces have identical positions and velocities at their joins. Uniqueness of the geodesic equation, [Geodesics A.1](geodesics-normal-coordinates-and-curvature.md#theorem-a-1), makes them one smooth affinely parametrized geodesic. The converse follows immediately from (A.6), and includes zero velocity.

For length the identical argument forces \(u'=0\) on each piece and \(u_i^-=u_i^+\) at each node. The increasing parameter \(\rho(t)=\int_a^t|T|\,dt\) has positive derivative on each piece and has a smooth inverse there by [Local tools 1.2](local-tools-for-bundles-and-transport.md#1-contraction-and-local-inversion). In that parameter the velocity is \(u\), with zero covariant derivative. At the joins the unit velocities agree, so geodesic uniqueness again glues the pieces. Conversely these conditions make (A.7) zero. □

**Theorem A.4 (energy and length Hessians).** Suppose the central curve \(\gamma\) is an affinely parametrized Riemannian geodesic, and put
\[
I(V,W)=\int_a^b
 \bigl(\langle V',W'\rangle-\langle R(V,T)T,W\rangle\bigr)\,dt,
\qquad A=D_s\partial_sF|_{s=0}.
\tag{A.8}
\]
For any piecewise smooth variation,
\[
E''(0)=I(V,V)+[\langle A,T\rangle]_a^b.
\tag{A.9}
\]
If \(|T|=c>0\), \(u=T/c\), and \(V^\perp=V-\langle V,u\rangle u\), then
\[
L''(0)=c^{-1}I(V^\perp,V^\perp)+[\langle A,u\rangle]_a^b.
\tag{A.10}
\]
For fixed endpoints the boundary terms vanish. The energy Hessian is \(I\), while the length Hessian has all endpoint-fixed tangential fields in its radical. The energy Hessian is positive on every nonzero endpoint-fixed tangential field.

**Proof.** Differentiate the energy integrand twice, using (A.2):
\[
\partial_s^2\frac{|T|^2}{2}
 =|D_sT|^2+\langle D_sD_sT,T\rangle
 =|D_tV|^2+\langle D_tD_sV+R(V,T)V,T\rangle.
\]
Along the central curve \(T'=0\). Metric curvature symmetry, [Geodesics C.3](geodesics-normal-coordinates-and-curvature.md#corollary-c-3), changes the last curvature term into
\(-\langle R(V,T)T,V\rangle\). Integrating \(D_tA\) by parts gives (A.9). At a subdivision node the endpoint curve \(s\mapsto F(s,t_i)\) is the same on both sides, so its covariant acceleration \(A(t_i)\) is the same. The central velocity is smooth; all interior boundary terms consequently cancel.

Twice differentiating the square root \(|T|=\langle T,T\rangle^{1/2}\) gives, at \(s=0\),
\[
L''(0)=c^{-1}I(V,V)
 -c^{-1}\int_a^b\langle V',u\rangle^2\,dt
 +[\langle A,u\rangle]_a^b.
\]
Here \(u'=0\). Write \(V=V^\perp+fu\). The two components and their derivatives are orthogonal; \(R(u,T)T=0\), and \(R(V^\perp,T)T\) is normal by [Geodesics C.3](geodesics-normal-coordinates-and-curvature.md#corollary-c-3). Hence
\[
I(V,V)=I(V^\perp,V^\perp)+\int_a^b(f')^2\,dt,
\qquad \langle V',u\rangle=f',
\]
which proves (A.10). For endpoint-fixed variations the endpoint accelerations are zero. Polarization of these quadratic expressions gives the bilinear Hessians; mixed variations with given two fields are obtained by replacing \(sV\) in (A.5) by \(sV+rW\). A nonzero endpoint-fixed \(f\) cannot have \(f'\equiv0\); its derivative-square integral is positive. This proves the final statements, including the vanishing of every mixed length-Hessian term containing a tangential field. □

## B. Endpoint Jacobi fields and conjugacy

Along a nonconstant geodesic of constant speed, parallel transport preserves the tangent line and its orthogonal complement. In a parallel orthonormal normal frame, a normal field is a function \(v:[a,b]\to\mathbb R^d\), \(d=\dim M-1\), and
\[
B(t)v=R(v,T)T,\qquad
I_B(v,w)=\int_a^b(v'\cdot w'-Bv\cdot w)\,dt.
\tag{B.1}
\]
The matrix \(B(t)\) is smooth and symmetric by [Geodesics C.3](geodesics-normal-coordinates-and-curvature.md#corollary-c-3). We use the space \(\mathcal V_0\) of continuous piecewise smooth normal fields vanishing at both endpoints. The **index** \(i(I)\) is the supremum of dimensions of subspaces on which \(I\) is negative definite. The **nullity** \(n(I)\) is the dimension of its radical
\(\{V:I(V,W)=0\text{ for all }W\in\mathcal V_0\}\).
Finally \(a(I)\) is the supremum of dimensions of subspaces on which \(I(V,V)\leq0\) for every \(V\). We prove below that all three numbers are finite and attained.

**Lemma B.1 (integration by parts and the radical).** For continuous piecewise smooth \(V,W\), using any common subdivision,
\[
\begin{aligned}
I(V,W)={}&[\langle V',W\rangle]_a^b
 +\sum_i\langle V_i'^--V_i'^+,W(t_i)\rangle\\
&-\sum_i\int_{t_i}^{t_{i+1}}
       \langle V''+R(V,T)T,W\rangle\,dt.
\end{aligned}
\tag{B.2}
\]
The radical on \(\mathcal V_0\) consists exactly of smooth normal Jacobi fields vanishing at both endpoints. The same assertion holds on all endpoint-fixed fields if the word normal is omitted.

**Proof.** Apply the metric product rule and integration by parts on each piece. Continuity of \(W\) combines the node contributions as displayed. Symmetry of \(B\) also proves symmetry of \(I\).

A smooth Jacobi field zero at the endpoints makes (B.2) vanish for every endpoint-fixed \(W\). Conversely, suppose \(V\) is in the radical. On the interior of a single smooth piece, choose a nonnegative smooth bump \(\chi\) and take \(W=\chi(V''+R(V,T)T)\). These fields are allowed, and in the normal case remain normal. Formula (B.2) gives
\(-\int\chi|V''+R(V,T)T|^2=0\).
If the residual were nonzero anywhere, a bump supported near that point would make the integral strictly negative. Thus \(V\) solves the Jacobi equation on every piece. Next choose a smooth field whose value at one interior node is the derivative jump there and which vanishes near all other nodes and endpoints. Cutoffs and a parallel frame construct it explicitly. Formula (B.2) now gives the squared length of that jump, which must vanish. Both \(V\) and \(V'\) therefore agree at all joins. Uniqueness in A.1 glues the pieces to one smooth Jacobi field. The same proof works without the normal restriction. □

**Theorem B.2 (conjugacy and the exponential differential).** A time \(t>0\) on \(\gamma(t)=\exp_p(tv)\) is conjugate to \(0\) if a nonzero solution of the Jacobi equation vanishes at \(0,t\). Its multiplicity \(\mu(t)\) is the dimension of that solution space. For an arbitrary smooth affine connection use (A.1); then
\[
\mu(t)=\dim\ker(d\exp_p)_{tv}.
\tag{B.3}
\]
For a nonconstant Riemannian geodesic every endpoint-vanishing Jacobi field is normal and \(\mu(t)\leq\dim M-1\). The tangential component of any Riemannian Jacobi field is affine in the geodesic parameter.

**Proof.** Differentiate \(F(s,u)=\exp_p(u(v+sw))\). A.1 makes its field Jacobi, and
\[
J_w(u)=(d\exp_p)_{uv}(uw),\qquad J_w(0)=0,\qquad J_w'(0)=w.
\tag{B.4}
\]
The last equality follows either from the initial velocity derivative or from [Geodesics B.1](geodesics-normal-coordinates-and-curvature.md#theorem-b-1); the torsion correction at zero is zero because \(J_w(0)=0\). Conversely A.1 says that every Jacobi field with initial value zero is precisely one such \(J_w\). Since multiplication by the nonzero scalar \(t\) is a linear isomorphism, (B.4) identifies its endpoint kernel with the kernel in (B.3).

In the Riemannian case,
\[
\frac{d^2}{du^2}\langle J,T\rangle
 =-\langle R(J,T)T,T\rangle=0
\]
by [Geodesics C.3](geodesics-normal-coordinates-and-curvature.md#corollary-c-3). This scalar function is affine and, if zero at two distinct endpoints, is identically zero. The field is then normal, and its initial derivative is a normal vector. Uniqueness makes the map from endpoint-vanishing fields to their initial derivatives injective, giving the dimension bound. The same affine calculation proves the last assertion. □

**Example B.3 (all constant-curvature solutions).** Along a unit-speed geodesic in constant sectional curvature \(k\), choose a parallel orthonormal frame \(E_1,\ldots,E_{n-1},T\). Every Jacobi field is
\[
J(t)=(\alpha+\beta t)T+
 \sum_{j=1}^{n-1}\bigl(a_jC_k(t)+b_jS_k(t)\bigr)E_j(t),
\tag{B.5}
\]
where \(S_k,C_k\) are the scalar functions of [Sectional curvature B.2](sectional-curvature-and-space-forms.md#lemma-b-2). If \(n\geq2\), the positive conjugate times are exactly \(q\pi/\sqrt{k}\), \(q=1,2,\ldots\), when \(k>0\), each of multiplicity \(n-1\). There are none when \(k\leq0\).

**Proof.** [Sectional curvature A.1](sectional-curvature-and-space-forms.md#theorem-a-1) gives \(R(V,T)T=kV\) for \(V\perp T\), and it vanishes for \(V\) parallel to \(T\). In the parallel frame A.1 consequently splits into \(f''=0\) in the tangent coordinate and \(f''+kf=0\) in each normal coordinate. [Sectional curvature B.2](sectional-curvature-and-space-forms.md#lemma-b-2) proves all scalar solutions and their initial conditions, giving (B.5). A field vanishing at zero has \(\alpha=a_j=0\). If it also vanishes at positive \(t\), then \(\beta=0\), and the remaining condition is \(b_jS_k(t)=0\). The zeros and their absence for nonpositive \(k\) follow from the same scalar formulas and [Connections E.1](connections-and-parallel-transport.md#lemma-e-1)'s exact circle period. This proves both the list and the multiplicities. □

## C. A finite space that retains the entire index

The next lemmas apply to any smooth symmetric matrix function \(B:[0,b]\to\operatorname{Sym}(d,\mathbb R)\) and its form (B.1), whether or not the matrix was obtained from curvature. Dimension \(d=0\) means the zero space and causes no exception. Fix \(C\geq0\) with \(\|B(t)\|\leq C\), which exists by compactness and [Local tools 0.1–0.2](local-tools-for-bundles-and-transport.md#0-analytic-and-linear-foundations).

**Lemma C.1 (short-interval positivity and interpolation).** On an interval \([c,e]\) of length \(\delta\) satisfying \(C\delta^2/2<1\), the form \(I_B\) is positive definite on nonzero fields vanishing at its two ends. Every two endpoint values determine a unique solution of \(j''+Bj=0\) on this interval. That solution depends smoothly on the endpoint values and on \(c,e\) while the strict bound holds.

**Proof.** For \(w(c)=0\), the fundamental theorem of calculus and Cauchy–Schwarz give
\[
|w(t)|^2=\left|\int_c^tw'(s)\,ds\right|^2
 \leq(t-c)\int_c^t|w'(s)|^2\,ds.
\]
The integral Cauchy–Schwarz inequality here follows by integrating the nonnegative square \(|f-\lambda g|^2\) and considering its quadratic discriminant; this also applies to vectors by the Euclidean dot product. Integrate the displayed bound, replace the inner integral by its full-interval value, and obtain
\[
\int_c^e|w|^2\leq\frac{\delta^2}{2}\int_c^e|w'|^2,\qquad
I_B(w,w)\geq(1-C\delta^2/2)\int_c^e|w'|^2.
\tag{C.1}
\]
A nonzero continuous piecewise smooth field with both endpoints zero cannot have zero derivative on every piece, so the latter integral is positive.

Solutions of the matrix equation have \(2d\) initial coordinates by the linear-system argument in A.1. The linear map sending a solution to its two endpoint values has trivial kernel: an element of its kernel has \(I_B(j,j)=0\) by integration by parts, so (C.1) forces zero. Between spaces of equal finite dimension an injective linear map is bijective. Its matrix depends smoothly on the interval endpoints, by [Local tools 2.1](local-tools-for-bundles-and-transport.md#2-differential-equations-and-their-parameters). Matrix inversion is smooth where invertible, by [Local tools 0.4](local-tools-for-bundles-and-transport.md#0-analytic-and-linear-foundations). This proves the claimed smooth dependence, together with the same theorem's dependence on initial data. □

**Lemma C.2 (finite symmetric forms and their variation).** A symmetric bilinear form \(Q\) on \(\mathbb R^D\) has an orthogonal decomposition into a negative, a zero and a positive space of dimensions \(p,k,q\). Its index is \(p\), its nullity is \(k\), and its maximal nonpositive dimension is \(p+k\). If \(Q(r)\) is a continuous family and \(Q(r_0)\) has those dimensions, then for all nearby \(r\),
\[
p\leq i(Q(r))\leq p+k.
\tag{C.2}
\]
In particular its index is locally constant when its nullity is zero.

**Proof.** Dimension zero is immediate. Otherwise represent \(Q\) by a real symmetric matrix \(A\). The function \(x\mapsto x\cdot Ax\) attains its maximum on the unit sphere by [Local tools 0.1](local-tools-for-bundles-and-transport.md#0-analytic-and-linear-foundations). Differentiation along every tangent direction at a maximizer \(v\) shows \(Av=\lambda v\). Its orthogonal complement is invariant because \(A\) is symmetric. Induction on dimension gives an orthonormal eigenbasis, including dimension zero. Split it by the signs of its eigenvalues. The kernel is exactly the zero space. Projection of a negative definite subspace to the negative space is injective, since a vector with zero such projection has \(Q(x,x)\geq0\). Thus the maximal negative dimension is \(p\). Similarly a nonpositive subspace projects injectively to the sum of the negative and zero spaces, because a nonzero vector in the positive space has positive square. This proves the dimension \(p+k\) and attainment.

On the unit sphere of the negative space the square is bounded above by a strictly negative number. On the unit sphere of the positive space it is bounded below by a strictly positive number. Continuity of the finitely many matrix entries preserves both bounds for all sufficiently close \(r\). Therefore \(i(Q(r))\geq p\). Any negative subspace of dimension greater than \(p+k=D-q\) would meet that fixed positive space nontrivially, by the dimension formula for subspaces, which is impossible. This gives the upper bound. When \(k=0\) the bounds coincide. □

**Theorem C.3 (broken-Jacobi reduction).** Choose
\(0=t_0<\cdots<t_N=b\) with every interval satisfying C.1. Let \(\mathcal J\) be the endpoint-fixed fields which solve \(j''+Bj=0\) on every piece, and \(\mathcal W\) the fields which vanish at every node. Then
\[
\mathcal V_0=\mathcal J\oplus\mathcal W,\qquad
I_B(\mathcal J,\mathcal W)=0,\qquad I_B|_{\mathcal W}>0.
\tag{C.3}
\]
Node evaluation identifies \(\mathcal J\) with \((\mathbb R^d)^{N-1}\). If \(Q=I_B|_{\mathcal J}\), then
\[
i(I_B)=i(Q),\qquad n(I_B)=n(Q),\qquad
a(I_B)=i(Q)+n(Q).
\tag{C.4}
\]
All these quantities are finite and attained. In particular a subspace on which the bilinear form vanishes identically has dimension at most \(a(I_B)\).

**Proof.** Interpolate the values of \(V\) at every adjacent pair of nodes by C.1. The resulting unique \(J\) is continuous and piecewise smooth, and \(W=V-J\) vanishes at all nodes. Uniqueness also proves directness of the sum and the node-coordinate identification. Integration by parts on each interval gives \(I_B(J,W)=0\), since the equation kills its integral term and \(W\) kills its endpoint terms. C.1 on each piece shows that \(I_B(W,W)>0\) unless \(W=0\).

Diagonalize the finite form on \(\mathcal J\) by C.2. Its positive eigenspace together with \(\mathcal W\) is positive definite; its zero eigenspace lies in the radical of the whole form. A radical vector must have zero \(\mathcal W\) component, by pairing with that component, and then must be in the finite radical. Projection to the negative eigenspace is injective on any negative definite subspace of \(\mathcal V_0\); projection to the negative-plus-zero eigenspace is injective on any nonpositive subspace. Indeed a nonzero vector in either forbidden kernel would have nonnegative, respectively positive, square. These projections give the upper bounds in (C.4); the finite eigenspaces themselves attain them. A totally isotropic subspace is nonpositive, proving the final assertion. □

**Lemma C.4 (there are finitely many conjugate times).** Let \(j''+Bj=0\) on \([0,b]\), and let \(\mu(t)\) count its solutions with \(j(0)=j(t)=0\). Then only finitely many \(t\in(0,b]\) have \(\mu(t)>0\), and the sum of their multiplicities is finite.

**Proof.** For any finite list of such times \(0=\tau_0<\tau_1<\cdots<\tau_s\), extend each endpoint-vanishing solution on \([0,\tau_i]\) by zero after \(\tau_i\). These extended fields are continuous and piecewise smooth. They span a totally isotropic subspace for \(I_B\): for two fields whose endpoints are ordered \(\tau_i\leq\tau_j\), integrate by parts using the untruncated, smooth Jacobi field ending at \(\tau_j\) on \([0,\tau_j]\). The other field vanishes at both ends, so the pairing is zero by (B.2).

The subspaces for distinct times are linearly independent. In a relation among their sums, restrict to \((\tau_{s-1},\tau_s)\); only the final solution survives, so it vanishes on an open interval. Uniqueness of the differential equation makes it zero everywhere. Descend through the remaining times. The resulting isotropic subspace has dimension \(\sum_{i=1}^s\mu(\tau_i)\), which is at most the finite bound \(a(I_B)\) from C.3. If there were infinitely many conjugate times, finite lists of arbitrarily large size would violate that bound, since each contributes at least one. The same bound now proves finiteness of the full multiplicity sum. □

**Lemma C.5 (strict increase after an endpoint kernel).** For \(0<\tau<b\),
\[
i(I_{[0,b]})\geq i(I_{[0,\tau]})+n(I_{[0,\tau]}).
\tag{C.5}
\]
Here both forms use restrictions of the same matrix \(B\). In particular, an interior conjugate time gives a negative field on the longer interval.

**Proof.** By C.3 choose a finite-dimensional negative subspace \(E\) of dimension \(p=i(I_{[0,\tau]})\), and let \(K\) be the radical, of dimension \(k=n(I_{[0,\tau]})\). By B.1 its members are Jacobi fields with both endpoint values zero. Extend every \(x\in E\) and \(j\in K\) by zero after \(\tau\), denoting the extensions by \(x^0,j^0\). The form on \(E^0\) stays negative, and \(I(x^0,j^0)=I(j^0,j^0)=0\).

For \(j\in K\), its derivative \(j'(\tau)\) determines it injectively, by uniqueness with final data \(j(\tau)=0\). Choose a smooth scalar cutoff \(\chi\) supported inside \((0,b)\), with \(\chi(\tau)=1\), and set
\[
w_j(t)=-\chi(t)j'(\tau)
\]
in the fixed parallel component frame. This is linear in \(j\) and vanishes at \(0,b\). Integration by parts on \([0,\tau]\) gives
\[
I(j^0,w_j)=-|j'(\tau)|^2.
\tag{C.6}
\]
Give \(K\) the norm \(\|j\|=|j'(\tau)|\), and choose any Euclidean coefficient norm on \(E\). Finite-dimensional boundedness, [Local tools 0.2](local-tools-for-bundles-and-transport.md#0-analytic-and-linear-foundations), supplies \(\alpha>0\) and \(M<\infty\) such that
\[
I(x^0,x^0)\leq-\alpha\|x\|^2,\quad
|I(x^0,w_j)|\leq M\|x\|\|j\|,\quad
|I(w_j,w_j)|\leq M\|j\|^2.
\]
If \(E=0\), simply omit its terms. For \(\varepsilon>0\),
\[
\begin{aligned}
I(x^0+j^0+\varepsilon w_j,x^0+j^0+\varepsilon w_j)
\leq{}&-\alpha\|x\|^2-2\varepsilon\|j\|^2\\
&+2\varepsilon M\|x\|\|j\|
 +\varepsilon^2M\|j\|^2.
\end{aligned}
\]
Completing a square bounds the mixed term by
\(\alpha\|x\|^2/2+2\varepsilon^2M^2\|j\|^2/\alpha\).
For one sufficiently small positive \(\varepsilon\), the result is strictly negative unless \(x=j=0\). With \(E=0\) the same conclusion follows from \(-2\varepsilon+\varepsilon^2M<0\). Consequently the linear map
\((x,j)\mapsto x^0+j^0+\varepsilon w_j\) is injective and its image is a negative subspace of dimension \(p+k\). This proves (C.5), including the cases where one of the two spaces is zero. □

## D. Counting conjugate points

**Theorem D.1 (Morse index and nullity).** Let \(\gamma:[0,b]\to M\) be a nonconstant Riemannian geodesic, and let \(\mu(t)\) be the conjugate multiplicity of B.2. Then
\[
i(I)=\sum_{0<t<b}\mu(t),\qquad
n(I)=\mu(b),\qquad
a(I)=\sum_{0<t\leq b}\mu(t).
\tag{D.1}
\]
All sums are finite. The same index is obtained on smooth endpoint-fixed fields, on all endpoint-fixed energy fields, and on normal fields for the length Hessian. For a constant geodesic its energy index form has index, nullity and maximal nonpositive dimension zero.

**Proof.** First work on normal fields, in the frame (B.1). Write \(i(r)=i(I_{[0,r]})\). Extension by zero from a shorter interval embeds its endpoint-fixed fields into the fields on every longer interval and preserves the form. Thus \(i(r)\) is nondecreasing. By C.1 it is zero for sufficiently small positive \(r\).

Choose an integer \(N\) large enough that \(C(b/N)^2/2<1\). For each \(r>0\), use the moving nodes
\[
t_j(r)=jr/N,\qquad 0\leq j\leq N.
\tag{D.2}
\]
On the fixed coordinate space \((\mathbb R^d)^{N-1}\), let \(Q(r)\) be the form on the interpolants with those node values. C.1 makes the interpolants smooth in \(r\) after each interval is parametrized by a fixed unit interval. Differentiation under a compact integral, [Local tools 0.3](local-tools-for-bundles-and-transport.md#0-analytic-and-linear-foundations), shows that all entries of \(Q(r)\) are smooth for \(r>0\). C.3 and B.1 identify
\[
i(Q(r))=i(r),\qquad \dim\ker Q(r)=\mu(r).
\tag{D.3}
\]
C.2 therefore makes \(i(r)\) locally constant at nonconjugate times.

There are only finitely many conjugate times by C.4. At one such time \(\tau\), put \(p=i(\tau)\), \(k=\mu(\tau)\). C.2 bounds all nearby indices between \(p\) and \(p+k\). On the left, monotonicity gives \(i(r)\leq p\), so \(i(r)=p\). On the right, C.5 gives \(i(r)\geq p+k\), so \(i(r)=p+k\). This right-hand statement is used only when \(\tau<b\). Beginning with zero on a short interval and passing through the finite list proves that \(i(b)\) is the sum of the multiplicities strictly before \(b\). A conjugate endpoint contributes its nullity but has not yet increased the index. B.1 gives \(n(I)=\mu(b)\), and C.3 gives \(a(I)=i(I)+n(I)\). These are (D.1).

The form splits orthogonally into its normal part and the positive tangential form
\(\int(f')^2\) by A.4. Thus adding tangential endpoint-fixed fields changes none of these three numbers, by the same projection argument as C.3. The length Hessian on normal fields is a positive scalar multiple of \(I\), so has the same index.

It remains to justify using smooth fields only. Take a basis of a maximal negative subspace, which C.3 supplies. Apply A.2 to its finitely many fields. Uniform convergence and squared-integral convergence of derivatives imply convergence of every Gram matrix entry of \(I\), by Cauchy–Schwarz and boundedness of \(B\). For example
\[
\left|\int(v_\varepsilon'\cdot w_\varepsilon'-v'\cdot w')\right|
 \leq\|v_\varepsilon'-v'\|_2\|w_\varepsilon'\|_2
   +\|v'\|_2\|w_\varepsilon'-w'\|_2,
\]
where \(\|f\|_2=(\int|f|^2)^{1/2}\); all integrands are piecewise continuous. C.2 preserves negative definiteness for sufficiently small errors. The approximated fields are linearly independent, since a dependence would give zero square to a nonzero coefficient vector in this negative Gram matrix. Their span gives the same index with smooth fields; the reverse inequality follows from inclusion. The radical fields already are smooth by B.1. Finally a constant geodesic has \(T=0\) and \(I(V,V)=\int|V'|^2\), positive for every nonzero endpoint-fixed field. All three stated numbers then vanish. □

**Theorem D.2 (the Jacobi interpolation inequality).** Suppose there are no conjugate times in \((0,b]\). For every normal piecewise smooth \(V\) with \(V(0)=0\), there is exactly one normal Jacobi field \(J\) with \(J(0)=0,J(b)=V(b)\), and
\[
I(V,V)\geq I(J,J),
\tag{D.4}
\]
with equality exactly when \(V=J\). In particular \(I\) is positive definite on \(\mathcal V_0\).

**Proof.** The map taking initial normal derivative to final value has equal domain and codomain dimension \(d\), by A.1. Its kernel has dimension \(\mu(b)=0\), so it is invertible. This proves existence and uniqueness of \(J\). D.1 gives index and nullity zero for endpoint-fixed normal fields. Index zero means \(I(W,W)\geq0\) for every such \(W\); otherwise its one-dimensional span would be negative. If a nonzero \(W\) had square zero, then for every \(Z\) and every real \(s\),
\[
0\leq I(W+sZ,W+sZ)=2sI(W,Z)+s^2I(Z,Z).
\]
Both signs of sufficiently small \(s\) force \(I(W,Z)=0\). Thus \(W\) would lie in the zero radical, a contradiction. This proves positivity. Now \(W=V-J\) vanishes at both endpoints, and B.1 gives \(I(J,W)=0\). Therefore
\(I(V,V)-I(J,J)=I(W,W)\), with equality precisely when \(W=0\). □

## E. Negative eigenvalues without an infinite-dimensional spectral theorem

For a smooth symmetric \(B:[0,b]\to\operatorname{Sym}(d,\mathbb R)\), the Dirichlet problem is
\[
\mathcal Lv=-v''-Bv=\lambda v,\qquad v(0)=v(b)=0.
\tag{E.1}
\]
A real \(\lambda\) is an eigenvalue when a nonzero smooth solution exists; its multiplicity is the dimension of that solution space. Define
\[
I_\lambda(v,w)=I_B(v,w)-\lambda\int_0^b v\cdot w\,dt.
\tag{E.2}
\]
Integration by parts identifies the radical of \(I_\lambda\) with the solution space in (E.1), by the proof of B.1 applied to \(B+\lambda I_d\).

**Lemma E.1 (uniform lower bound and a finite matrix family).** If \(\|B(t)\|\leq C\), every eigenvalue on any interval \([0,r]\), \(0<r\leq b\), satisfies \(\lambda>-C\). For every fixed compact interval of parameters \(\lambda\), there is a single subdivision of \([0,b]\) on which the broken-solution reduction of C.3 applies to all \(I_\lambda\), producing a smooth family of finite symmetric matrices \(Q(\lambda)\).

**Proof.** Multiply (E.1) by \(v\) and integrate. The endpoint conditions give
\[
\lambda\int_0^r|v|^2
 =\int_0^r|v'|^2-\int_0^rBv\cdot v
 \geq\int_0^r|v'|^2-C\int_0^r|v|^2.
\tag{E.3}
\]
For a nonzero endpoint-fixed solution both \(\int|v|^2\) and \(\int|v'|^2\) are positive; the latter could vanish only for a constant vector, then zero by its endpoint. Division proves the strict bound, independent of \(r\).

On a compact parameter interval enlarge \(\|B+\lambda I_d\|\)'s uniform bound slightly so it also holds in an open neighbourhood of that interval. Choose all subdivision lengths to satisfy C.1 for this bound. The solution of
\(j''+(B+\lambda I_d)j=0\) interpolating each pair of node values depends smoothly on \(\lambda\), by the parameter version of [Local tools 2.1](local-tools-for-bundles-and-transport.md#2-differential-equations-and-their-parameters) and the invertible endpoint matrix in C.1. Integrating its quadratic form on each fixed interval gives a smooth matrix \(Q(\lambda)\), by [Local tools 0.3](local-tools-for-bundles-and-transport.md#0-analytic-and-linear-foundations). C.3 gives
\[
i(Q(\lambda))=i(I_\lambda),\qquad
\dim\ker Q(\lambda)=\dim\ker(\mathcal L-\lambda I).
\tag{E.4}
\]
No basis of eigenfunctions is needed for this construction. □

**Lemma E.2 (a definite crossing of symmetric forms).** Let \(Q(s)\) be a smooth finite symmetric matrix family near \(s_0\), with nonzero kernel \(K\) at \(s_0\). If \(Q'(s_0)|_K\) is negative definite, then \(s_0\) is an isolated singular parameter. If \(p=i(Q(s_0))\), \(k=\dim K\), then its index is \(p\) just before \(s_0\) and \(p+k\) just after it.

**Proof.** Choose the Euclidean orthogonal complement \(H=K^\perp\). By C.2, \(Q(s_0)|_H\) is invertible. In \(H\oplus K\) write
\[
Q(s)=
\begin{pmatrix}A(s)&D(s)\\D(s)^{\mathsf T}&E(s)\end{pmatrix}.
\]
At \(s_0\), \(D=0\), \(E=0\), and \(A\) is invertible. It remains invertible nearby by [Local tools 0.4](local-tools-for-bundles-and-transport.md#0-analytic-and-linear-foundations). Completing the square by the invertible change \(x\mapsto x+A^{-1}Dy\) decomposes the form into \(A(s)\) and
\[
S(s)=E(s)-D(s)^{\mathsf T}A(s)^{-1}D(s).
\tag{E.5}
\]
An invertible coordinate change preserves the dimensions of negative spaces and of the kernel, by mapping those subspaces bijectively. Now \(S(s_0)=0\) and \(S'(s_0)=E'(s_0)=Q'(s_0)|_K\). The fundamental theorem of calculus entry by entry gives
\[
S(s)=(s-s_0)\bigl(S'(s_0)+R(s)\bigr),\qquad \|R(s)\|\longrightarrow0.
\]
Negative definiteness has a strict uniform bound on the unit sphere, so \(S(s)\) is positive definite just before \(s_0\) and negative definite just after. Meanwhile \(A(s)\) has constant index \(p\) by C.2. The square completion proves the asserted indices and makes both blocks invertible whenever \(s\ne s_0\) is sufficiently close. Hence the singularity is isolated. □

**Theorem E.3 (spectral index formula).** There are finitely many negative Dirichlet eigenvalues in (E.1), each of finite multiplicity, and
\[
i(I_B)=\sum_{\lambda<0}\dim\ker(\mathcal L-\lambda I).
\tag{E.6}
\]
The zero eigenspace is the space of endpoint Jacobi fields. For the normal operator of a Riemannian geodesic it has dimension \(\mu(b)\). The same negative-eigenvalue count holds for the full energy operator.

**Proof.** Set \(\lambda_0=-C-1\). For nonzero endpoint-fixed \(v\),
\[
I_{\lambda_0}(v,v)\geq\int_0^b(|v'|^2+|v|^2)\,dt>0.
\]
There are no eigenvalues at or below \(\lambda_0\), by E.1. Form its single smooth finite family \(Q(\lambda)\) on an open neighbourhood of \([\lambda_0,0]\).

We compute its derivative on a kernel. Fix a node-coordinate vector \(x\in\ker Q(\lambda_*)\), and let \(j_\lambda(x)\) be its interpolating broken solution. At \(\lambda_*\), C.3 and B.1 imply that \(j=j_{\lambda_*}(x)\) is a global solution of (E.1). Its parameter derivative \(z=\partial_\lambda j_\lambda(x)|_{\lambda_*}\) is continuous and piecewise smooth, with zero values at all fixed nodes, including the endpoints. Differentiating the integral yields
\[
\frac{d}{d\lambda}\bigg|_{\lambda_*}
 Q(\lambda)(x,x)
 =2I_{\lambda_*}(j,z)-\int_0^b|j|^2\,dt
 =-\int_0^b|j|^2\,dt.
\tag{E.7}
\]
The middle pairing is zero because \(j\) is in the radical on all endpoint-fixed fields. Node interpolation is injective, so \(x\ne0\) implies \(j\ne0\). Thus (E.7) is negative definite on the kernel. Polarization supplies the corresponding bilinear identity.

E.2 makes every singular parameter isolated. The singular set in \([\lambda_0,0]\) is closed, since it is the zero set of the continuous determinant, and hence compact by [Local tools 0.1](local-tools-for-bundles-and-transport.md#0-analytic-and-linear-foundations). The neighbourhoods isolating its individual points form an open cover; a finite subcover shows that the singular set is finite. Each multiplicity is finite because an endpoint-zero solution is determined by its initial derivative in \(\mathbb R^d\), by A.1.

The initial index is zero. It is constant between singular parameters by C.2, and increases at each interior singular parameter by exactly its kernel dimension, by E.2. At a possible final singular parameter \(0\), its value equals the preceding index; that endpoint contributes nullity, not negative index. Combining this count with (E.4) at zero proves (E.6). Integration by parts gives the asserted identification of the zero eigenspace, and B.2 identifies its geometric multiplicity. For the full energy operator the tangential scalar equation is \(-f''=\lambda f\) with zero endpoints. Its integrated identity
\(\lambda\int f^2=\int(f')^2\) excludes negative and zero eigenvalues, so it changes neither the negative count nor nullity. □

## F. What conjugate points say about minimization

**Theorem F.1 (the first conjugate obstruction).** If a nonconstant geodesic on \([0,b]\) has a conjugate time in \((0,b)\), it admits arbitrarily small smooth endpoint-fixed variations with smaller energy and smaller length. A minimizing geodesic has no interior conjugate time. At a first conjugate endpoint the index is zero and the nullity is positive; such a segment can still minimize.

**Proof.** C.5 constructs a negative endpoint-fixed normal field on the longer interval as soon as there is a nonzero endpoint Jacobi field on a strictly shorter interval. Smooth it by A.2. The form converges under this approximation by the estimates in D.1, so a smooth approximation still has negative square. Realize it by (A.5). Its first energy and length variations vanish by A.3, and A.4 gives strictly negative second variations for both, since the speed is constant and positive. The fundamental theorem of calculus twice, or its integral Taylor formula from [Local tools 0.3](local-tools-for-bundles-and-transport.md#0-analytic-and-linear-foundations), makes both values strictly smaller for every sufficiently small nonzero variation parameter. The family converges smoothly to the central curve as the parameter tends to zero, giving arbitrary smallness. Thus an interior conjugate point is incompatible with minimization.

If the final endpoint is the first conjugate time, D.1 gives index zero and nullity \(\mu(b)>0\). This situation can occur on a minimizing segment: the unit-sphere meridian from a point to its antipode has first conjugate time \(\pi\) by B.3 and is minimizing by [Riemannian connections E.1](riemannian-connections-and-convex-neighbourhoods.md#theorem-e-1), which proves the exact spherical distance and its minimizing arcs. □

**Theorem F.2 (a Ricci bound forces a conjugate time).** Let a unit-speed geodesic in dimension \(n\geq2\) be defined on
\([0,\pi/\sqrt{k}]\), where \(k>0\). If
\[
\operatorname{Ric}(T,T)\geq(n-1)k
\tag{F.1}
\]
throughout that interval, some time in \((0,\pi/\sqrt{k}]\) is conjugate to zero. In particular the conclusion holds if every sectional curvature of a plane containing \(T\) is at least \(k\).

**Proof.** Put \(L=\pi/\sqrt{k}\), and choose a parallel orthonormal normal frame \(E_1,\ldots,E_{n-1}\). If there were no conjugate time in the stated closed interval, D.2 would make \(I\) positive on every nonzero endpoint-fixed normal field. Apply it to
\(V_j(t)=\sin(\sqrt{k}t)E_j(t)\).
These fields are nonzero because the sine is positive in the interval interior, by [Sectional curvature B.2](sectional-curvature-and-space-forms.md#lemma-b-2). Tracing the curvature term gives
\[
\begin{aligned}
\sum_{j=1}^{n-1}I(V_j,V_j)
&=\int_0^L\bigl((n-1)k\cos^2(\sqrt{k}t)
 -\operatorname{Ric}(T,T)\sin^2(\sqrt{k}t)\bigr)\,dt\\
&\leq(n-1)k\int_0^L
       \bigl(\cos^2(\sqrt{k}t)-\sin^2(\sqrt{k}t)\bigr)\,dt=0.
\end{aligned}
\tag{F.2}
\]
The final equality follows by integrating the derivative of
\(\sin(\sqrt{k}t)\cos(\sqrt{k}t)/\sqrt{k}\); the endpoint values are zero. This contradicts positivity of all \(n-1\) summands. By the Ricci trace formula in [Sectional curvature A.1](sectional-curvature-and-space-forms.md#theorem-a-1), a lower sectional bound on the \(n-1\) planes spanned by \(T,E_j\) implies (F.1). □

**Corollary F.3 (nonpositive curvature has no conjugate points).** If every sectional curvature of a plane containing the velocity of a nonconstant geodesic is nonpositive, then it has no conjugate times and its endpoint index form is positive definite on every compact segment.

**Proof.** For a normal field,
\(\langle R(V,T)T,V\rangle\leq0\), with the zero-vector case immediate and the nonzero case given by the definition of sectional curvature. Consequently
\(I(V,V)\geq\int|V'|^2>0\) for every nonzero endpoint-fixed normal field. A nonzero endpoint Jacobi field would have square zero by B.1, a contradiction. Tangential endpoint-fixed fields add the positive derivative-square form of A.4, so positivity holds for all such fields too. □

**Example F.4 (endpoint degeneracy and global minimization are different).** On the unit \(S^n\), \(n\geq2\), every great semicircle minimizes between its antipodal endpoints despite having nullity \(n-1\). On the flat circle, a geodesic can have no conjugate times and nevertheless fail to minimize globally.

**Proof.** [Sectional curvature C.2](sectional-curvature-and-space-forms.md#theorem-c-2) gives the complete round metric and its unit-speed geodesics
\(\gamma(t)=\cos t\,p+\sin t\,v\), where \(p,v\) are orthonormal ambient vectors. [Hopf–Rinow B.2](completeness-and-the-hopf-rinow-theorem.md#theorem-b-2) supplies a minimizing unit-speed geodesic between \(p\) and \(-p\). Its length \(L>0\) must satisfy \(\cos L=-1,\sin L=0\), so \(L\) is an odd positive multiple of \(\pi\), by [Connections E.1](connections-and-parallel-transport.md#lemma-e-1). The explicit semicircle of length \(\pi\) is a competitor, forcing \(L=\pi\). Every such semicircle therefore minimizes. B.3 and D.1 give its nullity \(n-1\) and index zero.

For the other assertion, form the Euclidean quotient \(\mathbb R/(2\pi\mathbb Z)\) with its descended metric, as in [Sectional curvature G.3](sectional-curvature-and-space-forms.md#theorem-g-3). Its connection is ordinary differentiation in the covering coordinate. Every endpoint-fixed field has energy square \(\int|V'|^2>0\) unless zero. Its Jacobi equation is \(V''=0\), whose two zero endpoint values force the solution to vanish. Thus there are no conjugate times. But on \(0\leq t\leq3\pi/2\), the geodesic \([t]\) has length \(3\pi/2\), whereas the path \([-t/3]\) has the same endpoints and length \(\pi/2\). This explicitly disproves global minimization for that arc. □

## G. Exercises with complete solutions

**Exercise G.1 (round-sphere fields and meridians).** On the unit sphere take
\(\gamma(t)=(\sin t,0,\cos t)\). Find all Jacobi fields, realize one vanishing at \(0,\pi\) through a variation of meridians, and determine its conjugate multiplicities.

**Solution.** Let
\[
T(t)=(\cos t,0,-\sin t),\qquad E(t)=(0,1,0).
\]
These form an orthonormal tangent frame along \(\gamma\). The ambient derivative of \(E\) is zero and that of \(T\) is \(-\gamma\), purely normal to the sphere. The quadric connection formula in [Sectional curvature C.1](sectional-curvature-and-space-forms.md#theorem-c-1) thus makes both fields parallel along the curve. B.3, with \(k=1\), gives precisely
\[
J(t)=(a+bt)T(t)+(c\cos t+d\sin t)E(t),
\qquad a,b,c,d\in\mathbb R.
\tag{G.1}
\]
The family
\[
F(s,t)=(\sin t\cos s,\sin t\sin s,\cos t)
\tag{G.2}
\]
lies on the sphere and traces unit-speed great circles, hence geodesics by [Sectional curvature C.2](sectional-curvature-and-space-forms.md#theorem-c-2). Its variation field at \(s=0\) is \(\sin t\,E(t)\), zero at \(0,\pi\). Every Jacobi field vanishing at zero has \(a=c=0\). Requiring a further zero at positive \(t\) forces \(b=0\) and \(d\sin t=0\). Thus the conjugate times are the positive integer multiples of \(\pi\), each of multiplicity one. By D.1, at \(b=\pi,2\pi,3\pi\) the indices are respectively \(0,1,2\), with nullity one at each endpoint. Between \(q\pi\) and \((q+1)\pi\) the index is \(q\) and nullity zero. Exercise G.4 will also obtain this count directly from a finite matrix. □

**Exercise G.2 (moving endpoints).** Suppose \(F\) varies a unit-speed geodesic on \([0,b]\), with endpoint curves \(p(s)=F(s,0)\), \(q(s)=F(s,b)\). Retain their accelerations in the energy and length second variations, and explain the endpoint-fixed tangential case.

**Solution.** Set \(a_p=\nabla_s p'(s)|_0\), \(a_q=\nabla_s q'(s)|_0\). These are exactly \(A(0),A(b)\) in A.4, since restriction to a parameter edge commutes with the pullback derivative, [Linear connections B.2](linear-and-affine-connections.md#theorem-b-2). Therefore
\[
\begin{aligned}
E''(0)&=I(V,V)+\langle a_q,T(b)\rangle-\langle a_p,T(0)\rangle,\\
L''(0)&=I(V^\perp,V^\perp)
       +\langle a_q,T(b)\rangle-\langle a_p,T(0)\rangle.
\end{aligned}
\tag{G.3}
\]
These accelerations depend on the endpoint curves, not just on their initial velocities. If the endpoints are fixed, both are zero. For an endpoint-fixed tangential field \(V=fT\), \(f(0)=f(b)=0\), A.4 then gives
\[
E''(0)=\int_0^b(f')^2\,dt,\qquad L''(0)=0.
\]
The energy value is strictly positive unless the field vanishes. More generally, if endpoints are free, even a tangential field can have a nonzero length second variation because the acceleration term in (G.3) remains. This accounts for every term in both formulas. □

**Exercise G.3 (extend past a conjugate point).** Without using the Morse index-counting formula, prove that a geodesic extending strictly past a conjugate time is not minimizing. Give an explicit negative direction for a unit-sphere arc of length \(b>\pi\).

**Solution.** Let \(J\ne0\) vanish at \(0,\tau\), where \(0<\tau<b\), and extend it by zero to \([0,b]\). It is normal by B.2. Choose a smooth normal \(W\), zero at \(0,b\), with \(W(\tau)=-J'(\tau)\), using a cutoff in a parallel frame. B.1 gives
\[
I(J,J)=0,\qquad I(J,W)=-|J'(\tau)|^2<0.
\]
The strict inequality follows because \(J(\tau)=J'(\tau)=0\) would force \(J=0\) by A.1. Hence
\[
I(J+\varepsilon W,J+\varepsilon W)
 =-2\varepsilon|J'(\tau)|^2+\varepsilon^2 I(W,W)<0
\]
for sufficiently small positive \(\varepsilon\). A.2 smooths this field while preserving its negative square, by the integral estimates used in D.1; those estimates use no index formula. A.3–A.4 applied to its exponential variation give smaller length and energy. This proves the obstruction directly.

For the sphere take a parallel unit normal \(E\) and the smooth field
\(V(t)=\sin(\pi t/b)E(t)\). Since the unit sphere has curvature one,
\[
I(V,V)=\int_0^b\left((\pi/b)^2\cos^2(\pi t/b)
                         -\sin^2(\pi t/b)\right)\,dt
       =\frac{\pi^2-b^2}{2b}<0.
\tag{G.4}
\]
The two integrals of squared sine and cosine are \(b/2\), by their addition identities and integration over a half-period, as follows from [Connections E.1](connections-and-parallel-transport.md#lemma-e-1). The field is endpoint-fixed, so it gives the required explicit decreasing direction. □

**Exercise G.4 (moving-node crossings and the sphere matrix).** Prove the Morse index formula using the moving-node family (D.2) by computing its derivative on each kernel and applying E.2. Then calculate the complete broken-Jacobi matrix for a unit-sphere arc with equally spaced sufficiently short nodes, and determine its index and nullity directly.

**Solution.** Work in a parallel orthonormal normal frame and fix \(r_0>0\). Write \(j_r\) for the interpolant of a fixed node vector \(x\) in the family (D.2). Suppose \(x\in\ker Q(r_0)\). Then \(j=j_{r_0}\) is a global Jacobi field, by C.3 and B.1. On each moving subinterval let \(z=\partial_rj_r|_{r_0}\), differentiating at fixed \(t\). Since the value at node \(t_i(r)\) is fixed,
\[
z(t_i(r_0))+j'(t_i(r_0))\,t_i'(r_0)=0.
\tag{G.5}
\]
The global field \(j\) has matching one-sided derivatives. Hence the two values of \(z\) agree at an interior node. At the endpoints (G.5) gives \(z(0)=0\) and \(z(r_0)=-j'(r_0)\).

Differentiate the form, piece by piece, with its moving limits. At internal nodes the limit terms cancel: the integrand
\(|j'|^2-Bj\cdot j\) has equal values on both sides. The upper endpoint contributes \(|j'(r_0)|^2\), since \(j(r_0)=0\). The remaining terms are twice the index pairing with \(z\):
\[
\begin{aligned}
Q'(r_0)(x,x)
 &=|j'(r_0)|^2
   +2\int_0^{r_0}(j'\cdot z'-Bj\cdot z)\,dt\\
 &=|j'(r_0)|^2+2[j'\cdot z]_0^{r_0}
 =-|j'(r_0)|^2.
\end{aligned}
\tag{G.6}
\]
The second equality uses the Jacobi equation and continuity of \(z\). Final-data uniqueness makes \(j\mapsto j'(r_0)\) injective on the endpoint kernel. Thus this derivative is negative definite there. E.2 says that the finite index increases by exactly the conjugate multiplicity at every crossing and takes the lower value at the crossing itself. It begins at zero by C.1. C.4 supplies finitely many crossings, and C.2 makes the index constant between them. This proves the sum over \(0<t<b\) directly, without using D.1; B.1 and C.3 give its nullity and maximal nonpositive dimension as well.

Now let \(\gamma\) be a unit-speed arc on the unit \(n\)-sphere, \(n\geq2\). Take \(N\geq2\) equally spaced pieces of length
\(\delta=b/N<\min\{\sqrt2,\pi\}\). The normal curvature matrix is \(I_{n-1}\), by [Sectional curvature A.1](sectional-curvature-and-space-forms.md#theorem-a-1) and C.1. In one normal coordinate the solution with values \(x,y\) at the ends of a piece is
\[
j(t)=\frac{\sin(\delta-t)}{\sin\delta}\,x
       +\frac{\sin t}{\sin\delta}\,y,\qquad 0\leq t\leq\delta.
\]
Direct differentiation gives \(j''+j=0\) and the two endpoint values, so C.1 identifies it with the unique interpolant. Its contribution to the form is
\[
[j'j]_0^\delta
 =\frac{\cos\delta(x^2+y^2)-2xy}{\sin\delta}.
\tag{G.7}
\]
For normal node values \(x_0=x_N=0\), \(x_1,\ldots,x_{N-1}\), the complete matrix in each normal direction is therefore
\[
H_\delta=\frac1{\sin\delta}
\begin{pmatrix}
2\cos\delta&-1&0&\cdots&0\\
-1&2\cos\delta&-1&\ddots&\vdots\\
0&-1&2\cos\delta&\ddots&0\\
\vdots&\ddots&\ddots&\ddots&-1\\
0&\cdots&0&-1&2\cos\delta
\end{pmatrix}.
\tag{G.8}
\]
For \(N=2\) this means the single entry \(2\cot\delta\). The full normal matrix is the direct sum of \(n-1\) copies of (G.8).

For each \(k=1,\ldots,N-1\), the vector with components
\(x_j=\sin(jk\pi/N)\) is an eigenvector, with eigenvalue
\[
\lambda_k=\frac{2\cos\delta-2\cos(k\pi/N)}{\sin\delta}.
\tag{G.9}
\]
Indeed insert it in each row, using
\(\sin((j-1)\theta)+\sin((j+1)\theta)=2\cos\theta\sin(j\theta)\)
and its zero boundary components at \(j=0,N\). These identities follow from the circle multiplication in [Connections E.1](connections-and-parallel-transport.md#lemma-e-1). Each vector is nonzero because its first component is positive. Cosine is strictly decreasing on \((0,\pi)\), by [Sectional curvature B.2](sectional-curvature-and-space-forms.md#lemma-b-2), so the \(N-1\) eigenvalues are distinct. Eigenvectors of a symmetric matrix with distinct eigenvalues are orthogonal: taking their mutual inner product in the two eigenvalue equations proves this. They therefore form a basis.

Since \(\sin\delta>0\), (G.9) is negative exactly when \(k\pi<b\), and zero exactly when \(k\pi=b\). Our choice \(b<N\pi\) ensures that all positive integers satisfying either condition already lie in \(1,\ldots,N-1\). Thus the normal index is
\[
(n-1)\#\{k\in\mathbb Z_{>0}:k\pi<b\},
\]
and its nullity is \(n-1\) when \(b\) is a positive integer multiple of \(\pi\), and zero otherwise.

If tangential node coordinates are also included, their interpolants are linear. A piece contributes \((y-x)^2/\delta\), so their complete matrix has diagonal \(2/\delta\) and adjacent off-diagonal entries \(-1/\delta\). The same sine vectors have eigenvalues
\((2-2\cos(k\pi/N))/\delta>0\).
This supplies the entire matrix for all energy fields and confirms that the tangential block adds no index or nullity. In particular on \(S^2\) the values at \(b=\pi,2\pi,3\pi\) are exactly \(0,1,2\), with endpoint nullity one, in agreement with G.1. □

## Further reading

- Urs Lang, [*Lecture Notes on Riemannian Geometry*, ETH Zürich, 16 June 2020](https://metaphor.ethz.ch/x/2020/fs/401-3532-08L/sc/DG2_16June2020.pdf), Theorem 1.15 and §§3.1, 3.4–3.16, for variations, Jacobi fields, conjugacy, the index form and curvature consequences.
- Eduardo V. Sodré, [*Revisiting Arnold's topological proof of the Morse index theorem*, arXiv:2307.00655v1, 2 July 2023](https://arxiv.org/pdf/2307.00655v1), §2 and the definite-crossing calculation in §5, for the Jacobi operator, the uniform spectral lower bound and index-counting geometry.
