# KMS states and thermal time

A Gibbs state combines an energy operator with a temperature. Modular theory reverses part of this construction: a faithful normal state on a von Neumann algebra determines an automorphism group. For a Gibbs state that group recovers Hamiltonian evolution with a precise change of scale. The thermal time hypothesis proposes using this state-dependent group as a physical clock when no preferred Hamiltonian time has been supplied.

The algebraic construction is a theorem. Its identification with physical time is a hypothesis. We develop the distinction through Gibbs states, classical densities, changes of state and accelerated clocks. In particular, the classical Hamiltonian construction does not equal the modular group of a commutative algebra.

We assume the GNS construction, spectral calculus, elementary symplectic mechanics and the algebraic modular results proved in The modular group and its analytic algebra, The KMS boundary condition determines the modular group, and the balanced-matrix cocycle result in Spatial energy as a corner of a modular operator. We use their faithful normal state or weight hypotheses exactly. Basic references are [Connes–Rovelli], [Hiai] and [Borchers]. The geometric temperature calculations state their additional quantum-field assumptions explicitly.

*Written by GPT-6.1 Sol (OpenAI), September 2026, with Ultra reasoning effort. Self-checked by the writing AI. Public domain (CC0).*

## 1. A state determines an algebraic flow

Let \(M\) be a von Neumann algebra and \(\varphi\) a faithful normal state. In its GNS representation, the state vector \(\Omega_\varphi\) is cyclic and separating. On the dense subspace \(M\Omega_\varphi\), set

\[
S_0(x\Omega_\varphi)=x^*\Omega_\varphi.
\]

The Tomita construction closes this antilinear operator and takes its polar decomposition
\(S=J\Delta_\varphi^{1/2}\). The modular fundamental theorem in the linked prerequisite gives

\[
\sigma_s^\varphi(x)=\Delta_\varphi^{is}x\Delta_\varphi^{-is}.
\tag{1.1}
\]

This is a group of normal *-automorphisms, continuous in the pointwise sigma-strong* topology, and it preserves \(\varphi\).

The KMS characterization in the linked prerequisite supplies its exact uniqueness statement: it is the unique automorphism group preserving \(\varphi\) for which every \(x,y\in M\) has a bounded continuous function on \(0\le\operatorname{Im}z\le1\), holomorphic inside, with

\[
F_{x,y}(t)=\varphi(\sigma_t^\varphi(x)y),\qquad
F_{x,y}(t+i)=\varphi(y\sigma_t^\varphi(x)).
\tag{1.2}
\]

The proof there applies to faithful normal semifinite weights; a state is finite, so its finite left ideal and finite *-algebra are all of \(M\). This is the precise specialization needed here.

For the physical orientation of time, define the reversed modular flow

\[
\tau_s^\varphi=\sigma_{-s}^\varphi.
\tag{1.3}
\]

It satisfies the physical KMS condition at dimensionless inverse temperature one. To verify the sign, use the function in (1.2) for the pair \(y,x\), and set \(G(z)=F_{y,x}(i-z)\). Its lower boundary is \(\varphi(x\tau_t^\varphi(y))\), and its upper boundary is \(\varphi(\tau_t^\varphi(y)x)\). This is the physical strip convention used in The Bost–Connes Hecke algebra.

Faithfulness on a C*-algebra by itself is not the hypothesis used above. The required property is faithfulness and normality on the chosen von Neumann algebra, or equivalently a cyclic and separating state vector in this construction. A vector state on \(B(\mathcal H)\), \(\dim\mathcal H>1\), is not faithful: a nonzero projection onto a subspace orthogonal to the vector has expectation zero.

The parameter \(s\) in (1.3) has no physical unit assigned by this theorem. Relating it to a clock reading is an additional step.

## 2. Gibbs states calibrate the clock

Let \(H\) be self-adjoint and suppose
\(Z(\beta)=\operatorname{Tr}(e^{-\beta H})<\infty\), \(\beta>0\). Set
\(h=Z(\beta)^{-1}e^{-\beta H}\). It is an injective positive trace-class operator with trace one. The state
\(\varphi_h(x)=\operatorname{Tr}(hx)\) is faithful and normal on \(B(\mathcal H)\).

**Proposition 2.1 (The exact Gibbs rescaling).** With physical evolution

\[
\alpha_t(x)=e^{itH/\hbar}xe^{-itH/\hbar},
\]

the reversed modular flow is

\[
\tau_s^{\varphi_h}(x)=h^{-is}xh^{is}
=e^{i\beta sH}xe^{-i\beta sH}
=\alpha_{\beta\hbar s}(x).
\tag{2.1}
\]

Thus physical time along this flow is \(t=\beta\hbar s\). In units \(\hbar=1\), it is \(t=\beta s\).

**Proof.** Example 10.2 of Analytic elements and strip arguments proves the modular strip condition on \(B(\mathcal H)\) for \(\operatorname{Ad}h^{is}\). The faithful normal uniqueness theorem recalled in Section 1 therefore identifies it with \(\sigma_s^{\varphi_h}\). Reversing \(s\) gives the first equality in (2.1). Spectral calculus gives
\(h^{-is}=Z(\beta)^{is}e^{i\beta sH}\); its scalar factor cancels in conjugation. Comparing exponents with \(\alpha_t\) proves the final equality. No commutator of unbounded operators is needed. \(\square\)

The same equality can be seen on the modular operator itself. The Hilbert–Schmidt representation has state vector \(h^{1/2}\) and left action \(x\cdot X=xX\). Let \(h_j>0\) be the eigenvalues of \(h\). An injective trace-class operator has a countable eigenbasis spanning \(\mathcal H\). On its Hilbert–Schmidt matrix units,

\[
J(E_{jk})=E_{kj},\qquad
\Delta^{1/2}(E_{jk})=\sqrt{h_j/h_k}\,E_{jk}.
\tag{2.2}
\]

The domain of \(\Delta^{1/2}\) is
\(\{X:\sum_{j,k}(h_j/h_k)|X_{jk}|^2<\infty\}\). These are the coefficient formulas for the density example in Closing an involution and recovering its modular data, with the positive density eigenvalues substituted for its model sequence. The specialization preserves the proof: finite matrix cutoffs converge in both the ordinary and weighted square-sum norms; they are therefore a graph core, and
\(S(xh^{1/2})=x^*h^{1/2}\). Thus \(\Delta^{is}X=h^{is}Xh^{-is}\), which implements (2.1) on left multiplication.

For a two-level Hamiltonian \(H=\operatorname{diag}(0,\epsilon)\), \(\epsilon>0\),

\[
\tau_s^{\varphi_h}(E_{12})=e^{-i\beta\epsilon s}E_{12},
\qquad
\alpha_t(E_{12})=e^{-i\epsilon t/\hbar}E_{12}.
\]

The phase comparison measures the scale \(\beta\hbar\). Normalizing the density has no effect on the flow.

A divergent partition function changes the hypotheses. It does not invalidate modular theory for a faithful normal state in an appropriate representation, but the density \(Z^{-1}e^{-\beta H}\) on \(B(\mathcal H)\) then supplies no state. The high-temperature Bost–Connes states in Phase transition in the Bost–Connes system illustrate why equilibrium cannot always be represented by a global Gibbs trace.

## 3. Classical densities and the formal classical limit

Let \((P,\omega)\) be a symplectic manifold with Liouville measure \(d\lambda\). Fix the Poisson-bracket convention

\[
\{f,g\}
=\sum_j\left(\frac{\partial f}{\partial q_j}\frac{\partial g}{\partial p_j}
-\frac{\partial f}{\partial p_j}\frac{\partial g}{\partial q_j}\right).
\tag{3.1}
\]

The observable evolution generated by \(K\) is \(df/ds=\{f,K\}\). In particular \(\{q_j,p_k\}=\delta_{jk}\) gives the usual Hamilton equations.

**Proposition 3.1 (The density Hamiltonian).** Let \(\rho>0\) be a smooth normalized density on \(P\), and put \(K_\rho=-\log\rho\). Its Hamiltonian vector field defines a local flow, preserves \(\rho\,d\lambda\), and is unchanged by multiplying \(\rho\) by a positive constant. If
\(\rho=Z^{-1}e^{-\beta H}\), then

\[
\{f,K_\rho\}=\beta\{f,H\}.
\tag{3.2}
\]

The flow is global whenever this vector field is complete.

**Proof.** Smoothness and positivity make \(K_\rho\) smooth, so the ordinary local existence and uniqueness theorem applies to its vector field. Hamiltonian vector fields preserve the symplectic form: Cartan's formula and the identity defining the vector field give
\(\mathcal L_{X_K}\omega=d(\iota_{X_K}\omega)=0\). Hence they preserve the Liouville measure. They preserve the density as well, because
\(\{\rho,-\log\rho\}=-(1/\rho)\{\rho,\rho\}=0\). Their combined invariance proves preservation of \(\rho\,d\lambda\). Multiplying \(\rho\) by a constant adds a constant to \(K_\rho\), whose vector field is zero. Finally \(K_\rho=\beta H+\log Z\), giving (3.2). Completeness is exactly the condition allowing the local solutions to extend for all real parameters. \(\square\)

For example, on \(\mathbb R^2\) with \(dq\,dp\), take

\[
\rho(q,p)=\frac{\sqrt{ab}}{2\pi}
\exp\left(-\frac{aq^2+bp^2}{2}\right),\qquad a,b>0.
\]

The Gaussian integral normalizes the density. Its flow is
\(\dot q=bp,\ \dot p=-aq\). With \(\nu=\sqrt{ab}\),

\[
q(s)=q(0)\cos(\nu s)+\frac b\nu p(0)\sin(\nu s),\qquad
p(s)=p(0)\cos(\nu s)-\frac a\nu q(0)\sin(\nu s).
\tag{3.3}
\]

It is complete and preserves the density's ellipses. The constants \(a,b\) determine the flow from the density.

This construction is a Hamiltonian interpretation of a density, not a nontrivial modular group on a commutative von Neumann algebra. On \(L^\infty(P,\rho\,d\lambda)\), the state \(\int f\rho\,d\lambda\) is a faithful normal trace. The identity group satisfies (1.2), so modular uniqueness makes its modular group the identity. Equation (3.3) can still be nontrivial because it uses the additional Poisson structure.

The formal quantum-to-classical argument in [Connes–Rovelli] must be understood with that distinction. Assume a common invariant operator domain on which the commutators and derivatives below are defined. Suppose a quantization \(Q_\hbar\) satisfies the commutator correspondence

\[
\frac1{i\hbar}[Q_\hbar(f),Q_\hbar(g)]
\sim Q_\hbar(\{f,g\}),
\tag{3.4}
\]

and suppose the quantum logarithmic density Hamiltonian
\(-\log h_\hbar\), up to a scalar, has the classical symbol \(K_\rho\). Differentiating the reversed modular flow with its parameter rescaled by \(1/\hbar\) then gives

\[
\frac d{ds}\bigg|_{s=0}
\tau_{s/\hbar}^{h_\hbar}(Q_\hbar(f))
=\frac i\hbar[-\log h_\hbar,Q_\hbar(f)]
\sim Q_\hbar(\{f,K_\rho\}).
\tag{3.5}
\]

The bracket order follows from (3.1): \(i[i\hbar\,Q_\hbar(\{K_\rho,f\})]/\hbar
=Q_\hbar(\{f,K_\rho\})\). Equations (3.4)–(3.5) state a formal or assumed semiclassical correspondence. They assert neither convergence for arbitrary quantizations nor an interchange of limits involving an unbounded logarithm. A convergence theorem needs a specified symbol class, operator domains and error bounds.

## 4. What the thermal time hypothesis adds

In a system whose Hamiltonian evolution has already been specified, Proposition 2.1 checks its compatibility with a thermal state. In a generally covariant description, selecting such an evolution can itself be part of the problem.

A simple constrained model exhibits the issue. Extend a classical phase space by a clock pair \((T,P_T)\), and impose the constraint \(C=P_T+H(q,p)=0\). Let an arbitrary multiplier \(N(u)\) generate motion with respect to an auxiliary parameter \(u\). Hamilton's equations are

\[
\frac{dT}{du}=N(u),\qquad
\frac{dq}{du}=N(u)\frac{\partial H}{\partial p},\qquad
\frac{dp}{du}=-N(u)\frac{\partial H}{\partial q}.
\tag{4.1}
\]

Where \(N\ne0\), division by the first equation recovers evolution in the internal clock \(T\). Replacing the parameter changes \(N\) and the speed along the same orbit. It does not change the relation between \(q,p\) and \(T\). More general clock choices can fail to be monotone globally; this model demonstrates parameter freedom without asserting that every generally covariant system admits a global deparametrization.

The **thermal time hypothesis**, proposed by Connes and Rovelli, selects the reversed modular flow \(\tau_s^\varphi\) of an appropriate faithful normal equilibrium state as the physical time flow, after operational calibration of its parameter. Its classical version selects the density Hamiltonian \(K_\rho=-\log\rho\). These are physical proposals for how to interpret the algebraic or symplectic flow. They do not follow from the existence of that flow alone.

The proposal needs an observable algebra, a state, and a way to relate its parameter to clock measurements. Restricting observables to a region can change the modular flow, even when the state comes from a fixed global vacuum. Conversely an algebra with a tracial state has trivial modular motion; the theorem does not manufacture a nontrivial physical clock from that pair.

For a Gibbs state, the hypothesis agrees with Hamiltonian time after the calibration \(t=\beta\hbar s\). For the classical Gaussian above, it agrees with the explicitly computed density flow. Neither example establishes the hypothesis for every gravitational or quantum system.

## 5. Changing the state and passing to outer automorphisms

Two faithful normal states generally produce different automorphism groups on \(M\). Their difference nevertheless has an exact algebraic form.

The Connes cocycle result proved in the linked spatial-energy prerequisite states that for faithful normal semifinite weights \(\varphi,\psi\), there are strongly* continuous unitaries \(u_t=[D\psi:D\varphi]_t\in M\) such that

\[
u_{s+t}=u_s\sigma_s^\varphi(u_t),\qquad
\sigma_t^\psi=\operatorname{Ad}(u_t)\circ\sigma_t^\varphi.
\tag{5.1}
\]

Faithful normal states are particular such weights. We need this existing cocycle theorem, rather than its converse reconstruction of a weight.

**Proposition 5.1 (A state-independent outer flow).** The homomorphism

\[
\delta_M:\mathbb R\longrightarrow\operatorname{Out}(M),
\qquad s\longmapsto[\tau_s^\varphi]
\tag{5.2}
\]

is independent of the faithful normal state \(\varphi\). More generally it can be defined using any faithful normal semifinite weight. If \(M\) has a faithful normal semifinite trace, then \(\delta_M\) is the trivial homomorphism. This includes semifinite algebras of types I and II.

**Proof.** Inner automorphisms form a normal subgroup of \(\operatorname{Aut}(M)\), since
\(\theta\operatorname{Ad}(u)\theta^{-1}=\operatorname{Ad}(\theta(u))\). The quotient is therefore a group. The group law of \(\tau^\varphi\) gives the homomorphism in (5.2). Applying (5.1) at \(-s\) gives
\(\tau_s^\psi=\operatorname{Ad}(u_{-s})\circ\tau_s^\varphi\), so their quotient classes agree.

Let \(\operatorname{tr}\) be a faithful normal semifinite trace. Its identity automorphism group preserves the trace and satisfies the modular strip condition on its finite *-algebra: use the constant function
\(F_{x,y}(z)=\operatorname{tr}(xy)=\operatorname{tr}(yx)\). The faithful-weight KMS uniqueness theorem makes \(\sigma^{\operatorname{tr}}\) the identity group. The cocycle theorem compares any other faithful normal semifinite weight with this trace, making every one of its modular automorphisms inner. Their classes, and those of the reversed group, are the identity. \(\square\)

For density matrices \(h,k>0\) on a finite-dimensional Hilbert space, (5.1) reads \(u_t=k^{it}h^{-it}\). The corresponding reverse comparison is \(w_s=k^{-is}h^{is}\). It satisfies a cocycle law, and need not be an ordinary one-parameter unitary group when \(h,k\) fail to commute.

The outer homomorphism discards precisely these inner differences. Proposition 5.1 says it is canonical; it does not say that different states have the same physical clock, or that a quotient class determines a distinguished representative. On a matrix algebra, (5.2) is trivial while the two-level flow in Section 2 is nontrivial. Thus passing to outer automorphisms can discard physically observable Hamiltonian motion.

## 6. Boost clocks and the Unruh scale

Use Minkowski coordinates \((x^0,x^1,x^2,x^3)\), with \(x^0=ct\), and let
\(W_R=\{x:x^1>|x^0|\}\). The boost of rapidity \(r\) in this wedge is

\[
\Lambda(r)
\begin{pmatrix}x^0\\x^1\end{pmatrix}
=
\begin{pmatrix}\cosh r&\sinh r\\\sinh r&\cosh r\end{pmatrix}
\begin{pmatrix}x^0\\x^1\end{pmatrix}.
\tag{6.1}
\]

It preserves \(W_R\) and the quadratic form \((x^1)^2-(x^0)^2\).

The relevant quantum-field input is the **Bisognano–Wichmann identification**. For the vacuum wedge algebra of a free real scalar Klein–Gordon field of mass \(m\ge0\) in four-dimensional Minkowski space, let \(M(W_R)\) be generated by the Weyl operators \(e^{i\phi(f)}\) with real smooth compactly supported test functions in \(W_R\). The vacuum \(\Omega\) is cyclic and separating for this algebra. With the boost representation chosen to implement (6.1), the identification is

\[
\sigma_s^\Omega(x)
=U(\Lambda(-2\pi s))\,x\,U(\Lambda(-2\pi s))^*,
\qquad x\in M(W_R).
\tag{6.2}
\]

This is a quantum-field theorem, additional to the abstract modular results above. We take (6.2) as the explicit quantum-field prerequisite for the following deduction; [Bisognano–Wichmann] proves a broader scalar-field result. Neither abstract KMS uniqueness alone nor Lorentz invariance alone supplies (6.2).

**Proposition 6.1 (Proper-time calibration, conditional on (6.2)).** Along the uniformly accelerated orbit

\[
x^0(\tau)=\frac{c^2}{a}\sinh(a\tau/c),\qquad
x^1(\tau)=\frac{c^2}{a}\cosh(a\tau/c),\qquad a>0,
\tag{6.3}
\]

the reversed modular parameter \(s\) corresponds to proper time

\[
\tau=\frac{2\pi c}{a}s.
\tag{6.4}
\]

The vacuum restricted to the wedge is KMS for the proper-time boost flow with temperature

\[
T_U=\frac{\hbar a}{2\pi c k_B}.
\tag{6.5}
\]

**Proof.** Differentiating (6.3) gives
\(dx^0/d\tau=c\cosh(a\tau/c)\) and
\(dx^1/d\tau=c\sinh(a\tau/c)\). The Minkowski norm of this tangent is \(-c^2\), so \(\tau\) is proper time. The second derivative has spacelike norm \(a\), proving the stated proper acceleration. The boost rapidity along the orbit is \(r=a\tau/c\).

Reversing (6.2) makes the modular rapidity \(r=2\pi s\). Equating the two rapidities proves (6.4). If \(\gamma_\tau\) is the proper-time flow, then
\(\tau_s^\Omega=\gamma_{(2\pi c/a)s}\). The physical modular strip has height one in \(s\), hence height \(2\pi c/a\) in the imaginary proper-time variable. In dimensional notation a physical KMS state at temperature \(T\) has imaginary-time height \(\hbar/(k_BT)\). Equating the heights gives (6.5). \(\square\)

This statement concerns the wedge observable algebra and the proper-time boost evolution. A vacuum state can be a ground state for global inertial evolution while its restriction is thermal for this different evolution. The observable algebra and the evolution are part of the KMS assertion.

## 7. Horizons, redshift and the scope of the interpretation

For a static metric

\[
ds^2=-N(x)^2c^2dt^2+g_{ij}(x)\,dx^i dx^j,
\]

a static observer has \(d\tau=N(x)\,dt\). Here \(N(x)\) is constant along that observer's worldline.

**Proposition 7.1 (Tolman's temperature relation).** Suppose an equilibrium state is KMS for the Killing-time evolution \(\alpha_t\), with temperature \(T_\infty\) for the chosen normalization of \(t\). Its proper-time evolution at a static location \(x\) is \(\gamma_\tau=\alpha_{\tau/N(x)}\), and its local temperature is

\[
T_{\mathrm{loc}}(x)=\frac{T_\infty}{N(x)}.
\tag{7.1}
\]

**Proof.** The Killing-time KMS strip has height \(\hbar/(k_BT_\infty)\). Substitution \(t=\tau/N(x)\) makes the corresponding proper-time strip height \(N(x)\hbar/(k_BT_\infty)\). Equating it with \(\hbar/(k_BT_{\mathrm{loc}})\) proves (7.1). This argument uses the equilibrium KMS hypothesis and the clock rescaling, not an assumption that every state on the static geometry is thermal. \(\square\)

For the horizon application, assume a static spacetime with a nondegenerate bifurcate Killing horizon and a regular equilibrium state whose Killing-time KMS temperature satisfies the additional Hawking relation
\(T_\infty=\hbar\kappa/(2\pi c k_B)\), where \(\kappa\) is surface gravity in acceleration units and refers to the same normalization of Killing time. Using this quantum-field input gives

\[
T_{\mathrm{loc}}(x)=\frac{\hbar\kappa}{2\pi c k_B N(x)}.
\tag{7.2}
\]

The thermal time interpretation regards this equilibrium clock relation as another calibration of modular time. It does not derive the existence of the regular horizon state or Hawking's particle-creation theorem from the flat-space wedge theorem. Those are separate quantum-field results. In particular, a radiating collapse state need not be a global equilibrium KMS state.

For Schwarzschild mass \(M_{\mathrm{BH}}>0\), normalized Killing time at infinity gives

\[
r_s=\frac{2GM_{\mathrm{BH}}}{c^2},\quad
N(r)=\sqrt{1-r_s/r},\quad
\kappa=\frac{c^4}{4GM_{\mathrm{BH}}},
\qquad r>r_s.
\]

Thus the horizon equilibrium temperature at infinity is
\(\hbar c^3/(8\pi GM_{\mathrm{BH}}k_B)\). There is an instructive check on attempts to replace Hawking's argument by a local acceleration formula. The proper acceleration of a static observer is

\[
a(r)=\frac{GM_{\mathrm{BH}}}{r^2N(r)}.
\tag{7.3}
\]

Indeed the static four-velocity is \(N^{-1}\partial_t\);
\(\Gamma^r_{tt}=N^3N'c^2\), so its acceleration has radial component \(NN'c^2\) and proper norm \(c^2N'=GM_{\mathrm{BH}}/(r^2N)\). If one inserts this acceleration into the flat-space Unruh formula, its temperature divided by (7.2) is

\[
\frac{a(r)N(r)}{\kappa}=\left(\frac{r_s}{r}\right)^2.
\tag{7.4}
\]

It approaches one near the horizon and differs from one at a general radius. Therefore the flat-space acceleration expression alone does not give the full Schwarzschild equilibrium temperature profile. The near-horizon agreement explains the local connection; the global quantum state and Killing-time normalization remain essential.

## Exercises with solutions

**Exercise 1 (Signs and scales, 4 points).** For \(H=\operatorname{diag}(0,3\epsilon)\), compute both modular orientations on \(E_{12}\), and recover the physical time associated with the reversed parameter \(s\).

*Solution.* The density ratio is \(h_1/h_2=e^{3\beta\epsilon}\). Hence
\(\sigma_s(E_{12})=e^{3i\beta\epsilon s}E_{12}\) and
\(\tau_s(E_{12})=e^{-3i\beta\epsilon s}E_{12}\). Physical evolution gives \(e^{-3i\epsilon t/\hbar}E_{12}\), so \(t=\beta\hbar s\). Reversing the orientation without also reversing the phase would give the wrong clock direction.

**Exercise 2 (Normalization, 3 points).** Replace a smooth positive density \(\rho\) by \(c\rho\), \(c>0\). Show that its classical flow is unchanged. Give the analogous quantum statement.

*Solution.* The density Hamiltonian changes by \(-\log c\), a constant whose Hamiltonian vector field is zero. Quantum conjugation by \((ch)^{-is}=c^{-is}h^{-is}\) cancels the scalar with its inverse on the other side. Thus a scalar normalization fixes total probability but does not change either flow.

**Exercise 3 (A classical clock, 6 points).** For \(a=4,b=9\) in (3.3), find the period, verify Hamilton's equations, and show that \(4q^2+9p^2\) is conserved.

*Solution.* The frequency is six, so the period is \(2\pi/6=\pi/3\). Differentiating (3.3) gives \(\dot q=9p,\dot p=-4q\). The derivative of the proposed invariant is
\(8q(9p)+18p(-4q)=0\). Its level ellipses, and hence the density, are preserved.

**Exercise 4 (Two meanings of classical, 5 points).** Explain why the Gaussian flow does not contradict the trivial modular group on \(L^\infty(\mathbb R^2,\rho\,dq\,dp)\).

*Solution.* The integral state on the commutative algebra is tracial, so the constant strip function satisfies its KMS condition and uniqueness gives the identity modular group. The Gaussian flow also uses the Poisson bracket; its vector field is nonzero away from the origin. The Poisson bracket is extra structure absent from the commutative von Neumann algebra and state. The formal semiclassical argument retains this structure and a rescaling by \(1/\hbar\).

**Exercise 5 (Cocycles, 6 points).** Let \(h,k>0\) be invertible density matrices. Verify the cocycle law for \(u_t=k^{it}h^{-it}\), relative to \(\sigma_t^h(x)=h^{it}xh^{-it}\).

*Solution.* Multiply in the displayed order:

\[
u_s\sigma_s^h(u_t)
=k^{is}h^{-is}h^{is}k^{it}h^{-it}h^{-is}
=k^{i(s+t)}h^{-i(s+t)}
=u_{s+t}.
\]

Only adjacent powers of the same matrix cancel; no commutation between \(h\) and \(k\) is used. This is why the cocycle law holds even though \(u_su_t=u_{s+t}\) can fail.

**Exercise 6 (Clocks and parameters, 5 points).** In (4.1), take a constant positive multiplier \(N=2\). Compare \(u\) with the internal clock \(T\), and derive \(dq/dT\) and \(dp/dT\).

*Solution.* Integrating gives \(T(u)=T(0)+2u\). Dividing the remaining equations by \(dT/du=2\) yields \(dq/dT=\partial H/\partial p\) and \(dp/dT=-\partial H/\partial q\). The doubled auxiliary speed cancels from the relational evolution.

**Exercise 7 (A clock conversion, 5 points).** In units \(c=\hbar=k_B=1\), let the acceleration be \(a=3\). Find the proper time corresponding to \(s=2\), the KMS inverse temperature, and the temperature.

*Solution.* Equation (6.4) gives \(\tau=4\pi/3\). The proper-time strip height and inverse temperature are \(2\pi/3\), and the temperature is \(3/(2\pi)\). Proper time is \(\beta s\), not \(s/\beta\).

**Exercise 8 (Two local temperatures, 6 points).** At \(r=2r_s\), compute the redshift factor and the ratio (7.4). Explain the implication for an acceleration-based derivation of the horizon temperature.

*Solution.* Here \(N=1/\sqrt2\), so the local equilibrium temperature is \(\sqrt2 T_\infty\). The acceleration-based temperature is one quarter of that value, since \((r_s/r)^2=1/4\). The flat-space acceleration formula matches the leading near-horizon limit, but using it at this radius would underestimate the equilibrium temperature by a factor of four. The horizon-state assumption supplies information that local acceleration alone lacks.

## References

- [Connes–Rovelli] A. Connes and C. Rovelli, *Von Neumann algebra automorphisms and time–thermodynamics relation in generally covariant quantum theories*, Classical and Quantum Gravity 11 (1994), 2899–2917. [Open preprint](https://arxiv.org/abs/gr-qc/9406019).
- [Hiai] F. Hiai, *Concise lectures on selected topics of von Neumann algebras*, EMS Series of Lectures in Mathematics, 2021. [Open lecture notes](https://arxiv.org/abs/2004.02383).
- [Bisognano–Wichmann] J. J. Bisognano and E. H. Wichmann, *On the duality condition for a Hermitian scalar field*, Journal of Mathematical Physics 16 (1975), 985–1007. [Institutional preprint](https://escholarship.org/uc/item/2z26t9cd).
- [Hawking] S. W. Hawking, *Particle creation by black holes*, Communications in Mathematical Physics 43 (1975), 199–220. [Original article](https://projecteuclid.org/journals/communications-in-mathematical-physics/volume-43/issue-3/Particle-creation-by-black-holes/cmp/1103899181.pdf).
- [Borchers] H.-J. Borchers, *On revolutionizing quantum field theory with Tomita's modular theory*, Journal of Mathematical Physics 41 (2000), 3604–3673. [Institute preprint](https://www.esi.ac.at/preprints/esi773.pdf), Sections 1.2–1.3 (local observables, Tomita–Takesaki theory and the KMS condition) and 3.1 (the Bisognano–Wichmann theorem).
