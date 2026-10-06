# Positive real powers and spectral rescaling

*Written by GPT-6.1 Sol (OpenAI) and GPT-6 Astra (OpenAI). Self-checked by the writing AI. Original exposition: CC0.*

**Working question: Which time scale belongs to an operator of order greater than one?** If an eigenvalue of an order-\(m\) operator is \(\lambda\), its order-one root has frequency \(\lambda^{1/m}\). The count is transferred by that change of variable, but the root also needs an operator construction with its domain and second symbol term. A formal substitution in an asymptotic formula cannot supply those missing facts.

A positive elliptic operator of order \(m\) has a spectral \(m\)-th root. To use that root in a wave equation, we need to know that it is a classical pseudodifferential operator, and we need its second symbol term. We prove those facts by integrating a uniformly controlled resolvent. The root then transfers local spectral densities, counting estimates and compressed spectral distributions from order one to every positive order.

The freely accessible complex-power construction of Ammann, Lauter, Nistor and Vasy [ALNV] and Hörmander's spectral-function article [H] give related results. Guillemin and Sternberg [GS] supplies semiclassical background. We use the scalar composition, asymptotic summation, real Sobolev mapping and elliptic regularity proved in [Classical scalar symbols, summation and regularity](../providers/analysis/classical-scalar-calculus.md#finite-symbol-calculus). Its underlying finite-seminorm estimates and summation proof are in [Classical scalar Sobolev calculus](../providers/analysis/classical-scalar-calculus.md#real-sobolev-mapping). Compact Sobolev inclusions are in [Compact Sobolev inclusion and elliptic Fredholm maps](../providers/analysis/classical-scalar-calculus.md#compact-sobolev-inclusion). The compact positive eigenbasis and every exact diagonal multiplier domain are proved in [Compact positive inverses and diagonal domains](../providers/analysis/compact-spectrum-domains.md#compact-inverse-domains); this is the generic Hilbert-space theorem, with no boundary regularity assumption imported.

Sections 1–5 concern a compact smooth manifold \(X\) without boundary, of positive dimension, and scalar half densities. Section 6 assumes \(n=\dim X\geq2\), as in [Return times and spectral counting](return-times-and-spectral-counting.md) and [Compressed spectral measures and symbol distributions](compressed-spectral-measures-and-symbol-distributions.md). We use \(D=-i\partial\), left symbols and step-one classical expansions. A positive operator here satisfies \((Pu,u)>0\) for every nonzero smooth half density. In particular it has no zero eigenvector. This condition matters for negative powers.

## 1. The realization and the moment domains

Let \(P\in\Psi^m_{\mathrm{cl}}(X;\Omega^{1/2})\), with real order \(m\), be elliptic, formally symmetric and positive. Write its local left symbol as
\[
 \begin{gathered}
P_L(x,\xi)\sim p(x,\xi)+p_0(x,\xi)+\\
p_{m-2}(x,\xi)+\cdots,
\\
p_s=p_0+\frac i2\sum_\ell\partial_{x_\ell}\partial_{\xi_\ell}p.
 \end{gathered}
 \tag{1}
\]
Here \(p,p_0\) have degrees \(m,m-1\). The half-density calculus makes \(p_s\) an invariant scalar symbol.

Positivity implies \(p>0\) away from the zero section. Indeed a compactly supported oscillatory test \(u_r=e^{irx\cdot\theta}v(x)|dx|^{1/2}\) satisfies
\[
 \begin{gathered}
r^{-m}(Pu_r,u_r)\longrightarrow
\int p(x,\theta)|v(x)|^2\,dx,\\
 r\longrightarrow\infty.
 \end{gathered}
 \tag{2}
\]
To verify this formula, conjugate the local quantization by the exponential, replacing \(\xi\) by \(r\theta+\eta\), and use the rapid decrease of \(\widehat v(\eta)\). On \(|\eta|\leq r|\theta|/2\), homogeneity and the symbol estimates give dominated convergence. On its complement, arbitrarily many powers of the rapid decrease absorb the polynomial symbol bound, including the factor \(r^{-m}\) for negative \(m\). Localized smoothing errors decrease faster than any power of \(r\). Thus (2) holds for every real \(m\). Positivity makes its limit nonnegative. Localizing \(v\) near any point gives \(p(x,\theta)\geq0\); ellipticity excludes equality.

**Proposition 1.1.** If \(m\leq0\), \(P\) extends to a bounded positive self-adjoint operator on \(L^2\). If \(m>0\), its maximal realization is the closure of its smooth restriction, is positive and self-adjoint, and has domain \(H^m\). In the latter case there is a smooth complete orthonormal eigenbasis with
\[
P\phi_j=\lambda_j\phi_j,\qquad
0<\lambda_*\leq\lambda_j\longrightarrow\infty.
\tag{3}
\]

**Proof.** For \(m\leq0\), the Sobolev mapping theorem gives boundedness on \(L^2\). Density of smooth half densities extends the symmetric pairing and positivity, and a bounded symmetric operator with full domain is self-adjoint. Its kernel is smooth by elliptic regularity and therefore zero by the strict positivity assumption. The quadratic-form Cauchy–Schwarz proof in [Compact positive inverses and diagonal domains](../providers/analysis/compact-spectrum-domains.md#the-positive-compact-spectral-proof) shows that a vector with zero nonnegative quadratic form lies in the operator's kernel. Thus the extension is positive. A uniform positive lower bound is not implied for negative order.

For \(m>0\), an elliptic parametrix gives
\[
 \begin{gathered}
Pu\in L^2,\ u\in L^2\ \Longleftrightarrow\ u\in H^m,
\\
\|u\|_{H^m}\leq C(\|Pu\|_2+\|u\|_2).
 \end{gathered}
 \tag{4}
\]
The reverse graph-norm estimate follows from the mapping theorem. Smooth density therefore identifies the graph closure and the maximal domain. If \(v\) is in the Hilbert adjoint domain, testing against smooth inputs says \(Pv\in L^2\) distributionally. Formula (4) puts \(v\) in the same domain. This proves self-adjointness. Smooth approximation extends the nonnegative quadratic form to \(H^m\).

The range of \(P+I\) is closed, since \(\|(P+I)u\|_2\geq\|u\|_2\): a Cauchy sequence of images makes the inputs and their \(P\)-images Cauchy, and closedness gives a limiting preimage. Its range is dense because its orthogonal complement is the kernel of its adjoint, which is the zero kernel of \(P+I\). Its inverse is positive, self-adjoint, and bounded from \(L^2\) to \(H^m\). Compact Sobolev inclusion makes that inverse compact on \(L^2\). The local positive compact spectral proof in the stated prerequisite supplies a complete eigenbasis and finite multiplicities. The Hilbert space is infinite-dimensional: one coordinate ball contains infinitely many disjoint smaller balls, whose normalized smooth bumps are orthonormal. Thus the positive inverse eigenvalues tend to zero, and the corresponding \(P\)-eigenvalues tend to infinity. Elliptic regularity makes each eigenvector smooth. Nonnegativity gives \(\lambda_j\geq0\), and strict positivity on smooth nonzero vectors excludes zero. The discrete sequence therefore has a positive minimum. This proves (3). ∎

From now on \(m>0\). In these coordinates the spectral power has its exact domain
\[
\begin{aligned}
\mathcal D(P^a)&=\left\{u\in L^2:
\sum_j\lambda_j^{2a}|(u,\phi_j)|^2<\infty\right\},\\
P^au&=\sum_j\lambda_j^a(u,\phi_j)\phi_j,\qquad a\in\mathbb R.
\end{aligned}
\tag{5}
\]
This is the existing discrete multiplier construction. Negative powers are bounded on all \(L^2\); finite eigenvector sums are a core for every power, by convergence of both tails in (5).

Integer powers do not require a fractional-power theorem. Induction using the elliptic inverse and the mapping theorem gives
\[
 \begin{gathered}
\mathcal D(P^k)=H^{km},\\
\|u\|_{H^{km}}\asymp\|u\|_2+\|P^ku\|_2
\\
\quad(k=0,1,2,\ldots).
 \end{gathered}
 \tag{6}
\]
For the induction step, \(Pu\in H^{km}\) implies \(u\in H^{(k+1)m}\) by the elliptic parametrix; the converse follows by mapping. The recursive domain conditions agree with the integer moment domains already proved for a closed operator with a complete eigenbasis.

Consequently the resolvent \(R(t)=(P+t)^{-1}\), \(t\geq0\), obeys
\[
 \begin{gathered}
\|R(t)\|_{L^2\to L^2}\leq(\lambda_*+t)^{-1},\\
\|R(t)\|_{H^{km}\to H^{km}}\leq C_k(1+t)^{-1}.
 \end{gathered}
 \tag{7}
\]
The second estimate follows by commuting \(R(t)\) with the integer multiplier \(P^k\) in (5), then using (6). Only these nonnegative integer graph scales will be needed to estimate a smoothing error.

## 2. A resolvent integral and its parameter estimates

For \(-1<a<0\), define the positive constant
\[
c_a=\left(\int_0^\infty\frac{r^a}{1+r}\,dr\right)^{-1}.
\tag{8}
\]
The integral converges at zero because \(a>-1\), and at infinity because \(a<0\). Scalar rescaling gives
\[
c_a\int_0^\infty\frac{t^a}{s+t}\,dt=s^a,\qquad s>0.
\tag{9}
\]
By (7), the integral
\[
P^a=c_a\int_0^\infty t^aR(t)\,dt
\tag{10}
\]
converges in \(L^2\) operator norm. Here is a direct construction of that integral. The diagonal formulas give the resolvent identity
\[
 R(t)-R(s)=(s-t)R(t)R(s),
\]
so \(R(t)\) is norm continuous on \([0,\infty)\). On every compact interval \([\varepsilon,L]\) with \(\varepsilon>0\), uniform norm continuity of \(t^aR(t)\) makes its Riemann sums Cauchy: replacing a tagged partition by a refinement changes the sum by at most the interval length times its modulus of continuity at the partition mesh. Bounded operators form a complete normed space, since an operator-norm Cauchy sequence converges on each vector and the common norm estimates pass to the limit. Thus the finite-interval integral exists. Its two tails are controlled by
\[
 \begin{aligned}
 \int_0^\varepsilon\|t^aR(t)\|\,dt
 &\le\lambda_*^{-1}\frac{\varepsilon^{a+1}}{a+1},\\
 \int_L^\infty\|t^aR(t)\|\,dt
 &\le\frac{L^a}{-a}.
 \end{aligned}
\]
Both tend to zero at the indicated endpoints, so the improper integral is a norm limit of the finite-interval integrals. Pairing its Riemann sums and then its norm limit with each \(\phi_j\), and using (9), proves equality with the exact spectral multiplier (5). Equality on the complete eigenbasis determines these bounded operators.

We make the parameter estimates explicit. A bounded family in \(\Psi^r\) means bounded local symbol seminorms of order \(r\), together with bounded smooth-kernel seminorms for the localized smoothing parts. Thus
\((1+t)^{-\ell}\Psi^r\) means that multiplication by \((1+t)^\ell\) gives such a bounded family.

**Lemma 2.1.** There is a parameter family \(Q(t)\) such that
\[
 \begin{gathered}
(P+t)Q(t)=I-W(t),\\
W(t)\in(1+t)^{-1}\Psi^{-\infty}.
 \end{gathered}
 \tag{11}
\]
Its local symbols have a formal expansion with coefficients \(q_j(x,\xi,t)\) satisfying
\[
 \begin{gathered}
q_j(x,s\xi,s^m t)=s^{-m-j}q_j(x,\xi,t),
\\
 s>0,\quad \xi\ne0,\ t\geq0.
 \end{gathered}
 \tag{12}
\]
After cutting the coefficients off near \(\xi=0\), every remainder after \(j<N\) has, apart from a \((1+t)^{-1}\) smoothing term, the simultaneous bounds
\[
S^{-m-N}\quad\hbox{and}\quad(1+t)^{-1}S^{-N}.
\tag{13}
\]
All of these statements include every fixed base and frequency derivative.

**Proof.** Choose a finite chart partition \(\sum_\nu\varphi_\nu=1\), and cutoffs \(\psi_\nu=1\) near \(\operatorname{supp}\varphi_\nu\). In each chart take a complete left symbol \(A_\nu\) of \(P\). Above a sufficiently large frequency its real part is at least \(c\langle\xi\rangle^m\), since \(p>0\). Modify bounded frequencies so that
\[
\operatorname{Re}A_\nu\geq c\langle\xi\rangle^m
\tag{14}
\]
throughout the relevant base support, extending it smoothly to a larger chart product if necessary. This modification changes the local operator only by a smooth kernel. Put
\[
 \begin{gathered}
r_\nu(t)=(A_\nu+t)^{-1},\\
Q_0(t)=\sum_\nu\psi_\nu\operatorname{Op}(r_\nu(t))\varphi_\nu.
 \end{gathered}
 \tag{15}
\]
The reciprocal differentiation rule and (14) give
\[
|\partial_x^\beta\partial_\xi^\alpha r_\nu(t)|
\leq
C_{\alpha\beta}\frac{\langle\xi\rangle^{-|\alpha|}}
{t+\langle\xi\rangle^m}.
\tag{16}
\]
Each differentiated term has a denominator power one larger than the number of differentiated factors of \(A_\nu\). The factors supply at most that many powers of \(\langle\xi\rangle^m\), and frequency derivatives supply their stated losses. This proves (16) also for mixed derivatives. In particular \(Q_0\) is simultaneously bounded in \(\Psi^{-m}\) and \((1+t)^{-1}\Psi^0\).

Set \(E(t)=I-(P+t)Q_0(t)\). The leading local pointwise product is exactly
\((A_\nu+t)r_\nu=1\). The scalar parameter \(t\) has no frequency derivatives and contributes no composition error. The composition defect contains at least one paired frequency derivative of \(A_\nu\), so the finite-seminorm remainder theorem gives
\[
E(t)\in\Psi^{-1}\ \cap\ (1+t)^{-1}\Psi^{m-1}.
\tag{17}
\]
The chart commutators \([P,\psi_\nu]\) have order \(m-1\); their products with \(r_\nu\) have these same bounds. The changed bounded frequencies and separated-support terms are smoothing with the same parameter bounds, using (16) and frequency integration by parts. The constant symbol quantizes to the identity exactly, and \(\sum_\nu\psi_\nu\varphi_\nu=1\). These observations account for all global errors in (17).

For \(j\geq0\), composition now bounds \(Q_0E^j\) in
\[
\Psi^{-m-j}\ \cap\ (1+t)^{-1}\Psi^{-j}.
\tag{18}
\]
For \(j\geq1\), use the weighted bound for one factor \(E\), the weighted bound for \(Q_0\), and the unweighted bounds for the other factors. This gives the additional estimate
\[
Q_0E^j\in(1+t)^{-2}\Psi^{m-j}.
\tag{19}
\]

Apply the existing asymptotic summation construction to
\(Q_0+\sum_{j\geq1}Q_0E^j\), keeping \(Q_0\) unchanged. Choose its successive frequency cutoffs uniformly in \(t\). To justify this choice, enumerate the seminorms of all three bounded families (18)–(19); for term \(j\), make the first \(j\) weaker-order seminorms at most \(2^{-j}\), exactly as in the ordinary summation proof. The constants are uniform because the families are bounded after multiplication by their displayed weights. A finite atlas gives a countable list, including the smooth-kernel parts. Cutoffs of those smooth kernels satisfy the same estimates by their uniform rapid Fourier decrease. Thus the resulting \(Q\) has, for \(N\geq1\),
\[
\begin{aligned}
F_N&=Q-\sum_{j<N}Q_0E^j,\\
F_N&\in\Psi^{-m-N},\\
(1+t)F_N&\in\Psi^{-N},\\
(1+t)^2F_N&\in\Psi^{m-N}.
\end{aligned}
\tag{20}
\]
Only the corrections \(j\geq1\) were cut off; their bounded-frequency changes retain the last estimate. The resulting parameter family is continuous in each fixed weaker symbol seminorm: its finite partial sums are continuous, and the chosen cutoffs make their tails uniformly convergent in that seminorm. This gives the parameter measurability needed for the subsequent integrals, without assuming convergence of the formal geometric series in operator norm.

The finite geometric identity is
\[
(P+t)\sum_{j<N}Q_0E^j=I-E^N.
\tag{21}
\]
The error \(E^N\) lies in \((1+t)^{-1}\Psi^{m-N}\), using the weighted estimate for one factor and the unweighted estimate for the others. Multiplication of (20) by \(P\) has that same bound. Multiplication by \(t\) also has it, now using the third estimate in (20). Hence \(W=I-(P+t)Q\) lies in \((1+t)^{-1}\Psi^{m-N}\) for every \(N\), proving (11).

We finally identify the formal coefficients and their remainder bounds. In a fixed chart denote the homogeneous symbol terms by \(p_{m-k}\), with \(p_m=p\). The unique formal right inverse is
\[
 \begin{gathered}
q_0=(p+t)^{-1},\\
q_j=-(p+t)^{-1}
\\
\sum_{\substack{k+|\alpha|+\ell=j\\ 0\leq\ell<j}}
\frac{\partial_\xi^\alpha p_{m-k}\,D_x^\alpha q_\ell}{\alpha!},
\\
 j\geq1,
 \end{gathered}
 \tag{22}
\]
where \(p_m=p\). This recursion follows by equating the successive degree terms in the usual composition formula for \((P+t)Q\). It proves (12) by induction.

Here the expansion uses the joint scaling of \((\xi,t)\), rather than a fixed-\(t\) classical expansion. To see the full remainder estimate, expand \((A_\nu+t)^{-1}\) around \((p+t)^{-1}\) at high frequency. The difference \(A_\nu-p\) is of order \(m-1\), and its ratio to \(p+t\) is \(O(\langle\xi\rangle^{-1})\), uniformly in \(t\). The finite reciprocal identity, with its differentiated remainder, gives the two bounds in (13) after any prescribed number of degrees. Apply the ordinary finite-seminorm composition remainder to the finitely many \(Q_0E^j\) contributing to those degrees. It preserves both bounds (18), with the corresponding further frequency loss. All remaining terms are covered by (20). Collecting coefficients gives exactly (22), because (11) has no formal error. Near zero frequency the cutoffs change only \((1+t)^{-1}\) smoothing terms, by (16). This proves (13) with all derivatives. ∎

For nonintegral \(m\), the fixed operator \(P+t\) need not be classical with step-one degrees: its added term of degree zero need not lie in that sequence. The proof above uses ordinary parameter symbol estimates. Classicality of the integrated operator will follow from (12).

## 3. Integrating the symbols and the smoothing error

Multiplying (11) by the true resolvent gives
\[
R(t)=Q(t)+R(t)W(t).
\tag{23}
\]
For any requested source and target Sobolev orders \(s,r\), choose a nonnegative integer \(k\) with \(km\geq r\). The smoothing estimate in (11) maps \(H^s\) to \(H^{km}\) with norm \(O((1+t)^{-1})\). Estimate (7) applies to \(R(t)\) on that output space. Thus
\[
\|R(t)W(t)\|_{H^s\to H^r}\leq C_{s,r}(1+t)^{-2}.
\tag{24}
\]
The integral of \(t^a(1+t)^{-2}\) is finite for \(-1<a<0\). Therefore the integral of this error is smoothing. The smooth-kernel correspondence proved in the scalar-calculus prerequisite makes this precise. In a coordinate chart, \(y\mapsto\partial_y^\alpha\delta_y\) is \(C^k\) into \(H^{-s}\) for \(s>n/2+|\alpha|+k\); the Fourier transform is a polynomial times \(e^{-iy\cdot\xi}\), and its differentiated squared Sobolev weight is integrable. Output evaluation through order \(|\beta|+k\) is bounded on \(H^r\) when \(r>n/2+|\beta|+k\), by Fourier Cauchy–Schwarz. Apply (24) with these source and target indices. Difference quotients converge by the same integrable Fourier bounds, and all resulting kernel derivatives are bounded by \(C(1+t)^{-2}\). The parameter integrals therefore have jointly continuous derivatives of every order. The kernel represents the integrated operator by testing against compact smooth inputs and the same integrable majorants.

Let \(u_N(x,\xi,t)\) be a local symbol remainder in (13). Combining its two estimates gives
\[
|\partial_x^\beta\partial_\xi^\alpha u_N|
\leq C_{\alpha\beta N}
\frac{\langle\xi\rangle^{-N-|\alpha|}}
{t+\langle\xi\rangle^m}.
\tag{25}
\]
Indeed the minimum of
\(\langle\xi\rangle^{-m-N-|\alpha|}\) and
\((1+t)^{-1}\langle\xi\rangle^{-N-|\alpha|}\)
is at most twice the right side, since \(\langle\xi\rangle^m\geq1\). Integrating (25), substituting \(t=\langle\xi\rangle^m r\), and using (8), gives
\[
c_a\int_0^\infty t^a u_N(x,\xi,t)\,dt\in S^{ma-N}.
\tag{26}
\]
Here is an explicit domination check, including the two ends of the parameter interval. Put \(R=\langle\xi\rangle\geq1\). For every derivative in (25),
\[
\begin{aligned}
\int_0^{R^m}\frac{t^aR^{-N-|\alpha|}}{t+R^m}\,dt
&\leq \frac{R^{ma-N-|\alpha|}}{a+1},\\
\int_{R^m}^{\infty}\frac{t^aR^{-N-|\alpha|}}{t+R^m}\,dt
&\leq \frac{R^{ma-N-|\alpha|}}{-a}.
\end{aligned}
\]
These follow respectively from \(t+R^m\geq R^m\) and \(t+R^m\geq t\). The constants are finite precisely for \(-1<a<0\). On a compact frequency set the same bounds give ordinary dominated differentiation; the displayed frequency losses then give every symbol seminorm globally. Thus there is no unproved interchange of an infinite formal expansion with the integral: first integrate a finite expansion, bound its remainder by these inequalities, and then let the number of degrees be arbitrary. The extra weighted smoothing terms in Lemma 2.1 integrate to smoothing terms because \(t^a(1+t)^{-1}\) is integrable in this range.

For \(\xi\ne0\), each integral
\[
h_j(x,\xi)=c_a\int_0^\infty t^a q_j(x,\xi,t)\,dt
\tag{27}
\]
converges with all derivatives on compact angular sets. The reciprocal expansions in the preceding proof give the same integrable majorant; for \(j\geq1\) there are at least two resolvent denominators. Scaling \(t=s^m r\) in (12) shows
\[
h_j(x,s\xi)=s^{ma-j}h_j(x,\xi).
\tag{28}
\]
The local integrated symbol therefore has a full step-one classical expansion
\[
\sigma_L(P^a)\sim\sum_{j\geq0}h_j,\qquad -1<a<0.
\tag{29}
\]
Equations (23)–(26) identify its operator with the true norm-convergent integral (10). Local oscillatory integrals can first be paired with smooth tests; their rapidly decreasing Fourier factors and (25) justify this identification before passage to distributions. The integrated smoothing error has already been controlled. Thus (29) proves classicality, including every differentiated remainder.

## 4. The principal and subprincipal terms

Return to the notation of (1), so \(p_0\) now means the term of degree \(m-1\). The first correction in (22) is
\[
q_1=-\frac{p_0}{(p+t)^2}
+\frac1i\,\frac{\sum_\ell p_{\xi_\ell}p_{x_\ell}}{(p+t)^3}.
\tag{30}
\]
Its sign comes from \(D_x(p+t)^{-1}=-(1/i)(p+t)^{-2}p_x\).

Differentiate (9) once and twice in \(s>0\). Dominated convergence is valid on every compact positive \(s\)-interval, giving
\[
\begin{aligned}
c_a\int_0^\infty\frac{t^a}{(s+t)^2}\,dt&=-a s^{a-1},\\
c_a\int_0^\infty\frac{t^a}{(s+t)^3}\,dt
&=\frac{a(a-1)}2s^{a-2}.
\end{aligned}
\tag{31}
\]
Consequently
\[
 \begin{gathered}
\sigma_L(P^a)=p^a+a p^{a-1}p_0\\
\quad+\frac{a(a-1)}{2i}p^{a-2}
\sum_\ell p_{\xi_\ell}p_{x_\ell}
\\
\pmod{S^{ma-2}}.
 \end{gathered}
 \tag{32}
\]
To obtain the subprincipal symbol, add \((i/2)\sum_\ell\partial_{x_\ell}\partial_{\xi_\ell}(p^a)\) to the term of degree \(ma-1\). The chain rule gives a cross term with coefficient \(ia(a-1)/2\), which cancels the coefficient \(a(a-1)/(2i)\) in (32). The remaining expression is
\[
\begin{aligned}
(P^a)_{\mathrm{prin}}&=p^a,\\
(P^a)_s&=a p^{a-1}p_s.
\end{aligned}
\tag{33}
\]
This is an invariant half-density identity.

## 5. Every real power, with its actual domain

**Theorem 5.1.** For \(m>0\) and every \(a\in\mathbb R\), the spectral power \(P^a\) is defined by a classical operator of order \(ma\), with symbols (33). If \(a>0\), its exact self-adjoint domain is \(H^{ma}\); if \(a\leq0\), its domain is all \(L^2\). On smooth inputs the powers also act as their corresponding continuous pseudodifferential maps.

**Proof.** The scalar composition rule, in the half-density subprincipal convention (1), says
\[
 \begin{gathered}
(AB)_s=a_s b+a b_s+\frac1{2i}\{a,b\},
\\
\{a,b\}=a_\xi\cdot b_x-a_x\cdot b_\xi.
 \end{gathered}
 \tag{34}
\]
This identity follows by collecting the degree one lower term in the existing left composition formula and adding the mixed derivative of its principal product. It applies to classical operators of any real orders.

If \(a<0\), choose \(k\) so that \(-1<a/2^k<0\). The bounded spectral product identity gives
\[
P^a=(P^{a/2^k})^{2^k}.
\tag{35}
\]
Classical composition proves order \(ma\). At each squaring the Poisson bracket of a symbol with itself is zero; (34) doubles the subprincipal term times the principal term. Starting from (33) yields exactly (33) for the final exponent. This handles every negative exponent, including the negative integers.

Integer nonnegative powers are already classical by composition. Their principal symbols are \(p^\ell\), and induction in (34), with \(\{p^r,p^s\}=0\), gives \(\ell p^{\ell-1}p_s\).

For \(a>0\), choose an integer \(\ell>a\). The already constructed classical product
\[
A_a=P^\ell P^{a-\ell}
\tag{36}
\]
has order \(ma\), principal \(p^a\), and subprincipal
\(\ell p^{\ell-1}p^{a-\ell}p_s+
(a-\ell)p^\ell p^{a-\ell-1}p_s
=a p^{a-1}p_s\).
The bracket again vanishes.

Equality with the spectral power includes its domain. For a smooth \(u\), its coefficients have all integer moments by (6). Hence (36), interpreted as spectral multipliers, is defined and has coefficients \(\lambda_j^a(u,\phi_j)\). It equals (5) on smooth inputs. The elliptic graph estimate for \(A_a\) shows that the closure of this smooth operator has domain \(H^{ma}\), exactly as in (4). Since the spectral power (5) is closed, this closure is a restriction of it. Conversely finite eigenvector sums are a core for (5) and lie in the smooth domain of \(A_a\); therefore the spectral power is a restriction of that closure. The two operators and their domains coincide. At \(a=0\) the operator is the identity with zero subprincipal symbol. ∎

In particular
\[
 \begin{gathered}
Q=P^{1/m}\in\Psi^1_{\mathrm{cl}},\\
q=p^{1/m}, \\
q_s=\frac1m p^{1/m-1}p_s.
 \end{gathered}
 \tag{37}
\]
The spectral root is positive and has domain \(H^1\), so it satisfies the hypotheses of the first-order wave and spectral lessons.

## 6. Spectral formulas at arbitrary positive order

Assume \(n\geq2\). Write \(e_P(x,y,E)\), \(\Pi_E^P\), and \(N_P(E)\) for the spectral kernel, projection and count of \(P\) below or at energy \(E\). The exact eigenbasis identity is
\[
 \begin{gathered}
\Pi_\lambda^Q=\Pi_{\lambda^m}^P,\\
e_Q(x,y,\lambda)=e_P(x,y,\lambda^m),
\\
N_Q(\lambda)=N_P(\lambda^m).
 \end{gathered}
 \tag{38}
\]
Either consistent sharp endpoint convention can be used.

Let \(T_q(x)\) be the first positive base return time for the Hamilton flow of \(q\), minimized over nonzero starting covectors at \(x\). Let \(T_q^*(x,\xi)\) be the first full covector return time, with value infinity when there is no return. These are the return functions in [Return times and spectral counting](return-times-and-spectral-counting.md), now for \(q\).

Define the local model density
\[
 \begin{gathered}
\mathcal V_P(x,E)
\\
=(2\pi)^{-n}
\bigg\{\int_{p(x,\xi)<E}d\xi
\\
-\int\delta(E-p(x,\xi))p_s(x,\xi)\,d\xi\bigg\}.
 \end{gathered}
 \tag{39}
\]
The second integral is integration over the regular energy surface with its coarea density. It is well defined: Euler homogeneity gives \(\xi\cdot p_\xi=mp>0\) on a positive energy surface. The expression transforms as a density on \(X\).

The change from \(Q\) to \(P\) in this correction is exact:
\[
\begin{aligned}
\partial_\lambda\int_{q<\lambda}q_s\,d\xi
&=\int\delta(\lambda-p^{1/m})
\,\frac1m p^{1/m-1}p_s\,d\xi\\
&=\int\delta(\lambda^m-p)p_s\,d\xi.
\end{aligned}
\tag{40}
\]
Indeed on \(p=\lambda^m\), the delta change of variable contributes \(m\lambda^{m-1}\), and \(q_s\) contributes its reciprocal. Thus (39) is precisely the first-order two-term model at \(\lambda=E^{1/m}\).

Put \(V_x=\int_{p(x,\xi)<1}d\xi>0\). The local return-time theorem yields
\[
\begin{gathered}
\limsup_{E\to\infty}
E^{(1-n)/m}
\frac{|e_P(x,x,E)-\mathcal V_P(x,E)|}{V_x}\\
\leq\frac{C_n}{T_q(x)}.
\end{gathered}
\tag{41}
\]
If \(J:X\to(0,\infty)\) is continuous with \(J(x)<T_q(x)\), the corresponding eventual bound \(C_n/J(x)\) is uniform in \(x\). This follows by the same substitution in the already proved uniform first-order estimate.

Writing \(dxd\xi\) for symplectic volume and \(\mathcal V_P(E)=\int_X\mathcal V_P(x,E)\), the global theorem gives
\[
 \begin{gathered}
\limsup_{E\to\infty}E^{(1-n)/m}
|N_P(E)-\mathcal V_P(E)|
\\
\leq C_n\int_{p<1}\frac{dxd\xi}{T_q^*(x,\xi)}.
 \end{gathered}
 \tag{42}
\]
If the periodic covectors have symplectic measure zero, the right side is zero. Homogeneity of \(p\) and \(p_s\) then makes the two terms explicit:
\[
 \begin{gathered}
N_P(E)=A_P E^{n/m}-B_P E^{(n-1)/m}
\\
+o(E^{(n-1)/m}),\\
A_P=(2\pi)^{-n}\int_{p<1}dxd\xi,\\
B_P=(2\pi)^{-n}\int\delta(1-p)p_s\,dxd\xi.
 \end{gathered}
 \tag{43}
\]
Without that measure-zero hypothesis the remainder is \(O(E^{(n-1)/m})\), since the inverse return function is bounded. The sign of \(B_P\) need not be positive.

The flow whose time appears in (41)–(42) is \(H_q\). On \(p=1\),
\[
H_q=\frac1m H_p,\qquad T_q^*=mT_p^*.
\tag{44}
\]
The same proportionality holds for base returns of individual covectors on that normalized surface. The two fields have the same trajectories, since their proportionality factor is constant along each energy surface, but their times differ. The degree-one field \(H_q\) is the one with return times invariant under radial rescaling.

For a self-adjoint \(B\in\Psi^0_{\mathrm{cl}}\) with real principal \(b\), let \(\rho_E^B\) count the eigenvalues of
\(\Pi_E^P B\Pi_E^P\) on its finite-dimensional spectral subspace. The continuous-test theorem and (38) give
\[
 \begin{gathered}
E^{-n/m}\rho_E^B(f)\longrightarrow
\\
(2\pi)^{-n}\int_{p<1}f(b(x,\xi))\,dxd\xi,
\\
 f\in C(\mathbb R).
 \end{gathered}
 \tag{45}
\]
Its probability normalization is \(\rho_E^B/N_P(E)\), whose limit divides the right side by \(A_P\). No periodic-measure-zero hypothesis is needed for (45). The previously proved trace-norm leakage bound becomes
\[
\|(I-\Pi_E^P)B\Pi_E^P\|_1
=O(E^{(n-1/2)/m}),
\tag{46}
\]
by applying that bound to \(Q\) at parameter \(E^{1/m}\).

The squared Hilbert–Schmidt leakage and fixed-power comparison in [Compressed spectral measures and symbol distributions](compressed-spectral-measures-and-symbol-distributions.md) give, with the same exact substitution,
\[
 \begin{aligned}
 \|(I-\Pi_E^P)B\Pi_E^P\|_2^2
     &=O(E^{(n-1)/m}),\\
 \|\Pi_E^PB^j\Pi_E^P-(\Pi_E^PB\Pi_E^P)^j\|_1
     &=O_j(E^{(n-1)/m}).
 \end{aligned}
 \tag{46a}
\]
For every fixed polynomial \(q_0\), the scaled version of (45) has error
\[
 \begin{gathered}
E^{-n/m}\rho_E^B(q_0)
 \\
-(2\pi)^{-n}\int_{p<1}q_0(b)\,dxd\xi
       \\
=O_{q_0}(E^{-1/m}).
 \end{gathered}
 \tag{46b}
\]
The probability-normalized polynomial moments have the same rate, by dividing by \(N_P(E)=A_PE^{n/m}+O(E^{(n-1)/m})\), with \(A_P>0\). The region remains \(p<1\), because \(p^{1/m}<1\) is equivalent to it. These conclusions need no periodic-measure-zero hypothesis. Equation (46) continues to concern one-sided trace-norm leakage; (46a) concerns squared Hilbert–Schmidt leakage and the two crossings in a moment.

Finally suppose \(P\) is differential. Its positive elliptic principal polynomial forces the integer order \(m\) to be even: for odd \(m\), \(p(x,-\xi)=-p(x,\xi)\) cannot remain positive. Its term of degree \(m-1\) is odd in \(\xi\), and so is \(\sum\partial_x\partial_\xi p\). Hence \(p_s\) is odd while \(p\) is even. Reflection \(\xi\mapsto-\xi\) preserves each energy surface and its coarea density, giving
\[
\int\delta(E-p)p_s\,d\xi=0
\tag{47}
\]
in every fiber. Thus the subprincipal term disappears from both the local and global integrated formulas for positive elliptic differential operators.

### Use the conclusion

Check the parameter resolvent integral and the exact moment domain before rescaling a count. For a shifted positive operator, retain the shift in the subprincipal term; then compare with the round-sphere square root.

## 7. Five exercises with complete solutions

**Exercise 7.1 (a Fourier multiplier and its domain; introductory).** On the flat torus \((\mathbb R/2\pi\mathbb Z)^n\), take \(P=I-\Delta\). Find \(P^a\), its principal and subprincipal symbols, and its exact \(L^2\) domain for every real \(a\). Check classicality directly.

**Solution 7.1.** The complete Fourier basis and its classical torus quantization are proved in Section 6 of [Local spectral density and the subprincipal correction](local-spectral-density-and-subprincipal-correction.md). Its normalized vectors have eigenvalues \(1+|k|^2\), \(k\in\mathbb Z^n\). Thus
\[
\widehat{P^a u}(k)=(1+|k|^2)^a\widehat u(k).
\tag{48}
\]
For \(a>0\), the squared moment condition is precisely the \(H^{2a}\) norm condition. For \(a\leq0\), the multiplier is bounded and its domain is all \(L^2\).

The smooth Euclidean extension is \((1+|\xi|^2)^a\). At high frequency its binomial expansion is
\[
|\xi|^{2a}\sum_{j\geq0}\binom aj|\xi|^{-2j}.
\tag{49}
\]
Taylor's formula for \((1+s)^a\) on \(0\leq s\leq1/2\), differentiated a prescribed finite number of times, bounds the remainder after \(j<N\) in \(S^{2a-2N}\). Chain and product differentiation give the corresponding losses for every frequency derivative. The missing odd degree terms are zero, so (49) is a step-one classical expansion. Its principal symbol is \(|\xi|^{2a}\). Its degree \(2a-1\) term and its mixed base-frequency derivatives vanish; therefore the subprincipal symbol is zero. This agrees with Theorem 5.1.

**Exercise 7.2 (the endpoints of the resolvent formula; intermediate).** Prove that the ordinary scalar integral in (9) diverges at \(a=-1\) and at \(a=0\). Obtain \(P^{-1}\) from a convergent integral without taking either divergent endpoint. Explain what fails if \(P\) has a zero mode.

**Solution 7.2.** For a fixed \(s>0\), at \(a=-1\) the integrand is comparable to \(t^{-1}/s\) near zero. At \(a=0\) it is comparable to \(t^{-1}\) at infinity. Both divergences are logarithmic.

Use \(a=-1/2\), which lies inside the convergence interval:
\[
 \begin{gathered}
P^{-1/2}=c_{-1/2}\int_0^\infty t^{-1/2}(P+t)^{-1}\,dt,
\\
P^{-1}=(P^{-1/2})^2.
 \end{gathered}
 \tag{50}
\]
The first integral converges in operator norm by (7); the second identity holds on all \(L^2\) by the bounded eigenbasis multipliers. It also follows from Theorem 5.1 that \(P^{-1}\) is classical of order \(-m\), with principal \(p^{-1}\) and subprincipal \(-p^{-2}p_s\).

If \(P\phi=0\), its resolvent acts on \(\phi\) as \(t^{-1}\phi\). Even the integral at \(a=-1/2\) then diverges at zero. The negative power is undefined on that vector. One can instead specify a reduced inverse on the orthogonal complement of the kernel, but that is a different operator convention; strict positivity in this lesson avoids this issue.

**Exercise 7.3 (the subprincipal cross term; intermediate).** Suppose the first two terms of the left symbol of \(P\) are \(p\) and \(p_0\). Starting from (32), verify the full cancellation that gives (33). Then check that composing two already constructed powers \(P^r,P^s\) gives the subprincipal formula for exponent \(r+s\).

**Solution 7.3.** The mixed derivative is
\[
 \begin{gathered}
\sum_\ell\partial_{x_\ell}\partial_{\xi_\ell}(p^a)
\\
=a p^{a-1}\sum_\ell p_{x_\ell\xi_\ell}
\\
+a(a-1)p^{a-2}\sum_\ell p_{x_\ell}p_{\xi_\ell}.
 \end{gathered}
 \tag{51}
\]
The coefficient of the last sum after adding \(i/2\) times (51) is
\(a(a-1)(1/(2i)+i/2)=0\). The rest is
\(a p^{a-1}(p_0+(i/2)\sum p_{x_\ell\xi_\ell})=a p^{a-1}p_s\).
Both terms in that parenthesis are necessary when \(p\) depends on the base point.

For the product, \(\{p^r,p^s\}=rs p^{r+s-2}\{p,p\}=0\). Formula (34) therefore gives
\[
r p^{r-1}p_s p^s+p^r s p^{s-1}p_s
=(r+s)p^{r+s-1}p_s.
\tag{52}
\]
Its principal symbol is \(p^{r+s}\). This symbolic calculation describes the pseudodifferential product on smooth inputs. Equality of unbounded spectral products also requires their domains, as the next exercise shows.

**Exercise 7.4 (which inverse product has full domain; advanced).** For \(r>0\), find the exact domains of \(P^rP^{-r}\) and \(P^{-r}P^r\). Show that \(H^{mr}\) is a proper subspace of \(L^2\), using the eigenbasis alone.

**Solution 7.4.** The bounded multiplier \(P^{-r}\) maps every \(u\in L^2\) into \(\mathcal D(P^r)\), since
\[
\sum_j\lambda_j^{2r}|\lambda_j^{-r}(u,\phi_j)|^2
=\|u\|_2^2.
\tag{53}
\]
Thus \(P^rP^{-r}\) is the identity on all \(L^2\). In the reverse product the first applied factor \(P^r\) requires \(u\in H^{mr}\), and the bounded second factor imposes no additional condition. Hence \(P^{-r}P^r\) is the identity restricted to \(H^{mr}\).

Choose distinct indices \(j_k\) with \(\lambda_{j_k}^r\geq2^k\), possible by (3), and put
\[
u=\sum_{k\geq1}\lambda_{j_k}^{-r}\phi_{j_k}.
\tag{54}
\]
Its squared coefficients sum to at most \(\sum4^{-k}<\infty\), so \(u\in L^2\). Its \(2r\)-moment is \(\sum1=\infty\), so \(u\notin H^{mr}\). This also proves that the two inverse identities have different actual domains.

**Exercise 7.5 (a second term at nonintegral order; advanced).** On the flat \(n\)-torus with \(n\geq2\), choose a positive Fourier multiplier whose high-frequency symbol is
\[
p_L(\xi)=|\xi|^m+c|\xi|^{m-1},
\qquad m>0,\quad c\in\mathbb R.
\tag{55}
\]
Small Fourier modes are assigned positive eigenvalues. Find the first two symbols of its spectral root and the first two terms of \(N_P(E)\), including the sign and coefficient. Justify the small remainder.

**Solution 7.5.** The principal symbol is \(p=|\xi|^m\); since there are no base derivatives, \(p_s=c|\xi|^{m-1}\). Formula (37) gives
\[
q=|\xi|,\qquad q_s=\frac cm.
\tag{56}
\]
Equivalently \((|\xi|^m+c|\xi|^{m-1})^{1/m}
=|\xi|+c/m+O(|\xi|^{-1})\), with all differentiated remainder estimates at high frequency.

The flow of \(q\) is translation at velocity \(\xi/|\xi|\). Full periodicity holds precisely on rays in integer directions: a return requires \(t\xi/|\xi|\in2\pi\mathbb Z^n\). These countably many rays have zero \(n\)-dimensional fiber measure when \(n\geq2\), by the bounded thin-box covering and countable exhaustion proved in Solution 7.5 of [Return times and spectral counting](return-times-and-spectral-counting.md). The classical multiplier construction in the local spectral-density lesson verifies the operator hypotheses. Thus (43) has a small remainder. The torus volume cancels the factor \((2\pi)^{-n}\), giving \(A_P=v_n\), the Euclidean unit ball volume. Polar coarea gives
\[
B_P
=\int_{\mathbb R^n}\delta(1-|\xi|^m)c|\xi|^{m-1}\,d\xi
=\frac{nc}{m}v_n.
\tag{57}
\]
The radial surface is \(r=1\), the delta contributes \(1/m\), and the sphere area is \(nv_n\). Consequently
\[
\begin{aligned}
N_P(E)&=v_nE^{n/m}\\
&\quad-\frac{nc}{m}v_nE^{(n-1)/m}
+o(E^{(n-1)/m}).
\end{aligned}
\tag{58}
\]
A positive \(c\) raises the eigenvalues and reduces the count, agreeing with the negative sign. Finitely many small-mode choices change \(N_P\) by \(O(1)\), which is smaller than \(E^{(n-1)/m}\). This example allows nonintegral \(m\); it does not invoke the differential parity cancellation in (47).

## References

The free article [ALNV, §7.3, Theorem 7.9] proves classical complex powers, with principal symbol \(p^z\), in an extended Weyl algebra. Its proof uses the uniform resolvent statements of §7.2 and the special holomorphic families of §7.1; the latter construction also invokes an external holomorphic cohomology result. For the real scalar powers needed here, Lemma 2.1 and (23)–(29) give a direct negative-axis construction from the stated composition, summation and elliptic prerequisites. Equations (30)–(36) additionally compute the exact subprincipal term and identify the spectral domains. [H, §1 and §5, Theorem 5.1] explains spectral rescaling through a positive root, but invokes a separate complex-power theorem for the root's classicality. Our root construction supplies that missing step before any rescaling is used. Neither comparison is a substitute for the parameter remainder estimates above.

- [ALNV] Bernd Ammann, Robert Lauter, Victor Nistor and András Vasy, “Complex powers and non-compact manifolds,” *Communications in Partial Differential Equations* 29 (2004), 671–705. [Freely accessible arXiv version](https://arxiv.org/abs/math/0211305v1), §7, especially §7.3, Theorem 7.9.
- [H] Lars Hörmander, “The spectral function of an elliptic operator,” *Acta Mathematica* 121 (1968), 193–218. [Full article](https://projecteuclid.org/journalArticle/Download?urlid=10.1007%2FBF02391913), §§1 and 5.
- [GS] Victor Guillemin and Shlomo Sternberg, [*Semi-classical Analysis*, freely accessible author text](https://people.math.harvard.edu/~shlomo/docs/Semi_Classical_Analysis_Start.pdf), Introduction §0.5, printed pages xi–xii. Its semiclassical notation is interpreted through the preceding classical wave-construction lesson.
