# Heights of an immersed surface

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

A metric on an open set of the plane prescribes the lengths of curves. Is it the metric of a surface in three-dimensional space, at least near a given point? In September 2026 OpenAI released a proof that the answer can be no: there is a smooth metric on a square such that no neighbourhood of the centre has a smooth isometric immersion into \(\mathbb R^3\) [OpenAI-I]. This course presents the proof. The first lesson collects three tools that concern any immersion.

- If a surface is immersed isometrically in space, its height in a fixed direction satisfies one scalar equation of second order, in which only the metric appears (Theorem 2.1).
- Every smooth function of absolute value at most \(10^{-3}\) on the square is the curvature of a metric of the form \(dX^2+f^2\,dY^2\) (Proposition 3.2).
- If the curvature is negative in a disk and zero on its boundary, and the immersed surface is a graph over a plane, then at some boundary point the second fundamental form has rank one (Proposition 4.2).

The lesson follows [OpenAI-I, Sections 2 and 5]: the lemma on the height equation, the lemma on prescribing small curvature, and the lemma on a negatively curved disk. It uses the description of a surface in space by its metric and second fundamental form: [Submanifolds and hypersurfaces](course:DG-FND/submanifolds-and-hypersurfaces#proposition-a-3), Proposition A.3 (course *Bundles, curvature and holonomy*).

## 1. Metrics on plane domains

Let \(U\subseteq\mathbb R^2\) be open, with the coordinates \(x^1,x^2\); partial derivatives are written \(\partial_1,\partial_2\). All functions are smooth, that is, infinitely differentiable. A *metric* on \(U\) is a symmetric matrix \(g=(g_{ij})\) of functions on \(U\) that is positive definite at every point. Its inverse matrix is \((g^{ij})\). The *Christoffel symbols* are
\[
\begin{aligned}
\Gamma^k_{ij}=\frac12\sum_lg^{kl}\bigl(&\partial_ig_{jl}+\partial_jg_{il}\\
&-\partial_lg_{ij}\bigr),
\end{aligned}
\]
and the *curvature* \(K=K_g\) is the function with
\[
\begin{aligned}
K\det g=\sum_lg_{1l}\Bigl(&\partial_1\Gamma^l_{22}-\partial_2\Gamma^l_{12}\\
&+\sum_m\Gamma^l_{1m}\Gamma^m_{22}\\
&-\sum_m\Gamma^l_{2m}\Gamma^m_{12}\Bigr).
\end{aligned}
\]
This is the Gaussian curvature of the Riemannian manifold \((U,g)\), in the coordinate form (A.12) of the lesson on submanifolds and hypersurfaces. The value of \(K\) at a point depends only on the values of \(g\) and of its derivatives of order at most two at that point.

For a function \(z\) on \(U\), the *covariant Hessian* and the squared length of the differential are
\[
\begin{gathered}
H_{ij}=\partial_i\partial_jz-\sum_k\Gamma^k_{ij}\,\partial_kz,\\
|dz|_g^2=\sum_{i,j}g^{ij}\,\partial_iz\,\partial_jz .
\end{gathered}
\]

An *isometric immersion* of \((U,g)\) into \(\mathbb R^3\) is a smooth map \(F\colon U\to\mathbb R^3\) with
\[
\langle\partial_iF,\partial_jF\rangle=g_{ij}\qquad(i,j\in\{1,2\}).
\]
Since \(g\) is positive definite, \(\partial_1F\) and \(\partial_2F\) are linearly independent at every point. Let \(n\) be the unit normal in the direction of \(\partial_1F\times\partial_2F\). The *second fundamental form* is the symmetric matrix \(\mathrm{II}_{ij}=\langle\partial_i\partial_jF,n\rangle\).

**Theorem 1.1 (Gauss).** For an isometric immersion \(F\) of \((U,g)\),
\[
\begin{gathered}
\partial_i\partial_jF=\sum_k\Gamma^k_{ij}\,\partial_kF+\mathrm{II}_{ij}\,n,\\
\det\mathrm{II}=K\det g .
\end{gathered}
\]

This is Proposition A.3 of the lesson on submanifolds and hypersurfaces: formula (A.8) there is the first line and (A.11) the second.

**Lemma 1.2.** Let \(M\) be an invertible matrix, \(c\in\mathbb R^2\), \(\Phi(x)=c+Mx\), and \(U'=\Phi^{-1}(U)\). The *pull-back* of \(g\) is the metric \(g'=M^{\mathsf T}(g\circ\Phi)M\) on \(U'\).

1. \(K_{g'}=K_g\circ\Phi\).
2. For a function \(z\) on \(U\), the covariant Hessian of \(z\circ\Phi\) for \(g'\) is \(M^{\mathsf T}(H\circ\Phi)M\), where \(H\) is the covariant Hessian of \(z\) for \(g\), and \(|d(z\circ\Phi)|_{g'}=|dz|_g\circ\Phi\).
3. If \(F\) is an isometric immersion of \((U,g)\), then \(F\circ\Phi\) is an isometric immersion of \((U',g')\).

**Proof.** For a function \(w\), \(\partial_i(w\circ\Phi)=\sum_aM_{ai}(\partial_aw)\circ\Phi\), and, since \(M\) is constant, \(\partial_i\partial_j(w\circ\Phi)=\sum_{a,b}M_{ai}M_{bj}(\partial_a\partial_bw)\circ\Phi\). (3) follows from the first formula. For (2), let \(N=M^{-1}\). The inverse of \(g'\) is \(N(g^{-1}\circ\Phi)N^{\mathsf T}\), and the first derivatives of \(g'\) are \(\partial_ig'_{jl}=\sum M_{ai}M_{bj}M_{dl}(\partial_ag_{bd})\circ\Phi\). Inserting this in the definition gives the Christoffel symbols of \(g'\):
\[
\Gamma'^k_{ij}=\sum_{a,b,c}N_{kc}\,M_{ai}M_{bj}\,\Gamma^c_{ab}\circ\Phi .
\]
Since \(\sum_kN_{kc}M_{ek}\) is \(1\) for \(e=c\) and \(0\) otherwise,
\[
\begin{aligned}
&\sum_k\Gamma'^k_{ij}\,\partial_k(z\circ\Phi)\\
&\quad=\sum_{a,b,c}M_{ai}M_{bj}\,(\Gamma^c_{ab}\,\partial_cz)\circ\Phi .
\end{aligned}
\]
With the formula for the second derivatives this is the statement on the Hessian. The statement on \(|dz|\) follows from the formula for the inverse of \(g'\). (1) The map \(\Phi\) is an isometry from \((U',g')\) to \((U,g)\), and the Gaussian curvature is preserved by isometries (Proposition A.3 of the lesson on submanifolds and hypersurfaces). \(\blacksquare\)

## 2. The height equation

**Theorem 2.1.** Let \(F\) be an isometric immersion of \((U,g)\) into \(\mathbb R^3\), let \(e\in\mathbb R^3\) be a unit vector, and \(z=\langle F,e\rangle\), the *height* in the direction \(e\). Let \(\nu=\langle n,e\rangle\). Then
\[
\begin{gathered}
H=\nu\,\mathrm{II},\qquad|dz|_g^2+\nu^2=1,\\
\det H=K\det g\,\bigl(1-|dz|_g^2\bigr).
\end{gathered}
\]
If \(e\) is the normal \(n(b)\) at a point \(b\in U\), then \(dz(b)=0\) and \(H(b)=\mathrm{II}(b)\).

**Proof.** Take the scalar product of the first formula of Theorem 1.1 with \(e\): \(\partial_i\partial_jz=\sum_k\Gamma^k_{ij}\partial_kz+\mathrm{II}_{ij}\nu\), that is \(H=\nu\,\mathrm{II}\). Write \(e=\sum_ka_k\partial_kF+\nu n\). The scalar product with \(\partial_jF\) gives \(\partial_jz=\sum_ka_kg_{kj}\), so \(a_k=\sum_jg^{kj}\partial_jz\), and
\[
\begin{aligned}
1=|e|^2&=\sum_{k,l}a_ka_lg_{kl}+\nu^2\\
&=|dz|_g^2+\nu^2 .
\end{aligned}
\]
With the second formula of Theorem 1.1, \(\det H=\nu^2\det\mathrm{II}=(1-|dz|_g^2)K\det g\). If \(e=n(b)\), then \(\partial_jz(b)=\langle\partial_jF(b),n(b)\rangle=0\) and \(\nu(b)=1\). \(\blacksquare\)

The last equation is the *height equation*, also called the Darboux equation. It contains the metric and the function \(z\), and nothing else of the immersion. With \(E=\det g\,(1-|dz|_g^2)\) it reads
\[
H_{11}H_{22}-H_{12}^2=KE .
\]
So an isometric immersion gives, for every direction \(e\), a solution of this equation with \(|dz|_g\le1\). The course uses only this consequence of an immersion.

## 3. A metric with a given small curvature

**Lemma 3.1.** Let \(f\) be a positive function on an open set of the plane with the coordinates \(X,Y\). The curvature of the metric with \(g_{11}=1\), \(g_{12}=0\), \(g_{22}=f^2\), written \(dX^2+f^2\,dY^2\), is
\[
K=-\frac{f_{XX}}f .
\]

**Proof.** The inverse matrix has the entries \(1,0,f^{-2}\). From the definition, the Christoffel symbols that are not zero are
\[
\begin{gathered}
\Gamma^1_{22}=-ff_X,\qquad\Gamma^2_{22}=\frac{f_Y}f,\\
\Gamma^2_{12}=\Gamma^2_{21}=\frac{f_X}f .
\end{gathered}
\]
In the formula for \(K\det g\) only \(l=1\) contributes, because \(g_{12}=0\), and
\[
\begin{aligned}
K\det g&=\partial_1\Gamma^1_{22}-\Gamma^1_{22}\Gamma^2_{12}\\
&=-(f_X^2+ff_{XX})+f_X^2\\
&=-ff_{XX}.
\end{aligned}
\]
Divide by \(\det g=f^2\). \(\blacksquare\)

For example \(f=\cos X\) gives \(K=1\) where \(\cos X>0\), and \(f=\cosh X\) gives \(K=-1\).

**Proposition 3.2.** Let \(Q=(-1,1)^2\), with the coordinates \(X,Y\), and let \(K_0\) be a smooth function on \(Q\) with \(|K_0|\le10^{-3}\). There is a smooth function \(f\) on \(Q\) with
\[
\begin{gathered}
f_{XX}=-K_0f,\\
f(0,Y)=1,\qquad f_X(0,Y)=0,
\end{gathered}
\]
and \(|f-1|<10^{-3}\). The metric \(\bar g=dX^2+f^2\,dY^2\) on \(Q\) has the curvature \(K_0\), and \(0.99\,|v|^2\le\bar g(v,v)\le1.01\,|v|^2\) for all vectors \(v\).

**Proof.** Let \(f_0=1\) and
\[
\begin{aligned}
&f_{n+1}(X,Y)\\
&\ =-\int_0^X(X-u)K_0(u,Y)f_n(u,Y)\,du .
\end{aligned}
\]
Each \(f_n\) is smooth. By induction \(|f_n|\le10^{-3n}X^{2n}/(2n)!\), because \(\int_0^{|X|}(|X|-u)\,u^{2n}\,du\) is \(|X|^{2n+2}\) divided by \((2n+1)(2n+2)\). So the series \(f=\sum_nf_n\) converges uniformly on \(Q\), and
\[
\begin{aligned}
&f(X,Y)\\
&\ =1-\int_0^X(X-u)K_0(u,Y)f(u,Y)\,du .
\end{aligned}
\]
Hence \(f\) is twice differentiable in \(X\), with \(f_X=-\int_0^XK_0f\,du\) and \(f_{XX}=-K_0f\), and the two conditions at \(X=0\) hold. The sum of the bounds for \(n\ge1\) is at most \(\sum_{n\ge1}10^{-3n}/2<10^{-3}\), so \(|f-1|<10^{-3}\).

*Smoothness.* Fix \(r<1\) and \(b\ge0\), and let \(c\) be \(2^b\) times the maximum, over \([-r,r]^2\) and over \(b'\le b\), of \(|\partial_Y^{b'}K_0|\). We show by induction on \(n\) that on \([-r,r]^2\)
\[
|\partial_Y^{b'}f_n|\le\frac{c^n|X|^{2n}}{(2n)!}\qquad(b'\le b).
\]
For \(n=0\) this is clear. By the rule of Leibniz, \(\partial_Y^{b'}(K_0f_n)\) is a sum of \(2^{b'}\) products of a derivative of \(K_0\) and a derivative of \(f_n\), of orders at most \(b\), so \(|\partial_Y^{b'}(K_0f_n)|\le c\cdot c^n|u|^{2n}/(2n)!\) at the point \((u,Y)\). Differentiating under the integral and using the same integral as in the first step gives the bound for \(f_{n+1}\). In the same way \(|\partial_X\partial_Y^{b'}f_{n+1}|\le c^{n+1}|X|^{2n+1}/(2n+1)!\). So the series of the derivatives \(\partial_Y^{b'}f_n\) and \(\partial_X\partial_Y^{b'}f_n\) converge uniformly on \([-r,r]^2\), and \(f\) has the continuous derivatives \(\partial_Y^{b'}f\) and \(\partial_X\partial_Y^{b'}f\) for all \(b'\). Moreover \(\partial_X^2\partial_Y^{b'}f_{n+1}=-\partial_Y^{b'}(K_0f_n)\), and these series converge uniformly as well, so \(\partial_X^2\partial_Y^{b'}f=-\partial_Y^{b'}(K_0f)\). By induction on \(a\ge2\), the derivative \(\partial_X^a\partial_Y^{b'}f=-\partial_X^{a-2}\partial_Y^{b'}(K_0f)\) exists and is continuous. So \(f\) is smooth.

The curvature of \(\bar g\) is \(-f_{XX}/f=K_0\) by Lemma 3.1. For \(v=(v_1,v_2)\), \(\bar g(v,v)=v_1^2+f^2v_2^2\) and \(0.99<f^2<1.01\). \(\blacksquare\)

## 4. A disk of negative curvature

Let \(F\) be an isometric immersion of \((U,g)\) and \(e\) a unit vector. Choose an orthonormal basis \(e_1,e_2\) of the plane orthogonal to \(e\), and let \(\psi=(\langle F,e_1\rangle,\langle F,e_2\rangle)\colon U\to\mathbb R^2\). We say that \(F\) is a *graph over the plane orthogonal to \(e\)* if \(\psi\) is a diffeomorphism from \(U\) onto an open subset of \(\mathbb R^2\). Then \(u=\langle F,e\rangle\circ\psi^{-1}\) is a smooth function on \(\psi(U)\), and \(F=G\circ\psi\) with \(G(\xi)=\xi_1e_1+\xi_2e_2+u(\xi)e\).

**Lemma 4.1.** In this situation, let \(D^2u\) be the matrix of the second derivatives of \(u\), \(Du\) its gradient, and \(J\) the matrix of the first derivatives of \(\psi\). Then, for the normal \(n\) with \(\langle n,e\rangle>0\),
\[
\begin{gathered}
\mathrm{II}=J^{\mathsf T}\Bigl(\frac{D^2u}{\sqrt{1+|Du|^2}}\circ\psi\Bigr)J,\\
K=\frac{\det D^2u}{(1+|Du|^2)^2}\circ\psi .
\end{gathered}
\]
In particular \(K(p)\) and \(\det D^2u(\psi(p))\) have the same sign, and \(\mathrm{II}(p)\) and \(D^2u(\psi(p))\) have the same rank.

**Proof.** The vectors \(\partial_1G=e_1+u_1e\) and \(\partial_2G=e_2+u_2e\) are orthogonal to \(m=(-u_1e_1-u_2e_2+e)/\sqrt{1+|Du|^2}\), a unit vector with \(\langle m,e\rangle>0\). Since \(F=G\circ\psi\), the tangent plane of \(F\) at \(p\) is spanned by \(\partial_1G,\partial_2G\) at \(\psi(p)\), so \(n=m\circ\psi\). By the chain rule,
\[
\begin{aligned}
\partial_i\partial_jF&=\sum_{a,b}\partial_i\psi_a\,\partial_j\psi_b\,(\partial_a\partial_bG)\circ\psi\\
&\quad+\sum_a\partial_i\partial_j\psi_a\,(\partial_aG)\circ\psi .
\end{aligned}
\]
The last sum is orthogonal to \(n\), and \(\langle\partial_a\partial_bG,m\rangle=u_{ab}/\sqrt{1+|Du|^2}\). This is the first formula. The metric is \(g=J^{\mathsf T}(\gamma\circ\psi)J\) with \(\gamma_{ab}=\langle\partial_aG,\partial_bG\rangle\), the unit matrix plus the matrix \((u_au_b)\), and \(\det\gamma=1+|Du|^2\). By Theorem 1.1,
\[
K=\frac{\det\mathrm{II}}{\det g}=\frac{\det D^2u}{(1+|Du|^2)\det\gamma}\circ\psi .
\]
The matrix \(J\) is invertible, which gives the statement on the rank. \(\blacksquare\)

**Proposition 4.2.** Let \(\mathcal D\) be an open round disk whose closure lies in \(U\). Suppose that \(K<0\) in \(\mathcal D\) and \(K=0\) on the boundary circle \(\partial\mathcal D\), and that \(F\) is an isometric immersion of \((U,g)\) that is a graph over a plane. Then there is a point \(b\in\partial\mathcal D\) at which \(\mathrm{II}(b)\) has rank one.

**Proof.** Use the notation above. The set \(\Omega=\psi(\mathcal D)\) is open and bounded, its closure is the compact set \(\psi(\overline{\mathcal D})\), and its boundary is the closed curve \(\psi(\partial\mathcal D)\), parametrized by a smooth map \(\beta\) on the circle. By Lemma 4.1, \(\det D^2u<0\) in \(\Omega\).

Suppose that \(\mathrm{II}\) vanishes at every point of \(\partial\mathcal D\). By Lemma 4.1, \(D^2u=0\) at every point of the curve \(\beta\). Then the derivative of \(Du\circ\beta\) along the circle is \(D^2u(\beta)\beta'=0\), so \(Du\) is a constant vector \(a\) on the curve. Then the derivative of \(u\circ\beta-\langle a,\beta\rangle\) is \(\langle Du(\beta)-a,\beta'\rangle=0\), so \(u(\xi)=\langle a,\xi\rangle+c\) on the curve, with a constant \(c\). Let
\[
v(\xi)=u(\xi)-\langle a,\xi\rangle-c .
\]
Then \(v=0\) on the boundary of \(\Omega\), and \(\det D^2v=\det D^2u<0\) in \(\Omega\). The function \(v\) is not identically zero in \(\Omega\), because its Hessian is not zero there. So the continuous function \(v\) on the compact set \(\overline\Omega\) has a positive maximum or a negative minimum, attained at a point of \(\Omega\). At an interior maximum the Hessian is negative semidefinite, at an interior minimum positive semidefinite; in both cases its determinant is not negative. This contradicts \(\det D^2v<0\).

So \(\mathrm{II}(b)\ne0\) for some \(b\in\partial\mathcal D\). By Theorem 1.1, \(\det\mathrm{II}(b)=K(b)\det g(b)=0\). A symmetric matrix with two rows that is not zero and has determinant zero has rank one. \(\blacksquare\)

According to [OpenAI-I, Section 5], this observation is the third step of Section 2 of N. Nadirashvili and Y. Yuan, *Counterexamples for local isometric embedding* (2002), https://arxiv.org/abs/math/0208127.

## 5. Exercises

**5.1.** Let \(u\) be a function on an open set of the plane and \(F(x)=(x_1,x_2,u(x))\), with the metric \(g_{ij}=\delta_{ij}+u_iu_j\). For the height \(z=u\) in the direction \(e=(0,0,1)\), compute \(H\), \(|dz|_g^2\) and both sides of the height equation.

**5.2.** Let \(F\) be an isometric immersion of \((U,g)\) and \(K>0\) on \(U\). Show that for every unit vector \(e\) the height \(\langle F,e\rangle\) has only nondegenerate critical points: where its differential vanishes, the determinant of the matrix of its second derivatives is positive.

**5.3.** Let \(\lambda>0\) be a constant. Show that \(K_{\lambda^2g}=\lambda^{-2}K_g\).

**5.4.** In Proposition 3.2, show that the curves \(Y=\text{const}\) have the length \(|X_1-X_0|\) between the parameters \(X_0\) and \(X_1\), and that \(f\) is determined by \(K_0\).

## 6. Solutions

**5.1.** Here \(\psi\) is the identity, \(\nu=1/\sqrt{1+|Du|^2}\), and by Lemma 4.1 and Theorem 2.1
\[
\begin{gathered}
H=\nu\,\mathrm{II}=\frac{D^2u}{1+|Du|^2},\\
|dz|_g^2=1-\nu^2=\frac{|Du|^2}{1+|Du|^2}.
\end{gathered}
\]
The left side of the height equation is \(\det D^2u/(1+|Du|^2)^2\). On the right side, \(K=\det D^2u/(1+|Du|^2)^2\), \(\det g=1+|Du|^2\) and \(1-|dz|_g^2=1/(1+|Du|^2)\); the product is the same.

**5.2.** At a critical point \(b\) of \(z\), \(dz(b)=0\), so \(H(b)\) is the matrix of the second derivatives of \(z\) at \(b\), and by the height equation its determinant is \(K(b)\det g(b)>0\).

**5.3.** Multiplying \(g\) by \(\lambda^2\) multiplies the inverse by \(\lambda^{-2}\) and leaves the Christoffel symbols unchanged. In the formula for \(K\det g\) the right side is multiplied by \(\lambda^2\), and \(\det g\) by \(\lambda^4\).

**5.4.** Along \(Y=\text{const}\) the velocity is \((1,0)\), of length \(\sqrt{g_{11}}=1\). If \(f\) and \(\tilde f\) both satisfy the three conditions, \(d=f-\tilde f\) satisfies \(d(X,Y)=-\int_0^X(X-u)K_0d\,du\). If \(m\) is the supremum of \(|d|\) on the segment from \((0,Y)\) to \((X,Y)\), this gives \(m\le10^{-3}m/2\), so \(m=0\).

## References

- [OpenAI-I] OpenAI, *A smooth metric with no local isometric immersion into three-space*, OpenAI Math Release preprint, 24 September 2026, Sections 1, 2 and 5. https://github.com/openai/math/tree/main/preprints/A-Smooth-Metric-with-No-Local-Isometric-Immersion-into-Three-Space-September-24-2026
