# Chains, crossings and Dey's bound

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson proves the classical estimate behind the exponent \(4/3\): in a rank sweep of \(N\) points, a family of step-disjoint intervals in each of which at least \(b\) points change membership has \(O((N/b)^{4/3})\) members. With \(b=1\) it gives Dey's bound \(S_k(P)=O(N^{4/3})\). The argument follows Dey's mechanism of convex chains and crossings, in the form used by OpenAI [OpenAI-HL, Section 2]: intervals with much activity are converted into batches of exchanges, the exchanges form a straight-line graph whose crossings are few because its edges lie on few convex and few concave chains, and a crossing inequality turns few crossings into few edges. The crossing inequality is proved with a designated set of endpoints, a version needed again in [Limiting measures](limiting-measures.md).

Throughout, \(P\) is a generic configuration of \(N\) points, \(k\) is a rank with \(0\le k\le N\), and \(s_0<s_1<\dots<s_L\) are the states of [Halving lines and rank sweeps](halving-lines-and-rank-sweeps.md), with marked sets \(M(s)=M_k(s)\).

## 1. Activity and endpoint distance

An *interval* is a set of consecutive states \(s_{t_1},\dots,s_{t_2}\), \(t_1\le t_2\); its *steps* are \(t_1+1,\dots,t_2\). Two intervals are *step-disjoint* if no step belongs to both. The *activity* of an interval is the number of distinct points whose membership in \(M_k\) changes at one of its steps. For two sets \(M,M'\) of \(k\) points put
\[
\begin{aligned}
d(M,M')&=|M\setminus M'|=|M'\setminus M|\\
&=\tfrac12|M\triangle M'| .
\end{aligned}
\]
This is a metric on the \(k\)-subsets of \(P\), and since a step removes at most one point and adds at most one, it changes the distance of the marked set from a fixed set by at most one. An interval of positive activity contains a switch, so by Lemma 2.1(c) of [Halving lines and rank sweeps](halving-lines-and-rank-sweeps.md) its two endpoint sets have different sums of first coordinates and differ.

Activity counts every point that changes, including points that leave and return; the endpoint distance only sees the net change. The next lemma recovers net change from activity at the price of changing the rank.

**Lemma 1.1** (activity and endpoint distance). Let \(b\ge4\) and \(c=\lfloor b/4\rfloor\). Every family of intervals of activity at least \(b\) splits into two subfamilies \(\mathcal F_+\) and \(\mathcal F_-\) with the following properties. If \(\mathcal F_+\neq\varnothing\), then \(k+c\le N\) and every interval of \(\mathcal F_+\) has endpoint distance at least \(c\) in the rank-\((k+c)\) sweep. If \(\mathcal F_-\neq\varnothing\), then \(k-c\ge0\) and every interval of \(\mathcal F_-\) has endpoint distance at least \(c\) in the rank-\((k-c)\) sweep. For \(1\le b\le3\), every interval of activity at least \(b\) has endpoint distance at least \(1\) in the rank-\(k\) sweep.

*Proof.* The case \(b\le3\) was shown before the lemma. Let \(b\ge4\). Put an interval into \(\mathcal F_+\) if at least \(b/2\) of its active points are unmarked at its first state, and into \(\mathcal F_-\) otherwise.

*The family \(\mathcal F_+\).* Let \(I\) have first state \(s'\) and last state \(s''\). At least \(\lceil b/2\rceil\ge c\) points are unmarked at \(s'\), so \(k+c\le N\). Let \(E=M_{k+c}(s')\); it consists of \(M_k(s')\) and \(c\) further points, so at most \(c\) of the initially unmarked active points lie in \(E\), and the set \(U\) of initially unmarked active points outside \(E\) has
\[
|U|\ge\lceil b/2\rceil-c\ge c .
\]
Take \(u\in U\). Being active and initially unmarked, \(u\) is marked at some state \(s^*\) of \(I\). There at most \(k-1\) points precede \(u\), so at least \((k+c)-(k-1)=c+1\) points of \(E\) follow \(u\) at \(s^*\). At \(s'\) every point of \(E\) precedes \(u\). For a point \(e\in E\) following \(u\) at \(s^*\), the difference \(\varphi_s(u)-\varphi_s(e)\) is affine in \(s\), positive at \(s'\) and negative at \(s^*\ge s'\); so it is negative at every \(s\ge s^*\), in particular at \(s''\). Let \(E'=M_{k+c}(s'')\). If at least \(c\) points of \(U\) lie in \(E'\), then \(|E'\setminus E|\ge c\). Otherwise some \(u\in U\) lies outside \(E'\); the \(c+1\) points of \(E\) that follow \(u\) at \(s''\) are then outside \(E'\) as well, and \(|E\setminus E'|\ge c+1\). In both cases \(d(E,E')\ge c\).

*The family \(\mathcal F_-\).* The point reflection \(\bar P=\{(-x,-y):(x,y)\in P\}\) is generic with the same segment slopes, so it has the same states, and \(\varphi_s(-x,-y)=-\varphi_s(x,y)\) reverses every order. Hence the rank-\((N-k)\) marked set of \(\bar P\) at \(s\) is the reflection of the complement of \(M_k(s)\). An interval of \(\mathcal F_-\) has more than \(b/2\) active points that are marked at its first state, that is, unmarked for \(\bar P\) at rank \(N-k\), with the same activity. The previous case applied to \(\bar P\) gives \(N-k+c\le N\) and endpoint distance at least \(c\) between complements of rank-\((k-c)\) sets of \(P\). Complements have the same distance. \(\square\)

## 2. Greedy batches

**Lemma 2.1** (greedy batches). Let \(d\ge1\) be an integer and \(a=\lceil d/2\rceil\). Put \(\tau_0=0\) and, as long as possible, let \(\tau_{j+1}\) be the least \(t>\tau_j\) with \(d(M(s_t),M(s_{\tau_j}))=a\). Let \(R\) be the number of indices \(\tau_1,\dots,\tau_R\) so obtained. Then every family of step-disjoint intervals of endpoint distance at least \(d\) has at most \(R\) members.

The interval from \(s_{\tau_{j-1}}\) to \(s_{\tau_j}\) is the \(j\)th *batch*; it has endpoint distance exactly \(a\).

*Proof.* Let \(I\) run from \(s_{t_1}\) to \(s_{t_2}\). Suppose no \(\tau_j\) satisfies \(t_1<\tau_j\le t_2\). Let \(\tau_i\) be the largest index with \(\tau_i\le t_1\). Every state \(s_t\) with \(\tau_i\le t<\tau_{i+1}\), or with \(t\ge\tau_i\) if \(i=R\), has \(d(M(s_t),M(s_{\tau_i}))\le a-1\), by the choice of \(\tau_{i+1}\) as the first state at distance \(a\) (distances change by at most one per step). This applies to \(s_{t_1}\) and \(s_{t_2}\), so their distance is at most \(2a-2<d\), a contradiction. So we may assign to \(I\) an index \(\tau_j\) with \(t_1<\tau_j\le t_2\). Then the step \(\tau_j\) belongs to \(I\), and step-disjoint intervals receive different indices. \(\square\)

## 3. Exchange graphs

In the \(j\)th batch let \(L_j=M(s_{\tau_{j-1}})\setminus M(s_{\tau_j})\) be the \(a\) points *lost* and \(G_j=M(s_{\tau_j})\setminus M(s_{\tau_{j-1}})\) the \(a\) points *gained*. Its *exchange edges* are the \(a^2\) segments \(uv\) with \(u\in L_j\), \(v\in G_j\).

**Lemma 3.1.** For \(u\in L_j\) and \(v\in G_j\), \(x_u<x_v\), and the slope of \(uv\) lies strictly between \(s_{\tau_{j-1}}\) and \(s_{\tau_j}\). Different batches have no exchange edge in common.

*Proof.* At \(s_{\tau_{j-1}}\), \(u\) is marked and \(v\) is not, so \(\varphi(u)<\varphi(v)\); at \(s_{\tau_j}\) the reverse holds. The affine function \(\varphi_s(v)-\varphi_s(u)=(y_v-y_u)-s(x_v-x_u)\) changes from positive to negative between the two states, so \(x_v>x_u\), and it vanishes at the slope of \(uv\), which lies in between. The open intervals \((s_{\tau_{j-1}},s_{\tau_j})\) of different batches are disjoint. \(\square\)

A *window* is a set of consecutive batches. Its exchange edges form a simple graph drawn with straight segments. No vertex lies in the interior of an edge, by (G1), and two edges with a common endpoint meet only there. Two edges *cross* if they meet at a point interior to both; by (G4) no third edge passes through such a point.

## 4. Two chain partitions

A *convex chain* is a polygonal path \(q_0q_1\cdots q_r\) with \(x(q_0)<\dots<x(q_r)\) whose segment slopes increase strictly; it is the graph of a convex piecewise affine function on \([x(q_0),x(q_r)]\). A *concave chain* is the same with decreasing slopes.

**Lemma 4.1** (two chain partitions). Let a window have \(S\) distinct endpoints of exchange edges. Its exchange edges can be partitioned into at most \(aS\) convex chains, and also into at most \(aS\) concave chains. The number of pairs of its exchange edges that cross is at most \(2a^2S^2\).

*Proof.* *Convex chains.* In each batch \(j\) of the window, label \(L_j=\{u_1,\dots,u_a\}\) and \(G_j=\{v_1,\dots,v_a\}\), and for \(c=1,\dots,a\) let \(\pi_{j,c}\) be the perfect matching \(u_i\mapsto v_{i+c}\), indices modulo \(a\). Every exchange edge of the batch belongs to exactly one of these matchings. Fix \(c\). Place a token on each point marked at the first state of the window, and in the \(j\)th batch move the token on each \(u\in L_j\) to \(\pi_{j,c}(u)\), leaving the other tokens in place. By induction over the batches, the tokens occupy exactly the marked points at the start of each batch, so the move is defined. Along the moves of one token the first coordinate increases and, by Lemma 3.1, the slopes increase from batch to batch. So the moves of a token that moves at least once form a convex chain. Each exchange edge \(uv\) of batch \(j\) lying in \(\pi_{j,c}\) is traversed by the token on \(u\) in the process for \(c\), and by no other. A token that moves starts at an endpoint of an exchange edge, so there are at most \(S\) such tokens for each \(c\), and at most \(aS\) chains in all.

*Concave chains.* Place tokens on the unmarked points instead, and move the token on each \(v\in G_j\) to \(\pi_{j,c}^{-1}(v)\). The tokens occupy the unmarked points at the start of each batch. They move to the left, and read from left to right the slopes of a trajectory decrease, since the batches are met in reverse order. This gives at most \(aS\) concave chains.

*Crossings.* Let \(\Gamma\) be a convex chain, the graph of a convex function \(g\), and \(\Lambda\) a concave chain, the graph of a concave function \(f\), and let \(J\) be the common interval of their domains. On \(J\), \(f-g\) is concave, so the set where \(f-g\ge0\) is an interval, and \(f-g\) changes sign at most twice. An edge of \(\Gamma\) and an edge of \(\Lambda\) that cross have different slopes, so \(f-g\) changes sign at the crossing; by (G4) different pairs of edges cross at different points. Hence at most two pairs consisting of an edge of \(\Gamma\) and an edge of \(\Lambda\) cross. Every crossing pair \(\{e,e'\}\) consists of an edge \(e\) of some convex chain and an edge \(e'\) of some concave chain. Summing over the at most \((aS)^2\) pairs of chains gives at most \(2a^2S^2\) crossing pairs. \(\square\)

## 5. Crossings with designated endpoints

**Lemma 5.1.** Let a simple graph with \(e\) edges be drawn with straight segments on \(v\) distinct points, with no vertex in the interior of an edge and no crossing between edges with a common endpoint. Suppose every edge has an endpoint in a set \(D\) of \(m\le v\) vertices, and let \(\operatorname{cr}\) be the number of crossing pairs of edges. Then
\[
e^3\le2304\,mv\operatorname{cr}+13824\,v^3 .
\]
In particular \(e^3\le2304\,mv\operatorname{cr}\) if \(e\ge24v\).

*Proof.* *A linear bound.* For any such drawing with \(v'\) vertices, \(e'\) edges and \(\operatorname{cr}'\) crossing pairs, \(e'\le3v'+\operatorname{cr}'\). Indeed, deleting one edge from each crossing pair leaves a straight-line drawing without crossings, so a planar graph, which has at most \(3v'-6\) edges if \(v'\ge3\) by Theorem 5.34 of the core course [Applied Combinatorics](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C70) [KT, Theorem 5.34], and at most \(1\) edge if \(v'\le2\).

*Sampling.* If \(e<24v\), then \(e^3<24^3v^3=13824v^3\). Let \(e\ge24v\), so \(m\ge1\). Put each vertex of \(D\) independently into a set \(D_1\) with probability \(1/2\). An edge with one endpoint in \(D\) joins \(D_1\) to its complement exactly when that endpoint is chosen; an edge with both endpoints in \(D\) does so exactly when one of them is chosen. Both events have probability \(1/2\), so for some choice at least \(e_0\ge e/2\) edges join \(D_1\) to its complement. Keep only these edges; they form a bipartite drawing between \(D_1\), with at most \(m\) vertices, and the rest, with at most \(v\). Put
\[
p=\frac{12v}{e_0},\qquad q=\frac{12m}{e_0},
\]
both at most \(1\) since \(e_0\ge12v\ge12m\). Keep each vertex of \(D_1\) with probability \(p\) and each other vertex with probability \(q\), independently, and keep the edges between kept vertices. An edge survives with probability \(pq\); a crossing pair has four distinct endpoints, two on each side, and survives with probability \(p^2q^2\). Taking expectations in the linear bound,
\[
pq\,e_0\le3(pm+qv)+p^2q^2\operatorname{cr}.
\]
Substituting,
\[
\frac{144\,mv}{e_0}\le\frac{72\,mv}{e_0}+\frac{20736\,m^2v^2\operatorname{cr}}{e_0^4},
\]
so \(e_0^3\le288\,mv\operatorname{cr}\), and \(e^3\le8e_0^3\le2304\,mv\operatorname{cr}\). \(\square\)

With \(D\) all vertices, Lemma 5.1 is the crossing inequality of Ajtai, Chvátal, Newborn and Szemerédi and of Leighton; the designated set follows the imbalanced crossing argument of Pach, Solymosi and Tardos. The proof above is self-contained.

## 6. The classical packing bound

**Theorem 6.1.** There is an absolute constant \(C_1\) with the following property. For every generic configuration of \(N\) points, every rank \(k\) and every integer \(1\le b\le N\), every family of step-disjoint intervals of activity at least \(b\) has at most \(C_1(N/b)^{4/3}\) members.

*Proof.* By Lemma 1.1 the family splits into at most two subfamilies, each consisting of step-disjoint intervals of endpoint distance at least \(d\) in the sweep of some rank \(k'\), where \(d=\lfloor b/4\rfloor\) if \(b\ge4\) and \(d=1\) if \(b\le3\). Step-disjointness does not depend on the rank. By Lemma 2.1, each subfamily has at most \(R\) members, the number of batches of the rank-\(k'\) sweep with \(a=\lceil d/2\rceil\).

All \(R\) batches form one window with \(Ra^2\) exchange edges on \(S\le N\) points and, by Lemma 4.1, at most \(2a^2N^2\) crossing pairs. Lemma 5.1 with \(D\) all vertices and \(m=v=S\le N\) gives
\[
\begin{aligned}
R^3a^6&\le4608\,a^2N^4+13824\,N^3,\\
R&\le17\Bigl(\frac Na\Bigr)^{4/3}+24\,\frac N{a^2}\\
&\le41\Bigl(\frac Na\Bigr)^{4/3},
\end{aligned}
\]
using \((x+y)^{1/3}\le x^{1/3}+y^{1/3}\) and \(N/a^2\le(N/a)^{4/3}\) for \(a,N\ge1\). For \(b\ge4\), \(\lfloor b/4\rfloor\ge b/8\), so \(a\ge b/16\); for \(b\le3\), \(a=1\ge b/3\). Hence each subfamily has at most \(41\cdot16^{4/3}(N/b)^{4/3}\) members, and \(C_1=82\cdot16^{4/3}\) works. \(\square\)

**Corollary 6.2** (Dey's bound). \(S_k(P)\le C_1N^{4/3}\) for every generic configuration of \(N\) points and every rank \(k\).

*Proof.* The switch steps, each as a one-step interval, are step-disjoint intervals of activity \(2\ge1\). \(\square\)

The proof of Theorem 6.1 also gives a bound for part of a window, which [Limiting measures](limiting-measures.md) uses.

**Corollary 6.3** (localized crossing bound). Let a window of batches with parameter \(a\) have \(S\) distinct endpoints, and let \(e_F\) of its exchange edges have their left endpoint in a set of \(m\) of these endpoints. Then
\[
e_F^3\le4608\,a^2mS^3+13824\,S^3 .
\]

*Proof.* Apply Lemma 5.1 to these edges, on the \(S\) endpoints, with \(D\) the given \(m\) points. By Lemma 4.1 they have at most \(2a^2S^2\) crossing pairs. \(\square\)

The constant \(C_1\) is the starting point of the course. The remaining lessons show that it can be replaced by an arbitrarily small constant when \(N/b\) is large, and the next lesson shows that this is enough for a power saving.

## 7. Exercises

**7.1** (easy). Show that \(d\) is a metric on the \(k\)-subsets of \(P\), and that \(d(M\cup\{v\}\setminus\{u\},M')\) differs from \(d(M,M')\) by at most one.

**7.2** (medium). Draw a convex chain and a concave chain that cross twice. Why can they not cross three times, even when they share a segment?

**7.3** (easy). Show that in a drawing with straight segments and no vertex in the interior of an edge, two edges with a common endpoint never cross. Where does the proof of Lemma 5.1 use that crossing pairs have four distinct endpoints?

**7.4** (medium). Show that for \(N\) points in convex position, \(S_k(P)\le N\) for every \(k\). Compare with Corollary 6.2.

## 8. Solutions

**7.1.** The inequality
\[
\begin{aligned}
\tfrac12|M\triangle M''|&\le\tfrac12|M\triangle M'|\\
&\quad+\tfrac12|M'\triangle M''|
\end{aligned}
\]
holds since \(M\triangle M''\subseteq(M\triangle M')\cup(M'\triangle M'')\); symmetry and \(d(M,M')=0\Leftrightarrow M=M'\) are clear. Removing \(u\) and adding \(v\) changes \(|M\setminus M'|\) by \(-1\), \(0\) or \(+1\) from each of the two changes, and since both sets keep size \(k\), the total change of \(|M\setminus M'|\) is at most one.

**7.2.** The graphs of \(x^2\) and \(2-x^2\) on \([-2,2]\), replaced by polygonal approximations with breakpoints at \(\pm1/2,\pm3/2\), cross near \(\pm1\). The difference of a concave and a convex function is concave, so its nonnegative set is an interval: it can become positive once and negative once. A shared segment is a set where the difference vanishes; it does not create further sign changes.

**7.3.** Let \(pv\) and \(pw\) meet at a point \(X\ne p\). The lines through \(p\) and \(X\) contain both segments, so \(p,v,w\) lie on one line. If \(v\) and \(w\) lie on the same side of \(p\), the nearer of them lies in the interior of the other segment, which is excluded; if they lie on opposite sides, the segments meet only at \(p\). So a crossing pair has four distinct endpoints. The proof of Lemma 5.1 uses this twice: a crossing pair survives the sampling only if all four endpoints are kept, which has probability \(p^2q^2\), and deleting one edge of each crossing pair leaves a drawing in which no two edges meet outside their common endpoints.

**7.4.** At each state the marked set is separated from the other points by a line of slope \(s\), and a line meets the boundary of the convex polygon in at most two points, so the marked set consists of \(k\) consecutive vertices. For \(1\le k\le N-1\) there are \(N\) such sets. By Lemma 2.1(c) of [Halving lines and rank sweeps](halving-lines-and-rank-sweeps.md) the sum of first coordinates of the marked set increases strictly at each switch, so the sweep visits each of these sets at most once and has at most \(N-1\) switches. This is far below \(N^{4/3}\): sets with many switches are not in convex position.

## References

- [KT] K. Keller and W. T. Trotter, *Applied Combinatorics*, open textbook, Section 5.5, Theorem 5.34; the text of the core course Applied Combinatorics. https://www.appliedcombinatorics.org/book/s_graphs_planar.html
- [OpenAI-HL] OpenAI, *A power saving for planar halving lines*, OpenAI Math Release preprint, 25 September 2026. https://github.com/openai/math/tree/main/preprints/A-power-saving-for-planar-halving-lines-September-25-2026
