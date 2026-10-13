# Alignment of lists: patterns, minimax and Ramsey's theorem

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The third lesson of this course gave, for a chain, a short list of answers for every small set of layers, such that the lists of two sets of layers are disjoint if one set lies entirely before the other. This lesson and the next prove a statement about such families of lists that has nothing to do with graphs: one can choose a random set \(B\) of \(s\) layers, with a law that does not depend on the lists, such that with high probability every answer can be given a layer of \(B\) that belongs to all sets inside \(B\) on whose lists the answer stands. This is the alignment theorem of [OpenAI-I].

This lesson states the theorem, treats the cases \(s\le3\) by hand, and reduces the general case to a statement about random patterns whose law depends only on the order of the layers. The reduction uses the minimax theorem for finite games and Ramsey's theorem; both are proved here.

- The alignment theorem (Theorem 1.1), bad sets (Lemma 1.2), the cases \(s\le2\) and \(s=3\) (Proposition 1.6).
- Patterns: families of lists without the names of the labels (Section 2).
- The minimax theorem (Theorem 3.2).
- Ramsey's theorem (Theorem 4.1).
- If the theorem fails, there are laws of patterns that depend only on the order (Proposition 5.1).

The lesson follows [OpenAI-I, Sections 5 and 8]. It needs only finite sets, finite probability, and compact sets in \(\mathbb R^n\). The theorem is proved in the next lesson, [Order-invariant arrays and the common index](order-invariant-arrays-and-the-common-index.md).

## 1. The alignment theorem

Let \(r\ge s\ge1\) and \(d\ge1\) be integers, and let \(\mathcal I\) be the set of the nonempty subsets of \([r]=\{1,\dots,r\}\) with at most \(s\) elements.

**Definition.** A *family of lists* on \([r]\) consists of a set \(M_*\) of *labels* and, for every \(I\in\mathcal I\), a set \(A_I\subset M_*\) with at most \(d\) elements, the *list* of \(I\). It *respects separation* if \(A_I\cap A_J=\varnothing\) whenever \(\max I<\min J\). A set \(B\subset[r]\) with \(s\) elements is *aligned* for the family if there is a map \(a:M_*\to B\) with \(a(A_I)\subset I\) for every nonempty \(I\subset B\), and *bad* otherwise.

**Theorem 1.1** (alignment, [OpenAI-I]). For all integers \(s,d\ge1\) and every \(\eta>0\) there are an integer \(r\ge s\) and a probability law \(\mu\) with rational values on the subsets of \([r]\) with \(s\) elements, such that for every family of lists on \([r]\) that respects separation
\[
\Pr_{B\sim\mu}\bigl(B\text{ is bad}\bigr)\le\eta .
\]

The law \(\mu\) is chosen before the family, and it does not depend on the set of the labels. The lists of the third lesson respect separation for most chains, with \(M_*=M_r\), the set of answers of the last layer.

For a label \(x\), the sets \(I\in\mathcal I\) with \(x\in A_I\) are the *occurrence sets* of \(x\). If the family respects separation, no two occurrence sets \(I,J\) of one label have \(\max I<\min J\).

**Lemma 1.2.** A set \(B\) is bad if and only if there is a label that has an occurrence set inside \(B\) and whose occurrence sets inside \(B\) have an empty intersection.

**Proof.** The condition on \(a\) says: for every label \(x\), the layer \(a(x)\) lies in every occurrence set of \(x\) inside \(B\). For a label without occurrence sets inside \(B\) any element of \(B\) will do. For the others, a suitable \(a(x)\) exists exactly if the intersection of the occurrence sets inside \(B\) is not empty; the choices for different labels do not interfere. \(\blacksquare\)

**Example 1.3** (\(s\le2\)). For \(s=1\) the only nonempty subset of \(B=\{b\}\) is \(B\), and no set is bad. For \(s=2\) and \(B=\{a<b\}\), the occurrence sets of a label inside \(B\) are among \(\{a\}\), \(\{b\}\), \(\{a,b\}\), and not both \(\{a\}\) and \(\{b\}\) if the family respects separation. So they have a common element, and no set is bad.

**Example 1.4** (\(s=3\)). Let \(A_{\{1,3\}}=A_{\{2\}}=\{x\}\), and let the other lists be empty. The family respects separation, since neither of \(\{1,3\}\), \(\{2\}\) lies before the other. The set \(B=\{1,2,3\}\) is bad. So for \(s=3\) the theorem needs \(r>3\).

**Lemma 1.5.** Let a family respect separation, and let \(B=\{a<b<c\}\). Then \(B\) is bad if and only if there is a label \(x\) with

- (i) \(x\in A_{\{a,c\}}\cap A_{\{b\}}\), or
- (ii) \(x\in A_{\{a,c\}}\cap A_{\{b,c\}}\cap A_{\{a,b\}}\).

**Proof.** In both cases the named sets have an empty intersection, so \(B\) is bad by Lemma 1.2. Conversely, let \(x\) be a label as in Lemma 1.2, and let \(p\) be the largest of the minima of its occurrence sets inside \(B\). Every occurrence set \(I\) inside \(B\) has \(\min I\le p\le\max I\); the second inequality holds because \(I\) does not lie before an occurrence set with the minimum \(p\).

If \(p=a\), all occurrence sets contain \(a\). If \(p=c\), then \(\{c\}\) is an occurrence set and all others have the maximum \(c\). Both contradict the empty intersection. So \(p=b\): one of \(\{b\}\), \(\{b,c\}\) is an occurrence set. Some occurrence set \(I\) does not contain \(b\). Then \(\min I<b<\max I\), so \(I=\{a,c\}\). If \(\{b\}\) is an occurrence set, this is (i). Otherwise \(\{b,c\}\) is one, and since \(c\in\{a,c\}\cap\{b,c\}\), some occurrence set \(K\) does not contain \(c\). Then \(\max K=b\), because \(b=p\le\max K\); so \(K\) is \(\{b\}\) or \(\{a,b\}\), and it is \(\{a,b\}\) in this case. This is (ii). \(\blacksquare\)

**Proposition 1.6** (\(s=3\)). Let \(r\ge4\), and let \(B_b=\{1,b,r\}\) for \(1<b<r\). For every family of lists on \([r]\) that respects separation, at most \(d\) of the \(r-2\) sets \(B_b\) are bad. So Theorem 1.1 holds for \(s=3\) with every integer \(r\ge4\) such that \(r\ge2+d/\eta\), and the uniform law on these sets.

**Proof.** If \(B_b\) is bad, Lemma 1.5 gives a label \(x\in A_{\{1,r\}}\) for which (i) or (ii) holds with \(a=1\), \(c=r\). In both cases \(x\) has an occurrence set with the maximum \(b\), namely \(\{b\}\) or \(\{1,b\}\), and an occurrence set with the minimum \(b\), namely \(\{b\}\) or \(\{b,r\}\). If the same label \(x\) did this for \(b\) and for \(b'>b\), its occurrence set with the maximum \(b\) would lie before its occurrence set with the minimum \(b'\). So every label of \(A_{\{1,r\}}\) accounts for at most one \(b\), and this list has at most \(d\) labels. \(\blacksquare\)

For \(s\ge4\) this course gives no such direct argument. The proof of Theorem 1.1 in the general case is indirect and gives no bound for \(r\).

## 2. Patterns

Whether a family respects separation, and which sets are bad, depends only on which entries of the lists are equal. This is recorded in a finite object.

**Definition.** Let \(X\) be a finite set of integers or of rational numbers, with its order, and let \(\mathcal I(X)\) be the set of its nonempty subsets with at most \(s\) elements. A *slot* is a pair \((I,k)\) with \(I\in\mathcal I(X)\) and \(1\le k\le d\). A *pattern* on \(X\) consists of

- a number \(n_I\in\{0,1,\dots,d\}\) for every \(I\in\mathcal I(X)\); the slots \((I,k)\) with \(k\le n_I\) are *occupied*;
- an equivalence relation on the set of the occupied slots, for which two different slots \((I,k)\), \((I,k')\) of the same \(I\) are never equivalent.

An equivalence class of occupied slots is a *label* of the pattern, and the sets \(I\) of its slots are its *occurrence sets*. The pattern *respects separation* if no label has two occurrence sets \(I,J\) with \(\max I<\min J\). A subset \(B\subset X\) with \(s\) elements is *bad* for the pattern if some label has an occurrence set inside \(B\) and its occurrence sets inside \(B\) have an empty intersection. Let \(\mathcal P(X)\) be the finite set of the patterns on \(X\) that respect separation, and \(\mathcal P_t=\mathcal P([t])\).

A family of lists on \([r]\) has a pattern, once every list is written in some order as \(A_I=\{x_{I,1},\dots,x_{I,n_I}\}\): the slots \((I,k)\) and \((I',k')\) are equivalent if \(x_{I,k}=x_{I',k'}\). The labels of the pattern correspond to the labels that stand on some list, with the same occurrence sets. So, by Lemma 1.2:

**Lemma 2.1.** A family of lists respects separation if and only if its pattern does, and a set \(B\) is bad for the family if and only if it is bad for the pattern. Every pattern on \([r]\) is the pattern of a family of lists, with its labels as the set \(M_*\).

So Theorem 1.1 is a statement about the finite set \(\mathcal P_r\).

**Restriction and standard form.** For a pattern \(C\) on \(X\) and a subset \(X'\subset X\), the *restriction* \(C|_{X'}\) keeps the numbers \(n_I\) and the relation for the slots with \(I\subset X'\). It respects separation if \(C\) does, and a set \(B\subset X'\) is bad for \(C|_{X'}\) if and only if it is bad for \(C\), because badness of \(B\) involves only the slots with \(I\subset B\). An increasing bijection \(g:X\to Y\) carries a pattern \(C\) on \(X\) to a pattern \(g(C)\) on \(Y\), by renaming the elements; it preserves separation and bad sets. If \(X\) has \(t\) elements, the increasing bijection from \(X\) to \([t]\) carries \(C\) to a pattern in \(\mathcal P_t\), the *standard form* of \(C\). Restriction and standard form are compatible: for \(X''\subset X'\subset X\), the standard form of \(C|_{X''}\) is obtained from the standard form of \(C|_{X'}\) by restricting to the image of \(X''\) and taking the standard form.

## 3. The minimax theorem

**Lemma 3.1.** Let \(Z\subset\mathbb R^n\) be a nonempty closed convex set that does not contain \(0\). Then there is a point \(y\in Z\) with
\[
\langle y,z\rangle\ge|y|^2>0\qquad\text{for all }z\in Z .
\]

**Proof.** Take a point \(z_0\in Z\). The set of the points of \(Z\) with a norm of at most \(|z_0|\) is closed and bounded, so the norm has a least value on it, at a point \(y\); this is the least value on \(Z\), and \(y\ne0\). Let \(z\in Z\) and \(0<\lambda\le1\). The point \(y+\lambda(z-y)\) lies in \(Z\), so
\[
\begin{aligned}
|y|^2&\le|y+\lambda(z-y)|^2\\
&=|y|^2+2\lambda\langle y,z-y\rangle+\lambda^2|z-y|^2 .
\end{aligned}
\]
Divide by \(\lambda\) and let \(\lambda\to0\): \(\langle y,z-y\rangle\ge0\). \(\blacksquare\)

Let \(\Delta_n\subset\mathbb R^n\) be the set of the vectors with entries \(\ge0\) and the sum \(1\), the probability laws on \([n]\).

**Theorem 3.2** (minimax; J. von Neumann). Let \(b(i,j)\), \(1\le i\le n\), \(1\le j\le N\), be real numbers. Then
\[
\begin{aligned}
&\min_{\nu\in\Delta_n}\ \max_{1\le j\le N}\ \sum_{i}\nu_i\,b(i,j)\\
&\qquad=\max_{\rho\in\Delta_N}\ \min_{1\le i\le n}\ \sum_{j}b(i,j)\,\rho_j .
\end{aligned}
\]

**Proof.** The function \(\nu\mapsto\max_j\sum_i\nu_ib(i,j)\) is continuous on the compact set \(\Delta_n\), so the minimum \(w\) on the left exists; in the same way the maximum \(v\) on the right exists.

\(v\le w\): for all \(\nu\in\Delta_n\) and \(\rho\in\Delta_N\),
\[
\begin{aligned}
\min_i\sum_jb(i,j)\rho_j&\le\sum_{i,j}\nu_ib(i,j)\rho_j\\
&\le\max_j\sum_i\nu_ib(i,j),
\end{aligned}
\]
since a mean lies between the least and the largest of the numbers.

\(w\le v\): Let \(K\subset\mathbb R^n\) be the set of the vectors \(k(\rho)=(\sum_jb(i,j)\rho_j)_{i}\), \(\rho\in\Delta_N\); it is compact and convex. Let \(\mathbf 1=(1,\dots,1)\), let \(O\) be the set of the vectors \(e\in\mathbb R^n\) with all \(e_i\ge0\), and
\[
Z=\{k-w\mathbf 1-e:\ k\in K,\ e\in O\}.
\]
\(Z\) is convex. It is closed: if \(k_m-w\mathbf 1-e_m\to z\), a subsequence of the \(k_m\) converges to some \(k\in K\), and then \(e_m\) converges along it to \(k-w\mathbf 1-z\), which has entries \(\ge0\).

If \(0\in Z\), there is \(\rho\) with \(\sum_jb(i,j)\rho_j\ge w\) for all \(i\), and so \(v\ge w\).

Suppose \(0\notin Z\), and take \(y\) as in Lemma 3.1. For \(k\in K\), a coordinate \(i\) and \(\lambda\ge0\), the vector \(k-w\mathbf 1-\lambda\mathbf e_i\) lies in \(Z\), where \(\mathbf e_i\) is the \(i\)-th unit vector. So \(\langle y,k-w\mathbf 1\rangle-\lambda y_i>0\) for all \(\lambda\ge0\), which forces \(y_i\le0\). Since \(y\ne0\), the sum \(\Sigma\) of the \(y_i\) is negative, and \(\nu=y/\Sigma\) lies in \(\Delta_n\). For every \(j\), the column \(k=(b(i,j))_i\) lies in \(K\), and \(\langle y,k-w\mathbf 1\rangle>0\) becomes, after division by \(\Sigma<0\),
\[
\sum_i\nu_ib(i,j)-w<0 .
\]
So \(\max_j\sum_i\nu_ib(i,j)<w\), against the definition of \(w\). Hence \(0\in Z\). \(\blacksquare\)

In the words of games: the first player chooses a row with a law \(\nu\), the second a column with a law \(\rho\), and \(b\) is what the first pays. If for every law \(\nu\) some column costs more than \(\xi\), then one law \(\rho\) on the columns costs every row more than \(\xi\).

## 4. Ramsey's theorem

A *coloring* of the \(t\)-subsets of a set \(X\) with \(q\) colors gives every subset of \(X\) with \(t\) elements one of \(q\) colors. A subset \(H\subset X\) is *homogeneous* for it if all \(t\)-subsets of \(H\) have the same color.

**Theorem 4.1** (F. P. Ramsey). For all integers \(t,q,k\ge1\) there is an integer \(R_t(q,k)\) such that every coloring of the \(t\)-subsets of a totally ordered set with at least \(R_t(q,k)\) elements with \(q\) colors has a homogeneous subset with \(k\) elements.

**Proof.** For \(k<t\) every set with \(k\) elements is homogeneous, since it has no \(t\)-subsets; put \(R_t(q,k)=k\). Let \(k\ge t\). The proof is by induction on \(t\).

\(t=1\): among \(q(k-1)+1\) elements, some \(k\) have the same color.

From \(t\) to \(t+1\): put \(n=q(k-1)+1\), and define numbers \(a_n,a_{n-1},\dots,a_0\) by
\[
a_n=0,\qquad a_{i-1}=1+R_t(q,a_i) .
\]
Let \(X_0\) be a totally ordered set with at least \(a_0\) elements, and let a coloring of its \((t+1)\)-subsets with \(q\) colors be given. Choose in turn, for \(i=1,\dots,n\): the least element \(x_i\) of \(X_{i-1}\); and a subset \(X_i\subset X_{i-1}\setminus\{x_i\}\) with \(a_i\) elements that is homogeneous for the coloring of the \(t\)-subsets \(W\) of \(X_{i-1}\setminus\{x_i\}\) by the color of \(\{x_i\}\cup W\). This is possible because \(X_{i-1}\setminus\{x_i\}\) has at least \(a_{i-1}-1=R_t(q,a_i)\) elements. If \(a_i\ge t\), let \(\chi(i)\) be the common color of the sets \(\{x_i\}\cup W\), \(W\subset X_i\); otherwise let \(\chi(i)\) be any color.

Then \(x_1<x_2<\dots<x_n\), and \(x_j\in X_i\) for \(j>i\). So a \((t+1)\)-subset of \(\{x_1,\dots,x_n\}\) with the least element \(x_i\) has the form \(\{x_i\}\cup W\) with a \(t\)-subset \(W\) of \(X_i\), and its color is \(\chi(i)\). Among the \(n\) indices some \(k\) have the same value of \(\chi\). The \(k\) elements \(x_i\) with these indices form a homogeneous set. So \(R_{t+1}(q,k)=a_0\) has the property. \(\blacksquare\)

## 5. Laws that depend only on the order

Fix \(s,d\ge1\). For \(\xi>0\) consider the following statement.

**Statement \(\mathrm A(\xi)\).** There are an integer \(r\ge s\) and a probability law \(\nu\) on the subsets of \([r]\) with \(s\) elements such that \(\Pr_{B\sim\nu}(B\text{ is bad for }C)\le\xi\) for every pattern \(C\in\mathcal P_r\).

By Lemma 2.1, Theorem 1.1 is this statement with rational values of the law. A *law on \(\mathcal P_t\)* is a probability law on this finite set, that is, a random pattern. If \(C\) is a random pattern on \([u]\) and \(X\subset[u]\) has \(t\) elements, the standard form of \(C|_X\) is a random pattern on \([t]\).

**Proposition 5.1.** Let \(\xi>0\), and suppose that \(\mathrm A(\xi)\) is false. Then there are laws \(P_t\) on \(\mathcal P_t\), for all \(t\ge1\), with the following properties.

1. (Consistency.) If \(t\le u\), \(X\subset[u]\) has \(t\) elements and \(C\) has the law \(P_u\), then the standard form of \(C|_X\) has the law \(P_t\).
2. If \(C\) has the law \(P_s\), then \(\Pr([s]\text{ is bad for }C)\ge\xi\).

**Proof.** *Step 1: a law of patterns for every \(r\).* Let \(r\ge s\). Apply Theorem 3.2 to the matrix whose rows are the sets \(B\subset[r]\) with \(s\) elements, whose columns are the patterns \(C\in\mathcal P_r\), and with \(b(B,C)=1\) if \(B\) is bad for \(C\) and \(0\) otherwise. For a law \(\nu\) on the rows, \(\sum_B\nu_Bb(B,C)\) is the probability that \(B\) is bad for \(C\). Since \(\mathrm A(\xi)\) is false, the largest of these numbers over \(C\) is more than \(\xi\) for every \(\nu\); so the minimum \(w\) over \(\nu\), which is attained, is more than \(\xi\). By the theorem there is a law \(\rho_r\) on \(\mathcal P_r\) such that a random pattern \(C\) with this law has, for every \(B\),
\[
\Pr\bigl(B\text{ is bad for }C\bigr)\ge w>\xi .
\]

*Step 2: sets on which the law almost depends only on the order.* For a set \(X\subset[r]\) with \(t\) elements let \(\lambda_X\) be the law of the standard form of \(C|_X\), where \(C\) has the law \(\rho_r\); it is a law on \(\mathcal P_t\). Fix an integer \(k\ge s\). For \(1\le t\le k\), color the \(t\)-subsets \(X\) of \([r]\) by the family of integers
\[
\bigl(\lfloor k\,\lambda_X(C')\rfloor\bigr)_{C'\in\mathcal P_t} .
\]
There are at most \(q_t=(k+1)^{|\mathcal P_t|}\) colors, and two sets \(X,X'\) of the same color have \(|\lambda_X(C')-\lambda_{X'}(C')|<\tfrac1k\) for all \(C'\). Define \(n_k=k\) and \(n_{t-1}=R_t(q_t,n_t)\) for \(t=k,\dots,1\), with the numbers of Theorem 4.1, and let \(r=r_k=\max\{n_0,s\}\). Choose sets \([r]\supset X_1\supset\dots\supset X_k\) such that \(X_t\) has \(n_t\) elements and is homogeneous for the coloring of the \(t\)-subsets. Then \(H_k=X_k\) has \(k\) elements and is homogeneous for all \(k\) colorings.

For \(t\le k\) let \(P_t^{(k)}=\lambda_X\) for the set \(X\) of the first \(t\) elements of \(H_k\). Let \(t\le u\le k\) and let \(X\subset[u]\) have \(t\) elements. If \(C\) has the law \(P_u^{(k)}\), the standard form of \(C|_X\) has the law \(\lambda_{X'}\), where \(X'\subset H_k\) corresponds to \(X\) under the increasing bijection from \([u]\) to the first \(u\) elements of \(H_k\); this is the compatibility of restriction and standard form. Both \(X'\) and the set of the first \(t\) elements are \(t\)-subsets of \(H_k\). So, for every \(C'\in\mathcal P_t\), the probability \(e(C')\) that the standard form of \(C|_X\) is \(C'\) satisfies
\[
\bigl|e(C')-P_t^{(k)}(C')\bigr|<\tfrac1k .
\]
Also, by Step 1 and because restriction and standard form preserve bad sets,
\[
P_s^{(k)}\bigl([s]\text{ is bad}\bigr)>\xi .
\]

*Step 3: the limit.* Every \(P_t^{(k)}\), \(k\ge\max\{t,s\}\), is a point of the compact set of the laws on the finite set \(\mathcal P_t\). There are countably many pairs \((t,C')\). By the theorem of Bolzano and Weierstrass and a diagonal choice there is a sequence \(k_1<k_2<\dots\) along which \(P_t^{(k)}(C')\) converges for every \(t\) and every \(C'\in\mathcal P_t\). The limits \(P_t(C')\) form a law \(P_t\) on \(\mathcal P_t\). The probability that the standard form of \(C|_X\) is \(C'\), for \(C\) with the law \(P_u^{(k)}\), is a finite sum of values of \(P_u^{(k)}\). So the inequality of Step 2 gives (1) in the limit, and the last inequality gives (2). \(\blacksquare\)

By (1), the law of the restriction of a random pattern with the law \(P_u\) to a set \(X\) depends only on the number of the elements of \(X\), after the elements are renamed in their order. The next lesson uses these laws to build a random pattern on all rational numbers at once, and shows that it has no bad sets. This contradicts (2), so \(\mathrm A(\xi)\) is true for every \(\xi>0\).

## 6. Exercises

**6.1.** Let \(s=3\), \(d=1\), \(r=4\). Give two families of lists that respect separation such that for every law \(\nu\) on the four subsets of \([4]\) with three elements, one of the two families has \(\Pr_{B\sim\nu}(B\text{ is bad})\ge\tfrac12\). Compare with Proposition 1.6.

**6.2.** Let \(s=d=1\). List the patterns on \([2]\) and those that respect separation.

**6.3.** Compute both sides of Theorem 3.2 for the matrix with \(b(1,1)=b(2,2)=1\) and \(b(1,2)=b(2,1)=0\), and compare with the same expressions when \(\nu\) and \(\rho\) are restricted to the laws that give one row, or one column, the probability \(1\).

**6.4.** Let a label have the occurrence sets \(I_1,\dots,I_n\) in a family that respects separation, and let \(p\) be the largest of the numbers \(\min I_k\). Show that \(\min I_k\le p\le\max I_k\) for all \(k\). Give an example with \(p\notin I_k\) for some \(k\).

**6.5.** Show that \(R_1(q,k)=q(k-1)+1\) cannot be replaced by a smaller number, and that \(R_2(2,3)\le6\) can be taken in Theorem 4.1: every coloring of the pairs of six elements with two colors has a homogeneous set of three elements.

## 7. Solutions

**6.1.** Write \(ac\) for \(\{a,c\}\). Family 1: one label on the lists of \(13\), \(2\) and \(14\), a second label on the lists of \(24\) and \(3\). Family 2: one label on the lists of \(13\) and \(2\), a second label on the lists of \(14\), \(3\) and \(24\). In both, no two occurrence sets of a label lie one before the other, so separation is respected. By Lemma 1.5(i), family 1 makes \(123\) bad (\(13\) and \(2\)), \(124\) (\(14\) and \(2\)) and \(234\) (\(24\) and \(3\)); family 2 makes \(123\), \(134\) (\(14\) and \(3\)) and \(234\) bad. The two probabilities of a bad set add up to at least
\[
2\nu_{123}+2\nu_{234}+\nu_{124}+\nu_{134}\ge1 ,
\]
so one of them is at least \(\tfrac12\). Proposition 1.6 gives, for \(r=4\) and \(d=1\), the law with \(\nu_{124}=\nu_{134}=\tfrac12\) and the bound \(\tfrac12\). So \(\tfrac12\) is the best value for \(r=4\).

**6.2.** The slots are \((\{1\},1)\) and \((\{2\},1)\). The patterns: none occupied; only the first; only the second; both occupied and not equivalent; both occupied and equivalent. The last one has a label with the occurrence sets \(\{1\}\) and \(\{2\}\), and \(\max\{1\}<\min\{2\}\). So four of the five patterns respect separation.

**6.3.** For \(\nu=(\nu_1,\nu_2)\) the two column sums are \(\nu_1\) and \(\nu_2\); the larger is at least \(\tfrac12\), with equality for \(\nu=(\tfrac12,\tfrac12)\). So the left side is \(\tfrac12\), and by symmetry the right side is \(\tfrac12\). With laws that give one row the probability \(1\), the left expression is \(1\) (the column of that row costs \(1\)), and with one column of probability \(1\) the right expression is \(0\). The theorem needs the laws.

**6.4.** \(\min I_k\le p\) by the definition of \(p\). Let \(I_j\) be an occurrence set with \(\min I_j=p\). If \(\max I_k<p\), then \(I_k\) would lie before \(I_j\). An example is Example 1.4: the occurrence sets \(\{1,3\}\) and \(\{2\}\) have \(p=2\notin\{1,3\}\).

**6.5.** Color \(q(k-1)\) elements so that every color is used \(k-1\) times; then no \(k\) elements have the same color. For the second statement, take an element \(x\) of the six. Three of the five pairs that contain \(x\) have the same color, say the pairs \(\{x,y_1\}\), \(\{x,y_2\}\), \(\{x,y_3\}\) are red. If some pair \(\{y_i,y_j\}\) is red, then \(\{x,y_i,y_j\}\) is homogeneous; otherwise \(\{y_1,y_2,y_3\}\) is.

## References

- [OpenAI-I] OpenAI, *Hardness of finding large independent sets in three-colorable graphs*, OpenAI Math Release preprint, 24 September 2026, Sections 5 and 8. https://github.com/openai/math/tree/main/preprints/Hardness-of-finding-large-independent-sets-in-three-colorable-graphs-September-24-2026
