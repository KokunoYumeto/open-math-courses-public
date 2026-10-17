# The linear bound

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson proves the cycle decomposition theorem of [Paths, cycles and Lovász's decomposition theorem](paths-cycles-and-lovasz-decompositions.md): every graph with \(n\) vertices has a cycle-and-edge partition with at most \(Cn\) members. The graph is split at the scales \(D_j=n^{0.95^j}\) by [Splitting a graph at a scale](splitting-a-graph-at-a-scale.md). Processing the expanding pieces of every scale separately would cost a fixed multiple of \(n\) at each of the many scales. Instead, one layer of pieces is chosen whose total order pays for a whole prefix of scales. Its pieces serve as routers for [folding pairs and lifting cycles](folding-pairs-and-lifting-cycles.md), which saves a fixed fraction of their order, and the graphs left over by [closing paths through reservoirs](closing-paths-through-reservoirs.md) are small. An induction with a slightly sublinear potential absorbs the remaining overhead.

All logarithms are to base two. A *member* is a cycle or a single edge, as in a cycle-and-edge partition.

## 1. Parameters and the choice of a prefix

Fix
\[
\begin{gathered}
\theta=0.95,\quad K=200,\\
P_0=4(K+1),\quad\eta=\frac1{100P_0}.
\end{gathered}
\]
Since \(200\ln0.95<-10\), we have \(\theta^K\le e^{-10}\), hence
\[
1.02\,\theta^K<0.001,\qquad\theta^{K+1}<0.001 .
\]

**Lemma 1.1** (choice of a prefix). Let \((S_j)_{j\ge0}\) be a sequence of nonnegative numbers, only finitely many of them nonzero, and not all zero. There is an index \(i\) with \(S_i>0\) and
\[
\sum_{j=0}^{i+K}S_j\le P_0S_i .
\]

*Proof.* Start at the first positive term \(i\); then \(\sum_{j\le i}S_j=S_i\le2(K+1)S_i\). Maintain the invariant \(\sum_{j\le i}S_j\le2(K+1)S_i\). If the conclusion fails at \(i\), the \(K\) terms \(S_{i+1},\dots,S_{i+K}\) add up to more than \(4(K+1)S_i-2(K+1)S_i\), so their largest value \(M\) satisfies \(M>2S_i\). Move to an index \(i'\) in this window with \(S_{i'}=M\). Then
\[
\begin{aligned}
\sum_{j\le i'}S_j&\le2(K+1)S_i+KM\\
&<(K+1)M+KM\\
&\le2(K+1)S_{i'} ,
\end{aligned}
\]
so the invariant persists. Each move increases the index and lands on a positive term; there are finitely many positive terms, so the moves stop, and then the conclusion holds. \(\square\)

## 2. A potential slightly below one

Put \(\phi(1)=\frac12\) and, for real \(x>1\),
\[
\phi(x)=\max\Bigl\{\tfrac12,\,1-\frac1{\sqrt{\log x}}\Bigr\}.
\]
The function \(\phi\) is nondecreasing and \(\frac12\le\phi\le1\).

**Proposition 2.1.** There is an absolute constant \(C\) such that every graph with \(n\ge1\) vertices has a cycle-and-edge partition with at most \(C\phi(n)n\) members.

The proof occupies Sections 3 to 6. It is a strong induction on \(n\). An absolute *cutoff* \(D_*>2\) is fixed first, large enough for the requirements collected in Section 6; then \(C\) is chosen. Every auxiliary constant introduced before that choice is independent of \(C\).

## 3. Small graphs and the prospective layers

*Small graphs.* A graph without edges has the empty partition. If \(1\le n<D_*\), taking every edge singly gives at most \(n(n-1)/2<D_*n/2\) members, which is at most \(C\phi(n)n\) when \(C\ge D_*\), because \(\phi\ge\frac12\).

Let \(n\ge D_*\) and assume Proposition 2.1 for all smaller positive orders. Put
\[
\begin{gathered}
D_j=n^{\theta^j},\\
m=\min\{j\ge0:D_j<D_*\} .
\end{gathered}
\]
Since \(D_j\) decreases to \(1<D_*\) and \(D_0=n\ge D_*\), the index \(m\) is finite and positive, and \(D_0,\dots,D_{m-1}\) are at least \(D_*\).

*Prospective layers.* Apply both operations of Lemma 2.1 of [Splitting a graph at a scale](splitting-a-graph-at-a-scale.md) at the scales \(D_0,D_1,\dots,D_{m-1}\) in turn: at stage \(0\) to \(G\), and at stage \(j\ge1\) to the residual graph of every box of level \(j-1\), on that box's vertex set. The inputs of stage \(j\) have average degree at most \(D_j\): for \(G\) because its average degree is at most \(n-1<D_0\), and for a residual because its average degree is at most \(D_{j-1}^{0.95}=D_j\). Let \(\mathcal Y_j\) be the indexed family of boxes of level \(j\) and \(\mathcal R_j\) the family of pieces extracted from them. Every box has a unique parent, whose vertex set contains its own, and the descendants of a box cover its vertex set (Remark 2.2 there). Only a prefix of these stages is kept in the end. At the end of every prefix, the long cycles removed so far, the pieces extracted so far and the residuals of the last level partition \(E(G)\).

Put \(N_{-1}=n\) and, for \(0\le j<m\),
\[
N_j=\sum_{Y\in\mathcal Y_j}|Y|,\qquad S_j=\sum_{R\in\mathcal R_j}|V(R)| ;
\]
set \(S_j=0\) for \(j\ge m\). Let \(C_2=80\). For \(0\le j<m\), since \(\log D_l=\theta^{l-j}\log D_j\),
\[
\sum_{l=0}^j\frac1{\log D_l}=\frac1{\log D_j}\sum_{u=0}^j\theta^u\le\frac{20}{\log D_j} .
\]
Every stage multiplies the total order of the boxes by at most \(1+2/\log D_l\). If \(\log D_*\ge C_2\), then \(x=40/\log D_j\le\frac12\), and \(e^x\le1+2x\) on \([0,\frac12]\) gives
\[
\begin{aligned}
n\le N_j&\le n\prod_{l=0}^j\Bigl(1+\frac2{\log D_l}\Bigr)\\
&\le n\Bigl(1+\frac{C_2}{\log D_j}\Bigr)\le2n .
\end{aligned}
\]
The lower bound holds because the boxes of each level cover \(V(G)\). The same computation, applied to the stages after level \(i\), shows that the boxes of level \(j\) descending from one box of level \(i<j\) and order \(y\) have total order at most \((1+C_2/\log D_j)y\).

Let \(\mathcal L_j\) be the family of long cycles removed at the stages \(0,\dots,j\). If \(D^{-0.01}\le1/\log D\) for all \(D\ge D_*\), then
\[
\begin{aligned}
|\mathcal L_j|&\le\sum_{l=0}^j\frac{N_{l-1}}{2D_l^{0.01}}\le n\sum_{l=0}^j\frac1{\log D_l}\\
&\le\frac{20n}{\log D_j}.
\end{aligned}
\]
Pieces in one box are vertex-disjoint, so \(S_j\le N_j\le2n\).

## 4. The terminal cases

*No pieces.* If every \(S_j\) is zero, keep all stages. Take the long cycles as members and every other edge singly. The remaining edges lie in residuals of level \(m-1\), of average degree at most \(D_m<D_*\); there are at most \(N_{m-1}D_m/2<D_*n\) of them. With the bound on \(|\mathcal L_{m-1}|\), at most \((20+D_*)n\) members are used.

*A prefix reaching the end.* Otherwise choose \(i\) by Lemma 1.1. If \(i+K\ge m-1\), keep all stages again, take the long cycles as members and every edge of the last residuals singly, at most \((20+D_*)n\) members. Since \(S_j=0\) for \(j\ge m\),
\[
\sum_{j=0}^{m-1}S_j\le P_0S_i .
\]
Apply the small residue lemma (Lemma 1.1 of [Closing paths through reservoirs](closing-paths-through-reservoirs.md), with \(c=1\) and the fixed \(\eta\)) to every piece at its own scale; a piece of level \(j\) has cut expansion at least \(D_j^{0.90}\) and order between \(D_j^{0.90}\) and \(D_j^{1.02}\). This gives at most \(9P_0S_i\le18P_0n\) members and residual graphs of total order at most
\[
\eta P_0S_i=\frac{S_i}{100}\le\frac n{50} .
\]
Each residual graph has order less than the order of its piece, which is at most \(n\). By the induction hypothesis and \(\phi\le1\), the residual graphs need at most \(Cn/50\le Cn/4\) members together.

In both terminal cases the number of members is at most
\[
T(D_*)n+\frac{Cn}4,
\]
where \(T(D_*)=20+D_*+18P_0\); this is at most \(Cn/2\le C\phi(n)n\) when \(C\ge4T(D_*)\).

## 5. A prefix with a gap of scales

Let \(i+K<m-1\). Keep the stages \(0,\dots,t\), where \(t=i+K\), and discard the later ones. Put
\[
\begin{gathered}
D=D_i,\qquad w=\log D,\\
H=C_2\theta^{-K},\\
a=D^{0.01},\quad L_0=D^{0.03},\\
B_0=D^{0.30},\quad\sigma=D^{0.90}.
\end{gathered}
\]
Since \(\log D_t=\theta^Kw\), Section 3 gives
\[
N_t\le\Bigl(1+\frac Hw\Bigr)n,\qquad|\mathcal L_t|\le\frac{Hn}w ,
\]
the second because \(C_2\ge20\).

**5.1. Batches.** Fix a box \(Y\) of level \(i\), of order \(y\le D^{1.02}\). Its descendants of level \(t\) have order at most \(D_t^{1.02}=D^{1.02\theta^K}<D^{0.001}\), and their residuals have average degree at most \(D_{t+1}=D^{\theta^{K+1}}\). Let \(T_Y\) be the total order of these descendants; then
\[
y\le T_Y\le\Bigl(1+\frac Hw\Bigr)y\le2y ,
\]
since \(H/w=C_2/\log D_t\le1\). Let \(F(Y)\) be the graph on \(Y\) formed by the residual edges of all these descendants. Their edge sets are disjoint, so \(F(Y)\) is simple, and
\[
2|E(F(Y))|\le T_YD^{\theta^{K+1}}\le2yD^{\theta^{K+1}} .
\]
Group the descendants into *batches* whose orders add up to at most \(B_0\): fill a batch until the next descendant would exceed \(B_0\), then start a new one. If \(D^{0.001}\le B_0/2\), every batch except possibly the last has order sum greater than \(B_0/2\), so there are at most \(1+2T_Y/B_0\le1+4y/B_0\) batches. For a batch, let \(W\) be the union of the vertex sets of its descendants and \(J_W\) the graph on \(W\) of their residual edges; the batch index is kept, so different batches are different even if their sets \(W\) coincide. Then the graphs \(J_W\) partition \(E(F(Y))\), the sets \(W\) cover \(Y\), and
\[
\begin{gathered}
|W|\le B_0,\qquad\sum_W|W|\le T_Y,\\
\sum_{Y\in\mathcal Y_i}\sum_W|W|\le N_t .
\end{gathered}
\]
Every box of level \(t\) has a unique ancestor of level \(i\), so at the end of the kept prefix
\[
\begin{aligned}
E(G)={}&\bigcup_{L\in\mathcal L_t}E(L)\\
&\cup\bigcup_{j\le t}\bigcup_{R\in\mathcal R_j}E(R)\\
&\cup\bigcup_{Y,W}E(J_W),
\end{aligned}
\]
a disjoint union.

**5.2. Active sets.** Call a vertex of \(Y\) *good* if its degree in \(F(Y)\) is at most \(a\). At most
\[
\begin{aligned}
\frac{2|E(F(Y))|}a&\le2yD^{\theta^{K+1}-0.01}\\
&\le2yD^{-0.009}\le\frac yw
\end{aligned}
\]
vertices of \(Y\) are not good, the last inequality being a requirement on the cutoff. For every batch \(W\) and every piece \(R\in\mathcal R_i\) inside \(Y\), consider the good vertices of \(W\cap V(R)\). If there are at least \(L_0\) of them, they form the *active set* \(X_{W,R}\); otherwise the set is *skipped*. Active sets of one batch are disjoint. There are at most \(y/\sigma\) pieces in \(Y\), so the skipped sets of \(Y\), counted with their batches, have total size at most
\[
\begin{aligned}
&L_0\Bigl(1+\frac{4y}{B_0}\Bigr)\frac y\sigma\\
&\quad\le y\bigl(D^{-0.87}+4D^{-0.15}\bigr)\le\frac yw ,
\end{aligned}
\]
using \(y\le D^{1.02}\) and again a requirement on the cutoff.

Let \(s(Y)\) be the total order of the pieces of level \(i\) in \(Y\), let \(\Sigma_Y\) be the total size of the active sets of \(Y\), and \(\Sigma=\sum_{Y\in\mathcal Y_i}\Sigma_Y\). Every good piece vertex lies in some batch; choose one such occurrence for each. At most \(y/w\) piece vertices are not good, and at most \(y/w\) chosen occurrences lie in skipped sets, so \(\Sigma_Y\ge s(Y)-2y/w\). Conversely, a vertex of \(Y\) lying in \(u(v)\ge1\) batches is counted at most \(u(v)\) times, and \(\sum_v(u(v)-1)=\sum_W|W|-y\); since the pieces are vertex-disjoint, \(\Sigma_Y\le s(Y)+\sum_W|W|-y\). Summing over \(Y\), with \(n\le N_i\le2n\),
\[
\begin{aligned}
S_i-\frac{4n}w\le\Sigma&\le S_i+N_t-N_i\\
&\le S_i+\frac{Hn}w .
\end{aligned}
\]

**5.3. Resolving the batches and the pieces.** Split the edges of every piece of level \(i\) into two spanning graphs \(P_R\) and \(T_R\), each of cut expansion at least \(\sigma/4\), by Lemma 2.1 of [Random sampling in expanding graphs](random-sampling-in-expanding-graphs.md) with two classes. In every box \(Y\) of level \(i\), the hypotheses of the batch resolution lemma (Lemma 2.1 of [Folding pairs and lifting cycles](folding-pairs-and-lifting-cycles.md)) hold: the batches have order at most \(B_0\) and disjoint edge sets with union \(F(Y)\); the pieces have orders between \(\sigma\) and \(D^{1.02}\), disjoint vertex sets inside \(Y\) and edges outside \(F(Y)\); and the active sets have at least \(L_0\) vertices, each of degree at most \(a\) in the whole of \(F(Y)\). The lemma gives simple quotients \(Q_W\) with
\[
\begin{aligned}
q_W&=|W|-\sum_R\Bigl\lfloor\frac{|X_{W,R}|}2\Bigr\rfloor\\
&\le|W|-\frac13\sum_R|X_{W,R}| .
\end{aligned}
\]
Every batch has positive order and every pair leaves a vertex, so \(1\le q_W\le B_0\le n^{0.30}<n\). Apply the induction hypothesis to every quotient, and lift all the resulting partitions by the lemma: in each \(Y\) this costs at most \(8\Sigma_Y\) members beyond the quotient members, and the remaining graph of every piece \(R\) of level \(i\) contains \(T_R\).

Then apply the small residue lemma with the fixed \(\eta\): with \(c=1/4\) to the remaining graph of every piece of level \(i\), and with \(c=1\) to every other piece of the kept prefix, at its own scale. These applications give at most \(9P_0S_i\) members, and their family \(\mathcal H\) of residual graphs satisfies
\[
\sum_{H'\in\mathcal H}|V(H')|\le\eta\sum_{j=0}^tS_j\le\eta P_0S_i .
\]
Each member of \(\mathcal H\) has order less than its piece, hence less than \(n\), and the induction hypothesis applies to it.

Every edge of \(G\) is accounted for once: the long cycles are members; the batch lemma partitions the batch edges together with the router edges it uses, each router edge coming from one piece of level \(i\) and used once; the small residue lemma, applied after those edges were removed, partitions all remaining piece edges into members and the graphs of \(\mathcal H\); and boxes with overlapping vertex sets have disjoint edge sets. Recursive partitions of the graphs of \(\mathcal H\) complete a cycle-and-edge partition of \(G\).

**5.4. The final estimate.** Put
\[
\begin{gathered}
A_1=H+\frac43,\\
A_2=\max\{9P_0+8,\;9H\}.
\end{gathered}
\]
By Sections 5.1 to 5.3,
\[
\sum_{Y,W}q_W\le N_t-\frac\Sigma3\le n-\frac{S_i}3+\frac{A_1n}w .
\]
The members not produced by the recursive calls number at most
\[
\begin{aligned}
&|\mathcal L_t|+8\Sigma+9P_0S_i\\
&\quad\le(9P_0+8)S_i+\frac{9Hn}w\\
&\quad\le A_2\Bigl(S_i+\frac nw\Bigr).
\end{aligned}
\]
Since \(\phi\) is nondecreasing and \(q_W\le B_0\), the induction hypothesis bounds the members of the quotient partitions by \(C\phi(B_0)\sum q_W\), and those of the partitions of \(\mathcal H\) by \(C\eta P_0S_i\). So the partition has at most
\[
\begin{aligned}
&A_2\Bigl(S_i+\frac nw\Bigr)+C\eta P_0S_i\\
&\quad+C\phi(B_0)\Bigl(n-\frac{S_i}3+\frac{A_1n}w\Bigr)
\end{aligned}
\]
members. As \(\eta P_0=\frac1{100}\) and \(\phi\ge\frac12\), the coefficient of \(S_i\) is at most
\[
A_2+\frac C{100}-\frac C6=A_2-\frac{47C}{300},
\]
which is at most zero if \(C\ge7A_2\).
Then, as \(A_2\le C\) and \(\phi\le1\), the number of members is at most
\[
C\phi(B_0)n+\frac{C(A_1+1)n}w .
\]
Put \(\delta=1/\sqrt{0.30}-1>0\). If \(w\ge40/3\), then \(\log B_0=0.30w\ge4\) and \(\log n\ge w\), so both \(\phi(B_0)\) and \(\phi(n)\) are given by the second expression in the definition, and
\[
\begin{aligned}
\phi(n)-\phi(B_0)&=\frac1{\sqrt{0.30w}}-\frac1{\sqrt{\log n}}\\
&\ge\frac\delta{\sqrt w} .
\end{aligned}
\]
If moreover \(w\ge((A_1+1)/\delta)^2\), then \((A_1+1)/w\le\delta/\sqrt w\), and the partition has at most \(C\phi(n)n\) members. The total quotient order need not be at most \(n\); the gain in the potential pays for its excess.

## 6. The order of the constants

The parameters \(\theta,K,P_0,\eta\) are fixed, and so are \(C_2=80\), \(H=C_2\theta^{-K}\), \(A_1\), \(A_2\) and \(\delta\). Choose the cutoff \(D_*>2\) so large that:

- Lemma 2.1 of [Splitting a graph at a scale](splitting-a-graph-at-a-scale.md) holds for all \(D\ge D_*\);
- the batch resolution lemma holds for all \(D\ge D_*\);
- the edge splitting lemma holds with two classes and \(c=1\), and the small residue lemma holds with the fixed \(\eta\) and with \(c=1\) and \(c=1/4\), for all \(D\ge D_*\);
- \(\log D_*\ge C_2\), \(\log D_*\ge40/3\) and \(\log D_*\ge((A_1+1)/\delta)^2\);
- for every \(D\ge D_*\):
\[
\begin{gathered}
D^{-0.01}\le\frac1{\log D},\\
D^{0.001}\le\frac{D^{0.30}}2,\\
2D^{-0.009}\le\frac1{\log D},\\
D^{-0.87}+4D^{-0.15}\le\frac1{\log D}.
\end{gathered}
\]

Each of these holds for all sufficiently large \(D\), and none depends on \(C\). Then choose
\[
C\ge\max\{7A_2,\;4T(D_*)\},
\]
which also gives \(C\ge D_*\). With these choices the small graphs, the terminal cases and the case of a gap of scales all satisfy the bound \(C\phi(n)n\), which completes the strong induction and proves Proposition 2.1. \(\square\)

## 7. The theorem and two consequences

**Theorem 7.1** (the Erdős–Gallai cycle decomposition theorem [OpenAI-EG]). There is an absolute constant \(C\) such that the edges of every graph with \(n\) vertices can be partitioned into at most \(Cn\) cycles and single edges.

*Proof.* For \(n\ge1\) this is Proposition 2.1, since \(\phi\le1\). The graph without vertices has the empty partition. \(\square\)

A graph is *Eulerian* if all its degrees are even; connectivity is not required. A partition of an Eulerian graph into cycles needs at least \(\Delta(G)/2\) cycles, where \(\Delta(G)\) is the largest degree, because a cycle contains at most two edges at a vertex.

The second assertion below uses a named statement, which this course does not prove. For disjoint vertex sets \(A,B\), \(e_G(A,B)\) is the number of edges joining them.

**(GGKO)** [GGKO, Proposition 6.3]. Suppose there is a constant \(c\) such that every graph with \(N\) vertices, for every \(N\), has a cycle-and-edge partition with at most \(cN\) members. Then for all \(\delta,p>0\) there are \(\varepsilon>0\) and \(n_0\) such that every Eulerian graph \(G\) on \(n\ge n_0\) vertices in which every partition \(V(G)=A\cup B\) with \(|A|,|B|\ge\varepsilon n\) satisfies \(e_G(A,B)\ge p|A||B|\) can be partitioned into at most \(\Delta(G)/2+\delta n\) cycles.

Its proof uses the regularity and absorption methods of [GGKO]; in their terms, the condition on partitions says that \(G\) is weakly \((\varepsilon,p)\)-quasirandom.

**Corollary 7.2.** Let \(C\) be the constant of Theorem 7.1.

1. Every Eulerian graph with \(n\) vertices can be partitioned into at most \(Cn\) cycles.
2. Assuming (GGKO): for all \(\delta,p>0\) there are \(\varepsilon>0\) and \(n_0\) such that every Eulerian graph \(G\) on \(n\ge n_0\) vertices satisfying the partition condition of (GGKO) can be partitioned into at most \(\Delta(G)/2+\delta n\) cycles.

*Proof.* (1) Take a partition from Theorem 7.1 with \(r\) cycles and \(s\) single edges, \(r+s\le Cn\). Deleting the edges of a cycle keeps all degrees even (Lemma 4.2 of [Paths, cycles and Lovász's decomposition theorem](paths-cycles-and-lovasz-decompositions.md)), so the graph formed by the \(s\) single edges is Eulerian, and by Lemma 4.1 there it is partitioned into cycles. Each has at least three edges, so there are at most \(s/3\) of them, and \(r+s/3\le Cn\) cycles partition \(G\).

(2) Theorem 7.1 supplies the hypothesis of (GGKO) with \(c=C\). \(\square\)

So the bound \(\Delta(G)/2\) for Eulerian graphs is attained up to an arbitrarily small linear error under the partition condition of (GGKO).

## 8. Exercises

**8.1** (easy). Check that \(\theta^K\le e^{-10}\) and that \(1.02\theta^K<0.001\) and \(\theta^{K+1}<0.001\).

**8.2** (easy). Show that \(e^x\le1+2x\) for \(0\le x\le\frac12\).

**8.3** (medium). Show, conversely to Corollary 7.2(1), that if every Eulerian graph with \(n\) vertices has a partition into at most \(c'n\) cycles, then every graph with \(n\) vertices has a cycle-and-edge partition with at most \((c'+1)n\) members.

**8.4** (medium). Explain why the induction is run with \(C\phi(n)n\) rather than \(Cn\): which term of Section 5.4 could not be absorbed otherwise?

**8.5** (medium). Show that the proof of Lemma 1.1 gives the same conclusion with \(P_0\) replaced by \(2\lambda(K+1)\), for every real \(\lambda\ge2\). (Use the invariant \(\sum_{j\le i}S_j\le\lambda(K+1)S_i\).)

## 9. Solutions

**8.1.** \(\ln0.95<-0.0512\), so \(200\ln0.95<-10.24\) and \(\theta^K<e^{-10.24}<4\cdot10^{-5}\). Then \(1.02\theta^K<0.001\), and \(\theta^{K+1}<\theta^K<0.001\).

**8.2.** The function \(e^x-1-2x\) is convex, vanishes at \(0\), and at \(\frac12\) equals \(e^{1/2}-2<0\); so it is at most zero on \([0,\frac12]\).

**8.3.** Take a maximal family of edge-disjoint cycles in \(G\). The remaining edges form a forest, with at most \(n-1\) edges, and the union of the cycles is an Eulerian graph, which by assumption is partitioned into at most \(c'n\) cycles. Together with the forest edges taken singly this gives at most \((c'+1)n\) members.

**8.4.** The term \(C(A_1+1)n/w\) comes from the overlap of the boxes and the long cycles; it is of order \(Cn/\log D\). It contains the factor \(C\), so a larger \(C\) does not help. The potential gains \(C\delta n/\sqrt w\) between the order \(n\) and the order of the quotients, which is larger than \(C(A_1+1)n/w\) for large \(w\).

**8.5.** The invariant holds at the first positive term. If the conclusion fails at \(i\), the \(K\) window terms add up to more than \(2\lambda(K+1)S_i-\lambda(K+1)S_i\), so their largest value \(M\) satisfies \(M>\lambda(K+1)S_i/K>\lambda S_i\). At the index \(i'\) of that value,
\[
\begin{aligned}
\sum_{j\le i'}S_j&\le\lambda(K+1)S_i+KM\\
&<(K+1)M+KM ,
\end{aligned}
\]
and \((2K+1)M\le\lambda(K+1)M\) because \(\lambda\ge2\). So the invariant persists, and the moves stop as in the proof of Lemma 1.1. The proof of Proposition 2.1 needs only that \(\eta P_0\) is a small fixed number, so any such \(P_0\) works with \(\eta=1/(100P_0)\).

## References

- [OpenAI-EG] OpenAI, *A linear cycle-and-edge decomposition of every graph*, OpenAI Math Release preprint, 24 September 2026. https://github.com/openai/math/tree/main/preprints/A-linear-cycle-and-edge-decomposition-of-every-graph-September-24-2026
- [GGKO] A. Girão, B. Granet, D. Kühn and D. Osthus, *Path and cycle decompositions of dense graphs*, Journal of the London Mathematical Society 104 (2021), 1085–1134; arXiv:1911.05501. https://arxiv.org/abs/1911.05501
- [BM] M. Bucić and R. Montgomery, *Towards the Erdős–Gallai cycle decomposition conjecture*, Advances in Mathematics 437 (2024), 109434; arXiv:2211.07689. https://arxiv.org/abs/2211.07689
