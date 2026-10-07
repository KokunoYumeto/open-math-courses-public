# Bott periodicity

*Written by GPT-6.1 Sol (OpenAI), October 2026. Self-checked by the writing AI. Public domain (CC0).*

A projection gives a loop by rotating its range once and leaving its complement fixed. Bott periodicity says that every stable invertible loop comes from a unique difference of projection classes. We prove this for every complex C*-algebra, including nonunital, nonseparable algebras, by a concrete homotopy in the Toeplitz algebra.

We use [Lesson 9](KT-OPK-09.md), especially its Toeplitz extension and character \(\chi(T_f+k)=f(1)\). We also import compact stability from [Lesson 5, Theorem 4.1](KT-OPK-05.md#4-compact-operator-stabilization) and [Lesson 6, Corollary 4.2](KT-OPK-06.md#4-realizing-an-invertible-path-at-a-late-stage), split exactness and the index formula from [Lesson 7, Corollary 4.2 and Proposition 5.1](KT-OPK-07.md), and the natural suspension isomorphism from [Lesson 8, Theorem 2.1](KT-OPK-08.md#2-the-idempotent-loop-of-an-invertible). These results precede periodicity. Tensor products below are minimal C*-tensor products.

## 1. A projection makes a based loop

Write \(SA=C_0((0,1),A)\), and use \(z(t)=e^{2\pi it}\), with increasing \(t\) the positive circle direction. For a projection \(e\in M_n(D)\) in a unital algebra, put

\[
f_e(t)=z(t)e+I_n-e.
\tag{1.1}
\]

It is unitary, its inverse is \(\overline z e+I_n-e\), and its endpoint values are \(I_n\). Thus it represents an element of \(K_1(SD)\).

**Proposition 1.1.** Formula (1.1) induces a natural homomorphism

\[
\beta_D:K_0(D)\longrightarrow K_1(SD),
\qquad [e]\longmapsto[f_e].
\tag{1.2}
\]

*Proof.* A projection homotopy gives a based loop homotopy by (1.1). Equivalent projections become homotopic after zero stabilization by [Lesson 1, §§3–4](KT-OPK-01.md); adding a zero projection adds an identity loop. Moreover \(f_{e\oplus h}=f_e\oplus f_h\). Hence the map on the projection monoid is well-defined and additive, and extends to its group completion. Applying a *-homomorphism entrywise to the nonconstant part of the loop proves naturality. This also works for a nonunital homomorphism: its extension to the suspension unitization sends the scalar identity to the target scalar identity. \(\square\)

For nonunital \(A\), let \(\epsilon:A^+\to\mathbb C\) be the scalar quotient. Split exactness, also after suspension, identifies

\[
\begin{aligned}
K_0(A)&=\ker\epsilon_*,\\
K_1(SA)&=\ker(S\epsilon)_*.
\end{aligned}
\tag{1.3}
\]

Naturality of \(\beta_{A^+}\) therefore restricts it to \(\beta_A\). Explicitly, represent a relative class as \([e]-[P]\), where \(e\) is a projection over \(A^+\) and \(P=\epsilon(e)\) is its constant scalar projection. Then

\[
\boxed{\beta_A([e]-[P])=[f_e f_P^{-1}].}
\tag{1.4}
\]

The product has scalar part \(I\) for every \(t\) and endpoints \(I\), so belongs to the invertible matrices over \((SA)^+\). The equality with the restricted map follows from the product/block-sum identity in [Lesson 6, Theorem 2.2](KT-OPK-06.md#2-the-rotation-that-makes-addition-commute) and the injectivity in (1.3). This proves representative independence, rather than imposing it as an additional equivalence relation. Unital consistency follows from the same split diagram. We will prove that every \(\beta_A\) is an isomorphism.

## 2. Exact Toeplitz extensions with coefficients

Let \(\mathcal T=C^*(S)\) on \(H^2\), \(p_0=1-SS^*\), \(\mathcal K=K(H^2)\), and \(\sigma:\mathcal T\to C(\mathbb T)\) its symbol map. Put \(\mathcal T_0=\ker\chi\), where \(\chi=\operatorname{ev}_1\sigma\).

**Lemma 2.1 (universal isometry).** An isometry \(V\) in a unital C*-algebra determines a unique unital *-homomorphism \(\mathcal T\to C^*(V)\) sending \(S\) to \(V\). A corner isometry \(V^*V=p\), \(VV^*\leq p\), similarly determines a homomorphism with unit image \(p\).

*Proof.* Faithfully represent the target algebra on a Hilbert space. For an isometry \(V\), let \(D=\ker V^*\). The spaces \(V^jD\) are pairwise orthogonal, and

\[
I-V^NV^{*N}=\sum_{j=0}^{N-1}V^j(I-VV^*)V^{*j}.
\tag{2.1}
\]

The increasing ranges on the right have closed union \(H_s=\bigoplus_{j\geq0}V^jD\); their orthogonal complement is \(H_u=\bigcap_{N\geq0}V^NH\). Both reduce \(V\). It acts as copies of \(S\) on \(H_s\), and as a unitary on \(H_u\): on the latter \(VV^*=I\), and \(V^*\) preserves every \(V^NH\). For any *-polynomial \(r\), the norm on \(H_s\) is at most \(\|r(S)\|\); on \(H_u\), continuous functional calculus gives the bound \(\|r(z)\|_\infty\leq\|r(S)\|\), using the symbol quotient of Lesson 9. Thus evaluation at \(V\) is well-defined and contractive on the dense *-polynomial algebra, and extends to the required homomorphism. Uniqueness follows from the generator. Apply this argument in the corner \(pEp\) for the last assertion; the zero corner gives the zero map. \(\square\)

**Lemma 2.2 (coefficient exactness).** For every C*-algebra \(B\), the sequences

\[
\begin{aligned}
0&\longrightarrow B\otimes\mathcal K
\longrightarrow B\otimes\mathcal T\\
&\xrightarrow{\mathrm{id}\otimes\sigma} C(\mathbb T,B)
\longrightarrow0,\\
0&\longrightarrow B\otimes\mathcal K
\longrightarrow B\otimes\mathcal T_0\\
&\xrightarrow{\mathrm{id}\otimes\sigma} SB
\longrightarrow0
\end{aligned}
\tag{2.2}
\]

are exact. Here \(SB\) is identified with the functions on the circle vanishing at \(1\).

*Proof.* Faithfully represent \(B\) on \(H_B\). For \(F\in C(\mathbb T,B)\), multiply on \(L^2(\mathbb T)\otimes H_B\) and compress to \(H^2\otimes H_B\). This gives a contractive linear map \(s_B\). For a finite \(B\)-valued trigonometric polynomial, its compression is a finite sum \(\sum T_{z^j}\otimes b_j\), with tensor factors flipped if necessary, and its symbol is \(F\). Such polynomials are uniformly dense: a finite partition of unity approximates a continuous Banach-valued function by finite scalar functions times values in \(B\), and scalar trigonometric approximation approximates the scalar functions. Consequently \(s_B\) takes values in \(B\otimes\mathcal T\) and is a right inverse to the symbol map.

For an algebraic tensor \(x=\sum b_j\otimes a_j\), each
\(a_j-T_{\sigma(a_j)}\) is compact by Lesson 9. Hence
\(x-s_B\sigma_B(x)\in B\odot\mathcal K\). If \(\sigma_B(x)=0\) for a general completed tensor, approximate \(x\) by algebraic tensors \(x_m\). Boundedness of \(I-s_B\sigma_B\) shows
\(x_m-s_B\sigma_B(x_m)\to x\), proving the exact kernel assertion. Minimal tensor products preserve inclusions, so the indicated kernel is the stated completed tensor algebra.

The character extension \(0\to\mathcal T_0\to\mathcal T\xrightarrow\chi\mathbb C\to0\) has *-section \(j(\lambda)=\lambda1\). A *-split extension remains exact after tensoring with any \(B\): for its quotient \(q\) and section \(s\), \(\mathrm{id}_B\otimes sq\) is a bounded *-homomorphism. Applying \(I-\mathrm{id}_B\otimes sq\) to algebraic approximations proves the kernel equality just as above. It follows that the tensors with zero character are precisely \(B\otimes\mathcal T_0\). For a symbol \(F\) with \(F(1)=0\), its compression already has zero character. Restrict the first sequence to obtain the second. No exactness hypothesis on \(B\) has been used. \(\square\)

The bounded linear compression section need not be multiplicative. The proof uses its boundedness to identify the kernel; it does not turn the Toeplitz extension into a *-split extension.

## 3. The homotopy that removes the reduced Toeplitz algebra

**Theorem 3.1.** For every C*-algebra \(B\), the maps

\[
j_B:B\to B\otimes\mathcal T,\quad b\mapsto b\otimes1,
\qquad \chi_B=\mathrm{id}_B\otimes\chi
\]

induce mutually inverse isomorphisms on \(K_0\) and \(K_1\). In particular,

\[
K_i(B\otimes\mathcal T_0)=0\quad(i=0,1).
\tag{3.1}
\]

*Proof.* We first construct the homotopy before introducing \(B\). Inside \(\mathcal T\otimes\mathcal T\), define

\[
\widehat{\mathcal T}
=C^*(\mathcal K\otimes\mathcal T,\mathcal T\otimes1),
\qquad v=S\otimes1.
\tag{3.2}
\]

Apply Lemma 2.2 with coefficient algebra \(\mathcal T\), then flip the factors. The restriction of \(\sigma\otimes\mathrm{id}\) to (3.2) has kernel \(\mathcal K\otimes\mathcal T\) and image \(C(\mathbb T)\otimes1\). Denote the resulting quotient by \(\widehat\sigma\), so \(\widehat\sigma(v)=z\). Its quotient is \(C(\mathbb T)\). Form the pullback

\[
\mathcal P=
\{(x,y)\in\widehat{\mathcal T}\oplus\mathcal T:
\widehat\sigma(x)=\sigma(y)\}.
\tag{3.3}
\]

Projection onto \(y\) gives a *-split extension with kernel \(\mathcal K\otimes\mathcal T\) and section \(y\mapsto(y\otimes1,y)\).

Set

\[
\begin{aligned}
f&=p_0\otimes1,& w&=p_0\otimes S,& g&=p_0\otimes p_0,\\
h&=vfv^*,& a&=v(1-f)v^*.
\end{aligned}
\tag{3.4}
\]

The projections \(a,h,f\) are orthogonal and sum to \(1\). Also \(w^*w=f\), \(ww^*=f-g\). The partial isometry \(wv^*\) exchanges \(h\) with \(f-g\), and \(fv^*\) exchanges \(h\) with \(f\). Therefore

\[
\begin{aligned}
Z_0&=a+wv^*+vw^*+g,\\
Z_1&=a+fv^*+vf
\end{aligned}
\tag{3.5}
\]

are self-adjoint unitaries. Indeed each exchanged pair contributes its two support projections to the square, all cross-products with the complementary identity projections are zero, and those supports exhaust \(1\). Their quotient symbols are both \(1\).

Let \(E_j=(1-Z_j)/2\), and put

\[
Z_t=e^{i\pi tE_1}e^{i\pi(1-t)E_0},
\qquad v_t=Z_tv\quad(0\leq t\leq1).
\tag{3.6}
\]

These are norm-continuous unitaries and isometries, respectively; \(Z_t\) has quotient \(1\), and its endpoints are \(Z_0,Z_1\). Lemma 2.1 defines a homotopy \(\phi_t:\mathcal T\to\widehat{\mathcal T}\), \(\phi_t(S)=v_t\). It is pointwise norm-continuous because this is true on *-polynomials and all these homomorphisms are contractive. Multiplication of (3.5) by \(v\) gives

\[
\begin{aligned}
\phi_0(S)&=v(1-f)+w,\\
\phi_1(S)&=v(1-f)+f.
\end{aligned}
\tag{3.7}
\]

In (3.3), define \(\psi_t(S)=(v_t,S)\). Also define the two corner homomorphisms

\[
\begin{aligned}
\psi(S)&=(v(1-f),S),&\psi(1)&=(1-f,1),\\
\omega(S)&=(w,0),&\omega(1)&=(f,0).
\end{aligned}
\tag{3.8}
\]

The displayed generators are isometries in their indicated corners. Their quotient symbols satisfy the pullback condition. The two corners are orthogonal and their units sum to \((1,1)\). Formula (3.7) therefore implies equalities of homomorphisms

\[
\psi_0=\psi+\omega,
\qquad \psi_1=\psi+\omega j\chi.
\tag{3.9}
\]

For orthogonal-range homomorphisms \(\rho,\eta:D\to E\), one has
\((\rho+\eta)_*=\rho_*+\eta_*\) on either K-group. To see this even for nonunital algebras, factor the sum through \(D\xrightarrow{\Delta}D\oplus D\xrightarrow{\rho\oplus\eta}E\). Direct-sum K-theory identifies \(\Delta_*x=(x,x)\); the last induced map is the sum of its two restrictions. These are the direct-sum statements of Lessons 4 and 6.

Now tensor all these maps with \(B\). Their homotopies remain pointwise norm-continuous, by density of finite tensors and contractivity. The map \(\omega_B\) factors as

\[
B\otimes\mathcal T
\xrightarrow{\ c\ }B\otimes\mathcal K\otimes\mathcal T
\xrightarrow{\ \iota\ }B\otimes\mathcal P,
\qquad c(b\otimes y)=b\otimes p_0\otimes y.
\tag{3.10}
\]

Compact stability makes \(c_*\) an isomorphism. The *-split pullback extension stays exact after tensoring by Lemma 2.2's split-extension argument, and split K-exactness makes \(\iota_*\) injective. Thus \((\omega_B)_*\) is injective. Homotopy invariance and (3.9) give

\[
(\psi_B)_*+(\omega_B)_*
=(\psi_B)_*+(\omega_B)_*(j_B\chi_B)_*.
\]

Subtract the common summand and cancel this injective map. It follows that \((j_B\chi_B)_*=\mathrm{id}\). The reverse composite \(\chi_Bj_B\) is literally \(\mathrm{id}_B\). Finally the split character extension identifies \(K_i(B\otimes\mathcal T)\) with \(K_i(B\otimes\mathcal T_0)\oplus K_i(B)\). Since its section already induces an isomorphism, the first summand is zero. \(\square\)

The injectivity in (3.10) uses both compact stability and the split ideal inclusion. Split exactness alone would not make the corner map an isomorphism. In (3.7), the final summand is \(f\): replacing it by \(g\) gives initial projection \(1-f+g\), so fails the isometry equation. These checks also fix the pullback (3.3) over the actual quotient circle algebra.

## 4. The boundary proves periodicity and fixes its sign

**Theorem 4.1 (Bott periodicity).** The map \(\beta_A:K_0(A)\to K_1(SA)\) is a natural isomorphism for every complex C*-algebra \(A\). Under compact stability, the index boundary of the second extension in (2.2) satisfies

\[
\boxed{\partial_A\beta_A=-\mathrm{id}_{K_0(A)}.}
\tag{4.1}
\]

*Proof.* The exact segment from Lesson 7 for the second extension in (2.2) is

\[
\begin{aligned}
K_1(B\otimes\mathcal T_0)
&\longrightarrow K_1(SB)\\
&\xrightarrow{\partial_B}K_0(B\otimes\mathcal K)\\
&\longrightarrow K_0(B\otimes\mathcal T_0).
\end{aligned}
\tag{4.2}
\]

The outside groups vanish by Theorem 3.1; compact stability identifies the middle target with \(K_0(B)\). Thus \(\partial_B\) is an isomorphism for every \(B\).

For unital \(B\) and a projection \(e\in M_n(B)\), lift \(f_e\) to

\[
V_e=S\otimes e+1\otimes(I_n-e).
\tag{4.3}
\]

Its character is \(I_n\), so \(V_e-I_n\) belongs to \(M_n(B\otimes\mathcal T_0)\), after the tensor flip. Direct multiplication gives

\[
V_e^*V_e=I_n,
\qquad I_n-V_eV_e^*=p_0\otimes e.
\tag{4.4}
\]

The partial-isometry boundary is initial defect minus final defect, by Lesson 7, Proposition 5.1. Hence
\(\partial_B[f_e]=0-[p_0\otimes e]=-[e]\). This already gives \(\partial_\mathbb C[z]=-1\), the shift convention of Lesson 9. Additivity proves (4.1) on \(K_0(B)\). Since \(\partial_B\) is an isomorphism, \(\beta_B=-\partial_B^{-1}\) is one too.

For nonunital \(A\), use the two split kernel identifications (1.3). The natural maps \(\beta_{A^+}\) and \(\beta_\mathbb C\) are isomorphisms, so their commuting diagram restricts to an isomorphism of kernels: injectivity is inherited; for surjectivity, an element of the lower kernel has a unique preimage upstairs, whose scalar image must be zero by injectivity of \(\beta_\mathbb C\). Naturality of the coefficient Toeplitz boundaries, followed by the injective map \(K_0(A)\to K_0(A^+)\), proves (4.1) for \(A\). There is no need to assume that a product of two relative partial-isometry lifts is itself a partial isometry. \(\square\)

## 5. The polynomial-loop route: an outline with explicit reductions

Here is the finite-dimensional algebra behind the alternative polynomial proof. The reductions work over any unital complex Banach algebra \(D\); for the present course \(D\) is a C*-algebra. Reduction from a nonunital algebra is the split kernel diagram (1.3).

First, a based continuous invertible loop \(u:\mathbb T\to GL_n(D)\) is based-homotopic to a Laurent polynomial loop. To verify the analytic step, convolve with the Fejér kernel

\[
F_N(\theta)=\frac1{N+1}
\left|\sum_{j=0}^N e^{ij\theta}\right|^2.
\]

It is nonnegative, has normalized integral one, and its integral outside any fixed arc about zero tends to zero, by the geometric-sum bound \(F_N(\theta)\leq((N+1)\sin^2(\theta/2))^{-1}\). Uniform continuity gives uniform convergence of these Banach-valued convolutions to \(u\). If \(M=\sup_z\|u(z)^{-1}\|\), choose a polynomial \(g\) with \(\|g-u\|_\infty<M^{-1}\). The Neumann series makes every straight interpolation between \(u\) and \(g\) invertible. Normalize each interpolation \(H\) by \(H(z)H(1)^{-1}\). This makes the homotopy based, and its endpoint is the based Laurent polynomial \(g(z)g(1)^{-1}\). The argument is uniform for a continuous family of loops, since a compact family has a common inverse bound and uniform continuity.

Multiply a based Laurent loop by \(z^N I_n\) to obtain a polynomial
\(f(z)=a_0+a_1z+\cdots+a_mz^m\) with \(f(1)=I_n\). The multiplication changes its K-class by \(N\beta_D[I_n]\). The next lemma supplies a linear loop in a larger matrix algebra.

**Lemma 5.1 (finite linearization).** In block size \(n\), form the \((m+1)\)-by-\((m+1)\) block matrix

\[
\begin{gathered}
\mu_m(f)(z)=\\
\begin{pmatrix}
a_0&a_1&\cdots&a_m\\
-zI&I&\cdots&0\\
0&-zI&\ddots&\vdots\\
\vdots&\ddots&\ddots&I
\end{pmatrix}.
\end{gathered}
\tag{5.1}
\]

Precisely, the top-row blocks are \((\mu_m)_{0j}=a_j\); for \(1\leq j\leq m\), its only other nonzero blocks are \((\mu_m)_{jj}=I\) and \((\mu_m)_{j,j-1}=-zI\). It is pointwise invertible exactly when \(f\) is. The normalized linear loop
\(\widehat\mu_m(f)(z)=\mu_m(f)(z)\mu_m(f)(1)^{-1}\) is based-homotopic to \(\operatorname{diag}(f,I_{mn})\). For \(m=0\), use \(\mu_0(f)=f\).

*Proof.* Index the block rows and columns from \(0\) to \(m\). Work downward from \(j=m\) to \(1\). At stage \(j\), the first row through column \(j\) is
\((a_0,\ldots,a_{j-1},A_j)\), where
\(A_j=a_j+a_{j+1}z+\cdots+a_mz^{m-j}\); the rows with index greater than \(j\) are already their identity rows. Multiply on the left by the elementary matrix \(I-E_{0j}(A_j)\), where \(E_{ij}(c)\) means the block matrix with sole nonzero block \(c\) at \((i,j)\). This clears column \(j\) in row zero and replaces its preceding coefficient by \(a_{j-1}+A_jz\). Multiply on the right by \(I+E_{j,j-1}(zI)\); this clears the \(-zI\) in row \(j\), without changing the first row, since its column \(j\) is now zero. The other already cleared rows stay fixed. Induction ends at \(\operatorname{diag}(f,I_{mn})\).

Every elementary factor is invertible throughout its path from \(I\), obtained by multiplying its off-diagonal block by \(r\in[0,1]\); its inverse changes that block's sign. Thus these left and right operations provide an explicit homotopy through invertible matrices. The algebraic elimination also proves the invertibility criterion. Normalize the entire homotopy at \(z=1\). Its initial matrix is \(\widehat\mu_m(f)\), and its endpoint is \(\operatorname{diag}(f,I)\), since \(f(1)=I\). Continuity in all coefficients follows from the formulas and continuous inversion. \(\square\)

The normalization matters: \(\mu_m(f)(1)\) is generally not the identity, even for a based \(f\). Without it, the displayed elementary homotopy need not be a homotopy in \((SD)^+\).

**Lemma 5.2 (linear loops retract to idempotent loops).** A based linear invertible loop \(\ell(z)=a+bz\) is homotopic, through based linear invertible loops, to \(f_e(z)=I-e+ze\) for an idempotent \(e\). The idempotent depends continuously on \(\ell\).

*Proof.* Basing gives \(a+b=I\). For \(z\ne1\),

\[
I+(z-1)b=(1-z)\big((1-z)^{-1}I-b\big).
\tag{5.2}
\]

As \(z\) runs around the circle minus \(1\), \((1-z)^{-1}\) runs through the vertical line \(\operatorname{Re}\lambda=1/2\). Therefore the spectrum of \(b\) misses that line. Let \(e\) be its Riesz idempotent for the spectral part to the right of the line, using the holomorphic functional calculus of [Lesson 1](KT-OPK-01.md). It commutes with \(b\). Define \(b_r=(1-r)b+re\). On the right spectral part its spectral values are \((1-r)\lambda+r\), which remain strictly to the right; on the left they are \((1-r)\lambda\), which remain strictly to the left. Holomorphic spectral mapping gives these assertions also for nonnormal \(b\). Equation (5.2) then shows that \(I+(z-1)b_r\) is invertible for every \(z\), and equals \(I\) at \(z=1\). This is the claimed homotopy.

For \(b\) sufficiently close to a fixed \(b_0\), a common finite contour separates the same two parts of the spectrum; the resolvent identity and Neumann series make its Riesz integral continuous. These local definitions agree because they select exactly the right spectral component, giving continuity globally on the domain. \(\square\)

For a C*-algebra, the idempotent \(e\) can be replaced by a projection in its stable homotopy class by Lesson 1. Its idempotent loop has the same K-class as that projection loop. Combining the reductions gives the concrete representation

\[
[u]=\beta_D\big([e]-N[I_n]\big).
\tag{5.3}
\]

This outlines the surjectivity half of the polynomial proof and proves each reduction used in it. The full polynomial method additionally carries homotopies through common Laurent denominators, linearization sizes and identity padding to establish stable uniqueness of the relative idempotent class. In this lesson uniqueness follows from the completed Toeplitz proof, Theorem 4.1: two expressions in (5.3) for the same loop must have equal K₀-classes. It does not assert uniqueness of an unstabilized idempotent or of a denominator. Exercise 10.4 gives the complete finite linearization argument in a directly reusable form.

## 6. Two-periodicity, Euclidean spaces, and the planar sign

Let \(\theta_A:K_1(A)\to K_0(SA)\) be the positive cone-boundary isomorphism of Lesson 8. Define the ordered double suspension

\[
\mathsf B_A=\theta_{SA}\beta_A:
K_0(A)\xrightarrow{\cong}K_0(S^2A).
\tag{6.1}
\]

Apply this to every \(S^nA\). With the higher groups \(K_n(A)=K_0(S^nA)\) and their degree-one identification fixed in Lesson 8, it gives natural isomorphisms \(K_n(A)\cong K_{n+2}(A)\) for all \(n\geq0\). In the same way (3.1), applied to \(S^nB\), proves vanishing of all higher groups of \(B\otimes\mathcal T_0\). We use the usual function-algebra identification \(S^n(B\otimes\mathcal T_0)\cong S^nB\otimes\mathcal T_0\), obtained by uniform approximation of continuous compactly supported functions by finite scalar functions times tensor values.

**Corollary 6.1.** For every \(d\geq0\) and \(i=0,1\),

\[
K_i(C_0(\mathbb R^d))=
\begin{cases}
\mathbb Z,&i\equiv d\pmod2,\\
0,&i\not\equiv d\pmod2.
\end{cases}
\tag{6.2}
\]

*Proof.* For \(d=0\), use \(K_0(\mathbb C)=\mathbb Z[1]\) and \(K_1(\mathbb C)=0\). For \(d=1\), Lesson 8 gives \(K_0(S\mathbb C)=0\), and Theorem 4.1 gives \(K_1(S\mathbb C)=\mathbb Z[z]\). Identify increasing real coordinates with \(t\in(0,1)\) by \(x=-\cot(\pi t)\). Repeated application of (6.1) gives the groups for every subsequent \(d\), together with generators obtained by ordered Bott suspensions of these two base generators. \(\square\)

To fix the planar generator, retain the coordinate order of Lesson 8: the new outer suspension variable \(t\) comes first, the inner loop variable \(s\) second. Set \(x=-\cot(\pi t)\), \(y=-\cot(\pi s)\), and \(\zeta=x+iy\). The projection from [Lesson 4, equation (6.2)](KT-OPK-04.md#6-compact-supports-and-the-determinant-at-the-equator) is

\[
q(\zeta)=\frac1{1+|\zeta|^2}
\begin{pmatrix}1&\overline\zeta\\\zeta&|\zeta|^2\end{pmatrix},
\qquad q(\infty)=P=\begin{pmatrix}0&0\\0&1\end{pmatrix}.
\tag{6.3}
\]

Its relative class is \(\mathfrak b=[q]-[P]\). Lesson 8, equation (4.9), computes its actual finite-to-infinity clutching degree and proves

\[
\boxed{\theta_{S\mathbb C}\beta_\mathbb C[1]
=\mathfrak b,
\qquad
\partial_\mathbb C\theta_{S\mathbb C}^{-1}(\mathfrak b)=-[1].}
\tag{6.4}
\]

Thus \(\mathfrak b\) is the positive generator of \(K_0(C_0(\mathbb R^2))\), while the Toeplitz index of its positive loop antecedent is negative. Exchanging the two real coordinates reverses the clutching degree and gives \(-\mathfrak b\). Swapping the two vector coordinates by a constant unitary instead sends (6.3) to \((1+|\zeta|^2)^{-1}\begin{pmatrix}|\zeta|^2&\zeta\\\overline\zeta&1\end{pmatrix}\), the common alternative Bott projection, and conjugates its scalar projection at the same time. It preserves the relative class. A vector-coordinate swap is therefore different from reversing the orientation of the plane.

For \(A=C(X)\), where \(X\) is compact Hausdorff, the Serre–Swan correspondence of Lesson 2 makes (6.1) the two-periodicity of topological complex K-theory with compact supports on \(\mathbb R^2\times X\). Equivalently, it identifies \(K^0(X)\) with the reduced group of \(S^2\wedge X_+\), where \(X_+\) adds a disjoint base point. Evaluation at \(\infty\in S^2\) gives a split extension with ideal \(C_0(\mathbb R^2,C(X))\), so

\[
K_0(C(S^2\times X))\cong K_0(C(X))\oplus K_0(C(X)).
\tag{6.5}
\]

For \(X\) a point this gives two infinite cyclic summands; Exercise 10.5 derives their basis directly from clutching. The analytic Bott-operator lesson, §2 supplies the separate index-one model \(x+d/dx\). The present coefficient theorem supplies the K-theory periodicity used alongside that analytic construction.

## 7. Exercises with complete solutions

**Exercise 10.1 — The positive scalar loop (basic).** Prove that \(\beta_\mathbb C(1)=[z]\) generates \(K_1(C_0(\mathbb R))\).

*Solution.* For \(e=1\), (1.1) is exactly \(z(t)=e^{2\pi it}\). This is a unitary in \((S\mathbb C)^+\), with scalar part one and equal endpoint values. Under inclusion into \(C(\mathbb T)\), its determinant has winding \(+1\), the generator in Lesson 6, Theorem 5.2. The circle evaluation extension splits, and \(K_1(\mathbb C)=0\), so the inclusion \(K_1(S\mathbb C)\to K_1(C(\mathbb T))\) is an isomorphism. Therefore \([z]\) generates the source, and the increasing real-coordinate identification in Corollary 6.1 gives the claimed line group. This also verifies the normalization independently of the general Bott theorem.

**Exercise 10.2 — Write the homotopy (intermediate).** Give the complete homotopy \(\psi_t\) proving \(K_i(B\otimes\mathcal T_0)=0\), and specify the cancellation used in its proof.

*Solution.* In (3.4), form the two self-adjoint unitaries \(Z_0,Z_1\) of (3.5), their projections \(E_j=(1-Z_j)/2\), and the unitary path \(Z_t\) of (3.6). Its quotient is one. Define \(\psi_t:\mathcal T\to\mathcal P\) by the universal isometry \(S\mapsto(Z_tv,S)\); explicitly it sends a *-polynomial \(r\) to \((r(Z_tv),r(S))\), and extends contractively to every element. Its endpoints send \(S\) to \((v(1-f)+w,S)\) and \((v(1-f)+f,S)\). The complementary corners (3.8) identify these endpoints as \(\psi+\omega\) and \(\psi+\omega j\chi\). After tensoring with \(B\), homotopy invariance and orthogonal additivity give (3.9) on K-groups. The map \(\omega_B\) factors through the compact corner and the ideal inclusion in (3.10); stability makes the first an isomorphism, and the *-split extension makes the second injective. Cancel \((\omega_B)_*\), after subtracting \((\psi_B)_*\), to get \((j_B\chi_B)_*=\mathrm{id}\). Since \(\chi_Bj_B=\mathrm{id}\), the character's split kernel has zero K-groups. All tensors and homotopies are valid for nonunital \(B\) by Lemma 2.2.

**Exercise 10.3 — Which planar sign? (intermediate).** Determine the sign relating \([q]-[1]\) to \(\theta_{S\mathbb C}\beta_\mathbb C(1)\), and compare it with the Toeplitz boundary.

*Solution.* In the shorthand \([q]-[1]\), the subtracted class is the scalar rank-one projection \(P=q(\infty)\). The finite frame of (6.3) is \((1,\zeta)^T\); its infinity frame is \((1/\zeta,1)^T\). The finite frame is \(\zeta\) times the infinity frame, so coefficient transfer from the finite chart to the infinity chart is \(\zeta\), of winding \(+1\) on a counterclockwise equator. Lesson 8's doubled path has this same degree with outer \(t\), inner \(s\), and increasing real coordinates. Its exact computation in equation (4.9) gives the positive equality in (6.4). The shift lift has zero initial defect and rank-one final defect, so \(\partial_\mathbb C\beta_\mathbb C(1)=-1\). Reversing the plane-coordinate order changes the first equality's sign; conjugating both projections by the constant vector-coordinate swap does not.

**Exercise 10.4 — Polynomial linearization (intermediate).** Prove that the linearization \(\mu_m\) in (5.1) preserves the stable homotopy class of a based polynomial loop, including the base point throughout the homotopy.

*Solution.* At the last column use the invertible factors \(I-rE_{0m}(a_m)\), then \(I+rE_{m,m-1}(zI)\), with \(r\) running from zero to one in each path. The first folds the coefficient to \(a_{m-1}+a_mz\) and clears its old column; the second clears the last subdiagonal block. For each successive \(j\), use \(I-rE_{0j}(A_j)\), then \(I+rE_{j,j-1}(zI)\), with \(A_j\) as in Lemma 5.1. These operations involve no commutation of matrix coefficients; only the scalar coordinate \(z\) commutes with them. Each factor has the inverse with the opposite off-diagonal sign because its off-diagonal block squares to zero. The endpoint is exactly \(\operatorname{diag}(f,I_{mn})\); there are no remaining lower-triangular entries. The original matrix is invertible at every \(z\) because elimination gives an invertible endpoint through invertible factors. Let \(H_r(z)\) denote the resulting concatenated homotopy. Replace it at every stage by \(H_r(z)H_r(1)^{-1}\). This remains continuous and invertible and equals \(I\) at \(1\). Its endpoints are \(\mu_m(f)(z)\mu_m(f)(1)^{-1}\) and \(\operatorname{diag}(f(z),I_{mn})\). Thus the normalized linearization represents \([f]\) in \(K_1(SD)\). For a polynomial whose value at \(1\) is merely invertible, the same proof has endpoint \(\operatorname{diag}(f(z)f(1)^{-1},I)\); the normalized statement is still valid.

**Exercise 10.5 — The sphere without using periodicity (advanced).** Prove \(K_0(C(S^2))\cong\mathbb Z^2\) with basis \([1],[q]\) by clutching and determinant degree, then compare with (6.5).

*Solution.* Every bundle is trivial over each closed hemisphere by [Lesson 2, Corollary 4.3](KT-OPK-02.md#4-transport-along-a-cylinder). It therefore has a clutching map \(g:S^1\to GL_r(\mathbb C)\). Its determinant winding \(d(g)\) is independent of the frames: each change of frame extends across its disk, so its determinant loop has winding zero. The determinant-degree construction and its additivity are proved in Lesson 4, §6; rank is constant since the sphere is connected.

Two bundles of the same rank and degree become isomorphic after adding trivial bundles. Indeed their stabilized clutching maps have the same class by the determinant classification in Lesson 6, Theorem 5.2. Pad to a common finite size in which there is an actual invertible-loop homotopy. Gluing the two hemisphere products with that homotopy gives a bundle over \(S^2\times[0,1]\): on a collar of the seam the continuous invertible transition matrix supplies its bundle charts. Homotopy invariance of bundles, Lesson 2, Theorem 4.2, identifies its endpoint bundles. Conversely isomorphic bundles have the same rank and degree, as does adding the same trivial bundle.

Consequently the homomorphism

\[
K_0(C(S^2))\longrightarrow\mathbb Z^2,
\qquad [E]-[F]\longmapsto
(\operatorname{rank}E-\operatorname{rank}F,d(E)-d(F))
\tag{7.1}
\]

is injective: zero coordinates give equal-rank, equal-degree bundles, whose stable isomorphism makes their K₀-difference zero. It is surjective because the trivial line has coordinates \((1,0)\), while (6.3) has coordinates \((1,1)\), by the explicit frame transfer in Exercise 10.3. Their two coordinate vectors form an integral basis: \((r,d)=(r-d)(1,0)+d(1,1)\). Thus \([1],[q]\) is the stated basis. Equivalently \([1],[q]-[1]\) is the basis adapted to evaluation at infinity. Its kernel is generated by the second basis vector, agreeing with (6.5) and (6.4). This proof uses only disk triviality, stable determinant classification and group completion; its sphere computation does not assume Bott periodicity.

## References and exact convention checks

The main proof is the coefficient Toeplitz argument associated with Cuntz, compared with [Blackadar 1998, §9.4.2(d)–(f)]. Equations (3.3) and (3.7) spell out its required quotient and endpoint; (3.10) supplies the compact-stability step needed for cancellation. Definition (1.4) agrees with [Blackadar 1998, Definition 9.1.1]. Section 5 gives the explicit reductions corresponding to Lemmas 9.2.5, 9.2.7 and 9.2.8, with a based normalization at every elementary step.

[Emerson 2024, §8.8] treats the two-degree external-product Bott map. Here the one-degree projection-loop map has type \(K_0(A)\to K_1(SA)\), and its composition with \(\theta_{SA}\) has type \(K_0(A)\to K_0(S^2A)\). The typed, ordered formulas (4.1) and (6.4) specify the signs without identifying maps of different types. They use the positive loop and outer-first suspension convention in Frequency calculus for an action of Euclidean space, “A Bott orientation determined by clutching”, and the unitization convention in K-theory of the leaf space, “Suspension, Bott periodicity and extension boundaries”.

- **[Blackadar 1998]** B. Blackadar, *K-Theory for Operator Algebras*, second edition, MSRI Publications 5, Cambridge University Press, 1998, §§9.1–9.2 and 9.4.2. [Author's corrected second edition](https://www.bruceblackadar.com/Mathematics/book6.pdf).
- **[Emerson 2024]** H. Emerson, *An Introduction to C*-Algebras and Noncommutative Geometry*, Birkhäuser Advanced Texts, 2024, §8.8.
- **[Arici–Mesland 2019]** Francesca Arici and Bram Mesland, *Toeplitz extensions in noncommutative topology and mathematical physics*, arXiv:1911.05823v1, §3.1, pp. 6–7. [Freely readable versioned paper](https://arxiv.org/pdf/1911.05823v1#page=6). This compares the Toeplitz route to Bott periodicity; its cited coefficient K-isomorphism is fully proved in Theorem 3.1 here, and Theorem 4.1 fixes the actual boundary sign. It is not used as an omitted KK-theory or Clifford-algebra proof.
- **[Connes 1994]** A. Connes, *Noncommutative Geometry*, Academic Press, 1994, Chapter II, §1, printed pp. 86–90. [Author's electronic edition](https://alainconnes.org/wp-content/uploads/book94bigpdf.pdf#page=86).
