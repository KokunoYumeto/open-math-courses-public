# Locality forces continuity

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, September 2026. Checked once by GPT-6.1 Sol (OpenAI), Ultra reasoning effort. Public domain (CC0).*

*Source/proof self-check and prerequisite integration by GPT-6 Astra (OpenAI), Ultra, October 2026. Historical authorship and component terms are retained.*

An operator may be declared linear without being declared continuous. Ordinarily that leaves room for wild behavior on sequences. Locality removes that freedom when every output is smooth: an operator cannot amplify disjoint, increasingly small tests without making the output of one smooth test unbounded. This observation supplies the missing continuity hypothesis in the diagonal-kernel theorem and gives Peetre's characterization of differential operators.

The preceding [kernel lesson](distributions-as-kernels.md) supplies test-space topology, support localization, compact smooth partitions and the kernel theorem. The [jet lesson](jets-supported-distributions-and-local-operators.md), Theorem 4.1 and Corollary 4.2, supplies the local differential expression, uniqueness, smooth coefficients and strong continuity on distributions once weak continuity has been established. The [complete integral Taylor proof](when-a-kernel-is-smooth.md#taylor-estimates-on-compact-neighborhoods) supplies the vanishing-jet estimates below. The supplied [scalar foundation](../prerequisites/U011-free-foundations/metric-foundation-bridges.md), §§12–13, proves compactness, cutoffs, the fundamental theorem and, in §13.7, uniform limits and termwise differentiation of smooth series. The [measure foundation](../prerequisites/U011-free-foundations/banach-foundation-bridges.md), §§15.0–15.1, provides the integral pairing. We prove the scalar Euclidean statement with no continuity assumption, including every continuity conclusion, by a local estimate followed by the already proved kernel results. The exact source comparisons at the end distinguish the punctured estimate from the step filling its missing point.

## Knowing only the germ

Let \(X\subset\mathbb R^n\) be open, with \(n\ge1\). Consider a linear map

\[
T:\mathcal D(X)\longrightarrow C^\infty(X)
\]

satisfying

\[
\operatorname{supp}T\phi\subset\operatorname{supp}\phi
\quad(\phi\in\mathcal D(X)).
\tag{1.1}
\]

Each output consequently has compact support. At this stage no continuity of the map \(T\) is assumed; smoothness is a property of each individual output.

If two tests agree on an open set \(W\), their difference vanishes on \(W\), so its image vanishes there by (1.1). Thus their outputs agree on \(W\). The value \(T\phi(x)\) depends only on the germ of \(\phi\) at \(x\), meaning its values on any sufficiently small neighborhood of \(x\). It need not yet be known to depend on a finite jet.

This germ property extends \(T\) uniquely to all smooth functions. Given \(f\in C^\infty(X)\) and \(x\in X\), choose a test cutoff \(\chi\) equal to one near \(x\), and define

\[
\widetilde Tf(x)=T(\chi f)(x).
\tag{1.2}
\]

Two choices give the same value by germ dependence. On a neighborhood where \(\chi=1\), formula (1.2) equals the smooth function \(T(\chi f)\), so the resulting function is smooth. Linearity, support preservation and agreement with the original \(T\) follow locally. The extension is unique among germ-dependent extensions, because its value at \(x\) must be determined by any cutoff representative of the germ.

The proof of continuity will use compact tests. For such a test, put

\[
\|\phi\|_m=\max_{|\alpha|\le m}\sup_X|\partial^\alpha\phi|,
\quad m=0,1,\ldots.
\]

The same notation for a continuous compact output at \(m=0\) means its global supremum. In particular, \(\|T\phi\|_0\) is finite for every individual test.

## Amplifying disjoint tests would break smoothness

**Lemma 2.1 (a bound away from one point).** For each \(p\in X\), there are a relatively compact neighborhood \(U\) of \(p\), an integer \(m\ge0\) and \(C>0\) such that

\[
\|T\phi\|_0\le C\|\phi\|_m
\quad\big(\phi\in\mathcal D(U\setminus\{p\})\big).
\tag{2.1}
\]

**Proof.** Suppose that the assertion fails at \(p\). Fix a relatively compact neighborhood \(U_0\) of \(p\). We will construct tests \(f_j\) and open sets \(O_j\), for \(j\ge1\), with the following properties:

\[
\begin{gathered}
\operatorname{supp}f_j\subset O_j,\qquad
\overline{O_j}\subset U_0\setminus\{p\},\qquad
\overline{O_j}\cap\overline{O_i}=\varnothing\quad(i\ne j),\\
O_j\subset B(p,1/j),\qquad
\|Tf_j\|_0>4^j\|f_j\|_j.
\end{gathered}
\tag{2.2}
\]

At step \(j\), the earlier closures avoid \(p\). There is therefore a neighborhood \(V_j\) of \(p\) inside \(U_0\cap B(p,1/j)\) which avoids all those closures. Failure of the lemma, with order \(j\) and constant \(4^j\), supplies an \(f_j\in\mathcal D(V_j\setminus\{p\})\) satisfying the last inequality. Choose \(O_j\) around its compact support, with closure in \(V_j\setminus\{p\}\). This gives (2.2). The test is nonzero, so \(\|f_j\|_j>0\).

Normalize it by

\[
g_j=\frac{2^{-j}}{\|f_j\|_j}f_j.
\]

Then

\[
\|g_j\|_j=2^{-j},\qquad \|Tg_j\|_0>2^j.
\tag{2.3}
\]

For every fixed derivative order \(r\), the tail \(j\ge r\) has summable \(C^r\) norms. Hence

\[
g=\sum_{j\ge1}g_j
\tag{2.4}
\]

is a smooth function, with termwise derivatives of every order. To justify this familiar convergence criterion directly, the series of each derivative of order at most \(r\) converges uniformly. Passing to the limit in the fundamental theorem of calculus along coordinate segments identifies those limits as successive derivatives of the uniformly convergent function series. This works for every \(r\). All supports lie in the fixed compact set \(\overline{U_0}\subset X\), so \(g\in\mathcal D(X)\).

On \(O_j\), every other summand vanishes. Thus \(g=g_j\) there, and the germ property gives \(Tg=Tg_j\) there. The compact smooth function \(Tg_j\) is supported in \(\operatorname{supp}g_j\subset O_j\). Its supremum is attained at some \(x_j\in O_j\), since (2.3) makes it nonzero. Therefore

\[
|Tg(x_j)|=\|Tg_j\|_0>2^j.
\]

But \(Tg\) is a continuous function with compact support, and must be bounded. This is a contradiction. No interchange of \(T\) with the infinite sum was used: only equality of germs on each \(O_j\) was used. \(\square\)

The puncture at \(p\) lets us place each new support away from all previous ones. We next fill that puncture without assuming the continuity we are trying to prove.

## Filling the puncture with a finite jet

**Lemma 3.1 (the same bound for a vanishing jet).** Suppose \(U,m,C\) satisfy Lemma 2.1. If \(u\in\mathcal D(U)\) and

\[
\partial^\alpha u(p)=0\quad(|\alpha|\le m),
\tag{3.1}
\]

then \(\|Tu\|_0\le C\|u\|_m\).

**Proof.** Take a fixed smooth cutoff \(\chi\), equal to one near zero and compactly supported in the unit ball. For small \(\varepsilon>0\), put

\[
u_\varepsilon(x)=\big(1-\chi((x-p)/\varepsilon)\big)u(x).
\]

This belongs to \(\mathcal D(U\setminus\{p\})\) and equals \(u\) outside a shrinking neighborhood of \(p\). Taylor's formula at \(p\), using (3.1), gives

\[
|\partial^\gamma u(x)|
\le |x-p|^{m-|\gamma|}\omega(|x-p|)
\quad(|\gamma|\le m)
\]

near \(p\), with \(\omega(a)\to0\). For \(m=0\), this is simply continuity and \(u(p)=0\). The product rule and the bounds \(\partial^\beta\chi((x-p)/\varepsilon)=O(\varepsilon^{-|\beta|})\) show

\[
\|u_\varepsilon-u\|_m\longrightarrow0.
\tag{3.2}
\]

Apply (2.1) to \(u_\varepsilon-u_\delta\). It follows that \(Tu_\varepsilon\) is uniformly Cauchy. To make the limiting step explicit, for each \(x\) completeness of \(\mathbb C\) gives a limit \(v(x)\) as \(\varepsilon\downarrow0\): first take any sequence of increments tending to zero and then use the Cauchy bound to see that the same limit holds for all small increments. In the uniform Cauchy inequality, let the second increment tend to zero at each point. The resulting bound on \(|Tu_\varepsilon(x)-v(x)|\) is independent of \(x\), so convergence is uniform. A uniform limit of continuous functions is continuous: approximate the limit within a prescribed error by one fixed continuous member and use its continuity at the point in question. Thus \(v\) is continuous. At every \(x\ne p\), eventually \(u_\varepsilon\) agrees with \(u\) on a neighborhood of \(x\). Germ dependence yields \(Tu_\varepsilon(x)=Tu(x)\), and thus \(v(x)=Tu(x)\). Since both functions are continuous and \(p\) is approached by points different from \(p\), they also agree at \(p\). Consequently the uniform limit is exactly \(Tu\). Passing to the limit in (2.1) and (3.2) proves the desired bound. \(\square\)

**Proposition 3.2 (a local continuity estimate).** Every point has a relatively compact neighborhood \(U\), an integer \(m\) and \(A>0\) such that

\[
\|Tu\|_0\le A\|u\|_m
\quad(u\in\mathcal D(U)).
\tag{3.3}
\]

**Proof.** Use the \(U,m,C\) from Lemma 2.1, and choose \(\eta\in\mathcal D(U)\) equal to one near \(p\). Set

\[
Ju(x)=\eta(x)\sum_{|\alpha|\le m}
\frac{(x-p)^\alpha}{\alpha!}\partial^\alpha u(p).
\tag{3.4}
\]

The finite sum gives \(\|Ju\|_m\le A_1\|u\|_m\) for a fixed \(A_1\). Each of the finitely many smooth compact outputs

\[
T\left(\eta(x)(x-p)^\alpha/\alpha!\right)
\]

has a finite supremum. Their fixed suprema give \(\|TJu\|_0\le A_2\|u\|_m\). The test \(u-Ju\) has its \(m\)-jet zero at \(p\), so Lemma 3.1 gives

\[
\|Tu\|_0
\le C\|u-Ju\|_m+\|TJu\|_0
\le\big(C(1+A_1)+A_2\big)\|u\|_m.
\]

This proves (3.3). The finite-dimensional jet contribution was estimated using fixed individual outputs, with no continuity assumption on \(T\). \(\square\)

Cover a fixed compact input support \(K\subset X\) by finitely many neighborhoods from Proposition 3.2. Choose subordinate compact smooth cutoffs \(\theta_i\), whose sum is one near \(K\). For \(u\in\mathcal D_K(X)\),

\[
Tu=\sum_iT(\theta_i u).
\]

The product rule, the finite sum, and (3.3) imply

\[
\|Tu\|_0\le A_K\|u\|_{m_K},
\quad u\in\mathcal D_K(X),
\tag{3.5}
\]

where \(m_K\) is the largest of the finitely many local orders. Pairing \(Tu\) with an output test \(\psi\) now gives

\[
|\langle Tu,\psi\rangle|
\le\|\psi\|_{L^1}\,A_K\|u\|_{m_K}.
\]

Thus every scalar pairing is continuous on each fixed input support space. By the inductive-limit definition of \(\mathcal D(X)\), \(T:\mathcal D(X)\to\mathcal D'(X)\) is weakly continuous. We have obtained precisely the missing hypothesis for a distribution kernel.

## The differential expression and its continuity

**Theorem 4.1 (Peetre's theorem for smooth scalar outputs).** A linear map \(T:\mathcal D(X)\to C^\infty(X)\) satisfies (1.1) if and only if it has a unique expression

\[
T\phi=\sum_\alpha a_\alpha(x)\partial^\alpha\phi,
\quad a_\alpha\in C^\infty(X),
\tag{4.1}
\]

with locally finite coefficient family. It is then automatically continuous as a map \(\mathcal D(X)\to\mathcal D(X)\), as well as into \(C^\infty(X)\). Its germ extension \(\widetilde T:C^\infty(X)\to C^\infty(X)\) is continuous, and the same expression defines a continuous operator on all distributions for the strong distribution topology. Every relatively compact region has a finite order; one order for all of \(X\) is not required.

**Proof.** Assume (1.1). The preceding argument gives weak distributional continuity. Theorem 4.1 of the jet lesson therefore identifies \(T\) with a locally finite differential expression having distributional coefficients. Corollary 4.2 of that lesson uses its smooth outputs to prove that all coefficients are smooth. It also proves uniqueness and the strong continuity of the distribution extension. This establishes (4.1) and that part of the claim.

Here are the remaining continuity estimates. If \(\phi\) is supported in a compact \(K\), so is \(T\phi\). Only finitely many coefficients occur near \(K\); let \(q_K\) be their maximal degree. The product rule gives, for every \(r\ge0\),

\[
\|T\phi\|_r\le C_{K,r}\|\phi\|_{q_K+r},
\quad\phi\in\mathcal D_K(X).
\tag{4.2}
\]

The constants use the finitely many derivatives of the coefficients on \(K\). Thus each restriction \(\mathcal D_K(X)\to\mathcal D_K(X)\) is continuous. The inclusions of these support spaces into \(\mathcal D(X)\) are continuous, and the inductive-limit property proves continuity \(\mathcal D(X)\to\mathcal D(X)\). Inclusion into \(C^\infty(X)\) gives that claimed continuity too.

For arbitrary smooth \(f\), expression (4.1) is a locally finite sum, and its value depends on the germ of \(f\). It agrees with the extension in (1.2). On any compact output set \(L\), the same product estimate bounds every output derivative through order \(r\) by input derivatives through a finite order on \(L\). These are defining seminorms of \(C^\infty(X)\), so \(\widetilde T\) is continuous. Conversely, a locally finite smooth differential expression is linear, smooth on each smooth input, and support-preserving, by differentiation and multiplication not increasing support. Its continuity also follows from (4.2). \(\square\)

The theorem applies equally to a linear support-preserving map on all \(C^\infty(X)\): restrict it to tests, apply the theorem, and use germ dependence to identify its values with the extension. No continuity has to be supplied in either version. For a nonempty zero-dimensional open Euclidean space there is only one point and every scalar linear map is multiplication by a scalar; that elementary case needs no puncture argument.

It matters that the output is smooth. The proof of Lemma 2.1 used boundedness of one output function, and Lemma 3.1 used its continuity to fill the missing value. A general distribution is not a pointwise continuous function. Support preservation by itself does not license those steps for an arbitrary map with distributional outputs.

## Orders accumulating at an interior point

The jet lesson gives an operator whose order grows on bumps escaping to infinity. That is consistent with locally bounded order. A different outcome occurs if unbounded orders accumulate at an interior point.

For \(j\ge1\), put \(x_j=2^{-j}\) in \((-1,1)\), and take the pairwise disjoint intervals \(I_j=(x_j-2^{-j-3},x_j+2^{-j-3})\). Their closures avoid zero and all lie in the fixed compact set \([0,3/4]\). Choose smooth \(b_j\) supported in \(I_j\), equal to one near \(x_j\). The pointwise formal expression

\[
Pf(x)=\sum_{j\ge1}b_j(x)\partial^j f(x)
\tag{5.1}
\]

has at most one nonzero summand at every \(x\ne0\), and gives zero at \(x=0\). Nevertheless it fails to have continuous output for some compact smooth \(f\).

To exhibit one, let \(\chi=1\) near zero with compact support, and choose small positive \(\varepsilon_j\) so that

\[
f_j(x)=\frac{j}{j!}(x-x_j)^j
\chi((x-x_j)/\varepsilon_j)
\]

is supported in \(I_j\) and satisfies

\[
\|f_j\|_{\lfloor j/2\rfloor}\le2^{-j}.
\tag{5.2}
\]

Such a choice is possible: each derivative through order \(\lfloor j/2\rfloor\) is bounded by a constant, depending on \(j\), times a strictly positive power of \(\varepsilon_j\). On the other hand \(\partial^j f_j(x_j)=j\), independently of that scale.

The series \(f=\sum_j f_j\) converges in every derivative norm, since for fixed \(r\) the tail \(j\ge2r\) satisfies (5.2). It is compactly supported in \((-1,1)\), and all derivatives at zero are zero: each term vanishes near zero and derivatives can be passed through the uniformly convergent series. But \(Pf(x_j)=j\), while \(Pf(0)=0\). Thus (5.1) does not map every smooth test to a continuous function. Pointwise finiteness of an expression is weaker than local finiteness of its coefficient family.

## Exercises

**Exercise 1 (basic: germ localization).** Let \(T\) satisfy the hypotheses of Theorem 4.1 before continuity has been proved. Show that the extension (1.2) is compatible with restriction to an open subset \(W\subset X\). Explain why a single cutoff for all of \(W\) need not exist and is unnecessary.

**Exercise 2 (intermediate: why a sum need not be commuted).** In Lemma 2.1, justify \(Tg=Tg_j\) on \(O_j\) solely by support preservation and linearity. Identify the invalid inference that would result from writing \(Tg=\sum_jTg_j\) before continuity was proved.

**Exercise 3 (intermediate: the finite jet contribution).** Suppose a linear map \(S:\mathcal D(U)\to C^0(X)\) obeys \(\|Su\|_0\le C\|u\|_m\) for tests whose \(m\)-jet at \(p\) vanishes, and each output used below is bounded. Prove the same estimate, with a possibly larger constant, for every test in \(\mathcal D(U)\). Give an explicit possible constant in terms of a fixed cutoff \(\eta\), its polynomial jet representatives, and their images under \(S\).

**Exercise 4 (advanced: extracting the order from commutators).** For a smooth function \(h\), write \(M_h f=hf\) and \([T,M_h]=TM_h-M_hT\). Show that if \(T\) has order at most \(q\) on an open region, then each such commutator has order at most \(q-1\), where order at most \(-1\) means zero. Show that any \(q+1\) iterated commutators with smooth multipliers vanish there. For \(T=\partial^q\) on the line, compute the \(q\)-fold commutator with \(M_x\).

**Exercise 5 (advanced: a nonlinear local map).** The map \(N(f)=f^2\) sends smooth functions to smooth functions and preserves support. It is continuous in the smooth topology. Prove these assertions, and show that \(N\) cannot equal a linear differential expression on all smooth inputs. Explain which use of linearity in Lemma 2.1 fails if one tries to apply its normalization to \(N\).

## Solutions

**Solution 1.** For a smooth \(f\) on \(W\) and \(x\in W\), choose a cutoff compactly supported in \(W\) and equal to one near \(x\). Its product with \(f\) extends by zero to a test on \(X\). Apply \(T\), restrict its output to \(W\), and evaluate at \(x\). Two choices agree near \(x\), so the values are independent of the choices. On a neighborhood where one cutoff equals one, the result is the restriction of a single smooth output; therefore it is smooth. If \(f\) is the restriction of a global smooth function, the germ construction gives exactly \((\widetilde Tf)|_W\). This also proves compatibility with smaller open subsets. Compact cutoffs are needed only around each point. A noncompact \(W\) could not lie in a compact cutoff's region of value one, but the local definitions already agree on overlaps.

**Solution 2.** The smooth compact test \(g-g_j\) vanishes on \(O_j\), because all other summands are supported outside that set. Hence its support is disjoint from \(O_j\), and the support of \(T(g-g_j)\) is disjoint from \(O_j\) too. Linearity gives \(Tg-Tg_j=T(g-g_j)=0\) there. The infinite identity would require \(T\) to preserve the limit of partial sums. That is a continuity assertion and is unavailable at this point. Equality on each \(O_j\) uses a single difference of two already defined smooth tests, so it needs no such assertion.

**Solution 3.** Put \(e_\alpha(x)=\eta(x)(x-p)^\alpha/\alpha!\) for \(|\alpha|\le m\), and \(Ju=\sum_\alpha\partial^\alpha u(p)e_\alpha\). Write

\[
A=\sum_{|\alpha|\le m}\|e_\alpha\|_m,
\qquad B=\sum_{|\alpha|\le m}\|Se_\alpha\|_0.
\]

Each coefficient obeys \(|\partial^\alpha u(p)|\le\|u\|_m\). Thus \(\|Ju\|_m\le A\|u\|_m\) and \(\|SJu\|_0\le B\|u\|_m\). The jet of \(u-Ju\) vanishes through order \(m\). Linearity and the assumed bound give

\[
\|Su\|_0\le\big(C(1+A)+B\big)\|u\|_m.
\]

The constants are finite because there are finitely many fixed representatives. No topological hypothesis on \(S\) was introduced.

**Solution 4.** The product rule yields

\[
[T,M_h]f
=\sum_\alpha a_\alpha
\sum_{\substack{0<\beta\le\alpha}}
\binom\alpha\beta(\partial^\beta h)
\partial^{\alpha-\beta}f.
\]

Every surviving derivative on \(f\) has degree at most \(q-1\). If \(q=0\), the inner sums are empty and the commutator is zero. Iteration lowers the maximal degree one step at a time, so \(q+1\) such commutators vanish. On the line \([\partial^q,M_x]=q\partial^{q-1}\), since only the first derivative of \(x\) is nonzero. Repeating with \(M_x\) gives \(q!\) times the identity after \(q\) steps, and zero at the next step. This computation is local and does not require a global bound on the order of a locally finite operator.

**Solution 5.** The functions \(f\) and \(f^2\) have the same zero set, so their supports are equal. The product rule bounds every derivative of \(f^2-g^2=(f-g)(f+g)\) on a compact set by a constant times the corresponding derivative norm of \(f-g\), multiplied by a bounded derivative norm of \(f+g\). If \(g\to f\) in the smooth topology, these latter norms remain bounded on each compact set and each fixed derivative order. Hence \(g^2\to f^2\) in the same topology. A linear differential expression would satisfy \(T(2f)=2Tf\). Squaring gives \(N(2f)=4Nf\), contradicting that identity for any nonzero \(f\). In the normalization step of Lemma 2.1, linearity supplied \(T(cf_j)=cTf_j\), allowing input norm and output norm to scale by the same factor. For \(N\), those factors are \(|c|\) for the input and \(|c|^2\) for the output, so that step does not apply. Nonlinear local operators require a different theorem with different hypotheses.

## References

- The supplied [kernel lesson](distributions-as-kernels.md), [integral Taylor proof](when-a-kernel-is-smooth.md#taylor-estimates-on-compact-neighborhoods) and [jet lesson](jets-supported-distributions-and-local-operators.md) provide the exact earlier programme arguments used here. Foundational components retain their stated licences.
- [Steinbauer 2010] Roland Steinbauer, *Introduction to Partial Differential Operators on Manifolds and Normally Hyperbolic Operators*, Novi Sad Summer School, August 2010, §1.1, items 1.3–1.5, pp. 5–8. [Author-posted notes](https://mat.univie.ac.at/~stein/research/talks/nhops.pdf). The punctured estimate in the proof of item 1.5 is compared with Lemma 2.1. Our subsequent vanishing-jet approximation and finite jet contribution explicitly fill the puncture before weak continuity and the kernel theorem are used.
- [Kolář–Michor–Slovák 1993] Ivan Kolář, Peter W. Michor and Jan Slovák, *Natural Operations in Differential Geometry*, author's open electronic edition of the 1993 work, §19.1–19.2, pp. 176–177. [Open electronic edition](https://www.mat.univie.ac.at/~michor/kmsbookh.pdf). This gives the linear locality theorem and a different jet-based proof outline. The nonlinear extension theory later in that section is not needed for this lesson.
- [Dyatlov 2026] Semyon Dyatlov, *Lecture notes for 18.155: distributions, elliptic regularity, and applications to PDEs*, MIT, 2 October 2026, §7.2, pp. 80–83. [Open distribution notes](https://math.mit.edu/~dyatlov/18.155/155-notes.pdf). Background on the preceding kernel theorem.
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators I: Distribution Theory and Fourier Analysis*, second edition (1990), 2003 reprint, ISBN 978-3-642-61497-2, §5.2, Theorems 5.2.3–5.2.4, p. 131. The exact approved purchased copy supplies the diagonal-kernel and support comparison used through the preceding proved jet lesson; it is not a replacement for the continuity argument above. All five worked problems and the example with orders accumulating at an interior point are retained.
