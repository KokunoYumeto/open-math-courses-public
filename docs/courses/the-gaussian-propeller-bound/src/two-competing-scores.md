# Two competing scores

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

We continue in the standing setting (S1)–(S6) of Gaussian first moments of partitions, Section 4. The bounds of [Rearrangement bounds for one cell](rearrangement-bounds-for-one-cell.md) and [Ehrhard concavity and the loss of one score](ehrhard-concavity-and-the-loss-of-one-score.md) concern one cell at a time. This lesson looks at the cell with the shortest moment and uses its moment identity to constrain how the other scores are correlated. The result is Corollary 3.1: two inequalities between the three largest normalized lengths and the smallest one.

Relabel the cells so that
\[
\begin{gathered}
r_1\ge r_2\ge\dots\ge r_m=t>0,\\
L=r_1^2+r_2^2,\qquad c=r_3^2 .
\end{gathered}
\]
Since \(m\ge5\), the indices \(1,2,3\) and \(m\) are distinct, also when some lengths coincide.

## 1. Residual scores

Let \(g\) be standard Gaussian in \(V\) and put
\[
\begin{gathered}
e=\frac{z_m}{|z_m|},\qquad T=\langle e,g\rangle,\\
a_j=-\frac{\langle z_m,z_j\rangle}{|z_m|^2}\quad(j<m).
\end{gathered}
\]
By (S2), \(a_j>0\), and \(\sum_{j<m}a_j=-\langle z_m,\sum_{j<m}z_j\rangle/|z_m|^2=1\). Define the *residual vectors* and *residual scores*
\[
\begin{gathered}
w_j=\frac{z_j}{\sqrt C}+a_jt\,e,\\
Y_j=\langle w_j,g\rangle\qquad(j<m).
\end{gathered}
\]

**Lemma 1.1.** (a) Each \(w_j\) is orthogonal to \(e\), and \(\sum_{j<m}w_j=0\).
(b) The vector \(Y=(Y_j)_{j<m}\) is centered Gaussian and independent of the standard normal variable \(T\), and
\[
\frac{X_j}{\sqrt C}=Y_j-a_jtT\qquad(j<m).
\]
(c) The covariances \(H_{jk}=\mathbb EY_jY_k=\langle w_j,w_k\rangle\) are
\[
\begin{gathered}
H_{jk}=\frac{\langle z_j,z_k\rangle}C-a_ja_kt^2,\\
h_j:=H_{jj}=r_j^2-a_j^2t^2 .
\end{gathered}
\]
Every row of \(H\) sums to zero, and \(H_{jk}<0\) for \(j\ne k\).
(d) For distinct \(j,k<m\), \(D_{jk}=\sqrt{h_jh_k-H_{jk}^2}\) is positive. In particular every \(h_j\) is positive.

**Proof.** (a) Since \(t=|z_m|/\sqrt C\), \(\langle z_j,z_m\rangle/(\sqrt C|z_m|)=-a_jt\), so \(\langle w_j,e\rangle=-a_jt+a_jt=0\). Also \(\sum_{j<m}w_j=-z_m/\sqrt C+te=0\).

(b) In an orthonormal basis of \(V\) whose first vector is \(e\), \(T\) is the first coordinate of \(g\) and each \(Y_j\) is a linear function of the other coordinates, which are independent of the first (product rule, Gaussian first moments of partitions, Section 1). The identity follows from \(z_j/\sqrt C=w_j-a_jte\).

(c) Expand \(\langle w_j,w_k\rangle\) and use \(\langle e,z_k\rangle/\sqrt C=-a_kt\). The row sums vanish by (a). For \(j\ne k\) both terms of \(H_{jk}\) are negative by (S2).

(d) \(D_{jk}^2\) is the Gram determinant of \(w_j\) and \(w_k\), which vanishes only if they are linearly dependent. A relation \(\beta w_j+\beta'w_k=0\) is a relation among \(z_j,z_k,z_m\), a proper subset of the moments because \(m\ge5\); by (S3) it is trivial. \(\square\)

## 2. A pair bound

**Lemma 2.1.** For distinct \(j,k<m\),
\[
D_{jk}<\frac3\pi\,t\,(1+a_j)(1+a_k).
\]

**Proof.** Let \(K=K_m\) be the cone of the shortest moment. By (S4), \(\mathbb E[\mathbf 1_Kg]=z_m\), so
\[
\begin{gathered}
\mathbb E[\mathbf 1_KT]=|z_m|=\sqrt C\,t>Bt,\\
\mathbb E[\mathbf 1_KY_j]=\langle w_j,z_m\rangle=0 .
\end{gathered}
\]
On \(K\) the score \(X_m=|z_m|T\) is the largest, hence nonnegative by (S5), so \(T\ge0\); and \(X_j\le X_m\) gives \(Y_j-a_jtT\le tT\), that is, \(Y_j\le(1+a_j)tT\).

Fix \(j\ne k\) and put
\[
U=\frac{Y_j}{(1+a_j)t},\qquad W=\frac{Y_k}{(1+a_k)t}.
\]
The pair \((U,W)\) is centered Gaussian with covariance determinant \(D_{jk}^2/\bigl((1+a_j)^2(1+a_k)^2t^4\bigr)\), so its density is bounded by
\[
M=\frac{t^2(1+a_j)(1+a_k)}{2\pi D_{jk}} .
\]
Let \(\mathcal E\) be the event that \(T\ge0\), \(U\le T\) and \(W\le T\); it contains the event \(\{g\in K\}\). Adding the two zero expectations, taking a positive part and enlarging the region of integration to \(\mathcal E\),
\[
\begin{aligned}
\mathbb E[\mathbf 1_KT]&=\mathbb E[\mathbf 1_K(T+U+W)]\\
&\le\mathbb E\bigl[\mathbf 1_{\mathcal E}(T+U+W)_+\bigr].
\end{aligned}
\]
Condition on \(T=s\ge0\); the pair \((U,W)\) is independent of \(T\). With \(a=s-u\) and \(b=s-w\),
\[
\begin{aligned}
&\iint_{u\le s,\,w\le s}(s+u+w)_+\,du\,dw\\
&\quad=\int_0^\infty\!\!\int_0^\infty(3s-a-b)_+\,db\,da\\
&\quad=\int_0^{3s}\frac{(3s-a)^2}2\,da=\frac{(3s)^3}6 .
\end{aligned}
\]
The integrand is supported on the triangle with vertices \((s,s)\), \((s,-2s)\), \((-2s,s)\). Bounding the density by \(M\) and using \(\mathbb ET_+^3=\int_0^\infty s^3\phi(s)\,ds=2/\sqrt{2\pi}\),
\[
\begin{aligned}
Bt<\mathbb E[\mathbf 1_KT]&\le\frac{27M}6\cdot\frac2{\sqrt{2\pi}}\\
&=\frac{9t^2(1+a_j)(1+a_k)}{2\pi\sqrt{2\pi}\,D_{jk}} .
\end{aligned}
\]
Since \(B=3/(2\sqrt{2\pi})\), this is the claim. \(\square\)

The negative correlations of the residual scores prevent all pairwise determinants from being small at once; summing the pair bound over pairs among the three longest moments gives the constraints.

## 3. Two constraints

**Corollary 3.1.** The numbers \(L\), \(c\) and \(t\) satisfy the inequalities (C1), on the first line, and (C2), on the second:
\[
\begin{aligned}
(c-t^2)(L-c-2t^2)&\le8(3/\pi)^2t^2,\\
\tfrac32(c-t^2)^2&\le10(3/\pi)^2t^2.
\end{aligned}
\]

**Proof.** First, \(c\ge t^2\) by the ordering, and since \(0<a_j\le1\),
\[
h_j=r_j^2-a_j^2t^2\ge c-t^2\ge0\qquad(j\le3).
\]

(C1). Row 3 of \(H\) sums to zero and its off-diagonal entries are negative, so \(h_3=\sum_{k\ne3}|H_{3k}|\ge|H_{31}|+|H_{32}|\), and \(H_{31}^2+H_{32}^2\le(|H_{31}|+|H_{32}|)^2\le h_3^2\). Hence
\[
\begin{aligned}
&D_{31}^2+D_{32}^2\\
&\quad=h_3(h_1+h_2)-H_{31}^2-H_{32}^2\\
&\quad\ge h_3(h_1+h_2-h_3).
\end{aligned}
\]
Here \(h_3\ge c-t^2\ge0\) and
\[
\begin{aligned}
&h_1+h_2-h_3\\
&\quad=L-c-(a_1^2+a_2^2-a_3^2)t^2\\
&\quad\ge L-c-2t^2 .
\end{aligned}
\]
If \(L-c-2t^2\ge0\), then \(D_{31}^2+D_{32}^2\ge(c-t^2)(L-c-2t^2)\); otherwise this holds because the right side is at most zero. On the other side, Lemma 2.1 gives
\[
\begin{aligned}
&D_{31}^2+D_{32}^2\le\Bigl(\frac3\pi\Bigr)^2t^2(1+a_3)^2\\
&\qquad\cdot\bigl((1+a_1)^2+(1+a_2)^2\bigr).
\end{aligned}
\]
With \(\sigma=1-a_3\ge a_1+a_2\) and \(a_1^2+a_2^2\le(a_1+a_2)^2\),
\[
\begin{aligned}
(1+a_1)^2+(1+a_2)^2&\le2+2\sigma+\sigma^2\\
&=(2-a_3)^2+1 .
\end{aligned}
\]
For \(0\le x\le1\) the identity
\[
\begin{aligned}
&8-(1+x)^2\bigl((2-x)^2+1\bigr)\\
&\quad=(1-x)^2(3-x^2)\ge0
\end{aligned}
\]
then bounds \((1+a_3)^2((2-a_3)^2+1)\) by \(8\), which proves (C1).

(C2). Let \(\rho_{jk}=H_{jk}/\sqrt{h_jh_k}\) for \(1\le j<k\le3\); these correlations lie in \([-1,0]\). Since
\[
0\le\operatorname{Var}\Bigl(\sum_{j=1}^3\frac{Y_j}{\sqrt{h_j}}\Bigr)=3+2\sum_{j<k\le3}\rho_{jk},
\]
we get \(\sum_{j<k\le3}\rho_{jk}^2\le\sum_{j<k\le3}|\rho_{jk}|\le\frac32\), and therefore
\[
\begin{aligned}
\sum_{j<k\le3}D_{jk}^2&=\sum_{j<k\le3}h_jh_k(1-\rho_{jk}^2)\\
&\ge(c-t^2)^2\Bigl(3-\frac32\Bigr).
\end{aligned}
\]
On the other side, by Lemma 2.1, \(\sum_{j<k\le3}D_{jk}^2\) is at most \((3/\pi)^2t^2\) times \(\sum_{j<k\le3}(1+a_j)^2(1+a_k)^2\). With the elementary symmetric functions \(s_1,s_2,s_3\) of \(a_1,a_2,a_3\),
\[
\begin{aligned}
&\sum_{j<k\le3}(1+a_j)^2(1+a_k)^2\\
&\quad=3+4s_1+2s_1^2+2s_1s_2+s_2^2\\
&\qquad-(6+2s_1)s_3 .
\end{aligned}
\]
Since \(0\le s_1\le1\) (the \(a_j\) are positive with total \(1\)), \(0\le s_2\le s_1^2/3\le\frac13\) and \(s_3\ge0\), the sum is at most \(3+4+2+\frac23+\frac19=\frac{88}9<10\). This proves (C2). \(\square\)

## 4. Exercises

**4.1** (easy). Show that a centered Gaussian vector in \(\mathbb R^2\) with covariance matrix \(\Sigma\), \(\det\Sigma>0\), has density at most \(1/(2\pi\sqrt{\det\Sigma})\).

**4.2** (easy). Verify the expansion of \(\sum_{j<k\le3}(1+a_j)^2(1+a_k)^2\) in terms of \(s_1,s_2,s_3\) at \(a_1=a_2=a_3=\frac13\).

**4.3** (medium). Show that \(s_2\le s_1^2/3\) for real \(a_1,a_2,a_3\).

**4.4** (medium). For the three moments of the propeller (\(m=3\)), compute the coefficients \(a_1,a_2\) relative to \(z_3\), and the residual vectors \(w_1,w_2\). Why does the argument of Lemma 2.1 need two residual scores, and hence \(m\ge4\)?

## 5. Solutions

**4.1.** The density is \((2\pi)^{-1}(\det\Sigma)^{-1/2}\exp(-\frac12y^{\mathsf T}\Sigma^{-1}y)\), and the exponential is at most one.

**4.2.** Each product \((1+a_j)^2(1+a_k)^2\) equals \((4/3)^4=256/81\), so the sum is \(3\cdot256/81=256/27\). With \(s_1=1\), \(s_2=\frac13\) and \(s_3=\frac1{27}\), the expansion gives \(3+4+2+\frac23+\frac19-\frac8{27}\), which is \(9+\frac{13}{27}=\frac{256}{27}\).

**4.3.**
\[
\begin{aligned}
&s_1^2-3s_2\\
&\quad=a_1^2+a_2^2+a_3^2\\
&\qquad-a_1a_2-a_1a_3-a_2a_3\\
&\quad=\frac12\sum_{j<k}(a_j-a_k)^2\ge0 .
\end{aligned}
\]

**4.4.** The propeller moments have equal lengths and pairwise angles \(2\pi/3\), so \(a_1=a_2=\frac12\). Then \(w_1=-w_2\) are orthogonal to \(z_3\): with \(m=3\) there is only one independent residual score, \(Y_2=-Y_1\), and the determinant \(D_{12}\) vanishes. The argument needs two linearly independent residual vectors, which (S3) provides when \(m\ge4\).

## References

- [OpenAI-GP] OpenAI, *The Gaussian propeller bound in every dimension*, OpenAI Math Release preprint, 24 September 2026, Section 4. https://github.com/openai/math/tree/main/preprints/The-Gaussian-Propeller-Bound-in-Every-Dimension-September-24-2026
