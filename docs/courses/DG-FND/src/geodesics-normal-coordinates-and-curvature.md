# Geodesics, normal coordinates and curvature

A connection determines trajectories from initial vectors, local coordinates from its exponential map, and curvature through parallel transport. This lesson proves these constructions for arbitrary smooth linear connections, including torsion, convex neighbourhoods, curvature jets and holonomy. Complete calculations distinguish local and global behaviour on the line, plane, torus and sphere. Every proof uses freely accessible construction material and exact earlier programme proofs.

## A. From a connection to its trajectories

Let \(M\) be a finite-dimensional Hausdorff, second-countable smooth manifold without boundary, and let \(\nabla\) be a smooth real connection on \(TM\). No metric or torsion hypothesis is imposed. In a coordinate frame our convention is \(\nabla_{\partial_i}\partial_j=\Gamma^k_{ij}\partial_k\), with summation over repeated indices. The complete earlier chapter [Linear and affine connections](linear-and-affine-connections.md), abbreviated **Linear**, proves derivatives along maps, tangent connectors and all connection axioms. **Local** refers to [Local tools](local-tools-for-bundles-and-transport.md), and **PB** to [Principal bundles](principal-bundles-and-associated-bundles.md).

The free construction source is Peter W. Michor's exact [author manuscript, *Topics in Differential Geometry*](https://www.mat.univie.ac.at/~michor/dgbook.pdf), §§22.6–22.8. Its connector uses the opposite sign for its Christoffel symbol. All formulas below are derived with the programme convention \(\nabla=d+A\). Local 2.1 supplies the complete ODE proof and Local 1.2 the complete inverse-function proof; the external source replaces neither.

**Theorem A.1 (maximal geodesics and smooth flow).** A geodesic is a curve satisfying \(D_t\dot\gamma=0\). Each initial tangent vector \(v\in T_pM\) determines exactly one maximal geodesic \(\gamma_v:I_v\to M\), where \(I_v\) is an open interval containing zero. The set
\[
\mathcal D=\{(t,v):t\in I_v\}\subset\mathbb R\times TM
\]
is open, and \((t,v)\mapsto(\gamma_v(t),\dot\gamma_v(t))\) is smooth on it. If a geodesic has zero velocity at one time, it is constant. Thus every nonconstant geodesic has nowhere-zero velocity.

**Proof.** Linear B.2 gives the coordinate equation
\[
\ddot x^k+\Gamma^k_{ij}(x)\dot x^i\dot x^j=0.
\tag{A.1}
\]
Equivalently \((x,v)\) is an integral curve of the smooth field
\[
S(x,v)=(x,v;v,-\Gamma_x(v,v))\in T_{(x,v)}TM.
\tag{A.2}
\]
This is a global field. Indeed, Linear B.1 constructs the intrinsic horizontal lift \(H_u:T_pM\to T_uTM\), with \(p=\pi(u)\), whose coordinates are \((x,u;w,-\Gamma_x(w,u))\). Setting \(S(u)=H_u(u)\) gives (A.2) without choosing a chart. Its tangent projection to \(M\) is \(u\), so every integral curve \((x(t),v(t))\) has \(v=\dot x\), and conversely (A.1) gives an integral curve.

Local 2.1 gives a unique local integral curve through each tangent vector, with smooth local dependence. Any two such solutions through the same datum agree on the intersection of their time intervals: that intersection is an interval containing zero, and the uniqueness assertion in Local 2.1 applies throughout it. Take the union of all intervals of solutions through the datum. It is an open interval, because each interval contains zero. The matching solutions define a solution there. Any extension would already appear in that union, proving maximality and uniqueness.

We justify openness and smoothness on the full maximal domain, not merely near time zero. Fix \((t_0,v_0)\in\mathcal D\). The reference solution on the compact time segment between zero and \(t_0\) has compact image by Local 0.1. Cover that image by the smaller initial-value neighbourhoods from Local 2.1, on each of which a smooth local flow is defined for every time of absolute value less than some positive \(\epsilon_i\). Take a finite subcover and subdivide the reference time segment into steps of size less than half the minimum of those finitely many \(\epsilon_i\). At each step choose a member containing the reference starting value. Compose the corresponding finitely many smooth local solution maps. By continuity, shrinking the initial neighbourhood ensures that every composed intermediate value remains in the next prescribed neighbourhood. A final local flow near the endpoint allows the terminal time to vary near \(t_0\). This constructs a smooth solution for all initial data and times in a product neighbourhood of \((t_0,v_0)\). Uniqueness identifies it with the maximal solution. This proves that \(\mathcal D\) is open and its flow is smooth. The same reasoning with negative steps covers \(t_0<0\).

At \((p,0)\), (A.2) vanishes, so its constant integral curve exists for all time. If another solution has zero velocity at a time, uniqueness with that constant solution makes them agree on their common interval; maximality then makes the original maximal solution constant for all time. This proves the velocity assertion, including dimension zero. □

**Theorem A.2 (rescaling, exponential domain and completeness).** For \(a\ne0\),
\[
I_{av}=a^{-1}I_v,\qquad \gamma_{av}(t)=\gamma_v(at).
\tag{A.3}
\]
For \(a=0\), \(\gamma_0\) is the constant curve. Define
\[
\mathcal E=\{v\in TM:1\in I_v\},\qquad
\exp(v)=\gamma_v(1).
\tag{A.4}
\]
Then \(\mathcal E\) is an open neighbourhood of the zero section, \(\exp:\mathcal E\to M\) is smooth, and every fibre domain \(\mathcal E_p\) is star-shaped about zero. Whenever either expression is defined,
\[
\exp_p(tv)=\gamma_v(t).
\tag{A.5}
\]
The connection is geodesically complete, meaning \(I_v=\mathbb R\) for every \(v\), if and only if \(\mathcal E=TM\). On a nonconstant geodesic a regular \(C^2\) change of parameter preserves the geodesic equation if and only if the change is affine with nonzero slope.

**Proof.** The chain rule in Linear B.2 gives
\[
D_t\frac d{dt}\gamma_v(at)=a^2(D_s\dot\gamma_v)(at)=0.
\]
Its initial velocity is \(av\); A.1 identifies it with \(\gamma_{av}\) on \(a^{-1}I_v\). Applying the same argument with \(1/a\) proves equality of the maximal intervals: a proper extension on either side would extend the other by inverse rescaling. This proves (A.3), including negative \(a\).

Openness and smoothness in (A.4) follow by restricting A.1's domain and flow to time one. Every zero vector belongs to it by the constant solution. If \(v\in\mathcal E_p\) and \(0<a\le1\), then \(a\in I_v\), since \(I_v\) is an interval containing zero and one. Equation (A.3) gives \(av\in\mathcal E_p\); the case \(a=0\) is already proved. The same equation gives (A.5) and equality of its two domains, also for negative \(t\), with the case \(t=0\) immediate. Completeness implies \(\mathcal E=TM\). Conversely, if every vector belongs to \(\mathcal E\), then every multiple \(tv\) does; (A.5) makes every real \(t\) belong to \(I_v\), proving completeness.

For a general \(C^2\) parameter function \(s=\phi(t)\), the chain and product rules give
\[
D_t\frac d{dt}\gamma(\phi(t))
 =\phi'(t)^2D_s\dot\gamma(\phi(t))+\phi''(t)\dot\gamma(\phi(t)).
\tag{A.6}
\]
For a nonconstant geodesic A.1 makes the last vector nowhere zero, so this vanishes precisely when \(\phi''=0\). Local 0.3 then gives \(\phi(t)=at+b\) on the parameter interval. Regularity means \(a\ne0\). Conversely every such change satisfies (A.6). A constant curve remains geodesic under every change of parameter; the nonconstant hypothesis is essential. □

**Theorem A.3 (what the geodesics determine).** Two connections have the same affinely parametrized geodesics with every initial tangent vector if and only if their difference \(B(X,Y)\) is alternating in \(X,Y\). Every connection therefore has the same geodesics as the unique torsion-free connection
\[
\nabla^{\mathrm s}_XY=\nabla_XY-\tfrac12T(X,Y).
\tag{A.7}
\]
Conversely, a smooth second-order field on all of \(TM\), homogeneous of degree two in its fibre acceleration, determines a unique torsion-free connection whose geodesic field it is. Smoothness at the zero section is part of this assertion.

**Proof.** Linear A.3 makes the difference a bilinear tensor \(B\). In (A.1), changing the connection adds \(B(\dot\gamma,\dot\gamma)\). If \(B\) is alternating, this is zero and A.1's uniqueness gives the same maximal geodesics. Conversely equality of the curves with initial velocity \(v\), evaluated in their two equations at time zero, gives \(B_p(v,v)=0\) for every \(p,v\). Expanding \(B(v+w,v+w)=0\) and subtracting the two diagonal equalities gives \(B(v,w)+B(w,v)=0\). Linear D.4 proves that (A.7) is torsion-free and preserves the geodesic equation. If two torsion-free connections had these same geodesics, their difference would be both symmetric, by their torsion formula, and alternating, hence zero.

For the converse write a second-order field in a chart as \((x,v;v,F(x,v))\), with \(F(x,av)=a^2F(x,v)\) for every real \(a\). Differentiate this identity twice in \(a\) at zero, using smoothness there and Local 0.3. It gives
\[
F(x,v)=\tfrac12D_v^2F(x,0)[v,v].
\]
The second derivative is a symmetric bilinear form by the mixed-partial proof in PB C.3. Set \(\Gamma_x(v,w)=-\tfrac12D_v^2F(x,0)[v,w]\). These coefficients are smooth and symmetric. Under a coordinate change \(y=f(x)\), the acceleration transforms as \(F'(f(x),df_xv)=df_xF(x,v)+d^2f_x(v,v)\). Polarizing this equality yields
\[
\Gamma'_{f(x)}(df_xv,df_xw)
 =df_x\Gamma_x(v,w)-d^2f_x(v,w).
\tag{A.8}
\]
This is exactly the connection change rule: for local fields \(X,Y\), the extra term \(d^2f(X,Y)\) in \(d(df\,Y)(X)\) cancels the last term of (A.8). Thus \(dY(X)+\Gamma(X,Y)\) defines a global derivative satisfying the axioms, and its symmetry gives zero torsion by Linear D.1. Its field is the prescribed one. The first part proves uniqueness. A homogeneous field defined only away from zero has not met the smoothness hypothesis and is not covered by this conclusion. □

**Example A.4 (a globally invertible exponential for an incomplete connection).** On \(\mathbb R\) take \(\nabla_{\partial_x}\partial_x=\partial_x\). For initial point \(p\) and velocity \(v\),
\[
\gamma_v(t)=p+\log(1+vt),\qquad
I_v=\{t:1+vt>0\}.
\tag{A.9}
\]
For \(v=0\) this means the constant curve on all of \(\mathbb R\). The full exponential domain at every \(p\) is \((-1,\infty)\), and
\[
\exp_p(v)=p+\log(1+v)
\tag{A.10}
\]
is a diffeomorphism of that domain onto \(\mathbb R\). Nevertheless the connection is incomplete.

**Proof.** Apply Local 2.3 to the multiplicative Lie group \(\mathbb R_{>0}\). Its identity-starting exponential \(E\) satisfies \(E'=E\), \(E(0)=1\), \(E(t+s)=E(t)E(s)\), and is positive by its target. Hence it is strictly increasing. For \(t\ge0\), \(E(t)=1+\int_0^tE(s)\,ds\ge1+t\), so it tends to infinity; \(E(-t)=1/E(t)\) makes it tend to zero as \(t\to-\infty\). Every \(u>0\) is attained: choose \(a<b\) with \(E(a)<u<E(b)\) and take \(c=\sup\{t\in[a,b]:E(t)\le u\}\), using Local 0.0's real supremum property. Continuity forces \(E(c)=u\); a smaller value would permit a larger member of the set, and a larger value would exclude members approaching \(c\) from below. Thus the image is \((0,\infty)\). Local 1.2 supplies a smooth inverse \(\log\), whose derivative is \(1/u\) by differentiating \(E(\log u)=u\). This justifies all logarithmic facts used here.

For (A.9), direct differentiation gives \(\dot\gamma=v/(1+vt)\) and \(\ddot\gamma=-v^2/(1+vt)^2=-\dot\gamma^2\), which is (A.1) for this connection. The initial data are \(p,v\); A.1 supplies uniqueness. For nonzero \(v\), the finite boundary time of the indicated interval has \(1+vt\to0^+\), hence \(\gamma_v(t)\to-\infty\). No continuous extension as an \(\mathbb R\)-valued curve across that endpoint exists. The other endpoint is infinite, proving maximality. Evaluating at time one gives the domain and (A.10). Its smooth inverse is \(q\mapsto E(q-p)-1\). Taking, for instance, \(v=1\) gives the finite lower endpoint \(-1\), proving incompleteness. □

## B. Local endpoint coordinates and convexity

Michor's exact free author manuscript, §22.7, supplies the exponential-map construction used here. We prove the stronger endpoint uniqueness needed for convex neighbourhoods by an explicit speed estimate. The argument applies to every smooth linear connection, with arbitrary torsion; no length-minimization theorem for a metric is assumed.

**Theorem B.1 (normal coordinates and local endpoint inversion).** The vertical differential \((d\exp_p)_0:T_pM\to T_pM\) is the identity. Some open ball about zero in \(T_pM\) is mapped diffeomorphically onto a neighbourhood of \(p\). With a chosen basis, the inverse coordinates satisfy
\[
x(\exp_p(tv))=tv
\tag{B.1}
\]
when \(tv\) lies in this ball. At their centre,
\[
\Gamma^k_{ij}(p)+\Gamma^k_{ji}(p)=0,\qquad
\Gamma^k_{ij}(p)=\tfrac12 T^k_{ij}(p).
\tag{B.2}
\]
Thus all coefficients vanish there exactly when the torsion vanishes there. Moreover, near \((p,0)\) in \(TM\), the endpoint map
\[
\Psi(v)=(\pi(v),\exp(v))
\tag{B.3}
\]
is a diffeomorphism onto an open neighbourhood of \((p,p)\) in \(M\times M\).

**Proof.** For \(v\in T_pM\), equation (A.5) gives
\((d\exp_p)_0v=\left.\frac d{dt}\right|_0\gamma_v(t)=v\).
Local 1.2 makes \(\exp_p\) a diffeomorphism between neighbourhoods of zero and \(p\). Restrict its source to a smaller open Euclidean ball in a chosen basis. The restricted image is open because the original diffeomorphism has a continuous inverse. The inverse coordinates then give (B.1). Their tangent identification at \(p\) is the chosen basis, by the just-proved differential.

Each curve \(t\mapsto tv\) is the coordinate expression of a geodesic near time zero. Substitution in (A.1) at zero yields \(\Gamma_p(v,v)=0\) for every \(v\). Polarization gives the first equality in (B.2). Linear D.1 gives \(T^k_{ij}=\Gamma^k_{ij}-\Gamma^k_{ji}\) in any coordinate frame, proving the second equality and its two-way vanishing assertion. More generally these coordinates satisfy \(\Gamma_x(x,x)=0\) at every point in their radial domain: at \(x=tv\), the radial geodesic has zero coordinate acceleration and constant velocity \(v\); multiply its equation by \(t^2\). The case \(x=0\) was already handled.

Use a coordinate trivialization of \(TM\). Along the zero section, \(\exp_x(0)=x\), so the derivative of \(\exp\) in the base direction is the identity. Its fibre derivative is the identity by the first part. Thus
\[
d\Psi_{(p,0)}=
\begin{pmatrix}I&0\\ I&I\end{pmatrix}.
\]
Its inverse sends \((a,b)\) to \((a,b-a)\). Local 1.2 applies and proves the last assertion. This is a local inverse near one diagonal point; no assertion of global injectivity of the full exponential domain is being used. □

**Lemma B.2 (a small contained geodesic cannot have a large velocity).** Suppose the connection coefficients on a Euclidean coordinate ball satisfy
\[
|\Gamma_x(v,v)|\le C|v|^2
\tag{B.4}
\]
for a constant \(C\ge0\). Choose \(\rho>0\) such that
\(16C\rho\le\tfrac12\) and \(e^{8C\rho}<2\).
Every geodesic \(\gamma:[0,1]\to B(0,\rho)\) has
\[
\max_{0\le t\le1}|\dot\gamma(t)|<16\rho.
\tag{B.5}
\]

**Proof.** The constant case is immediate. Otherwise A.1 makes the speed \(w=|\dot\gamma|\) positive everywhere. Its Euclidean arclength parameter
\(\ell(t)=\int_0^t w(r)\,dr\) is smooth with positive derivative, and has a smooth inverse on its image by Local 1.2. Write \(u=\dot\gamma/w\) for its unit tangent. Differentiating and using (A.1), (B.4) gives
\[
\left|\frac{du}{d\ell}\right|\le2C,\qquad
\left|\frac{d\log w}{d\ell}\right|\le C.
\tag{B.6}
\]
For detail, \(w'=\dot\gamma\cdot\ddot\gamma/w\), so \(|w'|\le|\ddot\gamma|\le Cw^2\). Therefore \(u'=\ddot\gamma/w-\dot\gamma w'/w^2\) has norm at most \(2Cw\); division by \(\ell'=w\) gives the first bound. The second is \(|w'|/w^2\le C\). The dot-product estimate used here follows by expanding the nonnegative square \(|a-tb|^2\) and minimizing over \(t\). The logarithm and its derivative were proved in A.4.

Let \(L=\ell(1)\). If \(L\ge8\rho\), the first estimate, integrated with Local 0.3, gives \(u(0)\cdot u(\ell)\ge1-2C\ell\ge\tfrac12\) for \(0\le\ell\le8\rho\). Integrating \(d\gamma/d\ell=u\) then gives a displacement of at least \(4\rho\) in the \(u(0)\) direction over that portion of the curve. But two points in \(B(0,\rho)\) have distance less than \(2\rho\), a contradiction. Hence \(L<8\rho\).

The second estimate in (B.6) gives \(w(t)\le e^{CL}w(r)\) for every two times, by integration and the increasing exponential of A.4. Integrating with respect to \(r\) on \([0,1]\) yields \(w(t)\le e^{CL}L<2(8\rho)=16\rho\). This proves (B.5). Both required choices of \(\rho\) are possible by continuity of the exponential at zero, including \(C=0\). □

**Theorem B.3 (convex normal neighbourhoods for arbitrary connections).** Every point has arbitrarily small open neighbourhoods \(V\) such that any \(x,y\in V\) are joined by exactly one affinely parametrized geodesic \([0,1]\to V\) with endpoints \(x,y\). That segment depends smoothly on \((x,y)\). For each \(x\in V\) there is an open star-shaped neighbourhood \(W_x\subset T_xM\) of zero such that \(\exp_x:W_x\to V\) is a diffeomorphism.

**Proof.** Dimension zero is immediate with \(V=\{p\}\), \(W_p=\{0\}\). Otherwise put \(p=0\) in a coordinate chart contained in any prescribed neighbourhood. Choose a closed coordinate ball inside that chart. Smoothness and compactness, Local 0.1, bound the finitely many coefficients there and therefore give (B.4) for some \(C\). Shrink its radius to \(R>0\) with \(2CR\le1\), retaining the same bound. Along a geodesic lying in \(B(0,R)\),
\[
\frac{d^2}{dt^2}|\gamma(t)|^2
=2|\dot\gamma|^2-2\gamma\cdot\Gamma_\gamma(\dot\gamma,\dot\gamma)
\ge|\dot\gamma|^2\ge0.
\tag{B.7}
\]

B.1 gives an open neighbourhood \(U\) of \((0,0)\) in the coordinate tangent bundle on which \(\Psi\) is a diffeomorphism. We may shrink \(U\) so that every initial vector in it has a geodesic on \([0,1]\) lying in \(B(0,R)\). Here is the uniform justification. The constant zero solution exists at every time; A.1's open flow domain and continuity give, at each \(t\in[0,1]\), a product of a time neighbourhood and an initial-data neighbourhood on which solutions are defined and their base values lie in \(B(0,R)\). Finitely many time neighbourhoods cover \([0,1]\); intersect their initial-data neighbourhoods. This open neighbourhood of \((0,0)\) has the required property. Restrict the inverse-function neighbourhood to its intersection with it; its image is still open about \((0,0)\).

Choose \(\rho>0\) small enough that \(V=B(0,\rho)\) satisfies all of the following: \(V\subset B(0,R)\), \(V\times V\subset\Psi(U)\), \(\{(x,v):|x|<\rho,\ |v|<16\rho\}\subset U\), and the two inequalities of B.2. Each containment follows from openness about the relevant origin by reducing \(\rho\); the inequalities follow as in B.2.

For \(x,y\in V\), the inverse \(\Psi^{-1}(x,y)=(x,v(x,y))\) is smooth and supplies a geodesic joining them, lying initially by construction in \(B(0,R)\) for its entire parameter interval. Its squared coordinate norm is convex by (B.7), hence bounded above by the affine interpolation of its endpoint values. To verify this elementary convexity step, the fundamental theorem makes the derivative of a function with nonnegative second derivative nondecreasing. Its average derivative on \([0,t]\) is at most its average derivative on \([t,1]\); rearranging gives \(f(t)\le(1-t)f(0)+tf(1)\). Apply this to \(f=|\gamma|^2\). Both endpoint values are less than \(\rho^2\); thus this geodesic stays in \(V\).

Any other geodesic with the same endpoints and entirely contained in \(V\) has initial speed less than \(16\rho\), by B.2. Its initial vector therefore lies in \(U\). Injectivity of \(\Psi|_U\) forces that vector to equal \(v(x,y)\), and A.1 forces equality of the curves. This proves uniqueness among all segments contained in \(V\), including ones not initially assumed to lie in the small endpoint-inverse family.

Fix \(x\in V\) and put \(W_x=\{v(x,y):y\in V\}\). Since \(\Psi\) preserves the base coordinate, its inverse restricts on each slice to a smooth inverse for \(\exp_x\). The set \(W_x\) is open in \(T_xM\), by restricting the open source and target of this fibre-preserving diffeomorphism, and it contains zero by the unique constant segment. For \(v=v(x,y)\) and \(0<t\le1\), the reparametrized initial portion \(s\mapsto\gamma_v(ts)\) lies in \(V\) and has initial vector \(tv\). B.2 puts that vector in \(U\); uniqueness just proved identifies it with \(v(x,\gamma_v(t))\). Hence \(tv\in W_x\), and \(t=0\) is already included. This proves star-shapedness and every assertion. □

**Theorem B.4 (a normal frame with a prescribed value).** For a real or complex vector bundle with connection, any frame at \(p\) extends to a smooth local frame whose potential is zero at \(p\). In a tangent bundle this does not require zero torsion.

**Proof.** Begin with a local frame having the prescribed value: multiply any frame by the constant invertible matrix needed at \(p\). Choose real coordinates with \(x(p)=0\) and write its potential as \(A=\sum_iA_i\,dx^i\). Put
\[
g(x)=I-\sum_i x^i A_i(p).
\tag{B.8}
\]
It is invertible near \(p\), since \(g(p)=I\) and matrix inversion is open and smooth by Local 0.4. This holds for complex matrices as proved in Linear A.2. The changed frame \(e'=eg\) has the same value at \(p\), and Linear A.1 gives \(A'=g^{-1}Ag+g^{-1}dg\). At \(p\), \(dg=-A(p)\), so \(A'(p)=0\). On \(TM\), Linear D.1 then gives \(T(e'_i,e'_j)(p)=-e'_i,e'_j\). Thus such a frame can be noncoordinate when torsion is nonzero; the restriction in (B.2) on normal coordinate coefficients and this unrestricted frame construction are consistent. □

## C. Curvature on tensors and both Bianchi identities

The construction source for this part is Peter W. Michor's freely accessible [author manuscript, §§24.3–24.4](https://www.mat.univie.ac.at/~michor/dgbook.pdf). We use the programme convention \(\nabla_{\partial_i}\partial_j=\Gamma^k_{ij}\partial_k\); Michor's displayed acceleration coefficients have the opposite sign. All formulas below are derived with our convention. [Linear B.3, C.1 and D.1–D.2](linear-and-affine-connections.md) supply the complete earlier proofs of curvature, tensor differentiation, torsion and the structure identities.

**Theorem C.1 (coordinate curvature, tensor action and the second derivative).** Write \(R^l{}_{kij}\partial_l=R(\partial_i,\partial_j)\partial_k\). For every smooth linear connection,
\[
R^l{}_{kij}
=\partial_i\Gamma^l_{jk}-\partial_j\Gamma^l_{ik}
 +\Gamma^l_{im}\Gamma^m_{jk}-\Gamma^l_{jm}\Gamma^m_{ik}.
\tag{C.1}
\]
Repeated indices are summed. Curvature on any tensor bundle acts by \(R(X,Y)\) on each vector factor and by its negative dual action on each covector factor. In particular, for a vector-valued \(q\)-covariant tensor \(S\),
\[
\begin{split}
(\mathcal R(X,Y)S)(Z_1,\ldots,Z_q)
={}&R(X,Y)\bigl(S(Z_1,\ldots,Z_q)\bigr)\\
&-\sum_{\nu=1}^q
 S(Z_1,\ldots,R(X,Y)Z_\nu,\ldots,Z_q),
\end{split}
\tag{C.2}
\]
where \(\mathcal R(X,Y)=[\nabla_X,\nabla_Y]-\nabla_{[X,Y]}\) uses the induced tensor connection. Set
\(\nabla^2S(X,Y)=\nabla_X(\nabla_Y S)-\nabla_{\nabla_XY}S\).
Then
\[
\nabla^2S(X,Y)-\nabla^2S(Y,X)
=\mathcal R(X,Y)S-\nabla_{\mathcal T(X,Y)}S.
\tag{C.3}
\]
For functions this becomes
\(\nabla^2f(X,Y)-\nabla^2f(Y,X)=-df(\mathcal T(X,Y))\).

**Proof.** In the coordinate frame let \(A_i\) be the matrix with entries
\((A_i)^l{}_k=\Gamma^l_{ik}\). Linear B.3 gives
\(R_{ij}=\partial_i A_j-\partial_j A_i+[A_i,A_j]\). Matrix multiplication gives (C.1), including the order of the two last factors. The same earlier proof establishes tensoriality and skew-symmetry in \(X,Y\), so this is an intrinsic tensor formula.

On a tensor product \(s\otimes t\), apply the product rule of Linear C.1 twice. The two mixed terms in \(\nabla_X\nabla_Y(s\otimes t)\) are
\((\nabla_Ys)\otimes(\nabla_Xt)\) and
\((\nabla_Xs)\otimes(\nabla_Yt)\). They occur in the opposite-order derivative as well and cancel in its subtraction. Subtracting the product rule for \(\nabla_{[X,Y]}\) therefore leaves
\[
\mathcal R(X,Y)(s\otimes t)
=(\mathcal R(X,Y)s)\otimes t+s\otimes(\mathcal R(X,Y)t).
\tag{C.4}
\]
On a function \(f\), the operator is \(XYf-YXf-[X,Y]f=0\), by PB C.3. Apply (C.4) and contraction compatibility from Linear C.1 to the scalar evaluation \(\alpha(s)\). Its curvature is zero, so
\[
(\mathcal R(X,Y)\alpha)(s)+\alpha(R(X,Y)s)=0.
\]
This proves the negative dual action. Iterating (C.4) proves the action on every pure tensor. Such tensors span each fibre in the local tensor bases constructed in Linear C.1. Curvature is linear over functions by Linear B.3 on the induced bundle. Consequently the formula holds for arbitrary tensor sections. Evaluation on \(Z_1,\ldots,Z_q\) gives (C.2); the same argument covers several vector factors and scalar-valued tensors.

Finally, subtract the two defining second derivatives. Their difference is
\[
[\nabla_X,\nabla_Y]S-\nabla_{\nabla_XY-\nabla_YX}S.
\]
Linear D.1 says
\(\nabla_XY-\nabla_YX=[X,Y]+\mathcal T(X,Y)\).
Linearity of the derivative in its direction now proves (C.3). The scalar case uses the zero curvature already proved. These computations also show that the second derivative is tensorial in \(X,Y\): the differentiated coefficient in \(\nabla_X(\nabla_{fY}S)\) cancels that in \(\nabla_{\nabla_X(fY)}S\), and linearity in \(X\) is immediate. □

**Theorem C.2 (Bianchi identities with torsion).** With \(\sum_{\mathrm{cyc}}\) denoting the sum over \((X,Y,Z),(Y,Z,X),(Z,X,Y)\), one has
\[
\sum_{\mathrm{cyc}}R(X,Y)Z
=\sum_{\mathrm{cyc}}(\nabla_X\mathcal T)(Y,Z)
 +\sum_{\mathrm{cyc}}\mathcal T(\mathcal T(X,Y),Z),
\tag{C.5}
\]
and, as an equality of endomorphisms of \(TM\),
\[
\sum_{\mathrm{cyc}}(\nabla_XR)(Y,Z)
=-\sum_{\mathrm{cyc}}R(\mathcal T(X,Y),Z).
\tag{C.6}
\]
Both correction sums disappear for a torsion-free connection. Covariant differentiation in these formulas includes every tensor slot.

**Proof.** We first establish the conversion from exterior covariant differentiation to tensor covariant differentiation. Let \(\alpha\) be an \(E\)-valued alternating two-form, where \(E\) has a covariant derivative. Its exterior covariant derivative, from the local formula \(D\alpha=d\alpha+A\wedge\alpha\) in Curvature A.5, is
\[
(D\alpha)(X,Y,Z)
=\sum_{\mathrm{cyc}}\nabla^E_X\bigl(\alpha(Y,Z)\bigr)
 -\sum_{\mathrm{cyc}}\alpha([X,Y],Z).
\tag{C.7}
\]
Indeed the three derivative terms in the exterior-derivative formula of Curvature A.2 combine with the three \(A\)-action terms to form \(\nabla^E\); the bracket terms are unchanged. Linear C.1 gives
\[
\nabla^E_X(\alpha(Y,Z))
=(\nabla_X\alpha)(Y,Z)
 +\alpha(\nabla_XY,Z)+\alpha(Y,\nabla_XZ).
\]
In the cyclic sum, alternating the last term and relabelling the three summands turns it into
\(-\sum_{\mathrm{cyc}}\alpha(\nabla_YX,Z)\).
Thus (C.7) becomes the fully tensorial identity
\[
(D\alpha)(X,Y,Z)
=\sum_{\mathrm{cyc}}(\nabla_X\alpha)(Y,Z)
 +\sum_{\mathrm{cyc}}\alpha(\mathcal T(X,Y),Z).
\tag{C.8}
\]

Apply this first with \(E=TM\) and \(\alpha=\mathcal T\). Linear D.2 proves
\(D\mathcal T=R\wedge\operatorname{Id}_{TM}\): in a frame this is its identity
\(d\tau+A\wedge\tau=F\wedge\sigma\), and Linear D.1 identifies its terms intrinsically. The right side, on \(X,Y,Z\), is
\(R(X,Y)Z+R(Y,Z)X+R(Z,X)Y\).
Equation (C.8) proves (C.5).

For the second application let \(E=\operatorname{End}(TM)\) and \(\alpha=R\). The endomorphism connection in Linear C.1 has
\(\nabla^{\operatorname{End}}_XA=X(A)+[\Gamma(X),A]\) in any local frame. Consequently its exterior derivative on an endomorphism-valued two-form is \(dR+\Gamma\wedge R-R\wedge\Gamma\). The second structure identity of Linear D.2 says exactly that this expression vanishes for curvature. Substitution into (C.8) gives (C.6). No coordinate frame with vanishing connection coefficients or vanishing torsion was used. □

**Corollary C.3 (the metric symmetries and their hypotheses).** Suppose a nondegenerate symmetric bilinear form \(g\) is parallel. Then
\[
g(R(X,Y)Z,U)=-g(R(X,Y)U,Z).
\tag{C.9}
\]
If the connection is also torsion-free, then
\[
g(R(X,Y)Z,U)=g(R(Z,U)X,Y).
\tag{C.10}
\]
Positive definiteness is unnecessary for these two assertions.

**Proof.** Since \(\nabla g=0\), its tensor curvature is zero. The two negative covector actions proved in C.1 yield
\[
0=(\mathcal R(X,Y)g)(Z,U)
  =-g(R(X,Y)Z,U)-g(Z,R(X,Y)U).
\]
Symmetry of \(g\) proves (C.9).

Put \(K(X,Y,Z,U)=g(R(X,Y)Z,U)\). It is skew in its first two positions by C.1 and its last two by (C.9). For zero torsion, C.2 gives the cyclic relation in its first three positions. Use that relation in these four orders, with the displayed signs:
\[
\begin{aligned}
0={}&K(X,Y,Z,U)+K(Y,Z,X,U)+K(Z,X,Y,U),\\
0={}&K(Y,Z,U,X)+K(Z,U,Y,X)+K(U,Y,Z,X),\\
0={}&-K(Z,U,X,Y)-K(U,X,Z,Y)-K(X,Z,U,Y),\\
0={}&-K(U,X,Y,Z)-K(X,Y,U,Z)-K(Y,U,X,Z).
\end{aligned}
\]
The \(YZ\) terms cancel by last-pair skewness; the \(ZX\) and \(XZ\) terms cancel using both skewness rules. The \(UY\) and \(YU\) terms cancel using both rules, and the \(UX\) terms cancel by last-pair skewness. What remains is
\(2K(X,Y,Z,U)-2K(Z,U,X,Y)=0\).
Division by two proves (C.10). □

## D. Curvature derivatives and the geometry of the holonomy bundle

This part specializes complete programme proofs to the tangent frame bundle. Its providers are [Curvature C.5, G.3–G.4 and I.1](curvature-and-holonomy-groups.md), [Flat A.2–A.5 and B.1–B.2](flat-connections-and-infinitesimal-holonomy.md), and [Linear A.2, C.1 and H.2](linear-and-affine-connections.md). Those lessons retain the exact freely accessible human sources used to construct their proofs. Here we prove the identifications with tangent-space curvature and its full covariant derivatives; external references supply none of the proof obligations.

**Theorem D.1 (transported curvature in one tangent space).** Fix \(p\) in a connected smooth manifold and a frame \(u:\mathbb R^n\to T_pM\). Let \(P_\lambda:T_pM\to T_qM\) be parallel transport along any piecewise smooth path \(\lambda\) from \(p\) to \(q\). The Lie algebra of the full linear holonomy group at \(p\), equivalently of its restricted group, is
\[
\mathfrak{hol}_p
=\operatorname{span}_{\lambda,\ v,w\in T_pM}
\left\{
P_\lambda^{-1}\circ
R_q(P_\lambda v,P_\lambda w)\circ P_\lambda
\right\}.
\tag{D.1}
\]
The span is an ordinary finite-dimensional real linear span, without a topological closure. The full group need not be connected or closed.

**Proof.** Linear A.2 proves that the connection on \(TM\) corresponds to a principal connection \(\omega\) on its full frame bundle, and that the horizontal endpoint of \(u\) above \(\lambda\) is the frame \(u_\lambda=P_\lambda\circ u\). A loop with principal endpoint \(ua\) therefore has tangent transport \(uau^{-1}\). Thus the principal and linear holonomy groups are related by the Lie-group isomorphism \(a\mapsto uau^{-1}\), including their restricted groups and Lie algebras. Their identity components and Lie algebras agree by Curvature C.5.

The local curvature identity of Linear B.3, equivalently the principal/associated curvature calculation in Curvature A.6, gives
\[
\Omega_{u_\lambda}(B(a),B(b))
=u_\lambda^{-1}R_q(u_\lambda a,u_\lambda b)u_\lambda
\tag{D.2}
\]
for \(a,b\in\mathbb R^n\). Here \(B(a)\) is the standard horizontal field of Linear H.2. To check (D.2) directly in a local frame \(e\), write \(u_\lambda=eg\). The principal curvature is \(g^{-1}Fg\) on horizontal lifts, while \(F\) is the matrix of \(R\) in \(e\); moreover \(d\pi B(a)=u_\lambda a\). Substitution gives precisely (D.2).

Every reachable frame is some \(u_\lambda\), by the definition of horizontal reachability and the uniqueness of transport. The fields \(B(a)\) span the horizontal space at each such frame; curvature vanishes on vertical arguments. Curvature G.3 proves that these values of \(\Omega\) span the principal holonomy Lie algebra, without assuming that holonomy is closed. Conjugate its equality by \(u\), substitute \(u_\lambda=P_\lambda u\), and put \(v=ua,w=ub\). This gives (D.1) with exactly the stated range of paths and vectors. □

**Theorem D.2 (covariant curvature jets and local holonomy).** Let \(\nabla^0R=R\) and \(\nabla^{k+1}R=\nabla(\nabla^kR)\), using the full tensor derivative in every input and output position. At \(p\), define
\[
\mathfrak j_p
=\operatorname{span}_{k\geq0,\ v_1,\ldots,v_k,a,b\in T_pM}
 \left\{(\nabla^kR)_p(v_1,\ldots,v_k;a,b)\right\}
\subseteq\operatorname{End}(T_pM).
\tag{D.3}
\]
These are endomorphism values; the last vector acted on by the endomorphism is not fixed. Then \(\mathfrak j_p\) is a Lie algebra and
\[
\mathfrak j_p\subseteq\mathfrak{hol}^{\mathrm{loc}}_p
 \subseteq\mathfrak{hol}^{0}_p.
\tag{D.4}
\]
Local holonomy means the intersection of the restricted holonomy groups of all connected open neighbourhoods of \(p\), with loops contracted in those neighbourhoods. The connected immersed subgroup with algebra \(\mathfrak j_p\) is contained in the local holonomy group.

If \(\dim\mathfrak j_q\) is constant in a neighbourhood of \(p\), then \(\mathfrak j_p=\mathfrak{hol}^{\mathrm{loc}}_p\), and the corresponding connected groups agree. If the dimension is constant on connected \(M\), these groups also agree with restricted holonomy. If \(M\) and \(\nabla\) are real analytic, the infinitesimal, local and restricted groups agree at every point. None of these assertions removes possible additional components of full holonomy.

**Proof.** For each frame \(u\), let
\[
f_{k;c_1,\ldots,c_k,a,b}(u)
=u^{-1}(\nabla^kR)_{\pi(u)}
 (uc_1,\ldots,uc_k;ua,ub)u,
\tag{D.5}
\]
where all displayed lower-case arguments are fixed vectors in \(\mathbb R^n\).
The tensor connection and its transport rule are proved in Linear C.1. Along a horizontal frame path, the frame and every vector obtained by applying it to a fixed column are parallel. Differentiating the evaluated expression (D.5) along an integral curve of \(B(c)\) therefore differentiates only the tensor by its covariant derivative: all argument and conjugation derivatives are exactly cancelled by parallel transport. More explicitly, in that parallel frame the connection matrix on the path is zero by Linear A.2, so Linear C.1 makes tensor differentiation ordinary differentiation of all tensor components. Since the projected velocity is \(uc\), at the initial frame this proves
\[
B(c)f_{k;c_1,\ldots,c_k,a,b}
=f_{k+1;c,c_1,\ldots,c_k,a,b}.
\tag{D.6}
\]
The integral curves used here exist locally by Local 2.1, because Linear H.2 proves that \(B(c)\) is smooth. Formula (D.2) is the \(k=0\) case.

It follows inductively that the values in (D.5), for all \(k\), are exactly the span of all words in the fields \(B(e_i)\) applied to the functions \(\Omega(B(e_j),B(e_l))\), with \(e_i\) the standard basis of \(\mathbb R^n\). Multilinearity permits arbitrary constant arguments to be replaced by basis arguments. This is the horizontal curvature-jet space \(J(u)\) of Flat A.2. To check that no choice of horizontal frame changes that space, write any other local horizontal frame as \(E_i=\sum_j c_i^jB(e_j)\) with smooth coefficients; such coefficients exist and the coefficient matrix is invertible because both are bases of the horizontal subbundle. Curvature evaluations transform by two such coefficient factors. Repeated application of the product rule expresses every \(E\)-word of order at most \(k\) as a smooth linear combination of \(B\)-words of order at most \(k\). The inverse coefficient matrix gives the reverse inclusion. This is also the coordinate-independence argument of Flat A.2. Consequently
\[
J(u)=u^{-1}\mathfrak j_{\pi(u)}u.
\tag{D.7}
\]
This argument includes all tensor slots in \(\nabla^kR\); differentiating only the coordinate entries of \(R\) would not give (D.6).

Apply Flat A.3 to (D.7). It proves closure under commutators, and Flat A.1 constructs the connected immersed subgroup for this Lie algebra. Flat A.4 proves that the local-holonomy intersection stabilizes in a small neighbourhood and defines a connected immersed group. Flat A.5 proves both inclusions in (D.4) and the connected-group inclusion. Conjugation by \(u\), as in D.1, gives exactly the stated tangent-space groups.

Dimension is preserved by this conjugation. Thus local constant dimension is precisely the constant-rank hypothesis of Flat B.1, which proves local equality and, on a connected base with constant dimension, equality with restricted holonomy. All its hypotheses hold for the smooth principal frame connection established in Linear A.2; torsion was not a hypothesis of that theorem.

In the analytic case, the coordinate frame-bundle transitions are the Jacobian matrices of analytic coordinate changes, hence analytic: termwise differentiation of convergent power series is justified in Curvature I.1. Matrix multiplication and inversion are analytic there as well. The principal connection formula
\(\omega=g^{-1}A g+g^{-1}dg\) from Linear A.2 is therefore analytic when the coefficients of \(\nabla\) are analytic. Apply Flat B.2 on the connected component containing the point in question; all based loops and sufficiently small connected neighbourhoods stay in that component. It proves equality of the infinitesimal, local and restricted groups of this analytic principal connection. Equation (D.7) transfers that equality to \(TM\). These providers assert equality of connected groups, so no assertion about other components of full holonomy follows. □

**Theorem D.3 (parallel torsion and curvature give a frame algebra).** Suppose \(\nabla\mathcal T=0\) and \(\nabla R=0\). Fix a frame \(u_0\), let \(H\subseteq\mathrm{GL}(n,\mathbb R)\) be its full principal holonomy group, and let \(Q=P(u_0)\) be its reachable holonomy reduction, with its intrinsic principal-bundle structure. Put \(\mathfrak h=\operatorname{Lie}H\). There are constant alternating bilinear maps
\[
t:\mathbb R^n\times\mathbb R^n\to\mathbb R^n,
\qquad
r:\mathbb R^n\times\mathbb R^n\to\mathfrak h
\]
such that on \(Q\)
\[
\mathcal T_{\pi(u)}(ua,ub)=u\,t(a,b),\qquad
R_{\pi(u)}(ua,ub)=u\,r(a,b)u^{-1}.
\tag{D.8}
\]
The reduction lies over the connected component of \(\pi(u_0)\). For \(A\in\mathfrak h\) let \(A^\#\) be its fundamental vertical field and set \(Z_{A,a}=A^\#+B(a)\). These fields form a Lie algebra of dimension \(\dim\mathfrak h+n=\dim Q\), span each tangent space of \(Q\), and satisfy
\[
[Z_{A,a},Z_{C,b}]
=Z_{[A,C]-r(a,b),\,Ab-Ca-t(a,b)}.
\tag{D.9}
\]
No closedness of \(H\), completeness of these fields, or global action is asserted.

**Proof.** Curvature G.4 constructs the full reachable reduction as a Hausdorff, second-countable principal \(H\)-bundle, possibly immersed in the full frame bundle, and proves that the original connection restricts to it. Thus its horizontal spaces project isomorphically onto \(TM\), and \(B(a)\) is tangent to \(Q\). Fundamental fields for \(A\in\mathfrak h\) are also tangent to \(Q\).

Linear C.1 identifies parallel transport on tensors with the corresponding operations on vector transport. If a tensor has zero covariant derivative, its coefficients in a parallel frame on a path have derivative zero and are constant, by Linear A.2 and Local 0.3. Apply this to \(\mathcal T\) and \(R\) along each of the paths reaching a point of \(Q\) from \(u_0\). Their components therefore equal their components at \(u_0\); these constants define \(t,r\) and prove (D.8), independently of the chosen path. Curvature G.3 and (D.2) put every value \(r(a,b)\) in \(\mathfrak h\). Alternation follows from torsion's definition and curvature's skew-symmetry.

The coframe \((\theta,\omega)\) of Linear H.2 restricts on \(TQ\) to an isomorphism onto \(\mathbb R^n\oplus\mathfrak h\): its horizontal part gives the first summand, and on the vertical fundamental field \(A^\#\) it gives \((0,A)\). Hence \(Z_{A,a}\) has the constant coframe value \((a,A)\).

For fundamental fields one has \([A^\#,C^\#]=[A,C]^\#\). This sign can be checked in a principal-bundle chart: in its group coordinate \(g\), the two fields are \(gA,gC\). The coordinate bracket \(d(gC)(gA)-d(gA)(gC)\) is \(g(AC-CA)\), by PB C.3. Linear H.2 proves \([A^\#,B(b)]=B(Ab)\). Its two standard-horizontal bracket identities, combined with (D.8), give
\[
[B(a),B(b)]=-r(a,b)^\#-B(t(a,b)).
\tag{D.10}
\]
Indeed the \(\omega\)-value is \(-r(a,b)\) and the \(\theta\)-value is \(-t(a,b)\); the coframe is injective. Expand the bracket of \(A^\#+B(a)\) and \(C^\#+B(b)\), use skew-symmetry for the second mixed term, and apply (D.10). This proves (D.9).

The right side has constant coefficients and belongs to the same family, so its image is closed under brackets. The linear map \((A,a)\mapsto Z_{A,a}\) is injective since evaluation at any point followed by the coframe returns \((a,A)\). Its dimension is therefore \(\dim\mathfrak h+n\); the same coframe proves spanning at every point. Bilinearity, skew-symmetry and Jacobi are inherited from actual vector fields, whose bracket and Jacobi identity were proved in PB C.3. This establishes a Lie algebra without assuming any theorem integrating it to a global group action. □

## E. Coordinate and smooth-jet tests

These computations apply the proved formulas to explicit connections. The smooth flat function used in E.3 is constructed, with all derivative limits proved, in [Local 0.5](local-tools-for-bundles-and-transport.md). The principal-bundle analogue in [Flat C.2](flat-connections-and-infinitesimal-holonomy.md) motivates distinguishing all derivatives at one point from curvature in every neighbourhood. We give the tangent-bundle calculation separately, including its torsion and its actual transport groups.

**Exercise E.1 (Euclidean polar coordinates).** Let the plane have its connection given by ordinary component differentiation in Cartesian coordinates. In a polar coordinate chart with \(r>0\), calculate every connection coefficient and verify its curvature directly.

**Solution.** Use \(x=r\cos\phi,\ y=r\sin\phi\) on a sufficiently small angular interval. The sine and cosine functions and their derivatives are established in Connections E.1. The Jacobian determinant is \(r\), since \(\cos^2\phi+\sin^2\phi=1\), so Local 1.2 makes this a coordinate chart near each point with \(r>0\). Its coordinate fields, written in the Cartesian frame, are
\[
e_r=(\cos\phi,\sin\phi),\qquad
e_\phi=(-r\sin\phi,r\cos\phi).
\]
Differentiating these Cartesian components gives
\[
\nabla_{e_r}e_r=0,\quad
\nabla_{e_r}e_\phi=r^{-1}e_\phi,\quad
\nabla_{e_\phi}e_r=r^{-1}e_\phi,\quad
\nabla_{e_\phi}e_\phi=-r e_r.
\tag{E.1}
\]
Here \(e_r\) differentiates coordinate functions by \(\partial_r\) and \(e_\phi\) by \(\partial_\phi\), as follows from the coordinate map. Thus the only nonzero coefficients are
\(\Gamma^r_{\phi\phi}=-r\) and
\(\Gamma^\phi_{r\phi}=\Gamma^\phi_{\phi r}=r^{-1}\).
They give the matrix potential
\[
A_r=\begin{pmatrix}0&0\\0&r^{-1}\end{pmatrix},
\qquad
A_\phi=\begin{pmatrix}0&-r\\r^{-1}&0\end{pmatrix}.
\]
Compute
\[
\partial_rA_\phi=
\begin{pmatrix}0&-1\\-r^{-2}&0\end{pmatrix},
\qquad
\partial_\phi A_r=0,\qquad
[A_r,A_\phi]=
\begin{pmatrix}0&1\\r^{-2}&0\end{pmatrix}.
\]
Their sum \(\partial_rA_\phi-\partial_\phi A_r+[A_r,A_\phi]\) is zero. C.1 and skew-symmetry show that every curvature component vanishes. The symmetric lower coefficient indices also make torsion zero, by Linear D.1 and commutation of coordinate fields. Nonzero connection coefficients in this chart therefore do not imply nonzero curvature. □

**Exercise E.2 (both torsion corrections are necessary).** On \(\mathbb R^3\), let \(e_i=\partial_i\) and specify
\[
\nabla_{e_1}e_2=e_1,\qquad
\nabla_{e_2}e_3=e_2,
\]
with all other \(\nabla_{e_i}e_j=0\). Verify both identities of C.2 at \((e_1,e_2,e_3)\), including each correction.

**Solution.** Let \(E_{ij}\) be the matrix taking \(e_j\) to \(e_i\) and all other basis vectors to zero. The connection matrices are
\(A_1=E_{12}, A_2=E_{23}, A_3=0\).
Their constant coefficients define a smooth connection by Linear A.1. Since the coordinate fields commute,
\[
\mathcal T_{12}=e_1,\qquad
\mathcal T_{23}=e_2,\qquad
\mathcal T_{31}=0.
\tag{E.2}
\]
Here \(\mathcal T_{ij}=\mathcal T(e_i,e_j)\). Matrix units obey
\(E_{ij}E_{kl}=\delta_{jk}E_{il}\), by applying both sides to each basis vector. Consequently C.1 gives
\[
R_{12}=E_{13},\qquad R_{23}=R_{31}=0.
\tag{E.3}
\]
The left side of (C.5) is therefore \(e_1\).

To calculate its derivative sum, use all three terms in the tensor derivative:
\[
(\nabla_i\mathcal T)_{jk}
=A_i\mathcal T_{jk}
 -\mathcal T(A_i e_j,e_k)-\mathcal T(e_j,A_i e_k).
\]
For the three cyclic triples this gives
\[
(\nabla_1\mathcal T)_{23}=e_1,\qquad
(\nabla_2\mathcal T)_{31}=e_1,\qquad
(\nabla_3\mathcal T)_{12}=0.
\tag{E.4}
\]
For example the middle expression is
\(0-\mathcal T(e_2,e_1)-0=e_1\); the first is
\(A_1e_2-\mathcal T(e_1,e_3)-0=e_1\).
The quadratic torsion sum is
\[
\mathcal T(e_1,e_3)+\mathcal T(e_2,e_1)+0=-e_1.
\tag{E.5}
\]
Thus the right side of (C.5) is \(2e_1-e_1=e_1\), as required; deleting the quadratic torsion term would give a false equality.

For endomorphism-valued curvature the complete derivative is
\[
(\nabla_iR)_{jk}
=[A_i,R_{jk}]-R(A_i e_j,e_k)-R(e_j,A_i e_k),
\tag{E.6}
\]
because its ordinary coordinate derivatives vanish. In the three cyclic positions it gives respectively
\[
(\nabla_1R)_{23}=0,\qquad
(\nabla_2R)_{31}=E_{13},\qquad
(\nabla_3R)_{12}=0.
\]
Indeed the first is \(-R(e_1,e_3)=0\), while the second is
\(-R(e_2,e_1)=E_{13}\). The curvature-torsion sum is
\[
R(\mathcal T_{12},e_3)+R(\mathcal T_{23},e_1)
 +R(\mathcal T_{31},e_2)
=R_{13}+R_{21}+0=-E_{13}.
\]
Its negative is exactly the derivative sum in (C.6). Deleting that correction would incorrectly assert \(E_{13}=0\). □

**Exercise E.3 (a torsion-free connection invisible to every curvature jet).** On the tangent bundle of \(\mathbb R^2\), in its coordinate frame, set
\[
N=\begin{pmatrix}0&1\\0&0\end{pmatrix},\qquad
f(x)=\begin{cases}e^{-1/x^2},&x>0,\\0,&x\leq0,\end{cases}
\qquad A=f(x)N\,dy.
\tag{E.7}
\]
Show that torsion vanishes and every covariant derivative of curvature at the origin vanishes, while the local, restricted and full holonomy groups there are
\[
U=\{I+tN:t\in\mathbb R\}.
\tag{E.8}
\]
Consequently the infinitesimal group is trivial although the local group is not.

**Solution.** Local 0.5 proves that \(f\) is smooth and \(f^{(m)}(0)=0\) for every \(m\geq0\). The only nonzero connection coefficient is \(\Gamma^1_{22}=f(x)\). All antisymmetric differences \(\Gamma^k_{ij}-\Gamma^k_{ji}\) vanish, so Linear D.1 proves zero torsion. Linear B.3 gives
\[
R=f'(x)N\,dx\wedge dy,
\tag{E.9}
\]
since \(A\wedge A=0\).

Every ordinary partial derivative of every coefficient in (E.9) vanishes at the origin. This property persists after applying a tensor covariant derivative. To see this, Linear C.1 writes each resulting coefficient as an ordinary partial derivative of an old coefficient plus a finite sum of products of a connection coefficient with an old coefficient, one term for each tensor slot. Every ordinary partial derivative of the first term vanishes by hypothesis. Applying any finite collection of ordinary derivatives to a product gives a finite sum of derivatives of its two factors, by repeated use of the product rule; its old-tensor factor is always zero at the origin. Thus every such derivative of the product vanishes as well. Induction proves that all coefficients of every \(\nabla^kR\), and all their ordinary derivatives, vanish there. D.2 makes \(\mathfrak j_0=0\), whose connected group is the identity by Flat A.1.

For a piecewise smooth path \(\gamma(t)=(x(t),y(t))\), let
\(I_\gamma(t)=\int_0^t f(x(s))y'(s)\,ds\).
Since \(N^2=0\), the matrix
\[
G(t)=I-NI_\gamma(t)
\tag{E.10}
\]
has inverse \(I+NI_\gamma(t)\) and satisfies
\(G'=-f(x(t))y'(t)NG,\ G(0)=I\).
The fundamental theorem of calculus on each smooth piece is Local 0.3. Linear A.2 and uniqueness of its transport ODE identify (E.10) with parallel transport. At a junction the product of two such matrices adds their integrals, again because \(N^2=0\); hence the formula holds for the entire piecewise path. In particular every loop transport lies in \(U\).

Choose a coordinate ball about the origin and choose \(h>0\) small enough that the rectangles below lie in it for all sufficiently small \(|b|\). Traverse
\[
(0,0)\longrightarrow(h,0)\longrightarrow(h,b)
\longrightarrow(0,b)\longrightarrow(0,0).
\]
The integral in (E.10) is \(b f(h)\): horizontal sides contribute zero, the right side contributes \(bf(h)\), and the left side contributes zero since \(f(0)=0\). Thus these loops give \(I-bf(h)N\). Since \(f(h)>0\), varying \(b\) over an interval about zero gives all parameters \(t\) in an interval about zero in (E.8). Any real \(t\) is a finite sum of parameters in this interval: choose a positive integer \(m\) so large that \(t/m\) is in it and repeat that loop \(m\) times. Matrix multiplication adds parameters, so every element of \(U\) occurs. All these loops stay in the ball and contract there by linear contraction to the origin, including their finite concatenations. Their transports therefore belong to its restricted holonomy.

We have proved that every sufficiently small coordinate ball has restricted holonomy exactly \(U\), and every loop anywhere has transport in \(U\). Every connected neighbourhood contains such a ball. Its restricted holonomy also equals \(U\), by the two inclusions. Taking the neighbourhood intersection gives local holonomy \(U\); the same inclusions give global restricted and full holonomy \(U\). Its smooth connected group structure is explicit: \(t\mapsto I+tN\) is an injective smooth parametrization with smooth inverse given by the upper-right matrix entry, and multiplication is addition. Its Lie algebra is \(\mathbb RN\ne0\).

Finally this does not contradict the analytic assertion of D.2. The function \(f\) is not analytic at zero: its Taylor coefficients there are all zero, so analyticity would force it to vanish on an interval, whereas it is positive for every \(x>0\). The difference between curvature jets at one point and curvature arbitrarily near that point is essential. □

## F. Three geometries with explicit geodesics

The first example uses the connection specified in the historical coverage checklist; all its calculations are made below from the derivative axioms. The torus construction is already proved in [Curvature D.3](curvature-and-holonomy-groups.md). For the sphere we use Michor's exact free [author manuscript, §25.7](https://www.mat.univie.ac.at/~michor/dgbook.pdf), together with the complete sphere and projection-connection proofs in DG-CHAR-17 V.5 and [Linear G.2](linear-and-affine-connections.md). We use colatitude \(0<\theta<\pi\), with longitude restricted to an interval of length less than \(2\pi\) when a coordinate chart is needed.

**Example F.1 (straight geodesics with nonzero torsion and curvature).** On \(\mathbb R^2\), with \(e_1=\partial_x,e_2=\partial_y\), prescribe
\[
\nabla_{e_1}e_2=e_1,\qquad
\nabla_{e_2}e_1=-e_1,\qquad
\nabla_{e_1}e_1=\nabla_{e_2}e_2=0.
\tag{F.1}
\]
Every maximal geodesic is \(\gamma_v(t)=p+tv\), on all of \(\mathbb R\), and \(\exp_p(v)=p+v\). Nevertheless
\[
\mathcal T(e_1,e_2)=2e_1,\qquad
R(e_1,e_2)=N=\begin{pmatrix}0&1\\0&0\end{pmatrix}\ne0.
\tag{F.2}
\]
Both tensors are parallel. Full, restricted, local and infinitesimal holonomy at any point, in the coordinate frame, are \(\{I+tN:t\in\mathbb R\}\).

**Proof.** The matrices of (F.1) are \(A_1=N\) and \(A_2=\operatorname{diag}(-1,0)\); Linear A.1 constructs the connection. For \(v=(a,b)\),
\[
(aA_1+bA_2)v
=\begin{pmatrix}-b&a\\0&0\end{pmatrix}
 \begin{pmatrix}a\\b\end{pmatrix}=0.
\]
Thus A.1's geodesic equation is ordinary zero acceleration. Local 0.3 gives precisely \(p+tv\), and this curve exists for all time. Uniqueness and maximality in A.1 prove the first assertions, including the full exponential domain. The coordinate chart centred at any \(p\) is therefore a normal chart although its coefficients are nonzero.

Linear D.1 gives
\(\mathcal T_{12}=A_1e_2-A_2e_1=2e_1\).
The coefficient matrices are constant and
\([A_1,A_2]=N\); C.1 gives (F.2). To check parallelism, use the full tensor formulas from C.1 and E.2. Since these tensors are alternating in two arguments on a two-dimensional space, it suffices to check the pair \((e_1,e_2)\) in each coordinate direction. They give
\[
\begin{aligned}
(\nabla_1\mathcal T)_{12}
 &=A_1(2e_1)-\mathcal T(0,e_2)-\mathcal T(e_1,e_1)=0,\\
(\nabla_2\mathcal T)_{12}
 &=-2e_1-\mathcal T(-e_1,e_2)-\mathcal T(e_1,0)=0,\\
(\nabla_1R)_{12}
 &=[N,N]-R(0,e_2)-R(e_1,e_1)=0,\\
(\nabla_2R)_{12}
 &=[A_2,N]-R(-e_1,e_2)-R(e_1,0)=-N+N=0.
\end{aligned}
\tag{F.3}
\]
The derivative preserves alternation by Linear C.1, justifying the reduction to that pair. Thus \(\nabla\mathcal T=\nabla R=0\).

All higher covariant derivatives of \(R\) vanish, while the values of \(R\) span \(\mathbb RN\) at every point. The rank is constantly one, so D.2 makes the infinitesimal, local and restricted groups the connected immersed subgroup with that algebra. It is the displayed shear group: \(N^2=0\) gives \((I+sN)(I+tN)=I+(s+t)N\), the upper-right entry is a smooth inverse parameter, and its tangent algebra is \(\mathbb RN\). Uniqueness of the connected subgroup is Flat A.1. Every loop in \(\mathbb R^2\) contracts by the linear homotopy to its base point. Curvature C.5 therefore makes full holonomy equal to restricted holonomy here.

As a concrete instance of D.3, write \(V=N^\#\), \(H_1=B(e_1)\), \(H_2=B(e_2)\) on the reachable reduction. They form a frame with
\[
[V,H_1]=0,\qquad [V,H_2]=H_1,\qquad
[H_1,H_2]=-V-2H_1.
\tag{F.4}
\]
These follow by substituting (F.2) into (D.9). Straight geodesics alone therefore determine neither torsion, curvature nor this frame algebra. □

**Example F.2 (the complete flat torus).** The ordinary derivative on \(\mathbb R^n\) descends to \(\mathbb T^n=\mathbb R^n/\mathbb Z^n\). Identify each tangent space with \(\mathbb R^n\) by its descended coordinate frame. Then
\[
\gamma_v(t)=[p+tv]\quad(t\in\mathbb R),\qquad
\exp_{[p]}(v)=[p+v].
\tag{F.5}
\]
Torsion and curvature vanish and full holonomy is trivial. The connection is complete. For \(n>0\), its full exponential map at a point is surjective and is not injective, although every coordinate ball of radius less than \(1/2\) obtained by projection from \(\mathbb R^n\) is a convex normal neighbourhood in the sense of B.3.

**Proof.** Curvature D.3 proves the smooth quotient charts, descent of the ordinary derivative, the global parallel frame, zero torsion and curvature, and trivial full holonomy for every lattice, including \(\mathbb Z^n\). In its local lifted coordinates all coefficients vanish. The globally defined curve \([p+tv]\) solves the local zero-acceleration equation and has the prescribed initial data. A.1 identifies it as the unique maximal geodesic, with domain all of \(\mathbb R\). A.2 then proves (F.5) and completeness.

Every class \([q]\) is the image of \(v=q-p\), proving surjectivity. Adding any integer vector to \(v\) leaves that image unchanged; nonzero such vectors exist for \(n>0\), proving noninjectivity.

For the final assertion let \(B=B(c,\rho)\subset\mathbb R^n\), \(0<\rho<1/2\), and let \(V\) be its quotient image. Two distinct lifts of the same point differ by a nonzero integer vector, whose length is at least one. Two points in \(B\) have distance less than \(2\rho<1\), so the quotient is injective on \(B\). The quotient charts of Curvature D.3 make its restriction a local diffeomorphism, hence an open map with smooth local inverses; injectivity makes these inverses a single smooth inverse on \(V\).

In that chart a geodesic contained in \(V\) has zero coordinate acceleration. Its endpoints have unique lifts \(x,y\in B\), so Local 0.3 forces its coordinate expression to be \((1-t)x+ty\) on \([0,1]\). Conversely that segment stays in \(B\): the norm triangle inequality gives
\[
|(1-t)x+ty-c|
\leq(1-t)|x-c|+t|y-c|<\rho.
\]
Thus it projects to a contained geodesic and is the unique one with those endpoints. It depends smoothly on \(x,y\) and hence on the quotient endpoints. For the endpoint with lift \(x\), the open domain \(W_x=B-x\) contains zero, is star-shaped by the same inequality, and its exponential is the diffeomorphism \(v\mapsto[x+v]\) onto \(V\). This proves the asserted full convex-normal property. In dimension zero the torus and its tangent space are single points and all assertions have their evident zero-dimensional interpretation. □

**Example F.3 (round-sphere geodesics, curvature and holonomy).** On the unit sphere \(S^2\subset\mathbb R^3\), set
\[
\nabla_XY=P_p(dY(X)),\qquad P_p(w)=w-(p\cdot w)p.
\tag{F.6}
\]
This is the torsion-free metric connection. For \(v\in T_pS^2\), \(r=|v|\), its maximal geodesic is
\[
\gamma_v(t)=
\begin{cases}
\cos(rt)p+\dfrac{\sin(rt)}r\,v,&r>0,\\
p,&r=0,
\end{cases}
\qquad t\in\mathbb R.
\tag{F.7}
\]
The exponential is its value at \(t=1\); it is defined on all of \(T_pS^2\), and maps the open ball \(|v|<\pi\) diffeomorphically onto \(S^2\setminus\{-p\}\). In the programme curvature convention,
\[
R(X,Y)Z=(Y\cdot Z)X-(X\cdot Z)Y.
\tag{F.8}
\]
Its sectional curvature is one and \(\nabla R=0\). At every point all four holonomy groups in D.2, including the full group, are \(\mathrm{SO}(2)\) in an outward oriented orthonormal frame.

**Proof.** DG-CHAR-17 V.5 proves that this sphere is a smooth surface with its induced positive metric. Linear G.2 proves directly, on the entire sphere, that (F.6) obeys the connection axioms, preserves the metric and has zero torsion. Those facts are not inferred solely from a chart omitting the poles.

For a curve on the sphere, differentiating \(\gamma\cdot\gamma=1\) gives
\(\gamma\cdot\dot\gamma=0\) and
\(\gamma\cdot\ddot\gamma=-|\dot\gamma|^2\).
The geodesic equation \(P_\gamma\ddot\gamma=0\) therefore reads
\(\ddot\gamma=-|\dot\gamma|^2\gamma\).
It follows that
\(\frac d{dt}|\dot\gamma|^2=2\dot\gamma\cdot\ddot\gamma=0\),
so the speed is constant. Conversely direct differentiation of (F.7), using the trigonometric identities proved in Connections E.1, gives that equation and the initial data. Orthogonality of \(p,v\) and their lengths gives \(|\gamma_v(t)|^2=1\) for every \(t\). The case \(v=0\) is constant. Thus these are sphere-valued geodesics for all time; A.1 proves maximality and uniqueness, and A.2 supplies the smooth exponential map and completeness.

To check the stated normal domain, for \(0<r<\pi\) take the dot product of \(\exp_p(v)\) with \(p\). It is \(\cos r\). The cosine is strictly decreasing from one to minus one on \([0,\pi]\), since its derivative is \(-\sin r<0\) in the interior, with the signs and endpoints established in Connections E.1. Consequently, for \(q\ne p,-p\), there is a unique \(r\in(0,\pi)\) with \(p\cdot q=\cos r\), and then the unique possible initial vector is
\[
v=\frac r{\sin r}\bigl(q-(p\cdot q)p\bigr).
\tag{F.9}
\]
The vector in parentheses is orthogonal to \(p\), with length \(\sin r\), so this vector indeed has length \(r\) and satisfies the exponential formula. The intermediate-value assertion is Local 0.0. The point \(q=p\) corresponds only to \(v=0\) inside the ball. This proves bijectivity onto the stated punctured sphere. Away from \(p\), the inverse cosine is smooth by Local 1.2 because \(-\sin r\ne0\), so (F.9) is smooth. At \(p\), B.1 already supplies a smooth local inverse; uniqueness makes it agree with (F.9) off \(p\). Hence the global inverse is smooth. At radius \(\pi\), all radial directions give \(-p\), explaining the stated restriction. These geodesics join \(p\) to every point, including \(-p\), so the sphere is path connected and hence connected.

Now use the local coordinates
\[
p(\theta,\phi)=(\sin\theta\cos\phi,\sin\theta\sin\phi,\cos\theta),
\qquad 0<\theta<\pi.
\]
Writing \(s=\sin\theta,\ c=\cos\theta\), their orthonormal frame is
\(e_1=(c\cos\phi,c\sin\phi,-s)\),
\(e_2=(-\sin\phi,\cos\phi,0)\), and their dual coframe is
\(\sigma^1=d\theta,\sigma^2=s\,d\phi\).
Their tangent, orthonormal and outward orientation properties are checked in Linear G.2. That proof computes the derivatives in the longitude direction. In the other direction, \(\partial_\theta e_1=-p\) has zero tangent projection and \(\partial_\theta e_2=0\). Consequently
\[
A=J\cos\theta\,d\phi,\quad
J=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\qquad
F=-J\sin\theta\,d\theta\wedge d\phi=-J\,\sigma^1\wedge\sigma^2.
\tag{F.10}
\]
The last equality follows from Linear B.3: \(A\wedge A=0\) and differentiating \(\cos\theta\) gives \(-\sin\theta\). Thus
\(R(e_1,e_2)e_1=-e_2\) and
\(R(e_1,e_2)e_2=e_1\).
Expand \(X,Y,Z\) in this basis, using skew-symmetry and trilinearity, to get (F.8) on the chart. Both sides of (F.8) are smooth tensors on the whole sphere and agree off the two poles. The punctured charts approach each pole; continuity therefore gives equality there too. For any orthonormal \(X,Y\), (F.8) gives
\(g(R(X,Y)Y,X)=1\), which is the sectional curvature in this convention. Linear C.1's product and contraction rules and \(\nabla g=0\) show directly from (F.8) that \(\nabla R=0\).

Finally, the outward area form is
\(\mu_p(Y,Z)=\det(p,Y,Z)\).
It is parallel: when differentiating it in a tangent direction \(X\), the term \(\det(X,Y,Z)\) vanishes since three tangent vectors lie in a two-dimensional plane. Replacing each ambient derivative of \(Y,Z\) by its tangent projection changes its determinant term only by a multiple with two \(p\)'s, which is zero. Subtracting these two projected-derivative terms is precisely the covariant derivative of \(\mu\), by Linear C.1. Thus transport preserves both the metric and this orientation form, and every holonomy matrix belongs to \(\mathrm{SO}(2)\).

The values of \(R_p\) span the nonzero line \(\mathbb RJ\), and all its higher covariant derivatives vanish. This line has constant dimension, so D.2 identifies the infinitesimal, local and restricted groups with its connected subgroup. That subgroup is \(\mathrm{SO}(2)\): every positively oriented orthogonal \(2\)-by-\(2\) matrix has columns \((a,b)\), \((-b,a)\), with \(a^2+b^2=1\); Connections E.1 writes \(a+ib=e^{i\alpha}\). Hence it is a rotation \(e^{\alpha J}\), connected to the identity through \(e^{t\alpha J}\), with Lie algebra \(\mathbb RJ\). Flat A.1 supplies uniqueness of the connected immersed subgroup. Restricted holonomy is therefore all of \(\mathrm{SO}(2)\), while full holonomy is both a supergroup of it and a subgroup of it. The two coincide, proving the final assertion without an unproved assertion about the fundamental group of the sphere. □

## G. Global trajectories and pointwise distinctions

This part supplies additional coverage identified after the preceding six parts were written. Its construction uses their complete proofs and the exact earlier programme proofs cited below. In particular, the horizontal-lift theorem is [Connections C.1–C.2](connections-and-parallel-transport.md), tensor and frame differentiation are [Linear A.2, C.1 and H.2](linear-and-affine-connections.md), and exterior differentiation is [Curvature A.2 and A.5](curvature-and-holonomy-groups.md). These earlier chapters retain the free human sources used in their construction.

**Theorem G.1 (completeness on the frame bundle).** Fix a frame \(u:\mathbb R^n\to T_pM\) and a vector \(a\in\mathbb R^n\). The maximal integral curve of the standard horizontal field \(B(a)\) through \(u\) has exactly the maximal time interval \(I_{ua}\) of the geodesic with initial velocity \(ua\). Its projection is that geodesic. Consequently the connection is geodesically complete if and only if every \(B(a)\) on the full frame bundle is complete.

**Proof.** Let \(U(t)\) be an integral curve of \(B(a)\). Linear H.2 gives
\[
\omega(\dot U)=0,\qquad \theta(\dot U)=a,\qquad
\dot\gamma(t)=U(t)a,\quad \gamma=\pi\circ U.
\tag{G.1}
\]
Linear A.2 says that \(U(t)a\) is parallel, since \(U\) is horizontal. Thus \(D_t\dot\gamma=0\). A.1 identifies its projection with \(\gamma_{ua}\) wherever it is defined.

Conversely lift \(\gamma_{ua}\) horizontally starting at \(u\). Connections C.1 supplies a unique lift on every compact subinterval of \(I_{ua}\) containing zero, in both time directions. Uniqueness makes the lifts agree on overlaps. Their union defines a smooth horizontal lift \(U\) on all of \(I_{ua}\): each time has a compact subinterval with that time in its interior, and on that interior the lift is smooth by C.1. The velocity \(\dot\gamma_{ua}\) and the vector \(U(t)a\) are parallel with the same value at zero. The uniqueness of vector transport in Linear A.2 makes them equal throughout this interval. Hence \(\theta(\dot U)=a\); together with horizontality, the coframe isomorphism in Linear H.2 gives \(\dot U=B(a)\).

This integral curve cannot extend beyond \(I_{ua}\), because its projection would extend the maximal geodesic, contradicting A.1. It is therefore precisely the maximal integral curve. If the connection is complete, these intervals are all \(\mathbb R\), proving completeness of each field. Conversely, any tangent vector is \(ua\) for a frame \(u\) and a column \(a\), so completeness of all those fields gives every required geodesic for all real time. When \(a=0\), the coframe gives \(B(0)=0\); both curves are constant, consistently with the assertion. □

**Theorem G.2 (tensor coordinates and exterior differentiation in every degree).** For a tensor \(S\) with \(r\) vector and \(s\) covector factors, its coordinate derivative is
\[
\begin{split}
(\nabla_i S)^{a_1\ldots a_r}{}_{b_1\ldots b_s}
={}&\partial_i S^{a_1\ldots a_r}{}_{b_1\ldots b_s}\\
&+\sum_{\nu=1}^r\Gamma^{a_\nu}_{ic}
 S^{a_1\ldots c\ldots a_r}{}_{b_1\ldots b_s}\\
&-\sum_{\mu=1}^s\Gamma^c_{ib_\mu}
 S^{a_1\ldots a_r}{}_{b_1\ldots c\ldots b_s}.
\end{split}
\tag{G.2}
\]
At the centre of a normal coordinate chart, \(\mathcal T_p=0\) suffices for all the connection corrections in (G.2) to vanish at \(p\).

More generally let \(E\) have a connection, and let \(\alpha\) be an \(E\)-valued alternating \(q\)-form, \(q\geq0\). Give its covariant input positions the tangent connection \(\nabla\). Write \(\mathbf X_{\widehat i}\) for the ordered list \(X_0,\ldots,X_q\) with \(X_i\) omitted, and use two hats for two omissions. Then
\[
\begin{split}
(D\alpha)(X_0,\ldots,X_q)
={}&\sum_{i=0}^q(-1)^i(\nabla_{X_i}\alpha)(\mathbf X_{\widehat i})\\
&+\sum_{0\leq i<j\leq q}(-1)^{i+j+1}
 \alpha\bigl(\mathcal T(X_i,X_j),\mathbf X_{\widehat{i,j}}\bigr).
\end{split}
\tag{G.3}
\]
For a scalar form \(D=d\), using ordinary differentiation on the scalar line. Empty sums are zero.

**Proof.** Expand \(S\) in the basis tensors made from \(\partial_a\) and \(dx^b\). Linear C.1 gives the product rule on every factor. The vector derivative is \(\nabla_i\partial_b=\Gamma^a_{ib}\partial_a\). Differentiating \(dx^b(\partial_c)=\delta^b_c\) gives
\[
(\nabla_i dx^b)(\partial_c)=-\Gamma^b_{ic},
\qquad \nabla_i dx^b=-\Gamma^b_{ic}\,dx^c.
\]
Applying the product rule to each coefficient and factor, then renaming the summed index in each affected position, gives exactly (G.2). It includes \(r=0\), \(s=0\) and the scalar case. B.1 proves that at a normal-coordinate centre \(\Gamma^a_{ib}=\tfrac12\mathcal T^a_{ib}\). Hence \(\mathcal T_p=0\) makes all those coefficients zero at \(p\), without any hypothesis about torsion nearby.

For (G.3), Curvature A.2 and A.5 give the evaluated exterior formula
\[
\begin{split}
D\alpha(\mathbf X)
={}&\sum_i(-1)^i\nabla^E_{X_i}
       \bigl(\alpha(\mathbf X_{\widehat i})\bigr)\\
&+\sum_{i<j}(-1)^{i+j}
       \alpha([X_i,X_j],\mathbf X_{\widehat{i,j}}).
\end{split}
\tag{G.4}
\]
Indeed, in a local frame the matrix-action terms from \(A^E\wedge\alpha\) combine with the ordinary derivatives to form the first sum, and the bracket terms are unchanged. Linear C.1 expands its first sum into the tensor derivatives in (G.3) and the terms differentiating the arguments.

Fix a pair \(i<j\). The term differentiating \(X_j\) in the \(i\)-summand has sign \((-1)^i\); after omission of \(X_i\), that argument has position \(j-1\), counting from zero. Moving it to the first position therefore gives sign \((-1)^{i+j-1}\). The term differentiating \(X_i\) in the \(j\)-summand similarly gives sign \((-1)^{i+j}\). Together they are
\[
(-1)^{i+j+1}
\alpha(\nabla_{X_i}X_j-\nabla_{X_j}X_i,\mathbf X_{\widehat{i,j}}).
\]
Add the bracket term for this same pair in (G.4). Linear D.1 identifies the resulting first argument as \(\mathcal T(X_i,X_j)\), giving its term in (G.3). Every differentiated-argument term belongs to exactly one pair, so summing proves the identity. When \(q=0\) there are no pairs, and (G.4) is just the derivative of an \(E\)-section. Taking the scalar connection gives the assertion for \(d\). □

**Example G.3 (what vanishing at one point does not imply).** A frame normal at a point need not be a coordinate frame on any neighbourhood. Also \(\mathcal T_p=0\) does not imply the torsion-free first Bianchi identity at that point.

**Proof.** On the ordinary Euclidean plane put \(h=x^2\), \(c=\cos h\), \(s=\sin h\), and
\[
E_1=c\,\partial_x+s\,\partial_y,\qquad
E_2=-s\,\partial_x+c\,\partial_y.
\tag{G.5}
\]
Connections E.1 proves the trigonometric derivatives and \(c^2+s^2=1\), so these vectors form an orthonormal frame. Its matrix relative to the coordinate frame is
\(g=\left(\begin{smallmatrix}c&-s\\s&c\end{smallmatrix}\right)\).
The change rule in Linear A.1 gives its potential
\[
A'=g^{-1}dg=J\,dh=2xJ\,dx,\qquad
J=\begin{pmatrix}0&-1\\1&0\end{pmatrix}.
\tag{G.6}
\]
For example, \(dg=gJ\,dh\) follows by differentiating its four entries, and multiplication by \(g^{-1}\) proves the displayed formula. Thus \(A'\) vanishes at the origin. The coordinate bracket formula of PB C.3 gives
\[
[E_1,E_2]
 =\bigl(-2x(c^2+s^2)\bigr)\partial_x
   +\bigl(-2xcs+2xsc\bigr)\partial_y
 =-2x\,\partial_x.
\tag{G.7}
\]
Every open neighbourhood of the origin contains a point with \(x\ne0\), where this bracket is nonzero. Coordinate frame vectors commute, by equality of mixed partials in PB C.3. Consequently this normal frame cannot be a coordinate frame on such a neighbourhood.

For the second assertion use \(\mathbb R^3\), with coordinate vectors \(e_1,e_2,e_3\), and prescribe only
\(\nabla_{e_2}e_3=x^1e_1\); all other coordinate derivatives are zero. Linear A.1 constructs a smooth connection with \(A_2=x^1E_{13}\), \(A_1=A_3=0\), where \(E_{13}e_3=e_1\). Linear D.1 gives \(\mathcal T_{23}=x^1e_1\), with the other independent pairs zero. C.1 gives \(R_{12}=E_{13}\), \(R_{23}=R_{31}=0\). At the origin the connection coefficients and torsion vanish, but (G.2) gives
\[
\sum_{\mathrm{cyc}}(\nabla_{e_1}\mathcal T)(e_2,e_3)=e_1
 =\sum_{\mathrm{cyc}}R(e_1,e_2)e_3.
\tag{G.8}
\]
The quadratic torsion sum is zero there. This verifies the first Bianchi identity C.2 and disproves its torsion-free reduction under the weaker pointwise assumption. By contrast, the correction on the right of the second identity C.6 uses only the value of torsion, so it does vanish at a point where torsion vanishes. □

**Lemma G.4 (finite jets at a point and separate bracket components).** The space \(\mathfrak j_p\) in D.2 is spanned by derivatives up to some finite order depending on \(p\). Its dimension is lower semicontinuous. These pointwise facts do not assert any uniform derivative-order bound.

On the reachable frame bundle \(Q\) of D.3, the horizontal coframe component of \([B(a),B(b)]\) is constant whenever \(\nabla\mathcal T=0\), regardless of whether \(\nabla R=0\). The vertical component is constant whenever \(\nabla R=0\), regardless of whether \(\nabla\mathcal T=0\). If torsion vanishes identically, this bracket is vertical; if curvature vanishes identically, it is horizontal.

**Proof.** The endomorphism space has finite dimension \(n^2\), with basis its matrix units in a frame. Starting with the empty list, choose a generator of (D.3) outside the span of those already chosen whenever that span is smaller than \(\mathfrak j_p\). Each choice increases the independent-list length by one, so after at most \(n^2\) choices the list spans \(\mathfrak j_p\). Taking the maximum of its finitely many derivative orders proves the first assertion. For the zero space take order zero.

For lower semicontinuity suppose \(d=\dim\mathfrak j_p>0\). Extend the arguments of the selected generators as constant-component fields in a local frame. The resulting \(d\) endomorphism-valued functions \(S_1(q),\ldots,S_d(q)\) are smooth, by smoothness of the tensor derivatives, and their values always belong to \(\mathfrak j_q\). At \(p\) their column matrix, obtained by listing the \(n^2\) entries of each, has a nonzero \(d\)-by-\(d\) minor. To justify this elementary criterion, perform elimination on successive independent columns: each new column has a nonzero residual after eliminating the preceding pivots, so one can choose a new pivot row; the resulting selected square system is triangular after these column operations and has nonzero diagonal product. Its determinant, unchanged by subtracting multiples of earlier columns, is nonzero. That determinant is a polynomial in the original entries, hence continuous. It remains nonzero near \(p\), so the \(S_i(q)\) stay independent and \(\dim\mathfrak j_q\geq d\) there. For \(d=0\) the same inequality is automatic. This is precisely lower semicontinuity.

For the bracket assertions, the full reachable reduction and its restricted connection exist by Curvature G.4 without either parallel-tensor hypothesis. Linear H.2 gives on it
\[
\begin{split}
\theta([B(a),B(b)])&=-u^{-1}\mathcal T_{\pi(u)}(ua,ub),\\
\omega([B(a),B(b)])&=-u^{-1}R_{\pi(u)}(ua,ub)u.
\end{split}
\tag{G.9}
\]
The first row is the horizontal component expressed by the solder coframe; the second is the vertical component expressed by the connection coframe. The parallel-frame argument in the proof of D.3 applies separately to each tensor. Thus its own covariant constancy suffices to make the corresponding row constant throughout \(Q\); no use of the other tensor is made. Finally the coframe splitting of Linear H.2 identifies a vector as vertical exactly when its \(\theta\)-value is zero, and as horizontal exactly when its \(\omega\)-value is zero. Substitution in (G.9) proves the last assertions. □

**Example G.5 (which flat-torus geodesics close).** For \(v\ne0\), the geodesic \([p+tv]\) in F.2 is periodic exactly when \(av\in\mathbb Z^n\) for some \(a>0\). On \(\mathbb T^2\) the velocities \((1,1/2)\) and \((1,\sqrt2)\) give a periodic and a nonperiodic geodesic, respectively.

**Proof.** A return at time \(a>0\) means \([p+av]=[p]\), equivalent by the quotient definition to \(av\in\mathbb Z^n\). In that case
\([p+(t+a)v]=[p+tv]\) for every real \(t\), so the return gives a full period, including the velocity in the global frame of F.2. A period conversely gives a return. For \((1,1/2)\), take \(a=2\).

For \((1,\sqrt2)\), such an \(a\) would be a positive integer \(m\), and \(m\sqrt2\) an integer \(k\), making \(\sqrt2=k/m\). Here \(\sqrt2\) denotes the unique positive solution of \(z^2=2\): existence follows from continuity on \([1,2]\) and the intermediate-value property of Local 0.0, and strict increase there gives uniqueness. It is irrational. Indeed choose a representation \(k/m\) with the smallest positive integer denominator, if any exists. The equation \(k^2=2m^2\) makes \(k\) even, since the square of an odd integer \(2l+1\) is \(4l(l+1)+1\), which is odd. Write \(k=2j\); then \(m^2=2j^2\) makes \(m\) even by the same argument. Cancelling two gives a representation with smaller positive denominator, a contradiction. The minimum exists because a nonempty set of positive integers has a smallest member, or simply by choosing a denominator and checking the finite positive list below it. Thus the second velocity has no positive period. □

**Example G.6 (the sphere's coordinate coefficients).** In the colatitude and longitude chart of F.3, the only nonzero coordinate connection coefficients are
\[
\Gamma^\phi_{\theta\phi}
 =\Gamma^\phi_{\phi\theta}=\cot\theta,\qquad
\Gamma^\theta_{\phi\phi}=-\sin\theta\cos\theta.
\tag{G.10}
\]
These statements are confined to the chart \(0<\theta<\pi\).

**Proof.** In the notation of F.3, \(\partial_\theta=e_1\) and \(\partial_\phi=s e_2\). Its already proved potential \(A=Jc\,d\phi\) gives
\[
\nabla_\theta e_1=\nabla_\theta e_2=0,\qquad
\nabla_\phi e_1=c e_2,\qquad
\nabla_\phi e_2=-c e_1.
\]
The derivative rule and \(\partial_\theta s=c\), \(\partial_\phi s=0\), proved in Connections E.1, therefore give
\[
\begin{aligned}
\nabla_\theta\partial_\theta&=0,&
\nabla_\theta\partial_\phi&=c e_2=(c/s)\partial_\phi,\\
\nabla_\phi\partial_\theta&=c e_2=(c/s)\partial_\phi,&
\nabla_\phi\partial_\phi&=-sc e_1=-sc\partial_\theta.
\end{aligned}
\]
These four derivatives exhaust the coordinate input pairs, proving (G.10). Dividing by \(s\) is legitimate on this chart. The poles are excluded only from these coordinates: the global connection, geodesics and curvature there were already proved in F.3. □
