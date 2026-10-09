# Infinite matroids and the packing/covering conjecture

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

A matroid abstracts linear independence. On an infinite ground set, the right axioms were found by Bruhn, Diestel, Kriesell, Pendavingh and Wollan [BDKPW]: besides the finite exchange property, independent sets must extend to maximal ones inside every subset. With these axioms, restriction, contraction and duality behave as for finite matroids. Bowler and Carmesin [BC] formulated an infinite version of the matroid packing/covering theorem and showed that it is equivalent to the infinite matroid intersection conjecture, a central open problem going back to Nash-Williams. This course proves:

**Theorem** (OpenAI 2026; Theorem 2.1 of [No independent covering](no-independent-covering.md)). In ZFC there are a countably infinite set \(E\) and two matroids \(M_0,M_1\) on \(E\), each equal to its own dual, such that \(E\) is not the union of an independent set of \(M_0\) and an independent set of \(M_1\). The pair \((M_0,M_1)\) has no packing/covering partition, so the infinite matroid packing/covering conjecture is false.

This lesson sets up the axioms and the conjecture, proves that direct sums are matroids, and reduces the theorem to the absence of an independent covering (Lemma 4.2). [Ideals, ultrafilters and an ordinal rank](ideals-ultrafilters-and-an-ordinal-rank.md) builds the set-theoretic tools, [Probes and local bases](probes-and-local-bases.md) and [Assembling a self-dual matroid](assembling-a-self-dual-matroid.md) construct a self-dual matroid \(Q\) on a countable set whose bases carry a strict ordinal inequality, and [No independent covering](no-independent-covering.md) places copies of \(Q\) along a doubly infinite path. The construction of \(Q\) uses ideas of Bowler and Geschke [BG], who built countable self-dual uniform matroids under additional set-theoretic hypotheses; here no hypothesis beyond ZFC is used.

## 1. The axioms

Let \(F\) be a set and \(\mathcal I\) a family of subsets of \(F\). A member of \(\mathcal I\) is *independent*; other subsets are *dependent*. Consider the conditions

- **(I1)** \(\varnothing\in\mathcal I\);
- **(I2)** every subset of an independent set is independent;
- **(I3)** if \(I\in\mathcal I\) is not maximal in \(\mathcal I\) and \(B\in\mathcal I\) is maximal, there is \(e\in B\setminus I\) with \(I\cup\{e\}\in\mathcal I\);
- **(IM)** for every \(I\in\mathcal I\) and every \(Y\) with \(I\subseteq Y\subseteq F\), the family \(\{J\in\mathcal I:I\subseteq J\subseteq Y\}\) has a maximal member (with respect to inclusion).

**Definition 1.1.** A **matroid** on \(F\) is a pair \(N=(F,\mathcal I)\) satisfying (I1)–(IM). Its **bases** are the maximal independent sets. For \(X\subseteq F\), the **closure** \(\operatorname{cl}_N(X)\) is \(X\) together with all \(e\in F\) for which some independent \(I\subseteq X\) has \(I\cup\{e\}\) dependent, and \(X\) is **spanning** if \(\operatorname{cl}_N(X)=F\).

By (IM) with \(I=\varnothing\) and \(Y=F\), a matroid has a basis. For finite \(F\), (IM) is automatic, and (I1)–(I3) are equivalent to the usual independence axioms of a finite matroid [BDKPW, Section 1].

**Lemma 1.2.** Let \(N\) be a matroid on \(F\) and \(X\subseteq Y\subseteq F\).

1. \(\operatorname{cl}_N(X)\subseteq\operatorname{cl}_N(Y)\).
2. A basis spans; hence every set containing a basis spans.
3. If \(B\) is a maximal independent subset of \(Y\), then \(Y\subseteq\operatorname{cl}_N(B)\).

*Proof.* (1) An independent witness inside \(X\) lies inside \(Y\). (2) If \(B\) is a basis and \(e\notin B\), then \(B\cup\{e\}\) is dependent, so \(e\in\operatorname{cl}_N(B)\); then use (1). (3) For \(e\in Y\setminus B\), \(B\cup\{e\}\) is dependent by maximality. \(\square\)

The converse of (2), that every spanning set contains a basis, holds for all matroids [BDKPW, Section 4], but it requires a further argument that we do not need: for the matroids of this course we prove it directly ([No independent covering](no-independent-covering.md), Lemma 1.1).

## 2. Restriction, duality and contraction

These operations are defined on set systems; we use them only to state the conjecture and in Section 4.

For \(X\subseteq F\), the **restriction** \(N\!\upharpoonright\!X\) is the family of independent sets of \(N\) contained in \(X\), a family on the ground set \(X\). Its maximal members, the maximal independent subsets of \(X\), exist by (IM).

The **dual** \(N^*\) of a family \(\mathcal I\) on \(F\) with at least one maximal member is the family of subsets of complements \(F\setminus B\) of maximal members \(B\) of \(\mathcal I\). Its maximal members are exactly these complements: a complement \(F\setminus B\) cannot be properly contained in another one \(F\setminus B'\), because then \(B'\subsetneq B\), contradicting maximality of \(B'\). For \(X\subseteq F\), the **contraction onto \(X\)** is
\[
N.X=(N^*\!\upharpoonright\!X)^* ,
\]
also written \(N/(F\setminus X)\). Bruhn et al. proved that restrictions, duals and contractions of matroids are matroids [BDKPW, Section 3]; this fact is not used in the proofs below.

**Definition 2.1.** A matroid \(N\) is **self-dual** if \(N^*=N\), that is, if the complement of every basis is a basis. Then \(N.X=(N\!\upharpoonright\!X)^*\) for every \(X\subseteq F\).

## 3. Direct sums

**Proposition 3.1** (Direct sums). Let \((N_j)_{j\in\Lambda}\) be matroids on pairwise disjoint sets \(F_j\), and put \(F=\bigcup_jF_j\). Declare \(I\subseteq F\) independent if \(I\cap F_j\) is independent in \(N_j\) for every \(j\). This is a matroid \(\bigoplus_jN_j\) on \(F\). Its bases are the unions \(\bigcup_jB_j\) of one basis \(B_j\) of each \(N_j\), and \(e\in F_j\) lies in \(\operatorname{cl}(X)\) exactly when \(e\in\operatorname{cl}_{N_j}(X\cap F_j)\). If every \(N_j\) is self-dual, so is the direct sum.

*Proof.* (I1) and (I2) hold componentwise. If some \(I\cap F_j\) is not a basis of \(N_j\), an element can be added in that component; if every \(I\cap F_j\) is a basis, adding \(e\in F_j\setminus I\) makes \(I\cap F_j\cup\{e\}\) dependent. So the bases are as stated. (I3): if \(I\) is not maximal, some \(I\cap F_j\) is not a basis of \(N_j\); for a basis \(B\) of the sum, \(B\cap F_j\) is a basis of \(N_j\), and (I3) in \(N_j\) gives \(e\in(B\cap F_j)\setminus I\) with \(I\cup\{e\}\) independent. (IM): given independent \(I\subseteq Y\), choose in each component a maximal independent \(J_j\) with \(I\cap F_j\subseteq J_j\subseteq Y\cap F_j\) (using the axiom of choice for the family of choices); then \(\bigcup_jJ_j\) is maximal among independent sets between \(I\) and \(Y\), since a larger one would be larger in some component. For \(e\in F_j\) and independent \(I\subseteq X\), the set \(I\cup\{e\}\) is dependent exactly when \((I\cap F_j)\cup\{e\}\) is dependent in \(N_j\), which gives the closure. Finally, the complement of \(\bigcup_jB_j\) is \(\bigcup_j(F_j\setminus B_j)\), a basis when each \(N_j\) is self-dual. \(\square\)

## 4. The conjecture and a reduction

**Definition 4.1** [BC]. Let \((N_i)_{i\in\Theta}\) be matroids on a common set \(F\). A **packing/covering partition** is a partition \(F=P\mathbin{\dot\cup}C\) together with sets \(S_i\subseteq P\) and \(I_i\subseteq C\) such that the \(S_i\) are pairwise disjoint, each \(S_i\) is spanning in \(N_i\!\upharpoonright\!P\), each \(I_i\) is independent in \(N_i.C\), and \(\bigcup_iI_i=C\). The **packing/covering conjecture** asserts that every family of matroids on a common set has a packing/covering partition.

For finite matroids this is a classical theorem, a consequence of the matroid union theorem. Bowler and Carmesin proved that, for two matroids \(M,N\), a packing/covering partition of \((M,N^*)\) exists exactly when \((M,N)\) satisfies the intersection property: there are a set \(J\) independent in both and a partition \(J=J_M\mathbin{\dot\cup}J_N\) with \(\operatorname{cl}_M(J_M)\cup\operatorname{cl}_N(J_N)=F\) [BC, Proposition 3.6]. Since the pair of the theorem consists of self-dual matroids, it therefore also refutes the infinite matroid intersection conjecture; we do not reprove their equivalence in this course.

**Lemma 4.2** (Self-dual reduction). Let \(N_0,N_1\) be self-dual matroids on \(F\) such that, for every \(X\subseteq F\), every set spanning \(N_i\!\upharpoonright\!X\) contains a maximal independent subset of \(X\), for \(i=0,1\). If \((N_0,N_1)\) has a packing/covering partition, then \(F=I_0'\cup I_1'\) with \(I_i'\) independent in \(N_i\).

*Proof.* Let \(F=P\mathbin{\dot\cup}C\), \(S_i\) and \(I_i\) be a packing/covering partition. By self-duality \(N_i.C=(N_i\!\upharpoonright\!C)^*\), so \(I_i\subseteq C\setminus B_i\) for a maximal independent subset \(B_i\) of \(C\). Put \(T_i=C\setminus I_i\supseteq B_i\). By Lemma 1.2(3), \(C\subseteq\operatorname{cl}_{N_i}(B_i)\subseteq\operatorname{cl}_{N_i}(T_i)\), and \(T_0\cap T_1=C\setminus(I_0\cup I_1)=\varnothing\). Also \(P\subseteq\operatorname{cl}_{N_i}(S_i)\): if \(e\in P\setminus S_i\), a witness in \(N_i\!\upharpoonright\!P\) is a witness in \(N_i\). So \(A_i=S_i\cup T_i\) spans \(N_i\), by Lemma 1.2(1), and \(A_0\cap A_1=\varnothing\). By hypothesis (with \(X=F\)) \(A_i\) contains a basis \(B_i'\) of \(N_i\). By self-duality \(F\setminus B_i'\) is a basis of \(N_i\), and \(I_i'=F\setminus A_i\subseteq F\setminus B_i'\) is independent. Finally \(I_0'\cup I_1'=F\setminus(A_0\cap A_1)=F\). \(\square\)

So it suffices to construct a self-dual pair with the spanning property and no covering of the ground set by an independent set of each.

## 5. Exercises

**5.1.** Let \(F\) be infinite and let \(\mathcal I\) consist of the finite subsets of \(F\). Show that (I1)–(I3) hold but (IM) fails.

**5.2.** Show that the family of all subsets of \(F\) of size at most \(k\) (a uniform matroid) is a matroid, and describe its dual for finite \(F\).

**5.3.** Let \(N\) be self-dual on a finite set \(F\). Show that \(|F|\) is even and every basis has \(|F|/2\) elements.

**5.4.** Show that in Lemma 4.2 the spanning hypothesis is used only for \(X=F\).

## 6. Solutions

**5.1.** (I1), (I2) are clear. There are no maximal finite subsets of an infinite set, so the hypothesis of (I3) never holds. (IM) fails for \(I=\varnothing\), \(Y=F\): the finite subsets of \(F\) have no maximal member.

**5.2.** (I1), (I2) are clear. A maximal member has \(\min(k,|F|)\) elements: exactly \(k\) if \(|F|\ge k\), and it is \(F\) otherwise. If \(I\) is not maximal, then \(|I|<k\) and \(I\ne F\), so a maximal \(B\) is not contained in \(I\), and any \(e\in B\setminus I\) can be added because \(|I\cup\{e\}|\le k\). For (IM), a maximal member between \(I\) and \(Y\) is any set of size \(\min(k,|Y|)\) between them. For finite \(F\) of size \(n\ge k\), the dual consists of the sets of size at most \(n-k\).

**5.3.** In a finite matroid all bases have the same size \(r\), and complements of bases are bases, so \(r=|F|-r\).

**5.4.** The proof applies the hypothesis only to \(A_i\), a spanning set of \(N_i\) itself; the restrictions to \(P\) and \(C\) are handled by Lemma 1.2.

## References

- [OpenAI-IM] OpenAI, *A counterexample to the infinite matroid packing/covering conjecture*, OpenAI Math Release preprint, 24 September 2026. https://github.com/openai/math/blob/main/preprints/A-Counterexample-to-the-Infinite-Matroid-Packing-Covering-Conjecture-September-24-2026/paper.pdf
- [BDKPW] H. Bruhn, R. Diestel, M. Kriesell, R. Pendavingh and P. Wollan, *Axioms for infinite matroids*, Advances in Mathematics 239 (2013). https://arxiv.org/abs/1003.3919
- [BC] N. Bowler and J. Carmesin, *Matroid intersection, base packing and base covering for infinite matroids*, Combinatorica 35 (2015). https://arxiv.org/abs/1202.3409
- [BG] N. Bowler and S. Geschke, *Self-dual uniform matroids on infinite sets*, Proceedings of the AMS 144 (2016); author version (6 October 2014) on the author's page. https://www.math.uni-hamburg.de/home/geschke/papers/UniformMatroid7.pdf
