# Conormal amplitudes and complete test spaces

This modified component retains the definitions and complete Sections 1–5 of AN03-U008, *Singularities along a submanifold and smooth boundary passage*. It supplies the Besov endpoint, the full conormal amplitude characterization and all-real operator bounds used in boundary test spaces. Its later transmission and complex-type theories are not part of this selected component.

Principal author entity: AN-03 course-writing task, 2026. The AN-03 course-writing task and OpenAI Codex are responsible for the renewed edition. Current source connections and completeness additions: AN-04 course-writing task and OpenAI Codex, 5 October 2026; publisher: AN-04 local course project.

Original text: CC0.

## Exact current prerequisites

The full [measure and L2 proofs](../20261004-free-intrinsic-graph/prerequisites/measure-and-l2.md), [Fourier proofs](../20261004-free-intrinsic-graph/prerequisites/fourier-l2.md), [dyadic norms, local Sobolev bound and Schur estimate](../20261004-free-intrinsic-graph/prerequisites/dyadic-endpoint.md), and [ordinary quadratic multiplier and operator calculus O1–O6](../20261004-free-intrinsic-graph/prerequisites/ordinary-operator-calculus.md) are included earlier programme proofs. The [distributional coordinate map](../20261004-free-intrinsic-graph/prerequisites/coordinate-and-wavefront-localization.md), [all-real Hilbert duality](../20261005-mixed-halfspace-foundations/halfspace-support-and-duality.md), [Fourier Sobolev embedding](../20261005-restored-first-order-cauchy/spacetime-symbol-composition.md), and [locally finite partition construction PS5](../20261004-free-intrinsic-graph/prerequisites/global-principal-symbol.md) give the other exact entries. The proof map records their precise used nodes. In boundary charts the same partition construction uses relative half-balls; its compact exhaustion, cutoffs and local finiteness proof are unchanged.

The mathematical antecedent is the approved Hörmander III, 2007 eBook ISBN 978-3-540-49938-1, Sections 18.2–18.3. Source credit accompanies the included proofs; no citation is a replacement for them.

In local coordinates write \(x=(t,z)\in\mathbb R^k\times\mathbb R^{n-k}\), with dual variables \((\tau,\eta)\), and let \(Y=\{t=0\}\). For the nontrivial normal-frequency discussion \(1\leq k\leq n\). Codimension zero gives only smooth distributions and is treated by the same tangent-regularity definition with no normal frequency. An ordinary symbol \(a(z,\tau)\) of real order \(r\) satisfies
\[
|\partial_z^\beta\partial_\tau^\alpha a(z,\tau)|
\leq C_{K,\alpha,\beta}\langle\tau\rangle^{r-|\alpha|}
\quad(z\in K),\qquad \langle\tau\rangle=(1+|\tau|^2)^{1/2}.
\tag{C1}
\]
The global symbol class uses constants uniform in the base variables; the local class uses each compact set \(K\). Additional normal base variables \(t\) count as base variables in this definition. Finite-dimensional vector and matrix norms give the corresponding bundle-chart versions. Complex polyhomogeneous orders always refer to ordinary estimates of the real part of the order.

Throughout the retained Sections 1–5, \(\Psi^d\) denotes operators with ordinary \(S^d_{1,0}\) symbols; no polyhomogeneous expansion is assumed. A polyhomogeneity hypothesis is always stated expressly. The later transmission theory has separate classical-expansion hypotheses.

## 1. The endpoint is a Besov endpoint

Partition frequency space into a low-frequency ball and dyadic annuli, and let \(\Pi_j\) be their Fourier projections, \(j\geq0\). For \(1\leq p\leq\infty\), define
\[
\|u\|_{B^s_{2,p}}
=\left\|\big(2^{js}\|\Pi_j u\|_2\big)_{j\geq0}\right\|_{\ell^p}.
\tag{C2}
\]
Changing the first radius or using a smooth finite-overlap dyadic partition gives an equivalent norm. For the latter statement, each new frequency block is a sum of a fixed finite number of neighboring old blocks, with uniformly bounded multipliers; apply the triangle inequality in \(L^2\) and in \(\ell^p\), and reverse the two partitions. Sharp annuli give the same conclusion by their overlap with the smooth blocks. Plancherel and \(\langle\xi\rangle\asymp2^j\) on an annulus show that \(B^s_{2,2}=H^s\). The superscript \(p\) in the notation \({}^pH_{(s)}\) used in some accounts means this dyadic \(\ell^p\) index: it is \(B^s_{2,p}\), not an \(L^p\)-based Sobolev space.

We need three elementary continuity facts, including their endpoint versions.

First, a localized smooth change of coordinates or multiplication by a smooth function is bounded on \(B^s_{2,\infty}\) for every real \(s\). Here localized means that all relevant functions and derivatives are considered between fixed compact coordinate sets. For nonnegative integers \(a\), the chain and product rules prove boundedness on \(H^a\). The adjoint of a localized coordinate pullback is its inverse pullback times a smooth Jacobian factor; duality therefore proves the corresponding negative-integer bounds. To pass to the Besov index \(s\), choose integers \(a<s<b\). For such an operator \(T\), the two Sobolev bounds give
\[
\|\Pi_lT\Pi_j\|_{2\to2}
\leq C\min\big(2^{(j-l)a},2^{(j-l)b}\big).
\]
After multiplication by \(2^{ls-js}\), the right side decays geometrically in \(|l-j|\): use \(a\) if \(j\geq l\) and \(b\) if \(j<l\). Summation in \(j\) proves the assertion. The series represents the original distribution, since \(B^s_{2,\infty}\subset H^{s-\epsilon}\) for every \(\epsilon>0\), directly by summing \(2^{-2j\epsilon}\). This also proves that the local Besov spaces are well defined in charts and frames.

The same geometric matrix estimate proves boundedness for every \(1\leq p\leq\infty\), since convolution with an \(\ell^1\) sequence is bounded on each \(\ell^p\): apply the triangle inequality to its sum of shifted sequences. In particular both sequence endpoints are retained. The operator estimate in the next paragraph has the same summable matrix form and likewise holds for all these \(p\).

Second, a properly supported pseudodifferential operator with an ordinary \(S^d_{1,0}\) symbol of real order \(d\) maps \(B^s_{2,\infty,\mathrm{loc}}\) continuously to \(B^{s-d}_{2,\infty,\mathrm{loc}}\). We give the estimate rather than infer it from a Sobolev theorem at an endpoint. After localizing the output, its left symbol has compact base support. Integration by parts in that base variable gives the Fourier kernel bound
\[
|\widehat p(\xi-\theta,\theta)|
\leq C_M\langle\theta\rangle^d\langle\xi-\theta\rangle^{-M}.
\tag{C3}
\]
On neighboring dyadic blocks, integrating the last factor in either variable and applying the \(L^2\) Schur estimate gives \(\|\Pi_lP\Pi_j\|\leq C2^{jd}\). On separated blocks, \(|\xi-\theta|\) is comparable to \(2^{\max(j,l)}\). The same Schur estimate, now using the two block volumes, gives
\(C_M2^{jd}2^{-M\max(j,l)}2^{n(j+l)/2}\).
Choosing \(M\) larger than the dimension and the fixed weights gives a summable bound after multiplying by \(2^{l(s-d)-js}\). Summing the blocks proves the assertion for compact input localization. Proper support permits that localization on any fixed output compact set. The omitted input is separated from the diagonal; integration by parts in \(\xi\) in the kernel then gives a smooth function, with all derivatives, on that output set. This completes the local proof. Matrix entries obey the same estimates, so arbitrary finite bundle ranks are allowed.

For reference, the Schur estimate just used follows from Cauchy–Schwarz in the form
\(|Tf(\xi)|^2\leq (\int|K(\xi,\theta)|d\theta)
\int|K(\xi,\theta)||f(\theta)|^2d\theta\), followed by integration in \(\xi\). No pointwise positivity of the operator is assumed.

Third, local Sobolev estimates in frequency space will be used below. On a fixed pair of nested balls, any derivative of a smooth function at a point of the smaller ball is bounded by the \(L^2\) norms of finitely many derivatives on the larger ball. Multiply by a cutoff equal to one on the smaller ball and apply Fourier inversion, Cauchy–Schwarz with \(\langle\zeta\rangle^{-s}\), \(s>n/2\), and Plancherel, exactly as in the included [frequency Sobolev proof B2](../20261004-free-intrinsic-graph/prerequisites/dyadic-endpoint.md). Translation gives constants independent of the center. This proves the local estimate from the stated Fourier prerequisites.

## 2. Oscillatory amplitudes and removal of normal base variables

For a symbol \(a(t,z,\tau)\) of order \(r\), define
\[
u(t,z)=\int e^{it\cdot\tau}a(t,z,\tau)\,d\tau.
\tag{C4}
\]
This is a distribution for every real \(r\). To define its pairing with a compactly supported test function, use
\((1-\Delta_t)^N e^{it\cdot\tau}=\langle\tau\rangle^{2N}e^{it\cdot\tau}\), integrate by parts, and choose \(2N>r+k\). Derivatives of the amplitude in base variables do not raise its order. The resulting integral is absolutely convergent and bounded by finitely many test-function seminorms. Different sufficiently large \(N\)'s agree by integration by parts after a frequency cutoff and dominated convergence. The same argument proves independence of that cutoff and continuity under bounded symbol approximation.

For a symbol with **global** bounds in all base variables, there is a reduced amplitude depending only on \((z,\tau)\):
\[
\widetilde a(z,\tau)
=\left[e^{-i\langle D_t,D_\tau\rangle}a(t,z,\tau)\right]_{t=0},
\qquad u(t,z)=\int e^{it\cdot\tau}\widetilde a(z,\tau)\,d\tau.
\tag{C5}
\]
It belongs to \(S^r\), and truncation of the exponential before total degree \(N\) leaves \(S^{r-N}\), with every target seminorm controlled by finitely many input seminorms. The map is also continuous on bounded symbol sets with their local smooth topologies.

Here is a direct verification of all parts. For Schwartz \(a\), the partial Fourier transform of (C4) in \(t\), divided by \((2\pi)^k\), is
\((2\pi)^{-k}\iint e^{it\cdot(\theta-\tau)}a(t,z,\theta)\,dt\,d\theta\).
Fourier transformation in the two variables shows that this equals the first expression in (C5). In particular its sign is negative: a factor \(e^{ip\cdot t+iq\cdot\tau}\) acquires \(e^{-ip\cdot q}\).

For the estimates use the complete [ordinary metric and quadratic multiplier proof O2](../20261004-free-intrinsic-graph/prerequisites/ordinary-operator-calculus.md). Its \(Q=e^{iD_t\cdot D_\tau}\) has the opposite sign. If \(\mathcal R a(t,z,\tau)=a(-t,z,\tau)\), then \(\mathcal RQ\mathcal R=e^{-iD_t\cdot D_\tau}\): on Fourier variables the reflection changes the first dual variable to its negative. The reflection preserves every original symbol seminorm. Thus (O8), conjugated by this literal reflection, gives the complete order-\(r-N\) remainder in (C5), with the required negative sign. The metric is \(|dt|^2+\langle\tau\rangle^{-2}|d\tau|^2\), the weight is \(\langle\tau\rangle^r\), and its parameter is exactly \(1/(2\langle\tau\rangle)\). The passive variable \(z\) is held fixed; apply the same estimate to every \(z\)-derivative. The parameter-limit argument following (O9) proves these are genuine derivatives of the result, with finite seminorm control. Bounded compact symbol approximation from O3 then extends the Schwartz identity in (C5): the defining integrated-by-parts estimate for (C4) gives distributional convergence, and the multiplier estimate gives bounded locally smooth convergence of its reduced amplitudes. The full quadratic multiplier acts on tempered distributions; evaluation at \(t=0\) here is justified on the resulting smooth symbol, not on an arbitrary distribution.

For a local symbol, fix a compact working set inside its coordinate domain and a cutoff \(\chi(t,z)\) supported compactly in that domain and equal to one on a neighborhood of the working set. Extend \(a_\chi=\chi a\) by zero in the base variables. It is a global symbol of order \(r\), so (C5) applies to \(a_\chi\), and its inverse integral equals \(\chi u\) globally. It therefore equals the original \(u\) on the working neighborhood. Every remainder estimate is controlled by finitely many input seminorms on the fixed support of \(\chi\). At points \((0,z)\) where \(\chi\) is identically one nearby, all coefficients of the expansion are the derivatives of the original \(a\) at \(t=0\). Different such cutoffs give reduced amplitudes differing by \(S^{-\infty}\) locally in those \(z\)'s, since the expansion of their difference vanishes to every order. No global growth condition or global reduced representation is asserted for an uncut local symbol. We use this compact cutoff and zero-extension convention whenever (C5) is applied to local coordinates below.

## 3. Energy on an annulus and regularity away from the submanifold

Assume the reduced amplitude \(a(z,\tau)\) has compact \(z\)-support and global symbol bounds of order \(r\). Then
\(\widehat u(\tau,\eta)=(2\pi)^k\widehat a(\eta,\tau)\), where the second Fourier transform is only in \(z\). Integration by parts in \(z\) gives, for every \(M\),
\[
|\widehat a(\eta,\tau)|\leq C_M\langle\eta\rangle^{-M}\langle\tau\rangle^r.
\tag{C6}
\]
Thus \(\widehat u\) is locally square integrable. If \(\varphi\in C_c^\infty(\mathbb R^n)\) vanishes near zero, then for \(R>1\)
\[
\int |\widehat u(\xi)|^2|\varphi(\xi/R)|\,d\xi
\leq C_\varphi R^{k+2r}.
\tag{C7}
\]
To prove it, split the support of \(\varphi\) into a region where \(|\tau|\) is bounded below and one where \(|\eta|\) is bounded below. After scaling \(\tau=R\theta\), the first contribution is bounded by \(CR^{k+2r}\int\langle\eta\rangle^{-2M}d\eta\), since \(\theta\) lies in a compact set away from zero. In the second region \(|\eta|\geq cR\), and (C6) makes the contribution smaller than every prescribed negative power of \(R\) after choosing \(M\) large, despite the fixed polynomial growth in \(\tau\). This also works when \(r<0\).

If \(a\) is polyhomogeneous of complex degree \(r\), with leading homogeneous coefficient \(a_0\), then the exact leading energy limit is
\[
\lim_{R\to\infty}R^{-k-2\operatorname{Re}r}(2\pi)^{-n-k}
\int|\widehat u(\xi)|^2\varphi(\xi/R)\,d\xi
=\iint|a_0(z,\theta)|^2\varphi(\theta,0)\,dz\,d\theta.
\tag{C8}
\]
On the first region above, \(R^{-r}\widehat a(\eta,R\theta)\) converges to \(\widehat {a_0}(\eta,\theta)\), with an integrable majorant from the symbol bounds and compact base support. The second region still tends to zero. Dominated convergence and tangential Plancherel give the right side. The constants are \((2\pi)^{2k}\) from \(\widehat u\), \((2\pi)^{n-k}\) from tangential Plancherel, and the factor \((2\pi)^{-n-k}\) displayed on the left; their product is one. A complex test function is allowed by the same domination argument.

Formula (C7) is exactly \(u\in B^{-r-k/2}_{2,\infty}\). This endpoint cannot in general be replaced by \(H^{-r-k/2}\). For example, a delta distribution in \(k\) normal variables has constant normal Fourier transform: its weighted dyadic block norms at index \(-k/2\) are bounded, while their squared sum diverges.

If \(\chi(t)\) is compactly supported and equals one near zero, then \((1-\chi(t))u\) is Schwartz. Indeed,
\[
t^\alpha u=\int e^{it\cdot\tau}(-D_\tau)^\alpha a(z,\tau)\,d\tau.
\]
Any prescribed number of \((t,z)\)-derivatives of this integral is absolutely convergent after \(|\alpha|\) is chosen sufficiently large. On the support of \(1-\chi\), division by a sufficiently large power of \(|t|\) is smooth, with all derivatives controlled. Compact \(z\)-support and arbitrary choices of \(\alpha\) give all Schwartz seminorms. The same Fourier estimates after localization show \(\operatorname{WF}(u)\subset N^*Y\setminus0\): away from \(Y\) there is smoothness, and when the tangential covector dominates a fixed positive fraction of the full covector, (C6) gives rapid decay.

The generators tangent to the plane preserve the amplitude order. Tangential differentiation acts on \(a\); for \(i,j\leq k\),
\[
t_iD_{t_j}u
=\int e^{it\cdot\tau}(-D_{\tau_i})(\tau_j a(z,\tau))\,d\tau.
\tag{C9}
\]
A frequency derivative lowers the order raised by the factor \(\tau_j\). Thus every product of \(D_{z_j}\) and \(t_iD_{t_j}\) preserves the endpoint just proved. Multiplication by smooth local coefficients preserves it by Section 1.

## 4. Recovering the amplitude from tangent regularity

**The compact converse.** Suppose \(u\in\mathcal E'(\mathbb R^n)\), and for every pair of multiindices satisfying \(|\alpha_t|\geq|\beta_t|\),
\[
x^\alpha D^\beta u\in B^{-r-k/2}_{2,\infty}.
\tag{C10}
\]
Then \(u\) has the reduced representation (C4), with a global \(S^r\) amplitude of compact tangential support.

**Proof.** Compact support makes \(\widehat u\) smooth with polynomially bounded derivatives. Fourier transformation, (C2), and induction using the product rule give
\[
\int_{R/2<|\xi|<2R}
|\xi^\beta\partial_\xi^\alpha\widehat u(\xi)|^2d\xi
\leq C_{\alpha\beta}R^{2r+k},\qquad R\geq1,
\quad |\alpha_t|\geq|\beta_t|.
\tag{C11}
\]
The product rule first produces derivatives of \(\xi^\beta\widehat u\). Terms in which a derivative hits the monomial have smaller indices and preserve the difference \(|\alpha_t|-|\beta_t|\), so induction isolates (C11).

On the cone \(|\eta|\geq|\tau|\), use arbitrarily large tangential powers \(\eta^\beta\), with no normal powers. A unit ball about a large point in this cone is contained in a fixed enlargement of its dyadic annulus; at least one tangential coordinate is comparable to the radius on a smaller fixed ball. Formula (C11) bounds the \(L^2\) norm of every Fourier derivative on that ball by \(C R^{r+k/2-M}\), with arbitrary \(M\). The local Sobolev estimate in Section 1 then gives rapid decay of every derivative there. If there are no tangential variables, this cone has no large points and this step is unnecessary.

On the other cone put \(R=|\tau|\geq1\) and
\[
U_R(\theta,\eta)=R^{-r}\widehat u(R\theta,\eta).
\]
Use the ellipsoidal annulus
\(1/4<|\theta|^2+|\eta/R|^2<4\).
In (C11) choose the number of normal monomial factors equal to the number of normal derivatives. The powers of \(R\) from those two operations cancel; the change of variables contributes \(R^k\), canceled by the normalization in (C11). We obtain uniform \(L^2\) bounds on that ellipsoidal annulus for
\(\theta^\beta\eta^\gamma\partial_\theta^\alpha\partial_\eta^\delta U_R\), with \(|\beta|=|\alpha|\), for every \(\alpha,\gamma,\delta\).
The sum of \(|\theta^\beta|^2\) over \(|\beta|=|\alpha|\) is bounded below on a fixed neighborhood of the unit sphere. Hence these bounds control all derivatives of \(U_R\), with every tangential frequency weight, on fixed-size boxes centered at \(|\theta|=1,|\eta|\leq R\). The boxes fit inside the ellipsoidal annulus with a uniform margin after choosing their size small; bounded \(R\)'s are absorbed into the local bounds. The same local Sobolev estimate now gives
\[
|\partial_\xi^\alpha\widehat u(\tau,\eta)|
\leq C_{\alpha,M}\langle\tau\rangle^{r-|\alpha_t|}
\langle\eta\rangle^{-M}
\quad\hbox{for every }\alpha,M.
\tag{C12}
\]
Together with the first cone this holds globally.

Define
\[
a(z,\tau)=(2\pi)^{-n}\int e^{iz\cdot\eta}\widehat u(\tau,\eta)\,d\eta.
\tag{C13}
\]
Every derivative of this integral is absolutely convergent by (C12), including the polynomial \(\eta\)-factors from \(z\)-derivatives. It gives precisely the estimates (C1). Fourier inversion proves (C4). Partial Fourier transformation in \(t\) also shows that the amplitude vanishes outside the projection of \(\operatorname{supp}u\) onto the \(z\)-space. This proves the support statement and the converse. All estimates use finitely many of the hypotheses for each output seminorm. ∎

Every smooth vector field tangent to \(Y\) is a smooth linear combination of \(t_i\partial_{t_j}\) and \(\partial_{z_j}\). Indeed, a normal coefficient \(f(t,z)\) vanishing at \(t=0\) has the exact division formula
\[
f(t,z)=\sum_i t_i\int_0^1(\partial_{t_i}f)(st,z)\,ds.
\tag{C14}
\]
The integral is smooth, with all parameter derivatives obtained by differentiation under the integral. This proves the generator assertion.

Consequently the local amplitude class is exactly the class on which all products of tangent first-order operators preserve \(B^{-r-k/2}_{2,\infty,\mathrm{loc}}\). One direction is (C9) and (C14). For the converse, localize by a compact cutoff. Products of the generators express the normal balanced monomials in (C10), up to shorter terms; multiplication by additional powers of \(t\) and tangential coordinates is harmless on that compact set. Induction gives all of (C10), so the compact converse applies. Finally choose a locally finite family \(\psi_j\) with \(\sum_j\psi_j^2=1\). If \(\psi_j u\) has reduced amplitude \(a_j\), then \(u=\sum_j\psi_j(\psi_j u)\) has full amplitude \(\sum_j\psi_j(t,z)a_j(z,\tau)\). On each compact base set only finitely many terms contribute. This proves the local assertion without a support assumption on \(u\).

## 5. Intrinsic conormality, bundles and operator action

Let \(X\) be a smooth \(n\)-manifold, \(Y\) a closed smooth embedded submanifold, and \(E\) a smooth complex vector bundle. For real \(m\), define \(I^m(X,Y;E)\) by requiring
\[
L_1\cdots L_Nu\in B^{-m-n/4}_{2,\infty,\mathrm{loc}}(X;E)
\tag{C15}
\]
for every \(N\geq0\) and every collection of first-order smooth operators on \(E\) whose principal symbols vanish on \(N^*Y\). The topology is generated by the local Besov seminorms of all these images. Chart and frame changes preserve those spaces by Section 1, and the principal-symbol vanishing condition is intrinsic, so this definition and topology are coordinate independent.

In a bundle frame, (C14) expresses every such operator as
\(L=\sum_j A_jM_j+A_0\), where the \(A_j\) are smooth endomorphisms and the generators \(M_j\) have scalar principal symbols. When a coefficient is moved to the left across such a generator, the commutator is order zero: its first-order matrix terms cancel because the principal part is scalar. Induction on the length of an operator product therefore expresses it as a finite sum of smooth endomorphisms times words in the \(M_j\)'s. Thus scalar-principal generators suffice even for systems; no assumption that the original operator has scalar matrix coefficients is made.

By Section 4, the local normal form for codimension \(k\) is exactly
\[
u(t,z)=\int e^{it\cdot\tau}a(z,\tau)d\tau,
\qquad a\in S^{m+(n-2k)/4}.
\tag{C16}
\]
For compactly supported \(u\) in a chart the amplitude can be chosen globally in these coordinates. Conversely every such representation is locally conormal. Localization commutes with tangent words up to shorter words with smooth coefficients, so (C15) holds if and only if it holds after every member of any partition of unity. These arguments also compare the normal-form seminorms with the defining topology, using the finite-seminorm estimates above. For \(k=0\), every derivative is tangent, so repeated (C15) and local Sobolev estimates imply smoothness; all orders give the same smooth class.

A properly supported \(P\in\Psi^d(X;E,F)\) acts continuously
\[
P:I^m(X,Y;E)\longrightarrow I^{m+d}(X,Y;F).
\tag{C17}
\]
For completeness, let \(L\) on \(F\) have scalar tangent principal symbol, and choose \(L'\) on \(E\) with the same scalar symbol. The order \(d+1\) terms of \(LP\) and \(PL'\) cancel, so
\(LP=PL'+P_0\), with \(P_0\in\Psi^d(X;E,F)\).
This cancellation can be seen directly by differentiating the local oscillatory kernel; the terms without a derivative on a coefficient are the identical scalar products, and every remaining frequency derivative lowers the raised order by one. Apply this identity successively through a word of tangent generators. For an empty word, (C17) is the Besov estimate proved from (C3); for a longer word it reduces to shorter words and the same estimate. Scalar-principal reduction then gives (C15) for all tangent operators, with finite-seminorm continuity. This proves (C17) for arbitrary input and output ranks.

## 6. Completeness and the full local conormal topology

Here are the completeness details used by the boundary companions. Fix the sharp dyadic partition in (C2), including its low ball. If \(u_j\) is Cauchy in \(B^s_{2,p}\), every Fourier block is Cauchy in L2. Its limit \(v_l\) retains that block's Fourier support, up to measure-zero boundaries, by L2 convergence. The sequence \(2^{ls}\|v_l\|_2\) has the required \(\ell^p\) norm: for finite \(p\) first sum finitely many blocks and then take the supremum of the partial sums; for infinity take the supremum directly. The same argument applied to \(u_j-u_k\), followed by \(k\to\infty\), bounds the norm of the differences from the limiting sequence by the Cauchy bound.

The sum \(\sum_l v_l\) defines a tempered distribution. Choose any integer \(M>|s|+1\). Weighted orthogonality on disjoint annuli gives
\[
 \Big\|\sum_l v_l\Big\|_{H^{-M}}^2
 \le C\sum_l2^{-2l(M+s)}\big(2^{ls}\|v_l\|_2\big)^2<\infty.
 \tag{CT1}
\]
The sequence of bracketed terms is bounded by its \(\ell^p\) norm for every \(p\). The geometric sum converges. The complete Fourier L2 construction therefore gives one distribution \(u\), with \(\Pi_lu=v_l\). The preceding difference estimate proves \(u_j\to u\) in the original Besov norm. Thus every space in (C2), including both sequence endpoints, is Banach and embeds continuously into tempered distributions. This also supplies the distributional reconstruction used in the dyadic operator estimates.

For a fixed compact support and conormal index, a sequence Cauchy in every tangent-word seminorm converges first in its zeroth Besov norm to a distribution \(u\), retaining that support. Each tangent word is continuous on distributions, so the complete Besov limit of that word on the sequence equals the same word applied to \(u\). All the required norms are finite and the convergence holds in every defining seminorm. A countable chart exhaustion and the integer derivative indices give a countable seminorm family for the local space. The metric \(\sum_{j\ge0}2^{-j-1}\min(1,p_j(u-v))\) induces precisely that topology: finite initial sums control a fixed seminorm, and the uniform geometric tail controls the remainder. A metric Cauchy sequence is Cauchy in every \(p_j\); the local limits just constructed agree on overlapping charts by distributional uniqueness and glue by the locally finite partition to a complete local space. This proves the actual Fréchet completeness, including supported subspaces.

Smooth multiplication, coordinate changes and finite frame transitions have their full finite-seminorm continuity from Section 1 and the scalar tangent-generator reduction in Section 5. In particular these completed spaces have the same vectors and topology as the original conormal amplitude spaces; no new unspecified completion replaces an input distribution.
