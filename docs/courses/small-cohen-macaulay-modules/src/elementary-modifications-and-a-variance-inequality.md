# Elementary modifications and a variance inequality

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

A small Cohen–Macaulay module over a completed cone gives, by [Completed cones over surfaces](completed-cones-over-surfaces.md), a torsion-free sheaf \(P\) on the exceptional surface \(X\), and a sheaf \(f_*P\) on the plane that is the restriction of a sheaf trivial away from the plane. This lesson proves two facts about this situation.

- The sheaf on the regular model can be modified along \(X\), without changing it elsewhere, so that the slopes of the Harder–Narasimhan factors of its restriction lie in an interval of length at most one (Proposition 3.2).
- Every sheaf on the plane that arises as the restriction of a sheaf trivial away from the plane satisfies \(2N\operatorname{ch}_2\ge c_1^2\), where \(N\) is its rank (Proposition 4.2).

Both are proved in full. They use the first Chern class of coherent sheaves on a surface, which is introduced through a named hypothesis in Section 1; on the plane, the Chern classes are defined through Hilbert polynomials and everything is proved.

The lesson follows [OpenAI-SCM, Sections 3 and 4].

## 1. Chern classes on a surface and on the plane

Let \(X\) be a smooth integral projective surface over \(\mathbb C\). Divisor classes are elements of the Picard group \(\operatorname{Pic}X\), written additively, and \(D\cdot E\) is the intersection pairing of the lesson [Cycle classes and the Lefschetz fixed point formula for curves](course:AG-LTF/cycle-classes-and-the-lefschetz-fixed-point-formula-for-curves) (course *ℓ-adic cohomology and trace formulas*), formula (HI.1). The *rank* \(\operatorname{rk}F\) of a coherent sheaf \(F\) is its dimension at the generic point.

**Hypothesis (CS)** (Chern classes of coherent sheaves on a smooth projective surface). To every coherent sheaf \(F\) on \(X\) are attached a class \(c_1(F)\in\operatorname{Pic}X\) and a rational number \(\operatorname{ch}_2(F)\), with the following four properties.

(1) \(\operatorname{rk}\), \(c_1\) and \(\operatorname{ch}_2\) are additive in short exact sequences.

(2) For a line bundle \(L\), \(c_1(L)=L\) and \(\operatorname{ch}_2(L)=\tfrac12L^2\). For every \(F\) of rank \(r\) and every line bundle \(L\), \(c_1(F\otimes L)=c_1(F)+rL\) and
\[
\begin{aligned}
\operatorname{ch}_2(F\otimes L)&=\operatorname{ch}_2(F)+c_1(F)\cdot L\\
&\quad+\tfrac r2L^2 .
\end{aligned}
\]

(3) If \(\operatorname{rk}F=0\), then \(c_1(F)\cdot H\ge0\) for every ample \(H\).

(4) (Hirzebruch–Riemann–Roch) For every \(F\) of rank \(r\),
\[
\begin{aligned}
\chi(X,F)&=r\chi(\mathcal O_X)+\operatorname{ch}_2(F)\\
&\quad-\tfrac12c_1(F)\cdot K_X .
\end{aligned}
\]

These are the first Chern class and the degree-two part of the Chern character, constructed with finite locally free resolutions; \(c_2(F)=\tfrac12c_1(F)^2-\operatorname{ch}_2(F)\). The statements are standard (for the Riemann–Roch formula see [Reid, Chapter B, item ix]). They are not proved in the programme. This lesson uses parts 1 to 3 on the surface \(X\); part 4 is used in [The numerical obstruction](the-numerical-obstruction.md).

**On the plane everything is proved.** Let \(D=\mathbb P^2\) and \(\ell\) the class of a line. For a coherent sheaf \(F\) on \(D\), \(t\mapsto\chi(F(t))\) is a polynomial of degree at most two (Theorem 2.1 of [Euler characteristics and Hilbert polynomials](course:AG-QC/euler-characteristics-and-hilbert-polynomials)). Define the numbers \(\operatorname{rk}F\), \(c_1(F)\) and \(\operatorname{ch}_2(F)\) by
\[
\begin{aligned}
\chi(F(t))&=\operatorname{rk}F\binom{t+2}2\\
&\quad+c_1(F)\bigl(t+\tfrac32\bigr)+\operatorname{ch}_2(F) .
\end{aligned}
\]
We identify \(c_1(F)\) with the class \(c_1(F)\,\ell\).

**Lemma 1.1.** On \(D=\mathbb P^2\):

1. \(\operatorname{rk}\), \(c_1\) and \(\operatorname{ch}_2\) are additive in short exact sequences, and \(\operatorname{rk}F\) is the rank of \(F\) at the generic point;
2. \(c_1(\mathcal O(a))=a\) and \(\operatorname{ch}_2(\mathcal O(a))=\tfrac12a^2\); for \(F\) of rank \(r\), \(c_1(F(1))=c_1(F)+r\) and \(\operatorname{ch}_2(F(1))=\operatorname{ch}_2(F)+c_1(F)+\tfrac r2\);
3. if \(\operatorname{rk}F=0\), then \(c_1(F)\ge0\);
4. if \(F\) is globally generated, then \(c_1(F)\ge0\).

**Proof.** *Part 1.* Euler characteristics are additive (Proposition 1.1 of the lesson on Euler characteristics), and the three polynomials \(\binom{t+2}2\), \(t+\tfrac32\), \(1\) are linearly independent. The coefficient of \(t^2\) is \(\tfrac12\operatorname{rk}F\), and it was shown in the proof of Lemma 2.1 of [Completed cones over surfaces](completed-cones-over-surfaces.md) that this coefficient is half the generic rank.

*Part 2.* \(\chi(\mathcal O(a+t))=\binom{a+t+2}2\) (cohomology of projective space, Theorem 2.2 of [Cohomology of projective space](course:AG-QC/cohomology-of-projective-space)), which equals \(\binom{t+2}2+a(t+\tfrac32)+\tfrac12a^2\). For the twist, \(\chi(F(1)(t))=\chi(F(t+1))\), and \(\binom{t+3}2=\binom{t+2}2+(t+\tfrac32)+\tfrac12\), \((t+1)+\tfrac32=(t+\tfrac32)+1\).

*Part 3.* If \(\operatorname{rk}F=0\), then \(\chi(F(t))=c_1(F)t+\text{const}\). For large \(t\) this is \(h^0(F(t))\ge0\) (Theorem 2.1 of [Serre's theorems on projective schemes](course:AG-QC/serres-theorems-on-projective-schemes)), so \(c_1(F)\ge0\).

*Part 4.* Let \(n=\operatorname{rk}F\). Since \(F\) is globally generated, \(n\) global sections are linearly independent at the generic point; they define \(\mathcal O^n\to F\), injective because its kernel is a subsheaf of \(\mathcal O^n\) vanishing at the generic point, with a cokernel \(T\) of rank zero. By additivity \(c_1(F)=c_1(\mathcal O^n)+c_1(T)=c_1(T)\ge0\) by part 3. \(\blacksquare\)

With this definition, Riemann–Roch on the plane holds by construction, and by part 2 the numbers agree with the usual ones for sums of line bundles.

## 2. Slopes and the Harder–Narasimhan filtration

Fix \(X\) as in Section 1 and an ample divisor \(H\) on \(X\), with \(h=H^2>0\). For a coherent sheaf \(B\) of positive rank, its *normalized slope* is
\[
\mu(B)=\frac{c_1(B)\cdot H}{(\operatorname{rk}B)\,h} .
\]
By (CS), \(\mu(B\otimes\mathcal O_X(H))=\mu(B)+1\), and in a short exact sequence of sheaves of positive rank the slope of the middle term is the average of the outer slopes weighted by the ranks. A torsion-free sheaf \(G\ne0\) is *semistable* if \(\mu(B)\le\mu(G)\) for every nonzero subsheaf \(B\subseteq G\).

**Lemma 2.1.** Let \(P\) be a torsion-free sheaf of positive rank \(r\) on \(X\).

1. There are \(m,k\) with \(P\subseteq\mathcal O_X(mH)^{\oplus k}\), and every nonzero subsheaf of \(\mathcal O_X(mH)^{\oplus k}\) has slope at most \(m\).
2. The slopes of the nonzero subsheaves of \(P\) lie in \(\tfrac1{r!\,h}\mathbb Z\) and are bounded above; let \(\mu_{\max}(P)\) be their maximum.
3. If \(0\to P_1\to P\to P_2\to0\) is exact with \(P_1,P_2\) torsion-free (possibly zero), then \(\mu_{\max}(P)\) is at most the larger of \(\mu_{\max}(P_1)\) and \(\mu_{\max}(P_2)\), taken over the nonzero ones.

**Proof.** *Part 1.* For large \(m\), the sheaf \(P^\vee(mH)\) is globally generated (Theorem 2.2 of the lesson on Serre's theorems), say by \(k\) sections; dualizing \(\mathcal O^k\to P^\vee(mH)\) gives \(P^{\vee\vee}(-mH)\subseteq\mathcal O^k\). A torsion-free sheaf injects into its double dual, so \(P\subseteq\mathcal O_X(mH)^{\oplus k}\). For the bound, induct on \(k\). Let \(B\subseteq\mathcal O(mH)^{\oplus k}\) be nonzero, \(B'\) its intersection with the first \(k-1\) summands and \(B''\) its image in the last summand. If \(B''\ne0\), it is a subsheaf of rank one of \(\mathcal O(mH)\), the quotient has rank zero, and by (CS) parts 1 and 3, \(c_1(B'')\cdot H\le mh\). By additivity and induction, \(c_1(B)\cdot H\le(\operatorname{rk}B)\,mh\).

*Part 2.* A subsheaf \(B\) has rank between \(1\) and \(r\), and \(c_1(B)\cdot H\) is an integer, so \(\mu(B)\in\frac1{\operatorname{rk}B\,h}\mathbb Z\subseteq\frac1{r!\,h}\mathbb Z\). The bound is part 1.

*Part 3.* Let \(B\subseteq P\) be nonzero, \(B_1=B\cap P_1\) and \(B_2\) its image in \(P_2\). Then \(\mu(B)\) is the rank-weighted average of the slopes of those of \(B_1,B_2\) that have positive rank; a nonzero subsheaf of a torsion-free sheaf has positive rank. \(\blacksquare\)

**Proposition 2.2** (Harder–Narasimhan filtration). Every torsion-free sheaf \(P\) of positive rank on \(X\) has a filtration
\[
0=P_0\subsetneq P_1\subsetneq\dots\subsetneq P_k=P
\]
whose factors \(G_i=P_i/P_{i-1}\) are torsion-free and semistable, with \(\mu(G_1)>\mu(G_2)>\dots>\mu(G_k)\). Moreover \(\mu(G_1)=\mu_{\max}(P)\).

**Proof.** Induction on the rank. Among the subsheaves of slope \(\mu_{\max}(P)\), choose \(P_1\) of maximal rank. Its *saturation*, the preimage of the torsion of \(P/P_1\), has the same rank and contains \(P_1\) with a quotient of rank zero; by (CS) parts 1 and 3 its slope is at least \(\mu_{\max}(P)\), hence equal. So we may assume \(P/P_1\) torsion-free. \(P_1\) is semistable, since its subsheaves are subsheaves of \(P\). If a nonzero subsheaf \(C\subseteq P/P_1\) had \(\mu(C)\ge\mu_{\max}(P)\), its preimage in \(P\) would have slope at least \(\mu_{\max}(P)\), hence equal, and rank larger than that of \(P_1\), contrary to the choice. So \(\mu_{\max}(P/P_1)<\mu(P_1)\). If \(P_1\ne P\), apply the induction hypothesis to \(P/P_1\) and pull its filtration back. The first factor of the filtration of \(P/P_1\) has slope \(\mu_{\max}(P/P_1)<\mu(G_1)\). \(\blacksquare\)

We write \(\mu_{\min}(P)=\mu(G_k)\). The *slope width* of \(P\) is \(\mu_{\max}(P)-\mu_{\min}(P)\).

## 3. Elementary modifications

**Lemma 3.1.** Let \(W\) be an integral Noetherian scheme and \(i\colon X\to W\) an effective Cartier divisor with ideal \(\mathcal J\). Let \(\mathcal E\) be a coherent sheaf on \(W\) on which the local equations of \(X\) are nonzerodivisors, \(P=\mathcal E|_X\), and \(P\to G\) a surjection of \(\mathcal O_X\)-modules with kernel \(B\). Put
\[
\mathcal E'=\ker\bigl(\mathcal E\to P\to i_*G\bigr) .
\]
Then \(\mathcal E'\) agrees with \(\mathcal E\) off \(X\), the local equations of \(X\) are nonzerodivisors on \(\mathcal E'\), and there is an exact sequence
\[
0\to G\otimes\mathcal J|_X\to\mathcal E'|_X\to B\to0 .
\]

**Proof.** Locally \(X\) is cut out by one nonzerodivisor \(u\), and \(\operatorname{Tor}_1^{\mathcal O_W}(F,\mathcal O_X)\) is the kernel of multiplication by \(u\) from \(F\otimes\mathcal J\) to \(F\). It vanishes for \(F=\mathcal E\) by assumption, and for \(F=i_*G\), on which \(u\) acts by zero, it is \(G\otimes\mathcal J|_X\). The long exact Tor sequence of \(0\to\mathcal E'\to\mathcal E\to i_*G\to0\) restricted to \(X\) reads
\[
0\to G\otimes\mathcal J|_X\to\mathcal E'|_X\to P\to G\to0 ,
\]
which gives the claim. \(\mathcal E'\) is a subsheaf of \(\mathcal E\), so \(u\) stays injective on it. \(\blacksquare\)

**Proposition 3.2** (balancing; [OpenAI-SCM, Lemma 3.1]). Let \(W\) be an integral Noetherian scheme and \(X\subset W\) an effective Cartier divisor that is a smooth integral projective surface over \(\mathbb C\), with \(\mathcal J|_X\cong\mathcal O_X(H)\) for an ample \(H\). Let \(\mathcal E\) be a coherent torsion-free sheaf on \(W\) such that \(P=\mathcal E|_X\) is torsion-free of positive rank \(r\). Then there is a coherent torsion-free sheaf \(\mathcal E'\subseteq\mathcal E\), equal to \(\mathcal E\) off \(X\), such that \(P'=\mathcal E'|_X\) is torsion-free of rank \(r\) and of slope width at most one.

**Proof.** Suppose that the slope width of \(P\) exceeds one. Let \(G=G_k\) be the last Harder–Narasimhan factor of \(P\) and \(B=P_{k-1}\), and form \(\mathcal E'\) as in Lemma 3.1. By that lemma,
\[
0\to G(H)\to P'\to B\to0 ,
\]
so \(P'\) is torsion-free, as an extension of torsion-free sheaves, of rank \(r\).

*The maximal slope does not increase.* \(G(H)\) is semistable of slope \(\mu(G)+1<\mu_{\max}(P)\), and \(\mu_{\max}(B)\le\mu_{\max}(P)\) because \(B\subseteq P\). By Lemma 2.1(3), \(\mu_{\max}(P')\le\mu_{\max}(P)\).

*The average slope increases.* By (CS), \(c_1(P')=c_1(G)+(\operatorname{rk}G)H+c_1(B)\), which is \(c_1(P)+(\operatorname{rk}G)H\), so
\[
\mu(P')=\mu(P)+\frac{\operatorname{rk}G}r\ge\mu(P)+\frac1r .
\]

Repeat as long as the width exceeds one. The average slope \(\mu(P)\le\mu_{\max}(P)\) never exceeds the initial maximal slope and grows by at least \(1/r\) at each step. So the process stops, and when it stops the width is at most one. Each step keeps the sheaf torsion-free, unchanged off \(X\), and with a torsion-free restriction of rank \(r\). \(\blacksquare\)

The restriction need not become semistable; only the spread of its slopes is controlled. The modified sheaf can be quite different from the original one along \(X\), but it is the same away from \(X\), and only this matters for the next section.

## 4. A variance inequality on the plane

For a coherent sheaf \(F\) on \(D=\mathbb P^2\) of rank \(N>0\), put
\[
v(F)=\frac{2\operatorname{ch}_2(F)}N-\Bigl(\frac{c_1(F)}N\Bigr)^2 .
\]
For \(F=\bigoplus_{i=1}^N\mathcal O(a_i)\) this is \(\frac1N\sum a_i^2-\bigl(\frac1N\sum a_i\bigr)^2\), the variance of the integers \(a_i\). By Lemma 1.1(2), \(v(F(1))=v(F)\). In general \(v\) can be negative: the ideal sheaf of a point has rank one, \(c_1=0\) and \(\operatorname{ch}_2=-1\) (Exercise 6.2).

**Lemma 4.1** (restriction to a Cartier divisor in Hilbert polynomials). Let \(V\) be a Noetherian scheme with an effective Cartier divisor \(D\cong\mathbb P^2\) whose ideal \(\mathcal I\) satisfies \(\mathcal I|_D\cong\mathcal O_D(1)\). For a coherent sheaf \(Q\) on \(V\) killed by a power of \(\mathcal I\), the sheaves \(Q|_D\) and \(\operatorname{Tor}_1^{\mathcal O_V}(Q,\mathcal O_D)\) are coherent sheaves on \(D\); put
\[
\begin{aligned}
\delta_Q(t)&=\chi\bigl(Q|_D(t)\bigr)\\
&\quad-\chi\bigl(\operatorname{Tor}_1(Q,\mathcal O_D)(t)\bigr) .
\end{aligned}
\]
Then \(\delta\) is additive in short exact sequences of such sheaves, and \(\delta_Q(t)=\chi(Q(t))-\chi(Q(t+1))\) if \(\mathcal IQ=0\).

**Proof.** Locally \(\mathcal O_D\) has the free resolution \(0\to\mathcal I\to\mathcal O_V\to\mathcal O_D\to0\), so \(\operatorname{Tor}_i(-,\mathcal O_D)=0\) for \(i\ge2\), and a short exact sequence \(0\to Q'\to Q\to Q''\to0\) gives the exact sequence
\[
\begin{aligned}
&0\to\operatorname{Tor}_1(Q')\to\operatorname{Tor}_1(Q)\\
&\quad\to\operatorname{Tor}_1(Q'')\to Q'|_D\\
&\quad\to Q|_D\to Q''|_D\to0 .
\end{aligned}
\]
The alternating sum of Euler characteristics of an exact sequence of coherent sheaves on \(D\) is zero. If \(\mathcal IQ=0\), then \(Q|_D=Q\) and \(\operatorname{Tor}_1(Q,\mathcal O_D)=Q\otimes\mathcal I=Q(1)\), since the local equation acts by zero on \(Q\). \(\blacksquare\)

**Proposition 4.2** (variance inequality; [OpenAI-SCM, Lemma 4.1]). Let \(V\) be an integral Noetherian scheme with an effective Cartier divisor \(D\cong\mathbb P^2\) whose ideal \(\mathcal I\) satisfies \(\mathcal I|_D\cong\mathcal O_D(1)\). Let \(L'\) be a coherent torsion-free sheaf on \(V\) with \(L'|_{V\setminus D}\cong\mathcal O^N\), \(N>0\). Then \(F=L'|_D\) has rank \(N\) and \(v(F)\ge0\).

**Proof.** *Rank.* At the generic point \(\eta\) of \(D\), \(\mathcal O_{V,\eta}\) is a local ring of dimension one whose maximal ideal is generated by the nonzerodivisor \(u\): a discrete valuation ring. The torsion-free \(L'_\eta\) is free of rank \(N\), so \(F\) has rank \(N\).

*A sandwich.* Let \(L=\mathcal O_V^N\) and identify \(L\) and \(L'\) off \(D\). Both are torsion-free, so on an affine open set \(\operatorname{Spec}B\) on which \(D\) is cut out by \(u\), both modules lie in \(B_u^N\); they are finitely generated, so \(u^bL\subseteq L'\subseteq u^{-b}L\) there for some \(b\). Finitely many such sets cover \(V\), so
\[
\mathcal I^bL\subseteq L'\subseteq\mathcal I^{-b}L
\]
for some \(b\ge0\). Replacing \(L'\) by \(\mathcal I^bL'\cong L'\otimes\mathcal I^b\) replaces \(F\) by \(F(b)\) and does not change \(v(F)\). So we may assume \(\mathcal I^{2b}L\subseteq L'\subseteq L\).

*The layers.* \(Q=L/L'\) is killed by \(\mathcal I^{2b}\). Its layers \(Q_j=\mathcal I^jQ/\mathcal I^{j+1}Q\), \(0\le j<2b\), are killed by \(\mathcal I\), and \(Q_j\) is a quotient of \(\mathcal I^jL/\mathcal I^{j+1}L=\mathcal O_D(j)^N\). Let \(n_j=\operatorname{rk}Q_j\). Then \(0\le n_j\le N\), and \(Q_j(-j)\) is a quotient of \(\mathcal O_D^N\), hence globally generated; by Lemma 1.1,
\[
c_1(Q_j)=c_1\bigl(Q_j(-j)\bigr)+jn_j\ge jn_j .
\]

*The restriction.* The sequence \(0\to L'\to L\to Q\to0\) restricts to
\[
\begin{aligned}
&0\to\operatorname{Tor}_1(Q,\mathcal O_D)\to F\\
&\quad\to\mathcal O_D^N\to Q|_D\to0 ,
\end{aligned}
\]
because \(\operatorname{Tor}_1(L,\mathcal O_D)=0\) and \(\operatorname{Tor}_1(L',\mathcal O_D)=0\), \(u\) being injective on the torsion-free \(L'\). So \(\chi(F(t))=N\chi(\mathcal O(t))-\delta_Q(t)\). The filtration of \(Q\) by the \(\mathcal I^jQ\) and Lemma 4.1 give \(\delta_Q(t)=\sum_j\bigl(\chi(Q_j(t))-\chi(Q_j(t+1))\bigr)\), so
\[
\begin{aligned}
\chi(F(t))&=N\chi(\mathcal O(t))+\sum_j\chi\bigl(Q_j(1)(t)\bigr)\\
&\quad-\sum_j\chi\bigl(Q_j(t)\bigr) .
\end{aligned}
\]
By Lemma 1.1(2), \(c_1(Q_j(1))-c_1(Q_j)=n_j\) and \(\operatorname{ch}_2(Q_j(1))-\operatorname{ch}_2(Q_j)=c_1(Q_j)+\tfrac12n_j\). Comparing coefficients,
\[
\begin{aligned}
c_1(F)&=\sum_jn_j,\\
2\operatorname{ch}_2(F)&=\sum_j\bigl(2c_1(Q_j)+n_j\bigr)\\
&\ge\sum_j(2j+1)n_j .
\end{aligned}
\]

*The inequality.* Using \(\sum_j jn_j=\sum_{j>l}n_j\), where the sum runs over the pairs \(j>l\ge0\),
\[
\begin{aligned}
&N\sum_j(2j+1)n_j-\Bigl(\sum_jn_j\Bigr)^2\\
&\quad=\sum_jn_j(N-n_j)\\
&\qquad+2\sum_{j>l}n_j(N-n_l)\ge0 ,
\end{aligned}
\]
since \(0\le n_j\le N\). So \(2N\operatorname{ch}_2(F)\ge c_1(F)^2\), and dividing by \(N^2\) gives \(v(F)\ge0\). \(\blacksquare\)

For \(L'=L\) the inequality is an equality. For \(L'=\bigoplus_i\mathcal I^{a_i}\), \(F=\bigoplus_i\mathcal O(a_i)\) and \(v(F)\) is the variance of the \(a_i\) (Exercise 6.3). The proof shows more: \(2N\operatorname{ch}_2(F)-c_1(F)^2\ge\sum_jn_j(N-n_j)\).

## 5. Consequence for small Cohen–Macaulay modules

**Corollary 5.1.** Let \(X\), \(H\), \(R=R(X,H)\), \(f\colon X\to\mathbb P^2\) and the regular model \(W\) be as in [Completed cones over surfaces](completed-cones-over-surfaces.md), and let \(M\) be a small Cohen–Macaulay \(R\)-module of rank \(r\). Then there is a torsion-free sheaf \(P\) of rank \(r\) on \(X\) whose slope width is at most one and such that \(v(f_*P)\ge0\), where \(f_*P\) has rank \(N=rh\).

**Proof.** Let \(\mathcal E\) be the sheaf of Proposition 6.1 of the lesson on completed cones. Proposition 3.2 applies to \(\mathcal E\) on \(W\) (an integral Noetherian scheme with the Cartier divisor \(X\), \(\mathcal J|_X=\mathcal O_X(H)\)) and gives \(\mathcal E'\) equal to \(\mathcal E\) off \(X\), with restriction \(P\) of rank \(r\) and slope width at most one. Since \(\mathcal E'\) is unchanged off \(X\), \(L'=g_*\mathcal E'\) is still torsion-free and trivial of rank \(N\) off \(D\), and \(L'|_D=f_*P\) by the computation in Proposition 6.1 of that lesson, which used only that \(\mathcal J=g^*\mathcal I\) and that \(g\) is affine. Proposition 4.2 gives \(v(f_*P)\ge0\). \(\blacksquare\)

## 6. Exercises

**6.1.** Show that \(v(F)\) is unchanged when \(F\) is replaced by \(F(b)\) for any integer \(b\).

**6.2.** Let \(\mathcal I_p\subset\mathcal O_{\mathbb P^2}\) be the ideal sheaf of a point. Compute \(\operatorname{rk}\), \(c_1\), \(\operatorname{ch}_2\) and \(v\) of \(\mathcal I_p\).

**6.3.** Let \(F=\bigoplus_{i=1}^N\mathcal O(a_i)\). Show that \(v(F)=\frac1N\sum_i\bigl(a_i-\bar a\bigr)^2\) with \(\bar a=\frac1N\sum a_i\), so \(v(F)=0\) exactly when all \(a_i\) are equal.

**6.4.** In the setting of Proposition 4.2, let \(L'=\mathcal O_V^{\oplus n}\oplus\mathcal I^{\oplus(N-n)}\subseteq L=\mathcal O_V^{\oplus N}\). Compute \(F\), the \(n_j\), and both sides of the inequality.

**6.5.** Show that the balancing procedure of Proposition 3.2, applied to a sheaf whose restriction is \(P=\mathcal O_X\oplus\mathcal O_X(-2H)\), stops after one step.

## 7. Solutions

**6.1.** By Lemma 1.1(2) with \(\operatorname{rk}F=N\): \(c_1\) becomes \(c_1+bN\) and \(\operatorname{ch}_2\) becomes \(\operatorname{ch}_2+bc_1+\tfrac12b^2N\). Then
\[
\begin{aligned}
&\frac{2\operatorname{ch}_2}N+\frac{2bc_1}N+b^2-\Bigl(\frac{c_1}N+b\Bigr)^2\\
&\quad=\frac{2\operatorname{ch}_2}N-\Bigl(\frac{c_1}N\Bigr)^2 .
\end{aligned}
\]

**6.2.** \(0\to\mathcal I_p\to\mathcal O\to\mathcal O_p\to0\) and \(\chi(\mathcal O_p(t))=1\) give \(\chi(\mathcal I_p(t))=\binom{t+2}2-1\). So \(\operatorname{rk}=1\), \(c_1=0\), \(\operatorname{ch}_2=-1\) and \(v=-2\).

**6.3.** By additivity \(c_1(F)=\sum a_i\) and \(2\operatorname{ch}_2(F)=\sum a_i^2\), so \(v(F)=\frac1N\sum a_i^2-\bar a^2=\frac1N\sum(a_i-\bar a)^2\).

**6.4.** Since \(\mathcal I\otimes\mathcal O_D=\mathcal O_D(1)\), \(F=\mathcal O_D^n\oplus\mathcal O_D(1)^{N-n}\). Further \(Q=L/L'=(\mathcal O_V/\mathcal I)^{N-n}=\mathcal O_D^{N-n}\), so only \(j=0\) occurs, with \(n_0=N-n\) and \(c_1(Q_0)=0\). Then \(c_1(F)=N-n\), \(2\operatorname{ch}_2(F)=N-n\), and \(2N\operatorname{ch}_2-c_1^2\) equals \(N(N-n)-(N-n)^2=n(N-n)\ge0\), with equality exactly when \(n=0\) or \(n=N\).

**6.5.** The factors are \(G_1=\mathcal O_X\) of slope \(0\) and \(G_2=\mathcal O_X(-2H)\) of slope \(-2\); the width is two. The modification gives \(0\to\mathcal O_X(-H)\to P'\to\mathcal O_X\to0\). Every nonzero subsheaf of \(P'\) has slope at most \(0\) by Lemma 2.1(3). If \(P'\) is not semistable, its last factor \(Z\) is a torsion-free quotient of rank one. If \(\mathcal O_X(-H)\to Z\) is nonzero, its image is \(\mathcal O_X(-H)\) itself (a torsion-free quotient of rank one of a line bundle), with a quotient of rank zero, so \(\mu(Z)\ge-1\) by (CS); otherwise \(Z\) is a quotient of \(\mathcal O_X\) and \(\mu(Z)\ge0\). So all slopes lie in \([-1,0]\), the width is at most one, and the procedure stops.

## References

- [OpenAI-SCM] OpenAI, *A Complete Local Domain without a Small Cohen–Macaulay Module*, OpenAI Math Release preprint, 23 September 2026, Sections 3 and 4. https://github.com/openai/math/tree/main/preprints/A-Complete-Local-Domain-Without-a-Small-Cohen-Macaulay-Module-September-23-2026
- [Reid] M. Reid, *Chapters on algebraic surfaces*, in: Complex Algebraic Geometry (Park City, 1993), Chapter B, item ix. https://arxiv.org/abs/alg-geom/9602006
