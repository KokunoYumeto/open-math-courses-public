# Singularities along a submanifold and smooth boundary passage

A distribution can be rough across a submanifold while remaining stable under every derivative tangent to it. That stability identifies its normal-frequency amplitude, including its exact limiting regularity. At a boundary, the positive and negative normal frequencies carry additional information: a relation between their homogeneous coefficients decides whether applying an operator leaves a smooth function on the interior side. We develop that relation for every complex type, and then compute the boundary operators produced by simple and multiple layers.

We use the Fourier convention and quadratic multiplier estimates of AN03-U002, the local symbol tools of AN03-U001, and the distributional quantizations and classical symbol changes of AN03-U004. The Fourier transform is \(\widehat f(\xi)=\int e^{-ix\cdot\xi}f(x)\,dx\), its inverse has coefficient \((2\pi)^{-n}\), and \(D=-i\partial\). Schwartz Plancherel and its unitary \(L^2\) extension are used with these constants. Basic prerequisites are distributional differentiation and tensor products, finite-dimensional calculus, smooth charts and bundles, partitions of unity, dominated convergence, and the elementary Cauchy integral and maximum principles. Coordinate changes of classical operator symbols are derived below by amplitude reduction, using the stated quadratic-multiplier prerequisite. The normal-form, endpoint, transmission and boundary-symbol assertions are proved in this unit.

In local coordinates write \(x=(t,z)\in\mathbb R^k\times\mathbb R^{n-k}\), with dual variables \((\tau,\eta)\), and let \(Y=\{t=0\}\). For the nontrivial normal-frequency discussion \(1\leq k\leq n\). Codimension zero gives only smooth distributions and is treated by the same tangent-regularity definition with no normal frequency. An ordinary symbol \(a(z,\tau)\) of real order \(r\) satisfies
\[
|\partial_z^\beta\partial_\tau^\alpha a(z,\tau)|
\leq C_{K,\alpha,\beta}\langle\tau\rangle^{r-|\alpha|}
\quad(z\in K),\qquad \langle\tau\rangle=(1+|\tau|^2)^{1/2}.
\tag{C1}
\]
The global symbol class uses constants uniform in the base variables; the local class uses each compact set \(K\). Additional normal base variables \(t\) count as base variables in this definition. Finite-dimensional vector and matrix norms give the corresponding bundle-chart versions. Complex polyhomogeneous orders always refer to ordinary estimates of the real part of the order.

Throughout AN03-CN-001–AN03-CN-007, \(\Psi^d\) denotes operators with ordinary \(S^d_{1,0}\) symbols; no polyhomogeneous expansion is assumed. A polyhomogeneity hypothesis is always stated expressly. The transmission theory uses the classical expansions specified in AN03-TR-003.

## AN03-CN-001 — The endpoint is a Besov endpoint

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

Third, local Sobolev estimates in frequency space will be used below. On a fixed pair of nested balls, any derivative of a smooth function at a point of the smaller ball is bounded by the \(L^2\) norms of finitely many derivatives on the larger ball. Multiply by a cutoff equal to one on the smaller ball and apply Fourier inversion, Cauchy–Schwarz with \(\langle\zeta\rangle^{-s}\), \(s>n/2\), and Plancherel, exactly as in AN03-GAU-002. Translation gives constants independent of the center. This proves the local estimate from the stated Fourier prerequisites.

## AN03-CN-002 — Oscillatory amplitudes and removal of normal base variables

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

For the estimates apply AN03-GAU-008 to the phase \(-\langle D_t,D_\tau\rangle\), treating \(z\) as a passive variable. Use the metric
\(|dt|^2+|dz|^2+\langle\tau\rangle^{-2}|d\tau|^2\) and weight \(\langle\tau\rangle^r\). This metric is slowly varying. Its phase-dual distance is finite only for equal passive variables, and there it is a fixed factor times \(\langle\tau\rangle^2|\Delta t|^2+|\Delta\tau|^2\). Polynomial frequency-ratio bounds prove the required temperateness; they are the \((\rho,\delta)=(1,0)\) calculation in AN03-WP-008. The actual Gauss parameter at the observation point is \(1/(2\langle\tau\rangle)\). Restriction to \(t=0\) consequently gives exactly the order \(r-N\) remainder, including tangential derivatives. Bounded compactly supported approximation now extends the identity of distributions in (C5), using the defining estimate for (C4). The full quadratic multiplier acts on tempered distributions; its restriction in (C5) is asserted on these global symbol spaces, not on arbitrary tempered distributions for which restriction might be undefined.

For a local symbol, fix a compact working set inside its coordinate domain and a cutoff \(\chi(t,z)\) supported compactly in that domain and equal to one on a neighborhood of the working set. Extend \(a_\chi=\chi a\) by zero in the base variables. It is a global symbol of order \(r\), so (C5) applies to \(a_\chi\), and its inverse integral equals \(\chi u\) globally. It therefore equals the original \(u\) on the working neighborhood. Every remainder estimate is controlled by finitely many input seminorms on the fixed support of \(\chi\). At points \((0,z)\) where \(\chi\) is identically one nearby, all coefficients of the expansion are the derivatives of the original \(a\) at \(t=0\). Different such cutoffs give reduced amplitudes differing by \(S^{-\infty}\) locally in those \(z\)'s, since the expansion of their difference vanishes to every order. No global growth condition or global reduced representation is asserted for an uncut local symbol. We use this compact cutoff and zero-extension convention whenever (C5) is applied to local coordinates below.

## AN03-CN-003 — Energy on an annulus and regularity away from the submanifold

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
A frequency derivative lowers the order raised by the factor \(\tau_j\). Thus every product of \(D_{z_j}\) and \(t_iD_{t_j}\) preserves the endpoint just proved. Multiplication by smooth local coefficients preserves it by AN03-CN-001.

## AN03-CN-004 — Recovering the amplitude from tangent regularity

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

On the cone \(|\eta|\geq|\tau|\), use arbitrarily large tangential powers \(\eta^\beta\), with no normal powers. A unit ball about a large point in this cone is contained in a fixed enlargement of its dyadic annulus; at least one tangential coordinate is comparable to the radius on a smaller fixed ball. Formula (C11) bounds the \(L^2\) norm of every Fourier derivative on that ball by \(C R^{r+k/2-M}\), with arbitrary \(M\). The local Sobolev estimate in AN03-CN-001 then gives rapid decay of every derivative there. If there are no tangential variables, this cone has no large points and this step is unnecessary.

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

## AN03-CN-005 — Intrinsic conormality, bundles and operator action

Let \(X\) be a smooth \(n\)-manifold, \(Y\) a closed smooth embedded submanifold, and \(E\) a smooth complex vector bundle. For real \(m\), define \(I^m(X,Y;E)\) by requiring
\[
L_1\cdots L_Nu\in B^{-m-n/4}_{2,\infty,\mathrm{loc}}(X;E)
\tag{C15}
\]
for every \(N\geq0\) and every collection of first-order smooth operators on \(E\) whose principal symbols vanish on \(N^*Y\). The topology is generated by the local Besov seminorms of all these images. Chart and frame changes preserve those spaces by AN03-CN-001, and the principal-symbol vanishing condition is intrinsic, so this definition and topology are coordinate independent.

In a bundle frame, (C14) expresses every such operator as
\(L=\sum_j A_jM_j+A_0\), where the \(A_j\) are smooth endomorphisms and the generators \(M_j\) have scalar principal symbols. When a coefficient is moved to the left across such a generator, the commutator is order zero: its first-order matrix terms cancel because the principal part is scalar. Induction on the length of an operator product therefore expresses it as a finite sum of smooth endomorphisms times words in the \(M_j\)'s. Thus scalar-principal generators suffice even for systems; no assumption that the original operator has scalar matrix coefficients is made.

By AN03-CN-004, the local normal form for codimension \(k\) is exactly
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

## AN03-CN-006 — The intrinsic principal symbol and its normalization

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
Every base derivative of the composed symbol introduces a factor linear in \(\tau\) paired with a frequency derivative, so (C1) retains its order on compact coordinate sets. Frequency derivatives lower the order normally. Choose the compact base cutoff \(\chi\) of AN03-CN-002 equal to one on the working neighborhood and extend \(\chi A\) by zero. Reducing this global symbol by (C5) gives the exact amplitude
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

## AN03-CN-007 — Full action on amplitudes, not only leading symbols

Let \(P=p(x,D)\) have left symbol of order \(d\), and let \(u\) have the normalized reduced amplitude \(a(z,\tau)\) of (C18), of order \(r=m+(n-2k)/4\). Work first with compact input and output localization in one chart: the exact left symbol \(p\) is extended globally with compact base support, and \(a\) is the global reduced amplitude of the compactly localized input from AN03-CN-002. Thus both factors have global symbol bounds. The output amplitude of this localized operator and input is
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
This is the first quadratic multiplier in (C22), evaluated at \(w=z,\eta=0\). Its estimates follow directly from AN03-U002, including the passive variables. On the space of \((x,w,\tau,\eta)\), use
\[
G=|dx|^2+|dw|^2+\langle\tau\rangle^{-2}|d\tau|^2
+\langle(\tau,\eta)\rangle^{-2}|d\eta|^2,
\quad M=\langle(\tau,\eta)\rangle^d\langle\tau\rangle^r.
\tag{C24}
\]
The product symbol obeys these derivative bounds: derivatives of \(p\) in \(\tau\) cost at most \(\langle\tau\rangle^{-1}\), and those of \(a\) have exactly that cost. Small metric displacements preserve both brackets, so slow variation and local weight comparison hold. For the phase \(\langle D_w,D_\eta\rangle\), a finite phase distance keeps \((x,\tau)\) fixed. Relative to an observation point with \(\eta=0\), the \(\eta\)-part of \(G\) at any input point is no larger, while the remaining parts agree. The weight ratio is bounded by a power of \(1+|\eta|^2\), which the phase-dual distance controls. Thus the full hypotheses of the Gauss restriction theorem hold uniformly along \(w=z,\eta=0\). When \(n-k>0\), the parameter is \(1/(2\langle\tau\rangle)\). When \(k=n\), there are no tangential variables: this first reduction is ordinary multiplication, its phase and actual Gauss parameter are zero, and the zero-phase branch of AN03-GAU-008 applies. It gives \(a_1\in S^{d+r}\) and every remainder order \(d+r-N\), including parameter derivatives.

Now remove the normal base dependence of \(a_1\) by (C5). This gives the second multiplier and (C22). The constant-coefficient differential operators commute before restriction. Expanding the two finite Taylor polynomials and collecting terms of total degree less than \(N\) gives the stated single exponential expansion; each contraction lowers the order by one, and the discarded finite terms and both controlled remainders have order at most \(d+r-N\).

For general symbols, take bounded compactly supported approximants. The oscillatory definition, the two weak Gauss extensions, and the Schwartz action of ordinary \(S_{1,0}\) operators and their adjoints pass the equality to distributions. Explicitly, adjoints applied to a fixed Schwartz test function converge in Schwartz space: the classical estimates from AN03-WP-008 bound all output seminorms uniformly, local smooth convergence follows by dominated oscillatory integration, and a higher uniform decay seminorm controls the tails. Pair this convergence with the bounded, distributionally convergent input approximants. For the original local operator, proper support permits a compact input cutoff equal to one at all kernel input points over a fixed output compact set. Use a compact output cutoff equal to one on its working neighborhood. Splitting into chart pieces near the diagonal then gives the globally extended symbols just used. The remaining kernel pieces are separated from the diagonal, so frequency integration by parts makes their outputs smooth there; after compact output localization their normal Fourier transforms are \(S^{-\infty}\) amplitudes and are included in the local representation. This gives equality on the working neighborhood and every claimed local remainder without imposing growth at infinity on the original symbols. All estimates are componentwise, and (C20) glues the leading term, proving (C23) for bundle operators.

If the amplitudes and operator symbols have complex polyhomogeneous expansions in steps \(h=1/q\), \(q\) a positive integer, every coordinate and action formula above preserves that expansion. A frequency derivative lowers degree by an integer, which is \(q\) steps; multiplying homogeneous components adds their step indices. At each specified degree only finitely many indices contribute, and the remainder estimates just proved justify truncation. A common reciprocal-integer step may be chosen for two different such expansions. The boundary theory below uses step one, with degrees \(m-j\); its phase formulas are not assertions for arbitrary noninteger steps.

## AN03-TR-001 — What a normal-frequency tail does on one side

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

## AN03-TR-002 — Supported powers and the spaces of complex type

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

The space (T7) does not depend on the ambient extension of a boundary chart. The conormal change-of-coordinate proof in AN03-CN-006 gives the same polyhomogeneous class under any smooth extension, and support is intrinsic. Equivalently the local description just given glues by the bundle transition law. This treats arbitrary smooth vector bundles; finite-order Taylor coefficients and all constructions are taken componentwise in a frame.

Here is a concrete description of all its members, not only their leading terms:

* If \(\mu\notin\mathbb Z\), they have expansions
  \(\sum_{j\geq0}u_j(z)t_+^{j-\mu-1}\), with these powers interpreted by distributional continuation. After sufficiently many terms the remainder has any prescribed finite smoothness.
* If \(\mu\leq-1\) is an integer, they are exactly the zero extensions of smooth functions on \(\overline Y\) whose normal jets of orders less than \(-\mu-1\) vanish.
* If \(\mu\geq0\) is an integer, they are exactly a zero extension of a smooth function plus a finite sum \(\sum_{j=0}^{\mu}v_j(z)\delta^{(j)}(t)\), locally at the boundary.

To prove these descriptions, match successive Fourier coefficients using \(e_{j-\mu}\) in (T1)–(T2). Multiplication by a normal cutoff changes each Fourier expansion by lower terms only, which are matched successively; equivalently its cutoff is constant near the entire singular support, so the complementary part has a rapidly decreasing Fourier transform after compact localization. The difference after \(N\) terms has amplitude order \(\operatorname{Re}\mu-N\), hence is \(C^q\) for \(N>\operatorname{Re}\mu+q+1\). When \(\mu\) is not an integer, the gamma factors are nonzero and are absorbed in the coefficients of the stated powers. At integer \(\mu\), (T1) gives precisely the listed delta derivatives and nonnegative powers on the positive side. The smooth jet construction at the end of AN03-TR-001 realizes the latter coefficients by one smooth function on \(\overline Y\). The remaining amplitude is of every negative order, so its inverse is smooth; support makes it flat on the boundary. This proves exact membership statements, including their converses. One can also realize arbitrary infinite power expansions by multiplying the \(j\)-th term by a shrinking cutoff: the same \(2^{-j}\) construction is applied in successively weaker symbol orders, and then in each fixed finite distributional seminorm. This gives all the asserted asymptotic remainders.

For clarity, if \(f\) is smooth up to \(t=0\), compactly supported in a boundary chart, and \(f_0\) is its zero extension, its normal Fourier transform is
\[
\widehat {f_0}(z,\tau)=\int_0^\infty e^{-it\tau}f(t,z)dt
\sim-i\sum_{j\geq0}\tau^{-1-j}D_t^j f(0,z).
\tag{T9}
\]
Integrating by parts \(N\) times proves this expansion and its remainder. To differentiate it in \(\tau\), apply the same integration by parts to \((-it)^\alpha f\); its vanishing jets give the extra \(\alpha\) powers of decay. Tangential derivatives commute with the integral. Consequently (T9) is a full symbol expansion of degree \(-1\). The reduced amplitude in (C4) is \((2\pi)^{-1}\widehat {f_0}\), so the conormal order is exactly \(-(n+2)/4\), and these inputs form \(C_{-1}^\infty\). Arbitrary jets in (T9) can be prescribed by the smooth extension construction; two such amplitudes with identical jets differ by \(S^{-\infty}\).

For each integer \(N\geq0\), \(C_{\mu-N}^\infty\subset C_\mu^\infty\). Smooth multiplication preserves \(C_\mu^\infty\), by (C5) and support; a first-order derivative maps it into \(C_{\mu+1}^\infty\), by (C22) or direct differentiation of the power family. Tangential derivatives in a fixed boundary chart actually preserve its normal order. These inclusions will let us recover every jet in a transmission condition from an operator mapping property.

## AN03-TR-003 — All jets are necessary, at every complex type

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

## AN03-TR-004 — The invariant reflection of a classical operator

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
\(\sum_\alpha\partial_\eta^\alpha D_y^\alpha A(x,x,\eta)/\alpha!\) and remainder of order \(\operatorname{Re}m-N\) after \(|\alpha|<N\). For Schwartz amplitudes this follows by inserting the Fourier kernel and Fourier inversion; the sign also follows by moving \((y-x)^\alpha\) from a Taylor expansion onto the frequency derivative of the amplitude. For general amplitudes it is the same Gauss restriction as (C5), with the opposite sign and passive \(x\), metric \(|dy|^2+\langle\eta\rangle^{-2}|d\eta|^2\), and parameter \(1/(2\langle\eta\rangle)\). Thus AN03-U002 supplies every finite-seminorm remainder and the weak extension. A cutoff away from the diagonal gives a smooth kernel by repeated frequency integration by parts. This proves the full local coordinate formula needed here: all derivatives of the cutoff vanish on the working diagonal, and its value there is one. The discarded kernel pieces are smooth on the working chart and give smoothing symbol terms.

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
The tangential reduction argument in AN03-CN-007, with \(\xi\) as its retained frequency, gives the expansion and remainder of order \(\operatorname{Re}(m+m')-N\). The adjoint kernel has amplitude \(p(y,\xi)^*\); the reduction just proved gives its formula and remainder of order \(\operatorname{Re}m-N\). Schwartz identities pass to proper classical operators on distributions by the same Schwartz-adjoint convergence argument used after (C24). Thus these formulas do not assume the unresolved general-metric operator-composition extension.

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

## AN03-TR-005 — A normal integral defined by analytic subtraction

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

## AN03-TR-006 — Boundary traces of every layer order

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
The remainder is a symbol of the same order, locally uniformly in \(t\). Each frozen coefficient has an analytic subtraction. By AN03-TR-005 its oscillatory normal integral is \(\mathcal I_+(e^{it\cdot}\partial_t^l p(0,z,\cdot,\eta))\), continuous down to \(t=0\), with polynomial bounds in \(\eta\). Thus all terms with \(l>0\) tend to zero and the first gives (T19).

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

## AN03-CEX-001 — Three models that distinguish the hypotheses

**An endpoint measured by a sequence.** Let \(g\) be a nonzero smooth compactly supported function of \(z\), and set \(u=\delta(t)g(z)\) with \(k\) normal variables. On large frequency annuli its squared Fourier mass is comparable to \(R^k\). The upper estimate follows from (C7); for the lower estimate restrict \(\eta\) to a fixed ball on which \(\widehat g\) has positive squared integral and restrict \(\tau\) to a fixed subannulus of radius \(R\). Thus its dyadic sequence at \(s=-k/2\) is bounded above and below by positive constants. It belongs to \(B^{-k/2}_{2,\infty}\) and to no \(B^{-k/2}_{2,p}\) with finite \(p\); it belongs to every \(H^{-k/2-\epsilon}\), \(\epsilon>0\). The amplitude is order zero, so its intrinsic conormal order is \((2k-n)/4\). These are three compatible facts, not three different conventions for a Sobolev exponent.

**A complex order that distinguishes the two sides.** In one dimension let a classical symbol have homogeneous tails \(p_0(\tau)=\tau^i\) for \(\tau>0\) and \(p_0(\tau)=e^{-\pi}|\tau|^i\) for \(\tau<0\); smooth it near zero and localize its kernel properly. It satisfies ordinary transmission into \(t>0\): the ratio is \(e^{i\pi i}=e^{-\pi}\), and differentiation gives every higher frequency condition. There are no tangential frequencies, and the local symbol is independent of the base, so the other jets vanish. Into the opposite side, ordinary transmission would require \(1=e^{-2\pi}\), which fails. Type \(\mu'=-i\) does work on that side, since \(m+0+\mu'=0\) in (T15). The imaginary part of the type is mathematically active.

**Residues give a boundary operator.** At nonzero tangential frequency put \(a=|\eta|\) and take
\(p(\tau,\eta)=(\tau^2+a^2)^{-1}\). A smooth low-frequency extension makes a classical symbol of order \(-2\); proper localization changes only the local smoothing ambiguity. It has ordinary transmission, since each frequency derivative has the parity of its integer degree. The pole at \(\tau=ia\) has residue \((2ia)^{-1}\), so (T20) gives principal boundary symbol \(1/(2|\eta|)\), of order \(-1\). One normal derivative gives the principal symbol \(i/2\), and two give \(-|\eta|/2\). Directly, the inverse normal transform is \(e^{-a t}/(2a)\) for \(t>0\), and applying \(D_t=-i\partial_t\) confirms each value and sign. The polynomial part of \(\tau^2/(\tau^2+a^2)\) has plus integral zero, as (T17) requires.

## AN03-CPS-001 — Problems with full solutions

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

## References, prerequisites and further questions

The mathematical antecedent is Lars Hörmander, *The Analysis of Linear Partial Differential Operators III*, second printing with corrections (1994), §18.2 and Appendix B. The present proofs have been written independently, with their Fourier and half-density conventions made explicit. The exact dyadic endpoint is also stated in [Sá Barreto and Wang's author draft on triple interactions](https://www.math.purdue.edu/~sabarre/Papers/TripleInt.pdf), dated 25 October 2018, §2.1; that discussion refers elsewhere for its normal-form equivalence. It is not used here as a proof of the compact converse or the bundle symbol theorem.

[Grubb's 2014 version of the work on fractional Laplacians and transmission spaces](https://arxiv.org/pdf/1310.0951v5), §2, provides a useful comparison of the complex-type condition. Its supported-space parameter \(\nu\) corresponds to \(\nu=-\mu-1\) here; using \(-\mu\) would give the same phase but a different space. [Grubb's chapter on boundary operators](https://web.math.ku.dk/~grubb/dist10.pdf), §§10.3–10.4, gives a Laurent-symbol comparison for the upper residue integral. The general analytic subtraction lemma and the full complex-order remainder estimates required here have been proved above. These links are reading references, not imports of prose, figures or licensed proof text.

The exact advanced prerequisites are the symbol cutoff/localization bounds of AN03-U001; the possibly degenerate Gauss multiplier, its restriction theorem, finite-seminorm remainders and weak extension in AN03-GAU-008; and the distributional Fourier kernels, quantization changes, classical Schwartz estimates and \(L^2\) Fourier extension in AN03-WP-004, AN03-WP-005 and AN03-WP-008. The elementary entry base listed at the start includes Schwartz density and completeness of \(L^2\), so the extension from Schwartz Plancherel is legitimate. The local symbol coordinate, product and adjoint formulas used here have been derived with complete remainder orders from these prerequisites. General compatible-metric operator composition remains a separate course obligation and is not used as an unproved substitute for these classical local calculations.

A natural next question is how the collection of layer traces combines into a projection onto boundary data of solutions. The residue model gives a concrete starting point, while the all-jet transmission criterion identifies which operators admit those traces in the smooth category. For noninteger type, the spaces in (T7) suggest the appropriate weighted boundary data instead of ordinary smooth zero extensions. Those elliptic projection, solvability and weighted mapping theorems require additional arguments and are not consequences asserted by this unit.

This is an independently authored unit at its declared prerequisites.
