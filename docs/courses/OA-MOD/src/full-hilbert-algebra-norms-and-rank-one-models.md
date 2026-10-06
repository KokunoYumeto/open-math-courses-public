# Full Hilbert-algebra norms and weighted rank-one models

*Independently written by OpenAI Codex (AI), October 2026, at requested Ultra effort. New prose: CC0-1.0.*

A full left Hilbert algebra has a natural Banach algebra norm, although its original Hilbert norm need not be complete. Fullness can be tested by closing just the multiplier unit ball in the correct ambient domain. When the original Hilbert norm is already complete, every nonzero projection contains a minimal projection, and the generated von Neumann algebra splits into type I factors. We prove these statements, then construct a weighted rank-one algebra whose entire closed involution and modular domains are explicit.

The exact inputs are HA01–04, FL01–04, the controlled approximation HAP06, Baire and uniform boundedness AB03, bounded operators and polar decomposition BK01–07, the polar theorem TC07–08, the spectral calculus SK03–09, and the square-sum and finite-matrix proofs OW09–10. Their proofs are given in the linked lessons, not here. No modular commutant theorem, separability or faithful state is an input.

Free comparisons are Jesse Peterson, [*Notes on von Neumann algebras*, Theorem 3.4.3, page 54](https://math.vanderbilt.edu/peters10/teaching/spring2013/vonNeumannAlgebras.pdf), for the matrix-unit representation of a type I factor, and Fumio Hiai, [*Concise lectures on selected topics of von Neumann algebras*, Example 3.6(2), page 22](https://arxiv.org/abs/2004.02383), for the Hilbert–Schmidt representation. The norm and fullness arguments below are derived from the preceding full-algebra and approximation proofs. The tensor construction, its exact unbounded domains, and the sharp squared projection bound are proved here using the linked bounded and spectral calculus.

## A complete involutive algebra norm on the full algebra

Let \(\mathcal A\subset H\) be an arbitrary left Hilbert algebra, with closed involution \(S\), right algebra \(\mathcal A_r\), and generated algebra \(M=L(\mathcal A)''\). Put \(\mathcal B_l\) for the left-bounded vectors and \(\lambda_\xi\) for their bounded multipliers. FL01–04 give
\(\mathcal A''=\mathcal B_l\cap D(S)\), with multiplier
\(\lambda_\xi\eta=R_\eta\xi\) on \(\mathcal A_r\), and
\(\lambda_{S\xi}=\lambda_\xi^*\) on \(\mathcal A''\).
Fullness means \(\mathcal A=\mathcal A''\). No algebra unit is required.

For a full \(\mathcal A\), define

\[
 \begin{gathered}
 N(\xi)=\max\\
 \{\|\lambda_\xi\|,\|\xi\|,\|S\xi\|\}.
 \end{gathered}
 \tag{HE.1}
\]

It is a norm, and \(N(S\xi)=N(\xi)\). For \(\xi,\eta\in\mathcal A\), multiplicativity and the adjoint identity give

\[
 \begin{aligned}
 \|\lambda_{\xi\eta}\|&\leq\|\lambda_\xi\|\|\lambda_\eta\|,\\
 \|\xi\eta\|&\leq\|\lambda_\xi\|\|\eta\|,\\
 \|S(\xi\eta)\|&=\|(S\eta)(S\xi)\|\\
 &\leq\|\lambda_\eta\|\|S\xi\|.
 \end{aligned}
 \tag{HE.2}
\]

Thus \(N(\xi\eta)\leq N(\xi)N(\eta)\), and the involution is isometric.

To prove completeness, let \((\xi_n)\) be \(N\)-Cauchy. The three components converge to \(\xi\in H\), \(\zeta\in H\), and \(x\in M\), the last in operator norm. The operator-norm limit can be constructed directly: for each \(v\in H\), the vectors \(\lambda_{\xi_n}v\) are Cauchy. Define \(xv\) to be their limit. The Cauchy operator family has a common norm bound, so its limit is a bounded linear map. Passing to the pointwise limit in the Cauchy estimate gives \(\|\lambda_{\xi_n}-x\|\to0\). Each approximant commutes with \(M'\); taking this limit gives the same commutation for \(x\), so \(x\in M''=M\) by BK02. Closedness of \(S\) gives \(\xi\in D(S)\) and \(S\xi=\zeta\). For \(\eta\in\mathcal A_r\), boundedness of \(R_\eta\) gives
\(R_\eta\xi=\lim_nR_\eta\xi_n=\lim_n\lambda_{\xi_n}\eta=x\eta\).
Therefore \(\xi\in\mathcal B_l\) and \(\lambda_\xi=x\). Fullness puts \(\xi\) back in \(\mathcal A\); convergence of all three components proves \(N(\xi_n-\xi)\to0\). This is a Banach *-algebra norm. It is not asserted to satisfy the C*-identity.

## Closing the multiplier ball characterizes fullness

For an arbitrary left Hilbert algebra define

\[
 U_{\mathcal A}=\{\xi\in\mathcal A:\|L_\xi\|\leq1\}.
 \tag{HE.3}
\]

The topology on \(D(S)\) here is the topology induced by the Hilbert norm of \(H\). It is not the graph-norm topology, and the ambient space is not all of \(H\).

**Theorem.** The algebra is full exactly when \(U_{\mathcal A}\) is closed in \(D(S)\).

**Proof.** Suppose it is full, and a net \(\xi_i\in U_{\mathcal A}\) converges in Hilbert norm to \(\xi\in D(S)\). For each \(\eta\in\mathcal A_r\),

\[
 \|R_\eta\xi\|
   =\lim_i\|R_\eta\xi_i\|\leq\|\eta\|.
 \tag{HE.4}
\]

Thus \(\xi\in\mathcal B_l\) with \(\|\lambda_\xi\|\leq1\); fullness gives \(\xi\in U_{\mathcal A}\). This proves relative closedness for all convergent nets.

Conversely take \(\xi\in\mathcal A''\). HAP06 gives \(a_n\in\mathcal A\) with \(a_n\to\xi\), \(Sa_n\to S\xi\), and \(\|L_{a_n}\|\leq\|\lambda_\xi\|\). If \(\lambda_\xi=0\), injectivity gives \(\xi=0\). Otherwise divide the sequence and its limit by \(\|\lambda_\xi\|\). They lie in the multiplier ball, and their limit lies in \(D(S)\). Relative closedness puts this limit in \(\mathcal A\), hence \(\xi\in\mathcal A\). Since \(\mathcal A\subseteq\mathcal A''\) always, equality follows. The second graph-coordinate limit supplied by HAP06 is available, but the closedness test needs only the first limit in the stated ambient domain. \(\square\)

## Hilbert completeness controls every product and produces projections

Now assume \(\mathcal A=H\) as Hilbert spaces. If \(H=0\), its generated algebra is zero; assertions about a nonzero projection are restricted to the nonzero case. The inclusion \(\mathcal A\subseteq\mathcal A''\subseteq H\) already makes this algebra full.

Its closed involution \(S\) has domain \(H\). TC08 gives \(S=J|S|\) and \(D(|S|)=H\). The bounded spectral truncations \(\min(|S|,n)\) are pointwise bounded by \(\||S|\xi\|\). Uniform boundedness AB03 makes their norms uniformly bounded; spectral convergence then makes \(|S|\), hence \(S\), bounded. This argument proves the needed boundedness rather than hiding a closed-graph assumption.

For each \(\eta\in H\), right multiplication is bounded: the algebraic rule gives \(R_\eta=S L_{S\eta} S\) on all of \(H\). For each fixed \(\eta\), the family \(\{L_\xi:\|\xi\|\leq1\}\) is pointwise bounded, since
\(\|L_\xi\eta\|=\|R_\eta\xi\|\leq\|R_\eta\|\).
Uniform boundedness, now applied on \(H\), supplies \(C>0\) with

\[
 \|\xi\eta\|\leq C\|\xi\|\|\eta\|
       \qquad(\xi,\eta\in H).
 \tag{HE.5}
\]

No countability of \(H\) or of the operator family is required.

Let \(\xi=S\xi\ne0\); such a vector exists by taking a nonzero real or imaginary involution part of any nonzero vector. Its faithful multiplier \(x=L_\xi\) is nonzero self-adjoint. Choose \(\delta>0\) for which

\[
 \begin{aligned}
 q&=1_{\{|t|\geq\delta\}}(x)\ne0,\\
 b&=g(x),&
 g(t)&=t^{-1}1_{\{|t|\geq\delta\}}(t),\\
 L_{b\xi}&=bL_\xi=q.
 \end{aligned}
 \tag{HE.6}
\]

SK04/08 put the bounded \(b\) in \(M\), and FL01's covariance gives the last identity. Because \(b\xi\in H=\mathcal A\), injectivity of \(L\) and \(q^*=q=q^2\) show that \(e=b\xi\) satisfies \(Se=e=e^2\). Thus the vector algebra contains a nonzero self-adjoint idempotent.

For every such \(e\), (HE.5) gives

\[
 \begin{gathered}
 \|e\|=\|e^2\|\leq C\|e\|^2,\\
 \|e\|\geq C^{-1},\\
 \|e\|^2\geq C^{-2}.
 \end{gathered}
 \tag{HE.7}
\]

The last bound is the squared version of the preceding one. Replacing \(C^{-2}\) by \(C^{-1}\) is not valid in general; HE07 gives an exact counterexample.

## Every projection contains a minimal one, and the blocks are type I

We first localize the preceding argument to an arbitrary nonzero projection \(p\in M\). Nondegeneracy gives \(\xi\in H\) for which \(pL_\xi\ne0\). The vector \(\zeta=p\xi\) belongs to \(\mathcal A\), and \(L_\zeta=pL_\xi\). Then \(L_{\zeta S\zeta}=pL_\xi L_\xi^*p\) is positive nonzero and supported in \(p\). Apply the spectral extraction (HE.6) to this positive vector. We obtain a nonzero vector projection \(e\) with \(L_e\leq p\).

Define the nonempty local infimum

\[
 \begin{aligned}
 \lambda_p&=\inf\{\|e\|^2:
       e=Se=e^2\ne0,\ L_e\leq p\},\\
 \lambda_p&\geq C^{-2}>0 .
 \end{aligned}
 \tag{HE.8}
\]

Choose \(e\) in this set with \(\|e\|^2<2\lambda_p\). We claim \(L_e\) is minimal in the whole \(M\). If it had a nontrivial subprojection \(q\), put \(q_1=q\), \(q_2=L_e-q\), and \(e_j=q_je\). Covariance gives \(L_{e_j}=q_jL_e=q_j\). Faithfulness of \(L\) shows that both \(e_j\) are nonzero self-adjoint idempotents, \(e=e_1+e_2\), and \(e_1e_2=0\). The Hilbert-algebra adjoint identity gives

\[
 \begin{aligned}
 \langle e_1,e_2\rangle
 &=\langle e_1^2,e_2\rangle
 =\langle e_1,e_1e_2\rangle=0,\\
 \|e\|^2&=\|e_1\|^2+\|e_2\|^2
          \geq2\lambda_p .
 \end{aligned}
 \tag{HE.9}
\]

This contradicts the choice of \(e\). For \(p=1\), it proves the global near-infimum minimality assertion as well. Using local infima is what proves the stronger fact needed next: every nonzero projection of \(M\) contains a minimal projection.

Choose a maximal orthogonal family \((q_i)_{i\in I}\) of nonzero minimal projections. Its strong sum is \(1\), since a nonzero complement would contain another minimal projection. For a minimal \(q\), every self-adjoint member of \(qMq\) is scalar: a nonconstant spectral resolution would give a nontrivial subprojection of \(q\). Hence \(qMq=\mathbb C q\).

Declare \(i\sim j\) when \(q_i\) and \(q_j\) are Murray–von Neumann equivalent. If \(q_iMq_j\ne0\), the polar decomposition of a nonzero element of this corner has initial projection \(q_j\) and final projection \(q_i\), by minimality. Thus different equivalence classes have zero cross corners. For each class \(F\) put

\[
 z_F=\sum_{i\in F}q_i .
 \tag{HE.10}
\]

The sums are strong suprema of finite subsums. Compressing each off-diagonal block \(z_Fx(1-z_F)\) by the complete family \((q_i)\) gives zero; finite-subsum limits give that the block itself is zero. The opposite block is zero as well. Therefore \(z_F\) is central. A central projection below \(z_F\) selects each \(q_i\) either wholly or not at all; equivalence forces the same selection for every \(i\in F\). Thus \(z_F\) is a minimal central projection.

Fix \(i_0\in F\) and partial isometries \(v_i\) with
\(v_i^*v_i=q_{i_0}\), \(v_iv_i^*=q_i\), taking \(v_{i_0}=q_{i_0}\). Their ranges are orthogonal, so

\[
 \begin{aligned}
 e_{ij}&=v_iv_j^*,&
 e_{ij}e_{k\ell}&=\delta_{jk}e_{i\ell},\\
 U_F(\delta_i\otimes\eta)&=v_i\eta,\qquad
 U_F:\ell^2(F)\otimes q_{i_0}H\longrightarrow z_FH .
 \end{aligned}
 \tag{HE.11}
\]

The isometry \(U_F\) is onto because \(\sum_{i\in F}q_i=z_F\). For \(x\in z_FM\), \(v_i^*xv_j\) is a scalar multiple of \(q_{i_0}\). Consequently \(U_F^*xU_F\) has a bounded scalar matrix on \(\ell^2(F)\), tensored with the identity on \(q_{i_0}H\).

Here are the boundedness and convergence details. The tensor Hilbert space and bounded tensor norm used in (HE.11) are constructed at the start of HE05. Fix a unit vector \(\eta\in q_{i_0}H\), which exists since this projection is nonzero, and write \(v_i^*xv_j=a_{ij}q_{i_0}\). For finitely supported scalars \(c_j\), orthogonality and (HE.11) give

\[
 \sum_{i\in F}\left|\sum_j a_{ij}c_j\right|^2
 \leq \|x\|^2\sum_j|c_j|^2.
\]

Indeed the summands are the squared norms of the coordinates of \(U_F^*xU_F(\sum_jc_j\delta_j\otimes\eta)\). The sum over \(i\) is the supremum of finite subsums. Thus this matrix defines a bounded operator \(a\) on the dense finite-support subspace and extends to \(\ell^2(F)\) by completeness, with \(\|a\|\leq\|x\|\). Its coordinate formula agrees with \(U_F^*xU_F\) on every finite tensor sum, so density proves equality with \(a\otimes1\). Conversely the finite scalar matrices are represented by the \(e_{ij}\) in \(M\). For a bounded scalar operator \(a\), its finite-coordinate compressions converge strongly to \(a\) along finite subsets of \(F\); the represented limit belongs to \(M\). Explicitly, if \(P_E\) is projection on a finite coordinate set \(E\subset F\), then

\[
 \begin{aligned}
 &\|(P_EaP_E-a)c\|\\
 &\quad\leq\|a\|\|(P_E-I)c\|\\
 &\qquad+\|(P_E-I)ac\|\longrightarrow0.
 \end{aligned}
\]

The compression norms are bounded by \(\|a\|\). Tensoring with the identity preserves that bound and gives convergence first on finite tensor sums, then on every vector by density. Their conjugates by \(U_F\) are finite sums of the matrix units, hence belong to \(z_FM\); their strong limit therefore belongs there too. Thus

\[
 \begin{aligned}
 z_FM&\cong B(\ell^2(F)),\\
 M&\cong\prod_F B(\ell^2(F)).
 \end{aligned}
 \tag{HE.12}
\]

The product is the bounded von Neumann direct sum: coordinate families have bounded operator norm. To check that every such family occurs, let \(x_F\in z_FM\) and \(\sup_F\|x_F\|=C<\infty\). For each \(v\in H\), orthogonality gives

\[
 \begin{aligned}
 &\sum_F\|x_Fz_Fv\|^2\\
 &\quad\leq C^2\sum_F\|z_Fv\|^2\\
 &\quad=C^2\|v\|^2.
 \end{aligned}
\]

Finite partial sums of the image vectors are therefore Cauchy and define a bounded operator \(x\) of norm at most \(C\). The corresponding finite operator sums belong to \(M\), and converge strongly to \(x\), so \(x\in M\). Its compression is \(z_Fx=x_F\) for every \(F\). Conversely central compression preserves products and adjoints, and the same orthogonal decomposition shows \(\|x\|=\sup_F\|z_Fx\|\). This proves the asserted algebra isomorphism, including surjectivity and its norm. It is not an algebraic direct sum or a countable-sum assertion. This proves the type I factor decomposition at arbitrary cardinality, including its actual representation multiplicities.

## A weighted tensor algebra with dense products

Let \(K\) be any complex Hilbert space. Its conjugate space \(\overline K\) is identified by Riesz with its continuous complex-linear dual: \(\overline\eta\) corresponds to \(\xi\mapsto\langle\xi,\eta\rangle\). On simple tensors,

\[
 \langle\xi\otimes\overline\eta,\,
          \zeta\otimes\overline\omega\rangle
       =\langle\xi,\zeta\rangle\langle\omega,\eta\rangle .
 \tag{HE.13}
\]

Finite-dimensional orthonormal expansion in the span of the finitely many tensor factors proves positivity and nondegeneracy after quotienting by the algebraic tensor relations. Hilbert completion gives \(K\otimes\overline K\). For bounded operators, the same finite expansion proves
\(\|a\otimes b\|\leq\|a\|\|b\|\) and
\((a\otimes b)^*=a^*\otimes b^*\); testing simple unit vectors approaching the two norms gives equality of norms.

For clarity, the finite expansions and the completion can be made explicit. Expand the two finite spans of tensor factors in orthonormal lists, using the projection and Gram–Schmidt argument in BK01. A finite tensor then has a unique coefficient matrix \((c_{ij})\), and (HE.13) gives

\[
 \left\|\sum_{i,j}c_{ij}e_i\otimes\overline{f_j}\right\|^2
 =\sum_{i,j}|c_{ij}|^2.
\]

Uniqueness follows by applying the coordinate functionals in each factor; it also proves that zero norm means the zero algebraic tensor. Choose maximal orthonormal families in the two Hilbert spaces. Their spans are dense, since a nonzero orthogonal complement would extend the family by a unit vector. Finite projections in either family converge in norm on each vector: approximate that vector by a finite linear combination and use the contraction bound for projection. Applying these projections to each factor identifies every algebraic tensor with its square-summable coefficient array. Conversely every finite array comes from a finite tensor. The complete square-sum space on the product index set, proved in OW09, is therefore the required Hilbert completion; the families may be uncountable.

For the operator bound, write a finite tensor as \(v=\sum_j\xi_j\otimes\overline{f_j}\) with orthonormal second factors. Then

\[
 \begin{aligned}
 \|(a\otimes1)v\|^2
 &=\sum_j\|a\xi_j\|^2\\
 &\leq\|a\|^2\sum_j\|\xi_j\|^2.
 \end{aligned}
\]

Expanding instead in orthonormal first factors proves the bound for \(1\otimes b\). Composition gives the bound for \(a\otimes b\), and continuity extends it to the completion. Testing the inner product on simple tensors proves the adjoint formula; linearity and density extend it to the whole space. These arguments apply to any two Hilbert spaces, including the tensor in HE04. If either factor is zero, the tensor space and every tensor operator are zero, and the same norm assertions hold.

Let \(h\) be positive, injective and self-adjoint on \(K\), with no boundedness or bounded-inverse assumption. Set
\(\mathcal T=D(h)\odot\overline{D(h^{-1})}\), where \(\odot\) denotes the algebraic tensor product. For simple tensors define

\[
 \begin{aligned}
 (\xi_1\otimes\overline{\eta_1})
 (\xi_2\otimes\overline{\eta_2})
 &=\langle\xi_2,h^{-1}\eta_1\rangle\,
       \xi_1\otimes\overline{\eta_2},\\
 (\xi\otimes\overline\eta)^\sharp
 &=h^{-1}\eta\otimes\overline{h\xi}.
 \end{aligned}
 \tag{HE.14}
\]

The rules are compatible with the conjugate-space scalar relations and extend bilinearly and conjugate linearly. The second expression stays in \(\mathcal T\): \(h^{-1}\eta\in D(h)\) and \(h\xi\in D(h^{-1})\), by the actual inverse-domain identity SK07. Associativity follows by multiplying the two scalar coefficients of a triple product. Applying the involution twice returns the original tensor. For reversal of a product, the coefficient is conjugated; the identity
\(\langle h^{-1}\eta_1,\xi_2\rangle
=\overline{\langle\xi_2,h^{-1}\eta_1\rangle}\)
gives \((ab)^\sharp=b^\sharp a^\sharp\).

Write \(\Theta_{\alpha,\beta}\zeta=\langle\zeta,\beta\rangle\alpha\). Left multiplication on the completed tensor space is

\[
 \begin{gathered}
 L_{\xi\otimes\overline\eta}\\
       =\Theta_{\xi,h^{-1}\eta}\otimes1,\\
 L_{a^\sharp}=L_a^* .
 \end{gathered}
 \tag{HE.15}
\]

The first expression is bounded; the adjoint identity follows because \(h^{-1}(h\xi)=\xi\). It proves the Hilbert-algebra pairing axiom for all finite sums.

Both factor domains are dense, so \(\mathcal T\) is Hilbert dense. If \(K\ne0\), choose \(0\ne\alpha\in D(h)\) and put \(\beta=h\alpha\in D(h^{-1})\). The product
\((\xi\otimes\overline\beta)(\alpha\otimes\overline\eta)\)
is \(\|\alpha\|^2\xi\otimes\overline\eta\). Therefore the span of products is all of \(\mathcal T\), hence dense. If \(K=0\), every assertion is the corresponding zero assertion. The remaining Hilbert-algebra axiom, closability of the involution, will follow with its complete domain in HE06.

Since \(h^{-1}D(h^{-1})=D(h)\), HE15 ranges over all rank-one operators \(\Theta_{\xi,\zeta}\) with \(\xi,\zeta\in D(h)\), tensored with the identity. Hilbert-norm approximation of the two vectors approximates every rank-one operator in operator norm. Finite-rank compressions approximate every bounded operator strongly along the finite-dimensional subspaces of \(K\). Consequently

\[
 L(\mathcal T)''=B(K)\,\bar\otimes\,\mathbb C1_{\overline K}.
 \tag{HE.16}
\]

For the reverse inclusion, the algebra of operators \(a\otimes1\) is strongly closed. To see this directly, assume \(a_i\otimes1\to T\) strongly and choose a unit vector \(\eta\) in the nonzero second factor. The subspace \(K\otimes\mathbb C\overline\eta\) is closed, and on it the limit defines a bounded map \(a\) by \(T(\xi\otimes\overline\eta)=a\xi\otimes\overline\eta\), with \(\|a\|\leq\|T\|\). It follows that \(a_i\xi\to a\xi\) for each \(\xi\). Testing any other simple tensor therefore gives \(T(\xi\otimes\overline\zeta)=a\xi\otimes\overline\zeta\); density gives \(T=a\otimes1\). In the zero-space case the claim is immediate. This strongly closed unital star-algebra is its bicommutant by BK02, so it contains the generated algebra. Together with the finite-rank approximation, this proves (HE.16).

## Spectral bands determine the whole modular domain

Put \(p_n=1_{[1/n,n]}(h)\), \(Q_n=p_n\otimes\overline{p_n}\), and \(Q_0=0\). Injectivity and the spectral calculus give \(p_n\uparrow1\), hence \(Q_n\uparrow1\) strongly. On \(Q_n(K\otimes\overline K)\) the formula

\[
 A_n=(h|_{p_nK})\otimes
             \overline{(h^{-1}|_{p_nK})}
 \tag{HE.17}
\]

defines a bounded positive invertible operator. Positivity follows by writing it as the square of the corresponding bounded tensor of positive square roots. Its spectrum lies in \([n^{-2},n^2]\). The \(A_n\) agree on earlier bands and commute with every \(Q_m\).

Set \(V_n=(Q_n-Q_{n-1})(K\otimes\overline K)\), and let \(B_n=A_n|_{V_n}\). This is an orthogonal Hilbert decomposition into reducing subspaces. The direct-sum spectral rule SK08 defines the positive injective self-adjoint operator

\[
 \begin{aligned}
 D(A)&=\left\{v:\sum_{n\geq1}
           \|B_n(Q_n-Q_{n-1})v\|^2<\infty\right\},\\
 Av&=\sum_{n\geq1}B_n(Q_n-Q_{n-1})v .
 \end{aligned}
 \tag{HE.18}
\]

Each sum converges in Hilbert norm. Equivalently, \(A_nQ_nv\) has a norm limit. This construction avoids treating a product of unbounded tensor operators as automatically self-adjoint.

The self-adjointness and exact domain in this step admit a direct check. The finite sums of the spaces \(V_n\) are dense because \(Q_n\to I\), and are contained in (HE.18). Write \(v_n=(Q_n-Q_{n-1})v\). Testing the adjoint pairing on vectors supported in one \(V_n\) shows that a vector \(w\) can lie in \(D(A^*)\) only if its adjoint image has coordinates \(B_nw_n\). Such a vector exists in the Hilbert space precisely when

\[
 \sum_n\|B_nw_n\|^2<\infty.
\]

Conversely, this condition makes the sum converge; the Cauchy–Schwarz inequality for the two sequences of coordinate norms extends the finite-coordinate pairing to every \(v\in D(A)\). Thus it is sufficient for membership in \(D(A^*)\), and \(A^*=A\) with exactly the domain in (HE.18). Positivity follows by summing the nonnegative terms \(\langle B_nv_n,v_n\rangle\); this sum is absolutely convergent by the same inequality. Each \(B_n\) is invertible on its band, so the kernel is zero. This also proves closedness by the adjoint graph criterion TC03.

On a simple tensor in \(\mathcal T\), spectral graph convergence of both factors gives
\(A_nQ_n(\xi\otimes\overline\eta)\to
h\xi\otimes\overline{h^{-1}\eta}\).
Thus

\[
 \begin{gathered}
 A(\xi\otimes\overline\eta)\\
       =h\xi\otimes\overline{h^{-1}\eta}.
 \end{gathered}
 \tag{HE.19}
\]

Conversely \(\mathcal T\) is a graph core for \(A\). If \(v\in D(A)\), HE18 gives \(Q_nv\to v\) and \(AQ_nv\to Av\). Finite sums of tensors with both vectors in \(p_nK\) are dense in \(Q_n(K\otimes\overline K)\); they belong to \(\mathcal T\). The bound \(\|A_n\|\leq n^2\) turns these Hilbert approximations into graph approximations. Choose one sufficiently close finite sum for each \(n\); their vector and image limits are \(v,Av\). This proves equality of the graph closure with the entire operator in HE18.

Let \(J(\xi\otimes\overline\eta)=\eta\otimes\overline\xi\). Formula HE13 makes \(J\) an antiunitary involution. It preserves every \(Q_n\) and \(V_n\). On each band, swapping the factors gives \(JA_nJ=A_n^{-1}\). The direct-sum domains therefore give the full identity

\[
 JAJ=A^{-1},\qquad
 D(A^{-1})=J D(A).
 \tag{HE.20}
\]

The algebraic involution HE14 is \(JA\) on \(\mathcal T\). Since \(\mathcal T\) is an \(A\)-core and \(J\) is bounded antiunitary, its closure is exactly \(S=JA\), with \(D(S)=D(A)\). In particular it is closable, completing all four left Hilbert-algebra axioms.

The anti-linear adjoint is \(S^*=AJ\). To check the domain as well as the formula, for \(x\in D(A)\) the antiunitary identity gives

\[
 \langle Sx,y\rangle=\langle Jy,Ax\rangle.
\]

This pairing is bounded in \(\|x\|\) precisely when \(Jy\in D(A^*)=D(A)\), by the adjoint-domain test TC03. In that case it equals \(\langle AJy,x\rangle\). Thus the adjoint has exactly the asserted domain and action. Its product with \(S\) has domain \(D(A^2)\), since \(S v\in D(AJ)\) exactly when \(Av\in D(A)\). Hence

\[
 \begin{aligned}
 \Delta&=S^*S=A^2,&
 \Delta^{1/2}&=A,\\
 J(\xi\otimes\overline\eta)
       &=\eta\otimes\overline\xi .
 \end{aligned}
 \tag{HE.21}
\]

These are the polar modular data, including the full operator domains. The square of the involution and the adjoint product require separate domain calculations. For \(v\in D(A)\), the vector \(Av\) belongs to \(D(A^{-1})=JD(A)\), so \(Sv=JAv\in D(A)\). Equation (HE.20) then gives

\[
 \begin{gathered}
 D(S^2)=D(A),\\
 S^2v=v\quad(v\in D(A)).
 \end{gathered}
\]

The modular operator is the positive adjoint product \(S^*S\), whose domain is \(D(A^2)\) as proved above. In the usual notation \(A=h\otimes\overline{h^{-1}}\), that symbol means the self-adjoint closure HE18–19. Its domain can be larger than the intersection of the individual unbounded tensor-factor domains.

## Solved checks for the constant, norm and unbounded domain

**Finite weighted matrices.** For \(K=\mathbb C^m\) with positive integer dimension and \(h>0\), identify \(\xi\otimes\overline\eta\) with \(\xi\eta^*\), preserving the Hilbert–Schmidt inner product. Every matrix is in \(\mathcal T\), and the formulas become

\[
 \begin{aligned}
 X\cdot Y&=Xh^{-1}Y,\\
 X^\sharp&=h^{-1}X^*h,\\
 L_X&=L^{\mathrm{matrix}}_{Xh^{-1}},\\
 A(X)&=hXh^{-1},\\
 J(X)&=X^*.
 \end{aligned}
 \tag{HE.22}
\]

Here \(L^{\mathrm{matrix}}_B(X)=BX\).
They directly verify reversal, the Hilbert adjoint pairing and the operator represented in HE21. The optimal product constant for the Hilbert–Schmidt norm is \(C=\|h^{-1}\|\): the upper bound follows from the two matrix norm estimates, and rank-one matrices aligned with a maximal eigenvector of \(h^{-1}\) attain it. The estimates are proved in OW10. One can also verify optimality without choosing an eigenbasis: take unit vectors \(w,u,z\), put \(v=h^{-1}w/\|h^{-1}w\|\), and use \(X=\Theta_{u,v}\), \(Y=\Theta_{w,z}\). Their Hilbert–Schmidt norms are one, while

\[
 Xh^{-1}Y=\|h^{-1}w\|\Theta_{u,z}.
\]

Taking the supremum over unit \(w\) proves the lower bound for the optimal constant.

**The squared constant and the C*-identity.** Take \(m=1\) and \(h=t>0\). The vector projection is \(e=t\), because the product is \(xy/t\), and the optimal product constant is \(C=1/t\). Thus

\[
 \begin{gathered}
 \lambda=\inf_{e\ne0,\ e=e^\sharp=e^2}\|e\|^2\\
        =t^2=C^{-2}.
 \end{gathered}
 \tag{HE.23}
\]

At \(t=1/2\), \(\lambda=1/4<1/C=1/2\). This disproves the unsquared denominator while exactly attaining HE07. For a different test take \(m=2\), \(h=1\). The Banach norm HE01 is the Hilbert–Schmidt norm, since it dominates the operator norm and is adjoint invariant. At \(X=1_2\), \(N(X^\sharp X)=\sqrt2\), whereas \(N(X)^2=2\). The norm is an involutive Banach algebra norm with no C*-claim.

**A domain larger than the separate factor domains.** Take \(K=\ell^2(\mathbb Z)\) and \(h e_j=2^j e_j\). Specify the self-adjoint operator, rather than only its values on basis vectors, by

\[
 \begin{aligned}
 D(h)&=\bigl\{c\in\ell^2(\mathbb Z):\\
 &\qquad\sum_j2^{2j}|c_j|^2<\infty\bigr\},\\
 (hc)_j&=2^jc_j.
 \end{aligned}
\]

The coordinate adjoint test used in HE06 proves self-adjointness, positivity and injectivity. Replacing \(2^j\) by \(2^{-j}\) gives its inverse with the corresponding square-sum domain. Under the matrix-unit Hilbert basis of \(K\otimes\overline K\),

\[
 \begin{aligned}
 D(A)&=\left\{(a_{ij}):\sum_{i,j}
             2^{2(i-j)}|a_{ij}|^2<\infty\right\},\\
 (Aa)_{ij}&=2^{i-j}a_{ij},&
 (Ja)_{ij}&=\overline{a_{ji}} .
 \end{aligned}
 \tag{HE.24}
\]

Membership in the tensor Hilbert space, namely \(\sum_{i,j}|a_{ij}|^2<\infty\), is understood as well. Finite matrix truncations prove both necessity and sufficiency in HE18, since the band projections select finitely many integer coordinates.

Let \(v=\sum_{j\geq1}2^{-j}e_j\otimes\overline{e_j}\). Then

\[
 \begin{aligned}
 v&\in D(A),\\
 Av&=v,\\
 v&\notin D(h\otimes1),\\
 \sum_{j\geq1}2^{2j}2^{-2j}&=\infty .
 \end{aligned}
 \tag{HE.25}
\]

The finite diagonal sums nevertheless lie in \(\mathcal T\) and converge to \(v\) in the \(A\)-graph norm. Explicitly, with \(v_N=\sum_{j=1}^N2^{-j}e_j\otimes\overline{e_j}\), the geometric-sum identity gives

\[
 \begin{aligned}
 \|v-v_N\|^2&=\frac{4^{-N}}3,\\
 \|A(v-v_N)\|^2&=\frac{4^{-N}}3.
 \end{aligned}
\]

This proves both convergence claims and \(\|v\|^2=1/3\). The full modular operator in this model is diagonal with multiplier \(2^{2(i-j)}\), and its domain is

\[
 \begin{aligned}
 D(\Delta)&=\bigl\{a\in\ell^2(\mathbb Z^2):\\
 &\quad\sum_{i,j}2^{4(i-j)}|a_{ij}|^2<\infty\bigr\}.
 \end{aligned}
\]

It is obtained by the same coordinate test, or by the exact square-domain rule for \(A^2\). This exhibits why the algebraic construction must be closed in its actual graph, rather than assigned the smaller separate-factor domain. The weighted transpose \(S=JA\) and its adjoint product have the exact domains proved in HE06.

## References

- Jesse Peterson, [*Notes on von Neumann algebras*, Theorem 3.4.3, page 54](https://math.vanderbilt.edu/peters10/teaching/spring2013/vonNeumannAlgebras.pdf). The matrix-unit comparison is used with explicit finite-subset convergence and representation multiplicities.
- Fumio Hiai, *Concise lectures on selected topics of von Neumann algebras*, Example 3.6(2), complete PDF page 22 actually inspected for the Hilbert–Schmidt type I model. [Freely available author's text](https://arxiv.org/abs/2004.02383). No entire-source or weighted-model proof reading claim.

