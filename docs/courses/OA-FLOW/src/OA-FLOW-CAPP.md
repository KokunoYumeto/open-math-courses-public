# Compatible expectations carry the core-center invariant to a limit

<a id="capp-setting"></a>

The centers of increasing cores need not be increasing. The useful replacement is a norm-convergence statement for restrictions of each fixed normal functional. We prove that statement and use it to pass both the complete orbit metric and the entire subinvariant range to the limit.

Earlier complete proofs: [CINV.MASS](OA-FLOW-CINV.md#cinv-mass), [CINV.INVERSE](OA-FLOW-CINV.md#cinv-inverse), [CINV.COVARIANCE](OA-FLOW-CINV.md#cinv-covariance), [CINV.METRIC](OA-FLOW-CINV.md#cinv-metric), [OT.5](OA-FLOW-OT.md#oa-flow.ot.5), [CP.1](OA-FLOW-CP.md#oa-flow.cp.1), [CP.2](OA-FLOW-CP.md#oa-flow.cp.2), [CP.4](OA-FLOW-CP.md#oa-flow.cp.4), [CP.5](OA-FLOW-CP.md#oa-flow.cp.5), [CP.6](OA-FLOW-CP.md#oa-flow.cp.6), [NR.3](OA-FLOW-NR.md#oa-flow.nr.3), [NR.4](OA-FLOW-NR.md#oa-flow.nr.4), [CORE.3](OA-FLOW-CORE.md#core-3), [DA.AVERAGE](OA-FLOW-DA.md#da-compact), [SCW.1](OA-FLOW-SCW.md#scw-1), [SCW.2](OA-FLOW-SCW.md#scw-2), [SCW.3](OA-FLOW-SCW.md#scw-3), [ST.1](OA-FLOW-ST12.md#oa-flow.st.1), [GRP.VECTORINTEGRATION](OA-FLOW-L24.md#oa-flow.grp.vectorintegration), [CEXP.CONVERGENCE](OA-FLOW-CEXP.md#cexp-convergence), [CSAS.DISTANCE](OA-FLOW-CSAS.md#csas-distance), [CSAS.RANGE](OA-FLOW-CSAS.md#csas-range), OA-MOD DC-05.

<a id="capp-reference"></a>
## 1. Hypotheses and a common modular reference

Let \(M\) have separable predual. Suppose
\[
 M_0\subset M_1\subset\cdots\subset M,\qquad
 E_i:M\to M_i
\]
are faithful normal conditional expectations with common unit, satisfying
\[
 E_iE_j=E_jE_i=E_i\ (i\le j),\qquad
 \|\eta E_i-\eta\|\to0\quad(\eta\in M_*).                          \tag{CM1}
\]
Suppose the distance equality
\(\delta_{M_i}(\phi,\psi)=\|\chi_\phi-\chi_\psi\|\)
holds for every pair of positive normal functionals on each \(M_i\). The conclusions below concern all positive normal functionals, without equal-mass or faithfulness assumptions.

Choose a faithful normal state \(\omega_0\) on \(M_0\), and put
\(\omega=\omega_0E_0\). Compatibility implies \(\omega E_i=\omega\), and \(\omega\) is faithful because both factors are faithful. Write \(\omega_i=\omega|_{M_i}\).

OT5 applied to \(E_i\), \(\omega_i\) proves
\(\sigma^\omega_t|_{M_i}=\sigma^{\omega_i}_t\). Also
\[
 E_i\sigma^\omega_t=\sigma^{\omega_i}_tE_i.                        \tag{CM2}
\]
To verify the latter assertion, pair both sides against
\(y\mapsto\omega_i(a^*yb)\), \(a,b\in M_i\). Use \(\omega E_i=\omega\), bimodularity, and invariance of \(\omega\) under its modular group to move \(\sigma_t\) to \(a,b\). The two pairings coincide. These coefficient functionals separate \(M_i\) by faithful GNS, so (CM2) follows.

Use these references for the cores
\[
 C_i=M_i\rtimes_{\sigma^{\omega_i}}\mathbb R\subset
 C=M\rtimes_{\sigma^\omega}\mathbb R .
\]
The inclusions send coefficient elements and translation unitaries to the same operators in the regular representation. The regular construction is faithful for every faithful coefficient representation; restricting the coefficient representation to \(M_i\) therefore gives the asserted normal inclusion. All cores have the same dual action on their generators. Condition (CM1) makes \(\bigcup_iM_i\) ultraweakly dense: a normal functional annihilating the union equals the limit of its zero compositions with \(E_i\). Consequently \(\bigcup_iC_i\) is ultraweakly dense in \(C\).

<a id="capp-lift"></a>
## 2. Lifted expectations, trace preservation and predual convergence

The normal amplification \(E_i\bar\otimes\operatorname{id}\) on
\(M\bar\otimes B(L^2(\mathbb R))\) can be constructed entry by entry. On every finite matrix corner use \([x_{jk}]\mapsto[E_i(x_{jk})]\). Complete positivity gives its common norm bound one. The compatible finite compressions therefore determine a bounded operator, with positivity at every matrix level. Matrix vector pairings and then their summable tails prove normality. If a positive operator has zero image, every positive diagonal entry has zero \(E_i\)-value and is zero by faithfulness; positive \(2\times2\) corners then force its off-diagonal entries to vanish. Thus the amplification is faithful.

It is bimodular over \(1\otimes B(L^2(\mathbb R))\). Equation (CM2) sends the regular coefficient function \(t\mapsto\sigma_{-t}^\omega(x)\) to the corresponding coefficient for \(E_i(x)\), and fixes translations. Restriction gives
\[
 F_i:C\to C_i,\qquad
 F_i(\pi(x)\lambda_t)=\pi(E_i(x))\lambda_t.                         \tag{CM3}
\]
Products of such generators span an ultraweakly dense algebra. Normality proves that the range lies in \(C_i\) and that \(F_i\) fixes \(C_i\). Bimodularity follows directly from complete positivity: the \(2\times2\) Schwarz defect matrix
\([F_i(a_j^*a_k)-F_i(a_j)^*F_i(a_k)]_{j,k=1}^2\)
is positive, by applying \(F_i\) to the \(3\times3\) Gram matrix for \(a_1,a_2,1\) and taking the Schur complement of its last entry. If \(a_1=b\in C_i\), its first diagonal entry is zero, so both off-diagonal entries vanish. This gives \(F_i(b^*x)=b^*F_i(x)\); adjoints give the other module identity. Thus \(F_i\) is the faithful normal conditional expectation onto \(C_i\), and
\[
 F_iF_j=F_jF_i=F_i\ (i\le j),\qquad F_i\theta_s=\theta_sF_i.         \tag{CM4}
\]

These expectations converge in the full predual:
\[
 \|\eta F_i-\eta\|\to0\qquad(\eta\in C_*).                          \tag{CM5}
\]
Indeed finite sums of product normal functionals are norm dense in the ambient tensor-product predual: use CP's vector-series description, truncate the series, approximate the finitely many tensor vectors by finite sums of simple vectors, and expand. On a product functional the assertion is exactly (CM1). Contractivity passes it to all ambient normal functionals. Every normal functional on \(C\) extends to an ambient normal functional by CP's concrete predual quotient, so restriction proves (CM5).

Let \(\tau_i,\tau\) be the canonical traces with the same Haar convention. The complete positive averages commute with the expectations; test compact positive averages first and increase their integration intervals. Thus
\[
 \widetilde\omega=\widetilde{\omega_i}\,F_i.
\]
The canonical reference densities have the same imaginary powers \(\lambda_t\); their complete spectral operators agree under the inclusion. The bounded inverse-density formula of CORE3, with
\(a_\varepsilon=(h_\omega+\varepsilon)^{-1}\in C_i\), now gives, for every \(Y\ge0\),
\[
 \begin{aligned}
 \tau(Y)
 &=\sup_{\varepsilon>0}
       \widetilde\omega(a_\varepsilon^{1/2}Ya_\varepsilon^{1/2})\\
 &=\sup_{\varepsilon>0}
       \widetilde{\omega_i}(a_\varepsilon^{1/2}F_i(Y)a_\varepsilon^{1/2})
 =\tau_i(F_i(Y)).
 \end{aligned}
\]
Therefore
\[
 \tau|_{C_i}=\tau_i,\qquad \tau F_i=\tau.                          \tag{CM6}
\]
This proves equality on the whole positive cone with its infinite values; a trace-scaling rule alone would not have fixed the scalar.

<a id="capp-supported"></a>
## 3. Supported densities really lie in the smaller core

Let \(\phi_i\in(M_i)_*^+\), and lift it to \(\phi=\phi_iE_i\). Put \(p=s\phi_i\in M_i\). Faithfulness of \(E_i\) proves \(s\phi=p\): if \(\phi(x)=0\), \(x\ge0\), then \(pE_i(x)p=0\); hence \(E_i(pxp)=0\), then \(pxp=0\), which is the support criterion. The converse is immediate.

Choose a faithful completion
\[
 \alpha_i(x)=\phi_i(x)+\omega_i((1-p)x(1-p)),\qquad
 \alpha=\alpha_iE_i.
\]
Both are faithful positive normal functionals, \(p\) is in each centralizer, and
\(\phi_i=(\alpha_i)_p,\ \phi=\alpha_p\).
OT5, now applied to both \(\alpha_i,\omega_i\), identifies their normalized cocycles in \(M_i\) and \(M\). SCW's supported-density formula consequently gives
\[
 h_{\phi}^{it}
 =\pi(p)(D\alpha:D\omega)_t\lambda_t
 =h_{\phi_i}^{it}\in C_i                                             \tag{CM7}
\]
with zero on \(1-p\). The nonsingular density on \(p\) is determined by this unitary group; normal spectral transport includes its complete self-adjoint domain. Thus
\[
 h_\phi=h_{\phi_i},\qquad e_\phi=e_{\phi_i}\in C_i.                 \tag{CM8}
\]
The zero functional is immediate. Equations (CM6)–(CM8), with finite trace pairings, imply
\[
 \chi_{\phi_iE_i}(z)=\chi_{\phi_i}(F_i(z)),\qquad z\in Z(C).         \tag{CM9}
\]
Here \(F_i(z)\) is central in \(C_i\) by bimodularity. To justify the trace pairing, apply (CM6) to positive sandwiches by the finite projection \(e_{\phi_i}\), use bimodularity, and polarize. No unspecified unbounded product occurs.

<a id="capp-distance"></a>
## 4. Restriction to varying centers and the distance equality

For every \(\eta\in C_*\),
\[
 \|\eta|_{Z(C_i)}\|\longrightarrow\|\eta|_{Z(C)}\|.                \tag{CM10}
\]
For the lower bound, if \(z\in Z(C)\) is a contraction, then \(F_i(z)\in Z(C_i)\) is a contraction and \(\eta(F_i(z))\to\eta(z)\) by (CM5). Take the supremum over \(z\).

For the upper bound choose, along a subsequence attaining the limsup, contractions \(z_i\in Z(C_i)\) with \(\eta(z_i)\) real and within \(1/i\) of the restriction norm, multiplying by scalar phases if necessary. The unit ball is weak-star compact. A convergent subnet has a limit \(z\) of norm at most one. For each fixed \(j\), eventual \(z_i\) commute with \(C_j\); separate weak-star continuity of bounded multiplication passes this to \(z\). Density of \(\bigcup_jC_j\) gives \(z\in Z(C)\). Normality of \(\eta\) proves the desired upper bound. This argument does not assert that the centers are nested.

First suppose \(\phi=\phi E_j\), \(\psi=\psi E_j\). For \(i\ge j\), their restrictions \(\phi_i,\psi_i\) lift back to them under \(E_i\). The norm of a lifted functional equals its original norm, since \(E_i\) is contractive and fixes \(M_i\). Conjugation by \(u\in M_i\) commutes with lifting. Hence
\[
 \delta_M(\phi,\psi)\le\delta_{M_i}(\phi_i,\psi_i).
\]
By the assumed smaller-algebra isometry, the right side is
\(\|\chi_{\phi_i}-\chi_{\psi_i}\|\). Define the fixed normal functional
\(\eta(Y)=2\pi\tau((e_\phi-e_\psi)Y)\) on \(C\), meaning the difference of its two finite positive trace pairings. Equations (CM6)–(CM8) identify that norm with
\(\|\eta|_{Z(C_i)}\|\). Let \(i\to\infty\) in (CM10) and combine with construction (CI17). We obtain equality for this pair.

For arbitrary \(\phi,\psi\ge0\), use \(\phi E_j,\psi E_j\). They converge in norm by (CM1). The orbit metric is Lipschitz in each variable, and \(\chi\) is a contraction by (CI14). Passing to the limit proves
\[
 \boxed{\ \delta_M(\phi,\psi)=\|\chi_\phi-\chi_\psi\|
                 \quad(\phi,\psi\in M_*^+).\ }                    \tag{CM11}
\]
In particular its image is norm closed: a convergent sequence of image points is Cauchy; (CM11) and the explicit successive-unitary alignment in [the closed-orbit completeness proof](OA-FLOW-CINV.md#cinv-metric) produce a positive normal limit realizing its limit.

<a id="capp-resolvent"></a>
## 5. The resolvent cone is dense in the full subinvariant cone

This analytic step applies to any von Neumann algebra \(D\) with a spatial strongly continuous action \(\theta\). Its predual action is norm continuous: on vector functionals this follows from strong continuity of the implementing unitaries and the elementary vector-pair norm bound; truncate CP vector series to pass to every normal functional.

Write
\[
 P(D,\theta)=\{\chi\in D_*^+:
           \chi\theta_s\ge e^{-s}\chi\text{ for every }s\ge0\}.
\]
It is norm closed and invariant under every \(\theta_t\). For \(\eta\ge0\), the norm Bochner integral
\[
 R\eta=\int_0^\infty e^{-t}\eta\theta_{-t}\,dt                      \tag{CM12}
\]
exists, is positive and has mass \(\eta(1)\). Changing variables gives
\((R\eta)\theta_s\ge e^{-s}R\eta\); hence \(R(D_*^+)\subset P(D,\theta)\).

Let \(\chi\in P(D,\theta)\). Convolve its norm-continuous orbit with nonnegative smooth compactly supported approximate identities of integral one. The functionals \(\chi_n\) converge to \(\chi\) in norm and remain in \(P(D,\theta)\). They have norm differentiable orbits: differentiating the smooth kernel after changing variables gives the derivative. If \(A\) denotes that derivative at zero, positivity of
\((e^s\chi_n\theta_s-\chi_n)/s\), \(s>0\), and norm closedness of the positive cone show
\(\eta_n=\chi_n+A\chi_n\ge0\). The fundamental theorem of calculus in the Banach predual gives
\[
 \frac d{dt}\big(e^t\chi_n\theta_t\big)=e^t\eta_n\theta_t.
\]
The boundary term at \(-\infty\) has norm at most \(e^t\|\chi_n\|\) and vanishes. Integrating to zero proves \(\chi_n=R\eta_n\). Thus
\[
 \overline{R(D_*^+)}^{\,\|\cdot\|}=P(D,\theta).                    \tag{CM13}
\]

<a id="capp-range"></a>
## 6. Transfer of the entire range

Assume, in addition, that for every \(i\) the smaller-algebra image is the full cone \(P(Z(C_i),\theta)\). We show that the image for \(M\) is \(P(Z(C),\theta)\).

First extend any \(\eta\in Z(C)_*^+\) to a positive normal \(\Omega\in C_*^+\). Here is an explicit extension. Choose a faithful normal state \(\rho\) on \(C\). For \(x\ge0\), the finite measure
\(z\mapsto\rho(zx)\) on the abelian center is dominated by
\(\|x\|\rho|_{Z(C)}\). The scalar Radon–Nikodym construction DC05 therefore produces a unique \(E_Z(x)\in Z(C)_+\), bounded by \(\|x\|\), with
\(\rho(zE_Z(x))=\rho(zx)\) for central \(z\). Uniqueness gives additivity, central bimodularity and \(E_Z(z)=z\). For an increasing bounded positive net, normality of \(\rho\), followed by the faithful central pairing, proves that \(E_Z\) preserves its supremum. Hence \(E_Z\) is a normal positive unital map. Take \(\Omega=\eta E_Z\).

Put \(Y=R\Omega\in C_*^+\). Its restriction to \(Z(C)\) is \(R\eta\), and its restriction
\(\chi_i=Y|_{Z(C_i)}\) belongs to \(P(Z(C_i),\theta)\). By the assumed full range choose \(\phi_i\in(M_i)_*^+\) with \(\chi_{\phi_i}=\chi_i\), and set \(\psi_i=\phi_iE_i\). Equation (CM9) gives
\[
 \chi_{\psi_i}= (YF_i)|_{Z(C)}\longrightarrow
                  Y|_{Z(C)}=R\eta                              \tag{CM14}
\]
in norm, by (CM5). The already proved closedness of the image realizes \(R\eta\). Its closedness and (CM13) then realize every point of the full cone. Construction (CI15) supplies the reverse inclusion. We have proved
\[
 \boxed{\ \{\chi_\phi:\phi\in M_*^+\}=P(Z(C),\theta).\ }             \tag{CM15}
\]
Mass preservation in (CI6) restricts this to the corresponding assertion for states.

<a id="capp-iii-zero"></a>
## 7. Application to type III₀

For a separable-predual type III₀ factor, the preceding finite-block lesson supplies the actual \(M_i=F_i\) and \(E_i\) satisfying every part of (CM1), including predual norm convergence. Each \(F_i\) is a semifinite type II∞ nonfactor. The [semifinite distance theorem](OA-FLOW-CSAS.md#csas-distance) and [range construction](OA-FLOW-CSAS.md#csas-range) establish the full isometry and full range for precisely those algebras. Therefore (CM11) and (CM15) apply and prove both assertions for type III₀. Neither a factor-only theorem on the approximants nor a statement about state-space diameters would suffice.

The human antecedent is Haagerup–Størmer, [*Equivalence of Normal States on von Neumann Algebras and the Flow of Weights*](https://www.isibang.ac.in/~soumyashant/misc/collected-works-of-haagerup/1990s/1990_Equivalence_of_normal_states_on_von_Neumann_algebras_and_the_flow_of_weights.pdf), §§6–8, pp.215–234. The proof above keeps separate the normal core inclusion, the complete trace formula, supported densities, the varying-center norm limit and actual positive-functional realization.
