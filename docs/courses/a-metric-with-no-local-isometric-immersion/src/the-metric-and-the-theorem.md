# The metric and the theorem

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson constructs a smooth metric on the square \((-1,1)^2\) and proves that no neighbourhood of the origin has a smooth isometric immersion into \(\mathbb R^3\), assuming one statement about the height equation on a fixed square, the *patch obstruction* (P). The statement (P) is the analytic part of the proof of [OpenAI-I]; it is stated exactly in Section 1 and proved in the last lesson of the course, [The oscillating perturbation](the-oscillating-perturbation.md), which uses the four lessons before it.

- (P): near a model metric whose curvature is \(\kappa(x^2-h(y))\) there are metrics for which the height equation has no solution on the whole square \([-3,3]^2\) with a nonzero second derivative across the \(x\)-direction and a small mixed derivative (Section 1).
- Small copies of such squares, in finitely many orientations, are placed so that they accumulate at every boundary point of disks of negative curvature, and the disks accumulate at the origin (Lemma 3.1). All the pieces add up to one smooth metric (Section 4).
- An isometric immersion near the origin would, by the lesson on heights, produce a boundary point of a disk where the second fundamental form has rank one, and then a solution of the height equation on one of the small squares that (P) excludes (Theorem 5.1).
- The metric has the same Taylor series at the origin as the Euclidean metric (Corollary 6.1).

The lesson follows [OpenAI-I, Sections 2 and 5]. It continues [Heights of an immersed surface](heights-of-an-immersed-surface.md), whose notation it uses: metrics on plane domains, the curvature \(K\), the covariant Hessian \(H\) of a function \(z\), and isometric immersions.

## 1. The model square and the patch obstruction

Fix a smooth even function \(h\colon\mathbb R\to\mathbb R\) with
\[
\begin{gathered}
h=1\ \text{on }[-\tfrac12,\tfrac12],\qquad h'\le0\ \text{on }[0,\infty),\\
h>0\ \text{on }(-1,1),\qquad h<0\ \text{for }|y|>1,\\
h(1)=0,\qquad h'(1)<0 .
\end{gathered}
\]
Such functions exist (Exercise 7.1). Let \(S=[-3,3]^2\), with the coordinates \(x,y\), and \(\mathcal P=[-\tfrac1{10},\tfrac1{10}]^2\). A *model metric with the constant \(\kappa>0\)* is a metric \(g_0\) on an open set containing \(S\) with
\[
K_{g_0}(x,y)=\kappa\bigl(x^2-h(y)\bigr)\qquad\text{on }S .
\]
The curvature is negative in the region \(x^2<h(y)\) around the centre and positive outside its closure. On \([-\tfrac15,\tfrac15]^2\) it is at most \(-\tfrac{24}{25}\kappa\), because \(h=1\) and \(x^2\le\tfrac1{25}\) there.

A *perturbation* is a symmetric matrix \(\eta\) of smooth functions on the plane that vanish outside \(\mathcal P\). Its norm \(\|\eta\|_{C^m}\) is the largest absolute value of an entry or of a derivative of an entry of order at most \(m\). For a metric \(g\) on a neighbourhood of \(S\), a function \(z\) and the covariant Hessian \(H\) of \(z\), let
\[
\begin{gathered}
E=\det g\,\bigl(1-|dz|_g^2\bigr),\\
q=\frac{H_{xy}}{H_{yy}}\quad\text{where }H_{yy}\ne0 .
\end{gathered}
\]

**Definition 1.1.** An *admissible height* for \(g\) is a smooth function \(z\) on a neighbourhood of \(S\) such that at every point of \(S\)
\[
\begin{gathered}
H_{xx}H_{yy}-H_{xy}^2=KE,\\
E>0,\qquad H_{yy}\ne0,\qquad|q|\le\tfrac1{100}.
\end{gathered}
\]

The first condition is the height equation of the lesson on heights. The others say that \(|dz|_g<1\), that the Hessian does not vanish in the direction of \(y\), and that the Hessian is nearly diagonal in the coordinates \(x,y\).

**The patch obstruction (P).** Let \(g_0\) be a model metric with a constant \(\kappa>0\). For every \(m\ge0\) and every \(\varepsilon>0\) there is a perturbation \(\eta\) with \(\|\eta\|_{C^m}<\varepsilon\) such that \(g_0+\eta\) is positive definite and has no admissible height.

This is the proposition on the patch obstruction of [OpenAI-I, Section 2], in the form that the construction needs. It is Theorem 1.3 of the lesson on the oscillating perturbation, which shows more: among the metrics \(g_0+\eta\) that are positive definite with curvature below \(-\kappa/2\) on \([-\tfrac15,\tfrac15]^2\), those without an admissible height form a set whose complement is a countable union of nowhere dense sets, for the topology of the convergence of all derivatives. The proof has two parts. The first is an estimate, proved in the lesson [Regularity on a cap](regularity-on-a-cap.md). Above and below the central region, where the metric is the model metric, an admissible height with bounds on its derivatives up to order eight has bounds on its derivatives of every order, although the height equation changes its type where the curvature changes its sign. The second is an argument by category, in the lesson on the oscillating perturbation. If the metrics that have an admissible height with fixed bounds were dense in an open set, a thin and rapidly oscillating perturbation of the metric in the central region would force a change of a derivative of the height across the thin strip, of a definite size, and this is incompatible with the bounds on both sides. The theorem of Baire then gives the metrics without admissible heights.

Statement (P) concerns a whole square of a fixed size. Every zero of the curvature in \(S\) is a point where the differential of \(K\) is not zero (Exercise 7.2), and according to [OpenAI-I, Section 1] local isometric immersions exist near such points, by a theorem of G. Nakamura and Y. Maeda. So an obstruction can only come from the square as a whole.

## 2. A form of rank one in a rotated frame

**Lemma 2.1.** Let \(B\) be a symmetric bilinear form of rank one on \(\mathbb R^2\), and let \(r_1,r_2\) be an orthonormal basis such that the line of \(r_1\) makes the angle \(\alpha\) with the kernel of \(B\), \(|\alpha|<\tfrac\pi2\). Then \(B(r_2,r_2)\ne0\) and
\[
\Bigl|\frac{B(r_1,r_2)}{B(r_2,r_2)}\Bigr|=|\tan\alpha| .
\]

**Proof.** Let \(k\) be a unit vector in the kernel and \(m\) a unit vector orthogonal to it. Then \(B(v,w)=c\,\langle v,m\rangle\langle w,m\rangle\) with \(c=B(m,m)\ne0\). After changing the signs of \(k\) and \(m\) if necessary, \(r_1=\cos\alpha\,k+\sin\alpha\,m\) and \(r_2=\pm(-\sin\alpha\,k+\cos\alpha\,m)\). So \(B(r_2,r_2)=c\cos^2\alpha\ne0\) and \(B(r_1,r_2)=\pm c\sin\alpha\cos\alpha\). \(\blacksquare\)

For \(|\alpha|<\tfrac1{1000}\) the quotient is smaller than \(\tfrac1{100}\).

## 3. Disks and patches

Let \(Q=(-1,1)^2\), with the coordinates \(X,Y\). For \(j\ge1\) let \(\mathcal D_j\) be the open disk with the centre \(c_j=(2^{-j},0)\) and the radius \(\rho_j=2^{-j-4}\), and \(\mathcal D_j^+\) the open disk with the same centre and the radius \(2\rho_j\). The closures of the disks \(\mathcal D_j^+\) are pairwise disjoint, lie in \(Q\) and do not contain the origin: the distance of the centres \(c_j\) and \(c_{j+1}\) is \(2^{-j-1}\), more than the sum \(3\cdot2^{-j-4}\) of the radii \(2^{-j-3}\) and \(2^{-j-4}\) of \(\mathcal D_j^+\) and \(\mathcal D_{j+1}^+\). The disks converge to the origin.

Fix rotations \(R_1,\dots,R_A\) of the plane such that every line through the origin makes an angle smaller than \(\tfrac1{1000}\) with the line of \(R_ae_1\) for some \(a\), where \(e_1=(1,0)\); for example the \(A=3143\) rotations by the angles \(0,\tfrac1{1000},\tfrac2{1000},\dots,\tfrac{3142}{1000}\), the last of which is larger than \(\pi\). A *patch map* is a map \(\Phi(x,y)=c+\lambda R_a(x,y)\) with \(c\in\mathbb R^2\), \(\lambda>0\) and one of these rotations; its *full patch* is the square \(\Phi([-4,4]^2)\), which lies in the closed disk of radius \(4\sqrt2\,\lambda\) around \(c\).

**Lemma 3.1.** There is a sequence of patch maps \(\Phi_n=c_n+\lambda_nR_{a(n)}\), \(n\ge1\), with \(\lambda_n\le1\), such that:

1. the full patches are pairwise disjoint, and each of them lies in one of the sets \(\mathcal D_j^+\setminus\overline{\mathcal D_j}\);
2. for every \(j\), every point \(b\) of the circle \(\partial\mathcal D_j\), every \(a\le A\) and every \(\delta>0\) there is an \(n\) with \(a(n)=a\) whose full patch lies in the disk of radius \(\delta\) around \(b\).

**Proof.** Fix \(j\). For \(k\ge1\) take on the circle of radius \(\rho_j(1+2^{-k})\) around \(c_j\) the \(A2^k\) points with the angles \(2\pi i/(A2^k)\), \(0\le i<A2^k\), and give the point with the index \(i\) the rotation \(R_a\) with \(a-1\equiv i\) modulo \(A\). Let \(d\) be the smallest distance of two of these points, and choose \(\lambda>0\) with
\[
4\sqrt2\,\lambda<\min\bigl\{\tfrac d2,\ \rho_j2^{-k-2}\bigr\}.
\]
Use this \(\lambda\) for all these points. Their full patches are pairwise disjoint, because they lie in disks of radius smaller than \(d/2\) around the points. They lie in the annulus of the points whose distance from \(c_j\) is between \(\rho_j(1+2^{-k}-2^{-k-2})\) and \(\rho_j(1+2^{-k}+2^{-k-2})\). These annuli are pairwise disjoint for different \(k\), since \(2^{-k-1}+2^{-k-3}<2^{-k}-2^{-k-2}\), and they lie in \(\mathcal D_j^+\setminus\overline{\mathcal D_j}\), since \(2^{-k}+2^{-k-2}<1\). Patches for different \(j\) are disjoint because the \(\mathcal D_j^+\) are. Enumerate the patch maps for all \(j,k,i\) as a sequence. This gives (1).

For (2), let \(b\in\partial\mathcal D_j\) have the angle \(\theta\) as seen from \(c_j\). On the circle with the index \(k\), the points with the rotation \(R_a\) have angles at distances \(2\pi/2^k\) from one another, so one of them, \(p\), has an angle within \(\pi/2^k\) of \(\theta\). Then \(|p-b|\le\rho_j2^{-k}+2\rho_j\pi/2^k\), and the full patch around \(p\) lies in the disk of radius \(8\rho_j2^{-k}\) around \(b\). This is smaller than \(\delta\) for large \(k\). \(\blacksquare\)

## 4. The metric

**Lemma 4.1.** Let \(w_1,w_2,\dots\) be smooth functions on an open set \(V\subseteq\mathbb R^2\) such that for every \(m\) the series \(\sum_i\|w_i\|_{C^m}\) converges, where \(\|w\|_{C^m}\) is the supremum over \(V\) of the absolute values of \(w\) and of its derivatives of order at most \(m\). Then \(w=\sum_iw_i\) is smooth, and every derivative of \(w\) is the sum of the derivatives of the \(w_i\).

**Proof.** The series of the derivatives of each order converge uniformly, and a uniformly convergent series of continuously differentiable functions whose derivatives converge uniformly may be differentiated term by term. \(\blacksquare\)

The condition holds if \(\|w_i\|_{C^m}\le C2^{-i}\) for all \(i\ge m\), with a constant \(C\).

**The curvature.** For each \(j\) let \(\beta_j\) be the function that is \(-\exp\bigl(-1/(\rho_j^2-|p-c_j|^2)\bigr)\) at the points \(p\) of \(\mathcal D_j\) and \(0\) elsewhere; it is smooth on the plane and negative exactly in \(\mathcal D_j\). Fix a smooth function \(\chi\) on the plane that is \(1\) on \([-\tfrac72,\tfrac72]^2\) and \(0\) outside \((-4,4)^2\). For each \(n\) let \(\gamma_n\) be the function that is
\[
\bigl(\chi(x,y)\,(x^2-h(y))\bigr)\circ\Phi_n^{-1}
\]
on the full patch of \(\Phi_n\) and \(0\) elsewhere; it is smooth. Enumerate all the functions \(\beta_j\) and \(\gamma_n\) as one sequence \(w_1,w_2,\dots\), and choose numbers \(\epsilon_i>0\) with
\[
\|\epsilon_iw_i\|_{C^m}\le10^{-3}\,2^{-i}\qquad(0\le m\le i).
\]
Let \(K_0=\sum_i\epsilon_iw_i\). By Lemma 4.1 it is smooth on the plane, and \(|K_0|\le10^{-3}\). The sets where the functions \(w_i\) are not zero are pairwise disjoint, by Lemma 3.1. Therefore:

- \(K_0<0\) in every disk \(\mathcal D_j\);
- \(K_0\circ\Phi_n=\kappa_n(x^2-h(y))\) on \([-\tfrac72,\tfrac72]^2\), where \(\kappa_n>0\) is the number \(\epsilon_i\) of \(\gamma_n\);
- \(K_0=0\) outside the disks \(\mathcal D_j\) and the full patches, in particular on every circle \(\partial\mathcal D_j\) and at the origin.

**The background metric.** Let \(\bar g=dX^2+f^2\,dY^2\) be the metric on \(Q\) with the curvature \(K_0\) given by Proposition 3.2 of the lesson on heights. For every \(n\), the pull-back \(g_{0,n}=\lambda_n^2R^{\mathsf T}(\bar g\circ\Phi_n)R\), with \(R=R_{a(n)}\), is a metric on a neighbourhood of \([-4,4]^2\), and by Lemma 1.2 of the lesson on heights its curvature is \(K_0\circ\Phi_n\). So \(g_{0,n}\) is a model metric with the constant \(\kappa_n\).

**The perturbations.** Assume (P). For a perturbation \(\eta\) and a patch map \(\Phi=c+\lambda R\), let \(\widehat\eta\) be the symmetric matrix of functions that is
\[
\lambda^{-2}R\,(\eta\circ\Phi^{-1})\,R^{\mathsf T}
\]
on the full patch and \(0\) elsewhere. It is smooth, it vanishes outside \(\Phi(\mathcal P)\), and \(\lambda^2R^{\mathsf T}(\widehat\eta\circ\Phi)R=\eta\). Since \(\Phi^{-1}(p)=\lambda^{-1}R^{\mathsf T}(p-c)\), every differentiation of \(\eta\circ\Phi^{-1}\) gives a factor \(\lambda^{-1}\) and a sum of two terms with coefficients of absolute value at most \(1\); so, for \(\lambda\le1\),
\[
\|\widehat\eta\|_{C^m}\le4\cdot2^m\lambda^{-m-2}\|\eta\|_{C^m}.
\]
By (P), applied to \(g_{0,n}\) with \(m=n\), there is a perturbation \(\eta_n\) such that \(g_{0,n}+\eta_n\) is positive definite and has no admissible height, and so small that
\[
\|\widehat\eta_n\|_{C^m}\le\tfrac25\,2^{-n}\qquad(0\le m\le n).
\]

**Definition 4.2.** The metric \(g\) on \(Q\) is
\[
g=\bar g+\sum_{n\ge1}\widehat\eta_n .
\]

**Proposition 4.3.** Assume (P).

1. \(g\) is a smooth metric on \(Q\).
2. For every \(n\), the pull-back \(\lambda_n^2R^{\mathsf T}(g\circ\Phi_n)R\) of \(g\) by \(\Phi_n\) is \(g_{0,n}+\eta_n\) on \((-4,4)^2\). It has no admissible height.
3. \(K_g<0\) in every disk \(\mathcal D_j\), and \(K_g=0\) on every circle \(\partial\mathcal D_j\).

**Proof.** (1) The sum is smooth by Lemma 4.1. For a symmetric matrix \(\eta\) with entries of absolute value at most \(\delta\), \(|\eta(v,v)|\le2\delta|v|^2\) (Exercise 7.3). The entries of \(\sum_n\widehat\eta_n\) are at most \(\tfrac25\) in absolute value, and \(\bar g(v,v)\ge0.99|v|^2\), so \(g(v,v)\ge0.19|v|^2\).

(2) On the full patch of \(\Phi_n\) all the other \(\widehat\eta_{n'}\) vanish, because the full patches are disjoint. So \(g=\bar g+\widehat\eta_n\) there, and the pull-back is \(g_{0,n}+\eta_n\).

(3) No full patch meets the closed disk \(\overline{\mathcal D_j}\). So every \(\widehat\eta_n\) vanishes on \(\mathcal D_j\), \(g=\bar g\) there, and \(K_g=K_0<0\). Let \(b\in\partial\mathcal D_j\). Every \(\widehat\eta_n\) vanishes in a neighbourhood of \(b\), because its support is a compact set that does not contain \(b\). By Lemma 4.1 all derivatives of \(g-\bar g\) vanish at \(b\). The curvature at a point depends only on the derivatives of the metric of order at most two at that point, so \(K_g(b)=K_{\bar g}(b)=K_0(b)=0\). \(\blacksquare\)

In (3) the neighbourhood of \(b\) on which \(\widehat\eta_n\) vanishes depends on \(n\); no neighbourhood of \(b\) avoids all the patches.

## 5. The theorem

**Theorem 5.1 (OpenAI).** Assume the patch obstruction (P). Then the smooth metric \(g\) on \((-1,1)^2\) of Definition 4.2 has the following property: for no open neighbourhood \(U\) of the origin is there a smooth isometric immersion of \((U,g)\) into \(\mathbb R^3\).

**Proof.** Suppose that \(F\colon U\to\mathbb R^3\) is such an immersion.

*A graph.* Let \(e_0\) be the unit normal at the origin and \(e_1,e_2\) an orthonormal basis of the plane orthogonal to \(e_0\), and \(\psi=(\langle F,e_1\rangle,\langle F,e_2\rangle)\). The vectors \(\partial_1F(0)\), \(\partial_2F(0)\) are linearly independent and orthogonal to \(e_0\), so the matrix of the first derivatives of \(\psi\) at the origin is invertible. By the inverse function theorem there is an open neighbourhood \(U_1\subseteq U\) of the origin that \(\psi\) maps diffeomorphically onto an open set. On \(U_1\), \(F\) is a graph over the plane orthogonal to \(e_0\).

*A boundary point.* Choose \(j\) with \(\overline{\mathcal D_j}\subseteq U_1\). By Proposition 4.3 the curvature of \(g\) is negative in \(\mathcal D_j\) and zero on \(\partial\mathcal D_j\). By Proposition 4.2 of the lesson on heights there is a point \(b\in\partial\mathcal D_j\) at which the second fundamental form \(\mathrm{II}(b)\) has rank one.

*A height.* Let \(e\) be the unit normal at \(b\) and \(z=\langle F,e\rangle\) on \(U_1\), with the covariant Hessian \(H\). By Theorem 2.1 of the lesson on heights, \(dz(b)=0\) and \(H(b)=\mathrm{II}(b)\). Choose \(a\) such that the line of \(R_ae_1\) makes an angle smaller than \(\tfrac1{1000}\) with the kernel of \(H(b)\), and let \(r_1=R_ae_1\), \(r_2=R_ae_2\). By Lemma 2.1,
\[
\begin{gathered}
H(b)(r_2,r_2)\ne0,\\
\Bigl|\frac{H(b)(r_1,r_2)}{H(b)(r_2,r_2)}\Bigr|<\frac1{100}.
\end{gathered}
\]
By continuity there is an open neighbourhood \(W\subseteq U_1\) of \(b\) on which \(|dz|_g<1\), \(H(r_2,r_2)\ne0\) and \(|H(r_1,r_2)|<\tfrac1{100}|H(r_2,r_2)|\).

*A patch.* By Lemma 3.1 there is an \(n\) with \(a(n)=a\) whose full patch lies in \(W\). Let \(\Phi=\Phi_n\), \(\lambda=\lambda_n\), \(R=R_a\), and \(g'=\lambda^2R^{\mathsf T}(g\circ\Phi)R\) on \((-4,4)^2\), an open set that contains \(S\). By Lemma 1.2 of the lesson on heights, \(F\circ\Phi\) is an isometric immersion of \(((-4,4)^2,g')\), and \(z'=z\circ\Phi\) is its height in the direction \(e\). By Theorem 2.1 of that lesson, \(z'\) satisfies the height equation for \(g'\). By Lemma 1.2 its covariant Hessian is \(H'=\lambda^2R^{\mathsf T}(H\circ\Phi)R\), that is
\[
\begin{gathered}
H'_{yy}=\lambda^2H(r_2,r_2)\circ\Phi,\\
H'_{xy}=\lambda^2H(r_1,r_2)\circ\Phi,
\end{gathered}
\]
and \(|dz'|_{g'}=|dz|_g\circ\Phi\). So on \(S\): \(H'_{yy}\ne0\), \(|H'_{xy}/H'_{yy}|<\tfrac1{100}\), and \(E'=\det g'\,(1-|dz'|_{g'}^2)>0\). Hence \(z'\) is an admissible height for \(g'\). But \(g'=g_{0,n}+\eta_n\) has no admissible height, by Proposition 4.3. This contradiction proves the theorem. \(\blacksquare\)

The statement (P) is Theorem 1.3 of the lesson on the oscillating perturbation, so the assumption of Theorem 5.1, and of Corollary 6.1 below, is satisfied. An embedding is an immersion, so no neighbourhood of the origin has a smooth isometric embedding either. The curvature of \(g\) takes both signs in every neighbourhood of the origin. According to [OpenAI-I, Section 1], the question whether every smooth metric on a surface has smooth local isometric immersions into \(\mathbb R^3\) is part of S.-T. Yau's discussion of isometric embeddings and is stated as a problem in M. Ghomi's survey of open problems on curves and surfaces; for real analytic metrics local immersions exist by the theorem of M. Janet and É. Cartan; and Theorem 5.1 does not settle the question under either of the restrictions \(K\ge0\) and \(K\le0\).

## 6. The Taylor series at the origin

**Corollary 6.1.** Assume (P). For the metric \(g\) of Definition 4.2, all derivatives of all orders of the functions \(g_{ij}-\delta_{ij}\) vanish at the origin, where \(\delta_{ij}\) is \(1\) for \(i=j\) and \(0\) otherwise. So whether a smooth metric has a smooth isometric immersion near a point is not determined by its Taylor series at the point.

**Proof.** Every function \(w_i\) of Section 4 and every \(\widehat\eta_n\) vanishes in a neighbourhood of the origin, because its support is a compact set that does not contain the origin. By Lemma 4.1 all derivatives of \(K_0\) and of \(\sum_n\widehat\eta_n\) vanish at the origin. It remains to consider \(\bar g=dX^2+f^2\,dY^2\). Since \(f(0,Y)=1\) and \(f_X(0,Y)=0\), the derivatives \(\partial_Y^b(f-1)\) and \(\partial_X\partial_Y^b(f-1)\) vanish at the origin for all \(b\). For \(a\ge2\),
\[
\partial_X^a\partial_Y^bf=-\partial_X^{a-2}\partial_Y^b(K_0f),
\]
and by the rule of Leibniz every term of the right side contains \(K_0\) or one of its derivatives as a factor, and these vanish at the origin. So all derivatives of \(f-1\) vanish at the origin, and then those of \(f^2-1=(f-1)(f+1)\). The Euclidean metric \(dX^2+dY^2\) has the isometric immersion \((X,Y)\mapsto(X,Y,0)\); the metric \(g\) has none near the origin. \(\blacksquare\)

## 7. Exercises

**7.1.** Let \(\varrho\ge0\) be a smooth function on \(\mathbb R\) that vanishes outside \([\tfrac12,2]\) and is positive on \((\tfrac12,\tfrac32)\). Show that
\[
h(y)=1-\frac{\int_0^{|y|}\varrho(v)\,dv}{\int_0^1\varrho(v)\,dv}
\]
has the properties required in Section 1.

**7.2.** Show that at every point of \(S\) where \(K=\kappa(x^2-h(y))\) vanishes, one of the partial derivatives of \(K\) is not zero.

**7.3.** Let \(\eta\) be a symmetric matrix with two rows whose entries have absolute value at most \(\delta\). Show that \(|\eta(v,v)|\le2\delta|v|^2\) for all \(v\in\mathbb R^2\).

**7.4.** Let \(F\) be an isometric immersion of \((U,g)\) and \(b\in U\) a point with \(K(b)<0\). Show that for the height \(z\) in the direction of the normal at \(b\), the Hessian \(H(b)\) is indefinite, and that there is an orthonormal basis \(r_1,r_2\) with \(H(b)(r_2,r_2)\ne0\) and \(H(b)(r_1,r_2)=0\).

## 8. Solutions

**7.1.** Let \(c=\int_0^1\varrho>0\). Near \(y=0\) the function is \(1\), because \(\varrho=0\) on \([0,\tfrac12]\); away from \(0\) it is smooth because \(|y|\) is. It is even. For \(y>0\), \(h'(y)=-\varrho(y)/c\le0\), and \(h'(1)=-\varrho(1)/c<0\). \(h(1)=0\). For \(|y|<1\), \(\int_0^{|y|}\varrho<c\), because \(\varrho>0\) on the part of \((\tfrac12,1)\) above \(|y|\); so \(h>0\). For \(|y|>1\), \(\int_0^{|y|}\varrho>c\), because \(\varrho>0\) on \((1,\tfrac32)\); so \(h<0\).

**7.2.** \(\partial_xK=2\kappa x\). At a zero with \(x=0\), \(h(y)=0\), so \(y=\pm1\), and \(\partial_yK=-\kappa h'(y)\ne0\) there, since \(h'(1)<0\) and \(h'(-1)=-h'(1)\).

**7.3.** Since \(\eta(v,v)=\eta_{11}v_1^2+2\eta_{12}v_1v_2+\eta_{22}v_2^2\),
\[
\begin{aligned}
|\eta(v,v)|&\le\delta\,(|v_1|+|v_2|)^2\\
&\le2\delta\,(v_1^2+v_2^2).
\end{aligned}
\]

**7.4.** By Theorem 2.1 of the lesson on heights, \(H(b)=\mathrm{II}(b)\) and \(\det H(b)=K(b)\det g(b)<0\), so the symmetric form \(H(b)\) has one positive and one negative eigenvalue. An orthonormal basis of eigenvectors has the two properties.

## References

- [OpenAI-I] OpenAI, *A smooth metric with no local isometric immersion into three-space*, OpenAI Math Release preprint, 24 September 2026, Sections 1, 2 and 5. https://github.com/openai/math/tree/main/preprints/A-Smooth-Metric-with-No-Local-Isometric-Immersion-into-Three-Space-September-24-2026
