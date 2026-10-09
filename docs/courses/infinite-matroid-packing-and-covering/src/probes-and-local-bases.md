# Probes and local bases

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The bases of the self-dual matroid \(Q\) will be chosen class by class: a *class* consists of the subsets of \(E_0\) that differ from a fixed *prototype* \(T\) by a set of density zero. Inside one class, this lesson defines real-valued *probes* that measure how much a set exceeds or falls short of \(T\), first in a finite prefix of blocks and then in the tail. Two families of candidate bases are cut out by a half-open condition on the lower or upper limit of the probes. Finite exchanges of one element for another do not change these limits, so the families are closed under such exchanges, and an interpolation argument shows that every interval of sets contains a candidate, or lies on one side of one (Proposition 2.3). This interval property is what will give maximal extensions in [Assembling a self-dual matroid](assembling-a-self-dual-matroid.md). Notation is that of [Ideals, ultrafilters and an ordinal rank](ideals-ultrafilters-and-an-ordinal-rank.md); complements are taken in \(E_0\) and written \(X^c\).

## 1. Probes

Fix \(T\subseteq E_0\) such that \(T\) and \(T^c\) are \(\mathcal J_0\)-positive, and put
\[
\mathcal C(T)=\{X\subseteq E_0:X\mathbin\triangle T\in\mathcal J_0\}.
\]
Every \(X\in\mathcal C(T)\) and its complement are \(\mathcal J_0\)-positive: otherwise \(T\subseteq X\cup(X\mathbin\triangle T)\) or \(T^c\subseteq X^c\cup(X\mathbin\triangle T)\) would lie in \(\mathcal J_0\). For \(n\ge1\) let \(V_n=W_0\cup\dots\cup W_{n-1}\) and \(c_n=|V_n|\), and for \(X\in\mathcal C(T)\) define
\[
p_n(X)=|X\cap V_n|-|T\cap V_n|,\qquad d_m(X)=\frac{|X\cap W_m|-|T\cap W_m|}{|W_m|},
\]
\[
f_n(X)=p_n(X)+c_n\Bigl(\sup_{m\ge n}d_m(X)+\inf_{m\ge n}d_m(X)\Bigr),
\]
and \(\ell(X)=\liminf_nf_n(X)\), \(h(X)=\limsup_nf_n(X)\), with values in \([-\infty,+\infty]\). When the prototype must be shown we write \(f_n^T\), \(\ell_T\), \(h_T\). The two families of **local bases** are
\[
\mathcal B^-(T)=\{X\in\mathcal C(T):-1<\ell(X)\le0\},\qquad\mathcal B^+(T)=\{X\in\mathcal C(T):0\le h(X)<1\}.
\]
By Lemma 1.1 of [Ideals, ultrafilters and an ordinal rank](ideals-ultrafilters-and-an-ordinal-rank.md), \(|W_k|=2w_k\ge2\sum_{m<k}|W_m|\), so
\[
|W_k|\ge2c_n\qquad(k\ge n). \tag{1.1}
\]

**Lemma 1.1** (Probe properties). For \(X,Y\in\mathcal C(T)\):

1. \(d_m(X)\to0\) and \(p_n(X)/c_n\to0\).
2. If \(X\subseteq Y\), then \(f_n(Y)-f_n(X)\ge|(Y\setminus X)\cap V_n|\).
3. Adding or deleting one element changes every \(f_n\) by at most one. If \(Y\) arises from \(X\) by finitely many changes with net change \(b\) in cardinality, then \(f_n(Y)=f_n(X)+b\) for all large \(n\); so \(\ell(Y)=\ell(X)+b\) and \(h(Y)=h(X)+b\).
4. \(f_n^{T^c}(X^c)=-f_n^T(X)\); consequently \(\mathcal B^+(T^c)=\{B^c:B\in\mathcal B^-(T)\}\) and \(\mathcal B^-(T^c)=\{B^c:B\in\mathcal B^+(T)\}\).

*Proof.* (1) \(|d_m(X)|\le|(X\mathbin\triangle T)\cap W_m|/|W_m|\to0\). Also \(p_n(X)=\sum_{m<n}|W_m|d_m(X)\); given \(\varepsilon\), the terms with \(m\ge m_0\) contribute at most \(\varepsilon c_n\), and the first \(m_0\) terms contribute a fixed amount, which is \(o(c_n)\).

(2) Each \(d_m\) increases, hence so do both tail extrema, and the prefix count increases by \(|(Y\setminus X)\cap V_n|\).

(3) A change in a block \(W_k\) with \(k<n\) changes only \(p_n\), by one. A change in \(W_k\) with \(k\ge n\) changes only \(d_k\), by \(1/|W_k|\), so each tail extremum moves by at most \(1/|W_k|\) and \(f_n\) by at most \(2c_n/|W_k|\le1\) by (1.1). Once \(n\) exceeds every block touched by a finite modification, the tails agree and \(p_n\) changes by exactly \(b\).

(4) Complementing both \(X\) and \(T\) negates \(p_n\) and every \(d_m\), and the supremum of the negatives is minus the infimum. So \(\ell_{T^c}(X^c)=-h_T(X)\) and \(h_{T^c}(X^c)=-\ell_T(X)\), and the half-open conditions correspond. \(\square\)

**Lemma 1.2** (Continuity inside an interval). Let \(I,Y\in\mathcal C(T)\) and \(I\subseteq X_k\subseteq Y\) for \(k\ge1\), and suppose that every element of \(E_0\) eventually belongs to \(X_k\) exactly when it belongs to a set \(X\). Then \(X\in\mathcal C(T)\) and \(f_n(X_k)\to f_n(X)\) for every fixed \(n\).

*Proof.* \(I\subseteq X\subseteq Y\) and \(Y\setminus I\in\mathcal J_0\), so \(X\in\mathcal C(T)\). On the finite set \(V_n\), \(X_k\) eventually agrees with \(X\). For all \(m\), \(|d_m(X_k)-d_m(X)|\le|(Y\setminus I)\cap W_m|/|W_m|\), and for every finite set of blocks the difference is eventually zero; since the bound tends to zero as \(m\to\infty\), \(\sup_m|d_m(X_k)-d_m(X)|\to0\). Tail extrema move by at most this supremum. \(\square\)

**Lemma 1.3** (Antichains and exchanges). \(T\) belongs to \(\mathcal B^-(T)\) and to \(\mathcal B^+(T)\). Both families are antichains under inclusion, and both are closed under replacing finitely many elements by equally many others.

*Proof.* All probes of \(T\) vanish. A balanced finite change preserves the class and, by Lemma 1.1(3), the limits. Suppose \(X\subsetneq Y\) are both in \(\mathcal B^-(T)\). If \(Y\setminus X\) is finite with \(k\ge1\) elements, then \(\ell(Y)=\ell(X)+k>0\). If it is infinite, then \(|(Y\setminus X)\cap V_n|\to\infty\), while \(f_n(X)\) is eventually bounded below because \(\ell(X)>-1\); by Lemma 1.1(2), \(f_n(Y)\to\infty\). Both contradict \(\ell(Y)\le0\). For \(\mathcal B^+(T)\) use Lemma 1.1(4). \(\square\)

## 2. Moving the probes

**Lemma 2.1** (Divergence from a positive pool). Let \(X\in\mathcal C(T)\). If \(G\subseteq X^c\) is \(\mathcal J_0\)-positive, there is \(P\subseteq G\) with \(P\in\mathcal J_0\) and \(f_n(X\cup P)\to+\infty\). If \(G\subseteq X\) is \(\mathcal J_0\)-positive, there is \(P\subseteq G\) with \(P\in\mathcal J_0\) and \(f_n(X\setminus P)\to-\infty\).

*Proof.* Choose \(\delta>0\) such that \(|G\cap W_m|\ge\delta|W_m|\) for infinitely many \(m\), put \(a_n=\sup_{m\ge n}|d_m(X)|\), and by Lemma 1.1(1) choose increasing integers \(N_j\) with
\[
\frac{|p_n(X)|}{c_n}+2a_n+\frac1{\sqrt{c_n}}\le2^{-j}\qquad(n\ge N_j). \tag{2.1}
\]
Let \(j_0\) be such that \(b_j=2^{1-j}<\delta\) for \(j\ge j_0\). For each \(j\ge j_0\) choose a block \(m_j\ge N_{j+1}\), increasing in \(j\), with \(|G\cap W_{m_j}|\ge\delta|W_{m_j}|\) and \(1/|W_{m_j}|\le\delta-b_j\), and select exactly \(\lceil b_j|W_{m_j}|\rceil\le\delta|W_{m_j}|\) elements of \(G\cap W_{m_j}\). Let \(P\) be the union of the selections. Its density in \(W_{m_j}\) is at most \(b_j+1/|W_{m_j}|\), which tends to zero, so \(P\in\mathcal J_0\).

Let \(N_j\le n<N_{j+1}\) with \(j\ge j_0\). The block \(m_j\) belongs to the tail \(m\ge n\), and \(d_{m_j}(X\cup P)\ge b_j-a_n\); every \(d_m(X\cup P)\ge-a_n\) for \(m\ge n\); and \(p_n(X\cup P)\ge p_n(X)\). With (2.1),
\[
\frac{f_n(X\cup P)}{c_n}\ge-\frac{|p_n(X)|}{c_n}+b_j-2a_n\ge2^{-j}+\frac1{\sqrt{c_n}},
\]
so \(f_n(X\cup P)\ge\sqrt{c_n}\to\infty\). For deletions apply this to \(X^c\), the prototype \(T^c\) and the pool \(G\subseteq(X^c)^c\), and use Lemma 1.1(4). \(\square\)

**Lemma 2.2** (Interpolation). If \(I\subseteq Y\) are in \(\mathcal C(T)\) with \(\ell(I)\le-1\) and \(\ell(Y)>0\), there is \(B\in\mathcal B^-(T)\) with \(I\subseteq B\subseteq Y\).

*Proof.* *Finite limits.* If \(\ell(I)=a\) is finite, \(Y\setminus I\) has at least \(\lfloor-a\rfloor\) elements: a finite gap of \(g\) elements gives \(\ell(Y)=a+g\) by Lemma 1.1(3), so \(g>-a\). Adding \(\lfloor-a\rfloor\) elements of the gap to \(I\) gives lower limit \(a+\lfloor-a\rfloor\in(-1,0]\). If \(\ell(Y)=b\) is finite, deleting \(\lceil b\rceil\) gap elements from \(Y\) gives lower limit in \((-1,0]\); there are enough, since a finite gap of \(g\) elements gives \(\ell(I)=b-g\), so \(g\ge b+1\).

*Infinite limits.* Let \(\ell(I)=-\infty\) and \(\ell(Y)=+\infty\). Put \(X_0=Y\). At stage \(j\ge1\): if \(f_n(X_{j-1})\le0\) for some \(n\ge j\), put \(X_j=X_{j-1}\). Otherwise choose \(M_j\ge j\) with
\[
2c_j\sup_{m\ge M_j}\frac{|(Y\setminus I)\cap W_m|}{|W_m|}<2^{-j}, \tag{2.2}
\]
possible since \(Y\setminus I\in\mathcal J_0\), and delete the elements of \(X_{j-1}\setminus I\) lying in blocks \(m\ge M_j\) one at a time, in order of increasing block, stopping as soon as \(f_n\le0\) for some \(n\ge j\); let \(X_j\) be the result.

The stage stops after finitely many deletions. If all eligible elements were deleted, the result would differ from \(I\) by finitely many elements and have \(\ell=-\infty\), so some \(f_n\) with \(n\ge j\) would be negative there; by Lemma 1.2 the same \(f_n\) is negative after finitely many of the deletions. Just before the last deletion all \(f_n\) with \(n\ge j\) were positive, so by Lemma 1.1(3)
\[
f_n(X_j)\ge-1\qquad(n\ge j) \tag{2.3}
\]
at every stage with deletions. For \(n<j\), a stage does not change \(p_n\), since it only deletes in blocks \(m\ge M_j\ge j>n\), and each tail extremum decreases by at most the supremum in (2.2); as \(c_n\le c_j\), the stage lowers \(f_n\) by less than \(2^{-j}\).

Let \(X_\infty=\bigcap_jX_j\). Then \(I\subseteq X_\infty\subseteq Y\), and \(f_n(X_k)\to f_n(X_\infty)\) by Lemma 1.2. Every stage leaves some \(n\ge j\) with \(f_n(X_j)\le0\); deletions only lower probes (Lemma 1.1(2)), so \(f_n(X_\infty)\le0\) for infinitely many \(n\), and \(\ell(X_\infty)\le0\). Some stage \(j_0\) makes deletions, since otherwise \(Y\) would have nonpositive probes of arbitrarily large index. Fix \(n\ge j_0\). After stage \(j_0\), \(f_n\ge-1\) by (2.3); each later stage \(j\le n\) either does nothing or restores \(f_n\ge-1\) by (2.3); stages \(j>n\) lower \(f_n\) by less than \(2^{-j}\) each. In the limit \(f_n(X_\infty)\ge-1-2^{-n}\), so \(-1\le\ell(X_\infty)\le0\). If \(\ell(X_\infty)>-1\), take \(B=X_\infty\). If \(\ell(X_\infty)=-1\), add one element of \(Y\setminus X_\infty\) (this set is infinite, as \(\ell(Y)=+\infty\)), obtaining lower limit \(0\). \(\square\)

**Proposition 2.3** (Interval alternatives). Let \(\sigma\in\{-,+\}\) and \(I\subseteq Y\subseteq E_0\), and suppose \(T\setminus I\in\mathcal J_0\) or \(Y\setminus T\in\mathcal J_0\). Then some \(B\in\mathcal B^\sigma(T)\) satisfies
\[
B\subseteq I,\qquad\text{or}\qquad I\subseteq B\subseteq Y,\qquad\text{or}\qquad Y\subseteq B. \tag{2.4}
\]

*Proof.* *Step 1 (correcting one set, rule \(-\)).* Let \(X\in\mathcal C(T)\). If \(\ell(X)\le-1\) and \(G\subseteq X^c\) is positive, Lemma 2.1 gives \(P\subseteq G\) in \(\mathcal J_0\) with \(\ell(X\cup P)=+\infty\), and Lemma 2.2 gives \(B\in\mathcal B^-(T)\) with \(X\subseteq B\subseteq X\cup G\). If \(\ell(X)>0\) and \(G\subseteq X\) is positive, the deletion version gives \(B\in\mathcal B^-(T)\) with \(X\setminus G\subseteq B\subseteq X\). If \(-1<\ell(X)\le0\), then \(X\) itself is in \(\mathcal B^-(T)\). Since \(X\) and \(X^c\) are positive, every \(X\in\mathcal C(T)\) has a local basis below it, equal to it, or above it.

*Step 2 (endpoints in the class, rule \(-\)).* If \(I,Y\in\mathcal C(T)\): when \(\ell(I)>0\), Step 1 gives a basis below \(I\); when \(\ell(Y)\le-1\), a basis above \(Y\); when \(I\) or \(Y\) is a local basis, it is an outcome; otherwise \(\ell(I)\le-1<0<\ell(Y)\) and Lemma 2.2 applies. If \(I\in\mathcal C(T)\) and \(Y\setminus I\) is positive, Step 1 with \(G=Y\setminus I\) gives a basis below \(I\), equal to \(I\), or between \(I\) and \(Y\). If \(Y\in\mathcal C(T)\) and \(Y\setminus I\) is positive, Step 1 with \(G=Y\setminus I\) gives a basis between \(I\) and \(Y\), equal to \(Y\), or above \(Y\).

*Step 3 (rule \(+\)).* By Lemma 1.1(4), \(B\in\mathcal B^+(T)\) exactly when \(B^c\in\mathcal B^-(T^c)\), and \(X\in\mathcal C(T)\) exactly when \(X^c\in\mathcal C(T^c)\). Applying Step 2 to \(T^c\) and the interval \(Y^c\subseteq I^c\), with the same gap \(Y\setminus I\), and complementing gives the conclusions of Step 2 for the rule \(+\), the outcomes "below" and "above" being exchanged.

*Step 4 (the hypotheses).* Let \(T\setminus I\in\mathcal J_0\). If \(I\in\mathcal C(T)\), then either \(Y\setminus I\in\mathcal J_0\), so \(Y\in\mathcal C(T)\), or the gap is positive; Steps 2–3 apply. If \(I\notin\mathcal C(T)\), then \(I\setminus T\) is positive and \(T\cap I\in\mathcal C(T)\); Steps 2–3 for the interval \(T\cap I\subseteq I\) give a basis contained in \(I\). Finally let \(Y\setminus T\in\mathcal J_0\). Then \(T^c\setminus Y^c=Y\setminus T\in\mathcal J_0\), and the case just proved, for the prototype \(T^c\), the interval \(Y^c\subseteq I^c\) and the rule opposite to \(\sigma\), gives a local basis whose complement lies in \(\mathcal B^\sigma(T)\) and satisfies (2.4). \(\square\)

## 3. Exercises

**3.1.** Let \(F\subseteq T^c\) be finite. Show that \(\ell(T\cup F)=h(T\cup F)=|F|\), so \(T\cup F\in\mathcal B^-(T)\) only for \(F=\varnothing\).

**3.2.** Show that \(\mathcal B^-(T)\) is infinite and that its members are infinite with infinite complements.

**3.3.** Show that the family \(\{X\in\mathcal C(T):\ell(X)\le0\}\) is not an antichain. Which part of Lemma 1.3 uses the strict bound \(-1<\ell(X)\)?

**3.4.** In Lemma 2.2, why can \(M_j\) not simply be chosen equal to \(j\)?

## 4. Solutions

**3.1.** All probes of \(T\) vanish, and Lemma 1.1(3) with \(b=|F|\) gives \(f_n(T\cup F)=|F|\) for large \(n\).

**3.2.** Members of \(\mathcal C(T)\) and their complements are \(\mathcal J_0\)-positive, hence infinite. For \(a\in T\) and \(b\notin T\), \((T\setminus\{a\})\cup\{b\}\in\mathcal B^-(T)\) by Lemma 1.3, and these sets are distinct for distinct pairs.

**3.3.** For \(a\in T\), \(\ell(T\setminus\{a\})=-1\le0=\ell(T)\), and \(T\setminus\{a\}\subsetneq T\). The finite-difference case of the antichain argument needs \(\ell(Y)=\ell(X)+k>0\) to be impossible, which uses \(\ell(X)>-1\).

**3.4.** The deletions at stage \(j\) must lower the probes \(f_n\), \(n<j\), by a summable amount. Deleting in blocks \(m\ge M_j\) changes those probes only through tail densities, and (2.2) makes the change smaller than \(2^{-j}\); deletions in early blocks would change the prefix counts \(p_n\) by whole units.

## References

- [OpenAI-IM] OpenAI, *A counterexample to the infinite matroid packing/covering conjecture*, OpenAI Math Release preprint, 24 September 2026. https://github.com/openai/math/blob/main/preprints/A-Counterexample-to-the-Infinite-Matroid-Packing-Covering-Conjecture-September-24-2026/paper.pdf
- [BG] N. Bowler and S. Geschke, *Self-dual uniform matroids on infinite sets*, Proceedings of the AMS 144 (2016); author version on the author's page. https://www.math.uni-hamburg.de/home/geschke/papers/UniformMatroid7.pdf
