# Full factors without almost periodic weights

*Written by Claude Opus 5.5 (Anthropic), September 2026, revised October 2026. The September text was spot-checked by Claude Opus 5.5 in a separate session; the October revisions are self-checked by the writing AI. The density normalization in Lemma 6.1 was checked and corrected by GPT-6 Astra (OpenAI), Ultra, October 2026. Public domain (CC0).*

## Introduction

A factor \(M\) with separable predual carries a canonical homomorphism \(\delta_M\) from the real line into its outer
automorphism group \(\operatorname{Out} M = \operatorname{Aut} M / \operatorname{Int} M\): the class of the modular
automorphism \(\sigma^\varphi_t\) does not depend on the faithful normal semifinite weight \(\varphi\). When \(M\) is
full, the group \(\operatorname{Int} M\) is closed, so \(\operatorname{Out} M\) is a metrizable topological group and
\(\delta_M\) pulls its topology back to a group topology \(\tau(M)\) on \(\mathbb{R}\). This topology is an
isomorphism invariant. It is coarser than the usual topology, and it records how close the modular automorphisms
\(\sigma^\varphi_t\) come to being inner.

The lesson proves four things.

1. For every strongly continuous unitary representation \(\rho\) of \(\mathbb{R}\) on a separable Hilbert space there
   is a full factor \(M\) with \(\tau(M)\) equal to the weakest topology making \(\rho\) strongly continuous; when
   \(\rho\) is injective, \(M\) is of type III\(_1\) (Theorem 6.4).
2. If a full factor has an almost periodic weight, then \(\tau(M)\) is totally bounded. Taking \(\rho\) to be the
   regular representation, we get a factor of type III\(_1\) that has no almost periodic weight, and in particular no
   almost periodic state (Section 7).
3. That factor is a group measure space factor. Hence there is an ergodic countable group of nonsingular
   transformations of a probability space whose Radon–Nikodym derivatives take uncountably many values for every
   equivalent measure (Section 9).
4. The same factor is not a crossed product \(Q\rtimes D\) with \(Q\) semifinite and \(D\) a discrete abelian group
   (Section 10). This bears on which locally compact abelian groups \(G\) allow every type III factor to be written as
   a semifinite algebra crossed by \(G\) (Section 11).

So the discrete decomposition, which exists for factors with separable predual of type III\(_\lambda\) with
\(\lambda \neq 1\), and for those of type III\(_1\) with an almost periodic weight, has no analogue for general type
III\(_1\) factors. Only the
continuous decomposition, with the group \(\mathbb{R}\), always works.

**Prerequisites.** Tomita–Takesaki theory for weights, including the Connes cocycle derivative and crossed products.
"Results used from other lessons" lists the facts we use and where each is proved. From this course we
use the lessons Full factors and [Almost periodic weights and the invariant \(Sd\)](almost-periodic-weights-and-the-invariant-sd.html). Section 1 restates
exactly what we take from them.

A basic reference is [Connes 1974].

**Conventions.** All Hilbert spaces are complex. For a faithful normal state \(\psi\) on \(M\) we write
\(\|x\|_\psi = \psi(x^*x)^{1/2}\). In the standard form \(L^2(M,\psi)\) with cyclic and separating vector
\(\xi_\psi\) this is \(\|x\xi_\psi\|\). We write \(\mathbb{R}_+^*\) for the multiplicative group of positive reals,
\(\mathbb{T}\) for the unit circle and \(\mathbb{F}_2\) for the free group on two generators \(a, b\). A weight is
always faithful, normal and semifinite unless we say otherwise. We write "fns weight" for short.

## Results used from other lessons

The following standard facts are used freely.

- **Standard form.** For an fns weight \(\varphi\) on \(M\), \(M\) acts standardly on \(L^2(M,\varphi)\). There
  \(\sigma^\varphi_t(x) = \Delta_\varphi^{it} x \Delta_\varphi^{-it}\) and
  \(\Delta_\varphi^{it}\Lambda_\varphi(x) = \Lambda_\varphi(\sigma^\varphi_t(x))\) for \(x \in \mathfrak{n}_\varphi\).
  Every normal functional on a von Neumann algebra in standard form is a vector functional
  \(x \mapsto \langle x\eta,\zeta\rangle\). These are proved in the course *Modular theory and weights*: the standard
  form of \(L^2(M,\varphi)\) in The positive cone of a standard representation, §SF-05;
  the two formulas for \(\Delta_\varphi^{it}\) in The modular group and its analytic algebra,
  §MF-06; a cone vector for every positive normal functional, in every standard form,
  in Recovering a representation from its positive cone, §SE-11. For general
  \(\omega\in M_*\) take the polar decomposition \(\omega=v|\omega|\), that is \(\omega(x)=|\omega|(xv)\) with \(v\in M\)
  (Polar decomposition of functionals and weak compactness in preduals, Theorem 2.2), and write
  \(|\omega|=\langle\,\cdot\,\xi,\xi\rangle\); then \(\omega(x)=\langle xv\xi,\xi\rangle\).
- **Cocycle derivatives.** For fns weights \(\varphi,\psi\) on \(M\) the Connes cocycle \((D\psi:D\varphi)_t\) is a
  strongly continuous family of unitaries with \(\sigma^\psi_t = \operatorname{Ad}(D\psi:D\varphi)_t \circ
  \sigma^\varphi_t\). For a unitary \(u\), \((D(\psi\circ\operatorname{Ad}u):D\psi)_t = u^*\sigma^\psi_t(u)\). If
  \(\tau\) is an fns trace on \(N\), every fns trace on \(N\) is \(\tau(h\,\cdot)\) for a unique positive nonsingular
  \(h\) affiliated with the centre of \(N\), and \((D\tau(h\,\cdot):D\tau)_t = h^{it}\). A unitary \(u\) lies in the
  centralizer \(M_\psi\) of a faithful normal state \(\psi\) if and only if \(\psi\circ\operatorname{Ad}u = \psi\).
  The restriction of an fns weight to its centralizer is a trace. A normal weight is the pointwise supremum of the
  normal positive functionals it majorizes. These are proved in the course *Modular theory and weights*, except where a
  short argument is given. The cocycle: Supported GNS representations and the balanced cocycle,
  §§GC-03–GC-04 and Comparing supported weights and transporting their cuts,
  §WC-02. The formula for \(\psi\circ\operatorname{Ad}u\): Averaging a dual action and
  recovering its coefficients, OA-FLOW.AVG.INNER, which computes it from the
  balanced weight and the transport of modular groups by automorphisms (The KMS boundary condition determines the
  modular group, §KM-06). Traces: by Recognizing a weight by its fixed density,
  §PT-08, \(\sigma^\tau\) is trivial and every fns weight on \(N\) is \(\tau_h\)
  (written \(\tau(h\,\cdot)\) above) for a unique positive nonsingular \(h\) affiliated with \(N\). If \(\tau_h\) is a
  trace, then
  \(\tau_{u^*hu}=\tau_h\circ\operatorname{Ad}u=\tau_h\) for every unitary \(u\in N\), so \(u^*hu=h\) by uniqueness, and
  \(h\) is affiliated with the centre. Then \((D\tau_h:D\tau)_t=h^{it}\) by §PT-04 there, since the centralizer of \(\tau\)
  is \(N\). The centralizer: by Fixed elements and changes of density, §CZ-05, an
  element \(a\) lies in the centralizer \(N=M_\varphi\) of an fns weight \(\varphi\) if and only if it is a two-sided
  multiplier of \(\mathfrak m_\varphi\) and \(\varphi(az)=\varphi(za)\) for \(z\in\mathfrak m_\varphi\). For a unitary and
  a faithful normal state \(\psi\) this says \(\psi(ux)=\psi(xu)\) for all \(x\), that is \(\psi\circ\operatorname{Ad}u=\psi\).
  If \(x\in N\) has \(\varphi(x^*x)<\infty\) and polar decomposition \(x=v|x|\) in \(N\), then \(z=x^*xv^*\in\mathfrak
  m_\varphi\), and \(\varphi(xx^*)=\varphi(vz)=\varphi(zv)=\varphi(x^*x)\); applied to \(x^*\), this shows that
  \(\varphi(x^*x)\) and \(\varphi(xx^*)\) are finite together, so \(\varphi|_N\) is a trace. The supremum formula:
  Detecting normal weights by finite observations, §NW-11.
- **Conditional expectations.** If \(E : M \to N\) is a faithful normal conditional expectation and
  \(\varphi,\varphi_1,\varphi_2\) are fns weights on \(N\), then \(\sigma^{\varphi\circ E}_t\) restricts to
  \(\sigma^\varphi_t\) on \(N\), and \((D(\varphi_1\circ E):D(\varphi_2\circ E))_t = (D\varphi_1:D\varphi_2)_t\). If
  \(N \subset M\) is globally invariant under \(\sigma^\psi\) for a faithful normal state \(\psi\), there is a
  \(\psi\)-preserving faithful normal conditional expectation of \(M\) onto \(N\) (Takesaki's theorem). If a compact
  group \(L\) acts continuously on \(M\) by \(\gamma\), then \(x \mapsto \int_L \gamma_\chi(x)\,d\chi\) (normalized
  Haar measure) is a faithful normal conditional expectation onto the fixed-point algebra, and for each continuous
  character \(c\) of \(L\) the map \(x \mapsto \int_L \overline{c(\chi)}\gamma_\chi(x)\,d\chi\) is normal.
  The modular group of \(\varphi\circ E\): Conditional expectations from modular invariance,
  §ME-10. The cocycle identity is proved in Full factors, (B4)(d).
  Takesaki's theorem: Conditional expectations from modular invariance, §ME-01;
  the expectation is faithful because
  \(\psi\circ E=\psi\). The averages are weak integrals: for \(f\in C(L)\), \(x\in M\) and \(\omega\in M_*\),
  \(\omega(E_f(x))=\int_Lf(\chi)\,\omega(\gamma_\chi(x))\,d\chi\) defines \(E_f(x)\in M=(M_*)^*\); normalized Haar measure is
  constructed in Haar measure on locally compact groups, Theorem 8.3, and it charges every nonempty
  open set (Proposition 9.1 there). The map \(\chi\mapsto f(\chi)\,\omega\circ\gamma_\chi\) into \(M_*\) is continuous for
  the weak topology \(\sigma(M_*,M)\), so its weak integral \(\omega\circ E_f\) lies in \(M_*\) (Continuity of actions:
  scalar tests, preduals, and bounded nets, OA-FLOW.TOP.BARYCENTER), and
  \(E_f\) is normal. For \(f=1\), \(E=E_1\) is positive and unital; its values are fixed by every \(\gamma_\kappa\), by
  invariance of Haar measure; it fixes the fixed points; and \(E(axb)=aE(x)b\) for fixed \(a,b\), because \(y\mapsto
  \omega(ayb)\) is again normal. If \(x\ge0\) and \(E(x)=0\), then for each \(\omega\in M_*^+\) the continuous function
  \(\chi\mapsto\omega(\gamma_\chi(x))\ge0\) has integral \(0\), so it vanishes; at \(\chi=1\) this gives \(\omega(x)=0\),
  so \(x=0\).
- **Crossed products.** For an action \(\alpha\) of a locally compact abelian group \(G\) on \(Q\) the crossed product
  \(Q \rtimes_\alpha G\) is generated by \(\pi(Q)\) and unitaries \(\lambda(g)\) with
  \(\lambda(g)\pi(x)\lambda(g)^* = \pi(\alpha_g(x))\). It carries the dual action \(\hat\alpha\) of \(\hat G\), with
  \(\hat\alpha_\chi(\pi(x)) = \pi(x)\) and \(\hat\alpha_\chi(\lambda(g)) = \overline{\chi(g)}\lambda(g)\).
  Takesaki duality gives \((Q \rtimes_\alpha G)\rtimes_{\hat\alpha}\hat G \cong Q \mathbin{\bar\otimes} B(L^2(G))\). For an fns
  weight \(\varphi\), \(M \rtimes_{\sigma^\varphi}\mathbb{R}\) is semifinite. For a discrete group, the map
  \(\sum_g \pi(x_g)\lambda(g) \mapsto \pi(x_e)\) extends to a faithful normal conditional expectation onto \(\pi(Q)\).
  If \(\tau\) is an fns trace on \(Q\), the dual weight \(\tilde\tau\) on \(Q\rtimes_\alpha G\) is
  \(\hat\alpha\)-invariant and satisfies \(\sigma^{\tilde\tau}_t(\pi(x)) = \pi(x)\) and
  \(\sigma^{\tilde\tau}_t(\lambda(g)) = \lambda(g)\,\pi((D(\tau\circ\alpha_g):D\tau)_t)\). These are proved in the course
  *Crossed products and the flow of weights*: the crossed product in Changing the Hilbert space of a regular crossed
  product; the dual action in Averaging a dual action and recovering its
  coefficients, OA-FLOW.AVG.DUALACTION; Takesaki duality in Two crossed
  products and the surviving action; the fns trace on
  \(M\rtimes_{\sigma^\varphi}\mathbb R\) in Building an intrinsic flow from modular coordinates,
  OA-FLOW.CORE.TRACE; the conditional expectation for a discrete group in The
  coefficient algebra as the value space of a weight, OA-FLOW.OVW.DISCRETE;
  the invariance of the dual weight in Averaging a dual action and recovering its coefficients,
  OA-FLOW.AVG.NORMALIZATION; its modular
  group in How the dual weight moves crossed-product generators,
  OA-FLOW.DW.MODULARGENERATORS, where \(G\) is unimodular and
  \(\sigma^\tau\) is trivial.
- **Modular automorphisms and types.** If \(M\) is semifinite, every \(\sigma^\varphi_t\) is inner: Inner modular flow
  and rigidity of finite weight data, §VR-02. If \(M\) is a factor of type
  III\(_\lambda\) with \(0<\lambda<1\), then \(\sigma^\varphi_{T}\) is inner for \(T = 2\pi/|\log\lambda|\). In the notation
  of Section 3, \(T(M)=\mathbb{R}\) in the first case and \(T(M)=(2\pi/|\log\lambda|)\mathbb{Z}\) in the second [Connes
  1973, Theorems 1.3.4 and 3.4.1]. In a factor of type III with separable predual, any two nonzero projections are
  equivalent: they are infinite, and the factor is countably decomposable, so Projections and types of von Neumann
  algebras, Proposition 15.2(4) applies. A von Neumann algebra \(M\) with separable predual is
  countably decomposable: if \((\omega_n)\) is norm dense in the positive part of the unit ball of \(M_*\), then
  \(\omega=\sum_n2^{-n}\omega_n\) is a faithful normal positive functional, since \(\omega(x)=0\) for \(x\ge0\) forces
  \(\omega'(x)=0\) for every positive normal \(\omega'\), in particular for every vector functional.
- **Infinite tensor products.** For faithful normal states \(\varphi_s\) on von Neumann algebras \(P_s\) with
  separable predual (\(s\) in a countable set), the infinite tensor product \((N,\omega) = \bigotimes_s
  (P_s,\varphi_s)\) acts on \(\bigotimes_s (L^2(P_s,\varphi_s),\xi_{\varphi_s})\). The product state \(\omega\) is
  faithful and normal, and \(\Delta_\omega^{it} = \bigotimes_s \Delta_{\varphi_s}^{it}\). For abelian
  \(P_s = L^\infty(Y_s,\nu_s)\) with probability measures, this is \(L^\infty(\prod_s Y_s, \bigotimes_s\nu_s)\), with
  \(\bigotimes_s(L^2(Y_s,\nu_s),1) = L^2(\prod_s Y_s,\bigotimes_s\nu_s)\). The product state is faithful and normal by
  Infinite tensor products, Proposition 5.2, and
  \(\Delta_\omega^{it}=\bigotimes_s\Delta_{\varphi_s}^{it}\) is Theorem 6.1 there. In the abelian case, the map sending
  \(f_1\otimes\cdots\otimes f_n\otimes1\otimes\cdots\) (with \(f_k\) at the site \(s_k\)) to the function
  \(x\mapsto\prod_kf_k(x_{s_k})\) is isometric, because the product measure of a measurable cylinder is the product of the
  measures of its sides, and it has dense range, because every measurable set is approximated in measure by finite
  unions of measurable cylinders ([Fremlin, Measure Theory, Volume 2, Theorem 254F(b), (e)](https://www1.essex.ac.uk/maths/people/fremlin/cont25.htm), free). It
  carries the product algebra to the algebra generated by the multiplications by bounded functions of finitely many
  coordinates. That algebra is \(L^\infty(\prod_sY_s,\bigotimes_s\nu_s)\): the measurable sets whose indicators it contains
  form a \(\sigma\)-algebra containing the cylinders, and the product measure is the completion of its restriction to the
  \(\sigma\)-algebra they generate (Theorem 254F(f) there).
- **Spectral theory.** Stone's theorem: a strongly continuous unitary representation of \(\mathbb{R}\) has the form
  \(\rho(t) = H^{it}\) for a positive nonsingular self-adjoint \(H\). Proved in Analytic elements and strip
  arguments, Theorem 8.1(3).
- **Topological groups.** A Hausdorff first countable topological group is metrizable (the Birkhoff–Kakutani
  theorem): Polish spaces and standard Borel spaces, Lemma 8.4. Pontryagin duality holds for
  locally compact abelian groups: The Pontryagin duality theorem, Theorem 2.1. Every locally compact
  abelian group \(G\) is isomorphic to \(\mathbb{R}^n \times G_0\), where \(G_0\) has a compact open subgroup. Indeed, by
  The structure of locally compact abelian groups, Theorem 4.3, \(G\) has an open subgroup
  \(U\cong\mathbb R^n\times K\) with \(K\) compact. The projection of \(U\) onto \(\mathbb R^n\) extends to a homomorphism
  \(r:G\to\mathbb R^n\), because \(\mathbb R^n\) is divisible (Lemma 4.1 there), and \(r\) is continuous because it is
  continuous on the open subgroup \(U\). Identifying \(\mathbb R^n\) with \(\mathbb R^n\times\{0\}\subset U\), the map
  \(g\mapsto(r(g),g-r(g))\) is a topological isomorphism of \(G\) onto \(\mathbb R^n\times\ker r\), with inverse
  \((y,z)\mapsto y+z\), and \(U\cap\ker r=K\) is a compact open subgroup of \(\ker r\). The annihilator of a compact open
  subgroup is compact and open: Subgroups, quotients and annihilators, Corollary 2.2.

## 1. What we use from the earlier lessons

A reference for this section is [Connes 1974].

Let \(M\) have separable predual. The **u-topology** on \(\operatorname{Aut} M\) is the topology in which
\(\alpha_i \to \alpha\) if and only if \(\|\omega\circ\alpha_i - \omega\circ\alpha\| \to 0\) for every \(\omega \in
M_*\). \(M\) is **full** if \(\operatorname{Int} M\) is closed in \(\operatorname{Aut} M\).

From the lesson Full factors we use the following three results (Proposition 2.3, Construction 9.1 with
Proposition 9.2 and Theorem 9.4, and Theorem 7.1 there). Item 5 of Theorem 1.2 is not stated in that lesson, so we
prove it below.

**Theorem 1.1.** If \(M\) has separable predual, then \(\operatorname{Aut} M\) with the u-topology is a Polish
topological group.

**Theorem 1.2 (free Bernoulli crossed products).** Consider a von Neumann algebra \(P\) whose predual is separable,
with a faithful normal state \(\varphi\). Put \(\mathcal{H} = L^2(P,\varphi)\) and \(\xi_0 = \xi_\varphi\). Let
\((N,\omega) = \bigotimes_{s\in\mathbb{F}_2}(P,\varphi)\) act on \(\mathcal{K} = \bigotimes_{s\in\mathbb{F}_2}
(\mathcal{H},\xi_0)\), with product vector \(\eta_0\), \(\omega = \langle\,\cdot\,\eta_0,\eta_0\rangle\), and
embeddings \(\pi_s : P \to N\). Let \(V_s\) be the unitaries of \(\mathcal{K}\) that shift the tensor factors, so that
\(V_s\eta_0 = \eta_0\) and \(V_s\pi_t(x)V_s^* = \pi_{st}(x)\), and let \(\theta_s = \operatorname{Ad}V_s|_N\). Denote
by \(M\) the von Neumann algebra on \(\mathcal{K}\otimes\ell^2(\mathbb{F}_2)\) generated by \(N\otimes 1\) and the
unitaries \(U_s = V_s\otimes\lambda_s\) (\(\lambda\) the left regular representation), and put \(\zeta_0 =
\eta_0\otimes\delta_e\) and \(\psi = \langle\,\cdot\,\zeta_0,\zeta_0\rangle\). We identify \(N\) with \(N\otimes 1\),
so that \(U_sxU_s^* = \theta_s(x)\) for \(x \in N\). Then:

1. \(\psi\) is a faithful normal state of \(M\), and \(U_s\) lies in the centralizer \(M_\psi\) for every \(s\).
2. For every \(x \in M\),
   \[ \|x - \psi(x)1\|_\psi \le 20\max\big(\|[x,U_a]\|_\psi,\ \|[x,U_b]\|_\psi\big). \tag{1.1} \]
3. \(\Delta_\psi = \Delta_\omega\otimes 1\) on \(\mathcal{K}\otimes\ell^2(\mathbb{F}_2)\), and \(\Delta_\omega^{it} =
   \bigotimes_s\Delta_\varphi^{it}\) on \(\mathcal{K}\). Thus \(\Delta_\psi^{it}\) is a countable direct sum of copies
   of \(\Delta_\omega^{it}\).
4. \(M\) is a full factor, and its predual is separable.
5. There is a faithful normal conditional expectation \(E : M\to N\) with \(\psi = \omega\circ E\) and \(E(U_s) = 0\)
   for \(s \neq e\).

We call \(M\) the free Bernoulli crossed product built on \((P,\varphi)\). By item 5 and Lemma 8.1 below it is
isomorphic to \(N\rtimes_\theta\mathbb{F}_2\), but we never need this.

**Proof of item 5.** By item 3, \(\sigma^\psi_t = \operatorname{Ad}(\Delta_\omega^{it}\otimes 1)\) on \(M\), and this
maps \(x\otimes 1\) to \(\sigma^\omega_t(x)\otimes 1\). So \(N\) is globally invariant under \(\sigma^\psi\), and
Takesaki's theorem gives a \(\psi\)-preserving faithful normal conditional expectation \(E : M\to N\). Since
\(\psi(x\otimes 1) = \langle x\eta_0,\eta_0\rangle = \omega(x)\), we get \(\psi = \psi\circ E = \omega\circ E\). Let
\(s\neq e\) and \(x\in N\). Then
\[ \psi(xE(U_s)) = \psi(E(xU_s)) = \psi(xU_s) = \langle x V_s\eta_0\otimes\delta_s,\ \eta_0\otimes\delta_e\rangle = 0.
\]
Taking \(x = E(U_s)^*\) and using faithfulness of \(\psi\), \(E(U_s) = 0\). \(\square\)

**Theorem 1.3.** A factor of type III\(_0\) with separable predual is not full.

A weight \(\varphi\) is **almost periodic** if \(\Delta_\varphi\) is diagonalizable: \(\Delta_\varphi = \sum_\lambda
\lambda E_\lambda\) for pairwise orthogonal projections \(E_\lambda\) with sum \(1\). It is **strictly semifinite**
if its restriction to the centralizer \(M_\varphi\) is semifinite. For a subgroup \(\Lambda \subset \mathbb{R}_+^*\)
let \(G_\Lambda\) be the compact dual group of \(\Lambda\) with the discrete topology, and let
\(\hat\beta : \mathbb{R}\to G_\Lambda\), \(\hat\beta(t)(\lambda) = \lambda^{it}\). From the lesson [Almost periodic
weights and the invariant \(Sd\)](almost-periodic-weights-and-the-invariant-sd.html) we use the following two results: the implication (c)⇒(a) of Theorem 3.3 there,
and Lemma 7.3 there.

**Theorem 1.4.** Let \(\varphi\) be a strictly semifinite fns weight on \(M\), and \(\Lambda \subset \mathbb{R}_+^*\)
a subgroup. Suppose some set \(S\) generating \(M\) as a von Neumann algebra has this property: for each \(x\in S\)
there is a \(*\)-strongly continuous map \(f_x : G_\Lambda \to M\) with \(\sigma^\varphi_t(x) = f_x(\hat\beta(t))\)
for all \(t\). Then \(\varphi\) is almost periodic and the eigenvalues of \(\Delta_\varphi\) lie in \(\Lambda\).

**Theorem 1.5.** Let a countable discrete abelian group \(D\) act on a von Neumann algebra \(N\) whose predual is
separable and whose centre is diffuse. If \(N \rtimes D\) is a factor, then it is not full.

## 2. Automorphisms implemented by unitaries

Three elementary lemmas relate convergence in the u-topology to convergence of operators. We use them throughout.

**Lemma 2.1.** Let \(M\) act standardly on \(\mathcal{H}\). Let \(\alpha_n,\alpha \in \operatorname{Aut}M\) be
implemented by unitaries on \(\mathcal{H}\): \(\alpha_n(x) = V_nxV_n^*\) and \(\alpha(x) = VxV^*\). If \(V_n \to V\)
strongly, then \(\alpha_n \to \alpha\) in the u-topology. The same holds for nets.

**Proof.** For unitaries, \(V_n \to V\) strongly implies \(V_n^* \to V^*\) strongly, because
\(\|V_n^*\xi - V^*\xi\| = \|VV^*\xi - V_nV^*\xi\|\). Let \(\omega \in M_*\). By the standard form, \(\omega(x) =
\langle x\eta,\zeta\rangle\) for some vectors \(\eta,\zeta\). Then \(\omega(\alpha_n(x)) = \langle xV_n^*\eta,
V_n^*\zeta\rangle\), and for \(\|x\|\le 1\),
\[ |\omega(\alpha_n(x)) - \omega(\alpha(x))| \le \|V_n^*\eta - V^*\eta\|\,\|\zeta\| + \|\eta\|\,\|V_n^*\zeta -
V^*\zeta\|. \]
The right side does not depend on \(x\) and tends to \(0\). So \(\|\omega\circ\alpha_n - \omega\circ\alpha\| \to
0\). \(\square\)

**Lemma 2.2.** Fix a faithful normal state \(\psi\) of \(M\). If \(\alpha_n \to \mathrm{id}\) in the u-topology,
then \(\alpha_n(x) \to x\) \(*\)-strongly for every \(x \in M\).

**Proof.** Work in \(L^2(M,\psi)\). We have
\[ \|\alpha_n(x) - x\|_\psi^2 = \psi(\alpha_n(x^*x)) - 2\operatorname{Re}\psi(x^*\alpha_n(x)) + \psi(x^*x). \]
Since \(\psi\circ\alpha_n \to \psi\) in norm, the first term tends to \(\psi(x^*x)\). With \(\omega = \psi(x^*\,\cdot)
\in M_*\), the middle term is \(\omega(\alpha_n(x)) \to \omega(x) = \psi(x^*x)\). So
\(\|(\alpha_n(x)-x)\xi_\psi\| \to 0\). Applying this to \(x^*\) gives
\(\|(\alpha_n(x)-x)^*\xi_\psi\|\to 0\). Put \(y_n = \alpha_n(x) - x\). This is a bounded sequence in \(M\) with
\(y_n\xi_\psi \to 0\). For \(x' \in M'\) we get \(y_nx'\xi_\psi = x'y_n\xi_\psi \to 0\). Since \(\xi_\psi\) is
separating for \(M\), it is cyclic for \(M'\), so \(M'\xi_\psi\) is dense. Boundedness then gives \(y_n \to 0\)
strongly. The same argument applies to \(y_n^*\). \(\square\)

**Lemma 2.3.** Fix a faithful normal state \(\psi\) of \(M\) and a sequence \((t_n)\) of reals. Then
\(\sigma^\psi_{t_n} \to \mathrm{id}\) in the u-topology if and only if \(\Delta_\psi^{it_n} \to 1\) strongly.

**Proof.** If \(\Delta_\psi^{it_n}\to 1\) strongly, Lemma 2.1 applies with \(V_n = \Delta_\psi^{it_n}\) and \(V=1\).
Conversely, suppose \(\sigma^\psi_{t_n} \to \mathrm{id}\). By Lemma 2.2, \(\Delta_\psi^{it_n}x\xi_\psi =
\sigma^\psi_{t_n}(x)\xi_\psi \to x\xi_\psi\) for every \(x\in M\). The vectors \(x\xi_\psi\) are dense and the
operators \(\Delta_\psi^{it_n}\) are unitary, so \(\Delta_\psi^{it_n} \to 1\) strongly. \(\square\)

In particular \(t \mapsto \sigma^\psi_t\) is continuous from \(\mathbb{R}\) into \(\operatorname{Aut} M\), because
\(t \mapsto \Delta_\psi^{it}\) is strongly continuous and Lemma 2.1 holds for nets.

## 3. The invariant \(\tau(M)\)

A reference for this section is [Connes 1974].

Let \(M\) be a full factor whose predual is separable. Then \(\operatorname{Int}M\) is a closed subgroup of
\(\operatorname{Aut}M\). It is normal, since \(\theta\circ\operatorname{Ad}u\circ\theta^{-1} =
\operatorname{Ad}\theta(u)\). Let \(q : \operatorname{Aut} M \to \operatorname{Out} M\) be the quotient map, and give
\(\operatorname{Out}M\) the quotient topology.

**Lemma 3.1.** \(\operatorname{Out} M\) is a metrizable topological group, and \(q\) is continuous and open.

**Proof.** The quotient of a topological group by a normal subgroup is a topological group, and the quotient map is
continuous and open. The quotient is Hausdorff because \(\operatorname{Int} M\) is closed. By Theorem 1.1,
\(\operatorname{Aut} M\) is metrizable, so it is first countable. Since \(q\) is open, the images of a countable
neighbourhood base at \(\mathrm{id}\) form a neighbourhood base at \(1\) in \(\operatorname{Out} M\). By the
Birkhoff–Kakutani theorem, \(\operatorname{Out}M\) is metrizable. \(\square\)

For an fns weight \(\varphi\) on \(M\), put \(\delta_M(t) = q(\sigma^\varphi_t)\). By the cocycle theorem,
\(\sigma^\psi_t = \operatorname{Ad}(D\psi:D\varphi)_t\circ\sigma^\varphi_t\) for any other fns weight \(\psi\), so
\(\delta_M(t)\) does not depend on \(\varphi\). It is a homomorphism \(\mathbb{R} \to \operatorname{Out}M\), the
**modular homomorphism**. Since \(M_*\) is separable, \(M\) has a faithful normal state \(\psi\). By Lemma 2.3,
\(t\mapsto\sigma^\psi_t\) is continuous, and hence so is \(\delta_M\).

**Definition 3.2.** For a full factor \(M\) whose predual is separable, the topology \(\tau(M)\) on \(\mathbb{R}\) is
the weakest topology making \(\delta_M : \mathbb{R}\to\operatorname{Out}M\) continuous. Its open sets are the sets
\(\delta_M^{-1}(W)\) with \(W\) open in \(\operatorname{Out}M\).

We define \(\tau(M)\) for all full factors, not only those of type III\(_1\). It is interesting mainly in type
III\(_1\), where the next proposition shows it can be Hausdorff. Recall the invariant \(T(M) = \{t\in\mathbb{R} :
\sigma^\varphi_t \in \operatorname{Int}M\}\). It is independent of \(\varphi\) by the cocycle theorem, and it is the
kernel of \(\delta_M\).

**Proposition 3.3.** Let \(M\) be a full factor whose predual is separable.

1. \((\mathbb{R},\tau(M))\) is a topological group, and \(\tau(M)\) is weaker than the usual topology.
2. \(\tau(M)\) is pseudometrizable. A sequence \(t_n\) converges to \(t\) in \(\tau(M)\) if and only if
   \(\delta_M(t_n - t) \to 1\). Two pseudometrizable topologies with the same convergent sequences are equal, so
   \(\tau(M)\) is determined by the sequences that converge to \(0\).
3. The closure of \(\{0\}\) in \(\tau(M)\) is \(T(M)\). So \(\tau(M)\) is Hausdorff if and only if \(T(M) = \{0\}\).
4. If \(\theta : M \to M'\) is an isomorphism, then \(\tau(M) = \tau(M')\).
5. If \(M\) is semifinite, \(\tau(M)\) is the indiscrete topology.

**Proof.** (1) Let \(m\) be the multiplication of \(\operatorname{Out}M\) and \(W\) an open set. The preimage of
\(\delta_M^{-1}(W)\) under addition is \((\delta_M\times\delta_M)^{-1}(m^{-1}(W))\), because \(\delta_M(s+t) =
\delta_M(s)\delta_M(t)\). This set is open in \(\tau(M)\times\tau(M)\). Negation is handled the same way. Since
\(\delta_M\) is continuous for the usual topology, every \(\tau(M)\)-open set is open.

(2) Let \(d_O\) be a metric for \(\operatorname{Out}M\) (Lemma 3.1). Then \(d(s,t) = d_O(\delta_M(s),\delta_M(t))\) is
a pseudometric whose open balls are preimages of balls. So it generates exactly \(\tau(M)\). Moreover \(t_n\to t\) if
and only if \(\delta_M(t_n)\to\delta_M(t)\), if and only if \(\delta_M(t_n-t)\to 1\). In a pseudometrizable space a set
is closed if and only if it contains the limits of its convergent sequences. So two pseudometrizable topologies with
the same convergent sequences have the same closed sets.

(3) \(t\) lies in the closure of \(\{0\}\) if and only if the constant sequence \(0\) converges to \(t\), that is,
\(\delta_M(-t) = 1\), that is, \(t \in T(M)\). A pseudometrizable topology is Hausdorff exactly when points are closed.
Since the topology is a group topology, it is enough that \(\{0\}\) is closed.

(4) The map \(\theta_*(\alpha) = \theta\circ\alpha\circ\theta^{-1}\) is a group isomorphism \(\operatorname{Aut}M
\to\operatorname{Aut}M'\). It is a homeomorphism for the u-topologies, because \(\omega'\circ\theta\alpha\theta^{-1}
= (\omega'\circ\theta)\circ\alpha\circ\theta^{-1}\) and \(\omega\mapsto\omega\circ\theta^{-1}\) is isometric from
\(M_*\) onto \(M'_*\). It maps \(\operatorname{Int}M\) onto \(\operatorname{Int}M'\), so it induces a topological
isomorphism \(\operatorname{Out}M\to\operatorname{Out}M'\). If \(\varphi\) is an fns weight on \(M\), then
\(\varphi\circ\theta^{-1}\) is one on \(M'\), and its modular group is \(\theta\circ\sigma^\varphi_t\circ\theta^{-1}\)
by uniqueness of the modular group (The KMS boundary condition determines the modular group,
§KM-06). Hence \(\delta_{M'} = \theta_*\circ\delta_M\) on the level of \(\operatorname{Out}\),
and the two pulled-back topologies agree.

(5) If \(M\) is semifinite, every \(\sigma^\varphi_t\) is inner, so \(\delta_M\) is trivial. \(\square\)

So \(\tau(M)\) is a group topology on \(\mathbb{R}\), coarser than the usual one, and an invariant of \(M\) up to
isomorphism. We now compute it for a family of full factors.

## 4. Spectral gap and outer convergence

The free Bernoulli crossed products of Theorem 1.2 have a *spectral gap*: an element that almost commutes with
\(U_a\) and \(U_b\) is close to a scalar. The next lemma turns this into a comparison between convergence in
\(\operatorname{Out}M\) and convergence in \(\operatorname{Aut}M\).

**Lemma 4.1.** Fix a faithful normal state \(\psi\) of \(M\) and unitaries \(U_1,\dots,U_k\) in \(M\). Suppose
there is a constant \(C\) such that
\[ \|x - \psi(x)1\|_\psi \le C\sum_{j=1}^k \|[x,U_j]\|_\psi \qquad\text{for all } x\in M. \tag{4.1} \]
Let \(\alpha_n\) be automorphisms of \(M\) with \(\psi\circ\alpha_n = \psi\) and \(\alpha_n(U_j) = U_j\) for all
\(j\) and \(n\). If there are unitaries \(u_n\in M\) with \(\operatorname{Ad}u_n\circ\alpha_n \to \mathrm{id}\) in the
u-topology, then \(\alpha_n \to \mathrm{id}\) in the u-topology.

**Proof.** Work in \(L^2(M,\psi)\). Two facts about the norm \(\|\cdot\|_\psi\) are used repeatedly:
\(\|uy\|_\psi = \|y\|_\psi\) for a unitary \(u\in M\), and \(\|\alpha(y)\|_\psi = \|y\|_\psi\) when
\(\psi\circ\alpha = \psi\).

Put \(\beta_n = \operatorname{Ad}u_n\circ\alpha_n\). Since \(\beta_n \to \mathrm{id}\) and \(\operatorname{Aut}M\) is a
topological group, \(\beta_n^{-1} = \alpha_n^{-1}\circ\operatorname{Ad}u_n^* \to \mathrm{id}\). By Lemma 2.2,
\(\|\beta_n^{-1}(U_j) - U_j\|_\psi \to 0\). Now \(\alpha_n^{-1}(U_j) = U_j\) and \(\alpha_n^{-1}\) preserves
\(\psi\), so
\[ \|\beta_n^{-1}(U_j) - U_j\|_\psi = \|\alpha_n^{-1}(u_n^*U_ju_n - U_j)\|_\psi = \|u_n^*U_ju_n - U_j\|_\psi. \]
Since \([u_n,U_j] = u_n(U_j - u_n^*U_ju_n)\), we get \(\|[u_n,U_j]\|_\psi = \|u_n^*U_ju_n - U_j\|_\psi \to 0\).

Apply (4.1) to \(x = u_n\) and put \(\lambda_n = \psi(u_n)\). Then \(\|u_n - \lambda_n1\|_\psi \to 0\). Since
\(\|u_n\|_\psi = 1\) and \(\|\lambda_n1\|_\psi = |\lambda_n|\), we have \(1 - |\lambda_n| \le \|u_n -
\lambda_n1\|_\psi\), so \(|\lambda_n|\to 1\). For large \(n\) put \(\mu_n = \lambda_n/|\lambda_n|\) (and \(\mu_n =
1\) for the finitely many other \(n\)). Then
\[ \|u_n - \mu_n1\|_\psi \le \|u_n-\lambda_n1\|_\psi + (1-|\lambda_n|) \to 0. \]
Let \(v_n = \overline{\mu_n}u_n\), a unitary with \(\operatorname{Ad}v_n = \operatorname{Ad}u_n\) and \(\|v_n -
1\|_\psi\to 0\). Also \(v_n^* - 1 = -v_n^*(v_n-1)\), so \(\|v_n^*-1\|_\psi = \|v_n - 1\|_\psi \to 0\). As in the
proof of Lemma 2.2, a bounded sequence \(y_n\) with \(y_n\xi_\psi\to 0\) tends to \(0\) strongly. So \(v_n \to 1\)
\(*\)-strongly. By Lemma 2.1, \(\operatorname{Ad}v_n\to\mathrm{id}\), hence \(\operatorname{Ad}v_n^* \to
\mathrm{id}\). Finally \(\alpha_n = \operatorname{Ad}v_n^*\circ\beta_n \to \mathrm{id}\). \(\square\)

**Corollary 4.2.** Let \(M\), \(\psi\), \(U_a\), \(U_b\) be as in Theorem 1.2. For every sequence \((t_n)\) of reals,
\[ \delta_M(t_n)\to 1 \iff \sigma^\psi_{t_n}\to\mathrm{id} \text{ in }\operatorname{Aut}M \iff
\Delta_\psi^{it_n}\to 1 \text{ strongly}. \]

**Proof.** The second equivalence is Lemma 2.3. If \(\sigma^\psi_{t_n}\to\mathrm{id}\), then \(\delta_M(t_n) =
q(\sigma^\psi_{t_n}) \to 1\) because \(q\) is continuous. Conversely, suppose \(\delta_M(t_n)\to 1\). Since \(q\) is
open, the sets \(q(W)\), with \(W\) running through a countable neighbourhood base of \(\mathrm{id}\) in
\(\operatorname{Aut}M\), form a neighbourhood base at \(1\). Take such a base \(W_1\supset W_2\supset\cdots\) and put
\(W_0 = \operatorname{Aut}M\). For each \(n\) let \(k(n)\) be the largest \(k\le n\) with
\(\delta_M(t_n)^{-1}\in q(W_k)\). Since \(\delta_M(t_n)^{-1}\to 1\), \(k(n)\to\infty\). Choose
\(\gamma_n\in W_{k(n)}\) with \(q(\gamma_n) = \delta_M(t_n)^{-1}\). Then \(\gamma_n\to\mathrm{id}\). The automorphism
\(\sigma^\psi_{t_n}\circ\gamma_n\) lies in the kernel of \(q\), so it is inner, say equal to \(\operatorname{Ad}w_n\).
Put \(u_n = w_n^*\). Then \(\sigma^\psi_{t_n} = \operatorname{Ad}w_n\circ\gamma_n^{-1}\), so
\(\operatorname{Ad}u_n\circ\sigma^\psi_{t_n} = \gamma_n^{-1}\to\mathrm{id}\), since inversion is continuous in
\(\operatorname{Aut}M\). The automorphisms \(\alpha_n = \sigma^\psi_{t_n}\) preserve \(\psi\) and fix \(U_a\) and
\(U_b\), since these lie in the centralizer (Theorem 1.2(1)). Since a maximum is at most a sum, inequality (1.1)
gives (4.1) with \(C = 20\). Lemma 4.1 gives \(\sigma^\psi_{t_n}\to\mathrm{id}\). \(\square\)

So in a free Bernoulli crossed product, the modular automorphisms of the state \(\psi\) can approach
\(\operatorname{Int}M\) only by approaching the identity itself.

## 5. The topology of a unitary representation of the real line

Let \(\rho\) be a strongly continuous unitary representation of \(\mathbb{R}\) on a separable Hilbert space
\(\mathcal{H}\). Let \(\tau_\rho\) be the weakest topology on \(\mathbb{R}\) making \(t\mapsto\rho(t)\xi\) continuous
for every \(\xi\in\mathcal{H}\), that is, the weakest topology making \(\rho\) strongly continuous.

**Lemma 5.1.** \(\tau_\rho\) is a pseudometrizable group topology, weaker than the usual topology. A sequence
\(t_n\) converges to \(t\) in \(\tau_\rho\) if and only if \(\rho(t_n - t)\to 1\) strongly. The closure of \(\{0\}\) is
\(\ker\rho\).

**Proof.** Let \((\xi_k)\) be dense in the unit ball of \(\mathcal{H}\) and put \(d(s,t) =
\sum_k 2^{-k}\|\rho(s)\xi_k - \rho(t)\xi_k\|\). Each map \(t\mapsto\rho(t)\xi_k\) is \(d\)-continuous. For general
\(\xi\) in the unit ball, \(\|\rho(s)\xi - \rho(t)\xi\| \le 2\|\xi - \xi_k\| + \|\rho(s)\xi_k - \rho(t)\xi_k\|\), so
\(t\mapsto\rho(t)\xi\) is \(d\)-continuous too. Conversely \(d\) is continuous for \(\tau_\rho\). Hence \(d\)
generates \(\tau_\rho\). Next, \(\|\rho(s)\xi - \rho(t)\xi\| = \|\rho(s-t)\xi - \xi\|\), so \(d\) is translation
invariant, and \(d(-s,-t) = d(t,s)\) by the same identity. This makes \(\tau_\rho\) a group topology, and gives the
criterion for convergence. The usual topology makes \(\rho\) strongly continuous, so it is finer. Finally \(t\) is
in the closure of \(\{0\}\) if and only if \(d(t,0) = 0\), that is, \(\rho(t) = 1\). \(\square\)

The next lemma replaces \(\rho\) by a multiplication representation on one \(L^2\) space.

**Lemma 5.2.** Let \(\rho\) be as above, with \(\mathcal{H}\neq 0\). There is a finite positive Borel measure \(\mu\)
on \(\mathbb{R}_+^*\), not zero, with \(\int\lambda\,d\mu(\lambda) < \infty\), such that for every sequence \((t_n)\):
\[ \rho(t_n)\to 1 \text{ strongly} \iff \lambda^{it_n}\to 1 \text{ in } \mu\text{-measure}. \]
In particular \(\ker\rho = \{t : \lambda^{it} = 1 \text{ for } \mu\text{-almost every }\lambda\}\).

**Proof.** By Stone's theorem \(\rho(t) = H^{it}\) with \(H\) positive, self-adjoint and nonsingular. Let
\(E\) be the spectral measure of \(H\) on \(\mathbb{R}_+^*\), and for \(\xi\in\mathcal{H}\) let \(\mu_\xi(B) =
\langle E(B)\xi,\xi\rangle\). Then
\[ \|\rho(t)\xi - \xi\|^2 = \int |\lambda^{it} - 1|^2\,d\mu_\xi(\lambda). \tag{5.1} \]
Let \((\xi_k)\) be dense in the unit ball and put \(\mu_0 = \sum_k 2^{-k}\mu_{\xi_k}\), a finite measure. It is not
zero, since \(\mathcal{H}\neq 0\). If \(\mu_0(B) = 0\), then \(E(B)\xi_k = 0\) for all \(k\), so \(E(B) = 0\) and
\(\mu_\xi(B) = 0\) for every \(\xi\). Thus \(\mu_\xi\ll\mu_0\).

Suppose \(\lambda^{it_n}\to 1\) in \(\mu_0\)-measure. Absolute continuity of the finite measure \(\mu_\xi\) with respect
to \(\mu_0\) means: for every \(\varepsilon > 0\) there is \(\eta > 0\) with \(\mu_0(B)<\eta \Rightarrow
\mu_\xi(B)<\varepsilon\). Hence \(\lambda^{it_n}\to 1\) in \(\mu_\xi\)-measure. The integrand in (5.1) is bounded by
\(4\), so the integral tends to \(0\). Conversely, if \(\rho(t_n)\to 1\) strongly, then \(\int|\lambda^{it_n}-1|^2
d\mu_{\xi_k}\to 0\) for each \(k\). Each term of \(\sum_k 2^{-k}\int|\lambda^{it_n}-1|^2d\mu_{\xi_k}\) is at most
\(4\cdot 2^{-k}\), so by dominated convergence for series, \(\int|\lambda^{it_n}-1|^2\,d\mu_0\to 0\). Chebyshev's
inequality then gives convergence in \(\mu_0\)-measure.

Put \(d\mu = (1+\lambda)^{-1}d\mu_0\). It is finite, equivalent to \(\mu_0\), and \(\int\lambda\,d\mu \le
\mu_0(\mathbb{R}_+^*) < \infty\). Convergence in measure is the same for equivalent finite measures: a sequence
converges in measure if and only if every subsequence has a further subsequence converging almost everywhere, and
null sets are the same for both measures. The last statement follows by taking constant sequences. \(\square\)

**Lemma 5.3.** Let \(m\) be a finite measure on \(\mathbb{R}_+^*\) and \(g_n\) measurable functions of modulus one.
Multiplication by \(g_n\) tends to \(1\) strongly on \(L^2(m)\) if and only if \(g_n\to 1\) in \(m\)-measure.

**Proof.** If \(g_n\to 1\) strongly, then \(\int|g_n-1|^2dm = \|(g_n-1)\cdot 1\|^2 \to 0\), which gives convergence in
measure. Conversely, if \(g_n \to 1\) in measure, then \(\int|g_n-1|^2dm\to 0\) by bounded convergence. For bounded
\(f\), \(\|(g_n-1)f\|\le\|f\|_\infty\|g_n-1\|_2\to 0\). Bounded functions are dense and the operators are uniformly
bounded, so the convergence holds for all \(f\). \(\square\)

**Example 5.4 (the regular representation).** Let \(\rho(t)\) be multiplication by \(e^{itx}\) on \(L^2(\mathbb{R},
dx)\). By the Fourier transform this is unitarily equivalent to the regular representation. We claim \(\tau_\rho\) is
the usual topology. Suppose \(\rho(t_n)\to 1\) strongly but \(t_n\not\to 0\). Passing to a subsequence, we may assume
\(|t_n|\ge\varepsilon > 0\), and that either \(t_n\to t\) with \(|t|\ge\varepsilon\), or \(|t_n|\to\infty\). In the
first case \(\rho(t_n)\to\rho(t)\) strongly, so \(\rho(t) = 1\). But \(\rho(t)\) is multiplication by \(e^{itx}\), which
is not \(1\) for \(t \neq 0\). In the second case let \(g = 1_{[0,1]}\). Then
\[ \langle\rho(t_n)g,g\rangle = \int_0^1 e^{it_nx}dx = \frac{e^{it_n}-1}{it_n}\to 0, \]
while it should tend to \(\|g\|^2 = 1\). So \(\rho(t_n)\to 1\) forces \(t_n\to 0\). Both topologies are metrizable and
have the same convergent sequences, so they coincide.

**Example 5.5 (a one-dimensional representation).** Let \(\rho(t) = \lambda_0^{it}\) on \(\mathbb{C}\), with
\(0<\lambda_0<1\). Then \(\ker\rho = T_0\mathbb{Z}\) with \(T_0 = 2\pi/|\log\lambda_0|\), and \(\tau_\rho\) is the
topology pulled back from the circle by \(t\mapsto\lambda_0^{it}\). It is not Hausdorff. For two numbers
\(\lambda_1,\lambda_2\) with \(\log\lambda_1/\log\lambda_2\notin\mathbb{Q}\), the representation
\(\rho(t) = \lambda_1^{it}\oplus\lambda_2^{it}\) on \(\mathbb{C}^2\) is injective. Its topology is pulled back from the
torus \(\mathbb{T}^2\) by the dense line \(t\mapsto(\lambda_1^{it},\lambda_2^{it})\). It is Hausdorff but strictly
weaker than the usual topology: since \(\mathbb{T}^2\) is compact, the argument of Theorem 7.1(4) below gives
\(t_n\to\infty\) with \(\lambda_j^{it_n}\to 1\) for \(j=1,2\).

## 6. Realizing a representation as the topology of a full factor

Fix a finite nonzero measure \(\mu\) on \(\mathbb{R}_+^*\) with \(\int\lambda\,d\mu < \infty\). Let
\(P = M_2(L^\infty(\mathbb{R}_+^*,\mu))\), whose elements are matrices \(f = (f_{ij})\) of bounded functions, and
define
\[ \varphi(f) = c\Big(\int f_{11}\,d\mu + \int \lambda f_{22}(\lambda)\,d\mu(\lambda)\Big), \qquad c =
\Big(\mu(\mathbb{R}_+^*) + \int\lambda\,d\mu\Big)^{-1}. \tag{6.1} \]
This is a normal state on \(P\) (the constant \(c\) makes \(\varphi(1) = 1\)). It is faithful, because
\(\varphi = (\operatorname{Tr}\otimes\int d\mu)(h\,\cdot)\) with density \(h = c\operatorname{diag}(1,\lambda)\),
which is nonsingular since \(\lambda>0\). \(P\) has separable predual.

**Lemma 6.1.** The modular group of \(\varphi\) is
\[ \sigma^\varphi_t(f) = \begin{pmatrix} f_{11} & \lambda^{-it}f_{12} \\ \lambda^{it}f_{21} & f_{22}\end{pmatrix}.
\tag{6.2} \]
The space \(L^2(P,\varphi)\) is the orthogonal sum of four subspaces \(\mathcal{H}_{ij}\), the closures of
\(\{\Lambda_\varphi(fe_{ij})\}\) with \(f\) a bounded function. Here \(\mathcal{H}_{i1}\cong L^2(c\mu)\) and
\(\mathcal{H}_{i2}\cong L^2(c\lambda\mu)\) via \(\Lambda_\varphi(fe_{ij})\mapsto f\). The operator
\(\Delta_\varphi^{it}\) acts as \(1\) on \(\mathcal{H}_{11}\) and \(\mathcal{H}_{22}\), as multiplication by
\(\lambda^{it}\) on \(\mathcal{H}_{21}\), and as multiplication by \(\lambda^{-it}\) on \(\mathcal{H}_{12}\).

**Proof.** Since \(\varphi\) is given by the positive nonsingular density \(h\) relative to the trace
\(\operatorname{Tr}\otimes\int d\mu\), \(\sigma^\varphi_t(f) = h^{it}fh^{-it}\). Its \((i,j)\) entry is
\(h_i^{it}f_{ij}h_j^{-it}\) with \(h_1 = c\) and \(h_2 = c\lambda\), which is (6.2). Next,
\(\varphi((ge_{kl})^*(fe_{ij})) = \varphi(\bar gf\,e_{lk}e_{ij})\). This vanishes unless \(k=i\), and then
\(\varphi(\bar gf\,e_{lj})\) vanishes unless \(l=j\). For \(k=i\) and \(l=j\) it equals \(\int\bar gf h_j\,d\mu\),
with \(h_j/c\) equal to \(1\) or \(\lambda\). This gives the orthogonal decomposition and the identifications. The
four subspaces together contain \(\Lambda_\varphi(P)\), which is dense. Finally
\(\Delta_\varphi^{it}\Lambda_\varphi(fe_{ij}) = \Lambda_\varphi(\sigma^\varphi_t(fe_{ij}))\), and (6.2) gives the
stated action. \(\square\)

**Corollary 6.2.** For every sequence \((t_n)\): \(\Delta_\varphi^{it_n}\to 1\) strongly if and only if
\(\lambda^{it_n}\to 1\) in \(\mu\)-measure.

**Proof.** By Lemma 6.1 and Lemma 5.3, \(\Delta_\varphi^{it_n}\to 1\) if and only if \(\lambda^{it_n}\to 1\) in
\(c\mu\)-measure and \(\lambda^{-it_n}\to 1\) in \(c\lambda\mu\)-measure. Now \(|\lambda^{-it}-1| = |\lambda^{it}-1|\),
and the finite measures \(\mu\), \(c\mu\) and \(c\lambda\mu\) are equivalent because \(\lambda>0\). So both
conditions say that \(\lambda^{it_n}\to 1\) in \(\mu\)-measure. \(\square\)

**Lemma 6.3.** Let \((N,\omega) = \bigotimes_{s\in\mathbb{F}_2}(P,\varphi)\). For every sequence \((t_n)\),
\(\Delta_\omega^{it_n}\to 1\) strongly if and only if \(\Delta_\varphi^{it_n}\to 1\) strongly.

**Proof.** Write \(\Delta_\omega^{it} = \bigotimes_s\Delta_\varphi^{it}\) on \(\bigotimes_s(L^2(P,\varphi),
\xi_\varphi)\), and note \(\Delta_\varphi^{it}\xi_\varphi = \xi_\varphi\). If \(\Delta_\varphi^{it_n}\to 1\), then on
a product vector \(\eta_1\otimes\cdots\otimes\eta_k\otimes\xi_\varphi\otimes\cdots\) (finitely many factors different
from \(\xi_\varphi\)) we get
\(\Delta_\omega^{it_n}(\eta_1\otimes\cdots) = \Delta_\varphi^{it_n}\eta_1\otimes\cdots\otimes
\Delta_\varphi^{it_n}\eta_k\otimes\xi_\varphi\otimes\cdots\), which tends to the original vector. Such vectors are
total and the operators are unitary, so \(\Delta_\omega^{it_n}\to 1\). Conversely, the map \(\eta\mapsto
\eta\otimes\xi_\varphi\otimes\xi_\varphi\otimes\cdots\) (the vector \(\eta\) placed at one site) is isometric and
intertwines \(\Delta_\varphi^{it}\) with \(\Delta_\omega^{it}\). \(\square\)

**Theorem 6.4.** Let \(\rho\) be a strongly continuous unitary representation of \(\mathbb{R}\) on a nonzero
separable Hilbert space. There is a full factor \(M\) whose predual is separable and whose invariant \(\tau(M)\) equals
\(\tau_\rho\). If
\(\rho\) is injective, \(M\) is of type III\(_1\) and \(\tau(M)\) is Hausdorff.

*Reference:* [Connes 1974, Theorem 5.2], stated there for injective \(\rho\).

**Proof.** Choose \(\mu\) as in Lemma 5.2, and form \(P\) and \(\varphi\) as in (6.1). Let \(M\) and \(\psi\) be the
free Bernoulli crossed product of Theorem 1.2 built on \((P,\varphi)\), and \(\omega\) the product state on \(N\). By Theorem 1.2(4), \(M\) is a full factor and its predual is separable. For any sequence \((t_n)\) we have
the chain of equivalences
\[ \rho(t_n)\to 1 \iff \lambda^{it_n}\to 1 \text{ in }\mu\text{-measure} \iff \Delta_\varphi^{it_n}\to 1 \iff
\Delta_\omega^{it_n}\to 1 \iff \Delta_\psi^{it_n}\to 1 \iff \delta_M(t_n)\to 1, \]
where the operator limits are strong. The steps are, in order: Lemma 5.2, Corollary 6.2, Lemma 6.3, Theorem 1.2(3),
and Corollary 4.2. For the fourth step, \(\Delta_\psi^{it} = \Delta_\omega^{it}\otimes 1\) is a countable direct
sum of copies of \(\Delta_\omega^{it}\), and strong convergence of a direct sum of uniformly bounded operators is
equivalent to strong convergence of each summand. Applying the chain to \(t_n - t\) and using Lemma 5.1 and Proposition 3.3(2),
the two topologies have the same convergent sequences. Both are pseudometrizable, so they coincide.

Now let \(\rho\) be injective. Taking constant sequences in the chain, \(\delta_M(t) = 1\) if and only if
\(\rho(t) = 1\). So \(T(M) = \ker\delta_M = \{0\}\), and \(\tau(M)\) is Hausdorff by Proposition 3.3(3). We determine
the type of \(M\) by elimination. If \(M\) were semifinite, all \(\sigma^\psi_t\) would be inner and \(T(M) =
\mathbb{R}\). If \(M\) were of type III\(_0\), it would not be full (Theorem 1.3). If \(M\) were of type
III\(_\lambda\) with \(0<\lambda<1\), then \(2\pi/|\log\lambda|\in T(M)\). All three contradict \(T(M) = \{0\}\), so
\(M\) is of type III\(_1\). \(\square\)

For the trivial representation (\(\mu\) a point mass at \(1\)), \(\varphi\) is the normalized trace on \(M_2(\mathbb{C})\)
and \(\tau(M)\) is indiscrete, in line with Proposition 3.3(5). For Example 5.5 with one eigenvalue \(\lambda_0\), the
factor has \(T(M) = 2\pi\mathbb{Z}/|\log\lambda_0|\) and a non-Hausdorff \(\tau(M)\).

## 7. Almost periodic weights force a totally bounded topology

A reference for this section is [Connes 1974].

**Theorem 7.1.** Consider a full factor \(M\) whose predual is separable and an almost periodic weight \(\varphi\) of
\(M\); let \(\Lambda\subset\mathbb{R}_+^*\) be the subgroup generated by the eigenvalues of \(\Delta_\varphi\). Then:

1. \(\Lambda\) is countable, and \(G_\Lambda\) is a compact metrizable abelian group in which \(\hat\beta(\mathbb{R})\)
   is dense.
2. There is a continuous homomorphism \(\kappa : G_\Lambda\to\operatorname{Aut}M\) with
   \(\kappa(\hat\beta(t)) = \sigma^\varphi_t\) for all \(t\). Hence \(\delta_M = q\circ\kappa\circ\hat\beta\).
3. \(\tau(M)\) is weaker than the topology \(\hat\beta^{-1}(\text{topology of } G_\Lambda)\). It is totally bounded:
   every \(\tau(M)\)-neighbourhood \(V\) of \(0\) has finitely many translates covering \(\mathbb{R}\).
4. There is a sequence \(t_n\) of integers with \(t_n\to\infty\) and \(\delta_M(t_n)\to 1\).

**Proof.** (1) Write \(\Delta_\varphi = \sum_\lambda\lambda E_\lambda\). The eigenspaces are pairwise orthogonal in
\(L^2(M,\varphi)\), which is separable because \(M_*\) is. So there are countably many eigenvalues, and \(\Lambda\) is
countable. The dual of a countable discrete group is a closed subgroup of the countable product
\(\mathbb{T}^\Lambda\), so it is compact and metrizable. Let \(H\) be the closure of \(\hat\beta(\mathbb{R})\). If
\(H\neq G_\Lambda\), the compact group \(G_\Lambda/H\) has a nontrivial continuous character. By Pontryagin duality
this gives some \(\lambda\in\Lambda\), \(\lambda\neq 1\), with \(\lambda^{it} = \hat\beta(t)(\lambda) = 1\) for all
\(t\). That is impossible.

(2) For \(s\in G_\Lambda\) define the unitary \(V_s = \sum_\lambda s(\lambda)E_\lambda\) on \(L^2(M,\varphi)\). Then
\(V_{\hat\beta(t)} = \Delta_\varphi^{it}\) and \(V_sV_{s'} = V_{ss'}\). The map \(s\mapsto V_s\) is strongly
continuous: on each eigenvector it is the continuous function \(s\mapsto s(\lambda)\), the eigenvectors span a dense
subspace, and the operators are unitary. Fix \(s\). By (1) and metrizability there are \(t_n\) with
\(\hat\beta(t_n)\to s\), so \(\Delta_\varphi^{it_n}\to V_s\) strongly. For \(x\in M\) and vectors \(\eta,\zeta\),
\[ \langle\sigma^\varphi_{t_n}(x)\eta,\zeta\rangle = \langle x\Delta_\varphi^{-it_n}\eta,\Delta_\varphi^{-it_n}\zeta
\rangle \to \langle xV_s^*\eta,V_s^*\zeta\rangle = \langle V_sxV_s^*\eta,\zeta\rangle. \]
So \(V_sxV_s^*\) is a weak operator limit of elements of \(M\), and lies in \(M\). The same holds for
\(V_s^* = V_{s^{-1}}\). So \(\kappa(s) = \operatorname{Ad}V_s\) is an automorphism of \(M\), and \(\kappa\) is a
homomorphism with \(\kappa(\hat\beta(t)) = \sigma^\varphi_t\). It is continuous by Lemma 2.1 (for nets), since
\(M\) acts standardly on \(L^2(M,\varphi)\).

(3) Let \(O\) be open in \(\operatorname{Out}M\). Then \(\delta_M^{-1}(O) = \hat\beta^{-1}((q\circ\kappa)^{-1}(O))\) is
the preimage of an open subset of \(G_\Lambda\). For total boundedness, let \(V\) be a \(\tau(M)\)-neighbourhood of
\(0\). By what we just showed, \(V\supset\hat\beta^{-1}(W)\) for a neighbourhood \(W\) of \(1\) in \(G_\Lambda\).
Choose a neighbourhood \(W'\) of \(1\) with \(W'W'^{-1}\subset W\). By compactness \(G_\Lambda = \bigcup_{i=1}^m
g_iW'\). Each open set \(g_iW'\) meets the dense set \(\hat\beta(\mathbb{R})\), say at \(\hat\beta(s_i)\). For any
\(t\in\mathbb{R}\), \(\hat\beta(t)\in g_iW'\) for some \(i\), and then \(\hat\beta(t-s_i) = \hat\beta(t)\hat\beta(s_i)^{-1}
\in g_iW'(g_iW')^{-1} = W'W'^{-1}\subset W\), since \(G_\Lambda\) is abelian. So \(t\in s_i + V\).

(4) The sequence \(\hat\beta(n)\), \(n\in\mathbb{N}\), in the compact metrizable group \(G_\Lambda\) has a convergent
subsequence \(\hat\beta(n_k)\to g\). Passing to a further subsequence, we may assume \(n_{k+1} - n_k\ge k\). Then
\(t_k = n_{k+1} - n_k\to\infty\) and \(\hat\beta(t_k) = \hat\beta(n_{k+1})\hat\beta(n_k)^{-1}\to gg^{-1} = 1\). By (2),
\(\delta_M(t_k) = q(\kappa(\hat\beta(t_k)))\to 1\). \(\square\)

**Corollary 7.2.** There is a full factor of type III\(_1\), acting on a separable Hilbert space, with no almost
periodic weight. In particular it has no faithful normal state whose modular operator is diagonalizable.

*Reference:* [Connes 1974, Corollary 5.3].

**Proof.** Apply Theorem 6.4 to the representation \(\rho\) of Example 5.4. Since \(\rho\) is injective, the factor \(M\) is full, of type III\(_1\), with separable
predual, so it acts standardly on a separable Hilbert space. By Example 5.4, \(\tau(M)\) is the usual topology of
\(\mathbb{R}\). If \(M\) had an almost periodic weight, Theorem 7.1(4) would give \(t_n\to\infty\) with
\(\delta_M(t_n)\to 1\), that is, \(t_n\to 0\) in the usual topology. This is absurd. A faithful normal state is an fns
weight, so there is no almost periodic state either. \(\square\)

The same proof shows more: if \(\tau(M)\) is not totally bounded, \(M\) has no almost periodic weight. This holds, for
example, whenever \(\mu\) in Lemma 5.2 is absolutely continuous with respect to Lebesgue measure on
\(\mathbb{R}_+^*\). Then \(\int\lambda^{it}\,d\mu(\lambda)\to 0\) as \(|t|\to\infty\) by the Riemann–Lebesgue lemma,
and the argument of Example 5.4 shows that \(\tau_\rho\) is the usual topology. At the other extreme, when \(\mu\) is
supported on countably many points, \(\Delta_\varphi\) is diagonal. Then the tensor product and direct sum structure
of Theorem 1.2(3) make \(\Delta_\psi\) diagonal too, and \(\psi\) is an almost periodic state. Example 5.5 with two
independent eigenvalues gives a full factor of type III\(_1\) with an almost periodic state.

In the rest of the lesson, \(M_\infty\) denotes the factor of Corollary 7.2. It is a full factor of type III\(_1\)
with separable predual and no almost periodic weight.

## 8. Crossed products by discrete groups and almost periodic weights

This section gives two tools about crossed products by countable discrete groups. The first recognizes a crossed
product. The second produces almost periodic weights on crossed products.

**Lemma 8.1 (recognizing a crossed product).** Consider a von Neumann algebra \(B\), a von Neumann subalgebra
\(Q\subset B\) with a faithful normal state \(\chi\), and a unitary representation \(g\mapsto v_g\) of a countable group
\(\mathcal{G}\) in \(B\) with \(v_gQv_g^* = Q\). Put \(\alpha_g = \operatorname{Ad}v_g|_Q\). Suppose \(B\) is
generated by \(Q\) and the \(v_g\), and that there is a faithful normal conditional expectation \(F : B\to Q\) with
\(F(v_g) = 0\) for \(g\neq e\). Then there is an isomorphism \(B\cong Q\rtimes_\alpha\mathcal{G}\) sending \(q\) to
\(\pi(q)\) and \(v_g\) to \(\lambda(g)\).

**Proof.** Let \(B_0\) be the linear span of the elements \(qv_g\). Since \(v_gq = \alpha_g(q)v_g\), \(B_0\) is a unital
\(*\)-algebra, and it is \(\sigma\)-weakly dense in \(B\). By the bimodule property, \(F(qv_g) = qF(v_g) = 0\) for
\(g\neq e\). An element \(x = \sum_g q_gv_g\) of \(B_0\) (finite sum) therefore has \(q_g = F(xv_g^*)\), so the
coefficients are unique. Hence \(\Phi_0(\sum q_gv_g) = \sum\pi(q_g)\lambda(g)\) is a well defined linear bijection
from \(B_0\) onto the analogous \(*\)-algebra \(B_0'\subset Q\rtimes_\alpha\mathcal{G}\). It is a \(*\)-homomorphism,
because both sides obey the same multiplication rule \(qv_g\,rv_h = q\alpha_g(r)v_{gh}\) and \((qv_g)^* =
\alpha_g^{-1}(q^*)v_{g^{-1}}\).

Let \(F'\) be the canonical conditional expectation of the crossed product, and put \(\psi = \chi\circ F\) and \(\psi'
= \chi\circ\pi^{-1}\circ F'\). Both are faithful normal states. For \(x = \sum_g q_gv_g\) and \(y = \sum_h r_hv_h\),
\[ \psi(y^*x) = \sum_{g,h}\chi\big(F(v_h^*r_h^*q_gv_g)\big) = \sum_g \chi\big(\alpha_g^{-1}(r_g^*q_g)\big), \]
since \(v_h^*r_h^*q_gv_g = \alpha_h^{-1}(r_h^*q_g)v_{h^{-1}g}\). The same computation in the crossed product gives
\(\psi'(\Phi_0(y)^*\Phi_0(x))\) the same value. So \(W : x\xi_\psi\mapsto\Phi_0(x)\xi_{\psi'}\) is isometric on
\(B_0\xi_\psi\). By the Kaplansky density theorem (Kaplansky's density theorem and its consequences, Theorem
7.1), \(B_0\xi_\psi\) is dense in \(L^2(B,\psi)\), and likewise
\(B_0'\xi_{\psi'}\) is dense. So \(W\) extends to a unitary. For \(x,y\in B_0\), \(Wx\,y\xi_\psi =
\Phi_0(xy)\xi_{\psi'} = \Phi_0(x)Wy\xi_\psi\), so \(WxW^* = \Phi_0(x)\). The standard representations are faithful and
normal, so \(\operatorname{Ad}W\) is an isomorphism from \(B = B_0''\) onto \((B_0')'' =
Q\rtimes_\alpha\mathcal{G}\) extending \(\Phi_0\). \(\square\)

**Proposition 8.2 (almost periodic weights on crossed products).** Let \(\alpha\) be an action of a countable group
\(\mathcal{G}\) on a von Neumann algebra \(N\) with an fns trace \(\tau\). Let \(M = N\rtimes_\alpha\mathcal{G}\) with
canonical conditional expectation \(F\), and identify \(N\) with \(\pi(N)\). Write \(\tau\circ\alpha_g = \tau(h_g\,\cdot)\),
with \(h_g\) positive, nonsingular and affiliated with the centre of \(N\). Suppose each \(h_g\) has pure point
spectrum: \(h_g = \sum_{c\in C}c\,e_{g,c}\) for a countable set \(C\subset\mathbb{R}_+^*\) and central projections
\(e_{g,c}\) with \(\sum_ce_{g,c} = 1\). Then the weight \(\varphi = \tau\circ F\) on \(M\) is almost periodic, and the
eigenvalues of \(\Delta_\varphi\) lie in the subgroup generated by \(C\).

**Proof.** \(\varphi\) is an fns weight, because \(F\) is a faithful normal conditional expectation. Since
\(\sigma^\tau\) is trivial, \(\sigma^\varphi_t\) is the identity on \(N\). So \(N\subset M_\varphi\), and
\(\varphi|_N = \tau\) is semifinite. Hence \(\varphi\) is strictly semifinite: take projections \(e_i\in N\) with
\(\tau(e_i)<\infty\) increasing to \(1\); for \(x\in M_\varphi\), \(xe_i\in M_\varphi\), \(\varphi(e_ix^*xe_i)\le
\|x\|^2\tau(e_i)<\infty\), and \(xe_i\to x\) strongly.

Let \(u = \lambda(g)\). On \(M\) we have \(F(uxu^*) = \alpha_g(F(x))\). This holds on the dense \(*\)-algebra of finite
sums \(\sum_k x_k\lambda(k)\), since \(u\,x_k\lambda(k)\,u^* = \alpha_g(x_k)\lambda(gkg^{-1})\), and extends by
normality. Hence
\[ \varphi\circ\operatorname{Ad}u = \tau\circ\alpha_g\circ F = \tau(h_g\,\cdot)\circ F. \]
Using the background facts on cocycles,
\[ u^*\sigma^\varphi_t(u) = (D(\varphi\circ\operatorname{Ad}u):D\varphi)_t = (D(\tau(h_g\,\cdot)\circ F) : D(\tau\circ
F))_t = (D\tau(h_g\,\cdot):D\tau)_t = h_g^{it}. \]
So \(\sigma^\varphi_t(\lambda(g)) = \lambda(g)h_g^{it}\), and since \(e_{g,c}\in N\) is fixed,
\[ \sigma^\varphi_t(\lambda(g)e_{g,c}) = \lambda(g)h_g^{it}e_{g,c} = c^{it}\,\lambda(g)e_{g,c}. \]
Let \(\Lambda\) be the subgroup generated by \(C\), and take \(S = N\cup\{\lambda(g)e_{g,c} : g\in\mathcal{G},
c\in C\}\). This set generates \(M\), since \(\sum_c\lambda(g)e_{g,c} = \lambda(g)\) strongly. For \(x\in N\), take
\(f_x\) constant. For \(x = \lambda(g)e_{g,c}\), take \(f_x(s) = s(c)x\), which is norm continuous on \(G_\Lambda\),
and \(f_x(\hat\beta(t)) = c^{it}x = \sigma^\varphi_t(x)\). Theorem 1.4 now applies. \(\square\)

## 9. Ergodic transformation groups with uncountably many Radon–Nikodym values

We now realize the factor \(M_\infty\) of Corollary 7.2, and more generally every factor of Theorem 6.4, as a group
measure space factor.

Let \(\mu\) and \(\varphi\) be as in (6.1). Put \(Y = \mathbb{R}_+^*\times\{1,2\}\) with the probability measure
\[ \nu_Y(B\times\{1\}) = c\,\mu(B),\qquad \nu_Y(B\times\{2\}) = c\int_B\lambda\,d\mu(\lambda). \]
Let \(r : Y\to Y\) be the flip \(r(\lambda,i) = (\lambda,3-i)\). It is nonsingular, because \(\mu\) and \(\lambda\mu\)
are equivalent. The diagonal subalgebra \(A\subset P\) is \(L^\infty(Y,\nu_Y)\), with \(f_{11}e_{11} + f_{22}e_{22}\)
corresponding to the function equal to \(f_{ii}\) on \(\mathbb{R}_+^*\times\{i\}\). Under this identification,
\(\varphi|_A\) is integration against \(\nu_Y\). Let \(w = e_{12}+e_{21}\in P\). Then \(waw = a\circ r\) for \(a\in A\),
and \(P\) is generated by \(A\) and \(w\). Moreover \(\varphi(aw) = 0\) for \(a\in A\), because \(aw\) has zero diagonal.

Let \(X = Y^{\mathbb{F}_2}\) with the product probability measure \(\nu = \nu_Y^{\otimes\mathbb{F}_2}\). Let
\(\mathcal{G} = (\mathbb{Z}/2)^{(\mathbb{F}_2)}\rtimes\mathbb{F}_2\). The normal subgroup consists of the finite
subsets \(F\) of \(\mathbb{F}_2\) under symmetric difference, \(\mathbb{F}_2\) acts on it by left translation, and the
product is \((F,s)(F',s') = (F\mathbin{\triangle}sF',ss')\). The group \(\mathcal{G}\) acts on \(X\) by
\[ (T_{(F,s)}x)(u) = r^{[u\in F]}\big(x(s^{-1}u)\big), \]
where \(r^{[u\in F]}\) is \(r\) if \(u\in F\) and the identity otherwise. Each \(T_g\) is nonsingular for \(\nu\).
Indeed, a shift preserves the product measure, and \(T_{(F,e)}\) applies the nonsingular map \(r\) to finitely many
coordinates. A direct computation shows that \(g\mapsto T_g\) is an action.

**Theorem 9.1.** Let \(M\) and \(\psi\) be built from \((P,\varphi)\) as in Theorem 1.2. Then \(M\cong
L^\infty(X,\nu)\rtimes\mathcal{G}\), where \(\mathcal{G}\) acts by \(\alpha_g(f) = f\circ T_g^{-1}\). Moreover
\(\mathcal{G}\) acts ergodically on \((X,\nu)\).

**Proof.** Inside \(N = \bigotimes_s(P,\varphi)\), consider the von Neumann subalgebra \(Q\) generated by the
\(\pi_s(A)\), \(s\in\mathbb{F}_2\). The state \(\omega\) is faithful on \(Q\). The closure of \(Q\eta_0\), where
\(\eta_0\) is the product vector, is \(\bigotimes_s(\overline{A\xi_\varphi},\xi_\varphi) \cong
\bigotimes_s(L^2(Y,\nu_Y),1) = L^2(X,\nu)\). On it, \(Q\) acts by multiplication by functions of finitely many
coordinates and their weak limits, that is, as \(L^\infty(X,\nu)\). Since the representation of \(Q\) on the closure
of \(Q\eta_0\) is the representation of the faithful normal state \(\omega|_Q\), it is faithful and normal. So
\(Q\cong L^\infty(X,\nu)\), with \(\pi_u(a)\) corresponding to the function \(x\mapsto a(x(u))\).

For a finite set \(F\subset\mathbb{F}_2\) put \(w_F = \prod_{u\in F}\pi_u(w)\). These are commuting self-adjoint
unitaries with \(w_Fw_{F'} = w_{F\triangle F'}\). Put \(v_{(F,s)} = w_FU_s\). Since \(U_sw_{F'}U_s^* = \theta_s(w_{F'})
= w_{sF'}\),
\[ v_{(F,s)}v_{(F',s')} = w_Fw_{sF'}U_{ss'} = v_{(F\triangle sF',ss')}, \]
so \(v\) is a unitary representation of \(\mathcal{G}\). Next, \(\operatorname{Ad}v_g\) maps \(Q\) onto \(Q\) and
agrees with \(\alpha_g\) there. It suffices to check this on generators. We have \(\operatorname{Ad}U_s(\pi_u(a)) =
\pi_{su}(a)\), which is the function \(x\mapsto a(x(su))\), and this equals \(a(\cdot(u))\circ T_{(\emptyset,s)}^{-1}\)
since \((T_{(\emptyset,s)}^{-1}x)(u) = x(su)\). Similarly \(\operatorname{Ad}\pi_u(w)\) replaces \(\pi_u(a)\) by
\(\pi_u(a\circ r)\) and fixes \(\pi_{u'}(a)\) for \(u'\neq u\), which is composition with the flip of coordinate \(u\).
Two normal automorphisms of \(Q\) that agree on a generating set are equal.

\(M\) is generated by \(Q\) and the \(v_g\), because \(N\) is generated by the \(\pi_u(P)\), each \(P\) by \(A\) and
\(w\), and \(M\) by \(N\) and the \(U_s\). The \(\sigma^\omega\)-invariance of \(Q\) follows from
\(\sigma^\omega_t = \bigotimes\sigma^\varphi_t\) and (6.2): \(\sigma^\varphi_t\) fixes \(A\) pointwise, so
\(\sigma^\omega_t\) fixes \(Q\) pointwise. By Takesaki's theorem there is an \(\omega\)-preserving faithful normal
conditional expectation \(E_Q : N\to Q\). Let \(E : M\to N\) be the conditional expectation of Theorem 1.2(5), and put \(F_0 = E_Q\circ E : M\to Q\). This is a faithful normal conditional
expectation. For \(s\neq e\), \(F_0(w_FU_s) = E_Q(w_FE(U_s)) = 0\) by Theorem 1.2(5). For \(F\neq\emptyset\) and an elementary product
\(q = \prod_u\pi_u(a_u)\) with \(a_u \in A\), finitely many different from \(1\),
\[ \omega(qw_F) = \prod_{u\in F}\varphi(a_uw)\prod_{u\notin F}\varphi(a_u) = 0. \]
The linear span of such \(q\) is \(\sigma\)-weakly dense in \(Q\), so \(\omega(qw_F) = 0\) for all \(q\in Q\). Hence
\(\omega(qE_Q(w_F)) = 0\) for all \(q\in Q\). Taking \(q = E_Q(w_F)^*\) and using faithfulness, \(E_Q(w_F) = 0\).
Thus \(F_0(v_g) = 0\) for \(g\neq e\). Lemma 8.1 gives \(M\cong Q\rtimes\mathcal{G} = L^\infty(X,\nu)\rtimes
\mathcal{G}\).

Finally, if \(f\in L^\infty(X,\nu)\) is \(\mathcal{G}\)-invariant, then it commutes with \(Q\) and with every \(v_g\),
so it is central in the factor \(M\) and hence constant. So the action is ergodic. \(\square\)

**Theorem 9.2.** There is a standard probability space \((X,\nu)\) and a countable group \(\mathcal{G}\) of
nonsingular transformations of it, acting ergodically, with the following property. For every \(\sigma\)-finite
measure \(\nu'\) equivalent to \(\nu\), there is no countable set \(C\subset\mathbb{R}_+^*\) such that for every
\(g\in\mathcal{G}\) the Radon–Nikodym derivative \(d(\nu'\circ T_g)/d\nu'\) takes its values in \(C\)
\(\nu'\)-almost everywhere. In this sense the Radon–Nikodym derivatives take uncountably many values, for every choice
of equivalent measure.

*Reference:* [Connes 1974, Corollary 5.4].

**Proof.** Let \(\rho\) be the representation of Example 5.4 and \(\mu\) the measure that Lemma 5.2 gives for it,
so that the factor of Theorem 6.4 is \(M_\infty\).
Take \((X,\nu)\) and \(\mathcal{G}\) as in Theorem 9.1, so \(M_\infty\cong L^\infty(X,\nu)\rtimes\mathcal{G}\) and the
action is ergodic. (If some \(T_g\) acts trivially, replace \(\mathcal{G}\) by its image in the group of
transformations; the set of Radon–Nikodym derivatives is unchanged.) Suppose \(\nu'\sim\nu\) and \(C\) countable are
as excluded in the statement. Let \(\tau(f) = \int f\,d\nu'\), an fns trace on \(L^\infty(X,\nu)\). With the change
of variables \(y = T_g^{-1}x\),
\[ \tau(\alpha_g(f)) = \int f(T_g^{-1}x)\,d\nu'(x) = \int f\,d(\nu'\circ T_g) = \int f\,h_g\,d\nu',\qquad h_g =
\frac{d(\nu'\circ T_g)}{d\nu'}. \]
By assumption \(h_g = \sum_{c\in C}c\,1_{\{h_g = c\}}\) almost everywhere. Proposition 8.2 makes \(\tau\circ F\) an
almost periodic weight on \(M_\infty\), contradicting Corollary 7.2. \(\square\)

## 10. No discrete decomposition

Every factor of type III\(_\lambda\) with \(0\le\lambda<1\) and separable predual is a crossed product of a
semifinite algebra by \(\mathbb{Z}\) [Connes 1973, Theorems 4.4.1 and 5.3.1]. A factor with separable predual and an almost periodic weight is,
after tensoring with \(B(\ell^2)\), a crossed product of a semifinite algebra by a countable discrete abelian group
([Almost periodic weights and the invariant \(Sd\), Lemma 7.2](almost-periodic-weights-and-the-invariant-sd.html#section-7.2)). The factor \(M_\infty\) has no such
decomposition.

**Theorem 10.1.** Let \(M\) be a factor whose predual is separable. Suppose \(M\cong N\rtimes_\alpha D\) with \(N\)
semifinite and \(D\) a discrete abelian group. Then either \(M\) is not full, or \(M\) has an almost periodic weight.
Consequently \(M_\infty\) is not isomorphic to any crossed product \(Q\rtimes D\) with \(Q\) semifinite and \(D\)
discrete abelian.

*Reference:* [Connes 1974, Corollary 5.5].

**Proof.** Identify \(M\) with \(N\rtimes_\alpha D\), \(N\) with its image, and let \(u_d = \lambda(d)\) and \(F\) the
canonical conditional expectation. First, \(D\) is countable and \(N\) has separable predual. Fix a faithful normal
state \(\chi\) of \(N\) (for instance the restriction of one on \(M\)). The vectors \(u_d\xi\) are orthonormal in
\(L^2(M,\chi\circ F)\), because \(\chi(F(u_e^*u_d)) = \delta_{d,e}\), and that space is separable. Also \(\omega\mapsto
\omega\circ F\) embeds \(N_*\) isometrically into \(M_*\).

Let \(Z\) be the centre of \(N\). Each \(\alpha_d\) restricts to an automorphism of \(Z\). If \(z\in Z\) is fixed by all
\(\alpha_d\), then \(z\) commutes with \(N\) and with every \(u_d\), so \(z\) is central in \(M\) and scalar. So \(D\)
acts ergodically on \(Z\).

*Case 1: \(Z\) is diffuse.* By Theorem 1.5, \(M\) is not full.

*Case 2: \(Z\) has a minimal projection \(p\).* Each \(\alpha_d(p)\) is again a minimal projection of \(Z\). The
supremum of the \(\alpha_d(p)\) is a nonzero projection of \(Z\) fixed by \(D\), hence equal to \(1\). So \(Z\) is
atomic. Let \((p_i)_{i\in I}\) be its minimal projections; \(I\) is countable. Let \(\tau\) be an fns trace on \(N\).
By the background facts, \(\tau\circ\alpha_d = \tau(h_d\,\cdot)\) with \(h_d\) positive, nonsingular and affiliated
with \(Z\). Such an operator has the form \(h_d = \sum_ic_{d,i}p_i\) with \(0<c_{d,i}<\infty\). The set \(C =
\{c_{d,i}\}\) is countable. By Proposition 8.2, the weight \(\tau\circ F\) on \(M\) is almost periodic.

The factor \(M_\infty\) is full and has no almost periodic weight (Corollary 7.2). Both properties are preserved by
isomorphisms, so \(M_\infty\) is not isomorphic to such a crossed product. \(\square\)

The proof shows a little more. For a full factor \(M = N\rtimes D\) with \(N\) semifinite and \(D\) discrete abelian,
the centre of \(N\) is atomic, and the weight dual to any fns trace of \(N\) is almost periodic.

## 11. Crossed products by locally compact abelian groups

By the continuous decomposition, every type III factor is a crossed product of a semifinite algebra by
\(\mathbb{R}\). We ask for which locally compact abelian groups \(G\) the same holds with \(G\) in place of
\(\mathbb{R}\). All groups here are second countable, and all factors have separable predual.

**Lemma 11.1.** A second countable locally compact abelian group \(G\) has a closed subgroup isomorphic to
\(\mathbb{R}\) if and only if it has no compact open subgroup. In that case \(G\cong\mathbb{R}\times G''\) for some
locally compact abelian group \(G''\).

**Proof.** Write \(G\cong\mathbb{R}^n\times G_0\) with \(G_0\) having a compact open subgroup \(K_0\). If
\(n\ge 1\), then \(\mathbb{R}\times\{0\}\) is a closed copy of \(\mathbb{R}\), and \(G\cong\mathbb{R}\times G''\) with
\(G'' = \mathbb{R}^{n-1}\times G_0\). Suppose \(G\) has a compact open subgroup \(K\) and a closed subgroup \(H\cong
\mathbb{R}\). Then \(H\cap K\) is an open subgroup of \(H\). Since \(\mathbb{R}\) is connected, \(H\cap K = H\). So
\(H\) is a closed subset of the compact set \(K\), hence compact, which \(\mathbb{R}\) is not. Finally, if \(n = 0\),
then \(K_0\) is a compact open subgroup of \(G\). So having a closed copy of \(\mathbb{R}\), having no compact open
subgroup, and \(n\ge1\) are all equivalent. \(\square\)

**Lemma 11.2.** Let \(M\) be a type III factor with separable predual and \(\mathcal{K}\) a nonzero separable
Hilbert space. Then \(M\mathbin{\bar\otimes}B(\mathcal{K})\cong M\).

**Proof.** \(M\mathbin{\bar\otimes}B(\mathcal{K})\) is a factor of type III with separable predual. Let \(e\) be a
rank-one projection in \(B(\mathcal{K})\). The projections \(1\otimes e\) and \(1\) are nonzero, hence equivalent: \(1
= vv^*\) and \(1\otimes e = v^*v\) for a partial isometry \(v\). Then \(x\mapsto v^*xv\) is an isomorphism of
\(M\mathbin{\bar\otimes}B(\mathcal{K})\) onto \((1\otimes e)(M\mathbin{\bar\otimes}B(\mathcal{K}))(1\otimes e)\cong
M\). \(\square\)

**Theorem 11.3.** Let \(G\) be a second countable locally compact abelian group with a closed subgroup isomorphic
to \(\mathbb{R}\). Then every factor \(M\) of type III with separable predual is isomorphic to \(Q\rtimes G\) for some
semifinite von Neumann algebra \(Q\) and some continuous action of \(G\).

**Proof.** By Lemma 11.1, \(G\cong\mathbb{R}\times G''\). Fix a faithful normal state \(\varphi\) of \(M\) and put
\(Q_0 = M\rtimes_{\sigma^\varphi}\mathbb{R}\), a semifinite algebra with the dual action \(\beta\) of
\(\hat{\mathbb{R}}\cong\mathbb{R}\). By Takesaki duality and Lemma 11.2,
\(Q_0\rtimes_\beta\mathbb{R}\cong M\mathbin{\bar\otimes}B(L^2(\mathbb{R}))\cong M\). Let \(G''\) act on
\(L^\infty(G'')\) by translation \(\gamma\). Takesaki duality for the trivial action of \(\hat{G''}\) on
\(\mathbb{C}\) identifies \(L^\infty(G'')\rtimes_\gamma G''\) with \(B(L^2(G''))\), since
\(\mathbb{C}\rtimes\hat{G''}\) is the group von Neumann algebra of \(\hat{G''}\), which the Fourier transform identifies
with \(L^\infty(G'')\), and the dual action becomes translation. Let \(G = \mathbb{R}\times G''\) act on
\(Q = Q_0\mathbin{\bar\otimes}L^\infty(G'')\) by \(\beta\otimes\gamma\). The crossed product of a tensor product action
of a product group is the tensor product of the crossed products, as one sees from the definition on
\(L^2(\mathbb{R}\times G'', \mathcal{H}\otimes L^2(G''))\). So
\[ Q\rtimes G\cong(Q_0\rtimes_\beta\mathbb{R})\mathbin{\bar\otimes}(L^\infty(G'')\rtimes_\gamma G'')\cong
M\mathbin{\bar\otimes}B(L^2(G''))\cong M, \]
using Lemma 11.2 once more (\(L^2(G'')\) is separable and nonzero). The algebra \(Q\) is semifinite, as the tensor
product of a semifinite algebra with an abelian one. \(\square\)

For the converse direction we use the dual action. Let \(G\) have a compact open subgroup \(K\), let
\(L = K^\perp\subset\hat G\), a compact open subgroup, and \(D = G/K\), a countable discrete group. By Pontryagin
duality, \(D\) is the dual of \(L\): the coset \(g+K\) is the character \(\chi\mapsto\chi(g)\) of \(L\).

**Lemma 11.4.** Let \(M = Q\rtimes_\alpha G\) and restrict the dual action \(\hat\alpha\) to \(L\). The fixed-point
algebra \(M^L\) is the von Neumann algebra \(R_K\) generated by \(\pi(Q)\) and \(\lambda(K)\). For \(g\in G\),
\(\lambda(g)\) satisfies \(\hat\alpha_\chi(\lambda(g)) = \overline{\chi(g+K)}\lambda(g)\) for \(\chi\in L\).

**Proof.** The last formula is the definition of \(\hat\alpha\), noting that \(\chi(g)\) depends only on \(g+K\) for
\(\chi\in L\). Let \(E_L(x) = \int_L\hat\alpha_\chi(x)\,d\chi\), a faithful normal conditional expectation onto
\(M^L\). For \(x = \pi(a)\lambda(g)\),
\[ E_L(x) = \Big(\int_L\overline{\chi(g)}\,d\chi\Big)x, \]
and the integral is \(1\) if \(g\in K\) and \(0\) otherwise, since \(\chi\mapsto\chi(g)\) is a character of \(L\), trivial
exactly when \(g\in L^\perp = K\). The span \(B_0\) of the elements \(\pi(a)\lambda(g)\) is a \(\sigma\)-weakly dense
\(*\)-subalgebra of \(M\), and \(E_L(B_0)\subset R_K\). By normality \(M^L = E_L(M)\subset R_K\). The reverse
inclusion holds because \(\pi(Q)\) and \(\lambda(K)\) are fixed by \(L\). \(\square\)

**Lemma 11.5 (stabilization).** Let \(\gamma\) be a continuous action of a compact abelian group \(L\) with countable
dual \(D\) on a von Neumann algebra \(M\) whose predual is separable. For \(d\in D\) let \(M_d = \{x\in M :
\gamma_\chi(x) = \overline{d(\chi)}x \text{ for all } \chi\}\). Suppose each \(M_d\) contains a unitary \(w_d\). Then
\[ M\mathbin{\bar\otimes}B(\ell^2(D))\cong\big(M^\gamma\mathbin{\bar\otimes}B(\ell^2(D))\big)\rtimes D. \]

**Proof.** Write the group law of \(D\) additively. Then \(M_dM_e\subset M_{d+e}\), \(M_d^* = M_{-d}\) and
\(M_0 = M^\gamma\). The maps \(E_d(x) = \int_L d(\chi)\gamma_\chi(x)\,d\chi\) are normal projections of \(M\) onto
\(M_d\). The span of \(\bigcup_dM_d\) is \(\sigma\)-weakly dense in \(M\). Indeed, if \(\omega\in M_*\) annihilates
every \(M_d\), then for each \(x\) the continuous function \(f(\chi) = \omega(\gamma_\chi(x))\) on \(L\) has all Fourier
coefficients \(\int_L d(\chi)f(\chi)\,d\chi = \omega(E_d(x))\) equal to zero. So \(f = 0\) (by uniqueness of
the Fourier transform of the measure \(f(\chi)\,d\chi\), The Pontryagin duality theorem, Corollary
4.2, and continuity of \(f\)), and \(\omega(x) = f(1) =
0\).

Let \(\mathcal{M} = M\mathbin{\bar\otimes}B(\ell^2(D))\), viewed as \(D\times D\) matrices over \(M\), with matrix
units \(e_{ab}\). Let \(Z = \sum_aw_a\otimes e_{aa}\), a unitary. For \(x\in M_0\),
\[ Z(x\otimes e_{ab})Z^* = w_axw_b^*\otimes e_{ab}, \qquad w_axw_b^*\in M_{a-b}. \]
Define \(\tilde\gamma_\chi = \gamma_\chi\otimes\operatorname{Ad}m_\chi\), where \(m_\chi e_a = d_a(\chi)e_a\) and
\(d_a(\chi)\) denotes the pairing of \(a\in D\) with \(\chi\in L\). This is a continuous action of \(L\) on
\(\mathcal{M}\). For \(y\in M_c\),
\(\tilde\gamma_\chi(y\otimes e_{ab}) = \overline{c(\chi)}\,a(\chi)\,\overline{b(\chi)}\,y\otimes e_{ab}\). So a matrix
\(X = (x_{ab})\) is fixed if and only if \(x_{ab}\in M_{a-b}\) for all \(a,b\). Put \(\mathcal{P} =
\mathcal{M}^{\tilde\gamma}\). The entries of \(Z^*XZ\) are \(w_a^*x_{ab}w_b\), and these lie in \(M_0\) exactly when
\(x_{ab}\in M_{a-b}\). A bounded matrix with all entries in \(M_0\) lies in \(M_0\mathbin{\bar\otimes}B(\ell^2(D))\).
Hence \(\mathcal{P} = Z(M_0\mathbin{\bar\otimes}B(\ell^2(D)))Z^*\cong M^\gamma\mathbin{\bar\otimes}B(\ell^2(D))\).

Let \(U_d = 1\otimes\lambda_d\) with \(\lambda_de_a = e_{a+d}\), a unitary representation of \(D\). A direct computation
gives \(m_\chi\lambda_dm_\chi^* = d(\chi)\lambda_d\), so \(\tilde\gamma_\chi(U_d) = d(\chi)U_d\). So \(U_d\mathcal{P}U_d^* = \mathcal{P}\), since conjugation
by \(U_d\) commutes with \(\tilde\gamma\) up to the scalar factors, which cancel. The faithful normal conditional
expectation \(\mathcal{F} = \int_L\tilde\gamma_\chi\,d\chi\) onto \(\mathcal{P}\) satisfies \(\mathcal{F}(U_d) =
\big(\int_Ld(\chi)\,d\chi\big)U_d = 0\) for \(d\neq 0\). Finally, \(\mathcal{P}\) and the \(U_d\) generate
\(\mathcal{M}\). For \(y\in M_c\),
\[ y\otimes e_{ab} = (y\otimes e_{a,a-c})(1\otimes e_{a-c,a-c})U_{a-c-b}, \]
where the first two factors lie in \(\mathcal{P}\). Elements \(y\otimes e_{ab}\) with \(y\in\bigcup_cM_c\) span a
\(\sigma\)-weakly dense subspace of \(\mathcal{M}\). Since \(\mathcal{P}\) has a faithful normal state, Lemma 8.1
gives \(\mathcal{M}\cong\mathcal{P}\rtimes D\). \(\square\)

**Theorem 11.6.** Let \(G\) be a second countable locally compact abelian group with no closed subgroup isomorphic
to \(\mathbb{R}\), and \(K\) a compact open subgroup. Suppose \(M_\infty\cong Q\rtimes_\alpha G\) with \(Q\)
semifinite. Then the subalgebra \(R_K\) generated by \(\pi(Q)\) and \(\lambda(K)\) is not semifinite. In particular
\(Q\) has no fns trace \(\tau\) with \(\tau\circ\alpha_k = \tau\) for all \(k\in K\), and \(Q\) is not a factor.

**Proof.** Suppose \(R_K\) is semifinite. Apply Lemma 11.5 to the restriction to \(L = K^\perp\) of the dual action
on \(M_\infty = Q\rtimes G\). For \(d = g+K\in D\), the unitary \(\lambda(g)\) lies in \(M_d\) by Lemma 11.4, and
\(M^L = R_K\). So
\[ M_\infty\cong M_\infty\mathbin{\bar\otimes}B(\ell^2(D))\cong\big(R_K\mathbin{\bar\otimes}B(\ell^2(D))\big)\rtimes D,
\]
using Lemma 11.2 for the first isomorphism. Here \(R_K\mathbin{\bar\otimes}B(\ell^2(D))\) is semifinite and \(D\) is
discrete abelian. This contradicts Theorem 10.1.

Next suppose that \(Q\) has an fns trace \(\tau\) with \(\tau\circ\alpha_k = \tau\) for \(k\in K\). Let
\(\tilde\tau\) be the dual weight on \(M_\infty = Q\rtimes G\). Since \((D(\tau\circ\alpha_k):D\tau)_t = 1\) for
\(k\in K\),
\[ \sigma^{\tilde\tau}_t(\pi(x)) = \pi(x),\qquad \sigma^{\tilde\tau}_t(\lambda(k)) = \lambda(k)\qquad(x\in Q,\ k\in K). \]
So \(\sigma^{\tilde\tau}_t\) fixes the generators of \(R_K\), hence \(R_K\) pointwise. Thus \(R_K\subset
(M_\infty)_{\tilde\tau}\), and \(\tilde\tau\) restricts to a faithful normal trace on \(R_K\). It is also semifinite.
Indeed, \(\tilde\tau\) is \(\hat\alpha\)-invariant, so for \(x\ge 0\) and every normal positive functional
\(\omega\le\tilde\tau\) we have \(\omega(E_L(x)) = \int_L\omega(\hat\alpha_\chi(x))\,d\chi\le\tilde\tau(x)\); taking the
supremum over \(\omega\) gives \(\tilde\tau(E_L(x))\le\tilde\tau(x)\). By the Kadison–Schwarz inequality (Contractive retractions and the algebraic structure of expectations,
§CE-006)
\(E_L(x)^*E_L(x)\le E_L(x^*x)\), so \(E_L\) maps \(\mathfrak{n}_{\tilde\tau}\) into \(\mathfrak{n}_{\tilde\tau}\cap
R_K\). Taking a net in \(\mathfrak{n}_{\tilde\tau}\) converging \(\sigma\)-weakly to \(1\) and applying \(E_L\) shows
that \(\mathfrak{n}_{\tilde\tau}\cap R_K\) is \(\sigma\)-weakly dense in \(R_K\). So \(R_K\) is semifinite, which the
first part excludes.

Finally let \(Q\) be a semifinite factor with fns trace \(\tau\). Each \(\tau\circ\alpha_g\) is an fns trace on the
factor \(Q\), so \(\tau\circ\alpha_g = c(g)\tau\) with \(c(g) > 0\). Then \(c\) is a homomorphism
\(G\to\mathbb{R}_+^*\). It is continuous. Fix \(x\ge0\) with \(0<\tau(x)<\infty\), so that
\(c(g) = \tau(\alpha_g(x))/\tau(x)\). The function \(g\mapsto\tau(\alpha_g(x))\) is lower semicontinuous, as a supremum of
the continuous functions \(g\mapsto\omega(\alpha_g(x))\) over normal positive functionals \(\omega\le\tau\). So \(c\) is
lower semicontinuous, and so is \(g\mapsto c(g^{-1}) = c(g)^{-1}\); hence \(c\) is also upper semicontinuous, and therefore continuous. Its
restriction to \(K\) has compact image, and the only compact subgroup of \(\mathbb{R}_+^*\) is \(\{1\}\). So
\(\tau\circ\alpha_k = \tau\) for \(k\in K\), which the second part excludes. \(\square\)

**Corollary 11.7.** Let \(G\) be a second countable locally compact abelian group. Consider the statements:

1. every factor of type III with separable predual is isomorphic to \(Q\rtimes G\) for some semifinite von Neumann
   algebra \(Q\) and some continuous action of \(G\);
2. \(G\) has a closed subgroup isomorphic to \(\mathbb{R}\).

Then (2) implies (1). If (2) fails and \(K\) is a compact open subgroup of \(G\), then \(M_\infty\) is not a crossed
product \(Q\rtimes_\alpha G\) with \(Q\) semifinite and \(R_K\) semifinite. In particular it is not such a crossed
product with \(Q\) a semifinite factor, or with \(Q\) carrying an fns trace invariant under \(\alpha|_K\).

*Reference:* [Connes 1974, Corollary 5.6] states that (1) and (2) are equivalent. The argument there for
"(1) implies (2)" uses that a crossed product of a semifinite algebra by a compact abelian group is semifinite. We do
not prove that step here in general, so we state the converse only in the form above.

**Proof.** Theorem 11.3 and Theorem 11.6, with Lemma 11.1. \(\square\)

When \(G\) is discrete, \(K = \{0\}\) and \(R_K = \pi(Q)\) is semifinite by assumption. So for discrete abelian \(G\),
statement (1) fails outright, which is Theorem 10.1 again.

## 12. Exercises

**Exercise 12.1.** Let \(m_1\) and \(m_2\) be equivalent finite measures and \(g_n\) measurable functions. Show that
\(g_n\to 1\) in \(m_1\)-measure if and only if \(g_n\to 1\) in \(m_2\)-measure.

*Solution.* By symmetry it suffices to prove one direction. Let \(\varepsilon,\varepsilon'>0\). Since
\(m_2\ll m_1\) and \(m_2\) is finite, there is \(\eta>0\) with \(m_1(B)<\eta\Rightarrow m_2(B)<\varepsilon'\).
(Otherwise there are sets \(B_k\) with \(m_1(B_k)<2^{-k}\) and \(m_2(B_k)\ge\varepsilon'\). Then \(B =
\limsup B_k\) has \(m_1(B) = 0\) by the Borel–Cantelli lemma but \(m_2(B)\ge\varepsilon'\) by continuity from above
for the finite measure \(m_2\), a contradiction.) If \(g_n\to 1\) in \(m_1\)-measure, then \(B_n = \{|g_n-1|\ge
\varepsilon\}\) has \(m_1(B_n)<\eta\) for large \(n\), hence \(m_2(B_n)<\varepsilon'\).

**Exercise 12.2.** Let \(0<\lambda_0<1\) and let \(\rho(t) = \lambda_0^{it}\) on \(\mathbb{C}\). Let \(M\) and \(\psi\)
be the factor and state of Theorem 6.4, built with \(\mu = \delta_{\lambda_0}\). Show that \(\psi\) is almost periodic
with eigenvalues \(\lambda_0^{\mathbb{Z}}\), that \(T(M) = 2\pi\mathbb{Z}/|\log\lambda_0|\), and that \(\tau(M)\) is
the topology pulled back from \(\mathbb{T}\) by \(t\mapsto\lambda_0^{it}\).

*Solution.* Here \(P = M_2(\mathbb{C})\) and \(\varphi = c\operatorname{Tr}(\operatorname{diag}(1,\lambda_0)\,\cdot)\).
By Lemma 6.1, \(\Delta_\varphi\) has eigenvalues \(1\) (on \(\mathcal{H}_{11}\oplus\mathcal{H}_{22}\)),
\(\lambda_0\) (on \(\mathcal{H}_{21}\)) and \(\lambda_0^{-1}\) (on \(\mathcal{H}_{12}\)). Choose an orthonormal
eigenbasis of \(L^2(P,\varphi)\) containing \(\xi_\varphi\). The product vectors built from it, with all but finitely
many factors equal to \(\xi_\varphi\), form an orthonormal basis of \(\bigotimes_s(L^2(P,\varphi),\xi_\varphi)\)
consisting of eigenvectors of \(\Delta_\omega = \bigotimes_s\Delta_\varphi\). The eigenvalues are finite products of
\(1,\lambda_0,\lambda_0^{-1}\), and every element of \(\lambda_0^{\mathbb{Z}}\) occurs. By Theorem 1.2(3),
\(\Delta_\psi\) is a direct sum of copies of \(\Delta_\omega\), so it is diagonal with the same eigenvalues. So
\(\psi\) is almost periodic. By Theorem 6.4, \(\tau(M) = \tau_\rho\), and by Lemma 5.1 and Proposition 3.3(3),
\(T(M) = \ker\rho = \{t : \lambda_0^{it} = 1\} = 2\pi\mathbb{Z}/|\log\lambda_0|\). The topology \(\tau_\rho\) is the
weakest one making \(t\mapsto\lambda_0^{it}\in\mathbb{T}\) continuous, which is the pulled-back topology.

**Exercise 12.3.** Show that \(\tau_\rho\) is totally bounded when \(\rho\) is a finite direct sum of characters
\(t\mapsto\lambda_j^{it}\), and that it is not totally bounded when \(\rho\) is the representation of Example 5.4.

*Solution.* In the first case \(\tau_\rho\) is pulled back from the compact group \(\mathbb{T}^k\) by
\(t\mapsto(\lambda_j^{it})_j\). The argument of Theorem 7.1(3) (with \(\mathbb{T}^k\) in place of \(G_\Lambda\), and
the closure of the image in place of the whole group) shows total boundedness. In the second case \(\tau_\rho\) is the
usual topology. The neighbourhood \(V = (-1,1)\) has no finite family of translates covering \(\mathbb{R}\), since
\(m\) translates cover a set of length at most \(2m\).

**Exercise 12.4.** Let \(M\), \(\psi\), \(U_a\), \(U_b\) be as in Theorem 1.2. Show directly that if \(u_n\) are
unitaries in \(M\) with \(\operatorname{Ad}u_n\to\mathrm{id}\), then there are scalars \(\mu_n\) of modulus one with
\(u_n - \mu_n1\to 0\) \(*\)-strongly.

*Solution.* This is the proof of Lemma 4.1 with \(\alpha_n = \mathrm{id}\) and \(\beta_n = \operatorname{Ad}u_n\).
From \(\operatorname{Ad}u_n^*\to\mathrm{id}\) and Lemma 2.2, \(\|u_n^*U_ju_n - U_j\|_\psi\to 0\), hence
\(\|[u_n,U_j]\|_\psi\to 0\) for \(j = a,b\). Inequality (1.1) gives \(\|u_n - \psi(u_n)1\|_\psi\to 0\), so
\(|\psi(u_n)|\to 1\). With \(\mu_n = \psi(u_n)/|\psi(u_n)|\) for large \(n\), \(\|u_n - \mu_n1\|_\psi\to 0\) and
\(\|u_n^* - \overline{\mu_n}1\|_\psi = \|u_n - \mu_n1\|_\psi\to 0\). Bounded sequences \(y_n\) with
\(y_n\xi_\psi\to 0\) tend to \(0\) strongly, so \(u_n - \mu_n1\to 0\) \(*\)-strongly.

**Exercise 12.5.** Suppose \(M = N\rtimes D\) is a full factor whose predual is separable, with \(N\) semifinite and
\(D\) a countable discrete abelian group. Show that \(D\) permutes the minimal projections of the centre of \(N\)
transitively.

*Solution.* By the proof of Theorem 10.1, Case 1 is excluded by fullness, so the centre \(Z\) of \(N\) is atomic and
\(D\) acts ergodically on it. Let \(p\) be a minimal projection of \(Z\). The sum of the distinct projections
\(\alpha_d(p)\), \(d\in D\), is a nonzero projection of \(Z\) fixed by \(D\), hence equal to \(1\). Every minimal
projection \(p'\) of \(Z\) satisfies \(p' = p'\cdot 1 = \sum p'\alpha_d(p)\). The products \(p'\alpha_d(p)\) are
projections of \(Z\) below the minimal projections \(p'\) and \(\alpha_d(p)\), so each is \(0\) or equal to both, and
not all vanish. So \(p' = \alpha_d(p)\) for some \(d\).

## References



- [Connes 1973] A. Connes, Une classification des facteurs de type III, Ann. Sci. École Norm. Sup. (4) 6 (1973), no. 2,
  133–252. https://doi.org/10.24033/asens.1247 (open access: http://www.numdam.org/item?id=ASENS_1973_4_6_2_133_0). Free at https://alainconnes.org/wp-content/uploads/classificationfacteurs.pdf
- [Connes 1974] A. Connes, Almost periodic states and factors of type III₁, J. Functional Analysis 16 (1974),
  415–445. Free at https://doi.org/10.1016/0022-1236(74)90059-7
