# Packings from covers and a fractional packing

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson proves the two "positive" facts about the instance built in [Coordinates, cells and items](coordinates-cells-and-items.md) and [Sizes that enforce the patterns](sizes-that-enforce-the-patterns.md). First, a vertex cover of size \(k\) gives a packing into exactly \(B\) bins: part (a) of the graph-to-packing reduction. Second, for the complete graph \(K_4\) and \(k=2\) the two configuration programs have value exactly \(B\), although \(K_4\) has no vertex cover with two vertices. Both rest on one *local construction* at each vertex, made in one of two *states*; an integral packing must choose one state per vertex, while a fractional packing can take half of each.

We keep the notation of the two previous lessons. Recall the completion \(h=b-\Delta\mathbf 1\{\text{short}\}-\operatorname{len}(U)-\operatorname{len}(D)\) of a row in a tuple of kind M (Lemma 4.1 of the previous lesson), and the deadline count (5.2) of the lesson before.

## 1. The local construction at a vertex

Fix a vertex \(v\) and a state, *selected* or *unselected*. The construction fixes, for every item of label \(v\) (rows, anchors and local auxiliaries), the tuple it belongs to, and for each tuple the *species* of the two unlabelled items it still needs: a global auxiliary of a given subclass and length, or an edge resource of a given edge and kind, and a flag of a given subclass.

*Rows of kind M.* All \(t_v\) tree rows of label \(v\) go to tuples of kind M. At every position \(r\in\mathcal R_v\), the \(d\) long job rows go to kind M if \(v\) is selected, the \(d\) short ones if \(v\) is unselected. This gives \(t_v+J_v\) tuples of kind M, as many as the label has deadlines and items \(D^{\mathrm M}\).

*Global species.* If \(v\) is selected, \(d\) rows of the root of \(T^+\) (baseline \(1\)) are *funded*: they need a global item \(U^+\) of length one. If \(v\) is unselected, \(d\) rows of the root of \(T^-\) (baseline \(5\)) are funded with items \(U^-\) of length one. Every other row of kind M needs a global item of length zero, of subclass \(U^+\) for plus tree rows and job rows and \(U^-\) for minus tree rows.

*Local items.* The funded rows get local items of length zero. Let \(\sigma\) be the unfunded side (\(\sigma=-\) if \(v\) is selected, \(+\) otherwise) and let \(\mathcal M^\sigma\) be the \(d\)-fold marking of \(T^\sigma\) from the competing-trees lemma ([Two competing trees](two-competing-trees.md), Lemma 1.1(b)). For every marked vertex \(x\), of depth \(\ell\), give one of the \(d\) rows of \(x\) a local item of length \(\lambda_\ell\); the quota \(|\mathcal M^\sigma\cap V_\ell|\leq p_\ell\) ensures enough such items. These \(s_v=|\mathcal M^\sigma|\leq P\) rows are different from each other and from the funded rows (they have positive depth). There remain \(t_v+J_v-s_v-d\geq P-s_v\) rows without a local item, by \(t_v\geq P+2d\) ((5.1) of the third lesson). Give the \(P-s_v\) unused items of positive length to distinct remaining rows and items of length zero to the others. Every item \(D^{\mathrm M}\) of label \(v\) is now used once.

*Flags.* Tree rows need a flag \(F^{\mathrm T}\), job rows of kind M a flag \(F^{\mathrm M}\).

*Deadlines.* For the \(t_v+J_v\) rows of kind M with their auxiliaries, consider the completions \(h\) and the intervals \([h,b)\).

**Lemma 1.1 (local coverage).** Whatever the global items of length zero and one are, as long as they have the prescribed lengths, every test interval of \(v\) is contained in at least \(d\) of the intervals \([h,b)\).

*Proof.* A funded row has \(h\leq b-1\), so its interval contains \([0,1)\) (selected) or \([4,5)\) (unselected): all test intervals on the funded side, \(d\) times. In particular, if \(v\) is selected, all job intervals are covered \(d\) times. On the unfunded side, a row of a marked vertex \(x\) of depth \(\ell\) has baseline the right endpoint of the cell of \(x\) and, with global length \(0\), completion its left endpoint; its interval is the cell of \(x\) without its right endpoint and contains the test interval of every leaf below \(x\) (Lemma 3.1(a) of the third lesson). Every complete path of \(T^\sigma\) meets \(\mathcal M^\sigma\) at least \(d\) times, so every leaf test of side \(\sigma\) lies in at least \(d\) such intervals. If \(v\) is unselected, each job position has \(d\) short rows of kind M with \(h\leq b_r-\Delta\), whose intervals contain the job interval \([b_r-\Delta,b_r)\). Additional positive lengths only enlarge intervals to the left. \(\square\)

The baselines of the rows of kind M are the tree baselines and \(d\) copies of \(b_r\) for every position \(r\), whether the rows are long or short: this is the multiset \(\mathcal B_v\). By (5.1) of the first lesson, Lemma 1.1 and the deadline count (5.2) of the third lesson,
\[
\#\{h\leq a\}=B_v(a)+\#\{[h,b)\ni a\}\geq B_v(a)+d\,\mathbf 1\{a\in\mathcal I_v\}=\#\{\text{deadlines of label }v\text{ at most }a\}
\]
for every real \(a\). By Lemma 5.2 (matching by sorting) of the first lesson there is a bijection from the rows of kind M to the deadlines of label \(v\) with \(h\leq z\) for each row. Attach the deadlines accordingly.

*Rows of kind G.* At each position \(r=(e,j)\in\mathcal R_v\), the \(d\) remaining job rows (short if \(v\) is selected, long if unselected) are paired with the \(d\) keys of label \(v\) at \(r\), with \(J_v\) items \(D^{\mathrm G}\) of label \(v\) and with flags \(F^{\mathrm G}\). They need an edge resource of edge \(e\): a *nonpermit* if \(v\) is selected, a *permit* if \(v\) is unselected.

**Lemma 1.2 (local templates).** In either state the construction gives \(N_v=t_v+2J_v\) *templates*: tuples of five roles in which the row, the anchor and the local item are specific items of label \(v\), each used exactly once, and the global item and the flag are specified by species. Completing a template with any items of the specified species gives a good table tuple that fits into a bin.

*Proof.* The patterns are those of the table (Section 4 of the third lesson): \(T^\pm,Z,U^\pm,D^{\mathrm M},F^{\mathrm T}\); \(S,Z,U^+,D^{\mathrm M},F^{\mathrm M}\); and \(S,Y,W,D^{\mathrm G},F^{\mathrm G}\). The labels agree. For kind M the completion depends only on the lengths, which the species fix, and \(h\leq z\) holds; for kind G the key, row and resource have the same position and edge, and a short row accepts a nonpermit, a long row a permit (Lemma 4.1(b) of the previous lesson). Lemma 4.1 of the previous lesson shows that the tuples fit. There are \(t_v+J_v\) templates of kind M and \(J_v\) of kind G. \(\square\)

The demands of the two states for unlabelled items are, for each edge \(e\) incident to \(v\):

| species | selected | unselected |
|---|---|---|
| \(U^+\) of length \(1\) | \(d\) | \(0\) |
| \(U^+\) of length \(0\) | \(t_{v,+}+J_v-d\) | \(t_{v,+}+J_v\) |
| \(U^-\) of length \(1\) | \(0\) | \(d\) |
| \(U^-\) of length \(0\) | \(t_{v,-}\) | \(t_{v,-}-d\) |
| permits of \(e\) | \(0\) | \(dR\) |
| nonpermits of \(e\) | \(dR\) | \(0\) |
| \(F^{\mathrm T}\), \(F^{\mathrm M}\), \(F^{\mathrm G}\) | \(t_v\), \(J_v\), \(J_v\) | \(t_v\), \(J_v\), \(J_v\) |

## 2. A packing from a vertex cover

**Proposition 2.1 (completeness).** If \(G\) has a vertex cover with at most \(k\) vertices, the items of the instance pack into \(B\) bins.

*Proof.* Enlarge the cover to a set \(C\) of exactly \(k\) vertices; it is still a cover. Make the local construction at every \(v\in C\) in the selected state and at every \(v\notin C\) in the unselected state. It remains to supply the unlabelled items, each exactly once.

*Global auxiliaries.* The templates need \(d|C|=dk\) items \(U^+\) of length one, \(d(n-k)\) items \(U^-\) of length one, \(\sum_v(t_{v,+}+J_v)-dk\) items \(U^+\) of length zero and \(\sum_vt_{v,-}-d(n-k)\) items \(U^-\) of length zero. These are exactly the stocks (Section 5 of the third lesson), so they can be assigned bijectively.

*Edge resources.* Let \(e\) have endpoints \(v_1,v_2\). Each endpoint has \(dR\) templates of kind G at the positions of \(e\). Since \(C\) is a cover, at least one endpoint is selected. If exactly one is, the unselected endpoint needs \(dR\) permits and the selected one \(dR\) nonpermits, the stock of \(e\). If both are selected, all \(2dR\) rows are short, and a short row accepts either kind (Lemma 4.1(b) of the previous lesson); assign the \(2dR\) resources of \(e\) to them in any way.

*Flags.* The demands \(\sum_vt_v\) and \(\sum_vJ_v\), \(\sum_vJ_v\) are the stocks.

Every item now lies in exactly one tuple, every tuple is a good table tuple that fits (Lemma 1.2), and there are \(\sum_v(t_v+2J_v)=B\) tuples. \(\square\)

This proves part (a) of the graph-to-packing reduction (Theorem 4.1 of the first lesson).

## 3. A fractional packing for the complete graph on four vertices

**Proposition 3.1 (fractional value).** For the instance built from the complete graph \(K_4\) with \(k=2\), with the constants of Section 1 of the third lesson,
\[
\mathrm{LP}_{\mathrm{ind}}(I)=\mathrm{LP}(I)=B .
\]

*Proof.* *Lower bound.* The instance has \(5B\) items of size greater than \(1/6\) (Lemma 2.1 of the previous lesson), so \(\mathrm{LP}\geq B\) by the counting bound (Lemma 1.4 of the first lesson), and \(\mathrm{LP}_{\mathrm{ind}}\geq\mathrm{LP}\).

*Pools.* Group the unlabelled items into *pools*: for each species of the table above, the set of all items of that species (the four kinds of \(U^\pm\), the permits and the nonpermits of each edge, and the three kinds of flags). Items in one pool have the same subclass and coordinate and no label, hence the same size. For \(n=4\), \(k=2\) every pool is nonempty: the length-one pools have \(dk=d(n-k)=2d\) items, and the other pools have at least \(dR\) or \(4d\) items.

*Demands.* Take both states at every vertex with weight \(\frac12\). The weighted demand for a pool equals its size. For length-one items \(U^+\): \(4\cdot\frac d2=2d=dk\); for \(U^-\): \(4\cdot\frac d2=2d=d(n-k)\). For length-zero items \(U^+\): \(\sum_v(t_{v,+}+J_v-\frac d2)=\sum_v(t_{v,+}+J_v)-2d\), the stock; similarly for \(U^-\). The permits of an edge \(e\) are demanded \(dR\) times by each endpoint in its unselected state, so \(2\cdot\frac12dR=dR\); likewise the nonpermits. The flags have the same demand in both states, equal to their stock.

*Columns.* For each vertex \(v\), each state and each of its templates \(b\), let \(i^X_b,i^A_b,i^D_b\) be its labelled items, \(\mathcal U_b\) the pool of its global species and \(\mathcal F_b\) the pool of its flag. For every pair \((u,f)\in\mathcal U_b\times\mathcal F_b\) give the individual configuration \(\{i^X_b,i^A_b,u,i^D_b,f\}\) the weight
\[
\frac1{2\,|\mathcal U_b|\,|\mathcal F_b|},
\]
adding weights if the same configuration arises several times. Each such set consists of five distinct items (their roles differ) and fits into a bin, by Lemma 1.2 and because all items of a pool have the same size; so it is an individual configuration. The columns of one template have total weight \(\frac12\).

*Coverage.* A labelled item of label \(v\) belongs to one template in each state of \(v\), so it is covered with weight \(\frac12+\frac12=1\). An item \(u\) of a pool \(\mathcal U\) receives from each template requesting \(\mathcal U\), after summing over flags, the weight \(\frac1{2|\mathcal U|}\); the templates requesting \(\mathcal U\), over both states and all vertices, number twice the weighted demand, that is \(2|\mathcal U|\). So \(u\) is covered with weight one. The same computation, summing over global items, applies to flags. Hence these weights are feasible for the individual configuration program, with value \(\sum_v(\frac{N_v}2+\frac{N_v}2)=B\).

So \(\mathrm{LP}_{\mathrm{ind}}\leq B\), and with Lemma 1.3 of the first lesson and the lower bound, both values equal \(B\). \(\square\)

The fractional packing never makes the two states coexist: each vertex is half selected and half unselected, which needs no vertex cover. An integral packing must decide, and the next lesson shows that any packing into \(B+c\) bins decides in a way that yields a vertex cover of size at most \(k+\rho n\); for \(K_4\), \(k=2\) and \(\rho=1/8\) this is impossible.

## 4. Exercises

**4.1.** In the proof of Proposition 2.1, where is it used that the cover has *exactly* \(k\) vertices, and why may a smaller cover be enlarged?

**4.2.** Suppose an edge had both endpoints unselected. Count the permits that its long rows of kind G would need, and compare with the stock.

**4.3.** In the local construction, why may the \(P-s_v\) unused local items of positive length be given to arbitrary remaining rows without spoiling Lemma 1.1? Why must they be used at all?

**4.4.** Check the weighted demand for the length-zero items \(U^-\) in the proof of Proposition 3.1.

**4.5.** Why does the fractional construction require that all items of a pool have the same size, and where does the construction of the sizes guarantee this?

## 5. Solutions

**4.1.** The stocks of length-one global items are exactly \(dk\) and \(d(n-k)\), and the bijection between demands and stocks needs \(|C|=k\). Adding vertices to a vertex cover keeps it a cover.

**4.2.** Each endpoint has \(dR\) long rows of kind G at the positions of \(e\), each needing a permit of \(e\): \(2dR\) in all, while \(e\) has only \(dR\) permits. A long row at its own position and edge does not fit with a nonpermit.

**4.3.** Positive lengths move completions to the left, so intervals only grow and coverage is preserved; the deadlines are attached after all lengths are fixed. They must be used because a packing uses every item, and the count of rows of kind M is exactly the number of items \(D^{\mathrm M}\).

**4.4.** Selected: \(t_{v,-}\); unselected: \(t_{v,-}-d\); half of each: \(t_{v,-}-\frac d2\). Summed over four vertices: \(\sum_vt_{v,-}-2d\), the number of items \(U^-\) of length zero, since \(d(n-k)=2d\) of them have length one.

**4.5.** A column replaces the template's unspecified item by an arbitrary member of the pool; it fits because the template fits with any representative, which needs equal sizes. By (1.2) of the previous lesson the size depends on the primary score (subclass), the secondary score (label, none here) and the coordinate (equal within a pool).

## References

- [OpenAI-BP] OpenAI, *Additive hardness and unbounded configuration gaps in bin packing*, OpenAI Math Release preprint, 24 September 2026, Sections 4 and 5. https://github.com/openai/math/tree/main/preprints/Additive-hardness-and-unbounded-configuration-gaps-in-bin-packing-September-24-2026
