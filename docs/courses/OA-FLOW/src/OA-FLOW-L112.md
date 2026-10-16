
<a id="oa-flow.l112.0"></a><a id="l112-opening-context"></a>

# Cocycle matrix actions and the representation continuity test

A norm-continuous action on a C\*-algebra need not become a continuous normal action in every representation. We prove that quasi-equivalence of the translated representations gives a continuous normal action on every separable represented Hilbert space. Haar averages turn measurable scalar orbits into norm-continuous predual orbits. We then prove a concrete obstruction in the universal representation of \(C_0(\mathbb R)\). Shrinking bumps converge strongly to nonzero atomic projections, but translating the limiting projection makes a normal vector functional jump.

The final construction puts a unitary cocycle into a \(2\times2\) matrix action. Its two fixed diagonal corners carry the original and perturbed actions; the general equivalent-fixed-corner theorem then transfers their Connes spectra. Continuity of this action is proved directly in the concrete predual.

*The concluding Connes-spectrum application uses the exact earlier canonical GCC proof. Original exposition, new proofs and illustration are CC0-1.0 to the extent of rights held.*

<a id="oa-flow.l112.inputs"></a>

<a id="cm-inputs"></a>
## Exact earlier setting and conventions

The C\*-representation statements use arbitrary nonunital C\*-algebras, arbitrary Hilbert spaces and arbitrary LCH groups. Only the cocycle/Connes part imposes the original LCA hypothesis. Representations are nondegenerate where stipulated. Von Neumann automorphisms are normal, meaning ultraweakly continuous. Strong convergence is vectorwise convergence; every use of strong-to-ultraweak convergence below has an explicit uniform operator bound.

The exact earlier proofs are [GNS5.1](OA-FLOW-GNS.md#gns-theorem-5-1), [GNS7.1](OA-FLOW-GNS.md#gns-lemma-7-1), [GNS7.3](OA-FLOW-GNS.md#gns-theorem-7-3), the concrete predual [CP4–6](OA-FLOW-CP.md#oa-flow.cp.4), bounded bicommutant density [BD4–5](OA-FLOW-BD.md#oa-flow.bd.4), and finite normal tensor transport [NCF1](OA-FLOW-NCF.md#ncf-1). [PC1](OA-FLOW-PC.md#oa-flow.projection.pc1) supplies arbitrary projection joins; [CF6–9](OA-FLOW-CF.md#oa-flow.cf.6) supplies the C\*, Hilbert norm and forced-unitization facts. Complete integration and action-continuity alternatives in AT and the free-source GNS development remain available. No abstract bidual W* construction is used.

The general spectral framework has negative labels: an eigenphase \(e^{-it\lambda}\) has label \(\lambda\), by [SS3](OA-FLOW-SS.md#ss-3). Equations M1–M23 use this convention; M21 identifies the concrete summand \(zP\).

<a id="oa-flow.l112.predual"></a>

<a id="cm-predual"></a>
## A full predual continuity estimate

Let \(Q\subseteq B(\mathcal H)\) be a concrete von Neumann algebra, and let \(V_t\) be a strongly continuous unitary family normalizing \(Q\): \(V_tQV_t^*=Q\) for every \(t\). There is no group-law requirement for the following estimate; the choice \(Q=B(\mathcal H)\) is automatic. Its adjoints are strongly continuous, since

<a id="equation-cm1"></a>

\[
 \|V_t^*\xi-V_s^*\xi\|=\|\xi-V_tV_s^*\xi\|\longrightarrow0.
 \tag{CM1}
\]
Conjugation is normal: in CP6's vector-series tests, evaluating \(VXV^*\) replaces the two square-summable vector sequences by their unitary images. With \(\omega_{\xi,\eta}(X)=\langle X\xi,\eta\rangle\), the two-vector difference gives

<a id="equation-cm8"></a>

\[
 \|\omega_{\xi,\eta}\circ\operatorname{Ad}(V_t)
       -\omega_{\xi,\eta}\circ\operatorname{Ad}(V_s)\|
 \leq \|V_t^*\xi-V_s^*\xi\|\,\|\eta\|
       +\|\xi\|\,\|V_t^*\eta-V_s^*\eta\|.
 \tag{CM8}
\]
Indeed split \(\langle XV_t^*\xi,V_t^*\eta\rangle-\langle XV_s^*\xi,V_s^*\eta\rangle\) into the first-vector and second-vector differences, and take the supremum over \(\|X\|\leq1\). CP6 represents every normal functional by a series whose tail norm is bounded by \(\sum_{n>N}\|\xi_n\|\,\|\eta_n\|\to0\). Unitary conjugation preserves functional norms, so truncate that series, use (CM8) on its finite part, and bound the two remaining tails uniformly. This proves the full predual norm continuity in (M6), on arbitrary Hilbert spaces.

This proves point-ultraweak continuity of an inner action implemented by a strongly continuous unitary representation, since \(|\omega(V_tXV_t^*-V_sXV_s^*)|\) is bounded by the proved predual norm difference times \(\|X\|\). It does not assert operator-norm continuity of the implementing unitaries.

<a id="oa-flow.l112.systems"></a>

<a id="cm-systems"></a>
## Norm-continuous C-star covariant systems

A **C\*-covariant system** is a triple \((A,G,\alpha)\) consisting of a C\*-algebra \(A\), a locally compact group \(G\), and a homomorphism

<a id="equation-m12"></a>

$$\alpha:G\longrightarrow\operatorname{Aut}(A) \tag{M12}$$

such that every orbit is norm continuous:

<a id="equation-m13"></a>

$$\lim_{s\to t}\|\alpha_s(a)-\alpha_t(a)\|=0,
\qquad a\in A,\quad t\in G. \tag{M13}$$

Continuity at the identity suffices. Indeed

<a id="equation-m14"></a>

$$\|\alpha_s(a)-\alpha_t(a)\|
=\|\alpha_t(\alpha_{t^{-1}s}(a)-a)\|
=\|\alpha_{t^{-1}s}(a)-a\|. \tag{M14}$$

No commutativity of \(G\) is needed for this definition.

The equality in (M14) uses isometry, including nonunital algebras. CF9 constructs the forced unitization \(A^\dagger=A\oplus\mathbb C1_{\mathrm{new}}\) with its isometric inclusion of \(A\). An automorphism extends by \(\alpha^\dagger(a+\lambda1_{\mathrm{new}})=\alpha(a)+\lambda1_{\mathrm{new}}\); its multiplication and involution formulas immediately make this a unital star homomorphism with the similarly extended inverse. CF6's unital contractivity applied in both directions gives isometry on \(A^\dagger\), hence on \(A\). Likewise an algebraic star representation into nonzero \(B(\mathcal H)\) extends by \(a+\lambda1_{\mathrm{new}}\mapsto\pi(a)+\lambda I\), so CF6 proves its contractivity; the zero Hilbert space case is immediate. No abelian group hypothesis or pre-existing continuity of the algebraic homomorphism is used.

<a id="oa-flow.l112.representations"></a>

<a id="cm-representations"></a>
## A representation must carry a continuous von Neumann action

Let \(\pi:A\to B(\mathcal H)\) be a nondegenerate representation and put

<a id="equation-m15"></a>

$$P=\pi(A)''. \tag{M15}$$

The representation is an **\(\alpha\)-representation** when there is a point-ultraweakly continuous action

<a id="equation-m16"></a>

$$\widetilde\alpha:G\longrightarrow\operatorname{Aut}(P) \tag{M16}$$

satisfying

<a id="equation-m17"></a>

$$\widetilde\alpha_t(\pi(a))
=\pi(\alpha_t(a)),
\qquad a\in A,\quad t\in G. \tag{M17}$$

Such an action is unique if it exists: \(\pi(A)\) is ultraweakly dense in \(P\), and every \(\widetilde\alpha_t\) is normal. In particular, (M17) forces \(\ker\pi\) to be \(\alpha\)-invariant. Kernel invariance alone does not supply the continuity in (M16).

If a strongly continuous unitary representation \(U:G\to\mathcal U(\mathcal H)\) implements the covariance,

<a id="equation-m18"></a>

$$U_t\pi(a)U_t^*=\pi(\alpha_t(a)), \tag{M18}$$

then \(\widetilde\alpha_t=\operatorname{Ad}(U_t)|_P\) supplies (M16). The earlier predual-norm estimate, also used in (M6), proves its point-ultraweak continuity.

Here is the exact density and topology argument. Nondegeneracy puts the essential support at \(1_{\mathcal H}\). BD4 gives, for each \(x\in P\), a uniformly bounded strong-star net from \(\pi(A)\) converging to \(x\), and BD5/CP4 turns it into an ultraweakly convergent net. Thus two normal extensions agreeing on \(\pi(A)\) agree on all of \(P\). Applying an extension and its inverse to \(\pi(a)=0\) proves invariance of the kernel.

For (M18), unitary conjugation carries \(\pi(A)\) onto itself and hence carries its bicommutant onto itself: conjugating a commutation equation gives the corresponding commutation equation. The earlier full predual estimate supplies its normality and continuity on all of \(P\), not only on the C\*-generators.

<a id="oa-flow.l112.qi1"></a><a id="cm-quasi-equivalence"></a>
## Quasi-equivalence gives measurable scalar orbits

For representations \(\pi_1,\pi_2\) of the same C*-algebra, **quasi-equivalence** means that there is a normal star isomorphism, with normal inverse, from \(\pi_1(A)''\) onto \(\pi_2(A)''\) taking \(\pi_1(a)\) to \(\pi_2(a)\) for every \(a\). This specifies the generator correspondence, not just an abstract isomorphism between the two algebras.

**Lemma QI1.** Suppose \(\pi\) is nondegenerate on a nonzero separable Hilbert space \(\mathcal H\), and \(\pi\circ\alpha_s\) is quasi-equivalent to \(\pi\) for every \(s\in G\). There is a unique algebraic action \(\beta\) by normal automorphisms of \(P=\pi(A)''\) such that
\[
 \beta_s(\pi(a))=\pi(\alpha_s(a)).
 \tag{QI1}
\]
For every \(x\in P\) and \(\omega\in P_*\), the function \(s\mapsto\omega(\beta_s(x))\) is Borel measurable. No separability of \(A\), second countability of \(G\), or commutativity of \(G\) is needed.

**Proof.** Since \(\alpha_s(A)=A\), the two represented ranges have the same bicommutant. The normal isomorphism in the definition therefore gives \(\beta_s:P\to P\). Its uniqueness follows from the bounded density argument preceding (M18). On \(\pi(A)\), the maps \(\beta_s\beta_t\) and \(\beta_{st}\) agree, and both are normal. Thus they agree on \(P\). The same argument gives \(\beta_e=\mathrm{id}\) and \(\beta_s^{-1}=\beta_{s^{-1}}\).

Choose a countable dense sequence \((\xi_j)\) in \(\mathcal H\). For any \(x\in P\), [BD4](OA-FLOW-BD.md#oa-flow.bd.4) supplies \(a_n\in A\) such that \(\|\pi(a_n)\|\leq\|x\|\) and
\[
 \|(\pi(a_n)-x)\xi_j\|+
 \|(\pi(a_n)^*-x^*)\xi_j\|<1/n
 \quad(1\leq j\leq n).
 \tag{QI2}
\]
For \(x=0\), take \(a_n=0\). For other \(x\), rescale the contraction approximation. The uniform bound and approximation of each vector by some \(\xi_j\) prove strong-star convergence \(\pi(a_n)\to x\). [BD5](OA-FLOW-BD.md#oa-flow.bd.5) makes this ultraweak convergence. Normality of each fixed \(\beta_s\) gives
\[
 \omega(\beta_s(x))
   =\lim_{n\to\infty}\omega(\pi(\alpha_s(a_n))).
 \tag{QI3}
\]
Every function on the right is continuous, because the original action is point-norm continuous and the representation and functional are bounded. A pointwise limit of a sequence of continuous complex functions is Borel measurable. Inversion is continuous on \(G\), so the same holds with \(s^{-1}\) in place of \(s\). This is where the bounded approximation must be a sequence rather than an arbitrary net. \(\square\)

We will also use two direct consequences of the same countability assumption. Choose a dense sequence of unit vectors \((\eta_j)\). Then
\[
 \varphi(x)=\sum_{j\geq1}2^{-j}\langle x\eta_j,\eta_j\rangle
 \tag{QI4}
\]
is a faithful normal state on \(P\). [CP6](OA-FLOW-CP.md#oa-flow.cp.6) proves normality of this summable vector series. If \(x\geq0\) has value zero, \(x^{1/2}\eta_j=0\) for every \(j\), and density gives \(x=0\).

Moreover \(P_*\) is norm separable. [CP4–6](OA-FLOW-CP.md#oa-flow.cp.4) represents every normal functional by a norm-convergent sum of vector coefficients. Truncate the sum, approximate its finitely many vectors by a fixed countable dense vector set, and approximate the finitely many scalar coefficients by rational complex numbers. The estimate
\[
 \|\omega_{\xi,\eta}-\omega_{\xi',\eta'}\|
 \leq\|\xi-\xi'\|\,\|\eta\|+\|\xi'\|\,\|\eta-\eta'\|
 \tag{QI5}
\]
makes these finite rational combinations a countable norm-dense set.

<a id="oa-flow.l112.qi2"></a><a id="cm-normal-smoothing"></a>
## Averaging gives normal functionals, including on increasing nets

Use left Haar measure \(dt\), and set \(T_s\omega=\omega\circ\beta_{s^{-1}}\). These are linear isometries of \(P_*\), with
\[
 T_sT_t=T_{st}.
 \tag{QI6}
\]
Indeed, composition on the right reverses the two inverse parameters. Define, initially for \(f\in C_c(G)\) and \(\omega\in P_*\),
\[
 \Omega_{f,\omega}(x)
   =\int_G f(t)\,\omega(\beta_{t^{-1}}(x))\,dt.
 \tag{QI7}
\]
QI1 gives scalar measurability, and \(|\omega(\beta_{t^{-1}}(x))|\leq\|\omega\|\|x\|\), so this is an absolutely convergent scalar integral and
\[
 \|\Omega_{f,\omega}\|\leq\|f\|_1\|\omega\|.
 \tag{QI8}
\]
We do not presume that \(t\mapsto T_t\omega\) is norm measurable or already continuous.

**Lemma QI2.** The functional \(\Omega_{f,\omega}\) belongs to \(P_*\). Furthermore
\[
 T_s\Omega_{f,\omega}=\Omega_{L_sf,\omega},
 \qquad L_sf(t)=f(s^{-1}t),
 \tag{QI9}
\]
and
\[
 \|T_s\Omega_{f,\omega}-\Omega_{f,\omega}\|
 \leq\|L_sf-f\|_1\|\omega\|\longrightarrow0
 \quad(s\to e).
 \tag{QI10}
\]

**Proof.** First take \(f\geq0\) and \(\omega\geq0\). The integral is positive. For a bounded increasing positive sequence \(x_n\uparrow x\), normality of each \(\beta_{t^{-1}}\) and \(\omega\), followed by scalar monotone convergence, gives
\(\Omega_{f,\omega}(x_n)\uparrow\Omega_{f,\omega}(x)\). Scalar monotone convergence is [SC4](OA-FLOW-SC.md#sc-04).

Here is the additional step for an arbitrary bounded increasing positive net \(x_i\uparrow x\). Normality of the faithful state \(\varphi\) from (QI4) gives \(\varphi(x_i)\uparrow\varphi(x)\). Choose indices \(i_n\), increasing in the directed set, with
\(\varphi(x-x_{i_n})<1/n\). This is possible by directedness and the scalar supremum. Let \(y=\sup_n x_{i_n}\). Bounded increasing positive operators have their strong supremum in \(P\); it lies below \(x\). Normality of \(\varphi\) and the displayed bounds give \(\varphi(x-y)=0\), so faithfulness makes \(y=x\). Applying the sequential conclusion yields
\[
 \sup_i\Omega_{f,\omega}(x_i)
 \geq\sup_n\Omega_{f,\omega}(x_{i_n})
 =\Omega_{f,\omega}(x).
\]
Positivity gives the opposite inequality. Thus the functional preserves all bounded increasing positive suprema. [NF1–4](OA-FLOW-NF.md#oa-flow.nf.4) proves that such a bounded positive functional is ultraweakly continuous. Hence it belongs to \(P_*\).

For general \(\omega\), polarize the square-summable vector series in CP4–6. The identity, with inner products linear in the first variable,
\[
 \langle x\xi,\eta\rangle
 =\frac14\sum_{k=0}^3 i^k
       \langle x(\xi+i^k\eta),\xi+i^k\eta\rangle
 \tag{QI11}
\]
expresses it as a linear combination of four positive normal vector-series functionals: each of the four squared-norm sums is finite. Decompose the real and imaginary parts of \(f\) into positive and negative parts, still in \(C_c(G)\). Linearity reduces (QI7) to the positive case.

Finally,
\[
 \begin{aligned}
 (T_s\Omega_{f,\omega})(x)
 &=\int_G f(t)\,
       \omega(\beta_{t^{-1}}\beta_{s^{-1}}(x))\,dt\\
 &=\int_G f(t)\,
       \omega(\beta_{(st)^{-1}}(x))\,dt
 =\Omega_{L_sf,\omega}(x).
 \end{aligned}
\]
The last substitution is \(r=st\), so left invariance introduces no modular factor. Inequality (QI8) gives (QI10), and the full left-translation continuity is proved in [L24 Lemma 3.1](OA-FLOW-L24.md#oa-flow.grp.translations). Thus every averaged functional has a norm-continuous orbit before continuity has been established for general normal functionals. \(\square\)

<a id="oa-flow.l112.qi3"></a><a id="cm-quasi-invariant-criterion"></a>
## The averages determine the entire predual

**Theorem QI3.** Let \((A,G,\alpha)\) be a point-norm continuous C*-covariant system with arbitrary LCH group \(G\). Let \(\pi\) be a nondegenerate representation on a separable Hilbert space. Then the following are equivalent:

1. For every \(s\in G\), the representations \(\pi\circ\alpha_s\) and \(\pi\) are quasi-equivalent.
2. There is a point-ultraweakly continuous action by normal automorphisms of \(P=\pi(A)''\) satisfying (M17).

The action is unique, and all its predual orbits are norm continuous. There is no separability assumption on \(A\), no countability assumption on \(G\), and no abelian hypothesis.

**Proof.** The zero Hilbert space gives only the zero represented algebra, where the assertions have their unique zero interpretation. Otherwise QI1 and QI2 apply to the algebraic action obtained from condition 1.

Let \(\mathcal E\) be the linear span of all \(\Omega_{f,\omega}\). We prove that its norm closure is \(P_*\). If the closure were proper, [CF1's complex Hahn–Banach theorem](OA-FLOW-CF.md#OA-FLOW.CF.1) would give a nonzero bounded functional on \(P_*\) vanishing there. [CP6](OA-FLOW-CP.md#oa-flow.cp.6) identifies that functional with evaluation at a nonzero \(x\in P\).

Choose a countable norm-dense family \((\omega_n)\) in the unit ball of \(P_*\), available from (QI5). For each \(n\), the bounded Borel function
\[
 h_n(t)=\omega_n(\beta_{t^{-1}}(x))
 \tag{QI12}
\]
has zero integral against every \(f\in C_c(G)\). [HR3](OA-FLOW-HR.md#hr-03) makes \(C_c(G)\) dense in \(L^1(G)\). Since \(h_n\) is bounded, approximation therefore gives
\(\int_E h_n\,dt=0\) for every measurable finite-measure set \(E\).

Fix one nonempty relatively compact open set \(V\subseteq G\). Haar measure is finite on its compact closure and positive on \(V\), by [HR6](OA-FLOW-HR.md#hr-06). Apply the preceding integral identity to the positive and negative level sets of the real and imaginary parts of \(h_n\) inside \(V\). It follows that \(h_n=0\) almost everywhere on \(V\). The union of these exceptional null sets over all \(n\) is still null. At some \(t\in V\) outside it, every \(\omega_n\) annihilates \(\beta_{t^{-1}}(x)\). Norm density and CP6 duality force \(\beta_{t^{-1}}(x)=0\), contradicting invertibility and \(x\ne0\). This proves the norm density of \(\mathcal E\). The argument used only one finite-measure open set, so it requires no sigma compactness or global countable exhaustion of \(G\).

Each element of \(\mathcal E\) has a norm-continuous orbit by QI2. For \(\omega\in P_*\) and \(\eta\in\mathcal E\), isometry gives
\[
 \|T_s\omega-\omega\|
 \leq2\|\omega-\eta\|+\|T_s\eta-\eta\|.
 \tag{QI13}
\]
First choose \(\eta\) close to \(\omega\), then let \(s\to e\). Continuity at other parameters follows from \(T_sT_t=T_{st}\) and isometry. Consequently
\[
 |\omega(\beta_s(x)-\beta_t(x))|
 \leq\|x\|\,
       \|T_{s^{-1}}\omega-T_{t^{-1}}\omega\|
 \longrightarrow0\quad(s\to t),
 \tag{QI14}
\]
which proves condition 2 on all of \(P\). Conversely, the normal automorphism \(\beta_s\) supplied by condition 2 is exactly the generator-preserving isomorphism in the definition of quasi-equivalence. Uniqueness was proved in QI1. \(\square\)

<figure style="margin-left:0;margin-right:0">
<div style="max-width:100%;overflow-x:auto">
<img src="../assets/quasi-invariant-extension/predual-smoothing.svg" alt="The proof passes from bounded sequential approximation to measurable scalar orbits, then to normal Haar averages with continuous norm orbits, and finally to all predual functionals by norm density. The increasing-net normality step and the single finite-measure open set are shown separately." style="min-width:700px;width:100%;max-width:960px" />
</div>
<figcaption>QI1–QI3 identify where countability enters: approximation and separating tests belong to the represented algebra, while the Haar argument needs only one relatively compact open set. The arrows describe proved implications, not a claim that an arbitrary pointwise limit preserves continuity. <a href="../assets/quasi-invariant-extension/predual-smoothing.svg">Open the full diagram</a>. <a href="../assets/quasi-invariant-extension/draw_figure.py">Reproduction source</a>.</figcaption>
</figure>

<a id="oa-flow.l112.qi4"></a><a id="cm-quasi-invariant-states"></a>
## Quasi-invariant states and the limits of the criterion

A representation is **quasi-invariant** for the action when it admits the continuous normal extension (M16)–(M17). On a separable represented Hilbert space, QI3 gives the equivalent test by quasi-equivalence of all translates. This is the same extension property called an \(\alpha\)-representation above. A bounded positive functional on \(A\) is called quasi-invariant when its cyclic GNS representation has that property.

If \(A\) is separable, every cyclic GNS space of a bounded positive functional \(\psi\) is separable, including when \(A\) has no identity. Indeed the GNS construction has the dense set of classes \([a]\), \(a\in A\), with
\[
 \|[a]-[b]\|^2
 =\psi((a-b)^*(a-b))
 \leq\|\psi\|\,\|a-b\|^2.
 \tag{QI15}
\]
The image of a countable norm-dense subset of \(A\) is therefore dense in its Hilbert completion. The earlier [GNS construction](OA-FLOW-GNS.md#gns-theorem-5-1) gives its nondegenerate representation. For the zero functional the space is zero. Thus QI3 applies to every such \(\psi\) without a unitality assumption.

Two checks distinguish sufficient countability from a necessary condition for each individual action.

**Constant action.** Let \(G=\mathbb R\) and \(\alpha_t=\mathrm{id}_A\). In every nondegenerate representation, including the universal one on a possibly nonseparable Hilbert space, \(\beta_t=\mathrm{id}_P\) is a normal continuous extension. Its scalar and predual orbits are constant. Therefore a universal representation is not forced to fail merely because the acting group is nondiscrete.

**Translation action.** For the action of \(\mathbb R\) on \(C_0(\mathbb R)\), the next proof constructs a projection \(p_0\) whose orbit under any possible normal extensions has the discontinuous normal scalar test \(\mathbf1_{\{0\}}(t)\). The universal representation contains the mutually orthogonal evaluation GNS vectors \(\xi_s\) for every \(s\in\mathbb R\); hence its Hilbert space is not separable. QI3 consequently makes no continuity assertion for that representation. The obstruction is a failure that can occur outside the theorem's countability hypothesis, not a claim that every such action fails.

<a id="oa-flow.l112.obstruction"></a>

<a id="cm-obstruction"></a>
## The obstruction inside the concrete universal representation

The universal representation does not automatically satisfy (M16). Let

<a id="equation-m19"></a>

$$A=C_0(\mathbb R),\qquad
(\alpha_t f)(s)=f(s-t). \tag{M19}$$

This is a C\*-covariant system. To include its elementary premises, \(C_0(\mathbb R)\), with pointwise operations, conjugation and the supremum norm, is a C\*-algebra. A uniform Cauchy sequence has a uniform limit; the usual local epsilon estimate proves continuity of that limit. Approximation by one sequence member makes the limit vanish at infinity. Thus it is complete, and \(\|f^*f\|_\infty=\|f\|_\infty^2\). A nonnegative member has its continuous square root in \(C_0\), so positivity is exactly pointwise nonnegativity.

Translation preserves the operations, norm and vanishing at infinity, with inverse translation by \(-t\). It also preserves \(C_c(\mathbb R)\). For \(f\in C_c\) and \(|t|\leq1\), both translated supports lie in one fixed compact interval. Uniform continuity there gives \(\|\alpha_t f-f\|_\infty\to0\). To prove that continuity uniformly, for each point \(r\) choose \(\delta_r>0\) such that \(|f(q)-f(r)|<\varepsilon/2\) when \(|q-r|<2\delta_r\). A finite subcover of the intervals \((r-\delta_r,r+\delta_r)\) covers the compact interval. If two points are closer than the minimum of its finitely many \(\delta_r\), select a covering interval for the first; both points are within \(2\delta_r\) of its centre. The triangle inequality gives variation less than \(\varepsilon\). Every \(f\in C_0\) is uniformly approximable by compactly supported \(f\chi_R\), where \(\chi_R=1\) on \([-R,R]\), decreases linearly to zero on each of \([R,2R]\) and \([-2R,-R]\), and is zero outside \([-2R,2R]\). Indeed \(\|f-f\chi_R\|_\infty\leq\sup_{|r|>R}|f(r)|\to0\). Translation is isometric, so approximation proves (M13) on all of \(C_0\).

Use GNS7.3's direct sum of the GNS representations of all states, denoted \(\pi\) on \(\mathcal H_u\), and put \(P=\pi(A)''\). The representation is faithful, isometric and nondegenerate. Evaluation at \(s\) is a state: it is positive, bounded by the supremum norm, and the compact bump below has value and norm one. Its GNS summand supplies a unit vector \(\xi_s\). GNS5.1 gives

<a id="equation-cm2"></a>

\[
 \pi(f)\xi_s=f(s)\xi_s\quad(f\in C_0(\mathbb R)).
 \tag{CM2}
\]
For example the squared norm of the difference is
\(\operatorname{ev}_s(|f|^2)-2|f(s)|^2+|f(s)|^2=0\).
No identification with \(A^{**}\) is asserted.

For \(n\geq1\) and \(s\in\mathbb R\) define

<a id="equation-cm3"></a>

\[
 f_{n,s}(r)=\max\{0,1-n|r-s|\},\qquad a_{n,s}=\pi(f_{n,s}).
 \tag{CM3}
\]
These positive contractions decrease with \(n\). They have a strong limit. To prove this directly, for \(m\geq n\) put \(d=a_{n,s}-a_{m,s}=\pi(f_{n,s}-f_{m,s})\). The scalar function \(h=f_{n,s}-f_{m,s}\) satisfies \(0\leq h\leq1\); the function \(\sqrt{h-h^2}\) is in \(C_0\). Therefore \(d-d^2\geq0\), and

<a id="equation-cm4"></a>

\[
 \|(a_{n,s}-a_{m,s})\eta\|^2
 \leq\langle(a_{n,s}-a_{m,s})\eta,\eta\rangle.
 \tag{CM4}
\]
The scalar forms \(\langle a_{n,s}\eta,\eta\rangle\) decrease to a finite nonnegative limit, so (CM4) makes the vector sequence Cauchy. Its vectorwise limit is a bounded linear operator \(p_s\), with \(\|p_s\|\leq1\). Positivity, self-adjointness and \(p_s\leq a_{n,s}\) pass to the limit by forms. Since \(P\) is a commutant and each \(a_{n,s}\) commutes with every member of \(\pi(A)'\), passing the commutation equation to the strong limit gives \(p_s\in P\).

For each \(f\in C_0\), continuity at \(s\) gives

<a id="equation-cm5"></a>

\[
 \|(f-f(s))f_{n,s}\|_\infty
 \leq \sup_{|r-s|\leq1/n}|f(r)-f(s)|\longrightarrow0.
 \tag{CM5}
\]
Isometry of \(\pi\) and the strong limit give
\(\pi(f)p_s=f(s)p_s\). Apply this first with \(f=f_{m,s}\); then let \(m\to\infty\) strongly to obtain \(p_s^2=p_s\). Equation (CM2) gives \(p_s\xi_s=\xi_s\), so this is a nonzero projection.

The algebra \(P\) is abelian, without a bidual theorem. Since \(\pi(A)\) is abelian, \(P\subset\pi(A)'\); every element of \(P=(\pi(A)')'\) commutes with every element of that larger commutant, hence with every element of \(P\). For \(r\ne s\), choose \(f\in C_c\) with \(f(r)\ne f(s)\). The scalar relations for \(p_r,p_s\), together with commutation, give
\((f(r)-f(s))p_rp_s=0\). Thus the projections \(p_s\) are pairwise orthogonal. PC1 supplies their arbitrary join

<a id="equation-m20"></a>

$$z=\bigvee_{s\in\mathbb R}p_s. \tag{M20}$$

It is central in \(P\). In fact each \(p_sP=\mathbb Cp_s\). Every bounded operator on \(p_s\mathcal H_u\), extended by zero on its perpendicular complement, commutes with \(\pi(A)\): the restriction of \(\pi(f)\) there is the scalar \(f(s)\), and \(p_s\) reduces it. Thus every \(x\in P\) commutes with all of these operators. Commuting with each rank-one projection makes every nonzero vector an eigenvector for the restriction of \(x\); applying this to the sum of two independent vectors makes their eigenvalues equal. The restriction is scalar, proving the assertion, including arbitrary dimension.

The atomic summand is the proved concrete von Neumann algebra

<a id="equation-m21"></a>

$$zP\cong\ell^\infty(\mathbb R). \tag{M21}$$

Here is the full map and its topology. For bounded \(F:\mathbb R\to\mathbb C\), the finite sums \(\sum_{s\in S}F(s)p_s\), indexed by finite subsets \(S\), have norm at most \(\|F\|_\infty\). On each vector their squared tail is bounded by \(\|F\|_\infty^2\sum_{s\notin S}\|p_s\eta\|^2\). Orthogonality bounds the total scalar sum by \(\|\eta\|^2\); its definition as the supremum of finite subsums makes the tails tend to zero. Consequently the finite sums have a strong limit \(\Phi(F)\in zP\). Its adjoint is \(\Phi(\overline F)\), by the same argument. It satisfies \(\Phi(F)p_s=F(s)p_s\), so testing \(\xi_s\) gives \(\|\Phi(F)\|=\|F\|_\infty\). These identities prove linearity, multiplicativity and preservation of adjoints, since an operator in \(zP\) vanishing on every \(p_s\mathcal H_u\) vanishes on their closed span \(z\mathcal H_u\). Conversely \(xp_s=F(s)p_s\), with \(|F(s)|\leq\|x\|\), for \(x\in zP\), and \(x=\Phi(F)\). Thus \(\Phi\) is an onto isometric star isomorphism.

For completeness it and its inverse are normal. Realize \(\ell^\infty(\mathbb R)\) diagonally on the arbitrary Hilbert direct sum \(\ell^2(\mathbb R)\) of GNS7.1. This is a concrete von Neumann algebra: it is the commutant of the one-coordinate rank-one projections. An operator commuting with each such projection takes each basis vector to a scalar multiple of itself; boundedness bounds the coefficients, and finite-coordinate density makes it exactly the associated diagonal operator. PC1 makes \(zP\) a concrete corner on \(z\mathcal H_u\), so CP6 applies on both sides. A vector test of \(\Phi(F)\) is

<a id="equation-cm6"></a>

\[
 \langle\Phi(F)\eta,\zeta\rangle
 =\sum_s F(s)\langle p_s\eta,p_s\zeta\rangle,\qquad
 \sum_s|\langle p_s\eta,p_s\zeta\rangle|
 \leq\|\eta\|\,\|\zeta\|.
 \tag{CM6}
\]
The bound is finite Cauchy--Schwarz followed by the supremum over finite sets. An absolutely summable scalar family \(c_s\) has countable support, since each set \(\{|c_s|\geq1/k\}\) is finite. Its functional \(\sum_s c_sF(s)\) is a normal vector test of the diagonal algebra: choose coordinates \(a_s=\sqrt{|c_s|}\) and \(b_s=\overline{c_s}/\sqrt{|c_s|}\), with both zero when \(c_s=0\). They lie in \(\ell^2\) and \(\langle Fa,b\rangle=\sum_s c_sF(s)\). CP6's vector-series description and norm closure now make the pullback of every normal functional on \(zP\) normal. Conversely every normal test of the diagonal algebra is such an absolutely summable coefficient family, by applying the same Cauchy--Schwarz estimate to its CP6 vector series. Under \(\Phi^{-1}\), it pulls back to the norm-convergent sum \(\sum_s c_s\langle x\xi_s,\xi_s\rangle\), a normal functional on \(zP\) by CP6. This proves normality in both directions on the entire spaces, rather than only on bounded convergent nets.

Suppose a normal automorphism \(\theta_t\) of \(P\) extends the translation \(\alpha_t\) on \(\pi(A)\). Bounded strong convergence is ultraweak convergence by CP6's finite-series/tail estimate, so

<a id="equation-cm7"></a>

\[
 \theta_t(p_s)
 =\lim_n\theta_t(\pi(f_{n,s}))
 =\lim_n\pi(f_{n,s+t})=p_{s+t}.
 \tag{CM7}
\]
Here each limit is justified ultraweakly, and the last also exists strongly by the proved construction. Normality is used on the whole algebra; no existence of a normal extension has been assumed or supplied. An automorphism preserves joins by the order inverse, so \(\theta_t(z)=z\). On the concrete summand its forced formula is exactly

<a id="equation-m22"></a>

$$(\widetilde\alpha_tF)(s)=F(s-t). \tag{M22}$$

In this formula \(\widetilde\alpha_t=\Phi^{-1}\theta_t\Phi\) is merely the transported hypothetical normal extension; it is not presumed continuous. Indeed multiplying \(\theta_t\Phi(F)\) by \(p_s=\theta_t(p_{s-t})\) gives \(F(s-t)p_s\), which proves (M22) on every coordinate.

Take \(q=p_0\) in \(P\), identified under \(\Phi^{-1}\) with the indicator of \(\{0\}\). The functional \(\varepsilon_0(x)=\langle x\xi_0,\xi_0\rangle\) is normal on all of \(P\) by CP6 and restricts under \(\Phi\) to coordinate evaluation at \(0\). Write \(\varepsilon_0\) for this vector functional as well as its coordinate restriction. In the following display \(\widetilde\alpha_t\) denotes \(\theta_t\) on \(P\) as well as its transported restriction, and the two identified scalar evaluations coincide. Therefore every such extension satisfies

<a id="equation-m23"></a>

$$\varepsilon_0(\widetilde\alpha_t(q))
=
\begin{cases}
1,&t=0,\\
0,&t\ne0.
\end{cases} \tag{M23}$$

In (M23) the same notation denotes the normal extension on \(P\) and its restriction under \(\Phi\); both scalar evaluations are identical by construction. The orbit of \(q\) is not ultraweakly continuous at \(0\). Thus no family of normal extensions satisfying (M17) can satisfy (M16), and the universal representation is not an \(\alpha\)-representation.

**Additional problem.** Do the shrinking bumps \(a_{n,s}\to p_s\) converge in operator norm?

**Solution.** No; \(\|a_{n,s}-p_s\|=1\) for every \(n\). Positivity and \(p_s\leq a_{n,s}\leq1\) give the upper bound. For \(r\ne s\), orthogonality gives \(p_s\xi_r=0\), whereas \(a_{n,s}\xi_r=f_{n,s}(r)\xi_r\). As \(r\to s\) through distinct points this value approaches one, proving the lower bound. Strong convergence tests one fixed vector at a time; the norm takes the supremum over all of these vectors. Moreover, for fixed \(t\), \(\varepsilon_0(\pi(f_{n,t}))=\max\{0,1-n|t|\}\) converges to the discontinuous scalar in (M23), so the convergence is not locally uniform in \(t\). This identifies the exact continuity failure.

<a id="oa-flow.cocmat.action"></a>

<a id="cm-matrix"></a>
## A cocycle produces a matrix action

Let \(\alpha:G\to\operatorname{Aut}(M)\) be a point-ultraweakly continuous action of a locally compact abelian group, written additively, and let \(u:G\to\mathcal U(M)\) be a strongly continuous unitary \(\alpha\)-cocycle:

<a id="equation-m1"></a>

$$u_{s+t}=u_s\alpha_s(u_t),\qquad s,t\in G. \tag{M1}$$

On \(M_2=M\mathbin{\overline\otimes}M_2(\mathbb C)\), put

<a id="equation-m2"></a>

$$D_t=
\begin{pmatrix}1&0\\0&u_t\end{pmatrix},
\qquad
\gamma_t=\operatorname{Ad}(D_t)\circ(\alpha_t\otimes\operatorname{id}). \tag{M2}$$

Entrywise,

<a id="equation-m3"></a>

$$
\gamma_t
\begin{pmatrix}x_{11}&x_{12}\\x_{21}&x_{22}\end{pmatrix}
=
\begin{pmatrix}
\alpha_t(x_{11})&
\alpha_t(x_{12})u_t^*\\
u_t\alpha_t(x_{21})&
u_t\alpha_t(x_{22})u_t^*
\end{pmatrix}. \tag{M3}
$$

The cocycle identity is exactly the group-law calculation:

<a id="equation-m4"></a>

$$D_s(\alpha_s\otimes\operatorname{id})(D_t)
=
\begin{pmatrix}1&0\\0&u_s\alpha_s(u_t)\end{pmatrix}
=D_{s+t}. \tag{M4}$$

Therefore

<a id="equation-m5"></a>

$$\gamma_s\gamma_t
=\operatorname{Ad}\!\left(D_s(\alpha_s\otimes\operatorname{id})(D_t)\right)
\circ(\alpha_{s+t}\otimes\operatorname{id})
=\gamma_{s+t}. \tag{M5}$$

The action is point-ultraweakly continuous. Indeed \(t\mapsto D_t\) is strong-star continuous. Finite sums of vector functionals are norm dense in the predual, so every normal functional \(\omega\) satisfies

<a id="equation-m6"></a>

$$\|\omega\circ\operatorname{Ad}(D_t)
-\omega\circ\operatorname{Ad}(D_s)\|\longrightarrow0
\qquad(t\to s). \tag{M6}$$

Split a matrix coefficient of \(\gamma_t(X)-\gamma_s(X)\) into the change of the predual functional in (M6) and the fixed-functional evaluation of
\((\alpha_t^{(2)}-\alpha_s^{(2)})(X)\). The first tends to zero in norm and the second by point-ultraweak continuity of the amplification. This proves the required continuity without claiming operator-norm continuity of \(t\mapsto D_t\).

NCF1 constructs \(M\bar\otimes M_2\) as concrete two-by-two entries and gives the normal amplification of every \(\alpha_t\). Its point-ultraweak continuity follows on finite matrix vector tests from the continuity of each entry; CP6's norm-dense finite tests extend it to every normal functional, using \(\|\alpha_t^{(2)}X\|=\|X\|\). Normality of conjugation is the square-summable vector substitution proved above. Thus \(\gamma_t\) is a normal automorphism, and (M4)–(M5) give an action. The cocycle identity at zero gives \(u_0=1\), so \(\gamma_0=\operatorname{id}\); the group law gives the inverse. There is no operator-norm continuity requirement on \(u\).

<a id="oa-flow.cocmat.corners"></a>

<a id="cm-corners"></a>
## The two fixed corners encode cocycle perturbation

Let

<a id="equation-m7"></a>

$$e_{11}=\begin{pmatrix}1&0\\0&0\end{pmatrix},
\qquad
e_{22}=\begin{pmatrix}0&0\\0&1\end{pmatrix}. \tag{M7}$$

Formula (M3) gives

<a id="equation-m8"></a>

$$e_{11},e_{22}\in\operatorname{Proj}(M_2^\gamma). \tag{M8}$$

Under the canonical identifications \(e_{ii}M_2e_{ii}\cong M\), the two reduced actions are

<a id="equation-m9"></a>

$$\gamma^{e_{11}}=\alpha,
\qquad
\gamma^{e_{22}}=\alpha^u,
\qquad
\alpha_t^u=\operatorname{Ad}(u_t)\circ\alpha_t. \tag{M9}$$

The standard matrix unit

$$v=\begin{pmatrix}0&0\\1&0\end{pmatrix}$$

satisfies \(v^*v=e_{11}\) and \(vv^*=e_{22}\). Thus the two fixed projections are equivalent in the ambient matrix algebra. If the algebra is zero, both reduced algebras are zero and the literal Connes intersections are the same empty intersection, so the conclusion below is immediate. Otherwise apply the complete general [equivalent-fixed-corner theorem](OA-FLOW-GCC.md#gcc-equivalence). Its application to these two corners gives

<a id="equation-m10"></a>

$$\boxed{\Gamma(\alpha)=\Gamma(\alpha^u).} \tag{M10}$$

Notice what the matrix construction accomplishes. The partial isometry \(v\) need not be fixed by \(\gamma\); equivalence in the ambient algebra is enough. The cocycle is stored in the off-diagonal action so that both corner units themselves are fixed.

**Problem.** Take \(M=\mathbb C\), the trivial action of \(\mathbb R\), and \(u_t=e^{it\lambda}\) with \(\lambda\in\mathbb R\). Compute \(\gamma_t\) on \(M_2(\mathbb C)\).

**Solution.** Formula (M3) becomes

<a id="equation-m11"></a>

$$\gamma_t
\begin{pmatrix}a&b\\c&d\end{pmatrix}
=
\begin{pmatrix}
a&e^{-it\lambda}b\\
e^{it\lambda}c&d
\end{pmatrix}. \tag{M11}$$

The two scalar diagonal corners both carry the trivial action even though the off-diagonal phases are \(-\lambda\) and \(\lambda\). With the declared negative spectral convention their labels are \(\lambda\) and \(-\lambda\), respectively. This is the finite-dimensional model of (M9). \(\square\)

The general Connes-spectrum application uses neither an ambient factor hypothesis nor a fixed implementing partial isometry. The corner identifications intertwine all normal Fourier filters, hence their hull spectra and fixed-projection intersections. This last assertion follows by pulling the scalar tests through the normal isomorphisms; fixed projections correspond bijectively. The theorem used in (M10) applies to the full locally compact abelian group and both fixed corners.

<a id="oa-flow.l112.sources"></a>

<a id="cm-sources"></a>
## Sources and scope

The matrix construction and representation-continuity definition correspond to Takesaki, *Theory of Operator Algebras II*, [XI.2 Lemma 2.3, Definition 2.4 and following warning, printed 333](https://doi.org/10.1007/978-3-662-10451-4). The shrinking-bump construction gives a concrete proof of the universal-representation counterexample and its atomic summand. The exposition begins with the continuity test, proves its quasi-equivalence criterion by normal predual averaging, and examines the concrete obstruction before the concluding matrix transport application. Takesaki, *Theory of Operator Algebras II*, X.3 Proposition 3.1, Remark 3.2 and Definition 3.3, printed 279–280, give the source criterion and terminology. QI1–QI3 state their own generality: only the represented Hilbert space is separable. QI2 supplies the increasing-net normality argument explicitly; QI3 localizes the null-set argument to one finite-measure open set. The constant-action example shows why the source remark must be read as a possible failure, not a universal prohibition for nondiscrete groups.

The GNS, concrete-predual and normal-action lessons provide the representation and continuity tools used here. Arveson, [*On groups of automorphisms of operator algebras*](https://www.isibang.ac.in/~soumyashant/misc/collected-works-of-arveson/1970s/1974_On_groups_of_automorphisms_of_operator_algebras.pdf), J. Funct. Anal. 15 (1974), §1, provides a primary account of the distinction between weak integration and actual continuity hypotheses. The complete local providers, rather than these citations, prove every premise used here.

This chapter proves the arbitrary-Hilbert continuity definition and its concrete failure, the complete quasi-equivalence criterion on separable represented Hilbert spaces, quasi-invariant state definitions including nonunital GNS spaces, the full atomic summand and both normal inverse maps, and the normal matrix action at the stated LCA cocycle hypotheses. M10 applies the equivalent-fixed-corner theorem from GCC to the two diagonal matrix corners.

<a id="oa-flow.l112.figure"></a>

## Strong limits and the normal-action continuity test

![Shrinking bumps, a discontinuous normal test, and two fixed matrix corners](../assets/cocycle-matrix-continuity/assets/continuity-corners.png)

The left panels illustrate the complete concrete universal-representation proof in [CM2–7 and M19–23](OA-FLOW-L112.md#cm-obstruction). Here \(A=C_0(\mathbb R)\), \((\alpha_t f)(r)=f(r-t)\), and \(\pi\) is the nondegenerate direct sum of all state GNS representations. The plotted functions are the exact scalar bumps

<a id="equation-cmf1"></a>

\[
 f_{n,0}(r)=\max(0,1-n|r|),\qquad n=1,2,4.
 \tag{CMF1}
\]
The vertices \((-1/n,0),(0,1),(1/n,0)\) determine these piecewise-linear graphs exactly. Raster display uses numerical coordinates, but their semantic data retains the rational vertices. The curves are not graphs of operator-norm convergence.

The proof gives positive contractions \(a_n=\pi(f_{n,0})\) converging strongly to a nonzero projection \(p_0\). The evaluation summand has a unit vector \(\xi_0\) with \(p_0\xi_0=\xi_0\). Every hypothetical normal extension of translation is forced to satisfy \(\theta_t(p_s)=p_{s+t}\), and the actual normal vector functional \(\varepsilon_0(x)=\langle x\xi_0,\xi_0\rangle\) gives

<a id="equation-cmf2"></a>

\[
 \varepsilon_0(\theta_t(p_0))=\mathbf1_{\{0\}}(t),\qquad
 \varepsilon_0(\theta_t(a_n))=\max(0,1-n|t|).
 \tag{CMF2}
\]
Panel 2 uses an open dot at \((0,0)\) and a filled dot at \((0,1)\); there is no vertical segment in the function graph. Thus the forced scalar orbit is discontinuous. The normal extensions are hypothetical, not a claimed continuous action. Each bump test is continuous, and their pointwise limit is not locally uniform in \(t\).

Panel 3 compares actual tests: for the fixed vector \(\xi_{1/3}\), \(\|(a_n-p_0)\xi_{1/3}\|=\max(0,1-n/3)\), giving \(2/3,1/3,0,\ldots\). The moving vector at \(r_n=1/(2n)\) has bump value \(1/2\). The complete proof gives the stronger exact norm assertion \(\|a_n-p_0\|=1\) for every \(n\), by taking the supremum of evaluations at distinct points tending to zero. No uniform strong-convergence rate on all unit vectors is asserted.

Panel 4 shows a separate general construction from [M1–M11](OA-FLOW-L112.md#cm-matrix). Its group is arbitrary LCH abelian, its algebra and Hilbert space are arbitrary, and its cocycle is strongly continuous:

<a id="equation-cmf3"></a>

\[
 u_{s+t}=u_s\alpha_s(u_t),\qquad
 \gamma_t=\operatorname{Ad}\operatorname{diag}(1,u_t)\circ\alpha_t^{(2)}.
 \tag{CMF3}
\]
The four drawn entries are exactly M3. The fixed diagonal projections have reduced actions \(\alpha\) and \(\alpha^u\), and the lower-left matrix unit implements their ambient equivalence. It need not be fixed. The [general fixed-corner theorem](OA-FLOW-GCC.md#gcc-equivalence) gives \(\Gamma(\alpha)=\Gamma(\alpha^u)\); this application uses the hypotheses proved in GCC. Neither a real-action factor specialization nor the discontinuous extension of the left panels replaces that input.

The normality and full predual-norm continuity estimate are proved in the earlier [local predual section](OA-FLOW-L112.md#cm-predual). With the negative Fourier convention, the scalar example \(u_t=e^{it\lambda}\) has upper-right phase \(e^{-it\lambda}\) and label \(\lambda\), and lower-left phase \(e^{it\lambda}\) and label \(-\lambda\). Those phases are not silently interchanged in the diagram.

The source antecedent for the matrix construction and continuity warning is Takesaki, *Theory of Operator Algebras II*, [XI.2 Lemma 2.3, Definition 2.4 and following warning, printed 333](https://doi.org/10.1007/978-3-662-10451-4). The shrinking-bump construction, concrete atomic-summand proof, exact topology checks and combined figure are original here; the actual source page contains no corresponding model or illustration. The GNS, CP and AT lessons supply the representation, predual and continuity results used in the construction.

[Editable SVG](../assets/cocycle-matrix-continuity/assets/continuity-corners.svg), [exact semantic data](../assets/cocycle-matrix-continuity/assets/continuity-corners-data.json), and [reproduction source](../assets/cocycle-matrix-continuity/render_continuity.py) accompany the native 3200×2200 PNG. Fonts use the installed DejaVu Sans family; no font file is redistributed. Original illustration and caption: GPT-6.1 Sol (OpenAI), Ultra, 5 October 2026, CC0-1.0 to the extent of rights held.
