# Compact spectral decompositions and Schatten estimates

The operators act on complex Hilbert spaces, possibly nonseparable. Inner products are linear in the first variable. Bounded operators are everywhere defined. The Hilbert projection, orthonormal-basis, positive-root and bounded trace foundations used below are proved in [Bounded trace foundations, AN03-TRC-001–003](../reader/dependency-trace-ideals.html#AN03-TRC-001). The real Hahn–Banach extension used in Lemma 9.4 has its complete proof in [Banach foundations, Section 5](../reader/dependency-banach-foundations.html#section-5). Both are retained independently written programme proofs. The original programme expression is dedicated under CC0 1.0 Universal, to the extent rights are held.

<a id="spectral-decomposition-and-schatten-estimates"></a>

## Spectral decomposition and Schatten estimates

**Lemma 9.1 (compact positive operators).** A positive compact operator \(K\) has an orthonormal basis of its kernel and its positive eigenspaces. Its nonzero eigenvalues have finite multiplicity and tend to zero if there are infinitely many.

**Proof.** Positivity of the form \(\langle Kx,y\rangle\) and scalar quadratic minimization give
\[
|\langle Kx,y\rangle|^2\leq\langle Kx,x\rangle\langle Ky,y\rangle .
\]
Writing \(a=\sup_{\|x\|=1}\langle Kx,x\rangle\), taking the supremum over unit \(y\) proves
\(\|Kx\|^2\leq a\langle Kx,x\rangle\). Thus \(a=\|K\|\).
If \(a>0\), choose unit \(x_j\) with \(\langle Kx_j,x_j\rangle\to a\). Then
\[
\|(K-a)x_j\|^2
\leq a^2-a\langle Kx_j,x_j\rangle\longrightarrow0.
\tag{9.1}
\]
Compactness gives a convergent subsequence of \(Kx_j\); (9.1) then gives convergence of that subsequence of \(x_j\) to a unit eigenvector with eigenvalue \(a\).

The orthogonal complement of an eigenspace is invariant under \(K\), by selfadjointness. Repeat the construction there. An infinite orthonormal family of eigenvectors with eigenvalues bounded below by \(\varepsilon>0\) would have images at pairwise distance at least \(\sqrt2\varepsilon\), contradicting compactness. This proves finite multiplicity away from zero and convergence of the selected eigenvalues to zero. If \(K\) were nonzero on the orthogonal complement of all selected eigenspaces, the same maximum argument would produce a positive eigenvalue there. Every previously selected maximum would be at least that value, giving the contradiction just proved. The remaining complement is therefore the kernel. Choose an orthonormal basis in that closed subspace. This proves the result, including finite rank and \(K=0\). \(\square\)

Apply this to \(T^*T\) for compact \(T\). On an eigenvector with eigenvalue \(\mu^2>0\), put \(Ve=T e/\mu\). These images are orthonormal, since
\(\langle Te,Tf\rangle=\langle T^*Te,f\rangle\). Extend \(V\) by zero on the kernel. It is a partial isometry and \(T=V|T|\), where \(|T|\) multiplies those eigenvectors by \(\mu\). This is the compact polar decomposition used below.

**Lemma 9.2 (a compact-resolvent spectral core).** A selfadjoint \(D\) with compact resolvent has an orthonormal eigenbasis \((e_j)\), with real eigenvalues \(d_j\). Each bounded interval contains only finitely many eigenvalues, counted with multiplicity, and
\[
\operatorname{Dom}D
=\left\{x:\sum_j |d_j|^2|\langle x,e_j\rangle|^2<\infty\right\}.
\tag{9.2}
\]
Finite spectral sums are dense in this domain with its graph norm.

**Proof.** An adjoint is closed. Indeed, if \(y_n\in\operatorname{Dom}D^*\), \(y_n\to y\) and \(D^*y_n\to z\), then for every \(x\in\operatorname{Dom}D\),
\[
\langle Dx,y\rangle
=\lim_n\langle Dx,y_n\rangle
=\lim_n\langle x,D^*y_n\rangle
=\langle x,z\rangle.
\]
This is the adjoint-domain condition: \(y\in\operatorname{Dom}D^*\) and \(D^*y=z\). Density of \(\operatorname{Dom}D\) gives uniqueness of the representing vector. Since selfadjointness means \(D=D^*\) with equality of domains, \(D\) is closed.

For either sign,
\(\|(D\pm i)x\|^2=\|Dx\|^2+\|x\|^2\). The range is closed, using closedness of \(D\), and its orthogonal complement is \(\ker(D\mp i)=0\), using the adjoint definition. Thus \(D\pm i\) are bijective with bounded inverses. Their resolvent identity shows that these inverses commute. Put
\[
R=(D-i)^{-1}(D+i)^{-1}.
\]
Then \(R=(D+i)^{-1*}(D+i)^{-1}\) is positive, injective and compact. The identity \(D(D\pm i)^{-1}=I\mp i(D\pm i)^{-1}\) shows that its range is exactly \(\operatorname{Dom}D^2\) and that \(R=(1+D^2)^{-1}\) there.

Lemma 9.1 decomposes \(H\) into the finite-dimensional positive eigenspaces of \(R\); there is no kernel. Every such eigenspace lies in \(\operatorname{Dom}D^2\). The resolvent identities imply \(DRx=RDx\) for \(x\in\operatorname{Dom}D\), so \(D\) preserves each of them. Its restriction is a bounded Hermitian matrix: in an orthonormal basis, Cauchy–Schwarz bounds its norm by the square root of the sum of the squared norms of the images. Add that norm times the identity to make it positive. Lemma 9.1 applies in this finite-dimensional space; subtracting the same scalar gives a real eigenbasis for the original restriction. If \(De_j=d_je_j\), then \(Re_j=(1+d_j^2)^{-1}e_j\). Compactness of \(R\) proves the bounded-interval assertion.

For \(x\in\operatorname{Dom}D\), selfadjointness gives the coordinate of \(Dx\) as \(d_j\langle x,e_j\rangle\), so (9.2) is necessary by Parseval. Conversely that condition makes the images of the finite partial sums converge in \(H\). Closedness of \(D\) puts their limit in its domain and identifies its image with that coordinate sequence. The same argument proves graph density. Every scalar function of \(D\) consequently has its indicated square-sum domain, and the spectral cutoffs used in the corresponding spectral domains converge in every graph norm on which the vector belongs. \(\square\)

For the decreasing singular values obtained from the compact decomposition, including a zero tail after finite rank, one has
\[
\mu_j(T)=\inf_{\operatorname{rank}R\leq j}\|T-R\|.
\tag{1.1}
\]
The rank-\(j\) singular truncation proves the upper bound. For any rank-at-most-\(j\) map \(R\), its restriction to the span of the first \(j+1\) singular vectors has a nonzero kernel vector, by rank-nullity. On a unit vector there, \(\|(T-R)x\|=\|Tx\|\geq\mu_j(T)\). If the displayed singular value is zero, the lower bound is automatic. This proves the formula. Taking approximants and the triangle inequality gives \(|\mu_j(S)-\mu_j(T)|\leq\|S-T\|\). Multiplying the finite-rank approximants by a bounded map on either side gives both ideal inequalities used below.

For \(0<p<\infty\), define
\[
\mathcal S^p=\{T\text{ compact}:\sum_j\mu_j(T)^p<\infty\},
\qquad \|T\|_p=\left(\sum_j\mu_j(T)^p\right)^{1/p}.
\]
Use \(\mathcal S^\infty=B(H)\) and \(\|T\|_\infty=\|T\|\). For \(p=1\), (T6) of AN03-TRC-002 applied in the singular eigenbasis identifies this quantity with its trace norm. For \(p=2\), Parseval identifies it with the Hilbert-Schmidt norm there. We need normed ideals for \(p\geq1\); the product estimate itself also makes sense below one.

**Theorem 9.3 (Schatten Hölder).** If \(0<p,q,r\leq\infty\) and
\(1/r=1/p+1/q\), with \(1/\infty=0\), then
\[
\|AB\|_r\leq\|A\|_p\|B\|_q.
\tag{9.3}
\]
At least one finite exponent ensures compactness of the product. When both exponents are infinite, (9.3) is ordinary operator submultiplicativity.

**Proof.** First use finite-rank operators in a common finite-dimensional space. On its \(k\)-th exterior power, the singular decomposition gives
\[
\|\wedge^kT\|=\prod_{j<k}\mu_j(T),\qquad
\wedge^k(AB)=(\wedge^kA)(\wedge^kB).
\]
Indeed the wedge products of distinct orthonormal singular vectors form orthonormal systems, and the largest coefficient is the product of the \(k\) largest singular values. Operator submultiplicativity therefore yields
\[
\prod_{j<k}\mu_j(AB)\leq
\prod_{j<k}\mu_j(A)\mu_j(B)\qquad(k\geq1).
\tag{9.4}
\]

Here is the precise passage from products to sums. If decreasing real vectors \(u,v\) satisfy \(\sum_{j<k}u_j\leq\sum_{j<k}v_j\) for every \(k\), then for every real \(t\)
\[
\sum_j(u_j-t)_+
=\max_{k\geq0}\sum_{j<k}(u_j-t)
\leq\max_{k\geq0}\sum_{j<k}(v_j-t)
=\sum_j(v_j-t)_+.
\]
For \(r>0\), multiply by \(r^2e^{rt}\) and integrate over \(t\in\mathbb R\). The identity
\(\int_{-\infty}^w r^2e^{rt}(w-t)\,dt=e^{rw}\) proves
\(\sum_j e^{ru_j}\leq\sum_j e^{rv_j}\).
Apply this to
\(u_j=\log\mu_j(AB)\), \(v_j=\log(\mu_j(A)\mu_j(B))\), using (9.4).
Zeros cause no difficulty: discard the zero tail of the latter product vector, on which the product has rank zero by the rank inequality; replace any remaining zero in the former vector by a sufficiently small positive number. All prefix inequalities still hold, and passage of that number to zero gives
\[
\sum_j\mu_j(AB)^r
\leq\sum_j(\mu_j(A)\mu_j(B))^r.
\tag{9.5}
\]

If \(p,q\) are finite, ordinary sequence Hölder with exponents \(p/r,q/r\) bounds the right side by \(\|A\|_p^r\|B\|_q^r\).
To recall its proof, normalize the two nonnegative power sums to one and apply
\(ab\leq a^P/P+b^Q/Q\), \(1/P+1/Q=1\), term by term. This scalar inequality follows by minimizing \(a^P/P-ab+b^Q/Q\) in \(a\). Zero norms are immediate.

Finite-rank singular truncations \(A_n,B_n\) converge in operator norm and in their respective finite-exponent quantities. Their products converge in operator norm to \(AB\). Formula (1.1) gives
\(|\mu_j(S)-\mu_j(T)|\leq\|S-T\|\), so each product singular value converges. Taking every finite partial sum in (9.5) and then its supremum proves (9.3) for compact \(A,B\).
For a bounded factor, (1.1) gives directly
\(\mu_j(AB)\leq\|A\|\mu_j(B)\) and
\(\mu_j(BA)\leq\|A\|\mu_j(B)\), by multiplying finite-rank approximants. These prove the infinite-exponent cases. \(\square\)

Iteration gives the corresponding estimate for any finite product, including bounded factors. In particular, if \(s_j\geq0\), \(\sum_j s_j=1\), and \(e^{-uD^2}\) is trace class, then
\[
\left\|a_0e^{-us_0D^2}a_1e^{-us_1D^2}\cdots
 a_ne^{-us_nD^2}\right\|_1
\leq\left(\prod_{j=0}^n\|a_j\|\right)
 \operatorname{Tr}(e^{-uD^2}).
\tag{9.6}
\]
For \(s_j>0\), its heat factor has Schatten exponent \(1/s_j\) and norm
\((\operatorname{Tr}e^{-uD^2})^{s_j}\). For \(s_j=0\), it is the identity with operator norm one. Thus (9.6) holds also on the boundary of the simplex, with constant one. This proves the trace-ideal estimate whenever its explicit trace-class heat hypothesis holds.

For completeness, \(\mathcal S^p\) is a Banach ideal when \(1\leq p<\infty\). Hölder and bounded trace duality give
\[
\|T\|_p=\sup_{\substack{X\text{ finite rank}\\\|X\|_{p'}\leq1}}
 |\operatorname{Tr}(TX)|,\qquad 1/p+1/p'=1.
\tag{9.7}
\]
For the reverse inequality when \(p>1\), take \(T=V|T|\) and test with
\(|T|^{p-1}P_N V^*/(\sum_{j<N}\mu_j(T)^p)^{1/p'}\); let \(N\to\infty\). For \(p=1\), test with \(P_NV^*\). Zero partial sums are omitted. Formula (9.7) proves the triangle inequality. A Cauchy sequence in this norm is Cauchy in operator norm and has a compact operator limit. Continuity of each singular value and finite partial sums show
\(\|T-T_n\|_p\leq\liminf_m\|T_m-T_n\|_p\), which proves convergence in the ideal norm and completeness. Bounded left and right multiplication obey (9.3). These facts justify trace-norm limits and integrals under their stated integrability hypotheses.

**Lemma 9.4 (the extension used to construct a state).** A bounded real linear functional on a subspace of a real normed space has an extension with the same norm. In particular, the ordinary limit on convergent sequences extends to a positive unital complex functional of norm one on \(\ell^\infty\).

**Proof.** The norm-preserving extension theorem is proved in [Banach foundations](../reader/dependency-banach-foundations.html#section-5), Section 5. Its proof uses the explicitly stated Zorn choice principle and a one-dimensional extension interval; no completeness or closedness of the subspace is required. Apply its real form to the limit functional on real convergent sequences. We prove the positive unital extension here.

For the limit functional \(l\) on real convergent sequences, this gives \(l(1)=\|l\|=1\) on real \(\ell^\infty\). If \(0\leq x\leq1\), then
\(l(x)=1-l(1-x)\geq0\); rescaling proves positivity for every bounded nonnegative sequence. Complexify by
\(L(x+iy)=l(x)+il(y)\). This is complex linear and positive. If \(L(z)\ne0\), choose a scalar \(c\) of modulus one with \(cL(z)=|L(z)|\). Then
\[
|L(z)|=l(\operatorname{Re}(cz))\leq\|z\|_\infty.
\]
Thus its complex norm is one and it extends the complex ordinary limit. This proves the asserted positive unital extension. \(\square\)
