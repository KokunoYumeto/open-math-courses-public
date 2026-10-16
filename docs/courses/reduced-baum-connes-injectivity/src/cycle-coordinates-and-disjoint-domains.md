# Cycle coordinates and disjoint domains

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Peeling has two consequences. The first is algebraic: every finite cycle of the Cayley graph is, uniquely, a sum of cycles of the sheets. The second is analytic: one can remove from every sheet an allowed set (a small ball around an old vertex, a private vertex, or nothing) so that the remaining *domains* of all sheets are pairwise disjoint and the Cayley edges not internal to any domain form a forest. The domains are where the operators of the analytic part act; the forest is the residue whose norm is small. Choosing all removed sets at once, for infinitely many sheets, is a compactness argument, made possible by the finite cycle coordinates [OpenAI-BCI, Sections 7.2-7.3, Lemma 7.3, Proposition 7.4, Lemma 7.5].

- Finite cycle coordinates (Section 1).
- Simultaneous disjoint domains (Section 2).
- Incidence coordinates (Section 3).

The setting of [Polygons through sheets and finite peeling](polygons-through-sheets-and-finite-peeling.md) is in force: the formal right Cayley graph \(\mathcal C\) of \(\Gamma\), whose positive edges \((g,\sigma):g\to g\sigma\) are separate cells, the family \(\mathcal Q\) of sheets with their intrinsic metrics and the types of their vertices, the allowed removed sets, the stars, and Lemmas 2.1 and 3.1 there.

## 1. Finite cycle coordinates

Chains are finite linear combinations of oriented edges over a commutative ring \(R\). The *cycle module* of a graph \(Y\) is \(Z_1(Y;R)\), the kernel of \(\partial:C_1(Y;R)\to C_0(Y;R)\). A forest has no nonzero cycle: the support of a cycle is a finite subforest, and the coefficient of an edge at a leaf of it must vanish, so repeated removal of leaves empties the support. Every cycle of a graph is a finite combination of *circuit chains* of simple closed paths: take a spanning forest of its finite support, and subtract, for each edge outside the forest, its coefficient times the circuit formed with the forest path between its endpoints; what remains is a cycle on a forest, hence zero. Loops and parallel edges are allowed in this argument.

**Lemma 1.1** (direct cycle coordinates; [OpenAI-BCI, Lemma 7.3]). For every commutative ring \(R\), the sum of the inclusions
\[
\begin{gathered}
\Phi_R:\bigoplus_{Q\in\mathcal Q}Z_1(Q;R)\\
\longrightarrow Z_1(\mathcal C;R),\\
(c_Q)_Q\longmapsto\sum_Qc_Q ,
\end{gathered}\tag{1.1}
\]
is an isomorphism. All chains have finite support, and the direct sum has finitely many nonzero coordinates.

*Proof.* *Onto.* Let a circuit of \(\mathcal C\) start at \(g\) and read the word \(w\). By the definition of \(\Gamma\), \(w\) is in the free group a finite product of conjugates of labels of closed walks of \(\widetilde X\) and their inverses. Follow this product from \(g\) in \(\mathcal C\): each conjugating stem is traversed once in each direction, so its chain cancels; each relator walk lies in a translated sheet; and a free cancellation of two inverse letters cancels the corresponding edge chains. So the circuit chain is a finite sum of sheet cycles, and by the circuit decomposition above \(\Phi_R\) is onto.

*Injective.* Suppose \(\sum_{j=1}^nc_{Q_j}=0\). Order the finitely many sheets involved by Lemma 3.1 of the previous lesson. An edge of \(Q_1\) with a nonzero coefficient in \(c_{Q_1}\) must occur in another coordinate, since the total coefficient is zero; both of its endpoints are then contacts with a later sheet, hence lie in \(R_1\). So \(c_{Q_1}\) is supported on \(\operatorname{Star}_{Q_1}(R_1)\), a forest by Lemma 2.1 of the previous lesson, and \(c_{Q_1}=0\). Remove this coordinate and repeat. \(\square\)

## 2. Simultaneous disjoint domains

**Proposition 2.1** (simultaneous disjoint domains; [OpenAI-BCI, Proposition 7.4]). There are sets \(R_Q\subseteq V(Q)\), one for each sheet, each empty, an old-centered ball \(B_Q(v)\), or a private singleton, such that the *domains* \(D_Q=V(Q)\setminus R_Q\) have the following properties.

1. The vertex sets \(D_Q\) are pairwise disjoint in \(\mathcal C\).
2. Let
\[
\begin{gathered}
E_{\rm int}=\bigcup_{Q\in\mathcal Q}\{e\in E(Q):\\
\text{both ends of }e\text{ lie in }D_Q\} .
\end{gathered}
\]
Every edge of \(E_{\rm int}\) belongs to a unique such sheet, and the graph \((V(\mathcal C),E(\mathcal C)\setminus E_{\rm int})\) is a forest.
3. \(\operatorname{Star}_Q(R_Q)\) is a forest. If \(R_Q\) contains an old vertex of layer \(i\), then \(|R_Q|\le2^{10H_i}\). A private singleton removes no old vertex.

No equivariance of the choice is asserted or needed.

*Proof.* *The allowed sets form a closed set.* For a sheet \(Q\), let \(\mathcal K_Q\) be the set of allowed removed sets, as elements of \(\{0,1\}^{V(Q)}\) with the product topology. A fixed vertex \(p\) lies in only finitely many allowed balls: if \(p\in B_Q(v)\), then
\[
\begin{aligned}
d_Q(p,v)&\le\kappa\,m_Q(v)\\
&\le\kappa\bigl(m_Q(p)+a\,d_Q(p,v)\bigr),\\
d_Q(p,v)&\le\frac{\kappa\,m_Q(p)}{1-\kappa a},
\end{aligned}
\]
and \(Q\) is locally finite; \(p\) lies in at most one private singleton. If a sequence of allowed sets converges pointwise to a nonempty limit containing \(p\), all late terms contain \(p\) and so belong to a finite collection; a constant subsequence shows that the limit is one of them. An empty limit is allowed. So \(\mathcal K_Q\) is closed, and compact.

*Finitary conditions.* All vertices, sheets, finite circuits and incidences are countable. Orient every finite circuit \(C\) of \(\mathcal C\), and fix by Lemma 1.1 a decomposition of its integral circuit chain
\[
\begin{gathered}
c_C=\sum_{Q\in\mathcal F_C}c_{C,Q},\\
|\mathcal F_C|<\infty .
\end{gathered}\tag{2.1}
\]
Impose the following countably many conditions on the removed sets:

- (a) for each vertex \(x\) and distinct sheets \(Q,Q'\) containing it, \(x\) does not lie in both \(D_Q\) and \(D_{Q'}\);
- (b) for each circuit \(C\), there are \(Q\in\mathcal F_C\) and an edge \(e\) of \(C\) and of \(Q\) whose both ends lie in \(D_Q\).

Each condition involves finitely many membership coordinates, so it is preserved under pointwise limits. In (b), both the list of edges and the list of candidate sheets are finite; replacing \(\mathcal F_C\) by all sheets would destroy this.

*Finite satisfiability.* Given finitely many conditions, take the finite family of all sheets appearing in the selected conditions of type (a) and in the sets \(\mathcal F_C\) of those of type (b). Peel it by Lemma 3.1 of the previous lesson, use its removed sets, and give every other sheet the empty set. The conditions (a) hold by (3.1) there. Suppose a selected condition (b) failed for \(C\). In (2.1), take the earliest peeled sheet with a nonzero coordinate. An edge of this coordinate with both ends outside its removed set cannot occur in any later coordinate, since its ends would then be contacts lying in the removed set. If it belonged to \(C\), it would witness the condition; so it lies outside \(C\), its coefficient in \(c_C\) is zero, and hence its coefficient in this coordinate is zero. So this coordinate is supported on the star of its removed set, a forest, and is zero, a contradiction. Repeating, all coordinates vanish, contradicting \(c_C\ne0\).

*The limit.* Enumerate the conditions and choose, for each \(n\), an assignment satisfying the first \(n\). Enumerate the countably many coordinates \((Q,v)\), and pass successively to subsequences on which the first coordinate, the second, and so on, are constant; the diagonal subsequence converges pointwise. Each limit lies in \(\mathcal K_Q\) by closedness, and every condition holds in the limit.

The conditions (a) make the domains disjoint. An edge internal to two domains would have an endpoint in their intersection, so its sheet is unique. A circuit in the residual graph would violate its condition (b), so the residual graph is a forest. The last assertions are Lemma 2.1 of the previous lesson. \(\square\)

## 3. Incidence coordinates

**Lemma 3.1** (incidence coordinates; [OpenAI-BCI, Lemma 7.5]). Sending a sheet incidence \((Q,u)\), \(u\in V(Q)\), to its vertex in \(\mathcal C\) and its base vertex in \(X\) is a bijection
\[
\begin{gathered}
\{(Q,u)\}_{Q\in\mathcal Q,\ u\in V(Q)}\\
\longrightarrow\Gamma\times V(X).
\end{gathered}\tag{3.1}
\]
In particular a vertex of \(\mathcal C\) occurs in at most
\[
\begin{aligned}
n^{\rm full}_i&=|\mathscr A_i|+|\mathscr B_i|\\
&=(1+2^{2r-s})2^{H_i}\\
&\le C_s2^{H_i}
\end{aligned}\tag{3.2}
\]
old incidences of layer \(i\).

*Proof.* Write the reference sheet as \(j(v,f)=ft_v\), \(f\in\mathsf H\), \(v\in V(X)\) (Proposition 5.1 of the lesson on the graphical group). A sheet is \(hQ_0\) for a coset \(h\mathsf H\), its stabilizer being a conjugate of \(\mathsf H\). Given a vertex \(u\in\Gamma\) and a base vertex \(v\), the equation \(u=hft_v\) determines the coset \(h\mathsf H=ut_v^{-1}\mathsf H\), and embeddedness determines the source vertex. This is the bijection; (3.2) counts the base vertices of layer \(i\). Private singleton removals add no old incidence. \(\square\)

## 4. Exercises

**Exercise 4.1.** Give an example of a graph with two subgraphs \(Q_1,Q_2\) whose union carries a cycle that is not a sum of cycles of \(Q_1\) and \(Q_2\), and explain which hypothesis of Lemma 1.1 fails there.

**Exercise 4.2.** Show that the condition (b) for all circuits implies that \(\mathcal C\) minus the internal edges has no circuit, and that a graph without circuits is a forest.

**Exercise 4.3.** Why is it essential, in the compactness argument, that a vertex lies in only finitely many allowed balls?

## 5. Solutions

**4.1.** Let \(Q_1\) and \(Q_2\) be two paths between the same two vertices, with no common edge. Their union is a cycle, but each \(Q_i\) is a tree with no cycles. In Lemma 1.1 the surjectivity uses that every circuit of \(\mathcal C\) is a product of conjugates of relators, each read in a sheet; in the example the union is not a product of cycles of the pieces.

**4.2.** A circuit \(C\) in the residual graph has no edge in \(E_{\rm int}\), but (b) provides an edge of \(C\) internal to the domain of some sheet. A finite connected graph without circuits is a tree, and a graph whose finite subgraphs are forests is a forest.

**4.3.** Closedness of \(\mathcal K_Q\) requires that a pointwise limit of allowed sets be allowed. If infinitely many balls contained a vertex, a limit of balls could be an infinite union not of the allowed form; local finiteness and the bound \(d_Q(p,v)\le\kappa m_Q(p)/(1-\kappa a)\) rule this out.

## References

- [OpenAI-BCI] OpenAI, *A torsion-free counterexample to reduced Baum–Connes injectivity*, OpenAI Math Release preprint, 23 September 2026, Sections 7.2-7.3, Lemma 7.3, Proposition 7.4, Lemma 7.5. https://github.com/openai/math/tree/main/preprints/A-Torsion-Free-Counterexample-to-Reduced-Baum-Connes-Injectivity-September-23-2026
