# The tensor estimate

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

For a moment pair \((V,\varphi)\) and a test function \(f\), the lesson on moment coordinates defined the matrix field \(B=\tau\,D_x^2f\,\tau\), the vector field \(W=\delta_\mu B\) and the function \(u=\delta_\mu W=A(A-1)f\). This lesson proves the inequality of [OpenAI-L, Section 6] between them:
\[
\mathbb E\,u^2\ \ge\ \mathbb E\operatorname{tr}(MBHB)+\mathbb E\,W^THW ,
\]
where \(H=D_x^2V\) and \(M=\tau^{-1}\). It bounds the size of the test function \(u\) from below by two quadratic expressions in which the Hessian of \(V\) appears linearly. In the proof of the variance bound, \(H\) is a sum of the Hessians of the functions \(\psi_i\), and the inequality is used for each summand.

- The identity \(\mathbb Eu^2=\mathbb EW^THW+\mathbb E\operatorname{tr}((D_xW)^2)\) (Lemma 2.1).
- The moment equation, differentiated twice (Lemma 3.2).
- Two expansions (Lemmas 4.1 and 4.2) and three contractions (Lemma 5.1).
- A sum of squares, and the estimate (Lemma 6.1, Theorem 1.1).

The lesson follows [OpenAI-L, Section 6]. It continues [Moment coordinates and their adjoints](moment-coordinates-and-their-adjoints.md) and uses its notation and results. No hypothesis is used: the results hold for every moment pair.

## 1. The statement

Fix a moment pair \((V,\varphi)\) on \(\mathbb R^n\), with \(x=\nabla\varphi(z)\), \(\tau=D^2\varphi\), \(M=\tau^{-1}\), and a smooth function \(f\) of \(x\) with compact support. As in the lesson on moment coordinates,
\[
\begin{gathered}
h=D_x^2f,\qquad P=\tau h,\qquad B=\tau h\tau,\\
W=\delta_\mu B,\qquad u=\delta_\mu W .
\end{gathered}
\]
Let \(H=D_x^2V\), and let \(D_xW\) be the matrix with the entries \((D_xW)_{ij}=\partial_{x_j}W_i\).

In this lesson *repeated indices are summed from \(1\) to \(n\)*. We write \(\partial_k=\partial_{z_k}\), \(\partial_k^*=x_k-\partial_k\), and
\[
C_{ijk}=\partial_i\partial_j\partial_k\varphi ,
\]
a tensor that is symmetric in its three indices; \(C_i\) is the matrix with the entries \((C_i)_{jk}=C_{ijk}\). Recall the chain rule \(\partial_k(g(x(z)))=g_{x_i}\tau_{ik}\).

**Theorem 1.1 (tensor estimate).**
\[
\mathbb E\operatorname{tr}\bigl((D_xW)^2\bigr)\ \ge\ \mathbb E\operatorname{tr}(MBHB),
\]
and
\[
\mathbb E\,u^2\ \ge\ \mathbb E\operatorname{tr}(MBHB)+\mathbb E\,W^THW .
\]

The square in the first line is the square of a matrix, and \(\operatorname{tr}((D_xW)^2)=(\partial_{x_j}W_i)(\partial_{x_i}W_j)\). It need not be positive at each point.

## 2. The first identity

**Lemma 2.1.** For a smooth vector field \(W\) with compact support and \(u=\delta_\mu W\),
\[
\mathbb E\,u^2=\mathbb E\,W^THW+\mathbb E\operatorname{tr}\bigl((D_xW)^2\bigr).
\]

**Proof.** Since \(u=V_{x_j}W_j-\partial_{x_j}W_j\),
\[
\partial_{x_i}u=H_{ij}W_j+\bigl(V_{x_j}-\partial_{x_j}\bigr)\partial_{x_i}W_j .
\]
By Lemma 2.1 (2) of the lesson on moment coordinates, \(\mathbb E\,u^2=\mathbb E\,u\,\delta_\mu W=\mathbb E\,W_i\,\partial_{x_i}u\), and for each \(i,j\) the same lemma, read from right to left, shows that the mean of \(W_i(V_{x_j}-\partial_{x_j})\partial_{x_i}W_j\) is the mean of \((\partial_{x_j}W_i)(\partial_{x_i}W_j)\). \(\blacksquare\)

So the second inequality of Theorem 1.1 follows from the first.

## 3. The moment equation, differentiated twice

**Lemma 3.1.** With \(c_i=\operatorname{tr}(MC_i)\),
\[
\begin{gathered}
\tau_{ik}V_{x_k}=x_i+c_i,\\
\partial_dM_{dk}-x_dM_{dk}=-V_{x_k}.
\end{gathered}
\]

**Proof.** By Lemma 1.1 of the lesson on moment coordinates, \(V(x(z))=\varphi+\log\det\tau-\log Z\). Apply \(\partial_i\): the left side gives \(V_{x_k}\tau_{ki}\) by the chain rule, and the right side gives \(x_i+\operatorname{tr}(M\,\partial_i\tau)=x_i+c_i\), by the rule for the derivative of the logarithm of a determinant. For the second formula, \(\partial_dM=-M(\partial_d\tau)M=-MC_dM\), so
\[
\partial_dM_{dk}=-M_{da}C_{dab}M_{bk}=-c_bM_{bk},
\]
and by the first formula
\[
\begin{aligned}
\partial_dM_{dk}-x_dM_{dk}&=-(c_b+x_b)M_{bk}\\
&=-\tau_{bl}V_{x_l}M_{bk}=-V_{x_k}.
\end{aligned}
\]
\(\blacksquare\)

**Lemma 3.2.**
\[
\begin{aligned}
(\tau H\tau-\tau)_{ij}&=(\partial_d-x_d)\bigl(M_{dk}C_{ijk}\bigr)\\
&\quad-\operatorname{tr}(MC_iMC_j).
\end{aligned}
\]

**Proof.** Apply \(\partial_j\) to the first formula of Lemma 3.1. On the left,
\[
\partial_j(\tau_{ik}V_{x_k})=C_{ijk}V_{x_k}+\tau_{ik}H_{kl}\tau_{lj}.
\]
On the right, with \(\partial_jM=-MC_jM\),
\[
\begin{aligned}
\partial_j(x_i+c_i)&=\tau_{ij}-\operatorname{tr}(MC_jMC_i)\\
&\quad+M_{kl}\,\partial_jC_{ikl}.
\end{aligned}
\]
So
\[
\begin{aligned}
(\tau H\tau-\tau)_{ij}&=M_{dk}\,\partial_dC_{ijk}-C_{ijk}V_{x_k}\\
&\quad-\operatorname{tr}(MC_iMC_j),
\end{aligned}
\]
where the fourth derivatives of \(\varphi\) were renamed by their symmetry. By the second formula of Lemma 3.1,
\[
\begin{aligned}
&(\partial_d-x_d)(M_{dk}C_{ijk})\\
&\quad=-V_{x_k}C_{ijk}+M_{dk}\,\partial_dC_{ijk}.
\end{aligned}
\]
\(\blacksquare\)

The operator \(\partial_d-x_d\) is \(-\partial_d^*\). So when the right side of Lemma 3.2 is integrated against a function, its first term can be moved to the other factor.

## 4. Two expansions

**Lemma 4.1.** Let \(R_{al}=\partial_k^*\partial_lP_{ak}\). Then \(D_zW=B+R\), the matrix \(R\) is symmetric, \(D_xW=(B+R)M\), and
\[
\begin{aligned}
\mathbb E\operatorname{tr}\bigl((D_xW)^2\bigr)&=\mathbb E\operatorname{tr}(MBMB)\\
&\quad+2\,\mathbb E\,(\partial_kh_{al})(\partial_lP_{ak})\\
&\quad+\mathbb E\operatorname{tr}(MRMR).
\end{aligned}
\]

**Proof.** Since \(\partial_l(x_kF)-x_k\partial_lF=\tau_{kl}F\), we have \(\partial_l\partial_k^*F=\partial_k^*\partial_lF+\tau_{kl}F\). So
\[
\begin{aligned}
\partial_lW_a&=\partial_l\partial_k^*P_{ak}\\
&=R_{al}+P_{ak}\tau_{kl}=R_{al}+B_{al}.
\end{aligned}
\]
By Proposition 4.1 (3) of the lesson on moment coordinates \(D_zW\) is symmetric, and \(B\) is symmetric; so \(R\) is symmetric. The chain rule for the inverse map gives \(\partial_{x_j}W_i=(\partial_lW_i)M_{lj}\). Hence
\[
\begin{aligned}
&\operatorname{tr}\bigl((D_xW)^2\bigr)\\
&\quad=\operatorname{tr}\bigl((B+R)M(B+R)M\bigr)\\
&\quad=\operatorname{tr}(MBMB)+2\operatorname{tr}(MBMR)\\
&\qquad+\operatorname{tr}(MRMR).
\end{aligned}
\]
Since \(MBM=h\), the middle term is \(2h_{al}R_{al}=2h_{al}\,\partial_k^*\partial_lP_{ak}\), and by Lemma 2.1 (1) of the lesson on moment coordinates its mean is \(2\,\mathbb E\,(\partial_kh_{al})(\partial_lP_{ak})\). \(\blacksquare\)

**Lemma 4.2.** Let \(Q=h\tau h\). Then
\[
\begin{aligned}
\mathbb E\operatorname{tr}(MBHB)&=\mathbb E\operatorname{tr}(MBMB)\\
&\quad-\mathbb E\,(\partial_dQ_{ij})\,M_{dk}C_{ijk}\\
&\quad-\mathbb E\,Q_{ij}\operatorname{tr}(MC_iMC_j).
\end{aligned}
\]

**Proof.** \(\operatorname{tr}(MBHB)=\operatorname{tr}\bigl((\tau H\tau)\,MBMBM\bigr)\) and \(MBMBM=h\tau h=Q\). So \(\operatorname{tr}(MBHB)=Q_{ij}(\tau H\tau)_{ij}\). Insert Lemma 3.2. The term with \(\tau_{ij}\) gives \(\operatorname{tr}(Q\tau)=\operatorname{tr}(MBMB)\). In the term with \((\partial_d-x_d)=-\partial_d^*\), Lemma 2.1 (1) of the lesson on moment coordinates moves the derivative to \(Q_{ij}\), which has compact support. \(\blacksquare\)

Subtracting, the terms \(\mathbb E\operatorname{tr}(MBMB)\) cancel. Let \(\Delta\) be the difference of the two sides of the first inequality of Theorem 1.1,
\[
\Delta=\mathbb E\operatorname{tr}\bigl((D_xW)^2\bigr)-\mathbb E\operatorname{tr}(MBHB).
\]
Then
\[
\Delta=\mathbb E\operatorname{tr}(MRMR)+\mathbb E\,(T_1+T_2+T_3),
\]
with the three functions
\[
\begin{gathered}
T_1=2\,(\partial_kh_{al})(\partial_lP_{ak}),\\
T_2=(\partial_dQ_{ij})\,M_{dk}C_{ijk},\\
T_3=Q_{ij}\operatorname{tr}(MC_iMC_j).
\end{gathered}
\]
The matrix \(M^{1/2}RM^{1/2}\) is symmetric and \(\operatorname{tr}(MRMR)\) is its squared norm, so the first term in this formula for \(\Delta\) is not negative. It remains to show that \(T_1+T_2+T_3\ge0\) at every point.

## 5. Three contractions

At a point, let \(\tau^{1/2}\) be the positive square root of \(\tau\) and \(\tau^{-1/2}\) its inverse. Let \(S_{abc}=f_{x_ax_bx_c}\), and define the tensors
\[
\begin{gathered}
\hat S_{ijk}=\tau^{1/2}_{ia}\tau^{1/2}_{jb}\tau^{1/2}_{kc}\,S_{abc},\\
\hat J_{ijk}=(\tau^{1/2}h)_{iq}\,\tau^{-1/2}_{jr}\tau^{-1/2}_{ks}\,C_{qrs}.
\end{gathered}
\]
\(\hat S\) is symmetric in its three indices, and \(\hat J\) is symmetric in its last two indices. For tensors with three indices let \(\langle X,Y\rangle=X_{ijk}Y_{ijk}\), \(\|X\|^2=\langle X,X\rangle\), and \(X^{(12)}_{ijk}=X_{jik}\). If \(\tau\) is the identity matrix at the point, then \(\hat S=S\) and \(\hat J_{ijk}=h_{iq}C_{qjk}\).

**Lemma 5.1.** At every point,
\[
\begin{aligned}
T_1&=2\,\|\hat S\|^2+2\,\langle\hat S,\hat J\rangle,\\
T_2&=2\,\langle\hat S,\hat J\rangle+\langle\hat J,\hat J^{(12)}\rangle,\\
T_3&=\|\hat J\|^2 .
\end{aligned}
\]

**Proof.** Inserting the definitions and using \(\tau^{1/2}\tau^{1/2}=\tau\), \(\tau^{1/2}\tau^{-1/2}=I\), \(\tau^{-1/2}\tau^{-1/2}=M\), one finds
\[
\begin{aligned}
\|\hat S\|^2&=S_{abc}S_{a'b'c'}\,\tau_{aa'}\tau_{bb'}\tau_{cc'},\\
\langle\hat S,\hat J\rangle&=S_{abc}\,(\tau h)_{aq}\,C_{qbc},\\
\langle\hat J,\hat J^{(12)}\rangle&=h_{ia}C_{abd}\,h_{bj}C_{jik}\,M_{dk},\\
\|\hat J\|^2&=Q_{qq'}\,M_{rr'}M_{ss'}\,C_{qrs}C_{q'r's'} ,
\end{aligned}
\]
where \(Q=h\tau h\). Now compute the three functions with the chain rule.

For \(T_1\): \(\partial_kh_{al}=S_{alm}\tau_{mk}\) and \(\partial_lP_{ak}=C_{ail}h_{ik}+\tau_{ai}S_{ikp}\tau_{pl}\). So
\[
\begin{aligned}
\tfrac12T_1&=S_{alm}S_{ikp}\,\tau_{ai}\tau_{mk}\tau_{lp}\\
&\quad+S_{alm}\,(\tau h)_{mi}\,C_{ial}.
\end{aligned}
\]
By the symmetry of \(S\), the first term is \(\|\hat S\|^2\) and the second is \(\langle\hat S,\hat J\rangle\).

For \(T_2\): differentiating the three factors of \(Q=h\tau h\),
\[
\begin{aligned}
\partial_dQ_{ij}&=S_{iap}\tau_{pd}\,(\tau h)_{aj}+h_{ia}C_{abd}h_{bj}\\
&\quad+(h\tau)_{ib}\,S_{bjp}\tau_{pd}.
\end{aligned}
\]
Multiply by \(M_{dk}C_{ijk}\) and use \(\tau_{pd}M_{dk}=\delta_{pk}\). The first and the third term give \(S_{iak}(\tau h)_{aj}C_{ijk}\) and \(S_{bjk}(\tau h)_{bi}C_{ijk}\), each equal to \(\langle\hat S,\hat J\rangle\). The second gives \(h_{ia}C_{abd}h_{bj}C_{ijk}M_{dk}=\langle\hat J,\hat J^{(12)}\rangle\).

For \(T_3\): \(Q_{ij}\,M_{ab}C_{ibc}M_{cd}C_{jda}\) is the expression for \(\|\hat J\|^2\), after renaming the indices. \(\blacksquare\)

## 6. A sum of squares

**Lemma 6.1.** Let \(S\) be a tensor with three indices that is symmetric in all of them, and \(J\) one that is symmetric in its last two indices. Let \((\operatorname{Sym}J)_{ijk}=\tfrac13(J_{ijk}+J_{jik}+J_{kij})\). Then
\[
\begin{aligned}
&2\|S\|^2+4\langle S,J\rangle+\|J\|^2+\langle J,J^{(12)}\rangle\\
&\quad=2\,\|S+\operatorname{Sym}J\|^2+\tfrac16\,\|J-J^{(12)}\|^2 .
\end{aligned}
\]

**Proof.** Let \(J'_{ijk}=J_{kij}\). Since \(J\) is symmetric in its last two indices, \(\langle J,J'\rangle=J_{ijk}J_{kji}\), and renaming the indices and using the symmetry again shows \(\langle J,J'\rangle=\langle J,J^{(12)}\rangle=\langle J^{(12)},J'\rangle\). The three tensors \(J,J^{(12)},J'\) have the same norm. So
\[
\|\operatorname{Sym}J\|^2=\tfrac19\bigl(3\|J\|^2+6\langle J,J^{(12)}\rangle\bigr),
\]
and \(\langle S,\operatorname{Sym}J\rangle=\langle S,J\rangle\) because \(S\) is symmetric. Hence
\[
\begin{aligned}
&2\,\|S+\operatorname{Sym}J\|^2\\
&\quad=2\|S\|^2+4\langle S,J\rangle\\
&\qquad+\tfrac23\|J\|^2+\tfrac43\langle J,J^{(12)}\rangle,
\end{aligned}
\]
and \(\tfrac16\|J-J^{(12)}\|^2=\tfrac13\|J\|^2-\tfrac13\langle J,J^{(12)}\rangle\). Add. \(\blacksquare\)

**Proof of Theorem 1.1.** By Lemma 5.1, \(T_1+T_2+T_3\) is the left side of Lemma 6.1 for \(\hat S\) and \(\hat J\); so it is a sum of two squares. By the formula for \(\Delta\) of Section 4,
\[
\begin{aligned}
\Delta&=\mathbb E\,\bigl\|M^{1/2}RM^{1/2}\bigr\|^2\\
&\quad+2\,\mathbb E\,\bigl\|\hat S+\operatorname{Sym}\hat J\bigr\|^2\\
&\quad+\tfrac16\,\mathbb E\,\bigl\|\hat J-\hat J^{(12)}\bigr\|^2\ \ge\ 0 .
\end{aligned}
\]
The second inequality follows with Lemma 2.1. \(\blacksquare\)

The proof gives more than the inequality: the difference of the two sides is written as the mean of three squares. [OpenAI-L] obtains the three contractions by a linear change of the coordinates that makes \(\tau\) the identity at one point; the tensors \(\hat S\) and \(\hat J\) are the tensors \(S\) and \(h_{iq}C_{qjk}\) in those coordinates.

**Example 6.2.** For the Gaussian pair (\(\tau=I\), \(V=\tfrac12|x|^2\), \(H=I\), \(C=0\)) and \(f=x_1^3\), Example 4.2 of the lesson on moment coordinates gives \(W=(6x_1^2-6,0,\dots,0)\) and \(B=D^2f\) with the single entry \(6x_1\). Then \(D_xW\) has the single entry \(12x_1\), and
\[
\begin{gathered}
\mathbb E\operatorname{tr}((D_xW)^2)=144,\\
\mathbb E\operatorname{tr}(MBHB)=36 .
\end{gathered}
\]
The three squares: \(R=D_zW-B\) has the entry \(6x_1\), with \(\mathbb E\|R\|^2=36\); \(\hat S\) has the entry \(6\), so \(2\|\hat S\|^2=72\); and \(\hat J=0\). Indeed \(144-36=36+72\). Also \(u=6x_1^3-18x_1\), \(\mathbb Eu^2=36\cdot15-216\cdot3+324=216\), and \(\mathbb EW^THW=\mathbb E(6x_1^2-6)^2=72\): Lemma 2.1 reads \(216=72+144\).

## 7. Exercises

**7.1.** Prove Lemma 6.1 directly for \(n=1\), where all tensors are numbers.

**7.2.** For the Gaussian pair let \(f\) be a polynomial with \(Af=kf\) for an integer \(k\ge2\). Show that \(\mathbb E\operatorname{tr}((D_xW)^2)=(k-1)^2\,\mathbb E\|D^2f\|^2\) and \(\mathbb E\operatorname{tr}(MBHB)=\mathbb E\|D^2f\|^2\). For which \(k\) is the first inequality of Theorem 1.1 an equality?

**7.3.** Show that \(\operatorname{tr}(MBHB)\ge0\) at every point where \(H\) is positive semidefinite, and that \(\operatorname{tr}(MBH_1B)\le\operatorname{tr}(MBH_2B)\) if \(H_2-H_1\) is positive semidefinite.

**7.4.** Let \(n=1\). Write \(T_1\), \(T_2\), \(T_3\) in terms of \(\tau=\varphi''\), \(C=\varphi'''\), \(h=f''\) and \(S=f'''\), and check Lemma 5.1 and the sum of squares.

## 8. Solutions

**7.1.** For numbers, \(J^{(12)}=J\) and \(\operatorname{Sym}J=J\). The left side is \(2S^2+4SJ+2J^2=2(S+J)^2\), and the right side is \(2(S+J)^2+0\).

**7.2.** Here \(W=\nabla(Af-f)=(k-1)\nabla f\), so \(D_xW=(k-1)D^2f\), a symmetric matrix, and \(\operatorname{tr}((D_xW)^2)=(k-1)^2\|D^2f\|^2\). And \(M=H=I\), \(B=D^2f\). The two sides are equal exactly if \(k=2\) or \(D^2f=0\). (For polynomials and the Gaussian measure the integrations by parts of this lesson are valid without compact support.)

**7.3.** Let \(G=H^{1/2}BM^{1/2}\). Then \(\operatorname{tr}(MBHB)\) is \(\operatorname{tr}(M^{1/2}BH^{1/2}\cdot H^{1/2}BM^{1/2})\), which is \(\operatorname{tr}(G^TG)=\|G\|^2\ge0\). The expression is linear in \(H\), so the difference for \(H_2\) and \(H_1\) is the expression for \(H_2-H_1\).

**7.4.** \(P=\tau h\) and \(Q=\tau h^2\). \(\partial h=S\tau\), \(\partial P=Ch+\tau^2S\), \(\partial Q=Ch^2+2\tau^2hS\). So \(T_1=2S\tau(Ch+\tau^2S)\), which is \(2\tau^3S^2+2\tau hCS\); \(T_2=(Ch^2+2\tau^2hS)C/\tau\), which is \(C^2h^2/\tau+2\tau hCS\); and \(T_3=\tau h^2C^2/\tau^2=C^2h^2/\tau\). With \(\hat S=\tau^{3/2}S\) and \(\hat J=\tau^{-1/2}hC\): \(\|\hat S\|^2=\tau^3S^2\), \(\hat S\hat J=\tau hCS\), \(\hat J^2=h^2C^2/\tau\), in agreement with Lemma 5.1. The sum of the three is \(2\tau^3S^2+4\tau hCS+2h^2C^2/\tau\), and this is \(2(\hat S+\hat J)^2\).

## References

- [OpenAI-L] OpenAI, *The logarithmic Brunn-Minkowski conjecture*, OpenAI Math Release preprint, 23 September 2026, Section 6. https://github.com/openai/math/tree/main/preprints/The-logarithmic-Brunn-Minkowski-conjecture-September-23-2026
