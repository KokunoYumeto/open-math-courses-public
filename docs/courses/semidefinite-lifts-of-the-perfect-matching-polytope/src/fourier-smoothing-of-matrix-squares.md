# Fourier smoothing of matrix squares

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Let a positive semidefinite matrix-valued function be averaged, coordinate by coordinate, through random channels whose averages have small variance, as in [Averaging within a cell](averaging-within-a-cell.md). This lesson shows that the average can be written as a sum of squares \(\sum_qH_q^{\mathsf T}H_q\) in which the Fourier coefficients of each \(H_q\) concentrate near their own frequency \(q\): frequencies that differ from \(q\) in many coordinate blocks carry exponentially little weight [OpenAI-PSD, Section 4]. The proof processes the coordinates one at a time. Each new average is realized by stacking matrices, and the splitting lemma of [Splitting positive semidefinite matrices](splitting-positive-semidefinite-matrices.md) separates the new frequencies into branches. A fourth-order quantity, the squared Frobenius norm of a weighted Gram matrix, at most doubles at each step.

- Characters of Boolean blocks (Section 1).
- The theorem (Section 2).
- The proof (Section 3).

## 1. Characters of Boolean blocks

Fix an integer \(a\ge1\) and put \(L=2^a\). Let \(Y_1,\ldots,Y_t\) be copies of the group \(\mathbb F_2^a\), and let \(\Lambda=\mathbb F_2^a\) be a further copy, used to index characters. For \(p=(p_1,\ldots,p_t)\in\Lambda^t\) and \(y=(y_1,\ldots,y_t)\in\prod_iY_i\) put
\[
\chi_p(y)=(-1)^{\sum_{i=1}^tp_i\cdot y_i},
\]
where \(p_i\cdot y_i\) is the dot product modulo two. The functions on \(\prod_iY_i\) carry the uniform probability measure, and \(\mathbb E_y\) denotes the average.

**Lemma 1.1.** The characters \(\chi_p\), \(p\in\Lambda^t\), form an orthonormal basis of the real functions on \(\prod_iY_i\). Hence every function \(H\) with values in real matrices of a fixed size satisfies
\[
\begin{gathered}H(y)=\sum_{p\in\Lambda^t}\widehat H_p\,\chi_p(y),\\ \widehat H_p=\mathbb E_y\bigl[\chi_p(y)H(y)\bigr],\end{gathered}
\]
and \(\mathbb E_y\|H(y)\|_{\mathrm F}^2=\sum_p\|\widehat H_p\|_{\mathrm F}^2\).

*Proof.* We have \(\chi_p\chi_{p'}=\chi_{p+p'}\) and \(\chi_p^2=1\). If \(p\ne0\), say \(p_i\) has a nonzero coordinate \(\ell\), then changing the \(\ell\)-th bit of \(y_i\) is a bijection of \(\prod_iY_i\) that reverses the sign of \(\chi_p\), so \(\mathbb E_y\chi_p=0\). Thus \(\mathbb E_y\chi_p\chi_{p'}=1\) if \(p=p'\) and \(0\) otherwise. There are \(L^t\) characters, the dimension of the space, so they form an orthonormal basis. The expansion holds entrywise, and the last identity is Parseval's identity for each entry. \(\square\)

The *block degree* of \(\chi_p\) is \(|p|_{\mathrm{blk}}=|\{i:p_i\ne0\}|\). A function has *block degree at most \(D\)* if its Fourier coefficients vanish at every \(p\) with \(|p|_{\mathrm{blk}}>D\); the zero function qualifies. Put
\[
\operatorname{dist}(p,q)=|\{i:p_i\ne q_i\}|=|p+q|_{\mathrm{blk}} .
\]

**Lemma 1.2** (translation by a character). Let \(q\in\Lambda^t\) and let \(H\) be a matrix-valued function whose coefficients \(\widehat H_p\) vanish whenever \(\operatorname{dist}(p,q)>D\). Then every entry of \(\chi_qH\) has block degree at most \(D\), and \((\chi_qH)^{\mathsf T}(\chi_qH)=H^{\mathsf T}H\).

*Proof.* \(\chi_qH=\sum_p\widehat H_p\chi_{p+q}\), so the coefficient of \(\chi_qH\) at \(p'\) is \(\widehat H_{p'+q}\), which vanishes unless \(|p'|_{\mathrm{blk}}=\operatorname{dist}(p'+q,q)\le D\). The second statement holds because \(\chi_q^2=1\). \(\square\)

The same translation of Fourier supports, which keeps squares unchanged, appears in the construction of sparse sums of squares on finite abelian groups by Fawzi, Saunderson and Parrilo [FSP 2016].

## 2. The theorem

For \(1\le i\le t\), let \(X_i\) and \(\mathcal M_i\) be nonempty finite sets with the uniform probability measures, and let \(Y_i\) be a copy of \(\mathbb F_2^a\) as above. For \(m\in\mathcal M_i\) and \(y\in Y_i\), let \(\pi^m_{i,y}\) be a probability measure on \(X_i\), and for a function \(Z\) on \(X_i\) put
\[
(T_{i,y}Z)(m)=\sum_{x\in X_i}\pi^m_{i,y}(x)Z(x).
\]
Suppose that for some \(\theta\ge0\), for every \(i\), every \(y\in Y_i\) and every real function \(g\) on \(X_i\), with \(m\) uniform in \(\mathcal M_i\),
\[
\begin{gathered}\mathbb E_m\pi^m_{i,y}(x)=\frac1{|X_i|}\\ (x\in X_i),\end{gathered}\tag{2.1}
\]
\[
\begin{aligned}&\mathbb E_m\Bigl((T_{i,y}g)(m)-\mathbb E_xg\Bigr)^2\\&\quad\le\theta\,\mathbb E_xg(x)^2 .\end{aligned}\tag{2.2}
\]
Let \(C_L=2^{L-1}\) be the constant of Theorem 2.1 of [Splitting positive semidefinite matrices](splitting-positive-semidefinite-matrices.md).

**Theorem 2.1** (Fourier smoothing of matrix squares; [OpenAI-PSD, Theorem 4.1]). Let \(r\ge1\) and \(B>0\), and let \(F\colon\prod_iX_i\to\mathbb S^r_+\) satisfy \(\operatorname{tr}F(x)\le B\) for all \(x\). Let \(\lambda>1\) satisfy
\[
L\lambda^2C_L\theta\le1 .
\tag{2.3}
\]
For \(m=(m_1,\ldots,m_t)\in\prod_i\mathcal M_i\) and \(y\in\prod_iY_i\) put
\[
\overline F_m(y)=\sum_{x\in\prod_iX_i}\Bigl(\prod_{i=1}^t\pi^{m_i}_{i,y_i}(x_i)\Bigr)F(x).
\]
There are an integer \(R\) and functions \(H^m_q\colon\prod_iY_i\to\mathbb R^{R\times r}\), for \(m\in\prod_i\mathcal M_i\) and \(q\in\Lambda^t\), such that
\[
\begin{aligned}&\overline F_m(y)\\&\quad=\sum_{q\in\Lambda^t}H^m_q(y)^{\mathsf T}H^m_q(y),\end{aligned}\tag{2.4}
\]
and such that the matrices
\[
\begin{gathered}
U^m_q=\Bigl[\lambda^{\operatorname{dist}(q,p)/2}\,\widehat H^m_{q,p}\Bigr]_{p\in\Lambda^t},\\
C^m_q=U^m_q(U^m_q)^{\mathsf T},
\end{gathered}
\]
where \(\widehat H^m_{q,p}\) is the Fourier coefficient of \(H^m_q\) at \(p\) and the brackets denote the horizontal concatenation over \(p\), satisfy, for independent uniform \(m_i\),
\[
\mathbb E_m\sum_{q\in\Lambda^t}\|C^m_q\|_{\mathrm F}^2\le2^tB^2 .
\tag{2.5}
\]
Consequently, some \(m\) satisfies
\[
\begin{aligned}&\sum_{q,p\in\Lambda^t}\lambda^{\operatorname{dist}(q,p)}\,\|\widehat H^m_{q,p}\|_{\mathrm F}^2\\&\quad\le L^t\sqrt r\,B\,2^{t/2}.\end{aligned}\tag{2.6}
\]

The weights in (2.6) penalize the frequencies of the branch \(H^m_q\) that are far from its center \(q\). To see what (2.5) controls, fix \(m\) and \(q\), suppress them, and put \(w_p=\lambda^{\operatorname{dist}(q,p)}\). Then
\[
\begin{gathered}\operatorname{tr}C=\sum_pw_p\|\widehat H_p\|_{\mathrm F}^2,\\ \|C\|_{\mathrm F}^2=\|U^{\mathsf T}U\|_{\mathrm F}^2\\=\sum_{p,p'}w_pw_{p'}\|\widehat H_p^{\mathsf T}\widehat H_{p'}\|_{\mathrm F}^2 .\end{gathered}
\]
The trace is the weighted Fourier mass to be bounded; the squared Frobenius norm measures the overlaps of the coefficient matrices, and it is this fourth-order quantity that the variance condition (2.2) controls.

## 3. The proof

**Lemma 3.1.** Under (2.2), every function \(Z\) on \(X_i\) with values in real matrices of any fixed size satisfies
\[
\begin{aligned}&\mathbb E_m\bigl\|(T_{i,y}Z)(m)-\mathbb E_xZ\bigr\|_{\mathrm F}^2\\&\quad\le\theta\,\mathbb E_x\|Z(x)\|_{\mathrm F}^2 .\end{aligned}
\]

*Proof.* Apply (2.2) to each entry and sum over the entries. \(\square\)

*Partial averages and the potential.* For \(0\le i\le t\) write \(m_{\le i}=(m_1,\ldots,m_i)\), \(y_{\le i}=(y_1,\ldots,y_i)\) and \(x_{>i}=(x_{i+1},\ldots,x_t)\). At stage \(i\) we construct, for every \(m_{\le i}\) and every \(q\in\Lambda^i\), functions
\[
H^{(i)}_q(y_{\le i};x_{>i})\in\mathbb R^{R_i\times r}
\]
with a common number \(R_i\) of rows, such that
\[
\begin{gathered}\sum_{q\in\Lambda^i}\bigl(H^{(i)}_q\bigr)^{\mathsf T}H^{(i)}_q\\=\sum_{x_{\le i}}\Bigl(\prod_{j=1}^i\pi^{m_j}_{j,y_j}(x_j)\Bigr)F(x).\end{gathered}\tag{3.1}
\]
Their Fourier coefficients \(\widehat H^{(i)}_{q,p}(x_{>i})\), \(p\in\Lambda^i\), are taken in the variables \(y_{\le i}\) only. Put
\[
\begin{gathered}
U^{(i)}_q=\Bigl[\lambda^{\operatorname{dist}(q,p)/2}\,\widehat H^{(i)}_{q,p}\Bigr]_{p\in\Lambda^i},\\
C^{(i)}_q=U^{(i)}_q\bigl(U^{(i)}_q\bigr)^{\mathsf T},
\end{gathered}
\]
functions of \(x_{>i}\) (and of \(m_{\le i}\)); \(U^{(i)}_q\) has \(rL^i\) columns. The potential is
\[
\Phi_i=\mathbb E_{m_{\le i}}\mathbb E_{x_{>i}}\sum_{q\in\Lambda^i}\bigl\|C^{(i)}_q(x_{>i})\bigr\|_{\mathrm F}^2 ,
\]
with all listed variables independent and uniform. At stage zero, \(\Lambda^0\) has one element \(\varnothing\); take \(R_0=r\) and \(H^{(0)}_\varnothing(x)=F(x)^{1/2}\). Then (3.1) holds, \(C^{(0)}_\varnothing=F\), and by Lemma 1.1(3) of [PSD factorizations and semidefinite lifts](psd-factorizations-and-semidefinite-lifts.md),
\[
\Phi_0=\mathbb E_x\|F(x)\|_{\mathrm F}^2\le\mathbb E_x(\operatorname{tr}F(x))^2\le B^2 .
\]
We show how to pass from stage \(i\) to stage \(i+1\) preserving (3.1) with \(\Phi_{i+1}\le2\Phi_i\).

*The tagged stack.* Fix \(m_{\le i}\), a branch \(q\in\Lambda^i\), and \(x_{>i+1}\). Abbreviate \(X=X_{i+1}\), \(Y=Y_{i+1}\), \(T_y=T_{i+1,y}\), write \(x\in X\) for the new input and \(y\in Y\) for the new character variable, and put
\[
\begin{gathered}U(x)=U^{(i)}_q(x,x_{>i+1}),\\ Z(x)=U(x)^{\mathsf T}U(x).\end{gathered}
\]
Then \(Z(x)\) has size \(rL^i\), and \(\|Z(x)\|_{\mathrm F}=\|C^{(i)}_q(x,x_{>i+1})\|_{\mathrm F}\), since \(\|U^{\mathsf T}U\|_{\mathrm F}=\|UU^{\mathsf T}\|_{\mathrm F}\). The fixed data determine the whole function \(x\mapsto Z(x)\) before \(m_{i+1}\) is chosen.

Write \(H_x(y_{\le i})=H^{(i)}_q(y_{\le i};x,x_{>i+1})\) for \(x\in X\). For \(m\in\mathcal M_{i+1}\), define \(H'\) with \(R_{i+1}=L|X|R_i\) rows, divided into blocks indexed by \((y',x)\in Y\times X\):
\[
\begin{aligned}&H'(y_{\le i},y)_{(y',x)}\\&\quad=\mathbf 1_{\{y'=y\}}\sqrt{\pi^m_y(x)}\\&\qquad\cdot H_x(y_{\le i}).\end{aligned}\tag{3.2}
\]
Different values of \(y\) occupy disjoint blocks, and
\[
\begin{aligned}&H'^{\mathsf T}H'=\sum_{x\in X}\pi^m_y(x)\\&\qquad\cdot H_x(y_{\le i})^{\mathsf T}H_x(y_{\le i}).\end{aligned}\tag{3.3}
\]
For \(z\in\Lambda\), concatenate the Fourier coefficients of \(H'\) at the frequencies \((p,z)\), with the old weights:
\[
\begin{gathered}V_z=\Bigl[\lambda^{\operatorname{dist}(q,p)/2}\,\widehat{H'}_{p,z}\Bigr]_{p\in\Lambda^i},\\ A_z=V_zV_z^{\mathsf T}.\end{gathered}
\]
Since \(\mathbb E_y[\chi_z(y)\mathbf 1_{\{y'=y\}}]=L^{-1}\chi_z(y')\), the \((y',x)\) block of \(V_z\) is \(L^{-1}\chi_z(y')\sqrt{\pi^m_{y'}(x)}\,U(x)\). Multiplying blocks,
\[
\begin{aligned}&V_z^{\mathsf T}V_{z'}\\&\quad=\frac1{L^2}\sum_{y\in Y}\chi_z(y)\chi_{z'}(y)\\&\qquad\cdot(T_yZ)(m),\end{aligned}\tag{3.4}
\]
and \(\langle A_z,A_{z'}\rangle=\operatorname{tr}(V_zV_z^{\mathsf T}V_{z'}V_{z'}^{\mathsf T})=\|V_z^{\mathsf T}V_{z'}\|_{\mathrm F}^2\).

**Lemma 3.2** (overlaps). With \(m=m_{i+1}\) uniform,
\[
\begin{aligned}\mathbb E_m\langle A_z,A_{z'}\rangle&\le\frac1{L^2}\,\mathbb E_x\|Z(x)\|_{\mathrm F}^2\\&\quad\cdot\begin{cases}1,&z=z',\\ \theta,&z\ne z'.\end{cases}\end{aligned}
\]

*Proof.* For \(z=z'\), (3.4) gives \(V_z^{\mathsf T}V_z=L^{-1}\mathbb E_y(T_yZ)(m)\). The convexity of \(\|\cdot\|_{\mathrm F}^2\), first over \(y\) and then over the probability measure \(\pi^m_y\), gives
\[
\|V_z^{\mathsf T}V_z\|_{\mathrm F}^2\le\frac1{L^2}\,\mathbb E_y\sum_x\pi^m_y(x)\|Z(x)\|_{\mathrm F}^2 ,
\]
and (2.1) turns the average over \(m\) of the right side into \(L^{-2}\mathbb E_x\|Z(x)\|_{\mathrm F}^2\). For \(z\ne z'\), the character \(\chi_z\chi_{z'}=\chi_{z+z'}\) is nontrivial, so \(\sum_y\chi_z(y)\chi_{z'}(y)=0\), and \(\mu=\mathbb E_xZ(x)\) may be subtracted from every summand in (3.4). Convexity and Lemma 3.1 give
\[
\begin{aligned}&\mathbb E_m\|V_z^{\mathsf T}V_{z'}\|_{\mathrm F}^2\\&\quad\le\frac1{L^2}\,\mathbb E_y\mathbb E_m\|(T_yZ)(m)-\mu\|_{\mathrm F}^2\\&\quad\le\frac\theta{L^2}\,\mathbb E_x\|Z(x)\|_{\mathrm F}^2 .\end{aligned}
\]
Here Lemma 3.1 applies because \(Z\) was fixed before \(m\) was chosen. \(\square\)

*Splitting the stack.* For each \(m\), apply Theorem 2.1 of [Splitting positive semidefinite matrices](splitting-positive-semidefinite-matrices.md) to the \(L\) operators \(A_z\), \(z\in\Lambda\), on \(\mathbb R^{R_{i+1}}\). It gives mutually orthogonal projections \(P_s\), \(s\in\Lambda\), with \(\sum_sP_s=I\). Define the branches of stage \(i+1\) by
\[
H^{(i+1)}_{(q,s)}=P_sH'\qquad(s\in\Lambda),
\]
where \((q,s)\in\Lambda^{i+1}\). Since \(P_s^{\mathsf T}P_s=P_s\) and \(\sum_sP_s=I\), we get \(\sum_s(P_sH')^{\mathsf T}P_sH'=H'^{\mathsf T}H'\). By (3.3) and (3.1) at stage \(i\), summing over \(q\) gives (3.1) at stage \(i+1\).

The projections depend on \(m_{\le i+1}\), \(q\) and \(x_{>i+1}\), but not on \(y_{\le i+1}\). So they commute with taking Fourier coefficients: the coefficient of \(P_sH'\) at \((p,z)\) is \(P_s\widehat{H'}_{p,z}\). All \(R_{i+1}\) rows are kept, whatever the ranks of the projections, so all branches use the same number of rows. As all sets are finite, a choice of projections can be made for every value of the fixed data.

**Lemma 3.3** (one step). \(\Phi_{i+1}\le2\Phi_i\).

*Proof.* Since \(\operatorname{dist}((q,s),(p,z))=\operatorname{dist}(q,p)+\mathbf 1_{\{s\ne z\}}\), the matrix \(U^{(i+1)}_{(q,s)}\) is the concatenation over \(z\) of the blocks \(\lambda^{\mathbf 1_{\{s\ne z\}}/2}P_sV_z\), and
\[
C^{(i+1)}_{(q,s)}=\sum_{z\in\Lambda}\lambda^{\mathbf 1_{\{s\ne z\}}}P_sA_zP_s .
\]
By the Cauchy–Schwarz inequality for this sum of \(L\) terms, then \(\|P_zA_zP_z\|_{\mathrm F}\le\|A_z\|_{\mathrm F}\) and the inequality of Theorem 2.1 of [Splitting positive semidefinite matrices](splitting-positive-semidefinite-matrices.md),
\[
\begin{aligned}&\sum_s\bigl\|C^{(i+1)}_{(q,s)}\bigr\|_{\mathrm F}^2\\&\quad\le L\sum_s\sum_z\lambda^{2\cdot\mathbf 1_{\{s\ne z\}}}\|P_sA_zP_s\|_{\mathrm F}^2\\&\quad\le L\Bigl(\sum_z\|A_z\|_{\mathrm F}^2\\&\qquad+\lambda^2C_L\sum_{z\ne z'}\langle A_z,A_{z'}\rangle\Bigr).\end{aligned}
\]
There are \(L\) diagonal and \(L(L-1)\) ordered off-diagonal pairs, so Lemma 3.2 and (2.3) give
\[
\begin{aligned}&\mathbb E_{m_{i+1}}\sum_s\bigl\|C^{(i+1)}_{(q,s)}\bigr\|_{\mathrm F}^2\\&\quad\le\bigl(1+(L-1)\lambda^2C_L\theta\bigr)\,\mathbb E_x\|Z(x)\|_{\mathrm F}^2\\&\quad\le2\,\mathbb E_{x_{i+1}}\bigl\|C^{(i)}_q(x_{i+1},x_{>i+1})\bigr\|_{\mathrm F}^2 .\end{aligned}
\]
This holds for every \(m_{\le i}\), \(q\) and \(x_{>i+1}\). Under the product measure, \(m_{i+1}\) and \(x_{i+1}\) are uniform and independent of these data. Summing over \(q\) and averaging over \(m_{\le i}\) and \(x_{>i+1}\) gives \(\Phi_{i+1}\le2\Phi_i\). \(\square\)

*Proof of Theorem 2.1.* Starting from stage zero and applying the step \(t\) times gives, at stage \(t\), functions \(H^m_q=H^{(t)}_q\) of \(y\) alone (no inputs \(x_{>t}\) remain) with \(R=R_t\) rows, for which (3.1) is (2.4) and \(\Phi_t\le2^t\Phi_0\le2^tB^2\) is (2.5). Choose \(m\) with \(\sum_q\|C^m_q\|_{\mathrm F}^2\le2^tB^2\). Each \(U^m_q\) has \(rL^t\) columns, so \(\operatorname{rank}C^m_q\le rL^t\) whatever its number of rows. By Lemma 1.1(3) of [PSD factorizations and semidefinite lifts](psd-factorizations-and-semidefinite-lifts.md) and the Cauchy–Schwarz inequality over the \(L^t\) branches,
\[
\begin{aligned}&\sum_{q,p}\lambda^{\operatorname{dist}(q,p)}\|\widehat H^m_{q,p}\|_{\mathrm F}^2=\sum_q\operatorname{tr}C^m_q\\&\quad\le\sqrt{rL^t}\sum_q\|C^m_q\|_{\mathrm F}\\&\quad\le\sqrt{rL^t}\,\sqrt{L^t}\Bigl(\sum_q\|C^m_q\|_{\mathrm F}^2\Bigr)^{1/2}\\&\quad\le L^t\sqrt r\,B\,2^{t/2}. \qquad\square\end{aligned}
\]

The bound (2.6) has the factor \(L^t\) from the number of branches and \(2^{t/2}\) from the potential. In [The lower bound for perfect matching](the-lower-bound-for-perfect-matching.md) these are absorbed by the weight \(\lambda^{\operatorname{dist}(q,p)}\), with \(\lambda\) a large constant, at all frequencies far from the center.

## 4. Exercises

**4.1.** Show that \(\|C\|_{\mathrm F}^2=\sum_{p,p'}w_pw_{p'}\|\widehat H_p^{\mathsf T}\widehat H_{p'}\|_{\mathrm F}^2\) and \(\operatorname{tr}C=\sum_pw_p\|\widehat H_p\|_{\mathrm F}^2\) for \(C=UU^{\mathsf T}\) and \(U=[w_p^{1/2}\widehat H_p]_p\).

**4.2.** Show that a positive semidefinite \(F\) satisfies \(\|F\|_{\mathrm F}\le\operatorname{tr}F\), and that \(F=I_r\) has \(\|F\|_{\mathrm{op}}=1\) and \(\|F\|_{\mathrm F}=\sqrt r\). Why does the proof of Theorem 2.1 use a bound on the trace rather than on the operator norm?

**4.3.** Let \(t=1\), and suppose that \(\pi^m_{1,y}\) does not depend on \(m\). Show that (2.1) forces \(\pi^m_{1,y}\) to be uniform, that (2.2) then holds with \(\theta=0\), and that \(\overline F_m(y)=\mathbb E_xF(x)\) for every \(y\). Find a representation (2.4) with \(\widehat H^m_{q,p}=0\) for \(p\ne q\).

**4.4.** Verify (3.4) from the description of the blocks of \(V_z\).

**4.5.** Show that the number of rows \(R_t\) in the proof equals \(r\,L^t\prod_i|X_i|\).

## 5. Solutions

**4.1.** \(\operatorname{tr}C=\|U\|_{\mathrm F}^2\) is the sum of the squared norms of the blocks \(w_p^{1/2}\widehat H_p\). Also \(\|UU^{\mathsf T}\|_{\mathrm F}^2=\operatorname{tr}(UU^{\mathsf T}UU^{\mathsf T})=\|U^{\mathsf T}U\|_{\mathrm F}^2\), and \(U^{\mathsf T}U\) has the blocks \((w_pw_{p'})^{1/2}\widehat H_p^{\mathsf T}\widehat H_{p'}\).

**4.2.** By Lemma 1.1(3) of [PSD factorizations and semidefinite lifts](psd-factorizations-and-semidefinite-lifts.md), \(\|F\|_{\mathrm F}\le\operatorname{tr}F\). For \(F=I_r\) the eigenvalues are all one. The potential \(\Phi_0=\mathbb E_x\|F(x)\|_{\mathrm F}^2\) must be bounded independently of \(r\); a bound on the operator norm would only give \(\Phi_0\le rB^2\), and the factor \(r\) would enter (2.6).

**4.3.** If \(\pi^m_{1,y}=\pi_y\) does not depend on \(m\), then (2.1) says \(\pi_y(x)=1/|X_1|\). Then \(T_{1,y}g=\mathbb E_xg\) for every \(m\), the left side of (2.2) vanishes, and \(\overline F_m(y)=\mathbb E_xF(x)\) for every \(y\). Then \(H_0=(\mathbb E_xF)^{1/2}\), constant in \(y\), and \(H_q=0\) for \(q\ne0\) give (2.4); the only nonzero coefficient is \(\widehat H_{0,0}\).

**4.4.** The \((y',x)\) block of \(V_z\) is \(L^{-1}\chi_z(y')\sqrt{\pi^m_{y'}(x)}\,U(x)\). Hence
\[
\begin{aligned}V_z^{\mathsf T}V_{z'}&=\frac1{L^2}\sum_{y',x}\chi_z(y')\chi_{z'}(y')\\&\quad\cdot\pi^m_{y'}(x)\,U(x)^{\mathsf T}U(x),\end{aligned}
\]
and summing over \(x\) first gives \((T_{y'}Z)(m)\).

**4.5.** \(R_0=r\) and \(R_{i+1}=L|X_{i+1}|R_i\).

## References

- [OpenAI-PSD] OpenAI, *Exponential PSD rank of positively shifted matching matrices*, OpenAI Math Release preprint, 5 October 2026, Section 4. https://github.com/openai/math/tree/main/preprints/Exponential-PSD-rank-of-positively-shifted-matching-matrices-October-5-2026
- [FSP 2016] H. Fawzi, J. Saunderson, P. A. Parrilo, *Sparse sums of squares on finite abelian groups and improved semidefinite lifts*, Math. Program. 160 (2016); preprint title *Sparse sum-of-squares certificates on finite abelian groups*. https://arxiv.org/abs/1503.01207
