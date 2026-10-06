# Stationary concentration and point jets

*Original edition by GPT-6.1 Sol (OpenAI), Ultra reasoning effort. Repaired and self-checked by GPT-6 Astra (OpenAI), Ultra reasoning effort, October 2026. Original exposition: public domain (CC0); supplied prerequisites retain their stated licences.*

A scalar Gaussian detects a stationary point mass; a correlated planar Gaussian detects a mixed derivative that a product test misses. A cancelled phase requires a larger normalization, while a flat direction leaves concentration along a critical subspace. We measure these effects, prove the scalar and mixed strong limits, then derive every finite transverse-jet expansion for real symmetric quadratics and classify the surviving limits for every even scalar monomial amplitude.

We use \(\widehat f(\xi)=\int e^{-ix\cdot\xi}f(x)dx\), inverse factor \((2\pi)^{-d}\), and complex bilinear distributional pairings. Strong dual convergence is uniform on every bounded test family.

The supplied [Fourier foundation](../prerequisites/U011-free-foundations/schwartz-fourier-foundations-U017.md), F1–F5, proves every Schwartz seminorm estimate, inversion identity, Gaussian mass and transposed differentiation rule used below. The [integration foundation](../prerequisites/U011-free-foundations/banach-foundation-bridges.md), §§15.0–15.1 and 16, proves absolute Fubini, dominated convergence and the full real linear Jacobian. The [scalar foundation](../prerequisites/U011-free-foundations/metric-foundation-bridges.md), §§12–13, and [finite algebra](../prerequisites/U011-free-foundations/stable-prerequisite-bridges.md), §§10.1–10.6, supply the Euclidean, calculus and matrix operations. The arguments here need Schwartz inversion and its weighted estimates.

The exact Gaussian transform, its determinant branch and real symmetric diagonalization are [Point sources and complex Gaussian kernels](point-sources-and-complex-gaussian-kernels.md), Section 2 and the transform part of Theorem 3.1. [Quadratic phases and curved spectra](quadratic-phases-and-curved-spectra.md), Lemma 0.1, calculation G and Solution 10, proves the partial transforms, strong transposes, signed Fresnel identities and every degenerate rank. [Order, positivity and distributional limits](order-positivity-and-limits.md), (T1)–(T2), proves the common-support characterization of bounded compact-test families with its full test topology.

The complete [integral Taylor proof](when-a-kernel-is-smooth.md#taylor-estimates-on-compact-neighborhoods) supplies the finite-order remainders used here, including signed increments, complex-valued functions, directional derivatives and uniform bounds for all required derivatives on compact neighborhoods.

## Uniform test estimates for the strong limits

**Lemma 0.1.** For any polynomial \(P\) on \(\mathbb R^d\),
\(\phi\mapsto\int |P(\xi)\widehat\phi(\xi)|\,d\xi\)
is bounded by finitely many Schwartz seminorms. Every bounded family of compact smooth tests is bounded in Schwartz space. Hence each uniform remainder estimate below proves strong convergence in both tempered and compact-test duals.

**Proof.** Put \(W(\xi)=\prod_{j=1}^d(1+\xi_j^2)\). The Fourier foundation's (F4), applied to \(P\widehat\phi\), gives
\[
 \begin{gathered}
 \int |P(\xi)\widehat\phi(\xi)|\,d\xi\\
 \le\pi^d\sup_\xi W(\xi)|P(\xi)\widehat\phi(\xi)|.
 \end{gathered}
\]
Expand the finite polynomial \(WP\) and bound each monomial separately. F2 bounds every resulting Fourier seminorm by finitely many seminorms of \(\phi\). These bounds are uniform on any bounded Schwartz family.

For a bounded compact-test family, U008, (T1)–(T2), gives a common compact support \(K\) and uniform bounds on all derivatives. The supremum of each monomial \(|x^\alpha|\) on \(K\) is finite, so
\[
 \sup_x|x^\alpha\partial^\beta\phi(x)|
 \le\sup_{x\in K}|x^\alpha|\,
       \sup_{x\in K}|\partial^\beta\phi(x)|.
\]
Thus all Schwartz seminorms are bounded on that family. The strong-dual seminorm is precisely the supremum of the absolute pairing over such a bounded family. A remainder bounded by its fixed seminorm constant times a quantity tending to zero therefore tends strongly to zero in either dual. Restriction from tempered distributions to compact tests is the distributional restriction proved in F5. \(\square\)

## Measure what a stationary limit leaves behind

**S1. A scalar Gaussian sees the mass and the next jet.** Put \(\phi_b(x)=e^{-bx^2}\), where \(b>0\), and let \(t>0\). Absolute Gaussian integration gives

\[
\begin{gathered}
\sqrt t\,\langle\sin(tx^2),\phi_b\rangle
\\ =\sqrt\pi\,\operatorname{Im}(b/t-i)^{-1/2}
\\ =\frac{\sqrt\pi\sin(\tfrac12\arctan(t/b))}
{(1+(b/t)^2)^{1/4}}
\\ \longrightarrow\sqrt{\pi/2}.
\end{gathered}\tag{S1}
\]

The square root is the continuation of the positive root in the right half-plane. Since \(\phi_b(0)=1\), this measures the coefficient of the point mass in Theorem E. Now offset the phase by \(-\pi/4\). The leading mass cancels, but

\[
\begin{gathered}
t^{3/2}\langle\sin(tx^2-\pi/4),\phi_b\rangle
\\ =t\sqrt\pi\,\operatorname{Im}(1+ib/t)^{-1/2}
\\ \longrightarrow-\frac{\sqrt\pi b}{2}.
\end{gathered}\tag{S2}
\]

Indeed \((1+iu)^{-1/2}=1-iu/2+O(u^2)\) near zero. The value in (S2) is \((\sqrt\pi/4)\phi_b''(0)\), because \(\phi_b''(0)=-2b\). A zero at the first normalization therefore need not mean that every normalization gives zero. Solution 9 proves the next limit on every test, including translated phases and negative quadratic coefficients.

**S2. Correlation detects a mixed derivative.** Choose real \(a,b,c\) with \(a,b>0\) and \(D=ab-c^2>0\), and put
\(\phi_{a,b,c}(x,y)=e^{-ax^2-2cxy-by^2}\). Completing the square first in \(x\) leaves a one-dimensional Gaussian in \(y\), whose coefficient is \((D+t^2/4+ict)/a\) with positive real part. Thus

\[
\begin{gathered}
\langle e^{itxy},\phi_{a,b,c}\rangle
\\ =\frac{\pi}{(D+t^2/4+ict)^{1/2}}
\\ =\frac{2\pi}{t}
\left(1+\frac{4ic}{t}+\frac{4D}{t^2}\right)^{-1/2}.
\end{gathered}\tag{S3}
\]

Each square root has positive real part; this branch also follows continuously from \(t=0\). Its first-order expansion yields
\(t^2\langle\sin(txy),\phi_{a,b,c}\rangle\to-4\pi c\).
This is exactly \(2\pi\phi_{a,b,c,xy}(0)\), since that derivative is \(-2c\). For \(c=0\), the sine pairing is identically zero at every \(t\): the product Gaussian is even in each variable. The distribution in Theorem F is nevertheless nonzero. A correlated Gaussian detects the mixed derivative which this particular product test misses. Theorems E and F below establish the limits for arbitrary complex tests, not just Gaussian probes.

## E. A one-dimensional stationary concentration

**Theorem E (scalar stationary mass).** The only real exponent giving a nonzero distributional limit is \(a=1/2\), and

\[
\begin{gathered}
\sqrt n\sin(nx^2)\longrightarrow\sqrt{\pi/2}\,\delta_0
\\ \text{strongly in }\mathcal S'\text{ and }\mathcal D'.
\end{gathered} \tag{E1}
\]

**Proof.** Fourier inversion in the bilinear pairing and (G2) give, for every complex Schwartz test \(\phi\),

\[
\begin{gathered}
\sqrt t\,\langle e^{\pm itx^2},\phi\rangle
=\frac{\sqrt\pi e^{\pm i\pi/4}}{2\pi}
\\ {}\times\int e^{\mp i\xi^2/(4t)}\widehat\phi(-\xi)d\xi.
\end{gathered} \tag{E2}
\]

The integral without its exponential is \(2\pi\phi(0)\). The inequality \(|e^{is}-1|\leq|s|\) for real \(s\) bounds the error from replacing the exponential by one by
\(\sqrt\pi(8\pi t)^{-1}\int\xi^2|\widehat\phi(\xi)|d\xi\).
Take the difference of the two signs and divide by \(2i\); this is valid for complex tests and gives the limit \(\sqrt\pi\sin(\pi/4)\phi(0)=\sqrt{\pi/2}\phi(0)\). The same error bound holds for this half-difference.

Fourier continuity maps bounded Schwartz families to bounded Schwartz families, so their displayed weighted L1 moments are uniformly bounded. The error is uniformly \(O(t^{-1})\) on each such family, proving strong \(\mathcal S'\) convergence. Every bounded \(\mathcal D\) family has one compact support and bounded derivatives of every order, by U008, (T1)–(T2), as used in Lemma 0.1, hence is bounded in \(\mathcal S\). This proves strong \(\mathcal D'\) convergence. For \(a<1/2\), multiply the bounded limiting sequence by \(n^{a-1/2}\) to get zero. For \(a>1/2\), choose a real test with \(\phi(0)=1\); its normalized pairing tends to the positive number \(\sqrt{\pi/2}\), so its unnormalized pairing diverges. A finite nonzero limit is then impossible. \(\square\)

## F. A mixed stationary phase selects a point jet

**Theorem F (the mixed point jet).** In two dimensions the only real exponent giving a nonzero distributional limit is \(a=2\), and

\[
\begin{gathered}
n^2\sin(nxy)\longrightarrow2\pi\partial_x\partial_y\delta_{(0,0)}
\\ \text{strongly in }\mathcal S'\text{ and }\mathcal D'.
\end{gathered} \tag{F1}
\]

**Proof.** The orthogonal coordinates \(s=(x+y)/\sqrt2\), \(r=(x-y)/\sqrt2\) have unit absolute Jacobian and give \(xy=(s^2-r^2)/2\). Their dual coordinates are \((\xi+\eta)/\sqrt2\), \((\xi-\eta)/\sqrt2\). Formula (G2) with opposite phases and coefficient \(t/2\) gives

\[
\widehat{e^{\pm itxy}}(\xi,\eta)
=\frac{2\pi}{t}e^{\mp i\xi\eta/t}. \tag{F2}
\]

The two root phases cancel, and the difference of the two dual squares is \(2\xi\eta\), retaining the displayed exponent. This full distribution identity follows from the same damped Gaussian argument in the linked Gaussian calculation G; the output prefactor is uniformly bounded for fixed \(t>0\) and its exponent has nonpositive real part before taking the limit.

The complex bilinear pairing, taking the half-difference of the signs, now gives

\[
\begin{gathered}
t^2\langle\sin(txy),\phi\rangle=-\frac1{2\pi}
\\ {}\times\int t\sin(\xi\eta/t)
\widehat\phi(-\xi,-\eta)d\xi d\eta.
\end{gathered} \tag{F3}
\]

The derivative form of Fourier inversion is
\(\partial_x\partial_y\phi(0)=-(2\pi)^{-2}\int\xi\eta\widehat\phi(\xi,\eta)d\xi d\eta\).
Replace \(t\sin(\xi\eta/t)\) by \(\xi\eta\) in (F3), and change both integration variables' signs; the result is \(2\pi\partial_x\partial_y\phi(0)\). Two distributional derivatives give a positive sign on the test, so this is exactly the distribution in (F1).

Taylor's integral remainder gives \(|\sin s-s|\leq|s|^3/6\), for every real \(s\). The remaining pairing error is at most

\[
\frac1{12\pi t^2}
\int|\xi\eta|^3|\widehat\phi(\xi,\eta)|d\xi d\eta. \tag{F4}
\]

This is uniformly \(O(t^{-2})\) on bounded Schwartz families. The same bounded-test argument as in E proves both strong conclusions. For \(a<2\) the limit is zero; for \(a>2\) a real compact smooth test with nonzero mixed derivative at zero makes the pairing diverge after scaling. Thus \(a=2\) is the sole nonzero finite limit exponent. \(\square\)

## A flat direction leaves a critical line

**S3. Compare opposite transverse signs with a free coordinate.** In \(\mathbb R^3\), let \(q(x,y,z)=x^2-y^2\) and test it with
\(\phi_{a,b,c}=e^{-ax^2-by^2-cz^2}\), where \(a,b,c>0\). Absolute Fubini gives

\[
\begin{gathered}
\langle e^{itq},\phi_{a,b,c}\rangle
\\ =\frac{\pi^{3/2}}{\sqrt c}
\\ {}\times(a-it)^{-1/2}(b+it)^{-1/2}
\\ =\frac{\pi^{3/2}}{t\sqrt c}
\\ {}\times(1+ia/t)^{-1/2}(1-ib/t)^{-1/2}.
\end{gathered}\tag{S4}
\]

The two Fresnel root phases cancel. Expanding the last two factors gives

\[
\begin{gathered}
t\langle\cos(tq),\phi_{a,b,c}\rangle
\\ \longrightarrow\pi\sqrt{\pi/c},
\\ t^2\langle\sin(tq),\phi_{a,b,c}\rangle
\\ \longrightarrow\frac{\pi(b-a)}2\sqrt{\pi/c}.
\end{gathered}\tag{S5}
\]

Define the critical-line distribution \(D\) by
\(\langle D,\phi\rangle=\int_{\mathbb R}\phi(0,0,z)dz\); equivalently \(D=\delta_{(0,0)}\otimes1_z\). The corresponding full strong limits, proved in Solution 10, are

\[
\begin{gathered}
t\cos(tq)\longrightarrow\pi D,
\\
t^2\sin(tq)\longrightarrow
\frac\pi4(\partial_x^2-\partial_y^2)D.
\end{gathered}\tag{S6}
\]

For the Gaussian, \(D(\phi_{a,b,c})=\sqrt{\pi/c}\) and
\((\partial_x^2-\partial_y^2)D(\phi_{a,b,c})=2(b-a)\sqrt{\pi/c}\), agreeing with (S5). The dependence on \(c\) measures integration along the free coordinate. Both limits are supported on the entire critical line: a small bump near any point of the line detects \(D\), and a test agreeing transversely with \(x^2\), multiplied by a positive bump along the line, detects its displayed jet. The phase has no oscillation in \(z\) to concentrate that direction to a point.

## Exercises

**Exercise 1 (foundation: sign, translation and a phase offset).** For real \(\lambda\ne0\), \(c\) and \(\theta\), determine the strong tempered limit of \(\sqrt n\sin(n\lambda(x-c)^2+\theta)\). Give an error bound and identify the offsets for which this leading limit is zero.

**Exercise 2 (foundation: the even part of a mixed phase).** Prove \(n\cos(nxy)\to2\pi\delta_0\) strongly in both \(\mathcal S'(\mathbb R^2)\) and \(\mathcal D'(\mathbb R^2)\). Give an explicit weighted Fourier error bound. Compare its normalization with that of the sine.

**Exercise 3 (intermediate: a smooth amplitude changes the point jet).** Let \(a\in C_c^\infty(\mathbb R^2)\). Determine the strong limit of \(n^2a(x,y)\sin(nxy)\), expressed as a linear combination of \(\delta_0\), its two first derivatives and its mixed derivative. Prove all coefficient signs.

**Exercise 4 (advanced: the next scalar stationary term).** Put \(C=\sqrt{\pi/2}\). Prove
\[
n\bigl(\sqrt n\sin(nx^2)-C\delta_0\bigr)
\longrightarrow\frac C4\delta_0''
\]
strongly in \(\mathcal S'\) and \(\mathcal D'\). Give a remainder bound after subtracting the first two terms.

**Exercise 5 (advanced: the next mixed stationary term).** Prove
\[
n^2\bigl(n^2\sin(nxy)-2\pi\partial_x\partial_y\delta_0\bigr)
\longrightarrow-\frac\pi3\partial_x^3\partial_y^3\delta_0
\]
in both strong dual topologies. Retain the sixth-order point-jet sign and an explicit remainder bound.

**Exercise 6 (intermediate: slanted coordinate directions).** For \(c\in\mathbb R^2\) and independent row vectors \(a,b\), put \(M=(a;b)\). Determine the strong limit of
\(n^2\sin(n[a\cdot(x-c)][b\cdot(x-c)])\).
Express the answer using the columns of \(M^{-1}\). Compute it explicitly when \(c=0\), \(a=(1,2)\), \(b=(3,1)\).

**Exercise 7 (advanced: a vanishing amplitude changes the exponent).** Find the only real exponent \(q\) for which
\(n^q(x^2+y^2)\sin(nxy)\)
has a finite nonzero limit in \(\mathcal D'(\mathbb R^2)\). Compute that limit, prove convergence also strongly in \(\mathcal S'\), and prove both the zero and the divergent ranges of \(q\).

**Exercise 8 (advanced: sine and cosine of a positive planar quadratic).** Determine the strong limits of \(n\sin(n(x^2+y^2))\) and \(n^2\cos(n(x^2+y^2))\). Identify the sole exponent for a finite nonzero limit in each case. Explain the cancellation that distinguishes the two normalizations.

**Exercise 9 (advanced: a cancelled scalar mass).** Let \(\lambda\ne0\), \(c,\theta\in\mathbb R\), and assume
\(\theta+\pi\operatorname{sgn}(\lambda)/4\in\pi\mathbb Z\).
Find the sole real exponent \(q\) for which
\(n^q\sin(n\lambda(x-c)^2+\theta)\) has a finite nonzero distributional limit. Compute its coefficient and give an explicit error bound proving both strong dual limits.

**Exercise 10 (advanced: rank, signature and all transverse jets).** Let \(Q\) be a real symmetric \(n\times n\) matrix, \(q(x)=x^TQx\), \(K=\ker Q\), \(E=K^\perp\), and \(r=\dim E\). For \(r>0\), define
\(d_E=|\det Q_E|\), \(\sigma=\operatorname{sgn}Q_E\),
\(c_Q=\pi^{r/2}/\sqrt{d_E}\), and
\(L_Q=\sum_{j,k}(Q_E^{-1})_{jk}\partial_{y_j}\partial_{y_k}\) in orthonormal coordinates \(y\) on \(E\). Define \(D_K\) by
\(D_K(\phi)=\int_K\phi(0,z)dz\), using Euclidean measure. Derive every finite Taylor expansion of \(t^{r/2}\sin(tq+\theta)\) and its cosine analogue in powers of \(t^{-1}\), with all coefficients and a strong remainder estimate. Classify the sole exponent for a finite nonzero limit in each case. Include rank zero and explain the flat-coordinate factors.

**Exercise 11 (advanced: every even monomial amplitude).** For an integer \(m\geq0\) and \(\theta\in\mathbb R\), classify all real \(q\) for which
\(n^q x^{2m}\sin(nx^2+\theta)\) has a finite nonzero limit. Compute the exact surviving coefficient, including the case when the first available coefficient cancels. Prove convergence strongly in both test spaces and rule out every smaller and larger exponent.

## Solutions

**Solution 1.** Use the half-difference of the signed chirps multiplied by \(e^{i\theta}\) and \(e^{-i\theta}\); this identity is valid on complex tests. Translation gives the test \(\psi(s)=\phi(c+s)\). The signed Fresnel formula with parameter \(n|\lambda|\) gives
\[
\begin{gathered}
\sqrt n\sin(n\lambda(x-c)^2+\theta)
\\ \longrightarrow\sqrt{\pi/|\lambda|}
\sin\!\left(\theta+\frac\pi4\operatorname{sgn}\lambda\right)\delta_c.
\end{gathered}
\]
After removing its limiting coefficient, the pairing error is at most
\[
\frac{\sqrt\pi}{8\pi n|\lambda|^{3/2}}
\int\xi^2|\widehat\psi(\xi)|d\xi.
\]
The shift multiplies \(\widehat\phi\) by a unit phase, so it does not change this weighted absolute moment. This estimate proves strong convergence on bounded Schwartz families, and hence on bounded compact-test families. The leading coefficient vanishes precisely when
\(\theta+\pi\operatorname{sgn}\lambda/4\in\pi\mathbb Z\).
Only this normalization has been computed here. When that coefficient vanishes, a later stationary term can survive with a larger power; a uniqueness statement for the exponent cannot be inferred from this leading zero.

**Solution 2.** The half-sum of the two signed mixed transforms gives, for every complex Schwartz test,
\[
\begin{gathered}
n\langle\cos(nxy),\phi\rangle
\\ =\frac1{2\pi}\int\cos(\xi\eta/n)
\widehat\phi(-\xi,-\eta)d\xi d\eta.
\end{gathered}
\]
Replacing the cosine by one gives \(2\pi\phi(0)\). Since \(|\cos s-1|\leq s^2/2\), the error is bounded by
\[
\frac1{4\pi n^2}
\int|\xi\eta|^2|\widehat\phi(\xi,\eta)|d\xi d\eta.
\]
This proves both strong limits by the bounded-test argument. The even part retains the leading point mass and needs \(n\); the odd part cancels it, needs \(n^2\), and selects the mixed derivative rather than the mass.

**Solution 3.** Multiplication by a fixed compact smooth function is continuous on Schwartz space by the full product rule and is also continuous on compact-test space. It maps bounded families to bounded families, so it preserves the strong convergence in Theorem F. The limit is \(2\pi a\partial_x\partial_y\delta_0\). For a test \(\phi\), its pairing is
\(2\pi\partial_x\partial_y(a\phi)(0)\). Expanding that derivative yields
\[
2\pi\left[\begin{gathered}
a(0)\partial_x\partial_y\delta_0-a_y(0)\partial_x\delta_0
\\ {}-a_x(0)\partial_y\delta_0+a_{xy}(0)\delta_0
\end{gathered}\right].
\]
Each first derivative of a delta acts with a minus sign, whereas the mixed derivative acts with a plus sign. This accounts for all four coefficients, including the exchange of \(a_x\) and \(a_y\) in front of the remaining test derivative.

**Solution 4.** In the signed scalar pairing formula use
\(e^{\mp is}=1\mp is+R_\pm(s)\), with \(|R_\pm(s)|\leq s^2/2\), and \(s=\xi^2/(4n)\). Fourier inversion gives \(\int\widehat\phi(-\xi)d\xi=2\pi\phi(0)\) and \(\int\xi^2\widehat\phi(-\xi)d\xi=-2\pi\phi''(0)\). Therefore
\[
\begin{gathered}
\sqrt n\langle e^{\pm inx^2},\phi\rangle
\\ =\sqrt\pi e^{\pm i\pi/4}
\left(\phi(0)\pm\frac{i}{4n}\phi''(0)\right)
\\ {}+\mathcal R_{\pm,n}(\phi),
\end{gathered}
\]
where
\[
|\mathcal R_{\pm,n}(\phi)|
\leq\frac{\sqrt\pi}{64\pi n^2}
\int\xi^4|\widehat\phi(\xi)|d\xi.
\]
Taking the half-difference gives the constant \(C\) at the point and \(C/(4n)\) at its second derivative. The same remainder bound holds for that half-difference. After multiplication by \(n\), the remainder is uniformly \(O(n^{-1})\) on bounded Schwartz families, proving the limit. Two distributional derivatives give \(\delta''(\phi)=\phi''(0)\), so the positive sign remains. The compact-test strong result follows as before.

**Solution 5.** In Theorem F's exact pairing formula put \(s=\xi\eta/n\). Taylor's integral remainder gives
\(\sin s=s-s^3/6+R(s)\), with \(|R(s)|\leq|s|^5/120\). Thus
\[
\begin{gathered}
n^2\langle\sin(nxy),\phi\rangle=2\pi\phi_{xy}(0)
\\ {}+\frac1{12\pi n^2}
\int(\xi\eta)^3\widehat\phi(-\xi,-\eta)d\xi d\eta
\\ {}+\mathcal R_n(\phi).
\end{gathered}
\]
Since \(i^6=-1\), derivative inversion gives
\(\phi_{xxxyyy}(0)=-(2\pi)^{-2}\int(\xi\eta)^3\widehat\phi(\xi,\eta)d\xi d\eta\).
Changing both integration signs leaves this degree-six monomial unchanged. Its coefficient is consequently \(-\pi/(3n^2)\). After multiplying the remaining error by \(n^2\), its bound is
\[
|n^2\mathcal R_n(\phi)|
\leq\frac1{240\pi n^2}
\int|\xi\eta|^5|\widehat\phi(\xi,\eta)|d\xi d\eta.
\]
All weighted moments are uniform on bounded Schwartz families, giving the strong assertion and its compact-test consequence. The distribution has six derivatives, so it acts positively on \(\phi_{xxxyyy}(0)\); the negative coefficient comes from Fourier inversion and the sine expansion, not from an odd number of distributional derivatives.

**Solution 6.** Let \(v=M^{-1}e_1\), \(w=M^{-1}e_2\). The change of variables \((s,r)=M(x-c)\) has integration factor \(|\det M|^{-1}\), and the new test is \(\psi(s,r)=\phi(c+sv+rw)\). Theorem F therefore yields
\[
\frac{2\pi}{|\det M|}(v\cdot\nabla)(w\cdot\nabla)\delta_c.
\]
Indeed \(\psi_{sr}(0)=(v\cdot\nabla)(w\cdot\nabla)\phi(c)\), and two derivatives give a positive distributional sign. A fixed invertible affine change maps bounded Schwartz families to bounded Schwartz families, by the chain rule and comparable polynomial weights, and does the same for bounded compact-test families. Hence convergence is strong in both spaces. In the specified example,
\[
\begin{gathered}
\det M=-5,
\\ v=(-1/5,3/5),\quad w=(2/5,-1/5),
\end{gathered}
\]
so the answer is
\[
\frac{2\pi}{125}
(-2\partial_x^2+7\partial_x\partial_y-3\partial_y^2)\delta_0.
\]
The absolute determinant supplies the positive mass factor even though the coordinate orientation reverses.

**Solution 7.** Polynomial multiplication is continuous on Schwartz tests and on compact tests and maps bounded families to bounded families. By Solution 3's product calculation, or direct differentiation,
\((x^2+y^2)\partial_x\partial_y\delta_0=0\).
Multiplying the fully subtracted expansion in Solution 5 by this polynomial therefore gives
\[
\begin{gathered}
n^4(x^2+y^2)\sin(nxy)
\\ \longrightarrow-\frac\pi3(x^2+y^2)\partial_x^3\partial_y^3\delta_0
\\ =-2\pi(\partial_x\partial_y^3+\partial_x^3\partial_y)\delta_0.
\end{gathered}
\]
For the last identity, \(x^2\partial_x^3\delta_0=6\partial_x\delta_0\), proved by differentiating \(x^2\phi\) three times at zero and retaining the negative sign on both odd derivative pairings; the analogous \(y\) calculation gives the other term. The obtained fourth-order distribution is nonzero: a compact smooth test agreeing with \(xy^3\) near zero has pairing \(-12\pi\). The normalized sequence is strongly convergent, so multiplying it by \(n^{q-4}\) gives zero for \(q<4\), uniformly on each bounded family. For \(q>4\), its pairing on that fixed real test diverges in magnitude because its normalized pairing tends to \(-12\pi\ne0\). Thus only \(q=4\) gives a finite nonzero limit. The higher exponent is caused by the amplitude annihilating the first point jet.

**Solution 8.** The product of two positive signed scalar Fresnel identities gives
\(\mathcal F(e^{\pm in(x^2+y^2)})
 =(\pi/n)e^{\pm i\pi/2}e^{\mp i|\xi|^2/(4n)}\).
Inversion and the first-order exponential expansion give
\[
\begin{gathered}
n\langle e^{\pm in(x^2+y^2)},\phi\rangle
\\ =\pm i\pi\phi(0)-\frac\pi{4n}\Delta\phi(0)
\\ {}+\mathcal R_{\pm,n}(\phi),
\end{gathered}
\]
where
\[
|\mathcal R_{\pm,n}(\phi)|
\leq\frac1{128\pi n^2}
\int|\xi|^4|\widehat\phi(\xi)|d\xi.
\]
Here the inversion moment of \(|\xi|^2\) is \(-(2\pi)^2\Delta\phi(0)\). The half-difference divided by \(i\) retains \(\pi\phi(0)\), whereas the half-sum cancels the point mass and retains \(-\pi\Delta\phi(0)/(4n)\). Consequently
\[
\begin{gathered}
n\sin(n(x^2+y^2))\longrightarrow\pi\delta_0,
\\ n^2\cos(n(x^2+y^2))\longrightarrow-\frac\pi4\Delta\delta_0.
\end{gathered}
\]
The first error is uniformly \(O(n^{-2})\) and the second uniformly \(O(n^{-1})\) on bounded Schwartz families; the strong compact-test results follow too. Both limiting distributions are nonzero. Multiplying each normalized sequence by a smaller power gives zero; multiplying by a larger power produces divergence on a real compact test with respectively nonzero value or nonzero Laplacian at zero. Hence the sine's sole exponent is one and the cosine's sole exponent is two. The root phases \(\pm i\) explain why the leading mass survives for sine and cancels for cosine.

**Solution 9.** Put \(\psi=\theta+\pi\operatorname{sgn}(\lambda)/4\), \(c_\lambda=\sqrt{\pi/|\lambda|}\), and \(\varphi(s)=\phi(c+s)\). Use the signed version of (E2) with quadratic coefficient \(\lambda\), and expand its dual exponential through first order. The inversion moment is
\(\int\xi^2\widehat\varphi(-\xi)d\xi=-2\pi\varphi''(0)\).
Consequently the half-difference of the signed phases gives, on every complex Schwartz test,

\[
\begin{gathered}
\sqrt t\,\sin(t\lambda(x-c)^2+\theta)
\\ =c_\lambda\left(\begin{gathered}
\sin\psi\,\delta_c
\\ {}+\frac{\cos\psi}{4\lambda t}\delta_c''
\end{gathered}\right)+R_t,
\\ |R_t(\phi)|
\\ \leq\frac{c_\lambda}{64\pi\lambda^2t^2}
\int\xi^4|\widehat\varphi(\xi)|d\xi.
\end{gathered}\tag{S7}
\]

Here \(|e^{iu}-1-iu|\leq u^2/2\) for real \(u\) gives the stated constant. The same bound holds for the half-difference by the triangle inequality. This procedure does not take the imaginary part of a complex-test pairing. Since \(\sin\psi=0\), multiplying (S7) by \(t\) proves

\[
\begin{gathered}
t^{3/2}\sin(t\lambda(x-c)^2+\theta)
\\
\longrightarrow
\frac{\sqrt{\pi/|\lambda|}\cos\psi}{4\lambda}
\delta_c''.
\end{gathered}\tag{S8}
\]

Its error bound is the last bound in (S7) multiplied by \(t\). Translation changes the Fourier transform only by a unit phase, and every bounded Schwartz family has a uniform fourth weighted Fourier moment. Thus convergence is strong in \(\mathcal S'\), and the common-support bounded-test lemma gives strong \(\mathcal D'\) convergence. The coefficient is nonzero because \(\cos\psi=\pm1\) and \(\lambda\ne0\). A real compact smooth test agreeing with \((x-c)^2\) near \(c\) has second derivative two there. On it the normalized pairing has a nonzero limit. Multiplication by \(n^{q-3/2}\) gives zero strongly if \(q<3/2\), and divergence on that fixed test if \(q>3/2\). Therefore \(q=3/2\) is the sole finite nonzero exponent. For \(\lambda=1,c=0,\theta=-\pi/4\), (S8) gives \(\sqrt\pi\,\delta_0''/4\), exactly the Gaussian measurement in (S2).

**Solution 10.** First suppose \(r>0\). Orthogonal coordinates write \(x=(y,z)\in E\oplus K\), with \(q(x)=y^TQ_Ey\) and absolute Jacobian one. For a Schwartz test put
\(\varphi(y)=\int_K\phi(y,z)dz\). This marginal is Schwartz and depends continuously on \(\phi\). To verify that assertion, choose \(\ell>\dim K\). Differentiation under the integral is justified by the integrable weight \((1+|z|)^{-\ell}\), and

\[
\begin{gathered}
\sup_y(1+|y|)^N|\partial_y^\alpha\varphi(y)|
\\ \leq C_{K,\ell}\sup_{y,z}\left[\begin{gathered}
(1+|y|+|z|)^{N+\ell}
\\ {}\cdot|\partial_y^\alpha\phi(y,z)|
\end{gathered}\right],
\\ C_{K,\ell}=\int_K(1+|z|)^{-\ell}dz<\infty.
\end{gathered}\tag{S9}
\]

The finiteness of \(C_{K,\ell}\) follows directly from coordinate-box volumes. If \(k=\dim K>0\), the unit ball lies in a finite cube. On each shell \(2^j\le|z|<2^{j+1}\), the weight is at most \(2^{-j\ell}\), while its volume is at most \(2^{k(j+2)}\). Summing the geometric bound \(2^{2k}\sum_{j\ge0}2^{j(k-\ell)}\) is finite because \(\ell>k\). These are Schwartz seminorm bounds after the fixed orthogonal change. For zero-dimensional \(K\), the integral is evaluation in the absent variable and \(C_{K,\ell}=1\). In particular this map takes bounded families to bounded families. Moreover
\(D_K(\phi)=\varphi(0)\) and
\((L_Q^kD_K)(\phi)=(L_Q^k\varphi)(0)\), because there are \(2k\) distributional derivatives.

The full arbitrary-rank Fresnel proof in Solution 10 of *Quadratic phases and curved spectra*, scaled by \(t\), gives the exact signed pairing

\[
\begin{gathered}
t^{r/2}\langle e^{\pm itq},\phi\rangle
\\ =\frac{c_Qe^{\pm i\pi\sigma/4}}{(2\pi)^r}
\\ {}\times\int_E\left[\begin{gathered}
e^{\mp iA(\xi)/(4t)}
\\ {}\cdot\widehat\varphi(-\xi)
\end{gathered}\right]d\xi,
\\ A(\xi)=\xi^TQ_E^{-1}\xi.
\end{gathered}\tag{S10}
\]

This is a full distributional identity, not a restriction of a pointwise formula. One may first integrate the Schwartz test in the flat variables as in (S9), then apply the nondegenerate Fresnel identity on \(E\). Equivalently the full transformed chirp contains \((2\pi)^{n-r}\delta_0(\xi_K)\); the inverse factor \((2\pi)^{-n}\) leaves precisely \((2\pi)^{-r}\). Thus no extra \(2\pi\) factor belongs to the Euclidean critical-subspace action.

For every integer \(M\geq0\), Taylor's integral remainder on the real axis gives
\(|e^{iu}-\sum_{k=0}^M(iu)^k/k!|\leq|u|^{M+1}/(M+1)!\).
Derivative inversion gives

\[
\begin{gathered}
\frac1{(2\pi)^r}\int_E\left[\begin{gathered}
A(\xi)^k
\\ {}\cdot\widehat\varphi(-\xi)
\end{gathered}\right]d\xi
\\ =(-1)^k(L_Q^k\varphi)(0).
\end{gathered}\tag{S11}
\]

The sign change of the integration variable leaves \(A^k\) unchanged. Multiplying its moment by \((\mp i)^k\) therefore gives \((\pm i)^kL_Q^k\). Take the half-difference of (S10) multiplied by \(e^{i\theta}\) and \(e^{-i\theta}\). Put \(\psi=\theta+\pi\sigma/4\). The result is the finite distributional expansion

\[
\begin{gathered}
t^{r/2}\sin(tq+\theta)
\\ =c_Q\sum_{k=0}^M\left[\begin{gathered}
\frac{\sin(\psi+k\pi/2)}{4^kk!t^k}
\\ {}\cdot L_Q^kD_K
\end{gathered}\right]
\\ {}+R_{M,t},
\\ |R_{M,t}(\phi)|\leq\frac{c_Q}{(2\pi)^r}
\\ {}\times\frac1{4^{M+1}(M+1)!t^{M+1}}
\\ {}\times\int_E\left[\begin{gathered}
|A(\xi)|^{M+1}
\\ {}\cdot|\widehat\varphi(\xi)|
\end{gathered}\right]d\xi.
\end{gathered}\tag{S12}
\]

The half-sum gives exactly the same expansion and bound for the cosine, with each \(\sin(\psi+k\pi/2)\) replaced by \(\cos(\psi+k\pi/2)\). All formulas use bilinear pairings and therefore hold also for complex tests. Each fixed \(M\) has a strong \(O(t^{-M-1})\) remainder: (S9), Fourier continuity, and
\(|A(\xi)|\leq\|Q_E^{-1}\||\xi|^2\) bound the weighted integral uniformly on any bounded Schwartz family. Bounded compact-test families are also bounded Schwartz families. These assertions concern every finite expansion; they do not assert convergence of an infinite derivative series.

For the sine, if \(\sin\psi\ne0\), the sole exponent is \(r/2\), with limit \(c_Q\sin\psi D_K\). If \(\sin\psi=0\), the sole exponent is \(r/2+1\), with limit \(c_Q\cos\psi L_QD_K/4\). For the cosine, if \(\cos\psi\ne0\), the sole exponent is \(r/2\), with limit \(c_Q\cos\psi D_K\). If \(\cos\psi=0\), the sole exponent is \(r/2+1\), with limit \(-c_Q\sin\psi L_QD_K/4\).

To verify both the word "sole" and the nonzero limits, take compact smooth tests in these orthogonal coordinates. A transverse bump equal to one at zero, times a flat bump of integral one, detects \(D_K\). To detect \(L_QD_K\), choose an eigenvector coordinate \(y_j\) of nonzero eigenvalue \(\lambda_j\), take a transverse test equal to \(y_j^2\) near zero, and use the same flat bump. Its value is \(2/\lambda_j\ne0\). If \(K\) has dimension zero, omit the flat bump. The applicable normalized sequence is strongly convergent and its pairing on the indicated test tends to a nonzero real number. A smaller power gives zero uniformly on bounded families; a larger power diverges on that fixed test. This rules out every other exponent.

If \(r=0\), then \(Q=0\) and there is no oscillation. The sine and cosine are the constant functions \(\sin\theta\) and \(\cos\theta\). For a nonzero selected constant the sole exponent is zero, with that constant-function limit; a negative exponent gives zero and a positive exponent diverges on a test of nonzero integral. If the selected constant vanishes, the whole sequence is identically zero and no exponent gives a nonzero limit. This agrees with \(D_K=1\), \(c_Q=1\), \(\sigma=0\), and the absent transverse operator. Full rank instead has \(K=\{0\}\) and \(D_K=\delta_0\). For \(Q=\operatorname{diag}(1,-1,0)\), \(r=2,\sigma=0,c_Q=\pi\) and \(L_Q=\partial_x^2-\partial_y^2\), giving exactly both strong limits in (S6).

**Solution 11.** Polynomial multiplication takes bounded Schwartz families to bounded Schwartz families by the product rule and polynomial-weight bounds. It has the same property for bounded compact-test families, retaining their common support. For all integers \(k,m\geq0\), direct differentiation at zero gives

\[
\begin{gathered}
x^{2m}\delta_0^{(2k)}=0\quad(k<m),
\\ x^{2m}\delta_0^{(2k)}
\\ =\frac{(2k)!}{(2k-2m)!}\delta_0^{(2k-2m)}
\\ (k\geq m).
\end{gathered}\tag{S13}
\]

Indeed only the term differentiating \(x^{2m}\) exactly \(2m\) times survives in the Leibniz formula for \((x^{2m}\phi)^{(2k)}(0)\). All derivative orders here are even, so no extra distributional sign is introduced.

Apply (S12) in one dimension, with \(Q=1\), \(c_Q=\sqrt\pi\), \(L_Q=\partial_x^2\), and \(D_K=\delta_0\), and multiply it by \(x^{2m}\). All terms of index below \(m\) vanish by (S13). Define

\[
\begin{gathered}
\psi_m=\theta+\pi/4+m\pi/2,
\\ A_m=\frac{\sqrt\pi(2m)!}{4^mm!},
\\ B_m=\frac{\sqrt\pi(2m+2)!}{2\,4^{m+1}(m+1)!}.
\end{gathered}\tag{S14}
\]

If \(\sin\psi_m\ne0\), take \(M=m\) in that expansion and multiply by \(t^m\). Its sole exponent and limit are

\[
\begin{gathered}
q=m+\tfrac12,
\\ t^{m+1/2}x^{2m}\sin(tx^2+\theta)
\\ \longrightarrow A_m\sin\psi_m\,\delta_0.
\end{gathered}\tag{S15}
\]

If \(\sin\psi_m=0\), the term of index \(m\) cancels and the next sine coefficient is \(\cos\psi_m=\pm1\). Take \(M=m+1\) and multiply by \(t^{m+1}\). Then

\[
\begin{gathered}
q=m+\tfrac32,
\\ t^{m+3/2}x^{2m}\sin(tx^2+\theta)
\\ \longrightarrow B_m\cos\psi_m\,\delta_0''.
\end{gathered}\tag{S16}
\]

For completeness the remainders after these respective normalizations satisfy

\[
\begin{gathered}
\left|t^MR_{M,t}(x^{2m}\phi)\right|
\\ \leq\frac{\sqrt\pi}{2\pi\,4^{M+1}(M+1)!t}
\\ {}\times\int |\xi|^{2M+2}
\left|\widehat{x^{2m}\phi}(\xi)\right|d\xi,
\\ M=m\ \text{or}\ M=m+1.
\end{gathered}\tag{S17}
\]

Polynomial multiplication and Fourier continuity make the weighted moments uniform on bounded Schwartz families. This proves both strong limits, and the common-support lemma proves their strong compact-test versions. In the first case a compact test of value one at zero detects the nonzero coefficient; in the second a compact test agreeing with \(x^2\) near zero detects it. Multiplying each convergent normalized sequence by a smaller power gives zero strongly, while a larger power diverges on the indicated test. These are therefore the only finite nonzero exponents. For example, \(m=1,\theta=0\) gives \(t^{3/2}x^2\sin(tx^2)\to\sqrt{\pi/2}\,\delta_0/2\), whereas \(m=2,\theta=0\) gives \(t^{5/2}x^4\sin(tx^2)\to-3\sqrt{\pi/2}\,\delta_0/4\). The amplitude removes earlier jets, and the phase determines whether its first surviving coefficient also cancels.

## References

- The supplied [Fourier foundation](../prerequisites/U011-free-foundations/schwartz-fourier-foundations-U017.md), F1–F5, and [integration foundation](../prerequisites/U011-free-foundations/banach-foundation-bridges.md), §§15.0–15.1 and 16: exact Schwartz operations, inversion, absolute integration and real Jacobians.
- [Order, positivity and distributional limits](order-positivity-and-limits.md), (T1)–(T2): bounded compact-test families. [Point sources and complex Gaussian kernels](point-sources-and-complex-gaussian-kernels.md), Section 2 and Theorem 3.1: diagonalization and complex Gaussian transforms. [Quadratic phases and curved spectra](quadratic-phases-and-curved-spectra.md), Lemma 0.1, calculation G and Solution 10: signed transforms and all degenerate ranks.
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators I: Distribution Theory and Fourier Analysis*, reprint of the second edition (1990), Exercises 7.6.5 and 7.6.6, pp. 392–393, and answers, p. 416. This lesson supplies independent full proofs and original graded problems, including uniform remainders on complex test families.
- Jordan Bell, [*Stationary phase, Laplace’s method, and the Fourier transform for Gaussian integrals*](https://jordanbell.info/LaTeX/mathematics/stationaryphase/), July 28, 2015, §3, Theorem 2 and its complete provided proof: positive invertible Gaussian diagonalization with the same negative Fourier sign. The scalar Gaussian formula is quoted there; the stationary-phase result in §2 is also quoted. The signed, arbitrary-rank identities and strong finite expansions used here are proved in the linked lesson and above.
