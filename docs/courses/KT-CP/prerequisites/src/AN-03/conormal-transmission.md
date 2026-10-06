# Singularities along a submanifold and smooth boundary passage

A distribution can be rough across a submanifold while remaining stable under every derivative tangent to it. That stability identifies its normal-frequency amplitude, including its exact limiting regularity. At a boundary, the positive and negative normal frequencies carry additional information: a relation between their homogeneous coefficients decides whether applying an operator leaves a smooth function on the interior side. We develop that relation for every complex type, and then compute the boundary operators produced by simple and multiple layers.

We use the Fourier convention and quadratic multiplier estimates of [Quadratic Fourier multipliers at a moving scale](gauss-transform-estimates.md), the local symbol tools of [Localizing symbols with moving metrics](metric-localization.md), and the distributional quantizations and classical symbol changes of [Two measuring scales, one Weyl product](weyl-metric-products.md). The Fourier transform is \(\widehat f(\xi)=\int e^{-ix\cdot\xi}f(x)\,dx\), its inverse has coefficient \((2\pi)^{-n}\), and \(D=-i\partial\). Schwartz Plancherel and its unitary \(L^2\) extension are used with these constants. Basic prerequisites are distributional differentiation and tensor products, finite-dimensional calculus, smooth charts and bundles, partitions of unity, dominated convergence, and the elementary Cauchy integral and maximum principles. Coordinate changes of classical operator symbols are derived below by amplitude reduction, using the stated quadratic-multiplier prerequisite. The normal-form, endpoint, transmission and boundary-symbol assertions are proved in this lesson.

In local coordinates write \(x=(t,z)\in\mathbb R^k\times\mathbb R^{n-k}\), with dual variables \((\tau,\eta)\), and let \(Y=\{t=0\}\). For the nontrivial normal-frequency discussion \(1\leq k\leq n\). Codimension zero gives only smooth distributions and is treated by the same tangent-regularity definition with no normal frequency. An ordinary symbol \(a(z,\tau)\) of real order \(r\) satisfies
\[
|\partial_z^\beta\partial_\tau^\alpha a(z,\tau)|
\leq C_{K,\alpha,\beta}\langle\tau\rangle^{r-|\alpha|}
\quad(z\in K),\qquad \langle\tau\rangle=(1+|\tau|^2)^{1/2}.
\tag{C1}
\]
The global symbol class uses constants uniform in the base variables; the local class uses each compact set \(K\). Additional normal base variables \(t\) count as base variables in this definition. Finite-dimensional vector and matrix norms give the corresponding bundle-chart versions. Complex polyhomogeneous orders always refer to ordinary estimates of the real part of the order.

Throughout Sections 1–7, \(\Psi^d\) denotes operators with ordinary \(S^d_{1,0}\) symbols; no polyhomogeneous expansion is assumed. A polyhomogeneity hypothesis is always stated expressly. The transmission theory uses the classical expansions specified in Section 10.

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

Third, local Sobolev estimates in frequency space will be used below. On a fixed pair of nested balls, any derivative of a smooth function at a point of the smaller ball is bounded by the \(L^2\) norms of finitely many derivatives on the larger ball. Multiply by a cutoff equal to one on the smaller ball and apply Fourier inversion, Cauchy–Schwarz with \(\langle\zeta\rangle^{-s}\), \(s>n/2\), and Plancherel, exactly as in Section 2 of [Quadratic Fourier multipliers at a moving scale](gauss-transform-estimates.md). Translation gives constants independent of the center. This proves the local estimate from the stated Fourier prerequisites.

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

For the estimates apply Section 8 of [Quadratic Fourier multipliers at a moving scale](gauss-transform-estimates.md) to the phase \(-\langle D_t,D_\tau\rangle\), treating \(z\) as a passive variable. Use the metric
\(|dt|^2+|dz|^2+\langle\tau\rangle^{-2}|d\tau|^2\) and weight \(\langle\tau\rangle^r\). This metric is slowly varying. Its phase-dual distance is finite only for equal passive variables, and there it is a fixed factor times \(\langle\tau\rangle^2|\Delta t|^2+|\Delta\tau|^2\). Polynomial frequency-ratio bounds prove the required temperateness; they are the \((\rho,\delta)=(1,0)\) calculation in Section 8 of [Two measuring scales, one Weyl product](weyl-metric-products.md). The actual Gauss parameter at the observation point is \(1/(2\langle\tau\rangle)\). Restriction to \(t=0\) consequently gives exactly the order \(r-N\) remainder, including tangential derivatives. Bounded compactly supported approximation now extends the identity of distributions in (C5), using the defining estimate for (C4). The full quadratic multiplier acts on tempered distributions; its restriction in (C5) is asserted on these global symbol spaces, not on arbitrary tempered distributions for which restriction might be undefined.

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

## 6. The intrinsic principal symbol and its normalization

Factor out an ambient half-density and write a local conormal section as
\[
u(t,z)=(2\pi)^{-(n+2k)/4}
\int e^{it\cdot\tau}a(z,\tau)d\tau\,|dt\,dz|^{1/2},
\qquad a\in S^{m+(n-2k)/4}.
\tag{C18}
\]
Its leading symbol is the class of
\(a(z,\tau)|dz|^{1/2}|d\tau|^{1/2}\), modulo one lower ordinary amplitude order, on the chart \((z,\tau)\mapsto(0,z;\tau,0)\) of \(N^*Y\).

We check the full coordinate law. Let \(\kappa=(\kappa_1,\kappa_2)\) preserve \(t=0\), and pull back the ambient half-density. Formula (C14) gives \(\kappa_1(t,z)=\Psi(t,z)t\), with \(\Psi(0,z)=\kappa'_{11}(0,z)\) invertible. Near the submanifold shrink the chart so that \(\Psi\) is invertible; away from it the distribution is smooth. Changing the integration variable to \(\tau=\Psi(t,z)^T\theta\) gives the full amplitude
\[
A(t,z,\tau)=a_\kappa(\kappa_2(t,z),\Psi(t,z)^{-T}\tau)
\frac{|\det\kappa'(t,z)|^{1/2}}{|\det\Psi(t,z)|}.
\tag{C19}
\]
Every base derivative of the composed symbol introduces a factor linear in \(\tau\) paired with a frequency derivative, so (C1) retains its order on compact coordinate sets. Frequency derivatives lower the order normally. Choose the compact base cutoff \(\chi\) of Section 2 equal to one on the working neighborhood and extend \(\chi A\) by zero. Reducing this global symbol by (C5) gives the exact amplitude
\(a=[e^{-i\langle D_t,D_\tau\rangle}(\chi A)]_{t=0}\) of the localized pullback. Its inverse integral agrees with the original pullback on that neighborhood, and all \(N\)-term remainders have order \(m+(n-2k)/4-N\). At the working points of \(Y\), the cutoff and all its derivatives in the expansion are respectively one and zero.

The zeroth term is
\[
a_\kappa\big(\kappa_2(0,z),\kappa'_{11}(0,z)^{-T}\tau\big)
|\det\kappa'_{11}(0,z)|^{-1/2}
|\det\kappa'_{22}(0,z)|^{1/2}.
\tag{C20}
\]
Indeed, the off-diagonal block \(\kappa'_{12}(0,z)\) vanishes, so the full determinant is the product of the two diagonal block determinants. The factor in (C20) is exactly the half-density Jacobian on \((z,\tau)\). This proves intrinsic invariance modulo one lower order, including its exact determinant powers. A bundle transition matrix contributes its value on \(Y\); every additional normal derivative of that matrix in the reduction is paired with a frequency derivative and therefore contributes only to lower orders.

On a real rank-\(k\) vector bundle \(V\to Y\), define \(S^\nu(V;\Omega_V^{1/2})\) by requiring the coefficient of \(|dz|^{1/2}|d\tau|^{1/2}\) to have ordinary order \(\nu-k/2\). Fiber dilation multiplies that coordinate half-density by the factor \(t^{k/2}\); hence its intrinsic homogeneous degree includes \(k/2\). Base/fiber changes obey the same determinant calculation and preserve these estimates. In (C18) the intrinsic symbol order is consequently \(m+n/4\), independent of codimension.

Let \(\widehat E\) be the pullback of \(E|_Y\) to \(N^*Y\). The construction gives an isomorphism
\[
\frac{I^m(X,Y;\Omega_X^{1/2}\otimes E)}{I^{m-1}(X,Y;\Omega_X^{1/2}\otimes E)}
\simeq
\frac{S^{m+n/4}(N^*Y;\Omega_{N^*Y}^{1/2}\otimes\widehat E)}
{S^{m+n/4-1}(N^*Y;\Omega_{N^*Y}^{1/2}\otimes\widehat E)}.
\tag{C21}
\]
Surjectivity follows by realizing local amplitudes in (C18), multiplying by cutoffs in the ambient chart, and summing a locally finite partition on \(Y\). Formula (C20) makes the resulting principal symbol the prescribed one. To identify the kernel, localize compactly in a chart. The reduced amplitude is its partial Fourier transform in the normal variables, with the fixed factor in (C18), so it is unique. By the normal-form equivalence, the localized distribution belongs to \(I^{m-1}\) exactly when this amplitude has one lower order. This proves injectivity and the kernel assertion; changes off \(Y\) contribute smooth terms only.

The normalization can be checked in two ways. Before introducing (C18), put \(r=m+(n-2k)/4\) in (C8); then the power of \(R\) is \(2\operatorname{Re}m+n/2\), and with the factor \((2\pi)^{-n}\) on the energy side the limit is \((2\pi)^k\int|a_0|^2\varphi(\theta,0)\). Inserting the coefficient in (C18) multiplies that limit by \((2\pi)^{-(n+2k)/2}\). Thus the normalized amplitude has the equivalent limit with coefficient \((2\pi)^{-n/2}\) on the Fourier-energy side and coefficient one on the amplitude side.

For a pseudodifferential kernel on a \(d\)-manifold, the ambient dimension is \(n=2d\) and the diagonal codimension is \(k=d\). Formula (C18) becomes the usual \((2\pi)^{-d}\) kernel normalization, and the amplitude order is the operator order. Under \(N^*\Delta\simeq T^*X\), the cotangent symplectic density supplies \(|dx|^{1/2}|d\xi|^{1/2}\), of fiber degree \(d/2=n/4\). Multiplying the ordinary operator symbol by it gives (C21). A general conormal bundle has no such specified canonical half-density that would turn its symbols into scalar functions.

## 7. Full action on amplitudes, not only leading symbols

Let \(P=p(x,D)\) have left symbol of order \(d\), and let \(u\) have the normalized reduced amplitude \(a(z,\tau)\) of (C18), of order \(r=m+(n-2k)/4\). Work first with compact input and output localization in one chart: the exact left symbol \(p\) is extended globally with compact base support, and \(a\) is the global reduced amplitude of the compactly localized input from Section 2. Thus both factors have global symbol bounds. The output amplitude of this localized operator and input is
\[
b(z,\tau)=
\left[
\exp\big(i\langle D_w,D_\eta\rangle-i\langle D_t,D_\tau\rangle\big)
\{p(t,z,\tau,\eta)a(w,\tau)\}
\right]_{w=z,\ t=0,\ \eta=0}.
\tag{C22}
\]
The exponential means successive quadratic-multiplier restriction as below. Every truncation before total degree \(N\) has remainder in \(S^{d+r-N}\), with all base/frequency derivatives and finite-seminorm control. In particular
\[
\sigma(Pu)=\sigma(P)|_{N^*Y}\,\sigma(u).
\tag{C23}
\]

For Schwartz inputs, insert the Fourier transform of (C18) into the left quantization integral. Tangential Fourier inversion first gives the full amplitude
\[
a_1(t,z,\tau)=(2\pi)^{-(n-k)}
\iint e^{i(z-w)\cdot\eta}p(t,z,\tau,\eta)a(w,\tau)\,dw\,d\eta.
\]
This is the first quadratic multiplier in (C22), evaluated at \(w=z,\eta=0\). Its estimates follow directly from [Quadratic Fourier multipliers at a moving scale](gauss-transform-estimates.md), including the passive variables. On the space of \((x,w,\tau,\eta)\), use
\[
G=|dx|^2+|dw|^2+\langle\tau\rangle^{-2}|d\tau|^2
+\langle(\tau,\eta)\rangle^{-2}|d\eta|^2,
\quad M=\langle(\tau,\eta)\rangle^d\langle\tau\rangle^r.
\tag{C24}
\]
The product symbol obeys these derivative bounds: derivatives of \(p\) in \(\tau\) cost at most \(\langle\tau\rangle^{-1}\), and those of \(a\) have exactly that cost. Small metric displacements preserve both brackets, so slow variation and local weight comparison hold. For the phase \(\langle D_w,D_\eta\rangle\), a finite phase distance keeps \((x,\tau)\) fixed. Relative to an observation point with \(\eta=0\), the \(\eta\)-part of \(G\) at any input point is no larger, while the remaining parts agree. The weight ratio is bounded by a power of \(1+|\eta|^2\), which the phase-dual distance controls. Thus the full hypotheses of the Gauss restriction theorem hold uniformly along \(w=z,\eta=0\). When \(n-k>0\), the parameter is \(1/(2\langle\tau\rangle)\). When \(k=n\), there are no tangential variables: this first reduction is ordinary multiplication, its phase and actual Gauss parameter are zero, and the zero-phase branch of Section 8 of [Quadratic Fourier multipliers at a moving scale](gauss-transform-estimates.md) applies. It gives \(a_1\in S^{d+r}\) and every remainder order \(d+r-N\), including parameter derivatives.

Now remove the normal base dependence of \(a_1\) by (C5). This gives the second multiplier and (C22). The constant-coefficient differential operators commute before restriction. Expanding the two finite Taylor polynomials and collecting terms of total degree less than \(N\) gives the stated single exponential expansion; each contraction lowers the order by one, and the discarded finite terms and both controlled remainders have order at most \(d+r-N\).

For general symbols, take bounded compactly supported approximants. The oscillatory definition, the two weak Gauss extensions, and the Schwartz action of ordinary \(S_{1,0}\) operators and their adjoints pass the equality to distributions. Explicitly, adjoints applied to a fixed Schwartz test function converge in Schwartz space: the classical estimates from Section 8 of [Two measuring scales, one Weyl product](weyl-metric-products.md) bound all output seminorms uniformly, local smooth convergence follows by dominated oscillatory integration, and a higher uniform decay seminorm controls the tails. Pair this convergence with the bounded, distributionally convergent input approximants. For the original local operator, proper support permits a compact input cutoff equal to one at all kernel input points over a fixed output compact set. Use a compact output cutoff equal to one on its working neighborhood. Splitting into chart pieces near the diagonal then gives the globally extended symbols just used. The remaining kernel pieces are separated from the diagonal, so frequency integration by parts makes their outputs smooth there; after compact output localization their normal Fourier transforms are \(S^{-\infty}\) amplitudes and are included in the local representation. This gives equality on the working neighborhood and every claimed local remainder without imposing growth at infinity on the original symbols. All estimates are componentwise, and (C20) glues the leading term, proving (C23) for bundle operators.

If the amplitudes and operator symbols have complex polyhomogeneous expansions in steps \(h=1/q\), \(q\) a positive integer, every coordinate and action formula above preserves that expansion. A frequency derivative lowers degree by an integer, which is \(q\) steps; multiplying homogeneous components adds their step indices. At each specified degree only finitely many indices contribute, and the remainder estimates just proved justify truncation. A common reciprocal-integer step may be chosen for two different such expansions. The boundary theory below uses step one, with degrees \(m-j\); its phase formulas are not assertions for arbitrary noninteger steps.

## 8. What a normal-frequency tail does on one side

From here on the normal variable is one dimensional, and the interior is \(t>0\). Smoothness up to the boundary means restriction of a smooth function on a neighborhood of the closed half-space, locally in the other variables. We first establish a Fourier test that includes complex powers and logarithmic exceptions.

The entire family of supported distributions
\[
e_\lambda(t)=\frac{t_+^{\lambda-1}}{\Gamma(\lambda)},\qquad
\partial_t e_\lambda=e_{\lambda-1},\qquad
e_0=\delta,
\quad e_{-j}=\delta^{(j)}
\tag{T1}
\]
is initially defined by the integral when \(\operatorname{Re}\lambda>0\). Here is a construction at the remaining parameters. In its pairing with a test function subtract a Taylor polynomial at zero inside a cutoff. The subtracted integral converges on successively larger left half-planes; the integrals of the subtracted powers give simple poles at the nonpositive integers. These are precisely canceled by \(1/\Gamma(\lambda)\). Integration by parts proves the derivative identity on the initial half-plane and then on every continuation. At \(\lambda=1\) this is the Heaviside distribution, so differentiation gives the last two identities. This proves the asserted distributional normalization, rather than assigning a value to a divergent power integral.

The elementary properties of \(\Gamma\) used here can be obtained from its Euler integral. Integrating the beta integral repeatedly gives
\(\int_0^1 s^{z-1}(1-s)^Nds=N!/[z(z+1)\cdots(z+N)]\).
After the substitution \(s=y/N\), dominated convergence gives the usual product limit for \(\Gamma(z)\) when \(\operatorname{Re}z>0\). Taking logarithms of its factors, and subtracting their linear terms, leaves a uniformly convergent series on compact sets avoiding the nonpositive integers. Thus the continued function has no zeros; its only poles are simple, and the recursion \(\Gamma(z+1)=z\Gamma(z)\) gives residue \((-1)^j/j!\) at \(-j\). These facts justify the cancellations above.

Laplace damping and the Euler integral give, in our Fourier convention,
\[
\widehat {e_\lambda}(\tau)
=\lim_{\epsilon\downarrow0}(\epsilon+i\tau)^{-\lambda}.
\tag{T2}
\]
First prove this for \(\operatorname{Re}\lambda>0\) by integrating \(e^{-(\epsilon+i\tau)t}t^{\lambda-1}\). Passage to distributions follows by pairing with a Schwartz function and dominated convergence on the original \(t\)-integral. Differentiation and the continuation construction then give all \(\lambda\). On the positive and negative frequency rays the values in (T2) have ratio \(e^{i\pi\lambda}\). They are the boundary values of a homogeneous holomorphic function in the lower half-plane. Reflection in \(t\) gives the corresponding upper-half-plane function and a distribution supported in \(t\leq0\).

For a more explicit smoothness test, let a frequency function have homogeneous tails
\(c_+\tau^v\) for \(\tau>0\) and \(c_-|\tau|^v\) for \(\tau<0\), cut off near zero. The singular part on \(t>0\) of its inverse oscillatory integral *without* the inverse Fourier coefficient is
\[
\Gamma(v+1)
\big[c_+e^{i\pi(v+1)/2}+c_-e^{-i\pi(v+1)/2}\big]
t^{-v-1}.
\tag{T3}
\]
For \(\operatorname{Re}v>-1\), insert \(e^{-\epsilon|\tau|}\) on the two rays, apply the Euler integral, and let \(\epsilon\downarrow0\) at a fixed \(t>0\). Removing the low-frequency part changes the answer by a smooth function. Both this cutoff tail and its distributional inverse depend holomorphically on \(v\) on each vertical strip. Taylor subtraction at frequency zero therefore continues the displayed expression; any polar subtractions have inverse transforms that are polynomials in \(t\), hence smooth.

Away from negative integers, (T3) has a nonsmooth coefficient unless its bracket vanishes. That vanishing is exactly
\[
c_-=e^{i\pi v}c_+.
\tag{T4}
\]
At \(v=-\ell\), \(\ell=1,2,\ldots\), put \(v=-\ell+w\) and expand \(t^{-w}=1-w\log t+O(w^2)\). If \(B(v)\) denotes the bracket in (T3), the nonsmooth term is
\[
-\frac{(-1)^{\ell-1}}{(\ell-1)!}
B(-\ell)t^{\ell-1}\log t.
\tag{T5}
\]
It vanishes precisely under (T4) again. Terms arising from differentiating \(B\), or from the finite part of \(\Gamma\), are multiples of \(t^{\ell-1}\) and are smooth. Thus the exceptional integral exponents do not create an exception to the phase test; they replace a power singularity by a logarithm.

Suppose now that \(b(z,\tau)\) is polyhomogeneous of complex degree \(v\), with components \(b_j\) of degree \(v-j\). Then
\[
\int e^{it\tau}b(z,\tau)d\tau\text{ is smooth up to }t=0+
\quad\Longleftrightarrow\quad
b_j(z,-1)=e^{i\pi(v-j)}b_j(z,1)
\text{ for every }j.
\tag{T6}
\]
These conditions also say that every homogeneous component extends holomorphically to the upper half-plane: use \(b_j(z,1)\zeta^{v-j}\) with \(0\leq\arg\zeta\leq\pi\).

To verify that the expansion proves the equivalence, a remainder of order \(\operatorname{Re}v-N\) has a \(C^q\) inverse integral whenever \(N>\operatorname{Re}v+q+1\), by absolute integration after up to \(q\) derivatives. If every condition holds, (T3)–(T5) and this estimate give arbitrary regularity. Conversely take the first component violating (T4). If its power is \(t^\lambda\), where \(\lambda=-v+j-1\) is not a nonnegative integer, choose an integer \(q>\operatorname{Re}\lambda\). Differentiate \(q\) times and multiply by \(t^{q-\lambda}\). Smooth terms tend to zero; every later singular term tends to zero because it has an additional positive integer power of \(t\); the first term tends to its nonzero coefficient times \(\lambda(\lambda-1)\cdots(\lambda-q+1)\). Choose the truncation remainder to be \(C^q\). This contradicts smoothness. For a logarithm \(t^{\ell-1}\log t\), differentiate \(\ell\) times and multiply by \(t\); exactly the first logarithm has a nonzero limit. The same argument after tangential differentiation is uniform on compact sets. In particular a power with nonzero imaginary part and integer real part is covered: its critical derivative oscillates, and is not silently treated as a smooth integer power.

We will also use two elementary extension facts. Arbitrary smooth boundary jets \(f_j(z)\) are realized by a smooth function. Locally, sum
\(\chi(t/\epsilon_j)t^j f_j(z)/j!\), where \(\chi=1\) near zero. Choose \(\epsilon_j\downarrow0\) so that the \(j\)-th term has every prescribed compact \(C^N\) seminorm at most \(2^{-j}\) for \(N\leq j/2\); this is possible because its bound contains \(\epsilon_j^{j-N}\). The finitely many small indices are harmless, all derivative series converge, and the desired jets follow at zero. Exhausting tangential compact sets and then using a partition of unity proves the full assertion. Second, if all derivatives of a function on \(t>0\) have continuous one-sided limits, it is smooth up to the boundary. The fundamental theorem of calculus, using bounded next normal derivatives, proves existence and compatibility of these jets; the preceding construction supplies matching jets on \(t<0\). Their difference is flat at zero, so gluing gives a smooth extension.

## 9. Supported powers and the spaces of complex type

Let \(\overline Y\) be a smooth manifold with boundary inside a smooth ambient manifold \(X\). In this boundary discussion \(Y\) denotes its interior. For a complex number \(\mu\), define
\[
C_\mu^\infty(\overline Y;E)
=\{u\in I_{\mathrm{phg}}^{\mu-(n-2)/4}(X,\partial Y;E):
\operatorname{supp}u\subset\overline Y\}.
\tag{T7}
\]
The order refers to a step-one polyhomogeneous normal form and its real-part estimates. Smooth terms supported in \(\overline Y\) are included. In a boundary chart the normal amplitude has degree \(\mu\). By (T6) applied on the negative side, its homogeneous coefficients satisfy
\[
a_j(z,-1)=e^{-i\pi(\mu-j)}a_j(z,1).
\tag{T8}
\]
Conversely these relations allow an expansion by distributions supported on the positive side; a general amplitude satisfying them has a smooth inverse on the negative side, and subtracting a smooth extension of that part produces a supported representative with the same asymptotic coefficients. Formula (T2) gives a supported representative of each homogeneous term directly. In particular every smooth leading coefficient in the bundle fiber can be prescribed independently: multiply \(e_{-\mu}(t)\) by that coefficient and by a cutoff equal to one near zero. Its Fourier leading coefficient on the positive ray is \(e^{i\pi\mu/2}\), which never vanishes, so rescaling gives the desired normalization.

The space (T7) does not depend on the ambient extension of a boundary chart. The conormal change-of-coordinate proof in Section 6 gives the same polyhomogeneous class under any smooth extension, and support is intrinsic. Equivalently the local description just given glues by the bundle transition law. This treats arbitrary smooth vector bundles; finite-order Taylor coefficients and all constructions are taken componentwise in a frame.

Here is a concrete description of all its members, not only their leading terms:

* If \(\mu\notin\mathbb Z\), they have expansions
  \(\sum_{j\geq0}u_j(z)t_+^{j-\mu-1}\), with these powers interpreted by distributional continuation. After sufficiently many terms the remainder has any prescribed finite smoothness.
* If \(\mu\leq-1\) is an integer, they are exactly the zero extensions of smooth functions on \(\overline Y\) whose normal jets of orders less than \(-\mu-1\) vanish.
* If \(\mu\geq0\) is an integer, they are exactly a zero extension of a smooth function plus a finite sum \(\sum_{j=0}^{\mu}v_j(z)\delta^{(j)}(t)\), locally at the boundary.

To prove these descriptions, match successive Fourier coefficients using \(e_{j-\mu}\) in (T1)–(T2). Multiplication by a normal cutoff changes each Fourier expansion by lower terms only, which are matched successively; equivalently its cutoff is constant near the entire singular support, so the complementary part has a rapidly decreasing Fourier transform after compact localization. The difference after \(N\) terms has amplitude order \(\operatorname{Re}\mu-N\), hence is \(C^q\) for \(N>\operatorname{Re}\mu+q+1\). When \(\mu\) is not an integer, the gamma factors are nonzero and are absorbed in the coefficients of the stated powers. At integer \(\mu\), (T1) gives precisely the listed delta derivatives and nonnegative powers on the positive side. The smooth jet construction at the end of Section 8 realizes the latter coefficients by one smooth function on \(\overline Y\). The remaining amplitude is of every negative order, so its inverse is smooth; support makes it flat on the boundary. This proves exact membership statements, including their converses. One can also realize arbitrary infinite power expansions by multiplying the \(j\)-th term by a shrinking cutoff: the same \(2^{-j}\) construction is applied in successively weaker symbol orders, and then in each fixed finite distributional seminorm. This gives all the asserted asymptotic remainders.

For clarity, if \(f\) is smooth up to \(t=0\), compactly supported in a boundary chart, and \(f_0\) is its zero extension, its normal Fourier transform is
\[
\widehat {f_0}(z,\tau)=\int_0^\infty e^{-it\tau}f(t,z)dt
\sim-i\sum_{j\geq0}\tau^{-1-j}D_t^j f(0,z).
\tag{T9}
\]
Integrating by parts \(N\) times proves this expansion and its remainder. To differentiate it in \(\tau\), apply the same integration by parts to \((-it)^\alpha f\); its vanishing jets give the extra \(\alpha\) powers of decay. Tangential derivatives commute with the integral. Consequently (T9) is a full symbol expansion of degree \(-1\). The reduced amplitude in (C4) is \((2\pi)^{-1}\widehat {f_0}\), so the conormal order is exactly \(-(n+2)/4\), and these inputs form \(C_{-1}^\infty\). Arbitrary jets in (T9) can be prescribed by the smooth extension construction; two such amplitudes with identical jets differ by \(S^{-\infty}\).

For each integer \(N\geq0\), \(C_{\mu-N}^\infty\subset C_\mu^\infty\). Smooth multiplication preserves \(C_\mu^\infty\), by (C5) and support; a first-order derivative maps it into \(C_{\mu+1}^\infty\), by (C22) or direct differentiation of the power family. Tangential derivatives in a fixed boundary chart actually preserve its normal order. These inclusions will let us recover every jet in a transmission condition from an operator mapping property.

## 10. All jets are necessary, at every complex type

Let \(P:E\to F\) be properly supported, with a classical full left symbol
\(p\sim\sum_{j\geq0}p_j\), where \(p_j\) is homogeneous of complex degree \(m-j\). We say that \(P\) has transmission of type \(\mu\) into \(Y\) if \(Pu|_Y\) is smooth up to the boundary for every \(u\in C_\mu^\infty(\overline Y;E)\). The ordinary transmission property means that zero extensions of arbitrary smooth functions have this property; it is type \(-1\), or equivalently the phase type zero. Proper support is the hypothesis ensuring these local distributions can be acted on without a global compact-support restriction.

The complete criterion is, for every \(j\), every pair of multi-indices \(\alpha,\beta\), and every boundary point,
\[
(\partial_x^\beta\partial_\xi^\alpha p_j)(0,z,-1,0)
=e^{i\pi(m-j-|\alpha|+2\mu)}
(\partial_x^\beta\partial_\xi^\alpha p_j)(0,z,1,0).
\tag{T10}
\]
It is an equality of maps between the bundle fibers. In particular it includes every normal base jet and every tangential frequency jet, not just the two values of the leading symbol.

We first prove sufficiency. Apply the full amplitude formula (C22) to a supported input. Each homogeneous output term is a finite sum of products of a base/frequency derivative of some \(p_j\), of frequency degree \(d_p\), with a derivative of an input coefficient, of normal degree \(d_a=\mu-r\), \(r\) an integer. At the two normal rays, (T10) gives the first factor the ratio \(e^{i\pi(d_p+2\mu)}\); (T8), including its differentiated version, gives the second the ratio \(e^{-i\pi d_a}\). Their product is
\(e^{i\pi(d_p+2\mu-d_a)}=e^{i\pi(d_p+d_a)}\), because \(\mu-d_a\) is an integer. Matrix multiplication has the same scalar phase and preserves its order. Thus each output coefficient obeys the upper-half-plane relation in (T6). All remainder orders in (C22) are available, so (T6) proves the desired smoothness with all derivatives. Localizing and summing in charts proves it globally.

For necessity, first prescribe an arbitrary leading input coefficient using (T2). The leading output coefficient is the product \(p_0(0,z,\tau,0)a_0(z,\tau)\). Its upper-half-plane relation and the input's lower-half-plane relation give
\(p_0(0,z,-1,0)=e^{i\pi(m+2\mu)}p_0(0,z,1,0)\).
Arbitrary input vectors prove the entire matrix equality.

Next recover every derivative of \(p_0\). A commutator with multiplication by a coordinate has full symbol a fixed nonzero constant times the corresponding frequency derivative; a commutator with \(D_{x_i}\) has full symbol \(D_{x_i}p\). These are exact local identities obtained by differentiating the Fourier kernel; coordinate cutoffs equal to the coordinates near the point only add locally smooth kernels. Therefore an iterated commutator has full symbol a nonzero constant times \(\partial_x^\beta\partial_\xi^\alpha p\), with leading degree \(m-|\alpha|\).

Although derivatives need not preserve a particular \(C_\mu^\infty\), this commutator still has the required mapping property on a sufficiently smaller such space. Expand its finite nested commutator as a sum of words with one occurrence of \(P\). If \(N\) is at least the total number of first-order differential factors, every word to the right of \(P\) takes \(C_{\mu-N}^\infty\) into \(C_\mu^\infty\); every word to its left preserves smoothness on the interior up to the boundary. The preceding leading-coefficient argument therefore applies to this commutator with input parameter \(\mu-N\). Since \(e^{2\pi i(\mu-N)}=e^{2\pi i\mu}\), it gives exactly (T10) for \(p_0\) and all \(\alpha,\beta\).

Finally pass through all lower homogeneous degrees. Choose a frequency cutoff equal to one near infinity and properly quantize the single homogeneous symbol \(p_0\). Its sole homogeneous component satisfies every condition just proved, so the already established sufficiency shows that this operator has the mapping property. A cutoff of the kernel near the diagonal makes it proper and changes its local full symbol only by \(S^{-\infty}\), as follows by integration by parts off that diagonal. Subtract it from \(P\). The remainder has order \(m-1\) and the same mapping property. Apply the leading argument and the commutator argument to this remainder to obtain every jet of \(p_1\). Induction gives every \(p_j\), proving necessity in full.

The proof also shows why testing only functions with a fixed finite order of boundary vanishing still detects ordinary transmission. Such tests form \(C_{-1-N_0}^\infty\) for a fixed nonnegative integer \(N_0\). The phase is unchanged. In the commutator step choose inputs in still smaller \(C_{-1-N}^\infty\), so every right-hand word remains among the permitted tests. The same subtraction induction recovers all jets of all homogeneous terms. Finite boundary vanishing therefore cannot remove a failed transmission jet.

### 10.1. An equivalent family of boundary tests

The full condition (T10) can be checked using fewer separately prescribed derivatives, while recovering every jet. Keep the original homogeneous maps \(p_j\), complex orders \(m,\mu\), coordinates \(x=(t,z)\), \(\xi=(\tau,\eta)\), and both points \((0,z,\pm1,0)\). Then (T10) is equivalent to the following identities, for every \(j\geq0\), normal base order \(b\geq0\), tangential frequency multi-index \(a\), and every boundary point \(z\):
\[
 (\partial_t^b\partial_\eta^a p_j)(0,z,-1,0)
 =e^{i\pi(m-j-|a|+2\mu)}
   (\partial_t^b\partial_\eta^a p_j)(0,z,1,0).
 \tag{TJ1}
\]
The equality is between the same bundle fibers in a fixed smooth frame. It must hold at every boundary point, so it can be differentiated in every tangential base direction. This does not discard any base jet.

**Proof of the exact equivalence.** Fix a tangential base multi-index \(d\), and write
\[
 g(\tau)=(\partial_z^d\partial_t^b\partial_\eta^a p_j)(0,z,\tau,0),
 \qquad v=m-j-|a|.
 \tag{TJ2}
\]
Differentiating the original homogeneity law in \(\eta\) contributes exactly the factor \(s^{-|a|}\); base differentiation leaves the degree unchanged. Hence, for every real \(s>0\),
\[
 g(s)=s^v g(1),\qquad g(-s)=s^v g(-1),
 \qquad s^v=\exp(v\log s).
 \tag{TJ3}
\]
There is no branch change in this positive real logarithm. Repeated differentiation on each open ray gives, for every integer \(c\geq0\),
\[
 g^{(c)}(1)=(v)_c g(1),\qquad
 g^{(c)}(-1)=(-1)^c(v)_c g(-1),\qquad
 (v)_c=\prod_{r=0}^{c-1}(v-r),\quad(v)_0=1.
 \tag{TJ4}
\]
The negative-ray sign follows at each differentiation from \(s=-\tau\). Differentiating (TJ1) in \(z\), substituting it into (TJ4), and retaining the entire falling factorial yields
\[
 g^{(c)}(-1)=(-1)^c(v)_c e^{i\pi(v+2\mu)}g(1)
           =e^{i\pi(v-c+2\mu)}g^{(c)}(1).
 \tag{TJ5}
\]
The scalar phases agree because their quotient is \(e^{2\pi i c}=1\). If any factor in \((v)_c\) is zero, both sides vanish; no division by that product has occurred. Set \(\alpha=(c,a)\), \(\beta=(b,d)\). Then \(|\alpha|=c+|a|\), and (TJ5) is exactly (T10) for those original indices. They range over every required derivative. Conversely (T10), restricted to \(c=0,d=0\), gives (TJ1). This proves both implications, for complex \(m,\mu\), all matrix entries and dimension one, where \(a,d\) are empty multi-indices. The previously proved mapping property, invariant reflection and all higher trace consequences therefore receive precisely the same full jets.

**Human source and parameter correspondence.** [Gerd Grubb, *Fractional Laplacians on domains*, arXiv 1310.0951v5, October 1, 2014](https://arxiv.org/abs/1310.0951v5), Theorem 2.6, equations (2.11), (2.17), and the paragraph immediately following its proof, already gives this equivalent family. This is an explicit proof of that criterion. Her supported-power exponent \(\nu\) corresponds to \(\nu=-\mu-1\) here: her distribution \(I^\nu=t_+^\nu/\Gamma(\nu+1)\) is exactly \(e_{\nu+1}=e_{-\mu}\) from (T1), initially where the integral converges and then by the same derivative continuation. Its integer delta terms and lower-half-plane branch are retained. The source phase becomes
\[
 e^{i\pi(m-2\nu-j-|\alpha|)}
 =e^{i\pi(m+2\mu+2-j-|\alpha|)}
 =e^{i\pi(m-j-|\alpha|+2\mu)}.
 \tag{TJ6}
\]
The last equality records the full factor \(e^{2\pi i}=1\). Thus the comparison identifies the original supported distributions as well as every phase and index; it does not replace the course's symbols or proofs.

**Editorial correction to one source integral.** In the proof of Grubb's Lemma 2.7, the displayed \(\sigma=-2\) calculation omits \(i\) and uses the wrong transformed lower endpoint. This source-only error is already avoided in Problem 3. Retain both boundary values and the entire original integral. For \(t>0\),
\[
 \begin{split}
 \int_{|\tau|>1}e^{it\tau}(\tau^\pm)^{-3}|\tau|\,d\tau
 &=\int_1^\infty\tau^{-2}(e^{it\tau}-e^{-it\tau})\,d\tau\\
 &=2i\int_1^\infty\tau^{-2}\sin(t\tau)\,d\tau
 =2it\int_t^\infty s^{-2}\sin s\,ds.
 \end{split}
 \tag{TJ7}
\]
On the negative ray both branches contribute \(-|\tau|^{-2}\), since \(e^{\pm3\pi i}=-1\). Both original integrals converge absolutely. The substitution \(s=t\tau\) has \(d\tau=ds/t\), giving the factor \(t\) and lower endpoint \(t\). For \(0<t<1\), the last integral is
\[
 \int_t^\infty s^{-2}\sin s\,ds
 =-\log t+C-\int_0^t\frac{\sin s-s}{s^2}\,ds,
 \quad C=\int_0^1\frac{\sin s-s}{s^2}\,ds+
             \int_1^\infty\frac{\sin s}{s^2}\,ds.
 \tag{TJ8}
\]
The first integrand extends analytically to zero, with value zero, and the second integral converges absolutely. Consequently the complete singular contribution is \(-2it\log t\), with the remaining term smooth at zero. The source's conclusion that this example has a nonzero logarithmic term survives. Neither this correction nor (TJ1) changes the already valid full-jet theorem.

## 11. The invariant reflection of a classical operator

For an operator of fixed complex order \(m\), define, modulo smoothing operators,
\[
\widetilde p(x,\xi)\sim
\sum_{j\geq0}e^{-i\pi(m-j)}p_j(x,-\xi).
\tag{T11}
\]
Such a classical symbol exists. To see the asymptotic realization explicitly, multiply the \(j\)-th homogeneous term by \(\chi(\xi/R_j)\), where \(\chi\) vanishes near zero and is one near infinity. Choose \(R_j\to\infty\) so that each later term is at most \(2^{-j}\) in the first \(j\) compact symbol seminorms of order \(\operatorname{Re}m-j/2\). Homogeneity makes this possible; a fixed lower target order only involves finitely many excluded indices. The series then converges with precisely the required remainders. The construction is local in the base and glues by a partition. Two realizations differ by \(S^{-\infty}\). Directly from (T11),
\(\widetilde{\widetilde P}=e^{-2\pi im}P\) modulo smoothing, so \(e^{i\pi m}\widetilde{\phantom P}\) is an involution when the order label \(m\) is fixed.

We prove that (T11) is intrinsic. Here are the needed full coordinate estimates, including their remainder. For a coordinate change \(\kappa\), write near the diagonal
\(\kappa(x)-\kappa(y)=\Psi(x,y)(x-y)\), using the integral of its derivative along the segment. The matrix \(\Psi\) is invertible on a sufficiently small diagonal neighborhood. Choose a compact base cutoff \(\chi(x,y)\) supported there and equal to one near the working diagonal; extend the resulting amplitude by zero. Pullback of this localized operator kernel and the change \(\eta=\Psi(x,y)^T\theta\) give the global amplitude
\[
A(x,y,\eta)=\chi(x,y)p(\kappa(x),\Psi(x,y)^{-T}\eta)
\frac{|\det\kappa'(y)|}{|\det\Psi(x,y)|}
\tag{T12}
\]
for functions. For half-densities the numerator is
\(|\det\kappa'(x)\det\kappa'(y)|^{1/2}\); frame changes insert the corresponding smooth matrices on the two sides. All these extra factors have frequency degree zero. Each base derivative falling on \(\Psi^{-T}\eta\) brings a linear frequency factor paired with a symbol derivative, so \(A\) has order \(m\) with all amplitude estimates.

Its left symbol is the reduction
\([ e^{i\langle D_y,D_\eta\rangle}A(x,y,\eta)]_{y=x}\), with expansion
\(\sum_\alpha\partial_\eta^\alpha D_y^\alpha A(x,x,\eta)/\alpha!\) and remainder of order \(\operatorname{Re}m-N\) after \(|\alpha|<N\). For Schwartz amplitudes this follows by inserting the Fourier kernel and Fourier inversion; the sign also follows by moving \((y-x)^\alpha\) from a Taylor expansion onto the frequency derivative of the amplitude. For general amplitudes it is the same Gauss restriction as (C5), with the opposite sign and passive \(x\), metric \(|dy|^2+\langle\eta\rangle^{-2}|d\eta|^2\), and parameter \(1/(2\langle\eta\rangle)\). Thus [Quadratic Fourier multipliers at a moving scale](gauss-transform-estimates.md) supplies every finite-seminorm remainder and the weak extension. A cutoff away from the diagonal gives a smooth kernel by repeated frequency integration by parts. This proves the full local coordinate formula needed here: all derivatives of the cutoff vanish on the working diagonal, and its value there is one. The discarded kernel pieces are smooth on the working chart and give smoothing symbol terms.

Let \(A_j\) be the homogeneous component of (T12) of degree \(m-j\). A reduced term with index \(\alpha\) has degree \(m-j-|\alpha|\). Reflecting the reduced term with (T11) supplies the factor \(e^{-i\pi(m-j-|\alpha|)}\). Reflecting \(p_j\) first supplies \(e^{-i\pi(m-j)}\); differentiating \(A_j(x,y,-\eta)\) supplies \((-1)^{|\alpha|}\). These factors agree. All remainders can be taken arbitrarily low, so (T11) commutes with coordinates, density choices and bundle frames modulo smoothing.

It is useful also to check the algebra statement. Apply the same compact chart cutoffs and global extensions before each reduction, retaining the smooth off-diagonal pieces as smoothing terms. For local left symbols the full product and adjoint expansions are
\[
p\circ q\sim\sum_\alpha\frac{\partial_\xi^\alpha p\,D_x^\alpha q}{\alpha!},
\qquad
p^{\mathrm{adj}}\sim\sum_\alpha
\frac{\partial_\xi^\alpha D_x^\alpha p^*}{\alpha!}.
\tag{T13}
\]
The first formula follows by inserting two kernels: the remaining integral is
\((2\pi)^{-n}\iint e^{i(x-y)\cdot\eta}p(x,\xi+\eta)q(y,\xi)dy\,d\eta\).
The tangential reduction argument in Section 7, with \(\xi\) as its retained frequency, gives the expansion and remainder of order \(\operatorname{Re}(m+m')-N\). The adjoint kernel has amplitude \(p(y,\xi)^*\); the reduction just proved gives its formula and remainder of order \(\operatorname{Re}m-N\). Schwartz identities pass to proper classical operators on distributions by the same Schwartz-adjoint convergence argument used after (C24). Thus these formulas do not assume the unresolved general-metric operator-composition extension.

For a product term with component indices \(j,l\), reflection contributes
\(e^{-i\pi(m+m'-j-l-|\alpha|)}\), equal to the two separate reflection factors times \((-1)^{|\alpha|}\). Hence reflection is multiplicative with the summed order label. In the order-zero algebra its factors are the real numbers \((-1)^j\); the same calculation in the adjoint formula gives \(\widetilde{P^{\mathrm{adj}}}=(\widetilde P)^{\mathrm{adj}}\). Therefore it is an involution of that algebra commuting with adjoints, all modulo smoothing. No such unqualified adjoint assertion is made for an arbitrary complex order label.

Call a symbol flat on a conic submanifold when every derivative of every homogeneous component vanishes there. Differentiating (T11) shows that (T10) is equivalently
\[
\widetilde p-e^{2\pi i\mu}p
\text{ is flat on the inward conormal ray of }\partial Y.
\tag{T14}
\]
On the outward ray the equivalent expression is
\(e^{-2\pi i(m+\mu)}p-\widetilde p\). This follows either by reflecting (T14) twice or by reversing the two rays in (T10). In particular type depends only on \(\mu\) modulo \(\mathbb Z\). For the opposite side, a type \(\mu'\) is guaranteed by the same relations if
\[
m+\mu+\mu'\in\mathbb Z.
\tag{T15}
\]
Indeed its desired phase is the inverse of (T10), and their product is \(e^{2\pi i(m+\mu+\mu')}\). For complex parameters this equals one exactly when the sum is a real integer. This is a sufficient equivalence of the two systems of jet conditions; an operator whose relevant jets all vanish may of course satisfy more than one otherwise distinct type condition. In particular ordinary transmission is independent of the side for integer-order operators. Formula (T14) and the intrinsic mapping characterization prove invariance under boundary charts and arbitrary bundle trivializations.

## 12. A normal integral defined by analytic subtraction

Boundary symbols require an integral even when the normal symbol grows. We define the needed value without treating a divergent real integral as an ordinary integral.

Let \(q\) be continuous on the real line. Suppose that for some \(R>0\) there is a function \(Q\), holomorphic in the upper exterior \(\{\operatorname{Im}\zeta>0,|\zeta|>R\}\), continuous on its boundary, of at most polynomial growth there, and such that \(q(t)-Q(t)=O(|t|^{-2})\) on the two tails. Put
\[
\begin{split}
\mathcal I_+(q)={}&
\int_{|t|>R}(q(t)-Q(t))dt+\int_{-R}^{R}q(t)dt\\
&-\int_{\pi}^{0}Q(Re^{i\theta})Ri e^{i\theta}d\theta.
\end{split}
\tag{T16}
\]
The inner arc in this formula runs clockwise from \(-R\) to \(R\). Changing \(R\) changes the two real integrals by precisely the integral over the boundary of an upper half-annulus; Cauchy's theorem cancels the difference.

To prove independence of \(Q\), their difference \(H\) is holomorphic in an upper exterior, polynomially bounded, and \(O(|t|^{-2})\) on the real tails. Apply the maximum principle on this domain to
\(\zeta^2H(\zeta)(1-i\epsilon\zeta)^{-M}\), with \(M\) larger than the polynomial growth degree plus two. It tends to zero at infinity for each \(\epsilon>0\). On the real tails it is uniformly bounded, since \(|1-i\epsilon t|\geq1\), and on the fixed inner arc it has a bound independent of \(0<\epsilon\leq1\), since \(|1-i\epsilon\zeta|\geq1\) throughout the upper half-plane. Taking first the outer radius to infinity and then \(\epsilon\downarrow0\) proves \(|H(\zeta)|\leq C|\zeta|^{-2}\) in that upper exterior. Cauchy's theorem now applies with a vanishing outer-arc integral. Its conclusion is
\(\int_{|t|>R}H(t)dt+\int_\pi^0H(Re^{i\theta})Ri e^{i\theta}d\theta=0\), exactly the independence required in (T16).

There is a parameter version with no lost endpoint. Let \(F(\zeta,s)\) be bounded and jointly continuous on the closed upper half-plane times a parameter space, and holomorphic in \(\zeta\) in the open half-plane. Then \(QF\) is admissible for \(qF\), and
\(s\mapsto\mathcal I_+(qF(\cdot,s))\) is continuous. The tail of (T16) is dominated by a fixed integrable multiple of \(|q-Q|\), while the interval and arc are compact; dominated convergence proves the statement. Uniform bounds on a compact parameter set suffice, and the same argument permits derivatives whenever the differentiated tails have the corresponding common bound.

For a rational function without real poles, take \(R\) beyond every pole and take \(Q=q\) in that exterior. The two finite pieces of (T16) form the positively oriented boundary of the upper half-disk. Therefore
\[
\mathcal I_+(q)=2\pi i
\sum_{\operatorname{Im}\zeta>0}\operatorname{Res}_{\zeta}q.
\tag{T17}
\]
This includes rational functions with polynomial growth. For example \(\mathcal I_+(t/(t^2+1))=i\pi\), whereas its symmetric real principal value is zero; the two definitions answer different limiting problems.

Alternatively take \(Q\) to be the finite Laurent sum at infinity containing precisely the powers of degree at least \(-1\). The omitted rational tail is \(O(|\zeta|^{-2})\), so this is another admissible subtraction and gives the same value by the independence proof. This alternative often makes (T16) convenient to compute.

If \(q\) is in addition a classical normal symbol, its oscillatory inverse integral at \(t>0\) equals
\(\mathcal I_+(e^{it\cdot}q)\). To verify this carefully, insert \(F_\epsilon(\zeta)=(1-i\epsilon\zeta)^{-M}\), with \(M\) sufficiently large. The damped real integral is absolutely convergent, and an upper contour applied to \(e^{it\zeta}Q(\zeta)F_\epsilon(\zeta)\) gives its value from (T16). Its outer arc tends to zero, since the damping has made the polynomial factor decay faster than \(|\zeta|^{-1}\) and the exponential is bounded in the upper half-plane. The parameter assertion gives the limit of (T16) as \(\epsilon\downarrow0\). On the other hand, integrate the damped real integral by parts in frequency enough times. The derivatives of \(F_\epsilon\) satisfy uniform symbol bounds of the corresponding negative orders; after sufficiently many integrations all resulting terms are integrable with a common bound and converge to the undamped oscillatory definition. The two limits agree. This argument also explains why the upper half-plane is the one appropriate to the interior \(t>0\).

## 13. Boundary traces of every layer order

Assume ordinary transmission, equivalently (T10) with the factor \(e^{2\pi i\mu}=1\). Write \(\xi=(\tau,\eta)\), with \(\tau\) normal and \(\eta\) tangential. For every fixed \(z,\eta\), the full symbol \(p(0,z,\tau,\eta)\) admits an analytic subtraction as in (T16). Indeed Taylor-expand each homogeneous component at the positive normal ray:
\[
p_j(0,z,\tau,\eta)\sim
\sum_\alpha \frac{(\partial_\eta^\alpha p_j)(0,z,1,0)}{\alpha!}
\eta^\alpha\tau^{m-j-|\alpha|}\quad(\tau\to+\infty).
\tag{T18}
\]
On the negative ray its coefficients agree with the upper-half-plane values of these powers by (T10). Choose finitely many terms, for instance all \(j+|\alpha|<N\) with \(N>\operatorname{Re}m+2\), and use the branch \(0\leq\arg\zeta\leq\pi\). Their sum is a suitable \(Q\); the remainder is \(O(|\tau|^{-2})\) on both tails. Taylor's formula and the classical remainders prove this uniformly with any fixed finite set of tangential or base derivatives on compact sets of \((z,\eta)\), by choosing enough terms. The identical statement holds for every normal base derivative of \(p\) at \(t=0\), because the transmission hypothesis contains those jets.

The minimal indicated truncation is also valid: retaining exactly \(j+|\alpha|<2+\operatorname{Re}m\) leaves \(O(|\tau|^{-2})\), since every omitted integer index has real degree at most \(-2\). The larger truncations are useful when derivatives of the remainder are required.

Define
\[
q(z,\eta)=\frac1{2\pi}\mathcal I_+\big(p(0,z,\cdot,\eta)\big).
\tag{T19}
\]
It is a classical tangential symbol of degree \(m+1\), with homogeneous components
\[
q_j(z,\eta)=\frac1{2\pi}\mathcal I_+\big(p_j(0,z,\cdot,\eta)\big),
\qquad \eta\ne0,
\quad \deg q_j=m+1-j.
\tag{T20}
\]
For smoothness away from \(\eta=0\), choose an exterior radius larger than the parameters in a compact \(\eta\)-neighborhood and differentiate (T16), using the uniform remainders in (T18). Rescaling \(\tau\) and the radius together proves the asserted homogeneity, including the extra factor of the scale from \(d\tau\). At small \(\eta\), the full symbol (T19) remains smooth by the same parameter argument applied to the full smooth \(p\); the components (T20) need only be defined away from zero.

If the ambient dimension is one, the boundary is zero dimensional. Formula (T19) then gives the finite-dimensional boundary map directly; there is no nonzero tangential frequency at which (T20) needs to be specified.

Here are the full remainder estimates. On \(|\eta|>1\), no low-frequency cutoff is needed in the homogeneous terms of \(p\), since \(|(\tau,\eta)|>1\). For any integer \(N>\operatorname{Re}m+2\), the remainder \(R_N=p-\sum_{j<N}p_j\) has an absolutely convergent normal integral, and
\[
\left|\partial_z^\beta\partial_\eta^\alpha
\int R_N(0,z,\tau,\eta)d\tau\right|
\leq C\langle\eta\rangle^{\operatorname{Re}m+1-N-|\alpha|}.
\tag{T21}
\]
This follows by integrating the symbol bound
\(C\langle(\tau,\eta)\rangle^{\operatorname{Re}m-N-|\alpha|}\) and setting \(\tau=\langle\eta\rangle s\). Its exponent is less than \(-1\). For this integrable remainder choose \(Q=0\) in (T16), so its plus integral is its ordinary integral. This proves (T21) for the difference in (T19)–(T20). Arbitrarily large \(N\) give the expansion at every requested order; a shorter truncation is that long remainder plus the intervening homogeneous symbols, with precisely its stated order. Thus no finite number of symbol seminorms or remainder orders has been omitted.

We next prove that (T19) actually is the trace of the simple layer. For \(v\) smooth and compactly supported tangentially, set \(u=\delta(t)v(z)\). It belongs to \(C_0^\infty\), whose phase is ordinary transmission, so \(Pu|_{t>0}\) is already known to be smooth up to the boundary. Its local normal-frequency formula away from zero is
\[
Pu(t,z)=(2\pi)^{-n}\int e^{iz\cdot\eta}
\left(\int e^{it\tau}p(t,z,\tau,\eta)d\tau\right)
\widehat v(\eta)d\eta.
\tag{T22}
\]
Only the boundary jets of \(p\), rather than its values for positive \(t\), satisfy (T18). We therefore justify the limit by normal Taylor expansion. For a chosen integer \(L\), write
\[
p(t,z,\xi)=\sum_{l<L}\frac{t^l}{l!}\partial_t^l p(0,z,\xi)
+t^L r_L(t,z,\xi).
\tag{T23}
\]
The remainder is a symbol of the same order, locally uniformly in \(t\). Each frozen coefficient has an analytic subtraction. By Section 12 its oscillatory normal integral is \(\mathcal I_+(e^{it\cdot}\partial_t^l p(0,z,\cdot,\eta))\), continuous down to \(t=0\), with polynomial bounds in \(\eta\). Thus all terms with \(l>0\) tend to zero and the first gives (T19).

For explicit control of the remainder, a symbol \(r\) of fixed order has, away from \(t=0\), the bound
\(\left|\int e^{it\tau}r(t,z,\tau,\eta)d\tau\right|
\leq Ct^{-K}\langle\eta\rangle^M\), \(0<t<1\), for some \(K,M\). This follows by a dyadic partition in \(\tau\): the block of size \(R\) is bounded by a fixed power of \(R\) times a fixed power of \(\langle\eta\rangle\); after \(a\) frequency integrations by parts it has the additional factor \((tR)^{-a}\). Sum blocks below and above \(R=1/t\), choosing \(a\) larger than the growth exponent plus one. A possible logarithm at zero exponent is bounded by a slightly larger power of \(t^{-1}\). The same proof treats any fixed number of derivatives. Crucially these exponents depend on the symbol order and the requested derivative count, not on the Taylor length \(L\); its constants may depend on \(L\). Choose \(L>K\). Then the last term of (T23) tends to zero with a polynomial tangential bound. Taking larger \(L\) after each desired derivative proves all corresponding boundary limits. The rapid decrease of \(\widehat v\) justifies their integration in (T22). Consequently
\[
\left.P(\delta(t)v)\right|_{t=0+}=q(z,D_z)v.
\tag{T24}
\]

One can verify the same trace through genuine smooth layers, which also fixes the distributional meaning of (T22). Choose \(\varphi\in C_c^\infty(-1,1)\), \(\int\varphi=1\), and replace \(\delta\) by \(\varphi_\epsilon(t)=\epsilon^{-1}\varphi(t/\epsilon)\). The inner integral in (T22) acquires \(\widehat\varphi(\epsilon\tau)\). For \(\operatorname{Im}\zeta\geq0\) and \(t\geq\epsilon\),
\(e^{it\zeta}\widehat\varphi(\epsilon\zeta)=\int\varphi(s)e^{i(t-\epsilon s)\zeta}ds\) has modulus at most \(\|\varphi\|_1\). It is holomorphic and jointly continuous, including \((t,\epsilon)=(0,0)\) on compact frequency sets. The parameter lemma therefore gives the uniform frozen-coefficient limit. For the Taylor remainder choose \(a<1\) with \(\operatorname{supp}\varphi\subset[-a,a]\). On the full range \(t\geq\epsilon\), the preceding off-zero estimate applies at distances \(t-\epsilon s\geq(1-a)t\), uniformly in \(s\). Thus its contribution still tends to zero after the chosen \(t^L\) factor. At fixed \(t>0\), the mollified layers converge distributionally and in the displayed smooth off-boundary formula to \(P(\delta v)\). This proves the joint limiting construction and all the tangential derivative bounds used in (T24), with polynomial tangential growth uniformly for \(0\leq\epsilon\leq t\) near zero.

There is no restriction to simple layers. For any integers \(k,l\geq0\), the complete left symbol of \(D_t^kPD_t^l\) is
\[
p_{k,l}(t,z,\tau,\eta)=
\sum_{r=0}^k\binom{k}{r}
(D_t^{k-r}p)(t,z,\tau,\eta)\tau^{r+l}.
\tag{T25}
\]
This is the ordinary Leibniz rule applied to the kernel, and is exact. Its order is \(m+k+l\). Each homogeneous term obeys ordinary transmission: a normal base derivative preserves the phase, and multiplication by \(\tau^{r+l}\) supplies exactly its integer degree parity. Thus the preceding theorem applies to it. The boundary operator
\(v\mapsto[D_t^kP(D_t^l\delta\,v)]_{t=0+}\)
is a classical tangential operator of order \(m+k+l+1\), with full symbol \((2\pi)^{-1}\mathcal I_+(p_{k,l}(0,z,\cdot,\eta))\) and every homogeneous remainder given as above. Normal coefficient derivatives in (T25) affect its lower homogeneous terms and cannot be dropped. All constructions are local and compatible with coordinate and frame changes because they are traces of the intrinsic operators just proved; a partition of unity yields the corresponding layer operators for bundles on a smooth boundary.

## 14. Three models that distinguish the hypotheses

**An endpoint measured by a sequence.** Let \(g\) be a nonzero smooth compactly supported function of \(z\), and set \(u=\delta(t)g(z)\) with \(k\) normal variables. On large frequency annuli its squared Fourier mass is comparable to \(R^k\). The upper estimate follows from (C7); for the lower estimate restrict \(\eta\) to a fixed ball on which \(\widehat g\) has positive squared integral and restrict \(\tau\) to a fixed subannulus of radius \(R\). Thus its dyadic sequence at \(s=-k/2\) is bounded above and below by positive constants. It belongs to \(B^{-k/2}_{2,\infty}\) and to no \(B^{-k/2}_{2,p}\) with finite \(p\); it belongs to every \(H^{-k/2-\epsilon}\), \(\epsilon>0\). The amplitude is order zero, so its intrinsic conormal order is \((2k-n)/4\). These are three compatible facts, not three different conventions for a Sobolev exponent.

**A complex order that distinguishes the two sides.** In one dimension let a classical symbol have homogeneous tails \(p_0(\tau)=\tau^i\) for \(\tau>0\) and \(p_0(\tau)=e^{-\pi}|\tau|^i\) for \(\tau<0\); smooth it near zero and localize its kernel properly. It satisfies ordinary transmission into \(t>0\): the ratio is \(e^{i\pi i}=e^{-\pi}\), and differentiation gives every higher frequency condition. There are no tangential frequencies, and the local symbol is independent of the base, so the other jets vanish. Into the opposite side, ordinary transmission would require \(1=e^{-2\pi}\), which fails. Type \(\mu'=-i\) does work on that side, since \(m+0+\mu'=0\) in (T15). The imaginary part of the type is mathematically active.

**Residues give a boundary operator.** At nonzero tangential frequency put \(a=|\eta|\) and take
\(p(\tau,\eta)=(\tau^2+a^2)^{-1}\). A smooth low-frequency extension makes a classical symbol of order \(-2\); proper localization changes only the local smoothing ambiguity. It has ordinary transmission, since each frequency derivative has the parity of its integer degree. The pole at \(\tau=ia\) has residue \((2ia)^{-1}\), so (T20) gives principal boundary symbol \(1/(2|\eta|)\), of order \(-1\). One normal derivative gives the principal symbol \(i/2\), and two give \(-|\eta|/2\). Directly, the inverse normal transform is \(e^{-a t}/(2a)\) for \(t>0\), and applying \(D_t=-i\partial_t\) confirms each value and sign. The polynomial part of \(\tau^2/(\tau^2+a^2)\) has plus integral zero, as (T17) requires.

## 15. Problems with full solutions

**Problem 1.** In the first model, explain why replacing the Besov endpoint by the statement that every tangent derivative lies in \(H^{-k/2-\epsilon}\) for every \(\epsilon>0\) loses information. Produce a normal symbol-like amplitude that meets these weakened estimates but is not of order zero.

**Solution.** In one normal dimension choose smooth disjoint dyadic bumps \(\psi(2^{-j}\tau)\), supported where \(1<2^{-j}\tau<3/2\), and put
\(a(z,\tau)=g(z)\sum_{j\geq1}j\psi(2^{-j}\tau)\).
It has frequency derivatives bounded by \(C_\alpha\langle\tau\rangle^{\epsilon-\alpha}\) for every \(\epsilon>0\), but its zeroth derivative is unbounded on the bump maxima, so it is not \(S^0\). Form \(u\) by (C4) and compactly localize near the normal origin if desired. Every tangent generator \(tD_t\) replaces a bump by a finite linear combination of its scaled derivatives with the same factor \(j\); tangential derivatives act on \(g\). Balanced normal monomials have the same bound. The squared dyadic mass is at most \(C j^2 2^j\), so the weighted Sobolev sum at \(-1/2-\epsilon\) is bounded by \(C\sum j^2 2^{-2j\epsilon}<\infty\) for every word. Before localization the endpoint sequence is comparable to \(j\) along these annuli, and is unbounded. Localization equal to one near \(t=0\) subtracts an off-plane smooth rapidly decreasing term, by the proof after (C8) applied at any positive order \(\epsilon\); it cannot cancel this unbounded dyadic sequence. The exact compact converse would forbid an \(S^0\) representation. Thus arbitrarily small Sobolev losses cannot replace the stated Besov endpoint.

**Problem 2.** In ambient dimension two and codimension one, change coordinates by \(\kappa(t,z)=(2t,3z)\). If the normalized amplitude in the new chart is \(a_\kappa(z,\tau)=h(z)\tau^r\) on the positive frequency ray, what is the old-chart principal amplitude? Check the intrinsic degree.

**Solution.** Formula (C20) gives
\(a(z,\tau)=2^{-r}\sqrt{3/2}\,h(3z)\tau^r\) modulo one lower order. The square-root factor is the Jacobian of the induced map \((z,\tau)\mapsto(3z,\tau/2)\) on half-densities; replacing it by the normal integration determinant alone would be incorrect. Since \(n=2,k=1\), ordinary amplitude order is \(r=m\), while the fiber half-density adds \(1/2\). The intrinsic order is \(m+1/2=m+n/4\), as required.

**Problem 3.** Let \(b(\tau)=\operatorname{sgn}(\tau)|\tau|^{-2}\) on \(|\tau|>1\), with any smooth extension near the two endpoints. Find its first nonsmooth inverse-integral term on \(t>0\). Does it pass (T6)?

**Solution.** Altering bounded frequencies changes only a smooth function. The two tails give
\(2i\int_1^\infty\tau^{-2}\sin(t\tau)d\tau
=2it\int_t^\infty s^{-2}\sin s\,ds\).
Near zero, \(s^{-2}\sin s=s^{-1}+O(s)\), so the singular part is \(-2it\log t\). Here \(v=-2,c_+=1,c_-=-1\), whereas (T4) requires \(c_-=c_+\). The logarithmic failure agrees with (T5); neither the factor \(i\) nor the lower limit \(t\) may be removed in the rescaling.

**Problem 4.** Why is it insufficient to check only the values of homogeneous components at the boundary normal rays, without their base derivatives? Give a one-dimensional order-zero example and identify its first nonsmooth output term on an ordinary input.

**Solution.** Let \(a(\tau)\) be smooth, equal to one for large positive \(\tau\), and zero for large negative \(\tau\). Near the boundary take \(p(t,\tau)=t a(\tau)\), and arrange compact local support and proper support. Its order-zero homogeneous term vanishes at \(t=0\) on both rays, but its first normal base derivative has values one and zero. It fails (T10). Choose an ordinary smooth input equal to one near zero on the positive side and compactly supported. Formula (T9) gives Fourier leading term \(-i\tau^{-1}\); all further boundary jets vanish. The positive-frequency part of its output is consequently
\((2\pi)^{-1}t\int_1^\infty e^{it\tau}(-i\tau^{-1})d\tau\) modulo smooth terms. At \(v=-1\), (T5) gives leading term \(i(2\pi)^{-1}t\log t\). This is not smooth up to zero, although the undifferentiated boundary-ray test passed.

**Problem 5.** Put \(P=b(t,z)Q\), where the leading symbol of \(Q\) is \((\tau^2+|\eta|^2)^{-1}\), and suppose this is its full homogeneous model near the point. Find the two contributions to the full normal derivative trace of its simple layer. Which would be missed by using only \(\tau p\)?

**Solution.** Formula (T25) with \(k=1,l=0\) is \(p_{1,0}=\tau p+D_t p\). Its plus integral therefore has homogeneous terms \(ib(0,z)/2\), of order zero, and \((D_tb)(0,z)/(2|\eta|)\), of order \(-1\), with any other lower symbol terms treated in the same way. Direct differentiation of \(b(t,z)e^{-|\eta|t}/(2|\eta|)\) gives both. The second term is the normal derivative of the coefficient and would be lost by keeping only \(\tau p\).

**Problem 6.** Fix \(m=1/2+i\) and inward type \(\mu=1/3-2i\). Describe every opposite-side type guaranteed solely by the phase relation. Is there a real such type?

**Solution.** Equation (T15) gives
\(\mu'=N-m-\mu=N-5/6+i\), \(N\in\mathbb Z\). These differ by integers and hence give the same opposite-side phase. Every one has imaginary part one, so none is real. Requiring only the real part of \(m+\mu+\mu'\) to be integral would leave an exponential of nonunit modulus and would not give the inverse jet relation. An operator flat at all relevant conormal jets is an exceptional case satisfying every phase, which is why the question asks what the phase relation alone guarantees.

## Prerequisites and scope

The advanced prerequisites are the symbol cutoff/localization bounds of [Localizing symbols with moving metrics](metric-localization.md); the possibly degenerate Gauss multiplier, its restriction theorem, finite-seminorm remainders and weak extension in Section 8 of [Quadratic Fourier multipliers at a moving scale](gauss-transform-estimates.md); and the distributional Fourier kernels, quantization changes, classical Schwartz estimates and \(L^2\) Fourier extension in Section 4 of [Two measuring scales, one Weyl product](weyl-metric-products.md), Section 5 of [Two measuring scales, one Weyl product](weyl-metric-products.md) and Section 8 of [Two measuring scales, one Weyl product](weyl-metric-products.md). The elementary entry base listed at the start includes Schwartz density and completeness of \(L^2\), so the extension from Schwartz Plancherel is legitimate. The local symbol coordinate, product and adjoint formulas used here have been derived with complete remainder orders from these prerequisites. These classical local formulas do not establish operator composition for arbitrary compatible metrics.

## References

The mathematical antecedent is Lars Hörmander, *The Analysis of Linear Partial Differential Operators III*, second printing with corrections (1994), §18.2 and Appendix B. The exact dyadic endpoint is also stated in [Sá Barreto and Wang's author draft on triple interactions](https://www.math.purdue.edu/~sabarre/Papers/TripleInt.pdf), dated 25 October 2018, §2.1; that discussion refers elsewhere for its normal-form equivalence. It is not used here as a proof of the compact converse or the bundle symbol theorem.

[Grubb's 2014 version of the work on fractional Laplacians and transmission spaces](https://arxiv.org/pdf/1310.0951v5), §2, provides a useful comparison of the complex-type condition. Its supported-space parameter \(\nu\) corresponds to \(\nu=-\mu-1\) here; using \(-\mu\) would give the same phase but a different space. [Grubb's chapter on boundary operators](https://web.math.ku.dk/~grubb/dist10.pdf), §§10.3–10.4, gives a Laurent-symbol comparison for the upper residue integral. The general analytic subtraction lemma and the full complex-order remainder estimates required here have been proved above.

## Further questions

A natural next question is how the collection of layer traces combines into a projection onto boundary data of solutions. The residue model gives a concrete starting point, while the all-jet transmission criterion identifies which operators admit those traces in the smooth category. For noninteger type, the spaces in (T7) suggest the appropriate weighted boundary data instead of ordinary smooth zero extensions. Those elliptic projection, solvability and weighted mapping theorems require additional arguments and are not consequences asserted by this lesson.

## 16. Complex contour integrals and their complete foundations

The boundary subtraction and wave integrals require actual contour, continuation and Gamma proofs. This section supplies them with their original orientations, branches, factors and endpoint domains. The finite calculus and original circle constant are proved in [Metric foundations](metric-foundation-bridges.md); measure construction, product integration, affine substitution and the Gaussian are proved in [Banach estimates and measure foundations](banach-foundation-bridges.md). The nonlinear measure substitution and the full sphere density are proved here before their use in the beta and ball integrals.

### 16.1. The actual contour integral and triangle theorem

Let \(\Omega\subset\mathbb C\) be open. Holomorphic means complex differentiable at every point of \(\Omega\); continuity of the derivative is not assumed. A contour is a finite concatenation of continuously differentiable maps \(\gamma:[a,b]\to\Omega\). Its integral is the original oriented Riemann integral

\[
\int_\gamma f(\zeta)\,d\zeta
 =\int_a^b f(\gamma(t))\gamma'(t)\,dt,\qquad
\left|\int_\gamma f\,d\zeta\right|
 \leq \sup_{\gamma([a,b])}|f|\int_a^b|\gamma'(t)|\,dt.
\tag{CX1}
\]

This is defined for continuous \(f\). The real and imaginary coordinate integrals, their triangle inequality and the limit of Riemann sums prove the bound. Reversing the original parameter endpoints reverses the sign. Concatenation adds the integrals, including their endpoints. A continuously differentiable increasing reparameterization retains its derivative factor by substitution; reversing the orientation changes its sign. These assertions apply to each piece separately. A zero-length piece contributes zero.

For an oriented triangle \(T\) whose closed interior lies in \(\Omega\), let \(I(T)=\int_{\partial T}f\,d\zeta\). Join the side midpoints, forming four triangles with the inherited positive orientation. Each interior edge occurs twice with opposite orientation, so \(I(T)\) is the sum of their four boundary integrals. Choose a child whose integral has modulus at least \(|I(T)|/4\), then repeat. At each step choose the first child in a fixed finite ordering satisfying that inequality; no additional infinite-choice assumption is needed. The resulting closed triangles \(T_k\) are nested, with diameter \(2^{-k}d\) and perimeter \(2^{-k}L\), where \(d,L\) are the original diameter and perimeter. Compactness gives a common point \(z_*\), and the shrinking diameter makes it unique.

Complex differentiability at \(z_*\) gives

\[
f(\zeta)=f(z_*)+f'(z_*)(\zeta-z_*)
                 +(\zeta-z_*)\epsilon(\zeta),\qquad
\epsilon(\zeta)\longrightarrow0\quad(\zeta\longrightarrow z_*).
\tag{CX2}
\]

The boundary integrals of the first two terms are zero: the fundamental theorem on each side evaluates the respective primitives \(f(z_*)\zeta\) and \(f'(z_*)(\zeta-z_*)^2/2\), and the endpoint values cancel. Therefore CX1 gives

\[
|I(T)|\leq4^k|I(T_k)|
\leq dL\sup_{\zeta\in T_k}|\epsilon(\zeta)|
\longrightarrow0.
\tag{CX3}
\]

Thus every such triangle integral is zero. A degenerate triangle has zero integral directly by cancellation of its collinear oriented sides. No real partial derivative or continuity of \(f'\) has been used.

There is a point-removal version needed below. Suppose \(g\) is continuous on a disk and holomorphic except possibly at one point \(w\). Its triangle integrals are still zero. For a triangle having \(w\) as a vertex, remove the homothetic small triangle of ratio \(\delta>0\) at that vertex. The remaining quadrilateral splits into two triangles avoiding \(w\), whose integrals vanish by CX3. Interior-edge cancellation makes the original integral equal the small triangle integral. On its compact neighborhood \(g\) is bounded, so CX1 bounds this by \(\delta L\sup|g|\), tending to zero. If \(w\) is inside a triangle, split it into the three triangles joining \(w\) to its vertices. If it is on an edge, split into the two triangles with \(w\) as a vertex. Opposite internal sides cancel in both cases. If \(w\) is outside, CX3 already applies.

For any continuous \(g\) with zero triangle integrals on a disk centered at \(a\), define \(F(z)=\int_{[a,z]}g\,d\zeta\) on that disk. The triangle with vertices \(a,z,z+h\) gives

\[
F(z+h)-F(z)=h\int_0^1g(z+th)\,dt,\qquad F'(z)=g(z).
\tag{CX4}
\]

Continuity makes the quotient tend to \(g(z)\). The complex derivative is also the real coordinate derivative, since the remainder is \(o(|h|)\). Along every contour piece the already proved real chain rule gives \((F\circ\gamma)'=g(\gamma)\gamma'\). Consequently every closed contour in this disk has integral zero. This applies to the point-removal function as well; it does not assume in advance that the derivative of a holomorphic function is holomorphic.

### 16.2. The circle formula, every coefficient and both continuation principles

Let the closed disk \(|\zeta-a|\leq R\) lie in \(\Omega\), and let \(|z-a|<R\). Set

\[
g(\zeta)=
 \begin{cases}
 (f(\zeta)-f(z))/(\zeta-z),&\zeta\ne z,\\
 f'(z),&\zeta=z.
 \end{cases}
\tag{CX5}
\]

It is continuous at \(z\) by complex differentiability and holomorphic elsewhere by the proved field/product rules. The point-removal argument and CX4 give zero circle integral for \(g\). Use the original positively oriented circle \(\zeta=a+Re^{i\theta}\), \(0\leq\theta\leq2\pi\). The original complex exponential is its everywhere convergent series; the full binomial product gives \(e^{u+v}=e^ue^v\), and termwise differentiation gives \((e^u)'=e^u\). Its real and imaginary restrictions agree with the circle parameter constructed in the metric companion by their first-order equations and initial values. Thus this circle uses that companion's actual \(\pi\), rather than a new convention.

The geometric series for \((\zeta-z)^{-1}\) converges uniformly on the circle. With its derivative factor \(iRe^{i\theta}\), its term of index zero integrates to \(2\pi i\); each other term integrates to zero by the fundamental theorem for \(e^{-im\theta}/(-im)\). It follows that

\[
\int_{|\zeta-a|=R}\frac{d\zeta}{\zeta-z}=2\pi i,\qquad
f(z)=\frac1{2\pi i}\int_{|\zeta-a|=R}
                          \frac{f(\zeta)}{\zeta-z}\,d\zeta .
\tag{CX6}
\]

Let \(M=\sup_{|\zeta-a|=R}|f(\zeta)|\). Expanding the same full denominator and using CX1 proves

\[
\begin{aligned}
f(z)&=\sum_{m=0}^\infty c_m(z-a)^m,&
c_m&=\frac1{2\pi i}\int_{|\zeta-a|=R}
                     \frac{f(\zeta)}{(\zeta-a)^{m+1}}\,d\zeta,\\
|c_m|&\leq MR^{-m},&
\sup_{|z-a|\leq r}\left|f(z)-\sum_{m=0}^Nc_m(z-a)^m\right|
 &\leq \frac{M(r/R)^{N+1}}{1-r/R}\quad(0\leq r<R).
\end{aligned}
\tag{CX7}
\]

At \(r=0\), the remainder is exactly zero for \(N\geq0\). For every derivative order \(j\), the differentiated terms on a compact disk of positive radius \(r<R\) are bounded by the summable series

\[
M\sum_{m\geq j}\frac{m!}{(m-j)!}r^{m-j}R^{-m}.
\tag{CX8}
\]

Its successive ratio tends to \(r/R<1\). The metric companion's uniform differentiation theorem now proves all derivatives, including at the center by continuity. Hence

\[
f^{(j)}(a)=j!c_j,\qquad |f^{(j)}(a)|\leq j!MR^{-j}.
\tag{CX9}
\]

In particular complex differentiability implies a convergent local power series and continuous derivatives of every order; these have been proved rather than included in the definition.

If the first nonzero coefficient of a nonzero local power series at \(a\) has index \(m\), factor it as \((z-a)^m(c_m+\sum_{\ell>m}c_\ell(z-a)^{\ell-m})\). The parenthesis tends to \(c_m\ne0\), so the zero at \(a\) is isolated and has exactly that multiplicity. A holomorphic function on a connected open set which vanishes on a set with an accumulation point in that open set vanishes everywhere. Indeed the series at that point cannot have a first nonzero coefficient, so it vanishes on a disk. The set of points with a zero neighborhood is open. At a limit point inside the domain it has either an eventual equal point or distinct zeros accumulating there; the same series argument makes it closed relative to the domain. Connectedness makes it the whole domain. Applying this to the difference proves the identity theorem with the actual common connected domain.

Finally, if holomorphic \(f_n\) converge uniformly on every compact subset of \(\Omega\), their limit \(f\) is holomorphic and every \(f_n^{(j)}\) converges to \(f^{(j)}\) uniformly on smaller compact disks. On each fixed circle uniform convergence permits passage through CX6 and CX7. The limit therefore has the same circle representation and coefficient formula. The bound in CX8 with the uniformly bounded circle values proves differentiation and convergence on every smaller disk, for every fixed \(j\). A finite disk cover gives the result on an arbitrary compact subset. This proves the required locally uniform continuation principle without assuming it.

### 16.3. The full dominated holomorphic integral map

Let \((S,\mu)\) be an arbitrary positive measure space. The compact envelopes below restrict every required product integral to an actual sigma-finite positive-envelope part; Section16.3.1 proves that reduction and the completed joint measurability before Fubini is used. Suppose \(f(z,x)\) is measurable in \(x\) for every \(z\in\Omega\), and \(f(\,\cdot\,,x)\) is holomorphic on \(\Omega\) for every \(x\) outside one fixed null set. For every compact \(K\subset\Omega\), assume an actual integrable \(M_K\geq0\) bounds \(|f(z,x)|\) for all \(z\in K\), almost everywhere. Define the original integral \(F(z)=\int_S f(z,x)d\mu(x)\).

Dominated convergence proves continuity of \(F\) on every smaller compact neighborhood. Take a closed disk \(|\zeta-a|\leq R\subset\Omega\), and \(|z-a|\leq r<R\). CX6 for the integrand has denominator of modulus at least \(R-r\) on that circle. The integral of its absolute value over the original circle and \(S\) is at most \(2\pi R\|M_K\|_1/(R-r)\). Thus the proved absolute Fubini theorem gives

\[
\begin{aligned}
F(z)&=\frac1{2\pi i}\int_{|\zeta-a|=R}
                    \frac{F(\zeta)}{\zeta-z}\,d\zeta,\\
F^{(m)}(a)&=\int_S\partial_z^m f(a,x)\,d\mu(x),&
\int_S|\partial_z^m f(a,x)|\,d\mu(x)
 &\leq m!R^{-m}\|M_K\|_1 .
\end{aligned}
\tag{CX10}
\]

The first line gives a convergent power series by the actual geometric denominator expansion, hence holomorphy of \(F\). For the second line use CX9 for each integrand and its circle formula for the derivative. The full absolute bound is integrable, so the same Fubini interchange identifies the coefficient with the integral of the integrand derivative. Differentiability under the integral is therefore a consequence, not an extra assumption.

For \(d\) complex parameters on an actual product of disks, the same argument applied successively to their circle integrals gives, with multiindex \(\alpha=(\alpha_1,\ldots,\alpha_d)\) and original radii \(R_j\),

\[
\partial^\alpha F(a)=\int_S\partial^\alpha f(a,x)d\mu(x),
\qquad
\int_S|\partial^\alpha f(a,x)|d\mu(x)
 \leq\left(\prod_{j=1}^d\alpha_j!R_j^{-\alpha_j}\right)\|M_K\|_1 .
\tag{CX11}
\]

Every circle contributes its own \(1/(2\pi i)\), derivative factorial and radius. The iterated geometric series converges absolutely on every smaller product of disks, because its bound is the product of the \(d\) geometric sums times \(\|M_K\|_1\). It therefore supplies a joint power series, including every mixed derivative, rather than only separate differentiability. Additional continuous real parameters can be carried through this proof when the actual envelope is common on their compact parameter sets; dominated convergence supplies their continuity. Their derivatives can be passed through only when their full differentiated integrands have corresponding integrable envelopes, exactly as in the real dominated-integral provider.

#### 16.3.1. The actual circle and product measurability

To interchange the original parameter and circle integrals, first establish their joint measurability and absolute envelope bounds. It retains the original measure space \((S,\mu)\), the integrand \(f(z,x)\), every compact envelope and the original integral \(F(z)=\int_S f(z,x)\,d\mu(x)\). Its purpose is to prove the product measurability needed for the stated Fubini steps, rather than assume that separate measurability has already supplied it.

Fix the original closed disk \(K=\{|z-a|\leq R\}\subset\Omega\), \(R>0\), and the original circle parametrization
\(\zeta(t)=a+Re^{it}\), \(0\leq t\leq2\pi\). The hypotheses give one fixed null set \(N\) outside which \(f(\,\cdot\,,x)\) is holomorphic, hence continuous on the circle. Enlarge it by the null set for this compact envelope, so
\(|f(z,x)|\leq M_K(x)\) for every \(z\in K\), \(x\notin N\), with \(\int_S M_K\,d\mu<\infty\). A finite modification of the envelope on its own null exceptional set can be covered by this same \(N\); the original integral is unchanged.

For \(k\geq1\), partition \([0,2\pi)\) into its \(2^k\) half-open intervals
\(I_{k,j}=[2\pi j/2^k,2\pi(j+1)/2^k)\), and retain the endpoint \(\{2\pi\}\) separately. Define the actual finite sum

\[
f_k(t,x)=\sum_{j=0}^{2^k-1}
\boldsymbol1_{I_{k,j}}(t)
f\!\left(a+Re^{2\pi i j/2^k},x\right)
\ +\boldsymbol1_{\{2\pi\}}(t)f(a+R,x).
\tag{CMI1}
\]

Each function \(x\mapsto f(a+Re^{2\pi i j/2^k},x)\) is measurable by the original hypothesis. The corresponding function on the product is measurable: the inverse image of a Borel set on each strip is that strip times a measurable subset of \(S\), and the sum is finite. Thus every \(f_k\) is measurable for the product sigma-algebra. For each original \(t\) and \(x\notin N\), continuity on the circle gives \(f_k(t,x)\to f(\zeta(t),x)\). The countable limit is measurable off the product cylinder \([0,2\pi]\times N\). That cylinder has product measure zero, and its entire subsets are measurable in the completed product. Hence the original function \((t,x)\mapsto f(\zeta(t),x)\), with its actual values on that cylinder retained, is measurable for the completed product. No pointwise values of the working integrand have been substituted.

The product argument can be confined to an actual sigma-finite part even when the whole original measure space is not sigma-finite. Put
\[
S_K=\bigcup_{j=1}^\infty\{x:M_K(x)\geq1/j\}.
\tag{CMI2}
\]
Every set in this union has measure at most \(j\int_S M_K\,d\mu\), by the proved integral of its indicator and the pointwise inequality
\(\boldsymbol1_{\{M_K\geq1/j\}}\leq jM_K\).
Thus \(\mu|_{S_K}\) is sigma-finite. On \(S\setminus S_K\) the original \(M_K\) is zero and \(f(z,x)=0\) for every \(z\in K\), outside \(N\). The original integral therefore retains the entire decomposition
\[
\int_S f(z,x)\,d\mu(x)
=\int_{S_K}f(z,x)\,d\mu(x)
 +\int_{S\setminus S_K}f(z,x)\,d\mu(x),
\qquad
\int_{S\setminus S_K}f(z,x)\,d\mu(x)=0 .
\tag{CMI3}
\]
The zero complement is proved from the actual envelope; it is not a dropped contribution. Product measurability and completed complex Fubini on the sigma-finite factor \(S_K\) are supplied by the original measure chapter. The finite circle parameter is the other factor. Null exceptional cylinders are measurable in its completion, with measure zero as stated above.

For \(|z-a|\leq r<R\), the exact circle differential is
\(d\zeta=iRe^{it}\,dt\) and its modulus is \(R\,dt\). The original kernel has denominator of modulus at least \(R-r\). Consequently
\[
\int_0^{2\pi}\int_{S_K}
\left|
\frac{f(a+Re^{it},x)}{a+Re^{it}-z}
iRe^{it}
\right|d\mu(x)\,dt
\leq
\frac{2\pi R}{R-r}\int_S M_K(x)\,d\mu(x).
\tag{CMI4}
\]
Every circle factor and the zero-complement equality in CMI3 remain. This is precisely the absolute envelope required to interchange the original \(S\)-integral and the positively oriented circle in CX10. For its \(m\)-th coefficient the additional original Cauchy multiplier is
\(m!/(2\pi i)\) and the denominator is \((\zeta-a)^{m+1}\). The absolute parameter integral is bounded by
\[
\frac{m!}{2\pi}2\pi R R^{-m-1}
\int_S M_K\,d\mu
=m!R^{-m}\int_S M_K\,d\mu .
\tag{CMI5}
\]
This proves both product measurability and the complete bound before the derivative/Fubini step. Each derivative \(x\mapsto\partial_z^m f(a,x)\) is measurable outside \(N\), because it is a pointwise limit of countably many measurable difference quotients on the original coordinate disk. Define its extension to the exceptional set \(N\) to be zero, since a holomorphic derivative was required only off \(N\). This is a measurable extension on the original measure space, agrees with every required derivative, and changes no integral.

For the \(d\)-parameter extension, take the original product of closed disks centered at \(a_j\) with radii \(R_j>0\). The precise hypotheses are measurability in \(x\) for every parameter tuple, separate holomorphy in each complex coordinate outside one fixed null set, and one actual integrable \(M_K\) for the whole compact product. These suffice; joint holomorphy is the conclusion.

Joint measurability on the product of its circles follows by induction on their number. For one circle it is CMI1. For \(d>1\), replace only the first circle parameter by its finite dyadic endpoints. Each resulting summand is measurable in the remaining \(d-1\) parameters and \(x\) by the induction hypothesis, because fixing that endpoint preserves the original measurability and separate continuity. Multiplication by its first-parameter interval indicator gives product measurability. As its mesh tends to zero, separate continuity in that first coordinate gives pointwise convergence to the original function for every remaining parameter tuple and every \(x\notin N\). The completed null-cylinder argument proves the claim, with the entire original tuple retained. There is no assumption that separate continuity already gives joint continuity.

Apply the original one-variable Cauchy formula successively for the fixed other coordinates. The absolute completed Fubini bound on the circle product is
\[
\left(\prod_{j=1}^d\frac{2\pi R_j}{R_j-r_j}\right)
\int_S M_K\,d\mu,\qquad 0\leq r_j<R_j .
\tag{CMI6}
\]
It comes from the full product of the \(d\) differentials \(iR_je^{it_j}\,dt_j\), not a unit circle substitute. The resulting original multiple formula is
\[
F(z)=\left(\prod_{j=1}^d\frac1{2\pi i}\right)
\int_{|\zeta_1-a_1|=R_1}\cdots
\int_{|\zeta_d-a_d|=R_d}
\frac{F(\zeta_1,\ldots,\zeta_d)}
     {\prod_{j=1}^d(\zeta_j-z_j)}
\ d\zeta_d\cdots d\zeta_1 .
\tag{CMI7}
\]
All factors have their original positive orientations; Fubini justifies reversing the iterated order as well. In each denominator use its full convergent geometric expansion with its original numerator powers. On a smaller product of disks the absolute majorant is the product of the \(d\) geometric series, each of ratio \(r_j/R_j<1\). Its sum times \(\int_S M_K\,d\mu\) bounds the whole series, so the actual multiple Cauchy integral is a joint convergent power series. Differentiation of this joint series and the full coefficient integrals give
\[
\partial^\alpha F(a)
=\int_S\partial^\alpha f(a,x)\,d\mu(x),\qquad
\int_S|\partial^\alpha f(a,x)|\,d\mu(x)
\leq
\left(\prod_{j=1}^d\alpha_j!R_j^{-\alpha_j}\right)
\int_S M_K\,d\mu .
\tag{CMI8}
\]
Mixed derivatives of the integrand itself are supplied by the same multiple circle representation before integration in \(x\). Each is measurable by its countable original difference quotients off the fixed null set, and CMI8 gives its absolute integral bound. This closes the actual measurability, Fubini, mixed-derivative and joint-power-series steps used in CX10--CX11, including the full original radius and factorial factors. Additional real parameters still need their actual continuity and differentiated envelopes on compact parameter sets, as the original source states; no real derivative hypothesis is invented.

### 16.4. The original winding number

For a closed contour \(\Gamma\) and a point \(w\) off its image define

\[
n_\Gamma(w)=\frac1{2\pi i}\int_\Gamma\frac{d\zeta}{\zeta-w}.
\tag{CX12}
\]

On each contour piece set \(U(t)=\gamma(t)-w\), which never vanishes. Define the continuous accumulated integral \(A(t)=\int_{\Gamma|_{[a,t]}}d\zeta/(\zeta-w)\), with the pieces concatenated in their original order. The fundamental theorem and product rule give
\((U(t)e^{-A(t)})'=0\) on each piece, since \(A'=U'/U\). Endpoint continuity makes the constant the same on all pieces. Hence

\[
U(t)=U(a)e^{A(t)},\qquad e^{A(b)}=1 .
\tag{CX13}
\]

The complex exponential has modulus \(e^{\operatorname{Re}z}\), by its product law and conjugate series. Its purely imaginary restriction is the original circle parameter. That circle traverses the unit circle once during \(0\leq\theta<2\pi\), as proved by the arctangent chart and arc-length calculation in the metric companion. Consequently \(e^z=1\) holds exactly for \(z=2\pi i k\), \(k\in\mathbb Z\). CX13 therefore proves that CX12 is an integer, with its sign fixed by the original contour orientation.

The contour image is compact. On a neighborhood of any \(w\) outside it the denominator has a positive uniform lower bound. CX1 or dominated convergence proves continuity of CX12 there. Its integer values make it locally constant, and therefore constant on every connected component of the complement of the contour. If the image lies in \(|\zeta|\leq L\) and \(|w|>L\), the full geometric expansion gives

\[
\frac1{\zeta-w}
 =-\sum_{m=0}^{\infty}\frac{\zeta^m}{w^{m+1}}.
\tag{CX14}
\]

It converges uniformly on the contour. Each numerator \(\zeta^m\) has the global primitive \(\zeta^{m+1}/(m+1)\), so every term has zero closed-contour integral. Thus \(n_\Gamma(w)=0\) on the unbounded outside component. Reversing \(\Gamma\) negates its winding number; concatenating closed contours adds their winding numbers. These are exact oriented-integral identities.

### 16.5. The complete contour theorem and every finite-pole residue

A finite integer sum of closed contours is also allowed: add the original integrals and winding numbers with precisely those integer coefficients. In an integral bound use the sum of each length times the absolute value of its integer coefficient. Suppose \(\Gamma\) lies in \(\Omega\) and
\(n_\Gamma(w)=0\) for every \(w\notin\Omega\). For holomorphic \(f\) on \(\Omega\), define off the contour

\[
\Phi(w)=\frac1{2\pi i}\int_\Gamma\frac{f(\zeta)}{\zeta-w}\,d\zeta .
\tag{CX15}
\]

It is holomorphic there by CX10, with the positive distance to the compact contour supplying the actual local envelope. For \(w\in\Omega\), the function

\[
H(w)=\frac1{2\pi i}\int_\Gamma
             \frac{f(\zeta)-f(w)}{\zeta-w}\,d\zeta
\tag{CX16}
\]

is holomorphic even at points on the contour. At \(\zeta=w\) the quotient is defined as \(f'(w)\). To prove its required holomorphy in \(w\), expand \(f\) on a small disk at a diagonal point. Each divided power has the full polynomial
\(((\zeta-a)^m-(w-a)^m)/(\zeta-w)
=\sum_{j=0}^{m-1}(\zeta-a)^{m-1-j}(w-a)^j\).
The coefficient bounds in CX7 make this sum locally uniformly convergent, with every derivative on smaller disks by CX8. Away from the diagonal the quotient is a quotient of holomorphic functions with nonzero denominator. On a compact \(w\)-set and the compact contour, a finite disk cover of the diagonal supplies a uniform bound for those divided differences; on its compact complement the denominator is bounded away from zero. CX10 therefore proves the asserted integral holomorphy.

Off the contour, CX12 gives \(H=\Phi-n_\Gamma f\). Let \(V\) be the open set of points off the contour with \(n_\Gamma=0\). It is open by local constancy. The hypothesis places every point outside \(\Omega\) in \(V\). On \(V\), define \(H=\Phi\); this agrees with CX16 on the overlap. Since \(\Omega\cup V=\mathbb C\), these definitions construct one entire \(H\), including every contour point.

If the contour lies in \(|\zeta|\leq L\), let \(\ell\) be its total length with absolute integer multiplicities. For \(|w|>L\), CX14 gives \(n_\Gamma(w)=0\) and

\[
|H(w)|=|\Phi(w)|
\leq \frac{\ell\,\sup_\Gamma|f|}{2\pi(|w|-L)}
\longrightarrow0.
\tag{CX17}
\]

Continuity bounds \(H\) on the remaining compact disk, so it is bounded on the whole plane. CX9 at any center and any radius gives \(|H'(a)|\leq \sup_{\mathbb C}|H|/R\); letting \(R\to\infty\) proves \(H'=0\). The fundamental theorem on each straight segment makes \(H\) constant, and CX17 makes that constant zero. This is the full Liouville argument, including its actual Cauchy factor.

Consequently both original contour conclusions are

\[
\frac1{2\pi i}\int_\Gamma\frac{f(\zeta)}{\zeta-w}\,d\zeta
       =n_\Gamma(w)f(w)\quad(w\in\Omega\setminus\Gamma),
\qquad
\int_\Gamma f(\zeta)\,d\zeta=0 .
\tag{CX18}
\]

For the second conclusion use \(\Phi(w)=0\) at sufficiently large \(w\), multiply CX15 by \(w\), and pass to the uniform limit \(w/(\zeta-w)\to-1\) on the compact contour. All prefactors remain in that calculation. The winding hypothesis is necessary: for \(f(\zeta)=1/\zeta\) on \(\mathbb C\setminus\{0\}\), a positive circle has winding one at the omitted point and integral \(2\pi i\). This example identifies precisely the domain condition; it does not supply that condition by assuming away a pole.

For a deformation \(\gamma_s\) of closed contours within \(\Omega\), with a fixed finite piece decomposition and jointly continuous \(\gamma_s,\partial_t\gamma_s\), the winding at every point outside \(\Omega\) is continuous in \(s\), by its uniform positive denominator bound on the compact parameter/contour product. It is integer-valued, so it is constant. The cycle \(\gamma_1-\gamma_0\) thus has winding zero outside \(\Omega\). Applying CX18 proves equality of their holomorphic integrals. This proves the contour-deformation rule with the exact domains and actual orientation.

Now let \(f\) be meromorphic on \(\Omega\) with exactly the finite poles \(a_1,\ldots,a_p\), of actual orders \(m_1,\ldots,m_p\geq1\), and let \(\Gamma\) avoid them. At \(a_j\) the holomorphic function \(g_j(\zeta)=(\zeta-a_j)^{m_j}f(\zeta)\), with \(g_j(a_j)\ne0\), has the power series proved in CX7. Its entire principal part and residue are

\[
\begin{aligned}
P_j(\zeta)&=\sum_{\ell=1}^{m_j}
        \frac{g_j^{(m_j-\ell)}(a_j)}{(m_j-\ell)!}
                         (\zeta-a_j)^{-\ell},\\
\operatorname{Res}_{a_j}f
 &=\frac{g_j^{(m_j-1)}(a_j)}{(m_j-1)!}.
\end{aligned}
\tag{CX19}
\]

Subtracting every \(P_j\) gives a holomorphic function on \(\Omega\): its local residual power series has only nonnegative exponents at each original pole, and all the other subtracted principal parts are holomorphic there. CX18 gives zero integral for this difference when the same winding condition outside \(\Omega\) holds. Every term with \(\ell\geq2\) has the global primitive
\(-(\zeta-a_j)^{1-\ell}/(\ell-1)\) away from that pole, so its closed-contour integral is zero by the full chain and fundamental theorem. Each \(\ell=1\) term has integral \(2\pi i n_\Gamma(a_j)\) by CX12. Thus

\[
\int_\Gamma f(\zeta)d\zeta
 =2\pi i\sum_{j=1}^p n_\Gamma(a_j)
                  \frac{g_j^{(m_j-1)}(a_j)}{(m_j-1)!}.
\tag{CX20}
\]

Every original pole, order, derivative factorial and winding multiplicity is retained. Empty pole sets give CX18. A rational function is covered by \(\Omega=\mathbb C\), where the exterior winding condition is empty; its polynomial part has a global polynomial primitive and contributes zero.

For later orientation checks, a positive full circle has winding one inside and zero outside by the exact geometric integral in CX6 and CX14. A positive upper half-disk boundary runs along the real interval from \(-R\) to \(R\), then counterclockwise along the upper arc from \(R\) to \(-R\). Its winding is zero outside the closed half-disk: such points can be joined to infinity through the lower half-plane or outside the radius without crossing the contour. Its winding is constant on the connected open upper half-disk. At \(w=i\delta\), \(0<\delta<R\), the real segment integral has imaginary part
\(\int_{-R}^R\delta/(t^2+\delta^2)dt\to\pi\) and zero real part. The upper arc integral tends to \(i\pi\), uniformly away from its denominator as \(\delta\downarrow0\). The winding tends to one, so its integer value is one throughout that half-disk. Reversal negates this value. This proves the half-plane residue orientation used in T17 directly.

### 16.6. Bounded and exhausted maximum principles in the original domains

Suppose \(|f|\) has a local maximum at an interior point \(a\). If \(f(a)=0\), it vanishes on that neighborhood. Otherwise, if the local power series is nonconstant, let \(m\geq1\) be its first nonconstant coefficient. Choose a complex unit \(u\) so that \(c_m u^m\) is a positive real multiple of \(f(a)\); existence follows from the actual circle parameter by dividing that argument by the integer \(m\). For small positive \(r\),
\(f(a+ru)=f(a)+c_m u^m r^m+o(r^m)\).
Its component in the direction of \(f(a)\) is strictly greater than \(|f(a)|\), contradicting the maximum. Thus \(f\) is constant locally, and CX7's identity theorem makes it constant on the connected component. This proves the interior maximum-modulus principle.

If \(\Omega\) is bounded, \(f\) is holomorphic in it and continuous on its closure, compactness gives a maximum on that closure. If it is attained in the interior, the preceding argument makes \(f\) constant on that component. That bounded open component has a boundary point: follow a ray from one of its points until the first exit from a containing bounded ball and take the first component-exit limit. Its boundary lies in \(\partial\Omega\), because any interior ball meeting the component at a limit point would be connected to it and hence belong to the same component. Continuity therefore makes the constant value a boundary value. Consequently

\[
\sup_{\overline\Omega}|f|\leq\sup_{\partial\Omega}|f|.
\tag{CX21}
\]

The reverse inequality is immediate. Disconnected bounded domains cause no exception, since the argument applies to the component where the attained maximum lies.

For an upper half-plane or upper exterior, the exhausted form retains the boundary at infinity. Apply CX21 on its intersection with \(|\zeta|<L\), removing the prescribed inner disk in the exterior case. On that bounded domain the boundary consists of its original real and inner-arc pieces and the outer arc. If the outer-arc supremum tends to zero, CX21 and \(L\to\infty\) give the bound by the original boundary pieces. No claim discards an outer contribution without this hypothesis and calculation.

Here is the exact polynomial-growth application in the original CN proof. Suppose \(H\) is holomorphic in
\(\{\operatorname{Im}\zeta>0,\ |\zeta|>R\}\), continuous on its boundary, satisfies
\(|H(\zeta)|\leq C_g(1+|\zeta|)^d\) there with \(d\geq0\), and has \(|t|^2|H(t)|\leq C_t\) on the two real tails. Choose an integer \(M>d+2\). For \(0<\epsilon\leq1\), define the entire original damping expression

\[
F_\epsilon(\zeta)=\zeta^2H(\zeta)(1-i\epsilon\zeta)^{-M},
\qquad
|1-i\epsilon\zeta|^2
 =(1+\epsilon\operatorname{Im}\zeta)^2
                     +\epsilon^2(\operatorname{Re}\zeta)^2
 \geq1+\epsilon^2|\zeta|^2 .
\tag{CX22}
\]

Its sole possible damping pole is \(-i/\epsilon\), outside the upper domain. On the real tails \(|F_\epsilon|\leq C_t\). On the fixed inner arc it is bounded by
\(C_R=R^2\sup_{\operatorname{Im}\zeta\geq0,|\zeta|=R}|H(\zeta)|\),
independently of \(\epsilon\). On the outer arc \(|\zeta|=L\),

\[
\sup|F_\epsilon|
\leq C_g\epsilon^{-M}L^{2-M}(1+L)^d
\longrightarrow0\quad(L\longrightarrow\infty).
\tag{CX23}
\]

The exponent and the factor \(\epsilon^{-M}\) are retained. First let \(L\to\infty\) for each fixed \(\epsilon\), using CX21. Then, at each fixed original \(\zeta\), let \(\epsilon\downarrow0\). This gives

\[
|F_\epsilon(\zeta)|\leq\max(C_t,C_R),\qquad
|H(\zeta)|\leq\max(C_t,C_R)|\zeta|^{-2}.
\tag{CX24}
\]

The order of limits is necessary; CX23 supplies no uniform outer limit in \(\epsilon\). This proves the actual exterior maximum estimate with every damping, radius and growth factor still present.

### 16.7. The entire original upper subtraction and its parameter map

Use exactly the original hypotheses from CN: \(q\) is continuous on \(\mathbb R\); for some \(R>0\), \(Q\) is holomorphic on the upper exterior, continuous on its boundary and polynomially bounded there; and \(q(t)-Q(t)=O(|t|^{-2})\) on both real tails. Its original definition, with its whole clockwise arc and sign, is

\[
\begin{split}
\mathcal I_+(q)={}&
\int_{|t|>R}(q(t)-Q(t))dt+\int_{-R}^{R}q(t)dt\\
&-\int_{\pi}^{0}Q(Re^{i\theta})Ri e^{i\theta}d\theta.
\end{split}
\tag{CX25}
\]

Every integral in this definition exists: the difference tail is absolutely integrable, and the interval and arc have compact continuous integrands.

For \(R<L\), Cauchy's theorem for \(Q\) on the upper half-annulus gives

\[
\int_{R<|t|<L}Q(t)dt
 +\int_{\pi}^{0}Q(Re^{i\theta})Ri e^{i\theta}d\theta
 -\int_{\pi}^{0}Q(Le^{i\theta})Li e^{i\theta}d\theta=0 .
\tag{CX26}
\]

Here is the boundary justification when \(Q\) is only continuous on the real boundary. First use inner radius \(a>R\), outer radius \(b<L\), and height \(\delta>0\), on the boundary of
\(\{a<|\zeta|<b,\ \operatorname{Im}\zeta>\delta\}\).
Its contour lies strictly in the original holomorphy domain. Its winding is zero at every point outside that domain: a point in the excluded inner disk can be joined to zero within that disk and then to infinity through the lower half-plane, avoiding the contour; a point in the lower closed half-plane has the same outside path. CX18 therefore gives zero integral on this contour. Let \(\delta\downarrow0\). Uniform continuity of \(Q\) on the relevant compact closure, the explicit circle/segment parameterizations, and their bounded lengths make each piece converge to the corresponding horizontal segment or circular arc integral. Then let \(a\downarrow R\), \(b\uparrow L\), with the same compact continuity bound. The inner arc retains its clockwise orientation, and the outer arc is counterclockwise, producing exactly CX26.

Subtracting the two definitions CX25 at radii \(L\) and \(R\) gives precisely the left side of CX26: the difference of the real pieces is \(\int_{R<|t|<L}Q(t)dt\). Thus the radius is independent, with neither a discarded arc nor a sign change.

Suppose \(Q_1,Q_2\) are two admissible subtractions. Increase \(R\) if necessary so both are defined on the same original exterior, and set \(H=Q_1-Q_2\). The two real-tail remainders give \(H(t)=O(|t|^{-2})\). CX22--CX24 prove the full bound \(|H(\zeta)|\leq C|\zeta|^{-2}\) throughout that exterior. Its outer arc in CX26 has modulus at most \(\pi L\,CL^{-2}=\pi C/L\), tending to zero. Its real tails are absolutely integrable, so letting \(L\to\infty\) gives

\[
\int_{|t|>R}H(t)dt
 +\int_\pi^0H(Re^{i\theta})Ri e^{i\theta}d\theta=0 .
\tag{CX27}
\]

The difference of CX25 for \(Q_1,Q_2\) is the negative of this entire expression, hence zero. This proves independence of the subtraction from its actual growth and matching hypotheses.

For rational \(q\) with no real pole, choose \(R\) beyond every pole and set \(Q=q\) on that exterior. The tail difference is exactly zero. The remaining real interval minus the clockwise arc is the positively oriented upper half-disk boundary. CX20 and its proved half-disk winding therefore give the complete original conclusion

\[
\mathcal I_+(q)=2\pi i
 \sum_{\operatorname{Im}a_j>0}
           \frac{g_j^{(m_j-1)}(a_j)}{(m_j-1)!},
\qquad
g_j(\zeta)=(\zeta-a_j)^{m_j}q(\zeta).
\tag{CX28}
\]

All pole orders and the polynomial part are allowed. In the original example \(q(t)=t/(t^2+1)\), its upper pole at \(i\) has residue \(i/(2i)=1/2\), so \(\mathcal I_+(q)=i\pi\). Its symmetric real principal value is zero by oddness on every finite symmetric interval. The different answers retain the actual arc term; they do not result from replacing one integral definition with the other.

For the original parameter version let \(F(\zeta,s)\) be jointly continuous on the closed upper half-plane times its parameter space, holomorphic in \(\zeta\) in the open half-plane, and bounded there uniformly for \(s\) in each specified compact parameter set. Then \(QF\) is an admissible subtraction for \(qF\):
\((q-Q)F\) is bounded by the actual integrable tail \(|q-Q|\) times that parameter bound, and \(QF\) retains polynomial growth. In CX25 its interval and arc remain compact, and its tail has this common envelope. Dominated convergence proves continuity in \(s\), including every endpoint which belongs to the given closed parameter space. For complex parameters in an open domain with holomorphic \(F\) and the same compact-parameter envelope, CX10--CX11 prove holomorphic dependence and all allowed differentiated formulas. For real derivatives their full differentiated integrands need the corresponding common envelopes; then the proved real dominated-integral map gives the same result. The radius and all three original integration pieces remain fixed on that parameter neighborhood, so no parameter endpoint or contour derivative is silently omitted.

### 16.8. The original Gamma integral, every pole and the full reciprocal comparison

For \(\operatorname{Re}z>0\), retain the original Euler integral

\[
\Gamma(z)=\int_0^\infty e^{-u}u^{z-1}du,
\qquad u^{z-1}=\exp((z-1)\log u)\quad(u>0).
\tag{CX29}
\]

On a compact parameter set choose \(0<\sigma\leq\operatorname{Re}z\leq M\). The absolute integrand is bounded by
\(e^{-u}(u^{\sigma-1}+u^{M-1})\), integrable at both original endpoints. Every parameter derivative adds its actual factor \((\log u)^j\). Near zero its absolute integral is bounded by
\(\int_0^1u^{\sigma-1}|\log u|^jdu=j!/\sigma^{j+1}\):
put \(u=e^{-v}\) and integrate \(v^je^{-\sigma v}\) by parts \(j\) times, retaining its zero endpoint terms. At infinity, \(\log u\leq u\) and an exponential dominates each original finite power, by the real exponential series. Thus every differentiated integrand has an integrable compact-parameter envelope. CX10 proves holomorphy and every derivative of the original Gamma integral.

For each integer \(N\geq1\), integration by parts \(N\) times gives

\[
\begin{aligned}
B(z,N+1)&=\int_0^1t^{z-1}(1-t)^Ndt
              =\frac{N!}{z(z+1)\cdots(z+N)},\\
N^zB(z,N+1)&=\int_0^N u^{z-1}(1-u/N)^Ndu
                 \longrightarrow\Gamma(z).
\end{aligned}
\tag{CX30}
\]

One integration has zero boundary values because \(\operatorname{Re}z>0\) and the remaining positive power vanishes at one; it gives \(N/z\) times the integral with parameters \(z+1,N\). The last integral is \(1/(z+N)\), with its endpoint at one retained. For \(N=0\) the initial integral is directly \(1/z\). In the second line the change \(u=Nt\) retains the entire factor \(N^z\). Extend the integrand by zero for \(u\geq N\). On \(0<u<N\), the inequality \((1-u/N)^N\leq e^{-u}\) follows from \(\log(1-v)\leq-v\), proved by integrating its negative derivative. The preceding envelope therefore gives convergence uniformly on compact \(z\)-sets, with both integration endpoints retained.

Let \(H_N=\sum_{k=1}^N1/k\). Its original difference satisfies
\[
(H_{N+1}-\log(N+1))-(H_N-\log N)
 =\frac1{N+1}-\log(1+1/N)<0 .
\tag{CX31}
\]
The inequality follows by integrating \(1/t>1/(N+1)\) from \(N\) to \(N+1\). The comparison \(H_N\geq\int_1^{N+1}dt/t=\log(N+1)\) bounds this decreasing sequence below. Its real limit is the original constant \(\gamma\). The exact reciprocal of the second line in CX30 is the entire finite product

\[
P_N(z)=zN^{-z}\prod_{k=1}^N(1+z/k)
 =z\exp\bigl(z(H_N-\log N)\bigr)
              \prod_{k=1}^N(1+z/k)e^{-z/k}.
\tag{CX32}
\]

To prove its whole-plane limit, on \(|z|\leq R\) take an integer \(K>2R\). For \(k>K\), use the actual local logarithm series at one:

\[
\log(1+z/k)-z/k
 =\sum_{j=2}^\infty\frac{(-1)^{j+1}}j(z/k)^j,\qquad
|\log(1+z/k)-z/k|\leq 2R^2/k^2 .
\tag{CX33}
\]

The series derivative is the geometric sum \(1/(1+z/k)\) times \(1/k\); its value at zero is zero, so exponentiating gives exactly \(1+z/k\). Thus no branch is chosen across a zero of a finite initial factor. The tail logarithms converge uniformly on that disk. Their first derivatives are \(-z/[k(k+z)]\), bounded by \(2R/k^2\). At order \(j\geq2\), their derivatives are
\((-1)^{j-1}(j-1)!/(k+z)^j\), bounded by
\(2^j(j-1)!/k^j\). All derivative series therefore converge uniformly on smaller disks, or equivalently by the proved locally uniform holomorphic limit theorem. Keeping the first \(K\) factors exactly and exponentiating the convergent tail proves an entire function

\[
G(z)=z e^{\gamma z}\prod_{k=1}^\infty(1+z/k)e^{-z/k},
\qquad G(z)\Gamma(z)=1\quad(\operatorname{Re}z>0).
\tag{CX34}
\]

The second identity follows because \(P_N(z)N^zB(z,N+1)=1\) exactly for every \(N\), and both original factors converge locally uniformly. This fixes the full comparison constant; \(G\) is an auxiliary reciprocal, not a working replacement for \(\Gamma\).

The tail exponential is never zero. The retained finite factors therefore show that \(G\) has precisely the simple zeros \(0,-1,-2,\ldots\). It has no other zero anywhere in the plane. Its reciprocal consequently gives the unique meromorphic continuation of the original \(\Gamma\), with no zeros, and simple poles precisely at those points. Directly \(P_N(1)=(N+1)/N\), so \(G(1)=1\). Integration by parts in CX29, with its actual vanishing endpoints, gives \(\Gamma(z+1)=z\Gamma(z)\) on the right half-plane. Hence \(G(z)=zG(z+1)\) there; the identity theorem extends this entire identity to every \(z\). Iteration at the original pole \(-m\), \(m\in\mathbb N_0\), gives

\[
\begin{aligned}
G(z)&=z(z+1)\cdots(z+m)G(z+m+1),\\
G'(-m)&=(-1)^m m!,&
\operatorname{Res}_{z=-m}\Gamma(z)&=\frac{(-1)^m}{m!}.
\end{aligned}
\tag{CX35}
\]

For the derivative, exactly the factor \(z+m\) vanishes; its derivative is one. The product of the others at \(-m\) is \((-1)^m m!\), and the last factor is \(G(1)=1\). At \(m=0\) this is the empty product one. Taking the reciprocal of the local series with this nonzero linear coefficient gives the stated residue. Every original pole, sign and factorial is retained.

### 16.9. The full beta and duplication identities

We first prove the nonlinear measure substitution actually needed here. Let \(F:U\to V\) be a \(C^1\) diffeomorphism between open subsets of the original \(\mathbb R^d\), with its actual \(C^1\) inverse. For \(d\geq1\), use the original maximum coordinate norm only as an auxiliary comparison norm; the coordinates and map remain unchanged. The determinant \(J(x)=|\det DF(x)|\) is positive and continuous. Let \(Q\subset U\) be a closed coordinate cube with compact closure in \(U\), subdivide it into \(N^d\) cubes of side \(h\), and denote a child center by \(a\) and its actual derivative by \(A=DF(a)\). On the fixed compact cube, let \(M=\sup\|DF(x)^{-1}\|_\infty<\infty\), and let \(\delta(h)\) bound \(\|DF(x)-DF(a)\|_\infty\) on each child. Uniform continuity makes \(\delta(h)\to0\). The segment fundamental theorem gives the entire error, without replacing \(F\) by \(A\):

\[
\begin{aligned}
F(a+v)&=F(a)+Av+R_a(v),&
R_a(v)&=\int_0^1(DF(a+tv)-A)v\,dt,\\
E_a(v)&=A^{-1}R_a(v),&
\|E_a(v)\|_\infty&\leq M\delta(h)h/2
       \quad(\|v\|_\infty\leq h/2).
\end{aligned}
\tag{CX35a}
\]

Take \(N\) large enough that \(M\delta(h)<1\). In the image coordinates \(w=A^{-1}(y-F(a))\), the image of the child cube lies in the cube of half-side \((1+M\delta(h))h/2\). It contains the open cube of half-side \((1-M\delta(h))h/2\). To prove the latter inclusion, follow the segment \(y(s)=F(a)+sAw\), \(0\leq s\leq1\), for such a \(w\). Its initial point belongs to the open image of the child interior, because the given inverse is continuous. If the segment first leaves this open image, compactness of the closed child and continuity of \(F^{-1}\) place that first exit on the image of its boundary. At a boundary point some original coordinate of \(v\) has modulus \(h/2\), so CX35a gives \(\|v+E_a(v)\|_\infty\geq(1-M\delta(h))h/2\), contrary to the strict bound on every \(sw\). The image of the child interior has boundary exactly the image of the child boundary, since \(F\) and its inverse are continuous on a neighborhood of that compact child. Thus the first-exit argument uses the actual image, not an assumed surjectivity of a linear approximation.

The affine measure formula and those two inclusions give

\[
(1-M\delta(h))^d|\det A|h^d
 \leq |F(Q_a)|\leq
(1+M\delta(h))^d|\det A|h^d.
\tag{CX35b}
\]

Every original child face and its image are null. The face itself is a coordinate hyperplane piece. On the compact original cube, the segment derivative bound makes \(F\) Lipschitz with a finite constant \(L\). Cover a face of side \(s\) by at most \(C N^{d-1}\) coordinate pieces of diameter at most \(ds/N\). Each image lies in a coordinate cube of side at most \(2Lds/N\). The sum of their volumes is at most \(C N^{d-1}(2Lds/N)^d\), tending to zero. For \(d=1\), the faces are finite sets of points and this same estimate has \(N^0\) pieces. The face constants and original coordinate lengths are retained. Since \(F\) is injective, distinct child images overlap only on these null image faces. Sum CX35b over all children. The determinant sums are Riemann sums for the continuous original \(J\). Their upper and lower bounds have limits \(\int_QJ(x)\,dx\), proving \(|F(Q)|=\int_QJ(x)\,dx\).

For Borel \(E\subset U\), both \(\lambda(E)=|F(E)|\) and \(\nu(E)=\int_EJ(x)\,dx\) are measures: \(F\) is a homeomorphism, hence carries Borel sets to Borel sets, and its injectivity preserves disjoint unions. Half-open dyadic cubes with closures inside \(U\) form an intersection-closed countable generating family covering \(U\); cubes in one dyadic grid are either nested or disjoint. Removing their null faces from the closed-cube equality proves equality on each such cube and its intersections with the family. The finite-measure generating-family theorem on each covering cube, followed by a countable disjoint localization of that cover, proves \(\lambda=\nu\) on all Borel sets of \(U\). They are finite on each compact covering cube. Since \(J\) is positive, \(\int_EJ=0\) is equivalent to \(|E|=0\): intersect with the countable sets \(J\geq1/k\) for the reverse implication. Equality of the measures therefore preserves null sets in both directions. The Borel-set-plus-subset-of-a-Borel-null-set description of completion proves the same assertions for every completed Lebesgue measurable set and function. Indicators, increasing simple approximations and the four real and imaginary parts now prove the full substitution:

\[
\int_V f(y)\,dy
 =\int_U f(F(x))\,|\det DF(x)|\,dx.
\tag{CX35c}
\]

This holds with \(+\infty\) allowed for every nonnegative measurable \(f\). For complex \(f\), it holds precisely when either, and hence both, of the corresponding absolute integrals is finite. Applying it to the actual inverse gives the converse formula with \(|\det DF^{-1}|\); the determinant chain rule retains both factors and proves their product one. In dimension zero the spaces have their single point, the empty determinant and mass are one, and the same formula is immediate. This proves the needed measure theorem, including completed measurability and orientation reversal, from the original affine formula and finite calculus.

For \(\operatorname{Re}z>0,\operatorname{Re}w>0\), define the original beta integral and retain the whole change of variables

\[
\begin{aligned}
B(z,w)&=\int_0^1t^{z-1}(1-t)^{w-1}dt,\\
x&=ut,\quad y=u(1-t),\quad u=x+y>0,\quad t=x/(x+y)\in(0,1),\\
\left|\det\frac{\partial(x,y)}{\partial(u,t)}\right|&=u,\\
\Gamma(z)\Gamma(w)
 &=\int_0^\infty\int_0^\infty
            e^{-x-y}x^{z-1}y^{w-1}dx\,dy\\
 &=\int_0^\infty\int_0^1
   e^{-u}(ut)^{z-1}(u(1-t))^{w-1}u\,dt\,du
 =\Gamma(z+w)B(z,w).
\end{aligned}
\tag{CX36}
\]

The absolute product integral is finite because its two original one-variable absolute integrals have positive real exponents. The diffeomorphism has precisely the displayed positive absolute determinant and both inverse maps. Apply completed-measure substitution and absolute complex Fubini, already proved in the integration chapter. Positive real \(u,t,1-t\) have real logarithms, so the power product is exactly
\(u^{z+w-2}t^{z-1}(1-t)^{w-1}\), with the additional Jacobian \(u\) still present. This proves CX36, including every factor and endpoint. On compact parameter sets the corresponding logarithmic derivatives are integrable at zero and one, by the same power/log integral bounds as for CX29. CX11 proves joint holomorphy. Since \(\Gamma(z+w)\ne0\), its exact quotient is
\(B(z,w)=\Gamma(z)\Gamma(w)/\Gamma(z+w)\) in this original convergence domain. The explicit meromorphic function \(\Gamma(z)\Gamma(w)G(z+w)\) continues that integral. Uniqueness follows by the one-variable identity theorem first in \(z\), for every \(w\) in the original right half-plane, then in \(w\) for fixed \(z\) away from the poles; clearing local denominators extends the equality through their meromorphic charts. This asserts the continuation, without suppressing any intersection cancellation or assigning a value to a divergent endpoint integral.

For \(\operatorname{Re}z>0\), first substitute \(t=(1+v)/2\) in \(B(z,z)\), retaining \(dt=dv/2\) and \(t(1-t)=(1-v^2)/4\). Then use evenness and \(s=v^2\):

\[
\begin{aligned}
B(z,z)&=2^{1-2z}\int_{-1}^1(1-v^2)^{z-1}dv
       =2^{1-2z}B(1/2,z),\\
\Gamma(z)^2\Gamma(z+1/2)
       &=2^{1-2z}\Gamma(1/2)\Gamma(z)\Gamma(2z),\\
\Gamma(1/2)
       &=\int_0^\infty e^{-v^2}(v^2)^{-1/2}\,2v\,dv
         =2\int_0^\infty e^{-v^2}dv=\sqrt{\pi},\\
\Gamma(2z)&=2^{2z-1}\pi^{-1/2}\Gamma(z)\Gamma(z+1/2).
\end{aligned}
\tag{CX37}
\]

The half-interval substitution contributes \(ds/(2\sqrt s)\); the two symmetric intervals cancel exactly that factor two, producing the full \(B(1/2,z)\) integral. The second line is CX36 with both original Gamma denominators multiplied out. Nonvanishing of the original \(\Gamma(z)\) permits the stated comparison to the last line. The Gaussian value uses the integration chapter's proved original polar integral and original circle constant. For its \(v=0\) endpoint, perform the substitution on positive truncated intervals and pass by absolute convergence. The last line is therefore exactly the original duplication identity, with its factors of two and pi fixed. Both sides are meromorphic functions of \(z\), and CX7 extends their equality from the right half-plane to their actual meromorphic domain.

We also prove the full sphere density before using it in an arbitrary dimension. Let \(n\geq2\), \(S^{n-1}=\{\theta\in\mathbb R^n:\sum_{j=1}^n\theta_j^2=1\}\), with its original Euclidean surface measure \(dS\). On the hemisphere \(\epsilon\theta_i>0\), \(\epsilon\in\{1,-1\}\), use the actual graph coordinates \(u=(\theta_j)_{j\ne i}\), \(|u|<1\), and \(h(u)=\theta_i=\epsilon\sqrt{1-\sum_{j\ne i}u_j^2}\). The coordinate tangent Gram matrix and radial Jacobian are

\[
\begin{aligned}
\partial_{u_j}h&=-u_j/h,&
\mathcal G_{jk}&=\delta_{jk}+u_ju_k/h^2,\\
\det\mathcal G&=1+\sum_{j\ne i}u_j^2/h^2=1/h^2,&
\sqrt{\det\mathcal G}&=1/|h|,\\
\Phi_{i,\epsilon}(r,u)&=r\theta(u),&
|\det D\Phi_{i,\epsilon}|&=r^{n-1}/|h|
                  =r^{n-1}\sqrt{\det\mathcal G}.
\end{aligned}
\tag{CX37a}
\]

For the Gram determinant, multilinearity in its columns leaves the identity determinant and the \(n-1\) terms with exactly one column from \(u u^T/h^2\); terms with two such columns vanish because those columns are dependent. The remaining terms are \(u_j^2/h^2\). For the radial determinant, factor \(r\) from each of the \(n-1\) angular columns. After placing the \(i\)-th row first, its block columns are \((h,u)^T\) and \((-u_j/h,e_j)^T\). Adding \(\sum u_j/h\) times the respective lower rows to the first row makes its first entry \(h+\sum u_j^2/h=1/h\) and its other entries zero. The row permutation affects the sign only, so the absolute determinant is exactly the displayed value. The inverse on the cone \(\epsilon x_i>0\) is \(r=|x|\), \(u=(x_j/|x|)_{j\ne i}\); both maps are smooth with nonzero Jacobian.

The density \(\sqrt{\det\mathcal G}\,du\) is the original Euclidean surface density, not a radial definition substituted for it. On overlapping graph charts, the tangent chain rule gives \(\mathcal G_u=(DT)^T\mathcal G_vDT\), hence \(\sqrt{\det\mathcal G_u}=\sqrt{\det\mathcal G_v}|\det DT|\). CX35c in dimension \(n-1\) proves equality of their integrals. This verifies that the graph densities define one coordinate-independent completed surface measure.

For a finite smooth partition on these hemispheres, take the already constructed smooth function \(\chi\geq0\) which vanishes at nonpositive inputs and is positive at positive inputs. Put \(c=1/(2\sqrt n)\), \(b_{i,\epsilon}(\theta)=\chi(\epsilon\theta_i-c)\), and \(b(\theta)=\sum_{i,\epsilon}b_{i,\epsilon}(\theta)\). Some coordinate has modulus at least \(1/\sqrt n\), since their full squares sum to one, so \(b>0\). The functions \(\rho_{i,\epsilon}=b_{i,\epsilon}/b\) sum to one; their supports are inside the respective hemispheres and have \(|h|\geq c\). For nonnegative measurable \(f\), apply CX35c to each actual radial chart with the factor \(\rho_{i,\epsilon}(x/|x|)\), then add all \(2n\) terms. Each cone chart has its own original inverse and Jacobian. The origin has original \(n\)-dimensional measure zero, and the partition sums to one at every other point. Thus

\[
\int_{\mathbb R^n}f(x)\,dx
 =\sum_{i=1}^n\sum_{\epsilon\in\{1,-1\}}
   \int_0^\infty\int_{|u|<1}
      f(r\theta(u))\rho_{i,\epsilon}(\theta(u))
          r^{n-1}|h(u)|^{-1}\,du\,dr
 =\int_0^\infty\int_{S^{n-1}}f(r\theta)r^{n-1}\,dS(\theta)\,dr.
\tag{CX37b}
\]

Every term is nonnegative, so Tonelli allows infinite values and either order. Applying the same formula to \(|f|\) proves its exact absolute-integrability condition; the four component integrals give the complex formula in that domain. The support condition \(|h|\geq c\) bounds every angular density, so the finite chart cover gives finite surface mass. It is positive because one nonempty open graph patch has a strictly positive density. The radius-zero endpoint may be added with weighted integrand zero; it contributes no mass.

For \(n=1\), use the two original maps \(r\mapsto r\) and \(r\mapsto-r\) from \(r>0\), both with absolute derivative one. The sphere \(S^0=\{1,-1\}\) has counting measure, so CX37b holds with its two terms and \(r^{n-1}=1\). No angular chart of negative dimension is used. For every \(n\geq1\), the original Cartesian Gaussian and CX37b therefore give

\[
\begin{aligned}
(\sqrt\pi)^n
 &=\int_{\mathbb R^n}\prod_{j=1}^n e^{-x_j^2}\,dx
 =|S^{n-1}|\int_0^\infty e^{-r^2}r^{n-1}\,dr\\
 &=|S^{n-1}|\int_0^\infty e^{-s}
                    (\sqrt s)^{n-1}\frac{ds}{2\sqrt s}
 =\frac{|S^{n-1}|}{2}\Gamma(n/2),\\
|S^{n-1}|&=\frac{2\pi^{n/2}}{\Gamma(n/2)}.
\end{aligned}
\tag{CX37c}
\]

The substitution is first on positive finite intervals; absolute convergence then passes both endpoints. The Cartesian factors are the integration chapter's independently proved original Gaussian values. The radial factor is finite and positive by CX29. This fixes the entire original sphere coefficient, including its factor two. At \(n=1\), \(\Gamma(1/2)=\sqrt\pi\) gives the original counting mass two.

Consequently the original ball integral in WHK follows, for \(n\geq1\) and \(\operatorname{Re}\lambda>(n-1)/2\), from this full polar density and \(s=r^2\):

\[
\begin{aligned}
\int_{|y|<1}(1-|y|^2)^{\lambda-(n+1)/2}dy
 &=\frac{2\pi^{n/2}}{\Gamma(n/2)}
       \int_0^1 r^{n-1}(1-r^2)^{\lambda-(n+1)/2}dr\\
 &=\frac{\pi^{n/2}}{\Gamma(n/2)}
       B\bigl(n/2,\lambda+(1-n)/2\bigr)\\
 &=\pi^{n/2}
       \frac{\Gamma(\lambda+(1-n)/2)}{\Gamma(\lambda+1/2)}.
\end{aligned}
\tag{CX38}
\]

The original sphere coefficient is CX37c, proved above using every original radial and angular Jacobian. Both beta parameters have positive real part, exactly the displayed convergence condition. For \(n=1\), the sphere has its two original endpoints and coefficient two; the same calculation includes both half-intervals. In dimension zero the ball is a single point with mass one; the rightmost Gamma quotient is also one wherever its original integral comparison is used, so no zero-dimensional sphere formula or negative-dimensional Jacobian is introduced.

### 16.10. The original Laplace branch and every dominated derivative

On the right half-plane \(p=x+iy\), \(x>0\), take
\(\operatorname{Log}p=\frac12\log(x^2+y^2)+i\arctan(y/x)\),
using the actual real logarithm and principal arctangent. Direct differentiation gives
\(\partial_x\operatorname{Log}p=(x-iy)/(x^2+y^2)=1/p\) and
\(\partial_y\operatorname{Log}p=i/p\). The proved real differentiability remainder therefore gives complex derivative \(1/p\). The branch is holomorphic, real on \(p>0\), and has argument in \((-\pi/2,\pi/2)\).

For \(\operatorname{Re}p>0,\operatorname{Re}z>0\), the original Laplace identity is

\[
\int_0^\infty e^{-pt}t^{z-1}dt
       =\Gamma(z)\exp(-z\operatorname{Log}p)
       =\Gamma(z)p^{-z}.
\tag{CX39}
\]

For positive real \(p\), the change \(u=pt\) retains the full factor \(p^{-z}\) and reduces the integral exactly to CX29. For fixed \(z\), both sides are holomorphic in the entire original right half-plane. On compact parameter sets choose \(\operatorname{Re}p\geq\delta>0\) and \(0<\sigma\leq\operatorname{Re}z\leq M\). Every mixed derivative of the integrand is its full factor
\((-t)^a(\log t)^b e^{-pt}t^{z-1}\).
The power/log estimates at zero and the exponentially decaying bound at infinity give a common integrable envelope for every fixed pair \(a,b\). CX11 proves joint holomorphy and all derivative interchanges. The identity theorem in \(p\), from its positive-real accumulation set inside the domain, now proves CX39 at every allowed complex \(p\).

In particular, with \(a,b\in\mathbb N_0\), the complete differentiated receiving identity is

\[
\begin{aligned}
\int_0^\infty(-t)^a(\log t)^b e^{-pt}t^{z-1}dt
 &=(-1)^a p^{-z-a}
       \sum_{c=0}^b\binom bc\Gamma^{(c)}(z+a)
                            (-\operatorname{Log}p)^{b-c},\\
\Gamma(z+a)&=\Gamma(z)\prod_{j=0}^{a-1}(z+j).
\end{aligned}
\tag{CX40}
\]

For the first line, initially differentiate in \(p\) \(a\) times in the actual integral; it is \((-1)^a\Gamma(z+a)p^{-z-a}\) by CX39. Differentiate in \(z\) \(b\) times, retaining every Leibniz term, sign and logarithmic power. The second line is the entire original Gamma recursion; at \(a=0\) its empty product is one. Thus a shifted Gamma factor is explicitly compared with the original Gamma, rather than absorbing its product into a different object.

On the upper half-plane the branch \(\operatorname{Log}_+\zeta=\operatorname{Log}(-i\zeta)+i\pi/2\) retains argument \((0,\pi)\) and derivative \(1/\zeta\). Consequently its continuous boundary powers on the positive and negative real rays have ratio \(e^{i\pi v}\) for every original complex exponent \(v\), as required by T6. For \(p=\epsilon+i\tau\), \(\epsilon>0\), the branch in CX39 tends, at each \(\tau\ne0\), to
\(\log|\tau|+i\pi\operatorname{sgn}\tau/2\).
Thus its negative power has negative-ray/positive-ray ratio \(e^{i\pi z}\), with the full \(\Gamma(z)\) factor still present in the unnormalized integral. Passage at \(\tau=0\) is the original distributional damping and Taylor-subtraction construction, never substitution into a divergent point value.
