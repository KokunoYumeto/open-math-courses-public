# Canonical L2 and standard implementations

A standard Hilbert space can be defined from all faithful normal semifinite weights at once. Each weight supplies coordinates for the same vectors, with unique comparison unitaries relating the coordinates. We construct that space and its positive cone, specify the topology of its automorphism action, and realize a nonfaithful weight on its full GNS space.

Research antecedents are Uffe Haagerup's [*The standard form of von Neumann algebras*](https://doi.org/10.7146/math.scand.a-11606), Sections 2–3, especially Theorem 2.3, Lemma 2.10, Theorem 3.2 and Proposition 3.5, and Fumio Hiai's [*Concise lectures on selected topics of von Neumann algebras*, arXiv:2004.02383v1](https://arxiv.org/abs/2004.02383v1), Sections 3.2 and 7.1. Haagerup proves comparison and implementation in arbitrary cardinality; Hiai's displayed comparison proof is sigma-finite, and his weight Hilbert-algebra setup expressly omits its underlying proofs. The complete existing SF/SE/CW/CZ providers supply our full stated inputs. The four preceding arguments are retained; the coordinate, nonfaithful and finite-domain proofs and solved examples are independently written course exposition by OpenAI Codex (AI), October2026, under CC0.

## The precise topology of a standard implementation

Let \((M,H,J,P)\) be a standard form of an arbitrary von Neumann algebra. Equip \(\operatorname{Aut}(M)\) with the **u-topology**: a net \((\alpha_i)\) converges to \(\alpha\) when

\[
 \|f\circ\alpha_i-f\circ\alpha\|\longrightarrow0
 \qquad(f\in M_*).
 \tag{CL.1}
\]

The norm here is the norm of the Banach predual. The index set is arbitrary.

This definition already implies the corresponding convergence of inverse automorphisms. Composition with an automorphism is an isometry of the predual, so

\[
 \|f\circ\alpha_i^{-1}-f\circ\alpha^{-1}\|
 =\|f-f\circ\alpha^{-1}\circ\alpha_i\|\longrightarrow0.
 \tag{CL.2}
\]

For the last limit apply (CL.1) to the fixed functional \(f\circ\alpha^{-1}\). Thus the topology requiring both forward and inverse predual convergence in the existing standard-implementation proof is precisely the u-topology, with no additional convergence hypothesis.

The unitary group associated with the standard form is

\[
 \mathcal U_{\mathrm{std}}
 =\{u\in\mathcal U(H):uMu^*=M,\ uJu^*=J,\ uP=P\}.
 \tag{CL.3}
\]

The comparison theorem in the proof for arbitrary standard forms, together with its automorphism consequence, gives a unique \(U(\alpha)\in\mathcal U_{\mathrm{std}}\) implementing each automorphism. Unitary conjugation is normal because it preserves bounded increasing positive suprema. Conversely every member of (CL.3) implements an automorphism. Uniqueness gives

\[
 U(\alpha\beta)=U(\alpha)U(\beta),\qquad
 U(\alpha)^{-1}=U(\alpha^{-1}),\qquad
 U(\alpha)\xi_f=\xi_{f\circ\alpha^{-1}}
 \quad(f\in M_*^+).
 \tag{CL.4}
\]

Here \(\xi_f\) is the unique vector in \(P\) representing \(f\). The condition involving \(J\) follows already from preservation of \(P\): both \(J\) and \(uJu^*\) fix every vector of \(P\), and this cone has dense complex span. Antilinearity then makes the two operators equal on that span and hence on \(H\).

The map \(\alpha\mapsto U(\alpha)\) is a homeomorphism from the u-topology onto \(\mathcal U_{\mathrm{std}}\) with its strong operator topology. The full existing proofs are SF-12 and SE-11; the following argument identifies their hypotheses with (CL.1). The cone estimates in the norm-topology theorem and their transport to any standard form give

\[
 \|\xi_f-\xi_g\|^2\le\|f-g\|,\qquad
 \|\omega_\xi-\omega_\eta\|
 \le(\|\xi\|+\|\eta\|)\|\xi-\eta\|.
 \tag{CL.5}
\]

By (CL.2), u-convergence gives convergence of (CL.4) on every cone vector. The cone has dense complex span and all implementers have norm one, so approximation proves strong convergence on all of \(H\).

Conversely, suppose \(U(\alpha_i)\to U(\alpha)\) strongly. The limit is a unitary in the stated target group. For each \(\eta\in H\),

\[
 \|(U(\alpha_i)^*-U(\alpha)^*)\eta\|
 =\|\eta-U(\alpha_i)U(\alpha)^*\eta\|\longrightarrow0.
 \tag{CL.6}
\]

Use (CL.4) and the second estimate in (CL.5), first for positive normal functionals, with the inverse implementers to obtain (CL.1). The decomposition of an arbitrary normal functional into a linear combination of positive normal functionals completes the argument. Products and inverses of unitaries are continuous in this topology: for products use
\(\|(u_i v_i-uv)\eta\|\le\|(v_i-v)\eta\|+\|(u_i-u)v\eta\|\), and for inverses use (CL.6). This proves the asserted topological group isomorphism.

These conclusions include infinite algebras, nonseparable Hilbert spaces and arbitrary nets. They use finite normal functionals as tests and do not represent an infinite weight by a single Hilbert-space vector.

## Coherent weight coordinates define canonical L2

Let \(\mathcal W_0(M)\) be the set of faithful normal semifinite weights on \(M\). It is nonempty by the existence theorem for weights. For \(\varphi\in\mathcal W_0(M)\), let
\((\pi_\varphi(M),H_\varphi,J_\varphi,P_\varphi)\) be its standard form.

Write \(I_{\psi\leftarrow\varphi}:H_\varphi\to H_\psi\) for the unique comparison unitary. The complete proof in the comparison of natural cones gives the represented-algebra and cone identities, together with

\[
 \begin{aligned}
 I_{\chi\leftarrow\psi}I_{\psi\leftarrow\varphi}
   &=I_{\chi\leftarrow\varphi},\\
 I_{\varphi\leftarrow\varphi}&=1,\\
 I_{\psi\leftarrow\varphi}J_\varphi
   &=J_\psi I_{\psi\leftarrow\varphi}.
 \end{aligned}
 \tag{CL.7}
\]

Define

\[
 L^2(M)=
 \{(\xi_\varphi)_{\varphi\in\mathcal W_0(M)}:
       \xi_\psi=I_{\psi\leftarrow\varphi}\xi_\varphi
       \text{ for every }\psi,\varphi\}.
 \tag{CL.8}
\]

Coordinatewise addition and scalar multiplication preserve the compatibility condition. For any fixed weight \(\varphi\), define

\[
 \langle\xi,\eta\rangle
   =\langle\xi_\varphi,\eta_\varphi\rangle_{H_\varphi}.
 \tag{CL.9}
\]

Unitarity of all comparisons makes this independent of the selected weight. A family with norm zero has every coordinate zero, so this is an inner product. Its first variable is linear.

Evaluation \(E_\varphi:L^2(M)\to H_\varphi\) is a surjective isometry. Indeed a vector \(v\in H_\varphi\) determines the family
\((I_{\psi\leftarrow\varphi}v)_\psi\), whose compatibility follows from (CL.7); its \(\varphi\)-coordinate is \(v\). Conversely every compatible family has this form. Completeness of \(H_\varphi\) therefore proves completeness of \(L^2(M)\). No summability over the set of weights is required.

Define the left action, conjugation and positive cone by

\[
 \begin{aligned}
 (x\xi)_\varphi&=\pi_\varphi(x)\xi_\varphi,\\
 (J\xi)_\varphi&=J_\varphi\xi_\varphi,\\
 L^2(M)_+&=\{\xi:\xi_\varphi\in P_\varphi\ (\forall\varphi)\}.
 \end{aligned}
 \tag{CL.10}
\]

The algebra and conjugation intertwining identities make these compatible families. Membership in the cone can be checked in any one coordinate because the comparisons map the cones onto one another. Evaluation carries (CL.10) onto the complete standard form associated with \(\varphi\). In particular the left action is faithful and normal, \(J\) is an antiunitary involution, the cone is closed and self-dual, and the standard-form axioms hold. This proves the canonical standard-form construction at its full generality.

The standard GNS map for a faithful weight is

\[
 \eta_\varphi(x)=E_\varphi^{-1}\Lambda_\varphi(x),
 \qquad x\in\mathfrak n_\varphi.
 \tag{CL.11}
\]

It has dense range, obeys
\(\|\eta_\varphi(x)\|^2=\varphi(x^*x)\), and satisfies
\(a\eta_\varphi(x)=\eta_\varphi(ax)\).
All of the original finite left ideal is retained. Evaluation in another coordinate gives
\(E_\psi\eta_\varphi(x)=I_{\psi\leftarrow\varphi}\Lambda_\varphi(x)\), exactly the common-GNS map already proved in the domain-sensitive transport theorem. Thus the canonical construction realizes that theorem without selecting a permanent reference weight.

Standard implementations also act canonically. Let \(u_\alpha^\varphi\) be the implementer on \(H_\varphi\). The operators
\(I_{\psi\leftarrow\varphi}u_\alpha^\varphi\) and
\(u_\alpha^\psi I_{\psi\leftarrow\varphi}\) implement the same automorphism and map the same source cone onto the same target cone. Comparison uniqueness makes them equal. Consequently
\((U(\alpha)\xi)_\varphi=u_\alpha^\varphi\xi_\varphi\) defines a unitary on (CL.8), with the group and topology properties of CL-01. The full GNS transport formula is

\[
 U(\alpha)\eta_\varphi(x)
   =\eta_{\varphi\circ\alpha^{-1}}(\alpha(x)),
 \qquad
 \mathfrak n_{\varphi\circ\alpha^{-1}}
       =\alpha(\mathfrak n_\varphi).
 \tag{CL.12}
\]

The domain equality is the weight-pullback theorem. The formula is SF-13 transported through the evaluation unitaries. Positive normal functional vectors transform as in (CL.4). The zero algebra gives the zero Hilbert space, zero cone and trivial automorphism group throughout.

## A nonfaithful weight occupies its full right-support space

Let \(\psi\) be any normal semifinite weight on \(M\), with support \(e\). The support-compression theorem says that \(\psi(x)=\psi(exe)\) for \(x\ge0\), and that its restriction to \(eMe\) is faithful normal semifinite. Choose a faithful normal semifinite weight on the complementary corner \((1-e)M(1-e)\). Completing the two complementary corners gives a faithful normal semifinite weight \(\varphi\) on \(M\) such that

\[
 \begin{aligned}
 \psi(x)&=\varphi(exe)\quad(x\in M_+),\\
 e&\in M_\varphi.
 \end{aligned}
 \tag{CL.13}
\]

The zero-corner conventions are included in that theorem. Thus every \(\psi\) has such a completion; \(\psi\) need not be finite at \(1\). The completion is an auxiliary choice, whose weight and centralizer properties are proved in the corner-completion theorem cited above.

In canonical coordinates put \(R_e=JeJ\). This is an orthogonal projection in \(M'\). Since \(e\) is fixed by the modular group of \(\varphi\), its entire orbit is constant. The full finite-domain multiplier identity in the centralizer theorem, equation (CZ.3), gives

\[
 \begin{aligned}
 xe&\in\mathfrak n_\varphi,\\
 \eta_\varphi(xe)&=R_e\eta_\varphi(x)
 \\ &\quad(x\in\mathfrak n_\varphi).
 \end{aligned}
 \tag{CL.14}
\]

In particular
\(\varphi(ex^*xe)\le\varphi(x^*x)\) on that domain.
This is a bounded right-multiplication assertion on the full finite left ideal.

For an arbitrary \(x\in M\), (CL.13) shows that

\[
 \begin{aligned}
 x\in\mathfrak n_\psi
       &\ \Longleftrightarrow\ xe\in\mathfrak n_\varphi,\\
 \eta_\psi(x)&:=\eta_\varphi(xe).
 \end{aligned}
 \tag{CL.15}
\]

The squared norm of this vector is \(\psi(x^*x)\). Polarization gives the entire GNS inner product for every pair \(x,y\in\mathfrak n_\psi\); therefore (CL.15) factors through the GNS null space and is isometric on that quotient. Left multiplication is preserved:
\(a\eta_\psi(x)=\eta_\psi(ax)\).

We check its range, rather than assuming a support-corner identification. If \(x\in\mathfrak n_\psi\), then \(xe\in\mathfrak n_\varphi\), and applying (CL.14) to \(xe\) gives
\(R_e\eta_\varphi(xe)=\eta_\varphi(xe)\).
Thus the range is contained in \(R_eL^2(M)\).
Conversely \(\mathfrak n_\varphi\subseteq\mathfrak n_\psi\) by (CL.14), and

\[
 \begin{gathered}
 \eta_\psi(\mathfrak n_\varphi)
       =R_e\eta_\varphi(\mathfrak n_\varphi)\\
 \text{is dense in }R_eL^2(M).
 \end{gathered}
 \tag{CL.16}
\]

The density follows from the dense range of \(\eta_\varphi\) and boundedness of the projection \(R_e\). Completion of the GNS quotient now identifies the **full GNS Hilbert space of \(\psi\)** with \(JeJ\,L^2(M)\), as a reducing space for the left action of the whole algebra \(M\).

The faithful corner restriction has a different space. Restricting the domain to \(eMe\) gives vectors \(\eta_\varphi(exe)\); their closure is
\(eJeJ\,L^2(M)\). To see density, apply the bounded projection \(eR_e\) to the dense set \(\eta_\varphi(\mathfrak n_\varphi)\), and use
\(eR_e\eta_\varphi(x)=\eta_\varphi(exe)\).
The standard-form corner theorem supplies its conjugation and positive cone. These are the GNS coordinates for the faithful weight on \(eMe\). The whole-algebra GNS space in (CL.16) may be strictly larger.

The map in (CL.15) is independent of the completion. To prove this, let \(\varphi_1,\varphi_2\) be two completions. On the corner \(eMe\) they have the same faithful weight \(\psi|_{eMe}\). The GNS isometry sending \(\eta_{\varphi_1}(z)\) to \(\eta_{\varphi_2}(z)\) for \(z\) in that corner's finite left ideal extends to a unitary on \(eR_eL^2(M)\). It intertwines left multiplication and the closed finite-star involutions, so polar uniqueness and the natural-cone construction make it preserve the corner conjugation and cone. The standard-form and modular-corner results SE-02 and CZ-09 identify these with the inherited corner data. Uniqueness in SE-10 therefore makes this unitary the identity. The two GNS maps agree on the full corner finite left ideal.

We also need density after allowing left multiplication by the whole algebra. Put

\[
 K=\overline{M\,eR_eL^2(M)}.
 \tag{CL.16a}
\]

This is a reducing subspace for \(M\), contained in \(R_eL^2(M)\), so its orthogonal projection \(p_K\) belongs to \(M'\) and satisfies \(p_K\le R_e\). Since \(eR_eL^2(M)\subset K\), the projection \(q=R_e-p_K\) obeys \(qe=0\). Thus \(r=JqJ\in M\) satisfies \(r\le e\) and \(rR_e=0\). If \(r\ne0\), normal positive separation gives a nonzero positive normal functional supported in \(r\). Its cone representative \(\xi\ne0\), supplied by SE-11, satisfies \(r\xi=\xi\) and \(J\xi=\xi\). As \(e\ge r\), we get \(R_e\xi=JeJ\xi=\xi\), contradicting \(rR_e=0\). Hence \(q=0\) and \(K=R_eL^2(M)\).

The two whole-algebra GNS realizations of \(\psi\) define a unitary \(W\) on \(R_eL^2(M)\) by
\(W\eta_{\varphi_1}(xe)=\eta_{\varphi_2}(xe)\), \(x\in\mathfrak n_\psi\).
It commutes with the left action of \(M\), and the corner argument makes it fix the dense corner GNS set. It therefore fixes \(M eR_eL^2(M)\) and, by (CL.16a), every vector of \(R_eL^2(M)\). Thus \(W=1\), proving independence on every vector in the full domain (CL.15), including the zero-weight case.

## Three coordinate checks with complete solutions

**Problem 1: an uncountable diagonal algebra.** Let \(I\) be any set and \(M=\ell^\infty(I)\). Use the faithful counting weight
\(\varphi(x)=\sup_{F\subset I,\ F\text{ finite}}\sum_{i\in F}x_i\) for \(x\ge0\). Identify the canonical standard form, and characterize u-convergence to the identity for automorphisms induced by permutations of \(I\).

**Solution.** The GNS map is \(x\mapsto(x_i)\) on those bounded functions with \(\sum_i|x_i|^2<\infty\), and its completion is \(\ell^2(I)\). Finite-support vectors are dense: for any square-summable vector and any error, a finite partial sum captures all but that squared-norm error. No enumeration of \(I\) is required. The standard conjugation is coordinatewise complex conjugation, the cone consists of nonnegative coordinates, and the left action is multiplication. Each \(a\in\ell^1(I)_+\) has cone vector \((\sqrt{a_i})_i\). CL-02 identifies this standard form with canonical \(L^2(M)\).

For a permutation \(\tau\), set \(\alpha_\tau(x)_i=x_{\tau^{-1}(i)}\). The implementer is
\((U(\alpha_\tau)\xi)_i=\xi_{\tau^{-1}(i)}\).
A net \(\tau_j\) converges to the identity in the u-topology exactly when, for each \(i\in I\), \(\tau_j(i)=i\) eventually. Strong convergence applied to the unit vector at \(i\) proves necessity, because its displacement has norm either zero or \(\sqrt2\). For sufficiency, finitely many coordinates can be fixed at one common eventual net index; on their span the implementer is the identity. Approximate an arbitrary vector by that finite span and use the norm-one bound. CL-01 then gives u-convergence. This argument works for an uncountable \(I\) and for nets without a countable cofinal subset.

**Problem 2: the entire GNS space has two dimensions.** Take \(M=M_2(\mathbb C)\), \(h=\operatorname{diag}(2,5)\), \(\varphi(x)=\operatorname{Tr}(hx)\), and \(e=E_{11}\). Determine both GNS spaces in CL-03.

**Solution.** Use the Hilbert–Schmidt standard form, with left matrix multiplication, \(J\xi=\xi^*\), and the positive matrix cone. Its GNS coordinates are
\(\eta_\varphi(x)=xh^{1/2}\).
The projection \(e\) centralizes \(\varphi\), and \(R_e\xi=\xi e\). The nonfaithful weight and its GNS map are

\[
 \begin{aligned}
 \psi(x)&=2x_{11}\quad(x\ge0),\\
 \eta_\psi(x)&=\sqrt2
   \begin{pmatrix}x_{11}&0\\x_{21}&0\end{pmatrix},\\
 \|\eta_\psi(x)\|_{\mathrm{HS}}^2&\\
       &=2(|x_{11}|^2+|x_{21}|^2).
 \end{aligned}
 \tag{CL.17}
\]

The full GNS space is the two-dimensional column space \(R_e\mathrm{HS}_2\), on which the whole algebra acts by left multiplication. The faithful corner \(eMe\) has the one-dimensional space \(eR_e\mathrm{HS}_2=\mathbb C E_{11}\). Both spaces have the claimed ranges; their dimensions cannot be identified.

**Problem 3: a support projection need not centralize a chosen reference.** Keep the preceding \(h\), but let \(e\) be the projection onto \((1,1)\). Explain why the formula \(\eta_\varphi(xe)=JeJ\eta_\varphi(x)\) cannot be used with this reference.

**Solution.** Here

\[
 \begin{aligned}
 e&=\frac12\begin{pmatrix}1&1\\1&1\end{pmatrix},\\
 \eta_\varphi(e)&=\frac12
       \begin{pmatrix}\sqrt2&\sqrt5\\\sqrt2&\sqrt5\end{pmatrix},\\
 R_e\eta_\varphi(1)&=\frac12
       \begin{pmatrix}\sqrt2&\sqrt2\\\sqrt5&\sqrt5\end{pmatrix}.
 \end{aligned}
 \tag{CL.18}
\]

The two matrices differ because \(\sqrt2\ne\sqrt5\). Indeed \(e\) does not commute with \(h\), so it is not in this reference weight's centralizer. CL-03 first chooses a faithful diagonal completion for the given supported weight; that step supplies precisely the missing hypothesis.

## Infinite weights and their finite-energy domains

Let \(\psi\) be a normal semifinite weight on \(M\), let \(e=s(\psi)\), and use the canonical standard form of CL-02. The construction in CL-03 defines the completion-independent map

\[
 \begin{aligned}
 \mathcal L_\psi:\mathfrak n_\psi&\longrightarrow JeJ\,L^2(M),\\
 x\psi^{1/2}&:=\mathcal L_\psi(x)=\eta_\psi(x),\\
 \mathfrak n_\psi&=\{x\in M:\psi(x^*x)<\infty\}.
 \end{aligned}
 \tag{CL.19}
\]

The symbol on the left of the second line denotes the value of this map. It does not first posit a vector \(\psi^{1/2}\) to which a bounded operator is applied.

The finite-domain results Domain algebra and its positive cone through The GNS construction for an arbitrary weight and CL-03 give, for \(x,y\in\mathfrak n_\psi\) and \(a\in M\),

\[
 \begin{aligned}
 \langle x\psi^{1/2},y\psi^{1/2}\rangle
     &=\widetilde\psi(y^*x),\\
 \|x\psi^{1/2}\|^2&=\psi(x^*x),\\
 (ax)\psi^{1/2}&=a(x\psi^{1/2}),\\
 \|(ax)\psi^{1/2}\|&\le\|a\|\,\|x\psi^{1/2}\|.
 \end{aligned}
 \tag{CL.20}
\]

Here \(ax\in\mathfrak n_\psi\), and \(y^*x\in\mathfrak m_\psi\), so every term is defined. The finite linear extension \(\widetilde\psi\) is used only on its stated domain. The map is complex linear, and its range is dense in \(JeJ\,L^2(M)\). It does not discard the nonfaithful weight's full GNS space.

Its null ideal is exactly \(M(1-e)\). Indeed support compression gives
\(\psi(x^*x)=\psi(ex^*xe)\). The restricted weight is faithful on \(eMe\). Thus this number is zero exactly when
\(ex^*xe=(xe)^*(xe)=0\), or \(xe=0\). This is equivalent to \(x=x(1-e)\). All such \(x\) belong to the finite left ideal. This also proves the assertion for the zero weight, when \(e=0\), the domain is all \(M\), and the map has zero range.

Suppose first that \(\psi(1)<\infty\). The inequality
\(\psi(x^*x)\le\|x\|^2\psi(1)\) shows that \(\mathfrak n_\psi=M\). Set
\(\xi_\psi=\eta_\psi(1)\). This is the natural-cone representative of the bounded positive normal functional \(\psi\):

\[
 \begin{aligned}
 \xi_\psi&\in L^2(M)_+,\\
 \|\xi_\psi\|^2&=\psi(1),\\
 \psi(a)&=\langle a\xi_\psi,\xi_\psi\rangle
          \quad(a\in M),\\
 x\psi^{1/2}&=x\xi_\psi\quad(x\in M).
 \end{aligned}
 \tag{CL.21}
\]

For the cone assertion, take the same faithful diagonal completion \(\varphi\) used in CL-03. Then
\(\eta_\psi(1)=\eta_\varphi(e)\). The proof in Every normal positive functional has a cone vector proves that this vector belongs to the completion's natural cone and represents \(\psi\). Transport through the evaluation unitary in CL-02 gives (CL.21); cone uniqueness removes the auxiliary completion. The last identity is the module rule in (CL.20). By standard-form uniqueness, this is also the positive-root notation used in the intrinsic root construction.

For infinite mass, no vector in \(L^2(M)\) can represent the same module map. Here is the domain argument. Finite positive cutoffs characterize semifiniteness supplies increasing positive contractions \(b_i\) with
\(\psi(b_i)<\infty\) and \(b_i\uparrow1\). Put \(x_i=b_i^{1/2}\). Functional calculus and normality give

\[
 \begin{aligned}
 x_i&\in\mathfrak n_\psi,\qquad\|x_i\|\le1,\\
 \|\eta_\psi(x_i)\|^2&=\psi(b_i)
       \uparrow\psi(1).
 \end{aligned}
 \tag{CL.22}
\]

The \(b_i\) need not be projections; no directedness of finite-weight projections is assumed. If \(\psi(1)=\infty\) and there were \(\zeta\in L^2(M)\) with
\(\eta_\psi(x)=x\zeta\) for every \(x\in\mathfrak n_\psi\), then (CL.22) would be bounded above by \(\|\zeta\|^2\). This contradicts normality.

The same proof gives the exact extended operator-norm bound for this domain map:

\[
 \begin{gathered}
 \sup_{\substack{x\in\mathfrak n_\psi\\\|x\|\le1}}
       \|\eta_\psi(x)\|\\
   =\psi(1)^{1/2}\quad\text{in }[0,\infty].
 \end{gathered}
 \tag{CL.23}
\]

When the mass is finite, (CL.21) proves the upper bound, and \(x=1\) gives equality. For infinite mass, (CL.22) makes the supremum infinite. Consequently \(\mathcal L_\psi\), with the operator norm on its domain, is bounded exactly when \(\psi\) is a bounded functional. Its norm in that case is \(\psi(1)^{1/2}\). The infinite value in (CL.23) is a supremum of actual finite vector norms, not the norm of a nonexistent Hilbert vector.

There are two different domain topologies to keep distinct. The finite left ideal is ultraweakly dense: the bounded elements \(a b_i\in\mathfrak n_\psi\) converge strongly, hence ultraweakly, to \(a\), by the bounded-set topology result used in WG-008. For an infinite weight it is never operator-norm dense. In fact

\[
 \operatorname{dist}_{\|\cdot\|}(1,\mathfrak n_\psi)=1
       \quad\text{if }\psi(1)=\infty.
 \tag{CL.24}
\]

If \(\|1-x\|<1\), the Neumann series makes \(x\) invertible. Therefore
\(x^*x\ge\|x^{-1}\|^{-2}1\). Membership in \(\mathfrak n_\psi\) would force \(\psi(1)<\infty\), a contradiction. This proves the lower bound in (CL.24); \(x=0\) gives its upper bound. Thus semifiniteness supplies a dense finite-energy domain in the von Neumann topology without making an infinite weight a bounded Hilbert-vector map. All these arguments allow arbitrary directed nets and nonseparable standard spaces.

## The right module map and the half-power domain

The canonical conjugation defines a right action by

\[
 \xi a:=\beta(a)\xi,\qquad
 \beta(a)=Ja^*J\in M'.
 \tag{CL.25}
\]

The map \(a\mapsto\beta(a)\) is complex linear, preserves adjoints, and reverses products:
\(\beta(ab)=\beta(b)\beta(a)\). These identities follow by inserting \(J^2=1\), taking \((ab)^*=b^*a^*\), and using antilinearity of \(J\). Thus \((\xi a)b=\xi(ab)\); the two actions commute because \(\beta(a)\in M'\).

For any normal semifinite weight, define the right finite domain and map by

\[
 \begin{aligned}
 \mathfrak n_\psi^*&=\{x\in M:x^*\in\mathfrak n_\psi\}\\
    &=\{x\in M:\psi(xx^*)<\infty\},\\
 \psi^{1/2}x&:=J\eta_\psi(x^*)
       \quad(x\in\mathfrak n_\psi^*).
 \end{aligned}
 \tag{CL.26}
\]

Taking an adjoint and applying \(J\) are both conjugate linear, so their composition is complex linear. The domain is a right ideal. For \(a\in M\), (CL.20) proves

\[
 \begin{aligned}
 \psi^{1/2}(xa)
   &=J\eta_\psi(a^*x^*)\\
   &=Ja^*J\bigl(J\eta_\psi(x^*)\bigr)\\
   &=(\psi^{1/2}x)a,\\
 \|\psi^{1/2}x\|^2&=\psi(xx^*).
 \end{aligned}
 \tag{CL.27}
\]

Its null right ideal is \((1-e)M\), because
\(\eta_\psi(x^*)=0\) exactly when \(x^*e=0\), or \(ex=0\). Its range is dense in \(eL^2(M)\): CL-03 gives density of the left map in \(JeJ\,L^2(M)\), and \(J\) carries that closed subspace onto \(eL^2(M)\).

For a bounded positive normal functional, the two maps are ordinary actions of the same cone vector. Since \(J\xi_\psi=\xi_\psi\), (CL.21) gives

\[
 J\eta_\psi(x^*)=Jx^*J\xi_\psi
      =\xi_\psi x\quad(x\in M).
 \tag{CL.28}
\]

The exact domain-map norm in (CL.23) holds for the right map as well: the adjoint is an operator-norm isometry between the two finite domains, and \(J\) is an isometry.

There is a modular half-power identity when \(\psi\) is faithful. On the exact two-sided finite domain,

\[
 \begin{gathered}
 x\in\mathfrak n_\psi\cap\mathfrak n_\psi^*,\\
 \eta_\psi(x)\in D(\Delta_\psi^{1/2}),\\
 \psi^{1/2}x=\Delta_\psi^{1/2}(x\psi^{1/2}).
 \end{gathered}
 \tag{CL.29}
\]

To prove it, use One Hilbert space for all n.s.f. GNS maps with both weights equal to \(\psi\). The closed Tomita operator extends
\(S_\psi\eta_\psi(x)=\eta_\psi(x^*)\) on that finite-star core and has polar decomposition \(S_\psi=J\Delta_\psi^{1/2}\). Multiplication by \(J\) gives (CL.29). The core determines the full closed graph, but (CL.29) does not assert that every \(x\in M\) belongs to it.

For a nonfaithful weight, apply this statement to its faithful restriction on \(eMe\), on that corner's two-sided finite domain and standard space \(eJeJ\,L^2(M)\). The whole-algebra GNS space \(JeJ\,L^2(M)\) need not be preserved by \(J\). Its GNS null ideal need not be closed under adjoints. Therefore the map
\(\eta_\psi(x)\mapsto\eta_\psi(x^*)\) must not be declared a Tomita operator on that quotient without the faithful-corner restriction. The next problem exhibits the failure even for a bounded normal functional.

## Three further domain checks with complete solutions

**Problem 1: counting mass on an arbitrary infinite set.** Let \(I\) be an infinite set, use the counting weight of CL-04 on \(\ell^\infty(I)\), and determine its finite left ideal, its canonical module map, and its distance from the identity in operator norm.

**Solution.** For \(x=(x_i)\in\ell^\infty(I)\), its energy is

\[
 \psi(x^*x)
    =\sup_{F\subset I,\ F\text{ finite}}\sum_{i\in F}|x_i|^2.
 \tag{CL.30}
\]

Hence \(\mathfrak n_\psi=\ell^\infty(I)\cap\ell^2(I)\), and the module map is the same coordinate family \(x\), regarded as a vector of \(\ell^2(I)\). CL-04's complete coordinate proof identifies this with canonical \(L^2(M)\). Every such vector has countable support: for each positive integer \(n\), the set \(\{i:|x_i|\ge1/n\}\) is finite, or finite partial sums would be unbounded. The support is the countable union of these sets. This imposes no countability assumption on \(I\) itself.

For finite \(F\), the indicator \(p_F\) has operator norm one if \(F\ne\varnothing\), and its GNS norm is \(|F|^{1/2}\). The net indexed by finite subsets increases to \(1\), while these GNS norms are unbounded. The formal constant square root of counting mass is therefore not an element of \(\ell^2(I)\). Equation (CL.24) gives distance one. Directly, if \(\|1-x\|_\infty<1\), all coordinates of \(x\) have one fixed positive lower bound, so (CL.30) is infinite. This is a dense finite-domain construction in arbitrary cardinality, rather than a countable summation assumption.

**Problem 2: the two products have different energies.** In \(M_2(\mathbb C)\), take \(h=\operatorname{diag}(4,9)\), \(\psi(a)=\operatorname{Tr}(ha)\), and \(x=E_{12}\). Compute both module values and check their modular relation.

**Solution.** In the Hilbert–Schmidt standard form, \(\xi_\psi=h^{1/2}=\operatorname{diag}(2,3)\). Left and right multiplication give

\[
 \begin{aligned}
 x\psi^{1/2}&=xh^{1/2}=3E_{12},\\
 \psi^{1/2}x&=h^{1/2}x=2E_{12},\\
 \psi(x^*x)&=9,\qquad \psi(xx^*)=4.
 \end{aligned}
 \tag{CL.31}
\]

These are different vectors with the different squared norms required by their domains. All matrices have finite energy here. The modular operator has half-power
\(\Delta_\psi^{1/2}(\zeta)=h^{1/2}\zeta h^{-1/2}\), as follows from the matrix Tomita polar decomposition. On \(3E_{12}\), it yields \(2E_{12}\), proving (CL.29) in this noncommuting test. The norm of either domain map on the operator-norm unit ball is \(\sqrt{13}\), attained at the identity. Equality of the two module values for this \(x\) would require an additional commutation condition and is false.

**Problem 3: an adjoint does not descend through a nonfaithful quotient.** Take \(\psi(a)=2a_{11}\) on \(M_2(\mathbb C)\). Determine the left and right values at \(x=E_{12}\), and test whether \(S\eta_\psi(z)=\eta_\psi(z^*)\) defines an operator on the whole GNS quotient.

**Solution.** The cone vector is \(\xi_\psi=\sqrt2E_{11}\), and \(e=E_{11}\). All matrices lie in both finite domains. Nevertheless

\[
 \begin{aligned}
 E_{12}\psi^{1/2}&=0,\\
 \psi^{1/2}E_{12}&=\sqrt2E_{12},\\
 \eta_\psi(E_{21})&=\sqrt2E_{21}.
 \end{aligned}
 \tag{CL.32}
\]

Thus \(E_{12}\) represents the zero left-GNS vector, whereas its adjoint represents a nonzero one. The proposed \(S\) would send zero to \(\sqrt2E_{21}\), so it is not well-defined. The full left-GNS space is the two-dimensional first-column space of CL-04; the right range is the first-row space. The faithful corner has the one-dimensional standard space \(\mathbb CE_{11}\), where the corner Tomita formula is well-defined. This failure concerns the full nonfaithful quotient; it does not invalidate either domain map or the actual cone vector for this bounded functional.
