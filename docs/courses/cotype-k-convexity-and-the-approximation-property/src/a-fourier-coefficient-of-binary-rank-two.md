# A Fourier coefficient of binary rank two

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Functions on the cube of \(m\times m\) sign matrices have Fourier expansions indexed by binary \(m\times m\) matrices. In the decay theorem, a Fourier coefficient indexed by a binary matrix of rank \(k\) over \(\mathbb F_2\) turns into a Walsh pairing with \(k\) independent factors; the decisive case is \(k\ge2\). This lesson proves a purely scalar statement (Lemma 2.1): an odd bounded function of a sign matrix whose row and column averages reproduce two odd bounded functions with large first-order coefficients must have a coefficient of rank at least two, of a size bounded below in terms of the parameters only.

- Fourier analysis on sign cubes; binary rank (Section 1).
- Chebyshev polynomials (Lemma 1.1).
- The coefficient lemma (Lemma 2.1).

The lesson follows [OpenAI-CC, Section 3]. All ranks are over \(\mathbb F_2\).

## 1. Fourier analysis on sign cubes

For a finite index set \(I\), the functions \(z\mapsto z^P=\prod_{i\in I}z_i^{P_i}\), \(P\in\{0,1\}^I\), on \(\{-1,1\}^I\) are orthonormal for the uniform probability measure: \(\mathbb E_zz^Pz^Q=\mathbb E_zz^{P+Q}\), with \(P+Q\) computed modulo \(2\), and \(\mathbb Ez_i=0\). There are \(2^{|I|}\) of them, so they form a basis. Every \(h\colon\{-1,1\}^I\to\mathbb R\) is
\[
\begin{gathered}
h(z)=\sum_P\widehat h(P)z^P,\\
\widehat h(P)=\mathbb E_zh(z)z^P,
\end{gathered}
\]
and Parseval's identity \(\sum_P\widehat h(P)^2=\mathbb Eh^2\) holds. We use \(I=\{1,\dots,m\}\), with indices \(p\in\{0,1\}^m\), \(|p|\) the number of ones and \(e_i\) the unit vectors, and \(I=\{1,\dots,m\}^2\), with indices binary matrices \(P\) and sign matrices \(S\), so that \(S^P=\prod_{i,j}S_{ij}^{P_{ij}}\).

The *odd part* of \(h\) is \(\mathcal Oh(z)=\frac12(h(z)-h(-z))\), and \(h\) is *odd* if \(\mathcal Oh=h\). Since \((-z)^P=(-1)^{|P|}z^P\), \(\mathcal Oh\) keeps exactly the coefficients with \(|P|\) odd.

For a sign vector \(\sigma\), \(\sigma S\) multiplies row \(i\) of \(S\) by \(\sigma_i\), and \(S\tau\) multiplies column \(j\) by \(\tau_j\). Row \(i\) and column \(j\) of \(S\) are \(S_{i,:}\) and \(S_{:,j}\).

The *binary rank* of a binary matrix is its rank over \(\mathbb F_2\). A binary matrix of rank one is \(ph^{\mathrm t}\) with nonzero \(p,h\in\{0,1\}^m\), uniquely: \(p\) marks the nonzero rows and \(h\) is the common nonzero row. If \(u_i,v_j\in\mathbb F_2^n\) and \(S_{ij}=\chi(u_i,v_j)\), then
\[
S^P=(-1)^{\sum_{i,j}P_{ij}\,u_i\cdot v_j}.
\]
For example, the all-ones \(3\times3\) matrix \(P_1\) has rank one and \(S^{P_1}=\chi(u_1+u_2+u_3,v_1+v_2+v_3)\), a single Walsh factor, while
\[
P_2=\begin{pmatrix}1&1&0\\0&1&0\\0&0&0\end{pmatrix}
\]
has rank two and \(S^{P_2}=\chi(u_1,v_1+v_2)\,\chi(u_2,v_2)\), two factors in which \(v_1+v_2\) and \(v_2\) vary independently.

**Lemma 1.1** (Chebyshev polynomials). There are real polynomials \(T_j\) of degree \(j\) with \(T_j(\cos\theta)=\cos(j\theta)\). Every real polynomial \(Q\) of degree at most \(d\) is \(Q=\sum_{j=0}^dc_jT_j\) with \(|c_j|\le2\|Q\|_\infty\), where \(\|\cdot\|_\infty\) is the supremum on \([-1,1]\). Moreover \(|T_j|\le1\) on \([-1,1]\), \(|T_j'(0)|\le j\), and
\[
|Q'(0)|\le d(d+1)\|Q\|_\infty . \tag{1.1}
\]

*Proof.* Put \(T_0=1\), \(T_1(x)=x\) and \(T_{j+1}=2xT_j-T_{j-1}\); the identity
\[
\begin{aligned}
\cos((j+1)\theta)&+\cos((j-1)\theta)\\
&=2\cos\theta\cos(j\theta)
\end{aligned}
\]
gives \(T_j(\cos\theta)=\cos(j\theta)\) by induction, and \(T_j\) has degree \(j\) with leading coefficient \(2^{j-1}\) (\(j\ge1\)). So \(T_0,\dots,T_d\) are a basis of the polynomials of degree at most \(d\). The relations \(\int_0^\pi\cos(j\theta)\cos(k\theta)\,d\theta=0\) for \(j\ne k\) give
for \(j\ge1\),
\[
c_j=\frac{2}{\pi}\int_0^\pi Q(\cos\theta)\cos(j\theta)\,d\theta,
\]
and \(c_0\) is the mean of \(Q(\cos\theta)\); so \(|c_j|\le2\|Q\|_\infty\). Clearly \(|T_j|\le1\). Differentiating \(T_j(\cos\theta)=\cos(j\theta)\) at \(\theta=\pi/2\) gives \(T_j'(0)=j\sin(j\pi/2)\). Finally \(|Q'(0)|\le\sum_{j\le d}2\|Q\|_\infty\,j\), which is \(d(d+1)\|Q\|_\infty\). \(\blacksquare\)

## 2. The coefficient lemma

**Lemma 2.1** ([OpenAI-CC, Lemma 3.1]). Let \(M_0=4\), let \(m\) be an integer with
\[
4\le d=\lceil2\log_2m\rceil<m,
\]
let \(a,b>0\), and put \(A=ma\) and \(B=mb\). Assume
\[
\begin{aligned}
&\min(A,B)\\
&\quad\ge20M_0d(d+1)^2 .
\end{aligned} \tag{2.1}
\]
There is \(c_*>0\), depending only on \(m,a,b\), with the following property. Let \(\Psi\colon\{-1,1\}^{m\times m}\to\mathbb R\) and \(f,g\colon\{-1,1\}^m\to\mathbb R\) be odd, with sup norms at most \(M_0\), such that \(\widehat f(e_i)=a\) and \(\widehat g(e_j)=b\) for all \(i,j\), and
\[
\begin{gathered}
\mathbb E_\sigma\sigma_i\Psi(\sigma S)=a\,g(S_{i,:}),\\
\mathbb E_\tau\tau_j\Psi(S\tau)=b\,f(S_{:,j})
\end{gathered} \tag{2.2}
\]
for all \(i,j\) and \(S\). Then \(|\widehat\Psi(P)|\ge c_*\) for some binary matrix \(P\) of rank at least two.

*Proof.* *Reduction to nonvanishing.* The admissible triples \((\Psi,f,g)\) form a compact set in a finite-dimensional space: the conditions are closed (oddness and the identities are linear equations, and the sup norm bounds are closed). The function \((\Psi,f,g)\mapsto\max_{\operatorname{rank}P\ge2}|\widehat\Psi(P)|\) is continuous. If it never vanishes on the admissible set, its minimum there is a positive \(c_*\); if the set is empty, any \(c_*\) works. So suppose, to reach a contradiction, that \(\widehat\Psi(P)=0\) for every \(P\) of rank at least two.

*Rectangles.* As \(\Psi\) is odd, only indices with \(|P|\) odd occur; in particular \(P\ne0\). So every index in the support of \(\widehat\Psi\) is \(ph^{\mathrm t}\) with \(k=|p|\) and \(l=|h|\) odd. Put
\[
C_{kl}=\sum_{|p|=k,\ |h|=l}\widehat\Psi(ph^{\mathrm t}).
\]
By the Cauchy–Schwarz inequality and Parseval's identity,
\[
|C_{kl}|\le M_0\sqrt{\tbinom mk\tbinom ml}. \tag{2.3}
\]

*A damped polynomial.* Let
\[
H(s,u)=\sum_{\substack{1\le k,l\le m\\k,l\text{ odd}}}C_{kl}\,s^ku^l\,2^{-kl}.
\]
For \(s,u\in[-1,1]\), take independent signs \(D_i,E_j,R_{ij}\) with means \(s\), \(u\) and \(1/2\), and put \(S_{ij}=D_iE_jR_{ij}\). For an index \(ph^{\mathrm t}\) with \(k,l\) odd, \(S^{ph^{\mathrm t}}=\prod_{i\in p}D_i^l\prod_{j\in h}E_j^k\prod R_{ij}\), so \(\mathbb ES^{ph^{\mathrm t}}=s^ku^l2^{-kl}\). Hence \(H(s,u)=\mathbb E\Psi(S)\), and \(\|H\|_\infty\le M_0\) on \([-1,1]^2\).

*Deleting the large rectangles.* Let \(H_0\) be \(H\) without the terms with both \(k>d\) and \(l>d\). For such \(k,l\), \(\log_2m\le d/2<\min(k,l)/2\), so \((k+l)\log_2m<kl\); and \(k,l\ge5\) gives \(kl/2\ge k+l\). With (2.3) and \(\binom mk\le m^k\), the deleted part has sup norm at most
\[
\begin{aligned}
&M_0\sum_{k,l>d}m^{(k+l)/2}2^{-kl}\\
&\quad\le M_0\sum_{k,l>d}2^{-kl/2}\\
&\quad\le M_0\sum_{k,l\ge5}2^{-k-l}\le M_0 .
\end{aligned}
\]
So \(\|H_0\|_\infty\le2M_0\).

*The prescribed derivatives.* Substituting the Fourier expansion in (2.2): \(\Psi(\sigma S)=\sum_P\widehat\Psi(P)\sigma^{r(P)}S^P\), where \(r(P)\) is the vector of row parities, so \(\mathbb E_\sigma\sigma_i\Psi(\sigma S)\) keeps the indices with \(r(P)=e_i\). For \(P=ph^{\mathrm t}\) with \(l\) odd, \(r(P)=p\). Comparing coefficients of \(S^{e_ih^{\mathrm t}}=S_{i,:}^h\) gives \(\widehat\Psi(e_ih^{\mathrm t})=a\,\widehat g(h)\), and in the same way \(\widehat\Psi(pe_j^{\mathrm t})=b\,\widehat f(p)\). Hence
\[
\begin{gathered}
C_{1l}=ma\sum_{|h|=l}\widehat g(h),\\
C_{k1}=mb\sum_{|p|=k}\widehat f(p).
\end{gathered}
\]
The deletion did not touch the terms with \(k=1\) or \(l=1\). Put \(\Gamma(u)=\sum_h\widehat g(h)(u/2)^{|h|}\) and \(\Theta(s)=\sum_p\widehat f(p)(s/2)^{|p|}\). Since \(g\) and \(f\) are odd,
\[
\begin{gathered}
\partial_sH_0(0,u)=A\,\Gamma(u),\\
\partial_uH_0(s,0)=B\,\Theta(s),\\
\partial_s\partial_uH_0(0,0)=\tfrac12AB,
\end{gathered} \tag{2.4}
\]
the last because the coefficient of \(su\) is \(\frac12C_{11}\) and \(C_{11}=mb\sum_i\widehat f(e_i)=AB\). Here \(\Gamma(u)=\mathbb Eg(\xi)\) for independent signs \(\xi_j\) of mean \(u/2\), so \(\|\partial_sH_0(0,\cdot)\|_\infty\le AM_0\); likewise \(\|\partial_uH_0(\cdot,0)\|_\infty\le BM_0\).

*Splitting by degree.* Expand \(H_0(s,u)=\sum_jT_j(s)h_j(u)\) in Chebyshev polynomials in \(s\), with polynomial coefficients \(h_j\). Let \(H_1\) keep the terms with \(j\le d\), and \(H_2=H_0-H_1\). Then \(\deg_sH_1\le d\), and \(\deg_uH_2\le d\): the monomials of \(H_0\) with \(s\)-degree at most \(d\) contribute nothing to \(H_2\), and the others have \(u\)-degree at most \(d\). By Lemma 1.1, applied for each fixed \(u\),
\[
\begin{gathered}
\|H_1\|_\infty\le4M_0(d+1),\\
\|H_2\|_\infty\le6M_0(d+1).
\end{gathered}
\]
By (1.1) in \(s\) for \(H_1\) and in \(u\) for \(H_2\), and by (2.4),
\[
\begin{aligned}
\|\partial_sH_2(0,\cdot)\|_\infty&\le AM_0+4M_0d(d+1)^2,\\
\|\partial_uH_1(\cdot,0)\|_\infty&\le BM_0+6M_0d(d+1)^2 .
\end{aligned}
\]
These are polynomials of degree at most \(d\) in \(u\) and in \(s\), respectively. Applying (1.1) once more and adding,
\[
\begin{aligned}
&|\partial_s\partial_uH_0(0,0)|\\
&\quad\le M_0d(d+1)\bigl(A+B\\
&\qquad+10d(d+1)^2\bigr).
\end{aligned} \tag{2.5}
\]

*The contradiction.* By (2.1), \(\frac12AB\ge10M_0d(d+1)^2\max(A,B)\), which is at least \(5M_0d(d+1)^2(A+B)\), and \(10d(d+1)^2\le(A+B)/(4M_0)\). So (2.4) and (2.5) give
\[
\begin{aligned}
&5M_0d(d+1)^2(A+B)\\
&\quad\le M_0d(d+1)(A+B)\bigl(1+\tfrac1{4M_0}\bigr),
\end{aligned}
\]
that is \(5(d+1)\le1+1/(4M_0)\), which is false. \(\blacksquare\)

The constant \(c_*\) comes from compactness and is not explicit.

## 3. Exercises

**3.1.** Show that a binary matrix of rank one is \(ph^{\mathrm t}\) for unique nonzero \(p,h\).

**3.2.** Check the identity \(S^{P_2}=\chi(u_1,v_1+v_2)\chi(u_2,v_2)\) of Section 1.

**3.3.** Show that \(T_2(x)=2x^2-1\), \(T_3(x)=4x^3-3x\), and verify (1.1) for \(Q=T_3\).

**3.4.** Show that the smallest \(m\) with \(4\le\lceil2\log_2m\rceil<m\) is \(m=7\).

**3.5.** Why is the compactness argument needed? What would the proof give without it?

## 4. Solutions

**3.1.** The rows of a rank-one binary matrix are \(0\) or a fixed nonzero row \(h\); \(p\) records which rows are nonzero. Both are determined by the matrix.

**3.2.** \(P_2\) has ones at \((1,1)\), \((1,2)\) and \((2,2)\), so the exponent is \(u_1\cdot v_1+u_1\cdot v_2+u_2\cdot v_2\), which equals \(u_1\cdot(v_1+v_2)+u_2\cdot v_2\).

**3.3.** \(T_2=2x\cdot x-1\) and \(T_3=2x(2x^2-1)-x\). \(T_3'(0)=-3\) and \(\|T_3\|_\infty=1\), while \(d(d+1)=12\).

**3.4.** \(\lceil2\log_2m\rceil\) is \(4,4,5,6,6\) for \(m=3,4,5,6,7\); only \(m=7\) satisfies \(d<m\) among these, and \(d\ge4\) fails for \(m\le2\).

**3.5.** The argument by contradiction shows only that some coefficient of rank at least two is nonzero. A uniform lower bound, needed to iterate in the next lessons, comes from the minimum of a positive continuous function on a compact set.

## References

- [OpenAI-CC] OpenAI, *The cotype–cotype conjecture under the approximation property*, OpenAI Math Release preprint, 23 September 2026, Section 3. https://github.com/openai/math/tree/main/preprints/The-cotype-cotype-conjecture-under-the-approximation-property-September-23-2026
