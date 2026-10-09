# Tempered tensors and stationary Gaussian equations

*Reconstructed and self-checked by GPT-6 Astra (OpenAI), Ultra reasoning effort, October 2026. Earlier edition: GPT-6.1 Sol (OpenAI), Ultra reasoning effort. Original exposition: CC0. Supplied foundations retain their stated licences.*

A coordinate product can have both point-supported and principal-value frequency terms. We first construct its tensor as a continuous functional on the whole Schwartz space. We then classify the stationary equation \(\Delta u+x\cdot\nabla u+nu=0\). Its tempered solutions are parametrized by distributions on the sphere, and all of them are smooth in physical space. Requiring Schwartz decay reduces that entire family to scalar multiples of a Gaussian.

Pairings are complex bilinear. Our Fourier maps are \(Ff(\xi)=\int e^{-ix\cdot\xi}f(x)\,dx\) and \(G=(2\pi)^{-n}RF\), where \(Rf(x)=f(-x)\). The supplied [Fourier foundation](../prerequisites/U011-free-foundations/schwartz-fourier-foundations-U017.md), F1–F5, proves compact-test density, the continuous Fourier automorphism, its transposes, coordinate identities and the Gaussian integral with its exact constant. Write
\[
 p_N(\phi)=\max_{|\alpha|\le N}\sup_x(1+|x|)^N|\partial^\alpha\phi(x)|.
\]
These increasing seminorms define that Schwartz topology. Every tempered distribution is bounded by \(Cp_N\), by F5.

The compact-test tensor, including equality of the two iterated pairings and density of product tests, is fully proved in [U021](convolution-as-addition-of-supports.md), B0–B2. For angular data we use [U018](homogeneous-extensions-and-angular-moments.md), Lemma 1.1 and Theorem 1.2, and its supplied [angular foundation](../prerequisites/U011-free-foundations/angular-foundations-U018.md), A1–A3. Those proofs include the Euler/scaling equivalence, the angular representation away from zero, concrete sphere seminorms and the complete point-jet theorem. The [scalar foundation](../prerequisites/U011-free-foundations/metric-foundation-bridges.md), §§12 and 13.1–13.5, 13.7–13.10, and the [integration foundation](../prerequisites/U011-free-foundations/banach-foundation-bridges.md), §§15.0–15.1 and 16, supply the calculus and absolute integration used below.

## Coordinate tensors retain every contact term

**Theorem 1.1 (tempered tensor and Fourier factorization).** Let \(A\in\mathcal S'(\mathbb R^p)\), \(B\in\mathcal S'(\mathbb R^q)\). Their compact-test tensor has a unique continuous extension to \(\mathcal S(\mathbb R^{p+q})\). Both iterated pairings define that extension, and
\[
 F_{p+q}(A\otimes B)=(F_pA)\otimes(F_qB).
 \tag{1.1}
\]

**Proof.** Choose bounds \(|A(\alpha)|\le C_Ap_M(\alpha)\) and \(|B(\beta)|\le C_Bp_N(\beta)\). For a joint Schwartz test set \(h(y)=A(\theta(\,\cdot\,,y))\). Each slice is a Schwartz test. The one-variable Taylor formula in a parameter direction gives
\[
 \theta(x,y+te_j)-\theta(x,y)-t\partial_{y_j}\theta(x,y)
 =t^2\int_0^1(1-s)\partial_{y_j}^2\theta(x,y+ste_j)\,ds.
\]
After any \(x\)-derivative and the weight \((1+|x|)^M\), the integral is bounded uniformly in \(x\), locally uniformly in \(y\) and \(|t|\le1\). A higher joint Schwartz seminorm gives that bound. Applying \(A\), dividing by \(t\), and letting \(t\to0\) proves differentiation under the pairing. Repetition proves smoothness and \(\partial_y^\beta h=A(\partial_y^\beta\theta)\). Moreover, for every \(k\ge0\),
\[
 \begin{aligned}
 p_k(h)
 &\le C_A\max_{\substack{|\alpha|\le M\\|\beta|\le k}}
       \sup_{x,y}(1+|x|)^M(1+|y|)^k\\
 &\hspace{40mm}{}\cdot
       |\partial_x^\alpha\partial_y^\beta\theta(x,y)|\\
 &\le C_Ap_{M+k}(\theta).
 \end{aligned}
 \tag{1.2}
\]
The last inequality uses \(1+|x|,1+|y|\le1+|(x,y)|\) and \(|\alpha|+|\beta|\le M+k\). Thus \(h\in\mathcal S\) and \(|B(h)|\le C_AC_Bp_{M+N}(\theta)\). Reversing the roles gives another continuous functional. On compact tests both are exactly the tensor of U021 B2. The cutoff approximation of Fourier foundation F1 shows that compact tests are dense in the joint Schwartz space, so these two functionals agree and the extension is unique.

For \(\alpha\in\mathcal D(\mathbb R^p)\), \(\beta\in\mathcal D(\mathbb R^q)\), absolute Fubini gives \(F_{p+q}(\alpha\otimes\beta)=F_p\alpha\otimes F_q\beta\). The functions on the right are Schwartz. Applying the already proved iterated formula shows
\[
 \begin{aligned}
 [F_{p+q}(A\otimes B)](\alpha\otimes\beta)
 &=A(F_p\alpha)B(F_q\beta)\\
 &=[(F_pA)\otimes(F_qB)](\alpha\otimes\beta).
 \end{aligned}
\]
Both sides are tempered distributions. Product-test density in U021 B2 first identifies their compact-test restrictions, and Fourier foundation F1 then identifies them on \(\mathcal S\). This proves (1.1). If a coordinate space has dimension zero, its test space is \(\mathbb C\), its Fourier map is the identity, and the statement is just scalar multiplication. \(\square\)

Let \(H(t)=1_{\{t>0\}}\) and \(P=\operatorname{pv}(1/\xi)\). **Proposition 1.2 (four complete coordinate transforms).** On \(\mathbb R^2\),
\[
 \begin{gathered}
 F[H(x_1)H(x_2)]
 =\pi^2\delta_0\otimes\delta_0\\
 {}-i\pi(\delta_0\otimes P+P\otimes\delta_0)-P\otimes P,\\
 F\left[\frac{x_2}{(1+x_1^2)(1+x_2^2)}\right]
 =-i\pi^2\operatorname{sgn}(\xi_2)e^{-|\xi_1|-|\xi_2|},\\
 F[x_1e^{-\pi x_2^2}]
 =2\pi i\delta'_0\otimes e^{-\xi_2^2/(4\pi)},\\
 F[\delta'_0\otimes e^{-x_2^2/2}]
 =i\sqrt{2\pi}\,\xi_1e^{-\xi_2^2/2}.
 \end{gathered}
 \tag{1.3}
\]

**Proof.** [U046](spectral-gaps-and-explicit-fourier-distributions.md), Proposition 1.1 and §§2–3, proves the full one-dimensional identities
\[
 \begin{gathered}
 FH=\pi\delta_0-iP,\qquad Fx=2\pi i\delta'_0,\\
 F[(1+x^2)^{-1}]=\pi e^{-|\xi|},\qquad
 F[x/(1+x^2)]=-i\pi\operatorname{sgn}(\xi)e^{-|\xi|}.
 \end{gathered}
\]
Fourier foundation F3 gives \(F(e^{-b x^2})=\sqrt{\pi/b}\,e^{-\xi^2/(4b)}\) for every \(b>0\), while F5 gives \(F\delta'_0=i\xi\). Each factor is tempered: the ordinary factors are locally integrable with polynomial bounds, and a point derivative is bounded by a Schwartz derivative seminorm. Apply Theorem 1.1 separately to the four rows. Expanding \((\pi\delta_0-iP)\otimes(\pi\delta_0-iP)\) gives the first row and its negative \(P\otimes P\) coefficient. The second row has its odd factor only in coordinate two. For the third row \(b=\pi\) makes the Gaussian coefficient one. For the fourth row \(b=1/2\) makes it \(\sqrt{2\pi}\). These operations retain every point term and every principal value. \(\square\)

## Scaling describes every stationary solution

For \(n\ge1\), let \(S=\mathbb S^{n-1}\). An angular distribution means a continuous linear form on the sphere test space of angular foundation A1, with its seminorms \(q_m\). In particular \(|T(g)|\le C_Tq_m(g)\) for some finite \(m\). This includes derivatives of point evaluation; it does not require a density or a measure.

**Lemma 2.0 (the degree-zero radial extension).** For \(T\in\mathcal D'(S)\) and \(\theta\in\mathcal S(\mathbb R^n)\), set
\[
 \begin{gathered}
 I_\theta(\omega)=\int_0^\infty r^{n-1}\theta(r\omega)\,dr,\\
 W_0(T)(\theta)=T(I_\theta).
 \end{gathered}
 \tag{2.1}
\]
This defines a tempered distribution with \(EW_0(T)=0\), where \(E=\xi\cdot\nabla_\xi\). Every distribution \(V\in\mathcal D'(\mathbb R^n)\) satisfying \(EV=0\) is exactly one such \(W_0(T)\).

**Proof.** The radial-lift chain rule from angular foundation A2 bounds an angular derivative of \(\theta(r\omega)\), through order \(k\), by
\[
 C_k\sum_{j=0}^k r^j
       \max_{|\alpha|\le k}|\partial^\alpha\theta(r\omega)|.
\]
For \(0<r\le1\), multiplying this by \(r^{n-1}\) is bounded by \(C_kp_k(\theta)r^{n-1}\). For \(r\ge1\), choose an integer \(L>n+k\); the bound is \(C_kp_{\max(k,L)}(\theta)r^{n+k-1}(1+r)^{-L}\). Both radial majorants are integrable, independently of \(\omega\). Dominated difference quotients therefore show that \(I_\theta\) is smooth on the sphere and
\[
 q_k(I_\theta)\le C_{n,k,L}p_{\max(k,L)}(\theta).
\]
Taking the finite order \(k=m\) of \(T\) proves temperedness. The same estimates show that the truncated radial integrals converge in every sphere seminorm, so applying \(T\) after this integral is justified.

For a compact test \(\theta\), the transpose of \(E\) is \(-n-E\), and
\[
 \int_0^\infty r^{n-1}(n\theta+E\theta)(r\omega)\,dr
 =\left[r^n\theta(r\omega)\right]_{0}^{\infty}=0.
\]
At zero the factor \(r^n\) tends to zero, including after every angular derivative; the upper endpoint is zero by compact support. Thus \(EW_0(T)=0\) on compact tests and hence on Schwartz tests, by density and continuity of \(E\).

Conversely, restrict \(V\) to the punctured space. U018 Lemma 1.1 gives degree-zero homogeneity, and its Theorem 1.2 gives a unique \(T\) with \(V(\theta)=T(I_\theta)\) on tests supported away from zero. Those two proofs construct \(T\) using a normalized compact annular radial function and prove the representation using a compact radial primitive. Consequently \(J=V-W_0(T)\) is supported at zero and satisfies \(EJ=0\). Angular foundation A3 gives
\[
 J=\sum_{|\alpha|\le N}c_\alpha\partial^\alpha\delta_0,
 \qquad E\partial^\alpha\delta_0=-(n+|\alpha|)\partial^\alpha\delta_0.
\]
The jets are independent by the cutoff-monomial tests in that proof. Since \(n+|\alpha|>0\), every coefficient is zero. This proves existence and uniqueness on the whole space, as well as the fact that every such initially local \(V\) is tempered. \(\square\)

**Theorem 2.1 (all stationary Gaussian drift solutions).** Put
\[
 \mathcal Lu=\Delta u+\sum_{j=1}^n x_j\partial_j u+nu,\qquad n\ge1.
\]
All solutions in \(\mathcal S'(\mathbb R^n)\), uniquely parametrized, are
\[
 u=G\bigl(e^{-|\xi|^2/2}W_0(T)\bigr),
 \qquad T\in\mathcal D'(S).
 \tag{2.2}
\]
Every one has the smooth representative
\[
 \begin{gathered}
 K_n(z)=\int_0^\infty r^{n-1}e^{-r^2/2+irz}\,dr,\\
 u(x)=(2\pi)^{-n}T_\omega\bigl(K_n(x\cdot\omega)\bigr).
 \end{gathered}
 \tag{2.3}
\]
For some finite integer \(m\), every derivative satisfies \(|\partial^\alpha u(x)|\le C_{\alpha,T}(1+|x|)^m\). The Schwartz solutions are precisely \(u(x)=C e^{-|x|^2/2}\), \(C\in\mathbb C\). In dimension zero there is one point, \(\mathcal L=0\), and every scalar is a Schwartz solution; the same Gaussian formula means the constant one.

**Proof: classify the Fourier distribution.** Let \(U=Fu\). Fourier foundation F5 gives
\[
 F\Delta u=-|\xi|^2U,\qquad
 F(x_j\partial_j u)=-\partial_{\xi_j}(\xi_jU)
                  =-\xi_j\partial_{\xi_j}U-U.
\]
The \(n\) final terms cancel \(F(nu)\). The stationary equation is therefore
\[
 EU+|\xi|^2U=0.
\]
Set \(a(\xi)=e^{|\xi|^2/2}\) and \(V=aU\) in the local space \(\mathcal D'\). A smooth function multiplies compact tests, so this is defined even though \(a\) is not a Schwartz multiplier. Testing the definitions gives \(\partial_j(aU)=a\partial_jU+(\partial_ja)U\); since \(Ea=|\xi|^2a\), the preceding equation becomes \(EV=0\). Lemma 2.0 proves \(V=W_0(T)\) with unique \(T\), yielding the necessary formula for \(U\).

In the other direction, every derivative of \(b(\xi)=e^{-|\xi|^2/2}\) is a polynomial times \(b\). The product rule and boundedness of every such polynomial times the Gaussian prove that multiplication by \(b\) is continuous on \(\mathcal S\). Thus \(U=bW_0(T)\) is tempered. Its Euler derivative is \(-|\xi|^2U\), by Lemma 2.0 and \(Eb=-|\xi|^2b\). Inverting \(F\) proves sufficiency. Multiplication by \(a\) in \(\mathcal D'\), followed by the uniqueness in Lemma 2.0, also proves injectivity of the parameter \(T\). In particular no additional origin-supported term is left over.

**Proof: identify a smooth representative.** Every moment \(\int_0^\infty r^j e^{-r^2/2}\,dr\), \(j\ge0\), is finite. The exponential series dominates an arbitrarily large power of \(r\) for \(r\ge1\), and the integrand is bounded on \([0,1]\). After an \(x\)-derivative \(\alpha\), the integrand in (2.3) acquires \((ir\omega)^\alpha\). An angular derivative through order \(m\) falls on \(\omega^\alpha\) or on the phase; the latter contributes at most a factor \(r|x|\). Derivatives of the radial lift \(\omega(\xi)=\xi/|\xi|\) are bounded on the defining annulus for \(q_m\). Hence
\[
 q_m\!\left(\partial_x^\alpha
          [e^{irx\cdot\omega}]\right)
 \le C_{\alpha,m}r^{|\alpha|}(1+r)^m(1+|x|)^m.
\]
Multiplying by \(r^{n-1}e^{-r^2/2}\) gives an integrable majorant, locally uniformly in \(x\). Difference quotients and the finite bound on \(T\) prove smoothness, differentiation through both operations, and the stated polynomial estimate.

For \(\theta\in\mathcal S(\mathbb R^n)\), this estimate makes \(\int u(x)\theta(x)\,dx\) absolutely convergent. More precisely, every angular derivative needed by \(T\) is dominated by a constant times
\[
 r^{n-1}(1+r)^m e^{-r^2/2}
                 (1+|x|)^m|\theta(x)|.
\]
Its joint integral is finite. On compact \(r,x\) rectangles, Riemann sums converge in each sphere seminorm, allowing \(T\) through the integrals; the displayed majorant controls the tails in those same seminorms. Absolute Fubini and passage to the limits give
\[
 \begin{aligned}
 \int u(x)\theta(x)\,dx
 &=(2\pi)^{-n}T\!\left(\int_0^\infty
     r^{n-1}e^{-r^2/2}F\theta(-r\omega)\,dr\right)\\
 &=[G(bW_0(T))](\theta).
 \end{aligned}
\]
The last equality is exactly the transposed inverse transform in Fourier foundation F5. This proves (2.3) as a distributional identity, not only as a formal integral.

**Proof: characterize Schwartz decay.** If \(u\in\mathcal S\), then \(U=Fu\in\mathcal S\). Consequently \(V=aU\) is a smooth function on all of \(\mathbb R^n\), although it need not be rapidly decreasing. Its distributional Euler equation is its classical one: U021 B0 proves that a continuous function defining the zero distribution vanishes pointwise. Along any ray,
\[
 \frac d{dt}V(t\xi)=t^{-1}EV(t\xi)=0,\qquad t>0.
\]
The fundamental theorem makes this value constant in \(t\), and continuity at zero gives \(V(\xi)=V(0)\). Thus \(U=c e^{-|\xi|^2/2}\). Fourier foundation F3 then gives \(u=c(2\pi)^{-n/2}e^{-|x|^2/2}\), the asserted scalar family. Conversely each such Gaussian is Schwartz, and its derivatives give \(\Delta g=(|x|^2-n)g\), \(x\cdot\nabla g=-|x|^2g\), so \(\mathcal Lg=0\). The zero-dimensional case has no coordinates or derivatives and is immediate from the scalar test space. \(\square\)

For \(n=1\), an angular distribution is simply a pair of coefficients \(a,b\), and \(W_0(T)=aH(\xi)+bH(-\xi)\). For \(n>1\), \(T=\delta_{\omega_0}\) gives a profile depending only on \(x\cdot\omega_0\); its value on the orthogonal hyperplane is the positive constant \((2\pi)^{-n}K_n(0)\). Thus smoothness of all these solutions does not imply decay.

## Exercises

**Exercise 1 (foundation).** Find the entire Fourier transform of \(H(x_1-a)H(x_2-b)\), \(a,b\in\mathbb R\). Display every tensor term and its phase.

**Exercise 2 (intermediate).** For \(\alpha,\beta>0\), set \(g(x)=e^{-\alpha x_1^2-\beta x_2^2}\). Calculate \(Fg\), \(F(x_1g)\) and \(F(x_1^2g)\), including their constants.

**Exercise 3 (foundation).** For \(r\ge0\) an integer, \(a,b\in\mathbb R\) and \(\beta>0\), transform \(\delta_a^{(r)}\otimes e^{-\beta(x_2-b)^2}\). Decide for which \(r\) its transform is an ordinary function.

**Exercise 4 (intermediate).** Express every one-dimensional tempered stationary solution using the two angular coefficients. Find a first-order differential identity for the one-sided Gaussian integral, verify the stationary equation, and identify the Schwartz solutions.

**Exercise 5 (advanced).** In dimension two take \(T=\delta_{(1,0)}\). Give the physical profile, verify its stationary equation by a radial integration by parts, and prove that it is smooth and tempered but not Schwartz.

**Exercise 6 (advanced).** On the circle write \(\omega(\theta)=(\cos\theta,\sin\theta)\), and let \(T(\phi)=-\phi'(0)\) in this coordinate. Express its solution through the profile from Exercise 5. Verify the equation and find its exact linear growth on the line \(x_1=0\).

**Exercise 7 (advanced).** For \(\kappa>0\) classify all tempered and all Schwartz solutions of \(\Delta u+\kappa x\cdot\nabla u+\kappa n u=0\), \(n\ge1\). Keep the scale factors in both Gaussians.

**Exercise 8 (intermediate).** Show that no nonzero polynomial solves the stationary equation for \(n\ge1\). For \(g=e^{-|x|^2/2}\), calculate \(\mathcal L(\partial^\alpha g)\), and prove that every displayed derivative is a nonzero Schwartz eigenfunction.

## Solutions

**Solution 1.** Substitution in the ordinary Fourier integral gives \(F(\tau_cf)=e^{-ic\cdot\xi}Ff\); transposing the same test identity proves it for tempered distributions. Theorem 1.1 therefore gives
\[
 \begin{aligned}
 &\pi^2\delta_0\otimes\delta_0
 -i\pi\delta_0\otimes(e^{-ib\xi_2}P)\\
 &\quad{}-i\pi(e^{-ia\xi_1}P)\otimes\delta_0
 -(e^{-ia\xi_1}P)\otimes(e^{-ib\xi_2}P).
 \end{aligned}
\]
The phase takes value one at a delta supported at zero. Each remaining phase has bounded derivatives, so multiplication with \(P\) is a continuous Schwartz transpose. The final coefficient is \((-i)^2=-1\).

**Solution 2.** Put \(C=\pi/\sqrt{\alpha\beta}\) and \(Q(\xi)=e^{-\xi_1^2/(4\alpha)-\xi_2^2/(4\beta)}\). The Gaussian formula and tensor factorization give \(Fg=CQ\). The coordinate identity \(F(x_1f)=i\partial_{\xi_1}Ff\) gives
\[
 F(x_1g)=-\frac{iC\xi_1}{2\alpha}Q,\qquad
 F(x_1^2g)=C\left(\frac1{2\alpha}
                    -\frac{\xi_1^2}{4\alpha^2}\right)Q.
\]
Indeed \(\partial_{\xi_1}Q=-\xi_1Q/(2\alpha)\) and \(\partial_{\xi_1}^2Q=(\xi_1^2/(4\alpha^2)-1/(2\alpha))Q\); the square uses \(i^2=-1\). These are Schwartz functions.

**Solution 3.** Direct evaluation on a Fourier test, or the translation and derivative identities, gives \(F\delta_a^{(r)}=(i\xi_1)^re^{-ia\xi_1}\). The other factor has transform \(\sqrt{\pi/\beta}\,e^{-ib\xi_2-\xi_2^2/(4\beta)}\). Their tensor is the ordinary smooth function
\[
 \sqrt{\pi/\beta}\,(i\xi_1)^r
          e^{-i(a\xi_1+b\xi_2)-\xi_2^2/(4\beta)}.
\]
It has polynomial growth for every permitted \(r\), including zero. No frequency delta remains.

**Solution 4.** Define \(I(z)=\int_0^\infty e^{-r^2/2+izr}\,dr\). Formula (2.3) yields
\[
 u(x)=\frac{aI(x)+bI(-x)}{2\pi},\qquad a,b\in\mathbb C.
\]
Gaussian moments justify all derivatives. Integrate the derivative of \(e^{-r^2/2+izr}\) over the half-line; its boundary difference is \(-1\). Thus
\[
 \int_0^\infty r e^{-r^2/2+izr}\,dr=1+izI(z),
 \qquad I'(z)=i-zI(z).
\]
Differentiation gives \(I''+zI'+I=0\). The chain rule shows that \(I(-x)\) satisfies the same equation in \(x\), so every displayed \(u\) is stationary. Its transform is \(e^{-\xi^2/2}(aH(\xi)+bH(-\xi))\). When \(a\ne b\), a continuous representative is impossible at zero: on each open half-line it would equal the displayed smooth function by uniqueness of continuous distribution representatives, and its two limits disagree. It is therefore not Schwartz. When \(a=b\), the full Gaussian integral gives \(I(x)+I(-x)=\sqrt{2\pi}e^{-x^2/2}\), so \(u=a e^{-x^2/2}/\sqrt{2\pi}\).

**Solution 5.** Here \(u(x)=J(x_1)/(2\pi)^2\), with
\[
 J(z)=\int_0^\infty r e^{-r^2/2+izr}\,dr.
\]
Every derivative is bounded by a finite Gaussian moment, so \(u\) is smooth, bounded and tempered. Differentiation in \(z\) gives
\[
 \begin{aligned}
 J''(z)+zJ'(z)+2J(z)
 &=\int_0^\infty(2r-r^3+izr^2)e^{-r^2/2+izr}\,dr\\
 &=\left[r^2e^{-r^2/2+izr}\right]_0^\infty=0.
 \end{aligned}
\]
The equation in two dimensions follows because \(u\) is independent of \(x_2\). The primitive \(-e^{-r^2/2}\) gives \(J(0)=1\). Hence \(u(0,x_2)=(2\pi)^{-2}\) on an unbounded line, which excludes Schwartz decay.

**Solution 6.** The angular derivative of \(x\cdot\omega(\theta)\) at zero is \(x_2\). Thus
\[
 u(x)=-\frac{x_2J'(x_1)}{(2\pi)^2}
      =-\frac{i x_2}{(2\pi)^2}
            \int_0^\infty r^2e^{-r^2/2+irx_1}\,dr.
\]
The same moment estimates bound all derivatives by \(C_\alpha(1+|x_2|)\). Differentiating the profile equation gives \(J'''+zJ''+3J'=0\). Applying \(\Delta+x\cdot\nabla+2\) to \(x_2J'(x_1)\) produces \(x_2(J'''+x_1J''+3J')\), so the result is zero. Finally,
\[
 \int_0^\infty r^2e^{-r^2/2}\,dr
 =\int_0^\infty e^{-r^2/2}\,dr=\sqrt{\pi/2},
\]
by integration by parts with vanishing \(r e^{-r^2/2}\) endpoints and the Gaussian mass. Therefore \(u(0,x_2)=-i\sqrt{\pi/2}\,x_2/(2\pi)^2\), an exact nonzero linear profile.

**Solution 7.** Fourier transformation gives \(\kappa EU+|\xi|^2U=0\). In \(\mathcal D'\) set \(V=e^{|\xi|^2/(2\kappa)}U\); its Euler derivative vanishes. Lemma 2.0 consequently gives all solutions, uniquely,
\[
 u=G\bigl(e^{-|\xi|^2/(2\kappa)}W_0(T)\bigr),
 \qquad T\in\mathcal D'(S).
\]
The decreasing Gaussian is a Schwartz multiplier because \(\kappa>0\). Replacing \(e^{-r^2/2}\) by \(e^{-r^2/(2\kappa)}\) in (2.3) proves that all these solutions are smooth with polynomial derivative bounds. If \(u\) is Schwartz, the same ray and continuity-at-zero argument makes \(V\) constant. Inversion now yields \(u=C e^{-\kappa|x|^2/2}\); for frequency coefficient \(c\), the precise physical coefficient is \(c(\kappa/(2\pi))^{n/2}\). Conversely \(\Delta g=(\kappa^2|x|^2-\kappa n)g\) and \(\kappa x\cdot\nabla g=-\kappa^2|x|^2g\) verify the equation for that Gaussian.

**Solution 8.** If a nonzero polynomial has leading homogeneous part \(p_d\), the degree-\(d\) part of \(\mathcal Lp\) is \((d+n)p_d\): the Laplacian lowers degree by two and \(x\cdot\nabla p_d=dp_d\) on each monomial. It is nonzero because \(d+n>0\).

For a smooth \(v\), the product rule gives
\[
 \mathcal L(\partial_jv)=\partial_j(\mathcal Lv)-\partial_jv.
\]
Iterating over the \(|\alpha|\) individual derivatives proves
\[
 \mathcal L(\partial^\alpha g)=-|\alpha|\partial^\alpha g,
 \qquad g=e^{-|x|^2/2}.
\]
Each derivative is a polynomial times \(g\), hence Schwartz by Gaussian decay. Its polynomial has highest homogeneous term \((-1)^{|\alpha|}x^\alpha\). Indeed, in one differentiation the polynomial derivative lowers degree, while multiplication by \(-x_j\) raises degree and gives that leading term inductively. Thus every displayed function is nonzero. This constructs the stated eigenfunctions without asserting that they exhaust any operator spectrum.

## References

- Semyon Dyatlov, [*Lecture notes for 18.155: distributions, elliptic regularity, and applications to PDEs*](https://math.mit.edu/~dyatlov/18.155/155-notes.pdf), author-hosted edition dated 2 October 2026, §7.1, Theorem 7.1, and §5.1. The complete tensor proof was compared with the supplied U021 construction. The homogeneous definitions and origin-supported uniqueness argument were also compared. The source leaves the Euler equivalence and general angular construction to other treatments; the exact U018 and angular-foundation proofs used here supply them in full.
- The exact programme proof inputs are linked at the start and at their points of use. U046 supplies the full one-dimensional transforms, and Fourier foundation F3 supplies the Gaussian constants. Every further Schwartz estimate, stationary classification step and exercise solution is proved above. The scalar and integration components retain their CC0 1.0 notices; the reconstructed exposition is CC0.
