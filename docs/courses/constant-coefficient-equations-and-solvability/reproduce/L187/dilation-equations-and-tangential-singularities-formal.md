# Dilation equations and tangential analytic singularities

*Written by GPT-6.1 Sol (OpenAI), October 2026. Self-checked by the writing AI. Public domain (CC0).*

A dilation equation controls regularity along radial flow. Its angular data can still be singular. We prove directly that every smooth or analytic wavefront covector of a solution is perpendicular to the radial vector. The proof uses compact tests and an exact falling-factorial formula for the Euler operator. It applies to complex dilation degrees and to arbitrary open domains.

Basic references are Strohmaier and Witten [S] for the bounded-sequence analytic-wavefront convention, [Homogeneous extensions and angular moments][H] for the exact scaling-to-Euler equivalence, and [Analytic directions of holomorphic boundary values][A] for controlled cutoffs and ordinary-wavefront inclusion. Fourier evaluation is the complete preceding [Schwartz functions and Fourier inversion][F]. We reuse those exact inputs and prove the radial estimate here. A local analytic particular solution also gives the result when the Euler equation has analytic forcing.

Let \(X\subset\mathbb R^n\) be open, \(n\geq1\), let \(\lambda\in\mathbb C\), and put
\[
 E=\sum_{j=1}^n x_j\partial_{x_j}.
 \tag{1}
\]
All distributional pairings are complex-linear, and the Fourier phase is \(e^{-ix\cdot\xi}\).

## 1. The transpose equation gives an exact phase iteration

Suppose \(u\in\mathcal D'(X)\) solves \(Eu=\lambda u\). Integration by parts in the distributional definition gives, for every compact smooth test,
\[
 u\big((E+c)\psi\big)=0,\qquad c=n+\lambda .
 \tag{2}
\]
Indeed \(E^*=-E-n\).

Fix a nonzero frequency \(\xi\), and a compact test supported where \(x\cdot\xi\ne0\). On a neighborhood of its support define
\[
 a_\xi(x)=(i\,x\cdot\xi)^{-1},\qquad
 Q_\xi g=(E+c)(a_\xi g)=a_\xi(E+c-1)g .
 \tag{3}
\]
The last equality uses \(Ea_\xi=-a_\xi\). Such products are extended by zero outside the test support; the denominator remains nonzero on a neighborhood of that support.

**Lemma 1.1.** For every integer \(L\geq1\),
\[
 u(g e^{-ix\cdot\xi})
       =u(Q_\xi^L g\,e^{-ix\cdot\xi}),\qquad
 Q_\xi^L=a_\xi^L P_L(E),
 \quad P_L(E)=\prod_{j=1}^L(E+c-j).
 \tag{4}
\]

**Proof.** In (2), take \(\psi=a_\xi g e^{-ix\cdot\xi}\). The phase derivative is \(E(e^{-ix\cdot\xi})=-i(x\cdot\xi)e^{-ix\cdot\xi}\), so
\[
 (E+c)\psi=(Q_\xi g-g)e^{-ix\cdot\xi}.
 \tag{5}
\]
Equation (2) proves the first iteration. Its amplitude stays compactly supported in the same nonzero-denominator neighborhood, so iteration gives the first formula (4).

For the operator formula, \(Ea_\xi^j=a_\xi^j(E-j)\), as an identity acting on tests. If \(Q_\xi^L=a_\xi^LP_L(E)\), multiply by \(Q_\xi=a_\xi(E+c-1)\) on the left. The result is \(a_\xi^{L+1}(E+c-1-L)P_L(E)\), whose commuting Euler factors give \(P_{L+1}(E)\). The case \(L=1\) is (3), completing induction. \(\square\)

The shifts by \(j\) in (4) cannot be omitted. Multiplication by the reciprocal linear form does not commute with \(E\).

## 2. A falling factorial keeps the derivative count exact

For an operator or scalar \(z\), write
\[
 (z)_{\underline j}=z(z-1)\cdots(z-j+1),
       \qquad (z)_{\underline0}=1 .
 \tag{6}
\]
This is a falling factorial, distinct from the rising factors used in differentiating reciprocal powers.

**Lemma 2.1.** For \(b\in\mathbb C\) and \(L\geq0\),
\[
 \begin{aligned}
 (E+b)_{\underline L}
    &=\sum_{j=0}^L\binom Lj(b)_{\underline{L-j}}
                                      (E)_{\underline j},\\
 (E)_{\underline j}
    &=\sum_{|\alpha|=j}\frac{j!}{\alpha!}x^\alpha\partial^\alpha .
 \end{aligned}
 \tag{7}
\]
In particular, \(P_L(E)=(E+c-1)_{\underline L}\).

**Proof.** For nonnegative integers \(s,t\), \((s+t)_{\underline L}\) counts ordered choices of \(L\) distinct elements from two disjoint sets. If \(j\) positions are assigned to the first set, there are \(\binom Lj(s)_{\underline j}(t)_{\underline{L-j}}\) choices. Summing gives the scalar addition formula. Both sides are polynomials in \(s,t\). Fixing one nonnegative integer \(t\) gives equality for every complex \(s\), because their difference has infinitely many zeros; then fixing each complex \(s\) gives equality for every complex \(t\). Substituting the commuting operator \(E\) proves the first identity.

For the second identity, start at \(j=0\). If the right side at \(j\) is \(A_j\), Leibniz's rule gives
\[
 (E-j)A_j
    =\sum_{|\alpha|=j}\frac{j!}{\alpha!}
                     \sum_\ell x^{\alpha+e_\ell}
                                      \partial^{\alpha+e_\ell}.
 \tag{8}
\]
The \(j\) from differentiating \(x^\alpha\) cancels the displayed \(-j\). For a fixed \(\gamma\) of total order \(j+1\), its coefficient is
\[
 \sum_{\ell:\gamma_\ell>0}\frac{j!}{(\gamma-e_\ell)!}
          =\frac{j!}{\gamma!}\sum_\ell\gamma_\ell
          =\frac{(j+1)!}{\gamma!}.
 \tag{9}
\]
Thus \((E-j)A_j=A_{j+1}\), proving the formula by induction. \(\square\)

## 3. The amplitude bound has one analytic factorial scale

Fix a compact neighborhood \(K\subset X\) and a frequency cone \(\Gamma\) such that
\[
 |x\cdot\xi|\geq d|\xi|
                  \quad(x\in K,\ \xi\in\Gamma),\qquad d>0 .
 \tag{10}
\]
Let \(\chi_L\) be the cutoffs of [A], Lemma 1.1, supported in the interior of \(K\) and equal to one on a common smaller neighborhood. Every fixed-order derivative is uniformly bounded, and
\[
 \|\partial^{\alpha+\beta}\chi_L\|_\infty
        \leq C_\beta(CL)^{|\alpha|}
                  \quad(|\alpha|\leq L).
 \tag{11}
\]

**Lemma 3.1.** For every fixed integer \(m\geq0\), there is \(C_m\), independent of \(L\geq1\), \(\xi\in\Gamma\), and \(r=|\xi|>0\), such that
\[
 \max_{|\beta|\leq m}
       \|\partial^\beta[Q_\xi^L\chi_L]\|_\infty
            \leq C_m^{L+1}L^{L+m}r^{-L}.
 \tag{12}
\]

**Proof.** Put \(b=c-1\), and choose \(R\geq1\) bounding the absolute values of all coordinates on \(K\). A fixed scalar \(b\) satisfies
\[
 |(b)_{\underline q}|\leq C_b^q q!\quad(q\geq0),
 \tag{13}
\]
because the factor with index \(\ell\) has modulus at most \(C_b(\ell+1)\).

For \(|\beta|\leq m\), differentiate the second formula (7) applied to \(\chi_L\). Each derivative falling on \(x^\alpha\) contributes at most a factor \(j\), and the remaining powers are bounded by \(R^j\). The derivatives on \(\chi_L\) have the mixed bound (11), with the extra at most \(m\) derivatives in its fixed constant. Since \(\sum_{|\alpha|=j}j!/\alpha!=n^j\), this gives
\[
 \|\partial^\beta[(E)_{\underline j}\chi_L]\|_\infty
       \leq C_m L^{|\beta|}(C_1L)^j,\qquad 0\leq j\leq L .
 \tag{14}
\]
This also covers \(j=0\), using the uniform fixed-order cutoff bounds.

Use the first identity (7) and (13). Its \(j\)-th term is bounded by
\[
 C_m L^{|\beta|}
          \frac{L!}{j!}C_b^{L-j}(C_1L)^j
       \leq C_m L^{L+|\beta|}C_b^{L-j}C_1^j .
 \tag{15}
\]
Here \(L!/j!\leq L^{L-j}\). Summing \(L+1\) terms, and using \(L+1\leq2^L\) for \(L\geq1\), proves
\[
 \|\partial^\beta[P_L(E)\chi_L]\|_\infty
          \leq C_m^{L+1}L^{L+|\beta|}.
 \tag{16}
\]

For the other factor write \(\xi=r\theta\), \(|\theta|=1\). Direct repeated differentiation gives
\[
 \partial^\gamma(x\cdot\theta)^{-L}
  =(-1)^{|\gamma|}
      L(L+1)\cdots(L+|\gamma|-1)\,
          \theta^\gamma(x\cdot\theta)^{-L-|\gamma|}.
 \tag{17}
\]
For \(|\gamma|\leq m\), (10) bounds this by \(C_m^{L+1}L^{|\gamma|}\). Thus
\[
 \|\partial^\gamma a_\xi^L\|_\infty
         \leq C_m^{L+1}L^{|\gamma|}r^{-L}.
 \tag{18}
\]
Only fixed-order derivatives of this coefficient are used. Its rising factorial has at most \(m\) factors.

Finally differentiate \(a_\xi^L P_L(E)\chi_L\) with Leibniz's rule. Equations (16) and (18) give a power \(L^{L+|\beta|}\) in each split, since the two fixed derivative orders add to \(|\beta|\). The finitely many binomial constants are absorbed by increasing \(C_m\). This proves (12). \(\square\)

## 4. Dilation solutions have only tangential wavefront covectors

**Theorem 4.1.** For any \(\lambda\in\mathbb C\) and \(u\in\mathcal D'(X)\) satisfying \(Eu=\lambda u\),
\[
 \operatorname{WF}(u)\subseteq\operatorname{WF}_A(u)
             \subseteq\{(x,\xi):\xi\ne0,\ x\cdot\xi=0\}.
 \tag{19}
\]
No conic or star-shaped hypothesis on \(X\) is required.

**Proof.** If \(x_0\cdot\xi_0\ne0\), continuity gives a compact neighborhood \(K\) of \(x_0\), contained in \(X\), and a conic neighborhood \(\Gamma\) of \(\xi_0\) satisfying (10). Take the cutoffs (11) supported in its interior. The distribution \(u\) has some finite order \(m\) on this compact set:
\[
 |u(\psi)|\leq B\max_{|\beta|\leq m}\sup_K|\partial^\beta\psi|
                   \quad(\operatorname{supp}\psi\subset K).
 \tag{20}
\]
For \(N\geq1\), set \(L=N+m\) and \(u_N=\chi_Lu\). These distributions agree with \(u\) on the common cutoff plateau, have common compact support, and have a common order and bound independent of \(N\), by the uniform low-order part of (11).

Use Lemma 1.1 with \(g=\chi_L\), and apply (20) to its iterated test. Derivatives of the phase contribute at most \((1+r)^m\). Lemma 3.1 therefore gives
\[
 |\widehat u_N(\xi)|
   \leq C_m^{L+1}L^{L+m}r^{-L}(1+r)^m
             \quad(\xi\in\Gamma,\ r=|\xi|>0).
 \tag{21}
\]
For \(r\geq1\), \(r^{-L}(1+r)^m\leq2^m r^{-N}\). Moreover
\[
 (N+m)^{N+2m}
       \leq C_m^{N+1}N^{N+2m}.
 \tag{22}
\]
For example \((1+m/N)^{N+2m}\leq e^m(1+m)^{2m}\). The fixed polynomial \(N^{2m}\) is absorbed into a larger exponential constant, using \(\log N\leq N\). Thus
\[
 |\widehat u_N(\xi)|
       \leq A^{N+1}N^N(1+|\xi|)^{-N}
                         \quad(\xi\in\Gamma).
 \tag{23}
\]
The replacement of \(r^{-N}\) by \((1+r)^{-N}\) costs \(2^N\) for \(r\geq1\). For \(r\leq1\), the common compact finite-order bound on \(u_N\) supplies (23) after increasing \(A\), as in the bounded-sequence criterion of [A], Section 1.

The criterion proves analytic absence at every point with \(x\cdot\xi\ne0\). Ordinary-wavefront inclusion is [A], Theorem 3.1, proving (19). At \(x=0\) the condition \(x\cdot\xi=0\) holds for every covector; the theorem removes none there. \(\square\)

For a homogeneous distribution of degree \(\lambda\), the exact Euler identity \(Eu=\lambda u\) is [H], Lemma 1.1. Theorem 4.1 therefore applies to every distributional angular datum, including complex degrees, without requiring an angular density.

**Corollary 4.2 (radial hypersurfaces are noncharacteristic for the wavefront bound).** Let \(\Sigma\subset X\) be an analytic hypersurface defined near a point by \(\rho=0\), with \(d\rho\ne0\), and suppose \(x\cdot\nabla\rho(x)\ne0\) on \(\Sigma\). Then neither wavefront set in (19) meets its nonzero conormal bundle.

**Proof.** A conormal is \(\xi=t\nabla\rho(x)\), \(t\ne0\). Its radial pairing is \(x\cdot\xi=t\,x\cdot\nabla\rho(x)\ne0\), so Theorem 4.1 excludes it. For a sphere of radius \(a>0\), use \(\rho(x)=|x|^2-a^2\), giving \(x\cdot\xi=2ta^2\ne0\). \(\square\)

This supplies the exact conormal-disjointness hypothesis in an angular restriction calculation. The general distributional restriction theorem and its wavefront bounds remain additional operation results.

## 5. Analytic Euler forcing has a local analytic particular solution

**Theorem 5.1.** Suppose \((E-\lambda)u=f\) near \(x_0\ne0\), with \(f\) analytic there. Then
\[
 \operatorname{WF}_A(u)\cap\{(x,\xi):x\text{ near }x_0,\ x\cdot\xi\ne0\}
                                    =\varnothing .
 \tag{24}
\]
The same exclusion holds for ordinary wavefront.

**Proof.** Put \(v=x_0\), \(a=|x_0|^2>0\), and choose a small neighborhood \(V\) of \(x_0\). The function
\[
 t_0(x)=\frac{a}{v\cdot x}
 \tag{25}
\]
is positive and close to one on \(V\). Shrink \(V\) so that the real segment \(s x\), between \(s=t_0(x)\) and \(s=1\), lies in the analytic neighborhood of \(f\). Define
\[
 w(x)=\int_{t_0(x)}^1 s^{-\lambda-1}f(sx)\,ds .
 \tag{26}
\]
An integral whose lower endpoint exceeds its upper endpoint has its usual signed meaning.

We verify analyticity. Write \(s=t_0(x)+q(1-t_0(x))\), \(0\leq q\leq1\). Then
\[
 w(x)=(1-t_0(x))
       \int_0^1
       \bigl[t_0(x)+q(1-t_0(x))\bigr]^{-\lambda-1}
       f\bigl([t_0(x)+q(1-t_0(x))]x\bigr)\,dq .
 \tag{27}
\]
The analytic power series of \(f\) extends to a complex polydisk about \(x_0\). On a smaller complex neighborhood of \(x_0\), \(t_0\) is holomorphic, and all the displayed brackets are uniformly close to one for \(q\in[0,1]\). Their powers use the convergent logarithm series near one. Their products with \(x\) stay uniformly inside the polydisk of \(f\). The integrand is therefore holomorphic in \(x\), continuous in \(q\), and uniformly bounded on a smaller closed complex polydisk times \([0,1]\).

The successive circle formulas on that smaller polydisk give Taylor coefficient bounds uniform in \(q\), exactly the power-series calculation in [Holomorphic boundaries in convex cones][T], Section 3, formula (3.1). The coefficient series converges uniformly on every still smaller polydisk. Integrating its coefficients over \(q\) therefore gives a convergent holomorphic power series for (27). Its real restriction is analytic.

For positive \(t\) close to one, \(t_0(tx)=t_0(x)/t\). Substitution \(s=t\sigma\) in (26) gives
\[
 w(tx)=t^\lambda\int_{t_0(x)}^t s^{-\lambda-1}f(sx)\,ds .
 \tag{28}
\]
Differentiating at \(t=1\) proves \(Ew=\lambda w+f\). All paths lie in the chosen local neighborhood; no global radial flow is assumed.

Thus \(h=u-w\) solves \(Eh=\lambda h\) on a smaller neighborhood. Theorem 4.1 gives its tangential analytic-wavefront bound. Analytic functions have empty analytic wavefront by [A], Corollary 2.3, and its finite-sum argument gives \(\operatorname{WF}_A(u)=\operatorname{WF}_A(h)\). This proves (24); ordinary inclusion gives the final assertion. \(\square\)

**Corollary 5.2 (an analytic zeroth-order potential).** Suppose \((E-a(x))u=f\) near a nonzero point, with \(a\) and \(f\) analytic. Then the tangential wavefront exclusion (24) holds there.

**Proof.** Construction (26) with \(\lambda=0\) and forcing \(a\) gives a local analytic function \(\varphi\) with \(E\varphi=a\). Set \(v=e^{-\varphi}u\). The distributional product rule gives \(Ev=e^{-\varphi}(Eu-a u)=e^{-\varphi}f\), an analytic function. Apply Theorem 5.1 at degree zero. The multiplier and its reciprocal are analytic and nonvanishing, so [A], Theorem 2.2, gives \(\operatorname{WF}_A(v)=\operatorname{WF}_A(u)\). Ordinary inclusion gives the ordinary exclusion as well. \(\square\)

Theorem 5.1 and Corollary 5.2 assume analytic forcing on a neighborhood. They do not assert the general inhomogeneous microlocal regularity rule with arbitrary wavefront-controlled forcing.

## References

[S] Alexander Strohmaier and Edward Witten, *Analytic States in Quantum Field Theory on Curved Spacetimes*, Annales Henri Poincaré **25** (2024), 4543–4590, Appendix B. [Open-access primary article](https://link.springer.com/article/10.1007/s00023-024-01419-0), retaining its CC BY 4.0 terms. It gives the named convention; the Euler arguments used here are supplied above.

[H] [Homogeneous extensions and angular moments][H], Lemma 1.1, with its complete test-scaling proof.

[A] [Analytic directions of holomorphic boundary values][A], Lemma 1.1, its bounded-sequence definition, Corollary 2.3 and Theorem 3.1.

[F] [Schwartz functions and Fourier inversion][F], Sections 1–5.

[T] [Holomorphic boundaries in convex cones][T], Section 3, formula (3.1), with the complete successive-circle and uniform power-series calculation.

Original exposition is CC0. Linked programme proofs and external references retain their own provenance and terms. General pullback, product, restriction and projection theorems are separate mathematical results.

[H]: https://github.com/KokunoYumeto/open-math-courses-public/blob/67564e6cdda1ea9e9fef78883afc69b40417e84b/docs/courses/AN-01/src/homogeneous-extensions-and-angular-moments.md
[A]: ../../AN02-L186.html#complete-proof
[F]: https://github.com/KokunoYumeto/open-math-courses-public/blob/67564e6cdda1ea9e9fef78883afc69b40417e84b/docs/courses/AN-01/prerequisites/U011-free-foundations/schwartz-fourier-foundations-U017.md
[T]: ../../prerequisites/holomorphic-boundaries-in-convex-cones.html
