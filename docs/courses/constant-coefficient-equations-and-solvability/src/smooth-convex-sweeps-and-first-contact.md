# Smooth convex sweeps and first contact

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026. Self-checked by GPT-6.1 Sol (OpenAI). Public domain (CC0).*

A continuation proof needs a smooth surface at the first place where a singular set is encountered. We construct curved outer approximations of any compact convex set, interpolate them through a strictly nested family, and compute the exact outward gradient of the entry parameter.

Use multivariable differentiation, compact smooth mollifiers, the regular level theorem and the inverse function theorem. [Convex supports and convolution cancellation](../prerequisites/convex-supports-and-convolution-cancellation.html), Theorem 1.1, proves the compact-convex support characterization. The finite-dimensional separation theorem is [Fourier transforms, finite spectra and convex separation](../prerequisites/prerequisite-bridges.html), Theorem 4.1.

Let \(n\ge1\). A convex body means a nonempty compact convex subset of \(\mathbb R^n\) with nonempty interior. A smooth positively curved body has \(C^\infty\) boundary and positive definite second fundamental form for the outward normal, with the convention that this form is the derivative of the outward normal paired with tangent vectors. In dimension one the boundary is a two-point zero-dimensional manifold; positive definiteness on its zero tangent spaces is vacuous.

Hörmander’s seminar paper and Kalmes’s work on surjectivity explain the continuation setting. We prove the geometric construction and its quantitative bounds here.

## Smooth curved outer approximations

**Lemma 1.1.** If \(K\) is any nonempty compact convex set and \(U\) is an open neighborhood of \(K\), there is a smooth positively curved convex body \(L\) with
\[
K\subset\operatorname{int}L,\qquad L\subset U.
\tag{1}
\]
The set \(K\) can have empty interior, and the construction does not require it to contain the origin.

**Proof.** Choose \(\delta>0\) such that \(K+\overline B(0,\delta)\subset U\); compactness supplies such a positive distance margin. If \(U=\mathbb R^n\), any positive \(\delta\) is permitted. Put \(\Phi(x)=\operatorname{dist}(x,K)^2\).

For each \(x\), a closest point \(p(x)\in K\) exists by compactness. It is unique: if \(p,q\) were distinct minimizers, the midpoint belongs to \(K\), and the parallelogram identity gives
\[
\begin{gathered}
\left|x-\frac{p+q}{2}\right|^2
\\
=\frac{|x-p|^2+|x-q|^2}{2}-\frac{|p-q|^2}{4},
\end{gathered}
\tag{2}
\]
contradicting minimality. Comparing the segment from \(p(x)\) to \(y\in K\) at its initial point gives
\((x-p(x))\cdot(y-p(x))\le0\).
Using this twice at \(x,z\) gives
\[
\begin{gathered}
|p(x)-p(z)|^2
\\
\le(x-z)\cdot(p(x)-p(z)),
\end{gathered}
\tag{3}
\]
so the closest-point map is one-Lipschitz. Comparison with the old minimizer in each of \(\Phi(x+h)\) and \(\Phi(x)\) then yields
\(\Phi(x+h)=\Phi(x)+2(x-p(x))\cdot h+O(|h|^2)\).
Thus \(\Phi\) is continuously differentiable with that gradient, although the later smoothing does not need more differentiability.

It is convex. For \(0\le t\le1\), the point \((1-t)p(x)+tp(z)\) belongs to \(K\). Convexity of the squared Euclidean norm therefore gives
\[
\begin{gathered}
\Phi((1-t)x+tz)
\\
\le(1-t)\Phi(x)+t\Phi(z).
\end{gathered}
\tag{4}
\]
Let \(\rho_\varepsilon\) be a nonnegative compact smooth mollifier with mass one and support in \(\overline B(0,\varepsilon)\). Its convolution \(\Phi_\varepsilon=\rho_\varepsilon*\Phi\) is smooth and convex: convolution preserves (4) by integration, and derivatives can be moved to the compact smooth factor. Its Hessian is positive semidefinite, as follows from the nonnegative second differences of a smooth convex function. The one-Lipschitz property of distance gives the global lower bound and compact-set upper bound
\[
\begin{gathered}
\Phi_\varepsilon(x)\ge
(\operatorname{dist}(x,K)-\varepsilon)_+^2,\\
\qquad
\Phi_\varepsilon(x)\le\varepsilon^2\quad(x\in K).
\end{gathered}
\tag{5}
\]

Put \(R=\max_{x\in K}|x|\). Choose
\[
\begin{gathered}
0<\varepsilon<\delta/8,\\
\qquad
0<\lambda<\frac{\delta^2}{64\max(1,R^2)},\\
\qquad
f(x)=\Phi_\varepsilon(x)+\lambda|x|^2,\\
\qquad
b=\delta^2/16.
\end{gathered}
\tag{6}
\]
Then \(f<b\) on \(K\), since \(f\le\varepsilon^2+\lambda R^2<\delta^2/32\) there. If \(\operatorname{dist}(x,K)\ge\delta\), (5) instead gives \(f(x)>(7\delta/8)^2>b\). Also \(f\ge\lambda|x|^2\), so its sublevel
\[
L=\{x:f(x)\le b\}
\tag{7}
\]
is compact, convex, contains \(K\) in its interior, and lies in \(K+B(0,\delta)\subset U\).

The Hessian obeys \(D^2f\ge2\lambda I\). There is exactly one critical point, the global minimizer: coercivity gives existence of a minimum, and the strong convexity inequality
\[
\begin{gathered}
f(y)\\
\ge f(x)+\nabla f(x)\cdot(y-x)+\lambda|y-x|^2
\end{gathered}
\tag{8}
\]
gives uniqueness of a critical point and of the minimum. Inequality (8) follows by integrating the Hessian along the line segment. The minimum is below \(b\), because \(K\ne\varnothing\) and \(f<b\) there. Hence \(\nabla f\ne0\) on \(f=b\). The regular level theorem makes \(\partial L\) smooth.

Its outward unit normal is \(\nu=\nabla f/|\nabla f|\). For a tangent vector \(v\) at the level,
\[
\begin{gathered}
v\cdot d\nu(v)
=\frac{v^TD^2f\,v}{|\nabla f|}
\\
\ge\frac{2\lambda|v|^2}{|\nabla f|}>0
\\
\quad(v\ne0).
\end{gathered}
\tag{9}
\]
This proves the required positive curvature. In dimension one the same argument gives a compact interval with two regular endpoints. \(\square\)

**Lemma 1.2 (nested outer approximations).** Let \(A\subset B\) be nonempty compact convex sets, with open neighborhoods \(U_0\supset A\), \(U_1\supset B\). Smooth positively curved bodies can be chosen so that
\[
\begin{gathered}
A\subset\operatorname{int}L_0,\quad L_0\subset U_0,\quad
\\
B\subset\operatorname{int}L_1,\quad L_1\subset U_1,\quad
\\
L_0\subset\operatorname{int}L_1.
\end{gathered}
\tag{10}
\]

**Proof.** Choose \(e>0\) so that
\(A+\overline B(0,e)\subset U_0\) and
\(B+\overline B(0,4e)\subset U_1\).
Apply Lemma 1.1 to \(A\), with an outer tolerance smaller than \(e/2\), to obtain \(L_0\subset A+B(0,e/2)\). Apply it to \(B+\overline B(0,e)\), with outer tolerance smaller than \(e\), to obtain \(L_1\subset B+B(0,2e)\subset U_1\). The first body lies in the interior of \(B+\overline B(0,e)\), hence in the interior of \(L_1\). This proves every inclusion, even if \(A=B\) or either original set has empty interior. \(\square\)

## A nested family and its normal velocity

**Theorem 2.1.** Let \(L_0\subset\operatorname{int}L_1\) be smooth positively curved bodies. Define
\[
\begin{gathered}
L_s=(1-s)L_0+sL_1,\\
\qquad 0\le s\le1.
\end{gathered}
\tag{11}
\]
Every \(L_s\) is smooth positively curved. For some \(a>0\),
\[
\begin{gathered}
L_s+\overline B(0,a(t-s))\subset L_t
\\
\qquad(0\le s<t\le1).
\end{gathered}
\tag{12}
\]
Their boundaries give a smooth foliation of
\(\operatorname{int}L_1\setminus L_0\).
The entry parameter \(\tau(x)\in(0,1)\), defined by \(x\in\partial L_{\tau(x)}\), is smooth. If \(\nu(x)\) is that boundary's outward unit normal and \(h_i\) are the endpoint support functions, then
\[
\nabla\tau(x)=\frac{\nu(x)}{h_1(\nu(x))-h_0(\nu(x))}.
\tag{13}
\]

**Proof in \(n\ge2\).** For a smooth positively curved convex body \(L\), each unit normal \(\nu\) has exactly one support point \(X_L(\nu)\). A linear maximum exists by compactness. If two points maximized, their segment would lie in the supporting plane and in the boundary. At a relative interior point of that segment the normal derivative in its nonzero tangent direction would be zero, contradicting positive curvature. The normal at the unique maximum is \(\nu\).

The outward Gauss map is therefore bijective onto the sphere. Its differential on tangent vectors is the positive definite shape operator, hence invertible. The inverse function theorem gives a smooth local inverse. Compactness and bijectivity give the global inverse \(X_L\), which is consequently smooth. No origin or symmetry hypothesis enters this argument.

Write \(h_L(\nu)=\nu\cdot X_L(\nu)\). Differentiation along a tangent vector \(v\) gives
\(dh_L(v)=v\cdot X_L\), since \(\nu\cdot dX_L(v)=0\).
Thus
\[
\begin{gathered}
X_L(\nu)=h_L(\nu)\nu+\nabla_Sh_L(\nu),\\
\qquad
dX_L(v)=(h_LI+\nabla_S^2h_L)v.
\end{gathered}
\tag{14}
\]
The second equality follows by differentiating the first in Euclidean space: the two normal components \(dh_L(v)\nu\) and \(-(\nabla_Sh_L\cdot v)\nu\) cancel. The support-curvature matrix
\(A_L=h_LI+\nabla_S^2h_L\)
is the inverse of the shape operator, and is positive definite.

The maximum of \(\nu\cdot((1-s)y+sz)\) over \(y\in L_0,z\in L_1\) is the sum of the two separate maxima. Consequently
\[
\begin{gathered}
h_s=(1-s)h_0+sh_1,\\
\quad
X_s=(1-s)X_0+sX_1,\\
\quad
A_s=(1-s)A_0+sA_1.
\end{gathered}
\tag{15}
\]
The last matrix is positive definite. The second map is a smooth immersion with tangent space \(\nu^\perp\).

It parametrizes the whole boundary of \(L_s\). To see existence of a supporting normal at any boundary point \(p\) without an unstated smoothness assumption on the sum, take points outside \(L_s\) tending to \(p\), and their closest points in \(L_s\). The projection inequality used in the approximation proof gives supporting unit normals. A subsequence converges to a unit supporting normal at \(p\). The unique maximizing endpoint points force \(p=X_s(\nu)\). Conversely every \(X_s(\nu)\) is a support point.

The parametrization is injective. At \(0<s<1\), if \(X_s(\nu')=X_s(\nu)\), evaluation by \(\nu\) shows that each of the two endpoint points \(X_i(\nu')\) also maximizes \(\nu\). Uniqueness gives \(X_i(\nu')=X_i(\nu)\), and their smooth endpoint normals give \(\nu'=\nu\). At \(s=0,1\), endpoint injectivity was already proved. Compactness makes this injective immersion an embedding, with its local inverse supplied by its positive tangent matrix. Its normal is \(\nu\) and its shape operator is \(A_s^{-1}>0\). This proves the smooth curvature assertion.

Since \(L_0\) is compactly contained in \(\operatorname{int}L_1\), choose \(a>0\) with \(L_0+\overline B(0,a)\subset L_1\). Then \(h_1-h_0\ge a\) on the unit sphere. Equation (15) gives \(h_t-h_s\ge a(t-s)\). The support characterization of compact convex sets and the support function of a ball prove (12). In particular the boundaries at distinct parameters are disjoint.

Every point \(x\in\operatorname{int}L_1\setminus L_0\) is on one of these boundaries. Indeed \(h_s\to h_0,h_1\) uniformly at the respective endpoints. Closedness of \(L_0\) and the support inequalities put \(x\) outside \(L_s\) for all sufficiently small \(s\), and the positive interior support margin in \(L_1\) puts it in the interior of \(L_s\) for \(s\) sufficiently near one. The least \(s\) with \(x\in L_s\) is in \((0,1)\), exists by uniform convergence of the support functions, and puts \(x\) on the boundary. If it were interior, its positive support margin would permit a slightly smaller parameter. Strict nesting makes this parameter unique.

The map \((s,\nu)\mapsto X_s(\nu)\) has tangential derivative \(A_s\) and normal velocity
\[
\nu\cdot\partial_sX_s=h_1(\nu)-h_0(\nu)\ge a>0.
\tag{16}
\]
Its full derivative is invertible. The inverse function theorem and the global uniqueness just proved give a smooth inverse on the shell. Its first coordinate is \(\tau\). Its gradient annihilates the tangent vectors \(A_sv\), and its pairing with \(\partial_sX_s\) is one. This gives exactly (13), including the positive outward sign. \(\square\)

**The dimension-one case.** Write \(L_i=[a_i,b_i]\) with \(a_1<a_0<b_0<b_1\). The family has endpoints \(a_s=(1-s)a_0+sa_1\), \(b_s=(1-s)b_0+sb_1\). The support differences in the normals \(-1,+1\) are \(a_0-a_1>0\) and \(b_1-b_0>0\). Take their minimum for \(a\) in (12). The two shell intervals have entry functions
\[
\begin{gathered}
\tau(x)=\frac{a_0-x}{a_0-a_1}\quad(a_1<x<a_0),\\
\qquad
\tau(x)=\frac{x-b_0}{b_1-b_0}\quad(b_0<x<b_1).
\end{gathered}
\tag{17}
\]
They prove all assertions and the normal gradient formula directly. No positive-dimensional spherical curvature formula is used in this endpoint.

## First contact with a closed set

**Corollary 3.1.** Let \(S\) be a closed subset of a neighborhood of \(L_1\), disjoint from \(L_0\), and containing some point in \(\operatorname{int}L_1\). There is a parameter \(s_0\in(0,1)\) and \(y\in S\cap\partial L_{s_0}\) such that \(S\cap\operatorname{int}L_{s_0}=\varnothing\).

**Proof.** Extend the continuous entry function to the closed shell \(L_1\setminus\operatorname{int}L_0\), assigning zero on \(\partial L_0\) and one on \(\partial L_1\). Its continuity follows from strict nesting (12) and the uniform convergence of the support functions. Equivalently any convergent sequence of shell points and entry parameters has a subsequence of normals; their limit in the continuous map \(X_s\) identifies the limiting parameter uniquely.

The set \(S\cap L_1\) is nonempty and compact. Its positive distance from the disjoint compact \(L_0\) puts its minimum entry parameter above zero. The given interior point puts that minimum below one. It is attained at some \(y\) and equals \(s_0\). Minimality excludes any point of \(S\) in \(\operatorname{int}L_{s_0}\). \(\square\)

For [the singular-support geometry lesson](geometry-of-singular-supports.md), take \(S=\operatorname{sing\,supp}u\cap L_1\). Its first contact is on a smooth boundary whose exact defining function is \(\tau-s_0\). Formula (13) says that the defining gradient is a positive scalar multiple of the outward normal. If the support inequalities established there exclude every bad normal at that contact, the one-barrier theorem applies with precisely this gradient. 

## Exercises with complete solutions

**Exercise 1 (basic: intervals).** Take \(L_0=[2,4]\), \(L_1=[-1,7]\). Find the best uniform constant \(a\) in (12), and both entry functions and their signed gradients.

**Solution.** The support differences at the normals \(-1,+1\) both equal three, so \(a=3\). The endpoints are \(2-3s\) and \(4+3s\). On the left shell, \(\tau=(2-x)/3\) and \(\tau'=-1/3\); on the right shell, \(\tau=(x-4)/3\) and \(\tau'=1/3\). These agree with the outward normals divided by the corresponding support differences.

**Exercise 2 (intermediate: moving translated balls).** Let \(L_i=c_i+\overline B(0,r_i)\), \(r_i>0\), and assume \(r_1-r_0>|c_1-c_0|\). Compute the interpolated boundary, a strict nesting margin, and the gradient of its entry function.

**Solution.** The support functions are \(h_i(\nu)=c_i\cdot\nu+r_i\), so \(X_i=c_i+r_i\nu\). Hence \(L_s=c_s+\overline B(0,r_s)\), with affine \(c_s,r_s\), and its boundary is \(X_s=c_s+r_s\nu\). Its spherical support-curvature matrix is \(r_sI>0\); the linear support part from the translated center has zero contribution to that matrix. The minimum support difference is
\(a=r_1-r_0-|c_1-c_0|>0\).
At \(x=c_s+r_s\nu\),
\[
\nabla\tau(x)=
\frac{\nu}{r_1-r_0+(c_1-c_0)\cdot\nu}.
\tag{18}
\]
The denominator stays at least \(a\), so the moving center does not destroy strict nesting. The case of a translated ball with negative support value in some direction also works; positivity is required of curvature and normal velocity, not of each support value.

## References

- Lars Hörmander, “On the singularities of solutions of partial differential equations with constant coefficients,” *Séminaire Goulaouic–Schwartz*, 1971–1972, exposé 25, 1–6. [Seminar paper](https://www.numdam.org/item/SEDP_1971-1972____A25_0/).
- Thomas Kalmes, “Surjectivity of differential operators and linear topological invariants for spaces of zero solutions,” *Revista Matemática Complutense* 32 (2019), 37–55. [Preprint](https://arxiv.org/abs/1408.4356).
