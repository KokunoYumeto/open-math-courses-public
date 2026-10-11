# Prophets, matroids and an almighty adversary

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

A *prophet inequality* compares an online selection, made one item at a time without knowledge of the future, with the best selection made in hindsight. In the setting of this course the selected items must form an independent set of a matroid, the value of each item is random with an unknown distribution, and the selector knows only one independent sample from each distribution. The order of arrival is chosen by an adversary who sees every sample, every value and every random choice of the selector. This course proves OpenAI's 2026 theorem that a fixed constant fraction of the best value is still achievable: one sample suffices.

This lesson sets up matroids with complete proofs of the facts used later, proves that the greedy rule finds a best independent set, states the theorem, and reduces it to a problem about one fixed, hidden vector of weights.

## 1. Matroids, rank and closure

A *matroid* \(M=(E,\mathcal I)\) consists of a finite set \(E\) of *labels* and a family \(\mathcal I\) of subsets of \(E\), the *independent sets*, such that \(\varnothing\in\mathcal I\), every subset of an independent set is independent, and the *augmentation axiom* holds: if \(I,J\in\mathcal I\) and \(|I|<|J|\), then \(I\cup\{e\}\in\mathcal I\) for some \(e\in J\setminus I\). Examples: all sets of size at most \(k\) (the uniform matroid); the edge sets of forests of a graph (the graphic matroid); the linearly independent sets of columns of a matrix.

For \(X\subseteq E\), a *basis* of \(X\) is a maximal independent subset of \(X\).

**Lemma 1.1.** All bases of a set \(X\) have the same size, and every independent subset of \(X\) is contained in a basis of \(X\).

*Proof.* If \(I,J\) are bases of \(X\) with \(|I|<|J|\), augmentation gives \(e\in J\setminus I\subseteq X\) with \(I\cup\{e\}\) independent, contradicting maximality of \(I\). An independent subset of \(X\) can be enlarged inside \(X\) until it is maximal, since \(X\) is finite. \(\square\)

The common size is the *rank* \(\operatorname{rk}(X)\). Clearly \(\operatorname{rk}(X)\leq|X|\), with equality exactly for independent \(X\), and \(\operatorname{rk}\) is increasing: a basis of \(X\subseteq Y\) is an independent subset of \(Y\).

**Lemma 1.2 (submodularity).** For all \(A,B\subseteq E\),
\[
\begin{aligned}
&\operatorname{rk}(A)+\operatorname{rk}(B)\\
&\quad\geq\operatorname{rk}(A\cup B)\\
&\qquad+\operatorname{rk}(A\cap B).
\end{aligned}\tag{1.1}
\]

*Proof.* Let \(I\) be a basis of \(A\cap B\). By Lemma 1.1 extend it to a basis \(I\cup I_A\) of \(A\), and then to a basis \(I\cup I_A\cup I_B\) of \(A\cup B\). No element of \(I_B\) lies in \(A\), since adding it to the basis \(I\cup I_A\) of \(A\) would keep independence; so \(I_B\subseteq B\setminus A\) and \(I\cup I_B\) is an independent subset of \(B\). Hence
\[
\begin{aligned}
&\operatorname{rk}(A)+\operatorname{rk}(B)\\
&\quad\geq(|I|+|I_A|)+(|I|+|I_B|)\\
&\quad=\operatorname{rk}(A\cup B)+\operatorname{rk}(A\cap B).\qquad\square
\end{aligned}
\]

The *conditional rank* of \(A\) over \(P\) is \(\operatorname{rk}(A\mid P)=\operatorname{rk}(A\cup P)-\operatorname{rk}(P)\). Applying (1.1) to \(A\cup P\) and \(P'\) for \(P\subseteq P'\) gives
\[
\operatorname{rk}(A\mid P')\leq\operatorname{rk}(A\mid P):\tag{1.2}
\]
conditional rank decreases when the conditioning set grows. A set \(A\) is *independent over* \(P\) if \(\operatorname{rk}(A\mid P)=|A|\); then every subset \(A'\subseteq A\) is independent over \(P\) as well, since \(\operatorname{rk}(A\mid P)\) is the sum of \(\operatorname{rk}(A'\mid P)\) and \(\operatorname{rk}(A\setminus A'\mid P\cup A')\), and the last term is at most \(|A\setminus A'|\).

The *closure* of \(X\) is \(\operatorname{cl}(X)=\{e\in E:\operatorname{rk}(X\cup\{e\})=\operatorname{rk}(X)\}\). We say that \(X\) *spans* \(e\), or \(A\), when \(e\in\operatorname{cl}(X)\), or \(A\subseteq\operatorname{cl}(X)\). A *flat* is a set with \(\operatorname{cl}(F)=F\). The *loops* are the elements of \(L=\operatorname{cl}(\varnothing)\), those \(e\) with \(\{e\}\) dependent; every nonloop forms an independent set by itself.

**Lemma 1.3 (closure).** For all \(X,Y\subseteq E\):

(a) \(X\subseteq\operatorname{cl}(X)\), and \(X\subseteq Y\) implies \(\operatorname{cl}(X)\subseteq\operatorname{cl}(Y)\);

(b) \(\operatorname{rk}(X\cup Z)=\operatorname{rk}(X)\) for every \(Z\subseteq\operatorname{cl}(X)\); in particular \(\operatorname{rk}(\operatorname{cl}(X))=\operatorname{rk}(X)\), and adjoining spanned elements to \(X\) changes neither its rank nor its closure;

(c) \(\operatorname{cl}(X)\) is a flat, and it is the smallest flat containing \(X\);

(d) the intersection of two flats is a flat, and a flat \(F\) properly contained in a flat \(G\) has \(\operatorname{rk}(F)<\operatorname{rk}(G)\).

*Proof.* (a) The first inclusion is clear. If \(e\in\operatorname{cl}(X)\) and \(X\subseteq Y\), then (1.2) gives \(\operatorname{rk}(\{e\}\mid Y)\leq\operatorname{rk}(\{e\}\mid X)=0\).

(b) If \(Z=\{z_1,\ldots,z_m\}\), then by (1.2) the increment \(\operatorname{rk}(\{z_i\}\mid X\cup\{z_1,\ldots,z_{i-1}\})\) is at most \(\operatorname{rk}(\{z_i\}\mid X)=0\); adding these zero increments gives \(\operatorname{rk}(X\cup Z)=\operatorname{rk}(X)\). Taking \(Z=\operatorname{cl}(X)\) gives the rank statement. If \(Z\subseteq\operatorname{cl}(X)\), then \(X\cup Z\) and \(X\) have the same rank and \(\operatorname{cl}(X)\subseteq\operatorname{cl}(X\cup Z)\) by (a); conversely, if \(e\in\operatorname{cl}(X\cup Z)\), then \(\operatorname{rk}(X\cup\{e\})\leq\operatorname{rk}(X\cup Z\cup\{e\})\), which equals \(\operatorname{rk}(X\cup Z)=\operatorname{rk}(X)\); so \(e\in\operatorname{cl}(X)\).

(c) By (b) with \(Z=\operatorname{cl}(X)\), \(\operatorname{cl}(\operatorname{cl}(X))=\operatorname{cl}(X)\). If \(F\supseteq X\) is a flat, then \(\operatorname{cl}(X)\subseteq\operatorname{cl}(F)=F\) by (a).

(d) If \(F,G\) are flats, \(\operatorname{cl}(F\cap G)\subseteq\operatorname{cl}(F)\cap\operatorname{cl}(G)=F\cap G\) by (a). If \(F\subsetneq G\) and \(e\in G\setminus F\), then \(e\notin\operatorname{cl}(F)\), so \(\operatorname{rk}(G)\geq\operatorname{rk}(F\cup\{e\})=\operatorname{rk}(F)+1\). \(\square\)

So the flats form a lattice: the meet of two flats is their intersection, and their join is \(\operatorname{cl}(F\cup G)\). Inside a closure or a rank we often write a union as a sum, as in \(\operatorname{cl}(F+Z)=\operatorname{cl}(F\cup Z)\). By (b), \(\operatorname{rk}(A\mid P)=\operatorname{rk}(A\mid\operatorname{cl}(P))\) for all \(A,P\).

**Lemma 1.4 (greedy over a base).** Let \(P,Z\subseteq E\). Scan the elements of \(Z\) in any order and accept an element exactly when it is not spanned by \(P\) together with the elements accepted before it. The accepted set \(A\) is independent over \(P\), \(Z\subseteq\operatorname{cl}(P\cup A)\), and \(|A|=\operatorname{rk}(Z\mid P)\).

*Proof.* Each accepted element raises the rank of \(P\) together with the accepted elements by one, so \(\operatorname{rk}(A\mid P)=|A|\). A rejected element is spanned by \(P\) and some of the accepted elements, hence by \(P\cup A\) (Lemma 1.3(a)). So \(Z\subseteq\operatorname{cl}(P\cup A)\), and by Lemma 1.3(b) \(\operatorname{rk}(Z\cup P)\leq\operatorname{rk}(P\cup A\cup Z)\), which equals \(\operatorname{rk}(P\cup A)\); with \(A\subseteq Z\) this gives \(\operatorname{rk}(Z\mid P)=|A|\). \(\square\)

In particular the outcome size does not depend on the scanning order. This is the basic reason why matroids suit online selection: if items of a set \(Z\) arrive in any order and each is accepted when it keeps independence over a fixed set \(P\), the final number of acceptances is \(\operatorname{rk}(Z\mid P)\).

## 2. Weighted optima and greedy

For a vector \(w=(w_e)_{e\in E}\) of nonnegative weights write \(w(X)=\sum_{e\in X}w_e\) and
\[
\mathrm{OPT}_M(w)=\max_{I\in\mathcal I}w(I).
\]
Fix once and for all a total order on \(E\), the *label order*. Given \(w\), the *priority order* ranks labels by decreasing weight, with ties broken by the label order. *Priority greedy* scans the labels of positive weight in priority order and accepts each one that is not spanned by the labels accepted before it.

**Lemma 2.1 (greedy is optimal).** The set \(I^*\) accepted by priority greedy is independent and \(w(I^*)=\mathrm{OPT}_M(w)\). A positive label \(e\) belongs to \(I^*\) exactly when it is not spanned by the labels of higher priority.

*Proof.* By Lemma 1.4 (with \(P=\varnothing\)) the accepted labels before \(e\) span all labels scanned before \(e\), which are the positive labels of higher priority; this proves the last sentence, and \(I^*\) is independent. For \(\lambda>0\) let \(E_\lambda=\{e:w_e\geq\lambda\}\). The labels of \(E_\lambda\) are scanned before all other labels, so by Lemma 1.4 the set \(I^*\cap E_\lambda\) spans \(E_\lambda\) and is independent: \(|I^*\cap E_\lambda|=\operatorname{rk}(E_\lambda)\). For every independent \(I\), \(|I\cap E_\lambda|\leq\operatorname{rk}(E_\lambda)\). Since \(w_e=\int_0^\infty\mathbf 1\{w_e\geq\lambda\}\,d\lambda\),
\[
\begin{aligned}
w(I)&=\int_0^\infty|I\cap E_\lambda|\,d\lambda\\
&\leq\int_0^\infty\operatorname{rk}(E_\lambda)\,d\lambda=w(I^*).\qquad\square
\end{aligned}
\]

## 3. Prophets with one sample

An *online selection rule* for a known matroid \(M\) receives the labels of \(E\) one at a time, in an order \(\pi\) that it is not told in advance. When a label \(e\) arrives, the rule observes \(e\) and its value \(V_e\) and decides immediately and irrevocably whether to accept \(e\); the accepted set must be independent after every arrival. The rule may use its own random *seed* \(\rho\), drawn before the arrivals.

In the *one-sample* model the values \(V_e\geq0\) are independent, \(V_e\) has a law \(D_e\) on \([0,\infty)\) that the rule does not know, and before the arrivals the rule receives a vector of samples \(S=(S_e)_{e\in E}\), where \(S_e\) has the same law \(D_e\) and all \(2|E|\) variables \(S_e,V_e\) are independent. The seed is independent of \((S,V)\).

The arrival order is chosen by an *almighty adversary*: \(\pi\) may be any measurable function of \(M\), the laws \(D_e\), the samples \(S\), the values \(V\) and the seed \(\rho\). In particular the adversary knows every random choice the rule will make, and can place each label where it hurts most.

**Theorem 3.1 (OpenAI, 2026).** There is a measurable online selection rule that does not depend on the laws \(D_e\) and has the following property. For every finite matroid \(M\), all laws \(D_e\) with \(\mathbb E[\mathrm{OPT}_M(V)]<\infty\), and every measurable adversary, the accepted set \(A\) satisfies
\[
\mathbb E\Bigl[\sum_{e\in A}V_e\Bigr]\geq2^{-293}\,\mathbb E\bigl[\mathrm{OPT}_M(V)\bigr].
\]

The constant does not depend on \(M\), its size or its rank, or on the laws. No bound on running time is claimed: the rule is a finite construction, but it maximizes over all flats of the matroid. Classical results put the theorem in context. For a single item with known distributions the best fraction is \(1/2\) (Krengel and Sucheston, crediting Garling), and Kleinberg and Weinberg proved the fraction \(1/2\) for all matroids with known distributions. Azar, Kleinberg and Weinberg introduced the model in which only samples are known and related it to secretary problems; Rubinstein, Wang and Weinberg found the optimal one-sample fraction \(1/2\) for a single item. For general matroids, Feldman, Svensson and Zenklusen obtained one-sample guarantees that decrease doubly logarithmically in the rank, and Fu, Lu, Tang, Wu, Wu and Zhang obtained a fraction close to \(1/4\) with a number of samples growing polylogarithmically in the size of the matroid, against an almighty adversary. For an arrival order fixed in advance, independently of the samples and the values, Abdi, Banihashem, Hajiaghayi and Mittal give a one-sample rule with fraction \(1/2\) for every matroid. Write \(V(A)=\sum_{e\in A}V_e\). A guarantee for every fixed order bounds \(\min_\pi\mathbb E[V(A)]\), the smallest expected reward over the orders. Against an almighty adversary the order may depend on the outcome, so the quantity to bound is \(\mathbb E[\min_\pi V(A)]\), the expected reward under the worst order for each outcome, which can be much smaller (Exercise 6.5 gives a rule for which the first is \(\frac12\) and the second is \(0\)). The theorem above bounds the second quantity with one sample, losing only a constant independent of the matroid.

## 4. A hidden fixed vector

The proof first removes the randomness of the values. In the *fixed-vector formulation* a vector \(w\in[0,\infty)^E\) is fixed but hidden from the rule. The rule draws its seed \(\rho\); as a function of \(\rho\) alone it chooses a *sacrificed set* \(\Xi(\rho)\subseteq E\). It learns \(w_e\) for all \(e\in\Xi(\rho)\) before the arrivals and must reject every label of \(\Xi(\rho)\); for every other label it learns \(w_e\) on arrival. Write \(A(w,\rho,\pi)\) for the accepted set under the order \(\pi\).

**Proposition 4.1.** There is a measurable rule in the fixed-vector formulation, whose seed takes finitely many values and which is feasible for every seed and every order, such that for every \(w\in[0,\infty)^E\)
\[
\begin{aligned}
&\mathbb E_\rho\Bigl[\min_\pi\,w\bigl(A(w,\rho,\pi)\bigr)\Bigr]\\
&\quad\geq2^{-293}\,\mathrm{OPT}_M(w).
\end{aligned}\tag{4.1}
\]

The minimum is *inside* the expectation: for every seed separately the worst order is taken. This is exactly what an adversary who knows the seed can enforce. Proposition 4.1 is proved at the end of the ninth lesson; this section shows that it implies Theorem 3.1.

**Lemma 4.2 (one-sample simulation).** A measurable fixed-vector rule whose seed takes finitely many values and which satisfies (4.1) yields a measurable one-sample rule satisfying the conclusion of Theorem 3.1.

*Proof.* Draw the seed \(\rho\) of the fixed-vector rule independently of \((S,V)\). Run the fixed-vector rule with the following data: for \(e\in\Xi(\rho)\) it is told \(S_e\) before the arrivals, and for \(e\notin\Xi(\rho)\) it is told \(V_e\) when \(e\) arrives. Unused samples are ignored, and labels of \(\Xi(\rho)\) are rejected without looking at their values. For the analysis define the *glued vector*
\[
w^{\mathrm g}_e=\begin{cases}S_e,&e\in\Xi(\rho),\\V_e,&e\notin\Xi(\rho).\end{cases}
\]
For every fixed seed the coordinates of \(w^{\mathrm g}\) are distinct variables among the independent \(S_e,V_e\), with laws \(D_e\); since \((S,V)\) is independent of \(\rho\), the vector \(w^{\mathrm g}\) is independent of \(\rho\) and has the law of \(V\).

For fixed \(S,V,\rho\) and every order \(\pi\), induction over the arrivals shows that the one-sample rule makes exactly the decisions of the fixed-vector rule on the hidden vector \(w^{\mathrm g}\): both see the same numbers at the same moments. So the accepted set is \(A(w^{\mathrm g},\rho,\pi)\), and every accepted label \(e\notin\Xi(\rho)\) has \(V_e=w^{\mathrm g}_e\). Whatever order the adversary chooses, possibly using all of \(S,V,\rho\), the reward satisfies
\[
\begin{aligned}
\sum_{e\in A}V_e&=w^{\mathrm g}\bigl(A(w^{\mathrm g},\rho,\pi)\bigr)\\
&\geq\min_{\pi'}w^{\mathrm g}\bigl(A(w^{\mathrm g},\rho,\pi')\bigr).
\end{aligned}
\]
Write \(g(v,\rho)=\min_{\pi'}v(A(v,\rho,\pi'))\) for \(v\in[0,\infty)^E\); for each seed value it is a measurable function of \(v\), a minimum over finitely many orders. Given the seed value \(\rho\), the glued vector has the law of \(V\). The seed takes finitely many values, so linearity of expectation gives
\[
\begin{aligned}
&\mathbb E\bigl[g(w^{\mathrm g},\rho)\bigr]\\
&\quad=\sum_{\rho_0}\Pr(\rho=\rho_0)\,\mathbb E\bigl[g(V,\rho_0)\bigr]\\
&\quad=\mathbb E\Bigl[\sum_{\rho_0}\Pr(\rho=\rho_0)\,g(V,\rho_0)\Bigr],
\end{aligned}
\]
and by (4.1), applied to each value of \(V\), the inner sum is at least \(2^{-293}\,\mathrm{OPT}_M(V)\). So the expected reward is at least \(2^{-293}\,\mathbb E[\mathrm{OPT}_M(V)]\). The reward is at most \(\mathrm{OPT}_M(V)\), which is integrable, so all expectations are finite. \(\square\)

The sacrificed set must be chosen from the seed alone. If it depended on the samples, the glued vector would no longer have the law of \(V\) (Exercise 6.4).

## 5. The plan

The rule of Proposition 4.1 chooses, with probability \(1/2\) each, between a simple *maximum rule*, good when one label carries a large part of the optimum, and a *main rule*. The main rule rounds weights to powers of \(B=2^{32}\), sacrifices several independent random masks, and builds from the revealed weights, before any arrival, increasing paths of flats indexed by an auxiliary time. Arriving labels are sorted into *layers*, differences of flats two steps apart, and accepted greedily within their layer; nesting of the flats makes the union independent for every order. The analysis shows that these layers keep enough rank among unrevealed valuable labels, for every order at once.

- The second lesson, [Rounding, a maximum rule and candidates](rounding-a-maximum-rule-and-candidates.md), defines the rounding, the maximum rule and the candidate labels.
- The third, [Density expansions and paths of flats](density-expansions-and-paths-of-flats.md), builds the paths.
- The fourth, [Layers and a rank bound for every order](layers-and-a-rank-bound-for-every-order.md), gives the online decisions, their feasibility, and a lower bound on acceptances valid for every order.
- The fifth, [Disjoint certificates](disjoint-certificates.md), proves a probabilistic counting lemma.
- The sixth, [Reverse exposure and safe samples](reverse-exposure-and-safe-samples.md), protects sampled labels against lighter competitors.
- The seventh, [Marked pivots and sign patterns](marked-pivots-and-sign-patterns.md), counts how insertions into a sequence can change the moments at which labels become spanned.
- The eighth, [From safe samples to unrevealed rank](from-safe-samples-to-unrevealed-rank.md), converts safe samples into rank outside the sacrificed masks.
- The ninth, [The final count and a secretary rule](the-final-count-and-a-secretary-rule.md), adds everything up and proves Proposition 4.1 and Theorem 3.1, together with a consequence for the secretary problem.

## 6. Exercises

**6.1.** Show that in the graphic matroid of a connected graph with \(n\) vertices, the rank of the whole edge set is \(n-1\), and describe the closure of a set of edges.

**6.2.** Show that \(\operatorname{rk}(A\mid P)=\operatorname{rk}(A\setminus\operatorname{cl}(P)\mid P)\) for all \(A,P\).

**6.3.** Let \(E=\{a,b,c\}\) and let the independent sets be \(\varnothing,\{a\},\{b\},\{c\},\{b,c\}\) (all subsets of \(\{b,c\}\), and \(\{a\}\)). Is this a matroid? With weights \(w_a=2\), \(w_b=w_c=1.5\), compare priority greedy with the optimum.

**6.4.** In Lemma 4.2, suppose the sacrificed set were \(\{e:S_e>1\}\) instead of a function of the seed. Show by an example with one label that the glued vector need not have the law of \(V\).

**6.5.** For two labels with weights \(w=(1,0)\) in the uniform matroid of rank one, consider the rule that, by a fair coin, accepts either the first or the second arriving label. Compute \(\min_\pi\mathbb E_\rho[w(A)]\) and \(\mathbb E_\rho[\min_\pi w(A)]\).

## 7. Solutions

**6.1.** A spanning tree has \(n-1\) edges and is a maximal forest, so the rank is \(n-1\). An edge \(e=uv\) is spanned by a set \(F\) of edges exactly when \(u\) and \(v\) lie in one connected component of the graph \((V,F)\) (adding \(e\) creates no new forest edge). So \(\operatorname{cl}(F)\) consists of \(F\) and all edges joining two vertices of one component of \(F\).

**6.2.** The elements of \(A\cap\operatorname{cl}(P)\) are spanned by \(P\), hence by \(P\cup(A\setminus\operatorname{cl}(P))\) (Lemma 1.3(a)); by Lemma 1.3(b) adjoining them changes no rank, so \(\operatorname{rk}(A\cup P)=\operatorname{rk}((A\setminus\operatorname{cl}(P))\cup P)\).

**6.3.** It is not a matroid: \(I=\{a\}\) and \(J=\{b,c\}\) violate augmentation, since neither \(\{a,b\}\) nor \(\{a,c\}\) is independent. Greedy, accepting a label whenever the accepted set stays independent, takes \(a\) (weight \(2\)) and then neither \(b\) nor \(c\), while \(\{b,c\}\) has weight \(3\). Lemma 2.1 needs the augmentation axiom through Lemma 1.4.

**6.4.** Let \(S,V\) be independent and uniform on \(\{0,2\}\). The glued value is \(S\) when \(S>1\), that is, \(2\), and \(V\) otherwise; so it equals \(2\) with probability \(\frac12+\frac12\cdot\frac12=\frac34\), not \(\frac12\).

**6.5.** For a fixed order, the label of weight \(1\) is in one of the two positions and is accepted with probability \(\frac12\); so \(\min_\pi\mathbb E_\rho[w(A)]=\frac12\). For each seed the adversary puts the label of weight \(0\) in the position that will be accepted, so \(\mathbb E_\rho[\min_\pi w(A)]=0\). The guarantee (4.1) is of the second, stronger kind.

## References

- [OpenAI-P] OpenAI, *One Sample Suffices for Matroid Prophet Inequalities against an Almighty Adversary*, OpenAI Math Release preprint, 23 September 2026, Sections 1 and 2. https://github.com/openai/math/tree/main/preprints/One-Sample-Suffices-for-Matroid-Prophet-Inequalities-against-an-Almighty-Adversary-September-23-2026
- [OpenAI-Lean] OpenAI Math Release, scope of the Lean formalization of the same paper. https://github.com/openai/math/blob/main/lean/docs/111.md
- [KW] R. Kleinberg and S. M. Weinberg, *Matroid prophet inequalities*, arXiv:1201.4764 (https://arxiv.org/abs/1201.4764).
- [AKW] P. D. Azar, R. Kleinberg and S. M. Weinberg, *Prophet inequalities with limited information*, arXiv:1307.3736 (https://arxiv.org/abs/1307.3736).
- [RWW] A. Rubinstein, J. Z. Wang and S. M. Weinberg, *Optimal single-choice prophet inequalities from samples*, arXiv:1911.07945 (https://arxiv.org/abs/1911.07945).
- [FSZ] M. Feldman, O. Svensson and R. Zenklusen, *A simple O(log log(rank))-competitive algorithm for the matroid secretary problem*, arXiv:1404.4473 (https://arxiv.org/abs/1404.4473).
- [ABHM] H. Abdi, K. Banihashem, M. Hajiaghayi and D. Mittal, *On the strong matroid secretary conjecture and beyond*, arXiv:2609.19118 (https://arxiv.org/abs/2609.19118).
- U. Krengel and L. Sucheston (1977), D. J. H. Garling, and H. Fu, P. Lu, Z. G. Tang, H. Wu, J. Wu and Q. Zhang (2024) are named for credit; the course does not use their results.
