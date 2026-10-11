# Marked pivots and sign patterns

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The eighth lesson must control a set of labels that the rule's own random masks select. A union bound over all sets that *could* be selected works only if there are few of them. This lesson proves the counting statement behind that union bound. Take a fixed sequence of labels, each carrying a mark \(0\) or \(1\), and insert a few further labels anywhere, with any marks. Each label of a set \(V\) becomes spanned at some point of the combined sequence, and we record the mark found there. However long the fixed sequence is, the number of resulting mark vectors is bounded in terms of \(|V|\) and the number of insertions alone. The proof turns mark vectors into sign patterns of affine functions and counts these by a classical bound on hyperplane arrangements.

Matroid notation is that of [Prophets, matroids and an almighty adversary](prophets-matroids-and-an-almighty-adversary.md).

## 1. Sign patterns of affine functions

An affine function on \(\mathbb R^d\) is \(g(y)=a\cdot y+c\) with \(a\in\mathbb R^d\), \(c\in\mathbb R\); for \(d=0\), \(\mathbb R^0\) is a point and every function is constant. A *strict sign pattern* of affine functions \(g_1,\ldots,g_n\) is a vector \((\operatorname{sign}g_i(y))_{i\leq n}\in\{+,-\}^n\) for a point \(y\) at which no \(g_i\) vanishes. Let \(N(n,d)\) be the largest number of strict sign patterns of \(n\) affine functions on \(\mathbb R^d\), and write \(\binom n\ell=0\) for \(\ell>n\) or \(\ell<0\).

**Lemma 1.1 (sign patterns).** \(N(n,d)\leq\sum_{\ell=0}^d\binom n\ell\).

*Proof.* We show \(N(0,d)=1\), \(N(n,0)\leq1\), and, for \(n,d\geq1\), that \(N(n,d)\) is at most \(N(n-1,d)+N(n-1,d-1)\); the claim follows by induction from Pascal's rule \(\binom{n-1}\ell+\binom{n-1}{\ell-1}=\binom n\ell\). With no functions there is one empty pattern; on a point there is at most one pattern.

Let \(n,d\geq1\) and \(g_1,\ldots,g_n\) be given. Every strict pattern of all \(n\) functions restricts to a strict pattern \(\sigma'\) of \(g_1,\ldots,g_{n-1}\), and each \(\sigma'\) has at most two extensions. If \(g_n\) is a nonzero constant, each \(\sigma'\) has at most one extension; if \(g_n\) is zero, there are no strict patterns. Otherwise \(\Pi=\{g_n=0\}\) is an affine hyperplane, and choosing an affine bijection \(\mathbb R^{d-1}\to\Pi\) turns the restrictions of \(g_1,\ldots,g_{n-1}\) into affine functions on \(\mathbb R^{d-1}\).

Suppose \(\sigma'\) has two extensions. The set \(R_{\sigma'}\) of points where \(g_1,\ldots,g_{n-1}\) have the signs \(\sigma'\) is convex, as an intersection of open half-spaces, and contains points \(y_+\), \(y_-\) with \(g_n(y_+)>0>g_n(y_-)\). On the segment from \(y_-\) to \(y_+\), which lies in \(R_{\sigma'}\), the affine function \(g_n\) vanishes at some point \(y^*\). So \(y^*\in\Pi\) realizes \(\sigma'\) as a strict pattern of the restricted functions. Distinct \(\sigma'\) are realized at distinct points with distinct patterns. Hence the number of \(\sigma'\) with two extensions is at most \(N(n-1,d-1)\), and the total number of strict patterns is at most \(N(n-1,d)+N(n-1,d-1)\). \(\square\)

The bound is the classical count of the regions of an arrangement of affine hyperplanes, due to Schläfli. It is attained by \(n\) hyperplanes in general position.

## 2. Marked sequences and pivots

Let \(M=(E,\mathcal I)\) be a finite matroid. A *marked occurrence* is a label together with a mark in \(\{0,1\}\); a *marked sequence* is a finite sequence of marked occurrences, repetitions of labels allowed. Let \(V\) be a set of \(n\) nonloops, each spanned by the labels of the whole sequence. The *pivot* of \(f\in V\) is the first occurrence such that the labels up to and including it span \(f\). The *mark vector* of the sequence assigns to each \(f\in V\) the mark of its pivot.

Fix an *old sequence* of marked occurrences whose labels span \(E\), and a list of at most \(s\) further labels, the *movable occurrences*, repetitions allowed. An *insertion* places all movable occurrences into the old sequence, in any order and at any positions, and gives each of them any mark.

**Lemma 2.1 (marked pivots).** Over all insertions, the number of mark vectors on \(V\) is at most
\[
4^s\sum_{\ell=0}^s\binom n\ell.\tag{2.1}
\]

*Proof.* *Step 1: an old basis.* Delete from the old sequence every occurrence whose label is spanned by the old occurrences before it. After any insertion, such an occurrence is still spanned by its predecessors, so it changes the span of no prefix (Lemma 1.3(b) of the first lesson) and is never a pivot; deleting it changes no mark vector. The remaining old labels \(b_1,\ldots,b_r\), in order, are independent, since each is not spanned by the earlier ones, and they span \(E\): they form a basis. Write \(B_j=\{b_1,\ldots,b_j\}\) and let \(A\) be the set of labels of the movable occurrences.

*Step 2: few possible greedy sets.* For an insertion, call an occurrence *greedy* if it is not spanned by the occurrences before it. By Lemma 1.4 of the first lesson, the greedy occurrences of every prefix are independent and span the same flat as the prefix. Let
\[
\begin{aligned}
\Delta_j&=\operatorname{rk}(A\mid B_{j-1})-\operatorname{rk}(A\mid B_j)\\
&=1-\operatorname{rk}\bigl(\{b_j\}\bigm|B_{j-1}\cup A\bigr)\in\{0,1\}.
\end{aligned}
\]
The two expressions agree by expanding the conditional ranks, and \(\sum_j\Delta_j=\operatorname{rk}(A)-\operatorname{rk}(A\mid B_r)\), which is \(\operatorname{rk}(A)\leq s\) since \(B_r\) spans \(E\). If \(\Delta_j=0\), then \(b_j\) is not spanned by \(B_{j-1}\cup A\), hence by no set of labels preceding it in any insertion, and so it is greedy in every insertion. Therefore the set \(J\) of greedy occurrences is determined by which of the at most \(s\) old occurrences with \(\Delta_j=1\) it omits, and which movable occurrences it contains: at most \(2^s\cdot2^s=4^s\) possibilities.

*Step 3: pivots from a fixed greedy set.* Fix one possible \(J\). Its labels are independent and span \(E\). For \(f\in V\) there is a unique smallest subset \(S_f\subseteq J\) spanning \(f\): if \(S,S'\subseteq J\) both span \(f\), then submodularity applied to \(S\cup\{f\}\) and \(S'\cup\{f\}\), whose ranks are \(|S|\) and \(|S'|\), gives, with \(r_f=\operatorname{rk}((S\cap S')\cup\{f\})\),
\[
\begin{aligned}
|S|+|S'|&\geq\operatorname{rk}\bigl(S\cup S'\cup\{f\}\bigr)+r_f\\
&\geq|S\cup S'|+r_f,
\end{aligned}
\]
so \(r_f\leq|S\cap S'|\) and \(S\cap S'\) spans \(f\); the intersection of all spanning subsets of \(J\) is \(S_f\). It is nonempty because \(f\) is a nonloop. In an insertion with greedy set \(J\), a prefix spans \(f\) exactly when its greedy occurrences, a subset of \(J\), span \(f\), that is, when they contain \(S_f\). So the pivot of \(f\) is the last occurrence of \(S_f\) in the sequence.

*Step 4: marks as signs.* Still with \(J\) fixed, let \(o_1,\ldots,o_p\) be its old occurrences in order. Give \(o_i\) the *score* \(\pm2^{(s+1)i}\), with sign \(+\) for mark \(1\) and \(-\) for mark \(0\). Given an insertion with greedy set \(J\), give the movable occurrences of \(J\) distinct powers of two, in the order in which they appear: before \(o_1\) use exponents among \(0,\ldots,s\); between \(o_i\) and \(o_{i+1}\) use exponents among \((s+1)i+1,\ldots,(s+1)i+s\); after \(o_p\) the same with \(i=p\). There are at most \(s\) movable occurrences, so every gap has room. Give each the sign of its mark. Now the absolute scores increase along the sequence, and each exceeds the sum of all earlier ones. Hence for every \(f\in V\) the sum of the scores over \(S_f\) is nonzero and has the sign of its last member: positive exactly when the pivot of \(f\) has mark \(1\).

Regard the scores of the movable occurrences of \(J\) as variables \(y\in\mathbb R^{s'}\), \(s'\leq s\). For each \(f\in V\) the sum of the scores over \(S_f\) is an affine function \(g_f(y)\), whose constant term is the sum of the fixed old scores in \(S_f\). Every insertion with greedy set \(J\) gives a point \(y\) at which the strict sign pattern of \((g_f)_{f\in V}\) is exactly its mark vector. By Lemma 1.1 there are at most \(\sum_{\ell\leq s}\binom n\ell\) such patterns. Summing over the at most \(4^s\) sets \(J\) proves (2.1). \(\square\)

The bound depends on \(s\) and \(n\) only. All orders, positions and marks of the movable occurrences are included, and the length of the old sequence plays no role.

## 3. Exercises

**3.1.** Show directly that \(n\) affine functions on the real line have at most \(n+1\) strict sign patterns, in agreement with Lemma 1.1.

**3.2.** Show that three lines in general position in the plane realize \(7=\binom30+\binom31+\binom32\) strict sign patterns.

**3.3.** In the uniform matroid of rank one on \(\{x,y,z\}\), let the old sequence be the single occurrence \((x,0)\), let \(V=\{y,z\}\), and let the only movable occurrence have label \(y\). List all mark vectors and compare with (2.1).

**3.4.** In the matroid in which every set is independent, let the old sequence list every label once with mark \(0\), let the movable occurrences have \(s\) distinct labels \(f_1,\ldots,f_s\), and let \(V=\{f_1,\ldots,f_s\}\). How many mark vectors arise?

**3.5.** Why may Step 1 delete old occurrences without changing any mark vector, although after an insertion a deleted occurrence may come after movable occurrences that change the span?

## 4. Solutions

**3.1.** Each nonconstant affine function on \(\mathbb R\) changes sign at one point. At most \(n\) such points cut the line into at most \(n+1\) open intervals, on each of which all signs are constant; a point where some function vanishes realizes no strict pattern.

**3.2.** Three lines in general position cut the plane into seven regions: one bounded triangle, three regions touching it along an edge, and three touching it at a vertex. Distinct regions have distinct sign patterns.

**3.3.** If \(y\) is inserted after \(x\), both \(y\) and \(z\) are first spanned at \(x\): mark vector \((0,0)\). If \(y\) is inserted before \(x\) with mark \(\mu\), both are first spanned at \(y\): mark vector \((\mu,\mu)\). So the mark vectors are \((0,0)\) and \((1,1)\); the bound (2.1) is \(4(1+2)=12\).

**3.4.** Here a label is spanned only by an occurrence of itself. So the pivot of \(f_i\) is its movable occurrence if this is inserted before the old occurrence of \(f_i\), and the old one, with mark \(0\), otherwise. Inserting \(f_i\) early with mark \(1\) or \(0\), independently for each \(i\), realizes all \(2^s\) vectors. The bound (2.1) gives \(4^s2^s\), so the exponential dependence on \(s\) cannot be avoided.

**3.5.** A deleted occurrence is spanned by old occurrences that precede it in the old sequence, and these precede it in every insertion too. Prefixes ending just before and just after it span the same flat, so it can never be the first occurrence at which a label becomes spanned, and removing it does not change the flat spanned by any prefix.

## References

- [OpenAI-P] OpenAI, *One Sample Suffices for Matroid Prophet Inequalities against an Almighty Adversary*, OpenAI Math Release preprint, 23 September 2026, Section 5.1. https://github.com/openai/math/tree/main/preprints/One-Sample-Suffices-for-Matroid-Prophet-Inequalities-against-an-Almighty-Adversary-September-23-2026
- L. Schläfli, *Theorie der vielfachen Kontinuität* (written 1850–1852, published 1901), Section 16, is credited for the region count of hyperplane arrangements; the course proves the bound it uses.
