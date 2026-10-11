# Continuous decomposition and the modular spectrum

The following earlier programme argument is from OA-FLOW lesson 139, “Continuous decompositions, modular invariants, and canonical extensions”: the trace-scaling construction and equations (1)–(7), followed by the center-flow convention and the all-weight spectrum theorem, equations (10)–(18e). It supplies the exact type-theoretic input to [CAM-06–07](../OA-MOD-CAM.html#oa-mod-cam-06). The spectral intersection, dual-center kernel and crossed-product results used below retain their preceding OA-FLOW proofs and hypotheses. The circle eigenunitary construction and the centralizer-MASA construction are proved in CAM.

The newly written original programme expression is dedicated under CC0 1.0. The mathematical arguments and numbering below are retained from OA-FLOW; links to the current local OA-MOD cocycle, derivation and trace proofs identify the same results used there.

## The trace-scaling system and its crossed product

Let \(N\neq0\) be a von Neumann algebra, let \(\theta:\mathbb R\curvearrowright N\) be point-ultraweakly continuous, and let \(\tau\) be an n.s.f. trace such that

\[
 \tau\circ\theta_s=e^{-s}\tau . \tag{1}
\]

Put

\[
 P=N\rtimes_\theta\mathbb R, \qquad
 u(s)xu(s)^*=\theta_s(x). \tag{2}
\]

Our dual convention is

\[
 \widehat\theta_t(x)=x,\qquad
 \widehat\theta_t(u(s))=e^{-its}u(s). \tag{3}
\]

The dual weight \(\Phi\) of \(\tau\) has

\[
 \sigma_t^\Phi=\widehat\theta_t,\qquad P_\Phi=N. \tag{4}
\]

The center and type test proved in the trace-scaling lesson read

\[
 Z(P)=Z(N)^\theta. \tag{5}
\]

Moreover \(P\) is properly infinite. It is type III exactly when there is no nonzero \(e\in\operatorname{Proj}(Z(N)^\theta)\) and normal injective homomorphism \(j:L^\infty(\mathbb R)\to Z(N)e\), unital with respect to \(e\), intertwining translation with \(\theta\). The range must lie in the center of the corner. A translation algebra merely contained in \(Ne\) does not give this type test; every continuous core has the generally noncentral group algebra with its dual translation action. That last exclusion matters: the scalar translation system satisfies (1), but its crossed product is \(B(L^2\mathbb R)\), hence semifinite.

## Existence of a continuous decomposition

**Theorem.** Every type III von Neumann algebra \(P\) is isomorphic to a crossed product (2) for a trace-scaling system satisfying (1). The algebra \(N\) may be chosen of type \({\rm II}_\infty\).

**Proof.** A properly infinite von Neumann algebra absorbs \(B(L^2\mathbb R)\). Choose a stable representative \(P_0\) and an n.s.f. weight \(\varphi\) on it. Form its modular crossed product

\[
 N=C_\varphi(P_0)=P_0\rtimes_{\sigma^\varphi}\mathbb R. \tag{6}
\]

The core construction supplies an n.s.f. trace \(\tau_\varphi\) and the dual action \(\theta\), with \(\tau_\varphi\theta_s=e^{-s}\tau_\varphi\). Duality gives

\[
 N\rtimes_\theta\mathbb R
 \cong P_0\,\bar\otimes B(L^2\mathbb R)
 \cong P. \tag{7}
\]

The algebra \(N\) is semifinite by construction. Apply the type-reduction corollary in trace-scaling structure (OA-FLOW, `18-trace-scaling-structure.md`): the complement of its type \({\rm II}_\infty\) part has an automorphism-natural center-valued trace. Factoring \(\tau\) through that trace gives a scaled weight on the center. The central eigenunitary theorem then supplies a translation subsystem, and the semifinite-corner criterion makes the corresponding central corner of (7) semifinite. Since \(P\) is type III, that complement is zero. Hence \(N\) is of type \({\rm II}_\infty\). The center-valued trace and eigenunitary prerequisites of that corollary remain in force; trace scaling alone does not exclude a finite coefficient algebra. \(\square\)

The decomposition includes the action. Remembering only the semifinite algebra \(N\) discards the invariant that distinguishes the type III subtypes.

## Associated system, modulus, and center flow

For a type III algebra \(P\), a system \((N,\theta)\) supplied by the preceding theorem is its **associated trace-scaling system**, and (2) is its **continuous decomposition**. If an automorphism \(\beta\) of a semifinite algebra scales an n.s.f. trace by

\[
 \tau\beta=c\tau,\qquad c>0, \tag{10}
\]

we use

\[
 \operatorname{mod}(\beta)=c^{-1}. \tag{11}
\]

Thus \(\operatorname{mod}(\theta_s)=e^s\) under (1). The restriction

\[
 (Z(N),\mathbb R,\theta|_{Z(N)}) \tag{12}
\]

is the **flow of weights**. Its conjugacy class depends only on \(P\). This is proved in OA-FLOW lesson 139, “Why the decomposition is unique,” equations (8)–(9), using the intrinsic-core comparison. This selection uses the chosen system in (12). By (5), \(P\) is a factor precisely when this center flow is ergodic:

\[
 Z(N)^\theta=\mathbb C1. \tag{13}
\]

Ergodicity does not say that \(Z(N)\) itself is trivial. A periodic ergodic flow and a trivial flow lead to different types below.

## The three type III subtypes

Assume now that \(P\) is a factor. Let

\[
 K=\{s\in\mathbb R:\theta_s|_{Z(N)}=\operatorname{id}\}. \tag{14}
\]

It is a closed subgroup of \(\mathbb R\). The subtype is read from \(K\) and the carrier of the flow as follows.

1. If the center flow has least positive period \(T\), put \(\lambda=e^{-T}\). Then \(P\) is type \({\rm III}_\lambda\), where \(0<\lambda<1\).
2. If \(K=\{0\}\) and the center is nontrivial, then \(P\) is type \({\rm III}_0\).
3. If \(Z(N)=\mathbb C1\), so that the flow is trivial and \(K=\mathbb R\), then \(P\) is type \({\rm III}_1\).

The qualification about the carrier in the second and third clauses is essential: both a faithful aperiodic flow and a trivial flow can be described informally as having “no positive period,” but only the former is type \({\rm III}_0\).

## Modular spectrum from the kernel of the center flow

For a factor \(P\), define its modular spectrum by

\[
 S(P)=\bigcap_\psi \operatorname{Sp}(\Delta_\psi), \tag{15}
\]

where \(\psi\) runs through all n.s.f. weights and \(\Delta_\psi\) is the modular operator in the standard representation. Then

\[
 S(P)=\{0\}\cup\exp K. \tag{16}
\]

**Proof.** Write \(\alpha=\sigma^\Phi\). The dual-center kernel theorem identifies

\[
 \Gamma(\alpha)=K. \tag{17}
\]

We now connect this action invariant with **all** the weights in (15). Three earlier results have the required arbitrary-predual scope.

* The [invariant-weight spectrum theorem MSP-01–02](../OA-MOD-MSP.html#oa-mod-msp-01) identifies the Fourier annihilator of a weight-preserving real action with that of its GNS implementation. It proves strong continuity and the full GNS-domain filter identity from the local Hilbert-algebra construction; compare OA-FLOW lesson 100, (W8)–(W16). For \(\sigma^\psi\), the implementation is \(\Delta_\psi^{it}\). Spectral calculus therefore gives

  \[
\operatorname{Sp}(\sigma^\psi)
    =\operatorname{Sp}(\log\Delta_\psi)
    =\log\bigl(\operatorname{Sp}(\Delta_\psi)\setminus\{0\}\bigr).
    \tag{18a}
\]

  Indeed a finite real point \(r\) lies outside the spectrum of \(\log\Delta_\psi\) exactly when an interval around \(r\) has zero spectral projection; its exponential is an interval around \(e^r>0\) with the same projection. This local argument makes no assertion that the exponential of an unbounded spectrum is closed at zero.
* Every n.s.f. \(\psi\) gives the strongly continuous unitary \(\alpha\)-cocycle \(u_t=[D\psi:D\Phi]_t\), with \(\sigma_t^\psi=\operatorname{Ad}(u_t)\alpha_t\). Conversely **every** such unitary cocycle is the derivative of an n.s.f. weight on \(P\). The exact written prerequisite is OA-MOD CX-01–CX-10, especially (CX.41)–(CX.54), in [weight-cocycle reconstruction](../OA-MOD-CX.html#oa-mod-cx-10); its full finite GNS construction and two-coordinate relative graph are summarized under “The unitary converse and its actual graph” in the conventions guide (OA-FLOW, `01-contracts.md`). No faithful-state reduction, finite total mass, or bounded analytic continuation of the cocycle is imposed.
* The cocycle spectral intersection theorem (OA-FLOW, `120-cocycle-spectral-intersection-in-the-sigma-finite-case.md`), (C4), (C25a)–(C26) and (C29), holds at arbitrary cardinality. The action \(\alpha\) is centrally ergodic because \(P\) is a factor. It follows that

  \[
\Gamma(\alpha)
     =\bigcap_{u\in Z^1_\alpha(\mathbb R,P)}
        \operatorname{Sp}(\operatorname{Ad}(u)\alpha).
     \tag{18b}
\]

For the first inclusion, fix any n.s.f. \(\psi\). Cocycle invariance of the Connes spectrum for factors, proved in [MSP-03](../OA-MOD-MSP.html#oa-mod-msp-03) from the local fixed-corner theorem, gives

\[
\Gamma(\alpha)=\Gamma(\sigma^\psi)
   \subseteq\operatorname{Sp}(\sigma^\psi).
   \tag{18c}
\]

Equation (18a) therefore puts every \(e^r\), \(r\in\Gamma(\alpha)\), in \(\operatorname{Sp}(\Delta_\psi)\). Intersecting over \(\psi\) proves \(\exp\Gamma(\alpha)\subseteq S(P)\setminus\{0\}\).

For the reverse inclusion, let \(a>0\) belong to every modular-operator spectrum and put \(r=\log a\). For an arbitrary unitary cocycle \(u\), reconstruct its weight \(\psi_u\) by CX-10. Then (18a) puts \(r\) in \(\operatorname{Sp}(\operatorname{Ad}(u)\alpha)\). Equation (18b) puts it in \(\Gamma(\alpha)\). Thus

\[
 S(P)\setminus\{0\}=\exp\Gamma(\sigma^\Phi)=\exp K. \tag{18}
\]

The corner step in (18b) is an actual amplification, not an inference from full central support. For clarity, its properly infinite factor case works as follows. If \(0\ne e\in P^\alpha\) and \(e\sim1\), (C6)–(C11) transports the reduced action using an isometry. Otherwise the local cardinal lemma gives the homogeneous cardinal \(\kappa\) of \(1\), proves that of \(1-e\) is also \(\kappa\), and works in \(A=P\bar\otimes B(\ell^2(I))\), \(|I|=\kappa\). Put \(p=e\otimes1\), \(q=1\otimes e_{00}\) and \(b=e\otimes e_{00}\). Equations (C25d)–(C25e) construct a partial isometry \(v\) with \(v^*v=p\), \(vv^*=q\) and \(vb=bv=b\), by comparing \(p-b\) and \(q-b\) at their actual homogeneous cardinals. Hence the transported action from \(ePe\bar\otimes B(\ell^2(I))\) agrees with \(\alpha\) on the full common corner \(bAb\). The full-corner theorem of lesson 117 (OA-FLOW, `117-lifting-innerness-and-cocycles-from-a-full-corner.md`) gives a unitary cocycle on \(P\). Every Fourier filter acts on the matrix entries of the amplification, and finite matrix compressions separate the operators; its spectrum is exactly \(\operatorname{Sp}(\alpha^e)\). This proves the cornerwise containment needed in (18b), even if \(ePe\) itself is not isomorphic to \(P\). The normal projection-comparison prerequisites of the earlier cardinal lemma remain in force.

It remains to include zero for **each** n.s.f. \(\psi\). Suppose \(\Delta_\psi\) were bounded. The closed-operator identity \(J_\psi\Delta_\psi J_\psi=\Delta_\psi^{-1}\) would also make its inverse bounded. Thus \(L=\log\Delta_\psi\) is bounded self-adjoint on the entire GNS space. In the faithful GNS representation,

\[
d(x)=\lim_{t\to0}\frac{\sigma_t^\psi(x)-x}{t}
       =i[L,x]\in P,\qquad \|d\|\le2\|L\|.
       \tag{18d}
\]

The norm limit belongs to the norm-closed algebra \(P\), and the product and adjoint rules make \(d\) a bounded star derivation. The internally proved [innerness theorem](../OA-MOD-BI.html#oa-mod-bi-08), (GI.2), supplies a bounded self-adjoint \(h\in P\) with \(d=i[h,\cdot]\). Both norm-continuous groups have this bounded generator, so \(\sigma_t^\psi=\operatorname{Ad}(e^{ith})\): differentiating \(e^{-td}\sigma_t^\psi(x)\) identifies it with \(e^{td}x\), and does the same for the internal group. In particular \(h\in P_\psi\).

Set \(a=e^{-h}\), a bounded invertible positive element of \(P_\psi\). The exact earlier bounded-density construction OA-MOD CZ-07 and CZ-10, (CZ.24), (CZ.34)–(CZ.38), constructs the n.s.f. weight

\[
\eta(x)=\psi(a^{1/2}xa^{1/2}),\qquad
  \sigma_t^\eta=\operatorname{Ad}(e^{-ith})\sigma_t^\psi
               =\operatorname{id}. \tag{18e}
\]

The whole-positive trace criterion is OA-MOD VR-01, (VR.2)–(VR.3), in [inner flow and weight rigidity](../OA-MOD-VR.html#oa-mod-vr-01). It proves \(\eta(y^*y)=\eta(yy^*)\) for every bounded \(y\): the constant-orbit right multiplier formula applies to the polar decomposition whenever one value is finite; applying the same argument to \(y^*\) treats the other finite case, and otherwise both are infinite. Thus \(\eta\) is a faithful normal semifinite trace. This is impossible on a nonzero type III factor. Therefore every \(\Delta_\psi\) is unbounded.

Its positive spectrum has arbitrarily large points. The same modular-conjugation identity gives their positive reciprocals in its spectrum, tending to zero. Closedness of \(\operatorname{Sp}(\Delta_\psi)\) gives \(0\in\operatorname{Sp}(\Delta_\psi)\) for every \(\psi\). Together with (17)–(18) this proves (16). \(\square\)

For \(K=T\mathbb Z\), (16) gives \(\{0\}\cup\lambda^\mathbb Z\); for \(K=\{0\}\), it gives \(\{0,1\}\); and for \(K=\mathbb R\), it gives \([0,\infty)\). These are exactly the three cases above.
