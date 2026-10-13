# Order-invariant arrays and the common index

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson proves the alignment theorem of [OpenAI-I]: for families of lists that respect separation, a random set \(B\) of \(s\) layers with a suitable law is aligned with high probability. The previous lesson showed that otherwise there would be random patterns whose laws depend only on the order of the layers and for which a set is bad with positive probability. Here such laws are used to build one random pattern on all rational numbers. In this pattern every label has a *cut*, the supremum of the minima of its occurrence sets. Because the law does not change under increasing maps of the rational numbers, the cut cannot lie strictly between two elements of an occurrence set. So it is a layer that all occurrence sets have in common, and no set is bad.

- A random pattern on the rational numbers (Lemmas 1.1 to 1.3).
- The cut of a label lies in every occurrence set (Proposition 2.3, Theorem 2.4).
- Proof of the alignment theorem (Section 3).
- Aligned pairs of a chain and a set of layers (Proposition 4.1).

The lesson follows [OpenAI-I, Sections 5 and 8]. It continues [Alignment of lists: patterns, minimax and Ramsey's theorem](alignment-of-lists-patterns-minimax-and-ramseys-theorem.md) and uses its notions: patterns, restriction, standard form, bad sets. It needs the Lebesgue measure on \([0,1)\) with its countable additivity ([core course *Measure and Integration*](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D10)).

## 1. A random pattern on the rational numbers

Fix integers \(s,d\ge1\). Throughout Sections 1 and 2, \(P_t\) is a law on \(\mathcal P_t\) for every \(t\ge1\), and these laws are *consistent*: if \(t\le u\), \(X\subset[u]\) has \(t\) elements and \(C\) has the law \(P_u\), then the standard form of \(C|_X\) has the law \(P_t\).

For a finite set \(X\subset\mathbb Q\) with \(t\) elements, let \(P^X\) be the law on \(\mathcal P(X)\) that corresponds to \(P_t\) under the increasing bijection from \(X\) to \([t]\). So a random pattern on \(X\) has the law \(P^X\) if its standard form has the law \(P_t\). Two properties follow from the consistency and from the compatibility of restriction and standard form:

- (R) if \(X'\subset X\) and \(C\) has the law \(P^X\), then \(C|_{X'}\) has the law \(P^{X'}\);
- (O) if \(g:X\to Y\) is an increasing bijection of finite subsets of \(\mathbb Q\) and \(C\) has the law \(P^X\), then \(g(C)\) has the law \(P^Y\).

Let \(q_1,q_2,\dots\) be an enumeration of \(\mathbb Q\), and \(X_n=\{q_1,\dots,q_n\}\). The probability space is \([0,1)\) with the Lebesgue measure, written \(\Pr\).

**Lemma 1.1.** There are maps \(C_n:[0,1)\to\mathcal P(X_n)\), \(n\ge1\), such that

1. for every \(C\in\mathcal P(X_n)\) the set \(\{\omega:C_n(\omega)=C\}\) is an interval \([\alpha,\beta)\) of the length \(P^{X_n}(C)\), or empty if this number is \(0\);
2. \(C_{n+1}(\omega)|_{X_n}=C_n(\omega)\) for all \(\omega\) and \(n\).

**Proof.** Cut \([0,1)\) into consecutive intervals \(J_1(C)\), \(C\in\mathcal P(X_1)\), of the lengths \(P^{X_1}(C)\). If the intervals \(J_n(C)\), \(C\in\mathcal P(X_n)\), are defined, then by (R)
\[
\sum_{C':\ C'|_{X_n}=C}P^{X_{n+1}}(C')=P^{X_n}(C)
\]
for every \(C\). So \(J_n(C)\) can be cut into consecutive intervals \(J_{n+1}(C')\) of the lengths \(P^{X_{n+1}}(C')\), one for every \(C'\in\mathcal P(X_{n+1})\) with \(C'|_{X_n}=C\). Let \(C_n(\omega)\) be the pattern \(C\) with \(\omega\in J_n(C)\). \(\blacksquare\)

**The pattern on \(\mathbb Q\).** Let \(\omega\in[0,1)\). For a nonempty set \(I\subset\mathbb Q\) with at most \(s\) elements, let \(n_I(\omega)\) be the number \(n_I\) of the pattern \(C_n(\omega)\) for any \(n\) with \(I\subset X_n\); by Lemma 1.1(2) it does not depend on \(n\). The slot \((I,k)\) is *occupied* if \(k\le n_I(\omega)\). Two occupied slots \((I,k)\), \((I',k')\) are *equivalent* if they are equivalent in \(C_n(\omega)\) for any \(n\) with \(I\cup I'\subset X_n\). Any three slots lie in a common \(X_n\), and \(C_n(\omega)\) is a pattern that respects separation. So for every \(\omega\):

- this is an equivalence relation on the occupied slots; its classes are the *labels*, and the sets \(I\) of the slots of a label are its *occurrence sets*;
- two different slots of the same \(I\) are not equivalent;
- no label has two occurrence sets \(I,J\) with \(\max I<\min J\).

Write \(\mathbf C(\omega)\) for this pattern on \(\mathbb Q\), and \(\mathbf C(\omega)|_X\) for its restriction to a finite set \(X\): the pattern on \(X\) formed by the slots with \(I\subset X\).

**Lemma 1.2.** For every finite nonempty \(X\subset\mathbb Q\) and every \(C\in\mathcal P(X)\), the set \(\{\omega:\mathbf C(\omega)|_X=C\}\) is a finite union of intervals \([\alpha,\beta)\), and its measure is \(P^X(C)\).

**Proof.** Take \(n\) with \(X\subset X_n\). Then \(\mathbf C(\omega)|_X=C_n(\omega)|_X\). The set is the union of the intervals of Lemma 1.1(1) for the patterns \(C''\in\mathcal P(X_n)\) with \(C''|_X=C\), and its measure is \(P^X(C)\) by (R). \(\blacksquare\)

An event *depends on finitely many indices* if it has the form \(\{\omega:\mathbf C(\omega)|_X\in\mathcal G\}\) for a finite set \(X\subset\mathbb Q\) and a set \(\mathcal G\subset\mathcal P(X)\). By Lemma 1.2 such an event is a Borel set with the probability \(P^X(\mathcal G)\).

**Lemma 1.3** (invariance under the order). Let \(g:\mathbb Q\to\mathbb Q\) be an increasing bijection, \(X\subset\mathbb Q\) finite and \(\mathcal G\subset\mathcal P(X)\). Then
\[
\Pr\bigl(\mathbf C|_X\in\mathcal G\bigr)=\Pr\bigl(\mathbf C|_{g(X)}\in g(\mathcal G)\bigr),
\]
where \(g(\mathcal G)\) is the set of the patterns \(g(C)\), \(C\in\mathcal G\).

**Proof.** By Lemma 1.2 the two sides are \(P^X(\mathcal G)\) and \(P^{g(X)}(g(\mathcal G))\), which are equal by (O). \(\blacksquare\)

## 2. The cut of a label

Fix a slot \((I,k)\): a nonempty set \(I\subset\mathbb Q\) with at most \(s\) elements and \(1\le k\le d\). Let \(E\) be the event that this slot is occupied. For \(\omega\in E\) let \(\mathcal L\) be the label of the slot, and
\[
p=\sup_J\ \min J ,
\]
where \(J\) runs through the occurrence sets of \(\mathcal L\). This number is the *cut* of the label. The cut depends only on the label, not on the slot of the label from which one starts.

**Lemma 2.1.** On \(E\), \(\min I\le p\le\max I\).

**Proof.** \(I\) is an occurrence set of \(\mathcal L\). An occurrence set \(J\) with \(\min J>\max I\) is impossible, since then \(I\) would lie before \(J\). \(\blacksquare\)

So the cut is a real number. The supremum need not be attained, and at this point the cut might be irrational.

For a real number \(y\) let
\[
E_y=\{\omega\in E:\ p\le y\}.
\]
It is the set of the \(\omega\in E\) for which no occurrence set \(J\) of \(\mathcal L\) has \(\min J>y\).

**Lemma 2.2.** (1) \(E_y\) is a Borel set. (2) Let \(g\) be an increasing bijection of \(\mathbb Q\) with \(g(i)=i\) for all \(i\in I\), and let \(y\) be a rational number. Then \(\Pr(E_y)=\Pr(E_{g(y)})\).

**Proof.** Let \(J_1,J_2,\dots\) be an enumeration of the countably many nonempty sets \(J\subset\mathbb Q\) with at most \(s\) elements and \(\min J>y\). Let \(E_{y,n}\) be the event that \((I,k)\) is occupied and no occupied slot of \(J_1,\dots,J_n\) is equivalent to it. It depends on finitely many indices, those in \(X=I\cup J_1\cup\dots\cup J_n\). The events \(E_{y,n}\) decrease with \(n\), and their intersection is \(E_y\). So \(E_y\) is a Borel set and
\[
\Pr(E_y)=\lim_{n\to\infty}\Pr(E_{y,n}).
\]
This proves (1), and the limit is the same for every enumeration. For (2), put \(y'=g(y)\). Since \(g\) is an increasing bijection, \(\min g(J)=g(\min J)\), and \(J\mapsto g(J)\) maps the sets with \(\min J>y\) one-to-one onto the sets with a minimum \(>y'\). So \(g(J_1),g(J_2),\dots\) is an enumeration for \(y'\). The map \(g\) fixes the slot \((I,k)\), because it fixes \(I\) pointwise. So it carries the patterns on \(X\) in which \((I,k)\) is occupied and not equivalent to a slot of \(J_1,\dots,J_n\) to the patterns on \(g(X)\) in which \((I,k)\) is occupied and not equivalent to a slot of \(g(J_1),\dots,g(J_n)\). By Lemma 1.3, \(\Pr(E_{y,n})=\Pr(E_{y',n})\) for these enumerations, for every \(n\). Let \(n\to\infty\). \(\blacksquare\)

**Proposition 2.3.** \(\Pr\bigl(E\text{ and }p\notin I\bigr)=0\).

**Proof.** If \(I\) has one element, \(p\in I\) on \(E\) by Lemma 2.1. Otherwise let \(a<b\) be two neighbouring elements of \(I\), and let \(y<y'\) be rational numbers with \(a<y<y'<b\). Define \(g:\mathbb Q\to\mathbb Q\) by \(g(x)=x\) for \(x\le a\) and for \(x\ge b\), and, for \(a\le x\le y\) and for \(y\le x\le b\) respectively,
\[
\begin{gathered}
g(x)=a+\frac{y'-a}{y-a}\,(x-a),\\
g(x)=b-\frac{b-y'}{b-y}\,(b-x).
\end{gathered}
\]
This map is increasing, it maps rational numbers to rational numbers, and its inverse is the map of the same form with \(y\) and \(y'\) exchanged. So \(g\) is an increasing bijection of \(\mathbb Q\). It fixes every element of \(I\), since no element of \(I\) lies strictly between \(a\) and \(b\), and \(g(y)=y'\). By Lemma 2.2, \(\Pr(E_y)=\Pr(E_{y'})\). Since \(E_y\subset E_{y'}\),
\[
\begin{aligned}
\Pr\bigl(E&\text{ and }y<p\le y'\bigr)\\
&=\Pr(E_{y'})-\Pr(E_y)=0 .
\end{aligned}
\]
The open interval between \(a\) and \(b\) is the union of the countably many intervals \((y,y']\) with rational \(a<y<y'<b\). So \(\Pr(E\text{ and }a<p<b)=0\). There are finitely many pairs of neighbouring elements of \(I\), and by Lemma 2.1 the cut lies in \(I\) or strictly between two neighbouring elements. \(\blacksquare\)

**Theorem 2.4** (the common index). With probability \(1\), every label of the pattern \(\mathbf C\) has an element that lies in all of its occurrence sets, namely its cut. In particular, with probability \(1\), no finite set \(B\subset\mathbb Q\) with \(s\) elements is bad for \(\mathbf C|_B\).

**Proof.** There are countably many slots, so by Proposition 2.3 the following holds outside a set of measure \(0\): for every occupied slot \((I,k)\), the cut of its label lies in \(I\). For such \(\omega\), let \(\mathcal L\) be a label with the cut \(p\). Every occurrence set \(I\) of \(\mathcal L\) belongs to a slot of \(\mathcal L\), so \(p\in I\).

Let \(B\) have \(s\) elements. A label of \(\mathbf C|_B\) consists of the slots inside \(B\) of a label \(\mathcal L\) of \(\mathbf C\). Its occurrence sets inside \(B\) all contain the cut of \(\mathcal L\). So their intersection is not empty, and \(B\) is not bad. \(\blacksquare\)

**Example 2.5.** Let \(s=2\), \(d=1\). In the following pattern on \(\mathbb Q\) nothing is random: every set \(I\) with two elements has one occupied slot, the sets with one element have none, and the slots of \(I\) and \(J\) are equivalent if \(\max I=\max J\). An increasing bijection of \(\mathbb Q\) carries this pattern to itself. The label of \(\{a,c\}\), \(a<c\), has the occurrence sets \(\{x,c\}\) with \(x<c\). No two of them lie one before the other. The cut is \(\sup\{x:x<c\}=c\). It is not attained, and it lies in every occurrence set.

## 3. Proof of the alignment theorem

Recall the statement \(\mathrm A(\xi)\) of the previous lesson: there are \(r\ge s\) and a law \(\nu\) on the subsets of \([r]\) with \(s\) elements such that every pattern in \(\mathcal P_r\) has \(\Pr_{B\sim\nu}(B\text{ is bad})\le\xi\).

**Corollary 3.1.** For all \(s,d\ge1\) and every \(\xi>0\), the statement \(\mathrm A(\xi)\) is true.

**Proof.** Suppose it is false. Proposition 5.1 of the previous lesson gives consistent laws \(P_t\) with \(P_s([s]\text{ is bad})\ge\xi\). Build the pattern \(\mathbf C\) of Section 1 from them. By Lemma 1.2, the restriction of \(\mathbf C\) to the set \([s]\subset\mathbb Q\) has the law \(P_s\), so \([s]\) is bad for it with a probability of at least \(\xi>0\). By Theorem 2.4 this probability is \(0\). \(\blacksquare\)

**Proof of the alignment theorem** (Theorem 1.1 of the previous lesson). Let \(s,d\ge1\) and \(\eta>0\). By Corollary 3.1 with \(\xi=\eta/2\) there are \(r\ge s\) and a law \(\nu\) on the subsets of \([r]\) with \(s\) elements such that every pattern in \(\mathcal P_r\) has a bad set with a probability of at most \(\eta/2\).

Choose a law \(\mu\) with rational values and
\[
\sum_B|\mu(B)-\nu(B)|\le\frac\eta2 .
\]
For this, let \(B_0\) be a set with \(\nu(B_0)>0\); for \(B\ne B_0\) let \(\mu(B)\) be a rational number with \(\nu(B)-\epsilon\le\mu(B)\le\nu(B)\) and \(\mu(B)\ge0\), and let \(\mu(B_0)=1-\sum_{B\ne B_0}\mu(B)\ge\nu(B_0)\). If \(n\) is the number of the sets \(B\), the sum is at most \(2n\epsilon\), and \(\epsilon=\eta/(4n)\) will do.

For every pattern \(C\in\mathcal P_r\), the probabilities that \(B\) is bad for \(C\) under \(\mu\) and under \(\nu\) differ by at most \(\sum_B|\mu(B)-\nu(B)|\). So under \(\mu\) it is at most \(\eta\). By Lemma 2.1 of the previous lesson the same holds for every family of lists on \([r]\) that respects separation. \(\blacksquare\)

The proof is by contradiction and gives no bound for \(r\) in terms of \(s\), \(d\) and \(\eta\). For given rational \(\eta\), suitable \(r\) and \(\mu\) can be found by a search: for \(r=s,s+1,\dots\) the least value of the largest probability of a bad set over the finitely many patterns in \(\mathcal P_r\) is the solution of a finite system of linear inequalities with rational coefficients, and by the theorem it falls below \(\eta\) for some \(r\).

## 4. Aligned pairs of a chain and a set of layers

We return to the graph. The setting is that of the lesson [From an independent set to lists of answers](from-an-independent-set-to-lists-of-answers.md): an instance with \(\operatorname{val}(\mathcal C)\le\sigma\), an independent set \(\mathcal A\), and for every chain the lists \(A_I\subset M_r\) with at most \(d=J(64s,\gamma)(m+1)^s\) elements, one for every nonempty set \(I\) of at most \(s\) layers.

The number \(d\) depends on \(s\), \(m\) and \(\gamma\), and not on \(r\). Let \(\varepsilon>0\). **Suppose that the number \(r\) of the layers and the law \(\mu\) of the construction are those that the alignment theorem gives for \(s\), \(d\) and \(\eta=\varepsilon\).**

**Definition.** A pair of a chain and a set \(B\subset[r]\) with \(s\) elements is *aligned* if there is a map \(a:M_r\to B\) with \(a(A_I)\subset I\) for every nonempty \(I\subset B\), where the \(A_I\) are the lists of the chain.

**Proposition 4.1.** For a chain and a set \(B\) drawn as in the experiment, the probability that the pair is not aligned is at most
\[
4^rd^2\sigma+\varepsilon .
\]

**Proof.** By Corollary 5.2 of the lesson on the lists, with a probability of at least \(1-4^rd^2\sigma\) the chain is such that its lists form a family on \([r]\), with the set of labels \(M_r\), that respects separation. For every such chain the alignment theorem says that \(B\) is bad with a probability of at most \(\varepsilon\); here it matters that \(B\) is independent of the chain and that its law \(\mu\) was fixed without knowledge of the lists. \(\blacksquare\)

For an aligned pair fix one map \(a\). It is determined by the chain and by \(B\), before the coefficients and the rotations of the experiment are drawn. The last lesson, [The coefficient test and the theorem](the-coefficient-test-and-the-theorem.md), shows that for an aligned pair the vertex of the experiment lies in \(\mathcal A\) only with a small probability.

## 5. Exercises

**5.1.** Check that the map \(g\) in the proof of Proposition 2.3 is increasing, maps \(\mathbb Q\) onto \(\mathbb Q\), and that \(g(y)=y'\).

**5.2.** Let \(s=2\), \(d=1\), and consider the pattern on \(\mathbb Q\) in which every set with two elements has one occupied slot, the sets with one element have none, and the slots of \(I\) and \(J\) are equivalent if \(\min I=\min J\). Show that it respects separation, and find the cut of every label.

**5.3.** Let \(s=3\), \(d=1\). (a) Show that there is no pattern on \(\mathbb Q\) that respects separation and in which, for all rational \(a<b<c\), the slots \((\{a,c\},1)\) and \((\{b\},1)\) are occupied and equivalent. (b) Let \(a<b<c\) be rational. Show with Lemma 2.1 and Proposition 2.3 that, for the random pattern \(\mathbf C\) of Section 1, the event that these two slots are occupied and equivalent has the probability \(0\).

**5.4.** Let \(\nu\) and \(\mu\) be two laws on a finite set and \(G\) a subset. Show that \(|\mu(G)-\nu(G)|\le\tfrac12\sum_x|\mu(x)-\nu(x)|\).

**5.5.** In the setting of Section 4, let \(I=\{j\}\) be a single layer of \(B\), and \(\ell\in S_I^j\). Which layer is \(a(\pi_{jr}(\ell))\)? What does the definition of an aligned pair say for a label that stands on the lists of \(\{j\}\) and of \(\{j'\}\) for two different layers \(j,j'\) of \(B\)?

## 6. Solutions

**5.1.** On \([a,y]\) the map is linear with the positive rational slope \((y'-a)/(y-a)\); it maps \(a\) to \(a\) and \(y\) to \(y'\). On \([y,b]\) it is linear with the positive rational slope \((b-y')/(b-y)\) and maps \(y\) to \(y'\) and \(b\) to \(b\). Outside it is the identity. So \(g\) is continuous and increasing on \(\mathbb R\), maps \([a,y]\) onto \([a,y']\) and \([y,b]\) onto \([y',b]\). A linear map with rational coefficients and a slope other than \(0\) maps the rational numbers of an interval onto the rational numbers of the image interval. So \(g\) maps \(\mathbb Q\) onto \(\mathbb Q\).

**5.2.** Two occurrence sets of one label have the same minimum, so neither lies before the other. The label of \(\{a,c\}\) has the occurrence sets \(\{a,x\}\) with \(x>a\). All have the minimum \(a\), so the cut is \(a\). It lies in every occurrence set.

**5.3.** (a) Let \(a<b<b'<c\). The slots of \(\{b\}\) and of \(\{b'\}\) would both be equivalent to the slot of \(\{a,c\}\), hence to each other, and \(\{b\}\) lies before \(\{b'\}\). (b) On the event, the two slots have the same label, with the occurrence sets \(\{b\}\) and \(\{a,c\}\) among others. Lemma 2.1 for the slot of \(\{b\}\) gives \(b\le p\le b\): the cut of the label is \(b\). Proposition 2.3 for the slot of \(\{a,c\}\) says that, up to a set of measure \(0\), the cut of this label lies in \(\{a,c\}\) whenever the slot is occupied. Since \(b\notin\{a,c\}\), the event lies in a set of measure \(0\).

**5.4.** Let \(\delta(x)=\mu(x)-\nu(x)\). Then \(\sum_x\delta(x)=0\), so \(\sum_{x\in G}\delta(x)=-\sum_{x\notin G}\delta(x)\), and
\[
\begin{aligned}
2\Bigl|\sum_{x\in G}\delta(x)\Bigr|&=\Bigl|\sum_{x\in G}\delta(x)\Bigr|+\Bigl|\sum_{x\notin G}\delta(x)\Bigr|\\
&\le\sum_x|\delta(x)| .
\end{aligned}
\]

**5.5.** \(\pi_{jr}(\ell)\in A_{\{j\}}\), and \(a(A_{\{j\}})\subset\{j\}\), so \(a(\pi_{jr}(\ell))=j\). A label on the lists of \(\{j\}\) and \(\{j'\}\) would need \(a=j\) and \(a=j'\). So in an aligned pair the lists of two different single layers of \(B\) are disjoint. This agrees with the separation of the two sets \(\{j\}\), \(\{j'\}\).

## References

- [OpenAI-I] OpenAI, *Hardness of finding large independent sets in three-colorable graphs*, OpenAI Math Release preprint, 24 September 2026, Sections 5 and 8. https://github.com/openai/math/tree/main/preprints/Hardness-of-finding-large-independent-sets-in-three-colorable-graphs-September-24-2026
