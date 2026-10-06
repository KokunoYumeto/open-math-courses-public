# Haar averages and compact translation control

*Written by GPT-6.1 Sol (OpenAI), Ultra, September 2026. Author self-check in progress; not independently reviewed. New original text is public domain (CC0).*

## Introduction

For a locally compact group, a finite set of translations is replaced by a compact set. Almost invariance must hold uniformly over that set. Haar measure replaces counting, and convolution supplies the continuity needed to pass from finitely many estimates to a uniform one.

Read [Means, Følner sets, and regular representations](means-folner-sets-and-regular-representations.md) first. We use Haar measure, its uniqueness, regularity of Radon measures, norm continuity of translations on \(L^1\), Hahn–Banach separation, and weak-star compactness. We prove the smoothing and compact-control steps below.

Throughout \(G\) is a locally compact Hausdorff group with a fixed left Haar measure \(dt\). No countability or unimodularity assumption is made. Put
\[
L_sf(t)=f(s^{-1}t),\qquad R_sf(t)=f(ts),\qquad
(k*f)(t)=\int_G k(u)f(u^{-1}t)\,du.
\tag{0.1}
\]
Let \(\mathrm{LUC}(G)\), \(\mathrm{RUC}(G)\) denote the bounded continuous functions for which respectively \(L_sf\to f\), \(R_sf\to f\) in supremum norm as \(s\to e\). Their intersection is \(\mathrm{UC}(G)\).

## Proof dependencies and reading order

The four amenability lessons form a proof sequence at two scopes: countable discrete groups, then arbitrary locally compact Hausdorff groups. For the latter scope, a link to another lesson is not a requirement to read that entire lesson first. The following order specifies the results actually needed.

| Stage | Complete arguments to read | What they supply next |
| --- | --- | --- |
| 1. Discrete model | [Means, Følner sets, and regular representations](means-folner-sets-and-regular-representations.md), Sections 1–6 | Means, finite-set approximation, fixed points, the free-group obstruction, and the regular representation. These establish the countable discrete case; compact-uniform approximation for a general group is proved separately below. |
| 2. Haar means | [Section 0](#0-haar-integration-without-a-countable-base) and [Section 1](#1-smoothing-and-extending-a-mean) of this lesson | Locally completed Haar duality, translation continuity, and extension of a mean from uniformly continuous functions to Haar classes. |
| 3. Fixed points and approximation | [Sections 2–5](#2-fixed-points-and-two-sided-means) of this lesson | The fixed-point criterion, two-sided means, Reiter approximation, compact Følner sets, and the full/reduced norm criterion. This branch does not use closed-subgroup heredity. |
| 4. Closed subgroups | [Closed subgroups and continuous averaging](closed-subgroups-and-continuous-averaging.md), Lemmas 1.1–1.2 and Theorem 2.1 | A quotient partition, a normalized cutoff, and a positive unital averaging map. The theorem uses the Haar extension from Stage 2 and proves heredity without a countable base or a measurable section. |
| 5. Permanence | [Section 6](#6-permanence-with-topology) of this lesson | Closed-subgroup heredity from Stage 4, the fixed-point argument for normal extensions from Stage 3, and direct proofs for compact and abelian groups, quotients, increasing unions, and solvable groups. |
| 6. The radical criterion | [Almost-connected groups and the solvable radical](almost-connected-groups-and-the-solvable-radical.md), Sections 1–4 | Radical bookkeeping, discrete free lifting, explicit ping-pong, and the semisimple obstruction combine with Stage 5 and the discrete free-group obstruction to prove the criterion. Section 5 gives examples at the same stated scope. |

In particular the closed-subgroup proof depends on Theorem 1.2 here, while Proposition 6.1 here uses that closed-subgroup proof. These dependencies occur in this order; neither proof assumes its own conclusion. The compact-control and representation proofs in Sections 3–5 can be read before the subgroup lesson.

The maps used at the two interfaces matter. Smoothing converts a mean on uniformly continuous functions into a mean on locally completed Haar classes. Continuous subgroup averaging then maps bounded continuous functions on the subgroup to bounded continuous functions on the ambient group; composing with the ambient mean and applying Theorem 1.2 on the subgroup finishes heredity. Restricting arbitrary ambient Haar classes to the subgroup would not define this map: a closed subgroup can have ambient Haar measure zero. The horizontal subgroup of the plane in the subgroup lesson illustrates this obstruction.

The foundational inputs are explicit: Haar existence and uniqueness, Radon approximation and Riesz representation, Hahn–Banach and weak-star compactness, continuous compactly supported partitions and bumps, Stone–Weierstrass, and the integrated representation and group C-star framework. Section 0 supplies the local Haar convention and translation estimates needed when there is no countable base. Its free-lifting and ping-pong arguments are proved there. Reading the application does not supply a proof of those external structure theorems.

All four lessons include complete solutions: five in the discrete lesson, five here, six in the subgroup lesson, and eight in the radical lesson. Their hypotheses remain attached to each argument. The locally compact statements assume neither second countability nor unimodularity; the radical criterion also requires almost-connectedness. This reading order concerns these four group-amenability lessons. The measured-relation lesson has its own additional dependencies.

## 0. Haar integration without a countable base

For a group that is not sigma-compact, the usual Haar \(L^\infty\) means the locally completed Haar space, equivalently the dual of \(L^1(G)\). This convention permits bounded measurable classes on each sigma-compact open coset; it does not require a single global Borel representative for an arbitrary such class. Continuous bounded functions have their canonical representatives. Every mean below is a positive unital functional on this \(L^\infty\) space.

**Lemma 0.1.** Every locally compact group has a sigma-compact open subgroup \(K\). Haar \(L^1(G)\) is the \(\ell^1\) sum of the Haar \(L^1\) spaces on the disjoint left cosets of \(K\); its dual is their \(\ell^\infty\) product. Each integrable function is supported, up to locally Haar-null sets, on a countable union of these cosets. Continuous compactly supported functions are dense in \(L^p(G)\), \(1\leq p<\infty\), and translations are norm continuous there.

*Proof.* Take a compact neighborhood \(V\) of the identity. The subgroup generated by \(V\cup V^{-1}\) is a countable union of compact sets and contains an identity neighborhood, hence is open. Its cosets are disjoint clopen sigma-compact sets. A compact subset of \(G\) meets only finitely many cosets, since those open cosets cover it. Haar integration of a compactly supported function is therefore a finite sum over the cosets. Radon approximation on a sigma-compact coset gives density of continuous compactly supported functions there. Completing their finite coset sums in the integral norm proves the stated \(\ell^1\) description. An \(\ell^1\) family has at most countably many nonzero entries, by considering entries of norm at least \(1/n\); its dual is the bounded product of the sigma-finite coset duals. The same approximation proves the \(L^p\) density assertion.

For a continuous compactly supported function, translations near the identity have support in one compact set. Joint continuity and compactness give uniform convergence on that set, and its Haar measure is finite. This proves norm continuity for these functions. Density and the bounded translation norms give it for all \(L^p\) functions. Right translations use their Haar modular factor, which is continuous at the identity. \(\square\)

The integrations below consequently require no global sigma-finiteness. Each \(L^1\) or \(L^2\) vector has sigma-compact support in this sense. Continuous scalar integrands on a compact product are measurable for the product sigma-field: finite sums of products of continuous functions approximate them uniformly by the Stone–Weierstrass theorem. Approximation by compactly supported kernels, followed by \(L^1\) bounds, gives the convolution and Fubini identities used here. In particular smoothing an arbitrary \(L^\infty\) class can be read through duality: \(S_hf(t)=\langle f,L_th\rangle\). This gives its continuous representative directly and avoids assuming joint Borel measurability for arbitrary representatives on a nonmetrizable group.

## 1. Smoothing and extending a mean

For a probability density \(h\in L^1(G)\), define the right smoothing operator
\[
(S_hf)(t)=\int_G h(v)f(tv)\,dv.
\tag{1.1}
\]
Left Haar measure gives
\[
R_sS_hf=S_{L_sh}f,\qquad
\|R_sS_hf-S_hf\|_\infty
\leq\|L_sh-h\|_1\|f\|_\infty.
\tag{1.2}
\]
Thus \(S_hf\in\mathrm{RUC}(G)\). Similarly,
\[
L_s(k*f)=(L_sk)*f
\tag{1.3}
\]
shows \(k*f\in\mathrm{LUC}(G)\). If \(f\) is already right uniformly continuous, then \(k*f\in\mathrm{UC}(G)\), since right translations commute with left convolution.

**Lemma 1.1.** A bounded positive left-translation invariant functional on \(L^1(G)\) is a nonnegative scalar multiple of \(k\mapsto\int k\).

*Proof.* Restrict it to continuous compactly supported functions. Its bound by a constant times the \(L^1\)-norm makes it a positive Radon measure dominated by that constant times Haar measure. Translation invariance and uniqueness of Haar measure make it a scalar multiple of Haar measure. Density of compactly supported continuous functions in \(L^1\) extends the identity. \(\square\)

**Theorem 1.2.** A left invariant mean on \(\mathrm{UC}(G)\) produces a left invariant mean \(M\) on \(L^\infty(G)\) with the stronger property
\[
M(k*f)=M(f)\int k,\qquad
k\in L^1(G),\ f\in L^\infty(G).
\tag{1.4}
\]

*Proof.* Let \(m\) be the given mean. For \(f\in\mathrm{RUC}(G)\), the functional \(k\mapsto m(k*f)\) on \(L^1\) is left invariant by (1.3). For positive \(f\) it is positive. Lemma 1.1, followed by decomposition into real and imaginary positive parts, gives a scalar \(\widetilde m(f)\) with
\[
m(k*f)=\widetilde m(f)\int k.
\tag{1.5}
\]
Fixing one probability density \(k\) shows that \(\widetilde m\) is a mean on \(\mathrm{RUC}(G)\).

It extends \(m\): for \(f\in\mathrm{UC}(G)\), a positive \(L^1\) approximate identity has \(k_i*f\to f\) uniformly, so (1.5) gives \(\widetilde m(f)=m(f)\).

It is left invariant. In fact, \(k*L_sf=k^s*f\), where the measure \(k^s(u)\,du\) is the pushforward of \(k(u)\,du\) under \(u\mapsto us\). It has the same integral as \(k\). Apply (1.5) to both sides. This formulation includes the right-translation Haar factor without assuming it is one.

Choose a probability density \(h\) and set
\[
M(f)=\widetilde m(S_hf).
\tag{1.6}
\]
It is positive and unital. Right smoothing commutes with left translations, so it is left invariant. The earlier map \(\widetilde m\) extends \(m\); the final smoothing in (1.6) need not preserve a mean that was only left invariant.

Finally, Fubini gives \(S_h(k*f)=k*S_hf\). The latter is in \(\mathrm{UC}(G)\). Equations (1.5)–(1.6) now give (1.4). \(\square\)

A locally compact group is **amenable** when it has a left invariant mean on \(L^\infty(G)\). Restriction and Theorem 1.2 show that the \(\mathrm{UC}(G)\) formulation is equivalent.

## 2. Fixed points and two-sided means

**Theorem 2.1.** Amenability is equivalent to the compact convex fixed-point property for affine actions of \(G\) that are continuous in each variable separately.

*Proof.* Suppose a mean exists and \(G\) acts separately continuously and affinely on a nonempty compact convex \(K\) in a Hausdorff locally convex space. Fix \(x\in K\). For every continuous real linear functional \(\ell\), prescribe
\[
\ell(\bar x)=M(s\mapsto\ell(sx)).
\tag{2.1}
\]
These prescriptions define a point of \(K\). Indeed, for finitely many functionals, the prescribed vector lies in the compact convex image of \(K\): otherwise a separating linear combination would put its mean outside the minimum and maximum of that combination on the orbit. Thus the corresponding closed subsets of \(K\) have the finite-intersection property. Compactness gives a point satisfying all prescriptions.

We also need the barycenter identity for every continuous affine function \(\psi\) on \(K\). The restriction of \(M\) to \(C_b(G)\) lies in the weak-star closure of finite convex combinations of point evaluations: separation by a real continuous bounded function would contradict its value lying between that function's infimum and supremum. Choose a net of these finite probabilities converging to that restriction, and form the corresponding convex averages of the orbit points \(sx\). A compactness subnet converges to \(\bar x\) as determined by (2.1). Affinity and continuity give \(\psi(\bar x)=M(s\mapsto\psi(sx))\). Apply this to \(\psi(y)=\ell(gy)\), for fixed \(g\). Left invariance yields \(\ell(g\bar x)=\ell(\bar x)\), and separation by the \(\ell\)'s makes \(\bar x\) fixed. Only continuity of each orbit map and each individual affine transformation was needed.

Conversely, act on the state space of \(\mathrm{UC}(G)\) by \((s\cdot m)(f)=m(L_{s^{-1}}f)\). The inverse makes this a left action. It is continuous in the weak-star topology because translations of each function are norm continuous. The fixed-point property gives an invariant mean there. Theorem 1.2 supplies a Haar mean. \(\square\)

This includes the source's compact convex sets in a Banach dual pair equipped with its weak topology, since the defining representation has continuous orbit maps and continuous linear transformations. The proof constructs the barycenter in the specified compact set; it does not identify an arbitrary bounded bilinear form with an operator on a potentially nonreflexive Banach space.

**Proposition 2.2.** An amenable group has a mean on \(L^\infty(G)\) invariant under both left and right translations.

*Proof.* Inversion converts a left mean into a right mean. For \(f\in\mathrm{UC}(G)\), form the iterated mean
\[
m_0(f)=m_L(g\mapsto m_R(v\mapsto f(gv))).
\tag{2.2}
\]
The outer function is bounded and continuous: its variation under \(g\mapsto sg\) is bounded by \(\|L_{s^{-1}}f-f\|_\infty\). Thus it is measurable. As in the discrete proof, outer left invariance and inner right invariance make \(m_0\) two-sided.

In Theorem 1.2, extend \(m_0\) first to \(\widetilde m\) on \(\mathrm{RUC}(G)\). This extension is also right invariant, since \(k*R_sf=R_s(k*f)\). For arbitrary positive \(f\in L^\infty(G)\), the functional
\[
h\longmapsto\widetilde m(S_hf)
\]
on \(L^1(G)\) is positive and left invariant, by (1.2) and right invariance of \(\widetilde m\). Lemma 1.1 makes it a scalar multiple of \(\int h\). By linear decomposition the same independence of the probability density \(h\) holds for every bounded \(f\).

Now \(S_h(R_sf)=S_{h^s}f\), where \(h^s\,dv\) is the right-translation pushforward of \(h\,dv\), again a probability density. The independence just proved shows that (1.6) is right invariant. Its left invariance was already proved. \(\square\)

## 3. Normal densities and uniform compact control

Let \(\mathcal P(G)=\{p\in L^1(G):p\geq0,\int p=1\}\).

The weak convolution condition is the existence of a net \(p_i\in\mathcal P(G)\) such that
\[
\int f(k*p_i-p_i)\,dt\longrightarrow0
\quad\bigl(f\in L^\infty(G),\ k\in\mathcal P(G)\bigr).
\tag{3.0}
\]
The strong convolution condition replaces these scalar limits by \(\|k*p_i-p_i\|_1\to0\) for every fixed \(k\). Both are equivalent to the following three formulations of amenability.

**Theorem 3.1 (Reiter approximation).** Amenability is equivalent to each of the following conditions:

1. For every finite family \(k_1,\ldots,k_N\in\mathcal P(G)\) and \(\varepsilon>0\), there is \(p\in\mathcal P(G)\) with
   \[
   \sum_i\|k_i*p-p\|_1<\varepsilon.
   \tag{3.1}
   \]
2. For every compact \(C\subset G\) and \(\varepsilon>0\), there is \(p\in\mathcal P(G)\) with
   \[
   \sup_{s\in C}\|L_sp-p\|_1<\varepsilon.
   \tag{3.2}
   \]
3. In condition 2 one may require \(p\) to be continuous and compactly supported.

*Proof.* Construct \(M\) with (1.4). Normal states, identified with \(\mathcal P(G)\), are weak-star dense in the state space of \(L^\infty(G)\): separation by a real bounded function would contradict the fact that its supremum over normal states is its essential supremum.

For \(k\in\mathcal P(G)\), the adjoint of \(p\mapsto k*p\) sends \(f\) to
\[
(T_kf)(t)=\int k(s)f(st)\,ds.
\]
This equals \(k^\#*f\), where \(k^\#\,ds\) is the pushforward of \(k\,ds\) under inversion. This is a probability density, and (1.4) gives \(M(T_kf)=M(f)\). Approximating \(M\) by normal states therefore places zero in the weak closure of the convex set
\[
\{(k_i*p-p)_i:p\in\mathcal P(G)\}
\]
in a finite direct sum of \(L^1\) spaces. Hahn–Banach makes its norm closure contain zero, proving (3.1).

If (3.0) is assumed instead, its scalar limits place zero in the weak closure of exactly the same convex set, so the same separation proves (3.1). Conversely, direct the finite-family choices in (3.1) by all finite families and decreasing tolerances. They give the strong convolution net, which gives (3.0). This verifies both net formulations, including simultaneous estimates for any finite family.

To obtain (3.2), fix \(h\in\mathcal P(G)\). The set \(\{L_sh:s\in C\}\) is norm compact in \(L^1\). Choose finitely many \(s_i\) such that every \(L_sh\) is within \(\varepsilon/3\) of some \(L_{s_i}h\). Use (3.1) for \(h\) and these translates, obtaining \(p\) with all their convolution errors below \(\varepsilon/3\). Then \(g=h*p\) is a probability density and
\[
\begin{aligned}
\|L_sg-g\|_1
&\leq\|(L_sh-L_{s_i}h)*p\|_1\\
&\quad+\|(L_{s_i}h)*p-p\|_1+\|p-h*p\|_1
<\varepsilon.
\end{aligned}
\tag{3.3}
\]

Positive compactly supported continuous probability densities are dense in \(\mathcal P(G)\), by Radon regularity and approximation in \(L^1\), followed by normalization. Replacing \(g\) by such a density changes every translation error by at most twice the \(L^1\) approximation error. Thus condition 3 follows.

Conversely, probability densities satisfying (3.2), directed by compact sets and decreasing error, define normal states. A weak-star cluster point is invariant under each fixed translation, hence is a mean. \(\square\)

The compactness used in (3.3) belongs to the translated smoothing density \(h\). Pointwise estimates on an arbitrary family of densities alone would not give the uniform conclusion.

## 4. Compact Følner sets

Write \(|A|\) for left Haar measure.

**Theorem 4.1.** Amenability is equivalent to the following condition: for every compact \(C\subset G\) and \(\varepsilon>0\), there is a compact set \(F\) with \(0<|F|<\infty\) and
\[
|sF\triangle F|<\varepsilon|F|\quad(s\in C).
\tag{4.1}
\]

*Proof.* The reverse implication follows by using \(\mathbf1_F/|F|\) in (3.2). For the forward implication, enlarge \(C\) to a compact set \(D\) of positive Haar measure. Put \(Q=D\cup D^{-1}D\). For every \(s\in D\),
\[
D\subset sQ\cap Q.
\tag{4.2}
\]
Consequently, any Borel \(B\subset Q\) with \(|Q\setminus B|<|D|/2\) satisfies \(|sB\cap B|>0\) for all \(s\in D\), and hence \(D\subset BB^{-1}\).

Choose a continuous compactly supported probability density \(p\) with translation error less than \(\delta\) on \(Q\), where \(2\delta|Q|/\varepsilon<|D|/2\). For \(a>0\), set \(F_a=\{t:p(t)\geq a\}\). These sets are compact. The layer identity gives
\[
\int_0^\infty|F_a|\,da=1,\qquad
\int_0^\infty|sF_a\triangle F_a|\,da<\delta\quad(s\in Q).
\tag{4.3}
\]
For levels with positive measure, let
\[
B_a=\{s\in Q:|sF_a\triangle F_a|<(\varepsilon/2)|F_a|\}.
\]
At levels with zero measure put \(B_a=Q\); their contribution to the following weighted integral is zero.
Fubini and (4.3) imply
\[
\int_0^\infty |Q\setminus B_a|\,|F_a|\,da
\leq\frac{2}{\varepsilon}\int_Q\int_0^\infty
|sF_a\triangle F_a|\,da\,ds
<\frac{2\delta|Q|}{\varepsilon}<\frac{|D|}{2}.
\tag{4.4}
\]
Thus some level has \(0<|F_a|<\infty\) and \(|Q\setminus B_a|<|D|/2\). The product measurability in this calculation also holds without metrizability. For \(s\in Q\), all the relevant \(t\)'s lie in the fixed compact set \(\operatorname{supp}p\cup Q\operatorname{supp}p\). On this compact product the continuous scalar functions \(p(t)\) and \(p(s^{-1}t)\) are product measurable by the approximation in Lemma 0.1. Comparing them with the real parameter \(a\) gives product measurable indicators. The restricted Haar measures are finite, so Fubini applies. Integrating in \(t\) also proves measurability of \((s,a)\mapsto|sF_a\triangle F_a|\) and of the sets \(B_a\).

By (4.2), every \(s\in C\subset D\) can be written \(s=uv^{-1}\) with \(u,v\in B_a\). Left Haar invariance gives
\[
|uv^{-1}F_a\triangle F_a|
\leq|v^{-1}F_a\triangle F_a|+|uF_a\triangle F_a|
=|vF_a\triangle F_a|+|uF_a\triangle F_a|
<\varepsilon|F_a|.
\]
This is (4.1). \(\square\)

The extra overlap argument is what turns almost invariance for most translations in \(Q\) into invariance estimates for every translation in \(C\).

## 5. Regular vectors and the group norms

Let \(\lambda_s\xi(t)=\xi(s^{-1}t)\) on \(L^2(G)\).

**Theorem 5.1.** Amenability is equivalent to the existence of a net of unit vectors \(\xi_i\) with
\[
\sup_{s\in C}\|\lambda_s\xi_i-\xi_i\|_2\longrightarrow0
\quad\text{for every compact }C.
\tag{5.1}
\]
It is also equivalent to faithfulness of \(C^*(G)\to C_r^*(G)\).

*Proof.* For Reiter densities, \(\xi=p^{1/2}\) is a unit vector and
\[
\|\lambda_s\xi-\xi\|_2^2\leq\|L_sp-p\|_1.
\]
Conversely, \(\||\lambda_s\xi|^2-|\xi|^2\|_1
\leq2\|\lambda_s\xi-\xi\|_2\), as in the discrete proof. These estimates are uniform on the same compact set.

For a strongly continuous unitary representation \(\pi\) on \(K\), the unitary \(WF(t)=\pi(t)^{-1}F(t)\) on \(L^2(G;K)\) conjugates \(\lambda_s\otimes\pi(s)\) to \(\lambda_s\otimes1\). Compress with \(J_iv=\xi_i\otimes v\). For \(f\in L^1(G)\), the compression of the integrated representation differs from \(\pi(f)\) by at most
\[
\int_G |f(s)|\,|1-\langle\lambda_s\xi_i,\xi_i\rangle|\,ds.
\tag{5.2}
\]
Compact-uniform convergence and an \(L^1\) tail estimate make this tend to zero. Thus \(\|\pi(f)\|\leq\|\lambda(f)\|\) for every \(\pi\), proving equality of the full and reduced norms.

Conversely, faithfulness makes the trivial representation a state \(\epsilon\) on \(C_r^*(G)\). Extend it, through unitization if necessary, to a state \(\psi\) on \(B(L^2(G))\) by Hahn–Banach. The norm-one unital extension is positive by the argument in the discrete group-norm theorem.

Take a positive contractive approximate identity \(e_j\) of \(C_r^*(G)\). We have \(\psi(e_j)=\epsilon(e_j)\to1\). For every \(s\), \(\lambda_se_j\in C_r^*(G)\) and \(\epsilon(\lambda_se_j)=\epsilon(e_j)\). Moreover, Cauchy–Schwarz gives
\[
|\psi(\lambda_s(1-e_j))|^2
\leq\psi((1-e_j)^2)\leq1-\psi(e_j)\longrightarrow0.
\]
Hence \(\psi(\lambda_s)=1\). The same zero-variance argument as in the discrete theorem yields
\(\psi(\lambda_sB\lambda_s^*)=\psi(B)\) for every \(B\).

Restrict \(\psi\) to the multiplication algebra \(L^\infty(G)\). Since \(\lambda_sM_f\lambda_s^*=M_{L_sf}\), the restriction is a left invariant mean. \(\square\)

**Corollary 5.2 (the unit-ball coefficient formulation).** Amenability is also equivalent to a net \(\xi_i\) in the unit ball of \(L^2(G)\) such that
\[
c_{\xi_i}(s)=\int_G\xi_i(t)\overline{\xi_i(s^{-1}t)}\,dt
\longrightarrow1
\quad\text{uniformly on each compact subset of }G.
\tag{5.3}
\]
With \(\xi^\vee(t)=\overline{\xi(t^{-1})}\), this integral is the coefficient customarily denoted \(\xi*\xi^\vee(s)\). It is well defined by Cauchy–Schwarz even when inversion does not preserve the Haar \(L^2\)-norm.

*Proof.* Almost invariant unit vectors give (5.3), since \(|c_\xi(s)-1|\leq\|\lambda_s\xi-\xi\|_2\). Conversely (5.3) at the identity gives \(r_i=\|\xi_i\|_2\to1\). Eventually \(r_i>0\); normalize \(\eta_i=\xi_i/r_i\). The normalized coefficients \(c_{\eta_i}=c_{\xi_i}/r_i^2\) still converge uniformly to one on compact sets. Now
\[
\|\lambda_s\eta_i-\eta_i\|_2^2
=2-2\operatorname{Re}c_{\eta_i}(s),
\]
which yields (5.1). Theorem 5.1 finishes the equivalence. \(\square\)

The tensor unitary used in Theorem 5.1 also requires no separable representation space: first apply it to finite sums of scalar compactly supported functions times Hilbert-space vectors. On compact supports, the strongly continuous vector orbits have separable metric range and are Bochner measurable. The isometric formula and density extend it to the full tensor Hilbert space. All convergence is by nets and compact sets.

## 6. Permanence with topology

**Proposition 6.1.** Compact groups and abelian locally compact groups are amenable. Closed subgroups, quotients by closed normal subgroups, extensions by closed normal subgroups, and increasing unions of closed amenable subgroups preserve amenability.

*Proof.* A compact group has normalized Haar measure. For an abelian group, evaluate bounded continuous functions on finite rectangular averages in any finitely generated subgroup. That subgroup is a quotient of \(\mathbb Z^d\), so the rectangular probability errors for any prescribed finite family of translations tend to zero. Direct these averages by finite subsets of \(G\); a cluster point on \(\mathrm{UC}(G)\) is invariant.

The full closed-subgroup assertion is proved in [Closed subgroups and continuous averaging](closed-subgroups-and-continuous-averaging.md), Theorem 2.1. A continuous positive unital averaging map \(T:C_b(H)\to C_b(G)\) intertwines each left \(H\)-translation. Composing it with the ambient mean and applying Theorem 1.2 makes \(H\) amenable. Its construction works without a Borel cross-section or a countable base; arbitrary Haar-null classes on \(H\) are never pulled back to \(G\).

For a quotient by a closed normal subgroup, pull functions in its \(\mathrm{UC}\) algebra back to \(G\) and restrict a mean.

For an extension with amenable closed normal subgroup \(H\) and amenable quotient \(G/H\), use Theorem 2.1. In any compact convex \(G\)-space, the \(H\)-fixed set is nonempty, compact, convex, and \(G\)-invariant. The quotient acts continuously on it and has a fixed point. Thus \(G\) has the fixed-point property.

Finally, for an increasing union of closed amenable subgroups, restrict a function in \(\mathrm{UC}(G)\) to each subgroup and apply its mean. A weak-star cluster point of these means is invariant under every element of the union, since that element belongs to all sufficiently late subgroups. \(\square\)

In particular, locally compact solvable groups are amenable: use the closures in the finite derived series. Continuity of the commutator puts the commutators of each closure in the next closure, so the successive Hausdorff quotients are abelian. Apply the extension result inductively.

For example, the discrete group of permutations of \(\mathbb N\) moving only finitely many points is the increasing union of its finite symmetric subgroups, so is amenable. In contrast, every discrete free group \(F_n\), \(n\geq2\), contains the closed subgroup generated by its first two free generators, isomorphic to \(F_2\). The reduced-word obstruction in the discrete means lesson and the closed-subgroup theorem therefore prove its nonamenability. The subgroup topology matters, as Exercise 4.4 of the continuous averaging lesson shows.

## 7. Exercises with solutions

Level 1 asks for a computation or a direct application. Level 2 asks for a proof using the lesson’s framework. Level 3 combines results or examines a hypothesis whose failure changes the conclusion.

**Exercise 7.1 (where compactness enters).** *Level 2.* Identify the two uses of compactness in the proofs of Reiter and Følner approximation.

*Solution.* In (3.3), the continuous \(L^1\)-orbit of a fixed density over a compact set has a finite norm cover. In the Følner argument, \(Q\) has finite Haar measure, permitting the averaged bad-translation estimate (4.4); positive compact \(D\) also supplies the overlap bound (4.2).

**Exercise 7.2 (a nonunimodular example).** *Level 2.* On the affine group with multiplication
\((a,b)(a',b')=(aa',b+ab')\), \(a,a'>0\), verify the left Haar density \(da\,db/a^2\) and compute the effect of right translation by \((a_0,b_0)\) on set measure.

*Solution.* Left translation by \((a_0,b_0)\) has Jacobian \(a_0^2\), while the new squared first coordinate contributes the same factor in the denominator. The density is left invariant. Right translation sends \((a,b)\) to \((aa_0,b+ab_0)\), with Jacobian \(a_0\); its denominator contributes \(a_0^2\). Thus \(|E(a_0,b_0)|=a_0^{-1}|E|\). The group is solvable and hence amenable, although this right-translation factor is generally not one.

**Exercise 7.3 (the square-root estimate).** *Level 1.* Prove \(\|\sqrt p-\sqrt q\|_2^2\leq\|p-q\|_1\) for nonnegative integrable functions.

*Solution.* Pointwise,
\((\sqrt p-\sqrt q)^2\leq|\sqrt p-\sqrt q|(\sqrt p+\sqrt q)=|p-q|\).
Integration gives the inequality. Taking \(q=L_sp\) proves the first estimate in Theorem 5.1.

**Exercise 7.4 (an overlap factorization).** *Level 1.* Show directly that \(|sB\cap B|>0\) implies \(s\in BB^{-1}\), and explain why this implication alone does not require \(B\) to be compact.

*Solution.* Choose any \(z\in sB\cap B\). Write \(z=sw\) with \(w\in B\); since \(z\in B\), \(s=zw^{-1}\in BB^{-1}\). Positive measure ensures nonemptiness. Compactness is used elsewhere to construct the finite-measure test set and the compact Følner level, not in this algebraic implication.

**Exercise 7.5 (the nonunital step).** *Level 3.* Why does \(\epsilon(\lambda_se_j)=\epsilon(e_j)\) suffice to recover \(\psi(\lambda_s)=1\), even if \(\lambda_s\notin C_r^*(G)\)?

*Solution.* The extension \(\psi\) is defined on the larger unital algebra \(B(L^2(G))\). The product \(\lambda_se_j\) lies in the reduced algebra, so its value is known. The estimate displayed in Theorem 5.1 makes \(\psi(\lambda_s-\lambda_se_j)\to0\). Therefore \(\psi(\lambda_s)=\lim_j\epsilon(e_j)=1\), without asserting that the multiplier itself belongs to the reduced algebra.

## References

[Takesaki] Masamichi Takesaki, *Theory of Operator Algebras III*, Encyclopaedia of Mathematical Sciences 127, Springer, 2003. [Publisher record](https://doi.org/10.1007/978-3-662-10453-8).
