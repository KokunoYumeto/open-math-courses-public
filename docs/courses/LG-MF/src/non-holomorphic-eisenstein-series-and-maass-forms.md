# Non-holomorphic Eisenstein series and Maass forms

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

A holomorphic modular form satisfies a first-order differential equation. Here we replace holomorphy by an eigenvalue equation for the hyperbolic Laplacian. Averaging a power of the height over the modular group gives an Eisenstein series. Its Fourier coefficients involve Bessel functions; a theta integral explains its continuation and reflection symmetry.

We use the hyperbolic measure from The Petersson inner product and Poincaré series, and the real Poisson and Gaussian formulas from Theta functions and sums of squares, equations (1.3)–(1.5). All sums and integrals below are justified in their initial domains before they are continued.

## 1. The Laplacian and the defining series

Write \(z=x+iy\), \(y>0\), and put
\[
\Delta=-y^2(\partial_x^2+\partial_y^2),\qquad
d\mu=\frac{dx\,dy}{y^2}.
\tag{1.1}
\]
For a real determinant-one matrix \(\gamma\), its holomorphic fractional transformation has
\[
\gamma'(z)=(cz+d)^{-2},\qquad
\operatorname{Im}(\gamma z)=y|cz+d|^{-2}.
\]
The ordinary chain rule for a holomorphic map \(w=u+iv\) gives
\[
(\partial_x^2+\partial_y^2)(f\circ w)
=|w'(z)|^2(f_{uu}+f_{vv})\circ w.
\tag{1.2}
\]
Indeed \(u,v\) are harmonic, their gradients are orthogonal and have equal squared length \(|w'|^2\). Multiplying (1.2) by \(-y^2\) proves
\[
\Delta(f\circ\gamma)=(\Delta f)\circ\gamma.
\tag{1.3}
\]
Also \(\Delta y^s=-s(s-1)y^s\), where positive real numbers are raised to complex powers using their real logarithms.

Let
\[
\Gamma=SL_2(\mathbb Z),\qquad
\Gamma_\infty=\left\{\pm\begin{pmatrix}1&b\\0&1\end{pmatrix}:b\in\mathbb Z\right\}.
\]
For \(\operatorname{Re}s>1\) define
\[
E(z,s)=\sum_{\gamma\in\Gamma_\infty\backslash\Gamma}
       \operatorname{Im}(\gamma z)^s
=\frac12\sum_{\substack{(c,d)\in\mathbb Z^2\\\gcd(c,d)=1}}
       \frac{y^s}{|cz+d|^{2s}}.
\tag{1.4}
\]
The factor \(1/2\) identifies \((c,d)\) and \((-c,-d)\). To check the equality, a primitive row can be completed to a determinant-one matrix by Bezout's identity. Two completions differ by adding an integer multiple of the bottom row to the top row. Left multiplication by \(\Gamma_\infty\) performs exactly these operations, together with simultaneous negation.

**Theorem 1.1 (convergence and eigenfunction).** On \(\mathfrak H\times\{\operatorname{Re}s>1\}\), the series \(E\) is locally uniformly absolutely convergent, is holomorphic in \(s\), and is smooth in \(z\). All its fixed-order \(z\)-derivatives converge locally uniformly. It is \(\Gamma\)-invariant and satisfies
\[
\Delta E(z,s)=s(1-s)E(z,s).
\tag{1.5}
\]

**Proof.** On a compact set of \(z\)-values, the positive quadratic form
\[
|cz+d|^2=(cx+d)^2+c^2y^2
\]
is at least \(a(c^2+d^2)\) for one \(a>0\), uniformly on the compact set. There are \(O(R)\) integer pairs with \(\max(|c|,|d|)=R\). Thus for \(\operatorname{Re}s\ge1+\epsilon\), the sum is dominated by a constant times
\(\sum_{R\ge1}R^{1-2(1+\epsilon)}\), which converges.

Differentiation does not require a larger half-plane. If \(h=y^s|cz+d|^{-2s}\), differentiation of \(\log h\) introduces \(s/y\) and multiples of
\[
\frac{c}{cz+d},\qquad \frac{c}{c\bar z+d}.
\]
Their absolute values are at most \(1/y\). Further derivatives have the same property with higher powers of \(1/y\). Induction gives
\[
|\partial_x^\alpha\partial_y^\beta h|
\le C_{\alpha,\beta,K}|h|
\]
on any compact set \(K\) of \(z,s\)-values in the initial domain. The preceding summable majorant therefore applies to every fixed derivative. Uniform convergence proves smoothness and permits termwise application of \(\Delta\). Holomorphy in \(s\) follows from local uniform convergence of the holomorphic summands.

Right multiplication permutes the left cosets \(\Gamma_\infty\backslash\Gamma\), proving invariance. Each summand is an eigenfunction by (1.3) and the calculation for \(y^s\). Summing gives (1.5). \(\square\)

Separate every nonzero integer vector into its positive integer content and its primitive vector. Absolute convergence gives
\[
\zeta(2s)E(z,s)
=\frac12\sum_{(m,n)\ne(0,0)}\frac{y^s}{|mz+n|^{2s}}.
\tag{1.6}
\]
Here \(\zeta(w)=\sum_{r\ge1}r^{-w}\) initially for \(\operatorname{Re}w>1\). Its absolutely convergent Euler product is nonzero there: the logarithms of \((1-p^{-w})^{-1}\) form an absolutely convergent series. This justifies division by \(\zeta(2s)\) in the initial domain.

## 2. Fourier coefficients and the Bessel integral

For \(u>0\) and \(\nu\in\mathbb C\), define
\[
\begin{aligned}
K_\nu(u)
&=\frac12\int_0^\infty
       e^{-u(t+t^{-1})/2}t^\nu\,\frac{dt}{t}\\
&=\int_0^\infty e^{-u\cosh v}\cosh(\nu v)\,dv.
\end{aligned}
\tag{2.1}
\]
The second equality follows by \(t=e^v\), then pairing \(v\) with \(-v\). The exponential dominates every fixed power of \(t\), \(t^{-1}\), and \(\log t\) at both ends. Consequently \(K_\nu(u)\) is entire in \(\nu\), smooth in \(u\), and \(K_{-\nu}=K_\nu\).

For \(\nu\) in a compact set, and for every fixed number of \(u\)-derivatives, there are constants \(C,A\) such that, for \(u\ge1\),
\[
|\partial_u^j K_\nu(u)|\le C(1+u)^A e^{-u}.
\tag{2.2}
\]
For example, use \(\cosh v\ge1+v^2/2\), absorb the extra factors \((\cosh v)^j\) into a fixed exponential in \(v\), and integrate the resulting Gaussian bound. This estimate will justify all Fourier-series continuations.

**Lemma 2.1 (the Fourier integral).** If \(\operatorname{Re}s>1/2\), \(y>0\), and \(r\in\mathbb R\), then
\[
I_s(r,y):=\int_{\mathbb R}(x^2+y^2)^{-s}e^{-2\pi irx}\,dx
=\begin{cases}
\displaystyle
\frac{\sqrt\pi\,\Gamma(s-\tfrac12)}{\Gamma(s)}y^{1-2s},
&r=0,\\[6pt]
\displaystyle
\frac{2\pi^s}{\Gamma(s)}
\left(\frac{|r|}{y}\right)^{s-1/2}
K_{s-1/2}(2\pi|r|y),
&r\ne0.
\end{cases}
\tag{2.3}
\]

**Proof.** The Gamma integral gives
\[
(x^2+y^2)^{-s}
=\frac1{\Gamma(s)}\int_0^\infty
 t^{s-1}e^{-t(x^2+y^2)}\,dt.
\]
The absolute double integral after integration in \(x\) is a constant times
\(\int_0^\infty t^{\operatorname{Re}s-3/2}e^{-y^2t}\,dt\); it is finite precisely in the stated domain. Fubini and the Gaussian transform give
\[
I_s(r,y)=\frac{\sqrt\pi}{\Gamma(s)}
\int_0^\infty
 t^{s-3/2}e^{-y^2t-\pi^2r^2/t}\,dt.
\tag{2.4}
\]
For \(r=0\), substitution \(v=y^2t\) proves the first case. For \(r\ne0\), substitute \(t=(\pi|r|/y)v\) and compare with (2.1). The factor outside the integral is
\(\pi^s(|r|/y)^{s-1/2}/\Gamma(s)\), and the integral is twice \(K_{s-1/2}(2\pi|r|y)\). \(\square\)

Set \(\sigma_a(n)=\sum_{d\mid n,\ d>0}d^a\).

**Theorem 2.2 (the Fourier expansion).** For \(\operatorname{Re}s>1\),
\[
\begin{aligned}
E(z,s)
&=y^s+\phi(s)y^{1-s}\\
&\quad+\sum_{r\ne0}c_r(s)\sqrt y\,
 K_{s-1/2}(2\pi|r|y)e^{2\pi irx},
\end{aligned}
\tag{2.5}
\]
where
\[
\phi(s)=
\frac{\sqrt\pi\,\Gamma(s-\tfrac12)\zeta(2s-1)}
     {\Gamma(s)\zeta(2s)},\qquad
c_r(s)=
\frac{2\pi^s|r|^{s-1/2}\sigma_{1-2s}(|r|)}
     {\Gamma(s)\zeta(2s)}.
\tag{2.6}
\]

**Proof.** Compute the \(r\)-th Fourier coefficient of (1.6) by integrating over \(0\le x\le1\). The terms \(m=0\) contribute \(\zeta(2s)y^s\) when \(r=0\), and zero otherwise. Pair \((m,n)\) with \((-m,-n)\) to leave \(m>0\).

For fixed \(m\), write \(n=a+m\ell\), \(0\le a<m\). Factoring out \(m^{-2s}\) and putting \(v=x+a/m+\ell\), the intervals indexed by \(\ell\) cover the real line. Their combined contribution is
\[
y^s m^{-2s}
\sum_{a=0}^{m-1}e^{2\pi ira/m}I_s(r,y).
\tag{2.7}
\]
All these integral and sum interchanges are absolute: after dropping the Fourier exponential their total is the integral of the absolutely convergent lattice sum on a compact horizontal interval.

The finite geometric sum in (2.7) equals \(m\) if \(m\mid r\), and zero otherwise. For \(r=0\), all \(m\) occur, giving
\[
y^s\zeta(2s-1)I_s(0,y).
\]
For \(r\ne0\), only the positive divisors of \(|r|\) occur, giving
\(y^s\sigma_{1-2s}(|r|)I_s(r,y)\).
Substitute (2.3) and divide by \(\zeta(2s)\). This proves the claimed coefficients.

Estimate (2.2) and a polynomial bound for the divisor sum show that the displayed Fourier series and all its fixed \(z\)-derivatives converge uniformly on compact subsets. It has the coefficients just computed. Uniqueness of Fourier coefficients, or Fourier inversion for the smooth periodic function of \(x\), identifies it with \(E\). \(\square\)

The completed series is
\[
E^*(z,s)=\pi^{-s}\Gamma(s)\zeta(2s)E(z,s).
\tag{2.8}
\]
Its nonconstant coefficient is particularly simple:
\[
2|r|^{s-1/2}\sigma_{1-2s}(|r|)
\sqrt y\,K_{s-1/2}(2\pi|r|y).
\tag{2.9}
\]
Neither \(\Gamma(s)\) nor a zeta denominator remains in (2.9).

## 3. A theta integral, continuation and the residue

Define the positive quadratic form and its theta function by
\[
Q_z(m,n)=\frac{|mz+n|^2}{y},\qquad
\Theta_z(t)=\sum_{(m,n)\in\mathbb Z^2}e^{-\pi tQ_z(m,n)}
\quad(t>0).
\tag{3.1}
\]
In the coordinates \((m,n)\), its matrix is
\[
A_z=\frac1y
\begin{pmatrix}|z|^2&x\\x&1\end{pmatrix},
\qquad \det A_z=1.
\tag{3.2}
\]

**Lemma 3.1 (theta inversion).** One has
\[
\Theta_z(t)=t^{-1}\Theta_z(1/t).
\tag{3.3}
\]
Moreover, \(\Theta_z(t)-1\) and all its fixed \(z\)-derivatives decay exponentially as \(t\to\infty\), uniformly on compact subsets of \(\mathfrak H\).

**Proof.** Apply the one-dimensional Poisson formula in each coordinate to a Schwartz function on \(\mathbb R^2\). The iterated sums and integrals are absolute for a positive Gaussian; its partial transforms are also Gaussians. Diagonalizing a positive real symmetric matrix \(A\) by an orthogonal change of variables and using the one-dimensional Gaussian transform gives
\[
\widehat{e^{-\pi t v^tAv}}(\xi)
=t^{-1}(\det A)^{-1/2}e^{-\pi \xi^tA^{-1}\xi/t}.
\tag{3.4}
\]
This uses exactly the transform convention \(e^{-2\pi i v\cdot\xi}\).

For a symmetric \(2\)-by-\(2\) matrix of determinant one,
\[
A^{-1}=J^tAJ,\qquad
J=\begin{pmatrix}0&-1\\1&0\end{pmatrix}.
\]
Poisson summation and the bijection \(\xi\mapsto J\xi\) of \(\mathbb Z^2\) therefore prove (3.3) for \(A=A_z\).

On a compact \(z\)-set, \(Q_z(v)\ge a|v|^2\) for \(a>0\). Each derivative of a nonconstant summand adds a polynomial in \(t,m,n\). For \(t\ge1\), these polynomial factors can be absorbed into
\(C e^{-\pi a t|v|^2/2}\). Summing over \(v\ne0\), and splitting off another fixed part of this Gaussian, gives \(C'e^{-bt}\). This proves the last assertion. \(\square\)

For \(\operatorname{Re}s>1\), the Gamma integral and (1.6) yield
\[
E^*(z,s)=\frac12\int_0^\infty
(\Theta_z(t)-1)t^{s-1}\,dt.
\tag{3.5}
\]
The absolute interchange follows either from the convergent lattice sum or from (3.3) near zero and the exponential bound near infinity.

**Theorem 3.2 (continuation and reflection).** The completion extends meromorphically to all \(s\in\mathbb C\), has only simple poles at \(0,1\), and satisfies
\[
E^*(z,s)=E^*(z,1-s),\qquad
\operatorname*{Res}_{s=1}E^*(z,s)=\frac12,\qquad
\operatorname*{Res}_{s=0}E^*(z,s)=-\frac12.
\tag{3.6}
\]
It is smooth in \(z\) away from those poles.

**Proof.** Split (3.5) at \(1\). In the integral below \(1\), insert
\[
\Theta_z(t)-1
=t^{-1}(\Theta_z(1/t)-1)+t^{-1}-1
\]
and change variables \(t=1/u\) in the first part. The result is
\[
\begin{aligned}
E^*(z,s)
=\frac12\left\{
\frac1{s-1}-\frac1s+
\int_1^\infty(\Theta_z(t)-1)
\bigl(t^{s-1}+t^{-s}\bigr)\,dt
\right\}.
\end{aligned}
\tag{3.7}
\]
The integral is entire in \(s\). On every compact set of \(s,z\)-values, its derivatives in \(s\) add powers of \(\log t\), and its derivatives in \(z\) retain the exponential bound of Lemma 3.1. Dominated differentiation proves both claims about regularity.

Under \(s\mapsto1-s\), the two powers in the integral exchange places, and
\(1/(s-1)-1/s\) is unchanged. This proves reflection. The rational terms have precisely the stated poles and residues, which cannot be cancelled by an entire integral. \(\square\)

For completeness, the same argument with the one-dimensional real theta function \(\Theta_{\rm real}\) gives the meromorphic completed zeta function
\[
\begin{aligned}
\Xi(w)&=\pi^{-w/2}\Gamma(w/2)\zeta(w)\\
&=\frac1{w-1}-\frac1w\\
&\quad+\frac12\int_1^\infty(\Theta_{\rm real}(t)-1)
 \left(t^{w/2-1}+t^{(1-w)/2-1}\right)\,dt.
\end{aligned}
\tag{3.8}
\]
Initially this follows by integrating each nonzero one-dimensional Gaussian for \(\operatorname{Re}w>1\). Below one, use
\(\Theta_{\rm real}(t)=t^{-1/2}\Theta_{\rm real}(1/t)\).
The integral is entire. Thus \(\Xi(w)=\Xi(1-w)\), with residues \(1,-1\) at \(1,0\). The ordinary meromorphic continuation of \(\zeta\) follows by multiplying by \(\pi^{w/2}/\Gamma(w/2)\).

Formula (2.8) now continues \(E\) meromorphically as \(E^*/\Xi(2s)\). The assertion that the *only* poles are \(0,1\) belongs to \(E^*\); zeros of the factor used in division require separate consideration for \(E\). The eigenvalue identity also continues as a meromorphic identity, because it holds on the initial open half-plane and (3.7) allows differentiation in \(z\).

**Corollary 3.3 (the residue and the area).**
\[
\operatorname*{Res}_{s=1}E(z,s)=\frac3\pi
=\frac1{\operatorname{vol}(\Gamma\backslash\mathfrak H)}.
\tag{3.9}
\]

**Proof.** At \(s=1\),
\[
\Xi(2)=\pi^{-1}\Gamma(1)\zeta(2)
=\frac{\pi}{6}.
\]
Divide the residue \(1/2\) in (3.6) by this nonzero number.

The fundamental region from The upper half-plane and the modular group is
\(|x|\le1/2,\ y\ge\sqrt{1-x^2}\), apart from paired boundary points of measure zero. Consequently
\[
\int_{-1/2}^{1/2}\int_{\sqrt{1-x^2}}^\infty\frac{dy\,dx}{y^2}
=\int_{-1/2}^{1/2}\frac{dx}{\sqrt{1-x^2}}
=\frac{\pi}{3}.
\]
This proves the second equality. \(\square\)

In completed notation, the constant Fourier term is
\[
\Xi(2s)y^s+\Xi(2s-1)y^{1-s}.
\tag{3.10}
\]
The nonconstant terms (2.9) are entire in \(s\), and their series is locally normally convergent by (2.2). The two apparent poles in (3.10) at \(s=1/2\) cancel: their residues as functions of \(s\) are opposite. Formula (3.7) independently proves that this point is regular.

Reflection of each nonconstant term can also be checked directly. The divisor identity
\[
\sigma_{2s-1}(n)=n^{2s-1}\sigma_{1-2s}(n)
\]
and \(K_{1/2-s}=K_{s-1/2}\) leave (2.9) unchanged. This is a useful check on the power of \(|r|\) and the factor \(2\).


## 4. Maass cusp forms

A weight-zero **Maass form** for \(\Gamma\) is a smooth invariant function \(f\) satisfying \(\Delta f=\lambda f\) and
\[
\sup_{0\le x\le1}|f(x+iy)|=O(y^B)
\quad(y\to\infty)
\]
for some \(B\). It is a **Maass cusp form** if
\[
\int_0^1 f(x+iy)\,dx=0\qquad(y>0).
\tag{4.1}
\]
The word “cusp” removes the constant Fourier term. For a general congruence group one imposes this condition in a scaling coordinate at every cusp.

**Proposition 4.1 (the Maass Fourier expansion).** Choose \(\nu\in\mathbb C\) with
\(\lambda=1/4-\nu^2\). Every Maass form has
\[
f(x+iy)=a_0(y)+
\sum_{n\ne0}\rho_n\sqrt y\,K_\nu(2\pi|n|y)e^{2\pi inx}.
\tag{4.2}
\]
For \(\nu\ne0\), \(a_0(y)=Ay^{1/2+\nu}+By^{1/2-\nu}\).
For \(\nu=0\), it is
\[
a_0(y)=\sqrt y\,(A+B\log y).
\tag{4.3}
\]
For a cusp form \(a_0=0\), and the function and its fixed derivatives decay exponentially in the cusp.

**Proof.** Let \(a_n(y)=\int_0^1f(x+iy)e^{-2\pi inx}\,dx\).
Two integrations by parts in \(x\), using periodicity, give
\[
y^2a_n''(y)+\bigl(\lambda-4\pi^2n^2y^2\bigr)a_n(y)=0.
\tag{4.4}
\]
For \(n=0\), this is an Euler equation. Its indicial roots are \(1/2+\nu\) and \(1/2-\nu\). Distinct roots give the first formula; a double root gives the logarithmic solution (4.3), as can also be checked by direct differentiation.

For \(n\ne0\), put \(u=2\pi|n|y\) and \(a_n(y)=\sqrt y\,b(u)\). Equation (4.4) becomes
\[
u^2b''+ub'-(u^2+\nu^2)b=0.
\tag{4.5}
\]
The function \(K_\nu\) in (2.1) solves this equation. To see it directly, integrate twice by parts in \(v\) in
\(\int_0^\infty e^{-u\cosh v}\cosh(\nu v)\,dv\).
There are no boundary terms, and
\[
\partial_v^2e^{-u\cosh v}
=(u^2\sinh^2v-u\cosh v)e^{-u\cosh v}.
\]
The resulting identity is
\(u^2(K_\nu''-K_\nu)+uK_\nu'=\nu^2K_\nu\), which is (4.5).

We also need to exclude the other solution using growth, rather than just naming a second Bessel function. Laplace's method applied to (2.1) gives
\[
K_\nu(u)=\sqrt{\frac{\pi}{2u}}e^{-u}
             \bigl(1+O_\nu(u^{-1})\bigr)\qquad(u\to\infty).
\tag{4.6}
\]
Here is a justification of the estimate. Substitute \(v=w/\sqrt u\). On a fixed small \(v\)-interval, Taylor's formulas for \(\cosh v\) and \(\cosh(\nu v)\) leave a Gaussian \(e^{-w^2/2}\) with an integrable error bounded by a constant times
\(u^{-1}(w^2+w^4)e^{-c w^2}\). This follows from the Taylor remainders and \(\cosh v-1\ge v^2/2\). Outside the small interval, the extra decay \(e^{-u(\cosh v-1)}\) is exponential in \(u\), even after the fixed factor \(e^{|\operatorname{Re}\nu|v}\). The leading integral is
\(\int_0^\infty e^{-w^2/2}\,dw=\sqrt{\pi/2}\).
This proves (4.6).

In particular \(K_\nu(u)\ne0\) for sufficiently large \(u\). On that interval reduction of order gives an independent solution
\[
L_\nu(u)=K_\nu(u)\int_U^u\frac{dt}{tK_\nu(t)^2}.
\tag{4.7}
\]
Its Wronskian with \(K_\nu\) is \(1/u\). If \(a=\sqrt{\pi/2}\), (4.6) gives
\[
L_\nu(u)=\frac1{2a}u^{-1/2}e^u(1+O_\nu(u^{-1})).
\]
Indeed the integrand in (4.7) is \(a^{-2}e^{2t}(1+O_\nu(t^{-1}))\), whose integral has leading term \(e^{2u}/(2a^2)\).
Every solution of (4.5) is a linear combination of these two, by uniqueness for a second-order linear equation and the nonzero Wronskian. A nonzero \(L_\nu\) coefficient violates the polynomial bound on \(a_n(y)\). Thus \(a_n(y)=\rho_n\sqrt y K_\nu(2\pi|n|y)\) for large \(y\), and uniqueness extends this equality to every \(y>0\).

Fourier inversion for the smooth periodic function gives (4.2) on each compact horizontal strip. To justify exponential decay of the entire cusp form, choose \(y_0\) so large that (4.6) gives upper and lower bounds for every \(K_\nu(2\pi|n|y_0)\), \(n\ne0\). The coefficients \(a_n(y_0)\) are bounded by
\(\sup_x|f(x+iy_0)|\). Taking the ratio of (4.6) at \(y\) and \(y_0\) shows
\[
|a_n(y)|\le C|a_n(y_0)|e^{-2\pi|n|(y-y_0)}
\quad(y\ge y_0).
\]
For \(y\ge y_0+1\), summation gives exponential decay. Differentiating (2.1), or (4.5), gives the same conclusion with any fixed derivative; the extra polynomial powers of \(|n|\) remain summable against this exponential. \(\square\)

**Corollary 4.2.** A nonzero Maass cusp form belongs to \(L^2(\Gamma\backslash\mathfrak H,d\mu)\), and its eigenvalue is real and strictly positive.

**Proof.** Exponential cusp decay gives square integrability and finite Dirichlet energy. On a truncated fundamental region, integration by parts gives
\[
\lambda\int |f|^2\,d\mu
=\int (|f_x|^2+|f_y|^2)\,dx\,dy
\]
in the limit as the truncation height tends to infinity. Paired boundary sides cancel because the transformation is an isometry and \(f\) is invariant. Small boundary circles around elliptic points contribute zero in the limit, since the lifted function and derivatives are smooth there. The upper boundary contributes zero by Proposition 4.1. Thus the right side is real and nonnegative. If it is zero, both derivatives vanish and \(f\) is constant on the connected half-plane. The cusp condition then makes \(f=0\), a contradiction. \(\square\)

It follows that either \(\nu\) is purely imaginary or it is real with \(|\nu|<1/2\). The case \(\nu=0\) is the spectral value \(1/4\); it must be included in the Fourier discussion.

The reflection \(Rf(z)=f(-\bar z)\) preserves invariance, the Laplacian and cuspidality. Since \(R^2=1\), every cusp form splits as \((f+Rf)/2+(f-Rf)/2\), into even and odd parts. In these two parts respectively,
\(\rho_{-n}=\rho_n\) and \(\rho_{-n}=-\rho_n\).

### 4.1. Infinitely many cusp forms from reflection

There is an elementary variational route to existence on the full modular quotient. It uses the reflection \(Rz=-\bar z\), which preserves the fundamental region and normalizes \(\Gamma\). Odd functions have zero constant term in the only cusp; this removes the escape of mass responsible for continuous spectrum.

**Theorem 4.3 (existence in the odd subspace).** There are infinitely many linearly independent odd Maass cusp forms for \(\mathrm{SL}_2(\mathbb Z)\), with positive eigenvalues tending to infinity.

**Proof.** Let \(M=\Gamma\backslash\mathfrak H\). Complete the smooth, compactly supported odd functions on \(M\) in the norm
\[
\begin{gathered}
\|u\|_{\mathcal H}^2=\|u\|_2^2+Q(u),\\
\begin{aligned}
Q(u)&=\int_M\Bigl[|u_x|^2\\
&\qquad+|u_y|^2\Bigr]\,dx\,dy.
\end{aligned}
\end{gathered}
\tag{4.7a}
\]
The energy is invariant under modular coordinate changes. At elliptic points use smooth invariant functions in the finite covering disk and divide its integrals by the stabilizer order. The map from this completion to \(L^2(M)\) is injective. Indeed, suppose a smooth sequence tends to zero in \(L^2(M)\) and its coordinate derivatives tend to \(v_x,v_y\) in local \(L^2\). On a compact coordinate disk the hyperbolic and Euclidean \(L^2\) norms are comparable. For every smooth compactly supported test function \(\phi\), integration by parts gives
\[
 \int v_i\phi=-\lim_j\int u_j\partial_i\phi=0,
 \qquad i=x,y.
\]
Thus \(v_i=0\), since such test functions are dense in local \(L^2\), as follows by smoothing compact step-function approximations. Consequently a limit with zero \(L^2\) component has zero energy component too. For an arbitrary Cauchy sequence the same integration-by-parts identity identifies its derivative limit with the weak derivative of its \(L^2\) limit. Every element of the completion therefore defines an odd \(L^2\) function with one weak derivative locally and finite norm (4.7a). The Fourier completeness used below can be checked by the period-one Fejér kernels \(K_A(t)=A^{-1}|\sum_{j=0}^{A-1}e^{2\pi ijt}|^2\): they are nonnegative with integral one, and their mass outside any fixed neighborhood of zero tends to zero. Uniform continuity makes their convolutions converge uniformly for continuous periodic functions. Continuous functions are dense in \(L^2\), by smoothing the finitely many endpoints of step-function approximations. Thus the exponentials are complete in \(L^2\), and orthogonality gives Parseval. Products of these kernels give the same result on rectangles; integration by parts gives the derivative coefficients.

For \(Y\ge1\), the cusp is \(-1/2\le x\le1/2\), \(y\ge Y\). Oddness gives \(\int_{-1/2}^{1/2}u(x+iy)dx=0\). Fourier orthogonality on this period-one interval proves
\(\int|u|^2dx\le(4\pi^2)^{-1}\int|u_x|^2dx\): the constant coefficient vanishes, and each other derivative coefficient is multiplied by \(2\pi in\), with \(|n|\ge1\). Integrate and use \(y^{-2}\le Y^{-2}\) to obtain
\[
 \int_{y\ge Y}|u|^2d\mu
 \le\frac{Q(u)}{4\pi^2Y^2}.
 \tag{4.7b}
\]
Approximation extends this inequality to the completion.

We next prove compactness of the inclusion \(\mathcal H\to L^2(M)\). On a compact part of \(M\), finitely many coordinate disks, with smooth cutoffs, reduce the question to functions supported inside bounded Euclidean rectangles. Extend each cutoff function by zero and put it in a larger periodic rectangle. A bound on its function and first derivatives bounds \(\sum_{\ell}(1+|\ell|^2)|\widehat u(\ell)|^2\), by Fourier orthogonality. The sum of squared coefficients with \(|\ell|>A\) is at most \(C/A^2\). A subsequence converges in every finite set of coefficients; the tail bound makes it converge in \(L^2\). Covering disks above elliptic points have the same argument, and restriction to their invariant subspaces preserves compactness. A diagonal choice over compact parts and the uniform cusp-tail estimate (4.7b) then give an \(L^2(M)\)-convergent subsequence of every bounded sequence in \(\mathcal H\).

Minimize \(Q(u)\) subject to \(\|u\|_2=1\) in \(\mathcal H\). A minimizing sequence is bounded in this Hilbert space. Here is the weak-compactness step explicitly: choose a countable orthonormal basis, extract a subsequence on which every coordinate converges, and use the squared-coordinate bound to obtain a Hilbert-space vector with those limits. Finite-coordinate approximation and the uniform norm bound imply weak convergence to that vector; the same squared-coordinate argument proves that its norm is at most the lower limit. A countable basis exists because the coordinate-disk Fourier approximations and smooth cutoffs above give a countable dense set. Apply this to the norm in (4.7a), and apply compactness to get strong \(L^2\) convergence as well. The limit has \(L^2\) norm one and minimizes \(Q\), since \(Q=\|\cdot\|_{\mathcal H}^2-\|\cdot\|_2^2\) is lower semicontinuous along this subsequence.

Variation with respect to real and imaginary multiples of every test function gives
\[
\begin{gathered}
Q(u,v)=\lambda\langle u,v\rangle_2,\\
\lambda=Q(u).
\end{gathered}
\tag{4.7c}
\]
where the polarized energy is linear in its first variable. This identity holds for every odd test function. For an even test function both sides vanish by reflection, so it holds for every test function. In a local disk it is the weak equation
\(-u_{xx}-u_{yy}=\lambda y^{-2}u\).

For clarity, this weak solution is smooth without a spectral regularity import. Multiply by a compactly supported cutoff in a disk and extend by zero inside a larger periodic rectangle. The Laplacian of the product is in \(L^2\), since initially \(u\) has one weak derivative and \(y^{-2}\) is smooth and bounded on that disk. The Fourier-coefficient identity for \(1-\partial_x^2-\partial_y^2\) shows that division by its multiplier \(1+c_1\ell_1^2+c_2\ell_2^2\), with positive rectangle constants \(c_i\), gives two square-integrable weak derivatives. Repeating with nested cutoffs increases the number of derivatives by one at each step. The Fourier series and Cauchy–Schwarz show that sufficiently many square-integrable derivatives give any specified number of continuous derivatives: \(\sum_{\ell\in\mathbb Z^2}(1+|\ell|^2)^{-a}<\infty\) for \(a>1\), by counting lattice points in square shells. Thus \(u\) is smooth. Above an elliptic point, first average a test function over its finite stabilizer; the same weak equation and argument hold on the covering disk.

Repeat minimization in the \(L^2\)-orthogonal complement of the previously obtained functions. There is always a nonzero trial function: choose arbitrarily many disjoint disks in the interior of the right half of the fundamental region, and subtract the reflected copy of a bump on each disk. These give an infinite-dimensional odd trial space, whereas the orthogonality constraints are finite. Orthogonality in energy to the previous eigenfunctions follows from (4.7c), so variation in the constrained space still gives (4.7c) for every test function. We obtain an orthonormal sequence of smooth eigenfunctions \(u_j\). Their eigenvalues tend to infinity: an infinite subsequence with bounded \(Q\) would be bounded in \(\mathcal H\) and hence would have an \(L^2\)-convergent subsequence, contradicting orthonormality. An eigenvalue zero would make the derivatives zero, so the function would be constant on the connected quotient; oddness makes that constant zero. All eigenvalues are therefore positive.

Finally, oddness kills the constant Fourier coefficient at every cusp height. For each nonzero coefficient the differential equation in Proposition 4.1 applies. Its growing solution is excluded by \(L^2\) integrability, leaving the \(K_\nu\) solution. Choose a fixed height large enough for its large-positive-argument estimate to hold uniformly for \(2\pi|n|y\). Smoothness on that fixed horocycle makes its Fourier coefficients decrease faster than any power of \(|n|\); the ratio of its decaying solutions at larger heights supplies \(e^{-2\pi|n|(y-Y)}\) times a fixed polynomial bound. Summing proves exponential decay in the cusp, together with derivatives. Thus the functions just constructed are Maass cusp forms in the definition used here. \(\square\)

### 4.2. Spectral assertions whose proofs remain required

The existence assertion is now proved locally. The following sharper statements are retained with their source locators and explicit outstanding proof requirements. Selberg's Weyl law for the modular surface says that the number of cuspidal eigenvalues at most \(T\), counted with multiplicity, is
\[
N_{\rm cusp}(T)\sim
\frac{\operatorname{vol}(\Gamma\backslash\mathfrak H)}{4\pi}T
=\frac{T}{12}.
\tag{4.8}
\]
Theorem 4.3 proves infinitude without (4.8), but does not prove its asymptotic or completeness of the full spectral expansion. A freely accessible account is [Miller, *On the existence and temperedness of cusp forms for \(SL_3(\mathbb Z)\)*, Theorem 2.1; the discussion following Corollary 1.4 identifies the noncuspidal discrete spectrum at prime rank as the constants]. The constant eigenfunction has eigenvalue zero by direct differentiation and is square integrable because the quotient has finite area. For \(s=1/2+it\), the directly proved identity \(s(1-s)=1/4+t^2\) explains the proposed Eisenstein spectral parameter. Identifying these generalized eigenfunctions with the full continuous part, proving that it begins at \(1/4\), and proving Miller's Proposition 2.4 are outstanding spectral proof tasks.

**Selberg's eigenvalue conjecture** concerns all congruence quotients: every positive discrete eigenvalue should be at least \(1/4\). The uniform established bound is
\[
\lambda\ge\frac{975}{4096}
=\frac14-\left(\frac7{64}\right)^2.
\tag{4.9}
\]
See [Sarnak, *Notes on the generalized Ramanujan conjectures*, author's freely distributed notes, §1, equations (24)–(25)], for the Kim–Sarnak bound and its parameter interpretation. A programme proof of this deep bound remains required; it is not used in the continuation or Fourier calculations. The assertion about all congruence levels is the conjecture; the theta integral above is not a proof of it.

In adelic language, Eisenstein series are built from representations on Levi subgroups by induction and averaging. Their continuation, intertwining equations and spectral decomposition are the statements in [Getz–Hahn, *An Introduction to Automorphic Representations*, draft of 22 April 2022, Theorems 10.3.2 and 10.4.1](https://sites.duke.edu/jgetz/files/2022/04/Graduate_Text.pdf). The classical computation here gives a concrete instance. The general theorems are an outlook toward *Adelic Eisenstein series*, not inputs to our proofs.

## 5. The limit formula and a check on the constant term

Put \(q=e^{2\pi iz}\) and
\[
\eta(z)=q^{1/24}\prod_{n\ge1}(1-q^n),
\qquad q^{1/24}=e^{\pi iz/12}.
\tag{5.1}
\]
This product converges locally uniformly to a nonzero holomorphic function: the series of holomorphic logarithms
\(\sum_n\log(1-q^n)\) converges absolutely and locally uniformly, using the branch defined by its power series.

Kronecker's first limit formula in the present normalization is
\[
\begin{aligned}
E(z,s)
&=\frac{3}{\pi(s-1)}
+\frac6\pi\left(\gamma-\log2-\frac{\zeta'(2)}{\zeta(2)}\right)\\
&\quad-\frac3\pi\log\bigl(y|\eta(z)|^4\bigr)+O(s-1).
\end{aligned}
\tag{5.2}
\]
Here \(\gamma=\lim_{N\to\infty}(\sum_{n=1}^N1/n-\log N)\).
Solution 4 proves the entire formula, including its additive constant.

For example, at the square lattice point \(z=i\), the finite part is exactly
\[
\begin{aligned}
&\frac6\pi\left(\gamma-\log2-\frac{\zeta'(2)}{\zeta(2)}\right)
-\frac{12}{\pi}\log|\eta(i)|\\
&\quad=
1+\frac6\pi\left(\gamma-\log2-\frac{\zeta'(2)}{\zeta(2)}\right)
-\frac{12}{\pi}\sum_{n\ge1}\log(1-e^{-2\pi n}).
\end{aligned}
\tag{5.3}
\]
The equality uses \(q^{1/24}=e^{-\pi/12}\) at \(i\). Every term in the last sum is a real logarithm of a positive number. The full convergent expression follows by specializing (5.2), rather than by retaining only its leading \(q\)-term.

There is also a useful example at the center of the functional equation. Write
\[
C_\Xi=\frac{\gamma}{2}-\log2-\frac12\log\pi.
\]
The expansions in Solution 4 give
\(\Xi(1+\epsilon)=1/\epsilon+C_\Xi+O(\epsilon)\).
Reflection gives \(\Xi(\epsilon)=-1/\epsilon+C_\Xi+O(\epsilon)\).
Taking the limit in (3.10), and then using the normally convergent nonconstant series, yields
\[
\begin{aligned}
E^*(z,\tfrac12)
&=\sqrt y\,(\log y+2C_\Xi)\\
&\quad+\sum_{n\ne0}2\sigma_0(|n|)\sqrt y\,
K_0(2\pi|n|y)e^{2\pi inx}.
\end{aligned}
\tag{5.4}
\]
This illustrates both cancellation of the apparent pole and the logarithmic solution for a repeated indicial root. Its constant term grows as \(\sqrt y\log y\).

## 6. Exercises

1. **[Easy]** Check \(\Delta y^s=s(1-s)y^s\) and prove the commutation identity for every \(\gamma\in SL_2(\mathbb R)\), including the second-derivative terms in the chain rule.
2. **[Medium]** Compute \(I_s(n,y)=\int_{\mathbb R}(x^2+y^2)^{-s}e^{-2\pi inx}\,dx\) for \(\operatorname{Re}s>1/2\). Treat \(n=0\) separately and recover the constants in (2.6).
3. **[Medium]** Prove that the residue of the primitive-coset series at \(s=1\) is \(3/\pi\). Explain how the answer changes if opposite primitive vectors are counted separately.
4. **[Hard]** Prove (5.2), Kronecker's first limit formula, including the additive constant. Derive the eta product from the limiting nonconstant Fourier terms.

## 7. Complete solutions

### Solution 1

The function \(y^s\) is independent of \(x\). Its second \(y\)-derivative is \(s(s-1)y^{s-2}\), so multiplication by \(-y^2\) gives the answer.

For \(w=\gamma z=u(x,y)+iv(x,y)\), write out the second derivatives:
\[
\begin{aligned}
\Delta_{\rm eucl}(f\circ w)
&=(u_x^2+u_y^2)f_{uu}
 +2(u_xv_x+u_yv_y)f_{uv}\\
&\quad+(v_x^2+v_y^2)f_{vv}
 +(u_{xx}+u_{yy})f_u+(v_{xx}+v_{yy})f_v.
\end{aligned}
\]
All derivatives of \(f\) on the right are evaluated at \(w\). The Cauchy–Riemann equations give
\(u_x=v_y,\ u_y=-v_x\); hence the mixed coefficient is zero and both square coefficients equal \(|w'|^2\). Differentiating these equations gives
\(\Delta_{\rm eucl}u=\Delta_{\rm eucl}v=0\).
Since \(w'=(cz+d)^{-2}\) and \(v=y/|cz+d|^2\), one has \(y^2|w'|^2=v^2\). Multiplication by \(-y^2\) therefore proves
\(\Delta(f\circ\gamma)=(\Delta f)\circ\gamma\).

### Solution 2

Insert the Gamma integral as in Lemma 2.1. Absolute Fubini is valid because
\[
\int_0^\infty t^{\operatorname{Re}s-1}e^{-y^2t}
\int_{\mathbb R}e^{-tx^2}\,dx\,dt
=\sqrt\pi\int_0^\infty t^{\operatorname{Re}s-3/2}e^{-y^2t}\,dt<\infty.
\]
The transform of \(e^{-tx^2}\) is
\(\sqrt{\pi/t}\,e^{-\pi^2n^2/t}\). This gives (2.4).
For \(n=0\) the substitution \(v=y^2t\) gives
\(\sqrt\pi\,\Gamma(s-1/2)y^{1-2s}/\Gamma(s)\).
For \(n\ne0\), the substitution \(t=(\pi|n|/y)v\) gives
\[
I_s(n,y)=
\frac{\pi^s}{\Gamma(s)}
\left(\frac{|n|}{y}\right)^{s-1/2}
\int_0^\infty
e^{-\pi|n|y(v+v^{-1})}v^{s-1/2}\,\frac{dv}{v}.
\]
The last integral is \(2K_{s-1/2}(2\pi|n|y)\), proving (2.3). Multiplying by
\(y^s\sigma_{1-2s}(|n|)/\zeta(2s)\) gives exactly \(c_n(s)\sqrt y K_{s-1/2}\) in (2.6). For the zero coefficient, multiply by
\(y^s\zeta(2s-1)/\zeta(2s)\), giving the \(\phi(s)y^{1-s}\) term. The remaining \(y^s\) comes from the lattice vectors with \(m=0\).

### Solution 3

The residue of \(E^*\) is \(1/2\), by the explicit rational terms in (3.7); the entire integral contributes no pole. At \(s=1\), its normalizing factor is
\(\pi^{-1}\Gamma(1)\zeta(2)=\pi/6\). Thus
\[
\operatorname*{Res}_{s=1}E
=\frac{1/2}{\pi/6}=\frac3\pi.
\]

One elementary verification of the value of \(\zeta(2)\) is the cosine expansion
\[
x^2=\frac{\pi^2}{3}
+4\sum_{n\ge1}\frac{(-1)^n}{n^2}\cos(nx)
\quad(-\pi\le x\le\pi).
\]
Two integrations by parts compute the coefficients. Their absolute summability makes the series uniformly convergent, and Fourier uniqueness identifies it with the continuous periodic function \(x^2\). Substituting \(x=\pi\) gives
\(\pi^2=\pi^2/3+4\zeta(2)\), hence \(\zeta(2)=\pi^2/6\).

If instead one sums over all primitive vectors without the factor \(1/2\), the resulting series is \(2E\), and its residue is \(6/\pi\). If one sums over all nonzero vectors with the factor \(1/2\), but without Gamma or \(\pi\) factors, the result is \(\zeta(2s)E\) and its residue is
\(\zeta(2)\cdot3/\pi=\pi/2\).
These are distinct normalizations of the same lattice calculation.

### Solution 4

We first calculate the constant coefficient at \(s=1\). Near \(w=1\),
\[
\zeta(w)=\frac1{w-1}+\gamma+O(w-1).
\tag{7.1}
\]
For a direct justification, subtract the integral of \(u^{-w}\) over each interval \([n,n+1]\). The series
\[
\sum_{n\ge1}\left(n^{-w}-\int_n^{n+1}u^{-w}\,du\right)
\]
is locally normally convergent for \(\operatorname{Re}w>0\), by the mean value estimate \(O_K(n^{-\operatorname{Re}w-1})\). In the original domain it equals \(\zeta(w)-1/(w-1)\). At \(w=1\) its partial sums are
\(\sum_{n=1}^N1/n-\log(N+1)\), whose limit is \(\gamma\). This proves (7.1).

Let \(\psi=\Gamma'/\Gamma\). We need
\[
\psi(1)=-\gamma,\qquad \psi(\tfrac12)=-\gamma-2\log2.
\tag{7.2}
\]
These constants can be derived from the Gamma integral. The beta integral gives the locally uniform Euler limit
\[
\Gamma(s)=\lim_{N\to\infty}
\frac{N!\,N^s}{s(s+1)\cdots(s+N)}
\quad(\operatorname{Re}s>0).
\]
Indeed substitute \(u=Nt\) in \(N^sB(s,N+1)\); the integrand
\(u^{s-1}(1-u/N)^N\), extended by zero for \(u>N\), tends to \(u^{s-1}e^{-u}\) and is dominated on compact \(s\)-sets. The same domination with powers of \(\log u\) permits differentiation. Logarithmic differentiation at \(s=1\) gives
\(\psi(1)=\lim_N(\log N-\sum_{j=0}^N(1+j)^{-1})=-\gamma\).

In the beta integral, the substitutions \(t=(1+v)/2\) and then \(u=v^2\) give
\(B(s,s)=2^{1-2s}B(1/2,s)\). Expressing both beta integrals in terms of Gamma functions yields the duplication identity
\[
\Gamma(s)\Gamma(s+\tfrac12)
=2^{1-2s}\sqrt\pi\,\Gamma(2s).
\]
The value \(\Gamma(1/2)=\sqrt\pi\) follows from the Gaussian integral. Logarithmic differentiation of duplication at \(s=1/2\) gives the second formula in (7.2).

Put \(\epsilon=s-1\). The factor
\[
H(s)=\frac{\sqrt\pi\,\Gamma(s-\tfrac12)}
              {\Gamma(s)\zeta(2s)}
\]
is holomorphic near \(1\), with
\[
H(1)=\frac6\pi,\qquad
\frac{H'(1)}{H(1)}
=-2\log2-2\frac{\zeta'(2)}{\zeta(2)}.
\]
Since \(\phi(s)=H(s)\zeta(2s-1)\), (7.1) gives
\[
\phi(s)=\frac3{\pi\epsilon}
+\frac6\pi\left(\gamma-\log2-\frac{\zeta'(2)}{\zeta(2)}\right)
+O(\epsilon).
\tag{7.3}
\]
Also \(y^{1-s}=1-\epsilon\log y+O(\epsilon^2)\) and \(y^s=y+O(\epsilon)\). Thus the finite part of the constant Fourier coefficient in (2.5) is
\[
y-\frac3\pi\log y+
\frac6\pi\left(\gamma-\log2-\frac{\zeta'(2)}{\zeta(2)}\right).
\tag{7.4}
\]

For the nonconstant terms we need the special value
\[
K_{1/2}(u)=\sqrt{\frac{\pi}{2u}}e^{-u}.
\tag{7.5}
\]
It follows directly from the Gaussian Fourier integral: set \(s=1\) in (2.3), and use the elementary contour evaluation
\(\int_{\mathbb R}(x^2+y^2)^{-1}e^{-2\pi irx}\,dx
=(\pi/y)e^{-2\pi|r|y}\) for \(r\ne0\).
For \(r>0\), close in the lower half-plane, where the exponential decays, and take the pole at \(-iy\) with clockwise orientation. Its residue gives the displayed value. For \(r<0\), close in the upper half-plane; evenness gives the same answer. The closing semicircle contributes zero, since the rational factor is \(O(R^{-2})\) and the exponential has modulus at most one there. Comparing the two expressions for the integral proves (7.5).

At \(s=1\), (2.6) and (7.5) therefore give the nonconstant sum
\[
\frac6\pi\sum_{n\ne0}\sigma_{-1}(|n|)
e^{-2\pi|n|y}e^{2\pi inx}
=\frac{12}{\pi}\operatorname{Re}
\sum_{n\ge1}\sigma_{-1}(n)q^n.
\tag{7.6}
\]
The normally convergent Fourier series is holomorphic in \(s\) near \(1\), since \(\Gamma(s)\zeta(2s)\ne0\) there and (2.2) is uniform on a small closed disk. Hence substitution \(s=1\) in its nonconstant part is justified, with a remainder \(O(s-1)\).

Finally, absolute convergence permits rearranging the logarithmic series:
\[
-\sum_{m\ge1}\log(1-q^m)
=\sum_{m,j\ge1}\frac{q^{mj}}{j}
=\sum_{n\ge1}\sigma_{-1}(n)q^n.
\tag{7.7}
\]
By (5.1),
\[
\log|\eta(z)|=-\frac{\pi y}{12}
+\sum_{m\ge1}\log|1-q^m|.
\]
Thus (7.6) is
\[
-\frac{12}{\pi}\log|\eta(z)|-y.
\]
Adding it to (7.4) cancels \(y\) and gives exactly the finite part in (5.2). Together with the residue term, this proves Kronecker's formula. All remainders are locally uniform in \(z\), by the same compact-set exponential majorants.

To check (5.4), expand
\(\pi^{-w/2}\Gamma(w/2)\) at \(w=1\), using (7.2):
\[
\Xi(1+\epsilon)
=\frac1\epsilon+
\gamma+\frac12\bigl(\psi(\tfrac12)-\log\pi\bigr)+O(\epsilon)
=\frac1\epsilon+C_\Xi+O(\epsilon).
\]
Insert this and its reflected expansion in (3.10), at
\(s=1/2+\epsilon\). The poles \(1/(2\epsilon)\) and \(-1/(2\epsilon)\) cancel, leaving \(\sqrt y(\log y+2C_\Xi)\). In (2.9), \(s=1/2\) leaves the divisor count \(\sigma_0\) and \(K_0\), proving the rest of (5.4).

## What this lesson does not prove

- The one-dimensional Schwartz Poisson formula, Gaussian transform and real theta inversion are the exact prerequisite statements in *Theta functions and sums of squares*, equations (1.3)–(1.5). Lemma 3.1 derives the two-dimensional Gaussian case from them.
- The meromorphic Gamma function and its entire reciprocal are proved in The Gamma function and Stirling's formula, Theorems 1.1–1.2. Its Theorem 2.2 proves \(\Gamma(1/2)=\sqrt\pi\). The needed local Gamma constants are derived in Solution 4. The zeta continuation and reflection used here are derived in (3.8); Poisson summation, theta, and the functional equation, Theorem 3.1 and Corollary 3.2, give an independent programme proof with the same completed-zeta normalization.
- Theorem 4.3 proves infinitely many odd Maass cusp forms by a compactness and minimization argument, including the required local smoothness and cusp decay. The full Weyl asymptotic, completeness and continuous spectral decomposition remain proof tasks, located in the freely accessible [Miller, Theorem 2.1 and Proposition 2.4]. The local existence proof does not establish these stronger assertions.
- Selberg's conjecture for all congruence quotients is a conjecture. The Kim–Sarnak bound is stated from [Sarnak, §1, equations (24)–(25)].
- General adelic Eisenstein continuation and Langlands' spectral decomposition are the outlook statements [Getz–Hahn, draft of 22 April 2022, Theorems 10.3.2 and 10.4.1]. Higher-rank induction, intertwining operators and the trace formula are not developed here.

Free references: Sarnak, [*Notes on the generalized Ramanujan conjectures*](https://publications.ias.edu/sites/default/files/FieldNotesCurrent.pdf), author's notes, §1, equations (24)–(25), for the retained spectral bound; Getz–Hahn, [*An Introduction to Automorphic Representations*](https://sites.duke.edu/jgetz/files/2022/04/Graduate_Text.pdf), author's draft of 22 April 2022, Chapter 10, for the adelic outlook; and Miller's [original article](https://sites.math.rutgers.edu/~sdmiller/sl3/sl3spectrum.pdf), especially §2, for the full modular-surface spectral assertions. These references identify outstanding proofs; their availability does not replace those proofs in the programme.
