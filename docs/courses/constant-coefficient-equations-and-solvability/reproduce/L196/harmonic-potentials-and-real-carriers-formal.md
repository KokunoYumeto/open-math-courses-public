# Harmonic potentials and real carriers

*Written by GPT-6.1 Sol (OpenAI), October 2026. Self-checked by the writing AI. CC0.*

An analytic functional can have infinite order at a point. Its action on entire functions nevertheless determines its action on every holomorphic germ near a compact real carrier. An odd harmonic function in one additional real variable records that action. We construct this correspondence, prove its inverse, and identify the smallest real carrier. No convexity assumption is made on the carrier.

Basic references are André Martineau's *Supports d'une fonctionnelle analytique et croissance de sa transformée de Fourier-Borel*, Mikio Sato's *Theory of Hyperfunctions, I*, and Lars Hörmander's *The Analysis of Linear Partial Differential Operators I*. The proofs here use [Gaussian analytic localization][G], Lemma 4.1, [Poisson extension and subharmonic comparison][P], Theorems P3-P4, and the [Cauchy coefficient bounds][C]. All pairings are complex linear. The additional real coordinate is called \(t\); the original dimension is \(n\geq1\).

## 1. Local tests at an arbitrary compact real set

Let \(K\subset\mathbb R^n\) be compact. An analytic functional carried by \(K\) is a linear functional on the entire holomorphic functions satisfying, for each bounded open complex neighborhood \(W\supset K\),
\[
 |u(g)|\leq C_W\sup_W|g|.
 \tag{RC1}
\]
Write \(\mathcal A'(K)\) for this space. An unbounded supremum imposes no restriction. Every neighborhood contains a bounded smaller neighborhood, so these are the requisite every-neighborhood bounds. Set \(\mathcal A'(\varnothing)=\{0\}\).

**Lemma 1.1 (local germ action).** Every \(u\in\mathcal A'(K)\) has a unique linear action on holomorphic germs near \(K\). If \(g\) is holomorphic on \(W\supset K\), there are a compact complex neighborhood \(L\) of \(K\) contained in \(W\) and a constant \(C\) such that
\[
 |u(g)|\leq C\sup_L|g|.
 \tag{RC2}
\]
The choice can be made for each prescribed \(W\). Derivatives and compact parameter integration commute with this germ action whenever the functions are holomorphic on a common neighborhood and the relevant convergence is locally uniform there.

*Proof.* Choose a real smooth compact cutoff \(\chi\), supported in \(W\cap\mathbb R^n\), equal to one near \(K\). Extend \(\chi g\) by zero on the real space. The Gaussian functions
\[
 g_j(z)=\left(\frac j\pi\right)^{n/2}
      \int_{\mathbb R^n}e^{-j\sum(z_k-x_k)^2}\chi(x)g(x)\,dx
 \tag{RC3}
\]
are entire. Lemma 4.1 of [Gaussian analytic localization][G] proves uniform convergence to \(g\) on a fixed complex neighborhood of \(K\). Its full contour proof applies to every compact real set and to nonzero local germs. Choose a bounded smaller neighborhood there. Equation (RC1) makes \(u(g_j)\) Cauchy.

The limit does not depend on the sequence: any two entire approximating sequences converge to the same germ on a common smaller neighborhood, where (RC1) bounds their difference. This also proves linearity, independence of the representative germ, and agreement with the original action on entire tests. For any given \(W\), choose a smaller relatively compact neighborhood on which the approximation converges; (RC1) and passage to the limit give (RC2). Two continuous extensions agreeing on entire tests agree on these approximants, proving uniqueness. Uniform Cauchy estimates on a smaller neighborhood prove the derivative assertion; uniform approximation by Riemann sums proves the integration assertion. \(\square\)

In particular the germ action does not require a real distribution representative.

## 2. The extra coordinate and its normalization

Put \(d=n+1\), and let \(\sigma_d\) be the area of the unit sphere in \(\mathbb R^d\). The following radial distribution is a fundamental solution for the positive Laplacian:
\[
 E_d(X)=
 \begin{cases}
 (2\pi)^{-1}\log|X|,&d=2,\\
 ((2-d)\sigma_d)^{-1}|X|^{2-d},&d\geq3.
 \end{cases}
 \qquad \Delta E_d=\delta_0.
 \tag{RC4}
\]
Indeed these functions are locally integrable and harmonic off zero. On the radius-\(r\) sphere their outward radial derivative is \(1/(\sigma_dr^{d-1})\). Apply Green's identity outside a radius-\(r\) ball to a compact smooth test. The inner boundary term containing \(E_d\partial_r\phi\) tends to zero, and the term containing \(\phi\partial_rE_d\) tends to \(\phi(0)\). This proves (RC4), including its sign. The needed divergence identity is Theorem 2.1 of [Boundary flux and weak identities][F].

Differentiate in the last coordinate:
\[
 P(x,t)=\partial_tE_d(x,t)
       =\frac{t}{\sigma_d(|x|^2+t^2)^{d/2}}.
 \qquad \Delta P=\partial_t\delta_0.
 \tag{RC5}
\]
This is the half-normalized Poisson kernel: for \(t>0\),
\[
 \int_{\mathbb R^n}P(x,t)\,dx=\frac12,
 \qquad 2P(\cdot,t)*\phi\longrightarrow\phi
                         \quad\hbox{in }C^\infty(\mathbb R^n)
 \tag{RC6}
\]
for every compact smooth \(\phi\). To check the mass, project the plane at height \(t\) radially onto the upper unit hemisphere. Its surface Jacobian is \(t/(|x|^2+t^2)^{d/2}\), so the integral is half the sphere's area divided by \(\sigma_d\). Alternatively polar coordinates give this same hemisphere integral. For convergence, split each derivative's integral at \(|x|=r\). The near part is bounded by its modulus of continuity. On the far part, polar coordinates bound the kernel mass by \(C_nt/r\). This proves uniform convergence for every fixed derivative. For negative \(t\), oddness gives the negative of the corresponding limit.

**Lemma 2.1 (the odd harmonic lift).** Every entire \(g\) on \(\mathbb C^n\) has a unique entire function \(H_g\) on \(\mathbb C^{n+1}\) satisfying
\[
 (\Delta_z+\partial_t^2)H_g=0,\qquad
 H_g(z,0)=0,\qquad \partial_tH_g(z,0)=g(z).
 \tag{RC7}
\]
It is odd in \(t\), and is given by
\[
 H_g(z,t)=\sum_{k=0}^\infty
          \frac{(-1)^k t^{2k+1}}{(2k+1)!}\Delta_z^k g(z).
 \tag{RC8}
\]
If \(g\) is holomorphic near the closed coordinate polydisk of radius \(r\) about \(z\), and \(\sqrt n|t|<r\), then
\[
 |H_g(z,t)|\leq
 \frac{|t|}{1-n|t|^2/r^2}\sup_{|w_j-z_j|\leq r}|g(w)|.
 \tag{RC9}
\]
For local \(g\), this assertion defines a local lift on the indicated smaller region.

*Proof.* Expand the \(k\)-th Laplacian using the multinomial theorem. Cauchy's estimate gives
\[
 |\Delta_z^kg(z)|\leq
 \sum_{|\alpha|=k}\frac{k!}{\alpha!}(2\alpha)!r^{-2k}M
 \leq n^k(2k)!r^{-2k}M,
 \tag{RC10}
\]
where \(M\) is the displayed supremum and \((2\alpha)!\leq(2k)!\). The series in (RC8) is therefore bounded by
\(|t|M\sum_{k\geq0}(n|t|^2/r^2)^k/(2k+1)\), which gives (RC9). On each compact set for entire \(g\), choose one sufficiently large \(r\) and a larger common compact set of test values. Uniform convergence follows. Uniform convergence on slightly larger complex compact sets and the Cauchy formula permit all termwise derivatives. Adjacent terms cancel under the Laplacian, and the initial data follow directly. Expanding any putative solution in \(t\), the equation determines each coefficient from the preceding two and the specified initial data. This proves uniqueness and the local statement. \(\square\)

We also record the harmonic analyticity fact used below. The ball Poisson representation in [Poisson extension and subharmonic comparison][P], Theorem P3, applies to a harmonic function on a slightly larger ball by uniqueness. On a smaller ball its kernel has a convergent power series in the spatial coordinates, uniformly on the boundary sphere; the same denominator expansion used in Theorem P4 proves this. Thus harmonic functions are real analytic. A harmonic function zero on a nonempty open subset of a connected domain is zero everywhere there: propagate its zero power series along a finite chain of overlapping balls on each path in the domain.

## 3. A potential determines every analytic moment

For \(u\in\mathcal A'(K)\), use Lemma 1.1 to define
\[
 U_u(x,t)=u_y\bigl(P(x-y,t)\bigr),
          \qquad (x,t)\notin K\times\{0\}.
 \tag{RC11}
\]
The kernel is a holomorphic germ in \(y\) near \(K\). For example, for fixed real \((x,t)\) off the carrier, the real positive quantity \(|x-y|^2+t^2\) stays bounded away from zero for real \(y\in K\); a small complex neighborhood permits the uniquely normalized power in (RC5). The branch is chosen by its positive real value. The choices agree as germs. The same construction works for all real \((x,t)\) in a sufficiently small neighborhood of the chosen point.

**Theorem 3.1 (potential and residue).** The function \(U_u\) is smooth, harmonic, odd in \(t\), and tends to zero at infinity. If \(\chi\in C_c^\infty(\mathbb R^{n+1})\) is equal to one near \(K\times\{0\}\), then, for every entire holomorphic \(g\),
\[
 u(g)=-\int_{\mathbb R^{n+1}}U_u(X)\,
                         \Delta\bigl(\chi H_g\bigr)(X)\,dX.
 \tag{RC12}
\]
The integrand is supported away from the carrier. In particular the potential map is injective.

*Proof.* Fixed-order derivatives in \((x,t)\) may pass through the germ action on a common smaller complex neighborhood. Harmonicity and oddness follow from (RC5). For large \(|X|\), on one fixed bounded complex neighborhood of \(K\), the kernel is bounded by \(C|X|^{-n}\): expand its denominator about \(|X|^2\), with the complex source variable bounded. The fixed germ bound proves the stated decay.

For real \(y\) sufficiently near \(K\), distributional integration by parts and (RC5) give
\[
 \int P\bigl(X-(y,0)\bigr)\Delta(\chi H_g)(X)\,dX
     =-\partial_tH_g(y,0)=-g(y).
 \tag{RC13}
\]
The derivative of \(\chi\) vanishes there. Both sides extend holomorphically to a complex neighborhood of \(K\); the integral is over a fixed compact shell separated from it. The identity principle, coordinate by coordinate from a real open box, gives equality on that neighborhood. Lemma 1.1 permits applying \(u\) and exchanging its action with the integral. This proves (RC12). A zero potential has every entire test value zero, proving injectivity. \(\square\)

## 4. Recover the functional from an arbitrary odd harmonic potential

Write \(\mathcal H_K^-\) for the odd harmonic functions on
\(\mathbb R^{n+1}\setminus(K\times\{0\})\), and \(\mathcal H^-\) for the odd harmonic functions on all of \(\mathbb R^{n+1}\).

**Lemma 4.1 (zero residue means an entire harmonic extension).** Suppose \(W\in\mathcal H_K^-\) and
\[
 \int W\Delta(\chi H_g)=0
                 \quad\hbox{for every entire }g,
 \tag{RC14}
\]
where \(\chi\) is a compact smooth cutoff equal to one near the carrier. Then \(W\) extends to a member of \(\mathcal H^-\).

*Proof.* We may take \(\chi\) even in \(t\), since the integral is independent of the cutoff: for their difference \(\eta\), the compact smooth function \(\eta H_g\) is supported off the carrier, and integration by parts gives \(\int W\Delta(\eta H_g)=0\). Extend
\[
 F=(1-\chi)W
 \quad\hbox{smoothly by zero near }K\times\{0\},
 \qquad f=\Delta F.
 \tag{RC15}
\]
The function \(f\) is smooth, compactly supported, and odd. The convolution \(E_d*f\) is smooth on the full space: all derivatives can be transferred to the compact smooth factor, since \(E_d\) is locally integrable. Equation (RC4) shows that
\[
 A=F-E_d*f
 \tag{RC16}
\]
is an entire real harmonic odd function. We will prove that \(A=W\) off the carrier.

For an entire harmonic \(H_g\), integration by parts on the compact shell yields
\[
 \int fH_g
 =\int(-W\Delta\chi-2\nabla\chi\cdot\nabla W)H_g
 =\int W\Delta(\chi H_g)=0.
 \tag{RC17}
\]
Every harmonic polynomial in the \(n+1\) variables is a sum of its even and odd parts in \(t\). The even part pairs to zero with the odd \(f\). By uniqueness in Lemma 2.1, its odd part is \(H_g\) for the polynomial \(g=\partial_tH(\cdot,0)\). Consequently \(f\) has zero pairing with every harmonic polynomial.

Choose \(R\) with \(\operatorname{supp}f\subset B(0,R)\). For \(|X|>2R\), the Taylor expansion in \(Y\) of \(E_d(X-Y)\) converges uniformly for \(|Y|\leq R\) and consists of homogeneous harmonic polynomials in \(Y\). Here is a direct verification, also in dimension two. Expand
\[
 |X-\lambda Y|^2=|X|^2-2\lambda X\cdot Y+\lambda^2|Y|^2
 \tag{RC18}
\]
inside the power, or the logarithm, in (RC4). For real \(X,Y\), its complex \(\lambda\)-zeros have modulus \(|X|/|Y|\); when they coincide the same radius bound holds. There is therefore a holomorphic normalized logarithm on \(|\lambda|<|X|/R\), uniformly on the compact real \(Y\)-ball. Its Taylor coefficients are polynomials homogeneous of the indicated degree in \(Y\). Differentiating the harmonic kernel on a smaller ball shows each coefficient is harmonic. The constant term in dimension two is harmless, and all remaining terms follow from the logarithm expansion. Pairing this uniformly convergent expansion with \(f\) gives
\[
 (E_d*f)(X)=0\qquad (|X|>2R).
 \tag{RC19}
\]
On the complement of the carrier, \(W-A=W-F+E_d*f\) is harmonic. It vanishes outside a sufficiently large ball, by (RC19) and the compact support of \(\chi\). This complement is connected: its upper and lower half-spaces are connected, every permitted point of the middle plane has a small ball avoiding the compact carrier, and the two half-spaces join outside a large ball containing it. Harmonic analyticity from Section 2 proves \(W=A\) throughout. \(\square\)

**Theorem 4.2 (the harmonic representation).** For every compact real \(K\), the potential map gives an isomorphism
\[
 \mathcal A'(K)\ \simeq\ \mathcal H_K^-/\mathcal H^-.
 \tag{RC20}
\]
Every class has a unique representative tending to zero at infinity. For arbitrary \(U\in\mathcal H_K^-\), the corresponding functional is
\[
 u_U(g)=-\int U\Delta(\chi H_g).
 \tag{RC21}
\]
It is carried by \(K\), without a convexity or distributional-order assumption.

*Proof.* The integral is independent of the cutoff by the calculation in Lemma 4.1. Fix a bounded complex neighborhood \(W\supset K\). Choose \(\eta>0\) such that the complex \(\eta\)-neighborhood of \(K\) lies in \(W\), and choose a sufficiently small real \(\delta>0\), for instance \((4n+3)\delta<\eta\). Choose \(\chi\) supported within real distance \(\delta\) of \(K\times\{0\}\), equal to one on a smaller neighborhood.

The series estimate (RC9) on slightly larger complex boxes, followed by the Cauchy estimates, bounds \(H_g\) and its first real derivatives on \(\operatorname{supp}\chi\) by a constant depending on \(n,\delta\) times \(\sup_W|g|\). More explicitly use a source polydisk of radius \(4\sqrt n\delta\), and \(|t|\leq2\delta\). The ratio in (RC9) is at most \(1/4\), and all its source values have distance at most \((4n+2)\delta\) from \(K\). A smaller parameter box around each real point supplies the derivative bound by Cauchy's formula. Only first derivatives are needed, because
\[
 \Delta(\chi H_g)=(\Delta\chi)H_g+
                                 2\nabla\chi\cdot\nabla H_g.
 \tag{RC22}
\]
On the compact support of these cutoff derivatives, \(U\) is bounded. Equation (RC21) consequently satisfies (RC1), and defines an element of \(\mathcal A'(K)\).

Theorem 3.1 recovers this functional from its own potential. The difference \(U-U_{u_U}\) has zero residue, so Lemma 4.1 extends it harmonically and oddly across the carrier. An entire odd harmonic addition contributes zero to (RC21) by integration by parts, so the map is well-defined on the quotient. Theorem 3.1 gives injectivity and the inverse identities. Its potential tends to zero at infinity. An entire harmonic function tending to zero at infinity is zero: apply the ball maximum principle from [Poisson extension and subharmonic comparison][P], Lemma P2, to its real and imaginary parts on arbitrarily large balls. This proves uniqueness of the normalized representative. \(\square\)

## 5. Least real carriers and differentiation

**Theorem 5.1 (the smallest real carrier).** If an analytic functional has any compact real carrier, it has a smallest one. It consists exactly of the real points \(x\) at which its normalized odd harmonic potential does not extend harmonically to a neighborhood of \((x,0)\). In particular, for compact real sets,
\[
 \mathcal A'(K_1)\cap\mathcal A'(K_2)
                       =\mathcal A'(K_1\cap K_2).
 \tag{RC23}
\]
The assertion is about real carriers.

*Proof.* Potentials computed using different carriers agree for \(t\ne0\), where they act on the same holomorphic kernel germs, or by Theorem 3.1 and uniqueness after restriction to their union carrier. Harmonic continuation makes them agree wherever both are defined. Let \(S\) be the intersection of all compact real carriers. Their potentials patch to an odd harmonic function off \(S\times\{0\}\). It tends to zero at infinity, because one original carrier already supplies that decay there. Theorem 4.2 gives a functional carried by \(S\) whose normalized potential is the patched function. Injectivity on the original carrier, or on its union with \(S\), identifies it with \(u\). This proves existence of the smallest carrier, including \(S=\varnothing\), when the functional is zero.

A point outside \(S\) is outside some carrier and admits a harmonic extension. Conversely, if the normalized potential extends harmonically around \((x,0)\), reflect its extension oddly and use uniqueness on the two half-balls; it is the odd extension there. Remove a smaller real ball about \(x\) from an original carrier, and patch this extension with the old potential. Theorem 4.2 makes the remaining compact set a carrier, so \(x\notin S\). This gives the stated description. Finite intersections follow at once. \(\square\)

Call this smallest carrier \(\operatorname{supp}_{\mathcal A}u\). If \(\partial_j u\) is defined by
\[
 (\partial_j u)(g)=-u(\partial_jg),
 \qquad U_{\partial_ju}=\partial_{x_j}U_u,
 \tag{RC24}
\]
then Cauchy's estimate on nested neighborhoods shows it is carried by every carrier of \(u\). The identity follows by differentiating the kernel and using \(\partial_{y_j}P(x-y,t)=-\partial_{x_j}P(x-y,t)\). Thus differentiation does not enlarge this support, and all constant-coefficient differential operators act with their bilinear transpose signs. Multiplication by a function analytic near a carrier is defined by the germ action \((au)(g)=u(ag)\); the local product bound shows it also preserves carriers.

Finally every compact distribution defines an analytic functional with exactly the same support. Its finite-order estimate and the Cauchy bounds give (RC1). Equation (RC6), passed through the distribution pairing using convergence of all the finitely many required derivatives, gives
\[
 U_u(\cdot,t)\longrightarrow \tfrac12u\ (t\downarrow0),
 \qquad U_u(\cdot,t)\longrightarrow-\tfrac12u\ (t\uparrow0)
 \tag{RC25}
\]
in distributions. A harmonic odd extension across an open portion of the middle plane has zero trace there, so these two limits force \(u=0\) on that portion. Conversely the kernel definition extends off the ordinary distributional support. Theorem 5.1 proves support equality and hence injectivity. In particular \(\delta_a(g)=g(a)\) has potential \(P(x-a,t)\) and support \(\{a\}\).

## References

- André Martineau, *Supports d'une fonctionnelle analytique et croissance de sa transformée de Fourier-Borel*, Séminaire Schwartz, 4 (1959-1960), exposé 20. [Original article](https://www.numdam.org/item/SLS_1959-1960__4__A20_0/).
- Mikio Sato, *Theory of Hyperfunctions, I*, Journal of the Faculty of Science, University of Tokyo, Section I, 8 (1959). [Original article](https://repository.dl.itc.u-tokyo.ac.jp/records/39927).
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators I: Distribution Theory and Fourier Analysis*, second edition, Springer, 1990; 2003 reprint. Background on analytic functionals, harmonic potentials and real supports.
- The linked Gaussian, Poisson, flux and Cauchy lessons contain the complete preceding estimates used in the proof. The harmonic-moment argument in Lemma 4.1 supplies the extension step directly.

[G]: ../../AN02-L167.html#4-gaussian-smoothing-in-a-complex-neighborhood
[P]: ../../AN02-L132.html
[C]: ../../AN02-L045.html
[F]: ../../prerequisites/boundary-flux-and-weak-identities.html#the-derivative-of-a-region-is-its-oriented-surface-measure
