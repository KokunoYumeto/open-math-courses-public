# Weighted shifts whose invariant subspaces are tails

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

A closed subspace of a Hilbert space is *invariant* for an operator \(S\) if \(S\) maps it into itself, and *hyperinvariant* for \(S\) if every operator commuting with \(S\) maps it into itself. The *hyperinvariant subspace problem* asks whether every bounded operator on an infinite-dimensional separable complex Hilbert space that is not a multiple of the identity has a hyperinvariant subspace other than \(\{0\}\) and the whole space. OpenAI answered it negatively in 2026 [OAI]. This course proves their theorem: on every infinite-dimensional separable complex Hilbert space there is a nonzero operator \(S\) with \(\lim_n\|S^n\|^{1/n}=0\) whose commutant leaves no closed subspace invariant except \(\{0\}\) and the whole space.

The operator is a measurable family of bilateral weighted shifts \(S_x\), indexed by the points \(x\) of a probability space. Three facts make it work.

- Each \(S_x\) has only the obvious invariant subspaces, the *tails* spanned by the basis vectors \(e_j\) with \(j\ge h\). This lesson proves the criterion behind this fact, a theorem of Domar [Dom].
- An operator \(V\) that commutes with \(S\) carries each fibre to a neighbouring fibre and moves every tail one step backward.
- A closed subspace invariant under the commutant of \(S\) therefore consists, fibre by fibre, of tails whose starting index strictly decreases along an orbit of a measure-preserving transformation. On a probability space this is impossible unless all fibres are \(\{0\}\) or all fibres are everything.

The second lesson constructs the weights over the \(2\)-adic integers and proves the norm estimates; the third constructs \(V\) and proves the theorem.

This lesson has five parts. Section 1 sets up commutants and hyperinvariant subspaces. Section 2 translates weighted shifts into right translation on weighted sequence spaces. Section 3 proves a lemma on convex minorants of sequences. Section 4 proves Domar's support separation theorem, and Section 5 deduces that the invariant subspaces are the tails.

We use from [the Hilbert space lesson](course:foundations-of-von-neumann-algebras/hilbert-spaces-and-compact-operators#OA-FND-HS-02): the projection theorem (Theorem 2.2), including \(\overline Y=(Y^\perp)^\perp\) for a subspace \(Y\), and the Riesz–Fréchet theorem (Theorem 2.3). From [the double commutant lesson](course:foundations-of-von-neumann-algebras/the-double-commutant-theorem#oa-fnd-bi-02) we use Proposition 2.1, which states that a commutant is a weakly closed unital algebra, and Definition 2.3 of a von Neumann algebra (a \(*\)-algebra \(M\) of operators with \(M=M''\)).

## 1. Commutants and hyperinvariant subspaces

Hilbert spaces are complex, and operators are bounded. For \(S\in B(H)\) the *commutant* is
\[
\{S\}'=\{A\in B(H):AS=SA\}.
\]
A closed subspace \(L\subseteq H\) is *invariant* for a set \(\mathcal A\subseteq B(H)\) if \(AL\subseteq L\) for every \(A\in\mathcal A\). It is *hyperinvariant* for \(S\) if it is invariant for \(\{S\}'\). The subspaces \(\{0\}\) and \(H\) are invariant for every set; they are the *trivial* ones. An algebra \(\mathcal A\subseteq B(H)\) is *transitive* if its only invariant closed subspaces are the trivial ones. A net \(A_\lambda\) converges to \(A\) *weakly* if \(\langle A_\lambda\xi,\eta\rangle\to\langle A\xi,\eta\rangle\), and *strongly* if \(A_\lambda\xi\to A\xi\), for all \(\xi,\eta\in H\).

**Lemma 1.1** (the commutant of one operator). Let \(S\in B(H)\) with \(H\neq\{0\}\).

1. \(\{S\}'\) is a unital algebra, closed in the weak operator topology and therefore in the strong operator topology.
2. If \(S\) is not a scalar multiple of the identity, then \(\{S\}'\neq B(H)\).
3. \(\{S\}'\) is transitive if and only if \(S\) has no nontrivial hyperinvariant subspace.

**Proof.** (1) This is Proposition 2.1(1) of the double commutant lesson, applied to the set \(\{S\}\). Strong convergence implies weak convergence, so a weakly closed set is strongly closed.

(2) Suppose that every operator commutes with \(S\). For a unit vector \(\xi\), the rank-one projection \(Q\zeta=\langle\zeta,\xi\rangle\xi\) commutes with \(S\), so
\[
S\xi=SQ\xi=QS\xi=\langle S\xi,\xi\rangle\xi .
\]
Thus every nonzero vector is an eigenvector. If \(\xi,\eta\) are linearly independent with \(S\xi=a\xi\), \(S\eta=b\eta\) and \(S(\xi+\eta)=c(\xi+\eta)\), then \((a-c)\xi+(b-c)\eta=0\), so \(a=c=b\). Two linearly dependent nonzero vectors have the same eigenvalue anyway. Hence all nonzero vectors have one common eigenvalue \(a\), and \(S=a1\).

(3) Both statements say that the only closed subspaces invariant under every operator commuting with \(S\) are \(\{0\}\) and \(H\). \(\square\)

So an operator \(S\) that is not a scalar multiple of the identity and has no nontrivial hyperinvariant subspace has a commutant that is a weakly closed, unital, transitive algebra different from \(B(H)\). On an infinite-dimensional separable \(H\), such an algebra also answers negatively the *transitive algebra problem*, which asks whether every weakly closed unital transitive algebra of operators on \(H\) is all of \(B(H)\).

The next lemma connects hyperinvariant subspaces with von Neumann algebras. The OpenAI companion paper [OAI-C] uses it to deduce the same negative answer from an operator in the hyperfinite II\(_1\) factor that has no nontrivial invariant projection in that factor.

**Lemma 1.2.** Let \(M\subseteq B(H)\) be a von Neumann algebra and \(T\in M\). If \(L\) is a hyperinvariant subspace for \(T\), then its orthogonal projection \(P\) lies in \(M\), and \((1-P)TP=0\).

**Proof.** Every \(A\in M'\) commutes with \(T\), because \(T\in M\). So \(L\) is invariant for the set \(M'\), which is closed under adjoints. By Proposition 2.1(5) of the double commutant lesson, \(P\in(M')'=M''=M\). Since \(T\) commutes with itself, \(TL\subseteq L\), which is the identity \((1-P)TP=0\). \(\square\)

The converse fails: for \(T=0\) on \(\mathbb C^2\) and \(M=B(\mathbb C^2)\), every projection \(P\in M\) satisfies \((1-P)TP=0\), but \(\{T\}'=B(\mathbb C^2)\) and \(T\) has no nontrivial hyperinvariant subspace.

## 2. Weighted shifts and weighted sequence spaces

Let \(K=\ell^2(\mathbb Z)\) with its standard orthonormal basis \((e_j)_{j\in\mathbb Z}\). For \(h\in\mathbb Z\) put
\[
K_{\ge h}=\{\xi\in K:\xi_j=0\text{ for }j<h\},\qquad K_{\ge-\infty}=K,\qquad K_{\ge+\infty}=\{0\}.
\]
These are the *tails*. Each \(K_{\ge h}\) with \(h\in\mathbb Z\) is the closed span of the \(e_j\) with \(j\ge h\).

For positive numbers \(\beta_j\) (\(j\in\mathbb Z\)) with \(\sup_j\beta_j<\infty\), the *bilateral weighted shift* with weights \(\beta_j\) is the operator \(T\) with \(Te_j=\beta_je_{j+1}\). It maps the orthonormal basis to an orthogonal family, so \(\|T\xi\|^2=\sum_j\beta_j^2|\xi_j|^2\) and \(\|T\|=\sup_j\beta_j\). Every tail is invariant for \(T\).

Let \(w=(w_j)_{j\in\mathbb Z}\) be a positive *decreasing* sequence: \(w_{j+1}\le w_j\) for all \(j\). The *weighted space* \(\ell^2(w)\) consists of the complex sequences \(c=(c_j)_{j\in\mathbb Z}\) with
\[
\|c\|_w^2=\sum_{j\in\mathbb Z}|w_jc_j|^2<\infty .
\]
*Right translation* is \((Rc)_j=c_{j-1}\). Since \(w\) decreases,
\[
\|Rc\|_w^2=\sum_j|w_{j+1}c_j|^2\le\|c\|_w^2 .
\]
The *tails* of \(\ell^2(w)\) are \(\ell^2(w)_{\ge h}=\{c:c_j=0\text{ for }j<h\}\), for \(h\in\mathbb Z\cup\{\pm\infty\}\); they are closed and \(R\)-invariant.

**Lemma 2.1** (dictionary). Let \(w\) be positive and decreasing.

1. The map \(\Phi c=(w_jc_j)_{j\in\mathbb Z}\) is a unitary from \(\ell^2(w)\) onto \(K\). It maps \(\ell^2(w)_{\ge h}\) onto \(K_{\ge h}\), and \(\Phi R\Phi^{-1}\) is the bilateral weighted shift with weights \(\beta_j=w_{j+1}/w_j\).
2. Conversely, let \(T\) be the bilateral weighted shift with weights \(0<\beta_j\le1\), and define \(w_0=1\) and \(w_{j+1}=\beta_jw_j\) for all \(j\in\mathbb Z\). Then \(w\) is positive and decreasing, and \(T=\Phi R\Phi^{-1}\).
3. The bounded linear functionals on \(\ell^2(w)\) are exactly the maps \(c\mapsto\sum_jb_jc_j\) with \(\sum_j|b_j/w_j|^2<\infty\); these series converge absolutely.
4. For a closed subspace \(L\subseteq\ell^2(w)\), let \(L^{a}\) be the set of sequences \(b\) as in (3) with \(\sum_jb_jc_j=0\) for all \(c\in L\). A sequence \(c\in\ell^2(w)\) lies in \(L\) if and only if \(\sum_jb_jc_j=0\) for every \(b\in L^{a}\).

**Proof.** (1) \(\Phi\) is isometric by definition, and onto because \(\xi\mapsto(\xi_j/w_j)_j\) is an inverse. It preserves the vanishing of coordinates. Writing \(\delta_j\) for the sequence with a single \(1\) at \(j\), we get \(\Phi R\Phi^{-1}e_j=\Phi R(w_j^{-1}\delta_j)=\Phi(w_j^{-1}\delta_{j+1})=(w_{j+1}/w_j)e_{j+1}\).

(2) The recursion determines \(w_j\) for all \(j\), positive, and \(w_{j+1}/w_j=\beta_j\le1\). Apply (1).

(3) Let \(\varphi\) be a bounded functional. By the Riesz–Fréchet theorem there is \(\eta\in K\) with \(\varphi(c)=\langle\Phi c,\eta\rangle=\sum_jw_jc_j\bar\eta_j\). Put \(b_j=w_j\bar\eta_j\). Conversely, for such \(b\) the Cauchy–Schwarz inequality gives \(\sum_j|b_jc_j|\le\|(b_j/w_j)\|_{\ell^2}\|c\|_w\).

(4) Transport by \(\Phi\): the functionals vanishing on \(L\) correspond to the vectors \(\eta\in(\Phi L)^\perp\), and \(\Phi L=((\Phi L)^\perp)^\perp\) by the projection theorem. \(\square\)

By (1) and (2), *the closed invariant subspaces of a bilateral weighted shift with weights in \((0,1]\) are the tails exactly when the closed \(R\)-invariant subspaces of the corresponding \(\ell^2(w)\) are its tails.* Multiplying \(T\) by a positive constant changes no invariant subspace, so the restriction \(\beta_j\le1\) is harmless.

## 3. Convex minorants

A real sequence \((g_n)_{n\ge0}\) is *convex* if its differences \(g_{n+1}-g_n\) are nondecreasing, that is, \(g_{n+1}-2g_n+g_{n-1}\ge0\) for \(n\ge1\). It is *concave* if \(-g\) is convex. We use four elementary facts about a convex sequence \(g\).

- (C1) *Chords.* For \(0\le i<n<k\), \(g_n\le\frac{(k-n)g_i+(n-i)g_k}{k-i}\). Indeed, each of the \(n-i\) differences between \(i\) and \(n\) is at most each of the \(k-n\) differences between \(n\) and \(k\), so \(\frac{g_n-g_i}{n-i}\le\frac{g_k-g_n}{k-n}\); rearrange.
- (C2) If \(g_0=0\), then \(g_n-g_{n-1}\ge g_n/n\) for \(n\ge1\), since \(g_n\) is the sum of \(n\) differences, the last of which is the largest.
- (C3) For \(0\le m\le n\) and \(k\ge0\), \(g_{n+k}-g_n\ge g_{m+k}-g_m\): both sides are sums of \(k\) consecutive differences, and those on the left come later.
- (C4) If a family of convex sequences has a finite pointwise supremum, the supremum is convex, because each member satisfies \(g_n\le\frac12(g_{n-1}+g_{n+1})\).

**Lemma 3.1** (greatest convex minorant). Let \(f_0=0\) and \(f_n\in[0,\infty]\) for \(n\ge1\), with \(f_n<\infty\) for infinitely many \(n\). Suppose some convex sequence \(G\) satisfies \(G_0=0\), \(G_n\le f_n\) for all \(n\), and \(G_n/n\to\infty\). Let \(F_n\) be the supremum of \(g_n\) over all convex sequences \(g\) with \(g\le f\) termwise.

1. \(F\) is a finite convex sequence with \(F_0=0\) and \(G\le F\le f\).
2. The differences \(F_n-F_{n-1}\) tend to \(+\infty\).
3. The set of *contact indices* \(\{n\ge1:F_{n+1}-2F_n+F_{n-1}>0\}\) is infinite, and \(F_n=f_n\) at every contact index \(n\).

**Proof.** (1) Every admissible \(g\) has \(g_0\le f_0=0\), and \(G\) is admissible, so \(F_0=0\) and \(F\ge G\). For \(n\ge1\) choose \(k>n\) with \(f_k<\infty\). By (C1) with \(i=0\), every admissible \(g\) satisfies \(g_n\le\frac{(k-n)g_0+ng_k}{k}\le\frac nkf_k\). So \(F_n\) is finite. \(F\le f\) holds because each admissible \(g\) does, and \(F\) is convex by (C4).

(2) By (C2), \(F_n-F_{n-1}\ge F_n/n\ge G_n/n\to\infty\).

(3) If there were only finitely many contact indices, the differences of \(F\) would be constant from some index on, contradicting (2). Let \(n\) be a contact index, \(\delta=F_{n+1}-2F_n+F_{n-1}>0\), and suppose \(F_n<f_n\). Choose \(0<\varepsilon<\delta/2\) with \(F_n+\varepsilon\le f_n\). The sequence \(g\) that agrees with \(F\) except for \(g_n=F_n+\varepsilon\) has second difference \(\delta-2\varepsilon>0\) at \(n\), second differences increased by \(\varepsilon\) at \(n\pm1\), and unchanged ones elsewhere. So \(g\) is convex and \(g\le f\), but \(g_n>F_n\), contradicting the definition of \(F\). \(\square\)

\(F\) is the *greatest convex minorant* of \(f\).

## 4. Support separation

**Standing hypotheses (D).** The sequence \(w=(w_j)_{j\in\mathbb Z}\) is positive and decreasing, \(\log w_j\) is convex for \(j\le0\) and concave for \(j\ge0\) (as functions of the integer \(j\) on these half-lines), and
\[
\sum_{j\ne0}w_j^{1/j}<\infty .\tag{D1}
\]
For \(j=-n<0\) the summand is \(w_{-n}^{-1/n}\). In addition, at least one of the following holds:
\[
\limsup_{n\to\infty}\frac{\log w_{-n}}{n^2}>\log3,\tag{D2}
\]
\[
\liminf_{n\to\infty}\frac{\log w_{n}}{n^2}<-\log3.\tag{D2'}
\]
Dividing \(w\) by \(w_0\) changes neither \(\ell^2(w)\) as a space nor its closed subspaces, and keeps (D); so we normalize \(w_0=1\). Put, for \(n\ge0\),
\[
P_n=\log w_{-n},\qquad Q_n=-\log w_n,\qquad\beta_j=\frac{w_{j+1}}{w_j}\in(0,1].
\]

**Lemma 4.1.** Assume (D) and (D1), with \(w_0=1\).

1. \(P\) and \(Q\) are convex, nonnegative, vanish at \(0\), and \(P_n/n\to\infty\), \(Q_n/n\to\infty\).
2. \(\sum_{j\in\mathbb Z}\beta_j<\infty\).
3. \(w_j/w_{j-r}\le\beta_{j-r}\) for all \(j\in\mathbb Z\) and \(r\ge1\).
4. If \(|c_j|w_j\le1\) and \(|b_j|\le w_j\) for all \(j\), then \(\sum_j|b_jc_{j-r}|\le\sum_j\beta_j\) for every \(r\ge1\).

**Proof.** (1) The differences of \(Q\) are \(Q_{n+1}-Q_n=-(\log w_{n+1}-\log w_n)\), nondecreasing by concavity of \(\log w\) on \(j\ge0\). The differences of \(P\) are \(P_{n+1}-P_n=-(\log w_{-n}-\log w_{-n-1})\); as \(n\) grows, the difference \(\log w_{-n}-\log w_{-n-1}\) moves left, where it is smaller by convexity of \(\log w\) on \(j\le0\), so the differences of \(P\) are nondecreasing. Nonnegativity follows from \(w_{-n}\ge w_0=1\ge w_n\). By (D1), \(w_n^{1/n}=e^{-Q_n/n}\to0\) and \(w_{-n}^{-1/n}=e^{-P_n/n}\to0\).

(2) For \(n\ge1\), (C2) gives
\[
\beta_{n-1}=e^{-(Q_n-Q_{n-1})}\le e^{-Q_n/n}=w_n^{1/n},\qquad
\beta_{-n}=e^{-(P_n-P_{n-1})}\le e^{-P_n/n}=w_{-n}^{-1/n}.
\]
Every \(j\in\mathbb Z\) has exactly one of the forms \(n-1\) or \(-n\) with \(n\ge1\), so \(\sum_j\beta_j\le\sum_{j\ne0}w_j^{1/j}\).

(3) \(w_j/w_{j-r}=\beta_{j-r}\beta_{j-r+1}\cdots\beta_{j-1}\le\beta_{j-r}\), as all \(\beta_i\le1\).

(4) \(|b_jc_{j-r}|\le w_j/w_{j-r}\le\beta_{j-r}\). \(\square\)

**Proposition 4.2** (support separation; Domar). Assume (D), (D1), and (D2) or (D2'). Let \(b,c\) be nonzero complex sequences on \(\mathbb Z\) such that \((c_jw_j)_j\) and \((b_j/w_j)_j\) are bounded and
\[
\sum_{j\in\mathbb Z}b_jc_{j-r}=0\qquad\text{for every }r\ge1.\tag{4.1}
\]
Then the support of \(b\) has a largest element \(t\), the support of \(c\) has a least element \(h\), and \(t\le h\).

**Proof.** Multiplying \(b\) and \(c\) by positive constants changes neither the hypotheses nor the conclusion, so we may assume \(|c_j|w_j\le1\) and \(|b_j|\le w_j\) for all \(j\). Normalize \(w_0=1\). By Lemma 4.1(4), the series (4.1) converge absolutely.

*Step 1: if the support of \(c\) has a least element \(h\), the conclusion holds.* First we show that the support of \(b\) is bounded above. Suppose not. Apply Lemma 3.1 to \(f_0=0\) and \(f_n=-\log|b_n|\) for \(n\ge1\) (with \(-\log0=+\infty\)), and \(G=Q\). This is allowed: \(f_n\ge-\log w_n=Q_n\ge0\), \(f_n<\infty\) for infinitely many \(n\), and \(Q_n/n\to\infty\). Let \(B\) be the greatest convex minorant and \(v_n=e^{-B_n}\). Then
\[
|b_n|\le v_n\le w_n\quad(n\ge1),\qquad|b_p|=v_p\ \text{at contact indices }p.
\]
Fix an integer \(p_0\ge\max(1,h+1)\). Let \(p\ge p_0\) be a contact index of \(B\), and apply (4.1) with \(r=p-h\ge1\). The terms with \(j<p\) vanish, because then \(j-r<h\). Since \(b_p\neq0\),
\[
|c_h|\le\sum_{k\ge1}\frac{|b_{p+k}|}{|b_p|}|c_{h+k}|\le\sum_{k\ge1}\frac{v_{p+k}}{v_p}|c_{h+k}|.\tag{4.2}
\]
By (C3), \(B_{p+k}-B_p\ge B_{p_0+k}-B_{p_0}\), so \(v_{p+k}/v_p\le v_{p_0+k}/v_{p_0}\le w_{p_0+k}/v_{p_0}\). With \(|c_{h+k}|\le1/w_{h+k}\) and Lemma 4.1(3) (for \(j=p_0+k\) and \(r=p_0-h\ge1\)), the \(k\)-th term of (4.2) is at most \(\beta_{h+k}/v_{p_0}\), which is summable in \(k\). For fixed \(k\ge1\), once \(p\) is so large that the differences of \(B\) from \(p\) on are nonnegative, \(v_{p+k}/v_p=e^{-(B_{p+k}-B_p)}\le e^{-(B_{p+1}-B_p)}\), which tends to \(0\) by Lemma 3.1(2). Letting \(p\to\infty\) through contact indices, dominated convergence for series turns (4.2) into \(|c_h|\le0\). This contradicts \(h\in\operatorname{supp}c\).

So the support of \(b\), which is nonempty, has a largest element \(t\). If \(t>h\), then in (4.1) with \(r=t-h\) the only nonzero term is \(b_tc_h\): a nonzero \(b_j\) needs \(j\le t\), and a nonzero \(c_{j-r}\) needs \(j\ge t\). This is impossible, so \(t\le h\).

*Step 2: reflection.* Put \(\tilde w_j=1/w_{-j}\), \(\tilde b_j=c_{-j}\) and \(\tilde c_j=b_{-j}\). Then \(\tilde w\) is positive and decreasing with \(\tilde w_0=1\); \(\log\tilde w_j=-\log w_{-j}\) is convex for \(j\le0\) and concave for \(j\ge0\); \(\tilde w_j^{1/j}=w_{-j}^{1/(-j)}\), so (D1) is unchanged; and (D2) for \(w\) is (D2') for \(\tilde w\), and conversely. Moreover \(|\tilde c_j|\tilde w_j=|b_{-j}|/w_{-j}\le1\), \(|\tilde b_j|/\tilde w_j=|c_{-j}|w_{-j}\le1\), and, substituting \(i=r-j\),
\[
\sum_j\tilde b_j\tilde c_{j-r}=\sum_jc_{-j}b_{r-j}=\sum_ib_ic_{i-r}=0\qquad(r\ge1).
\]
Suppose the support of \(b\) has a largest element \(t\). Then the support of \(\tilde c\) has the least element \(-t\), and Step 1 applied to \((\tilde w,\tilde b,\tilde c)\) shows that the support of \(\tilde b\) has a largest element \(-h\le-t\). That is, the support of \(c\) has the least element \(h\ge t\). Step 1 did not use (D2) or (D2'), so this is legitimate.

*Step 3: the remaining case is impossible.* It remains to exclude that the support of \(c\) is unbounded below while the support of \(b\) is unbounded above. The reflection of Step 2 preserves this case and exchanges (D2) and (D2'), so we may assume (D2).

Let \(A\) be the greatest convex minorant of \(f^c_0=0\), \(f^c_m=-\log|c_{-m}|\) (\(m\ge1\)), with \(G=P\); this is allowed since \(|c_{-m}|\le1/w_{-m}\) gives \(f^c_m\ge P_m\). Let \(B\) be the greatest convex minorant of \(f^b\) as in Step 1. Define
\[
u_j=e^{A_{-j}}\ (j\le0),\qquad u_j=e^{-B_j}\ (j\ge0),
\]
consistently \(u_0=1\), and write \(\alpha_m=A_m-A_{m-1}\) and \(\gamma_p=B_p-B_{p-1}\) for \(m,p\ge1\).

- (i) Since \(A\ge P\ge0\) and \(B\ge Q\ge0\) vanish at \(0\), \(\alpha_1,\gamma_1\ge0\). So all \(\alpha_m,\gamma_p\) are nonnegative and nondecreasing, and they tend to \(\infty\) by Lemma 3.1(2).
- (ii) Hence \(u\) is positive and decreasing, and \(\log u\) is convex for \(j\le0\) and concave for \(j\ge0\).
- (iii) \(|c_j|\le1/u_j\) and \(|b_j|\le u_j\) for all \(j\). For \(j\le-1\), \(|c_j|=e^{-f^c_{-j}}\le e^{-A_{-j}}\) and \(|b_j|\le w_j=e^{P_{-j}}\le u_j\). For \(j\ge1\), \(|b_j|=e^{-f^b_j}\le e^{-B_j}\) and \(|c_j|\le1/w_j\le1/u_j\), because \(u_j=e^{-B_j}\le e^{-Q_j}=w_j\). For \(j=0\), both bounds read \(|c_0|,|b_0|\le1\).
- (iv) If \(m\) is a contact index of \(A\), then \(|c_{-m}|=1/u_{-m}\); if \(p\) is a contact index of \(B\), then \(|b_p|=u_p\).
- (v) \(\sum_{j\in\mathbb Z}u_{j+1}/u_j<\infty\). For \(j\ge0\), (C2) gives \(u_{j+1}/u_j=e^{-\gamma_{j+1}}\le e^{-B_{j+1}/(j+1)}\le e^{-Q_{j+1}/(j+1)}=w_{j+1}^{1/(j+1)}\). For \(j=-m\le-1\), \(u_{j+1}/u_j=e^{-\alpha_m}\le e^{-P_m/m}=w_{-m}^{-1/m}\). Apply (D1). In particular \(u_{j+1}/u_j\to0\) as \(j\to\pm\infty\).

Choose \(\lambda\) with \(\log3<\lambda<\limsup_nP_n/n^2\); this is possible by (D2).

*Large curvature.* There are arbitrarily large \(m\) with \(\alpha_{m+1}-\alpha_m>2\lambda\). Otherwise \(\alpha_{m+1}\le\alpha_m+2\lambda\) for all \(m\ge m_0\), and summing twice gives \(P_m\le A_m\le\lambda m^2+O(m)\), so \(\limsup_mP_m/m^2\le\lambda\), contrary to the choice of \(\lambda\).

*Matching slopes.* Take such an \(m\), large enough that \(\alpha_m+\lambda\ge\gamma_1\), and let \(p\ge1\) be the largest index with \(\gamma_p\le\alpha_m+\lambda\); it exists because \(\gamma_p\to\infty\). Then
\[
\gamma_p\le\alpha_m+\lambda<\gamma_{p+1},\qquad\alpha_{m+1}>\alpha_m+2\lambda\ge\gamma_p+\lambda.\tag{4.3}
\]
So the second differences of \(A\) at \(m\) and of \(B\) at \(p\) are positive: \(m\) and \(p\) are contact indices. As \(m\to\infty\) through such indices, \(\alpha_m\to\infty\) and hence \(p\to\infty\).

*The middle terms.* Let \(M=u_p/u_{-m}\); by (iv), \(M=|b_pc_{-m}|>0\). The sequence
\[
\Lambda(n)=\log\frac{u_{p+n}}{u_{n-m}}=-B_{p+n}-A_{m-n}\qquad(-p\le n\le m)
\]
is concave, and by (4.3)
\[
\Lambda(1)-\Lambda(0)=\alpha_m-\gamma_{p+1}<-\lambda,\qquad\Lambda(-1)-\Lambda(0)=\gamma_p-\alpha_{m+1}<-\lambda .
\]
A concave sequence lies below the lines through \(\Lambda(0)\) with these slopes, so
\[
\frac{u_{p+n}}{u_{n-m}}\le Me^{-\lambda|n|}\qquad(-p\le n\le m).\tag{4.4}
\]

*The contradiction.* Apply (4.1) with \(r=q:=m+p\) and the summation index \(j=p+n\): \(\sum_nb_{p+n}c_{n-m}=0\). The term \(n=0\) has modulus \(M\), so by (iii)
\[
M\le\sum_{n\ne0}\frac{u_{p+n}}{u_{n-m}}=S_-+S_0+S_+,
\]
where \(S_0\) is the sum over \(-p\le n\le m\), \(S_+\) over \(n>m\), and \(S_-\) over \(n<-p\).

- By (4.4), \(S_0\le M\sum_{n\ne0}e^{-\lambda|n|}=MC_\lambda\) with \(C_\lambda=\frac{2}{e^\lambda-1}<1\), since \(e^\lambda>3\).
- For \(n=m+k\) (\(k\ge1\)) the term is \(u_{q+k}/u_k\). By (4.4) at \(n=m\), \(u_q=u_q/u_0\le M\). Concavity of \(\log u\) on \(j\ge0\) compares the increments over \([q,q+k]\) and \([1,1+k]\): \(u_{q+k}/u_q\le u_{k+1}/u_1\) for \(q\ge1\). Hence
\[
\frac{S_+}{M}\le\sum_{k\ge1}\frac{u_{q+k}}{u_ku_q}\quad\text{and}\quad\frac{u_{q+k}}{u_ku_q}\le\frac1{u_1}\cdot\frac{u_{k+1}}{u_k}.
\]
The bound is summable by (v), and for fixed \(k\) the term tends to \(0\) as \(q\to\infty\), since \(u_{q+k}/u_q\) is a product of \(k\) ratios \(u_{i+1}/u_i\) with \(i\ge q\). By dominated convergence, \(S_+/M\to0\) as \(m\to\infty\).
- For \(n=-p-k\) (\(k\ge1\)) the term is \(u_{-k}/u_{-q-k}\). With \(v_k=1/u_{-k}=e^{-A_k}\) it is \(v_{q+k}/v_k\), and \(v_q\le M\) by (4.4) at \(n=-p\). The sequence \(\log v=-A\) is concave with \(v_0=1\), and \(\sum_kv_{k+1}/v_k<\infty\) by (v). The argument for \(S_+\) gives \(S_-/M\to0\).

Dividing by \(M\) gives \(1\le C_\lambda+o(1)\) as \(m\to\infty\) through the chosen indices, which contradicts \(C_\lambda<1\). \(\square\)

The constant \(\log3\) enters only through \(C_\lambda<1\): the contact term at \(n=0\) must dominate the two geometric tails \(\sum_{n\ne0}e^{-\lambda|n|}\).

## 5. The invariant subspaces are tails

**Theorem 5.1** (Domar). Let \(w\) satisfy (D), (D1), and (D2) or (D2'). Then the closed \(R\)-invariant subspaces of \(\ell^2(w)\) are exactly the tails \(\ell^2(w)_{\ge h}\), \(h\in\mathbb Z\cup\{\pm\infty\}\).

**Proof.** The tails are closed and invariant. Let \(L\) be a closed invariant subspace with \(L\neq\{0\}\) and \(L\neq\ell^2(w)\). For \(c\in L\) and \(b\in L^a\) (Lemma 2.1(4)), all translates \(R^rc\) (\(r\ge0\)) lie in \(L\), so
\[
\sum_jb_jc_{j-r}=0\qquad(r\ge0),
\]
and the sequences \((c_jw_j)\) and \((b_j/w_j)\) are square-summable, hence bounded. Since \(L\neq\ell^2(w)\), Lemma 2.1(4) gives a nonzero \(b^*\in L^a\); since \(L\neq\{0\}\), there is a nonzero \(c\in L\).

By Proposition 4.2, \(t=\max\operatorname{supp}b^*\) exists, and every nonzero \(c\in L\) is supported in \([t,\infty)\). The relation with \(r=0\) reduces to \(b^*_tc_t=0\), so \(c_t=0\). Hence the supports of all elements of \(L\) lie in \([t+1,\infty)\). Their union is nonempty; let \(h\) be its least element and choose \(c^*\in L\) with \(c^*_h\neq0\). Then \(L\subseteq\ell^2(w)_{\ge h}\).

Conversely, let \(b\in L^a\) be nonzero. Proposition 4.2 for the pair \((b,c^*)\) gives \(\max\operatorname{supp}b\le h\), and the relation with \(r=0\) reduces to \(b_hc^*_h=0\), so \(b_h=0\). Thus every \(b\in L^a\) vanishes on \([h,\infty)\) and annihilates \(\ell^2(w)_{\ge h}\). By Lemma 2.1(4), \(\ell^2(w)_{\ge h}\subseteq L\). \(\square\)

The fibres in the next lesson are given by their logarithmic weights \(a_j=-\log\beta_j\). The following form of the theorem is the one we use.

**Corollary 5.2.** Let \(\kappa>2\log3\), and let \(a_j\) (\(j\in\mathbb Z\)) be real numbers with
\[
a_0\le a_1\le a_2\le\cdots,\qquad a_{-1}\le a_{-2}\le a_{-3}\le\cdots,
\]
\[
a_j\ge\kappa(j+1)\ (j\ge0),\qquad a_j\ge\kappa|j|\ (j\le-1).
\]
Then the closed invariant subspaces of the bilateral weighted shift \(Te_j=e^{-a_j}e_{j+1}\) on \(K\) are exactly the tails \(K_{\ge h}\), \(h\in\mathbb Z\cup\{\pm\infty\}\).

**Proof.** The weights \(\beta_j=e^{-a_j}\) lie in \((0,1)\). Let \(w\) be the sequence of Lemma 2.1(2):
\[
w_0=1,\qquad w_n=\exp\Big(-\sum_{k=0}^{n-1}a_k\Big),\qquad w_{-n}=\exp\Big(\sum_{k=1}^{n}a_{-k}\Big)\qquad(n\ge1).
\]
It is positive and decreasing. The differences \(\log w_{j+1}-\log w_j=-a_j\) are nonincreasing for \(j\ge0\) and nondecreasing for \(j\le-1\), which is concavity on \(j\ge0\) and convexity on \(j\le0\). The lower bounds give
\[
w_n^{1/n}\le e^{-\kappa(n+1)/2},\qquad w_{-n}^{-1/n}\le e^{-\kappa(n+1)/2}\qquad(n\ge1),
\]
which proves (D1), and \(\log w_{-n}\ge\kappa n(n+1)/2\), so the \(\limsup\) in (D2) is at least \(\kappa/2>\log3\). Theorem 5.1 and Lemma 2.1(1) finish the proof. \(\square\)

By the symmetric computation, \(\log w_n\le-\kappa n(n+1)/2\), so (D2') holds as well; Theorem 5.1 needs only one of the two.

## 6. Exercises

**Exercise 6.1** (easy; slowly decaying weights). Let \(w\) be positive and decreasing, and suppose \(\sum_{n\ge0}\rho^{2n}/w_n^2<\infty\) for some \(\rho>0\). Show that
\[
L=\Big\{c\in\ell^2(w):c_n=0\text{ for }n<0,\ \sum_{n\ge0}c_n\rho^n=0\Big\}
\]
is a closed \(R\)-invariant subspace that is not a tail. Deduce that the unweighted bilateral shift on \(\ell^2(\mathbb Z)\) has a nontrivial invariant subspace that is not a tail.

*Solution.* By the Cauchy–Schwarz inequality, \(|\sum_{n\ge0}c_n\rho^n|\le\|c\|_w(\sum_{n\ge0}\rho^{2n}/w_n^2)^{1/2}\), so \(L\) is an intersection of kernels of bounded functionals and is closed. If \(c\in L\), then \(Rc\) vanishes at negative indices (its \(0\)-th coordinate is \(c_{-1}=0\)), and \(\sum_{n\ge0}(Rc)_n\rho^n=\sum_{n\ge1}c_{n-1}\rho^n=\rho\sum_{m\ge0}c_m\rho^m=0\). So \(L\) is invariant. The vector \(c=\rho\delta_0-\delta_1\) lies in \(L\) and has \(c_0\neq0\), so a tail containing \(L\) is \(\ell^2(w)_{\ge h}\) with \(h\le0\); but \(L\subseteq\ell^2(w)_{\ge0}\), and \(\delta_0\notin L\) because \(\sum_{n\ge0}(\delta_0)_n\rho^n=1\). So \(L\) is not a tail. For \(w_j=1\) for all \(j\) take \(\rho=\frac12\); then \(\ell^2(w)=\ell^2(\mathbb Z)\) and \(R\) is the bilateral shift. \(\square\)

So some decay of \(w\) is needed for Theorem 5.1: weights with \(w_n\ge Ce^{-\kappa n}\) for \(n\ge0\) satisfy the hypothesis of Exercise 6.1 with any \(\rho<e^{-\kappa}\).

**Exercise 6.2** (easy; powers of a weighted shift). Let \(T\) be the bilateral weighted shift with bounded positive weights \(\beta_j\). Show that \(T^ne_j=\beta_j\beta_{j+1}\cdots\beta_{j+n-1}e_{j+n}\) and \(\|T^n\|=\sup_j\beta_j\beta_{j+1}\cdots\beta_{j+n-1}\).

*Solution.* The formula for \(T^ne_j\) follows by induction on \(n\). So \(T^n\) maps the orthonormal basis to an orthogonal family, \(\|T^n\xi\|^2=\sum_j(\beta_j\cdots\beta_{j+n-1})^2|\xi_j|^2\), and the norm is the supremum of the coefficients. \(\square\)

**Exercise 6.3** (medium; the reflection). Let \(T\) be the bilateral weighted shift with weights \(\beta_j\in(0,1]\) and let \(J\) be the unitary \(Je_j=e_{-j}\) of \(K\). Show that \(JT^*J\) is the bilateral weighted shift with weights \(\beta_{-j-1}\), and that a closed subspace \(L\) is invariant for \(T\) if and only if \(J(L^\perp)\) is invariant for \(JT^*J\). Use this to show directly that if the closed invariant subspaces of \(T\) are the tails, the same holds for the weighted shift with weights \(\beta_{-j-1}\).

*Solution.* \(T^*e_{j+1}=\beta_je_j\), since \(\langle T^*e_{j+1},e_i\rangle=\langle e_{j+1},Te_i\rangle=\beta_i\delta_{i,j}\). Hence \(JT^*Je_j=JT^*e_{-j}=\beta_{-j-1}Je_{-j-1}=\beta_{-j-1}e_{j+1}\). Next, \(TL\subseteq L\) if and only if \(T^*L^\perp\subseteq L^\perp\), and applying \(J\) gives the second statement. The map \(L\mapsto J(L^\perp)\) is a bijection of the closed subspaces, and \(J(K_{\ge h}^\perp)=J\overline{\operatorname{span}}\{e_j:j<h\}=K_{\ge-h+1}\), with \(J(K^\perp)=\{0\}\) and \(J(\{0\}^\perp)=K\). So it maps tails to tails, and the claim follows. \(\square\)

Exercise 6.3 is the operator form of the reflection used in Step 2 of Proposition 4.2.

## Where this leads

The [next lesson](measurable-fields-of-weighted-shifts.md) builds a measurable family of weighted shifts over the \(2\)-adic integers whose logarithmic weights satisfy Corollary 5.2 in every fibre, and proves the norm estimate \(\|S^n\|\le\exp(-10\lfloor(n+1)^2/4\rfloor)\). The [last lesson](a-transitive-commutant.md) couples the fibres by a commuting operator that moves tails backward, and proves that the commutant is transitive.

## References

- [OAI] OpenAI, *Backward intertwiners and a transitive commutant*, OpenAI Math Release preprint, 27 September 2026. https://github.com/openai/math/blob/main/preprints/Backward-intertwiners-and-a-transitive-commutant-September-27-2026/paper.pdf. Section 2 proves the two-sided case of Theorem 5.1 that the construction uses; Step 1 of Proposition 4.2 follows its direct argument.
- [OAI-C] OpenAI, *Invariant-projection counterexamples for every irrational rotation*, OpenAI Math Release preprint, 27 September 2026. https://github.com/openai/math/blob/main/preprints/Invariant-projection-counterexamples-for-every-irrational-rotation-September-27-2026/paper.pdf. Lemmas 1.2 and 1.3 there correspond to Lemmas 1.1 and 1.2 here.
- [Dom] Y. Domar, *Translation invariant subspaces of weighted \(\ell^p\) and \(L^p\) spaces*, Math. Scand. 49 (1981), 133–144. https://doi.org/10.7146/math.scand.a-11926. Theorem 2 there proves the conclusion of Theorem 5.1 for all \(\ell^p(w)\), \(1\le p<\infty\), and for \(c_0(w)\); Theorem 5.1 is its case \(p=2\). Theorem 5 there is Proposition 4.2, and Step 3 follows Domar's proof of it. For the one-sided cases Domar uses a theorem of Nikolskii instead of Step 1.
