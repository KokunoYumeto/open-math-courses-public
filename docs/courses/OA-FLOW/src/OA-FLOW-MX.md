# Normal operator filters and their relative topology

This chapter supplies the exact operator-space foundation for the spectral sum and filtration theorems that follow. It retains the projective-tensor and preadjoint arguments from the preserved operator-module lesson, and binds them to the current complete Fourier and integration proofs. Normal operators are used as a norm-closed space with a specified relative topology; no full-dual or ambient weak-star-closed assertion is made.

*Written in Codex (OpenAI), 2026. No human review is claimed. Newly written original expression is dedicated under CC0.*

The earlier inputs are BS0–4 for specified-dual vector actions, BS6 for the preadjoint integration mechanism, LF0–7 for Fourier products, local cutoffs and closed ideals, [L24 §§2–5](OA-FLOW-L24.md#oa-flow.grp.vectorintegration) for Haar representatives, translations and full-domain integrals, [HR5](OA-FLOW-HR.md#hr-05) for qualified Radon-product interchange, [H1](OA-FLOW-HARMONIC.md#l138-h1) for Fourier uniqueness, and [H2–4](OA-FLOW-HARMONIC-LATE.md#l138-h2) for the scalar Fourier unitary and paired dual Haar measure. Finite compact partitions are proved in [H0](OA-FLOW-TOPOLOGY.md#l138-h0). Norm separation uses CF1; the norm completion needed here is constructed in MX0.

Throughout this packet, write

<a id="equation-mx1"></a>

\[
 \mathcal Fa(p)=\int_G a(t)(t,p)\,dt,\qquad
 \alpha_f x=\int_G a(t)\alpha_t x\,dt\quad(f=\mathcal Fa).
 \tag{MX1}
\]
This is the positive-character convention. It is obtained from the negative-character LF/BS convention by replacing the frequency by its inverse. Reflection is an isometric algebra isomorphism, so it preserves every support, ideal and cutoff assertion with its frequency sets reflected. This is also the independently checked convention in AF0; no AF1–4 result is needed here. Haar integration uses L24's finite-exponent Borel representatives on sigma compact carriers and HR5's Radon product, never an unrestricted product-Borel identification.

<a id="mx-0"></a>

## MX0. Preadjoints and the operator sigma topology

Let \(X=X_*^*\) and \(Y=Y_*^*\) be complex Banach duals with their specified preduals. Denote by \(\mathcal L_w(X,Y)\) the bounded linear maps \(T:X\to Y\) that are continuous from the specified weak-star topology of \(X\) to that of \(Y\). A bounded map lies in this space exactly when

<a id="equation-o1"></a>

$$T^*(Y_*)\subset X_*. \tag{O1}$$

Indeed, for \(\psi\in Y_*\), the functional \(x\mapsto\langle Tx,\psi\rangle\) is weak-star continuous precisely when it belongs to \(X_*\). Condition (O1) therefore defines the preadjoint \(T_*:Y_*\to X_*\) by

<a id="equation-o2"></a>

$$\langle Tx,\psi\rangle=\langle x,T_*\psi\rangle,\qquad
\|T_*\|=\|T\|. \tag{O2}$$

Conversely every bounded \(S:Y_*\to X_*\) has adjoint \(S^*:X\to Y\) in \(\mathcal L_w(X,Y)\). Hence \(T\mapsto T_*\) is an isometric linear correspondence with \(\mathcal L(Y_*,X_*)\). It also proves that \(\mathcal L_w(X,Y)\) is closed in the operator norm.

Put \(Q=X\widehat\otimes_\pi Y_*\), the projective tensor product. We use its standard duality with bounded bilinear forms: a bounded \(T:X\to Y=Y_*^*\) corresponds isometrically to the functional

<a id="equation-o3"></a>

$$\langle T,x\otimes\psi\rangle_Q=\langle Tx,\psi\rangle,
\qquad Q^*\cong\mathcal L(X,Y). \tag{O3}$$

The source's ambient relative topology is \(\sigma_0=\sigma(Q^*,Q)|_{\mathcal L_w}\). It agrees with pointwise weak-star convergence **on norm-bounded sets**: finite tensors give the point evaluations, and their projective-norm density extends convergence to every tensor when the operators have a uniform norm bound. No such extension is automatic for an arbitrary unbounded net.

For an auxiliary completion put \(V=\mathcal L_w(X,Y)\), and define

<a id="equation-o3a"></a>

$$\begin{aligned}
\ell_{x,\psi}(T)&=\langle Tx,\psi\rangle,\\
\mathcal E&=\overline{\operatorname{span}\{\ell_{x,\psi}:x\in X,\ \psi\in Y_*\}}^{\|\cdot\|_{V^*}},\\
\sigma&=\sigma(V,\mathcal E).
\end{aligned} \tag{O3a}$$

The pairing is norming: the specified dual norms imply \(\|T\|=\sup_{\|x\|\le1,\|\psi\|\le1}|\ell_{x,\psi}(T)|\). Consequently \(V\) embeds isometrically in \(\mathcal E^*\), though no surjectivity or weak-star closedness of that image is asserted. The topology \(\sigma\) agrees with \(\sigma_0\) and with pointwise weak-star convergence on norm-bounded sets, by norm approximation of their test functionals. Every tensor in \(Q\) restricts to a member of \(\mathcal E\), so \(\sigma\) is at least as strong as \(\sigma_0\). We prove filter continuity for both topologies. The operator spectral closures below and in the following lessons use the source topology \(\sigma_0\).

For clarity, the tensor duality used in (O3) needs only the following construction. On the algebraic tensor product put \(\|q\|_\pi=\inf\sum_j\|x_j\|\|\psi_j\|\), the infimum over finite representations of \(q\). Bounded bilinear forms have bound at most this norm. They separate algebraic tensors: express a nonzero tensor using linearly independent finite families, choose coordinate functionals on their finite-dimensional spans, and extend them by Hahn–Banach. Thus this is a norm. Complete it to obtain \(Q\). Every bounded bilinear form extends uniquely to the completion with the same norm. Conversely a functional on \(Q\) gives such a form by evaluating elementary tensors. Because \(Y=Y_*^*\), each form is exactly \(\langle Tx,\psi\rangle\) for a bounded operator \(T:X\to Y\); taking the two unit-ball suprema gives its norm. This proves (O3), not a corresponding full-dual claim for its normal subspace.

The elementary norm facts in that construction can be made explicit. A norm on a finite-dimensional span is bounded above by a constant times the Euclidean coordinate norm. On the Euclidean unit sphere it is continuous and positive, so CF1 compactness gives a positive minimum. Thus the coordinate functionals on the span are bounded, as required before Hahn–Banach is used. The completion of a normed space consists of its Cauchy sequences modulo differences tending to zero; addition and scalar multiplication are termwise and the norm is the limit of the original norms. These definitions are independent of representatives by the triangle inequality. Constant sequences embed the original space isometrically and densely, since a Cauchy sequence is arbitrarily close to each sufficiently late constant term. To verify completeness, take a Cauchy sequence of classes, retain a subsequence with consecutive distances at most \(2^{-j}\), and approximate its \(j\)-th term by an original-space vector to within \(2^{-j}\). The approximating vectors are Cauchy by the summable consecutive-distance bound. Their class is the limit of that subsequence, and then of the whole Cauchy sequence by its Cauchy property. Bounded functionals extend by taking limits along representatives, with unchanged norm. This justifies every completion assertion used for \(Q\).

<a id="mx-1"></a>

## MX1. Conjugation by two dual Banach actions

Let \(G\) be an arbitrary locally compact Hausdorff abelian group, \(H=\widehat G\), and let \(\alpha:G\to\operatorname{GL}(X)\), \(\beta:G\to\operatorname{GL}(Y)\) satisfy the specified-dual hypotheses of BS0–1: their operators are weak-star continuous, their predual orbits are norm continuous, and

<a id="equation-o4"></a>

$$C_\alpha=\sup_t\|\alpha_t\|<\infty,\qquad
C_\beta=\sup_t\|\beta_t\|<\infty. \tag{O4}$$

Write \(\alpha_{t,*}:X_*\to X_*\) and \(\beta_{t,*}:Y_*\to Y_*\) for the preadjoints, so \(\langle\alpha_t x,\phi\rangle=\langle x,\alpha_{t,*}\phi\rangle\). Define

<a id="equation-o5"></a>

$$\gamma_t(T)=\beta_tT\alpha_{-t},\qquad T\in\mathcal L_w(X,Y). \tag{O5}$$

Composition of normal maps makes \(\gamma_t(T)\) normal. Since \(G\) is abelian, \(\gamma_s\gamma_t=\gamma_{s+t}\), and \(\sup_t\|\gamma_t\|\le C_\alpha C_\beta\). For fixed \(t\), the tensor map \(x\otimes\psi\mapsto\alpha_{-t}x\otimes\beta_{t,*}\psi\) extends boundedly on \(Q\) by the projective norm and proves \(\sigma_0\)-continuity of \(\gamma_t\). The map is also \(\sigma\)-continuous: its pullback on the finite evaluation span sends

<a id="equation-o6"></a>

$$\ell_{x,\psi}\longmapsto\ell_{\alpha_{-t}x,\beta_{t,*}\psi}, \tag{O6}$$

and extends boundedly to \(\mathcal E\), since \(\gamma_t\) is bounded on \(V\). Every orbit \(t\mapsto\gamma_t(T)\) is \(\sigma\)-continuous as well. For fixed \(x,\psi\),

<a id="equation-o7"></a>

$$\langle\gamma_t(T)x,\psi\rangle
=\langle\alpha_{-t}x,T_*\beta_{t,*}\psi\rangle. \tag{O7}$$

The second argument is norm continuous by the predual hypothesis and boundedness of \(T_*\); the first is weak-star continuous and uniformly bounded. Splitting the difference of two pairings proves scalar continuity at every \(t\). Norm density of the evaluation span in \(\mathcal E\) and the uniform bound on \(\gamma_t(T)\) extend continuity to all tests in \(\mathcal E\). The orbit need not be norm continuous in \(V\), and its \(\sigma\)-continuity alone does not make it a Bochner-integrable operator-valued function.

<a id="mx-2"></a>

## MX2. Full-domain integration and arbitrary-net filter continuity

Use the positive Fourier sign (MX1): for \(a\in L^1(G)\), write \(f=\mathcal Fa\in A(H)\). We construct the operator filter

<a id="equation-o10"></a>

$$\Gamma_f(T)=\int_G a(t)\gamma_t(T)\,dt \tag{O10}$$

as a scalar integral against every test in \(\mathcal E\) and prove that it belongs to \(\mathcal L_w(X,Y)\). The notation agrees with the source's inverse-Fourier convention after replacing its kernel \(\widetilde f(-t)\) by \(a(t)\); the sign conversion is the reflection fixed in (MX1).

Normality follows first from the actual preadjoint:

<a id="equation-o14"></a>

$$\bigl(\Gamma_f(T)\bigr)_*\psi
=\int_G a(t)\alpha_{-t,*}T_*\beta_{t,*}\psi\,dt\in X_*. \tag{O14}$$

For \(a\in C_c(G)\), this is a Bochner integral of a norm-continuous predual orbit. Its norm is at most \(C_\alpha C_\beta\|a\|_1\|T\|\|\psi\|\). Approximation in \(L^1(G)\) gives the same integral and bound for every \(a\in L^1(G)\). Taking its adjoint defines \(\Gamma_f(T)\in V\), and pairing with \(x\) gives (O10). In particular,

<a id="equation-o13"></a>

$$\|\Gamma_f(T)\|\le C_\alpha C_\beta\|f\|_A\|T\|. \tag{O13}$$

We next prove continuity for the full source topology \(\sigma_0\).
Take \(a\in C_c(G)\) and a compact set \(K\) containing its support.
For fixed \(x\in X\) and \(\psi\in Y_*\), choose a finite nonnegative
continuous partition \(\mathcal P=(h_i,t_i)\) on \(K\), with
\(\sum_i h_i=1\), such that
\(\|\beta_{t,*}\psi-\beta_{t_i,*}\psi\|<\varepsilon_{\mathcal P}\)
whenever \(h_i(t)>0\). Norm continuity on the compact set gives
partitions with errors tending to zero. Form genuine tensors

<a id="equation-o11a"></a>

$$\begin{aligned}
x_i&=\int_G a(t)h_i(t)\alpha_{-t}x\,dt\in X,\\
q_{\mathcal P}(x,\psi)&=\sum_i x_i\otimes\beta_{t_i,*}\psi\in Q.
\end{aligned} \tag{O11a}$$

Extend each scalar kernel by zero outside \(K\). Its weak-star integral
exists by BS1. Directly from the projective norm,
\(\|q_{\mathcal P}(x,\psi)\|_\pi
\le C_\alpha C_\beta\|a\|_1\|x\|\|\psi\|\).

The essential step is convergence in the **projective norm itself**.
For a second partition \(\mathcal R=(k_j,s_j)\), put
\(x_{ij}=\int a(t)h_i(t)k_j(t)\alpha_{-t}x\,dt\).
Linearity of this integral and the two partition identities give

<a id="equation-o11b"></a>

$$\begin{aligned}
q_{\mathcal P}-q_{\mathcal R}
 &=\sum_{i,j}x_{ij}\otimes
       (\beta_{t_i,*}\psi-\beta_{s_j,*}\psi),\\
\|q_{\mathcal P}-q_{\mathcal R}\|_\pi
 &\le C_\alpha\|x\|\|a\|_1
       (\varepsilon_{\mathcal P}+\varepsilon_{\mathcal R}).
\end{aligned} \tag{O11b}$$

Indeed, where \(h_i k_j>0\), each sampled vector is within its own
partition error of \(\beta_{t,*}\psi\); and
\(\sum_{i,j}h_i k_j=1\). This estimate does not test an arbitrary
bounded operator against a weak-star integral. It proves an intrinsic
Cauchy limit \(q_a(x,\psi)\in Q\), independent of the partitions.

Using common partitions for any finite collection of vectors \(\psi\)
proves linearity in \(\psi\); linearity in \(x\) follows from the
integral. The bound above therefore gives a bounded linear map

<a id="equation-o11c"></a>

$$
R_a:Q\longrightarrow Q,\qquad
R_a(x\otimes\psi)=q_a(x,\psi),\qquad
\|R_a\|\le C_\alpha C_\beta\|a\|_1.
\tag{O11c}
$$

For **normal** \(T\), passing \(T\) through the finitely many weak-star
integrals in (O11a) is valid. Uniform approximation of the sampled
predual vectors then identifies the limit:

<a id="equation-o11d"></a>

$$
\langle\Gamma_f(T),q\rangle_Q=\langle T,R_aq\rangle_Q
\qquad(T\in V,\ q\in Q).
\tag{O11d}
$$

First this holds on elementary tensors, then on all \(Q\) by the norm
bounds. Common partitions also prove linearity in \(a\); approximation
by \(C_c(G)\) in \(L^1(G)\) extends \(R_a\) in operator norm and (O11d)
to every \(a\in L^1(G)\). Since \(R_aq\) is an actual member of \(Q\),
(O11d) proves filter continuity for every \(\sigma_0\)-convergent net,
with no boundedness assumption on that net. No corresponding integral
identity for nonnormal \(T\) is required or asserted.

We also retain continuity for the completed evaluation topology.
First take \(a\in C_c(G)\). For \(x\in X\), \(\psi\in Y_*\), and a compact subset containing \(\operatorname{supp}(a)\), the map \(t\mapsto\beta_{t,*}\psi\) is norm continuous. Choose finite continuous partitions of unity on that compact set to approximate it uniformly by \(\sum_i h_i(t)\psi_i\). For each \(i\), the weak-star integral

<a id="equation-o11"></a>

$$x_i=\int_G a(t)h_i(t)\alpha_{-t}x\,dt\in X \tag{O11}$$

exists by the predual integration construction of BS1. The finite sum \(\sum_i\ell_{x_i,\psi_i}\) belongs to \(\mathcal E\). Normality of \(T\) permits passing \(T\) through each integral in (O11). If the uniform approximation error to \(\beta_{t,*}\psi\) is \(\varepsilon\), the resulting error, tested against every **normal** \(T\in V\) with \(\|T\|\le1\), is at most \(C_\alpha\|x\|\|a\|_1\varepsilon\). Thus these sums converge in the \(V^*\) norm to a member \(S_a\ell_{x,\psi}\in\mathcal E\), with

<a id="equation-o12"></a>

$$\begin{aligned}
(S_a\ell_{x,\psi})(T)
&=\int_G a(t)\langle T\alpha_{-t}x,\beta_{t,*}\psi\rangle\,dt,\\
\|S_a\ell_{x,\psi}\|_{\mathcal E}
&\le C_\alpha C_\beta\|a\|_1\|x\|\|\psi\|.
\end{aligned} \tag{O12}$$

For a finite evaluation sum \(q\), (O12) says \((S_aq)(T)=q(\Gamma_f(T))\). The already proved bound (O13) therefore gives

<a id="equation-o12a"></a>

$$\|S_aq\|_{\mathcal E}
\le C_\alpha C_\beta\|a\|_1\|q\|_{\mathcal E}. \tag{O12a}$$

It also shows that the construction respects all linear relations between evaluations. Completion extends \(S_a\) to \(\mathcal E\); the same bound extends it from compactly supported kernels to all \(L^1(G)\). The identity \(q(\Gamma_f(T))=(S_aq)(T)\), now for every \(q\in\mathcal E\), proves \(\sigma\)-continuity of the filter.

This completed-evaluation proof and the projective-norm proof establish
both continuity statements. Normality is used only to identify the
operator integral with the pullback of tests. The norm construction
(O11b) supplies the tensor limit independently and closes the full
source-topology assertion.

The group law and Fubini for compactly supported kernels give \(\Gamma_f\Gamma_g=\Gamma_{fg}\), then the \(L^1\) bounds extend it to all \(f,g\in A(H)\). The neighborhood approximate identities of BS1 satisfy

<a id="equation-o15"></a>

$$\Gamma_{e_V}T\longrightarrow T\quad\text{in }\sigma\text{ and }\sigma_0. \tag{O15}$$

To see this, pair against \(\ell_{x,\psi}\); the orbit scalar (O7) is continuous at zero, and the nonnegative kernel \(a_V\) has mass one and support in the identity neighborhood. The uniform bound \(\|\Gamma_{e_V}T\|\le C_\alpha C_\beta\|T\|\) extends convergence from finite evaluation sums to every test in \(\mathcal E\). No norm convergence of the operator orbit is asserted.

For an arbitrary \(L^1\) kernel, the last definition is independent of its representative and agrees with the full preadjoint Bochner integral: L24 places the scalar kernel on a sigma compact carrier; each compact part of the norm-continuous orbit has separable image, and the integral bound is \(C_\alpha C_\beta|a(t)|\|T\|\|\psi\|\). The full Banach-valued integration proof of BS1 applies. Its adjoint has exactly the tested value (O10). Thus neither operator-valued Bochner measurability nor a barycenter theorem on arbitrary compact sets of normal operators is a premise.

For (O11a), a finite continuous partition on the compact set can be chosen subordinate to the norm-continuity cover by H0. Restrict these Borel functions to that compact set and extend by zero when forming the kernels. The products with \(a\) are genuine \(L^1\) functions. Common refinements give (O11b) even if the partition functions do not extend continuously across the boundary of that compact set.

<a id="mx-3"></a>

## MX3. Closed and open operator spectral spaces

For \(T\in V=\mathcal L_w(X,Y)\), define

<a id="equation-mx2"></a>

\[
 I_\gamma(T)=\{f\in A(H):\Gamma_f(T)=0\},\qquad
 \operatorname{Sp}_\gamma(T)=h(I_\gamma(T)).
 \tag{MX2}
\]
The module law and (O13) make the annihilator a norm-closed ideal. Apply LF6 to this ideal. A compactly supported Fourier function whose support misses its hull belongs to the ideal; so does every Fourier function vanishing on a neighbourhood of that hull. If the hull is empty, the ideal is all of \(A(H)\), and (O15) gives \(T=0\). Moreover

<a id="equation-mx3"></a>

\[
 \operatorname{Sp}_\gamma(\Gamma_f T)
 \subset\operatorname{Sp}_\gamma(T)\cap\operatorname{supp}f.
 \tag{MX3}
\]
For the first inclusion use \(I_\gamma(T)\subset I_\gamma(\Gamma_fT)\). For the second, a point outside \(\operatorname{supp}f\) has a compact local plateau \(g\) disjoint from that support; then \(gf=0\) and \(g\in I_\gamma(\Gamma_fT)\), excluding the point.

For closed \(E\subset H\), define \(V_\gamma(E)=\{T:\operatorname{Sp}_\gamma(T)\subset E\}\). Then

<a id="equation-mx4"></a>

\[
 V_\gamma(E)=\bigcap_{\substack{g\in A_c(H)\\\operatorname{supp}g\cap E=\varnothing}}\ker\Gamma_g.
 \tag{MX4}
\]
One inclusion is LF6 applied to \(I_\gamma(T)\). For the other, at each point outside \(E\) choose a compact plateau supported in its complement; its nonzero value excludes that point from the hull. Each kernel is \(\sigma_0\)-closed by (O11d), including for unbounded convergent nets. Thus \(V_\gamma(E)\) is a closed linear subspace in the relative topology.

For open \(U\), let \(V_{\gamma,0}(U)\) be the \(\sigma_0\)-closed linear span of \(\Gamma_fT\) with \(\operatorname{supp}f\subset U\). If \(U\subset E\subset W\), with \(E\) closed and \(U,W\) open, then

<a id="equation-mx5"></a>

\[
 V_{\gamma,0}(U)\subset V_\gamma(E)\subset V_{\gamma,0}(W).
 \tag{MX5}
\]
The first inclusion follows from (MX3) and closedness. For the second let \(T\in V_\gamma(E)\), \(g\in A_c(H)\), and \(K=\operatorname{supp}g\). LF4 supplies \(c\in A_c(H)\), supported in \(W\), equal to one near the compact \(K\cap E\); take \(c=0\) if that intersection is empty. The compact support of \(g-cg\) misses \(E\), so (MX4) gives \(\Gamma_gT=\Gamma_{cg}T\in V_{\gamma,0}(W)\). LF5 norm density and (O13) extend this membership to every \(g\in A(H)\). Applying (O15) and closedness gives \(T\in V_{\gamma,0}(W)\).

In particular the usual closed-neighbourhood formula holds:

<a id="equation-mx6"></a>

\[
 V_\gamma(E)=\bigcap_{W\supset E,\ W\mathrm{\ open}}V_{\gamma,0}(W).
 \tag{MX6}
\]
Indeed \(V_{\gamma,0}(W)\subset V_\gamma(\overline W)\) by (MX3). For \(p\notin E\), choose an open neighbourhood \(O\) of \(p\) with \(\overline O\cap E=\varnothing\) and take \(W=H\setminus\overline O\); the neighbourhood \(O\) keeps \(p\) out of \(\overline W\). Hence the intersection of these closed sets is \(E\). The same arguments hold for \(\sigma\)-closures because the filters are also \(\sigma\)-continuous. None of these statements identifies the ideal of a general closed set with the closure of functions vanishing near it: arbitrary closed-set spectral synthesis is not used.

<a id="mx-4"></a>

## MX4. The precise compact-frequency inverse domain

If \(a\in L^1(G)\) and \(f=\mathcal Fa\in C_c(H)\), then \(a\in L^2(G)\), and its \(L^2\) Fourier transform is \(f\). Here is the compatibility proof needed when an initially known \(L^1\) kernel is put into the Plancherel domain.

Choose nonnegative \(b_V\in C_c(G)\) with integral one and support tending to zero, as in L24. The function \(a*b_V\) is in \(L^1\cap L^2\). For the second membership, integrate the norm-continuous \(L^2\)-valued function \(t\mapsto L_tb_V\) against \(a(t)\); the Bochner bound is \(\|a\|_1\|b_V\|_2\). Its equality with scalar convolution follows first against compact continuous test functions by HR5, then by local Radon uniqueness. The Fourier identity on \(L^1\) and the already established \(L^1\cap L^2\) compatibility give

<a id="equation-mx7"></a>

\[
 \mathcal F(a*b_V)=f\,\mathcal Fb_V.
 \tag{MX7}
\]
On \(K=\operatorname{supp}f\), \(\mathcal Fb_V\to1\) uniformly. Indeed joint character evaluation and compactness of \(K\), proved in H3, give

<a id="equation-mx8"></a>

\[
 \sup_{p\in K}|\mathcal Fb_V(p)-1|
 \le\sup_{t\in\operatorname{supp}b_V,\ p\in K}|(t,p)-1|\longrightarrow0.
 \tag{MX8}
\]
Thus \(f\mathcal Fb_V\to f\) in \(L^2(H)\); the inverse unitary gives \(a*b_V\to v=\mathcal F^{-1}f\) in \(L^2(G)\). Also \(a*b_V\to a\) in \(L^1(G)\) by L24. For every \(d\in C_c(G)\), the two limits give \(\int a\overline d=\int v\overline d\), using respectively \(\|d\|_\infty\) and \(\|d\|_2\). Local Radon uniqueness identifies them on each sigma compact open coset. Both have sigma compact carriers as finite-exponent classes; only countably many such cosets can meet their nonzero classes. Hence they are the same global Haar class, and \(a\in L^2\). H2's inverse integral supplies a continuous representative when required, with the sign in (MX1).

For \(f=\mathcal Fa,g=\mathcal Fb\in A_c(H)\), the full \(L^2\) product formula LF0, reflected to the positive convention, now gives

<a id="equation-mx9"></a>

\
 \mathcal F\bigl[b(t)a(-t)\bigr
 =\int_H g(r)f(r-q)\,dr.
 \tag{MX9}
\]
The kernel on the left is \(L^1\) by Cauchy–Schwarz. The integral on the right exists at every \(q\) and is continuous; LF0 proves the identity pointwise, not merely as an almost-everywhere statement. This is the exact domain and sign used in the filtration converse.

The mathematical context is [Takesaki, Theory of Operator Algebras II](https://doi.org/10.1007/978-3-662-10451-4), XI §1. The proof here retains the programme's projective-norm construction of the filter pullback and its independent preadjoint construction. It does not import the book's compact-convex-hull theorem.
