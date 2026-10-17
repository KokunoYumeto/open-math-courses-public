# Levels and k-sets

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson deduces Corollary C of [Halving lines and rank sweeps](halving-lines-and-rank-sweeps.md): an \(n\)-point set has at most \(C_0n(k+1)^{1/3-\varepsilon_0}\) subsets that are \(k\)-sets, improving Dey's \(O(n(k+1)^{1/3})\). OpenAI [OpenAI-HL, Section 8] derives it from Theorem B with Matoušek's shallow cutting lemma, in the form of Agarwal, Aronov, Chan and Sharir [AACS, Lemma 3.2]. The same paper gives a second route, by random sampling below a lower envelope and the moment bound of Clarkson and Shor [AACS, proof of Theorem 3.1]; this lesson follows that route in the plane and proves everything it uses. The uniformity of Theorem B in the rank is what makes the reduction work: the level of the full arrangement becomes a level of a different rank in each piece.

## 1. Duality

A *line arrangement* \(H\) is a finite set of non-vertical lines. It is in *general position* if no two lines are parallel, no three pass through one point, and different intersection points, the *vertices*, have different first coordinates. For a vertex \(v\), its *level* is the number of lines of \(H\) passing strictly below \(v\). Let \(V_j(H)\) be the set of vertices of level \(j\).

To a point \(q=(a,b)\) associate the line \(\ell_q=\{(s,y):y=b-as\}\). Then the height of \(\ell_q\) at abscissa \(s\) is \(\varphi_s(q)=b-as\), the projection of [Halving lines and rank sweeps](halving-lines-and-rank-sweeps.md). For a configuration \(Q\) of points, the dual arrangement \(Q^*=\{\ell_q\}\) is in general position exactly when \(Q\) satisfies (G1)–(G3): distinct first coordinates give distinct slopes, three points on a line give three concurrent lines, and the vertex of \(\ell_q\) and \(\ell_{q'}\) lies at \(s=\sigma_{qq'}\), the slope of the segment \(qq'\).

**Lemma 1.1.** Let \(Q\) satisfy (G1)–(G3). For every \(j\), \(|V_j(Q^*)|\) is the number of pairs \(\{q,q'\}\) with exactly \(j\) points of \(Q\) strictly below the line \(qq'\). If \(Q\) is generic, \(|V_j(Q^*)|=S_{j+1}(Q)\).

*Proof.* The vertex of \(\ell_q\) and \(\ell_{q'}\) is at \(s=\sigma_{qq'}\), and \(\ell_m\) passes below it exactly when \(\varphi_\sigma(q_m)<\varphi_\sigma(q)\), that is, when \(q_m\) lies below the line \(qq'\). For generic \(Q\), the proof of Lemma 2.2 of [Halving lines and rank sweeps](halving-lines-and-rank-sweeps.md) shows that the step crossing \(\sigma_{qq'}\) is a switch of rank \(j+1\) exactly when \(j\) points lie below the line \(qq'\). \(\square\)

**Corollary 1.2.** Let \(\varepsilon\) and \(C\) be the constants of Theorem B. Every line arrangement \(H\) of \(m\) lines in general position satisfies \(|V_j(H)|\le Cm^{4/3-\varepsilon}\) for all \(j\).

*Proof.* \(H=Q^*\) for a configuration \(Q\) satisfying (G1)–(G3). By Lemma 1.1 of [Halving lines and rank sweeps](halving-lines-and-rank-sweeps.md), \(Q\) has a generic perturbation \(Q'\) with the same orientations of all triples and the same order of first coordinates. Whether \(q_m\) lies below the line \(qq'\) is decided by the sign of \(\Delta(q,q',q_m)\) and the order of the first coordinates of \(q,q'\), so the counts of Lemma 1.1 are the same for \(Q\) and \(Q'\), and \(|V_j(Q^*)|=S_{j+1}(Q')\le Cm^{4/3-\varepsilon}\). \(\square\)

Put \(\varepsilon_0=\min(\varepsilon,1/6)\) and \(\beta=4/3-\varepsilon_0\); then Corollary 1.2 holds with \(\beta\) in place of \(4/3-\varepsilon\), and \(|V_j(H)|\le C|H|^\beta\) also when \(|H|\le1\), where there are no vertices.

## 2. Cells below a lower envelope

Fix an arrangement \(H\) of \(n\) lines in general position. For a subset \(R\subseteq H\), the *lower envelope* is the graph of \(\min_{h\in R}h\), a concave polygonal chain in which each line of \(R\) occupies at most one interval; so it has at most \(|R|\) edges. Its *cells* are the regions \(\{(s,y):s_l<s<s_r,\ y<h(s)\}\), one for each edge, where \(h\) is the line of the edge and \(s_l<s_r\) are the first coordinates of its ends, possibly infinite. If \(R=\varnothing\), the single cell is the whole plane. So \(R\) has at most \(|R|+1\) cells.

A cell \(\Delta\) is determined by its *defining set* \(D(\Delta)\): the line \(h\) of its edge and the lines meeting \(h\) at the finite ends, at most three lines; for \(R=\varnothing\), \(D=\varnothing\). Its *conflict set* \(K(\Delta)\) is the set of lines of \(H\) meeting \(\Delta\). The lines of \(D\) do not meet \(\Delta\): the envelope line at the left end has larger slope than \(h\), since the envelope is concave, so it lies above \(h\) to the right of the end, and symmetrically at the right end. A *potential cell* is a region of this form, for some set \(D\subseteq H\) of at most three lines arranged in this way.

**Lemma 2.1.** A potential cell \(\Delta\) is a cell of \(R\) exactly when \(D(\Delta)\subseteq R\) and \(K(\Delta)\cap R=\varnothing\).

*Proof.* If \(\Delta\) is a cell of \(R\), its defining lines are in \(R\), and no line of \(R\) passes below the envelope. Conversely, if \(D(\Delta)\subseteq R\) and no line of \(R\) meets \(\Delta\), then over \((s_l,s_r)\) every line of \(R\) lies on or above \(h\), so \(h\) is the envelope there; at \(s_l\) the left defining line crosses \(h\) and lies below it further left, so \(s_l\) is an end of the edge, and likewise \(s_r\). \(\square\)

**Lemma 2.2** (moment bound). Let \(\gamma\ge0\). There is a constant \(C_\gamma\) such that if \(R\) is formed by choosing each line of \(H\) independently with probability \(p\in(0,1]\), then
\[
\mathbb E\sum_{\Delta\text{ cell of }R}|K(\Delta)|^\gamma\le C_\gamma\,(np+1)\,p^{-\gamma}.
\]

*Proof.* For a potential cell \(\Delta\) write \(d_\Delta=|D(\Delta)|\in\{0,1,2,3\}\) and \(t_\Delta=|K(\Delta)|\). By Lemma 2.1, \(\Delta\) is a cell of \(R\) with probability \(p^{d_\Delta}(1-p)^{t_\Delta}\). So the left side equals \(\sum_\Delta t_\Delta^\gamma p^{d_\Delta}(1-p)^{t_\Delta}\).

*The empty sample.* The only potential cell with \(d_\Delta=0\) is the whole plane, with \(t_\Delta=n\). It contributes \(n^\gamma(1-p)^n\le n^\gamma e^{-pn}\le c_\gamma p^{-\gamma}\), where \(c_\gamma=\sup_{u\ge0}u^\gamma e^{-u}\).

*Counting potential cells.* For \(d\in\{1,2,3\}\) let \(N_d(x)\) be the number of potential cells with \(d_\Delta=d\) and \(t_\Delta\le x\). For \(x\ge2\), sample with probability \(1/x\): the expected number of cells is at most \(n/x+1\), and at least \(N_d(x)\,x^{-d}(1-1/x)^x\ge N_d(x)x^{-d}/4\). So \(N_d(x)\le4(n/x+1)x^d\le8(n+1)x^{d-1}\) for \(2\le x\le n+1\); for larger \(x\), \(N_d(x)=N_d(n+1)\le8(n+1)x^{d-1}\), since \(t_\Delta\le n\) and \(d\ge1\).

*Summing.* Split the potential cells with \(d_\Delta\ge1\) according to \(t_\Delta<2/p\) or \(2^i/p\le t_\Delta<2^{i+1}/p\), \(i\ge1\). In the first group the terms are at most \((2/p)^\gamma p^{d}\), and their sum is at most
\[
\begin{aligned}
&\sum_{d=1}^38(n+1)(2/p)^{d-1}(2/p)^\gamma p^d\\
&\quad\le56(n+1)\,p\,(2/p)^\gamma .
\end{aligned}
\]
In the \(i\)th group \((1-p)^{t_\Delta}\le e^{-2^i}\), and the sum is at most
\[
\begin{aligned}
&\sum_{d=1}^38(n+1)\Bigl(\frac{2^{i+1}}p\Bigr)^{d-1+\gamma}p^de^{-2^i}\\
&\quad\le24(n+1)\,p\,2^{(i+1)(\gamma+2)}p^{-\gamma}e^{-2^i}.
\end{aligned}
\]
The series over \(i\) converges. Since \((n+1)p\le np+1\), the bound follows with a constant depending only on \(\gamma\). \(\square\)

## 3. Levels with few lines below

**Proposition 3.1.** There is a constant \(C_2\) such that for every arrangement \(H\) of \(n\) lines in general position and every \(0\le k\le n\),
\[
|V_k(H)|\le C_2\,n\,(k+2)^{\beta-1}.
\]

*Proof.* Let \(p=1/(2(k+2))\) and form \(R\) as in Lemma 2.2. Let \(v\in V_k(H)\). With probability at least \((1-p)^{k+2}\ge1-(k+2)p=\frac12\), none of the \(k\) lines below \(v\) and neither line through \(v\) is in \(R\). Then every line of \(R\) passes strictly above \(v\), and \(v\) is not on a vertical boundary of a cell, which lies at the first coordinate of a vertex of two lines of \(R\); so \(v\) lies inside exactly one cell \(\Delta\) of \(R\). The two lines through \(v\) meet \(\Delta\), and so does every line passing below \(v\), since the vertical ray below \(v\) lies in \(\Delta\). A line not meeting \(\Delta\) lies above it, because \(\Delta\) is unbounded below. So \(v\) is a vertex of level \(k\) of the arrangement \(K(\Delta)\), which is in general position. Hence
\[
\begin{aligned}
\tfrac12|V_k(H)|&\le\mathbb E\sum_{\Delta}\bigl|V_k(K(\Delta))\bigr|\\
&\le C\,\mathbb E\sum_\Delta|K(\Delta)|^\beta\\
&\le CC_\beta(np+1)p^{-\beta},
\end{aligned}
\]
by Corollary 1.2 and Lemma 2.2. Since \(k\le n\), \(np\ge n/(2(n+2))\ge\frac16\), so \(np+1\le7np\), and \((np+1)p^{-\beta}\le7n\,p^{1-\beta}\), which is \(7\cdot2^{\beta-1}n(k+2)^{\beta-1}\). \(\square\)

Since \(\beta-1=\frac13-\varepsilon_0\), the levels of an arrangement of \(n\) lines have \(O(n(k+2)^{1/3-\varepsilon_0})\) vertices, uniformly in the level \(k\) counted from below; by reflecting in the first axis, the same holds for levels counted from above.

## 4. k-sets

**Proof of Corollary C.** Let \(Q\) be a set of \(n\ge2\) points with no three on a line and \(1\le k\le n/2\). Choose for each of its finitely many \(k\)-sets a separating line containing no point of \(Q\). A small perturbation keeps all these separations, so it does not decrease the number of \(k\)-sets; by Lemma 1.1 of [Halving lines and rank sweeps](halving-lines-and-rank-sweeps.md) we may assume \(Q\) generic.

A \(k\)-set is the set of points where some linear function \(x\mapsto u\cdot x\) takes its \(k\) smallest values, with no ties at the threshold. If \(u_2>0\), it is the marked set \(M_k(s)\) of the rank-\(k\) sweep for \(s=-u_1/u_2\), at a state or at a limit of states; if \(u_2<0\), it is the complement of a marked set \(M_{n-k}(s)\); if \(u_2=0\), it consists of the \(k\) leftmost or the \(k\) rightmost points, the marked sets at the first and last states of the rank-\(k\) sweep. The rank-\(k\) sweep has \(S_k(Q)+1\) marked sets, so
\[
\#\{k\text{-sets}\}\le S_k(Q)+S_{n-k}(Q)+2 .
\]
By Lemma 1.1, \(S_k(Q)=|V_{k-1}(Q^*)|\), and \(S_{n-k}(Q)=|V_{n-k-1}(Q^*)|\) counts the vertices with \(k-1\) lines above them. By Proposition 3.1 and its reflection, both are at most \(C_2n(k+1)^{1/3-\varepsilon_0}\), and the corollary follows with \(C_0=2C_2+2\). \(\square\)

**Levels.** For an arrangement \(\mathcal L\) of \(n\) non-vertical lines, no two parallel and no three concurrent, let \(\Lambda_k\) be the closure of the set of points on the lines with exactly \(k\) lines strictly below them, a polygonal chain. Its vertices are the vertices of the arrangement of level \(k-1\) or \(k\): at a vertex of level \(j\) the lines in positions \(j+1\) and \(j+2\) exchange, and the chain turns there exactly when \(k\in\{j,j+1\}\). The levels of the vertices are preserved by the perturbation of Corollary 1.2, which makes the arrangement general. So the number of vertices and edges of \(\Lambda_k\) is at most \(2(|V_{k-1}|+|V_k|)+1\), which is \(O(n(k+1)^{1/3-\varepsilon_0})\) for \(1\le k\le n/2\).

## 5. Exercises

**5.1** (easy). Show that for \(n\) points in convex position there are exactly \(n\) \(k\)-sets for each \(1\le k\le n-1\), and that \(S_k(Q)+S_{n-k}(Q)+2\ge n\) for them.

**5.2** (medium). In Lemma 2.2 with \(\gamma=0\), show directly that the expected number of cells is at most \(np+1\).

**5.3** (medium). Why does Proposition 3.1 need Corollary 1.2 for all levels \(j\), and not only for the middle level?

## 6. Solutions

**5.1.** A line meets the boundary of the convex polygon in at most two points, so a \(k\)-set is a set of \(k\) consecutive vertices, and each of the \(n\) arcs of \(k\) consecutive vertices is cut off by a line. The \(n\) sets are each a marked set of one of the two sweeps, or a set of leftmost or rightmost points, so the inequality holds.

**5.2.** The number of cells is at most \(|R|+1\), and \(\mathbb E|R|=np\).

**5.3.** In a cell, the level of a vertex of level \(k\) of \(H\) is \(k\) in the arrangement \(K(\Delta)\), which has \(|K(\Delta)|\) lines, typically about \(k\); this is not the middle level of \(K(\Delta)\), nor any fixed fraction of it. A bound for one rank only would not apply.

## References

- [AACS] P. K. Agarwal, B. Aronov, T. M. Chan and M. Sharir, *On levels in arrangements of lines, segments, planes, and triangles*, Discrete & Computational Geometry 19 (1998), 315–331; Lemma 3.2 and the proof of Theorem 3.1. https://tmc.web.engr.illinois.edu/kset.pdf
- [OpenAI-HL] OpenAI, *A power saving for planar halving lines*, OpenAI Math Release preprint, 25 September 2026, Section 8. https://github.com/openai/math/tree/main/preprints/A-power-saving-for-planar-halving-lines-September-25-2026
