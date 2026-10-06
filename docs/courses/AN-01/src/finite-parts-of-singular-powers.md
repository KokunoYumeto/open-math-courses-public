# Finite parts of singular powers

*Reconstructed by GPT-6 Astra (OpenAI), Ultra reasoning effort, October 2026. The earlier edition was written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort. Original lesson exposition and exercises: CC0. Separately credited programme prerequisites retain their own licences.*

A divergent power integral can have a well-defined constant after its divergent terms are removed. That constant is a distribution. Its derivative and dilation remember the singular endpoint through explicit point terms. We construct the whole complex-parameter family, prove both cutoff formulas, and determine exactly when the one-sided scaling obstruction cancels.

The supplied [gamma integral and reciprocal proof](../prerequisites/U011-free-foundations/gamma-foundations-U016.md) includes the entire product construction, every pole and residue, and all parameter-integral estimates. It is a licensed selection from an earlier programme lesson, with its analytic preliminaries supplied. [Order, positivity and distributional limits](order-positivity-and-limits.md), Definition (1.2) and Proposition 1.2, supplies the finite-order test estimates and extension to finite differentiability. [Cauchy kernels and distributional boundary limits](cauchy-kernels-and-boundary-limits.md), Corollary 2.2 and Section 4, supplies complex power series and the precise symmetric-pole normalization. The one-variable identity theorem is proved in [Gluing holomorphic sides](gluing-holomorphic-sides.md), Lemma 3.2. Their included scalar and integration foundations prove the calculus, cutoffs and convergence arguments used here. We prove the needed point-supported distribution theorem below.

All distributions act complex linearly on tests. Write \(p_m(\phi)=\max_{0\le j\le m}\|\phi^{(j)}\|_\infty\) on a fixed compact support. Derivatives mean \(u'(\phi)=-u(\phi')\), and multiplication means \((xu)(\phi)=u(x\phi)\). These are distributions by the product rule and the finite-order estimate. Let \(\delta_0(\phi)=\phi(0)\), so \(\delta_0^{(j)}(\phi)=(-1)^j\phi^{(j)}(0)\).

**Taylor and continuation details used throughout.** For \(m\ge1\), repeated fundamental-theorem integration gives

\[
 \phi(x)=\sum_{j=0}^{m-1}\frac{\phi^{(j)}(0)}{j!}x^j
 +\frac{x^m}{(m-1)!}\int_0^1(1-t)^{m-1}\phi^{(m)}(tx)\,dt.
 \tag{T}
\]

For \(m=1\) this is the fundamental theorem after the substitution \(s=tx\). Integrating the next derivative once more and interchanging the two continuous integrals over the finite triangle changes the remainder kernel of order \(m\) to the kernel of order \(m+1\), giving induction. Oriented integration proves the same formula for negative \(x\). Thus its remainder is bounded by \(p_m(\phi)|x|^m/m!\). Applying the formula to each derivative gives every derivative remainder used below.

For positive \(x\), set \(x^a=\exp(a\log x)\) with the real logarithm. The gamma prerequisite, (G0)–(G2), proves these complex powers, their derivatives, and
\(\int_0^1x^{\sigma-1}|\log x|^j\,dx=j!/\sigma^{j+1}\) for \(\sigma>0\). It also proves complex differentiation inside each power integral with these envelopes. Holomorphic dependence of a distribution means holomorphy after every test pairing. Every family below has an explicit common finite-order bound on each compact parameter set and compact test support.

We also use the meromorphic identity principle in its following elementary form. A function locally given as a holomorphic function divided by a power of \(a-a_0\) is meromorphic. If two such functions agree on an open subset of a connected domain, they agree throughout. Indeed, the set of points with zero difference as a meromorphic germ is open. At a limit point, clear its possible pole by multiplying by a sufficiently high power; the holomorphic identity theorem on a disk makes the resulting function zero there. Thus the set is also closed. A Laurent coefficient is an ordinary coefficient of this local power series after the pole is cleared, so its uniqueness follows from the proved power-series uniqueness.

## A normalized family separates existence from finite-part calculations

Initially, for \(\operatorname{Re}a>-1\), define

\[
 U_a(\phi)=\int_0^\infty x^a\phi(x)\,dx.
 \tag{1.1}
\]

On a compact test support contained in \([-R,R]\), \(R\ge1\), the integral is bounded by
\(p_0(\phi)\int_0^R x^{\operatorname{Re}a}\,dx\). This proves the distribution estimate. The logarithmic envelopes just proved give holomorphy, including every parameter derivative.

The supplied gamma proof constructs the entire function \(G=1/\Gamma\), with precisely the simple zeros \(0,-1,-2,\ldots\), and proves

\[
 G(z)=zG(z+1),\qquad G(1)=1,\qquad
 G'(-m)=(-1)^m m!\quad(m\ge0).
 \tag{1.3}
\]

It starts with the Euler integral on \(\operatorname{Re}z>0\), proves its exact reciprocal product by scaled beta integrals, and retains the normalization constant. Thus \(\Gamma\) has no zeros and has residue \((-1)^m/m!\) at \(-m\).

Here is the full distribution-family construction. For an integer \(s\ge0\) on the half-plane \(\operatorname{Re}a+s>-1\), put

\[
 C_a^{[s]}(\phi)=(-1)^sG(a+s+1)
                   \int_0^\infty x^{a+s}\phi^{(s)}(x)\,dx.
 \tag{N1}
\]

The power/log estimates prove holomorphy. For compact parameter sets, the least real exponent is strictly greater than \(-1\), and the largest exponent is finite. Splitting the integral at one proves one \(p_s\) bound; any fixed parameter derivative satisfies the same kind of bound.

On the overlap of two adjacent half-planes, integration by parts gives

\[
 \int_0^\infty x^{a+s+1}\phi^{(s+1)}(x)\,dx
 =-(a+s+1)\int_0^\infty x^{a+s}\phi^{(s)}(x)\,dx.
\]

The lower endpoint is zero because \(\operatorname{Re}(a+s+1)>0\); the upper endpoint is zero by compact support. Equation (1.3) makes \(C_a^{[s+1]}=C_a^{[s]}\). Any two permitted integers can be joined by adjacent ones, so the formulas define one entire family \(C_a\). Each parameter neighborhood is covered by one sufficiently large \(s\). In the initial half-plane it equals \(G(a+1)U_a\).

For every \(a\), choose such an \(s\) for \(a\); using \(s+1\) for \(a-1\) in (N1) proves the derivative identity by the test definition. At \(a=0\), \(G(1)=1\) gives the Heaviside function. Its derivative is \(\delta_0\), since \(-\int_0^\infty\phi'=\phi(0)\). Consequently

\[
 C_a=\frac{x_+^a}{\Gamma(a+1)},\qquad
 \partial_x C_a=C_{a-1},\qquad
 C_0=\boldsymbol1_{\{x>0\}},\qquad
 C_{-k}=\delta_0^{(k-1)}\quad(k\ge1).
 \tag{1.2}
\]

The first expression names the constructed continuation, including where its separate factors initially had no value. Every member is supported in \([0,\infty)\), directly from (N1).

Define \(U_a=\Gamma(a+1)C_a\) meromorphically. It agrees with (1.1) in its initial region. Its value at a pole is not defined; the Laurent coefficients will be distinct distributions.

**Proposition 1.1 (residues and a finite-order formula).** The family \(U_a\) has exactly the simple poles \(a=-k\), \(k\ge1\), with

\[
 R_k=\frac{(-1)^{k-1}}{(k-1)!}\delta_0^{(k-1)},\qquad
 R_k(\phi)=\frac{\phi^{(k-1)}(0)}{(k-1)!}.
 \tag{1.4}
\]

For integer \(s\ge0\), \(\operatorname{Re}a+s>-1\), and \(a\) not a negative integer,

\[
 U_a(\phi)=
 \frac{(-1)^s}{(a+1)\cdots(a+s)}
                 \int_0^\infty x^{a+s}\phi^{(s)}(x)\,dx.
 \tag{1.5}
\]

The empty denominator for \(s=0\) is one. This formula extends continuously to compact \(C^s\) tests and has order at most \(s\). As meromorphic families,

\[
 xU_a=U_{a+1},\qquad
 \partial_xU_a=aU_{a-1}.
 \tag{1.6}
\]

**Proof.** At \(-k\), the gamma factor's residue is \((-1)^{k-1}/(k-1)!\), and \(C_{-k}\) is the nonzero point derivative in (1.2). Their product gives (1.4), so no stated pole disappears. There are no other poles.

Multiplying (N1) by \(\Gamma(a+1)\) gives (1.5), because iteration of (1.3) gives
\(\Gamma(a+1)G(a+s+1)=1/[(a+1)\cdots(a+s)]\) away from the poles. Its integral estimate uses \(p_s\) on every compact support, also for \(C^s\) tests. The finite-regularity extension is unique by the smoothing proof in U008, Proposition 1.2.

The first identity (1.6) follows from the ordinary integral for \(\operatorname{Re}a>-1\). The second follows by integration by parts for \(\operatorname{Re}a>0\), with both endpoint terms zero. Apply the meromorphic identity principle to each test pairing on the whole parameter plane. At a pole the conclusion is equality of Laurent coefficients, never substitution of an infinite value. \(\square\)

## The constant Laurent coefficient contains a harmonic number

Let \(H_m=\sum_{j=1}^m1/j\), \(H_0=0\). For \(k\ge1\), define \(F_k\) to be the constant coefficient in

\[
 U_{-k+\varepsilon}
       =\frac{R_k}{\varepsilon}+F_k+O(\varepsilon),
 \tag{2.1}
\]

tested against each compact smooth function. Put \(F_0=U_0=\boldsymbol1_{\{x>0\}}\).

**Theorem 2.1 (explicit finite part).** For \(k\ge1\),

\[
 F_k(\phi)=\frac1{(k-1)!}
 \left[-\int_0^\infty\log x\,\phi^{(k)}(x)\,dx
                 +H_{k-1}\phi^{(k-1)}(0)\right].
 \tag{2.2}
\]

This is supported in \([0,\infty)\), agrees with \(x^{-k}\) on the positive half-line, and acts continuously on compact \(C^k\) tests.

**Proof.** Set \(a=-k+\varepsilon\) and \(s=k\) in (1.5). The finite product is

\[
 (a+1)\cdots(a+k)
 =(-1)^{k-1}(k-1)!\,\varepsilon
              \left[1-H_{k-1}\varepsilon+O(\varepsilon^2)\right].
 \tag{2.3}
\]

To see its linear coefficient, divide each nonzero factor \(-j+\varepsilon\), \(1\le j\le k-1\), by \(-j\). The resulting product of \(1-\varepsilon/j\) has linear coefficient \(-H_{k-1}\). Its reciprocal, including the numerator \((-1)^k\) from (1.5), is
\(-[1+H_{k-1}\varepsilon+O(\varepsilon^2)]/[\varepsilon(k-1)!]\).

The integral has expansion

\[
 \int_0^\infty x^\varepsilon\phi^{(k)}(x)\,dx
 =-\phi^{(k-1)}(0)
   +\varepsilon\int_0^\infty\log x\,\phi^{(k)}(x)\,dx
   +O(\varepsilon^2).
 \tag{2.4}
\]

For complex \(|\varepsilon|\le\eta<1\), the exponential series or its twice-integrated fundamental identity bounds the second-order remainder by
\(\tfrac12|\varepsilon|^2|\log x|^2 e^{|\varepsilon\log x|}\).
On \((0,1)\), this is bounded by a constant times
\(|\varepsilon|^2x^{-\eta}|\log x|^2\), which is integrable by (G1). On the remaining compact integration interval it has a fixed bound. The constant integral is \(\int_0^\infty\phi^{(k)}=-\phi^{(k-1)}(0)\). Multiplying the two expansions proves (2.2).

Since \(\log x\) is integrable at zero, (2.2) has a \(p_k\) estimate on any fixed support, proving that the coefficient is a distribution and its stated finite-regularity action. On tests supported strictly in the positive half-line, the integral (1.1) is entire in \(a\), so continuation and coefficient comparison give \(x^{-k}\) there. On negative-side tests every coefficient is zero. \(\square\)

In particular \(F_1(\phi)=-\int_0^\infty\log x\,\phi'(x)\,dx\), while
\(F_2(\phi)=-\int_0^\infty\log x\,\phi''(x)\,dx+\phi'(0)\).
The second formula's last term is part of its normalization.

**Corollary 2.2 (multiplication survives; differentiation has a correction).** For \(k\ge1\),

\[
 xF_k=F_{k-1},
 \tag{2.5}
\]

and for \(k\ge0\),

\[
 \partial_xF_k=-kF_{k+1}+R_{k+1}.
 \tag{2.6}
\]

Thus \(\partial_xF_0=\delta_0\), even though zero is not a pole of \(U_a\).

**Proof.** At \(a=-k+\varepsilon\), compare constant coefficients in \(xU_a=U_{a+1}\). For \(k=1\), the right side is regular and its constant is \(U_0\); the left residue is zero because \(x\delta_0=0\). For \(k\ge2\), both expansions give (2.5).

For \(k\ge1\), the constant coefficient of
\[
 \partial_xU_{-k+\varepsilon}
       =(-k+\varepsilon)U_{-(k+1)+\varepsilon}
\]
is \(-kF_{k+1}+R_{k+1}\). The residue contributes through the additional factor \(\varepsilon\). At \(k=0\), \(U_\varepsilon\) is regular and \(\varepsilon U_{-1+\varepsilon}\to R_1\). This proves (2.6) at every stated integer. \(\square\)

## Removing a small interval gives the same finite part

**Lemma 3.1 (uniqueness of nondecaying power and logarithm terms).** Suppose the distinct nonzero complex numbers \(\lambda_1,\ldots,\lambda_r\) satisfy \(\operatorname{Re}\lambda_j\ge0\). If

\[
 c_0+c_{\log}\log\varepsilon+
       \sum_{j=1}^r c_j\varepsilon^{-\lambda_j}
           \longrightarrow0\quad(\varepsilon\downarrow0),
 \tag{3.1}
\]

then every coefficient is zero. Empty power or logarithm sums are allowed.

**Proof.** Put \(t=-\log\varepsilon\). If a positive real part occurs, take the largest one, \(\sigma>0\), and divide by \(e^{\sigma t}\). The original expression tends to zero after this division; the constant, linear, and smaller-exponent terms also tend to zero. The remaining trigonometric sum \(p(t)=\sum_{\operatorname{Re}\lambda_j=\sigma}c_je^{i\operatorname{Im}\lambda_jt}\) therefore tends to zero.

For distinct real frequencies \(\beta_j\), any finite sum \(p(t)=\sum_jd_je^{i\beta_jt}\) tending to zero has all coefficients zero. Indeed it is bounded, and
\(L^{-1}\int_0^L|p(t)|^2dt\to0\), by separating a fixed initial interval from a uniformly small tail. Expanding the square makes the same mean tend to \(\sum_j|d_j|^2\): every off-diagonal integral is
\((e^{i(\beta_j-\beta_l)L}-1)/(i(\beta_j-\beta_l)L)\to0\).
Thus each coefficient at real part \(\sigma\) vanishes. Repeat through the finitely many positive real parts.

The remaining exponentials have purely imaginary exponents and are bounded. A nonzero coefficient of the linear term \(-c_{\log}t\) would then contradict convergence to zero, so it vanishes. Apply the same mean-square argument, now including \(c_0\) as the zero-frequency coefficient. All remaining coefficients vanish. \(\square\)

**Theorem 3.2 (Hadamard cutoff formulas).** Let \(b_j=\phi^{(j)}(0)/j!\). If \(a\) is not a negative integer, then

\[
 U_a(\phi)=\lim_{\varepsilon\downarrow0}
 \left[\int_\varepsilon^\infty x^a\phi(x)\,dx
       +\sum_{\substack{j\ge0\\\operatorname{Re}(a+j+1)\le0}}
             \frac{b_j\varepsilon^{a+j+1}}{a+j+1}\right].
 \tag{3.2}
\]

The sum is finite with nonzero denominators. Terms of zero real exponent are included even when they are bounded oscillations. At \(a=-k\), \(k\ge1\),

\[
 F_k(\phi)=\lim_{\varepsilon\downarrow0}
 \left[\int_\varepsilon^\infty x^{-k}\phi(x)\,dx
       -\sum_{j=0}^{k-2}\frac{b_j\varepsilon^{j-k+1}}{k-j-1}
       +b_{k-1}\log\varepsilon\right].
 \tag{3.3}
\]

The power sum is empty for \(k=1\). The nondecaying terms and the remaining constant are unique for this cutoff parameter.

**Proof.** Choose \(M\ge1\) with \(\operatorname{Re}a+M>-1\), and put
\(r_M(x)=\phi(x)-\sum_{j=0}^{M-1}b_jx^j\) on \([0,1]\). Formula (T) gives \(|r_M(x)|\le p_M(\phi)x^M/M!\). Direct monomial integration for \(\operatorname{Re}a>-1\) gives

\[
 U_a(\phi)=\int_0^1x^ar_M(x)\,dx
       +\int_1^\infty x^a\phi(x)\,dx
       +\sum_{j=0}^{M-1}\frac{b_j}{a+j+1}.
 \tag{3.4}
\]

On the larger half-plane \(\operatorname{Re}a+M>-1\), the two integrals are holomorphic by their stated bounds and (G2); the finite sum is meromorphic. The meromorphic identity principle on that connected half-plane proves (3.4) throughout. The same bounds give finite-order estimates locally in the parameter.

For nonexceptional \(a\), integrate each polynomial from \(\varepsilon\) to one, obtaining

\[
 \int_\varepsilon^\infty x^a\phi(x)\,dx
 =U_a(\phi)-\sum_{j=0}^{M-1}
            \frac{b_j\varepsilon^{a+j+1}}{a+j+1}
       -\int_0^\varepsilon x^ar_M(x)\,dx.
 \tag{3.5}
\]

The final absolute value is at most
\(p_M(\phi)\varepsilon^{\operatorname{Re}a+M+1}/[M!(\operatorname{Re}a+M+1)]\), tending to zero. The monomials with positive real exponent also tend to zero. The remaining terms are exactly those in (3.2).

At \(a=-k\), take \(M\ge k\). In (3.4), only \(b_{k-1}/(a+k)\) has a pole, and its constant coefficient is zero. The other fractions and integrals are regular. Their values at \(-k\) therefore give \(F_k\). The exceptional monomial integrates to \(-b_{k-1}\log\varepsilon\); the monomials of lower degree give the powers in (3.3), and the higher degrees and residual lower integral tend to zero. This proves (3.3). The difference of two proposed decompositions has the form of Lemma 3.1 after equal exponents are combined, so it has every coefficient zero. \(\square\)

The endpoint prescription matters. If the excluded interval ends at \(c\varepsilon\), \(c>0\), update the power counterterms to that endpoint but keep the logarithmic counterterm \(b_{k-1}\log\varepsilon\). The result is

\[
 F_k-(\log c)R_k.
 \tag{3.6}
\]

Indeed the raw logarithmic term is \(-b_{k-1}\log(c\varepsilon)\). Its remaining constant is \(-b_{k-1}\log c\), which is precisely the displayed residue pairing. If the logarithmic counterterm also uses \(\log(c\varepsilon)\), the result remains \(F_k\).

## A pole leaves a logarithmic scaling correction

For \(t>0\), define

\[
 (D_tu)(\phi)=t^{-1}u(\phi(\cdot/t)).
 \tag{4.1}
\]

This is the distribution representing \(u(tx)\) for an ordinary locally integrable function, by substitution. It is continuous on each fixed compact test space by the chain rule. Homogeneity of degree \(a\) means \(D_tu=t^au\).

**Lemma J (all distributions supported at a point are finite jets).** If \(u\in\mathcal D'(\mathbb R)\) is zero on every test supported away from zero, then
\(u=\sum_{j=0}^N c_j\delta_0^{(j)}\) for some finite \(N\). The coefficients are unique.

**Proof.** Choose a smooth cutoff \(\chi=1\) near zero supported in \([-1,1]\). The finite-order definition in U008 gives \(C,N\) controlling tests supported in \([-1,1]\). For \(0<\varepsilon<1\),
\(u(\phi)=u(\chi(x/\varepsilon)\phi(x))\), because their difference is zero near zero.

If \(\phi^{(j)}(0)=0\) for \(0\le j\le N\), Taylor's formula applied to \(\phi^{(l)}\) gives
\(|\phi^{(l)}(x)|\le C_\phi|x|^{N+1-l}\) near zero, \(0\le l\le N\). The product rule shows that each derivative of \(\chi(x/\varepsilon)\phi(x)\) through degree \(r\le N\) is a finite sum of terms bounded by
\[
 C_{\phi,\chi}\varepsilon^{-j}
           \varepsilon^{N+1-(r-j)}
       =C_{\phi,\chi}\varepsilon^{N+1-r}
       \longrightarrow0.
 \tag{J}
\]
All supports stay in \([-1,1]\), so the distribution estimate makes \(u(\phi)=0\).

Now put \(\eta_j(x)=\chi(x)x^j/j!\), \(0\le j\le N\). Its derivative of degree \(l\le N\) at zero is one if \(l=j\) and zero otherwise. Subtracting
\(\sum_{j=0}^N\phi^{(j)}(0)\eta_j\) from any test removes all these derivatives. Hence
\(u(\phi)=\sum_j u(\eta_j)\phi^{(j)}(0)\), or \(c_j=(-1)^ju(\eta_j)\). The same tests isolate each coefficient, proving uniqueness and linear independence of the jets. \(\square\)

**Theorem 4.1 (scaling and the one-sided obstruction).** Away from its poles,
\(D_tU_a=t^aU_a\). At each pole \(-k\),

\[
 D_tF_k=t^{-k}\bigl(F_k+(\log t)R_k\bigr).
 \tag{4.2}
\]

With \(E=x\partial_x\), one has

\[
 (E+k)F_k=R_k.
 \tag{4.3}
\]

No distribution homogeneous of degree \(-k\) can equal \(x^{-k}\) on \(x>0\) and zero on \(x<0\).

**Proof.** Changing the variable in (1.1) proves the family dilation identity in the initial half-plane; continue meromorphically. Near \(a=-k+\varepsilon\), expand
\(t^a=t^{-k}(1+\varepsilon\log t+O(\varepsilon^2))\). Its product with (2.1) has constant \(t^{-k}(F_k+(\log t)R_k)\), giving (4.2).

The test product rule gives \(x\delta_0^{(j)}=-j\delta_0^{(j-1)}\) for \(j\ge1\), and \(x\delta_0=0\). In the residue normalization this says \(xR_{k+1}=R_k\). Multiply (2.6) by \(x\) and use (2.5) to obtain (4.3).

If \(D_tu=t^{-k}u\), differentiate (4.1) at \(t=1\). This is justified within the pairing: for \(t\) near one, the tests have a common compact support, and their difference quotients converge with every fixed derivative uniformly, by the ordinary parameter fundamental theorem. The derivative test is \(-\phi-x\phi'\), so the result is \(Eu=-ku\).

Any extension with the prescribed half-line values differs from \(F_k\) by a distribution supported at zero. A test away from zero splits into its positive and negative parts, both smooth because it vanishes near zero, which verifies this support assertion. Lemma J makes the difference a finite sum of jets. On each one,

\[
 E\delta_0^{(j)}=-(j+1)\delta_0^{(j)},\qquad
 (E+k)\delta_0^{(j)}=(k-j-1)\delta_0^{(j)}.
 \tag{4.4}
\]

At degree \(j=k-1\) the coefficient is zero. Thus no finite jet correction can cancel the nonzero \(\delta_0^{(k-1)}\) coefficient of \(R_k\) in (4.3); the other degrees are independent by Lemma J. This contradicts \((E+k)u=0\). \(\square\)

The normalized family \(C_a\) has no such anomaly. In its initial region it is homogeneous, and both tested sides of that identity are entire, so homogeneity holds at every \(a\). At \(-k\) it is the homogeneous point jet, which is zero off the origin. It is not an extension of the nonzero positive-half-line function \(x^{-k}\).

## Reflection cancels the obstruction in a symmetric finite part

Define reflection by \((\mathcal Ru)(\phi)=u(\phi(-\cdot))\). It is a distribution by the chain rule and sends the initial \(U_a\) to the negative-side power \(|x|^a\). Direct evaluation of the test derivatives gives

\[
 \mathcal RR_k=\frac1{(k-1)!}\delta_0^{(k-1)}.
 \tag{5.1}
\]

**Proposition 5.1 (the symmetric finite parts).** Put
\(S_k=F_k+(-1)^k\mathcal RF_k\), \(k\ge1\). Then

\[
 S_1=\operatorname{pv}\frac1x,\qquad
 \partial_xS_k=-kS_{k+1},\qquad
 D_tS_k=t^{-k}S_k.
 \tag{5.2}
\]

In particular,

\[
 S_k=\frac{(-1)^{k-1}}{(k-1)!}
        \partial_x^{k-1}\!\left(\operatorname{pv}\frac1x\right)
     =\operatorname{pf}\frac1{x^k},
 \tag{5.3}
\]

with the normalization proved in the Cauchy-kernel lesson.

**Proof.** Formula (2.2) and the substitution \(x\mapsto-x\) give
\(S_1(\phi)=-\int_{\mathbb R}\log|x|\,\phi'(x)\,dx\).
Integrating by parts off \((-\varepsilon,\varepsilon)\) produces

\[
 \int_{|x|>\varepsilon}\frac{\phi(x)}x\,dx
       +\bigl(\phi(\varepsilon)-\phi(-\varepsilon)\bigr)\log\varepsilon.
 \tag{5.4}
\]

The omitted logarithmic integral tends to zero by its absolute integrability. The added term is bounded by
\(2\varepsilon p_1(\phi)|\log\varepsilon|\to0\); that last limit follows by \(v=-\log\varepsilon\) and exponential domination. The remaining integral converges to the principal value proved in U013, Section 4.

On tests the chain rule gives
\(\partial_x\mathcal R=-\mathcal R\partial_x\).
Applying (2.6), the nonpoint terms combine to \(-kS_{k+1}\), and the point terms cancel because \(R_{k+1}=(-1)^k\mathcal RR_{k+1}\). Reflection commutes with \(D_t\) by their test definitions. The logarithmic terms in (4.2) cancel because \(R_k+(-1)^k\mathcal RR_k=0\), proving homogeneity. Iterating the derivative identity gives (5.3). \(\square\)

At degree two the harmonic-number terms in \(F_2+\mathcal RF_2\) also cancel. The second half-line supplies the opposite residue, allowing a symmetric homogeneous extension although the one-sided extension is obstructed.

## Exercises

1. **Residues are test jets — foundation.** Find the residues of \(U_a\) at \(-1,-2,-4\), with their test pairings. Explain the two alternating signs.
2. **The second finite part — intermediate.** Suppose \(\phi=1+2x+3x^2\) near zero. Give the divergent terms of \(\int_\varepsilon^\infty x^{-2}\phi(x)\,dx\), the formula tending to \(F_2(\phi)\), and the change when the endpoint is \(5\varepsilon\) but only the power counterterm changes to that endpoint.
3. **Bounded oscillations — advanced.** For \(a=-1+i\beta\), real \(\beta\ne0\), and \(\phi(0)\ne0\), identify the nondecaying term and its counterterm. Prove that the raw truncated integral has no limit.
4. **Derivative corrections — intermediate.** Compute \(F_1'\), \(F_2'\), and the second identity's point correction on a test with \(\phi''(0)=6\). Check \(F_0'\) directly.
5. **An impossible half-line extension — advanced.** Prove that no extension of \(x^{-3}\) on the positive half-line and zero on the negative half-line is homogeneous of degree \(-3\). Identify the jet degree that cannot be adjusted by \(E+3\).
6. **Dilation and reflection — advanced.** For \(\phi'(0)=2\), compute the extra term in \((D_4F_2)(\phi)\) relative to \(4^{-2}F_2(\phi)\). Prove its cancellation for \(F_2+\mathcal RF_2\), and explain why this is compatible with Exercise 5.

## Complete solutions

**Solution 1.** The residues are \(R_1=\delta_0\), \(R_2=-\delta'_0\), \(R_4=-\delta'''_0/6\). Their pairings are \(\phi(0)\), \(\phi'(0)\), and \(\phi'''(0)/6\). The coefficient \((-1)^{k-1}/(k-1)!\) is multiplied by the evaluation sign \((-1)^{k-1}\) of the delta derivative. Thus the residue pairing is the positive Taylor coefficient.

**Solution 2.** The divergent terms are \(\varepsilon^{-1}-2\log\varepsilon\); the degree-two Taylor term contributes no nondecaying divergence. Therefore
\[
 F_2(\phi)=\lim_{\varepsilon\downarrow0}
 \left[\int_\varepsilon^\infty x^{-2}\phi(x)\,dx
                 -\varepsilon^{-1}+2\log\varepsilon\right].
\]
At endpoint \(5\varepsilon\), subtract \((5\varepsilon)^{-1}\). Keeping \(2\log\varepsilon\) leaves \(-2\log5\), so the answer is \(F_2(\phi)-2\log5\). Updating the logarithm to \(2\log(5\varepsilon)\) would instead leave \(F_2(\phi)\).

**Solution 3.** Only \(j=0\) contributes a nonpositive real exponent. Formula (3.5) becomes
\[
 \int_\varepsilon^\infty x^{-1+i\beta}\phi(x)\,dx
 =U_{-1+i\beta}(\phi)
       -\frac{\phi(0)}{i\beta}\varepsilon^{i\beta}+o(1).
\]
The counterterm is \(+\phi(0)\varepsilon^{i\beta}/(i\beta)\). Choose
\(\varepsilon_n=e^{-2\pi n/|\beta|}\) and
\(\widetilde\varepsilon_n=e^{-(2n+1)\pi/|\beta|}\).
Their powers \(\varepsilon^{i\beta}\) equal \(1\) and \(-1\), respectively. Since the coefficient is nonzero, the raw integrals have two different limiting values. A prescription removing only unbounded terms would miss this bounded oscillation.

**Solution 4.** Equation (2.6) gives
\[
 F_1'=-F_2-\delta'_0,\qquad
 F_2'=-2F_3+\tfrac12\delta''_0.
\]
The second point correction pairs as \(\phi''(0)/2=3\). Directly,
\(F_0'(\phi)=-\int_0^\infty\phi'(x)\,dx=\phi(0)\), so \(F_0'=\delta_0\).

**Solution 5.** Lemma J gives \(u-F_3=\sum_jc_j\delta_0^{(j)}\). But
\((E+3)F_3=\delta''_0/2\), whereas
\((E+3)\delta_0^{(j)}=(2-j)\delta_0^{(j)}\).
The coefficient at degree two is zero, so it cannot cancel \(\delta''_0/2\). Every other jet degree is independent, and therefore \((E+3)u\ne0\). This contradicts the necessary Euler identity for degree \(-3\).

**Solution 6.** Here \(R_2=-\delta'_0\), so \(R_2(\phi)=2\). The extra term is
\(4^{-2}(\log4)\cdot2=(\log4)/8\).
Reflection gives \(\mathcal RR_2=\delta'_0\), and hence the two residues cancel in \(F_2+\mathcal RF_2\), along with the logarithmic term. This symmetric distribution equals \(x^{-2}\) on both half-lines. The one-sided extension in Exercise 5 has zero values on its negative half-line and therefore has no opposite-side contribution to cancel its residue. The prescribed extension data differ.

## Programme proof locations and freely accessible sources

- [The gamma integral and its entire reciprocal](../prerequisites/U011-free-foundations/gamma-foundations-U016.md), (G0)–(G2) and the complete earlier proof (W4a)–(W4e): complex powers, every parameter envelope, Euler integral/product identity, simple zeros and exact residues. This separately credited proof selection retains CC0 1.0.
- [Order, positivity and distributional limits](order-positivity-and-limits.md), Definition (1.2) and Proposition 1.2: exact finite-order topology and finite-regularity extension. Its supplied scalar and integration foundations prove the cutoff and convergence tools used above.
- [Cauchy kernels and distributional boundary limits](cauchy-kernels-and-boundary-limits.md), Corollary 2.2 and Section 4, and [Gluing holomorphic sides](gluing-holomorphic-sides.md), Lemma 3.2: complete power-series, pole-normalization and one-variable identity proofs.
- Semyon Dyatlov, [*Lecture notes for 18.155: distributions, elliptic regularity, and applications to PDEs*, freely accessible author notes](https://math.mit.edu/~dyatlov/18.155/155-notes.pdf), Section 4.4, Theorem 4.19 and Lemma 4.22, and Section 5.2 through Proposition 5.9. The shrinking-cutoff proof and derivative continuation were read as the human mathematical sources. Their needed arguments, estimates and exceptional parameters are proved explicitly in Lemma J and (N1)–(1.6) here.
