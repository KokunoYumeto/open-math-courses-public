# Ehrhard concavity and the loss of one score

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

We continue in the standing setting (S1)–(S6) of [Gaussian first moments of partitions](gaussian-first-moments-of-partitions.md), Section 4. [Rearrangement bounds for one cell](rearrangement-bounds-for-one-cell.md) gave \(P_i>Ar_i^2\), a bound that is weak for short moments. This lesson proves a bound that is linear in \(r_i\) (Proposition 5.2):
\[
P_i>0.415\,r_i+0.15\,r_i^2 .
\]
The idea is to delete one score. By optimality the expected maximum of the remaining scores is noticeably smaller, so the deleted score must win by a margin on a substantial set. On the other hand, the probability that the deleted score wins by a margin \(u\) is the Gaussian measure of a translate of its cone, and Ehrhard's inequality makes this probability decay at least as fast as for a half-space.

## 1. The loss of one score

Fix \(i\), put \(\alpha=m/(m-1)\), \(M_i=\max_{j\ne i}X_j\), and \(u_+=\max\{u,0\}\).

**Lemma 1.1.** \(1-\alpha r_i^2\ge0\), and
\[
\mathbb E(X_i-M_i)_+\ge C\bigl(1-\sqrt{1-\alpha r_i^2}\bigr).
\]

**Proof.** Put \(w_j=z_j+z_i/(m-1)\) for \(j\ne i\). Since \(\sum_{j\ne i}z_j=-z_i\),
\[
\begin{aligned}
\sum_{j\ne i}|w_j|^2&=C-|z_i|^2-\frac{2|z_i|^2}{m-1}\\
&\quad+\frac{|z_i|^2}{m-1}=C-\alpha|z_i|^2 ,
\end{aligned}
\]
which is nonnegative, so \(\alpha r_i^2\le1\). The scores \(\langle w_j,g\rangle\) differ from the \(X_j\) by the common term \(\langle z_i,g\rangle/(m-1)\), whose mean is zero, so \(\mathbb EM_i=\mathbb E\max_{j\ne i}\langle w_j,g\rangle\), which is at most \(\sqrt C\sqrt{C-\alpha|z_i|^2}\) by (S6). Since \(\max_jX_j=M_i+(X_i-M_i)_+\) and \(\mathbb E\max_jX_j=C\) by (S5),
\[
\begin{aligned}
\mathbb E(X_i-M_i)_+&=C-\mathbb EM_i\\
&\ge C-\sqrt C\sqrt{C-\alpha|z_i|^2} .
\end{aligned}
\]
\(\square\)

## 2. Gap probabilities

By (S3) the vectors \(z_i-z_j\), \(j\ne i\), form a basis of \(V\), so there is \(h\in V\) with \(\langle h,z_i-z_j\rangle=1\) for every \(j\ne i\); then \(\langle h,z_i\rangle=1/\alpha\) ([Gaussian first moments of partitions](gaussian-first-moments-of-partitions.md), Exercise 5.5). For \(u\in\mathbb R\), the translate \(K_i+uh\) is the set of \(x\in V\) with \(\langle z_i-z_j,x\rangle\ge u\) for all \(j\ne i\). So the *gap probability* \(p_i(u)\), the probability that \(X_i-X_j\ge u\) for all \(j\ne i\), is
\[
p_i(u)=\gamma_{m-1}(K_i+uh).
\]

**Lemma 2.1.** \(p_i(0)=P_i\), \(p_i\) is differentiable, and \(p_i'(0)=-1/\alpha\). Moreover
\[
\mathbb E(X_i-M_i)_+=\int_0^\infty p_i(u)\,du .
\]

**Proof.** Write \(\varphi(y)=(2\pi)^{-(m-1)/2}e^{-|y|^2/2}\). Translation invariance of Lebesgue measure gives \(p_i(u)=\int_{K_i}\varphi(y+uh)\,dy\). The derivative of the integrand in \(u\) is \(-\langle y+uh,h\rangle\varphi(y+uh)\); for \(|u|\le u_0\) it is bounded by \(|h|(|y|+u_0|h|)\) times \((2\pi)^{-(m-1)/2}e^{-|y|^2/2+u_0|y||h|}\), which is integrable. Differentiation under the integral sign ([Fremlin, *Measure Theory*, Volume 1, 123D](https://www1.essex.ac.uk/maths/people/fremlin/chap12.pdf), core course [Measure and Integration](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D10)) gives
\[
\begin{aligned}
p_i'(0)&=-\int_{K_i}\langle y,h\rangle\varphi(y)\,dy\\
&=-\langle h,z_i\rangle=-\frac1\alpha ,
\end{aligned}
\]
using (S4). For the last formula, \(W=(X_i-M_i)_+\) is nonnegative, \(\mathbb EW=\int_0^\infty\Pr\{W\ge u\}\,du\) by Fubini's theorem, and for \(u>0\) the event \(\{W\ge u\}\) is \(\{X_i-X_j\ge u\text{ for all }j\ne i\}\). \(\square\)

## 3. Ehrhard's inequality

The following theorem is Theorem A of the course [Ehrhard's inequality for convex sets](course:ehrhards-inequality-for-convex-sets/gaussian-heat-semigroups-and-a-gradient-bound#the-theorem), where it is proved in full; Corollary 3.4 there is the concavity statement of Lemma 3.1 below.

**(EHR) Ehrhard's inequality.** Let \(K,L\subseteq\mathbb R^d\) be closed convex sets with \(\gamma_d(K),\gamma_d(L)\in(0,1)\), and \(0\le\lambda\le1\). Then
\[
\begin{aligned}
&\Phi^{-1}\bigl(\gamma_d(\lambda K+(1-\lambda)L)\bigr)\\
&\quad\ge\lambda\,\Phi^{-1}(\gamma_d(K))\\
&\qquad+(1-\lambda)\,\Phi^{-1}(\gamma_d(L)).
\end{aligned}
\]

Ehrhard proved it for convex sets by a Gaussian symmetrization [Ehrhard]. Latała extended it to the case in which only one set is convex, and Borell to arbitrary Borel sets; van Handel [vH] and Neeman and Paouris [NP] gave further proofs, by a stochastic game and by interpolation along the Ornstein–Uhlenbeck semigroup; the course cited above follows the interpolation method with the heat semigroup. For parallel half-spaces \(\{\langle e,x\rangle\le a\}\) and \(\{\langle e,x\rangle\le b\}\) both sides equal \(\lambda a+(1-\lambda)b\), so the inequality is sharp.

**Lemma 3.1.** The function \(u\mapsto\Phi^{-1}(p_i(u))\) is concave on \(\mathbb R\).

**Proof.** By (S4) the cone \(K_i\) is closed and convex with nonempty interior, and it is not all of \(V\); its complement is open and nonempty. So every translate \(K_i+uh\) has Gaussian measure in \((0,1)\). For convex \(K\), \(\lambda K+(1-\lambda)K=K\), hence
\[
\begin{aligned}
&\lambda(K_i+u_1h)+(1-\lambda)(K_i+u_2h)\\
&\quad=K_i+(\lambda u_1+(1-\lambda)u_2)h ,
\end{aligned}
\]
and (EHR) gives the concavity inequality. \(\square\)

**Lemma 3.2** (tangent bound). Let \(q=\Phi^{-1}(P_i)\). For every \(u\ge0\),
\[
p_i(u)\le\Phi\Bigl(q-\frac u{\alpha\phi(q)}\Bigr).
\]

**Proof.** The function \(\psi=\Phi^{-1}\circ p_i\) is concave by Lemma 3.1 and differentiable at \(0\) with \(\psi(0)=q\) and \(\psi'(0)=p_i'(0)/\phi(q)=-1/(\alpha\phi(q))\), by Lemma 2.1 and the derivative of \(\Phi^{-1}\). For a concave function the difference quotient \((\psi(u)-\psi(0))/u\) is nonincreasing in \(u>0\), so it is at most its limit \(\psi'(0)\) as \(u\to0^+\). Hence \(\psi(u)\le q+\psi'(0)u\), and \(\Phi\) is increasing. \(\square\)

**Corollary 3.3.** With \(q=\Phi^{-1}(P_i)\),
\[
\mathbb E(X_i-M_i)_+\le\alpha\,\phi(q)\bigl(q\Phi(q)+\phi(q)\bigr).
\]

**Proof.** By Lemmas 2.1 and 3.2 and the substitution \(s=q-u/(\alpha\phi(q))\),
\[
\begin{aligned}
&\mathbb E(X_i-M_i)_+\\
&\quad\le\int_0^\infty\Phi\Bigl(q-\frac u{\alpha\phi(q)}\Bigr)du\\
&\quad=\alpha\phi(q)\int_{-\infty}^q\Phi(s)\,ds ,
\end{aligned}
\]
and \(\int_{-\infty}^q\Phi=q\Phi(q)+\phi(q)\), because the right side has derivative \(\Phi(q)\) and tends to \(0\) as \(q\to-\infty\). \(\square\)

**The loss constraint.** Put
\[
G(q)=\frac{\phi(q)\bigl(q\Phi(q)+\phi(q)\bigr)}{\Phi(q)^2}.
\]
Lemma 1.1 and Corollary 3.3 give
\[
\begin{aligned}
&\alpha\phi(q)\bigl(q\Phi(q)+\phi(q)\bigr)\\
&\quad\ge C\bigl(1-\sqrt{1-\alpha r_i^2}\bigr)\\
&\quad=\frac{C\alpha r_i^2}{1+\sqrt{1-\alpha r_i^2}} .
\end{aligned}
\]
Dividing by \(\alpha\), and using \(C>B^2\) and \(\alpha>1\), we obtain the *loss constraint* (L):
\[
P_i^2\,G\bigl(\Phi^{-1}(P_i)\bigr)>\frac{B^2r_i^2}{1+\sqrt{1-r_i^2}} .
\]

## 4. The function \(G\)

**Lemma 4.1.** Let \(\lambda(q)=\phi(q)/\Phi(q)\) and \(V(q)=\operatorname{Var}(Z\mid Z\le q)\) for a standard normal \(Z\). Then \(G=\lambda(q+\lambda)=1-V\), so \(0<G<1\); \(G\) is nonincreasing; and \(P\mapsto P^2G(\Phi^{-1}(P))\) is increasing on \((0,\frac12]\).

**Proof.** Integration by parts gives \(\int_{-\infty}^qs\phi(s)\,ds=-\phi(q)\) and \(\int_{-\infty}^qs^2\phi(s)\,ds=\Phi(q)-q\phi(q)\), so \(\mathbb E(Z\mid Z\le q)=-\lambda\) and \(V=1-q\lambda-\lambda^2\). Expanding \(G\) gives \(G=\lambda q+\lambda^2=1-V\). The variable \(U=q-Z\), conditioned on \(Z\le q\), is nonnegative and nonconstant, with mean \(q+\lambda>0\) and variance \(V>0\); so \(G=\lambda(q+\lambda)>0\) and \(G=1-V<1\).

The survival function of \(U\) is \(S(u)=\Phi(q-u)/\Phi(q)\) for \(u\ge0\). Since \(\lambda'=-\lambda(q+\lambda)\), we have \((\log\Phi)''=\lambda'<0\), so \(\log S\) is concave on \([0,\infty)\) with \(\log S(0)=0\). A concave function has nonincreasing increments over intervals of equal length, so \(\log S(u+v)-\log S(u)\) is at most \(\log S(v)-\log S(0)\), that is, \(S(u+v)\le S(u)S(v)\). Integrating over \(u,v\ge0\) by Fubini's theorem,
\[
\begin{aligned}
\frac12\mathbb EU^2&=\int_0^\infty\!\!\int_0^\infty S(u+v)\,du\,dv\\
&\le\Bigl(\int_0^\infty S\Bigr)^2=(\mathbb EU)^2 .
\end{aligned}
\]
So \(V=\mathbb EU^2-(\mathbb EU)^2\le(\mathbb EU)^2=(q+\lambda)^2\). Differentiating \(V=1-q\lambda-\lambda^2\) with \(\lambda'=-\lambda(q+\lambda)\),
\[
\begin{aligned}
V'&=-\lambda+\lambda(q+\lambda)(q+2\lambda)\\
&=\lambda\bigl((q+\lambda)^2-V\bigr)\ge0 ,
\end{aligned}
\]
so \(G=1-V\) is nonincreasing.

Finally \(P^2G(\Phi^{-1}(P))=\phi(q)(q\Phi(q)+\phi(q))\) with \(q=\Phi^{-1}(P)\). For \(q\le0\) both factors are positive and increasing in \(q\): \(\phi\) increases on \((-\infty,0]\), and \(q\Phi(q)+\phi(q)\) has derivative \(\Phi(q)>0\) and is positive, being \(\Phi(q)\,\mathbb E(q-Z\mid Z\le q)\). Since \(P\le\frac12\) means \(q\le0\), the claim follows. \(\square\)

At the two ends, \(G(0)=\phi(0)^2/\Phi(0)^2=2/\pi\) and \(G(q)\to1\) as \(q\to-\infty\) (Exercise 6.3).

## 5. The linear–quadratic bound

Put \(P_0(r)=(0.415+0.15r)\,r\). Then \(P_0(r)\le P_0(\frac23)=\frac{103}{300}<\frac12\) for \(0<r\le\frac23\).

**Lemma 5.1.** For \(0<r\le\frac23\) the following inequality (T) holds:
\[
\begin{aligned}
&(0.415+0.15r)^2\,G\bigl(\Phi^{-1}(P_0(r))\bigr)\\
&\qquad<\frac{B^2}{1+\sqrt{1-r^2}} .
\end{aligned}
\]

**Proof.** Cover \((0,\frac23]\) by the ten intervals \([a,b]\) of Table 1. On each interval we bound \(G(\Phi^{-1}(P_0(r)))\) above by the number \(U\) of the table: in the first row by \(G<1\) (Lemma 4.1); in the other rows, Table 2 gives a rational \(q_a\) with \(\Phi(q_a)<P_0(a)\) and \(G(q_a)<U\), and for \(r\ge a\) we have \(\Phi^{-1}(P_0(r))\ge\Phi^{-1}(P_0(a))>q_a\), so \(G(\Phi^{-1}(P_0(r)))\le G(q_a)<U\) because \(G\) is nonincreasing. The coefficient \((0.415+0.15r)^2\) and the right side of (T) increase with \(r\), so (T) holds on \([a,b]\) as soon as
\[
\begin{aligned}
&\Delta(a,b,U)=\frac{B^2}{1+\sqrt{1-a^2}}\\
&\quad-U(0.415+0.15b)^2>0 .
\end{aligned}
\]
The last column of Table 1 gives strict lower bounds, obtained with the rational enclosures of [Rearrangement bounds for one cell](rearrangement-bounds-for-one-cell.md), Section 3 (an upper bound for \(\pi\) in \(B^2=9/(8\pi)\) and an upper bound for \(\sqrt{1-a^2}\)). \(\square\)

*Table 1. The interval cover for (T).*

| \(a\) | \(b\) | \(U\) | \(10^6\,\Delta(a,b,U)>\) |
|---|---|---|---|
| 0 | 0.05 | 1 | 542 |
| 0.05 | 0.14 | 0.91 | 6173 |
| 0.14 | 0.24 | 0.87 | 2976 |
| 0.24 | 0.33 | 0.836 | 1328 |
| 0.33 | 0.41 | 0.809 | 523 |
| 0.41 | 0.48 | 0.788 | 392 |
| 0.48 | 0.54 | 0.771 | 1076 |
| 0.54 | 0.59 | 0.756 | 2787 |
| 0.59 | 0.64 | 0.743 | 4115 |
| 0.64 | 2/3 | 0.73 | 8886 |

*Table 2. Quantiles and values of \(G\), from the enclosures of \(\phi\) and \(\Phi\).*

| \(a\) | \(q_a\) | \(10^6\,(P_0(a)-\Phi(q_a))>\) | \(G(q_a)<\) |
|---|---|---|---|
| 0.05 | −2.033 | 98 | 0.887728 |
| 0.14 | −1.548 | 228 | 0.854397 |
| 0.24 | −1.238 | 381 | 0.826606 |
| 0.33 | −1.024 | 366 | 0.803691 |
| 0.41 | −0.860 | 470 | 0.783737 |
| 0.48 | −0.728 | 452 | 0.766006 |
| 0.54 | −0.621 | 539 | 0.750456 |
| 0.59 | −0.535 | 739 | 0.737150 |
| 0.64 | −0.450 | 684 | 0.723262 |

In every row of Table 2 the bound for \(G(q_a)\) is below the \(U\) of the same row of Table 1.

**Proposition 5.2.** For every \(i\), \(P_i>(0.415+0.15r_i)\,r_i\).

**Proof.** Suppose \(P_i\le P_0(r_i)\). Both numbers lie in \((0,\frac12]\), by (S5) and since \(r_i<\frac23\) ([Rearrangement bounds for one cell](rearrangement-bounds-for-one-cell.md), Proposition 2.4). By Lemma 4.1,
\[
\begin{aligned}
&P_i^2G(\Phi^{-1}(P_i))\\
&\quad\le P_0(r_i)^2G\bigl(\Phi^{-1}(P_0(r_i))\bigr)\\
&\quad=r_i^2(0.415+0.15r_i)^2\\
&\qquad\cdot G\bigl(\Phi^{-1}(P_0(r_i))\bigr),
\end{aligned}
\]
which is less than \(B^2r_i^2/(1+\sqrt{1-r_i^2})\) by (T). This contradicts (L). \(\square\)

**Summary of the scalar bounds.** With \(A=0.929\) for \(m=5\) and \(A=0.884\) for \(m\ge6\), every cell satisfies
\[
\begin{gathered}
r_i<\frac23,\qquad P_i>Ar_i^2,\\
P_i>0.415\,r_i+0.15\,r_i^2 .
\end{gathered}
\]
These three bounds, the identities \(\sum P_i=\sum r_i^2=1\), and the geometric constraints of [Two competing scores](two-competing-scores.md) are all that [Five or more cells and the propeller bound](five-or-more-cells-and-the-propeller-bound.md) uses.

## 6. Exercises

**6.1** (easy). Let \(K=\{x:\langle e,x\rangle\ge0\}\) with \(|e|=1\), and \(h\) a vector with \(\langle e,h\rangle=c>0\). Show that \(\Phi^{-1}(\gamma_d(K+uh))=-cu\) for all \(u\), so Lemma 3.2 holds with equality for a half-space whose parameters match.

**6.2** (medium). Suppose only that \(\log p_i\) is concave. (This follows from Lemma 3.1, because \(\log\Phi\) is concave and increasing.) Show that then \(p_i(u)\le P_ie^{-u/(\alpha P_i)}\), and that the argument of Section 3 yields only \(P_i>Br_i/\sqrt{1+\sqrt{1-r_i^2}}\). Evaluate both this bound and \(P_0(r)\) at \(r=0.42\).

**6.3** (medium). Show that \(G(q)\to1\) as \(q\to-\infty\), using \(\lambda(q)=-q+1/(-q)+O(|q|^{-3})\).

**6.4** (easy). Show that \(\mathbb EW=\int_0^\infty\Pr\{W\ge u\}\,du\) for a nonnegative random variable \(W\).

## 7. Solutions

**6.1.** \(K+uh=\{x:\langle e,x\rangle\ge cu\}\), whose measure is \(\Phi(-cu)\). Here \(\gamma_d(K)=\frac12\), \(q=0\), and \(\int_Kx\,d\gamma_d=\phi(0)e\) gives \(p'(0)=-\langle h,\phi(0)e\rangle=-c\phi(0)\); the tangent bound is \(\Phi(0-c\phi(0)u/\phi(0))=\Phi(-cu)\), the exact value.

**6.2.** The tangent line of \(\log p_i\) at \(0\) has slope \(p_i'(0)/P_i=-1/(\alpha P_i)\), so \(p_i(u)\le P_ie^{-u/(\alpha P_i)}\) and \(\int_0^\infty p_i\le\alpha P_i^2\). With Lemma 1.1, \(\alpha P_i^2\ge C\alpha r_i^2/(1+\sqrt{1-\alpha r_i^2})\), so \(P_i^2>B^2r_i^2/(1+\sqrt{1-r_i^2})\). At \(r=0.42\) this gives only \(P>0.18197\), whereas \(P_0(0.42)=0.20076\). The difference matters: [Five or more cells and the propeller bound](five-or-more-cells-and-the-propeller-bound.md) uses the excess of \(P_0(0.42)\) over \(Ar^2\) with a margin of less than \(0.003\).

**6.3.** \(G=\lambda(q+\lambda)\). With \(\lambda=-q+1/(-q)+O(|q|^{-3})\), \(q+\lambda=1/(-q)+O(|q|^{-3})\), and \(\lambda(q+\lambda)=1+O(q^{-2})\). (The expansion of \(\lambda\) follows from the asymptotic series of \(\Phi(q)/\phi(q)\) as \(q\to-\infty\), obtained by integrating by parts twice.)

**6.4.** \(W=\int_0^\infty\mathbf 1_{\{W\ge u\}}\,du\) pointwise; take expectations and exchange the integrals by Fubini's theorem for nonnegative functions.

## References

- [OpenAI-GP] OpenAI, *The Gaussian propeller bound in every dimension*, OpenAI Math Release preprint, 24 September 2026, Section 3. https://github.com/openai/math/tree/main/preprints/The-Gaussian-Propeller-Bound-in-Every-Dimension-September-24-2026
- [Ehrhard] A. Ehrhard, *Symétrisation dans l'espace de Gauss*, Mathematica Scandinavica 53 (1983), 281–301. https://journals.msp.org/mscand/article/view/1636
- [vH] R. van Handel, *The Borell–Ehrhard game*, Probability Theory and Related Fields 170 (2018), 555–585; arXiv:1605.00285. https://arxiv.org/abs/1605.00285
- [NP] J. Neeman and G. Paouris, *An interpolation proof of Ehrhard's inequality*, arXiv:1605.07233. https://arxiv.org/abs/1605.07233
- [Fremlin] D. H. Fremlin, *Measure Theory*, Volumes 1 and 2, author's edition, the basis of the core course [Measure and Integration](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D10). https://www1.essex.ac.uk/maths/people/fremlin/mt.htm
