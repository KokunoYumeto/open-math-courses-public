# The lower bound for perfect matching

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson proves Theorem 4.3 and Corollary 4.4 of [PSD factorizations and semidefinite lifts](psd-factorizations-and-semidefinite-lifts.md): the shifted matching matrices \(A_n(\rho)\), \(0<\rho<1\), have PSD rank \(2^{\Omega(n)}\), and every semidefinite lift of the perfect matching polytope has size \(2^{\Omega(n)}\) [OpenAI-PSD, Section 6]. The three ingredients are the local averaging theorem of [Averaging within a cell](averaging-within-a-cell.md), the Fourier smoothing theorem of [Fourier smoothing of matrix squares](fourier-smoothing-of-matrix-squares.md), and the separating functional of [An expanding parity system](an-expanding-parity-system.md). The vertices of the expanding graph become cells of vertices of \(K_n\), and averaging a row factor within the cells realizes the parity disagreement function exactly.

- The constants (Section 1).
- Realizing the parity system by odd cuts and matchings (Section 2).
- Proof of the main theorem (Section 3).
- Semidefinite lifts (Section 4).

## 1. The constants

Use the constants \(d=100\), \(\beta=1/100\) and \(\tau=1/1000\) of [An expanding parity system](an-expanding-parity-system.md), put \(L=2^{d-1}\), and let \(C_L=2^{L-1}\) be the constant of the splitting lemma. Choose \(\lambda>1\) with
\[
\lambda^\tau\ge64L^4 .
\tag{1.1}
\]
Let \(\theta_d(k)\) be as in Theorem 5.1 of [Averaging within a cell](averaging-within-a-cell.md). Since \(\theta_d(k)\to0\), we can fix an even integer \(k\), satisfying the size condition of that theorem, with
\[
L\lambda^2C_L\,\theta_d(k)\le1 .
\tag{1.2}
\]
These constants are absolute: they do not depend on \(n\) or on \(\rho\). They are very large, and the rate \(c=1/(2k)\) obtained below is correspondingly small.

## 2. Realizing the parity system by odd cuts and matchings

Let \(n\) be even and large, and let \(t\) be the largest even integer with \(kt\le n\), so that
\[
kt\le n<k(t+2).
\tag{2.1}
\]
Assume \(t\ge1000\). Let \(H\) be a bipartite \(d\)-regular multigraph on \([t]\) as in Lemma 1.2 of [An expanding parity system](an-expanding-parity-system.md), with ordered incidences, and with bits \(b_i\in\{0,1\}\) of which exactly one equals one. For \(e=uv\in E(H)\), let \(j_u(e)\) and \(j_v(e)\) be its positions at \(u\) and at \(v\).

*Cells and cuts.* Choose disjoint subsets \(C_1,\ldots,C_t\) of \([n]\) with \(k\) elements each, the *cells*. The remaining \(n-kt\) vertices are even in number; pair them by a fixed perfect matching \(M_{\mathrm{rest}}\). In cell \(i\), let \(w_i\in\{k/2,k/2+1\}\) have the parity of \(b_i\), and let \(X_i\) be the set of subsets of \(C_i\) with \(w_i\) elements. For \(a=(a_1,\ldots,a_t)\in\prod_iX_i\) put
\[
U(a)=a_1\cup\cdots\cup a_t .
\]
Since \(|U(a)|=\sum_iw_i\equiv\sum_ib_i=1\pmod2\), the set \(U(a)\) is odd.

*Matchings.* Identify each cell with \([k]\), and let \(\mathcal M_i\) be the set of local column data of Section 1 of [Averaging within a cell](averaging-within-a-cell.md) for the cell \(C_i\): terminals \(v^i_1,\ldots,v^i_d\in C_i\) and a perfect matching of the other vertices of \(C_i\). For \(m=(m_1,\ldots,m_t)\in\prod_i\mathcal M_i\), let \(M(m)\) consist of

- for each edge \(e=uv\) of \(H\), the edge of \(K_n\) joining the terminals \(v^u_{j_u(e)}\) and \(v^v_{j_v(e)}\);
- the internal pairs of every \(m_i\);
- the edges of \(M_{\mathrm{rest}}\).

The \(d\) terminals of cell \(i\) correspond to the \(d\) incidences at the vertex \(i\), and every incidence belongs to exactly one edge of \(H\); so every vertex of \(K_n\) lies in exactly one edge of \(M(m)\), and \(M(m)\) is a perfect matching. Parallel edges of \(H\) use different positions, hence different terminals. Different local data may give the same matching; this does no harm.

*Restrictions.* Let \(Y_i\subseteq\{0,1\}^d\) be the assignments of parity \(b_i\), as in (2.1) of [An expanding parity system](an-expanding-parity-system.md); it is the set \(Y_{b_i}\) of [Averaging within a cell](averaging-within-a-cell.md). For \(y=(y_1,\ldots,y_t)\in\prod_iY_i\) and \(m\in\prod_i\mathcal M_i\), let \(\pi^{m_i}_{y_i}\) be the probability measure of that lesson on \(X_i\), and put \(f=f_\varepsilon\) with \(\varepsilon=1-\rho\), as in (2.2) of the parity lesson.

**Lemma 2.1** (realization). If every \(a_i\) lies in the support of \(\pi^{m_i}_{y_i}\), then
\[
|M(m)\cap\delta(U(a))|-1+\rho=f(y).
\]

*Proof.* An internal pair of \(m_i\) has equal values of \(\mathbf 1_{a_i}\), so its two vertices are both in \(U(a)\) or both outside, and the pair does not cross \(\delta(U(a))\). The vertices outside the cells are not in \(U(a)\), so \(M_{\mathrm{rest}}\) does not cross either. The edge for \(e=uv\) has the endpoint \(v^u_{j_u(e)}\in C_u\), which lies in \(U(a)\) exactly when \(y_{u,j_u(e)}=y_{u,e}=1\), and likewise at \(v\). So it crosses exactly when \(y_{u,e}\ne y_{v,e}\), and
\[
\begin{aligned}&|M(m)\cap\delta(U(a))|-1+\rho\\&\quad=\sum_{e=uv}\mathbf 1_{\{y_{u,e}\ne y_{v,e}\}}-(1-\rho)\\&\quad=f(y). \qquad\square\end{aligned}
\]

## 3. Proof of the main theorem

*Proof of Theorem 4.3 of [PSD factorizations and semidefinite lifts](psd-factorizations-and-semidefinite-lifts.md).* Fix \(0<\rho<1\), put \(\varepsilon=1-\rho\), and let \(n\) be even and so large that the \(t\) of (2.1) satisfies \(t\ge1000\). Suppose that \(A_n(\rho)\) has a PSD factorization of size at most \(2^t\). We derive a contradiction when \(n\) is large enough in terms of \(\rho\).

*A normalized factorization.* The entries of \(A_n(\rho)\) are positive and at most \(n/2\le n\). Lemma 2.3 of [PSD factorizations and semidefinite lifts](psd-factorizations-and-semidefinite-lifts.md) gives a factorization of some size \(r\le2^t\) with
\[
\operatorname{tr}F_U\le n,\qquad\operatorname{tr}G_M\le r .
\]
Put \(F(a)=F_{U(a)}\) for \(a\in\prod_iX_i\), and for \(m\in\prod_i\mathcal M_i\)
\[
\overline F_m(y)=\sum_a\Bigl(\prod_{i=1}^t\pi^{m_i}_{y_i}(a_i)\Bigr)F(a).
\]
Each \(a\) with a nonzero coefficient satisfies Lemma 2.1, and the coefficients are probabilities, so
\[
\begin{gathered}\operatorname{tr}\bigl(\overline F_m(y)\,G_{M(m)}\bigr)=f(y)\\ \bigl(y\in\textstyle\prod_iY_i\bigr).\end{gathered}\tag{3.1}
\]

*Fourier smoothing.* Identify each \(Y_i\) with \(\mathbb F_2^{d-1}\) through its first \(d-1\) bits; the characters of [Fourier smoothing of matrix squares](fourier-smoothing-of-matrix-squares.md), with \(a=d-1\), are then the characters \(\chi_p\) of the parity lesson. Theorem 5.1 of [Averaging within a cell](averaging-within-a-cell.md) gives the hypotheses (2.1) and (2.2) of Theorem 2.1 of the smoothing lesson with \(\theta=\theta_d(k)\), since \(\mathbb E|B-\mathbb E B|^2\le\mathbb E B^2\); and (1.2) is its condition (2.3). That theorem, with \(B=n\), gives some \(m\) and functions \(H_q\colon\prod_iY_i\to\mathbb R^{R\times r}\), \(q\in\Lambda^t\), with
\[
\begin{aligned}&\overline F_m(y)\\&\quad=\sum_qH_q(y)^{\mathsf T}H_q(y),\end{aligned}\tag{3.2}
\]
\[
\begin{aligned}&\sum_{q,p}\lambda^{\operatorname{dist}(q,p)}\|\widehat H_{q,p}\|_{\mathrm F}^2\\&\quad\le L^t\sqrt r\,n\,2^{t/2}.\end{aligned}\tag{3.3}
\]
Fix these data and put \(G=G_{M(m)}\). Since \(\operatorname{tr}(H^{\mathsf T}HG)=\operatorname{tr}(G^{1/2}H^{\mathsf T}HG^{1/2})\), (3.1) and (3.2) give
\[
f(y)=\sum_q\bigl\|H_q(y)G^{1/2}\bigr\|_{\mathrm F}^2 .
\tag{3.4}
\]

*Truncation.* Let \(D=\lfloor\tau t\rfloor\). In each branch keep the frequencies within distance \(D\) of the center:
\[
\begin{gathered}
K_q(y)=\sum_{p:\,\operatorname{dist}(q,p)\le D}\widehat H_{q,p}\,\chi_p(y),\\
f_*(y)=\sum_q\bigl\|K_q(y)G^{1/2}\bigr\|_{\mathrm F}^2 .
\end{gathered}
\]
The discarded part satisfies, for every \(y\),
\[
\begin{aligned}E(y)^2&:=\sum_q\bigl\|(H_q(y)-K_q(y))G^{1/2}\bigr\|_{\mathrm F}^2\\&\le L^t\sum_{q,\ p:\,\operatorname{dist}(q,p)>D}\bigl\|\widehat H_{q,p}G^{1/2}\bigr\|_{\mathrm F}^2\\&\le L^t\,r\,\lambda^{-\tau t}\,L^t\sqrt r\,n\,2^{t/2}\\&\le n\Bigl(\frac{4L^2}{\lambda^\tau}\Bigr)^t\le n\,(4L)^{-2t}.\end{aligned}
\]
The first inequality is the triangle inequality, \(|\chi_p|=1\), and the Cauchy–Schwarz inequality over the at most \(L^t\) frequencies of each branch. In the second, \(\|\widehat HG^{1/2}\|_{\mathrm F}^2=\operatorname{tr}(\widehat HG\widehat H^{\mathsf T})\), which is at most \(\|G\|_{\mathrm{op}}\|\widehat H\|_{\mathrm F}^2\le r\|\widehat H\|_{\mathrm F}^2\), by Lemma 1.1(3) of [PSD factorizations and semidefinite lifts](psd-factorizations-and-semidefinite-lifts.md); an integer distance larger than \(D\) is larger than \(\tau t\), so \(1\le\lambda^{\operatorname{dist}(q,p)-\tau t}\); and (3.3) applies. The last line uses \(r\le2^t\), so \(r^{3/2}2^{t/2}\le4^t\), and (1.1).

*The uniform error.* For fixed \(y\), let \(\mathbf S\) be the stack of the matrices \(H_q(y)G^{1/2}\) and \(\mathbf S_*\) that of the \(K_q(y)G^{1/2}\). Then \(f(y)=\|\mathbf S\|_{\mathrm F}^2\le n\), \(f_*(y)=\|\mathbf S_*\|_{\mathrm F}^2\) and \(\|\mathbf S-\mathbf S_*\|_{\mathrm F}=E(y)\). Since
\[
\begin{aligned}&\bigl|\|\mathbf S\|^2-\|\mathbf S_*\|^2\bigr|\\&\quad\le\|\mathbf S-\mathbf S_*\|\,(2\|\mathbf S\|+\|\mathbf S-\mathbf S_*\|),\end{aligned}
\]
the bound for \(E(y)^2\) gives
\[
\begin{gathered}\|f-f_*\|_\infty\\ \le2n(4L)^{-t}+n(4L)^{-2t}.\end{gathered}\tag{3.6}
\]

*The separating functional.* For each \(q\), the coefficients of \(K_qG^{1/2}\) vanish at the frequencies \(p\) with \(\operatorname{dist}(q,p)>D\). By Lemma 1.2 of [Fourier smoothing of matrix squares](fourier-smoothing-of-matrix-squares.md), every entry of \(\chi_qK_qG^{1/2}\) has block degree at most \(D\), and \(\|\chi_qK_qG^{1/2}\|_{\mathrm F}^2=\|K_qG^{1/2}\|_{\mathrm F}^2\). So \(f_*\) is a finite sum of squares of real functions of block degree at most \(D\). Proposition 3.1 of [An expanding parity system](an-expanding-parity-system.md) gives a functional \(\mathcal D\) with
\[
\mathcal D(f_*)\ge0,\qquad\mathcal D(f)=-\varepsilon,
\]
and, by its norm bound and (3.6),
\[
\begin{aligned}|\mathcal D(f-f_*)|&\le L^t\|f-f_*\|_\infty\\&\le2n\,4^{-t}+n\,(16L)^{-t}.\end{aligned}
\]
Hence \(-\varepsilon=\mathcal D(f_*)+\mathcal D(f-f_*)\), and this is at least \(-(2n4^{-t}+n(16L)^{-t})\). By (2.1), \(t>n/k-2\) with \(k\) fixed, so \(2n4^{-t}+n(16L)^{-t}\le3n\,4^{2-n/k}\), which is smaller than \(\varepsilon\) for all large \(n\). This contradiction shows that, for every even \(n\) beyond a threshold \(n_0(\rho)\), there is no factorization of size at most \(2^t\).

*Conclusion.* For \(n\ge4k\), (2.1) gives \(t\ge n/k-2\ge n/(2k)\). So for every even \(n\ge n_0(\rho)\), enlarged if necessary,
\[
\operatorname{rank}_{\mathrm{psd}}A_n(\rho)>2^t\ge2^{n/(2k)},
\]
which is Theorem 4.3 with \(c=1/(2k)\). The constant \(c\) does not depend on \(\rho\); only the final comparison with \(\varepsilon=1-\rho\) makes the threshold depend on \(\rho\). \(\square\)

## 4. Semidefinite lifts

*Proof of Corollary 4.4 of [PSD factorizations and semidefinite lifts](psd-factorizations-and-semidefinite-lifts.md).* Since \(A_n(\rho)=A_n(0)+\rho\mathbf 1\), Lemma 2.2(3) there gives \(\operatorname{rank}_{\mathrm{psd}}A_n(\rho)\le\operatorname{rank}_{\mathrm{psd}}A_n(0)+1\). Take \(\rho=\frac12\). For even \(n\ge n_0(\frac12)\), Theorem 4.3 gives
\[
\operatorname{rank}_{\mathrm{psd}}A_n(0)\ge2^{cn}-1 ,
\]
and \(T_n(0)\), which contains the rows of \(A_n(0)\), has at least this PSD rank by Lemma 2.2(1). Now let \(P_n\) have a semidefinite lift of size \(r\); for \(n\ge4\) it has at least two points. The affine functions \(\ell_U\), \(U\in\mathcal O_n\), of Section 4 of that lesson are nonnegative on \(P_n\), and \(\ell_U(\mathbf 1_M)=A_n(0)_{U,M}\). Proposition 3.4 there gives
\[
2^{cn}-1\le\operatorname{rank}_{\mathrm{psd}}A_n(0)\le r+1 .
\]
So \(r\ge2^{cn}-2\). For large \(n\), \(2^{cn}-2\ge2^{cn/2}\) and \(2^{cn}-1\ge2^{cn/2}\), so \(c_0=c/2\) works. \(\square\)

The argument uses no symmetry of the lift: the factors of a small factorization may be arbitrary. Symmetry enters only through the averaging operators, whose analysis in [Averaging within a cell](averaging-within-a-cell.md) uses permutations of the vertices of a cell.

## 5. Exercises

**5.1.** Show that every vertex of \(K_n\) lies in exactly one edge of \(M(m)\).

**5.2.** Show that \(\|\widehat HG^{1/2}\|_{\mathrm F}^2\le\|G\|_{\mathrm{op}}\,\|\widehat H\|_{\mathrm F}^2\) for a real matrix \(\widehat H\) with \(r\) columns and \(G\in\mathbb S^r_+\).

**5.3.** Prove
\[
\begin{aligned}&\bigl|\|\mathbf S\|^2-\|\mathbf S_*\|^2\bigr|\\&\quad\le\|\mathbf S-\mathbf S_*\|\,(2\|\mathbf S\|+\|\mathbf S-\mathbf S_*\|)\end{aligned}
\]
for vectors in a Euclidean space.

**5.4.** Show that \(2n4^{-t}+n(16L)^{-t}\le3n\,4^{2-n/k}\) when \(t>n/k-2\).

**5.5.** Where does the proof use that exactly one bit \(b_i\) equals one, and where would it fail for the endpoint \(\rho=1\)?

## 6. Solutions

**5.1.** A vertex outside the cells lies in exactly one edge of \(M_{\mathrm{rest}}\). A non-terminal vertex of a cell lies in exactly one internal pair. The terminal \(v^i_j\) corresponds to the incidence \((i,j)\), which belongs to exactly one edge \(e\) of \(H\), and \(v^i_j\) lies in the edge of \(K_n\) built from \(e\) and in no other.

**5.2.** \(\|\widehat HG^{1/2}\|_{\mathrm F}^2=\operatorname{tr}(\widehat HG\widehat H^{\mathsf T})=\sum_hhGh^{\mathsf T}\), summed over the rows \(h\) of \(\widehat H\), and \(hGh^{\mathsf T}\le\|G\|_{\mathrm{op}}\|h\|^2\).

**5.3.** The number \(\bigl|\|\mathbf S\|^2-\|\mathbf S_*\|^2\bigr|\) equals \(\bigl|\|\mathbf S\|-\|\mathbf S_*\|\bigr|\,(\|\mathbf S\|+\|\mathbf S_*\|)\), and \(\bigl|\|\mathbf S\|-\|\mathbf S_*\|\bigr|\le\|\mathbf S-\mathbf S_*\|\) and \(\|\mathbf S_*\|\le\|\mathbf S\|+\|\mathbf S-\mathbf S_*\|\).

**5.4.** \((16L)^{-t}\le4^{-t}\), so the left side is at most \(3n4^{-t}\), and \(4^{-t}<4^{2-n/k}\).

**5.5.** Oddness of \(\sum_ib_i\) makes each \(U(a)\) an odd set, so that its row exists in \(A_n(\rho)\), and makes the disagreement count odd (Lemma 2.1 of the parity lesson). At \(\rho=1\) the function \(f=f_0\) is the disagreement count itself, and \(\mathcal D(f)=0\) gives no contradiction; indeed \(\operatorname{rank}_{\mathrm{psd}}A_n(1)\le\binom n2\).

## References

- [OpenAI-PSD] OpenAI, *Exponential PSD rank of positively shifted matching matrices*, OpenAI Math Release preprint, 5 October 2026, Sections 1 and 6. https://github.com/openai/math/tree/main/preprints/Exponential-PSD-rank-of-positively-shifted-matching-matrices-October-5-2026
