# The numerical obstruction

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson proves the obstruction of the course: if the completed cone \(R(X,H)\) over a smooth projective surface has a small Cohen–Macaulay module, then \(K_X^2-2c_2(X)\le6H^2\). By [Elementary modifications and a variance inequality](elementary-modifications-and-a-variance-inequality.md), such a module gives a torsion-free sheaf \(P\) on \(X\) with Harder–Narasimhan slopes in an interval of length at most one, and with \(v(f_*P)\ge0\) for a finite map \(f\colon X\to\mathbb P^2\). Here the same quantity \(v(f_*P)\) is bounded from above: by Riemann–Roch it is computed from the Chern classes of the factors, and Bogomolov's inequality, the Hodge index theorem and Noether's formula bound it by \(\frac12-\frac{K_X^2-2c_2(X)}{12H^2}\).

- Two named hypotheses: Noether's formula and Bogomolov's inequality (Section 1).
- The upper bound for one semistable factor (Lemma 2.1).
- Mixtures of factors and the proof of the obstruction (Section 3).
- Examples (Section 4).

The lesson follows [OpenAI-SCM, Section 5]. It uses hypothesis (CS) of the lesson on elementary modifications, the Chern classes on \(\mathbb P^2\) defined there through Hilbert polynomials, and the Hodge index theorem, Theorem HI of [Cycle classes and the Lefschetz fixed point formula for curves](course:AG-LTF/cycle-classes-and-the-lefschetz-fixed-point-formula-for-curves) (course *ℓ-adic cohomology and trace formulas*).

## 1. Two named hypotheses

Let \(X\) be a smooth integral projective surface over \(\mathbb C\), with canonical divisor \(K_X\). Write \(c_2(X)\) for the topological Euler number of the complex manifold \(X\), the alternating sum of its Betti numbers; it equals the second Chern class of the tangent bundle.

**Hypothesis (NF)** (Noether's formula). \(12\chi(\mathcal O_X)=K_X^2+c_2(X)\).

**Hypothesis (BI)** (Bogomolov's inequality). Let \(H\) be ample and \(G\) a torsion-free sheaf of rank \(u\ge1\) on \(X\) that is semistable for the slope defined by \(H\). Then
\[
2u\operatorname{ch}_2(G)\le c_1(G)^2 .
\]

With \(c_2(G)=\tfrac12c_1(G)^2-\operatorname{ch}_2(G)\), (BI) says that the discriminant \(2uc_2(G)-(u-1)c_1(G)^2\) is nonnegative. Neither statement is proved in the programme. (NF) is stated in [Reid, Chapter B, item ix]. (BI) is due to Bogomolov; it is stated, with the discriminant, in [Langer, Section 2 and Theorem 3.13]. Semistability does not change when \(H\) is replaced by a positive multiple, so the very ample polarization used there covers the ample one used here.

**The Hodge index theorem in the form used.** If \(H\) is ample, \(h=H^2\), and \(C\) is a divisor class with rational coefficients, then
\[
h\,C^2\le(C\cdot H)^2 .
\]
Indeed, for an integral multiple \(nC\), the class \(E=h\,nC-(nC\cdot H)H\) satisfies \(E\cdot H=0\), so \(E^2\le0\) by Theorem HI of the lesson on cycle classes; expanding, \(E^2=h^2n^2C^2-h\,n^2(C\cdot H)^2\).

## 2. One semistable factor

Fix \(X\), an ample and globally generated \(H\) with \(h=H^2\), and the finite map \(f\colon X\to\mathbb P^2\) with \(f^*\mathcal O(1)=\mathcal O_X(H)\) of Lemma 2.1 of [Completed cones over surfaces](completed-cones-over-surfaces.md), of degree \(h\). For a coherent sheaf \(F\) on \(\mathbb P^2\) of rank \(N>0\), \(v(F)=2\operatorname{ch}_2(F)/N-(c_1(F)/N)^2\) as in the lesson on elementary modifications, with Chern classes defined through Hilbert polynomials. Put \(k=K_X\cdot H\).

**Lemma 2.1** ([OpenAI-SCM, Lemma 5.1]). Assume (CS), (NF) and (BI). For every nonzero torsion-free semistable sheaf \(G\) on \(X\),
\[
v(f_*G)\le\frac14-\frac{K_X^2-2c_2(X)}{12h},
\]
and
\[
\frac{c_1(f_*G)}{\operatorname{rk}(f_*G)}=\mu(G)-\frac k{2h}-\frac32 .
\]

**Proof.** Let \(u=\operatorname{rk}G\). The sheaf \(F=f_*G\) has rank \(uh\), since \(f\) has degree \(h\). Put
\[
\begin{gathered}
m=\frac{c_1(F)}{uh},\qquad q=\frac{\operatorname{ch}_2(F)}{uh},\\
a=\mu(G)-\frac k{2h} .
\end{gathered}
\]

*Two Riemann–Roch polynomials.* Since \(f\) is finite and \(f^*\mathcal O(t)=\mathcal O_X(tH)\), \(\chi(X,G(tH))=\chi(\mathbb P^2,F(t))\) for every \(t\). On \(\mathbb P^2\), by the definition of the Chern classes and \(\binom{t+2}2=\tfrac12t^2+\tfrac32t+1\),
\[
\begin{aligned}
\frac{\chi(F(t))}{uh}&=\frac{t^2}2+\Bigl(\frac32+m\Bigr)t\\
&\quad+1+\frac32m+q .
\end{aligned}
\]
On \(X\), (CS) gives
\[
\begin{aligned}
c_1(G(tH))&=c_1(G)+utH,\\
\operatorname{ch}_2(G(tH))&=\operatorname{ch}_2(G)+t\,c_1(G)\cdot H\\
&\quad+\tfrac12ut^2h,
\end{aligned}
\]
and Riemann–Roch, divided by \(uh\), gives
\[
\begin{aligned}
\frac{\chi(G(tH))}{uh}&=\frac{t^2}2+a\,t+\frac{\chi(\mathcal O_X)}h\\
&\quad+\frac{\operatorname{ch}_2(G)}{uh}-\frac{c_1(G)\cdot K_X}{2uh} .
\end{aligned}
\]

*Comparison.* The coefficients of \(t\) give \(\frac32+m=a\), which is the formula for \(c_1(F)/\operatorname{rk}F=m\). The constant terms give
\[
\begin{aligned}
q&=\frac{\chi(\mathcal O_X)}h+\frac{\operatorname{ch}_2(G)}{uh}\\
&\quad-\frac{c_1(G)\cdot K_X}{2uh}-1-\frac32m .
\end{aligned}
\]
With \(m=a-\frac32\), one has \(-2-3m-m^2=\frac14-a^2\), so
\[
\begin{aligned}
2q-m^2&=\frac14+\frac{2\chi(\mathcal O_X)}h\\
&\quad+\frac{2\operatorname{ch}_2(G)}{uh}-\frac{c_1(G)\cdot K_X}{uh}\\
&\quad-a^2 .
\end{aligned}
\]

*Bogomolov and Hodge index.* By (BI), \(2\operatorname{ch}_2(G)/u\le c_1(G)^2/u^2\). Put \(C=c_1(G)/u-\tfrac12K_X\), a class with rational coefficients. Then
\[
\begin{aligned}
&\frac{c_1(G)^2}{u^2}-\frac{c_1(G)\cdot K_X}u\\
&\quad=C^2-\frac{K_X^2}4,\qquad a=\frac{C\cdot H}h .
\end{aligned}
\]
So the terms of \(2q-m^2\) after \(\frac{2\chi(\mathcal O_X)}h\) add up to at most
\[
\frac{C^2-K_X^2/4}h-\frac{(C\cdot H)^2}{h^2}\le-\frac{K_X^2}{4h}
\]
by the Hodge index theorem. Hence \(2q-m^2\le\frac14+\frac{2\chi(\mathcal O_X)}h-\frac{K_X^2}{4h}\).

*Noether.* By (NF), \(2\chi(\mathcal O_X)=\frac16(K_X^2+c_2(X))\), so
\[
\begin{aligned}
&\frac{2\chi(\mathcal O_X)}h-\frac{K_X^2}{4h}\\
&\quad=\frac{2K_X^2+2c_2(X)-3K_X^2}{12h}\\
&\quad=-\frac{K_X^2-2c_2(X)}{12h} .
\end{aligned}
\]
Since \(v(F)=2q-m^2\), this proves the lemma. \(\blacksquare\)

The first part of the lemma is the only place where semistability enters; the second part holds for every \(G\) of positive rank.

## 3. Mixtures and the obstruction

**Lemma 3.1** (mixture). Let \(F\) on \(\mathbb P^2\) have a filtration with factors \(F_i\) of positive ranks \(N_i\), \(N=\sum_iN_i\), and put \(w_i=N_i/N\), \(m_i=c_1(F_i)/N_i\), \(\bar m=\sum_iw_im_i\). Then
\[
v(F)=\sum_iw_i\,v(F_i)+\sum_iw_i(m_i-\bar m)^2 .
\]

**Proof.** By additivity, \(c_1(F)/N=\bar m\) and 
\[
\begin{aligned}
\frac{2\operatorname{ch}_2(F)}N&=\sum_iw_i\frac{2\operatorname{ch}_2(F_i)}{N_i}\\
&=\sum_iw_i\bigl(v(F_i)+m_i^2\bigr) .
\end{aligned}
\]
Subtract \(\bar m^2\) and use \(\sum_iw_im_i^2-\bar m^2=\sum_iw_i(m_i-\bar m)^2\). \(\blacksquare\)

**Lemma 3.2.** If numbers \(m_i\) lie in an interval of length at most one and \(w_i\ge0\), \(\sum_iw_i=1\), then \(\sum_iw_i(m_i-\bar m)^2\le\frac14\).

**Proof.** For every number \(c\),
\[
\begin{aligned}
\sum_iw_i(m_i-c)^2&=\sum_iw_i(m_i-\bar m)^2\\
&\quad+(\bar m-c)^2 ,
\end{aligned}
\]
so the weighted mean minimizes the mean square distance. Take \(c\) the midpoint of the interval; every \(m_i\) is within \(\frac12\) of it. \(\blacksquare\)

**Theorem 3.3** (obstruction; [OpenAI-SCM, Theorem 1.2]). Assume (CS), (NF) and (BI). Let \(X\) be a smooth integral projective surface over \(\mathbb C\) and \(H\) a divisor with \(\mathcal O_X(H)\) ample and globally generated. If \(R(X,H)\) has a small Cohen–Macaulay module, then
\[
K_X^2-2c_2(X)\le6H^2 .
\]

**Proof.** Let \(h=H^2\). By Corollary 5.1 of the lesson on elementary modifications, there is a torsion-free sheaf \(P\) of rank \(r\) on \(X\) with Harder–Narasimhan factors \(G_1,\dots,G_k\) whose slopes lie in an interval of length at most one, and with \(v(f_*P)\ge0\). Pushforward along the finite map \(f\) is exact, so the \(F_i=f_*G_i\) are the factors of a filtration of \(F=f_*P\), of ranks \(N_i=u_ih\), \(u_i=\operatorname{rk}G_i\); the weights are \(w_i=u_i/r\). By Lemma 2.1, \(m_i=c_1(F_i)/N_i\) differs from \(\mu(G_i)\) by the same constant for all \(i\), so the \(m_i\) lie in an interval of length at most one. Lemmas 3.1, 3.2 and 2.1 give
\[
0\le v(F)\le\frac14-\frac{K_X^2-2c_2(X)}{12h}+\frac14 .
\]
So \(K_X^2-2c_2(X)\le6h\). \(\blacksquare\)

Neither \(P\) nor \(f_*P\) needs to be semistable, and no grading of the module is used: the argument works with the actual sheaf on the punctured spectrum. Both inequalities come from different sources. The lower bound \(v\ge0\) comes from the triviality of the module over the power series ring, that is, from the Cohen–Macaulay property. The upper bound comes from the geometry of the surface, through Bogomolov's inequality.

**Corollary 3.4.** Assume (CS), (NF) and (BI). If \(K_X^2-2c_2(X)>6H^2\) for an ample and globally generated \(H\), then \(R(X,H)\) is a three-dimensional complete Noetherian normal local domain with residue field \(\mathbb C\) without a small Cohen–Macaulay module.

**Proof.** Proposition 3.1 and Proposition 4.1 of the lesson on completed cones, and Theorem 3.3. \(\blacksquare\)

## 4. Examples

The inequality \(K_X^2-2c_2(X)>6H^2\) is far from the surfaces one meets first. For \(\mathbb P^2\), \(K^2=9\) and \(c_2=6\), so \(K^2-2c_2=3\); for \(\mathbb P^1\times\mathbb P^1\), \(K^2=8\) and \(c_2=4\), so \(K^2-2c_2=0\). Both satisfy the obstruction for every \(H\), and indeed their completed cones for the polarizations of Exercises 7.1 and 7.2 of the lesson on completed cones are Cohen–Macaulay. The obstruction can only bite when \(K_X^2>2c_2(X)\), a region close to the bound \(K_X^2\le3c_2(X)\) of Miyaoka and Yau, and only for polarizations of small degree. Covers of the plane branched along line arrangements, studied by Hirzebruch, reach this region; [A Hirzebruch–Kummer surface](a-hirzebruch-kummer-surface.md) constructs one together with a polarization of small degree.

## 5. Exercises

**5.1.** Let \(G=\mathcal O_X\). Show that
\[
\begin{aligned}
v(f_*\mathcal O_X)&=\frac14+\frac{2\chi(\mathcal O_X)}h\\
&\quad-\frac{(K_X\cdot H)^2}{4h^2},
\end{aligned}
\]
and check it for \(X=\mathbb P^2\), \(H\) a line, where \(f_*\mathcal O_X=\mathcal O\).

**5.2.** For \(X=\mathbb P^1\times\mathbb P^1\) and \(H\) of bidegree \((1,1)\), the map \(f\) is the projection of the quadric surface in \(\mathbb P^3\) from a point outside it, and \(f_*\mathcal O_X=\mathcal O\oplus\mathcal O(-1)\). Compute \(v(f_*\mathcal O_X)\) in two ways.

**5.3.** Show that the bound of Lemma 2.1 for \(G=\mathcal O_X\) is equivalent to \(K_X^2\,H^2\le(K_X\cdot H)^2\), using (NF), and that this is an instance of the Hodge index theorem.

**5.4.** Show that the bound \(\frac14\) in Lemma 3.2 is attained, and that it cannot be improved for two values at distance one.

**5.5.** Suppose that the slope width in Corollary 5.1 of the lesson on elementary modifications could be made at most \(\lambda\). Which inequality would the proof of Theorem 3.3 give?

## 6. Solutions

**5.1.** For \(G=\mathcal O_X\): \(u=1\), \(c_1(G)=0\), \(\operatorname{ch}_2(G)=0\), \(\mu(G)=0\), \(a=-\frac k{2h}\). The formula for \(2q-m^2\) in the proof of Lemma 2.1 gives the claim. For \(\mathbb P^2\): \(\chi(\mathcal O)=1\), \(h=1\), \(K\cdot H=-3\), so \(v=\frac14+2-\frac94=0\), the variance of a single line bundle.

**5.2.** Directly: the variance of \(\{0,-1\}\) is \(\frac14\). By Exercise 5.1: \(\chi(\mathcal O_X)=1\), \(h=2\), \(K_X\cdot H=-4\), so \(v=\frac14+1-1=\frac14\).

**5.3.** By Exercise 5.1 and (NF), \(2\chi(\mathcal O_X)/h=(K_X^2+c_2(X))/(6h)\). The inequality \(v\le\frac14+\frac{2c_2(X)-K_X^2}{12h}\) becomes \(\frac{2K_X^2+2c_2(X)}{12h}-\frac{k^2}{4h^2}\le\frac{2c_2(X)-K_X^2}{12h}\), that is, \(\frac{K_X^2}{4h}\le\frac{k^2}{4h^2}\), or \(K_X^2\,h\le k^2\). This is the Hodge index theorem of Section 1 for \(C=K_X\).

**5.4.** Two values \(0\) and \(1\) with weights \(\frac12\) have variance \(\frac14\). For two values at distance one with weights \(w,1-w\), the variance is \(w(1-w)\le\frac14\), with equality at \(w=\frac12\).

**5.5.** The weighted variance would be at most \(\lambda^2/4\), and the proof would give \(0\le\frac14+\frac{\lambda^2}4-\frac{K_X^2-2c_2(X)}{12h}\), that is, \(K_X^2-2c_2(X)\le3(1+\lambda^2)H^2\). The balancing of Proposition 3.2 there reaches \(\lambda=1\), which gives the constant \(6\).

## References

- [OpenAI-SCM] OpenAI, *A Complete Local Domain without a Small Cohen–Macaulay Module*, OpenAI Math Release preprint, 23 September 2026, Section 5. https://github.com/openai/math/tree/main/preprints/A-Complete-Local-Domain-Without-a-Small-Cohen-Macaulay-Module-September-23-2026
- [Reid] M. Reid, *Chapters on algebraic surfaces*, in: Complex Algebraic Geometry (Park City, 1993), Chapter B, item ix. https://arxiv.org/abs/alg-geom/9602006
- [Langer] A. Langer, *On boundedness of semistable sheaves*, arXiv:2107.03125, version 2, Section 2 and Theorem 3.13. https://arxiv.org/abs/2107.03125
