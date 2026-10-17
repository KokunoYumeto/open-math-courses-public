# The numerical range and the Crouzeix inequality

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

For a normal matrix \(A\), the norm of a polynomial \(p(A)\) is the largest value of \(|p|\) on the spectrum. For a matrix that is not normal the spectrum gives no such control: a nonzero nilpotent matrix has spectrum \(\{0\}\), while \(p(A)\) can be large for polynomials that are small at \(0\). The *numerical range* \(W(A)=\{u^*Au:\|u\|=1\}\), a compact convex set containing the spectrum, does give a universal bound. Crouzeix proved in 2007 that \(\|p(A)\|\le11.08\max_{W(A)}|p|\) and conjectured that the constant \(2\) holds; Crouzeix and Palencia lowered the constant to \(1+\sqrt2\) [CP], and Ransford and Schwenninger simplified their argument [RS]. In 2026 the constant \(2\) for scalar polynomials was proved by Jin [Jin], by Lorist and Schwenninger [LoS], who also treat operators on Hilbert space and rational functions, and by Luo [Luo]; Crouzeix and Greenbaum used the theorem of Lorist and Schwenninger to lower the spectral constants of other regions, showing for example that certain annular regions are \(2\)-spectral sets [CG]. The *complete* form of the conjecture allows matrix coefficients and asks for the constant \(2\) uniformly in their size; Badea, Crouzeix and Delyon proved it for matrices \(A\) of order \(2\), and Åhag, Czyż and Virtanen for order at most \(3\) [ÅCV]. This course proves the complete form in all dimensions, a theorem of OpenAI [OpenAI-CC], following OpenAI's direct proof [OpenAI-DC].

## The theorem

For \(B_0,\dots,B_d\in M_m(\mathbf C)\) and the polynomial \(P(z)=\sum_{k=0}^dB_kz^k\) with matrix coefficients, and for \(A\in M_n(\mathbf C)\), put
\[
P[A]=\sum_{k=0}^dA^k\otimes B_k,
\]
an operator on \(\mathbf C^n\otimes\mathbf C^m\). All norms are operator norms for the Euclidean inner products. For \(m=1\), \(P[A]\) is the usual \(p(A)\).

**Theorem A** (OpenAI). For all positive integers \(n,m\), every \(A\in M_n(\mathbf C)\) and every polynomial \(P\) with coefficients in \(M_m(\mathbf C)\),
\[
\|P[A]\|\le2\max_{z\in W(A)}\|P(z)\| .
\]
The constant \(2\) cannot be replaced by a smaller number.

The bound does not depend on \(n\), \(m\) or the degree. Its *complete* character is the uniformity in \(m\): the coefficients \(B_k\) need not commute with each other, and a proof for scalar polynomials need not survive this amplification. The proof below keeps the order of multiplication, using \(FG\) and \(GF\) separately. OpenAI's other manuscript [OpenAI-CC] proves the theorem by a different method: it finds a similarity \(S\) with \(\|S\|\|S^{-1}\|\le2\) that turns a conformal image of \(A\) into a contraction; it is not treated here.

**The course.**

1. This lesson: the numerical range, the Toeplitz–Hausdorff theorem, matrix polynomials, sharpness, and the plan of the proof.
2. [Smooth convex neighbourhoods](smooth-convex-neighbourhoods.md): every compact convex set is approximated from outside by convex domains whose boundaries have analytic polar parametrizations.
3. [An exterior conformal coordinate](an-exterior-conformal-coordinate.md): the exterior of such a domain is the conformal image of \(\{|\lambda|>1\}\) under a map that extends across the unit circle.
4. [Faber polynomials and a positive kernel](faber-polynomials-and-a-positive-kernel.md): the Faber polynomials of the domain, a nonnegative kernel with marginals one, and a two-sided estimate of boundary norms by coefficients.
5. [The bound on a smooth convex domain](the-bound-on-a-smooth-convex-domain.md): the resolvent, its positive real part, singular vectors, and the proof of Theorem A.

**What the course assumes.** Linear algebra over \(\mathbf C\), including tensor products of matrices; complex analysis as in the core course [Complex Analysis](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C50), whose results are cited by number from Lebl's *Guide to Cultivating Complex Analysis*; Fourier series of absolutely convergent trigonometric series.

## 1. The numerical range

For \(A\in M_n(\mathbf C)\),
\[
W(A)=\{u^*Au:u\in\mathbf C^n,\ u^*u=1\}.
\]
It is compact, as the continuous image of the unit sphere, and it contains every eigenvalue: for a unit eigenvector \(u\) with \(Au=\lambda u\), \(u^*Au=\lambda\). It is invariant under unitary conjugation, \(W(VAV^*)=W(A)\), and \(W(aA+bI)=aW(A)+b\) for scalars \(a,b\).

**Theorem 1.1** (Toeplitz–Hausdorff). \(W(A)\) is convex.

*Proof.* Let \(z_1=u_1^*Au_1\) and \(z_2=u_2^*Au_2\) with unit vectors \(u_1,u_2\). If they are linearly dependent, \(z_1=z_2\). Otherwise let \(e_1,e_2\) be an orthonormal basis of their span and \(A_2=(e_i^*Ae_j)_{i,j}\in M_2(\mathbf C)\); the unit vectors \(v=xe_1+ye_2\) of the span give \(v^*Av=(\bar x,\bar y)A_2(x,y)^{\mathsf T}\), so \(z_1,z_2\in W(A_2)\subseteq W(A)\). It suffices to show that \(W(A_2)\) is convex. Write \(A_2=\bigl(\begin{smallmatrix}\alpha&\beta\\\gamma&\delta\end{smallmatrix}\bigr)\) and, for \(|x|^2+|y|^2=1\),
\[
w=\bigl(2\operatorname{Re}(\bar xy),\ 2\operatorname{Im}(\bar xy),\ |x|^2-|y|^2\bigr).
\]
Then
\[
\begin{aligned}
\|w\|^2&=4|\bar xy|^2+(|x|^2-|y|^2)^2\\
&=(|x|^2+|y|^2)^2=1,
\end{aligned}
\]
and every point of the unit sphere \(S^2\subset\mathbf R^3\) arises: choose \(|x|,|y|\ge0\) with \(|x|^2-|y|^2=w_3\) and then the phases so that \(\bar xy=(w_1+iw_2)/2\), whose modulus \(\frac12\sqrt{1-w_3^2}\) equals \(|x||y|\). Expanding,
\[
\begin{aligned}
(\bar x,\bar y)A_2(x,y)^{\mathsf T}={}&\tfrac{\alpha+\delta}2+\tfrac{\alpha-\delta}2w_3\\
&+\tfrac{\beta+\gamma}2w_1+i\tfrac{\beta-\gamma}2w_2,
\end{aligned}
\]
a real-affine map \(\Lambda:\mathbf R^3\to\mathbf C\cong\mathbf R^2\) evaluated at \(w\). So \(W(A_2)=\Lambda(S^2)\). The linear part of \(\Lambda\) has a nonzero kernel, and moving a point of the closed unit ball along a kernel direction until it reaches the sphere does not change its image. Hence \(\Lambda(S^2)=\Lambda(\text{ball})\), which is convex. \(\square\)

## 2. Matrix polynomials

If \(F(z)=\sum_iD_iz^i\) and \(G(z)=\sum_jE_jz^j\) have coefficients in \(M_m(\mathbf C)\), then
\[
\begin{aligned}
(FG)[A]&=\sum_{i,j}A^{i+j}\otimes D_iE_j\\
&=F[A]\,G[A],
\end{aligned}
\]
because \((A^i\otimes D_i)(A^j\otimes E_j)=A^{i+j}\otimes D_iE_j\). Likewise \((GF)[A]=G[A]F[A]\), and \(FG\ne GF\) in general.

For a normal matrix \(A=V\operatorname{diag}(\lambda_1,\dots,\lambda_n)V^*\) with \(V\) unitary,
\[
P[A]=(V\otimes I)\,D_P\,(V\otimes I)^*,
\]
where \(D_P\) is the block diagonal matrix with blocks \(P(\lambda_1),\dots,P(\lambda_n)\). So \(\|P[A]\|=\max_i\|P(\lambda_i)\|\), which is at most \(\max_{W(A)}\|P\|\). For normal matrices the constant is \(1\).

## 3. Sharpness

Let \(A=\bigl(\begin{smallmatrix}0&2\\0&0\end{smallmatrix}\bigr)\), \(m=1\) and \(P(z)=z\). Then \(\|P[A]\|=\|A\|=2\). For a unit vector \(u\), \(u^*Au=2\bar u_1u_2\) and \(|2\bar u_1u_2|\le|u_1|^2+|u_2|^2=1\), with equality when \(|u_1|=|u_2|=1/\sqrt2\). Varying the phases and the moduli, \(W(A)\) is the closed unit disc, and \(\max_{W(A)}|z|=1\). So the ratio \(2\) is attained, and no smaller constant works in Theorem A.

## 4. The plan of the proof

The proof replaces \(W(A)\) by a slightly larger convex domain \(\Omega\) with a smooth boundary and proves \(\|F[A]\|\le2\) whenever \(\|F(z)\|\le1\) on \(\partial\Omega\). For such domains there is a conformal map \(h\) from \(\{|\lambda|>1\}\) onto the exterior of \(\Omega\), extending across the unit circle. The expansion
\[
\frac{\lambda h'(\lambda)}{h(\lambda)-z}=\sum_{k\ge0}b_k(z)\lambda^{-k}
\]
defines polynomials \(b_k\) of degree \(k\), the *Faber polynomials*, whose values on \(\partial\Omega=h(\{|\mu|=1\})\) are \(\mu^k\) plus negative powers of \(\mu\). Convexity makes a certain kernel on the torus nonnegative, and this gives a two-sided estimate of the boundary norm of \(G=\sum_kb_kC_k\) by the coefficients \(C_k\). Substituting \(A\) gives \(\lambda h'(\lambda)(h(\lambda)I-A)^{-1}=\sum_kb_k(A)\lambda^{-k}\), whose Hermitian part is positive semidefinite on the circle because \(W(A)\subset\Omega\). Testing with the singular vectors of \(F[A]\), with products \(FG\) and \(GF\) in both orders, and comparing a positive \(2\times2\) block matrix gives the constant \(2\). A limit over shrinking domains reaches \(W(A)\) itself.

## 5. Exercises

**1.1** (easy). Show that the numerical range of \(\bigl(\begin{smallmatrix}a&b\\0&a\end{smallmatrix}\bigr)\) is the closed disc with centre \(a\) and radius \(|b|/2\).

**1.2** (easy). Give \(F\), \(G\) with coefficients in \(M_2(\mathbf C)\) and \(A=I_1\) (so \(n=1\)) with \(F[A]G[A]\ne G[A]F[A]\).

**1.3** (medium). Show that for a normal matrix \(W(A)\) is the convex hull of the eigenvalues.

**1.4** (medium). Show that \(\|A\|\le2\max_{z\in W(A)}|z|\) for every \(A\in M_n(\mathbf C)\), using \(A=H+iJ\) with Hermitian \(H=(A+A^*)/2\) and \(J=(A-A^*)/2i\). This is Theorem A for \(P(z)=z\).

## 6. Solutions

**1.1.** Subtracting \(aI\) reduces to \(a=0\). For a unit vector \(u\), \(u^*Au=b\,\bar u_1u_2\), and \(|\bar u_1u_2|\) takes every value in \([0,\frac12]\) with every phase.

**1.2.** For \(n=1\) and \(A=1\), \(F[A]=\sum_iD_i\) and \(G[A]=\sum_jE_j\). Take \(F(z)=\bigl(\begin{smallmatrix}0&1\\0&0\end{smallmatrix}\bigr)\) and \(G(z)=\bigl(\begin{smallmatrix}0&0\\1&0\end{smallmatrix}\bigr)\), constant polynomials whose products in the two orders differ.

**1.3.** With \(A=V\operatorname{diag}(\lambda_i)V^*\) and \(v=V^*u\), \(u^*Au=\sum_i\lambda_i|v_i|^2\), a convex combination with arbitrary weights \(|v_i|^2\).

**1.4.** \(u^*Hu=\operatorname{Re}(u^*Au)\) and \(u^*Ju=\operatorname{Im}(u^*Au)\), so \(\|H\|,\|J\|\le\max_{W(A)}|z|\), and \(\|A\|\le\|H\|+\|J\|\).

## References

- [OpenAI-DC] OpenAI, *A direct proof of the complete Crouzeix inequality*, OpenAI Math Release preprint, 26 September 2026. https://github.com/openai/math/tree/main/preprints/A-direct-proof-of-the-complete-Crouzeix-inequality-September-26-2026
- [OpenAI-CC] OpenAI, *The complete Crouzeix theorem: optimal similarity and a common positive boundary representation*, OpenAI Math Release preprint, 23 September 2026. https://github.com/openai/math/tree/main/preprints/The-complete-Crouzeix-theorem-September-23-2026
- [CP] M. Crouzeix and C. Palencia, *The numerical range is a \((1+\sqrt2)\)-spectral set*, SIAM Journal on Matrix Analysis and Applications 38 (2017), 649–655; arXiv:1702.00668. https://arxiv.org/abs/1702.00668
- [RS] T. Ransford and F. L. Schwenninger, *Remarks on the Crouzeix–Palencia proof that the numerical range is a \((1+\sqrt2)\)-spectral set*, arXiv:1708.08633. https://arxiv.org/abs/1708.08633
- [Jin] S. Jin, *The numerical range is a 2-spectral set*, Preprints.org 202607.1919, version 4, August 2026. https://www.preprints.org/manuscript/202607.1919/v4
- [LoS] E. Lorist and F. L. Schwenninger, *A solution to Crouzeix's conjecture*, arXiv:2608.03841, August 2026. https://arxiv.org/abs/2608.03841
- [Luo] Q. Luo, *Two boundary-certificate proofs of the Crouzeix theorem: fiberwise Fourier recurrence and defect-Gram telescoping*, Preprints.org 202608.1661, version 2, 2026. https://www.preprints.org/manuscript/202608.1661/v2
- [CG] M. Crouzeix and A. Greenbaum, *Update to: Spectral sets: numerical range and beyond*, arXiv:2609.22460, September 2026. https://arxiv.org/abs/2609.22460
- [ÅCV] P. Åhag, R. Czyż and J. Virtanen, *The complete Crouzeix conjecture in dimension three and the Clouâtre–Ostermann–Ransford conjecture*, arXiv:2608.27346, August 2026. https://arxiv.org/abs/2608.27346
