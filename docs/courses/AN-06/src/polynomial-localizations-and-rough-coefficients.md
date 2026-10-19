# Polynomial localizations and rough coefficients

*Written by GPT-6.1 Sol (OpenAI) and GPT-6 Astra (OpenAI). Self-checked by the writing AI. Original exposition: CC0.*

**Working question: Can narrow high peaks satisfy a short-range coefficient test?** A peak's height does not determine its local multiplication norm: its support size matters as well. The exponent selected by the available derivatives measures that tradeoff. Elliptic and real-principal-type operators supply different local regularity, so their admissible coefficient exponents must be computed rather than copied from one case to the other.

A potential can become arbitrarily large on small sets and still be short range. The useful size is a local \(L^p\) norm, with its exponent determined by the derivatives that the free operator controls. This lesson proves a coefficient criterion for elliptic operators and for operators of real principal type, including the critical-dimensional case.

We first identify those polynomial classes in the normalized frequency picture from [Polynomial translations and regular energies](polynomial-translations-and-regular-energies.md). We then apply the exact compactness criterion in [Short-range compactness and local tests](short-range-compactness-and-local-tests.md). Section 3 constructs the required derivative kernels and proves their finite Sobolev endpoint, including odd derivative gaps. For the classical fractional-integration theorem, see Tao, Proposition 6.1 and Corollary 6.3; for translated coefficient estimates in wave-operator theory, see Hörmander [HW, Section 2].

Throughout, \(D_j=-i\partial_j\), Fourier transformation is unitary, and \(\langle\xi\rangle=(1+|\xi|^2)^{1/2}\). Coefficients may be complex unless a later application expressly requires symmetry. The required Euclidean interchanges and Plancherel are proved in [A finite-derivative bound for left quantization](../providers/analysis/finite-derivative-l2.md#fourier-normalization). The complete programme reading [Approximation, convolution and integer Sobolev density](../providers/analysis/euclidean-approximation-and-convolution.md) proves Hölder, Young, finite-integral-norm translation and compact smooth Sobolev approximation, with all endpoints used below. The Fourier inverse factor is retained in Section 3, so the convolution kernels correspond exactly to the stated unitary convention.

<a id="localization-family"></a>
## 1. The normalized polynomials seen at infinity

The normalized localizations used here are those of Hörmander [H2, Definition 10.2.6]; their simple-characteristic condition is [H2, Definition 14.3.1].

For a nonzero real polynomial \(p\) of degree \(d\), put

\[
 T_p(\eta)=\left(\sum_{|\beta|\leq d}|\partial^\beta p(\eta)|^2\right)^{1/2},
 \qquad p_\eta(\xi)=p(\eta+\xi)/T_p(\eta).
 \tag{1}
\]

A nonzero constant derivative makes \(T_p\) positive everywhere. Taylor's formula identifies \(T_p(\eta)\) with a fixed norm of the translated coefficient vector. Therefore the \(p_\eta\) have compact closure in the finite-dimensional space of polynomials of degree at most \(d\). Every member of that closure satisfies \(T_Q(0)=1\).

Define \(\mathcal L(p)\) to be the set of limits of \(p_{\eta_\nu}\) along sequences \(|\eta_\nu|\to\infty\). This set is nonempty and compact. Indeed it is the intersection, over integer \(N\), of the nested nonempty compact closures of \(\{p_\eta:|\eta|\geq N\}\). A member of the intersection is obtained by choosing centres of size at least \(N\) whose normalized polynomials are within \(1/N\) of it. The term localization also allows a nonzero scalar multiple of such a limit.

**Lemma 1.1.** If \(Q\in\mathcal L(p)\) and \(a\in\mathbb R^n\), then

\[
 Q_a(\xi)=Q(\xi+a)/T_Q(a)\in\mathcal L(p).
 \tag{2}
\]

If \(p\) has no invariant direction, then \(\mathcal L(p-\lambda)=\mathcal L(p)\) for every fixed real \(\lambda\).

**Proof.** Suppose \(p_{\eta_\nu}\to Q\). Translation and differentiation are continuous on coefficient space, so

\[
 \frac{T_p(\eta_\nu+a)}{T_p(\eta_\nu)}
       =T_{p_{\eta_\nu}}(a)\longrightarrow T_Q(a)>0.
\]

Dividing the translated numerator by this ratio gives \(p_{\eta_\nu+a}\to Q_a\), proving (2).

The strength properness theorem in the linked polynomial lesson gives \(T_p(\eta)\to\infty\) when there is no invariant direction. The vectors defining the strengths of \(p\) and \(p-\lambda\) differ only in their zeroth component. Hence

\[
 |T_{p-\lambda}(\eta)-T_p(\eta)|\leq|\lambda|.
 \tag{3}
\]

Along any escaping sequence their ratio tends to one, and \(\lambda/T_p(\eta)\to0\). Their normalized translated polynomials consequently have the same limits. \(\square\)

Recall the simple-characteristic condition

\[
 T_p(\eta)\leq C\bigl(1+|p(\eta)|+|\nabla p(\eta)|\bigr).
 \tag{4}
\]

<a id="localization-simple-zeros"></a>
**Theorem 1.2.** Suppose \(p\) has no invariant direction. Condition (4) holds if and only if every real zero of every \(Q\in\mathcal L(p)\) is simple: \(Q(\xi)=0\) implies \(\nabla Q(\xi)\ne0\).

**Proof.** Divide (4) by \(T_p(\eta_\nu)\) and pass to a localization limit. Strength properness gives

\[
 1\leq C\bigl(|Q(0)|+|\nabla Q(0)|\bigr).
 \tag{5}
\]

Apply this to the normalized translates (2). At any zero \(a\) of \(Q\), (5) implies \(\nabla Q(a)\ne0\).

Conversely, the hypothesis implies \(|Q(0)|+|\nabla Q(0)|>0\) for every localization. Compactness of \(\mathcal L(p)\) makes its minimum a positive number \(c\). If \((|p(\eta)|+|\nabla p(\eta)|)/T_p(\eta)\) were smaller than \(c/2\) at arbitrarily large centres, an escaping sequence and a convergent coefficient subsequence would produce a localization contradicting that minimum. Thus (4) holds outside a ball. On the ball \(T_p\) is bounded, and the added \(1\) proves (4) there. \(\square\)

The no-invariant-direction hypothesis matters in this equivalence. For example \(p(\xi_1,\xi_2)=\xi_1^2\) satisfies (4), but translation along the \(\xi_2\) axis yields a quadratic localization with a multiple zero.

<a id="localization-affine"></a>
**Corollary 1.3.** If every localization of the nonzero real polynomial \(p\) has degree at most one, then \(p\) is simply characteristic. This localization condition is equivalent to

\[
 \frac{\partial^\beta p(\eta)}{T_p(\eta)}\longrightarrow0
       \quad(|\eta|\to\infty),\qquad |\beta|>1.
 \tag{6}
\]

**Proof.** Every affine \(Q\in\mathcal L(p)\) has the exact normalization

\[
 \begin{aligned}
 1&=T_Q(0)^2=|Q(0)|^2+|\nabla Q(0)|^2,\\
 |Q(0)|+|\nabla Q(0)|&\geq1.
 \end{aligned}
\]

If \((|p(\eta)|+|\nabla p(\eta)|)/T_p(\eta)<1/2\) at arbitrarily large centres, choose an escaping sequence with this property. A coefficient-convergent subsequence produces \(Q\in\mathcal L(p)\) with \(|Q(0)|+|\nabla Q(0)|\leq1/2\), a contradiction. Thus \(T_p\leq2(|p|+|\nabla p|)\) outside a ball. On the remaining compact ball \(T_p\) is bounded, and the added \(1\) in (4) gives the required global estimate. This proof uses no strength properness and allows invariant directions.

To prove the equivalence with (6), coefficient convergence sends every derivative of order greater than one to zero for an affine limit. If (6) failed for one derivative, an escaping subsequence with that normalized derivative bounded away from zero would have a limit of degree at least two. The reverse implication follows directly by taking the derivatives of every coefficient limit. \(\square\)

In particular, the corollary includes every nonzero constant and every affine polynomial, even when it has invariant directions. The hypothesis in Theorem 1.2 and its quadratic counterexample remain necessary for that theorem's equivalence.

<a id="localization-polynomial-classes"></a>
## 2. Polynomial classes and the available derivatives

An elliptic polynomial of degree \(d\geq1\) has principal homogeneous part \(p_d\) with \(p_d(\theta)\ne0\) for every unit real vector \(\theta\). Compactness of the sphere and the lower-degree remainder give, for large \(|\eta|\),

\[
 |p(\eta)|\geq c|\eta|^d,\qquad
 T_p(\eta)\asymp\langle\eta\rangle^d.
 \tag{7}
\]

For the upper bound, each derivative of a polynomial of degree \(d\) is at most \(C\langle\eta\rangle^d\). The lower bound at bounded frequencies follows from the positive constant derivative in \(T_p\). This proves (7) globally and also proves (4). Such a polynomial has no invariant direction: a nonzero invariant vector would make \(p_d\) vanish on that vector.

The following terminology follows Hörmander [H1, Definition 8.3.5].

A constant-coefficient operator is of real principal type when its degree-\(d\) principal symbol is real and

\[
 \nabla p_d(\theta)\ne0\qquad(|\theta|=1).
 \tag{8}
\]

Equivalently it suffices to impose (8) at the zeros of \(p_d\), because Euler's identity is \(\theta\cdot\nabla p_d(\theta)=d p_d(\theta)\). Lower-order coefficients need not be real for the estimates immediately below. In the real scattering theory we take the whole polynomial real.

**Proposition 2.1.** If \(p\) is of real principal type and \(d\geq2\), then

\[
 T_p(\eta)\geq c\langle\eta\rangle^{d-1},\qquad
 \frac{|\partial^\beta p(\eta)|}{T_p(\eta)}
       \leq C_\beta\langle\eta\rangle^{-1}
       \quad(|\beta|\geq2).
 \tag{9}
\]

It has no invariant direction and, when real, is simply characteristic. A polynomial of degree one is always simply characteristic, though in more than one dimension it can have invariant directions.

**Proof.** Homogeneity and the positive minimum in (8) give \(|\nabla p_d(\eta)|\geq c|\eta|^{d-1}\). The gradient of the lower-degree remainder is \(O(|\eta|^{d-2})\), so \(|\nabla p(\eta)|\geq(c/2)|\eta|^{d-1}\) at large frequencies. This and the constant derivative give the first bound in (9). A derivative of order at least two is \(O(\langle\eta\rangle^{d-2})\), proving the second.

If \(v\ne0\) were invariant, write coordinates with \(v\) as their last axis. The principal polynomial would be independent of the last coordinate. Since \(d\geq2\), all its first derivatives vanish at the vector \(v\), contrary to (8). Thus there is no invariant direction. Equation (9) and Corollary 1.3 give the remaining assertion. Alternatively, higher derivatives are bounded by a constant times \(1+|\nabla p|\), which gives (4) directly. For degree one there are no higher derivatives and (4) follows at once. \(\square\)

The derivative-ratio characterization below is also [H2, Theorem 11.1.1 and Definition 11.1.2]; its complex-zero and quantitative forms are given in [H2, Theorem 11.1.3].

For completeness, the polynomial characterization of a hypoelliptic constant-coefficient operator is

\[
 \frac{\partial^\beta p(\eta)}{p(\eta)}\longrightarrow0
       \quad(|\eta|\to\infty),\qquad \beta\ne0,
 \tag{10}
\]

where \(p\) is nonzero outside a sufficiently large ball. The statement concerns every nonzero complex polynomial in any dimension: \(p(D)u\) smooth near a point implies \(u\) smooth there for every distribution \(u\), if and only if (10) holds. Nonzero constants satisfy both assertions directly. See Hörmander [H55, Theorems 3.3, 3.4 and 3.7] for the classical characterization.

<a id="closed-graph-input"></a>
**The closed graph input.** We prove the functional-analytic statement used in the necessity argument. A nonempty complete metric space cannot be a countable union of closed sets with empty interiors. Otherwise choose nested nonempty closed balls, the \(j\)-th contained in the interior of the preceding ball and outside the \(j\)-th closed set, with radius at most \(2^{-j}\). Such a ball exists because that closed set contains no open ball. Their centres are Cauchy, and completeness gives a point in every closed ball. It lies outside every member of the asserted cover, a contradiction.

Let \(T:E\to F\) be a bounded surjective linear map of Banach spaces, and let \(B_E\) be the closed unit ball. The closed sets \(\overline{T(nB_E)}\), \(n\ge1\), cover \(F\). The preceding argument gives one with interior. Subtracting two points of a ball in that interior and taking approximating images shows that, for some \(a>0\),

\[
 B_F(0,a)\subset\overline{T(B_E)}.
\]

Indeed if \(B_F(y_0,r)\subset\overline{T(nB_E)}\), the differences of approximating vectors lie in \(2nB_E\), so one can take \(a=r/(2n)\). For a nonzero residual \(y\), rescale this inclusion to choose \(x_1\) with \(\|x_1\|\le2\|y\|/a\) and \(\|y-Tx_1\|\le\|y\|/2\). Repeat for each residual. The successive input norms are at most \(2\|y\|/(a2^{j-1})\); completeness sums them to \(x\in E\) with \(Tx=y\) and \(\|x\|\le4\|y\|/a\). A zero residual stops the construction. This is the required bounded preimage statement, including its norm control.

For an everywhere-defined linear map \(A:E\to F\) with closed graph, that graph is a Banach space in the norm \(\|(x,Ax)\|=\|x\|+\|Ax\|\): a Cauchy sequence converges componentwise and closedness keeps its limit in the graph. Its first projection onto \(E\) is bounded and bijective. The preceding preimage bound, and uniqueness of that preimage, therefore give \(\|Ax\|\le C\|x\|\). This proves the closed graph theorem used below. The free comparison is Teschl [T], Theorems 0.42 and 2.9; the argument above supplies the programme proof.

<a id="localization-hypoellipticity"></a>
**Proof of the characterization.** For \(p=c\ne0\), the operator is multiplication by \(c\) and every positive-order derivative of \(p\) vanishes, proving both assertions. Now let \(p\) be nonconstant and first suppose \(p(D)\) is hypoelliptic. Let \(U\) be its distributional null space in \(L^2(\Omega)\), for a bounded ball \(\Omega\), and choose a smaller ball \(\Omega'\) with compact closure in \(\Omega\). The null space is closed because \(p(D)\) is continuous from \(L^2\) into distributions. Hypoellipticity makes every member of \(U\) smooth. The map
\(u\mapsto\nabla u:U\to L^2(\Omega')^n\) has closed graph: both its input limit and derivative limit give the same distributional derivative. The closed graph theorem gives
\[
\|\nabla u\|_{L^2(\Omega')}\leq C\|u\|_{L^2(\Omega)},\qquad u\in U.
\]
For any complex zero \(\zeta\) of \(p\), use \(u(x)=e^{ix\cdot\zeta}\). When \(|\operatorname{Im}\zeta|\leq A\), the exponential's absolute value is bounded above and below on these two fixed balls by positive constants depending only on \(A\). The estimate therefore bounds \(|\zeta|\) by a constant depending on \(A\). In particular the distance
\[
d(\eta)=\operatorname{dist}(\eta,\{\zeta\in\mathbb C^n:p(\zeta)=0\})
\]
from a real \(\eta\) to the complex zero set tends to infinity as \(|\eta|\to\infty\). If it did not, nearby zeros would have bounded imaginary parts and unbounded real parts. It also gives eventual nonvanishing on the real domain.

For a fixed real vector \(h\), factor the one-variable polynomial \(t\mapsto p(\eta+th)\). Each of its roots has absolute value at least \(d(\eta)/|h|\). Dividing its factorization at \(t=1\) by that at \(t=0\) proves
\(p(\eta+h)/p(\eta)\to1\); the number of factors is bounded by \(\deg p\), and a constant restriction gives the same assertion. Every fixed polynomial derivative is a finite linear combination of real translates. To see this with coefficients independent of \(\eta\), interpolate \(\theta\mapsto p(\eta+\theta)\) on a tensor grid of \(\deg p+1\) points in each coordinate and differentiate its finite Lagrange interpolation formula at zero. For a nonzero derivative the coefficients sum to zero, because differentiation kills the constant polynomial. The translate ratios consequently give (10). This proves the necessary direction with no real-coefficient restriction.

Conversely, assume (10), and let \(p\) be nonconstant. A highest-order nonzero derivative is a nonzero constant, so (10) implies \(|p(\eta)|\to\infty\). The finite Taylor expansion shows
\[
\frac{p(\eta+z)}{p(\eta)}\longrightarrow1
\quad\text{uniformly for }|z|\leq A
\]
for every fixed complex ball. Hence \(d(\eta)\to\infty\). The lineality space is zero: along a nonzero invariant real direction, both \(p\) and its nonzero highest derivative would remain constant, contradicting their vanishing ratio.

The required quantitative algebraic input is now proved in [Quantitative polynomial growth and a smooth Fourier parametrix, (Q1)–(Q5)](../providers/analysis/quantitative-polynomial-growth.md#the-radial-minimum-and-its-positive-power): for some \(c>0\) and \(0<\delta\leq1\),
\[
d(\eta)\geq c\langle\eta\rangle^\delta
\quad\text{at sufficiently large real }|\eta|.
\]
Here is the full route to this bound. Regard the complex zero set as the two real polynomial equations \(\operatorname{Re}p(a+ib)=\operatorname{Im}p(a+ib)=0\). The graph of its distance is specified by existence of a point at that distance and absence of any closer point. The proved Boolean and projection theorems in the linked free preparation treatment make that graph globally subanalytic. The minimum \(\rho(r)=\min_{|\eta|=r}d(\eta)\) exists by compactness and is definable by the same finite quantified formulas. Since \(d(\eta)\to\infty\), \(\rho(r)\to\infty\). Apply the treatment's proved convergent one-variable Puiseux theorem to \(\rho(1/t)\). Its lowest nonzero exponent is negative, with positive coefficient, so convergence gives \(\rho(r)\geq c r^\delta\) for a positive \(\delta\), reduced to at most one if necessary. Taking the spherical minimum controls every real direction. The real polynomial coefficients in this argument are unrestricted, and the coefficients of \(p\) may be complex.

Choose a smooth frequency cutoff \(\chi\) equal to one on a ball containing all real zeros and supported in a larger ball where the preceding bound is valid outside it. Put
\(m=(1-\chi)/p\), extended smoothly by zero in the inner ball. Reciprocal derivatives satisfy
\[
|\partial^\alpha m(\eta)|\leq C_\alpha
 \langle\eta\rangle^{-\delta|\alpha|}
\quad\text{outside a fixed ball}.
\]
To check every mixed derivative, factor \(p(\eta+tv)/p(\eta)=\prod_j(1-t/\tau_j)\) for any fixed real direction \(v\); every root has \(|\tau_j|\geq d(\eta)/|v|\). Expanding the reciprocal product in geometric series bounds its derivative of order \(\ell\) by
\(C_\ell |p(\eta)|^{-1}|v|^\ell d(\eta)^{-\ell}\).
The finite polarization identity converts these diagonal derivative bounds into
\(C_\alpha |p(\eta)|^{-1}d(\eta)^{-|\alpha|}\)
for each mixed derivative; the complete coefficient and polarization calculations are [(Q6)–(Q9) in the provider](../providers/analysis/quantitative-polynomial-growth.md#all-polynomial-and-reciprocal-derivatives). Constant or lower-degree restrictions cause no difficulty. Now use \(|p(\eta)|\geq1\) and the quantitative distance bound. Derivatives of \(\chi\) have compact support.

With the stated unitary Fourier transform define
\[
E_0=(2\pi)^{-n/2}\mathcal F^{-1}m,\qquad
r=(2\pi)^{-n/2}\mathcal F^{-1}\chi.
\]
Then \(p(D)E_0=\delta_0-r\), and \(r\) is a Schwartz function. The distribution \(E_0\) is smooth away from zero. For every prescribed derivative \(\partial_x^\beta\), first multiply its Fourier integrand by a compact smooth cutoff \(\vartheta(\eta/L)\), one for \(|\eta|\leq L\) and zero for \(|\eta|\geq2L\). Integrate by parts \(N\) times using \((x/(i|x|^2))\cdot\partial_\eta\). The differentiated multiplier has order at most \(|\beta|-\delta N\): Leibniz terms putting derivatives on \(\eta^\beta\) improve this estimate because \(\delta\leq1\). Choose \(\delta N>|\beta|+n\). The main integral then converges absolutely. A term with \(j\geq1\) derivatives on the expanding cutoff has integral bounded by
\(C L^{n+|\beta|-\delta N-(1-\delta)j}\to0\).
All limits are uniform on compact sets with \(x\ne0\), and the cut off inverse transforms also converge as tempered distributions. Applying this to each finite list of spatial derivatives proves smoothness; [(Q10)–(Q14) in the provider](../providers/analysis/quantitative-polynomial-growth.md#the-cutoff-and-the-fourier-boundary-terms) give the complete boundary calculation. 

The provider's [Distributional localization, (Q15)–(Q19)](../providers/analysis/quantitative-polynomial-growth.md#distributional-localization) proves the finite-order bounds, convolution with a compactly supported distribution, derivative transfer and separated-support smoothing used in the last step. Finally let \(p(D)u=f\) be smooth near \(x_0\), with \(u\) an arbitrary distribution. Choose \(\psi\in C_c^\infty\) supported where \(f\) is smooth and equal to one on a neighborhood of \(x_0\). Extend \(v=\psi u\) by zero. Convolution of the compactly supported \(v\) with the parametrix identity gives
\[
v=E_0*(\psi f)+E_0*([p(D),\psi]u)+r*v.
\]
The first term is smooth because \(\psi f\) is a compactly supported smooth function. The commutator is a compactly supported distribution whose support is separated from \(x_0\); smoothness of \(E_0\) off zero makes its convolution smooth near \(x_0\). The last term is smooth because \(r\) is smooth and \(v\) has compact support. Hence \(u\) is smooth near \(x_0\). This supplies the inhomogeneous arbitrary-distribution conclusion without an \(L^2\) restriction. Together with the proved growth input and the constant case it proves the stated full equivalence. \(\square\)

The consequences needed to compare the polynomial classes are elementary: (10) immediately gives \(T_p/|p|\to1\), so every real polynomial satisfying (10) satisfies (4). If it is nonconstant, the highest-derivative argument above excludes invariant directions. The elliptic and real-principal-type coefficient theorem below is proved from (7)–(9), independently of the quantitative algebraic input. We do not infer an isotropic Sobolev gain from hypoellipticity alone.

The compact-support estimate of Lemma 1.1 in [Short-range compactness and local tests](short-range-compactness-and-local-tests.md) says

\[
 \|T_p(D)w\|_2\leq C_{p,Q}\|p(D)w\|_2,\qquad
                      w\in C_c^\infty(Q).
 \tag{11}
\]

Here the left side is the square sum of all polynomial-derivative norms, by Plancherel. Combining (7) or (9) with (11) proves the graph bound we need.

<a id="localization-supported-gain"></a>
**Corollary 2.2.** Let \(m\geq1\), and suppose \(p\) is either elliptic of order \(m\), or of real principal type of order \(m+1\). On every fixed ball \(Q\),

\[
 \|w\|_{H^m(\mathbb R^n)}
       \leq C_{p,Q}\|p(D)w\|_2,\qquad w\in C_c^\infty(Q).
 \tag{12}
\]

The constant is unchanged by translating the ball in physical space.

**Proof.** In either case \(T_p(\eta)\geq c\langle\eta\rangle^m\). Apply Plancherel and (11). Translation commutes with \(p(D)\) and preserves the Sobolev norm. \(\square\)

The support restriction in (12) allows a real-principal-type operator to control \(m\) derivatives despite its characteristic cone. Its differential order is \(m+1\); that does not supply \(m+1\) isotropic derivatives.

<a id="localization-sobolev"></a>
## 3. The exact local Sobolev estimates

Let \(Q=B(0,1)\) and let \(k\geq1\) be an integer. The estimates needed for coefficient multiplication are

\[
 \|w\|_{L^q(Q)}\leq C\|w\|_{H^k(\mathbb R^n)},\qquad
 w\in C_c^\infty(Q),
 \quad
 \begin{cases}
 q=2n/(n-2k),&n>2k,\\
 \text{any fixed }2<q<\infty,&n=2k,\\
 q=\infty,&n<2k.
 \end{cases}
 \tag{13}
\]

Here is a direct construction, including odd values of \(k\). Take the homogeneous elliptic polynomial \(q_0(\xi)=|\xi|^{2k}\), and a smooth compact low-frequency cutoff \(\chi\) equal to one near zero. Its regularized inverse symbol is \(b_0=(1-\chi)/q_0\). For our unitary Fourier transform put \(F_0=(2\pi)^{-n/2}\mathcal F^{-1}b_0\), so \(b_0(D)f=F_0*f\). The multinomial identity gives

\[
 w=\chi(D)w+
       \sum_{|\beta|=k}\frac{k!}{\beta!}
          (D^\beta F_0)*D^\beta w.
 \tag{14}
\]

This is an exact Fourier identity: the sum of the symbols in its second term is
\((1-\chi)|\xi|^{-2k}\sum_{|\beta|=k}(k!/\beta!)\xi^{2\beta}=1-\chi\).
It requires only \(k\) derivatives of the input.

The multiplier for \(D^\beta F_0\) is
\((1-\chi)\xi^\beta/|\xi|^{2k}\), of order \(-k\). Split it into smooth dyadic annuli of frequency size \(2^j\), \(j\geq0\), absorbing finitely many low annuli in the first term. Rescale each annulus to a fixed compact annulus. Differentiating its symbol there gives uniform bounds times \(2^{-jk}\); integration by parts in the Fourier integral therefore bounds its convolution kernel \(K_j\) by
\[
|K_j(x)|\leq C_N2^{j(n-k)}(1+2^j|x|)^{-N}
\]
for every \(N\). In particular \(\|K_j\|_1\leq C2^{-jk}\) when \(N>n\), so their sum converges in \(L^1\) and is the actual convolution kernel. For \(0<|x|\leq1\), split the sum at \(2^j|x|=1\). Summing its geometric bounds gives
\[
|D^\beta F_0(x)|\leq C
\begin{cases}
|x|^{k-n},&k<n,\\
1+|\log|x||,&k=n,\\
1,&k>n.
\end{cases}
\]
For \(|x|\geq1\), summing with arbitrarily large \(N\) gives rapid decay. This proves all the kernel bounds used here from smooth compact-frequency Fourier integrals.

<a id="localization-fractional-endpoint"></a>
For the finite endpoint \(n>2k\), these bounds imply
\(|D^\beta F_0(x)|\leq C|x|^{k-n}\) on all of \(\mathbb R^n\setminus0\). We give the required fractional-integration estimate at input exponent two. Let \(Mf\) denote the supremum of the centered ball averages of \(|f|\). We supply the precise maximal estimate. For an integrable \(g\), each fixed-radius average is continuous in the center: its change is at most the \(L^1\) translation difference divided by the ball volume, which tends to zero by the proved approximation reading. Thus \(\{Mg>a\}\) is open.

Take a compact subset of this open set. At each of its points choose a ball centered there with average greater than \(a\). Finitely many such balls cover the compact set. Select a largest-radius ball, discard all balls meeting it, and repeat in the finite remaining list. The selected balls are disjoint. Every discarded ball meets a selected ball of at least its radius and is contained in that selected ball's threefold dilation. Therefore the compact set has measure at most
\[
 3^n\sum_j|B_j|\le\frac{3^n}{a}\sum_j\int_{B_j}|g|
       \le\frac{3^n}{a}\|g\|_1.
\]
Exhaust the open level set by its intersections with large closed balls at distance at least \(1/j\) from its complement. Monotone convergence of their measures proves the weak \(L^1\) estimate on the entire level set. This is a finite-ball proof of the required covering assertion.

Now let \(f\in L^2\). Its fixed-radius averages are locally continuous by the same argument after a compact cutoff, so \(Mf\) is measurable. For each \(a>0\), the function \(g_a=f\mathbf1_{\{|f|>a/2\}}\) belongs to \(L^1\), since its integral is at most \(2a^{-1}\|f\|_2^2\). The complementary part is bounded by \(a/2\). Subadditivity of ball averages gives
\[
 |\{Mf>a\}|\le |\{Mg_a>a/2\}|
       \le\frac{2\,3^n}{a}\int_{|f|>a/2}|f(x)|\,dx.
\]
The pointwise identity \(b^2=\int_0^b2a\,da\), followed by nonnegative product interchange, is the layer-cake formula. It and the last estimate give
\[
 \|Mf\|_2^2
 =2\int_0^\infty a|\{Mf>a\}|\,da
 \le4\,3^n\int_0^\infty\int_{|f|>a/2}|f(x)|\,dx\,da
 =8\,3^n\|f\|_2^2.
\]
This argument proves finiteness as well as the bound; it does not assume in advance that the maximal function is in \(L^2\).

Split convolution with \(|x|^{k-n}\) at radius \(R\). Summing balls of radii \(2^{-j}R\) bounds the near part by \(C R^k Mf(x)\). Cauchy–Schwarz bounds the far part by
\(C R^{k-n/2}\|f\|_2\), because \(2k<n\). Choosing
\(R=(\|f\|_2/Mf(x))^{2/n}\) proves
\[
\int |x-y|^{k-n}|f(y)|\,dy
 \leq C\|f\|_2^{2k/n}(Mf(x))^{1-2k/n}.
\]
The zero function is handled separately. If \(Mf(x)=0\) at any point, the integral of \(|f|\) over every ball centered there vanishes; their union is \(\mathbb R^n\), so \(f=0\) almost everywhere. For nonzero \(f\), therefore, \(0<Mf(x)<\infty\) almost everywhere, which justifies the chosen radius. Raise this inequality to
\(q=2n/(n-2k)\); its maximal-function exponent is exactly two. Integration proves the endpoint convolution bound \(L^2\to L^q\). Apply it to each \(D^\beta w\) in (14). This proves the finite endpoint in (13).

At \(n=2k\), choose any fixed finite \(q>2\). The kernel restricted to \(B(0,2)\) belongs to \(L^r\) when \(1/r=1/2+1/q\), because this \(r\) is strictly less than \(2=n/(n-k)\). Young's inequality applies to the zero extension of \(D^\beta w\), and all differences of input and output points in \(Q\) lie in that restricted ball. At \(n<2k\), the same restricted kernel belongs to \(L^2\): the power singularity is square integrable when \(k>n/2\), and the logarithmic or bounded cases satisfy this as well. Cauchy–Schwarz gives the \(L^\infty(Q)\) bound.

Finally the smooth low-frequency term is bounded in \(L^\infty\) by \(C\|w\|_2\), since its inverse Fourier kernel is in \(L^2\). On \(Q\) this also bounds each finite \(L^q\) norm. Summing (14) proves (13). By completion it holds for all \(H^k\) functions supported in the closure of \(Q\) that are limits of compact smooth tests.

<a id="localization-multiplication"></a>
For \(|\alpha|<m\), set \(k=m-|\alpha|\). Apply (13) to \(w=D^\alpha u\), and use (12). The finitely many derivatives of \(D^\alpha u\) of order at most \(k\) have norms controlled by \(\|u\|_{H^m}\). We obtain

\[
 \|D^\alpha u\|_{L^{q_\alpha}(Q)}
       \leq C\|p(D)u\|_2,\qquad u\in C_c^\infty(Q).
 \tag{15}
\]

Choose the coefficient exponent \(r_\alpha\) and its partner \(q_\alpha\) according to the gap \(k=m-|\alpha|\):

- If \(n>2k\), take \(r_\alpha=n/k\) and \(q_\alpha=2n/(n-2k)\).
- If \(n=2k\), choose any fixed finite \(r_\alpha>2\) and take \(q_\alpha=2r_\alpha/(r_\alpha-2)\).
- If \(n<2k\), take \(r_\alpha=2\) and \(q_\alpha=\infty\).

In every case \(1/2=1/r_\alpha+1/q_\alpha\). Hölder and (15) therefore give

\[
 \|aD^\alpha u\|_{L^2(Q)}
       \leq C\|a\|_{L^{r_\alpha}(Q)}\|p(D)u\|_2.
 \tag{16}
\]

The strict coefficient exponent in the critical case is essential. The critical case gives all finite derivative exponents and supplies no \(L^\infty\) endpoint. The complete free [critical multiplication provider](../providers/analysis/critical-multiplication.md#critical-multiplication) constructs compactly supported \(a\in L^2(\mathbb R^2)\) and \(w\in H^1(\mathbb R^2)\) with \(aw\notin L^2\), including the weak derivative across the puncture. If a critical coefficient is locally \(L^\infty\) and satisfies the analogous shell sum of essential suprema, it also satisfies (18) for every fixed finite \(r_\alpha>2\), by the finite volume of the unit ball.

<a id="localization-rough-coefficients"></a>
## 4. Rough coefficients with summable local norms

Use the shells and radii from [Endpoint spaces and flat energy shells](endpoint-spaces-and-flat-energy-shells.md):
\(A_0=\{|x|<1\}\), \(A_j=\{2^{j-1}\leq|x|<2^j\}\) for \(j\geq1\), and \(R_j=2^j\). Recall

\[
 X_p=\{u:(\partial^\beta p)(D)u\in B^*
                         \text{ for every }\beta\},\qquad
 \|u\|_{X_p}=\sum_\beta\|(\partial^\beta p)(D)u\|_{B^*}.
\]

The three coefficient exponents and the summable shell condition below are those of Hörmander [H2, (14.4.6), pp. 246–247].

**Theorem 4.1.** Let \(p\) be elliptic of order \(m\geq1\), or of real principal type of order \(m+1\). Let

\[
 V(x,D)=\sum_{|\alpha|<m}a_\alpha(x)D^\alpha,
 \qquad a_\alpha\in L^{r_\alpha}_{\rm loc}(\mathbb R^n),
 \tag{17}
\]

with exponents from the three cases above. For each coefficient assume

\[
 S_\alpha=
   \sum_{j\geq0}R_j
      \sup_{y\in A_j}
         \left(\int_{|x|<1}|a_\alpha(x+y)|^{r_\alpha}\,dx\right)^{1/r_\alpha}
       <\infty.
 \tag{18}
\]

Then the coefficient-product action on smooth members of \(X_p\) has a unique compact extension \(X_p\to B\), with
\(\|V\|_{X_p\to B}\leq C_p\sum_\alpha S_\alpha\).
This extension is the local coefficient-product action on every \(u\in X_p\).

**Proof: local size.** All \(r_\alpha\geq2\), so each coefficient is locally \(L^2\). For \(u\in C_c^\infty(Q)\), (16) gives

\[
 \|V(x+y,D)u\|_2
       \leq C\sum_{|\alpha|<m}
             \|a_\alpha(\,\cdot+y)\|_{L^{r_\alpha}(Q)}
                       \|p(D)u\|_2.
 \tag{19}
\]

Thus the local operator norm \(M_j\) in Theorem 3.1 of the compactness lesson is bounded by the sum of these shell suprema. Equation (18) proves \(\sum_jR_jM_j<\infty\).

**Proof: fixed-location compactness.** Fix a physical centre \(y\) and one multi-index \(\alpha\). The image of the local unit graph ball under \(D^\alpha\) is precompact in \(L^2(Q)\). To check this directly, (12) bounds its \(H^k\) norm, with \(k=m-|\alpha|\geq1\). Its Fourier tail outside radius \(L\) has squared mass at most \(C L^{-2k}\). Inside that radius, the truncated operator on \(L^2(Q)\) has kernel
\[
 {\bf1}_Q(x){\bf1}_Q(z)(2\pi)^{-n}
       \int_{|\xi|\le L}e^{i(x-z)\cdot\xi}\,d\xi.
\]
Its absolute value is at most \((2\pi)^{-n}|B(0,L)|\), so it is square integrable on \(Q\times Q\). The [finite-kernel argument in the compactness lesson](short-range-compactness-and-local-tests.md#short-range-strength-ratio) approximates it in \(L^2(Q\times Q)\) by finite sums of product indicators. These give finite-rank operators; Cauchy–Schwarz bounds the operator-norm error by the kernel's \(L^2\) error. Thus the truncation is compact. The high-frequency error is uniformly small, proving precompactness. This is also the strict-strength criterion in Proposition 5.1 of the compactness lesson.

Write \(a=a_\alpha(\,\cdot+y)\) on \(Q\), and truncate it:

\[
 a^{(s)}=a\,\mathbf1_{\{|a|\leq s\}},\qquad
             \|a-a^{(s)}\|_{r_\alpha}\longrightarrow0.
 \tag{20}
\]

The norm limit follows from dominated convergence in the finite exponent \(r_\alpha\). Multiplication by the bounded \(a^{(s)}\) preserves the precompact \(D^\alpha\) image. Equation (16) makes its difference from \(aD^\alpha\) uniformly small on the unit graph ball. A uniform limit of these precompact images is precompact: for a prescribed error, choose \(s\) making the error small and use a finite net for the truncated image. A finite sum preserves precompactness. This proves the fixed-\(y\) condition of the compactness theorem. No uniform truncation limit in all physical centres is required.

Theorem 3.1 of the linked compactness lesson now gives the unique compact extension and its stated norm. Its Lemma 2.1 proves density of smooth members of \(X_p\) by locally varying mollification radii. This is the density used for uniqueness; compact smooth functions need not be norm dense in this endpoint graph space.

**Proof: interpretation on the graph space.** Choose a smooth cutoff \(\phi\) supported inside a fixed ball. Polynomial Leibniz's rule expresses every derivative component of \(\phi u\) as a finite sum of bounded cutoff derivatives times the local \(L^2\) graph components of \(u\). Thus \(\phi u\) belongs to the compact graph completion used in that lesson. Equation (12), by mollification of those components, puts \(\phi u\) in \(H^m\). Hence \(u\in H^m_{\rm loc}\), and (13) makes each coefficient product \(a_\alpha D^\alpha u\) locally \(L^2\).

Smooth graph approximation on that fixed ball converges in \(H^m\), then in the relevant \(L^{q_\alpha}\) derivative norm by (13). Hölder shows convergence of its coefficient products in \(L^2\). Their limit is precisely the pointwise product with the weak derivative of \(u\). The global extension was obtained by the same local graph approximation and summable shell bounds, so it agrees with these products on each compact set. \(\square\)

For a real \(p\) and a symmetric \(V\), the free hypotheses for the full short-range theory are now available: elliptic positive-order polynomials and real-principal-type polynomials of order at least two are simply characteristic and have no invariant direction. [Self-adjoint short-range operators](self-adjoint-short-range-operators.md) gives the self-adjoint closure, and the subsequent resolvent and scattering lessons apply. Symmetry is an additional hypothesis on the differential operator; real coefficients on a differentiated term do not automatically imply it.

<a id="localization-examples"></a>
## 5. Examples with singularities and concentration

**Example 5.1: an isolated singularity.** For one term with gap \(k\), let \(r\) be its coefficient exponent from Section 3. Take a smooth cutoff \(\chi\), equal to one near zero and supported in a fixed ball, and put

\[
 a(x)=\chi(x)|x|^{-\gamma}
             +(1-\chi(x))(1+|x|)^{-1-\delta},
 \qquad \delta>0,\quad 0<\gamma<n/r.
 \tag{21}
\]

Its local singularity is in \(L^r\), since its radial integral is a constant times
\(\int_0^\varepsilon t^{n-1-\gamma r}\,dt<\infty\).
On each sufficiently distant translated unit ball the \(L^r\) norm is at most \(C R_j^{-1-\delta}\). The finite central shell suprema are bounded by the \(L^r\) norm on a fixed larger ball. Thus (18) holds. For \(n>2k\), the condition is \(\gamma<k\). For \(n=2k\) one must choose \(r>2\), so it is \(\gamma<n/r<k\). For \(n<2k\), it is \(\gamma<n/2\).

**Example 5.2: the same four derivatives from different operators.** In dimension eight, compare the elliptic polynomial \(p(\xi)=|\xi|^4\) with

\[
 p(\xi)=\xi_1^5+\cdots+\xi_8^5.
 \tag{22}
\]

For (22), the principal gradient is \((5\xi_1^4,\ldots,5\xi_8^4)\), nonzero at every nonzero vector, so it is of real principal type. Both operators satisfy (12) with \(m=4\). Their permissible derivative orders are \(0,1,2,3\); the coefficient exponents, in that order, are any fixed \(r_0>2\), \(8/3\), \(4\), and \(8\). Each coefficient must also satisfy (18). The fifth-order operator has a nontrivial characteristic cone and is covered by this criterion without an ellipticity assumption.

**Example 5.3: high peaks at large distances.** In \(\mathbb R^5\) take \(p(\xi)=|\xi|^2\), \(m=2\), and a nonnegative nonzero smooth bump \(\varphi\) supported in \(B(0,1/8)\), with \(\varphi(0)>0\). Define

\[
 x_\ell=4^\ell e_1,\quad \varepsilon_\ell=e^{-\ell^2},\quad
 c_\ell=4^{-\ell}\ell^{-2},\qquad
 a(x)=\sum_{\ell\geq1}c_\ell\varepsilon_\ell^{-2}
                    \varphi((x-x_\ell)/\varepsilon_\ell).
 \tag{23}
\]

The supports are disjoint and locally finite, so \(a\) is a nonnegative smooth function. The gap is \(k=2\), and its coefficient exponent is \(r=5/2\). Scaling cancels the concentrating radius:

\[
 \|c_\ell\varepsilon_\ell^{-2}
             \varphi((\,\cdot-x_\ell)/\varepsilon_\ell)\|_{5/2}
       =c_\ell\|\varphi\|_{5/2}.
 \tag{24}
\]

A translated unit ball meets at most one bump. Its centre then lies within two units of \(x_\ell\), so only a fixed number of shells with \(R_j\asymp4^\ell\) can contribute. Consequently (18) is bounded by
\(C\sum_\ell4^\ell c_\ell=C\sum_\ell\ell^{-2}<\infty\).
The multiplication operator is short range. Nevertheless
\(a(x_\ell)=4^{-\ell}\ell^{-2}e^{2\ell^2}\varphi(0)\to\infty\).
Uniform pointwise decay would exclude this example.

### Use the conclusion

Work the high-peak example using the actual local exponent, then check the critical dimension. Keep the exact polynomial weakness condition and the local compactness argument before declaring the coefficient short range.

<a id="localization-exercises"></a>
## 6. Exercises

**Exercise 6.1 (foundation).** Let \(p(\xi_1,\xi_2)=\xi_1-\xi_2^2\). Find the localization limits along \(\eta=(t^2,t)\) as \(t\to+\infty\) and \(t\to-\infty\), and along \(\eta=(t,0)\) as \(t\to+\infty\). Show that every localization has degree at most one. Explain why this polynomial is simply characteristic although its principal homogeneous part does not satisfy (8).

**Exercise 6.2 (intermediate).** On \(\mathbb R^2\), take \(p(\xi)=\xi_1^5+\xi_2^5\) and \(Q(\xi)=\xi_1^4\). Show that \(Q\) is weaker than \(p\), but its strength ratio does not tend to zero. Use a nonzero compact smooth test to show that adding a bounded smooth compact coefficient to this fourth-order term can fail the local compactness condition. State the derivative orders that Theorem 4.1 does permit.

**Exercise 6.3 (intermediate).** In dimension five let \(a(x)=|x|^{-\gamma}\) on the unit ball, \(0<\gamma<1\), and \(r=5\). Compute \(\|a\mathbf1_{\{|a|>s\}}\|_5\) for \(s\geq1\), including its decay exponent in \(s\). Apply the result to a first-order term relative to the elliptic polynomial \(|\xi|^2\).

**Exercise 6.4 (advanced).** Verify every part of the short-range criterion for (23). Then replace \(c_\ell\) by \(4^{-\ell}/\ell\). Determine whether the sufficient sum (18) converges. Explain why its failure alone is not a necessity test, and determine the actual short-range behavior by testing a rescaled bump.

**Exercise 6.5 (advanced).** Use the real potential (23) in \(H=-\Delta+a\) on \(\mathbb R^5\). State the self-adjointness, wave-operator, spectral and scattering-matrix conclusions supplied by the earlier lessons. Identify the free critical energy and the measure on a positive-energy sphere. Check whether the quadratic uniqueness theorem's pointwise potential bound applies.

<a id="localization-solutions"></a>
## 7. Complete solutions

**Solution 6.1.** The exact strength is
\(T_p(a,b)^2=(a-b^2)^2+4b^2+5\).
Along \((t^2,t)\), the normalized polynomial is

\[
 \frac{\xi_1-2t\xi_2-\xi_2^2}{\sqrt{4t^2+5}}.
\]

Its limits are \(-\xi_2\) for positive \(t\) and \(+\xi_2\) for negative \(t\). Along \((t,0)\), it is
\((t+\xi_1-\xi_2^2)/\sqrt{t^2+5}\to1\).
The only nonzero second derivative is the constant \(-2\). Strength properness makes its normalized value tend to zero along every escaping sequence, so all localization limits are affine. Corollary 1.3 applies. The principal part is \(-\xi_2^2\), whose gradient vanishes at the nonzero vector \((1,0)\); real principal type is sufficient, not necessary, for simple characteristics.

**Solution 6.2.** The gradient \((5\xi_1^4,5\xi_2^4)\) bounds \(T_p\) below by \(c\langle\xi\rangle^4\). Every derivative of \(Q\) has degree at most four, so \(T_Q/T_p\) is bounded. Along \(\eta_t=(t,-t)\),
\(p(\eta_t)=0\), \(T_p(\eta_t)=5\sqrt2\,t^4(1+O(t^{-2}))\), and \(T_Q(\eta_t)=t^4(1+O(t^{-2}))\). The ratio tends to \(1/(5\sqrt2)\).

Choose nonzero \(\psi\in C_c^\infty(Q_0)\) in a ball \(Q_0\) strictly inside the unit ball, and a smooth compact coefficient \(b\) equal to one near \(\overline{Q_0}\). The functions \(u_t=e^{i\eta_t\cdot x}\psi/T_p(\eta_t)\) have bounded compact \(p(D)\) norms by Taylor expansion. Moreover

\[
 bQ(D)u_t=e^{i\eta_t\cdot x}
       \left(\frac{\psi}{5\sqrt2}+o_{L^2}(1)\right).
\]

Their norms stay positive, whereas the sequence converges weakly to zero: each compact profile paired with an \(L^2\) test is an \(L^1\) oscillatory integral, and the Riemann–Lebesgue lemma applies. Therefore the image is not precompact. Rescaling the bounded inputs by one common constant places them in the local unit graph ball without changing this obstruction. Here \(m=4\), so Theorem 4.1 permits orders at most three. A fourth-order coefficient needs a separate analysis.

**Solution 6.3.** The set \(\{|a|>s\}\) is \(\{|x|<s^{-1/\gamma}\}\), up to a null boundary. With \(\sigma_4\) the area of the unit four-sphere,

\[
 \|a\mathbf1_{\{|a|>s\}}\|_5^5
       =\frac{\sigma_4}{5-5\gamma}
                    s^{-(5-5\gamma)/\gamma},
 \qquad
 \|a\mathbf1_{\{|a|>s\}}\|_5
       =\left(\frac{\sigma_4}{5-5\gamma}\right)^{1/5}
                    s^{1-1/\gamma}.
\]

The exponent is negative precisely because \(\gamma<1\). For an order-one derivative relative to \(p=|\xi|^2\), \(m=2\) and \(k=1\), Section 3 gives \(r=5\), \(q=10/3\). Equation (16) makes the norm of the discarded multiplication-derivative operator at most a constant times this tail norm. Thus the truncations converge in operator norm on the compact graph ball. With a compactly supported coefficient, the global sum (18) has only finitely many contributing shells.

**Solution 6.4.** Every compact set meets finitely many bump supports, so \(a\in L^{5/2}_{\rm loc}\subset L^2_{\rm loc}\). Each translated unit ball meets at most one support because neighbouring centres are separated by at least twelve units. Its \(L^{5/2}\) norm is at most (24), while centres whose unit ball meets that support lie within \(1+\varepsilon_\ell/8<2\) of \(x_\ell\). A bounded number of dyadic shell indices occur, all with \(R_j\) comparable to \(4^\ell\). Summing their contributions gives (18) by \(\sum\ell^{-2}<\infty\). At each fixed centre the finite-exponent coefficient truncation tends to zero in norm; the bounded part is compact by the derivative-gap proof. These are both conditions of the exact compactness criterion.

For the changed coefficients the sufficient sum diverges. Indeed take \(y=x_\ell\), which lies in \(A_{2\ell+1}\), and the entire bump lies in the translated unit ball. Thus the term with \(j=2\ell+1\) is at least
\(2\cdot4^\ell c_\ell\|\varphi\|_{5/2}=2\|\varphi\|_{5/2}/\ell\).
Failure of (18) alone does not prove failure of short range: (18) bounds the actual local operator norms from above, whereas necessity in the exact criterion concerns the actual \(M_j\). Here we can supply the needed lower bound. Choose \(w\in C_c^\infty(B(0,1/8))\) with \(\varphi w\ne0\), and put

\[
 w_\ell(x)=\varepsilon_\ell^{-1/2}w(x/\varepsilon_\ell).
\]

In dimension five, scaling gives \(\|\Delta w_\ell\|_2=\|\Delta w\|_2>0\) and
\[
 \|a(x+x_\ell)w_\ell(x)\|_2=c_\ell\|\varphi w\|_2.
\]

Only the bump at \(x_\ell\) meets this test. Normalize by \(\|\Delta w\|_2\). Then \(M_{2\ell+1}\geq c_\ell\|\varphi w\|_2/\|\Delta w\|_2\), and the necessary sum of actual norms is bounded below by a positive multiple of \(\sum_\ell1/\ell\). The changed potential is not short range. This conclusion uses the additional operator lower bound.

**Solution 6.5.** Theorem 4.1 makes real multiplication by \(a\) compact \(X_{|\xi|^2}\to B\). It is symmetric on compact smooth functions. The polynomial is real, elliptic, simply characteristic, and has no invariant direction. The self-adjoint lesson therefore gives the self-adjoint closure of the Schwartz restriction. The wave-operator and completeness lessons give both \(W_\pm\), their isometry on the free \(L^2\) space, and their common range \(H_{\rm ac}(H)\). The spectral lesson gives absence of singular continuous spectrum; the orthogonal complement of that range is spanned by eigenfunctions.

The only critical value of \(|\xi|^2\) is zero. For each positive \(\lambda\), \(M_\lambda=\{|\xi|=\sqrt\lambda\}\) has \(g=|\nabla p|=2\sqrt\lambda\), and its energy measure is \(dS/(2\sqrt\lambda)\). The regular-energy scattering lesson gives a unitary \(S(\lambda)\) in that space, with \(S(\lambda)-I\) compact, including the exceptional regular eigenvalues dealt with there. Since \(g\) is constant on this sphere, the weighted spaces in that lesson differ only by constant norm factors.

Finally \(|x_\ell|a(x_\ell)=\ell^{-2}e^{2\ell^2}\varphi(0)\to\infty\). Thus no bound \(|a(x)|\leq C/|x|\) can hold. The Laplacian uniqueness theorem in the quadratic lesson does not apply to this potential, so these hypotheses alone do not give its conclusion that regular positive eigenvalues are absent. \(\square\)

## References

- [H55] Lars Hörmander, “On the theory of general partial differential operators,” *Acta Mathematica* 94 (1955), 161–248. Lemmas 3.7–3.10 and Theorems 3.3, 3.4 and 3.7. [Original full article](https://projecteuclid.org/journalArticle/Download?urlid=10.1007%2FBF02392492).
- [Quantitative polynomial growth and a smooth Fourier parametrix](../providers/analysis/quantitative-polynomial-growth.md). Radial minimum, convergent Puiseux, reciprocal derivative and cutoff arguments (Q1)–(Q14), followed by the distributional convolution and localization proofs (Q15)–(Q19). Its reading order includes the analytic foundations supplement and exact programme preparation proof with their source credits and terms.
- [The critical two-dimensional multiplication obstruction](../providers/analysis/critical-multiplication.md#critical-multiplication). Complete compactly supported counterexample at the excluded critical endpoint.
- [HW] Lars Hörmander, “The existence of wave operators in scattering theory,” *Mathematische Zeitschrift* 146 (1976), 69–91. Section 2, Theorem 2.1 and its complete argument on printed pp. 70–72. [Freely accessible GDZ scan](https://gdz.sub.uni-goettingen.de/download/pdf/PPN266833020_0146/LOG_0012.pdf).

- Terence Tao, *Lecture Notes 2 for 247A*, UCLA, fall 2006, Section 6, Proposition 6.1 and Corollary 6.3. [Open notes](https://www.math.ucla.edu/~tao/247a.1.06f/notes2.pdf).
- [T] Gerald Teschl, *Mathematical Methods in Quantum Mechanics*, second edition, 2014, Theorem 0.42, printed p. 38, and Theorem 2.9 with its proof, pp. 75–76. [Free author edition](https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe2.pdf). The complete closed graph input used here is proved in Section 2 above.


- [H1] Lars Hörmander, *The Analysis of Linear Partial Differential Operators I: Distribution Theory and Fourier Analysis*, second edition (1990), 2003 reprint, Springer, Definition 8.3.5, p. 275. ISBN 978-3-642-61497-2. [Edition information](https://doi.org/10.1007/978-3-642-61497-2).
- [H2] Lars Hörmander, *The Analysis of Linear Partial Differential Operators II: Differential Operators with Constant Coefficients*, reprint of the 1983 edition, Springer, 2005, Definition 10.2.6, p. 21; Theorem 11.1.1, Definition 11.1.2 and Theorem 11.1.3, pp. 61–62; Definition 14.3.1, pp. 237–238; and (14.4.6) with its proof, pp. 246–247. ISBN 978-3-540-26964-9. [Edition information](https://doi.org/10.1007/b138375).
