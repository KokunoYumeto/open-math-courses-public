# The switch chain

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

How can one choose, uniformly at random, a simple graph on \(\{1,\dots,n\}\) in which vertex \(i\) has a prescribed degree \(d_i\)? A natural method is a random walk: start from any such graph and repeatedly perform a *switch*, which removes two disjoint edges and inserts another perfect matching on their four endpoints, when both new edges are absent. Switches preserve every degree. The question whether this walk mixes in polynomial time for every degree sequence goes back to Kannan, Tetali and Vempala, who studied it for bipartite graphs; in its present form it is the Kannan–Tetali–Vempala conjecture [EGMMSS, Conjecture 1.1]. Cooper, Dyer and Greenhill proved rapid mixing for regular graphs, later work covered growing classes of irregular sequences, including every P-stable class [EGMMSS], and Fu, Qin and Wang proved the bipartite case, that is, binary matrices with prescribed row and column sums, for all margins [FQW]. This course presents OpenAI's proof for simple graphs and every degree sequence [OpenAI-SW]:

**Theorem 5.4** (OpenAI 2026). For every \(n\ge4\) and every graphical degree vector \(d\), the switch chain \(P_d\) defined in Section 2 has mixing time \(t_{\mathrm{mix}}(d)\le2n^8\), and, if \(\Omega_d\) has more than one element, spectral gap at least \(\bigl[24n^2\binom n4\bigr]^{-1}\).

The proof compares the switch chain with a stronger move. For a pair of vertices \(a=\{i,j\}\), take the vertices adjacent to exactly one of \(i\) and \(j\), and redistribute them uniformly between \(i\) and \(j\), keeping the number that goes to each. For binary matrices such moves form the Curveball algorithm of Verhelst and of Strona, Nappo, Boccacci, Fattorini and San-Miguel-Ayanz; the version for undirected graphs is due to Carstens, Berger and Strona [CBS]. Let \(h_a\) subtract from a function its average over the graphs reachable by the move at \(a\), and let \(H=\sum_ah_a\). The central estimate is the operator inequality \(H^2\succeq H\) (Theorem 4.2). Its proof follows the squared-generator method of Caputo [Caputo]: in the expansion of \(H^2\), the products of intersecting pairs live on vertex triples and are treated in [A variance inequality for three rows](a-variance-inequality-for-three-rows.md); the products of disjoint pairs, where undirected graphs need a new estimate, are treated in [Disjoint pair resamplings](disjoint-pair-resamplings.md). This lesson defines the chain, proves that switches connect the graphs with degree vector \(d\) (Lemma 3.1), and shows that \(H^2\succeq H\) implies Theorem 5.4 (Proposition 5.3). [Exact uniform sampling](exact-uniform-sampling.md) turns the theorem into an exact sampler.

All function spaces are real, and \(\log\) is the natural logarithm.

## 1. Reversible chains and spectral gaps

Let \(\Omega\) be a finite set with the uniform probability measure \(\pi\), and give the functions on \(\Omega\) the inner product \(\langle f,g\rangle=\mathbb E_\pi[fg]\) and norm \(\|f\|\). A Markov kernel \(P\) on \(\Omega\) is *symmetric* if \(P(x,y)=P(y,x)\); then \(\pi\) is stationary, \((Pf)(x)=\sum_yP(x,y)f(y)\) is self-adjoint, and its eigenvalues lie in \([-1,1]\). For self-adjoint operators, \(A\succeq B\) means \(\langle f,(A-B)f\rangle\ge0\) for all \(f\). The *total variation distance* of probability measures is \(\|\mu-\nu\|_{\mathrm{TV}}=\frac12\sum_x|\mu(x)-\nu(x)|\).

**Lemma 1.1.** Let \(P\) be symmetric, and suppose that all eigenvalues of \(P\) on the functions with mean zero lie in \([0,1-\gamma]\), where \(0<\gamma\le1\). Then for every \(x\in\Omega\) and \(t\ge0\),
\[
\|P^t(x,\cdot)-\pi\|_{\mathrm{TV}}\le\tfrac12\sqrt{|\Omega|}\,\mathrm e^{-\gamma t}.
\]

**Proof.** Let \(u_t(y)=|\Omega|P^t(x,y)\), the density of \(P^t(x,\cdot)\) with respect to \(\pi\). By symmetry \(u_t=P^tu_0\), where \(u_0=|\Omega|\mathbf 1_{\{x\}}\), and \(u_0-1\) has mean zero and \(\|u_0-1\|^2=\mathbb E_\pi u_0^2-1=|\Omega|-1\). Hence \(\|u_t-1\|\le(1-\gamma)^t\sqrt{|\Omega|}\le\mathrm e^{-\gamma t}\sqrt{|\Omega|}\), and \(\|P^t(x,\cdot)-\pi\|_{\mathrm{TV}}=\frac12\mathbb E_\pi|u_t-1|\le\frac12\|u_t-1\|\) by the Cauchy–Schwarz inequality. \(\square\)

## 2. The switch chain

Let \(n\ge4\), \(V=\{1,\dots,n\}\), and let \(d=(d_1,\dots,d_n)\) be *graphical*: the set \(\Omega_d\) of simple graphs on \(V\) in which vertex \(i\) has degree \(d_i\) is nonempty. Let \(\pi_d\) be the uniform measure on \(\Omega_d\). A *switch* replaces two edges \(\{u,v\},\{x,y\}\) with four distinct endpoints by a different perfect matching of \(\{u,v,x,y\}\), say \(\{u,x\},\{v,y\}\), provided both new edges are absent. It preserves simplicity and all degrees, and its reverse is again a switch. Two graphs related by a switch are *switch neighbours*.

The chain \(P_d\) does the following. With probability \(\frac12\) it stays. Otherwise it chooses a four-element set \(S\subseteq V\) uniformly and one of the six ordered pairs \((F,F')\) of different perfect matchings of \(S\) uniformly; if both edges of \(F\) are present and both edges of \(F'\) are absent, it replaces \(F\) by \(F'\), and otherwise it stays. Let \(L\) be the *Laplacian of the switch graph*,
\[
(Lf)(G)=\sum_{G'\text{ switch neighbour of }G}\bigl(f(G)-f(G')\bigr).\tag{2.1}
\]

**Lemma 2.1.** For switch neighbours \(G\neq G'\), \(P_d(G,G')=\bigl[12\binom n4\bigr]^{-1}\), and \(P_d(G,G')=0\) for other \(G'\neq G\). Hence \(P_d\) is symmetric,
\[
I-P_d=\frac{L}{12\binom n4},\tag{2.2}
\]
and all eigenvalues of \(P_d\) lie in \([0,1]\).

**Proof.** A switch \(G\to G'\) determines its four-element set and the ordered pair of the removed and the inserted matching, so it is proposed with probability \(\frac12\cdot\binom n4^{-1}\cdot\frac16\). The diagonal entries make the rows sum to one, which gives (2.2). Write \(P_d=\frac12(I+Q)\), where \(Q\) is the symmetric Markov kernel of the proposal step with rejections; its eigenvalues lie in \([-1,1]\), so those of \(P_d\) lie in \([0,1]\). \(\square\)

## 3. Connectivity

The following argument is Havel's switching proof of the greedy criterion for graphical sequences [Havel], with a fixed tie-breaking rule so that every graph is led to the same target.

**Lemma 3.1.** Any two graphs in \(\Omega_d\) are joined by a sequence of switches. Moreover, the following greedy prescription produces a graph in \(\Omega_d\). Start with \(R=V\) and residual degrees \(r=d\). Let \(v\) be the first vertex of \(R\); join \(v\) to the \(r_v\) vertices of \(R\setminus\{v\}\) with the largest residual degrees, ties broken by label; lower the residual degree of each of them by one, remove \(v\) from \(R\), and repeat until \(R\) is empty.

**Proof.** We transform every \(G\in\Omega_d\) by switches into the graph of the prescription. Suppose a set of vertices has been *frozen*, every edge at a frozen vertex being in its prescribed state, and let \(R\) be the set of the other vertices; write \(d^R_w\) for the degree of \(w\) in the graph induced on \(R\). This is \(d_w\) minus the number of frozen vertices joined to \(w\), so it equals the residual degree of the prescription and does not depend on \(G\). Let \(v\) be the first vertex of \(R\), and call the \(d^R_v\) vertices of \(R\setminus\{v\}\) with the largest \(d^R\), ties broken by label, its *desired* neighbours. Suppose that the neighbours of \(v\) in \(R\) are not exactly the desired ones. Then some desired \(j\) is not a neighbour of \(v\) and some neighbour \(i\) is not desired, and \(d^R_j\ge d^R_i\) because \(j\) precedes \(i\) in the ranking. Let \(A=N_R(j)\setminus\{i\}\) and \(B=N_R(i)\setminus\{j\}\). Whether or not \(ij\) is an edge, \(|A|-|B|=d^R_j-d^R_i\ge0\). The vertex \(v\) lies in \(B\) but not in \(A\), so \(B\setminus A\neq\varnothing\), and therefore \(A\setminus B\neq\varnothing\). Pick \(k\in A\setminus B\). It is none of \(v,i,j\), it is adjacent to \(j\) and not to \(i\), while \(v\) is adjacent to \(i\) and not to \(j\). The switch \(\{vi,jk\}\to\{vj,ik\}\) involves only vertices of \(R\), leaves the other edges at \(v\) alone, and raises the number of desired neighbours of \(v\) by one. After finitely many such switches \(v\) has exactly its desired neighbours. (When \(|R|\le3\) no discrepancy can occur, since one would yield the four distinct vertices \(v,i,j,k\).) Then freeze \(v\): its edges agree with the prescription, and the residual degrees on \(R\setminus\{v\}\) are again independent of \(G\). Frozen edges never change, since all switches stay inside \(R\). When every vertex is frozen, every \(G\in\Omega_d\) has been transformed into one and the same graph, which is the graph of the prescription and lies in \(\Omega_d\). Following one transformation forwards and another backwards joins any two graphs. \(\square\)

## 4. Pair resamplings

Fix an unordered pair \(a=\{i,j\}\) of vertices. Two graphs lie in the same *\(a\)-fiber* if they have the same edges with no endpoint in \(a\), agree on the edge \(ij\), and give every \(w\notin a\) the same number of neighbours in \(a\). In an \(a\)-fiber, a vertex \(w\notin a\) with exactly one neighbour in \(a\) is a *singleton*.

**Lemma 4.1.** Let an \(a\)-fiber have \(N\) singletons. The number \(q\) of singletons adjacent to \(i\) is the same throughout the fiber, and the map sending a graph to the set of singletons adjacent to \(i\) is a bijection from the fiber onto the \(q\)-element subsets of the singletons.

**Proof.** The degree of \(i\) is the sum of \([ij\in G]\), the number of vertices with two neighbours in \(a\), and \(q\); the first two are constant on the fiber. Conversely, any \(q\)-subset gives a graph of the fiber: each singleton keeps one neighbour in \(a\), the degrees of \(i\) and \(j\) are \(d_i\) and \(d_j\), and nothing else changes. \(\square\)

Exchanging the assignments of two singletons \(k,l\) with different neighbours in \(a\) is a switch: if \(k\sim i\) and \(l\sim j\), it replaces \(\{ik,jl\}\) by \(\{il,jk\}\).

Let \(E_a\) be the conditional expectation with respect to the partition of \(\Omega_d\) into \(a\)-fibers, \(h_a=I-E_a\), and
\[
H=\sum_{a\in\binom V2}h_a.\tag{4.1}
\]
This is the heat-bath construction of Dyer, Greenhill and Ullrich [DGU] for these partitions. Each \(E_a\) and \(h_a\) is an orthogonal projection, so \(H\succeq0\), and \(H\) kills the constants.

**Theorem 4.2** (OpenAI). \(H^2\succeq H\).

The proof occupies [A variance inequality for three rows](a-variance-inequality-for-three-rows.md) and [Disjoint pair resamplings](disjoint-pair-resamplings.md) (Theorem 3.3 there).

## 5. From the operator inequality to mixing

**Lemma 5.1.** If \(H^2\succeq H\), then the kernel of \(H\) consists of the constants, and \(\operatorname{Var}_{\pi_d}(f)\le\langle f,Hf\rangle\) for every \(f\).

**Proof.** \(\langle f,Hf\rangle=\sum_a\|h_af\|^2\) vanishes only if \(f\) is constant on every pair fiber. A switch \(\{uv,xy\}\to\{ux,vy\}\) exchanges the two singletons \(v,x\) in a fiber of the pair \(\{u,y\}\): before the switch \(v\sim u\) and \(x\sim y\), afterwards \(v\sim y\) and \(x\sim u\), and nothing else changes. So such an \(f\) takes the same value at switch neighbours, and it is constant by Lemma 3.1. For an eigenvalue \(\lambda\) of \(H\), \(\lambda^2\ge\lambda\) and \(\lambda\ge0\), so \(\lambda=0\) or \(\lambda\ge1\). The functions with mean zero are orthogonal to the kernel, so all eigenvalues of \(H\) on them are at least \(1\), and \(\langle f,Hf\rangle=\langle f-\mathbb Ef,H(f-\mathbb Ef)\rangle\ge\|f-\mathbb Ef\|^2\). \(\square\)

For a pair \(a\), define \(J_a\) on each \(a\)-fiber by \(J_a=\sum_{k<l}(I-\tau_{kl})\), where \(k,l\) run over its singletons and \(\tau_{kl}\) exchanges their assignments.

**Lemma 5.2** (comparison). \(h_a\preceq n^2J_a\) for every pair \(a\), \(\sum_aJ_a=2L\), and \(H\preceq2n^2L\).

This is the fiberwise comparison that Carstens and Kleer used for bipartite switch and Curveball chains [CK], with its own constant.

**Proof.** Fix an \(a\)-fiber with \(N\) singletons and identify it with the \(q\)-subsets of the singletons (Lemma 4.1). Draw \(S_0\) uniformly and, independently, a uniformly random permutation \(\sigma\) of the singletons. Whatever \(S_0\) is, \(\sigma S_0\) is uniformly distributed, so \(S_0\) and \(\sigma S_0\) are independent copies, and \(\operatorname{Var}(f)=\frac12\mathbb E\bigl(f(S_0)-f(\sigma S_0)\bigr)^2\). Every permutation of \(N\) symbols is a product of at most \(N\) transpositions; fix such a product \(t_N\cdots t_1\) for each \(\sigma\), using identity factors where needed, and put \(S_m=t_m\cdots t_1S_0\). Given \(\sigma\), each \(S_m\) is the image of the uniform set \(S_0\) under a fixed permutation, hence uniform. By the Cauchy–Schwarz inequality \(\bigl(f(S_0)-f(S_N)\bigr)^2\le N\sum_m\bigl(f(S_{m-1})-f(S_m)\bigr)^2\), and the \(m\)-th term has expectation at most \(\sum_{k<l}\mathbb E(f-\tau_{kl}f)^2\). Therefore
\[
\operatorname{Var}(f)\le\frac{N^2}2\sum_{k<l}\mathbb E\bigl(f-\tau_{kl}f\bigr)^2=N^2\Bigl\langle f,\sum_{k<l}(I-\tau_{kl})f\Bigr\rangle,
\]
since \(\mathbb E(f-\tau f)^2=2\langle f,(I-\tau)f\rangle\) for an involution \(\tau\) preserving the measure. With \(N\le n\) and averaging over the fibers, \(h_a\preceq n^2J_a\).

A switch \(\{uv,xy\}\to\{ux,vy\}\) toggles the four-cycle \(u,v,y,x\). By the proof of Lemma 5.1 it is the exchange of \(v,x\) for the pair \(\{u,y\}\), and in the same way the exchange of \(u,y\) for the pair \(\{v,x\}\). Conversely, an exchange of two singletons \(k,l\) for a pair \(a\) changes exactly the four vertex pairs joining \(a\) to \(\{k,l\}\); if it produces this switch, these are the four edges of the toggled cycle, and \(a\) and \(\{k,l\}\) are its two pairs of opposite vertices. So every switch occurs exactly twice in \(\sum_aJ_a\), which proves \(\sum_aJ_a=2L\). Summing the first inequality gives \(H\preceq2n^2L\). \(\square\)

**Proposition 5.3.** If \(H^2\succeq H\), then for every \(f\), \(\operatorname{Var}_{\pi_d}(f)\le2n^2\langle f,Lf\rangle\), and Theorem 5.4 holds.

**Theorem 5.4** (OpenAI 2026). For every \(n\ge4\) and graphical \(d\), \(t_{\mathrm{mix}}(d)\le2n^8\), and if \(|\Omega_d|>1\), the spectral gap of \(P_d\) is at least \(\gamma_0=\bigl[24n^2\binom n4\bigr]^{-1}\).

Here \(t_{\mathrm{mix}}(d)\) is the least \(t\) with \(\max_G\|P_d^t(G,\cdot)-\pi_d\|_{\mathrm{TV}}\le\frac14\).

**Proof of Proposition 5.3.** Lemmas 5.1 and 5.2 give \(\operatorname{Var}(f)\le\langle f,Hf\rangle\le2n^2\langle f,Lf\rangle\). If \(|\Omega_d|=1\), the mixing time is \(0\). Otherwise, by (2.2), for \(f\) with mean zero, \(\langle f,(I-P_d)f\rangle=\langle f,Lf\rangle/(12\binom n4)\ge\gamma_0\|f\|^2\), so the eigenvalues of \(P_d\) on mean-zero functions lie in \([0,1-\gamma_0]\) (Lemma 2.1). By Lemma 1.1, the total variation distance is at most \(\frac14\) once \(t\ge\gamma_0^{-1}\bigl(\log2+\frac12\log|\Omega_d|\bigr)\). There are at most \(2^{\binom n2}\) graphs on \(V\), so \(\log2+\frac12\log|\Omega_d|\le(1+\frac{n(n-1)}4)\log2\le n^2\), and \(\gamma_0^{-1}=24n^2\binom n4=n^3(n-1)(n-2)(n-3)\le n^6\). Hence \(t_{\mathrm{mix}}(d)\le n^8+1\le2n^8\). \(\square\)

Theorem 5.4 follows from Proposition 5.3 and Theorem 4.2, which is Theorem 3.3 of [Disjoint pair resamplings](disjoint-pair-resamplings.md).

## 6. Exercises

**Exercise 6.1** (easy). Let \(n=4\) and \(d=(1,1,1,1)\). Show that \(\Omega_d\) consists of the three perfect matchings, that any two are switch neighbours, and that the spectral gap of \(P_d\) is \(\frac14\). Compare with \(\gamma_0\).

**Exercise 6.2** (easy). Show that in Lemma 1.1 the hypothesis that the eigenvalues are nonnegative cannot be dropped: give a symmetric \(P\) on two points whose eigenvalue on mean-zero functions is \(-1\) and for which \(P^t(x,\cdot)\) does not converge.

**Exercise 6.3** (medium). Run the greedy prescription of Lemma 3.1 on \(d=(2,2,2,2)\) and on \(d=(3,1,1,1)\).

**Exercise 6.4** (medium). Show that \(\langle f,Lf\rangle=\frac1{2|\Omega_d|}\sum_{G}\sum_{G'}\bigl(f(G)-f(G')\bigr)^2\), the inner sum running over the switch neighbours of \(G\), and deduce that \(L\succeq0\).

## 7. Solutions

**6.1.** A graph on four vertices with all degrees one is a perfect matching; there are three. The two edges of one matching have four distinct endpoints, and the edges of another matching are absent, so removing the first and inserting the second is a switch. Hence \(P_d(G,G')=\frac1{12}\) for \(G\neq G'\) and \(P_d(G,G)=\frac56\). On mean-zero functions, \(P_d\) acts by \(\frac56-\frac1{12}=\frac34\), so the gap is \(\frac14\), much larger than \(\gamma_0=\frac1{384}\).

**6.2.** \(P=\begin{pmatrix}0&1\\1&0\end{pmatrix}\) has eigenvalue \(-1\) on \((1,-1)\), and \(P^t(x,\cdot)\) alternates between the two point masses.

**6.3.** For \((2,2,2,2)\): vertex \(1\) joins the two vertices of largest residual degree among \(2,3,4\) (all equal), namely \(2\) and \(3\), leaving residual degrees \(1,1,2\) at \(2,3,4\); vertex \(2\) joins \(4\), leaving residual degrees \(1,1\) at \(3,4\); vertex \(3\) joins \(4\). The result is the four-cycle \(1,2,4,3\). For \((3,1,1,1)\), vertex \(1\) joins \(2,3,4\), giving the star.

**6.4.** Expanding \(\langle f,Lf\rangle=\frac1{|\Omega_d|}\sum_Gf(G)\sum_{G'}(f(G)-f(G'))\) as a sum over ordered pairs of switch neighbours, and averaging it with the same sum in which the two graphs of each pair are interchanged, gives the formula; a sum of squares is nonnegative.

## References

- [OpenAI-SW] OpenAI, *Polynomial mixing of the switch chain for every graphical degree sequence*, OpenAI Math Release preprint, 25 September 2026. https://github.com/openai/math/tree/main/preprints/Polynomial-Mixing-of-the-Switch-Chain-for-Every-Graphical-Degree-Sequence-September-25-2026
- [EGMMSS] P. L. Erdős, C. Greenhill, T. R. Mezei, I. Miklós, D. Soltész and L. Soukup, *The mixing time of the switch Markov chains: a unified approach*, European Journal of Combinatorics 99 (2022), 103421. https://arxiv.org/abs/1903.06600
- [FQW] W. Fu, Q. Qin and G. Wang, *Spectral gap for the binary fixed-margin swap chain*, 2026. https://arxiv.org/abs/2606.22636
- [CBS] C. J. Carstens, A. Berger and G. Strona, *A unifying framework for fast randomization of ecological networks with fixed (node) degrees*, MethodsX 5 (2018), 773–780; extended version. https://arxiv.org/abs/1609.05137
- [Caputo] P. Caputo, *On the spectral gap of the Kac walk and other binary collision processes*, ALEA Latin American Journal of Probability and Mathematical Statistics 4 (2008), 205–222. https://alea.impa.br/articles/v4/04-10.pdf
- [Havel] V. Havel, *Poznámka o existenci konečných grafů* (A remark on the existence of finite graphs), Časopis pro pěstování matematiky 80 (1955), 477–480. https://dml.cz/handle/10338.dmlcz/108220
- [DGU] M. Dyer, C. Greenhill and M. Ullrich, *Structure and eigenvalues of heat-bath Markov chains*, Linear Algebra and its Applications 454 (2014), 57–71. https://arxiv.org/abs/1301.4055
- [CK] C. J. Carstens and P. Kleer, *Speeding up switch Markov chains for sampling bipartite graphs with given degree sequence*, APPROX/RANDOM 2018, LIPIcs 116, 36:1–36:18 (open access). https://doi.org/10.4230/LIPIcs.APPROX-RANDOM.2018.36
