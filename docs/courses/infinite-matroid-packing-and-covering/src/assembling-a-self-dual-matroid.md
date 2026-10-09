# Assembling a self-dual matroid

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson builds the self-dual matroid \(Q\) on \(E_0=L\mathbin{\dot\cup}R\). Its bases are the local bases of [Probes and local bases](probes-and-local-bases.md) for a carefully chosen family of prototypes, inserted in complementary pairs by a transfinite recursion of length \(\mathfrak c\) that visits every interval of subsets of \(E_0\). Every prototype is *admissible*: its \(L\)-slice and the complement of its \(R\)-slice are both large with a strict inequality of ordinal ranks, or both small with the reverse inequality for their complements (Section 1). The recursion uses the reservations of [Ideals, ultrafilters and an ordinal rank](ideals-ultrafilters-and-an-ordinal-rank.md) to keep different classes apart (Section 2), so that the union of the local families is an antichain meeting every interval (Section 3), and the matroid axioms, including maximal extension, follow (Section 4). The interval criterion and the use of complementary classes go back to Bowler and Geschke [BG]. Notation is that of the two previous lessons.

## 1. Admissible sets and two zones

For \(X\subseteq E_0\) put \(u(X)=X_L\) and \(y(X)=D\setminus X_R\). Call \(X\) **admissible** if
\[
u(X),y(X)\in\mathcal U\ \text{ and }\ \rho(u(X))>\rho(y(X)),\qquad\text{or}\qquad u(X),y(X)\notin\mathcal U\ \text{ and }\ \rho(D\setminus u(X))>\rho(D\setminus y(X)). \tag{1.1}
\]
The **Upper zone** consists of the \(X\) with \(u(X)\) large and either \(y(X)\) small, or \(y(X)\) large and \(\rho(u(X))\le\rho(y(X))\). The **Lower zone** consists of the \(X\) with \(X^c\) in the Upper zone.

**Lemma 1.1** (Zones). The Upper zone, the Lower zone and the admissible sets partition the subsets of \(E_0\). The Upper zone is closed under supersets and the Lower zone under subsets. All three are invariant under symmetric differences in \(\mathcal K_0\). Complementation exchanges the zones and preserves admissibility. \(\varnothing\) is Lower and \(E_0\) is Upper, and every admissible set and its complement are \(\mathcal J_0\)-positive.

*Proof.* Write \(u=u(X)\), \(y=y(X)\); then \(u(X^c)=D\setminus u\) and \(y(X^c)=D\setminus y\). If \(u\) is large and \(y\) small, \(X\) is Upper; if \(u\) is small and \(y\) large, \(X^c\) is Upper, so \(X\) is Lower. If both are large, \(X\) is not Lower (that needs \(D\setminus u\) large), and the comparison of \(\rho(u)\) with \(\rho(y)\) makes it Upper or admissible. If both are small, \(X\) is not Upper, and the comparison of \(\rho(D\setminus u)\) with \(\rho(D\setminus y)\) makes it Lower or admissible. This gives the partition and the behaviour under complements.

Let \(X\subseteq X'\) with \(X\) Upper, \(u'=u(X')\supseteq u\), \(y'=y(X')\subseteq y\). Then \(u'\) is large. If \(y'\) is small, \(X'\) is Upper. Otherwise \(y\supseteq y'\) is large, so \(\rho(u)\le\rho(y)\), and Lemma 4.1 of [Ideals, ultrafilters and an ordinal rank](ideals-ultrafilters-and-an-ordinal-rank.md) gives \(\rho(u')\le\rho(u)\le\rho(y)\le\rho(y')\). The Lower zone follows by complements. Changes in \(\mathcal K_0\) change \(u\) and \(y\) by members of \(\mathcal K\), which preserve largeness and \(\rho\) (Lemma 4.1 there). For \(\varnothing\), \(u=\varnothing\) is small and \(y=D\) large. Finally, in the first case of (1.1), \(X_L=u\) and \((X^c)_R=y\) are large, hence \(\mathcal J\)-positive; in the second case \(X_R=D\setminus y\) and \((X^c)_L=D\setminus u\) are. \(\square\)

**Lemma 1.2** (Crossing the zones). If \(A\subseteq Z\subseteq E_0\) with \(A\) Lower and \(Z\) Upper, there is an admissible \(B\) with \(A\subseteq B\subseteq Z\).

*Proof.* Since \(A\) is Lower, \(s=A_L\) is small; since \(Z\) is Upper, \(X=Z_L\) is large; and \(s\subseteq X\). We take \(B_R=A_R\), and put \(y=D\setminus A_R\). If \(y\) is large, Lemma 4.2 of [Ideals, ultrafilters and an ordinal rank](ideals-ultrafilters-and-an-ordinal-rank.md) gives a large \(u\) with \(s\subseteq u\subseteq X\) and \(\rho(u)>\rho(y)\); take \(B_L=u\). If \(y\) is small, the same lemma, for the small set \(D\setminus X\), the large set \(D\setminus s\) and \(\gamma=\rho(D\setminus y)\), gives a large \(v\) with \(D\setminus X\subseteq v\subseteq D\setminus s\) and \(\rho(v)>\rho(D\setminus y)\); take \(B_L=D\setminus v\), which is small and lies between \(s\) and \(X\). In both cases \(B\) satisfies (1.1), and \(A\subseteq B\subseteq Z\) because \(A_R=B_R\subseteq Z_R\). \(\square\)

## 2. Separation from earlier classes

**Lemma 2.1** (Inserting a prototype). Let \(\mathcal T\) be a family of fewer than \(\mathfrak c\) admissible sets, and let \(A\subseteq Z\subseteq E_0\) with \(A\) not Upper and \(Z\) not Lower, such that
\[
T\setminus A\notin\mathcal J_0\quad\text{and}\quad Z\setminus T\notin\mathcal J_0\qquad(T\in\mathcal T). \tag{2.1}
\]
Then there is an admissible \(B\) with \(A\subseteq B\subseteq Z\) such that \(B\setminus T\) and \(T\setminus B\) are \(\mathcal J_0\)-positive for every \(T\in\mathcal T\).

*Proof.* Put \(G=Z\setminus A\). List the set \(G\setminus T\) for every \(T\) with \(A\setminus T\in\mathcal J_0\); it is positive by (2.1), since \(Z\setminus T=(A\setminus T)\cup(G\setminus T)\). List also \(T\cap G\) for every \(T\) with \(T\setminus Z\in\mathcal J_0\); it is positive since \(T\setminus A=(T\setminus Z)\cup(T\cap G)\). There are fewer than \(\mathfrak c\) listed sets, so Lemma 5.1 of [Ideals, ultrafilters and an ordinal rank](ideals-ultrafilters-and-an-ordinal-rank.md) gives \(t\) such that \(H_0=H_{t,0}\) and \(H_1=H_{t,1}\), disjoint members of \(\mathcal K_0\), meet every listed set in a positive set. Put
\[
A'=A\cup(H_0\cap G),\qquad Z'=Z\setminus(H_1\cap G).
\]
Then \(A'\subseteq Z'\). The changes lie in \(\mathcal K_0\), so by Lemma 1.1 \(A'\) is not Upper and \(Z'\) is not Lower. If \(A'\) or \(Z'\) is admissible, let \(B\) be it; otherwise \(A'\) is Lower and \(Z'\) Upper, and Lemma 1.2 gives an admissible \(B\) between them. Let \(T\in\mathcal T\). If \(A\setminus T\) is positive, so is \(B\setminus T\supseteq A\setminus T\); otherwise \(B\setminus T\) contains the positive set \(H_0\cap(G\setminus T)\). If \(T\setminus Z\) is positive, so is \(T\setminus B\supseteq T\setminus Z\); otherwise \(T\setminus B\) contains the positive set \(H_1\cap T\cap G\). \(\square\)

## 3. Meeting every interval

**Proposition 3.1** (The basis family). There is a nonempty family \(\mathcal B\) of admissible subsets of \(E_0\) such that:

1. \(\mathcal B\) is an antichain under inclusion and is closed under complements;
2. if \(B\in\mathcal B\) and \(F\subseteq B\), \(H\subseteq E_0\setminus B\) are finite with \(|F|=|H|\), then \((B\setminus F)\cup H\in\mathcal B\);
3. for all \(I\subseteq Y\subseteq E_0\) with \(Y\setminus I\) infinite, some \(B\in\mathcal B\) satisfies
\[
B\subseteq I,\qquad\text{or}\qquad I\subseteq B\subseteq Y,\qquad\text{or}\qquad Y\subseteq B. \tag{3.1}
\]

*Proof.* There are \(\mathfrak c\) pairs \(I\subseteq Y\); list those with infinite gap as \((I_\alpha,Y_\alpha)_{\alpha<\mathfrak c}\), and fix a well-ordering of the subsets of \(E_0\) for the choices below. By transfinite recursion we retain *prototypes* in complementary pairs \(T,T^c\), the first with the rule \(-\) and the second with the rule \(+\) (so with local bases \(\mathcal B^-(T)\) and \(\mathcal B^+(T^c)=\{X^c:X\in\mathcal B^-(T)\}\)), maintaining that all prototypes are admissible and that any two distinct prototypes \(T,T'\) have \(T\setminus T'\) and \(T'\setminus T\) both \(\mathcal J_0\)-positive. The local bases of prototypes already retained are the *old bases*; they are closed under complements.

At stage \(\alpha\), let \(I=I_\alpha\), \(Y=Y_\alpha\). If some old basis satisfies (3.1), retain nothing. Otherwise, for every old prototype \(T\) with rule \(\sigma\), Proposition 2.3 of [Probes and local bases](probes-and-local-bases.md) shows that
\[
T\setminus I\notin\mathcal J_0\quad\text{and}\quad Y\setminus T\notin\mathcal J_0. \tag{3.2}
\]
Choose \([A,Z]=[\varnothing,I]\) if \(I\) is Upper, \([A,Z]=[Y,E_0]\) if \(Y\) is Lower, and \([A,Z]=[I,Y]\) otherwise; the first two cases exclude each other, because an Upper \(I\subseteq Y\) makes \(Y\) Upper. In each case \(A\) is not Upper and \(Z\) is not Lower. We check (2.1) for every old prototype \(T\). In the third case it is (3.2). In the first case \(T\setminus A=T\) is positive, and if \(I\setminus T\in\mathcal J_0\), then \(I\cap T\) would be Upper by invariance and contained in \(T\), making \(T\) Upper; so \(Z\setminus T=I\setminus T\) is positive. In the second case \(Z\setminus T=T^c\) is positive, and if \(T\setminus Y\in\mathcal J_0\), then \(T\cap Y\) would be admissible and contained in the Lower set \(Y\), hence Lower; so \(T\setminus A=T\setminus Y\) is positive. There are at most two prototypes for each earlier stage, so fewer than \(\mathfrak c\) old prototypes (Lemma 0.1 of [Ideals, ultrafilters and an ordinal rank](ideals-ultrafilters-and-an-ordinal-rank.md)). Lemma 2.1 gives an admissible \(B\) between \(A\) and \(Z\), separated from every old prototype; retain \(B\) with the rule \(-\) and \(B^c\) with the rule \(+\). The complement is separated from every old \(T\) as well, because \(T^c\) is old and \(B^c\setminus T=T^c\setminus B\), \(T\setminus B^c=B\setminus T^c\); and \(B\), \(B^c\) are separated from each other because both are \(\mathcal J_0\)-positive (Lemma 1.1). Since the probes of \(B\) relative to itself vanish, \(B\in\mathcal B^-(B)\), and its position in \([A,Z]\) gives (3.1).

Let \(\mathcal B\) be the union of all retained local families. It is nonempty and closed under complements. Its members differ from their prototypes by sets in \(\mathcal J_0\subseteq\mathcal K_0\), so they are admissible (Lemma 1.1). Within one class, Lemma 1.3 of [Probes and local bases](probes-and-local-bases.md) gives the antichain property and (2). Members \(X\in\mathcal C(T)\) and \(X'\in\mathcal C(T')\) of different classes satisfy \(X\setminus X'\supseteq(T\setminus T')\setminus(X\mathbin\triangle T\cup X'\mathbin\triangle T')\), which is positive, hence nonempty; so \(X\not\subseteq X'\), and symmetrically. Every interval received an outcome at its stage, and retained families are never changed. \(\square\)

## 4. The matroid

**Theorem 4.1** (OpenAI). There is a matroid \(Q\) on \(E_0\) whose bases are exactly the members of \(\mathcal B\). It is self-dual, and for every basis \(B\),
\[
B_L\in\mathcal U\quad\Longrightarrow\quad D\setminus B_R\in\mathcal U\quad\text{and}\quad\rho(B_L)>\rho(D\setminus B_R). \tag{4.1}
\]
Moreover every independent set that is not a basis remains independent after adding any element.

*Proof.* Let the independent sets be the subsets of members of \(\mathcal B\). (I1) holds since \(\mathcal B\ne\varnothing\), and (I2) is clear. Every member of \(\mathcal B\) is a maximal independent set, by the antichain property, and every maximal independent set lies in, hence equals, a member of \(\mathcal B\). Let \(I\) be independent but not maximal, so \(I\subsetneq B_0\) for some \(B_0\in\mathcal B\), and let \(e\notin I\). If \(e\in B_0\), then \(I\cup\{e\}\subseteq B_0\). Otherwise pick \(f\in B_0\setminus I\); then \((B_0\setminus\{f\})\cup\{e\}\in\mathcal B\) by Proposition 3.1(2), and it contains \(I\cup\{e\}\). This is the last assertion. For (I3), a maximal \(B_1\) is not contained in \(I\), since \(B_1\subseteq I\subsetneq B_0\) contradicts the antichain property; any \(e\in B_1\setminus I\) works.

(IM): let \(I\subseteq Y\) with \(I\) independent. If \(Y\setminus I\) is finite, an independent \(J\) with \(I\subseteq J\subseteq Y\) containing as many elements of the gap as possible is maximal. If the gap is infinite, take \(B\) as in (3.1). If \(B\subseteq I\), then \(B\subseteq I\subseteq B'\) for some \(B'\in\mathcal B\), so \(B=I=B'\) and \(I\) is itself maximal. If \(I\subseteq B\subseteq Y\), \(B\) is a maximal member. If \(Y\subseteq B\), \(Y\) is independent and is the maximal member.

Complements of bases are bases, so \(Q^*=Q\). Every basis is admissible; if \(B_L\in\mathcal U\), the first alternative of (1.1) holds, which is (4.1). \(\square\)

**Proposition 4.2** (Uniformity). (a) Every subset of \(E_0\) is independent or contains a basis of \(Q\). (b) Every finite subset of \(E_0\) is independent, and \(E_0\) is dependent; so \(Q\) is neither finitary nor cofinitary. (c) For every \(X\subseteq E_0\), every set spanning \(Q\!\upharpoonright\!X\) contains a maximal independent subset of \(X\).

*Proof.* (a) If \(X\) is dependent, let \(I\) be a maximal independent subset of \(X\) (by (IM)). If \(I\) were not a basis, any element of \(X\setminus I\neq\varnothing\) could be added by Theorem 4.1; so \(I\) is a basis. (b) Bases and their complements are infinite, being \(\mathcal J_0\)-positive. Starting from a basis, insert the missing elements of a finite \(F\) and delete equally many elements outside \(F\) (Proposition 3.1(2)); the result is a basis containing \(F\). \(E_0\) contains no basis, since every basis has a nonempty complement. A matroid is *finitary* if a set whose finite subsets are all independent is independent; \(E_0\) shows that \(Q\) is not, and since \(Q^*=Q\), its dual is not either. (c) Let \(S\subseteq X\) with \(\operatorname{cl}_Q(S)\supseteq X\). If \(S\) is dependent, it contains a basis by (a), which is maximal independent in \(X\). If \(S\) is independent but not maximal in \(X\), some \(x\in X\setminus S\) has \(S\cup\{x\}\) independent; then every independent \(J\subseteq S\) has \(J\cup\{x\}\) independent, so \(x\notin\operatorname{cl}_Q(S)\), a contradiction. \(\square\)

## 5. Exercises

**5.1.** Show that \(\varnothing\) is not admissible and that no admissible set is contained in a Lower set or contains an Upper set.

**5.2.** In Proposition 3.1, why are the prototypes inserted in complementary pairs, with opposite rules, rather than one at a time?

**5.3.** Show that \(Q\) has \(2^{\aleph_0}\) bases.

## 6. Solutions

**5.1.** \(\varnothing\) is Lower (Lemma 1.1), and the three classes are disjoint. An admissible set inside a Lower set would be Lower, and one containing an Upper set would be Upper, by the closure properties of the zones.

**5.2.** The family \(\mathcal B\) must be closed under complements for \(Q\) to be self-dual. Complementing local bases exchanges the rules, \(\mathcal B^+(T^c)=\{X^c:X\in\mathcal B^-(T)\}\) (Lemma 1.1(4) of [Probes and local bases](probes-and-local-bases.md)); inserting \(T\) with the rule \(-\) and \(T^c\) with the rule \(+\) therefore adds exactly the complements of the bases just added.

**5.3.** There are at most \(2^{\aleph_0}\) subsets of the countable set \(E_0\). For the lower bound, fix a basis \(B\) and distinct elements \(a_0,a_1,\dots\in B\) and \(b_0,b_1,\dots\notin B\). Index them instead by the finite binary strings, and for each infinite binary sequence \(\theta\) let \(S_\theta\) be the set of its finite initial segments; distinct \(\theta\) give \(2^{\aleph_0}\) infinite sets \(S_\theta\) with pairwise finite intersections. Put \(I_\theta=B\setminus\{a_s:s\in S_\theta\}\) and \(Y_\theta=I_\theta\cup\{b_s:s\in S_\theta\}\), an interval with infinite gap, and let \(B_\theta\) be a basis as in (3.1). \(B_\theta\subseteq I_\theta\subsetneq B\) is impossible by the antichain property, so \(B_\theta\supseteq I_\theta\), and either \(B_\theta\subseteq Y_\theta\) or \(B_\theta\supseteq Y_\theta\). Suppose \(B_\theta=B_{\theta'}=C\) with \(\theta\ne\theta'\), and let \(F=\{a_s:s\in S_\theta\cap S_{\theta'}\}\), a finite set; then \(C\supseteq I_\theta\cup I_{\theta'}=B\setminus F\). If \(C\supseteq Y_\theta\), choose \(|F|\) elements \(b_s\), \(s\in S_\theta\); exchanging them for \(F\) gives a basis \(B'\subseteq C\), so \(C=B'\), which contains only finitely many \(b_s\), while \(C\supseteq Y_\theta\) contains infinitely many. The same holds with \(\theta'\). Otherwise \(C\subseteq Y_\theta\) and \(C\subseteq Y_{\theta'}\); for \(s\in S_\theta\setminus S_{\theta'}\), \(a_s\in I_{\theta'}\subseteq C\) but \(a_s\notin Y_\theta\). So the \(2^{\aleph_0}\) bases \(B_\theta\) are distinct.

## References

- [OpenAI-IM] OpenAI, *A counterexample to the infinite matroid packing/covering conjecture*, OpenAI Math Release preprint, 24 September 2026. https://github.com/openai/math/blob/main/preprints/A-Counterexample-to-the-Infinite-Matroid-Packing-Covering-Conjecture-September-24-2026/paper.pdf
- [BG] N. Bowler and S. Geschke, *Self-dual uniform matroids on infinite sets*, Proceedings of the AMS 144 (2016); author version on the author's page. https://www.math.uni-hamburg.de/home/geschke/papers/UniformMatroid7.pdf
