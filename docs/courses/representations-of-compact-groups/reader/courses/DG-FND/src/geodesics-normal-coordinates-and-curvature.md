# Geodesics, normal coordinates and curvature

*Written by GPT-6.1 Sol (OpenAI), Ultra effort, October 2026. Draft; self-checked by the writing AI, GPT-6.1 Sol, at Ultra effort. Original text dedicated to the public domain under CC0 1.0.*

## 1. Launching a geodesic

Let \(M\) be a finite-dimensional Hausdorff second-countable smooth manifold, with a smooth linear connection \(\nabla\). No metric or torsion condition is assumed. In coordinates write

\[
\nabla_{\partial_i}\partial_j=\Gamma^k_{ij}\partial_k.
\]

Repeated indices are summed. The first lower index gives the direction of differentiation. If \(\gamma(t)\) has coordinates \(x(t)\), the derivative along it is

\[
(D_tV)^k=\dot V^k+\Gamma^k_{ij}(x(t))\dot x^iV^j.
\tag{1.1}
\]

A \(C^2\) curve is a **geodesic with affine parameter** if \(D_t\dot\gamma=0\). Equivalently,

\[
\ddot x^k+\Gamma^k_{ij}(x)\dot x^i\dot x^j=0.
\tag{1.2}
\]

Constant curves are included.

**Theorem 1.1 (initial data and parameter).** Every \(p\in M\) and \(v\in T_pM\) determine a unique maximal geodesic \(\gamma_v:I_v\to M\), with \(0\in I_v\), \(\gamma_v(0)=p\) and \(\dot\gamma_v(0)=v\). It is smooth and depends smoothly on its initial data wherever its solution is defined. A nonconstant geodesic has nowhere-zero velocity. A regular change of parameter preserves its geodesic equation exactly when the change is affine.

**Proof.** Put \(z=\dot x\). Equation (1.2) becomes the first-order system

\[
\dot x^k=z^k,\qquad
\dot z^k=-\Gamma^k_{ij}(x)z^iz^j.
\tag{1.3}
\]

This is a smooth vector field on \(TM\). To check the assertion under a change of coordinates, apply the chain rule to the first derivative of the new coordinates along a curve. The second derivative has the Hessian term of the coordinate change; the transformation of the connection in (1.1) cancels it. Thus a solution in one tangent chart gives a solution in every overlapping tangent chart. Local existence, uniqueness and smooth dependence follow from the local-flow theorem in Local tools for bundles and transport. Glue all extensions of the same initial solution. Uniqueness makes them agree on overlapping intervals and gives one solution on their union, an open interval \(I_v\). It is maximal by construction.

Smooth dependence persists over every compact subinterval of \(I_v\). Cover its trajectory in \(TM\) by finitely many flow charts and compose their smooth solution maps. This also shows that nearby initial data have solutions over that subinterval. Smoothness in time follows from (1.3).

If the velocity vanishes at some time, the constant curve at that point has the same initial data there. Uniqueness forces the two curves to agree on their entire common interval. Hence a nonconstant solution has no zero velocity.

Let \(\eta(s)=\gamma(t(s))\), where \(t\) is \(C^2\) and \(t'\ne0\). The derivative rule along curves gives

\[
D_s\dot\eta=(t')^2D_t\dot\gamma+t''\dot\gamma.
\tag{1.4}
\]

For a nonconstant geodesic the first term is zero and \(\dot\gamma\ne0\), so \(\eta\) is geodesic precisely when \(t''=0\). This means \(t(s)=as+b\), \(a\ne0\). For a constant curve every change of parameter works; the nonconstant hypothesis is essential. □

For \(s\in\mathbb R\), uniqueness also gives the scaling identity

\[
\gamma_{sv}(t)=\gamma_v(st)
\tag{1.5}
\]

on the corresponding domains. For \(s=0\) both sides are constant.

There is a useful description upstairs. Let \(u:\mathbb R^n\to T_pM\) be a frame, put \(a=u^{-1}v\), and let \(B(a)\) be the standard horizontal field, defined by \(\theta(B(a))=a\). Its integral curve \(u(t)\) is horizontal and projects to a curve with velocity \(u(t)a\). That vector is parallel, so the projected curve is a geodesic. Conversely, horizontally lift a geodesic from \(u\). Its parallel velocity has constant coordinates \(a\) in that lift, hence the lift is an integral curve of \(B(a)\).

The connection is **geodesically complete** if all the intervals \(I_v\) equal \(\mathbb R\). This holds if and only if every standard horizontal field \(B(a)\) on \(L(M)\) is complete. In one direction its complete integral curve projects to every required geodesic. In the other direction lift a complete geodesic on each compact time interval. Whole-interval parallel transport exists by Connections and parallel transport, Theorem 4.1. Uniqueness glues these lifts for all real time, giving the complete integral curve of \(B(a)\). Completeness is an extra global property; the local existence theorem does not imply it.

Geodesics also forget one part of the connection. The torsion is

\[
T(X,Y)=\nabla_XY-\nabla_YX-[X,Y].
\]

It is a smooth skew tensor by Linear and affine connections, Proposition 3.1. Therefore

\[
\nabla^s_XY=\nabla_XY-\tfrac12T(X,Y)
\tag{1.6}
\]

is another connection. Its torsion is zero and it has exactly the same geodesics with the same affine parameters, since \(T(\dot\gamma,\dot\gamma)=0\). More generally, if \(\nabla'=\nabla+S\), the two connections have the same parametrized geodesics if and only if \(S(X,Y)+S(Y,X)=0\).

Indeed, skewness makes \(S(\dot\gamma,\dot\gamma)=0\). Conversely, launch their common geodesic with any initial vector \(v\) at any point. Subtracting its two equations gives \(S(v,v)=0\). Polarization,

\[
\begin{gathered}
S(v+w,v+w)-S(v,v)-S(w,w)\\
=S(v,w)+S(w,v),
\end{gathered}
\]

proves skewness. Thus geodesics determine the symmetric part of a connection, while parallel transport retains additional information.

## 2. Coordinates made from initial vectors

Define

\[
\begin{gathered}
\mathcal D=\{v\in TM:1\in I_v\},\\
\operatorname{Exp}(v)=\gamma_v(1).
\end{gathered}
\tag{2.1}
\]

Write \(\exp_p\) for its restriction to \(T_pM\). The domain \(\mathcal D\) is open, contains the zero section, and \(\operatorname{Exp}\) is smooth. For an initial vector in \(\mathcal D\), Theorem 1.1 gives existence and smooth dependence for nearby initial data throughout \([0,1]\). A zero initial vector gives a constant solution for all time, so these observations prove all three assertions. No completeness assumption is needed. Equation (1.5) implies

\[
\exp_p(tv)=\gamma_v(t)
\tag{2.2}
\]

whenever the indicated geodesic and exponential values are defined.

**Theorem 2.1 (normal coordinates).** For every \(p\), the differential \((d\exp_p)_0:T_pM\to T_pM\) is the identity. There is an open ball \(W\) about zero in \(T_pM\) on which \(\exp_p\) is a diffeomorphism onto a neighbourhood \(U\) of \(p\). After choosing a basis of \(T_pM\), its inverse gives coordinates \(x\) on \(U\) in which

\[
x(\exp_p(tv))=t\,x_*(v).
\tag{2.3}
\]

Here \(x_*(v)\) means the components of \(v\) in the chosen basis. At the centre,

\[
\begin{gathered}
\Gamma^k_{ij}(p)+\Gamma^k_{ji}(p)=0,\\
\Gamma^k_{ij}(p)=\tfrac12T^k_{ij}(p).
\end{gathered}
\tag{2.4}
\]

Consequently every coefficient vanishes there if and only if the torsion vanishes at \(p\).

**Proof.** For any fixed \(v\), equation (2.2) holds for \(t\) near zero. Differentiation at zero gives

\[
(d\exp_p)_0(v)=\dot\gamma_v(0)=v.
\]

The inverse function theorem from Local tools for bundles and transport gives a diffeomorphism on a neighbourhood of zero. Restrict it to a sufficiently small ball \(W\). Its line segments through zero remain in \(W\), so (2.2) proves (2.3). It also proves uniqueness of the germ of these coordinates for a fixed initial basis: a chart with property (2.3) has the same inverse map \(v\mapsto\exp_p(v)\).

Substitute \(x(t)=ta\) into the geodesic equation at \(t=0\). For every \(a\in\mathbb R^n\),

\[
\Gamma^k_{ij}(p)a^ia^j=0.
\]

Polarization gives the first identity in (2.4). In a coordinate frame \([\partial_i,\partial_j]=0\), so the definition of torsion gives \(T^k_{ij}=\Gamma^k_{ij}-\Gamma^k_{ji}\). Combining the two identities gives the second one. □

The radial identity holds throughout the normal chart:

\[
\Gamma^k_{ij}(x)x^ix^j=0.
\tag{2.5}
\]

For \(x\ne0\), use the radial geodesic through that point and multiply its equation by the square of its radial parameter. At zero the identity is immediate. A radial line is therefore geodesic with its linear parameter, whereas a general straight line in the chart need not be geodesic.

At a torsion-free centre the tensor-derivative formula has no connection correction terms. Thus the components of \(\nabla S\) there are the ordinary partial derivatives of the components of any tensor \(S\). Torsion-free at the point is sufficient for this conclusion; vanishing torsion on the whole chart is unnecessary.

We will need one uniform version of normal coordinates. It concerns geodesics, without a length-minimizing assertion.

**Theorem 2.2 (convex normal neighbourhoods).** Every point has a neighbourhood \(V\) such that each pair \(x,y\in V\) is joined by exactly one affinely parametrized geodesic segment \(\gamma:[0,1]\to V\) with endpoints \(x,y\). This segment depends smoothly on \((x,y)\). For each \(x\in V\), an open star-shaped neighbourhood \(W_x\subset T_xM\) of zero is mapped diffeomorphically by \(\exp_x\) onto \(V\).

**Proof.** Work in a coordinate chart with the given point at zero, using Euclidean norms only for this proof. Consider the map

\[
\Phi(x,v)=(x,\exp_xv).
\]

At \((0,0)\), its differential is

\[
(\delta x,\delta v)\longmapsto
(\delta x,\delta x+\delta v).
\]

Indeed, \(\exp_x0=x\), and Theorem 2.1 supplies the derivative in \(v\). The differential is invertible. Restrict \(\Phi\) to an open neighbourhood \(O\) on which it is a diffeomorphism onto an open neighbourhood of \((0,0)\). Choose numbers \(a,b>0\) with

\[
\{|x|<a,\ |v|<b\}\subset O.
\tag{2.6}
\]

On a sufficiently small closed coordinate ball, smoothness supplies \(K\ge1\) such that

\[
|\Gamma(x)(z,z)|\le K|z|^2.
\]

Choose an outer radius \(c>0\) in this ball with \(Kc<1/2\). For any geodesic contained in that outer ball, \(F(t)=|x(t)|^2\) obeys

\[
\begin{aligned}
F''(t)&=2|\dot x|^2\\
&\quad-2x\cdot\Gamma(x)(\dot x,\dot x)\\
&\ge|\dot x|^2.
\end{aligned}
\tag{2.7}
\]

After shrinking the neighbourhood of endpoint pairs, the inverse \(\Phi^{-1}(x,y)=(x,v(x,y))\) gives geodesic segments defined throughout \([0,1]\) and contained in \(|x|<c\). This follows from smooth dependence and compactness of \([0,1]\): the segment for \((0,0)\) is constant, and finitely many time neighbourhoods control all nearby segments. Arrange also that these initial vectors satisfy \(|v(x,y)|<b\).

Choose \(r>0\) small enough that every pair in \(B_r\times B_r\) lies in this endpoint neighbourhood, \(r<a\),

\[
4r<\frac1{4K},\qquad 4r e^{4Kr}<b.
\tag{2.8}
\]

Let \(V=B_r\). Equation (2.7) makes \(F\) convex along the constructed segment, hence

\[
F(t)\le(1-t)|x|^2+t|y|^2<r^2.
\]

So that segment stays in \(V\).

We must exclude a different segment in \(V\) with a large initial velocity. Let such a segment be nonconstant and let \(\ell\) be its Euclidean arc length parameter. Its velocity never vanishes, by Theorem 1.1. If \(w=dx/d\ell\) is its unit tangent and \(h=|\dot x|\), equation (1.2) gives

\[
\left|\frac{dw}{d\ell}\right|\le2K,\qquad
\left|\frac{d\log h}{d\ell}\right|\le K.
\tag{2.9}
\]

For the first bound, differentiate \(\dot x/h\), project \(\ddot x\) onto the orthogonal complement of \(\dot x\), and divide by \(h^2\); the stated bound follows from \(|\ddot x|\le Kh^2\). The second follows from \(|\dot h|\le Kh^2\), dividing by \(h^2\).

For \(0\le\ell\le1/(4K)\), the first bound gives \(w(\ell)\cdot w(0)\ge1-2K\ell\ge1/2\). If the total arc length \(L\) were at least \(4r\), the displacement at arc length \(4r\) would have component at least \(2r\) in direction \(w(0)\). This contradicts both points being in the open ball \(B_r\). Thus \(L<4r\). The second bound gives \(h(t)\ge h(0)e^{-KL}\), and integration over \(0\le t\le1\) yields

\[
|\dot x(0)|\le L e^{KL}<4r e^{4Kr}<b.
\]

Its initial data therefore lie in \(O\), by (2.6). The injectivity of \(\Phi|_O\) forces its initial vector to be \(v(x,y)\), so initial-value uniqueness identifies the segments. A constant segment is covered as well; any competing nonconstant segment has just been excluded by the same argument.

For a fixed \(x\in V\), put \(W_x=\{v(x,y):y\in V\}\). The inverse-function charts make this an open neighbourhood of zero in \(T_xM\), and \(\exp_x:W_x\to V\) a diffeomorphism. If \(v\in W_x\) and \(0\le t\le1\), its geodesic segment stays in \(V\), so \(\exp_x(tv)\in V\). Also \(|tv|<b\); equation (2.6) and the injectivity of \(\Phi\) identify \(tv\) with the vector assigned to this endpoint. Hence \(tv\in W_x\). This proves star-shapedness and completes the proof. □

This is Whitehead's local convexity theorem. The quantitative velocity bound in the proof makes the uniqueness assertion apply to every segment contained in \(V\), rather than only to the small initial vectors in the inverse-function chart. Length minimization requires a Riemannian metric and will be proved separately.

