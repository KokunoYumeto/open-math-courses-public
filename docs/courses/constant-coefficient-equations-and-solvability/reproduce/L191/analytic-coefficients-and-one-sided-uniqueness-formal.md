# Analytic coefficients and one-sided uniqueness

*Written by GPT-6.1 Sol (OpenAI), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This chapter proves Holmgren uniqueness for distributions of arbitrary finite local order, for analytic operators of any differential order, and across noncharacteristic surfaces of class \(C^1\). It also treats square systems whose highest normal coefficient is invertible. We do not assume that a solution is analytic, smooth, tempered, or has a normal trace.

The preceding chapter [Fundamental solutions in shrinking cones][S], Sections 7.1–7.2, gives the complete analytic test construction and one-sided uniqueness for arbitrary finite first-order systems. We reuse that proof. [Cauchy bounds, root counts and analytic extensions][C] supplies the coefficient estimates and holomorphic extensions used there. Basic references are [S], Crétier's notes [R], and Hörmander's historical account [H]. The latter two give context; the proofs required here are internal.

## 1. The first-order theorem being reused

Put \(y\in\mathbb R^d\), \(t\in\mathbb R\), and let \(U\) have \(q\) distribution components. The exact first-order statement from [S], Section 7.2, is
\[
 \partial_tU=\sum_{\ell=1}^d A_\ell(y,t)\partial_{y_\ell}U+B(y,t)U,
 \qquad U=0\ \text{where }t<0
 \quad\Longrightarrow\quad U=0\ \text{near }(0,0).
 \tag{1}
\]
All matrix entries are real analytic near the origin; they may be complex valued. The integer \(q\) is arbitrary and finite.

The proof in [S] curves the zero region by \(t'=t+|y|^2\), makes the tangential support compact, and solves the transposed first-order equation for polynomial tangential data and smooth compactly supported time data. Section 7.1 constructs these tests by ordered integrals with successive holomorphic radius losses. Its existence interval depends on the coefficients and radii, not on the size or degree of the forcing. The tests vanish near their terminal time. Polynomial approximation after tangential Gaussian smoothing then separates all distributions on the compact support. Thus (1) applies to distributions directly; it is not a classical-solution assertion.

In dimension \(d=0\), the same proof uses \(\mathbb C^q\) in place of the holomorphic function spaces. Its ordered integrals are the elementary matrix ordinary-differential-equation construction. There are no tangential derivatives or radius losses. The adjoint tests and the conclusion are unchanged.

## 2. Every finite scalar order reduces to that theorem

Use ordinary derivatives in this chapter. For \(D=-i\partial\), the principal symbol in ordinary derivatives differs by the nonzero factor \((-i)^m\); noncharacteristic directions are the same.

Let
\[
 P=\sum_{|\alpha|+j\le m} C_{\alpha j}(y,t)
             \partial_y^\alpha\partial_t^j
 \tag{2}
\]
act on vectors of length \(r\), with analytic \(r\) by \(r\) coefficient matrices. Define
\[
 p_m((y,t),(\eta,\tau))
   =\sum_{|\alpha|+j=m} C_{\alpha j}(y,t)\eta^\alpha\tau^j.
 \tag{3}
\]
The scalar case is \(r=1\).

**Lemma 2.1 (the full jet system).** Suppose \(C_{0m}\) is invertible near the origin. If \(Pu=0\), the finite vector
\[
 W_{\alpha j}=\partial_y^\alpha\partial_t^j u,
 \qquad |\alpha|+j\le m-1
 \tag{4}
\]
satisfies a first-order system of the form (1). Its length is
\[
 q=r\binom{d+m}{m-1}.
 \tag{5}
\]
Every component vanishes on any open set where \(u\) vanishes.

**Proof.** First let \(m\ge1\). If \(|\alpha|+j\le m-2\), the row is
\[
             \partial_tW_{\alpha j}=W_{\alpha,j+1}.
 \tag{6}
\]
If \(|\alpha|+j=m-1\) and \(\alpha\ne0\), choose a coordinate \(\ell\) with \(\alpha_\ell>0\). Distributional derivatives commute, so
\[
       \partial_tW_{\alpha j}
             =\partial_{y_\ell}W_{\alpha-e_\ell,j+1}.
 \tag{7}
\]
The remaining row is \((\alpha,j)=(0,m-1)\). Multiplying (2) on the left by the analytic matrix \(C_{0m}^{-1}\) gives
\[
 \partial_tW_{0,m-1}
 =-C_{0m}^{-1}
      \sum_{(\beta,k)\ne(0,m)}
       C_{\beta k}\partial_y^\beta\partial_t^k u.
 \tag{8}
\]
Terms of total order at most \(m-1\) are components of (4). A term of total order \(m\) has \(\beta\ne0\); choosing \(\beta_\ell>0\) writes it as
\[
       \partial_y^\beta\partial_t^k u
          =\partial_{y_\ell}W_{\beta-e_\ell,k}.
 \tag{9}
\]
Hence each row contains only first tangential derivatives and zeroth-order terms in \(W\). All coefficients are analytic. Matrix inversion is analytic because the determinant is nonzero and the cofactor formula expresses the inverse through analytic products and a nonvanishing analytic reciprocal. The reciprocal is analytic locally by a convergent geometric series.

There are \(\binom{d+m}{m-1}\) multi-indices in \(d+1\) variables of total order at most \(m-1\): insert a final slack coordinate to count weak compositions of \(m-1\) into \(d+2\) parts. This proves (5). No independence of the components is asserted or needed. Derivatives vanish on any open zero set by their definition on tests. For \(m=0\), an invertible multiplication matrix gives \(u=0\) directly, and no jet system is needed. \(\square\)

**Theorem 2.2 (an analytic graph).** Let \(Pu=0\) near a point of a real analytic graph \(t=g(y)\). Suppose
\[
       \det p_m((y_0,g(y_0)),(-\nabla g(y_0),1))\ne0.
 \tag{10}
\]
If the distribution \(u\) vanishes on one side of that graph, it vanishes in a neighborhood of the point.

**Proof.** Translate the point to the origin. Set \(s=t-g(y)\), orienting \(s\) or \(-s\) so that the known zero side is \(s<0\). This is an analytic change of coordinates with explicit inverse \(t=s+g(y)\) and Jacobian one. For distributions its scalar pullback is defined by
\[
 \langle v,\phi(y,s)\rangle
    =\langle u,\phi(y,t-g(y))\rangle.
 \tag{11}
\]
The test on the right has compact support because the change of coordinates is a diffeomorphism. The ordinary change-of-variable and integration-by-parts rules give, in the new coordinates,
\[
          \partial_t=\partial_s,\qquad
          \partial_{y_\ell}^{\,\mathrm{old}}
             =\partial_{y_\ell}^{\,\mathrm{new}}
                        -(\partial_{y_\ell}g)\partial_s.
 \tag{12}
\]
These formulas first follow for smooth functions; distributional transposition gives the same formulas on (11). Iterating them yields the transformed operator. Derivatives falling on coefficients lower the differential order. Its highest coefficient of \(\partial_s^m\) is therefore exactly
\[
              p_m((y,s+g(y)),(-\nabla g(y),1)).
 \tag{13}
\]
It is invertible on a smaller neighborhood by (10) and continuity of its determinant. All transformed coefficients are analytic. Lemma 2.1 reduces the equation to (1), and the open zero side makes all jet components zero there. The reused theorem proves their vanishing near the origin, including the component \(v\) itself. Invert the coordinate change. Reversing the side multiplies the normal by \(-1\), which changes (13) by the scalar \((-1)^m\) and preserves invertibility. \(\square\)

## 3. A continuously differentiable surface needs no analytic flattening

For clarity a \(C^1\) hypersurface means a local level set \(\rho=0\), where \(\rho\) is real valued, continuously differentiable, and \(d\rho\ne0\).

**Lemma 3.1 (the local graph).** After an affine orthogonal change of coordinates, such a surface at the origin has the form
\[
           t=g(y),\qquad g(0)=0,\quad \nabla g(0)=0,
 \tag{14}
\]
where \(g\) is \(C^1\). One side is \(t<g(y)\).

**Proof.** Choose the last coordinate in the direction of \(d\rho(0)\), and multiply \(\rho\) by a positive constant so that \(\partial_t\rho(0)=1\). Its tangential gradient at zero is then zero. On a small box, \(\partial_t\rho\ge1/2\). At the two sufficiently small fixed time endpoints, \(\rho(0,t)\) has opposite signs; the signs persist for nearby \(y\) by continuity. The intermediate value theorem gives a zero for each such \(y\), and strict monotonicity in \(t\) makes it unique.

The same lower bound \(1/2\), applied by the mean value theorem, shows that the zero depends continuously on \(y\). Subtract the equations at \(y+h\) and \(y\); the integral form of the difference of a \(C^1\) function gives
\[
 g(y+h)-g(y)
   =-\frac{\nabla_y\rho(y,g(y))\cdot h}{\partial_t\rho(y,g(y))}
           +o(|h|).
 \tag{15}
\]
For this last step, first use the mean value bound to obtain \(g(y+h)-g(y)=O(|h|)\), then use continuity of all first derivatives in the difference formula. Thus \(g\) is differentiable, with continuous derivative \(-\nabla_y\rho/\partial_t\rho\). This derivative is zero at the origin. Monotonicity also identifies the two sides. \(\square\)

**Theorem 3.2 (distributional Holmgren uniqueness).** Let \(P\) have analytic coefficients near \(x_0\), and let \(u\in\mathcal D'\) solve \(Pu=0\) there. Let \(\rho=0\) be a \(C^1\) hypersurface through \(x_0\). If
\[
                \det p_m(x_0,d\rho(x_0))\ne0
 \tag{16}
\]
and \(u\) vanishes on one side, then \(u=0\) near \(x_0\).

This includes all scalar orders, complex coefficients, and the square systems specified in (2). No condition is imposed on the distribution's order or growth.

**Proof.** For \(m=0\), continuity keeps the multiplication matrix invertible near \(x_0\). Suppose \(m\ge1\). Apply Lemma 3.1 using affine coordinates only. Analyticity of the coefficients is preserved under this affine change. Orient the known zero side as \(t<g(y)\). By (16) and continuity, choose \(\varepsilon>0\) and a neighborhood \(V\) so that
\[
 \det p_m((y,t),(v,1))\ne0
       \quad\text{on }V,\qquad |v|\le4\varepsilon.
 \tag{17}
\]
Because \(\nabla g(0)=0\), choose \(a>0\) sufficiently small that \(|\nabla g(y)|\le\varepsilon\) for \(|y|\le a\). Segment integration gives \(|g(y)|\le\varepsilon|y|\). Shrink \(a\) further so that the closed cylinder
\[
        C=\{|y|\le a,\ |t|\le2\varepsilon a\}
 \tag{18}
\]
lies in the coordinate neighborhood and in \(V\).

Assume for contradiction that the origin is in \(\operatorname{supp}u\). The closed set \(K=\operatorname{supp}u\cap C\) is compact and contains it. Since the known zero side is open, all its points satisfy \(t\ge g(y)\). On \(C\) minimize
\[
          F(y,t)=t+\kappa|y|^2,\qquad
                         \kappa=2\varepsilon/a.
 \tag{19}
\]
Its minimum \(\mu\) on \(K\) is at most zero, since \(F(0,0)=0\). No point of \(K\) is on the bottom \(t=-2\varepsilon a\), because there \(t<-\varepsilon a\le g(y)\). On the side \(|y|=a\),
\[
             F\ge-\varepsilon a+\kappa a^2
                          =\varepsilon a>0.
 \tag{20}
\]
On the top, \(F\ge2\varepsilon a>0\). Thus a minimizing support point lies in the interior of \(C\).

Near that point the distribution is supported on \(F\ge\mu\). The level \(F=\mu\) is a real analytic graph, and its normal is
\[
             dF=(2\kappa y,1),\qquad |2\kappa y|\le4\varepsilon.
 \tag{21}
\]
It is noncharacteristic by (17). Theorem 2.2 now makes \(u\) vanish near this support point, a contradiction. Consequently the origin is outside the closed support and has an open zero neighborhood.

If there are no tangential coordinates, a \(C^1\) surface is locally a single point; its two sides are intervals. The analytic-graph theorem, with \(d=0\), applies directly. This also covers all one-dimensional scalar orders. \(\square\)

The \(C^1\) graph was never used to transform the operator. Such a transformation could destroy analytic coefficients. Instead we touched the support by an analytic paraboloid with a nearby normal. This geometric step is John's extension of the classical analytic-surface argument; [H] describes its history.

## 4. Three useful consequences with their full support hypotheses

**Corollary 4.1 (noncharacteristic exterior normals).** If \(Pu=0\) near a point where the closed support of \(u\) lies on one side of a \(C^1\) surface, that surface must be characteristic at the point whenever the point is in the support.

**Proof.** Otherwise Theorem 3.2 gives a zero neighborhood at a support point. \(\square\)

**Corollary 4.2 (compact homogeneous constant-coefficient solutions).** A compactly supported distribution \(u\) on \(\mathbb R^n\) satisfying \(P(\partial)u=0\) for a nonzero scalar constant-coefficient polynomial is zero.

**Proof.** In order zero the assertion is immediate. Otherwise the nonzero highest homogeneous polynomial \(p_m\) is nonzero at some real direction \(N\). Indeed a polynomial vanishing on all real points is zero: successively treat it as a one-variable polynomial on real coordinate boxes. If the support is nonempty, \(N\cdot x\) has a maximum on it, at \(x_*\). The supporting hyperplane is noncharacteristic because \(p_m(N)\ne0\), and the solution vanishes on its exterior side. Theorem 3.2 contradicts \(x_*\in\operatorname{supp}u\). \(\square\)

**Corollary 4.3 (causal uniqueness without a growth bound).** Let \(p_m(N)\ne0\), \(N\ne0\), for a scalar constant-coefficient operator. If \(P(\partial)u=0\) on all of \(\mathbb R^n\) and \(\operatorname{supp}u\subset\{N\cdot x\ge0\}\), then \(u=0\).

**Proof.** Rescale and use affine orthogonal coordinates so \(N\cdot x=t\) and \(p_m(e_t)\ne0\). If there is a support point \((y_0,t_0)\), minimize on the whole support
\[
                  G(y,t)=t+\delta|y-y_0|^2,\qquad \delta>0.
 \tag{22}
\]
The sublevel \(G\le t_0\), with \(t\ge0\), is compact, contains the chosen point, and therefore contains a minimizer. If \(t_0>0\), its tangential normal satisfies
\[
       |2\delta(y-y_0)|\le2\sqrt{\delta t_0}.
 \tag{23}
\]
Choose \(\delta\) small enough that every normal obeying this bound is noncharacteristic; continuity of \(p_m\) at \(e_t\) suffices. If \(t_0=0\), the only possible minimizer has \(y=y_0,t=0\), and its normal is exactly \(e_t\). In either case the support is locally on the upper side of the analytic minimum level, contradicting Theorem 3.2 at its minimizing support point. No compactness of the whole support, Fourier transform of \(u\), or growth hypothesis was used. \(\square\)

These consequences prove precisely local uniqueness and the stated support continuations. They do not assert solvability for arbitrary data, uniqueness across characteristic surfaces, analytic regularity of every solution, or a singular normal-coefficient system classification.

## References

[S]: ../../AN02-L113.html#7-the-analytic-uniqueness-argument-used-by-the-barrier
[C]: ../../AN02-L045.html

- **[S]** *Fundamental solutions in shrinking cones*, Sections 7.1–7.2. Complete ordered-integral analytic test construction and distributional uniqueness for arbitrary finite first-order systems. Original exposition, CC0.
- **[C]** *Cauchy bounds, root counts and analytic extensions*, Lemmas 1.1 and 3.1. Full polydisc coefficient bounds and local holomorphic extension.
- **[R]** Romain Crétier, *Cauchy-Kovalevska Theorem, Characteristics and Holmgren Theorem*, Sections 2, 3 and 5. [Author-hosted notes](https://www.imo.universite-paris-saclay.fr/media/filer_public/2f/54/2f545d60-a80b-41b4-ae17-58f05160651c/notes_ck.pdf). Freely readable reference; no redistribution licence is inferred.
- **[H]** Lars Hörmander, “Remarks on Holmgren's uniqueness theorem,” *Annales de l'Institut Fourier* **43** (1993), no. 5, 1223–1251. [Original article](https://www.numdam.org/item/10.5802/aif.1371.pdf), DOI 10.5802/aif.1371. Historical account of Holmgren's analytic argument and John's treatment of \(C^1\) surfaces.
