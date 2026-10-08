# Return times and spectral counting

*Written by GPT-6.1 Sol (OpenAI) and GPT-6 Astra (OpenAI). Self-checked by the writing AI. Original exposition: CC0.*

**Working question: How much information is lost by smoothing a counting staircase?** A smoothed count cannot directly see a jump at an eigenvalue. Positivity bounds what can lie in the short interval that smoothing averages. A longer interval without full returns permits a narrower spectral average. This gives a reason for the geometric hypothesis and for the order in which time localization and energy limits are taken.

The short-time wave kernel gives a smooth approximation to the spectral measure. To recover a count of eigenvalues, we need to control what smoothing has removed. Positivity supplies that control. A longer interval without a returning trajectory permits less smoothing and gives a smaller remainder.

The positive-window argument in Hörmander's spectral-function article [HS, Lemma 4.3 and Theorem 4.4], Wunsch's wave-trace discussion [W, Sections 7 and 9], and Ivrii's Tauberian and dynamical survey [I, Sections 2.1.3–2.1.4] identify the mechanisms used here. We prove the quantitative Tauberian comparison, its endpoint treatment, and the partition argument below, including the dependence on return time. The classical and semiclassical conventions are related explicitly after Theorem 5.1. Guillemin and Sternberg [GS] give further semiclassical context; the [DG] article provides the classical spectral setting. We use [Wave evolution and cotangent flow](wave-evolution-and-cotangent-flow.md) and [Local spectral density and the subprincipal correction](local-spectral-density-and-subprincipal-correction.md). Quantization, composition, adjoints, conic support and asymptotic summation are the scalar calculus of [Classical scalar symbols, summation and regularity](../providers/analysis/classical-scalar-calculus.md#finite-symbol-calculus).

More precisely, the wave lesson's Sections 1 and 6 provide the counting bound and the compact spatial-integration proof. [Qualified pullback, (R1)–(R8)](../providers/analysis/wavefront-qualified-pullback.md#qualified-pullback), and [transverse composition, (G1)–(G14)](../providers/analysis/transverse-composition-and-graph-operators.md#transverse-composition), supply the kernel operations used in Section 2. The preceding local coefficient lesson proves its full differentiated amplitude reduction in Section 4 and its real scalar coefficients in Sections 5–6. We also use the earlier [Euclidean measure/product proof](../providers/analysis/finite-derivative-l2.md#euclidean-products), [Fourier inversion](../providers/analysis/finite-derivative-l2.md#fourier-normalization), and [finite smooth partition construction](../providers/analysis/coordinate-inverses-and-integration.md#finite-partitions). 

Let \(X\) be compact, connected and without boundary, of dimension \(n\geq2\). Let \(P\) be a scalar classical elliptic operator of order one on half densities, self-adjoint on \(H^1\), with positive principal symbol \(p\) and subprincipal symbol \(p_s\). Initially assume \(P>0\). Section 6 removes this spectral positivity assumption.

Write \(\chi_t\) for the Hamiltonian flow of \(p\), and use \(E(t)=e^{-itP}\). In local coordinates the spectral function and its integral are
\[
e(x,x,\lambda)=\sum_{\lambda_j\leq\lambda}|\phi_j(x)|^2,
\qquad N(\lambda)=\sum_{\lambda_j\leq\lambda}1.
\tag{1}
\]
The diagonal is a density. The wave lesson proves its \(O(\lambda^n)\) bound, uniformly on \(X\), and the same bound for \(N\). One may consistently use \(<\lambda\) in (1). The arguments below apply to either endpoint convention, including at an eigenvalue.

<a id="counting-positive-window"></a>

## 1. A positive smoothing kernel

Fix a nonnegative Schwartz function \(\varphi\) such that
\[
\int_{\mathbb R}\varphi(s)\,ds=1,\qquad
\operatorname{supp}\widehat\varphi\subset(-1,1),\qquad
\varphi(s)\geq c_0>0\quad (|s|\leq\tfrac12).
\tag{2}
\]
Here \(\widehat f(t)=\int e^{-it\lambda}f(\lambda)\,d\lambda\). Such a function exists: take a nonzero, even, nonnegative \(\psi\in C_c^\infty(-1/4,1/4)\), let \(u=\mathcal F^{-1}\psi\), and normalize \(|u|^2\) to have integral one. Its Fourier support is contained in \([-1/2,1/2]\). For \(|s|\leq1/2\), the integral for \(u(s)\) is real and bounded below by
\[
(2\pi)^{-1}\cos(1/8)\int\psi>0.
\]
Integration by parts proves that \(u\) is Schwartz; the product and Fourier convolution rules prove the support assertion. We fix this kernel once for all dimensions. Its constants do not depend on \(P\).

For \(a>0\), put
\[
\varphi_a(s)=a^{-1}\varphi(s/a),\qquad
\widehat{\varphi_a}(t)=\widehat\varphi(at).
\tag{3}
\]
Thus convolution on the energy axis uses only wave times \(|t|<1/a\).

<a id="counting-tauberian"></a>

The quantitative comparison is Hörmander’s Tauberian lemma [H3, Lemma 17.5.6].

**Lemma 1.1 (quantitative removal of smoothing).** Let \(\mu\) be an increasing tempered function with \(\mu(0)=0\). Let \(\nu\) be the locally absolutely continuous representative of a function of locally bounded variation, with \(\nu(0)=0\). Suppose
\[
|d\nu(\tau)|\leq M_0(|\tau|+a_0)^{n-1}\,d\tau,
\qquad
|g(\tau)|\leq M_1(|\tau|+a_1)^\kappa,
\tag{4}
\]
where
\[
g=(d\mu-d\nu)*\varphi_a,\qquad
0\leq\kappa\leq n-1,\qquad a_0,a_1\geq a.
\]
The first bound in (4) makes \(d\nu\) absolutely continuous. The specified representative is equivalently \(\nu(\tau)=\int_0^\tau d\nu\), with an oriented integral; changing isolated point values is not allowed. Either monotone endpoint representative of \(\mu\) is allowed.
Then
\[
|\mu(\tau)-\nu(\tau)|
\leq C_{n,\kappa}
\left[
M_0a(|\tau|+a_0)^{n-1}
+M_1(|\tau|+a)(|\tau|+a_1)^\kappa
\right].
\tag{5}
\]
The constant depends only on \(n,\kappa\) and the fixed kernel (2). If \(g\) is bounded and integrable, then
\[
\limsup_{\tau\to+\infty}
\tau^{1-n}|\mu(\tau)-\nu(\tau)|
\leq C_n aM_0.
\tag{6}
\]

<a id="counting-stieltjes-measure"></a>

**Proof.** We first justify the measure and growth facts, including their pointwise meaning. An increasing function has finite one-sided limits on every bounded interval. Its jumps are countable: on a fixed bounded interval there are only finitely many jumps of size at least $1/k$, since their sum is bounded by the total increment; take the countable union over $k$ and intervals. Replace it temporarily by its right-continuous representative $F$, equal to it almost everywhere. Put $\alpha=F(-\infty)$, $\beta=F(+\infty)$, allowing infinite endpoints. For $s\in(\alpha,\beta)$ define
\[
 q(s)=\inf\{x:F(x)>s\}.
\]
This is a finite, measurable, increasing function of $s$. Indeed its strict sublevel sets are intervals, as follows directly by testing whether some $x<t$ has $F(x)>s$. Push Lebesgue measure on $(\alpha,\beta)$ forward by $q$. For $a<b$, right continuity gives
\[
 \bigl|\{s:a<q(s)\le b\}\bigr|=F(b)-F(a).
\]
The possible ambiguity at $s=F(a),F(b)$ has measure zero: $s>F(a)$ forces $q(s)>a$, $s<F(a)$ forces $q(s)\le a$, and the analogous statements hold at $b$. Thus this pushforward is locally finite. The case $\alpha=\beta$ gives the zero measure. Write it as $m$. For a smooth test supported in $(a,b)$, use $F(x)=F(a)+m((a,x])$ and the product-integration theorem to obtain
\[
 -\int F(x)\psi'(x)\,dx=\int\psi(s)\,dm(s).
\]
This proves $d\mu=m\ge0$ as distributions. Its closed-interval mass is $m([a,b])=F(b)-F(a-)$, which bounds the increment between any allowed endpoint representatives.

<a id="counting-unsmoothing"></a>

Temperedness also gives the polynomial growth required below. For $x>1$, test $\mu$ against a fixed nonnegative unit-integral smooth bump translated into $(x,x+1)$. Monotonicity and $\mu(0)=0$ bound $0\le\mu(x)$ by this pairing; the tempered test estimate bounds the pairing by $C(1+x)^N$. Translating the bump into $(x-1,x)$ gives the corresponding bound for $-\mu(x)$ when $x<-1$. The measure mass on a unit interval is bounded by the increments on a slightly larger interval, hence has polynomial growth as well. The bound on $\nu'$ gives the same property for $\nu$ and $d\nu$. Consequently all Schwartz convolutions and differentiations below are justified by absolute majorants and the distributional integration-by-parts identity. From (2),
\[
\frac{c_0}{a}
d\mu([\tau-a/2,\tau+a/2])
\leq (d\mu*\varphi_a)(\tau)
\leq |g(\tau)|+(|d\nu|*\varphi_a)(\tau).
\tag{7}
\]
The last convolution is bounded by
\[
M_0\int\varphi(s)(|\tau-as|+a_0)^{n-1}\,ds
\leq C_nM_0(|\tau|+a_0)^{n-1},
\tag{8}
\]
because \(a\leq a_0\) and every moment of \(\varphi\) is finite.

Divide the interval between \(\tau\) and \(\tau-as\) into at most \(|s|+1\) intervals of length at most \(a\). Applying (7) at their centers bounds the increment by
\[
|\mu(\tau)-\mu(\tau-as)|
\leq Ca(|s|+1)
\left[
M_0(|\tau|+a_0+a|s|)^{n-1}
+M_1(|\tau|+a_1+a|s|)^\kappa
\right].
\tag{9}
\]
Closed interval masses bound these increments for both the left and the right representative of an increasing function. Values chosen between its one-sided limits satisfy the same estimate.

Integrate (9) against \(\varphi(s)\). Using \(a\leq a_0,a_1\) again gives
\[
|\mu-\mu*\varphi_a|(\tau)
\leq Ca
\left[
M_0(|\tau|+a_0)^{n-1}
+M_1(|\tau|+a_1)^\kappa
\right].
\tag{10}
\]
Direct integration of the first bound in (4), using the specified absolutely continuous representative of \(\nu\), gives the corresponding estimate for \(\nu\), with the \(M_1\) term omitted.

Set \(w=\mu-\nu\). Since \((w*\varphi_a)'=g\),
\[
|(w*\varphi_a)(\tau)-(w*\varphi_a)(0)|
\leq M_1|\tau|(|\tau|+a_1)^\kappa.
\tag{11}
\]
All convolutions are well defined: the functions and measures have polynomial growth and the kernel is Schwartz. The estimates also justify differentiation. As \(w(0)=0\), applying (10) and its \(\nu\) counterpart at zero bounds \(|(w*\varphi_a)(0)|\). Applying them at \(\tau\), and then (11), proves (5). Terms evaluated at zero are bounded by the corresponding displayed terms at \(\tau\).

For (6), take \(\kappa=0\) and \(M_1=\|g\|_\infty\) in the unsmoothing estimate (10). In place of (11), use the sharper bound
\[
|(w*\varphi_a)(\tau)-(w*\varphi_a)(0)|
\leq \|g\|_1.
\tag{12}
\]
Consequently
\[
|w(\tau)|\leq
CaM_0(|\tau|+a_0)^{n-1}
+Ca\|g\|_\infty
+C\!\left[aM_0a_0^{n-1}+a\|g\|_\infty+\|g\|_1\right].
\tag{13}
\]
Multiply by \(\tau^{1-n}\) and let \(\tau\) tend to infinity. The bracket and bounded-error terms disappear because \(n\geq2\), proving (6). In particular, the integrability in (12) removes a possible linear error in dimension two. ∎

The same proof is uniform over a compact family when \(a,a_0\) stay in bounded positive ranges, \(\|g\|_\infty+\|g\|_1\) is uniformly bounded, and the leading \(M_0\)'s have a positive lower bound. The constant multiplying \(aM_0\) in (6) remains dimensional; only the energy threshold depends on the family.

<a id="counting-return-geometry"></a>

## 2. Which returns a kernel can see

Define the first base return and the first full period by
\[
\begin{aligned}
T(x)&=\inf\{t>0:\ \chi_t(x,\eta)=(x,\xi)
                  \text{ for some }\eta\ne0,\xi\},\\
T_*(x,\eta)&=\inf\{t>0:\ \chi_t(x,\eta)=(x,\eta)\}.
\end{aligned}
\tag{14}
\]
An infimum over the empty set is \(+\infty\). The second function is homogeneous of degree zero. Positive homogeneity lets us normalize every initial covector to \(p=1\), a compact hypersurface.

**Lemma 2.1.** The functions in (14) are lower semicontinuous and have a common positive lower bound. The function
\[
f(x,\eta)=T_*(x,\eta)^{-1},\qquad (+\infty)^{-1}=0,
\tag{15}
\]
is bounded, upper semicontinuous and homogeneous of degree zero.

**Proof.** Euler's identity gives \(\eta\cdot p_\eta=p>0\). The base velocity \(p_\eta\) therefore never vanishes on \(p=1\). The compact-coordinate Taylor argument in the wave lesson gives a uniform deleted interval about zero without any base return. Let its positive radius be \(\delta\). A full return is a base return, so both functions are at least \(\delta\).

For lower semicontinuity of \(T\), let \(x_j\to x\) and suppose the lower limit of \(T(x_j)\) is finite. Pass to a subsequence realizing that lower limit. Choose actual return times within \(1/j\) of the corresponding infima and normalize their initial covectors to \(p=1\). Compactness gives a convergent subsequence of covectors and times. The limiting time is at least \(\delta\). Continuity of the flow makes it a base return at \(x\); hence \(T(x)\leq\liminf T(x_j)\). If the lower limit is infinite there is nothing to prove.

The same argument with convergent normalized initial covectors proves the assertion for \(T_*\), now requiring equality of both final coordinates. Taking reciprocals of positive extended-valued lower semicontinuous functions proves (15). ∎

<a id="counting-diagonal-trace"></a>

For $B\in\Psi^0_{\mathrm{cl}}$, the diagonal of \(E(t)B\) has wavefront directions of the form
\[
(t,x;\,-p(x,\eta),\,\xi-\eta),
\qquad \chi_t(x,\eta)=(x,\xi),\quad (x,\eta)\in\operatorname{WF}(B).
\tag{16}
\]
Its spatial trace can retain only the directions with \(\xi=\eta\). The composition proof applies to the wave graph and the pseudodifferential identity relation: matching is unique and transverse, with proper support on each compact time interval and normalized energy set. It also retains the input conic support of $B$. The diagonal conormal has time component zero, whereas $-p\ne0$, so the qualified-pullback theorem constructs the diagonal restriction and sends $(\tau,\xi,-\eta)$ to $(\tau,\xi-\eta)$. Finally the compact integration proof in the wave lesson, Section 6, evaluates the localized Fourier transform at zero spatial frequency. It keeps only $\xi-\eta=0$, proving the trace assertion. This last step uses the general wavefront integration rule; no positive-excess composition formula is assumed at a periodic orbit.

The distributional trace is exactly the Fourier transform of its spectral measure. To check this without an unjustified pointwise kernel sum, pair time against $h\in C_c^\infty$. Its spectral multiplier is $\widehat h(P)$, rapidly decreasing on the spectrum. The earlier elliptic Sobolev estimates bound every fixed derivative of both $\phi_k$ and $B^*\phi_k$ by a fixed power of $1+\lambda_k$. The $O(\lambda^n)$ count and arbitrary rapid decrease therefore make
\[
 \sum_k\widehat h(\lambda_k)\phi_k(x)
                   \overline{B^*\phi_k(y)}
\]
converge uniformly with every fixed list of $x,y$ derivatives. Pairing against smooth spatial tests identifies this kernel with $\widehat h(P)B$ by the spectral expansion. Its diagonal can thus be integrated term by term, giving $\sum_k\widehat h(\lambda_k)\langle B\phi_k,\phi_k\rangle$; this series is absolutely convergent also from $|\langle B\phi_k,\phi_k\rangle|\le\|B\|$. This proves the asserted distributional trace identity directly. For $B=I$ the identical argument at a fixed $x$, using the local $O(\lambda^n)$ bound, identifies the diagonal Fourier transform with $de(x,x,\lambda)$.

For \(B=I\), (16) makes the diagonal smooth when \(0<|t|<T(x)\). For a trace localized to a conic set \(\Gamma\), it makes the trace smooth when
\[
0<|t|<\inf_\Gamma T_*.
\tag{17}
\]
Negative time returns are equivalent to positive ones by reversing the flow. Smoothness holds jointly on open sets where the displayed return conditions are excluded. These are inclusions: cancellation can make a trace smooth even at some periods.

<a id="counting-local-remainder"></a>

## 3. The local counting bound

For a homogeneous \(g\), retain the energy density notation
\[
I_g(x,\lambda)=\int_{p(x,\eta)<\lambda}g(x,\eta)\,d\eta.
\]
In particular \(I_1(x,\lambda)=\lambda^nI_1(x,1)\) and \(I_{p_s}(x,\lambda)=\lambda^nI_{p_s}(x,1)\). Define
\[
V(x,\lambda)=(2\pi)^{-n}
\left[I_1(x,\lambda)-\partial_\lambda I_{p_s}(x,\lambda)\right].
\tag{18}
\]
Both \(e\) and \(V\) are densities, so their difference divided by the positive density \(I_1(x,1)\) is a scalar.

The base-return estimate is Hörmander’s local spectral bound [H4, Theorem 29.1.4].

**Theorem 3.1 (base returns bound the local remainder).** There is a constant \(C_n\), depending only on dimension, such that
\[
\limsup_{\lambda\to+\infty}
\lambda^{1-n}
\frac{|e(x,x,\lambda)-V(x,\lambda)|}{I_1(x,1)}
\leq \frac{C_n}{T(x)}.
\tag{19}
\]
If \(J:X\to(0,\infty)\) is continuous and \(J(x)<T(x)\) everywhere, then, for all sufficiently large \(\lambda\), uniformly on \(X\),
\[
\lambda^{1-n}
\frac{|e(x,x,\lambda)-V(x,\lambda)|}{I_1(x,1)}
\leq \frac{C_n}{J(x)}.
\tag{20}
\]
One dimensional constant may be enlarged to serve both statements.

**Proof.** Fix \(x_0\) and \(0<L<T(x_0)\). Lower semicontinuity gives a neighborhood of \(x_0\) with no base returns at \(0<|t|\leq L\), after shrinking the neighborhood or slightly increasing \(L\) within the strict gap. Choose a spatial cutoff equal to one near \(x_0\).

The local coefficient theorem supplies a normalized primitive \(A(x,0)=0\), whose derivative has the leading term
\[
\begin{aligned}
\partial_\lambda A(x,\lambda)
&=n(2\pi)^{-n}I_1(x,1)\lambda^{n-1}\\
&\quad+O(\lambda^{n-2}).
\end{aligned}
\tag{21}
\]
Also \(A-V=O(\lambda^{n-2})\) for \(n\geq3\), and \(A-V=O(\log(2+\lambda))\) for \(n=2\). In either case
\[
A(x,\lambda)-V(x,\lambda)=o(\lambda^{n-1}).
\tag{22}
\]
Here is an exact choice of the model, including its smooth residual. Fix one even real $\rho\in C_c^\infty$, equal to one near zero and supported inside the common small-time construction. Define
\[
 \begin{aligned}
 a(x,\lambda)&=\frac1{2\pi}\int e^{it\lambda}\rho(t)K(t,x)\,dt,\\
 A(x,\lambda)&=\int_0^\lambda a(x,s)\,ds.
 \end{aligned}
\]
The first integral is a compactly supported distribution paired against the exponential. Its Fourier inversion is exactly $\rho K$. Section 4 of the local coefficient lesson proves that its oscillatory part is a classical symbol with every differentiated remainder, and its smooth time residual contributes a Schwartz symbol. Thus this exact choice has (21)–(22); it is not merely a formal coefficient series. The symmetry $K(-t,x)=\overline{K(t,x)}$ and even real $\rho$ make $a$ and $A$ real. The negative-energy derivative decreases rapidly by that lesson's reduced-amplitude estimate: before reduction the amplitude vanishes at large negative frequency, and in its exact Fourier convolution the time frequency must then be comparable to $|\lambda|$ or larger. Its arbitrary rapid decrease absorbs every derivative and polynomial factor. These estimates hold uniformly with all base derivatives on the finite coordinate cover.

Work in a half-density coordinate frame and set
\[
\mu(\lambda)=e(x_0,x_0,\lambda),\quad
\nu(\lambda)=A(x_0,\lambda),\quad
M_0=n(2\pi)^{-n}I_1(x_0,1).
\]
Since \(P>0\), both cumulative functions vanish at zero. The first is increasing and tempered. From (21), rapid decrease at negative energies and smoothness on bounded intervals, one can choose \(a_0\geq a=1/L\) such that
\[
|\nu'(\lambda)|\leq M_0(|\lambda|+a_0)^{n-1}.
\tag{23}
\]
To justify keeping precisely this \(M_0\), the \(O(\lambda^{n-2})\) term at positive infinity is absorbed by increasing \(a_0\) in the binomial expansion on the right. Bounded intervals and the negative tail are then absorbed by another increase. The assumption \(n\geq2\) is used here.

The Fourier transforms of $d\mu$ and $d\nu$ are exactly $K(t,x_0)$ and $\rho(t)K(t,x_0)$. Their difference is $(1-\rho)K$, identically zero near zero time and smooth at all other times $|t|<L$ by (16). Multiplication by $\widehat\varphi(at)$ gives a smooth compactly supported function. Repeated integration by parts bounds every power of the energy variable in its inverse transform, and differentiating that transform only inserts powers of the bounded time variable. Fourier inversion therefore gives
\[
g=(d\mu-d\nu)*\varphi_a\in\mathcal S(\mathbb R).
\tag{24}
\]
Applying (6), then (22), gives the left side of (19) at most \(C_n/L\). Let \(L\uparrow T(x_0)\). If \(T(x_0)=\infty\), take \(L\) arbitrarily large. This proves (19).

For (20), fix $x_0$ and choose $L_{x_0}$ strictly between $J(x_0)$ and $T(x_0)$. Continuity of $J$ and lower semicontinuity of $T$ give a neighborhood on which $J<L_{x_0}<T$. Shrink its closure inside that neighborhood. A finite such cover of $X$ gives compact time-base sets, away from zero, on which the kernel is smooth and all needed time derivatives are bounded. The closed time support of $\widehat\varphi(t/J(x))$ is inside those sets, while $1-\rho$ eliminates zero time exactly. Time differentiation of the cutoff gives only powers of $1/J(x)$, bounded since $J$ has a positive minimum. Hence the compactly supported functions just constructed have uniformly bounded time derivatives and support. In particular, integration by parts twice gives a uniform bound $|g_x(\lambda)|\le C(1+|\lambda|)^{-2}$, which controls both its supremum and $L^1$ norm. No base derivative of the merely continuous function $J$ is used.

The quantities \(a(x)=1/J(x)\) range in a compact positive interval. One can choose a common \(a_0\) in (23); \(I_1(x,1)\) has a positive lower bound in each fixed coordinate-density trivialization. The uniform form of (13) and uniform (22) give (20) after enlarging the dimensional constant. All bounded errors vanish uniformly on division by \(\lambda^{n-1}\); the threshold may depend on \(P\) and \(J\). No derivative of \(J\) is needed: only time derivatives of its cutoff enter this argument. ∎

<a id="counting-positive-partition"></a>

## 4. A positive partition in cotangent space

For global counting we can localize directions as well as base points. Positivity must survive that localization.

**Lemma 4.1 (normalizing a positive operator partition).** Let finitely many open cones \(\Gamma_j\) cover \(T^*X\setminus0\). There exist scalar \(C_j\in\Psi^0_{\mathrm{cl}}\), microlocally supported in \(\Gamma_j\), such that
\[
B_j=C_jC_j^*\geq0,\qquad
\sum_j B_j=I+R,\qquad R\in\Psi^{-\infty}.
\tag{25}
\]
Their principal symbols \(b_j\) are nonnegative and sum to one. Their subprincipal symbols \(b_{j,s}\) sum to zero.

**Proof.** On the compact level \(p=1\), use the earlier finite bump construction to choose smooth real functions \(\beta_j\) with support compactly inside the corresponding cones and
\[
\sum_j\beta_j^2=1.
\tag{26}
\]
For example normalize a finite subordinate nonnegative partition by the square root of the sum of its squares. Extend homogeneously and use a cutoff at small frequency. The scalar quantization and conic calculus give \(A_j\) with principal symbol \(\beta_j\) and \(\operatorname{WF}(A_j)\subset\Gamma_j\). Set \(S=\sum_jA_jA_j^*\). It is self-adjoint and \(S-I\in\Psi^{-1}\).

We construct \(Q=I+\Psi^{-1}\) with
\[
QSQ^*=I\quad\bmod\Psi^{-\infty}.
\tag{27}
\]
Start with \(Q_0=I\). Suppose a finite construction has error \(Q_{r-1}SQ_{r-1}^*-I\) of order \(-r\). Its leading homogeneous symbol \(h_{-r}\) is real, since the error is self-adjoint. Quantize a correction \(D_r\) of order \(-r\) with principal symbol \(-h_{-r}/2\), and put \(Q_r=Q_{r-1}+D_r\). The new error differs from the old one by
\[
D_rSQ_{r-1}^*+Q_{r-1}SD_r^*+D_rSD_r^*.
\tag{28}
\]
The first two terms have combined leading symbol \(-h_{-r}\), because the order-zero principal symbols of \(S,Q_{r-1}\) are one. The last term has order \(-2r\leq-r-1\). Thus the new error has order \(-r-1\).

Apply the existing asymptotic summation theorem to the successive corrections. The resulting classical \(Q\) satisfies \(Q-Q_r\in\Psi^{-r-1}\) at every stage, so (27) follows from composition and the smooth-kernel ideal. Set \(C_j=QA_j\). The conic product rule preserves their microlocal supports, and (27) proves (25). Principal symbols are \(b_j=\beta_j^2\). Principal and subprincipal symbols are additive; those of \(I+R\) are one and zero. This proves both sum assertions. The recursive construction needs no convergence of an operator power series. ∎

<a id="counting-projected-traces"></a>

For these operators define positive cumulative measures
\[
\mu_j(\lambda)=\operatorname{Tr}(\Pi_\lambda B_j)
=\sum_{\lambda_k\leq\lambda}\|C_j^*\phi_k\|^2,
\tag{29}
\]
where \(\Pi_\lambda\) is the spectral projection. They are increasing, vanish at zero and have \(O(\lambda^n)\) growth. The last assertion follows from boundedness of \(C_j^*\) and the bound for \(N\).

We also need the smoothing error in (25) to contribute only a bounded trace. A direct spectral proof is useful. For any integer \(M>n\), \(R(P+c)^M\) is bounded for a positive shift \(c\), because \(R\) is smoothing. Thus
\[
|\langle R\phi_k,\phi_k\rangle|
\leq C_M(\lambda_k+c)^{-M}.
\tag{30}
\]
The \(O(\lambda^n)\) counting bound makes the series on the right summable: a dyadic shell contributes \(O(2^{(n-M)l})\). It follows that
\[
|\operatorname{Tr}(\Pi_\lambda R)|\leq C
\quad\hbox{uniformly in }\lambda.
\tag{31}
\]

<a id="counting-global-remainder"></a>

## 5. The global remainder and periodic covectors

Write \(dz=dx\,d\eta\) for symplectic volume and set
\[
\mathcal V(\lambda)=(2\pi)^{-n}
\left[
\int_{p<\lambda}dz
-\partial_\lambda\int_{p<\lambda}p_s\,dz
\right].
\tag{32}
\]

The full-period estimate and its measure-zero consequence are Hörmander’s global spectral bound [H4, Theorem 29.1.5 and Corollary 29.1.6].

**Theorem 5.1 (full periods bound the global remainder).** There is a dimensional constant \(C_n\) such that
\[
\limsup_{\lambda\to+\infty}
\lambda^{1-n}|N(\lambda)-\mathcal V(\lambda)|
\leq C_n\int_{p<1}T_*^{-1}\,dz.
\tag{33}
\]
In particular, if the periodic covectors form a set of symplectic measure zero in \(T^*X\setminus0\), then
\[
N(\lambda)=\mathcal V(\lambda)+o(\lambda^{n-1}).
\tag{34}
\]

**Proof.** First choose cones \(\Gamma_j\) and positive numbers \(L_j\) with
\[
L_j<T_*(z)\quad(z\in\Gamma_j).
\tag{35}
\]
Use Lemma 4.1 with supports strictly inside these cones. The trace of \(E(t)B_j\) is smooth for \(0<|t|\leq L_j\). Choose the same kind of even real small-time cutoff $\rho$ as above and define $\nu_j'$ to be the exact inverse Fourier transform of $\rho(t)\operatorname{Tr}(E(t)B_j)$, with $\nu_j(0)=0$. The local coefficient theorem and compact spatial integration give a real function \(\nu_j\) with expansion
\[
\nu_j(\lambda)=(2\pi)^{-n}
\left[
\int_{p<\lambda}(b_j+b_{j,s})\,dz
-\partial_\lambda\int_{p<\lambda}
\left(p_sb_j+\frac i2\{b_j,p\}\right)\,dz
\right]+o(\lambda^{n-1}).
\tag{36}
\]
Here \(\{b,p\}=H_bp=-H_pb\). The integrated bracket vanishes, by the Hamiltonian divergence calculation in the local coefficient lesson. Reality also follows directly from
\(\operatorname{Tr}(E(-t)B_j)=\overline{\operatorname{Tr}(E(t)B_j)}\) and an even real time cutoff. Its derivative is rapidly decreasing at negative energy and has leading positive coefficient
\[
M_{0,j}=n(2\pi)^{-n}\int_{p<1}b_j\,dz.
\tag{37}
\]
Discard identically zero partition functions; the remaining integrals are positive. As in (23), choose \(a_{0,j}\) to bound \(|\nu_j'|\) with exactly \(M_{0,j}\).

By the spectral identity proved after (16), the Fourier transform of $d\mu_j-d\nu_j$ is exactly $(1-\rho(t))\operatorname{Tr}(E(t)B_j)$. By (17), multiplying it by the cutoff \(\widehat\varphi(t/L_j)\) gives a smooth compactly supported function. Its inverse transform is Schwartz. Lemma 1.1 with \(a=1/L_j\) gives
\[
\limsup_{\lambda\to+\infty}
\lambda^{1-n}|\mu_j(\lambda)-\nu_j(\lambda)|
\leq \frac{C_n}{L_j}\int_{p<1}b_j\,dz.
\tag{38}
\]

By (25) and (31), \(N=\sum_j\mu_j+O(1)\). In (36) the principal symbols sum to one and the subprincipal symbols to zero. The bracket terms either cancel individually after integration or sum to \(\{1,p\}=0\). The remainders are \(o(\lambda^{n-1})\), also in dimension two. Therefore
\[
\limsup_{\lambda\to+\infty}
\lambda^{1-n}|N-\mathcal V|
\leq C_n\int_{p<1}\sum_j b_jL_j^{-1}\,dz.
\tag{39}
\]

<a id="counting-period-majorants"></a>

It remains to approximate \(f=T_*^{-1}\) from above. This step must respect its possible discontinuities. Give the compact hypersurface \(Z=\{p=1\}\) a metric \(d\), and define
\[
f_m(z)=\sup_{w\in Z}\bigl(f(w)-m\,d(z,w)\bigr).
\tag{40}
\]
These functions are \(m\)-Lipschitz, satisfy \(f\leq f_m\leq\sup f\), and decrease pointwise to \(f\). For the last assertion choose points within \(1/m\) of the supremum. Their distance from \(z\) tends to zero, since \(f\) is bounded; upper semicontinuity of \(f\) bounds the upper limit by \(f(z)\). The reverse bound follows by taking \(w=z\).

Fix \(m\) and \(\varepsilon>0\). Cover \(Z\) by open sets so small that the oscillation of \(f_m\) on each is at most \(\varepsilon\), and use smaller supports for a subordinate square partition. Extend the sets conically. For each set let
\[
\gamma_j=\sup_{\Gamma_j\cap Z}f+\varepsilon,
\qquad L_j=\gamma_j^{-1}.
\tag{41}
\]
Then (35) holds. If \(z\) belongs to the support of \(b_j\), then
\(\gamma_j\leq f_m(z)+2\varepsilon\). Since \(\sum_jb_j=1\),
\[
\sum_j b_j(z)L_j^{-1}\leq f_m(z)+2\varepsilon.
\tag{42}
\]
Extend this inequality radially to \(0<p<1\). Combining (39) and (42), then sending \(\varepsilon\) to zero and \(m\) to infinity, proves (33) by dominated convergence. The sublevel volume is finite; all functions are bounded by a fixed constant. The zero section has zero volume.

Finally \(f\) is zero at every nonperiodic covector and is bounded. Under the stated measure-zero hypothesis its integral is zero. Equation (33) then gives (34). The usual equivalent energy-surface formulation follows from homogeneity: on each compact cotangent chart, write $\eta=r\omega/p(x,\omega)$ with $p=1$ at $r=1$. The change-of-variables and coarea proofs give a positive smooth angular density times $r^{n-1}dr$. The periodic set is conic because the degree-one Hamiltonian flow commutes with positive fiber dilation. Its measure on any annulus therefore vanishes exactly when its natural energy-surface measure vanishes. This justifies the comparison with the energy-surface hypothesis in [I]. ∎

<a id="counting-semiclassical-scaling"></a>

**The semiclassical scaling and the dynamical hypothesis.** To compare this theorem with [I], put \(h=\lambda^{-1}\) and \(P_h=hP\), in a fixed compact cotangent energy annulus. The semiclassical left symbol of \(P_h\) is
\(p+h p_0+h^2p_{-1}+\cdots\): this follows by replacing the classical frequency by \(\xi/h\) in the symbol of \(hP\). The principal Hamiltonian is still \(p\), its semiclassical subprincipal coefficient is \(p_s\), and
\[
e^{-itP_h/h}=e^{-itP},\qquad
N_{P_h}(1)=N_P(h^{-1}).
\]
The symbol comparison is asserted on this fixed annulus, away from zero covectors; no uniform classical expansion through the zero section is assumed. The displayed group and spectral-count identities are exact. Thus the physical return time is unchanged. Homogeneity in (32) gives
\[
\mathcal V(h^{-1})=(2\pi)^{-n}
 \left[h^{-n}\int_{p<1}1\,dz
       -n h^{1-n}\int_{p<1}p_s\,dz\right].
\]
Equation (34) is consequently a remainder \(o(h^{1-n})\) at fixed semiclassical energy, with the same two coefficients. A fixed bounded classical spectral interval contains only finitely many eigenvalues by the earlier counting bound, so its contribution is $O(1)$; a smooth remainder in a localization has bounded projected trace by (30)–(31). Ivrii uses the opposite sign in its evolution convention, which reverses the flow direction but leaves these return times and measure-zero conditions unchanged.

The local statement in [I, Theorem 2.1.12] requires negligible directions that return to the same base point. Its global statement requires negligible periodic phase points. Our distinction between \(T(x)\) and \(T_*(x,\eta)\) is exactly this distinction, and (25)–(42) prove the full-period version without replacing it by a condition on projected paths. The global error constant integrates \(T_*^{-1}\); the local one retains \(T(x)^{-1}\). A fixed short-time convolution alone gives neither improved remainder.

The leading local remainder in [HS] and the leading wave-trace argument in [W, Section 7] use positive spectral windows. Full periodic covectors enter the spatial trace in [W, Section 9] and [DG]. The logarithmic or power improvements discussed in [I, Sections 2.1.3–2.1.4] use times growing with the reciprocal semiclassical parameter and require control of long-time flow derivatives. Equations (33)–(34) use fixed finite times; no such additional long-time hypothesis is needed.

The two return functions answer different geometric questions. A trajectory may revisit its starting point with a different covector. That revisit can affect a local diagonal while disappearing under the spatial trace, which requires the difference \(\xi-\eta\) in (16) to be zero. The refinement in (33) retains precisely this distinction.

<a id="counting-spectral-shift"></a>

## 6. Shifting a lower-bounded operator

**Proposition 6.1.** Theorems 3.1 and 5.1 remain valid when \(P\) merely has a lower bound, with the same principal-symbol return times and the same displayed coefficient formulas.

**Proof.** Choose \(c\) such that \(P+c>0\). Its principal symbol is still \(p\), its subprincipal symbol is \(p_s+c\), and its Hamiltonian flow is unchanged. Its spectral count satisfies
\[
N_{P+c}(\lambda+c)=N_P(\lambda),
\]
and the diagonal satisfies the identical energy translation. Homogeneity and Taylor's formula give
\[
\begin{aligned}
I_1(\lambda+c)&=I_1(\lambda)+c\partial_\lambda I_1(\lambda)
                       +O(\lambda^{n-2}),\\
\partial_\lambda I_{p_s+c}(\lambda+c)
 &=\partial_\lambda I_{p_s}(\lambda)
   +c\partial_\lambda I_1(\lambda)+O(\lambda^{n-2}).
\end{aligned}
\tag{43}
\]
The terms involving \(c\partial_\lambda I_1\) cancel in (18). The same calculation after spatial integration applies to (32). The remaining error is \(o(\lambda^{n-1})\) in every \(n\geq2\), uniformly locally and globally. Also \((\lambda+c)^{1-n}/\lambda^{1-n}\to1\). Applying the positive-operator conclusions at energy \(\lambda+c\) proves the limsup statements and (34). Their uniform versions follow with the enlarged dimensional constant already allowed in (20). The wave lesson proves the needed lower bound from ellipticity and positivity of \(p\). ∎

### Use the conclusion

Use the positive kernel to bound a short spectral interval before extracting the global remainder. Keep localized return conditions, full periodic covectors and the lower-bounded spectral shift separate.

<a id="counting-solutions"></a>

## 7. Exercises and complete solutions

**Exercise 7.1 (a smoothing window; introductory).** In the construction of (2), verify the Fourier support and the positive lower bound on \([-1/2,1/2]\). Which time interval can influence convolution by \(\varphi_a\)?

**Solution 7.1.** With the stated Fourier convention,
\[
\widehat{|u|^2}=(2\pi)^{-1}\psi*\overline{\psi(-\,\cdot)}.
\]
Its support lies in the difference of two copies of \([-1/4,1/4]\), hence in \([-1/2,1/2]\). Normalization does not change support. Evenness makes \(u(s)=(2\pi)^{-1}\int\cos(s\xi)\psi(\xi)\,d\xi\). On the indicated interval \(|s\xi|\leq1/8\), so this is at least the positive bound given above. Squaring and dividing by \(\int|u|^2>0\) gives \(c_0\). Formula (3) shows that only \(|t|<1/a\) can contribute; this particular kernel actually has support within the smaller closed interval \(|t|\leq1/(2a)\). The larger interval is the convenient uniform window used in the proof.

**Exercise 7.2 (why two hypotheses matter; intermediate).** Give one example showing why the anchor at zero cannot be omitted from Lemma 1.1, and another showing why monotonicity cannot be omitted, even when the smoothed derivative difference is identically zero.

**Solution 7.2.** Let \(\mu=C\ne0\) and \(\nu=0\). Then both derivatives and their smoothed difference vanish, so (4) holds with \(M_0=M_1=0\), but (5) would falsely say \(|C|\leq0\). Here only the anchor fails.

For the second example let \(\mu(\lambda)=\sin(L\lambda)\), \(\nu=0\), and choose \(aL>1\). Both functions vanish at zero and are tempered; \(\mu\) is not increasing. Since \(\widehat\varphi(aL)=\widehat\varphi(-aL)=0\),
\[
(d\mu)*\varphi_a
=L\cos(L\lambda)*\varphi_a=0.
\]
Again \(M_0=M_1=0\) would give a false conclusion. A positive derivative measure was used in (7) to control unsmoothed mass; a signed oscillation can cancel completely under this convolution.

The representative condition on \(\nu\) is also essential for a pointwise conclusion. The function equal to one at every nonzero point and zero at zero has distributional derivative zero and satisfies the anchor, but is not its absolutely continuous representative. With \(\mu=0\) it would contradict (5) if arbitrary point values were permitted. The prescribed integral representative of that derivative is instead identically zero. The smooth spectral primitives in Sections 3 and 5 already satisfy this condition.

**Exercise 7.3 (the first normalization correction; intermediate).** Suppose \(S=I+R_1\), where \(S=S^*\), \(R_1\in\Psi^{-1}_{\mathrm{cl}}\), and the principal order-minus-one symbol of \(R_1\) is \(r_{-1}\). Find a first correction \(Q_1=I+D_1\) making \(Q_1SQ_1^*-I\) of order \(-2\). Explain why summing the normalized positive operators makes their subprincipal symbols add to zero.

**Solution 7.3.** The symbol \(r_{-1}\) is real. Choose \(D_1\in\Psi^{-1}_{\mathrm{cl}}\) with principal symbol \(-r_{-1}/2\). Expanding,
\[
(I+D_1)S(I+D_1)^*-I
=R_1+D_1+D_1^*+\Psi^{-2}.
\]
The three order-minus-one principal symbols sum to
\(r_{-1}-r_{-1}/2-r_{-1}/2=0\). Thus the error is of order \(-2\), irrespective of the chosen lower terms of \(D_1\). Repeating this cancellation and applying asymptotic summation gives (27). For \(B_j=C_jC_j^*\), the identity \(\sum_j B_j=I+\Psi^{-\infty}\) implies that its order-zero principal symbol is one and its order-minus-one subprincipal symbol is zero. Linearity of both symbol assignments gives \(\sum b_j=1\) and \(\sum b_{j,s}=0\). Positivity alone would not give the second identity; normalization to all symbol orders does.

**Exercise 7.4 (large jumps at the second scale; advanced).** Consider the abstract positive counting function
\[
\mu(\lambda)=
\begin{cases}\lfloor\lambda\rfloor^n,&\lambda\geq0,\\0,&\lambda<0.\end{cases}
\]
Show that no continuous function \(F\) can satisfy \(\mu-F=o(\lambda^{n-1})\) on the entire positive axis. Explain the relevance of the endpoint convention.

**Solution 7.4.** At a positive integer \(k\), the jump is
\[
J_k=k^n-(k-1)^n=nk^{n-1}+O(k^{n-2}).
\]
The values immediately below \(k\) and at \(k\) differ by \(J_k\), while the corresponding limiting values of continuous \(F\) agree. At least one of the two limiting absolute errors is therefore at least \(J_k/2\), by the triangle inequality. Approaching each integer from below if necessary gives
\[
\limsup_{\lambda\to\infty}
\lambda^{1-n}|\mu(\lambda)-F(\lambda)|\geq n/2.
\]
Choosing the left representative moves the value at the jump but leaves the same two one-sided limits, so cannot remove this obstruction. The example is an abstract measure, not a claimed scalar elliptic operator. It demonstrates why jump sizes at the second scale matter and why a proof must control both endpoint representatives, rather than silently equating their counts.

**Exercise 7.5 (returns on a flat torus; advanced).** On \(X=(\mathbb R/2\pi\mathbb Z)^n\), \(n\geq2\), take principal symbol \(p(\eta)=|\eta|\). Compute \(T(x)\) and describe \(T_*(x,\eta)\). Apply Theorem 5.1 to a positive Fourier multiplier that equals \(|\eta|\) at high frequency and has no lower homogeneous terms.

**Solution 7.5.** The flow is
\[
\chi_t(x,\eta)=(x+t\eta/|\eta|,\eta).
\]
A base return requires \(t\eta/|\eta|=2\pi k\) for some nonzero \(k\in\mathbb Z^n\). The shortest possible time among all directions is \(2\pi\), so \(T(x)=2\pi\) for every \(x\). For a fixed direction, a return exists exactly when \(\eta/|\eta|\) is parallel to a nonzero integer vector. If \(k\) is its primitive integer vector, then \(T_*(x,\eta)=2\pi|k|\); otherwise it is infinite.

For completeness, the primitive vector can be chosen as a shortest nonzero lattice vector on the specified positive ray. Such a vector exists because bounded balls contain only finitely many integer vectors. Every other positive lattice vector on the ray is an integer multiple: subtracting the floor of its real multiple of the shortest vector would otherwise give a shorter nonzero lattice vector. This proves the stated first full period.

There are countably many periodic directions. A bounded segment of each ray has measure zero for $n\ge2$: rotate it to a coordinate axis and cover it by a box of bounded length and transverse width $\varepsilon$, whose volume tends to zero. Countable exhaustion in length and countable subadditivity show that their union is null. Product integration with the finite-volume torus preserves zero symplectic measure. The preceding local coefficient lesson, Section 6, proves directly that the smooth classical Fourier multiplier on the torus is a pseudodifferential operator with its indicated local symbol, and proves completeness of the Fourier modes by Fejer kernels. Thus all hypotheses of the present theorem apply. This multiplier has \(p_s=0\), and altering its finitely many small Fourier modes changes the count by \(O(1)\). Equation (34) therefore yields
\[
N(\lambda)=(2\pi)^{-n}\operatorname{vol}(X)
                  \operatorname{vol}(B_1)\lambda^n
                  +o(\lambda^{n-1})
=\operatorname{vol}(B_1)\lambda^n+o(\lambda^{n-1}).
\]
The base return bound is positive at every point, whereas the full-period integral is zero. This example shows the gain obtained by localizing cotangent directions before taking the trace.

## References

- [HS] Lars Hörmander, “The spectral function of an elliptic operator,” *Acta Mathematica* 121 (1968), 193–218. Section 4. [Full article](https://projecteuclid.org/journalArticle/Download?urlid=10.1007%2FBF02391913).
- [W] Jared Wunsch, *Microlocal analysis and evolution equations*, arXiv:0812.3181v3 (20 July 2023 revision of 2008 lecture notes). Section 7; Section 9. [Free author preprint, version 3](https://arxiv.org/pdf/0812.3181v3).
- [I] Victor Ivrii, *100 years of Weyl's law*, arXiv:1608.03963v2 (27 February 2017). Sections 2.1.3–2.1.4; the wave/Tauberian comparison in Section 1.2. [Free author preprint, version 2](https://arxiv.org/pdf/1608.03963v2).
- [GS] Victor Guillemin and Shlomo Sternberg, *Semi-classical analysis*, author text dated April 25, 2012. Introduction Section 0.5, printed pages xi–xii, for functional-calculus/trace context. [Author PDF](https://people.math.harvard.edu/~shlomo/docs/Semi_Classical_Analysis_Start.pdf).
- [DG] Johannes J. Duistermaat and Victor W. Guillemin, “The spectrum of positive elliptic operators and periodic bicharacteristics,” *Inventiones Mathematicae* 29 (1975), 39–79. Introduction for the classical spectral setting. [Freely readable complete GDZ scan](https://gdz.sub.uni-goettingen.de/download/pdf/PPN356556735_0029/LOG_0010.pdf).
- [H3] Lars Hörmander, *The Analysis of Linear Partial Differential Operators III: Pseudo-Differential Operators*, reprint of the 1994 edition, Springer, 2007, Lemma 17.5.6 and its Fourier-window setup, pp. 49–50. ISBN 978-3-540-49938-1. [Edition information](https://doi.org/10.1007/978-3-540-49938-1).
- [H4] Lars Hörmander, *The Analysis of Linear Partial Differential Operators IV: Fourier Integral Operators*, reprint of the 1994 edition, Springer, 2009, (29.1.13)–(29.1.14), Theorems 29.1.4–29.1.5, Corollary 29.1.6 and the spectral-shift remark, pp. 256–259. ISBN 978-3-642-00136-9. [Edition information](https://doi.org/10.1007/978-3-642-00136-9).
