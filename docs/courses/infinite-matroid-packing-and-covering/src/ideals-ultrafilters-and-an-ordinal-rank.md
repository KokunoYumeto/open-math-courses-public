# Ideals, ultrafilters and an ordinal rank

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The self-dual matroid built in this course lives on two copies of a countable set \(D\) cut into finite blocks of rapidly growing size. This lesson constructs the set-theoretic tools on \(D\): two ideals of "small" sets (Section 2), an ultrafilter that avoids the larger ideal (Section 3), an ordinal-valued rank on the members of the ultrafilter that can be raised at will inside intervals (Section 4), and a supply of reserved sets that separate any fewer than continuum many prescribed sets (Section 5). Notation is that of [Infinite matroids and the packing/covering conjecture](infinite-matroids-and-the-conjecture.md).

We work in ZFC. From the core course [Mathematical Logic, Set Theory, and Computability](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C80), whose set theory text is Button's *Set Theory: An Open Introduction* in the Open Logic Project [OLP], we use: every nonempty set of ordinals has a least element (Proposition 10.2); transfinite recursion (Theorem 11.4); every set has a cardinality, an initial ordinal equinumerous with it (Lemma 14.2), and infinite cardinals are limit ordinals (Corollary 14.10); \(\kappa\oplus\lambda=\kappa\otimes\lambda=\max(\kappa,\lambda)\) for infinite cardinals (Theorem 15.11), and a union of at most \(\kappa\) sets of size at most \(\kappa\) has size at most \(\kappa\) for infinite \(\kappa\) (Proposition 15.12); Cantor's theorem (Theorem 5.16); and the equivalence of choice with the well-ordering principle (Theorem 16.6). Write \(\mathfrak c=2^{\aleph_0}\) for the cardinality of \(\{0,1\}^{\mathbb N}\), regarded as an initial ordinal.

**Lemma 0.1** (Counting). (a) \(3\mathfrak c=\mathfrak c\). (b) If \(\lambda<\mathfrak c\), a union of at most \(\lambda\) finite sets has cardinality at most \(\max(\lambda,\aleph_0)<\mathfrak c\). (c) If \(\gamma<\mathfrak c\) is an ordinal, then \(|\gamma+1|<\mathfrak c\).

*Proof.* (a) Theorem 15.11 with \(\kappa=\lambda=\mathfrak c\), twice. (b) Proposition 15.12 with \(\kappa=\max(\lambda,\aleph_0)\), which is less than \(\mathfrak c\) because \(\lambda<\mathfrak c\) and \(\aleph_0<2^{\aleph_0}\) by Cantor's theorem. (c) \(\mathfrak c\) is a limit ordinal, so \(\gamma+1<\mathfrak c\), and an initial ordinal is not equinumerous with a smaller ordinal. \(\square\)

## 1. Blocks and the density ideal

For \(m\ge0\) let
\[
D_m=\{m\}\times\{0,1\}^{\{0,1\}^m},\qquad D=\bigcup_{m\ge0}D_m,\qquad w_m=|D_m|=2^{2^m}.
\]
The sets \(D_m\), the *blocks*, are finite and disjoint, and \(D\) is countably infinite. Each element of \(D_m\) is a pair \((m,f)\) with \(f:\{0,1\}^m\to\{0,1\}\).

**Lemma 1.1** (Block growth). \(w_m\ge2\sum_{j<m}w_j\) for every \(m\ge1\).

*Proof.* For \(m=1\): \(w_1=4=2w_0\). If it holds for \(m\), then \(2\sum_{j\le m}w_j\le w_m+2w_m=3w_m\le w_m^2=w_{m+1}\), since \(w_m\ge4\). \(\square\)

An **ideal** on a set \(S\) is a family of subsets closed under subsets and finite unions; a set not in the ideal is **positive** for it. The **density ideal** is
\[
\mathcal J=\Bigl\{X\subseteq D:\frac{|X\cap D_m|}{w_m}\to0\Bigr\}.
\]
It is a proper ideal containing every finite set. Let \(L\) and \(R\) be two labelled copies of \(D\) and \(E_0=L\mathbin{\dot\cup}R\). A set \(X\subseteq E_0\) has two *slices* \(X_L,X_R\subseteq D\). Let \(W_m\) be the union of the two copies of \(D_m\) and \(\mathcal J_0\) the ideal of sets with both slices in \(\mathcal J\); since the density of \(X\) in \(W_m\) is the average of its two slice densities, \(X\in\mathcal J_0\) exactly when \(|X\cap W_m|/|W_m|\to0\).

## 2. Independent columns and a larger ideal

**Lemma 2.1** (Independent columns). There are subsets \(A_t,B_t,G_t\subseteq D\), for \(t<\mathfrak c\), with the following property. For any \(r\) distinct sets among them (the *columns*) and any prescription of membership or non-membership in each, the proportion of \(D_m\) satisfying the prescription is exactly \(2^{-r}\) for all large \(m\).

*Proof.* By Lemma 0.1(a) we can assign pairwise distinct infinite binary sequences \(h\) to the \(3\mathfrak c\) columns. Put \((m,f)\) in the column with sequence \(h\) exactly when \(f(h\upharpoonright m)=1\), where \(h\upharpoonright m\) is the initial segment of length \(m\). For finitely many distinct sequences, their initial segments of length \(m\) are distinct once \(m\) is large. Prescribing the values of \(f\) at \(r\) distinct arguments leaves \(2^{2^m-r}\) of the \(2^{2^m}\) functions. \(\square\)

Define
\[
\mathcal K=\Bigl\{X\subseteq D:X\cap\bigcap_{t\in\Phi}A_t\in\mathcal J\ \text{for some finite }\Phi\subseteq\mathfrak c\Bigr\},
\]
where the empty intersection is \(D\). It is closed under subsets, and under finite unions because enlarging \(\Phi\) keeps the defining condition. It contains \(\mathcal J\) and every complement \(D\setminus A_t\). Write \(X\subseteq_{\mathcal K}Y\) if \(X\setminus Y\in\mathcal K\), and let \(\mathcal K_0\) be the ideal of subsets of \(E_0\) with both slices in \(\mathcal K\).

**Lemma 2.2** (Patterns are positive). Let \(P\) be the set of points of \(D\) lying in \(A_t\) for \(t\) in a finite set \(\Phi_1\), and lying in or outside \(G_t\) as prescribed for \(t\) in a finite set \(\Phi_2\). Then \(P\notin\mathcal K\). In particular \(D\notin\mathcal K\), so \(\mathcal K\) is proper.

*Proof.* For every finite \(\Phi\), \(P\cap\bigcap_{t\in\Phi}A_t\) is again given by a prescription on finitely many distinct columns, so by Lemma 2.1 it has a fixed positive proportion of \(D_m\) for large \(m\), and it is not in \(\mathcal J\). \(\square\)

## 3. An ultrafilter avoiding the larger ideal

A **filter** on a set \(S\) is a nonempty family of subsets, closed under supersets and finite intersections, not containing \(\varnothing\). An **ultrafilter** is a filter containing \(X\) or \(S\setminus X\) for every \(X\subseteq S\). A family has the **finite intersection property** if all its finite intersections are nonempty (the empty intersection being \(S\)).

**Lemma 3.1** (Ultrafilter extension). Every family of subsets of \(S\) with the finite intersection property is contained in an ultrafilter.

*Proof.* Let \(\mathcal F\) have the property, and well-order the subsets of \(S\) as \((X_\alpha)_{\alpha<\kappa}\) (Theorem 16.6). By transfinite recursion put \(\mathcal F_0=\mathcal F\), \(\mathcal F_{\alpha+1}=\mathcal F_\alpha\cup\{X_\alpha\}\) if this has the finite intersection property and \(\mathcal F_\alpha\cup\{S\setminus X_\alpha\}\) otherwise, and \(\mathcal F_\lambda=\bigcup_{\alpha<\lambda}\mathcal F_\alpha\) for limit \(\lambda\). The property is preserved: if both extensions failed, there would be finite \(\mathcal A,\mathcal A'\subseteq\mathcal F_\alpha\) with \(\bigcap\mathcal A\cap X_\alpha=\varnothing=\bigcap\mathcal A'\cap(S\setminus X_\alpha)\), so \(\bigcap(\mathcal A\cup\mathcal A')=\varnothing\); and at limits every finite subfamily lies in an earlier stage. The final family \(\mathcal G\) contains \(X\) or \(S\setminus X\) for every \(X\). The sets containing a finite intersection of members of \(\mathcal G\) form a filter containing \(\mathcal F\) and one of \(X\), \(S\setminus X\) for every \(X\). \(\square\)

Call \(Z\subseteq D\) *forbidden* if \(Z\subseteq_{\mathcal K}G_t\) for infinitely many \(t\).

**Lemma 3.2** (The ultrafilter). There is an ultrafilter \(\mathcal U\) on \(D\) containing no member of \(\mathcal K\), containing every \(G_t\), and such that for every \(X\in\mathcal U\),
\[
\{t<\mathfrak c:X\subseteq_{\mathcal K}G_t\}\ \text{is finite}. \tag{3.1}
\]

*Proof.* Consider the family of all complements of members of \(\mathcal K\), all \(G_t\), and all complements of forbidden sets. A finite subfamily consists of complements \(D\setminus N_k\), whose intersection is \(D\setminus N\) with \(N=\bigcup_kN_k\in\mathcal K\); sets \(G_t\) for \(t\) in a finite \(\Phi\); and complements of forbidden sets \(Z_1,\dots,Z_q\). Choose distinct indices \(t_1,\dots,t_q\notin\Phi\) with \(Z_j\subseteq_{\mathcal K}G_{t_j}\), possible since each \(Z_j\) has infinitely many such indices. The pattern
\[
P=\bigcap_{t\in\Phi}G_t\cap\bigcap_{j=1}^q(D\setminus G_{t_j})
\]
is \(\mathcal K\)-positive by Lemma 2.2, and \(P\cap Z_j\subseteq Z_j\setminus G_{t_j}\in\mathcal K\). If \(P\setminus(N\cup Z_1\cup\dots\cup Z_q)\) were in \(\mathcal K\), then \(P\) would be a finite union of members of \(\mathcal K\). So this set is nonempty, and it lies in the finite intersection. By Lemma 3.1 the family extends to an ultrafilter \(\mathcal U\). It contains the complement of every member of \(\mathcal K\), hence no member of \(\mathcal K\), and the complement of every forbidden set, hence no forbidden set, which is (3.1). \(\square\)

Fix such a \(\mathcal U\). Members of \(\mathcal U\) are called **large**, other subsets of \(D\) **small**. Large sets are \(\mathcal K\)-positive, hence \(\mathcal J\)-positive, and complements of members of \(\mathcal K\) are large.

## 4. An ordinal rank

The family \(\mathcal U\) has at most \(\mathfrak c\) members, since \(D\) is countable; list it, with repetitions, as \((F_\xi)_{\xi<\mathfrak c}\). For a large \(X\) define
\[
\rho(X)=\min\{\xi<\mathfrak c:F_\xi\subseteq_{\mathcal K}X\},
\]
which exists because \(X\) itself occurs in the list (Proposition 10.2). This *ordinal rank* is unrelated to the rank of a matroid.

**Lemma 4.1** (Invariance and monotonicity). If \(X\mathbin\triangle Y\in\mathcal K\), then \(X\) is large exactly when \(Y\) is, and then \(\rho(X)=\rho(Y)\). If \(X,Y\) are large and \(X\subseteq_{\mathcal K}Y\), then \(\rho(X)\ge\rho(Y)\).

*Proof.* The complement of \(X\mathbin\triangle Y\) is large; its intersection with a large \(X\) is large and contained in \(Y\). The indices allowed in the two minima are the same, because \(\subseteq_{\mathcal K}\) is unaffected by changes in \(\mathcal K\). If \(F_\xi\subseteq_{\mathcal K}X\subseteq_{\mathcal K}Y\), then \(F_\xi\setminus Y\subseteq(F_\xi\setminus X)\cup(X\setminus Y)\in\mathcal K\); so every index allowed for \(X\) is allowed for \(Y\). \(\square\)

**Lemma 4.2** (Raising the rank). Let \(s\subseteq X\subseteq D\) with \(s\) small and \(X\) large, and let \(\gamma<\mathfrak c\). There is a large \(u\) with \(s\subseteq u\subseteq X\) and \(\rho(u)>\gamma\).

*Proof.* For \(\xi\le\gamma\), the set \(Y_\xi=F_\xi\cap(X\setminus s)\) is large, so by (3.1) only finitely many \(t\) have \(Y_\xi\subseteq_{\mathcal K}G_t\). The union over \(\xi\le\gamma\) of these finite sets has fewer than \(\mathfrak c\) elements (Lemma 0.1(b), (c)); choose \(t\) outside it and put \(u=s\cup(X\cap G_t)\). It is large, as it contains \(X\cap G_t\), and \(s\subseteq u\subseteq X\). If \(F_\xi\subseteq_{\mathcal K}u\) for some \(\xi\le\gamma\), then
\[
Y_\xi\setminus G_t=F_\xi\cap X\cap(D\setminus s)\cap(D\setminus G_t)\subseteq F_\xi\setminus u\in\mathcal K,
\]
so \(Y_\xi\subseteq_{\mathcal K}G_t\), contrary to the choice of \(t\). Hence \(\rho(u)>\gamma\). \(\square\)

## 5. Simultaneous reservations

For \(t<\mathfrak c\) define the subsets of \(E_0\), with the same labels in both copies,
\[
H_{t,0}=\bigl((D\setminus A_t)\cap(D\setminus B_t)\bigr)\times\{L,R\},\qquad H_{t,1}=\bigl((D\setminus A_t)\cap B_t\bigr)\times\{L,R\}.
\]
They are disjoint and belong to \(\mathcal K_0\), because their slices lie in \(D\setminus A_t\in\mathcal K\).

**Lemma 5.1** (Simultaneous reservations). Let \(\mathscr S\) be a family of fewer than \(\mathfrak c\) subsets of \(E_0\), each \(\mathcal J_0\)-positive. There is \(t<\mathfrak c\) with \(S\cap H_{t,0}\notin\mathcal J_0\) and \(S\cap H_{t,1}\notin\mathcal J_0\) for every \(S\in\mathscr S\).

*Proof.* Fix \(S\in\mathscr S\) and \(\varepsilon>0\) such that \(|S\cap W_m|\ge\varepsilon|W_m|\) for infinitely many \(m\). Call \(t\) *bad* for \(S\) if \(S\cap H_{t,0}\) or \(S\cap H_{t,1}\) lies in \(\mathcal J_0\). Let \(t_1,\dots,t_q\) be distinct bad indices and choose \(k_i\) with \(S\cap H_{t_i,k_i}\in\mathcal J_0\); put \(H_i=H_{t_i,k_i}\). Avoiding \(H_i\) excludes one of the four membership patterns in the two columns \(A_{t_i},B_{t_i}\); these \(2q\) columns are distinct, so by Lemma 2.1 the points of \(W_m\) outside \(H_1\cup\dots\cup H_q\) have proportion exactly \((3/4)^q\) for large \(m\). Every point of \(S\cap W_m\) avoids all \(H_i\) or lies in some \(S\cap H_i\), so
\[
\frac{|S\cap W_m|}{|W_m|}\le\Bigl(\frac34\Bigr)^q+\sum_{i=1}^q\frac{|S\cap H_i\cap W_m|}{|W_m|},
\]
and the sum tends to zero. Along the infinitely many \(m\) with density at least \(\varepsilon\), this gives \(\varepsilon\le(3/4)^q\). So there are only finitely many bad indices for \(S\). The union of these finite sets over \(S\in\mathscr S\) has fewer than \(\mathfrak c\) elements (Lemma 0.1(b)); any \(t\) outside it works. \(\square\)

## 6. Exercises

**6.1.** Show that \(\mathcal J\) is not a maximal ideal: find \(X\subseteq D\) with \(X\notin\mathcal J\) and \(D\setminus X\notin\mathcal J\).

**6.2.** Show that a nonprincipal ultrafilter on \(D\) (one containing no finite set) contains every cofinite set, and that \(\mathcal U\) of Lemma 3.2 is nonprincipal.

**6.3.** Show that for every ordinal \(\gamma<\mathfrak c\) there is a large set \(u\) with \(\rho(u)>\gamma\), so \(\rho\) is unbounded below \(\mathfrak c\).

**6.4.** Why is the condition "fewer than \(\mathfrak c\)" in Lemma 5.1 needed? Give a family of \(\mathfrak c\) sets for which no index works.

## 7. Solutions

**6.1.** Take \(X=A_0\): by Lemma 2.1 both \(A_0\) and its complement have proportion \(\frac12\) in \(D_m\) for large \(m\).

**6.2.** If \(X\) is cofinite and \(X\notin\mathcal U\), then \(D\setminus X\in\mathcal U\) is finite. Finite sets lie in \(\mathcal J\subseteq\mathcal K\), and \(\mathcal U\) contains no member of \(\mathcal K\).

**6.3.** Apply Lemma 4.2 with \(s=\varnothing\), which is small, and \(X=D\).

**6.4.** For each \(t\), the set \(S_t=H_{t,1}\cup(E_0\setminus(H_{t,0}\cup H_{t,1}))\) is \(\mathcal J_0\)-positive and meets \(H_{t,0}\) in the empty set, so \(t\) is bad for \(S_t\). The family \(\{S_t:t<\mathfrak c\}\) has \(\mathfrak c\) members and every index is bad for one of them.

## References

- [OpenAI-IM] OpenAI, *A counterexample to the infinite matroid packing/covering conjecture*, OpenAI Math Release preprint, 24 September 2026. https://github.com/openai/math/blob/main/preprints/A-Counterexample-to-the-Infinite-Matroid-Packing-Covering-Conjecture-September-24-2026/paper.pdf
- [OLP] T. Button, *Set Theory: An Open Introduction*, Open Logic Project (core course Mathematical Logic, Set Theory, and Computability). https://builds.openlogicproject.org/courses/set-theory/settheory-screen.pdf
- [BG] N. Bowler and S. Geschke, *Self-dual uniform matroids on infinite sets*, Proceedings of the AMS 144 (2016); author version on the author's page. https://www.math.uni-hamburg.de/home/geschke/papers/UniformMatroid7.pdf
