# Expansion of the realized incidence

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The previous lesson bounded the *mean* incidence of a pair, averaged over the random table of its marked block. This lesson chooses an actual table. A tail bound for the number of edges leaving a fixed set, summed over all sets, would bring in the number of vertices of the layer, which grows without bound; instead the bad events are indexed by connected sets in a graph of bounded degree, and the Lovász local lemma, whose proof is included, finds a table that avoids all of them. A discrete Cheeger argument then turns the edge expansion into a spectral bound, uniform in the layers [OpenAI-KK, Lemma 5.3 and Proposition 5.4].

- The mean cut (Section 1).
- The tail of a cut (Section 2).
- The local lemma (Section 3).
- Choosing the tables (Section 4).
- From cuts to the incidence norm (Section 5).

The notation of [The mean incidence and its gap](the-mean-incidence-and-its-gap.md) is in force: a fixed adjacent pair \((i,k)\), \(A=A_i\), \(B=B_k\), \(D'=D_{ik}\), \(E=d|A|=D'|B|\), the tables at the earlier marked blocks of the family fixed, and the table of the marked block of \((i,k)\) random, so that its edges in \(Y^0\) are independent uniform matchings of clusters (Lemma 5.1 of [Gated permutations and the two towers](gated-permutations-and-the-two-towers.md)).

## 1. The mean cut

Give \(A\sqcup B\) the *degree measure* \(\mu(a)=d\), \(\mu(b)=D'\), and write \(v(Z)=\sum_{z\in Z}\mu(z)\), so that \(v(A\sqcup B)=2E\). For a set \(Z\) and a realization of the edges, let \(b(Z)\) be the number of edges with exactly one end in \(Z\).

On \(L^2(A\sqcup B,\mu)\) the random walk of a realization is \((R_0F)(x)=\mu(x)^{-1}\sum_{e\ni x}F(y_e)\), with \(y_e\) the other end of \(e\). It is self-adjoint, and
\[
\begin{gathered}
\langle(1-R_0)F,F\rangle_\mu\\
=\sum_{\text{edges }xy}|F(x)-F(y)|^2 .
\end{gathered}\tag{1.1}
\]
In particular \(\langle(1-R_0)\mathbf1_Z,\mathbf1_Z\rangle_\mu=b(Z)\). Up to the factor \(E\), \(L^2(A\sqcup B,\mu)\) is \(L^2(A)\oplus L^2(B)\) with the uniform measures, and the mean walk \(R=\mathbb ER_0\) is the block operator with off-diagonal blocks \(M\) and \(M^*\).

**Lemma 1.1** (mean cut). For every set \(Z\) with \(0<v(Z)\le E\), \(\mathbb E\,b(Z)\ge0.1\,v(Z)\).

*Proof.* The functions that are constant on each side span the eigenvectors \(\mathbf1\) and \(\mathbf1_A-\mathbf1_B\) of \(R\), with eigenvalues \(1\) and \(-1\). On their orthogonal complement, the sum of the spaces of functions of mean zero on each side, \(\|R\|<0.8\) by Lemma 4.1 of the previous lesson. So \(R\le0.8\) on the orthogonal complement of \(\mathbf1\). Write \(\mathbf1_Z=c\mathbf1+w\) with \(c=v(Z)/2E\) and \(w\perp\mathbf1\). Then
\[
\begin{aligned}
\mathbb E\,b(Z)&=\langle(1-R)w,w\rangle_\mu\ge0.2\|w\|_\mu^2\\
&=0.2\Bigl(v(Z)-\frac{v(Z)^2}{2E}\Bigr)\\
&\ge0.1\,v(Z) ,
\end{aligned}
\]
since \(v(Z)\le E\). \(\square\)

## 2. The tail of a cut

**Lemma 2.1** (tail for a cut; [OpenAI-KK, Lemma 5.3]). For every set \(Z\) with \(0<v(Z)\le E\),
\[
\mathbb P\Bigl\{b(Z)<\frac{v(Z)}{20}\Bigr\}\le e^{-v(Z)/400} .
\]

*Proof.* Let \(X\) be the number of edges with both ends in \(Z\). Every slot incidence at \(Z\) belongs to one edge, so \(b(Z)=v(Z)-2X\). Choose the side, \(A\) or \(B\), on which \(Z\) has fewer slot incidences, and let \(N_Z\le v(Z)/2\) be that number. In each cluster pair, the incidences of the chosen side that belong to \(Z\) are mapped by a uniform bijection to the other cluster, and the number of them landing in \(Z\) is a count of successes in sampling without replacement from a population of zeros and ones. These counts are independent over the cluster pairs, and their sample sizes add up to \(N_Z\). By Lemma 5.1 of [Streams, slots and slot evaluations](streams-slots-and-slot-evaluations.md), applied to each cluster, \(\mathbb Ee^{h(X-\mathbb EX)}\le e^{N_Zh^2/8}\) for all real \(h\).

By Lemma 1.1, \(\mathbb EX=\frac12(v(Z)-\mathbb Eb(Z))\le0.45\,v(Z)\), while \(b(Z)<v(Z)/20\) means \(X>0.475\,v(Z)\). So a bad cut requires \(X-\mathbb EX>v(Z)/40\); if \(N_Z=0\) this is impossible. By Markov's inequality with \(h=4(v(Z)/40)/N_Z\),
\[
\begin{aligned}
&\mathbb P\{X-\mathbb EX>v(Z)/40\}\\
&\quad\le\exp\Bigl(-\frac{2(v(Z)/40)^2}{N_Z}\Bigr)\\
&\quad\le e^{-v(Z)/400} .\qquad\square
\end{aligned}
\]

## 3. The local lemma

The local lemma is due to Erdős and Lovász. The asymmetric form below has a short proof by conditional probabilities [OpenAI-KK, Section 5].

**Lemma 3.1** (the local lemma, asymmetric form). Let \(\mathcal E_1,\ldots,\mathcal E_n\) be events in a probability space, and let a graph on \(\{1,\ldots,n\}\) be such that each \(\mathcal E_z\) is independent of the family of all \(\mathcal E_{z'}\) with \(z'\) not adjacent to \(z\) and \(z'\ne z\). If there are numbers \(0\le x_z<1\) with
\[
\mathbb P(\mathcal E_z)\le x_z\prod_{z'\sim z}(1-x_{z'})\qquad\text{for all }z,
\]
then \(\mathbb P\bigl(\bigcap_z\mathcal E_z^c\bigr)\ge\prod_z(1-x_z)>0\).

*Proof.* We show by induction on \(|\mathcal S|\) that \(\mathbb P(\mathcal E_z\mid\bigcap_{z'\in\mathcal S}\mathcal E_{z'}^c)\le x_z\) for every set \(\mathcal S\) of indices not containing \(z\) with \(\mathbb P(\bigcap_{\mathcal S}\mathcal E^c)>0\). Split \(\mathcal S\) into the neighbours \(\mathcal N\) of \(z\) and the rest \(\mathcal T\). If \(\mathcal N\) is empty, independence gives the probability \(\mathbb P(\mathcal E_z)\le x_z\). Otherwise
\[
\begin{aligned}
&\mathbb P\Bigl(\mathcal E_z\Bigm|\bigcap_{\mathcal S}\mathcal E^c\Bigr)\\
&\quad\le\frac{\mathbb P(\mathcal E_z\mid\bigcap_{\mathcal T}\mathcal E^c)}{\mathbb P(\bigcap_{\mathcal N}\mathcal E^c\mid\bigcap_{\mathcal T}\mathcal E^c)}\\
&\quad=\frac{\mathbb P(\mathcal E_z)}{\mathbb P(\bigcap_{\mathcal N}\mathcal E^c\mid\bigcap_{\mathcal T}\mathcal E^c)} .
\end{aligned}
\]
Writing \(\mathcal N=\{z_1,\ldots,z_r\}\), the denominator is the product of the probabilities \(1-\mathbb P(\mathcal E_{z_l}\mid\bigcap_{\mathcal T}\mathcal E^c\cap\bigcap_{l'<l}\mathcal E_{z_{l'}}^c)\), each conditioned on fewer than \(|\mathcal S|\) events, so by induction it is at least \(\prod_{\mathcal N}(1-x_{z'})\ge\prod_{z'\sim z}(1-x_{z'})\). This proves the claim. Then
\[
\begin{aligned}
&\mathbb P\Bigl(\bigcap_z\mathcal E_z^c\Bigr)\\
&\quad=\prod_{l=1}^n\Bigl(1-\mathbb P\Bigl(\mathcal E_l\Bigm|\bigcap_{l'<l}\mathcal E_{l'}^c\Bigr)\Bigr)\\
&\quad\ge\prod_l(1-x_l) ,
\end{aligned}
\]
where the conditioning events have positive probability by the same product, step by step. \(\square\)

## 4. Choosing the tables

Let \(\mathcal G\) be the finite simple graph on \(A\sqcup B\) in which two vertices are adjacent if some edge of the pair can join them, that is, if they carry slot incidences in matched clusters. A cluster has \(2^t\le2^s\) incidences, and a vertex has at most \(\max\{d,D'\}\le2D\) slots, so the maximum degree of \(\mathcal G\) is at most
\[
\Delta=2D\,2^s,\qquad\text{and we put }Q=1+\Delta .
\]

For every connected vertex set \(Z\) of \(\mathcal G\) with \(0<v(Z)\le E\), let \(\mathcal E_Z\) be the event \(b(Z)<v(Z)/20\). It suffices to avoid these events: an arbitrary set \(Z\) with \(0<v(Z)\le E\) is the disjoint union of its components in \(\mathcal G\), no edge joins two of them, so \(b\) and \(v\) are additive over the components, and each component has volume at most \(E\).

**Dependencies.** The event \(\mathcal E_Z\) depends only on the matchings of the cluster pairs with incidences in \(Z\). All vertices of one cluster pair are within distance two of each other in \(\mathcal G\), since every edge between its two sides is possible. So if two sets have distance more than two in \(\mathcal G\), their events depend on disjoint families of independent matchings, and \(\mathcal E_Z\) is independent of the family of all events of sets at distance more than two from \(Z\). Join two events when their sets have distance at most two.

**Counting.** At most \(zQ^2\) vertices lie within distance two of a set of \(z\) vertices. The number of connected sets of \(m\) vertices containing a given vertex is at most \(Q^{2(m-1)}\): a depth-first traversal of a spanning tree of the set, rooted at the vertex, is a walk of length \(2(m-1)\) that visits exactly the set, and with fixed orders on the vertices and on their neighbours, the set determines its first spanning tree and traversal, so sets correspond injectively to walks, of which there are at most \(\Delta^{2(m-1)}\). Hence an event \(\mathcal E_Z\) with \(|Z|=z\) has at most \(zQ^{2m}\) neighbours indexed by sets of \(m\) vertices.

**Lemma 4.1** (the realized expansion). For large \(\ell\), uniformly in the pair and in the tables at the earlier marked blocks, the table of the marked block of \((i,k)\) can be chosen so that
\[
\begin{gathered}
b(Z)\ge\frac{v(Z)}{20}\\
\text{for every set }Z\\
\text{with }0<v(Z)\le E .
\end{gathered}\tag{4.1}
\]

*Proof.* Put \(a=d/800\) and \(x_Z=e^{-a|Z|}\). Since \(\log Q=O(\ell)\) and \(d=2^{4\ell}\), for large \(\ell\)
\[
a\ge2,\qquad\rho:=Q^2e^{-a}\le\tfrac12 .
\]
Then
\[
\begin{aligned}
\sum_{Z'\sim Z}x_{Z'}&\le|Z|\sum_{m\ge1}Q^{2m}e^{-am}\\
&=|Z|\frac\rho{1-\rho}\le|Z| ,
\end{aligned}
\]
and since \(x_{Z'}\le e^{-2}<\frac12\) and \(\log(1-x)\ge-2x\) for \(0\le x\le\frac12\),
\[
\begin{aligned}
x_Z\prod_{Z'\sim Z}(1-x_{Z'})&\ge e^{-a|Z|-2|Z|}\\
&\ge e^{-2a|Z|}\ge e^{-v(Z)/400}\\
&\ge\mathbb P(\mathcal E_Z) ,
\end{aligned}
\]
using \(v(Z)\ge d|Z|\) (because \(D'\ge D/2\ge d\)) and Lemma 2.1. There are finitely many events, so Lemma 3.1 gives a table that avoids all of them. \(\square\)

## 5. From cuts to the incidence norm

**Proposition 5.1** (expansion of the realized incidence; [OpenAI-KK, Proposition 5.4]). For the tables of Lemma 4.1, let \(U^0_{ik}\) be the incidence matrix of the pair, from \(\ell^2(B_k)\) to \(\ell^2(A_i)\) with counting measures, divided by \(\sqrt{dD'}\). Then \(U^0_{ik}\) maps \(|B_k|^{-1/2}\mathbf1_{B_k}\) to \(|A_i|^{-1/2}\mathbf1_{A_i}\), its adjoint maps \(|A_i|^{-1/2}\mathbf1_{A_i}\) to \(|B_k|^{-1/2}\mathbf1_{B_k}\), and its norm from \(\mathbf1_{B_k}^\perp\) to \(\mathbf1_{A_i}^\perp\) is at most \(1-\chi\), where
\[
\chi=\frac1{800} .
\]

*Proof.* Let \(w\ge0\) be a function whose support has volume at most \(E\). Every level set \(\{w^2>t\}\) has volume at most \(E\), and an edge \(xy\) crosses it exactly for \(t\) between \(w(y)^2\) and \(w(x)^2\). Integrating (4.1),
\[
\begin{aligned}
&\sum_{\text{edges }xy}|w(x)^2-w(y)^2|\\
&\quad=\int_0^\infty b(\{w^2>t\})\,dt\\
&\quad\ge\frac1{20}\int_0^\infty v(\{w^2>t\})\,dt=\frac1{20}\|w\|_\mu^2 .
\end{aligned}
\]
By the Cauchy–Schwarz inequality and \((w(x)+w(y))^2\le2w(x)^2+2w(y)^2\), the square of the left side is at most \(\mathcal E(w)\cdot2\|w\|_\mu^2\), where \(\mathcal E(w)\) is the right side of (1.1), because every vertex \(x\) lies on \(\mu(x)\) edges. So \(\mathcal E(w)\ge\|w\|_\mu^2/800\).

Let \(f\) be real with \(\langle f,\mathbf1\rangle_\mu=0\). Order its finitely many values and choose \(m\) so that both \(\{f>m\}\) and \(\{f<m\}\) have volume at most \(E\). Apply the preceding bound to \(w_+=(f-m)_+\) and \(w_-=(m-f)_+\); on every edge
\[
\begin{aligned}
&(w_+(x)-w_+(y))^2\\
&\quad+(w_-(x)-w_-(y))^2\\
&\quad\le(f(x)-f(y))^2 ,
\end{aligned}
\]
with equality when both ends lie on the same side of \(m\), and by \(a^2+b^2\le(a+b)^2\) otherwise. Therefore
\[
\begin{aligned}
\mathcal E(f)&\ge\frac{\|f-m\|_\mu^2}{800}=\frac{\|f\|_\mu^2+2Em^2}{800}\\
&\ge\frac{\|f\|_\mu^2}{800} .
\end{aligned}
\]
Applying this to real and imaginary parts, \(R_0\le1-\chi\) on the orthogonal complement of \(\mathbf1\) in \(L^2(A\sqcup B,\mu)\).

Multiplication by \(\sqrt d\) on \(A\) and \(\sqrt{D'}\) on \(B\) is a unitary from \(L^2(A\sqcup B,\mu)\) to the counting space, and it carries \(R_0\) to the block operator with off-diagonal blocks \(U^0_{ik}\) and its adjoint. Each vertex of \(A\) has \(d\) edges and each vertex of \(B\) has \(D'\) edges, which, with \(d|A|=D'|B|\), gives the statements about constants. The two spaces of functions orthogonal to the constants on each side are invariant, and on their sum the block operator has norm \(\|U^0_{ik}|_{\mathbf1^\perp}\|\) and a spectrum symmetric about \(0\), because conjugation by \(\operatorname{diag}(1,-1)\) changes its sign. Its largest spectral value is therefore its norm. These vectors correspond to vectors orthogonal to \(\mathbf1\) in degree measure, where \(R_0\le1-\chi\). \(\square\)

**The tables.** There are finitely many families. In each family, the tables are chosen in increasing order of their marked blocks, each by Proposition 5.1, which applies whatever the earlier tables are; a table never changes the edges of an earlier pair, since its marked block is inactive on their padded streams (Lemma 2.1 of the lesson on gated permutations). Choosing at each step the first table in a fixed order of the finitely many candidates, all tables are defined, and every pair of \(Y^0\) satisfies Proposition 5.1.

## 6. Exercises

**6.1** (easy). Check (1.1) for the graph with one edge between \(a\in A\) and \(b\in B\), \(d=D'=1\).

**6.2** (medium). Show that the number of connected sets of \(m\) vertices containing a given vertex of the infinite \(\Delta\)-regular tree is at most \(\Delta^{2(m-1)}\), and compute it exactly for \(m=2,3\).

**6.3** (medium). In Lemma 3.1 with all \(x_z=x\) and every event having at most \(k\) neighbours, show that \(\mathbb P(\mathcal E_z)\le\frac1{e(k+1)}\) suffices, by choosing \(x=\frac1{k+1}\).

**6.4** (medium). For the cycle of length \(2n\) with alternate vertices in \(A\) and \(B\), \(d=D'=2\), compute the smallest ratio \(b(Z)/v(Z)\) over sets with \(v(Z)\le E\), and show that it tends to \(0\) with \(n\). Which step of this lesson fails for such graphs?

## 7. Solutions

**6.1.** \(\mu(a)=\mu(b)=1\), \((R_0F)(a)=F(b)\), \((R_0F)(b)=F(a)\), and
\[
\begin{aligned}
\langle(1-R_0)F,F\rangle&=|F(a)|^2+|F(b)|^2\\
&\quad-2\operatorname{Re}F(a)\overline{F(b)}\\
&=|F(a)-F(b)|^2 .
\end{aligned}
\]

**6.2.** Each connected set containing the root is the vertex set of a subtree, traversed by a closed walk of length \(2(m-1)\) from the root with at most \(\Delta\) choices per step. For \(m=2\): \(\Delta\) sets. For \(m=3\): either a path of two edges from the root, \(\Delta(\Delta-1)\) sets, or two neighbours of the root, \(\binom\Delta2\) sets; together \(\frac{3\Delta(\Delta-1)}2\le\Delta^4\).

**6.3.** \(x(1-x)^k=\frac1{k+1}\bigl(1-\frac1{k+1}\bigr)^k\ge\frac1{e(k+1)}\), since \((1-\frac1{k+1})^k\ge e^{-1}\).

**6.4.** A path of \(n\) consecutive vertices has \(v(Z)=2n=E\) and \(b(Z)=2\), so the ratio is \(1/n\). The mean bound of Lemma 1.1 fails: the incidence of a cycle has no uniform gap, since its second singular value tends to \(1\).

## References

- [OpenAI-KK] OpenAI, *A torsion-free counterexample to the Kadison–Kaplansky projection conjecture*, OpenAI Math Release preprint, 23 September 2026, Section 5, Lemma 5.3 and Proposition 5.4. https://github.com/openai/math/tree/main/preprints/A-Torsion-Free-Counterexample-to-the-Kadison-Kaplansky-Projection-Conjecture-September-23-2026
