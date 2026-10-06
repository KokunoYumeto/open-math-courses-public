# From symbol estimates to operators on every Sobolev scale

**AN-03 · Unit AN03-U010 · Independent English AI draft, not admitted.**

Frequency differentiation improves a symbol, while differentiation in the base variable may worsen it. The balance between those two effects controls an expansion. Boundedness requires a different argument: a decomposition into frequency bands continues to work when the two effects exactly balance. We develop these mechanisms separately, then combine them to construct inverses and act on Sobolev and Besov spaces.

We use the Fourier conventions of AN03-DEP-001 and AN03-GAU-001: the forward kernel is \(e^{-ix\cdot\xi}\), inverse transformation has factor \((2\pi)^{-n}\), and \(D=-i\partial\). Fourier inversion and Plancherel, including their extension to \(L^2\), are explicit prerequisites. The additional entry contracts are completeness of \(L^2\), density of Schwartz functions in \(L^2\), the usual integration and dominated-convergence theorems for Lebesgue measure, Taylor's formula and the multivariable product rule. Distributional Fourier transformation, invertible linear pullback on tempered distributions, and the tempered Schwartz kernel theorem are the same explicit contracts as in AN03-WP-004. In particular the kernel theorem means that every continuous linear map \(\mathcal S(\mathbb R^n)\to\mathcal S'(\mathbb R^n)\) has exactly one kernel in \(\mathcal S'(\mathbb R^{2n})\), and conversely. Its foundational proof is not repeated or claimed here.

The quantitative quadratic-multiplier theorem AN03-GAU-007–008 and the classical metric verification AN03-WP-008 are proved earlier in this course. We use those results with specified metrics below. All statements are for a fixed finite dimension. Scalar symbols may be replaced by matrices between fixed finite-dimensional complex Hermitian spaces: norms replace absolute values, products keep their displayed order, and adjoints are conjugate transposes. The inverse theorem uses square matrices and a lower bound for their smallest singular value. No infinite-dimensional operator-valued extension is implicit.

## AN03-EUC-001 — The symbol topology and the order budget

Fix
\[
0<\rho\leq1,\qquad 0\leq\delta<1,\qquad m\in\mathbb R,
\qquad \langle\xi\rangle=(1+|\xi|^2)^{1/2}.
\tag{E1}
\]
The space \(S^m_{\rho,\delta}\) consists of smooth functions on \(\mathbb R_x^n\times\mathbb R_\xi^n\) for which every seminorm
\[
p_{m,L}(a)=\max_{|\alpha|+|\beta|\leq L}
\sup_{x,\xi}\langle\xi\rangle^{-m+\rho|\alpha|-\delta|\beta|}
\|\partial_\xi^\alpha\partial_x^\beta a(x,\xi)\|
\tag{E2}
\]
is finite. Bounds hold for all base points with the same constants. Estimates only on compact sets in \(x\) define a different, local topology. We write \(S^m=S^m_{1,0}\), \(S^{-\infty}=\bigcap_m S^m_{\rho,\delta}\), and \(S^\infty_{\rho,\delta}=\bigcup_mS^m_{\rho,\delta}\). The intersection is independent of the parameters in (E1): it consists precisely of functions all of whose derivatives decrease faster than every power of \(\langle\xi\rangle\), uniformly in \(x\).

These are Fréchet spaces. Indeed, a Cauchy sequence in all seminorms has uniformly Cauchy derivatives on every compact set. Successive integration along coordinate segments identifies the limits as derivatives of a smooth function. Passing to the limit in each weighted uniform bound proves convergence in that seminorm and completeness. The seminorm family is countable and separates points.

Differentiation is continuous with its exact order change,
\[
\partial_\xi^\alpha\partial_x^\beta:
S^m_{\rho,\delta}\longrightarrow
S^{m-\rho|\alpha|+\delta|\beta|}_{\rho,\delta}.
\tag{E3}
\]
Multiplication is continuous bilinear from orders \(m,m'\) to order \(m+m'\). To see the finite-seminorm assertion, expand a derivative of \(ab\): each term is
\(\binom\alpha\gamma\binom\beta\nu
(\partial_\xi^\gamma\partial_x^\nu a)
(\partial_\xi^{\alpha-\gamma}\partial_x^{\beta-\nu}b)\).
The powers contributed by the two factors add to
\(m+m'-\rho|\alpha|+\delta|\beta|\). Summing the finitely many coefficients gives
\(p_{m+m',L}(ab)\leq C_Lp_{m,L}(a)p_{m',L}(b)\).
This calculation also explains why exchanging two matrix factors is not allowed.

We will need one elementary stability property. If \(a_1,\ldots,a_k\in S^0_{\rho,\delta}\) and \(F\) is a smooth real-variable function on \(\mathbb C^k\), then \(F(a_1,\ldots,a_k)\in S^0_{\rho,\delta}\). Their ranges have compact closure in a bounded subset of \(\mathbb C^k\), so every derivative of \(F\) needed at a given stage is bounded there. An iterated chain-rule term is a derivative of \(F\) times a product of positive-order derivatives of the \(a_j\); their total frequency and base derivative counts are \(|\alpha|\) and \(|\beta|\). Equation (E2) follows. The same proof works when \(F\) is defined on an open neighborhood of that compact closure. In particular inversion of a matrix-valued order-zero symbol whose inverse is uniformly bounded preserves order zero: differentiate \(a^{-1}a=I\), obtaining \(\partial a^{-1}=-a^{-1}(\partial a)a^{-1}\), and iterate with the original factor order.

## AN03-EUC-002 — Completing formal expansions without losing support

**Frequency rescaling.** If \(a\in S^0\), then \(a_\varepsilon(x,\xi)=a(x,\varepsilon\xi)\), \(0\leq\varepsilon\leq1\), is a bounded family in \(S^0\), and
\[
a_\varepsilon\longrightarrow a(x,0)\quad\hbox{in }S^t
\quad(t>0).
\tag{E4}
\]
For \(0<t\leq1\), each fixed \(S^t\) seminorm of the difference is at most \(C\varepsilon^t\), with a finite number of seminorms of \(a\) in \(C\). For derivatives with \(\alpha=0\), boundedness and the mean-value formula give a bound \(C\min(1,\varepsilon|\xi|)\leq C(\varepsilon|\xi|)^t\). For \(q=|\alpha|\geq1\), derivatives of the limit vanish and
\[
\varepsilon^q\langle\xi\rangle^{q-t}
\langle\varepsilon\xi\rangle^{-q}\leq\varepsilon^t,
\tag{E5}
\]
because \(\varepsilon\langle\xi\rangle\leq\langle\varepsilon\xi\rangle\) and \(q\geq t\). The estimates also prove boundedness at order zero. Values \(t>1\) follow by the inclusion \(S^1\subset S^t\). Convergence in \(S^0\) need not hold: \(a(\xi)=\xi_1/\langle\xi\rangle\) has \(a(x,0)=0\) and \(\sup_\xi|a(\varepsilon\xi)|=1\) for every positive \(\varepsilon\).

**Summation theorem.** Let \(a_j\in S^{m_j}_{\rho,\delta}\), \(j\geq0\), with \(m_j\to-\infty\), without assuming monotonicity. Put \(M_k=\max_{j\geq k}m_j\). There exists \(a\in S^{M_0}_{\rho,\delta}\) such that
\[
\operatorname{supp}a\subset\bigcup_j\operatorname{supp}a_j,
\qquad a-\sum_{j<k}a_j\in S^{M_k}_{\rho,\delta}\quad(k\geq0).
\tag{E6}
\]
Any two such sums differ by \(S^{-\infty}\). Permuting the terms does not change their sum modulo that space.

**Proof.** Choose a smooth function \(\chi\) equal to one near zero and with compact support. For each \(j\) choose \(R_j\to\infty\), strictly increasing if necessary, so that
\[
\|(1-\chi(\xi/R_j))a_j\|_{m_j+1,L}\leq2^{-j}
\quad(0\leq L\leq j).
\tag{E7}
\]
Here \(\|\cdot\|_{m,L}\) means (E2). This choice is possible: on the support of the high-frequency cutoff, \(\langle\xi\rangle^{-1}\to0\) uniformly as \(R_j\to\infty\). A frequency derivative of order \(\gamma\) hitting the cutoff gives \(R_j^{-|\gamma|}\), supported where \(|\xi|\asymp R_j\); since \(\rho\leq1\), it is bounded by a constant times \(\langle\xi\rangle^{-\rho|\gamma|}\). The remaining factors have their stipulated symbol bounds. For a fixed finite set of derivatives these estimates prove (E7).

Let \(A_j=(1-\chi(\xi/R_j))a_j\) and \(a=\sum_jA_j\). The sum is locally finite in frequency, hence smooth. For fixed \(k,L\), choose \(J\geq\max(k,L)\) so large that \(m_j+1\leq M_k\) for all \(j\geq J\). The tail \(\sum_{j\geq J}A_j\) converges in the order-\(M_k\), derivative-\(L\) seminorm by (E7). The remaining terms in
\(a-\sum_{j<k}a_j\) are finitely many symbols of order at most \(M_k\), together with finitely many \(-\chi(\xi/R_j)a_j\). The latter are in \(S^{-\infty}\), since their frequency support is bounded and all base derivatives are uniformly bounded there. This proves every differentiated estimate in (E6).

Support is also preserved at points outside the union. Near such a point only finitely many \(A_j\) can be nonzero, and each of those vanishes in some neighborhood of the point; intersect those neighborhoods. Uniqueness follows by taking \(k\to\infty\). For a permutation and a specified finite initial segment of it, let \(M\) be the largest order among the omitted terms. Choose an original initial segment containing the specified terms and all terms of order greater than \(M\). Subtracting its expansion expresses the new remainder as finitely many symbols of order at most \(M\), plus a remainder of that order. This proves the permuted version of (E6). ∎

**Recognition from values.** Suppose \(a\) is smooth, every one of its derivatives has some polynomial bound in \(\langle\xi\rangle\), uniformly in \(x\), and
\[
\left\|a-\sum_{j<k}a_j\right\|\leq C_k\langle\xi\rangle^{\mu_k},
\qquad \mu_k\to-\infty.
\tag{E8}
\]
Then \(a\) has the full symbol expansion (E6). In particular no differentiated remainder assumptions are needed in (E8).

To prove this, subtract a sum \(a_0\) constructed above. The difference \(f=a-a_0\) decreases faster than every frequency power: for a prescribed power choose \(k\) for which both \(\mu_k\) and \(M_k\) are sufficiently negative. Every derivative of \(f\) still has a polynomial bound. If \(\partial_j^2 f\) has growth exponent \(q\), the one-dimensional Taylor formula in either a base or a frequency coordinate gives, for \(0<h\leq1\),
\[
|\partial_j f(x,\xi)|
\leq h^{-1}|f((x,\xi)+he_j)-f(x,\xi)|
+C h\langle\xi\rangle^q.
\tag{E9}
\]
The weight at the shifted point is comparable to the original weight. Given an arbitrary desired decay power \(N\), take \(h=\langle\xi\rangle^{-L}\) with \(L>q+N\), then use the already known decay of \(f\) of degree greater than \(L+N\). Both terms in (E9) are \(O(\langle\xi\rangle^{-N})\). Thus every first derivative decreases rapidly. Reapply the same argument to each derivative already treated; the necessary second derivative has a polynomial bound by hypothesis. Induction proves rapid decrease of every derivative, so \(f\in S^{-\infty}\). This proof and the summation construction work throughout (E1), including \(\delta>\rho\).

**Complex homogeneous expansions.** For \(z\in\mathbb C\) and \(h=1/q\), with \(q\) a positive integer, a polyhomogeneous symbol of degree \(z\) and step \(h\) is a symbol \(a\in S^{\operatorname{Re}z}\) satisfying \(a\sim\sum_{j\geq0}a_j\) in the sense of (E6), where \(a_j\) is homogeneous of degree \(z-jh\) outside the unit frequency ball. The convention is \(t^z=e^{z\log t}\) for \(t>0\). Smooth angular coefficients whose base and angular derivatives are uniformly bounded have the required symbol estimates: polar differentiation lowers the radial degree by one for each frequency derivative. Multiplying each homogeneous term by a fixed cutoff near zero makes it globally smooth; such choices differ in \(S^{-\infty}\). The summation theorem then constructs the symbol. Without the uniform angular/base bounds, a homogeneous formula alone would give only a local-in-base symbol. Integer frequency differentiations change the degree by an integer, which is an integral multiple of the stipulated step \(h\).

## AN03-EUC-003 — Quantization, kernels, and a sign check

For every symbol in (E1), left quantization is
\[
\operatorname{Op}(a)u(x)=(2\pi)^{-n}
\int e^{ix\cdot\xi}a(x,\xi)\widehat u(\xi)\,d\xi,
\qquad u\in\mathcal S.
\tag{E10}
\]
This integral and all its differentiated versions converge absolutely. The map \((a,u)\mapsto\operatorname{Op}(a)u\) is continuous bilinear from \(S^m_{\rho,\delta}\times\mathcal S\) into \(\mathcal S\), throughout (E1). Indeed, output derivatives create finitely many powers of \(\xi\) and base derivatives of \(a\). To estimate \(x^\gamma\partial_x^\beta\operatorname{Op}(a)u\), move \(|\gamma|\) frequency derivatives off the exponential by integration by parts. Each resulting integrand is a derivative of \(a\), a polynomial, and a derivative of \(\widehat u\). Its absolute integral is bounded by one sufficiently large Schwartz seminorm of \(u\) times finitely many seminorms (E2), after choosing the remaining weight less than \(-n\). Boundary terms vanish by the same rapid decrease. This gives every Schwartz seminorm and the asserted joint continuity.

Differentiation and one integration by parts give
\[
[\operatorname{Op}(a),D_j]=i\operatorname{Op}(\partial_{x_j}a),
\qquad
[\operatorname{Op}(a),x_j]=-i\operatorname{Op}(\partial_{\xi_j}a).
\tag{E11}
\]
If \(a(x,\xi)=\sum_\alpha a_\alpha(x)\xi^\alpha\), then
\(\operatorname{Op}(a)=\sum_\alpha a_\alpha(x)D^\alpha\): coefficients stand on the left. Such a polynomial belongs to a global symbol class only when its coefficients have the relevant uniform derivative bounds.

There is also an exact definition for every \(a\in\mathcal S'(\mathbb R^{2n})\). Take the partial inverse Fourier transform in \(\xi\), call its second variable \(z\), and use the invertible linear substitution \(z=x-y\). The result is a tempered kernel \(K_a\). Conversely,
\[
K_a(x,y)=(2\pi)^{-n}\int e^{i(x-y)\cdot\xi}a(x,\xi)\,d\xi,
\quad
a(x,\xi)=\int e^{-iz\cdot\xi}K_a(x,x-z)\,dz
\tag{E12}
\]
are inverse operations on tempered distributions. The displayed integrals mean Fourier transforms there, not potentially divergent ordinary integrals. Each step is a continuous linear isomorphism, so the symbol–kernel correspondence is bijective and continuous in both directions. Combined with the explicit tempered kernel theorem contract, it identifies arbitrary continuous \(\mathcal S\to\mathcal S'\) maps with tempered symbol-distributions. For smooth symbols (E12) agrees with (E10), by testing against two Schwartz functions and Fourier inversion.

Use the sesquilinear pairing \((u,v)=\int u\overline v\), linear in \(u\). Transposing and conjugating the kernel sends \(K_a(x,y)\) to \(K_a(y,x)^*\). Its left symbol is
\[
a^\dagger=Q_1(a^*),\qquad
Q_t=\exp\bigl(it\langle D_x,D_\xi\rangle\bigr).
\tag{E13}
\]
Here \(Q_t\) is the Fourier multiplier \(e^{itp\cdot q}\) in the variables dual to \((x,\xi)\). It preserves \(\mathcal S\) and \(\mathcal S'\) because all derivatives of that multiplier grow at most polynomially. To check the sign directly, apply (E12) first to \(a(x,\xi)=e^{i(p\cdot x+q\cdot\xi)}\). Its operator is multiplication by \(e^{ip\cdot x}\) followed by translation \(u(x)\mapsto u(x+q)\). Its adjoint is therefore
\(v(x)\mapsto e^{-ip\cdot(x-q)}v(x-q)\), whose symbol is
\(e^{ip\cdot q}e^{-i(p\cdot x+q\cdot\xi)}\). This is exactly (E13). Integrating this identity against Schwartz Fourier transforms proves it for Schwartz symbols, and continuity of the kernel and Fourier operations proves it for all tempered symbols. Thus
\((\operatorname{Op}(a)u,v)=(u,\operatorname{Op}(a^\dagger)v)\)
whenever \(u,v\in\mathcal S\), with distributional pairing when needed.

## AN03-EUC-004 — A Gaussian reduction with explicit parameters

Assume now \(\delta\leq\rho\). Set \(\kappa=\rho-\delta\). AN03-WP-008 applies to
\[
g_{(x,\xi)}(y,\eta)=\langle\xi\rangle^{2\delta}|y|^2
+\langle\xi\rangle^{-2\rho}|\eta|^2,
\qquad m_a=\langle\xi\rangle^m.
\tag{E14}
\]
Its slow variation and temperateness hold uniformly, and its symplectic parameter is \(\langle\xi\rangle^{-\kappa}\). Consequently, for every fixed real \(t\),
\[
Q_t:S^m_{\rho,\delta}\longrightarrow S^m_{\rho,\delta},
\quad
Q_ta-\sum_{|\alpha|<N}\frac{t^{|\alpha|}}{\alpha!}
\partial_\xi^\alpha D_x^\alpha a
\in S^{m-N\kappa}_{\rho,\delta}.
\tag{E15}
\]
For each output seminorm only finitely many input seminorms are used. These maps preserve convergence in the local smooth topology on bounded source sets. The phase convention matters: for \(A(p,q)=t p\cdot q\), the symmetric representative is \(t/2\) times the swap map, so the Gauss parameter is \(|t|\langle\xi\rangle^{-\kappa}/2\). A fixed rescaling of (E14) makes it at most one if necessary. This proves (E15) directly from AN03-GAU-008 with precisely the hypotheses checked in AN03-WP-008.

For composition we need a parameter version that retains more information before restricting to a diagonal. Let
\[
c(x,\xi,y,\eta)=a(x,\eta)b(y,\xi),\qquad
\mathcal B=\exp(i\langle D_y,D_\eta\rangle)c.
\tag{E16}
\]
At fixed \((x,\xi)\), let \(s=\langle\xi\rangle\) and equip the \((y,\eta)\) variables with
\[
G_{(y,\eta)}(v,w)=s^{2\delta}|v|^2+
\langle\eta\rangle^{-2\rho}|w|^2.
\tag{E17}
\]
The evaluation points needed for composition have \(\eta=\xi\). At these points the Gauss parameter for the phase \(p_y\cdot p_\eta\) is \(s^{-\kappa}/2\). We verify the uniform global hypotheses for that evaluation instead of assuming uncertainty at every \(\eta\).

Write \(r=\langle\eta\rangle\), \(d=|\eta-\xi|\). The phase-dual distance based at \((y,\eta)\) includes \(4s^{-2\delta}d^2\). Both ratios \(r/s\) and \(s/r\) are bounded by a fixed power of
\(1+s^{-2\delta}d^2\), with constants depending only on \(\delta<1\). If \(r\) and \(s\) are within a factor two this is immediate. If \(r>2s\), then \(d>r/2\) and
\(s^{-2\delta}d^2\geq (r/s)^2/4\), since \(s^{2-2\delta}\geq1\).
If \(s>2r\), then \(d>s/2\), so the same expression is at least \(s^{2(1-\delta)}/4\); choosing a sufficiently large power bounds \(s/r\leq s\). These inequalities control the ratio of the two frequency coefficients of (E17), every real power weight \(r^q\), and their reciprocals. The base coefficient is constant. Slow variation follows from \(\rho\leq1\) and the Lipschitz inequality for \(\langle\eta\rangle\); the same comparison proves local continuity of \(r^q\). Thus every condition of the observation-point form of AN03-GAU-007–008 holds, with constants independent of \(x,\xi,y\).

The tensor \(c\) has weight \(r^{m_1}s^{m_2}\) in (E17): each \(y\)-derivative costs at most \(s^\delta\), and each \(\eta\)-derivative costs at most \(r^{-\rho}\). Applying the Gauss theorem and then restricting \(y=x,\eta=\xi\) gives a remainder of order \(m_1+m_2-N\kappa\). To obtain every derivative estimate, differentiate (E16) first. Derivatives commute with its constant-coefficient multiplier. For example
\(\partial_\xi^\alpha\partial_x^\beta
\partial_\eta^{\alpha'}\partial_y^{\beta'}c\)
has weight
\(r^{m_1-\rho|\alpha'|+\delta|\beta|}
s^{m_2-\rho|\alpha|+\delta|\beta'|}\).
Apply the same theorem with those modified real exponents. Finally, differentiation of the diagonal restriction is the sum of the corresponding derivatives in the two sets of variables. Each term has the required total order in (E2). The product rule bounds every input seminorm by a finite sum of products of seminorms of \(a\) and \(b\).

For the classical case \((\rho,\delta)=(1,0)\), this argument holds at every \((y,\eta)\), not just \(\eta=\xi\), because (E17) no longer depends on \(s\). It gives the stronger, pre-diagonal estimate
\[
\begin{split}
&\left\|\partial_\xi^\alpha\partial_x^\beta
\partial_\eta^{\alpha'}\partial_y^{\beta'}
\left(\mathcal B-
\sum_{|\gamma|<N}\frac{\partial_\eta^\gamma a(x,\eta)
D_y^\gamma b(y,\xi)}{\gamma!}\right)\right\|\\
&\hspace{12mm}\leq C
\langle\eta\rangle^{m_1-N-|\alpha'|}
\langle\xi\rangle^{m_2-|\alpha|}.
\end{split}
\tag{E18}
\]
In particular the loss is attached to the transformed frequency variable before evaluation. The constants in (E18) also involve only finitely many source seminorms.

All these Gauss limits agree with the distributional multipliers wherever both are defined. Multiply the symbols by cutoffs in both variables that tend to one. They stay in bounded symbol sets and converge locally smoothly; their polynomial growth gives convergence in \(\mathcal S'\). The distributional multiplier is continuous there, while the Gauss estimate gives the same locally smooth limit on its evaluation set. This also justifies differentiating with respect to the fixed parameters in (E16): differentiated approximants have the estimates just proved, converge locally, and their limits are successive derivatives by the fundamental theorem of calculus along parameter segments.

## AN03-EUC-005 — Adjoints, products, and their exact domain

**Theorem.** For \(\delta\leq\rho\), the adjoint symbol (E13) belongs to \(S^m_{\rho,\delta}\), and left quantization extends continuously to \(\mathcal S'\) by transposition of its adjoint's Schwartz action. If \(a\in S^{m_1}_{\rho,\delta}\) and \(b\in S^{m_2}_{\rho,\delta}\), then
\[
\operatorname{Op}(a)\operatorname{Op}(b)=\operatorname{Op}(a\circ b),
\quad a\circ b=\mathcal B(x,\xi,x,\xi)
\in S^{m_1+m_2}_{\rho,\delta}.
\tag{E19}
\]
The identity holds on both \(\mathcal S\) and \(\mathcal S'\). The product is continuous bilinear. For every \(N\geq0\),
\[
a^\dagger-\sum_{|\alpha|<N}
\frac{\partial_\xi^\alpha D_x^\alpha(a^*)}{\alpha!}
\in S^{m-N\kappa}_{\rho,\delta},
\tag{E20}
\]
\[
a\circ b-\sum_{|\alpha|<N}
\frac{(\partial_\xi^\alpha a)(D_x^\alpha b)}{\alpha!}
\in S^{m_1+m_2-N\kappa}_{\rho,\delta}.
\tag{E21}
\]
Each remainder map has finite-seminorm control as described above. Adjoint transformation sends bounded sequences converging locally smoothly to sequences with the same property; the product has the analogous bounded-set continuity in both factors.

**Proof.** The symbol assertions and their estimates follow from (E15)–(E18), including \(N=0\). Formula (E13) and the Schwartz action prove extension to tempered distributions. For Schwartz symbols and \(u\in\mathcal S\), Fubini's theorem applied to two instances of (E10) gives
\[
(a\circ b)(x,\xi)=(2\pi)^{-n}
\iint e^{i(x-y)\cdot(\eta-\xi)}a(x,\eta)b(y,\xi)\,dy\,d\eta,
\tag{E22}
\]
which equals (E16) restricted to the diagonal. The sign can also be checked by taking \(a=a(\xi)\), \(b=e^{iv\cdot x}b_0(\xi)\): (E22) becomes \(e^{iv\cdot x}a(\xi+v)b_0(\xi)\), agreeing with (E21).

Choose compactly supported smooth approximants \(a_j,b_j\) as at the end of AN03-EUC-004. Their symbols and products remain bounded in their respective orders and converge locally smoothly. For any fixed \(u\in\mathcal S\), (E10) and dominated convergence give local smooth convergence of the outputs. The Schwartz estimates of AN03-EUC-003 bound all output Schwartz seminorms uniformly. Local convergence plus those stronger uniform seminorms gives convergence in every Schwartz seminorm: outside a large base ball use one extra power of \(\langle x\rangle\), and inside use local convergence. Thus \(\operatorname{Op}(a_j)u\to\operatorname{Op}(a)u\) in \(\mathcal S\), and similarly for \(b_j\) and their products. Boundedness of the Schwartz operator seminorms allows passage through the double composition. This proves (E19) on \(\mathcal S\).

Taking adjoints there identifies the transpose of the product with the reverse product of the transposes. Apply their continuous extensions to \(\mathcal S'\) and test against \(\mathcal S\) to obtain (E19) on \(\mathcal S'\). Equivalently, the identities of pairings determine the extension uniquely. Kernel injectivity proves associativity of \(\circ\) and that the constant symbol \(I\) is its unit. ∎

When \(\delta<\rho\), (E20)–(E21) are asymptotic expansions in decreasing orders. When \(\delta=\rho<1\), closure and every finite remainder estimate survive, but all their target orders are the original order. Taking more terms then supplies no smoothing assertion. This distinction will be used in the inverse construction.

## AN03-EUC-006 — A finite-derivative \(L^2\) estimate

We first prove an estimate that involves no symbol order. Suppose \(a(x,\xi)\) is smooth and all derivatives up to a sufficiently large fixed order are bounded. Then
\[
\|\operatorname{Op}(a)u\|_2\leq C_n M\|u\|_2,
\qquad
M=\max_{|\alpha|+|\beta|\leq L_n}
\|\partial_\xi^\alpha\partial_x^\beta a\|_\infty.
\tag{E23}
\]
The number \(L_n\) is finite; the proof permits \(L_n=4N\) for any integer \(N>n/2\). Only this estimate, not an optimal derivative count, is needed.

We record the integral estimate used in its proof. If a measurable kernel \(K(s,t)\) on any two copies of a measure space satisfies
\(\sup_t\int|K(s,t)|\,ds\leq A\) and
\(\sup_s\int|K(s,t)|\,dt\leq B\), then its operator has \(L^2\) norm at most \(\sqrt{AB}\). In fact,
\[
\left|\int K(s,t)u(t)\,dt\right|^2
\leq\left(\int|K(s,t)|\,dt\right)
\left(\int|K(s,t)||u(t)|^2\,dt\right).
\tag{E24}
\]
Integration in \(s\) and Tonelli's theorem give \(AB\|u\|_2^2\). Truncation first handles any existence issue, and the estimate supplies the extension. This includes continuous kernels with equal marginal bound \(A=B=C\) and norm at most \(C\).

**Proof of (E23).** Fix \(\phi\in\mathcal S(\mathbb R^n)\) with \(\|\phi\|_2=1\), and put
\(\phi_{q,p}(x)=e^{ip\cdot x}\phi(x-q)\).
Use phase-space measure \(d\mu(q,p)=(2\pi)^{-n}dq\,dp\). The packet transform
\(Vu(q,p)=(u,\phi_{q,p})\) is an isometry from \(L^2\) into \(L^2(d\mu)\): Plancherel in \(p\), followed by integration in \(q\), gives
\[
\int|Vu(q,p)|^2d\mu(q,p)
=\iint |u(x)|^2|\phi(x-q)|^2\,dx\,dq=\|u\|_2^2.
\tag{E25}
\]
The synthesis map \(V^*f=\int f(Q)\phi_Q\,d\mu(Q)\), initially for bounded compactly supported \(f\), has norm at most one: pairing with an \(L^2\) function, applying Cauchy–Schwarz and (E25), and taking the supremum over unit vectors proves this bound. Completeness extends synthesis to every \(f\in L^2(d\mu)\). Polarization of (E25) gives \(V^*V=I\). For Schwartz \(u\), \(Vu\) decreases rapidly in both packet variables; integration by parts in \(x\) controls the momentum variable and the product of two Schwartz functions controls the position variable. Thus the reconstruction \(u=\int Vu(Q)\phi_Q\,d\mu(Q)\) converges in \(\mathcal S\).

Consider the matrix of \(A=\operatorname{Op}(a)\) between two packets, with output packet \((q,p)\) and input packet \((q',p')\). Substitute \(x=q+s\), \(\xi=p'+t\) in (E10). Apart from a factor of absolute value one it is
\[
(2\pi)^{-n}\iint
e^{i[s\cdot(p'-p)+t\cdot(q-q')]}
e^{is\cdot t}a(q+s,p'+t)\widehat\phi(t)\overline{\phi(s)},ds\,dt.
\tag{E26}
\]
Apply \((1-\Delta_s)^N(1-\Delta_t)^N\) to the last three factors by integration by parts. Derivatives of \(e^{is\cdot t}\) create only polynomials in \(s,t\); derivatives of the two fixed Schwartz functions absorb those polynomials. Consequently the absolute integral of all differentiated amplitudes is bounded by \(C_{n,N,\phi}M\), uniformly in all four packet parameters. The derivative order of \(a\) is at most \(4N\). We obtain
\[
|(A\phi_{q',p'},\phi_{q,p})|
\leq CM\langle q-q'\rangle^{-2N}
\langle p-p'\rangle^{-2N}.
\tag{E27}
\]
Since \(2N>n\), both phase-space marginals are integrable and uniformly bounded by \(CM\). Equation (E24) bounds the corresponding operator \(\mathcal M\) on \(L^2(d\mu)\). The zeroth bound on \(a\) already makes (E10) a continuous map \(\mathcal S\to\mathcal S'\), since its outputs are bounded functions. For Schwartz \(u,v\), their packet reconstructions and (E27) give
\((Au,v)=(\mathcal M Vu,Vv)\).
All integrals converge by the decay just proved. Hence \(A=V^*\mathcal M V\) on \(\mathcal S\) as distributions, which establishes both membership of \(Au\) in \(L^2\) and the norm bound. No \(L^2\) boundedness of \(A\) was assumed in forming its packet matrix. This proves (E23), and density gives the extension. ∎

The calculation works for fixed-size matrices by estimating the matrix norm in (E26) and applying the scalar majorant to the norm of the vector input. It therefore has no positivity or scalar-commutativity assumption.

Two consequences also isolate the lower-order mechanisms in the classical calculus. If \(a\in S^q_{\rho,\delta}\) with \(q<-n\), its kernel is an ordinary continuous function. Every \((x-y)^\alpha K_a(x,y)\) is, up to a fixed power of \(i\), the inverse-frequency transform of \(\partial_\xi^\alpha a\). That derivative has integrable absolute value uniformly in \(x\). Dominated convergence on compact base sets proves continuity, and integration by parts, first with a cutoff and then letting it tend to one, gives
\(|K_a(x,y)|\leq C_N\langle x-y\rangle^{-N}\) for every \(N\). Taking \(N>n\) verifies both marginals in (E24). For classical symbols this proves boundedness at all sufficiently negative orders without the packet estimate. If boundedness is known at order \(2q\), the identity \(\|\operatorname{Op}(a)u\|_2^2=(\operatorname{Op}(a^\dagger\circ a)u,u)\) proves it at order \(q\), since the composed symbol has order \(2q\). A finite number of doublings brings any fixed \(q<0\) below \(-n\). This proves boundedness at every negative order, including order minus one.

For scalar classical \(a\in S^0\), choose \(M>\sup|a|^2\) with a fixed positive gap and set \(c=(M-|a|^2)^{1/2}\in S^0\), using AN03-EUC-001. Equations (E20)–(E21) give
\(a^\dagger\circ a+c^\dagger\circ c=M+r\), \(r\in S^{-1}\).
Taking the quadratic form on Schwartz functions and discarding \(\|\operatorname{Op}(c)u\|_2^2\geq0\) proves order-zero boundedness from the negative-order result. Thus the classical square-root argument is justified in full, while the packet and band argument below supplies the additional equality endpoint where a decreasing remainder is unavailable.

## AN03-EUC-007 — Equality of the derivative costs still allows \(L^2\) boundedness

**Theorem.** If \(\delta\leq\rho\) in (E1), then
\[
a\in S^0_{\rho,\delta}
\quad\Longrightarrow\quad
\|\operatorname{Op}(a)\|_{L^2\to L^2}
\leq C p_{0,L}(a)
\tag{E28}
\]
for some finite \(L\), with \(C,L\) depending only on the fixed parameters and dimension. In particular (E28) includes \(0<\rho=\delta<1\).

**Proof.** Take a smooth dyadic partition \(1=\sum_{j\geq0}\chi_j(\xi)\), with \(\chi_0\) supported in a fixed ball and, for \(j\geq1\), \(\chi_j\) supported where \(2^{j-1}\leq|\xi|\leq2^{j+1}\). All frequency derivatives obey the corresponding \(2^{-j|\alpha|}\) bounds. Set \(a_j=a\chi_j\). Under the unitary dilation
\(u(x)\mapsto 2^{-jn\rho/2}u(2^{-j\rho}x)\), the symbol of the conjugated operator is
\[
\widetilde a_j(X,\Xi)=a_j(2^{-j\rho}X,2^{j\rho}\Xi).
\tag{E29}
\]
Its derivatives are uniformly bounded: a base derivative gives
\(2^{-j\rho}2^{j\delta}\leq1\), and a frequency derivative gives \(2^{j\rho}2^{-j\rho}=1\). Cutoff derivatives satisfy the same bounds because \(\rho\leq1\). Hence (E23) gives \(\|\operatorname{Op}(a_j)\|\leq C p_{0,L_n}(a)\), uniformly in \(j\). This alone would not justify summing their norms.

Separate each \(a_j\) into a symbol with small base Fourier support and an error. Choose \(\psi\in\mathcal S\) with \(\widehat\psi\in C_c^\infty\), equal to one near zero, and with its Fourier support in the unit ball. With the Fourier normalization fixed above, \(\int\psi=1\), and every nonconstant polynomial moment of \(\psi\) is zero. For \(j\geq1\), put \(\lambda_j=2^{j-4}\) and
\[
\ell_j(x,\xi)=\int\psi(z)a_j(x-z/\lambda_j,\xi)\,dz,
\qquad r_j=a_j-\ell_j.
\tag{E30}
\]
Convolution preserves the uniform derivative bounds used in (E29), up to \(\|\psi\|_1\). Taylor expansion in \(x\) to order \(K-1\), together with the vanished moments, gives
\[
\|\partial_x^\beta\partial_\xi^\alpha r_j\|_\infty
\leq C_K\lambda_j^{-K}
\max_{|\nu|=K}\|\partial_x^{\beta+\nu}
\partial_\xi^\alpha a_j\|_\infty
\leq C p_{0,L}(a)
2^{-jK(1-\delta)}2^{j\delta|\beta|-j\rho|\alpha|}.
\tag{E31}
\]
The integral Taylor remainder is bounded using \(\int|z|^K|\psi(z)|dz<\infty\). Thus after the dilation (E29), (E23) implies
\[
\|\operatorname{Op}(r_j)\|_{2\to2}
\leq C p_{0,L}(a)2^{-jK(1-\delta)}.
\tag{E32}
\]
Choose for example \(K=1\). Since \(\delta<1\), these norms are summable, with finite bound depending on \(1-2^{-(1-\delta)}\). Larger \(K\) is available when needed.

The symbol \(\ell_j\) has base Fourier support \(|\theta|\leq2^{j-4}\), in the distributional sense; multiplication by \(\widehat\psi(\theta/\lambda_j)\) proves this even though the base variable is not integrable. Its frequency support remains that of \(\chi_j\). In the Fourier representation of (E10), output frequency equals input frequency plus base Fourier frequency. Hence \(\operatorname{Op}(\ell_j)\) kills inputs outside the \(j\)-th frequency annulus and its outputs are supported in a slightly enlarged annulus, for example
\(2^{j-2}\leq|\eta|\leq2^{j+2}\).
One can verify the support assertion by testing against compactly supported frequency test functions with disjoint sum supports, using the distributional Fourier formula; it requires no pointwise Fourier transform of \(\ell_j\).

Let \(P_j\) be the sharp \(L^2\) projection onto the support annulus of \(\chi_j\). Then \(\operatorname{Op}(\ell_j)=\operatorname{Op}(\ell_j)P_j\), and \(\sum_j\|P_ju\|_2^2\leq C\|u\|_2^2\) because the annuli overlap only finitely often. The enlarged output annuli have the same finite-overlap property. Pointwise Cauchy–Schwarz in Fourier space and Plancherel therefore give, for every finite sum,
\[
\left\|\sum_j\operatorname{Op}(\ell_j)u\right\|_2^2
\leq C\sum_j\|\operatorname{Op}(\ell_j)P_ju\|_2^2
\leq C p_{0,L}(a)^2\|u\|_2^2.
\tag{E33}
\]
The same estimate for tails shows convergence for each \(u\in L^2\), since the tail of \(\sum\|P_ju\|^2\) tends to zero. The single low-frequency term \(a_0\) is bounded by (E23). Adding (E32) proves a bounded operator with estimate (E28). On Schwartz inputs the dyadic symbol sum converges in (E10), with all Schwartz output seminorms, by the rapid decrease of \(\widehat u\) and the already established seminorm estimates. The bounded operator is therefore exactly \(\operatorname{Op}(a)\). ∎

This proof uses \(\delta\leq\rho\) in the rescaling and \(\delta<1\) in the summable error. It never treats the zero gain \(\rho-\delta\) as positive.

There is a useful complementary result with no frequency differentiability. Suppose \(a(x,\xi)\) is measurable and, for each \(\xi\), is \(C^{n+1}\) in \(x\), with
\[
\sup_\xi\sum_{|\alpha|\leq n+1}
\int\|D_x^\alpha a(x,\xi)\|\,dx\leq M.
\tag{E34}
\]
Then \(\operatorname{Op}(a)\) is bounded on \(L^2\), with norm at most \(C_nM\). Define it initially when \(\widehat u\in C_c^\infty\). Let
\(A(\theta,\xi)=(2\pi)^{-n}\mathcal F_xa(\theta,\xi)\).
Integration by parts in the sense of integrable weak derivatives gives
\[
\|A(\theta,\xi)\|\leq C_nM\langle\theta\rangle^{-n-1}.
\tag{E35}
\]
Indeed the Fourier transforms of all derivatives of order at most \(n+1\) are bounded by their \(L^1\) norms, and the corresponding monomials dominate \(\langle\theta\rangle^{n+1}\). Cutoffs in \(x\), followed by their limit in these \(L^1\) derivative norms, justify the integration by parts. Fubini gives
\(\widehat{\operatorname{Op}(a)u}(\eta)=\int A(\eta-\xi,\xi)\widehat u(\xi)d\xi\).
Both kernel marginals are bounded by \(C_nM\) using (E35). Apply (E24) and Plancherel, then density. Joint measurability and the derivative hypotheses suffice; no hidden \(\xi\)-smoothness is used.

## AN03-EUC-008 — All real Sobolev orders and all dyadic sequence endpoints

For real \(s\), let \(H^s\) be the tempered distributions whose Fourier transforms are locally square integrable and satisfy
\[
\|u\|_{H^s}^2=(2\pi)^{-n}
\int\langle\xi\rangle^{2s}|\widehat u(\xi)|^2\,d\xi<\infty.
\tag{E36}
\]
The multiplier \(J^s=\langle D\rangle^s\) is an isometric isomorphism \(H^s\to L^2\), by the Fourier \(L^2\) contract. Its symbol belongs to \(S^s_{\rho,\delta}\) in (E1): actual frequency derivatives lose one order, which is at least the required loss \(\rho\), and all nonzero base derivatives vanish.

For \(a\in S^m_{\rho,\delta}\) with \(\delta\leq\rho\), the composition theorem gives
\(J^{s-m}\operatorname{Op}(a)J^{-s}\in\operatorname{Op}(S^0_{\rho,\delta})\).
The finite-seminorm bounds in (E21) and (E28) therefore prove
\[
\operatorname{Op}(a):H^s\longrightarrow H^{s-m}
\quad\hbox{continuously for every real }s.
\tag{E37}
\]
This is the restriction of the already defined tempered-distribution operator: it agrees first on Schwartz functions and then by continuity and density in \(H^s\). For integer nonnegative \(s\), (E36) is equivalent to the sum of squared \(L^2\) norms of the derivatives through order \(s\), by expanding \((1+|\xi|^2)^s\); negative and noninteger orders retain the Fourier definition.

The relevant Besov scale uses an \(\ell^p\) index, not an \(L^p\) index in the base variable. Its domain consists of tempered distributions with locally square-integrable Fourier transforms. Set
\(A_0=\{|\xi|<1\}\), \(A_j=\{2^{j-1}\leq|\xi|<2^j\}\) for \(j\geq1\), and let \(\Pi_j\) be their sharp Fourier projections. For \(1\leq p\leq\infty\), define
\[
\|u\|_{B^s_{2,p}}=
\left\|(2^{js}\|\Pi_ju\|_2)_{j\geq0}\right\|_{\ell^p},
\tag{E38}
\]
with the supremum when \(p=\infty\). A distribution in this space has a locally \(L^2\) Fourier transform. The sharp projections are consequently well defined; conversely a sequence of \(L^2\) functions on these annuli with at most polynomial growth defines a tempered distribution by summation. Cauchy–Schwarz on each annulus and rapid decay of a Schwartz test function make that series convergent. Thus (E38) is a Banach norm, by completeness of the weighted \(\ell^p\) sum of the Hilbert spaces \(L^2(A_j)\). It is equivalent to the norm using \(\|\Pi_ju\|_{H^s}\), since \(\langle\xi\rangle\asymp2^j\) on each annulus. The latter is the convention often denoted \({}^pH_{(s)}\). In particular \(B^s_{2,2}=H^s\) with equivalent norms. Smooth dyadic cutoffs give the same spaces: each smooth piece meets finitely many sharp annuli and vice versa, so the two finite-overlap triangle estimates give norm equivalence.

Here is a proof of the exact interpolation implication needed for the calculus. Suppose a linear operator \(T\) is consistent and bounded from \(H^{s_-}\) to \(H^{s_--m}\) and from \(H^{s_+}\) to \(H^{s_+-m}\), with \(s_-<s<s_+\). On \(\Pi_ju\), the two estimates imply
\[
2^{k(s-m)}\|\Pi_kT\Pi_ju\|_2
\leq C\min\{2^{(k-j)(s-s_-)},
2^{(k-j)(s-s_+)}\}\,
2^{js}\|\Pi_ju\|_2.
\tag{E39}
\]
For example insert \(2^{-k(s_--m)}\|T\Pi_ju\|_{H^{s_--m}}\), then use \(\|\Pi_ju\|_{H^{s_-}}\leq C2^{js_-}\|\Pi_ju\|_2\); the other endpoint is identical. The sequence
\(c_l=\min(2^{l(s-s_-)},2^{l(s-s_+)})\) is summable over \(l\in\mathbb Z\). For a nonnegative sequence \(v\),
\(\|c*v\|_{\ell^p}\leq\|c\|_{\ell^1}\|v\|_{\ell^p}\): for finite sums this is the triangle inequality for translations; monotone passage to the sum proves the assertion, also for \(p=1,\infty\). Equation (E39) thus bounds the output norm (E38).

For a general input of finite (E38) norm, the annular sum converges in \(H^{s_-}\), because its weighted \(\ell^2\) norm there is bounded by an exponentially decreasing sequence times a bounded sequence. Hence \(Tu\) is already defined by the lower endpoint. Passing to each fixed output projection and using (E39) proves the asserted Besov bound, even for \(p=\infty\), where finite annular sums need not converge in the Besov norm. For \(p<\infty\) those sums do converge in that norm by the tail property of \(\ell^p\).

Applying this implication to (E37), with any \(s_-<s<s_+\), proves
\[
\operatorname{Op}(a):B^s_{2,p}\longrightarrow B^{s-m}_{2,p}
\quad(1\leq p\leq\infty,\ s\in\mathbb R).
\tag{E40}
\]
All constants are controlled by finitely many symbol seminorms. Multiplication by any smooth function with all derivatives bounded is the order-zero special case; in particular it is continuous on every space in (E38). For a distribution \(u\) on an open set, its product with \(\chi\in C_c^\infty\) of that set extends by zero to a compactly supported tempered distribution. The local space is therefore defined by the seminorms \(\|\chi u\|_{B^s_{2,p}}\) of these extensions. Equivalent cutoff families follow by partitions of unity and this multiplication estimate. Coordinate invariance and the later microlocal assertions require their own geometric arguments; (E40) supplies their exact global continuity input.

## AN03-EUC-009 — Elliptic inversion uses a strictly positive gain

Assume \(\delta<\rho\), so \(\kappa>0\), and let \(a\in S^m_{\rho,\delta}\) be scalar. The following global ellipticity condition is equivalent to the existence of a symbol \(b\in S^{-m}_{\rho,\delta}\) with both products inverse modulo smoothing:
\[
|a(x,\xi)|\geq c\langle\xi\rangle^m
\quad\hbox{for all }x\hbox{ and }|\xi|\geq R,
\tag{E41}
\]
\[
a\circ b-I\in S^{-\infty},\qquad
b\circ a-I\in S^{-\infty}.
\tag{E42}
\]
Moreover either of the two relations in (E42), for a given \(b\), implies the other and determines \(b\) uniquely modulo \(S^{-\infty}\). Either implies
\[
ab-I\in S^{-\kappa}_{\rho,\delta}.
\tag{E43}
\]
In the classical case the gain in (E43) is one. For square matrices replace (E41) by \(\|a(x,\xi)v\|\geq c\langle\xi\rangle^m\|v\|\); all assertions remain true.

**Proof.** Normalize \(a\) pointwise by \(a_0=\langle\xi\rangle^{-m}a\). It belongs to \(S^0_{\rho,\delta}\). Condition (E41) makes its scalar reciprocal, or matrix inverse, uniformly bounded outside the ball. Choose a frequency cutoff \(\theta\) supported in that region and equal to one outside a larger ball. Define
\(b_0=\theta\langle\xi\rangle^{-m}a_0^{-1}\), extended by zero across the interior neighborhood where \(\theta=0\). The chain-rule/inverse estimates of AN03-EUC-001 show \(b_0\in S^{-m}_{\rho,\delta}\), and
\(ab_0=b_0a=I\) for sufficiently large \(|\xi|\). Thus (E21) gives
\(r=I-a\circ b_0\in S^{-\kappa}\) and
\(\ell=I-b_0\circ a\in S^{-\kappa}\).

For a right inverse take the formal series
\(\sum_{j\geq0}b_0\circ r^{\circ j}\), whose terms have orders \(-m-j\kappa\). Use (E6) to obtain a sum \(b_R\). Its first \(N\) terms satisfy the exact telescoping identity
\[
a\circ\sum_{j<N}b_0\circ r^{\circ j}=I-r^{\circ N}.
\tag{E44}
\]
Continuity of composition and the remainder order in (E6) show
\(a\circ b_R-I\in S^{-N\kappa}\) for every \(N\), hence it is smoothing. Similarly the series \(\sum_{j\geq0}\ell^{\circ j}\circ b_0\) gives \(b_L\) with \(b_L\circ a-I\) smoothing. The class \(S^{-\infty}\) is a two-sided ideal for composition with a finite-order symbol: apply (E19) at arbitrarily negative source orders. Therefore
\[
b_L-b_R=b_L\circ(I-a\circ b_R)
+(b_L\circ a-I)\circ b_R\in S^{-\infty}.
\tag{E45}
\]
Either choice is a two-sided inverse.

Conversely, a right relation in (E42) and (E21) with \(N=1\) give (E43). In fact (E43) alone implies (E41). Since \(\kappa>0\), \(ab\) is uniformly within \(1/2\) of \(I\) at large frequency. In the scalar case
\(1/2\leq|a||b|\leq C|a|\langle\xi\rangle^{-m}\), proving (E41). In the square matrix case \(ab\) is invertible there by the convergent geometric series in operator norm; a square matrix with a right inverse is invertible by finite-dimensional linear algebra, and \(\|a^{-1}\|=\|b(ab)^{-1}\|\leq C\langle\xi\rangle^{-m}\). A left relation works in the same way. The construction already gives a two-sided inverse \(c\), and if \(a\circ b-I\) is smoothing then
\(b-c=c\circ(a\circ b-I)-(c\circ a-I)\circ b\) is smoothing. The other side follows. This also proves uniqueness and covers a given one-sided inverse. ∎

The geometric-series argument here is formal in decreasing symbol orders, followed by (E6); no convergence of the operator Neumann series is assumed. At \(\delta=\rho\) the orders \(-m-j\kappa\) do not tend to \(-\infty\). The construction therefore makes no elliptic-parametrix claim at that endpoint. A positive lower bound for the order-zero symbol is a different fact from a positive symbolic remainder gain.

## AN03-EUC-010 — The exact constant-coefficient interface

The origin of more general symbol orders includes reciprocals of hypoelliptic polynomials. That implication has a separate other-volume prerequisite, **AN03-DEP-EUC-HYPO**: if a nonzero complex polynomial \(P\) defines a hypoelliptic constant-coefficient operator, meaning that \(P(D)u\) smooth implies \(u\) smooth on every open set for every distribution \(u\), then \(P(\xi)\ne0\) for all sufficiently large real \(|\xi|\), and there are constants \(c>0,C,R\) such that
\[
\left|\frac{\partial^\alpha P(\xi)}{P(\xi)}\right|
\leq C|\xi|^{-c|\alpha|}
\quad (\alpha\ne0,\ \xi\in\mathbb R^n,\ |\xi|>R).
\tag{E48}
\]
Only finitely many nonzero derivatives occur, so a common \(C\) is possible. This is the quantitative implication of Hörmander II, Theorem 11.1.3, with hypoellipticity as in Theorem 11.1.1/Definition 11.1.2. Its proof, including the algebraic growth theorem needed to pass from a qualitative limit to a power bound, remains an explicit external dependency; the symbol-space definition is not a proof of (E48).

Here is the complete adapter from that contract to the present calculus. If \(P\) has degree \(d>0\), replace \(c\) by \(\rho=\min(c,1)>0\). A derivative of total degree \(d\) is a nonzero constant for some multiindex, so (E48) yields \(|P(\xi)|^{-1}\leq C|\xi|^{-d\rho}\). Repeated differentiation of \(P^{-1}P=1\) expresses each derivative of \(P^{-1}\) as a finite sum of
\[
P^{-1}\prod_{\nu=1}^k
\frac{\partial^{\alpha_\nu}P}{P},
\qquad \alpha_\nu\ne0,\qquad
\alpha_1+\cdots+\alpha_k=\alpha,
\tag{E49}
\]
with numerical coefficients. Induction follows by differentiating one factor at a time, using the quotient rule; total derivative degree increases by one in each resulting term. Equation (E48) bounds (E49) by \(C_\alpha\langle\xi\rangle^{-d\rho-\rho|\alpha|}\). A smooth cutoff \(\theta\) that is zero on a sufficiently large ball and one outside a larger ball therefore gives
\(\theta(\xi)/P(\xi)\in S^{-d\rho}_{\rho,0}\), independent of \(x\).
Cutoff derivatives occur only in a compact region where \(P\ne0\) and do not change the conclusion. A nonzero constant polynomial has its constant reciprocal in \(S^0_{\rho,0}\) for any allowed \(\rho\). No reciprocal is asserted across real zeros of a nonconstant polynomial. Thus the adapter is proved, while the hypoellipticity characterization itself remains with its other-volume owner.

## AN03-EUC-EX-001 — Two exact products and an endpoint obstruction

For a bounded smooth matrix function \(B(x)\) with bounded derivatives and a constant matrix \(M\), take \(a(\xi)=M\xi_j\), \(b(x,\xi)=B(x)\). Formula (E21) terminates because \(a\) is frequency-linear:
\[
a\circ b=M\xi_jB+M D_jB,
\qquad b\circ a=BM\xi_j.
\tag{E46}
\]
One can also prove termination directly from \(MD_j(Bu)=MB D_ju+M(D_jB)u\); kernel injectivity identifies the symbols. The leading commutator contains \((MB-BM)\xi_j\), which has order one. Scalar Poisson-bracket cancellation cannot remove it.

For a scalar example, \(a(x,\xi)=2+\tfrac14\sin x_1+\langle\xi\rangle^2\) is uniformly elliptic of order two. The initial inverse is its ordinary reciprocal, of order minus two, but it is usually not the inverse symbol for composition. The first correction term in \(a\circ a^{-1}-1\) is
\(\sum_j(\partial_{\xi_j}a)D_j(a^{-1})\), which the general calculus places in order at most minus one. In this particular example its base derivatives give the sharper order minus three. The theorem corrects the error recursively without imposing any periodic-boundary or compact-base condition.

The loss of gain at equality is visible in one dimension. Fix \(0<r<1\), let \(R_j=2^{Lj}\) for a fixed large integer \(L\), and put \(\lambda_j=R_j^r\). Start the sequence at an index large enough that intervals of radius \(3\lambda_j\) about \(R_j\) are disjoint. Choose \(\varphi,\omega\in C_c^\infty(\mathbb R)\), supported in \((-2,2)\) and \((-1/10,1/10)\), respectively, with \(\omega(0)=1\) and \(\varphi(1)\ne\varphi(0)\). Define
\[
a(\xi)=\sum_j\varphi((\xi-R_j)/\lambda_j),
\qquad
b(x,\xi)=\sum_j e^{i\lambda_j x}
\omega((\xi-R_j)/\lambda_j).
\tag{E47}
\]
Disjoint supports and \(\langle\xi\rangle\asymp R_j\) on each term prove \(a,b\in S^0_{r,r}\): a base derivative costs \(\lambda_j\), and a frequency derivative costs \(\lambda_j^{-1}\). On the support of the \(j\)-th term of \(b\), the exact frequency-shift calculation after (E22) gives
\((a\circ b)(x,\xi)=e^{i\lambda_jx}a(\xi+\lambda_j)\omega((\xi-R_j)/\lambda_j)\).
At \(\xi=R_j\), the difference from \(ab\) has absolute value
\(|\varphi(1)-\varphi(0)|>0\). It therefore belongs to no strictly negative symbol order. Nevertheless (E28), (E37) and (E40) apply to both operators. This example separates boundedness from decreasing-order asymptotics.

## AN03-EUC-PS-001 — Problems with solutions

**Problem 1.** Let \(m_{2j}=-j\), \(m_{2j+1}=3-j\), and choose arbitrary \(a_j\in S^{m_j}_{\rho,\delta}\). What order is guaranteed for the remainder after the first four terms? Does summing the even terms first preserve the same meaning?

**Solution.** The remaining orders start with \(m_4=-2\), \(m_5=1\), \(m_6=-3\), \(m_7=0\); their maximum is one. Thus (E6) gives remainder order one after four terms. A genuine permutation of the natural numbers preserves the expansion modulo smoothing. The instruction “all even terms first, then all odd terms” is not a permutation indexed by the natural numbers, since no odd term occurs at a finite position. One may separately sum both subsequences and add the resulting two symbols; each tail still has orders tending to minus infinity, and (E6) verifies that the resulting sum has the original expansion. This is an additional two-sum construction, not a nonexistent enumeration.

**Problem 2.** In one dimension compute the exact left symbol of \(D^2 M_{e^{3ix}}\), where \(M_f\) denotes multiplication by \(f\). Check the coefficient of the first derivative term.

**Solution.** Since \(D(e^{3ix}u)=e^{3ix}(D+3)u\), the symbol is
\(e^{3ix}(\xi+3)^2=e^{3ix}(\xi^2+6\xi+9)\).
In (E21), the first derivative term is \((2\xi)D_xe^{3ix}=6\xi e^{3ix}\); the second is \((2)D_x^2e^{3ix}/2!=9e^{3ix}\). Higher frequency derivatives of \(\xi^2\) vanish. The sign is positive in the frequency shift, which agrees with (E13) and (E22).

**Problem 3.** Show explicitly why the proof of (E28) gives no uniform constant as \(\delta\uparrow1\), even when \(\delta\leq\rho\).

**Solution.** With fixed Taylor order \(K\), the error norms in (E32) sum to at most a constant times
\(\sum_{j\geq1}2^{-jK(1-\delta)}
=2^{-K(1-\delta)}/(1-2^{-K(1-\delta)})\).
This tends to infinity. The finite-band part remains bounded, but the estimate for the errors no longer sums at \(\delta=1\). This is a precise failure of this proof's uniform bound; it is not a proof that every particular type-\((1,1)\) operator is unbounded.

**Problem 4.** Construct a distribution in \(B^0_{2,\infty}\) that does not belong to \(H^0\), and explain why Schwartz density must not be used in the \(B^0_{2,\infty}\) proof.

**Solution.** For every \(j\geq1\), choose a smooth Fourier function \(f_j\) supported strictly inside \(A_j\), normalized so that the inverse Fourier transform has \(L^2\) norm one. The distribution with Fourier transform \(\sum_jf_j\) is tempered: on each annulus Cauchy–Schwarz bounds its pairing with a Schwartz function by that function's annular \(L^2\) norm, and those norms form a summable rapidly decreasing sequence. Every dyadic \(L^2\) norm is one, so its \(B^0_{2,\infty}\) norm is one, while its squared \(H^0\) norm is \(\sum_j1=\infty\). The tails of its finite annular sums all have Besov norm one. For any Schwartz function the annular norms tend to zero, so its distance from this distribution in that norm is at least one. The proof after (E39) instead uses convergence in a strictly weaker Sobolev space and estimates each fixed output band; it remains valid at the sequence endpoint.

**Problem 5.** Suppose \(a\in S^m_{\rho,\delta}\), \(\delta<\rho\), is square-matrix elliptic, \(b\in S^{-m}_{\rho,\delta}\), and \(a\circ b-I\) is smoothing. A proposed proof of \(b\circ a-I\) interchanges \(a\) and \(b\) in every differential coefficient. Identify the problem and give a valid replacement.

**Solution.** Matrix factors in (E21) do not commute, and the derivatives fall on different factors in the two orders. Even their leading products need not agree. Use (E43) to obtain a uniform inverse bound for the pointwise matrix \(a\), construct a two-sided parametrix \(c\) by (E44)–(E45), and compute
\(b-c=c\circ(a\circ b-I)-(c\circ a-I)\circ b\).
Both terms are smoothing because it is a two-sided ideal. Hence \(b\circ a-I=(b-c)\circ a+(c\circ a-I)\) is smoothing. Associativity and the ideal property replace commutativity.

**Problem 6.** Let \(a(x,\xi)=f(x)g(\xi)\), where \(f\in C^{n+1}(\mathbb R^n)\) and all its derivatives through order \(n+1\) are integrable, while \(g\) is only bounded and measurable. Prove \(L^2\) boundedness and state whether (E21) follows.

**Solution.** Condition (E34) holds with
\(M=\|g\|_\infty\sum_{|\alpha|\leq n+1}\|D^\alpha f\|_1\), so the rough-frequency theorem gives the asserted bound. It does not imply a differentiated composition formula: \(g\) need not have a first frequency derivative, whereas (E21) is a theorem about smooth symbols with all the specified derivative bounds. The simpler factorization is multiplication by \(f\) after the bounded Fourier multiplier \(g(D)\); the hypotheses also imply \(f\) is bounded, as follows from the integrable Fourier bound (E35).

## References and research directions

The mathematical antecedent for the assigned calculus is Lars Hörmander, *The Analysis of Linear Partial Differential Operators III: Pseudo-Differential Operators*, corrected second printing (1994), §18.1 and Appendix B.1. The metric and quadratic-multiplier framework used here is developed independently in AN03-U001, AN03-U002 and AN03-U004. Nicolas Lerner's author-hosted [first chapter](https://webusers.imj-prg.fr/~nicolas.lerner/ch1booklerner.pdf), Lemma 1.1.24 and Remark 1.1.28, compares classical summation and the parameter ranges; the [metric chapter](https://webusers.imj-prg.fr/~nicolas.lerner/ch2booklerner.pdf), Lemma 2.2.18 and Theorems 2.3.7 and 2.5.1, supplies further metric composition and boundedness readings. The checked chapter files have September 2009 metadata; their byte identities, rather than an assumed final-print edition, fix the comparison. Richard Melrose's [pseudodifferential-operator lectures](https://math.mit.edu/~rbm/18.157-F05.pdf), version 0.7E of November 29, 2006, provide another classical reading. The checked classical summation results do not themselves supply the entire \(\delta>\rho\) range or the Besov sequence endpoints proved here. These are comparison readings; no source prose, figures or exercises are imported.

The next structural questions have distinct hypotheses: coordinate changes introduce a lower bound on \(\delta\) relative to \(1-\rho\); positivity estimates depend on more than boundedness; and boundary kernels require additional structure near the normal-frequency directions. The endpoint example (E47) is a useful test for any proposed extension that claims a decreasing symbolic error at \(\delta=\rho\).

This independently written programme text carries CC0 1.0, as specified by the course license. Its proofs are relative to the explicit entry contracts and cited internal theorems. Independent mathematical, correspondence, prerequisite and expression review, followed by render verification, remain required.
