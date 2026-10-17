# Disjoint representatives in hypergraphs

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The cycle decomposition theorem of this course needs many short connecting paths at once, pairwise edge-disjoint, inside a graph that expands well. The next lesson, [Routing in graphs with cut expansion](routing-in-graphs-with-cut-expansion.md), finds them by encoding every admissible path as an edge of a hypergraph and choosing one edge for every connection request, with the chosen edges pairwise disjoint. This lesson proves the condition that makes such a choice possible. It is a version of Hall's marriage theorem for hypergraphs, due to Haxell (see [Ann] for its statement and an algorithmic treatment); the proof below is a self-contained alternating-tree argument.

## 1. Statement

A *hypergraph* on a finite ground set \(S\) is a finite family of nonempty subsets of \(S\), its *edges*. A *matching* is a set of pairwise disjoint edges. For hypergraphs \(\mathcal H_i\) on the same ground set we write \(\bigcup_{i\in I}\mathcal H_i\) for the hypergraph whose edges are the edges of some \(\mathcal H_i\) with \(i\in I\); an edge shared by several \(\mathcal H_i\) counts once.

Let \((\mathcal H_i)_{i\in J}\) be a family of hypergraphs on \(S\) indexed by a finite set \(J\). *Disjoint representatives* are edges \(E_i\in\mathcal H_i\), one for every \(i\in J\), that are pairwise disjoint.

**Theorem 1.1** (Haxell's condition). Let \(s\ge1\) be an integer and let \((\mathcal H_i)_{i\in J}\) be a finite family of hypergraphs on a finite set \(S\), all of whose edges have at most \(s\) elements. Suppose that for every nonempty \(I\subseteq J\) the hypergraph \(\bigcup_{i\in I}\mathcal H_i\) has a matching with more than
\[
(2s-1)(|I|-1)
\]
edges. Then \((\mathcal H_i)_{i\in J}\) has disjoint representatives.

For \(s=1\) all edges are single points and the condition says that the hypergraphs indexed by \(I\) contain at least \(|I|\) distinct points; this is Hall's condition (Exercise 5.1). Aharoni and Haxell proved the sharper sufficient condition with \(s(|I|-1)\) in place of \((2s-1)(|I|-1)\), by a topological argument; it is stated in [BM, Section 2]. This course does not use it: the applications have room for the factor \(2s-1\).

## 2. States and trees

We prove Theorem 1.1 by induction on \(|J|\). For \(J=\varnothing\) there is nothing to choose. Let \(|J|\ge1\), fix \(i_0\in J\) and put \(J_0=J\setminus\{i_0\}\). Every nonempty \(I\subseteq J_0\) is a nonempty subset of \(J\), so the family indexed by \(J_0\) satisfies the hypothesis, and by induction it has disjoint representatives \((E_i)_{i\in J_0}\). The task is to change some of them so that \(i_0\) can be served as well.

**Definition 2.1.** A *state* consists of disjoint representatives \((E_i)_{i\in J_0}\) of the family indexed by \(J_0\), and a finite sequence of pairs \((f_1,j_1),\dots,(f_k,j_k)\), where \(f_t\in\mathcal H_{j_t}\), with the following property. Define index sets
\[
\begin{gathered}
A_0=\{i_0\},\\
A_t=A_{t-1}\cup\{i\in J_0:E_i\cap f_t\ne\varnothing\} .
\end{gathered}
\]
Then, for every \(t\le k\):

- (T1) \(j_t\in A_{t-1}\);
- (T2) \(f_t\) is disjoint from \(f_1,\dots,f_{t-1}\) and from \(E_i\) for every \(i\in A_{t-1}\setminus\{i_0\}\);
- (T3) \(A_t\ne A_{t-1}\).

The sequence \(f_1,\dots,f_k\) is the *tree* of the state, and the numbers \(b_t=|A_t\setminus A_{t-1}|\ge1\) form its *signature* \((b_1,\dots,b_k)\).

The edge \(f_t\) belongs to a hypergraph whose index has already been reached, and it is *blocked* by the representatives \(E_i\) with \(i\in A_t\setminus A_{t-1}\). By (T2) these indices lie outside \(A_{t-1}\), and they join the tree. Since \(\sum_tb_t=|A_k|-1\le|J_0|\), a signature is a sequence of positive integers with sum at most \(|J_0|\); there are finitely many such sequences.

**Lemma 2.2** (size of a tree). For a state with tree \(f_1,\dots,f_k\), the set
\[
B=f_1\cup\dots\cup f_k\cup\bigcup_{i\in A_k\setminus\{i_0\}}E_i
\]
has at most \((2s-1)(|A_k|-1)\) elements.

*Proof.* By (T3), each step adds at least one index, so \(k\le|A_k|-1\), and the edges \(f_t\) contribute at most \(sk\le s(|A_k|-1)\) elements. An index \(i\in A_k\setminus\{i_0\}\) enters at some step \(t\), and then \(E_i\) meets \(f_t\); so \(E_i\) has at most \(s-1\) elements outside \(f_1\cup\dots\cup f_k\). These indices contribute at most \((s-1)(|A_k|-1)\) further elements. \(\square\)

## 3. Growing the tree and using a free edge

**Lemma 3.1** (one step). Given a state with tree \(f_1,\dots,f_k\) and the set \(B\) of Lemma 2.2, there is \(j\in A_k\) and an edge \(f\in\mathcal H_j\) disjoint from \(B\). If \(f\) meets some representative \(E_i\), then appending \((f,j)\) to the sequence gives a state.

*Proof.* By hypothesis \(\bigcup_{i\in A_k}\mathcal H_i\) has a matching with more than \((2s-1)(|A_k|-1)\ge|B|\) edges. The edges of a matching are disjoint, so each element of \(B\) lies in at most one of them, and some edge \(f\) of the matching avoids \(B\); it lies in some \(\mathcal H_j\) with \(j\in A_k\). If \(f\) meets \(E_i\), then \(i\notin A_k\setminus\{i_0\}\), because \(E_i\subseteq B\) for those indices; also \(i\ne i_0\) since \(i\in J_0\). So the new index set differs from \(A_k\), which is (T3). Properties (T1) and (T2) hold because \(j\in A_k\) and \(f\cap B=\varnothing\). \(\square\)

An edge \(f\in\mathcal H_j\) with \(j\in A_k\) is *free* for the state if it is disjoint from \(B\) and from every representative \(E_i\), \(i\in J_0\).

**Lemma 3.2** (using a free edge). Let a state with tree \(f_1,\dots,f_k\) and signature \((b_1,\dots,b_k)\) have a free edge \(f\in\mathcal H_j\), \(j\in A_k\). Then either the family indexed by \(J\) has disjoint representatives, or there is a state with signature \((b_1,\dots,b_{t-1},b_t-1)\) for some \(t\le k\) with \(b_t\ge2\).

*Proof.* If \(j=i_0\), the representatives \((E_i)_{i\in J_0}\) together with \(E_{i_0}=f\) are disjoint representatives for \(J\), because \(f\) meets no \(E_i\).

Let \(j\ne i_0\). Then \(j\) entered the index sets at a unique step \(t\le k\): \(j\in A_t\setminus A_{t-1}\). Replace \(E_j\) by \(f\). Call the new representatives \(E'_i\); they are disjoint representatives for \(J_0\), because \(f\in\mathcal H_j\) is disjoint from every other \(E_i\). Keep the pairs up to step \(t\) and discard the later ones. Let \(A'_u\) be the index sets of the shortened sequence computed with the representatives \(E'_i\).

For \(u<t\) we have \(A'_u=A_u\). Indeed \(E'_i=E_i\) for \(i\ne j\). Also \(E_j\) meets no \(f_u\) with \(u<t\), since otherwise \(j\in A_u\subseteq A_{t-1}\); and \(E'_j=f\) meets no \(f_u\), since \(f\) avoids \(B\). For the same reasons \(A'_t=A_t\setminus\{j\}\). Properties (T1) and (T2) for the steps \(u\le t\) involve only representatives with indices in \(A_{u-1}\setminus\{i_0\}\subseteq A_{t-1}\), which are unchanged, and (T3) holds for \(u<t\). At step \(t\), property (T3) holds exactly when \(A_t\setminus\{j\}\ne A_{t-1}\), that is, when \(b_t\ge2\).

If \(b_t\ge2\), the shortened sequence with the representatives \(E'_i\) is a state with signature \((b_1,\dots,b_{t-1},b_t-1)\).

If \(b_t=1\), consider the edge \(f_t\in\mathcal H_{j_t}\), where \(j_t\in A_{t-1}\) by (T1). It meets no \(E'_i\): for \(i\in A_{t-1}\setminus\{i_0\}\) by (T2), and among the other indices it met only \(E_j\), which has been replaced by \(f\), disjoint from \(f_t\). By (T2) it is also disjoint from \(f_1,\dots,f_{t-1}\). So, for the state formed by the representatives \(E'_i\) and the pairs up to step \(t-1\), the edge \(f_t\) is free, and its owner \(j_t\) lies in \(A'_{t-1}=A_{t-1}\). Repeat the argument with this state and this free edge. Each repetition shortens the sequence, so after finitely many repetitions either the owner is \(i_0\), and disjoint representatives for \(J\) exist, or a step \(t'\) with \(b_{t'}\ge2\) is reached. In the latter case the signature is \((b_1,\dots,b_{t'-1},b_{t'}-1)\) with \(t'\le t\le k\). \(\square\)

## 4. Proof of Theorem 1.1

Order finite sequences of positive integers as follows: append the symbol \(\infty\), larger than every integer, to both sequences and compare them lexicographically. This is a strict total order \(\prec\). Two of its properties are used:

- a proper extension is smaller: \((b_1,\dots,b_k,b_{k+1})\prec(b_1,\dots,b_k)\), because at position \(k+1\) the integer \(b_{k+1}\) is compared with \(\infty\);
- decreasing an entry and discarding the later ones gives a smaller sequence: \((b_1,\dots,b_{t-1},b_t-1)\prec(b_1,\dots,b_k)\) for \(t\le k\).

Start with the representatives \((E_i)_{i\in J_0}\) and the empty sequence; this is a state with the empty signature. Given a state, Lemma 3.1 produces an edge \(f\) avoiding \(B\). If \(f\) meets a representative, appending it gives a state with a smaller signature. Otherwise \(f\) is free, and Lemma 3.2 gives disjoint representatives for \(J\) or a state with a smaller signature. The signatures form a strictly decreasing sequence in the finite set of sequences of positive integers with sum at most \(|J_0|\), on which \(\prec\) is a strict total order. So the procedure cannot continue forever, and it ends with disjoint representatives for \(J\). \(\square\)

The proof is constructive: it is an augmenting-path search in which an augmenting step may stop part of the way along the tree. The signature records how many representatives block each edge of the tree, and every change either lengthens the tree or removes a blocking representative from one of its edges.

## 5. Exercises

**5.1** (easy). Show that for \(s=1\) the hypothesis of Theorem 1.1 is Hall's condition: the hypergraphs indexed by every nonempty \(I\) together contain at least \(|I|\) distinct points. Deduce Hall's marriage theorem.

**5.2** (easy). Let \(S=\{a,b,c,d\}\), \(\mathcal H_1=\{\{a,b\}\}\) and \(\mathcal H_2=\{\{a,c\},\{b,d\}\}\). Show that \(\mathcal H_1\cup\mathcal H_2\) has a matching with \(2=s(|J|-1)\) edges, where \(s=2\) and \(J=\{1,2\}\), but that there are no disjoint representatives. So the strict inequality in the sharper condition of Aharoni and Haxell cannot be relaxed to equality.

**5.3** (easy). Show that if disjoint representatives exist, then for every nonempty \(I\subseteq J\) the hypergraph \(\bigcup_{i\in I}\mathcal H_i\) has a matching with at least \(|I|\) edges. So the hypothesis of Theorem 1.1 differs from a necessary condition by the factor \(2s-1\) in front of \(|I|-1\).

**5.4** (medium). In the proof of Lemma 3.2 with \(b_t=1\), explain why the edge \(f_t\) cannot be reused with the representative \(E'_j=f\) to undo the replacement, and why the repetitions end.

## 6. Solutions

**5.1.** For \(s=1\) the edges are singletons \(\{v\}\), and a matching is a set of distinct singletons; so the largest matching of \(\bigcup_{i\in I}\mathcal H_i\) has as many edges as there are points in these hypergraphs together. "More than \(|I|-1\)" means at least \(|I|\). Hall's theorem: if each \(i\in J\) is given a set \(N_i\) of acceptable points and \(|\bigcup_{i\in I}N_i|\ge|I|\) for every nonempty \(I\), apply Theorem 1.1 to \(\mathcal H_i=\{\{v\}:v\in N_i\}\); disjoint representatives are distinct points \(v_i\in N_i\).

**5.2.** The edges \(\{a,c\}\) and \(\{b,d\}\) are disjoint, so the union has a matching with two edges, and none with three, since \(S\) has four points and every edge two. Disjoint representatives would use \(E_1=\{a,b\}\), which meets both edges of \(\mathcal H_2\).

**5.3.** The representatives \(E_i\), \(i\in I\), are pairwise disjoint edges of \(\bigcup_{i\in I}\mathcal H_i\), and there are \(|I|\) of them. Theorem 1.1 asks for more than \((2s-1)(|I|-1)\) edges; for \(s=1\) this is the necessary condition itself.

**5.4.** After the replacement, \(f_t\) meets no representative, so it is not blocked; it is used as a free edge for its own owner \(j_t\), which entered at an earlier step. Each repetition passes from step \(t\) to the step at which the owner entered, which is smaller than \(t\) by (T1); a strictly decreasing sequence of positive integers is finite.

## References

- [BM] M. Bucić and R. Montgomery, *Towards the Erdős–Gallai cycle decomposition conjecture*, Advances in Mathematics 437 (2024), 109434; arXiv:2211.07689. https://arxiv.org/abs/2211.07689
- [Ann] C. Annamalai, *Finding perfect matchings in bipartite hypergraphs*, arXiv:1509.07007 (2015, revised 2016). Haxell's condition and an algorithmic version of its proof. https://arxiv.org/abs/1509.07007
