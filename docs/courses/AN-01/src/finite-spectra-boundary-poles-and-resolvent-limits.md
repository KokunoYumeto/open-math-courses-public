# Finite spectra, boundary poles and resolvent limits

*Reconstructed and self-checked by GPT-6 Astra (OpenAI), Ultra reasoning effort, October 2026. Earlier edition: GPT-6.1 Sol (OpenAI), Ultra reasoning effort. Original exposition: CC0. Supplied foundations retain their stated licences.*

An oriented interval of frequencies gives both a removable quotient and its exact square norm. At a real pole, the limiting side supplies additional point masses. We calculate these complete distributions and prove uniform estimates on bounded Schwartz families, then determine which fundamental solution a small imaginary term selects.

Pairings are complex bilinear. Write \(Ff(\xi)=\int e^{-ix\xi}f(x)dx\), \(G=(2\pi)^{-1}RF\), and \(R\theta(x)=\theta(-x)\). The [Fourier foundation](../prerequisites/U011-free-foundations/schwartz-fourier-foundations-U017.md), F1–F5, proves inversion and every seminorm and transpose identity. [U046](spectral-gaps-and-explicit-fourier-distributions.md), Proposition 1.1, Section 3 and Lemma 5.1, supplies the complete plane-wave and sign transforms, principal-value convention and Parseval norm limit.

The [scalar foundation](../prerequisites/U011-free-foundations/metric-foundation-bridges.md), Sections 12.4–12.9, 13.1–13.5 and 13.7–13.10, and the [integration foundation](../prerequisites/U011-free-foundations/banach-foundation-bridges.md), Sections 15.0–15.4 and 16.1–16.2, supply calculus, compactness, smooth cutoffs, absolute substitution, Fubini, convergence and \(L^2\) completeness. Every additional pole estimate and classification argument appears below.

Put \(P_N(\theta)=\max_{j\le N}\sup_x\langle x\rangle^N|\theta^{(j)}(x)|\), where \(\langle x\rangle=(1+x^2)^{1/2}\). A bounded Schwartz family has all these seminorms uniformly bounded. Strong convergence in \(\mathcal S'\) means uniform convergence of pairings on every such family. If \(B\) is bounded, the Fourier seminorm estimates make \(FB\) and \(GB\) bounded. Therefore transposition proves strong continuity directly:
\(\sup_{\theta\in B}|Fv(\theta)|=\sup_{\eta\in FB}|v(\eta)|\), and likewise for \(G\).

## A finite frequency profile determines the norm

**Theorem 1.1 (a finite interval spectrum and its norm).** For real \(t\), let
\[
f_t(x)=\frac{\cos x-e^{-itx}}x\quad(x\ne0),\qquad f_t(0)=it.
\]
For real \(b,a\), define the oriented indicator \(J_{b,a}\) as \(1_{(b,a)}\) when \(b<a\), as \(-1_{(a,b)}\) when \(a<b\), and as zero when \(a=b\). Then
\[
\begin{gathered}
Ff_t=i\pi(J_{-t,1}+J_{-t,-1}),\\
\int_{\mathbb R}|f_t(x)|^2dx
=\pi\bigl[1+2(|t|-1)_+\bigr].
\end{gathered}
\tag{1.1}
\]

**Proof.** FTC applied to the frequency variable gives
\[
f_t(x)=\frac i2\int_{-t}^1e^{irx}dr
       +\frac i2\int_{-t}^{-1}e^{irx}dr.
\tag{1.2}
\]
The integrals are oriented. At zero their sum is \(it\). Every physical derivative can be taken under these finite integrals, because powers of \(r\) are bounded on the fixed intervals; this proves a smooth extension. Pairing (1.2) with \(F\theta\) is absolutely integrable, bounded by the total interval length times \(\|F\theta\|_1/2\). Fubini and U046's \(F(e^{irx})=2\pi\delta_r\) prove the whole Fourier distribution in (1.1).

The finite integrals bound \(f_t\) near zero, and the quotient has modulus at most \(2/|x|\) for \(x\ne0\). Thus \(f_t\in L^2\). Its computed transform is bounded and compactly supported, hence also in \(L^2\). The exact smooth-function norm passage in U046, Lemma 5.1, applies and gives
\[
\|f_t\|_2^2=\frac\pi2
 \int|J_{-t,1}+J_{-t,-1}|^2d\xi.
\tag{1.3}
\]
For \(-1\le t\le1\), the indicator sum is \(-1\) on \((-1,-t)\) and \(1\) on \((-t,1)\); its square integral is \(2\). At either endpoint one interval is empty. For \(t>1\), the sum is \(2\) on \((-t,-1)\) and \(1\) on \((-1,1)\), giving \(4(t-1)+2\). For \(t<-1\), it is \(-1\) on \((-1,1)\) and \(-2\) on \((1,-t)\), giving \(2+4(-t-1)\). All remaining values are zero. These three cases prove the norm formula, including both transitions and \(t=0\). \(\square\)

In particular \(f_1=i\sin x/x\), \(f_{-1}=-i\sin x/x\), and both have squared norm \(\pi\).

We will use the corresponding inner-product identity for smooth \(L^2\) functions with regular \(L^2\) transforms. It follows from U046's norm identity applied to \(f+g,f-g,f+ig,f-ig\): for the convention \(\langle f,g\rangle=\int f\overline g\),
\[
4\langle f,g\rangle
=\|f+g\|_2^2-\|f-g\|_2^2
 +i\|f+ig\|_2^2-i\|f-ig\|_2^2.
\]
Expansion of the four squares verifies this sign. Substituting the four norm identities gives
\(\langle f,g\rangle=(2\pi)^{-1}\langle Ff,Fg\rangle\).

## A quadratic pole remembers both sides

**Lemma 2.0 (a quantitative scalar pole).** Fix a compact interval containing the support of a smooth test \(q\). For \(0<\varepsilon\le1/2\) and \(\sigma\in\{-1,1\}\),
\[
\left|\int\frac{q(y)}{y+i\sigma\varepsilon}dy
 -\operatorname{pv}\int\frac{q(y)}y\,dy
 +i\sigma\pi q(0)\right|
\le C\varepsilon\log(2/\varepsilon)\|q\|_{C^1}.
\]
The constant depends on the fixed interval and a fixed cutoff, not on \(q\) or \(\varepsilon\).

**Proof.** Choose a real even compact smooth \(\chi\), equal to one near zero, and write \(q=q(0)\chi+yh\). The quotient \(h=(q-q(0)\chi)/y\) is smooth by FTC and supported in a fixed interval \([-A,A]\). Near zero its absolute value is bounded by a derivative of the numerator; away from zero division is bounded. Thus \(\|h\|_\infty\le C\|q\|_{C^1}\).

The real kernel is \(y/(y^2+\varepsilon^2)\). Its error on \(yh\) relative to the principal value is
\(-\varepsilon^2\int h(y)/(y^2+\varepsilon^2)dy\), of absolute value at most \(\pi\varepsilon\|h\|_\infty\). Both constant real terms vanish by oddness. The imaginary kernel is \(-\sigma\varepsilon/(y^2+\varepsilon^2)\). On the constant term, the mass difference is bounded by
\[
|q(0)|\int\frac{\varepsilon|1-\chi(y)|}{y^2+\varepsilon^2}dy
\le C\varepsilon|q(0)|,
\]
because \(1-\chi=0\) on a fixed neighborhood of zero and is bounded elsewhere. We used the exact integral \(\int\varepsilon/(y^2+\varepsilon^2)dy=\pi\), proved by scaling the arctangent primitive. On \(yh\), the bound is
\[
\|h\|_\infty\int_{-A}^A
 \frac{\varepsilon|y|}{y^2+\varepsilon^2}dy
=\varepsilon\log\!\left(1+\frac{A^2}{\varepsilon^2}\right)\|h\|_\infty.
\]
The logarithmic primitive follows by differentiation. Combining the bounds proves the claim and also proves the stated principal-value limit. \(\square\)

**Theorem 2.1 (quadratic boundary transforms).** For \(s>0\), both limits
\(B_s^\pm=\lim_{\varepsilon\downarrow0}(x^2-s^2\pm i\varepsilon)^{-1}\) exist strongly in \(\mathcal S'\). With \(P_a=\operatorname{pv}(1/(x-a))\), symmetrically deleted at \(a\),
\[
\begin{gathered}
B_s^\pm=\frac{P_s-P_{-s}}{2s}
 \mp\frac{i\pi}{2s}(\delta_s+\delta_{-s}),\\
FB_s^\pm=\mp\frac{i\pi}{s}e^{\mp is|\xi|}.
\end{gathered}
\tag{2.1}
\]

**Proof: local coordinates and both masses.** Near \(x=s\) and \(x=-s\), use \(y=x^2-s^2\). Its inverse branches are explicitly
\(x_\pm(y)=\pm\sqrt{s^2+y}\), for \(|y|<s^2/2\), with absolute derivative
\[
|x_\pm'(y)|=\frac1{2\sqrt{s^2+y}}.
\]
The scalar derivative rules prove their smoothness and bounded derivatives on smaller compact subintervals. Choose disjoint compact smooth cutoffs \(\rho_\pm\) in these charts, equal to one near the respective root. Absolute substitution transforms the local test into
\[
q_\pm(y)=\frac{\rho_\pm(x_\pm(y))\theta(x_\pm(y))}
                  {2\sqrt{s^2+y}},
\]
extended by zero; its support is fixed inside the chart. Its \(C^1\) norm is at most \(C_s(\|\theta\|_\infty+\|\theta'\|_\infty)\), by the product and chain rules. Its value at zero is \(\theta(\pm s)/(2s)\). Lemma 2.0 gives exactly the two indicated point coefficients and a real principal value with deletion \(|x^2-s^2|>r\).

On the remaining factor \(1-\rho_+-\rho_-\), the real denominator has no zero. The difference between the regularized reciprocal and the ordinary reciprocal has absolute value at most \(\varepsilon/(x^2-s^2)^2\). Multiplying by that cutoff produces an integrable function bounded away from the roots and decaying like \(x^{-4}\). The tested error is therefore at most \(C_s\varepsilon\|\theta\|_\infty\). Together with the two local estimates this proves a global bound by
\[
C_s\varepsilon\log(2/\varepsilon)
  \bigl(\|\theta\|_\infty+\|\theta'\|_\infty\bigr).
\]
It proves convergence uniformly on every bounded Schwartz family, as well as continuity of the resulting tempered functional.

**Proof: identify the canonical real part.** Away from the roots,
\[
\frac1{x^2-s^2}=\frac1{2s}
 \left(\frac1{x-s}-\frac1{x+s}\right).
\]
Near a root \(a=\pm s\), writing \(x=a+h\), the tested density equals \(\theta(a)/(2ah)\) plus a smooth remainder. Indeed \((\theta(a+h)-\theta(a))/h\) is smooth by FTC, and \(2a+h\) stays nonzero. At \(s\), deletion \(|x^2-s^2|\le r\) removes distances
\[
\sqrt{s^2+r}-s=\frac r{\sqrt{s^2+r}+s},\qquad
s-\sqrt{s^2-r}=\frac r{s+\sqrt{s^2-r}}
\]
on the two sides. Their ratio tends to one; at \(-s\) the distances are interchanged. The bounded remainder loses intervals whose lengths tend to zero. For the singular constant, the difference from symmetric deletion is a constant times the logarithm of that ratio, hence tends to zero. This proves the real-part formula in (2.1), with no extra point term.

**Proof: the complete Fourier transform.** U046 proves \(F\operatorname{sgn}=-2iP_0\). Apply \(F\), use \(F^2=2\pi R\), and divide to obtain \(FP_0=-i\pi\operatorname{sgn}\). Translation gives \(FP_a=-i\pi e^{-ia\xi}\operatorname{sgn}\xi\). Hence
\[
F\left(\frac{P_s-P_{-s}}{2s}\right)
=-\frac\pi s\sin(s|\xi|),\qquad
F(\delta_s+\delta_{-s})=2\cos(s\xi).
\]
Combining the sine and cosine terms gives exactly the exponential in (2.1) for each sign. Every operation acts on the whole tempered distribution. \(\square\)

## An imaginary differential term selects the limit

**Theorem 3.1 (the vanishing resolvent).** For every \(\varepsilon>0\),
\(L_\varepsilon=i\varepsilon\partial_x^4+\partial_x^2+1\) has exactly one tempered fundamental solution:
\[
E_\varepsilon=Gm_\varepsilon,\qquad
m_\varepsilon(\xi)=\frac1{1-\xi^2+i\varepsilon\xi^4}.
\tag{3.1}
\]
Its strong tempered limit is
\[
E_\varepsilon\longrightarrow E=-\frac i2e^{i|x|},
\qquad (\partial_x^2+1)E=\delta_0.
\tag{3.2}
\]

**Proof: invert the fixed regularization.** The imaginary part of
\(p_\varepsilon=1-\xi^2+i\varepsilon\xi^4\) vanishes only at zero, where its real part is one. Thus its reciprocal is smooth. On compact sets \(|p_\varepsilon|\) has a positive minimum, while for \(|\xi|\ge2\) its real part gives
\[
|m_\varepsilon(\xi)|\le\frac1{\xi^2-1}\le\frac4{3\xi^2}.
\]
Every derivative of \(1/p_\varepsilon\) is a finite sum of products of derivatives of \(p_\varepsilon\) divided by powers of \(p_\varepsilon\). This follows inductively from the product and reciprocal rules. The compact minimum and tail bound show polynomial growth of each derivative. Product-rule estimates then make multiplication continuous on \(\mathcal S\): for each \(N\), finitely many polynomial bounds are dominated by \(CP_M\) for some finite \(M\). Transposition defines the corresponding product on \(\mathcal S'\).

The Fourier equation is \(p_\varepsilon FE_\varepsilon=F\delta_0=1\). Multiplication by \(1/p_\varepsilon\) constructs \(FE_\varepsilon=m_\varepsilon\) and forces uniqueness. The regular function \(m_\varepsilon\) is tempered by the same bounds, so (3.1) is well defined.

**Proof: a uniform comparison near the two roots.** Put \(f(\xi)=1-\xi^2\) and \(g(\xi)=\xi^4\). Near \(a=\pm1\), \(g\ge c>0\) and
\(|g-1|=|f|(\xi^2+1)\le C|f|\). The exact difference is
\[
\frac1{f+i\varepsilon g}-\frac1{f+i\varepsilon}
=\frac{-i\varepsilon(g-1)}
       {(f+i\varepsilon g)(f+i\varepsilon)}.
\tag{3.3}
\]
Its absolute value is at most \(C\varepsilon|f|/(f^2+\varepsilon^2)\). The explicit coordinate \(\xi=\pm\sqrt{1-y}\), \(y=f(\xi)\), has bounded absolute Jacobian on these fixed neighborhoods. Integrating the estimate there gives
\(C\varepsilon\log(2/\varepsilon)\|\theta\|_\infty\).
The constant-imaginary kernel is \(-( \xi^2-1-i\varepsilon)^{-1}\), so Theorem 2.1 and its quantitative proof give the local limit
\[
m=\operatorname{Pf}\frac1{1-\xi^2}
  -\frac{i\pi}{2}(\delta_1+\delta_{-1}).
\tag{3.4}
\]
Here \(\operatorname{Pf}\) means deletion \(|1-\xi^2|>r\); its real part is \(-(P_1-P_{-1})/2\), by the already proved deletion comparison.

Away from the two fixed root neighborhoods,
\[
\left|\frac1{f+i\varepsilon g}-\frac1f\right|
\le\frac{\varepsilon|g|}{|f|^2}\le C\varepsilon.
\]
The last ratio is bounded there, including the tails. Its pairing is bounded by \(C\varepsilon\|\theta\|_1\le C'\varepsilon P_2(\theta)\), using \(\int(1+\xi^2)^{-1}d\xi=\pi\). The local and nonlocal estimates prove strong convergence \(m_\varepsilon\to m\), with an error bounded by \(C\varepsilon\log(2/\varepsilon)P_2(\theta)\). The previously proved strong continuity of \(G\) passes this to \(E_\varepsilon\).

**Proof: identify and verify the selected solution.** Formula (3.4) is \(m=-B_1^-\). Theorem 2.1 gives \(Fm=-i\pi e^{i|x|}\), and \(G=(2\pi)^{-1}RF\) gives \(E=-ie^{i|x|}/2\). On both open half-lines \(v=e^{i|x|}\) solves \(v''+v=0\). It is continuous at zero, and \(v'\) jumps from \(-i\) to \(i\). Integration by parts twice against a compact test on the two half-lines gives a jump term \(2i\theta(0)\), with no derivative of a point mass because the function itself has no jump. Thus \(v''+v=2i\delta_0\), proving (3.2). \(\square\)

**Corollary 3.2 (the local imaginary signs).** Let \(r\) be real smooth, with every derivative polynomially bounded, and \(r(1)r(-1)\ne0\). For each \(\varepsilon>0\), \((f+i\varepsilon r)^{-1}\) is a Schwartz multiplier, and its strong tempered limit is
\[
\operatorname{Pf}\frac1f
-\frac{i\pi}{2}\operatorname{sgn}r(1)\delta_1
-\frac{i\pi}{2}\operatorname{sgn}r(-1)\delta_{-1}.
\tag{3.5}
\]
**Proof.** A zero of the complex denominator would have \(f=0\), but the imaginary part is nonzero at both such points. Its reciprocal is smooth. Compact minima, the bound \(1/|f|\) on the tails, and the differentiated reciprocal formula just proved give polynomial bounds on all derivatives for fixed \(\varepsilon\).

Near \(a=\pm1\), continuity gives a fixed sign and \(|r|\ge c>0\). FTC gives \(|r(\xi)-r(a)|\le C|\xi-a|\le C'|f(\xi)|\). Compare to \(1/(f+i\varepsilon r(a))\) as in (3.3). Both denominator moduli dominate a positive constant times \(\sqrt{f^2+\varepsilon^2}\), and the difference has the same \(C\varepsilon|f|/(f^2+\varepsilon^2)\) bound. Lemma 2.0 at height \(\varepsilon|r(a)|\) gives the sign \(-i\pi\operatorname{sgn}r(a)\), with absolute Jacobian \(1/2\). Changing this fixed positive height factor does not change the limit or the logarithmic error order.

On the complement of the root neighborhoods the error from \(1/f\) is at most \(\varepsilon|r|/f^2\). Choose an integer \(d\ge0\) with \(|r(\xi)|\le C\langle\xi\rangle^d\). On the tails its pairing is bounded by \(C\varepsilon P_{d+2}(\theta)\int\langle\xi\rangle^{-6}d\xi\); this integral is finite by comparison with \((1+\xi^2)^{-1}\). The remaining compact portion has an \(O(\varepsilon)\|\theta\|_\infty\) bound. The resulting finite-seminorm error proves strong convergence on all bounded Schwartz sets. Only the two local signs enter the point coefficients. \(\square\)

## Exercises

**Exercise 1 (foundation).** For \(s>0\) and real \(b\), find the entire transform of \(((x-b)^2-s^2+i0)^{-1}\), and display the principal values and both point masses before transformation.

**Exercise 2 (intermediate).** For \(k>0\), find the two even fundamental solutions of \(\partial_x^2+k^2\) selected by opposite imaginary quadratic boundaries. Compute their difference and its Fourier distribution, and verify the point source directly.

**Exercise 3 (intermediate).** For \(a>0\) and real \(t\), find the complete transform and squared norm of \((\cos(ax)-e^{-itx})/x\), including all interval transitions and its value at zero.

**Exercise 4 (advanced).** For \(t,u\in[-1,1]\), calculate \(\int f_t\overline{f_u}\) and \(\|f_t-f_u\|_2\). Determine the exact continuity rate of the parametrization.

**Exercise 5 (advanced).** For real smooth \(r\) with polynomially bounded derivatives and \(r(\pm1)>0\), prove the multiplier property and strong limit of \((1-\xi^2+i\varepsilon r(\xi))^{-1}\), and identify its inverse-transform limit.

**Exercise 6 (advanced).** Use the imaginary term \(i\varepsilon\xi\) instead. Determine the limiting frequency distribution, the physical fundamental solution, its exact support and its derivative jump.

**Exercise 7 (intermediate).** Classify all tempered solutions of \((\partial_x^2+1)u=\delta_0\). Explain why regularization gives uniqueness although the limiting equation has a two-parameter family.

**Exercise 8 (advanced).** Let \(g\in\mathcal S\), with \(Fg\) compact smooth and supported away from \(\{-1,1\}\). Prove that \(u_\varepsilon=G(m_\varepsilon Fg)\) converges in every Schwartz seminorm, identify the limit and verify both forced equations.

## Solutions

**Solution 1.** Translating every test by \(b\) gives
\[
\frac{P_{b+s}-P_{b-s}}{2s}
-\frac{i\pi}{2s}(\delta_{b+s}+\delta_{b-s}).
\]
Both masses have the negative imaginary sign because the absolute slope is \(2s\) at each root. U046's translation rule multiplies the complete transform by \(e^{-ib\xi}\), giving
\[
-\frac{i\pi}{s}e^{-ib\xi}e^{-is|\xi|}.
\]
The principal values are each symmetrically deleted about their own translated center. This is the entire distribution, including both masses.

**Solution 2.** The Fourier equation is \((k^2-\xi^2)FE=1\). The upper boundary is \(-B_k^-\) and the lower boundary is \(-B_k^+\); the overall negative sign reverses the imaginary side. Theorem 2.1 and inversion give
\[
E_{\rm out}=-\frac{i}{2k}e^{ik|x|},\qquad
E_{\rm in}=\frac{i}{2k}e^{-ik|x|}.
\]
Both are continuous. For each, the derivative at zero from the right is \(1/2\) and from the left is \(-1/2\); their jump is one. Two half-line integrations by parts therefore give the required delta source with no delta derivative, while the homogeneous equation holds off zero. Their difference and its transform are
\[
E_{\rm out}-E_{\rm in}=-\frac i k\cos(kx),\qquad
F(E_{\rm out}-E_{\rm in})
=-\frac{i\pi}{k}(\delta_k+\delta_{-k}).
\]
This also matches the difference of the two boundary formulas.

**Solution 3.** Replace the endpoints \(1,-1\) in (1.2) by \(a,-a\):
\[
\frac{\cos(ax)-e^{-itx}}x
=\frac i2\int_{-t}^ae^{irx}dr
 +\frac i2\int_{-t}^{-a}e^{irx}dr.
\]
Its value at zero is \(it\), and its transform is \(i\pi(J_{-t,a}+J_{-t,-a})\). The finite-integral and tail bounds prove smoothness and \(L^2\) membership, so U046's norm lemma applies. For \(|t|\le a\), the squared interval sum integrates to \(2a\). For \(t>a\), values two on \((-t,-a)\) and one on \((-a,a)\) give \(4(t-a)+2a\). For \(t<-a\), values minus one on \((-a,a)\) and minus two on \((a,-t)\) give \(2a+4(-t-a)\). Thus
\[
\int\left|\frac{\cos(ax)-e^{-itx}}x\right|^2dx
=\pi\bigl[a+2(|t|-a)_+\bigr].
\]
The extra intervals are empty at \(t=\pm a\); the same formula includes both transition values.

**Solution 4.** Write \(S_t=J_{-t,1}+J_{-t,-1}\). On \((-1,1)\) it changes from minus one to plus one at \(-t\). The product \(S_tS_u\) is minus one between \(-t\) and \(-u\), an interval of length \(|t-u|\), and plus one elsewhere. Hence its integral is \(2-2|t-u|\). The inner-product version of Parseval proved after Theorem 1.1 gives
\[
\int f_t\overline{f_u}=\pi(1-|t-u|),\qquad
\|f_t-f_u\|_2^2=2\pi|t-u|.
\]
The norm identity also follows by adding the two squared norms \(\pi\) and subtracting twice the real part of the pairing. The exact distance is \(\sqrt{2\pi}|t-u|^{1/2}\). On every nondegenerate parameter interval, its ratio to \(|t-u|^\alpha\) is unbounded near equal parameters whenever \(\alpha>1/2\), in particular for \(\alpha=1\). The exponent one half is therefore sharp.

**Solution 5.** A complex denominator zero would require \(\xi=\pm1\), where the assumed positive imaginary coefficients exclude it. All reciprocal derivatives have polynomial bounds by the explicit product/reciprocal argument in Theorem 3.1 and Corollary 3.2. This proves the multiplier assertion for each fixed positive \(\varepsilon\), without a sign requirement away from the two roots.

Corollary 3.2 applies with both local signs positive and gives
\[
\operatorname{Pf}\frac1{1-\xi^2}
-\frac{i\pi}{2}(\delta_1+\delta_{-1})=-B_1^-.
\]
Its inverse is \(-ie^{i|x|}/2\). The corollary's finite-seminorm error proves strong convergence and remains so after inverse Fourier transformation. The positive sizes \(r(\pm1)\) only rescale the two small heights; reversing either sign reverses only that root's point coefficient, leaving the real finite part unchanged.

**Solution 6.** Here \(r(1)=1\), \(r(-1)=-1\), so the limit is
\[
m=\operatorname{Pf}\frac1{1-\xi^2}
-\frac{i\pi}{2}\delta_1+\frac{i\pi}{2}\delta_{-1}.
\]
The real part is \(-(P_1-P_{-1})/2\). Its Fourier transform is \(\pi\sin|x|\), by Theorem 2.1, and its inverse is \(\frac12\sin|x|\). The two masses invert to
\((-i/4)e^{ix}+(i/4)e^{-ix}=\frac12\sin x\).
Thus
\[
Gm=\tfrac12(\sin|x|+\sin x)=H(x)\sin x.
\]
This vanishes on the negative half-line and has exact support \([0,\infty)\). Indeed sine cannot vanish identically on any positive open interval: its derivative would make cosine vanish there too, contradicting \(\sin^2+\cos^2=1\). Every neighborhood of zero also meets an interval where it is nonzero. The function is continuous at zero and its derivative jumps from zero to one. Half-line integration by parts gives \(E''+E=\delta_0\).

**Solution 7.** Subtract \(E=-ie^{i|x|}/2\). For the difference \(v\), put \(W=Fv\); then \((1-\xi^2)W=0\). We prove the complete kernel without a point-support theorem. Choose compact smooth \(\zeta_+,\zeta_-\) with values \(1,0\) at \(1,-1\) and \(0,1\), respectively. For each \(\theta\in\mathcal S\), the numerator
\(\theta-\theta(1)\zeta_+-\theta(-1)\zeta_-\) vanishes at both roots. FTC division at each simple factor makes
\[
q(\xi)=\frac{\theta(\xi)-\theta(1)\zeta_+(\xi)-\theta(-1)\zeta_-(\xi)}
                  {1-\xi^2}
\]
smooth there. Off fixed root neighborhoods, derivatives of the reciprocal are polynomially bounded and decay on the tails, so \(q\in\mathcal S\). Testing \(W\) on this decomposition gives
\(W(\theta)=W(\zeta_+)\theta(1)+W(\zeta_-)\theta(-1)\).
Consequently \(W=c_+\delta_1+c_-\delta_{-1}\), and every solution is
\[
u=-\frac i2e^{i|x|}+Ae^{ix}+Be^{-ix},\qquad A,B\in\mathbb C.
\]
Conversely both added waves are tempered and solve the homogeneous equation, so every pair is allowed. Their Fourier masses have distinct supports and independent coefficients. For the regularized problem, multiplication by the global reciprocal \(1/p_\varepsilon\) kills the Fourier difference of two fundamental solutions. Thus regularization has uniqueness even though the limiting equation does not.

**Solution 8.** Set \(h=Fg\) and \(K=\operatorname{supp}h\). If \(h=0\), all functions and claims are zero. Otherwise compactness supplies a compact neighborhood \(K'\) of \(K\) and \(d>0\) with \(|1-\xi^2|\ge d\) there. On \(K'\times[0,1]\), every denominator has modulus at least \(d\). Induction using the reciprocal rule shows that each \(\partial_\xi^j m_\varepsilon\) and its \(\varepsilon\)-derivative is a finite rational expression with a nonvanishing denominator and bounded numerator on this compact set. FTC in \(\varepsilon\) gives
\[
\sup_{K'}\left|\partial_\xi^j
\left(m_\varepsilon-\frac1{1-\xi^2}\right)\right|
\le C_{j,K'}\varepsilon.
\]
Leibniz and bounded weights on \(K\) make every Schwartz seminorm of the product difference tend to zero. The functions are extended by zero off the support of \(h\); multiplication is smooth because the rational factors are smooth near that support. Continuity of the supplied Schwartz inverse then gives
\[
u_\varepsilon\longrightarrow
u=G\left(\frac{h}{1-\xi^2}\right)\quad\hbox{in }\mathcal S.
\]
Multiplication by \(p_\varepsilon\) verifies \(L_\varepsilon u_\varepsilon=g\), and multiplication by \(1-\xi^2\) verifies \((\partial_x^2+1)u=g\). Both point terms of the general limiting multiplier annihilate \(h\), since it vanishes near their supporting roots.

## References

- Semyon Dyatlov, [*Lecture notes for 18.155: distributions, elliptic regularity, and applications to PDEs*](https://math.mit.edu/~dyatlov/18.155/155-notes.pdf), free author notes, Section 5.2.3, PDF page 64, formulas (5.26)–(5.27), the complete symmetric principal-value derivation. Boundary-value exercises in the notes are not used as supplied proofs; Lemma 2.0 and Theorem 2.1 above prove all limits and their strong estimates.
- Terence Tao, [*Lecture Notes 2, Math 247A*](https://www.math.ucla.edu/~tao/247a.1.06f/notes2.pdf), Fall 2006, PDF pages 19–20, Fourier symmetries and Schwartz Parseval. The supplied programme proofs establish inversion and the exact convention and norm limit independently of the source's polynomial-Gaussian density assertion.
- [U046](spectral-gaps-and-explicit-fourier-distributions.md), Proposition 1.1, Section 3 and Lemma 5.1; [Fourier foundation](../prerequisites/U011-free-foundations/schwartz-fourier-foundations-U017.md), F1–F5; and the exact scalar and integration sections named above. All programme proofs and their component licences accompany this edition.
