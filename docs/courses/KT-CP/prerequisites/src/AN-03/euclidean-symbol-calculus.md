# Symbols, operators and Sobolev scales

Frequency differentiation improves a symbol, while differentiation in the base variable may worsen it. The balance between those two effects controls an expansion. Boundedness requires a different argument: a decomposition into frequency bands continues to work when the two effects exactly balance. We develop these mechanisms separately, then combine them to construct inverses and act on Sobolev and Besov spaces.

We use the Fourier conventions proved in [Fourier transforms, finite spectra and convex separation](prerequisite-bridges.md) and applied in [Quadratic Fourier multipliers at a moving scale](gauss-transform-estimates.md): the forward kernel is \(e^{-ix\cdot\xi}\), inverse transformation has factor \((2\pi)^{-n}\), and \(D=-i\partial\). Fourier inversion and Plancherel, including their extension to \(L^2\), are explicit prerequisites. The additional entry contracts are completeness of \(L^2\), density of Schwartz functions in \(L^2\), the usual integration and dominated-convergence theorems for Lebesgue measure, Taylor's formula and the multivariable product rule. Distributional Fourier transformation, invertible linear pullback on tempered distributions, and the tempered Schwartz kernel theorem are the same explicit contracts as in Section 4 of [Two measuring scales, one Weyl product](weyl-metric-products.md). In particular the kernel theorem means that every continuous linear map \(\mathcal S(\mathbb R^n)\to\mathcal S'(\mathbb R^n)\) has exactly one kernel in \(\mathcal S'(\mathbb R^{2n})\), and conversely. Its full proof is [Sections4.1--4.5 of the Weyl-product lesson](weyl-metric-products.md#AN03-WP-KERNEL-001), including the exact global kernel and strong-dual maps. [Sections8.1--8.4 of the Fourier lesson](prerequisite-bridges.md#AN03-DEP-PARTIAL-001) prove partial transforms and the full original distributional and L2 extensions. [The Banach and measure lesson](banach-foundation-bridges.md#AN03-BFD-LP-003) supplies completeness and density; [the metric and calculus lesson](metric-foundation-bridges.md#AN03-MFD-CALC-006) supplies the complete Taylor and product maps.

The multiplier results in Sections 7–8 of [Quadratic Fourier multipliers at a moving scale](gauss-transform-estimates.md) and the classical metric verification in Section 8 of [Two measuring scales, one Weyl product](weyl-metric-products.md) are available here. We use those results with specified metrics below. All statements are for a fixed finite dimension. Scalar symbols may be replaced by matrices between fixed finite-dimensional complex Hermitian spaces: norms replace absolute values, products keep their displayed order, and adjoints are conjugate transposes. The inverse theorem uses square matrices and a lower bound for their smallest singular value. No infinite-dimensional operator-valued extension is implicit.

## 1. Symbol classes and the order budget

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

## 2. Summing symbol expansions and preserving support

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

## 3. Quantization, kernels and signs

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

## 4. Gaussian estimates for the product

Assume now \(\delta\leq\rho\). Set \(\kappa=\rho-\delta\). Section 8 of [Two measuring scales, one Weyl product](weyl-metric-products.md) applies to
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
For each output seminorm only finitely many input seminorms are used. These maps preserve convergence in the local smooth topology on bounded source sets. The phase convention matters: for \(A(p,q)=t p\cdot q\), the symmetric representative is \(t/2\) times the swap map, so the Gauss parameter is \(|t|\langle\xi\rangle^{-\kappa}/2\). The finite-bound theorem applies to the original metric itself; the complete receiving calculation below retains every parameter-dependent factor. This proves (E15) directly from Section 8 of [Quadratic Fourier multipliers at a moving scale](gauss-transform-estimates.md) with precisely the hypotheses checked in Section 8 of [Two measuring scales, one Weyl product](weyl-metric-products.md).

**The unchanged metric and its full remainder constants.**

Retain E14, E1's parameter range and the original weight \(m_a(X)=\langle\xi\rangle^m\). Assume \(\delta\leq\rho\) and set \(\kappa=\rho-\delta\geq0\), \(X=(x,\xi)\). The original metric is

\[
 g_X(y,\eta)=\langle\xi\rangle^{2\delta}|y|^2+
            \langle\xi\rangle^{-2\rho}|\eta|^2,\qquad
 m_a(X)=\langle\xi\rangle^m.
 \tag{EC5}
\]

For \(n\geq1\) and \(t\ne0\), the exact phase \(A_t(p,q)=tp\cdot q\) has the symmetric map

\[
 B_t=\frac t2\begin{pmatrix}0&I_n\\I_n&0\end{pmatrix},\qquad
 g_X(B_t(p,q))=\frac{t^2}{4}
 \bigl(\langle\xi\rangle^{2\delta}|q|^2+
       \langle\xi\rangle^{-2\rho}|p|^2\bigr).
 \tag{EC6}
\]

Taking the dual of this full positive quadratic form gives, on every original direction,

\[
 g_X^{A_t}(y,\eta)=\frac4{t^2}
 \bigl(\langle\xi\rangle^{2\rho}|y|^2+
       \langle\xi\rangle^{-2\delta}|\eta|^2\bigr)
 =\frac4{t^2}g_X^\sigma(y,\eta),\qquad
 h_{g,A_t}(X)=\frac{|t|}{2}\langle\xi\rangle^{-\kappa}
 \leq h_*=\frac{|t|}{2}.
 \tag{EC7}
\]

Indeed the ratio of each original metric coefficient to its phase-dual coefficient is \(t^2\langle\xi\rangle^{-2\kappa}/4\). Its positive square root is the exact supremum defining \(h\). No direction is lost. The phase-dual form is finite on the entire original space, since \(B_t\) is invertible.

For the original temperateness and weight inequalities, retain the exact comparison

\[
 1+g_Y^\sigma(X-Y)
 =1+\frac{t^2}{4}g_Y^{A_t}(X-Y)
 \leq\max(1,t^2/4)\bigl(1+g_Y^{A_t}(X-Y)\bigr).
 \tag{EC8}
\]

Thus every occurrence of an original metric constant \(C_g\) with distance exponent \(L_g\) becomes \(C_g\max(1,t^2/4)^{L_g}\), and each original weight constant \(C_m\) with its own exponent \(L_m\) becomes \(C_m\max(1,t^2/4)^{L_m}\). Local continuity and slow variation remain those of the unchanged \(g\) and unchanged weight. The [original Gauss finite-bound theorem G24--G26](gauss-transform-estimates.md#AN03-GAU-008) applies with \(h_*=|t|/2\). Its packing step is in dimension \(2n\) and retains the full factor \((1+|t|/2)^{2n}\), in addition to the original structural constants and their displayed changes. That factor alone does not describe all dependence on \(t\) of the theorem's constant.

For \(N,l\geq0\) and \(T_j=(y_j,\eta_j)\), its exact receiving estimate is

\[
 \begin{split}
 |\partial_{T_1}\cdots\partial_{T_l}R_{N,t}a(X)|
 &\leq C_{N,l,t}\langle\xi\rangle^m
       \left(\frac{|t|}{2}\langle\xi\rangle^{-\kappa}\right)^N\\
 &\quad{}\times
       \prod_{j=1}^{l}
       \left(\langle\xi\rangle^{2\delta}|y_j|^2+
             \langle\xi\rangle^{-2\rho}|\eta_j|^2\right)^{1/2}
       p_{\leq J_{N,l,t}}(a;m_a,g),\\
 R_{N,t}a&=Q_ta-\sum_{j<N}\frac{(iA_t(D))^j}{j!}a .
 \end{split}
 \tag{EC9}
\]

The constants and finite derivative budget carry the actual unchanged local metric constants, the full EC8 temperateness/weight constants and the finite \(h_*\) counting constants. For coordinate derivatives \(\alpha\) in \(\xi\) and \(\beta\) in \(x\), choose the corresponding coordinate directions in EC9. Their product is \(\langle\xi\rangle^{-\rho|\alpha|+\delta|\beta|}\). Hence

\[
 |\partial_\xi^\alpha\partial_x^\beta R_{N,t}a(X)|
 \leq C_{N,\alpha,\beta,t}
       (|t|/2)^N
       \langle\xi\rangle^{m-N\kappa-\rho|\alpha|+\delta|\beta|}
       p_{\leq J_{N,\alpha,\beta,t}}(a;m_a,g).
 \tag{EC10}
\]

The source metric seminorms are exactly controlled by finitely many E2 coordinate seminorms: expand each directional derivative into its \(2n\) coordinate components and use \(|y_k|\leq\langle\xi\rangle^{-\delta}g_X(T)^{1/2}\) and \(|\eta_k|\leq\langle\xi\rangle^\rho g_X(T)^{1/2}\). Each ordered product expansion has finitely many terms, at most \((2n)^l\) at order \(l\), and all factors remain. Conversely insert the coordinate directions to bound each coordinate seminorm by its metric seminorm. Thus EC10 proves the original E15 class inclusion with finite E2 source-seminorm control, retaining the full \((|t|/2)^N\) rather than replacing its value by one.

The Taylor coefficients are the original ones:

\[
 \begin{split}
 \sum_{j<N}\frac{(iA_t(D))^j}{j!}a
 &=\sum_{j<N}\sum_{|\alpha|=j}
       \frac{i^j t^j}{\alpha!}D_x^\alpha D_\xi^\alpha a\\
 &=\sum_{j<N}\sum_{|\alpha|=j}
       \frac{i^j(-i)^jt^j}{\alpha!}
       \partial_\xi^\alpha D_x^\alpha a
 =\sum_{|\alpha|<N}\frac{t^{|\alpha|}}{\alpha!}
       \partial_\xi^\alpha D_x^\alpha a .
 \end{split}
 \tag{EC11}
\]

For \(N=0\) the sum is empty and \(R_{0,t}=Q_t\). The finite-bound theorem also gives bounded-set local smooth convergence, continuity and uniqueness on the original symbol class. When \(t=0\), \(Q_0=I\): for \(N\geq1\) the term of order zero is \(a\) and all positive-order terms vanish, so the remainder is exactly zero; for \(N=0\) the remainder is \(a\). These cases use the identity directly, without assigning a phase-dual metric or evaluating a zero denominator. If \(n=0\) all symbols are functions on a one-point space and the phase is zero for every \(t\); the same identity argument applies. For \(\kappa=0\) the estimate has no improving frequency order. None of these arguments rescale or replace the original \(g\).

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
If \(s>2r\), then \(d>s/2\), so the same expression is at least \(s^{2(1-\delta)}/4\); choosing a sufficiently large power bounds \(s/r\leq s\). These inequalities control the ratio of the two frequency coefficients of (E17), every real power weight \(r^q\), and their reciprocals. The base coefficient is constant. Slow variation follows from \(\rho\leq1\) and the Lipschitz inequality for \(\langle\eta\rangle\); the same comparison proves local continuity of \(r^q\). Thus every condition of the observation-point form of Sections 7–8 of [Quadratic Fourier multipliers at a moving scale](gauss-transform-estimates.md) holds, with constants independent of \(x,\xi,y\).

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

## 5. Adjoints and composition

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

Choose compactly supported smooth approximants \(a_j,b_j\) as at the end of Section 4. Their symbols and products remain bounded in their respective orders and converge locally smoothly. For any fixed \(u\in\mathcal S\), (E10) and dominated convergence give local smooth convergence of the outputs. The Schwartz estimates of Section 3 bound all output Schwartz seminorms uniformly. Local convergence plus those stronger uniform seminorms gives convergence in every Schwartz seminorm: outside a large base ball use one extra power of \(\langle x\rangle\), and inside use local convergence. Thus \(\operatorname{Op}(a_j)u\to\operatorname{Op}(a)u\) in \(\mathcal S\), and similarly for \(b_j\) and their products. Boundedness of the Schwartz operator seminorms allows passage through the double composition. This proves (E19) on \(\mathcal S\).

Taking adjoints there identifies the transpose of the product with the reverse product of the transposes. Apply their continuous extensions to \(\mathcal S'\) and test against \(\mathcal S\) to obtain (E19) on \(\mathcal S'\). Equivalently, the identities of pairings determine the extension uniquely. Kernel injectivity proves associativity of \(\circ\) and that the constant symbol \(I\) is its unit. ∎

When \(\delta<\rho\), (E20)–(E21) are asymptotic expansions in decreasing orders. When \(\delta=\rho<1\), closure and every finite remainder estimate survive, but all their target orders are the original order. Taking more terms then supplies no smoothing assertion. This distinction will be used in the inverse construction.

## 6. A finite-derivative \(L^2\) estimate

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
\(\sup_s\int|K(s,t)|\,dt\leq B\), then its canonical pairing operator has \(L^2\) norm at most \(\sqrt{AB}\). The raw integral agrees globally under semifinite output measure, as proved below. Pointwise Cauchy--Schwarz gives
\[
\left|\int K(s,t)u(t)\,dt\right|^2
\leq\left(\int|K(s,t)|\,dt\right)
\left(\int|K(s,t)||u(t)|^2\,dt\right).
\tag{E24}
\]
On semifinite output measures, integration in \(s\) on finite pieces by Tonelli and the global recovery below give \(AB\|u\|_2^2\). The raw integral therefore supplies the bounded extension there. This includes continuous kernels with equal marginal bound \(A=B=C\) and norm at most \(C\).

**The exact measure-space interpretation.** For arbitrary measure spaces, the operator in the preceding statement is the canonical pairing operator, not an unrestricted raw-integral operator. Write \(\mu\) for the output measure in \(s\) and \(\nu\) for the input measure in \(t\). Their original constants are column \(A\) and row \(B\); this is \(A_{\rm SC}=B\), \(B_{\rm SC}=A\) in [the complete Schur proof, Section1.1](totally-characteristic-operators.md#AN03-TC-SCHUR-001). Joint product measurability is required.

For finite-valued representatives \(u\in L^2(\nu)\) and \(v\in L^2(\mu)\), their actual supports are sigma-finite, since
\[
 S_u=\bigcup_{k\geq1}\{|u|>1/k\},\qquad
 \nu\{|u|>1/k\}\leq k^2\|u\|_2^2,
\]
and the same bound holds for \(v\). On the original restricted product \(S_v\times S_u\), Tonelli and Cauchy--Schwarz therefore prove
\[
 \begin{split}
 b_K(u,v)&=\int_{S_v}\int_{S_u}
               K(s,t)u(t)\overline{v(s)}\,d\nu(t)\,d\mu(s),\\
 \int_{S_v\times S_u}|K|\,|u|^2\,d(\mu\otimes\nu)&\leq A\|u\|_2^2,\\
 \int_{S_v\times S_u}|K|\,|v|^2\,d(\mu\otimes\nu)&\leq B\|v\|_2^2,\\
 |b_K(u,v)|&\leq\sqrt{AB}\|u\|_2\|v\|_2.
 \end{split}
 \tag{E24a}
\]
Absolute convergence also proves invariance under changing the original null representatives and sesquilinearity. The complete Hilbert representation argument SC10--SC13 gives the unique operator \(T_K\) with \(\langle T_Ku,v\rangle=b_K(u,v)\) and \(\|T_K\|\leq\sqrt{AB}\), including both zero-constant cases.

SC14--SC23 prove the raw integral's measurability and existence on every finite output piece, the exact finite-piece comparison with \(T_Ku\), and the onto isometry \(L^2(\mu)\to F_\mu/N_\mu\). The raw representative has class \(i_\mu(T_Ku)\). Under semifinite output measure SC24 proves that the divergent set is globally null and that this raw representative equals \(T_Ku\) in the original global \(L^2(\mu)\). The explicit SC2--SC6 counterexample shows why truncation alone cannot establish this global assertion on arbitrary output measures.

In every application below the measure is Lebesgue measure, or its original multiple \(d\mu(q,p)=(2\pi)^{-n}dq\,dp\), hence is sigma-finite and semifinite. Indeed the boxes \([-k,k]^{2n}\) have their exact finite phase-space measures \((2\pi)^{-n}(2k)^{2n}\) and exhaust the space. A measurable set with positive measure then has a positive finite-measure intersection with one of these boxes. The same proof applies to the ordinary position and frequency measures. Thus the raw integral and all bounds below have the proved meaning. The finite matrix case keeps the original operator norm and both vector dimensions, exactly as SC26 proves.

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

Consider the matrix of \(A=\operatorname{Op}(a)\) between two packets, with output packet \((q,p)\) and input packet \((q',p')\). Substitute \(x=q+s\), \(\xi=p'+t\) in (E10). The integral below is the amplitude of this matrix; its full scalar phase is computed immediately afterward:
\[
(2\pi)^{-n}\iint
e^{i[s\cdot(p'-p)+t\cdot(q-q')]}
e^{is\cdot t}a(q+s,p'+t)\widehat\phi(t)\overline{\phi(s)},ds\,dt.
\tag{E26}
\]

Keep the original \(\phi_{q,p}(x)=e^{ip\cdot x}\phi(x-q)\), its \(L^2\) norm one, \(d\mu(q,p)=(2\pi)^{-n}dq\,dp\), and the linear-first pairing. Directly changing variables in the original forward transform gives

\[
 \widehat{\phi_{q',p'}}(\xi)
 =e^{-iq'\cdot(\xi-p')}\widehat\phi(\xi-p').
 \tag{EC12}
\]

Insert this expression into E10 and pair with \(\phi_{q,p}\). With \(x=q+s\) and \(\xi=p'+t\), the full phase before any grouping is

\[
 (q+s)\cdot(p'+t)-q'\cdot t-p\cdot(q+s)
 =q\cdot(p'-p)+s\cdot(p'-p)
  +t\cdot(q-q')+s\cdot t.
 \tag{EC13}
\]

Consequently the actual original packet matrix is

\[
 \begin{split}
 (\operatorname{Op}(a)\phi_{q',p'},\phi_{q,p})
 &=e^{iq\cdot(p'-p)}(2\pi)^{-n}
   \iint e^{i[s\cdot(p'-p)+t\cdot(q-q')]}\\
 &\quad{}\times e^{is\cdot t}
       a(q+s,p'+t)\widehat\phi(t)\overline{\phi(s)}\,ds\,dt .
 \end{split}
 \tag{EC14}
\]

The integration measure is \(ds\,dt\): the comma before \(ds\) in the previous E26 is typographical punctuation, not an amplitude factor. All scalar phase factors, the original inverse Fourier multiplier and the matrix order remain. The omitted factor has absolute value one for these real packet parameters, so E27's absolute-value estimate and both Schur marginals remain valid. It is independent of \(s,t\) and therefore survives every displayed integration by parts unchanged.

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

Two consequences also isolate the lower-order mechanisms in the classical calculus. If \(a\in S^q_{\rho,\delta}\) with \(q<-n\), its kernel is an ordinary continuous function. Every \((x-y)^\alpha K_a(x,y)\) is the inverse-frequency transform multiplied by the exact power of \(i\) specified below, applied to \(\partial_\xi^\alpha a\). That derivative has integrable absolute value uniformly in \(x\). Dominated convergence on compact base sets proves continuity. The needed integration by parts uses a cutoff first and then lets it tend to one.

For the original inverse-frequency kernel E12, differentiating \(a\) in \(\xi\) and integrating by parts gives

\[
 K_{\partial_\xi^\alpha a}(x,y)
 =(-i)^{|\alpha|}(x-y)^\alpha K_a(x,y),\qquad
 (x-y)^\alpha K_a(x,y)
 =i^{|\alpha|}K_{\partial_\xi^\alpha a}(x,y).
 \tag{EC15}
\]

These are also exact distributional identities: frequency differentiation is multiplication by \(-i(x-y)\) under the inverse transform, proved by testing the defining tempered transforms. When \(q<-n\), every displayed frequency derivative is integrable uniformly in \(x\). For an ordinary integration proof insert a smooth compact cutoff \(\chi(\xi/R)\). Each boundary term contains a positive cutoff derivative, at least one factor \(R^{-1}\), and lies where \(|\xi|\) is of order \(R\). The earlier intermediate estimate claimed an absolute bound by a constant times \(R^{n+q-|\alpha|}\), or a smaller power; this exponent is valid when \(\rho=1\) but is excessive in the general range \(0<\rho<1\). The following correction keeps the entire product rule and proves the actual vanishing bound.

The convergence still follows from \(q<-n\), with every original derivative factor retained. Choose the original cutoff to equal one on \(|\xi|\leq c_0\) and vanish on \(|\xi|\geq c_1\), with \(0<c_0<c_1\). Take \(R\geq\max(1,c_0^{-1})\). The complete derivative is
\[
 \partial_\xi^\alpha\bigl(a(x,\xi)\chi(\xi/R)\bigr)
 =\sum_{\beta\leq\alpha}{\alpha\choose\beta}
   (\partial_\xi^{\alpha-\beta}a)(x,\xi)
   R^{-|\beta|}(\partial^\beta\chi)(\xi/R).
 \tag{EC16}
\]
For each \(0<\beta\leq\alpha\), put \(s_\beta=q-\rho|\alpha-\beta|<0\). Its original annular support lies in \(c_0R\leq|\xi|\leq c_1R\). On this set \(\langle\xi\rangle^{s_\beta}\leq c_0^{s_\beta}R^{s_\beta}\). Equation E2 and the original coordinate volume therefore give, with \(\omega_n\) the volume of the Euclidean unit ball,
\[
 \begin{split}
 &\int\left\|{\alpha\choose\beta}
       (\partial_\xi^{\alpha-\beta}a)(x,\xi)
       R^{-|\beta|}(\partial^\beta\chi)(\xi/R)\right\|\,d\xi\\
 &\qquad\leq{\alpha\choose\beta}\,
       p_{q,|\alpha-\beta|}(a)\,
       \|\partial^\beta\chi\|_\infty\,
       \omega_nc_1^n c_0^{q-\rho|\alpha-\beta|}
       R^{n+q-\rho|\alpha-\beta|-|\beta|}.
 \end{split}
 \tag{EC17}
\]
Every factor is retained, and the bound is uniform in the original base point. Because \(\rho>0\) and \(|\beta|\geq1\), every exponent is at most \(n+q-1<0\). Thus every boundary term tends to zero. The term \(\beta=0\) converges in absolute integral by dominated convergence against the integrable original \(\partial_\xi^\alpha a\). The integration-by-parts phase has absolute value one, so these are sufficient absolute bounds for that passage. This proves EC15 as an ordinary integral with its exact power of \(i\). When \(|\alpha|=0\), there are no boundary terms; in dimension zero there is no positive frequency multiindex. The resulting absolute kernel and norm conclusions remain unchanged.

Here is an exact counterexample to the excessive earlier absolute exponent. Take \(n=1\), \(0<\rho<1\), \(\delta=0\), and \(q<-1\). Choose smooth \(\theta\) equal to zero for \(\xi\leq1\) and one for \(\xi\geq2\). Define \(a(\xi)=0\) for \(\xi\leq1\) and \(a(\xi)=\theta(\xi)\xi^q e^{i\xi^{1-\rho}}\) for \(\xi>1\). It is smooth at the join, and for \(\xi\geq2\) every derivative has the full finite form
\[
 a^{(j)}(\xi)=e^{i\xi^{1-\rho}}
       \sum_{k=0}^j C_{j,k}\xi^{q-j+k(1-\rho)},
 \qquad C_{0,0}=1,
 \tag{EC18}
\]
where coefficients outside \(0\leq k\leq j\) are zero and direct differentiation gives
\[
 C_{j+1,k}=\bigl(q-j+k(1-\rho)\bigr)C_{j,k}
                  +i(1-\rho)C_{j,k-1}.
 \tag{EC19}
\]
Each exponent is at most \(q-\rho j\). On the compact transition interval all terms of the product with \(\theta\) are bounded with the original binomial coefficients; there are no position derivatives. Hence \(a\in S^q_{\rho,0}\) with the original E2 seminorms. On the positive tail,
\[
 |a'(\xi)|=\left|q\xi^{q-1}+i(1-\rho)\xi^{q-\rho}\right|
                 \geq(1-\rho)\xi^{q-\rho}.
 \tag{EC20}
\]
A smooth compact cutoff which equals one near zero must have a nonzero derivative on some positive interval; continuity supplies a closed interval \(J\subset(0,\infty)\) on which \(|\chi'|\) is bounded below by a positive constant. For \(R\) large enough that \(RJ\subset[2,\infty)\), the original \(\alpha=2,\beta=1\) boundary term satisfies
\[
 \int_{RJ}\left|2a'(\xi)R^{-1}\chi'(\xi/R)\right|\,d\xi
 \geq2(1-\rho)R^{q-\rho}
            \int_J t^{q-\rho}|\chi'(t)|\,dt>0.
 \tag{EC21}
\]
The last integral is a fixed positive number. Division by the earlier proposed power \(R^{q-1}\) gives growth by \(R^{1-\rho}\), so that stronger absolute bound fails. This is a lower bound for the absolute integral of this particular full product-rule term; it does not assert a lower bound for its oscillatory integral or for a sum with cancellation. The corrected EC17 bound still tends to zero and proves the unchanged original identity and its receiving estimates.

The full kernel estimate is
\(|K_a(x,y)|\leq C_N\langle x-y\rangle^{-N}\) for every \(N\). Taking \(N>n\) verifies both marginals in (E24). For classical symbols this proves boundedness at all sufficiently negative orders without the packet estimate. If boundedness is known at order \(2q\), the identity \(\|\operatorname{Op}(a)u\|_2^2=(\operatorname{Op}(a^\dagger\circ a)u,u)\) proves it at order \(q\), since the composed symbol has order \(2q\). A finite number of doublings brings any fixed \(q<0\) below \(-n\). This proves boundedness at every negative order, including order minus one.

For scalar classical \(a\in S^0\), choose \(M>\sup|a|^2\) with a fixed positive gap and set \(c=(M-|a|^2)^{1/2}\in S^0\), using Section 1. Equations (E20)–(E21) give
\(a^\dagger\circ a+c^\dagger\circ c=M+r\), \(r\in S^{-1}\).
Taking the quadratic form on Schwartz functions and discarding \(\|\operatorname{Op}(c)u\|_2^2\geq0\) proves order-zero boundedness from the negative-order result. Thus the classical square-root argument is justified in full, while the packet and band argument below supplies the additional equality endpoint where a decreasing remainder is unavailable.

## 7. \(L^2\) boundedness at equal derivative costs

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

## 8. Sobolev and Besov mapping

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

**Editorial extension: the same original annuli for every positive sequence exponent.**
The restriction \(p\ge1\) in (E38)--(E40) is unnecessary for the mapping theorem. The smaller exponents give complete metric vector spaces, with the following exact proofs. Retain every original annulus \(A_j\), sharp projection \(\Pi_j\), Fourier convention, and weight \(2^{js}\). For \(0<p<1\), put
\[
N_{s,p}(u)=\left(\sum_{j\ge0}(2^{js}\|\Pi_ju\|_2)^p\right)^{1/p},
\qquad d_{s,p}(u,v)=N_{s,p}(u-v)^p.
\tag{BQ1}
\]
The domain is the same locally square-integrable Fourier domain as in (E38), with finite displayed sum. For \(a,b\ge0\), \((a+b)^p\le a^p+b^p\): after treating \(a=0\) separately, differentiate \((1+t)^p-1-t^p\) for \(t>0\). Its derivative is \(p((1+t)^{p-1}-t^{p-1})<0\), and its limit at zero is zero. The original \(L^2\) triangle inequality, followed by this inequality and summation, proves
\[
N_{s,p}(u+v)^p\le N_{s,p}(u)^p+N_{s,p}(v)^p,
\qquad N_{s,p}(zu)=|z|N_{s,p}(u).
\tag{BQ2}
\]
If the sum vanishes, every original Fourier piece vanishes, hence the distribution vanishes. Thus \(d_{s,p}\) is a translation-invariant metric; scalar multiplication is continuous because of homogeneity and (BQ2). No norm triangle inequality is required for this assertion.

Here is the exact annular reconstruction and completeness argument. Choose arbitrary \(F_j\in L^2(A_j)\), extended by zero, with
\(v_j=2^{js}(2\pi)^{-n/2}\|F_j\|_2\) in \(\ell^p\). Then \(v_j\le\|v\|_{\ell^p}\). Define \(F=\sum_jF_j\) on the disjoint original annuli, and define its inverse Fourier distribution by
\[
\langle u,\varphi\rangle=(2\pi)^{-n}\sum_{j\ge0}
       \int_{A_j}F_j(\xi)\widehat\varphi(-\xi)\,d\xi.
\tag{BQ3}
\]
For \(j\ge1\), retain the actual volume bound \(|A_j|\le\omega_n2^{jn}\). If \(C_N=\sup_\xi\langle\xi\rangle^N|\widehat\varphi(-\xi)|\), Cauchy--Schwarz bounds the absolute value of the \(j\)-th summand, including its Fourier factor, by
\((2\pi)^{-n/2}\omega_n^{1/2}2^NC_N2^{j(n/2-s-N)}v_j\).
Choose an integer \(N>n/2-s\). The complete geometric tail converges. The \(j=0\) term is at most \((2\pi)^{-n/2}v_0\|\widehat\varphi\|_{L^2(A_0)}\). These estimates also prove continuity in a finite Schwartz seminorm and continuous passage from the displayed sequence metric to \(\mathcal S'\). The actual Fourier transform is \(F\); every compact frequency set meets finitely many original annuli, so it is locally \(L^2\). Plancherel gives \(\|\Pi_ju\|_2=(2\pi)^{-n/2}\|F_j\|_2\), with the original factor retained. This is an onto isometry for (BQ1) between its domain and the weighted sequence of original Hilbert spaces.

For a Cauchy sequence \(u^{(r)}\) in \(d_{s,p}\), each weighted Fourier piece is Cauchy in its actual Hilbert norm. Let \(F_j\) be its limit. For every fixed \(r\), finite partial sums and their increasing limit give
\[
\sum_j\left(2^{js}(2\pi)^{-n/2}
       \|\widehat{\Pi_ju^{(r)}}-F_j\|_2\right)^p
\le\liminf_{t\to\infty}N_{s,p}(u^{(r)}-u^{(t)})^p.
\tag{BQ4}
\]
One fixed \(r\) and (BQ2) show that the limiting sequence has finite sum. Equation (BQ3) constructs its distribution \(u\). The Cauchy bound in (BQ4) then gives \(d_{s,p}(u^{(r)},u)\to0\). Thus the metric is complete, with the full original Fourier domain, rather than a completion containing unidentified objects. Finite annular sums converge in this metric by the tail of the actual \(\ell^p\) sum.

All earlier comparisons retain their original constants. On each \(A_j\), \(2^{-j}\langle\xi\rangle\) lies between \(1/2\) and \(\sqrt2\), also when \(j=0\). For every real \(t\), set
\[
a_t=\min(2^{-t},2^{t/2}),\qquad b_t=\max(2^{-t},2^{t/2}).
\]
Then \(a_t2^{jt}\|\Pi_ju\|_2\le\|\Pi_ju\|_{H^t}\le b_t2^{jt}\|\Pi_ju\|_2\). In particular, for \(\varepsilon=s-s_->0\), disjointness of the original annuli gives
\[
\|u\|_{H^{s_-}}^2
 =\sum_j\|\Pi_ju\|_{H^{s_-}}^2
 \le {b_{s_-}^2\over1-2^{-2\varepsilon}}N_{s,p}(u)^2.
\tag{BQ5}
\]
The same bound for tails proves convergence of the annular sum in the actual lower-endpoint Sobolev space.

For completeness, take smooth dyadic multipliers \(\phi_k\) with \(\sum_k\phi_k=1\), \(\sup_k\|\phi_k\|_\infty\le M\), and \(\phi_k|_{A_j}=0\) unless \(|k-j|\le L\), including the low piece. The original Fourier multiplier and the \(L^2\) triangle inequality give
\[
\begin{aligned}
\sum_k(2^{ks}\|\phi_k(D)u\|_2)^p
 &\le M^p2^{p|s|L}(2L+1)\sum_j(2^{js}\|\Pi_ju\|_2)^p,\\
\sum_j(2^{js}\|\Pi_ju\|_2)^p
 &\le 2^{p|s|L}(2L+1)\sum_k(2^{ks}\|\phi_k(D)u\|_2)^p.
\end{aligned}
\tag{BQ6}
\]
The first uses \(\phi_k(D)u=\sum_{|j-k|\le L}\phi_k(D)\Pi_ju\); the second uses \(\Pi_ju=\sum_{|k-j|\le L}\Pi_j\phi_k(D)u\). Each sum is finite. Apply (BQ2) to each sum, then count at most \(2L+1\) appearances of each input. Thus the same smooth-cutoff space is obtained for these exponents as well.

Retain precisely the two consistent endpoint maps in (E39), with operator norms \(M_-\) and \(M_+\). They give that formula with, for example,
\(C=\max(M_-b_{s_-}/a_{s_--m},M_+b_{s_+}/a_{s_+-m})\).
For finite annular input sums put \(v_j=2^{js}\|\Pi_ju\|_2\) and \(y_k=2^{k(s-m)}\|\Pi_kTu\|_2\). Equation (E39) gives \(y_k\le C\sum_jc_{k-j}v_j\), with its unchanged sequence \(c_l\). For \(0<p<1\), (BQ2), now for nonnegative scalars, gives the exact replacement for the convex triangle step:
\[
\begin{aligned}
\sum_{k\ge0}y_k^p
 &\le C^p\sum_{k,j\ge0}c_{k-j}^pv_j^p
 \le C^p\left(\sum_{l\in\mathbb Z}c_l^p\right)\sum_{j\ge0}v_j^p,\\
\sum_{l\in\mathbb Z}c_l^p
 &=1+{2^{-p(s-s_-)}\over1-2^{-p(s-s_-)}}
       +{2^{-p(s_+-s)}\over1-2^{-p(s_+-s)}}.
\end{aligned}
\tag{BQ7}
\]
Both denominators are positive. For a general input, (BQ5) defines \(Tu\) by the original lower endpoint. Annular input partial sums converge there; each fixed output projection converges in \(L^2\), since its Sobolev weight has a positive lower bound on its original annulus. Finite output sums, then their increasing limit, pass (BQ7) to this actual \(Tu\). Consequently its target metric is finite, and the map is continuous, with norm bound \(C(\sum_lc_l^p)^{1/p}\). This proves the implication without supposing a norm triangle inequality for \(p<1\), and without redefining \(T\).

Apply the proved implication to the actual operator (E37). Combining it with the original proof for \(p\ge1\) yields
\[
\operatorname{Op}(a):B^s_{2,p}\longrightarrow B^{s-m}_{2,p}
\quad(0<p\le\infty,\ s\in\mathbb R),
\tag{BQ8}
\]
under the original hypotheses (E1), \(\delta\le\rho\), and \(a\in S^m_{\rho,\delta}\). For \(p<1\) the displayed Besov space means (BQ1); for the earlier exponents it means (E38). All bounds still use finitely many original symbol seminorms. Finite-dimensional vector norms follow by the same Hilbert and triangle arguments; every matrix product in the original composition remains ordered.

The multiplication special case and local definition after (E40) now hold for every positive \(p\). To check the cutoff-family assertion explicitly, let a finite partition \(\sum_i\psi_i=1\) on a neighborhood of \(\operatorname{supp}\chi\) be subordinate to regions on which test cutoffs \(\chi_i\) are one. Then \(\chi u=\sum_i(\chi\psi_i)(\chi_i u)\). Each multiplier is smooth with bounded derivatives. Apply (BQ8) to each term and (BQ2) to the finite sum for \(p<1\); use the original triangle estimate for the other exponents. A locally finite family reduces to such a finite family on the actual compact support. This proves the equivalence of the corresponding local membership tests. It makes no coordinate-invariance claim.

The added exponents do change the space. For \(n\ge1\), choose \(F_j\) supported in the original \(A_j\), with \((2\pi)^{-n/2}\|F_j\|_2=(1+j)^{-a}\), \(j\ge1\), and \(F_0=0\). The annular reconstruction is (BQ3). Its \(H^0\) norm squared is exactly \(\sum_{j\ge1}(1+j)^{-2a}\), whereas its \(B^0_{2,p}\) metric to zero is exactly \(\sum_{j\ge1}(1+j)^{-ap}\). Comparing each decreasing power with its integral on consecutive unit intervals proves convergence precisely when the exponent is greater than one. Thus \(1/2<a\le1/p\) gives an actual \(H^0\) element outside \(B^0_{2,p}\). This is a proved editorial consequence of the original annular construction.

## 9. Elliptic inversion

The parameters satisfy \(0<\rho\leq1\), \(0\leq\delta<\rho\), \(m\in\mathbb R\), and \(\kappa=\rho-\delta>0\). Every ellipticity bound below has constants \(c>0\) and \(R\geq0\), uniform in the displayed original base variable. The matrix norm is the induced norm of its original vector norm.

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

**Proof.** On the original elliptic region the entire original matrix \(a(x,\xi)\) is invertible and its inverse satisfies
\(\|a(x,\xi)^{-1}\|\leq c^{-1}\langle\xi\rangle^{-m}\).
The full ordered derivative recurrence and every resulting constant are calculated in Section9.1 below, giving all original \(S^{-m}_{\rho,\delta}\) inverse estimates. Choose the actual frequency cutoff \(\theta\), supported in that invertibility region and equal to one outside a larger ball. Define
\(b_0=\theta a^{-1}\), extended by zero across the interior neighborhood where \(\theta=0\). The complete cutoff product in Section9.1 proves \(b_0\in S^{-m}_{\rho,\delta}\) and retains
\(ab_0=b_0a=\theta I\) at every frequency. The full composition remainder (E21), with its actual bounded-frequency term \((1-\theta)I\), therefore gives
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
\(1/2\leq|a||b|\leq C|a|\langle\xi\rangle^{-m}\), proving (E41). In the square matrix case \(ab\) is invertible there by the convergent geometric series in operator norm; a square matrix with a right inverse is invertible by finite-dimensional linear algebra, and \(\|a^{-1}\|=\|b(ab)^{-1}\|\leq C\langle\xi\rangle^{-m}\). Starting instead with a left relation, (E21) gives \(ba-I\in S^{-\kappa}_{\rho,\delta}\). At sufficiently large \(|\xi|\), \(ba\) is invertible, hence so is the square matrix \(a\), with \(a^{-1}=(ba)^{-1}b\) and \(\|a^{-1}\|\le C\langle\xi\rangle^{-m}\). Differentiating \(a^{-1}a=I\) gives its \(S^{-m}_{\rho,\delta}\) bounds there. The exact ordered identity \(ab-I=a(ba-I)a^{-1}\) places \(ab-I\) in \(S^{-\kappa}_{\rho,\delta}\) at large frequency. On the remaining compact frequency region, the smooth symbol also belongs to that class. Thus (E43) follows from either side. The construction already gives a two-sided inverse \(c\), and if \(a\circ b-I\) is smoothing then
\(b-c=c\circ(a\circ b-I)-(c\circ a-I)\circ b\) is smoothing. The other side follows. This also proves uniqueness and covers a given one-sided inverse. ∎

The geometric-series argument here is formal in decreasing symbol orders, followed by (E6); no convergence of the operator Neumann series is assumed. At \(\delta=\rho\) the orders \(-m-j\kappa\) do not tend to \(-\infty\). The construction therefore makes no elliptic-parametrix claim at that endpoint. A positive lower bound for the order-zero symbol is a different fact from a positive symbolic remainder gain.

### 9.1. The full inverse of the original symbol

The inverse theorem requires derivative estimates before its finite composition errors can be corrected. The original symbol \(a(x,\xi)\), all of its entries and every derivative remain the working object. The original symbol estimates, composition map and support-controlled asymptotic sum are those proved in Euclidean Sections1/2/4/5. Their original constants and full remainders are retained.

Let \(a\) be scalar or a square finite matrix in \(S^m_{\rho,\delta}\), where \(0<\rho\leq1\), \(0\leq\delta<\rho\), \(m\in\mathbb R\), and \(\kappa=\rho-\delta>0\). Retain the entire original ellipticity assumption:

\[
\|a(x,\xi)v\|\geq c\langle\xi\rangle^m\|v\|
\quad\hbox{for every original }x,\ |\xi|\geq R,\ v,
\qquad\langle\xi\rangle=(1+|\xi|^2)^{1/2}.
\tag{OI1}
\]

For a scalar, take the ordinary complex modulus. The matrix norm is the induced operator norm of the displayed original vector norm. No change of basis or discarded coefficient is implicit. This lower bound makes \(a(x,\xi)\) injective, hence invertible because its domain and codomain have the same finite dimension. Substituting \(v=a^{-1}w\) into OI1 gives
\(\|a^{-1}(x,\xi)\|\leq c^{-1}\langle\xi\rangle^{-m}\).
The inverse is smooth on this actual invertibility region, by the original finite determinant/cofactor formula and its nonzero determinant.

The full original symbol estimate for every base/frequency multi-index is

\[
\|\partial_x^\beta\partial_\xi^\alpha a(x,\xi)\|
\leq C_{\alpha\beta}
\langle\xi\rangle^{m-\rho|\alpha|+\delta|\beta|}.
\tag{OI2}
\]

Set \(h=a^{-1}\) on that region. Differentiating the original identity \(ah=I\) by the complete joint product rule gives, for \(|\alpha|+|\beta|>0\),

\[
\partial_x^\beta\partial_\xi^\alpha h
=-h\!
\sum_{\substack{0<(\nu_x,\nu_\xi)\leq(\beta,\alpha)}}
\binom{\beta}{\nu_x}\binom{\alpha}{\nu_\xi}
(\partial_x^{\nu_x}\partial_\xi^{\nu_\xi}a)
(\partial_x^{\beta-\nu_x}
     \partial_\xi^{\alpha-\nu_\xi}h).
\tag{OI3}
\]

There is no permutation of the three ordered matrix factors in any summand. Each final inverse derivative has strictly smaller total order. Induction starts with OI1 and then uses OI2. The exact three powers in each summand multiply to

\[
\begin{split}
&\langle\xi\rangle^{-m}
\langle\xi\rangle^{m-\rho|\nu_\xi|+\delta|\nu_x|}
\langle\xi\rangle^{-m-\rho|\alpha-\nu_\xi|
                              +\delta|\beta-\nu_x|}\\
&\hspace{15mm}
=\langle\xi\rangle^{-m-\rho|\alpha|+\delta|\beta|}.
\end{split}
\tag{OI4}
\]

The equality uses only the componentwise index decompositions in the original sum. If \(H_{\alpha\beta}\) bounds the inverse derivative, the induction supplies the explicit permissible constant

\[
H_{\alpha\beta}
=c^{-1}\!
\sum_{\substack{0<(\nu_x,\nu_\xi)\leq(\beta,\alpha)}}
\binom{\beta}{\nu_x}\binom{\alpha}{\nu_\xi}
C_{\nu_\xi,\nu_x}
H_{\alpha-\nu_\xi,\beta-\nu_x},
\qquad H_{00}=c^{-1}.
\tag{OI5}
\]

Every term is present. An increased constant remains permissible, but no contribution is absorbed into a substitute symbol. This proves the entire original inverse derivative estimate on \(|\xi|\geq R\).

Choose a smooth original frequency cutoff \(\theta(\xi)\), supported in \(|\xi|>R\), and equal to one for \(|\xi|\geq R_1\), with \(R_1>R\). Such a cutoff is supplied by the finite calculus bump construction; retain its actual derivatives. Define \(b_0=\theta h\) on the invertibility region and zero elsewhere. Since \(\theta\) vanishes on a neighborhood of its inner support boundary, the extension is smooth. The full derivative formula is

\[
\partial_x^\beta\partial_\xi^\alpha b_0
=\sum_{\lambda\leq\alpha}\binom{\alpha}{\lambda}
(\partial_\xi^\lambda\theta)
(\partial_x^\beta\partial_\xi^{\alpha-\lambda}h).
\tag{OI6}
\]

The \(\lambda=0\) term has the order proved in OI4. For every \(\lambda\ne0\), the cutoff derivative has support in the compact annulus \(R<|\xi|<R_1\). There all positive and negative powers of the full \(\langle\xi\rangle\) are bounded above and away from zero, with constants determined by both radii and the displayed real exponents; OI3--OI5 remain uniform in every original \(x\). Thus every term of OI6 satisfies the target global \(S^{-m}_{\rho,\delta}\) estimate. In particular
\(ab_0=b_0a=\theta I\), retaining the entire cutoff factor, rather than silently asserting identity at bounded frequency.

Use the original full composition, denoted \(\circ\), whose oscillatory formula is

\[
(a\circ b)(x,\xi)=(2\pi)^{-n}
\iint e^{i(x-y)\cdot(\eta-\xi)}
           a(x,\eta)b(y,\xi)\,dy\,d\eta .
\tag{OI7}
\]

For symbols its value is the distributional/regularized limit proved in E19--E22, rather than an unjustified absolute integral. The exact finite expansion and its full remainder are

\[
a\circ b-\sum_{|\gamma|<N}
\frac{(\partial_\xi^\gamma a)(D_x^\gamma b)}{\gamma!}
\in S^{m_a+m_b-N\kappa}_{\rho,\delta},
\qquad D_x=-i\partial_x .
\tag{OI8}
\]

With \(N=1\), \(m_a=m\), \(m_b=-m\), and the retained bounded-frequency term \(I-\theta I\), this proves both actual defects
\[
r=I-a\circ b_0\in S^{-\kappa}_{\rho,\delta},\qquad
\ell=I-b_0\circ a\in S^{-\kappa}_{\rho,\delta}.
\tag{OI9}
\]
The term \((1-\theta)I\) is smoothing in this global symbol class: its base derivatives of positive order are zero and every frequency derivative is supported in a bounded set. The other defect terms are exactly the composition remainders from OI8.

Retain the ordered finite sums
\[
b_{R,N}=\sum_{j=0}^{N-1}b_0\circ r^{\circ j},
\qquad
b_{L,N}=\sum_{j=0}^{N-1}\ell^{\circ j}\circ b_0.
\tag{OI10}
\]
Their terms have orders \(-m-j\kappa\) by the proved composition bound; the original zeroth powers are \(I\). Associativity and the unit \(I\) are established by Fourier/kernel injectivity in Euclidean Section5. They give the entire exact telescoping identities
\[
a\circ b_{R,N}=I-r^{\circ N},\qquad
b_{L,N}\circ a=I-\ell^{\circ N}.
\tag{OI11}
\]
For example each right summand contributes
\((I-r)\circ r^{\circ j}=r^{\circ j}-r^{\circ(j+1)}\);
summing all \(j\) leaves both stated endpoints. The left computation keeps the reverse matrix order and has the same complete telescoping endpoints.

Since \(\kappa>0\), the support-controlled sum theorem in Euclidean Section2 applies to those actual sequences: it supplies \(b_R,b_L\in S^{-m}_{\rho,\delta}\) with
\(b_R-b_{R,N},b_L-b_{L,N}\in S^{-m-N\kappa}_{\rho,\delta}\).
Every tail is retained as an actual symbol. Composing each such tail with \(a\) and using OI11 yields
\[
a\circ b_R-I\in S^{-N\kappa}_{\rho,\delta},\qquad
b_L\circ a-I\in S^{-N\kappa}_{\rho,\delta}
\quad\hbox{for every }N.
\tag{OI12}
\]
The actual positive \(\kappa\) makes those orders tend to minus infinity, so the two errors are smoothing. The smoothing class is a two-sided ideal, by applying the proved composition estimate with arbitrary negative order for its smoothing factor. The full ordered identity
\[
b_L-b_R
=b_L\circ(I-a\circ b_R)
 +(b_L\circ a-I)\circ b_R
\in S^{-\infty}
\tag{OI13}
\]
then makes either one a two-sided inverse. No convergence of the operator geometric series is assumed.

For completeness retain both one-sided converses from the original theorem. A smoothing right error for an arbitrary \(b\in S^{-m}_{\rho,\delta}\), together with OI8 at \(N=1\), gives \(ab-I\in S^{-\kappa}\). Its original norm is at most \(1/2\) above a uniform frequency radius. The finite matrix geometric series makes \(ab\) invertible there; hence the square \(a\) is invertible and
\(a^{-1}=b(ab)^{-1}\), with norm at most \(2C_b\langle\xi\rangle^{-m}\).
Taking reciprocals of this inverse norm proves OI1 with a corresponding positive constant. A left smoothing error similarly gives \(ba-I\in S^{-\kappa}\), the exact inverse
\(a^{-1}=(ba)^{-1}b\), and the same original lower bound. OI3 proves all inverse derivatives in that region. The ordered pointwise identity
\[
ab-I=a(ba-I)a^{-1}
\tag{OI14}
\]
and the full product derivative rule then give \(ab-I\in S^{-\kappa}\) at large frequency. On the complementary bounded-frequency set the original smooth symbols have the same estimate, including every base derivative.

The construction above already supplies a two-sided inverse \(c\). For a given right inverse \(b\), retain
\[
b-c=c\circ(a\circ b-I)-(c\circ a-I)\circ b .
\tag{OI15}
\]
Both terms are smoothing, so \(b-c\) is smoothing and the other side follows by the ideal property. For a given left inverse the exact companion identity
\[
b-c=(b\circ a-I)\circ c-b\circ(a\circ c-I)
\tag{OI16}
\]
gives the same conclusion. This proves uniqueness modulo the actual smoothing class, preserving the original matrix order in each case. All assertions of E41--E45 are thereby reconstructed from the entire original symbol and its full derivative formulas. At \(\delta=\rho\), the displayed tail orders no longer decrease; this calculation does not claim an inverse at that endpoint.

The preceding edition used the auxiliary expression
\(a_0(x,\xi)=q(\xi)a(x,\xi)\), where the full positive factor is
\(q(\xi)=\langle\xi\rangle^{-m}=(1+|\xi|^2)^{-m/2}\).
The new inverse proof above calculates directly with the entire original \(a(x,\xi)\). Here we retain the exact relation to the preceding expression, including all scalar and differentiated factors.

For every real \(\xi\) and real \(m\), \(q(\xi)>0\) and its full inverse is
\(q(\xi)^{-1}=\langle\xi\rangle^m=(1+|\xi|^2)^{m/2}\).
Thus \(a=q^{-1}a_0\), and \(a_0\) is invertible exactly where \(a\) is. If their original finite matrix rank is \(r\), then
\[
\det a_0=q^r\det a,\qquad
\ker a_0=\ker a,\qquad
a_0^{-1}=a^{-1}q^{-1}.
\tag{OC1}
\]
The determinant equality follows from multilinearity in every one of the \(r\) columns. The kernel equality follows from multiplication by the nonzero scalar. The inverse identity follows by multiplying on both sides, retaining the displayed order. At \(\xi=0\) the factor is one; it introduces no excluded frequency point or additional zero. In rank zero every determinant is one, and the unique empty linear maps satisfy the same relations.

The complete derivatives of the scalar factor can be retained without hiding their contributions. Write \(g(\xi)=1+\sum_j\xi_j^2\) and \(\nu=-m/2\). For a list \(J\) of labeled derivative positions whose coordinate counts are \(\alpha\), the full chain formula is
\[
\partial_\xi^\alpha q
=\sum_{\substack{\pi\text{ a partition of }J\\
                  |B|\leq2\ (B\in\pi)}}
 \left(\prod_{j=0}^{|\pi|-1}(\nu-j)\right)
 g^{\nu-|\pi|}
 \prod_{B\in\pi}\partial_{\xi_B}g,
\quad
\partial_{\xi_j}g=2\xi_j,\quad
\partial_{\xi_j}\partial_{\xi_k}g=2\delta_{jk}.
\tag{OC2}
\]
The empty partition gives the unchanged zeroth derivative. All larger blocks have zero derivative and therefore make zero contributions to the original full chain formula. The finite chain rule proved in the calculus chapter gives this equality by induction: differentiating a factor either adds the new label to one existing block or creates its singleton block, which generates each next labeled partition exactly once.

If a term has \(s\) singleton blocks and \(t\) two-label blocks, then
\(|\alpha|=s+2t\), \(|\pi|=s+t\). Its full \(g\)-power times its singleton coordinate factors has an absolute bound of order
\(\langle\xi\rangle^{-m-2(s+t)+s}
=\langle\xi\rangle^{-m-|\alpha|}\).
The actual falling-factorial product, each factor \(2\), each Kronecker delta and every repeated-coordinate partition remain in OC2; their finite sum supplies its bound constant. The same proof with \(\nu=m/2\) gives all derivatives of the full \(q^{-1}\).
The original product formula for the earlier auxiliary expression is
\[
\partial_x^\beta\partial_\xi^\alpha a_0
=\sum_{\lambda\leq\alpha}\binom{\alpha}{\lambda}
 (\partial_\xi^\lambda q)
 (\partial_x^\beta\partial_\xi^{\alpha-\lambda}a).
\tag{OC3}
\]
Each summand has its complete power
\[
\langle\xi\rangle^{-m-|\lambda|}
\langle\xi\rangle^{m-\rho|\alpha-\lambda|+\delta|\beta|}
=\langle\xi\rangle^{-\rho|\alpha|-(1-\rho)|\lambda|+\delta|\beta|}.
\tag{OC4}
\]
Since \(0<\rho\leq1\), these actual exponents prove the earlier \(S^0_{\rho,\delta}\) statement, with all its derivative terms retained. They are a comparison of the two expressions; OI1--OI16 continue to use the original full symbol.

On the original invertibility region and with the same cutoff \(\theta\), the preceding and current preliminary inverse expressions obey the entire factor identity
\[
b_{\mathrm{preceding}}
=\theta q a_0^{-1}
=\theta q a^{-1}q^{-1}
=\theta a^{-1}=b_0 .
\tag{OC5}
\]
Both expressions are extended by zero across the region where the cutoff vanishes, so this equality holds as a global smooth symbol even at frequencies where \(a\) is singular. No inverse is evaluated at those singular frequencies.

To compare every derivative, put \(h=a^{-1}\) on the invertibility region and use a joint base/frequency multi-index \(\gamma\). The complete four-factor derivative is
\[
\partial^\gamma(\theta q h q^{-1})
=\sum_{\gamma_1+\gamma_2+\gamma_3+\gamma_4=\gamma}
\frac{\gamma!}{\gamma_1!\gamma_2!\gamma_3!\gamma_4!}
(\partial^{\gamma_1}\theta)(\partial^{\gamma_2}q)
(\partial^{\gamma_3}h)(\partial^{\gamma_4}q^{-1}).
\tag{OC6}
\]
All scalar derivatives commute with the actual matrix derivative of \(h\). Group the terms with
\(\lambda=\gamma_2+\gamma_4\). Their inner sum is the entire product derivative
\[
\sum_{\gamma_2+\gamma_4=\lambda}
\frac{\lambda!}{\gamma_2!\gamma_4!}
(\partial^{\gamma_2}q)(\partial^{\gamma_4}q^{-1})
=\partial^\lambda(qq^{-1})
=\begin{cases}1,&\lambda=0,\\0,&|\lambda|>0.\end{cases}
\tag{OC7}
\]
This proves the cancellations of all scalar derivative contributions rather than omitting them. Substitution in OC6 gives exactly OI6's remaining original cutoff and inverse derivative sum. At the zero-extension boundary the symbols are smooth and coincide, so all derivatives coincide there too. Their actual quantizations are equal by the full original Fourier formula, hence their left and right composition defects and finite ordered inverse powers coincide. The new proof supplies each original inverse derivative and every subsequent remainder directly, while this comparison preserves the exact provenance of the preceding expression.

## 10. Hypoelliptic polynomials and the symbol calculus

The origin of more general symbol orders includes reciprocals of hypoelliptic polynomials. The quantitative hypoelliptic polynomial theorem, proved in this section, states: if a nonzero complex polynomial \(P\) defines a hypoelliptic constant-coefficient operator, meaning that \(P(D)u\) smooth implies \(u\) smooth on every open set for every distribution \(u\), then \(P(\xi)\ne0\) for all sufficiently large real \(|\xi|\), and there are constants \(c>0,C,R\) such that
\[
\left|\frac{\partial^\alpha P(\xi)}{P(\xi)}\right|
\leq C|\xi|^{-c|\alpha|}
\quad (\alpha\ne0,\ \xi\in\mathbb R^n,\ |\xi|>R).
\tag{E48}
\]
Only finitely many nonzero derivatives occur, so a common \(C\) is possible. This is the quantitative implication of Hörmander II, Theorem 11.1.3, with hypoellipticity as in Theorem 11.1.1/Definition 11.1.2. We prove every step below, including the finite real polynomial projection theorem, its power-growth consequence, the original complex-zero separation and every reciprocal derivative. The algebraic and spectral proofs are in [Stable prerequisites](stable-prerequisite-bridges.md#full-factorization-leading-coefficient-and-multiplicities) and [Fourier prerequisites](prerequisite-bridges.md#real-spectral-decomposition). The compactness and calculus proofs are in [Metric foundations](metric-foundation-bridges.md#open-cover-compactness-and-the-exact-closed-and-bounded-criterion), the Hilbert and closed-graph proofs in [Banach foundations](banach-foundation-bridges.md#the-closed-graph-and-its-exact-estimate), and the original-circle coefficient formula in [Conormal transmission](conormal-transmission.md#the-circle-formula-every-coefficient-and-both-continuation-principles).

### 10.1. Polynomial sign counts through their original multiplication matrices

Let
\[
F(t)=\sum_{j=0}^{d}a_jt^j,\qquad a_j\in\mathbb R,\quad d\geq1,\quad a_d\ne0.
\tag{HP1}
\]
In \(E_F=\mathbb R[t]/(F)\), polynomial division proves that the classes \(1,t,\ldots,t^{d-1}\) form a basis. Multiplication by the original class of \(t\) has matrix \(C_F\): column \(j<d-1\) is the coordinate vector of \(t^{j+1}\), and its last column has entries \(-a_j/a_d\), \(0\leq j<d\). Indeed
\[
a_dt^d+\sum_{j=0}^{d-1}a_jt^j=0\quad\hbox{in }E_F,
\qquad F(C_F)=0,\qquad F(\lambda)=a_d\det(\lambda I_d-C_F).
\tag{HP2}
\]
For the determinant identity, expand along the last column of \(\lambda I_d-C_F\). Its row-\(j\) cofactor is \(\lambda^j\): the upper shift part contributes \(j\) diagonal factors \(\lambda\), the lower part contributes \(d-1-j\) factors \(-1\), and its cofactor sign is \((-1)^{j+d-1}\), making the total sign positive. The last-column entries are \(a_j/a_d\) for \(j<d-1\) and \(\lambda+a_{d-1}/a_d\) in the last row. Their sum is \(\lambda^d+\sum_{j=0}^{d-1}(a_j/a_d)\lambda^j\). Multiplying by the actual \(a_d\) proves HP2, including \(d=1\). Its leading factor has not been suppressed.

For a real polynomial \(h\), define the symmetric trace matrix
\[
H_{F,h}=\left[\operatorname{Tr}\big(h(C_F)C_F^{j+k}\big)\right]_{0\leq j,k<d}.
\tag{HP3}
\]
It represents the original bilinear form
\[
\mathcal H_{F,h}(u,v)=\operatorname{Tr}_{E_F}(m_{huv}),\qquad
u=\sum_{j=0}^{d-1}u_jt^j,\quad v=\sum_{k=0}^{d-1}v_kt^k,
\tag{HP4}
\]
where \(m_w\) is multiplication by the class of \(w\). Evaluating each basis pair proves HP3. Its entries are rational functions of all the coefficients, with denominators powers of the actual nonzero \(a_d\).

The complex-root theorem and conjugation give the full original factorization
\[
F(t)=a_d
\prod_{\ell=1}^{r}(t-r_\ell)^{m_\ell}
\prod_{\ell=1}^{s}\big((t-b_\ell)^2+c_\ell^2\big)^{n_\ell},
\quad c_\ell>0,\quad
d=\sum_\ell m_\ell+2\sum_\ell n_\ell.
\tag{HP5}
\]
The real roots and the nonreal conjugate pairs are distinct. All multiplicities are retained. Bézout for these coprime powered factors gives the isomorphism from \(E_F\) to the product of their quotient algebras, sending each polynomial to all of its remainder classes. Injectivity follows because divisibility by all coprime factors implies divisibility by their product; multiplication by \(a_d^{-1}\) identifies that ideal with \((F)\). For surjectivity, write \(G_\ell\) for a powered factor and \(B_\ell=\prod_{j\ne\ell}G_j\). Bézout gives \(u_\ell B_\ell+v_\ell G_\ell=1\), so the classes \(e_\ell=u_\ell B_\ell\) are one modulo their own factor and zero modulo the others; their sum is one, and \(\sum_\ell e_\ell w_\ell\) receives any prescribed tuple of remainder classes.

At a real root the remainder map is
\[
[u]\longmapsto\sum_{j=0}^{m_\ell-1}
\frac{u^{(j)}(r_\ell)}{j!}\epsilon^j
\quad\hbox{in }\mathbb R[\epsilon]/(\epsilon^{m_\ell}).
\tag{HP6}
\]
For a nonreal pair \(z_\ell=b_\ell+ic_\ell,\bar z_\ell\), complexifying and using the same Bézout maps gives both Taylor remainders. The conjugation-fixed pairs are \((w(\epsilon),\overline{w(\epsilon)})\). Thus the original real quotient is isomorphic as a real algebra to \(\mathbb C[\epsilon]/(\epsilon^{n_\ell})\), by the Taylor remainder at \(z_\ell\), with all derivatives through \(n_\ell-1\). This proves its real dimension \(2n_\ell\), while preserving both conjugate factors.

Multiplication by \(huv\) is triangular in the real basis \(1,\epsilon,\ldots,\epsilon^{m_\ell-1}\), with every diagonal entry \(h(r_\ell)u(r_\ell)v(r_\ell)\). Its trace is
\[
m_\ell h(r_\ell)u(r_\ell)v(r_\ell).
\tag{HP7}
\]
Its form has the scalar block \(m_\ell h(r_\ell)\) and \(m_\ell-1\) zero directions; if \(h(r_\ell)=0\), the whole block vanishes. On the complex local factor its real trace is \(2n_\ell\operatorname{Re}(h(z_\ell)u(z_\ell)v(z_\ell))\). In constant coordinates \(1,i\) its block is
\[
2n_\ell\begin{pmatrix}
\operatorname{Re}h(z_\ell)&-\operatorname{Im}h(z_\ell)\\
-\operatorname{Im}h(z_\ell)&-\operatorname{Re}h(z_\ell)
\end{pmatrix},
\qquad \det=-(2n_\ell)^2|h(z_\ell)|^2,
\tag{HP8}
\]
with \(2n_\ell-2\) further zero directions. If \(h(z_\ell)\ne0\), its eigenvalues are \(2n_\ell|h(z_\ell)|,-2n_\ell|h(z_\ell)|\); otherwise both vanish.

The product remainder isomorphism has an invertible real coordinate matrix \(S\). The earlier expression \(S^TH_{F,h}S\) used this coefficient-to-remainder map in the wrong direction; the exact corrected map is as follows.

Keep the polynomial \(F\), its actual nonzero leading coefficient \(a_d\), the coefficient basis \(1,t,\ldots,t^{d-1}\), every real-root multiplicity and both members of each complex conjugate pair in HP1--HP8. Let \(\psi\) be the proved real-algebra isomorphism from \(E_F\) to the product of the local remainder algebras. Let \(S\) be its matrix, taking an original coefficient column \(u\) to the local remainder column \(Su\). Invertibility follows from the exact injectivity and surjectivity argument in the preceding CRT and Taylor-remainder arguments HP5--HP6.

Write \(B\) for the direct sum of the full real and complex trace blocks in HP7--HP8, including every zero direction. For multiplication by any original \(w\), the matrices of multiplication before and after \(\psi\) are conjugate: \(\psi m_w\psi^{-1}=m_{\psi(w)}\). The trace is invariant under this conjugation because, for arbitrary square matrices \(X,Y\), direct summation gives \(\operatorname{Tr}(XY)=\sum_{j,k}X_{jk}Y_{kj}=\operatorname{Tr}(YX)\). Since \(\psi\) is an algebra map, the full original trace form consequently satisfies

\[
 u^T H_{F,h}v=(Su)^T B(Sv)=u^T S^TBSv
 \quad\hbox{for every }u,v\in\mathbb R^d.
 \tag{EC1}
\]

Taking every pair of coordinate vectors proves the exact matrix equalities

\[
 H_{F,h}=S^TBS,\qquad
 B=S^{-T}H_{F,h}S^{-1}.
 \tag{EC2}
\]

Thus \(S\) itself is the coefficient-to-remainder map, while the map from local remainder coordinates to coefficient coordinates is \(S^{-1}\). The earlier \(S^TH_{F,h}S\) applied that map in the wrong direction.

The inertia conclusion survives with the correct morphism. A subspace \(U\) of original coefficient columns is positive for \(H\) if and only if \(SU\) is positive for \(B\), by EC1; \(S\) preserves dimension and has an inverse. Thus the maximum dimensions of positive subspaces agree. The same proof applies to negative subspaces. Also \(Hu=0\) if and only if \(B(Su)=0\) by EC2, so \(S\) identifies the nullspaces. This proves preservation of positive, negative and zero counts, with no omission of nilpotent directions. Combining the original HP7--HP8 blocks therefore gives precisely the original HP9 signature formula, including roots at which \(h\) vanishes.

For the exact counterexample \(F=(t-2)(t-3)\), \(h=1\), all original coefficients are \(a_2=1,a_1=-5,a_0=6\). The coefficient-basis companion matrix and the remainder map are

\[
 C_F=\begin{pmatrix}0&-6\\1&5\end{pmatrix},\qquad
 H_{F,1}=\begin{pmatrix}2&5\\5&13\end{pmatrix},\qquad
 S=\begin{pmatrix}1&2\\1&3\end{pmatrix},\qquad
 S^{-1}=\begin{pmatrix}3&-2\\-1&1\end{pmatrix}.
 \tag{EC3}
\]

Here \(\operatorname{Tr}(I)=2\), \(\operatorname{Tr}(C_F)=5\), and \(C_F^2\) has diagonal \(-6,19\), whose sum is13. The two simple real blocks are \(B=I_2\). Direct multiplication gives

\[
 S^T B S=H_{F,1},\qquad
 S^{-T}H_{F,1}S^{-1}=I_2,\qquad
 S^TH_{F,1}S=\begin{pmatrix}25&68\\68&185\end{pmatrix}.
 \tag{EC4}
\]

The last equality records the original erroneous congruence's actual value, rather than silently interpreting \(S\) as its inverse.

 Congruence preserves positive and negative counts: the spectral proof identifies the positive count with the largest dimension of a subspace on which the original quadratic form is positive definite. A larger subspace would meet the nonpositive eigenspaces nontrivially by the dimension formula. An invertible map preserves that maximum; apply the same argument to the negative form. Hence
\[
\operatorname{sig}H_{F,h}
=\sum_{\ell=1}^{r}\operatorname{sign}h(r_\ell).
\tag{HP9}
\]
Each distinct real root contributes once; all original multiplicities, complex blocks and null directions remain in the calculation.

The signature can be computed using only rational coefficient operations and sign tests. Permute any nonzero diagonal entry \(a\) first. For \(H=\left(\begin{smallmatrix}a&v^T\\v&W\end{smallmatrix}\right)\), multiplication gives
\[
\begin{pmatrix}1&0\\-v/a&I\end{pmatrix}
H\begin{pmatrix}1&-v^T/a\\0&I\end{pmatrix}
=\begin{pmatrix}a&0\\0&W-vv^T/a\end{pmatrix}.
\tag{HP10}
\]
Its signature is \(\operatorname{sign}a+\operatorname{sig}(W-vv^T/a)\). If all diagonal entries vanish but an off-diagonal \(b\ne0\) exists, permute that pair first, with
\[
A=\begin{pmatrix}0&b\\b&0\end{pmatrix},
\qquad A^{-1}=\begin{pmatrix}0&1/b\\1/b&0\end{pmatrix}.
\tag{HP11}
\]
For \(H=\left(\begin{smallmatrix}A&V\\V^T&W\end{smallmatrix}\right)\), the invertible block change \(\left(\begin{smallmatrix}I&-A^{-1}V\\0&I\end{smallmatrix}\right)\) gives \(\operatorname{diag}(A,W-V^TA^{-1}V)\). The block \(A\) has eigenvalues \(b,-b\), so signature zero. An all-zero matrix has signature zero. Each step decreases dimension by one or two and covers empty matrices. Every branch tests a rational coefficient \(p/q\), \(q\ne0\): equality means \(p=0\), and positivity means \(pq>0\), since \((p/q)q^2=pq\) with its positive factor \(q^2\). Thus each possible signature has a finite Boolean description by polynomial signs in the original coefficients.

For a finite family of real polynomials \(q_1,\ldots,q_k\), define
\[
T_e=\operatorname{sig}H_{F,\prod_{j=1}^{k}q_j^{e_j}},
\quad e\in\{0,1,2\}^k,\qquad
N_\sigma=\#\{r:F(r)=0,\ (\operatorname{sign}q_j(r))_j=\sigma\},
\quad \sigma\in\{-1,0,1\}^k.
\tag{HP12}
\]
Roots in the count are distinct, and \(0^0=1\). HP9 gives
\[
T_e=\sum_{\sigma\in\{-1,0,1\}^k}
\left(\prod_{j=1}^{k}\sigma_j^{e_j}\right)N_\sigma.
\tag{HP13}
\]
In the order \(e=0,1,2\), \(\sigma=-1,0,1\), the one-coordinate matrix is
\[
V=\begin{pmatrix}1&1&1\\-1&0&1\\1&0&1\end{pmatrix},
\quad W=V^{-1}=
\begin{pmatrix}0&-1/2&1/2\\1&0&-1\\0&1/2&1/2\end{pmatrix},
\qquad \det V=2.
\tag{HP14}
\]
Direct multiplication proves both inverse identities. Successive multiplication in each coordinate yields
\[
N_\sigma=\sum_{e\in\{0,1,2\}^k}
\left(\prod_{j=1}^{k}W_{\sigma_j,e_j}\right)T_e.
\tag{HP15}
\]
Each of the \(3^k\) signatures lies in the finite integer interval \([-d,d]\); enumerating its possibilities proves that \(N_\sigma>0\) is a finite Boolean polynomial condition on all coefficients. For \(k=0\), the empty product is one and its single query counts the distinct real roots. A nonzero constant \(F\) has no roots and all counts zero.

### 10.2. Eliminating real polynomial quantifiers with all degree branches

A semialgebraic set is one described by a finite Boolean combination of real polynomial equalities and inequalities. Take such a formula \(\Phi(x,t)\) expressed by the signs of its full original family \(f_1(x,t),\ldots,f_k(x,t)\). Partition parameter space into finite degree branches: an identically zero input has all its \(t\)-coefficients zero; degree \(j\) has all higher coefficients zero and its coefficient of \(t^j\) nonzero. These are polynomial conditions in the retained coordinates \(x\). Each zero input still contributes its zero sign to \(\Phi\). On a branch form
\[
F_x(t)=\prod_{\{j:f_j(x,\cdot)\ne0\}}f_j(x,t).
\tag{HP16}
\]
Nonzero constant factors are included and an empty product is one. All original inputs and signs remain in \(\Phi\); this auxiliary product only locates their roots.

At roots of \(F_x\) and its nonzero derivative \(F_x'\), HP12--HP15 test every possible original input sign pattern. A zero or constant derivative has no root candidates. The multiplication matrices have their actual branch degrees and leading coefficients. Their rational entries and finite signature branches give semialgebraic conditions for every tested pattern.

Between consecutive distinct real roots of \(F_x\), each nonzero \(f_j\) has constant nonzero sign by continuity and the intermediate value theorem. Rolle's theorem supplies a root of \(F_x'\) strictly inside every such bounded interval, so that pattern is tested. The unbounded intervals are tested by the leading coefficients:
\[
\operatorname{sign}f_j(x,t)=\operatorname{sign}a_j(x)
\quad(t\hbox{ sufficiently large positive}),\qquad
\operatorname{sign}f_j(x,t)=(-1)^{d_j}\operatorname{sign}a_j(x)
\quad(t\hbox{ sufficiently large negative}),
\tag{HP17}
\]
where \(d_j\) is the actual degree and \(a_j(x)\ne0\) its leading coefficient. Divide the entire finite polynomial by its leading power and choose the threshold so the sum of the absolute values of all lower terms is smaller than \(|a_j(x)|\). All finitely many thresholds can be met together, and zero inputs still have sign zero. With no real roots, these tail patterns also test the whole line; with a constant product, they are the only candidates.

Consequently \(\exists t\,\Phi(x,t)\) is equivalent, on every degree branch, to the finite disjunction of its acceptable patterns at roots of \(F_x,F_x'\) and its two tails. This proves the projection theorem by finite coefficient conditions, with every degree drop and repeated root covered. Starting from an innermost quantified variable and repeating eliminates any finite number of quantifiers. Universal quantifiers are eliminated through \(\forall t\,\Phi=\neg\exists t\,\neg\Phi\). Every resulting formula is still a finite Boolean polynomial formula.

### 10.3. The actual power bound for an unbounded semialgebraic function

Suppose \(g:(R_0,\infty)\to(0,\infty)\) has semialgebraic graph and \(g(r)\to\infty\). Choose a Boolean polynomial formula for its graph, retaining the fixed truth values of identically zero inputs. Let \(Q_1,\ldots,Q_N\) be its nonzero polynomial inputs, including nonzero constants. At each \((r,g(r))\), some \(Q_j\) vanishes: otherwise all signs would stay fixed in a small open rectangle, forcing the whole rectangle into the graph, whereas a graph has only one ordinate for a fixed abscissa. Thus
\[
Q(r,g(r))=0,\qquad Q(r,s)=\prod_{j=1}^{N}Q_j(r,s)\ne0.
\tag{HP18}
\]
The nonzero product follows by successively multiplying leading coefficients in the polynomial ring in each variable. All factors are retained; this product is not substituted for the original graph formula.

Write its complete coefficient expansion
\[
Q(r,s)=\sum_{i=0}^{I}r^ia_i(s),\qquad
a_I(s)=\sum_{\ell=0}^{J}b_{I\ell}s^\ell,\quad b_{IJ}\ne0.
\tag{HP19}
\]
Choose \(S\geq1\) with \(\sum_{\ell<J}|b_{I\ell}|S^{\ell-J}\leq |b_{IJ}|/2\); then \(|a_I(s)|\geq |b_{IJ}|s^J/2\) for \(s\geq S\). For nonzero \(a_i\), \(i<I\), let \(J_i=\deg a_i\) and \(B_i\) be the absolute sum of all its coefficients. A zero \(a_i\) contributes \(B_i=0\). Put
\[
L=\max\big(\{0\}\cup\{J_i-J:i<I,\ a_i\ne0\}\big),
\quad \epsilon=\frac1{2(L+1)},\quad B=\sum_{i<I}B_i.
\tag{HP20}
\]
For \(r\geq1\), \(S\leq s\leq r^\epsilon\), every lower contribution is bounded by
\[
\left|\sum_{i<I}r^ia_i(s)\right|
\leq B r^{I-1}s^{J+L}
\leq B r^{I-1+\epsilon L}s^J,\qquad
|r^Ia_I(s)|\geq \frac{|b_{IJ}|}{2}r^Is^J.
\tag{HP21}
\]
For \(I\geq1\), choose \(R\geq1\) so that \((2B/|b_{IJ}|)r^{-1+\epsilon L}<1\) for \(r>R\). Since \(\epsilon L<1/2\), such an \(R\) exists. The leading term then strictly exceeds the whole lower sum, forbidding \(Q(r,s)=0\) in that strip. For \(I=0\), the lower sum is empty and the same nonvanishing is immediate. Since \(g(r)\geq S\) eventually, HP18 proves
\[
g(r)>r^\epsilon\quad\hbox{for all sufficiently large }r.
\tag{HP22}
\]
The \(I=0\) case would contradict HP18 and \(g(r)\to\infty\), so it cannot occur for this graph. The algebraic growth assertion has now been proved.

### 10.4. Local regularity forces the original complex zero set away

Let
\[
P(\zeta)=\sum_{|\alpha|\leq m}p_\alpha\zeta^\alpha,\quad
p_\alpha\in\mathbb C,\quad P\ne0,\qquad
P(D)=\sum_{|\alpha|\leq m}p_\alpha(-i)^{|\alpha|}\partial^\alpha
\tag{HP23}
\]
be the original constant-coefficient operator. Suppose it is hypoelliptic: on every open \(U\subset\mathbb R^n\), for every distribution \(u\), smoothness of \(P(D)u\) implies smoothness of \(u\). For a nonzero constant polynomial all nonzero-order derivatives vanish and the reciprocal is constant. The zero-dimensional coordinate space also has only constant polynomials. Hence assume \(n\geq1\) and actual degree \(m\geq1\).

The original zero set \(Z=\{\zeta\in\mathbb C^n:P(\zeta)=0\}\) is closed and nonempty. Its highest-degree homogeneous part is nonzero at some real \(v\): a polynomial cannot vanish on all of \(\mathbb R^n\), by induction in the number of variables, regarding it as a polynomial in the last variable and using that a nonzero one-variable polynomial has at most its degree many roots. The original \(P(tv)\) therefore has degree \(m\) and a complex root by the proved root theorem. Fix one original zero \(\zeta_0\).

On the original unit ball \(U=\{x:|x|<1\}\) with Lebesgue measure, put
\[
\mathcal E=\{u\in L^2(U):P(D)u=0\hbox{ as a distribution on }U\}.
\tag{HP24}
\]
This is a closed Hilbert subspace. If \(u_k\to u\) in \(L^2(U)\), Cauchy--Schwarz proves convergence against each test function and every derivative appearing in HP23, so all the distributional equations pass to the limit. Hypoellipticity makes every member smooth. The inclusion \(\mathcal E\to C^\infty(U)\) has closed graph: simultaneous convergence in \(L^2(U)\) and in all compact derivative seminorms has the same distributional limit. Hence the two functions coincide almost everywhere, with the smooth representative unique. The complete Fréchet structure of \(C^\infty(U)\) is proved in the foundations. Their closed-graph theorem supplies one constant \(A>0\) such that
\[
\max_{1\leq j\leq n}|\partial_j u(0)|
\leq A\|u\|_{L^2(U)}\qquad(u\in\mathcal E).
\tag{HP25}
\]
Indeed that maximum is one continuous target seminorm; finitely many input seminorms of the Hilbert domain are all bounded by a constant times its one original norm.

For \(\zeta=a+ib\in Z\), the actual \(u_\zeta(x)=e^{i\langle x,\zeta\rangle}\) lies in \(\mathcal E\), since \(D^\alpha u_\zeta=\zeta^\alpha u_\zeta\) and HP23 gives \(P(D)u_\zeta=P(\zeta)u_\zeta=0\). Its derivative at zero is \(i\zeta_j\), and
\[
\|u_\zeta\|_{L^2(U)}^2
=\int_U e^{-2\langle x,b\rangle}\,dx
\leq |U|e^{2|b|},
\qquad
|\zeta|\leq\sqrt n\,A|U|^{1/2}e^{|b|}.
\tag{HP26}
\]
The original sign, volume factor and every coordinate of \(\zeta\) have been kept. Zeros with bounded imaginary part consequently have bounded full norm.

For real \(\xi\), retain its exact distance
\[
\delta(\xi)=\inf_{\zeta\in Z}|\xi-\zeta|
=\inf_{\zeta=a+ib\in Z}
\left(\sum_{j=1}^{n}(\xi_j-a_j)^2+\sum_{j=1}^{n}b_j^2\right)^{1/2}.
\tag{HP27}
\]
The infimum is attained: using the competitor \(\zeta_0\), a minimizing sequence can be restricted to a fixed closed bounded ball, and \(Z\) is closed. Moreover \(\delta(\xi)\to\infty\) as \(|\xi|\to\infty\). Otherwise some \(\xi_k\) tending to infinity and \(\zeta_k\in Z\) would have \(|\xi_k-\zeta_k|\leq M\) for a fixed \(M\). Then \(|\operatorname{Im}\zeta_k|\leq M\) but \(|\zeta_k|\geq|\xi_k|-M\to\infty\), contradicting HP26. This is a uniform statement outside large real balls.

Now define the actual minimum
\[
g(r)=\min_{\substack{|\xi|=r,\ \xi\in\mathbb R^n\\
                    \zeta=a+ib\in Z}}
\left(\sum_{j=1}^{n}(\xi_j-a_j)^2+\sum_{j=1}^{n}b_j^2\right),
\qquad r>0.
\tag{HP28}
\]
The sphere is nonempty and compact. The competitor \(\zeta_0\) bounds this cost by \((r+|\zeta_0|)^2\). Restricting to costs no larger than that also bounds \(|\zeta|\leq r+(r+|\zeta_0|)\), so a closed bounded feasible set attains the minimum. HP27 implies \(g(r)\to\infty\).

The graph of \(g\) is semialgebraic by the projection theorem just proved. Its exact formula says there exist \(\xi,a,b\) such that
\[
\sum_j\xi_j^2=r^2,\quad
\operatorname{Re}P(a+ib)=0,\quad
\operatorname{Im}P(a+ib)=0,\quad
s=\sum_j(\xi_j-a_j)^2+\sum_jb_j^2,
\tag{HP29}
\]
and for all \(\xi',a',b'\) satisfying the same sphere and both zero equations, the full corresponding squared cost is at least \(s\). The real and imaginary equations are real polynomials obtained by expanding all of HP23, with every coefficient retained. Quantifier elimination applies to this precise formula. Since \(g(r)>0\) eventually, HP22 gives \(\epsilon>0,R\geq1\) such that
\[
\delta(\xi)^2\geq g(|\xi|)>|\xi|^\epsilon\qquad(|\xi|>R).
\tag{HP30}
\]
In particular \(P(\xi)\ne0\) there; the separation is at least \(|\xi|^{\epsilon/2}\).

### 10.5. Every derivative of the original polynomial

Fix such a real \(\xi\), and write \(\delta=\delta(\xi)>0\). For a complex unit vector \(\eta\), retain the whole restriction \(P(\xi+t\eta)\). If its actual degree \(d_\eta\geq1\), its original factorization is
\[
P(\xi+t\eta)=a_\eta\prod_{\ell=1}^{d_\eta}(t-t_\ell),
\quad
P(\xi)=a_\eta\prod_{\ell=1}^{d_\eta}(-t_\ell),
\quad
|t_\ell|\geq\delta,\quad d_\eta\leq m.
\tag{HP31}
\]
Indeed \(\xi+t_\ell\eta\in Z\) and \(|t_\ell\eta|=|t_\ell|\). Here \(a_\eta\) is the actual leading coefficient of the restriction. Comparing both full products, with that coefficient present, yields
\[
|P(\xi+t\eta)|
\leq |P(\xi)|\prod_{\ell=1}^{d_\eta}
\left(1+\frac{|t|}{|t_\ell|}\right)
\leq |P(\xi)|(1+|t|/\delta)^m.
\tag{HP32}
\]
If the restriction is constant, it equals \(P(\xi)\) and the same bound holds with its empty product. For \(w\ne0\), take \(t=|w|,\eta=w/|w|\); the value \(w=0\) is immediate. On the full polydisc \(|w_j|\leq\delta/(2\sqrt n)\), this gives \(|w|\leq\delta/2\) and \(|P(\xi+w)|\leq(3/2)^m|P(\xi)|\).

Apply the positively oriented Cauchy coefficient formula successively on the \(n\) original coordinate circles of radius \(r_\xi=\delta/(2\sqrt n)\). The polynomial is entire and continuous on their compact product, so finite-circle Fubini justifies the iterated integration. The full formula is
\[
\partial^\alpha P(\xi)=
\frac{\alpha!}{(2\pi i)^n}
\int_{|w_1|=r_\xi}\cdots\int_{|w_n|=r_\xi}
\frac{P(\xi+w)}{\prod_{j=1}^{n}w_j^{\alpha_j+1}}\,
dw_n\cdots dw_1,
\qquad
\left|\frac{\partial^\alpha P(\xi)}{P(\xi)}\right|
\leq\alpha!(3/2)^m(2\sqrt n)^{|\alpha|}\delta^{-|\alpha|}.
\tag{HP33}
\]
The \(n\) circle lengths \((2\pi r_\xi)^n\) cancel the displayed \((2\pi)^n r_\xi^n\) denominator exactly. Set \(c=\epsilon/2>0\), and choose the finite common constant
\[
C=\max\left(\{1\}\cup
\{\alpha!(3/2)^m(2\sqrt n)^{|\alpha|}:1\leq|\alpha|\leq m\}\right).
\tag{HP34}
\]
HP30 and HP33 prove
\[
\left|\frac{\partial^\alpha P(\xi)}{P(\xi)}\right|
\leq C|\xi|^{-c|\alpha|}
\qquad(\alpha\ne0,\ |\xi|>R).
\tag{HP35}
\]
Derivatives with \(|\alpha|>m\) are exactly zero and are included. This is the quantitative hypoelliptic polynomial implication for the original operator and its original local regularity definition.

### 10.6. The reciprocal, its full ordered derivatives and its cutoffs

Choose \(p_{\alpha_*}\ne0\) with \(|\alpha_*|=m\). Then \(\partial^{\alpha_*}P=\alpha_*!p_{\alpha_*}\), so
\[
|P(\xi)|^{-1}\leq D_0|\xi|^{-cm},\qquad
D_0=C/|\alpha_*!p_{\alpha_*}|\quad(|\xi|>R).
\tag{HP36}
\]
The selected original coefficient supplies only this bound; every coefficient remains in \(P\).

For every multiindex \(\alpha\), the full derivative identity is
\[
\partial^\alpha(P^{-1})=
\sum_{k=0}^{|\alpha|}(-1)^kP^{-k-1}
\!\!\sum_{\substack{\alpha_1+\cdots+\alpha_k=\alpha\\|\alpha_j|\geq1}}
\frac{\alpha!}{\alpha_1!\cdots\alpha_k!}
\prod_{j=1}^{k}\partial^{\alpha_j}P.
\tag{HP37}
\]
For \(k=0\), the inner sum has one empty tuple if \(\alpha=0\), with coefficient and product one, and is zero otherwise. To prove the identity at a nonzero point \(P(\xi)\), expand the entire finite Taylor polynomial of \(P(\xi+w)-P(\xi)\). Modulo monomials of degree greater than \(|\alpha|\), multiply
\[
\sum_{k=0}^{|\alpha|}(-1)^kP(\xi)^{-k-1}
\big(P(\xi+w)-P(\xi)\big)^k
\tag{HP38}
\]
by the full \(P(\xi+w)\). The product is
\(1+(-1)^{|\alpha|}P(\xi)^{-|\alpha|-1}
(P(\xi+w)-P(\xi))^{|\alpha|+1}\);
its last term has no coefficient of degree at most \(|\alpha|\). The coefficients in HP38 are therefore the reciprocal Taylor coefficients, by recursive comparison in the identity \(P\cdot P^{-1}=1\). The coefficient of \(w^\alpha\), multiplied by \(\alpha!\), gives exactly HP37, including every ordered tuple and sign.

Apply HP35 to each derivative factor, and HP36 to the remaining \(P^{-1}\). Then
\[
|\partial^\alpha(P^{-1})(\xi)|
\leq D_\alpha|\xi|^{-cm-c|\alpha|},\qquad
D_\alpha=D_0\sum_{k=0}^{|\alpha|}C^k
\!\!\sum_{\substack{\alpha_1+\cdots+\alpha_k=\alpha\\|\alpha_j|\geq1}}
\frac{\alpha!}{\alpha_1!\cdots\alpha_k!}.
\tag{HP39}
\]
The empty tuple convention remains and zero higher derivatives remain zero in the exact identity. Put \(\rho=\min(c,1)>0\). For \(|\xi|\geq1\), the full comparison \(\langle\xi\rangle/|\xi|\leq\sqrt2\) gives
\[
|\partial^\alpha(P^{-1})(\xi)|
\leq 2^{\rho(m+|\alpha|)/2}D_\alpha
\langle\xi\rangle^{-\rho m-\rho|\alpha|}
\qquad(|\xi|>R).
\tag{HP40}
\]
Only the estimate uses \(\rho\); the original polynomial and its \(c\)-estimates have not been replaced.

Choose \(R_2>R_1>R\) and an actual smooth cutoff \(\theta\) zero for \(|\xi|\leq R_1\) and one for \(|\xi|\geq R_2\). Define \(a=\theta/P\) on the nonzero domain outside the inner ball, and define it as zero on a neighborhood of that ball. The definitions agree smoothly because the cutoff vanishes there. Every derivative is
\[
\partial^\alpha a=
\sum_{\beta\leq\alpha}\binom{\alpha}{\beta}
(\partial^\beta\theta)\,\partial^{\alpha-\beta}(P^{-1}).
\tag{HP41}
\]
The term \(\beta=0\) has HP40's frequency bound. Every positive-order cutoff derivative is supported in the compact nonzero annulus, where every reciprocal derivative and weight is continuous and bounded. On the inner zero region all derivatives are zero. Thus \(a\in S^{-\rho m}_{\rho,0}\), with every cutoff contribution retained. It is independent of \(x\), so its positive-order \(x\)-derivatives vanish exactly. A nonzero constant \(P\) has its constant reciprocal in \(S^0_{\rho,0}\) for any allowed \(\rho\). No reciprocal is asserted across real zeros of a nonconstant \(P\).

The finite sign-count inversion is the classical Tarski-query mechanism. Cohen and Mahboubi, *Formal proofs in real algebraic geometry: from ordered fields to quantifier elimination*, [arXiv:1201.3731v2](https://arxiv.org/abs/1201.3731v2), original part5.tex, lines 226--328, gives the query/count relation in its own row order. Original part6.tex, lines 1--158 and 379--459, describes its formal quantifier-elimination setting. The present proof supplies the full trace-form calculation, projection argument and analytic receiving estimates; no omitted formal proof is imported.

Their row vectors are \(n=(N_+,N_-,N_0)\), \(t=(T_1,T_2,T_0)\), with \(t=nS\) and
\[
S=\begin{pmatrix}1&1&1\\-1&1&1\\0&0&1\end{pmatrix},
\quad R=\begin{pmatrix}0&1&0\\0&0&1\\1&0&0\end{pmatrix},
\quad L=\begin{pmatrix}0&0&1\\1&0&0\\0&1&0\end{pmatrix}.
\tag{HP42}
\]
Our column vectors are \(N=Rn^T\), \(T=Lt^T\), and direct multiplication gives \(V=LS^TR^T\), with \(\det S=\det V=2\). This retains the source's factor two and exact ordering maps. Their article supplies historical context for the query mechanism; the complete trace, projection, growth and operator argument has been proved above.

Here is the resulting adapter to the present calculus. If \(P\) has degree \(d>0\), replace \(c\) by \(\rho=\min(c,1)>0\). A derivative of total degree \(d\) is a nonzero constant for some multiindex, so (E48) yields \(|P(\xi)|^{-1}\leq C|\xi|^{-d\rho}\). Repeated differentiation of \(P^{-1}P=1\) expresses each derivative of \(P^{-1}\) as a finite sum of
\[
P^{-1}\prod_{\nu=1}^k
\frac{\partial^{\alpha_\nu}P}{P},
\qquad \alpha_\nu\ne0,\qquad
\alpha_1+\cdots+\alpha_k=\alpha,
\tag{E49}
\]
with numerical coefficients. Induction follows by differentiating one factor at a time, using the quotient rule; total derivative degree increases by one in each resulting term. Equation (E48) bounds (E49) by \(C_\alpha\langle\xi\rangle^{-d\rho-\rho|\alpha|}\). A smooth cutoff \(\theta\) that is zero on a sufficiently large ball and one outside a larger ball therefore gives
\(\theta(\xi)/P(\xi)\in S^{-d\rho}_{\rho,0}\), independent of \(x\).
Cutoff derivatives occur only in a compact region where \(P\ne0\) and do not change the conclusion. A nonzero constant polynomial has its constant reciprocal in \(S^0_{\rho,0}\) for any allowed \(\rho\). No reciprocal is asserted across real zeros of a nonconstant polynomial. The quantitative hypoelliptic implication and the full reciprocal adapter are now proved.

**Editorial completion: the exact converse for the original polynomial.**
Retain the nonzero polynomial \(P\), all its complex coefficients, \(D=-i\partial\), and the original complex zero set
\(Z=\{\zeta\in\mathbb C^n:P(\zeta)=0\}\). For \(n\ge1\) and \(m=\deg P\ge1\), the following three statements are equivalent:
\[
\begin{array}{ll}
\text{(i)}&P(D)u\in C^\infty(U)\Longrightarrow u\in C^\infty(U)
       \text{ for every open }U\text{ and }u\in\mathcal D'(U);\\
\text{(ii)}&\delta(\xi)=\inf_{\zeta\in Z}|\xi-\zeta|\longrightarrow\infty
       \text{ as real }|\xi|\longrightarrow\infty;\\
\text{(iii)}&\text{There are }R,C,c>0\text{ such that, for }|\xi|>R,\ P(\xi)\ne0\text{ and}\\
&|\partial^\alpha P(\xi)|\le C|P(\xi)|\,|\xi|^{-c|\alpha|}
       \quad\text{for every nonzero multiindex }\alpha.
\end{array}
\tag{HC1}
\]
Derivatives above the full original degree are zero, and remain part of (iii). Statement (i) implies (ii) by HP23--HP27: the complete closed-graph estimate on the original unit-ball solution space bounds every zero's real part by its imaginary part through the actual exponential \(e^{i\langle x,\zeta\rangle}\) and the original ball volume. The attained distance argument there gives (ii). No reciprocal has been evaluated at a real zero.

The proof HP28--HP35 needs only (ii) after that point. Specifically, retain its exact minimum of the squared distance on the sphere of real radius \(r\), all real and imaginary coordinates of \(\zeta\), and its full quantifier formula. Statement (ii) makes that minimum tend to infinity. The proved projection and graph-growth argument HP16--HP22 supplies a positive power lower bound. The full restriction \(P(\xi+t\eta)\), its leading coefficient and every root give HP31--HP32, and its original polydisc estimate gives HP33--HP35. Thus (ii) implies (iii) with the original constants and derivative factors, without requiring (i) as an extra hypothesis.

In this polynomial application, the circle step can also be checked without importing a general analytic theorem. Retain the finite expansion
\(P(\xi+w)=\sum_{|\beta|\le m}\partial^\beta P(\xi)w^\beta/\beta!\).
On each positively oriented circle \(w_j=re^{it_j}\), its original derivative is \(dw_j=ire^{it_j}dt_j\); direct integration gives
\(\int_{|w_j|=r}w_j^{\beta_j-\alpha_j-1}dw_j=2\pi i\) if \(\beta_j=\alpha_j\), and zero otherwise, including negative nonzero exponent differences. Integrating the finite expansion in the original coordinate order therefore proves
\[
\partial^\alpha P(\xi)=\frac{\alpha!}{(2\pi i)^n}
 \int_{|w_1|=r}\cdots\int_{|w_n|=r}
 \frac{P(\xi+w)}{w_1^{\alpha_1+1}\cdots w_n^{\alpha_n+1}}
 \,dw_n\cdots dw_1.
\tag{HC2}
\]
For \(|\alpha|>m\), no matching monomial occurs and both sides are zero. At the original radius \(r=\delta(\xi)/(2\sqrt n)\), HP32 bounds the numerator by \((3/2)^m|P(\xi)|\). The full circle lengths \((2\pi r)^n\), denominator \(r^{|\alpha|+n}\), and prefactor \(\alpha!/(2\pi)^n\) give exactly \(\alpha!(3/2)^m(2\sqrt n)^{|\alpha|}|P(\xi)|\delta(\xi)^{-|\alpha|}\). There are finitely many nonzero original derivatives through degree \(m\), so one maximum of these explicit constants gives the common \(C\) in (iii). The earlier general circle proof remains a separate valid analytic result.

We prove (iii) implies (i), including the actual local distribution map. HP36--HP41 is the full reciprocal calculation for precisely (iii). A nonzero derivative of degree \(m\) supplies HP36's lower growth bound for \(|P|\); HP37 retains every ordered reciprocal tuple, sign and factorial. With \(\rho=\min(c,1)\), it proves that the actual cutoff reciprocal of HP41 belongs to \(S^{-\rho m}_{\rho,0}\). Denote that same symbol by \(q(\xi)=\theta(\xi)/P(\xi)\) on its original nonzero domain and by zero on the inner neighborhood, and put \(r(\xi)=1-\theta(\xi)\). The actual cutoff has \(R_2>R_1>R\), is zero for \(|\xi|\le R_1\), and is one for \(|\xi|\ge R_2\). Consequently \(r\in C_c^\infty\), and on the whole frequency space, including the original real zeros,
\[
Pq=qP=\theta,\qquad
P(D)q(D)=q(D)P(D)=\theta(D),\qquad
I=q(D)P(D)+r(D).
\tag{HC3}
\]
These are actual Fourier multiplier identities on \(\mathcal S\) and \(\mathcal S'\), using the unchanged inverse factor \((2\pi)^{-n}\). Polynomial multiplication, the smooth multiplier with polynomially bounded derivatives, and their transpose actions are all defined on these domains. Equality of their full multiplier products proves both orders in (HC3).

Let \(K_q=\mathcal F^{-1}q\) and \(K_r=\mathcal F^{-1}r\), as tempered distributions with that factor. The first kernel is smooth off zero. Here is the complete estimate. For an arbitrary multiindex \(\beta\), choose an integer \(M\ge0\) with
\(2M\rho>n-\rho m+|\beta|\). The distributional Fourier differentiation identities give, for \(z\ne0\),
\[
\partial_z^\beta K_q(z)=(2\pi)^{-n}|z|^{-2M}
 \int e^{i\langle z,\xi\rangle}(-\Delta_\xi)^M[(i\xi)^\beta q(\xi)]\,d\xi.
\tag{HC4}
\]
Indeed multiplication by \(|z|^{2M}\) is inverse Fourier transformation of \((-\Delta_\xi)^M\), and the amplitude on the right is integrable by the following full expansion:
\[
\begin{aligned}
(-\Delta_\xi)^M[(i\xi)^\beta q]
={}&(-1)^Mi^{|\beta|}
 \sum_{|\gamma|=M}\frac{M!}{\gamma!}
 \sum_{\substack{\nu\le2\gamma\\\nu\le\beta}}
 \binom{2\gamma}{\nu}\frac{\beta!}{(\beta-\nu)!}
 \xi^{\beta-\nu}\partial^{2\gamma-\nu}q.
\end{aligned}
\tag{HC5}
\]
Every displayed term has large-frequency bound with power
\(|\beta|-\rho m-2M\rho-(1-\rho)|\nu|\le|\beta|-\rho m-2M\rho<-n\).
The bounded frequency region is smooth and finite. The full original coefficients, all zeros of higher polynomial derivatives, and all compact cutoff terms have therefore been retained. This proves absolute integrability and continuity of the right side of (HC4) on the punctured space. The distributional identity identifies it with the corresponding distributional derivative there, so it does not assume vanishing of an unproved cutoff boundary term.

For clarity, continuous distributional derivatives of every order imply classical smoothness here. On any smaller ball whose closure avoids zero, convolve locally with a compact mollifier of integral one. Each continuous derivative converges uniformly on yet smaller compact sets to its displayed derivative. For a coordinate segment in such a set, the fundamental theorem of calculus for the convolutions, followed by uniform convergence of the function and its first derivative, gives the same theorem for the limiting function. It is therefore differentiable with that derivative. Apply the argument to every derivative in turn. This proves the asserted smoothness with all derivatives in (HC4). The kernel \(K_r\) is smooth everywhere by the absolutely convergent integrals of \((i\xi)^\beta r(\xi)\) for every \(\beta\), retaining \((2\pi)^{-n}\).

We also need the precise receiving map for a compact distribution, rather than a kernel picture. If \(g\) has compact support disjoint from a relatively compact open neighborhood \(W\), choose \(\eta\in C_c^\infty\) equal to one near \(\operatorname{supp}g\), with support disjoint from \(\overline W\). On \(W\) the actual multiplier \(q(D)g\) is the function
\[
(q(D)g)(x)=\langle g(y),\eta(y)K_q(x-y)\rangle.
\tag{HC6}
\]
The pairing is complex-linear, with no conjugation. A compact distribution has a finite derivative-order bound on the fixed compact support of \(\eta\). All derivatives of \(K_q\) are continuous on the resulting compact set of differences away from zero. Difference quotients and their Taylor integral remainders converge uniformly through that finite order. Applying the bound for \(g\) proves arbitrary differentiability in \(x\), with derivative obtained by replacing \(K_q\) by \(\partial_x^\beta K_q\) in (HC6). To identify the function with the multiplier, pair it with a test function supported in \(W\). Moving its compact integral through the continuous distribution pairing gives the distribution convolution \(K_q*g\); Fourier transformation of convolution with a compact distribution is multiplication of its Fourier transform by \(q\), with the original inverse factor. This identity follows first for compact smooth approximants of \(g\) by the full Fourier integral, and then by their distribution limit; multiplication by \(q\) is continuous on \(\mathcal S'\). Thus (HC6) is the required restriction of the actual multiplier. The same argument for \(K_r\) proves that \(r(D)g\) is smooth everywhere for every compact distribution \(g\), without a separation condition.

Finally let \(u\in\mathcal D'(U)\), with \(f=P(D)u\in C^\infty(U)\). Fix \(x_0\in U\); choose \(\chi\in C_c^\infty(U)\) equal to one on an open neighborhood \(V\) of \(x_0\), and extend \(v=\chi u\) by zero to its actual compact tempered distribution. Writing the unchanged original polynomial as \(P(\xi)=\sum_{|\alpha|\le m}p_\alpha\xi^\alpha\), the full Leibniz formula is
\[
\begin{aligned}
P(D)v&=\chi f+g,\\
g&=\sum_{|\alpha|\le m}p_\alpha
 \sum_{0<\beta\le\alpha}\binom\alpha\beta
 (D^\beta\chi)D^{\alpha-\beta}u.
\end{aligned}
\tag{HC7}
\]
Each term is formed on \(U\), has compact support inside \(U\), and then extends by zero. The full factors \(D^\beta\chi=(-i)^{|\beta|}\partial^\beta\chi\) and \(D^{\alpha-\beta}=(-i)^{|\alpha-\beta|}\partial^{\alpha-\beta}\) remain. Every term of \(g\) is supported outside \(V\). Choose a smaller neighborhood \(W\) of \(x_0\) with closure in \(V\). Applying (HC3) to the actual \(v\) gives
\[
v=q(D)(\chi f)+q(D)g+r(D)v.
\tag{HC8}
\]
The first term is Schwartz, because \(\chi f\) is compactly supported smooth and the polynomial derivative bounds of \(q\) preserve every Schwartz seminorm under multiplication in Fourier space. The second is smooth on \(W\) by (HC6), and the third is smooth everywhere by its proved compact-distribution map. Therefore \(u=v\) is smooth near \(x_0\). Since \(U,u,x_0\) were arbitrary, (i) follows. This proves all directions of (HC1), without assuming the local regularity conclusion or suppressing the actual commutator contributions.

A nonzero constant polynomial is separately hypoelliptic: \(P(D)u=p_0u\) and its actual inverse is multiplication by \(p_0^{-1}\). Its zero set is empty, so (HC1)'s nonconstant distance statement is not used for it. In dimension zero the space has one point and the same constant argument applies. The zero polynomial is excluded throughout. These are editorial consequences of the original full polynomial calculation; its original forward statement and historical attribution remain identifiable.

## 11. Worked examples

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

## 12. Exercises and solutions

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

## Further questions

The next structural questions have distinct hypotheses: coordinate changes introduce a lower bound on \(\delta\) relative to \(1-\rho\); positivity estimates depend on more than boundedness; and boundary kernels require additional structure near the normal-frequency directions. The endpoint example (E47) is a useful test for any proposed extension that claims a decreasing symbolic error at \(\delta=\rho\).

The classical summation results cited below do not themselves supply the entire \(\delta>\rho\) range or the Besov sequence endpoints proved here.

## References

- Lars Hörmander, *The Analysis of Linear Partial Differential Operators III: Pseudo-Differential Operators*, corrected second printing, Springer, 1994, §18.1 and Appendix B.1.
- Nicolas Lerner, [first chapter](https://webusers.imj-prg.fr/~nicolas.lerner/ch1booklerner.pdf), Lemma 1.1.24 and Remark 1.1.28; [metric chapter](https://webusers.imj-prg.fr/~nicolas.lerner/ch2booklerner.pdf), Lemma 2.2.18 and Theorems 2.3.7 and 2.5.1. These are the author-hosted September 2009 chapter files used for the earlier source comparison.
- Richard Melrose, [Pseudodifferential-operator lectures](https://math.mit.edu/~rbm/18.157-F05.pdf), version 0.7E, 29 November 2006.
