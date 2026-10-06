# The scalar subprincipal symbol on half densities

This companion retains the calculation in Section 3, equations G11–G14, of AN03-U012, *Detecting regularity without choosing coordinates*, in *Elliptic Operators & Boundary Problems: Renewed 2026 Course Draft*. The equations and index calculation are unchanged. Its two references to the general coordinate expansion now point to the explicitly proved first-correction formula (SC2), and its multiplication formula points to the exact existing programme proof. Section S1 below supplies the required coordinate correction with every differentiated remainder.

Original principal author and publisher: AN-03 course-writing task / AN-03 local course project. Copyright © 2026 AN-03 course project contributors. Earlier modification: AN-03 course-writing task and OpenAI Codex. Selection, prerequisite bindings and Section S1: GPT-6 Astra (OpenAI), Ultra, 5 October 2026; publisher: AN-04 local course project.

Permission is granted to copy, distribute and modify this component under the GNU Free Documentation License, Version 1.2 only, with no Invariant Sections, no Front-Cover Texts and no Back-Cover Texts. The [licence](notices/COPYING), [title page](notices/TITLE_PAGE.md), [history](notices/HISTORY.md) and [rights notice](notices/RIGHTS.md) accompany it. The combined component retains that licence.

The exact earlier proofs are [coordinate transport T1–T2](../20261004-free-intrinsic-graph/prerequisites/coordinate-and-wavefront-localization.md), [amplitude reduction O4 and composition O3](../20261004-free-intrinsic-graph/prerequisites/ordinary-operator-calculus.md), [finite calculus and inverses](../20261004-free-stationary-phase/prerequisite-completions.md), [determinants and finite algebra, P9.1–P9.5](../20261004-free-stationary-phase/differential-prerequisite-completions.md), and [positive powers and complex exponentials, P14–P15](../20261004-free-stationary-phase/exponential-prerequisite-completions.md). The [proof map](proof-map.json) gives each exact provider. All symbol estimates here are ordinary \(S_{1,0}\) estimates on compact base sets.

## S1. The first coordinate correction with its full remainder

Write the old and new coordinates as \(x\) and \(z=\kappa(x)\). Put \(M_{kj}=\partial_{x_j}\kappa_k\), \(N=M^{-1}\), \(J=|\det M|\), and \(\xi=M^T\eta\). For the second base variable use \(y\), \(w=\kappa(y)\). The proved coordinate transport T1 gives
\[
 L(x,y)=\int_0^1D\kappa(y+t(x-y))\,dt,\qquad
 c(z,w,\eta)=a(x,L(x,y)^T\eta)\frac{|\det L(x,y)|}{J(y)}.
 \tag{SC1}
\]
Compact cutoffs, equal to one near the diagonal under examination, are understood. Their derivatives vanish at that diagonal; separated pieces have smooth kernels. T1 proves that \(L,L^{-1}\), the determinant factors and all their derivatives are bounded after this localization, and that every base derivative of the frequency-linear argument has net order zero. Its amplitude therefore has ordinary order \(m\), with a loss of one for each frequency derivative. The amplitude reduction O4 at \(N=2\) gives \(a_\kappa=c|_{w=z}-i\sum_k\partial_{\eta_k}\partial_{w_k}c|_{w=z}\) modulo \(S^{m-2}\), with every derivative estimate.

Here is the complete derivative at that diagonal. With \(\ell\) an old-coordinate index,
\[
 \partial_{y_\ell}L_{kj}|_{y=x}
       =\tfrac12\partial_{x_\ell}M_{kj},\qquad
 \partial_{y_\ell}\log\frac{|\det L|}{J(y)}\bigg|_{y=x}
       =-\tfrac12\partial_{x_\ell}\log J,\qquad
 \partial_{w_k}|_{w=z}=\sum_\ell N_{\ell k}\partial_{y_\ell}.
 \tag{SC1a}
\]
The first identity integrates \(1-t\). The second is the determinant derivative, since \(L=M\) there. One can verify that derivative directly by multilinearity: differentiating one determinant column at a time gives \(\partial\det M=(\det M)\operatorname{tr}(M^{-1}\partial M)\). The sign of \(\det M\) is locally constant, so the logarithmic derivative is also that of \(J\).

In \(\sum_k\partial_{\eta_k}\partial_{w_k}c\), the derivatives of \(a\) of frequency order two give
\(\frac12\sum_{\ell,j,h}a_{\xi_\ell\xi_j}\eta_h\partial_{x_\ell}M_{hj}\), because \(\sum_kN_{\ell k}M_{ki}=\delta_{\ell i}\). The remaining terms are
\[
 \frac12\sum_{k,\ell,j}N_{\ell k}(\partial_{x_\ell}M_{kj})a_{\xi_j}
 -\frac12\sum_\ell(\partial_{x_\ell}\log J)a_{\xi_\ell}=0.
 \tag{SC1b}
\]
Indeed mixed derivatives give \(\partial_{x_\ell}M_{kj}=\partial_{x_j}M_{k\ell}\), and the determinant identity identifies the first sum's coefficient with \(\partial_{x_j}\log J\). Consequently
\[
 a_\kappa(\kappa(x),\eta)=a(x,M^T\eta)
 -\frac i2\sum_{i,j,k}
   a_{\xi_i\xi_j}(x,M^T\eta)\eta_k\partial_{x_i}\partial_{x_j}\kappa_k
 \pmod {S^{m-2}}.
 \tag{SC2}
\]
This conclusion holds for a general ordinary symbol. Its correction has order \(m-1\). Every discarded term has the stated differentiated \(S^{m-2}\) bound by O4, and T1 supplies those bounds uniformly on the fixed compact coordinate sets. For a classical symbol \(a=p+r\) modulo \(S^{m-2}\), use \(p\) in the correction: two derivatives of \(r\), followed by the one frequency factor, have order \(m-2\). Thus both the leading and next homogeneous terms transform by the displayed rule. This is precisely the part of the coordinate expansion required below; no assertion about a higher expansion is needed.

## 3. The second symbol term and the density it measures

Equation (SC2) first gives
\(a_\kappa(\kappa(x),\eta)-a(x,\kappa'(x)^T\eta)\in S^{m-1}\).
Suppose that \(a\sim a_m+a_{m-1}+\cdots\) is classical with step one. Define
\[
s(a)=a_{m-1}+\frac{i}{2}\sum_j\partial_{x_j}\partial_{\xi_j}a_m.
\tag{G11}
\]
For operators on functions, this is generally not a scalar on the cotangent bundle. If \(J=|\det\kappa'|\), then
\[
s(a_\kappa)(\kappa(x),\eta)
=s(a)(x,\kappa'(x)^T\eta)
-\frac12\sum_j(\partial_{\xi_j}a_m)(x,\kappa'(x)^T\eta)
\frac{D_{x_j}J}{J}.
\tag{G12}
\]
Here is an index verification of the correction. Write \(M_{kj}=\partial_j\kappa_k\), \(N=M^{-1}\), and \(\xi=M^T\eta\). The order-\(m-1\) term added by (SC2) is
\(-\frac i2\sum_{j,l,k}(\partial_{\xi_j}\partial_{\xi_l}a_m)\,\eta_k\partial_j\partial_l\kappa_k\).
In \(\sum_k\partial_{z_k}\partial_{\eta_k}[a_m(x,M^T\eta)]\), the chain rule produces \(\sum_j\partial_{x_j}\partial_{\xi_j}a_m\), the same Hessian term with coefficient \(+1\), and
\(\sum_{j,k,l}N_{lk}(\partial_lM_{kj})\partial_{\xi_j}a_m\).
The Hessian terms cancel after multiplication by \(i/2\). Since mixed derivatives commute,
\(\sum_{k,l}N_{lk}\partial_lM_{kj}=\sum_{k,l}N_{lk}\partial_jM_{kl}=\partial_j\log J\),
by the determinant derivative formula. The remainder is \((i/2)\sum_j\partial_{\xi_j}a_m\,\partial_j\log J\), which is (G12). Orientation reversal changes the sign of \(\det M\) only by a locally constant factor, so its logarithmic derivative is that of \(J\).

The density line bundle \(\Omega\) has local generator \(|dx|\). For any \(z\in\mathbb C\), define \(\Omega^z\) using positive Jacobians raised to \(z\): \(t^z=e^{z\log t}\) for \(t>0\). The real logarithm makes \((t_1t_2)^z=t_1^zt_2^z\), proving the cocycle relation, including complex exponents. Components transform by
\(u_\kappa(\kappa(x))=J(x)^{-z}u(x)\).
Thus an operator on \(z\)-densities is transported as the function operator conjugated in the old coordinates by \(J^{-z}AJ^z\). Its symbol differs from \(a\), modulo \(S^{m-2}\), by
\[
z\sum_j\partial_{\xi_j}a\,\frac{D_jJ}{J}.
\tag{G13}
\]
Indeed Section O3 of [Ordinary symbols, composition and proper localization](../20261004-free-intrinsic-graph/prerequisites/ordinary-operator-calculus.md) applied to multiplication by \(J^z\) gives \(J^{-z}(aJ^z+\sum_j\partial_{\xi_j}a D_jJ^z)\) through the first correction; all higher frequency derivatives have order at most \(m-2\). The identity \(D_jJ^z=zJ^zD_jJ/J\) proves (G13). At \(z=\frac12\) it cancels (G12).

There is a version without homogeneity. For scalar half-density operators, the local quantity
\[
\sigma_{[2]}(A)=a+\frac i2\sum_j\partial_{x_j}\partial_{\xi_j}a
\pmod {S^{m-2}}
\tag{G14}
\]
agrees on overlaps as a scalar symbol class on \(T^*X\). Repeat the preceding calculation with \(a\) in place of \(a_m\): omitted terms contain at least two net frequency losses, so they are of order \(m-2\). A partition of unity patches the local quantities to a global symbol, and any two patches differ by \(S^{m-2}\) because they agree in each chart modulo that space. Its homogeneous term of degree \(m-1\), when present, is (G11). Formula (G12) also shows invariance for function operators at double zeros of \(a_m\), and under transformations with locally constant Jacobian. The refined assertion (G14) is specifically for scalar half-densities; a varying vector-bundle frame introduces its own first-order correction.
