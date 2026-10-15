# Every scale and every center

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The independent tests of [Random routing and independent tests](random-routing-and-independent-tests.md) control one scale \(t\) at one stable center \(x\). This lesson controls all scales \(t\in[1,2]\) at once, chooses the parameters of the construction, and repairs the centers where the random set still misses by a small open set [OpenAI-ES, Section 5]. This proves Proposition 3.1 of [Measure-universal sets and periodic hitting sets](measure-universal-sets-and-periodic-hitting-sets.md), and with it Theorem 2.2 there: no geometric progression is measure universal.

- All scales at a stable center (Section 1).
- The choice of the parameters (Section 2).
- Misses at stable centers (Section 3).
- Every center: the proof of Proposition 3.1 (Section 4).

We keep the notation of [Dyadic grids and windows on a tree](dyadic-grids-and-windows-on-a-tree.md) and [Random routing and independent tests](random-routing-and-independent-tests.md). From the core courses we use continuity of measure from above (Fremlin, *Measure Theory*, Volume 1, [112C](https://www1.essex.ac.uk/maths/people/fremlin/chap11.pdf), in [Measure and Integration](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D10)) and the Bolzano–Weierstrass theorem (Lebl, *Basic Analysis I*, [Theorem 2.3.8](https://www.jirka.org/ra/html/sec_bw.html), in [Real Analysis I](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C10)). For an integer \(r\ge1\) put
\[
\begin{aligned}D_{M,q}(r)&=4+2(M-1)r\\&\quad\times\bigl(1+2c\,q^{-2r}\bigr).\end{aligned}\tag{0.1}
\]

## 1. All scales at a stable center

**Lemma 1.1** (all scales; [OpenAI-ES, Lemma 5.1]). Let \(x\in\mathcal S\) be a stable center and \(\xi\) an atom of its exposure on which the route of \(x\) makes a default choice; let \(U\) be the first vertex where it does, \(h\) its height and \(r=r_h\). Then
\[
\begin{aligned}&\mathbb P\Bigl(\exists t\in[1,2]\ \forall n\in\mathcal N:\\&\qquad x+tq^n\notin B\Bigm|\xi\Bigr)\\&\quad\le D_{M,q}(r)\,e^{-p(M-1)r/2}.\end{aligned}\tag{1.1}
\]

*Proof.* On \(\xi\) the vertex \(U\) and the edges \(e_i=(U,i)\), \(i<M\), are fixed. The local test \(Q_i(z)\) of (3.1) of [Random routing and independent tests](random-routing-and-independent-tests.md) reads the key of \(z\) on \(e_i\) and keys of \(z\) on edges below \(U_i\) and at leaves below \(U_i\); all of them have resolution at most \(b_{e_i}^*\). By Lemma 1.1(2) of [Dyadic grids and windows on a tree](dyadic-grids-and-windows-on-a-tree.md), for every outcome \(Q_i(z)\) is a function of the single key \(J_{b_{e_i}^*}(z)\).

*Recorded scales.* For \(i<M\) and \(n\in W_{e_i}\), let \(\mathcal T_{i,n}\) be the set of \(t\in[1,2]\) with \(x+tq^n\in\Gamma_{b_{e_i}^*}\). As \(t\) runs over \([1,2]\), the point \(x+tq^n\) runs over an interval of length \(q^n\), which contains at most \(1+q^nN_{b_{e_i}^*}\) points of the lattice \(\Gamma_{b_{e_i}^*}\). By Lemma 1.1(1) and Lemma 2.1 of [Dyadic grids and windows on a tree](dyadic-grids-and-windows-on-a-tree.md), with \(n\ge a_{e_i}\) and \(b_{e_i}^*\le a_{e_i}+2r-1\),
\[
q^nN_{b_{e_i}^*}<2c\,q^{n-b_{e_i}^*}\le2c\,q^{1-2r}\le2c\,q^{-2r}.
\]
Let \(\mathcal T_0\) be the union of the sets \(\mathcal T_{i,n}\) with \(\{1,2\}\); there are \((M-1)r\) pairs \((i,n)\), so \(|\mathcal T_0|\le2+(M-1)r(1+2cq^{-2r})\). Let \(\mathcal T\) consist of \(\mathcal T_0\) and the midpoints of consecutive elements of \(\mathcal T_0\); then \(|\mathcal T|\le2|\mathcal T_0|\le D_{M,q}(r)\). The set \(\mathcal T\) depends only on \(x\), the windows, the grids and \(U\); it is fixed on \(\xi\).

*Constancy between recorded scales.* Let \(J\) be an open interval between consecutive elements of \(\mathcal T_0\), and \(t_1<t_2\) in \(J\). A point of \(\Gamma_{b_{e_i}^*}\) in \((x+t_1q^n,\,x+t_2q^n]\) would be \(x+t'q^n\) with \(t'\in(t_1,t_2]\subseteq J\), a recorded scale inside \(J\). So by Lemma 1.1(3) of [Dyadic grids and windows on a tree](dyadic-grids-and-windows-on-a-tree.md), the key \(J_{b_{e_i}^*}(x+tq^n)\) is constant for \(t\in J\), and for every outcome the whole vector \(\bigl(Q_i(x+tq^n)\bigr)_{i<M,\ n\in W_{e_i}}\) is constant on \(J\).

*Union bound.* Suppose that for some \(t\in[1,2]\) no point \(x+tq^n\), \(n\in\mathcal N\), lies in \(B\). By Lemma 3.1 of [Random routing and independent tests](random-routing-and-independent-tests.md), all local tests fail at \(t\). If \(t\in\mathcal T_0\), put \(t'=t\); otherwise \(t\) lies in an open interval between consecutive elements of \(\mathcal T_0\), because \(1,2\in\mathcal T_0\), and we let \(t'\) be its midpoint. In both cases \(t'\in\mathcal T\) and all local tests fail at \(t'\). Each \(t'\in\mathcal T\) is a fixed number on \(\xi\), so Lemma 4.1 of [Random routing and independent tests](random-routing-and-independent-tests.md) applies to it, and
\[
\begin{aligned}&\mathbb P\Bigl(\exists t\in[1,2]\ \forall n\in\mathcal N:\\&\qquad x+tq^n\notin B\Bigm|\xi\Bigr)\\&\quad\le|\mathcal T|\Bigl(1-\frac p2\Bigr)^{(M-1)r}\\&\quad\le D_{M,q}(r)\,e^{-p(M-1)r/2},\end{aligned}
\]
using \(1-u\le e^{-u}\). \(\square\)

The count uses the finest grid in the block of the edge \(e_i\), not the finest grid of the whole construction. Lemma 2.1 of [Dyadic grids and windows on a tree](dyadic-grids-and-windows-on-a-tree.md) bounds its resolution in terms of the window length \(r\) alone; this is what lets the exponential gain \(e^{-p(M-1)r/2}\) beat the count \(D_{M,q}(r)\), which grows like \(rq^{-2r}\).

## 2. The choice of the parameters

Fix \(p\in(0,1)\). Choose, in this order:

1. an integer \(M\ge2\) with
\[
\begin{aligned}\alpha&:=\frac{p(M-1)}2\\&>2\log\frac1q ;\end{aligned}\tag{2.1}
\]
2. an integer \(d\ge1\) with \((1-2^{1-M})^d<p\);
3. with \(K\) the number of edges of the ordered \(M\)-ary tree of height \(d\), an integer \(g\ge1\) with \(4Kc\,q^{g+1}<p\);
4. an integer \(r_*\ge1\) such that for every integer \(r\ge r_*\)
\[
D_{M,q}(r)\,e^{-\alpha r}<p .\tag{2.2}
\]

The last choice is possible because \(D_{M,q}(r)e^{-\alpha r}\) is at most a constant times \(r\,q^{-2r}e^{-\alpha r}=r\,e^{-(\alpha-2\log(1/q))r}\), which tends to \(0\) by (2.1). Build the windows of [Dyadic grids and windows on a tree](dyadic-grids-and-windows-on-a-tree.md) with these \(M\), \(d\), \(g\) and \(r_0=r_*\); then every \(r_h\ge r_*\). Build the random set \(B\) of [Random routing and independent tests](random-routing-and-independent-tests.md) with these windows and the given \(p\).

## 3. Misses at stable centers

**Lemma 3.1** (stable centers; [OpenAI-ES, Section 5]). For every stable center \(x\),
\[
\begin{aligned}&\mathbb P\Bigl(\exists t\in[1,2]\ \forall n\in\mathcal N:\\&\qquad x+tq^n\notin B\Bigr)\le2p .\end{aligned}\tag{3.1}
\]

*Proof.* Split \(\Omega\) according to the atoms of the exposure of \(x\). The atoms on which the route makes no default choice have total probability \((1-2^{1-M})^d<p\), by Lemma 2.1 of [Random routing and independent tests](random-routing-and-independent-tests.md) and the choice of \(d\). On an atom with a default choice, Lemma 1.1, \(r_h\ge r_*\) and (2.2) bound the conditional probability of the event by \(p\). Summing, the probability is less than \(p+p\). \(\square\)

The event in (3.1) quantifies over all \(t\in[1,2]\), but \(\Omega\) is finite, so it is an event like any other subset of \(\Omega\).

## 4. Every center: the proof of Proposition 3.1

*Proof of Proposition 3.1 of [Measure-universal sets and periodic hitting sets](measure-universal-sets-and-periodic-hitting-sets.md)* ([OpenAI-ES, Section 5]).

*Open enlargement.* For each outcome, \(B\) is \(1\)-periodic and in each period a union of finitely many half-open cells \([u,v)\); replacing each by \((u-\varepsilon,v)\), with \(\varepsilon\) times the number of cells at most \(p\), gives an open \(1\)-periodic set \(B^+\supseteq B\) with
\[
\rho(B^+)\le\rho(B)+p .
\]

*The missed centers.* For each outcome put
\[
\begin{aligned}R=\bigl\{&x\in\mathbb R:\ \exists t\in[1,2]\\&\forall n\in\mathcal N,\\&x+tq^n\notin B^+\bigr\}.\end{aligned}\tag{4.1}
\]
\(R\) is \(1\)-periodic because \(B^+\) is. It is closed: let \(x_k\in R\) converge to \(x\), with \(t_k\in[1,2]\) witnessing \(x_k\in R\). By the Bolzano–Weierstrass theorem a subsequence of \((t_k)\) converges to some \(t\in[1,2]\). For each \(n\in\mathcal N\), the points \(x_k+t_kq^n\) along this subsequence converge to \(x+tq^n\) and lie in the closed set \(\mathbb R\setminus B^+\), so \(x+tq^n\notin B^+\). Hence \(x\in R\).

*Expected sizes.* If \(x\) is stable and \(x\in R\), then the event of (3.1) occurs, since \(B\subseteq B^+\). With Lemma 3.2 of [Dyadic grids and windows on a tree](dyadic-grids-and-windows-on-a-tree.md) and the choice of \(g\), \(\rho(\mathbb R\setminus\mathcal S)\le4Kcq^{g+1}<p\). Since \(\Omega\) is finite,
\[
\begin{aligned}\mathbb E\rho(R)&=\int_0^1\mathbb P(x\in R)\,dx\\&\le2p\,\rho(\mathcal S)+\rho(\mathbb R\setminus\mathcal S)<3p,\end{aligned}
\]
and \(\mathbb E\rho(B^+)\le\mathbb E\rho(B)+p=2p\) by Lemma 1.1 of [Random routing and independent tests](random-routing-and-independent-tests.md). So some outcome satisfies
\[
\rho(B^+)+\rho(R)<5p .
\]
Fix such an outcome.

*Covering the missed centers.* For \(k\ge1\) let \(V_k=\{x:\operatorname{dist}(x,R)<1/k\}\), an open \(1\)-periodic set; if \(R\) is empty, put \(V_k=\varnothing\). The sets \(V_k\cap[0,1)\) decrease, and their intersection is \(R\cap[0,1)\) because \(R\) is closed. By continuity from above, \(\rho(V_k)\to\rho(R)\); choose \(k\) with \(\rho(V_k)\le\rho(R)+p\) and put \(V=V_k\) and
\[
H=B^+\cup V .
\]
Then \(H\) is open and \(1\)-periodic, and \(\rho(H)\le\rho(B^+)+\rho(R)+p<6p\).

*Every center is hit.* Let \(x\in\mathbb R\) and \(t\in[1,2]\). If \(x\notin R\), there is \(n\in\mathcal N\) with \(x+tq^n\in B^+\subseteq H\). If \(x\in R\), then \(x\in V\), which is open; since \(x+tq^n\to x\) as \(n\to\infty\), we get \(x+tq^n\in V\subseteq H\) for all large \(n\). These indices need not lie in \(\mathcal N\), and (3.1) of [Measure-universal sets and periodic hitting sets](measure-universal-sets-and-periodic-hitting-sets.md) allows every \(n\ge1\). \(\square\)

With Section 3 of [Measure-universal sets and periodic hitting sets](measure-universal-sets-and-periodic-hitting-sets.md), Theorem 2.2 there is proved: for every \(q\in(0,1)\) and \(\eta\in(0,1)\), a compact subset of \([0,1]\) of measure greater than \(1-\eta\) contains no affine copy of \(\{q^n:n\ge1\}\). Everything used is proved in this course, apart from basic facts of Lebesgue measure and real analysis from the core courses.

The construction is explicit but very large: the branching number \(M\) is of the order of \(\log(1/q)/p\), and the height \(d\) of the order of \(2^{M}\log(1/p)\) (Exercise 5.3).

## 5. Exercises

**5.1.** Show that for \(\alpha=2\log(1/q)\) the quantity \(D_{M,q}(r)e^{-\alpha r}\) tends to infinity as \(r\to\infty\). Which inequality in the proof needs the strict inequality (2.1)?

**5.2.** Show that \(R\) in (4.1) is closed by a second argument: write \(R\) as the projection to the first coordinate of a closed subset of \(\mathbb R\times[1,2]\), and show that such projections are closed.

**5.3.** Let \(q=\frac12\) and \(p=\frac1{10}\). Find the least \(M\) allowed by (2.1) and the least \(d\) allowed by the second choice in Section 2.

**5.4.** In the proof of Proposition 3.1, why does one not take \(H=B^+\)? Describe where the indices outside \(\mathcal N\) are used.

**5.5.** Show that \(H\) in the proof satisfies the stronger property: for every \(x\in\mathbb R\) and \(t\in[1,2]\), either some \(n\in\mathcal N\) has \(x+tq^n\in B^+\), or all sufficiently large \(n\) have \(x+tq^n\in H\).

## 6. Solutions

**5.1.** For \(\alpha=2\log(1/q)\), \(e^{-\alpha r}=q^{2r}\), so \(D_{M,q}(r)e^{-\alpha r}\ge4c(M-1)r\to\infty\). The strict inequality in (2.1) is needed for the existence of \(r_*\) in (2.2).

**5.2.** \(R\) is the projection to the first coordinate of the set \(Z\) of pairs \((x,t)\in\mathbb R\times[1,2]\) with \(x+tq^n\notin B^+\) for all \(n\in\mathcal N\), which is closed as an intersection of preimages of the closed set \(\mathbb R\setminus B^+\) under continuous maps. If \(x_k\to x\) with \((x_k,t_k)\in Z\), a subsequence of \(t_k\) converges to some \(t\in[1,2]\) by the Bolzano–Weierstrass theorem, and \((x,t)\in Z\) because \(Z\) is closed; so the projection is closed. The compactness of \([1,2]\) is essential: the projection of the closed set \(\{(x,t):xt=1\}\subseteq\mathbb R\times\mathbb R\) is \(\mathbb R\setminus\{0\}\), not closed.

**5.3.** (2.1) asks \((M-1)/20>2\log2\approx1.386\), so \(M-1\ge28\) and \(M=29\). Then \(d\) must satisfy \((1-2^{-28})^d<\frac1{10}\), that is \(d>\log10/(-\log(1-2^{-28}))\), approximately \(6.18\times10^8\); the least such \(d\) is \(618{,}095{,}479\).

**5.4.** The set \(R\) of missed centers can be nonempty: the random set gives every center only a probability of being hit, and unstable centers are not controlled at all. The open set \(V\supseteq R\) of small density repairs them, and the points \(x+tq^n\) that it contains have large indices \(n\), which need not belong to any window.

**5.5.** This is the case distinction of the last paragraph of the proof: if \(x\notin R\), some \(n\in\mathcal N\) works with \(B^+\); if \(x\in R\subseteq V\), all large \(n\) work with \(V\subseteq H\).

## References

- [OpenAI-ES] OpenAI, *The geometric case of the Erdős similarity conjecture*, OpenAI Math Release preprint, 5 October 2026, Section 5. https://github.com/openai/math/tree/main/preprints/The-geometric-case-of-the-Erdos-similarity-conjecture-October-5-2026
- [Chlebík 2015] M. Chlebík, *On the Erdős similarity problem*, preprint, 2015. https://arxiv.org/abs/1512.05607
- [Kolountzakis–Papageorgiou 2025] M. N. Kolountzakis, E. Papageorgiou, *Large sets containing no copies of a given infinite sequence*, Anal. PDE 18 (2025), 93–108. https://arxiv.org/abs/2208.02637
