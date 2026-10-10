# Extracting a vertex cover

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson proves part (b) of the graph-to-packing reduction: from any packing of the constructed instance into at most \(B+c\) bins one can read off a vertex cover of size at most \(k+\rho n\). With the earlier lessons this completes the proof that the configuration gap is unbounded (Theorem 3.1 of [Bin packing and the configuration program](bin-packing-and-the-configuration-program.md)). The last section derives the hardness of additive approximation from one imported theorem on satisfiability gaps.

The argument has four steps. Deadlines that the packing must meet force every test interval of every vertex to be covered almost \(d\) times (Section 1). The competing trees then force each vertex to spend almost \(d\) long global items on one of its two sides (Section 2). At the job positions, a vertex that spends little on the plus side must match many keys with long rows of the same position, which needs scarce permits (Section 3). Since each edge has only \(dR\) permits, one of its endpoints must spend on the plus side; and the global stock bounds how many vertices can do so (Section 4).

We use the notation of [Coordinates, cells and items](coordinates-cells-and-items.md), [Sizes that enforce the patterns](sizes-that-enforce-the-patterns.md) and [Packings from covers and a fractional packing](packings-from-covers-and-a-fractional-packing.md). Fix, throughout Sections 1 to 4, a packing into at most \(B+c\) bins. By Lemma 3.1 of the second of these lessons, for every label \(v\) fewer than \(3K\) anchors of label \(v\) lie outside good tuples; this holds for every subset of these anchors, in particular for the deadlines at most a given point and for the keys at given positions.

## 1. Coverage at every test point

For a label \(v\) let \(\mathcal M_v\) be the set of good tuples of kind M of label \(v\) in the packing. Each \(M\in\mathcal M_v\) has a row baseline \(b(M)\), a completion \(h(M)\leq b(M)\) and an interval \([h(M),b(M))\). Let \(x_v^+\) and \(x_v^-\) be the numbers of tuples in \(\mathcal M_v\) whose global item is \(U^+\), respectively \(U^-\), of length one. Distinct tuples use distinct items, so the stocks give
\[
\sum_vx_v^+\leq dk,\qquad\sum_vx_v^-\leq d(n-k),\qquad\sum_v(x_v^++x_v^-)\leq dn.\tag{1.1}
\]
For a real \(a\) put
\[
A_v(a)=\#\{M\in\mathcal M_v:b(M)\leq a\},\quad C_v(a)=\#\{M\in\mathcal M_v:h(M)\leq a\},\quad I_v(a)=\#\{M\in\mathcal M_v:a\in[h(M),b(M))\}.
\]
By the prefix identity (5.1) of the first lesson,
\[
C_v(a)=A_v(a)+I_v(a).\tag{1.2}
\]
Recall that \(B_v(a)\) counts the members of the baseline multiset \(\mathcal B_v\) at most \(a\); it is defined by the instance, not by the packing.

**Lemma 1.1 (prefix bounds).** For every label \(v\) and every real \(a\),
\[
C_v(a)\geq\#\{\text{deadlines of label }v\text{ at most }a\}-3K,\tag{1.3}
\]
\[
A_v(a)\leq B_v(a)+3K-\xi,\tag{1.4}
\]
where \(\xi\geq0\) is the number of good tuples of kind G whose key has label \(v\) and baseline greater than \(a\) and whose row has baseline at most \(a\).

*Proof.* (1.3) A deadline is an anchor of subclass \(Z\), which occurs only in tuples of kind M. Of the deadlines of label \(v\) at most \(a\), all but fewer than \(3K\) lie in good tuples, which then belong to \(\mathcal M_v\) and fit, so \(h\leq z\leq a\) (Lemma 4.1(a) of the second lesson). Different deadlines lie in different tuples.

(1.4) The tree rows of label \(v\) with baseline at most \(a\) number exactly the tree part of \(B_v(a)\). For the job rows, let \(N'\) be the number of positions \(r\in\mathcal R_v\) with \(b_r\leq a\); there are \(2dN'\) job rows of label \(v\) with baseline at most \(a\), and \(B_v(a)\) contains \(dN'\) job baselines. The \(dN'\) keys of label \(v\) at these positions lie, all but fewer than \(3K\), in good tuples of kind G, whose rows have label \(v\) and a position not later than the key (Lemma 4.1(b) of the second lesson), hence baseline at most \(a\). The \(\xi\) tuples of the statement use further such rows, with keys at later positions. All these tuples are distinct and use distinct rows, so at least \(dN'-3K+\xi\) job rows of label \(v\) with baseline at most \(a\) are used in tuples of kind G, and at most \(2dN'-(dN'-3K+\xi)=dN'+3K-\xi\) remain for \(\mathcal M_v\). Adding the tree rows gives (1.4). \(\square\)

**Lemma 1.2 (coverage).** For every label \(v\) and every point \(a\) of a test interval of \(v\),
\[
I_v(a)\geq d-6K .
\]

*Proof.* There are \(B_v(a)+d\) deadlines of label \(v\) at most \(a\), by (5.2) of the third lesson. By (1.2), (1.3) and (1.4) with \(\xi\geq0\),
\[
I_v(a)=C_v(a)-A_v(a)\geq(B_v(a)+d-3K)-(B_v(a)+3K)=d-6K.\qquad\square
\]

## 2. Every vertex pays for one side

**Lemma 2.1 (a large count on one side).** Every vertex \(v\) satisfies \(x_v^+\geq d-6K\) or \(x_v^-\geq d-6K\).

*Proof.* Suppose \(x_v^+<d-6K\) and \(x_v^-<d-6K\). Choose a point \(a_y\) in the interior of the cell of every leaf \(y\) of \(T^+\) and of \(T^-\) (in the copy belonging to \(v\)).

*Marks.* For every tuple \(M\in\mathcal M_v\) whose global item has length \(0\) and whose local item has positive length \(\lambda_\ell\), the interval of \(M\) has length at most \(\lambda_\ell+\Delta\) (Corollary 4.2(a) of the second lesson) and therefore meets at most one cell of depth \(\ell\), over both trees (Lemma 3.1(c) of the third lesson). If it meets one, mark the corresponding vertex of \(T^+\) or of \(T^-\). Let \(\mathcal A^+,\mathcal A^-\) be the sets of marked vertices. Different tuples use different local items, and label \(v\) has exactly \(p_\ell\) local items of length \(\lambda_\ell\); so
\[
|\mathcal A^+\cap V_\ell(T^+)|+|\mathcal A^-\cap V_\ell(T^-)|\leq p_\ell\qquad(1\leq\ell\leq L).
\]

*Every leaf is reached.* Let \(y\) be a leaf of \(T^+\). The point \(a_y\) lies in a test interval, so by Lemma 1.2 at least \(d-6K\) intervals of \(\mathcal M_v\) contain it. An interval with a global item \(U^-\) belongs to a minus row and lies in \((2,5]\); one with a length-one \(U^+\) is one of at most \(x_v^+<d-6K\). So some interval containing \(a_y\) has a global item of length \(0\). If its local item also had length \(0\), the interval would be empty or a job test interval (Corollary 4.2(b) of the second lesson), and job intervals are disjoint from leaf cells. So its local item has some length \(\lambda_\ell>0\), the interval meets the cell of depth \(\ell\) that contains \(a_y\), which is the cell of the ancestor of \(y\) of depth \(\ell\) (Lemma 3.1(c) of the third lesson), and that ancestor is in \(\mathcal A^+\). It lies on the complete path to \(y\). The same argument applies to the leaves of \(T^-\), using \(x_v^-<d-6K\).

So \(\mathcal A^+\) and \(\mathcal A^-\) hit every complete path of \(T^+\) and of \(T^-\) while respecting the shared quotas. This contradicts the competing-trees lemma ([Two competing trees](two-competing-trees.md), Lemma 1.1(c)). \(\square\)

## 3. Job positions and displaced rows

The forced side does not yet tell us that the edges are covered. That needs the job positions. A key may take a row of an earlier position; such a *displaced* row is missing from the prefix count, and we keep track of it with \(\xi\) of Lemma 1.1.

Call a position \(r\in\mathcal R_v\) *excluded* if its closed job cell \([b_r-\Delta,b_r]\) meets the interval of some \(M\in\mathcal M_v\) with global length \(0\) and positive local length. Such an interval has length at most \(\lambda_1+\Delta\) and meets at most one job cell (Lemma 3.1(c) of the third lesson), and there are at most \(P\) such tuples (label \(v\) has \(P\) local items of positive length). So at most \(P\) positions of \(\mathcal R_v\) are excluded, and every edge at \(v\) keeps at least \(R-P\) positions that are not excluded.

For \(r\in\mathcal R_v\) let \(L_{v,r}\) be the number of good tuples of kind G whose key is at \(r\) (label \(v\)) and whose row is a long row of the same position \(r\).

**Lemma 3.1 (long matches at a job).** Every position \(r\in\mathcal R_v\) that is not excluded satisfies
\[
L_{v,r}\geq d-x_v^+-9K .
\]

*Proof.* Let \(a=b_r-\Delta/2\), a point of the job interval of \(r\). Baselines of different positions differ by at least \(g>\Delta\), so the positions with baseline at most \(a\) are exactly those before \(r\). Let \(\xi\) count the good tuples of kind G with key at \(r\) and row at an earlier position; these are counted by the \(\xi\) of Lemma 1.1 at this \(a\), so \(A_v(a)\leq B_v(a)+3K-\xi\). Let \(u\) be the number of short rows of position \(r\) used in \(\mathcal M_v\).

*Upper bound for \(I_v(a)\).* An interval of \(\mathcal M_v\) containing \(a\) belongs to one of these kinds: (i) global item of length one: necessarily \(U^+\), since minus rows cannot reach \(a<1\); at most \(x_v^+\) such intervals; (ii) global length \(0\) and positive local length: impossible, since \(r\) is not excluded; (iii) both lengths \(0\): tree rows and long rows give empty intervals, and a short row gives its own job interval, which contains \(a\) only for position \(r\); at most \(u\) such intervals. So \(I_v(a)\leq x_v^++u\).

*Comparison.* By (1.2), (1.3) with the \(B_v(a)+d\) deadlines at most \(a\), and (1.4),
\[
B_v(a)+d-3K\leq C_v(a)=A_v(a)+I_v(a)\leq B_v(a)+3K-\xi+x_v^++u,
\]
that is,
\[
u-\xi\geq d-x_v^+-6K.\tag{3.1}
\]

*Counting the keys at \(r\).* At least \(d-3K\) of the \(d\) keys at \(r\) lie in good tuples of kind G. Exactly \(\xi\) of these use rows of earlier positions; all the others use rows of position \(r\) itself (Lemma 4.1(b) of the second lesson). At most \(d-u\) short rows of position \(r\) are available to them, the other \(u\) being in \(\mathcal M_v\). So at least \(d-3K-\xi-(d-u)\) of them use long rows of position \(r\):
\[
L_{v,r}\geq u-\xi-3K\geq d-x_v^+-9K\qquad\text{by (3.1)}.\qquad\square
\]

## 4. A vertex cover of the right size

**Lemma 4.1 (the threshold set covers every edge).** The set \(C=\{v:x_v^+>d/8\}\) is a vertex cover of \(G\).

*Proof.* Fix an edge \(e\) with endpoints \(v_1,v_2\).

*Earlier edges.* The edge resources of the edges \(1,\ldots,e-1\) number \(2dR(e-1)\); so do the keys at positions of these edges, over all labels (each edge has two endpoints, \(R\) positions and \(d\) keys per endpoint and position). All but fewer than \(3nK\) of these keys lie in good tuples of kind G, and each of these tuples uses a resource of an edge not later than its key's edge (Lemma 4.1(b) of the second lesson), hence an earlier-edge resource. So fewer than \(3nK\) earlier-edge resources are left for all other tuples.

*Capacity.* A tuple counted by \(L_{v,(e,j)}\) has a long row at its key's position, so its resource is a permit of \(e\) or belongs to an earlier edge (Lemma 4.1(b) of the second lesson). Summing over both endpoints and all \(j\),
\[
\sum_{v\in\{v_1,v_2\}}\sum_{j=1}^RL_{v,(e,j)}\leq dR+3nK.\tag{4.1}
\]

*Contradiction if both endpoints are outside \(C\).* Then \(x_{v_i}^+\leq d/8\), and by Lemma 3.1 and \(d\geq72K\), every position of \(e\) at \(v_i\) that is not excluded has
\[
L_{v_i,(e,j)}\geq d-\frac d8-9K\geq\frac{3d}4 .
\]
Each endpoint has at least \(R-P\) such positions of \(e\), so the left side of (4.1) is at least \(2(R-P)\frac{3d}4\). With \(R=100(P+nK+1)\),
\[
2(R-P)\frac{3d}4-(dR+3nK)=\frac d2(R-3P)-3nK=\frac{97d}2P+(50d-3)nK+50d>0,
\]
contradicting (4.1). So every edge has an endpoint in \(C\). \(\square\)

**Lemma 4.2 (size of the cover).**
\[
|C|\leq\frac{dk}{d-6K}+\frac{48Kn}d\leq k+\frac{60Kn}d\leq k+\rho n .
\]

*Proof.* Let \(V_+=\{v:x_v^+\geq d-6K\}\). Since \(d\geq72K\), \(d-6K>d/8\), so \(V_+\subseteq C\); by (1.1), \(|V_+|(d-6K)\leq\sum_vx_v^+\leq dk\).

For \(v\in V_+\) *charge* \(x_v^+\), and for \(v\notin V_+\) charge \(x_v^-\), which is at least \(d-6K\) by Lemma 2.1. Every vertex is charged at least \(d-6K\), so the charges total at least \(n(d-6K)\), while all counts together total at most \(dn\) by (1.1). The uncharged counts, among them \(x_v^+\) for \(v\notin V_+\), total at most \(6Kn\). Each vertex of \(C\setminus V_+\) has \(x_v^+>d/8\), so \(|C\setminus V_+|<48Kn/d\). This gives the first inequality. For the second, \(d\geq12K\) gives \(d-6K\geq d/2\), and with \(k\leq n\),
\[
\frac{dk}{d-6K}-k=\frac{6Kk}{d-6K}\leq\frac{12Kn}d .
\]
The last inequality is \(d\geq120K/\rho\) (1.2 of the third lesson), which even gives \(60Kn/d\leq\rho n/2\). \(\square\)

**Proposition 4.3 (soundness).** If the instance packs into at most \(B+c\) bins, then \(G\) has a vertex cover with at most \(k+\rho n\) vertices.

*Proof.* Lemmas 4.1 and 4.2. \(\square\)

This proves part (b) of the graph-to-packing reduction. Together with Proposition 2.1 of the previous lesson (part (a)) and Section 5 of the second lesson before it (running time), Theorem 4.1 of the first lesson is proved; and with Proposition 3.1 of the previous lesson, so is Theorem 3.1 there: *for every \(c\geq0\) there is an instance with configuration value \(B\) and optimum greater than \(B+c\).* The proof of Theorem 3.1 given in the first lesson uses \(K_4\), \(k=2\) and \(\rho=1/8\).

## 5. Hardness of additive approximation

*Complexity notions.* Instances are finite objects encoded as bit strings, and an algorithm runs in polynomial time if its number of steps is bounded by a polynomial in the length of its input. A language \(\mathcal L\) belongs to NP if there are a polynomial \(q\) and a polynomial-time algorithm \(V\) such that \(x\in\mathcal L\) exactly when some string \(y\) of length at most \(q(|x|)\) makes \(V(x,y)\) accept. A *distinguishing problem* is a pair of disjoint sets \((\mathrm{YES},\mathrm{NO})\) of instances. It is *NP-hard* if for every \(\mathcal L\) in NP there is a polynomial-time map \(\phi\) with \(\phi(x)\in\mathrm{YES}\) for \(x\in\mathcal L\) and \(\phi(x)\in\mathrm{NO}\) for \(x\notin\mathcal L\). Composing such a map with a polynomial-time map that sends YES into YES' and NO into NO' shows that (YES', NO') is NP-hard as well. If an NP-hard distinguishing problem can be solved in polynomial time (by an algorithm correct on YES and NO instances), then every language in NP is decidable in polynomial time, that is \(\mathrm P=\mathrm{NP}\).

We import one theorem. It is a consequence of the theory of probabilistically checkable proofs and is not proved in this programme; it is an open obligation of the course.

**Imported theorem (Håstad's satisfiability gap).** Let \(\eta=1/16\). It is NP-hard to distinguish satisfiable formulas in conjunctive normal form with exactly three literals per clause (and at least one clause) from such formulas in which every assignment satisfies at most a fraction \(1-\eta\) of the clauses.

Håstad proved this with soundness \(7/8+\varepsilon\) for every \(\varepsilon>0\); \(\varepsilon=1/16\) gives \(\eta=1/16\).

*The clause graph.* For a formula \(F\) with \(M\geq1\) clauses of three literal places each, let \(G_F\) have one vertex for every literal place, \(n=3M\) vertices, the three places of each clause joined into a triangle, and two places joined whenever they hold complementary literals (one edge per pair). Let \(\operatorname{MAXSAT}(F)\) be the largest number of clauses satisfied by one assignment.

**Lemma 5.1.** \(\tau(G_F)=3M-\operatorname{MAXSAT}(F)\).

*Proof.* The complement of a vertex cover is an *independent set* (no two of its vertices adjacent) and conversely, so \(\tau=n-\alpha\), with \(\alpha\) the largest size of an independent set. An independent set contains at most one place of each clause and no two complementary literals; setting its literals true (consistently) and the other variables arbitrarily satisfies every clause that has a chosen place, so \(\operatorname{MAXSAT}\geq\alpha\). Conversely, given an assignment, choose a true place in every satisfied clause; two chosen places are in different clauses and both true, hence not complementary, so they form an independent set, and \(\alpha\geq\operatorname{MAXSAT}\). \(\square\)

So a satisfiable formula gives \(\tau(G_F)=2M\), and a formula of the second kind in the imported theorem gives \(\tau(G_F)\geq3M-(1-\eta)M=2M+\frac\eta3n\).

**Theorem 5.2 (additive hardness; OpenAI, 2026; Theorem 3.2 of the first lesson).** For every fixed \(c\geq0\) it is NP-hard to distinguish pairs \((I,B)\) for which \(I\) packs into \(B\) bins from pairs for which \(I\) does not pack into \(B+c\) bins, with all sizes above \(1/6\).

*Proof.* Fix \(c\) and \(\rho=1/96<\eta/3\). Map a formula \(F\) to \(G_F\) with \(k=2M\), and then to the instance of the graph-to-packing reduction with these \(c,\rho\); both maps take polynomial time, and \(G_F\) has at least one edge. If \(F\) is satisfiable, \(\tau(G_F)=k\) and Proposition 2.1 of the previous lesson packs the items into \(B\) bins. In the other case \(\tau(G_F)\geq k+n/48>k+\rho n\), so by Proposition 4.3 there is no packing into \(B+c\) bins. Composing with the imported theorem gives the claim. \(\square\)

**Corollary 5.3 (Corollary 3.3 of the first lesson).** A deterministic polynomial-time algorithm that always uses at most \(\mathrm{OPT}(I)+C\) bins, for an absolute constant \(C\), exists if and only if \(\mathrm P=\mathrm{NP}\).

*Proof.* If such an algorithm exists, take \(c\geq C\) in Theorem 5.2 and run it on \(I\): for a pair of the first kind it uses at most \(B+C\leq B+c\) bins, for one of the second kind more than \(B+c\) bins. Counting the bins solves an NP-hard distinguishing problem in polynomial time, so \(\mathrm P=\mathrm{NP}\).

Conversely, suppose \(\mathrm P=\mathrm{NP}\). The language of triples (instance, number \(b\), partial assignment of items to bins \(1,\ldots,b\)) that can be completed to a packing into \(b\) bins is in NP: a completion is a certificate, checked by exact rational arithmetic in polynomial time. So it is decidable in polynomial time. Find \(\mathrm{OPT}(I)\) by trying \(b=0,1,\ldots,|\mathcal I|\) (or by binary search), then place the items one at a time, trying the bins \(1,\ldots,\mathrm{OPT}(I)\) for each and keeping a choice for which a completion still exists. This uses at most \(|\mathcal I|^2+|\mathcal I|+1\) decisions and finds an optimal packing, so \(C=0\) works. \(\square\)

**Remark 5.4 (formal verification).** OpenAI's release contains a Lean formalization of these results. Its scope document states: for every integer \(c\geq0\) there are an integer \(B\) and a rational instance with \(5B\) items whose individual and type configuration values both equal \(B\) and whose optimum exceeds \(B+c\); distinguishing packings into \(B\) bins from the absence of packings into \(B+c\) bins is NP-hard for each fixed \(c\); and a polynomial-time algorithm with a fixed additive allowance exists exactly when \(\mathrm P=\mathrm{NP}\), in which case an optimal algorithm is constructed.

## 6. Exercises

**6.1.** In Lemma 1.2 the loss \(6K\) consists of two losses of \(3K\). Which anchors does each of them concern?

**6.2.** Show that Lemma 3.1 would fail without the correction \(\xi\): describe how keys at \(r\) matched with rows of earlier positions could otherwise make \(u\) large without producing long matches at \(r\).

**6.3.** Verify the identity \(\frac d2(R-3P)-3nK=\frac{97d}2P+(50d-3)nK+50d\) for \(R=100(P+nK+1)\).

**6.4.** For \(K_4\), \(k=2\) and \(\rho=1/8\), show that Lemma 4.2 gives \(|C|\leq2\), while every vertex cover of \(K_4\) has at least three vertices. Which hypothesis of the soundness proposition is then violated?

**6.5.** Check Lemma 5.1 on the formula consisting of the two clauses \(x\vee x\vee x\) and \(\neg x\vee\neg x\vee\neg x\).

## 7. Solutions

**6.1.** One loss concerns the deadlines of label \(v\) at most \(a\), which must lie in good tuples to give completions at most \(a\) (1.3); the other concerns the keys at positions with baseline at most \(a\), which must lie in good tuples to remove rows from the prefix (1.4).

**6.2.** A key at \(r\) may take a short or long row of an earlier position. Each such match removes a row from the earlier prefix, so fewer rows there are available to tuples of kind M, \(A_v(a)\) drops by one, and the deadline inequality can then be met with one interval less at \(a\): one short row of position \(r\) fewer is needed in kind M. The term \(-\xi\) in (1.4) records exactly this, and \(L_{v,r}\geq u-\xi-3K\) subtracts these matches from the keys at \(r\).

**6.3.** \(\frac d2(R-3P)=\frac d2(97P+100nK+100)=\frac{97d}2P+50dnK+50d\); subtract \(3nK\).

**6.4.** \(\frac{60Kn}d\leq\frac{\rho n}2=\frac14\), so \(|C|\leq k+\frac14\) and, \(|C|\) being an integer, \(|C|\leq2\). A set of two vertices of \(K_4\) misses the edge between the other two. So no packing into at most \(B+c\) bins exists: the hypothesis of Proposition 4.3 fails.

**6.5.** The graph has six vertices: two triangles, and every place of the first clause joined to every place of the second (complementary literals). \(\operatorname{MAXSAT}=1\), and the largest independent set has one vertex, since any two places are in one clause or complementary. So \(\tau=6-1=5=3\cdot2-1\).

## References

- [OpenAI-BP] OpenAI, *Additive hardness and unbounded configuration gaps in bin packing*, OpenAI Math Release preprint, 24 September 2026, Sections 6 and 7. https://github.com/openai/math/tree/main/preprints/Additive-hardness-and-unbounded-configuration-gaps-in-bin-packing-September-24-2026
- [OpenAI-Lean] OpenAI Math Release, *Bin packing and unbounded configuration-LP gaps*, scope of the Lean formalization. https://github.com/openai/math/blob/main/lean/docs/118.md
- J. Håstad, *Some optimal inapproximability results*, J. ACM 48 (2001), Theorem 6.5, is the source of the imported theorem; R. M. Karp (1972) gave the satisfiability-to-clique graph that the clause graph complements. Both are named for credit; The imported theorem is an open obligation of the course.
