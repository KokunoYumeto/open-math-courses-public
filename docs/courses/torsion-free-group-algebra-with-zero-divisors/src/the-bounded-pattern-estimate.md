# The bounded-pattern estimate

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson proves the bounded-pattern estimate, Proposition 1.2 of [Image graphs and multiplicity stages](image-graphs-and-multiplicity-stages.md) [OpenAI-KZ, Section 3], with the tools of that lesson and of [Aligned blocks and word counts](aligned-blocks-and-word-counts.md). For every enlarged pattern and every multiplicity stage we bound the expected number of realizations of that stage in the random graph: vertex choices give powers of \(n\), edge prescriptions give powers of \(1/n\), and the letters along the blocks give the factors \(P(W_i)\). Counting the letters that a stage can carry uses the propagation along links and the bins of [Aligned blocks and word counts](aligned-blocks-and-word-counts.md). Multiplying the bounds over all stages makes the powers of \(n\) cancel by the stage balance and leaves an exponentially small number; so one stage has a small expected count, which bounds the probability that the whole pattern is realized.

- Realizations of a stage (Section 1).
- Fixed letters (Section 2).
- Permitted letters (Section 3).
- The product over the stages (Section 4).
- Proof of the bounded-pattern estimate (Section 5).

We use the random graph \(\Gamma\) conditioned on girth at least \(L\), with the prescription bound (3.1) of [Random matchings with large girth](random-matchings-with-large-girth.md); the turn weights \(w(t,u)\), word weights \(P(W)\) and \(p=129/16513\) of [Projective planes and prescribed types](projective-planes-and-prescribed-types.md); the stages \(\Delta_j\), the counts \(E_j,V_j\), the numbers \(k_j\) and the balance (5.2) of [Image graphs and multiplicity stages](image-graphs-and-multiplicity-stages.md); and the blocks, bins, link components and Lemmas 3.1, 4.1–4.3, 5.1 and 5.2 of [Aligned blocks and word counts](aligned-blocks-and-word-counts.md), with \(\delta=1/600\) and \(a_0=2\log129\).

## 1. Realizations of a stage

Fix an enlarged pattern: an unlabelled pattern together with the bins \(d_i\) of its full blocks. It determines \(H\), \(b\), the stages, the blocks and the link graph. A *permitted letter assignment* on \(\Delta_j\) is the restriction to \(\Delta_j\) of a word assignment on \(\Delta\), in the sense of Section 4 of [Aligned blocks and word counts](aligned-blocks-and-word-counts.md), whose block words have the prescribed bins. A *realization* of the stage \(\Delta_j\) with a permitted letter assignment is an injective map of the vertices and edges of \(\Delta_j\) into \(\Gamma\), on the prescribed sides, sending every edge to an edge of \(\Gamma\) carrying the assigned letter, and sending the starting vertex of the interval path to the prescribed vertex \(x_A\) or \(x_B\) when \(j=1\) and \(\iota=1\). Let \(X_j\) be the number of pairs (permitted letter assignment, realization). A system realizing the enlarged pattern restricts to a realization of every stage, so it forces \(X_j\ge1\) for every \(j\). The condition is only on the letters, not on an embedding of the rest of \(\Delta\).

## 2. Fixed letters

For a stage \(j\) let \(D_j=\sum_{i:\,m_i\ge j}d_i\) be the sum of the bins of the full blocks of \(\Delta_j\).

**Lemma 2.1** (fixed letters; [OpenAI-KZ, Section 3]). For a fixed permitted letter assignment on \(\Delta_j\), the expected number of realizations of \(\Delta_j\) with these letters is at most
\[
n^{V_j-E_j-k_j}e^{-D_j+o(L)}.\tag{2.1}
\]

*Proof.* Let \(Q_j\) be the number of chains in \(\Delta_j\); every chain of \(\Delta_j\) is a whole chain of \(\Delta\), so \(\Delta_j\) has \(E_j-Q_j\) interior chain vertices. An interior vertex between an incoming letter \(t\) and an outgoing letter \(u\), read in the chain orientation, must be mapped to a vertex of its side whose type contains \(\bar t\) and \(u\). On \(B\) there are exactly \(np\,w(t,u)\) such vertices, and on \(A\) at most that many, by Lemma 2.1(1) and Lemma 3.1(1)–(2) of [Projective planes and prescribed types](projective-planes-and-prescribed-types.md). The other vertices have at most \(n\) images each, and a prescribed vertex has one. So the number of vertex maps is at most
\[
n^{V_j-k_j}\,p^{E_j-Q_j}\prod_{\text{interior turns}}w(t,u).
\]
For an injective vertex map, the \(E_j\) edges require \(E_j\) prescriptions of matched pairs, all distinct: two distinct edges prescribing the same pair would have the same ends and the same letter at a common end, and in an immersed graph they would be the same edge of \(\Gamma\), contrary to injectivity on edges. Since \(E_j\le CL\), these prescriptions hold with probability at most \((np)^{-E_j}e^{o(L)}\), by (3.1) of [Random matchings with large girth](random-matchings-with-large-girth.md). Multiplying gives
\[
n^{V_j-E_j-k_j}\,p^{-Q_j}\,e^{o(L)}\prod_{\text{interior turns}}w(t,u).
\]
The number \(Q_j\) is bounded, so \(p^{-Q_j}=e^{O(1)}\). Every turn weight is at most \(1\), so the product over interior turns is at most the product over the turns inside the full blocks of \(\Delta_j\), which is \(\prod_{i:\,m_i\ge j}P(W_i)\le e^{-D_j}\). \(\square\)

## 3. Permitted letters

**Lemma 3.1** (permitted letters; [OpenAI-KZ, Section 3]). The number of permitted letter assignments on \(\Delta_j\) is at most
\[
\begin{aligned}&\exp\Bigl(o(L)+{}\\&\ \ \sum_{\mathcal U}\bigl(2d_{\min}(\mathcal U)-\delta s\bigr)\Bigr),\end{aligned}\tag{3.1}
\]
where the sum runs over the link components \(\mathcal U\) without self-links with \(z_{\mathcal U}\ge j\), and \(d_{\min}(\mathcal U)=\min_{i\in\mathcal U}d_i\).

*Proof.* A permitted letter assignment on \(\Delta_j\) is determined by the words on the full blocks of \(\Delta_j\) and the letters on the end fragments of its chains. The end fragments have at most \(s+1\) positions on each of the boundedly many chains, giving at most \((\#T)^{O(s)}=e^{o(L)}\) choices. The full blocks of \(\Delta_j\) are those with \(m_i\ge j\); they lie in the link components \(\mathcal U\) with \(z_{\mathcal U}\ge j\). For each such component, the words on its blocks of \(\Delta_j\) are the restriction of the words on all its blocks in a word assignment, so their number is at most the number of compatible words on all blocks of \(\mathcal U\) with the prescribed bins. If \(\mathcal U\) has no self-link, choose a block \(i_0\) with \(d_{i_0}=d_{\min}(\mathcal U)\); it has at most \(\exp(2d_{\min}(\mathcal U)-\delta s)\) words by Lemma 5.1, and each extends in at most \(\exp(o(s)\#\mathcal U)\) ways by Lemma 4.1. If \(\mathcal U\) has a self-link, Lemmas 4.2 and 4.1 give at most \(\exp(o(s)\#\mathcal U)\) words in all. There are \(O(L/s)\) blocks, so the factors \(\exp(o(s)\#\mathcal U)\) multiply to \(e^{o(L)}\). \(\square\)

Let \(B_j\) be the product of (2.1) and (3.1). Summing (2.1) over the permitted letter assignments gives
\[
\mathbb E\,X_j\le B_j .\tag{3.2}
\]

## 4. The product over the stages

**Lemma 4.1** (product bound). For every enlarged pattern,
\[
\begin{aligned}\log\prod_{j=1}^{m_*}B_j&\le-\frac\delta2H\\&\quad+a_0b+o(L).\end{aligned}\tag{4.1}
\]

*Proof.* There are at most \(2(C+K)\) stages, by (3.1) of [Image graphs and multiplicity stages](image-graphs-and-multiplicity-stages.md), so the error terms add up to \(o(L)\). The powers of \(n\) multiply to \(n^{\sum_j(V_j-E_j-k_j)}\le1\) by the balance (5.2) of that lesson. A block \(i\) lies in \(\Delta_j\) for exactly \(m_i\) stages, and a component \(\mathcal U\) has \(z_{\mathcal U}\ge j\) for exactly \(z_{\mathcal U}\) stages. So the remaining logarithm is \(\sum_{\mathcal U}F_{\mathcal U}+o(L)\), with
\[
\begin{aligned}F_{\mathcal U}&=-\sum_{i\in\mathcal U}m_id_i\\&\quad+\epsilon_{\mathcal U}z_{\mathcal U}\bigl(2d_{\min}(\mathcal U)-\delta s\bigr),\end{aligned}
\]
where \(\epsilon_{\mathcal U}=1\) if \(\mathcal U\) has no self-link and \(0\) otherwise. Write \(d_{\min}\), \(S\), \(z\), \(b'\) for \(d_{\min}(\mathcal U)\), \(S_{\mathcal U}\), \(z_{\mathcal U}\), \(b_{\mathcal U}\). We show
\[
F_{\mathcal U}\le-\frac\delta2sS+a_0s\,b'.\tag{4.2}
\]
Since \(d_i\ge d_{\min}\) for \(i\in\mathcal U\), the first sum is at least \(Sd_{\min}\).

- If \(\mathcal U\) has a self-link, \(F_{\mathcal U}\le-Sd_{\min}\le-\frac\delta2sS\) by Lemma 5.1 of [Aligned blocks and word counts](aligned-blocks-and-word-counts.md).
- If \(\mathcal U\) has no self-link and \(2z\le S\), then
\[
\begin{aligned}
F_{\mathcal U}&\le-(S-2z)d_{\min}-\delta sz\\
&\le-(S-2z)\frac{\delta s}2-\delta sz\\
&=-\frac\delta2sS.
\end{aligned}
\]
- If \(\mathcal U\) has no self-link and \(2z>S\), then \(2z-S\le b'\) by Lemma 4.3 of that lesson, and \(d_{\min}\le a_0s\), so
\[
\begin{aligned}
F_{\mathcal U}&\le(2z-S)d_{\min}-\delta sz\\
&\le a_0s\,b'-\frac\delta2sS,
\end{aligned}
\]
using \(z>S/2\).

Summing (4.2): \(\sum_{\mathcal U}S_{\mathcal U}=\sum_im_i\), and
\[
\begin{aligned}s\sum_im_i&\ge\sum_im_ih_i-O(L/s)\\&\ge H-O(s+L/s),\end{aligned}
\]
since the positions outside full blocks lie in boundedly many end fragments of fewer than \(s+1\) positions, traversed boundedly often. Also \(s\sum_{\mathcal U}b_{\mathcal U}=sb_*\le b+o(L)\) by Lemma 3.1 of that lesson. Hence \(\sum_{\mathcal U}F_{\mathcal U}\le-\frac\delta2H+a_0b+o(L)\). \(\square\)

## 5. Proof of the bounded-pattern estimate

*Proof of Proposition 1.2 of [Image graphs and multiplicity stages](image-graphs-and-multiplicity-stages.md).* Put
\[
\varepsilon=\min\Bigl\{\frac14,\ \frac\delta{16(1+a_0)}\Bigr\}>0 ;
\]
it depends only on the turn weights, through \(\delta\) and \(a_0\). Now fix \(K\), \(C\) and \(I\). For an enlarged pattern with \(L\le H\le CL\) and \(b\le\varepsilon H\), we have \(a_0b\le\frac\delta{16}H\), so (4.1) gives
\[
\begin{aligned}\log\prod_jB_j&\le-\frac\delta2H+\frac\delta{16}H+o(L)\\&\le-\frac\delta4H\end{aligned}
\]
for large \(L\), since \(H\ge L\). Let \(M=\max\{1,\lceil2(C+K)\rceil\}\), so that there are at most \(M\) stages. Since the product of the \(B_j\) is at most \(1\), the smallest of them is at most their geometric mean, and some stage has \(B_j\le e^{-\delta H/(4M)}\le e^{-\delta L/(4M)}\). For that stage, by (3.2),
\[
\begin{aligned}&\Pr(\text{the enlarged pattern is realized})\\&\quad\le\Pr(X_j\ge1)\le\mathbb E\,X_j\le e^{-\delta L/(4M)} .\end{aligned}
\]
No independence between the stages is used; the product of the \(B_j\) only serves to find one stage with a small bound. By Lemma 5.2 of [Aligned blocks and word counts](aligned-blocks-and-word-counts.md), there are \(\exp(o(L))\) enlarged patterns, so the probability that some system as in the proposition exists is at most \(\exp(o(L)-\delta L/(4M))\), which tends to \(0\). \(\square\)

## 6. Exercises

**6.1.** Show that if \(B_1,\ldots,B_m>0\) and \(\prod_jB_j\le e^{-x}\) with \(x\ge0\), then \(\min_jB_j\le e^{-x/m}\).

**6.2.** Compute \(a_0\) and \(\varepsilon\) numerically for \(\delta=1/600\).

**6.3.** Explain why Lemma 2.1 bounds the number of vertex images on side \(A\) by \(np\,w(t,u)\), although the proportions on \(A\) can differ from those on \(B\).

**6.4.** Where in the proof of Lemma 4.1 is it used that the root of a component without self-links is chosen with the smallest bin?

**6.5.** Suppose the turn weights were all equal to \(1\). Which estimate of this lesson would fail?

## 7. Solutions

**6.1.** If every \(B_j>e^{-x/m}\), then \(\prod_jB_j>e^{-x}\).

**6.2.** \(a_0=2\log129\approx9.72\), so \(16(1+a_0)\approx171.5\) and \(\varepsilon=\delta/171.5\approx9.7\cdot10^{-6}\).

**6.3.** By Lemma 3.1(2) of [Projective planes and prescribed types](projective-planes-and-prescribed-types.md), among the \(np\) vertices of \(A\) containing \(\bar t\) at most a proportion \(w(t,u)\) contain \(u\).

**6.4.** In the second and third cases. The root contributes \(z(2d_{i_0}-\delta s)\) to \(F_{\mathcal U}\), and the blocks contribute \(-\sum_im_id_i\le-Sd_{\min}\). With \(d_{i_0}=d_{\min}\) the two combine to \((2z-S)d_{\min}-\delta sz\). With a root of larger bin the positive term \(2zd_{i_0}\) could exceed what \(Sd_{\min}\) cancels.

**6.5.** Every word without cancelling turns would have \(P(W)=1\) and bin \(0\), so the lower bound \(d_i\ge\delta s/2\) of Lemma 5.1 of [Aligned blocks and word counts](aligned-blocks-and-word-counts.md) would fail, and the number of words of length \(h\) with bin \(0\) would be \(\#T(\#T-1)^{h-1}\), not at most \(e^{-\delta s}\). Then (4.2) fails: a component with a self-link would give \(F_{\mathcal U}=0\), and the letter count of Lemma 3.1 would grow exponentially in \(s\). The powers of \(n\) still balance, but no decay remains.

## References

- [OpenAI-KZ] OpenAI, *A Torsion-Free Group Algebra with Zero Divisors*, OpenAI Math Release preprint, 23 September 2026, Section 3. https://github.com/openai/math/tree/main/preprints/A-Torsion-Free-Group-Algebra-with-Zero-Divisors-September-23-2026
