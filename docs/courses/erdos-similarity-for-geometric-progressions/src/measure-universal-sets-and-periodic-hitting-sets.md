# Measure-universal sets and periodic hitting sets

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

A set \(A\subseteq\mathbb R\) is measure universal if every measurable set of positive Lebesgue measure contains an affine copy \(x+sA\) of it, with \(s\ne0\). Finite sets are measure universal. Erdős conjectured in 1974 that no infinite set is; the question is open in general, and the introduction of [Chlebík 2015] surveys what is known. Falconer proved non-universality for sequences \(x_k\to0\) with \(x_{k+1}/x_k\to1\), Bourgain for sums of three infinite sets, and Kolountzakis and Chlebík gave criteria in terms of large finite subsets with large gaps. Geometric progressions \(\{q^n:n\ge1\}\) are the simplest infinite sets that escape these criteria. This course proves OpenAI's theorem that they are not measure universal [OpenAI-ES]: for each \(q\in(0,1)\) there is a compact subset of \([0,1]\) of measure as close to \(1\) as we like that contains no affine copy of \(\{q^n:n\ge1\}\). For \(q=1/2\) the theorem has a formal proof in Lean in OpenAI's release [OpenAI-ESd].

- Measure-universal sets (Section 1).
- Geometric progressions and the theorem (Section 2).
- Periodic hitting sets (Section 3).
- The plan of the course (Section 4).

We write \(m\) for Lebesgue measure on \(\mathbb R\). From the core course [Measure and Integration](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D10) we use: countable additivity, continuity from below and from above (Fremlin, *Measure Theory*, Volume 1, [112C](https://www1.essex.ac.uk/maths/people/fremlin/chap11.pdf)); invariance of Lebesgue measure under translations (Volume 1, [134A](https://www1.essex.ac.uk/maths/people/fremlin/chap13.pdf)); for every set \(A\subseteq\mathbb R\), the outer measure \(m^*A\) is the infimum of \(m(G)\) over open sets \(G\supseteq A\) (Volume 1, [134F(a)](https://www1.essex.ac.uk/maths/people/fremlin/chap13.pdf)); and \(m(cE)=|c|\,m(E)\) for measurable \(E\) and real \(c\ne0\) (Volume 2, [263A](https://www1.essex.ac.uk/maths/people/fremlin/chap26.pdf)).

## 1. Measure-universal sets

**Definition 1.1.** An *affine copy* of a set \(A\subseteq\mathbb R\) is a set \(x+sA=\{x+sa:a\in A\}\) with \(x\in\mathbb R\) and \(s\in\mathbb R\setminus\{0\}\). The set \(A\) is *measure universal* if every Lebesgue measurable set of positive measure contains an affine copy of \(A\).

**Proposition 1.2** (finite sets are universal). Every finite set \(F\subseteq\mathbb R\) is measure universal. More precisely, if \(m(A)>0\), there is \(s_0>0\) such that \(A\) contains a copy \(x+sF\) for every \(0<s\le s_0\).

*Proof.* Let \(F=\{a_1,\ldots,a_k\}\), \(k\ge1\); the empty set is contained in every set. By continuity from below, \(m(A\cap[-j,j])>0\) for some \(j\), so we may assume that \(A\) is bounded and \(0<m(A)<\infty\). By 134F(a) there is an open set \(G\supseteq A\) with
\[
m(G)<\Bigl(1+\frac1{2k}\Bigr)m(A).
\]
For \(z\in G\) let \(I_z\) be the union of all open intervals \(J\) with \(z\in J\subseteq G\). It is an open interval contained in \(G\). If \(I_z\) and \(I_w\) meet, \(I_z\cup I_w\) is an open interval in \(G\) containing \(z\) and \(w\), so \(I_z=I_z\cup I_w=I_w\). Each \(I_z\) contains a rational number, so \(G\) is the union of a countable family of disjoint open intervals \(I_j\), each of finite length since \(m(G)<\infty\). By countable additivity,
\[
\begin{aligned}&\sum_jm(A\cap I_j)=m(A)\\&\quad>\Bigl(1+\frac1{2k}\Bigr)^{-1}\sum_jm(I_j),\end{aligned}
\]
so some interval \(I=(u,u+\ell)\) satisfies \(m(A\cap I)>(1+\frac1{2k})^{-1}\ell\ge(1-\frac1{2k})\ell\). Put \(A'=A\cap I\) and \(D=\max_i|a_i|\).

For \(s>0\), each translate \(A'-sa_i\) lies in the interval \(I_s=(u-sD,\,u+\ell+sD)\) of length \(\ell+2sD\), and by 134A
\[
\begin{aligned}m\bigl(I_s\setminus(A'-sa_i)\bigr)&=\ell+2sD-m(A')\\&<\frac\ell{2k}+2sD .\end{aligned}
\]
Hence
\[
\begin{aligned}&m\Bigl(\bigcap_{i=1}^k(A'-sa_i)\Bigr)\\&\quad\ge m(I_s)-\sum_{i=1}^km\bigl(I_s\setminus(A'-sa_i)\bigr)\\&\quad>\ell+2sD-k\Bigl(\frac\ell{2k}+2sD\Bigr)\\&\quad=\frac\ell2-2(k-1)sD .\end{aligned}
\]
If \(k=1\) or \(D=0\), put \(s_0=1\); otherwise put \(s_0=\ell/(4(k-1)D)\). For \(0<s\le s_0\) the intersection has positive measure, so it contains a point \(x\), and then \(x+sa_i\in A'\subseteq A\) for every \(i\). \(\square\)

**Conjecture 1.3** (Erdős). No infinite subset of \(\mathbb R\) is measure universal.

A measure-universal set is bounded, since its affine copies inside \([0,1]\) are bounded, and subsets of measure-universal sets are measure universal (Exercise 5.1).

## 2. Geometric progressions and the theorem

For \(q\in(0,1)\) put
\[
G_q=\{q^n:n\in\mathbb N,\ n\ge1\}.
\]
Chlebík proved that a bounded infinite set \(X\) is not measure universal if, for arbitrarily small \(\sigma>0\), it contains points \(x_1>x_2>\cdots>x_n\), \(n\ge3\), with
\[
\min_{1\le i<n}(x_i-x_{i+1})\ge(1-\sigma)^n(x_1-x_n)
\]
[Chlebík 2015, Theorem 15]; this contains the earlier criterion of Kolountzakis. Geometric progressions are not covered.

**Remark 2.1.** \(G_q\) does not satisfy Chlebík's hypothesis. Let \(x_1>\cdots>x_n\) be points of \(G_q\), \(n\ge3\), and let \(\delta\) be their smallest gap. The \(n-1\) gaps add up to \(x_1-x_n\), so \(\delta\le(x_1-x_n)/(n-1)\le(x_1-x_n)/2\). Also \(x_{n-1}\le q^{n-2}x_1\) and \(x_n\le qx_1\), so
\[
\begin{aligned}\delta&\le x_{n-1}-x_n<x_{n-1}\\&\le q^{n-2}x_1\le\frac{q^{n-2}}{1-q}(x_1-x_n).\end{aligned}
\]
Choose \(n_1\) with \(q^{n-2}/(1-q)<\bigl(\frac{1+q}2\bigr)^n\) for all \(n\ge n_1\), which is possible because \(q<\frac{1+q}2\), and let \(0<\sigma<\min\bigl(\frac{1-q}2,\,1-2^{-1/n_1}\bigr)\). For \(n\ge n_1\), \((1-\sigma)^n\ge\bigl(\frac{1+q}2\bigr)^n>q^{n-2}/(1-q)\); for \(3\le n<n_1\), \((1-\sigma)^n>\frac12\). In both cases \(\delta<(1-\sigma)^n(x_1-x_n)\).

**Theorem 2.2** (geometric progressions are not universal; [OpenAI-ES, Theorem 1.1]). For every \(q\in(0,1)\) and \(\eta\in(0,1)\) there is a compact set \(E_{q,\eta}\subseteq[0,1]\) with \(m(E_{q,\eta})>1-\eta\) such that for every \(x\in\mathbb R\) and every \(s\in\mathbb R\setminus\{0\}\), some point \(x+sq^n\), \(n\ge1\), lies outside \(E_{q,\eta}\).

In particular \(G_q\) is not measure universal. The set \(E_{q,\eta}\) depends on \(q\); the theorem says nothing about one set avoiding the progressions of several ratios at once.

## 3. Periodic hitting sets

A set \(H\subseteq\mathbb R\) is *\(1\)-periodic* if \(H+1=H\). For a measurable \(1\)-periodic set put
\[
\rho(H)=m\bigl(H\cap[0,1)\bigr),
\]
its density. Since \(m\) is invariant under translations, \(m(H\cap[a,a+1))=\rho(H)\) for every \(a\in\mathbb R\).

**Proposition 3.1** (periodic hitting sets; [OpenAI-ES, Proposition 2.1]). Let \(q\in(0,1)\). For every \(p\in(0,1)\) there is an open \(1\)-periodic set \(H\) with \(\rho(H)\le6p\) such that for every \(x\in\mathbb R\) and every \(t\in[1,2]\) some integer \(n\ge1\) satisfies
\[
x+tq^n\in H .\tag{3.1}
\]

The proof occupies the rest of the course and is completed in [Every scale and every center](every-scale-and-every-center.md). It is the heart of the matter: a periodic open set of small density must meet every copy \(x+tG_q\) with the dilation \(t\) between \(1\) and \(2\) and every center \(x\). Dilations by powers of two, and reflections, then handle all nonzero \(s\) at once.

*Proof of Theorem 2.2 from Proposition 3.1* ([OpenAI-ES, Section 2]). For \(k\in\mathbb Z\) put \(p_k=\frac\eta{64}4^{-|k|}\in(0,1)\), let \(H_k\) be given by Proposition 3.1 for \(p=p_k\), and put
\[
\begin{gathered}C=\bigcup_{k\in\mathbb Z}\bigl(2^kH_k\cup(-2^kH_k)\bigr),\\ E_{q,\eta}=[0,1]\setminus C .\end{gathered}
\]
The set \(C\) is open, as a union of images of open sets under the homeomorphisms \(z\mapsto\pm2^kz\), so \(E_{q,\eta}\) is closed and bounded, hence compact.

*Measure.* The set \(\pm2^kH_k\) is \(2^k\)-periodic, and by 263A its intersection with an interval of length \(2^k\) has measure \(2^k\rho(H_k)\). If \(k\le0\), \([0,1)\) is the disjoint union of \(2^{-k}\) intervals of length \(2^k\), so \(m\bigl((\pm2^kH_k)\cap[0,1]\bigr)=\rho(H_k)\). If \(k>0\), \([0,1]\) lies in an interval of length \(2^k\), so the measure is at most \(2^k\rho(H_k)\). In both cases it is at most \(\max(1,2^k)\cdot6p_k\), and
\[
\begin{aligned}&m\bigl(C\cap[0,1]\bigr)\le12\sum_{k\in\mathbb Z}p_k\max(1,2^k)\\&\quad=\frac{12\eta}{64}\Bigl(\sum_{j\ge0}4^{-j}+\sum_{k\ge1}2^{-k}\Bigr)\\&\quad=\frac{12\eta}{64}\cdot\frac73=\frac{7\eta}{16}.\end{aligned}
\]
So \(m(E_{q,\eta})\ge1-\frac{7\eta}{16}>1-\eta\).

*Avoidance.* Let \(x\in\mathbb R\) and \(s>0\). Write \(s=2^kt\) with \(k\in\mathbb Z\) and \(t\in[1,2)\). By (3.1) for \(H_k\) at the center \(2^{-k}x\), there is \(n\ge1\) with \(2^{-k}x+tq^n\in H_k\), so \(x+sq^n=2^k(2^{-k}x+tq^n)\in2^kH_k\subseteq C\). If \(s<0\), the same argument for \(-x\) and \(-s\) gives \(n\) with \(-x-sq^n\in2^kH_k\), so \(x+sq^n\in-2^kH_k\subseteq C\). In both cases \(x+sq^n\notin E_{q,\eta}\). \(\square\)

The powers of two in this proof only normalize the dilation; they need no relation between \(2\) and \(q\).

## 4. The plan of the course

The set \(H\) of Proposition 3.1 is built as a random set and then enlarged slightly.

- [Dyadic grids and windows on a tree](dyadic-grids-and-windows-on-a-tree.md): nested dyadic grids with cells of width comparable to \((1-q)q^b\), a finite ordered tree whose edges carry consecutive windows of indices \(n\), and two facts about the points \(x+tq^n\): for most centers \(x\), translations from a later window do not change the grid cells used by earlier windows, and within one window the points lie in distinct cells.
- [Random routing and independent tests](random-routing-and-independent-tests.md): random tables on the grids route every point to a leaf of the tree and decide whether it belongs to a random set \(B\) of expected density \(p\). If the route of a center makes a default choice somewhere, the window below that choice offers many independent chances for a point \(x+tq^n\) to fall in \(B\).
- [Every scale and every center](every-scale-and-every-center.md): finitely many values of \(t\) represent all \(t\in[1,2]\); the parameters are chosen so that a miss is unlikely at every center; a small open set repairs the remaining centers. This proves Proposition 3.1.

## 5. Exercises

**5.1.** Show that a subset of a measure-universal set is measure universal, and that every affine copy of a measure-universal set is measure universal. Deduce that Theorem 2.2 for \(q^2\) implies Theorem 2.2 for \(q\).

**5.2.** Show that if some infinite set is measure universal, then some strictly decreasing sequence with limit \(0\) is measure universal. So Conjecture 1.3 is equivalent to its case of sequences decreasing to \(0\). Use the Bolzano–Weierstrass theorem from the core course [Real Analysis I](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C10) (Lebl, *Basic Analysis I*, [Theorem 2.3.8](https://www.jirka.org/ra/html/sec_bw.html)).

**5.3.** In the proof of Theorem 2.2, check that \(\sum_{k\in\mathbb Z}p_k\max(1,2^k)=\frac{7\eta}{192}\).

**5.4.** Let \(F\) be finite, \(A\) measurable and \(I\) an interval with \(m(A\cap I)>0\). Show that \(A\cap I\) contains an affine copy of \(F\).

**5.5.** Show that the set \(E_{q,\eta}\) of Theorem 2.2 contains no nonempty open interval.

## 6. Solutions

**5.1.** If \(A'\subseteq A\) and \(x+sA\subseteq E\), then \(x+sA'\subseteq E\). If \(A\) is universal and \(u\ne0\), let \(E\) have positive measure and \(x+sA\subseteq E\); with \(s'=s/u\) and \(x'=x-sy/u\) we get \(x'+s'(y+uA)=x+sA\subseteq E\), so \(E\) contains a copy of \(y+uA\). Finally \(G_{q^2}=\{q^{2n}:n\ge1\}\subseteq G_q\), so a copy of \(G_q\) contains a copy of \(G_{q^2}\), and the set \(E_{q^2,\eta}\), which contains no copy of \(G_{q^2}\), contains no copy of \(G_q\).

**5.2.** A universal set \(A\) is bounded, since \([0,1]\) contains a copy \(x+sA\). If \(A\) is infinite, it contains a sequence of distinct points, which has a convergent subsequence with some limit \(a\) by the Bolzano–Weierstrass theorem. At most one of its terms equals \(a\), so infinitely many lie on one side of \(a\); say above \(a\), the other case being symmetric. Choose \(b_1\) among them, and inductively \(b_{k+1}\) among them with \(a<b_{k+1}<b_k\) and \(b_{k+1}-a<1/k\); this is possible because the terms converge to \(a\). Then \(\{b_k-a\}\) is a strictly decreasing sequence with limit \(0\); it is an affine copy of the subset \(\{b_k\}\) of \(A\), hence universal by 5.1. In the symmetric case use \(\{a-b_k\}\), the copy with \(s=-1\).

**5.3.** \(\sum_{k\le0}4^{-|k|}=\frac43\) and \(\sum_{k\ge1}4^{-k}2^k=\sum_{k\ge1}2^{-k}=1\), so the sum is \(\frac\eta{64}\cdot\frac73=\frac{7\eta}{192}\); then \(12\cdot\frac{7\eta}{192}=\frac{7\eta}{16}\), as used in the proof.

**5.4.** \(A\cap I\) is measurable with positive measure, so Proposition 1.2 applied to it gives a copy \(x+sF\subseteq A\cap I\).

**5.5.** Suppose \((a,b)\subseteq E_{q,\eta}\) with \(a<b\). Put \(\ell=b-a\), \(x=a+\ell/4\) and \(s=\ell/2\). For \(n\ge1\), \(0<sq^n<\ell/2\), so \(x+sq^n\in(a+\ell/4,\,a+3\ell/4)\subseteq(a,b)\). Then \(E_{q,\eta}\) contains the affine copy \(x+sG_q\), which Theorem 2.2 excludes.

## References

- [OpenAI-ES] OpenAI, *The geometric case of the Erdős similarity conjecture*, OpenAI Math Release preprint, 5 October 2026. https://github.com/openai/math/tree/main/preprints/The-geometric-case-of-the-Erdos-similarity-conjecture-October-5-2026
- [OpenAI-ESd] OpenAI, *The dyadic case of the Erdős similarity conjecture*, OpenAI Math Release preprint, 25 September 2026, with a Lean formalization of its main theorem. https://github.com/openai/math/tree/main/preprints/The-dyadic-case-of-the-Erdos-similarity-conjecture-September-25-2026
- [Chlebík 2015] M. Chlebík, *On the Erdős similarity problem*, preprint, 2015. https://arxiv.org/abs/1512.05607
- [Kolountzakis–Papageorgiou 2025] M. N. Kolountzakis, E. Papageorgiou, *Large sets containing no copies of a given infinite sequence*, Anal. PDE 18 (2025), 93–108. https://arxiv.org/abs/2208.02637
