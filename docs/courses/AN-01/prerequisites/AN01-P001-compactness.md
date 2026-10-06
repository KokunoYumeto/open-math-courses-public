# Compactness of continuous families: prerequisite proofs

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026. Independently written mathematical exposition; author self-check only. Public domain (CC0 1.0).*

This prerequisite proves the compactness and finite-net results used for smooth tests and short paths in AN-01. Its elementary bases are completeness of the real and complex numbers, finite-dimensional Euclidean norm estimates, compactness of Euclidean closed bounded sets, and ordinary differential calculus with the fundamental theorem of calculus. Compactness means that every open cover has a finite subcover. No function-space compactness theorem is assumed.

## AN01-CMP-001: Finite uniform nets

For a metric space \(K\), write \(B_K(x,r)=\{y\in K:d(x,y)<r\}\). A subset \(A\) of a metric space is **totally bounded** if, for every \(\varepsilon>0\), finitely many balls of radius \(\varepsilon\) cover it. A finite \(\varepsilon\)-net is their collection of centers. Centers can always be chosen in \(A\), at the cost of doubling the radius: discard balls missing \(A\), choose one point of \(A\) in each remaining ball, and use the triangle inequality.

Let \(E=\mathbb R^q\) or \(\mathbb C^q\), with its Euclidean norm, and let \(\mathcal F\subset C(K;E)\). The family is **pointwise bounded** if \(\sup_{f\in\mathcal F}|f(x)|<\infty\) for each \(x\in K\). It is **equicontinuous** if, for every \(x\in K\) and \(\eta>0\), there is \(r_x>0\) such that
\[
|f(y)-f(x)|<\eta
\quad(f\in\mathcal F,\ d(x,y)<r_x).
\]
The radius is common to the family, though initially it can depend on \(x\).

**Theorem 1 (finite uniform nets).** On a compact metric space \(K\), a pointwise bounded, equicontinuous family \(\mathcal F\) is uniformly bounded and totally bounded for
\[
\|f-g\|_\infty=\sup_{x\in K}|f(x)-g(x)|.
\]
Every finite net needed here can have its centers in \(\mathcal F\).

**Proof.** Empty sets cause no difficulty, so suppose \(K\) and \(\mathcal F\) are nonempty. Equicontinuity with \(\eta=1\) supplies balls about each point. A finite subcover with centers \(x_1,\ldots,x_N\) gives
\[
\sup_{f\in\mathcal F}\|f\|_\infty
\le 1+\max_{1\le i\le N}\sup_{f\in\mathcal F}|f(x_i)|<\infty.
\tag{CMP-1}
\]

Equicontinuity also becomes uniform in the spatial point. Given \(\eta>0\), choose \(r_x\) using \(\eta/2\), and cover \(K\) by finitely many balls \(B_K(x_i,r_{x_i}/2)\). Put \(\delta=\min_i r_{x_i}/2>0\). If \(d(y,z)<\delta\) and \(y\) belongs to one of these balls, both \(y,z\) lie in \(B_K(x_i,r_{x_i})\). Comparing their values to \(f(x_i)\) gives \(|f(y)-f(z)|<\eta\) for every \(f\).

Fix \(\varepsilon>0\) and put \(\eta=\varepsilon/5\). Choose such a \(\delta\), and then a finite spatial cover \(K=\bigcup_i B_K(x_i,\delta)\). By (CMP-1), all values lie in one bounded Euclidean cube. Choose a finite value grid \(Q\) within distance \(\eta\) of every point of that cube. For \(\mathbb R^q\), a coordinate grid with spacing at most \(\eta/\sqrt q\) suffices; for \(\mathbb C^q\), use its \(2q\) real coordinates.

For each \(f\), choose \(q_i\in Q\) with \(|f(x_i)-q_i|\le\eta\), resolving any ties by a fixed ordering of \(Q\). This gives finitely many possible patterns \((q_1,\ldots,q_N)\). For each pattern that occurs, select one actual member \(f_P\in\mathcal F\) realizing it. If \(f\) has that pattern and \(d(x,x_i)<\delta\), then
\[
\begin{aligned}
|f(x)-f_P(x)|
&\le |f(x)-f(x_i)|+|f(x_i)-q_i|\\
&\quad+|q_i-f_P(x_i)|+|f_P(x_i)-f_P(x)|\\
&<4\eta<\varepsilon.
\end{aligned}
\tag{CMP-2}
\]
The selected family members are the promised finite net. In particular, grid patterns do not have to be continuous functions or compatible derivative data. \(\square\)

## AN01-CMP-002: Completeness and compact closure

**Lemma 2 (the metric compactness facts used below).** A complete, totally bounded metric space is compact. A compact metric space is complete and every sequence in it has a convergent subsequence.

**Proof.** In a totally bounded space, cover successively by finite nets of radii \(2^{-m}\). From any sequence choose an infinite set \(I_1\) of indices in one first ball. From those indices choose an infinite subset \(I_2\) in one second ball, and continue with \(I_{m+1}\subset I_m\). Choose increasing \(j_m\in I_m\). For \(k,l\ge m\), both selected points belong to the same ball at stage \(m\), so their distance is less than \(2^{1-m}\). This is a Cauchy subsequence. Completeness gives its limit.

We now prove that the resulting sequential compactness implies open-cover compactness. First it implies total boundedness: if finitely many \(\varepsilon\)-balls never suffice, successive choices outside the previous balls give an infinite sequence whose distinct points are at least \(\varepsilon\) apart. It has no convergent subsequence. Second, every open cover has a **Lebesgue number** \(r>0\): every \(B(x,r)\) is contained in some member of the cover. Otherwise choose \(x_m\) whose ball of radius \(1/m\) has no such containment. A subsequence tends to \(x\); a cover member containing \(x\) contains \(B(x,2a)\) for some \(a>0\). Eventually \(d(x_m,x)<a\) and \(1/m<a\), contradicting that choice. A finite net of radius \(r\) now gives a finite subcover by choosing a cover member containing each net ball.

Conversely, a sequence in an open-cover compact space has a convergent subsequence. If it did not, each point would have some neighborhood containing only finitely many indices: infinitely many indices in every ball about a point would let us choose increasing indices converging to it. These neighborhoods cover the space, and a finite subcover would contain only finitely many indices in total, a contradiction. A Cauchy sequence therefore has a convergent subsequence; the triangle inequality makes the entire Cauchy sequence converge to that same limit. This proves completeness. \(\square\)

**Theorem 3 (Arzelà–Ascoli in the required form).** The space \(C(K;E)\) is complete in the supremum norm for compact metric \(K\). The closure of the family in Theorem 1 is compact in that norm. Consequently every sequence in that family has a uniformly convergent subsequence with a continuous limit.

**Proof.** Every continuous function on compact \(K\) is bounded: continuity gives a local bound near each point, and a finite cover gives a global one. For a supremum-norm Cauchy sequence \(f_j\), the values \(f_j(x)\) converge in the complete finite-dimensional space \(E\); call their limit \(f(x)\). Given \(\eta>0\), the Cauchy estimate \(\|f_j-f_l\|_\infty<\eta\) for large \(j,l\), followed by \(l\to\infty\) at each \(x\), gives \(\|f_j-f\|_\infty\le\eta\). Thus convergence is uniform. Continuity follows by comparing \(f(x),f(y)\) to one continuous \(f_j\), with each uniform error less than one third of the desired tolerance. This also makes \(f\) bounded, and proves completeness.

Let \(A=\overline{\mathcal F}\) in this norm. It is complete: a Cauchy sequence in \(A\) has a limit in \(C(K;E)\), and its approximation by elements of \(\mathcal F\), with the triangle inequality, puts that limit in \(A\). It is totally bounded: a finite \(\varepsilon/3\)-net for \(\mathcal F\) also covers \(A\) by balls of radius \(\varepsilon\), since every element of \(A\) is arbitrarily close to \(\mathcal F\). Lemma 2 gives compactness and explicitly constructs the required Cauchy subsequence from successive finite nets. \(\square\)

The real, complex and finite-vector conclusions all follow from the same proof. A finite product may equally use the maximum of its coordinate norms: if there are \(D\) coordinates, that maximum is at most the Euclidean product norm, which is at most \(\sqrt D\) times the maximum. Changing the finite-net tolerance by this factor gives the same conclusions.

## AN01-CMP-003: Smooth derivative nets

Let \(\Omega\subset\mathbb R^n\) be open, \(K\subset\Omega\) compact, and \(m\ge0\) an integer. For functions defined on a neighborhood of \(K\), put
\[
p_{K,m}(f)=\max_{|\alpha|\le m}\sup_{x\in K}|\partial^\alpha f(x)|.
\tag{CMP-3}
\]
This is the seminorm on restricted ambient derivatives meant here by a finite \(C^m\) net.

For empty \(K\), this seminorm is zero and the net assertion is immediate. In the neighborhood argument below assume \(K\ne\varnothing\).

**Corollary 4 (one further derivative gives a finite net).** Choose \(r>0\) so that the closed neighborhood
\[
N_r(K)=\{x\in\mathbb R^n:\operatorname{dist}(x,K)\le r\}
\]
is compact and contained in \(\Omega\). Suppose \(\mathcal B\subset C^{m+1}(\Omega;E)\) satisfies
\[
\sup_{f\in\mathcal B}p_{N_r(K),m+1}(f)<\infty.
\tag{CMP-4}
\]
Then for every \(\varepsilon>0\) there are finitely many \(f_1,\ldots,f_N\in\mathcal B\) such that every \(f\in\mathcal B\) has \(p_{K,m}(f-f_i)<\varepsilon\) for some \(i\).

**Proof.** Such an \(r\) exists: cover \(K\) by finitely many balls of half the radius of larger balls contained in \(\Omega\), and choose \(r\) smaller than every half-radius. The closed neighborhood then lies in \(\Omega\); it is closed and bounded, hence compact. Distance to \(K\) is continuous because the triangle inequality gives
\[
|\operatorname{dist}(x,K)-\operatorname{dist}(y,K)|\le|x-y|.
\]

Write \(M\) for the bound in (CMP-4). For \(x,y\in K\) with \(|x-y|<r\), the segment between them lies in \(N_r(K)\), since every point of it is within \(r\) of \(x\). The fundamental theorem of calculus along that segment gives, for \(|\alpha|\le m\),
\[
|\partial^\alpha f(y)-\partial^\alpha f(x)|
\le M\sum_{i=1}^n|y_i-x_i|
\le\sqrt n\,M|y-x|.
\tag{CMP-5}
\]
If \(M=0\) this is already equicontinuity; otherwise take the spatial tolerance smaller than both \(r\) and \(\eta/(\sqrt n M)\). The finite vector of all derivatives through order \(m\), restricted to \(K\), is therefore uniformly bounded and equicontinuous. Apply Theorem 1 jointly to that vector, using the maximum product norm. Its net centers are derivative vectors of actual members of \(\mathcal B\), giving the asserted seminorm net. This argument does not require convexity or nonempty interior of \(K\). \(\square\)

A bounded family in \(C^\infty(\Omega)\) satisfies (CMP-4) for every fixed \(K,m\), since its definition bounds all derivative seminorms on every compact subset of \(\Omega\). For a family of smooth tests supported in one compact \(K\subset\Omega\), each derivative vanishes outside \(K\); thus uniform bounds for \(p_{K,m+1}\) also bound the derivatives on \(N_r(K)\). Zero extension to \(\mathbb R^n\) is smooth because \(K\) stays inside \(\Omega\). Corollary 4 applies to both types of family.

For a continuous family \(\mathcal B\subset C_c(\Omega;E)\) with a common compact support, a common supremum bound and a common modulus of continuity after zero extension, Theorem 1 on a compact neighborhood gives a finite uniform net with centers in \(\mathcal B\). The supremum difference on that neighborhood equals the global supremum difference, since both functions vanish outside the common support.

**Finite-net consequence for functionals.** Let linear functionals \(T_j\) tend to zero on each individual member of \(\mathcal B\), and suppose \(|T_j(h)|\le C p(h)\) for differences of members, with \(C\) independent of \(j\). If \(\mathcal B\) has finite nets in \(p\) with centers \(f_i\in\mathcal B\), then
\[
\sup_{f\in\mathcal B}|T_j(f)|
\le C\varepsilon+\max_{1\le i\le N}|T_j(f_i)|\longrightarrow C\varepsilon
\quad\text{in limit superior}.
\tag{CMP-6}
\]
Indeed subtract a center within \(\varepsilon\), apply the common bound, and use convergence at the finitely many centers. Letting \(\varepsilon\downarrow0\) proves uniform convergence. In AN-01 this is used with \(p=p_{K,m}\) for distribution pairings, or with the supremum norm and a common compact mass bound for measure pairings. The common functional bound is established in the respective lesson.

## AN01-CMP-004: Compact Lipschitz paths

For a continuous \(c:[0,1]\to\mathbb R^n\), define
\[
\ell(c)=\sup_{0=t_0<\cdots<t_N=1}
\sum_{i=1}^N|c(t_i)-c(t_{i-1})|.
\tag{CMP-7}
\]

**Corollary 5 (path subsequences and length).** Suppose \(S\subset\mathbb R^n\) is compact and \(c_j:[0,1]\to S\) have Lipschitz constants at most one common finite number \(A\). They have a uniformly convergent subsequence with continuous limit \(c:[0,1]\to S\). Fixed endpoints are preserved; more generally convergent endpoint sequences pass to their limits. If their Lipschitz bounds are \(A_j\to L\), then the limit is \(L\)-Lipschitz. For every uniformly convergent subsequence,
\[
\ell(c)\le\liminf_{k\to\infty}\ell(c_{j_k}).
\tag{CMP-8}
\]
One can choose the subsequence so that the right side is \(\liminf_j\ell(c_j)\).

**Proof.** The common Lipschitz bound gives equicontinuity, and the compact target gives pointwise boundedness. Theorem 3, with \(K=[0,1]\) and \(E=\mathbb R^n\), gives uniform convergence. Since compact Euclidean \(S\) is closed, each limiting value lies in \(S\). Endpoint assertions are evaluations of this uniform limit. Passing to the limit in
\[
|c_j(s)-c_j(t)|\le A_j|s-t|
\]
proves the \(L\)-Lipschitz assertion.

For each fixed partition, its increment sum for \(c\) is the limit of the sums for \(c_{j_k}\), and each of those is at most \(\ell(c_{j_k})\). Hence the limiting sum is at most their length limit inferior. Taking the supremum over partitions proves (CMP-8). Every \(\ell(c_j)\le A\), by summing its Lipschitz increments. First choosing indices whose lengths tend to \(\liminf_j\ell(c_j)\), and then applying the compactness argument, proves the last assertion. \(\square\)

In particular, let \(F\subset\mathbb R^n\) be compact and nonempty, let \(\varepsilon_j\downarrow0\), and let \(c_j\) join fixed \(a,b\in F\) within \(F_{\varepsilon_j}=\{x:\operatorname{dist}(x,F)<\varepsilon_j\}\). If their Lipschitz constants are at most \(L+\varepsilon_j\), all values lie in the common compact target \(N_{\varepsilon_1}(F)\). The preceding result applies. Moreover
\[
\operatorname{dist}(c(t),F)
\le \|c-c_{j_k}\|_\infty+\varepsilon_{j_k}\longrightarrow0,
\]
so the limit stays in \(F\), keeps its endpoints and is \(L\)-Lipschitz, with \(\ell(c)\le L\). If only a common Lipschitz bound \(A\) and separate length bounds \(\ell(c_j)\le L+\varepsilon_j\) are supplied, the limit still stays in \(F\), keeps its endpoints and has \(\ell(c)\le L\), by (CMP-8); its guaranteed Lipschitz bound is \(A\). Thus reparametrized paths of controlled length satisfy precisely the compactness step used in the quasiconvexity proof.

Endpoint bounds alone give no equicontinuity, even with a common compact target: \(c_j(t)=\sin(2\pi jt)\) has both endpoints zero and values in \([-1,1]\), but \(c_j(1/(4j))=1\). Any uniformly convergent subsequence would have continuous limit equal to zero at zero, contradicting these values at parameters tending to zero.

## Scholarly credit

Richard Melrose, *18.155 Lecture 15*, MIT, 1 November 2016, discusses Schwartz kernels and smoothing operators, the surrounding context of AN-01's smooth-test application. [Author-hosted lecture](https://math.mit.edu/~rbm/18.155-F16/L15.pdf). It is an external scholarly reference; the finite-net, completeness and path proofs above are independently written here. This prerequisite contains no reproduced lecture text or PDF and claims no redistribution licence for that external file.
