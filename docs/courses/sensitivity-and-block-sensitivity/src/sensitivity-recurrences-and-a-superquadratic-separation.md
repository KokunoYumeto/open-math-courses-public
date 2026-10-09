# Sensitivity recurrences and a superquadratic separation

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson proves OpenAI's theorem that block sensitivity is not bounded by a constant multiple of the square of sensitivity [OpenAI-S, Sections 3 and 4]:

**Theorem 3.1** (OpenAI). For every real \(C>0\) there are \(n\ge1\) and a nonconstant Boolean function \(f:\{0,1\}^n\to\{0,1\}\) with \(\operatorname{bs}(f)>C\,s(f)^2\). More precisely, for every integer \(d\ge1\) there is a nonconstant Boolean function \(f\) with
\[
\frac{\operatorname{bs}(f)}{s(f)^2}\ge\frac{2^d}{4(d+2)^2}.
\]

The functions are disjoint ORs of the predicates of [Nested predicates on a labelled tournament](nested-predicates-on-a-labelled-tournament.md). There, the number of disjoint sensitive blocks at zero is multiplied by \(k=2M^2+1\) at each level. Here we show that the square of sensitivity grows only by a factor of about \(M^2\) per level: up to small errors, the profile \(S_{\ell,1}\) is \(M^2\) times \(S_{\ell-1,0}\) and \(S_{\ell,0}\) is \(S_{\ell-1,1}\), so both profiles grow by a factor of about \(M\) per level (Proposition 1.1 and Lemma 2.1). Over \(d\) levels the ratio of block sensitivity to squared sensitivity gains about \((k/M^2)^d\ge2^d\). The proof (Proposition 1.1) looks at a rejecting input and the clauses that one flip can make true. A clause that fails exactly one target can be repaired only in a position fixed by the labels, and the labels allow fewer than \(16\) such clauses. A clause that fails exactly one gate lies in a row whose targets all hold, and the tournament allows at most three such clauses; repairing any of them but at most one must change two predicates of the same child at once. So the recurrences also track such simultaneous changes, the *joint* profiles, which vanish at level zero and stay small.

We use from [Nested predicates on a labelled tournament](nested-predicates-on-a-labelled-tournament.md) the parameters \(L,k,r,t,H_\ell,N_\ell\) of its Sections 1–2, Lemma 1.1, the clauses and Lemma 3.1, Lemma 4.1, the profiles \(S_{\ell,b},J_{\ell,b}\) and Lemma 5.1; and from [Sensitivity, block sensitivity and composition](sensitivity-block-sensitivity-and-composition.md) Lemma 2.1 and Proposition 4.2.

## 1. The recurrences

**Proposition 1.1** (sensitivity recurrences). For \(1\le\ell\le d\), write \(S'_b=S_{\ell-1,b}\) and \(J'_b=J_{\ell-1,b}\). Then
\[
\begin{aligned}
S_{\ell,1}&\le M^2S'_0+rS'_1, &\qquad J_{\ell,1}&\le M^2J'_0+rS'_1,\\
S_{\ell,0}&\le tS'_0+S'_1+3J'_1, &\qquad J_{\ell,0}&\le tS'_0+3J'_1.
\end{aligned}\tag{1.1}
\]

**Proof.** Let \(H=H_\ell\) and \(Q=H+1\). A *flip* is a flip of one coordinate of the input; it changes only the predicates of the child containing that coordinate, possibly several of them. By Lemma 3.1(a) of [Nested predicates on a labelled tournament](nested-predicates-on-a-labelled-tournament.md), it changes at most one condition of any fixed clause. The predicates of level \(\ell-1\) are nested, so for indices \(g'<g\) and any child \(y\): \(P_{\ell-1,g}(y)=1\) implies \(P_{\ell-1,g'}(y)=1\), and \(P_{\ell-1,g'}(y)=0\) implies \(P_{\ell-1,g}(y)=0\).

*The bound for \(S_{\ell,1}\).* Let \(P_{\ell,q}(x)=1\) and fix a clause \(C_{i,q}\) that holds at \(x\). A flip that makes \(P_{\ell,q}\) reject makes \(C_{i,q}\) fail, so it breaks one of its conditions: it turns \(P_{\ell-1,Q}\) off at one of the \(r\) target children, at most \(S'_1\) flips each, or it turns \(P_{\ell-1,Q-q}\) on at one of the \(M^2\) gate children, at most \(S'_0\) flips each.

*The bound for \(J_{\ell,1}\).* Let \(q<q'\), let \(P_{\ell,q}(x)=P_{\ell,q'}(x)=1\), and fix a clause \(C_{i,q'}\) that holds at \(x\); then \(C_{i,q}\) holds at \(x\) too (Lemma 3.1(b) there). A flip that makes both parent predicates reject makes \(C_{i,q}\) fail. Either it breaks a target, at most \(rS'_1\) flips in all, or it breaks a gate of \(C_{i,q}\) at a child \(y\). Put \(g=Q-q\) and \(g'=Q-q'\), so \(1\le g'<g\le H\). Since \(C_{i,q'}\) holds at \(x\), \(P_{\ell-1,g'}(y)=0\), hence \(P_{\ell-1,g}(y)=0\); after the flip the gate of \(C_{i,q}\) fails, so \(P_{\ell-1,g}=1\), hence \(P_{\ell-1,g'}=1\) at the flipped child. So both predicates \(g'<g\) of the child change from \(0\) to \(1\): at most \(J'_0\) flips for each of the \(M^2\) gate children.

*Candidate clauses at a rejecting input.* Fix \(q\) and \(x\) with \(P_{\ell,q}(x)=0\). Let \(\mathcal T\) be the set of rows \(i\) for which \(C_{i,q}\) fails exactly one target and no gate at \(x\), and \(\mathcal G\) the set of rows for which \(C_{i,q}\) fails exactly one gate and no target. Both sets depend only on \(x\) and \(q\).

(A) *If a flip makes \(C_{i,q}\) hold, then \(i\in\mathcal T\cup\mathcal G\) and the flip repairs the unique failing condition of \(C_{i,q}\) at \(x\).* Indeed, \(C_{i,q}\) fails at \(x\), and a flip changes at most one of its conditions.

(B) *\(|\mathcal T|<t\).* For \(j\in\mathcal T\) let \(m_j\in[r]\) be the position of the failing target of \(C_{j,q}\). Let \(i,j\in\mathcal T\) with \(i\to j\). The gate of \(C_{i,q}\) at the child \((j,a(i,j))\) holds, so \(P_{\ell-1,Q-q}\) rejects there, and therefore \(P_{\ell-1,Q}\) rejects there as \(Q-q<Q\). That is a failing target of \(C_{j,q}\), so \(a(i,j)=m_j\). If \(|\mathcal T|\ge t\), any \(t\) elements of \(\mathcal T\) with these \(m_j\) would contradict Lemma 1.1 there.

(C) *\(|\mathcal G|\le3\); each \(i\in\mathcal G\) has at most one out-neighbour in \(\mathcal G\), and at most one \(i\in\mathcal G\) has none.* For \(j\in\mathcal G\) all targets of \(C_{j,q}\) hold, so \(P_{\ell-1,Q}\) accepts at every child of row \(j\), and therefore so does \(P_{\ell-1,Q-q}\). Hence if \(i,j\in\mathcal G\) and \(i\to j\), the gate of \(C_{i,q}\) at \((j,a(i,j))\) fails; as \(C_{i,q}\) has one failing gate, \(i\) has at most one out-neighbour in \(\mathcal G\), and that gate is its failing gate. The tournament restricted to \(\mathcal G\) has \(\binom m2\) edges, \(m=|\mathcal G|\), each leaving one vertex; so \(\binom m2\le m\) and \(m\le3\). Two vertices without out-neighbours in \(\mathcal G\) would be joined by an edge leaving one of them.

*The bound for \(S_{\ell,0}\).* By (A), every flip that makes \(P_{\ell,q}\) accept repairs the unique failing condition of a clause \(C_{i,q}\) with \(i\in\mathcal T\cup\mathcal G\). For \(i\in\mathcal T\), it turns \(P_{\ell-1,Q}\) on at the child \((i,m_i)\): at most \(S'_0\) flips, and fewer than \(t\) rows by (B). For \(i\in\mathcal G\) with an out-neighbour \(j\in\mathcal G\), the failing gate is at the child \(y=(j,a(i,j))\), where both \(P_{\ell-1,Q-q}\) and \(P_{\ell-1,Q}\) accept by (C); the repair makes \(P_{\ell-1,Q-q}\) reject, and then \(P_{\ell-1,Q}\) rejects too. The indices \(Q-q<Q\) are distinct, so this is a simultaneous change from \(1\) to \(0\): at most \(J'_1\) flips, for at most three rows. For the possible row \(i\in\mathcal G\) without an out-neighbour in \(\mathcal G\), the repair turns \(P_{\ell-1,Q-q}\) off at the failing gate child: at most \(S'_1\) flips. Altogether at most \(tS'_0+S'_1+3J'_1\) flips.

*The bound for \(J_{\ell,0}\).* Let \(q<q'\), let \(P_{\ell,q}(x)=P_{\ell,q'}(x)=0\), and form \(\mathcal T,\mathcal G\) for \(x\) and the index \(q\). Let a flip make both parent predicates accept, and choose a clause \(C_{i,q'}\) that holds after the flip; then \(C_{i,q}\) holds after the flip too. By (A), \(i\in\mathcal T\cup\mathcal G\). If \(i\in\mathcal T\), the flip turns \(P_{\ell-1,Q}\) on at the child \((i,m_i)\), as counted above: at most \(tS'_0\) flips in all. If \(i\in\mathcal G\), let \(y\) be the child of the failing gate of \(C_{i,q}\), and \(g=Q-q\), \(g'=Q-q'\), so \(1\le g'<g\le H\). At \(x\), \(P_{\ell-1,g}(y)=1\), hence \(P_{\ell-1,g'}(y)=1\). After the flip, \(C_{i,q'}\) holds, so its gate at \(y\) holds: \(P_{\ell-1,g'}=0\), hence \(P_{\ell-1,g}=0\) at the flipped child. Both change from \(1\) to \(0\): at most \(J'_1\) flips for each of the at most three rows of \(\mathcal G\). The lists \(\mathcal T\) and \(\mathcal G\) do not depend on the flip, so altogether at most \(tS'_0+3J'_1\) flips.

Taking maxima over \(q\), \(q<q'\) and \(x\) gives (1.1); if \(H=1\) the joint profiles of level \(\ell\) are \(0\) by convention. \(\square\)

## 2. Growth of the profiles

**Lemma 2.1** (profiles). If \(M\ge9^{d+1}\), then \(S_{\ell,b}\le2LM^{\ell+b}\) for \(0\le\ell\le d\) and \(b\in\{0,1\}\).

**Proof.** Put
\[
u_\ell=\max_{b\in\{0,1\}}\frac{S_{\ell,b}}{M^{\ell+b}},\qquad v_\ell=\max_{b\in\{0,1\}}\frac{J_{\ell,b}}{M^{\ell+b}},\qquad\varepsilon=\frac{\max\{r,t\}}M.
\]
Lemma 5.1 of [Nested predicates on a labelled tournament](nested-predicates-on-a-labelled-tournament.md) gives \(u_0\le L\) and \(v_0=0\). Dividing the four inequalities (1.1) by \(M^{\ell+1}\), \(M^{\ell+1}\), \(M^\ell\) and \(M^\ell\), and using \(S'_b\le u_{\ell-1}M^{\ell-1+b}\) and \(J'_b\le v_{\ell-1}M^{\ell-1+b}\),
\[
u_\ell\le(1+\varepsilon)u_{\ell-1}+3v_{\ell-1},\qquad v_\ell\le\varepsilon u_{\ell-1}+3v_{\ell-1}.\tag{2.1}
\]
Since \(\sqrt M\ge3^{d+1}\ge9\), \(r\le\sqrt M+1\le2\sqrt M\) and \(t=16\le2\sqrt M\), so
\[
\varepsilon\le\frac2{\sqrt M}\le\frac2{3^{d+1}}.\tag{2.2}
\]
Let \(U_0=L\), \(V_0=0\), \(U_\ell=(1+\varepsilon)U_{\ell-1}+3V_{\ell-1}\) and \(V_\ell=\varepsilon U_{\ell-1}+3V_{\ell-1}\). The coefficients are nonnegative, so (2.1) gives \(u_\ell\le U_\ell\) and \(v_\ell\le V_\ell\) by induction. We show by induction that \(U_\ell\le2L\) and \(V_\ell\le\varepsilon L(3^\ell-1)\) for \(0\le\ell\le d\). Both hold for \(\ell=0\). If they hold below \(\ell\), then \(V_\ell\le2\varepsilon L+3\varepsilon L(3^{\ell-1}-1)=\varepsilon L(3^\ell-1)\), and
\[
U_\ell=L+\sum_{j=0}^{\ell-1}(\varepsilon U_j+3V_j)\le L+2\varepsilon L\ell+3\varepsilon L\sum_{j=0}^{\ell-1}(3^j-1)=L+\varepsilon L\Bigl(\tfrac32(3^\ell-1)-\ell\Bigr).
\]
By (2.2) and \(\ell\le d\), \(\varepsilon\bigl(\frac32(3^\ell-1)-\ell\bigr)\le\frac{3^{\ell+1}-3-2\ell}{3^{d+1}}<1\), so \(U_\ell<2L\). Hence \(u_\ell\le2L\), which is the claim. \(\square\)

## 3. The separation

**Proof of Theorem 3.1.** Let \(d\ge1\), choose an integer \(M\ge9^{d+1}\), and fix labels by Lemma 1.1 of [Nested predicates on a labelled tournament](nested-predicates-on-a-labelled-tournament.md). Let \(f\) be the disjoint OR of \(M\) copies of \(P_{d,1}\), a function on \(n=MN_d=LM^2(kr)^d\) bits. By Lemma 4.1 there, \(P_{d,1}(0)=0\) and \(\operatorname{bs}(P_{d,1},0)\ge Mk^d\). By Lemma 2.1 of [Sensitivity, block sensitivity and composition](sensitivity-block-sensitivity-and-composition.md) and Lemma 2.1 above (with \(H_d=1\), so \(s_b(P_{d,1})=S_{d,b}\)),
\[
s(f)\le\max\{M\,S_{d,0},\,S_{d,1}\}\le2LM^{d+1},\qquad\operatorname{bs}(f)\ge\operatorname{bs}(f,0)\ge M^2k^d.\tag{3.1}
\]
In particular \(f(0)=0\) and \(f\) has a sensitive block, so \(f\) is nonconstant and \(s(f)\ge1\). Since \(k/M^2>2\) and \(L=d+2\),
\[
\frac{\operatorname{bs}(f)}{s(f)^2}\ge\frac{M^2k^d}{4L^2M^{2d+2}}=\frac{(k/M^2)^d}{4L^2}\ge\frac{2^d}{4(d+2)^2}.
\]
Given \(C>0\), choose \(d\) with \(2^d>4(d+2)^2C\). \(\square\)

The OR of \(M\) copies balances the two sides: \(P_{d,1}\) alone has \(s_1\) of order \(M^{d+1}\) but \(s_0\) only of order \(M^d\), and the OR multiplies \(s_0\) and the block count by \(M\) while keeping \(s_1\) (Exercise 4.3).

**Corollary 3.2** (a power separation). There are a real number \(\alpha>2\) and nonconstant Boolean functions \(F_m\), \(m\ge1\), with \(F_m(0)=0\), \(\operatorname{bs}(F_m,0)\ge s(F_m)^\alpha\) and \(\operatorname{bs}(F_m,0)\to\infty\).

**Proof.** Take \(d=9\), so \(L=11\), an integer \(M\ge9^{10}\), and the function \(f\) of the proof above. By (3.1), \(s(f)\le A=22M^{10}\) and \(\operatorname{bs}(f,0)\ge B=M^2k^9\), and
\[
\frac B{A^2}=\frac{(k/M^2)^9}{484}>\frac{2^9}{484}=\frac{128}{121}>1.
\]
Since \(A>1\), Proposition 4.2 of [Sensitivity, block sensitivity and composition](sensitivity-block-sensitivity-and-composition.md) applies to \(f\), with \(\alpha=\log B/\log A>2\), and gives nonconstant \(F_m\) with \(F_m(0)=0\), \(\operatorname{bs}(F_m,0)\ge B^m\ge s(F_m)^\alpha\) and \(\operatorname{bs}(F_m)/s(F_m)^2\ge(128/121)^m\); and \(B^m\to\infty\). \(\square\)

**Remarks.** (1) The exponent obtained this way is only slightly larger than \(2\): for \(M=9^{10}\), \(\alpha\approx2.00025\). By Huang's theorem, every exponent of this kind is at most \(4\) [Huang].

(2) The *sensitivity graph* of \(f\) joins inputs differing in one coordinate on which \(f\) differs; its largest degree is \(s(f)\), and its *spectral sensitivity* \(\lambda(f)\) is the largest absolute value of an eigenvalue of its adjacency matrix [ABKRT]. Since \(\lambda(f)\le s(f)\), Meiburg's examples with \(\operatorname{bs}(f)>\lambda(f)^2\) [Meiburg] do not give Theorem 3.1, whose estimates bound ordinary sensitivity directly.

## 4. Exercises

**Exercise 4.1** (easy). Derive the normalized inequalities (2.1) from (1.1).

**Exercise 4.2** (easy). Show that a tournament on \(m\) vertices in which every vertex has at most one out-neighbour has \(m\le3\), and that for \(m=3\) it is a directed triangle.

**Exercise 4.3** (medium). Bound \(s(P_{d,1})\) and \(\operatorname{bs}(P_{d,1},0)\) with Lemma 2.1 above and Lemma 4.1 of [Nested predicates on a labelled tournament](nested-predicates-on-a-labelled-tournament.md), and show that these bounds alone give only \(\operatorname{bs}(P_{d,1})/s(P_{d,1})^2\ge(k/M^2)^d/(4L^2M)\).

**Exercise 4.4** (medium). In the bound for \(S_{\ell,0}\), show that the contribution of \(\mathcal G\) is in fact at most \(\max\{3J'_1,\,J'_1+S'_1\}\).

## 5. Solutions

**4.1.** For instance \(S_{\ell,1}/M^{\ell+1}\le S'_0/M^{\ell-1}+\frac rM\,S'_1/M^\ell\le(1+\frac rM)u_{\ell-1}\), and \(S_{\ell,0}/M^\ell\le\frac tM\,S'_0/M^{\ell-1}+S'_1/M^\ell+3J'_1/M^\ell\le(1+\frac tM)u_{\ell-1}+3v_{\ell-1}\); similarly \(J_{\ell,1}/M^{\ell+1}\le v_{\ell-1}+\frac rMu_{\ell-1}\) and \(J_{\ell,0}/M^\ell\le\frac tMu_{\ell-1}+3v_{\ell-1}\). Take maxima and use \(r,t\le\varepsilon M\).

**4.2.** The \(\binom m2\) edges each leave one vertex, so \(\binom m2\le m\), that is \(m\le3\). For \(m=3\), the three edges leave three different vertices, so every vertex has exactly one out-neighbour, which forces a directed triangle.

**4.3.** \(s(P_{d,1})\le\max\{S_{d,0},S_{d,1}\}\le2LM^{d+1}\) and \(\operatorname{bs}(P_{d,1},0)\ge Mk^d\), so the ratio is at least \(Mk^d/(4L^2M^{2d+2})=(k/M^2)^d/(4L^2M)\), which tends to \(0\) as \(M\to\infty\). In the disjoint OR of \(M\) copies the block count gains the factor \(M\), \(s_1\) is unchanged, and \(s_0\) is multiplied by at most \(M\); since \(S_{d,0}\le2LM^d\), both sides stay below \(2LM^{d+1}\), and the ratio gains the factor \(M\).

**4.4.** By Exercise 4.2, if \(|\mathcal G|=3\) the three rows form a directed triangle, each with an out-neighbour: at most \(3J'_1\). If \(|\mathcal G|=2\), one row has an out-neighbour and one has none: at most \(J'_1+S'_1\). If \(|\mathcal G|\le1\): at most \(S'_1\).

## References

- [ABKRT] S. Aaronson, S. Ben-David, R. Kothari, S. Rao and A. Tal, *Degree vs. approximate degree and quantum implications of Huang's sensitivity theorem*, STOC 2021; arXiv:2010.12629. https://arxiv.org/abs/2010.12629
- [Huang] H. Huang, *Induced subgraphs of hypercubes and a proof of the Sensitivity Conjecture*, Ann. of Math. 190 (2019); arXiv:1907.00847. https://arxiv.org/abs/1907.00847
- [Meiburg] A. Meiburg, *Block sensitivity can exceed spectral sensitivity squared*, arXiv:2608.00851 (2026). https://arxiv.org/abs/2608.00851
- [OpenAI-S] OpenAI, *A superquadratic separation between sensitivity and block sensitivity*, OpenAI Math Release preprint, 25 September 2026, Sections 3 and 4. https://github.com/openai/math/tree/main/preprints/A-superquadratic-separation-between-sensitivity-and-block-sensitivity-September-25-2026
