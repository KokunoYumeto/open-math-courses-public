# Scalar tests and the anchor obstruction

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson proves the theorem on blocks, with the tools of the lesson on signed measures. An operator of finite rank and norm at most \(p\) that is close to the identity at all anchors gives signed measures \(\mu_x\) on a finite set \(S\) of states. For every oriented edge \(e\colon x\to y\) of a suitable graph we build a real function \(f_e\) with Lipschitz constant at most \(1\) that agrees with the bump \(b_x\) on most of \(S\) as seen from \(x\), and with \(-b_y\) on most of \(S\) as seen from \(y\). Integrating \(f_e\) against \(\mu_x-\mu_y\) gives a number of at least about \(\tfrac32L\), minus a loss on the states that were given up. The norm of the operator bounds the same number by \(2p\). On average over all edges the loss is small, and \(\tfrac32L=15p\) is larger than \(2p\). This is the contradiction.

- Extension of real Lipschitz functions from a finite set (Lemma 1.1).
- The test function of an edge (Lemma 2.1).
- The lower and the upper bound (Lemmas 3.1 and 3.2).
- The average over all incidences (Lemma 4.1).
- Proof of the theorem on blocks (Section 5), and an overview of the course (Section 6).

The lesson follows [OpenAI-LF, Section 6]. It uses the setting, the facts (G1), (G2) and (N), Lemmas 2.1, 3.1, 3.2 and 6.1 and Proposition 5.1 of [Signed measures and matched walks](signed-measures-and-matched-walks.md), and Proposition 5.1 of [Colored graphs with a tree limit](colored-graphs-with-a-tree-limit.md).

## 1. Extension of real Lipschitz functions

**Lemma 1.1.** Let \((M,d)\) be a metric space, \(L>0\), \(P\subseteq M\) a finite nonempty set, and \(v\) a function from \(P\) to \([-L,L]\) with \(|v(j)-v(j')|\le d(j,j')\) for all \(j,j'\in P\). Put
\[
\begin{aligned}
F(z)&=\min_{j\in P}\bigl(v(j)+d(z,j)\bigr),\\
f(z)&=\max\bigl\{-L,\ \min\{L,\ F(z)\}\bigr\} .
\end{aligned}
\]
Then \(f\) maps \(M\) to \([-L,L]\), \(|f(z)-f(z')|\le d(z,z')\) for all \(z,z'\), and \(f=v\) on \(P\).

**Proof.** For \(z\in P\) the term \(j=z\) gives \(F(z)\le v(z)\), and every term satisfies \(v(j)+d(z,j)\ge v(z)\) by the assumption; so \(F(z)=v(z)\). For \(z,z'\in M\) and every \(j\), \(v(j)+d(z,j)\le v(j)+d(z',j)+d(z,z')\); taking the minimum over \(j\) gives \(F(z)\le F(z')+d(z,z')\), and the same with \(z\) and \(z'\) exchanged. Cutting off the values at \(L\) and at \(-L\) does not increase differences and does not change values in \([-L,L]\). \(\blacksquare\)

## 2. The test function of an edge

We keep the setting of the lesson on signed measures: the integer \(p\), the block \(M_p\), a finite set \(S\subseteq M_p\) of states with \(o\in S\), an integer \(n\ge2\), and one graph \(G=G_m\) with its good and bad vertices. For an incidence \(e\colon x\to y\) of \(G\), the set \(E_e\subseteq S\) consists of the states at which \(e\) is exceptional for \(x\), and \(E_{\bar e}\) of the states at which the reverse incidence \(\bar e\colon y\to x\) is exceptional for \(y\). The bumps are \(b_x\) and \(b_y\).

**Lemma 2.1** (edge tests). For every incidence \(e\colon x\to y\) of \(G\) there is a function \(f_e\) from \(M_p\) to \([-L,L]\) with \(|f_e(z)-f_e(z')|\le d_p(z,z')\) for all \(z,z'\) such that
\[
\begin{aligned}
f_e(j)&=b_x(j)&&\text{for }j\in S\setminus E_e,\\
f_e(j')&=-b_y(j')&&\text{for }j'\in S\setminus E_{\bar e}.
\end{aligned}
\]

**Proof.** We show that the required values are consistent and satisfy the Lipschitz inequality with the constant \(1\) on the set \(P=(S\setminus E_e)\cup(S\setminus E_{\bar e})\). Then Lemma 1.1 gives \(f_e\); if \(P\) is empty, take \(f_e=0\).

For two states of \(S\setminus E_e\) the inequality holds because \(b_x\) has a Lipschitz constant of at most \(1\) (Lemma 3.1 of the lesson on signed measures); likewise for two states of \(S\setminus E_{\bar e}\) and \(-b_y\). Let \(j\in S\setminus E_e\) and \(j'\in S\setminus E_{\bar e}\). The two required values, \(b_x(j)\) and \(-b_y(j')\), differ by \(b_x(j)+b_y(j')\), which is at most \(2L\). If \(d_p(j,j')\ge2L\), the inequality holds. Let \(d_p(j,j')<2L\); we show that \(b_x(j)=0\) and \(b_y(j')=0\).

Suppose \(b_x(j)>0\). Then \(\|h(x)-h(j)\|_\infty<K\), so \(x\) and \(j\) are compatible. The ends \(x,y\) of a source edge have a distance of at most \(1\), so by (G2)
\[
\begin{aligned}
\|h(y)-h(j')\|_\infty&\le\|h(y)-h(x)\|_\infty\\
&\quad+\|h(x)-h(j)\|_\infty\\
&\quad+\|h(j)-h(j')\|_\infty\\
&<1+K+2L .
\end{aligned}
\]
So \(y\) and \(j'\) are compatible, and \(d_p(j,j')\le2L\). By Lemma 6.1 of the lesson on signed measures, \(j\in E_e\) or \(j'\in E_{\bar e}\). This contradicts the choice of \(j\) and \(j'\). So \(b_x(j)=0\). The same argument with the roles of the two ends exchanged gives \(b_y(j')=0\).

So for \(d_p(j,j')<2L\) both required values are \(0\), and the inequality holds. The case \(j=j'\) shows that the two requirements agree at a state that lies in both sets. \(\blacksquare\)

The lemma is the place where the exceptional directions are used: where \(b_x\) and \(-b_y\) would be required at nearby states with nonzero values, one of the two states has been given up.

## 3. Two bounds for an edge

Now let \(T\) be a bounded linear operator on \(\mathcal F(M_p)\) with range in the span of the \(\delta_j\), \(j\in S\), with \(\|T\|\le2p\) and \(\|T\delta_a-\delta_a\|<1\) for all anchors \(a\), and let \(\mu_x\), \(x\in M_p\), be its measures (Lemma 3.2 of the lesson on signed measures): signed measures on \(S\) of total mass \(1\) with \(\|\mu_x\|_{\mathrm{TV}}\le V\) and \(\int b_x\,d\mu_x\ge\tfrac34L\) for source vertices.

**Lemma 3.1** (lower bound). For every incidence \(e\colon x\to y\) of \(G\),
\[
\begin{aligned}
&\int f_e\,d(\mu_x-\mu_y)\\
&\qquad\ge\frac{3L}2-2L\,\bigl(|\mu_x|(E_e)+|\mu_y|(E_{\bar e})\bigr) .
\end{aligned}
\]

**Proof.** The function \(f_e-b_x\) is \(0\) on \(S\setminus E_e\), and \(|f_e-b_x|\le2L\) everywhere. So
\[
\begin{aligned}
\int f_e\,d\mu_x&=\int b_x\,d\mu_x+\int(f_e-b_x)\,d\mu_x\\
&\ge\tfrac34L-2L\,|\mu_x|(E_e) .
\end{aligned}
\]
The function \(f_e+b_y\) is \(0\) on \(S\setminus E_{\bar e}\) and at most \(2L\) in absolute value. So
\[
\begin{aligned}
-\int f_e\,d\mu_y&=\int b_y\,d\mu_y\\
&\quad-\int(f_e+b_y)\,d\mu_y\\
&\ge\tfrac34L-2L\,|\mu_y|(E_{\bar e}) .
\end{aligned}
\]
Add the two inequalities. \(\blacksquare\)

The signs of the measures play no role: the errors are bounded with the total variation on the sets that were given up.

**Lemma 3.2** (upper bound). For every incidence \(e\colon x\to y\) of \(G\),
\[
\Bigl|\int f_e\,d(\mu_x-\mu_y)\Bigr|\le2p .
\]

**Proof.** By property (1) of the lemma on the measures, applied to \(x\) and to \(y\),
\[
\begin{aligned}
&\int f_e\,d(\mu_x-\mu_y)\\
&\qquad=\bigl(T(\delta_x-\delta_y)\bigr)\bigl(f_e-f_e(o)\bigr) .
\end{aligned}
\]
The function \(f_e-f_e(o)\) lies in \(\operatorname{Lip}_0(M_p)\) with a norm of at most \(1\), and \(\|T(\delta_x-\delta_y)\|\le2p\,d_p(x,y)\le2p\) by (G1). \(\blacksquare\)

## 4. The average over all incidences

Let \(\mathcal I\) be the set of all incidences of \(G\). The graph is \(\Delta\)-regular, so \(|\mathcal I|=\Delta\,|G|\), where \(|G|\) is the number of vertices. Let \(\beta\) be the fraction of bad vertices.

**Lemma 4.1.** With sums over all incidences \(e\colon x\to y\) of \(G\),
\[
\begin{aligned}
\frac1{|\mathcal I|}\sum_e|\mu_x|(E_e)&\le\frac V\Delta+V\beta,\\
\frac1{|\mathcal I|}\sum_e|\mu_y|(E_{\bar e})&\le\frac V\Delta+V\beta .
\end{aligned}
\]

**Proof.** Group the incidences by their initial vertex \(x\). If \(x\) is good, every state lies in at most one of the sets \(E_e\), \(e\in\mathcal D(x)\). So
\[
\sum_{e\in\mathcal D(x)}|\mu_x|(E_e)\le\|\mu_x\|_{\mathrm{TV}}\le V .
\]
If \(x\) is bad, each of the \(\Delta\) terms is at most \(V\). There are at most \(|G|\) good and \(\beta|G|\) bad vertices. So the first sum is at most \(V|G|+\Delta V\beta|G|\); divide by \(\Delta|G|\).

The map \(e\mapsto\bar e\) is a bijection of \(\mathcal I\), and the term \(|\mu_y|(E_{\bar e})\) for \(e\colon x\to y\) is the term of the first sum for the incidence \(\bar e\colon y\to x\). So the two sums are equal. \(\blacksquare\)

## 5. Proof of the theorem on blocks

**Theorem 5.1** ([OpenAI-LF, Section 1]). Let \(p\ge1\) be an integer and let \((M_p,d_p,o)\) and \(A_p\) be the block and its set of anchors. Every bounded linear operator \(T_0\) of finite rank on \(\mathcal F(M_p)\) with \(\|T_0\|\le p\) satisfies
\[
\max_{a\in A_p}\|T_0\delta_a-\delta_a\|\ge\tfrac12 .
\]

**Proof.** Suppose \(T_0\) has finite rank, \(\|T_0\|\le p\) and \(\|T_0\delta_a-\delta_a\|<\tfrac12\) for all \(a\in A_p\).

*Step 1.* By the lemma on a common finite support there are a finite set \(S\ni o\) and an operator \(T\) with range in the span of the \(\delta_j\), \(j\in S\), with \(\|T\|\le2p\) and \(\|T\delta_a-\delta_a\|<1\) for all anchors. Let \(\mu_x\) be its measures.

*Step 2.* With this set \(S\) of states, the proposition on rare matched walks gives \(n\ge2\) and \(m\) such that the fraction \(\beta\) of bad vertices of \(G=G_m\) is less than \(1/(20V)\). Define the sets \(E_e\) and the functions \(f_e\) for this graph.

*Step 3.* Average the inequality of Lemma 3.1 over all incidences of \(G\). By Lemma 4.1 and (N), each of the two averages of the losses is at most
\[
\frac V\Delta+V\beta<\frac1{20}+\frac1{20}=\frac1{10} .
\]
So
\[
\begin{aligned}
&\frac1{|\mathcal I|}\sum_e\int f_e\,d(\mu_x-\mu_y)\\
&\qquad>\frac{3L}2-2L\cdot\frac2{10}=\frac{11L}{10}=11p .
\end{aligned}
\]
By Lemma 3.2 every term of the average is at most \(2p\). So \(2p>11p\), which is false. \(\blacksquare\)

Together with the properties of the block (Proposition 5.1 of the lesson on colored graphs: countably infinite, distances at least \(1\), diameter at most \(B_p\), finitely many anchors, one of them the base point), this is the theorem on blocks stated in the first lesson.

**The order of the choices.** The integer \(p\) determines the numbers \(L,R,K,D,B,V\), then \(\Delta\), \(Q\), \(H\) and \(k\), then the sequence of graphs, the block and its anchors. All of this is fixed before an operator is considered. An operator \(T_0\) then determines the support \(S\). Only after that the length \(n\) and the graph \(G_m\) are chosen, depending on \(S\). The set \(S\) may be related to the graphs in any way; the proof needs no independence between the operator and the graphs. This is possible because the statement about the tree limit holds for every fixed property of colored balls.

## 6. Overview of the course

The course proves, with no result from outside the programme:

- For every \(p\) the block \(M_p\) is a bounded countable metric space with distances at least \(1\) whose free space, a renorming of \(\ell_1\), has \(2B_p\)-BAP and does not have \(p\)-BAP (Theorem 5.1 here, with the proposition on coefficients of the first lesson).
- The real space \(\ell_1\) has equivalent norms without the metric approximation property, and for every \(p\) an equivalent norm without \(p\)-BAP (the corollary on new norms in the first lesson).
- The wedge \(M\) of the blocks is a countable metric space with distances at least \(1\) whose free space has the approximation property and not the bounded approximation property (the lesson on the wedge).

It derives from one named hypothesis, a theorem of Kalton on nets in approximable Banach spaces: the free space of the wedge is not approximable by equi-uniformly continuous maps with relatively compact ranges.

The ingredients of the obstruction are, in the order of the proof: a bounded metric with finitely many anchors, so that an operator that is good at the anchors is controlled at every point; labels that are \(1\)-Lipschitz and bumps of small slope, which turn this control into a statement about measures; many colors, so that a state can follow only few vertices; a large degree, so that giving up one direction per state costs little; and graphs whose small balls look like a tree with independent colors, so that long followed walks are rare.

## 7. Exercises

**7.1.** In Lemma 1.1, show that \(F(z)\ge-L\) for all \(z\), so that only the cut at \(L\) is needed. Show that \(F'(z)=\max_{j\in P}(v(j)-d(z,j))\) is another extension of \(v\) with Lipschitz constant at most \(1\), and that \(F'\le F\).

**7.2.** Where in the proof of Theorem 5.1 are the conditions \(\Delta>20V\) and \(k>2\Delta QH\) used?

**7.3.** Let \(e\colon x\to y\) be an incidence of \(G\). (a) Show that every state \(j\) with \(b_x(j)>0\) lies in \(E_e\) or in \(E_{\bar e}\). (b) Conclude that \(|\mu_x|(E_e\cup E_{\bar e})\ge\tfrac34\) for the measures of Section 3.

**7.4.** (a) Show that Theorem 5.1 holds with \(1\) in place of \(\tfrac12\). (b) Show more: every operator \(T_0\) of finite rank on \(\mathcal F(M_p)\) with \(\|T_0\|\le p\) has \(\|T_0\delta_a-\delta_a\|\ge150p^2+7p\) for some anchor \(a\).

**7.5.** Let \(S_m\) be the operators of finite rank from the proof of the proposition on coefficients in the first lesson, for the space \(M_p\). Show that \(\|S_m\|>p\) for all large \(m\).

## 8. Solutions

**7.1.** \(F(z)\ge\min_jv(j)\ge-L\). For \(z\in P\): \(F'(z)\ge v(z)\) by the term \(j=z\), and \(v(j)-d(z,j)\le v(z)\) for all \(j\). The Lipschitz inequality for \(F'\) follows as for \(F\). For all \(j,j'\): \(v(j)-v(j')\le d(j,j')\le d(j,z)+d(z,j')\), so \(v(j)-d(z,j)\le v(j')+d(z,j')\); hence \(F'\le F\).

**7.2.** \(\Delta>20V\) gives \(V/\Delta<\tfrac1{20}\) in Step 3: the loss from the at most one exceptional direction per state at good vertices. \(k>2\Delta QH\) gives \(\Delta QH/k<\tfrac12\) in the proposition on rare matched walks, which makes the fraction \(\beta\) of bad vertices less than \(1/(20V)\) in Step 2.

**7.3.** (a) If \(b_x(j)>0\), then \(\|h(x)-h(j)\|_\infty<K\), so \(x\) and \(j\) are compatible, and \(\|h(y)-h(j)\|_\infty<K+1\), so \(y\) and \(j\) are compatible. Lemma 6.1 of the lesson on signed measures with \(j'=j\) gives \(j\in E_e\) or \(j\in E_{\bar e}\). (b) By (a) the function \(b_x\) vanishes on the states outside \(E_e\cup E_{\bar e}\), and \(b_x\le L\). So \(\tfrac34L\le\int b_x\,d\mu_x\le L\,|\mu_x|(E_e\cup E_{\bar e})\). So the states that are given up carry a large part of the measure. The proof works because the part in \(E_e\) alone is small on average, and only this part is lost for \(\mu_x\).

**7.4.** (a) Let \(\theta=\max_a\|T_0\delta_a-\delta_a\|<1\). In the proof of the lemma on a common finite support choose \(\eta<\min\{p,(1-\theta)/B\}\). Then \(\|T\delta_a-\delta_a\|\le\theta+\eta B<1\) and \(\|T\|<2p\), and the rest of the proof is unchanged.

(b) Let \(\epsilon\ge0\) and let \(T\) have range in the span of the \(\delta_j\), \(j\in S\), with \(\|T\|\le2p\) and \(\|T\delta_a-\delta_a\|\le\epsilon\) for all anchors. The total variation bound \(V\) does not depend on \(\epsilon\). In the proof of property (3) of the lemma on the measures, \(\|T\delta_x-\delta_{a(x)}\|\le2pR+\epsilon\), so \(\int b_x\,d\mu_x\ge L-\frac LK(2pR+\epsilon)\). The average in Step 3 is then larger than
\[
2L-\frac{2L}K\,(2pR+\epsilon)-\frac{4L}{10} ,
\]
and it is at most \(2p=L/5\). This is a contradiction as soon as \(\frac2K(2pR+\epsilon)\le\frac75\), that is, \(60p^2+\epsilon\le\frac7{10}K=210p^2+7p\), that is, \(\epsilon\le150p^2+7p\). Now let \(T_0\) have finite rank, \(\|T_0\|\le p\), and \(\theta=\max_a\|T_0\delta_a-\delta_a\|<150p^2+7p\). Choose \(\eta<p\) with \(\theta+\eta B\le150p^2+7p\) in the lemma on a common finite support; the operator \(T\) contradicts what was just shown.

**7.5.** Every \(\delta_a\) is an evaluation combination, so \(S_m\delta_a=\delta_a\) for all anchors once \(E_m\) contains the finitely many anchors other than \(o\). Such an \(S_m\) has finite rank and no error at the anchors; by Theorem 5.1 its norm is larger than \(p\).

## References

- [OpenAI-LF] OpenAI, *A uniformly discrete counterexample to bounded approximation in Lipschitz-free spaces*, OpenAI Math Release preprint, 26 September 2026, Section 6. https://github.com/openai/math/tree/main/preprints/Failure-of-Bounded-Approximation-in-a-Lipschitz-Free-Space-over-a-Uniformly-Discrete-Metric-Space-September-26-2026
