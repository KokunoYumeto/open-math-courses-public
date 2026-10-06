# Regularity and tempered growth

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026. Self-checked by GPT-6.1 Sol (OpenAI). Public domain (CC0).*

Every nonzero constant-coefficient polynomial has a regular fundamental solution. Regularity controls its Fourier transform after compact cutoffs; it does not bound its growth on all of space. We now prove a necessary condition for having regularity and tempered growth simultaneously. Positive limiting symbols must have uniformly integrable reciprocals. A degenerate diffusion equation will violate that condition even though it has a tempered causal inverse.

Read [Symbols at infinity](symbols-at-infinity.md), [Regular kernels and changes in the equation](regular-kernels-and-parameter-changes.md), and [Wavefronts of regular kernels](wavefronts-of-regular-kernels.md). We use the Fourier transform on tempered distributions and the Schwartz topology from Grubb's freely readable lecture chapter §5 [Grubb], especially the fixed-seminorm bound (5.21) and Theorems 5.16–5.17; Melrose's notes [Melrose] give additional background. Coste [Coste] provides background on the algebraic asymptotics used below.

Keep \(D=-i\partial\) and the negative-exponential Fourier transform. For \(P\ne0\), \(S_P\) is its full derivative norm and \(\mathcal L(P)\) its set of normalized localizations. A positive localization here means a real polynomial \(Q\) with \(Q(\xi)>0\) for every real \(\xi\), still normalized by \(|Q|_J=1\).

## A necessary uniform integral bound

**Theorem 1.1.** If \(P(D)\) has a fundamental solution
\[
E\in\mathcal S'(\mathbb R^n)
\cap B_{\infty,S_P}^{\mathrm{loc}}(\mathbb R^n),
\tag{1}
\]
then there is a finite constant \(C\) such that
\[
\int_{|\xi|<1}\frac{d\xi}{Q(\xi)}\leq C
\tag{2}
\]
for every positive \(Q\in\mathcal L(P)\).

The constant is uniform over normalized positive localizations. Their individual lower bounds can tend to zero.

**Proof.** Fix such a \(Q\). It belongs to some directional set by compactness of the unit sphere of directions. The polynomial-path theorem gives a real polynomial path \(\eta(t)\), tending to infinity, with
\[
P_t(\xi)=\frac{P(\xi+\eta(t))}{S_P(\eta(t))}
\longrightarrow Q(\xi)
\tag{3}
\]
in coefficient norm. If \(m=\deg P\), then
\[
|P_t(\xi)-Q(\xi)|
\leq C_Qt^{-1}(1+|\xi|)^m
\tag{4}
\]
for large \(t\). To verify the rate, every coefficient of the numerator in (3) is a polynomial in \(t\). The squared denominator is the sum of their squared absolute values with the derivative weights, so its leading term is \(a^2t^{2\sigma}\), \(a>0\). Factoring this term gives
\[
S_P(\eta(t))=at^\sigma(1+O(t^{-1})).
\]
No numerator coefficient can have degree greater than \(\sigma\). Dividing its polynomial by this expression has its limiting constant plus \(O(t^{-1})\). The finite coefficient norm and the Taylor formula give (4).

Positivity and the algebraic lower-bound argument of the symbols-at-infinity lesson give
\[
Q(\xi)\geq c_Q(1+|\xi|)^{-N}
\tag{5}
\]
for some \(N\geq0\). In particular \(1/Q\) is a smooth function of polynomial growth and defines a tempered distribution.

Set
\[
E_t=S_P(\eta(t))e^{-ix\cdot\eta(t)}E.
\tag{6}
\]
It is tempered. Modulation of the equation gives \(P_t(D)E_t=\delta_0\), hence
\[
P_t\widehat E_t=1.
\tag{7}
\]
Choose \(a,\delta>0\) small enough that, for \(T(t)=at^\delta\), (4) and (5) imply
\[
\begin{gathered}
|P_t(\xi)-Q(\xi)|\leq\tfrac12c_Q(1+|\xi|)^{-N},\\
|P_t(\xi)|\geq\tfrac12c_Q(1+|\xi|)^{-N},\\
|\xi|\leq T(t).
\end{gathered}
\tag{8}
\]
For example take \(\delta(m+N)<1\) when \(m+N>0\), then increase the lower bound on \(t\). If \(m+N=0\), any fixed positive \(\delta\) works after doing so. Equation (7), multiplied locally by the smooth reciprocal of \(P_t\), gives
\[
\widehat E_t=1/P_t
\quad\text{on the ball }|\xi|<T(t).
\tag{9}
\]

We claim
\[
\widehat E_t\longrightarrow1/Q
\quad\text{in }\mathcal S'.
\tag{10}
\]
The tail estimate is essential here; (9) alone gives only convergence on compactly supported frequency tests.

Take \(h\in\mathcal S\), and choose a smooth cutoff \(\chi\) supported in the unit ball, equal to one on the half-unit ball. Write \(h=h_{\rm in}+h_{\rm out}\), where \(h_{\rm in}(\xi)=\chi(\xi/T(t))h(\xi)\). On the inner part, (4), (5), and (8) give
\[
\begin{aligned}
&|\langle\widehat E_t-Q^{-1},h_{\rm in}\rangle|\\
&\quad\leq C_Qt^{-1}
\int(1+|\xi|)^{m+2N}|h(\xi)|\,d\xi\\
&\quad\longrightarrow0.
\end{aligned}
\tag{11}
\]
The tail pairing with \(1/Q\) also tends to zero, since this function has polynomial growth and \(h_{\rm out}\) is supported outside a ball of radius \(T(t)/2\).

For the other tail, temperedness provides some \(M\) and a constant \(C_E\) such that
\[
\begin{aligned}
|\langle\widehat E,g\rangle|
&\leq C_E\max_{|\beta|\leq M}\\
&\quad\sup_\xi(1+|\xi|)^M|\partial^\beta g(\xi)|.
\end{aligned}
\tag{12}
\]
If the path has degree \(k\), then \(|\eta(t)|\leq C t^k\) and \(S_P(\eta(t))\leq Ct^\sigma\). The Fourier transform of (6) is the translate of \(\widehat E\) multiplied by that scalar. Applied to \(h_{\rm out}\), (12) therefore gives
\[
\begin{aligned}
&|\langle\widehat E_t,h_{\rm out}\rangle|\\
&\quad\leq C t^{\sigma+kM}\max_{|\beta|\leq M}\\
&\qquad\sup_\xi(1+|\xi|)^M
|\partial^\beta h_{\rm out}(\xi)|.
\end{aligned}
\tag{13}
\]
Indeed translating a test function by \(\eta(t)\) enlarges its weight by at most \(C(1+|\eta(t)|)^M\). The derivatives of the dilated cutoff are bounded by nonpositive powers of \(T(t)\), and every surviving term is supported where \(|\xi|\geq T(t)/2\). Schwartz decrease thus bounds the last maximum by \(C_L T(t)^{-L}\) for any \(L\). Choose \(L>(\sigma+kM)/\delta\). Equation (13) tends to zero. Together with (11) this proves (10). These estimates are uniform for \(h\) in any bounded subset of \(\mathcal S\), so they also give convergence in the strong distribution topology.

Now fix \(\phi\in C_c^\infty(\mathbb R^n)\). Regularity of the original \(E\) gives a constant \(C_\phi\), independent of the path and of \(Q\), with
\[
\begin{aligned}
|\langle E_t,\phi\rangle|
&=S_P(\eta(t))
|\widehat{\phi E}(\eta(t))|\\
&\leq C_\phi.
\end{aligned}
\tag{14}
\]
Fourier inversion on tempered distributions and (10) imply
\[
\left|(2\pi)^{-n}
\int\frac{\widehat\phi(-\xi)}{Q(\xi)}\,d\xi\right|
\leq C_\phi.
\tag{15}
\]

Choose once and for all a real nonnegative \(\psi\in C_c^\infty(B(0,r))\) of integral one, with \(r<1/2\), and let
\[
\widetilde\psi(x)=\psi(-x),\qquad
\phi=\psi*\widetilde\psi.
\]
Then \(\widehat\phi=|\widehat\psi|^2\geq0\). For \(|\xi|\leq1\),
\[
|\widehat\psi(\xi)-1|
\leq\int|x\cdot\xi|\psi(x)\,dx
\leq r,
\]
so \(\widehat\phi(\xi)\geq1/4\) there. Its modulus is even because \(\psi\) is real. Positivity of \(Q\) makes the integral in (15) nonnegative, and yields
\[
\int_{|\xi|<1}Q(\xi)^{-1}\,d\xi
\leq4(2\pi)^n C_\phi.
\tag{16}
\]
The choice of \(\phi\) is fixed, so this constant is independent of \(Q\). \(\square\)

The constants in the convergence proof can depend on \(Q\). Uniformity in the final conclusion comes entirely from applying the original regular estimate to the same physical cutoff \(\phi\).

## A degenerate diffusion equation

Consider four variables, written \((x,t)\in\mathbb R^3\times\mathbb R\), with symbol
\[
P(\xi,\tau)=\xi_1^2\xi_2^2+2\xi_3^2+i\tau.
\tag{17}
\]
Its differential operator is
\[
\begin{gathered}
P(D)=\partial_t+A(D_x),\\
A(\xi)=\xi_1^2\xi_2^2+2\xi_3^2\geq0.
\end{gathered}
\tag{18}
\]

**Proposition 2.1.** This operator has a tempered fundamental solution supported in \(t\geq0\). It is the unique tempered fundamental solution with that support. The operator has no fundamental solution that is both regular and tempered.

**Proof: the inverse and its causal uniqueness.** Define \(E_+\) by the spatial inverse Fourier transform of
\[
H(t)e^{-tA(\xi)}.
\tag{19}
\]
Precisely, for \(\varphi\in\mathcal S(\mathbb R^4)\), set
\[
\begin{aligned}
\langle E_+,\varphi\rangle
&=(2\pi)^{-3}\int_0^\infty\int_{\mathbb R^3}\\
&\quad e^{-tA(\xi)}
\widehat{\varphi(\cdot,t)}(-\xi)\,d\xi\,dt.
\end{aligned}
\tag{20}
\]
The integrand is bounded by the absolute value of the partial Fourier transform of the Schwartz test, since \(A\geq0\). For instance its product with \((1+t)^2(1+|\xi|)^4\) is bounded by a Schwartz seminorm. The inverse of that weight is integrable on this half-space. Thus (20) is a continuous functional on \(\mathcal S\), and is tempered with support in \(t\geq0\).

Integration by parts in \(t\), or differentiation of (19) as a distribution, gives
\[
(\partial_t+A(\xi))
\big(H(t)e^{-tA(\xi)}\big)=\delta_0(t).
\tag{21}
\]
The boundary value at \(t=0\) is the constant \(1\) in spatial frequency, whose inverse transform is \(\delta_0(x)\). Hence \(P(D)E_+=\delta_0(x,t)\).

For uniqueness let \(w\) be the difference of two tempered causal inverses. Its partial spatial Fourier transform \(\widetilde w\) is tempered, has support in \(t\geq0\), and solves
\[
(\partial_t+A(\xi))\widetilde w=0.
\]
In the space of distributions, without any growth requirement on the multiplier, \(v=e^{tA(\xi)}\widetilde w\) is well defined locally and satisfies \(\partial_t v=0\). Such a distribution has the form \(v=C(\xi)\otimes1\): for a compactly supported test \(h(\xi,t)\), subtract \(\rho(t)\int h(\xi,s)\,ds\), where \(\int\rho=1\). The difference has zero time integral and is a time derivative of a compactly supported smooth function, so \(v\) annihilates it. This proves the asserted form. Choose \(\rho\) supported in \(t<0\). Causality then gives \(C=0\), hence \(w=0\).

**Proof: the obstruction.** For \(a>0\), take centers \(\eta_s=(0,s,as,0)\) in the four frequency variables. Translating (17), dividing by \(s^2\), and then letting \(s\to\infty\) gives the polynomial \(\xi_1^2+2a^2\). The leading derivative norm is
\[
\begin{gathered}
S_P(\eta_s)/s^2\longrightarrow\sqrt{4+4a^4},\\
\sqrt{4+4a^4}=2\sqrt{1+a^4}.
\end{gathered}
\tag{22}
\]
Indeed the undifferentiated value is \(2a^2s^2\), the second \(\xi_1\)-derivative is \(2s^2\), and every other derivative is \(O(s)\) or \(O(1)\). Therefore
\[
Q_a(\xi,\tau)=
\frac{\xi_1^2+2a^2}{2\sqrt{1+a^4}}
\in\mathcal L(P).
\tag{23}
\]
It is positive for every real frequency.

The box with all four coordinate absolute values less than \(r=1/4\) lies in the unit ball. Integrating on this box gives
\[
\begin{aligned}
&\int_{|\zeta|<1}\frac{d\zeta}{Q_a(\zeta)}\\
&\quad\geq 2(2r)^3\int_{-r}^r\frac{ds}{s^2+2a^2}\\
&\quad=\frac{4(2r)^3}{\sqrt2\,a}
\arctan\left(\frac r{\sqrt2\,a}\right).
\end{aligned}
\tag{24}
\]
For \(0<a\leq r/\sqrt2\), the arctangent is at least \(\pi/4\), so this is at least \(\pi/(8\sqrt2\,a)\). It diverges as \(a\to0\), contradicting the necessary uniform bound of Theorem 1.1. No inverse can have both properties. \(\square\)

Consequently \(E_+\) is tempered but not regular, whereas every regular inverse supplied by the averaging construction is untempered. The equation is the same; the two existence statements concern different choices and different estimates.

There is no unrestricted uniqueness among tempered inverses. The symbol (17) vanishes at zero, so \(P(D)1=0\). Hence \(E_++c\) is a tempered fundamental solution for every constant \(c\). The support requirement \(t\geq0\) in Proposition 2.1 is what makes its uniqueness true.

## Exercises with complete solutions

**Exercise 1. Why normalization is necessary.** If \(Q\) is a positive localization, explain why a bound uniform over all its positive scalar multiples cannot hold. What set is used in Theorem 1.1?

**Solution.** For \(\lambda>0\), the integral of \(1/(\lambda Q)\) is \(\lambda^{-1}\) times that of \(1/Q\), and becomes arbitrarily large as \(\lambda\to0\). The theorem uses only coefficient-normalized limits \(Q\in\mathcal L(P)\), with \(|Q|_J=1\), rather than all nonzero multiples allowed by the broader word “localization.”

**Exercise 2. Strict positivity and a zero minimum at infinity.** Show that
\[
q(u,v)=(uv-1)^2+u^2
\tag{25}
\]
is positive everywhere but has infimum zero. Give an explicit polynomial lower bound in terms of \(|(u,v)|\).

**Solution.** A zero would require both \(u=0\) and \(uv=1\), which is impossible. Along \((u,v)=(s^{-1},s)\), its value is \(s^{-2}\to0\). Put \(R=\sqrt{u^2+v^2}\). If \(|uv-1|\geq1/2\), then \(q\geq1/4\). Otherwise \(|uv|>1/2\), so \(v\ne0\) and \(|u|>1/(2|v|)\), giving \(q\geq u^2>1/(4R^2)\). In both cases \(q\geq1/[4(1+R)^2]\). Thus strict positivity does not give a constant positive lower bound, but is compatible with (8) of the symbols-at-infinity lesson.

**Exercise 3. A growing ball is insufficient by itself.** Let \(T_j=j\) and \(u_j=e^{j^2}\delta_{2j}\) on the real frequency line. Show that \(u_j\) vanishes on \((-T_j,T_j)\), yet does not tend to zero in \(\mathcal S'\).

**Solution.** Its support is the point \(2j\), outside that interval. Take \(h(\xi)=e^{-\xi^2/8}\), a Schwartz function. Then
\[
\langle u_j,h\rangle=e^{j^2}e^{-(2j)^2/8}
=e^{j^2/2}\to\infty.
\]
This explains why the tail estimate (13), using the polynomial growth of the modulation factors and the fixed tempered distribution \(E\), is required in the proof of Theorem 1.1.

**Exercise 4. The test stays fixed.** Identify all quantities in the proof of Theorem 1.1 that may depend on \(Q\), and explain why the final integral constant still does not.

**Solution.** The polynomial path, its degree, the coefficient convergence constant, the positive lower-bound constants \(c_Q,N\), and the parameters \(a,\delta\) of the growing ball can all depend on \(Q\). They are used only to prove the limit (10) for that individual localization. The physical cutoff \(\phi=\psi*\widetilde\psi\) is chosen once. Its regular estimate \(S_P(\eta)|\widehat{\phi E}(\eta)|\leq C_\phi\) holds for every center with the same constant. Passing to the limit separately for each \(Q\) therefore gives the common bound \(4(2\pi)^n C_\phi\).

**Exercise 5. Changing the diffusion coefficient.** Replace \(2\xi_3^2\) in (17) by \(c\xi_3^2\), where \(c>0\). Compute the normalized localization along \((0,s,as,0)\), and show that the same obstruction persists.

**Solution.** The leading undifferentiated coefficient is \(ca^2s^2\), and the second \(\xi_1\)-derivative remains \(2s^2\). All other derivatives are of lower order in \(s\). The localization is
\[
Q_{a,c}=
\frac{\xi_1^2+ca^2}{\sqrt{4+c^2a^4}}.
\]
It is positive. Its reciprocal integral on the same box is bounded below by a positive constant times
\[
\int_{-r}^r\frac{ds}{s^2+ca^2}
=\frac2{\sqrt c\,a}
\arctan\left(\frac r{\sqrt c\,a}\right),
\]
which diverges as \(a\to0\). Since \(A_c\geq0\), formula (20) still constructs its unique tempered causal inverse, and Theorem 1.1 still excludes regular tempered inverses.

## References

- **[Grubb]** Gerd Grubb, *Distributions and Operators*, author-hosted lecture chapter §5, *Fourier transformation of distributions*: §§5.1–5.3, Definitions 5.1 and 5.8, estimate (5.21), Example 5.11, and Theorems 5.16–5.17 (native pp. 5.1, 5.9 and 5.11–5.14). [Exact freely readable chapter](https://www.math.ku.dk/~grubb/dist5.pdf). [Author's notes](https://web.math.ku.dk/~grubb/).
- **[Melrose]** Richard Melrose, *Introduction to Microlocal Analysis*, chapters on distributions and Fourier analysis. [MIT notes](https://math.mit.edu/~rbm/iml/).
- **[Coste]** Michel Coste, *Real Algebraic Sets*, lecture notes, 2003, §1.1 and §1.5. [ICTP notes](https://indico.ictp.it/event/a02455/session/9/contribution/6/material/0/0.pdf).
