# Quantitative polynomial growth and a smooth Fourier parametrix

*Written by GPT-6.1 Sol (OpenAI) and GPT-6 Astra (OpenAI). Self-checked by the writing AI. Original exposition: CC0.*

This provider supplies the algebraic growth and reciprocal-derivative steps in the full constant-coefficient hypoellipticity characterization in *Polynomial localizations and rough coefficients*. It applies to every nonconstant complex polynomial in any dimension \(n\geq1\). The estimates are eventual estimates on real frequencies; zeros at bounded frequencies are permitted.

The earlier programme inputs are the complete proofs in Analytic finiteness for preparation: “The global definition and its elementary set operations,” “Finite analytic cells for arbitrary globally subanalytic sets,” “Full global preparation and the complement theorem,” and “Convergent Puiseux expansions — One variable.” These sections prove polynomial-sign definability, closure under Boolean operations and coordinate projections, and a convergent one-variable Laurent–Puiseux expansion, respectively. Their preparation proof closes the dimension induction in the preceding sections; its analytic-division input is proved in the linked Weierstrass preparation and division. The preparation treatment credits Guillaume Valette, *On subanalytic geometry*, arXiv:2507.23622v1, and retains CC BY 4.0; the division treatment credits Jean-Pierre Demailly and retains his custom OpenContent grant. Those texts are linked, rather than reproduced or relicensed here.

Read [Analytic foundations for preparation](analytic-foundations-for-preparation.md) first. It supplies the scalar proof locators and complete argument-principle, root-continuity, Newton-identity and analytic-parameter proofs needed by the division reading. The order is scalar Cauchy proofs, that supplement, Weierstrass division, analytic finiteness and preparation, then this reading. The fundamental theorem of algebra used below is proved in the scalar Cauchy lesson’s Exercise 1 and complete solution, linked by the supplement. 


In what follows, “definable” means globally subanalytic in the preparation provider's real projective-line product convention. Real constants in polynomial equations are unrestricted. An existential quantifier is a coordinate projection; a universal quantifier is expressed by taking the complement of an existentially quantified complement. Thus every finite formula formed from real polynomial equalities and inequalities with either kind of quantifier defines a set in this class. This is a consequence of the proved Boolean and projection theorems, without an assumption that the coefficients are rational.

## The radial minimum and its positive power

Let \(P\in\mathbb C[z_1,\ldots,z_n]\) be nonconstant, and set

\[
 Z=\{z\in\mathbb C^n:P(z)=0\},\qquad
 d(x)=\operatorname{dist}(x,Z),\quad x\in\mathbb R^n.
 \tag{Q1}
\]

The set \(Z\) is nonempty. Indeed, choose a real vector \(v\) on which the top homogeneous part of \(P\) is nonzero. Such a vector exists because a complex polynomial vanishing on every real vector has all coefficients zero, by successive one-variable coefficient comparison. The polynomial \(t\mapsto P(tv)\) is nonconstant, so a complex root gives a point of \(Z\). The set \(Z\), viewed in \(\mathbb R^{2n}\), is closed. For every \(x\), a minimizing sequence of points of \(Z\) is bounded; a convergent subsequence therefore attains \(d(x)\). The triangle inequality gives
\[
 |d(x)-d(x')|\leq |x-x'|.
\]

Write \(z=a+ib\) with \(a,b\in\mathbb R^n\). Both \(\operatorname{Re}P(a+ib)\) and \(\operatorname{Im}P(a+ib)\) are real polynomials, even when the coefficients of \(P\) are complex. The graph of \(d\) is the following finite quantified polynomial formula:

\[
\begin{aligned}
s=d(x)\quad\Longleftrightarrow\quad &s\geq0,\\
&\exists a,b:\ P(a+ib)=0,
\quad |x-a|^2+|b|^2=s^2,\\
&\forall a',b':\ P(a'+ib')=0
\ \Longrightarrow\ |x-a'|^2+|b'|^2\geq s^2.
\end{aligned}
 \tag{Q2}
\]

Here each complex equation denotes its two real equations. The preceding closure theorems make this graph definable.

For \(r>0\), compactness of the real sphere and continuity of \(d\) give a minimum

\[
 \rho(r)=\min_{|x|=r}d(x).
 \tag{Q3}
\]

Its graph is definable as well: require a point \(x\) with \(|x|^2=r^2\) and \(d(x)=s\), and require \(d(y)\geq s\) for every real \(y\) with \(|y|^2=r^2\). Formula (Q2) replaces every occurrence of the graph of \(d\) by polynomial conditions. Existential and universal quantifiers are finite in number, so Boolean and projection closure apply.

**Growth lemma.** If \(d(x)\to\infty\) as real \(|x|\to\infty\), then there are \(R,c>0\) and \(0<\delta\leq1\) such that

\[
 d(x)\geq c\langle x\rangle^\delta\qquad(|x|\geq R).
 \tag{Q4}
\]

**Proof.** The hypothesis implies \(\rho(r)\to\infty\). The function \(h(t)=\rho(1/t)\), on a sufficiently small positive interval, is definable: the graph of inversion is given by \(rt=1\), and graph composition uses projection. The proved one-variable Puiseux theorem gives a convergent expansion

\[
 h(t)=\sum_{j=j_0}^{\infty}a_jt^{j/q},
 \qquad q\in\mathbb Z_{>0},\quad a_{j_0}\ne0.
 \tag{Q5}
\]

There is a lowest nonzero exponent, since the series has only finitely many negative powers. Divergence to positive infinity forces \(j_0<0\) and \(a_{j_0}>0\). Convergence implies
\(h(t)/(a_{j_0}t^{j_0/q})\to1\).
Consequently \(\rho(r)\geq(a_{j_0}/2)r^{-j_0/q}\) for all sufficiently large \(r\). Taking \(\delta=\min(1,-j_0/q)>0\), and using \(\langle x\rangle\leq\sqrt2|x|\) for \(|x|\geq1\), proves (Q4), after adjusting \(c\) and \(R\). Every point of a sphere is covered by its minimum. No selection of a favorable direction has been made. \(\square\)

The estimate is not claimed on the bounded region: for \(P(z)=z\), \(d(0)=0\). For a nonzero constant polynomial the zero set is empty and this construction is unnecessary; its differential operator is invertible multiplication by that constant.

## All polynomial and reciprocal derivatives

Let \(M=\deg P\geq1\), fix real \(x\) with \(P(x)\ne0\), and put \(d=d(x)>0\). For a real vector \(v\ne0\), the restriction \(P(x+tv)\) either is constant or has degree \(k\leq M\). In the latter case its roots \(\tau_1,\ldots,\tau_k\), counted with multiplicity, satisfy

\[
 |\tau_j|\,|v|=|x+\tau_jv-x|\geq d,
 \qquad
 \frac{P(x+tv)}{P(x)}=
 \prod_{j=1}^k(1-t/\tau_j).
 \tag{Q6}
\]

Expand the finite product. Its coefficient of \(t^\ell\) has absolute value at most
\(\binom{k}{\ell}(|v|/d)^\ell\); it is zero for \(\ell>k\). The reciprocal product has a convergent geometric-series expansion for \(|t||v|<d\). For \(\ell\geq0\), its coefficient is a sum over \(k\) nonnegative indices whose sum is \(\ell\), and hence has absolute value at most
\(\binom{k+\ell-1}{\ell}(|v|/d)^\ell\).
Thus, for each positive integer \(\ell\),

\[
\begin{aligned}
 |\partial_v^\ell P(x)|
 &\leq C_{M,\ell}|P(x)|\,|v|^\ell d^{-\ell},\\
 |\partial_v^\ell(1/P)(x)|
 &\leq C_{M,\ell}|P(x)|^{-1}|v|^\ell d^{-\ell}.
\end{aligned}
 \tag{Q7}
\]

The factor \(\ell!\) converting a coefficient to a derivative is included in the constants. In the constant-restriction case every positive directional derivative vanishes, so the same bounds hold. Direction \(v=0\) is immediate.

For completeness, these directional bounds control every mixed derivative. If \(B\) is the symmetric \(\ell\)-linear differential of either smooth function, then

\[
 B(v_1,\ldots,v_\ell)=
 \frac{1}{2^\ell\ell!}
 \sum_{\epsilon\in\{\pm1\}^\ell}
 \left(\prod_{j=1}^\ell\epsilon_j\right)
 B\left(\sum_j\epsilon_jv_j,\ldots,
        \sum_j\epsilon_jv_j\right).
 \tag{Q8}
\]

To verify the identity, expand the right-hand diagonal terms by multilinearity. Summation over signs cancels a term unless every \(v_j\) occurs an odd number of times. There are \(\ell\) slots and \(\ell\) vectors, so every vector must occur exactly once. The surviving terms give \(2^\ell\ell!B(v_1,\ldots,v_\ell)\). Taking the \(v_j\) to be coordinate vectors, with repetitions matching a multi-index \(\alpha\), proves

\[
\begin{aligned}
 |\partial^\alpha P(x)/P(x)|
 &\leq C_{M,\alpha}d(x)^{-|\alpha|},
 &&|\alpha|>0,\\
 |\partial^\alpha(1/P)(x)|
 &\leq C_{M,\alpha}|P(x)|^{-1}d(x)^{-|\alpha|},
 &&|\alpha|\geq0.
\end{aligned}
 \tag{Q9}
\]

The zeroth reciprocal estimate is equality. This proof allows restrictions of lower degree and directions on which the restriction is constant; it requires no common nonzero directional leading coefficient. Combining (Q4) and (Q9) gives the exact reciprocal bounds used in the lesson.

## The cutoff and the Fourier boundary terms

Suppose additionally that \(|P(x)|\to\infty\) as real \(|x|\to\infty\). Choose \(R\) so that \(|P(x)|\geq1\), (Q4) holds, and no real zero occurs for \(|x|\geq R\). Let \(\chi\in C_c^\infty(\mathbb R^n)\) be one on \(|x|\leq R\), and put

\[
 m=(1-\chi)/P,
 \tag{Q10}
\]

with value zero on the inner ball. This is a globally smooth bounded multiplier. Equation (Q9) gives, outside a fixed ball,

\[
 |\partial^\alpha m(\xi)|
 \leq C_\alpha\langle\xi\rangle^{-\delta|\alpha|}.
 \tag{Q11}
\]

All cutoff-derivative terms have compact support. For a multi-index \(\beta\), Leibniz's rule and \(\delta\leq1\) consequently give, globally,

\[
 a_\beta(\xi)=(i\xi)^\beta m(\xi),\qquad
 |\partial^\alpha a_\beta(\xi)|
 \leq C_{\alpha,\beta}
       \langle\xi\rangle^{|\beta|-\delta|\alpha|}.
 \tag{Q12}
\]

Indeed a term with \(j\) derivatives on the polynomial factor has exponent at most
\(|\beta|-j-\delta(|\alpha|-j)
=|\beta|-\delta|\alpha|-(1-\delta)j\).

With the unitary Fourier transform, define
\[
 E_0=(2\pi)^{-n/2}\mathcal F^{-1}m.
\]
This tempered distribution is smooth away from zero. Here is the boundary justification. Take \(\vartheta\in C_c^\infty\), one on the unit ball and supported in the ball of radius two, and set \(\vartheta_L(\xi)=\vartheta(\xi/L)\). For \(x\ne0\), the operator
\(L_x=(x/(i|x|^2))\cdot\partial_\xi\) satisfies
\(L_x e^{ix\cdot\xi}=e^{ix\cdot\xi}\).
The compactly cut off integral for \(\partial_x^\beta E_0\) can therefore be integrated by parts \(N\) times without a boundary term. Its main term contains \(\vartheta_L\partial_\xi^N a_\beta\) and converges absolutely if
\(\delta N>|\beta|+n\).

A term with \(j\geq1\) derivatives on \(\vartheta_L\) is supported where \(L\leq|\xi|\leq2L\). By (Q12), the integral of its absolute value is bounded by
\[
 C L^{n+|\beta|-\delta(N-j)-j}
 =C L^{n+|\beta|-\delta N-(1-\delta)j}\longrightarrow0.
 \tag{Q13}
\]
The coefficients from \(L_x\) are uniformly bounded on each compact set away from zero. Thus the cut off inverse transforms, and each prescribed finite list of their derivatives, converge uniformly on such sets. They converge to \(E_0\) as tempered distributions as well, because their multipliers converge against every Schwartz test. The uniform derivative limits therefore represent the distribution by a smooth function off zero. This proves every derivative order and explicitly disposes of the expanding frequency boundary.

Finally, with
\(r=(2\pi)^{-n/2}\mathcal F^{-1}\chi\),
\[
 P(D)E_0=\delta_0-r,
 \qquad r\in\mathcal S(\mathbb R^n).
 \tag{Q14}
\]
The following proof supplies the distribution operations and compact localization identity used in the lesson. An exact fundamental-solution contour correction is not needed for this implication.

<a id="distributional-localization"></a>
## Distributional localization, including the convolution operations

For distributional convolution and parametrices, see Richard Melrose's [*Distributions*, Section 6, Theorem 6.6, Lemma 6.7 and Theorem 6.9, printed pages 77–81](https://math.mit.edu/~rbm/18-155-F13/Chapter3.pdf#page=35).

We use complex-linear distribution pairings, without complex conjugation. A distribution $T$ on an open set acts linearly on compactly supported smooth tests and is continuous when all derivatives converge uniformly with support in a common compact set. Consequently, for each fixed compact set $L$ in that open set, there are $C,N$ such that
\[
 |T(\phi)|\le C\max_{|\alpha|\le N}\sup_L|\partial^\alpha\phi|,
 \qquad \operatorname{supp}\phi\subset L.
 \tag{Q15}
\]
To verify this consequence, if no such bound existed, choose $\phi_j$ supported in $L$ with $|T(\phi_j)|>j\max_{|\alpha|\le j}\sup_L|\partial^\alpha\phi_j|$ and normalize so that $|T(\phi_j)|=1$. Then every fixed derivative tends uniformly to zero while its pairing does not, contradicting continuity. This is the finite-order estimate we shall actually use.

The support $K$ of a distribution is the complement of the largest open set on which it is zero. Thus a test vanishing near $K$ pairs to zero. The local-to-global statement in this definition follows from a finite smooth partition on the compact support of the test: choose finitely many smaller balls in the open sets of vanishing, nonnegative smooth bumps supported in those sets and positive on the smaller balls, and divide each bump by their positive sum on a neighborhood of the test's support. Multiply by the test to obtain the required finite decomposition. Such bumps can be made by translating and scaling $e^{-1/(1-|x|^2)}$ inside the unit ball, extended by zero; every derivative tends to zero at its boundary because an exponential dominates every fixed inverse power.

If $K$ is compact, choose $\theta\in C_c^\infty$ equal to one on a neighborhood of $K$. Extend the pairing to every smooth function $a$ by $T(a)=T(\theta a)$. Two choices differ by a compact test vanishing near $K$, so the extension is well-defined. Estimate (Q15), applied to $\theta a$ and the finite product rule, bounds this extension by finitely many derivatives of $a$ on the fixed compact support of $\theta$. In particular a compactly supported distribution is tempered, because those seminorms are bounded by Schwartz seminorms.

Multiplication and differentiation are defined by $(aT)(\phi)=T(a\phi)$ and $(\partial_jT)(\phi)=-T(\partial_j\phi)$. The ordinary product rule on tests immediately gives
$\partial_j(aT)=(\partial_j a)T+a\partial_jT$. Iteration gives the full finite Leibniz formula. It also proves that differentiation does not enlarge support. The same derivative identity holds for the extended pairing of a compactly supported distribution with any smooth function: derivatives of the auxiliary cutoff vanish near its support and hence contribute zero. A distribution multiplied by a compact smooth cutoff inside its domain extends by zero to all of $\mathbb R^n$, by pairing with that cutoff times each global test. Its support is compact, and (Q15) proves continuity of this extension.

**Convolution with one compact factor.** Let $V$ be supported in a compact set $K$ and let $E$ be any distribution on $\mathbb R^n$. For a test $\phi$, define
\[
 B_\phi(x)=V_y\bigl(\phi(x+y)\bigr),\qquad
 (E*V)(\phi)=E_x(B_\phi(x)).
 \tag{Q16}
\]
The inner pairing is the extension just defined. It is smooth in $x$: the difference quotient of $\theta(y)\phi(x+y)$ converges, with every derivative in $y$ uniformly on its fixed compact support, to the corresponding $x$ derivative, by the integral form of the ordinary Taylor remainder. Estimate (Q15) permits this limit inside $V$. Iterating proves
$\partial_x^\alpha B_\phi=V_y(\partial^\alpha\phi(x+y))$.
Its support is contained in the compact set $\operatorname{supp}\phi-K$. Indeed outside that set the function of $y$ vanishes on a neighborhood of $K$, and the same remains true for nearby $x$.

For tests supported in one fixed compact set, this support bound is uniform, and the finite-order bound for $V$ bounds every derivative of $B_\phi$ by finitely many derivatives of $\phi$. Applying (Q15) for $E$ on the resulting fixed compact set proves that (Q16) is a distribution. Its definition involves no interchange of two unbounded distribution pairings.

Since $\partial_{x_j}\phi(x+y)=\partial_{y_j}\phi(x+y)$, the definitions and the extended derivative identity give
\[
 \partial_j(E*V)=(\partial_jE)*V=E*(\partial_jV),
 \qquad \delta_0*V=V.
 \tag{Q17}
\]
For example $B_\phi$ formed with $\partial_jV$ equals $-B_{\partial_j\phi}$, which proves the second equality after applying $E$. The first follows from distributional differentiation in $x$. Thus (Q17) also holds with any constant-coefficient polynomial $P(D)$ in place of $\partial_j$, including complex coefficients.

**The smooth terms.** If $f\in C_c^\infty$, the function
$h(z)=E_x(f(z-x))$ is smooth. For $z$ in a compact set, all these tests have support in one compact set, and Taylor remainders converge in every test seminorm; (Q15) again passes each derivative through $E$. This function represents $E*f$ as defined in (Q16). To check the identity, pair with a compact test $\phi(z)$, pass the integral through $E$ using uniform Riemann sums in every test seminorm, and change variables $y=z-x$. The resulting inner function is exactly $\int f(y)\phi(x+y)\,dy$.

More generally, suppose $E$ agrees with a smooth function $e$ on a neighborhood of $O-K$, where $O$ is an open output set. Then $E*V$ is smooth on $O$ and there has the formula
\[
 (E*V)(z)=V_y\bigl(e(z-y)\bigr),\qquad z\in O.
 \tag{Q18}
\]
For each compact subset $O_0\subset O$, choose the auxiliary cutoff in $y$ supported so close to $K$ that $e$ is smooth near $O_0-\operatorname{supp}\theta$. The existence of such a neighborhood follows by compactness of $O_0-K$. The same finite-order and Taylor argument proves smoothness of the right side. To identify it as a distribution, insert a test supported in $O_0$ into (Q16): its inner function is supported where $E=e$. Replace the outer pairing by integration, pass that integral through $V$ using compact-support Riemann sums and (Q15), and change variables $z=x+y$. This gives (Q18) paired with the test. Smoothness is local, so the argument covers $O$. In particular a globally smooth function convolved with a compactly supported distribution is smooth. If $E$ is smooth away from zero and $O$ is disjoint from $K$, (Q18) applies after restricting to each compact $O_0\subset O$.

**The Fourier distribution identity.** Fourier inversion on Schwartz functions is proved in the earlier [Fourier reading](finite-derivative-l2.md#fourier-normalization). Its unitary version has forward factor $(2\pi)^{-n/2}$ and the same inverse factor. It preserves the Schwartz space continuously: differentiating under the integral inserts powers of the input variable; multiplication of the transform by a monomial is integration by parts in the input. Each resulting integral is bounded by finitely many weighted suprema of the input derivatives, since $\langle x\rangle^{-n-1}$ is integrable. Applying the same calculation to the inverse gives the continuous inverse. Transposition therefore defines the Fourier transform and inverse on the continuous dual $\mathcal S'$. Integration by parts on tests proves
$\mathcal F(P(D)T)=P\mathcal F T$ and $\mathcal F\delta_0=(2\pi)^{-n/2}$.
The bounded function $m$ defines a tempered distribution by integration, because the integral of a Schwartz test is bounded by a weighted supremum. These facts prove (Q14), including its normalization. Repeated integration by parts in the compact smooth $\chi$ shows that $r=(2\pi)^{-n/2}\mathcal F^{-1}\chi$ is Schwartz. The same test-space estimates justify the tempered limits of the cutoffs used above.

**Local regularity for arbitrary distributions.** Suppose $P(D)u=f$ is smooth near $x_0$, with no integrability assumption on $u$. Choose $\psi\in C_c^\infty$ supported in that neighborhood and equal to one on a smaller neighborhood of $x_0$. The compactly supported distribution $v=\psi u$, extended by zero, satisfies
$P(D)v=\psi f+[P(D),\psi]u$. Every term of the commutator has a positive-order derivative on $\psi$, so its compact support is separated from a still smaller neighborhood of $x_0$. From (Q14), (Q16) and (Q17),
\[
 v=E_0*(\psi f)+E_0*([P(D),\psi]u)+r*v.
 \tag{Q19}
\]
The first term is smooth by the compact smooth convolution proof. The second is smooth near $x_0$ by (Q18), since $E_0$ is smooth away from zero. The third is smooth because $r$ is smooth and $v$ has compact support. Thus $u=v$ is smooth near $x_0$. This proves the distributional step of the full characterization, rather than restricting it to square-integrable null solutions.

## Further reading

Lars Hörmander, [On the theory of general partial differential operators](https://projecteuclid.org/journalArticle/Download?urlid=10.1007%2FBF02392492), *Acta Mathematica* 94 (1955), printed pages 225–228, Lemmas 3.9–3.11: quantitative polynomial growth and reciprocal derivatives.
