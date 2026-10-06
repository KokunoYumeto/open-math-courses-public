# Toeplitz operators and the index theorem on the circle

*Written by GPT-6.1 Sol (OpenAI), at Ultra. Independently authored CC0 lesson; self-checked by the writing AI.*

Multiplication by a nonvanishing function on a circle is invertible. Compressing it to nonnegative Fourier modes can lose finitely many directions. The resulting defect counts how often the function winds around zero. For a general circle extension, the integer relating winding to index must also be determined; the two-shift example below shows why. We will construct the quotient that makes this statement precise, compute its connecting map, and then determine the K-theory of the Toeplitz algebra.

We use [the index-map lesson](KT-OPK-07.md), Theorems 2.2, 4.1 and 6.1 and Corollary 4.2, and [the suspension lesson](KT-OPK-08.md). The compact ideal has \(K_0=\mathbb Z\), normalized by rank, by [the nonunital lesson](KT-OPK-04.md), Example 5.2; its \(K_1=0\) follows from [the invertibles lesson](KT-OPK-06.md), Corollary 4.2 and the scalar computation. That lesson's Theorem 5.2 identifies circle \(K_1\) by determinant winding. [The Grothendieck-group lesson](KT-OPK-03.md), Example 5.5, gives \(K_0(C(S^1))=\mathbb Z[1]\).

For Fredholm theory we import Theorem 1.1, Theorem 3.2 and Corollary 3.3 of *Fredholm operators and the stable index* in OA-FOUND-REMAINDER: the parametrix criterion, finite defects, local constancy and compact-perturbation invariance. That lesson uses \(\kappa=\dim\ker T^*-\dim\ker T\). Here, as in Lesson 07, we use the opposite convention

\[
\operatorname{Ind}(T)=\dim\ker T-\dim\ker T^*=-\kappa(T).
\tag{0.1}
\]

All winding numbers are counterclockwise. No periodicity theorem is used in this lesson.

## 1. Compression to the Hardy space

Give \(\mathbb T=S^1\) normalized arc-length measure. The functions \(e_j(z)=z^j\), \(j\in\mathbb Z\), form an orthonormal basis of \(L^2(\mathbb T)\). Set

\[
H^2=\overline{\operatorname{span}}\{e_j:j\geq0\},
\qquad P:L^2(\mathbb T)\longrightarrow H^2.
\tag{1.1}
\]

For \(f\in L^\infty(\mathbb T)\), multiplication \(M_f\) is bounded. Its **Toeplitz compression** is

\[
T_f=PM_f|_{H^2},\qquad
\|T_f\|\leq\|f\|_\infty,\qquad T_f^*=T_{\overline f}.
\tag{1.2}
\]

The adjoint identity follows by taking inner products with vectors of \(H^2\). The matrix coefficient in row \(j\), column \(k\), is \(\widehat f(j-k)\). In particular \(S=T_z\) satisfies

\[
Se_j=e_{j+1},\qquad S^*S=1,
\qquad SS^*=1-p_0,
\tag{1.3}
\]

where \(p_0\) projects onto \(\mathbb C e_0\). Write \(\mathcal T=C^*(S)\) and \(\mathcal K=\mathcal K(H^2)\). We include the identity in this generated algebra; it is already \(S^*S\).

For a continuous matrix function \(F:\mathbb T\to M_n(\mathbb C)\), define \(T_F\) on \(H^2\otimes\mathbb C^n\) by the same compression. Its entries are the operators \(T_{F_{jk}}\).

## 2. The symbol survives modulo compact operators

**Lemma 2.1 (compact semicommutators).** For \(f,g\in C(\mathbb T)\),

\[
T_fT_g-T_{fg}=-PM_f(1-P)M_g|_{H^2}\in\mathcal K.
\tag{2.1}
\]

*Proof.* Insert \(P+(1-P)=1\) between the two multiplication operators. If \(g=z^q\) with \(q\geq0\), the right side is zero. If \(q=-r<0\), the range of \((1-P)M_g|_{H^2}\) is contained in the span of \(e_{-r},\ldots,e_{-1}\). Thus the right side has finite rank for trigonometric-polynomial \(g\), for every bounded \(f\). Approximate continuous \(g\) uniformly by such polynomials. The error on the right has norm at most \(\|f\|_\infty\|g-g_m\|_\infty\), so its limit is compact. This also proves the asserted result when both functions are continuous. Entrywise summation proves the matrix version. \(\square\)

The operators

\[
E_{jk}=S^jp_0(S^*)^k,\qquad j,k\geq0,
\tag{2.2}
\]

send \(e_k\) to \(e_j\) and kill the other basis vectors. Their finite spans are dense in \(\mathcal K\); hence \(\mathcal K\subset\mathcal T\). Also \(T_{z^q}=S^q\) for \(q\geq0\), and \(T_{z^{-r}}=(S^*)^r\). Uniform trigonometric approximation therefore places every continuous \(T_f\) in \(\mathcal T\).

We must still prove that no nonzero continuous symbol becomes compact.

**Lemma 2.2 (the essential norm).** For \(f\in C(\mathbb T)\) and \(k\in\mathcal K\),

\[
\|T_f\|=\|f\|_\infty,
\qquad \|T_f+k\|\geq\|f\|_\infty.
\tag{2.3}
\]

*Proof.* Let \(v\) be a finite Laurent polynomial of norm one in \(L^2\). For sufficiently large \(N\), \(z^Nv\in H^2\). Its compressed image has norm

\[
\|T_f(z^Nv)\|=\|P(z^Nfv)\|
\longrightarrow\|fv\|_2.
\tag{2.4}
\]

Indeed the discarded negative Fourier tail of the fixed \(L^2\) function \(fv\) tends to zero. Finite Laurent polynomials are dense in \(L^2\). Taking their supremum in (2.4) gives \(\|T_f\|\geq\|M_f\|=\|f\|_\infty\); the reverse inequality is (1.2).

The matrix coefficients show that \((S^*)^NT_fS^N=T_f\). For a rank-one operator \(k=\xi\otimes\eta^*\),
\(\|kS^N\|=\|\xi\|\|(S^*)^N\eta\|\to0\). Finite-rank approximation gives the same limit for every compact \(k\). Consequently

\[
\|T_f+k\|\geq
\|(S^*)^N(T_f+k)S^N\|
\longrightarrow\|T_f\|.
\]

This proves the second assertion. \(\square\)

**Theorem 2.3 (the Toeplitz extension).** Every element of \(\mathcal T\) has a unique expression \(T_f+k\), with \(f\in C(\mathbb T)\) and \(k\in\mathcal K\). The map \(\sigma(T_f+k)=f\) gives an exact sequence of C*-algebras

\[
0\longrightarrow\mathcal K\longrightarrow\mathcal T
\xrightarrow{\ \sigma\ }C(\mathbb T)\longrightarrow0.
\tag{2.5}
\]

*Proof.* The set \(\{T_f+k\}\) is a *-algebra by Lemma 2.1 and the fact that compacts form an ideal of \(B(H^2)\). It is closed: if \(T_{f_m}+k_m\) is Cauchy, (2.3) makes \(f_m\) uniformly Cauchy, with continuous limit \(f\). Then \(T_{f_m}\to T_f\), so \(k_m\) also converges, to a compact \(k\). This closed algebra contains \(S\) and is contained in \(\mathcal T\), so equals \(\mathcal T\). Lemma 2.2 proves uniqueness and continuity of \(\sigma\). Equation (2.1) proves multiplicativity, (1.2) proves preservation of adjoints, and \(f\mapsto T_f\) proves surjectivity. Its kernel is precisely \(\mathcal K\). \(\square\)

The compression map \(f\mapsto T_f\) is a bounded linear section. It is not multiplicative: \(T_zT_{\overline z}=1-p_0\), whereas \(T_{z\overline z}=1\). Later we will prove that (2.5) has no homomorphic section at all.

## 3. The connecting map is minus winding

**Theorem 3.1 (continuous scalar and matrix symbols).** For every \(F\in M_n(C(\mathbb T))\), \(T_F\) is Fredholm if and only if \(\det F(z)\neq0\) for every \(z\in\mathbb T\). In that case

\[
\operatorname{Ind}(T_F)
=-\operatorname{wind}(\det F).
\tag{3.1}
\]

*Proof.* If \(F\) is pointwise invertible, compactness of the circle makes its inverse continuous. The matrix version of (2.1) gives a parametrix \(T_{F^{-1}}\). Thus \(T_F\) is Fredholm by the imported criterion.

For the converse, (2.5) embeds \(M_n(C(\mathbb T))\) faithfully as a unital C*-subalgebra of the Calkin algebra on \(H^2\otimes\mathbb C^n\), through \(F\mapsto\pi(T_F)\). Faithfulness follows entrywise from Lemma 2.2. A unital C*-subalgebra is inverse closed: if \(b\) is invertible in the ambient algebra, \(b^*b\) has a positive spectral gap; continuous functional calculus, or uniform polynomial approximation to its reciprocal on that spectral interval, puts \((b^*b)^{-1}b^*\) in the subalgebra. Therefore an invertible \(\pi(T_F)\) forces \(F\) invertible. This is equivalent to the stated determinant condition.

Let \(\partial\) denote the connecting map of (2.5). The inclusion \(\mathcal T\subset B(H^2)\) and the symbol embedding into the Calkin algebra give a morphism from (2.5) to the Calkin extension, with the identity on the compact ideal. Naturality and Lesson 07, Theorem 6.1, yield

\[
\partial[F]=\operatorname{Ind}(T_F)
\quad\text{in }K_0(\mathcal K)=\mathbb Z.
\tag{3.2}
\]

In particular the isometry \(S\) lifts \(z\), so the partial-isometry formula gives

\[
\partial[z]=[1-S^*S]-[1-SS^*]
=-[p_0]=-1.
\tag{3.3}
\]

Lesson 06, Theorem 5.2, identifies \(K_1(C(\mathbb T))\) with \(\mathbb Z\) by \([F]\mapsto\operatorname{wind}(\det F)\), taking \([z]\) to 1. Since \(\partial\) is a homomorphism, (3.3) determines it as minus that identification. Equations (3.2)–(3.3) prove (3.1) for every continuous invertible matrix symbol, without a differentiability hypothesis. \(\square\)

Continuity alone does not imply Fredholmness. For example \(T_0=0\) on the infinite-dimensional space \(H^2\) is not Fredholm. The nonvanishing hypothesis omitted in [E, Corollary 2.5.2] is necessary; the preceding theorem supplies the corrected exact criterion.

**Examples 3.2.** For all integers \(k\), \(T_{z^k}\) has index \(-k\). When \(k\geq0\), it is \(S^k\): its kernel is zero and its cokernel has basis \(e_0,\ldots,e_{k-1}\). When \(k=-r<0\), it is \((S^*)^r\): those first \(r\) vectors span its kernel and its range is all of \(H^2\).

For \(F=\operatorname{diag}(z^2,z^{-5},1)\), the determinant winds \(-3\) times, and the index is 3. Directly, the three block indices are \(-2,5,0\), whose sum is 3.

The function \(f(z)=2+z\) has winding zero: \(2+tz\), \(0\leq t\leq1\), is a nonvanishing homotopy to a constant. Here invertibility of the compression can be seen directly:

\[
(2I+S)^{-1}=\frac12\sum_{j=0}^{\infty}(-S/2)^j,
\tag{3.4}
\]

with convergence in operator norm. Section 5 proves the corresponding invertibility assertion for every scalar nonvanishing symbol of winding zero.

**Corollary 3.3 (nonsplitting).** The Toeplitz extension has no *-homomorphic section, and more generally no bounded algebra-homomorphic section.

*Proof.* A section \(s\) would make \(\sigma_*s_*=1\) on \(K_1\). Exactness gives \(\partial\sigma_*=0\), hence \(\partial=\partial\sigma_*s_*=0\). Equation (3.3) contradicts this. This uses the nonunital functorial convention too, so does not require the proposed section to preserve the identity. \(\square\)

## 4. Two K-theory computations before Bott periodicity

**Theorem 4.1.** The scalar inclusion \(j:\mathbb C\to\mathcal T\), \(\lambda\mapsto\lambda1\), induces isomorphisms on \(K_0\) and \(K_1\). Explicitly,

\[
K_0(\mathcal T)=\mathbb Z[1],\qquad K_1(\mathcal T)=0.
\tag{4.1}
\]

*Proof.* The already proved extension sequence has the segment

\[
\begin{aligned}
0&\longrightarrow K_1(\mathcal T)
\longrightarrow\mathbb Z
\xrightarrow{\ -1\ }\mathbb Z\\
&\longrightarrow K_0(\mathcal T)
\xrightarrow{\ \sigma_*\ }\mathbb Z[1].
\end{aligned}
\tag{4.2}
\]

The first zero is \(K_1(\mathcal K)\); the next two integers are circle \(K_1\) and compact-ideal \(K_0\). Exactness and the bijective middle arrow give \(K_1(\mathcal T)=0\) and make the compact-ideal map on \(K_0\) zero. Thus \(\sigma_*\) on \(K_0\) is injective. It is onto because \([1_{\mathcal T}]\) maps to the generator \([1_{C(\mathbb T)}]\). This proves (4.1) and identifies \(j_*\) on \(K_0\) as an isomorphism. On \(K_1\), both scalar and Toeplitz groups are zero. We have not assumed surjectivity at the final term of an arbitrary extension sequence. \(\square\)

Define the character \(\chi=\operatorname{ev}_1\circ\sigma\) and its kernel

\[
\mathcal T_0=\ker\chi
=\{T_f+k:f(1)=0,\ k\in\mathcal K\}.
\tag{4.3}
\]

**Corollary 4.2.** For \(j=0,1\), \(K_j(\mathcal T_0)=0\). The character \(\chi_*\) is the inverse of the scalar inclusion on these two groups.

*Proof.* The extension \(0\to\mathcal T_0\to\mathcal T\xrightarrow{\chi}\mathbb C\to0\) does split, by the scalar inclusion. Lesson 07, Corollary 4.2, gives

\[
K_j(\mathcal T)\cong K_j(\mathcal T_0)\oplus K_j(\mathbb C),
\qquad j=0,1,
\tag{4.4}
\]

with the second summand carried by the scalar inclusion and projection to it given by \(\chi_*\). Theorem 4.1 says that this summand already accounts for the whole group. Hence the first summand is zero. \(\square\)

Here \(K_*\) denotes the two groups \(K_0,K_1\). Vanishing of all higher groups will follow after the periodicity theorem. Also, tensoring these calculations with an arbitrary coefficient algebra is a separate theorem; the scalar calculation does not prove it.

Restricting the symbol map gives a useful second nonsplit extension:

\[
0\longrightarrow\mathcal K\longrightarrow\mathcal T_0
\longrightarrow C_0(\mathbb T\setminus\{1\})
\longrightarrow0.
\tag{4.5}
\]

To verify surjectivity, a continuous symbol vanishing at 1 has its lift \(T_f\in\mathcal T_0\). The kernel is still \(\mathcal K\). Identify the quotient with \(S\mathbb C=C_0((0,1))\) by \(z=e^{2\pi it}\). Its normalized winding-one unitary is \(\omega(t)=e^{2\pi it}\) in the unitization. The quotient inclusion into \(C(\mathbb T)\) sends it to \(z\). Naturality of the connecting map therefore gives

\[
\partial_{\mathcal T_0}[\omega]=-[p_0].
\tag{4.6}
\]

This sign will matter when the next lesson introduces coefficient algebras.

## 5. Coburn's lemma and actual invertibility

Index zero counts equal defects; it does not generally say that both defects vanish. The scalar Toeplitz structure supplies an additional argument.

We first give the analytic fact needed below, with its proof. A vector \(a\in H^2\) with Fourier coefficients \(a_n\) defines the holomorphic function \(A(w)=\sum_{n\geq0}a_nw^n\) on the disk. Cauchy–Schwarz gives convergence there, and Parseval gives \(A(r\,\cdot)\to a\) in \(L^2(\mathbb T)\) as \(r\uparrow1\).

**Lemma 5.1 (boundary uniqueness).** A nonzero vector of \(H^2\) is nonzero almost everywhere on \(\mathbb T\).

*Proof.* Factor \(A(w)=w^kG(w)\), where \(G(0)\neq0\); shifting coefficients shows that \(G\) also has square-summable coefficients. For a radius \(r<1\) with no zero on its circle, factor the finitely many zeros \(a_1,\ldots,a_m\) in \(|w|<r\), with multiplicities. The remaining factor has a harmonic logarithm of its modulus on the closed disk. Its mean-value identity and
\(\frac1{2\pi}\int\log|re^{i\theta}-a_j|\,d\theta=\log r\)
give

\[
\begin{aligned}
&\frac1{2\pi}\int_0^{2\pi}
\log|G(re^{i\theta})|\,d\theta\\
&\quad=\log|G(0)|+\sum_{j=1}^m\log\frac r{|a_j|}\\
&\quad\geq\log|G(0)|.
\end{aligned}
\tag{5.1}
\]

The identity for a linear factor follows by expanding \(\log(1-(a_j/r)e^{-i\theta})\): all nonconstant Fourier terms have mean zero. There is no zero at 0. The zero-free remaining factor admits a holomorphic logarithm on the disk, which justifies the harmonic mean identity.

Write \(\log^+x=\max(\log x,0)\) and \(\log^-x=\max(-\log x,0)\). Since \(\log^+x\leq x^2\), the means of \(\log^+|G(r\,\cdot)|\) are bounded by its squared Hardy norm. Equation (5.1) gives a uniform bound for the means of \(\log^-|G(r\,\cdot)|\) as well. Choose radii tending to 1, avoiding the countably many radii of zeros, along which the \(L^2\) radial convergence has an almost-everywhere convergent subsequence. If the boundary vector vanished on a set of positive measure, the nonnegative functions \(\log^-|G(r\,\cdot)|\) would tend to infinity there. Fatou's lemma contradicts their uniform integral bound. Multiplication by \(z^k\) does not change the boundary zero set. \(\square\)

**Theorem 5.2 (Coburn's lemma).** If \(f\in L^\infty(\mathbb T)\) is not zero almost everywhere, at least one of \(T_f,T_f^*\) is injective. In particular this holds for every nonzero continuous scalar symbol. For the classical attribution and a broader Banach-space version, see [Karlovich, Theorem 1.1 and its historical discussion](https://arxiv.org/pdf/1708.01475).

*Proof.* Suppose instead that \(0\neq a\in\ker T_f\) and \(0\neq b\in\ker T_f^*\). The negative-frequency space is \(\overline z\,\overline{H^2}\), so there exist \(c,d\in H^2\) with

\[
fa=\overline z\,\overline c,
\qquad \overline f\,b=\overline z\,\overline d.
\tag{5.2}
\]

Conjugate the second equality, multiply it by \(a\), and multiply the first by \(\overline b\). The two expressions for \(fa\overline b\) give

\[
z\,ad=\overline z\,\overline{cb}.
\tag{5.3}
\]

Products of two \(H^2\) boundary vectors belong to \(L^1\) by Cauchy–Schwarz, and have only nonnegative Fourier coefficients. Indeed their analytic polynomial approximations converge in \(L^2\), hence their products converge in \(L^1\). The left side of (5.3) has only strictly positive frequencies; the right side has only strictly negative frequencies. Therefore all Fourier coefficients of their common \(L^1\) function vanish, so it is zero. The Fourier uniqueness used here follows, for example, by convolution with the Fejér kernels, which approximates every \(L^1\) function in \(L^1\).

Let \(D\) be the holomorphic function associated to \(d\), as \(A\) is associated to \(a\). The analytic product \(AD\) has the coefficients of the zero boundary product \(ad\), so is identically zero. Since \(A\) is not identically zero, the identity theorem makes \(D=0\), so \(d=0\). The second equality in (5.2) is then \(\overline f\,b=0\). Lemma 5.1 says \(b\neq0\) almost everywhere, forcing \(f=0\) almost everywhere, a contradiction. \(\square\)

**Corollary 5.3.** If \(f\in C(\mathbb T)\) is nowhere zero and has winding zero, \(T_f\) is invertible.

*Proof.* Theorem 3.1 gives closed range and equal finite dimensions of \(\ker T_f\) and \(\ker T_f^*\). Theorem 5.2 makes one of these spaces zero, hence both zero. The range is closed and has orthogonal complement \(\ker T_f^*=0\), so it is all of \(H^2\). The bounded inverse theorem completes the proof. \(\square\)

The scalar hypothesis matters. The matrix symbol \(F=\operatorname{diag}(z,z^{-1})\) is invertible with determinant 1, but \(T_F=\operatorname{diag}(S,S^*)\) has a one-dimensional kernel and cokernel. Its index is zero and it is not invertible. Thus Theorem 3.1 extends to matrices, while Corollary 5.3 does not extend merely by replacing winding with determinant winding.

## 6. Matching the positive spectral convention

On \(L^2(\mathbb R/2\pi\mathbb Z)\), let \(D_0=-i\,d/dx\). Its Fourier eigenvalue on \(e^{ijx}\) is \(j\). Our Hardy projection is \(\mathbf1_{[0,\infty)}(D_0)\). For \(D_\eta=D_0+\eta\), \(0<\eta<1\), it is the strictly positive spectral projection. Consequently the positive compression of multiplication by \(e^{ix}\) is exactly \(S\), with index \(-1\).

This agrees with *The local index formula*, NCG-LOCAL-INDEX, §§1–2, which uses \(D_\eta\), and with its Exercise 24: \(\operatorname{diag}(e^{2ix},e^{-5ix},1)\) has index 3. Its residue formula is not needed here.

If one instead uses \(\mathbf1_{(0,\infty)}(D_0)\), the constant Fourier mode is removed. On \(H^2=\mathbb C e_0\oplus\overline{\operatorname{span}}\{e_j:j\geq1\}\), the two off-diagonal blocks of a bounded compression have finite rank. The remaining scalar block acts on a one-dimensional space and has index zero. Compact-perturbation invariance therefore gives the same index for the strictly positive compression. In particular \(e^{ix}\) misses its first positive mode and still has index \(-1\). Compressing to nonpositive rather than nonnegative frequencies changes the shift to a backward shift and reverses the winding sign.

### The integer attached to a circle extension

The Toeplitz extension has boundary coefficient \(-1\). A different algebra with the same circle quotient need not have that coefficient. This is the point at which an abstract index formula must retain information about its extension.

**Proposition 6.1 (the extension coefficient).** Let \(H\) be an infinite-dimensional Hilbert space and let \(\mathcal E\subset B(H)\) be a unital C*-algebra containing \(\mathcal K(H)\), with a specified quotient isomorphism
\(q:\mathcal E/\mathcal K(H)\cong C(S^1)\). There is a unique integer \(k\) such that every Fredholm \(T\in M_n(\mathcal E)\), with invertible symbol \(F=q_n(T)\), satisfies

\[
\operatorname{Ind}(T)=k\,\operatorname{Wind}(\det F).
\tag{6.1}
\]

Here \(k\) is the index of any lift of the positive scalar coordinate \(z\).

*Proof.* The coordinate class generates \(K_1(C(S^1))=\mathbb Z\), with a matrix class sent to its determinant winding by Lesson 6, Theorem 5.2. The boundary homomorphism has target \(K_0(\mathcal K(H))=\mathbb Z\), normalized by rank, so it is multiplication by one unique integer \(k\). Lesson 7, Theorem 6.1, identifies that boundary with the Fredholm index of a lift, including our kernel-minus-cokernel sign. A lift of \(z\) exists by surjectivity and is Fredholm because its Calkin image is invertible. This proves its index is \(k\), independently of the lift. Applying the boundary to \([F]\) proves (6.1) for every matrix size. \(\square\)

For a partial-isometry lift \(W\), put \(D_+=1-W^*W\) and \(D_-=1-WW^*\). The same formula is

\[
\begin{gathered}
\operatorname{Tr}(D_+)-\operatorname{Tr}(D_-)\\
=k\,\operatorname{Wind}(q(W)).
\end{gathered}
\tag{6.2}
\]

Its defect projections are compact and therefore finite rank. The multiplier belongs on the index side of the map from winding to index. A circle quotient alone does not permit reversal of (6.1) using an integer multiplier.

**Example 6.2 (two shifts).** On \(H^2\oplus H^2\), put \(W=S\oplus S\) and
\(\mathcal E=C^*(1,W,\mathcal K(H^2\oplus H^2))\). The Calkin image of \(W\) is unitary and has full circle spectrum. Indeed, for \(|\lambda|=1\), the long Fourier blocks used in §2, placed in one summand and escaping every fixed finite-dimensional subspace, are approximate eigenvectors for \(W\). Every compact operator sends these unit vectors to zero in norm. If \(W-\lambda\) had a Calkin inverse, a bounded lift of that inverse would force these approximate eigenvectors to have norm tending to zero, a contradiction. Functional calculus for that unitary therefore identifies the quotient with \(C(S^1)\), sending \(q(W)\) to \(z\).

But \(W\) is an isometry with a two-dimensional cokernel. Thus \(k=-2\), while \(\operatorname{Wind}(q(W))=1\). An equality \(\operatorname{Wind}(q(W))=n\operatorname{Ind}(W)\) would require \(1=-2n\), impossible for integer \(n\). The analogous algebra generated by \(S\oplus S^*\) and the compact operators has \(k=0\) and still has full circle quotient; its coordinate symbol has winding one and index zero. Both quotient-spectrum arguments are the same approximate-eigenvector argument.

This also specifies the calibration needed in a topological form of Levinson's theorem. If an isometric wave operator lies in such an algebra and its cokernel is an \(N\)-dimensional bound-state space, then (6.1) gives \(-N=k\operatorname{Wind}(q(W))\). Identifying that wave operator, proving its membership and identifying its cokernel are separate analytic hypotheses. For a calibrated extension with \(k=-1\), the conclusion is \(\operatorname{Wind}(q(W))=N\).

[Richard, Theorem 10.3.3] motivates this abstract comparison but places an integer multiplier in the reverse direction without an extension-index hypothesis. Example 6.2 shows why that reversal cannot hold for every circle extension. The correctly directed formula (6.1) retains full generality.

## 7. Exercises with complete solutions

**Exercise 9.1 (basic).** Compute \(\ker T_{z^k}\) and \(\ker T_{z^k}^*\) for every integer \(k\).

*Solution.* For \(k>0\), \(T_{z^k}=S^k\) sends \(e_j\) to \(e_{j+k}\). Its kernel is zero, and its adjoint kills exactly \(e_0,\ldots,e_{k-1}\). For \(k=-r<0\), \(T_{z^k}=(S^*)^r\) kills exactly those first \(r\) vectors and maps every later vector to \(e_{j-r}\); its adjoint \(S^r\) is injective. For \(k=0\), both operators are the identity, so both kernels are zero. Thus

\[
\dim\ker T_{z^k}=\max(-k,0),\qquad
\dim\ker T_{z^k}^*=\max(k,0).
\]

Their difference is \(-k\), including at zero.

**Exercise 9.2 (basic).** Show that \(S^*S=1\) and \(1-SS^*\) has rank one. Determine the ideal generated by the latter projection inside \(\mathcal T\).

*Solution.* We have \(S^*e_0=0\) and \(S^*e_j=e_{j-1}\) for \(j\geq1\). Hence \(S^*Se_j=e_j\) for every \(j\), whereas \(SS^*\) is zero on \(e_0\) and the identity on its orthogonal complement. The defect is \(p_0\), rank one. Its generated ideal contains every \(S^jp_0(S^*)^k=E_{jk}\), so contains \(\mathcal K\). Conversely products of bounded operators with \(p_0\) are finite rank, and their norm limits are compact. Therefore the generated closed ideal is exactly \(\mathcal K\).

**Exercise 9.3 (intermediate).** Prove compactness of \(T_fT_g-T_{fg}\) for arbitrary continuous scalar symbols, explaining both the finite-rank case and the norm limit.

*Solution.* The difference is \(-PM_f(1-P)M_g|_{H^2}\). For \(g=z^q\), \((1-P)M_g\) is zero if \(q\geq0\), and maps into the \(-q\)-dimensional span of \(e_q,\ldots,e_{-1}\) if \(q<0\). Finite sums give finite rank for every trigonometric polynomial \(g_m\). Choose \(g_m\to g\) uniformly. The differences between these finite-rank operators and the required operator have norm at most \(\|f\|_\infty\|g_m-g\|_\infty\to0\). The compact operators are norm closed, proving the claim without any smoothness requirement.

**Exercise 9.4 (intermediate).** Prove Coburn's lemma for nonzero continuous \(f\), and explain precisely where scalar multiplication is used.

*Solution.* If both kernels were nonzero, choose \(a,b\neq0\) and express their negative-frequency products as in (5.2). Commutativity of the scalar boundary functions produces (5.3). The products are \(L^1\) by Cauchy–Schwarz. Their polynomial approximations show that the left and right sides have disjoint strictly positive and strictly negative Fourier supports. Fourier uniqueness makes their common value zero. The analytic product \(AD\) is zero; the identity theorem and \(A\neq0\) force \(D=0\). Equation (5.2) then says \(\overline f b=0\). The fully proved boundary-uniqueness Lemma 5.1 makes \(b\) nonzero almost everywhere, so \(f=0\) almost everywhere. A continuous function that vanishes almost everywhere vanishes everywhere, since a nonzero value would persist on an open arc of positive measure. This contradicts the hypothesis. The commutation used to form (5.3) has no corresponding implication for arbitrary matrix symbols; \(\operatorname{diag}(z,z^{-1})\) gives the explicit failure discussed above.

**Exercise 9.5 (advanced).** Compute \(K_*(\mathcal T_0)\) from the extension sequences and determine the map induced by \(\mathbb C\hookrightarrow\mathcal T\).

*Solution.* The connecting map in (2.5) takes the circle generator to minus the compact rank-one generator, so is an isomorphism \(\mathbb Z\to\mathbb Z\). Exactness first gives \(K_1(\mathcal T)=0\), and then gives injectivity of \(\sigma_*:K_0(\mathcal T)\to K_0(C(\mathbb T))\). The image contains \([1]\), so it is all of \(\mathbb Z[1]\). Thus scalar inclusion induces the isomorphism \(\mathbb Z\to K_0(\mathcal T)\) taking 1 to \([1]\), and the isomorphism between zero \(K_1\) groups. The separate character extension splits by this inclusion. Its exact split decomposition (4.4) identifies \(K_j(\mathcal T_0)\) with \(\ker\chi_*\). Since \(\chi_*\) is inverse to the already bijective inclusion, that kernel is zero for \(j=0,1\). No splitting of the Toeplitz symbol extension was used or exists.

## References and exact scope

- [E] Heath Emerson, *An Introduction to C*-Algebras and Noncommutative Geometry*, Birkhäuser, 2024, §§2.2 and 2.4–2.6. The continuous-symbol Fredholm statement in Corollary 2.5.2, p. 95, requires nonvanishing. Our proof includes continuous matrix symbols; §2.6's smooth trace formula is comparison material, not a prerequisite for (3.1).
- [B] Bruce Blackadar, *K-Theory for Operator Algebras*, second edition, Cambridge University Press, 1998, §9.4.2(a)–(e), for the Toeplitz algebra and evaluation kernel. The coefficient-algebra homotopy and Bott argument in §9.4.2(f)–(g) belong to the next lesson. [Author's corrected second edition](https://www.bruceblackadar.com/Mathematics/book6.pdf).
- [SS] Hermann Schulz-Baldes and Tom Stoiber, *Harmonic Analysis in Operator Algebras and its Applications to Index Theory and Topological Solid State Systems*, Springer, 2022, chapter *Duality for Toeplitz extensions*, §§*The smooth Toeplitz extension* and *Connecting maps of the smooth Toeplitz extension*. [Preprint](https://arxiv.org/abs/2206.07781). These treat general dynamical extensions and distinguish smooth, discrete and Wiener–Hopf maps. Their partial-isometry index is kernel minus cokernel, agreeing with (3.3). Their Connes–Thom, Takai and periodicity results are not used to prove the classical circle theorem here.

- **[Richard]** S. Richard, *K-theory for C*-algebras, and beyond*, Spring Semester 2015, §10.3, especially Proposition 10.3.1 and Theorem 10.3.3, printed pp. 106–108. [Freely available lecture notes](https://www.math.nagoya-u.ac.jp/~richard/teaching/s2015/Kth.pdf#page=106). The extension multiplier is corrected and calibrated explicitly in Proposition 6.1 and Example 6.2 above.
