# Sizes that enforce the patterns

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The previous lesson, [Coordinates, cells and items](coordinates-cells-and-items.md), listed the \(5B\) items of the reduction with their roles, subclasses, labels and coordinates. This lesson gives them rational sizes. Each size is \(1/5\) plus three perturbations of decreasing order: a *primary score* that detects whether five items follow one of the four table patterns, a *secondary score* that compares labels, and the coordinate. A bin then holds at most five items; a five-item bin can fit only if its primary score is not positive; and a good tuple fits exactly when its coordinates sum to at most zero. The scores sum to zero over the whole instance, which limits how far any packing with few extra bins can stray from the patterns: Lemma 3.1 below loses at most \(3K\) anchors per vertex, a bound that does not grow with the number of positions. We keep the notation of the previous lesson; in particular the role and subclass names and the constants \(P_0,K\) of (1.1) there.

## 1. Two scores and the sizes

For a collection of items let \(N_s\) be the number of items of subclass \(s\) and \(N_r\) the number of items of role \(r\). Consider the following ten homogeneous linear equations in these counts: the five *role equations*
\[
5N_r-\sum_sN_s=0\qquad(r=X,A,U,D,F,\ \text{in this order}),
\]
where \(\sum_s\) runs over all thirteen subclasses, followed by the five *pattern equations*
\[
\begin{aligned}
N_{T^+}+N_{T^-}-N_{F^{\mathrm T}}&=0,\\
N_Z-N_{F^{\mathrm T}}-N_{F^{\mathrm M}}&=0,\\
N_{U^+}+N_{U^-}-N_{F^{\mathrm T}}-N_{F^{\mathrm M}}&=0,\\
N_{D^{\mathrm M}}-N_{F^{\mathrm T}}-N_{F^{\mathrm M}}&=0,\\
N_{T^-}-N_{U^-}&=0.
\end{aligned}\tag{1.1}
\]
Number them \(j=0,\ldots,9\) in the order given, and let \(\delta_j(i)\) be the coefficient that one item \(i\) contributes to the left side of equation \(j\); it depends only on the subclass of \(i\). An item of role \(r\) contributes \(4\) to its own role equation and \(-1\) to the other four; its contributions to (1.1) lie in \(\{-1,0,1\}\). The *primary score* of an item is the integer
\[
p(i)=\sum_{j=0}^9100^j\delta_j(i),\qquad|p(i)|\leq4\sum_{j=0}^9100^j<P_0=100^{11}.
\]
For a label \(v\) put \(Q_v=3^v\). The *secondary score* is \(q(i)=Q_v\) for a row or a local auxiliary of label \(v\), \(q(i)=-2Q_v\) for an anchor of label \(v\), and \(q(i)=0\) for global auxiliaries and flags. The *size* of item \(i\) is
\[
a_i=\frac15+\gamma p(i)+\mu q(i)+\nu w(i),\qquad\gamma=\frac1{1000P_0},\quad\mu=\frac\gamma{1000Q_n},\quad\nu=\frac\mu{1000}.\tag{1.2}
\]
The output of the reduction is the list of these sizes, one for each item; roles, labels and coordinates are only used to analyse it.

## 2. The scalar encoding

**Lemma 2.1 (scalar encoding).** (a) Every size lies in \((1/6,1)\); so every bin holds at most five items.

(b) A five-item tuple has total primary score zero exactly when it is a table tuple.

(c) A five-item tuple that fits into a bin has total primary score at most \(0\); if that score is \(0\), its total secondary score is at most \(0\); if both are \(0\), it fits exactly when \(\sum_iw(i)\leq0\).

(d) Over the whole instance, \(\sum_ip(i)=0\) and \(\sum_iq(i)=0\).

*Proof.* (a) Since \(|p(i)|<P_0\), \(|q(i)|\leq2Q_n\) and \(|w(i)|\leq6\) (Lemma 5.1 of the previous lesson),
\[
\Bigl|a_i-\frac15\Bigr|<\frac1{1000}+\frac2{10^6P_0}+\frac6{10^9P_0Q_n}<\frac1{30},
\]
so \(a_i\in(\frac16,\frac7{30})\). Six items would exceed one.

(b) For a five-item tuple let \(E_j\) be the total of the left side of equation \(j\). The role totals \(E_0,\ldots,E_4\) are \(5N_r-5\in[-5,20]\), and \(E_5,\ldots,E_9\in[-5,5]\): all ten are integers of absolute value less than \(100\). The total primary score is \(\sum_j100^jE_j\). If it is zero, then \(E_0\) is divisible by \(100\), hence \(E_0=0\); dividing by \(100\) and repeating gives \(E_j=0\) for all \(j\). Conversely, if all \(E_j\) vanish, the score is zero. So it remains to show that the ten equations hold for a five-item tuple exactly when it is a table tuple.

If they hold, the role equations give \(N_r=1\) for each role. If the flag is \(F^{\mathrm T}\), the first equation of (1.1) makes the row a tree row, the next three make the anchor \(Z\), the global item \(U^+\) or \(U^-\) and the local item \(D^{\mathrm M}\), and the last pairs \(T^-\) with \(U^-\) (and hence \(T^+\) with \(U^+\)). If the flag is \(F^{\mathrm M}\), the first equation excludes tree rows, so the row is \(S\); the anchor is \(Z\), the local item \(D^{\mathrm M}\), the global item \(U^+\) or \(U^-\), and the last equation, with no \(T^-\), excludes \(U^-\). If the flag is \(F^{\mathrm G}\), the equations exclude tree rows, \(Z\), \(U^\pm\) and \(D^{\mathrm M}\), so the tuple is \(S,Y,W,D^{\mathrm G},F^{\mathrm G}\). These are the four patterns, and each of them satisfies all ten equations.

(c) A five-item tuple has total size \(1+\gamma\sum p+\mu\sum q+\nu\sum w\). The last two terms together have absolute value at most \(10Q_n\mu+30\nu\), and
\[
\frac{10Q_n\mu+30\nu}\gamma=\frac1{100}+\frac3{10^5Q_n}<1 .
\]
So an integer primary total of at least \(1\) makes the total size exceed one. If the primary total is \(0\), then \(|\nu\sum w|\leq30\nu=\frac3{100}\mu<\mu\), so a secondary total of at least \(1\) makes the size exceed one. If both vanish, the size is \(1+\nu\sum w\).

(d) The whole inventory satisfies the ten equations: every role has \(B\) items; the tree rows and the flags \(F^{\mathrm T}\) both number \(\sum_vt_v\); the deadlines, the global items \(U^\pm\) and the items \(D^{\mathrm M}\) each number \(\sum_v(t_v+J_v)\), as do the flags \(F^{\mathrm T}\) and \(F^{\mathrm M}\) together; and the rows \(T^-\) and the items \(U^-\) both number \(\sum_vt_{v,-}\). Hence \(\sum_ip(i)=\sum_j100^j\cdot0=0\). For each label \(v\), there are \(t_v+2J_v\) rows, anchors and local auxiliaries each (Lemma 5.1 of the previous lesson), contributing \((1-2+1)Q_v(t_v+2J_v)=0\). \(\square\)

The proof of (c) shows more: a fitting five-item tuple that is not a table tuple has primary total at most \(-1\), and a fitting table tuple with unequal labels has secondary total at most \(-1\) (Section 3).

## 3. Few items leave the patterns

**Lemma 3.1 (good anchors under an additive allowance).** In every packing of the instance into at most \(B+c\) bins, fewer than \(K\) items lie outside five-item table tuples, and for every label \(v\) at most \(3K\) anchors of label \(v\) lie outside good tuples. The second bound applies jointly to the deadlines and keys of label \(v\), so to every subset of them.

*Proof.* Let the packing have \(N\leq B+c\) bins. Since a bin holds at most five items, \(5N\geq5B\); the number of empty places, \(5N-5B\leq5c\), bounds the number of bins with fewer than five items, which therefore hold at most \(25c\) items. Since the primary scores of all items add up to zero (Lemma 2.1(d)), the full bins together have primary total equal to minus the total of the at most \(25c\) items in the other bins, which is at least \(-25cP_0\). Every full bin has primary total at most \(0\) (Lemma 2.1(c)), and a nonzero total is at most \(-1\); so at most \(25cP_0\) full bins have a nonzero primary total. The items outside full bins of primary total zero number at most
\[
25c+5\cdot25cP_0=25c(1+5P_0)<K,
\]
and the full bins of primary total zero are exactly the table tuples (Lemma 2.1(b)).

*Labels.* In a table tuple let \(v_X,v_A,v_D\) be the labels of row, anchor and local item. Its secondary total \(Q_{v_X}+Q_{v_D}-2Q_{v_A}\) is at most \(0\) if it fits (Lemma 2.1(c)). If \(v_X>v_A\), then \(Q_{v_X}\geq3Q_{v_A}\) and the total is positive; the same holds for \(v_D\). So
\[
v_X\leq v_A,\qquad v_D\leq v_A\tag{3.1}
\]
in every table tuple of the packing.

*Conservation over label prefixes.* Fix \(h\in\{0,\ldots,n\}\), put \(S=\{1,\ldots,h\}\), and let \(r\in\{X,D\}\). Let \(O_A(S)\) and \(O_r(S)\) be the numbers of anchors, respectively items of role \(r\), with label in \(S\) that lie outside table tuples, and let \(E_r(S)\) be the number of table tuples whose role-\(r\) item has label in \(S\) and whose anchor has label outside \(S\). There are \(N_S=\sum_{v\in S}(t_v+2J_v)\) anchors and as many items of role \(r\) with label in \(S\). The table tuples whose anchor is in \(S\) number \(N_S-O_A(S)\), and by (3.1) their role-\(r\) item is in \(S\). The table tuples whose role-\(r\) item is in \(S\) number \(N_S-O_r(S)\); they are those with anchor in \(S\) and the \(E_r(S)\) others. Hence
\[
E_r(S)=O_A(S)-O_r(S)\leq O_A(S)<K.\tag{3.2}
\]

*Anchors of label \(v\).* An anchor of label \(v\) outside good tuples is (i) outside table tuples (fewer than \(K\) items in all), or (ii) in a table tuple whose row has a different, hence smaller, label, or (iii) in a table tuple whose local item has a smaller label. The tuples in (ii) are counted by \(E_X(\{1,\ldots,v-1\})<K\), those in (iii) by \(E_D(\{1,\ldots,v-1\})<K\). So there are fewer than \(3K\). \(\square\)

The point of the conservation identity is that the loss at a vertex is bounded independently of the number of its job positions, which grows with the graph. Summed over all vertices, at most \(3nK\) anchors are lost.

## 4. Good tuples

**Lemma 4.1 (completion and key inequalities).** A good tuple has primary and secondary totals zero, so it fits exactly when its coordinates sum to at most zero. Concretely:

(a) A good tuple of kind M, with row baseline \(b\), deadline \(z\), global item \(U\) and local item \(D\), fits if and only if its completion
\[
h=b-\Delta\,\mathbf 1\{\text{the row is short}\}-\operatorname{len}(U)-\operatorname{len}(D)
\]
satisfies \(h\leq z\). Always \(h\leq b\).

(b) A good tuple of kind G, with key at position \(r=(e,j)\), row at position \(r'\) and edge resource belonging to edge \(f\), fits if and only if
\[
b_{r'}-b_r+\beta_f-\beta_e+\Delta\bigl(\mathbf 1\{\text{nonpermit}\}-\mathbf 1\{\text{the row is short}\}\bigr)\leq0.\tag{4.1}
\]
If it fits, then \(r'\leq r\) and \(f\leq e\). If it fits and the row is a long row at position \(r\), its resource is a permit of edge \(e\) or belongs to an earlier edge. If \(r'=r\) and \(f=e\), it fits exactly when the row is short or the resource is a permit.

*Proof.* A table tuple has primary total zero; equal labels give secondary total \(Q_v+Q_v-2Q_v=0\). Lemma 2.1(c) applies.

(a) The coordinates are \(b\) or \(b-\Delta\) (row), \(-z\) (deadline), \(-\operatorname{len}(U)\), \(-\operatorname{len}(D)\) and \(0\) (flag); their sum is \(h-z\). Lengths and \(\Delta\) are nonnegative, so \(h\leq b\).

(b) The coordinates are \(b_{r'}\) or \(b_{r'}-\Delta\) (row), \(-b_r-\beta_e\) (key), \(\beta_f\) or \(\beta_f+\Delta\) (resource), \(0\) and \(0\); their sum is the left side of (4.1). If \(r'>r\), then by Lemma 2.1 of the previous lesson \(b_{r'}-b_r=g(H_{r'}-H_r)\geq g(\theta_e+1)\), while \(\beta_f-\beta_e\geq-g\theta_e\) and the last term is at least \(-\Delta\); the sum is at least \(g-\Delta>0\). If \(f>e\), then \(\beta_f-\beta_e\geq g(H_{e,R}+1)\), while \(b_{r'}-b_r\geq-gH_r\geq-gH_{e,R}\); again the sum is at least \(g-\Delta>0\). For a long row at position \(r\) the sum is \(\beta_f-\beta_e+\Delta\mathbf 1\{\text{nonpermit}\}\); fitting forces \(f\leq e\), and if \(f=e\) a nonpermit leaves \(\Delta>0\). If \(r'=r\) and \(f=e\), the sum is \(\Delta(\mathbf 1\{\text{nonpermit}\}-\mathbf 1\{\text{short}\})\). \(\square\)

**Corollary 4.2 (intervals of good M tuples).** In a good tuple of kind M, the interval \([h,b)\):

(a) has length at most \(\lambda_\ell+\Delta\) if the global item has length \(0\) and the local item length \(\lambda_\ell\);

(b) is empty if both auxiliary lengths are \(0\) and the row is not short, and equals the job test interval \([b_r-\Delta,b_r)\) if both lengths are \(0\) and the row is a short job row at position \(r\);

(c) lies in \((2,5]\) if the row is a minus tree row, and in \((-2,1]\) if the row is a plus tree row or a job row.

In particular an interval of a minus row contains no point of a plus test interval, and an interval of a plus or job row no point of a minus test interval.

*Proof.* (a) and (b) are read off from the formula for \(h\). (c) Minus rows have baseline at least \(4\), are never short, and \(h\geq4-1-\lambda_1>2\). Plus and job rows have baseline at most \(1\), and \(h\geq b-\Delta-1-\lambda_1>-2\). Plus test intervals lie in \([0,\frac9{16})\) and minus test intervals in \([4,5]\). \(\square\)

## 5. The construction runs in polynomial time

For fixed \(c\) and \(\rho\), the trees, \(L\), the quotas, \(P\) and \(D_*\) are constants, and so is \(t_v=t\) for every label. The number of positions is \(mR\) with \(R=100(P+nK+1)=O(n+1)\), and \(B=nt+4dmR\) (since \(\sum_vJ_v=2dmR\)). So all items can be listed in time polynomial in the size of the graph. All coordinates are rationals with the common denominator
\[
D_{\mathrm{geom}}=160(R+1)^m[100(D_*+1)]^L,
\]
which accounts for \(g\), every \(\lambda_\ell\), \(\Delta\), all cell endpoints, baselines and offsets; by (1.2) all sizes have the common denominator \(10^9P_03^nD_{\mathrm{geom}}\). These have \(O(n+m\log(n+2))\) bits, with constants depending on \(c\) and \(\rho\), and the numerators of the sizes, which lie in \((0,1)\), are no longer. Powers, products and sums of such integers take polynomial time. This proves the running-time statement of Theorem 4.1 of [Bin packing and the configuration program](bin-packing-and-the-configuration-program.md), and the sizes lie in \((1/6,1)\) by Lemma 2.1.

## 6. Exercises

**6.1.** Compute the ten coefficients \(\delta_0,\ldots,\delta_9\) for an item of subclass \(T^-\) and for a flag \(F^{\mathrm M}\), and check that they sum to the coefficients of a pattern in which they occur.

**6.2.** Show that a five-item tuple consisting of a row \(S\), an anchor \(Z\), items \(U^+\), \(D^{\mathrm M}\) and a flag \(F^{\mathrm T}\) has total primary score at least \(1\) in absolute value, and determine its sign. Can it fit into a bin?

**6.3.** In the proof of Lemma 3.1, why does the bound on items outside table tuples not depend on the graph?

**6.4.** Give an example, in terms of labels, of a table tuple that fits although it is not good. Which term of Lemma 3.1 counts its anchor?

**6.5.** Show from Lemma 4.1(b) that in a good tuple of kind G the key at position \(r=(e,j)\) can be matched with a short row of the same position and a nonpermit of edge \(e\), but not with a long row of the same position and a nonpermit of edge \(e\).

## 7. Solutions

**6.1.** A row \(T^-\) has role \(X\): \(\delta_0=4\), \(\delta_1=\cdots=\delta_4=-1\); in (1.1) it appears in the first equation (\(+1\)) and the last (\(+1\)): \(\delta_5=1\), \(\delta_6=\delta_7=\delta_8=0\), \(\delta_9=1\). A flag \(F^{\mathrm M}\) has role \(F\): \(\delta_0=\cdots=\delta_3=-1\), \(\delta_4=4\); in (1.1): \(\delta_5=0\), \(\delta_6=\delta_7=\delta_8=-1\), \(\delta_9=0\). In the pattern \(S,Z,U^+,D^{\mathrm M},F^{\mathrm M}\) the five items together give \(0\) in every coordinate; for instance in equation 6 the anchor \(Z\) gives \(+1\) and the flag \(-1\).

**6.2.** Each role occurs once, so the five role totals vanish. In the first equation of (1.1) the tuple has no tree row and one flag \(F^{\mathrm T}\): \(E_5=-1\). The other four totals are \(E_6=1-1=0\), \(E_7=1-1=0\), \(E_8=1-1=0\) and \(E_9=0\). So the primary total is \(-100^5\), negative and nonzero. Its size is \(1-100^5\gamma+\mu\sum q+\nu\sum w<1\), since the last two terms are smaller than \(\gamma\) in absolute value; so it fits into a bin. It is one of the tuples outside table tuples counted in Lemma 3.1.

**6.3.** It is bounded through the number of extra places, \(5c\), and the largest possible primary score, \(P_0\); neither depends on the graph.

**6.4.** A row of label \(1\), a deadline of label \(2\) and a local item of label \(2\), with the rest of a pattern M: the secondary total is \(3+9-18<0\), so the tuple fits whatever the coordinates. Its anchor is counted by \(E_X(\{1\})\).

**6.5.** With \(r'=r\), \(f=e\), the left side of (4.1) is \(\Delta(1-1)=0\) for a short row and a nonpermit, and \(\Delta(1-0)>0\) for a long row and a nonpermit.

## References

- [OpenAI-BP] OpenAI, *Additive hardness and unbounded configuration gaps in bin packing*, OpenAI Math Release preprint, 24 September 2026, Section 3. https://github.com/openai/math/tree/main/preprints/Additive-hardness-and-unbounded-configuration-gaps-in-bin-packing-September-24-2026
- K. Jansen, M. Pirotton and M. Tutas (2025) and J. M. Anthonisse (1973) are named for credit for aggregating bounded integer equations into a single one; the course proves the version it uses.
