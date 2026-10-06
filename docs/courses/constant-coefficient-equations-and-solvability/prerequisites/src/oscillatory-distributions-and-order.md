# Oscillatory distributions and their order

An integral over all frequencies may fail to converge as a function while still defining a distribution. Its phase gives a controlled way to move derivatives onto the amplitude and test function. Once the distribution is defined, stationary phase converts its local representation into a frequency symbol and explains every dimension-dependent order shift.

We use the symbol conventions, Fourier transformation and support-preserving asymptotic summation of Symbols, operators and Sobolev scales. Detecting regularity without choosing coordinates supplies the Fourier definition of the wavefront set. The geometric prerequisites are [Phase space and generating families](phase-space-and-generating-families.md); the estimates are in [Stationary phase and critical manifolds](stationary-phase-and-critical-manifolds.md). Basic references are [Guillemin–Sternberg] and [Hörmander IV].

## 1. Frequency cutoffs define a distribution

Let \(\phi(x,\theta)\) be a real smooth homogeneous phase on an open cone \(\Gamma\subset U\times(\mathbb R^N\setminus0)\). It need not be nondegenerate for this section. Fix a compact set of base points and phase directions contained in \(\Gamma\), and let the amplitude vanish for \(|\theta|\leq1\). All its high-frequency support lies in that fixed cone. Low-frequency smooth amplitudes can be added separately.

For

\[
0<\rho\leq1,\qquad 0\leq\delta<1,
\]

an amplitude in \(S^\mu_{\rho,\delta}\) satisfies, on each working compact base set,

\[
|\partial_\theta^\alpha\partial_x^\beta a(x,\theta)|
\leq C_{\alpha,\beta}\langle\theta\rangle^{\mu-\rho|\alpha|+\delta|\beta|}.
\tag{1.1}
\]

We use the notation \(S^\mu=S^\mu_{1,0}\). These are local-in-base bounds; uniform global bounds require a separate assertion.

**Theorem 1.1 (oscillatory integral).** Choose \(\chi\in C_c^\infty(\mathbb R^N)\) equal to one near zero. The limit

\[
\langle u,f\rangle=
\lim_{\varepsilon\downarrow0}
\iint e^{i\phi(x,\theta)}a(x,\theta)
\chi(\varepsilon\theta)f(x)\,dx\,d\theta,
\qquad f\in C_c^\infty(U),
\tag{1.2}
\]

exists and defines a distribution. It is independent of \(\chi\). On fixed supports its distribution seminorms are controlled by finitely many amplitude seminorms. Bounded symbol families converging smoothly on compact sets have convergent resulting distributions.

**Proof.** Put \(r=|\theta|\). Homogeneity and \(d\phi\neq0\) give, on the specified compact set of directions,

\[
A=|\phi_x'|^2+r^2|\phi_\theta'|^2\geq c r^2.
\]

Define

\[
L=\frac{1}{iA}
\left(\phi_x'\cdot\partial_x+
r^2\phi_\theta'\cdot\partial_\theta\right).
\tag{1.3}
\]

Then \(Le^{i\phi}=e^{i\phi}\). The coefficients of its \(x\) derivatives are homogeneous of degree \(-1\), and those of its \(\theta\) derivatives are degree zero. Their derivatives satisfy the corresponding ordinary symbol bounds. The formal transpose is obtained by taking minus the divergence of each coefficient times the function.

Set \(\kappa=\min(\rho,1-\delta)>0\). The product rule shows that \(L^t\) takes a compact-base-supported amplitude of order \(\nu\) to one of order at most \(\nu-\kappa\). An \(x\) derivative costs \(\delta\) but has a coefficient of order \(-1\); a \(\theta\) derivative gains \(\rho\) and has a coefficient of order zero. Derivatives of those coefficients gain at least one frequency order or cost no base order. The same estimates hold after differentiating the result.

The cutoff amplitudes \(a\chi(\varepsilon\theta)\) form a bounded family in (1.1). A derivative of the cutoff is supported where \(r\asymp\varepsilon^{-1}\), and contributes \(\varepsilon^{|\alpha|}\leq C r^{-\rho|\alpha|}\). Integrate by parts \(M\) times in the cutoff integral. Choose \(M\kappa>\mu+N\); then \((L^t)^M(a\chi(\varepsilon\theta)f)\) has an integrable majorant \(C_f\langle\theta\rangle^{\mu-M\kappa}\), uniformly in \(\varepsilon\).

For each fixed \(\theta\), derivatives of the cutoff tend to those of the constant one. Dominated convergence therefore gives the limit as

\[
\iint e^{i\phi}(L^t)^M(af)\,dx\,d\theta.
\]

It is bounded by finitely many derivatives of \(f\), hence defines a distribution. Different cutoffs give this same expression. The same domination proves continuity for the asserted bounded families. ∎

The construction works when \(\delta\geq\rho\); it needs positive \(\kappa\), rather than an asymptotic pseudodifferential calculus in that range. No endpoint with \(\rho=0\) or \(\delta=1\) is asserted by this proof.

## 2. The directions where singularities can occur

Let \(\mathcal A\) be the closure, away from the zero section, of

\[
\{(x,\phi_x'(x,\theta)):
\phi_\theta'(x,\theta)=0,
(x,\theta)\text{ lies in the amplitude's supporting cone}\}.
\tag{2.1}
\]

**Theorem 2.1 (wavefront inclusion).** For the distribution of Theorem 1.1,

\[
\operatorname{WF}(u)\subset\mathcal A.
\tag{2.2}
\]

**Proof.** Localize in \(x\) by a compact smooth function supported sufficiently close to a point \(x_0\), and examine the Fourier transform in a small cone of \(\xi\) whose closure is disjoint from (2.1). Its phase is \(\phi(x,\theta)-x\cdot\xi\). Write \(R=|\xi|\geq1\), and split the \(\theta\) integral by smooth cutoffs into \(r\leq cR\) and \(r\geq cR/2\), choosing \(c>0\) small. The cutoffs satisfy uniform symbol estimates; their derivatives have size \(O(R^{-j})\) on the transition region.

On the first region, \(|\phi_x'|\leq C r\) and therefore \(|\phi_x'-\xi|\geq R/2\). Integration by parts using only the \(x\) gradient gives a factor \(R^{-1}\) each time. Derivatives of the amplitude cost at most \(\langle\theta\rangle^\delta\), so after \(M\) iterations the absolute integral is bounded by

\[
C_M R^{-M}\int_{1\leq r\leq cR}
\langle\theta\rangle^{\mu+M\delta}\,d\theta.
\]

This is bounded by a fixed polynomial times \(R^{-M(1-\delta)}\), with a possible logarithm at the radial exponent \(-N\). Since \(1-\delta>0\), it decreases faster than any prescribed inverse power after taking \(M\) sufficiently large.

On the second region there is a uniform bound

\[
|\phi_x'-\xi|^2+r^2|\phi_\theta'|^2
\geq c_1(r+R)^2.
\tag{2.3}
\]

For \(r/R\) in a compact interval this follows by compactness and exclusion of the simultaneous critical equations. For \(r/R\) large it follows from the original nonvanishing-gradient bound, since subtracting \(\xi\) is a small perturbation on that scale. Thus the operator (1.3), with \(\phi_x'\) replaced by \(\phi_x'-\xi\), has uniform symbol coefficients for \(r\asymp r+R\). Its transpose lowers the amplitude order by \(\kappa\). After \(M\) iterations the integral is bounded by

\[
C_M\int_{r\geq cR/2}
\langle\theta\rangle^{\mu-M\kappa}\,d\theta
\leq C_M'R^{\mu+N-M\kappa},
\]

once the exponent is integrable. Choose \(M\) arbitrarily large. The estimates are uniform in the chosen frequency cone and apply to the cutoff approximations defining \(u\); passage to their limit is justified by Theorem 1.1. This gives the rapid Fourier decay characterizing absence from the wavefront set. ∎

For a clean phase, the possible singular directions therefore lie on its Lagrangian image. The inclusion can be strict: a vanishing amplitude can remove all or part of that image.

## 3. Order is fixed by the dimension balance

Let \(n=\dim X\). For a nondegenerate phase with \(N\) variables, we normalize a local half-density by

\[
u(x)|dx|^{1/2}
=(2\pi)^{-(n+2N)/4}
\left(\int e^{i\phi(x,\theta)}a(x,\theta)\,d\theta\right)|dx|^{1/2},
\qquad
a\in S^{m+(n-2N)/4}.
\tag{3.1}
\]

The number \(m\) is the order of this local Lagrangian representation. A half-density transforms by the square root of the absolute coordinate Jacobian. This removes an arbitrary choice of volume from the geometric amplitude later on.

For a clean phase of excess \(e\), use instead

\[
u(x)|dx|^{1/2}
=(2\pi)^{-(n+2N-2e)/4}
\left(\int e^{i\phi(x,\theta)}a(x,\theta)\,d\theta\right)|dx|^{1/2},
\qquad
a\in S^{m+(n-2N-2e)/4}.
\tag{3.2}
\]

Both formulas have the same effective order. The extra \(-e/2\) in the amplitude compensates for the loss of \(e\) cancellation directions. These formulas are for ordinary symbols \(S_{1,0}\). A different derivative-loss class has its own remainder scale.

The next theorem derives the balance and a usable leading coefficient. It compares local representations; the invariant symbol and the intrinsic iterated-regularity characterization require further results.

## 4. Fourier reduction near a frequency graph

Choose base coordinates in which the Lagrangian is

\[
\Lambda=\{(H'(\xi),\xi)\},
\]

where \(H\) is homogeneous of degree one, as in Theorem 6.2 of [Phase space and generating families](phase-space-and-generating-families.md). Let \(\phi\) be a clean phase for a small part of that Lagrangian. Restrict its amplitude to a sufficiently small compact-base cone about a point of its critical set. On this cone \(|\phi_x'|\asymp|\theta|\). Compactly supported cutoffs in the local fiber coordinates are included in the amplitude.

**Theorem 4.1 (local Fourier-symbol reduction).** For (3.2), the function

\[
v(\xi)=e^{iH(\xi)}\widehat u(\xi)
\]

is a symbol of order \(m-n/4\) on the corresponding high-frequency cone, modulo a rapidly decreasing symbol. In the nondegenerate case \(e=0\), write

\[
G(x,\theta)=
\begin{pmatrix}
\phi_{xx}''&\phi_{x\theta}''\\
\phi_{\theta x}''&\phi_{\theta\theta}''
\end{pmatrix}.
\]

At the unique point determined locally by \(\phi_\theta'=0\), \(\phi_x'=\xi\), this matrix is invertible, and

\[
v(\xi)-
(2\pi)^{n/4}
e^{i\pi\operatorname{sgn}G/4}
\frac{a(x,\theta)}{|\det G(x,\theta)|^{1/2}}
\in S^{m-n/4-1}.
\tag{4.1}
\]

There is a full expansion with successive orders \(m-n/4-j\). Every remainder has the differentiated symbol estimates in its stated order.

For excess \(e\), split \(\theta=(\theta',\theta'')\), with \(\dim\theta''=e\), so that \(\theta''\) locally parametrizes the fiber

\[
C_\xi=\{(x,\theta):\phi_\theta'=0,\ \phi_x'=\xi\}.
\]

Replace \(G\) by the Hessian \(G'\) in the \((x,\theta')\) directions. The leading coefficient becomes

\[
(2\pi)^{n/4}
\int_{C_\xi}
e^{i\pi\operatorname{sgn}G'/4}
\frac{a(x,\theta)}{|\det G'(x,\theta)|^{1/2}}\,d\theta''.
\tag{4.2}
\]

The same order and remainder conclusion holds. These are local fiber integrals on the compact part of the fiber met by the amplitude.

**Proof.** The Fourier transform has phase \(\phi(x,\theta)-x\cdot\xi\). If \(|\theta|\) is much larger or much smaller than \(|\xi|\), then \(|\phi_x'-\xi|\) is bounded below by a fixed positive multiple of \(|\theta|+|\xi|\). Repeated integration by parts in \(x\) makes those regions rapidly decreasing in \(\xi\), with every derivative. Differentiating in \(\xi\) inserts bounded powers of \(x\); the extra powers from an order estimate are absorbed by more integrations. Thus insert a cutoff restricting \(|\theta|\asymp|\xi|\).

Set \(R=|\xi|\), \(\eta=\xi/R\), and \(\theta=R\vartheta\). The phase of \(v\) becomes \(R\Psi\), where

\[
\Psi(x,\vartheta,\eta)=
\phi(x,\vartheta)+H(\eta)-x\cdot\eta.
\]

Its critical equations are \(\phi_\vartheta'=0\) and \(\phi_x'=\eta\). On the critical set, \(x=H'(\eta)\), Euler's identity gives \(\phi=0\), and \(H(\eta)=H'(\eta)\cdot\eta\). Hence the critical value is zero.

The critical set has dimension \(e\). Its tangent kernel is exactly the kernel of the Hessian of \(\Psi\), because the critical equations are its full gradient equations and the clean critical map has fibers of dimension \(e\). Thus it is a clean critical manifold in the \(n+N\) integration variables. For \(e=0\), the Hessian is invertible.

The amplitude \(a(x,R\vartheta)\) is a symbol in \(R\) of order

\[
\mu=m+(n-2N-2e)/4
\]

with bounded derivatives in \(x,\vartheta,\eta\) on the fixed compact annulus. The measure contributes \(R^N\), and clean stationary phase contributes \(R^{-(n+N-e)/2}\). Their combined order is

\[
\mu+N-\frac{n+N-e}{2}=m-\frac n4.
\tag{4.3}
\]

The prefactor in (3.2) times the stationary-phase constant is

\[
(2\pi)^{-(n+2N-2e)/4}
(2\pi)^{(n+N-e)/2}=(2\pi)^{n/4}.
\]

The symbol-remainder result of [Stationary phase and critical manifolds](stationary-phase-and-critical-manifolds.md) supplies all \(R\) derivatives and angular-parameter derivatives, in successively lower orders. Polar-coordinate differentiation converts them to the ordinary differentiated symbol bounds in \(\xi\).

In the nondegenerate case, the Hessian of the scaled phase is \(G(x,\vartheta)\). Homogeneity gives

\[
\det G(x,R\vartheta)=R^{n-N}\det G(x,\vartheta).
\]

This follows by scaling the first \(n\) rows by \(R^{-1}\) and the last \(N\) columns by \(R\) in the matrix at \(R\vartheta\). The resulting matrix is the one at \(\vartheta\). Congruence by a positive diagonal scaling preserves its signature. Returning to the original variables gives (4.1).

For excess \(e\), the differential of \(\theta''\) on each fiber can be chosen invertible, since a critical-map fiber has \(\delta x=0\) and an \(e\)-dimensional phase-variable tangent. With \(\theta''\) fixed, the Hessian in \((x,\theta')\) is invertible: a vector in its kernel extends to a full Hessian-kernel vector with \(\delta\theta''=0\), and hence is zero. Equivalently, the full symmetric Hessian has radical equal to the fiber tangent; every complementary subspace carries a nondegenerate restriction. Its determinant is homogeneous of degree \(n-N+e\); the physical fiber measure \(d\theta''\) contributes degree \(e\). Undoing the scaling therefore gives exactly (4.2), with the order in (4.3). The normal-density transformation rule in clean stationary phase makes the fiber expression independent of this split. ∎

## 5. Changing phase variables and adding a quadratic block

An invertible homogeneous change \(\theta=T(x,\eta)\) leaves an oscillatory distribution unchanged when its amplitude is replaced by

\[
\widetilde a(x,\eta)=
a(x,T(x,\eta))|\det T_\eta'(x,\eta)|.
\tag{5.1}
\]

On fixed compact-base cones the map and its inverse make the two frequency sizes comparable. Their homogeneity and the chain rule preserve the ordinary symbol order. Formula (5.1) follows first with bounded frequency support from change of variables, then with unrestricted frequency support by the bounded-family convergence in Theorem 1.1. The cutoffs need not have the same shape after transformation; their equality follows from that same defining estimate.

A stabilization adds new phase variables while preserving the Lagrangian. Homogeneity requires some care. Let \(r(\theta)>0\) be smooth and homogeneous of degree one, comparable to \(|\theta|\) on the working cone, and let \(A\) be a real symmetric invertible \(k\times k\) matrix. Set

\[
\widetilde\phi(x,\theta,\eta)=
\phi(x,\theta)+\frac{\eta^TA\eta}{2r(\theta)}.
\tag{5.2}
\]

This is homogeneous of degree one under joint dilation of \((\theta,\eta)\). Its new critical equations force \(\eta=0\); the remaining equations and the critical covector are those of \(\phi\). The Hessian gains a nondegenerate block \(A/r\).

**Proposition 5.1 (stabilized amplitude).** Suppose \(\phi\) is nondegenerate and \(a\) has the order in (3.1). There is an ordinary symbol \(\widetilde a\) of order

\[
m+\frac{n-2(N+k)}4
\]

supported where \(|\eta|\leq C r(\theta)\), such that the normalized integrals for \((\phi,a)\) and \((\widetilde\phi,\widetilde a)\) differ by a smooth function locally. Its leading restriction is

\[
\widetilde a(x,\theta,0)
\equiv
r(\theta)^{-k/2}|\det A|^{1/2}
e^{-i\pi\operatorname{sgn}A/4}a(x,\theta)
\quad\text{in the leading symbol order}.
\tag{5.3}
\]

**Proof.** Choose a smooth compactly supported \(\psi\) equal to one near zero and begin with the right side of (5.3) times \(\psi(\eta/r)\). Substitute \(\eta=rz\) in its inner integral. The measure gives \(r^k\), the phase is \(r z^TAz/2\), and stationary phase gives \((2\pi/r)^{k/2}e^{i\pi\operatorname{sgn}A/4}|\det A|^{-1/2}\). Multiplying by the amplitude factor in (5.3) leaves \((2\pi)^{k/2}a\) to leading order. The normalization in the stabilized integral has an additional factor \((2\pi)^{-k/2}\), so the leading integral agrees.

All positive-degree quadratic stationary-phase coefficients of \(\psi\) vanish, because \(\psi\) is constant near zero. Thus the explicit amplitude just constructed already gives an inner difference of order \(-\infty\), with all parameter derivatives; no successive amplitude corrections are required. Multiplying by the fixed-order symbol \(a\) preserves that rapid decrease.

The outer difference is smooth: every base derivative inserts at most a fixed power of \(|\theta|\), still integrable for a sufficiently negative symbol order. For a bounded outer-frequency cutoff, the support condition \(|\eta|\leq Cr\) also bounds the inner frequencies, so ordinary Fubini applies. Pass to unrestricted outer frequencies by the bounded-symbol convergence of Theorem 1.1. This justifies the successive integrations as distributions. ∎

The signature factor in (5.3) is the local compensation that later becomes part of the Maslov transition data. This proposition establishes one elementary phase change; a general phase-equivalence theorem still needs its own proof.

## 6. Examples and the endpoint regularity

**A delta distribution on a submanifold.** Let \(x=(t,z)\), with \(t\in\mathbb R^k\), and let \(b(z)\) be smooth with compact support. Fourier inversion gives

\[
b(z)\delta(t)=(2\pi)^{-k}\int e^{it\cdot\theta}b(z)\,d\theta.
\]

In (3.1), its amplitude is \((2\pi)^{n/4-k/2}b(z)\), of order zero. Its Lagrangian representation order is therefore

\[
m=\frac k2-\frac n4.
\tag{6.1}
\]

This agrees with the nonzero conormal directions generated by \(t\cdot\theta\).

**The identity kernel.** On \(\mathbb R^d\), the kernel \(\delta(x-y)\) lives on a base of dimension \(n=2d\) and uses \(N=d\) phase variables. Formula (3.1) becomes \((2\pi)^{-d}\int e^{i(x-y)\cdot\theta}\,d\theta\). Its order is zero. The ambient dimension is the kernel's base dimension, which differs from the dimension of its input or output manifold.

The intrinsic Lagrangian definition uses an iterated-regularity endpoint. The conormal result in Singularities along a submanifold and smooth boundary passage uses

\[
B^s_{2,\infty}:
\qquad \sup_{j\geq0}2^{js}\|\Pi_j u\|_2<\infty.
\]

This is a dyadic supremum, rather than the square sum defining \(H^s\). Conormal and Lagrangian order conventions must preserve that distinction when an iterated-regularity characterization is used. The present lesson proves phase-integral and Fourier-symbol statements; it does not replace that endpoint by a Sobolev assertion.

## 7. Exercises with complete solutions

**Exercise 7.1 (order of a normal derivative; introductory).** Find the representation order of \(\partial_{t_1}^q(b(z)\delta(t))\), with \(q\geq0\) and \(b\neq0\).

**Solution.** Its amplitude acquires \((i\theta_1)^q\), of ordinary symbol order \(q\). Therefore \(m=q+k/2-n/4\). The wavefront directions remain conormal where the corresponding leading amplitude does not vanish; differentiation does not change the phase.

**Exercise 7.2 (endpoint versus square sum; intermediate).** For a delta distribution at zero in \(\mathbb R^k\), compare \(B^{-k/2}_{2,\infty}\) with \(H^{-k/2}\).

**Solution.** The Fourier transform is one. A dyadic annulus of radius \(2^j\) has volume comparable to \(2^{jk}\), so its Fourier \(L^2\) norm is comparable to \(2^{jk/2}\). Multiplying by \(2^{-jk/2}\) gives a bounded sequence with terms bounded below. Its supremum is finite and its square sum diverges. Thus the delta distribution belongs to the Besov endpoint but not to the Sobolev endpoint. This is an exact obstruction to silently strengthening the iterated-regularity space.

**Exercise 7.3 (homogeneous stabilization; intermediate).** Explain why adding \(\eta^TA\eta/2\) directly to a degree-one phase is incompatible with its joint homogeneity, and verify (5.2).

**Solution.** Joint dilation multiplies the unscaled quadratic term by \(t^2\), while multiplying the original phase by \(t\). In (5.2), the numerator has degree two and \(r\) has degree one; their quotient has degree one. Its \(\eta\) gradient is \(A\eta/r\), which vanishes only at \(\eta=0\). There its other derivatives vanish, so the original critical equations and covector are preserved.

**Exercise 7.4 (clean order compensation; advanced).** A clean phase has \(N\) variables and excess \(e\). Under the prefactor for excess zero, an amplitude of order \(m+(n-2N)/4\) is used without changing its order. What Fourier-symbol order does the calculation yield?

**Solution.** Substitution \(\theta=R\vartheta\) contributes \(R^N\). The clean normal rank is \(n+N-e\), so stationary phase contributes \(R^{-(n+N-e)/2}\). The result has order \(m-n/4+e/2\). It is higher by \(e/2\) than the desired order. Decreasing the amplitude order by \(e/2\), as in (3.2), restores \(m-n/4\). The modified prefactor also makes the leading scalar constant \((2\pi)^{n/4}\).

**Exercise 7.5 (regular amplitude; advanced).** Show that an amplitude of order \(-\infty\) produces a smooth function, and determine which part of Theorem 1.1 becomes unnecessary.

**Solution.** Every base derivative of \(e^{i\phi}a\) is a finite sum of products of phase derivatives, bounded by polynomial powers of \(|\theta|\), with derivatives of \(a\), which decrease faster than every power. All such integrals are absolutely convergent locally, uniformly on compact base sets. Dominated differentiation therefore proves smoothness. Frequency-cutoff regularization and integration by parts are no longer needed to define these integrals.

## References

- [Guillemin–Sternberg] Victor Guillemin and Shlomo Sternberg, *Semi-classical Analysis*, January 13, 2010. [Online reading](https://math.mit.edu/~vwg/semiclassGuilleminSternberg.pdf).
- [Hörmander IV] Lars Hörmander, *The Analysis of Linear Partial Differential Operators IV: Fourier Integral Operators*, Springer, 1985.

*Written by GPT-6.1 Sol (OpenAI), Ultra, September 2026. Self-checked by the writing AI. Original text: public domain (CC0).*
