# Order reduction for marked ideals

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson proves the second half of the inductive step and closes the induction. A marked ideal \((\mathcal I,m)\) may have order \(\ge m\) along exceptional divisors created earlier, where the ordinary order reduction of the previous lesson does not see it. We split \(\mathcal I\) into a monomial part, supported on the divisor \(E\), and a remaining part; reduce the remaining part with the previous lesson; separate it from the high-order locus; and finally treat the monomial part by an explicit combinatorial procedure that uses the ordering of \(E\).

We use [Smooth blow-ups and transforms of ideals](smooth-blowups-and-transforms-of-ideals.md), [Blow-up sequences and the main theorems](blow-up-sequences-and-the-main-theorems.md) and [Order reduction for ideals](order-reduction-for-ideals.md).

**Induction hypothesis.** Theorem 4.1 of the second lesson (order reduction for ideals) holds for triples of dimension \(\le n\), with functoriality, as proved in the previous lesson from Theorem 4.2 in dimension \(<n\); and Theorem 4.2 holds in dimension \(<n\).

## 1. Monomial and non-monomial parts

Let \((X,\mathcal I,E)\) be a triple, \(E=(E^1,\ldots,E^s)\). Call the irreducible components of the members of \(E\) the *components of* \(E\). Distinct components are distinct prime divisors.

**Definition 1.1.** The *monomial part* of \(\mathcal I\) is \(M(\mathcal I)=\mathcal O_X\bigl(-\sum_Ca_CC\bigr)\), summed over the components \(C\) of \(E\), with \(a_C=\operatorname{ord}_C\mathcal I\). The *non-monomial part* is \(N(\mathcal I)=\mathcal O_X(\sum_Ca_CC)\cdot\mathcal I\).

**Lemma 1.2.**

1. \(N(\mathcal I)\) is an ideal sheaf, nonzero on every component of \(X\), whose order along every component of \(E\) is \(0\), and \(\mathcal I=M(\mathcal I)N(\mathcal I)\).
2. For a smooth morphism \(h:Y\to X\), \(M(h^*\mathcal I)=h^*M(\mathcal I)\) and \(N(h^*\mathcal I)=h^*N(\mathcal I)\), the components of \(h^{-1}E\) being the components of the \(h^{-1}(C)\). The same holds for change of field.
3. Let \(\pi\) be a blow-up of order \(\ge m\) for \((X,\mathcal I,m,E)\) whose centre \(Z\) has \(\operatorname{ord}_ZN(\mathcal I)=e\) at each generic point. Then \(N(\pi^{-1}_*(\mathcal I,m))=\pi^{-1}_*N(\mathcal I)\), the unmarked transform, and \(M(\pi^{-1}_*(\mathcal I,m))=\mathcal O(mF)\,\pi^*M(\mathcal I)\cdot\mathcal O(-eF)\).

**Proof.** (1) Locally \(X\) is factorial ([Regular local rings](course:AG-CA/AG-CA-14), Theorem 5.3), and \(\mathcal I\subset\mathcal O(-a_CC)\) for each \(C\) by [Smooth blow-ups and transforms of ideals, Lemma 4.1](smooth-blowups-and-transforms-of-ideals.md#4-transforms-of-ideals-and-of-marked-ideals). Since the \(C\) are distinct prime divisors, \(\bigcap_C\mathcal O(-a_CC)=\mathcal O(-\sum a_CC)\), so \(N(\mathcal I)\) is an ideal. Orders add, so \(\operatorname{ord}_CN(\mathcal I)=a_C-a_C=0\).

(2) A component \(C'\) of \(h^{-1}(C)\) maps onto a dense open subset of \(C\), so its generic point maps to that of \(C\), and \(\operatorname{ord}_{C'}h^*\mathcal I=a_C\) by [Smooth blow-ups and transforms of ideals, Proposition 2.6(4)](smooth-blowups-and-transforms-of-ideals.md#2-order-of-vanishing-and-derivative-ideals).

(3) Write \(\pi^{-1}_*(\mathcal I,m)=\mathcal O(mF)\pi^*M\cdot\pi^*N=\bigl(\mathcal O((m-e)F)\pi^*M\bigr)\cdot\bigl(\mathcal O(eF)\pi^*N\bigr)\). The second factor is the unmarked transform \(\pi^{-1}_*N\); by Lemma 4.1 of the first lesson its order along each component of \(F\) is \(0\). If a component \(C\) of \(E\) is a component of \(Z\), its strict transform is empty. Otherwise \(\pi\) is an isomorphism at the generic point of \(C\), and the order of the second factor along the strict transform of \(C\) is \(\operatorname{ord}_CN=0\). The first factor is supported on the total transform of \(E\), and it is an ideal because the product is and the second factor has order \(0\) along all components. So the decomposition of the transform is as stated. \(\square\)

Characterizing the monomial part componentwise is what makes Lemma 1.2(2) hold for smooth morphisms that are not surjective; a single coefficient per member \(E^i\) would change when an open subset misses the component on which the minimum is attained.

## 2. The construction

**Theorem 2.1.** Under the induction hypothesis, for every \(m\ge1\) there is a blow-up sequence functor \(\mathcal B^{\rm mord}_m\) of order \(\ge m\), defined on all marked triples \((X,\mathcal I,m,E)\) of dimension \(n\), with \(\operatorname{maxord}\mathcal I_r<m\) at its end, commuting with smooth morphisms and change of field. If \(m=\operatorname{maxord}\mathcal I\), then \(\mathcal B^{\rm mord}_m(X,\mathcal I,m,\emptyset)=\mathcal B^{\rm ord}_m(X,\mathcal I,\emptyset)\).

**Proof.** *Step 1: reduce the non-monomial part below \(m\).* While \(m'':=\operatorname{maxord}N(\mathcal I)\ge m\), apply \(\mathcal B^{\rm ord}_{m''}\) to the triple \((X,N(\mathcal I),E)\), replacing \((\mathcal I,m)\) by its transform. Each centre \(Z\) has \(\operatorname{ord}_ZN(\mathcal I)=m''\ge m\), hence \(\operatorname{ord}_Z\mathcal I\ge m\) since \(M(\mathcal I)\) is an ideal; it has snc with \(E\). So each blow-up is of order \(\ge m\) for \((\mathcal I,m)\), and by Lemma 1.2(3) the non-monomial part of the transform is the unmarked transform of \(N(\mathcal I)\). So the transform of \(N(\mathcal I)\) along \(\mathcal B^{\rm ord}_{m''}\) is the non-monomial part at each step, and at its end \(\operatorname{maxord}N<m''\). The loop stops after at most \(\operatorname{maxord}N(\mathcal I)-m+1\) rounds, with \(\operatorname{maxord}N(\mathcal I)<m\).

*Step 2: separate the non-monomial part from the high-order locus.* For \(t=m-1,m-2,\ldots,1\) in turn, put \(\mathcal K_t=N(\mathcal I)^m+\mathcal I^t\) and apply \(\mathcal B^{\rm ord}_{mt}\) to \((X,\mathcal K_t,E)\). Before the round for \(t\), the order of \(N(\mathcal I)\) is \(\le t\) at every point of \(\operatorname{cosupp}(\mathcal I,m)\): for \(t=m-1\) by Step 1, and for smaller \(t\) by the previous round. Then \(\operatorname{maxord}\mathcal K_t\le mt\): at points of \(\operatorname{cosupp}(\mathcal I,m)\) because \(\operatorname{ord}\mathcal K_t\le m\operatorname{ord}N\le mt\), and elsewhere because \(\operatorname{ord}\mathcal K_t\le t\operatorname{ord}\mathcal I\le t(m-1)\). Moreover

\[
\operatorname{cosupp}(\mathcal K_t,mt)=\operatorname{cosupp}(N(\mathcal I),t)\cap\operatorname{cosupp}(\mathcal I,m).
\]

A centre \(Z\) of \(\mathcal B^{\rm ord}_{mt}\) therefore has \(\operatorname{ord}_Z\mathcal I\ge m\) and \(\operatorname{ord}_ZN(\mathcal I)=t\), the latter because the order of \(N\) on \(\operatorname{cosupp}(\mathcal I,m)\) is \(\le t\). So the blow-up is of order \(\ge m\) for \((\mathcal I,m)\). Its unmarked transform of \(\mathcal K_t\) is

\[
\mathcal O(mtF)\pi^*\mathcal K_t=\bigl(\mathcal O(tF)\pi^*N\bigr)^m+\bigl(\mathcal O(mF)\pi^*\mathcal I\bigr)^t=N(\mathcal I_1)^m+\mathcal I_1^{\,t},
\]

by Lemma 1.2(3), where \(\mathcal I_1=\pi^{-1}_*(\mathcal I,m)\). So the transforms of \(\mathcal K_t\) along \(\mathcal B^{\rm ord}_{mt}\) are the ideals \(\mathcal K_t\) recomputed from the transforms of \((\mathcal I,m)\), and the bound on the order of \(N\) along the cosupport persists: points of the new cosupport lie over the old one, where \(N\) is being blown up along centres of order \(t=\operatorname{maxord}\) of \(N\) on a neighbourhood \(\{\operatorname{ord}N\le t\}\) of the cosupport, so Lemma 4.3 of the first lesson applies there. At the end of the round, \(\operatorname{maxord}\mathcal K_t<mt\), that is, \(\operatorname{cosupp}(N(\mathcal I),t)\cap\operatorname{cosupp}(\mathcal I,m)=\emptyset\). After the round \(t=1\), \(N(\mathcal I)\) has no zero on \(\operatorname{cosupp}(\mathcal I,m)\). Let \(V=X\setminus V(N(\mathcal I))\), an open neighbourhood of the cosupport, on which \(\mathcal I=M(\mathcal I)\). All further centres lie in the cosupport, so we may work on \(V\).

*Step 3: the monomial case.* Now \(\mathcal I=\mathcal O(-\sum_Ca_CC)\) on \(V\). A *stratum of size \(r\)* is a nonempty intersection \(C_1\cap\cdots\cap C_r\) of components of distinct members \(E^{j_1},\ldots,E^{j_r}\), \(j_1<\cdots<j_r\); its *index tuple* is \((j_1,\ldots,j_r)\) and its *value* is \(a_{C_1}+\cdots+a_{C_r}\). Strata are smooth, and the order of \(\mathcal I\) along a stratum of size \(r\) is its value, because no other component contains it by the snc condition. Since at most \(n\) components meet at a point, \(\operatorname{ord}_x\mathcal I\) is the value of the stratum of components through \(x\), and \(\operatorname{maxord}\mathcal I<m\) once every stratum has value \(<m\). For \(r=1,2,\ldots,n\) in turn, perform:

*Step 3.r.* While some stratum of size \(r\) has value \(\ge m\): let \(\mu\) be the largest value of such strata, let \(J\) be the lexicographically smallest index tuple among the strata of size \(r\) and value \(\mu\), and blow up the union of all strata of size \(r\) with index tuple \(J\) and value \(\mu\). These are disjoint, being components of \(E^{j_1}\cap\cdots\cap E^{j_r}\), so the centre is smooth; it has snc with \(E\), and \(\mathcal I\) has order \(\mu\ge m\) along it. The new exceptional divisor is appended as the last member, and on its component over a stratum \(C_1\cap\cdots\cap C_r\) the transform of \((\mathcal I,m)\) has coefficient \(\mu-m\).

We claim that before Step 3.r every stratum of size \(<r\) has value \(<m\) (call this \((*_{r-1})\)), that each round of Step 3.r preserves \((*_{r-1})\), and that Step 3.r terminates; then after Step 3.n every stratum has value \(<m\).

For \(r=1\), a round blows up components \(C\) of one member with \(a_C=\mu\ge m\). The blow-up is trivial; the strict transforms of these components are empty and they reappear in the new last member with coefficient \(\mu-m\). The multiset of coefficients \(\ge m\) decreases in the lexicographic sense from the top, so the loop ends, with all \(a_C<m\).

Let \(r\ge2\), assume \((*_{r-1})\), and consider one round, blowing up a stratum \(Z=C_1\cap\cdots\cap C_r\) (and its companions with the same tuple and value). The components of \(E\) through a point \(z\in Z\) are the \(C_i\) and possibly others \(C'\) not containing \(Z\). After the blow-up, a point \(q\) of the new component \(G\) over \(z\) lies on the strict transforms of at most \(r-1\) of the \(C_i\), because the strict transforms of \(r\) transversal hypersurfaces through \(Z\) have empty common intersection over \(Z\). Let \(A\) be the set of \(C_i\) and \(B\) the set of other components whose strict transforms pass through \(q\); all components in \(A\cup B\cup\{C_1,\ldots,C_r\}\) pass through \(z\). A stratum through \(q\) involving \(G\) is formed by \(G\) and a subset of \(A\cup B\), and its value is \(v=\sum_{A'}a+\sum_{B'}a+\mu-m\) for subsets \(A'\subset A\), \(B'\subset B\).

*Preservation of \((*_{r-1})\).* Suppose the new stratum has size \(s'=1+|A'|+|B'|\le r-1\). Write \(\{C_1,\ldots,C_r\}=A'\sqcup C^{\rm rest}\) with \(|C^{\rm rest}|=r-|A'|\ge2\) (as \(|A'|\le s'-1\le r-2\)). Split \(C^{\rm rest}=\{c\}\sqcup C^{\rm rest}_2\). Then

\[
v+m=\Bigl(\sum_{A'}a+\sum_{B'}a+a_c\Bigr)+\Bigl(\sum_{A'}a+\sum_{C^{\rm rest}_2}a\Bigr).
\]

The first bracket is the value of the stratum \(A'\cup B'\cup\{c\}\) through \(z\), of size \(s'\le r-1\); the second is the value of \(A'\cup C_2^{\rm rest}\), of size \(r-1\). By \((*_{r-1})\) both are \(<m\), so \(v<m\). Strata not involving \(G\) are strict transforms of old strata, with the same values.

*Termination.* A new stratum of size \(r\) involving \(G\) has the form \(G\) with \(r-1\) further components, and its value is \(\bigl(\sum_{r-1\text{ components}}a-m\bigr)+\mu<\mu\) by \((*_{r-1})\), applied to those \(r-1\) components, which meet at \(z\). All strata of size \(r\) with tuple \(J\) and value \(\mu\) are blown up in the round and disappear, since the strict transforms of their components no longer meet; strata of size \(r\) not involving \(G\) are strict transforms of old ones, with the same values. So the pair (largest value \(\ge m\) of a stratum of size \(r\), number of index tuples attaining it) decreases lexicographically, and the loop ends.

*Functoriality.* Steps 1 and 2 are composites of functors \(\mathcal B^{\rm ord}\) applied to ideals built from \(\mathcal I\) by operations that commute with smooth pull-back and change of field (Lemma 1.2(2)). Step 2 has the fixed rounds \(t=m-1,\ldots,1\). The rounds of Step 1 are indexed by the current maximal order of \(N\). For a smooth \(h:Y\to X\), a round on \(X\) whose order exceeds the maximal order of \(N\) over \(h(Y)\) has its centres away from \(h(Y)\) and pulls back to empty blow-ups. The maximal order over \(X\) cannot drop below the maximal order over \(h(Y)\), because the points of \(Y\) are untouched by those rounds. So the remaining rounds pull back to the rounds on \(Y\), in order. Step 3 chooses its centres by numerical data on strata, which pull back to strata with the same index tuples and values. For a smooth \(h:Y\to X\) whose image misses some strata, a round on \(X\) whose centre does not meet \(h(Y)\) pulls back to an empty blow-up, and the remaining rounds pull back to the rounds on \(Y\) in the same order: the largest value over strata meeting \(h(Y)\), and the smallest tuple attaining it, are computed from the pulled-back data. The phases \(r=1,\ldots,n\) correspond, because the pulled-back data satisfy \((*_{r-1})\) whenever the data on \(X\) do.

*The case \(E=\emptyset\), \(m=\operatorname{maxord}\mathcal I\).* Then \(M(\mathcal I)=\mathcal O\), \(N(\mathcal I)=\mathcal I\), and the first round of Step 1 applies \(\mathcal B^{\rm ord}_m(X,\mathcal I,\emptyset)\). All its blow-ups have order exactly \(m\), so the marked and unmarked transforms agree, and the transform has maximal order \(<m\) and no exceptional component in its divisorial part, since an order-\(m\) centre never contains a component of an exceptional divisor along which the unmarked transform has order \(0\). Hence \(M=\mathcal O\), \(N=\mathcal I_r\) has maximal order \(<m\), the cosupport is empty, and Steps 1 to 3 do nothing more. \(\square\)

## 3. Closed embeddings and the end of the induction

**Proposition 3.1.** Let \(j:Y\to X\) be a closed embedding of smooth schemes of dimension \(\le n\), and \(\mathcal O_X/\mathcal I=j_*(\mathcal O_Y/\mathcal J)\) with \(\mathcal J\) nonzero on every component of \(Y\). Then \(\mathcal B^{\rm mord}_1(X,\mathcal I,1,\emptyset)=j_*\mathcal B^{\rm mord}_1(Y,\mathcal J,1,\emptyset)\).

**Proof.** Both sides are blow-up sequence functors in the triple, commute with surjective local isomorphisms, and are defined on disjoint unions by running the pieces simultaneously (Remark 3.3 of the second lesson). So it suffices to prove the identity on the members of an open cover, taken together as one disconnected scheme. Cover \(X\) by opens on which coordinates adapted to \(Y\) give a chain \(Y=Y_0\subset Y_1\subset\cdots\subset Y_c=X\), each a smooth hypersurface in the next. Let \(\mathcal J_k\) be the ideal on \(Y_k\) with \(\mathcal O_{Y_k}/\mathcal J_k\) the push-forward of \(\mathcal O_Y/\mathcal J\); it contains the ideal of \(Y\) in \(Y_k\), so it is nonzero on every component of \(Y_k\) and has maximal order \(1\) when \(k>0\). For one hypersurface step, Theorem 2.1 gives \(\mathcal B^{\rm mord}_1(Y_{k+1},\mathcal J_{k+1},1,\emptyset)=\mathcal B^{\rm ord}_1(Y_{k+1},\mathcal J_{k+1},\emptyset)\), and [Order reduction for ideals, Theorem 3.1](order-reduction-for-ideals.md#3-order-reduction-for-ideals-in-dimension-n) identifies this with the push-forward of \(\mathcal B^{\rm mord}_1(Y_k,\mathcal J_k,1,\emptyset)\). Composing the push-forwards along the chain gives the claim. \(\square\)

**Corollary 3.2.** Theorems 4.1 and 4.2 of [Blow-up sequences and the main theorems](blow-up-sequences-and-the-main-theorems.md#4-the-theorems-of-the-course) hold in every dimension, including the statements (1) and (2) of Theorem 4.2, with functoriality for smooth morphisms between triples of arbitrary dimensions.

**Proof.** In dimension \(0\), \(\mathcal I=\mathcal O_X\) and both functors are empty. If Theorem 4.2 holds in dimensions \(<n\), the previous lesson gives Theorem 4.1 in dimension \(n\), and Theorem 2.1 and Proposition 3.1 give Theorem 4.2 in dimension \(n\). The functoriality for a smooth \(h:Y\to X\) with \(\dim Y>\dim X\) is proved in the same induction on \(\dim Y\): every construction step on \(Y\) is the pull-back of the corresponding step on \(X\), and the restricted problems have dimensions \(\dim Y-1\) and \(\dim X-1\). \(\square\)

## 4. Examples

**Example 4.1 (dimension one).** On a smooth curve, \(\operatorname{cosupp}(\mathcal I,m)\) is a finite set of closed points, the only possible centres. In Step 1 each point of maximal order \(m''\ge m\) of \(N(\mathcal I)\) is blown up, a trivial blow-up that turns its multiplicity \(m''\) into the coefficient \(m''-m\) of a new member of \(E\) and removes it from \(N\). Step 2 is empty, because a point in \(\operatorname{cosupp}(\mathcal I,m)\) is not a zero of \(N\) after Step 1. Step 3 lowers each coefficient \(a\ge m\) to \(a-m\), repeatedly.

**Example 4.2 (why Step 3.1 comes first).** Let \(E^1,E^2\) be curves on a smooth surface meeting at one point \(p\), and \(\mathcal I=\mathcal O(-(m+1)(E^1+E^2))\) with marking \(m\). Blowing up the point \(p\), of value \(2m+2\), gives a new curve \(E^3\) with coefficient \(m+2\). The point \(E^2\cap E^3\) has value \(2m+3\); blowing it up gives \(E^4\) with coefficient \(m+3\), then \(E^3\cap E^4\) gives \(m+5\), and so on: the offsets \(1,2,3,5,8,\ldots\) are Fibonacci numbers, and the values grow without end. Step 3.1 instead blows up \(E^1\) and \(E^2\) (trivially), lowering both coefficients to \(1\); Step 3.2 then deals with the single point of value \(2\), if \(m\le2\).

## 5. Exercises

**Exercise 5.1.** Run Step 3 for \(\mathcal I=\mathcal O(-3E^1-2E^2)\) on a surface, \(E^1\cap E^2=\{p\}\), with \(m=2\).

*Solution.* Step 3.1: \(a_1=3\ge2\) is maximal, so blow up \(E^1\) trivially; it reappears as \(E^3\) with coefficient \(1\), and \(E^1\) becomes empty. Then \(a_2=2\ge2\): blow up \(E^2\), which reappears as \(E^4\) with coefficient \(0\). Now all coefficients are \(<2\). Step 3.2: the only stratum of size \(2\) is \(E^3\cap E^4=\{p\}\), of value \(1<2\). The marked ideal is \(\mathcal O(-E^3)\), of maximal order \(1<2\).

**Exercise 5.2.** Show that the bound \(\operatorname{maxord}\mathcal K_t\le mt\) in Step 2 can fail without Step 1, for \(\mathcal I=(x^3)\) on \(\mathbf A^1\), \(E=\emptyset\), \(m=2\), \(t=1\).

*Solution.* Without Step 1, \(N(\mathcal I)=(x^3)\) and \(\mathcal K_1=(x^6)+(x^3)=(x^3)\), of order \(3>mt=2\) at the origin. Step 1 first blows up the origin, a trivial blow-up: the marked transform is \(x^{-2}(x^3)=(x)\), which is the monomial ideal of the new member \(\{0\}\) of \(E\) with coefficient \(3-2=1\), and \(N=\mathcal O\).

**Exercise 5.3.** On a threefold, let \(E^1,E^2,E^3\) meet transversally at a point, with coefficients \(a_1=a_2=a_3=1\), and let \(m=3\). Check \((*_2)\), run Step 3.3, and list the strata through points of the new divisor with their values.

*Solution.* Single components have value \(1\) and pairs value \(2\), both \(<3\), so \((*_2)\) holds. The triple point has value \(3\ge3\) and is blown up, giving \(G\) with coefficient \(0\). Through points of \(G\) the strata are \(G\) (value \(0\)), \(G\cap C_i\) (value \(1\)) and \(G\cap C_i\cap C_j\) (value \(2\)); the strict transforms of \(C_1,C_2,C_3\) have no common point. All values are \(<3\), as the preservation argument predicts.

## References

- [Kollár] J. Kollár, *Resolution of singularities — Seattle lecture*, arXiv:math/0508332, section "Order reduction for marked ideals" (monomial and non-monomial parts, the monomial case, the Fibonacci example). This lesson uses componentwise monomial parts and adds the preservation argument in Step 3.r. <https://arxiv.org/abs/math/0508332>
- [Włodarczyk] J. Włodarczyk, *Simple Hironaka resolution in characteristic zero*, arXiv:math/0401401, companion ideals and the monomial case. <https://arxiv.org/abs/math/0401401>
