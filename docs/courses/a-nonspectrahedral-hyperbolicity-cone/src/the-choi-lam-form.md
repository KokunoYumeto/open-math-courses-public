# The Choi–Lam form

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The polynomial of Theorem A in [Hyperbolic polynomials and spectrahedral cones](hyperbolic-polynomials-and-spectrahedral-cones.md) is built from the biquadratic form
\[
\begin{aligned}
b(z,y)={}&\sum_{i=1}^3z_i^2y_i^2-2\sum_{i<j}z_iy_iz_jy_j\\
&+\sum_{i=1}^3z_i^2y_{i+1}^2\qquad(z,y\in\mathbf R^3),
\end{aligned}
\]
with indices read modulo \(3\). Choi found the first nonnegative biquadratic form that is not a sum of squares of bilinear forms, with coefficient \(2\) in place of \(1\) in the last sum, and Choi and Lam showed that the form with coefficient \(1\) is extremal among nonnegative biquadratic forms. The proof of Theorem A needs one consequence of that extremality, proved directly in this lesson following OpenAI [OpenAI-NS, Section 2]: no nonzero bilinear form has its square below \(b\). Blekherman, Raiță, Shankar and Sinn call this property *weak extremality* [BRSS].

## 1. Nonnegativity

**Lemma 2.1** (principal minors). A matrix \(M\in\mathbb S^n\) all of whose principal minors are nonnegative is positive semidefinite.

*Proof.* Expanding the determinant, \(\det(tI+M)=\sum_{k=0}^nc_kt^{n-k}\), where \(c_0=1\) and \(c_k\) is the sum of the principal minors of \(M\) of order \(k\). So \(\det(tI+M)>0\) for \(t>0\), and \(-t\) is not an eigenvalue of \(M\). The eigenvalues are real and therefore nonnegative, and Lemma 1.3(1) of the previous lesson applies. \(\square\)

**Lemma 2.2.** The form \(b\) is nonnegative and \(b(e_1,e_1)=1\), where \(e_1,e_2,e_3\) are the standard unit vectors.

*Proof.* Put \(a_i=z_i^2\). As a quadratic form in \(y\), \(b(z,y)=y^{\mathsf T}M(z)y\), where \(M(z)\) is the matrix
\[
\begin{pmatrix}a_1+a_3&-z_1z_2&-z_1z_3\\ -z_1z_2&a_2+a_1&-z_2z_3\\ -z_1z_3&-z_2z_3&a_3+a_2\end{pmatrix}.
\]
Indeed, the coefficient of \(y_j^2\) collects \(z_j^2y_j^2\) and \(z_{j-1}^2y_j^2\). The diagonal entries are nonnegative. The principal minors of order two are
\[
\begin{aligned}
&(a_i+a_{i-1})(a_{i+1}+a_i)-a_ia_{i+1}\\
&\quad=a_i^2+a_{i-1}(a_i+a_{i+1})\ge0 .
\end{aligned}
\]
The determinant is
\[
\begin{aligned}
\det M(z)={}&a_1^2a_2+a_2^2a_3+a_3^2a_1\\
&-3a_1a_2a_3 .
\end{aligned}
\]
It is nonnegative by the inequality between the arithmetic and geometric means of the three numbers \(a_1^2a_2,\ a_2^2a_3,\ a_3^2a_1\), whose product is \((a_1a_2a_3)^3\). In detail, for \(u,v,w\ge0\),
\[
\begin{aligned}
&u^3+v^3+w^3-3uvw\\
&\quad=\tfrac12(u+v+w)\bigl((u-v)^2\\
&\qquad+(v-w)^2+(w-u)^2\bigr)\ge0,
\end{aligned}
\]
applied to the cube roots of the three numbers. By Lemma 2.1, \(M(z)\succeq0\), so \(b\ge0\). Finally \(b(e_1,e_1)=1\). \(\square\)

## 2. No dominated bilinear square

**Lemma 2.3** (OpenAI). If a bilinear form \(\ell:\mathbf R^3\times\mathbf R^3\to\mathbf R\) satisfies \(\ell(z,y)^2\le b(z,y)\) for all \(z,y\in\mathbf R^3\), then \(\ell=0\).

*Proof.* Write \(\ell(z,y)=\sum_{i,j}c_{ij}z_iy_j\). The bound forces \(\ell\) to vanish at every zero of \(b\). Two families of zeros eliminate the coefficients off the diagonal.

- \(b(e_i,e_{i-1})=0\): the only terms of \(b\) that can be nonzero at \(z=e_i\) are \(z_i^2y_i^2\) and \(z_i^2y_{i+1}^2\), and both vanish at \(y=e_{i-1}\). Hence \(c_{i,i-1}=\ell(e_i,e_{i-1})=0\).
- For every sign vector \(\sigma\in\{-1,1\}^3\), \(b(\sigma,\sigma)=3-6+3=0\). Hence
\[
\begin{aligned}
0&=\ell(\sigma,\sigma)\\
&=\sum_ic_{ii}\\
&\quad+\sum_{i<j}(c_{ij}+c_{ji})\sigma_i\sigma_j .
\end{aligned}
\]
Multiply by \(\sigma_p\sigma_q\), for \(p<q\), and average over the eight sign vectors. The average of \(\sigma_p\sigma_q\) is \(0\), and the average of \(\sigma_p\sigma_q\sigma_i\sigma_j\) is \(1\) if \(\{i,j\}=\{p,q\}\) and \(0\) otherwise. So \(c_{pq}+c_{qp}=0\).

Together, \(c_{ij}=0\) for \(i\ne j\): for each pair \(i\ne j\), one of \(c_{ij},c_{ji}\) has the form \(c_{k,k-1}\), and their sum vanishes. Thus \(\ell(z,y)=\sum_ic_iz_iy_i\) with \(c_i=c_{ii}\).

The diagonal coefficients are eliminated by curves along which \(b\) vanishes to fourth order. For a cyclic index \(i\) and \(s\in\mathbf R\), put \(z=e_i+se_{i-1}\) and \(y=e_{i-1}+se_i\). Then
\[
\begin{aligned}
b(z,y)&=2s^2-2s^2+s^4=s^4,\\
\ell(z,y)&=s\,(c_i+c_{i-1}).
\end{aligned}
\]
Indeed, the first sum of \(b\) gives \(s^2+s^2\), the middle term gives \(-2s^2\), and the last sum gives \(z_{i-1}^2y_i^2=s^4\), the term \(z_i^2y_{i+1}^2\) being zero. The bound gives \((c_i+c_{i-1})^2s^2\le s^4\), so \((c_i+c_{i-1})^2\le s^2\) for \(s\ne0\), and \(c_i+c_{i-1}=0\). The three equations \(c_1+c_3=c_2+c_1=c_3+c_2=0\) force \(c_1=c_2=c_3=0\). \(\square\)

**Corollary 2.4.** The form \(b\) is not a sum of squares of bilinear forms.

*Proof.* If \(b=\sum_k\ell_k^2\), each \(\ell_k^2\le b\), so every \(\ell_k=0\) by Lemma 2.3, and \(b=0\), contradicting \(b(e_1,e_1)=1\). \(\square\)

## 3. Exercises

**2.1** (easy). Show that \(b(z,z)=\frac12\sum_{i<j}(z_i^2-z_j^2)^2\), and find all \(z\) with \(b(z,z)=0\).

**2.2** (easy). Show that the form \(\sum_iz_i^2y_i^2-2\sum_{i<j}z_iy_iz_jy_j\), without the last sum, takes negative values.

**2.3** (medium). Show that \(b\) is invariant under the simultaneous cyclic shift \(z_i\mapsto z_{i+1}\), \(y_i\mapsto y_{i+1}\), and under \((z,y)\mapsto(\sigma\odot z,\sigma\odot y)\) for every sign vector \(\sigma\), where \(\odot\) is the coordinatewise product, but that \(b(z,y)\ne b(y,z)\) in general.

**2.4** (medium). Let \(\ell(z,y)=z_1y_1\). Find \(z,y\) with \(\ell(z,y)^2>b(z,y)\), as Lemma 2.3 predicts.

## 4. Solutions

**2.1.** At \(y=z\), the last sum is \(\sum_iz_i^2z_{i+1}^2=\sum_{i<j}z_i^2z_j^2\), so
\[
\begin{aligned}
b(z,z)&=\sum_iz_i^4-\sum_{i<j}z_i^2z_j^2\\
&=\frac12\sum_{i<j}(z_i^2-z_j^2)^2 .
\end{aligned}
\]
It vanishes exactly when \(z_1^2=z_2^2=z_3^2\), that is, \(z=r\sigma\) with \(r\in\mathbf R\) and \(\sigma\) a sign vector.

**2.2.** At \(z=y=(1,1,1)\) it equals \(3-6=-3\).

**2.3.** The cyclic shift permutes the terms of each of the three sums. A sign vector multiplies \(z_iy_i\) by \(\sigma_i^2=1\) and leaves all squares unchanged. Finally \(b(e_1,e_2)=1\), from the term \(z_1^2y_2^2\), while \(b(e_2,e_1)=0\).

**2.4.** Take \(z=e_1+se_3\) and \(y=e_3+se_1\), the curve of the proof with \(i=1\): \(b=s^4\) and \(\ell=s\), so \(\ell^2>b\) for \(0<|s|<1\).

## References

- [OpenAI-NS] OpenAI, *A nonspectrahedral hyperbolicity cone*, OpenAI Math Release preprint, 24 September 2026, Section 2. https://github.com/openai/math/tree/main/preprints/A-Nonspectrahedral-Hyperbolicity-Cone-September-24-2026
- [BRSS] G. Blekherman, B. Raiță, I. Shankar and R. Sinn, *Weak and strong extremal biquadratics*, arXiv:2204.10625. https://arxiv.org/abs/2204.10625
