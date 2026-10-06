# Linear and affine connections

*Written by GPT-6.1 Sol (OpenAI), Ultra effort, October 2026. Self-checked by the writing AI. Original text and figure dedicated to the public domain under CC0 1.0.*

## 1. Differentiation and moving frames

Let \(E\to M\) be a smooth vector bundle of rank \(r\) over \(\mathbb F=\mathbb R\) or \(\mathbb C\). The base manifold is finite dimensional, Hausdorff and second countable. Vector fields on the base are real. Write \(\Gamma(E)\) for smooth sections.

A **covariant derivative** is an additive operation \(\nabla_Xs\in\Gamma(E)\), real linear in the vector field \(X\), \(\mathbb F\)-linear in \(s\), satisfying

\[
\begin{aligned}
\nabla_{fX}s&=f\nabla_Xs,\\
\nabla_X(hs)&=X(h)s+h\nabla_Xs.
\end{aligned}
\]

Here \(f\) is a real smooth function and \(h\) is an \(\mathbb F\)-valued smooth function. Thus \(X\mapsto\nabla_Xs\) is a section of \(T^*M\otimes_{\mathbb R}E\). We denote it by \(\nabla s\). For a complex bundle it is complex linear in the section; no complex structure on \(M\) is required.

The axioms imply locality. Suppose \(s=0\) on a neighbourhood of \(x\). Choose a smooth cutoff \(\chi\), equal to one near \(x\), whose support lies in that neighbourhood. Then \(\chi s=0\), and

\[
0=\nabla_X(\chi s)(x)=\nabla_Xs(x),
\]

since \(X(\chi)(x)=0\). If \(X=0\) near \(x\), the identity \(\nabla_{\chi X}s=\chi\nabla_Xs\) proves the same assertion for \(X\). Consequently the value of \(\nabla_Xs\) at \(x\) depends only on the germs of \(X\) and \(s\). A local section or field can be multiplied by a cutoff and extended by zero; the resulting definition of its derivative near \(x\) is independent of this extension. This justifies working with local frames from now on.

A frame \(e=(e_1,\ldots,e_r)\) over \(U\) is equivalently a smoothly varying isomorphism \(e_x:\mathbb F^r\to E_x\). Write a section as \(s=e v\), with \(v:U\to\mathbb F^r\). The columns \(\nabla e_j\) determine a matrix-valued one-form \(A\) by \(\nabla_Xe_j=e A(X)\mathbf e_j\). The axioms give

\[
\nabla(e v)=e(dv+A v). \tag{1.1}
\]

The matrix entries are smooth: use local coordinate fields to evaluate \(\nabla e_j\), and express the resulting smooth sections in the frame. Conversely, every smooth matrix-valued one-form in (1.1) defines a covariant derivative on \(U\times\mathbb F^r\).

**Theorem 1.1 (frame correspondence).** Covariant derivatives on \(E\) correspond bijectively to principal connections on its full frame bundle \(\operatorname{Fr}(E)\), with group \(\mathrm{GL}(r,\mathbb F)\). Their parallel transports agree under evaluation of a frame on a vector.

**Proof.** On an overlap change frame by \(e'=e a\), where \(a:U\cap U'\to\mathrm{GL}(r,\mathbb F)\). Applying (1.1) to \(e a v'\) and comparing with \(e'(dv'+A'v')\) gives

\[
A'=a^{-1}A a+a^{-1}da. \tag{1.2}
\]

This is exactly the principal-connection transformation rule proved in Section 2 of Connections and parallel transport. More explicitly, in the principal trivialization \(u=e_x g\) set

\[
\omega=g^{-1}A g+g^{-1}dg. \tag{1.3}
\]

It reproduces the generator of \(u\mapsto u\exp(tB)\) and transforms by \(\operatorname{Ad}(b^{-1})\) under a fixed right translation by \(b\). Equation (1.2) makes (1.3) agree in overlapping trivializations. It therefore defines a principal connection. Its potential in the section \(e\) is \(A\), so it is unique.

In the other direction take a principal connection, pull it back by each local frame \(e\), and use (1.1). Equation (1.2) proves that these local derivatives agree. The two constructions preserve each local potential, so they are inverse.

Along a piecewise \(C^1\) path \(\gamma\), define the derivative of a section \(V(t)=e_{\gamma(t)}v(t)\) along that path by

\[
\frac{D V}{dt}=e_{\gamma(t)}\bigl(v'(t)+A(\gamma'(t))v(t)\bigr).
\]

The chain rule and (1.2) make this frame independent. A horizontal frame \(u(t)=e_{\gamma(t)}g(t)\) satisfies \(g'=-A(\gamma')g\). Therefore \(V(t)=u(t)v_0\) has \(D V/dt=0\). Conversely uniqueness for that linear equation makes every parallel vector field of this form. Whole-interval existence and smooth dependence were proved for principal transport in the preceding lesson. □

Taking \(E=TM\) gives the correspondence between covariant derivatives of vector fields and **linear connections** on \(M\). In the coordinate frame \(\partial_j=\partial/\partial x^j\), define the Christoffel coefficients by

\[
\nabla_{\partial_i}\partial_j=\sum_k\Gamma^k_{ij}\partial_k.
\]

Then the \(kj\) entry of \(A\) is \(\sum_i\Gamma^k_{ij}dx^i\), and

\[
\nabla_XY=\sum_k\left(X(Y^k)+\sum_{i,j}\Gamma^k_{ij}X^iY^j\right)\partial_k.
\]

These coefficients need not be symmetric in \(i,j\). On \(\mathbb R^n\), setting them all to zero gives \(\nabla_XY=D_XY\) and constant-coordinate parallel transport. A moving frame can have a nonzero potential for this same connection: (1.2) then gives \(A'=a^{-1}da\).

**Proposition 1.2 (difference of derivatives).** The difference of two covariant derivatives is a one-form with values in \(\operatorname{End}_{\mathbb F}(E)\). Conversely adding any such one-form to a covariant derivative gives another one.

**Proof.** If \(S_Xs=\nabla'_Xs-\nabla_Xs\), the terms \(X(h)s\) cancel, so \(S_X(hs)=hS_Xs\). It is also linear over real smooth functions in \(X\). In a local frame it is multiplication by \(A'-A\); thus it depends only on \(X(x)\) and \(s(x)\) and has smooth coefficients. The converse follows by substitution into the two derivative axioms. □

## 2. Tensors and metrics

A connection on \(E\) determines one on its dual by the requirement that differentiation commute with evaluation:

\[
(\nabla_X\lambda)(s)=X\bigl(\lambda(s)\bigr)-\lambda(\nabla_Xs).
\tag{2.1}
\]

The right side is linear over smooth functions in \(s\), so it defines a dual section. In the dual frame its column-coordinate potential is \(-A^T\). For bundles \(E,F\) over the same field, define a connection on their tensor product by

\[
\begin{gathered}
\nabla_X(s\otimes t)\\
=\nabla_Xs\otimes t+s\otimes\nabla_Xt.
\end{gathered}
\tag{2.2}
\]

This respects the relation \((hs)\otimes t=s\otimes(ht)\): each side gives the same additional term \(X(h)s\otimes t\). In local tensor frames extend by the derivative rule to general sections. Equations (2.1)–(2.2) then agree under every change of frame, and so define a global connection. They also prove uniqueness because local tensor frames span every fibre.

Repeated tensor products give derivatives of all tensor fields. Permuting factors commutes with differentiation by (2.2); contracting a dual and a vector factor commutes by (2.1). Symmetric and alternating tensors consequently remain symmetric and alternating under differentiation. For example, a covariant two-tensor \(h\) on a real bundle satisfies

\[
\begin{gathered}
(\nabla_Xh)(s,t)=X\bigl(h(s,t)\bigr)\\
-h(\nabla_Xs,t)-h(s,\nabla_Xt).
\end{gathered}
\tag{2.3}
\]

For a Hermitian metric the same formula applies, with antilinearity in the first argument. The base field \(X\) remains real. On \(TM\), applying this construction to a tensor \(K\) gives a tensor \(\nabla K\) with one additional covariant slot, since it is linear over smooth functions in \(X\).

**Theorem 2.1 (metric compatibility).** Every smooth real vector bundle admits a positive definite fibre metric, and every smooth complex vector bundle admits a positive definite Hermitian fibre metric. For each such metric \(h\), there is a covariant derivative satisfying \(\nabla h=0\). This condition is equivalent to preservation of \(h\) by parallel transport.

**Proof.** Give each local trivialization its Euclidean or Hermitian metric and sum these metrics using a subordinate locally finite smooth partition of unity. Each summand, extended by zero with its weight, is smooth; their sum is positive definite because at each point some weight is positive.

Choose any covariant derivative \(\nabla^0\), whose existence follows from the connection existence theorem on \(\operatorname{Fr}(E)\) and Theorem 1.1. Put \(B_X=\nabla^0_Xh\), a symmetric or Hermitian form on each fibre. Define \(K_X\in\operatorname{End}(E)\) uniquely by

\[
h(s,K_Xt)=\tfrac12 B_X(s,t).
\]

In a local frame the Gram matrix \(H\) is invertible and \(K_X=\tfrac12H^{-1}B_X\); hence this is a smooth endomorphism-valued one-form. The symmetry of \(B_X\) makes \(K_X\) self-adjoint for \(h\). With \(\nabla=\nabla^0+K\), equation (2.3) yields

\[
\begin{aligned}
(\nabla_Xh)(s,t)&=B_X(s,t)-h(K_Xs,t)\\
&\quad-h(s,K_Xt)=0.
\end{aligned}
\]

Along a path, the product rule gives

\[
\begin{aligned}
\frac{d}{dt}h(V,W)&=(\nabla_{\gamma'}h)(V,W)\\
&\quad+h(D_tV,W)+h(V,D_tW).
\end{aligned}
\]

If \(\nabla h=0\), the metric pairing of parallel fields is constant. Conversely, suppose transport preserves \(h\). For arbitrary initial vectors choose their parallel extensions along any path through a point. The displayed equation at that point shows \((\nabla_Xh)(s,t)=0\) for every velocity \(X\) and every pair of vectors. □

The theorem concerns the **full frame bundle**. A prescribed smaller structure group can prevent metric compatibility. For example, over \(\mathbb R\) take the principal bundle with group \(\{1\}\), its associated line with constant coordinate, and the metric \(h_x(v,w)=e^{2x}vw\). The only connection for that principal group transports coordinates constantly. It does not preserve \(h\). Its prescribed frame has unit length only at \(x=0\), so its unit frames do not form a reduction over the base. A metric reduction within a prescribed group requires local frames in that group which actually make the metric standard. Once such a reduction exists, the parallel-reduction criterion in Section 2 of Reduction and the holonomy theorem applies.

