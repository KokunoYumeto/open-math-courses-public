# Infinite matroids and the packing/covering conjecture

*Written by Claude Opus 5.5 (Anthropic), October 2026. General duality, restriction, contraction, spanning and intersection-equivalence proofs added by GPT-6 Astra (OpenAI), October 2026. The universal Packing and Covering equivalences were added by GPT-6 Astra (OpenAI), October 2026. Self-checked by the respective writing AIs. Public domain (CC0).*

A matroid abstracts linear independence. On an infinite ground set, the right axioms were found by Bruhn, Diestel, Kriesell, Pendavingh and Wollan [BDKPW]: besides the finite exchange property, independent sets must extend to maximal ones inside every subset. With these axioms, restriction, contraction and duality behave as for finite matroids. Bowler and Carmesin [BC] formulated an infinite version of the matroid packing/covering theorem and showed that it is equivalent to the infinite matroid intersection conjecture, a longstanding conjecture going back to Nash-Williams. This course proves:

**Theorem** (OpenAI 2026; Theorem 2.1 of [No independent covering](no-independent-covering.md)). In ZFC there are a countably infinite set \(E\) and two matroids \(M_0,M_1\) on \(E\), each equal to its own dual, such that \(E\) is not the union of an independent set of \(M_0\) and an independent set of \(M_1\). The pair \((M_0,M_1)\) has no packing/covering partition, so the infinite matroid packing/covering conjecture is false.

This lesson sets up the axioms and the conjecture, proves duality and the minor operations from the axioms, establishes the intersection and universal Packing/Covering equivalences, proves that direct sums are matroids, and reduces the theorem to the absence of an independent covering (Lemma 4.2). [Ideals, ultrafilters and an ordinal rank](ideals-ultrafilters-and-an-ordinal-rank.md) builds the set-theoretic tools, [Probes and local bases](probes-and-local-bases.md) and [Assembling a self-dual matroid](assembling-a-self-dual-matroid.md) construct a self-dual matroid \(Q\) on a countable set whose bases carry a strict ordinal inequality, and [No independent covering](no-independent-covering.md) places copies of \(Q\) along a doubly infinite path. The construction of \(Q\) uses ideas of Bowler and Geschke [BG], who built countable self-dual uniform matroids under additional set-theoretic hypotheses; here no hypothesis beyond ZFC is used.

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

Every spanning set contains a basis: Lemma 2.7 below proves this for all matroids from the independence axioms. The direct argument for the particular matroids of this course is retained in [No independent covering](no-independent-covering.md), Lemma 1.1.

## 2. Restriction, duality and contraction

We first define these operations on set systems, then prove that they give matroids. The proofs make the contraction and duality steps in Section 4 available without a finiteness assumption.

For \(X\subseteq F\), the **restriction** \(N\!\upharpoonright\!X\) is the family of independent sets of \(N\) contained in \(X\), a family on the ground set \(X\). Its maximal members, the maximal independent subsets of \(X\), exist by (IM).

The **dual** \(N^*\) of a family \(\mathcal I\) on \(F\) with at least one maximal member is the family of subsets of complements \(F\setminus B\) of maximal members \(B\) of \(\mathcal I\). Its maximal members are exactly these complements: a complement \(F\setminus B\) cannot be properly contained in another one \(F\setminus B'\), because then \(B'\subsetneq B\), contradicting maximality of \(B'\). For \(X\subseteq F\), the **contraction onto \(X\)** is
\[
N.X=(N^*\!\upharpoonright\!X)^* ,
\]
also written \(N/(F\setminus X)\). The following proofs establish the facts about these operations that Section 4 uses; compare [BDKPW, Section 3].

**Definition 2.1.** A matroid \(N\) is **self-dual** if \(N^*=N\), that is, if the complement of every basis is a basis. Then \(N.X=(N\!\upharpoonright\!X)^*\) for every \(X\subseteq F\).

### Completing independent sets without a finiteness assumption

All complements in the following arguments are taken in the displayed ground set \(F\). No step assumes finite rank, finite circuits or countability. The results supply the foundations of [BDKPW, Section 3] needed for Proposition 4.3.

**Lemma 2.2** (Controlled basis extension). If \(A\) is independent in \(N\) and \(D\) is a basis of \(N\), there is a basis \(H\) such that
\[
A\subseteq H\subseteq A\cup D.
\]

*Proof.* Apply (IM) inside \(A\cup D\), starting with \(A\), and call the resulting maximal independent set \(H\). If \(H\) were not a basis on \(F\), (I3) with the basis \(D\) would supply an element of \(D\setminus H\) that could be added. That would contradict the chosen maximality inside \(A\cup D\). Thus \(H\) is a basis on \(F\). \(\square\)

### Why the dual satisfies all four axioms

**Theorem 2.3** (Duality). The set system \(N^*\) is a matroid. Its bases are precisely the complements of the bases of \(N\), and \(N^{**}=N\).

*Proof.* A basis of \(N\) exists, so its complement contains the empty set; this proves (I1) for \(N^*\). Heredity proves (I2). The antichain argument preceding Definition 2.1 identifies the maximal dual-independent sets with the basis complements.

For (I3), let \(J\) be dual-independent but not a dual basis, and let \(F\setminus D\) be any dual basis. Choose a basis \(B\) disjoint from \(J\). Lemma 2.2 extends the independent set \(D\setminus J\) to a basis \(H\) satisfying
\[
D\setminus J\subseteq H\subseteq(D\setminus J)\cup B.
\]
Both sets on the right avoid \(J\). Hence \(J\subseteq F\setminus H\), and the inclusion is strict because \(J\) is not a dual basis. Choose \(e\in(F\setminus H)\setminus J\). The inclusion \(D\setminus J\subseteq H\) forces \(e\notin D\). Thus \(e\in(F\setminus D)\setminus J\), and \(J\cup\{e\}\) is dual-independent because it lies in \(F\setminus H\). This is exactly dual (I3).

For (IM), fix a dual-independent \(J\subseteq X\subseteq F\), and choose a basis \(B\) avoiding \(J\). By (IM) for \(N\), choose a maximal independent subset \(A\) of \(F\setminus X\). Complete it using Lemma 2.2 to a basis \(H\subseteq A\cup B\). Then \(H\) avoids \(J\), and
\[
H\setminus X=A,
\]
because a larger independent subset of \(F\setminus X\) would contradict the maximality of \(A\). Put \(K=X\setminus H\). It is dual-independent and contains \(J\).

Suppose a dual-independent \(L\) satisfies \(K\subsetneq L\subseteq X\). A basis \(D\) avoiding \(L\) would have
\[
D\cap X\subseteq X\setminus L\subsetneq H\cap X.
\]
Consequently \(T=(D\cap X)\cup A\) is a proper subset of the basis \(H\), so it is independent and not a basis. Apply (I3) to \(T\) and \(D\). It gives \(e\in D\setminus T\) with \(T\cup\{e\}\) independent. Every point of \(D\cap X\) already belongs to \(T\); therefore \(e\in(F\setminus X)\setminus A\). Heredity makes \(A\cup\{e\}\) independent, contradicting the choice of \(A\). This proves the required maximality of \(K\).

Finally the dual bases have just been proved to be exactly the basis complements. Taking complements twice gives the original bases. Every independent set extends to a basis by (IM), so a matroid's independent sets are exactly the subsets of its bases. The two set systems \(N^{**}\) and \(N\) therefore coincide. \(\square\)

### Restricting and contracting on specified ground sets

**Lemma 2.4** (Complementary maximality). For a basis \(B\) of \(N\) and \(X\subseteq F\), the following are equivalent:

1. \(B\cap X\) is maximal among independent subsets of \(X\).
2. \((F\setminus B)\cap(F\setminus X)\) is maximal among dual-independent subsets of \(F\setminus X\).

*Proof.* Assume (1). If (2) fails, enlarge the indicated dual-independent set inside \(F\setminus X\), and take a basis \(D\) disjoint from that larger set. Complementation within \(F\setminus X\) gives \(D\setminus X\subsetneq B\setminus X\). By Lemma 2.2 there is a basis \(H\) with
\[
B\cap X\subseteq H\subseteq(B\cap X)\cup D.
\]
Its outside part satisfies \(H\setminus X\subsetneq B\setminus X\). If its inside part equalled \(B\cap X\), then \(H\) would be a proper subset of the independent set \(B\), impossible for a basis. Hence \(H\cap X\) properly contains \(B\cap X\), contrary to (1). For the reverse direction, apply this already proved implication to the matroid \(N^*\), its basis \(F\setminus B\), and the subset \(F\setminus X\). Theorem 2.3 identifies the double dual with \(N\), and the two assertions exchange places. \(\square\)

**Theorem 2.5** (Restrictions and contractions). For every \(X\subseteq F\), both \(N\!\upharpoonright\!X\) and \(N.X\) are matroids on \(X\).

*Proof.* Restriction inherits (I1), (I2) and (IM) directly. To establish (I3), let \(I\subseteq X\) be independent and not maximal there, and let \(J\) be any maximal independent subset of \(X\). Extend \(J\) to a basis \(D\) on \(F\). Necessarily \(D\cap X=J\). Lemma 2.2 supplies a basis \(B\) with \(I\subseteq B\subseteq I\cup D\). Thus \(B\setminus X\subseteq D\setminus X\), so
\[
(F\setminus B)\cap(F\setminus X)
\supseteq(F\setminus D)\cap(F\setminus X).
\]
By Lemma 2.4 the right-hand set is maximal dual-independent inside \(F\setminus X\). The left-hand set is dual-independent, so equality holds and it too is maximal there. The reverse implication of Lemma 2.4 now makes \(B\cap X\) maximal independent inside \(X\). Since
\[
I\subseteq B\cap X\subseteq I\cup J
\]
and \(I\) is not maximal, some \(e\in J\setminus I\) belongs to \(B\cap X\). Its addition to \(I\) preserves independence. This proves restriction (I3). The definition \(N.X=(N^*\!\upharpoonright\!X)^*\), together with the restriction result and Theorem 2.3, proves the contraction assertion. \(\square\)

**Lemma 2.6** (Contraction and gluing independent sets). Fix \(X\subseteq F\).

1. A set \(I\subseteq X\) is a basis of \(N.X\) if and only if \(I\cup A\) is a basis of \(N\) for some basis \(A\) of \(N\!\upharpoonright\!(F\setminus X)\). In that case the same holds for every such basis \(A\).
2. A set \(J\subseteq X\) is independent in \(N.X\) if and only if \(J\cup A\) is independent in \(N\) for some basis \(A\) of \(N\!\upharpoonright\!(F\setminus X)\). If these conditions hold, \(J\cup K\) is independent in \(N\) for every independent \(K\subseteq F\setminus X\).

*Proof.* By definition of contraction, \(I\) is a contraction basis precisely when \(X\setminus I\) is a basis of \(N^*\!\upharpoonright\!X\). Extend \(X\setminus I\) to a dual basis \(F\setminus B\). Maximality inside \(X\) gives \(B\cap X=I\); Lemma 2.4 applied to the dual matroid gives that \(A=B\setminus X\) is a basis of the outside restriction. This proves one direction of the first equivalence. Conversely, if \(B=I\cup A\) is a basis with \(A\) maximal independent outside \(X\), Lemma 2.4 with \(F\setminus X\) makes \(X\setminus I\) a basis of the dual restriction. Thus \(I\) is a contraction basis.

To show independence from the choice of \(A\), let \(A'\) be another basis of the outside restriction. Complete \(A'\) to a basis \(H\) contained in \(A'\cup(I\cup A)\), using Lemma 2.2. Its outside part equals \(A'\) by maximality there, and \(H\cap X\subseteq I\). But
\[
X\setminus(H\cap X)\supseteq X\setminus I.
\]
The left-hand set is dual-independent as a subset of \(F\setminus H\); the right-hand set is maximal dual-independent inside \(X\). Equality follows. Hence \(H=I\cup A'\), proving the assertion for every outside basis.

For (2), first suppose \(J\) is contraction-independent. Extend it to a contraction basis \(I\), and extend any outside independent \(K\) to an outside basis \(A\), using Theorem 2.5 and (IM). Part (1) makes \(I\cup A\) a basis on \(F\); its subset \(J\cup K\) is independent. Conversely, if \(J\cup A\) is independent for an outside basis \(A\), extend their union to a basis \(B\) on \(F\). Maximality of \(A\) outside \(X\) implies \(B\setminus X=A\). Part (1) identifies \(B\cap X\) as a contraction basis, and this basis contains \(J\). \(\square\)

### Closure and complements of spanning sets

**Lemma 2.7** (Closure and bases). If \(B\) is a maximal independent subset of \(Y\subseteq F\), then
\[
\operatorname{cl}_N(B)=\operatorname{cl}_N(Y).
\]
Consequently a set spans \(N\) if and only if it contains a basis. Also, for \(S\subseteq X\subseteq F\),
\[
\operatorname{cl}_{N\upharpoonright X}(S)
=X\cap\operatorname{cl}_N(S).
\]

*Proof.* Monotonicity gives one closure inclusion, and Lemma 1.2 gives \(Y\subseteq\operatorname{cl}_N(B)\). Take \(e\in\operatorname{cl}_N(Y)\setminus Y\). There is an independent \(A\subseteq Y\) for which \(A\cup\{e\}\) is dependent. By (IM), extend \(A\) to a maximal independent subset \(D\) of \(Y\cup\{e\}\). It cannot contain \(e\), so \(D\subseteq Y\). If \(e\notin\operatorname{cl}_N(B)\), then \(B\cup\{e\}\) is independent, making \(B\) nonmaximal in the restriction to \(Y\cup\{e\}\). Theorem 2.5 permits (I3) in that restriction, with its basis \(D\). It yields an element of \(D\setminus B\) that can be added to \(B\), contrary to maximality inside \(Y\). This proves the other inclusion.

If \(S\) spans, choose a maximal independent subset \(B\) of \(S\). The equality just proved gives \(\operatorname{cl}_N(B)=F\). Were \(B\cup\{e\}\) independent for some \(e\notin B\), every subset \(A\subseteq B\) would also have \(A\cup\{e\}\) independent, contradicting the closure definition at \(e\). Hence \(B\) is a basis on \(F\). The converse is Lemma 1.2(2). Finally, the restriction identity follows directly because all the independent witnesses defining closure of \(S\) lie inside \(X\); their independence and dependence are unchanged by restriction. \(\square\)

**Corollary 2.8** (Spanning/independence duality). For \(S\subseteq F\), \(S\) spans \(N\) if and only if \(F\setminus S\) is independent in \(N^*\). In particular, for \(S,I\subseteq X\):

- \(S\) spans \(N\!\upharpoonright\!X\) if and only if \(X\setminus S\) is independent in \(N^*.X\).
- \(I\) is independent in \(N.X\) if and only if \(X\setminus I\) spans \(N^*\!\upharpoonright\!X\).

*Proof.* By Lemma 2.7, spanning means containing a basis \(B\). Complementation turns \(B\subseteq S\) into \(F\setminus S\subseteq F\setminus B\), exactly dual independence. The same implication backwards proves the equivalence. Apply it on ground set \(X\) to the restriction and to the dual restriction. The identities
\[
(N\!\upharpoonright\!X)^*=N^*.X,
\qquad (N.X)^*=N^*\!\upharpoonright\!X
\]
follow from the contraction definition and Theorem 2.3. \(\square\)

## 3. Direct sums

**Proposition 3.1** (Direct sums). Let \((N_j)_{j\in\Lambda}\) be matroids on pairwise disjoint sets \(F_j\), and put \(F=\bigcup_jF_j\). Declare \(I\subseteq F\) independent if \(I\cap F_j\) is independent in \(N_j\) for every \(j\). This is a matroid \(\bigoplus_jN_j\) on \(F\). Its bases are the unions \(\bigcup_jB_j\) of one basis \(B_j\) of each \(N_j\), and \(e\in F_j\) lies in \(\operatorname{cl}(X)\) exactly when \(e\in\operatorname{cl}_{N_j}(X\cap F_j)\). If every \(N_j\) is self-dual, so is the direct sum.

*Proof.* (I1) and (I2) hold componentwise. If some \(I\cap F_j\) is not a basis of \(N_j\), an element can be added in that component; if every \(I\cap F_j\) is a basis, adding \(e\in F_j\setminus I\) makes \(I\cap F_j\cup\{e\}\) dependent. So the bases are as stated. (I3): if \(I\) is not maximal, some \(I\cap F_j\) is not a basis of \(N_j\); for a basis \(B\) of the sum, \(B\cap F_j\) is a basis of \(N_j\), and (I3) in \(N_j\) gives \(e\in(B\cap F_j)\setminus I\) with \(I\cup\{e\}\) independent. (IM): given independent \(I\subseteq Y\), choose in each component a maximal independent \(J_j\) with \(I\cap F_j\subseteq J_j\subseteq Y\cap F_j\) (using the axiom of choice for the family of choices); then \(\bigcup_jJ_j\) is maximal among independent sets between \(I\) and \(Y\), since a larger one would be larger in some component. For \(e\in F_j\) and independent \(I\subseteq X\), the set \(I\cup\{e\}\) is dependent exactly when \((I\cap F_j)\cup\{e\}\) is dependent in \(N_j\), which gives the closure. Finally, the complement of \(\bigcup_jB_j\) is \(\bigcup_j(F_j\setminus B_j)\), a basis when each \(N_j\) is self-dual. \(\square\)

## 4. The conjecture and a reduction

**Definition 4.1** [BC]. Let \((N_i)_{i\in\Theta}\) be matroids on a common set \(F\). A **packing/covering partition** is a partition \(F=P\mathbin{\dot\cup}C\) together with sets \(S_i\subseteq P\) and \(I_i\subseteq C\) such that the \(S_i\) are pairwise disjoint, each \(S_i\) is spanning in \(N_i\!\upharpoonright\!P\), each \(I_i\) is independent in \(N_i.C\), and \(\bigcup_iI_i=C\). The **packing/covering conjecture** asserts that every family of matroids on a common set has a packing/covering partition.

For finite matroids this is a classical theorem, a consequence of the matroid union theorem. Bowler and Carmesin proved that, for two matroids \(M,N\), a packing/covering partition of \((M,N^*)\) exists exactly when \((M,N)\) satisfies the intersection property: there are a set \(J\) independent in both and a partition \(J=J_M\mathbin{\dot\cup}J_N\) with \(\operatorname{cl}_M(J_M)\cup\operatorname{cl}_N(J_N)=F\) [BC, Proposition 3.6]. Since the pair of the theorem consists of self-dual matroids, it therefore also refutes the infinite matroid intersection conjecture; Proposition 4.3 below supplies the equivalence with all the required minor and duality arguments.

**Lemma 4.2** (Self-dual reduction). Let \(N_0,N_1\) be self-dual matroids on \(F\) such that, for every \(X\subseteq F\), every set spanning \(N_i\!\upharpoonright\!X\) contains a maximal independent subset of \(X\), for \(i=0,1\). If \((N_0,N_1)\) has a packing/covering partition, then \(F=I_0'\cup I_1'\) with \(I_i'\) independent in \(N_i\).

*Proof.* Let \(F=P\mathbin{\dot\cup}C\), \(S_i\) and \(I_i\) be a packing/covering partition. By self-duality \(N_i.C=(N_i\!\upharpoonright\!C)^*\), so \(I_i\subseteq C\setminus B_i\) for a maximal independent subset \(B_i\) of \(C\). Put \(T_i=C\setminus I_i\supseteq B_i\). By Lemma 1.2(3), \(C\subseteq\operatorname{cl}_{N_i}(B_i)\subseteq\operatorname{cl}_{N_i}(T_i)\), and \(T_0\cap T_1=C\setminus(I_0\cup I_1)=\varnothing\). Also \(P\subseteq\operatorname{cl}_{N_i}(S_i)\): if \(e\in P\setminus S_i\), a witness in \(N_i\!\upharpoonright\!P\) is a witness in \(N_i\). So \(A_i=S_i\cup T_i\) spans \(N_i\), by Lemma 1.2(1), and \(A_0\cap A_1=\varnothing\). By hypothesis (with \(X=F\)) \(A_i\) contains a basis \(B_i'\) of \(N_i\). By self-duality \(F\setminus B_i'\) is a basis of \(N_i\), and \(I_i'=F\setminus A_i\subseteq F\setminus B_i'\) is independent. Finally \(I_0'\cup I_1'=F\setminus(A_0\cap A_1)=F\). \(\square\)

So it suffices to construct a self-dual pair with the spanning property and no covering of the ground set by an independent set of each.

### The general intersection equivalence

**Proposition 4.3** (Bowler–Carmesin). Let \(M,N\) be matroids on the same set \(F\), with no restriction on its cardinality. The following conditions are equivalent:

1. There are disjoint \(A,B\subseteq F\) such that \(A\cup B\) is independent in both matroids and
\[
\operatorname{cl}_M(A)\cup\operatorname{cl}_N(B)=F.
\]
2. The pair \((M,N^*)\) admits a packing/covering partition as in Definition 4.1.

The proof gives witnesses in both directions. This is [BC, Proposition 3.6], with its duality and minor prerequisites supplied by Theorems 2.3–2.5 and Lemma 2.6 rather than assumed.

*Proof, from a packing/covering partition to intersection.* Write \(F=P\mathbin{\dot\cup}C\). Let \(S_M,S_D\subseteq P\) be the disjoint spanning sets for \(M\!\upharpoonright\!P,N^*\!\upharpoonright\!P\), respectively. Let \(I_M,I_D\subseteq C\) cover \(C\) and be independent in \(M.C,N^*.C\), respectively. The packing sets need not cover \(P\), and the covering sets need not be disjoint.

Choose a maximal \(M\)-independent subset \(A\) of \(S_M\). Lemma 2.7 shows that it has the same closure as \(S_M\), so it spans \(P\) and is a basis of \(M\!\upharpoonright\!P\). Put
\[
T=C\setminus I_D.
\]
The covering condition implies \(T\subseteq I_M\). Corollary 2.8, applied to \(N^*\), says that \(T\) spans \(N\!\upharpoonright\!C\). Choose a maximal \(N\)-independent subset \(B\) of \(T\). Again Lemma 2.7 makes \(B\) span \(C\), and \(B\subseteq I_M\) is independent in \(M.C\).

Now verify both required independences on the full ground set. In \(M\), the set \(A\) is independent on \(P\) and \(B\) is independent after contracting onto \(C\); Lemma 2.6(2) gives that \(A\cup B\) is independent. In \(N\), the set \(S_D\) spans the dual restriction on \(P\); Corollary 2.8 gives that \(P\setminus S_D\) is independent in \(N.P\). Disjointness of the packing sets places \(A\) inside \(P\setminus S_D\). Thus \(A\) is independent in \(N.P\), whereas \(B\) is independent in \(N\!\upharpoonright\!C\). Lemma 2.6(2) gives independence of their union in \(N\) as well. Finally \(A\cap B=\varnothing\), since they lie on opposite sides, and their closures cover \(P\cup C=F\).

*Proof, from intersection to a packing/covering partition.* Suppose \(A,B\) satisfy (1). Use the explicit partition
\[
P=\operatorname{cl}_M(A)\setminus B,
\qquad C=F\setminus P.
\]
It has \(A\subseteq P\subseteq\operatorname{cl}_M(A)\), because \(A\cap B=\varnothing\). Also \(B\subseteq C\). Any point of \(C\setminus B\) lies outside \(\operatorname{cl}_M(A)\), and hence in \(\operatorname{cl}_N(B)\) by (1). Therefore \(C\subseteq\operatorname{cl}_N(B)\). Lemma 2.7's restriction identity shows that \(A\) spans \(M\!\upharpoonright\!P\) and \(B\) spans \(N\!\upharpoonright\!C\). They are independent, so each is a basis of its respective restriction: an independent spanning set cannot admit an independent one-element extension, by the closure definition.

For the packing side, take
\[
S_M=A,\qquad S_D=P\setminus A.
\]
The set \(A\cup B\) is \(N\)-independent, and \(B\) is a basis of the outside restriction on \(C\). Lemma 2.6(2) therefore makes \(A\) independent in \(N.P\). Corollary 2.8 says exactly that \(P\setminus A\) spans \(N^*\!\upharpoonright\!P\). Thus these two disjoint sets are the required packing.

For the covering side, take
\[
I_M=B,\qquad I_D=C\setminus B.
\]
Since \(A\) is a basis on \(P\) and \(A\cup B\) is \(M\)-independent, Lemma 2.6(2) gives independence of \(B\) in \(M.C\). Since \(B\) spans \(N\!\upharpoonright\!C\), Corollary 2.8 gives independence of \(C\setminus B\) in \(N^*.C\). The two sets cover \(C\), completing the construction. All the arguments allow empty packing or covering sides. \(\square\)

For the self-dual pair constructed later, \(M_1^*=M_1\); hence Theorem 2.1 of [No independent covering](no-independent-covering.md) and Proposition 4.3 give the claimed failure of intersection. Lemma 4.2 remains a separate direct route to the packing/covering counterexample, and the course's special spanning proofs remain valid alternatives to Lemma 2.7.

### Closure and minor facts used by the universal equivalences

The following arguments use arbitrary sets and arbitrary set-indexed families. In particular, we will not take unions of independent sets at limit stages: that would not be justified for the matroids under discussion.

**Lemma 4.4** (Closure and change of ground set). Let \(L\) be a matroid on \(F\).

1. Closure is idempotent: \(\operatorname{cl}_L(\operatorname{cl}_L(S))=\operatorname{cl}_L(S)\).
2. If \(X\subseteq Y\subseteq F\), every set independent in \(L.X\) is independent in \(L.Y\).
3. If \(F=P\mathbin{\dot\cup}C\) and \(Y\subseteq C\), then, as matroids on \(Y\),
\[
(L.C)\!\upharpoonright\!Y
=(L\!\upharpoonright\!(P\cup Y)).Y.
\]
4. In the situation of (3), suppose \(S\subseteq P\) spans \(L\!\upharpoonright\!P\) and \(T\subseteq Y\) spans \((L.C)\!\upharpoonright\!Y\). Then \(S\cup T\) spans \(L\!\upharpoonright\!(P\cup Y)\).

*Proof.* Choose a maximal independent \(B\subseteq S\). Lemma 2.7 gives \(\operatorname{cl}_L(B)=\operatorname{cl}_L(S)\). No point of this closure outside \(B\) can be added independently to \(B\): an independent extension would make all the witnesses in the closure definition independent. Thus \(B\) is a maximal independent subset of \(\operatorname{cl}_L(S)\). Apply Lemma 2.7 to that subset to prove (1).

For (2), choose a basis \(A\) of the restriction to \(F\setminus Y\), and extend it to a basis \(D\) of the restriction to \(F\setminus X\). If \(J\) is independent in \(L.X\), Lemma 2.6 makes \(J\cup D\) independent in \(L\), so its subset \(J\cup A\) is independent. The converse part of that lemma makes \(J\) independent in \(L.Y\).

For (3), fix a basis \(A\) of \(L\!\upharpoonright\!P\). For every \(J\subseteq Y\), Lemma 2.6 says that \(J\) is independent in the left-hand matroid precisely when \(J\cup A\) is independent in \(L\). Applying the same lemma within \(L\!\upharpoonright\!(P\cup Y)\) gives exactly the same test for the right-hand matroid. Equality of the independent-set families proves the identity, with ground set \(Y\) on both sides.

For (4), take a basis \(A\) of the restriction to \(P\) contained in \(S\), and a basis \(D\) of the restriction of \(L.C\) to \(Y\) contained in \(T\). These exist by Lemma 2.7. Parts (3) and Lemma 2.6 show that \(A\cup D\) is a basis of \(L\!\upharpoonright\!(P\cup Y)\). Since this basis lies in \(S\cup T\), the latter set spans. \(\square\)

### A packing part that contains every possible packing part

For a family \(\mathcal M=(M_i)_{i\in K}\) on \(F\), a *wave* consists of a subset \(P\subseteq F\) and a packing of the restrictions to \(P\). Thus its witnesses \((S_i)_{i\in K}\) are disjoint subsets of \(P\), each spanning the corresponding restriction. The support of this wave is \(P\). A family is *loose* when the only support of a wave is the empty set. We need maximality of the support, not an assumption that the witnesses are independent.

**Lemma 4.5** (Greatest wave support). There is a wave whose support \(P\) contains the support of every wave. For this \(P\), the family \((M_i.(F\setminus P))_{i\in K}\) is loose.

*Proof.* The collection of waves is a set: supports and witnesses can be encoded by subsets of \(F\) and \(F\times K\). It is nonempty, since the empty support with empty witnesses is a wave. In ZFC, well-order this collection as
\[
\bigl(P_\alpha,(S_{i,\alpha})_{i\in K}\bigr)_{\alpha<\lambda}.
\]
Put \(P=\bigcup_{\alpha<\lambda}P_\alpha\). For each stage define its new part and its retained witnesses by
\[
\begin{aligned}
D_\alpha&=P_\alpha\setminus\bigcup_{\beta<\alpha}P_\beta,\\
T_i&=\bigcup_{\alpha<\lambda}(D_\alpha\cap S_{i,\alpha}).
\end{aligned}
\]
The \(D_\alpha\) are disjoint; within each of them the original witnesses are disjoint. Consequently the sets \(T_i\) are pairwise disjoint subsets of \(P\).

Fix \(i\). Transfinite induction proves \(P_\alpha\subseteq\operatorname{cl}_{M_i}(T_i)\) for every \(\alpha\). Indeed, a point of \(S_{i,\alpha}\) either is new, in which case it belongs to \(T_i\), or lies in an earlier \(P_\beta\), in which case the induction hypothesis places it in that closure. Hence \(S_{i,\alpha}\subseteq\operatorname{cl}_{M_i}(T_i)\). Spanning of \(P_\alpha\), monotonicity and Lemma 4.4(1) give the desired inclusion. This argument applies at successor and limit stages alike; no union is claimed to be independent. The restriction closure identity of Lemma 2.7 now shows that every \(T_i\) spans the restriction to \(P\). Thus \((P,(T_i))\) is a wave, and its support contains every wave support by construction.

Let \(C=F\setminus P\). If the contracted family on \(C\) had a wave with nonempty support \(Y\), let its disjoint spanning witnesses be \(U_i\subseteq Y\). Lemma 4.4(4) makes \(T_i\cup U_i\) span the restriction of \(M_i\) to \(P\cup Y\). These unions remain pairwise disjoint because the two ground-set parts are disjoint. They therefore form a wave on \(P\cup Y\), contradicting the choice of \(P\). The contracted family is loose. \(\square\)

The ZFC prerequisites are identified in the opening paragraph of [Ideals, ultrafilters and an ordinal rank](ideals-ultrafilters-and-an-ordinal-rank.md): Button's Theorem 16.6 for well-ordering and Theorem 11.4 for transfinite recursion. The induction above can also be read as a least-counterexample argument: a first failing ordinal would have all earlier supports in the closure, and the displayed reasoning would rule out failure there. No countability assumption is imposed on \(F\), \(K\), or the collection of waves. This reconstructs the wave argument of [BC, Lemma 4.3 and Corollaries 4.4–4.9].

### Encoding a family by two matroids

**Proposition 4.6** (Family-to-pair encoding). Suppose \(K\ne\varnothing\). On the explicitly tagged ground set \(F\times K\), define
\[
A=\bigoplus_{i\in K}M_i,
\qquad B=\bigoplus_{e\in F}Q_e,
\]
where the \(i\)-th summand of \(A\) is carried by \(F\times\{i\}\), and \(Q_e\) is the dual of the rank-one uniform matroid on \(\{e\}\times K\). Then \(\mathcal M\) has a packing/covering partition if and only if \((A,B)\) has one.

*The row matroids.* On any nonempty set \(R\), the independent sets of the rank-one uniform matroid are the empty set and the singletons. The independence axioms hold directly, including maximal extension inside each subset. Its dual \(Q_R\) has bases \(R\setminus\{r\}\), so its independent sets are the proper subsets of \(R\). A set spans \(Q_R\) precisely when it omits at most one point, by Lemma 2.7. Restriction of \(Q_R\) to a proper subset is free. For nonempty \(Z\subseteq R\), its contraction onto \(Z\) is \(Q_Z\), because
\[
Q_R.Z=(U_{1,R}\!\upharpoonright\!Z)^*=U_{1,Z}^*.
\]
These assertions include the one-point case, where \(Q_R\) is a loop matroid.

Restrictions, duals and contractions of a direct sum are taken separately in its summands. For restriction this follows from the independent-set definition in Proposition 3.1. For duality, a basis of the direct sum is a union of summand bases; its complement is the union of their complements. Theorem 2.3 therefore gives the assertion for duals. The definition of contraction then gives the assertion for contractions.

*From the family to the pair.* Let \(F=P\mathbin{\dot\cup}C\) and \((S_i,I_i)\) witness packing/covering for \(\mathcal M\). On \(P'=P\times K\), take the \(A\)-spanning set
\[
S^A=\{(e,i):e\in S_i\}
\]
and the \(B\)-spanning set \(S^B=P'\setminus S^A\). Each row of \(S^B\) omits at most one point because the \(S_i\) are disjoint; the row calculation proves that it spans. On \(C'=C\times K\), put \(I^A=\{(e,i):e\in I_i\}\) and \(I^B=C'\setminus I^A\). The direct-sum calculation makes \(I^A\) independent in \(A.C'\). Every row of \(I^B\) is proper because the \(I_i\) cover \(C\), so \(I^B\) is independent in \(B.C'\). This supplies the pair's witnesses.

*From the pair to the family.* Start with a partition \(F\times K=P'\mathbin{\dot\cup}C'\), disjoint spanning sets \(S^A,S^B\subseteq P'\), and independent covering sets \(I^A,I^B\subseteq C'\). No assumption that the spanning sets cover \(P'\) or that the covering sets are disjoint is needed. Partition \(F\) by
\[
P=\{e:\{e\}\times K\subseteq P'\},
\qquad C=F\setminus P.
\]
For a row indexed by \(e\in C\), its portion in \(P'\) is a proper subset of the row. The restriction of \(Q_e\) there is free. Since \(S^B\) spans that restriction, it contains the entire portion. Disjointness forces \(S^A\) to avoid it. Thus \(S^A\subseteq P\times K\). It spans the larger set \(P'\) in \(A\), and hence spans the restriction to \(P\times K\).

Define \(S_i=\{e:(e,i)\in S^A\}\). On every full row with \(e\in P\), the spanning set \(S^B\) omits at most one point. Hence \(S^A\) has at most one point in that row: the \(S_i\) are disjoint. Their spanning property in each \(M_i\!\upharpoonright\!P\) follows from the direct sum.

Define \(I_i=\{e:(e,i)\in I^A\}\). Each row indexed by \(e\in C\) meets \(C'\) in a nonempty set \(Z_e\). The corresponding summand of \(B.C'\) is \(Q_{Z_e}\), so the independent set \(I^B\) misses a point of \(Z_e\). The covering condition puts that point in \(I^A\). Thus the \(I_i\) cover \(C\). Finally \(C'\subseteq C\times K\). Lemma 4.4(2), which explicitly handles enlargement of a contraction's ground set, makes \(I^A\) independent in \(A.(C\times K)\). The direct-sum calculation now makes every \(I_i\) independent in \(M_i.C\). These are all the required family witnesses. \(\square\)

This proves [BC, Proposition 3.8] with the coordinate sets and the change-of-contraction step explicit. When \(K=\varnothing\), the family already has a packing/covering partition with \(P=F\) and \(C=\varnothing\), so no encoding is required.

### The two separate conditions and their universal equivalences

A *covering* of a family on \(F\) consists of independent sets, one in each matroid, whose union is \(F\). A *packing* consists of pairwise disjoint spanning sets. Equivalently one may use bases: extend each independent covering set to a basis, or choose a basis in each spanning packing set. The required extensions and selections are provided by (IM), Lemma 2.7 and the axiom of choice. We use the independent/spanning formulations so that the witnesses remain explicit.

For a particular family \(\mathcal M=(M_i)_{i\in K}\), consider the following two conditions:

- **Covering condition:** for each \(Y\subseteq F\), if \((M_i\!\upharpoonright\!Y)_i\) has a packing, then it has a covering.
- **Packing condition:** for each \(Y\subseteq F\), if \((M_i.Y)_i\) has a covering, then it has a packing.

These are conditions on all restrictions or all contractions of the specified family. They do not assert that an arbitrary chosen packing is a covering, or conversely.

**Theorem 4.7** (Universal equivalences, Bowler–Carmesin). Over ZFC the following assertions are equivalent:

1. Every pair of matroids on a common set satisfies intersection as in Proposition 4.3.
2. Every pair of matroids on a common set has a packing/covering partition.
3. Every set-indexed family of matroids on a common set has a packing/covering partition.
4. Every such family has a covering if and only if it satisfies the covering condition.
5. Every such family has a packing if and only if it satisfies the packing condition.

*Proof.* We prove the logical implications, not any of the assertions themselves. Their equivalence is compatible with the counterexample later in this course.

**Assertions 1, 2 and 3.** Proposition 4.3 and double duality give \(1\iff2\). Assertion 3 includes pairs. In the other direction, apply assertion 2 to the pair in Proposition 4.6 for any nonempty index set; the empty-index case was settled there. This proves \(2\iff3\).

**Assertion 3 implies assertion 4.** A covering restricts to a covering on every subset, proving necessity of the covering condition without any conjecture. For sufficiency, take a family satisfying that condition and apply assertion 3. Let \(F=P\mathbin{\dot\cup}C\), with disjoint spanning witnesses on \(P\) and independent covering witnesses \(I_i\) in \(M_i.C\). The covering condition, applied to \(P\), supplies independent \(J_i\subseteq P\) covering \(P\). By Lemma 2.6, \(J_i\cup I_i\) is independent in \(M_i\). Their unions cover \(F\).

**Assertion 4 implies assertion 3.** Choose a wave with greatest support \(P\) by Lemma 4.5 and write \(C=F\setminus P\). The contracted family \((M_i.C)_i\) is loose. It satisfies the covering condition: a packing of its restriction to a subset \(Y\) would be a wave supported on \(Y\), hence \(Y=\varnothing\), where empty witnesses give a covering. Assertion 4 therefore supplies an independent covering of the contracted family on \(C\). Combine it with the already chosen wave on \(P\); this is a packing/covering partition. The argument also proves the equivalence of assertions 3 and 4 when both are restricted to any one fixed size of the index set, in particular to pairs.

**Assertion 3 implies assertion 5.** First prove necessity for a family already having a packing \((S_i)_i\). Each \(S_i\) contains a basis \(D_i\). For every \(Y\subseteq F\), the set \(D_i\cap Y\) spans \(M_i.Y\): the independent set \(D_i\setminus Y\) extends to a basis \(A_i\) of the outside restriction, and Lemma 2.2 extends \(A_i\) to a basis \(H_i\subseteq A_i\cup D_i\). Its outside part is \(A_i\), so Lemma 2.6 identifies \(H_i\cap Y\subseteq D_i\cap Y\) as a contraction basis. The sets \(D_i\cap Y\) are disjoint, and thus give a packing of the contractions. In particular, the packing condition holds.

For sufficiency, take a family satisfying the packing condition and its partition supplied by assertion 3. On the covering side \(C\), that condition upgrades the independent covering of \((M_i.C)_i\) to a packing with disjoint spanning sets \(T_i\subseteq C\). If \(S_i\) are the original disjoint spanning sets on \(P\), Lemma 4.4(4) with \(Y=C\) makes \(S_i\cup T_i\) span \(M_i\). These unions are pairwise disjoint, and hence form a packing on \(F\).

**Assertion 5 implies assertion 3.** We first translate between covering and packing for two matroids. For a pair \((L_0,L_1)\) on \(H\), complements turn an independent covering \((J_0,J_1)\) into disjoint spanning sets \((H\setminus J_0,H\setminus J_1)\) for \((L_0^*,L_1^*)\), by Corollary 2.8. Complements reverse the construction. Consequently a pair has a covering if and only if its dual pair has a packing; a pair has a packing if and only if its dual pair has a covering.

Apply this observation on each subset \(Y\). The duals of \(L_i\!\upharpoonright\!Y\) are \(L_i^*.Y\). Thus the covering condition for \((L_0,L_1)\) is exactly the packing condition for \((L_0^*,L_1^*)\). Assertion 5, applied to the dual pair, implies the sufficiency direction of assertion 4 for the original pair; necessity was already unconditional. The fixed-pair version of the implication \(4\Rightarrow3\) gives assertion 2. Proposition 4.6 then upgrades it to assertion 3 for arbitrary families. This completes all the implications. \(\square\)

The theorem supplies the universal equivalences summarized in [BC, Section 7], with the wave argument, family encoding, and both sufficiency directions proved here. In the author version 1202.3409v2, Proposition 6.4 repeats the references to Conjectures 1.2 and 5.2 although it lies in the packing section. The argument above states the packing condition explicitly and proves its equivalence, rather than relying on that cross-reference.

For the pair constructed in the fifth lesson, failure of packing/covering disproves assertion 2 and therefore each of the five equivalent universal assertions. This conclusion concerns the general conjectures. It neither removes hypotheses from valid special cases nor says that the same pair must itself violate both of the separate conditional characterizations.

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
- [BDKPW] H. Bruhn, R. Diestel, M. Kriesell, R. Pendavingh and P. Wollan, *Axioms for infinite matroids*, Advances in Mathematics 239 (2013). https://arxiv.org/abs/1003.3919v3 (author version, 23 February 2013; proofs read at https://arxiv.org/html/1003.3919v3)
- [BC] N. Bowler and J. Carmesin, *Matroid intersection, base packing and base covering for infinite matroids*, Combinatorica 35 (2015). https://arxiv.org/abs/1202.3409v2 (author version, 5 March 2012; proofs read at https://arxiv.org/html/1202.3409v2)
- [BG] N. Bowler and S. Geschke, *Self-dual uniform matroids on infinite sets*, Proceedings of the AMS 144 (2016); author version (6 October 2014) on the author's page. https://www.math.uni-hamburg.de/home/geschke/papers/UniformMatroid7.pdf
