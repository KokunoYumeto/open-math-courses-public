# Ultrapowers and Darbo's fixed-point theorem

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson supplies two general tools for the proof of Tingley's theorem [OpenAI-T, Section 3 and Appendix A]. The first is the ultrapower of a normed space, a limit construction in which a supremum over sequences becomes a value at one point; with it, a surjective sphere isometry of positive defect yields one whose defect is attained (Proposition 3.1). The second is Darbo's fixed-point theorem: a continuous self-map of a closed bounded convex subset of a Banach space that strictly decreases Kuratowski's measure of noncompactness has a fixed point (Theorem 6.1). It is deduced from Schauder's theorem for compact convex sets, which in turn follows from Brouwer's theorem.

We use: Zorn's lemma, [Theorem 1.1 of the Banach space lesson](course:foundations-of-von-neumann-algebras/hahn-banach-baire-and-the-basic-theorems-on-banach-spaces#OA-FND-HB-01); Brouwer's fixed-point theorem for compact convex subsets of \(\mathbb R^n\), [Corollary 1.2 of Lebesgue's covering theorem and the dimension of cubes](course:index-theory-of-elliptic-operators/lebesgue-s-covering-theorem-and-the-dimension-of-cubes#1-fixed-points-on-compact-convex-sets); and from [Supports, radial contact and the Mazur–Ulam theorem](supports-radial-contact-and-the-mazur-ulam-theorem.md) the defect and Lemma 4.1.

## 1. Ultrafilters and limits along them

A *filter* on \(\mathbb N\) is a nonempty family \(\mathcal U\) of subsets of \(\mathbb N\) with \(\varnothing\notin\mathcal U\), closed under finite intersections and under passing to larger sets. It is *free* if it contains every cofinite set, and an *ultrafilter* if it is maximal among filters for inclusion.

**Lemma 1.1.** There is a free ultrafilter \(\mathcal U\) on \(\mathbb N\). For every \(A\subseteq\mathbb N\), exactly one of \(A\) and \(\mathbb N\setminus A\) lies in \(\mathcal U\); and if \(A\cup B\in\mathcal U\), then \(A\in\mathcal U\) or \(B\in\mathcal U\).

**Proof.** The filters containing all cofinite sets, ordered by inclusion, form a nonempty set (the cofinite sets form such a filter) in which the union of a chain is again such a filter. By Zorn's lemma there is a maximal one, \(\mathcal U\). It is an ultrafilter: a filter containing \(\mathcal U\) also contains the cofinite sets. Let \(A\notin\mathcal U\). If \(A\cap B\neq\varnothing\) for every \(B\in\mathcal U\), the sets containing some \(A\cap B\), \(B\in\mathcal U\), would form a filter strictly larger than \(\mathcal U\). So \(A\cap B=\varnothing\) for some \(B\in\mathcal U\), and \(\mathbb N\setminus A\supseteq B\) lies in \(\mathcal U\). Both \(A\) and its complement cannot lie in \(\mathcal U\), since their intersection is empty. If neither \(A\) nor \(B\) lies in \(\mathcal U\), their complements do, and so does the complement of \(A\cup B\). \(\square\)

Fix a free ultrafilter \(\mathcal U\) on \(\mathbb N\).

**Lemma 1.2** (limits along \(\mathcal U\)). For every bounded real sequence \((a_n)\) there is exactly one real number \(L=\lim_{\mathcal U}a_n\) such that \(\{n:|a_n-L|<\varepsilon\}\in\mathcal U\) for every \(\varepsilon>0\). Moreover:

(a) \(\lim_{\mathcal U}\) is linear, and \(\lim_{\mathcal U}a_n\le\lim_{\mathcal U}b_n\) whenever \(\{n:a_n\le b_n\}\in\mathcal U\);

(b) if \(\phi:\mathbb R^k\to\mathbb R\) is continuous and \(a^{(1)},\dots,a^{(k)}\) are bounded sequences, then \(\lim_{\mathcal U}\phi(a^{(1)}_n,\dots,a^{(k)}_n)=\phi(\lim_{\mathcal U}a^{(1)}_n,\dots,\lim_{\mathcal U}a^{(k)}_n)\);

(c) if \(a_n\to L\) in the usual sense, then \(\lim_{\mathcal U}a_n=L\).

**Proof.** Let \(a_n\in I_0=[\alpha,\beta]\). Halve \(I_0\) into two closed intervals; the set of \(n\) with \(a_n\in I_0\) is \(\mathbb N\in\mathcal U\), so by Lemma 1.1 the set of \(n\) with \(a_n\) in one of the halves, call it \(I_1\), lies in \(\mathcal U\). Continuing, we obtain nested closed intervals \(I_j\) of length \(2^{-j}(\beta-\alpha)\) with \(\{n:a_n\in I_j\}\in\mathcal U\). Let \(L\) be their common point. For \(\varepsilon>0\), some \(I_j\) lies in \((L-\varepsilon,L+\varepsilon)\), so \(\{n:|a_n-L|<\varepsilon\}\in\mathcal U\). Two different numbers with this property would give two disjoint sets in \(\mathcal U\).

(a) If \(\{|a_n-L|<\varepsilon\}\) and \(\{|b_n-L'|<\varepsilon\}\) lie in \(\mathcal U\), so does their intersection, on which \(|(a_n+b_n)-(L+L')|<2\varepsilon\); scalar multiples are similar. If \(L>L'\), take \(\varepsilon=\frac12(L-L')\): on the intersection of the two sets with \(\{a_n\le b_n\}\), which lies in \(\mathcal U\) and is not empty, we would have \(b_n<L'+\varepsilon=L-\varepsilon<a_n\le b_n\).

(b) The values lie in a compact box, on which \(\phi\) is uniformly continuous. Given \(\varepsilon\), choose \(\delta\) accordingly; the set where all \(|a^{(i)}_n-L_i|<\delta\) is a finite intersection of members of \(\mathcal U\), and on it \(|\phi(a_n)-\phi(L)|<\varepsilon\).

(c) The set \(\{n:|a_n-L|<\varepsilon\}\) is cofinite. \(\square\)

## 2. Ultrapowers of normed spaces

Let \(X\) be a real normed space and \(\ell^\infty(X)\) the space of bounded sequences in \(X\). By Lemma 1.2, \(p((a_n))=\lim_{\mathcal U}\|a_n\|\) is a seminorm on \(\ell^\infty(X)\). Let \(Q_X\) be the quotient by \(\{p=0\}\), with the norm induced by \(p\), and write \([a_n]\) for the class of \((a_n)\). The map \(x\mapsto[x]\) sending \(x\) to the constant sequence is a linear isometry \(X\to Q_X\).

**Lemma 2.1.** Every unit vector of \(Q_X\) is \([a_n]\) for a sequence with \(\|a_n\|=1\) for all \(n\), provided \(X\neq0\).

**Proof.** Let \(\lim_{\mathcal U}\|a_n\|=1\). Replace each \(a_n\neq0\) by \(a_n/\|a_n\|\) and each \(a_n=0\) by a fixed unit vector. The change at index \(n\) has norm \(|\|a_n\|-1|\), whose limit along \(\mathcal U\) is \(0\). \(\square\)

Let \(\widehat{Q_X}\) be the completion of \(Q_X\), a Banach space containing \(Q_X\) as a dense subspace. Its unit sphere is the closure of the unit sphere of \(Q_X\): a unit vector \(\xi\) of \(\widehat{Q_X}\) is a limit of vectors \(\xi_k\in Q_X\), and \(\xi_k/\|\xi_k\|\to\xi\).

## 3. Attaining the defect

**Proposition 3.1** (attainment). Let \(X,Y\) be nonzero real normed spaces and \(f:S_X\to S_Y\) a surjective isometry with defect \(M>0\). There are nonzero real Banach spaces \(\widehat X,\widehat Y\), a surjective isometry \(F:S_{\widehat X}\to S_{\widehat Y}\), vectors \(x_0,y\in S_{\widehat X}\) and \(0<t<1\) such that
\[
|D^F_q(a,c)|\le M\quad(a,c\in S_{\widehat X},\ 0\le q\le1),\qquad D^F_t(x_0,y)=\|F(x_0)-tF(y)\|-\|x_0-ty\|=M.\tag{3.1}
\]

**Proof.** Choose \(x_n,y_n\in S_X\) and \(q_n\in[0,1]\) with \(|D_{q_n}(x_n,y_n)|\to M\). Passing to a subsequence, all \(D_{q_n}(x_n,y_n)\) have the same sign. If the sign is negative, replace \(f\) by \(f^{-1}\) and \((x_n,y_n)\) by \((f(x_n),f(y_n))\); by Lemma 4.1(a) of the first lesson this changes the sign of the defects and keeps \(M\). So \(D_{q_n}(x_n,y_n)\to M\). Passing to a further subsequence, \(q_n\to t\in[0,1]\), and since \(D_q\) is \(2\)-Lipschitz in \(q\), \(D_t(x_n,y_n)\to M\). From \(|D_t|\le2\min(t,1-t)\) we get \(\frac M2\le t\le1-\frac M2\), so \(0<t<1\).

Form \(Q_X\) and \(Q_Y\). For unit vectors \([a_n]\in Q_X\) with \(\|a_n\|=1\) (Lemma 2.1) put \(F_0([a_n])=[f(a_n)]\). Since \(\lim_{\mathcal U}\|f(a_n)-f(a'_n)\|=\lim_{\mathcal U}\|a_n-a'_n\|\), this is well defined and an isometry of \(S_{Q_X}\) into \(S_{Q_Y}\); the same construction with \(f^{-1}\) gives its inverse, so \(F_0\) is surjective. For unit vectors \([a_n],[c_n]\) and \(q\in[0,1]\), Lemma 1.2(a),(b) gives
\[
\|F_0[a_n]-qF_0[c_n]\|-\|[a_n]-q[c_n]\|=\lim_{\mathcal U}D_q(a_n,c_n)\in[-M,M].
\]
For \(a=[x_n]\) and \(c=[y_n]\) the value at \(q=t\) is \(\lim_{\mathcal U}D_t(x_n,y_n)=M\) by Lemma 1.2(c).

Let \(\widehat X,\widehat Y\) be the completions of \(Q_X,Q_Y\); they are nonzero because \(X,Y\) embed in them. The isometry \(F_0\) and its inverse are uniformly continuous on the dense subsets \(S_{Q_X}\) and \(S_{Q_Y}\) of the complete spheres \(S_{\widehat X}\) and \(S_{\widehat Y}\), so they extend to isometries \(F\) and \(F'\) between these spheres, and \(F'F\) and \(FF'\) are the identity by continuity. So \(F\) is a surjective isometry. The defect bound and the equality at \((x_0,y,t)=([x_n],[y_n],t)\) pass to the extension by continuity. \(\square\)

## 4. The measure of noncompactness

For a bounded nonempty subset \(H\) of a normed space, *Kuratowski's measure of noncompactness* is
\[
\chi(H)=\inf\{\delta>0:H\text{ is covered by finitely many sets of diameter at most }\delta\}.
\]
It is monotone in \(H\), and \(\chi(H)=0\) exactly when \(H\) is totally bounded. Write \(\overline{\operatorname{conv}}\,H\) for the closed convex hull.

**Lemma 4.1.** Let \(H\) be bounded and nonempty.

(a) \(\chi(\overline H)=\chi(H)\) and \(\chi(\operatorname{conv}H)=\chi(\overline{\operatorname{conv}}\,H)=\chi(H)\).

(b) If \(C_0\supseteq C_1\supseteq\cdots\) are nonempty closed bounded subsets of a Banach space with \(\chi(C_n)\to0\), then \(\bigcap_nC_n\) is nonempty and compact.

**Proof.** (a) The closures of the sets of a cover of \(H\) cover \(\overline H\) and have the same diameters; monotonicity gives the reverse inequality. For the convex hull, cover \(H\) by nonempty sets \(H_1,\dots,H_N\) of diameter at most \(\delta\), and let \(R\) bound the norms of the points of \(H\). Each \(\operatorname{conv}H_i\) has diameter at most \(\delta\): for convex combinations \(x=\sum_j\alpha_jh_j\) and \(x'=\sum_k\beta_kh'_k\) of points of \(H_i\), \(x-x'=\sum_{j,k}\alpha_j\beta_k(h_j-h'_k)\). Grouping the terms of a convex combination according to a choice of the set \(H_i\) containing each point, every point of \(\operatorname{conv}H\) has the form \(\sum_{i=1}^N\lambda_iz_i\) with \(z_i\in\operatorname{conv}H_i\) and \((\lambda_i)\) in the simplex \(\Delta=\{\lambda\in\mathbb R^N:\lambda_i\ge0,\sum_i\lambda_i=1\}\). Given \(\eta>0\), partition \(\Delta\), a compact set, into finitely many pieces \(P_1,\dots,P_m\) of \(\ell^1\)-diameter at most \(\eta\), and let \(A_\alpha\) be the set of sums \(\sum_i\lambda_iz_i\) with \(\lambda\in P_\alpha\) and \(z_i\in\operatorname{conv}H_i\). The sets \(A_\alpha\) cover \(\operatorname{conv}H\), and for two sums in one \(A_\alpha\),
\[
\Bigl\|\sum_i\lambda_iz_i-\sum_i\lambda'_iz'_i\Bigr\|\le\Bigl\|\sum_i\lambda_i(z_i-z'_i)\Bigr\|+\Bigl\|\sum_i(\lambda_i-\lambda'_i)z'_i\Bigr\|\le\delta+R\eta.
\]
So \(\chi(\operatorname{conv}H)\le\delta+R\eta\); letting \(\eta\to0\) and \(\delta\downarrow\chi(H)\) gives \(\chi(\operatorname{conv}H)\le\chi(H)\), and monotonicity gives equality. The closed convex hull is the closure of the convex hull.

(b) Choose \(x_n\in C_n\). For each \(k\) choose \(n_k\) with \(\chi(C_{n_k})<2^{-k}\), increasing in \(k\). Inductively choose infinite sets \(N_1\supseteq N_2\supseteq\cdots\) of indices such that the points \(x_n\), \(n\in N_k\), lie in \(C_{n_k}\) and in one set of a finite cover of \(C_{n_k}\) by sets of diameter less than \(2^{-k}\): since all \(x_n\) with \(n\ge n_k\) lie in \(C_{n_k}\), infinitely many of those with \(n\in N_{k-1}\) lie in one set of the cover. Choosing increasing indices \(m_k\in N_k\) gives a sequence \((x_{m_k})\) with \(\|x_{m_k}-x_{m_l}\|<2^{-k}\) for \(l\ge k\). It converges to some \(x\), by completeness, and \(x\in C_n\) for every \(n\), since the tail of the sequence lies in the closed set \(C_n\). The intersection \(K\) is closed and \(\chi(K)\le\chi(C_n)\to0\), so \(K\) is complete and totally bounded, hence compact. \(\square\)

## 5. Schauder's theorem

**Theorem 5.1** (Schauder). Every continuous self-map \(g\) of a nonempty compact convex subset \(K\) of a normed space has a fixed point.

**Proof.** Let \(\delta>0\). By compactness there are \(P_1,\dots,P_N\in K\) such that every point of \(K\) has distance less than \(\delta\) from some \(P_i\). For \(x\in K\) put
\[
\lambda_i(x)=\frac{\max\{\delta-\|P_i-g(x)\|,0\}}{\sum_j\max\{\delta-\|P_j-g(x)\|,0\}}.
\]
The denominator is positive because \(g(x)\in K\), so the \(\lambda_i\) are continuous functions with values in the simplex \(\Delta\subseteq\mathbb R^N\). The map \(a\mapsto\bigl(\lambda_i(\sum_ja_jP_j)\bigr)_i\) is a continuous self-map of the compact convex set \(\Delta\) (the points \(\sum_ja_jP_j\) lie in \(K\) by convexity). By Brouwer's theorem it has a fixed point \(a\). For \(x=\sum_ja_jP_j\) we have \(a_i=\lambda_i(x)\), and since \(\lambda_i(x)>0\) only when \(\|P_i-g(x)\|<\delta\),
\[
\|x-g(x)\|=\Bigl\|\sum_i\lambda_i(x)\bigl(P_i-g(x)\bigr)\Bigr\|<\delta.
\]
Applying this with \(\delta=1/k\) gives points \(x_k\in K\) with \(\|x_k-g(x_k)\|<1/k\); a limit point \(x\) of \((x_k)\) in \(K\) satisfies \(g(x)=x\) by continuity. \(\square\)

## 6. Darbo's theorem

**Theorem 6.1** (Darbo). Let \(C\) be a nonempty closed bounded convex subset of a Banach space, \(0\le\gamma<1\), and \(g:C\to C\) continuous with \(\chi(g(H))\le\gamma\chi(H)\) for every nonempty \(H\subseteq C\). Then \(g\) has a fixed point.

**Proof.** Put \(C_0=C\) and \(C_{n+1}=\overline{\operatorname{conv}}\,g(C_n)\). By induction these are nonempty closed bounded convex sets with \(C_{n+1}\subseteq C_n\): \(C_1\subseteq C\) because \(C\) is closed and convex, and \(C_n\subseteq C_{n-1}\) gives \(g(C_n)\subseteq g(C_{n-1})\). By Lemma 4.1(a), \(\chi(C_{n+1})=\chi(g(C_n))\le\gamma\chi(C_n)\), so \(\chi(C_n)\le\gamma^n\chi(C)\to0\). By Lemma 4.1(b), \(K=\bigcap_nC_n\) is nonempty and compact; it is convex, and \(g(K)\subseteq K\) because \(g(x)\in g(C_n)\subseteq C_{n+1}\) for \(x\in K\) and every \(n\). Theorem 5.1 gives a fixed point in \(K\). \(\square\)

## 7. Exercises

**Exercise 7.1** (easy). Show that the sequence \(a_n=(-1)^n\) has \(\lim_{\mathcal U}a_n=1\) if the set of even numbers belongs to \(\mathcal U\), and \(-1\) otherwise.

**Exercise 7.2** (easy). Show that Theorem 6.1 contains two classical statements: (i) a map \(g:C\to C\) with \(\|g(x)-g(x')\|\le\gamma\|x-x'\|\), \(\gamma<1\), has a fixed point; (ii) a continuous \(g:C\to C\) with \(g(C)\) totally bounded has a fixed point.

**Exercise 7.3** (medium). Let \(B\) be the closed unit ball of a finite-dimensional normed space. Show that \(\chi(B)=0\), and that \(\chi(B)\le2\) for the unit ball of every normed space.

**Exercise 7.4** (medium). In Proposition 3.1, explain why the defect of \(F\) equals \(M\), and why one cannot in general take \(F=f\): give a reason why the supremum defining \(M\) need not be attained in \(X\).

## 8. Solutions

**7.1.** If the even numbers form a set in \(\mathcal U\), then \(\{n:|a_n-1|<\varepsilon\}\) contains it; otherwise the odd numbers lie in \(\mathcal U\) by Lemma 1.1 and the limit is \(-1\).

**7.2.** (i) A \(\gamma\)-Lipschitz map sends a set covered by finitely many sets of diameter at most \(\delta\) to one covered by finitely many sets of diameter at most \(\gamma\delta\), so \(\chi(g(H))\le\gamma\chi(H)\). (ii) If \(g(C)\) is totally bounded, then \(\chi(g(H))=0\) for every \(H\subseteq C\).

**7.3.** A finite-dimensional unit ball is compact, hence totally bounded. In general \(B\) itself has diameter at most \(2\).

**7.4.** By (3.1) the defect of \(F\) is at most \(M\), and it is attained at \((x_0,y,t)\). In \(X\) the supremum is over a set that need not be compact: the maximizing triples \((x_n,y_n,q_n)\) need not have convergent subsequences when \(X\) is infinite-dimensional, and the ultrapower provides a space in which the limit configuration exists.

## References

- [OpenAI-T] OpenAI, *A positive solution to Tingley's problem*, OpenAI Math Release preprint, 23 September 2026, Section 3 and Appendix A. https://github.com/openai/math/blob/main/preprints/A-positive-solution-to-Tingleys-problem-September-23-2026
