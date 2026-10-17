# A product of two simplices

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Two facts combine here. The functional \(R\) is multiplicative on products (Proposition 4.1 of [Projection bodies of polytopes](projection-bodies-of-polytopes.md)), and every \(d\)-dimensional simplex has the value \(c_d=(d+1)d^d/d!\) (Proposition 2.2 of [The simplex value](the-simplex-value.md)). So a product of simplices of dimensions \(r\) and \(s\) has the value \(c_rc_s\), to be compared with \(c_{r+s}\). This lesson proves Theorems A and B of OpenAI [OpenAI-PB, Section 4], and shows that dimension twenty is the first in which a product of simplices exceeds the simplex value.

Products of simplices are not the only counterexamples to the simplex bound: Feng, Hu, Liu and Xu constructed polytopes with \(R_d>c_d\) in every dimension \(d\ge9\) [FHLX, Theorem 1.3]. The product construction gives an exact value and, iterated, an exponential excess.

## 1. The counterexample in dimension twenty

*Proof of Theorem A.* \(K=T_{10}\times T_{10}\) is a polytope in \(\mathbb R^{20}\), and by the product formula and the simplex value
\[
\begin{aligned}
R_{20}(K)&=R_{10}(T_{10})^2=c_{10}^2\\
&=\Bigl(\frac{11\cdot10^{10}}{10!}\Bigr)^2 .
\end{aligned}
\]
Since \(c_{20}=21\cdot20^{20}/20!\),
\[
\begin{aligned}
\frac{R_{20}(K)}{c_{20}}&=\frac{121\cdot10^{20}\cdot20!}{(10!)^2\cdot21\cdot20^{20}}\\
&=\frac{121\binom{20}{10}}{21\cdot2^{20}}=\frac{22\,355\,476}{22\,020\,096},
\end{aligned}
\]
with \(\binom{20}{10}=184\,756\) and \(2^{20}=1\,048\,576\). The ratio exceeds \(1\) because
\[
\begin{gathered}
121\cdot184\,756-21\cdot1\,048\,576\\
=335\,380>0 .\qquad\square
\end{gathered}
\]

## 2. The product test

For \(r,s\ge2\) put
\[
\rho(r,s)=\frac{R_{r+s}(T_r\times T_s)}{c_{r+s}}=\frac{c_rc_s}{c_{r+s}} .
\]

**Proposition 2.1** (OpenAI). For \(r,s\ge2\), with \(n=r+s\),
\[
\rho(r,s)=\frac{(r+1)(s+1)}{n+1}\binom nr\frac{r^rs^s}{n^n} .
\]

*Proof.* \(\frac{c_rc_s}{c_n}=\frac{(r+1)r^r}{r!}\cdot\frac{(s+1)s^s}{s!}\cdot\frac{n!}{(n+1)n^n}\), and \(\frac{n!}{r!\,s!}=\binom nr\). \(\square\)

So every upper bound for \(R_n\) valid for all convex bodies in \(\mathbb R^n\) is at least \(c_rc_s\) for every split \(n=r+s\) with \(r,s\ge2\).

**Proposition 2.2.** If \(r,s\ge2\) and \(r+s\le19\), then \(\rho(r,s)<1\). Consequently, for \(n\le19\), every Cartesian product of at least two simplices of dimensions \(\ge2\) and total dimension \(n\) has \(R_n<c_n\). In dimension \(20\), \(\rho(10,10)>1\).

*Proof.* There are \(72\) pairs \(2\le r\le s\) with \(r+s\le19\), and \(\rho(r,s)=\rho(s,r)\). Evaluating the rational numbers of Proposition 2.1 exactly, the largest value for each \(n=r+s\) is attained at the most balanced split:

| \(n\) | split | largest \(\rho\) |
|---|---|---|
| 4, 5, 6, 7 | 2+2, 3+2, 3+3, 4+3 | 0.675, 0.691, 0.714, 0.734 |
| 8, 9, 10, 11 | 4+4, 5+4, 5+5, 6+5 | 0.760, 0.781, 0.805, 0.826 |
| 12, 13, 14, 15 | 6+6, 7+6, 7+7, 8+7 | 0.850, 0.871, 0.894, 0.914 |
| 16, 17, 18, 19 | 8+8, 9+8, 9+9, 10+9 | 0.936, 0.955, 0.976, 0.995 |
| 20 | 10+10 | 1.015 |

All values for \(n\le19\) are below \(1\). For a product of \(k\ge3\) simplices of dimensions \(p_1,\dots,p_k\ge2\) with \(p_1+\dots+p_k=n\le19\), the product formula gives \(R_n=c_{p_1}\cdots c_{p_k}\), and replacing \(c_{p_1}c_{p_2}\) by the larger number \(c_{p_1+p_2}\) reduces the number of factors; after \(k-1\) such steps the value \(c_n\) is reached, and each step increased the product strictly. The value at \(n=20\) is Theorem A. \(\square\)

Products with a factor of dimension one are not covered by Proposition 4.1 as stated, which assumes \(r,s\ge2\).

## 3. An exponential excess

*Proof of Theorem B.* Put \(\beta=\frac{11}4\). Since \(\frac1{(j+1)!}<\frac13\cdot\frac1{j!}\) for \(j\ge3\),
\[
\begin{aligned}
e&=\frac52+\sum_{j\ge3}\frac1{j!}<\frac52+\frac16\sum_{i\ge0}3^{-i}\\
&=\frac52+\frac14=\beta .
\end{aligned}
\]
The term \(n^n/n!\) is one of the positive terms of the series of \(e^n\), so, for \(n\ge2\),
\[
c_n<(n+1)e^n<(n+1)\beta^n .
\]
Exact arithmetic gives \(c_{10}=\frac{17\,187\,500}{567}\) and
\[
A=\frac{c_{10}}{\beta^{10}}=\frac{1\,638\,400\,000\,000}{1\,336\,956\,340\,797}>1 .
\]
Fix \(\lambda\) with \(1<\lambda<A^{1/10}\). Every \(n\ge20\) is uniquely \(n=10k+d\) with \(k\ge1\) and \(10\le d\le19\); let
\[
K_n=T_{10}^{\,k}\times T_d ,
\]
the product of \(k\) copies of \(T_{10}\) and one \(T_d\). All factors have dimension at least two, so the product formula, applied \(k\) times, and the simplex value give \(R_n(K_n)=c_{10}^kc_d\). Hence
\[
\begin{aligned}
\frac{R_n(K_n)}{c_n\lambda^n}&>\frac{c_{10}^kc_d}{(n+1)\beta^n\lambda^n}\\
&=\frac{c_d}{(\beta\lambda)^d}\cdot\frac{(A/\lambda^{10})^k}{10k+d+1} .
\end{aligned}
\]
For each of the ten values of \(d\), the right side tends to infinity as \(k\to\infty\), since \(A/\lambda^{10}>1\); so it is at least \(1\) for all \(k\ge k_d\). Then \(N=\max_d(10k_d+d)\) has the required property. \(\square\)

## 4. Exercises

**4.1** (easy). Compute \(\rho(2,2)\) and \(\rho(3,3)\).

**4.2** (medium). Using Stirling's formula in the form \(m!=\sqrt{2\pi m}\,(m/e)^m(1+o(1))\), show that \(\rho(m,m)\) grows like a constant times \(\sqrt m\), so that \(\rho(m,m)>1\) for all large \(m\).

**4.3** (easy). Show that \(K_n\) in the proof of Theorem B is a polytope whose number of facets is \(11k+d+1\).

## 5. Solutions

**4.1.** \(\rho(2,2)=c_2^2/c_4=36\cdot\frac3{160}=\frac{27}{40}\), and \(\rho(3,3)=c_3^2/c_6=324/c_6\) with \(c_6=\frac{7\cdot6^6}{6!}=\frac{2268}5\), so \(\rho(3,3)=\frac{1620}{2268}=\frac57\).

**4.2.** With \(n=2m\), \(\binom{2m}m\frac{m^{2m}}{(2m)^{2m}}=\binom{2m}m4^{-m}=\frac{1+o(1)}{\sqrt{\pi m}}\) by Stirling's formula, and \(\frac{(m+1)^2}{2m+1}=\frac m2(1+o(1))\). So \(\rho(m,m)=\frac{\sqrt m}{2\sqrt\pi}(1+o(1))\).

**4.3.** A product of polytopes is described by the inequalities of its factors (proof of Proposition 4.1 of [Projection bodies of polytopes](projection-bodies-of-polytopes.md)), and \(T_p\) has \(p+1\) facets (Lemma 1.2 of [The simplex value](the-simplex-value.md)); so \(K_n\) has \(11k+(d+1)\) facets.

## References

- [OpenAI-PB] OpenAI, *A product counterexample to the simplex maximum for projection-body volume*, OpenAI Math Release preprint, 24 September 2026, Section 4. https://github.com/openai/math/tree/main/preprints/A-product-counterexample-to-the-simplex-maximum-for-projection-body-volume-September-24-2026
- [FHLX] Y. Feng, S. Hu, W. Liu and L. Xu, *On the reverse projection inequality*, preprint, 2026, MathSciDoc 2608.23002; Theorem 1.3 and Section 4. https://archive.ymsc.tsinghua.edu.cn/pacm_download/743/12781--2026.8.26.pdf
