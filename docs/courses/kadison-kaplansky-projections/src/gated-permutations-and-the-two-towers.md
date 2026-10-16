# Gated permutations and the two towers

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson defines the edges of the tower. An edge between \(A_i\) and \(B_k\) is a solution of two equations of padded streams, which tie the evaluation at a slot on each side to the input stream on the other side, transformed by a *triangular permutation*. The permutations are chosen at one block only, the last active block of each pair, and only there do they mix bits; this is what will make the incidence between neighbouring layers expanding. Two versions of the rule are needed: in the *gated* tower \(Y^\#\) one family-wide rule recovers long paths from their labels, and in the *auxiliary* tower \(Y^0\) the last permutation of each pair acts unconditionally, which makes its choice a family of independent uniform matchings [OpenAI-KK, Section 4.3 and Lemma 4.2].

- Labels (Section 1).
- Triangular rules (Section 2).
- The edge equations (Section 3).
- The two towers and the alphabet (Section 4).
- Independent matching clusters (Section 5).

The notation of [Streams, slots and slot evaluations](streams-slots-and-slot-evaluations.md) is in force: layers \(A_i,B_i\), stream lengths \(l_A,l_B\), blocks and the interleaved order (2.1), adjacent pairs \((i,k)\) with \(\alpha,\beta,p,p'\), slots, families and the slot evaluations \(Q=v+\mathcal Ku\) with the coefficients and spills of Lemma 6.1 there.

## 1. Labels

A *positive label* is a triple \((\varphi,j,x)\) of a family \(\varphi\), a serial number \(1\le j\le d\) and a vector \(x\in\mathbb F_2^p\), where \(p\) is the number attached to \(\varphi\). Write \(x=b\Vert x'\) with \(b\) of length \(p-p'\) and \(x'\) of length \(p'\). An edge from \(A_i\) to \(B_k\) with positive label \((\varphi,j,x)\) attaches to the slot \(a=(k-i,j)\) at its \(A\)-end and to the slot \(c=(i-k,j,b)\) at its \(B\)-end. Traversed from \(B_k\) to \(A_i\), it carries the formal inverse label \((\varphi,j,x)^{-1}\).

## 2. Triangular rules

For each label we define two maps of padded streams: \(\mathcal F\), acting on \(B\)-streams, and \(\mathcal J\), acting on \(A\)-streams. Both act block by block. The rule at a block may depend on the label and on the *keys* of that block: all input blocks, of both sides, strictly earlier in the interleaved order. No rule depends on its own block or a later one through its keys.

**Marked blocks.** For each adjacent pair \((i,k)\) of a family, its *marked block* is its last active block in the interleaved order, with its number \(t\) of active coordinates (Lemma 2.2 of the previous lesson). At the marked block, a *table* assigns to each label of the family and each tuple of keys a permutation of \(\mathbb F_2^t\); it acts on the first \(t\) coordinates of the block and leaves the others unchanged. A marked \(B\)-block contributes to \(\mathcal F\), a marked \(A\)-block to \(\mathcal J\). At all other blocks the rule is the identity.

**The gate.** At a marked block the four immediately preceding blocks of the interleaved order are full blocks of length \(s\). The *gate* of the marked block is *open* if these four input blocks are not all zero, and *closed* otherwise. In the *gated rule*, the permutation of a marked block is applied only when its gate is open.

**Lemma 2.1** (properties of the gated rule). Fix a family and tables at all its marked blocks.

1. At most one marked block of the family occupies a given position of the interleaved order, and a finite prefix uses finitely many tables.
2. On the padded streams of a pair \((i,k)\) of the family, the gates of all marked blocks after its own are closed, when the rule is applied and when it is inverted. So the rule and its inverse preserve the active lengths \(l_A(i)\) and \(l_B(k)\).
3. The rule is invertible block by block: given the output and the already recovered earlier blocks, each input block is recovered.

*Proof.* (1) Marked blocks of different pairs of a family are at least \(32\) positions apart, and every prefix meets finitely many. (2) The first marked block after that of \((i,k)\) lies at least \(32\) positions later, so the four blocks before it lie beyond the cutoff of \((i,k)\), where the padded inputs vanish; its gate is closed and it acts as the identity, and inductively the same holds at every later marked block. When the rule is inverted on a stream that vanishes beyond the cutoff, the unmarked blocks beyond it are recovered as zeros, so the next marked block again sees four zero blocks before it, and induction applies. At its own marked block the permutation changes only the \(t\) active coordinates. (3) The gate and the key of a block are determined by earlier blocks, so the permutation used at the block is known before the block is inverted. \(\square\)

## 3. The edge equations

For an adjacent pair \((i,k)\), a vertex \((u_A,v_A)\in A_i\) with slot \(a\) and a vertex \((u_B,v_B)\in B_k\) with slot \(c\) are joined by an edge with label \((\varphi,j,x)\) when
\[
\begin{gathered}
Q_A=x\Vert\mathcal F(u_B),\\
Q_B=x'\Vert\mathcal J(u_A),
\end{gathered}\tag{3.1}
\]
equations of padded streams, where \(Q_A=v_A+\mathcal K_au_A\), \(Q_B=v_B+\mathcal K_cu_B\), and \(\mathcal F,\mathcal J\) are the rules of the label \((\varphi,j,x)\).

**Lengths.** The active lengths of the evaluations are
\[
\begin{aligned}
|v_A|&=r+1+l_B(i)\\
&=p+l_B(k),\\
|v_B|&=s-r+1+l_A(k)\\
&=p'+l_A(i),
\end{aligned}\tag{3.2}
\]
which are the lengths of the right sides of (3.1). The output of \(\mathcal K_a\) on \(u_A\) ends, including the last spill, at most at position \(|v_A|\): in form (B) of the cutoff the last \(A\)-block is full and the output ends by \(r+ns+\alpha\le|v_A|=r+\alpha+ns+t\); in form (A) it ends by \(r+(n+1)s+\alpha=|v_A|\). In the same way the output of \(\mathcal K_c\) on \(u_B\) ends by \((n+1)s+\beta\le|v_B|\).

**Lemma 3.1** (one edge per slot). For every vertex of \(A_i\) and every slot \(a\) of the pair \((i,k)\) there is exactly one solution of (3.1), that is, one vertex of \(B_k\), one slot \(c\) and one label. The same holds from the side of \(B_k\), and the two constructions are inverse to each other.

*Proof.* From \((u_A,v_A)\) and \(a=(k-i,j)\): compute \(Q_A\); its first \(p\) coordinates are \(x\), which contains the bucket \(b\) and so the slot \(c=(i-k,j,b)\). The remaining coordinates of \(Q_A\) equal \(\mathcal F(u_B)\); invert \(\mathcal F\) block by block (Lemma 2.1(3)), the keys on side \(A\) being the known blocks of \(u_A\). This gives \(u_B\), of active length \(l_B(k)\) by Lemma 2.1(2). Then the second equation gives \(Q_B\), and \(v_B=Q_B+\mathcal K_cu_B\), of active length \(|v_B|\) by (3.2). Conversely, from \((u_B,v_B)\) and \(c=(i-k,j,b)\): the first \(p'\) coordinates of \(Q_B\) give \(x'\), and \(x=b\Vert x'\); invert \(\mathcal J\) to obtain \(u_A\) from the remaining coordinates of \(Q_B\), then \(Q_A\) from the first equation and \(v_A=Q_A+\mathcal K_au_A\). Both constructions solve the same triangular equations with the same keys, so each undoes the other. \(\square\)

## 4. The two towers and the alphabet

**The gated tower \(Y^\#\).** Its vertices are those of all \(A_i,B_i\), and its edges are the solutions of (3.1) with the gated rule, for all adjacent pairs. Every slot carries exactly one edge, so the degrees are those of Lemma 3.1 of the previous lesson; parallel edges may occur and are counted as distinct slot incidences.

**The auxiliary tower \(Y^0\).** It has the same vertices. For the edges of a pair \((i,k)\), the rule differs from the gated rule only at the marked block of \((i,k)\) itself, where the permutation is applied unconditionally; at earlier marked blocks the gates are kept, and later marked blocks are inactive by Lemma 2.1(2). Lemma 3.1 holds for \(Y^0\) with the same proof, so \(Y^0\) has the same degrees and labels.

A labelled graph is *folded* if at every vertex each oriented label occurs on at most one outgoing edge.

**Lemma 4.1** (folding and the alphabet). \(Y^\#\) and \(Y^0\) are folded. The number \(m_\ell\) of positive labels satisfies
\[
\begin{gathered}
m_\ell\le27K^2d\,2^{r+2},\\
\log_2(2m_\ell)=11\ell+O(\log\ell) .
\end{gathered}
\]

*Proof.* At a vertex of \(A_i\), two distinct slots differ in the offset or in the serial number, so the labels of their edges differ in the family or in \(j\). At a vertex of \(B_k\), two distinct slots differ in the offset, the serial number or the bucket, which is part of \(x\). All labels leaving \(A\)-vertices are positive and all labels leaving \(B\)-vertices are formal inverses, so no further coincidences occur. There are at most \(27K^2\) families, \(d\) serial numbers and \(2^p\le2^{r+2}\) vectors \(x\). With \(K=320\ell\), \(d=2^{4\ell}\) and \(r=7\ell\) the logarithm is \(11\ell+O(\log\ell)\). \(\square\)

The tables are still to be chosen. They are chosen family by family, in increasing order of the marked blocks, in the next two lessons; a choice at the marked block of a pair does not change the edges of any earlier pair of the family, because on the padded inputs of an earlier pair that block is inactive.

## 5. Independent matching clusters

**Lemma 5.1** (matching clusters; [OpenAI-KK, Lemma 4.2]). Fix an adjacent pair \((i,k)\) and the tables at all earlier marked blocks of its family. Sample the table at the marked block of \((i,k)\) by choosing, for every label and every tuple of keys, an independent uniform permutation of \(\mathbb F_2^t\). Then the edges of the pair in \(Y^0\) are given by independent uniform perfect matchings between pairs of *clusters* of slot incidences, one pair of clusters for every label and tuple of keys, each cluster with \(2^t\) elements. Every edge between two matched clusters is possible, and different tuples have disjoint clusters.

*Proof.* Fix a slot \(a\) and a vector \(x\). The map \((u_A,v_A)\mapsto(u_A,Q_A)\) is a bijection, so the vertices of \(A_i\) whose evaluation at \(a\) begins with \(x\) are parametrized freely by \(u_A\), of length \(l_A(i)\), and the remaining coordinates of \(Q_A\), of length \(|v_A|-p=l_B(k)\). Likewise the vertices of \(B_k\) whose evaluation at the corresponding slot \(c\) begins with \(x'\) are parametrized freely by \(u_B\) and the remaining coordinates of \(Q_B\), of lengths \(l_B(k)\) and \(l_A(i)\).

Consider form (B) of the cutoff, in which the marked block is the \(B\)-block \(n+1\) with \(t\) active coordinates. Fix all blocks before it in the interleaved order: they comprise the whole of \(u_A\) and the first \(n\) blocks of \(u_B\). They determine the key tuple, the remaining coordinates of \(Q_B\) (through \(\mathcal J(u_A)\)), and all coordinates of \(Q_A\) except the last \(t\), which correspond to the marked block of \(\mathcal F(u_B)\). So the \(A\)-incidences with these data form a cluster parametrized by those last \(t\) coordinates of \(Q_A\), and the \(B\)-incidences a cluster parametrized by the last \(t\) coordinates of \(u_B\), each of size \(2^t\). The first equation of (3.1) says exactly that the edges match these clusters through the permutation of the table at this label and key tuple, applied unconditionally in \(Y^0\). The second equation then determines the remaining coordinate \(v_B\) and adds no condition. In form (A) the roles are exchanged: the last \(t\) coordinates of \(u_A\) are matched to the last \(t\) coordinates of \(Q_B\) through the table of \(\mathcal J\). Different labels or key tuples give disjoint clusters, and the permutations are independent and uniform. \(\square\)

## 6. Exercises

**6.1** (easy). Explain why a vertex of \(B_k\) can be the endpoint of two parallel edges to the same vertex of \(A_i\), and why these are counted twice in the degree.

**6.2** (easy). In Lemma 3.1, which blocks of \(u_A\) are needed as keys to invert the \(n\)-th block of \(\mathcal F\)?

**6.3** (medium). Suppose the gate were omitted, so that every marked block of a family always applies its permutation. Show that the rule of a later pair could then change the edges of an earlier pair, and explain which conclusion of Lemma 2.1 fails.

**6.4** (medium). Count the clusters of Lemma 5.1 in form (B): show that there are \(2^{p}\,2^{l_A(i)+ns}\) cluster pairs for each serial number, and that together they contain all \(d\,|A_i|\) slot incidences at \(A_i\) of the pair.

## 7. Solutions

**6.1.** The two slots at the \(B\)-vertex are different, but nothing prevents the two solutions of (3.1) from having the same \(A\)-endpoint, with different slots there. The degree counts slots, so both edges count.

**6.2.** The keys of \(B\)-block \(n\) are the blocks before it in the interleaved order: \(A\)-blocks \(0,\ldots,n-1\) and \(B\)-blocks \(1,\ldots,n-1\). So \(A\)-blocks \(0\) to \(n-1\) of \(u_A\) are needed.

**6.3.** On the padded inputs of an earlier pair, the coordinates of a later marked block are zero, but an ungated permutation can map the zero vector of \(\mathbb F_2^{t}\) to a nonzero one. Then \(\mathcal F(u_B)\) would have nonzero coordinates beyond the active length of \(Q_A\), and the equations of the earlier pair would change. Lemma 2.1(2) fails: the rule does not preserve active lengths.

**6.4.** For fixed \(j\), the data of a cluster on side \(A\) are \(x\in\mathbb F_2^p\), the stream \(u_A\) and the first \(ns\) coordinates of \(Q_A\) after \(x\), which correspond to the first \(n\) blocks of \(u_B\): \(l_A(i)+ns\) coordinates besides \(x\). This gives \(2^p2^{l_A(i)+ns}\) clusters of size \(2^t\). With \(l_B(k)=ns+t\), they contain \(2^p2^{l_A(i)+l_B(k)}=2^{|v_A|+l_A(i)}=|A_i|\) incidences, one for each vertex of \(A_i\), and the \(d\) serial numbers give \(d|A_i|\).

## References

- [OpenAI-KK] OpenAI, *A torsion-free counterexample to the Kadison–Kaplansky projection conjecture*, OpenAI Math Release preprint, 23 September 2026, Section 4.3 and Lemma 4.2. https://github.com/openai/math/tree/main/preprints/A-Torsion-Free-Counterexample-to-the-Kadison-Kaplansky-Projection-Conjecture-September-23-2026
