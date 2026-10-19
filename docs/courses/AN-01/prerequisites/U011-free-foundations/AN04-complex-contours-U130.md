# Gaussian reduction near a complex critical graph

The arguments below are Sections 2–7 of the AN-04 reading *Uniform complex stationary phase from exact critical-ideal division*. They prove a local Gaussian reduction from the following hypotheses. The variables \(x\in\mathbb R^d\) and the real parameters \(p\) range on fixed small neighborhoods. The smooth phase satisfies
\[
 \operatorname{Im}f\ge0,\qquad f_x(0,0)=0,\qquad
 \operatorname{Im}f(0,0)=0,\qquad \det f_{xx}(0,0)\ne0.
 \tag{P1}
\]
Suppose a smooth complex graph \(T\), with \(T(0)=0\), and a smooth parameter-only \(f_0\) satisfy
\[
 I=(f_{x_1},\ldots,f_{x_d})=(x-T(p)),\qquad
 f-f_0\in I^2,\qquad
 \operatorname{Im}f_0\ge c|\operatorname{Im}T|^2.
 \tag{P2}
\]
The change between these two generator systems is invertible on the patch. The amplitude \(b(x,p,\lambda)\) is smooth, supported in a fixed compact \(x\) patch, and bounded with every mixed derivative. The auxiliary parameter \(\lambda\) may range in a noncompact set. The frequency \(t\ge1\) is independent of it.

The exact division and positive-value hypotheses (P2) are established in Proposition 1 of [Virtual critical points and explicit coefficients](../../src/virtual-critical-points-and-explicit-coefficients.md). [Smooth complex equations and flat remainders](../../src/smooth-complex-equations-and-flat-remainders.md), Theorems 1–6 and I9–I11, supplies graph division, flatness and almost-analytic extensions. [The real inverse theorem](implicit-maps-U070.md), §§16.4–16.5, applies to the actual real coordinate maps.

All references to foundations A1–A4 below mean the complete supplied reading [Contour calculus and the Gaussian branch](AN04-contour-calculus-U130.md). Its A2 identity is proved directly from determinant differentiation and the fundamental theorem of calculus. The Gaussian expansion can also be obtained from [Finite stationary jets and quadratic exchange](../../src/finite-stationary-jets-and-quadratic-exchange.md), Theorem 1. The scalar and integration foundations linked by those readings supply compact cutoffs, Taylor remainders and differentiation under the integral.

Programme exposition by the AN-04 course contributors; supporting contour and Gaussian proofs by GPT-6 Astra (OpenAI), October 2026. CC0 1.0 Universal for the original expression. Earlier programme proofs retain their own attribution and licences.

## 2. A complete nonstationary proof

Let K be a fixed compact integration patch, f a bounded smooth phase family with \(\operatorname{Im}f\ge0\), and

\[
 |d_xf|^2+\operatorname{Im}f\ge c>0\quad\hbox{on }K.
 \tag{N1}
\]

Choose a scalar smooth cutoff \(\chi\), zero below \(c/4\) and one above \(c/2\). Split b into \(\chi(\operatorname{Im}f)b\) and \((1-\chi(\operatorname{Im}f))b\). On the first support \(\operatorname{Im}f\ge c/4\), so its integral is bounded by the compact-volume constant times \(e^{-tc/4}\) times the amplitude supremum. Parameter derivatives produce only finitely many powers of t and remain rapid.

On the second support \(|d_xf|^2\ge c/2\). There use

\[
 V=\sum_j\frac{\overline{f_{x_j}}}{|d_xf|^2}\partial_{x_j},
 \qquad (it)^{-1}V(e^{itf})=e^{itf}.
 \tag{N2}
\]

After k integrations by parts,

\[
 \int e^{itf}(1-\chi(\operatorname{Im}f))b\,dx
 =(it)^{-k}\int e^{itf}(V^*)^k
             [(1-\chi(\operatorname{Im}f))b]\,dx.
 \tag{N3}
\]

All denominators are bounded below uniformly. Derivatives of V and of the splitting cutoff use finitely many bounded phase derivatives, the lower bound c, and finitely many amplitude derivatives. Since \(|e^{itf}|\le1\), the last integral is uniformly bounded. This proves \(O(t^{-k})\) for every k. There are no boundary terms because the amplitudes are compactly supported. Choose k larger after differentiating a parameter. The estimate includes the imaginary-value alternative without an imaginary-Hessian definiteness hypothesis.

## 3. Exact quadratic factorization before complexifying

Set \(\phi=-if\), \(\phi_0=-if_0\), and \(Y=\operatorname{Im}T\). Then \(\operatorname{Re}\phi\ge0\) and \(\operatorname{Re}\phi_0\ge c|Y|^2\). From the exact membership in (P2), choose a symmetric smooth matrix \(Q(x,p)\) with

\[
 \phi(x,p)=\phi_0(p)+\tfrac12(x-T(p))^tQ(x,p)(x-T(p)).
 \tag{Q1}
\]

Symmetrizing the ideal-square coefficients does not change the scalar expression. At the mark \(Q(0,0)=\phi_{xx}(0,0)\), so it is invertible there. Shrink once so all matrices used below stay in its invertibility patch. This is a critical-ideal identity; it does not assert that a smooth phase is holomorphic.

The generator-change matrix is also invertible on that patch. Consequently

\[
 c_1|x-T(p)|\le |\phi_x(x,p)|\le C_1|x-T(p)|
 \quad(x\hbox{ real}).
 \tag{Q2}
\]

Construct an almost-analytic extension of Q in x, denoted \(\widetilde Q(z,p)\), and an almost-analytic extension \(B(z,p,\lambda)\) of b, on a fixed complex neighborhood. The almost-analytic construction in [Smooth complex equations and flat remainders](../../src/smooth-complex-equations-and-flat-remainders.md), I9–I11, gives, for every M and every fixed mixed derivative,

\[
 |\partial_{\bar z}\widetilde Q|+|\partial_{\bar z}B|
 \le C_M|\operatorname{Im}z|^M.
 \tag{Q3}
\]

The constants are uniform in \(\lambda\); parameter derivatives are included. Extend the amplitude with compact real-direction support inside a larger fixed integration domain. Define a specially chosen extension of the phase by

\[
 \Phi(z,p)=\phi_0(p)+\tfrac12(z-T(p))^t
                     \widetilde Q(z,p)(z-T(p)).
 \tag{Q4}
\]

It equals phi on real z. It is almost analytic there because its only antiholomorphic derivatives come from \(\widetilde Q\). At the virtual point it has the exact identities

\[
 \Phi(T,p)=\phi_0(p),\quad \Phi_z(T,p)=0,\quad
 \Phi_{zz}(T,p)=\widetilde Q(T,p),\quad
 \Phi_{z\bar z}(T,p)=\Phi_{\bar z\bar z}(T,p)=0.
 \tag{Q5}
\]

These properties are constructed for an extension and a critical-ideal representative. They require no genuine complex critical point for the original real-domain smooth f.

Let \(Q^\ast\)=\(Q(0,0)\). Foundation A1 proves that one can choose an invertible constant complex matrix S with \(S^tS=Q^\ast\). Put

\[
 K(z,p)=S^{-t}\widetilde Q(z,p)S^{-1},\qquad
 q(z,p)=K(z,p)^{1/2}S(z-T(p)).
 \tag{Q6}
\]

K is a small symmetric perturbation of I. Its square root is defined by the convergent matrix power series near I; foundation A1 proves convergence, the square identity, symmetry, invertibility and all parameter derivative bounds, including noncommuting matrix increments. Thus, exactly,

\[
 \Phi=\phi_0+\tfrac12q^tq.
 \tag{Q7}
\]

The real inverse function theorem on \(\mathbb C^d=\mathbb R^{2d}\) makes q a smooth real diffeomorphism on one common patch. At T its antiholomorphic derivative is zero: differentiating the matrix factor with respect to \(\bar z\) retains the factor \(z-T\). Hence \(q_z(T)\) is a complex invertible matrix and

\[
 q_z(T)^tq_z(T)=\widetilde Q(T,p).
 \tag{Q8}
\]

This exact square factorization follows from the ideal-square identity (Q1), which is assumed in (P2). Matrix square roots near I do not select the Gaussian determinant branch by themselves; orientation is fixed in Section 7 below.

## 4. First contour: obtain damping without strict imaginary Hessian

For \(0\le s\le1\) and one fixed sufficiently small \(\delta>0\) define

\[
 Z_s(x,p)=x+s\delta\,\overline{\phi_x(x,p)}.
 \tag{C1}
\]

At real x, \(\Phi_z=\phi_x\) and \(\Phi_{\bar z}=0\). Taylor's theorem with bounded second derivatives gives

\[
 \Phi(Z_s,p)=\phi(x,p)+s\delta|\phi_x|^2
       +O(s^2\delta^2|\phi_x|^2).
\]

Choose delta to make the error at most \((s\delta/2)|\phi_x|^2\). Then

\[
 \operatorname{Re}\Phi(Z_s,p)
 \ge \operatorname{Re}\phi(x,p)
           +(s\delta/2)|\phi_x(x,p)|^2\ge0,
 \qquad
 |\operatorname{Im}Z_s|\le s\delta|\phi_x|.
 \tag{C2}
\]

In particular \(\operatorname{Re}\Phi(Z_s)\ge c|\operatorname{Im}Z_s|^2\), uniformly also as s tends to zero. At \(s=1\), (Q2) strengthens this to

\[
 \operatorname{Re}\Phi(Z_1,p)
       \ge c_2(|x-\operatorname{Re}T|^2+|Y|^2).
 \tag{C3}
\]

For small delta these are embedded contours, since their real Jacobians are uniformly close to those of \(x\mapsto x\). Use the exact determinant identity (A4) in foundation A2, integrated by the fundamental theorem of calculus. This proves the needed Stokes formula, including its orientation and boundary terms, for the complex d-form \(e^{-t\Phi}B\,dz_1\wedge\cdots\wedge dz_d\) over the homotopy. Its exterior derivative is

\[
 e^{-t\Phi}(\bar\partial B-tB\bar\partial\Phi)
                 \wedge dz_1\wedge\cdots\wedge dz_d.
 \tag{C4}
\]

The holomorphic differential terms vanish when wedged with all \(dz_j\). Each antiholomorphic defect is bounded by every power of \(|\operatorname{Im}Z_s|\). All homotopy Jacobians and its integration volume are bounded. For any M,

\[
 (1+t)|v|^M e^{-ct|v|^2}
       \le C_M(1+t)t^{-M/2}.
 \tag{C5}
\]

Taking M arbitrarily large makes the Stokes error absolutely \(O(t^{-A})\) for every A. Lateral boundary terms vanish by the enlarged compact support chosen in Section 3. Differentiating a fixed number of parameters adds finitely many factors of t; increasing M absorbs them. Therefore the original real integral equals its integral over \(Z_1\), modulo an absolutely rapid error with rapid mixed derivatives.

Only (Q2), nonnegativity of \(\operatorname{Im}f\) on the real patch, and Hessian invertibility were used. No strictly positive imaginary Hessian has been introduced.

## 5. Second contour: pass through the virtual point

Transfer \(Z_1\) into q coordinates. At the marked parameter it passes through \(q=0\) and obeys

\[
 \operatorname{Re}(q^tq/2)\ge c|q|^2.
\]

This inequality also holds on its tangent plane at 0. Writing \(q=u+iv\), projection to u is an isomorphism on that real d-plane: a nonzero vector with \(u=0\) would give \(\operatorname{Re}(q^tq)=-|v|^2<0\). The inverse function theorem therefore writes a neighborhood of the contour, uniformly for small p, as

\[
 q=u+i h(u,p),\qquad u\in W\subset\mathbb R^d,
 \tag{C6}
\]

with one fixed small W. Moreover \(h(0,p)=O(|Y|)\), and \(|h(u,p)|\le C(|u|+|Y|)\). To see the first bound, insert \(x=\operatorname{Re}T\) into \(Z_1\); (Q2) puts that point \(O(|Y|)\) from T, and hence its q coordinates \(O(|Y|)\) from zero. The uniformly invertible u projection moves x only \(O(|Y|)\) to reach \(u=0\).

For \(0\le s\le1\) let

\[
 G_s(u,p)=q(\cdot,p)^{-1}(u+i s h(u,p)).
 \tag{C7}
\]

The \(s=1\) contour is the first deformed contour, and \(s=0\) passes through T. Its exact phase real part is

\[
 \operatorname{Re}\Phi(G_s,p)
 =\operatorname{Re}\phi_0+(|u|^2-s^2|h|^2)/2
 =(1-s^2)(\operatorname{Re}\phi_0+|u|^2/2)
      +s^2\operatorname{Re}\Phi(G_1,p).
 \tag{C8}
\]

The first term's endpoint is at least \(c|Y|^2+|u|^2/2\) by (P2). The other endpoint is at least \(c'(|u|^2+|Y|^2)\) by (C3), since \(|q(Z_1)|\le C|x-T|\). Thus the convex combination gives

\[
 \operatorname{Re}\Phi(G_s,p)\ge c_3(|u|^2+|Y|^2).
 \tag{C9}
\]

Also \(|\operatorname{Im}G_s|\le C(|u|+|Y|)\), by the bounded inverse derivative of q, \(q(T)=0\), and the estimate on h. In (C4), the antiholomorphic defects are therefore bounded by arbitrary powers of \((|u|^2+|Y|^2)^{1/2}\), while (C9) supplies the corresponding Gaussian decay. The same proved identity (A4) gives another absolutely rapid error. Choose a fixed cutoff in u equal to one near zero. Its transition and the lateral homotopy boundary have \(|u|\) bounded below, so their contributions are exponentially small, with every fixed parameter derivative. Hence the integral becomes

\[
 e^{itf_0(p)}\int_{\mathbb R^d}e^{-t|u|^2/2}
                    H(u,p,\lambda)\,du+O(t^{-\infty}),
 \tag{C10}
\]

where H is the smoothly cut off pullback amplitude

\[
 H=B(G_0(u,p),p,\lambda)
               \det\bigl(\partial_uG_0(u,p)\bigr).
 \tag{C11}
\]

It has all mixed derivatives bounded uniformly. The determinant is the complex Jacobian of the pulled back top form along real u. It is not an absolute determinant.

## 6. Gaussian expansion and residue operators

Taylor-expand H through degree \(2L-1\) at \(u=0\). Odd monomials integrate to zero, and even Gaussian moments give

\[
 \int e^{-t|u|^2/2}H(u)\,du
 =(2\pi/t)^{d/2}
   \sum_{j=0}^{L-1}\frac{t^{-j}}{2^j j!}(\Delta_u^jH)(0)
      +O(t^{-L-d/2}).
 \tag{G1}
\]

The Taylor remainder is bounded by \(C|u|^{2L}\) times a finite \(C^{2L}\) seminorm. Rescaling \(u=t^{-1/2}v\) gives its stated integral bound. Parts outside the fixed Taylor neighborhood are exponentially small. Because \(|e^{itf_0}|\le1\), multiplication by the prefactor preserves the absolute remainder estimate. Combining this with the two rapid contour errors gives an absolute remainder of order \(t^{-L-d/2}\) for the original integral.

The full inverse-jet induction and residue algebra in foundation A4 justify the chain rule in (C11), which shows that \((\Delta_u^jH)(0)\) uses amplitude derivatives of order at most \(2j\), with smooth bounded phase coefficients. At \(u=0\), \(G_0=T\). Holomorphic jets of almost-analytic extensions of the real amplitude derivatives give their smooth critical-ideal residues. Terms containing antiholomorphic jets are flat in \(|Y|\). They disappear from the expansion modulo absolutely rapid expressions, since

\[
 |Y|^M e^{-t\operatorname{Im}f_0}
       \le C_Mt^{-M/2}.
 \tag{G2}
\]

The same remains true after each fixed parameter or \(\lambda\) derivative. Thus the operators can be expressed through residues of differentiated original amplitudes. Their phase patch and cutoffs never depend on j, L, or the amplitude.

At \(u=0\), \(q_{\bar z}(T)=0\), so \(\partial_uG_0(0)=q_z(T)^{-1}\). Therefore

\[
 C_0b=B(T,p,\lambda)\det(q_z(T,p))^{-1}.
 \tag{G3}
\]

From (Q8), its determinant factor squares to \(\det(\widetilde Q(T,p))^{-1}\). On real x, differentiating (Q1) twice shows \(\phi_{xx}-Q\) is in \((x-T)\). Thus \(\widetilde Q(T)\) is a residue of \(\phi_{xx}=f_{xx}/i\). Together with the residue of \(B(T)\), this gives the leading Gaussian factor once orientation is fixed.

## 7. Gaussian branch, with null damping directions allowed

For a complex symmetric invertible A with \(\operatorname{Im}A\ge0\), regularize its Gaussian by

\[
 \int_{\mathbb R^d}e^{i x^tAx/2-\epsilon|x|^2/2}\,dx
 =(2\pi)^{d/2}\det(\epsilon I-iA)^{-1/2},\qquad\epsilon>0.
 \tag{B1}
\]

The root on the right is determined by continuation from positive real symmetric Gaussian matrices. Foundation A3 proves this identity directly. Gaussian integration by parts gives its full second-moment matrix; differentiation along a matrix path and the cofactor determinant identity give a scalar differential equation for the integral. Its solution fixes one continuous inverse root from the positive real Gaussian, without importing an analytic-continuation theorem. The limit \(\epsilon\) down to zero is the regularized Fresnel value. Invertibility of A makes its determinant nonzero at the endpoint.

Equivalently, start at I and continue the inverse root along

\[
 M_s=(1-s)A/i+sI,\qquad 0\le s\le1.
 \tag{B2}
\]

For \(0<s\le1\) its real part is positive definite, and \(M_0\) is invertible. The path cannot meet determinant zero. It fixes the Gaussian value even when \(\operatorname{Im}A\) has null directions. Choose the local contour orientation and q coordinate orientation to agree with this elementary quadratic computation at the mark, then continue on the small invertibility patch. This fixes \(\det(q_z)^{-1}\) and the leading coefficient. A scalar principal square root of \(\det(A/i)\) alone is insufficient.
