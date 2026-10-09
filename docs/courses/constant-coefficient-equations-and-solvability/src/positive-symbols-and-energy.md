# Positive symbols and energy estimates

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026. Self-checked by GPT-6.1 Sol (OpenAI). Public domain (CC0).*

A nonnegative polynomial symbol gives a nonnegative quadratic form. On a bounded set, that form controls the quadratic form of every weaker operator, even when the symbol vanishes at real frequencies. The proof turns a quadratic expression into a linear Fourier-space estimate by using the autocorrelation of a test function.

Read [Operator strength and local inverses](operator-strength-and-local-inverses.md) and [Measuring regularity with weighted Fourier spaces](weighted-fourier-spaces.md) first. We use the Parseval–Plancherel theorem with the unnormalized Fourier transform. [Fourier transforms, finite spectra and convex separation](../prerequisites/prerequisite-bridges.html), Theorem 2.1 and Sections 7.1–7.3, proves the Schwartz identity, its extension to the completed L² space and its agreement with ordinary inverse integrals. We use that written proof with its stated normalization. Grubb [Grubb] is a basic reference for the Fourier background.

Throughout, \(D=-i\partial\), \(P\ne0\), and
\[
S_P(\xi)=\left(\sum_\alpha|\partial^\alpha P(\xi)|^2\right)^{1/2}.
\]
The pairing in this lesson is the Hilbert-space pairing
\((v,u)=\int v\overline u\,dx\), linear in its first argument. Distributional transposition elsewhere in the course remains complex-linear and uses \(P(-D)\).

## The autocorrelation identity

For \(u\in C_c^\infty(\mathbb R^n)\), put
\[
\widetilde u(x)=\overline{u(-x)},\qquad v=u*\widetilde u.
\]
Both functions are smooth and compactly supported, and
\[
\begin{aligned}
\widehat{\widetilde u}(\xi)&=\overline{\widehat u(\xi)},\\
\widehat v(\xi)&=|\widehat u(\xi)|^2.
\end{aligned}
\tag{1}
\]
In particular, for any polynomial \(Q\), Fourier inversion and Parseval give
\[
\begin{aligned}
Q(D)v(0)&=(2\pi)^{-n}\int Q(\xi)|\widehat u(\xi)|^2\,d\xi\\
&=\int Q(D)u\,\overline u\,dx.
\end{aligned}
\tag{2}
\]
All integrals converge absolutely, since \(\widehat u\) is Schwartz. The conjugation in \(\widetilde u\) is essential: reflection without conjugation would give \(\widehat u(\xi)\widehat u(-\xi)\), which need not be nonnegative.

If \(\operatorname{supp}u\subset X\), then
\[
\begin{aligned}
\operatorname{supp}v&\subset
\operatorname{supp}u-\operatorname{supp}u\\
&\subset\overline X-\overline X.
\end{aligned}
\tag{3}
\]
For bounded \(X\), the last set is compact and can be used as one fixed support set for every such \(u\).

## A quadratic estimate from a regular inverse

Assume now that
\[
P(\xi)\geq0\qquad(\xi\in\mathbb R^n).
\tag{4}
\]
Define the energy
\[
\begin{aligned}
\mathcal A_P(u)&=(P(D)u,u)\\
&=(2\pi)^{-n}\int P(\xi)|\widehat u(\xi)|^2\,d\xi.
\end{aligned}
\tag{5}
\]
It is a real nonnegative number.

**Theorem 2.1.** For every bounded open set \(X\), there is \(C_{P,X}\) such that, writing \(M_Q=\sup_\xi |Q(\xi)|/S_P(\xi)\),
\[
\begin{aligned}
|(Q(D)u,u)|&\leq C_{P,X}M_Q\mathcal A_P(u),\\
u&\in C_c^\infty(X),\quad Q\prec P.
\end{aligned}
\tag{6}
\]
The constant is independent of \(u\) and \(Q\).

**Proof.** Let \(K=\overline X-\overline X\), and fix a smooth compact cutoff \(\chi\) equal to one near \(K\). Let \(E\) be a regular fundamental solution of \(P(D)\). The compact-data inverse estimate, with \(p=1\) and \(k=1\), gives
\[
\begin{gathered}
\|w\|_{1,S_P}\leq C_{P,K}\|P(D)w\|_{1,1},\\
\operatorname{supp}w\subset K.
\end{gathered}
\tag{7}
\]
Here is why one constant works for the whole support set. Write \(w=E*P(D)w\). For \(\psi\) equal to one near \(\operatorname{supp}\chi-K\), the equality
\(\chi w=\chi((\psi E)*P(D)w)\) holds. The kernel \(\psi E\) belongs to \(B_{\infty,S_P}\); the weighted convolution and cutoff bounds prove (7). None of these choices depends on \(w\).

Apply (7) to the autocorrelation \(v\) in (1). Set
\(M_Q=\sup_\xi |Q(\xi)|/S_P(\xi)<\infty\). Then
\[
\begin{aligned}
\|Q(D)v\|_{1,1}&\leq M_Q\|v\|_{1,S_P}\\
&\leq C_{P,K}M_Q\|P(D)v\|_{1,1}.
\end{aligned}
\tag{8}
\]
The Fourier transform of \(P(D)v\) is \(P|\widehat u|^2\). By (4) it is nonnegative, so
\[
\begin{aligned}
\|P(D)v\|_{1,1}&=(2\pi)^{-n}\int P|\widehat u|^2\\
&=\mathcal A_P(u).
\end{aligned}
\tag{9}
\]
Fourier inversion bounds \(|Q(D)v(0)|\) by \(\|Q(D)v\|_{1,1}\). Combine (2), (8), and (9). This proves (6). \(\square\)

The positivity assumption is used in the equality (9), not in the linear inverse estimate (7). It converts the Fourier \(L^1\) norm into the energy without cancellation.

Since \(S_P\) has a positive global lower bound, \(1\prec P\). Taking \(Q=1\) gives
\[
\|u\|_2^2\leq C'_{P,X}\mathcal A_P(u).
\tag{10}
\]
Thus a nonzero nonnegative symbol has strictly positive energy on every nonzero compactly supported test function. No positive lower bound for \(P(\xi)\) on the whole real frequency space is required. Bounded spatial support supplies the estimate.

## Which derivative norms are controlled?

For a polynomial \(R\), let \(\overline R\) denote coefficientwise conjugation. On real frequencies, \(R\overline R=|R|^2\). If
\[
R\overline R\prec P,
\tag{11}
\]
then (6) and Parseval give
\[
\begin{aligned}
\|R(D)u\|_2^2&=(R(D)u,R(D)u)\\
&=((R\overline R)(D)u,u)\\
&\leq C_{P,X,R}\mathcal A_P(u).
\end{aligned}
\tag{12}
\]
Condition (11) involves the square of the symbol. Merely knowing \(R\prec P\) controls its quadratic pairing in (6); it does not by itself turn that pairing into the squared derivative norm in (12).

For example, consider
\[
P(\xi_1,\xi_2)=\xi_1^2+\xi_2^4.
\]
Its energy is
\[
\mathcal A_P(u)=\|D_1u\|_2^2+\|D_2^2u\|_2^2.
\tag{13}
\]
The symbol \(\xi_2^2\) is weaker than \(P\). Indeed \(|\xi_2|^2\leq1+\xi_2^4\), while \(S_P\) controls both the nonnegative value \(P\) and a nonzero constant derivative. Hence (12), with \(R=\xi_2\), also controls \(\|D_2u\|_2^2\) by (13). Together with (10), the energy controls the function, its first derivative in each coordinate, and its second derivative in the second coordinate. It need not control every second derivative.

The estimates concern functions compactly supported in the open set. Taking a completion of these functions in an energy norm is a further choice of solution space. The present estimate does not prescribe boundary traces for an arbitrary nonelliptic operator.

## Two limits on the estimate

Boundedness of the set matters. In one dimension, let \(P(\xi)=\xi^2\), choose nonzero \(a\in C_c^\infty(\mathbb R)\), and put \(u_R(x)=a(x/R)\). Then
\[
\|u_R\|_2^2=R\|a\|_2^2,
\qquad \mathcal A_P(u_R)=R^{-1}\|a'\|_2^2.
\]
Their ratio tends to infinity. There is no single version of (10) for all compact supports in \(\mathbb R\).

Positivity matters as well. For \(P(\xi_1,\xi_2)=\xi_1\xi_2\), take \(u(x_1,x_2)=a(x_1)b(x_2)\) with nonzero real test functions. Then
\[
(P(D)u,u)
=\left(\int(-ia')a\right)
 \left(\int(-ib')b\right)=0,
\]
because each integral is the integral of a derivative, multiplied by \(-i/2\). Yet \(\|u\|_2>0\), and \(1\prec P\). This rules out (6) with that sign-changing symbol, even on a bounded rectangle.

## Exact constants and further consequences

The following results retain the original symbol, its full derivative norm, and the Fourier factor. Unless stated otherwise, \(n\geq1\). They use the written [regular-kernel construction, Theorem 3.1](../AN02-L004.html#a-smooth-family-with-small-exponential-growth), whose averaging input is proved in [the complete polynomial-averaging proof PA1–PA16](../AN02-L120.html#complete-formal-proof-pa1-pa16). The precise multiplication and convolution bounds are [Theorem 4.1 and Proposition 4.2 of the weighted-spaces lesson](../AN02-L002.html#cutoffs-differential-operators-and-convolution); the equivalence between value bounds and full derivative bounds is [Lemma 1.1 of the strength lesson](../AN02-L005.html#comparing-what-two-equations-control). [The compact-data proof, Theorems 2.1–2.2](../AN02-L005.html#the-exact-gain-for-compact-data), keeps the support and distributional convolution hypotheses explicit. Fourier inversion uses [Theorem 1.1 of the Fourier foundation](../prerequisites/prerequisite-bridges.html#fourier-inversion-on-the-schwartz-space), and the pairing uses its [Theorem 2.1](../prerequisites/prerequisite-bridges.html#plancherel-and-integer-sobolev-weights). Its [integral-triangle proof](../prerequisites/prerequisite-bridges.html#fourier-integral-triangle-proof) supplies the approximation estimate for the surrounding completed-space theory.

### One constant for the support set and coefficient family

Fix \(K=\overline X-\overline X\), choose \(\chi=1\) near \(K\), and choose \(\psi=1\) near \(\operatorname{supp}\chi-K\), with both cutoffs smooth and compactly supported. For \(w\in C_c^\infty\) supported in \(K\), put \(f=P(D)w\). The identity \(E*f=w\) is distributional: differentiation of \(w(x-y)\) satisfies \(D_x=-D_y\), so the complex-linear transpose moves \(P(-D_y)\) to \(P(D)E=\delta_0\). No Hilbert-space conjugation is involved. The compact test factor defines convolution even when the uncut \(E\) is not tempered. Since \(\operatorname{supp}f\subset K\), localization gives
\[
w=\chi((\psi E)*f),\qquad
\|w\|_{1,S_P}\leq
A_{S_P}(\chi)\|\psi E\|_{\infty,S_P}\|f\|_{1,1}.
\tag{PE1}
\]
Here
\[
A_{S_P}(g)=(2\pi)^{-n}
\int M_{S_P}(h)|\widehat g(h)|\,dh.
\]
Thus (7) holds with the explicit finite constant \(A_{S_P}(\chi)\|\psi E\|_{\infty,S_P}\). Neither cutoff nor constant depends on \(w\), \(u\), or \(Q\).

There is also uniformity as the controlling polynomial varies. Fix its maximum degree \(m\), the dimension, and the bounded open set \(X\). [Proposition 1.3 of the weighted-spaces lesson](../AN02-L002.html#weights-that-tolerate-frequency-shifts) gives \(M_{S_P}(h)\leq(1+A|h|)^m\), where \(A\) depends only on \(m,n\), including polynomials whose actual degree drops. Fix one averaging radius \(\rho\) and \(\varepsilon>\rho\). The regular-kernel theorem constructs a family with
\[
\|E_\rho(P)/w_\varepsilon\|_{\infty,S_P}\leq C_0,
\qquad w_\varepsilon(x)=\cosh(\varepsilon|x|),
\]
where \(C_0\) is independent of the coefficients of \(P\). Define
\[
B_m(g)=(2\pi)^{-n}\int(1+A|h|)^m|\widehat g(h)|\,dh.
\]
Multiplication by the compact smooth function \(\psi w_\varepsilon\) gives
\[
\|\psi E_\rho(P)\|_{\infty,S_P}
\leq B_m(\psi w_\varepsilon)C_0.
\]
Consequently one admissible constant in (6), simultaneously for every nonzero nonnegative \(P\) of degree at most \(m\), is
\[
C_{m,n,X}=B_m(\chi)B_m(\psi w_\varepsilon)C_0.
\tag{PE2}
\]
Apply (PE1) to the same autocorrelation and repeat (8)–(9); the factor \(M_Q\) is unchanged. This does not assert a coefficient-independent constant after discarding \(M_Q\). For \(Q=1\), \(M_1\) can diverge as \(P\) approaches zero. If \(P=a>0\) is constant, the weaker polynomials are constants \(Q=b\), and the exact value \(1\) works in (6), since \(M_Q\mathcal A_P(u)=|b|\|u\|_2^2\). If \(X\) is empty every assertion about its test functions is trivial.

### The derivative criterion is necessary as well as sufficient

For a nonempty bounded open \(X\), a nonzero nonnegative \(P\), and a complex polynomial \(R\),
\[
\begin{gathered}
\|R(D)u\|_2^2\leq C\mathcal A_P(u)
\quad\text{for all }u\in C_c^\infty(X)
\text{ and some finite }C\geq0
\\\Longleftrightarrow\quad R\overline R\prec P.
\end{gathered}
\tag{PE3}
\]
Sufficiency is (12), with constant \(C_{m,n,X}M_{R\overline R}\). For necessity, choose a real \(\chi\in C_c^\infty(X)\) equal to one on a ball \(B\) of positive measure. Use \(u_\xi(x)=e^{ix\cdot\xi}\chi(x)\), keeping \(\xi\) arbitrary. On \(B\), \(R(D)u_\xi=e^{ix\cdot\xi}R(\xi)\), hence
\[
|B|\,|R(\xi)|^2\leq\|R(D)u_\xi\|_2^2.
\]
The moments
\[
\mu_\alpha=(2\pi)^{-n}\int\eta^\alpha|\widehat\chi(\eta)|^2\,d\eta
\]
are finite. The exact finite Taylor identity, followed by Cauchy–Schwarz, gives
\[
\begin{aligned}
\mathcal A_P(u_\xi)
&=\sum_{|\alpha|\leq m}\frac{\mu_\alpha}{\alpha!}\partial^\alpha P(\xi),\\
0\leq\mathcal A_P(u_\xi)
&\leq S_P(\xi)
\left(\sum_{|\alpha|\leq m}|\mu_\alpha/\alpha!|^2\right)^{1/2}.
\end{aligned}
\tag{PE4}
\]
Thus the assumed estimate implies
\[
|R(\xi)|^2\leq\frac{C}{|B|}
\left(\sum_{|\alpha|\leq m}|\mu_\alpha/\alpha!|^2\right)^{1/2}S_P(\xi).
\]
The value/derivative equivalence in Lemma 1.1 of the strength lesson, applied to \(R\overline R\), proves necessity. Its zero-polynomial case includes \(R=0\). Necessity uses only one ball and therefore holds on any nonempty open set; sufficiency in (PE3) retains boundedness.

For the original example \(P=\xi_1^2+\xi_2^4\), the full norm, without dropping derivative terms, is
\[
\begin{aligned}
S_P^2={}&(\xi_1^2+\xi_2^4)^2+4\xi_1^2
+16\xi_2^6+144\xi_2^4\\
&+576\xi_2^2+4+576.
\end{aligned}
\tag{PE5}
\]
It is comparable to \(1+\xi_1^2+\xi_2^4\). The value term and constant derivatives prove the lower comparison. For the upper one, \(\xi_1^2\leq1+\xi_1^4\); the powers \(|\xi_2|^2,|\xi_2|^4,|\xi_2|^6\) are bounded on \(|\xi_2|\leq1\) and bounded by \(|\xi_2|^8\) on its complement.

Assign a monomial \(\xi_1^\alpha\xi_2^\beta\) weight \(2\alpha+\beta\). Under \((\xi_1,\xi_2)=(s^2a,sb)\), the full \(S_P\) grows at most like \(s^4\). If a nonzero polynomial has highest weighted degree greater than four, choose a real \((a,b)\) where that highest part is nonzero. Its value divided by \(S_P\) is then unbounded. Conversely, put \(L=\max(1,|\xi_1|^{1/2},|\xi_2|)\). Each monomial of weight at most four has modulus at most \(L^4\leq1+\xi_1^2+\xi_2^4\). Therefore the complete space of weaker polynomials is
\[
\operatorname{span}_{\mathbb C}
\{1,\xi_1,\xi_1^2,\xi_2,\xi_1\xi_2,
\xi_2^2,\xi_1\xi_2^2,\xi_2^3,\xi_2^4\}.
\tag{PE6}
\]
If the highest weighted part of \(R\) is \(R_w\), that of \(R\overline R\) is \(R_w\overline{R_w}\), of weight \(2w\). It cannot vanish identically on real frequencies unless \(R_w=0\). Consequently (PE3) gives the exact space of controlled derivative operators:
\[
R\in\operatorname{span}_{\mathbb C}\{1,\xi_1,\xi_2,\xi_2^2\}.
\tag{PE7}
\]
In particular neither \(D_1^2\) nor \(D_1D_2\) is controlled in this norm on any fixed nonempty bounded open set. This preserves, and makes precise, the distinction following (13).

The modulation in Exercise 3 also has an exact version. For real nonzero compact tests \(a,b\), set \(A_j=\|D_1^j a\|_2^2\), \(B_j=\|D_2^j b\|_2^2\), and \(u_N=e^{iNx_1}ab\). Expansion and integration by parts give
\[
\begin{aligned}
\mathcal A_P(u_N)&=(N^2A_0+A_1)B_0+A_0B_2,\\
\|D_1^2u_N\|_2^2&=(N^4A_0+6N^2A_1+A_2)B_0.
\end{aligned}
\tag{PE8}
\]
Indeed \(D_1^2(e^{iNx_1}a)=e^{iNx_1}(N^2a-2iNa'-a'')\). Its real and imaginary parts have no mixed contribution to the squared modulus; \(\int aa''=-\int|a'|^2\) yields the coefficient six. The analogous first-derivative expansion yields the first identity. The divergence claimed in the exercise follows without suppressing any lower-order term.

### The sharp strip constant

For every open \(X\subset(a,b)\times\mathbb R^{n-1}\), even if the transverse directions are unbounded,
\[
\|u\|_2^2\leq\frac{(b-a)^2}{\pi^2}\|D_1u\|_2^2,
\qquad u\in C_c^\infty(X).
\tag{PE9}
\]
Extend \(u\) by zero; compact containment makes this extension smooth. Put \(w(x_1)=\sin(\pi(x_1-a)/(b-a))\), and for each transverse coordinate put \(g=u/w\). Since \(u\) vanishes near the endpoints and \(w>0\) in the interval, \(g\) vanishes near the endpoints too. Expand
\[
|(wg)'|^2=w^2|g'|^2+(w')^2|g|^2+ww'(|g|^2)'.
\]
Integration by parts has no boundary term. Using \(w''=-\pi^2w/(b-a)^2\) gives the exact identity
\[
\int_a^b|\partial_1u|^2
-\frac{\pi^2}{(b-a)^2}\int_a^b|u|^2
=\int_a^bw^2|\partial_1g|^2\geq0.
\tag{PE10}
\]
Integrate in the transverse coordinates and use \(|D_1u|=|\partial_1u|\). This proves (PE9) for complex as well as real tests.

The constant is sharp for the full strip, though a smaller \(X\) may have a better constant. Cut \(w\) off smoothly in endpoint intervals of length \(\varepsilon\), with cutoff derivative bounded by \(C/\varepsilon\). On those intervals \(w=O(\varepsilon)\) and \(w'\) is bounded. The function error and its first derivative tend to zero in \(L^2\): the derivative error is bounded on sets of length \(O(\varepsilon)\), including the product of the cutoff derivative and \(w\). Thus the compact tests approach \(w\) in \(H^1(a,b)\). Multiply by any fixed nonzero compact smooth transverse function; in dimension one use the unit function on the zero-dimensional transverse space. The norm ratio tends to \((b-a)^2/\pi^2\). No boundary condition for a general nonelliptic operator is being imposed.

### A single constant for every compact support

Fix a nonzero nonnegative polynomial \(P\), a complex polynomial \(Q\), and \(C\geq0\). Then
\[
\begin{gathered}
|(Q(D)u,u)|\leq C\mathcal A_P(u)
\quad\text{for every }u\in C_c^\infty(\mathbb R^n)
\\\Longleftrightarrow\quad
|Q(\xi)|\leq CP(\xi)\quad\text{for every real }\xi.
\end{gathered}
\tag{PE11}
\]
The pointwise bound proves sufficiency by taking the absolute value inside (2). For necessity, choose nonzero \(a\in C_c^\infty\), fix any real \(\xi_0\), and for \(R>0\) put
\[
w_R(x)=R^{-n/2}e^{ix\cdot\xi_0}a(x/R),\qquad
\widehat w_R(\xi)=R^{n/2}\widehat a(R(\xi-\xi_0)).
\]
Substitution \(\eta=R(\xi-\xi_0)\) in (2) gives
\[
(Q(D)w_R,w_R)=(2\pi)^{-n}\int
Q(\xi_0+\eta/R)|\widehat a(\eta)|^2\,d\eta.
\tag{PE12}
\]
The same formula with \(P\) gives its energy. For \(R\geq1\), a fixed polynomial in \(|\eta|\) bounds the symbols; its product with \(|\widehat a|^2\) is integrable. Dominated convergence gives limits \(Q(\xi_0)\|a\|_2^2\) and \(P(\xi_0)\|a\|_2^2\). Passing to the limit in the assumed estimate and dividing by the positive common factor proves the pointwise bound, including zeros of \(P\).

The least common constant is therefore
\[
\sup_{\xi\in\mathbb R^n}\frac{|Q(\xi)|}{P(\xi)},
\tag{PE13}
\]
where the ratio is zero when \(P=Q=0\) and is \(+\infty\) when \(P=0\) but \(Q\neq0\). An infinite supremum means no finite common constant; \(Q=0\) gives zero. With \(Q=1\), a common whole-space \(L^2\) coercivity constant exists exactly when \(\inf P>0\). This is stronger than merely having positive energy on each nonzero test.

Indeed every nonzero real polynomial has a zero set of Lebesgue measure zero. In one dimension it has finitely many roots. Inductively write it as a polynomial in the last coordinate. Except where all coefficient polynomials vanish, each fibre has finitely many roots. The exceptional set is contained in the zero set of one nonzero coefficient polynomial and is null by induction. Fubini on increasing bounded boxes proves the assertion. Since nonnegativity on real frequencies forces the imaginary-part polynomial to vanish identically, the present \(P\) is real and \(P>0\) almost everywhere. If a Schwartz function had zero energy, its transform would vanish almost everywhere; Parseval would force the function to be zero. This proves strict positivity without a common support bound, while (PE11) identifies the separate uniform estimate.

For \(n=0\), the one-point integral has unit mass and all polynomials are constants. With \(P=a>0\), the pairing is \(b|u|^2\), energy is \(a|u|^2\), and the least common constant is \(|b|/a\). The strip and two-variable examples are restricted to their stated dimensions.

*These consequences integrate the complete supplied proofs by GPT-6.1 Sol (OpenAI), Ultra, with current proof-provider connections and exposition by GPT-6 Astra (OpenAI), Ultra. October 2026. CC0-1.0.*


## Exercises with solutions

**Exercise 1 (entry).** Show directly that \(v(0)=\|u\|_2^2\) for the autocorrelation in (1). Verify the factor \((2\pi)^{-n}\) in its Fourier expression.

**Solution.** The convolution formula gives
\(v(0)=\int u(-y)\overline{u(-y)}\,dy=\|u\|_2^2\).
Fourier inversion at zero gives
\(v(0)=(2\pi)^{-n}\int\widehat v=(2\pi)^{-n}\int|\widehat u|^2\), exactly Parseval with the course convention.

**Exercise 2 (intermediate).** Suppose \(X\subset(a,b)\times\mathbb R^{n-1}\). Prove directly that
\(\|u\|_2^2\leq(b-a)^2\|D_1u\|_2^2\) for \(u\in C_c^\infty(X)\). Compare this with (10) for \(P=\xi_1^2\).

**Solution.** Extend \(u\) by zero. For each fixed transverse coordinate,
\(u(x_1,x')=\int_a^{x_1}\partial_1u(s,x')\,ds\).
Cauchy–Schwarz bounds its squared absolute value by
\((b-a)\int_a^b|\partial_1u(s,x')|^2\,ds\).
Integrate in \(x_1\) and \(x'\). Since \(|D_1u|=|\partial_1u|\), the stated estimate follows. It exhibits a concrete dependence on the width of the support region. This direct argument also works for an unbounded strip; the general theorem only needs the simpler bounded-set hypothesis.

**Exercise 3 (intermediate).** For the anisotropic symbol in (13), show that \(D_1^2u\) is not bounded in \(L^2\) by the square root of that energy on a fixed rectangle.

**Solution.** Let \(u_N=e^{iNx_1}a(x_1)b(x_2)\), with fixed nonzero test functions supported in the rectangle. Then
\(\|D_1^2u_N\|_2=N^2\|ab\|_2+O(N)\), by expanding \((D_1+N)^2a\).
The energy is \(N^2\|ab\|_2^2+O(N)+O(1)\), so its square root grows only like \(N\). The proposed estimate fails. Correspondingly, \(\xi_1^4\not\prec P\), as the ratio \(|\xi_1|^4/S_P(\xi_1,0)\) grows like \(|\xi_1|^2\).

**Exercise 4 (advanced).** If \(Q\prec P\) has complex coefficients, does (6) require its quadratic pairing to be real? Give an example and explain the role of the absolute value.

**Solution.** No. Take \(P=\xi^2\) and \(Q=i\), which is weaker. Then
\((Q(D)u,u)=i\|u\|_2^2\), a purely imaginary number. Its absolute value is \(\|u\|_2^2\), bounded by (10). Positivity is required for the controlling symbol \(P\); the weaker symbol can be complex. Removing the absolute value would not give an ordered real inequality in this example.

## References

- [Grubb] Gerd Grubb, *Fourier transformation*, open chapter of the lecture notes for *Distributions and Operators*, Theorem 5.5. [Author's PDF](https://web.math.ku.dk/~grubb/dist5.pdf).
- [Melrose] Richard Melrose, *Differential Analysis*, MIT OpenCourseWare, Fall 2004, Section 9, Lemma 9.2. [Open Fourier chapter](https://ocw.mit.edu/courses/18-155-differential-analysis-fall-2004/fa60b20e070ee676b70cdf8a373e6197_section9.pdf).
