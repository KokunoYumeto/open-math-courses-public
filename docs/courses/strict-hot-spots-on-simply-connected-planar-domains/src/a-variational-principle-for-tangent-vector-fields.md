# A variational principle for tangent vector fields

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The gradient of a Neumann eigenfunction is a vector field tangent to the boundary. Rohleder discovered that these gradients are exactly the minimizers of a variational problem for tangent vector fields, with the same minimum value \(\mu\) [Roh21, Theorem 1.1]. This lesson proves that principle on our class of domains, with its equality case, and an identity that rewrites the divergence–curl energy as a Dirichlet energy plus a boundary curvature term. The next lesson transfers this energy to the boundary circle.

- The vector variational principle (Section 1).
- The curvature identity (Section 2).

Notation is that of [Neumann eigenfunctions and the hot-spots problem](neumann-eigenfunctions-and-the-hot-spots-problem.md). In particular \(\Omega\) is simply connected, \(\mu<\lambda_D\) (Proposition 4.1 there), and Green's formulas (2.1)–(2.2) and the Poincaré inequalities of Lemma 2.3 there are available.

## 1. The vector variational principle

A vector field \(X\in H^1(\Omega;\mathbb R^2)\) is *tangent* if \(\operatorname{tr}X\cdot\nu=0\) almost everywhere on \(\partial\Omega\). For such fields put
\[
\begin{gathered}
\mathcal Q(X)=\int_\Omega\bigl(|\operatorname{div}X|^2+|\operatorname{curl}X|^2\bigr),\\
\operatorname{curl}X=\partial_1X_2-\partial_2X_1,
\end{gathered}
\]
and write \(\nabla^\perp j=(-\partial_2j,\partial_1j)\) for a scalar \(j\).

**Proposition 1.1** (Rohleder's principle; [OpenAI-HS, Proposition 3.1]). For every tangent \(X\in H^1(\Omega;\mathbb R^2)\),
\[
\mathcal Q(X)\ge\mu\int_\Omega|X|^2, \tag{1.1}
\]
with equality if and only if \(X=\nabla v\) for some \(v\in V\).

*Proof.* *Step 1: a Neumann potential.* By Lemma 2.3(2) of the first lesson, \(\int\nabla v\cdot\nabla\phi\) is an inner product on the mean-zero subspace of \(H^1(\Omega)\), equivalent to the \(H^1\) inner product. The Riesz–Fréchet theorem gives a mean-zero \(v\in H^1(\Omega)\) with \(\int\nabla v\cdot\nabla\phi=-\int(\operatorname{div}X)\phi\) for mean-zero \(\phi\). For \(\phi=1\) both sides vanish, the right side because Green's formula (2.1) of the first lesson and the tangent condition give \(\int\operatorname{div}X=\int_{\partial\Omega}\operatorname{tr}X\cdot\nu\,ds=0\). So the identity holds for all \(\phi\in H^1(\Omega)\). By (ER N) with \(k=0\), \(v\in H^2(\Omega)\), and as in the proof of Proposition 3.1(3) of the first lesson, \(\Delta v=\operatorname{div}X\) almost everywhere and \(\partial_\nu v=0\).

*Step 2: a Dirichlet potential.* By (B10) and (B29) of [Boundary energy, local inverses, and harmonic data](course:elliptic-operators-and-boundary-problems/second-order-boundary), there is \(j\in H^1_0(\Omega)\cap H^2(\Omega)\) with \(\Delta j=\operatorname{curl}X\) almost everywhere.

*Step 3: \(\nabla^\perp j\) is tangent.* For \(F\in C^2(\overline\Omega)\), \(\nabla^\perp F\cdot\nu=-\nabla F\cdot\tau=-\partial_\tau F\), and (SOB 1) applied to the divergence-free field \(\nabla^\perp F\) gives \(\int_{\partial\Omega}\partial_\tau F\,ds=0\). Let \(j_n\in C^\infty(\overline\Omega)\) converge to \(j\) in \(H^2(\Omega)\) (SOB 2), and let \(\psi\in C^\infty(\overline\Omega)\). Applying this to \(F=j_n\psi\),
\[
\begin{aligned}
&\int_{\partial\Omega}(\nabla^\perp j_n\cdot\nu)\psi\,ds\\
&\quad=-\int_{\partial\Omega}(\partial_\tau j_n)\psi\,ds\\
&\quad=\int_{\partial\Omega}j_n\,\partial_\tau\psi\,ds .
\end{aligned}
\]
As \(n\to\infty\), the traces converge in \(L^2(\partial\Omega)\), and the right side tends to \(\int\operatorname{tr}j\,\partial_\tau\psi\,ds=0\). Since such \(\psi\) have dense traces, \(\operatorname{tr}(\nabla^\perp j)\cdot\nu=0\).

*Step 4: the remainder is a gradient.* Put \(Z=X-\nabla v-\nabla^\perp j\in H^1(\Omega;\mathbb R^2)\). It is tangent, and since \(\operatorname{div}\nabla^\perp j=0\), \(\operatorname{curl}\nabla v=0\) and \(\operatorname{curl}\nabla^\perp j=\Delta j\),
\[
\operatorname{div}Z=0,\qquad\operatorname{curl}Z=0 .
\]
In the sense of distributions \(\Delta Z_1=\partial_1\operatorname{div}Z-\partial_2\operatorname{curl}Z=0\) and \(\Delta Z_2=\partial_2\operatorname{div}Z+\partial_1\operatorname{curl}Z=0\), so \(Z_1,Z_2\) are real analytic in \(\Omega\) ([Anisotropic derivative classes and analyticity](course:constant-coefficient-equations-and-solvability/AN02-L031), Theorem 3.1). The Cauchy–Riemann equations for \(Z_1-iZ_2\) are exactly \(\operatorname{div}Z=0\) and \(\operatorname{curl}Z=0\), so \(Z_1-iZ_2\) is holomorphic, and it has a primitive \(G\) on the simply connected domain \(\Omega\) (Lemma A.2 of [Dirichlet series and Euler products](course:NT-ZETA/NT-ZETA-01)). The function \(r=\operatorname{Re}G\) satisfies \(\nabla r=(\operatorname{Re}G',-\operatorname{Im}G')=Z\) in \(\Omega\).

We show \(r\in H^1(\Omega)\). For \(M>0\) let \(r_M=\max(-M,\min(r,M))\). Approximating the truncation by smooth functions with derivative in \([0,1]\), as in Lemma 3.2 of the first lesson, shows that \(r_M\) has weak gradient \(\mathbf 1_{\{|r|<M\}}Z\); hence \(r_M\in H^1(\Omega)\) with \(|\nabla r_M|\le|Z|\). Fix a disc \(B\) with \(\overline B\subseteq\Omega\). By Lemma 2.3(2) of the first lesson,
\[
\begin{aligned}
\|r_M\|&\le C_B\bigl(\|\nabla r_M\|+|(r_M)_B|\bigr)\\
&\le C_B\Bigl(\|Z\|+\max_{\overline B}|r|\Bigr).
\end{aligned}
\]
Letting \(M\to\infty\), Fatou's lemma gives \(r\in L^2(\Omega)\). Then \(r_M\to r\) and \(\nabla r_M\to Z\) in \(L^2\) by dominated convergence, so \(r\in H^1(\Omega)\) with \(\nabla r=Z\). Green's formula (2.1) of the first lesson, with the tangent condition and \(\operatorname{div}Z=0\), gives
\[
\begin{aligned}
\int_\Omega|Z|^2&=\int_\Omega Z\cdot\nabla r=-\int_\Omega(\operatorname{div}Z)r\\
&\quad+\int_{\partial\Omega}(\operatorname{tr}Z\cdot\nu)\operatorname{tr}r\,ds=0 .
\end{aligned}
\]
Hence
\[
X=\nabla v+\nabla^\perp j . \tag{1.2}
\]

*Step 5: the energy.* By (2.1) of the first lesson with the tangent field \(\nabla^\perp j\), \(\int\nabla v\cdot\nabla^\perp j=-\int v\operatorname{div}\nabla^\perp j=0\). So the two summands in (1.2) are orthogonal in \(L^2\), and \(\|X\|^2=\|\nabla v\|^2+\|\nabla j\|^2\). Also \(\operatorname{div}X=\Delta v\) and \(\operatorname{curl}X=\Delta j\), so
\[
\mathcal Q(X)=\|\Delta v\|^2+\|\Delta j\|^2 .
\]
Green's formula (2.2) with \(\partial_\nu v=0\), the Cauchy–Schwarz inequality and the definition of \(\mu\) (\(v\) has mean zero) give
\[
\begin{aligned}
&\|\nabla v\|^2=-\int v\Delta v\\
&\quad\le\|v\|\|\Delta v\|\\
&\quad\le\mu^{-1/2}\|\nabla v\|\|\Delta v\|,
\end{aligned} \tag{1.3}
\]
so \(\|\Delta v\|^2\ge\mu\|\nabla v\|^2\). Since \(\operatorname{tr}j=0\), the same argument with \(\lambda_D\) gives \(\|\Delta j\|^2\ge\lambda_D\|\nabla j\|^2\). Therefore
\[
\begin{aligned}
\mathcal Q(X)&\ge\mu\|\nabla v\|^2+\lambda_D\|\nabla j\|^2\\
&=\mu\|X\|^2+(\lambda_D-\mu)\|\nabla j\|^2,
\end{aligned}
\]
and (1.1) follows from \(\mu<\lambda_D\).

*Step 6: equality.* If equality holds, then \(\nabla j=0\), so \(j=0\) by Lemma 2.3(1) of the first lesson, and \(\|\Delta v\|^2=\mu\|\nabla v\|^2\). If \(\Delta v=0\), then (1.3) gives \(\nabla v=0\) and \(X=0=\nabla0\). Otherwise the inequalities in (1.3) are equalities, so \(\|\nabla v\|^2=\mu\|v\|^2\), and \(v\in V\) by Proposition 3.1(2) of the first lesson. Conversely, for \(v\in V\) the field \(\nabla v\) is tangent, \(\operatorname{div}\nabla v=-\mu v\) and \(\operatorname{curl}\nabla v=0\), so \(\mathcal Q(\nabla v)=\mu^2\|v\|^2=\mu\|\nabla v\|^2\). \(\square\)

For tangent \(X,Y\in H^1(\Omega;\mathbb R^2)\) put
\[
\begin{aligned}
&\mathcal E(X,Y)=\int_\Omega\operatorname{div}X\operatorname{div}Y\\
&\quad+\int_\Omega\operatorname{curl}X\operatorname{curl}Y-\mu\int_\Omega X\cdot Y,
\end{aligned}
\]
and \(\mathcal E(X)=\mathcal E(X,X)\).

**Corollary 1.2.** \(\mathcal E(X)\ge0\) for every tangent \(X\in H^1(\Omega;\mathbb R^2)\). If \(\mathcal E(X)=0\), then \(X=\nabla v\) for some \(v\in V\), and \(\mathcal E(X,Y)=0\) for every tangent \(Y\in H^1(\Omega;\mathbb R^2)\).

*Proof.* The first two assertions are Proposition 1.1. For the third, \(0\le\mathcal E(X+tY)=2t\,\mathcal E(X,Y)+t^2\mathcal E(Y)\) for all real \(t\), which forces \(\mathcal E(X,Y)=0\). \(\square\)

Rohleder proved the principle for bounded simply connected Lipschitz domains with piecewise smooth boundary and convex corners, in the form of a minimum over tangent fields of the Dirichlet energy plus a curvature term [Roh21, Theorem 1.1]; the identity of Section 2 connects the two forms. His curvature is negative where the domain is convex; the curvature \(\kappa\) below is positive there.

## 2. The curvature identity

Let \(\kappa=\det(\tau,\partial_\tau\tau)\) on \(\partial\Omega\), where \(\partial_\tau\) is differentiation with respect to arclength in the direction \(\tau\). On the unit circle, \(\tau=(-\sin\theta,\cos\theta)\), \(\partial_\tau\tau=(-\cos\theta,-\sin\theta)\) and \(\kappa=1\).

**Lemma 2.1** ([OpenAI-HS, Lemma 3.2]). For every tangent \(X\in C^2(\overline\Omega;\mathbb R^2)\),
\[
\begin{aligned}
\mathcal Q(X)&=\int_\Omega|\nabla X|^2\\
&\quad+\int_{\partial\Omega}\kappa|X|^2\,ds,
\end{aligned} \tag{2.1}
\]
where \(|\nabla X|^2=\sum_{i,k}(\partial_kX_i)^2\).

*Proof.* Expanding the squares,
\[
\begin{aligned}
&|\operatorname{div}X|^2+|\operatorname{curl}X|^2\\
&\quad=|\nabla X|^2+2\det\nabla X,
\end{aligned}
\]
with \(\det\nabla X=\partial_1X_1\partial_2X_2-\partial_2X_1\partial_1X_2\). Since \(\operatorname{div}\nabla^\perp F=0\), one has \(\operatorname{div}(X_1\nabla^\perp X_2)=\nabla X_1\cdot\nabla^\perp X_2\), which is \(-\det\nabla X\), and \(\operatorname{div}(X_2\nabla^\perp X_1)=\det\nabla X\). By (SOB 1) and \(\nabla^\perp F\cdot\nu=-\partial_\tau F\),
\[
\begin{aligned}
&2\int_\Omega\det\nabla X\\
&\quad=\int_{\partial\Omega}(X_2\nabla^\perp X_1-X_1\nabla^\perp X_2)\cdot\nu\,ds\\
&\quad=\int_{\partial\Omega}(X_1\partial_\tau X_2-X_2\partial_\tau X_1)\,ds .
\end{aligned}
\]
On \(\partial\Omega\) write \(X=a\tau\) with \(a=X\cdot\tau\in C^1(\partial\Omega)\). Then
\[
\begin{aligned}
&X_1\partial_\tau X_2-X_2\partial_\tau X_1\\
&\quad=a^2(\tau_1\partial_\tau\tau_2-\tau_2\partial_\tau\tau_1)\\
&\qquad+a\,\partial_\tau a\,(\tau_1\tau_2-\tau_2\tau_1)\\
&\quad=\kappa a^2=\kappa|X|^2 .\qquad\square
\end{aligned}
\]

The next lesson uses (2.1) for fields that are smooth up to the boundary, and passes to Lipschitz boundary data by an approximation argument.

## 3. Exercises

**3.1.** On the unit disc let \(X=(-x_2,x_1)\). Show that \(X\) is tangent, and check (2.1) by computing both sides.

**3.2.** For the field of Exercise 3.1, find \(v\) and \(j\) in (1.2), and show \(\mathcal E(X)>0\).

**3.3.** On the unit disc let \(X=(1,0)\). Show \(\mathcal Q(X)=0<\mu\int|X|^2\), and explain why this does not contradict Proposition 1.1.

**3.4.** In a boundary chart at \(x_0\) (Section 1 of the first lesson), show that \(\kappa(x_0)=\gamma''(0)\). Deduce that \(\kappa\ge0\) when \(\Omega\) is convex.

**3.5.** Show that the tangent condition is used in Step 1 of the proof of Proposition 1.1, and give an example of a nontangent field \(X\) on the unit disc for which no \(v\in H^1\) satisfies \(\Delta v=\operatorname{div}X\), \(\partial_\nu v=0\).

## 4. Solutions

**3.1.** On the circle \(X=\tau\), so \(X\cdot\nu=0\). Here \(\operatorname{div}X=0\) and \(\operatorname{curl}X=2\), so \(\mathcal Q(X)=4\pi\). The derivatives are \(\partial_2X_1=-1\), \(\partial_1X_2=1\) and \(0\) otherwise, so \(\int|\nabla X|^2=2\pi\); with \(\kappa=1\) and \(|X|=1\) on the circle, the boundary term is \(2\pi\).

**3.2.** \(\operatorname{div}X=0\) gives \(v=0\). The function \(j=(|x|^2-1)/2\) vanishes on the circle and \(\nabla^\perp j=(-x_2,x_1)=X\), so \(X=\nabla^\perp j\). Step 5 of the proof gives \(\mathcal E(X)\ge(\lambda_D-\mu)\|\nabla j\|^2>0\), because \(\nabla j=x\ne0\).

**3.3.** \(\operatorname{div}X=\operatorname{curl}X=0\), while \(\int|X|^2=\pi\). On the circle \(X\cdot\nu=x_1\), which is not zero, so \(X\) is not tangent.

**3.4.** With \(\Omega\) above the graph, \(\nu=(\gamma',-1)/\sqrt{1+\gamma'^2}\) and \(\tau=i\nu=(1,\gamma')/\sqrt{1+\gamma'^2}\). At \(x_1=0\), \(\gamma'=0\), \(ds=dx_1\), \(\tau=(1,0)\) and \(\partial_\tau\tau=(0,\gamma''(0))\), so \(\kappa=\gamma''(0)\). If \(\Omega\) is convex, its intersection with the chart rectangle lies above every tangent line of the graph near \(0\), so \(\gamma\) is convex near \(0\) and \(\gamma''(0)\ge0\).

**3.5.** The compatibility \(\int\operatorname{div}X=0\) is needed for \(\phi=1\) in Step 1. For \(X=(x_1,x_2)\) on the unit disc, \(\operatorname{div}X=2\); a solution would satisfy \(\int\Delta v=\int_{\partial\mathbb D}\partial_\nu v\,ds=0\), but \(\int\operatorname{div}X=2\pi\).

## References

- [OpenAI-HS] OpenAI, *Strict hot spots and absence of interior critical points on smooth simply connected planar domains*, OpenAI Math Release preprint, 24 September 2026, Proposition 3.1, Lemma 3.2. https://github.com/openai/math/tree/main/preprints/Strict-hot-spots-and-absence-of-interior-critical-points-on-smooth-simply-connected-planar-domains-September-24-2026
- [Roh21] J. Rohleder, *A new approach to the hot spots conjecture*, arXiv:2106.05224, Theorem 1.1. https://arxiv.org/abs/2106.05224
