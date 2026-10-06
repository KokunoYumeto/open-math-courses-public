# Stationary phase and critical manifolds

A rapidly oscillating integral cancels where its phase changes to first order. Near a critical point, the quadratic part controls the size and the complex phase of the answer. When critical points form a manifold, cancellation acts only in its normal directions. This lesson develops those three mechanisms with estimates that remain useful when the phase and amplitude vary.

The precise prerequisites are the earlier proof companions. [Quadratic stationary phase, Q1–Q9](quadratic-stationary-phase.md) proves the analytic identities; [Morse reduction, M1–M2](parameter-morse-reduction.md) proves the smooth coordinate construction; [change of variables, P19–P21](change-of-variables-prerequisite-completions.md) proves substitution and its measure prerequisites. Their exact earlier-programme proof bindings retain Jiří Lebl's freely accessible *Basic Analysis*, version 6.3, and supply the used omitted exercises locally. Appendix A below proves the sharper Plancherel estimate needed here, the finite cutoffs, and the density and localization facts for critical manifolds.

The complete mathematical proof chain of this lesson is recorded in the accompanying full-stationary proof bindings.

For a human account of stationary phase, see [Guillemin–Sternberg, Chapter 14](https://math.mit.edu/~vwg/semiclassGuilleminSternberg.pdf) and [Bates–Weinstein, Appendix B](https://math.berkeley.edu/~alanw/GofQ.pdf). The estimates below include uniform parameter derivatives, differentiated symbol remainders and the quotient density of a clean critical manifold.

## 1. What a uniform estimate means

Let \(U\subset\mathbb R^d\) be open, \(K\Subset U\), and let \(s\) vary in an open set \(S\subset\mathbb R^p\). For a real smooth phase \(\phi(x,s)\) and an amplitude \(a(x,s)\) supported in \(K\) in the \(x\) variable, set

\[
I(\lambda,s)=\int_U e^{i\lambda\phi(x,s)}a(x,s)\,dx,
\qquad \lambda\geq1.
\]

Uniformity will always refer to \(s\) in a specified compact set \(S_0\Subset S\), fixed supports, finitely many bounds on derivatives, and positive lower bounds for the geometric quantities used in the proof. Pointwise nondegeneracy alone does not give a uniform bound across a family.

Our convention is

\[
\widehat b(\xi)=\int e^{-ix\cdot\xi}b(x)\,dx,
\qquad
b(x)=(2\pi)^{-d}\int e^{ix\cdot\xi}\widehat b(\xi)\,d\xi,
\qquad D_j=-i\partial_{x_j}.
\]

The signature of a real symmetric invertible matrix is its number of positive eigenvalues minus its number of negative eigenvalues.

All integrals here are compact Riemann integrals or absolutely convergent improper integrals as constructed in P17–P21. A zero-dimensional integral is evaluation, the empty determinant is one, and the empty signature is zero. The zero-dimensional quadratic identity is therefore immediate; calculations with a radial variable below concern positive dimension.

## 2. Cancellation away from critical points

**Proposition 2.1 (nonstationary estimate).** Suppose \(|\nabla_x\phi|\geq c>0\) on a fixed neighborhood of \(K\times S_0\). For all integers \(M,r\geq0\),

\[
\|I(\lambda,\cdot)\|_{C^r(S_0)}
\leq C_{M,r}\lambda^{-M}
\max_{|\alpha|+|\beta|\leq M+2r}
\sup_{K\times S_0}|\partial_x^\alpha\partial_s^\beta a|.
\tag{2.1}
\]

The constant depends on the fixed support, \(c^{-1}\), and finitely many phase derivatives on that neighborhood. Increasing the displayed amplitude seminorm is harmless.

**Proof.** Define

\[
L=\frac{\nabla_x\phi\cdot\nabla_x}
{i\lambda|\nabla_x\phi|^2}.
\]

Then \(Le^{i\lambda\phi}=e^{i\lambda\phi}\). Its formal transpose for the bilinear integral pairing is

\[
L^tb=-\frac1{i\lambda}
\operatorname{div}_x\left(
\frac{b\nabla_x\phi}{|\nabla_x\phi|^2}\right).
\]

Integrating by parts \(M\) times gives \(I=\int e^{i\lambda\phi}(L^t)^Ma\,dx\). Each iteration contributes \(\lambda^{-1}\), differentiates the amplitude at most once, and differentiates a coefficient whose denominator is bounded away from zero. Compact support removes all boundary terms. This proves the estimate for \(r=0\).

A derivative of order at most \(r\) in \(s\) produces a finite sum of integrals with amplitudes \(\lambda^q b_q\), \(q\leq r\), where \(b_q\) is a product of phase derivatives and derivatives of \(a\) in \(s\). Apply \(M+r\) integrations by parts to each. The derivatives of \(a\) needed have total order at most \(M+2r\). This proves (2.1). ∎

For each fixed number of derivatives, the estimate still decays faster than every power. It does not assert that differentiating the phase has no cost.

## 3. The quadratic calculation with its sign

For a real symmetric invertible \(d\times d\) matrix \(H\), put

\[
Q_H(x)=\tfrac12x^THx,
\qquad
\Delta_H=\sum_{j,k}(H^{-1})_{jk}\partial_{x_j}\partial_{x_k}.
\]

**Lemma 3.1 (Fresnel transform).** As a tempered distribution,

\[
\mathcal F(e^{i\lambda Q_H})(\xi)
=c_H(\lambda)
\exp\left(-\frac{i}{2\lambda}\xi^TH^{-1}\xi\right),
\qquad
c_H(\lambda)=\left(\frac{2\pi}{\lambda}\right)^{d/2}
\frac{e^{i\pi\operatorname{sgn}H/4}}{|\det H|^{1/2}}.
\tag{3.1}
\]

**Proof.** First multiply the left side by \(e^{-\varepsilon|x|^2/2}\), \(\varepsilon>0\), so its Fourier transform is an ordinary integral. Orthogonal diagonalization reduces the calculation to

\[
\int_{\mathbb R}e^{-zx^2/2-i\xi x}\,dx
=(2\pi)^{1/2}z^{-1/2}e^{-\xi^2/(2z)},
\qquad \operatorname{Re}z>0.
\tag{3.2}
\]

Here is a direct real-parameter justification of (3.2). Write \(z=\varepsilon-iq\), with \(\varepsilon>0\), \(q\in\mathbb R\), and
\[
J(q)=\int_{\mathbb R}e^{-(\varepsilon-iq)x^2/2}\,dx.
\]
Differentiation in \(q\) is allowed by the integrable Gaussian bounds. Integration of the derivative of \(x e^{-zx^2/2}\) gives
\[
\int x^2e^{-zx^2/2}\,dx=z^{-1}J(q),\qquad
J'(q)=\frac{i}{2z}J(q).
\]
At \(q=0\), the positive Gaussian integral in Appendix A gives \(J(0)=(2\pi/\varepsilon)^{1/2}\). The function \((2\pi)^{1/2}z^{-1/2}\), with the continuous square root positive at \(q=0\), satisfies the same first-order equation and initial value. The quotient of \(J(q)\) by the displayed nonvanishing candidate has derivative zero and initial value one, so they agree. This does not assume in advance that \(J\) is nonzero. For fixed \(z\), put
\[
F_z(\xi)=\int e^{-zx^2/2-i\xi x}\,dx.
\]
Integrating the derivative of \(e^{-zx^2/2-i\xi x}\) gives \(F_z'(\xi)=-\xi z^{-1}F_z(\xi)\). Multiplication by \(e^{\xi^2/(2z)}\) shows that \(F_z(\xi)=F_z(0)e^{-\xi^2/(2z)}\). This proves (3.2) for every \(z\) in the right half-plane, without requiring a complex-analytic continuation theorem.

For an eigenvalue \(h_j\neq0\), use \(z=\varepsilon-i\lambda h_j\). As \(\varepsilon\downarrow0\), its inverse square root tends to \((\lambda|h_j|)^{-1/2}e^{i\pi\operatorname{sign}(h_j)/4}\). The exponential on the right of (3.2) has absolute value at most one for real \(\xi\), so dominated convergence against Schwartz functions proves the transformed limit. The original damped functions also converge as tempered distributions, since their absolute values are at most one. Multiply the scalar formulas. The orthogonal substitution is P21.4, the spectral decomposition is Q5, and the root limits and signs are P16.3. Q1 supplies the compact-plus-tail justification of each limit and parameter derivative, and Appendix A.2 defines the distributional transpose. ∎

**Theorem 3.2 (quadratic expansion).** Let \(b\in C_c^\infty(\mathbb R^d)\), and let \(\ell>d/2\) be an integer. For every integer \(N\geq0\),

\[
\int e^{i\lambda Q_H(x)}b(x)\,dx
=c_H(\lambda)
\left[
\sum_{j=0}^{N-1}\frac{1}{j!}
\left(\frac{i}{2\lambda}\right)^j
\Delta_H^jb(0)+R_N(\lambda)
\right],
\tag{3.3}
\]

where, on a fixed compact support,

\[
|R_N(\lambda)|
\leq C_{d,\ell,N,K}\lambda^{-N}\|H^{-1}\|^N
\sum_{|\alpha|\leq2N+\ell}\|\partial^\alpha b\|_{L^\infty}.
\tag{3.4}
\]

For \(N=0\) the sum is empty and the matrix factor is one; the unexpanded exponential in (3.5) has absolute value one.

**Proof.** The pairing version of (3.1), followed by Fourier inversion, gives the bracket in (3.3) as

\[
(2\pi)^{-d}\int
e^{-i\xi^TH^{-1}\xi/(2\lambda)}\widehat b(\xi)\,d\xi.
\tag{3.5}
\]

Taylor's formula on the real axis bounds the exponential remainder by \(|\xi^TH^{-1}\xi|^N/(2^NN!\lambda^N)\). Fourier inversion identifies the polynomial terms: multiplication by \(\xi_j\xi_k\) corresponds to \(-\partial_{x_j}\partial_{x_k}\), giving the positive \(i\) in (3.3).

For the remainder, take the absolute integral and use

\[
\int|\xi|^{2N}|\widehat b(\xi)|\,d\xi
\leq C_{d,\ell,N}
\sum_{|\alpha|\leq2N+\ell}\|\partial^\alpha b\|_{L^2}.
\]

This is Cauchy–Schwarz with the integrable weight \(\langle\xi\rangle^{-2\ell}\), then Plancherel. Appendix A.3 proves this estimate with the derivative count displayed here. The fixed support bounds each \(L^2\) norm by its supremum times the square root of its outer measure, as proved in Appendix A.3; no Jordan measurability of an arbitrary compact support is assumed. ∎

The estimate is for the bracket. The error in the integral has the additional factor \(\lambda^{-d/2}|\det H|^{-1/2}\).

## 4. A quadratic coordinate system that varies smoothly

**Lemma 4.1 (Morse coordinates with parameters).** Suppose \(\nabla_x\phi(x_0,s_0)=0\) and \(H_0=\phi_{xx}''(x_0,s_0)\) is invertible. After shrinking neighborhoods, there are a smooth critical point \(x_c(s)\), a local diffeomorphism \(x=F(z,s)\), and a diagonal matrix \(J\) with entries \(+1\) or \(-1\) such that

\[
F(0,s)=x_c(s),\qquad
\phi(F(z,s),s)=c(s)+\tfrac12z^TJz,
\qquad c(s)=\phi(x_c(s),s).
\tag{4.1}
\]

The signature of \(J\) is that of \(H(s)=\phi_{xx}''(x_c(s),s)\), and

\[
|\det F_z'(0,s)|=|\det H(s)|^{-1/2}.
\tag{4.2}
\]

**Proof.** The smooth inverse and implicit function theorems are P3; the full argument including its induction is also M1. Smooth differentiation of the integral remainder is P12.7, the Schur calculation is P4, and congruence of signatures is P5. The implicit function theorem applied to \(\phi_x'\) gives \(x_c(s)\). Translate this point to zero. Make a fixed real linear change of variables so that the first diagonal entry of the Hessian is nonzero. Such a direction exists because a symmetric form with zero quadratic value on every vector is zero, whereas this Hessian is invertible.

Write \(x=(x_1,x')\). The implicit function theorem gives \(x_1=h(x',s)\) solving \(\partial_{x_1}\phi=0\). Taylor's formula with integral remainder gives

\[
\phi(h+v,x',s)=g(x',s)+\tfrac12v^2A(v,x',s),
\qquad
A=2\int_0^1(1-t)\partial_{x_1}^2\phi(h+tv,x',s)\,dt.
\]

The smooth function \(A\) is nonzero near the origin. Its sign \(\sigma\) is fixed there. The coordinate \(z_1=v|A|^{1/2}\) is valid by the inverse function theorem and changes this expression into \(g(x',s)+\sigma z_1^2/2\).

The Hessian of \(g\) at its critical point is the Schur complement of the first pivot in the original Hessian. Block elimination shows that its determinant is the original determinant divided by that pivot, so it is invertible. Induct on the remaining variables, keeping \(s\) as a parameter. This proves (4.1).

Differentiating (4.1) twice at \(z=0\) gives \(F_z'^THF_z'=J\), because the first derivative of \(\phi\) vanishes there. Congruence preserves the numbers of positive and negative directions. Taking absolute determinants gives (4.2). ∎

Every coordinate change has bounded derivatives on a sufficiently small fixed compact neighborhood; its inverse has bounded derivatives on the corresponding compact image inside its inverse domain (M2). This is the quantitative fact needed below; the argument does not claim a neighborhood of fixed size when the Hessian approaches singularity.

## 5. One critical point and a full expansion

**Theorem 5.1 (uniform real stationary phase).** Suppose \(\phi\) and \(a\) are smooth, the \(x\) support of \(a\) lies in a fixed compact set, and, near that support, \(\phi(\cdot,s)\) has one critical point \(x_c(s)\) with invertible Hessian \(H(s)\). Fix a compact parameter set on which these hypotheses hold with uniform neighborhoods, a uniformly invertible Hessian, and a positive gradient lower bound outside a fixed neighborhood of the critical point. Then

\[
I(\lambda,s)=e^{i\lambda c(s)}
\left(\frac{2\pi}{\lambda}\right)^{d/2}
\frac{e^{i\pi\sigma/4}}{|\det H(s)|^{1/2}}
\left[\sum_{j=0}^{N-1}\lambda^{-j}C_j a(s)
+\mathcal R_N(\lambda,s)\right],
\tag{5.1}
\]

where \(\sigma=\operatorname{sgn}H\) is constant on each connected parameter component, \(C_0a(s)=a(x_c(s),s)\), and \(C_ja\) depends only on derivatives of the amplitude in \(x\) of order at most \(2j\) at \(x_c(s)\). For every \(r\geq0\),

\[
\|\mathcal R_N(\lambda,\cdot)\|_{C^r}
\leq C_{N,r}\lambda^{-N}p_{N,r}(a),
\tag{5.2}
\]

where \(p_{N,r}\) is a finite amplitude seminorm. The constants also depend on finitely many phase and coordinate derivatives and the lower bounds just specified. The derivatives in (5.2) act on the remainder after the oscillatory factor in (5.1) has been removed.

**Proof.** Work first in one parameter neighborhood and shrink to precompact coordinate and parameter domains. Appendix A.4 supplies a smooth cutoff in their product, equal to one on a fixed smaller neighborhood of the critical graph. Its support has a compact inverse image strictly inside the Morse chart (M2). Split the amplitude into its near and far parts. Proposition 2.1 makes the far integral smaller than every inverse power of \(\lambda\), with any fixed number of parameter derivatives. Multiplying it by \(e^{-i\lambda c(s)}\lambda^{d/2}\) costs only finitely many powers, which that proposition can absorb.

For the near part use Lemma 4.1 and define

\[
b(z,s)=a(F(z,s),s)|\det F_z'(z,s)|
\]

with the cutoff included. Compact chart substitution is P21.4. The precompact support just chosen makes extension of \(b\) by zero smooth, with a common compact support in \(z\) for the parameter neighborhood (P17.4). Theorem 3.2 with \(H=J\) gives (5.1) with

\[
C_ja(s)=\frac{|\det H(s)|^{1/2}}{j!}
\left(\frac i2\right)^j\Delta_J^jb(0,s).
\tag{5.3}
\]

The cutoff is one near zero, so its derivatives do not enter these coefficients. The chain rule shows that no more than \(2j\) derivatives of \(a\) in \(x\) occur. Formula (4.2) gives \(C_0a=a(x_c,s)\).

After the critical value has been factored out, the quadratic phase and \(J\) do not depend on \(s\). Thus parameter derivatives act only on \(b\) and the smooth determinant factor. Apply (3.4) to those derivatives. For the near integral it is enough to bound the corresponding mixed derivatives of \(b\) through order \(2N+\ell+r\); the far integral may require a larger finite seminorm. This proves (5.2).

Although (5.3) uses a coordinate choice, the coefficients do not depend on that choice. Two such expansions approximate the same normalized integral. If their coefficients below order \(j\) agree, subtract the expansions through order \(j\), using \(N=j+1\). Multiplication by \(\lambda^j\) gives the difference of the order-\(j\) coefficients plus \(O(\lambda^{-1})\). Taking \(\lambda\to\infty\) makes that difference zero. Starting at \(j=0\) proves equality of every coefficient.

Morse coordinates need only exist locally in the parameter. Cover the specified compact parameter set by finitely many neighborhoods on each of which Lemma 4.1 provides coordinates and a fixed signature. Prove the expansion and all its differentiated estimates on each neighborhood as above. The uniqueness argument identifies the local coefficient functions on overlaps; they therefore define the same smooth coefficients wherever the critical branch is defined. Take the maximum of the finitely many remainder constants and the union of their finite seminorm requirements. This yields the stated uniform bounds without assuming a global signed Morse frame. ∎

The assertion remains valid for smooth amplitudes with values in a finite-dimensional vector space: apply it component by component. Its constants can be chosen uniformly on bounded sets in that space.

For several isolated nondegenerate critical points separated uniformly on the support, use disjoint cutoffs and add their expansions. Each contribution has its own critical value, Hessian and signature.

## 6. Amplitudes that are symbols in the large parameter

A family \(a_\lambda(x,s)\), supported in the same compact set, is a symbol of order \(\mu\) in \(\lambda\) if, for all \(k,\alpha,\beta\),

\[
|\partial_\lambda^k\partial_x^\alpha\partial_s^\beta
a_\lambda(x,s)|\leq C_{k,\alpha,\beta}\lambda^{\mu-k}.
\tag{6.1}
\]

**Corollary 6.1 (symbol remainder).** Under the geometric hypotheses of Theorem 5.1, replace \(a\) by a family satisfying (6.1), and apply \(C_j\) to that family without expanding it further. The normalized remainder satisfies

\[
|\partial_\lambda^k\partial_s^\beta\mathcal R_N(\lambda,s)|
\leq C_{N,k,\beta}\lambda^{\mu-N-k}.
\tag{6.2}
\]

If \(a_\lambda\sim\sum_{l\geq0}\lambda^{\mu-l}a_l\) with remainders satisfying (6.1) in the appropriate lower orders, then the coefficient at total degree \(\lambda^{\mu-q}\) in the bracket is \(\sum_{j+l=q}C_ja_l\).

**Proof.** The Morse coordinates are independent of \(\lambda\), so the transformed amplitude also satisfies (6.1). In (3.5), subtract the first \(N\) terms of the exponential. With \(q=\xi^TJ^{-1}\xi/2\), the Taylor remainder is \(E_N(q/\lambda)\). Taylor's integral formula implies

\[
|\partial_\lambda^k E_N(q/\lambda)|
\leq C_{N,k}\lambda^{-N-k}
\bigl(1+|q|\bigr)^{N+k},\qquad \lambda\geq1.
\tag{6.3}
\]

Indeed, write \(E_N(t)=t^N\int_0^1e^{-iut}(1-u)^{N-1}(-i)^N\,du/(N-1)!\) for \(N\geq1\), and differentiate; each \(\lambda\) derivative introduces \(\lambda^{-1}\) and at most one additional factor \(t\). For \(N=0\), differentiate \(e^{-it}\) directly. Since \(\lambda\geq1\), the resulting powers of \(|q|/\lambda\) are bounded as in (6.3).

Use the product rule and weighted Fourier \(L^1\) bounds for derivatives of the transformed amplitude. Each term has order \(\lambda^{\mu-N-k}\). Parameter derivatives act only on amplitudes and smooth factors, as in Theorem 5.1. The far integral is rapidly decreasing with all these derivatives: each fixed derivative creates only a fixed polynomial power of \(\lambda\), absorbed by sufficiently many integrations by parts. This proves (6.2). Substituting the amplitude expansion and collecting pairs \((j,l)\) proves the last assertion. ∎

This corollary concerns a large real parameter and compact integration variables. Symbol estimates in noncompact phase variables, including two-index classes with derivative losses, require additional statements.

## 7. Cancellation normal to a critical manifold

**Definition 7.1 (clean critical manifold).** A smooth submanifold \(C\subset U\) is clean for a real smooth function \(\phi\) if \(d\phi=0\) on \(C\) and

\[
\ker\phi''(x)=T_xC,\qquad x\in C.
\tag{7.1}
\]

At a critical point the Hessian is a bilinear form independent of coordinates. Condition (7.1) says that it induces a nondegenerate form on the normal quotient \(T_xU/T_xC\). Let \(r=d-\dim C\).

**Theorem 7.2 (clean stationary phase).** Suppose the critical set near the support of a compactly supported smooth amplitude is clean, and first localize the amplitude so that its support meets only one connected critical component \(C\). Then \(\phi|_C=c\) is constant. There are coefficients \(A_j\), with

\[
\int_U e^{i\lambda\phi}a\,dx
=e^{i\lambda c}\left(\frac{2\pi}{\lambda}\right)^{r/2}
e^{i\pi\sigma/4}
\left[\sum_{j<N}\lambda^{-j}A_j+O(\lambda^{-N})\right],
\tag{7.2}
\]

where \(\sigma\) is the signature of the normal Hessian, constant on that component. With the Euclidean metric used only to express the answer,

\[
A_0=\int_C
\frac{a(x)}{|\det H_\perp(x)|^{1/2}}\,d\operatorname{vol}_C(x).
\tag{7.3}
\]

Here \(H_\perp\) is the restriction of the Hessian to an orthonormal normal frame. Only the portion met by the support contributes. The formula also holds for an arbitrary smooth density in place of \(a\,dx\), using the quotient density described below. Multiple components contribute separate terms of the form (7.2). For smooth compact parameter families with fixed adapted clean charts, common compact coordinate supports, uniformly invertible normal Hessians, and a positive gradient lower bound on the remaining support, the normalized remainder has the parameter and symbol estimates of Theorem 5.1 and Corollary 6.1. These are the same uniform localization requirements as in the isolated case.

**Proof.** Appendix A.5 proves the coordinate and quotient-density assertions, and A.6 supplies the finite localization, including zero normal dimension. Since \(d\phi=0\) on \(C\), its restriction is locally constant and hence constant on the connected component. Choose coordinates \((y,z)\) with \(C=\{z=0\}\). The normal Hessian in the \(z\) variables is invertible. Apply Lemma 4.1 to those variables with \(y\) as a parameter. This gives \(\phi=c+z^TJz/2\) in new coordinates. Use a partition of unity on the compact part of the support met by \(C\), and Proposition 2.1 away from \(C\).

In each chart apply Theorem 3.2 to the normal integral and then integrate the coefficients in \(y\). The uniform remainder estimate can be integrated because the tangential support is fixed and compact. The leading coefficient is the original density on \(U\) divided by the density on the normal quotient whose coordinate expression is \(|\det H_\perp|^{1/2}|dz|\).

To check independence, change a normal frame by a matrix \(B\). The Hessian changes to \(B^TH_\perp B\), so its determinant square root changes by \(|\det B|\), exactly the density transformation factor. In arbitrary adapted coordinates, if the original density is \(m(y,z)|dy\,dz|\), the leading density on \(C\) is \(m(y,0)|\det\phi_{zz}''(y,0)|^{-1/2}|dy|\). Changing the transverse complement does not change the induced normal-quotient form, since the Hessian annihilates \(T C\); the density transformation in the exact sequence \(0\to T C\to T U|_C\to T U|_C/T C\to0\) cancels the normal determinant factor. Thus dividing the ambient density by this normal density gives a well-defined density on \(C\). In orthonormal frames for the Euclidean metric this is (7.3). The same calculation proves the arbitrary-density assertion. The parameter and symbol estimates follow chart by chart from the already proved estimates, using the finite partition and compact tangential integration in A.6. Apply the parameter Morse lemma to \(z\) with \((y,s)\) as parameter; the critical value is independent of \(y\) on each connected critical component. This proof does not invoke a later Fourier-integral composition theorem. ∎

The decay power depends on the normal dimension. If there are \(e\) critical directions among \(d\) variables, the power is \(\lambda^{-(d-e)/2}\). The extra factor \(\lambda^{e/2}\), relative to an isolated point, is the analytic origin of the excess correction in clean Fourier-integral composition.

## 8. Three models worth remembering

**An indefinite critical point.** Let \(\phi(x,y)=x^2-3y^2/2\), and let \(a\) be smooth and compactly supported near zero. The Hessian is \(\operatorname{diag}(2,-3)\), with determinant \(-6\) and signature zero. Therefore

\[
I(\lambda)=\frac{2\pi}{\lambda\sqrt6}
\left[a(0,0)+\frac{i}{2\lambda}
\left(\tfrac12\partial_x^2-\tfrac13\partial_y^2\right)a(0,0)
+O(\lambda^{-2})\right].
\]

Opposite signs cancel the signature factor, while the determinant remains in the size.

**A stationary line.** For \(\phi(x,y,z)=(x^2-y^2)/2\), the critical set is \(x=y=0\), with two normal directions. For compactly supported \(a\),

\[
I(\lambda)=\frac{2\pi}{\lambda}
\left[\int_{\mathbb R}a(0,0,z)\,dz+O(\lambda^{-1})\right].
\]

There is no cancellation along the line.

**Two critical points approaching each other.** Let \(\phi_t(x)=x^3/3-tx\). For \(t>0\), the critical points are \(\pm\sqrt t\), with Hessians \(\pm2\sqrt t\). For \(t\) in a compact interval bounded away from zero, an amplitude supported near the two points has leading term

\[
\left(\frac{2\pi}{\lambda}\right)^{1/2}
\frac1{(2\sqrt t)^{1/2}}
\left[
a(\sqrt t,t)e^{-2i\lambda t^{3/2}/3+i\pi/4}
+a(-\sqrt t,t)e^{2i\lambda t^{3/2}/3-i\pi/4}
\right].
\]

The stated remainder is \(O(\lambda^{-3/2})\) uniformly on that interval. As \(t\downarrow0\), the Hessians degenerate and this expansion loses uniformity. A different scaling is needed at the collision.

## 9. Exercises with complete solutions

**Exercise 9.1 (first correction; introductory).** Let \(\chi\in C_c^\infty(\mathbb R)\) be one near zero and supported sufficiently close to zero. For fixed real \(\kappa\), find the expansion through order \(\lambda^{-1}\) inside the stationary-phase bracket for

\[
\int e^{i\lambda(x^2/2+\kappa x^4/4)}\chi(x)\,dx.
\]

**Solution.** Near zero set \(z=x\sqrt{1+\kappa x^2/2}\). This is a valid smooth coordinate with \(z=x+\kappa x^3/4+O(x^5)\) and inverse \(x=z-\kappa z^3/4+O(z^5)\). The transformed amplitude is \(b(z)=1-3\kappa z^2/4+O(z^4)\) near zero. Thus \(b(0)=1\) and \(b''(0)=-3\kappa/2\). Formula (3.3) gives

\[
\left(\frac{2\pi}{\lambda}\right)^{1/2}e^{i\pi/4}
\left[1-\frac{3i\kappa}{4\lambda}+O(\lambda^{-2})\right].
\]

Shrinking the support ensures that \(x(1+\kappa x^2)=0\) has only the critical point zero there, including when \(\kappa<0\).

**Exercise 9.2 (parameter derivatives; intermediate).** For \(\phi(x,t)=t+x^2/2\) and a fixed amplitude \(\chi\) equal to one near zero, explain why the \(t\) derivative of the integral need not be \(O(\lambda^{-1/2})\), even though the integral is of that order.

**Solution.** The integral is \(e^{i\lambda t}J(\lambda)\), where \(J(\lambda)\sim(2\pi/\lambda)^{1/2}e^{i\pi/4}\). Its \(t\) derivative is \(i\lambda e^{i\lambda t}J(\lambda)\), of size \(\lambda^{1/2}\). Removing \(e^{i\lambda t}\) leaves a function independent of \(t\). This is why the normalized remainder, rather than the original integral, has uniform parameter estimates of the same order.

**Exercise 9.3 (failure of uniform nondegeneracy; intermediate).** Let \(\chi\geq0\) be smooth, compactly supported, with positive integral. Show that

\[
\int e^{i\lambda t x^2/2}\chi(x)\,dx
\]

cannot have a bound \(C\lambda^{-1/2}\) with \(C\) independent of \(0<t\leq1\).

**Solution.** Choose \(t=\lambda^{-2}\). The phase factor converges uniformly to one on the support, so the integral converges to \(\int\chi>0\). The proposed bound tends to zero. Each fixed positive \(t\) has a nondegenerate Hessian, but its inverse and determinant factor are not uniformly bounded as \(t\downarrow0\).

**Exercise 9.4 (clean density; advanced).** On \(\mathbb R^2\), take \(\phi(x,y)=x^2h(y)/2\), with smooth \(h>0\) near the compact support of \(a\). Determine the leading term, and recover it by the coordinate change \(z=x\sqrt{h(y)}\).

**Solution.** The critical set near the support is \(x=0\); the normal Hessian is \(h(y)\), with signature one. Thus the leading term is

\[
e^{i\pi/4}\left(\frac{2\pi}{\lambda}\right)^{1/2}
\int a(0,y)h(y)^{-1/2}\,dy.
\]

The coordinate change has \(dx\,dy=h(y)^{-1/2}dz\,dy\); its phase is \(z^2/2\). The quadratic formula gives exactly the same density. The next error is \(O(\lambda^{-3/2})\), since \(h\) is bounded away from zero on the compact tangential support.

**Exercise 9.5 (an absent critical direction; advanced).** Let \(a\in C_c^\infty(\mathbb R^3)\) and \(\phi=(x^2-y^2)/2+z\). Compare its decay to the stationary-line example.

**Solution.** Now \(\partial_z\phi=1\), so there are no critical points. Repeated integration by parts in \(z\) gives

\[
I(\lambda)=(-1)^M(i\lambda)^{-M}
\int e^{i\lambda\phi}\partial_z^Ma\,dx\,dy\,dz,
\]

and hence \(I=O(\lambda^{-M})\) for every \(M\). A stationary quadratic part in two variables does not suffice when another integration variable has a nonzero phase derivative.

## Appendix A. The analytic prerequisites used in the proof

### A.1. Gaussian integral and Fourier inversion

The Schwartz space \(\mathcal S(\mathbb R^d)\) consists of smooth functions \(b\) for which \(x^\alpha\partial^\beta b\) is bounded for every pair of multi-indices. Equivalently, every \((1+|x|)^m|\partial^\beta b(x)|\) is bounded. One direction follows from \(|x^\alpha|\leq(1+|x|)^{|\alpha|}\). For the other use \(|x|\leq\sum_j|x_j|\) and expand the integer power of \(1+\sum_j|x_j|\) into finitely many monomials. The rectangular-shell decay estimate P18.3 now proves integrability of these functions and all their derivatives. The Fourier convention is that of Section 1.

First,
\[
\left(\int_{\mathbb R}e^{-x^2/2}\,dx\right)^2
=\int_{\mathbb R^2}e^{-(x^2+y^2)/2}\,dx\,dy
=2\pi\int_0^\infty e^{-r^2/2}r\,dr=2\pi.
\tag{A1}
\]
The absolute product Fubini theorem P18.4 and the complete polar exhaustion P21.5 justify these equalities and the limits of the bounded integrals. Rescaling gives the Gaussian integral at every positive real scale. For \(t>0\), define
\[
g_t(x)=(2\pi t)^{-d/2}e^{-|x|^2/(2t)}.
\]
Integration by parts in one variable gives the differential equation
\(\partial_{\xi_j}\widehat g_t=-t\xi_j\widehat g_t\).
Since \(\widehat g_t(0)=1\), solving these scalar equations gives
\[
\widehat g_t(\xi)=e^{-t|\xi|^2/2}.
\tag{A2}
\]
All integrations and differentiations have integrable Gaussian majorants.

If \(b\in\mathcal S\), repeated integration by parts shows
\[
\xi^\alpha\partial_\xi^\beta\widehat b(\xi)
=(-i)^{|\beta|}\,\widehat{D^\alpha(x^\beta b)}(\xi),
\qquad D_j=-i\partial_{x_j}.
\tag{A3}
\]
The functions on the right are bounded by the \(L^1\) norms of their integrands. Consequently \(\widehat b\) is also a Schwartz function and is integrable. Fubini and the positive Gaussian transform give
\[
(2\pi)^{-d}\int e^{ix\cdot\xi}e^{-t|\xi|^2/2}
       \widehat b(\xi)\,d\xi
=\int g_t(x-y)b(y)\,dy.
\tag{A4}
\]
For the left side, absolute integrability follows from
\(\|b\|_{L^1}\int e^{-t|\xi|^2/2}\,d\xi<\infty\).
For the right side, substitute \(y=x-\sqrt t\,z\). The resulting integrand is \(g_1(z)b(x-\sqrt t\,z)\), bounded by \(\|b\|_\infty g_1(z)\), and converges pointwise to \(g_1(z)b(x)\). On a fixed compact \(z\) box the convergence is uniform by continuity of \(b\); outside that box the Gaussian tail is uniformly small. Q1 therefore proves convergence of the integral to \(b(x)\). The left side tends, by the integrability of \(\widehat b\), to its undamped inverse transform. This proves Fourier inversion for every Schwartz function.

### A.2. Plancherel and the pairing calculation

For \(b,c\in\mathcal S\), insert the inversion formula for \(c\) into \(\int b\overline c\). The product of \(|b(x)|\) and \(|\widehat c(\xi)|\) is integrable on the product space. Hence
\[
\int b(x)\overline{c(x)}\,dx
=(2\pi)^{-d}\int\widehat b(\xi)\,
                  \overline{\widehat c(\xi)}\,d\xi.
\tag{A5}
\]
Taking \(c=b\) proves exactly the Plancherel identity needed below. No extension to arbitrary \(L^2\) functions is needed for this lesson.

The pairing step in (3.5) can also be performed before taking a distributional limit. Insert the inversion formula for \(b\) into
\(\int e^{i\lambda Q_H(x)}e^{-\varepsilon|x|^2/2}b(x)\,dx\).
For each \(\varepsilon>0\), Fubini is legitimate. Apply the damped Gaussian transform from Lemma 3.1 with Fourier variable \(-\xi\). Its matrix exponential has absolute value at most one, and its prefactor is bounded as \(\varepsilon\downarrow0\), because \(H\) is invertible. Dominated convergence against \(|\widehat b|\) then gives (3.5). On the original side, convergence follows from the compact support of \(b\). Thus only ordinary Gaussian integrals and the Schwartz inversion just proved are required.

For the distributional wording of Lemma 3.1, a bounded function \(f\) defines the continuous functional \(b\mapsto\int f b\) on \(\mathcal S\): choose any integer \(k>d/2\) and bound the absolute integral by \(\|f\|_\infty\int\langle x\rangle^{-2k}\,dx\) times \(\sup_x\langle x\rangle^{2k}|b(x)|\). Formula (A3) bounds every Schwartz seminorm of \(\widehat b\) by finitely many seminorms of \(b\), so the Fourier transform is continuous on \(\mathcal S\). Define its action on tempered distributions by transposition. The two dominated-convergence arguments in Lemma 3.1 then prove exactly the asserted identity in that dual space.

### A.3. The weighted estimate with its precise derivative count

First prove the integral Cauchy–Schwarz inequality in the setting used here. If continuous \(u,v\) have finite square integrals, then \(2|u\overline v|\leq |u|^2+|v|^2\) proves absolute convergence of their product. Set \(A=\int|u|^2\), \(B=\int|v|^2\), and \(C=\int u\overline v\). Positivity and linearity, first on compact boxes and then by the absolute tail limits P18.1–P18.2, give
\[
0\leq\int|u-zv|^2=A-2\operatorname{Re}(\overline z C)+|z|^2B.
\tag{A8}
\]
If \(B>0\), take \(z=C/B\) to obtain \(|C|^2\leq AB\). If \(B=0\) and \(C\neq0\), taking \(z=tC\) and \(t\to+\infty\) contradicts (A8); thus \(C=0\) and the same inequality holds.

Let \(N\geq0\), and let the integer \(\ell>d/2\). Apply this inequality to \(u(\xi)=\langle\xi\rangle^{-\ell}\) and \(v(\xi)=|\xi|^{2N}\langle\xi\rangle^\ell|\widehat b(\xi)|\). Both square integrals converge by P18.3 and the Schwartz bounds. Since \(|\xi|^{4N}\leq\langle\xi\rangle^{4N}\), it gives
\[
\int |\xi|^{2N}|\widehat b(\xi)|\,d\xi
\leq\left(\int\langle\xi\rangle^{-2\ell}\,d\xi\right)^{1/2}
 \left(\int\langle\xi\rangle^{4N+2\ell}
                   |\widehat b(\xi)|^2\,d\xi\right)^{1/2}.
\tag{A6}
\]
The first integral is finite by the rectangular-shell estimate P18.3 with exponent \(2\ell>d\), using the comparable weights \(\langle\xi\rangle=(1+|\xi|^2)^{1/2}\) and \(1+|\xi|\). No additional spherical integration theorem is used. Because \(2N+\ell\) is an integer, the multinomial expansion of
\((1+\xi_1^2+\cdots+\xi_d^2)^{2N+\ell}\)
is a finite sum of positive constants times \(|\xi^\alpha|^2\), with \(|\alpha|\leq2N+\ell\). Apply (A5) to \(D^\alpha b\), using
\(\widehat{D^\alpha b}=\xi^\alpha\widehat b\), and take square roots. This proves
\[
\int |\xi|^{2N}|\widehat b(\xi)|\,d\xi
\leq C_{d,N,\ell}
       \sum_{|\alpha|\leq2N+\ell}\|\partial^\alpha b\|_{L^2}.
\tag{A7}
\]
Here \(|K|\) denotes the outer measure \(m^*(K)\) of P19. For any \(\varepsilon>0\), cover \(K\) by open rectangles with sum of volumes at most \(m^*(K)+\varepsilon\); compactness gives a finite subcover with no larger sum. Their union is Jordan measurable by P20.3. For continuous \(u\) supported in \(K\), positivity, finite additivity and null-overlap subdivision give
\(\int|u|^2\leq\|u\|_\infty^2(m^*(K)+\varepsilon)\).
Let \(\varepsilon\downarrow0\). Thus on this fixed compact support each norm is bounded by
\(|K|^{1/2}\|\partial^\alpha b\|_\infty\), including when \(K\) itself is not a Jordan set.
The same argument applies after any fixed parameter or scale derivative. This proves the bound used in (3.4) and (6.2) with no derivative loss beyond their stated finite seminorms.

### A.4. Finite smooth cutoffs

Put \(h(t)=e^{-1/t}\) for \(t>0\), and \(h(t)=0\) for \(t\leq0\). Every right derivative is a polynomial in \(t^{-1}\) times \(e^{-1/t}\), which tends to zero at the origin: \(v^m e^{-v}\to0\) as \(v\to\infty\). The flatness and smoothness, including all derivatives at zero, are proved in P14.3. The function
\[
\theta(t)=\frac{h(t)}{h(t)+h(1-t)}
\]
is smooth, equals zero for \(t\leq0\) and one for \(t\geq1\). Composing it with affine functions of \(|x-x_0|^2\) gives a cutoff equal to one on a closed ball and supported in any prescribed larger ball.

Given a compact set covered by coordinate neighborhoods, choose finitely many such smaller balls that cover it, with cutoffs \(b_j\) supported in their assigned neighborhoods. On a neighborhood of the compact set, \(S=\sum_jb_j>0\). Choose a further cutoff \(\chi\), equal to one near the compact set, whose support lies where \(S>0\), using a finite cover by balls inside that open set. For example, if the associated cutoffs are \(c_k\), then \(1-\prod_k(1-c_k)\) provides such a \(\chi\). The functions \(\chi b_j/S\), extended by zero, form a smooth partition with sum one near the compact set. This gives the precise finite partitions used in Sections 5 and 7. With parameters in a compact set, perform the construction in the product coordinate neighborhoods; compactness keeps every derivative needed in a fixed estimate bounded.

### A.5. Hessians and quotient densities in full

A smooth \(k\)-dimensional submanifold means a subset with smooth adapted coordinate charts \((y,z)\) in which it is \(z=0\), \(y\in\mathbb R^k\), \(z\in\mathbb R^r\). This is the chart definition; no unproved constant-rank theorem is needed. At a critical point, the chain rule for a coordinate map \(F\) gives
\[
(\phi\circ F)''=F'^T\phi''F',
\]
because its other terms contain first derivatives of \(\phi\), which vanish. If \(\ker H=W=T_xC\), the rule
\(\overline H([v],[w])=H(v,w)\) is independent of the lifts, since \(H\) annihilates \(W\). If its pairing with every quotient vector vanishes, then \(v\in\ker H=W\); hence \(\overline H\) is nondegenerate.

An ordinary density on an \(n\)-dimensional vector space assigns a number to each ordered basis, with transformation rule
\(\mu(vB)=|\det B|\mu(v)\). We allow complex-valued amplitudes multiplying these ordinary densities. For a nondegenerate real symmetric form \(H\), define the positive density
\[
\nu_H(v_1,\ldots,v_n)=
\left|\det\bigl(H(v_i,v_j)\bigr)\right|^{1/2}.
\]
Indeed the matrix under a basis change is \(B^THB\), and determinant multiplication shows that its absolute square root is multiplied by \(|\det B|\). Only ordinary densities and this positive square root are used.

Let \(W\subset V\), let \(\mu\) be a density on \(V\), and let \(\nu\) be a positive density on \(V/W\). If \(t\) is a basis of \(W\), \(q\) a basis of \(V/W\), and \(v\) any lifts of \(q\), set
\[
(\mu/\nu)(t)=\frac{\mu(t,v)}{\nu(q)}.
\]
Changing lifts adds tangent vectors to \(v\); the combined change matrix is block upper triangular with identity diagonal, so it has determinant one. Changing \(q\) by \(B\) multiplies numerator and denominator by \(|\det B|\). Changing \(t\) by \(P\) multiplies the quotient by \(|\det P|\), exactly the density rule on \(W\). To justify the block determinant used here, expand the determinant by permutations: a nonzero term cannot send a lower row to an upper-block column because the lower-left block is zero; counting columns then forces each block to use its own columns, and the sum factors into the two block determinants. This proves lift and frame independence.

Apply this construction with \(V=T_xU\), \(W=T_xC\), and \(\nu=\nu_{\overline H}\). For ambient density \(m(y,z)|dy\,dz|\), its quotient is
\[
\frac{m(y,0)}{|\det\phi''_{zz}(y,0)|^{1/2}}\,|dy|.
\tag{A9}
\]
The \(z\) classes form a quotient basis and the \(y\) vectors a tangent basis, so this follows directly from the definition. The critical kernel condition makes the \(z\) block invertible.

Integration of a compactly supported density on \(C\) is defined with finitely many adapted charts and the cutoffs of A.4 restricted to \(C\). It is independent of these choices: refine two such partitions by their products. On each common chart overlap, the coordinate transition is a smooth diffeomorphism and P21.4 cancels the density factor with the absolute Jacobian in the integral. Finite additivity identifies both sums. A zero-dimensional compact support gives a finite sum of point values, since every point has a one-point chart and compactness gives a finite cover.

Finally, let \(T\) be the matrix of the tangent coordinate frame. Its Gram matrix \(T^TT\) is positive definite, since \(v^TT^TTv=|Tv|^2>0\) for \(v\neq0\). The orthogonal projection onto the tangent space is \(T(T^TT)^{-1}T^T\), smooth by P2. Project a fixed normal basis at one point using the complementary projection; linear independence persists nearby by the nonzero Gram determinant. Gram–Schmidt, with the positive square roots proved in P8 and the construction P9.4, gives a smooth orthonormal normal frame \(n\). In the combined frame \((T,n)\), the Gram matrix is block diagonal with blocks \(T^TT\) and the identity. Hence
\[
|\det(T,n)|=\sqrt{\det(T^TT)}.
\]
The Euclidean density restricted in this combined frame is therefore the induced tangent volume density. Dividing by \(\nu_{\overline H}(n)=|\det H_\perp|^{1/2}\) proves (7.3). The empty tangent or normal blocks obey the dimension-zero conventions stated in Section 1. This also proves that the Euclidean expression represents the intrinsic quotient (A9).

The ordinary density and exact-sequence viewpoint is described in the freely posted Bates–Weinstein Appendix A. The transformation and integration arguments required here have been given in full.

### A.6. Finite clean localization and its uniform bounds

Intersect the critical set with the compact amplitude support \(K\). This is compact: it is the zero set of the continuous gradient inside \(K\). At each point choose a smaller adapted product chart with connected tangent zero section and precompact closure in a larger adapted chart. Its critical points form that connected zero section, so the chart meets only one critical component. Compactness gives finitely many such smaller charts covering the critical subset. In particular only finitely many critical components meet \(K\), and the amplitude may be split among them.

On the critical set, the derivative in every tangent direction of \(\phi|_C\) is zero. In a small convex tangent coordinate box, the fundamental theorem along each segment proves constancy. Thus the restriction is locally constant. On a connected component the set on which it equals a chosen value and its complement are both open; connectedness forces the complement to be empty. The same reasoning applies to the locally constant normal signature furnished by the signed Morse reduction and P5.

Before constructing cutoffs, refine this cover by the parameter Morse charts for the normal variables, and choose smaller precompact charts inside them. Compactness again gives a finite cover. Construct the finite cutoffs of A.4 in these charts, with their sum one near the compact critical subset. Subtract their sum from one on the amplitude support. The remaining amplitude has compact support disjoint from the critical set, so continuity and the extreme-value theorem give a positive minimum of \(|\nabla\phi|\) there. Proposition 2.1 applies to that remaining part.

On each near chart use the resulting normal Morse coordinates, with \(y\) as parameter. The supports chosen in the preceding paragraph make each localized amplitude and its transformed version compactly supported inside its respective chart; P21.4 justifies substitution and smooth extension by zero. Compact Fubini P17.5 orders the tangential and normal integrals. Theorem 3.2 gives a normal remainder bounded by a constant times \(\lambda^{-N}\), uniformly in \(y\) on a fixed compact set. Its tangential integral is bounded by that supremum times the volume of a containing tangent rectangle. The same argument integrates every coefficient and every fixed parameter derivative, using P12.7. A.5 identifies the leading coefficient after summing the cutoffs. Equality of higher coefficients under different cutoffs follows from the subtraction-and-limit argument in Section 5, applied to the localized component.

If \(r=0\), the normal integral is evaluation, the quadratic prefactor is one, and the phase is constant on each such chart. Its expansion is exact with \(A_j=0\) for \(j>0\); any far contribution is rapidly decreasing. No positive-dimensional Fresnel calculation is being applied to this case.

For the families in Theorem 7.2, use the stipulated smooth adapted charts over compact parameter neighborhoods, common compact coordinate supports, and the stated normal-inverse and far-gradient bounds. Treat \((y,s)\) as the parameter in M1. M2 bounds inverse-coordinate derivatives on their compact images. Finite parameter covers, products of the cutoffs of A.4, and finite maxima of the bounds give uniform constants; take the union of the finitely many amplitude seminorm requirements. The critical value \(c(s)\) is independent of \(y\) on the component just proved constant. Remove \(e^{i\lambda c(s)}\) before applying the differentiated estimate. Corollary 6.1 then gives each scale derivative with its stated decrease in order; compact tangential integration preserves the bound. This proves all the uniformity assertions of the clean theorem without importing composition of Fourier integral operators.

## References

- [Guillemin–Sternberg] Victor Guillemin and Shlomo Sternberg, *Semi-classical Analysis*, author draft, 13 January 2010, Chapter 14 and §8.14. [Online reading](https://math.mit.edu/~vwg/semiclassGuilleminSternberg.pdf).
- [Bates–Weinstein] Sean Bates and Alan Weinstein, *Lectures on the Geometry of Quantization*, author-posted draft, Appendix A (ordinary densities and the exact sequence) and Appendix B (nonstationary integration and the invariant leading coefficient). The Gaussian calculation used here is proved locally from the independently checked free route in Q2 and Q6. [Online reading](https://math.berkeley.edu/~alanw/GofQ.pdf).
- [Lebl] Jiří Lebl, *Basic Analysis I–II*, version 6.3, 15 May 2026, selected elementary prerequisites and §§8.3–8.6 and 10.7. [Author edition](https://www.jirka.org/ra/). The exact programme versions and completed prerequisite proofs are bound in this receiving edition.

*Retained original text by GPT-6.1 Sol (OpenAI), Ultra, September 2026, with its 3 October 2026 analytic revision: CC0. Free-source proof reconciliation and additional prerequisite, density and localization arguments by GPT-6 Astra (OpenAI), Ultra, 4 October 2026. This receiving edition is offered under CC BY-SA 4.0; the retained CC0 component keeps its original terms, and linked prerequisite components retain their own notices. Self-checked by the writing AI.*
