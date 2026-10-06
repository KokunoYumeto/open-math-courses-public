# Local regularity, sharp embeddings, and compactness

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026. Self-checked by GPT-6.1 Sol (OpenAI). Public domain (CC0).*

Weighted Fourier norms are global. An equation on an open set needs norms that ignore growth at infinity and near the boundary. Smooth cutoffs make that localization possible. They also give a way to prove that our embedding conditions are necessary: a fixed compactly supported function, moved to high frequency, tests the weight at the frequency where it is placed.

The prerequisite lesson is [Measuring regularity with weighted Fourier spaces](weighted-fourier-spaces.md). We also use the Banach closed graph theorem, Arzelà–Ascoli, and smooth compact cutoffs on open subsets of Euclidean space. Grubb [Grubb] and Melrose [Melrose] give background. The functional-analytic proofs used here are the linked internal closed-graph and compact-limit arguments. All weights and Fourier normalizations are those of the preceding lesson. Write \(p'\) for the conjugate exponent, including the endpoints.

[Continuous functionals, test families and compact limits](continuous-functionals-and-test-families.md), Section 3, proves the compact subsequence arguments. The closed graph theorem is [Banach estimates, quotient spaces and compact parameter arguments](../prerequisites/banach-foundation-bridges.html), Section 14.5, and the cutoff construction is [Metric and topological foundations](../prerequisites/metric-foundation-bridges.html), Section 13.10.

## Modulation reads a weight at one point

Fix a nonzero \(\phi\in C_c^\infty(\mathbb R^n)\), and set \(\phi_\eta(x)=e^{i\eta\cdot x}\phi(x)\). The Fourier transform is \(\widehat\phi(\xi-\eta)\). For every moderate weight \(k\),
\[
c_{\phi,k,p}k(\eta)\leq\|\phi_\eta\|_{p,k}
\leq C_{\phi,k,p}k(\eta),
\tag{1}
\]
where the constants are positive, finite, and independent of \(\eta\).

To prove this, put \(h=\xi-\eta\) and use
\[
\frac{k(\eta)}{M_k(-h)}\leq k(\eta+h)\leq k(\eta)M_k(h).
\]
The upper constant is \((2\pi)^{-n/p}\|M_k\widehat\phi\|_p\); the lower constant is \((2\pi)^{-n/p}\|\widehat\phi/M_k(-\cdot)\|_p\). Both are finite because \(\widehat\phi\) is Schwartz and \(M_k\) has polynomial growth. The lower constant is nonzero because Fourier inversion shows \(\widehat\phi\ne0\). The same reasoning uses essential suprema when \(p=\infty\).

## Which weighted inclusions are possible?

**Theorem 2.1.** For moderate weights \(k_1,k_2\), the following are equivalent:

1. \(k_1\leq Ck_2\) everywhere for some finite \(C\).
2. \(B_{p,k_2}\) is continuously included in \(B_{p,k_1}\).
3. On some nonempty open set \(X\), every compactly supported distribution in \(B_{p,k_2}\) with support in \(X\) also belongs to \(B_{p,k_1}\).

**Proof.** The first condition directly gives the norm bound in the second, and the second implies the third. Assume the third. Choose a closed ball \(K\subset X\) with positive radius. The space of \(B_{p,k_2}\) distributions supported in \(K\) is closed and hence Banach: convergence in \(B_{p,k_2}\) implies convergence in distributions, which preserves vanishing off \(K\). The inclusion into \(B_{p,k_1}\) has closed graph because both norms give distributional convergence to the same limit. The closed graph theorem therefore makes the inclusion bounded. Apply it to \(\phi_\eta\), for a fixed nonzero \(\phi\) supported in the interior of \(K\), and use (1). It follows that \(k_1(\eta)\leq Ck_2(\eta)\) for every \(\eta\). \(\square\)

In particular,
\[
B_{p,k_1}\cap B_{p,k_2}=B_{p,k_1+k_2},
\qquad
\max(\|u\|_{p,k_1},\|u\|_{p,k_2})
\leq\|u\|_{p,k_1+k_2}
\leq\|u\|_{p,k_1}+\|u\|_{p,k_2}.
\]
The two inequalities follow from pointwise comparison and Minkowski. They include the essential-supremum endpoint.

## The exact threshold for classical derivatives

**Theorem 3.1.** Let \(j\geq0\) be an integer. The condition
\[
\frac{(1+|\xi|)^j}{k(\xi)}\in L^{p'}(\mathbb R^n)
\tag{2}
\]
implies a continuous inclusion \(B_{p,k}\subset C_b^j(\mathbb R^n)\). Conversely, if every \(B_{p,k}\) distribution with compact support in some nonempty open set \(X\) is \(C^j\) on \(X\), then (2) holds. Here \(C_b^j\) has the norm given by the sum of the suprema of all derivatives of order at most \(j\).

**Proof of sufficiency.** For \(|\alpha|\leq j\), Hölder gives
\[
\int|\xi^\alpha\widehat u(\xi)|\,d\xi
\leq\|k\widehat u\|_p\|\xi^\alpha/k\|_{p'}.
\]
The inverse Fourier integrals of these functions converge absolutely. Dominated convergence makes them continuous, and differentiation in the distributional sense identifies them with \(D^\alpha u\). Their uniform bounds prove the continuous inclusion. \(\square\)

**Proof of necessity.** Choose \(\chi\in C_c^\infty(X)\) equal to one near a point \(x_0\). By the hypothesis, \(u\mapsto\chi u\) maps \(B_{p,k}\) into \(C_b^j(\mathbb R^n)\): its support is compactly contained in \(X\), so extension by zero introduces no boundary issue. Its graph is closed. Indeed convergence in the weighted norm gives distributional convergence, and convergence in \(C_b^j\) gives the same distributional limit. Thus the Banach closed graph theorem gives
\(\|\chi u\|_{C_b^j}\leq A\|u\|_{p,k}\).

Apply this to inverse transforms of smooth compactly supported frequency functions \(g\). Since \(\chi=1\) near \(x_0\), evaluation of the derivative there yields
\[
\left|\int e^{ix_0\cdot\xi}\xi^\alpha g(\xi)\,d\xi\right|
\leq A_\alpha\|kg\|_p,
\qquad |\alpha|\leq j.
\]
The converse form of Hölder's inequality now says \(\xi^\alpha/k\in L^{p'}\). This converse also covers both endpoints: an integral functional bounded on \(L^1\) has an essentially bounded density, and a density bounded as an integral functional on compactly supported \(L^\infty\) tests is integrable. Restrict first to finite frequency sets and approximate the required bounded tests by smooth functions there; continuity and strict positivity of \(k\) allow that approximation in the displayed integral. Let the sets increase to all of space. Finally, \((1+|\xi|)^j\) is bounded by a fixed constant times \(\sum_{|\alpha|\leq j}|\xi^\alpha|\), and the reverse comparison also holds. The finitely many conditions give (2). \(\square\)

**Example 3.2.** For \(k=\langle\xi\rangle^s\) and \(1<p\leq\infty\), condition (2) is exactly \(s>j+n/p'\). For \(p=1\), it is \(s\geq j\). The strict inequality in the former case comes from the logarithmic divergence at equality. At \(p=2\) this recovers the usual Sobolev threshold. At \(p=1\), integrability is already part of the Fourier norm, so equality is allowed.

## Compactness after fixing physical support

Let \(B_{p,k}(K)\) denote distributions in \(B_{p,k}\) supported in a fixed compact set \(K\).

**Theorem 4.1.** If
\[
\frac{k_1(\xi)}{k_2(\xi)}\longrightarrow0
\quad\text{as }|\xi|\longrightarrow\infty,
\tag{3}
\]
then the inclusion \(B_{p,k_2}(K)\to B_{p,k_1}\) is compact. Conversely, if this inclusion is compact for one compact \(K\) with nonempty interior, then (3) holds. The theorem includes \(p=\infty\).

**Proof of sufficiency.** Let \(u_l\) be bounded in \(B_{p,k_2}(K)\), and choose \(\psi\in C_c^\infty\) equal to one near \(K\). Since \(u_l=\psi u_l\),
\[
\widehat u_l=(2\pi)^{-n}\widehat\psi*\widehat u_l.
\]
Differentiate the smooth Schwartz kernel and apply Hölder. For every multiindex \(\beta\),
\[
|\partial^\beta\widehat u_l(\xi)|
\leq(2\pi)^{-n}\|k_2\widehat u_l\|_p
\left\|\frac{\partial^\beta\widehat\psi(\xi-\cdot)}{k_2(\cdot)}\right\|_{p'}.
\]
The last norm is uniformly bounded for \(\xi\) in any fixed ball, because \(1/k_2\) has polynomial growth and the kernel and all its derivatives are Schwartz. Thus the Fourier transforms are uniformly bounded and equicontinuous on every compact set. Arzelà–Ascoli and a diagonal selection give a subsequence converging uniformly on each compact frequency set.

Given \(\delta>0\), choose a ball outside which \(k_1/k_2\leq\delta\). On the ball, uniform convergence and boundedness of \(k_1\) imply convergence in weighted \(L^p\), including the supremum norm. Off the ball, the norm of a difference is at most \(\delta\) times its bounded \(k_2\)-norm. The subsequence is therefore Cauchy in \(B_{p,k_1}\), which is complete. This proves compactness. \(\square\)

**Proof of necessity.** Choose a nonzero \(\phi\in C_c^\infty(\operatorname{int}K)\). For any sequence \(|\eta_l|\to\infty\), put
\(u_l=e^{i\eta_l\cdot x}\phi(x)/k_2(\eta_l)\).
Equation (1) makes this a bounded sequence in \(B_{p,k_2}(K)\). It converges to zero in distributions: pairing with a test function produces the value of the rapidly decreasing Fourier transform of \(\phi\) times that test function at \(-\eta_l\), divided by a weight with a polynomial lower bound. Every convergent subsequence in \(B_{p,k_1}\) must therefore have limit zero. Compactness implies that the whole sequence tends to zero in that norm, since otherwise a subsequence bounded away from zero would have a convergent further subsequence. The lower bound in (1) gives
\(c k_1(\eta_l)/k_2(\eta_l)\leq\|u_l\|_{p,k_1}\to0\).
The original escaping sequence was arbitrary, so (3) follows. \(\square\)

## Passing to an open set

There is a general operation behind localization. Let \(F\subset\mathcal D'(X)\) be a linear subspace stable under multiplication by compactly supported smooth functions. Set
\[
F_{\mathrm{loc}}=\{u:\chi u\in F\text{ for every }\chi\in C_c^\infty(X)\}.
\]
Call a cutoff-stable space local if membership of all its localized products implies membership of the distribution itself.

**Lemma 5.0.** The space \(F_{\mathrm{loc}}\) is the smallest local space containing \(F\). Its compactly supported elements are exactly the compactly supported elements of \(F\). For any local space \(G\), membership is also determined point by point: if each \(x\) has a cutoff \(\chi_x\) nonzero at \(x\) with \(\chi_xu\in G\), then \(u\in G\).

**Proof.** Cutoff stability gives \(F\subset F_{\mathrm{loc}}\) and stability of \(F_{\mathrm{loc}}\). To see that it is local, suppose \(\chi u\in F_{\mathrm{loc}}\) for every cutoff. For a particular \(\chi\), choose \(\psi=1\) near its support. Then \(\chi u=\psi(\chi u)\in F\), proving \(u\in F_{\mathrm{loc}}\). Any local space containing \(F\) contains \(F_{\mathrm{loc}}\) by its defining membership rule. If \(u\) is compactly supported, a cutoff equal to one near its support gives \(u=\chi u\), proving the equality of the compactly supported parts.

For the pointwise assertion, fix a compactly supported cutoff \(\psi\). Choose finitely many of the \(\chi_x\) such that \(S=\sum_l|\chi_l|^2>0\) on a neighborhood of \(\operatorname{supp}\psi\). The smooth compactly supported multipliers \(a_l=\psi\overline{\chi_l}/S\), extended by zero off that neighborhood, satisfy \(\psi u=\sum_l a_l(\chi_lu)\in G\). Locality gives \(u\in G\). \(\square\)

For an open \(X\subset\mathbb R^n\), define
\[
B_{p,k}^{\mathrm{loc}}(X)=
\{u\in\mathcal D'(X):\chi u\in B_{p,k}\text{ for every }
\chi\in C_c^\infty(X)\}.
\]
The product \(\chi u\) is extended by zero to all of space. Give this space the seminorms \(u\mapsto\|\chi u\|_{p,k}\).

**Theorem 5.1.** This is a Fréchet space. Multiplication by every \(a\in C^\infty(X)\) is continuous. The inclusion into \(\mathcal D'(X)\) is continuous, and \(C^r(X)\) is continuously included for some finite integer \(r\) depending on the weight. A compactly supported element of the local space belongs to the global space, and on distributions supported in a fixed compact \(K\subset X\) the local and global topologies agree.

**Proof.** Choose compact sets \(K_l\subset\operatorname{int}K_{l+1}\) exhausting \(X\), and cutoffs \(\chi_l\) equal to one near \(K_l\), with support in \(\operatorname{int}K_{l+1}\). Every seminorm is bounded by a constant times one of the countable seminorms \(\|\chi_lu\|_{p,k}\): if \(\operatorname{supp}\chi\subset K_l\), then \(\chi u=\chi(\chi_lu)\), and the cutoff estimate from the preceding lesson applies. These seminorms separate distributions, so they define a metrizable Hausdorff locally convex topology.

For completeness, let \(u_j\) be Cauchy in all those seminorms. Write \(v_l=\lim_j\chi_lu_j\) in the global Banach space. For a test function \(\varphi\) supported in \(K_l\), define \(\langle u,\varphi\rangle=\langle v_l,\varphi\rangle\). The definition is unchanged on enlarging \(l\), by distributional convergence of the same pairings \(\langle u_j,\varphi\rangle\). It defines a distribution because, on every fixed compact test support, the pairing is that of one distribution \(v_l\). For any cutoff \(\chi\), take \(l\) with \(\chi_l=1\) near its support. Then \(\chi u=\chi v_l\), and the global cutoff estimate proves both membership and convergence in its seminorm. Thus the local space is complete.

For a smooth multiplier, choose \(\psi=1\) near \(\operatorname{supp}\chi\). Then \(\chi au=(\chi a)(\psi u)\), and \(\chi a\) is a compactly supported smooth multiplier. This proves continuity. Distributional continuity follows from the global inclusion applied to a cutoff equal to one near each test support. If \(k(\xi)\leq A\langle\xi\rangle^N\), choose an integer \(r>N+n\). Integration by parts gives
\(\langle\xi\rangle^r|\widehat{\chi f}(\xi)|\leq C\sum_{|\alpha|\leq r}\|\partial^\alpha(\chi f)\|_1\)
for \(f\in C^r(X)\). It follows that \(\|\chi f\|_{p,k}\) is bounded by a finite \(C^r\) seminorm for every \(p\). Finally, a cutoff equal to one near \(K\) recovers a distribution supported in \(K\) itself; in the other direction all local seminorms are bounded by its global norm. \(\square\)

**Proposition 5.2.** The weight comparison in Theorem 2.1 is also necessary and sufficient for
\(B_{p,k_2}^{\mathrm{loc}}(X)\subset B_{p,k_1}^{\mathrm{loc}}(X)\)
on any nonempty open \(X\). Condition (2) is necessary and sufficient for
\(B_{p,k}^{\mathrm{loc}}(X)\subset C^j(X)\).
Condition (3) is necessary and sufficient for every bounded subset of \(B_{p,k_2}^{\mathrm{loc}}(X)\) to be precompact in \(B_{p,k_1}^{\mathrm{loc}}(X)\).

**Proof.** The first two sufficiencies follow after applying the global results to a cutoff equal to one near each point. Their necessities follow by considering compactly supported distributions in a ball contained in \(X\). For the compactness sufficiency, apply Theorem 4.1 to \(\chi_lu_j\) on its fixed compact support and choose subsequences successively for \(l=1,2,\ldots\). A diagonal subsequence is Cauchy in every target seminorm, so Theorem 5.1 gives its limit. Both local spaces are metrizable; this sequential argument characterizes relative compactness. Conversely, the global unit ball with support in a fixed ball is bounded locally, and local convergence on that fixed support is global convergence. Theorem 4.1 then gives (3). \(\square\)

**Proposition 5.3.** For nonzero \(Q\),
\(Q(D):B_{p,k}^{\mathrm{loc}}(X)\to B_{p,k/S_Q}^{\mathrm{loc}}(X)\)
is continuous. If \(u\in B_{p,k_1}^{\mathrm{loc}}(\mathbb R^n)\) has compact support and \(v\in B_{\infty,k_2}^{\mathrm{loc}}(\mathbb R^n)\), then
\(u*v\in B_{p,k_1k_2}^{\mathrm{loc}}(\mathbb R^n)\).

**Proof.** For a cutoff \(\chi\), choose \(\psi=1\) near its support. Locally there, \(Q(D)u=Q(D)(\psi u)\). The global differential bound followed by multiplication by \(\chi\) proves the first claim. In the second claim \(u\) belongs globally to \(B_{p,k_1}\). Choose \(\psi=1\) near the compact set \(\operatorname{supp}\chi-\operatorname{supp}u\). Then \(u*v=u*(\psi v)\) near \(\operatorname{supp}\chi\). The global convolution and cutoff bounds prove the result. \(\square\)

Countable intersections of these local spaces, with all their seminorms, are again Fréchet by the same completeness argument. In particular,
\[
C^\infty(X)=\bigcap_{r=0}^\infty B_{\infty,\langle\xi\rangle^r}^{\mathrm{loc}}(X).
\]
Smooth localized functions have rapidly decreasing transforms, giving one inclusion. The derivative criterion with arbitrarily large \(r\) gives the other.

## Exercises with solutions

**Exercise 1 (entry).** On a fixed compact set with nonempty interior, when is the inclusion from \(B_{p,\langle\xi\rangle^s}\) to \(B_{p,\langle\xi\rangle^t}\) bounded, and when is it compact?

**Solution.** Their weight ratio is \(\langle\xi\rangle^{t-s}\). It is bounded precisely when \(t\leq s\), and tends to zero precisely when \(t<s\). Theorems 2.1 and 4.1 give the two assertions. Nonempty interior is needed for the necessity argument using a nonzero test function.

**Exercise 2 (intermediate).** Prove that \(k(\xi_1,\xi_2)=\langle\xi_1\rangle^{7/4}\langle\xi_2\rangle^{7/4}\) gives \(B_{2,k}^{\mathrm{loc}}(\mathbb R^2)\subset C^1\). Explain how its two exponents relate to an isotropic weight.

**Solution.** Take \(k(\xi_1,\xi_2)=\langle\xi_1\rangle^a\langle\xi_2\rangle^b\), with \(a,b>3/2\). Since \(1+|\xi|\leq C(\langle\xi_1\rangle+\langle\xi_2\rangle)\), the squared integrability in (2) follows from the separate integrability of \(\langle\xi_1\rangle^{2-2a}\langle\xi_2\rangle^{-2b}\) and its counterpart with the exponent two on the second variable. One may choose \(a=b=7/4\), whereas an isotropic weight \(\langle\xi\rangle^s\) in dimension two needs \(s>2\). These are different weights: this comparison does not assert an inclusion based on a single common numerical order.

**Exercise 3 (intermediate).** Why can Theorem 4.1 not omit the requirement of fixed physical support? Use \(k_2=\langle\xi\rangle\), \(k_1=1\), \(p=2\).

**Solution.** Choose a nonzero compactly supported smooth \(\phi\) and translate it by integer multiples of a vector long enough that the supports are disjoint. Translation multiplies its Fourier transform by a phase and preserves both norms, so the sequence is bounded in \(B_{2,k_2}\). Its members have pairwise \(L^2=B_{2,1}\) distance \(\sqrt2\|\phi\|_2\), so it has no convergent subsequence there. The frequency ratio tends to zero, but physical mass escapes to infinity.

**Exercise 4 (advanced).** Let \(k_1/k_2\to0\). Show that a sequence bounded in \(B_{p,k_2}^{\mathrm{loc}}(X)\) and converging in distributions to \(u\) converges to \(u\) in \(B_{p,k_1}^{\mathrm{loc}}(X)\).

**Solution.** Proposition 5.2 gives relative compactness in the target space. Every target-convergent subsequence has the same distributional limit \(u\), by continuity into distributions, so \(u\) belongs to the target space. If the original sequence failed to converge there, some target seminorm and a subsequence would stay at a positive distance from \(u\). Relative compactness would give a further convergent subsequence, whose limit must be \(u\), contradicting that positive distance. Thus the whole sequence converges.

## References

- [Grubb] Gerd Grubb, *Distributions and Operators*, open lecture-note versions, 2007–2008, Fourier and Sobolev sections. [Author's lecture-note index](https://web.math.ku.dk/~grubb/distribution.htm).
- [Melrose] Richard Melrose, *Differential Analysis*, MIT OpenCourseWare, Fall 2004, sections on Sobolev spaces and compactness. [Open course](https://ocw.mit.edu/courses/18-155-differential-analysis-fall-2004/).
- Internal closed graph theorem: [Banach estimates, quotient spaces and compact parameter arguments](../prerequisites/banach-foundation-bridges.html#section-14-5), Section 14.5, with the target-seminorm estimate.
- Internal compact-limit argument: [Continuous functionals, test families and compact limits](continuous-functionals-and-test-families.md), Proposition 3.1 and its following compact-frequency-ball adapter.
- Internal cutoff construction: [Metric and topological foundations](../prerequisites/metric-foundation-bridges.html#section-13-10), Section 13.10.
