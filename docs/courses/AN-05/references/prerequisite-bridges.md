# Fourier transforms, finite spectra and convex separation

The Gaussian estimates in Quantitative estimates for quadratic Fourier multipliers use a precise Fourier convention, a real spectral theorem, and finite-dimensional convex separation. This chapter proves those facts with their constants and endpoint cases. Metric and topological foundations supplies the measure and compactness background. Basic references are [Melrose] for Fourier analysis and [Beezer] for finite-dimensional linear algebra, but the arguments below do not require either book.

Section 13 of Metric and topological foundations proves the full original scalar and finite-coordinate calculus. Its Section 13.12 gives the exact Gaussian, Rayleigh, logarithmic-contour, matrix and half-line receiving maps, retaining every original factor, endpoint and norm.

The complete original real-number, compactness, extrema and finite-norm proofs are in Section 12 of Metric and topological foundations. Its Section 12.10 gives the exact receiving minimum and spectral-contour maps; the original coordinates, norms and constants are retained.

We assume multivariable differentiation and Taylor's formula, smooth compact cutoffs, change of variables and Fubini for absolutely integrable functions, dominated convergence and differentiation, Cauchy–Schwarz, finite-dimensional compactness, and completeness of the real numbers. We also use elementary matrix algebra, determinants, Gram–Schmidt, and the usual monomial Schwartz seminorms. The complete finite basis, Gram, matrix and adjoint proofs are given in Section 10 of Polynomial and contour interfaces for stable boundary models. Each further step is proved here.

## 1. Fourier inversion on the Schwartz space

For \(d\geq1\), let \(\mathcal S(\mathbb R^d)\) have the seminorms
\[
p_{\alpha,\beta}(f)=\sup_x|x^\alpha\partial^\beta f(x)|.
\]
Use \(D_j=-i\partial_j\) and
\[
Ff(\xi)=\int e^{-ix\cdot\xi}f(x)\,dx,
\qquad
Gv(x)=(2\pi)^{-d}\int e^{ix\cdot\xi}v(\xi)\,d\xi.
\]
**Theorem 1.1 (Fourier inversion).** The map \(F\) is a continuous automorphism of the Schwartz space with inverse \(G\), and
\[
F(D_jf)=\xi_jFf,\qquad F(x_jf)=i\partial_{\xi_j}Ff.
\]
For the complex-linear distribution convention, \(\langle Fu,\phi\rangle=\langle u,F\phi\rangle\); transposition of the continuous Schwartz maps supplies the transform on \(\mathcal S'\), its inverse with the corresponding factor, and the differentiated identities. This convention agrees with the integral for regular distributions induced by Schwartz functions, by Fubini.

**Proof of Theorem 1.1.** Differentiation under the integral and integration by parts give the displayed identities. More precisely, \(\xi^\alpha\partial_\xi^\beta Ff(\xi)=F[D^\alpha((-ix)^\beta f)](\xi)\). By the finite Leibniz rule, \(D^\alpha((-ix)^\beta f)\) is a finite linear combination of derivatives of \(x^\beta f(x)\), with each coefficient fixed by \(\alpha,\beta\). Its Fourier transform is bounded in supremum norm by the \(L^1\) norm of that full expression. If \(N>d\), then
\[
\|h\|_1\leq\left(\int_{\mathbb R^d}\langle x\rangle^{-N}\,dx\right)
\sup_x\langle x\rangle^N|h(x)|,
\]
so finitely many Schwartz seminorms bound each output seminorm. Thus \(F:\mathcal S\to\mathcal S\) is continuous.

For \(\varepsilon>0\), put
\[
k_\varepsilon(x)=(4\pi\varepsilon)^{-d/2}e^{-|x|^2/(4\varepsilon)}.
\]
The one-dimensional Gaussian integral is \(\int_{\mathbb R}e^{-t^2}\,dt=\sqrt{\pi}\): square the integral, use Fubini, and in \(\mathbb R^2\) make the polar change of variables with Jacobian \(r\), obtaining \(2\pi\int_0^\infty e^{-r^2}r\,dr=\pi\). Hence \(\int k_\varepsilon=1\). Let
\[
I_\varepsilon(x)=\int_{\mathbb R^d}e^{ix\cdot\xi}e^{-\varepsilon|\xi|^2}\,d\xi.
\]
Integration of a total \(\xi_j\)-derivative gives
\[
0=ix_jI_\varepsilon(x)-2\varepsilon
\int_{\mathbb R^d}\xi_j e^{ix\cdot\xi}e^{-\varepsilon|\xi|^2}\,d\xi,
\qquad
\partial_{x_j}I_\varepsilon(x)=-\frac{x_j}{2\varepsilon}I_\varepsilon(x).
\]
Its value at zero is \((\pi/\varepsilon)^{d/2}\). Solving these coordinate equations yields the exact inverse-Gaussian identity
\[
(2\pi)^{-d}I_\varepsilon(x)=k_\varepsilon(x).
\]

For \(f\in\mathcal S\), Fubini is legitimate after inserting \(e^{-\varepsilon|\xi|^2}\). It gives
\[
(2\pi)^{-d}\int e^{ix\cdot\xi}e^{-\varepsilon|\xi|^2}Ff(\xi)\,d\xi
=\int_{\mathbb R^d}k_\varepsilon(x-y)f(y)\,dy.
\]
On the left, dominated convergence gives \(GFf(x)\), since \(Ff\in L^1\). On the right, write the difference from \(f(x)\) as \(\int k_\varepsilon(y)(f(x-y)-f(x))\,dy\). On \(|y|<\delta\), the mean-value formula bounds the difference by \(\|\nabla f\|_\infty\delta\). On its complement, boundedness of \(f\) gives at most \(2\|f\|_\infty\) times the Gaussian mass \(\int_{|y|\geq\delta}k_\varepsilon(y)\,dy=\pi^{-d/2}\int_{|z|\geq\delta/(2\sqrt{\varepsilon})}e^{-|z|^2}\,dz\), which tends to zero for fixed \(\delta>0\). First let \(\varepsilon\downarrow0\), then \(\delta\downarrow0\). Thus the right side tends to \(f(x)\), uniformly in \(x\). Hence \(GF=I\) on \(\mathcal S\). The calculation of the other inverse follows below without changing any Fourier factor. ∎

Here is the two-sided inverse bridge. Define \(Rf(x)=f(-x)\) and \(a=(2\pi)^{-d}\). A change of variables gives \(FR=RF\), and the candidate inverse is \(G=aRF\). The proof above gives \(GF=I\). Therefore
\[
FG=aFRF=aRF^2=GF=I.
\]
Reflection preserves the monomial seminorms, so \(G\) is continuous. No equivalence with an unstated alternative topology is required. In dimension zero the integral convention is the identity on \(\mathbb C\); this includes that harmless endpoint whenever a zero-dimensional factor occurs.

## 2. Plancherel and integer Sobolev weights

**Theorem 2.1 (Plancherel on Schwartz functions).** For \(u\in\mathcal S(\mathbb R^d)\),
\[
\|Fu\|_2^2=(2\pi)^d\|u\|_2^2.
\]
For \(f,g\in\mathcal S\), substitute \(g=GFg\) from Theorem 1.1 into \(\int f\overline g\). Fubini is valid because \(f\) and \(Fg\) are integrable. The inner integral is \(Ff\), so \(\int f\overline g=(2\pi)^{-d}\int Ff\,\overline{Fg}\). Taking \(g=f\) proves the displayed identity, including its full factor. No extension to arbitrary \(L^2\) functions is needed here.

For every integer \(s\geq0\), the multinomial identity and differentiation under \(F\) give the more precise formula
\[
\|\langle\xi\rangle^s Fu\|_2^2
=(2\pi)^d\sum_{|\alpha|\leq s}
\frac{s!}{(s-|\alpha|)!\,\alpha!}\|D^\alpha u\|_2^2.
\]
Indeed expand \((1+\xi_1^2+\cdots+\xi_d^2)^s\), multiply by \(|Fu|^2\), integrate the finite sum and apply Theorem 2.1 to each derivative. All coefficients are positive, so this also proves both norm comparisons, with constants depending only on \(d,s\). For \(s=0\) the sum has one term.

When \(s>d/2\), Cauchy–Schwarz yields
\[
\|Fu\|_1\leq
\|\langle\xi\rangle^{-s}\|_2
\|\langle\xi\rangle^sFu\|_2.
\]
The first norm is finite: the integral inside the unit ball is bounded; the annulus \(2^k\leq|\xi|<2^{k+1}\) contributes at most a constant times \(2^{k(d-2s)}\), whose sum converges. This is the precise integer-derivative control used in the local multiplier estimate.

## 3. Real spectral decomposition

**Theorem 3.1 (Real spectral decomposition).** Every self-adjoint endomorphism of a finite-dimensional real inner-product space has a real orthonormal eigenbasis, including repeated and zero eigenvalues.

**Proof.** In dimension zero the empty basis suffices. Otherwise maximize \(\langle Av,v\rangle\) over the compact unit sphere, and call a maximizer \(v\). For each \(w\perp v\), differentiate \(\langle A(v+tw),v+tw\rangle/\langle v+tw,v+tw\rangle\) at \(t=0\). Its derivative vanishes, so \(\langle Av,w\rangle=0\); hence \(Av=\lambda v\) for \(\lambda=\langle Av,v\rangle\). Self-adjointness makes \(v^\perp\) invariant, since \(\langle Aw,v\rangle=\langle w,Av\rangle=0\) for \(w\perp v\). Induction on dimension gives an orthonormal eigenbasis of \(v^\perp\). Together with \(v\) it gives the asserted basis, with no distinct-eigenvalue assumption. ∎

The complexification gives a second check of the real eigenspaces.

In dimension zero take the empty basis. Otherwise use Gram–Schmidt to choose real orthonormal coordinates. The real symmetric matrix \(A\), regarded as a complex matrix, is Hermitian. The real basis just proved complexifies to an eigenbasis of \(\mathbb C^d\), and every eigenvalue remains real. For real \(\lambda\), taking real and imaginary parts proves
\[
\ker_{\mathbb C}(A-\lambda I)
=\ker_{\mathbb R}(A-\lambda I)
 +i\ker_{\mathbb R}(A-\lambda I).
\]
Decompose a real vector into complex eigenvectors and take real parts. Thus the real eigenspaces span \(\mathbb R^d\). If \(Av=\lambda v\) and \(Aw=\mu w\), symmetry gives
\[
(\lambda-\mu)\langle v,w\rangle
=\langle Av,w\rangle-\langle v,Aw\rangle=0.
\]
Distinct eigenspaces are orthogonal. Choosing an orthonormal basis in each gives the required real basis, with all multiplicities retained.

The following triangular-matrix facts retain the zero-dimensional case and the order of multiplication. Its induction includes dimension zero with the empty matrix. Products of upper triangular matrices are upper triangular: when \(i>j\), in each term \(a_{ik}b_{kj}\), either \(k<i\) or \(k\geq i>j\), so one factor vanishes. An invertible upper triangular matrix preserves every coordinate flag space \(E_j\); its restriction to that finite-dimensional space is injective and therefore onto. Its inverse preserves the same flag and is upper triangular. The diagonal equation in \(AA^{-1}=I\) gives \((A^{-1})_{jj}=a_{jj}^{-1}\).

### 3.1. Real skew-adjoint operators and their full coordinate blocks

The scalar positivity argument uses both real self-adjoint and real skew-adjoint finite-dimensional spectral decompositions. The self-adjoint theorem is proved in Section3 of [Fourier transforms, finite spectra and convex separation](prerequisite-bridges.md), with the original inner product. We now prove the skew-adjoint theorem and every coordinate comparison needed to use it.

Let \(V\) be a finite-dimensional real vector space with its given positive-definite inner product \(h\), and let \(A:V\to V\) satisfy
\[
h(Au,v)=-h(u,Av)\qquad(u,v\in V).
\tag{SS1}
\]
Keep an original ordered coordinate basis \(b\), its full positive Gram matrix \(H\), and the original coordinate matrix \(M\) of \(A\). Thus
\[
h(J_bx,J_by)=x^{\mathsf T}Hy,\qquad
AJ_bx=J_bMx,\qquad M^{\mathsf T}H+HM=0.
\tag{SS2}
\]
The last equality follows by substituting each original pair of coordinate vectors into SS1. No coefficient, Gram factor or coordinate of the working operator is replaced.

Put \(B=-A^2\). Two applications of SS1 give
\[
h(Bu,v)=h(Au,Av)=h(u,Bv),\qquad
h(Bu,u)=h(Au,Au)\geq0.
\tag{SS3}
\]
The proved real self-adjoint theorem applies to this actual \(B\): its real eigenspaces give an orthogonal direct sum of \(V\), with every multiplicity retained. If \(Bu=\tau u\), \(u\ne0\), SS3 gives
\(\tau h(u,u)=h(Au,Au)\geq0\), hence \(\tau\geq0\). Moreover
\[
\ker B=\ker A,\qquad AB=BA,\qquad
A\ker(B-\tau I)\subset\ker(B-\tau I).
\tag{SS4}
\]
For the kernel equality one direction follows from \(B=-A^2\); in the other direction SS3 gives \(h(Au,Au)=0\), so \(Au=0\). The commuting identity is the full equality \(-A^3=-A^3\), and substitution proves the invariant-eigenspace assertion.

For each positive eigenvalue \(\tau\), let \(\lambda=\sqrt{\tau}>0\), the positive real root constructed in the real-number chapter. Choose a vector \(u\) of original \(h\)-length one in its eigenspace; finite Gram–Schmidt provides such a vector. Define \(v=Au/\lambda\). Then SS1--SS3 give the complete identities
\[
h(u,v)=\lambda^{-1}h(u,Au)=0,\qquad
h(v,v)=\lambda^{-2}h(Au,Au)
=\lambda^{-2}\tau h(u,u)=1,
\qquad Au=\lambda v,\quad Av=-\lambda u.
\tag{SS5}
\]
Here \(h(u,Au)=-h(Au,u)=-h(u,Au)\), so it is zero over the original real field. The last identity uses the actual equation \(A^2u=-\tau u\), retaining both \(\lambda\) factors.

The original \(h\)-orthogonal complement of \(\operatorname{span}\{u,v\}\) inside that eigenspace is \(A\)-invariant: for a vector \(w\) in the complement,
\[
h(Aw,u)=-h(w,Au)=-\lambda h(w,v)=0,\qquad
h(Aw,v)=-h(w,Av)=\lambda h(w,u)=0.
\tag{SS6}
\]
Induction on its finite dimension constructs all pairs there. It cannot terminate in a positive-eigenvalue line, because SS5 would construct two orthogonal unit vectors in that line. Thus each positive eigenspace has even dimension, with one pair per two dimensions. Choose an \(h\)-orthonormal basis of \(\ker A\) by the proved Gram construction. Altogether there are \(k\) orthonormal kernel vectors and \(l\) ordered pairs, with \(k+2l=\dim V\). The actual operator is zero on those \(k\) vectors and has the full ordered block
\[
C_j=\begin{pmatrix}0&-\lambda_j\\ \lambda_j&0\end{pmatrix}
\quad\hbox{on the ordered pair }(u_j,v_j),\qquad
\lambda_j>0.
\tag{SS7}
\]
Equal positive numbers are allowed and all their pairs remain.

Let \(S\) have, in the original coordinates \(b\), the columns of this entire constructed basis, and put \(C=\operatorname{diag}(0_k,C_1,\ldots,C_l)\). Orthogonality and the actual images in SS5 prove
\[
S^{\mathsf T}HS=I,\qquad MS=SC,\qquad
S^{-1}=S^{\mathsf T}H,\qquad
M=SCS^{-1}=SC S^{\mathsf T}H.
\tag{SS8}
\]
The columns form a basis, so \(S\) is invertible; multiplying the first equation by \(S^{-1}\) proves the displayed inverse formula. These are exact morphisms between the original coordinates and the displayed blocks, preserving \(H\) and every coordinate coefficient. They do not identify \(M\) numerically with \(C\).

Complexify the original maps and inner product. In each pair,
\[
A(u_j+i v_j)=-i\lambda_j(u_j+i v_j),\qquad
A(u_j-i v_j)=i\lambda_j(u_j-i v_j).
\tag{SS9}
\]
Both eigenvectors are nonzero and independent: their coefficients on the original real independent pair give determinant \(-2i\ne0\). They span its complexification, while each chosen kernel vector remains an eigenvector with eigenvalue zero. Each is nonzero, since its original squared norm is one. Thus the full complex spectrum is zero with multiplicity \(k\) and both signs \(i\lambda_j,-i\lambda_j\) for every pair. The real characteristic polynomial comparison retains the entire determinant factors:
\[
\begin{split}
\det(tI-M)
&=\det S\,\det(tI-C)\,\det(S^{-1})\\
&=\det S\,t^k\prod_{j=1}^l(t^2+\lambda_j^2)\,\det(S^{-1}),\\
\det S\,\det(S^{-1})&=\det(SS^{-1})=1.
\end{split}
\tag{SS10}
\]
Every zero and repeated pair is accounted for. In dimension zero the basis is empty, both coordinate maps are the unique empty bijection, each determinant and empty product is one, and \(k=l=0\). This proves the entire real skew-adjoint decomposition used by the scalar positivity argument at its original finite-dimensional inner product.

## 4. Strict separation of an open convex set

**Theorem 4.1 (Strict separation).** Let \(V\) be a finite-dimensional real vector space, let \(C\subset V\) be nonempty, open and convex, and let \(x\notin C\). There is a nonzero real covector \(\eta\) such that
\[
\eta(y)<\eta(x)\quad(y\in C),
\qquad \sup_{y\in C}\eta(y)\leq\eta(x).
\]
The second inequality includes \(x\) on the boundary. The supremum need not be attained. The proof uses only finite-dimensional compactness and the inner product.

Choose an auxiliary Euclidean norm, put \(K=\overline C\), and fix \(c\in C\) with \(B(c,r)\subset C\), \(r>0\). First, if \(z\in K\) and \(0\leq t<1\), then
\[
(1-t)c+tz\in C.
\]
For \(t=0\) this is immediate. For \(0<t<1\), choose \(z_j\in C\) tending to \(z\). Convexity gives a ball of radius \((1-t)r\) centered at \((1-t)c+tz_j\) inside \(C\). For sufficiently large \(j\), this ball contains \((1-t)c+tz\), proving the assertion.

For \(\varepsilon>0\), put \(z_\varepsilon=x+\varepsilon(x-c)\). This point lies outside \(K\): if it lay in \(K\), then
\[
x=\frac{\varepsilon}{1+\varepsilon}c
 +\frac{1}{1+\varepsilon}z_\varepsilon
\]
would lie in \(C\) by the preceding assertion. The nonempty closed set \(K\) has a point \(q_\varepsilon\) nearest to \(z_\varepsilon\). To see existence without a compactness assumption on \(K\), take a minimizing sequence. Its distance to \(z_\varepsilon\) is bounded, so it has a convergent subsequence in finite dimensions; closedness places its limit in \(K\).

Write \(v_\varepsilon=z_\varepsilon-q_\varepsilon\ne0\). For \(y\in K\), the segment \(q_\varepsilon+t(y-q_\varepsilon)\), \(0\leq t\leq1\), lies in \(K\). Differentiating the squared distance at its minimum \(t=0\) gives
\[
\langle v_\varepsilon,y-q_\varepsilon\rangle\leq0.
\]
Consequently, for \(u_\varepsilon=v_\varepsilon/|v_\varepsilon|\),
\[
\langle u_\varepsilon,y\rangle
\leq\langle u_\varepsilon,z_\varepsilon\rangle
-|v_\varepsilon|
\leq\langle u_\varepsilon,z_\varepsilon\rangle.
\]
Choose \(\varepsilon=1/k\) and a convergent subsequence of the unit vectors, with limit \(u\), \(|u|=1\). Since \(z_\varepsilon\to x\), the last inequality implies \(\langle u,y\rangle\leq\langle u,x\rangle\) for every \(y\in K\). The same subsequence works for every \(y\): it was selected using only the unit vectors, and the inequality holds for every \(y\) at every index.

Set \(\eta(y)=\langle u,y\rangle\). It is nonzero. For \(y\in C\), openness gives \(y+\delta u\in C\) for some \(\delta>0\), whence
\[
\eta(y)+\delta\leq\eta(x).
\]
This proves strict pointwise separation. The supremum statement follows because \(\eta(C)\) is nonempty and bounded above. In dimension zero the hypotheses cannot occur, since the only nonempty open set is all of \(V\).

## 5. Support functions of Minkowski sums

**Proposition 5.1.** For nonempty \(A,B\subset V\), put
\[
h_A(\eta)=\sup_{a\in A}\eta(a)\in\mathbb R\cup\{+\infty\}.
\]
Then \(h_{A+B}(\eta)=h_A(\eta)+h_B(\eta)\), where \(A+B=\{a+b:a\in A,b\in B\}\). Nonemptiness excludes \(-\infty\), so the right side is unambiguous.

Linearity first gives the inequality \(\leq\). If both right-hand suprema are finite, choose \(a,b\) within \(\varepsilon/2\) of the two suprema. Their sum gives the reverse inequality up to \(\varepsilon\); let \(\varepsilon\downarrow0\). If \(h_A(\eta)=+\infty\), fix \(b_0\in B\). The values \(\eta(a+b_0)\) are unbounded above, so \(h_{A+B}(\eta)=+\infty\). Interchange \(A,B\) for the other case. No boundedness, compactness or convexity is needed for this identity.

## 6. Phase checks and exercises

The exact Fourier phases used above can be checked without changing conventions: the segment integral in the fundamental theorem runs from \(0\) to \(1\); frequency continuity compares \(e^{-ix\cdot\xi}-e^{-ix\cdot\xi'}\); the squared one-dimensional Gaussian integral is an integral over \(\mathbb R^2\); Parseval uses the conjugate transform of \(\psi\) as its second factor; and an \(H^m\) condition uses \(\langle\xi\rangle^{m}Fu\in L^2\). These checks preserve the signs and the factor \((2\pi)^{-d}\) in Theorems 1.1 and 2.1.

Exercise. For the open strip \(C=\{(a,b)\in\mathbb R^2:|a|<2\}\) and boundary point \(x=(2,7)\), determine all separating covectors satisfying the strict inequality in Theorem 4.1. Explain why the support value need not be attained and why its finiteness constrains the covector.

Solution. Write \(\eta(a,b)=\alpha a+\beta b\). Since \(b\) is unrestricted, finite upper support forces \(\beta=0\). Nonzero separation at the right boundary then forces \(\alpha>0\), and every such \(\alpha\) works: \(\alpha a<2\alpha=\eta(x)\). The support equals \(2\alpha\) but is not attained because \(a=2\) is excluded. This distinguishes strict pointwise separation from a positive uniform gap at a boundary point.

**Exercise 6.2 (A Gaussian transform).** For \(t>0\) and \(f_t(x)=e^{-t|x|^2}\) on \(\mathbb R^d\), compute \(Ff_t(\xi)\) with the exact convention of Section 1.

**Solution.** Apply the Gaussian identity from the proof of Theorem 1.1 after exchanging the roles of \(x\) and \(\xi\). Equivalently, the same integration-by-parts equation gives \(\partial_{\xi_j}Ff_t=-\xi_jFf_t/(2t)\), while \(Ff_t(0)=(\pi/t)^{d/2}\). Hence
\[
Ff_t(\xi)=(\pi/t)^{d/2}e^{-|\xi|^2/(4t)}.
\]
The positive value at zero fixes the constant and the negative exponent fixes the phase.

The polar and Gaussian integrations in Section 1 are proved in Sections 15.6–15.7 of Banach estimates, quotient spaces and compact parameter arguments. These proofs include completed measurability, both determinant terms, the radial endpoints and the full Fourier heat-kernel factors.

## 7. Fourier transforms on the complete \(L^2\) space

The Schwartz identities above extend to the original completed Lebesgue \(L^2(\mathbb R^d)\), with both Fourier factors unchanged. The measure, density, translation and completeness proofs used here are Sections 15.0–15.4 of Banach estimates, quotient spaces and compact parameter arguments. We use their original measure and scalar field.

### 7.1. Constructing both inverse maps

Suppose first that \(d\geq1\). Compact smooth functions are dense in \(L^2\), by the truncation and mollification proof there, and belong to the Schwartz space. For \(f\in L^2\), choose Schwartz \(f_j\to f\) in \(L^2\). Theorem 2.1 gives the exact difference identity
\[
 \|Ff_j-Ff_k\|_2=(2\pi)^{d/2}\|f_j-f_k\|_2.
                                                               \tag{FL1}
\]
Completeness makes this a convergent sequence. If \(\widetilde f_j\to f\) is another such sequence, its difference from \(f_j\) tends to zero in \(L^2\), so (FL1) gives the same output. Define \(Ff\) as that limit. Linearity follows by approximating each summand and taking limits; the norm identity follows from continuity of the norm.

For Schwartz \(h\), Theorem 1.1 gives \(F(Gh)=h\), and Theorem 2.1 applied to \(Gh\) gives \(\|Gh\|_2=(2\pi)^{-d/2}\|h\|_2\). Thus the same construction extends \(G\) to \(L^2\). Applying continuity to \(GFf_j=f_j\) and \(FGh_j=h_j\) proves, on the original entire spaces,
\[
 \begin{split}
 F,G&:L^2(\mathbb R^d)\longrightarrow L^2(\mathbb R^d),\\
 GF&=I,\qquad FG=I,\\
 \|Ff\|_2&=(2\pi)^{d/2}\|f\|_2,\qquad
 \|Gh\|_2=(2\pi)^{-d/2}\|h\|_2 .
 \end{split}                                                   \tag{FL2}
\]
These are bijections with their original norms. In dimension zero the measure is the point mass on the one point \(\mathbb R^0\), the space is \(\mathbb C\), and both maps are the identity with \((2\pi)^0=1\). No assertion that this point is null is used in that case.

### 7.2. Ordinary integrals and simultaneous approximation

For any finite exponents \(a,c\geq1\) and \(f\in L^a\cap L^c\), put
\(f_j=1_{\{|x|_\infty\leq j,\ |f(x)|\leq j\}}f\).
Dominated convergence of \(|f|^a\) and \(|f|^c\) proves convergence in both original norms. Each \(f_j\) is bounded and supported in its displayed coordinate cube. Fix the compact smooth nonnegative approximate identity \(\rho\), with \(\int\rho=1\), from Section 15.4 of the linked chapter. For
\(\rho_\varepsilon(x)=\varepsilon^{-d}\rho(x/\varepsilon)\), its proved translation estimate is
\[
 \|\rho_\varepsilon*f_j-f_j\|_t
 \leq\int|\rho(z)|\,\|f_j(\,\cdot-\varepsilon z)-f_j\|_t\,dz
 \longrightarrow0,\qquad t=a,c.                                \tag{FL3}
\]
**The full integral triangle estimate in (FL3).** Fix an original finite exponent \(t\geq1\), the actual \(f_j\), and \(\varepsilon>0\). Put \(h_z(x)=f_j(x-\varepsilon z)-f_j(x)\) and \(M_\varepsilon(x)=\int|\rho(z)||h_z(x)|\,dz\). These are the original translated differences and their nonnegative integral envelope. The joint integrand is measurable for completed Lebesgue measure: first take a Borel representative of the given \(f_j\) class. Its coordinate compositions are Borel. Changing that representative on a null set \(N\) changes the composed functions only on the inverse images of \(N\times\mathbb R^d\) under the identity product map and the invertible shear \((x,z)\mapsto(x-\varepsilon z,z)\). Its inverse is \((w,z)\mapsto(w+\varepsilon z,z)\), its full block determinant is one, and completed product integration and affine substitution make both inverse images null. Thus the calculation respects the original completed classes. For each fixed \(x\), the section in \(z\) is also measurable by the invertible affine substitution \(z\mapsto x-\varepsilon z\).

The original truncation gives \(|f_j|\leq j\) and support in \(Q_j=[-j,j]^d\). Consequently \(0\leq M_\varepsilon\leq2j\|\rho\|_1\), with support contained in the actual compact set \(Q_j\cup(Q_j+\varepsilon\operatorname{supp}\rho)\). It follows that \(M_\varepsilon\in L^t\). At \(t=1\), nonnegative Tonelli gives \(\|M_\varepsilon\|_1=\int|\rho(z)|\|h_z\|_1\,dz\). If \(t>1\), apply the proved scalar Hölder inequality with its actual conjugate exponent \(t'=t/(t-1)\). The full power satisfies \(\|M_\varepsilon^{t-1}\|_{t'}=\|M_\varepsilon\|_t^{t-1}\), since \((t-1)t'=t\). Nonnegative Tonelli then gives
\[
 \begin{aligned}
 \|M_\varepsilon\|_t^t
 &=\int M_\varepsilon(x)^{t-1}
              \left(\int|\rho(z)||h_z(x)|\,dz\right)dx\\
 &=\int|\rho(z)|
              \left(\int M_\varepsilon(x)^{t-1}|h_z(x)|\,dx\right)dz\\
 &\leq\|M_\varepsilon\|_t^{t-1}
                 \int|\rho(z)|\|h_z\|_t\,dz.
 \end{aligned}\tag{FL3a}
\]
The last integral is finite, because translation is an isometry and \(\|h_z\|_t\leq2\|f_j\|_t\). If \(\|M_\varepsilon\|_t>0\), division by its displayed positive power proves the integral triangle bound. If that norm is zero, the same bound is immediate without division. The exact difference formula (LP13), with both original scaling Jacobians retained, gives \(|\rho_\varepsilon*f_j-f_j|\leq M_\varepsilon\). Combining these two inequalities proves exactly (FL3), rather than replacing it by the weaker power-integral bound (LP14). Translation continuity makes \(\|h_z\|_t\to0\) for each fixed \(z\), and its original bound \(2|\rho(z)|\|f_j\|_t\) is integrable. Its dependence on \(z\) is continuous by that same translation theorem and the reverse norm inequality. Dominated convergence therefore proves the limit in (FL3) for each of the original exponents \(a,c\), without an infinite-dimensional integration theorem.

Its bound \(2|\rho(z)|\|f_j\|_t\) is integrable. Choose a positive \(\varepsilon_j<1/j\) making both errors at most \(1/j\). Then \(v_j=\rho_{\varepsilon_j}*f_j\) is compact smooth and tends to \(f\) in both norms. Differentiating this absolutely convergent convolution proves smoothness, and its support is contained in the sum of the two original compact supports. This constructs a single approximation, rather than assuming that two independently chosen approximations coincide.

Apply this with \(a=1,c=2\). The ordinary Fourier and inverse integrals satisfy
\[
 \begin{split}
 \sup_\xi|Fv_j(\xi)-Ff(\xi)|&\leq\|v_j-f\|_1,\\
 \sup_x|Gv_j(x)-Gf(x)|&\leq(2\pi)^{-d}\|v_j-f\|_1 .
 \end{split}                                                   \tag{FL4}
\]
Here the symbols on the right side of each difference denote their ordinary absolutely defined integrals. Their uniform limits therefore agree almost everywhere with the \(L^2\) limits in (FL2). Indeed, the summable-difference argument in the completeness proof supplies an almost-everywhere convergent subsequence of either \(L^2\) sequence. The uniform and almost-everywhere limits of that subsequence are equal. Thus the constructed \(L^2\) classes coincide with the original integrals on \(L^1\cap L^2\), with the exact inverse factor retained.

The same simultaneous approximation identifies any two finite-exponent continuous extensions of an operator from Schwartz functions when both original norm bounds are available. For completeness, if functions converge in \(L^a\) and \(L^c\) to two limits, select a common subsequence with summable \(a\)-th and \(c\)-th powers of its errors. Chebyshev's integral inequality and the measure of the countable tail unions make both errors tend to zero almost everywhere; the limits must agree. This is the identification used for the multiplier below.

### 7.3. Parseval pairing, multiplication and the actual adjoint

Approximating both inputs by Schwartz functions in \(L^2\), Theorem 2.1 and Cauchy–Schwarz prove
\[
 \langle u,v\rangle
   =(2\pi)^{-d}\int_{\mathbb R^d}
                     Fu(\xi)\overline{Fv(\xi)}\,d\xi .
                                                               \tag{FL5}
\]
The inner product is linear in the first variable. Each pairing difference tends to zero by the sum of the two Cauchy–Schwarz bounds, so the original factor persists.

If \(b\) is a measurable scalar frequency function with
\(\|b\|_\infty\leq B\), multiplication by \(b\) respects the completed null classes and maps \(L^2\) to itself with norm at most \(B\). Hence
\[
 \begin{split}
 T_b&=G\,M_b\,F,\qquad M_bh=bh,\\
 \|T_bf\|_2
 &\leq(2\pi)^{-d/2}B(2\pi)^{d/2}\|f\|_2=B\|f\|_2,\\
 \langle T_bu,v\rangle
 &=(2\pi)^{-d}\int b(\xi)Fu(\xi)\overline{Fv(\xi)}\,d\xi
   =\langle u,T_{\overline b}v\rangle .
 \end{split}                                                   \tag{FL6}
\]
This proves the actual adjoint \(T_b^*=T_{\overline b}\). It uses the constructed inverse maps, not an assumed representation of an \(L^p\) dual space. For Schwartz \(f\), \(bFf\in L^1\cap L^2\), so \(T_bf\) is exactly the original inverse integral. These statements apply in the elliptic chapter with \(d=n\geq1\); its arbitrary value of the symbol at zero changes no frequency integral.

## 8. Partial Fourier transforms in the original product coordinates

Banach estimates, quotient spaces and compact parameter arguments supplies the full original integration, monomial Schwartz and lattice-cutoff proofs used here. Metric and topological foundations supplies the exact derivative and segment-integration maps.

These proofs extend the course's existing scalar Fourier calculation to its actual product spaces. The original transform, Lebesgue densities, complex-linear distribution convention, coordinate orders and every inverse factor remain. The independent inputs are the scalar Fourier inversion and Schwartz Plancherel proofs in Sections 1 and 2 of the Fourier chapter, the two-sided original L2 extensions in its Section 7, the scalar measure and density proofs in Banach Sections 15--16, the full monomial Schwartz proof in Banach Section 18, and the actual cutoff in Banach Section 21. The distribution, symbol, conormal and operator receivers do not prove these inputs.

### 8.1. The actual transform and every monomial derivative

Let \(p,q\geq0\) be integers. Write the original coordinates as \((x,y)\in\mathbb R^p\times\mathbb R^q\), with dual coordinate \(\xi\in\mathbb R^p\). The monomial seminorms are

\[
\begin{aligned}
 P_{a,b;c,d}(f)=\sup_{x,y}
       |x^a y^b\partial_x^c\partial_y^d f(x,y)|,
 \qquad\\
 (T_xf)(\xi,y)=\int_{\mathbb R^p}e^{-ix\cdot\xi}f(x,y)\,dx,
 \qquad\\
 (G_\xi h)(x,y)=(2\pi)^{-p}
           \int_{\mathbb R^p}e^{ix\cdot\xi}h(\xi,y)\,d\xi.
 \end{aligned}
\tag{PF1}
\]

Dimension zero means a singleton carrying measure one; its empty monomials and derivative products equal one. Thus these formulas include the identity when \(p=0\), and the full scalar transform when \(q=0\).

For \(p\geq1\), choose an integer \(M\) with \(2M>p\) and retain the actual finite integral

\[
 I_{p,M}=\int_{\mathbb R^p}(1+|x|^2)^{-M}\,dx,
 \qquad
 (1+|x|^2)^M=
    \sum_{|r|\leq M}{M!\over(M-|r|)!\,r!}x^{2r}.
 \tag{PF2}
\]

Its finiteness, with the entire integral and all shell bounds retained, was proved by SC3. This also bounds the integral of any Schwartz function in the \(x\) variables uniformly in all original \(y\) variables and in each prescribed \(y\) monomial. Derivatives under the integral follow from the original dominated derivative theorem: on a compact parameter segment, every derivative of the integrand is bounded by a finite sum of original monomial Schwartz seminorms times the integrable \((1+|x|^2)^{-M}\). The exact fundamental theorem on that segment identifies each derivative of the integral with the integral of the derivative. Iterating gives all joint derivatives, with the original \((-ix)^\gamma\) factors.

Here are the integration-by-parts limits, including their cutoff terms. Take the actual Banach Section 21 function \(\vartheta\), equal to one on \([-1,1]^p\) and supported in \([-7/4,7/4]^p\subset(-2,2)^p\), and set \(\vartheta_R(x)=\vartheta(x/R)\), \(R\geq1\). For any Schwartz \(g(x,y)\) and multiindex \(a\), compact integration by parts gives

\[
\begin{aligned}
 \xi^a\int e^{-ix\cdot\xi}\vartheta_R(x)g(x,y)\,dx
 \\
 =(-i)^{|a|}\sum_{v\leq a}{a\choose v}R^{-|v|}
       \int e^{-ix\cdot\xi}
          (\partial^v\vartheta)(x/R)
          \partial_x^{a-v}g(x,y)\,dx.
 \end{aligned}
\tag{PF3}
\]

The \(v=0\) term converges by dominated convergence to the full original derivative integral. Every \(v\ne0\) term is supported where \(R\leq\max_j|x_j|\leq2R\). Its absolute value is at most its original coefficient \( {a\choose v}R^{-|v|}\|\partial^v\vartheta\|_\infty\) times the integral of \(|\partial_x^{a-v}g(x,y)|\) over that set, and tends to zero. Multiplying by any requested \(y\) monomial and taking any \(y\) derivative gives the same conclusion with its corresponding original seminorm bound. The left side tends to \(\xi^aT_xg\). Consequently \(T_xD_x^ag=\xi^aT_xg\), with \(D_x=-i\partial_x\). No boundary contribution or cutoff derivative has been omitted before its limiting estimate.

Apply this identity to \(g=(-ix)^\gamma y^\beta\partial_y^\delta f\). The full product rule gives

\[
\begin{aligned}
 \xi^\alpha y^\beta\partial_\xi^\gamma\partial_y^\delta T_xf
 \\
 =(-i)^{|\alpha|+|\gamma|}
   \sum_{\substack{v\leq\alpha\\v\leq\gamma}}
       {\alpha\choose v}{\gamma!\over(\gamma-v)!}
       \int e^{-ix\cdot\xi}x^{\gamma-v}y^\beta
                \partial_x^{\alpha-v}\partial_y^\delta f(x,y)\,dx.
 \end{aligned}
\tag{PF4}
\]

Taking absolute values and expanding the entire weight in PF2 proves the finite, explicit seminorm estimate

\[
\begin{aligned}
 \sup_{\xi,y}
  |\xi^\alpha y^\beta\partial_\xi^\gamma\partial_y^\delta T_xf|
 \\
 \leq I_{p,M}
   \sum_{\substack{v\leq\alpha\\v\leq\gamma}}
       {\alpha\choose v}{\gamma!\over(\gamma-v)!}
 \\
   \sum_{|r|\leq M}{M!\over(M-|r|)!\,r!}
       P_{2r+\gamma-v,\beta;\alpha-v,\delta}(f).
 \end{aligned}
\tag{PF5}
\]

Every factorial, multiindex and coefficient is retained. For \(p=0\), this is the equality of the original \(y\) seminorms, with \(I_{0,M}=1\) and the singleton empty-index sums. PF5 proves that \(T_x\) maps the original full product Schwartz space continuously into itself. It does not rely on a tensor-density assertion, a Schwartz kernel theorem, or a coordinate pullback theorem.

### 8.2. Both inverse maps, with the original factors

Reflection in the transformed variables is \(R_xf(x,y)=f(-x,y)\). Its original monomial seminorms equal those of \(f\). Direct change of the original integration variable gives \(T_xR_x=R_\xi T_x\), and the actual inverse in PF1 is \(G_\xi=(2\pi)^{-p}R_xT_\xi\), with the input coordinates named accordingly. Thus PF5 also proves continuity of \(G_\xi\), retaining the factor \((2\pi)^{-p}\) on each output bound.

For every fixed original \(y\), the slice \(f(\cdot,y)\) is Schwartz by PF2 and the original monomial bounds. The proved scalar Fourier inversion applies to this slice and gives

\[
 G_\xi T_x f(x,y)=f(x,y),\qquad
 T_xG_\xi h(\xi,y)=h(\xi,y),\qquad
 T_\xi T_x f(x,y)=(2\pi)^p f(-x,y).
 \tag{PF6}
\]

Both compositions lie in the original full Schwartz space by PF5, so pointwise equality is equality of its actual elements. The third identity follows from the first and the full reflection/inverse formula. It retains the entire power of \(2\pi\); the original transform has not been replaced by a unitary convention.

For each transformed coordinate \(j\) and unchanged coordinate \(k\), PF3, differentiation under PF1 and the original product rule give all four original maps

\[
 T_x(D_{x_j}f)=\xi_jT_xf,\qquad
 T_x(x_jf)=i\partial_{\xi_j}T_xf,\qquad
 T_x(D_{y_k}f)=D_{y_k}T_xf,\qquad
 T_x(y_kf)=y_kT_xf.
 \tag{PF7}
\]

Their arbitrary finite iterates follow by composition in the actual indicated order. Formula PF4 supplies the full simultaneous derivative formula, rather than suppressing its product terms.

### 8.3. Tempered distributions and both original dual topologies

Let \(\mathcal S'\) denote the complex-linear continuous dual of the original monomial Schwartz space. In the transposed formula below, \(T_\xi\phi(x,y)\) is the same original negative-sign transform applied to the test function's \(\xi\) variables, with its output named \(x\). Define

\[
 \langle T_xu,\phi(\xi,y)\rangle
       =\langle u,T_\xi\phi(x,y)\rangle,
 \qquad
 \langle G_\xi v,\psi(x,y)\rangle
       =\langle v,G_x\psi(\xi,y)\rangle.
 \tag{PF8}
\]

The test transforms are continuous by PF5 and its full inverse bound, so these are actual tempered distributions. Transposing the two equations in PF6 proves that these distribution maps are mutual inverses. On regular distributions induced by Schwartz functions, Fubini identifies PF8 with the original integrals in PF1. Here is its full absolute-integrability bound: choose integers \(M,N\) with \(2M>p\), \(2N>q\), retain \(I_{p,M}\), \(I_{q,N}\), and put

\[
\begin{aligned}
 A_f=\sum_{\substack{|r|\leq M\\|s|\leq N}}
       {M!\over(M-|r|)!\,r!}{N!\over(N-|s|)!\,s!}
       P_{2r,2s;0,0}(f),\qquad\\
 B_\phi=\sum_{|r|\leq M}{M!\over(M-|r|)!\,r!}
       P_{2r,0;0,0}(\phi),
 \qquad\\
 \iiint |f(x,y)\phi(\xi,y)|\,dx\,d\xi\,dy
       \leq I_{p,M}^2 I_{q,N} A_f B_\phi<\infty.
 \end{aligned}
\tag{PF8a}
\]

The full weight expansions give
\(|f(x,y)|\leq A_f(1+|x|^2)^{-M}(1+|y|^2)^{-N}\) and
\(|\phi(\xi,y)|\leq B_\phi(1+|\xi|^2)^{-M}\).
Their product and positive Tonelli prove PF8a. Empty-dimensional factors retain their unit mass and empty-index coefficient one. Consequently the distribution convention agrees with the original function convention, including its inverse coefficient.

For the strong dual topology use its actual bounded-set seminorm \(q_C(u)=\sup_{\phi\in C}|\langle u,\phi\rangle|\). PF5 proves that the image of every bounded Schwartz set \(C\) under \(T_\xi\) is bounded. Directly from PF8,

\[
 q_C(T_xu)=q_{T_\xi C}(u),\qquad
 q_C(G_\xi v)=q_{G_x C}(v).
 \tag{PF9}
\]

Thus both distribution maps are continuous for the original strong dual topology; singletons give the weak dual continuity too. No unidentified distribution topology enters the argument.

The identities in PF7 hold for these distributions with precisely the same factors and signs. For example,

\[
 \langle T_xD_{x_j}u,\phi\rangle
  =i\langle u,\partial_{x_j}T_\xi\phi\rangle
  =\langle u,T_\xi(\xi_j\phi)\rangle,
 \qquad
 \langle i\partial_{\xi_j}T_xu,\phi\rangle
  =-i\langle u,T_\xi\partial_{\xi_j}\phi\rangle
  =\langle u,x_jT_\xi\phi\rangle.
 \tag{PF10}
\]

Here \(\partial_{x_j}T_\xi\phi=-iT_\xi(\xi_j\phi)\) and \(T_\xi\partial_{\xi_j}\phi=i x_jT_\xi\phi\), with the latter proved by PF3 in the test variable. Differentiating \(y\) commutes with the test transform by the proved dominated derivative step, and multiplication by \(y\) factors out of that integral. The original distributional signs in the unchanged variables therefore give the last two identities in PF7. Their finite iterates keep their actual multiplication order.

### 8.4. Original L2 maps and the exact unitary comparison

For \(f,g\in\mathcal S(\mathbb R^{p+q})\), apply the original scalar Schwartz Parseval identity at each fixed \(y\). Positive Tonelli, or absolute Fubini for the pairing, then gives

\[
\begin{aligned}
 \|T_xf\|_{L^2(d\xi\,dy)}^2
       =(2\pi)^p\|f\|_{L^2(dx\,dy)}^2,
 \qquad\\
 \int f(x,y)\overline{g(x,y)}\,dx\,dy
       =(2\pi)^{-p}
         \int T_xf(\xi,y)\overline{T_xg(\xi,y)}\,d\xi\,dy.
 \end{aligned}
\tag{PF11}
\]

The pairing is absolutely integrable on either side by the already proved integral Cauchy--Schwarz inequality. All densities and the full power of \(2\pi\) remain.

Compact smooth density in the original \(L^2(dx\,dy)\), proved by LP10--LP12, supplies Schwartz approximants \(f_j\to f\). PF11 makes \(T_xf_j\) Cauchy with its exact norm factor \((2\pi)^{p/2}\). Completeness of the original target \(L^2(d\xi\,dy)\) gives a unique limit, independent of the approximants. This defines the bounded original \(T_x\) on the whole original L2 space, with precisely that norm factor. The inverse \(G_\xi\) extends by its exact \((2\pi)^{-p/2}\) norm bound. Taking limits in both identities in PF6 shows that these two whole-space maps are mutual inverses. Taking limits in PF11 gives both original norm and pairing identities for all L2 inputs.

The distribution and L2 maps agree on L2 functions. Indeed for every fixed Schwartz test, the original integral pairing against that test is continuous in L2 by Cauchy--Schwarz. Pair PF8 with the same approximants on both sides and pass to their L2 limits. This identifies the two exact maps without a pointwise Fourier-integrability assumption for a general L2 input.

If the receiving statement uses a unitary transform, its exact comparison is

\[
\begin{aligned}
 U_x=(2\pi)^{-p/2}T_x,\qquad\\
 U_x^{-1}=(2\pi)^{p/2}G_\xi,\qquad\\
 \|U_xf\|_2^2=(2\pi)^{-p}\|T_xf\|_2^2=\|f\|_2^2.
 \end{aligned}
\tag{PF12}
\]

Both inverse maps and their surjectivity have just been proved, so this receiving comparison is unitary. It leaves the original \(T_x\), \(G_\xi\), measures and constants explicit throughout the calculation.

### 8.5. Exact receiving scope

For the conormal coordinates \((t,z)\in\mathbb R^k\times\mathbb R^{n-k}\), take the actual substitutions \(p=k\), \(q=n-k\), \(x=t\), \(y=z\), \(\xi=\tau\). PF1--PF12 then supply the entire partial normal Fourier, full tempered-distribution, monomial derivative and L2 extension clause with inverse coefficient \((2\pi)^{-k}\). The codimension-zero factor has already been proved as the identity; it requires no nonexistent normal coordinate. The complete original scalar Fourier proof supplies the full transform when every coordinate is transformed. These are exact maps on the specified spaces, with every original coordinate and factor retained.

This supplies the elementary Fourier interface itself. Distribution test-function tensor operations, nonlinear coordinate pullbacks, bundle covariance, intrinsic wavefront statements and complex contour continuation are distinct receiving calculations that still require their complete actual proofs.

## References

- [Melrose] Richard Melrose, *Differential Analysis*, MIT 18.155 lecture notes, 2004, [MIT OpenCourseWare lecture notes](https://ocw.mit.edu/courses/18-155-differential-analysis-fall-2004/pages/lecture-notes/).
- [Beezer] Robert Beezer, *A First Course in Linear Algebra*, [author's source repository](https://github.com/rbeezer/fcla).
