# Random sampling in expanding graphs

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The pieces produced in [Splitting a graph at a scale](splitting-a-graph-at-a-scale.md) have order between \(D^{0.90}\) and \(D^{1.02}\) and cut expansion of order \(D^{0.90}\). Two random operations on such a piece are needed later: dividing its edges into a few classes that each keep a fixed fraction of the cut expansion, and choosing a random set of vertices that still induces a graph with good cut expansion. This lesson proves both. The second is the delicate one: a sampled set has far too many subsets to control each cut separately, and the proof approximates every possible bad cut by a cut from a small family fixed in advance.

All probability spaces in this lesson are finite. Logarithms are to base two and \(\ln\) is the natural logarithm. Throughout, \(D\) is a large real number, and
\[
\sigma=D^{0.90},\qquad\tau=D^{0.74}.
\]
Statements "for all sufficiently large \(D\)" hold with a threshold that depends only on the constants fixed in the statement, uniformly over all graphs and orders allowed there.

## 1. Tail bounds

**Lemma 1.1** (Markov's inequality). For a random variable \(X\ge0\) and \(a>0\), \(\Pr(X\ge a)\le\mathbb EX/a\).

*Proof.* \(X\ge a\mathbf 1_{\{X\ge a\}}\); take expectations. \(\square\)

A *binomial* random variable is a sum of independent indicator variables with a common success probability; its mean is the number of indicators times that probability.

**Lemma 1.2** (Chernoff bounds). If \(X\) is binomial with mean \(\mu\), then
\[
\begin{gathered}
\Pr\Bigl(X\le\frac\mu2\Bigr)\le e^{-\mu/8},\\
\Pr(X\ge2\mu)\le e^{-\mu/3}.
\end{gathered}
\]

*Proof.* Let \(X=X_1+\dots+X_m\) with independent indicators of probability \(\pi\), so \(\mu=m\pi\). For real \(t\), independence gives
\[
\mathbb Ee^{tX}=\prod_{i=1}^m\bigl(1+\pi(e^t-1)\bigr)\le e^{\mu(e^t-1)},
\]
using \(1+y\le e^y\). With \(t=\ln2\) and Lemma 1.1 applied to \(e^{tX}\),
\[
\begin{aligned}
\Pr(X\ge2\mu)&\le e^{\mu(2-1)-2\mu\ln2}\\
&=e^{-\mu(2\ln2-1)} .
\end{aligned}
\]
With \(t=-\ln2\), the event \(X\le\mu/2\) is the event \(e^{tX}\ge e^{t\mu/2}\), so
\[
\begin{aligned}
\Pr\Bigl(X\le\frac\mu2\Bigr)&\le e^{\mu(\frac12-1)+\frac\mu2\ln2}\\
&=e^{-\mu\frac{1-\ln2}2} .
\end{aligned}
\]
Finally \(2\ln2-1>0.38>1/3\) and \((1-\ln2)/2>0.15>1/8\). \(\square\)

Together with the union bound, \(\Pr(\bigcup_iE_i)\le\sum_i\Pr(E_i)\), these are the only probabilistic tools of the course.

## 2. Splitting the edges

**Lemma 2.1** (edge splitting). Fix \(c>0\) and an integer \(l\ge1\). For all sufficiently large \(D\): if a graph \(P\) of order \(r\) with \(D^{0.90}\le r\le D^{1.02}\) has cut expansion at least \(h_0\ge cD^{0.90}\), then \(E(P)\) can be partitioned into \(l\) spanning subgraphs, each of cut expansion at least \(h_0/(2l)\).

*Proof.* Put every edge into one of \(l\) classes, independently and uniformly. Fix \(U\subseteq V(P)\) with \(u=|U|\) and \(1\le u\le r/2\), and let \(e=|\partial_PU|\ge h_0u\). In a fixed class the number of edges of \(\partial_PU\) is binomial with mean \(e/l\ge h_0u/l\). By Lemma 1.2 it is less than \(h_0u/(2l)\) with probability at most \(e^{-h_0u/(8l)}\). There are at most \(r^u\) sets \(U\) of size \(u\), so the probability that some class fails at some cut is at most
\[
l\sum_{u\ge1}\rho^u,\qquad\rho=re^{-h_0/(8l)} .
\]
Since \(r\le D^{1.02}\) and \(h_0\ge cD^{0.90}\), the ratio \(\rho\) tends to zero uniformly, and for large \(D\) the sum \(l\rho/(1-\rho)\) is less than one. Some assignment therefore succeeds. A cut is controlled by its smaller side, so each class, taken on all of \(V(P)\), has cut expansion at least \(h_0/(2l)\). \(\square\)

## 3. Sampling the vertices

For \(A,B\subseteq V(P)\) disjoint, \(e_P(A,B)\) is the number of edges of \(P\) with one end in \(A\) and the other in \(B\). For \(V'\subseteq V(P)\), \(P[V']\) is the subgraph induced on \(V'\).

**Lemma 3.1** (vertex sampling). Fix \(c'>0\) and \(p\in(0,1)\). Let \(P\) be a graph of order \(r\) with \(D^{0.90}\le r\le D^{1.02}\) and cut expansion at least \(h=c'D^{0.90}\). Choose every vertex independently with probability \(p\), forming \(V'\). Then, with probability \(1-o(1)\) as \(D\to\infty\), uniformly in \(P\):
\[
\begin{gathered}
|V'|\le2pr,\\
|N_P(v)\cap V'|\ge\frac{ph}2\quad(v\in V(P)),\\
P[V']\text{ has cut expansion at least }\tau .
\end{gathered}
\]

*Proof.* *Size and degrees.* By Lemma 1.2 of [Routing in graphs with cut expansion](routing-in-graphs-with-cut-expansion.md), every vertex has degree at least \(h\). So \(|N_P(v)\cap V'|\) is binomial with mean at least \(ph\), and Lemma 1.2 bounds the probability that it is at most \(ph/2\) by \(e^{-ph/8}\). Also \(|V'|\) is binomial with mean \(pr\). The first two assertions fail with probability at most
\[
e^{-pr/3}+re^{-ph/8}=o(1).
\]

*A family of witness sets, fixed before sampling.* Put
\[
M=\frac{16}p\log r,\qquad s=\Bigl\lceil\frac{4rM}h\Bigr\rceil .
\]
For large \(D\), \(M/h<1\) and \(s\le r\). Let \(\mathcal U\) be the family of all unions \(\bigcup_{v\in S}N_P(v)\) of neighbourhoods in \(P\), over sets \(S\subseteq V(P)\) with \(|S|\le s\). Then
\[
|\mathcal U|\le\sum_{t=0}^s\binom rt\le(s+1)r^s .
\]

**Claim 1.** With probability \(1-o(1)\), every \(U\in\mathcal U\) with \(\min\{|U|,r-|U|\}\ge ph/8\) satisfies
\[
e_P(U\cap V',\,V'\setminus U)\ge\frac{p^2}4|\partial_PU| .
\]

Fix such a \(U\) and put \(e=|\partial_PU|\); cut expansion gives \(e\ge ph^2/8\). Colour the edges of \(\partial_PU\) greedily so that edges of one colour share no vertex: an edge meets fewer than \(2r\) other edges, so \(2r\) colours suffice, and the colour classes are matchings. Fix this colouring before sampling. Classes with fewer than \(e/(4r)\) edges contain fewer than \(e/2\) edges in total. In a class with \(m\ge e/(4r)\) edges, the edges have pairwise disjoint ends, so the events that both ends of an edge are sampled are independent, each of probability \(p^2\). The number of edges of the class with both ends in \(V'\) is binomial with mean \(p^2m\), and by Lemma 1.2 it is less than \(p^2m/2\) with probability at most
\[
e^{-p^2m/8}\le e^{-p^2e/(32r)}\le e^{-p^3h^2/(256r)} .
\]
If no large class fails, at least \(\frac{p^2}2\cdot\frac e2\) edges of \(\partial_PU\) have both ends sampled, and each of them joins \(U\cap V'\) to \(V'\setminus U\). The union bound over the at most \(2r|\mathcal U|\) pairs of a set and a class bounds the failure probability by
\[
2r(s+1)r^se^{-p^3h^2/(256r)} .
\]
Here \(h^2/r\ge c'^2D^{0.78}\), while \(r/h\le D^{0.12}/c'\) and \(M=O(\log D)\), so the logarithm of \(2r(s+1)r^s\) is \(O(D^{0.12}\log^2D)\), with constants depending on \(p\) and \(c'\). The bound is \(o(1)\), which proves Claim 1.

*Approximating a bad cut.* Fix an outcome satisfying the size and degree bounds and Claim 1. Suppose that some \(A\subseteq V'\) satisfies
\[
\begin{gathered}
0<a=|A|\le\frac{|V'|}2,\\
e_P(A,V'\setminus A)<\tau a .
\end{gathered}
\]
We derive a contradiction for large \(D\); take \(D\) so large that \(\tau<ph/4\).

*Step 1: \(a>ph/4\).* Otherwise a vertex of \(A\) has at least \(ph/2\) sampled neighbours, of which at most \(a-1<ph/4\) lie in \(A\); so it has more than \(ph/4\) neighbours in \(V'\setminus A\), and \(e_P(A,V'\setminus A)>aph/4>\tau a\).

*Step 2: few vertices of \(A\) look outward.* Let \(A_{\rm good}\) be the set of \(v\in A\) with \(|N_P(v)\cap A|\ge ph/4\). A vertex of \(A\setminus A_{\rm good}\) has more than \(ph/4\) neighbours in \(V'\setminus A\), so
\[
|A\setminus A_{\rm good}|\le\frac{4\tau a}{ph}.
\]

*Step 3: a small hitting set.* With \(V'\) and \(A\) fixed, choose a random set \(S\subseteq A\), containing each vertex independently with probability \(q=M/h\). For \(v\in A_{\rm good}\), the probability that \(S\) misses \(N_P(v)\cap A\) is at most
\[
(1-q)^{ph/4}\le e^{-pM/4}=e^{-4\log r}\le r^{-4},
\]
so with probability at least \(1-r^{-3}\ge7/8\), the set \(S\) meets the neighbourhood of every vertex of \(A_{\rm good}\). Let \(T(S)\) be the number of vertices of \(V'\setminus A\) with a neighbour in \(S\). Then \(\mathbb E|S|=aM/h\) and
\[
\begin{aligned}
\mathbb ET(S)&\le\frac Mh\sum_{w\in V'\setminus A}|N_P(w)\cap A|\\
&=\frac Mhe_P(A,V'\setminus A)<\frac{\tau Ma}h .
\end{aligned}
\]
By Lemma 1.1, \(|S|>4aM/h\) and \(T(S)>4\tau Ma/h\) each have probability at most \(1/4\). The three failure probabilities add up to less than one, so there is a set \(S\subseteq A\) with
\[
\begin{gathered}
|S|\le\frac{4aM}h,\qquad T(S)\le\frac{4\tau Ma}h,\\
S\cap N_P(v)\ne\varnothing\quad(v\in A_{\rm good}).
\end{gathered}
\]
This auxiliary choice only proves that \(S\) exists; Claim 1 was established for the whole family \(\mathcal U\) in advance.

*Step 4: comparison.* Put \(U=\bigcup_{v\in S}N_P(v)\). Since \(|S|\le4rM/h\le s\), \(U\in\mathcal U\). Every vertex of \(A_{\rm good}\) has a neighbour in \(S\) and so lies in \(U\); every vertex of \((U\cap V')\setminus A\) is counted by \(T(S)\). Hence
\[
\delta=\bigl|(U\cap V')\,\triangle\,A\bigr|\le\frac{4\tau a}{ph}+\frac{4\tau Ma}h .
\]
Since \(\tau M/h=O(D^{-0.16}\log D)\), we have \(\delta=o(a)\). Both sides of the cut of \(U\) in \(P\) are large:
\[
\begin{aligned}
|U|&\ge a-\delta,\\
r-|U|&\ge|V'\setminus U|\\
&\ge|V'\setminus A|-\delta\ge a-\delta ,
\end{aligned}
\]
and for large \(D\) both are at least \(a/2>ph/8\). Claim 1 and cut expansion give
\[
e_P(U\cap V',V'\setminus U)\ge\frac{p^2}4h\frac a2=\frac{p^2ha}8 .
\]
On the other hand, moving one vertex of \(V'\) from one side to the other changes the number of crossing edges by at most \(r-1\). Turning \(A\) into \(U\cap V'\) takes \(\delta\) such moves, so
\[
e_P(U\cap V',V'\setminus U)<\tau a+r\delta .
\]
Dividing by \(ha\), the right side becomes at most
\[
\begin{aligned}
&\frac\tau h+O\Bigl(\frac{\tau Mr}{h^2}\Bigr)\\
&\quad=O(D^{-0.16})+O(D^{-0.04}\log D),
\end{aligned}
\]
which is less than \(p^2/8\) for large \(D\). This contradiction shows that no such \(A\) exists.

A set \(X\subseteq V'\) with \(|X|>|V'|/2\) is handled through its complement in \(V'\). So \(P[V']\) has cut expansion at least \(\tau\), and the three assertions hold with probability \(1-o(1)\). Every \(o(1)\) above depends only on \(D\), once \(p\) and \(c'\) are fixed. \(\square\)

A direct union bound over all subsets of \(V'\) would fail. The edges leaving a set \(A\) may end at few outside vertices, each joined to \(A\) by many edges, and then the probability that few of them survive the sampling is only about \(e^{-pha/r}\), far more than \(r^{-a}\). The witness family has \(e^{O(D^{0.12}\log^2D)}\) members, each controlled with failure probability \(e^{-\Omega(D^{0.78})}\), and every bad cut is close to one of them; this is where the gap between the exponents \(0.78\) and \(0.12\) is used.

## 4. Exercises

**4.1** (easy). Prove \(1+y\le e^y\) for all real \(y\).

**4.2** (easy). Show that a greedy colouring of the edges of a simple graph of order \(r\) uses at most \(2r-3\) colours, with every colour class a matching.

**4.3** (medium). Let \(X\) be binomial with mean \(\mu\). Show that \(\Pr(X\ge3\mu)\le e^{-\mu}\).

**4.4** (medium). In Step 3, the vertices of \(S\) are chosen inside \(A\). Explain why choosing them in all of \(V(P)\) would not work with the same estimate for \(T(S)\).

## 5. Solutions

**4.1.** The function \(e^y-1-y\) has derivative \(e^y-1\), negative for \(y<0\) and positive for \(y>0\), so its minimum is its value \(0\) at \(y=0\).

**4.2.** An edge \(xy\) meets at most \(r-2\) other edges at \(x\) and at most \(r-2\) at \(y\). When it is coloured, at most \(2r-4\) colours are excluded, so one of \(2r-3\) colours is free.

**4.3.** With \(t=\ln3\), the bound on \(\mathbb Ee^{tX}\) and Lemma 1.1 give
\[
\begin{aligned}
\Pr(X\ge3\mu)&\le e^{\mu(3-1)-3\mu\ln3}\\
&=e^{-\mu(3\ln3-2)},
\end{aligned}
\]
and \(3\ln3-2>1.29>1\).

**4.4.** The estimate \(\mathbb ET(S)\le\frac Mhe_P(A,V'\setminus A)\) counts, for each outside vertex \(w\), its neighbours that could enter \(S\). If \(S\) could contain vertices outside \(A\), a vertex of \(V'\setminus A\) could have many neighbours outside \(A\), and \(T(S)\) would not be controlled by the few edges leaving \(A\).

## References

- [OpenAI-EG] OpenAI, *A linear cycle-and-edge decomposition of every graph*, OpenAI Math Release preprint, 24 September 2026. https://github.com/openai/math/tree/main/preprints/A-linear-cycle-and-edge-decomposition-of-every-graph-September-24-2026
- [BM] M. Bucić and R. Montgomery, *Towards the Erdős–Gallai cycle decomposition conjecture*, Advances in Mathematics 437 (2024), 109434; arXiv:2211.07689. https://arxiv.org/abs/2211.07689
