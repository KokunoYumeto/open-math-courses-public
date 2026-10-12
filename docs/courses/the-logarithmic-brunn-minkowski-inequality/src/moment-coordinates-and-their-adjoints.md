# Moment coordinates and their adjoints

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The variance bound of [OpenAI-L] is proved in new coordinates. A probability density \(Z^{-1}e^{-V(x)}\) on \(\mathbb R^n\) is written as the image of a density \(e^{-\varphi(z)}\) under the gradient map \(x=\nabla\varphi(z)\) of the same convex function \(\varphi\). In these *moment coordinates* the Hessian \(\tau=D^2\varphi\) turns integration by parts against \(x\) into a first-order expression, and it defines a second-order operator \(A\) with \(A1=0\) and \(Ax_j=x_j\).

This lesson defines moment pairs, states the existence theorem that the course takes from the literature as a named hypothesis, and proves the identities for \(A\) and for the test functions \(A(A-1)f\) on which the proof of the variance bound rests.

- Moment pairs and the moment equation (Lemma 1.1); the hypothesis (M).
- Adjoints of the derivatives in the two coordinates (Lemma 2.1).
- The operator \(A\) (Proposition 3.1).
- The test fields \(B\), \(W\), \(u\) and their pairings; the Hessian identity (Proposition 4.1).

The lesson follows [OpenAI-L, Sections 3 and 4]. It continues [Wulff bodies and the reduction to a variance bound](wulff-bodies-and-the-reduction-to-a-variance-bound.md), but uses from it only the notation \(\mathbb E_\mu\). It uses integration by parts and the change of variables for integrals in \(\mathbb R^n\).

## 1. Moment pairs

**Definition.** A *moment pair* on \(\mathbb R^n\) consists of smooth real functions \(V\) and \(\varphi\) on \(\mathbb R^n\) such that

- \(Z=\int e^{-V(x)}dx\) is finite, and \(\int e^{-\varphi(z)}dz=1\);
- the Hessian \(D^2\varphi(z)\) is positive definite at every point, and \(\nabla\varphi\) is a one-to-one map of \(\mathbb R^n\) onto \(\mathbb R^n\);
- the image of the probability measure \(d\nu=e^{-\varphi(z)}dz\) under \(\nabla\varphi\) is \(d\mu=Z^{-1}e^{-V(x)}dx\).

Since the Jacobian matrix \(D^2\varphi\) of \(\nabla\varphi\) is invertible, the inverse map is smooth. We write
\[
x=\nabla\varphi(z),\quad\tau=D^2\varphi,\quad M=\tau^{-1}.
\]
A function of \(z\) is also regarded as a function of \(x\), and conversely, through this map; so \(\tau\) and \(M\) are matrix fields in both coordinates. For a function \(g\) of \(x\), the chain rule reads
\[
\partial_{z_k}\bigl(g(x(z))\bigr)=\sum_ig_{x_i}\,\tau_{ik}. \tag{C}
\]
The expectation of a function under \(\nu\), or of the same function in the other coordinates under \(\mu\), is written \(\mathbb E\). A function has compact support in \(x\) exactly if it has compact support in \(z\), because the map and its inverse are continuous.

**Lemma 1.1 (moment equation).** For a moment pair,
\[
\begin{aligned}
&\log\det D^2\varphi(z)\\
&\quad=V(\nabla\varphi(z))+\log Z-\varphi(z).
\end{aligned}
\]

**Proof.** For a continuous function \(g\) with compact support, the change of variables \(x=\nabla\varphi(z)\), whose Jacobian determinant is \(\det\tau>0\), gives
\[
\begin{aligned}
&\int g(x)\,Z^{-1}e^{-V(x)}dx\\
&\quad=\int g(x(z))\,Z^{-1}e^{-V(x(z))}\det\tau(z)\,dz .
\end{aligned}
\]
By the third condition the left side is \(\int g(x(z))e^{-\varphi(z)}dz\). The functions \(g(x(z))\) run through all continuous functions of \(z\) with compact support, so the two continuous densities agree: \(e^{-\varphi}=Z^{-1}e^{-V(x(z))}\det\tau\). \(\blacksquare\)

**Example 1.2.** Let \(a>0\), \(V(x)=\tfrac1{2a}|x|^2\) and \(\varphi(z)=\tfrac a2|z|^2+\tfrac n2\log\tfrac{2\pi}a\). Then \(\nu\) is the Gaussian measure with the covariance \(\tfrac1aI\), the map \(x=az\) carries it to the Gaussian measure with the covariance \(aI\), which is \(\mu\), and \(\tau=aI\). Here \(D^2V=\tfrac1aI\); with \(\varepsilon=\tfrac1a\) the Hessian of \(\varphi\) is \(\tfrac1\varepsilon I\).

**Hypothesis (M).** Let \(n\ge2\) and \(\varepsilon>0\), and let \(V\) be a smooth even function on \(\mathbb R^n\) with \(D^2V\ge\varepsilon I\) at every point. Then there is an even smooth function \(\varphi\) such that \((V,\varphi)\) is a moment pair and
\[
D^2\varphi\le\frac4\varepsilon\,I\qquad\text{at every point.}
\]

This is the lemma on moment coordinates of [OpenAI-L, Section 3]. It is not proved in this course. According to [OpenAI-L], its proof starts from a theorem of R. Berman and B. Berndtsson, which gives the function \(\varphi\) when the density lives on a ball, and from an estimate of B. Klartag, which gives the bound \(4/\varepsilon\) for the Hessian independently of the radius of the ball; the passage to the whole space uses interior estimates for elliptic equations. The general theory of such pairs is attributed there to D. Cordero-Erausquin and B. Klartag. Lemma 1.1 shows that the equation in the statement of [OpenAI-L] follows from the other properties.

The results of Sections 2 to 4 hold for every moment pair. They use neither the evenness nor the bound for the Hessian.

## 2. Adjoints

Fix a moment pair. Write \(\partial_k=\partial_{z_k}\), and for a function \(F\) of \(z\)
\[
\partial_k^*F=x_kF-\partial_kF .
\]
For a vector field \(W=(W_1,\dots,W_n)\) in the coordinates \(x\) let
\[
\delta_\mu W=\sum_j\bigl(V_{x_j}W_j-\partial_{x_j}W_j\bigr).
\]
For a matrix field, \(\delta_\mu\) is applied to each row and gives a vector field.

**Lemma 2.1.** Let \(g,F\) be smooth functions and \(W\) a smooth vector field, and let \(g\), or else \(F\) and \(W\), have compact support.

1. \(\mathbb E\,(\partial_kg)\,F=\mathbb E\,g\,\partial_k^*F\).
2. \(\mathbb E\,\nabla_xg\cdot W=\mathbb E\,g\,\delta_\mu W\).
3. For a smooth matrix field \(P\), \(\sum_k\partial_k^*P_{ak}=(\delta_\mu(P\tau))_a\) for every \(a\).
4. \(\delta_\mu\tau=x\); that is, \(\mathbb E\,x_jg=\mathbb E\sum_k\tau_{jk}\,g_{x_k}\) for smooth \(g\) with compact support.

**Proof.** (1) Integrate \(\partial_k(gFe^{-\varphi})\) over \(\mathbb R^n\); the integral is \(0\), and \(\partial_ke^{-\varphi}=-x_ke^{-\varphi}\) because \(\partial_k\varphi=x_k\). (2) In the same way, integrate \(\partial_{x_j}(gW_je^{-V})\) and sum over \(j\). (3) Let \(g\) have compact support. By (1), the chain rule (C) and (2),
\[
\begin{aligned}
\mathbb E\,g\sum_k\partial_k^*P_{ak}&=\mathbb E\sum_k(\partial_kg)\,P_{ak}\\
&=\mathbb E\sum_{i,k}g_{x_i}\,\tau_{ik}P_{ak}\\
&=\mathbb E\,g\,(\delta_\mu(P\tau))_a .
\end{aligned}
\]
This holds for all such \(g\), and both functions are continuous. (4) Take for \(P\) the identity matrix in (3): \(\sum_k\partial_k^*\delta_{ak}=x_a\). The second form is (2). \(\blacksquare\)

Statement (4) says that \(\tau\) turns a multiplication by \(x_j\) into derivatives. For the Gaussian pair of Example 1.2 with \(a=1\) it is the familiar formula \(\mathbb E\,x_jg=\mathbb E\,g_{x_j}\). According to [OpenAI-L], this construction of such a matrix field from the moment map is due to M. Fathi.

## 3. The operator \(A\)

For a smooth function \(f\) of \(x\) let
\[
\begin{gathered}
Af=\delta_\mu(\tau\nabla_xf),\\
\Gamma(f,g)=\nabla_xf\cdot\tau\nabla_xg .
\end{gathered}
\]

**Proposition 3.1.**

1. \(Af=\sum_k\partial_k^*f_{x_k}\), and this is \(x\cdot\nabla_xf-\sum_{i,k}\tau_{ik}f_{x_ix_k}\).
2. \(\mathbb E\,g\,Af=\mathbb E\,\Gamma(g,f)\) if \(f\) or \(g\) has compact support. In particular \(\mathbb E\,g\,Af=\mathbb E\,f\,Ag\), and \(\mathbb E\,Af=0\) for \(f\) with compact support.
3. \(A1=0\) and \(Ax_j=x_j\).
4. \(A(fg)=f\,Ag+g\,Af-2\,\Gamma(f,g)\). For a smooth function \(\beta\) of one variable, \(A(\beta(f))\) is \(\beta'(f)\,Af-\beta''(f)\,\Gamma(f,f)\).

**Proof.** (1) The first equality is Lemma 2.1 (3) for the matrix with the single row \((f_{x_1},\dots,f_{x_n})\). By the chain rule (C), \(\partial_kf_{x_k}=\sum_if_{x_kx_i}\tau_{ik}\), which gives the second. (2) is Lemma 2.1 (2) for \(W=\tau\nabla_xf\). (3) follows from the formula in (1). (4) The first-order part \(x\cdot\nabla\) obeys the product rule and the chain rule. For the second-order part write \(\tau{:}D^2f=\sum_{i,k}\tau_{ik}f_{x_ix_k}\). Then
\[
\begin{aligned}
\tau{:}D^2(fg)&=f\,\tau{:}D^2g+g\,\tau{:}D^2f\\
&\quad+2\,\Gamma(f,g),\\
\tau{:}D^2(\beta(f))&=\beta'(f)\,\tau{:}D^2f\\
&\quad+\beta''(f)\,\Gamma(f,f).
\end{aligned}
\]
\(\blacksquare\)

So \(A\) is a symmetric operator on smooth functions with compact support, constants are in its kernel, and the coordinate functions are eigenfunctions with the eigenvalue \(1\). Hence \(A(A-1)\) annihilates every affine function. For the Gaussian pair, \(A=x\cdot\nabla-\Delta\).

## 4. The test functions

Let \(f\) be a smooth function of \(x\) with compact support. Put
\[
\begin{gathered}
h=D_x^2f,\qquad P=\tau h,\qquad B=\tau h\tau,\\
W_a=\sum_k\partial_k^*P_{ak},\qquad u=\delta_\mu W .
\end{gathered}
\]
These fields have compact support. The matrices \(h\) and \(B\) are symmetric.

**Proposition 4.1.**

1. \(W=\delta_\mu B\).
2. For every smooth function \(F\) of \(x\),
\[
\begin{aligned}
\mathbb E\,uF&=\mathbb E\,W\cdot\nabla_xF\\
&=\mathbb E\sum_{a,i}B_{ai}F_{x_ax_i}.
\end{aligned}
\]
3. \(W\) is the gradient in \(z\) of the function \((Af-f)(x(z))\); so \(W=\tau\,\nabla_x(Af-f)\), and \(u=A(A-1)f\). In particular the matrix \(D_zW=(\partial_lW_a)\) is symmetric.
4. (Hessian identity)
\[
\begin{aligned}
&\mathbb E\,(Af)\,(Af-f)\\
&\quad=\mathbb E\,\operatorname{tr}(h\tau h\tau)\\
&\quad=\mathbb E\,\bigl\|\tau^{1/2}\,D_x^2f\,\tau^{1/2}\bigr\|^2 ,
\end{aligned}
\]
where \(\|Q\|^2=\operatorname{tr}(Q^TQ)\).

**Proof.** (1) is Lemma 2.1 (3), since \(P\tau=B\). (2) Apply Lemma 2.1 (2) twice: first to \(g=F\) and \(W\), then, for each \(a\), to \(g=F_{x_a}\) and the row \(a\) of \(B\).

(3) Let \(C_{aik}=\partial_a\partial_i\partial_k\varphi\). By the definition and the chain rule (C),
\[
\begin{aligned}
W_a&=\sum_kx_k\,P_{ak}-\sum_k\partial_k\Bigl(\sum_i\tau_{ai}f_{x_ix_k}\Bigr)\\
&=\sum_{i,k}x_k\tau_{ai}f_{x_ix_k}-\sum_{i,k}C_{aik}f_{x_ix_k}\\
&\quad-\sum_{i,j,k}\tau_{ai}\tau_{jk}f_{x_ix_kx_j}.
\end{aligned}
\]
On the other hand \(Af-f=\sum_kx_kf_{x_k}-\sum_{i,k}\tau_{ik}f_{x_ix_k}-f\), and its derivative in \(z_a\) is
\[
\begin{aligned}
&\sum_k\tau_{ak}f_{x_k}+\sum_{i,k}x_kf_{x_kx_i}\tau_{ia}\\
&\quad-\sum_{i,k}C_{aik}f_{x_ix_k}-\sum_{i,j,k}\tau_{ik}f_{x_ix_kx_j}\tau_{ja}\\
&\quad-\sum_if_{x_i}\tau_{ia}.
\end{aligned}
\]
The first and the last sum cancel, and the rest is \(W_a\). The second form of \(W\) is the chain rule (C). Then \(u=\delta_\mu(\tau\nabla_x(Af-f))=A(Af-f)\). A gradient in \(z\) has a symmetric matrix of derivatives.

(4) By Proposition 3.1 (2), then (3), then Lemma 2.1 (2) for the rows of \(B\),
\[
\begin{aligned}
&\mathbb E\,(Af)(Af-f)\\
&\quad=\mathbb E\,\nabla_xf\cdot\tau\nabla_x(Af-f)\\
&\quad=\mathbb E\,\nabla_xf\cdot W\\
&\quad=\mathbb E\sum_{a,i}B_{ai}f_{x_ax_i},
\end{aligned}
\]
and \(\sum B_{ai}h_{ai}=\operatorname{tr}(\tau h\tau h)\), which is the squared norm of the symmetric matrix \(\tau^{1/2}h\tau^{1/2}\). \(\blacksquare\)

Statement (2) allows to compute the pairing of the test function \(u\) with a function \(F\) through the first or through the second derivatives of \(F\); the function \(F\) need not have compact support. The Hessian identity shows why affine functions play a special role: if \(Af=f\) or \(Af=0\) held for a function with compact support, its Hessian would vanish. According to [OpenAI-L], the identity is a special case of a formula of A. Kolesnikov, G. Livshyts and L. Rotem.

**Example 4.2.** For the Gaussian pair with \(a=1\) and a polynomial \(f\) (the formulas of this section do not need compact support when all functions are polynomials), \(B=D^2f\), \(W=\nabla(Af-f)\) and \(u=A(A-1)f\). For \(f=x_1^3\): \(Af=3x_1^3-6x_1\), \((A-1)f=2x_1^3-6x_1\), \(W=(6x_1^2-6,0,\dots,0)\), and \(u=A(2x_1^3-6x_1)=6x_1^3-18x_1\). The Hessian identity reads \(\mathbb E(3x_1^3-6x_1)(2x_1^3-6x_1)=\mathbb E\,36x_1^2\); both sides are \(36\), since \(\mathbb Ex_1^2=1\), \(\mathbb Ex_1^4=3\), \(\mathbb Ex_1^6=15\).

## 5. Exercises

**5.1.** Let \(n=1\), and let \(\varphi\) be a smooth function on \(\mathbb R\) with \(\varphi''>0\), \(\int e^{-\varphi}=1\) and \(\varphi'(\mathbb R)=\mathbb R\). Show that there is a function \(V\), unique up to the choice of \(Z\), such that \((V,\varphi)\) is a moment pair, and give \(V'(x)\) in terms of \(\varphi\).

**5.2.** Show that for a moment pair the mean of \(\mu\) is \(0\): \(\mathbb E\,x_j=0\).

**5.3.** Show that \(\mathbb E\,\operatorname{tr}\tau=\mathbb E\,|x|^2\), if \(|x|^2\) is integrable for \(\mu\) and \(\tau\) is bounded.

**5.4.** Check Proposition 4.1 (2) for the Gaussian pair with \(a=1\), \(f=x_1^3\) and \(F=x_1^4\).

## 6. Solutions

**5.1.** The map \(x=\varphi'(z)\) is a smooth bijection of \(\mathbb R\) with \(dx=\varphi''dz\). The image of \(e^{-\varphi}dz\) has the density \(e^{-\varphi(z)}/\varphi''(z)\) at \(x=\varphi'(z)\). So one must take \(V(x)=\varphi(z)+\log\varphi''(z)-\log Z\), as in Lemma 1.1, and this function is smooth with \(\int e^{-V}dx=Z\). Differentiating in \(z\): \(V'(x)\,\varphi''=\varphi'+\varphi'''/\varphi''\), so \(V'(x)=\bigl(x+\varphi'''(z)/\varphi''(z)\bigr)/\varphi''(z)\).

**5.2.** \(\mathbb E\,x_j=\int\partial_j\varphi\,e^{-\varphi}dz=-\int\partial_j(e^{-\varphi})dz\). Since \(\varphi\) is convex and \(e^{-\varphi}\) is integrable, \(\varphi(z)\ge c|z|-b\) for some \(c>0\), so \(e^{-\varphi}\) tends to \(0\) at infinity and the integral of its derivative over each line parallel to the axis \(j\) is \(0\). On such a line \(e^{-\varphi}\) increases and then decreases, so the integral of \(|\partial_je^{-\varphi}|\) over the line is at most twice the maximum of \(e^{-\varphi}\) on it, which is integrable over the family of lines; this justifies the integration line by line. (For the bound: the convex set where \(\varphi\le\varphi(0)+1\) has finite volume, so it is bounded, say by the radius \(\varrho\); then by convexity \(\varphi(z)\ge\varphi(0)+|z|/\varrho\) for \(|z|\ge\varrho\).)

**5.3.** Apply Lemma 2.1 (4) to \(g=\eta_r(x)\,x_j\), where \(\eta_r\) is a smooth function with \(\eta_r=1\) for \(|x|\le r\), \(\eta_r=0\) for \(|x|\ge2r\) and \(|\nabla\eta_r|\le2/r\), and sum over \(j\): \(\mathbb E\,\eta_r|x|^2=\mathbb E\,\eta_r\operatorname{tr}\tau+\mathbb E\,x\cdot\tau\nabla\eta_r\). The last term is at most \(4\|\tau\|\,\mathbb P(|x|\ge r)\) in absolute value, because \(|x|\le2r\) where \(\nabla\eta_r\ne0\). Let \(r\to\infty\).

**5.4.** \(u=6x_1^3-18x_1\) and \(F=x_1^4\): \(\mathbb E\,uF=6\,\mathbb Ex_1^7-18\,\mathbb Ex_1^5=0\). \(W\cdot\nabla F=(6x_1^2-6)\,4x_1^3\), with the mean \(0\). \(\sum B_{ai}F_{x_ax_i}=6x_1\cdot12x_1^2\), with the mean \(0\). All three vanish because the integrands are odd. With \(F=x_1^3\) instead: \(\mathbb E\,uF=6\cdot15-18\cdot3=36\), \(\mathbb E\,(6x_1^2-6)\,3x_1^2=54-18=36\), and \(\mathbb E\,6x_1\cdot6x_1=36\).

## References

- [OpenAI-L] OpenAI, *The logarithmic Brunn-Minkowski conjecture*, OpenAI Math Release preprint, 23 September 2026, Sections 3 and 4. https://github.com/openai/math/tree/main/preprints/The-logarithmic-Brunn-Minkowski-conjecture-September-23-2026
