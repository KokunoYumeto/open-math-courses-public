# Category and computability

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

A subset of the line or of the plane is *meager* if it is a countable union of nowhere dense sets. Meager sets are small in the sense of category, as sets of measure zero are small in the sense of measure. This lesson proves three statements that connect this notion with computability. A Borel function is continuous on the complement of a meager set. For a Borel function \(F\) from the reals to the sets of natural numbers, the least index of a reduction of \(F(x+y)\) to \(F(x)\oplus F(y)\) is again a Borel function. And two real numbers, taken outside a meager set of pairs, do not help to compute a set: if \(Y\) is not computable from \(A\), then \(Y\) is not computable from \(A\) together with the cuts of \(u\) and \(v\), except for a meager set of pairs \((u,v)\).

- Meager and comeager sets; Baire's theorem (Theorem 1.1, Lemma 1.2).
- Borel sets have the Baire property (Lemma 2.1); a Borel function is continuous on a comeager set (Lemma 2.2).
- The reduction relations are Borel (Lemmas 3.1 and 3.2).
- The avoidance lemma (Lemma 4.1).

The lesson follows [OpenAI-R, Section 2]; according to [OpenAI-R], the avoidance lemma is a principle of G. Sacks. It continues Relative computability and the Turing degrees and uses its reductions \(\Phi_e\), joins and cuts \(C(x)\). It uses the topology of \(\mathbb R^k\) and the notion of a Borel set from the core course [Measure and Integration (D10)](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D10).

## 1. Meager sets

Let \(X=\mathbb R^k\) with \(k=1\) or \(k=2\). A set \(N\subset X\) is *nowhere dense* if its closure contains no nonempty open set. A set is *meager* if it is a countable union of nowhere dense sets, and *comeager* if its complement is meager. Subsets and countable unions of meager sets are meager; so countable intersections of comeager sets are comeager.

**Theorem 1.1 (Baire).** A nonempty open subset of \(X\) is not meager. So a comeager set meets every nonempty open set: it is dense.

**Proof.** Let \(U\) be nonempty and open, and \(N_1,N_2,\dots\) nowhere dense. The closure of \(N_1\) does not contain \(U\), so there is a closed ball \(B_1\subset U\) of positive radius, at most \(1\), that does not meet \(N_1\). The closure of \(N_2\) does not contain the interior of \(B_1\), so there is a closed ball \(B_2\) in this interior, of positive radius at most \(\tfrac12\), that does not meet \(N_2\); and so on. The centres of the balls form a Cauchy sequence. Its limit lies in every \(B_n\), hence in \(U\) and in no \(N_n\). \(\blacksquare\)

**Lemma 1.2.**

1. A homeomorphism of \(X\) onto itself maps meager sets to meager sets.
2. If \(M\subset\mathbb R\) is meager, then \(M\times\mathbb R\) is meager in \(\mathbb R^2\).
3. A countable set is meager. A comeager subset of a nonempty open interval, that is, a set whose complement in the interval is meager, is uncountable.

**Proof.** (1) A homeomorphism maps closures to closures and open sets to open sets. (2) If the closure of \(N\) contains no interval, the closed set \(\overline N\times\mathbb R\) contains no nonempty open set. (3) A point is nowhere dense. If a comeager subset of an interval were countable, the interval would be meager, against Theorem 1.1. \(\blacksquare\)

## 2. Borel functions are continuous on a comeager set

A set \(S\subset X\) has the *Baire property* if there is an open set \(V\) such that the symmetric difference \(S\,\triangle\,V\) is meager.

**Lemma 2.1.** Every Borel subset of \(X\) has the Baire property.

**Proof.** The sets with the Baire property contain the open sets. We show that they are closed under complements and countable unions; then they contain all Borel sets.

*Complements.* Let \(S\,\triangle\,V\) be meager with \(V\) open. The closed set \(X\setminus V\) differs from its interior \(V'\) by its boundary, which is closed and contains no nonempty open set: it is nowhere dense. The set \((X\setminus S)\,\triangle\,V'\) is contained in the union of \(S\,\triangle\,V\) and this boundary.

*Unions.* If \(S_n\,\triangle\,V_n\) is meager for every \(n\), then \(\bigl(\bigcup S_n\bigr)\triangle\bigl(\bigcup V_n\bigr)\) is contained in the union of these sets. \(\blacksquare\)

The space \(2^{\mathbb N}\) carries the topology in which the sets \([\sigma]\) of all sets \(A\) with \(\sigma\prec A\), for strings \(\sigma\), form a base of open sets; these sets are open and closed. The set \(\mathbb N\) carries the discrete topology. A function \(f\) from \(X\) to one of these spaces is *Borel* if the preimage of every open set is a Borel set; it suffices that the preimages of the sets of a countable base are Borel. If \(F:\mathbb R\to2^{\mathbb N}\) is Borel and \(g:\mathbb R^2\to\mathbb R\) is continuous, then \(F\circ g\) is Borel, because preimages of Borel sets under continuous maps are Borel; for example \((x,y)\mapsto F(x+y)\). A map into a product of such spaces is Borel if its components are, because the products of sets of the bases form a countable base of the product.

**Lemma 2.2.** Let \(Y\) be \(2^{\mathbb N}\) or \(\mathbb N\), and \(f:X\to Y\) a Borel function. Then there is a comeager set \(D\subset X\) such that the restriction of \(f\) to \(D\) is continuous.

**Proof.** Let \(U_1,U_2,\dots\) be a countable base of \(Y\). By Lemma 2.1 there are open sets \(V_n\subset X\) and meager sets \(M_n\) with \(f^{-1}(U_n)\,\triangle\,V_n\subset M_n\). Let \(D\) be the complement of \(\bigcup_nM_n\). For \(x\in D\) we have \(f(x)\in U_n\) exactly if \(x\in V_n\). So the preimage of \(U_n\) under the restriction of \(f\) to \(D\) is \(D\cap V_n\), which is open in \(D\). \(\blacksquare\)

For \(Y=\mathbb N\) the conclusion means: every point of \(D\) has a neighbourhood \(V\) such that \(f\) is constant on \(D\cap V\). For \(Y=2^{\mathbb N}\) it means: for every point \(x\in D\) and every \(j\) there is a neighbourhood \(V\) of \(x\) such that the bit \(f(y)(j)\) is the same for all \(y\in D\cap V\). The lemma says nothing about the points outside \(D\).

## 3. The reduction relations are Borel

**Lemma 3.1.** For every index \(e\), the set of the triples \((A,B,Z)\) of sets such that \(\Phi_e\) computes \(Z\) from \(A\oplus B\) is a Borel subset of \(2^{\mathbb N}\times2^{\mathbb N}\times2^{\mathbb N}\).

**Proof.** For a number \(n\) and a bit \(b\) let \(P_{n,b}\) be the set of the triples with \(Z(n)=b\), and \(Q_{n,b}\) the set of the triples such that \(\sigma\prec A\oplus B\) for some \((\sigma,n,b)\in\Phi_e\). The first is open and closed, the second is a countable union of sets that are open and closed. The set of the lemma consists of the triples that lie, for all \(n\) and \(b\), in both or in neither of \(P_{n,b}\) and \(Q_{n,b}\): a countable intersection of Borel sets. \(\blacksquare\)

**Lemma 3.2.** Let \(F:\mathbb R\to2^{\mathbb N}\) be a Borel function with \(F(x+y)\le_TF(x)\oplus F(y)\) for all real \(x,y\). For \((x,y)\in\mathbb R^2\) let \(e(x,y)\) be the least index \(e\) such that \(\Phi_e\) computes \(F(x+y)\) from \(F(x)\oplus F(y)\). Then \(e:\mathbb R^2\to\mathbb N\) is a Borel function.

**Proof.** The map \((x,y)\mapsto(F(x),F(y),F(x+y))\) is Borel. Let \(G_e\) be the preimage of the set of Lemma 3.1 under it; it is a Borel set. By the assumption every pair lies in some \(G_e\), and \(e(x,y)=e\) exactly if \((x,y)\) lies in \(G_e\) and in no \(G_{e'}\) with \(e'<e\). \(\blacksquare\)

## 4. The avoidance lemma

**Lemma 4.1.** Let \(A\) and \(Y\) be sets of natural numbers such that \(Y\) is not computable from \(A\). Then the set of the pairs \((u,v)\in\mathbb R^2\) with
\[
Y\le_TA\oplus C(u)\oplus C(v)
\]
is meager.

**Proof.** For an index \(e\) let \(S_e\) be the set of the pairs \((u,v)\) such that \(\Phi_e\) computes \(Y\) from \(A\oplus C(u)\oplus C(v)\). The set of the lemma is the union of the sets \(S_e\). We show that every \(S_e\) is nowhere dense.

*Strings and rectangles.* A string \(\gamma\) is an initial segment of the cut \(C(u)\) exactly if \(q_i<u\) for the \(i\) with \(\gamma(i)=1\) and \(u\le q_i\) for the \(i\) with \(\gamma(i)=0\); that is, exactly if \(u\) lies in an interval \((l_\gamma,u_\gamma]\), whose ends are computed from \(\gamma\) (they may be infinite, and the interval may be empty). For an open interval \((a,b)\) with rational ends, the set of the \(u\in(a,b)\) with \(\gamma\prec C(u)\) contains a nonempty open interval exactly if \(\max\{l_\gamma,a\}<\min\{u_\gamma,b\}\). This is a computable condition on \(\gamma,a,b\).

An initial segment \(\tau\) of a set \(A_0\oplus C_1\oplus C_2\) consists of three strings: its *parts* \(\alpha,\gamma_1,\gamma_2\), which are initial segments of \(A_0,C_1,C_2\); they are computed from \(\tau\).

*The reduction.* Suppose that \(S_e\) is dense in a rectangle \(R=(a_1,b_1)\times(a_2,b_2)\) with rational ends: every nonempty open subset of \(R\) contains a point of \(S_e\). Let \(\Psi\) be the set of the triples \((\alpha,n,b)\) for which there is a triple \((\tau,n,b)\in\Phi_e\) with the parts \(\alpha_0,\gamma_1,\gamma_2\) such that \(\alpha_0\) is an initial segment of \(\alpha\), the set of the \(u\in(a_1,b_1)\) with \(\gamma_1\prec C(u)\) contains a nonempty open interval, and the same holds for \(\gamma_2\) and \((a_2,b_2)\). The set \(\Psi\) is computably enumerable. We show that it computes \(Y\) from \(A\), which contradicts the assumption.

Let \((\alpha,n,b)\in\Psi\) with \(\alpha\prec A\), and \(\tau\) as in the definition. There is a nonempty open rectangle \(O\subset R\) with \(\gamma_1\prec C(u)\) and \(\gamma_2\prec C(v)\) for all \((u,v)\in O\). It contains a pair \((u,v)\in S_e\). For this pair \(\tau\prec A\oplus C(u)\oplus C(v)\), and since \(\Phi_e\) computes \(Y\) from this set, \(Y(n)=b\).

Conversely let \(n\) be given, and choose \((u,v)\in S_e\cap R\). There is \(\tau\prec A\oplus C(u)\oplus C(v)\) with \((\tau,n,Y(n))\in\Phi_e\). Its parts satisfy \(\alpha_0\prec A\), \(\gamma_1\prec C(u)\), \(\gamma_2\prec C(v)\). The set of the \(u'\in(a_1,b_1)\) with \(\gamma_1\prec C(u')\) is the intersection of \((a_1,b_1)\) with the interval \((l_{\gamma_1},u_{\gamma_1}]\), and it contains \(u\); so it contains the nonempty open interval from \(\max\{l_{\gamma_1},a_1\}\) to \(u\). The same holds for \(v\). So \((\alpha_0,n,Y(n))\in\Psi\).

*Conclusion.* So \(S_e\) is dense in no rectangle with rational ends. Every nonempty open set contains such a rectangle, and this contains a nonempty open set without points of \(S_e\). So the closure of \(S_e\) contains no nonempty open set. \(\blacksquare\)

The index \(e\) may depend on the pair \((u,v)\); the proof takes the union over all indices. This is what makes the lemma usable for reductions that are not uniform in the pair.

## 5. Exercises

**5.1.** Show that the set of the irrational numbers is comeager in \(\mathbb R\), and that the set of the rational numbers does not have a comeager intersection with any interval.

**5.2.** Give a Borel function \(f:\mathbb R\to\mathbb N\) that is continuous at no point of \(\mathbb Q\), and a comeager set \(D\) as in Lemma 2.2 for it.

**5.3.** For the string \(\gamma\) with \(\gamma(i)=1\) exactly for \(i\in\{0,2\}\), of length \(4\), and \(q_0=0,q_1=1,q_2=\tfrac12,q_3=2\): which \(u\) satisfy \(\gamma\prec C(u)\)?

**5.4.** Let \(a<b\) be rational and \(\gamma\) a string. Show that the set of the \(u\in(a,b)\) with \(\gamma\prec C(u)\) is empty or contains a nonempty open interval. Where does the proof of Lemma 4.1 use this?

**5.5.** Let \(Y\) be a set that is not computable. Show that the set of the real numbers \(u\) with \(Y\le_TC(u)\) is meager. Is it empty?

## 6. Solutions

**5.1.** \(\mathbb Q\) is countable, hence meager (Lemma 1.2), so its complement is comeager. If \(\mathbb Q\cap I\) were comeager in an interval \(I\), then \(I\) would be the union of two meager sets.

**5.2.** Let \(f(x)=1\) for rational \(x\) and \(f(x)=0\) otherwise. It is Borel, and it is not continuous at any point. On the comeager set \(D\) of the irrational numbers it is constant.

**5.3.** \(q_0<u\) and \(q_2<u\), and \(u\le q_1\), \(u\le q_3\): the interval \((\tfrac12,1]\).

**5.4.** The set is the intersection of \((a,b)\) with an interval \((l,r]\). If it contains a point \(u\), then \(l<u\) and \(a<u\), and it contains the open interval from \(\max\{l,a\}\) to \(u\). The proof uses this in its second half: the strings of a triple for a pair of \(S_e\cap R\) hold at this pair, hence on a nonempty open set of pairs, which is what the definition of \(\Psi\) asks for.

**5.5.** Repeat the proof of Lemma 4.1 with one real number in place of two and with the empty set for \(A\): for every index \(e\), the set of the \(u\) such that \(\Phi_e\) computes \(Y\) from \(C(u)\) is dense in no interval with rational ends, because otherwise \(Y\) would be computable. So the set in question is meager. It is not empty: by Lemma 5.1 (3) of the lesson on relative computability there is \(t\) with \(C(t)\) Turing equivalent to \(Y\).

## References

- [OpenAI-R] OpenAI, *Rigidity of the Turing degrees*, OpenAI Math Release preprint, 24 September 2026, Section 2. https://github.com/openai/math/tree/main/preprints/Rigidity-of-the-Turing-degrees-September-24-2026
