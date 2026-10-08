# Integral representations for arbitrary distributions

*Original proof exposition by GPT-6.1 Sol (OpenAI), Ultra, October 2026. CC0 1.0.*

We solve both unnumbered exercises on printed page 300 of Hörmander's Chapter 15. The first extends the characteristic-surface formula to every distributional homogeneous solution. The second represents every distribution by an integral over the whole complex frequency space. Orders may increase without bound over a compact exhaustion. No single global moderate Sobolev weight is imposed on the distribution.

Use complex-linear distribution pairings, \(D=-i\partial\), \(F_v(z)=\int v(x)e^{-ix\cdot z}\,dx\), and Euclidean volume \(dV\) on \(\mathbb C^n\). Let \(X\subset\mathbb R^n\) be open and convex. Fix nonempty compact convex sets \(K_j\subset\operatorname{int}K_{j+1}\), exhausting \(X\); write \(K_0=\varnothing\) without using its support function.

Our full lower inputs are [L153 TP1–TP7](../../AN02-L153.html#tp1-the-four-exact-neighborhood-descriptions), including the exact logarithmic contour and compatible strict weights; [L152 SR2–SR6](../../AN02-L152.html#sr2-an-exact-algebraic-area-bound), including algebraic area, anisotropic cover, all multiplicity jets and the complete weighted local-remainder repair; [L150 NV2 and NV4](../../AN02-L150.html#nv4-a-strict-estimate-for-a-nonsmooth-weight), for polynomial strength and the actual nonsmooth weighted solution; [L122 CF2–CF4](../../AN02-L122.html#complete-formal-proof-compact-fourier-division-and-multiplicity-sensitive-annihilators), for compact carriers and entire division; and [L043](../../AN02-L043.html#a-representing-vector-in-hilbert-space), for the full complex Hilbert representation. The new approximation argument below does not assume weighted-norm density of smooth compact transforms.

## AR1. A whole-space formula for every distribution

**Theorem AR1.** For every \(u\in\mathcal D'(X)\) there are a finite real locally Lipschitz PSH weight \(\phi\) and a measurable \(U\) on \(\mathbb C^n\) such that
\[
\begin{aligned}
e^{-\phi(z)}&\le C_K(1+|z|)^{N_K}e^{-H_K(\operatorname{Im}z)}
&& (K\Subset X\text{ compact convex}),\\
|\nabla\phi(z)|&\le C_0+\log(1+|\operatorname{Im}z|)
&&\text{almost everywhere},\\
\mathcal L_\phi(w)&\ge c(1+|\operatorname{Im}z|^2)^{-3/4}|w|^2
&&\text{distributionally},\quad c>0,
\end{aligned}
\tag{AR1}
\]
and
\[
\int_{\mathbb C^n}|U(z)|^2e^{2\phi(-z)}\,dV(z)<\infty,\qquad
u(v)=\int_{\mathbb C^n}U(z)F_v(-z)\,dV(z)
\quad(v\in\mathcal D(X)).
\tag{AR2}
\]
Every tested integral is absolutely convergent. This is a weak formula for \(u(x)=\int U(z)e^{ix\cdot z}\,dV(z)\), with no pointwise assertion.

The convex balanced set \(V=\{v:|u(v)|<1\}\) is a zero-neighborhood by distributional continuity. L153 TP5 supplies \(\phi\) satisfying AR1 and containing its weighted unit ball in \(V\). Set
\[
q_\phi(v)=\left(\int|F_v(z)|^2e^{-2\phi(z)}\,dV(z)\right)^{1/2}.
\tag{AR3}
\]
This is finite and continuous on each compact smooth support stage: if the support lies in \(K\), the full entire integration-by-parts estimate of TP11 bounds the integrand by a finite derivative seminorm squared times \((1+|z|)^{-2(L-N_K)}\); choose \(L>N_K+n\). Hence it is a continuous inductive-topology seminorm. If \(q_\phi(v)=0\), Fourier inversion gives \(v=0\). For \(q_\phi(v)>0\), apply the unit-ball implication to \(tv/q_\phi(v)\), \(0<t<1\), then let \(t\uparrow1\). This proves
\[
|u(v)|\le q_\phi(v).
\tag{AR4}
\]

Map \(v\) isometrically to \(F_v\) in \(L^2(e^{-2\phi}dV)\). AR4 defines a bounded complex-linear functional on its range, and then on the closure by continuity. The full Hilbert theorem gives a vector \(g\) in that closure, with inner product linear in its first argument, such that
\[
u(v)=\int F_v(s)\overline{g(s)}e^{-2\phi(s)}\,dV(s).
\tag{AR5}
\]
Put \(U(z)=\overline{g(-z)}e^{-2\phi(-z)}\). Reflection preserves real \(2n\)-volume. Substitution in AR5 gives AR2, and its weighted squared norm is exactly \(\|g\|^2\). Cauchy–Schwarz gives the absolute tested integral. Conversely any \(U\) satisfying that norm condition defines a distribution, because its pairing is bounded by its norm times the stage-continuous AR3. Thus the formula has the asserted distributional meaning. It covers the second page-300 exercise.

## AR2. Finite envelopes that survive physical smoothing

The surface proof needs a stronger consequence than AR4. Its repaired entire transforms initially have compact distribution carriers. They need not be smooth compact transforms, so neither a pairing of two distributions nor weighted-norm convergence of a mollifier can be assumed.

**Lemma AR2.** Given \(u\in\mathcal D'(X)\), there are increasing finite strict weights \(\phi_J\), with a common gradient and Levi bound as in AR1, increasing to a weight \(\phi\) satisfying AR1, with this property: whenever an entire \(F\) has
\[
N^2=\int|F(z)|^2e^{-2\phi_J(z)}\,dV(z)<\infty,
\tag{AR6}
\]
it is the transform of a continuous compactly supported function \(f\), with carrier in \(K_{J+1}\). For a fixed normalized smooth mollifier \(\rho_\epsilon\), whose support shrinks to zero, all sufficiently small \(\epsilon>0\) have support in \(X\) and satisfy
\[
|u(f*\rho_\epsilon)|\le N.
\tag{AR7}
\]
The threshold for \(\epsilon\) can depend on \(F,J\). The constant in AR7 is one, uniformly in \(J\). No limit of \(u(f*\rho_\epsilon)\) is claimed for an arbitrary \(F\).

Here is a full construction and proof. From L153 TP1, obtain derivative orders \(L_j\) and thresholds \(\delta_j>0\) such that every smooth compact \(v\) satisfying the entire-exterior conditions
\[
|D^\alpha v(x)|\le\delta_j
\quad(x\in X\setminus K_j,\ |\alpha|\le L_j,\ j\ge0)
\tag{AR8}
\]
belongs to \(V=\{|u(v)|<1\}\). Increase orders to integers
\[
A_j=\max_{0\le l\le j+1}L_l,\qquad \epsilon_j=\delta_j/8.
\tag{AR9}
\]
We construct a Fourier envelope enforcing order \(A_j\) and bound \(\epsilon_j\) on \(X\setminus K_j\), with a margin for small neighborhoods of its points.

For \(j\ge2\), let \(c_j=\operatorname{dist}(K_{j-1},\mathbb R^n\setminus\operatorname{int}K_j)>0\). At any \(x\notin K_j\), the nearest-point separating unit vector \(\eta\) of TP19 satisfies \(x\cdot\eta-H_{K_{j-1}}(\eta)\ge c_j\). On a sufficiently small neighborhood \(O_x\) of \(x\), the gap is at least \(c_j/2\). Use this half-gap in all successive choices below.

At step \(k\), earlier \(d_l,M_l\) are fixed. For \(k\ge2\), choose \(R_k\) large enough that the sum, over \(l<k\), of
\[
C\,d_l(1+R_k)^{p_{kl}+1}
\int_{\mathbb R^n}(1+|\xi|)^{p_{kl}}
 (2+|\xi|^2)^{-R_kc_k/2}\,d\xi
<\epsilon_k/2,\quad p_{kl}=\max(A_k-M_l,0).
\tag{AR10}
\]
Each term tends to zero: split its last negative power in half, use one half for an integrable polynomial bound and the other for \(2^{-R_kc_k/4}\); that exponential beats every fixed power of \(R_k\). This also proves finiteness at the chosen sufficiently large \(R_k\).

For \(2\le j\le k\), define
\[
b_{jk}=\max\left(0,\sup_{|\eta|=1}
 [H_{K_k}(\eta)-H_{K_{j-1}}(\eta)-c_j/2]\right).
\tag{AR11}
\]
Choose increasing positive integers \(M_k\) such that \(M_k\ge A_0+n+2,A_1+n+2\), and
\[
M_k\ge A_j+2R_jb_{jk}+n+2\quad(2\le j\le k).
\tag{AR12}
\]
Choose \(d_k>0\) so small that
\[
C_{jk}d_k\le2^{-k-2}\epsilon_j\quad(0\le j\le k),
\qquad d_k\le2^{-k}e^{-k(1+r_{K_k})}.
\tag{AR13}
\]
Here \(C_{0k}=C_{1k}=(2\pi)^{-n}\int(1+|\xi|)^{-n-1}d\xi\), and for \(j\ge2\) use
\(C_{jk}=(2\pi)^{-n}(1+R_j)2^{R_jb_{jk}}\int(1+|\xi|)^{-n-1}d\xi\).
The extra power in AR12 is harmless. Every step imposes finitely many conditions. The last AR13 bound gives local uniform convergence of
\[
B(z)=\sum_{k\ge1}d_k(1+|z|)^{-M_k}e^{H_{K_k}(\operatorname{Im}z)}.
\tag{AR14}
\]

Apply the actual L153 TP6–TP7 seed construction to these particular \(M_k,d_k\): set \(a_l=(M_{l+1}+1)/2\), enlarge \(t_l\) so that \(\sqrt{t_l}\ge32a_l\), the uniform active-region gradient bound holds and \(t_l^{-1/2}\) fits the \(K_l\)-to-\(K_{l+1}\) support gap. Put
\[
\psi_l=H_{K_l}(\eta)-a_l\log(t_l^2+|z|^2)
+p_{t_l}(\eta),\qquad
p_t(\eta)=\frac{\sqrt{t^2+|\eta|^2}}{\sqrt t}
 -(t^2+|\eta|^2)^{1/4}.
\tag{AR15}
\]
Choose \(G_l\) by TP33–TP34, including inactivity of each later branch on an increasing whole strip \(|\eta|\le B_l\). Thus
\[
\phi_J=\max_{1\le l\le J}(\psi_l-G_l),\qquad
\phi=\lim_J\phi_J,
\tag{AR16}
\]
have the common strict Levi lower bound and gradient bound. Every fixed strip stabilizes; the final weight is finite, locally a finite maximum and satisfies AR1. The exact pointwise TP33 is
\[
C_{\rm mean}e^{C_0}(2+|z|)e^{\psi_l-G_l}
\le d_{l+1}(1+|z|)^{-M_{l+1}}e^{H_{K_{l+1}}(\eta)},
\quad C_{\rm mean}=(n!/\pi^n)^{1/2}.
\tag{AR17}
\]
The unit-ball submean estimate and common gradient bound therefore turn AR6 into the finite envelope
\[
|F(z)|\le N\sum_{k=2}^{J+1}
 d_k(1+|z|)^{-M_k}e^{H_{K_k}(\eta)}.
\tag{AR18}
\]
All constants here are independent of \(J\).

For the following argument normalize \(N=1\); \(N=0\) gives \(F=0\). On the real plane AR12 gives integrability of \(\xi^\alpha F(\xi)\) up to orders \(A_0,A_1\). Define \(f\) by the real inverse Fourier integral. Differentiation under its integrable majorants makes \(f\) globally \(C^{\max(A_0,A_1)}\). AR13 bounds those derivatives by \(\epsilon_0,\epsilon_1\), respectively. Also AR18 implies a polynomial-exponential bound with carrier \(K_{J+1}\), so the full compact Fourier support theorem identifies this function with the inverse compact distribution supported there.

We must justify higher exterior derivatives without assuming that their real Fourier integrals converge. Fix \(j\ge2\), \(x\notin K_j\), its separating \(\eta\), and the neighborhood \(O_x\) with half-gap. On the logarithmic contour
\[
z_s(\xi)=\xi+i sR_j\eta\log(2+|\xi|^2),\qquad
J_s=1+i sR_j\eta\cdot\nabla_\xi\log(2+|\xi|^2),
\tag{AR19}
\]
the finite envelope bounds every derivative kernel \(z_1^\alpha F(z_1)e^{iy\cdot z_1}J_1\), \(|\alpha|\le A_j,\ y\in O_x\), by an integrable majorant. For earlier \(k<j\), nesting and the half-gap give exactly AR10. For later \(k\ge j\), AR11–AR12 give \(C_{jk}d_k(1+|\xi|)^{-n-1}\), up to the displayed fixed normalization. The earlier sum is below \(\epsilon_j/2\); the later sum is at most \(\epsilon_j\sum_{k\ge j}2^{-k-2}<\epsilon_j/2\). Truncating the sum at \(J+1\) only decreases these bounds.

Define on \(O_x\) the contour integral with \(\alpha=0\). Its derivatives through \(A_j\) are legitimate by these common majorants. To identify it with \(f\), first test against \(\chi\in C_c^\infty(O_x)\). The entire product \(F(z)F_\chi(-z)\) has, along every intermediate contour, arbitrary real-frequency decay supplied by \(F_\chi\). In detail AR18 is a finite sum with carrier \(K_{J+1}\), whereas TP11 for \(\chi\) has any desired power \(-L\). Along AR19 its exponential factors are at most \((2+|\xi|^2)^{R_j(r_{K_{J+1}}+r_{\operatorname{supp}\chi})}\). Choose \(L\) larger than this doubled exponent, the finite polynomial order and \(n+2\). The exact TP14 divergence identity, integrated on \([-T,T]^n\), then has boundary bounded by a constant times \(T^{n-1}\log(2+nT^2)\) times a power less than \(-n-1\), tending to zero. Its cube integrals have a uniform integrable majorant in \(s\). Thus the real tested integral equals the tested contour integral. Fubini at the final contour is valid by the majorant already proved on \(\operatorname{supp}\chi\).

It follows that the contour function equals \(f\) as a distribution on \(O_x\), and hence as a continuous function. Therefore \(f\) is \(C^{A_j}\) there and
\[
|D^\alpha f(y)|\le\epsilon_j
\quad(y\in X\setminus K_j,\ |\alpha|\le A_j).
\tag{AR20}
\]
This holds on the entire exterior, including all its boundary-near points by their own separating neighborhoods. It establishes the additional local regularity needed for smoothing; it did not insert a divergent high-order real-plane integral.

For each \(j\ge3\), the points of \(X\setminus K_j\), and their boundary limits inside \(X\), are separated from \(K_{j-1}\). On a neighborhood of them within any fixed bounded region, the preceding result gives \(C^{A_{j-1}}\) regularity, with \(A_{j-1}\ge L_j\). The cases \(j=0,1,2\) follow from the global regularity \(A_0,A_1\). Convolution therefore converges uniformly in all derivatives through \(L_j\) on \(X\setminus K_j\): only a fixed bounded neighborhood of the compact carrier matters, and uniform continuity of these derivatives on that compact neighborhood proves convergence by the usual normalized-mollifier integral.

Choose the mollifier radius small enough that its carrier is compact inside \(K_{J+2}\). For \(j\ge J+2\), all exterior derivatives of the mollified function are zero. For the finitely many smaller \(j\), AR20 and uniform convergence make them at most \(\delta_j/4<\delta_j\), after shrinking the radius further. Hence \(f*\rho_\epsilon\) satisfies AR8 and lies in \(V\), so \(|u(f*\rho_\epsilon)|<1\). Rescaling proves AR7. This completes the lemma. In particular it proves the needed physical smoothing consequence without asserting convergence in the weighted entire-transform norm.

## AR3. The full characteristic-surface formula

**Theorem AR3.** Let \(u\in\mathcal D'(X)\) satisfy \(P(D)u=0\). For nonconstant \(P\), write
\[
P=c_P\prod_{\ell=1}^sP_\ell^{m_\ell},\qquad
m=\deg P,\quad P_m(\tau)\ne0,\quad \tau\in\mathbb C^n,
\qquad N_\ell=\{P_\ell=0\}.
\tag{AR21}
\]
The factors are distinct irreducible nonconstant polynomials. Use the exact Euclidean real \(2n-2\) surface measure on the regular reduced graph loci, extended by zero to the other points; in dimension one it is counting measure. There are a weight satisfying AR1 and measurable densities \(U_\ell^a\), \(0\le a<m_\ell\), for which, with \(W=1+|z|^2\),
\[
\sum_{\ell,a<m_\ell}\int_{N_\ell}
 |U_\ell^a(z)|^2 e^{2\phi(-z)}W(z)^{-K}\,dS_\ell(z)<\infty,
\tag{AR22}
\]
and
\[
u(x)=\sum_{\ell,a<m_\ell}(x\cdot\tau)^a
 \int_{N_\ell}U_\ell^a(z)e^{ix\cdot z}\,dS_\ell(z)
\quad\text{in }\mathcal D'(X).
\tag{AR23}
\]
Every tested integral is absolutely convergent. One admissible exponent is the full L152 exponent
\[
E=m^4+m^2(2m-1)(m-1)+(m-1)(2n-2),\qquad K=E+2m+2.
\tag{AR24}
\]
The assertion is an actual surface formula, with every multiplicity jet retained.

Apply Lemma AR2 to this particular distribution \(u\). Let \(e=\tau/|\tau|\), \(\mathcal Q(z)=cP(-z)\) as normalized by the unitary direction change in L152, and use its actual local division/partition construction for \(F=F_v\), \(v\in\mathcal D(X)\). It produces smooth locally finite \(H,G\) and closed data \(b=-\bar\partial G\), satisfying \(F=H+\mathcal QG\). All geometric estimates SR7–SR25 are independent of the distribution and its weight.

The common three weight conditions suffice for the complete weighted estimates SR28–SR37. To be explicit, the positive polynomial strength
\(\mathcal J^2=\sum_{|\gamma|\le m}|\partial^\gamma\mathcal Q|^2(T_0^2+|\eta|^2)^{|\gamma|}\)
satisfies \(|\mathcal Q|\le\mathcal J\), \(\mathcal J^2\le C W^m\), and a Levi error bounded by \(B/(T_0^2+|\eta|^2)\). Choose \(T_0\) once so that this error is at most half the common \(c(1+|\eta|^2)^{-3/4}\). Then \(2(\phi_J-\log\mathcal J)\) is an actual finite continuous PSH weight with uniform strict curvature.

The local remainder bound contributes \(W^E\), squared cutoffs \(W^{m-1}\), strength \(W^m\), inverse curvature at most \(W\), and a weight comparison over distance two contributes \(W^2\). The uniformly bounded overlap therefore gives exactly
\[
\begin{aligned}
\int |H|^2e^{-2\phi_J}dV
 +\int|b|^2\mathcal J^2e^{-2\phi_J}(1+|\eta|^2)^{3/4}dV
 &\le C\,\mathcal A_J(F),\\
\mathcal A_J(F)&=\sum_{\ell,a<m_\ell}
 \int_{-N_\ell}|\partial_e^aF(z)|^2e^{-2\phi_J(z)}W(z)^K\,dS_\ell(z).
\end{aligned}
\tag{AR25}
\]
The constant is uniform in \(J\). These are the fully proved L152 summation estimates, applied with the weights of AR16; no fixed \(k\) estimate is used.

For all sufficiently large \(J\), \(\mathcal A_J(F_v)<\infty\). Indeed the support of each \((x\cdot e)^av\) lies in a compact \(S\) with \(S+\rho\overline B\subset K_J\). The lower seed bound gives \(e^{-\phi_J}\le C_J(1+|z|)^{M_{J+1}+1}e^{-H_{K_J}(\eta)}\). TP11 gives arbitrary whole-complex polynomial decay for each jet, times \(e^{H_S(\eta)}\); the support gap leaves \(e^{-\rho|\eta|}\). Choose the real-frequency decay power larger than all fixed losses and \(2n+2\). The proved algebraic area bound is uniform on ordinary unit balls. Summing their integrand suprema over lattice cubes therefore proves surface integrability. This verifies the prerequisite of the weighted solution estimate.

L150 NV4 now gives \(\bar\partial w_J=b\) and \(\int|w_J|^2\mathcal J^2e^{-2\phi_J}\le C\mathcal A_J(F)\). Set
\[
V_{1,J}=H-\mathcal Qw_J,\qquad
V_{2,J}=\mathcal Q(G+w_J),\qquad
F=V_{1,J}+V_{2,J},\qquad
\int|V_{1,J}|^2e^{-2\phi_J}\le C\mathcal A_J(F).
\tag{AR26}
\]
The distributional Cauchy–Riemann equations and harmonic smoothing proved in the lower inputs make these actual entire functions, with entire quotient \(G+w_J\).

Lemma AR2 identifies \(V_{1,J}\) with a compact continuous function \(v_{1,J}\), supported in \(K_{J+1}\), and gives the small-radius bound AR7 with \(N_J=\|V_{1,J}\|_{L^2(e^{-2\phi_J})}\). The difference \(v_{2,J}=v-v_{1,J}\) is a compact distribution in the same carrier, whose transform is divisible by \(\mathcal Q=cP(-z)\). The full compact entire-division theorem supplies \(a_J\), also with that convex carrier, such that \(v_{2,J}=cP(-D)a_J\).

For all sufficiently small mollifier radii, every carrier remains compact in \(X\), and
\[
u(v*\rho_\epsilon)
 =u(v_{1,J}*\rho_\epsilon)
   +c\,u(P(-D)(a_J*\rho_\epsilon))
 =u(v_{1,J}*\rho_\epsilon).
\tag{AR27}
\]
The last term vanishes by the distributional equation, tested against the smooth compact function \(a_J*\rho_\epsilon\). Since \(v*\rho_\epsilon\to v\) in its smooth compact support stage, AR7 and AR26 yield
\[
|u(v)|^2\le N_J^2\le C\mathcal A_J(F_v).
\tag{AR28}
\]
This is the needed bound with a constant independent of \(J\). We never tested \(u\) against the rough compact inverse \(a_J\) or assumed the existence of such a pairing. The limiting identity comes from smooth \(v*\rho_\epsilon\) and legitimate smooth equation tests.

The weights \(\phi_J\) increase to \(\phi\). Their surface integrands decrease and have the integrable majorant from one sufficiently large initial stage. Dominated convergence passes AR28 to
\[
|u(v)|^2\le C\sum_{\ell,a<m_\ell}
 \int_{-N_\ell}|\partial_e^aF_v(z)|^2e^{-2\phi(z)}W(z)^K\,dS_\ell(z).
\tag{AR29}
\]
Use the finite Hilbert direct sum of these weighted surface spaces. AR29 makes \(Jv=(\partial_e^aF_v|_{-N_\ell})\mapsto u(v)\) well defined and bounded. Extend to its closure, represent by \(g_\ell^a\), and put
\[
B_\ell^a(s)=\overline{g_\ell^a(s)}e^{-2\phi(s)}W(s)^K,\qquad
U_\ell^a(z)=(-i)^a|\tau|^{-a}B_\ell^a(-z).
\tag{AR30}
\]
The representing-vector norm gives AR22; the finite constants \(|\tau|^{-2a}\) are harmless. Euclidean reflection preserves \(dS\) and \(W\), and
\[
\partial_e^aF_v(-z)=v\bigl((-i\,x\cdot e)^ae^{ix\cdot z}\bigr).
\tag{AR31}
\]
Thus the representing identity is precisely AR23. Cauchy–Schwarz proves absolute convergence after every compact smooth test, including every jet. Each kernel solves the equation: the finite polynomial product rule uses only derivatives of \(P(z+t\tau)\) of order at most \(a<m_\ell\), all zero at \(z\in N_\ell\) because of the \(P_\ell^{m_\ell}\) factor. This remains true at singular characteristic points.

For nonzero constant \(P\), the solution is zero and the sum is empty. The zero polynomial has no noncharacteristic direction; its arbitrary distributions are covered by AR1 rather than an invented characteristic factorization. For empty \(X\), both statements concern only zero; \(\phi=p_1(\eta)\) supplies the vacuous growth condition and actual strict curvature, and \(U=0\). These endpoints finish both page-300 exercises in their full scope.

## Source and course scope

The classical human source is Lars Hörmander, *The Analysis of Linear Partial Differential Operators II*, §15.4, two unnumbered exercises on printed p.300, immediately after Theorem15.4.3. The actual approved edition is native PDF page313. Its protected statement/proof pixels and exercise text were read privately; no protected book body or page image is included here. The underlying surface theorem is15.3.3, and the whole-complex formula is the requested analogue of15.2.18.

All local division, area and weighted existence providers used above have full original proofs in the linked lower lessons. The new finite-envelope smoothing lemma is proved here in full and specifically closes the arbitrary-distribution gap. Completing these exercises does not complete the three Chapter15 notes, its remaining passage audit, all78 Chapter16 targets or any assigned residual in Chapters10–13. The entire course goal remains active.
