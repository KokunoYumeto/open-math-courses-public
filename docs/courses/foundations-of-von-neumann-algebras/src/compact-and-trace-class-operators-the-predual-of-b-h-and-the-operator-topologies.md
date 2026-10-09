# Compact and trace-class operators, the predual of B(H), and the operator topologies

*Originally written by Claude Opus 5.5 (Anthropic), September 2026, with a separate historical AI spot-check; revised and self-checked by that writing AI in October 2026. GPT-6.1 Sol (OpenAI), at the Ultra setting, read and self-checked the full lesson and all five solutions, completed the measure, Fourier and Schatten-extension proofs and corrected the topology hypothesis and examples, October 2026. Public domain (CC0).*

Let \(H\) be a Hilbert space. The algebra \(B(H)\) of all bounded operators on \(H\) is the dual of a Banach space, and this one fact produces most of the topologies used in the theory of operator algebras. This lesson builds the three Banach spaces behind it: the compact operators \(K(H)\), the trace-class operators \(\mathcal L^1(H)\), and \(B(H)\) itself. The dual of \(K(H)\) is \(\mathcal L^1(H)\), and the dual of \(\mathcal L^1(H)\) is \(B(H)\), just as the dual of the sequence space \(c_0\) is \(\ell^1\) and the dual of \(\ell^1\) is \(\ell^\infty\). On the way we develop the Schmidt decomposition of a compact operator, its singular values, the Hilbert–Schmidt operators and the trace.

The second half studies the topologies of \(B(H)\). Besides the norm topology there are six locally convex topologies: the weak, strong and strong\(^*\) topologies, which test an operator on finitely many vectors, and their \(\sigma\)-versions, which test it on square-summable sequences of vectors and come from the duality with \(\mathcal L^1(H)\). We compare them, find their continuous linear functionals, show that a convex set has the same closure in all topologies with the same continuous functionals, prove the Krein–Šmulian theorem on weak\(^*\) closed convex sets, and decide when these topologies are metrizable.

Several applications follow. We classify the two-sided ideals of \(B(H)\) by spaces of sequences, following Calkin, and show that the Calkin algebra \(B(H)/K(H)\) cannot act nontrivially on a separable Hilbert space. We show that every state that vanishes on the compact operators is a limit of vector states. The last section compares two small ideals through their effect on self-adjoint operators. By the Weyl–von Neumann theorem, when \(H\) is separable, a Hilbert–Schmidt perturbation of arbitrarily small norm makes any self-adjoint operator diagonal. By the Kato–Rosenblum theorem, a trace-class perturbation never changes the absolutely continuous part, up to unitary equivalence. So the Hilbert–Schmidt condition in the first theorem cannot be replaced by the trace-class condition.

We assume basic Hilbert space theory, the spectral theorem for compact self-adjoint operators and the continuous functional calculus, as in the lesson [C\*-algebras: continuous functional calculus, automatic continuity, positive cones, approximate identities and quotients](c-star-algebras-continuous-functional-calculus-automatic-continuity-positive-cones.md). Sections 7 and 11 also use the spectral theorem in its projection-valued form, and Section 11 uses some Fourier analysis on the real line. Everything used without proof is stated in the section *Results used from other lessons*. The topologies of Sections 8 and 9 are used throughout the next lesson, [The double commutant theorem](the-double-commutant-theorem.md).

Freely readable background is [van Neerven] and [Blackadar]. The trace-class duality and the scattering arguments used in Section 11 are proved in full below.

## Conventions

Hilbert spaces are complex. They may have any dimension; separability is assumed only where it is stated. Inner products are linear in the first variable and conjugate linear in the second.

- \(B(H)\) is the algebra of bounded operators on \(H\), \(K(H)\) the compact operators, \(F(H)\) the operators of finite rank, and \(1\) the identity. \(B(H)_1\) is the closed unit ball, \(B(H)_{\mathrm{sa}}\) the set of self-adjoint operators, and \(B(H)_+\) the set of positive operators. An operator \(x\) is *positive*, \(x\ge0\), when \(\langle x\xi,\xi\rangle\ge0\) for all \(\xi\). A positive \(x\) has a unique positive square root \(x^{1/2}\), and \(|x|=(x^*x)^{1/2}\).
- For \(\xi,\eta\in H\) we write \(\theta_{\xi,\eta}\) for the operator \(\zeta\mapsto\langle\zeta,\eta\rangle\xi\), and \(\omega_{\xi,\eta}\) for the functional \(x\mapsto\langle x\xi,\eta\rangle\) on \(B(H)\); \(\omega_\xi=\omega_{\xi,\xi}\).
- A family \((a_i)_{i\in I}\) in a normed space is *summable* with sum \(a\) when the finite partial sums converge to \(a\) along the directed set of finite subsets of \(I\). For numbers \(a_i\ge0\) the sum is the supremum of the finite partial sums, a number in \([0,\infty]\). An absolutely summable family in a Banach space may be summed in any order and grouped in any way. Indeed, if \(\sum_i\|a_i\|<\infty\), each set \(\{i:\|a_i\|\geq1/n\}\) is finite, so the nonzero support is countable. For every \(\varepsilon>0\), a finite partial norm sum lies within \(\varepsilon\) of the supremum, and all disjoint finite tail sums then have norm at most \(\varepsilon\). Completeness gives the finite-subset-net limit. The same tail estimate shows that every ordering or grouping has this limit. It applies to scalars in particular, and to square-summable norms when proving countable support in \(\ell^2\).
- For a set \(I\): \(\ell^\infty(I)\) is the space of bounded families \(\lambda=(\lambda_i)_{i\in I}\) of scalars; \(c_0(I)\) consists of those with only finitely many \(|\lambda_i|\ge\varepsilon\) for every \(\varepsilon>0\); \(\ell^1(I)\) and \(\ell^2(I)\) are the summable and square-summable families; \(c_{00}(I)\) the finitely supported ones; \(\delta_i\) is the family with \(1\) at \(i\) and \(0\) elsewhere. For \(I=\mathbb N\) we write \(\ell^\infty,c_0,\ell^1,\ell^2,c_{00}\).
- \(\ell^2(I;H)\) is the Hilbert space of families \((\xi_i)_{i\in I}\) in \(H\) with \(\sum_i\|\xi_i\|^2<\infty\), with inner product \(\sum_i\langle\xi_i,\eta_i\rangle\). A sequence \((\xi_n)\) with \(\sum_n\|\xi_n\|^2<\infty\) is called *square summable*.
- The *conjugate space* \(\overline H\) consists of the symbols \(\bar\xi\), \(\xi\in H\), with \(\bar\xi+\bar\eta=\overline{\xi+\eta}\), \(c\,\bar\xi=\overline{\bar c\,\xi}\) and \(\langle\bar\xi,\bar\eta\rangle=\langle\eta,\xi\rangle\). It is a Hilbert space, and \(\xi\mapsto\bar\xi\) is conjugate linear and isometric.

## Results used from other lessons

The facts below are proved in these earlier lessons: Hahn–Banach, Baire and the basic theorems on Banach spaces (*the Hahn–Banach lesson*), [Weak topologies: Tychonoff, Banach–Alaoglu, Mazur, bipolars, Krein–Milman and Eberlein–Šmulian](weak-topologies-tychonoff-banach-alaoglu-mazur-bipolars-krein-milman-and-eberlein-smulian.md) (*the lesson on weak topologies*), [Hilbert spaces and compact operators](hilbert-spaces-and-compact-operators.md) (*the Hilbert-space lesson*) and [The spectral theorem for bounded self-adjoint operators](the-spectral-theorem-for-bounded-self-adjoint-operators.md) (*the spectral-theorem lesson*). The exact measure proofs are Theorems 1.1, 2.1–2.2, 3.1–3.2 and 4.1 of the measure-tools lesson, the [generating-family lemma and probability products](the-double-commutant-theorem.md#oa-fnd-bi-18), and the real-line tools proved immediately below. Fremlin’s paragraph numbers remain human bibliographic references, rather than proof providers.

1. **Hilbert spaces** (the Hilbert-space lesson). (a) *Riesz representation* (Theorem 2.3). Every bounded linear functional \(f\) on \(H\) has the form \(f(\xi)=\langle\xi,\eta\rangle\) for a unique \(\eta\in H\). (b) *Bessel and Parseval* (Theorem 4.1(1) and (3)). For an orthonormal family \((\varepsilon_i)\), \(\sum_i|\langle\xi,\varepsilon_i\rangle|^2\le\|\xi\|^2\). If the family is an orthonormal basis, then \(\xi=\sum_i\langle\xi,\varepsilon_i\rangle\varepsilon_i\) and \(\langle\xi,\eta\rangle=\sum_i\langle\xi,\varepsilon_i\rangle\langle\varepsilon_i,\eta\rangle\). (c) Every orthonormal family is contained in an orthonormal basis (Theorem 4.1(4)). (d) *Cauchy–Schwarz for forms* (Proposition 1.1(3)). If \(B\) is a sesquilinear form on a complex vector space with \(B(\xi,\xi)\ge0\) for all \(\xi\), then \(|B(\xi,\eta)|^2\le B(\xi,\xi)B(\eta,\eta)\).
2. **Compact operators** (the Hilbert-space lesson). (a) \(K(H)\) is a norm-closed two-sided ideal of \(B(H)\), closed under adjoints, and it is the norm closure of \(F(H)\) (Theorem 5.1). (b) *Spectral theorem for compact self-adjoint operators* (Theorem 6.2). If \(x\in K(H)\) is self-adjoint and \(x\ne0\), there are an orthonormal family \((e_n)_{n\in N}\), with \(N=\{1,\dots,r\}\) or \(N=\mathbb N\), and real numbers \(\lambda_n\ne0\) with \(|\lambda_1|\ge|\lambda_2|\ge\cdots\), tending to \(0\) when \(N=\mathbb N\), such that \(x=\sum_n\lambda_n\theta_{e_n,e_n}\) with convergence in norm. The nonzero eigenvalues of \(x\) are the \(\lambda_n\); the eigenspace of an eigenvalue \(\mu\ne0\) is spanned by the \(e_n\) with \(\lambda_n=\mu\) and is finite-dimensional. If \(x\ge0\), all \(\lambda_n\) are positive.
3. **Functional calculus.** (a) *Continuous calculus.* For a self-adjoint operator the continuous functional calculus exists; positive operators have unique positive square roots, and \(x^{1/2}\) commutes with every operator that commutes with \(x\). See the lesson on C\*-algebras named above. (b) *Spectral theorem* (the spectral-theorem lesson, Theorems 3.1 and 4.4 and Remark 4.5). For \(h\in B(H)_{\mathrm{sa}}\) there is a unique projection-valued measure \(E\) on the Borel sets of \(\mathbb R\), supported in \([-\|h\|,\|h\|]\), with \(h=\int\lambda\,dE(\lambda)\). For bounded Borel functions \(f\), the operators \(f(h)=\int f\,dE\) form a \(*\)-homomorphism \(f\mapsto f(h)\) that extends the continuous calculus, with \(\|f(h)\|\le\sup|f|\) and \(f(h)\ge0\) when \(f\ge0\); each \(f(h)\) commutes with every operator that commutes with \(h\). For \(\xi\in H\), \(\mu_\xi(\Delta)=\langle E(\Delta)\xi,\xi\rangle=\|E(\Delta)\xi\|^2\) is a finite positive Borel measure, the *spectral measure* of \(\xi\), with \(\mu_\xi(\mathbb R)=\|\xi\|^2\) and \(\langle f(h)\xi,\xi\rangle=\int f\,d\mu_\xi\). We write \(e^{ith}\) for \(f(h)\) with \(f(\lambda)=e^{it\lambda}\); it is the sum of the exponential series.
4. **Measure theory and Fourier analysis.** (a) A finite positive Borel measure on \(\mathbb R\) that vanishes on Lebesgue null sets has an \(L^1\) density: Theorem 4.1 of the measure-tools lesson. Lebesgue measure and its sigma-finiteness are constructed in Lemma 0.1(b) below. (b) \(C_c^\infty(I)\) is dense in \(L^2(I)\) for every open interval \(I\), by Lemma 0.1(c). (c) With \(\widehat w(s)=\int e^{-is\lambda}w(\lambda)\,d\lambda\), Theorem 0.3 gives \(\int|\widehat w|^2=2\pi\int|w|^2\) and the unitary extension of \((2\pi)^{-1/2}\widehat w\). Lemma 0.2 proves the normalized Gaussian transform with this same sign and constant. (d) The full Dynkin-system/generating-family proof is the lemma preceding the probability product theorem linked above. It also determines finite signed measures of finite variation: if their difference is \(\nu\), the finite measures \((|\nu|+\nu)/2\) and \((|\nu|-\nu)/2\) are positive, since \(|\nu(E)|\leq|\nu|(E)\); agreement on the generating family makes these two positive measures agree there, hence everywhere. Countable additivity of variation is proved in [the complex-measure tools](abelian-operator-algebras.md#oa-fnd-ao-23). (e) Monotone and dominated convergence are Theorems 2.1–2.2 of the measure-tools lesson. Lemma 0.1(a) proves Tonelli and Fubini for arbitrary sigma-finite measure spaces; it imposes no topological condition on the spaces.
5. **Locally convex spaces.** (a) *Hahn–Banach separation* (the Hahn–Banach lesson, Theorems 6.2 and 6.3). If \(A\) and \(B\) are disjoint nonempty convex subsets of a topological vector space and \(A\) is open, there are a continuous linear functional \(f\) and \(\gamma\in\mathbb R\) with \(\operatorname{Re}f(a)<\gamma\le\operatorname{Re}f(b)\) for \(a\in A\), \(b\in B\). If the space is locally convex, \(A\) is compact and \(B\) is closed, then even \(\operatorname{Re}f(a)<\gamma_1<\gamma_2<\operatorname{Re}f(b)\). (b) *Weak topologies of a dual pair* (the lesson on weak topologies, Theorem 1.2). If \(Y\) is a vector space of linear functionals on a vector space \(X\) that separates the points of \(X\), then the topology \(\sigma(X,Y)\) of pointwise convergence on \(Y\) is locally convex, and its continuous linear functionals are exactly the elements of \(Y\). (c) *Closures of convex sets* (the lesson on weak topologies, Theorem 4.2). In a locally convex space \(X\) with continuous dual \(X^*\), a convex set has the same closure in the given topology and in \(\sigma(X,X^*)\). Hence two locally convex topologies on \(X\) with the same continuous linear functionals have the same closed convex sets. (d) *Banach–Alaoglu* (the lesson on weak topologies, Theorem 3.1). The closed unit ball of the dual \(X^*\) of a normed space \(X\) is compact for \(\sigma(X^*,X)\). (e) *Annihilators* (the lesson on weak topologies, Theorem 5.1(2) and Proposition 5.4). Let \(X\) be a Banach space. For a subspace \(N\subseteq X^*\), the \(\sigma(X^*,X)\)-closure of \(N\) is \(({}^\perp N)^\perp\), where \({}^\perp N=\{x:f(x)=0\ \text{for all}\ f\in N\}\) and \(({}^\perp N)^\perp=\{f\in X^*:f=0\ \text{on}\ {}^\perp N\}\). For a closed subspace \(M\subseteq X\) with quotient map \(q:X\to X/M\), the map \(g\mapsto g\circ q\) is an isometric isomorphism of \((X/M)^*\) onto \(M^\perp\). (f) *Norming* (the Hahn–Banach lesson, Corollary 2.3(2)). For every \(z\) in a normed space \(Z\), \(\|z\|=\sup\{|g(z)|:g\in Z^*,\ \|g\|\le1\}\). (g) *Krein–Milman and Milman* (the lesson on weak topologies, Theorems 6.1 and 6.2). In a Hausdorff locally convex space, a nonempty compact convex set is the closed convex hull of its extreme points; and if \(Q\) is compact and the closed convex hull of \(Q\) is compact, then every extreme point of that hull lies in \(Q\). (h) *Closed kernels* (the Hahn–Banach lesson, Lemma 6.5). A linear functional on a topological vector space is continuous if its kernel is closed. (i) *Uniform boundedness* (the Hahn–Banach lesson, Theorem 4.2). A family of bounded operators from a Banach space to a normed space that is bounded at each point is bounded in norm.

### Measure and Fourier tools on the real line

The perturbation argument needs the real-line Fourier transform with its exact constant. We prove that version here. The measure results used in the proof are Carathéodory, monotone and dominated convergence, Hölder, completeness and Radon–Nikodym, Theorems 1.1, 2.1–2.2, 3.1–3.2 and 4.1 of *Measure and Hilbert space tools for Haar integration*. The construction below also uses [the probability product theorem and its generating-family lemma](the-double-commutant-theorem.md#oa-fnd-bi-18). Those proofs use the measure-tools lesson, and do not use the operator-topology or Fourier results of this lesson.

**Lemma 0.1 (sigma-finite products and real-line measure).**

(a) If \((X,\Sigma,\mu)\) and \((Y,\mathcal T,\nu)\) are sigma-finite measure spaces, their product measure exists on \(\Sigma\otimes\mathcal T\). For a nonnegative measurable \(F\), both iterated integrals are measurable and
\[
\begin{gathered}
\int F\,d(\mu\otimes\nu)
\\
=\int_X\!\int_Y F(x,y)\,d\nu(y)\,d\mu(x)
\\
=\int_Y\!\int_X F(x,y)\,d\mu(x)\,d\nu(y).
\end{gathered}
\]
For an integrable complex \(F\), the sections are integrable almost everywhere and the same identities hold. Classes in the completed product may be represented by functions measurable for the uncompleted product; iterated integrals are taken using such representatives.

(b) Lebesgue measure can be constructed as normalized Haar measure on \(\mathbb R\), completed on its null sets. It is sigma-finite, translation invariant, and assigns length \(b-a\) to \((a,b)\). A set is null exactly when, for every \(\varepsilon>0\), it has a countable cover by open intervals of total length less than \(\varepsilon\). Every null set is contained in a null Borel set. A locally Lipschitz map between real intervals maps null sets to null sets.

(c) \(C_c^\infty(I)\) is dense in \(L^2(I)\) for every open interval \(I\). Translations are continuous in \(L^2(\mathbb R)\), and convolution with a nonnegative integral-one kernel \(\alpha_j\) converges to the identity in \(L^2\) if
\[
\int_{|t|>\delta}\alpha_j(t)\,dt\longrightarrow0
\quad\text{for every }\delta>0.
\]

*Proof.* (a) First suppose both measures are finite and nonzero. Normalize them to probability measures, apply the proved probability product theorem to these two factors, and multiply the resulting measure by \(\mu(X)\nu(Y)\). If either total mass is zero use the zero product measure. For finite measures, let \(\mathcal D\) consist of the measurable sets \(E\) for which the sections are measurable, \(x\mapsto\nu(E_x)\) is measurable and
\(\int\nu(E_x)\,d\mu(x)=(\mu\otimes\nu)(E)\).
Rectangles belong to \(\mathcal D\). It is a Dynkin system: it contains the whole product, nested differences follow by subtraction of finite section measures and finite integrals, and countable disjoint unions follow by monotone convergence. The generating-family proof linked above therefore gives every product-measurable set. Interchanging the factors proves the other section identity. Nonnegative simple approximation followed by monotone convergence proves the formula for every \(F\geq0\). Apply it to \(|F|\) and then to the positive and negative real and imaginary parts for integrable \(F\).

For sigma-finite measures, partition \(X\) and \(Y\) into countably many disjoint measurable pieces \(X_n,Y_m\) of finite measure, by disjointifying finite-measure exhaustions. On each \(X_n\times Y_m\) use the finite construction and sum the resulting measures. Rectangles have the required product values: the double sum of \(\mu(A\cap X_n)\nu(B\cap Y_m)\) is \(\mu(A)\nu(B)\), with zero times infinity interpreted as zero. Two candidate measures agree on each finite block by generating-family uniqueness, hence on the product. Apply the finite-block integral identity and monotone convergence to the countable blocks to obtain both iterated formulas. A completed-measurable function has a product-measurable representative: replace the sets in its countable simple approximations by measurable sets differing by subsets of measurable null sets. Their union is one measurable null set. Tonelli says its sections are null almost everywhere, so the integral identities are independent of the representative.

(b) Haar existence and uniqueness, Theorems 8.3 and 9.2, give a nonzero Radon measure on \(\mathbb R\), finite on compact sets and positive on nonempty open sets. Every singleton has the same mass \(c\) by translation invariance. Placing arbitrarily many distinct points in \([0,1]\) gives \(Nc\leq\mu([0,1])\), so \(c=0\). Normalize \(\mu([0,1])\) to one; this mass is finite and positive. Partitioning into equal intervals gives \(\mu([0,q])=q\) for nonnegative rational \(q\). Increasing rational endpoints to \(t\geq0\), countable additivity gives \(\mu([0,t])=t\). Translation and the zero mass of endpoints give every interval length. The intervals \([-n,n]\) show sigma-finiteness.

Every open subset of the line is a countable disjoint union of open intervals: each component is an interval and contains a different rational point. Its measure is the sum of their lengths. Outer regularity of Haar measure now says that a null Borel set has open interval covers of arbitrarily small total length. The same statement holds for a subset of a null Borel set. Conversely, such covers force outer measure zero; Carathéodory's construction includes these subsets in the completion. Intersecting open covers with total lengths tending to zero supplies a null Borel superset. If \(g\) is Lipschitz with constant \(L\) on an interval, the image of each covering interval has diameter at most \(L\) times its length; enlarge the image intervals by summably small amounts if necessary. The covering criterion shows that \(g\) maps null sets to null sets. A locally Lipschitz map is Lipschitz on a countable cover by compact subintervals, which gives the local assertion.

Integrals of continuous functions on compact intervals agree with Riemann integrals: uniform step-function approximations have integral error at most interval length times their uniform error. Reflection preserves Lebesgue measure. For \(a>0\), the pushforward under \(x\mapsto ax\) assigns \((b,c)\) mass \((c-b)/a\); generating-family uniqueness on bounded intervals therefore gives \(\int F(ax)\,dx=a^{-1}\int F(y)\,dy\) for nonnegative or integrable \(F\). Thus the elementary substitution and integration-by-parts formulas from [Lemma 0.1 of the Cauchy lesson](cauchy-s-theorem-for-cycles-and-its-consequences.md#oa-fnd-ct-07) apply to the continuous integrands below.

(c) The Haar density proof, Proposition 3.1(4), supplies \(C_c(\mathbb R)\)-density in \(L^2(\mathbb R)\). For a proper open interval \(I\), let \(d(x)=\operatorname{dist}(x,\mathbb R\setminus I)\) and set \[
\begin{gathered}
\chi_n(x)\\
=\min(1,\max(0,nd(x)-1))\\
{}\cdot\min(1,\max(0,n-|x|));
\end{gathered}
\] for \(I=\mathbb R\) omit the first factor. These continuous cutoffs have compact support inside \(I\), increase to one there, and lie between zero and one. Extend a function on \(I\) by zero, approximate it by \(C_c(\mathbb R)\), and multiply the approximants by a fixed \(\chi_n\). The error does not increase; dominated convergence then gives \(C_c(I)\)-density. For an explicit smooth kernel set
\[
\beta(t)=
\begin{cases}
\exp\big(-1/(1-t^2)\big),&|t|<1,\\
0,&|t|\geq1.
\end{cases}
\]
Inside \((-1,1)\), every derivative is the exponential times a rational function with a finite power of \(1-t^2\) in its denominator. These derivatives tend to zero at the endpoints: \(u^Ne^{-u}\to0\) as \(u\to\infty\), since the exponential series bounds \(e^u\) below by \(u^{N+1}/(N+1)!\). Inductively the extensions of all derivatives are continuous with zero endpoint values, so \(\beta\) is smooth on the line. Normalize its positive finite integral and rescale to obtain \(\beta_\varepsilon\), supported in \([-\varepsilon,\varepsilon]\) with integral one. For \(f\in C_c(I)\), differentiation of \(f*\beta_\varepsilon\) falls on the kernel; compact parameter differentiation from the Cauchy lemma justifies every derivative. For small \(\varepsilon\) the support remains inside \(I\), and uniform continuity gives uniform convergence to \(f\). A common finite-length compact support gives convergence in \(L^2\).

Translations \(\tau_tf(x)=f(x-t)\) are isometries by (b). For \(f\in C_c(\mathbb R)\), uniform continuity and a common compact support give \(\|\tau_tf-f\|_2\to0\) as \(t\to0\); density and the isometry extend this to every \(f\in L^2\). Cauchy–Schwarz with the probability density \(\alpha_j\), followed by Tonelli, gives
\[
\|f*\alpha_j-f\|_2^2
\leq\int\alpha_j(t)\|\tau_tf-f\|_2^2\,dt.
\]
It also shows that the convolution integral exists almost everywhere. Choose a neighbourhood of zero on which the squared norm in the integrand is small, and bound it on the complement by \(4\|f\|_2^2\). The concentration hypothesis finishes the proof. \(\square\)

**Lemma 0.2 (Gaussian transform).** For \(\sigma>0\) the function
\[
\gamma_\sigma(x)=\frac{1}{\sqrt{2\pi}\,\sigma}
\exp\left(-\frac{x^2}{2\sigma^2}\right)
\]
has integral one and transform
\[
\int_{\mathbb R}e^{-itx}\gamma_\sigma(x)\,dx
=e^{-\sigma^2t^2/2}.
\]
Its mass outside any fixed neighbourhood of zero tends to zero as \(\sigma\downarrow0\).

*Proof.* The integral \(J=\int e^{-x^2}\,dx\) is finite, since outside \([-1,1]\) its integrand is bounded by \(e^{-|x|}\). Tonelli gives \(J^2=\int_{\mathbb R^2}e^{-x^2-y^2}\,dx\,dy\). The disc of radius \(r\) has area
\[
\int_{-r}^r2\sqrt{r^2-x^2}\,dx=\pi r^2:
\]
its sections give the first expression by Tonelli, and \(x=r\sin\theta\), \(-\pi/2\leq\theta\leq\pi/2\), gives the second by the elementary substitution formula. Write \(e^{-x^2-y^2}=\int_0^1 1_{\{u<e^{-x^2-y^2}\}}\,du\) and use Tonelli again. Then
\[
J^2=\int_0^1\pi(-\log u)\,du=\pi.
\]
The last integral follows by integrating on \([\delta,1]\) and letting \(\delta\downarrow0\); \(\delta\log\delta\to0\) by the same exponential estimate. Since \(J>0\), \(J=\sqrt\pi\). Scaling gives the stated normalization.

Let \(\phi(t)=\int e^{-itx}\gamma_\sigma(x)\,dx\). Dominated convergence differentiates under the integral, since the difference quotients are bounded by \(|x|\gamma_\sigma(x)\), which is integrable. Since \(\gamma_\sigma'(x)=-x\gamma_\sigma(x)/\sigma^2\), integration by parts first on \([-R,R]\) and then letting \(R\to\infty\) gives
\[
\phi'(t)=i\sigma^2\int e^{-itx}\gamma_\sigma'(x)\,dx
=-\sigma^2t\phi(t).
\]
The boundary terms tend to zero and both improper integrals converge absolutely. Differentiating \(e^{\sigma^2t^2/2}\phi(t)\) shows it is constant, equal to \(\phi(0)=1\). Finally, the substitution \(x=\sigma v\) identifies the tail mass with \(\int_{|v|>\delta/\sigma}\gamma_1(v)\,dv\), which tends to zero by integrability. \(\square\)

**Theorem 0.3 (real-line Plancherel).** For \(f\in L^1(\mathbb R)\cap L^2(\mathbb R)\), put \(\widehat f(t)=\int e^{-itx}f(x)\,dx\). Then
\[
\int|\widehat f(t)|^2\,dt=2\pi\int|f(x)|^2\,dx.
\]
The operator \(T:f\mapsto(2\pi)^{-1/2}\widehat f\) extends uniquely to a unitary operator on \(L^2(\mathbb R)\).

*Proof.* For \(\varepsilon>0\), Fubini and Lemma 0.2 give
\[
\begin{gathered}
\int e^{-\varepsilon t^2}|\widehat f(t)|^2\,dt
\\
=\sqrt{\frac\pi\varepsilon}
\int\!\int f(x)\overline{f(y)}\\
{}\cdot e^{-(x-y)^2/(4\varepsilon)}\,dx\,dy\\
\\
=2\pi\langle f,f*\gamma_{\sqrt{2\varepsilon}}\rangle.
\end{gathered}
\]
The interchange is justified before computing the inner integral: the integral of the absolute value of the three-variable integrand is
\(\|f\|_1^2\int e^{-\varepsilon t^2}\,dt<\infty\).
The last convolution converges to \(f\) in \(L^2\) by Lemmas 0.1(c) and 0.2. On the left let \(\varepsilon=1/n\); monotone convergence proves the norm identity. The domain contains \(C_c^\infty\) and is dense in \(L^2\), so completeness extends \(T\) to an isometry with closed range. Polarization gives inner-product preservation.

We prove surjectivity as well. If \(g\in C_c^\infty(\mathbb R)\), two integrations by parts give
\[
|\widehat g(t)|\leq
\min\big(\|g\|_1,\,|t|^{-2}\|g''\|_1\big)
\quad(t\ne0).
\]
Thus \(\widehat g\in L^1\cap L^2\). Fubini and the Gaussian formula show that
\[
\frac1{2\pi}\int e^{itx}e^{-\varepsilon t^2}
\widehat g(t)\,dt
=(g*\gamma_{\sqrt{2\varepsilon}})(x).
\]
The absolute-integrability justification is \(\|g\|_1\int e^{-\varepsilon t^2}\,dt<\infty\). The right side tends to \(g(x)\) for every \(x\), by bounded uniform continuity and Gaussian concentration. Dominated convergence on the left, using \(\widehat g\in L^1\), gives
\[
g(x)=\frac1{2\pi}\int e^{itx}\widehat g(t)\,dt.
\]
Consequently \(T^2g(x)=g(-x)\). The range of \(T\) therefore contains every reflection of a function in \(C_c^\infty\), a dense subspace. Its closed range is all of \(L^2\). \(\square\)

Lemmas 0.1–0.3 give the measure, product-integration and Fourier arguments used below, including their hypotheses, sign and normalization. The exact earlier programme proofs used in Lemma 0.1 are identified there.


## 1. Forms, rank-one operators and vector functionals

Bounded operators on a Hilbert space are the same thing as bounded sesquilinear forms. This section sets up that dictionary, and the simplest operators and functionals, which are built from two vectors.

**Definition 1.1.** A *sesquilinear form* on \(H\) is a map \(B:H\times H\to\mathbb C\) that is linear in the first variable and conjugate linear in the second. (The same words are used for forms on any complex vector space, and for maps with values in any complex vector space.) The form is *hermitian* if \(B(\eta,\xi)=\overline{B(\xi,\eta)}\) for all \(\xi,\eta\), *positive* if \(B(\xi,\xi)\ge0\) for all \(\xi\), and *bounded* if
\[
\|B\|=\sup\{|B(\xi,\eta)|:\ \|\xi\|\le1,\ \|\eta\|\le1\}
\]
is finite. The bounded forms make up a normed space \(\operatorname{Sesq}(H)\).

**Lemma 1.2** (polarization). For every sesquilinear form \(B\) on \(H\), or on any complex vector space, and all vectors \(\xi,\eta\),
\[
\begin{gathered}
B(\xi,\eta)\\
=\frac14\sum_{k=0}^{3}i^k\,B(\xi+i^k\eta,\ \xi+i^k\eta).
\end{gathered}
\tag{1.1}
\]
So \(B\) is determined by its values \(B(\zeta,\zeta)\). The form \(B\) is hermitian exactly when every value \(B(\zeta,\zeta)\) is real; in particular every positive form is hermitian.

**Proof.** Because \(B\) is conjugate linear in the second variable,
\[
\begin{gathered}
B(\xi+i^k\eta,\xi+i^k\eta)\\
=B(\xi,\xi)+\overline{i^k}\,B(\xi,\eta)+i^k B(\eta,\xi)+B(\eta,\eta).
\end{gathered}
\]
Multiply by \(i^k\) and add over \(k=0,1,2,3\). The terms with \(B(\xi,\xi)\) and \(B(\eta,\eta)\) carry the factor \(\sum_ki^k=0\), and the terms with \(B(\eta,\xi)\) carry \(\sum_ki^{2k}=0\), while \(i^k\overline{i^k}=1\). What remains is \(4B(\xi,\eta)\), which is (1.1).

If \(B\) is hermitian, then \(B(\zeta,\zeta)=\overline{B(\zeta,\zeta)}\) is real. Conversely, suppose every \(B(\zeta,\zeta)\) is real. Apply (1.1) to \(B(\eta,\xi)\). Since \(\eta+i^k\xi=i^k(\xi+i^{-k}\eta)\) and \(B(c\zeta,c\zeta)=|c|^2B(\zeta,\zeta)\), we get
\[
\begin{gathered}
B(\eta,\xi)\\
=\frac14\sum_k i^k\,B(\xi+i^{-k}\eta,\xi+i^{-k}\eta)\\
=\frac14\sum_j i^{-j}\,B(\xi+i^{j}\eta,\xi+i^{j}\eta),
\end{gathered}
\]
which is the complex conjugate of the right side of (1.1), because the values \(B(\xi+i^j\eta,\xi+i^j\eta)\) are real. \(\square\)

**Theorem 1.3.** For every bounded sesquilinear form \(B\) on \(H\) there is a unique \(t\in B(H)\) with \(B(\xi,\eta)=\langle t\xi,\eta\rangle\) for all \(\xi,\eta\). The map \(t\mapsto B_t\), \(B_t(\xi,\eta)=\langle t\xi,\eta\rangle\), is a linear isometry of \(B(H)\) onto \(\operatorname{Sesq}(H)\); in particular \(\operatorname{Sesq}(H)\) is a Banach space. The operator \(t\) is self-adjoint if and only if \(B_t\) is hermitian, and positive if and only if \(B_t\) is positive.

**Proof.** Fix \(\xi\). The map \(\eta\mapsto\overline{B(\xi,\eta)}\) is linear and bounded by \(\|B\|\,\|\xi\|\,\|\eta\|\). By the Riesz theorem there is a unique vector, which we call \(t\xi\), with \(\overline{B(\xi,\eta)}=\langle\eta,t\xi\rangle\), that is, \(B(\xi,\eta)=\langle t\xi,\eta\rangle\); and \(\|t\xi\|\le\|B\|\,\|\xi\|\). The uniqueness makes \(\xi\mapsto t\xi\) linear, so \(t\in B(H)\) and \(\|t\|\le\|B\|\).

For every \(t\in B(H)\) we have \(\|B_t\|=\sup|\langle t\xi,\eta\rangle|=\|t\|\): take \(\eta=t\xi/\|t\xi\|\) when \(t\xi\ne0\). So \(t\mapsto B_t\) is a linear isometry, and the first paragraph shows that it is onto. A normed space isometric to a Banach space is complete. The form \(B_t\) is hermitian exactly when \(\langle t\xi,\eta\rangle=\overline{\langle t\eta,\xi\rangle}=\langle\xi,t\eta\rangle\) for all \(\xi,\eta\), that is, when \(t=t^*\). Positivity of \(B_t\) is positivity of \(t\), by the definitions. \(\square\)

By Lemma 1.2, an operator \(t\) is self-adjoint exactly when \(\langle t\zeta,\zeta\rangle\) is real for all \(\zeta\), and every positive operator is self-adjoint.

**Lemma 1.4** (rank-one operators and vector functionals). Let \(\xi,\eta,\zeta,\upsilon\in H\) and \(a,b\in B(H)\).

(a) \(\|\theta_{\xi,\eta}\|=\|\xi\|\,\|\eta\|\) and \(\theta_{\xi,\eta}^*=\theta_{\eta,\xi}\).

(b) \(a\,\theta_{\xi,\eta}\,b=\theta_{a\xi,\,b^*\eta}\) and \(\theta_{\xi,\eta}\theta_{\zeta,\upsilon}=\langle\zeta,\eta\rangle\,\theta_{\xi,\upsilon}\).

(c) For a unit vector \(\xi\), \(\theta_{\xi,\xi}\) is the orthogonal projection onto \(\mathbb C\xi\).

(d) Every operator of rank one equals \(\theta_{\xi,\eta}\) for some nonzero \(\xi,\eta\). If \(x\in F(H)\) and \(\varepsilon_1,\dots,\varepsilon_r\) is an orthonormal basis of \(xH\), then \(x=\sum_{j=1}^r\theta_{\varepsilon_j,\,x^*\varepsilon_j}\). So \(F(H)\) is the linear span of the rank-one operators, and it is a two-sided ideal of \(B(H)\) closed under adjoints.

(e) \(\omega_{\xi,\eta}(\theta_{\zeta,\upsilon})=\langle\zeta,\eta\rangle\langle\xi,\upsilon\rangle\), and \(\|\omega_{\xi,\eta}\|=\|\xi\|\,\|\eta\|\), both as a functional on \(B(H)\) and on \(K(H)\).

**Proof.** (a) \(\|\theta_{\xi,\eta}\zeta\|=|\langle\zeta,\eta\rangle|\,\|\xi\|\le\|\zeta\|\,\|\eta\|\,\|\xi\|\), with equality for \(\zeta=\eta\). Also \[
\begin{gathered}
\langle\theta_{\xi,\eta}\zeta,\upsilon\rangle\\
=\langle\zeta,\eta\rangle\langle\xi,\upsilon\rangle\\
=\langle\zeta,\langle\upsilon,\xi\rangle\eta\rangle\\
=\langle\zeta,\theta_{\eta,\xi}\upsilon\rangle.
\end{gathered}
\]

(b) \(a\theta_{\xi,\eta}b\zeta=\langle b\zeta,\eta\rangle a\xi=\langle\zeta,b^*\eta\rangle a\xi\), and \(\theta_{\xi,\eta}\theta_{\zeta,\upsilon}\kappa=\langle\kappa,\upsilon\rangle\langle\zeta,\eta\rangle\xi\).

(c) \(\theta_{\xi,\xi}\zeta=\langle\zeta,\xi\rangle\xi\).

(d) The range \(xH\) is finite-dimensional. For every \(\zeta\), \(x\zeta=\sum_j\langle x\zeta,\varepsilon_j\rangle\varepsilon_j=\sum_j\langle\zeta,x^*\varepsilon_j\rangle\varepsilon_j\). For \(r=1\) this is \(\theta_{\varepsilon_1,x^*\varepsilon_1}\), and \(x^*\varepsilon_1\ne0\) because \(x\ne0\). By (a) and (b), adjoints of rank-one operators and products of them with bounded operators are again of rank at most one.

(e) \(\omega_{\xi,\eta}(\theta_{\zeta,\upsilon})=\langle\theta_{\zeta,\upsilon}\xi,\eta\rangle=\langle\xi,\upsilon\rangle\langle\zeta,\eta\rangle\). Clearly \(|\omega_{\xi,\eta}(x)|\le\|x\|\,\|\xi\|\,\|\eta\|\). On the other hand \(\omega_{\xi,\eta}(\theta_{\eta,\xi})=\|\xi\|^2\|\eta\|^2\) and \(\|\theta_{\eta,\xi}\|=\|\xi\|\,\|\eta\|\). Since \(\theta_{\eta,\xi}\) is compact, the norm is attained on \(K(H)\) as well. \(\square\)

## 2. Compact operators and singular values

A compact operator is a norm limit of operators of finite rank. Each one has a canonical form, the Schmidt decomposition. Its coefficients, the singular values, measure how well the operator can be approximated by operators of small rank.

**Lemma 2.1.** Let \(x\in K(H)\) and let \((\xi_n)\) be an orthonormal sequence. Then \(\|x\xi_n\|\to0\).

**Proof.** Let \(\varepsilon>0\), and choose \(f\in F(H)\) with \(\|x-f\|<\varepsilon\). By Lemma 1.4(d), \(f=\sum_{j\le r}\theta_{\varepsilon_j,f^*\varepsilon_j}\), so \(f\xi_n=\sum_{j\le r}\langle\xi_n,f^*\varepsilon_j\rangle\varepsilon_j\). By Bessel's inequality \(\langle\xi_n,f^*\varepsilon_j\rangle\to0\) for each \(j\), so \(f\xi_n\to0\). Hence \(\limsup_n\|x\xi_n\|\le\varepsilon\). \(\square\)

**Example 2.2** (diagonal operators). Let \((\varepsilon_i)_{i\in I}\) be an orthonormal basis of \(H\) and \(\lambda\in\ell^\infty(I)\). Put
\[
d_\lambda\zeta=\sum_i\lambda_i\langle\zeta,\varepsilon_i\rangle\varepsilon_i .
\]
The series converges because its coefficients are square summable, and \(\|d_\lambda\zeta\|^2=\sum_i|\lambda_i|^2|\langle\zeta,\varepsilon_i\rangle|^2\le\|\lambda\|_\infty^2\|\zeta\|^2\). Since \(d_\lambda\varepsilon_i=\lambda_i\varepsilon_i\), \(\|d_\lambda\|=\|\lambda\|_\infty\). One checks \(d_\lambda d_\mu=d_{\lambda\mu}\) and \(d_\lambda^*=d_{\bar\lambda}\). The operator \(d_\lambda\) is compact if and only if \(\lambda\in c_0(I)\). Indeed, if \(\lambda\in c_0(I)\) and \(F\subseteq I\) is a finite set outside of which \(|\lambda_i|<\varepsilon\), then \(d_{\lambda1_F}\) has finite rank and \(\|d_\lambda-d_{\lambda1_F}\|\le\varepsilon\). If \(\lambda\notin c_0(I)\), there are \(\varepsilon>0\) and distinct \(i_1,i_2,\dots\) with \(|\lambda_{i_n}|\ge\varepsilon\), so \(\|d_\lambda\varepsilon_{i_n}\|\ge\varepsilon\), and \(d_\lambda\) is not compact by Lemma 2.1. In this way \(\ell^\infty(I)\) and \(c_0(I)\) sit inside \(B(H)\) and \(K(H)\) as algebras of diagonal operators.

**Theorem 2.3** (Schmidt decomposition). Let \(x\in K(H)\), \(x\ne0\). There are orthonormal families \((e_n)_{n\in N}\) and \((f_n)_{n\in N}\), where \(N=\{1,\dots,r\}\) or \(N=\mathbb N\), and numbers \(s_1\ge s_2\ge\cdots>0\), tending to \(0\) when \(N=\mathbb N\), such that
\[
\begin{gathered}
x\\
=\sum_{n\in N}s_n\,\theta_{f_n,e_n},\\
\text{that is,}\\
x\zeta\\
=\sum_n s_n\langle\zeta,e_n\rangle f_n,
\end{gathered}
\tag{2.1}
\]
with convergence in norm. For every decomposition of this form:

(a) \(\|x\|=s_1\), the kernel of \(x\) is \(\{e_n:n\in N\}^\perp\), and \(xe_n=s_nf_n\), \(x^*f_n=s_ne_n\);

(b) \(x^*=\sum_ns_n\theta_{e_n,f_n}\), \(|x|=\sum_ns_n\theta_{e_n,e_n}\) and \(|x^*|=\sum_ns_n\theta_{f_n,f_n}\);

(c) the numbers \(s_n\), listed with repetitions, are the nonzero eigenvalues of \(|x|\) counted with multiplicity; so they do not depend on the decomposition;

(d) the operator \(v\zeta=\sum_n\langle\zeta,f_n\rangle e_n\) satisfies \(\|v\|\le1\), \(vx=|x|\) and \(v^*|x|=x\);

(e) if \(x\) is self-adjoint, a decomposition exists with \(f_n=\pm e_n\) for every \(n\), and if \(x\ge0\), one with \(f_n=e_n\);

(f) if \(x\) is self-adjoint and \(x=\sum_n\lambda_n\theta_{e_n,e_n}\) as in (e), then the spectrum of \(x\) contains every \(\lambda_n\), and \(\sigma(x)\setminus\{0\}=\{\lambda_n:n\in N\}\); if \(H\) is infinite-dimensional, then \(0\in\sigma(x)\), so \(\sigma(x)=\{\lambda_n:n\in N\}\cup\{0\}\).

**Proof.** *Existence.* The operator \(x^*x\) is compact and positive, since \(\langle x^*x\zeta,\zeta\rangle=\|x\zeta\|^2\). By Background 2(b), \(x^*x=\sum_n\mu_n\theta_{e_n,e_n}\) with an orthonormal family \((e_n)_{n\in N}\) and numbers \(\mu_1\ge\mu_2\ge\cdots>0\), tending to \(0\) if \(N=\mathbb N\). If \(x\zeta=0\), then \(\mu_n\langle\zeta,e_n\rangle=\langle\zeta,x^*xe_n\rangle=\langle x^*x\zeta,e_n\rangle=0\) for all \(n\). Conversely, if \(\zeta\perp e_n\) for all \(n\), then \(x^*x\zeta=0\) and \(\|x\zeta\|^2=\langle x^*x\zeta,\zeta\rangle=0\). So the kernel of \(x\) is \(\{e_n\}^\perp\).

Put \(s_n=\mu_n^{1/2}\) and \(f_n=s_n^{-1}xe_n\). Then \(\langle f_n,f_m\rangle=(s_ns_m)^{-1}\langle x^*xe_n,e_m\rangle=\delta_{nm}\), so \((f_n)\) is orthonormal. Every \(\zeta\in H\) is \(\zeta=\sum_n\langle\zeta,e_n\rangle e_n+\zeta_0\) with \(\zeta_0\) in the kernel of \(x\), so \(x\zeta=\sum_n\langle\zeta,e_n\rangle xe_n=\sum_ns_n\langle\zeta,e_n\rangle f_n\). When \(N=\mathbb N\), the remainder \(\zeta\mapsto\sum_{n>M}s_n\langle\zeta,e_n\rangle f_n\) has norm at most \(s_{M+1}\), because \[
\begin{gathered}
\|\sum_{n>M}s_n\langle\zeta,e_n\rangle f_n\|^2\\
=\sum_{n>M}s_n^2|\langle\zeta,e_n\rangle|^2\\
\le s_{M+1}^2\|\zeta\|^2.
\end{gathered}
\] So (2.1) converges in norm.

*Properties.* Now let (2.1) be any decomposition of the stated form.

(a) \(\|x\zeta\|^2=\sum_ns_n^2|\langle\zeta,e_n\rangle|^2\le s_1^2\|\zeta\|^2\), with equality for \(\zeta=e_1\). The same formula shows that \(x\zeta=0\) exactly when \(\zeta\perp e_n\) for all \(n\). Clearly \(xe_n=s_nf_n\), and \(x^*f_n=s_ne_n\) follows from (b).

(b) Taking adjoints term by term, which is allowed since the series converges in norm, gives \(x^*=\sum s_n\theta_{e_n,f_n}\). By Lemma 1.4(b), \(\theta_{e_n,f_n}\theta_{f_m,e_m}=\delta_{nm}\theta_{e_n,e_m}\), so \(x^*x=\sum_ns_n^2\theta_{e_n,e_n}\). The operator \(\sum_ns_n\theta_{e_n,e_n}\) is positive and its square is \(x^*x\) by the same computation. By uniqueness of positive square roots it equals \(|x|\). In the same way \(xx^*=\sum s_n^2\theta_{f_n,f_n}\) and \(|x^*|=\sum s_n\theta_{f_n,f_n}\).

(c) By (b), \(|x|\zeta=\sum_ns_n\langle\zeta,e_n\rangle e_n\), so \(|x|e_n=s_ne_n\). If \(|x|\zeta=\mu\zeta\) with \(\mu\ne0\), then \(\zeta=\mu^{-1}|x|\zeta\) lies in the closed span of the \(e_n\), and \((s_n-\mu)\langle\zeta,e_n\rangle=0\) for every \(n\). So the eigenspace of \(\mu\) is spanned by the \(e_n\) with \(s_n=\mu\), and the nonzero eigenvalues of \(|x|\), counted with multiplicity, are the \(s_n\) listed with repetitions.

(d) \(\|v\zeta\|^2=\sum_n|\langle\zeta,f_n\rangle|^2\le\|\zeta\|^2\). For every \(\zeta\), \[
\begin{gathered}
vx\zeta\\
=\sum_ns_n\langle\zeta,e_n\rangle vf_n\\
=\sum_ns_n\langle\zeta,e_n\rangle e_n\\
=|x|\zeta.
\end{gathered}
\] The adjoint is \(v^*\zeta=\sum_n\langle\zeta,e_n\rangle f_n\), so \(v^*|x|\zeta=\sum_ns_n\langle\zeta,e_n\rangle f_n=x\zeta\).

(e) If \(x\) is self-adjoint, Background 2(b) gives \(x=\sum\lambda_n\theta_{e_n,e_n}\) with \(|\lambda_n|\) decreasing; put \(s_n=|\lambda_n|\) and \(f_n=(\operatorname{sign}\lambda_n)\,e_n\). If \(x\ge0\), all \(\lambda_n>0\).

(f) Each \(\lambda_n\) is an eigenvalue, since \(xe_n=\lambda_ne_n\). Let \(\mu\notin\{\lambda_n:n\in N\}\cup\{0\}\). This set is closed, because \(\lambda_n\to0\) when \(N=\mathbb N\), so \(d=\inf_n|\lambda_n-\mu|>0\). Let \(p\) be the projection onto the closed span of the \(e_n\); its complement \(1-p\) projects onto the kernel of \(x\). The operator \(r\zeta=\sum_n(\lambda_n-\mu)^{-1}\langle\zeta,e_n\rangle e_n-\mu^{-1}(1-p)\zeta\) is bounded, with \(\|r\|\le\max(d^{-1},|\mu|^{-1})\), and one checks on each \(e_n\) and on the kernel of \(x\) that \(r(x-\mu)=(x-\mu)r=1\). So \(\mu\notin\sigma(x)\). If \(H\) is infinite-dimensional and \(0\notin\sigma(x)\), then \(1=x^{-1}x\) would be compact, which contradicts Lemma 2.1 applied to any orthonormal sequence. \(\square\)

Part (d) is the polar decomposition of a compact operator, written out explicitly. The general polar decomposition of bounded operators is not needed in this lesson.

**Definition 2.4.** The *singular values* of \(x\in K(H)\) are the numbers \(s_n(x)=s_n\), \(n\in N\), of any decomposition (2.1), followed by \(s_n(x)=0\) for \(n>r\) when \(N=\{1,\dots,r\}\). For \(x=0\) all \(s_n(x)=0\). We write \(s(x)=(s_n(x))_{n\ge1}\); it is a decreasing sequence in \(c_0\).

**Proposition 2.5** (approximation numbers). For \(x\in K(H)\) and \(n\ge1\),
\[
\begin{gathered}
s_n(x)\\
=\min\{\|x-f\|:\\
\ f\in F(H),\ \operatorname{rank}f<n\}.
\end{gathered}
\tag{2.2}
\]
Consequently, for \(x,y\in K(H)\), \(a,b\in B(H)\) and \(m,n\ge1\):

(a) \(s_n(axb)\le\|a\|\,s_n(x)\,\|b\|\);

(b) \(s_{m+n-1}(x+y)\le s_m(x)+s_n(y)\);

(c) \(s_n(x^*)=s_n(|x|)=s_n(x)\);

(d) \(|s_n(x)-s_n(y)|\le\|x-y\|\).

**Proof.** We may assume \(x\ne0\) and use (2.1). The operator \(x_{n-1}=\sum_{k<n}s_k\theta_{f_k,e_k}\) has rank less than \(n\), and \(x-x_{n-1}=\sum_{k\ge n}s_k\theta_{f_k,e_k}\) has norm \(s_n(x)\) by Theorem 2.3(a) (or is \(0\) if \(n>r\)). Conversely, let \(f\in F(H)\) with \(\operatorname{rank}f<n\). If \(s_n(x)=0\) there is nothing to prove. Otherwise \(e_1,\dots,e_n\) exist, and \(f\) restricted to their \(n\)-dimensional span has a nonzero kernel, since its range has dimension less than \(n\). Take a unit vector \(\zeta=\sum_{k\le n}c_ke_k\) with \(f\zeta=0\). Then \(\|(x-f)\zeta\|^2=\|x\zeta\|^2=\sum_{k\le n}s_k^2|c_k|^2\ge s_n^2\). This proves (2.2).

(a) \(axb\) is compact; if \(\operatorname{rank}f<n\) then \(\operatorname{rank}(afb)<n\), and \(\|axb-afb\|\le\|a\|\,\|x-f\|\,\|b\|\). Take the minimum over \(f\).

(b) If \(\operatorname{rank}f<m\) and \(\operatorname{rank}g<n\), then \(\operatorname{rank}(f+g)\le m+n-2<m+n-1\) and \(\|x+y-f-g\|\le\|x-f\|+\|y-g\|\).

(c) By Theorem 2.3(b), \(x^*\) and \(|x|\) have decompositions (2.1) with the same numbers \(s_n\).

(d) \(\|x-f\|\le\|x-y\|+\|y-f\|\) for every \(f\), and symmetrically. \(\square\)

**Example 2.6.** For \(\lambda\in c_0(I)\), the diagonal operator \(d_\lambda\) of Example 2.2 satisfies \(|d_\lambda|=d_{|\lambda|}=\sum_i|\lambda_i|\theta_{\varepsilon_i,\varepsilon_i}\). By Theorem 2.3(c), \(s(d_\lambda)\) lists the nonzero numbers \(|\lambda_i|\) in decreasing order, with repetitions, followed by zeros. Only countably many \(\lambda_i\) are nonzero because \(\lambda\in c_0(I)\).

## 3. Hilbert–Schmidt operators

An operator is Hilbert–Schmidt when the squares of its matrix entries are summable. These operators form a Hilbert space, and on a space of square-integrable functions they are exactly the integral operators with square-integrable kernels.

**Lemma 3.1.** Let \(x\in B(H)\), and let \((\varepsilon_i)_{i\in I}\) and \((\varepsilon'_j)_{j\in J}\) be orthonormal bases. Then, in \([0,\infty]\),
\[
\begin{gathered}
\sum_i\|x\varepsilon_i\|^2\\
=\sum_{i,j}|\langle x\varepsilon_i,\varepsilon'_j\rangle|^2\\
=\sum_j\|x^*\varepsilon'_j\|^2 .
\end{gathered}
\tag{3.1}
\]
In particular \(\sum_i\|x\varepsilon_i\|^2\) does not depend on the basis, and it does not change when \(x\) is replaced by \(x^*\).

**Proof.** By Parseval, \(\|x\varepsilon_i\|^2=\sum_j|\langle x\varepsilon_i,\varepsilon'_j\rangle|^2\), and since \(\langle x\varepsilon_i,\varepsilon'_j\rangle=\langle\varepsilon_i,x^*\varepsilon'_j\rangle\), also \(\sum_i|\langle x\varepsilon_i,\varepsilon'_j\rangle|^2=\|x^*\varepsilon'_j\|^2\). A double sum of nonnegative terms may be computed in either order. The right side of (3.1) involves only \((\varepsilon'_j)\); applying (3.1) with a third basis in place of \((\varepsilon_i)\) shows that the left side is the same for all bases. \(\square\)

**Definition 3.2.** The *Hilbert–Schmidt norm* of \(x\in B(H)\) is \(\|x\|_2=(\sum_i\|x\varepsilon_i\|^2)^{1/2}\in[0,\infty]\) for any orthonormal basis \((\varepsilon_i)\). The operators with \(\|x\|_2<\infty\) are the *Hilbert–Schmidt operators*; they form the set \(\mathcal L^2(H)\).

**Theorem 3.3.**

(a) \(\|x\|\le\|x\|_2=\|x^*\|_2\) and \(\|axb\|_2\le\|a\|\,\|x\|_2\,\|b\|\) for \(a,b\in B(H)\). So \(\mathcal L^2(H)\) is a two-sided ideal of \(B(H)\), closed under adjoints.

(b) \(\mathcal L^2(H)\subseteq K(H)\). A compact operator \(x\) is Hilbert–Schmidt if and only if \(\sum_ns_n(x)^2<\infty\), and then \(\|x\|_2^2=\sum_ns_n(x)^2\).

(c) For \(x,y\in\mathcal L^2(H)\), the sum \(\langle x,y\rangle_2=\sum_i\langle x\varepsilon_i,y\varepsilon_i\rangle\) converges absolutely and does not depend on the basis. With this inner product \(\mathcal L^2(H)\) is a Hilbert space with norm \(\|\cdot\|_2\), and \(F(H)\) is dense in it.

(d) \(\|\theta_{\xi,\eta}\|_2=\|\xi\|\,\|\eta\|\), and \(\langle\theta_{\xi,\eta},\theta_{\xi',\eta'}\rangle_2=\langle\xi,\xi'\rangle\langle\eta',\eta\rangle\).

**Proof.** (a) For a unit vector \(\zeta\), choose an orthonormal basis containing \(\zeta\); then \(\|x\zeta\|^2\le\sum_i\|x\varepsilon_i\|^2\). The equality \(\|x^*\|_2=\|x\|_2\) is Lemma 3.1. Since \(\|ax\varepsilon_i\|\le\|a\|\,\|x\varepsilon_i\|\), \(\|ax\|_2\le\|a\|\,\|x\|_2\); then \(\|xb\|_2=\|b^*x^*\|_2\le\|b\|\,\|x\|_2\). Minkowski's inequality in \(\ell^2(I)\) gives \(\|x+y\|_2\le\|x\|_2+\|y\|_2\).

(b) Let \(x\in\mathcal L^2(H)\) and \(\varepsilon>0\). Choose a finite \(F\subseteq I\) with \(\sum_{i\notin F}\|x\varepsilon_i\|^2<\varepsilon^2\), and let \(p_F\) be the projection onto the span of \(\{\varepsilon_i:i\in F\}\). Then \(xp_F\) has finite rank and, by (a) and the choice of the basis, \[
\begin{gathered}
\|x-xp_F\|\\
\le\|x-xp_F\|_2\\
=(\sum_{i\notin F}\|x\varepsilon_i\|^2)^{1/2}<\varepsilon.
\end{gathered}
\] So \(x\) is a norm limit of finite-rank operators, hence compact, and \(F(H)\) is dense in \(\mathcal L^2(H)\) for \(\|\cdot\|_2\). For a compact \(x\) with decomposition (2.1), choose an orthonormal basis consisting of the \(e_n\) and a basis of the kernel of \(x\). Then \(\|x\|_2^2=\sum_n\|xe_n\|^2=\sum_ns_n^2\).

(c) \(|\langle x\varepsilon_i,y\varepsilon_i\rangle|\le\frac12(\|x\varepsilon_i\|^2+\|y\varepsilon_i\|^2)\) gives absolute convergence. The form \(\langle\cdot,\cdot\rangle_2\) is sesquilinear, and \(\langle x,x\rangle_2=\|x\|_2^2\). By the polarization identity (1.1) it is determined by \(\|\cdot\|_2\), which does not depend on the basis; and \(\|x\|_2=0\) forces \(x=0\) by (a). For completeness, let \((x_k)\) be Cauchy for \(\|\cdot\|_2\). By (a) it is Cauchy in norm, so \(x_k\to x\) in norm for some \(x\in B(H)\). For finite \(F\subseteq I\),
\[
\begin{gathered}
\sum_{i\in F}\|(x-x_k)\varepsilon_i\|^2\\
=\lim_m\sum_{i\in F}\|(x_m-x_k)\varepsilon_i\|^2\\
\le\sup_{m\ge k}\|x_m-x_k\|_2^2 .
\end{gathered}
\]
Taking the supremum over \(F\) gives \(\|x-x_k\|_2\le\sup_{m\ge k}\|x_m-x_k\|_2\to0\). So \(x\in\mathcal L^2(H)\) and \(x_k\to x\) in \(\|\cdot\|_2\). Density of \(F(H)\) was shown in (b).

(d) \(\theta_{\xi,\eta}\varepsilon_i=\langle\varepsilon_i,\eta\rangle\xi\), so \(\|\theta_{\xi,\eta}\|_2^2=\sum_i|\langle\varepsilon_i,\eta\rangle|^2\|\xi\|^2=\|\eta\|^2\|\xi\|^2\), and \[
\begin{gathered}
\langle\theta_{\xi,\eta},\theta_{\xi',\eta'}\rangle_2\\
=\sum_i\langle\varepsilon_i,\eta\rangle\overline{\langle\varepsilon_i,\eta'\rangle}\langle\xi,\xi'\rangle\\
=\langle\xi,\xi'\rangle\langle\eta',\eta\rangle
\end{gathered}
\] by Parseval. \(\square\)

**Example 3.4** (Hilbert–Schmidt operators as integral operators). Let \((X,\mu)\) be a \(\sigma\)-finite measure space and \(H=L^2(X,\mu)\). For \(k\in L^2(X\times X,\mu\otimes\mu)\) define
\[
(x_kf)(s)=\int_Xk(s,t)f(t)\,d\mu(t).
\]
Then \(x_k\in\mathcal L^2(H)\), \(\|x_k\|_2=\|k\|_{L^2}\), and \(k\mapsto x_k\) is a unitary operator of \(L^2(X\times X,\mu\otimes\mu)\) onto \(\mathcal L^2(H)\). So the Hilbert–Schmidt operators on \(L^2(X,\mu)\) are exactly the integral operators with square-integrable kernels.

*Proof.* By Tonelli's theorem \(\int\!\!\int|k(s,t)|^2d\mu(t)\,d\mu(s)=\|k\|^2<\infty\), so \(k(s,\cdot)\in L^2(X,\mu)\) for almost every \(s\). For such \(s\) the integral defining \((x_kf)(s)\) converges absolutely, and \(|(x_kf)(s)|\le\|k(s,\cdot)\|\,\|f\|\) by Cauchy–Schwarz. If \(A\subseteq X\) has finite measure, then \[
\begin{gathered}
\int_A\int|k(s,t)f(t)|\,d\mu(t)\,d\mu(s)\\
\le\mu(A)^{1/2}\|k\|\,\|f\|<\infty,
\end{gathered}
\] so Fubini's theorem shows that \(x_kf\) is measurable on \(A\); as \(X\) is a countable union of such sets, \(x_kf\) is measurable. Then \(\|x_kf\|^2\le\|k\|^2\|f\|^2\). So \(x_k\in B(H)\), \(\|x_k\|\le\|k\|\), and \(k\mapsto x_k\) is linear.

For a product kernel \(k(s,t)=\varphi(s)\overline{\psi(t)}\) with \(\varphi,\psi\in L^2(X,\mu)\) we get \(x_k=\theta_{\varphi,\psi}\). By Theorem 3.3(d),
\[
\begin{gathered}
\langle\theta_{\varphi,\psi},\theta_{\varphi',\psi'}\rangle_2\\
=\langle\varphi,\varphi'\rangle\langle\psi',\psi\rangle\\
=\langle\varphi\otimes\bar\psi,\ \varphi'\otimes\bar\psi'\rangle_{L^2(X\times X)} .
\end{gathered}
\]
So \(k\mapsto x_k\) is isometric from the span \(P\) of the product kernels into \(\mathcal L^2(H)\). The span \(P\) is dense in \(L^2(X\times X)\). Indeed, if \(g\in L^2(X\times X)\) is orthogonal to \(P\), let \(X=\bigcup_nA_n\) with \(A_n\) increasing of finite measure. The finite signed measures \(E\mapsto\int_E\operatorname{Re}g\) and \(E\mapsto\int_E\operatorname{Im}g\) on \(A_n\times A_n\) vanish on the rectangles \(A\times B\subseteq A_n\times A_n\), which form a family closed under intersections that generates the product \(\sigma\)-algebra; by Dynkin's lemma they vanish identically, so \(g=0\) almost everywhere on each \(A_n\times A_n\), and hence almost everywhere on \(X\times X\).

Consequently \(k\mapsto x_k\) extends from \(P\) to an isometry \(U\) of \(L^2(X\times X)\) into \(\mathcal L^2(H)\). If \(k_n\in P\) and \(k_n\to k\) in \(L^2\), then \(x_{k_n}\to x_k\) in operator norm (since \(\|x_k-x_{k_n}\|\le\|k-k_n\|\)), and \(x_{k_n}\to Uk\) in \(\|\cdot\|_2\), hence in operator norm. So \(Uk=x_k\). The range of \(U\) is closed and contains every \(\theta_{\varphi,\psi}\), hence \(F(H)\), which is dense in \(\mathcal L^2(H)\) by Theorem 3.3(c). So \(U\) is onto. \(\square\)

**Example 3.5** (an operator that is Hilbert–Schmidt but not of trace class). On \(H=L^2(0,1)\) let \((Vf)(s)=\int_0^sf(t)\,dt\), the integral operator with kernel \(k(s,t)=1\) for \(t<s\) and \(0\) otherwise. By Example 3.4, \(V\in\mathcal L^2(H)\) and \(\|V\|_2^2=\int_0^1\!\int_0^1k^2=\frac12\). We compute its singular values. The adjoint is \((V^*g)(t)=\int_t^1g(s)\,ds\). Let \(\mu>0\) and \(f\ne0\) with \(V^*Vf=\mu f\). The function \(u=Vf\) is continuous with \(u(0)=0\): Cauchy–Schwarz gives \(|u(t)-u(s)|\leq|t-s|^{1/2}\|f\|_2\). The continuous-integrand fundamental theorem in [Lemma 0.1 of the Cauchy lesson](cauchy-s-theorem-for-cycles-and-its-consequences.md#oa-fnd-ct-07) justifies the derivatives below. Then \(\mu f=V^*u\) is continuous, so \(u\) is continuously differentiable with \(u'=f\). Next \(\mu f=V^*u\) is continuously differentiable with \((\mu f)'=-u\) and \(\mu f(1)=0\). Thus \(\mu u''=-u\), \(u(0)=0\) and \(u'(1)=0\). Put \(a=\mu^{-1/2}\). The general solution of \(u''+a^2u=0\) is \(A\cos(at)+B\sin(at)\). To verify completeness of this list, choose \(A=u(0)\), \(B=u'(0)/a\), and subtract that solution. The difference \(w\) has \(w(0)=w'(0)=0\); differentiating \(|w'|^2+a^2|w|^2\) gives zero, so \(w=0\). Thus the boundary conditions leave precisely the multiples of \(\sin(t/\sqrt\mu)\) with \(\cos(1/\sqrt\mu)=0\). So the nonzero eigenvalues of \(V^*V\) are \(\mu_n=((n-\frac12)\pi)^{-2}\), \(n\ge1\), each with a one-dimensional eigenspace spanned by \(\cos((n-\frac12)\pi t)\). One checks directly that these functions are eigenvectors. By Theorem 2.3(c),
\[
s_n(V)=\frac{1}{(n-\frac12)\pi},\qquad n\ge1 .
\]
Theorem 3.3(b) and the independently computed kernel norm now give \(\frac4{\pi^2}\sum_n(2n-1)^{-2}=\sum_ns_n(V)^2=\|V\|_2^2=\frac12\). In particular this calculation proves \(\sum_n(2n-1)^{-2}=\pi^2/8\), rather than assuming that sum. But \(\sum_ns_n(V)=\infty\), so \(V\) is not of trace class (Theorem 4.3 below).

## 4. Trace-class operators and the trace

An operator is of trace class when its matrix entries along pairs of orthonormal families have uniformly bounded absolute sums. For a compact operator this is the summability of its singular values. The trace is defined on these operators and has the properties of the trace of a matrix.

**Definition 4.1.** For \(x\in B(H)\) let
\[
\begin{gathered}
\|x\|_1\\
=\sup\Big\{\sum_{j\in J}|\langle x\xi_j,\eta_j\rangle|\Big\}\in[0,\infty],
\end{gathered}
\tag{4.1}
\]
the supremum over all finite sets \(J\) and all orthonormal families \((\xi_j)_{j\in J}\) and \((\eta_j)_{j\in J}\) in \(H\). The operators with \(\|x\|_1<\infty\) are the *trace-class* (or *nuclear*) operators; they form the set \(\mathcal L^1(H)\). Since the terms are nonnegative, the supremum does not change if infinite index sets \(J\) are allowed.

**Lemma 4.2.**

(a) \(\mathcal L^1(H)\) is a linear subspace of \(B(H)\), \(\|\cdot\|_1\) is a norm on it, \(\|x\|\le\|x\|_1\), and \(\|x^*\|_1=\|x\|_1\).

(b) \(\|\theta_{\xi,\eta}\|_1=\|\xi\|\,\|\eta\|\).

(c) If \((x_\alpha)\) is a net with \(\langle x_\alpha\xi,\eta\rangle\to\langle x\xi,\eta\rangle\) for all \(\xi,\eta\), then \(\|x\|_1\le\liminf_\alpha\|x_\alpha\|_1\).

(d) \((\mathcal L^1(H),\|\cdot\|_1)\) is a Banach space.

**Proof.** (a) The inequalities \(\|x+y\|_1\le\|x\|_1+\|y\|_1\) and \(\|cx\|_1=|c|\,\|x\|_1\) hold term by term. With one pair of unit vectors, \(|\langle x\xi,\eta\rangle|\le\|x\|_1\); the supremum over \(\xi,\eta\) is \(\|x\|\). Since \(|\langle x^*\xi_j,\eta_j\rangle|=|\langle x\eta_j,\xi_j\rangle|\), passing to \(x^*\) exchanges the two families.

(b) By Cauchy–Schwarz and Bessel's inequality,
\[
\begin{gathered}
\sum_j|\langle\theta_{\xi,\eta}\xi_j,\eta_j\rangle|\\
=\sum_j|\langle\xi_j,\eta\rangle|\,|\langle\xi,\eta_j\rangle|\\
\le\Big(\sum_j|\langle\xi_j,\eta\rangle|^2\Big)^{1/2}\Big(\sum_j|\langle\eta_j,\xi\rangle|^2\Big)^{1/2}\\
\le\|\eta\|\,\|\xi\| .
\end{gathered}
\]
If \(\xi,\eta\ne0\), the single pair \(\xi_1=\eta/\|\eta\|\), \(\eta_1=\xi/\|\xi\|\) gives equality.

(c) For fixed finite families, \[
\begin{gathered}
\sum_j|\langle x\xi_j,\eta_j\rangle|\\
=\lim_\alpha\sum_j|\langle x_\alpha\xi_j,\eta_j\rangle|\\
\le\liminf_\alpha\|x_\alpha\|_1.
\end{gathered}
\]

(d) Let \((x_k)\) be Cauchy for \(\|\cdot\|_1\). By (a) it is Cauchy in norm, so \(x_k\to x\) in norm. For fixed \(k\), apply (c) to the sequence \((x_m-x_k)_m\), which converges in norm to \(x-x_k\): \(\|x-x_k\|_1\le\sup_{m\ge k}\|x_m-x_k\|_1\), which tends to \(0\). So \(x=(x-x_k)+x_k\in\mathcal L^1(H)\) and \(x_k\to x\) in \(\|\cdot\|_1\). \(\square\)

**Theorem 4.3.**

(a) \(\|x\|_2^2\le\|x\|\,\|x\|_1\) for every \(x\in B(H)\). Hence \(\mathcal L^1(H)\subseteq\mathcal L^2(H)\subseteq K(H)\).

(b) For \(x\in K(H)\), \(\|x\|_1=\sum_ns_n(x)\) in \([0,\infty]\). So \(x\in\mathcal L^1(H)\) if and only if \(x\) is compact and \(\sum_ns_n(x)<\infty\).

(c) If \(x\in\mathcal L^1(H)\), every decomposition (2.1) of \(x\) converges in \(\|\cdot\|_1\).

**Proof.** (a) We may assume \(\|x\|_1<\infty\). Let \(\xi_1,\dots,\xi_m\) be orthonormal, let \(L\) be their span and \(p\) the projection onto \(L\). The operator \(px^*xp\) is positive and maps \(L\) into \(L\), so \(L\) has an orthonormal basis \(\zeta_1,\dots,\zeta_m\) with \(px^*xp\,\zeta_k=\sigma_k^2\zeta_k\), \(\sigma_k\ge0\). Then \(\langle x\zeta_k,x\zeta_l\rangle=\langle px^*xp\,\zeta_k,\zeta_l\rangle=\sigma_k^2\delta_{kl}\): the vectors \(x\zeta_k\) are orthogonal, with norms \(\sigma_k\). Choose orthonormal \(\eta_1,\dots,\eta_m\) with \(x\zeta_k=\sigma_k\eta_k\): put \(\eta_k=\sigma_k^{-1}x\zeta_k\) when \(\sigma_k>0\), and complete by further orthonormal vectors, which is possible since \(\dim H\ge m\). Then
\[
\sum_k\sigma_k=\sum_k\langle x\zeta_k,\eta_k\rangle\le\|x\|_1 .
\]
Apply Lemma 3.1 to \(xp\) and to the two orthonormal bases of \(H\) obtained by completing \((\xi_i)\) and \((\zeta_k)\) with one and the same orthonormal basis of \(L^\perp\), on which \(xp\) vanishes. This gives \(\sum_i\|x\xi_i\|^2=\sum_k\|x\zeta_k\|^2=\sum_k\sigma_k^2\). Since \(\sigma_k\le\|x\|\),
\[
\sum_{i\le m}\|x\xi_i\|^2=\sum_k\sigma_k^2\le\|x\|\sum_k\sigma_k\le\|x\|\,\|x\|_1 .
\]
Every finite subfamily of an orthonormal basis is such a family, so \(\|x\|_2^2\le\|x\|\,\|x\|_1\). The inclusion \(\mathcal L^2(H)\subseteq K(H)\) is Theorem 3.3(b).

(b) Let \(x\in K(H)\), \(x\ne0\), with decomposition (2.1), and let \((\xi_j)\), \((\eta_j)\) be finite orthonormal families. Since \(\langle x\xi_j,\eta_j\rangle=\sum_ns_n\langle\xi_j,e_n\rangle\langle f_n,\eta_j\rangle\),
\[
\begin{gathered}
\sum_j|\langle x\xi_j,\eta_j\rangle|\\
\le\sum_ns_n\sum_j|\langle\xi_j,e_n\rangle|\,|\langle f_n,\eta_j\rangle|\\
\le\sum_ns_n\Big(\sum_j|\langle e_n,\xi_j\rangle|^2\Big)^{1/2}\\
{}\cdot\Big(\sum_j|\langle f_n,\eta_j\rangle|^2\Big)^{1/2}\\
\le\sum_ns_n
\end{gathered}
\]
by Cauchy–Schwarz and Bessel's inequality. So \(\|x\|_1\le\sum_ns_n\). Conversely, the families \(\xi_j=e_j\), \(\eta_j=f_j\), \(j\le M\), give \(\sum_{j\le M}\langle xe_j,f_j\rangle=\sum_{j\le M}s_j\), so \(\|x\|_1\ge\sum_{j\le M}s_j\) for every \(M\). Together with (a), which shows that a trace-class operator is compact, this proves (b).

(c) The remainder \(\sum_{n>M}s_n\theta_{f_n,e_n}\) is compact and has a decomposition of the form (2.1) with the numbers \(s_{M+1},s_{M+2},\dots\). By (b) its trace norm is \(\sum_{n>M}s_n\), which tends to \(0\). \(\square\)

**Corollary 4.4.**

(a) If \(x\in\mathcal L^1(H)\) and \(a,b\in B(H)\), then \(axb\in\mathcal L^1(H)\) and \(\|axb\|_1\le\|a\|\,\|x\|_1\,\|b\|\). So \(\mathcal L^1(H)\) is a two-sided ideal of \(B(H)\), closed under adjoints.

(b) \(x\in\mathcal L^1(H)\) if and only if \(|x|\in\mathcal L^1(H)\), if and only if \(x^*\in\mathcal L^1(H)\), and \(\|x\|_1=\||x|\|_1=\|x^*\|_1\).

(c) \(F(H)\subseteq\mathcal L^1(H)\), and \(F(H)\) is dense in \(\mathcal L^1(H)\) for \(\|\cdot\|_1\). For \(x\in\mathcal L^1(H)\), \(\|x\|\le\|x\|_2\le\|x\|_1\).

(d) If \(\sum_n\|\xi_n\|\,\|\eta_n\|<\infty\), the series \(\sum_n\theta_{\xi_n,\eta_n}\) converges in \(\|\cdot\|_1\), and its sum \(t\) satisfies \(\|t\|_1\le\sum_n\|\xi_n\|\,\|\eta_n\|\).

**Proof.** (a) follows from Proposition 2.5(a) and Theorem 4.3(b). (b) By Lemma 4.2(a), \(x^*\in\mathcal L^1(H)\) exactly when \(x\in\mathcal L^1(H)\), and \(\|x^*\|_1=\|x\|_1\). If \(x\in\mathcal L^1(H)\), then \(x\) is compact by Theorem 4.3(a). If \(|x|\in\mathcal L^1(H)\), then \(x\) is compact too: \(\|x\zeta\|^2=\langle x^*x\zeta,\zeta\rangle=\||x|\zeta\|^2\) for every \(\zeta\), so \(\|x\|_2=\||x|\|_2\), which is finite by Theorem 4.3(a), and \(\mathcal L^2(H)\subseteq K(H)\) by Theorem 3.3(b). For compact \(x\), Proposition 2.5(c) and Theorem 4.3(b) give \(\|x\|_1=\||x|\|_1\) in \([0,\infty]\). (c) A finite-rank operator has only finitely many nonzero singular values. Density follows from Theorem 4.3(c). For \(x\in\mathcal L^1(H)\), \(\|x\|_2^2=\sum s_n^2\le(\sum s_n)^2\). (d) By Lemma 4.2(b) the series converges absolutely in the Banach space \(\mathcal L^1(H)\). \(\square\)

**Example 4.5** (three different norms). Let \(\xi\perp\eta\) be unit vectors and \(x=\theta_{\xi,\eta}+\theta_{\eta,\xi}\). Then \(x(\xi\pm\eta)=\pm(\xi\pm\eta)\) and \(x\) vanishes on \(\{\xi,\eta\}^\perp\). So \(x\) is self-adjoint with eigenvalues \(\pm1\), and \(s(x)=(1,1,0,0,\dots)\). Hence \(\|x\|=1\), \(\|x\|_2=\sqrt2\), \(\|x\|_1=2\), and \(\operatorname{Tr}(x)=0\) (Theorem 4.6). For the diagonal operators of Example 2.2, Example 2.6 shows that \(d_\lambda\in\mathcal L^2(H)\) exactly when \(\lambda\in\ell^2(I)\) and \(d_\lambda\in\mathcal L^1(H)\) exactly when \(\lambda\in\ell^1(I)\), with \(\|d_\lambda\|_2=\|\lambda\|_2\) and \(\|d_\lambda\|_1=\|\lambda\|_1\). The Volterra operator of Example 3.5 lies in \(\mathcal L^2(H)\) but not in \(\mathcal L^1(H)\).

**Theorem 4.6** (the trace). Let \(x\in\mathcal L^1(H)\) and let \((\varepsilon_i)_{i\in I}\) be an orthonormal basis. Then \(\sum_i\langle x\varepsilon_i,\varepsilon_i\rangle\) converges absolutely, \(\sum_i|\langle x\varepsilon_i,\varepsilon_i\rangle|\le\|x\|_1\), and the sum, denoted \(\operatorname{Tr}(x)\), does not depend on the basis. More precisely, if \(x=\sum_n\theta_{\xi_n,\eta_n}\) with \(\sum_n\|\xi_n\|\,\|\eta_n\|<\infty\), as in (2.1), then
\[
\operatorname{Tr}(x)=\sum_n\langle\xi_n,\eta_n\rangle .
\tag{4.2}
\]
The trace is a linear functional on \(\mathcal L^1(H)\) with \(|\operatorname{Tr}(x)|\le\|x\|_1\), \(\operatorname{Tr}(x^*)=\overline{\operatorname{Tr}(x)}\), \(\operatorname{Tr}(x)\ge0\) for \(x\ge0\), and \(\operatorname{Tr}(\theta_{\xi,\eta})=\langle\xi,\eta\rangle\). For \(a\in B(H)\),
\[
\begin{gathered}
\operatorname{Tr}(ax)\\
=\operatorname{Tr}(xa),\\
|\operatorname{Tr}(ax)|\\
\le\|a\|\,\|x\|_1,
\end{gathered}
\tag{4.3}
\]
and in particular
\[
\operatorname{Tr}(a\,\theta_{\xi,\eta})=\langle a\xi,\eta\rangle=\omega_{\xi,\eta}(a).
\tag{4.4}
\]
Finally \(\|x\|_1=\operatorname{Tr}(|x|)\).

**Proof.** Taking \(\xi_j=\eta_j=\varepsilon_j\) over finite subsets in (4.1) gives absolute convergence and the bound. Let \(x=\sum_n\theta_{\xi_n,\eta_n}\) with \(\sum\|\xi_n\|\,\|\eta_n\|<\infty\); the series converges in \(\|\cdot\|_1\) by Corollary 4.4(d), hence in norm. Then \(\langle x\varepsilon_i,\varepsilon_i\rangle=\sum_n\langle\varepsilon_i,\eta_n\rangle\langle\xi_n,\varepsilon_i\rangle\). The double family is absolutely summable:
\[
\begin{gathered}
\sum_n\sum_i|\langle\varepsilon_i,\eta_n\rangle|\,|\langle\xi_n,\varepsilon_i\rangle|\\
\le\sum_n\|\eta_n\|\,\|\xi_n\|<\infty,
\end{gathered}
\]
by Cauchy–Schwarz and Parseval in \(i\). So we may sum over \(i\) first: \[
\begin{gathered}
\sum_i\langle x\varepsilon_i,\varepsilon_i\rangle\\
=\sum_n\sum_i\langle\xi_n,\varepsilon_i\rangle\langle\varepsilon_i,\eta_n\rangle\\
=\sum_n\langle\xi_n,\eta_n\rangle,
\end{gathered}
\] by Parseval. The right side does not involve the basis. Every trace-class operator has such a representation, namely (2.1) with \(\xi_n=s_nf_n\), \(\eta_n=e_n\).

Linearity is clear for a fixed basis. \(\operatorname{Tr}(x^*)=\sum_i\langle x^*\varepsilon_i,\varepsilon_i\rangle=\sum_i\overline{\langle x\varepsilon_i,\varepsilon_i\rangle}\), positivity is termwise, and \(\operatorname{Tr}(\theta_{\xi,\eta})=\langle\xi,\eta\rangle\) is (4.2). For (4.3), write \(x=\sum_ns_n\theta_{f_n,e_n}\) as in (2.1). By Lemma 1.4(b), \(ax=\sum_ns_n\theta_{af_n,e_n}\) and \(xa=\sum_ns_n\theta_{f_n,a^*e_n}\), both with \(\sum_ns_n\|a\|<\infty\). By (4.2), \[
\begin{gathered}
\operatorname{Tr}(ax)\\
=\sum_ns_n\langle af_n,e_n\rangle\\
=\sum_ns_n\langle f_n,a^*e_n\rangle\\
=\operatorname{Tr}(xa).
\end{gathered}
\] The bound follows from \(|\operatorname{Tr}(ax)|\le\|ax\|_1\) and Corollary 4.4(a). Formula (4.4) is (4.2) for \(a\theta_{\xi,\eta}=\theta_{a\xi,\eta}\). Finally \(|x|=\sum s_n\theta_{e_n,e_n}\) by Theorem 2.3(b), so \(\operatorname{Tr}(|x|)=\sum s_n=\|x\|_1\). \(\square\)

**Proposition 4.7** (testing on one basis). Let \(h\in B(H)_+\). The sum \(\sum_i\langle h\varepsilon_i,\varepsilon_i\rangle\in[0,\infty]\) is the same for all orthonormal bases. It is finite if and only if \(h\in\mathcal L^1(H)\), and then it equals \(\operatorname{Tr}(h)=\|h\|_1\). Consequently, an operator \(x\) is of trace class if and only if \(\sum_i\langle|x|\varepsilon_i,\varepsilon_i\rangle<\infty\) for one orthonormal basis; and then \(\operatorname{Tr}(x)=\sum_i\langle x\varepsilon_i,\varepsilon_i\rangle\) for every orthonormal basis, with absolute convergence.

**Proof.** \(\sum_i\langle h\varepsilon_i,\varepsilon_i\rangle=\sum_i\|h^{1/2}\varepsilon_i\|^2=\|h^{1/2}\|_2^2\), which does not depend on the basis (Lemma 3.1). If it is finite, then \(h^{1/2}\in\mathcal L^2(H)\subseteq K(H)\), so \(h=(h^{1/2})^2\) is compact. Write \(h=\sum_ns_n\theta_{e_n,e_n}\) as in Theorem 2.3(e) and complete \((e_n)\) to an orthonormal basis: \(\sum_ns_n=\sum_n\langle he_n,e_n\rangle\le\|h^{1/2}\|_2^2<\infty\). By Theorem 4.3(b), \(h\in\mathcal L^1(H)\), and by Theorem 4.6 the sum over any basis is \(\operatorname{Tr}(h)=\operatorname{Tr}(|h|)=\|h\|_1\). If \(h\in\mathcal L^1(H)\), the sum is \(\operatorname{Tr}(h)<\infty\). The last statement follows from Corollary 4.4(b) and Theorem 4.6. \(\square\)

**Proposition 4.8** (positive parts). Every \(x\in\mathcal L^1(H)\) can be written \(x=h_1-h_2+i(h_3-h_4)\) with positive trace-class operators \(h_1,\dots,h_4\). A self-adjoint \(x\in\mathcal L^1(H)\) can be written \(x=h_1-h_2\) with \(h_1,h_2\ge0\) of trace class and \(\|x\|_1=\operatorname{Tr}(h_1)+\operatorname{Tr}(h_2)\).

**Proof.** The operators \(\operatorname{Re}x=\frac12(x+x^*)\) and \(\operatorname{Im}x=\frac1{2i}(x-x^*)\) are self-adjoint, lie in \(\mathcal L^1(H)\) by Corollary 4.4(b), and \(x=\operatorname{Re}x+i\operatorname{Im}x\). For self-adjoint \(x\in\mathcal L^1(H)\), \(x\ne0\), Theorem 2.3(e) gives \(x=\sum_n\lambda_n\theta_{e_n,e_n}\) with real \(\lambda_n\) and \(\sum|\lambda_n|=\|x\|_1\). Put \(h_1=\sum_{\lambda_n>0}\lambda_n\theta_{e_n,e_n}\) and \(h_2=\sum_{\lambda_n<0}|\lambda_n|\theta_{e_n,e_n}\). \(\square\)

**Proposition 4.9** (products of Hilbert–Schmidt operators).

(a) An operator \(x\) is Hilbert–Schmidt if and only if \(x^*x\) is of trace class, and then \(\operatorname{Tr}(x^*x)=\|x\|_2^2\).

(b) If \(x,y\in\mathcal L^2(H)\), then \(xy\in\mathcal L^1(H)\), \(\|xy\|_1\le\|x\|_2\,\|y\|_2\), and \(\operatorname{Tr}(y^*x)=\langle x,y\rangle_2\).

(c) Every \(t\in\mathcal L^1(H)\) is a product \(t=xy\) of two Hilbert–Schmidt operators, with \(\|x\|_2^2=\|y\|_2^2=\|t\|_1\).

**Proof.** (a) \(\sum_i\langle x^*x\varepsilon_i,\varepsilon_i\rangle=\sum_i\|x\varepsilon_i\|^2\); apply Proposition 4.7 to \(h=x^*x\). (b) For finite orthonormal families, extend each to an orthonormal basis and use Cauchy–Schwarz:
\[
\begin{gathered}
\sum_j|\langle xy\xi_j,\eta_j\rangle|\\
=\sum_j|\langle y\xi_j,x^*\eta_j\rangle|\\
\le\Big(\sum_j\|y\xi_j\|^2\Big)^{1/2}\Big(\sum_j\|x^*\eta_j\|^2\Big)^{1/2}\\
\le\|y\|_2\,\|x^*\|_2\\
=\|x\|_2\,\|y\|_2 .
\end{gathered}
\]
Then \[
\begin{gathered}
\operatorname{Tr}(y^*x)\\
=\sum_i\langle y^*x\varepsilon_i,\varepsilon_i\rangle\\
=\sum_i\langle x\varepsilon_i,y\varepsilon_i\rangle\\
=\langle x,y\rangle_2.
\end{gathered}
\] (c) With (2.1) for \(t\ne0\), put \(x=\sum_ns_n^{1/2}\theta_{f_n,e_n}\) and \(y=\sum_ns_n^{1/2}\theta_{e_n,e_n}\). Both are Hilbert–Schmidt with \(\|x\|_2^2=\|y\|_2^2=\sum s_n\) (Theorem 3.3(b)), and \(xy=\sum_ns_n\theta_{f_n,e_n}=t\) because \(\theta_{f_n,e_n}\theta_{e_m,e_m}=\delta_{nm}\theta_{f_n,e_n}\). \(\square\)

## 5. Duality between compact, trace-class and bounded operators

The model is the chain of sequence spaces \(c_0\), \(\ell^1\), \(\ell^\infty\), each the dual of the one before. Replacing sequences by operators and sums by traces gives the chain \(K(H)\), \(\mathcal L^1(H)\), \(B(H)\). 

**Example 5.1** (the commutative model). Let \(I\) be a set and \(\langle\lambda,\alpha\rangle=\sum_i\lambda_i\alpha_i\) for \(\lambda\in\ell^\infty(I)\), \(\alpha\in\ell^1(I)\).

(a) \(\alpha\mapsto\langle\cdot,\alpha\rangle\) is an isometric isomorphism of \(\ell^1(I)\) onto \(c_0(I)^*\).

(b) \(\lambda\mapsto\langle\lambda,\cdot\rangle\) is an isometric isomorphism of \(\ell^\infty(I)\) onto \(\ell^1(I)^*\).

*Proof.* In both cases \(|\langle\lambda,\alpha\rangle|\le\|\lambda\|_\infty\|\alpha\|_1\). (a) Let \(f\in c_0(I)^*\) and \(\alpha_i=f(\delta_i)\). For a finite \(F\subseteq I\) choose \(c_i\) with \(|c_i|=1\) and \(c_i\alpha_i=|\alpha_i|\); then \(\sum_{i\in F}|\alpha_i|=f(\sum_{i\in F}c_i\delta_i)\le\|f\|\). So \(\alpha\in\ell^1(I)\) with \(\|\alpha\|_1\le\|f\|\). The finite-cutoff vectors are dense in \(c_0(I)\): retaining \(\{i:|\lambda_i|\geq\varepsilon\}\) leaves supremum-norm error at most \(\varepsilon\). Thus the functionals \(f\) and \(\langle\cdot,\alpha\rangle\), agreeing on \(c_{00}(I)\), are equal. The bound \(\|\alpha\|_1\leq\|f\|\) together with the first inequality proves the isometry. (b) Let \(g\in\ell^1(I)^*\) and \(\lambda_i=g(\delta_i)\). Then \(|\lambda_i|\le\|g\|\), and finite cutoffs are dense in \(\ell^1(I)\): a finite partial absolute sum within \(\varepsilon\) of \(\|\alpha\|_1\) leaves tail norm at most \(\varepsilon\). Hence \(g\) and \(\langle\lambda,\cdot\rangle\), agreeing on \(c_{00}(I)\), are equal. Testing on \(\delta_i\) shows \(\|\langle\lambda,\cdot\rangle\|\ge\|\lambda\|_\infty\). \(\square\)

So \(c_0(I)^{**}=\ell^\infty(I)\). Through the diagonal operators of Example 2.2 this model sits inside the operator picture: for \(\lambda\in\ell^\infty(I)\) and \(\alpha\in\ell^1(I)\), \(d_\lambda d_\alpha=d_{\lambda\alpha}\) is of trace class and \(\operatorname{Tr}(d_\lambda d_\alpha)=\sum_i\lambda_i\alpha_i\) by (4.2).

**Theorem 5.2** (the dual of \(K(H)\)). For \(t\in\mathcal L^1(H)\) let \(\varphi_t(x)=\operatorname{Tr}(xt)\), \(x\in K(H)\). Then \(t\mapsto\varphi_t\) is an isometric linear isomorphism of \(\mathcal L^1(H)\) onto \(K(H)^*\). Its inverse sends \(\omega\in K(H)^*\) to the operator \(t(\omega)\) determined by
\[
\begin{gathered}
\langle t(\omega)\xi,\eta\rangle\\
=\omega(\theta_{\xi,\eta})\\
(\xi,\eta\in H).
\end{gathered}
\tag{5.1}
\]
Consequently every \(\omega\in K(H)^*\) can be written
\[
\begin{gathered}
\omega\\
=\sum_ns_n\,\omega_{f_n,e_n}\ \ \\
(\text{norm convergent}),\\
\|\omega\|\\
=\sum_ns_n,
\end{gathered}
\tag{5.2}
\]
with orthonormal families \((e_n)\), \((f_n)\) and numbers \(s_n>0\) with \(\sum s_n<\infty\); here \(t(\omega)=\sum_ns_n\theta_{f_n,e_n}\). Conversely, for orthonormal sequences \((\xi_n)\), \((\eta_n)\) and \(\alpha\in\ell^1\), the series \(\omega=\sum_n\alpha_n\omega_{\xi_n,\eta_n}\) converges in \(K(H)^*\), \(t(\omega)=\sum_n\alpha_n\theta_{\xi_n,\eta_n}\), and \(\|\omega\|=\|\alpha\|_1\).

**Proof.** (i) By (4.3), \(|\varphi_t(x)|\le\|x\|\,\|t\|_1\), so \(\|\varphi_t\|\le\|t\|_1\).

(ii) Let \(\omega\in K(H)^*\). The map \((\xi,\eta)\mapsto\omega(\theta_{\xi,\eta})\) is sesquilinear and bounded by \(\|\omega\|\,\|\xi\|\,\|\eta\|\) (Lemma 1.4(a)). Theorem 1.3 gives a unique \(t(\omega)\in B(H)\) with (5.1).

(iii) \(\|t(\omega)\|_1\le\|\omega\|\). Let \((\xi_j)\), \((\eta_j)\) be finite orthonormal families, and choose \(c_j\) with \(|c_j|=1\) and \(c_j\langle t(\omega)\xi_j,\eta_j\rangle=|\langle t(\omega)\xi_j,\eta_j\rangle|\). With \(y=\sum_jc_j\theta_{\xi_j,\eta_j}\),
\[
\sum_j|\langle t(\omega)\xi_j,\eta_j\rangle|=\sum_jc_j\,\omega(\theta_{\xi_j,\eta_j})=\omega(y).
\]
Now \(y\) has finite rank and \[
\begin{gathered}
\|y\zeta\|^2\\
=\|\sum_jc_j\langle\zeta,\eta_j\rangle\xi_j\|^2\\
=\sum_j|\langle\zeta,\eta_j\rangle|^2\\
\le\|\zeta\|^2,
\end{gathered}
\] so \(\|y\|\le1\) and \(\omega(y)\le\|\omega\|\). Hence \(t(\omega)\in\mathcal L^1(H)\) and \(\|t(\omega)\|_1\le\|\omega\|\).

(iv) \(t(\varphi_t)=t\): by Lemma 1.4(b) and (4.2), \[
\begin{gathered}
\varphi_t(\theta_{\xi,\eta})\\
=\operatorname{Tr}(\theta_{\xi,\eta}t)\\
=\operatorname{Tr}(\theta_{\xi,t^*\eta})\\
=\langle\xi,t^*\eta\rangle\\
=\langle t\xi,\eta\rangle.
\end{gathered}
\]

(v) \(\varphi_{t(\omega)}=\omega\): both are bounded functionals on \(K(H)\), and by (4.4) and (5.1) they agree on every \(\theta_{\xi,\eta}\), hence on \(F(H)\) (Lemma 1.4(d)), which is dense in \(K(H)\).

By (iv) and (v), \(t\mapsto\varphi_t\) is bijective with inverse \(\omega\mapsto t(\omega)\), and (i) and (iii) give \(\|t\|_1\le\|\varphi_t\|\le\|t\|_1\). For (5.2), write \(t(\omega)\) as in (2.1); since \(xt(\omega)=\sum_ns_n\theta_{xf_n,e_n}\), formula (4.2) gives \(\omega(x)=\operatorname{Tr}(xt(\omega))=\sum_ns_n\langle xf_n,e_n\rangle\), and \(\|\omega\|=\|t(\omega)\|_1=\sum s_n\). The series converges in norm because \(\|\omega_{f_n,e_n}\|=1\). For the converse, \(t=\sum\alpha_n\theta_{\xi_n,\eta_n}\) is of trace class by Corollary 4.4(d) and \(\varphi_t=\sum\alpha_n\omega_{\xi_n,\eta_n}\) by (4.2). Writing \(\alpha_n=|\alpha_n|c_n\) with \(|c_n|=1\), we have \(t=\sum|\alpha_n|\theta_{c_n\xi_n,\eta_n}\), which after ordering the nonzero \(|\alpha_n|\) by size is a decomposition of the form (2.1). So \(\|\varphi_t\|=\|t\|_1=\|\alpha\|_1\) by Theorem 4.3(b). \(\square\)

The proof shows in particular that for every \(\omega\in K(H)^*\) the operator \(t(\omega)\) is compact and \(\sum_i|\langle t(\omega)\xi_i,\xi_i\rangle|\le\|\omega\|\) for every orthonormal family \((\xi_i)\). This estimate is the heart of the theorem: a bounded functional on \(K(H)\) cannot put too much weight on the diagonal of any basis.

**Proposition 5.3** (the module structure). For \(a\in B(H)\) and \(\omega\in K(H)^*\) define \((a\omega)(x)=\omega(xa)\) and \((\omega a)(x)=\omega(ax)\), \(x\in K(H)\). Then \(t(a\omega)=a\,t(\omega)\) and \(t(\omega a)=t(\omega)\,a\).

**Proof.** Let \(t=t(\omega)\), so \(\omega=\varphi_t\). By (4.3), \((a\omega)(x)=\operatorname{Tr}(xat)=\varphi_{at}(x)\) and \((\omega a)(x)=\operatorname{Tr}(axt)=\operatorname{Tr}(xta)=\varphi_{ta}(x)\). Apply Theorem 5.2. \(\square\)

So the two-sided ideal property of \(\mathcal L^1(H)\) (Corollary 4.4(a)) is the same thing as the natural \(B(H)\)-module structure of \(K(H)^*\).

**Theorem 5.4** (the dual of \(\mathcal L^1(H)\)). For \(a\in B(H)\) let \(\psi_a(t)=\operatorname{Tr}(at)\), \(t\in\mathcal L^1(H)\). Then \(a\mapsto\psi_a\) is an isometric linear isomorphism of \(B(H)\) onto \(\mathcal L^1(H)^*\). Consequently \(B(H)\) is isometrically isomorphic to \(K(H)^{**}\): the operator \(a\) corresponds to the functional \(\omega\mapsto\operatorname{Tr}(a\,t(\omega))\) on \(K(H)^*\), whose value at \(\omega_{\xi,\eta}\) is \(\langle a\xi,\eta\rangle\). Under this identification the canonical embedding of \(K(H)\) into \(K(H)^{**}\) is the inclusion \(K(H)\subseteq B(H)\).

**Proof.** By (4.3), \(\|\psi_a\|\le\|a\|\). By (4.4), \(\psi_a(\theta_{\xi,\eta})=\langle a\xi,\eta\rangle\), and \(\|\theta_{\xi,\eta}\|_1=\|\xi\|\,\|\eta\|\) by Lemma 4.2(b); so \(\|\psi_a\|\ge\sup\{|\langle a\xi,\eta\rangle|:\|\xi\|,\|\eta\|\le1\}=\|a\|\). To see that the map is onto, let \(\psi\in\mathcal L^1(H)^*\). The form \((\xi,\eta)\mapsto\psi(\theta_{\xi,\eta})\) is sesquilinear and bounded by \(\|\psi\|\,\|\xi\|\,\|\eta\|\), so Theorem 1.3 gives \(a\in B(H)\) with \(\langle a\xi,\eta\rangle=\psi(\theta_{\xi,\eta})=\psi_a(\theta_{\xi,\eta})\). Then \(\psi\) and \(\psi_a\) agree on \(F(H)\), which is dense in \(\mathcal L^1(H)\) (Corollary 4.4(c)), so \(\psi=\psi_a\).

By Theorem 5.2, \(\omega\mapsto t(\omega)\) is an isometric isomorphism \(K(H)^*\to\mathcal L^1(H)\); composing its adjoint with \(a\mapsto\psi_a\) gives the isometric isomorphism \(B(H)\to K(H)^{**}\), \(a\mapsto(\omega\mapsto\psi_a(t(\omega)))\). Since \(t(\omega_{\xi,\eta})=\theta_{\xi,\eta}\) by (5.1) and Lemma 1.4(e), the value at \(\omega_{\xi,\eta}\) is \(\operatorname{Tr}(a\theta_{\xi,\eta})=\langle a\xi,\eta\rangle\). For \(x\in K(H)\), the canonical image of \(x\) is \(\omega\mapsto\omega(x)=\varphi_{t(\omega)}(x)=\operatorname{Tr}(x\,t(\omega))\), which is the functional attached to \(a=x\). \(\square\)

## 6. The predual of B(H)

**Definition 6.1.** A linear functional \(\omega\) on \(B(H)\) is *normal* if \(\omega(x)=\operatorname{Tr}(xt)\) for some \(t\in\mathcal L^1(H)\). By Theorem 5.4 the operator \(t\) is unique; we write \(t=t_\omega\). The normal functionals form a subspace \(B(H)_*\) of \(B(H)^*\), with the norm of \(B(H)^*\); it is the *predual* of \(B(H)\).

**Theorem 6.2.**

(a) \(t\mapsto\operatorname{Tr}(\cdot\,t)\) is an isometric isomorphism of \(\mathcal L^1(H)\) onto \(B(H)_*\). In particular \(B(H)_*\) is a norm-closed subspace of \(B(H)^*\).

(b) Restriction to \(K(H)\) is an isometric isomorphism of \(B(H)_*\) onto \(K(H)^*\). So every bounded functional on \(K(H)\) has exactly one normal extension to \(B(H)\), and it has the same norm.

(c) The map sending \(a\in B(H)\) to the functional \(\omega\mapsto\omega(a)\) is an isometric isomorphism of \(B(H)\) onto \((B(H)_*)^*\).

(d) Every \(\omega\in B(H)_*\) can be written \(\omega=\sum_ns_n\omega_{f_n,e_n}\) with orthonormal families \((e_n)\), \((f_n)\) and \(\sum s_n=\|\omega\|\), or equivalently \(\omega=\sum_n\omega_{\xi_n,\eta_n}\) with \(\sum\|\xi_n\|^2=\sum\|\eta_n\|^2=\|\omega\|\), the series converging in norm. Conversely, if \(\sum_n\|\xi_n\|\,\|\eta_n\|<\infty\), then \(\sum_n\omega_{\xi_n,\eta_n}\) converges in norm to an element of \(B(H)_*\) of norm at most \(\sum\|\xi_n\|\,\|\eta_n\|\). In particular the finite sums of vector functionals are norm dense in \(B(H)_*\).

(e) For \(\omega\in B(H)_*\), \(\omega(x)=\operatorname{Tr}(xt_\omega)=\operatorname{Tr}(t_\omega x)\) and \(\omega(1)=\operatorname{Tr}(t_\omega)\).

**Proof.** (a) For \(t\in\mathcal L^1(H)\), \(\|\operatorname{Tr}(\cdot\,t)\|_{B(H)^*}\le\|t\|_1\) by (4.3). Its restriction to \(K(H)\) is \(\varphi_t\), of norm \(\|t\|_1\) by Theorem 5.2, so the norm is exactly \(\|t\|_1\). Injectivity follows, and \(B(H)_*\) is complete, hence closed. (b) follows from (a) and Theorem 5.2. (c) is Theorem 5.4 transported by (a). (d) With (2.1) for \(t_\omega\), \(xt_\omega=\sum_ns_n\theta_{xf_n,e_n}\) and (4.2) give \(\omega(x)=\sum_ns_n\langle xf_n,e_n\rangle\) for every \(x\in B(H)\), and \(\sum s_n=\|t_\omega\|_1=\|\omega\|\). For the second form put \(\xi_n=s_n^{1/2}f_n\), \(\eta_n=s_n^{1/2}e_n\). For the converse, \(t=\sum_n\theta_{\xi_n,\eta_n}\) is of trace class with \(\|t\|_1\le\sum\|\xi_n\|\,\|\eta_n\|\) (Corollary 4.4(d)), and \(\operatorname{Tr}(xt)=\sum_n\langle x\xi_n,\eta_n\rangle\) by (4.2). The partial sums of the first form are finite sums of vector functionals. (e) is (4.3). \(\square\)

**Proposition 6.3** (positive and hermitian normal functionals). Let \(\omega\in B(H)_*\).

(a) \(\omega\) is positive, that is \(\omega(x^*x)\ge0\) for all \(x\), if and only if \(t_\omega\ge0\). Then \(\omega=\sum_ns_n\omega_{e_n}\) for an orthonormal family \((e_n)\) and numbers \(s_n>0\) with \(\sum s_n=\omega(1)=\|\omega\|\); equivalently \(\omega=\sum_n\omega_{\zeta_n}\) with \(\sum\|\zeta_n\|^2=\omega(1)\).

(b) \(\omega\) is hermitian, that is \(\omega(x^*)=\overline{\omega(x)}\) for all \(x\), if and only if \(t_\omega\) is self-adjoint. A hermitian \(\omega\) is a difference \(\omega=\omega_1-\omega_2\) of positive normal functionals with \(\|\omega\|=\|\omega_1\|+\|\omega_2\|\).

(c) Every normal functional can be written \(\omega_1-\omega_2+i(\omega_3-\omega_4)\) with positive normal functionals \(\omega_1,\dots,\omega_4\).

**Proof.** Write \(t=t_\omega\). (a) If \(\omega\ge0\), then by (4.4) \(\langle t\xi,\xi\rangle=\operatorname{Tr}(t\theta_{\xi,\xi})=\omega(\theta_{\xi,\xi})\ge0\), since \(\theta_{\xi,\xi}=\|\xi\|^2p\) with \(p=p^*p\) a projection (Lemma 1.4(c)). Conversely, if \(t\ge0\), Theorem 2.3(e) gives \(t=\sum_ns_n\theta_{e_n,e_n}\), so \(\omega(x)=\sum_ns_n\langle xe_n,e_n\rangle\) and \(\omega(x^*x)=\sum_ns_n\|xe_n\|^2\ge0\). Then \(\|\omega\|=\|t\|_1=\operatorname{Tr}(t)=\omega(1)\), and \(\zeta_n=s_n^{1/2}e_n\) gives the second form.

(b) \(\omega(x^*)=\operatorname{Tr}(x^*t)\), while \(\overline{\omega(x)}=\operatorname{Tr}((xt)^*)=\operatorname{Tr}(t^*x^*)=\operatorname{Tr}(x^*t^*)\) by Theorem 4.6. So \(\omega\) is hermitian exactly when \(\operatorname{Tr}(y(t-t^*))=0\) for all \(y\in B(H)\). Taking \(y=\theta_{\xi,\eta}\) and using (4.3) and (4.4), this says \(\langle(t-t^*)\xi,\eta\rangle=0\) for all \(\xi,\eta\), that is, \(t=t^*\). Then Proposition 4.8 writes \(t=h_1-h_2\) with \(h_k\ge0\) and \(\|t\|_1=\operatorname{Tr}(h_1)+\operatorname{Tr}(h_2)\); put \(\omega_k=\operatorname{Tr}(\cdot\,h_k)\).

(c) Proposition 4.8. \(\square\)

**Remark 6.4.** When \(H\) is infinite-dimensional, \(B(H)_*\) is a proper subspace of \(B(H)^*\). By Theorem 6.2(b), a normal functional that vanishes on \(K(H)\) is zero, while Proposition 10.5(b) below produces states of \(B(H)\) that vanish on \(K(H)\). Sections 8 and 9 show that the normal functionals are exactly the linear functionals that are continuous for the \(\sigma\)-weak topology. The name *normal* refers to an order property, continuity along bounded increasing nets, which is treated in the lesson [The universal enveloping von Neumann algebra of a C\*-algebra, and W\*-algebras](the-universal-enveloping-von-neumann-algebra-of-a-c-star-algebra-and-w-star-algebras.md).

## 7. Ideals of B(H) and the Calkin algebra

In this section *ideal* means two-sided ideal of \(B(H)\), not necessarily closed. The finite-rank operators form the smallest nonzero ideal. When \(H\) is separable and infinite-dimensional, the compact operators form the largest proper ideal, and every proper ideal is determined by a space of sequences, the singular values of its elements. 

**Proposition 7.1.** Every nonzero ideal \(J\) of \(B(H)\) contains \(F(H)\). So \(F(H)\) is the smallest nonzero ideal, and \(K(H)\) is the smallest nonzero closed ideal.

**Proof.** Take \(x\in J\), \(x\ne0\), and \(\xi\) with \(x\xi\ne0\). By Lemma 1.4(b), \(x\theta_{\xi,\xi}x^*=\theta_{x\xi,x\xi}\in J\). For the unit vector \(\eta=x\xi/\|x\xi\|\), the projection \(\theta_{\eta,\eta}\) is a multiple of it, so it lies in \(J\). For arbitrary \(\zeta,\upsilon\in H\), Lemma 1.4(b) gives \(\theta_{\zeta,\upsilon}=\theta_{\zeta,\eta}\,\theta_{\eta,\eta}\,\theta_{\eta,\upsilon}\in J\). By Lemma 1.4(d), \(F(H)\subseteq J\). A closed nonzero ideal therefore contains the closure of \(F(H)\), which is \(K(H)\). \(\square\)

**Lemma 7.2.** Let \(h\in B(H)_+\) be noncompact. There are \(\varepsilon>0\) and a projection \(e\) of infinite rank that commutes with \(h\) and satisfies \(\varepsilon e\le he\le h\).

**Proof.** For \(\varepsilon>0\) let \(e_\varepsilon=1_{[\varepsilon,\infty)}(h)\), a spectral projection of \(h\) (Background 3(b)); it commutes with \(h\). On \([0,\infty)\) we have \(\lambda1_{[\varepsilon,\infty)}(\lambda)\ge\varepsilon1_{[\varepsilon,\infty)}(\lambda)\) and \(0\le\lambda-\lambda1_{[\varepsilon,\infty)}(\lambda)=\lambda1_{[0,\varepsilon)}(\lambda)\le\varepsilon\). By the functional calculus, \(\varepsilon e_\varepsilon\le he_\varepsilon\), \(0\le h-he_\varepsilon\), and \(\|h-he_\varepsilon\|\le\varepsilon\). If every \(e_\varepsilon\) had finite rank, then every \(he_\varepsilon\) would have finite rank, and \(h\) would be a norm limit of finite-rank operators, hence compact. So some \(e=e_\varepsilon\) has infinite rank. \(\square\)

**Proposition 7.3.** Let \(H\) be separable and infinite-dimensional, and let \(a\in B(H)\) be noncompact. There are \(b,c\in B(H)\) with \(bac=1\). Consequently every proper ideal of \(B(H)\) is contained in \(K(H)\); so \(K(H)\) is the largest proper ideal, and the closed ideals of \(B(H)\) are exactly \(0\), \(K(H)\) and \(B(H)\).

**Proof.** First, \(a^*a\) is not compact. Otherwise, let \((\zeta_k)\) be a sequence with \(\|\zeta_k\|\le M\), and pass to a subsequence along which \(a^*a\zeta_k\) converges. Since
\[
\begin{gathered}
\|a(\zeta_k-\zeta_l)\|^2\\
=\langle a^*a(\zeta_k-\zeta_l),\zeta_k-\zeta_l\rangle\\
\le2M\,\|a^*a(\zeta_k-\zeta_l)\|,
\end{gathered}
\]
\((a\zeta_k)\) is a Cauchy sequence along it, so \(a\) would be compact. By Lemma 7.2 there are \(\varepsilon>0\) and an infinite-rank projection \(e\) with \(\varepsilon e\le a^*a\). For \(\xi\in eH\), \(\|a\xi\|^2=\langle a^*a\xi,\xi\rangle\ge\varepsilon\langle e\xi,\xi\rangle=\varepsilon\|\xi\|^2\). The space \(eH\) is infinite-dimensional and separable, like \(H\), so there is an isometry \(c\) of \(H\) onto \(eH\): send an orthonormal basis of \(H\) onto one of \(eH\). Then \(\|ac\xi\|\ge\varepsilon^{1/2}\|\xi\|\) for all \(\xi\). So \(ac\) is injective with closed range \(L=acH\). Define \(b\) as the inverse of \(ac\) on \(L\) and \(0\) on \(L^\perp\); then \(\|b\|\le\varepsilon^{-1/2}\) and \(bac=1\). If an ideal \(J\) contains a noncompact \(a\), then \(1=bac\in J\) and \(J=B(H)\). With Proposition 7.1 this gives the last statement. \(\square\)

**Example 7.4** (separability is needed). Let \(H\) be nonseparable, and let \(J\) be the set of operators whose range lies in a separable closed subspace. If \(x,y\in J\), then \((x+y)H\) lies in the closed span of two separable subspaces, which is separable; \(axH\) lies in the closure of \(a\) applied to a separable subspace, which is separable; and \(xaH\subseteq xH\). So \(J\) is an ideal. It does not contain \(1\), and it contains the projection onto any separable infinite-dimensional subspace, which is not compact. So \(K(H)\) is not the largest proper ideal, and Proposition 7.3 fails without separability.

From now on in this section, \(H\) is separable and infinite-dimensional. For \(\lambda\in\ell^\infty\) and an orthonormal sequence \(\xi=(\xi_n)\) in \(H\) let
\[
d^\xi_\lambda=\sum_n\lambda_n\theta_{\xi_n,\xi_n},
\]
the series converging strongly. It is the diagonal operator of Example 2.2 on the closed span of the \(\xi_n\), extended by \(0\); so \(\|d^\xi_\lambda\|=\|\lambda\|_\infty\), \(d^\xi_\lambda d^\xi_\mu=d^\xi_{\lambda\mu}\), and \(d^\xi_\lambda\) is compact exactly when \(\lambda\in c_0\).

**Definition 7.5.** For an ideal \(J\) of \(B(H)\) let \(E(J)\) be the set of \(\lambda\in\ell^\infty\) such that \(d^\xi_\lambda\in J\) for some orthonormal sequence \(\xi\). A linear subspace \(E\) of \(c_0\) is *solid* if \(\mu\in E\) whenever \(\lambda\in E\) and \(|\mu_n|\le|\lambda_n|\) for all \(n\); solid subspaces are the ideals of \(c_0\) in the sense of ordered vector spaces. A solid subspace is *symmetric* if \((\lambda_{\pi(n)})_n\in E\) for every \(\lambda\in E\) and every bijection \(\pi\) of \(\mathbb N\). For a symmetric solid subspace \(E\) let
\[
J(E)=\{x\in K(H):\ s(x)\in E\}.
\]

**Lemma 7.6** (rearrangements). Let \(E\ne0\) be a symmetric solid subspace of \(c_0\).

(a) \(E\) contains \(c_{00}\).

(b) Let \(\lambda\in E\) and \(\mu\in c_0\), and suppose there is an injective map \(\sigma\) from \(S=\{n:\mu_n\ne0\}\) into \(\mathbb N\) with \(|\mu_n|\le|\lambda_{\sigma(n)}|\) for \(n\in S\). Then \(\mu\in E\).

In particular, \(E\) contains every subsequence of each of its elements, every sequence obtained from one of its elements by inserting zeros or by prefixing finitely many terms, and the sequence \((\lambda_1,\lambda_1,\lambda_2,\lambda_2,\dots)\) for each \(\lambda\in E\).

**Proof.** (a) Some \(\lambda\in E\) has a coordinate \(\lambda_m\ne0\). Then \(|\delta_m|\le|\lambda/\lambda_m|\) coordinatewise, so \(\delta_m\in E\); by symmetry every \(\delta_n\in E\), and \(E\) is a subspace.

(b) If \(S\) is finite, \(\mu\in c_{00}\subseteq E\). Suppose \(S\) is infinite, and first assume that \(\mathbb N\setminus S\) and \(\mathbb N\setminus\sigma(S)\) are both infinite. Then \(\sigma\) extends to a bijection \(\pi\) of \(\mathbb N\) (map \(\mathbb N\setminus S\) bijectively onto \(\mathbb N\setminus\sigma(S)\)). The sequence \(\rho=(\lambda_{\pi(n)})_n\) lies in \(E\) by symmetry, and \(|\mu_n|\le|\rho_n|\) for all \(n\), so \(\mu\in E\) by solidity. In general, list \(S=\{k_1<k_2<\cdots\}\) and put \(S_1=\{k_1,k_3,\dots\}\), \(S_2=\{k_2,k_4,\dots\}\). For \(i=1,2\) the complement of \(S_i\) contains \(S_{3-i}\) and the complement of \(\sigma(S_i)\) contains \(\sigma(S_{3-i})\), so both are infinite, and the first case gives \(\mu1_{S_i}\in E\). Hence \(\mu=\mu1_{S_1}+\mu1_{S_2}\in E\).

For the examples: a subsequence \((\lambda_{n_k})_k\) uses \(\sigma(k)=n_k\); inserting zeros uses the inverse of the placement map; prefixing finitely many terms gives a sequence in \(c_{00}\) plus a sequence of the previous kind; and \((\lambda_1,\lambda_1,\lambda_2,\lambda_2,\dots)\) is the sum of the two sequences that carry \(\lambda_n\) at the places \(2n-1\) and \(2n\) respectively. \(\square\)

**Theorem 7.7** (Calkin). Let \(H\) be separable and infinite-dimensional. For every nonzero proper ideal \(J\) of \(B(H)\), \(E(J)\) is a nonzero symmetric solid subspace of \(c_0\); for every nonzero symmetric solid subspace \(E\) of \(c_0\), \(J(E)\) is a nonzero proper ideal; and the maps \(J\mapsto E(J)\) and \(E\mapsto J(E)\) are inverse to each other. Moreover, \(\lambda\in E(J)\) if and only if \(d^\xi_\lambda\in J\) for every orthonormal sequence \(\xi\), and \(x\in J\) if and only if \(x\) is compact and \(s(x)\in E(J)\).


Under this correspondence \(c_{00}\), \(\ell^1\), \(\ell^2\) and \(c_0\) correspond to \(F(H)\), \(\mathcal L^1(H)\), \(\mathcal L^2(H)\) and \(K(H)\), by Theorems 3.3(b) and 4.3(b).

**Proof.** *Step 1: \(E(J)\) does not depend on the orthonormal sequence.* Let \(d^\xi_\lambda\in J\) and let \(\eta\) be another orthonormal sequence. The operator \(v\zeta=\sum_n\langle\zeta,\xi_n\rangle\eta_n\) has norm at most \(1\), maps \(\xi_n\) to \(\eta_n\), and \(v^*\zeta=\sum_n\langle\zeta,\eta_n\rangle\xi_n\). Then \(vd^\xi_\lambda v^*\zeta=\sum_n\lambda_n\langle\zeta,\eta_n\rangle\eta_n=d^\eta_\lambda\zeta\), so \(d^\eta_\lambda\in J\).

*Step 2: \(E(J)\) is a nonzero symmetric solid subspace of \(c_0\).* By Proposition 7.3, \(J\subseteq K(H)\), so \(E(J)\subseteq c_0\). Using one orthonormal sequence for all elements, \(d^\xi_{\lambda+\mu}=d^\xi_\lambda+d^\xi_\mu\) and \(d^\xi_{c\lambda}=cd^\xi_\lambda\) show that \(E(J)\) is a subspace. If \(|\mu|\le|\lambda|\) coordinatewise, put \(\beta_n=\mu_n/\lambda_n\) when \(\lambda_n\ne0\) and \(\beta_n=0\) otherwise; then \(\beta\in\ell^\infty\) and \(d^\xi_\mu=d^\xi_\beta d^\xi_\lambda\in J\). For a bijection \(\pi\), \(d^\xi_{\lambda\circ\pi}=d^\eta_\lambda\) with the orthonormal sequence \(\eta_m=\xi_{\pi^{-1}(m)}\), which lies in \(J\) by Step 1. Finally \(F(H)\subseteq J\) by Proposition 7.1, so \(\delta_1\in E(J)\).

*Step 3: \(J(E)\) is a nonzero proper ideal.* Let \(x,y\in J(E)\). By Proposition 2.5(b) with \(m=n\), \(s_{2n-1}(x+y)\le s_n(x)+s_n(y)\), and \(s_{2n}(x+y)\le s_{2n-1}(x+y)\). So, coordinatewise,
\[
\begin{gathered}
s(x+y)\\
\le D\big(s(x)+s(y)\big),\\
D(\alpha)\\
=(\alpha_1,\alpha_1,\alpha_2,\alpha_2,\dots).
\end{gathered}
\]
By Lemma 7.6, \(D(s(x)+s(y))\in E\), and by solidity \(s(x+y)\in E\). Also \(s(cx)=|c|\,s(x)\), and \(s(axb)\le\|a\|\,\|b\|\,s(x)\) by Proposition 2.5(a). So \(J(E)\) is an ideal. It contains \(F(H)\), because \(c_{00}\subseteq E\), and it lies in \(K(H)\ne B(H)\).

*Step 4: \(E(J(E))=E\).* Let \(\lambda\in c_0\) and let \(\xi\) be an orthonormal sequence. By Example 2.6, \(s(d^\xi_\lambda)\) lists the nonzero \(|\lambda_n|\) in decreasing order. So there are injective maps \(\sigma\) from the support of \(s(d^\xi_\lambda)\) into \(\mathbb N\) with \(s_k(d^\xi_\lambda)=|\lambda_{\sigma(k)}|\), and \(\tau\) from the support of \(\lambda\) into \(\mathbb N\) with \(|\lambda_n|=s_{\tau(n)}(d^\xi_\lambda)\). If \(\lambda\in E\), then \(s(d^\xi_\lambda)\in E\) by Lemma 7.6(b) with \(\sigma\), so \(d^\xi_\lambda\in J(E)\) and \(\lambda\in E(J(E))\). If \(\lambda\in E(J(E))\), then \(d^\eta_\lambda\in J(E)\) for some \(\eta\), so \(s(d^\eta_\lambda)\in E\), and Lemma 7.6(b) with \(\tau\) gives \(\lambda\in E\).

*Step 5: \(J(E(J))=J\).* Let \(x\in J\). Then \(x\) is compact. Write \(x\) as in (2.1). If the family \((e_n)\) is finite, extend it to an orthonormal sequence, which is possible since \(H\) is infinite-dimensional. By Theorem 2.3(b),(d), \(|x|=vx\in J\) and \(|x|=d^e_{s(x)}\). So \(s(x)\in E(J)\) and \(x\in J(E(J))\). Conversely, if \(x\in J(E(J))\), then \(s(x)\in E(J)\), so \(|x|=d^e_{s(x)}\in J\) by Step 1, and \(x=v^*|x|\in J\) by Theorem 2.3(d).

The last two statements of the theorem are Step 1 and Step 5. \(\square\)

**Example 7.8** (why the doubling operation matters). One may try to describe an ideal \(J\) by the set \(\Sigma(J)=\{s(x):x\in J\}\) of decreasing sequences alone. This set is hereditary (a decreasing sequence below a member is a member) and closed under addition. These two properties do not suffice. Let \(\Sigma\) be the set of decreasing nonnegative sequences \(\alpha\) with \(\alpha_n\le C2^{-n}\) for some \(C\). It is hereditary and closed under addition, but \(\{x\in K(H):s(x)\in\Sigma\}\) is not closed under addition. Indeed, let \(\xi\) and \(\eta\) be orthonormal sequences with \(\xi_n\perp\eta_m\) for all \(n,m\), and \(\lambda_n=2^{-n}\). Then \(s(d^\xi_\lambda)=s(d^\eta_\lambda)=\lambda\in\Sigma\), while \(d^\xi_\lambda+d^\eta_\lambda\) has each eigenvalue \(2^{-n}\) twice, so \(s_{2n}(d^\xi_\lambda+d^\eta_\lambda)=2^{-n}\), which is not \(O(2^{-2n})\). The missing condition is closure under \(D\), which Theorem 7.7 obtains from symmetry and solidity (Lemma 7.6).

*Human reference:* [Blackadar]. The counterexample above directly establishes the need for doubling; Theorem 7.7 includes it through symmetry and solidity.

**Proposition 7.9** (the Calkin algebra). Let \(H\) be infinite-dimensional, \(Q(H)=B(H)/K(H)\) the Calkin algebra, and \(q:B(H)\to Q(H)\) the quotient map. \(Q(H)\) is a C\*-algebra, as a quotient of a C\*-algebra by a closed ideal (lesson on C\*-algebras, Section 15).

(a) Fix an orthonormal sequence \(\xi\). The map \(\lambda\mapsto q(d^\xi_\lambda)\) induces an isometric \(*\)-isomorphism of \(\ell^\infty/c_0\) onto a C\*-subalgebra of \(Q(H)\).

(b) Every representation of \(Q(H)\) on a separable Hilbert space is zero. If \(H\) is separable, \(Q(H)\) is simple: its only closed ideals are \(0\) and \(Q(H)\).

**Proof.** (a) \(\lambda\mapsto d^\xi_\lambda\) is a \(*\)-homomorphism \(\ell^\infty\to B(H)\), so \(\lambda\mapsto q(d^\xi_\lambda)\) is a \(*\)-homomorphism with kernel \(\{\lambda:d^\xi_\lambda\in K(H)\}=c_0\). The induced map on \(\ell^\infty/c_0\) is an injective \(*\)-homomorphism between C\*-algebras, hence isometric with closed range (lesson on C\*-algebras, Section 4).

(b) If \(H\) is separable, the closed ideals of \(Q(H)\) correspond to the closed ideals of \(B(H)\) that contain \(K(H)\), which are \(K(H)\) and \(B(H)\) by Proposition 7.3; so \(Q(H)\) is simple. Let \(\pi:Q(H)\to B(K)\) be a nonzero \(*\)-representation, where \(K\) is a separable Hilbert space.

*Case 1: \(H\) separable.* The kernel of \(\pi\) is a closed ideal, not all of \(Q(H)\), so \(\pi\) is injective. Choose an uncountable family \((A_\iota)_{\iota\in\Omega}\) of infinite subsets of \(\mathbb N\) with \(A_\iota\cap A_\kappa\) finite for \(\iota\ne\kappa\). (Number the finite words in the letters \(0,1\) by \(\mathbb N\), and for each infinite \(0\)–\(1\) sequence \(\iota\) let \(A_\iota\) be the set of numbers of its initial segments.) The elements \(P_\iota=q(d^\xi_{1_{A_\iota}})\) are projections, nonzero because \(1_{A_\iota}\notin c_0\), and \(P_\iota P_\kappa=q(d^\xi_{1_{A_\iota\cap A_\kappa}})=0\) for \(\iota\ne\kappa\). So the \(\pi(P_\iota)\) are uncountably many nonzero mutually orthogonal projections on \(K\). Unit vectors in their ranges form an uncountable orthonormal family in the separable space \(K\), which is impossible.

*Case 2: \(H\) nonseparable.* Theorem 8.5 of the Hahn–Banach lesson proves that every uncountable set can be partitioned into uncountably many subsets, each in bijection with the whole set. Apply it to an orthonormal basis of \(H\). Let \(P_\iota\) be the projection onto the closed span of the \(\iota\)-th subfamily, and \(v_\iota\) an isometry of \(H\) onto \(P_\iota H\); then \(v_\iota^*P_\iota v_\iota=1\). The map \(\pi\circ q\) is a nonzero \(*\)-representation of \(B(H)\). If \(\pi(q(P_\iota))=0\), then \(\pi(q(1))=\pi(q(v_\iota^*P_\iota v_\iota))=0\) and \(\pi\circ q=0\). So the \(\pi(q(P_\iota))\) are uncountably many nonzero mutually orthogonal projections on \(K\), which is again impossible. \(\square\)

## 8. Seven topologies on B(H)

Besides the norm topology, \(B(H)\) carries six weaker locally convex topologies. Three of them test an operator on finitely many vectors at a time. The other three test it on square-summable sequences of vectors; they come from the duality \(B(H)=(B(H)_*)^*\) of Theorem 6.2(c).

**Definition 8.1.** Each topology below is the locally convex topology on \(B(H)\) generated by the listed seminorms. Here \(\xi,\eta\in H\), and \(\omega\) runs through \(B(H)_*\), or through the positive elements \(B(H)_*^+\) of \(B(H)_*\) where stated.

| topology | seminorms |
|---|---|
| weak | \(x\mapsto\lvert\langle x\xi,\eta\rangle\rvert\) |
| strong | \(x\mapsto\lVert x\xi\rVert\) |
| strong\(^*\) | \(x\mapsto(\lVert x\xi\rVert^2+\lVert x^*\xi\rVert^2)^{1/2}\) |
| \(\sigma\)-weak | \(x\mapsto\lvert\omega(x)\rvert\), \(\omega\in B(H)_*\) |
| \(\sigma\)-strong | \(x\mapsto p_\omega(x)=\omega(x^*x)^{1/2}\), \(\omega\in B(H)_*^+\) |
| \(\sigma\)-strong\(^*\) | \(x\mapsto(p_\omega(x)^2+p_\omega(x^*)^2)^{1/2}\), \(\omega\in B(H)_*^+\) |
| norm | \(x\mapsto\lVert x\rVert\) |

The norm topology is also called the uniform topology, the \(\sigma\)-weak topology the ultraweak topology, and the \(\sigma\)-strong topology the ultrastrong topology. By definition the \(\sigma\)-weak topology is \(\sigma(B(H),B(H)_*)\), the weak\(^*\) topology of \(B(H)\) as the dual of \(B(H)_*\), or equivalently of \(\mathcal L^1(H)\). The weak topology is \(\sigma(B(H),F_*)\), where \(F_*\) denotes the space of finite sums of vector functionals \(\omega_{\xi,\eta}\).

**Lemma 8.2** (equivalent seminorms).

(a) For \(\omega\in B(H)_*^+\) write \(\omega=\sum_n\omega_{\zeta_n}\) with \(\sum\|\zeta_n\|^2<\infty\) (Proposition 6.3(a)). Then \(p_\omega(x)=(\sum_n\|x\zeta_n\|^2)^{1/2}\), and \(p_\omega\) is a seminorm. Conversely, for every square-summable sequence \((\xi_n)\), \((\sum_n\|x\xi_n\|^2)^{1/2}=p_\omega(x)\) with \(\omega=\sum_n\omega_{\xi_n}\in B(H)_*^+\). So the \(\sigma\)-strong topology is generated by the seminorms \(x\mapsto(\sum_n\|x\xi_n\|^2)^{1/2}\), and the \(\sigma\)-strong\(^*\) topology by \(x\mapsto(\sum_n\|x\xi_n\|^2+\|x^*\xi_n\|^2)^{1/2}\), with \((\xi_n)\) square summable.

(b) The \(\sigma\)-weak topology is generated by the seminorms \(x\mapsto|\sum_n\langle x\xi_n,\eta_n\rangle|\) with \((\xi_n)\), \((\eta_n)\) square summable.

(c) In each of the strong, strong\(^*\), \(\sigma\)-strong and \(\sigma\)-strong\(^*\) topologies, finitely many of the defining seminorms are dominated by a single seminorm of the same kind. So every neighbourhood of \(x_0\) contains a set \(\{x:p(x-x_0)<\varepsilon\}\) with one seminorm \(p\) of that kind; for the strong topology \(p\) can be taken as \((\sum_{j\le m}\|x\xi_j\|^2)^{1/2}\) for finitely many vectors, and similarly for the strong\(^*\) topology.

**Proof.** (a) \[
\begin{gathered}
p_\omega(x)^2\\
=\omega(x^*x)\\
=\sum_n\langle x^*x\zeta_n,\zeta_n\rangle\\
=\sum_n\|x\zeta_n\|^2.
\end{gathered}
\] This is the square of the norm of the vector \((x\zeta_n)_n\) of \(\ell^2(\mathbb N;H)\), which depends linearly on \(x\); so \(p_\omega\) is a seminorm. The converse holds because \(\sum_n\omega_{\xi_n}\) is normal and positive by Theorem 6.2(d) and Proposition 6.3(a). (b) is Theorem 6.2(d). (c) For vectors, concatenate the finite families or the square-summable sequences; for positive normal functionals, \(p_{\omega_1}^2+\dots+p_{\omega_k}^2=p_{\omega_1+\dots+\omega_k}^2\). \(\square\)

**Proposition 8.3** (comparison). In the table

| | weak type | strong type | strong\(^*\) type |
|---|---|---|---|
| plain | weak | strong | strong\(^*\) |
| \(\sigma\) | \(\sigma\)-weak | \(\sigma\)-strong | \(\sigma\)-strong\(^*\) |

each topology is finer than the topologies to its left and than the topology above it, and the norm topology is finer than all six. So the weak topology is the coarsest and the \(\sigma\)-strong\(^*\) topology the finest of the six.

**Proof.** A topology given by seminorms is finer than another if each seminorm of the second is dominated by finitely many seminorms of the first. Now \(|\langle x\xi,\eta\rangle|\le\|x\xi\|\,\|\eta\|\) and \[
\begin{gathered}
|\sum_n\langle x\xi_n,\eta_n\rangle|\\
\le(\sum_n\|x\xi_n\|^2)^{1/2}(\sum_n\|\eta_n\|^2)^{1/2};
\end{gathered}
\] a starred seminorm dominates the unstarred one; a plain seminorm is the \(\sigma\)-seminorm of a sequence with one nonzero term; and \(p_\omega(x)\le\omega(1)^{1/2}\|x\|\). \(\square\)

**Example 8.4** (the comparisons are strict). Let \(H\) be infinite-dimensional and \((\xi_n)\) an orthonormal sequence.

(a) *Norm and \(\sigma\)-strong\(^*\).* The projections \(e_n=\theta_{\xi_n,\xi_n}\) tend to \(0\) \(\sigma\)-strongly\(^*\), although \(\|e_n\|=1\). Indeed \(p_\omega(e_n)^2=\omega(e_n)\), and \(\sum_n\omega(e_n)\le\omega(1)\) for \(\omega\in B(H)_*^+\) because \(e_1+\dots+e_m\le1\).

(b) *Starred and unstarred.* \(\theta_{\xi_1,\xi_n}\to0\) \(\sigma\)-strongly: for square-summable \((\zeta_k)\), \(\sum_k\|\theta_{\xi_1,\xi_n}\zeta_k\|^2=\sum_k|\langle\zeta_k,\xi_n\rangle|^2\to0\) by dominated convergence, since each term tends to \(0\) by Bessel's inequality and is at most \(\|\zeta_k\|^2\). But \(\theta_{\xi_1,\xi_n}^*=\theta_{\xi_n,\xi_1}\) and \(\|\theta_{\xi_n,\xi_1}\xi_1\|=1\), so the sequence does not tend to \(0\) strongly\(^*\). So the strong\(^*\) topology is finer than the strong one without being equal to it, and the same holds for the \(\sigma\)-strong\(^*\) and \(\sigma\)-strong topologies.

(c) *Strong type and weak type.* \(\theta_{\xi_n,\xi_1}\to0\) \(\sigma\)-weakly: for \(\omega\in B(H)_*\), (4.4) gives \(\omega(\theta_{\xi_n,\xi_1})=\operatorname{Tr}(\theta_{\xi_n,\xi_1}t_\omega)=\langle\xi_n,t_\omega^*\xi_1\rangle\to0\). But \(\|\theta_{\xi_n,\xi_1}\xi_1\|=1\), so there is no strong convergence to \(0\).

Example 9.2 below shows that each \(\sigma\)-topology is strictly finer than its plain version. If \(H\) is finite-dimensional, all seven topologies coincide: for an orthonormal basis \(\varepsilon_1,\dots,\varepsilon_d\), \(x=\sum_{i,j}\langle x\varepsilon_j,\varepsilon_i\rangle\theta_{\varepsilon_i,\varepsilon_j}\), so \(\|x\|\le\sum_{i,j}|\langle x\varepsilon_j,\varepsilon_i\rangle|\), and the weak topology is already the norm topology.

**Lemma 8.5** (bounded sets). On every bounded subset of \(B(H)\), the weak and \(\sigma\)-weak topologies coincide, the strong and \(\sigma\)-strong topologies coincide, and the strong\(^*\) and \(\sigma\)-strong\(^*\) topologies coincide.

**Proof.** Let \(\mathcal B\) be bounded, say \(\|x\|\le r\) for \(x\in\mathcal B\). Topologies are determined by their convergent nets, and each \(\sigma\)-topology is finer than its plain version. So it suffices to show: if a net \((x_\alpha)\) in \(\mathcal B\) converges to \(x\in\mathcal B\) in a plain topology, it converges in the \(\sigma\)-version. *Weak.* Let \(\omega\in B(H)_*\) and \(\varepsilon>0\). By Theorem 6.2(d) there is a finite sum \(\omega_0\) of vector functionals with \(\|\omega-\omega_0\|<\varepsilon\). Then \(|\omega(x_\alpha-x)|\le2r\varepsilon+|\omega_0(x_\alpha-x)|\), and the last term tends to \(0\). *Strong.* For square-summable \((\xi_n)\) and every \(N\),
\[
\begin{gathered}
\sum_n\|(x_\alpha-x)\xi_n\|^2\\
\le\sum_{n\le N}\|(x_\alpha-x)\xi_n\|^2+4r^2\sum_{n>N}\|\xi_n\|^2 .
\end{gathered}
\]
Choose \(N\) so that the tail is small; the finitely many remaining terms tend to \(0\). *Strong\(^*\).* Apply the same estimate to \(x_\alpha^*-x^*\) as well. \(\square\)

**Proposition 8.6** (continuity of the operations).

(a) For fixed \(a,b\in B(H)\), the map \(x\mapsto axb\) is continuous for all seven topologies. In particular multiplication is separately continuous in each of them.

(b) The adjoint \(x\mapsto x^*\) is continuous for the norm, weak, \(\sigma\)-weak, strong\(^*\) and \(\sigma\)-strong\(^*\) topologies. If \(H\) is infinite-dimensional, it is not continuous for the strong or the \(\sigma\)-strong topology, not even on the unit ball.

(c) If \(x_\alpha\to x\) and \(y_\alpha\to y\) strongly (resp. \(\sigma\)-strongly) and \(\sup_\alpha\|x_\alpha\|<\infty\), then \(x_\alpha y_\alpha\to xy\) strongly (resp. \(\sigma\)-strongly). If both nets are bounded and converge strongly\(^*\) (resp. \(\sigma\)-strongly\(^*\)), then \(x_\alpha y_\alpha\to xy\) strongly\(^*\) (resp. \(\sigma\)-strongly\(^*\)).

(d) If \(H\) is infinite-dimensional, multiplication is not jointly continuous for the weak or the \(\sigma\)-weak topology, not even on the unit ball.

**Proof.** (a) \(\|axb\xi\|\le\|a\|\,\|x(b\xi)\|\) and \(\sum_n\|axb\xi_n\|^2\le\|a\|^2\sum_n\|x(b\xi_n)\|^2\), where \((b\xi_n)\) is again square summable; \(\langle axb\xi_n,\eta_n\rangle=\langle x(b\xi_n),a^*\eta_n\rangle\); and \((axb)^*=b^*x^*a^*\) handles the starred seminorms. (b) \(\sum_n\langle x^*\xi_n,\eta_n\rangle=\overline{\sum_n\langle x\eta_n,\xi_n\rangle}\), and the starred seminorms are unchanged by \(x\mapsto x^*\). The counterexample is Example 8.4(b), which lies in the unit ball. (c) \[
\begin{gathered}
\|(x_\alpha y_\alpha-xy)\xi\|\\
\le\|x_\alpha\|\,\|(y_\alpha-y)\xi\|+\|(x_\alpha-x)y\xi\|,
\end{gathered}
\] and the same estimate holds in \(\ell^2(\mathbb N;H)\) for square-summable \((\xi_n)\), with \((y\xi_n)\) square summable. For the adjoints use \((x_\alpha y_\alpha)^*=y_\alpha^*x_\alpha^*\) and the bound on \(\|y_\alpha\|\). (d) Choose an orthonormal sequence in \(H\), let \(L\) be its closed span and \(p_L\) its projection. On \(L\cong\ell^2\) let \(S\delta_k=\delta_{k+1}\), and extend \(S\) by zero on \(L^\perp\). Then \(S^{*n}S^n=p_L\ne0\) for all \(n\geq1\), while both powers have norm at most one. In the following estimate use the coordinates of the \(L\)-components of \(\xi,\eta\). But \(S^n\to0\) and \(S^{*n}\to0\) weakly: \[
\begin{gathered}
|\langle S^n\xi,\eta\rangle|\\
=|\sum_k\xi_k\overline{\eta_{k+n}}|\\
\le\|\xi\|(\sum_{k>n}|\eta_k|^2)^{1/2}\to0,
\end{gathered}
\] and \(\langle S^{*n}\xi,\eta\rangle=\overline{\langle S^n\eta,\xi\rangle}\). By Lemma 8.5 the convergence is also \(\sigma\)-weak. \(\square\)

## 9. Continuous functionals and closed convex sets

The weak, strong and strong\(^*\) topologies have the same continuous linear functionals, and so do the three \(\sigma\)-topologies. By the Hahn–Banach theorem this forces them to have the same closed convex sets. The Krein–Šmulian theorem then reduces \(\sigma\)-weak closedness of a convex set to closedness of its bounded parts.

**Theorem 9.1** (continuous functionals). Let \(M\subseteq B(H)\) be a linear subspace and \(\omega\) a linear functional on \(M\). Continuity refers to the topologies restricted to \(M\).

(i) The following are equivalent: (1) \(\omega\) is weakly continuous; (2) \(\omega\) is strongly continuous; (3) \(\omega\) is strongly\(^*\) continuous; (4) there are finitely many vectors \(\xi_k,\eta_k\) with \(\omega(x)=\sum_k\langle x\xi_k,\eta_k\rangle\) for \(x\in M\).

(ii) The following are equivalent: (1) \(\omega\) is \(\sigma\)-weakly continuous; (2) \(\omega\) is \(\sigma\)-strongly continuous; (3) \(\omega\) is \(\sigma\)-strongly\(^*\) continuous; (4) there are square-summable sequences \((\xi_n)\), \((\eta_n)\) with \(\omega(x)=\sum_n\langle x\xi_n,\eta_n\rangle\) for \(x\in M\); (5) \(\omega\) is the restriction of a normal functional on \(B(H)\).

In particular, for \(M=B(H)\), the continuous linear functionals of the weak, strong and strong\(^*\) topologies are the elements of \(F_*\), and those of the three \(\sigma\)-topologies are the normal functionals.

**Proof.** (i) (1)\(\Rightarrow\)(2)\(\Rightarrow\)(3) because the topologies get finer (Proposition 8.3), and (4)\(\Rightarrow\)(1) is clear. (3)\(\Rightarrow\)(4): By continuity at \(0\) and Lemma 8.2(c), there are vectors \(\xi_1,\dots,\xi_m\) and \(\delta>0\) such that \(|\omega(x)|<1\) for all \(x\in M\) with \(q(x)<\delta\), where \(q(x)=(\sum_j\|x\xi_j\|^2+\|x^*\xi_j\|^2)^{1/2}\). By homogeneity \(|\omega(x)|\le\delta^{-1}q(x)\) on \(M\): if \(q(x)=0\), then \(q(sx)<\delta\) for all \(s>0\), so \(|\omega(x)|<1/s\) for all \(s\), and \(\omega(x)=0\). Let \(\mathcal K=H^m\oplus\overline H^m\) and
\[
J(x)=(x\xi_1,\dots,x\xi_m,\ \overline{x^*\xi_1},\dots,\overline{x^*\xi_m}).
\]
The map \(J:M\to\mathcal K\) is complex linear, because \((cx)^*\xi=\bar cx^*\xi\) and \(\overline{\bar cv}=c\bar v\) in \(\overline H\); and \(\|J(x)\|=q(x)\). So \(\omega=\tilde\omega\circ J\) for a well-defined linear functional \(\tilde\omega\) on \(J(M)\) with \(|\tilde\omega(v)|\le\delta^{-1}\|v\|\). Extend \(\tilde\omega\) by continuity to the closure of \(J(M)\) and by \(0\) on its orthogonal complement. The Riesz theorem gives \(\eta_1,\dots,\eta_m,\zeta_1,\dots,\zeta_m\in H\) with
\[
\begin{gathered}
\omega(x)\\
=\sum_j\langle x\xi_j,\eta_j\rangle+\sum_j\langle\overline{x^*\xi_j},\overline{\zeta_j}\rangle\\
=\sum_j\langle x\xi_j,\eta_j\rangle+\sum_j\langle\zeta_j,x^*\xi_j\rangle\\
=\sum_j\langle x\xi_j,\eta_j\rangle+\sum_j\langle x\zeta_j,\xi_j\rangle .
\end{gathered}
\]
This is (4).

(ii) (1)\(\Rightarrow\)(2)\(\Rightarrow\)(3) by Proposition 8.3. (3)\(\Rightarrow\)(4): the same argument, with a square-summable sequence \((\xi_n)\) in place of \(\xi_1,\dots,\xi_m\) and \(\mathcal K=\ell^2(\mathbb N;H)\oplus\ell^2(\mathbb N;\overline H)\), gives square-summable \((\eta_n)\), \((\zeta_n)\) with \(\omega(x)=\sum_n\langle x\xi_n,\eta_n\rangle+\sum_n\langle x\zeta_n,\xi_n\rangle\) on \(M\); interleaving the two sums gives one pair of square-summable sequences. (4)\(\Rightarrow\)(5): \(\sum_n\omega_{\xi_n,\eta_n}\) is normal by Theorem 6.2(d), since \(\sum\|\xi_n\|\,\|\eta_n\|<\infty\) by Cauchy–Schwarz. (5)\(\Rightarrow\)(1) holds by the definition of the \(\sigma\)-weak topology. \(\square\)

**Example 9.2** (the \(\sigma\)-topologies are strictly finer). Let \(H\) be infinite-dimensional, \((\xi_n)\) orthonormal, and \(\omega=\sum_n2^{-n}\omega_{\xi_n}\). Then \(\omega\) is normal, so it is \(\sigma\)-weakly continuous. It is not strongly\(^*\) continuous: otherwise, by Theorem 9.1(i), \(\omega=\sum_{k\le m}\omega_{\xi'_k,\eta'_k}\), and then \(t_\omega=\sum_{k\le m}\theta_{\xi'_k,\eta'_k}\) would have finite rank (Theorem 6.2(a)), whereas \(t_\omega=\sum_n2^{-n}\theta_{\xi_n,\xi_n}\) has infinite rank. Since each \(\sigma\)-topology is finer than its plain version (Proposition 8.3) and \(\omega\) is continuous for the \(\sigma\)-weak topology but not for the strong\(^*\) topology, no \(\sigma\)-topology equals its plain version: the \(\sigma\)-weak topology differs from the weak one, the \(\sigma\)-strong from the strong, and the \(\sigma\)-strong\(^*\) from the strong\(^*\).

**Theorem 9.3** (Krein–Šmulian). Let \(X\) be a Banach space and \(K\subseteq X^*\) a convex set. If \(K\cap rB_{X^*}\) is weak\(^*\) closed for every \(r>0\), then \(K\) is weak\(^*\) closed. Here \(B_{X^*}\) is the closed unit ball of \(X^*\) and weak\(^*\) means \(\sigma(X^*,X)\).


**Proof.** If \(K=\varnothing\), the conclusion is immediate. Otherwise write \(B=B_{X^*}\), and for \(F\subseteq X\) let \(F^\circ=\{\varphi\in X^*:|\varphi(x)|\le1\ \text{for all}\ x\in F\}\). Each \(F^\circ\) is weak\(^*\) closed, and \(F^\circ\cap G^\circ=(F\cup G)^\circ\).

*Step 1: reduction.* Let \(\varphi_0\in X^*\setminus K\); we must find a weak\(^*\) neighbourhood of \(\varphi_0\) that misses \(K\). The set \(K-\varphi_0\) is convex, and \[
\begin{gathered}
(K-\varphi_0)\cap rB\\
=\big(K\cap(r+\|\varphi_0\|)B\cap(\varphi_0+rB)\big)-\varphi_0
\end{gathered}
\] is weak\(^*\) closed, because \[
\begin{gathered}
\varphi_0+rB\\
=\{\varphi:|\varphi(x)-\varphi_0(x)|\le r\|x\|\ \text{for all}\ x\}
\end{gathered}
\] is weak\(^*\) closed. So we may assume \(\varphi_0=0\notin K\). The hypothesis makes \(K\) norm closed: a norm-convergent sequence in \(K\) is bounded, so it lies in some \(K\cap rB\), which is weak\(^*\) closed and hence norm closed. So some ball \(\rho B\), \(\rho>0\), misses \(K\), and after replacing \(K\) by \(\rho^{-1}K\) we may assume \(K\cap B=\emptyset\).

*Step 2: finite sets.* We choose finite sets \(F_1,F_2,\dots\subseteq X\), with \(\|x\|\le1/n\) for \(x\in F_n\), such that for every \(n\ge1\)
\[
K\cap nB\cap F_1^\circ\cap\dots\cap F_{n-1}^\circ=\emptyset .
\tag{9.1}
\]
For \(n=1\) this says \(K\cap B=\emptyset\). Suppose \(F_1,\dots,F_{n-1}\) are chosen, and put \(Q=F_1^\circ\cap\dots\cap F_{n-1}^\circ\). Suppose that \(K\cap(n+1)B\cap Q\cap F^\circ\ne\emptyset\) for every finite set \(F\) of vectors of norm at most \(1/n\). These sets are weak\(^*\) closed subsets of \((n+1)B\), which is weak\(^*\) compact by the Banach–Alaoglu theorem, and they have the finite intersection property. So they have a common point \(\varphi\). Then \(\varphi\in K\cap(n+1)B\cap Q\), and \(|\varphi(x)|\le1\) whenever \(\|x\|\le1/n\), so \(\|\varphi\|\le n\) and \(\varphi\in K\cap nB\cap Q\), contradicting (9.1) for \(n\). Hence some finite \(F_n\) of vectors of norm at most \(1/n\) gives \(K\cap(n+1)B\cap Q\cap F_n^\circ=\emptyset\), which is (9.1) for \(n+1\).

*Step 3: a null sequence.* List the elements of \(F_1,F_2,\dots\), in this order, as a sequence \((x_k)\), adding zeros if there are only finitely many. Then \(x_k\to0\). Let \(\varphi\in K\). Then \(\|\varphi\|>1\); choose an integer \(n\ge2\) with \(\|\varphi\|\le n\). By (9.1), \(\varphi\notin F_1^\circ\cap\dots\cap F_{n-1}^\circ\), so \(|\varphi(x_k)|>1\) for some \(k\).

*Step 4: separation.* The map \(T\varphi=(\varphi(x_k))_k\) is linear from \(X^*\) into \(c_0\). The convex set \(T(K)\) misses the open unit ball \(U\) of \(c_0\), by Step 3. By Hahn–Banach separation and Example 5.1(a), there are \(\alpha\in\ell^1\), \(\alpha\ne0\), and \(\gamma\in\mathbb R\) with
\[
\begin{gathered}
\operatorname{Re}\sum_k\alpha_ku_k<\gamma\\
\le\operatorname{Re}\sum_k\alpha_k\varphi(x_k)\\
(u\in U,\ \varphi\in K).
\end{gathered}
\]
The supremum of the left side over \(u\in U\) is \(\|\alpha\|_1\), so \(\gamma\ge\|\alpha\|_1\). The series \(x=\|\alpha\|_1^{-1}\sum_k\alpha_kx_k\) converges absolutely in \(X\), and \(\operatorname{Re}\varphi(x)\ge1\) for all \(\varphi\in K\). So the weak\(^*\) open set \(\{\varphi:\operatorname{Re}\varphi(x)<1\}\) contains \(0\) and misses \(K\). \(\square\)

**Theorem 9.4** (preduals of subspaces). Let \(M\subseteq B(H)\) be a \(\sigma\)-weakly closed linear subspace. Let \(M_*\) be the space of \(\sigma\)-weakly continuous linear functionals on \(M\) and \(M_\sim\) the space of weakly continuous ones, both with the norm of \(M^*\), and let \(M_\perp=\{\omega\in B(H)_*:\omega|_M=0\}\).

(a) Restriction \(\omega\mapsto\omega|_M\) maps \(B(H)_*\) onto \(M_*\), and it induces an isometric isomorphism of \(B(H)_*/M_\perp\) onto \(M_*\). In particular \(M_*\) is complete, and it is a norm-closed subspace of \(M^*\).

(b) The map sending \(x\in M\) to the functional \(\varphi\mapsto\varphi(x)\) is an isometric isomorphism of \(M\) onto \((M_*)^*\). Under it, \(\sigma(M,M_*)\) is the \(\sigma\)-weak topology restricted to \(M\).

(c) \(M_\sim\) is norm dense in \(M_*\).

**Proof.** (a) Restriction maps onto \(M_*\) by Theorem 9.1(ii), and its kernel is \(M_\perp\). Let \(\omega\in B(H)_*\). By Background 5(f), the quotient norm \(\|\omega+M_\perp\|\) is the supremum of \(|g(\omega+M_\perp)|\) over the unit ball of \((B(H)_*/M_\perp)^*\). By Background 5(e), with \(X=B(H)_*\) and \(X^*=B(H)\) (Theorem 6.2(c)), this dual is isometrically \[
\begin{gathered}
(M_\perp)^\perp\\
=\{x\in B(H):\omega'(x)=0\ \text{for all}\ \omega'\in M_\perp\},
\end{gathered}
\] and \((M_\perp)^\perp\) is the \(\sigma\)-weak closure of \(M\), which is \(M\). Hence
\[
\begin{gathered}
\|\omega+M_\perp\|\\
=\sup\{|\omega(x)|:\ x\in M,\ \|x\|\le1\}\\
=\|\omega|_M\|_{M^*}.
\end{gathered}
\]
So restriction induces an isometry of the Banach space \(B(H)_*/M_\perp\) onto \(M_*\).

(b) By (a) and Background 5(e), \((M_*)^*\cong(B(H)_*/M_\perp)^*\cong(M_\perp)^\perp=M\) isometrically. Following an element \(x\in M\) through these identifications, it acts on \(\omega|_M\) by \(\omega|_M\mapsto\omega(x)\), which is evaluation at \(x\). The topology \(\sigma(M,M_*)\) is pointwise convergence on the restrictions of normal functionals, which is the restricted \(\sigma\)-weak topology.

(c) By Theorem 9.1(i), \(M_\sim\) consists of the restrictions of elements of \(F_*\). Since \(F_*\) is norm dense in \(B(H)_*\) (Theorem 6.2(d)) and restriction is contractive and onto \(M_*\), the image of \(F_*\) is dense in \(M_*\). \(\square\)

**Theorem 9.5** (continuity on the unit ball). Let \(M\subseteq B(H)\) be a \(\sigma\)-weakly closed subspace, \(M_1=M\cap B(H)_1\), and \(\omega\) a linear functional on \(M\). The following are equivalent: (1) \(\omega\) is \(\sigma\)-weakly continuous on \(M\); (2) \(\omega\) is weakly continuous on \(M_1\); (3) \(\omega\) is strongly continuous on \(M_1\); (4) \(\omega\) is strongly\(^*\) continuous on \(M_1\). No boundedness of \(\omega\) is assumed.

**Proof.** (1)\(\Rightarrow\)(2): on \(M_1\) the \(\sigma\)-weak and weak topologies coincide (Lemma 8.5). (2)\(\Rightarrow\)(3)\(\Rightarrow\)(4): Proposition 8.3.

(4)\(\Rightarrow\)(2): The set \(M_1\) is \(\sigma\)-weakly closed in \(B(H)_1\), which is \(\sigma\)-weakly compact by the Banach–Alaoglu theorem (\(B(H)=\mathcal L^1(H)^*\), Theorem 5.4). So \(M_1\) is \(\sigma\)-weakly compact, hence weakly compact (the weak topology is coarser and Hausdorff), hence weakly closed, hence strongly\(^*\) closed. For \(c\in\mathbb R\), the set \(\{x\in M_1:\operatorname{Re}\omega(x)\le c\}\) is convex and closed in \(M_1\) for the strong\(^*\) topology, so it is strongly\(^*\) closed in \(B(H)\). The weak and strong\(^*\) topologies have the same continuous linear functionals (Theorem 9.1(i) with \(M=B(H)\)), so by Background 5(c) this convex set is weakly closed. The same holds for the sets where \(\operatorname{Re}\omega\ge c\), \(\operatorname{Im}\omega\le c\) and \(\operatorname{Im}\omega\ge c\). A real function whose sublevel and superlevel sets are all closed is continuous; so \(\operatorname{Re}\omega\) and \(\operatorname{Im}\omega\) are weakly continuous on \(M_1\).

(2)\(\Rightarrow\)(1): For \(r>0\), \(\ker\omega\cap rM_1=r(\ker\omega\cap M_1)\) is weakly closed, being the zero set of a weakly continuous function on the weakly closed set \(M_1\), rescaled. It is therefore \(\sigma\)-weakly closed. By Theorem 9.4(b), \(M\) is the dual of the Banach space \(M_*\), its weak\(^*\) topology is the restricted \(\sigma\)-weak topology, and its closed unit ball is \(M_1\). The Krein–Šmulian theorem shows that the convex set \(\ker\omega\) is \(\sigma\)-weakly closed in \(M\). A linear functional with closed kernel is continuous (Background 5(h)). \(\square\)

**Theorem 9.6** (closed convex sets). Let \(C\subseteq B(H)\) be convex.

(a) \(C\) has the same closure in the \(\sigma\)-weak, \(\sigma\)-strong and \(\sigma\)-strong\(^*\) topologies, and the same closure in the weak, strong and strong\(^*\) topologies.

(b) The following are equivalent: (1) \(C\) is \(\sigma\)-weakly closed; (2) \(C\) is \(\sigma\)-strongly closed; (3) \(C\) is \(\sigma\)-strongly\(^*\) closed; (4) \(C\cap rB(H)_1\) is weakly closed for every \(r>0\); (5) \(C\cap rB(H)_1\) is strongly closed for every \(r>0\); (6) \(C\cap rB(H)_1\) is strongly\(^*\) closed for every \(r>0\).

(c) The same holds for convex subsets of a \(\sigma\)-weakly closed subspace \(M\), and for convex subsets of \(B(H)_{\mathrm{sa}}\), with the relative topologies.

**Proof.** (a) By Theorem 9.1 with \(M=B(H)\), the three \(\sigma\)-topologies have the same continuous linear functionals, namely the normal ones, and the three plain topologies all have \(F_*\). Apply Background 5(c).

(b) (1)\(\Leftrightarrow\)(2)\(\Leftrightarrow\)(3) by (a). (1)\(\Rightarrow\)(4): \(rB(H)_1\) is \(\sigma\)-weakly closed, since \(\|x\|=\sup\{|\omega(x)|:\omega\in B(H)_*,\ \|\omega\|\le1\}\) by Theorem 6.2(c). So \(C\cap rB(H)_1\) is a \(\sigma\)-weakly closed subset of the \(\sigma\)-weakly compact set \(rB(H)_1\), hence \(\sigma\)-weakly compact, hence weakly compact and weakly closed. (4)\(\Rightarrow\)(5)\(\Rightarrow\)(6): a set closed in a coarser topology is closed in a finer one. (6)\(\Rightarrow\)(4): \(C\cap rB(H)_1\) is convex and strongly\(^*\) closed, hence weakly closed by (a). (4)\(\Rightarrow\)(1): each \(C\cap rB(H)_1\) is weakly closed, hence \(\sigma\)-weakly closed. Since \(B(H)=\mathcal L^1(H)^*\) with the \(\sigma\)-weak topology as weak\(^*\) topology, the Krein–Šmulian theorem shows that \(C\) is \(\sigma\)-weakly closed.

(c) Let \(M\) be a \(\sigma\)-weakly closed subspace, or \(M=B(H)_{\mathrm{sa}}\), which is a \(\sigma\)-weakly closed real subspace because the adjoint is \(\sigma\)-weakly continuous (Proposition 8.6(b)). For \(C\subseteq M\) and each of the six topologies, the closure of \(C\) in \(M\) is its closure in \(B(H)\) intersected with \(M\); so the equalities of (a) hold for closures in \(M\). Since \(M\) is \(\sigma\)-weakly closed, it is closed in all three \(\sigma\)-topologies, so \(C\) is closed in \(M\) for one of them exactly when it is closed in \(B(H)\). Finally \(M\cap rB(H)_1\) is \(\sigma\)-weakly compact, hence weakly closed, so a subset of \(C\cap rB(H)_1\) is closed in \(M\) for one of the plain topologies exactly when it is closed in \(B(H)\). So (b) holds for \(C\) with the relative topologies. \(\square\)

**Corollary 9.7.**

(a) The unit ball \(B(H)_1\) is \(\sigma\)-weakly compact and weakly compact, and so are \(\{x\in B(H)_{\mathrm{sa}}:\|x\|\le1\}\) and \(\{x:0\le x\le1\}\).

(b) A linear subspace of \(B(H)\) is \(\sigma\)-weakly closed if and only if it is \(\sigma\)-strongly\(^*\) closed, if and only if its intersection with the unit ball is weakly closed.

(c) On \(B(H)_{\mathrm{sa}}\) the \(\sigma\)-strong and \(\sigma\)-strong\(^*\) topologies coincide. The real-valued real-linear functionals on \(B(H)_{\mathrm{sa}}\) that are continuous for this topology, or for the \(\sigma\)-weak topology, are exactly the restrictions of hermitian normal functionals.

**Proof.** (a) Banach–Alaoglu, since \(B(H)=\mathcal L^1(H)^*\). The two sets are \(\sigma\)-weakly closed subsets of the unit ball: the conditions \(\langle x\xi,\xi\rangle\in\mathbb R\) for all \(\xi\) (which means \(x=x^*\), by Lemma 1.2) and \(0\le\langle x\xi,\xi\rangle\le\|\xi\|^2\) are \(\sigma\)-weakly closed. Weak compactness follows since the weak topology is coarser.

(b) Theorem 9.6(b) with \(r\) scaled out: for a subspace \(C\), \(C\cap rB(H)_1=r(C\cap B(H)_1)\).

(c) For \(h\) self-adjoint, \(p_\omega(h^*)=p_\omega(h)\). Let \(\rho\) be a real-linear functional on \(B(H)_{\mathrm{sa}}\) that is \(\sigma\)-strongly continuous. As in the proof of Theorem 9.1, \(|\rho(h)|\le Cp(h)\) for a single \(\sigma\)-strong seminorm \(p\). Define \(\omega(x)=\rho(\operatorname{Re}x)+i\rho(\operatorname{Im}x)\), with \(\operatorname{Re}x=\frac12(x+x^*)\) and \(\operatorname{Im}x=\frac1{2i}(x-x^*)\). Since \(\operatorname{Re}(ix)=-\operatorname{Im}x\) and \(\operatorname{Im}(ix)=\operatorname{Re}x\), we get \(\omega(ix)=i\omega(x)\), so \(\omega\) is complex linear. Also \(p(\operatorname{Re}x)\) and \(p(\operatorname{Im}x)\) are at most \(\frac12(p(x)+p(x^*))\), so \(|\omega(x)|\le C(p(x)+p(x^*))\) and \(\omega\) is \(\sigma\)-strongly\(^*\) continuous, hence normal by Theorem 9.1(ii). It is hermitian and restricts to \(\rho\). Conversely, a hermitian normal functional is real on \(B(H)_{\mathrm{sa}}\) and \(\sigma\)-weakly continuous, hence also \(\sigma\)-strongly continuous. \(\square\)

## 10. Metrizability and vector states

**Proposition 10.1** (metrizability on bounded sets).

(a) If \(H\) is separable, each of the six topologies weak, strong, strong\(^*\), \(\sigma\)-weak, \(\sigma\)-strong and \(\sigma\)-strong\(^*\) is metrizable on every bounded subset of \(B(H)\). Explicitly, let \((\zeta_n)\) be dense in the unit ball of \(H\) and put
\[
\begin{gathered}
d_w(x,y)\\
=\sum_{n,m}2^{-n-m}|\langle(x-y)\zeta_n,\zeta_m\rangle|,\\
d_s(x,y)\\
=\sum_n2^{-n}\|(x-y)\zeta_n\|,\\
d_{s^*}(x,y)\\
=d_s(x,y)+d_s(x^*,y^*).
\end{gathered}
\]
On each ball \(rB(H)_1\), \(d_w\) induces the weak and \(\sigma\)-weak topology, \(d_s\) the strong and \(\sigma\)-strong topology, and \(d_{s^*}\) the strong\(^*\) and \(\sigma\)-strong\(^*\) topology.

(b) If \(H\) is not separable, none of the six topologies is metrizable on \(B(H)_1\).

**Proof.** (a) The series converge on bounded sets, and each \(d\) is a metric: if \(d_w(x,y)=0\), then \(\langle(x-y)\zeta_n,\zeta_m\rangle=0\) for all \(n,m\), and \(x=y\) by density. Let \((x_\alpha)\) be a net in \(rB(H)_1\) and \(x\in rB(H)_1\). If \(x_\alpha\to x\) weakly, each term of \(d_w(x_\alpha,x)\) tends to \(0\), and the terms with \(n+m>N\) contribute at most \(2r\sum_{n+m>N}2^{-n-m}\), uniformly in \(\alpha\); so \(d_w(x_\alpha,x)\to0\). Conversely, if \(d_w(x_\alpha,x)\to0\), then \(\langle(x_\alpha-x)\zeta_n,\zeta_m\rangle\to0\) for all \(n,m\). For \(\xi,\eta\) in the unit ball choose \(\zeta_n,\zeta_m\) close to them; then \[
\begin{gathered}
|\langle(x_\alpha-x)\xi,\eta\rangle|\\
\le|\langle(x_\alpha-x)\zeta_n,\zeta_m\rangle|\\
+2r(\|\xi-\zeta_n\|+\|\eta-\zeta_m\|),
\end{gathered}
\] so \(x_\alpha\to x\) weakly. The same argument works for \(d_s\) and \(d_{s^*}\), and Lemma 8.5 transfers the result to the \(\sigma\)-topologies.

(b) The finite-rank projections form a directed set under \(p\le p'\). Along it, \((1-p)\xi=0\) as soon as \(\xi\in pH\), so the net \(1-p\) in \(B(H)_1\) tends to \(0\) strongly\(^*\), hence in each of the six topologies (on \(B(H)_1\) the strong\(^*\) topology is the finest of them, by Lemma 8.5). If one of the six topologies were metrizable on \(B(H)_1\), some sequence \(1-p_k\) would tend to \(0\) in it, hence weakly. Then \(\|(1-p_k)\xi\|^2=\langle(1-p_k)\xi,\xi\rangle\to0\) for every \(\xi\), so every \(\xi\) lies in the closure of \(\bigcup_kp_kH\), which is separable. This contradicts the nonseparability of \(H\). \(\square\)

**Proposition 10.2** (the six topologies are not metrizable on B(H)). Let \(H\) be infinite-dimensional, let \((e_n)\) be a sequence of nonzero mutually orthogonal projections, let \(c_n>0\), and let \(A=\{c_ne_n:n\ge1\}\).

(a) If \(\sum_nc_n^{-2}=\infty\), then \(0\) is an accumulation point of \(A\) for the \(\sigma\)-strong\(^*\) topology, and hence for all six topologies.

(b) If \(\sum_nc_n^{-1}=\infty\), then \(0\) is an accumulation point of \(A\) for the \(\sigma\)-weak topology.

(c) Let \(e_n=\theta_{\xi_n,\xi_n}\) for an orthonormal sequence \((\xi_n)\). If \(\sum_nc_n^{-2}<\infty\), then \(0\) is not in the strong closure of \(A\); if \(\sum_nc_n^{-1}<\infty\), then \(0\) is not in the weak closure of \(A\).

(d) If \(c_n\to\infty\), no subsequence of \((c_ne_n)\) converges weakly.

(e) None of the six topologies is metrizable on \(B(H)\); indeed none of them has a countable base of neighbourhoods at \(0\).

**Proof.** (a) By Lemma 8.2(c), every \(\sigma\)-strong\(^*\) neighbourhood of \(0\) contains a set \(\{x:p_\omega(x)^2+p_\omega(x^*)^2<\varepsilon^2\}\) with \(\omega\in B(H)_*^+\). Since \(e_n=e_n^*=e_n^*e_n\), \(p_\omega(c_ne_n)^2+p_\omega(c_ne_n^*)^2=2c_n^2\omega(e_n)\). Now \(\sum_n\omega(e_n)\le\omega(1)<\infty\), because \(e_1+\dots+e_m\le1\). If \(2c_n^2\omega(e_n)\ge\varepsilon^2\) held for all \(n\ge N\), then \(\omega(e_n)\ge\frac{\varepsilon^2}2c_n^{-2}\) would not be summable. So infinitely many \(c_ne_n\) lie in the neighbourhood. The other five topologies are coarser.

(b) A basic \(\sigma\)-weak neighbourhood of \(0\) is \(\{x:|\omega_j(x)|<\varepsilon,\ j\le m\}\) with \(\omega_j\in B(H)_*\). By Proposition 6.3(c) each \(\omega_j\) is a combination \(\sum_lc_{jl}\omega_{jl}\) of positive normal functionals; put \(\omega=\sum_{j,l}|c_{jl}|\omega_{jl}\). Then \(|\omega_j(e_n)|\le\omega(e_n)\) and \(\sum_n\omega(e_n)<\infty\). As in (a), \(c_n\omega(e_n)<\varepsilon\) for infinitely many \(n\).

(c) If \(\sum c_n^{-2}<\infty\), the vector \(\xi=\sum_nc_n^{-1}\xi_n\) exists and \(\|c_ne_n\xi\|=c_nc_n^{-1}=1\) for all \(n\); so the strong neighbourhood \(\{x:\|x\xi\|<1\}\) of \(0\) misses \(A\). If \(\sum c_n^{-1}<\infty\), the vector \(\xi=\sum_nc_n^{-1/2}\xi_n\) exists and \(\langle c_ne_n\xi,\xi\rangle=1\) for all \(n\).

(d) A weakly convergent sequence \((x_k)\) is bounded. Indeed, for each \(\xi\) the functionals \(\eta\mapsto\langle\eta,x_k\xi\rangle\) are bounded at each point, so \(\sup_k\|x_k\xi\|<\infty\) by uniform boundedness; applying uniform boundedness again gives \(\sup_k\|x_k\|<\infty\). But \(\|c_ne_n\|=c_n\to\infty\).

(e) Take \(c_n=\sqrt n\). By (a), \(0\) lies in the closure of \(A\) for each of the six topologies. If one of them had a countable neighbourhood base at \(0\), some sequence \((a_k)\) in \(A\) would converge to \(0\) in it, hence weakly. A sequence in \(A\) that takes some value \(c_me_m\ne0\) infinitely often cannot converge to \(0\), since the topology is Hausdorff. So \((a_k)\) has a subsequence of the form \((c_{n_k}e_{n_k})\) with \(n_k\) strictly increasing, which converges weakly to \(0\). This contradicts (d). \(\square\)

With \(c_n=n\), part (b) still gives an accumulation point for the \(\sigma\)-weak and weak topologies, but part (c) shows that \(\sqrt n\) cannot be replaced by \(n\) for the strong-type topologies.

The comparison just proved explains the choice \(\sqrt n\,e_n\): replacing it by \(ne_n\) retains weak-type accumulation but loses strong-type accumulation.

**Definition 10.3.** A *state* of \(B(H)\) is a positive linear functional \(\varphi\), that is \(\varphi(x^*x)\ge0\) for all \(x\), with \(\varphi(1)=1\). The states form a convex set \(S(H)\). A *pure state* is an extreme point of \(S(H)\). A *vector state* is a state \(\omega_\xi\) with \(\|\xi\|=1\); let \(V\) be the set of vector states and \(\overline V\) its closure in the weak\(^*\) topology \(\sigma(B(H)^*,B(H))\). Let \(S_0(H)\) be the set of states that vanish on \(K(H)\).

**Lemma 10.4.** (a) Every positive linear functional \(\varphi\) on \(B(H)\) is bounded, with \(\|\varphi\|=\varphi(1)\), and hermitian: \(\varphi(x^*)=\overline{\varphi(x)}\). (b) \(S(H)\) is weak\(^*\) compact, and \(S_0(H)\) is a weak\(^*\) closed convex subset of it.

**Proof.** (a) The form \((x,y)\mapsto\varphi(y^*x)\) on \(B(H)\) is sesquilinear and positive, so it is hermitian by Lemma 1.2, which gives \(\varphi(x^*)=\overline{\varphi(x)}\) (take \(y=1\)), and Background 1(d) gives \(|\varphi(y^*x)|^2\le\varphi(x^*x)\varphi(y^*y)\). Since \(x^*x\le\|x\|^21\), \(\varphi(x^*x)\le\|x\|^2\varphi(1)\). With \(y=1\): \(|\varphi(x)|^2\le\varphi(1)\varphi(x^*x)\le\varphi(1)^2\|x\|^2\). And \(\varphi(1)\le\|\varphi\|\). (b) By (a), \(S(H)\) lies in the unit ball of \(B(H)^*\) and is defined by weak\(^*\) closed conditions; apply Banach–Alaoglu. \(S_0(H)\) is cut out by the further conditions \(\varphi(x)=0\), \(x\in K(H)\). \(\square\)

**Proposition 10.5** (vector states).

(a) Every pure state of \(B(H)\) lies in \(\overline V\).

(b) Let \(H\) be infinite-dimensional. Then \(S_0(H)\cap\overline V\ne\emptyset\). If \(f\in\overline V\cap S_0(H)\) and \(L\subseteq H\) is a finite-dimensional subspace, then \(f\) lies in the weak\(^*\) closure of \(\{\omega_\eta:\eta\in L^\perp,\ \|\eta\|=1\}\).

(c) \(\overline V\cap S_0(H)\) is convex.

(d) \(S_0(H)\subseteq\overline V\): every state that vanishes on the compact operators is a weak\(^*\) limit of vector states.

**Proof.** (a) First, the weak\(^*\) closed convex hull \(C\) of \(V\) is \(S(H)\). Otherwise take \(\varphi\in S(H)\setminus C\). The space \(B(H)^*\) with the weak\(^*\) topology is locally convex, and its continuous linear functionals are the evaluations at elements of \(B(H)\) (Background 5(b)). By Background 5(a), applied to the compact set \(\{\varphi\}\) and the closed convex set \(C\), there are \(x\in B(H)\) and \(\gamma\in\mathbb R\) with \(\operatorname{Re}\varphi(x)>\gamma\ge\operatorname{Re}\psi(x)\) for all \(\psi\in C\). States are hermitian (Lemma 10.4), so with \(h=\frac12(x+x^*)\) we have \(\operatorname{Re}\psi(x)=\psi(h)\) for every state. In particular \(\langle h\xi,\xi\rangle\le\gamma\) for every unit vector \(\xi\), that is \(h\le\gamma1\), and so \(\varphi(h)\le\gamma\) by positivity. This contradicts \(\varphi(h)=\operatorname{Re}\varphi(x)>\gamma\). Now \(\overline V\) is weak\(^*\) compact, as a closed subset of \(S(H)\), and its closed convex hull \(S(H)\) is compact. By Milman's theorem (Background 5(g)) every extreme point of \(S(H)\) lies in \(\overline V\).

(b) Let \((\xi_n)\) be an orthonormal sequence. The states \(\omega_{\xi_n}\) have a weak\(^*\) cluster point \(f\in\overline V\), by compactness. For \(x\in K(H)\), \(\omega_{\xi_n}(x)=\langle x\xi_n,\xi_n\rangle\to0\) by Lemma 2.1, so \(f(x)=0\) and \(f\in S_0(H)\). For the second statement let \(f=\lim_\alpha\omega_{\xi_\alpha}\) with unit vectors \(\xi_\alpha\), and let \(p\) be the projection onto \(L\). Since \(p\) has finite rank, \(\|p\xi_\alpha\|^2=\omega_{\xi_\alpha}(p)\to f(p)=0\). So eventually \((1-p)\xi_\alpha\ne0\), and \(\eta_\alpha=(1-p)\xi_\alpha/\|(1-p)\xi_\alpha\|\) is a unit vector in \(L^\perp\) with \(\|\xi_\alpha-\eta_\alpha\|\to0\). Since \(|\omega_\xi(x)-\omega_\eta(x)|\le\|x\|(\|\xi\|+\|\eta\|)\|\xi-\eta\|\), \(\omega_{\eta_\alpha}\to f\).

(c) Let \(f,g\in\overline V\cap S_0(H)\) and \(0<\lambda<1\). A basic weak\(^*\) neighbourhood of \(\lambda f+(1-\lambda)g\) is given by finitely many operators \(x_1,\dots,x_n\) and \(\varepsilon>0\); we may assume \(x_1=1\), since adding an operator only shrinks the neighbourhood. Choose a unit vector \(\xi\) with \(|f(x_j)-\omega_\xi(x_j)|<\varepsilon\) for all \(j\). Apply (b) to \(g\) and \(L=\operatorname{span}\{x_j\xi,x_j^*\xi:j\le n\}\): there is a unit vector \(\eta\in L^\perp\) with \(|g(x_j)-\omega_\eta(x_j)|<\varepsilon\) for all \(j\). Put \(\zeta=\lambda^{1/2}\xi+(1-\lambda)^{1/2}\eta\). Since \(\eta\perp x_1\xi=\xi\), \(\|\zeta\|=1\). Since \(\langle x_j\xi,\eta\rangle=0\) and \(\langle x_j\eta,\xi\rangle=\langle\eta,x_j^*\xi\rangle=0\), we get \(\omega_\zeta(x_j)=\lambda\omega_\xi(x_j)+(1-\lambda)\omega_\eta(x_j)\), which is within \(\varepsilon\) of \(\lambda f(x_j)+(1-\lambda)g(x_j)\). So \(\lambda f+(1-\lambda)g\in\overline V\), and it lies in \(S_0(H)\) because \(S_0(H)\) is convex.

(d) If \(H\) is finite-dimensional, \(S_0(H)=\emptyset\). Otherwise \(S_0(H)\) is a nonempty weak\(^*\) compact convex set, by (b) and Lemma 10.4. It is a face of \(S(H)\): if \(f\in S_0(H)\) and \(f=\lambda\psi_1+(1-\lambda)\psi_2\) with \(\psi_i\in S(H)\) and \(0<\lambda<1\), then \(\psi_1(k)=\psi_2(k)=0\) for every positive compact \(k\), because \(0=f(k)\) is a combination of two nonnegative numbers with positive coefficients; every compact operator is a linear combination of positive compact operators (Theorem 2.3(e) applied to \(\operatorname{Re}k\) and \(\operatorname{Im}k\)); so \(\psi_1,\psi_2\in S_0(H)\). Hence every extreme point of \(S_0(H)\) is an extreme point of \(S(H)\), a pure state, and lies in \(\overline V\) by (a). So the extreme points of \(S_0(H)\) lie in \(\overline V\cap S_0(H)\), which is weak\(^*\) closed and, by (c), convex. By the Krein–Milman theorem, \(S_0(H)\subseteq\overline V\cap S_0(H)\). \(\square\)

The states in \(S_0(H)\) are the *singular* states: by Theorem 6.2(b) a normal state is determined by its restriction to \(K(H)\), so no singular state is normal. Part (d) shows that even so, each of them is a limit of vector states.

## 11. Self-adjoint operators modulo small ideals

In this section \(h\) and \(k\) denote bounded self-adjoint operators. We use the spectral theorem of Background 3(b): \(E\) is the spectral measure of \(h\), and \(\mu_\xi(\Delta)=\|E(\Delta)\xi\|^2\) is the spectral measure of a vector \(\xi\). Lebesgue measure on \(\mathbb R\) is written \(d\lambda\), and "null set" means Lebesgue null set. 

### The Weyl–von Neumann theorem

**Lemma 11.1.** Let \(h\in B(H)_{\mathrm{sa}}\), \(\xi\in H\) and \(m\ge1\). There is a projection \(p\) of rank at most \(m\) with \(p\xi=\xi\) and \(\|(1-p)hp\|_2\le\|h\|\,m^{-1/2}\).

**Proof.** If \(h=0\), let \(p\) be the projection onto \(\mathbb C\xi\). Otherwise put \(r=\|h\|\) and \(\delta=2r/m\), and divide \([-r,r]\) into the intervals \(\Delta_j=[-r+(j-1)\delta,-r+j\delta)\), \(j<m\), and \(\Delta_m=[r-\delta,r]\), with midpoints \(c_j\). Let \(e_j=E(\Delta_j)\). These are mutually orthogonal projections that commute with \(h\), \(\sum_je_j=E([-r,r])=1\), and \(\|(h-c_j)e_j\|\le\delta/2\) by the functional calculus. Let \(\xi_j=e_j\xi\), let \(p_j\) be the projection onto \(\mathbb C\xi_j\) (zero if \(\xi_j=0\)), and \(p=\sum_jp_j\). Since \(p_j\le e_j\), the \(p_j\) are mutually orthogonal, \(p\) is a projection of rank at most \(m\), \(p_j\xi=p_je_j\xi=\xi_j\), and \(p\xi=\sum_j\xi_j=\xi\). Also \(e_jp=p_j=pe_j\), so \(p\) commutes with every \(e_j\).

Put \(y_j=(1-p)hp_j\). Since \((1-p)p_j=0\), \(y_j=(1-p)(h-c_j)e_jp_j=e_j(1-p)(h-c_j)p_j\). So \(y_j\) has rank at most one, maps into \(e_jH\), and \(\|y_j\|\le\delta/2\). For a rank-one operator the Hilbert–Schmidt norm equals the norm (Theorem 3.3(b)), so \(\|y_j\|_2\le\delta/2\). The ranges of the \(y_j\) are mutually orthogonal, so for every vector \(\zeta\), \(\|(1-p)hp\,\zeta\|^2=\sum_j\|y_j\zeta\|^2\). Summing over an orthonormal basis,
\[
\begin{gathered}
\|(1-p)hp\|_2^2\\
=\sum_j\|y_j\|_2^2\\
\le m\,\frac{\delta^2}4\\
=\frac{r^2}m .\\
\square
\end{gathered}
\]

**Theorem 11.2** (Weyl–von Neumann). Let \(H\) be separable, \(h\in B(H)_{\mathrm{sa}}\) and \(\varepsilon>0\). Then \(h=k+a\), where \(a\) is a self-adjoint Hilbert–Schmidt operator with \(\|a\|_2<\varepsilon\) and \(k\) is a self-adjoint operator for which \(H\) has an orthonormal basis of eigenvectors.

**Proof.** Let \((\zeta_n)_{n\ge1}\) be a dense sequence in \(H\). We construct mutually orthogonal finite-rank projections \(q_1,q_2,\dots\) and self-adjoint Hilbert–Schmidt operators \(a_1,a_2,\dots\) with \(\|a_n\|_2\le\varepsilon2^{-n-1}\), such that, with \(Q_n=q_1+\dots+q_n\) and \(Q_0=0\):

(i) \(\zeta_n\in Q_nH\);

(ii) \[
\begin{gathered}
k_n:\\
=h-(a_1+\dots+a_n)\\
=\sum_{j\le n}q_jhq_j+(1-Q_n)h(1-Q_n).
\end{gathered}
\]

Suppose \(q_1,\dots,q_n\) and \(a_1,\dots,a_n\) are constructed; for \(n=0\) nothing is given and (ii) reads \(k_0=h\). Apply Lemma 11.1 in the Hilbert space \((1-Q_n)H\) to the self-adjoint operator \((1-Q_n)h(1-Q_n)\), of norm at most \(\|h\|\), to the vector \((1-Q_n)\zeta_{n+1}\), and to an \(m\) so large that \(\|h\|m^{-1/2}\le\varepsilon2^{-n-3}\). This gives a finite-rank projection \(q=q_{n+1}\le1-Q_n\) with \((1-Q_n)\zeta_{n+1}\in qH\) and, with \(Q_{n+1}=Q_n+q\), \(\|(1-Q_{n+1})hq\|_2\le\varepsilon2^{-n-3}\). Put
\[
a_{n+1}=(1-Q_{n+1})hq+qh(1-Q_{n+1}).
\]
It is self-adjoint, and \(\|a_{n+1}\|_2\le2\|(1-Q_{n+1})hq\|_2\le\varepsilon2^{-n-2}\) by Theorem 3.3(a). Condition (i) holds because \(\zeta_{n+1}=Q_n\zeta_{n+1}+(1-Q_n)\zeta_{n+1}\in Q_{n+1}H\). For (ii) write \(1-Q_n=q+s\) with \(s=1-Q_{n+1}\). Then \((1-Q_n)h(1-Q_n)=qhq+qhs+shq+shs\), so \(k_{n+1}=k_n-a_{n+1}=\sum_{j\le n+1}q_jhq_j+shs\), which is (ii) for \(n+1\).

Since \(\mathcal L^2(H)\) is complete and \(\sum\|a_n\|_2\le\varepsilon/2\), the series \(a=\sum_na_n\) converges in \(\|\cdot\|_2\), hence in norm; \(a\) is self-adjoint and \(\|a\|_2\le\varepsilon/2<\varepsilon\). Put \(k=h-a=\lim_nk_n\), a norm limit. For \(n\ge j\), (ii) gives \(q_jk_n=q_jhq_j=k_nq_j\), so \(q_jk=kq_j\) for every \(j\). The projections \(Q_n\) increase, and their ranges contain all \(\zeta_n\), which are dense; so \(Q_n\xi\to\xi\) for every \(\xi\), and \(H\) is the orthogonal sum of the finite-dimensional subspaces \(q_jH\). Each \(q_jH\) is invariant under the self-adjoint \(k\), so it has an orthonormal basis of eigenvectors of \(k\). Together they form an orthonormal basis of \(H\). \(\square\)

**Example 11.3** (separability cannot be dropped). Let \(\Gamma\) be an uncountable set, \(H=\ell^2(\Gamma;L^2(0,1))\), and let \(h\) act on each coordinate as the operator \(m\) of multiplication by the variable, \((m g)(t)=tg(t)\). Then \(h\ne k+a\) for every Hilbert–Schmidt operator \(a\) and every operator \(k\) for which \(H\) has an orthonormal basis of eigenvectors. Suppose otherwise. Since \(a\) is compact, the closures of the ranges of \(a\) and \(a^*\) are separable, and so is the closed span \(L\) of the vectors \(h^j v\), \(j\ge0\), with \(v\) in these ranges. \(L\) is invariant under \(h\), hence reduces \(h\). It contains the ranges of \(a\) and \(a^*\), so \(L^\perp\) lies in the kernels of \(a^*\) and \(a\): both \(a\) and \(a^*\) vanish on \(L^\perp\). Every vector of \(H\) has countably many nonzero coordinates, so a countable dense subset of \(L\) is supported in a countable set \(\Gamma_0\subseteq\Gamma\), and \(L\) lies in the coordinates \(\Gamma_0\). For \(\gamma\notin\Gamma_0\), the subspace \(X_\gamma\) of vectors supported at \(\gamma\) lies in \(L^\perp\) and reduces \(h\), \(a\) (which is \(0\) there) and hence \(k\). The projection \(P\) onto \(X_\gamma\) commutes with \(k\), so it maps each eigenvector of \(k\) to an eigenvector or to \(0\). These images span a dense subspace of \(X_\gamma\), so \(k\) has an eigenvector in \(X_\gamma\). But on \(X_\gamma\), \(k=h\) acts as \(m\), which has no eigenvectors: \((t-c)g(t)=0\) almost everywhere forces \(g=0\). This contradiction shows that Theorem 11.2 needs separability, even for Hilbert–Schmidt perturbations of arbitrary size.

**Remark 11.4.** The Hilbert–Schmidt norm enters only through Lemma 11.1: a block of rank at most \(m\) whose pieces have norm at most \(\|h\|/m\) has Hilbert–Schmidt norm at most \(\|h\|m^{-1/2}\), which tends to \(0\). The trace norm of the same block is only bounded by \(\|h\|\). Theorem 11.12 and Remark 11.17 show that this is not a weakness of the proof: the theorem is false for trace-class perturbations.

### Absolutely continuous and singular parts

**Definition 11.5.** For \(h\in B(H)_{\mathrm{sa}}\) let \(H_{\mathrm{ac}}(h)\) be the set of vectors \(\xi\) whose spectral measure \(\mu_\xi\) vanishes on null sets, and \(H_{\mathrm s}(h)\) the set of vectors whose spectral measure is concentrated on a null Borel set. The operator \(h\) is *absolutely continuous* if \(H_{\mathrm{ac}}(h)=H\).

**Proposition 11.6.** \(H_{\mathrm{ac}}(h)\) and \(H_{\mathrm s}(h)\) are closed subspaces, \(H_{\mathrm s}(h)=H_{\mathrm{ac}}(h)^\perp\), and both are invariant under every \(f(h)\), \(f\) a bounded Borel function; in particular they reduce \(h\). Every eigenvector of \(h\) lies in \(H_{\mathrm s}(h)\). We write \(P_{\mathrm{ac}}(h)\) for the projection onto \(H_{\mathrm{ac}}(h)\), and \(h_{\mathrm{ac}}\) and \(h_{\mathrm s}\) for the restrictions of \(h\) to the two subspaces; the spectral measures of \(h_{\mathrm{ac}}\) are the \(\mu_\xi\), \(\xi\in H_{\mathrm{ac}}(h)\).

**Proof.** If \(N\) is a null set and \(\mu_\xi(N)=\mu_\eta(N)=0\), then \(\|E(N)(\xi+\eta)\|\le\|E(N)\xi\|+\|E(N)\eta\|=0\); scalar multiples are clear, and \(\|E(N)\xi\|=\lim\|E(N)\xi_k\|\) when \(\xi_k\to\xi\). So \(H_{\mathrm{ac}}(h)\) is a closed subspace. For bounded Borel \(f\), \(E(N)\) commutes with \(f(h)\), so \(\mu_{f(h)\xi}(N)=\|f(h)E(N)\xi\|^2\le(\sup|f|)^2\mu_\xi(N)\); hence \(H_{\mathrm{ac}}(h)\) is invariant.

If \(\mu_\eta\) is concentrated on a null set \(N\), that is \(E(\mathbb R\setminus N)\eta=0\), then for \(\xi\in H_{\mathrm{ac}}(h)\), \(\langle\eta,\xi\rangle=\langle E(N)\eta,\xi\rangle=\langle\eta,E(N)\xi\rangle=0\). Conversely let \(\eta\perp H_{\mathrm{ac}}(h)\). Let \(\alpha\) be the supremum of \(\mu_\eta(N)\) over null Borel sets \(N\), and choose null sets \(N_k\) with \(\mu_\eta(N_k)\to\alpha\). Their union \(N\) is null and \(\mu_\eta(N)=\alpha\), so \(\mu_\eta(N'\setminus N)=0\) for every null \(N'\). The vector \(\xi=E(\mathbb R\setminus N)\eta\) has \(\mu_\xi(\Delta)=\mu_\eta(\Delta\setminus N)\), which vanishes on null sets; so \(\xi\in H_{\mathrm{ac}}(h)\), and \(0=\langle\eta,\xi\rangle=\|E(\mathbb R\setminus N)\eta\|^2\). So \(\mu_\eta\) is concentrated on \(N\). This proves \(H_{\mathrm s}(h)=H_{\mathrm{ac}}(h)^\perp\), which is invariant under the \(f(h)\) because the family \(\{f(h)\}\) is closed under adjoints. If \(h\xi=c\xi\), then \(\langle f(h)\xi,\xi\rangle=f(c)\|\xi\|^2\) for continuous \(f\), so \(\mu_\xi\) is the point mass \(\|\xi\|^2\delta_c\) (two finite measures on a compact interval with the same integrals of continuous functions agree on open intervals by monotone approximation, hence everywhere by Dynkin's lemma). \(\square\)

**Lemma 11.7** (cyclic subspaces). For \(\xi\in H\) let \(Z(\xi)\) be the closure of \(\{f(h)\xi:f\ \text{bounded Borel}\}\). Then \(Z(\xi)\) reduces \(h\), and there is a unitary \(U:Z(\xi)\to L^2(\mathbb R,\mu_\xi)\) with \(U(f(h)\xi)=f\). Under \(U\), each \(g(h)\) restricted to \(Z(\xi)\) becomes multiplication by \(g\); in particular \(h\) becomes multiplication by the variable \(\lambda\).

**Proof.** \(\|f(h)\xi\|^2=\langle|f|^2(h)\xi,\xi\rangle=\int|f|^2d\mu_\xi\). So \(f(h)\xi\mapsto f\) is well defined and isometric from a dense subspace of \(Z(\xi)\) onto the bounded Borel functions, which are dense in \(L^2(\mu_\xi)\); it extends to a unitary \(U\). Since \(g(h)f(h)\xi=(gf)(h)\xi\), \(Z(\xi)\) is invariant under each \(g(h)\), hence reducing, and \(Ug(h)f(h)\xi=gf\). \(\square\)

**Proposition 11.8** (the model). The operator \(h_{\mathrm{ac}}\) is unitarily equivalent to a direct sum \(\bigoplus_{i\in I}m_{S_i}\), where each \(S_i\subseteq[-\|h\|,\|h\|]\) is a Borel set and \(m_S\) is multiplication by \(\lambda\) on \(L^2(S,d\lambda)\). If \(H\) is separable, \(I\) is countable. Conversely, every such direct sum is absolutely continuous. So \(h\) is absolutely continuous exactly when it is unitarily equivalent to such a direct sum.

**Proof.** The spectral measure of \(m_S\) is \(\Delta\mapsto\) multiplication by \(1_\Delta\): this is a projection-valued measure whose integral of \(\lambda\) is \(m_S\), and the spectral measure is unique. So the spectral measure of a vector \(g=(g_i)\) of the direct sum is \(\Delta\mapsto\sum_i\int_{\Delta\cap S_i}|g_i|^2d\lambda\), which vanishes on null sets. Conversely, by Zorn's lemma choose a maximal family \((\xi_i)_{i\in I}\) of nonzero vectors of \(H_{\mathrm{ac}}(h)\) whose cyclic subspaces \(Z(\xi_i)\) are mutually orthogonal. If a nonzero \(\zeta\in H_{\mathrm{ac}}(h)\) were orthogonal to all \(Z(\xi_i)\), then \(\langle f(h)\zeta,g(h)\xi_i\rangle=\langle\zeta,(\bar fg)(h)\xi_i\rangle=0\), so \(Z(\zeta)\perp Z(\xi_i)\) for all \(i\), contradicting maximality. So \(H_{\mathrm{ac}}(h)=\bigoplus_iZ(\xi_i)\), and \(I\) is countable if \(H\) is separable. By the Radon–Nikodym theorem \(\mu_{\xi_i}=\rho_i\,d\lambda\) with a Borel function \(\rho_i\ge0\), which we may take to vanish outside \([-\|h\|,\|h\|]\). Let \(S_i=\{\rho_i>0\}\). The map \(g\mapsto g\rho_i^{1/2}\) is a unitary of \(L^2(\mu_{\xi_i})\) onto \(L^2(S_i,d\lambda)\) that commutes with multiplication by \(\lambda\). Combined with Lemma 11.7, this gives the unitary equivalence. \(\square\)

**Proposition 11.9** (multiplication operators). Let \((X,\mu)\) be a \(\sigma\)-finite measure space, \(f:X\to\mathbb R\) a bounded measurable function, and \(m_f\) multiplication by \(f\) on \(L^2(X,\mu)\).

(a) \(m_f\) is absolutely continuous exactly when \(\mu(f^{-1}(N))=0\) for every null Borel set \(N\subseteq\mathbb R\).

(b) Let \(X\) be a bounded open interval with Lebesgue measure and \(f\) continuously differentiable and bounded. Then \(m_f\) is absolutely continuous exactly when \(\{t:f'(t)=0\}\) is a null set.

**Proof.** (a) As in Proposition 11.8, the spectral measure of \(m_f\) is \(\Delta\mapsto\) multiplication by \(1_{f^{-1}(\Delta)}\), so \(\mu_g(\Delta)=\int_{f^{-1}(\Delta)}|g|^2d\mu\). If every \(f^{-1}(N)\) is \(\mu\)-null, every \(\mu_g\) vanishes on null sets. If \(\mu(f^{-1}(N))>0\) for some null \(N\), choose \(A\subseteq f^{-1}(N)\) with \(0<\mu(A)<\infty\); then \(g=1_A\) has \(\mu_g(N)=\mu(A)>0\).

(b) Let \(Z=\{f'=0\}\). If \(Z\) is null: the open set \(\{f'\ne0\}\) is a countable union of open intervals \(J\), on each of which \(f\) is strictly monotone with a continuously differentiable inverse \(g_J\) defined on the interval \(f(J)\). The inverse derivative is \(g_J'(f(t))=1/f'(t)\): this follows by taking difference quotients in \(f(g_J(y))=y\), and continuity follows from continuity and nonvanishing of \(f'\). On compact subintervals its derivative is bounded, so the mean value theorem makes \(g_J\) Lipschitz. Lemma 0.1(b) then shows that it maps null sets to null sets, and \(f^{-1}(N)\cap J=g_J(N\cap f(J))\) is null for every null \(N\). Hence \(f^{-1}(N)\subseteq Z\cup\bigcup_J(f^{-1}(N)\cap J)\) is null, and (a) applies. Conversely suppose \(Z\) has positive measure. Then \(f(Z)\) is null. Indeed, let \([c,d]\subseteq X\) and \(\varepsilon>0\); by uniform continuity of \(f'\) on \([c,d]\), divide \([c,d]\) into finitely many intervals on each of which \(f'\) varies by less than \(\varepsilon\). On each such interval that meets \(Z\) we have \(|f'|<\varepsilon\), so by the mean value theorem its image is an interval of length at most \(\varepsilon\) times its length. Hence \(f(Z\cap[c,d])\) is covered by intervals of total length at most \(\varepsilon(d-c)\); letting \(\varepsilon\to0\) and exhausting \(X\) by countably many \([c,d]\), \(f(Z)\) is null. Choose a null Borel set \(N\supseteq f(Z)\). Then \(f^{-1}(N)\supseteq Z\) has positive measure, and \(m_f\) is not absolutely continuous by (a). \(\square\)

The Cantor function used in the next example has an elementary construction. Start with \(c_0(t)=t\) on \([0,1]\), and define \(c_{n+1}(t)=c_n(3t)/2\) on \([0,1/3]\), \(c_{n+1}(t)=1/2\) on \([1/3,2/3]\), and \(c_{n+1}(t)=1/2+c_n(3t-2)/2\) on \([2/3,1]\). Induction gives continuity, monotonicity and endpoint values zero and one. Moreover \(\|c_{n+1}-c_n\|_\infty\leq2^{-n}\|c_1-c_0\|_\infty\), so the sequence is uniformly Cauchy and has a continuous nondecreasing limit \(c\). On every middle-third interval removed at stage \(j\), all later functions have the same constant dyadic value, hence so does \(c\). The remaining Cantor set is covered at stage \(n\) by \(2^n\) intervals of length \(3^{-n}\), so it is null by Lemma 0.1(b). There are only countably many removed intervals, and their union has full measure in \((0,1)\).

For example, multiplication by \(t\) on \(L^2(0,1)\) is absolutely continuous. At the other extreme, let \(c\) be the Cantor function on \((0,1)\). It is continuous and nondecreasing, and it is constant on each of the countably many open intervals removed in the construction of the Cantor set, whose total length is \(1\). So for almost every \(t\), \(c(t)\) lies in the countable set \(C\) of values taken on these intervals. Hence \(L^2(0,1)\) is the orthogonal sum of the spaces \(L^2(c^{-1}(v))\), \(v\in C\), on each of which \(m_c\) acts as the scalar \(v\): every spectral measure of \(m_c\) is a countable sum of point masses, and \(m_c\) has an orthonormal basis of eigenvectors, although \(c\) is continuous and nondecreasing.

**Lemma 11.10** (square-integrable Fourier transforms). Let \(\mu\) be a finite positive Borel measure on \(\mathbb R\) and \(\hat\mu(s)=\int e^{is\lambda}d\mu(\lambda)\).

(a) If \(\hat\mu\in L^2(\mathbb R)\), then \(\mu=g\,d\lambda\) with \(g\in L^1(\mathbb R)\cap L^2(\mathbb R)\).

(b) If \(\mu=g\,d\lambda\) with \(g\in L^1(\mathbb R)\cap L^2(\mathbb R)\), then \(\hat\mu\in L^2(\mathbb R)\) and \(\int|\hat\mu|^2ds=2\pi\int g^2d\lambda\).

**Proof.** (b) \(\hat\mu(s)=\hat g(-s)\); apply Plancherel (Background 4(c)). (a) For \(\sigma>0\) let \(\rho_\sigma(\lambda)=\int\gamma_\sigma(\lambda-\nu)\,d\mu(\nu)\), with the normal density \(\gamma_\sigma\) of Background 4(c). Then \(0\le\rho_\sigma\le(2\pi\sigma^2)^{-1/2}\mu(\mathbb R)\) and \(\int\rho_\sigma=\mu(\mathbb R)\), so \(\rho_\sigma\in L^1\cap L^2\). By Fubini's theorem and the formula for the transform of \(\gamma_\sigma\),
\[
\begin{gathered}
\hat\rho_\sigma(s)\\
=\int e^{-is\nu}\Big(\int e^{-is(\lambda-\nu)}\gamma_\sigma(\lambda-\nu)\,d\lambda\Big)d\mu(\nu)\\
=e^{-\sigma^2s^2/2}\,\hat\mu(-s).
\end{gathered}
\]
As \(\sigma\to0\), these functions converge in \(L^2(ds)\) to \(\hat\mu(-s)\), by dominated convergence. Since \(w\mapsto(2\pi)^{-1/2}\hat w\) extends to a unitary operator of \(L^2(\mathbb R)\), the functions \(\rho_\sigma\) converge in \(L^2(d\lambda)\) to some \(g\) as \(\sigma\to0\). Since \(\rho_\sigma\ge0\), also \(g\ge0\) almost everywhere (a sequence \(\rho_{\sigma_k}\) converges to \(g\) almost everywhere). For continuous \(\varphi\) with compact support, on the one hand \(\int\varphi\rho_\sigma\,d\lambda\to\int\varphi g\,d\lambda\). On the other hand \(\int\varphi\rho_\sigma\,d\lambda=\int(\int\varphi(\lambda)\gamma_\sigma(\lambda-\nu)\,d\lambda)\,d\mu(\nu)\), and the inner integral is bounded by \(\sup|\varphi|\) and tends to \(\varphi(\nu)\) for every \(\nu\), by continuity of \(\varphi\); so \(\int\varphi\rho_\sigma\,d\lambda\to\int\varphi\,d\mu\). Hence \(\int\varphi\,d\mu=\int\varphi g\,d\lambda\). Taking \(0\le\varphi_j\uparrow1_{(c,d)}\) and using monotone convergence, \(\mu((c,d))=\int_c^dg\,d\lambda\) for every bounded interval. Letting \((c,d)\) increase to \(\mathbb R\) gives \(\int g=\mu(\mathbb R)<\infty\), so \(g\in L^1\), and \(\mu=g\,d\lambda\) by Dynkin's lemma. \(\square\)

**Proposition 11.11** (a Fourier criterion). Let \(u(t)=e^{ith}\), so that \(\langle u(t)\xi,\xi\rangle=\hat\mu_\xi(t)\). Let \(D\) be the set of \(\xi\in H\) with \(\int_{\mathbb R}|\langle u(t)\xi,\xi\rangle|^2dt<\infty\). Then \(D\subseteq H_{\mathrm{ac}}(h)\), and the set of \(\xi\in H_{\mathrm{ac}}(h)\) whose spectral measure has a bounded density is contained in \(D\) and dense in \(H_{\mathrm{ac}}(h)\). Consequently \(h\) is absolutely continuous exactly when \(D\) is dense in \(H\).

**Proof.** \(\langle u(t)\xi,\xi\rangle=\int e^{it\lambda}d\mu_\xi(\lambda)\) by Background 3(b). Lemma 11.10(a) gives \(D\subseteq H_{\mathrm{ac}}(h)\). If \(\mu_\xi\) has a bounded density, that density lies in \(L^1\cap L^2\), and \(\xi\in D\) by Lemma 11.10(b). Now let \(\xi\in H_{\mathrm{ac}}(h)\) with density \(\rho\), a Borel function, and put \(\xi_n=E(\{\rho\le n\})\xi\). Then \(\mu_{\xi_n}(\Delta)=\mu_\xi(\Delta\cap\{\rho\le n\})\) has the density \(\rho1_{\{\rho\le n\}}\le n\), and \(\|\xi-\xi_n\|^2=\mu_\xi(\{\rho>n\})=\int_{\{\rho>n\}}\rho\,d\lambda\to0\). This proves the density statement. If \(D\) is dense in \(H\), then so is \(H_{\mathrm{ac}}(h)\supseteq D\), which is closed; so \(H_{\mathrm{ac}}(h)=H\). The converse follows from the density statement. \(\square\)

### Trace-class perturbations: the Kato–Rosenblum theorem

For \(a,b\in B(H)_{\mathrm{sa}}\) we write \(W(t)=W_{a,b}(t)=e^{ita}e^{-itb}\), a unitary operator. The map \(t\mapsto W(t)\) is differentiable in norm with derivative \(ie^{ita}(a-b)e^{-itb}\), so for \(t,t'\in\mathbb R\) and \(\zeta\in H\)
\[
\begin{gathered}
W(t)\zeta-W(t')\zeta\\
=i\int_{t'}^te^{isa}(a-b)e^{-isb}\zeta\,ds .
\end{gathered}
\tag{11.1}
\]
Since \(e^{ita}-e^{itb}=(W(t)-W(0))e^{itb}\), (11.1) with \(t'=0\) gives \(\|e^{ita}-e^{itb}\|\le|t|\,\|a-b\|\).

**Theorem 11.12** (Kato–Rosenblum). Let \(h,k\in B(H)_{\mathrm{sa}}\) with \(h-k\in\mathcal L^1(H)\). Then the strong limit
\[
W_+=\lim_{t\to\infty}e^{ith}e^{-itk}P_{\mathrm{ac}}(k)
\]
exists. It is a partial isometry with initial space \(H_{\mathrm{ac}}(k)\) and final space \(H_{\mathrm{ac}}(h)\), and \(hW_+=W_+k\). In particular \(h_{\mathrm{ac}}\) and \(k_{\mathrm{ac}}\) are unitarily equivalent. The same holds for \(t\to-\infty\).

The proof takes the rest of this section. Its argument uses the following elementary stages: an estimate for the rate of convergence is proved first for perturbations for which convergence is easy, in a form that does not involve the limit, and then carried over to all trace-class perturbations by approximation. The operator \(W_+\) is called a *wave operator*. Nothing in the proof uses separability of \(H\).

**Lemma 11.13** (an \(L^2\) estimate). Let \(k\in B(H)_{\mathrm{sa}}\) and let \(\zeta\in H_{\mathrm{ac}}(k)\) have spectral density \(\rho\le M\) almost everywhere. Then for every \(\eta\in H\),
\[
\int_{\mathbb R}|\langle e^{-isk}\zeta,\eta\rangle|^2ds\le2\pi M\,\|\eta\|^2 .
\]

**Proof.** Let \(U:Z(\zeta)\to L^2(\mu_\zeta)\) be the unitary of Lemma 11.7 for \(k\), let \(\eta_Z\) be the projection of \(\eta\) onto \(Z(\zeta)\), and \(\gamma=U\eta_Z\). Since \(e^{-isk}\zeta\in Z(\zeta)\) and \(Ue^{-isk}\zeta=e^{-is\lambda}\),
\[
\begin{gathered}
\langle e^{-isk}\zeta,\eta\rangle\\
=\langle e^{-isk}\zeta,\eta_Z\rangle\\
=\int e^{-is\lambda}\,\overline{\gamma(\lambda)}\,\rho(\lambda)\,d\lambda\\
=\hat w(s),\\
w\\
=\bar\gamma\rho .
\end{gathered}
\]
Now \(\int|w|\le(\int|\gamma|^2\rho)^{1/2}(\int\rho)^{1/2}=\|\eta_Z\|\,\|\zeta\|\) and \[
\begin{gathered}
\int|w|^2\\
=\int|\gamma|^2\rho^2\\
\le M\int|\gamma|^2\rho\\
=M\|\eta_Z\|^2\\
\le M\|\eta\|^2.
\end{gathered}
\] By Plancherel, \(\int|\hat w|^2ds=2\pi\int|w|^2\le2\pi M\|\eta\|^2\). \(\square\)

**Lemma 11.14** (Cook's criterion). Let \(a,b\in B(H)_{\mathrm{sa}}\), and let \(D\subseteq H_{\mathrm{ac}}(b)\) be a set whose linear span is dense in \(H_{\mathrm{ac}}(b)\). If \(\int_0^\infty\|(a-b)e^{-isb}\zeta\|\,ds<\infty\) for every \(\zeta\in D\), then \(\lim_{t\to\infty}W_{a,b}(t)\zeta\) exists for every \(\zeta\in H_{\mathrm{ac}}(b)\).


**Proof.** For \(\zeta\in D\), (11.1) gives \[
\begin{gathered}
\|W(t)\zeta-W(t')\zeta\|\\
\le\int_{t'}^t\|(a-b)e^{-isb}\zeta\|\,ds\to0
\end{gathered}
\] as \(t,t'\to\infty\). So \(W(t)\zeta\) converges for \(\zeta\) in the span of \(D\). For \(\zeta\in H_{\mathrm{ac}}(b)\) and \(\varepsilon>0\) choose \(\zeta'\) in the span with \(\|\zeta-\zeta'\|<\varepsilon\); since \(W(t)\) is unitary, \(\|W(t)\zeta-W(t')\zeta\|\le2\varepsilon+\|W(t)\zeta'-W(t')\zeta'\|\). \(\square\)

**Lemma 11.15** (properties of wave operators). Let \(a,b\in B(H)_{\mathrm{sa}}\), and suppose that \(\lim_{t\to\infty}W(t)\zeta\) exists for every \(\zeta\in H_{\mathrm{ac}}(b)\), where \(W=W_{a,b}\). Let \(W_+\) equal this limit on \(H_{\mathrm{ac}}(b)\) and \(0\) on \(H_{\mathrm{ac}}(b)^\perp\).

(a) \(\|W_+\zeta\|=\|\zeta\|\) for \(\zeta\in H_{\mathrm{ac}}(b)\), and \(\|W_+\|\le1\).

(b) \(e^{isa}W_+=W_+e^{isb}\) for all \(s\in\mathbb R\), and \(aW_+=W_+b\).

(c) For \(\zeta\in H_{\mathrm{ac}}(b)\), the spectral measure of \(W_+\zeta\) for \(a\) equals the spectral measure of \(\zeta\) for \(b\). In particular \(W_+H_{\mathrm{ac}}(b)\subseteq H_{\mathrm{ac}}(a)\).

(d) Suppose \(a-b=\sum_{n=1}^Nc_n\theta_{f_n,f_n}\) with real \(c_n\) and vectors \(f_n\in H\), and let \(\zeta\in H_{\mathrm{ac}}(b)\) have spectral density bounded by \(M\). Put \(\eta_n(t)=\int_t^\infty|\langle e^{-isb}\zeta,f_n\rangle|^2ds\), finite by Lemma 11.13. Then for every \(t\),
\[
\begin{gathered}
\|W_+\zeta-W(t)\zeta\|^2\\
\le2(2\pi M)^{1/2}\\
{}\cdot\Big(\sum_n|c_n|\,\|f_n\|^2\Big)^{1/2}\\
{}\cdot\Big(\sum_n|c_n|\,\eta_n(t)\Big)^{1/2}.
\end{gathered}
\tag{11.2}
\]

**Proof.** (a) \(\|W_+\zeta\|=\lim\|W(t)\zeta\|=\|\zeta\|\). The operator \(W_+\) is linear, and it is isometric on \(H_{\mathrm{ac}}(b)\) and zero on its complement.

(b) Let \(\zeta\in H_{\mathrm{ac}}(b)\). Then \(e^{-isb}\zeta\in H_{\mathrm{ac}}(b)\) by Proposition 11.6, and \(W(t+s)=e^{isa}W(t)e^{-isb}\). Letting \(t\to\infty\) gives \(W_+\zeta=e^{isa}W_+e^{-isb}\zeta\); replacing \(\zeta\) by \(e^{isb}\zeta\) gives \(W_+e^{isb}\zeta=e^{isa}W_+\zeta\). On \(H_{\mathrm{ac}}(b)^\perp\), which is invariant under \(e^{isb}\), both sides vanish. For \(\zeta\in H\), \(s^{-1}(e^{isa}-1)W_+\zeta\to iaW_+\zeta\) and \(W_+s^{-1}(e^{isb}-1)\zeta\to iW_+b\zeta\) as \(s\to0\), because \(s^{-1}(e^{isx}-1)\to ix\) in norm for bounded \(x\). So \(aW_+=W_+b\).

(c) By (b), \(p(a)W_+=W_+p(b)\) for every polynomial \(p\). Let \(\zeta\in H_{\mathrm{ac}}(b)\). By (a) and polarization, \(W_+\) preserves inner products on \(H_{\mathrm{ac}}(b)\), and \(p(b)\zeta\in H_{\mathrm{ac}}(b)\); so
\[
\begin{gathered}
\langle p(a)W_+\zeta,W_+\zeta\rangle\\
=\langle W_+p(b)\zeta,W_+\zeta\rangle\\
=\langle p(b)\zeta,\zeta\rangle .
\end{gathered}
\]
Thus the two spectral measures give the same integral to every polynomial. Both live on \([-R,R]\) with \(R=\max(\|a\|,\|b\|)\). By the Weierstrass approximation theorem (Proposition 15.1(2) of The Stone–Weierstrass theorem for functions vanishing at infinity, specialized to the compact real interval (where the coordinate and its conjugate agree)) they give the same integral to every continuous function on \([-R,R]\); by monotone approximation of indicator functions of open intervals and Dynkin's lemma they are equal.

(d) Since \(\|W_+\zeta\|=\|\zeta\|=\|W(t)\zeta\|\),
\[
\begin{gathered}
\|W_+\zeta-W(t)\zeta\|^2\\
=2\operatorname{Re}\langle W_+\zeta-W(t)\zeta,W_+\zeta\rangle .
\end{gathered}
\]
By (11.1), with \(V=a-b\),
\[
\begin{gathered}
\langle W_+\zeta-W(t)\zeta,W_+\zeta\rangle\\
=\lim_{r\to\infty}\,i\int_t^r\langle e^{isa}Ve^{-isb}\zeta,W_+\zeta\rangle\,ds .
\end{gathered}
\]
By (b), \(e^{-isa}W_+\zeta=W_+e^{-isb}\zeta\), so the integrand is
\[
\begin{gathered}
\langle Ve^{-isb}\zeta,W_+e^{-isb}\zeta\rangle\\
=\sum_nc_n\langle e^{-isb}\zeta,f_n\rangle\,\langle W_+^*f_n,e^{-isb}\zeta\rangle .
\end{gathered}
\]
By Lemma 11.13 applied to \(b\) and \(\eta=W_+^*f_n\), with \(\|W_+^*f_n\|\le\|f_n\|\), \(\int_{\mathbb R}|\langle e^{-isb}\zeta,W_+^*f_n\rangle|^2ds\le2\pi M\|f_n\|^2\). Let \(\eta_n(t)=\int_t^\infty|\langle e^{-isb}\zeta,f_n\rangle|^2ds\), which is finite by Lemma 11.13. The Cauchy–Schwarz inequality, first in \(s\) and then in \(n\), gives for every \(r>t\)
\[
\begin{gathered}
\Big|\int_t^r\langle Ve^{-isb}\zeta,W_+e^{-isb}\zeta\rangle\,ds\Big|\\
\le\sum_n|c_n|\,\eta_n(t)^{1/2}\\
{}\cdot(2\pi M)^{1/2}\|f_n\|\\
\le(2\pi M)^{1/2}\Big(\sum_n|c_n|\,\|f_n\|^2\Big)^{1/2}\\
{}\cdot\Big(\sum_n|c_n|\eta_n(t)\Big)^{1/2}.
\end{gathered}
\]
The same bound holds for the limit \(r\to\infty\), and (11.2) follows. \(\square\)

The point of (11.2) is that its right side involves neither \(W_+\) nor \(a\). This is what allows passage to a limit in the perturbation.

**Lemma 11.16** (a model for the absolutely continuous part). Let \(k\in B(H)_{\mathrm{sa}}\). There are a Hilbert space \(H'\), an absolutely continuous \(k'\in B(H')_{\mathrm{sa}}\), a bounded open interval \(I\), a set \(J\), and a unitary \(\Phi\) of \(H_{\mathrm{ac}}(k)\oplus H'\) onto the Hilbert space \(L^2(I;\ell^2(J))\) of families \((g_j)_{j\in J}\) in \(L^2(I)\) with \(\sum_j\|g_j\|^2<\infty\), such that \(H_{\mathrm{ac}}(k\oplus k')=H_{\mathrm{ac}}(k)\oplus H'\) and \(\Phi(k\oplus k')\Phi^{-1}\) is multiplication by \(\lambda\) in each entry. Let \(D\) be the set of \(\zeta\in H_{\mathrm{ac}}(k\oplus k')\) such that \(\Phi\zeta\) has finitely many nonzero entries, each in \(C_c^\infty(I)\). Then \(D\) is a dense subspace of \(H_{\mathrm{ac}}(k\oplus k')\), and for \(\zeta,\eta\in D\):

(i) the spectral density of \(\zeta\) for \(k\oplus k'\) is the bounded function \(\lambda\mapsto\sum_j|(\Phi\zeta)_j(\lambda)|^2\);

(ii) the function \(s\mapsto\langle e^{-is(k\oplus k')}\zeta,\eta\rangle\) is integrable on \(\mathbb R\).

**Proof.** By Proposition 11.8, there is a unitary \(\Phi_0\) of \(H_{\mathrm{ac}}(k)\) onto \(\bigoplus_{j\in J}L^2(S_j)\) carrying \(k_{\mathrm{ac}}\) to \(\bigoplus_jm_{S_j}\), with \(S_j\subseteq[-\|k\|,\|k\|]\). Let \(I=(-\|k\|-1,\|k\|+1)\), \(H'=\bigoplus_jL^2(I\setminus S_j)\) and \(k'=\bigoplus_jm_{I\setminus S_j}\), which is absolutely continuous by Proposition 11.8. The spectral measure of \(k\oplus k'\) is the direct sum of the spectral measures, so the spectral measure of \(\zeta\oplus\zeta'\) is \(\mu_\zeta+\mu_{\zeta'}\), and \(H_{\mathrm{ac}}(k\oplus k')=H_{\mathrm{ac}}(k)\oplus H'\). Regard \(L^2(S_j)\) and \(L^2(I\setminus S_j)\) as the functions in \(L^2(I)\) that vanish off \(S_j\), respectively on \(S_j\); then \(L^2(I)=L^2(S_j)\oplus L^2(I\setminus S_j)\), and adding the entries defines \(\Phi\). Density of \(D\) follows from Background 4(b). Statement (i) follows as in the proof of Proposition 11.8. For (ii), \(\langle e^{-is(k\oplus k')}\zeta,\eta\rangle=\int_Ie^{-is\lambda}w(\lambda)\,d\lambda\) with \(w=\sum_j(\Phi\zeta)_j\overline{(\Phi\eta)_j}\in C_c^\infty(I)\). Integrating by parts twice, this is at most \(\min(\|w\|_1,s^{-2}\|w''\|_1)\) in absolute value, which is integrable in \(s\). \(\square\)

**Proof of Theorem 11.12.** Let \(V=h-k\). It is a self-adjoint trace-class operator, so by Theorem 2.3(e) \(V=\sum_nc_n\theta_{f_n,f_n}\) with an orthonormal family \((f_n)\), real \(c_n\ne0\), and \(\sum|c_n|=\|V\|_1\) by Theorem 4.3(b); the index \(n\) runs through \(\{1,\dots,r\}\) or \(\mathbb N\) (if \(V=0\), there is nothing to prove).

*Step 1: enlarging the space.* Take \(H'\), \(k'\), \(\Phi\) and \(D\) as in Lemma 11.16, and put \(\hat H=H\oplus H'\), \(\hat k=k\oplus k'\) and \(\hat h=h\oplus k'\). Then \(\hat h-\hat k=V\oplus0=\sum_nc_n\theta_{\hat f_n,\hat f_n}\) with \(\hat f_n=f_n\oplus0\), and \(\hat W(t)=e^{it\hat h}e^{-it\hat k}=W_{h,k}(t)\oplus1\). Since \(H_{\mathrm{ac}}(k)\oplus0\subseteq H_{\mathrm{ac}}(\hat k)\), it suffices to prove that \(\hat W(t)\zeta\) converges for every \(\zeta\in H_{\mathrm{ac}}(\hat k)\); by density of \(D\) and \(\|\hat W(t)\|=1\) (the approximation step at the end of the proof of Lemma 11.14), it suffices to do this for \(\zeta\in D\).

*Step 2: approximating the perturbation.* Let \(g_n=P_{\mathrm{ac}}(\hat k)\hat f_n\). For each integer \(m\ge1\) and each \(n\le m\) choose \(g^{(m)}_n\in D\) with \(\|g^{(m)}_n-g_n\|\le1/m\), put \(f^{(m)}_n=\hat f_n-g_n+g^{(m)}_n\), and let
\[
\begin{gathered}
V_m\\
=\sum_{n\le m}c_n\theta_{f^{(m)}_n,f^{(m)}_n},\\
h_m\\
=\hat k+V_m,\\
W_m(t)\\
=e^{ith_m}e^{-it\hat k}.
\end{gathered}
\]
Then \(\|f^{(m)}_n\|\le1+1/m\le2\). Since \(\theta_{x,x}-\theta_{y,y}=\theta_{x-y,x}+\theta_{y,x-y}\) has norm at most \(\|x-y\|(\|x\|+\|y\|)\),
\[
\begin{gathered}
\|V_m-(\hat h-\hat k)\|\\
\le\sum_{n>m}|c_n|+\sum_{n\le m}|c_n|\,\frac1m\Big(2+\frac1m\Big)\to0 .
\end{gathered}
\]
So \(\|h_m-\hat h\|\to0\), and by the estimate after (11.1), \(W_m(t)\to\hat W(t)\) in norm for each fixed \(t\).

*Step 3: the approximants have wave operators.* Let \(\zeta\in D\). Since \(e^{-is\hat k}\zeta\in H_{\mathrm{ac}}(\hat k)\) and \(f^{(m)}_n-g^{(m)}_n=\hat f_n-g_n\) is orthogonal to \(H_{\mathrm{ac}}(\hat k)\),
\[
\langle e^{-is\hat k}\zeta,f^{(m)}_n\rangle=\langle e^{-is\hat k}\zeta,g^{(m)}_n\rangle ,
\]
which is integrable in \(s\) by Lemma 11.16(ii). Hence \(\|V_me^{-is\hat k}\zeta\|\le\sum_{n\le m}|c_n|\,\|f^{(m)}_n\|\,|\langle e^{-is\hat k}\zeta,g^{(m)}_n\rangle|\) is integrable, and by Cook's criterion the limit \(W_{m,+}\zeta=\lim_tW_m(t)\zeta\) exists for every \(\zeta\in H_{\mathrm{ac}}(\hat k)\).

*Step 4: a uniform estimate.* Fix \(\zeta\in D\), and let \(M\) bound its spectral density (Lemma 11.16(i)). Put \(\eta_n(t)=\int_t^\infty|\langle e^{-is\hat k}\zeta,\hat f_n\rangle|^2ds\) and \(\eta(t)=\sum_n|c_n|\eta_n(t)\). By Lemma 11.13, \(\eta_n(t)\le2\pi M\); each \(\eta_n(t)\to0\) as \(t\to\infty\); and by dominated convergence \(\eta(t)\to0\). As in Step 3, \(\langle e^{-is\hat k}\zeta,\hat f_n\rangle=\langle e^{-is\hat k}\zeta,g_n\rangle\), so
\[
\begin{gathered}
\int_t^\infty|\langle e^{-is\hat k}\zeta,f^{(m)}_n\rangle|^2ds\\
=\int_t^\infty|\langle e^{-is\hat k}\zeta,g_n+(g^{(m)}_n-g_n)\rangle|^2ds\\
\le2\eta_n(t)+2\cdot2\pi M\,m^{-2},
\end{gathered}
\]
using Lemma 11.13 for the second part. Lemma 11.15(d) for the pair \((h_m,\hat k)\), together with \(\sum_{n\le m}|c_n|\,\|f^{(m)}_n\|^2\le4\|V\|_1\), gives
\[
\begin{gathered}
\|W_{m,+}\zeta-W_m(t)\zeta\|^2\\
\le\delta_m(t)^2\\
:=4(2\pi M)^{1/2}\|V\|_1^{1/2}\\
{}\cdot\big(2\eta(t)+4\pi M\|V\|_1m^{-2}\big)^{1/2}.
\end{gathered}
\]

*Step 5: passing to the limit.* For \(t,t'\in\mathbb R\), \(\|W_m(t)\zeta-W_m(t')\zeta\|\le\delta_m(t)+\delta_m(t')\). Let \(m\to\infty\) with \(t,t'\) fixed. By Step 2,
\[
\begin{gathered}
\|\hat W(t)\zeta-\hat W(t')\zeta\|\\
\le\delta(t)+\delta(t'),\\
\delta(t)^2\\
=4(2\pi M)^{1/2}\|V\|_1^{1/2}(2\eta(t))^{1/2}.
\end{gathered}
\]
Since \(\delta(t)\to0\) as \(t\to\infty\), \(\hat W(t)\zeta\) is a Cauchy net and converges. By Step 1, \(W_+(h,k):=\lim_te^{ith}e^{-itk}P_{\mathrm{ac}}(k)\) exists.

*Step 6: the conclusion.* Since \(k-h=-V\) is also of trace class, \(W_+(k,h)=\lim_te^{itk}e^{-ith}P_{\mathrm{ac}}(h)\) exists as well. By Lemma 11.15, \(W_+(h,k)\) maps \(H_{\mathrm{ac}}(k)\) isometrically into \(H_{\mathrm{ac}}(h)\), and \(W_+(k,h)\) maps \(H_{\mathrm{ac}}(h)\) isometrically into \(H_{\mathrm{ac}}(k)\). For \(\zeta\in H_{\mathrm{ac}}(k)\),
\[
\begin{gathered}
e^{itk}e^{-ith}\,W_+(h,k)\zeta-\zeta\\
=e^{itk}e^{-ith}\big(W_+(h,k)\zeta-e^{ith}e^{-itk}\zeta\big)\to0,
\end{gathered}
\]
and \(W_+(h,k)\zeta\in H_{\mathrm{ac}}(h)\); so \(W_+(k,h)W_+(h,k)\zeta=\zeta\). In the same way \(W_+(h,k)W_+(k,h)\eta=\eta\) for \(\eta\in H_{\mathrm{ac}}(h)\). Hence \(W_+(h,k)\) maps \(H_{\mathrm{ac}}(k)\) onto \(H_{\mathrm{ac}}(h)\): it is a partial isometry with these initial and final spaces, and \(hW_+=W_+k\) by Lemma 11.15(b). Restricted to \(H_{\mathrm{ac}}(k)\) it is a unitary onto \(H_{\mathrm{ac}}(h)\) carrying \(k_{\mathrm{ac}}\) to \(h_{\mathrm{ac}}\). For \(t\to-\infty\), apply the result to \(-h\) and \(-k\): \(e^{it(-h)}e^{-it(-k)}=e^{-ith}e^{itk}\), and \(H_{\mathrm{ac}}(-h)=H_{\mathrm{ac}}(h)\) because reflection preserves null sets. \(\square\)

**Remark 11.17** (trace class cannot replace Hilbert–Schmidt). If \(H\) has an orthonormal basis of eigenvectors of a self-adjoint \(k\), then \(H_{\mathrm s}(k)\) contains this basis (Proposition 11.6) and is closed, so \(H_{\mathrm{ac}}(k)=0\). If moreover \(h-k\) is of trace class, Theorem 11.12 gives \(H_{\mathrm{ac}}(h)\cong H_{\mathrm{ac}}(k)=0\). So a self-adjoint operator \(h\) with a nonzero absolutely continuous part is never a diagonal operator plus a trace-class operator. Self-adjointness of the two summands is no restriction here: if \(h=d_\lambda+x\) as in Example 2.2, with \(x\) of trace class, then also \(h=\frac12(h+h^*)=d_{\operatorname{Re}\lambda}+\frac12(x+x^*)\), and \(d_{\operatorname{Re}\lambda}\) is self-adjoint with the basis as eigenvectors. For instance, multiplication by \(t\) on \(L^2(0,1)\) is absolutely continuous (Proposition 11.9); by Theorem 11.2 it is a diagonal operator plus a self-adjoint Hilbert–Schmidt operator of arbitrarily small Hilbert–Schmidt norm, but it is not a diagonal operator plus a trace-class operator of any size.

### Diagonalization with a Schatten perturbation

For a compact operator set \(N_p(x)=(\sum_ns_n(x)^p)^{1/p}\), allowing infinity. The next proof uses approximation numbers and scalar Minkowski; it does not assume completeness or a triangle inequality for the operator quantity \(N_p\).

**Proposition 11.18 (Kuroda's extension).** If \(1<p<\infty\), \(H\) is separable, \(h\in B(H)_{\mathrm{sa}}\), and \(\varepsilon>0\), there are a self-adjoint compact operator \(a\) with \(N_p(a)<\varepsilon\) and a self-adjoint diagonal operator \(k\) such that \(h=k+a\).

*Proof.* We first justify the series estimate needed for the construction. For compact \(x_1,\ldots,x_N\), put \(\lambda_j=2^{-j}\) and
\(k_j(n)=\lfloor\lambda_j(n-1)\rfloor+1\).
Since \(\sum_{j=1}^N\lambda_j<1\),
\(\sum_j(k_j(n)-1)\leq n-1\).
Choose operators of rank at most \(k_j(n)-1\) approximating \(x_j\) within \(s_{k_j(n)}(x_j)+\delta\), using the approximation formula (2.2) in Proposition 2.5. Their sum has rank at most \(n-1\); applying that formula again and letting \(\delta\downarrow0\) gives
\[
s_n\left(\sum_{j=1}^Nx_j\right)
\leq\sum_{j=1}^Ns_{k_j(n)}(x_j).
\]
Each integer value of \(k_j(n)\) occurs exactly \(2^j\) times as \(n\) runs through the positive integers. Scalar Minkowski, Theorem 3.1 of the measure-tools lesson for counting measure, therefore yields
\[
N_p\left(\sum_{j=1}^Nx_j\right)
\leq\sum_{j=1}^N2^{j/p}N_p(x_j).
\]
If \(\sum_j2^{j/p}N_p(x_j)<\infty\), then \(\sum_j\|x_j\|<\infty\), since \(\|x_j\|=s_1(x_j)\leq N_p(x_j)\). The operator-norm sum \(x\) is compact. Proposition 2.5(d) gives convergence of every singular value of the partial sums to that of \(x\). Taking any finite number of singular values, passing to the limit, and then taking their supremum proves
\[
N_p(x)\leq\sum_j2^{j/p}N_p(x_j).
\]

Now refine Lemma 11.1. With its notation, \(y_j=y_jp_j\) has norm at most \(r/m\), its initial space lies in \(p_jH\), and its range lies in \(e_jH\). The initial spaces and ranges are each mutually orthogonal. Hence, for \(b=(1-p)hp=\sum_jy_j\),
\[
\begin{gathered}
\|b\zeta\|^2\\
=\sum_j\|y_jp_j\zeta\|^2
\\
\leq(r/m)^2\sum_j\|p_j\zeta\|^2
\\
\leq(r/m)^2\|\zeta\|^2.
\end{gathered}
\]
Thus \(\|b\|\leq r/m\) and \(\operatorname{rank}b\leq m\). The self-adjoint off-diagonal correction \(b+b^*\) has rank at most \(2m\) and norm at most \(2r/m\), so
\[
N_p(b+b^*)\leq2^{1+1/p}r\,m^{1/p-1}.
\]
For \(p>1\) this tends to zero as \(m\to\infty\).

Repeat the projection construction of Theorem 11.2, choosing the integer \(m\) at its \(j\)-th step large enough that the resulting correction satisfies
\(N_p(a_j)\leq\varepsilon 2^{-j(1+1/p)-2}\).
The compressed self-adjoint operator has norm at most \(\|h\|\), so the preceding bound permits this choice; a zero compression gives correction zero. The finite-rank projections still contain the successive members of a dense sequence and the same block identity (ii) holds. The series estimate gives an operator-norm sum \(a=\sum_ja_j\), self-adjoint and compact, with
\[
N_p(a)\leq\sum_j2^{j/p}N_p(a_j)
\leq\frac\varepsilon4\sum_{j=1}^\infty2^{-j}
=\frac\varepsilon4<\varepsilon.
\]
For \(k=h-a\), the block identity passes to the operator-norm limit. Each finite-dimensional block reduces \(k\), their orthogonal sum is \(H\), and the compact self-adjoint spectral theorem on each block supplies an orthonormal eigenbasis. Their union diagonalizes \(k\), exactly as in Theorem 11.2. \(\square\)

The restriction \(p>1\) is essential: the exponent \(1/p-1\) becomes zero at \(p=1\), and Remark 11.17 gives a spectral obstruction to trace-class diagonalization. A human reference is S. T. Kuroda, *On a theorem of Weyl–von Neumann*, 1958.


## 12. Exercises

**Exercise 12.1** (medium; the adjoint on normal operators). Show that the adjoint is strongly continuous on the set of normal operators: if \(x_\alpha\) and \(x\) are normal and \(x_\alpha\to x\) strongly, then \(x_\alpha^*\to x^*\) strongly. Compare with Proposition 8.6(b).

*Solution.* For a normal operator \(y\), \(\|y^*\xi\|^2=\langle yy^*\xi,\xi\rangle=\langle y^*y\xi,\xi\rangle=\|y\xi\|^2\). Hence
\[
\begin{gathered}
\|(x_\alpha^*-x^*)\xi\|^2\\
=\|x_\alpha\xi\|^2-2\operatorname{Re}\langle x_\alpha^*\xi,x^*\xi\rangle+\|x^*\xi\|^2\\
=\|x_\alpha\xi\|^2-2\operatorname{Re}\langle\xi,x_\alpha x^*\xi\rangle+\|x\xi\|^2 .
\end{gathered}
\]
As \(x_\alpha\to x\) strongly, \(\|x_\alpha\xi\|\to\|x\xi\|\) and \(x_\alpha x^*\xi\to xx^*\xi\). So the right side tends to \(2\|x\xi\|^2-2\langle\xi,xx^*\xi\rangle=2\|x\xi\|^2-2\|x^*\xi\|^2=0\). The operators \(\theta_{\xi_1,\xi_n}\) of Example 8.4(b) are not normal, so there is no contradiction.

**Exercise 12.2** (medium; cyclicity of the trace for Hilbert–Schmidt operators). Let \(x,y\in\mathcal L^2(H)\). Show that \(xy\) and \(yx\) are of trace class and that \(\operatorname{Tr}(xy)=\operatorname{Tr}(yx)\), although neither \(x\) nor \(y\) need be of trace class.

*Solution.* Both products are of trace class by Proposition 4.9(b). Fix an orthonormal basis \((\varepsilon_i)\). By Parseval,
\[
\begin{gathered}
\operatorname{Tr}(xy)\\
=\sum_i\langle y\varepsilon_i,x^*\varepsilon_i\rangle\\
=\sum_i\sum_j\langle y\varepsilon_i,\varepsilon_j\rangle\langle x\varepsilon_j,\varepsilon_i\rangle ,
\end{gathered}
\]
and in the same way \(\operatorname{Tr}(yx)=\sum_j\sum_i\langle x\varepsilon_j,\varepsilon_i\rangle\langle y\varepsilon_i,\varepsilon_j\rangle\). The double family is absolutely summable, since by Cauchy–Schwarz and (3.1) its absolute sum is at most \[
\begin{gathered}
(\sum_{i,j}|\langle y\varepsilon_i,\varepsilon_j\rangle|^2)^{1/2}(\sum_{i,j}|\langle x\varepsilon_j,\varepsilon_i\rangle|^2)^{1/2}\\
=\|y\|_2\|x\|_2.
\end{gathered}
\] So the two iterated sums agree. The Volterra operator \(V\) of Example 3.5 is Hilbert–Schmidt but not of trace class, and \(V^*V\) is of trace class.

**Exercise 12.3** (medium; the diagonal algebra and its predual). Let \((\varepsilon_i)_{i\in I}\) be an orthonormal basis and \(\mathcal D=\{d_\lambda:\lambda\in\ell^\infty(I)\}\) (Example 2.2). Show that \(\mathcal D\) is \(\sigma\)-weakly closed, that \(\omega\mapsto(\omega(d_{\delta_i}))_i\) is an isometric isomorphism of \(\mathcal D_*\) onto \(\ell^1(I)\), and that on the unit ball of \(\mathcal D\) the \(\sigma\)-weak topology is the topology of coordinatewise convergence of \(\lambda\).

*Solution.* An operator \(x\) lies in \(\mathcal D\) exactly when \(\langle x\varepsilon_i,\varepsilon_j\rangle=0\) for all \(i\ne j\): then \(x\varepsilon_i=\langle x\varepsilon_i,\varepsilon_i\rangle\varepsilon_i\) and \(x=d_\lambda\) with \(\lambda_i=\langle x\varepsilon_i,\varepsilon_i\rangle\), \(|\lambda_i|\le\|x\|\). So \(\mathcal D\) is the intersection of the kernels of the \(\sigma\)-weakly continuous functionals \(\omega_{\varepsilon_i,\varepsilon_j}\), \(i\ne j\). For \(\omega\in B(H)_*\) with \(t=t_\omega\), computing the trace in the basis \((\varepsilon_i)\) gives \(\omega(d_\lambda)=\operatorname{Tr}(d_\lambda t)=\sum_i\lambda_i\alpha_i\) with \(\alpha_i=\langle t\varepsilon_i,\varepsilon_i\rangle=\omega(d_{\delta_i})\), and \(\sum_i|\alpha_i|\le\|t\|_1\) by Theorem 4.6. Since \(\|d_\lambda\|=\|\lambda\|_\infty\), the norm of \(\omega|_{\mathcal D}\) is the norm of the functional \(\lambda\mapsto\sum_i\lambda_i\alpha_i\) on \(\ell^\infty(I)\). This is \(\|\alpha\|_1\): it is at most \(\|\alpha\|_1\), and its restriction to \(c_0(I)\) already has norm \(\|\alpha\|_1\) by Example 5.1(a). Every \(\alpha\in\ell^1(I)\) arises, from \(t=d_\alpha\). By Theorem 9.4(a) the elements of \(\mathcal D_*\) are the restrictions \(\omega|_{\mathcal D}\), so \(\omega|_{\mathcal D}\mapsto\alpha\) is an isometric isomorphism onto \(\ell^1(I)\). On the unit ball, \(\sigma\)-weak convergence \(d_{\lambda^\beta}\to d_\lambda\) means \(\sum_i\lambda^\beta_i\alpha_i\to\sum_i\lambda_i\alpha_i\) for all \(\alpha\in\ell^1(I)\); for a bounded net this holds as soon as it holds for \(\alpha\in c_{00}(I)\), which is dense, that is, for coordinatewise convergence.

**Exercise 12.4** (medium; the shift). Let \(S\) be the unilateral shift on \(\ell^2\). Show that \(S\) is a strong limit of unitary operators, so that the unitary group is not strongly closed, but that \(\|S-u\|\ge1\) for every unitary \(u\).

*Solution.* Let \(u_n\) be the unitary with \(u_n\delta_j=\delta_{j+1}\) for \(j\le n\), \(u_n\delta_{n+1}=\delta_1\), and \(u_n\delta_j=\delta_j\) for \(j>n+1\). For a finitely supported \(\xi\), \(u_n\xi=S\xi\) as soon as \(n\) exceeds its support. Since all these operators have norm one and finitely supported vectors are dense, \(u_n\to S\) strongly. For a unitary \(u\), \(\|S-u\|=\|u^*S-1\|\). The operator \(u^*S\) is an isometry whose range \(u^*(S\ell^2)\) is a proper subspace, so it is not invertible and \(0\) lies in its spectrum. Then \(-1\) lies in the spectrum of \(u^*S-1\), and the norm of an operator is at least its spectral radius (lesson [Banach algebras, spectrum, holomorphic functional calculus and Gelfand theory](banach-algebras-spectrum-holomorphic-functional-calculus-and-gelfand-theory.md)). So \(\|S-u\|\ge1\).

**Exercise 12.5** (easy; the trace is not weak\(^*\) continuous). Let \((\xi_n)\) be an orthonormal sequence. Show that \(\theta_{\xi_n,\xi_n}\to0\) in the weak\(^*\) topology \(\sigma(\mathcal L^1(H),K(H))\) that comes from Theorem 5.2, while \(\operatorname{Tr}(\theta_{\xi_n,\xi_n})=1\). Conclude that the trace is not continuous for this topology on the unit ball of \(\mathcal L^1(H)\), although this ball is compact for it.

*Solution.* For \(x\in K(H)\), \(\operatorname{Tr}(x\theta_{\xi_n,\xi_n})=\langle x\xi_n,\xi_n\rangle\to0\) by (4.4) and Lemma 2.1, while \(\operatorname{Tr}(\theta_{\xi_n,\xi_n})=\|\xi_n\|^2=1\) and \(\|\theta_{\xi_n,\xi_n}\|_1=1\). So the trace is not continuous on the unit ball, which is compact by the Banach–Alaoglu theorem and Theorem 5.2. The trace is the pairing with \(1\in B(H)\), and \(1\notin K(H)\) when \(H\) is infinite-dimensional.

## Where this leads

- *Von Neumann algebras.* The next lesson, [The double commutant theorem](the-double-commutant-theorem.md), shows that a nondegenerate \(*\)-algebra of operators equals its bicommutant exactly when it is closed in at least one of the six topologies of Section 8, and that it is then closed in all of them. Theorem 9.4 then makes every von Neumann algebra the dual of its predual. The order-theoretic meaning of normal functionals is treated in [The universal enveloping von Neumann algebra of a C\*-algebra, and W\*-algebras](the-universal-enveloping-von-neumann-algebra-of-a-c-star-algebra-and-w-star-algebras.md).
- *Another construction of the predual.* The lesson *Concrete preduals from Hilbert tensors* of the course *Modular theory and weights* builds the predual of a von Neumann algebra as a quotient of the completed projective tensor product of \(H\) with its conjugate space, and proves the continuous-dual statements of Theorem 9.1(ii) in that setting. The lesson *Detecting normal weights by finite observations* in the same course uses Theorem 9.1 and Theorem 9.6. It also uses the description of the \(\sigma\)-strongly and \(\sigma\)-weakly continuous real-linear functionals on the self-adjoint part of a von Neumann algebra \(M\); Corollary 9.7(c) gives this description for \(M=B(H)\).
- *Schatten classes.* For \(1\leq p<\infty\), the symmetric solid subspace \(\ell^p\subset c_0\) corresponds under Theorem 7.7 to the ideal of compact operators with \(\sum_ns_n(x)^p<\infty\). These ideals increase with \(p\): an \(\ell^p\) sequence is bounded, and \(\sum|s_n|^q\leq\|s\|_\infty^{q-p}\sum|s_n|^p\) for \(q>p\). The cases \(p=1,2\) are the trace and Hilbert–Schmidt classes. Proposition 11.18 gives the full proof that Theorem 11.2 extends to every finite \(p>1\), while Remark 11.17 gives the obstruction at \(p=1\). 

## References

- [van Neerven] J. van Neerven, *Functional Analysis*, [corrected author version, arXiv:2112.11166v7](https://arxiv.org/pdf/2112.11166v7).
- [Blackadar] B. Blackadar, *Operator Algebras: Theory of C*-Algebras and von Neumann Algebras*, [revised author edition, 8 February 2017](https://www.bruceblackadar.com/Mathematics/Cycr.pdf).

*Freely accessible reading:* [Jesse Peterson, *Notes on operator algebras*, §§3.1–3.4](https://math.vanderbilt.edu/peters10/teaching/spring2015/OperatorAlgebras.pdf) gives a route through trace duality and operator topologies; the compact-operator duality exercise and Krein–Šmulian are proved here. The lesson includes its own complete proofs at the stated hypotheses; references to human sources do not imply permission to adapt their expression.
