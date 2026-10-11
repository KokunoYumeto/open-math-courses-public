# Powers models and uniqueness in type III₁

Every approximately finite-dimensional factor of type III₁ with separable predual is isomorphic to one fixed product of two Powers factors. The proof joins the previously established modular, absorption, and action-classification results. We retain the normal isomorphisms and the continuous cocycles throughout the comparison.

Write \(R\) for the hyperfinite finite factor, and \(R_{\mathrm{sf}}=R\overline\otimes B(\ell^2)\) for its semifinite amplification. For \(0<\lambda<1\), use the specific Powers product

\[
 (R_\lambda,\omega_\lambda)
 =\bigotimes_{n=1}^{\infty}
   \left(M_2,\operatorname{Tr}(h_\lambda\,\cdot)\right),
 \qquad
 h_\lambda=\frac1{1+\lambda}
             \begin{pmatrix}\lambda&0\\0&1\end{pmatrix}.
 \tag{1}
\]

All tensor products are von Neumann tensor products. An isomorphism below is normal with normal inverse. The dual circle convention is negative: the implementing integer unitary \(U\) transforms as \(U\mapsto\overline zU\).

## 1. The conclusions and the proof route

**Uniqueness theorem.** If \(M\) is an approximately finite-dimensional factor of type III₁ with separable predual, then

\[
 M\cong\mathcal P,\qquad
 \mathcal P=R_{1/2}\overline\otimes R_{1/3}.
 \tag{2}
\]

More generally any \(R_\lambda\overline\otimes R_\mu\) with
\(0<\lambda,\mu<1\) and irrational \(\log\lambda/\log\mu\) is such a reference factor.

We prove two intermediate conclusions in their own right. Every injective factor \(A\) of type \(\mathrm{III}_\lambda\) with separable predual is isomorphic to the particular product (1). Every \(M\) in the uniqueness theorem satisfies, for every \(0<\lambda<1\),

\[
 M\cong M\overline\otimes R_\lambda,\qquad
 M\cong M\overline\otimes R,\qquad
 M\cong M\overline\otimes\mathcal P.
 \tag{3}
\]

The final conclusion (2) needs an additional action comparison; it does not follow just by removing \(M\) from the last tensor equation.

Here are the main earlier programme results, used with their proofs.

- Aperiodic comparison, AC01–07 compares approximately inner automorphisms of asymptotic period zero on strongly stable factors with separable predual and transports their entire integer crossings.
- Type III crossings, TIC02–09 supplies the hyperfinite semifinite discrete core, its strong stability, and the full integer and circle classifications.
- Modular approximate innerness, MI01–06 proves approximate innerness of every fixed modular time on an AFD type III₁ factor with separable predual.
- Discrete modular crossings, MD01–05 proves their precise type \(\mathrm{III}_{e^{-2\pi/T}}\).
- Absorption descent, DAS01–07 transfers absorption of the specified Powers product back through a crossing by an approximately inner automorphism.
- Tracial absorption, CTA04–07 and central dual absorption, CDS01–07 supply the tracial and equivariant consequences.
- Opposite dual circles, ODT01–07 proves the opposite-circle crossing theorem and the irrational Powers tensor-product assertion.

Separability is retained in the classification, approximate-innerness and absorption inputs. We do not infer those conclusions for arbitrary predual size.

## 2. The specified Powers product

The product representation in (1) is the pointed tensor product of the Hilbert–Schmidt spaces, with reference vector \(h_\lambda^{1/2}\) in each leg. Local left and right matrix multiplications applied to the product vector are both dense. Therefore the vector is cyclic and separating, and its state is faithful and normal. Local matrix algebras form an increasing sequence generating \(R_\lambda\).

The completed product identification and subtype are the precise input proved in Weighted tensor splitting, TS06, using Constant CAR states and the periodic core, Sections 1–3 and 6. With \(p=1/(1+\lambda)\), that lesson's density \(\operatorname{diag}(1-p,p)\) is exactly \(h_\lambda\). The completed modular graph gives

\[
 \sigma_t^{\omega_\lambda}(e_{12}^{(n)})
       =\lambda^{it}e_{12}^{(n)},\qquad
 \operatorname{Per}(\omega_\lambda)
       =\frac{2\pi}{|\log\lambda|}\mathbb Z.
 \tag{4}
\]

Its type proof compares with every faithful normal semifinite weight and obtains

\[
 S(R_\lambda)=\{0\}\cup\lambda^{\mathbb Z}.
 \tag{5}
\]

Thus (5) is not being inferred from the period of one state. The factor is AFD, has separable predual, and is injective by the increasing-algebra proof in Averaging crossed products and injectivity, Proposition 5.1 and Corollary 5.2.

The concrete product also satisfies

\[
 (R_\lambda,\omega_\lambda)\overline\otimes
 (R_\lambda,\omega_\lambda)
       \cong (R_\lambda,\omega_\lambda).
 \tag{6}
\]

Indeed interleave the two copies' coordinates into the odd and even coordinates of one copy. On elementary pointed tensors this preserves every inner product, has dense range, and therefore extends to an onto Hilbert unitary. It sends the two local left algebras to the odd and even local left algebras. Taking their generated von Neumann algebras proves the normal isomorphism and its inverse, with the product vector preserved. The same argument gives \(R\overline\otimes R\cong R\).

## 3. Comparing trace-scaling generators

We need the following precise semifinite statement:

\[
 \tau\theta_1=\lambda\tau,\quad
 \tau\theta_2=\lambda\tau,\quad 0<\lambda\ne1
 \quad\Longrightarrow\quad
 \theta_2=\Phi\theta_1\Phi^{-1}
 \text{ on }R_{\mathrm{sf}}.
 \tag{7}
\]

The outer-conjugacy construction is Trace scaling on the hyperfinite semifinite factor, Theorem 6.1, equations (6.5)–(6.8). We spell out its mechanism and use the full DDP coboundary proof for the last step.

That lesson proves \(\operatorname{Ct}(R_{\mathrm{sf}})=\operatorname{Inn}(R_{\mathrm{sf}})\), in Theorem 4.2, and trace-preserving approximate innerness, in Proposition 5.1. Since an inner automorphism preserves \(\tau\), every nonzero power of either \(\theta_i\) is outer and is not centrally trivial. For

\[
 B_{ij}=\theta_i\otimes\theta_j^{-1}
\]

on \(R_{\mathrm{sf}}\overline\otimes R_{\mathrm{sf}}\cong R_{\mathrm{sf}}\), the product trace is preserved. A nonzero power cannot be inner: the nonzero-slice intertwiner proof, Lemma 4.1 of the same lesson, would make the corresponding power of \(\theta_i\) inner. Thus \(B_{ij}\) is approximately inner with asymptotic period zero.

Let \(\sigma_0\) be the explicit aperiodic product automorphism of \(R\) from TIC01, and let \(A_0=\sigma_0\otimes\mathrm{id}_{B(\ell^2)}\). The aperiodic comparison theorem makes every \(B_{ij}\) outer conjugate to \(A_0\). The aperiodic branch of Matrix eigenvectors and tensor absorption, Theorem 6.1, followed by the type-I amplification conjugacy from the trace-scaling lesson, gives
\(\theta_i\sim_o\theta_i\otimes A_0\).
Here \(\sim_o\) denotes outer conjugacy. Hence

\[
 \begin{aligned}
 \theta_2
 &\sim_o\theta_2\otimes A_0
 \sim_o\theta_2\otimes B_{12}\\
 &\cong B_{22}\otimes\theta_1
 \sim_o A_0\otimes\theta_1
 \sim_o\theta_1 .
 \end{aligned}
 \tag{8}
\]

The middle map permutes the three actual tensor factors. There is no tensor cancellation step.

Consequently \(\theta_2=\operatorname{Ad}c\circ\alpha\), where
\(\alpha=\Psi\theta_1\Psi^{-1}\).
A normal automorphism of the semifinite factor rescales its trace by a positive scalar. Those scalars cancel under conjugation, so \(\tau\alpha=\lambda\tau\). The complete trace-scaling coboundary proof in DDP Section 6 gives \(z\) with

\[
 c=z^*\alpha(z).
\]

Then \(\operatorname{Ad}z\circ\theta_2\circ\operatorname{Ad}z^*=\alpha\), so (7) holds with \(\Phi=\operatorname{Ad}z^*\circ\Psi\). For \(\lambda>1\) the same coboundary statement follows by applying its contracting case to \(\alpha^{-1}\) and \(\alpha^{-1}(c^*)\), as checked in the trace-scaling lesson. Only \(0<\lambda<1\) is needed below.

## 4. Identifying every injective type IIIλ factor

Let \(A\) be an injective factor of type \(\mathrm{III}_\lambda\) with separable predual. TIC02 constructs a full normal discrete decomposition

\[
 A=N_A\rtimes_{\theta_A}\mathbb Z,\qquad
 N_A\cong R_{\mathrm{sf}},\qquad
 \tau_A\theta_A=\lambda\tau_A.
 \tag{9}
\]

It proves the centralizer's injectivity through the periodic expectation, identifies its finite corner by the finite injective-factor theorem, and constructs a filling family to recover the whole semifinite algebra. These conclusions concern the actual algebra, not just its stabilized isomorphism class.

Apply the same result to \(R_\lambda\), which meets all its hypotheses by Section 2:

\[
 R_\lambda=N_\lambda\rtimes_{\theta_\lambda}\mathbb Z.
\]

Choose normal identifications of both semifinite algebras with \(R_{\mathrm{sf}}\). Their transported traces are positive scalar multiples of its trace; both generators still have multiplier \(\lambda\). Equation (7) gives a normal isomorphism \(f:N_A\to N_\lambda\) with \(f\theta_A=\theta_\lambda f\).

The normal crossing transport AC07, now with no inner correction, gives

\[
 N_A\rtimes_{\theta_A}\mathbb Z
       \longrightarrow
 N_\lambda\rtimes_{\theta_\lambda}\mathbb Z,\qquad
 x\mapsto f(x),\quad U_A\mapsto U_\lambda .
 \tag{10}
\]

The regular-representation proof establishes normality, onto range and normal inverse on the full algebras. It follows that

\[
 A\cong R_\lambda,\qquad
 A\cong A\overline\otimes R_\lambda .
 \tag{11}
\]

The second assertion uses (6) and the first. We have identified an arbitrary injective factor with the specified product without using type III₁ uniqueness.

## 5. Strong λ-stability of an AFD type III₁ factor

Let \(M\) satisfy the uniqueness theorem's hypotheses, fix \(0<\lambda<1\), and put

\[
 T=\frac{2\pi}{|\log\lambda|}.
\]

Choose a faithful normal state \(\varphi\) on \(M\), which exists because its predual is separable. The full MI theorem gives approximate innerness of
\(\alpha=\sigma_T^\varphi\).
MD01–05 gives

\[
 N=M\rtimes_\alpha\mathbb Z
       \quad\text{of type }\mathrm{III}_\lambda.
 \tag{12}
\]

AFD implies injective. Crossing by the amenable group \(\mathbb Z\) preserves injectivity, by Averaging crossed products and injectivity, Theorem 2.3. The regular Hilbert space can be chosen separable, so \(N\) has separable predual. Section 4 applies and gives

\[
 N\cong R_\lambda\cong R_\lambda\overline\otimes R_\lambda
       \cong N\overline\otimes R_\lambda.
\]

The hypotheses of the complete absorption descent theorem DAS01–07 are now verified: the original algebra is a type III factor with separable predual, its sampled automorphism is approximately inner, and the crossing absorbs this particular \(R_\lambda\). Therefore

\[
 M\cong M\overline\otimes R_\lambda.
 \tag{13}
\]

As \(\lambda\) was arbitrary, this proves strong \(\lambda\)-stability for every parameter in \((0,1)\). We need no coherent choice of the isomorphisms for different parameters.

This establishes the full absorption assertion of the source's Corollary 4.21. It uses the type III₁ approximate-innerness theorem only in its stated AFD, separable-predual scope.

## 6. A reference factor and tracial stability

Theorem ODT01–07 proves that

\[
 R_\lambda\overline\otimes R_\mu
\]

is AFD of type III₁ whenever the logarithm ratio is irrational. The specified factors exist by Section 2, and their product has separable predual. In particular \(\mathcal P\) in (2) has all the hypotheses imposed on \(M\). The ratio \(\log2/\log3\) is irrational: a positive rational value \(p/q\) would imply \(2^q=3^p\), contrary to parity.

Apply (13) with \(\lambda\) and with \(\mu\). If \(f_\lambda:M\to M\overline\otimes R_\lambda\) and \(f_\mu:M\to M\overline\otimes R_\mu\) are the resulting maps, then

\[
 (f_\lambda\otimes\mathrm{id}_{R_\mu})\circ f_\mu
 :M\longrightarrow M\overline\otimes R_\lambda
                         \overline\otimes R_\mu
 \tag{14}
\]

is a normal isomorphism with normal inverse. This proves absorption of the chosen irrational reference product. Reindexing its two types of coordinates also gives
\(\mathcal P\overline\otimes\mathcal P\cong\mathcal P\).

The complete tracial-product argument CTA04–07 gives
\(R_\lambda\overline\otimes R\cong R_\lambda\).
Using any one isomorphism (13),

\[
 M\overline\otimes R
 \cong M\overline\otimes R_\lambda\overline\otimes R
 \cong M\overline\otimes R_\lambda
 \cong M.
 \tag{15}
\]

Thus \(M\) is strongly stable. Both (14) and (15) are constructed isomorphisms; they are not cancellation assertions.

## 7. The fixed algebra of the product circle action

Two circle models enter the proof. On
\(R=\bigotimes_{n\ge1}(M_2,\operatorname{tr}_2)\), define

\[
 b_z=\bigotimes_{n\ge1}\operatorname{Ad}
                \begin{pmatrix}\overline z&0\\0&1\end{pmatrix}.
 \tag{16}
\]

It preserves the trace \(\tau\), and \(b_z(e_{12}^{(n)})=\overline z e_{12}^{(n)}\). On the other hand, put

\[
 K=R\rtimes_{\sigma_0}\mathbb Z,\qquad
 \beta_z(x)=x\ (x\in R),\quad
 \beta_z(W)=\overline zW,
 \tag{17}
\]

as in TIC01. TIC07 proves \(K\cong R\). We shall prove an actual conjugacy

\[
 (R,b)\cong(K,\beta).
 \tag{18}
\]


The normal product action (16) is well defined by its trace-GNS unitaries. Those unitaries are continuous on finite tensor vectors, hence strongly continuous everywhere. Finite vector coefficients are norm dense in the predual, so the action is point-predual norm continuous.

Let \(F=R^b\), and average \(b\) with probability Haar measure to obtain \(E_F:R\to F\). The averaging is normal: on the predual it is the Bochner integral of the norm-continuous orbit. It is unital, completely positive, \(F\)-bimodular and trace preserving, and thus faithful.

The fixed algebra \(F\) is a finite factor. To prove this, let \(g_n\) interchange the first \(n\) tensor positions with the next \(n\). The finite permutation unitary \(u_n\) commutes with the coordinate product of the same two-by-two matrix in (16), so \(u_n\in F\). Write \(\rho_n=\operatorname{Ad}u_n\). For any \(x,y\in R\),

\[
 \tau(\rho_n(x)y)\longrightarrow\tau(x)\tau(y).
 \tag{19}
\]

For local \(x,y\), their supports become disjoint, making the equation eventually exact by product independence. For general \(x,y\), choose bounded local \(x_0,y_0\) close in trace \(2\)-norm. Cauchy–Schwarz and trace preservation bound the error by

\[
 \|x-x_0\|_2\|y\|_2+
 \|x_0\|_2\|y-y_0\|_2+
 |\tau(x-x_0)|\,|\tau(y)|
 +|\tau(x_0)|\,|\tau(y-y_0)|.
\]

This can be made arbitrarily small, proving (19).

If \(x\in F'\cap R\), then \(\rho_n(x)=x\). Equation (19) gives
\(\tau(xy)=\tau(x)\tau(y)\) for all \(y\). Taking \(y=(x-\tau(x)1)^*\) proves \(x=\tau(x)1\). Therefore

\[
 F'\cap R=\mathbb C1.
 \tag{20}
\]

In particular \(F\) is a factor. It contains the local diagonal algebras of every size, hence infinitely many nonzero orthogonal projections and cannot be a finite matrix algebra. Its faithful trace makes it type \(\mathrm{II}_1\). It is injective as the expected subalgebra of injective \(R\), and has separable predual. The finite injective-factor theorem used in TIC02 therefore identifies \(F\cong R\).

## 8. A homogeneous unitary identifies the circle models

Write \(t=e_{12}\), \(p=tt^*=e_{11}\) and \(q=t^*t=e_{22}\) in the first tensor position. Both \(p,q\) belong to \(F\), and \(\tau(p)=\tau(q)=1/2\). Factor projection comparison PC Section 2 gives a partial isometry \(s\in F\) with

\[
 s^*s=p,\qquad ss^*=q.
\]

Indeed comparison gives a subequivalence in one direction; equality of the faithful traces makes the leftover projection zero. The self-adjoint unitary \(u=s+s^*\in F\) interchanges \(p\) and \(q\). Define

\[
 v=t+utu^*.
 \tag{21}
\]

Its two summands have respectively initial projections \(q,p\) and final projections \(p,q\). These are orthogonal and sum to one on both sides. Hence

\[
 v^*v=vv^*=1,\qquad b_z(v)=\overline z v.
 \tag{22}
\]

The second equation uses \(u\in F\). No assertion that the ordinary first-leg flip is fixed by \(b\) is involved.

Let \(\eta=\operatorname{Ad}v|_F\). Equation (22) makes \(vFv^*=F\), so this is an automorphism of \(F\), preserving its trace. We claim the full normal identification

\[
 R\cong F\rtimes_\eta\mathbb Z,
 \tag{23}
\]

with \(v\) corresponding to the implementing unitary and \(b\) to the negative dual action.

For each \(n\in\mathbb Z\), the spectral subspace
\(R_n=\{x:b_z(x)=\overline z^{\,n}x\}\) is exactly \(Fv^n\): multiply \(x\in R_n\) by \(v^{-n}\), and the product is fixed. Circle Fejér averaging, proved in CC0, makes finite sums of these subspaces strongly dense on bounded sets, and \(2\)-norm dense.

Here is the normal regular implementation. On
\(\ell^2(\mathbb Z,L^2(F,\tau|_F))\), set

\[
 J(\delta_n\otimes a\Omega_F)=v^n a\Omega_R.
 \tag{24}
\]

Orthogonality of characters and trace preservation give

\[
 \tau\bigl((v^n a)^*v^m d\bigr)
      =\begin{cases}\tau(a^*d),&n=m,\\0,&n\ne m.\end{cases}
\]

Thus \(J\) is isometric; the Fourier density just proved makes it onto. Left multiplication by \(x\in F\) becomes the regular coefficient
\(\eta^{-n}(x)\) in coordinate \(n\), and left multiplication by \(v\) becomes the shift \(n\mapsto n+1\). Consequently the unitary identifies exactly the two generated von Neumann algebras. It has a normal inverse, proves (23), and checks negative dual equivariance on both generators.

Since \(R\) is a factor, the factoriality criterion MPR02 implies every nonzero power of \(\eta\) is outer. Moreover

\[
 \operatorname{Ct}(F)=\operatorname{Inn}(F).
 \tag{25}
\]

To verify the precise input, identify \(F\cong R\), apply the equivariant type-I amplification result in Trace scaling, Proposition 3.1, then its Theorem 4.2 on \(R_{\mathrm{sf}}\). If an automorphism of \(F\) is centrally trivial, its tensor product with \(\mathrm{id}_{B(\ell^2)}\) is inner. Lemma 4.1 in that lesson, by a nonzero slice of an implementing unitary, makes the automorphism itself inner. The converse holds because inner automorphisms act trivially on central sequences.

Therefore \(p_a(\eta)=0\). Every automorphism of \(F\cong R\) is approximately inner by Hyperfinite finite factors, Theorem 6.3. The factor is strongly stable. AC01–07 makes \(\eta\) outer conjugate to \(\sigma_0\) and gives a normal dual-equivariant isomorphism

\[
 F\rtimes_\eta\mathbb Z\cong R\rtimes_{\sigma_0}\mathbb Z.
\]

Together with (23), this is the actual conjugacy (18).

## 9. Two exact absorption identities for a modular dual

Return to an AFD type III₁ factor \(M\), a state \(\varphi\), and

\[
 N=M\rtimes_{\sigma_T^\varphi}\mathbb Z,\qquad
 T=\frac{2\pi}{|\log\lambda|}.
\]

Let \(\theta\) be its negative dual circle action.

First,

\[
 (N,\theta)\cong
 (N\overline\otimes R_\lambda,\theta\otimes\mathrm{id}).
 \tag{26}
\]

Choose \(f:M\to M\overline\otimes R_\lambda\) from (13), and put
\(\chi=(\varphi\otimes\omega_\lambda)\circ f\).
The product modular formula gives

\[
 f\sigma_T^\chi f^{-1}
 =\sigma_T^\varphi\otimes\sigma_T^{\omega_\lambda}
 =\sigma_T^\varphi\otimes\mathrm{id},
\]

using (4). The full state-change construction CDS07, equations (CDS.31)–(CDS.33), identifies the crossings for \(\chi\) and \(\varphi\) and conjugates their dual actions exactly. Crossing the displayed tensor action and regrouping the regular Hilbert space gives (26). This argument does not require \(f\) to preserve \(\varphi\).

Second, tracial stability (15) and the exact central-dual absorption theorem CDS01–07 give

\[
 (N,\theta)\cong(N\overline\otimes R,\theta\otimes b).
 \tag{27}
\]

That theorem uses positive dual characters and the positive product action. Replace \(z\) by \(z^{-1}\) in its equivariance equation: both signs reverse, giving precisely the negative \(\theta\) and \(b\) used here. It is an actual conjugacy. Section 8 now gives

\[
 (N,\theta)\cong(N\overline\otimes K,\theta\otimes\beta).
\]


Put

\[
 (S,e)=(R_\lambda\overline\otimes K,
                         \mathrm{id}_{R_\lambda}\otimes\beta).
 \tag{28}
\]

Combining the two exact conjugacies, and interchanging tensor legs, yields

\[
 (N,\theta)\cong(N\overline\otimes S,\theta\otimes e).
 \tag{29}
\]

Normal tensor maps and their inverses are obtained by their spatial implementations or the bounded-array tensor theorem. Every map in (29) is a genuine conjugacy of the continuous circle actions.

## 10. The opposite-dual pair has one cocycle class

Let \(M_1,M_2\) be AFD type III₁ factors with separable predual, choose states \(\varphi_i\), and use the same \(T\) and \(\lambda\). Set

\[
 N_i=M_i\rtimes_{\sigma_T^{\varphi_i}}\mathbb Z,
 \qquad
 \delta_{ij,z}=\theta^i_z\otimes\theta^j_{z^{-1}}
 \quad\text{on }N_i\overline\otimes N_j .
 \tag{30}
\]

By Section 4 each \(N_i\cong R_\lambda\); (6) then makes each tensor base \(N_i\overline\otimes N_j\cong R_\lambda\). In particular it is an injective type \(\mathrm{III}_\lambda\) factor with separable predual.

ODT01–06 proves that

\[
 (N_i\overline\otimes N_j)\rtimes_{\delta_{ij}}\mathbb T
\]

is again a factor of type \(\mathrm{III}_\lambda\). Its normal identification retains and then absorbs the countable type-I factor. All hypotheses of the circle classification TIC09 are therefore satisfied. It makes \(\delta_{ij}\) cocycle conjugate to the identity action on its base tensored with \(\beta\). Transport any isomorphism of that base with \(R_\lambda\) to obtain

\[
 \delta_{ij}\sim_c e
 \qquad(i,j\in\{1,2\}),
 \tag{31}
\]

where \(\sim_c\) denotes cocycle conjugacy and \(e\) is (28). This is the full opposite-dual assertion of the source's Corollary 4.19, including the cocycle and its normal conjugating map. It is valid also when \(i=j\).

For use in the next step, cocycle conjugacy is an equivalence relation and survives tensoring with another action. These facts have explicit cocycles. If

\[
 b_g=F\circ\operatorname{Ad}u_g\circ a_g\circ F^{-1},
 \qquad
 c_g=G\circ\operatorname{Ad}v_g\circ b_g\circ G^{-1},
\]

then the composite is implemented by \(GF\) and the \(a\)-cocycle

\[
 w_g=F^{-1}(v_g)u_g.
 \tag{32}
\]

Indeed \(u_g a_g(F^{-1}(v_h))=F^{-1}(b_g(v_h))u_g\), so
\(w_ga_g(w_h)=F^{-1}(v_{gh})u_{gh}\).
For the inverse use \(F(u_g^*)\), a \(b\)-cocycle. For tensoring use \(u_g\otimes1\); factor permutation is an ordinary conjugacy. These operations preserve strong continuity and normality.

## 11. The three-factor comparison and uniqueness

Use the two factors in Section 10 and the absorption (29) for each. Then

\[
 \begin{aligned}
 \theta^2
 &\cong\theta^2\otimes e
 \sim_c\theta^2\otimes\delta_{12}\\
 &\cong\delta_{22}\otimes\theta^1
 \sim_c e\otimes\theta^1
 \cong\theta^1.
 \end{aligned}
 \tag{33}
\]

All algebras in this chain are specified by (28)–(30). The middle permutation reorders

\[
 N_2\otimes N_1\otimes N_2
       \longrightarrow N_2\otimes N_2\otimes N_1
\]

and changes the order of the three actions
\(\theta^2_z,\theta^1_z,\theta^2_{z^{-1}}\) to
\(\theta^2_z,\theta^2_{z^{-1}},\theta^1_z\).
It is exactly \(\delta_{22,z}\otimes\theta^1_z\). Thus (33) compares the original dual actions by genuine continuous cocycles, using (32), without cancelling a tensor factor.

Cocycle conjugacy gives a normal isomorphism of the circle crossings. The full regular proof is NR Section 5. To fix its orientation, if
\(b_z=F\operatorname{Ad}u_z\,a_zF^{-1}\),
then the map from the \(a\)-crossing to the \(b\)-crossing is

\[
 x\longmapsto F(x),\qquad
 \lambda_a(z)\longmapsto F(u_z^*)\lambda_b(z).
 \tag{34}
\]

NR5 implements it by a multiplication unitary on the full regular Hilbert space; its inverse is normal and the displayed image generates the target algebra.

Finally normal double duality, ND, applied to the original integer actions, gives

\[
 N_i\rtimes_{\theta^i}\mathbb T
       \cong M_i\overline\otimes B(\ell^2(\mathbb Z)).
 \tag{35}
\]

Each \(M_i\) is properly infinite. The filling isometries and normal bounded-array inverse in CA Section 6 identify the right side with \(M_i\). Combining (33)–(35) proves \(M_1\cong M_2\).

Take \(M_2=\mathcal P\), whose AFD, type III₁ and separability properties were proved in Section 6. This gives (2), and hence the uniqueness theorem. Taking any other irrational pair gives its stated alternative reference model.

## 12. Solved checks and source scope

**Exercise 1: the two times.** For \(\lambda=1/2\), compute the modular sampling time \(T\) and the corresponding center-flow period of \(M\rtimes_{\sigma_T^\varphi}\mathbb Z\).

**Solution.** They are \(T=2\pi/\log2\) and \(2\pi/T=\log2\), respectively. The subtype is \(e^{-2\pi/T}=1/2\). Replacing it with \(e^{-T}\) would change the factor parameter.

**Exercise 2: filling the homogeneous unitary.** Verify both unitary identities for (21), and explain why its two terms have the same circle degree.

**Solution.** The initial projections are \(q\) and \(uqu^*=p\), and the final projections are \(p\) and \(upu^*=q\). Cross terms in \(v^*v\) vanish because the final projections are orthogonal; cross terms in \(vv^*\) vanish because the initial projections are orthogonal. The diagonal terms sum to one. Since \(b_z(u)=u\), the two terms each transform by \(\overline z\). The partial isometry \(s\) must be chosen inside \(F\), not just inside \(R\).

**Exercise 3: the three legs.** On an elementary tensor \(x\otimes y\otimes z\in N_2\otimes N_1\otimes N_2\), check the middle equality of (33).

**Solution.** After applying the action and swapping the second and third factors, the result is

\[
 \theta^2_t(x)\otimes\theta^2_{t^{-1}}(z)
                       \otimes\theta^1_t(y).
\]

This is \((\delta_{22,t}\otimes\theta^1_t)(x\otimes z\otimes y)\). Normality extends the equality from elementary tensors to the full tensor product.

**Exercise 4: composing the absorption maps.** If \(f_\lambda\) and \(f_\mu\) have the domains in Section 6, why does
\((f_\lambda\otimes\mathrm{id}_{R_\mu})f_\mu\) have the desired target?

**Solution.** The first map lands in \(M\otimes R_\mu\). The next applies \(f_\lambda\) to that \(M\)-coordinate and leaves the existing \(R_\mu\)-coordinate fixed, giving \(M\otimes R_\lambda\otimes R_\mu\). Its inverse is \(f_\mu^{-1}(f_\lambda^{-1}\otimes\mathrm{id}_{R_\mu})\), with the same association of tensor products.

**Exercise 5: absorption is not cancellation.** Give an algebra that absorbs \(R\) but is not isomorphic to \(R\).

**Solution.** Let \(A=L^\infty([0,1])\overline\otimes R\). Since \(R\overline\otimes R\cong R\), the algebra \(A\) absorbs \(R\). It has a nonscalar center, whereas \(R\) is a factor. Thus no general inference \(A\cong A\otimes R\Rightarrow A\cong R\) is valid. The proof of uniqueness above uses the dual-action comparison (33) and double duality, beyond the absorption equations.

The source theorem is Masamichi Takesaki, *Theory of Operator Algebras III*, Chapter XVIII, Theorem 4.16(i), printed pages 389 and 395–396. Sections 5–6 establish Corollary 4.21, printed page 393; Section 10 establishes Corollary 4.19, printed page 391. The semifinite comparison uses the earlier programme proof corresponding to XVII.3.12. The product-circle identification in Sections 7–8 makes explicit the relation between the two models used in the final argument. All source mathematics is written independently through the stated programme proofs; no source-book pages are included.

The result here concerns AFD type III₁ factors with separable predual. It does not classify measured groupoids or remove the separability hypothesis. Those are separate mathematical statements.

