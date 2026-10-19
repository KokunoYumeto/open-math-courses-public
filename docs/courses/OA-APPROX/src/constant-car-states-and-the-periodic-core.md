# Constant CAR states and the periodic core

*Written by GPT-6.1 Sol (OpenAI), Ultra, October 2026. Author self-checked relative to the stated prerequisites; not independently reviewed. New original text: public domain (CC0).*

An infinite sequence of identical two-level density matrices gives a type III factor when the two eigenvalues differ. To find its parameter, we must compute a modular invariant. A period of one modular action, or even its complete group of inner times, does not by itself justify the subtype.

We use [Infinite tensor products and their reference states](infinite-tensor-products.md), especially its explicit faithful product representation, local slice maps and closed modular graph, and [Fermions, Fock space and quasi-free factors](car-fock-and-quasifree-states.md), including its direct constant-state type III proof in Section 20. Sections 4–5 below construct the represented period-circle crossed product and continuous core. Scalar Lebesgue integration and Hilbert completion underlie the Fourier and measurable-phase arguments.

The modular foundations can be followed through [BG1–6](../components/bounded-graph-modular-foundations.md#bg1), which prove normalization, fullification and the complete closed modular graphs for an arbitrary left Hilbert algebra. [FC1–5](../components/fixed-modular-corners-from-whole-graphs.md#fc1) prove fixed-corner GNS and modular restriction for every faithful normal semifinite weight, even when the corner has infinite weight. These arguments supply the pure Hilbert-algebra and fixed-corner steps in the MG comparison. The finite-ideal graph closedness and every-weight comparison retain their stated prerequisite proofs. Type III corner transport is a separate prerequisite of the general reverse inclusion in MG-4; the product-spectrum upper bound below does not use it.

For the subtype inference, Section 6 uses the full finite-ideal spectral comparison and the every-weight fixed-corner comparison in [MG-0–3](../../OA-FLOW/OA-FLOW-MG.html#oa-flow.mg.3). [PP00–PP04](../components/periodic-corner-spectra-from-factor-contact.md#pp00) provide the concrete filter and factor-contact arguments showing that every integer modular degree survives in every nonzero fixed corner. We also compute the entire spectrum of the product modular operator from its coefficient domain. These two calculations determine the intersection over **all** faithful normal semifinite weights, including weights of infinite total mass. The center calculation then gives, for this factor with least positive center period \(L\),
\[
M\text{ is type }\mathrm{III}_{e^{-L}}. \tag{1}
\]
Here (1) is a consequence of the all-weight calculation, not a premise inferred from periodicity. The upper bound on the intersection comes from the explicit product modular operator; its lower bound comes from comparison with every weight. The general type III corner-transport step of MG-4 is therefore unnecessary for this particular upper bound. Its full stated proof remains available for the general comparison problem.

The periodic subtype calculation fixes a separable one-particle Hilbert space. The subtype calculation below assumes this space is infinite-dimensional. The earlier CAR lesson separately retains finite-dimensional and arbitrary directed finite-mode approximation statements.

## 1. The constant faithful product state

Let \(0<p<1\), \(p\ne\tfrac12\), and set
\[
\rho=\begin{pmatrix}1-p&0\\0&p\end{pmatrix},
\qquad \phi_0(x)=\operatorname{Tr}(\rho x).
\]
On a separable infinite-dimensional one-particle space, the CAR parity strings identify the state with
\[
(M,\phi)=\bigotimes_{j=1}^{\infty}(M_2,\phi_0). \tag{2}
\]
This is an identification of the completed GNS representations, not just of their finite moments. Write \(A_n=\bigotimes_{j=1}^nM_2\subset M\) and let \(\Omega\) be the product GNS vector.

The state \(\phi\) is faithful and normal. For clarity, in one coordinate represent \(M_2\) by left multiplication on its Hilbert–Schmidt space with reference vector \(\rho^{1/2}\). Since \(\rho\) is invertible, this vector is cyclic both for left and for right multiplication. Finite left products applied to \(\Omega\) span a dense subspace of the pointed product Hilbert space. Finite right products commute with the represented algebra and have the same density property. Thus \(\Omega\) is cyclic for \(M\) and for \(M'\), hence separating for \(M\). Its vector state is faithful.

Factorality follows from the concrete expectations constructed in Section 2. If \(z\in Z(M)\), bimodularity puts \(E_n(z)\) in \(Z(A_n)=\mathbb C1\); state preservation makes it \(\phi(z)1\). Lemma 2.1 gives \(z=\phi(z)1\). The same lemma proves that the increasing finite matrix algebras have strong closure \(M\), so \(M\) is AFD.

For the modular calculation, choose in one Hilbert–Schmidt leg the orthonormal basis
\[
 \rho^{1/2},\qquad
 \begin{pmatrix}\sqrt p&0\\0&-\sqrt{1-p}\end{pmatrix},
 \qquad e_{12},\qquad e_{21}.
\]
Finite tensor words in these vectors, with the reference vector in all remaining legs, form an orthonormal basis \((\xi_\kappa)\) of the pointed completion. Put \(m_\kappa=\#e_{12}-\#e_{21}\) and \(d_\kappa=((1-p)/p)^{m_\kappa}\). The coefficient operator
\[
 \Delta\Bigl(\sum_\kappa c_\kappa\xi_\kappa\Bigr)
   =\sum_\kappa d_\kappa c_\kappa\xi_\kappa,
 \qquad
 \operatorname{Dom}\Delta
   =\Bigl\{\sum_\kappa c_\kappa\xi_\kappa:
                   \sum_\kappa d_\kappa^2|c_\kappa|^2<\infty\Bigr\}
\]
is positive and selfadjoint: its resolvent at a nonreal number is the bounded coefficient inverse, whose image satisfies the displayed domain condition. Let \(J\) conjugate coefficients and interchange \(e_{12}\) with \(e_{21}\) in each word. On a finite matrix vector, \(J\Delta^{1/2}(a\Omega)=a^*\Omega\). The entire domains are
\[
 \operatorname{Dom}(J\Delta^{1/2})
       =\{\xi:\sum_\kappa d_\kappa|c_\kappa|^2<\infty\},
 \qquad
 \operatorname{Dom}(J\Delta^{-1/2})
       =\{\xi:\sum_\kappa d_\kappa^{-1}|c_\kappa|^2<\infty\}.
\]
Testing the adjoint identity on each basis vector forces the coefficients of the antilinear adjoint, and their square summability gives exactly the second domain. Thus \((J\Delta^{1/2})^*=J\Delta^{-1/2}\). Membership in the product domain additionally requires \(\sum d_\kappa^2|c_\kappa|^2<\infty\), and gives \((J\Delta^{1/2})^*(J\Delta^{1/2})=\Delta\) on its full displayed domain. Truncating coefficient series converges simultaneously in vector norm and in each corresponding weighted norm, so finite matrix vectors are graph cores. The full graph argument in Section 11 of the tensor-product lesson, using \(E_n(x)\Omega\to x\Omega\) and \(E_n(x^*)\Omega\to x^*\Omega\), identifies \(J\Delta^{1/2}\) with the closure of \(x\Omega\mapsto x^*\Omega\) on **all** of \(M\Omega\). Indeed these approximating finite graph points converge to every initial graph point, while the finite-support core already closes to \(J\Delta^{1/2}\); the two closed graphs therefore agree. Thus this \(\Delta\) is \(\Delta_\phi\), rather than an operator specified only on an algebraic core. Its imaginary powers fix \(\Omega\), are strongly continuous by bounded coefficient convergence, and implement, on every local algebra,
\[
\sigma_t(x)=\rho_n^{it}x\rho_n^{-it}. \tag{3}
\]
Here \(x\in A_n\) and \(\rho_n=\rho^{\otimes n}\). Put
\[
\begin{aligned}
r&=\frac{1-p}{p},\\
\omega&=|\log r|,\\
P&=\frac{2\pi}{\omega},\\
\lambda&=\min(r,r^{-1}).
\end{aligned} \tag{4}
\]
In particular \(0<\lambda<1\) and \(\omega=|\log\lambda|\).

If \(b_j=e_{12}\) in coordinate \(j\), then
\[
\sigma_t(b_j)=r^{it}b_j. \tag{5}
\]
Consequently \(\sigma_P=\operatorname{id}\). This is the least positive period of the action: (5) forces \(t\log r\in2\pi\mathbb Z\) at any period. For each integer \(k\), there is a nonzero local operator \(x_k\) with
\[
\sigma_t(x_k)=e^{ik\omega t}x_k. \tag{6}
\]
Choose \(b_j\) or \(b_j^*\) with positive frequency \(\omega\), and multiply \(k\) copies in distinct coordinates when \(k>0\); use adjoints for negative \(k\), and \(x_0=1\). Products in distinct tensor coordinates are nonzero.

For comparison with the scalar overlap appearing in the tensor-product lesson, at any \(t\) for which the phases of \((1-p)^{it}\) and \(p^{it}\) differ one has
\[
1-\left|(1-p)^{1+it}+p^{1+it}\right|>0. \tag{7}
\]
Indeed, for \(a=1-p\), \(b=p\), \(|z|=|w|=1\),
\( |az+bw|^2=1-ab|z-w|^2\). This proves (7), but a divergence criterion is not the type III argument used here.

To prove type III, let \(X_j\) be a matrix of bounded norm in a tail leg. Right multiplication by \(\rho^{-1/2}X_j\rho^{1/2}\) gives a commuting operator \(R_j\) with \(R_j\Omega=X_j\Omega\) and \(\|R_j\|\le C(p)\|X_j\|\), where \(C(p)\) is independent of \(j\). Given \(u\in M\), approximate \(u\Omega\) by a local vector \(a\Omega\). For \(j\) outside the support of \(a\),
\[
 [X_j,u]\Omega=(X_j-R_j)(u-a)\Omega,
 \qquad
 \|[X_j,u]\Omega\|\le(1+C(p))\|X_j\|\,\|(u-a)\Omega\|.
\]
The commutator commutes with the right local algebra and has a uniform norm bound. Density of its right orbit extends this limit to every vector. Repeating it with adjoints proves \([X_j,u]\to0\) strongly*. Apply this to the tensor matrix unit \(b_j\) of (5), with its CAR parity string already included in the identification (2).

The projections \(b_j^*b_j\) and \(b_jb_j^*\) converge weakly to \(p1\) and \((1-p)1\), respectively. Between two finite-support vectors, this is an exact equality once \(j\) is beyond their supports; their uniform bounds extend it to arbitrary vectors.

Suppose that \(e\in M\) is a nonzero finite projection. Its corner is a finite factor: the contact argument in Sections 8.5 and 11.3 proves factoriality of every nonzero corner of a factor. On the separable Hilbert space \(eH\), Sections 18–19 of the CAR lesson construct a faithful normal tracial state \(\tau\) on this finite factor, with \(\tau(e)=1\). This is the supplied finite-factor trace proof, including normality through summable vector coefficients; it is not an infinite-product classification criterion. Set \(B_j=eb_je\). Strong* commutator convergence gives
\[
 eb_j^*b_je-B_j^*B_j=eb_j^*(1-e)b_je\longrightarrow0,
 \qquad
 eb_jb_j^*e-B_jB_j^*=eb_j(1-e)b_j^*e\longrightarrow0
\]
strongly: for example \((1-e)b_je=(1-e)[b_j,e]e\to0\), and multiplying by the uniformly bounded remaining factors preserves the limit. Hence \(B_j^*B_j\to pe\) and \(B_jB_j^*\to(1-p)e\) weakly. Normality passes these bounded limits through \(\tau\): first pass each vector coefficient, then control the tail of its summable coefficient representation uniformly. Traciality gives \(p=1-p\), contradicting the hypothesis. Thus \(M\) has no nonzero finite projection and is type III. The complete GNS identification in the CAR lesson transports this conclusion to the CAR factor.

## 2. Slice expectations and the occupation diagonal

Regroup the represented product as \(M=A_n\bar\otimes M_{>n}\), using the head–tail Hilbert unitary and the matrix-unit corner calculation in Section 10.2 below. Compression by the tail reference vector, followed by amplification with the tail identity, constructs the normal unital completely positive expectation
\[
\begin{aligned}
E_n&:M\longrightarrow A_n,\\
E_n&=\operatorname{id}_{A_n}\bar\otimes\phi_{>n}.
\end{aligned}
\tag{8}
\]
It is \(A_n\)-bimodular, preserves \(\phi\), and commutes with \(\sigma_t\). The following construction proves these assertions on the represented closure.

### Faithful matrix vectors and concrete local slices

Here the slice map in (8) can be constructed directly. Write the product Hilbert space as \(H_n\otimes H_{>n}\), and let \(V_n\eta=\eta\otimes\Omega_{>n}\). On \(B(H)\) put
\[
\widehat E_n(x)=(V_n^*xV_n)\otimes1.
\]
Compression is normal: its vector coefficients are vector coefficients of \(x\). Amplification is normal as well. For an elementary tensor coefficient, this follows by expanding its two vectors in finite sums of elementary tensor vectors; the uniform operator bound then gives the conclusion for all vector coefficients. Both maps are unital and completely positive, since their matrix amplifications preserve positivity by compression and by tensoring with the identity. Their composition is contractive and is bimodular over \(B(H_n)\otimes1\).

On a finite left product, compression replaces each tail leg by its reference-vector value. To pass to the represented closure, choose an orthonormal basis \((f_u)\) of the finite-dimensional \(H_n\). The amplified compression is the finite sum
\[
 \widehat E_n(x)=\sum_{u,v}
 \langle f_u\otimes\Omega_{>n},x(f_v\otimes\Omega_{>n})\rangle
                 (F_{uv}\otimes1).
\]
It is therefore weak-operator continuous on every net, with no assumption that the approximating net is uniformly bounded. The finite-dimensional subspace \(A_n\subset B(H_n)\) is weak-operator closed. The bicommutant closure of the local left algebra consequently maps into \(A_n\), and compression fixes \(A_n\). This restriction is precisely \(E_n\). It preserves \(\phi\), because \(V_n\Omega_n=\Omega\), and commutes with the coordinate action because its implementing unitaries fix the reference vectors. For normality on arbitrary ultraweak nets, each coefficient is a vector functional and the displayed sum is finite; this also gives the exact all-net argument used in Section 10.3.

For completeness, the cyclicity used in Lemma 2.1 needs only finite matrix algebra. In one Hilbert--Schmidt coordinate, the maps \(a\mapsto a\rho^{1/2}\) and \(a\mapsto\rho^{1/2}a\) are bijective because \(\rho\) is invertible. Their finite tensor products fill each finite-support Hilbert space. Consequently finite left and finite right products applied to \(\Omega\) are dense in the pointed completion. Every right product commutes with the left products and their strong closure. An element of \(M\) annihilating \(\Omega\) therefore annihilates that dense right-product orbit and is zero. The vector state is normal, and \(\phi(x^*x)=0\) now implies \(x=0\), so it is faithful. The orthogonal-projection and dense-orbit argument in Lemma 2.1 consequently requires no modular theorem.

**Lemma 2.1.** For every \(x\in M\), \(E_n(x)\to x\) strongly*. Equivalently, the bounded sequence converges strongly both for \(x\) and for \(x^*\).

**Proof.** Let \(Q_n\) project onto \(A_n\Omega\). For \(a\in A_n\), state preservation and bimodularity give
\[
\langle a\Omega,E_n(x)\Omega\rangle
=\phi(a^*E_n(x))=\phi(a^*x).
\]
Since \(E_n(x)\Omega\in A_n\Omega\), this proves
\[
E_n(x)\Omega=Q_nx\Omega. \tag{9}
\]
The subspaces increase and their union is dense, so \(Q_n\to1\) strongly. Thus the difference in (9) tends to zero, as does the corresponding difference for \(x^*\).

For every finite-support vector \(\eta\in H_k\) and \(n\ge k\), the same compression gives the stronger identity \(E_n(x)\eta=Q_nx\eta\). Indeed, the tail of \(\eta\) is the reference vector and \(Q_n\) is precisely the projection onto \(H_n\otimes\Omega_{>n}\). Thus convergence holds on all finite-support vectors. The differences have norm at most \(2\|x\|\), so their dense union extends convergence to every vector. Apply compression separately to \(x^*\), using \(E_n(x)^*=E_n(x^*)\), to obtain the strong* assertion. Equation (9) also gives the commutant-orbit proof requested in Exercise 2. \(\square\)

Let \(D_n\) be the diagonal algebra of \(A_n\), and put
\[
D=\left(\bigcup_nD_n\right)''.
\]
The product diagonal is identified with
\[
\begin{gathered}
L^\infty(X,\nu),\qquad X=\{0,1\}^{\mathbb N},\\
\nu=\bigotimes_{j=1}^{\infty}((1-p)\delta_0+p\delta_1).
\end{gathered} \tag{10}
\]
The identification maps occupation projections to coordinate indicator functions. Here is its passage to the full bounded measurable algebra. Use the completed Bernoulli measure constructed in Section 3. Cylinder inner products agree exactly with the inner products of local diagonal vectors; the cylinder-density proof there therefore gives a unitary
\(\overline{D\Omega}\to L^2(X,\nu)\). To lift a bounded measurable \(h\), average it over the cells \(C_s\) of the first \(n\) coordinates:
\[
 h_n=\sum_s\frac{\int_{C_s}h\,d\nu}{\nu(C_s)}1_{C_s}.
\]
Every denominator is positive, \(\|h_n\|_\infty\le\|h\|_\infty\), and these are the increasing finite-dimensional orthogonal projections of \(h\) in \(L^2\). Cylinder density proves \(h_n\to h\) in \(L^2\). Let \(d_n\in D_n\) be the corresponding cylinder operator. Both \(d_n\Omega\) and \(d_n^*\Omega\) are Cauchy. For every finite right product \(y'\),
\(\|(d_n-d_m)y'\Omega\|\le\|y'\|\,\|(d_n-d_m)\Omega\|\).
The uniform norm bound extends this to every vector, and the same argument applies to adjoints. Thus \(d_n\) converges strongly* to an element \(d\in D\). On each cylinder vector its restriction is multiplication by \(h\), and density gives the full multiplication operator.

Conversely, the finite coefficient formula for \(E_n\) puts \(E_n(d)\in D_n\) for \(d\in D\): it holds on local diagonal products and passes to their weak-operator closure. The corresponding functions have uniform bound \(\|d\|\), and Lemma 2.1 gives their \(L^2\) limit \(h\). This limit is essentially bounded with the same bound. Indeed, choose a subsequence with \(L^2\) errors at most \(2^{-2j}\); the sets where the error exceeds \(2^{-j}\) have summable measures, and the union of each tail has measure tending to zero. Outside the resulting null set the subsequence converges pointwise. The restriction of \(d\) to \(\overline{D\Omega}\) is therefore multiplication by \(h\). It is injective because \(\Omega\) separates \(M\). The lift above proves surjectivity, and restriction proves preservation of products and adjoints.

This is a **normal** identification in both directions. Restriction to the reducing subspace \(\overline{D\Omega}\) is normal, since every compressed vector coefficient is a vector coefficient on \(H\). Positivity is equivalent on the two sides: a positive \(h\) has positive averages and a positive strong limit, and a positive \(d\) has a positive multiplication restriction. The inverse order isomorphism consequently preserves least upper bounds of arbitrary bounded increasing positive nets. The concrete normality criterion, proved in Section 18 of the CAR lesson using positive functionals and summable vector coefficients, makes the inverse ultraweakly continuous on the entire algebra. Thus (10) is an identification of completed normal operator algebras, not merely of cylinder moments or an algebraic GNS subspace.

**Lemma 2.2.** \(D\) is a maximal abelian subalgebra of \(M\).

**Proof.** The local diagonals commute, so \(D\) is abelian. If \(x\in M\) commutes with \(D\), then \(E_n(x)\) commutes with \(D_n\), by \(A_n\)-bimodularity. In \(A_n\), the commutant of its full diagonal is just \(D_n\): commuting with each diagonal matrix unit kills every off-diagonal entry. Thus \(E_n(x)\in D_n\). Lemma 2.1 and strong closedness put \(x\in D\). \(\square\)

## 3. The product-state centralizer is a factor

The centralizer is the fixed algebra
\[
N=M^\sigma=\{x\in M:\sigma_t(x)=x\text{ for every }t\}.
\]
The restriction of \(\phi\) to \(N\) is a faithful normal tracial state by the following finite-density argument. If \(x\in N\), equivariance gives \(E_n(x)\in A_n^\sigma\), so \(E_n(x)\) commutes with \(\rho^{\otimes n}\). For every \(y\in M\), bimodularity and state preservation reduce both \(\phi(E_n(x)y)\) and \(\phi(yE_n(x))\) to the finite matrices \(E_n(x),E_n(y)\). Commutation with the density and cyclicity of the finite matrix trace make them equal. Lemma 2.1 passes the equality to \(\phi(xy)=\phi(yx)\). Conversely, if this equality holds for every \(y\), testing local matrix units makes \(E_n(x)\) commute with \(\rho^{\otimes n}\); equivariance and strong* convergence put \(x\in N\). This establishes the centralizer identity itself on the completed representation. On \(N\) it is tracial, and an isometry \(v\in N\) has \(\phi(1-vv^*)=0\), so faithfulness makes it unitary. Hence \(N\) is finite. The diagonal is fixed by each coordinate density, so \(D\subset N\).

For every finite permutation \(\pi\) of the coordinate set, there is a unitary \(v_\pi\) in a sufficiently large \(A_n\) that permutes its tensor legs. The identical tensor densities satisfy
\[
v_\pi\rho^{\otimes n}v_\pi^*=\rho^{\otimes n};
\]
hence \(v_\pi\in N\). On \(D\), conjugation permutes the Bernoulli coordinates.

### Direct diagonal density and permutation invariance

There is also an operator proof of the density and independence used in Lemma 3.1. Normality first shows that \(E_n(D)\subset D_n\), by checking this on local diagonal products. Lemma 2.1 gives
\[
\|E_n(z)-z\|_{2,\phi}=\|(E_n(z)-z)\Omega\|\longrightarrow0
\qquad(z\in D).
\]
Thus local diagonal elements are dense in the state \(L^2\) norm, directly in the pointed representation.

Let \(z\in D\) be invariant under finite permutations, and let \(f\) be local diagonal. Choose local diagonal \(g\) with \(\|z-g\|_{2,\phi}<\varepsilon\). A finite permutation moves the support of \(f\) disjointly from that of \(g\); call the image \(f_\pi\). The identical one-leg states imply that permutations preserve \(\phi\). Invariance gives \(\phi(zf)=\phi(zf_\pi)\), and disjoint finite tensor supports give exactly \(\phi(gf_\pi)=\phi(g)\phi(f)\). Cauchy--Schwarz in the abelian state algebra gives
\[
|\phi(zf)-\phi(z)\phi(f)|
\le\varepsilon\bigl(\|f\|_{2,\phi}+|\phi(f)|\bigr).
\]
Let \(\varepsilon\) tend to zero. Applying the equality to adjoints of all local \(f\), and then using their state \(L^2\) density, gives \((z-\phi(z)1)\Omega=0\). Faithfulness implies \(z=\phi(z)1\). Under (10) this is the conclusion of Lemma 3.1. The calculation uses finite tensor independence, rather than an imported zero-one theorem.

### Bernoulli measure and finite-permutation invariance

The following construction explains the measure and approximation steps used in Lemma 3.1. The domain is the countable product \(X=\{0,1\}^{\mathbb N}\), with the identical Bernoulli probability measure in (10); the functions are complex elements of \(L^\infty(X,\nu)\), and invariance means equality modulo null sets under every permutation fixing all but finitely many coordinates. The conclusion is constancy almost everywhere. We retain \(0<p<1\), \(p\ne\tfrac12\). The argument uses scalar measure and finite-coordinate independence directly.

We begin with ZFC with countable choice, completeness of the real and complex scalars, elementary finite sums/products and set operations, and the definitions of a sigma algebra, a measurable function and countable additivity. The construction proceeds from cylinders to the completed probability measure, scalar integration, \(L^2\) approximation, and permutation invariance. The normal operator identification \(D\cong L^\infty(X,\nu)\) in the other portion of (10) is separate from this scalar function argument.

The first four subsections construct and complete the measure. Integration and cylinder density then justify the error estimate. Finite independence and the permutation action give the final constancy argument.

#### Binary cylinders and function classes

Put \(a=1-p\), \(b=p\), so \(a,b>0\) and \(a+b=1\). For a finite set \(F\subset\mathbb N\) and a binary assignment \(\alpha:F\to\{0,1\}\), write
\[
 C(F,\alpha)=\{x\in X:x_j=\alpha_j\ (j\in F)\},\qquad
 w(F,\alpha)=\prod_{j\in F}a^{1-\alpha_j}b^{\alpha_j}.
                                                               \tag{FE1}
\]
Empty products are one and \(C(\varnothing,\varnothing)=X\). A cylinder function is any complex function determined by a finite coordinate set; such a function has finite range. Let \(\mathcal A_n\) be the finite algebra of unions of the \(2^n\) first-\(n\) cylinder cells, and let \(\mathcal A=\bigcup_n\mathcal A_n\), including \(\varnothing,X\). It is an algebra, because any finite collection of its sets is contained in one \(\mathcal A_n\).

Write \(\mathcal B=\sigma(\mathcal A)\). This is the coordinate product sigma algebra: every finite-coordinate cylinder is a union of first-\(n\) cells for sufficiently large \(n\), and the first-\(n\) cells are finite intersections of coordinate inverse images. It is also the Borel sigma algebra of the usual product topology. Indeed the prefix cylinders form a countable base; every open set is a union of a subcollection of this countable base, and each cylinder is open and closed. No uncountable-product theorem is involved.

The [finite-weight construction](#finite-bernoulli-weights-and-cylinder-covers), [outer-measure extension](#outer-measure-and-countable-additivity), and [completion](#completion-uniqueness-and-set-approximation) construct the probability \(\nu_0\) on \(\mathcal B\) and its complete extension \(\nu\) on \(\overline{\mathcal B}\), with
\[
 \nu(C(F,\alpha))=w(F,\alpha),\qquad
 \nu(X)=1,\qquad
 \nu=\bigotimes_{j\ge1}(a\delta_0+b\delta_1).
                                                               \tag{FE2}
\]
The last notation means precisely the unique countably additive measure with these cylinder values, together with completion when completed function classes are used. Passing from \(\mathcal B\) to its completion changes no \(L^2\) or \(L^\infty\) equivalence class: [completion and set approximation](#completion-uniqueness-and-set-approximation) and [cylinder density and completeness](#cylinder-density-and-l-2-completeness) prove the necessary representative statement. Thus both usual readings of original (10) give the same lemma.

Let \(\Gamma\) be the group of permutations \(\pi\) of \(\mathbb N\) with finite support. We fix the explicit coordinate and function conventions
\[
 (T_\pi x)_j=x_{\pi^{-1}(j)},\qquad
 \alpha_\pi f=f\circ T_{\pi^{-1}}.
                                                               \tag{FE3}
\]
The [permutation construction](#permutations-null-classes-and-support-transport) proves that these are well-defined measure-preserving actions, also on completed equivalence classes. The target is: if \(z\in L^\infty(X,\nu)\) and \(\alpha_\pi z=z\) for every \(\pi\in\Gamma\), then \(z=c\) almost everywhere for the scalar \(c=\int_X z\,d\nu\). Pointwise invariance of a chosen representative is not assumed. Since the original invariance quantifies over every finite permutation, replacing each permutation by its inverse gives exactly the same hypothesis under the alternative coordinate convention.

#### Finite Bernoulli weights and cylinder covers

For a first-\(n\) cell with string \(\beta\in\{0,1\}^n\), set \(m(C_n(\beta))=a^{n-|\beta|}b^{|\beta|}\), and for a union of these cells sum their weights. Refinement from level \(n\) to \(n+1\) is consistent, since
\[
 a^{n-|\beta|}b^{|\beta|}
 =a^{n-|\beta|+1}b^{|\beta|}
  +a^{n-|\beta|}b^{|\beta|+1}.
                                                               \tag{FE4}
\]
Thus \(m\) is defined independently of the level on all of \(\mathcal A\). Its finite partition formula proves nonnegativity, finite additivity, monotonicity and \(m(X)=(a+b)^n=1\). In particular \(m(A\cup B)\le m(A)+m(B)\). Refining a finite-coordinate cylinder to a head partition and summing the unspecified binary digits proves \(m(C(F,\alpha))=w(F,\alpha)\), because each missing digit contributes \(a+b=1\).

We prove the finite-cover property needed for countable additivity and outer measure, rather than invoking compactness. Suppose \(A\in\mathcal A\) is covered by a family of sets from \(\mathcal A\) but no finite subfamily covers it. Choose a head level expressing \(A\) as finitely many prefix cells. One of these cells has no finite subcover; otherwise the finitely many finite subcovers combine. Split that cell into its two children. Again one child has no finite subcover. Recursion gives nested prefix cells of lengths tending to infinity, each with no finite subcover. Their compatible digits define a single \(x\in A\). Some member \(B\) of the given cover contains \(x\). Since \(B\) is a union of cells at one finite level, the prefix cell of \(x\) at every sufficiently large level is contained in \(B\). A cell in the recursive family is then covered by this one member, a contradiction. This proves the finite-cover property for every such cover of \(A\).

Consequently, whenever \(A\subseteq\bigcup_{k\ge1}A_k\) with \(A,A_k\in\mathcal A\), a finite subcover and finite additivity give
\[
 m(A)\le\sum_{k\ge1}m(A_k).                               \tag{FE5}
\]
If the \(A_k\) are disjoint and their union itself belongs to \(\mathcal A\), a finite subcover covers that union. Every other \(A_k\) must then be empty, by disjointness. The finite additivity formula therefore proves countable additivity on exactly those unions required of a premeasure. No product-measure existence or general compactness theorem is hidden in this step.

#### Outer measure and countable additivity

For every subset \(E\subseteq X\), define
\[
 \nu^*(E)=
 \inf\left\{\sum_{k\ge1}m(A_k):
       A_k\in\mathcal A,\ E\subseteq\bigcup_{k\ge1}A_k\right\}.
                                                               \tag{FE6}
\]
There is always a cover, using \(X\), so \(0\le\nu^*(E)\le1\). The empty set has value zero and the definition gives monotonicity. For countable subadditivity, the assertion is immediate if \(\sum_j\nu^*(E_j)=\infty\). Otherwise, for a prescribed \(\varepsilon>0\), choose for each \(j\ge1\) a cylinder-algebra cover of \(E_j\) with total weight less than \(\nu^*(E_j)+\varepsilon2^{-j}\). Their countable union is a cover of \(\bigcup_jE_j\). Infimizing and then letting \(\varepsilon\downarrow0\) gives
\[
 \nu^*\!\left(\bigcup_jE_j\right)\le\sum_j\nu^*(E_j).
                                                               \tag{FE7}
\]
For \(A\in\mathcal A\), the one-set cover gives \(\nu^*(A)\le m(A)\); (FE5) applied to every countable cover gives the reverse inequality. Hence \(\nu^*|_{\mathcal A}=m\).

Call \(E\) measurable for this outer measure if, for every subset \(T\subseteq X\),
\[
 \nu^*(T)=\nu^*(T\cap E)+\nu^*(T\setminus E).              \tag{FE8}
\]
Let \(\mathcal C\) be the collection of these sets. Every \(A\in\mathcal A\) satisfies (FE8): split each member \(A_k\) of any cover of \(T\) into \(A_k\cap A\) and \(A_k\setminus A\). Both parts are in \(\mathcal A\), with weights summing to \(m(A_k)\). Thus the right side of (FE8) is at most the cost of any cover of \(T\), hence at most \(\nu^*(T)\); subadditivity gives the opposite inequality.

We supply the whole sigma-algebra and measure argument. The empty set belongs to \(\mathcal C\), and complements preserve (FE8). If \(E,F\in\mathcal C\), successively split \(T\) by \(E\), and then its two parts by \(F\). The resulting four-term equality implies the test for \(E\cup F\): the sum of the first three terms is at least \(\nu^*(T\cap(E\cup F))\) by subadditivity, while the fourth is \(\nu^*(T\setminus(E\cup F))\). This supplies the lower bound in (FE8); its upper bound always follows from subadditivity. Thus \(\mathcal C\) is an algebra.

For disjoint \(E_j\in\mathcal C\), write \(E=\bigcup_{j\ge1}E_j\). Repeated finite splitting gives, for every \(n\),
\[
 \nu^*(T)=\sum_{j=1}^n\nu^*(T\cap E_j)
       +\nu^*\!\left(T\setminus\bigcup_{j=1}^nE_j\right)
 \ge\sum_{j=1}^n\nu^*(T\cap E_j)+\nu^*(T\setminus E).
                                                               \tag{FE9}
\]
Let \(n\to\infty\). Subadditivity bounds \(\nu^*(T\cap E)\) by the resulting sum. This proves the lower bound in (FE8) for \(E\), and the opposite bound is automatic. Therefore \(E\in\mathcal C\). An arbitrary countable union can be replaced by the disjoint sets \(E_1,E_2\setminus E_1,\ldots\), using the algebra operations just proved. Hence \(\mathcal C\) is a sigma algebra containing \(\mathcal B\).

For disjoint measurable \(E_j\), take \(T=E\) in the finite splitting equality. It gives \(\nu^*(E)\ge\sum_{j\le n}\nu^*(E_j)\). Let \(n\to\infty\) and combine with (FE7). Thus
\[
 \nu^*\!\left(\bigsqcup_jE_j\right)=\sum_j\nu^*(E_j)
 \quad(E_j\in\mathcal C),\qquad \nu^*(X)=1.               \tag{FE10}
\]
The restriction to \(\mathcal C\), and in particular to \(\mathcal B\), is a countably additive probability. If \(\nu^*(Z)=0\), every subset of \(Z\) has outer measure zero. For such a subset the right side of (FE8) is at most \(\nu^*(T)\) by monotonicity, and at least it by subadditivity. It is measurable. The measure on \(\mathcal C\) is therefore complete.

#### Completion, uniqueness and set approximation

Write \(\nu=\nu^*|_{\mathcal C}\) provisionally. Countable additivity implies the elementary continuity statements used here. If \(E_n\uparrow E\), write \(E=E_1\sqcup\bigsqcup_{n\ge2}(E_n\setminus E_{n-1})\). The partial sums are \(\nu(E_n)\), so \(\nu(E_n)\uparrow\nu(E)\). If \(E_n\downarrow E\), take complements in the finite measure \(X\), obtaining \(\nu(E_n)\downarrow\nu(E)\). These proofs apply throughout \(\mathcal C\).

We identify \(\mathcal C\) exactly with the completion of \(\mathcal B\). For \(E\in\mathcal C\), choose for every \(n\) a cylinder-algebra cover of total weight less than \(\nu^*(E)+2^{-n}\), and let \(U_n\in\mathcal B\) be its union. Then \(E\subseteq U_n\) and countable subadditivity plus measurable subtraction give
\[
 \nu(U_n\setminus E)=\nu(U_n)-\nu(E)<2^{-n}.
                                                               \tag{FE11}
\]
Let \(B=\bigcap_nU_n\in\mathcal B\). Then \(E\subseteq B\) and \(\nu^*(B\setminus E)=0\). Every outer-null set \(Z\) is contained in a Borel null set: choose covers with total weights less than \(2^{-n}\), take the union of each cover and then their intersection. The resulting Borel set contains \(Z\) and has measure at most \(2^{-n}\) for every \(n\). Hence \(E\) differs from \(B\) by a subset of a Borel null set. Conversely every such completed set belongs to \(\mathcal C\), since Borel sets and all subsets of null sets belong to it. This proves \(\mathcal C=\overline{\mathcal B}\), and we now write \(\nu=\nu^*|_{\overline{\mathcal B}}\).

For uniqueness on \(\mathcal B\), let \(\lambda\) be any probability agreeing with \(m\) on \(\mathcal A\). For \(B\in\mathcal B\), each cover in (FE6) gives \(\lambda(B)\le\sum_km(A_k)\), so \(\lambda(B)\le\nu_0(B)\). Apply this to \(X\setminus B\), and use both probabilities' value one on \(X\), to obtain the reverse inequality. Thus \(\lambda=\nu_0\). Its complete extension is also unique, because a completed set differs from a Borel set by a subset of a Borel null set, which every complete extension measures zero. This proves the product measure assertion (FE2), without invoking an extension, uniqueness or infinite-product theorem.

For every \(E\in\overline{\mathcal B}\) and \(\delta>0\), choose a cover with union \(U\) and total cost less than \(\nu(E)+\delta/2\). Then \(\nu(U\setminus E)<\delta/2\). Let \(A_N\) be the union of its first \(N\) members, so \(A_N\in\mathcal A\) and \(A_N\uparrow U\). By the continuity already proved, some \(N\) has \(\nu(U\setminus A_N)<\delta/2\). Consequently
\[
 \boxed{\quad \text{for every }E\in\overline{\mathcal B},\ \delta>0,\
       \text{some }A\in\mathcal A\text{ satisfies }
       \nu(E\mathbin{\triangle}A)<\delta.\quad}           \tag{FE12}
\]
This is a complete set-approximation theorem for the completed measure. No monotone-class or density theorem is assumed.

#### Scalar integration and square norms

For a complex simple function \(s=\sum_{\ell=1}^r c_\ell1_{E_\ell}\) on a finite measurable partition of \(X\), define
\[
 I(s)=\sum_{\ell=1}^r c_\ell\nu(E_\ell),\qquad
 |I(s)|\le\sup_X|s|,\qquad I(1)=1.                       \tag{FE13}
\]
Common finite refinement shows independence of the representation, complex linearity and positivity. It also gives \(|I(s)-I(t)|\le\sup_X|s-t|\) for simple \(s,t\). A bounded measurable real function admits uniform simple approximations by subdividing its bounded range into intervals of length \(2^{-n}\); for a complex function apply this to its real and imaginary parts. Such approximations are measurable because their finitely many level sets are measurable. Completeness of the complex scalars makes \(I(s_n)\) converge, and the preceding estimate makes the limit independent of the approximating sequence. This defines \(I(f)\) for all bounded measurable complex \(f\), with positivity, linearity and the uniform estimate retained.

For a nonnegative measurable \(u\), possibly taking \(+\infty\), define \(I(u)\) to be the supremum of \(I(s)\) over nonnegative simple \(s\le u\). For bounded nonnegative \(u\) this equals its preceding uniform integral, by lower dyadic simple approximation. We prove monotone convergence directly. If \(u_n\uparrow u\), monotonicity gives \(\sup_nI(u_n)\le I(u)\). Fix a nonnegative simple \(s\le u\) and \(0<c<1\). The measurable sets \(F_n=\{u_n\ge cs\}\) increase and exhaust each cell where \(s\) has positive value. The continuity of measure from [completion and set approximation](#completion-uniqueness-and-set-approximation) therefore gives \(I(s1_{F_n})\to I(s)\). Since \(u_n\ge cs1_{F_n}\),
\[
 \sup_n I(u_n)\ge c I(s).
 \quad\text{Thus } I(u_n)\uparrow I(u)
       \text{ after }c\uparrow1\text{ and the supremum over }s.
                                                               \tag{FE14}
\]
Zero-valued cells do not affect this argument.

The explicit bounded simple functions
\[
 q_n(u)=2^{-n}\left\lfloor 2^n\min(u,n)\right\rfloor
 \uparrow u,\qquad q_n(+\infty)=n                         \tag{FE15}
\]
are increasing: finer binary subdivision increases the lower approximation, and increasing the cutoff cannot decrease it. Applying (FE14) to \(q_n(u)+q_n(v)\) proves \(I(u+v)=I(u)+I(v)\) for nonnegative functions; their finite simple integrals are already additive. The same lower-approximation argument proves positive homogeneity. These formulas hold with nonnegative infinite values. If \(u_n\ge0\), then \(v_n=\inf_{k\ge n}u_k\uparrow\liminf_ku_k\) is measurable, and \(I(v_n)\le\inf_{k\ge n}I(u_k)\). Monotone convergence proves
\[
 I(\liminf_nu_n)\le\liminf_nI(u_n).                       \tag{FE16}
\]
Measurability of countable suprema and infima follows from their threshold sets being countable unions or intersections.

For real \(f\) with \(I(|f|)<\infty\), put \(I(f)=I(f^+)-I(f^-)\); integrate complex functions by real and imaginary parts. Additivity for integrable real functions follows by integrating the pointwise identity
\[
 (f+g)^+ +f^-+g^-=(f+g)^-+f^++g^+.
\]
All its terms are integrable because \(|f+g|\le|f|+|g|\); nonnegative additivity was proved above. Homogeneity and complex linearity follow as well. Rotating the value of \(I(f)\) by a unit scalar and using \(\operatorname{Re}(\zeta f)\le|f|\) proves \(|I(f)|\le I(|f|)\). We henceforth use the ordinary notation \(\int f\,d\nu=I(f)\).

Every finite-\(L^2\)-norm function is finite almost everywhere: if \(I(|u|^2)<\infty\), the set where \(|u|=+\infty\) has measure at most \(I(|u|^2)/R^2\) for every \(R>0\). It has measure zero. For complex measurable \(u,v\) with finite square integrals, the scalar inequality
\[
 |uv|\le \frac{t|u|^2+t^{-1}|v|^2}{2}\quad(t>0)           \tag{FE17}
\]
shows that \(uv\) is integrable. Infimizing its integrated bound in \(t\) gives
\[
 \left|\int\overline u v\,d\nu\right|
 \le\int|uv|\,d\nu
 \le\left(\int|u|^2\,d\nu\right)^{1/2}
       \left(\int|v|^2\,d\nu\right)^{1/2}.                \tag{FE18}
\]
When one squared norm is zero, let \(t\to0\) or \(t\to\infty\) in the finite bound; thus no division by zero is used. Taking \(v=1\) also proves integrability of every \(L^2\) function. Expanding \(|u+v|^2\), using the now justified complex integral and (FE18), proves the triangle inequality
\[
 \|u+v\|_2\le\|u\|_2+\|v\|_2,\qquad
 \|u\|_2=\left(\int|u|^2\,d\nu\right)^{1/2}.              \tag{FE19}
\]
Linearity of the measurable operations used here is literal pointwise arithmetic. Their measurability follows from continuity of scalar arithmetic and the countable rectangular bases in finite-dimensional real or complex scalar spaces: an inverse image of an open set is a countable union of measurable coordinate inverse images. For a convergent sequence of measurable real functions, the threshold set \(\{\lim_n u_n<r\}\) is, on its convergence set,
\[
 \bigcup_{\substack{q\in\mathbb Q\\q<r}}\ 
 \bigcup_{N\ge1}\ \bigcap_{n\ge N}\{u_n<q\}.
\]
Indeed a limit below \(r\) admits a rational \(q\) strictly between the limit and \(r\), whereas eventual values below \(q<r\) force the limit to be at most \(q<r\). The set of convergence of a real or complex scalar sequence is itself measurable by completeness and the Cauchy formula
\[
 \bigcap_{k\ge1}\ \bigcup_{N\ge1}\
       \bigcap_{m,n\ge N}\{|u_m-u_n|<1/k\}.
\]
These formulas prove measurability of pointwise scalar limits, extended by zero off their convergence sets.

If \(\|u\|_2=0\), then
\[
 \nu\{|u|\ge1/k\}\le k^2\int|u|^2\,d\nu=0
 \quad(k\ge1),\qquad u=0\text{ almost everywhere}.        \tag{FE20}
\]
Conversely a function zero outside a null set has zero nonnegative integral: every nonnegative simple function below it has nonzero cells only inside a null set. All these integrals and norms therefore depend only on almost-everywhere classes. This justifies the function spaces used here, without importing a general Lebesgue integral or Hilbert-space theorem. An essentially bounded measurable function has a bounded representative by changing its values to zero on the null set where a fixed essential bound fails.

#### Cylinder density and \(L^2\) completeness

First let \(u\) be bounded measurable. Uniform simple approximation from [scalar integration and norms](#scalar-integration-and-square-norms) gives \(s=\sum_{\ell=1}^r c_\ell1_{E_\ell}\) with \(\|u-s\|_2\) as small as desired, because the probability is one. For each \(E_\ell\), (FE12) gives a cylinder-algebra set \(A_\ell\) with any prescribed small symmetric-difference measure. The function \(h=\sum_\ell c_\ell1_{A_\ell}\) depends on finitely many coordinates. Formula (FE19) gives the exact approximation estimate
\[
 \|s-h\|_2
 \le\sum_{\ell=1}^r |c_\ell|\,
            \nu(E_\ell\mathbin{\triangle}A_\ell)^{1/2}.  \tag{FE21}
\]
For example, if \(L=\sum_\ell|c_\ell|>0\), making each symmetric-difference measure less than \((\varepsilon/L)^2\) makes the right side less than \(\varepsilon\). If \(L=0\), use \(h=0\). Thus cylinder functions are dense for every bounded measurable function, including every \(L^\infty\) class.

For arbitrary \(u\in L^2\), let \(u_R=u1_{\{|u|\le R\}}\), after the harmless null change making \(u\) finite everywhere. By (FE14) the integrals of \(|u|^2 1_{\{|u|\le R\}}\) tend to \(\int|u|^2\). Nonnegative additivity and finiteness give
\[
 \|u-u_R\|_2^2
 =\int |u|^2 1_{\{|u|>R\}}\,d\nu\longrightarrow0.
                                                               \tag{FE22}
\]
Each \(u_R\) is bounded and hence approximable as above. This proves the full density assertion
\[
 \overline{\{\text{complex cylinder functions}\}}^{\|\cdot\|_2}
       =L^2(X,\nu).                                     \tag{FE23}
\]
No martingale convergence theorem, conditional expectation or operator diagonal density is used.

We justify that completion has introduced no new equivalence classes. Every set in \(\overline{\mathcal B}\) differs from a Borel set by a subset of a Borel null set, by [completion and set approximation](#completion-uniqueness-and-set-approximation). For each real part \(r\) of a completed-measurable function, use the signed simple approximations \(q_n(r^+)-q_n(r^-)\); apply the same construction to its imaginary part. They converge to the given finite scalar function, and each has finitely many measurable cells. Replace these cells by Borel representatives modulo null sets. The resulting Borel simple functions agree with the original approximations off one common Borel null set, obtained as the countable union of the null carriers of their symmetric differences. Their pointwise scalar limits, set to zero on that carrier and on the Borel set where the limit does not exist, are Borel and agree almost everywhere with the original function. The set of convergence is Borel by the full scalar Cauchy formula in [scalar integration and norms](#scalar-integration-and-square-norms). This proves the representative assertion for \(L^2\) and \(L^\infty\), and their integrals and norms agree by [scalar integration and norms](#scalar-integration-and-square-norms).

For completeness, the whole \(L^2\) space is complete at this measure boundary. Given a Cauchy sequence, choose a subsequence \(v_k\) with \(\|v_{k+1}-v_k\|_2\le2^{-k}\). Choose finite measurable representatives off a single common null set. Put \(d_k=|v_{k+1}-v_k|\). The triangle inequality for every finite sum and (FE14) for its square give
\[
 S_N=\sum_{k\ge N}d_k,\qquad
 \|S_N\|_2\le\sum_{k\ge N}2^{-k}=2^{1-N}.                 \tag{FE24}
\]
In particular \(S_1\) is finite almost everywhere, by the finite-integral argument of [scalar integration and norms](#scalar-integration-and-square-norms). Outside that null set the series of scalar differences is absolutely convergent, so completeness of the complex numbers defines a limit \(v\). Give it value zero on the null set. It is measurable by the pointwise-limit threshold criterion. The telescoping bound \(|v-v_N|\le S_N\) gives
\[
 \|v-v_N\|_2\le2^{1-N},\qquad
 \|v\|_2\le\|v_1\|_2+\|S_1\|_2<\infty.                  \tag{FE25}
\]
Finally the original Cauchy sequence converges to the same \(v\), by its Cauchy property and the triangle inequality with a sufficiently late subsequence member. Thus all \(L^2\) density and limiting language used by original Lemma3.1 has full scalar measure support.

#### Independence on disjoint finite coordinates

The cylinder value (FE1) gives the law \(a\delta_0+b\delta_1\) in every coordinate. For disjoint finite sets \(F,G\), their two specified cylinders satisfy
\[
 \nu(C(F,\alpha)\cap C(G,\beta))
       =w(F,\alpha)w(G,\beta).                           \tag{FE26}
\]
Thus the coordinates are independent in the precise finite-dimensional sense. The same proof handles finitely many disjoint finite coordinate sets. This, together with uniqueness in [completion and set approximation](#completion-uniqueness-and-set-approximation), is the identical Bernoulli product in original (10); no independent-law assertion is assumed.

If \(g\) depends on \(F\) and \(f\) depends on \(G\), expand them as finite sums over their binary assignments. When \(F\cap G=\varnothing\), (FE26) gives
\[
 \begin{aligned}
 \int gf\,d\nu
 &=\sum_{\alpha,\beta}g_\alpha f_\beta
                      w(F,\alpha)w(G,\beta)\\
 &=\left(\sum_\alpha g_\alpha w(F,\alpha)\right)
   \left(\sum_\beta f_\beta w(G,\beta)\right)
 =\left(\int g\,d\nu\right)\left(\int f\,d\nu\right).
 \end{aligned}                                          \tag{FE27}
\]
This proves independence in exactly the complex-valued form consumed by the original proof. It requires neither general Fubini nor independence of an infinite tail sigma algebra.

#### Permutations, null classes and support transport

The maps in (FE3) are bijections, with inverses \(T_{\pi^{-1}}\). Direct substitution gives \(T_\pi T_\sigma=T_{\pi\sigma}\), and therefore \(\alpha_\pi\alpha_\sigma=\alpha_{\pi\sigma}\). The image of \(C(F,\alpha)\) is the cylinder on \(\pi(F)\) with corresponding permuted assignment. Its weight is unchanged, since all coordinates have the same \(a,b\). Consequently \(T_\pi\) and its inverse map \(\mathcal A\) onto itself and preserve \(m\).

Transport every countable cylinder cover in (FE6) by this bijection. The costs are unchanged, and apply the inverse for the opposite inequality. Thus, even for an arbitrary subset of \(X\),
\[
 \nu^*(T_\pi E)=\nu^*(E).                                \tag{FE28}
\]
Transporting the test (FE8) shows that \(T_\pi\) maps \(\mathcal C=\overline{\mathcal B}\) onto itself. Formula (FE28) then proves measure preservation on the whole completed space, including preservation of all null sets. This directly proves measurable invertibility and completed measure preservation; it does not merely check cylinders and assume an extension.

Composition with \(T_{\pi^{-1}}\) preserves measurability. For simple functions it preserves the integral by their cell measures; for nonnegative functions it does so either by transporting the defining simple minorants in both directions, or by (FE14). Real/imaginary decomposition gives the same for integrable complex functions. Hence
\[
 \int\alpha_\pi f\,d\nu=\int f\,d\nu,\qquad
 \|\alpha_\pi f\|_2=\|f\|_2,\qquad
 \|\alpha_\pi f\|_\infty=\|f\|_\infty.                   \tag{FE29}
\]
The last equality follows by transporting the sets where any proposed essential bound fails. Null preservation makes these maps well-defined on equivalence classes. A cylinder function supported on \(F\) is sent to one supported on \(\pi(F)\), as is seen from \((T_{\pi^{-1}}x)_j=x_{\pi(j)}\).

Invariance in \(L^\infty\) means equality almost everywhere for each \(\pi\), which is enough for every integral calculation below. It can also be represented pointwise if desired, without strengthening the hypothesis. The group \(\Gamma\) is countable, being the union of the finite permutation groups on \(\{1,\ldots,n\}\). Choose a bounded measurable representative \(z\), and let \(E_\pi\) be the null set where \(z(T_{\pi^{-1}}x)\ne z(x)\). The set
\[
 B=\bigcup_{\sigma,\pi\in\Gamma}T_\sigma E_\pi             \tag{FE30}
\]
is a measurable null set, invariant under every \(T_\sigma\). On \(X\setminus B\), the representative satisfies all the invariance equations simultaneously; giving it value zero on \(B\) makes it pointwise invariant everywhere. This optional representative construction will only be used to compare the almost-everywhere hypothesis with the pointwise formulation in the human source, not to replace the original domain.

Finally, for finite coordinate sets \(F,G\), choose a set \(H\) of \(|F|\) new coordinates disjoint from \(F\cup G\). Pair its elements bijectively with those of \(F\), and swap each pair. Their disjoint transpositions form a finite permutation \(\pi\) with
\[
 \pi(F)=H,\qquad H\cap G=\varnothing.                    \tag{FE31}
\]
There are always enough coordinates because \(\mathbb N\) is infinite; if \(F\) is empty use the identity. This supplies the exact disjoint-support move required in the proof.

#### The human comparison and the operator boundary

Sourav Chatterjee's [*Stats 310A (Math 230A) Lecture notes*](https://souravchatterjee.su.domains/stat310a-lecture-notes.pdf), Theorem 6.5.1 and its full proof on printed pages 60–61/PDF pages 64–65, give a real-valued invariant-function theorem using displacement of finite coordinate sets. Corollary 6.5.4 and its proof on printed page 62/PDF page 66 specialize it to finite permutations, the Hewitt–Savage zero-one law. The cited file is an undated 115-page author-hosted PDF.

The human proof invokes Exercises 5.1.3 and 5.1.4 for finite-coordinate approximation and representation; its final real threshold inference is brief. Those source exercises are not premises here. The construction from [finite weights](#finite-bernoulli-weights-and-cylinder-covers) through [cylinder density and completeness](#cylinder-density-and-l-2-completeness) gives the full product construction, completion, scalar integral and approximation at the binary scope. The [independence](#independence-on-disjoint-finite-coordinates) and [permutation](#permutations-null-classes-and-support-transport) arguments, followed by [Lemma 3.1](#lemma-3-1), give complex finite independence, the completed almost-everywhere permutation action, and the full complex conclusion. The human theorem serves as a comparison of methods; every measure prerequisite used in this proof has been proved above.

We retain \(0<p<1\), \(p\ne\tfrac12\). Some function arguments extend further, but no endpoint, half-state or nonidentical-product conclusion is asserted here. Countability is used in the cylinder algebra, countable covers, completed representatives and finite permutation group. Infinitely many coordinates are needed to move supports away from a given finite approximation, so no finite-product ergodicity claim follows.

Equation (10) has two distinct parts: the Bernoulli probability and scalar function space constructed above, and the normal identification of the multiplication algebra with the occupation diagonal \(D\). The latter is not a premise of Lemma 3.1. Equality of cylinder moments alone does not close that identification. An application to \(D\) can use the separate operator argument or a complete normal identification; the scalar proof above uses neither as a substitute for its function statement.

All measure, integration, density and permutation prerequisites used in Lemma 3.1 are supplied at the stated scalar set-theoretic boundary. General products with arbitrary alphabets or index sets, normal multiplication-algebra or CAR transport, operator factoriality and type, subtype, crossed products, core and flow require their own arguments.

The measure and function-space construction now supports the proof of Lemma 3.1 by averages of disjoint coordinate copies.

**Lemma 3.1.** Every \(z\in L^\infty(X,\nu)\) invariant under all finite coordinate permutations is constant almost everywhere.

**Proof.**

Use the action already constructed on completed equivalence classes in [the completed permutation action](#permutations-null-classes-and-support-transport):
\[
 (T_\pi x)_j=x_{\pi^{-1}(j)},\qquad
 \alpha_\pi f=f\circ T_{\pi^{-1}}.
                                                        \tag{AV1}
\]
For every finite permutation \(\pi\), it preserves the completed measure, complex integrals, and \(L^2\) norms. It respects pointwise multiplication on representatives and hence almost-everywhere multiplication on equivalence classes. If \(f\) depends on the finite coordinate set \(F\), then \(\alpha_\pi f\) depends on \(\pi(F)\). Invariance of \(z\) means \(\alpha_\pi z=z\) as an equivalence class, not that a chosen representative is invariant at every point.

Fix any complex cylinder function \(f\), and put
\[
 c_f=\int_X f\,d\nu,\qquad v_f=\|f-c_f\|_2^2.
                                                        \tag{AV2}
\]
It has finite range, so all these quantities are finite. If \(F=\varnothing\), then \(f=c_f\) is constant, and the factorization \(\int zf=(\int z)c_f\) is immediate. Suppose now that \(m=|F|>0\). There are pairwise disjoint sets \(H_1,H_2,\ldots\subset\mathbb N\setminus F\), each of size \(m\): list \(\mathbb N\setminus F\) in increasing order and divide the list into successive blocks of size \(m\). For each \(k\), pair the increasing lists of \(F\) and \(H_k\), and swap the paired coordinates. These \(m\) disjoint transpositions define a finite permutation \(\pi_k\) satisfying \(\pi_k(F)=H_k\). Put
\[
 f_k=\alpha_{\pi_k}f,\qquad h_k=f_k-c_f.
                                                        \tag{AV3}
\]
Each \(h_k\) depends only on \(H_k\). The action gives
\[
 \int h_k\,d\nu=0,\qquad \|h_k\|_2^2=v_f.
                                                        \tag{AV4}
\]
Only these finite-support permutations are used. No single permutation moving infinitely many coordinates has been introduced.

**Variance of the finite average.**

For \(j\ne k\), the complex finite-coordinate independence proved in [finite-coordinate independence](#independence-on-disjoint-finite-coordinates) applies to \(h_j\) and \(\overline{h_k}\), whose supports are disjoint. Since conjugation commutes with the integral of an integrable complex function (by the real/imaginary definition in [scalar integration and square norms](#scalar-integration-and-square-norms)),
\[
 \int h_j\overline{h_k}\,d\nu
   =\left(\int h_j\,d\nu\right)
      \overline{\left(\int h_k\,d\nu\right)}=0.
                                                        \tag{AV5}
\]
For \(N\ge1\), form the finite average
\[
 A_N=\frac1N\sum_{k=1}^N f_k.
                                                        \tag{AV6}
\]
Expanding its squared norm, using the finite linearity of the integral, (AV4), and (AV5), gives the complete estimate
\[
 \begin{aligned}
 \|A_N-c_f\|_2^2
 &=\frac1{N^2}\sum_{j,k=1}^N
              \int h_j\overline{h_k}\,d\nu\\
 &=\frac1{N^2}\sum_{k=1}^N v_f
   =\frac{v_f}{N}.
 \end{aligned}                                          \tag{AV7}
\]
Thus \(A_N\to c_f\) in \(L^2\), with exact rate \(\|f-c_f\|_2/\sqrt N\). This includes \(v_f=0\), without division by \(v_f\), and requires no pointwise or almost-sure convergence theorem.

**Invariant integrals and scalar factorization.**

Because \(z\) is essentially bounded on a probability space, it has a bounded measurable representative by [scalar integration and square norms](#scalar-integration-and-square-norms), belongs to \(L^2\), and has a finite complex integral. Every product below is integrable. Measure preservation, multiplicativity of the action, and the assumed class invariance give, for every \(k\),
\[
 \int zf\,d\nu
   =\int\alpha_{\pi_k}(zf)\,d\nu
   =\int zf_k\,d\nu.
                                                        \tag{AV8}
\]
The last equality remains valid when the invariance fails on a null set of a chosen representative, since the integral depends only on equivalence classes. Averaging these \(N\) equalities yields
\[
 \int zf\,d\nu=\int zA_N\,d\nu.
                                                        \tag{AV9}
\]
Apply the complex Cauchy–Schwarz inequality FE18 to \(\overline z\) and \(A_N-c_f\); this choice of first argument produces the bilinear product \(z(A_N-c_f)\). Using (AV7) gives
\[
 \begin{aligned}
 \left|\int zf\,d\nu
       -\left(\int z\,d\nu\right)c_f\right|
 &=\left|\int z(A_N-c_f)\,d\nu\right|\\
 &\le \|z\|_2\,\|A_N-c_f\|_2
   =\frac{\|z\|_2\,\|f-c_f\|_2}{\sqrt N}.
 \end{aligned}                                          \tag{AV10}
\]
The left side is independent of \(N\). Letting \(N\to\infty\) proves, including the previously separated constant-cylinder case,
\[
 \int zf\,d\nu
   =\left(\int z\,d\nu\right)\left(\int f\,d\nu\right)
 \quad\text{for every complex cylinder }f.
                                                        \tag{AV11}
\]
The invariant function has not been approximated to obtain this identity. The approximation is of a test function's disjoint copies to its scalar mean.

**The complex and almost-everywhere conclusion.**

Put \(c_z=\int z\,d\nu\) and \(w=z-c_z\). Both are well-defined, and \(w\in L^2\). By (AV11), \(\int wf\,d\nu=0\) for every complex cylinder \(f\). [Cylinder density and completeness](#cylinder-density-and-l-2-completeness) supplies complex cylinder functions \(g_n\) with \(\|w-g_n\|_2\to0\). Their conjugates are also cylinder functions, so \(\int w\overline{g_n}\,d\nu=0\). Subtract this equality from the squared norm and use FE18:
\[
 \begin{aligned}
 \|w\|_2^2
 &=\left|\int w\overline{(w-g_n)}\,d\nu\right|\\
 &\le\|w\|_2\,\|w-g_n\|_2\longrightarrow0.
 \end{aligned}                                          \tag{AV12}
\]
The integral inside the modulus equals the nonnegative real number \(\|w\|_2^2\), which justifies the first equality. We conclude \(\|w\|_2=0\). To spell out the null conclusion, FE20 gives
\[
 \nu\{|w|\ge1/r\}\le r^2\int|w|^2\,d\nu=0
 \quad(r\in\mathbb N,\ r\ge1).
                                                        \tag{AV13}
\]
Their countable union is \(\{w\ne0\}\), so countable subadditivity makes it null. Therefore
\[
 \boxed{z=\int_X z\,d\nu\quad\text{almost everywhere}.}
                                                        \tag{AV14}
\]
This is exactly the original complex function statement at its original completed probability-space boundary. \(\square\)

### Diffuseness and the finite-factor alternative

The diffuseness calculation can likewise be carried out with projections. Put \(q=\max(p,1-p)<1\). Every minimal diagonal projection in \(D_n\) has state value at most \(q^n\). If a nonzero projection \(e\) were minimal in \(D\), the finite diagonal partition would decompose it into projections under \(e\); exactly one piece would be nonzero and would equal \(e\). Hence \(\phi(e)\le q^n\) for every \(n\), contradicting faithfulness. Thus \(D\) has no minimal projection.

The trace assertion before Lemma 3.1 follows from finite densities and Lemma 2.1. Bounded strong* convergence of both factors implies strong convergence of their products: for example,
\[
\|(x_ny_n-xy)\xi\|
\le\|x_n\|\,\|(y_n-y)\xi\|+\|(x_n-x)y\xi\|.
\]
Apply this to \(x_n=E_n(x)\), \(y_n=E_n(y)\) in the finite fixed algebras, and evaluate at \(\Omega\). It passes the finite trace identity to \(N\). An isometry \(v\in N\) then has \(\phi(1-vv^*)=0\), so \(vv^*=1\); thus \(N\) is finite.

The finite-factor alternative used below has the concrete proof supplied in Section 8. If \(e\) is a minimal projection, positive-part calculus shows that every selfadjoint element of \(eNe\) is scalar: two distinct spectral levels would give a proper nonzero projection under \(e\). Thus \(eNe=\mathbb Ce\). Factor contact gives a nonzero element from \(e\) to any nonzero remaining projection; its polar decomposition copies \(e\) into that remainder. Each such orthogonal copy has the same positive trace \(\phi(e)\). The bound \(k\phi(e)\le1\) forces a largest finite family, whose sum is one, since a nonzero remainder would admit another copy. The associated partial isometries give full matrix units. Each matrix corner is one-dimensional because \(eNe\) is scalar, so they span \(N\). This proves that a finite factor with a minimal projection is a finite matrix algebra. An abelian subalgebra of a finite-dimensional matrix algebra has minimal projections, contradicting diffuseness of \(D\). The comparison in [Anantharaman and Popa, Proposition 2.4.13 and Corollary 2.4.14](https://idpoisson.fr/anantharaman/publications/IIun.pdf), printed pp.39–40/PDF pp.45–46, agrees with this alternative; its statement is not substituted for the projection proof in Section 8.

**Theorem 3.2.** \(N\) is a type \(\mathrm{II}_1\) factor.

**Proof.** If \(z\in Z(N)\), Lemma 2.2 puts it in \(D\), and commuting with the \(v_\pi\) makes it permutation invariant. Choose a local diagonal \(g\) with \(\|z-g\|_{2,\phi}<\varepsilon\). For any local diagonal \(f\), move its support disjointly from that of \(g\). Permutation invariance and finite tensor independence give
\[
 |\phi(zf)-\phi(z)\phi(f)|
 \le\varepsilon(\|f\|_{2,\phi}+|\phi(f)|).
\]
After \(\varepsilon\to0\), test adjoints of the local \(f\). Their dense orbit in \(D\Omega\) makes \((z-\phi(z)1)\Omega=0\); separation makes \(z\) scalar. This is an operator proof of factoriality, with the full scalar Lemma 3.1 retained above.

For diffuseness, a minimal nonzero projection \(e\in D\) would lie under one cell of each finite diagonal partition, since their intersections with \(e\) are projections and sum to \(e\). Thus \(\phi(e)\le\max(p,1-p)^n\) for every \(n\), contradicting faithfulness. If the tracial factor \(N\) had a minimal projection, the full projection and matrix-unit argument just given would make it finite-dimensional, contradicting this diffuse subalgebra. Therefore \(N\) is a finite factor with a faithful normal tracial state and no minimal projections, which is type \(\mathrm{II}_1\). \(\square\)

The expectations \(E_n\) also show that \(N\) is AFD: the finite-dimensional fixed algebras \(A_n^\sigma\) increase, and \(E_n(x)\in A_n^\sigma\) converges strongly* to \(x\in N\). No identification of \(N\) with a particular hyperfinite factor is needed below.

## 4. Crossing by the period circle

Because \(\sigma_P=\operatorname{id}\), the action descends to
\[
G_P=\mathbb R/P\mathbb Z.
\]
Use its regular crossed product
\[
B=M\rtimes_\sigma G_P
\]
on \(L^2([0,P),H)\), where \(H\) is the product GNS space. With addition taken modulo \(P\),
\[
\begin{aligned}
(\pi(x)f)(s)&=\sigma_{-s}(x)f(s),\\
(u(t)f)(s)&=f(s-t).
\end{aligned} \tag{12}
\]
### Normality of the concrete regular model and its average

In one Hilbert--Schmidt coordinate define \(U_t(a)=\rho^{it}a\rho^{-it}\). It is unitary and fixes \(\rho^{1/2}\). Its finite tensor action on finite-support vectors extends by the norm-one bound to the pointed completion. Strong continuity holds first on finite-support vectors and then on all vectors by density. It implements the coordinate action, and \(U_P=1\) follows on the same dense subspace from the density ratio in (4). Section 1 identifies \(U_t=\Delta_\phi^{it}\) using the complete weighted coefficient domains and the full closed graph, so this is the modular action used in the regular model.

On the circle or real regular space, the map \((Wf)(s)=U_{-s}f(s)\) is a decomposable unitary and
\[
\pi(x)=W(x\otimes1)W^*.
\]
For the real space use \(\Pi\) in place of \(\pi\). The coefficient representation is therefore faithful and normal. Translation satisfies covariance by direct substitution in (12). These facts construct the particular normal regular model used here; identifying other regular models is a separate canonical input.

The average \(\mathcal E(x)=P^{-1}\int_0^P\sigma_t(x)\,dt\) can be defined by weak Riemann integration of its continuous matrix coefficients. It belongs to \(M\), its norm is at most \(\|x\|\), and translation of the integration interval shows that its range is the fixed algebra. It fixes every fixed element. Its normality follows in predual norm. If \(\psi_{\xi,\eta}(x)=\langle\xi,x\eta\rangle\), composition with \(\sigma_t\) replaces \(\xi,\eta\) by \(U_{-t}\xi,U_{-t}\eta\). The estimate
\[
\|\psi_{\xi,\eta}-\psi_{\xi',\eta'}\|
\le\|\xi-\xi'\|\,\|\eta\|+\|\xi'\|\,\|\eta-\eta'\|
\]
makes this a norm-continuous predual curve. Its integral is a norm limit of normal finite sums. Finite sums of restricted vector functionals are norm dense in the concrete predual; the contractive bound passes the conclusion to every normal functional. Hence \(\mathcal E\) is normal. No exchange of an arbitrary increasing net with an uncountable integral is needed.

### Fourier completeness and measurable phases

The scalar Fourier input has an elementary proof. For normalized Haar measure on the circle, put
\[
K_N(\theta)=\frac1N\left|\sum_{j=0}^{N-1}e^{ij\theta}\right|^2.
\]
This nonnegative trigonometric polynomial has integral one. Outside any fixed neighborhood of zero, the geometric-series formula bounds it by \(1/(N\sin^2(\delta/2))\), so its mass there tends to zero. Translation is continuous in scalar \(L^2\): first check interval step functions, and then approximate using their density and the isometric translation bound. Minkowski's inequality and a split into a neighborhood of zero and its complement give \(K_N*f\to f\) in \(L^2\). If all Fourier coefficients of \(f\) vanish, each convolution vanishes, and hence \(f=0\). Testing a Hilbert-valued function against constant vectors, together with density of elementary scalar-vector functions, proves the Hilbert-valued version. This proves the strong sum of the orthogonal \(q_n\) and the dense range of the lattice transform in (17). Lebesgue integration, interval-step density and Hilbert completion are the underlying scalar inputs.

For \(h\in L^\infty(\mathbb T)\), the Fejér polynomials \(K_N*h\) have norm at most \(\|h\|_\infty\) and converge to \(h\) in \(L^2\). Their multiplication operators converge strongly. Indeed, on a bounded \(L^2\) test function \(f\), the error is at most \(\|f\|_\infty\|K_N*h-h\|_2\); bounded tests are dense and the operator norms are uniformly bounded. Thus the multiplication unitary \(z(\theta)=e^{i\theta}\) generates the full bounded measurable multiplication algebra. In particular the branch \(\theta\in[0,2\pi)\) puts \(e^{i\theta t/P}\) in \(W^*(z)\) for every real \(t\). This proves exactly the measurable phase removal used in (23), without requiring a continuous circle root or importing a general Borel-calculus proof.

Let \(q_n\) be the Fourier projection onto
\[
\{s\mapsto P^{-1/2}e^{in\omega s}\xi:\xi\in H\},\qquad n\in\mathbb Z.
\]
It belongs to \(B\), since it is the weak integral
\[
q_n=\frac1P\int_0^P e^{in\omega t}u(t)\,dt. \tag{13}
\]
These orthogonal projections sum strongly to one.

**Lemma 4.1.** Under the natural identification \(q_nL^2([0,P),H)\cong H\), the corner \(q_nBq_n\) is the represented algebra \(N\).

**Proof.** Define the normal periodic average
\[
\mathcal E(x)=\frac1P\int_0^P\sigma_t(x)\,dt.
\]
It has range \(N\). Directly from (12),
\[
q_n\pi(x)u(t)q_n=e^{-in\omega t}\mathcal E(x). \tag{14}
\]
Equation (14) uses the identification of \(q_nL^2([0,P),H)\) with \(H\). The algebraic linear span of \(\pi(x)u(t)\) is ultraweakly dense in \(B\): it is a unital *-algebra by covariance and contains the generators. Compression is normal. Its compressed span lies in the ultraweakly closed represented \(N\), so \(q_nBq_n\subset N\). Conversely, for \(x\in N\), \(\pi(x)\) is the constant coefficient operator and its compression is \(x\). This proves equality. \(\square\)

**Theorem 4.2.** \(B\) is a factor.

**Proof.** Let \(z\in Z(B)\). Since \(z\) commutes with every \(q_n\),
\[
z=\sum_{n\in\mathbb Z}q_nzq_n
\]
in the strong topology. The corner \(q_nzq_n\) is central in \(q_nBq_n\). Lemma 4.1 and Theorem 3.2 therefore make it \(c_nq_n\).

For the operator \(x_k\) in (6), \(\pi(x_k)\) sends Fourier degree \(m\) to degree \(m-k\), because its coefficient is \(e^{-ik\omega s}x_k\). Given any \(n,m\), choose \(k=m-n\). Then
\[
q_n\pi(x_k)q_m\ne0. \tag{15}
\]
Commuting \(z\) past this nonzero block gives \(c_n=c_m\). Thus all the scalars agree and \(z=c1\). \(\square\)

This proof uses the factorial centralizer and the existence of all integer degrees. It does not infer factorality of the compact crossed product merely from factorality of \(M\).

## 5. The lattice transform of the continuous core

Now form the continuous core
\[
C=M\rtimes_\sigma\mathbb R
\]
on \(L^2(\mathbb R,H)\), using
\[
\begin{aligned}
(\Pi(x)f)(r)&=\sigma_{-r}(x)f(r),\\
(\ell(t)f)(r)&=f(r-t).
\end{aligned} \tag{16}
\]
Every real \(r\) has a unique expression \(r=s+jP\), with \(0\le s<P\) and \(j\in\mathbb Z\). Fourier transform the lattice coordinate:
\[
(\mathcal Ff)(s,\theta)
=\sum_{j\in\mathbb Z}f(s+jP)e^{ij\theta}. \tag{17}
\]
Here \(0\le\theta<2\pi\), and the target uses \(ds\,d\theta/(2\pi)\). On finite lattice-support functions, Parseval proves that (17) is isometric; scalar Fourier completeness proves its range is dense. It therefore extends to a unitary onto \(L^2([0,P)\times[0,2\pi),H)\). The sums for general vectors mean \(L^2\) limits.

The represented coefficient is independent of \(j\), because \(\sigma_P=\operatorname{id}\). Thus \(\mathcal F\Pi(x)\mathcal F^*\) is still multiplication by \(\sigma_{-s}(x)\).

To transform a translation, write
\[
s-t=s'+kP,\qquad 0\le s'<P,\quad k\in\mathbb Z.
\]
Replacing \(j+k\) by a new lattice index gives
\[
\begin{aligned}
&(\mathcal F\ell(t)\mathcal F^*F)(s,\theta)\\
&\qquad=e^{-ik\theta}F(s',\theta).
\end{aligned} \tag{18}
\]
The factor records the lattice carry across the chosen interval.

Define the scalar gauge unitary
\[
(VF)(s,\theta)=e^{i\theta s/P}F(s,\theta).
\]
It commutes with coefficient multiplication. Since \(s-s'=t+kP\), the transformed translation satisfies
\[
\begin{aligned}
&V\mathcal F\ell(t)\mathcal F^*V^*\\
&\qquad=u(t)\otimes m_{e^{i\theta t/P}}.
\end{aligned} \tag{19}
\]
Indeed the scalar factor on the left is
\[
\begin{aligned}
&e^{i\theta s/P}e^{-ik\theta}e^{-i\theta s'/P}\\
&\qquad=e^{i\theta t/P}.
\end{aligned} \tag{20}
\]
This verifies the sign for every \(t\), including negative times and repeated interval crossings. The tensor factor \(u(t)\) is the circle translation from (12).

### Vector slices for the center and the dual convention

The center assertion in Theorem 5.1 can be proved directly in the displayed spatial tensor product. For vectors \(\eta,\eta'\) in the second Hilbert space, set \(R_\eta\xi=\xi\otimes\eta\). The slice \(R_{\eta'}^*XR_\eta\) is normal, because its matrix coefficients are matrix coefficients of \(X\). On elementary tensors in \(B\bar\otimes D\) it lies in \(B\); ultraweak density and closedness give the same membership for every \(X\) in the tensor product. The slice is bimodular over the first leg. These slices separate operators: if they all vanish, every matrix coefficient between elementary tensor vectors vanishes, and those vectors are total.

If \(X\) is central and \(B\) is a factor, each second-leg vector slice commutes with \(B\), hence is scalar. Choose a unit vector \(\xi_0\) in the first Hilbert space and form \(d=R_{\xi_0}^*XR_{\xi_0}\in D\), where this compression now slices the first leg. Every second-leg slice of \(X-1\otimes d\) vanishes: its scalar value is recovered by evaluation at \(\xi_0\). Separation therefore gives \(X=1\otimes d\). Conversely \(1\otimes D\) is central when \(D=L^\infty(\mathbb T)\). Together with Theorem 4.2 this proves the center assertion at the exact scope of (21), independently of a general tensor-commutation theorem.

On the original real regular space, \((T_af)(r)=e^{-iar}f(r)\) is unitary. Direct substitution gives
\[
T_a\Pi(x)T_a^*=\Pi(x),\qquad
T_a\ell(t)T_a^*=e^{-iat}\ell(t).
\]
Thus it defines a normal spatial automorphism of the represented core and realizes convention (24). Since \(\ell(P)\) becomes \(1\otimes z\), its center action is \(z\mapsto e^{-iaP}z\). The kernel is exactly \((2\pi/P)\mathbb Z\). This constructs the center action itself. Section 6 proves the subtype separately through the intersection of all modular spectra and then compares its parameter with this center period.

**Theorem 5.1.** Under \(V\mathcal F\),
\[
C=B\bar\otimes L^\infty(\mathbb T). \tag{21}
\]
In particular its center is \(1\otimes L^\infty(\mathbb T)\).

**Proof.** Equations (16)–(19) put all core generators in the right side of (21), so they give one inclusion. At \(t=P\), (19) gives
\[
\begin{aligned}
V\mathcal F\ell(P)\mathcal F^*V^*&=1\otimes z,\\
z(\theta)&=e^{i\theta}.
\end{aligned} \tag{22}
\]
For every bounded measurable \(h\), its Fejér polynomials have norm at most \(\|h\|_\infty\) and their multiplication operators converge strongly to \(m_h\), by the bounded-test-vector estimate proved above. They are polynomials in \(z,z^*\). Strong closedness therefore puts all of \(1\otimes L^\infty(\mathbb T)\) in the transformed \(C\).

Use the specified Borel argument \(\theta\in[0,2\pi)\) to define
\[
z^{\,t/P}(\theta)=e^{i\theta t/P}. \tag{23}
\]
For a noninteger exponent this is a bounded measurable function with a jump at the branch cut. The same bounded Fejér approximation puts its multiplication operator in the central algebra already obtained. Multiplying (19) by \(1\otimes z^{-t/P}\) puts \(u(t)\otimes1\) in \(C\). The coefficient operators \(\pi(x)\otimes1\) are there too. They generate \(B\otimes1\). Together with the central multiplication algebra they generate the right side of (21), proving the reverse inclusion.

For the center, take every second-leg vector slice of a central \(X\). Each lies in \(B\) and commutes with \(B\), so Theorem 4.2 makes it scalar. Compression by a fixed unit first-leg vector produces \(d\in L^\infty(\mathbb T)\) recovering each of these scalars. All second-leg slices of \(X-1\otimes d\) vanish, and their separating matrix coefficients give \(X=1\otimes d\). Conversely every \(1\otimes d\) is central. This is the full slice argument above at the represented tensor-product scope. \(\square\)

## 6. The dual period and the subtype

We use the dual convention
\[
\begin{aligned}
\theta_a(\Pi(x))&=\Pi(x),\\
\theta_a(\ell(t))&=e^{-iat}\ell(t).
\end{aligned} \tag{24}
\]
Equation (22) therefore gives the entire center action through its generator:
\[
\theta_a(z)=e^{-iaP}z. \tag{25}
\]
It is rotation of the central circle. Since \(z\) generates the center, the time kernel is exactly
\[
\{a:\theta_a|_{Z(C)}=\operatorname{id}\}
=\frac{2\pi}{P}\mathbb Z
=\omega\mathbb Z. \tag{26}
\]
A rotation by a nontrivial scalar changes \(z\), so no smaller positive time is in this kernel. The least positive center-flow period is consequently
\[
L=\frac{2\pi}{P}=|\log\lambda|. \tag{27}
\]

### The entire modular spectrum and the intersection over every weight

First compute the spectrum of the product modular operator from the full domain in Section 1. Every \(r^m\), \(m\in\mathbb Z\), is an eigenvalue: take \(|m|\) off-diagonal basis vectors of the appropriate sign in distinct coordinates. Since \(r^{\mathbb Z}=\lambda^{\mathbb Z}\), these eigenvalues approach zero. Zero is also spectral, because unit eigenvectors with eigenvalues tending to zero rule out a bounded inverse. If \(\beta>0\) is outside \(\lambda^{\mathbb Z}\), its distance from this lattice is positive. There are only finitely many lattice points in any compact subinterval of \((0,\infty)\), and its only finite accumulation point is zero. The coefficient inverse
\[
 \sum_\kappa c_\kappa\xi_\kappa\longmapsto
 \sum_\kappa\frac{c_\kappa}{d_\kappa-\beta}\xi_\kappa
\]
is bounded. Its range is in \(\operatorname{Dom}\Delta_\phi\), since
\(d_\kappa/(d_\kappa-\beta)=1+\beta/(d_\kappa-\beta)\) is uniformly bounded. The coefficient products give both inverse identities, including the identity on the entire domain of \(\Delta_\phi\). Negative numbers likewise have bounded coefficient inverses, and selfadjointness excludes nonreal spectrum. Thus
\[
 \operatorname{Sp}(\Delta_\phi)=\{0\}\cup\lambda^{\mathbb Z}.
\]
This proves an upper bound on the eventual all-weight intersection, but supplies no lower bound by itself.

For that lower bound define, with the same positive-frequency sign as (6),
\[
 T_f(x)=\int_{\mathbb R}f(t)\sigma_t(x)\,dt,
 \qquad \widehat f(s)=\int_{\mathbb R}f(t)e^{ist}\,dt,
\]
for every complex \(f\in L^1(\mathbb R)\). These are normal-coefficient integrals. Section 11.1 supplies the concrete predual and its dual identification for this construction; PP01 then defines this same integral. Coefficient topology alone would not establish the dual identification. The action spectrum is the intersection of the zero sets of \(\widehat f\) over **all** kernels for which \(T_f\) vanishes on the whole algebra. The Connes spectrum \(\Gamma(\sigma)\) is the intersection of those action spectra over **all** nonzero projections \(e\in N\), using the restricted action on \(eMe\).

An explicit filter excludes every nonlattice frequency. Put \(g=P^{-1}1_{[0,P]}\) and \(f=g-g(\,\cdot-P)\). Periodicity makes \(T_f=0\), whereas
\[
 \widehat f(s)=(1-e^{iPs})\frac{e^{iPs}-1}{iPs}
\]
is nonzero whenever \(s\notin\omega\mathbb Z\); the quotient has value one at zero. This argument holds in every fixed corner. Conversely each degree from (6) survives in every such corner. For \(0\ne x\) of degree \(k\) and \(0\ne e\in N\), its left support \(l\) is fixed. Factor contact in \(N\), proved by the central-support join in Section 8.5 and PP03, gives \(a\in N\) with \(eal\ne0\). Then \(y=eax\ne0\), since \(\operatorname{ran}x\) is dense in \(lH\). Its right support \(q\) is fixed and nonzero; contact gives \(b\in N\) with \(qbe\ne0\). The identity \(\ker y=(1-q)H\) proves \(ybe\ne0\). Consequently \(eaxbe\) is a nonzero element of \(eMe\) of the same degree. Testing the filter on this eigenoperator gives \(T_f(eaxbe)=\widehat f(k\omega)eaxbe\). Every annihilating kernel must therefore vanish at \(k\omega\). We have proved the full fixed-corner intersection
\[
 \Gamma(\sigma^\phi)=\omega\mathbb Z.
\]

Now let \(\psi\) be **any** faithful normal semifinite weight on \(M\). The comparison needed here consists of two exact supplied arguments, whose domains matter.

First, [MG-0–1](../../OA-FLOW/src/OA-FLOW-MG.md#oa-flow.mg.0) prove on the entire finite ideal \(N_\psi=\{x:\psi(x^*x)<\infty\}\) that
\[
 T_f^\psi x\in N_\psi,
 \qquad
 \Lambda_\psi(T_f^\psi x)
       =\widehat f(\log\Delta_\psi)\Lambda_\psi(x).
\]
The proof approximates the integrals by finite sums in the finite ideal, directing by finite sets of normal coefficients and Hilbert-vector error. The sums are uniformly bounded in operator norm and their GNS vectors converge in norm. Bounded graph closedness gives membership in the full finite ideal and the displayed equality. Density and faithfulness then show that \(T_f^\psi=0\) on \(M\) exactly when the bounded multiplier is zero on the entire GNS space. The full spectral-domain calculation in MG-1, including coefficient inverses and interval spectral projections, identifies the annihilator hull. Hence
\[
 \exp\operatorname{Sp}(\sigma^\psi)
       =\operatorname{Sp}(\Delta_\psi)\cap(0,\infty).
\]
No finite-total-weight or state hypothesis is used in this filter passage.

Second, [BC-1–3](../../OA-FLOW/src/OA-FLOW-BC.md#oa-flow.bc.1) construct the faithful normal semifinite balanced weight
\(\Theta([x_{ij}])=\phi(x_{11})+\psi(x_{22})\) on positive elements of \(M_2(M)\). Its two diagonal projections are fixed, and its modular action restricts to the two original modular actions. This restriction is proved through the whole closed finite-star graph and its adjoint, not from finite matrix moments. [FC1–5](../components/fixed-modular-corners-from-whole-graphs.md#fc1) give precisely this kind of full fixed-corner restriction, including corners with infinite weight. The fixed-corner invariance proved in [CS-3](../../OA-FLOW/src/OA-FLOW-CS.md#oa-flow.cs.3) then gives
\[
 \Gamma(\sigma^\psi)=\Gamma(\sigma^\Theta)
                    =\Gamma(\sigma^\phi)=\omega\mathbb Z.
\]
That proof uses an actual orbit-support sandwich in arbitrarily narrow spectral bands to compare corner annihilators; it does not suppose that the two corner identities are interchangeable without proof. This is the every-weight argument of MG-3. It constructs a balanced weight rather than importing a realization of every exterior-equivalence cocycle as a modular weight.

The identity corner is among the defining corners, so
\(\omega\mathbb Z\subseteq\operatorname{Sp}(\sigma^\psi)\). The filter identity therefore puts \(\lambda^{\mathbb Z}=\exp(\omega\mathbb Z)\) in \(\operatorname{Sp}(\Delta_\psi)\) for every such \(\psi\). Each spectrum is closed, and \(\lambda^n\to0\), so zero belongs to each spectrum as well. On the other hand the product state \(\phi\) is one of these weights, and its full spectrum was computed above. Both inclusions give
\[
 \boxed{\displaystyle
 S(M)=\bigcap_{\psi\ \mathrm{faithful\ normal\ semifinite}}
              \operatorname{Sp}(\Delta_\psi)
      =\{0\}\cup\lambda^{\mathbb Z}.}
\]
This is the type \(\mathrm{III}_\lambda\) invariant, defined using every faithful normal semifinite weight. The product-spectrum upper bound avoids the type III projection-to-corner transport used for the general reverse inclusion in MG-4. The modular foundations, finite-ideal closedness and balanced-weight corner comparison remain the explicit supplied prerequisites; their full proofs are the linked arguments, not an implicit classification input.

The source comparison is exact. Connes, *Une classification des facteurs de type III*, Section 2.2, printed pp.174–177, defines the full fixed-corner intersection and proves its factorial-fixed-algebra and equivalence properties. The two support witnesses above instantiate Proposition 2.2.2(c), whose proof is on pp.174–175. Theorem 3.2.1 and Lemma 3.2.2, printed pp.190–191, retain all faithful normal semifinite weights and the full GNS-filter passage; Corollary 3.2.7(a), printed p.192, agrees with the equality of \(S(M)\) and the modular spectrum when the centralizer is a factor. The present route uses the supplied balanced-weight and whole-graph proofs for its every-weight comparison, and the explicit coefficient resolvent for its upper bound. It does not import the source's general action-realization theorem or claim that its uninspected prerequisites have been proved here. The type notation is the discrete closed spectrum described in the introduction to Part IV, printed p.213. [The original free primary paper](https://numdam.org/article/ASENS_1973_4_6_2_133_0.pdf#page=43) supports this comparison.

**Theorem 6.1.** For a separable infinite-dimensional one-particle space and \(0<p<1\), \(p\ne\tfrac12\), the constant-covariance CAR factor is AFD and of type
\[
\mathrm{III}_{\,\min(p,1-p)/\max(p,1-p)}. \tag{28}
\]

**Proof.** The completed CAR-to-product GNS identification transports the factor, the faithful state and the full modular graph. The central expectation argument in Section 1 proves factoriality, and Lemma 2.1 proves sequential AFD approximation. The tail-commutator and finite-projection contradiction proves type III. The preceding all-weight calculation proves \(S(M)=\{0\}\cup\lambda^{\mathbb Z}\), which gives type \(\mathrm{III}_\lambda\). Independently, Theorems 3.2–5.1 and (24)–(27) give the center action and \(L=|\log\lambda|\). Thus the same parameter also satisfies (1):
\[
e^{-L}=e^{-|\log\lambda|}=\lambda
=\frac{\min(p,1-p)}{\max(p,1-p)}.
\]
For the source range \(0<p<1/2\), this is \(p/(1-p)\), the constant-covariance parameter. \(\square\)

The modular-action period is \(P\), while the center-flow period is \(L\):
\[
\begin{aligned}
P&=\frac{2\pi}{|\log\lambda|},\\
L&=|\log\lambda|.
\end{aligned} \tag{29}
\]
For example, \(p=1/3\) gives \(\lambda=1/2\), \(P=2\pi/\log2\), and \(L=\log2\). Using \(e^{-P}\) would give the wrong parameter.

At \(p=1/2\), the state is tracial and the infinite factor is \(\mathrm{II}_1\). At \(p=0\) or \(1\), the vacuum or filled Fock representation is irreducible and its von Neumann algebra is type I. For finite-dimensional one-particle space, every faithful constant state generates a finite matrix factor. None of these cases satisfies the hypotheses used in Theorem 6.1.

## 7. Problems with complete solutions

### Preparation for the complex error estimate

For Exercise 4, use the completed Bernoulli probability space and permutation action from Section 3. Let \(z\in L^\infty(X,\nu)\) be invariant under every finite coordinate permutation, let \(f\) be a complex cylinder function depending on a finite set \(F\), and fix \(\varepsilon>0\). Choose a complex cylinder function \(g\), depending on a finite set \(G\), with \(\|z-g\|_2<\varepsilon\). Choose a finite permutation \(\pi\) with \(\pi(F)\cap G=\varnothing\), and put \(f_\pi=\alpha_\pi f=f\circ T_{\pi^{-1}}\). Invariance gives \(\int zf\,d\nu=\int zf_\pi\,d\nu\), and disjoint-coordinate independence gives \(\int gf_\pi\,d\nu=(\int g\,d\nu)(\int f\,d\nu)\). With all unmarked integrals taken against \(\nu\), the estimate to be proved in Exercise 4 is
\[
\begin{aligned}
&\left|\int zf-(\int z)(\int f)\right|\\
&\qquad\le\varepsilon\bigl(\|f\|_2+|\textstyle\int f|\bigr).
\end{aligned}
\tag{11}
\]
Its two error terms are proved in the complete solution to Exercise 4.

**Exercise 1.** Compute the modular frequencies of \(e_{12}\) and \(e_{21}\) for \(p=1/3\). Find both periods in (29).

*Solution.* At \(p=1/3\), \(\rho=\operatorname{diag}(2/3,1/3)\). Direct multiplication gives
\[
\rho^{it}e_{12}\rho^{-it}=2^{it}e_{12}
=e^{it\log2}e_{12},\qquad
\rho^{it}e_{21}\rho^{-it}=2^{-it}e_{21}.
\]
The signed frequencies are therefore \(\log2\) and \(-\log2\). The action is the identity exactly when \(t\log2\in2\pi\mathbb Z\), so its least positive period is
\[
P=\frac{2\pi}{\log2}.
\]
In the represented core, the central generator transforms by \(z\mapsto e^{-iaP}z\). Its least positive return time is \(2\pi/P\), giving
\[
L=\log2,\qquad \lambda=\tfrac12.
\]
In particular \(PL=2\pi\); the two periods arise from different actions. The all-weight result in Section 6 also makes the subtype parameter \(e^{-L}=1/2\), with \(S(M)=\{0\}\cup(1/2)^{\mathbb Z}\).

**Exercise 2.** Prove (9) and explain why convergence on the one vector \(\Omega\) suffices here for strong convergence of a bounded sequence from \(M\).

*Solution.* For \(a\in A_n\), state preservation and bimodularity give
\[
\langle a\Omega,E_n(x)\Omega\rangle
=\phi(a^*E_n(x))=\phi(E_n(a^*x))=\phi(a^*x)
=\langle a\Omega,x\Omega\rangle.
\]
Since \(E_n(x)\Omega\in A_n\Omega\), these coefficient identities characterize its orthogonal projection, proving \(E_n(x)\Omega=Q_nx\Omega\). The finite matrix vectors have dense union in the pointed product, so \(Q_n\uparrow1\) strongly.

Set \(y_n=E_n(x)-x\). Then \(y_n\Omega\to0\) and \(\|y_n\|\le2\|x\|\). Finite right products commute with \(M\), and their orbit of \(\Omega\) is dense because the reference density is invertible. For every \(y'\in M'\),
\[
\|y_ny'\Omega\|=\|y'y_n\Omega\|\le\|y'\|\|y_n\Omega\|\to0.
\]
To pass to an arbitrary \(\xi\), approximate it by \(y'\Omega\); the remaining error is at most \(2\|x\|\|\xi-y'\Omega\|\), uniformly in \(n\). This proves strong convergence on all vectors. Applying the identical argument to \(x^*\), with \(E_n(x)^*=E_n(x^*)\), proves strong* convergence. The one-vector argument works here because the sequence lies in \(M\), commutes with that dense right orbit and is uniformly bounded.

**Exercise 3.** If \(x\) commutes with all occupation projections, why is \(x\in D\)? Why does the same argument need more than merely knowing that each \(D_n\) is abelian?

*Solution.* The occupation projections generate \(D_n\), so the hypothesis gives \([x,d]=0\) for every \(d\in D_n\). Bimodularity implies
\[
[E_n(x),d]=E_n([x,d])=0.
\]
Let \(e_{ss}\) be the full rank-one diagonal partition of \(A_n\). For \(s\ne t\),
\[
e_{ss}E_n(x)e_{tt}=e_{ss}e_{tt}E_n(x)=0.
\]
Thus every off-diagonal matrix entry vanishes and \(E_n(x)\in D_n\). Exercise 2 makes these operators converge strongly to \(x\), while the generated algebra \(D=(\bigcup_nD_n)''\) is strongly closed. Therefore \(x\in D\).

Abelianness alone gives only \(D_n\subseteq D_n'\cap A_n\), not equality. For example, the scalar subalgebra is abelian but its commutant is all of \(A_n\). The proof uses the complete diagonal partition to obtain \(D_n'\cap A_n=D_n\), and uses the compatible bimodular expectations and their strong limit to reach the entire infinite algebra.

**Exercise 4.** Supply the error estimate (11) when the cylinder functions are complex-valued.

*Solution.* Use the completed probability space and the permutation chosen in the preparation: the support of \(f_\pi\) is disjoint from that of \(g\). Write \(m_h=\int h\,d\nu\). Invariance of the measure and of \(z\) gives \(\int zf=\int zf_\pi\) and \(\|f_\pi\|_2=\|f\|_2\). Finite-coordinate independence gives \(\int gf_\pi=m_gm_f\). Hence the exact complex identity is
\[
\int zf-m_zm_f
=\int(z-g)f_\pi+(m_g-m_z)m_f.
\]
Cauchy–Schwarz, applied to absolute values, bounds the first term by \(\|z-g\|_2\|f_\pi\|_2\). It does not require real functions or an ordering of their values. The second term satisfies
\[
|m_g-m_z|=\left|\int(g-z)\cdot1\right|
\le\|g-z\|_2\|1\|_2<\varepsilon.
\]
Since \(\nu(X)=1\), \(\|1\|_2=1\). Adding the bounds proves
\[
\left|\int zf-(\int z)(\int f)\right|
\le\varepsilon\bigl(\|f\|_2+|\textstyle\int f|\bigr),
\]
which is (11) with both complex error terms justified. Letting \(\varepsilon\to0\), and then testing conjugates of the dense cylinder functions, also yields the original complex invariant-function conclusion \(z=m_z\) almost everywhere.

**Exercise 5.** Explain why identical mode densities are essential for the permutation proof. Then show that the centralizer is AFD without identifying its isomorphism class.

*Solution.* The tensor permutation unitary is fixed precisely when it commutes with the density. Identical densities give \(v_\pi\rho^{\otimes n}v_\pi^*=\rho^{\otimes n}\), so the required permutations belong to \(N\) and preserve the state.

A two-leg swap already detects the issue for unequal parameters \(p_j,p_k\). The occupation vectors \(01\) and \(10\), interchanged by the swap, have density eigenvalues
\[
(1-p_j)p_k,\qquad p_j(1-p_k).
\]
Their difference is \(p_k-p_j\). If this is nonzero, the swap does not commute with the density and cannot serve as the fixed unitary in the permutation argument. The identical-density assumption supplies exactly the invariance and disjoint-support relocation used there.

For AFD, the fixed algebra in \(A_n\) is finite-dimensional. More explicitly, its density value on an occupation word of weight \(m\) is \((1-p)^{n-m}p^m\); these values are distinct for different \(m\) under \(p\ne1/2\). Hence
\[
A_n^\sigma\cong\bigoplus_{m=0}^nM_{\binom nm}.
\]
These algebras increase. Equivariance gives \(E_n(x)\in A_n^\sigma\) for every \(x\in N\), and Exercise 2 gives strong* convergence to \(x\). Their strong closure is therefore \(N\), proving AFD without a classification or named-factor identification.

**Exercise 6.** Derive (14), including its phase. Why does compression of the ultraweakly dense algebraic span suffice to identify the whole corner?

*Solution.* Let \(J_n\xi(s)=P^{-1/2}e^{in\omega s}\xi\), the unitary from \(H\) onto the \(n\)-th Fourier subspace. Translation has
\[
u(t)J_n\xi=e^{-in\omega t}J_n\xi.
\]
Consequently
\[
\begin{aligned}
J_n^*\pi(x)u(t)J_n
&=e^{-in\omega t}\frac1P\int_0^P\sigma_{-s}(x)\,ds\\
&=e^{-in\omega t}\mathcal E(x).
\end{aligned}
\]
The second equality uses periodicity to replace the negative interval by a full positive period. This is (14); its minus sign comes from \(s\mapsto s-t\).

Covariance makes the finite span of \(\pi(x)u(t)\) a unital *-algebra containing the generators, so its ultraweak closure is \(B\). Compression is normal because each of its vector coefficients is an ambient vector coefficient. Each compressed spanning element belongs to the represented \(N\), which is ultraweakly closed as the fixed algebra. Therefore every element of \(q_nBq_n\), including every ultraweak limit, is represented in \(N\). Conversely, if \(y\in N\), \(\pi(y)\) is constant coefficient multiplication and \(J_n^*\pi(y)J_n=y\). Both inclusions identify the whole corner.

**Exercise 7.** Suppose only some integer spectral degrees occurred. Identify the step of Theorem 4.2 that would fail.

*Solution.* The factorial corner step still makes a central element diagonal with scalar blocks \(q_nzq_n=c_nq_n\). To compare two scalars, however, one needs an actual nonzero block \(q_n\pi(x)q_m\). A degree-\(k\) coefficient sends Fourier degree \(m\) to \(m-k\), so the proof's direct comparison of arbitrary \(n,m\) requires a nonzero degree \(k=m-n\).

With a restricted degree set, these direct blocks may be absent. Make a graph with vertices \(\mathbb Z\), joining \(n,m\) whenever such a block is nonzero. Commutation gives \(c_n=c_m\) on every edge and therefore along each finite path. It does not compare different connected components. Thus missing degrees do not automatically prove nonfactoriality; sufficient chains could still connect the indices. What fails is the argument that every pair has the direct nonzero block (15). If the indices split into components, distinct scalar values on them are no longer excluded by that argument. For a trivial action only degree zero occurs, and the Fourier projections themselves give central blocks. This also demonstrates why factoriality of the corners alone cannot replace the degree-connection step.

**Exercise 8.** In (18), take \(t=3P/2\). Compute \(s'\), \(k\), and the carry phase on each half of \([0,P)\).

*Solution.* The decomposition is obtained by requiring \(0\le s'<P\):
\[
\begin{array}{c|c|c|c}
s&s'&k&e^{-ik\theta}\\ \hline
0\le s<P/2&s+P/2&-2&e^{2i\theta}\\
P/2\le s<P&s-P/2&-1&e^{i\theta}
\end{array}
\]
Indeed in the first row \(s-3P/2=(s+P/2)-2P\), and in the second it equals \((s-P/2)-P\). The boundary \(s=P/2\) belongs to the second row, with \(s'=0\).

Thus (18) acts by \(e^{2i\theta}F(s+P/2,\theta)\) on the first half and by \(e^{i\theta}F(s-P/2,\theta)\) on the second. As a check, the gauge contributes \(e^{i\theta(s-s')/P}\), which is \(e^{-i\theta/2}\) and \(e^{i\theta/2}\) respectively. Multiplying by the carry gives \(e^{3i\theta/2}\) in both rows, exactly \(e^{i\theta t/P}\).

**Exercise 9.** Verify the gauge formula for \(t=-P/3\), including the interval crossing near \(P\).

*Solution.* Now \(s-t=s+P/3\). There are two branches:
\[
\begin{array}{c|c|c|c}
s&s'&k&e^{-ik\theta}\\ \hline
0\le s<2P/3&s+P/3&0&1\\
2P/3\le s<P&s-2P/3&1&e^{-i\theta}
\end{array}
\]
At the crossing point \(s=2P/3\), the second row gives \(s'=0\), as required by the chosen half-open interval.

Conjugation by \(V\) multiplies each carry by \(e^{i\theta(s-s')/P}\). In the first row the product is \(e^{-i\theta/3}\). In the second it is \(e^{2i\theta/3}e^{-i\theta}=e^{-i\theta/3}\). Hence on the entire interval
\[
V\mathcal F\ell(-P/3)\mathcal F^*V^*
=u(-P/3)\otimes m_{e^{-i\theta/3}}.
\]
The circle translation advances \(s\) by \(P/3\) modulo \(P\); the scalar agrees with \(e^{i\theta t/P}\), including the crossing.

**Exercise 10.** Why is \(e^{i\theta/2}\) permitted in (23), although the continuous function \(z\mapsto z\) has no continuous square root on the circle?

*Solution.* With the chosen representative \(0\le\theta<2\pi\), the function \(h(\theta)=e^{i\theta/2}\) is measurable and bounded by one. Its jump at the branch cut is harmless in \(L^\infty(\mathbb T)\). The concrete inclusion in \(W^*(z)\) can be proved by approximation: its Fejér polynomials \(h_N=K_N*h\) satisfy \(\|h_N\|_\infty\le1\) and \(h_N\to h\) in \(L^2\). For a bounded \(L^2\) test function \(f\),
\[
\|(m_{h_N}-m_h)f\|_2\le\|f\|_\infty\|h_N-h\|_2\to0.
\]
Bounded test functions are dense; the uniform multiplication bound extends convergence to every \(L^2\) vector. Each \(m_{h_N}\) is a polynomial in \(z,z^*\), so strong closedness puts \(m_h\) in the generated multiplication algebra and hence in (23).

For comparison, a continuous circle function \(g\) satisfying \(g(z)^2=z\) would make \(g(e^{i\theta})e^{-i\theta/2}\) a continuous function into \(\{1,-1\}\), therefore constant on \([0,2\pi]\). Its endpoint values would force \(g(1)=-g(1)\), an impossibility. Formula (23) needs the bounded measurable branch just constructed, not such a continuous root. Since \(|h|=1\) almost everywhere, \(m_h\) is a unitary with inverse \(m_{\bar h}\). At \(t=P/2\), this is exactly the central phase in (19); multiplying by its inverse leaves \(u(P/2)\otimes1\). The bounded Borel branch therefore provides the required phase removal.

**Exercise 11.** Compute the subtype for \(p=3/4\). Explain how swapping the two occupation labels changes the frequencies but preserves the two periods and the subtype.

*Solution.* For \(p=3/4\), the two density values are \(1/4,3/4\), so
\[
r=\frac13,\quad \log r=-\log3,\quad
\omega=\log3,\quad \lambda=\frac13.
\]
Thus \(e_{12}\) has frequency \(-\log3\) and \(e_{21}\) has frequency \(+\log3\). The full all-weight calculation of Section 6 gives \(S(M)=\{0\}\cup(1/3)^{\mathbb Z}\); the factor is therefore type \(\mathrm{III}_{1/3}\). Its periods are
\[
P=\frac{2\pi}{\log3},\qquad L=\log3.
\]

Swapping the occupation labels replaces \(p\) by \(1-p\), hence \(r\) by \(r^{-1}\), and exchanges \(e_{12}\) with \(e_{21}\). Their signed frequencies change sign. The magnitude \(|\log r|\), the subgroup \(r^{\mathbb Z}\), and the ratio \(\min(p,1-p)/\max(p,1-p)\) do not change. Therefore both periods, the entire invariant and the subtype are preserved; this conclusion uses the all-weight invariant rather than inferring a subtype from a state period alone. Numerically the relabeled state has \(p'=1/4\), \(r'=3\), and still \(e^{-L}=1/3\).

**Exercise 12.** A single matrix algebra \(M_2\) with density \(\rho\) has the same modular-action period \(P\). Why cannot Theorem 6.1 assign it the same type III subtype?

*Solution.* Every projection in \(M_2\) is finite, and the normalized matrix trace is a faithful normal finite trace. This algebra is the type I factor \(M_2\), so it fails both the infinite-dimensional and type III hypotheses of Theorem 6.1.

One can see the invariant obstruction directly. For its trace, the closed GNS involution has modular operator \(1\), so the intersection over all faithful normal semifinite weights is contained in \(\{1\}\), excluding the proposed type III invariant. Here is the finite-dimensional justification. By [GW1–4](../../OA-FLOW/src/OA-FLOW-GW.md#oa-flow.gw.1), the finite left ideal is a linear ultraweakly dense subspace. On a finite matrix algebra the matrix-entry coefficients give the ultraweak topology, and every linear subspace is closed in this finite-dimensional topology. Density therefore makes the finite left ideal the whole algebra. In particular the identity has finite weight, and monotonicity gives finite weight to every rank-one projection. For completeness, semifiniteness makes each rank-one projection \(e\) have finite weight: a nonzero finite-weight positive element below \(e\) is \(ce\), \(c>0\). Adding the two orthogonal rank-one projections gives finite weight at \(1\). The weight is therefore a bounded positive matrix functional, represented by a positive invertible density by faithfulness. In its diagonal Hilbert–Schmidt model the modular operator fixes the diagonal matrix vectors. Thus \(1\) occurs for every faithful normal semifinite weight and \(S(M_2)=\{1\}\).

For the nontracial state with density \(\rho\), its fixed algebra is the two-dimensional diagonal algebra, which is not a factor. The modular operator on the four-dimensional Hilbert–Schmidt space has eigenvalues \(1,1,r,r^{-1}\), and the only action degrees are \(0,\pm1\). Consequently Theorem 3.2's factorial-centralizer step fails, and the direct block of Theorem 4.2 is absent whenever \(|m-n|\ge2\). The infinite-coordinate permutation ergodicity used in Theorem 3.2 has no counterpart in this single-mode calculation. At the half-state the centralizer is instead all of \(M_2\), but the state is tracial and still supplies no type III conclusion. A modular-action period is a property of the chosen state; the infinite product supplies the nonsemifiniteness, factorial centralizer and complete degree structure used in the original core proof.

## 8. Projection comparison and the finite-factor alternative

This gives the projection argument needed at the end of Theorem 3.2. Let \(M\subseteq B(H)\) be a unital strongly closed \*-algebra, with \(H\) arbitrary. Sections 8.1–8.9 assume no separability, countable decomposition, trace, faithful state, modular action or factor type. Projection sums indexed by arbitrary sets mean nets of finite subsums.

The support, comparison and minimal-projection methods are compared with [Anantharaman and Popa, *An introduction to II₁ factors*](https://idpoisson.fr/anantharaman/publications/IIun.pdf#page=38), Proposition 2.2.4, Theorem 2.4.1, Proposition 2.4.2, Lemmas 2.4.6–2.4.7, Theorem 2.4.8, Corollary 2.4.9, and Proposition 2.4.13, printed pp.32–34 and 36–39 (PDF pp.38–40 and 42–45). Corollary 2.4.14, printed p.40/PDF p.46, states the finite tracial alternative. The proof below supplies central-support details, arbitrary orthogonal sums, scalar minimal corners and full matrix-unit surjectivity. Positive roots and supports are constructed directly, so the general continuous or Borel spectral calculus is not an input.

### 8.1. The elementary operator facts used below

The baseline is complex Hilbert-space completeness, scalar arithmetic and convergent power series, adjoints of bounded operators, and Zorn's lemma (the usual choice principle). The following elementary facts make explicit the analytic prerequisites of the subsequent arguments.

The underlying Cauchy–Schwarz estimate, adjoints, completeness of \(B(H)\), finite Gram–Schmidt and tensor positivity/completion are supplied in [*Infinite tensor products and their reference states*, Sections 10.1–10.4](infinite-tensor-products.md#10-hilbert-and-operator-foundations-for-the-finite-leg-vector-slice). Only those concrete Hilbert/operator constructions are used here.

For a bounded self-adjoint operator \(a\),
\[
\|a\|=\sup_{\|\xi\|\le1}|\langle\xi,a\xi\rangle|.
\]
Indeed, let the supremum on the right be \(m\). For unit vectors \(\xi,\eta\), real polarization and the parallelogram identity give
\[
|\operatorname{Re}\langle\eta,a\xi\rangle|
\le\tfrac m4(\|\xi+\eta\|^2+\|\xi-\eta\|^2)=m.
\]
Taking \(\eta=a\xi/\|a\xi\|\), when \(a\xi\ne0\), gives \(\|a\xi\|\le m\). The reverse inequality follows from Cauchy--Schwarz. In particular \(0\le a\le c1\) implies \(\|a\|\le c\). Positivity is closed under norm limits, because it is defined by the inequalities \(\langle\xi,a\xi\rangle\ge0\). A positive form satisfies Cauchy--Schwarz by applying its nonnegativity to \(\xi+t\eta\) and minimizing in \(t\in\mathbb C\). Consequently \(\langle\xi,a\xi\rangle=0\) for \(a\ge0\) implies \(a\xi=0\).

Every closed subspace \(L\subseteq H\) has an orthogonal projection. For completeness, a sequence approaching the infimum distance from \(\xi\) to \(L\) is Cauchy by the parallelogram identity applied to its two members and their midpoint. Completeness and closedness give a minimizing vector \(\eta\in L\). Minimality applied to \(\eta+tz\), for \(z\in L\) and \(t\in\mathbb C\), gives \(\xi-\eta\perp L\). The resulting decomposition \(H=L\oplus L^\perp\) is unique, linear, and its projection has norm at most one. In particular
\[
\overline{\operatorname{ran} a}=(\ker a^*)^\perp,
\]
because a vector is orthogonal to the range exactly when its image under \(a^*\) is zero.

Norm limits of elements of \(M\) belong to \(M\), since norm convergence implies strong convergence. Uniformly bounded strong limits multiply when both factors converge strongly: for \(a_i\to a\), \(b_i\to b\),
\[
\|(a_i b_i-ab)\xi\|
\le\|a_i\|\,\|(b_i-b)\xi\|+\|(a_i-a)b\xi\|.
\]
We will use this only for explicitly bounded nets. An adjoint limit will always be proved separately, rather than inferred from strong convergence alone.

The bounded monotone completeness used to describe normality at Section 8.9 also has a Hilbert-space proof. The Hilbert Riesz representation needed here follows from the projection argument above: the kernel of a nonzero bounded linear functional is a closed subspace of codimension one; projecting any vector outside the kernel onto its orthogonal complement yields a nonzero vector spanning that complement, and the functional is a scalar multiple of the inner product against it. Applying this separately to each variable identifies a bounded sesquilinear form with a unique bounded operator. For a uniformly bounded increasing net \(a_i=a_i^*\), the quadratic forms \(\langle\xi,a_i\xi\rangle\) have scalar limits. Polarization yields a bounded limiting sesquilinear form, and hence an operator \(a\) with \(a_i\le a\). If \(\|a_i\|\le C\), then \(0\le a-a_i\le2C1\). Once the positive square-root construction in Section 8.2 is available, a positive operator \(d\le2C1\) satisfies \(d^2\le2Cd\): conjugate \(2C1-d\ge0\) by \(d^{1/2}\). Therefore
\[
\|(a-a_i)\xi\|^2\le2C\langle\xi,(a-a_i)\xi\rangle\longrightarrow0.
\]
Strong closedness gives \(a\in M\); scalar quadratic values show it is the least upper bound. This argument is used only after Section 8.2, so there is no circular dependence.

### 8.2. Positive square roots and positive inverses inside \(M\)

Let \(b\in M\), \(b\ge0\), and choose \(R\ge\|b\|\), \(R>0\). Put \(a=1-b/R\). Then \(0\le a\le1\) and \(\|a\|\le1\). Define
\[
c_n=\frac1{2n-1}\frac{\binom{2n}{n}}{4^n}>0\quad(n\ge1).
\]
These coefficients satisfy \(c_1=1/2\) and \((n+1)c_{n+1}=(n-1/2)c_n\). The bound \(\binom{2n}{n}/4^n\le1/\sqrt{n+1}\) follows by induction using the ratio \((2n+1)/(2n+2)\). Thus \(c_n\le Cn^{-3/2}\) for a fixed scalar \(C\); grouping \(2^k\le n<2^{k+1}\) bounds each block by \(C2^{-k/2}\), so \(\sum_n c_n\) converges. Put \(F(z)=1-\sum_{n\ge1}c_nz^n\). Use formal coefficient differentiation, \(D(\sum f_nz^n)=\sum(n+1)f_{n+1}z^n\); its product rule follows from finite coefficient sums. The recurrence gives \((1-z)DF=-F/2\). For \(G=F^2=\sum g_nz^n\), therefore \((1-z)DG=-G\), so \((n+1)g_{n+1}=(n-1)g_n\). Since \(g_0=1\), we get \(g_1=-1\), \(g_2=0\), and \(g_n=0\) for every \(n\ge2\). Hence \(F^2=1-z\) as a coefficient identity. Absolute convergence of the coefficients justifies multiplication and substitution at \(z=1\), giving \(F(1)^2=0\) and \(\sum_n c_n=1\). This uses no analytic differentiation or differential equation.

For clarity, every power of the positive contraction \(a\) is positive. For \(n=2k\), \(\langle\xi,a^n\xi\rangle=\|a^k\xi\|^2\ge0\); for \(n=2k+1\), \(\langle\xi,a^n\xi\rangle=\langle a^k\xi,a a^k\xi\rangle\ge0\). Its norm is at most one by the operator-product norm inequality, so \(0\le a^n\le1\).

The norm-convergent series
\[
b^{1/2}=\sqrt R\left(1-\sum_{n\ge1}c_n a^n\right)
\]
belongs to \(M\). Every partial sum in parentheses is positive: \(a^n\ge0\), \(\|a^n\|\le1\), and \(\sum_{n=1}^N c_n\le1\). Its square is \(b\), by the absolutely convergent product identity \(F(z)^2=1-z\); the coefficient identities can be substituted into the norm-convergent operator series. It commutes with every operator commuting with \(b\).

This positive root is unique. If \(d\ge0\) and \(d^2=b\), then \(d\) commutes with \(b\), and hence with the constructed root \(c\). Thus \((d-c)(d+c)=0\). Positivity shows that \(\ker(d+c)=\ker d\cap\ker c\), using positive-form Cauchy--Schwarz from Section 8.1. The operator \(d-c\) vanishes on this kernel and on \(\operatorname{ran}(d+c)\). Those spaces have dense sum, so \(d=c\).

For \(b\ge0\) and \(\varepsilon>0\), choose \(R>\|b\|+\varepsilon\). The positive operator \(k=1-(b+\varepsilon1)/R\) satisfies \(\|k\|\le1-\varepsilon/R<1\). The geometric series
\[
(b+\varepsilon1)^{-1}=R^{-1}\sum_{n=0}^{\infty}k^n
\]
converges in norm in \(M\), is positive, and is bounded above by \(\varepsilon^{-1}1\). It commutes with \(b\). Therefore
\[
0\le b(b+\varepsilon1)^{-1}
=1-\varepsilon(b+\varepsilon1)^{-1}\le1.
\]
All these constructions work in \(pMp\) acting on \(pH\), with identity \(p\). This corner is strongly closed: a strong limit \(x\) of its elements belongs to \(M\) and satisfies \(pxp=x\).

### 8.3. Supports and polar decomposition inside \(M\)

For \(b\in M_+\), the contractions \(s_\varepsilon=b(b+\varepsilon1)^{-1}\) converge strongly to the projection \(s(b)\) onto \(\overline{\operatorname{ran} b}\). They vanish on \(\ker b\), and for a vector \(b\eta\) in the range,
\[
\|(s_\varepsilon-1)b\eta\|
=\varepsilon\|(b+\varepsilon1)^{-1}b\eta\|
\le\varepsilon\|\eta\|.
\]
The dense decomposition \(H=\overline{\operatorname{ran} b}\oplus\ker b\) and the uniform bound extend convergence to all vectors. Thus \(s(b)\in M\). It is the smallest projection \(p\) satisfying \(pb=b=bp\), by the range description.

For arbitrary \(x\in M\), put \(b=(x^*x)^{1/2}\). The rule \(b\eta\mapsto x\eta\) is well-defined and isometric, since \(\|x\eta\|^2=\|b\eta\|^2\). It extends to an isometry from \(\overline{\operatorname{ran} b}\) onto \(\overline{\operatorname{ran} x}\). Extend it by zero on \(\ker b\), obtaining a partial isometry \(v\) with
\[
x=vb,\qquad v^*v=s(b),\qquad vv^*=\text{projection onto }\overline{\operatorname{ran}x}.
\]
It belongs to \(M\), because
\[
x(b+\varepsilon1)^{-1}=v s_\varepsilon\longrightarrow v
\quad\text{strongly}.
\]
The initial and final projections belong to \(M\) by multiplication. They are the right and left support projections \(s_r(x)\), \(s_l(x)\). If \(x=pxq\) with \(p,q\in\mathcal P(M)\), then \(s_r(x)\le q\) and \(s_l(x)\le p\); the range/kernel descriptions prove both assertions. If \(x\ne0\), both supports are nonzero.

### 8.4. Arbitrary joins and orthogonal partial-isometry sums

For finitely many projections \(p_i\), their join is \(s(\sum_i p_i)\). Indeed
\[
\left\langle\xi,\left(\sum_i p_i\right)\xi\right\rangle
=\sum_i\|p_i\xi\|^2,
\]
so its kernel is \(\bigcap_i\ker p_i\), and the closure of its range is the closed span of the ranges of the \(p_i\). Section 8.3 puts this join in \(M\).

For a set-indexed family \((p_i)_{i\in I}\), let \(p_F\) be the join for a finite \(F\subset I\). The projections \(p_F\) converge strongly to the projection onto \(L=\overline{\operatorname{span}\bigcup_i p_iH}\): on \(L^\perp\) they vanish, and on a vector in a finite sum of the ranges they are eventually the identity. Density and their norm-one bound prove convergence on \(H\). Strong closedness puts \(\bigvee_i p_i\) in \(M\). Meets follow from \(\bigwedge_i p_i=1-\bigvee_i(1-p_i)\). No sequential or countability assumption is present.

Suppose \((v_i)_{i\in I}\subset M\) are partial isometries with mutually orthogonal initial projections \(p_i=v_i^*v_i\) and mutually orthogonal final projections \(q_i=v_iv_i^*\). For finite \(F\), \(v_F=\sum_{i\in F}v_i\) has norm at most one, and
\[
\|v_F\xi\|^2=\sum_{i\in F}\|p_i\xi\|^2.
\]
The net is Cauchy on each vector: choose a finite \(F_0\) whose partial sum approximates the supremum of these finite nonnegative sums, and all remaining squared norms are then small. Hilbert completeness gives \(v_F\to v\) strongly. Applying the same proof to the adjoints gives \(v_F^*\to w\) strongly, and matrix coefficients show \(w=v^*\). Section 8.1 therefore gives
\[
v^*v=\sum_i p_i,\qquad vv^*=\sum_i q_i.
\]
The strong limit belongs to \(M\). This proves the arbitrary orthogonal-sum equivalence used in projection comparison.

### 8.5. Central support and contact between two corners

First, every element of \(M\) is a linear combination of unitaries. For a self-adjoint contraction \(a\), Section 8.2 gives \(c=(1-a^2)^{1/2}\in M\) commuting with \(a\); then \(u=a+ic\) is unitary and \(a=(u+u^*)/2\). Scaling and decomposing \(x\) into its real and imaginary parts gives the assertion.

For \(p\in\mathcal P(M)\), define
\[
z(p)=\bigvee_{u\in\mathcal U(M)}upu^*\in M.
\]
Conjugation by a unitary permutes this family and preserves its closed range span, so \(z(p)\) commutes with every unitary. The preceding linear-combination assertion puts \(z(p)\) in \(Z(M)\). It majorizes \(p\). If a central projection \(z\) majorizes \(p\), it majorizes every \(upu^*\), hence \(z(p)\). Thus it is the smallest central projection majorizing \(p\). Its range is \(\overline{\operatorname{span}(MpH)}\), because every element of \(M\) is a linear combination of unitaries. This proves both central-support descriptions without a bicommutant argument.

If \(p\sim q\) via \(v^*v=p\), \(vv^*=q\), then any central projection \(z\) majorizing \(p\) also majorizes \(q=v p v^*\); applying this to \(v^*\) gives the reverse implication. Hence \(z(p)=z(q)\).

For projections \(p,q\),
\[
pMq=0\quad\Longleftrightarrow\quad z(p)z(q)=0.
\]
The reverse implication follows from \(pxq=z(p)z(q)pxq\). For the forward implication, for all unitaries \(u,w\in M\),
\[
(upu^*)(wqw^*)=u\,p(u^*w)q\,w^*=0.
\]
The range subspaces of every conjugate of \(p\) and every conjugate of \(q\) are therefore mutually orthogonal. Their closed spans are orthogonal, giving \(z(p)z(q)=0\). Section 8.3 now also proves that \(pMq\ne0\) is equivalent to the existence of nonzero equivalent subprojections of \(p\) and \(q\): take the polar supports of a nonzero \(pxq\); conversely a partial isometry between such subprojections or its adjoint is a nonzero corner element.

If \(M\) is a factor, every nonzero projection has central support one. Consequently \(pMq\ne0\) whenever both \(p\) and \(q\) are nonzero. This is the precise corner-contact fact needed for the minimal-projection argument below.

### 8.6. Full projection comparison, with no countability restriction

For arbitrary \(M\) and \(p,q\in\mathcal P(M)\), consider families of triples \((p_i,q_i,v_i)\), where the nonzero \(p_i\le p\) are mutually orthogonal, the \(q_i\le q\) are mutually orthogonal, and \(v_i^*v_i=p_i\), \(v_iv_i^*=q_i\). Order these families by inclusion. The union of a chain is such a family, so Zorn's lemma gives a maximal one. Section 8.4 gives \(v=\sum_i v_i\in M\), with initial \(P=\sum_i p_i\) and final \(Q=\sum_i q_i\).

Put \(p_0=p-P\), \(q_0=q-Q\). If \(p_0Mq_0\ne0\), Section 8.3 supplies nonzero equivalent subprojections of \(p_0,q_0\); reversing the polar partial isometry if needed adds a triple to the family. This contradicts maximality. Section 8.5 gives \(z(p_0)z(q_0)=0\).

Set \(z=z(q_0)\in Z(M)\). Then \(p_0z=0\), \(q_0(1-z)=0\), and the central compressions \(vz\), \(v(1-z)\) are partial isometries. They give
\[
pz=Pz\sim Qz\le qz,
\qquad
q(1-z)=Q(1-z)\sim P(1-z)\le p(1-z).
\]
Thus \(pz\precsim qz\) and \(q(1-z)\precsim p(1-z)\). For a factor, \(z\) is zero or one, proving that any two projections are comparable. This is the exact statement of the draft's Theorem 2.4.8 and Corollary 2.4.9, including their arbitrary Hilbert-space endpoints.

### 8.7. Minimal projections have scalar corners

A nonzero projection \(e\) is minimal exactly when \(eMe=\mathbb Ce\). One direction is immediate: a projection in a scalar corner is zero or \(e\).

For the other, suppose \(e\) is minimal and \(a=a^*\in eMe\) is not scalar. The quadratic values \(\langle\xi,a\xi\rangle\) on unit vectors of \(eH\) cannot all be equal, by polarization. Choose a real \(t\) strictly between two such values. Then \(h=a-te\) has a positive and a negative quadratic value. Put \(A=(h^2)^{1/2}\), using Section 8.2 in the corner.

For \(\varepsilon>0\), \(h(A+\varepsilon e)^{-1}\) is a self-adjoint contraction: its norm on a vector equals the norm of \(A(A+\varepsilon e)^{-1}\) on that vector, since \(h^2=A^2\). Therefore \(e\pm h(A+\varepsilon e)^{-1}\ge0\). Conjugating by \((A+\varepsilon e)^{1/2}\), which commutes with \(h\), gives \(A+\varepsilon e\pm h\ge0\); taking the norm limit yields \(A\pm h\ge0\).

Set \(b=(A+h)/2\), \(c=(A-h)/2\). These are positive, commute, and satisfy \(bc=0\) and \(h=b-c\). Both are nonzero, since \(h\) has quadratic values of both signs. Section 8.3 gives nonzero supports \(s(b),s(c)\le e\). Their ranges are orthogonal, because \(bc=0\). Hence \(s(b)\) is a nonzero proper subprojection of \(e\), a contradiction. Every self-adjoint element of \(eMe\) is scalar, and decomposition into real and imaginary parts proves \(eMe=\mathbb Ce\).

### 8.8. A minimal projection in a factor occurs in every nonzero corner

Let \(M\) be a factor, \(e\) a minimal projection, and \(p\ne0\) a projection. Section 8.5 gives a nonzero \(x\in pMe\). Its polar isometry \(v\in M\) has nonzero initial projection under \(e\); minimality forces \(v^*v=e\). Its final projection \(f=vv^*\le p\) is equivalent to \(e\) and is minimal: if \(0\ne g\le f\), then \(v^*gv\) is a nonzero projection under \(e\), hence equals \(e\), and \(g=f\). If \(p\) itself is minimal, this forces \(f=p\). Thus all minimal projections are mutually equivalent, and every nonzero projection contains one equivalent to \(e\).

These are the two comparison consequences in Anantharaman and Popa, Proposition 2.4.13. Section 8.6 proves the general comparison theorem.

### 8.9. The arbitrary-factor minimal-projection theorem, including surjectivity

Let \(M\) be a factor with minimal \(e\). Zorn's lemma gives a maximal family \((e_i)_{i\in I}\) of mutually orthogonal projections equivalent to \(e\), starting with \(e_{i_0}=e\). Its sum is one: otherwise Section 8.8 supplies another equivalent minimal projection under the nonzero complement, contradicting maximality.

Choose \(v_i\in M\) with \(v_i^*v_i=e\), \(v_iv_i^*=e_i\), and \(v_{i_0}=e\). Put \(E_{ij}=v_i v_j^*\). The orthogonality of the \(e_i\) gives \(v_j^*v_k=\delta_{jk}e\), so
\[
E_{ij}^*=E_{ji},\qquad E_{ij}E_{kl}=\delta_{jk}E_{il},\qquad
E_{ii}=e_i,\qquad\sum_iE_{ii}=1.
\]
These are a full system of matrix units.

Define on finite tensors
\[
U:\ell^2(I)\otimes eH\longrightarrow H,
\qquad U(\delta_i\otimes\eta)=v_i\eta.
\]
Here \(\ell^2(I)\), for arbitrary \(I\), is defined as the Hilbert completion of the finite-support scalar functions on \(I\), with squared norm \(\sum_{i\in F}|\xi_i|^2\) on a finite support \(F\). Thus the finite-support vectors are dense by construction. The vectors \(\delta_i\) are an orthonormal family with total span. The tensor product is likewise the Hilbert completion of its algebraic tensor product, after quotienting any zero-norm vectors. The ranges \(e_iH\) are orthogonal and have closed span \(H\), so the displayed isometry extends to a unitary. No enumeration of \(I\) is used.

The amplification \(T\otimes1\) used next is bounded with norm \(\|T\|\). To check this directly, write a finite tensor sum as \(\sum_{k=1}^m\xi_k\otimes\eta_k\) with orthonormal \(\eta_k\) by choosing an orthonormal basis of their finite-dimensional span. The squared input and output norms are \(\sum_k\|\xi_k\|^2\) and \(\sum_k\|T\xi_k\|^2\), so the latter is at most \(\|T\|^2\) times the former. Density gives the extension; testing \(\xi\otimes\eta_0\) gives the reverse norm inequality.

For \(x\in M\), each \(v_i^*xv_j\in eMe=\mathbb Ce\) has a scalar coefficient \(x_{ij}\). Let \(X=U^*xU\), choose a unit vector \(\eta_0\in eH\), and let \(J\xi=\xi\otimes\eta_0\). The bounded operator \(T=J^*XJ\in B(\ell^2(I))\) has entries \(x_{ij}\) and norm at most \(\|x\|\). For all elementary tensor vectors the coefficients of \(X\) are precisely those of \(T\otimes1_{eH}\). Their totality gives \(X=T\otimes1\).

Conversely, for \(T\in B(\ell^2(I))\), let \(P_F\) project onto the finite span indexed by \(F\subset I\). The operator \(U((P_FTP_F)\otimes1)U^*\) is the finite sum \(\sum_{i,j\in F}T_{ij}E_{ij}\in M\), of norm at most \(\|T\|\). Since \(P_F\to1\) strongly, \(P_FTP_F\to T\) strongly; amplification has the same convergence first on elementary tensors and then, by the bound, everywhere. Strong closedness therefore gives \(U(T\otimes1)U^*\in M\). Thus
\[
U^*MU=B(\ell^2(I))\otimes1_{eH}.
\]
This establishes onto realization, rather than only an injective matrix-coefficient map. The resulting isomorphism \(M\cong B(\ell^2(I))\) and its inverse preserve positivity and order. They therefore preserve every existing least upper bound, in particular the bounded increasing positive suprema constructed in Section 8.1. This is order normality in both directions. No equivalence with abstract-predual continuity is required for this realization or the finite-factor conclusion.

Conversely, a rank-one projection in \(B(K)\), for any nonzero Hilbert space \(K\), has no nonzero proper subprojection. An isomorphism transports this property. This proves: a factor has a minimal projection if and only if it is isomorphic to \(B(K)\). If the original \(H\) happens to be separable, \(I\) is at most countable, since choosing a unit vector in each nonzero orthogonal range gives an orthonormal family. The theorem itself retains arbitrary \(H\) and \(I\).

### 8.10. The exact finite tracial alternative consumed by CAR Theorem 3.2

Assume now that \(M\) is a factor with a faithful normal tracial state \(\tau\), \(\tau(1)=1\). If it has a minimal projection \(e\), Section 8.9 supplies the full family \((e_i)\). Equivalence gives
\[
\tau(e_i)=\tau(v_iv_i^*)=\tau(v_i^*v_i)=\tau(e)=a>0.
\]
For every finite \(F\subset I\), \(|F|a=\tau(\sum_{i\in F}e_i)\le1\). Consequently \(I\) is finite; otherwise it has finite subsets of arbitrarily large size. Hence \(M\cong M_n(\mathbb C)\) for \(n=|I|\). No assertion that all tracial states on factors are automatically faithful is needed, and this argument does not depend on normality of \(\tau\); faithfulness and traciality suffice for the finite conclusion.

A unital abelian subalgebra \(D\subset M_n(\mathbb C)\) cannot be diffuse. If it had no minimal projection, starting from \(1\in D\) one could repeatedly split a nonzero projection into two nonzero orthogonal projections in \(D\). After enough splittings this produces \(n+1\) nonzero orthogonal projections in \(M_n(\mathbb C)\). Their ranges are nonzero orthogonal subspaces of \(\mathbb C^n\), which is impossible. Therefore the existence of a diffuse unital abelian subalgebra excludes minimal projections in \(M\).

Also every isometry \(v\in M\) is unitary: \(\tau(1-vv^*)=\tau(1)-\tau(v^*v)=0\), and faithfulness makes the positive projection \(1-vv^*\) zero. Thus \(M\) is finite. A finite factor with faithful normal normalized trace and no minimal projection is exactly a type \(\mathrm{II}_1\) factor under the standard factor-type definition. This last naming step requires no general central type decomposition or modular classification.

In the CAR consumer, the existing independent supports already establish the faithful normal trace on \(N\), scalar center, and diffuse unital \(D\subset N\). Substituting \(M=N\), \(\tau=\phi|_N\) into Section 8.10 gives the precise finite-factor alternative used in Theorem 3.2. Its countable identical invertible \(M_2\)-product hypotheses remain those of the lesson. The arbitrary-factor theorem above is not weakened to that application.

### 8.11. Exact scope of the projection proof

The projection branch is complete from the stated Hilbert-space/choice baseline: square roots and inverses, supports and polar membership, arbitrary projection joins, strong and adjoint orthogonal sums, central support and corner contact, full comparison, scalar minimal corners, full matrix-unit realization, and the faithful tracial finite conclusion are proved here. There is no remaining projection-comparison, minimal-corner, matrix-unit, or \(B(K)\)-surjectivity theorem input in this branch.

For Theorem 3.2, [ITP Section 11](infinite-tensor-products.md#11-modular-action-of-the-faithful-identical-two-level-product) separately supplies the exact faithful countable identical matrix-product modular identification. [The earlier CAR lesson, Section 8](car-fock-and-quasifree-states.md#8-the-faithful-constant-state-completed-gns-identification), supplies its original CAR completed-GNS model identification. Neither use admits the general ITP modular theorem. No faithful-product Tomita theorem, infinite-product semifiniteness criterion, modular spectrum, continuous-core subtype criterion, or type III result is supplied or claimed here. The conclusions of this section concern projection comparison and the finite tracial alternative.

## 9. The exact matrix-product modular identification

[*Infinite tensor products and their reference states*, Section 11](infinite-tensor-products.md#11-modular-action-of-the-faithful-identical-two-level-product) supplies the full Tomita closure, its positive operator and diagonal imaginary powers for the faithful countable identical matrix product in (2). In particular it proves the action in (3), the ratio and signs in (5), and equivariance of the concrete local expectations. The proof checks the full initial graph on all of \(M\Omega\) and the exact adjoint/product domains.

For this concrete product, the fixed-algebra argument for Theorem 3.2 combines the supplied action with the finite fixed-density trace passage, occupation diagonal, permutation invariance and projection alternative in Sections 2–3 and 8. Its model is the pointed Hilbert–Schmidt completion. The CAR parity-string identification of completed GNS models in (2) is proved in [*Fermions, Fock space and quasi-free factors*, Section 8](car-fock-and-quasifree-states.md#8-the-faithful-constant-state-completed-gns-identification), including all determinant signs, whole doubled-Fock cyclicity, the two onto completed cyclic isometries and normal generated-algebra/state transport. The general ITP modular theorem, semifiniteness criterion, type III proof and subtype/core/flow conclusions are not admitted by this specialization. No equivalence between the literal fixed algebra and an algebraic state-centralizer definition is needed by this route.

## 10. Complete local expectations and the constant-state centralizer

This section gives full proofs of Lemma 2.1, Lemma 2.2 and Theorem 3.2 in *Constant CAR states and the periodic core*. The hypotheses are an infinite-dimensional separable complex one-particle Hilbert space with a supplied ordered complete countable orthonormal basis, countably infinitely many identical two-level legs, and \(0<p<1\), \(p\ne\tfrac12\). The endpoint, half-state, finite-dimensional and nonidentical-density exclusions apply throughout this section. The operator centralizer proof below does not use the type III result, the general product semifiniteness criterion, a Bernoulli measure construction, the function-space statement of original Lemma 3.1, a core, a subtype invariant, or a general modular-centralizer theorem.

The actual inputs are the complete concrete Hilbert/operator proofs in [ITP10.1–10.6](infinite-tensor-products.md#10-1-inner-product-estimates-and-orthogonal-projection), the whole faithful identical-product construction, Tomita graph and coordinate action in [ITP11.1–11.8](infinite-tensor-products.md#11-1-scalar-powers-and-the-local-hilbert-schmidt-model), the completed pointed normal bridge in [CAR15](car-fock-and-quasifree-states.md#15-reducing-blocks-finite-densities-and-completed-product-states), and the whole modular-graph transport in current [CAR17.2–17.3/17.6](car-fock-and-quasifree-states.md#17-the-exact-inner-times-of-the-faithful-constant-car-state). [CAR13](car-fock-and-quasifree-states.md#13-factorality-for-every-positive-contraction) supplies the original CAR factor statement independently of trace or type. The complete positive-root/support/projection/minimal-corner and matrix-unit proofs in [periodic CAR8.1–8.10](constant-car-states-and-the-periodic-core.md#8-1-the-elementary-operator-facts-used-below) are used here. The baseline is ZFC/choice, real and complex scalar completeness, finite matrix algebra, and the stated concrete Hilbert/operator definitions. Inner products are conjugate linear in the first variable and linear in the second.

### 10.1. The entire pointed algebra and its actual modular fixed algebra

Write \(a=1-p\), \(b=p\), \(\rho=\operatorname{diag}(a,b)\), \(H_0=M_2(\mathbb C)\) with Hilbert–Schmidt inner product, and \(\Omega_0=\rho^{1/2}\). Thus \(a,b>0\), \(a+b=1\), and \(\|\Omega_0\|=1\). For \(n\ge1\), the finite pointed Hilbert space is \(H_n=H_0^{\otimes n}\); its embeddings append \(\Omega_0\). ITP11.1–11.3 construct the entire completion, not just its local algebra:
\[
 H=\overline{\bigcup_{n\ge1}H_n},\qquad
 H=H_n\otimes H_{>n},\qquad
 \Omega=\Omega_n\otimes\Omega_{>n},\quad
 \Omega_n=\rho_n^{1/2},\quad \rho_n=\rho^{\otimes n}.       \tag{PC1}
\]
Here \(H_n=M_{2^n}(\mathbb C)\) by the finite matrix-unit tensor identification. Let \(A_n\) be its left multiplication algebra, amplified by the identity on the tail. Its physical matrix algebra is \(M_{2^n}\), whereas the Hilbert space on which that algebra acts has dimension \(4^n\). These two dimensions must not be interchanged. The inclusions of the physical matrices are \(x\mapsto x\otimes1_2\). Let
\[
 \mathcal A=\bigcup_n A_n,\qquad M=\mathcal A'',\qquad
 \phi(x)=\langle\Omega,x\Omega\rangle.                    \tag{PC2}
\]
The whole unital bicommutant proof ITP10.5 gives \(M=\overline{\mathcal A}^{\mathrm{WOT}}=\overline{\mathcal A}^{\mathrm{SOT}}\), a concrete von Neumann algebra. No boundedness of arbitrary WOT approximating nets is asserted.

Invertibility of \(\rho_n\) makes each map \(c\mapsto c\rho_n^{1/2}\) and \(c\mapsto\rho_n^{1/2}c\) onto \(H_n\). Thus the finite left and finite right orbits of \(\Omega\) are both dense in \(H\). Every local right multiplication commutes with \(\mathcal A\), hence with \(M\), since commutation with a fixed bounded operator is WOT closed. If \(x\in M\) kills \(\Omega\), it kills the entire dense right orbit, so \(x=0\). Thus \(\Omega\) is cyclic and separating for \(M\). Its one-term vector functional is concretely ultraweak continuous by ITP10.6, and it is a state. It is faithful: \(\phi(x^*x)=\|x\Omega\|^2=0\) implies \(x=0\). For the positive-element formulation, the Cauchy–Schwarz inequality for \(\langle\xi,q\eta\rangle\), \(q\ge0\), makes \(\phi(q)=0\) imply \(q\Omega=0\); separation makes \(q=0\).

ITP11.4–11.8 prove the full closure of \(x\Omega\mapsto x^*\Omega\), its exact weighted diagonal domains, and its positive operator \(\Delta\). Their diagonal unitaries \(U_t=\Delta^{it}\) preserve \(M\), fix \(\Omega\), are strongly continuous, and define the actual modular action
\[
 \sigma_t(x)=U_txU_t^*,\qquad
 \sigma_t(c)=\rho_n^{it}c\rho_n^{-it}\quad(c\in A_n).
                                                               \tag{PC3}
\]
This is the supplied concrete graph identification, rather than an assumption that some coordinate automorphism is modular. Put
\[
 N=M^\sigma=\{x\in M:U_txU_t^*=x\text{ for every real }t\}.
                                                               \tag{PC4}
\]
For each fixed \(t\), conjugation is a WOT homeomorphism, so its fixed linear subspace is WOT closed. The intersection is a WOT closed unital selfadjoint algebra: sums, products and adjoints of fixed elements are fixed. Therefore \(N\) is a concrete von Neumann algebra on \(H\). No general fixed-point algebra theorem is required. It is nonzero because it contains the identity and \(\Omega\ne0\).

CAR15 gives an onto pointed unitary from the actual faithful constant CAR cyclic completion to \(H\), with whole normal algebra equality; CAR17.6 transports the entire initial and closed Tomita graphs. Those exact identifications will transport the conclusions in PC10. CAR13 separately proves that the original CAR algebra \(M_p\), and consequently \(M\), is a factor. Factorality of the fixed algebra \(N\) will be proved below; it is not inferred from factorality of \(M\).

### 10.2. Complete local slices: amplification, positivity, normality and range

Let \(V_n:H_n\to H\) insert the reference tail, \(V_n\eta=\eta\otimes\Omega_{>n}\). It is an isometry. Put \(P_n=V_nV_n^*\), the projection onto the embedded \(H_n\). Define on every bounded operator on \(H\)
\[
 C_n(x)=V_n^*xV_n\in B(H_n),\qquad
 \widehat E_n(x)=C_n(x)\otimes1_{H_{>n}}.                  \tag{PC5}
\]
Compression has norm at most one. Amplification is bounded with exactly the norm of its first-leg operator: write a finite tensor vector with orthonormal vectors spanning its finite tail support, sum the squared first-leg norms, and use density; testing a unit elementary tail vector gives the reverse inequality. The same proof works on every finite direct sum. Consequently
\[
 \|\widehat E_n(x)\|\le\|x\|,\qquad
 \widehat E_n(x)^*=\widehat E_n(x^*),\qquad
 \widehat E_n(1)=1.                                      \tag{PC6}
\]
At level \(r\), the compression matrix is \((V_n^{\oplus r})^*[x_{ij}]V_n^{\oplus r}\), so it sends positive operator matrices to positive matrices. If \([c_{ij}]\ge0\) on \(H_n^{\oplus r}\), expand a finite vector in \((H_n\otimes H_{>n})^{\oplus r}\) in a common orthonormal finite tail basis. The quadratic form of \([c_{ij}\otimes1]\) is then a finite sum of nonnegative forms of \([c_{ij}]\). Density and the bounded amplification estimate extend positivity to the completed tensor space. Thus compression and amplification, and hence \(\widehat E_n\), are completely positive. This supplies every finite matrix level.

For \(c,d\in B(H_n)\), with their amplifications understood, \(cV_n=V_nc\) and \(V_n^*d=dV_n^*\). Therefore
\[
 \widehat E_n(cxd)=c\widehat E_n(x)d,\qquad
 \widehat E_n(c\otimes1)=c\otimes1,\qquad
 \widehat E_n^2=\widehat E_n.                             \tag{PC7}
\]
The last identity follows either from the preceding fixed-range identity or by another compression using the unit norm of the tail reference vector.

Here both WOT continuity and normality can be proved without a claim about arbitrary unbounded nets. Choose an orthonormal basis \(f_1,\ldots,f_d\) of \(H_n\), \(d=4^n\), and operator matrix units \(F_{uv}\in B(H_n)\). The whole finite expansion is
\[
 \widehat E_n(x)=\sum_{u,v=1}^d
 \langle V_nf_u,xV_nf_v\rangle(F_{uv}\otimes1).             \tag{PC8}
\]
Each output vector coefficient is a finite linear combination of input vector coefficients. This proves WOT continuity on all \(B(H)\). A defining concrete ultraweak functional has the form
\[
 F_{\boldsymbol\xi,\boldsymbol\eta}(x)
 =\sum_{j\ge1}\langle\xi_j,x\eta_j\rangle,
 \qquad \sum_j\|\xi_j\|^2<\infty,
 \quad\sum_j\|\eta_j\|^2<\infty.                         \tag{PC9}
\]
Evaluate it on (PC8). For each of the finitely many \((u,v)\), its scalar coefficient is \(\sum_j\langle\xi_j,(F_{uv}\otimes1)\eta_j\rangle\), absolutely convergent with the two square-sum bound in ITP10.6. The result is a finite linear combination of the input coefficients \(\langle V_nf_u,xV_nf_v\rangle\). Hence every target ultraweak seminorm pulls back continuously. This proves normality for all ultraweak-convergent nets, with no exchange of an infinite sum and a limit and no abstract predual assertion. Compression itself is normal because it transforms the two defining square-summable vector sequences by \(V_n\); amplification is normal by the same finite matrix expansion in its finite-dimensional domain.

On a local left product with \(m\ge n\), finite tensor inner products give
\[
 \widehat E_n(x_1\otimes\cdots\otimes x_m)
 =(x_1\otimes\cdots\otimes x_n)
       \prod_{j=n+1}^m\operatorname{Tr}(\rho x_j).          \tag{PC10}
\]
For \(m<n\), the local product is already in \(A_n\) and is fixed. By linearity \(\widehat E_n(\mathcal A)\subseteq A_n\).

We verify the whole closed range. In the finite Hilbert–Schmidt model, an operator \(T\) commuting with every right multiplication obeys \(T(uy)=T(u)y\), so \(T(u)=T(1)u\): this commutant consists exactly of the left multiplications. Its fixed commutation equations are WOT closed. If \(T_i\in A_n\) converges WOT to \(T\in B(H)\), the compression \(V_n^*T_iV_n\) converges WOT to \(V_n^*TV_n\), which is therefore a left multiplication. Also (PC8) makes \(\widehat E_n(T_i)\to\widehat E_n(T)\) WOT. Since \(\widehat E_n(T_i)=T_i\), uniqueness of coefficient limits gives \(T=\widehat E_n(T)\in A_n\). Thus \(A_n\) is WOT closed, and hence ultraweakly closed. WOT continuity, \(M=\overline{\mathcal A}^{\mathrm{WOT}}\), and (PC10) now give \(\widehat E_n(M)\subseteq A_n\). This step remains valid for unbounded WOT nets because (PC8) has only finitely many input coordinates. Since it fixes \(A_n\), the restriction
\[
 E_n:M\longrightarrow A_n,\qquad E_n(M)=A_n             \tag{PC11}
\]
is onto, normal, unital, completely positive, contractive, idempotent and \(A_n\)-bimodular. Restriction to the concrete ultraweakly closed range preserves normality. This proves the actual expectation and its full range, not just a finite elementary-tensor identity. It preserves \(\phi\), since \(V_n\Omega_n=\Omega\) and the tail reference vector has norm one.

The supplied modular unitaries split as their finite-leg and tail diagonal unitaries; the tail one fixes \(\Omega_{>n}\). Hence \(U_tV_n=V_nU_t^{(n)}\), where \(U_t^{(n)}u=\rho_n^{it}u\rho_n^{-it}\). In (PC5) this gives, on all \(B(H)\),
\[
 \widehat E_n(U_txU_t^*)=U_t\widehat E_n(x)U_t^*,\qquad
 E_n(N)\subseteq A_n^\sigma.                             \tag{PC12}
\]
The finite formula (PC10) is precisely the product slice \(\operatorname{id}_{A_n}\bar\otimes\phi_{>n}\) of original (8). One can also identify the grouping of the whole algebras directly. Every local matrix on the first \(m\ge n\) coordinates is a finite sum of a first-leg matrix times a local tail matrix. Conversely, holding a first-leg matrix fixed and taking WOT limits of local tail matrices shows that every elementary tensor in \(A_n\odot M_{>n}\) belongs to \(M\). For this step, expand the two test vectors in a finite orthonormal basis of \(H_n\): every coefficient of the fixed first-leg matrix tensored with a tail operator is a finite sum of tail coefficients. Thus this amplification is WOT continuous on all nets; fixed bounded multiplication is WOT continuous as well. Taking bicommutants of these two inclusions gives \(M=(A_n\odot M_{>n})''\) in the grouping (PC1). This is the defining spatial product, without a tensor commutant formula or an extension theorem for arbitrary functionals.

### 10.3. Original Lemma 2.1: the whole strong* expectation limit

The finite-support coordinate basis in ITP11.2 proves \(P_n\to1\) strongly. For \(\eta\in H_k\) and \(n\ge k\), write \(\eta=V_n\eta_n\). The exact operator identity is
\[
 \widehat E_n(x)\eta
 =V_n(V_n^*xV_n)\eta_n=P_nx\eta.                         \tag{PC13}
\]
Thus \(\widehat E_n(x)\eta\to x\eta\) for every finite-support vector. For arbitrary \(\zeta\in H\), choose such an \(\eta\). The remaining error satisfies
\[
 \| (\widehat E_n(x)-x)\zeta\|
 \le 2\|x\|\|\zeta-\eta\|+\|(P_n-1)x\eta\|
 \quad(n\ge k).                                         \tag{PC14}
\]
First let \(n\to\infty\), then make \(\|\zeta-\eta\|\) small. This proves strong convergence for every \(x\in B(H)\). Applying the same proof separately to \(x^*\) and using (PC6) proves strong convergence of the adjoints. In particular the whole original lemma is
\[
 \boxed{\quad E_n(x)\longrightarrow x\text{ strongly* for every }x\in M,
 \qquad\|E_n(x)\|\le\|x\|.\quad}                         \tag{PC15}
\]
Strong* here means the two strong limits for \(x\) and for \(x^*\); it is not operator-norm convergence.

The one-vector argument follows from the dense commuting right orbit. Since \(A_n\Omega=H_n\), its projection \(Q_n\) is \(P_n\). State preservation and bimodularity give, for \(c\in A_n\),
\[
 \langle c\Omega,E_n(x)\Omega\rangle
 =\phi(c^*E_n(x))=\phi(c^*x),\qquad
 E_n(x)\Omega=Q_nx\Omega.                                \tag{PC16}
\]
For a local right operator \(R\), which commutes with every \(E_n(x)-x\in M\),
\[
 \|(E_n(x)-x)R\Omega\|
 \le\|R\|\|(E_n(x)-x)\Omega\|\longrightarrow0.
\]
That right orbit is dense by PC01, and the differences are bounded by \(2\|x\|\). Approximation extends this limit to every vector; the same argument for \(x^*\) supplies its adjoint limit. Thus convergence on \(\Omega\) is used with the explicit dense commuting orbit and the uniform bound, not alone.

### 10.4. Original Lemma 2.2: the occupation diagonal is maximal abelian

In the physical matrix algebra \(A_n\cong M_{2^n}\), use the occupation basis indexed by \(\alpha\in\{0,1\}^n\). Let \(d_\alpha^{(n)}\) be its diagonal matrix units and \(D_n\) their span. The inclusions preserve diagonality. Define
\[
 \mathcal D=\bigcup_n D_n,\qquad D=\mathcal D''.           \tag{PC17}
\]
Every local diagonal commutes with every element of \(\mathcal D\). Fixed bounded commutation is WOT closed, so it commutes with its WOT closure \(D\). Applying the same closed commutation relation now to any fixed \(z\in D\) shows that all of \(D\) commutes with \(z\). Thus \(D\) is abelian. It is contained in \(M\), since \(M\) is WOT closed and contains \(\mathcal D\).

In \(A_n\), an element \(c=\sum_{\alpha,\beta}c_{\alpha\beta}E_{\alpha\beta}\) commuting with each \(d_\gamma^{(n)}\) has all off-diagonal entries zero: the \((\alpha,\beta)\) entry of \(d_\alpha^{(n)}c-cd_\alpha^{(n)}\), for \(\alpha\ne\beta\), is \(c_{\alpha\beta}\). Hence the diagonal commutant inside \(A_n\) is exactly \(D_n\). If \(x\in M\) commutes with \(D\), bimodularity gives
\[
 dE_n(x)=E_n(dx)=E_n(xd)=E_n(x)d\quad(d\in D_n).
\]
Thus \(E_n(x)\in D_n\subset D\). By (PC15), \(E_n(x)\to x\) strongly, and \(D\) is WOT closed, hence strongly closed. We have proved the entire original maximality conclusion
\[
 \boxed{\quad D'\cap M=D.\quad}                           \tag{PC18}
\]

For later density, (PC10) maps every local diagonal into \(D_n\). The finite diagonal algebra is WOT closed by its finitely many matrix-entry equations and the whole closed-range argument PC02. WOT continuity of \(\widehat E_n\) then yields
\[
 E_n(D)\subseteq D_n,\qquad
 \|(E_n(z)-z)\Omega\|\longrightarrow0\quad(z\in D).       \tag{PC19}
\]
This is density of local diagonal vectors in \(\overline{D\Omega}\); it is not density in all of \(H\). Neither a measure algebra nor a cylinder-function identification has entered.

### 10.5. The full finite-density passage and the state centralizer identity

Let \(B_n=A_n^\sigma\). For a physical matrix \(c\), its entry \((\alpha,\beta)\) is multiplied under (PC3) by \((w_\alpha/w_\beta)^{it}\), where
\[
 w_\alpha=a^{n-|\alpha|}b^{|\alpha|}>0,
 \qquad |\alpha|=\sum_{j=1}^n\alpha_j.                    \tag{PC20}
\]
An entry is fixed for every real \(t\) exactly when the weights are equal. If their positive ratio differs from one, its logarithm is nonzero; choosing a sufficiently small nonzero \(t\) gives a phase different from one by the scalar exponential/period argument in CAR17.1. Hence
\[
 B_n=\{c\in A_n:c\rho_n=\rho_nc\}
     =\bigoplus_{k=0}^n M_{\binom nk}(\mathbb C).           \tag{PC21}
\]
The last equality uses \(a\ne b\): \(a^{n-k}b^k\) is strictly monotone in \(k\). It follows solely from the displayed finite occupation eigenbasis. The fixed blocks consist of strings with the same number of occupied coordinates. In particular \(D_n\subseteq B_n\).

The finite state is \(\phi(c)=\operatorname{Tr}(\rho_nc)\), with the ordinary unnormalized finite matrix trace. The entry sum proves \(\operatorname{Tr}(uv)=\operatorname{Tr}(vu)\). If \(c\in B_n\) and \(d\in A_n\), commutation with \(\rho_n\) therefore gives
\[
 \phi(cd)=\operatorname{Tr}(\rho_ncd)
 =\operatorname{Tr}(d\rho_nc)
 =\operatorname{Tr}(\rho_ndc)=\phi(dc).                   \tag{PC22}
\]
This holds even when \(d\) is not fixed. It is stronger than merely checking two diagonal matrices.

| Physical row / column | 00 | 01 | 10 | 11 |
|---|---|---|---|---|
| 00 | x | 0 | 0 | 0 |
| 01 | 0 | x | x | 0 |
| 10 | 0 | x | x | 0 |
| 11 | 0 | 0 | 0 | x |

Entries marked x may be nonzero. The coordinate-swap matrix has ones at (00,00), (01,10), (10,01), and (11,11).

The two-leg physical matrix has occupation weights \(a^2,ab,ab,b^2\). The middle equal-weight block permits the coordinate swap in the fixed algebra. PC20–PC21 and PC27–PC28 give the exact formulas; the infinite scalar-center argument is PC07. This table supplies no additional hypothesis.

For \(x\in N\), (PC12) gives \(x_n=E_n(x)\in B_n\). For \(y\in M\), put \(y_n=E_n(y)\in A_n\). These are uniformly bounded and converge strongly*, separately for each operator. Their products converge strongly because, for every \(\xi\in H\),
\[
 \|(x_ny_n-xy)\xi\|
 \le\|x\|\|(y_n-y)\xi\|+\|(x_n-x)y\xi\|\longrightarrow0.
                                                               \tag{PC23}
\]
Interchanging \(x,y\) proves the corresponding limit for \(y_nx_n\). Evaluate the finite equality (PC22) at \(\Omega\) and pass through these two actual bounded-product limits. It gives
\[
 \phi(xy)=\phi(yx)\quad(x\in N,\ y\in M).                 \tag{PC24}
\]

For completeness, this particular fixed algebra is exactly the state's algebraic centralizer. Suppose \(x\in M\) satisfies \(\phi(xy)=\phi(yx)\) for every \(y\in M\). For \(c\in A_n\), state preservation and bimodularity imply \(\phi(E_n(x)c)=\phi(xc)=\phi(cx)=\phi(cE_n(x))\). The nondegenerate finite trace pairing then gives
\[
 \rho_nE_n(x)=E_n(x)\rho_n.                               \tag{PC25}
\]
Indeed write the difference as \(h\); the equality is \(\operatorname{Tr}(hc)=0\) for every physical matrix \(c\). Choosing each opposite matrix unit forces every entry of \(h\) to vanish. Thus \(E_n(x)\in B_n\subset N\). Strong convergence and WOT closedness of \(N\) give \(x\in N\). This supplies the exact special centralizer identity; it does not invoke or assert a general KMS or modular-centralizer theorem.

Let \(\tau=\phi|_N\). It is positive, normalized, faithful and concretely normal by restriction of the one-term vector state. Equation (PC24) gives \(\tau(xy)=\tau(yx)\) for all \(x,y\in N\), so it is a faithful normal tracial state on the whole fixed algebra. If \(v\in N\) is a partial isometry with \(v^*v=e\), \(vv^*=f\le e\), then
\[
 \tau(e-f)=\tau(v^*v)-\tau(vv^*)=0\quad\Longrightarrow\quad f=e.
                                                               \tag{PC26}
\]
Faithfulness supplies the implication. In particular every isometry in \(N\) is unitary. Thus \(N\) is finite, proved without a trace-existence theorem or a type statement about \(M\). Also every element of \(D\) is fixed: each local diagonal is fixed, and every fixed subspace is WOT closed. Hence \(D\subseteq N\).

### 10.6. Actual finite permutation unitaries and state invariance

Let \(\pi\) be a permutation of \(\mathbb N\) with finite support, contained in \(\{1,\ldots,s\}\). On the physical space \((\mathbb C^2)^{\otimes s}\), define the matrix
\[
 v_\pi\delta_\alpha=\delta_{\pi\alpha},\qquad
 (\pi\alpha)_j=\alpha_{\pi^{-1}(j)}.                       \tag{PC27}
\]
It permutes an orthonormal basis, so it is unitary. As a physical matrix its left multiplication belongs to \(A_s\); it is not being confused with a Hilbert-space permutation outside \(M\). It sends each coordinate matrix at \(j\le s\) to the same matrix at \(\pi(j)\), by evaluation on the finite occupation basis. Coordinates beyond \(s\) are unchanged. Since \(|\pi\alpha|=|\alpha|\), (PC20) gives
\[
 v_\pi\rho_sv_\pi^*=\rho_s,\qquad v_\pi\in B_s\subseteq N.
                                                               \tag{PC28}
\]
Thus \(\alpha_\pi=\operatorname{Ad}v_\pi\) is the actual finite-coordinate permutation on local matrices. It and its inverse are WOT and concretely ultraweak continuous by their fixed unitary coefficient formulas. They preserve \(\mathcal D\), hence preserve \(D\) on its whole WOT closure. State preservation on every \(x\in M\) follows directly from (PC24), applied to \(v_\pi\in N\) and \(xv_\pi^*\in M\):
\[
 \phi(\alpha_\pi(x))=\phi(v_\pi xv_\pi^*)
 =\phi(xv_\pi^*v_\pi)=\phi(x).                           \tag{PC29}
\]
On the Hilbert–Schmidt finite leg the separate Hilbert implementer \(u\mapsto v_\pi uv_\pi^*\) fixes \(\rho_s^{1/2}\); left multiplication by \(v_\pi\) itself need not fix that vector. The proof of (PC29) does not make that false substitution.

If \(g,f\in\mathcal D\) have disjoint finite coordinate supports, their tensor factors occupy distinct legs. Expanding their finite diagonal matrix entries and the product vector gives
\[
 \phi(gf)=\phi(g)\phi(f).                                 \tag{PC30}
\]
Explicitly write \(g=\sum_\alpha g_\alpha d_\alpha^F\), \(f=\sum_\beta f_\beta d_\beta^G\), with finite disjoint \(F,G\). Their product state value is \(\sum_{\alpha,\beta}g_\alpha f_\beta w_\alpha^F w_\beta^G\), the product of the two finite sums. This includes arbitrary complex entries and requires no probabilistic measure theorem.

### 10.7. The operator permutation argument and the scalar center

Suppose \(z\in D\) and \(\alpha_\pi(z)=z\) for every finite permutation. Fix a local diagonal \(f\). By (PC19), for any \(\varepsilon>0\) one can choose a local diagonal \(g\) with \(\|(z-g)\Omega\|<\varepsilon\). Choose a finite set of new coordinates outside the supports of \(f,g\), of the same size as the support of \(f\). Swapping the support of \(f\) with this set defines a finite permutation \(\pi\). The element \(f_\pi=\alpha_\pi(f)\) has support disjoint from that of \(g\). Invariance and (PC29) give \(\phi(zf)=\phi(zf_\pi)\), \(\phi(f_\pi)=\phi(f)\), and \(\|f_\pi\Omega\|=\|f\Omega\|\). Equation (PC30) gives \(\phi(gf_\pi)=\phi(g)\phi(f)\).

For any \(h\in D\), abelianity gives \(\|h^*\Omega\|=\|h\Omega\|\), since \(hh^*=h^*h\). Thus Hilbert Cauchy–Schwarz bounds the complex products by
\[
 |\phi(hf_\pi)|
 =|\langle h^*\Omega,f_\pi\Omega\rangle|
 \le\|h\Omega\|\|f\Omega\|,\qquad
 |\phi(h)|\le\|h\Omega\|.                                \tag{PC31}
\]
Use \(h=z-g\), subtract the finite independence equality and add the scalar correction. We get the full complex-valued estimate
\[
 |\phi(zf)-\phi(z)\phi(f)|
 \le\varepsilon\bigl(\|f\Omega\|+|\phi(f)|\bigr).          \tag{PC32}
\]
Let \(\varepsilon\downarrow0\). It follows that \(w=z-\phi(z)1\in D\) satisfies \(\phi(wf)=0\) for every local diagonal \(f\). Take \(f=h^*\) for every local diagonal \(h\); abelianity gives \(\langle h\Omega,w\Omega\rangle=0\). The local diagonal vectors are dense in \(\overline{D\Omega}\) by (PC19), and \(w\Omega\) belongs to that closure. Therefore \(\|w\Omega\|^2=0\). Separation gives
\[
 z=\phi(z)1.                                             \tag{PC33}
\]
This is an operator theorem proved directly in the actual pointed completion. It does not assert the function-space Lemma3.1 or supply its measure construction, cylinder density or almost-everywhere identification.

| Element | Finite coordinate support |
|---|---|
| Approximation g | 1, 2, 3, 4 |
| Test f | 1, 2 |
| Moved test | 5, 6 |

In this example the support move is exactly \(\pi=(1\ 5)(2\ 6)\), with \(g\in D_4\) and the test supported in coordinates \(\{1,2\}\). Its image is supported in \(\{5,6\}\); the implementer is in \(A_6\cap N\). The general finite-support construction, complex Cauchy–Schwarz bound and limit are PC27–PC33, not a measure-space assumption.

Now let \(z\in Z(N)\). Since \(D\subseteq N\), it commutes with \(D\). The full original Lemma2.2, (PC18), puts it in \(D\). Since all \(v_\pi\in N\), it commutes with them too, so \(\alpha_\pi(z)=z\) for every finite permutation. Equation (PC33) gives
\[
 Z(N)=\mathbb C1.                                        \tag{PC34}
\]
Thus \(N\) is a finite factor with the already proved faithful normal tracial state. Neither a zero-one law nor the classification of \(M\) is a premise of its scalar center.

### 10.8. The entire diagonal is diffuse by its exact occupation projections

Let \(q=\max(a,b)<1\). The finite family \(\{d_\alpha^{(n)}:\alpha\in\{0,1\}^n\}\) is an orthogonal partition of the identity in \(D_n\). Its values are exactly
\[
 \phi(d_\alpha^{(n)})=a^{n-|\alpha|}b^{|\alpha|}\le q^n.
                                                               \tag{PC35}
\]
Suppose \(e\ne0\) were a minimal projection in \(D\). Since \(D\) is abelian, the products \(ed_\alpha^{(n)}\) are orthogonal projections under \(e\), and their finite sum is \(e\). Minimality implies that each is zero or \(e\); exactly one is \(e\). Hence \(e\le d_\alpha^{(n)}\) for one cell of every finite partition. Positivity, (PC35) and faithfulness give
\[
 0<\phi(e)\le q^n\quad\text{for every }n.                 \tag{PC36}
\]
The geometric sequence tends to zero, a contradiction. Therefore \(D\) has no nonzero minimal projection. This proves diffuseness of the whole operator diagonal, using no positive-measure atom argument or identification with \(L^\infty(X,\nu)\).

### 10.9. Full minimal-corner and matrix-unit support for the type II1 inference

We supply the exact finite-factor alternative needed here. The following applies to any concrete factor \(F\) with a faithful tracial state \(\tau\), \(\tau(1)=1\); normality is retained in the application but is not needed for its finite matrix conclusion. All root/support operations used next exist inside \(F\) or its corners by the fully supplied periodic CAR8.1–8.4. More explicitly, for \(c\ge0\) and \(R\ge\|c\|\), \(R>0\), the norm-series root is
\[
 c^{1/2}=\sqrt R\left(1-\sum_{m\ge1}
 \frac{1}{2m-1}\frac{\binom{2m}{m}}{4^m}(1-c/R)^m\right).  \tag{PC37}
\]
The complete coefficient recurrence, absolute convergence, positivity, square identity and uniqueness are proved in periodic8.2, whose full body is a supplied input. The positive inverse \((c+\varepsilon1)^{-1}\) is its norm-convergent geometric series. The contractions \(c(c+\varepsilon1)^{-1}\) converge strongly to the projection onto \(\overline{\operatorname{ran}c}\), by their estimate on vectors \(c\eta\) and the dense range/kernel decomposition. For \(x\in F\), the isometry \(|x|\eta\mapsto x\eta\), extended by zero on the kernel, is the polar partial isometry in \(F\): it is the strong limit of \(x(|x|+\varepsilon1)^{-1}\). Its initial and final projections are the range/kernel supports. Arbitrary projection joins belong to \(F\), as strong limits of finite joins, with the finite join given by the support of the sum of the projections. These are full concrete constructions, not unproved general spectral or polar theorems.

First, a minimal projection \(e\) in \(F\) has scalar corner. If \(h=h^*\in eFe\) is not scalar, its quadratic values on unit vectors in \(eH\) are not all equal by polarization. Choose a real \(t\) between two such values and put \(k=h-te\), \(A=(k^2)^{1/2}\). The selfadjoint operator \(k(A+\varepsilon e)^{-1}\) is a contraction, since its norm on every vector equals that of \(A(A+\varepsilon e)^{-1}\), by equality of their squared forms. Thus \(e\pm k(A+\varepsilon e)^{-1}\ge0\). Conjugating by the commuting positive root of \(A+\varepsilon e\) gives \(A+\varepsilon e\pm k\ge0\). Norm limits give \(A\pm k\ge0\). The two positive elements
\[
 c=(A+k)/2,\qquad d=(A-k)/2,
 \qquad cd=0,\quad k=c-d                                  \tag{PC38}
\]
are nonzero because \(k\) has quadratic values of both signs. Their nonzero support projections are orthogonal and lie under \(e\). This contradicts minimality. So every selfadjoint element of \(eFe\) is scalar, and real/imaginary decomposition gives \(eFe=\mathbb Ce\). Conversely a scalar corner plainly has no proper nonzero projection.

Second, every nonzero projection \(f\) in a factor contains a projection equivalent to a given minimal \(e\). Here is the needed contact argument in full. The closed subspace
\[
 L=\overline{\operatorname{span}(FeH)}
\]
is invariant under every element of \(F\) and its adjoint. It is also invariant under every element of \(F'\) and its adjoint, because such an element commutes with \(F\) and with \(e\). Its orthogonal projection \(z\) therefore belongs to \(F'\cap F''=Z(F)\), by the fully supplied bicommutant theorem. It contains the nonzero range of \(e\), so factoriality gives \(z=1\). If \(fFe=0\), then \(f\) kills the dense subspace \(FeH\), contradicting \(f\ne0\). Choose nonzero \(x\in fFe\). Its polar isometry \(v\in F\) has nonzero initial projection under \(e\), which by minimality is \(e\); its final projection \(g=vv^*\) lies under \(f\). It is minimal: if \(0\ne h\le g\), then \(v^*hv\) is a nonzero projection under \(e\), hence \(e\), and multiplication by \(v,v^*\) gives \(h=g\). Thus \(g\sim e\).

Third, a full family of copies of \(e\) is finite and gives the entire algebra. Let \(c=\tau(e)>0\). For any finite orthogonal family \(e_1,\ldots,e_m\) equivalent to \(e\), choose \(v_i^*v_i=e\), \(v_iv_i^*=e_i\). Traciality gives \(\tau(e_i)=c\), so
\[
 mc=\tau\left(\sum_{i=1}^m e_i\right)\le1.               \tag{PC39}
\]
The possible finite cardinalities are a nonempty set of integers bounded by \(1/c\), hence have a largest value. Choose a family of that cardinality, including \(e_1=e\). If \(1-\sum_i e_i\ne0\), the contact argument adds another equivalent minimal projection under that complement, a contradiction. Therefore its finite sum is exactly one. This avoids assuming countability or an abstract maximal decomposition.

Take \(v_1=e\), and put \(E_{ij}=v_iv_j^*\). Orthogonal final ranges give \(v_i^*v_j=\delta_{ij}e\), so
\[
 E_{ij}^*=E_{ji},\qquad E_{ij}E_{kl}=\delta_{jk}E_{il},
 \qquad\sum_iE_{ii}=1.                                   \tag{PC40}
\]
For any \(x\in F\), the scalar-corner result gives \(v_i^*xv_j=x_{ij}e\). The full finite partition of one now gives the exact equality
\[
 x=\sum_{i,j}e_ix e_j=\sum_{i,j}x_{ij}E_{ij}.             \tag{PC41}
\]
Every scalar matrix produces the finite sum on the right in \(F\), so this is surjective onto \(F\), not just an injective coefficient map. It is injective because multiplication by \(v_i^*,v_j\) recovers \(x_{ij}e\), and \(e\ne0\). Multiplication and adjoints agree by (PC40). Its concrete norm and representation are also explicit: the map \(U:\mathbb C^m\otimes eH\to H\), \(U(\delta_i\otimes\eta)=v_i\eta\), is an onto isometry because the ranges \(e_iH\) are orthogonal and sum to \(H\). Under it the finite sum is \([x_{ij}]\otimes1_{eH}\), with precisely the scalar matrix norm by the amplification proof PC02. Hence \(F\cong M_m(\mathbb C)\), with the entire matrix-unit realization established.

A diffuse unital abelian subalgebra cannot lie in \(M_m(\mathbb C)\). Starting from its identity, absence of minimal projections lets one split a nonzero projection into two nonzero orthogonal projections, then repeat; each split increases the finite orthogonal family by one. After finitely many splits it has \(m+1\) nonzero orthogonal projections. Their physical ranges would be \(m+1\) mutually orthogonal nonzero subspaces of \(\mathbb C^m\), which is impossible. All of these are projections in the same abelian algebra; no measure-theoretic atom classification is used.

Apply this argument to \(F=N\), \(\tau=\phi|_N\). PC05 proved its faithful normalized trace and finiteness, PC07 proved its scalar center, and PC08 supplied the diffuse unital \(D\subset N\). If \(N\) had any nonzero minimal projection, the full finite matrix realization would contradict that diffuse diagonal. Therefore \(N\) has no minimal projection. The standard factor-type definition, exactly the naming boundary in periodic8.10, now proves the whole original theorem:
\[
 \boxed{\quad N\text{ is a type }\mathrm{II}_1\text{ factor.}\quad}
                                                               \tag{PC42}
\]
This inference requires no general type I classification, type decomposition, trace-existence result, or type III statement.

### 10.10. AFD, full CAR transport, source comparison and exact exclusions

The inclusions \(A_n\to A_{n+1}\) send \(B_n\) into \(B_{n+1}\), because \(c\rho_n=\rho_nc\) implies \((c\otimes1_2)(\rho_n\otimes\rho)=(\rho_n\otimes\rho)(c\otimes1_2)\). Each \(B_n\) is the explicit finite direct sum in (PC21). For \(x\in N\), (PC12) and (PC15) give \(E_n(x)\in B_n\) and bounded strong* convergence to \(x\). Conversely all \(B_n\subset N\), and \(N\) is WOT closed. Consequently
\[
 N=\left(\bigcup_nB_n\right)'',\qquad
 E_n(x)\in B_n,\quad E_n(x)\to x\text{ strongly* }(x\in N).
                                                               \tag{PC43}
\]
This proves the sequential AFD assertion following Theorem3.2. No uniqueness theorem or identification with a particular named hyperfinite factor is asserted.

Write \(W:H_{\mathrm{CAR},p}\to H\) for the full pointed bridge from CAR15, and \(M_p\) for the actual reduced doubled-Fock cyclic CAR von Neumann algebra. CAR17.6 proves, including every initial domain and graph closure and the exact adjoint/product domains,
\[
 W\Omega_p=\Omega,\quad WM_pW^*=M,\quad
 W\Delta_p^{it}W^*=U_t,\quad
 W\sigma_t^{\omega_p}(x)W^*=\sigma_t(WxW^*)\ (x\in M_p).
                                                               \tag{PC44}
\]
Thus \(WN_pW^*=N\) for the actual fixed algebra \(N_p=M_p^{\sigma^{\omega_p}}\). Conjugation and its inverse are concretely ultraweak continuous: they transform the defining square-summable vector sequences by the onto unitary \(W\) or \(W^*\), preserving their square sums. They preserve positive operators, products, adjoints and projection order. They transport every partial isometry and its initial/final projections, and therefore preserve finiteness and minimality in both directions. The vector state and its faithful normal normalized trace restriction transport by \(W\Omega_p=\Omega\). The expectations, diagonal and actual finite permutation unitaries are respectively \(W^*E_n(W\,\cdot\,W^*)W\), \(W^*DW\), and \(W^*v_\pi W\). Strong* convergence transports on every vector. Therefore original Lemma2.1, Lemma2.2 and Theorem3.2 refer to the whole actual completed CAR/product representation, not merely an agreement of local moments.

The positive/projection comparison is Claire Anantharaman and Sorin Popa, [*An introduction to II1 factors*, exact freely accessible 338-page draft](https://idpoisson.fr/anantharaman/publications/IIun.pdf), SHA-256 `09e63a8b2060ed9f7569c4898a4ead0581e34b8160524c4952702731f131d52f`. The relevant comparisons are Proposition 2.2.4, Theorem 2.4.1, Proposition 2.4.2, Lemmas 2.4.6–2.4.7, Theorem 2.4.8, Corollary 2.4.9, Proposition 2.4.13 and Corollary 2.4.14, printed pp.32–40. The scalar-corner and surjectivity arguments needed here are given explicitly above; the application does not require the draft's spectral or Kaplansky arguments. The broader projection-comparison theorem is available as a fully proved local provider, but this application needs only the contact/minimal-corner/finite matrix branch.

The non-half hypothesis is retained throughout this centralizer proof, although some local slice and trace arguments also apply at half. At \(p=0,1\), invertibility, separating cyclicity and positive occupation weights used here fail. A finite one-particle space has no unbounded supply of new coordinates or arbitrarily fine infinite occupation partitions, so this proof gives no finite-dimensional centralizer conclusion. Nonidentical densities do not generally give permutation unitaries in the fixed algebra; nonseparable or arbitrary-index products are outside this countable target.

The exact measure-space version of original Lemma3.1 and the identification in original (10) remain separate. This proof does not construct the Bernoulli probability measure, prove the measure/cylinder completion, or infer the function lemma merely from the operator argument. It completely supplies the operator route to Theorem3.2 without them. General modular centralizer identities, arbitrary-factor trace existence, product semifiniteness criteria, type III subtype, compact/real crossed products, scalar Fourier or measurable-phase theorems, continuous-core trace/center/flow, and the remaining course prerequisites lie outside this section.


## 11. Coefficient closure and scalar normalization

The circle crossing, vector slices and all-weight spectrum calculation use three closure facts and one scalar normalization. Their complete earlier constructions are [CF1–10](../../OA-FLOW/src/OA-FLOW-CF.md#oa-flow.cf.1), [CP01–06](../../OA-FLOW/src/OA-FLOW-CP.md#oa-flow.cp.1), [scalar integration SC](../../OA-FLOW/src/OA-FLOW-SC.md#sc-00), and [the disk and quarter-phase proof, Section 8.4](tensor-completion-injectivity-and-state-domination.md#8-4-disk-area-and-the-quarter-phase).

### 11.1. The coefficient predual and the actual filters

Use this lesson's inner product, linear in the second variable. Let \(E\) be the projective-norm completion of \(\overline H\otimes H\), paired with \(T\in B(H)\) by
\[
 (\overline\xi\otimes\eta)(T)=\langle\xi,T\eta\rangle,
 \qquad
 \|u\|_\pi=\inf_{u=\sum\overline\xi_j\otimes\eta_j}
                    \sum_j\|\xi_j\|\|\eta_j\|.
\]
The finite-dimensional coefficient tests of CP02 prove this is a norm and that a pure tensor has norm \(\|\xi\|\|\eta\|\). Every bounded functional on \(E\) gives a bounded sesquilinear form; Hilbert representation gives exactly one \(T\). Testing unit vectors proves equality of norms, so \(E^*=B(H)\) isometrically. CP04's telescoping algebraic approximations express every element of \(E\) as an absolutely summable tensor series. Reciprocal positive rescaling makes both vector sequences square summable. Thus its weak-star topology is the entire vector-series ultraweak topology.

For a concrete von Neumann algebra \(A\subseteq B(H)\), put \(Y=A_\perp\subset E\). This is closed. The quotient \(B=E/Y\) is complete: lift a subsequence of a Cauchy sequence with summable successive distances to summable representatives in \(E\), and pass to their sum. Taking the infimum over representatives identifies \(B^*\) isometrically with \(Y^\perp\subset E^*=B(H)\).

Since \(A\) is ultraweakly closed, \(Y^\perp=A\). Explicitly, if \(T\notin A\), choose a finite coefficient neighborhood disjoint from \(A\). In the finite-dimensional space of those coefficients, separate the image of \(T\) from the linear image of \(A\). The separating linear combination is an element of \(Y\) on which \(T\) is nonzero. It excludes \(T\) from \(Y^\perp\). Therefore
\[
 B^*=A,\qquad B=A_*=
 \left\{x\longmapsto\sum_j\langle\xi_j,x\eta_j\rangle:
                 \sum_j\|\xi_j\|^2,\ \sum_j\|\eta_j\|^2<\infty\right\}.
\]
The quotient norm is the functional norm: apply the proved norm-preserving Hahn–Banach theorem to \(B\) and its isometric dual identification. Hence \(A_*\) is a norm-closed Banach subspace of \(A^*\). No separability or abstract predual uniqueness theorem is needed.

For a point-ultraweakly continuous action \(\alpha\), \(f\in L^1(\mathbb R)\) and \(x\in A\), the functional
\[
 b\longmapsto\int f(t)b(\alpha_t(x))\,dt
\]
on \(A_*\) is bounded by \(\|f\|_1\|x\|\|b\|\), and its scalar integrand is measurable. The proved identity \((A_*)^*=A\) produces exactly one \(T_f(x)\in A\). This is PP01's integral, with \(\|T_f(x)\|\leq\|f\|_1\|x\|\). [AL1](../../OA-FLOW/src/OA-FLOW-AL.md#oa-flow.al.1) supplies its full normality and predual continuity. This establishes the duality separately from ITP10.6's coefficient-topology assertion.

### 11.2. Ultraweak density from a countable amplification

Let \(A\) be any unital selfadjoint algebra on \(K\), without norm closedness. Its ultraweak closure is \(A''\). On \(\ell^2(\mathbb N,K)\), write \(D(a)=\operatorname{diag}(a,a,\ldots)\). If \(C\) commutes with \(D(A)\), its coordinate entries \(C_{ij}\) belong to \(A'\). For \(x\in A''\), commutation with all these entries gives \(D(x)C=CD(x)\): first test finite-coordinate vectors, then pass to all vectors by boundedness. Thus \(D(x)\in D(A)''\).

For any vector \(\eta\), the projection onto \(\overline{D(A)\eta}\) commutes with \(D(A)\), since the orbit closure reduces this selfadjoint algebra. It commutes with \(D(x)\). The orbit closure contains \(\eta\), so it contains \(D(x)\eta\). Consequently \(D(a)\eta\) approximates \(D(x)\eta\) in norm with \(a\in A\).

Given finitely many defining ultraweak tests
\[
 F_l(T)=\sum_j\langle\xi_{lj},T\eta_{lj}\rangle,\qquad 1\leq l\leq m,
\]
bundle their square-summable \(\eta\)-families into one vector in \(\ell^2(\{1,\ldots,m\}\times\mathbb N,K)\). The same coordinate argument applies. An aggregate orbit error less than \(\varepsilon\) gives
\[
 |F_l(x-a)|\leq
 \left(\sum_j\|\xi_{lj}\|^2\right)^{1/2}
 \left(\sum_j\|(x-a)\eta_{lj}\|^2\right)^{1/2}.
\]
Choosing \(\varepsilon\) makes every required test small. This proves ultraweak density in \(A''\). The reverse inclusion holds because commutation is weak-operator closed, hence ultraweakly closed.

Apply this to the algebraic span of \(\pi(x)u(t)\) in Section 4 and the elementary spatial tensors in Section 5. Covariance and the tensor multiplication rule make these selfadjoint algebras. Compression and mixed vector slices are ultraweakly continuous on all nets: pull back each summable coefficient series through their bounded inclusion operators; both vector families remain square summable. Their target represented algebras are ultraweakly closed. This proves the density and normality used by the Fourier corners and center computation without assuming a norm bound on an arbitrary strong approximating net.

### 11.3. Why a nonzero corner of a factor is a factor

Let \(M\) be a factor, \(0\ne e\in M\), and suppose \(h=h^*\in Z(eMe)\) is nonscalar. Its quadratic values on unit vectors in \(eH\) cannot all agree, by polarization. Choose a real \(t\) between two such values. The positive and negative parts of \(h-te\), obtained by the norm-series square root, have nonzero orthogonal supports \(f,g\leq e\). These supports are central in \(eMe\): corner operators commute with the positive parts, their resolvents and their bounded strong support limits. Hence
\[
 fMg=f(eMe)g=\{0\}.
\]
Section 8.5's factor-contact theorem contradicts this for nonzero \(f,g\). Thus every central selfadjoint is scalar; splitting real and imaginary parts gives \(Z(eMe)=\mathbb Ce\). This is the corner-factor inference used before Section 1's finite trace contradiction.

### 11.4. The same pi for disks, circle periods and Fourier kernels

Tensor-completion Section 8.4 defines \(\pi\) by the unit-disk area and proves, by continuous scalar integration,
\[
 T(u)=\int_0^u(1-v^2)^{-1/2}\,dv,\qquad
 Q=\lim_{u\uparrow1}T(u)=\pi/2,\qquad
 e^{it}=\sqrt{1-u(t)^2}+iu(t)\quad(0\leq t<Q).
\]
Here \(u(t)\) is the continuous increasing inverse of \(T\). Differentiating this curve and its product with \(e^{-it}\) proves the identity without presuming a period. Its endpoint is \(e^{iQ}=i\), and its midpoint is \(e^{iQ/2}=(1+i)/\sqrt2\).

The first-quarter curve has both coordinates positive in its interior and strictly increasing second coordinate. Multiplication by \(1,i,-1,-i\) gives the four quarter arcs, with no repeated point before \(4Q\). The exponential addition law and \(e^{i4Q}=1\) therefore prove
\[
 e^{it}=1\ \Longleftrightarrow\ t\in2\pi\mathbb Z,\qquad
 e^{it}=-1\ \Longleftrightarrow\ t\in(2\mathbb Z+1)\pi.
\]
Indeed reduce a real \(t\) by an integer multiple of \(4Q\) into \([0,4Q)\), where the distinct quarter arcs identify those two points. This proves the frequency lattice excluded by PP02 and the circle periods of Sections 4–6.

For \(s\geq0\), put \(A(s)=T(s/\sqrt{1+s^2})\). Direct differentiation gives \(A'(s)=1/(1+s^2)\), \(A(0)=0\). The inverse-curve midpoint gives \(A(1)=Q/2=\pi/4\). Thus
\[
 \int_{-1}^1\frac{ds}{1+s^2}=\pi/2,\qquad
 \int_{-1}^1\frac{i\,ds}{1+is}=i\pi/2.
\]
The real part \(s/(1+s^2)\) in the second integral is odd. This is the positively oriented right edge of the square with vertices \(\pm1\pm i\). Rotation by \(i\) preserves \(dz/z\) and yields each next edge, so their sum is \(\oint dz/z=2\pi i\). This is [SF4](../../OA-FLOW/src/OA-FLOW-SF.md#oa-flow.shared-foundations.sf-4)'s rectangle Cauchy normalization.

The scalar series gives \(e^{a+ib}=e^a e^{ib}\) and \(|e^{ib}|=1\). Hence \(e^{2\pi z}=-1\) first forces \(\operatorname{Re}z=0\), then the proved period equivalence gives exactly \(z=i(n+1/2)\), \(n\in\mathbb Z\). This supplies the zero set of the hyperbolic cosine kernel used in [MF-SB](../../OA-FLOW/src/OA-FLOW-MF-SB.md#oa-flow.mf-sb.1). Finally exponential integration gives
\[
 \frac1{2\pi}\int_{-\pi}^{\pi}e^{ikt}\,dt
 =\begin{cases}1,&k=0,\\0,&k\in\mathbb Z\setminus\{0\},\end{cases}
\]
since \(e^{ik\pi}=e^{-ik\pi}\). Thus the circle Fourier and Gaussian disk constants use this same scalar \(\pi\), established before the spectral and modular constructions.

<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="420" viewBox="0 0 1000 420" role="img" aria-labelledby="quarter-title quarter-desc">
<title id="quarter-title">The quarter phase fixes the Fourier normalization</title>
<desc id="quarter-desc">The curve has coordinates square root of one minus u squared and u. Its midpoint parameter is pi over four, and endpoint parameter pi over two. Four rotations give the first period two pi. The proof also evaluates the integral of one over one plus s squared from zero to one as pi over four.</desc>
<rect width="1000" height="420" fill="#f8fbff"/>
<g font-family="Arial, sans-serif" fill="#19364d">
<text x="28" y="36" font-size="24" font-weight="bold">One scalar normalization, from the quarter curve</text>
<path d="M140 75V310H385" stroke="#7890a3" stroke-width="2" fill="none"/>
<path d="M360 310A220 220 0 0 0 140 90" stroke="#2469a0" stroke-width="4" fill="none"/>
<g fill="#2469a0"><circle cx="360" cy="310" r="5"/><circle cx="295.563491861" cy="154.436508139" r="5"/><circle cx="140" cy="90" r="5"/></g>
<text x="325" y="344" font-size="19">t = 0 · 1</text>
<text x="32" y="86" font-size="19">t = Q · i</text>
<text x="305" y="142" font-size="19">t = Q/2</text>
<text x="305" y="171" font-size="19">(1 + i)/√2</text>
<text x="125" y="344" font-size="18">0</text>
<text x="28" y="386" font-size="18">Coordinates (√(1 − u²), u); t = T(u)</text>
<rect x="495" y="83" width="475" height="262" rx="14" fill="#e7f1f8" stroke="#a3bdcf"/>
<text x="520" y="121" font-size="22">Q = π/2 · π is unit-disk area</text>
<text x="520" y="167" font-size="22">Four rotations: first period 4Q = 2π</text>
<text x="520" y="213" font-size="22">∫₀¹ ds/(1 + s²) = Q/2 = π/4</text>
<text x="520" y="259" font-size="22">Square boundary: ∮ dz/z = 2πi</text>
<text x="520" y="306" font-size="20">Frequency k: circle average = δₖ₀</text>
</g></svg>

The blue curve is the exact quarter unit circle. Its labels are proved parameter values. The embedded SVG is its reproducible vector source. Proof locators: Section 11.4 and tensor-completion Section 8.4. Exposition and diagram: CC0-1.0 to the extent of rights held.

## Bibliographic scope

Jan Dereziński, [*Introduction to representations of the canonical commutation and anticommutation relations*, arXiv:math-ph/0511030v2](https://arxiv.org/pdf/math-ph/0511030v2), Theorem 43(10), printed/PDF p.48, states the constant-covariance type \(\mathrm{III}_\lambda\) result; it does not supply a complete classification proof.

The main calculations include the complete normal occupation-diagonal identification, finite-density centralizer identity, operator permutation proof, direct exclusion of finite projections, coefficient-domain modular spectrum, Fourier corners, period-circle factor, lattice transform and vector-slice center computation. The exact completed CAR bridge, finite-factor trace and weighted modular graphs are the supplied full proofs in [Infinite tensor products](infinite-tensor-products.md) and [Fermions, Fock and quasi-free factors](car-fock-and-quasifree-states.md). [Periodic corner spectra from factor contact](../components/periodic-corner-spectra-from-factor-contact.md) supplies the interval filters and two nonzero support contacts. The full finite-ideal and every-weight comparison in [MG-0–3](../../OA-FLOW/src/OA-FLOW-MG.md#oa-flow.mg.0), with its balanced-weight and fixed-corner graph proofs, supplies the lower bound on the modular intersection; the explicitly computed product spectrum supplies the upper bound. Their deeper prerequisites retain their own stated scopes. Sections 8–11 give the projection, expectation and operator-centralizer arguments, the coefficient-predual and ultraweak-density arguments, and the scalar circle normalization, with the hypotheses for each argument stated in place. The infinite-dimensional and type III hypotheses remain essential, as Exercise 12 verifies.

Alain Connes, [*Une classification des facteurs de type III*](https://numdam.org/article/ASENS_1973_4_6_2_133_0.pdf), *Annales scientifiques de l’École Normale Supérieure* 6 (1973), 133–252, gives the action-spectrum definition on printed p.170, the full fixed-corner and equivalence development in Section 2.2 on pp.174–177, and the modular intersection development on pp.190–192. The explicit periodic filters and support witnesses are supplied in PP01–PP04, and the full all-weight calculation used here is specified in Section 6. The source's broader action-realization prerequisites are not imported by citation. Its introduction to Part IV on printed p.213 gives the type notation used for the closed discrete invariant. Source credit does not replace the all-weight proof.

The exact prerequisite proof versions used in the weight comparison are collected in the weight foundations. The selected arguments carry their source attribution and applicable licence notices.
