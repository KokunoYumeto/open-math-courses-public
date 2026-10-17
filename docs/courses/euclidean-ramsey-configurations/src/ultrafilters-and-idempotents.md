# Ultrafilters and idempotents

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The sufficiency proof needs to evaluate products in a free group, including inverses, by actual strings of points. Strings can only be concatenated, never inverted. The remedy is to pass to ultrafilters on the monoid of strings: they form a compact semigroup, which contains an idempotent \(p\) whose corner \(p(\beta\mathcal S)p\) is a group, so a free group maps into it. A product of ultrafilters can then be realized by concatenating strings, with the same string chosen in every position where the factors agree. This lesson proves these facts. The idempotent comes from the classical argument of Ellis [Ellis]; the semigroup structure on ultrafilters is developed in the monograph of Hindman and Strauss (see [OpenAI-ER, Section 5]).

## 1. Ultrafilters

Let \(X\) be a set. A *filter* on \(X\) is a nonempty family \(u\) of subsets of \(X\) that does not contain \(\varnothing\), contains \(B\cap B'\) whenever it contains \(B\) and \(B'\), and contains every superset of each of its members. An *ultrafilter* is a filter not contained in a larger filter. A family has the *finite intersection property* if every finite subfamily has nonempty intersection.

**Lemma 1.1.** (a) Every family of subsets of \(X\) with the finite intersection property is contained in an ultrafilter.
(b) A filter \(u\) is an ultrafilter if and only if, for every \(B\subseteq X\), exactly one of \(B\) and \(X\setminus B\) belongs to \(u\).
(c) If \(X=X_1\cup\dots\cup X_r\) is a partition and \(u\) an ultrafilter, exactly one \(X_j\) belongs to \(u\).

*Proof.* (a) The finite intersections of the family, with their supersets, form a filter. Filters containing it, ordered by inclusion, have unions of chains as upper bounds, so Zorn's lemma gives a maximal one.
(b) If neither \(B\) nor \(X\setminus B\) is in \(u\), then \(B\) meets every member of \(u\): otherwise some member lies in \(X\setminus B\), which would then be in \(u\). So \(u\cup\{B\}\) has the finite intersection property and lies in a strictly larger filter. Conversely, if exactly one of each pair lies in \(u\) and \(u'\supsetneq u\) is a filter, a set \(B\in u'\setminus u\) has \(X\setminus B\in u\subseteq u'\), and \(\varnothing=B\cap(X\setminus B)\in u'\), which is impossible. Both cannot lie in \(u\), since their intersection is empty.
(c) If none of the \(X_j\) is in \(u\), their complements are all in \(u\), and so is their intersection, which is empty. Two members of \(u\) intersect, so at most one \(X_j\) is in \(u\). \(\square\)

For \(x\in X\), the *principal* ultrafilter \(\delta_x\) consists of all sets containing \(x\). The cofinite subsets of an infinite set have the finite intersection property, so by Lemma 1.1(a) there is a *nonprincipal* ultrafilter containing all of them.

Let \(\beta X\) be the set of ultrafilters on \(X\). For \(B\subseteq X\) put \(\overline B=\{u\in\beta X:B\in u\}\). Then \(\overline{B\cap B'}=\overline B\cap\overline{B'}\) and \(\beta X\setminus\overline B=\overline{X\setminus B}\), by Lemma 1.1(b). Give \(\beta X\) the topology whose open sets are the unions of sets \(\overline B\); each \(\overline B\) is open and closed.

**Lemma 1.2.** The space \(\beta X\) is compact and Hausdorff.

*Proof.* If \(u\ne v\), some \(B\in u\) is not in \(v\); then \(X\setminus B\in v\), and \(\overline B\), \(\overline{X\setminus B}\) are disjoint open sets containing \(u\) and \(v\). A closed set is an intersection of sets of the form \(\overline B\), since its complement is a union of such sets and \(\beta X\setminus\overline B=\overline{X\setminus B}\). So it suffices to show that sets \(\overline{B_j}\), \(j\in J\), with the finite intersection property have a common point. Since \(\overline{B_1}\cap\dots\cap\overline{B_m}=\overline{B_1\cap\dots\cap B_m}\) is nonempty only if \(B_1\cap\dots\cap B_m\ne\varnothing\), the family \((B_j)\) has the finite intersection property, and an ultrafilter containing it, from Lemma 1.1(a), lies in every \(\overline{B_j}\). \(\square\)

## 2. The semigroup of ultrafilters on a monoid

Let \(\mathcal S\) be a monoid, written multiplicatively with identity \(\epsilon\). For \(x\in\mathcal S\) and \(B\subseteq\mathcal S\) put \(x^{-1}B=\{y\in\mathcal S:xy\in B\}\); this is a preimage, not an inverse. For ultrafilters \(u,v\) define
\[
B\in uv\iff\{x\in\mathcal S:x^{-1}B\in v\}\in u .
\]

**Lemma 2.1.** This defines an associative multiplication on \(\beta\mathcal S\) with identity \(\delta_\epsilon\). For each \(v\), the map \(\rho_v(u)=uv\) is continuous. Moreover \(\delta_x\delta_y=\delta_{xy}\).

*Proof.* For fixed \(v\), the map \(B\mapsto\{x:x^{-1}B\in v\}\) commutes with finite intersections and complements, because \(x^{-1}\) does and \(v\) is an ultrafilter (Lemma 1.1(b)). So \(uv\) is a filter satisfying the criterion of Lemma 1.1(b), an ultrafilter. For three ultrafilters, both \((uv)w\) and \(u(vw)\) contain \(B\) exactly when
\[
\bigl\{x:\{y:\{z:xyz\in B\}\in w\}\in v\bigr\}\in u ,
\]
which proves associativity. The identity and the formula for principal ultrafilters follow from the definition. Finally \(\rho_v^{-1}(\overline B)=\overline{\{x:x^{-1}B\in v\}}\) is open. \(\square\)

A *left ideal* is a nonempty set \(L\subseteq\beta\mathcal S\) with \(\beta\mathcal S\,L\subseteq L\). For every \(v\), the set \(\beta\mathcal S\,v=\rho_v(\beta\mathcal S)\) is a compact left ideal.

**Proposition 2.2** (the corner group). There is an idempotent \(p\in\beta\mathcal S\), \(p^2=p\), such that \(G=p(\beta\mathcal S)p\) is a group with identity \(p\).

*Proof.* *A minimal compact left ideal.* The intersection of a chain of compact left ideals is compact, nonempty by Lemma 1.2 and the finite intersection property, and a left ideal. By Zorn's lemma there is a compact left ideal \(L_0\) containing no smaller one. For \(v\in L_0\), the compact left ideal \(\beta\mathcal S\,v\) lies in \(L_0\), so
\[
\beta\mathcal S\,v=L_0\qquad(v\in L_0).
\]

*An idempotent.* The set \(L_0\) is closed under multiplication. By Zorn's lemma again it contains a nonempty compact subsemigroup \(H_0\) containing no smaller one. Let \(x\in H_0\). The set \(H_0x=\rho_x(H_0)\) is compact, contained in \(H_0\), and closed under multiplication, since \((ax)(bx)=(axb)x\). So \(H_0x=H_0\), and in particular \(x=yx\) for some \(y\in H_0\). The set \(\{y\in H_0:yx=x\}\) is therefore nonempty; it is closed, being \(H_0\cap\rho_x^{-1}(\{x\})\), hence compact, and closed under multiplication. By minimality it is all of \(H_0\), so \(x^2=x\). Let \(p\) be this idempotent.

*The corner.* The set \(G=p(\beta\mathcal S)p\) is closed under multiplication, and \(p\) is an identity for it, because \(p^2=p\). Every \(y\in G\) lies in \(L_0\): \(y=pwp\), and \(wp\in L_0\) because \(p\in L_0\) and \(L_0\) is a left ideal. So \(\beta\mathcal S\,y=L_0\ni p\), and \(p=vy\) for some \(v\). Since \(py=y\),
\[
(pvp)\,y=pv(py)=pvy=p .
\]
So every element of \(G\) has a left inverse in \(G\). In a monoid with this property, if \(ay=p\) and \(ba=p\), then \(b=b(ay)=(ba)y=y\), so \(ya=p\) as well: left inverses are inverses, and \(G\) is a group. \(\square\)

## 3. Realizing products by strings

For the rest of the lesson \(\mathcal S\) is the monoid of finite strings over an alphabet, with concatenation and the empty string \(\epsilon\).

**Lemma 3.1** (simultaneous realization). Let \(q_{i,j}\in\beta\mathcal S\) for \(1\le i\le s\) and \(1\le j\le M\). Suppose that each column \(j\) has one of two forms:

1. *common*: \(q_{i,j}=q_j\) does not depend on \(i\);
2. *principal*: \(q_{i,j}=\delta_{z_{i,j}}\) for prescribed strings \(z_{i,j}\).

If \(B\subseteq\mathcal S\) belongs to \(q_{i,1}q_{i,2}\cdots q_{i,M}\) for every \(i\), then there are strings \(x_{i,j}\), equal for all \(i\) in each common column and equal to \(z_{i,j}\) in each principal column, such that \(x_{i,1}x_{i,2}\cdots x_{i,M}\in B\) for every \(i\).

*Proof.* Choose the strings column by column from the left. Before column \(j\), let \(P_i\) be the concatenation of the strings chosen in row \(i\), with \(P_i=\epsilon\) at the start, and keep the invariant
\[
\begin{gathered}
P_i^{-1}B\in q_{i,j}q_{i,j+1}\cdots q_{i,M}\\
(1\le i\le s).
\end{gathered}
\]
Put \(v_i=q_{i,j+1}\cdots q_{i,M}\), or \(v_i=\delta_\epsilon\) if \(j=M\). By the definition of the product, the set \(E_i=\{x:x^{-1}(P_i^{-1}B)\in v_i\}\) belongs to \(q_{i,j}\). In a common column, \(E_1\cap\dots\cap E_s\) belongs to the ultrafilter \(q_j\), so it is nonempty; choose one string \(x\) in it for all rows. In a principal column, \(z_{i,j}\in E_i\); choose \(x_{i,j}=z_{i,j}\). In both cases \((P_ix_{i,j})^{-1}B=x_{i,j}^{-1}(P_i^{-1}B)\in v_i\), which is the invariant for the next column. After the last column the invariant says \(P_i^{-1}B\in\delta_\epsilon\), that is, \(P_i\in B\). \(\square\)

## 4. Exercises

**4.1** (easy). Show that a principal ultrafilter \(\delta_x\) is an isolated point of \(\beta X\), and that the principal ultrafilters are dense in \(\beta X\).

**4.2** (medium). For the monoid \(\mathcal S\) of strings over a nonempty alphabet, show that \(\delta_x\) is not an idempotent unless \(x=\epsilon\). Show that every idempotent \(p\ne\delta_\epsilon\) of \(\beta\mathcal S\) is nonprincipal.

**4.3** (medium). Let \(p\) be an idempotent and \(B\in p\). Show that \(\{x\in B:x^{-1}B\in p\}\) belongs to \(p\).

**4.4** (easy). In Lemma 3.1, why does the argument fail if a column were allowed to have different nonprincipal ultrafilters in different rows?

## 5. Solutions

**4.1.** \(\overline{\{x\}}=\{\delta_x\}\), since an ultrafilter containing \(\{x\}\) contains every set containing \(x\). A nonempty open set contains a nonempty set \(\overline B\); then \(B\ne\varnothing\), and \(\delta_x\in\overline B\) for every \(x\in B\).

**4.2.** \(\delta_x\delta_x=\delta_{xx}\), and \(xx=x\) only for the empty string, since lengths add. If \(p=\delta_x\) were idempotent then \(x=\epsilon\).

**4.3.** \(B\in pp\) means \(\{x:x^{-1}B\in p\}\in p\); intersect with \(B\in p\).

**4.4.** In a column with different ultrafilters \(q_{1,j}\ne q_{2,j}\), the sets \(E_1\in q_{1,j}\) and \(E_2\in q_{2,j}\) may be disjoint, so no common string exists; and a principal column prescribes the strings. Only these two kinds of columns are needed in the next lesson.

## References

- [Ellis] R. Ellis, *Distal transformation groups*, Pacific Journal of Mathematics 8 (1958), 401–405. https://doi.org/10.2140/pjm.1958.8.401
- [OpenAI-ER] OpenAI, *A classification of finite Euclidean Ramsey configurations*, OpenAI Math Release preprint, 23 September 2026. https://github.com/openai/math/tree/main/preprints/A-classification-of-finite-Euclidean-Ramsey-configurations-September-23-2026
