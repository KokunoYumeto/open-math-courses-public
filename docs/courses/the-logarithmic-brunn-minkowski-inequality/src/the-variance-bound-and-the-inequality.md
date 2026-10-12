# The variance bound and the inequality

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson proves the variance bound for the soft polytopes,
\[
\operatorname{Var}_\mu\Bigl(\sum_ib_i\psi_i\Bigr)\le\sum_ib_i^2\,\mathbb E_\mu\psi_i ,
\]
from the tensor estimate and the density of the test functions, and with it the logarithmic Brunn-Minkowski inequality. The proof is that of [OpenAI-L, Section 7]. It uses the two statements from the literature that the course names as hypotheses: (M), the existence of moment coordinates with a bounded Hessian, and (ER), interior elliptic regularity. For the exponent \(q=2\) the lesson also gives a short proof of the variance bound that needs no hypothesis.

- The functions \(\psi_i\) in moment coordinates (Lemma 2.1).
- The bound on the test functions, by two inequalities of Cauchy and Schwarz (Proposition 3.1).
- The variance bound (Theorem 4.1) and the inequality (Theorem 5.1).
- The case \(q=2\) (Proposition 6.1).

The lesson uses all the earlier lessons of the course: [Wulff bodies and the reduction to a variance bound](wulff-bodies-and-the-reduction-to-a-variance-bound.md), [Moment coordinates and their adjoints](moment-coordinates-and-their-adjoints.md), [The tensor estimate](the-tensor-estimate.md) and [Density of the even tests](density-of-the-even-tests.md).

## 1. The setting

Let \(n\ge2\), \(N\ge1\), let \(q\ge2\) be an even integer, \(\varepsilon>0\), \(p_1,\dots,p_N\) nonzero vectors and \(h_1,\dots,h_N>0\). As in the first lesson,
\[
\begin{gathered}
\psi_i(x)=\Bigl(\frac{\langle p_i,x\rangle}{h_i}\Bigr)^q,\\
V=\frac\varepsilon2|x|^2+\sum_i\psi_i,\\
d\mu=Z^{-1}e^{-V}dx,\qquad a_i=\mathbb E\,\psi_i .
\end{gathered}
\]
Let \(H_i=D^2\psi_i\) and \(H=D^2V=\varepsilon I+\sum_iH_i\). With the linear function \(\ell_i=\langle p_i,x\rangle/h_i\),
\[
\begin{gathered}
\nabla\psi_i=q\,\ell_i^{q-1}\,\frac{p_i}{h_i},\\
H_i=q(q-1)\,\ell_i^{q-2}\,\frac{p_ip_i^T}{h_i^2}.
\end{gathered}
\]
Since \(q-2\) is even, \(H_i\) is positive semidefinite, and \(H\ge\varepsilon I\). The function \(V\) is smooth and even. Every polynomial is integrable for \(\mu\), because \(e^{-V}\le e^{-\varepsilon|x|^2/2}\); and \(a_i>0\). The functions \(\psi_i\) are homogeneous of the degree \(q\), so
\[
x\cdot\nabla\psi_i=q\,\psi_i,\qquad H_i\,x=(q-1)\,\nabla\psi_i .
\]
These two formulas are called the homogeneity relations below.

Assume the hypothesis (M) of the lesson on moment coordinates. It gives an even function \(\varphi\) such that \((V,\varphi)\) is a moment pair with \(\tau=D^2\varphi\le\tfrac4\varepsilon I\). We use the notation of that lesson: \(M=\tau^{-1}\), the operator \(A\), and for a smooth \(f\) with compact support the fields \(B\), \(W\) and \(u=A(A-1)f\). Expectations are means for \(\mu\).

## 2. The functions \(\psi_i\) in moment coordinates

**Lemma 2.1.** \(\mathbb E\operatorname{tr}(\tau H_i)=\mathbb E\,x\cdot\nabla\psi_i=q\,a_i\).

**Proof.** The second equality is the first homogeneity relation. For the first, let \(\eta_r\) be the cutoff functions of the lesson on the density of the even tests. By Lemma 2.1 (4) of the lesson on moment coordinates, applied to \(g=\eta_r\,\partial_{x_j}\psi_i\) and summed over \(j\),
\[
\begin{aligned}
\mathbb E\,\eta_r\,x\cdot\nabla\psi_i&=\mathbb E\,\eta_r\operatorname{tr}(\tau H_i)\\
&\quad+\mathbb E\,\nabla\psi_i\cdot\tau\nabla\eta_r .
\end{aligned}
\]
The last term is at most \(\tfrac4\varepsilon\tfrac{c_1}r\,\mathbb E|\nabla\psi_i|\) in absolute value and tends to \(0\) as \(r\to\infty\). In the other two terms the integrands are bounded by integrable functions, since \(\tau\) is bounded and \(H_i\), \(x\cdot\nabla\psi_i\) are polynomials; so they converge to the means without \(\eta_r\). \(\blacksquare\)

Write \(m_i=\mathbb E\operatorname{tr}(\tau H_i)=q\,a_i\).

## 3. The bound on the test functions

**Proposition 3.1.** Assume (M). Let \(f\) be smooth with compact support, \(u=A(A-1)f\), and \(d_i=\mathbb E\,u\,\psi_i\). Then
\[
\sum_{i=1}^N\frac{d_i^2}{a_i}\ \le\ \mathbb E\,u^2 .
\]

**Proof.** By Proposition 4.1 (2) of the lesson on moment coordinates with \(F=\psi_i\),
\[
d_i=\mathbb E\,W\cdot\nabla\psi_i=\mathbb E\operatorname{tr}(BH_i).
\]
*First inequality.* Let \(G_1=H_i^{1/2}\tau^{1/2}\) and \(G_2=H_i^{1/2}BM^{1/2}\). Then \(\operatorname{tr}(G_1^TG_2)=\operatorname{tr}(H_iB)\), \(\|G_1\|^2=\operatorname{tr}(\tau H_i)\) and \(\|G_2\|^2=\operatorname{tr}(MBH_iB)\). The inequality of Cauchy and Schwarz, for the trace and for the mean, gives
\[
d_i^2\ \le\ m_i\;\mathbb E\operatorname{tr}(MBH_iB).
\]
*Second inequality.* By the homogeneity relations and Lemma 2.1,
\[
\begin{aligned}
\mathbb E\,x^TH_ix&=(q-1)\,\mathbb E\,x\cdot\nabla\psi_i\\
&=(q-1)\,m_i,\\
\mathbb E\,x^TH_iW&=(q-1)\,\mathbb E\,\nabla\psi_i\cdot W\\
&=(q-1)\,d_i .
\end{aligned}
\]
The form \((X,Y)\mapsto\mathbb E\,X^TH_iY\) is positive semidefinite, so \((\mathbb E\,x^TH_iW)^2\le\mathbb E\,x^TH_ix\cdot\mathbb E\,W^TH_iW\), that is,
\[
\mathbb E\,W^TH_iW\ \ge\ (q-1)\,\frac{d_i^2}{m_i}.
\]
*The tensor estimate.* By Theorem 1.1 of the lesson on the tensor estimate, \(\mathbb E\,u^2\ge\mathbb E\operatorname{tr}(MBHB)+\mathbb E\,W^THW\). Both terms are linear in \(H=\varepsilon I+\sum_iH_i\), and the part of \(\varepsilon I\) is not negative: \(\operatorname{tr}(MB^2)=\|BM^{1/2}\|^2\) and \(W^TW\ge0\). So
\[
\begin{aligned}
\mathbb E\,u^2&\ge\sum_i\mathbb E\operatorname{tr}(MBH_iB)\\
&\quad+\sum_i\mathbb E\,W^TH_iW\\
&\ge\sum_i\Bigl(\frac{d_i^2}{m_i}+(q-1)\frac{d_i^2}{m_i}\Bigr)\\
&=\sum_i\frac{q\,d_i^2}{m_i}=\sum_i\frac{d_i^2}{a_i}.
\end{aligned}
\]
\(\blacksquare\)

The two inequalities bound the same number \(d_i\) in two ways, through the second derivatives of \(\psi_i\) and through the first. Their sum gives the factor \(q\), which is exactly the factor between \(m_i\) and \(a_i\).

## 4. The variance bound

**Theorem 4.1.** Assume (M) and (ER). Then the variance bound holds in every dimension \(n\ge2\): for all real \(b_1,\dots,b_N\),
\[
\operatorname{Var}_\mu\Bigl(\sum_{i=1}^Nb_i\psi_i\Bigr)\ \le\ \sum_{i=1}^Nb_i^2\,\mathbb E_\mu\psi_i .
\]

**Proof.** Let \(u\in L^2(\mu)\) be even with \(\mathbb E\,u=0\). By Theorem 1.1 of the lesson on the density of the even tests, with \(\Lambda=4/\varepsilon\), there are even smooth functions \(f_m\) with compact support such that \(u_m=A(A-1)f_m\to u\) in \(L^2(\mu)\). The functions \(\psi_i\) are in \(L^2(\mu)\), so \(\mathbb E\,u_m\psi_i\to\mathbb E\,u\,\psi_i\), and Proposition 3.1 passes to the limit:
\[
\sum_i\frac{(\mathbb E\,u\,\psi_i)^2}{a_i}\ \le\ \mathbb E\,u^2 .
\]
Now let \(F=\sum_ib_i\psi_i\) and \(u=F-\mathbb E\,F\). This function is even, because \(q\) is even, and it has the mean \(0\). With \(d_i=\mathbb E\,u\,\psi_i\),
\[
\begin{aligned}
\mathbb E\,u^2&=\mathbb E\,u\,F=\sum_ib_id_i\\
&\le\Bigl(\sum_ib_i^2a_i\Bigr)^{1/2}\Bigl(\sum_i\frac{d_i^2}{a_i}\Bigr)^{1/2}\\
&\le\Bigl(\sum_ib_i^2a_i\Bigr)^{1/2}\bigl(\mathbb E\,u^2\bigr)^{1/2}.
\end{aligned}
\]
So \(\mathbb E\,u^2\le\sum_ib_i^2a_i\), and \(\mathbb E\,u^2\) is the variance of \(F\). \(\blacksquare\)

## 5. The inequality

**Theorem 5.1.** Assume (M) and (ER). Then for every \(n\ge1\), all convex bodies \(K=-K\), \(L=-L\) in \(\mathbb R^n\) and all \(0\le\lambda\le1\),
\[
\Bigl|\mathcal W\bigl[h_K^{1-\lambda}h_L^\lambda\bigr]\Bigr|\ \ge\ |K|^{1-\lambda}\,|L|^\lambda ,
\]
and for \(0<p<1\) the additive inequality of Corollary 6.1 of the first lesson holds.

**Proof.** Theorem 4.1, and Theorem 2.2 and Corollary 6.1 of the lesson on Wulff bodies. \(\blacksquare\)

What the course proves and what it assumes: the reduction to the variance bound, the identities in moment coordinates, the tensor estimate, the density argument and the two inequalities of this lesson are proved in the course. The existence of the moment coordinates with the bound \(\tau\le4/\varepsilon\), and the smoothness of weak solutions of an elliptic equation of order four, are taken from the literature, as in [OpenAI-L].

[OpenAI-L, Section 8.2] also deduces the same inequality for every even log-concave measure in place of the volume, and the statement that \(t\mapsto\mu(e^tK)\) is log-concave for such a measure \(\mu\) and a symmetric convex body \(K\). This uses a theorem of C. Saroglou and a theorem of C. Borell and is not part of the course.

## 6. The exponent 2

For \(q=2\) the measure \(\mu\) is Gaussian, and the variance bound can be proved directly.

**Proposition 6.1.** The variance bound holds for \(q=2\) in every dimension \(n\ge1\), without any hypothesis.

**Proof.** Let \(\alpha_i=p_i/h_i\), so \(\psi_i=\langle\alpha_i,x\rangle^2\) and \(V=\tfrac12x^T\Sigma^{-1}x\) with
\[
\Sigma^{-1}=\varepsilon I+2\sum_i\alpha_i\alpha_i^T .
\]
So \(\mu\) is the centered Gaussian measure with the covariance matrix \(\Sigma\). For two linear functions, \(\mathbb E\,\langle\alpha,x\rangle\langle\beta,x\rangle=\alpha^T\Sigma\beta\), and by Exercise 7.1 the covariance of their squares is \(2(\alpha^T\Sigma\beta)^2\). Let \(g_i=\Sigma^{1/2}\alpha_i\) and \(\Gamma_{ij}=\langle g_i,g_j\rangle\). Then \(a_i=\Gamma_{ii}\), the covariance matrix of the \(\psi_i\) has the entries \(2\Gamma_{ij}^2\), and the variance bound says that the matrix with the entries
\[
\Gamma_{ii}\,\delta_{ij}-2\,\Gamma_{ij}^2
\]
is positive semidefinite. Multiply the formula for \(\Sigma^{-1}\) from both sides by \(\Sigma^{1/2}\): \(I=\varepsilon\Sigma+2\sum_ig_ig_i^T\). So \(2\sum_ig_ig_i^T\le I\). If \(\mathsf G\) is the matrix with the columns \(g_i\), this says \(2\mathsf G\mathsf G^T\le I\), and then also \(2\mathsf G^T\mathsf G=2\Gamma\le I\), because \(\mathsf G\mathsf G^T\) and \(\mathsf G^T\mathsf G\) have the same eigenvalues different from \(0\). The matrices \(I-2\Gamma\) and \(\Gamma\) are positive semidefinite. So is the matrix of the products of their entries, by Exercise 7.2, and its entries are \((\delta_{ij}-2\Gamma_{ij})\Gamma_{ij}\). \(\blacksquare\)

## 7. Exercises

**7.1.** Let \(X,Y\) be centered jointly Gaussian variables with the variances \(s^2,t^2\) and the covariance \(c\). Show that \(\mathbb E\,X^2Y^2=s^2t^2+2c^2\), so that the covariance of \(X^2\) and \(Y^2\) is \(2c^2\).

**7.2.** Let \(P\) and \(\Gamma\) be positive semidefinite matrices of the same size. Show that the matrix with the entries \(P_{ij}\Gamma_{ij}\) is positive semidefinite.

**7.3.** Show that the bound \(\sum_i(\mathbb E\,u\,\psi_i)^2/a_i\le\mathbb E\,u^2\) of the proof of Theorem 4.1 holds for every \(u\in L^2(\mu)\) with mean \(0\), even or not.

**7.4.** Let \(n=1\) and \(V=\psi=x^2\) (one function, \(q=2\), and \(\varepsilon=0\); the density \(e^{-x^2}\) is integrable). Use the Gaussian pair of Example 1.2 of the lesson on moment coordinates with \(a=\tfrac12\), for which \(\tau=\tfrac12\), and \(f=x^2\). Compute \(a_1\), \(m_1\), \(u\), \(W\), \(B\) and \(d_1\), and check the two inequalities of the proof of Proposition 3.1 and its conclusion. (For polynomials and a Gaussian measure the integrations by parts are valid without compact support.)

## 8. Solutions

**7.1.** If \(s=0\) both sides are \(0\). Otherwise \(R=Y-\tfrac c{s^2}X\) is Gaussian and uncorrelated with \(X\), hence independent of \(X\), with the variance \(t^2-c^2/s^2\). Then \(\mathbb E\,X^2Y^2\) is \(\tfrac{c^2}{s^4}\mathbb E\,X^4+\mathbb E\,X^2\,\mathbb E\,R^2\), since the mixed term has the mean \(0\); with \(\mathbb E\,X^4=3s^4\) this is \(3c^2+s^2t^2-c^2\).

**7.2.** Write \(\Gamma=\sum_k\lambda_kv_kv_k^T\) with \(\lambda_k\ge0\). The matrix with the entries \(P_{ij}(v_k)_i(v_k)_j\) is \(D_kPD_k\), where \(D_k\) is the diagonal matrix of the vector \(v_k\); it is positive semidefinite. The matrix in question is the sum of these with the weights \(\lambda_k\).

**7.3.** Let \(u_0(x)=\tfrac12(u(x)+u(-x))\). Since \(\mu\) and \(\psi_i\) are even, \(\mathbb E\,u\,\psi_i=\mathbb E\,u_0\psi_i\), \(\mathbb E\,u_0=0\), and \(\mathbb E\,u_0^2\le\mathbb E\,u^2\). Apply the bound to the even function \(u_0\).

**7.4.** \(\mu\) is the Gaussian measure with the variance \(\tfrac12\), so \(\mathbb E\,x^2=\tfrac12\) and \(\mathbb E\,x^4=\tfrac34\). \(a_1=\tfrac12\), \(H_1=2\), \(m_1=\mathbb E\,\tau H_1=1=q\,a_1\). Here \(A=x\,\partial_x-\tfrac12\partial_x^2\). For \(f=x^2\): \(h=2\), \(B=\tau h\tau=\tfrac12\), \(Af=2x^2-1\), \(Af-f=x^2-1\), \(W=\tau\,\partial_x(x^2-1)=x\), and \(u=A(x^2-1)=2x^2-1\). Then \(d_1=\mathbb E\,(2x^2-1)x^2=\tfrac32-\tfrac12=1\); also \(\mathbb E\,W\psi'=\mathbb E\,2x^2=1\) and \(\mathbb E\,BH_1=1\). First inequality: \(\mathbb E\,MBH_1B=2\cdot\tfrac12\cdot2\cdot\tfrac12=1\) and \(d_1^2/m_1=1\). Second: \(\mathbb E\,WH_1W=2\,\mathbb E\,x^2=1\) and \((q-1)d_1^2/m_1=1\). Conclusion: \(\mathbb E\,u^2=4\cdot\tfrac34-4\cdot\tfrac12+1=2\) and \(d_1^2/a_1=2\). All three are equalities, in agreement with Exercise 7.2 of the first lesson, where the variance bound for one direction and \(\varepsilon=0\) is an equality.

## References

- [OpenAI-L] OpenAI, *The logarithmic Brunn-Minkowski conjecture*, OpenAI Math Release preprint, 23 September 2026, Sections 7 and 8. https://github.com/openai/math/tree/main/preprints/The-logarithmic-Brunn-Minkowski-conjecture-September-23-2026
