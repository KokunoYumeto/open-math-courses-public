# Whole-cone averaging and comparison of general dual weights

*New expression: CC0-1.0 to the extent of rights held; inherited expressions retain their recorded terms.*

Let \(G\) be an arbitrary locally compact Hausdorff group with left Haar measure \(dt\) and \(\mu(Es)=\delta(s)\mu(E)\). Let \(\alpha\) be a point-ultraweak continuous normal automorphism action on an arbitrary von Neumann algebra \(M\). Scalar products are linear in the first entry. There is no countability, separability, unimodularity, invariant-weight or finite-state hypothesis. The zero algebra has the unique zero map; assume \(M\ne0\) below.

Use the actual [AT](OA-FLOW-AT.md#oa-flow.at.1), [NR](OA-FLOW-NR.md#oa-flow.nr.1), [CCM](OA-FLOW-CAI.md#ccm-4), [Haar](OA-FLOW-HR.md#hr-03), [L24](OA-FLOW-L24.md#oa-flow.grp.haarconventions), [extended-positive EP](OA-FLOW-EP.md#ep-2), [normal-weight EW](OA-FLOW-EW.md#ew-5), [full completion WH04](OA-FLOW-WH04.md#oa-flow.wh04.2), [WF](OA-FLOW-WF.md#oa-flow.wf.1), [BC](OA-FLOW-BC.md#bc-2), [OT](OA-FLOW-OT.md#ot-1), [MA](OA-FLOW-MA.md#oa-flow.ma.4), [CZ](OA-FLOW-CZ.md#cz-6), [RF5](OA-FLOW-RF.md#rf-5) and [GDW1–7](OA-FLOW-GDW.md#gdw-1) proofs. The elementary GNS, positive calculus, weak compactness and scalar convergence inputs are the earlier CF/GNS/CP/CV/SF/SC bodies. Every application below specifies its domain. The primary mathematical route is Haagerup, [*On the dual weights for crossed products of von Neumann algebras II*](https://journals.msp.org/mscand/article/view/1878), Math. Scand. 43 (1978), especially Theorem 3.1. We supply the directedness, scalar finite-domain, positive-kernel and whole-cone passages used by that route. A dense GNS quadratic test determines the weight once its modular group is fixed; the proof uses the closed positive density operator and the earlier MA/CZ/RF results.

<a id="gda-0"></a>

## GDA0. The complete conclusions

The exact scalar and operator preliminaries used below are [CF8–10](OA-FLOW-CF.md#oa-flow.cf.8) (Hilbert–Riesz, positive calculus and weak compactness), [GNS](OA-FLOW-GNS.md#gns-theorem-4-1), [CP4–6](OA-FLOW-CP.md#oa-flow.cp.4) (normal vector-series tests and positive extensions), [SC3–5](OA-FLOW-SC.md#sc-03) (scalar approximation and convergence), [HR5](OA-FLOW-HR.md#hr-05) and [L24 Proposition4.3](OA-FLOW-L24.md#oa-flow.grp.vectorintegration) (product interchange), [SF, SB0–6](OA-FLOW-SF.md#oa-flow.sf.sb0) (full Borel domains), [NF5](OA-FLOW-NF.md#oa-flow.nf.5), [GW3–4](OA-FLOW-GW.md#oa-flow.gw.3), [EW2](OA-FLOW-EW.md#oa-flow.ew.2), [HA-R4](OA-FLOW-HA-R.md#oa-flow.ha-r.4), [NC4](OA-FLOW-NC.md#oa-flow.nc.4) and the general normal-weight [sum theorem WS](OA-FLOW-WS.md#oa-flow.weight-sum.ws5). These are earlier programme proof bodies; the dependency ledger binds each actual range and its inherited closure.

Write \(R=M\rtimes_\alpha G=\{\pi(M),\lambda(G)\}''\), in the normal regular model. We construct a faithful normal semifinite operator-valued weight

<a id="equation-gda1"></a>

\[
T:R_+\longrightarrow\widehat{\pi(M)}_+,
\qquad
T(L_x^*L_x)=\pi\left(\int_G x(t)^*x(t)\,dt\right)
\quad(x\in\mathscr K).
\tag{GDA1}
\]
Here \(\mathscr K\) is GDW's bounded, strongly* continuous compact coefficient algebra, \(L_x=\int\lambda_t\pi(x(t))dt\). The integral in (GDA1) is bounded, with no pointwise input-weight finiteness assumption. On every positive \(X\), including infinite values,

<a id="equation-gda2"></a>

\[
T(\lambda_sX\lambda_s^*)
=\delta(s)\lambda_sT(X)\lambda_s^*.
\tag{GDA2}
\]
For every faithful normal semifinite \(\varphi\), its already constructed GDW dual weight is exactly

<a id="equation-gda3"></a>

\[
\widehat\varphi=\widehat{\varphi\circ\pi^{-1}}\circ T,
\qquad
(D\widehat\psi:D\widehat\varphi)_r=\pi((D\psi:D\varphi)_r).
\tag{GDA3}
\]
The outer hat on a scalar weight in the composition means EP's extension to the entire extended positive cone. The first equality subsequently defines the extension to every normal input weight, allowing zero, nonfaithful and nonsemifinite cases. For faithful n.s.f. inputs we also give the whole relative positive-operator domains. GDA0 is a forward theorem statement; its proofs are GDA1–9 and it is not an earlier proved premise.

<a id="gda-1"></a>

## GDA1. The scalar group weight and every L1 coefficient

Apply GDW with \(M=\mathbb C\), trivial action and the weight \(z\mapsto z\) on \(\mathbb R_+\). It gives a faithful normal semifinite weight \(\Omega\) on \(L(G)=\lambda(G)''\), with \(L^2(G)\) as its whole GNS space. Its original algebra is \(C_c(G)\), with ordinary convolution and

<a id="equation-gda4"></a>

\[
f^\#(t)=\delta(t)^{-1}\overline{f(t^{-1})},\qquad
\Lambda_\Omega(\lambda(f))=f\quad(f\in C_c(G)).
\tag{GDA4}
\]
Its complete finite ideal is GDW6's full left-multiplier ideal. In particular, \(\Omega(X)<\infty\) precisely when \(X^{1/2}=\lambda_\xi\) for its actual full left-bounded vector \(\xi\); the value is \(\|\xi\|_2^2\). WH04's mixed identity holds for **every** right-bounded vector, even outside its adjoint involution domain.

For \(f\in L^1(G)\), we claim the complete formula

<a id="equation-gda5"></a>

\[
\Omega(\lambda(f)^*\lambda(f))=\int_G|f(t)|^2dt,
\tag{GDA5}
\]
where the right side may be infinite. If \(f\in L^1\cap L^2\), HR/L24 give compact continuous approximants converging in both norms. Their integrated operators converge in operator norm, and their GNS vectors converge in \(L^2\). EW2's bounded adjoint-strong GNS graph gives \(\lambda(f)\in N_\Omega\) with vector \(f\).

Conversely, finite left side means \(\lambda(f)=\lambda_\xi\) for \(\xi\in L^2\). Every \(h\in C_c(G)\) is right bounded: right convolution is the integral of right-translation unitaries, with norm at most \(\int|h(t)|\delta(t)^{-1/2}dt\). WH04.3 gives
\(f*h=\lambda(f)h=R_h\xi=\xi*h\).
Take nonnegative normalized compact bumps \(h_i\) whose supports shrink to the identity. Left convolution by \(h_i\) tends strongly to the identity; right convolution has a common bound and tends strongly to the identity too, by the continuous right-translation representation and \(\delta(t)\to1\) at the identity. Thus \(f*h_i\to f\) in \(L^1\) and \(\xi*h_i\to\xi\) in \(L^2\). On each compact finite-measure set the latter is also \(L^1\) convergence. Hence \(f=\xi\) locally almost everywhere. A countable union of compact carriers covers the finite-exponent supports of these two fields, so the equality is their global Haar class. This proves (GDA5), including its infinite case, without replacing the full multiplier test by a compact-domain test.

Conjugation by \(\lambda_s\) scales this entire scalar weight:

<a id="equation-gda6"></a>

\[
\Omega(\lambda_sX\lambda_s^*)=\delta(s)\Omega(X)\quad(X\in L(G)_+).
\tag{GDA6}
\]
For clarity, this is a whole-domain assertion. Define \((B_s f)(t)=\delta(s)f(s^{-1}ts)\) on \(L^2(G)\). Haar change of variables gives \(\|B_s f\|_2^2=\delta(s)\|f\|_2^2\). On \(C_c(G)\), \(B_s\) is a convolution and involution automorphism, and \(\lambda(B_sf)=\lambda_s\lambda(f)\lambda_s^*\). The bounded invertible map \(B_s\) transports the entire closed involution, each bounded-vector test and its first/second dual: substitute \(B_s^{-1}a\) in the defining inequalities, and use its fixed Hilbert norm scale. It therefore transports the full multiplier ideal and satisfies \(\lambda_{B_s\xi}=\lambda_s\lambda_\xi\lambda_s^*\). Equivalently its normalized unitary is the product of left and right regular unitaries, so this equality also follows on their dense original algebra. The complete square-root criterion for \(\Omega\) now proves (GDA6), both at finite values and when the finite-ideal condition fails.

<a id="gda-2"></a>

## GDA2. Directed strict normal minorants, proved locally

For any faithful n.s.f. weight \(\nu\) on any von Neumann algebra \(A\), put

<a id="equation-gda7"></a>

\[
\mathcal F_\nu^\circ=
\{f\in A_*^+:f\leq(1-\varepsilon)\nu\text{ for some }0<\varepsilon<1\}.
\tag{GDA7}
\]
This set is directed in the positive-functional order. Let \(f_1,f_2\) belong to it. The maps \(T_j\Lambda_\nu(a)=\Lambda_{f_j}(a)\), \(a\in N_\nu\), extend to bounded intertwiners; \(R_j=T_j^*T_j\) belongs to \(\pi_\nu(A)'\) and \(0\leq R_j\leq(1-\varepsilon_j)1\). The bounded-functional GNS representation is normal by NF5. GW4's finite positive contractions tend strongly to one there, so \(\Lambda_{f_j}(N_\nu)\) is dense in its whole unital GNS space.

In the commutant define

<a id="equation-gda8"></a>

\[
H_j=R_j(1-R_j)^{-1},\qquad H=H_1+H_2,\qquad R=H(1+H)^{-1}.
\tag{GDA8}
\]
The inverse-order inequality for positive invertible operators gives \(R\geq R_j\). Also \(R\leq(1-\varepsilon')1\) for some \(\varepsilon'>0\), since \(H\) is bounded, and \(R\leq H\leq C(R_1+R_2)\) for finite \(C\). No commutation between \(R_1,R_2\) is assumed.

Let \(\rho=f_1+f_2\), a bounded normal positive functional. The form
\(\langle R\Lambda_\nu(a),\Lambda_\nu(b)\rangle\)
is well defined and bounded on \(\Lambda_\rho(N_\nu)\), by the last inequality and Cauchy–Schwarz. This space is dense, as above. Hilbert–Riesz gives a bounded positive operator \(Q\) on \(H_\rho\). Its form identity with multiplication by \(c,c^*\in A\) makes \(Q\) commute with \(\pi_\rho(A)\). Thus

<a id="equation-gda9"></a>

\[
f(a)=\langle Q\pi_\rho(a)\Lambda_\rho(1),\Lambda_\rho(1)\rangle
\tag{GDA9}
\]
is a bounded normal positive functional and, on every \(a\in N_\nu\),
\(f(a^*a)=\langle R\Lambda_\nu(a),\Lambda_\nu(a)\rangle\).
It follows that \(f\leq(1-\varepsilon')\nu\) on the entire cone: test a finite positive element by its square root; an infinite \(\nu\)-value imposes no further upper restriction. To see \(f\geq f_j\) on every positive \(x\), test first on \(u_i x u_i\), where \(u_i\) are the finite positive contractions. Their square roots belong to \(N_\nu\), since \(x^{1/2}u_i\in N_\nu\) and the finite cone is hereditary. The form inequality applies there, and normality of the bounded functionals passes to the bounded strong limit \(x\). Hence \(f\) is a common upper member of (GDA7).

EW5 and scaling also prove

<a id="equation-gda10"></a>

\[
\nu(x)=\sup_{f\in\mathcal F_\nu^\circ}f(x)\quad(x\in A_+).
\tag{GDA10}
\]
Indeed every normal minorant is approached pointwise by its factors \((1-\varepsilon)f\). Directedness is used below for \(\nu=\Omega\); no directedness assertion for nonsemifinite input weights is needed.

<a id="gda-3"></a>

## GDA3. Positive-definite functions and the exact scalar tests

A continuous function \(p:G\to\mathbb C\) is positive definite when all matrices \([p(s_i s_j^{-1})]\) are positive. Here is the needed representation without a cited group theorem. Complete the finite formal vectors \(v_s\) with scalar product \(\langle v_s,v_t\rangle=p(ts^{-1})\), quotienting the null space. The maps \(\rho_gv_s=v_{sg^{-1}}\) preserve this scalar product and form a unitary representation. Continuity of \(p\) makes it strongly continuous first on finite vectors, then everywhere by the common unitary bound. With \(v=v_e\),

<a id="equation-gda11"></a>

\[
p(g)=\langle\rho_gv,v\rangle,\qquad\|v\|^2=p(e),\qquad
v_t=\rho_{t^{-1}}v.
\tag{GDA11}
\]
The finite formal vectors span densely, so \(v\) is cyclic; compact bumps approximate their group translates by continuous vector integrals.

Write \(p\preccurlyeq\delta_e\) for the test inequalities

<a id="equation-gda12"></a>

\[
\int_G p(t)(h^\#*h)(t)dt\leq\|h\|_2^2\quad(h\in C_c(G)).
\tag{GDA12}
\]
This notation concerns the identity distribution, not the modular function \(\delta(t)\). It is equivalent to the existence of a unique \(\omega_p\in L(G)_*^+\) with

<a id="equation-gda13"></a>

\[
\omega_p(\lambda_g)=p(g),\qquad\omega_p\leq\Omega.
\tag{GDA13}
\]
One direction follows from (GDA4). Conversely define \(Th=\rho(h)v\) on \(C_c(G)\). The integrated group product and adjoint formulas make its squared norm the left side of (GDA12), so it extends to a contraction \(T:L^2(G)\to H_\rho\). It intertwines \(\lambda_g\) with \(\rho_g\), and has dense range by cyclicity and the compact-bump limit. Its linear polar decomposition \(T=U|T|\), proved in HA-R4, therefore has \(UU^*=1\); its partial isometry intertwines the two representations, by uniqueness on the positive range. Put \(\zeta=U^*v\). It gives the normal functional \(\omega_p(X)=\langle X\zeta,\zeta\rangle\), with the required coefficients. Moreover
\(\lambda(h)\zeta=U^*\rho(h)v=|T|h\),
so \(\zeta\) is right bounded with \(\|R_\zeta\|\leq1\). For every \(X\) with finite \(\Omega(X)\), its actual square root is \(\lambda_\xi\) and WH04.3 gives

<a id="equation-gda14"></a>

\[
\omega_p(X)=\|\lambda_\xi\zeta\|^2
=\|R_\zeta\xi\|^2\leq\|\xi\|^2=\Omega(X).
\tag{GDA14}
\]
For infinite \(\Omega(X)\), domination is automatic. Coefficients of normal functionals determine them because the linear span of \(\lambda(G)\) is ultraweakly dense. This proves the equivalence and its order correspondence.

Consequently \(\mathcal P^\circ\), the positive-definite functions corresponding to \(\mathcal F_\Omega^\circ\), is directed in the order \(p\leq q\) meaning \(q-p\) positive definite. Its corresponding functionals have supremum \(\Omega\) on every positive element. For every \(g\in L^1(G)\),

<a id="equation-gda15"></a>

\[
\sup_{p\in\mathcal P^\circ}
\int\!\!\int p(st^{-1})g(s)\overline{g(t)}\,dsdt
=\int_G\delta(s)|g(s)|^2ds.
\tag{GDA15}
\]
The double integral is absolutely convergent for each \(p\), since \(|p|\leq p(e)\). In fact it is
\(\omega_p(\lambda(g^\#)^*\lambda(g^\#))\): substitute
\(\lambda(g^\#)=\int\overline{g(s)}\lambda_{s^{-1}}ds\)
and evaluate its squared vector norm. Formula (GDA10), followed by (GDA5), proves (GDA15); Haar inversion gives \(\|g^\#\|_2^2=\int\delta(s)|g(s)|^2ds\). This remains valid when that integral is infinite. The normalized \(L^1\) involution is essential in a nonunimodular group.

We also need a positive compact-convolution test:

<a id="equation-gda16"></a>

\[
f\in C_c(G),\quad\lambda(f)\geq0
\quad\Longrightarrow\quad\Omega(\lambda(f))=f(e).
\tag{GDA16}
\]
Here are its finite-domain details. The continuous kernel of \(\lambda(f)\) is \(f(tu^{-1})\delta(u)^{-1}\). Localized normalized scalar bumps at finitely many points turn its positivity into positivity of the kernel matrices. Multiplying rows/columns by the positive \(\delta\)-factors shows that \(h(s)=\delta(s)^{1/2}f(s)\) is positive definite. Explicitly the kernel becomes
\(\delta(t)^{-1/2}\delta(u)^{-1/2}h(tu^{-1})\).
Use its cyclic representation from (GDA11), and on \(C_c(G)\) put

<a id="equation-gda17"></a>

\[
Tq=\int_G\delta(t)^{-1/2}q(t)\rho_{t^{-1}}v\,dt.
\tag{GDA17}
\]
Its squared norm is \(\langle\lambda(f)q,q\rangle\). Hence \(T\) extends boundedly, with \(T^*T=\lambda(f)\), and its range is dense by compact bumps at each point. If \(r_s q(t)=\delta(s)^{1/2}q(ts)\), Haar substitution gives \(Tr_s=\rho_sT\). The polar decomposition \(T=U\lambda(f)^{1/2}\) has \(UU^*=1\) and \(U\) intertwines these representations. Thus \(\zeta=U^*v\) has \(\|\zeta\|_2^2=h(e)=f(e)\), and for \(q\in C_c(G)\),

<a id="equation-gda18"></a>

\[
\lambda(f)^{1/2}q=U^*Tq
=\int\delta(t)^{-1/2}q(t)r_{t^{-1}}\zeta\,dt
=\zeta*q.
\tag{GDA18}
\]
Take the normalized bumps \(q_i\) from GDA1. The operators \(\lambda(f)^{1/2}\lambda(q_i)\) lie in \(N_\Omega\), are uniformly bounded, and tend boundedly strongly* to \(\lambda(f)^{1/2}\). Their GNS vectors are \(\lambda(f)^{1/2}q_i=\zeta*q_i\to\zeta\). EW2 identifies the complete GNS limit. Therefore \(\lambda(f)^{1/2}\in N_\Omega\), and its squared GNS norm proves (GDA16). No positive convolution root was merely assumed to belong to the finite ideal.

In particular, if \(f\in C_c(G)\) and \(\int p(t)f(t)dt\geq0\) for every continuous positive-definite \(p\), then \(\lambda(f)\geq0\): test the positive normal functionals of \(L(G)\), whose group coefficients are such functions. Thus (GDA10) and (GDA16) give

<a id="equation-gda19"></a>

\[
\sup_{p\in\mathcal P^\circ}\int_Gp(t)f(t)dt=f(e).
\tag{GDA19}
\]

<a id="gda-4"></a>

## GDA4. Normal Schur maps and their whole extended supremum

On \(K=L^2(G,H)\), for any continuous positive-definite \(p\), define the bounded map

<a id="equation-gda20"></a>

\[
(V\xi)(t)=\xi(t)\otimes\rho_{t^{-1}}v,
\qquad
F_p(X)=V^*(X\otimes1)V\quad(X\in B(K)).
\tag{GDA20}
\]
The tensor/function identification is obtained first on compact continuous sections and finite tensors; their dense completions agree by the already proved vector-integration facts. The pointwise formula gives \(\|V\|^2=p(e)\). Amplification is normal: positive normal tests are vector series and finite tensors are dense, so bounded increasing nets converge strongly in each amplified vector test. Hence \(F_p\) is normal and completely positive.

Let \(D_0=1_H\otimes L^\infty(G)\), the scalar multiplication algebra, and \(Q=D_0'\). The map \(V\) intertwines every operator in \(Q\) with its amplification: on finite scalar/vector tensors this is immediate for constants and multiplication, and equivalently \(V\) is the strong sum of scalar multiplication maps along an orthonormal basis of \(H_\rho\). For detail, if \(a_i(t)=\langle\rho_{t^{-1}}v,e_i\rangle\), then \(\sum_i|a_i(t)|^2=p(e)\); finite sums increase uniformly on each compact set by compactness of the continuous feature-vector range. Thus

<a id="equation-gda21"></a>

\[
F_p(X)=\sum_i M_{\overline{a_i}}X M_{a_i}
\tag{GDA21}
\]
with normal strong positive sums, first on positive \(X\), then linearly. The scalar multipliers commute with \(Q\), proving its bimodule identity. This argument uses only countable coordinates for each compact feature range, not a countable basis of the whole representation.

The kernel factor is \(p(tu^{-1})\). In particular

<a id="equation-gda22"></a>

\[
F_p(\lambda_s)=p(s)\lambda_s,
\qquad F_p(aXb)=aF_p(X)b\quad(a,b\in Q).
\tag{GDA22}
\]
The multiplier and left/right regular translations generate \(B(L^2(G))\): for \(f,g\in C_c(G)\), choose a compact continuous \(h=1\) on \(\operatorname{supp}f\,\operatorname{supp}g^{-1}\). The operator \(M_f\lambda(h)M_{\delta\overline g}\) has kernel \(f(t)\overline{g(u)}\), hence is the rank-one operator \(\eta\mapsto\langle\eta,g\rangle f\). Compact scalar functions are dense, so these rank ones generate all bounded operators. Inversion conjugates left into right translation, leaving multiplication invariant. Only the commutant definition \(Q=D_0'\) is used below; no pointwise decomposition theorem for its operators is needed.

These relations determine \(F_p\) uniquely: the span of \(\lambda_s a\), \(a\in Q\), is a star algebra and contains a weakly dense algebra by the rank-one argument. Normal bimodule maps agreeing there agree everywhere. Thus \(F_{p+q}=F_p+F_q\), and positive-definite order implies completely positive order. Define

<a id="equation-gda23"></a>

\[
S(X)(\omega)=\sup_{p\in\mathcal P^\circ}\omega(F_p(X)),
\quad X\in B(K)_+,\quad\omega\in B(K)_*^+.
\tag{GDA23}
\]
Directedness proves additivity in \(\omega\), including infinite values; a common upper index approximates both summands. It is homogeneous and norm lower semicontinuous as a supremum of bounded continuous evaluations. EP2–4 therefore give an actual element of \(\widehat{B(K)}_+\). The same common-index argument proves additivity and homogeneity in \(X\). Normality follows by interchanging the supremum over \(p\) with the supremum of a bounded increasing \(X_i\), since every \(F_p\) is normal. The \(Q\)-sandwich identity also passes to this entire extended supremum.

Its values belong to \(\widehat Q_+\). Let \(A_\xi\eta=\langle\eta,\xi\rangle\xi\) be a positive rank-one operator. For \(\eta\in K\), put \(g(t)=\langle\xi(t),\eta(t)\rangle\), which belongs to \(L^1\). Formula (GDA21) and Cauchy–Schwarz/Fubini on the actual finite-exponent carriers give

<a id="equation-gda24"></a>

\[
S(A_\xi)(\omega_\eta)
=\sup_{p\in\mathcal P^\circ}\int\!\!\int p(st^{-1})g(s)\overline{g(t)}dsdt
=\int_G\delta(t)|\langle\xi(t),\eta(t)\rangle|^2dt.
\tag{GDA24}
\]
The first expression means the extended quadratic-form value, not a bounded-operator pairing assumed finite. The form is invariant under every unitary scalar multiplier. EP's unique closed form and full spectral projections therefore put \(S(A_\xi)\) in \(\widehat Q_+\), retaining any infinite part. Every \(X\geq0\) is the increasing sum of rank ones \(A_{X^{1/2}e_i}\) over finite subsets of an orthonormal basis. Normality of \(S\), EP4 and the spectral fixed-point test show that \(S(X)\in\widehat Q_+\). This argument never requires a common pointwise orthonormal basis of the coefficient fields.

The map \(S\) is faithful. If \(\xi\ne0\), (GDA24) at \(\eta=\xi\) is strictly positive, possibly infinite, because \(\delta>0\). Thus a zero \(S(X)\) makes every rank-one summand just used zero and forces \(X=0\).

<a id="gda-5"></a>

## GDA5. The value algebra is precisely the coefficient algebra

Each regular coefficient \(\pi(a)\) commutes with scalar multiplication and hence belongs to \(Q\). Formula (GDA22) gives

<a id="equation-gda25"></a>

\[
E_p(\lambda_s\pi(a))=p(s)\lambda_s\pi(a),\qquad E_p=F_p|_R.
\tag{GDA25}
\]
Normality and generator density imply \(F_p(R)\subset R\). Therefore \(T(X)=S(X)\), \(X\in R_+\), is an extended positive element affiliated both with \(R\) and with \(Q\). We prove \(R\cap Q=\pi(M)\), without a decomposable-field theorem.

Use NR1's strongly continuous standard implementing group \(U_s\) on \(H\); normal model independence NR4 allows this choice. The right commutant unitaries and the unitary change of coordinates are

<a id="equation-gda26"></a>

\[
(V_s\xi)(t)=\delta(s)^{1/2}U_s\xi(ts),
\qquad (W\xi)(t)=U_t\xi(t).
\tag{GDA26}
\]
CCM gives \(V_s\in R'\); every constant \(b'\in M'\) is also in \(R'\). Direct substitution gives \(WV_sW^*=r_s\), the scalar right regular translation, and \(W\pi(a)W^*=a\otimes1\). The unitary \(W\) commutes with scalar multiplication. If \(X\in R\cap Q\), then \(WXW^*\) commutes with both right translations and multiplication. The rank-one proof in GDA4 shows that it commutes with \(1_H\otimes B(L^2(G))\), so \(WXW^*=a\otimes1\). This tensor commutant assertion follows directly by testing scalar rank ones on simple tensors, and is valid for arbitrary \(H\).

Commutation with \(W(b'\otimes1)W^*\) then tests the continuous scalar functions \(\langle[a,U_tb'U_t^*]\xi,\eta\rangle\). Compact scalar-vector tests make their integrals against every \(C_c\) test zero. Positivity of Haar measure on open sets makes each continuous function zero everywhere. At \(t=e\), this gives \([a,b']=0\) for every \(b'\in M'\), hence \(a\in M\) and \(X=\pi(a)\). The reverse inclusion was already noted.

The finite-part projection and each finite-part spectral projection of \(T(X)\) thus lie in \(R\cap Q=\pi(M)\). EP2–3 reconstruct its whole value in \(\widehat{\pi(M)}_+\), including the infinite subspace. Normality, faithfulness and \(\pi(M)\)-bimodularity follow from GDA4; a normal inclusion into \(B(K)\) preserves the extended-positive tests, since EP1 supplies positive normal extensions of every normal functional of the subalgebra. Hence

<a id="equation-gda27"></a>

\[
T:R_+\longrightarrow\widehat{\pi(M)}_+
\tag{GDA27}
\]
is a faithful normal operator-valued weight. The normal Schur maps are intrinsic by (GDA25) and normal generator density, so NR4 transports the same entire map to every faithful normal initial regular representation.

<a id="gda-6"></a>

## GDA6. Bounded compact-square values, semifiniteness and group scaling

For \(x\in\mathscr K\), let \(z=x^\#*x\). It is compact, bounded and strongly* continuous by CCM4. For \(\omega\in R_*^+\), the continuous compact scalar function
\(f_\omega(t)=\omega(\lambda_t\pi(z(t)))\)
satisfies

<a id="equation-gda28"></a>

\[
\int p(t)f_\omega(t)dt=\omega(E_p(L_x^*L_x))\geq0
\tag{GDA28}
\]
for every continuous positive-definite \(p\). Normality of \(E_p\) and its generator formula justify passage through the compact integral. GDA3's full scalar test now gives

<a id="equation-gda29"></a>

\[
T(L_x^*L_x)(\omega)=f_\omega(e)
=\omega\left(\pi\left(\int x(t)^*x(t)dt\right)\right).
\tag{GDA29}
\]
These values determine the bounded positive operator on the right, by EP1–3. In particular \(L(\mathscr K)\subset N_T\). This coefficient algebra is ultraweakly dense by GDW2/CCM, hence \(T\) is semifinite. EP6 supplies its actual whole ideals
\(N_T=\{X:T(X^*X)\in\pi(M)_+\}\)
and \(m_T=\operatorname{span}N_T^*N_T\), with a coefficient-algebra-valued bimodule linear extension on this finite algebra; the extension need not be norm-bounded. We have proved finiteness of the compact coefficients, not asserted that they equal those whole ideals.

For scaling, (GDA25) on generators and normality give
\(E_p(\lambda_sX\lambda_s^*)=\lambda_s E_{p^s}(X)\lambda_s^*\),
where \(p^s(t)=p(sts^{-1})\). By (GDA6), the corresponding normal-functional transformation \(\omega_p\mapsto\omega_p\circ\operatorname{Ad}\lambda_s\) is an order bijection from the strict \(\Omega\)-minorants to the strict \(\delta(s)\Omega\)-minorants. Linearity of the Schur construction and the cofinal strict family consequently give

<a id="equation-gda30"></a>

\[
\sup_{p\in\mathcal P^\circ}E_{p^s}(X)=\delta(s)T(X).
\tag{GDA30}
\]
This is an equality in the entire extended cone, tested on every normal positive functional. Sandwiching proves (GDA2) with its stated Haar factor and nonabelian order.

<a id="gda-7"></a>

## GDA7. A dense GNS test determines the weight

The following Hilbert-space observation is the mechanism. Let \(B\) be a closed positive self-adjoint operator on a Hilbert space \(H\), and let \(\mathcal E\subset D(B)\) be a dense linear subspace on which \(\|B\xi\|=\|\xi\|\). Then \(B=1\). Indeed, for any \(\xi\in H\), choose \(\xi_n\in\mathcal E\) tending to \(\xi\). Linearity gives
\[
 \|B\xi_n-B\xi_m\|=\|\xi_n-\xi_m\|,
\]
so \(B\xi_n\) converges. Closedness puts \(\xi\) in \(D(B)\) and identifies that limit with \(B\xi\). Thus \(D(B)=H\) and \(B\) is an isometry. Polarization gives \(B^*B=1\); since \(B=B^*\geq0\), uniqueness of the positive square root of \(1\), proved in [CF9](OA-FLOW-CF.md#oa-flow.cf.9), gives \(B=1\). The approximating sequence is chosen separately for each vector; the Hilbert space need not be separable.

**GNS uniqueness criterion.** Let \(\Phi,\Psi\) be faithful normal semifinite weights on a von Neumann algebra \(N\), with the same modular automorphism group. Suppose a linear subspace \(\mathcal C\subset\mathfrak n_\Phi\) satisfies
\[
 \overline{\Lambda_\Phi(\mathcal C)}=H_\Phi,\qquad
 \Psi(a^*a)=\Phi(a^*a)\quad(a\in\mathcal C).
\]
Then \(\Psi=\Phi\) on the entire positive cone. No algebra or multiplication-invariance condition on \(\mathcal C\) is required.

**Central density.** We first derive the density needed for the criterion from the earlier local proofs. If faithful n.s.f. weights \(\rho,\nu\) have \((D\rho:D\nu)_r=1\), [BC4](OA-FLOW-BC.md#bc-4) gives the constant off-diagonal orbit \(\beta_r^{\rho,\nu}(1)=1\). Its norm-entire extension has values one at \(-i\) and \(-i/2\). [MA4](OA-FLOW-MA.md#oa-flow.ma.4), equation MA11 with \(k=1\), gives both inequalities \(\rho(h)\leq\nu(h)\) and \(\nu(h)\leq\rho(h)\), for every \(h\geq0\), including infinite values. The BC chain rule also proves injectivity for cocycles with a fixed reference weight.

Equality of the modular groups makes \(u_r=(D\Psi:D\Phi)_r\) central, by BC4. The group fixes the center: a central self-adjoint multiplier commutes with the full finite-star involution and its adjoint, hence with their positive product and imaginary powers, by [NC4](OA-FLOW-NC.md#oa-flow.nc.4). The cocycle law is consequently \(u_{r+s}=u_ru_s\). [RF5](OA-FLOW-RF.md#rf-5) gives the self-adjoint generator \(A\), with \(u_r=e^{irA}\). Its resolvents and spectral projections commute with every operator commuting with the center, so \(A\) is affiliated with the center. The full Borel calculus of [SF](OA-FLOW-SF.md#oa-flow.sf.sb3) gives the positive nonsingular central operator \(h=e^A\). The density construction [CZ1–6](OA-FLOW-CZ.md#cz-1) supplies a faithful n.s.f. weight \(\Phi_h\) with cocycle \(h^{ir}=u_r\). Fixed-reference injectivity therefore gives
<a id="equation-gda31"></a>
\[
 \Psi(X)=\Phi_h(X)
 =\sup_n\Phi(h_n^{1/2}Xh_n^{1/2}),\qquad
 h_n=\min(h,n),\quad X\in N_+.
 \tag{GDA31}
\]
To compare these cutoffs with CZ's resolvent regularizations, use
\(h(1+\varepsilon h)^{-1}\leq h_n\) when \(n\geq\varepsilon^{-1}\), and
\(h_n\leq(1+\varepsilon n)h(1+\varepsilon h)^{-1}\).
Centrality makes these positive-operator inequalities valid inside the weight evaluations. Letting \(n\) and \(\varepsilon^{-1}\) increase proves equality of the two suprema, including their infinite values.

**Proof of the criterion.** Represent \(N\) faithfully on \(H_\Phi\), as in [NF5](OA-FLOW-NF.md#oa-flow.nf.5), and transport the spectral projections of \(h\) by this normal representation. Let \(B=\pi_\Phi(h)^{1/2}\) be the resulting closed positive operator, with its full domain from [SB3–4](OA-FLOW-SF.md#oa-flow.sf.sb3). For \(a\in\mathfrak n_\Phi\), centrality and the bounded GNS identity give
<a id="equation-gda32"></a>
\[
 \begin{aligned}
 \Psi(a^*a)
 &=\sup_n\Phi(a^*h_n a)\\
 &=\sup_n\|\pi_\Phi(h_n)^{1/2}\Lambda_\Phi(a)\|^2
 =\|B\Lambda_\Phi(a)\|^2 .
 \end{aligned}
 \tag{GDA32}
\]
The last expression is interpreted as infinity off \(D(B)\); its equality with the supremum is precisely the positive spectral-domain criterion. On \(\mathcal E=\Lambda_\Phi(\mathcal C)\) the hypothesis makes it finite and gives \(\|B\xi\|=\|\xi\|\). The dense-space observation proves \(B=1\). Faithfulness of \(\pi_\Phi\), applied to the spectral projections, then gives \(h=1\). Equation (GDA31) proves \(\Psi=\Phi\) on all \(N_+\). Only the closed operator is extended from a dense set; no continuity of an unbounded weight on a dense positive subset is assumed. \(\square\)

**Application to the dual weight.** Take \(\Phi=\widehat\varphi\), the weight constructed by GDW. Suppose a faithful n.s.f. weight \(\Psi\) has its two modular generator formulas and the same quadratic values at every \(L_x\), \(x\in\mathscr B_\varphi\). Normality and the two generating families give equality of the modular groups on \(R\). Use the linear space
\(\mathcal C=L(\mathscr D_\varphi)\subset L(\mathscr B_\varphi)\).
[GDW6](OA-FLOW-GDW.md#gdw-6) identifies
\(\Lambda_\Phi(L_x)=\eta_\varphi(x)\), and [GDW2](OA-FLOW-GDW.md#gdw-2) proves that \(\eta_\varphi(\mathscr D_\varphi)\) is dense in the whole \(L^2(G,H_\varphi)\). The GNS criterion therefore applies and yields
<a id="equation-gda33"></a>
\[
 \Psi=\widehat\varphi\quad\hbox{on the entire positive cone}.
 \tag{GDA33}
\]
The group, algebra and Hilbert space retain their full arbitrary scope. The classical dual-weight characterization appears in Takesaki, [*Theory of Operator Algebras II*, Chapter X, Lemma 1.18, printed p.250](https://doi.org/10.1007/978-3-662-10451-4); the criterion above uses the closed positive density operator on the GNS Hilbert space.

### The closed-graph mechanism

![Central density, the GNS quadratic identity, closed-graph extension and positivity](../assets/gns-weight-uniqueness/gns-weight-uniqueness.png)

The four boxes display the actual proof maps and domains. The density \(h\) is central and nonsingular; \(B=\pi_\Phi(h)^{1/2}\) acts on \(H_\Phi\), and \(\mathcal E=\Lambda_\Phi(\mathcal C)\) is a linear dense subspace of its domain. Equality (GDA32) makes \(B|_{\mathcal E}\) isometric. For every \(\xi\in H_\Phi\), the two coordinates of \((\xi_n,B\xi_n)\) converge, so the closed graph puts their limit in the graph of \(B\). This proves the full domain assertion before positivity forces \(B=1\). A general isometry need not be the identity; positivity is the essential final hypothesis. The diagram is a logical schematic of this arbitrary-dimensional argument, not a numerical or finite-dimensional approximation.

The local proofs used for the central density are MA4, BC4, NC4, RF5 and CZ1–6, as specified above. [Editable SVG](../assets/gns-weight-uniqueness/gns-weight-uniqueness.svg), [exact diagram labels](../assets/gns-weight-uniqueness/data.json), and [reproduction source](../assets/gns-weight-uniqueness/render.py) accompany the figure. The diagram and caption are CC0-1.0 to the extent of rights held; DejaVu font terms remain applicable.

<a id="gda-8"></a>

## GDA8. Composition is the full GDW weight, for every faithful input

For faithful n.s.f. \(\varphi\) on \(M\), set \(\Psi_\varphi=\widehat{\varphi\circ\pi^{-1}}\circ T\). EP5–6 prove that it is faithful normal semifinite on the whole \(R_+\). OT gives
\(\sigma_r^{\Psi_\varphi}(\pi(a))=\pi(\sigma_r^\varphi(a))\).

We need the exact inner convention. For any faithful n.s.f. \(\nu\) and unitary \(v\),

<a id="equation-gda34"></a>

\[
(D(\nu\circ\operatorname{Ad}v):D\nu)_r=v^*\sigma_r^\nu(v).
\tag{GDA34}
\]
To prove it from BC, transport \(\Theta(\nu,\nu)\) by \(\operatorname{diag}(v,1)\). Its two corner weights are \(\nu\circ\operatorname{Ad}v,\nu\). BC5 transports the modular group. On \(E_{21}\) its coefficient is \(\sigma_r^\nu(v^*)v\), as direct diagonal multiplication shows. BC4 identifies this as the reverse cocycle; take its adjoint. This proves (GDA34) with the actual weight normalization.

Equation (GDA2) gives
\(\Psi_\varphi\circ\operatorname{Ad}\lambda_s=\delta(s)\Psi_{\varphi\circ\alpha_s}\).
OT's two-composition cocycle identity, BC5's positive scalar rule and (GDA34) therefore give

<a id="equation-gda35"></a>

\[
\sigma_r^{\Psi_\varphi}(\lambda_s)
=\delta(s)^{ir}\lambda_s\pi((D(\varphi\circ\alpha_s):D\varphi)_r).
\tag{GDA35}
\]
The coefficient stays to the right; no commutation was used. These are exactly GDW7's two modular generators.

For \(x\in\mathscr B_\varphi\), (GDA29) and GDW1's bounded normal finite-coefficient pairing give

<a id="equation-gda36"></a>

\[
\Psi_\varphi(L_x^*L_x)
=\varphi\left(\int x(t)^*x(t)dt\right)
=\|\eta_\varphi(x)\|_2^2
=\widehat\varphi(L_x^*L_x)<\infty.
\tag{GDA36}
\]
The unbounded \(\varphi\) is not formally moved through an operator integral: write \(x\) as finite right-ideal coefficients and use exactly GDW1's bounded normal sandwich functionals. GDA7 now identifies \(\Psi_\varphi=\widehat\varphi\) on every positive element. Thus (GDA3)'s first identity has complete finite-ideal and positive-cone meaning; GDW6's actual entire ideal and GNS data remain unchanged.

For any normal \(\theta\), define its dual by this same whole composition. EP5–6 prove normality without faithfulness or semifiniteness assumptions. Its complete finite and null ideals are, exactly,

<a id="equation-gda37"></a>

\[
N_{\widehat\theta}=\{X:\widehat{\theta\circ\pi^{-1}}(T(X^*X))<\infty\},
\quad
N^0_{\widehat\theta}=\{X:\widehat{\theta\circ\pi^{-1}}(T(X^*X))=0\}.
\tag{GDA37}
\]
Its finite algebra and quotient GNS construction are GW1–3 at these ideals. No n.s.f. or faithful relative-modular conclusion is asserted for such a general input. On compact squares its value is \(\theta(\int x(t)^*x(t)dt)\), possibly infinite. Additivity, nonnegative scalar factors including zero, and arbitrary-index sums are preserved: apply EP5's increasing bounded spectral approximations to a fixed extended value, then interchange its supremum with the finite-partial-sum supremum. This proves these laws on the whole cone, not just on coefficient tests.

<a id="gda-9"></a>

## GDA9. Two dual weights and their full relative spectral domains

For faithful n.s.f. \(\varphi,\psi\), GDA8 has identified both constructed weights with their compositions with this single \(T\). OT's complete relative strip/domain theorem gives

<a id="equation-gda38"></a>

\[
(D\widehat\psi:D\widehat\varphi)_r=\pi((D\psi:D\varphi)_r)
\quad(r\in\mathbb R).
\tag{GDA38}
\]
This is the balanced-weight normalized cocycle, not merely an intertwiner of modular automorphisms. Its chain, adjoint and scalar laws are the actual BC laws; in particular no central phase is lost.

In \(K_\varphi=L^2(G,H_\varphi)\), let \(\widehat\Delta_{\psi,\varphi}\) be BC2's whole relative positive operator for these two dual weights, and let

<a id="equation-gda39"></a>

\[
K_t^{\psi,\varphi}=\delta(t)\Delta_{\psi\circ\alpha_t,\varphi}.
\tag{GDA39}
\]
BC3's full imaginary-power identity, GDW7 and (GDA38) give, for every real \(r\),

<a id="equation-gda40"></a>

\[
(\widehat\Delta_{\psi,\varphi}^{ir}\xi)(t)
=(K_t^{\psi,\varphi})^{ir}\xi(t).
\tag{GDA40}
\]
Indeed the noncommutative coefficient product is
\(\alpha_{t^{-1}}((D\psi:D\varphi)_r)(D(\varphi\circ\alpha_t):D\varphi)_r
=(D(\psi\circ\alpha_t):D\varphi)_r\),
by BC5 covariance followed by BC4 chain. Relative operators are injective by BC2, so their logarithms have the full SF domains.

Here is the whole-domain passage, rather than a fiber formula on an unspecified dense class. Write \(A=\log\widehat\Delta_{\psi,\varphi}\), \(A_t=\log K_t^{\psi,\varphi}\). Its bounded resolvent is

<a id="equation-gda41"></a>

\[
(A-i)^{-1}=i\int_0^\infty e^{-r}\widehat\Delta_{\psi,\varphi}^{-ir}dr.
\tag{GDA41}
\]
SF's scalar spectral integral verifies the identity on every vector; the integrand is a continuous norm-bounded Hilbert field and the tail is integrable. The pointwise imaginary powers are jointly strongly continuous on fixed vectors: BC chain gives \((D(\psi\circ\alpha_t):D\varphi)_r=(D(\psi\circ\alpha_t):D\psi)_r(D\psi:D\varphi)_r\); GDW7 supplies joint strong* continuity of the first factor, applied to \(\psi\), and the second factor and \(\Delta_\varphi^{ir}\) are strongly continuous in \(r\). Multiplication by \(\delta(t)^{ir}\) preserves this conclusion. Strongly measurable simple approximants to \(\xi\) therefore give joint strong measurability of the field in (GDA40). Scalar/Fubini tests on its actual countable compact carriers, with the uniform \(e^{-r}\) bound, identify (GDA41) pointwise with \((A_t-i)^{-1}\xi(t)\). Its adjoint has the analogous formula. Polynomial/uniform calculus of these resolvents, interval-projection approximations, finite intersections and countable disjoint sums give the whole Borel calculus, exactly as in GDW5; the missing point at infinity has no spectral mass. Unbounded truncation and SC monotone convergence consequently prove, for every finite complex-valued Borel function \(q\) on \((0,\infty)\),

<a id="equation-gda42"></a>

\[
D(q(\widehat\Delta_{\psi,\varphi}))
=\left\{\xi:\xi(t)\in D(q(K_t^{\psi,\varphi}))\text{ a.e.},\ 
\int_G\|q(K_t^{\psi,\varphi})\xi(t)\|^2dt<\infty\right\},
\quad(q(\widehat\Delta_{\psi,\varphi})\xi)(t)
=q(K_t^{\psi,\varphi})\xi(t).
\tag{GDA42}
\]
The output field is strongly measurable by the same bounded-resolvent approximation and truncated norm limit. These exact domains include positive square roots, real/complex powers and logarithms; the operators have no zero eigenvector. The single-input GNS/involution domains are the already proved GDW domains, and the full relative graph and polar domains are BC2's restrictions of the complete balanced graph. No measurable disintegration or finite-state shortcut is used.

This proves the general whole-cone averaging map, all-normal-input extension, equality with every faithful n.s.f. GDW construction and the normalized comparison of two such dual weights.

<a id="gda-10"></a>

## GDA10. A scalar composition determines the operator-valued map

The extended-value and form arguments here use [EP2–5](OA-FLOW-EP.md#ep-2), the dense GNS left module of [GW1–4](OA-FLOW-GW.md#oa-flow.gw.1), its faithful normal representation in [NF5](OA-FLOW-NF.md#oa-flow.nf.5), and [SB4's unbounded spectral domains and graph cutoffs](OA-FLOW-SF.md#oa-flow.sf.sb4), together with [SF1's affiliation and normal transport](OA-FLOW-SF.md#oa-flow.sf.sf1). A direct uniqueness argument in the operator-valued setting is also given in [compatible modular operator-valued weights](../../OA-MOD/OA-MOD-OE.html#faithfulness-semifiniteness-and-direct-uniqueness).

**Theorem.** Let \(P\subseteq N\) be von Neumann algebras and let \(S_1,S_2:N_+\to\widehat P_+\) be operator-valued weights. If a faithful normal semifinite weight \(\varphi\) on \(P\) satisfies

<a id="equation-gdau1"></a>

\[
 \overline\varphi\circ S_1=\overline\varphi\circ S_2
 \quad\hbox{on all }N_+,
 \tag{GDAU1}
\]

then \(S_1=S_2\). The bar denotes EP5's evaluation on the entire extended positive cone. Consequently the map \(T\) of GDA1–8 is the unique operator-valued weight with its scalar composition identities for all faithful normal semifinite input weights. No countability assumption is made.

**Proof.** Denote the common scalar composition by \(\Phi\), fix \(X\in N_+\), and set \(Y_i=S_i(X)\). In the faithful normal GNS representation of \(P\), write \(D=\Lambda_\varphi(\mathfrak n_\varphi)\). GW proves that \(D\) is dense and invariant under every element of \(P\). Let \(q_i\) be the extended closed quadratic form of \(Y_i\), including the component where its value is infinite. For \(a\in\mathfrak n_\varphi\), bounded spectral truncations, the GNS identity and EP4–5 give

<a id="equation-gdau2"></a>

\[
 q_i(\Lambda_\varphi(a))
 =\overline\varphi(a^*Y_i a)
 =\Phi(a^*Xa).
 \tag{GDAU2}
\]

Indeed for bounded positive \(b\in P\) the first identity is \(\langle\pi_\varphi(b)\Lambda_\varphi(a),\Lambda_\varphi(a)\rangle=\varphi(a^*ba)\). The normal vector functional and normal congruence extend it to \(Y_i\); the second identity is \(P\)-bimodularity of \(S_i\). Thus \(q_1=q_2\) on \(D\), with infinite values retained.

To pass from this equality to the entire forms, write \((e_i,A_i)\) for EP's finite-part projection and positive affiliated operator representing \(Y_i\). Let \(e_{i,n}=1_{[0,n]}(A_i)\), zero on the infinite component. Its range satisfies \(q_i\leq n\|\cdot\|^2\), and \(e_{i,n}D\subseteq D\). Spectral truncation approximates each finite-domain vector \(\xi\) by \(e_{i,n}\xi\) in the form norm \(\|\xi\|_{q_i}=(\|\xi\|^2+q_i(\xi))^{1/2}\). For fixed \(n\), choose \(d_j\in D\) with \(d_j\to\xi\) in Hilbert norm. Then

<a id="equation-gdau3"></a>

\[
 \|e_{i,n}(d_j-\xi)\|_{q_i}
 \leq\sqrt{1+n}\,\|d_j-\xi\|\longrightarrow0.
 \tag{GDAU3}
\]

It follows that \(D\cap\operatorname{Dom}(q_i)\) is a form core, and its Hilbert closure is the finite-part space \(e_iH_\varphi\). Equation(GDAU2) makes the two finite subsets of \(D\) equal and their polarized forms equal. Closing the common core gives identical entire closed forms and identical finite-part projections. EP3's uniqueness therefore gives \(Y_1=Y_2\). Since \(X\) was arbitrary, \(S_1=S_2\). No subtraction of infinite weight values, or continuity of an unbounded weight on a merely dense positive set, is used.

For the canonical-map conclusion one faithful normal semifinite scalar input is sufficient. Such an input exists on every nonzero concrete \(P\subseteq B(K)\), without a faithful-state assumption. For a nonzero projection \(p\), choose nonzero \(v\in pK\) and let \(e\) project onto \(\overline{P'v}\). The subspace reduces \(P'\), so \(e\in P\) and \(e\leq p\), by [CF8's projection construction](OA-FLOW-CF.md#oa-flow.cf.8) and [BD1's bicommutant characterization](OA-FLOW-BD.md#oa-flow.bd.1). The normalized vector functional is faithful on \(ePe\): if \(a\in(ePe)_+\) has zero value, \(a^{1/2}\) kills \(v\), hence kills \(P'v\) by commutation, and therefore \(a=0\).

Choose a maximal mutually orthogonal family of these nonzero projections \(e_i\), with unit vectors \(v_i\). Their join is one: a nonzero complementary projection would supply a further pair by the same construction. Define

<a id="equation-gdau4"></a>

\[
 \varphi(a)=\sup_{F\subseteq I,\ F\text{ finite}}
       \sum_{i\in F}\langle av_i,v_i\rangle
 \quad(a\in P_+).
 \tag{GDAU4}
\]

A common finite superset of indices proves additivity and homogeneity. Vector functionals are normal by [CP4/6](OA-FLOW-CP.md#oa-flow.cp.4) and the bounded increasing-operator lemma [WF2](OA-FLOW-WF.md#oa-flow.wf.2). Interchanging the two nonnegative suprema for a bounded increasing positive net proves normality of(GDAU4). If its value is zero, \(a^{1/2}\) kills every \(v_i\) and \(P'v_i\), hence all \(K\), so it is faithful. For finite \(F\), \(p_F=\sum_{i\in F}e_i\) has \(\varphi(p_F)=|F|<\infty\). These projections increase strongly to one; [GW4's finite-projection criterion](OA-FLOW-GW.md#oa-flow.gw.4) proves semifiniteness. The maximal principle is the earlier CF1 choice convention, and the index set may be arbitrary. Applying(GDAU1) to this one input proves uniqueness of \(T\). On the zero algebra the only map is zero. \(\square\)

<a id="gda-11"></a>

## GDA11. The balanced derivative under the action

Let \(\varphi,\psi\) be faithful normal semifinite weights on \(M\), set \(\chi=\varphi\oplus\psi\) on \(M_2(M)\), and let \(\beta=\alpha\otimes\mathrm{id}_2\). For fixed \(s\in G\), write \(\varphi_s=\varphi\circ\alpha_s\) and \(\psi_s=\psi\circ\alpha_s\). [BC1](OA-FLOW-BC.md#bc-1) gives \(\chi\circ\beta_s=\varphi_s\oplus\psi_s\) on the whole positive cone. In particular its second diagonal summand is \(\psi_s\).

**Theorem.** For every \(s\in G\) and \(r\in\mathbb R\),

<a id="equation-gdab1"></a>

\[
 (D(\chi\circ\beta_s):D\chi)_r
 =\begin{pmatrix}
  (D(\varphi\circ\alpha_s):D\varphi)_r&0\\
  0&(D(\psi\circ\alpha_s):D\psi)_r
 \end{pmatrix}.
 \tag{GDAB1}
\]

**Proof.** Identify \(M_2(M_2(M))\) with \(M_4(M)\), ordering the diagonal entries as \((\varphi,\psi,\varphi_s,\psi_s)\). BC1 identifies the outer balanced weight \(\Theta(\chi,\chi\circ\beta_s)\) with this four-weight matrix weight, including all finite GNS domains. The outer lower-left matrix unit becomes \(E_{31}+E_{42}\). [BC3's two-entry corner independence](OA-FLOW-BC.md#bc-3) and [BC4's normalized derivative definition](OA-FLOW-BC.md#bc-4) give

<a id="equation-gdab2"></a>

\[
 \sigma_r^{\Theta_4}(E_{31})=(D\varphi_s:D\varphi)_rE_{31},
 \qquad
 \sigma_r^{\Theta_4}(E_{42})=(D\psi_s:D\psi)_rE_{42}.
 \tag{GDAB2}
\]

Apply the modular group to their sum and read its outer lower-left block. BC4 gives precisely(GDAB1). This determines the normalized unitary itself, without an undetermined central phase. Only the full finite-matrix corner construction is used; compression by an arbitrary centralizer projection is unnecessary. \(\square\)

<a id="gda-12"></a>

## GDA12. Dualization of the balanced weight on the whole cone

With \(\chi\) and \(\beta\) as in GDA11, let \(R_2=M_2(M)\rtimes_\beta G\). The finite coordinate unitary

<a id="equation-gdad1"></a>

\[
 L^2(G,H\otimes\mathbb C^2)
 \cong L^2(G,H)\otimes\mathbb C^2
 \tag{GDAD1}
\]

identifies \(R_2\) normally with \(M_2(R)\). The coefficient generators become \([\pi(a_{ij})]\), and the group generator becomes \(\lambda_s\otimes I_2\). These generate all \(M_2(R)\): the coefficient algebra contains \(I\otimes E_{ij}\), and the diagonal regular generators give every entry of \(R\). [NR4](OA-FLOW-NR.md#oa-flow.nr.4) transports this identification to the faithful GNS regular model of \(\chi\).

The compact function algebras and their integrated operators have the same identification. Write \(\mathscr K_\alpha\) for [GDW1's](OA-FLOW-GDW.md#gdw-1) bounded, compactly supported, strongly* continuous coefficient functions, and define \(\mathscr K_\beta\) in the same way. A matrix field \(F=[f_{ij}]\) is strongly* continuous exactly when its four entries are: apply the coordinate inclusions and projections in one direction, and take the finite sum of the resulting vector norms in the other. Each entry inherits a norm bound and a compact carrier from \(F\). Conversely the union of four compact carriers is compact and \(\|F(s)\|\leq\sum_{i,j}\|f_{ij}(s)\|\). Consequently
<a id="equation-gdad1a"></a>
\[
 \mathscr K_\beta=M_2(\mathscr K_\alpha)
 =\mathscr K_\alpha\odot M_2(\mathbb C),\qquad
 (F*H)_{ij}=\sum_{k=1}^2 f_{ik}*h_{kj},\qquad
 (F^\#)_{ij}=(f_{ji})^\# .
 \tag{GDAD1a}
\]
Here \(\odot\) denotes the algebraic tensor product; no completion is needed for the four matrix coordinates. The convolution and involution identities follow by substituting into (GDW2): \(\beta\) acts entrywise, matrix multiplication contributes the finite sum, and the Haar modular factor is the same for every entry. Under the coordinate unitary (GDAD1),
<a id="equation-gdad1b"></a>
\[
 L_F^\beta
 =\int_G(\lambda_s\otimes I_2)[\pi(f_{ij}(s))]\,ds
 =[L_{f_{ij}}^\alpha] .
 \tag{GDAD1b}
\]
To justify the integral equality, pair with arbitrary two-component Hilbert vectors. Each pairing is a finite sum of scalar integrals of bounded functions on a compact carrier, so the sum and integral interchange. Equality of all these pairings proves the bounded-operator identity. This verifies the identification on the full compact coefficient algebra as well as on the generating operators.

**Theorem.** Under(GDAD1), every \(X=[X_{ij}]\in M_2(R)_+\) satisfies

<a id="equation-gdad2"></a>

\[
 \widehat\chi(X)=\widehat\varphi(X_{11})+
                    \widehat\psi(X_{22}),
 \tag{GDAD2}
\]

including infinite values.

**Proof.** Use [GDA1–4](OA-FLOW-GDA.md#gda-1) with the same group and fixed Haar measure for \(M\) and \(M_2(M)\). Their scalar Plancherel weight and directed strict-minorant family \(\mathcal P^\circ\) are the same. For \(p\in\mathcal P^\circ\), the bounded normal Schur maps satisfy

<a id="equation-gdad3"></a>

\[
 E_p^{(2)}=E_p\otimes\mathrm{id}_2.
 \tag{GDAD3}
\]

Both normal maps agree on every \(\lambda_s\pi_\beta(A)\): their values are \(p(s)\) times that generator, entry by entry. The span of these generators is an ultraweakly dense star algebra, proving(GDAD3) everywhere. Matrix amplification is positive because GDA4 proves complete positivity by its concrete positive-kernel construction.

GDA4 takes the directed supremum to construct \(T^{(2)}\) on the entire extended positive cone. With \(P_i=I\otimes E_{ii}\), [EP4's normal congruence and supremum rule](OA-FLOW-EP.md#ep-4) gives

<a id="equation-gdad4"></a>

\[
 P_iT^{(2)}(X)P_i=T(X_{ii})\otimes E_{ii}.
 \tag{GDAD4}
\]

This is first the bounded-map equality(GDAD3), then the equality of directed suprema. It applies T only to the positive diagonal entries; off-diagonal entries need not belong to its finite linear ideal.

Identify \(\pi(M)\) with \(M\) and its matrix amplification with \(M_2(M)\) through the normal coefficient isomorphisms. BC1 defines \(\chi(Y)=\varphi(Y_{11})+\psi(Y_{22})\) for bounded positive \(Y\). [EP3's increasing bounded spectral approximants](OA-FLOW-EP.md#ep-3) and [EP5's scalar extension](OA-FLOW-EP.md#ep-5) extend the same formula to every extended-positive \(Y\). Its diagonal corners are the suprema of the corresponding bounded corners. The supremum of the sum of two increasing nonnegative nets with common directed index equals the sum of their suprema, including infinity: simultaneous lower bounds use a common upper index, and the reverse inequality is immediate. Hence \(\overline\chi(Y)=\overline\varphi(Y_{11})+\overline\psi(Y_{22})\) on the entire extended cone.

Apply [GDA8's scalar composition theorem](OA-FLOW-GDA.md#gda-8) to \(\chi\), and then(GDAD4):

\[
 \widehat\chi(X)
 =\overline\chi(T^{(2)}X)
 =\overline\varphi(T(X_{11}))+\overline\psi(T(X_{22}))
 =\widehat\varphi(X_{11})+\widehat\psi(X_{22}).
\]

This proves(GDAD2) for all positive \(X\), including each possible infinite summand. It is a finite-amplification consequence of the arbitrary-group Schur construction. No abelian dual group, Plancherel averaging over that dual, unimodularity, compatible-pair reconstruction theorem or restriction to compact convolution squares is used. \(\square\)

<a id="gda-figure"></a>

## Directed kernels, exact finite transport and an infinite whole-cone value

![Directed Schur averaging, exact two-point and matrix examples, and the infinite real-group identity value](../assets/general-dual-weight-averaging/assets/general-dual-weight-averaging.png)

The first panel explains [GDA2–6](OA-FLOW-GDA.md#gda-2) for an arbitrary locally compact Hausdorff group and an arbitrary coefficient Hilbert space. The other three panels are exact examples with their stated Haar measures; their coordinates do not model an arbitrary group. The general case is developed in [Haagerup, *On the dual weights for crossed products of von Neumann algebras II*](https://journals.msp.org/mscand/article/view/1878), Math. Scand. 43 (1978). Every calculation below has a local proof.

### The directed construction and the value algebra

For a strict normal minorant of the scalar group weight, its continuous positive-definite coefficient \(p\) gives the normal completely positive Schur map
\[
F_p(X)=V_p^*(X\otimes1)V_p,\qquad
(V_p\xi)(t)=\xi(t)\otimes\rho_{t^{-1}}v,
\qquad F_p(\lambda_s)=p(s)\lambda_s.
\]
The strict family is directed in completely positive order by the explicitly proved commutant-resolvent construction in [GDA2](OA-FLOW-GDA.md#gda-2). Its entire extended supremum is [GDA23](OA-FLOW-GDA.md#gda-4), tested on every normal positive functional. On the positive rank one \(A_\xi\), [GDA24](OA-FLOW-GDA.md#gda-4) is
\[
S(A_\xi)(\omega_\eta)
=\int_G\delta(t)|\langle\xi(t),\eta(t)\rangle|^2dt.
\]
This equality includes infinite values. Invariance under every scalar multiplication unitary puts the full spectral projections in \(Q=(1\otimes L^\infty(G))'\). For \(X\) in the crossed product, the same projections are in \(R\), and [GDA5](OA-FLOW-GDA.md#gda-5) proves \(R\cap Q=\pi(M)\) by right commutant unitaries and scalar rank ones. Thus the supremum really has values in the coefficient algebra's extended positive cone. The arrows in the first panel represent these exact inclusions and tests, rather than a finite numerical approximation of the general supremum.

### A two-point rank one becomes a diagonal value

Take \(G=\mathbb Z/2\mathbb Z\), counting Haar measure, and the scalar coefficient Hilbert space \(H=\mathbb C\). Then \(\delta=1\). For \(\xi=(1,2)\),

<a id="equation-gdaf1"></a>

\[
A_\xi=\begin{pmatrix}1&2\\2&4\end{pmatrix},\qquad
S(A_\xi)=\begin{pmatrix}1&0\\0&4\end{pmatrix}.
\tag{GDAF1}
\]
Indeed the general rank-one formula is \(|\eta_0|^2+4|\eta_1|^2\). It determines exactly the displayed diagonal operator; no sampled quadratic tests are being used to infer it. Here the scalar group weight is finite, \(\Omega(1)=1\), and the strict minorants \((1-\varepsilon)\Omega\) have coefficients \((1-\varepsilon)1_{\{0\}}\). Their Schur maps are \((1-\varepsilon)\) times diagonal compression, and their supremum gives (GDAF1). Shading records the exact nonnegative entries. The matrix is rank one before averaging and rank two afterwards.

### One averaging map, two noncommuting scalar densities

Again take counting Haar measure on \(\mathbb Z/2\mathbb Z\), but now \(M=M_2(\mathbb C)\) and

<a id="equation-gdaf2"></a>

\[
v=\begin{pmatrix}0&1\\1&0\end{pmatrix},\quad
\alpha_1(a)=vav^*,\quad
d=\begin{pmatrix}1&0\\0&3\end{pmatrix},\quad
e=R d R^*=\begin{pmatrix}2&-1\\-1&2\end{pmatrix},\quad
R=2^{-1/2}\begin{pmatrix}1&-1\\1&1\end{pmatrix}.
\tag{GDAF2}
\]
Both \(\varphi(a)=\operatorname{Tr}(da)\) and \(\psi(a)=\operatorname{Tr}(ea)\) are faithful normal finite weights. They are not normalized states: each takes value \(4\) at one. The first is not action invariant, since its values on \(E_{11}\) and \(\alpha_1(E_{11})\) are \(1\) and \(3\). The second is invariant, since \(vev^*=e\). The densities do not commute: their \((1,2)\) commutator entry is \(2\).

Use the faithful regular model on \(\mathbb C^2\oplus\mathbb C^2\). Its coefficient copy is \(\pi(a)=\operatorname{diag}(a,vav^*)\), and \(\lambda_1\) swaps the two summands. For \(x(0)=I\), \(x(1)=E_{12}\), direct multiplication gives

<a id="equation-gdaf3"></a>

\[
L_x=\begin{pmatrix}I&E_{21}\\E_{12}&I\end{pmatrix},\quad
L_x^*L_x=\begin{pmatrix}\operatorname{diag}(1,2)&2E_{21}\\2E_{12}&\operatorname{diag}(2,1)\end{pmatrix},\quad
T(L_x^*L_x)=\pi(q),\quad q=\operatorname{diag}(1,2).
\tag{GDAF3}
\]
The operator on the left is positive because it is an actual square. The two diagonal blocks are exchanged by \(\alpha_1\); diagonal compression therefore gives precisely the coefficient value asserted by [GDA29](OA-FLOW-GDA.md#gda-6). The same full averaging map gives

<a id="equation-gdaf4"></a>

\[
\widehat\varphi(L_x^*L_x)=\varphi(q)=7,\qquad
\widehat\psi(L_x^*L_x)=\psi(q)=6.
\tag{GDAF4}
\]
These are exact finite sums, illustrating the full composition identity in [GDA8](OA-FLOW-GDA.md#gda-8).

For the normalized two-weight cocycle, put \(r_* = \pi/\log3\). The finite GNS graph has positive operator \(L_dR_{d^{-1}}\), so its imaginary powers give \(\sigma_r^\varphi(a)=d^{ir}ad^{-ir}\). Applying the same calculation to the balanced block density \(\operatorname{diag}(d,e)\) identifies the actual BC cocycle as \(u_r=e^{ir}d^{-ir}\). At \(r_*\), each density power \(e^{ir_*}\) and \(d^{-ir_*}\) has eigenvalues \(1,-1\). Their noncommuting product is the cocycle displayed below, whose characteristic polynomial is \(z^2+1\) and whose eigenvalues are \(+i,-i\). Hence

<a id="equation-gdaf5"></a>

\[
u_{r_*}=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\qquad
(D\widehat\psi:D\widehat\varphi)_{r_*}
=\pi(u_{r_*})=\operatorname{diag}(u_{r_*},-u_{r_*}).
\tag{GDAF5}
\]
The lower-left panel shows this exact \(4\times4\) matrix in the ordered regular basis \((e_1,e_2)\oplus(e_1,e_2)\); blue and red indicate \(1\) and \(-1\), with every zero labeled. This is a faithful regular representation of the cocycle. The weight GNS space in this example has dimension \(8\), as in GDW; the displayed \(4\times4\) matrix is not claimed to be its relative positive operator.

### A bounded identity has infinite averaging value

Take \(G=\mathbb R\), Lebesgue Haar measure, trivial scalar coefficient algebra. Its modular function is one. Put

<a id="equation-gdaf6"></a>

\[
f_\varepsilon(t)=\varepsilon^{-1}(1-|t|/\varepsilon)_+\quad(\varepsilon>0).
\tag{GDAF6}
\]
Integration over \([-\varepsilon,\varepsilon]\) gives \(\|f_\varepsilon\|_1=1\) and \(\|f_\varepsilon\|_2^2=2/(3\varepsilon)\). Thus \(\|\lambda(f_\varepsilon)\|\leq1\), and [GDA5](OA-FLOW-GDA.md#gda-1) gives

<a id="equation-gdaf7"></a>

\[
0\leq\lambda(f_\varepsilon)^*\lambda(f_\varepsilon)\leq I,\qquad
T(I)=\Omega(I)\geq\frac{2}{3\varepsilon}\quad(\varepsilon>0).
\tag{GDAF7}
\]
No finite number satisfies all these lower bounds, so \(T(I)=+\infty\) in \(\widehat{\mathbb C}_+\). This is the infinite-value part of an extended positive element; it is not a statement about Murray–von Neumann infinite projections. The plotted curve is the exact lower bound \(2/(3\varepsilon)\) for \(1/16\leq\varepsilon\leq1\). The theorem uses every \(\varepsilon>0\), not only this displayed interval. Its vertical axis is a finite lower bound for \(T(I)\), never a finite value assigned to \(T(I)\).

The native PNG is \(3600\times2600\). The illustration, exact rational matrix data, SVG and reproduction code are original expressions and are CC0-1.0 to the extent of rights held. [Editable SVG](../assets/general-dual-weight-averaging/assets/general-dual-weight-averaging.svg), [exact data](../assets/general-dual-weight-averaging/figure-data.json), [reproduction source](../assets/general-dual-weight-averaging/render_general_dual_weight_averaging.py).

<a id="gda-13"></a>

## GDA13. Discrete Haar mass and the entire bounded expectation

Suppose now that \(G\) is discrete, of arbitrary cardinality. Fix its Haar measure so that every singleton has mass \(c>0\). Let \(M\ne0\), let \(\alpha\) be a normal automorphism action, and use any faithful normal unital \(\rho:M\to B(K)\). The regular algebra \(R=M\rtimes_\alpha G\) acts on \(L^2(G,K)\) with the conventions of [NR3–4](OA-FLOW-NR.md#oa-flow.nr.3). Its coordinate inclusions are the isometries
\[
 J_r\eta=c^{-1/2}1_{\{r\}}\eta\qquad(r\in G,\ \eta\in K).
 \tag{GDA13.a}
\]
The compact coefficient formula of [GDA6](#gda-6) determines how the canonical operator-valued weight relates to coordinate compression. We prove that relationship on the entire algebra, retaining the Haar mass.

First construct the compression map independently. The finite sums of \(\lambda_s\pi_\rho(a_s)\) form a unital star algebra by covariance. Their span is ultraweakly dense in \(R\): [BD1 and BD4–5](OA-FLOW-BD.md#oa-flow.bd.1) give bounded strong-star approximants in their norm closure, and its vector-series tail estimate gives ultraweak convergence; norm approximation returns to finite polynomials. For each such polynomial,
\[
 J_e^*\left(\sum_s\lambda_s\pi_\rho(a_s)\right)J_e=\rho(a_e),
 \tag{GDA13.b}
\]
where a missing identity coefficient is zero. This follows directly from
\([\lambda_s\pi_\rho(a)\xi](t)
 =\rho(\alpha_{t^{-1}s}(a))\xi(s^{-1}t)\).

Compression is ultraweakly continuous, since each vector-series test pulls back by the coordinate inclusion. [ST2](OA-FLOW-ST12.md#oa-flow.st.2) proves that \(\rho(M)\) is ultraweakly closed and that \(\rho^{-1}\) is normal on its full image. Passing (GDA13.b) through the polynomial density therefore gives \(J_e^*XJ_e\in\rho(M)\) for every \(X\in R\). Define
\[
 E_0(X)=\pi_\rho\bigl(\rho^{-1}(J_e^*XJ_e)\bigr),
 \qquad X\in R.
 \tag{GDA13.c}
\]
This is a bounded normal map into the coefficient copy, by NR3's normal coefficient embedding and the full normal inverse just used. Compression on each finite matrix amplification proves complete positivity after transporting the coefficient representation. The two faithful coefficient embeddings are isometric, so \(\|E_0\|\le1\); its value at one gives \(\|E_0\|=1\).

The identity \(\pi_\rho(a)J_e=J_e\rho(a)\) proves
\[
 E_0(\pi_\rho(a)X\pi_\rho(b))
       =\pi_\rho(a)E_0(X)\pi_\rho(b),\qquad
 E_0(\pi_\rho(a))=\pi_\rho(a).
 \tag{GDA13.d}
\]
Thus \(E_0\) is a normal conditional expectation. Its faithfulness is also local to these coordinates. For polynomials, direct evaluation at any \(r\) gives
\[
 J_r^*XJ_r
 =\rho\!\left(\alpha_{r^{-1}}
       \bigl(\pi_\rho^{-1}(E_0(X))\bigr)\right).
 \tag{GDA13.e}
\]
Normality of all maps in this identity extends it to every \(X\in R\). If \(X\ge0\) and \(E_0(X)=0\), it gives
\(\|X^{1/2}J_r\eta\|^2=0\) for every \(r,\eta\). Finite-coordinate vectors span a dense subspace of the discrete Hilbert sum, even for uncountable \(G\). Hence \(X=0\).

Now compute the canonical weight. The compact coefficient
\(h=c^{-1}1_{\{e\}}1_M\) integrates to \(L_h=1_R\), while
\(\int h(t)^*h(t)\,dt=c^{-1}1_M\). GDA6 therefore gives
\[
 T(1)=c^{-1}1.
 \tag{GDA13.f}
\]
For every \(X\in R_+\), monotonicity implies
\[
 0\le T(X)\le c^{-1}\|X\|1.
 \tag{GDA13.g}
\]
The bounded-element criterion [EP3](OA-FLOW-EP.md#ep-3) makes each value a genuine bounded positive coefficient operator, rather than an extended value with an infinite part. Consequently the whole finite ideals of [EP6](OA-FLOW-EP.md#ep-6) satisfy \(N_T=m_T=R\). Its hereditary-cone and polarization proof gives a unique complex-linear positive bimodule extension of \(T\) on all of \(R\). The extension is bounded, using (GDA13.g) on the real and imaginary parts. It preserves bounded increasing positive suprema by the proved normality of the original weight. [NF6](OA-FLOW-NF.md#oa-flow.nf.6) then proves ultraweak continuity on the entire algebra. This is the required order-to-topology step for the bounded extension.

Set \(E_c=cT\). It is a unital normal positive bimodule map fixing the coefficient algebra. To identify it, polarize the compact-square formula of GDA6. For compact coefficients \(g,f\), linearity of the finite extension gives
\[
 T(L_g^*L_f)=\pi_\rho\left(\int g(t)^*f(t)\,dt\right).
 \tag{GDA13.h}
\]
In particular, put \(g=c^{-1}1_{\{e\}}1\) and
\(f=c^{-1}1_{\{s\}}a\). Their integrated operators are \(1\) and \(\lambda_s\pi_\rho(a)\), respectively, and the ordered integral in (GDA13.h) is
\(c^{-1}1_{\{s=e\}}a\). Thus
\[
 E_c(\lambda_s\pi_\rho(a))
 =1_{\{s=e\}}\pi_\rho(a)
 =E_0(\lambda_s\pi_\rho(a)).
 \tag{GDA13.i}
\]
Both maps are bounded and normal, so polynomial density proves equality everywhere. In particular,
\[
 \boxed{\ T(X)=c^{-1}E_0(X)\quad(X\in R_+).\ }
 \tag{GDA13.j}
\]
The equality covers every positive operator, not only finite Fourier sums or diagonal tests. The bounded linear extensions agree on all of \(R\). Complete positivity and faithfulness of \(cT\) follow from the compression proof. For a nonzero algebra, \(T\) itself is a conditional expectation if and only if \(c=1\). For the zero algebra the unique zero map has its usual zero-algebra interpretation for every Haar scale.

This is the discrete normalization relevant to Takesaki, [*Theory of Operator Algebras II*](https://doi.org/10.1007/978-3-662-10451-4), Chapter X.1, Exercise3. Counting measure gives \(c=1\); an unnormalized discrete Haar measure retains the factor in (GDA13.j).


<a id="gda-paired-coefficients"></a>

## GDA14. Paired coefficients and finite normal sandwiches

Write \(P=\pi(M)\subset R=M\rtimes_\alpha G\), and let \(T:R_+\to\widehat P_+\) be the canonical operator-valued weight constructed in GDA4–6. All groups retain the locally compact Hausdorff hypotheses of GDW, without a countability assumption. The compact coefficient algebra \(\mathscr K\), its integrated operators \(L_x\), and its involution \(x^\#\) use the conventions of [GDW1](OA-FLOW-GDW.md#gdw-1).

The square formula determines an ordered pairing on the actual finite linear domain:
\[
 L_x^*L_y\in m_T,\qquad
 T_0(L_x^*L_y)=
 \pi\left(\int_G x(t)^*y(t)\,dt\right)
 \quad(x,y\in\mathscr K).
 \tag{GDA14.a}
\]
Here \(T_0\) is the unique linear extension on \(m_T\) proved in [EP6](OA-FLOW-EP.md#ep-6). Indeed, GDA6 puts \(L_x,L_y\) in \(N_T\), and
\[
 A^*B=\frac14\sum_{k=0}^3 i^{-k}
       (A+i^kB)^*(A+i^kB).
 \tag{GDA14.b}
\]
Apply this identity to \(A=L_x,B=L_y\), use the square formula on each term, and use the same identity inside the bounded weak operator integral. This proves (GDA14.a) with the order \(x^*y\). It requires neither a bounded extension of \(T\) to all of \(R\) nor pointwise finiteness for a scalar coefficient weight.

The pairing has a concrete Hilbert-space meaning. For a faithful normal representation \(\rho:M\to B(H)\), define
\[
 V_x:H\longrightarrow L^2(G,H),\qquad
 (V_x\xi)(t)=\rho(x(t))\xi .
\]
The continuous compactly supported vector field is square integrable. Its norm identity, first tested on vectors and then polarized, gives
\[
 V_x^*V_y=\rho\left(\int_G x(t)^*y(t)\,dt\right).
 \tag{GDA14.c}
\]
In particular, for finitely many \(x_1,\ldots,x_n\), the matrix
\(\bigl[\int x_i^*x_j\bigr]_{i,j}\) is positive in \(M_n(M)\): its represented quadratic form at \((\xi_1,\ldots,\xi_n)\) is
\(\int\|\sum_j\rho(x_j(t))\xi_j\|^2dt\).
The representation is faithful, so this proves positivity in the coefficient algebra itself. The operator inequality
\(\|V_x^*V_y\|\le\|V_x\|\|V_y\|\) also gives
\[
 \left\|\int x^*y\right\|^2
 \le \left\|\int x^*x\right\|
       \left\|\int y^*y\right\|.
 \tag{GDA14.d}
\]

There is a second use of polarization in comparing scalar weights. Put
\(\Phi=\widehat\varphi\), where \(\varphi\) is faithful normal semifinite on \(M\). Suppose \(\Psi\) is another faithful normal semifinite weight on \(R\) satisfying
\[
 \Psi(L_f^*L_f)=\Phi(L_f^*L_f)<\infty
       \qquad(f\in\mathscr B_\varphi).
 \tag{GDA14.e}
\]
For \(a=L_f\), both expressions
\[
 \omega_{\Psi,a}(X)=\Psi_0(a^*Xa),\qquad
 \omega_{\Phi,a}(X)=\Phi_0(a^*Xa)
 \tag{GDA14.f}
\]
are bounded normal positive functionals on the entire algebra \(R\). For example, the first is
\(\langle\pi_\Psi(X)\Lambda_\Psi(a),\Lambda_\Psi(a)\rangle\);
its norm is \(\Psi(a^*a)\). The expression is defined because
\(a,Xa\in\mathfrak n_\Psi\), hence \(a^*Xa\in\mathfrak m_\Psi\).
The same reasoning applies to \(\Phi\).

The two functionals in (GDA14.f) agree everywhere. To see this without applying continuity to an unbounded weight, fix \(k\in\mathscr K\). The left-ideal statement in GDW1 gives
\(L_ka=L_{k*f}\in L(\mathscr B_\varphi)\).
Polarizing (GDA14.e) on the linear space \(L(\mathscr B_\varphi)\) therefore gives
\[
 \Psi_0(a^*L_ka)=\Phi_0(a^*L_ka).
\]
They agree at \(1\) as well. The compact integrated algebra is ultraweakly dense by GDW2, so normality of these two bounded functionals proves
\[
 \boxed{\ \Psi_0(a^*Xa)=\Phi_0(a^*Xa)
          \quad(X\in R,\ a\in L(\mathscr B_\varphi)).\ }
 \tag{GDA14.g}
\]

Finite normal sandwiches also give a bounded-resolvent proof of uniqueness when
\(\sigma^\Psi=\sigma^\Phi\). Use only the central-density construction of
[GDA7](#gda-7): there is a nonsingular positive central affiliated operator \(h\)
such that
\[
 \Psi(b)=\sup_n\Phi(h_n^{1/2}bh_n^{1/2}),\qquad
 h_n=\min(h,n),\qquad b\in R_+.
\]
Set \(c=(1+h)^{-1}\), a central positive contraction. The following four
operators are bounded and positive:
\[
 X_0=c^2,\qquad Y_0=c(1-c),\qquad
 X_1=c(1-c),\qquad Y_1=(1-c)^2.
 \tag{GDA14.h1}
\]
The scalar identities
\[
 t(1+t)^{-2}=(1+t)^{-1}\bigl(1-(1+t)^{-1}\bigr),
 \qquad
 t^2(1+t)^{-2}=\bigl(1-(1+t)^{-1}\bigr)^2
\]
show that \(h_nX_j\uparrow Y_j\) for \(j=0,1\). This is an identity
of bounded spectral functions followed by an increasing limit; no
product with an undefined unbounded-operator domain is used.

Fix \(a\in L(\mathscr B_\varphi)\). Centrality, the density formula and
normality of \(\Phi\) give
\[
 \begin{aligned}
 \Psi(a^*X_j a)
 &=\sup_n\Phi(a^*h_nX_j a)\\
 &=\Phi(a^*Y_j a)\qquad(j=0,1).
 \end{aligned}
 \tag{GDA14.h2}
\]
All these values are finite: \(0\le X_j,Y_j\le1\), and \(a\) lies in
both finite GNS ideals by (GDA14.e). The bounded sandwich identity
(GDA14.g), applied separately to \(X_0\) and \(X_1\), therefore yields
\[
 \Phi(a^*c^2a)=\Phi(a^*c(1-c)a)
             =\Phi(a^*(1-c)^2a).
 \tag{GDA14.h3}
\]
Apply the *bounded linear functional* \(\omega_{\Phi,a}\) to
\[
 (1-2c)^2=c^2-2c(1-c)+(1-c)^2.
\]
The finite equalities above give the positive-square identity
\[
 \boxed{\ \Phi\bigl(a^*(1-2c)^2a\bigr)=0
          \qquad(a\in L(\mathscr B_\varphi)).\ }
 \tag{GDA14.h}
\]
Faithfulness implies \((1-2c)a=0\). The space
\(L(\mathscr B_\varphi)\) contains the ultraweakly dense algebra
\(L(\mathscr D_\varphi)\) of GDW2. Multiplication by the fixed bounded
operator \(1-2c\) is ultraweakly continuous, so \(1-2c=0\).

Consequently \(c=\tfrac12\,1\). The full spectral inverse has
\(D(h)=\operatorname{ran}c\) and \(h=c^{-1}-1\) there. Thus \(D(h)\)
is the entire representation space and \(h=1\). The density formula
proves \(\Psi=\Phi\) on all of \(R_+\), including infinite values.
In particular both central projections
\(1_{[1+\varepsilon,\infty)}(h)\) and
\(1_{(0,1-\varepsilon]}(h)\) vanish for every \(0<\varepsilon<1\).
Only bounded normal functionals were linearly combined; no
continuity of an unbounded weight on an ultraweakly dense set was used.

<a id="gda-column-domains"></a>

## GDA15. Balanced coefficient columns and full finite domains

Let \(\varphi_1,\ldots,\varphi_k\) be faithful normal semifinite weights on \(M\), where \(1\le k<\infty\), and set
\[
 \chi(A)=\sum_{j=1}^k\varphi_j(A_{jj})
 \quad(A\in M_k(M)_+),\qquad
 \beta=\alpha\otimes\mathrm{id}_{M_k}.
\]
The normal crossed-product identification of GDA12 extends to this finite matrix size by the same coordinate unitary:
\[
 M_k(M)\rtimes_\beta G\ \cong\ M_k(R).
 \tag{GDA15.a}
\]
It sends the coefficient embedding to the entrywise embedding and sends each group unitary to the scalar diagonal matrix with that group unitary in every diagonal position. These statements follow by applying the defining regular operators to each of the \(k\) coordinates.

Write \(\mathscr B_j=\mathscr B_{\varphi_j}\) and
\(\mathscr D_j=\mathscr B_j\cap\mathscr B_j^\#\).
The exact compact coefficient domains for the balanced weight are
\[
 \begin{aligned}
 \mathscr K_\beta&=M_k(\mathscr K_\alpha),\\
 \mathscr B_\chi
   &=\{F=(F_{ij}): F_{ij}\in\mathscr B_j\},\\
 \mathscr D_\chi
   &=\{F: F_{ij}\in\mathscr B_j,\
                 F_{ij}^{\#}\in\mathscr B_i\text{ for every }i,j\}.
 \end{aligned}
 \tag{GDA15.b}
\]
In particular, the input weight is indexed by the **column**.

Here are the domain proofs. A finite matrix-valued function is strongly* continuous exactly when its entries are; finitely many compact supports have a compact union, and finite matrix norm bounds control the operator norm. Hence the first equality holds. Matrix convolution multiplies the entries in their stated order, and
\((F^\#)_{ij}=(F_{ji})^\#\).

By [BC1](OA-FLOW-BC.md#bc-1), a matrix \(A=(a_{ij})\) belongs to \(\mathfrak n_\chi\) exactly when \(a_{ij}\in\mathfrak n_{\varphi_j}\). Expand an elementary coefficient \(ZA\), with \(Z\in M_k(\mathscr K)\) and \(A\in\mathfrak n_\chi\):
\[
 (ZA)_{ij}(t)=\sum_{\ell=1}^k Z_{i\ell}(t)a_{\ell j}.
\]
Every term is in \(\mathscr B_j\). Conversely, each elementary term \(z(t)a\) in an \((i,j)\)-entry, with \(a\in\mathfrak n_{\varphi_j}\), factors as
\((zE_{ij})(aE_{jj})\); the second factor belongs to \(\mathfrak n_\chi\). Finite sums prove the second equality of (GDA15.b). Apply the entrywise transpose-involution to obtain the third. This reasoning uses right factors in the specified scalar finite ideals; it does not assert that \(\mathscr B_j\) is a right \(M\)-module.

The coefficient GNS map has the exact norm identity
\[
 \|\eta_\chi(F)\|^2
   =\sum_{i,j=1}^k
       \|\eta_{\varphi_j}(F_{ij})\|_{L^2(G,H_{\varphi_j})}^2
 \quad(F\in\mathscr B_\chi).
 \tag{GDA15.c}
\]
Indeed, BC1 identifies
\(H_\chi=\bigoplus_{i,j}H_{\varphi_j}\) and
\(\Lambda_\chi(A)=(\Lambda_{\varphi_j}(a_{ij}))_{i,j}\).
Applying this at each group coordinate and integrating the finite sum proves (GDA15.c), including the order of its summands.

The full balanced dual weight is
\[
 \widehat\chi(X)=
      \sum_{j=1}^k\widehat{\varphi_j}(X_{jj}),
       \qquad X\in M_k(R)_+.
 \tag{GDA15.d}
\]
To verify that this is a whole-cone identity, use the directed bounded completely positive Schur maps \(E_p\) of GDA4. At matrix size \(k\), their formulas on integrated coefficients are precisely \(E_p\otimes\mathrm{id}_{M_k}\); normality extends this equality to the whole matrix algebra. Compression to the \(j\)-th coordinate gives \(E_p(X_{jj})\). Taking the directed supremum defines the amplified extended-positive value and commutes with this compression, since both are tested by the same normal positive functionals. Evaluation by \(\chi\) is the sum of the \(k\) diagonal evaluations, by the extended-cone construction of EP3–5 and the formula for \(\chi\) on bounded positive matrices. Finite sums commute with a common directed supremum: the upper bound is immediate, and any finitely many indices have a common larger index. Now compose with the scalar weights using GDA8. This proves (GDA15.d) even when one or more summands are infinite.

Let \(n_j=\mathfrak n_{\widehat{\varphi_j}}\). Applying the balanced finite-domain theorem BC1 to (GDA15.d) gives
\[
 \begin{aligned}
 \mathfrak n_{\widehat\chi}
   &=\{A=(a_{ij})\in M_k(R):a_{ij}\in n_j\},\\
 \mathfrak n_{\widehat\chi}\cap\mathfrak n_{\widehat\chi}^{\,*}
   &=\{A:a_{ij}\in n_j\cap n_i^*\},\\
 \mathfrak m_{\widehat\chi}
   &=\{A:a_{ij}\in\operatorname{span}(n_i^*n_j)\}.
 \end{aligned}
 \tag{GDA15.e}
\]
For the last equality, an entry of \(B^*C\) is a finite sum
\(\sum_\ell b_{\ell i}^*c_{\ell j}\). Conversely each product \(b^*c\) in the \((i,j)\)-entry is obtained from matrices supported in positions \((1,i)\) and \((1,j)\), respectively. This proves both inclusions and the claimed whole finite linear domain.

The full GNS space is therefore
\(\bigoplus_{i,j}L^2(G,H_{\varphi_j})\), with
\[
 \Lambda_{\widehat\chi}(A)
   =(\Lambda_{\widehat{\varphi_j}}(a_{ij}))_{i,j}.
 \tag{GDA15.f}
\]
The compact domain (GDA15.b) embeds in these full domains through \(F\mapsto L_F=(L_{F_{ij}})\). Formula (GDA15.e) is not restricted to compact coefficients. On the full finite-star domain the involution interchanges \((i,j)\) and \((j,i)\) and takes adjoints; [BC2](OA-FLOW-BC.md#bc-2) closes this operator with its full adjoint and relative spectral domains.

<a id="gda-haar-rescaling"></a>

## GDA16. Haar rescaling on the entire extended cone

Fix \(c>0\), and compare Haar measures \(\mu\) and \(\nu=c\mu\) for the same action. The unitary
\[
 U_c:L^2(G,\nu;H)\longrightarrow L^2(G,\mu;H),
       \qquad U_c\xi=c^{1/2}\xi
 \tag{GDA16.a}
\]
intertwines both the coefficient representations and the regular group unitaries. We identify the crossed products through it. Their modular functions are the same, whereas integration gives
\[
 L_x^\nu=cL_x^\mu,\qquad
 \int x^*x\,d\nu=c\int x^*x\,d\mu .
 \tag{GDA16.b}
\]
The coefficient spaces \(\mathscr K,\mathscr B_\varphi,\mathscr D_\varphi\) themselves do not change: scaling convolution by \(c\) does not change their underlying linear spaces, and the coefficient involution depends only on the unchanged modular function and action.

For every faithful normal semifinite coefficient weight \(\varphi\),
\[
 \boxed{\ \widehat\varphi_\nu
                  =c^{-1}\widehat\varphi_\mu
                  \quad\hbox{on }R_+.\ }
 \tag{GDA16.c}
\]
To prove the whole-cone assertion, put
\(\Psi=c^{-1}\widehat\varphi_\mu\).
The scalar-weight calculation [BC5](OA-FLOW-BC.md#bc-5) gives
\(\sigma^\Psi=\sigma^{\widehat\varphi_\mu}\). GDW's two modular generator formulas are independent of the Haar scale, so this is also the modular group of \(\widehat\varphi_\nu\). For each \(x\in\mathscr B_\varphi\),
\[
 \begin{aligned}
 \Psi((L_x^\nu)^*L_x^\nu)
  &=c^{-1}\widehat\varphi_\mu(c^2(L_x^\mu)^*L_x^\mu)\\
  &=c\int_G\varphi(x(t)^*x(t))\,d\mu(t)\\
  &=\int_G\varphi(x(t)^*x(t))\,d\nu(t)
   =\widehat\varphi_\nu((L_x^\nu)^*L_x^\nu).
 \end{aligned}
 \tag{GDA16.d}
\]
These values are finite. The full uniqueness criterion GDA7, with the dense GNS domain constructed for \(\nu\), proves (GDA16.c). Thus the equality includes positive elements of infinite weight.

The canonical maps satisfy the corresponding extended-valued identity
\[
 \boxed{\ T_\nu(X)=c^{-1}T_\mu(X)
            \quad(X\in R_+).\ }
 \tag{GDA16.e}
\]
For a nonzero coefficient algebra, choose one faithful normal semifinite weight \(\varphi\), whose existence was proved in GDA10. By GDA8 and (GDA16.c), \(T_\nu\) and \(c^{-1}T_\mu\) have the same composition with \(\varphi\) on the whole cone. The uniqueness theorem [GDA10](#gda-10) therefore proves (GDA16.e). Multiplication by the finite positive scalar \(c^{-1}\) preserves normality, semifiniteness and faithfulness; it multiplies every normal-functional test of an extended value and retains its infinite part. The zero algebra satisfies the equality directly.

Consequently \(N_{T_\nu}=N_{T_\mu}\) and \(m_{T_\nu}=m_{T_\mu}\), and their finite linear extensions obey
\((T_\nu)_0=c^{-1}(T_\mu)_0\).
For any normal coefficient weight \(\theta\), including a nonfaithful or nonsemifinite one, GDA8's definition by scalar composition gives
\(\widehat\theta_\nu=c^{-1}\widehat\theta_\mu\) with the same finite and null ideals.

There are two useful Hilbert-space normalization formulas. For a fixed operator \(X\) in the common scalar finite left ideal, the unitary between weight GNS spaces is
\[
 W_c\Lambda_{\widehat\varphi_\nu}(X)
       =c^{-1/2}\Lambda_{\widehat\varphi_\mu}(X).
 \tag{GDA16.f}
\]
Its isometry follows from (GDA16.c); the common finite ideal makes its range dense, hence onto. At the integrated coefficient \(X=L_x^\nu=cL_x^\mu\), the right side becomes
\(c^{1/2}\eta_{\varphi,\mu}(x)\).
Under the GDW GNS identifications this is exactly \(U_c\eta_{\varphi,\nu}(x)\). The inverse factor in (GDA16.f) is attached to a fixed operator \(X\); the factor in (GDA16.a) compares the same coefficient function.

Finally, these identifications preserve full operator domains. Both weights have the same finite-star algebra. On it,
\[
 W_cS_{\nu,0}\Lambda_\nu(X)
   =c^{-1/2}\Lambda_\mu(X^*)
   =S_{\mu,0}W_c\Lambda_\nu(X),
\]
where the scalar is real and positive. Taking graph closures gives
\(W_cS_\nu W_c^*=S_\mu\); taking adjoints and positive products gives the corresponding identity for \(\Delta_\nu\) and \(\Delta_\mu\). Unitary transport of their spectral resolutions identifies the domains of every Borel function, including unbounded powers, by the spectral integral criterion in SF. For two coefficient weights, both dual weights are multiplied by the same \(c^{-1}\). BC5 and the chain rule cancel these scalar factors in their normalized relative cocycle. Equivalently, apply the preceding graph argument to their balanced matrix weight and then take the corners described by BC2.

<a id="gda-nondiscrete-identity"></a>

## GDA17. Nondiscrete groups and the infinite identity value

Assume \(M\ne0\). For every nondiscrete locally compact Hausdorff group \(G\),
\[
 \boxed{\ T(1_R)=\infty\,1_P.\ }
 \tag{GDA17.a}
\]
The right side is the extended-positive element that is infinite on every nonzero normal positive functional and zero at the zero functional.

We first justify the required Haar functions in full generality. If a Haar measure had \(\mu(\{e\})>0\), any compact identity neighborhood \(C\) would contain at most \(\mu(C)/\mu(\{e\})\) distinct points: apply finite additivity to arbitrary finite subsets of \(C\). Hence \(C\) would be finite. An open identity neighborhood contained in \(C\), after removing its finitely many other points using the Hausdorff property, would make \(\{e\}\) open. The group would be discrete. Therefore a nondiscrete group has \(\mu(\{e\})=0\).

Fix \(A>0\). Outer regularity at the singleton and local compactness provide a relatively compact open identity neighborhood \(V\) with
\(0<\mu(V)<A^{-1}\).
The strict positivity follows from the full support of Haar measure proved in [HR6](OA-FLOW-HR.md#hr-06). The compact cutoff construction [H0](OA-FLOW-TOPOLOGY.md#l138-h0) supplies a nonzero \(h\in C_c(G)\) with \(h\ge0\) and \(\operatorname{supp}h\subset V\). Normalize
\(f=h/\int h\,d\mu\). Then
\[
 \|f\|_1=1,\qquad
 1=\left|\int_V f\,d\mu\right|^2
       \le\mu(V)\|f\|_2^2,\qquad
 \|f\|_2^2>A.
 \tag{GDA17.b}
\]
The compact coefficient \(x(t)=f(t)1_M\) is in \(\mathscr K\). Its integrated operator is \(\lambda(f)\), a contraction by the [integrated representation estimate](OA-FLOW-L24.md#oa-flow.grp.vectorintegration). Hence GDA6 and monotonicity give
\[
 T(1_R)\ \ge\ T(\lambda(f)^*\lambda(f))
          =\|f\|_2^2\,1_P>A1_P .
 \tag{GDA17.c}
\]
For any nonzero \(\omega\in P_*^+\), \(\omega(1)>0\). Let \(A\) increase in (GDA17.c) to obtain \(T(1)(\omega)=\infty\). Extended-positive elements are determined by all these functional tests, so (GDA17.a) follows. This proof uses neither a faithful state nor a countable neighborhood basis.

Bimodularity now determines the canonical value on every positive coefficient:
\[
 T(\pi(a))=\infty\,s(\pi(a))
       \quad(a\in M_+),
 \tag{GDA17.d}
\]
where \(s(b)=1_{(0,\infty)}(b)\) is the support projection. In fact,
\(T(\pi(a))=\pi(a)^{1/2}T(1)\pi(a)^{1/2}\);
its value at \(\omega\) is infinite exactly when \(\omega(\pi(a))>0\).
This is equivalent to \(\omega(s(\pi(a)))>0\): one direction uses
\(\pi(a)\le\|a\|s(\pi(a))\); the other uses the increasing spectral projections \(1_{[1/n,\infty)}(\pi(a))\), each bounded above by \(n\pi(a)\), and normality of \(\omega\).
At \(a=0\), both sides of (GDA17.d) are zero.

It follows that
\[
 N_T\cap P=\{0\}
 \quad\hbox{when }G\hbox{ is nondiscrete}.
 \tag{GDA17.e}
\]
Indeed, a nonzero \(b\in P\) has \(b^*b\ne0\), whose value in (GDA17.d) has a nonzero infinite part and is not a bounded element of \(P\). This coexists with the ultraweak density of \(N_T\) established in GDA6. A dense finite left ideal need not contain a nonzero element of the coefficient subalgebra.

Together with GDA13, this proves that the canonical operator-valued weight is bounded exactly when \(G\) is discrete. For singleton Haar mass \(c\), its bounded linear extension is \(c^{-1}E_0\) and has norm \(c^{-1}\). It is a conditional expectation precisely for counting normalization \(c=1\).

The assertion concerns the canonical map; a different conditional expectation can exist. For a complete example, take the scalar coefficient algebra, the circle group with probability Haar measure, and the trivial action. The characters \(z\mapsto z^n\), \(n\in\mathbb Z\), form an orthonormal basis of \(L^2(\mathbb T)\). Here is the completeness argument. Haar invariance gives \(\int z^n dz=0\) for \(n\ne0\), by rotating by a point whose \(n\)-th power is not one. This proves orthogonality. The nonnegative trigonometric polynomials
\[
 K_N(z)=\frac1{N+1}\left|\sum_{j=0}^Nz^j\right|^2
\]
have integral one. On any closed set not containing \(1\), the geometric sum formula bounds \(K_N(z)\) by \(4/((N+1)|1-z|^2)\), so their mass there tends to zero. For a continuous function \(g\), split the convolution integral for \(K_N*g-g\) between a small identity neighborhood and its complement. Uniform continuity makes the first contribution arbitrarily small; the displayed bound makes the second tend to zero. Thus \(K_N*g\to g\) uniformly. Each convolution is a finite linear combination of characters, by expanding \(K_N\) and applying Haar substitution. Continuous functions are dense in \(L^2\) by [HR3](OA-FLOW-HR.md#hr-03), proving completeness. In these coordinates,
\(R=\operatorname{VN}(\mathbb T)\cong\ell^\infty(\mathbb Z)\):
translations are diagonal, and integrating the character \(z^n\) against the translation operators gives the projection \(p_n\) onto the \(n\)-th Fourier coordinate. These coordinate projections generate the entire diagonal algebra by bounded strong sums.

Each integrated character has squared \(L^2\)-norm one, so GDA6 gives \(T(p_n)=1\). Normality, applied to the increasing finite-coordinate truncations of any \(a=(a_n)\in\ell^\infty(\mathbb Z)_+\), gives
\[
 T(a)=\sum_{n\in\mathbb Z}a_n .
 \tag{GDA17.f}
\]
This includes infinite sums. On the same algebra put
\[
 w_n=\frac13\,2^{-|n|},\qquad
 E_w(a)=\left(\sum_{n\in\mathbb Z}w_na_n\right)1 .
 \tag{GDA17.g}
\]
The weights are strictly positive and sum to
\((1+2\sum_{n\ge1}2^{-n})/3=1\).
Thus the series defines a positive unital contraction onto the scalars. It is a scalar bimodule map and fixes the scalars. It is normal: for an increasing bounded positive net, finite sums commute with its supremum, and the supremum over finite subsets then gives the whole weighted series. It is faithful because every coordinate has a strictly positive weight.

For the finite projection \(p_{[-N,N]}=\sum_{n=-N}^Np_n\), \(N\ge0\), the two exact values are
\[
 T(p_{[-N,N]})=2N+1,\qquad
 E_w(p_{[-N,N]})
     =\left(1-\frac23\,2^{-N}\right)1 .
 \tag{GDA17.h}
\]
The canonical values increase without bound, whereas the conditional-expectation values increase to \(1\). Both formulas concern the same projections in the same algebra.
