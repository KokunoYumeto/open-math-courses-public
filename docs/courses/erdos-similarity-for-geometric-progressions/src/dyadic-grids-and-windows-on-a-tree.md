# Dyadic grids and windows on a tree

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The periodic hitting set of Proposition 3.1 of [Measure-universal sets and periodic hitting sets](measure-universal-sets-and-periodic-hitting-sets.md) is built from random tables indexed by the cells of finitely many grids. This lesson sets up the grids and the bookkeeping of the indices \(n\) of the points \(x+tq^n\) [OpenAI-ES, Section 3]. The indices are grouped into windows attached to the edges of a finite ordered tree, and two facts are proved. For all centers \(x\) outside a periodic set of small density, the points \(x+tq^n\) with \(n\) in a window lie in the same cells as \(x\) in the grids of all earlier windows. And within one window, the points \(x\) and \(x+tq^n\) lie in pairwise distinct cells of that window's grid, at every center.

- Dyadic grids and keys (Section 1).
- Windows on an ordered tree (Section 2).
- Stable centers (Section 3).
- Separation within a window (Section 4).

Throughout, \(q\in(0,1)\) is fixed, \(m\) is Lebesgue measure, and \(\rho\) is the density of a measurable \(1\)-periodic set, as in [Measure-universal sets and periodic hitting sets](measure-universal-sets-and-periodic-hitting-sets.md). We write \(\{z\}=z-\lfloor z\rfloor\) for the fractional part and put
\[
c=\frac4{1-q}.
\]

## 1. Dyadic grids and keys

For each integer \(b\ge1\) put
\[
\begin{gathered}N_b=2^{\lceil\log_2(cq^{-b})\rceil},\qquad\Gamma_b=N_b^{-1}\mathbb Z,\\ J_b(z)=\bigl\lfloor N_b\{z\}\bigr\rfloor\in\{0,1,\ldots,N_b-1\}.\end{gathered}
\]
The number \(J_b(z)\) is the *key* of \(z\) at resolution \(b\). The points with key \(k\) form the *cell* \(\bigl[\frac k{N_b},\frac{k+1}{N_b}\bigr)+\mathbb Z\): cells are closed on the left and open on the right, so a point of \(\Gamma_b\) belongs to the cell on its right.

**Lemma 1.1** (grids). 

1. \(cq^{-b}\le N_b<2cq^{-b}\).
2. \(N_b\) is a power of two and nondecreasing in \(b\). If \(b'\ge b\), then \(N_{b'}/N_b\) is an integer and \(J_b(z)=\bigl\lfloor J_{b'}(z)\big/(N_{b'}/N_b)\bigr\rfloor\) for every \(z\): a finer key determines every coarser key.
3. \(J_b\) is \(1\)-periodic. On a segment \([u,v]\) with \((u,v]\cap\Gamma_b=\varnothing\), \(J_b\) is constant.

*Proof.* (1) For \(y>0\), \(2^{\lceil\log_2y\rceil}\) is the least power of two that is at least \(y\), so it lies in \([y,2y)\). (2) \(cq^{-b}\) increases with \(b\). Put \(K=N_{b'}/N_b\), an integer power of two, and \(y=N_{b'}\{z\}\), so \(J_{b'}(z)=\lfloor y\rfloor\) and \(J_b(z)=\lfloor y/K\rfloor\). Write \(\lfloor y\rfloor=Kj+i\) with integers \(j\) and \(0\le i<K\). Then \(j\le y/K<(Kj+i+1)/K\le j+1\), so \(\lfloor y/K\rfloor=j=\lfloor\lfloor y\rfloor/K\rfloor\). (3) Periodicity is clear, and \(J_b(z)=\lfloor N_bz\rfloor-N_b\lfloor z\rfloor\) because \(N_b\lfloor z\rfloor\) is an integer. Let \(u\le w\le v\). An integer \(k\) with \(N_bu<k\le N_bw\) would give the point \(k/N_b\) of \(\Gamma_b\) in \((u,v]\); so \(\lfloor N_bw\rfloor=\lfloor N_bu\rfloor\). Likewise \(\lfloor w\rfloor=\lfloor u\rfloor\), since the integers belong to \(\Gamma_b\). Hence \(J_b(w)=J_b(u)\). \(\square\)

So each cell of the grid \(\Gamma_b\) has width \(1/N_b\le q^b/c=\frac{(1-q)q^b}4\). The grids are dyadic even when \(q\) is not, so that coarser keys are functions of finer ones; their resolutions follow \(q^{-b}\).

## 2. Windows on an ordered tree

Fix integers \(M\ge2\), \(d\ge1\), \(g\ge1\) and \(r_0\ge1\). Take the complete ordered \(M\)-ary tree of height \(d\): every vertex of height \(h\ge1\) has \(M\) children \(P_1,\ldots,P_M\), in this order, of height \(h-1\), and the leaves have height \(0\). Write \((P,i)\) for the edge from \(P\) to \(P_i\); there are
\[
K=M+M^2+\cdots+M^d
\]
edges. The *preorder* of the edges lists, for \(i=1,\ldots,M\) in turn, the edge \((P,i)\) followed by all edges of the subtree rooted at \(P_i\) in preorder, starting at the root. So an edge and the subtree below it form a consecutive block.

Put \(r_1=r_0\), \(\sigma_1=Mr_1+(M-1)g\), and for \(2\le h\le d\)
\[
\begin{gathered}r_h=\max\{r_0,\ g+\sigma_{h-1}\},\\ \sigma_h=M\bigl(r_h+g+\sigma_{h-1}\bigr)+(M-1)g .\end{gathered}
\]
Choose an integer \(n_0\ge1\) with \(2q^{n_0}\le\frac14\). Now assign to the edges, in preorder, consecutive sets of integers \(W_e=\{a_e,a_e+1,\ldots,b_e\}\), the *windows*: the first window starts at \(n_0\), an edge leaving a vertex of height \(h\) gets a window of exactly \(r_h\) integers, and between consecutive windows exactly \(g\) integers are left unused. Put
\[
\mathcal N=\bigcup_eW_e ,
\]
and for an edge \(e=(P,i)\) let \(b_e^*\) be the largest endpoint among \(W_e\) and the windows of the edges below \(P_i\). The grid of the edge \(e\) is \(\Gamma_{b_e}\).

**Lemma 2.1** (spans; [OpenAI-ES, Lemma 3.1]). For a vertex \(P\) of height \(h\ge1\), the windows of all edges below \(P\), together with the gaps between them, occupy exactly \(\sigma_h\) consecutive integers. For an edge \(e=(P,i)\) leaving a vertex of height \(h\),
\[
b_e^*-a_e+1\le2r_h .
\tag{2.1}
\]

*Proof.* By induction on \(h\). If \(h=1\), the edges below \(P\) are \((P,1),\ldots,(P,M)\), consecutive in preorder, with windows of length \(r_1\) and \(M-1\) gaps between them: \(\sigma_1\) integers. If \(h\ge2\), preorder lists the blocks \((P,i)\), subtree of \(P_i\), for \(i=1,\ldots,M\). A block consists of a window of length \(r_h\), a gap, and the windows below \(P_i\), which occupy \(\sigma_{h-1}\) integers by induction; consecutive blocks are separated by a gap. This gives \(M(r_h+g+\sigma_{h-1})+(M-1)g=\sigma_h\).

For (2.1): \(b_e^*-a_e+1\) is the number of integers occupied by the block of \(e\). If \(h=1\), \(P_i\) is a leaf and the block is \(W_e\), of length \(r_1\). If \(h\ge2\), the block has length \(r_h+g+\sigma_{h-1}\le2r_h\) by the choice of \(r_h\). \(\square\)

So the finest grid used anywhere in the block of an edge has index at most \(2r_h-1\) beyond the start of its window. This is what keeps the number of grid boundaries under control in [Every scale and every center](every-scale-and-every-center.md); the gaps serve the next lemma.

## 3. Stable centers

**Definition 3.1.** A point \(x\in\mathbb R\) is *stable* if for every window \(W_e\) other than the first, with \(b'\) the right endpoint of the window immediately before \(W_e\),
\[
(x,\ x+2q^{a_e}]\cap\Gamma_{b'}=\varnothing .
\]
We write \(\mathcal S\) for the set of stable points.

The left endpoint \(x\) is excluded because a point of \(\Gamma_{b'}\) at \(x\) itself belongs to the cell on its right, which the points \(x+tq^n\) do not leave; the right endpoint is included because reaching the next point of \(\Gamma_{b'}\) does change the key.

**Lemma 3.2** (stable centers keep earlier keys; [OpenAI-ES, Lemma 3.2]). The set \(\mathcal S\) is measurable and \(1\)-periodic, and
\[
\rho(\mathbb R\setminus\mathcal S)\le4Kc\,q^{g+1}.
\tag{3.1}
\]
If \(x\in\mathcal S\), \(n\in W_e\) and \(t\in[1,2]\), then every edge \(f\) before \(e\) in preorder satisfies
\[
J_{b_f}(x+tq^n)=J_{b_f}(x).
\tag{3.2}
\]

*Proof.* For a window \(W_e\) other than the first, with \(b'\) as in Definition 3.1, the condition fails exactly when some \(\gamma\in\Gamma_{b'}\) satisfies \(x<\gamma\le x+2q^{a_e}\), that is, on the union of the intervals \([\gamma-2q^{a_e},\gamma)\), \(\gamma\in\Gamma_{b'}\). This union is \(V+\mathbb Z\), where \(V\) is the union of the \(N_{b'}\) intervals \([\gamma-2q^{a_e},\gamma)\) with \(\gamma\in\Gamma_{b'}\cap[0,1)\); it is \(1\)-periodic and measurable. For any measurable \(V\), translation invariance and countable subadditivity give
\[
\begin{aligned}\rho(V+\mathbb Z)&\le\sum_{k\in\mathbb Z}m\bigl((V+k)\cap[0,1)\bigr)\\&=\sum_{k\in\mathbb Z}m\bigl(V\cap[-k,1-k)\bigr)\\&=m(V).\end{aligned}
\]
So the density of the union is at most
\[
2N_{b'}q^{a_e}<4c\,q^{a_e-b'}=4c\,q^{g+1},
\]
by Lemma 1.1(1) and \(a_e=b'+g+1\). There are at most \(K\) such windows, which proves (3.1); \(\mathcal S\) is the complement of a finite union of measurable periodic sets.

Let \(x\in\mathcal S\), \(n\in W_e\) and \(t\in[1,2]\). If \(e\) is the first edge, (3.2) is empty. Otherwise \(0<tq^n\le2q^{a_e}\), so \((x,x+tq^n]\) contains no point of \(\Gamma_{b'}\), and \(J_{b'}(x+tq^n)=J_{b'}(x)\) by Lemma 1.1(3). An edge \(f\) before \(e\) has its window before \(W_e\), so \(b_f\le b'\), and Lemma 1.1(2) turns the equality of the keys at resolution \(b'\) into (3.2). \(\square\)

## 4. Separation within a window

**Lemma 4.1** (separation; [OpenAI-ES, Lemma 3.3]). Let \(e\) be an edge, \(x\in\mathbb R\) and \(t\in[1,2]\). The points
\[
x\quad\text{and}\quad x+tq^n\ (n\in W_e)
\]
have pairwise distinct keys under \(J_b\) for every \(b\ge b_e\).

*Proof.* All these points lie in \([x,x+2q^{n_0}]\), an interval of length at most \(\frac14\), since every window consists of integers \(n\ge n_0\). The distance from \(x\) to \(x+tq^n\) is \(tq^n\ge q^{b_e}\). For \(n<n'\) in \(W_e\),
\[
\begin{aligned}t(q^n-q^{n'})&=tq^n(1-q^{n'-n})\\&\ge(1-q)q^{b_e}.\end{aligned}
\]
If two points \(z,w\) have the same key at resolution \(b\), their fractional parts lie in one interval \(\bigl[\frac k{N_b},\frac{k+1}{N_b}\bigr)\), so \(|z-w-j|<1/N_b\) for the integer \(j=\lfloor z\rfloor-\lfloor w\rfloor\). If moreover \(|z-w|<\frac14\), then \(j=0\), since otherwise \(|z-w-j|\ge1-|z-w|>\frac34>1/N_b\); so \(|z-w|<1/N_b\). But by Lemma 1.1(1)
\[
\begin{aligned}\frac1{N_b}&\le\frac1{N_{b_e}}\le\frac{q^{b_e}}c\\&=\frac{(1-q)q^{b_e}}4<(1-q)q^{b_e},\end{aligned}
\]
smaller than every distance between our points. \(\square\)

At a stable center, the random construction of [Random routing and independent tests](random-routing-and-independent-tests.md) will therefore read the same earlier table entries at \(x\) and at \(x+tq^n\), while the points of one window read pairwise distinct entries of their own table.

## 5. Exercises

**5.1.** For \(q=\frac12\), compute \(c\), \(N_b\) and the width of the cells of \(\Gamma_b\).

**5.2.** Show that \(\lfloor\lfloor y\rfloor/K\rfloor=\lfloor y/K\rfloor\) can fail when \(K>0\) is not an integer.

**5.3.** Let \(M=2\), \(d=3\), \(g=1\) and \(r_0=1\), and take \(n_0=1\), which is allowed when \(q\le\frac18\). Compute \(r_1,r_2,r_3\) and \(\sigma_1,\sigma_2,\sigma_3\), list the windows in preorder, and check (2.1) for the two edges leaving the root.

**5.4.** Show that \(K=(M^{d+1}-M)/(M-1)\) and that the windows occupy \(\sigma_d\) consecutive integers in total.

**5.5.** Show that the bound (3.1) tends to \(0\) as \(g\to\infty\) with \(M\) and \(d\) fixed, but that the windows then become longer: show that \(r_h\ge g\) for \(h\ge2\).

## 6. Solutions

**5.1.** \(c=8\), \(cq^{-b}=2^{b+3}\) is a power of two, so \(N_b=2^{b+3}\) and the cells have width \(2^{-b-3}\).

**5.2.** For \(K=\frac12\) and \(y=\frac12\): \(\lfloor\lfloor y\rfloor/K\rfloor=0\) but \(\lfloor y/K\rfloor=1\).

**5.3.** \(r_1=1\), \(\sigma_1=3\); \(r_2=\max(1,1+3)=4\), \(\sigma_2=2(4+1+3)+1=17\); \(r_3=\max(1,1+17)=18\), \(\sigma_3=2(18+1+17)+1=73\). Write \(R\) for the root, \(A,B\) for its children and \(A_1,A_2,B_1,B_2\) for theirs. In preorder, with one unused integer between windows: \((R,1)\): \(1\)–\(18\); \((A,1)\): \(20\)–\(23\); \((A_1,1)\): \(25\); \((A_1,2)\): \(27\); \((A,2)\): \(29\)–\(32\); \((A_2,1)\): \(34\); \((A_2,2)\): \(36\); \((R,2)\): \(38\)–\(55\); \((B,1)\): \(57\)–\(60\); \((B_1,1)\): \(62\); \((B_1,2)\): \(64\); \((B,2)\): \(66\)–\(69\); \((B_2,1)\): \(71\); \((B_2,2)\): \(73\). The windows fill \(1\)–\(73\), that is \(\sigma_3\) integers. For \((R,1)\), \(b^*=36\) and \(b^*-a+1=36=2r_3\); for \((R,2)\), \(b^*=73\) and \(73-38+1=36=2r_3\).

**5.4.** There are \(M^j\) vertices of height \(d-j\), and each vertex other than the root has exactly one incoming edge; so \(K=\sum_{j=1}^dM^j=(M^{d+1}-M)/(M-1)\). The second claim is Lemma 2.1 for the root.

**5.5.** \(4Kcq^{g+1}\to0\) as \(g\to\infty\) because \(q<1\). For \(h\ge2\), \(r_h\ge g+\sigma_{h-1}>g\). Choosing \(g\) large makes most centers stable, at the price of longer windows above height one; the choice of parameters in [Every scale and every center](every-scale-and-every-center.md) takes \(g\) after \(M\) and \(d\), and the window lengths do not enter the bound that \(g\) must satisfy.

## References

- [OpenAI-ES] OpenAI, *The geometric case of the Erdős similarity conjecture*, OpenAI Math Release preprint, 5 October 2026, Section 3. https://github.com/openai/math/tree/main/preprints/The-geometric-case-of-the-Erdos-similarity-conjecture-October-5-2026
