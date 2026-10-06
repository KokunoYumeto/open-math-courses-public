# Stationary phase and critical manifolds

A rapidly oscillating integral cancels where its phase changes to first order. Near a critical point, the quadratic part controls the size and the complex phase of the answer. When critical points form a manifold, cancellation acts only in its normal directions. This lesson develops those three mechanisms with estimates that remain useful when the phase and amplitude vary.

We assume multivariable calculus, the inverse and implicit function theorems, smooth partitions of unity, and the Fourier inversion and Plancherel conventions in Fourier transforms, finite spectra and convex separation. The uniform Fourier multiplier estimate in Quadratic Fourier multipliers at a moving scale supplies one estimate below. Basic references are [Hörmander I] and [Guillemin–Sternberg]. The proofs here use only the stated prerequisites.

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

For positive real \(z\), the Gaussian integral and differentiation with respect to \(\xi\) prove (3.2). Both sides are holomorphic in the connected right half-plane; dominated differentiation on compact subsets and the identity theorem extend the identity there. Choose the square root positive on the positive real axis.

For an eigenvalue \(h_j\neq0\), use \(z=\varepsilon-i\lambda h_j\). As \(\varepsilon\downarrow0\), its inverse square root tends to \((\lambda|h_j|)^{-1/2}e^{i\pi\operatorname{sign}(h_j)/4}\). The exponential on the right of (3.2) has absolute value at most one for real \(\xi\), so dominated convergence against Schwartz functions proves the transformed limit. The original damped functions also converge as tempered distributions, since their absolute values are at most one. Multiply the scalar formulas. ∎

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

For \(N=0\) the sum is empty and the matrix factor is one.

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

This is Cauchy–Schwarz with the integrable weight \(\langle\xi\rangle^{-2\ell}\), then Plancherel. It is precisely the Fourier estimate used in Theorem 2.1 of Quadratic Fourier multipliers at a moving scale. The fixed support bounds each \(L^2\) norm by its supremum times the square root of the support volume. ∎

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

**Proof.** The implicit function theorem applied to \(\phi_x'\) gives \(x_c(s)\). Translate this point to zero. Make a fixed real linear change of variables so that the first diagonal entry of the Hessian is nonzero. Such a direction exists because a symmetric form with zero quadratic value on every vector is zero, whereas this Hessian is invertible.

Write \(x=(x_1,x')\). The implicit function theorem gives \(x_1=h(x',s)\) solving \(\partial_{x_1}\phi=0\). Taylor's formula with integral remainder gives

\[
\phi(h+v,x',s)=g(x',s)+\tfrac12v^2A(v,x',s),
\qquad
A=2\int_0^1(1-t)\partial_{x_1}^2\phi(h+tv,x',s)\,dt.
\]

The smooth function \(A\) is nonzero near the origin. Its sign \(\sigma\) is fixed there. The coordinate \(z_1=v|A|^{1/2}\) is valid by the inverse function theorem and changes this expression into \(g(x',s)+\sigma z_1^2/2\).

The Hessian of \(g\) at its critical point is the Schur complement of the first pivot in the original Hessian. Block elimination shows that its determinant is the original determinant divided by that pivot, so it is invertible. Induct on the remaining variables, keeping \(s\) as a parameter. This proves (4.1).

Differentiating (4.1) twice at \(z=0\) gives \(F_z'^THF_z'=J\), because the first derivative of \(\phi\) vanishes there. Congruence preserves the numbers of positive and negative directions. Taking absolute determinants gives (4.2). ∎

Every coordinate change and its inverse has bounded derivatives on a sufficiently small fixed compact neighborhood. This is the quantitative fact needed below; the argument does not claim a neighborhood of fixed size when the Hessian approaches singularity.

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

**Proof.** Choose a smooth cutoff equal to one on a fixed smaller neighborhood of \(x_c(s)\), and split the amplitude into its near and far parts. Proposition 2.1 makes the far integral smaller than every inverse power of \(\lambda\), with any fixed number of parameter derivatives. Multiplying it by \(e^{-i\lambda c(s)}\lambda^{d/2}\) costs only finitely many powers, which that proposition can absorb.

For the near part use Lemma 4.1 and define

\[
b(z,s)=a(F(z,s),s)|\det F_z'(z,s)|
\]

with the cutoff included. Extend \(b\) by zero outside the fixed coordinate neighborhood. Theorem 3.2 with \(H=J\) gives (5.1) with

\[
C_ja(s)=\frac{|\det H(s)|^{1/2}}{j!}
\left(\frac i2\right)^j\Delta_J^jb(0,s).
\tag{5.3}
\]

The cutoff is one near zero, so its derivatives do not enter these coefficients. The chain rule shows that no more than \(2j\) derivatives of \(a\) in \(x\) occur. Formula (4.2) gives \(C_0a=a(x_c,s)\).

After the critical value has been factored out, the quadratic phase and \(J\) do not depend on \(s\). Thus parameter derivatives act only on \(b\) and the smooth determinant factor. Apply (3.4) to those derivatives. For the near integral it is enough to bound the corresponding mixed derivatives of \(b\) through order \(2N+\ell+r\); the far integral may require a larger finite seminorm. This proves (5.2).

Although (5.3) uses a coordinate choice, the coefficients do not depend on that choice. Two such expansions approximate the same normalized integral. Their first different coefficient, multiplied by its power of \(\lambda\) and followed by \(\lambda\to\infty\), would have to be both zero and nonzero. Induction on \(j\) proves equality of every coefficient. ∎

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

**Theorem 7.2 (clean stationary phase).** Suppose the critical set near the support of a compactly supported smooth amplitude is clean, and work on one connected critical component \(C\). Then \(\phi|_C=c\) is constant. There are coefficients \(A_j\), with

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

Here \(H_\perp\) is the restriction of the Hessian to an orthonormal normal frame. Only the portion met by the support contributes. The formula also holds for an arbitrary smooth density in place of \(a\,dx\), using the quotient density described below. Multiple components contribute separate terms of the form (7.2). For smooth compact parameter families with fixed clean charts and uniformly invertible normal Hessians, the normalized remainder has the parameter and symbol estimates of Theorem 5.1 and Corollary 6.1.

**Proof.** Since \(d\phi=0\) on \(C\), its restriction is locally constant and hence constant on the connected component. Choose coordinates \((y,z)\) with \(C=\{z=0\}\). The normal Hessian in the \(z\) variables is invertible. Apply Lemma 4.1 to those variables with \(y\) as a parameter. This gives \(\phi=c+z^TJz/2\) in new coordinates. Use a partition of unity on the compact part of the support met by \(C\), and Proposition 2.1 away from \(C\).

In each chart apply Theorem 3.2 to the normal integral and then integrate the coefficients in \(y\). The uniform remainder estimate can be integrated because the tangential support is fixed and compact. The leading coefficient is the original density on \(U\) divided by the density on the normal quotient whose coordinate expression is \(|\det H_\perp|^{1/2}|dz|\).

To check independence, change a normal frame by a matrix \(B\). The Hessian changes to \(B^TH_\perp B\), so its determinant square root changes by \(|\det B|\), exactly the density transformation factor. Dividing the ambient density by this normal density gives a well-defined density on \(C\). In orthonormal frames for the Euclidean metric this is (7.3). The same calculation proves the arbitrary-density assertion. The parameter and symbol estimates follow chart by chart from the already proved estimates, using a finite partition of unity. ∎

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

## References

- [Guillemin–Sternberg] Victor Guillemin and Shlomo Sternberg, *Semi-classical Analysis*, lecture notes. [Online reading](https://math.mit.edu/~vwg/semiclassGuilleminSternberg.pdf).
- [Hörmander I] Lars Hörmander, *The Analysis of Linear Partial Differential Operators I: Distribution Theory and Fourier Analysis*, Springer, 1983.

*Written by GPT-6.1 Sol (OpenAI), Ultra, September 2026. Self-checked by the writing AI. Original text: public domain (CC0).*
