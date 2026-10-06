<span id="spatial-energy-as-a-corner-of-a-modular-operator"></span>
# Spatial energy as a corner of a modular operator

<a id="OA-MOD-SI-01"></a>
<span id="oa-mod-si-01-conventions-and-exact-inputs"></span>
<span id="oa-mod-si-01"></span>
## OA-MOD-SI-01. Conventions and exact inputs

Let \(M\subseteq B(H)\) be a concrete unital von Neumann algebra, put \(N=M'\), and fix an NSF weight \(\psi\) on \(N\). Here NSF means normal, semifinite and faithful. The Hilbert space and all indexing sets are arbitrary. Inner products are linear in the first variable.

Use [SC-01–10](../../reader/orbit-proof-route/scdirect.html#OA-MOD-SC-01) for the direct spatial form. Thus
\[
R_\psi(\xi)\Lambda_\psi(y)=y\xi,\qquad
\theta_\psi(\xi)=R_\psi(\xi)R_\psi(\xi)^*,\qquad \xi\in D_\psi.
\tag{SI.1}
\]
For a normal numerator \(\varphi\), its closed form has domain \(V_\varphi\), Hilbert closure \(e_\varphi H\), and null space \(f_\varphi H\). Its effective support is \(p_\varphi=e_\varphi-f_\varphi\). Its represented operator acts on \(e_\varphi H\); for a semifinite numerator, \(e_\varphi=1\).

The exact further inputs are WG's GNS and finite-ideal results; WS-02–06's finite and null corners; OW-03/08's opposite-weight vector criterion; WH-02–13's full Hilbert algebras, right weight, GNS identifications and existence of an NSF weight; and MF-05–06's modular conjugation and modular automorphism theorem. BK supplies bounded polar decompositions, bicommutants and operator topologies. TC supplies closed-involution polar decomposition. SK-05–09 supplies the spectral calculus with actual domains. FC and QF supply closed-form uniqueness and representation. [SS-09](../../reader/orbit-proof-route/index.html#downstream-spatial-convergence) is used for the final convergence consequence. CP's normal vector-series representation supplies its predual-topology step. MA enters through MF's already proved analytic arguments; no additional strip theorem is assumed here.

These results use their stated scalar and Hilbert-space prerequisites. In particular, the argument does not invoke the uniqueness part of the KMS characterization to identify a corner modular group. It identifies that group's GNS operator directly.

For a closed antilinear map \(T\), write \(|T|=(T^*T)^{1/2}\). The relative modular operator in this unit is
\[
\Delta_T=T^*T=|T|^2.
\tag{SI.2}
\]
This convention is fixed by the squared-norm energy formula. An antilinear polar factor between different Hilbert spaces is not automatically a conjugation on either space.



<span id="oa-mod-si-02-the-opposite-weight-and-its-modular-data"></span>
<span id="OA-MOD-SI-02"></span>
<span id="oa-mod-si-02"></span>
## OA-MOD-SI-02. The opposite weight and its modular data

Let \(\omega\) be NSF on an algebra \(B\), and identify \(B\) with its faithful GNS image on \(K=H_\omega\). Write \(S,J,\Delta\) for its modular data. Let \(\omega^{\mathrm{opp}}\) be the OW weight on \(B'\).

**Proposition.** Its GNS space identifies canonically with \(K\), its closed involution is \(S^*\), and its modular data are \(J,\Delta^{-1}\). For positive \(b\in B\),
\[
\omega^{\mathrm{opp}}(JbJ)=\omega(b),\qquad
(\omega^{\mathrm{opp}})^{\mathrm{opp}}=\omega
\tag{SI.3}
\]
under these specified GNS identifications. In particular,
\[
\sigma_t^{\omega^{\mathrm{opp}}}(c)=\Delta^{-it}c\Delta^{it}
\quad(c\in B').
\tag{SI.4}
\]

**Proof.** Let \(\mathcal A=\Lambda_\omega(\mathfrak n_\omega\cap\mathfrak n_\omega^*)\) be the full left algebra and \(\mathcal D\) its full right algebra. WH identifies its right weight with \(\omega^{\mathrm{opp}}\). If \(R_\eta\in B'\) is the right multiplier of a right-bounded vector, the canonical GNS identification is
\[
\Gamma(R_\eta)=\eta,
\qquad \omega^{\mathrm{opp}}(R_\eta^*R_\eta)=\|\eta\|^2.
\tag{SI.5}
\]
WH's finite-ideal theorem makes this the entire GNS map, not just a dense submap. Its finite-star algebra is \(\mathcal D^{\mathrm{op}}\), whose closed involution is \(F=S^*\). TC gives \(F=J\Delta^{-1/2}\). Polar uniqueness gives the asserted modular data and MF gives (SI.4).

For completeness, MF's identity \(J\lambda_\xi J=R_{J\xi}\) also extends to all left-bounded vectors, and symmetrically to right-bounded vectors. Indeed, if \(\eta\) is right bounded and \(\zeta\in\mathcal D\), then
\[
R_\zeta J\eta=J\lambda_{J\zeta}\eta=JR_\eta J\zeta.
\]
This is exactly the left-bounded test for \(J\eta\), with multiplier \(JR_\eta J\). The reverse follows by \(J^2=1\).

Now \(\omega(b)<\infty\) precisely when \(b^{1/2}=\lambda_\xi\) for a left-bounded vector \(\xi\), and its value is \(\|\xi\|^2\). The preceding identity makes \(Jb^{1/2}J=R_{J\xi}\), with the same squared norm. The symmetric argument proves the converse. Thus the finite positive cones and their values correspond, proving the first formula of (SI.3), including infinite values. Applying WH's construction to the opposite right algebra recovers the original full left algebra and its weight. This proves the double-opposite assertion. ∎

We will also use the equality between \(D_\omega(K)\), defined by the GNS test, and the right-bounded space just used. Restriction of the GNS test gives one inclusion. For the other, choose finite positive contractions \(u_i\uparrow1\). If \(x\in\mathfrak n_\omega\), then \(u_i x\in\mathfrak n_\omega\cap\mathfrak n_\omega^*\),
\(\Lambda(u_i x)\to\Lambda(x)\), and \(u_i x\eta\to x\eta\). The bounded right-multiplier identity on the finite-star algebra therefore extends to all \(x\in\mathfrak n_\omega\). This proves the equality with its exact operator.

<a id="OA-MOD-SI-03"></a>
<span id="oa-mod-si-03-unitary-and-antiunitary-changes-of-representation"></span>
<span id="oa-mod-si-03"></span>
## OA-MOD-SI-03. Unitary and antiunitary changes of representation

Let \(C:H\to\widetilde H\) be unitary or antiunitary. Transport both algebras by \(x\mapsto CxC^{-1}\), and transport each weight on positive elements by composition with the inverse map. The latter is well-defined even when the map is conjugate-linear: it preserves addition, nonnegative scalar multiplication, positivity and positive suprema.

**Lemma.** The transported spatial form has domain \(CV_\varphi\) and energy
\[
\widetilde q[C\xi]=q[\xi].
\tag{SI.6}
\]
Its operator, on the transported Hilbert subspace, is \(CAC^{-1}\) with domain \(CD(A)\).

**Proof.** The GNS map
\[
G\Lambda_\psi(y)=\Lambda_{\widetilde\psi}(CyC^{-1})
\]
extends to a unitary or antiunitary of the same type as \(C\). Its norm equality follows from the weight formula; polarization gives the appropriate inner-product identity. It has dense range because the entire finite left ideal is transported bijectively. The defining bounded-vector test then gives
\[
D_{\widetilde\psi}=CD_\psi,
\qquad
R_{\widetilde\psi}(C\xi)=CR_\psi(\xi)G^{-1}.
\tag{SI.7}
\]
Both sides of the second formula are linear operators. Their coefficients are \(C\theta_\psi(\xi)C^{-1}\), so their initial energies agree. The same map preserves the form-completion norm. SC's canonical closure therefore gives (SI.6) on the full domains. Real spectral calculus and closed-form uniqueness identify the represented operator and its domain. ∎

For an antiunitary \(C\), complex powers require the scalar conjugation:
\[
C A^{it}C^{-1}=(CAC^{-1})^{-it}.
\tag{SI.8}
\]
This follows from SK's antiunitary Borel calculus; it is not the formula for a unitary change of representation.

<a id="OA-MOD-SI-04"></a>
<span id="oa-mod-si-04-every-finite-rectangular-intertwiner-has-a-vector"></span>
<span id="oa-mod-si-04"></span>
## OA-MOD-SI-04. Every finite rectangular intertwiner has a vector

Return to \(N\subseteq B(H)\), \(\psi\), and \(K=H_\psi\). Put
\[
B=\pi_\psi(N)',\qquad \chi=\psi^{\mathrm{opp}},
\qquad
\mathcal X=\{X\in B(K,H):X\pi_\psi(y)=yX\ (y\in N)\}.
\tag{SI.9}
\]

**Theorem.** The following maps are inverse bijections:
\[
\begin{aligned}
D_\psi&\longrightarrow\{X\in\mathcal X:\chi(X^*X)<\infty\},\\
\xi&\longmapsto R_\psi(\xi),\\
\{X\in\mathcal X:\chi(X^*X)<\infty\}&\longrightarrow D_\psi,\\
X&\longmapsto\eta(X).
\end{aligned}
\tag{SI.10}
\]
They satisfy
\[
\chi(X^*X)=\|\eta(X)\|^2,
\quad \eta(aX)=a\eta(X)\quad(a\in M).
\tag{SI.11}
\]

**Proof.** Use the rectangular polar decomposition \(X=Vh\), where \(h=(X^*X)^{1/2}\in B\). The polar factor intertwines the two \(N\)-actions. Its initial and final projections \(P=V^*V\in B\) and \(Q=VV^*\in M\) are the respective support projections.

If \(\chi(h^2)<\infty\), OW-08 supplies a unique \(\zeta\in K\) such that
\[
h\Lambda_\psi(y)=\pi_\psi(y)\zeta,
\qquad\|\zeta\|^2=\chi(h^2)
\quad(y\in\mathfrak n_\psi).
\]
Because \(Ph=h\) and \(P\) commutes with \(\pi_\psi(N)\), the vector \((1-P)\zeta\) is annihilated by every \(\pi_\psi(y)\) in that finite ideal. Finite cutoffs imply \(P\zeta=\zeta\). Set \(\eta(X)=V\zeta\). Then
\[
X\Lambda_\psi(y)=yV\zeta,
\qquad\|V\zeta\|=\|\zeta\|,
\]
so \(X=R_\psi(\eta(X))\) and (SI.11)'s norm formula follows.

Conversely let \(X=R_\psi(\xi)\). Since \(QX=X\), the equation \((1-Q)y\xi=0\) and finite cutoffs give \(Q\xi=\xi\). Hence \(\zeta=V^*\xi\) has norm \(\|\xi\|\), and
\[
h\Lambda_\psi(y)=V^*y\xi=\pi_\psi(y)\zeta.
\]
OW-08 gives \(\chi(X^*X)=\|\xi\|^2\). Injectivity of \(R_\psi\), proved in SD, makes the two constructions inverse. The covariance \(R_\psi(a\xi)=aR_\psi(\xi)\) gives the final assertion. Linearity of the inverse follows from injectivity and linearity of \(R_\psi\). ∎

The theorem proves surjectivity onto the whole finite rectangular ideal. Merely expressing some intertwiners as products would not supply the GNS identification needed next.

<a id="OA-MOD-SI-05"></a>
<span id="oa-mod-si-05-a-diagonal-weight-separates-four-graph-corners"></span>
<span id="oa-mod-si-05"></span>
## OA-MOD-SI-05. A diagonal weight separates four graph corners

Here is the block argument in a general algebra. Let \(L\) be a von Neumann algebra with complementary projections \(e,f\), and let \(\alpha,\beta\) be NSF weights on \(eLe,fLf\). Define
\[
\rho(z)=\alpha(eze)+\beta(fzf),\qquad z\in L_+.
\tag{SI.12}
\]

**Lemma.** This is NSF. On its GNS space \(H_\rho\), left multiplication \(L_i=\pi_\rho(i)\) and
\[
Q_i\Lambda_\rho(x)=\Lambda_\rho(xi),\qquad i=e,f,
\tag{SI.13}
\]
are commuting orthogonal projections. Put \(H_{ij}=L_iQ_jH_\rho\). The closed Tomita map \(S_\rho\) carries \(D(S_\rho)\cap H_{ij}\) bijectively onto \(D(S_\rho)\cap H_{ji}\), and
\[
S_\rho L_iQ_j\xi=L_jQ_i S_\rho\xi
\quad(\xi\in D(S_\rho)).
\tag{SI.14}
\]
Each \(L_i,Q_j\) reduces \(\Delta_\rho\), and
\[
J_\rho L_iJ_\rho=Q_i,
\qquad J_\rho H_{ij}=H_{ji}.
\tag{SI.15}
\]
The vectors
\[
\Lambda_\rho(iLj\cap\mathfrak n_\rho\cap\mathfrak n_\rho^*)
\tag{SI.16}
\]
form a graph core for the restricted Tomita map on \(H_{ij}\).

**Proof of the weight and projections.** Compression is positive and normal; addition proves the weight axioms and normality. If \(z\geq0\) has both diagonal compressions zero, then \(z^{1/2}e=z^{1/2}f=0\), so \(z=0\). Faithfulness follows. Finite positive contractions in the two corners combine to an increasing finite positive contraction net with supremum \(1\). Thus WG proves semifiniteness.

For any \(x\in\mathfrak n_\rho\),
\[
\rho(x^*x)=\rho(ex^*xe)+\rho(fx^*xf).
\tag{SI.17}
\]
It follows that \(xe,xf\in\mathfrak n_\rho\) and that their GNS vectors give an orthogonal decomposition of \(\Lambda_\rho(x)\). Polarization proves that (SI.13) extends to complementary orthogonal projections. They commute with every left multiplier. Likewise \(L_e,L_f\) are complementary orthogonal projections. This proves the four-space decomposition.

**Proof of the domain assertions.** Compression \(x\mapsto ixj\) preserves the finite-star domain: its GNS norm is bounded by that of \(x\), and the same holds after taking adjoints. On this domain, adjunction gives (SI.14). Approximate an arbitrary \(\xi\in D(S_\rho)\) in the full graph norm by finite-star GNS vectors and compress them. Closedness gives (SI.14) and proves (SI.16). Applying \(S_\rho^2=1\) on its domain gives the stated bijection.

The adjoint pairing for this orthogonal decomposition makes \(S_\rho^*\) exchange the same pair of corners in the reverse direction. Hence \(S_\rho^*S_\rho\) reduces every corner and each sum of corners defining \(L_i,Q_j\). On the dense domain, \(S_\rho L_i=Q_iS_\rho\). In its polar decomposition \(S_\rho=J_\rho\Delta_\rho^{1/2}\), the square root commutes with \(L_i\) and has dense range. Thus \(J_\rho L_i=Q_iJ_\rho\), first on that range and then everywhere. This proves (SI.15). ∎

The \(ii\) corner, with map \(x\mapsto\Lambda_\rho(x)\) for \(x\in iLi\cap\mathfrak n_\rho\), is exactly the GNS space of the corresponding corner weight. Its restricted \(S,J,\Delta\) are therefore that weight's modular data. In particular \(\sigma_t^\rho(e)=e\), \(\sigma_t^\rho(f)=f\), and the corner restrictions of \(\sigma_t^\rho\) are \(\sigma_t^\alpha,\sigma_t^\beta\). This conclusion uses the actual GNS and graph-core identifications above.

<a id="OA-MOD-SI-06"></a>
<span id="oa-mod-si-06-the-first-gns-column-is-the-original-representation"></span>
<span id="oa-mod-si-06"></span>
## OA-MOD-SI-06. The first GNS column is the original representation

For now assume that \(\varphi\) is NSF on \(M\). On \(K\oplus H\), define
\[
\mathcal N=\{\pi_\psi(y)\oplus y:y\in N\},
\qquad L=\mathcal N',
\tag{SI.18}
\]
and let \(e,f\) project onto \(K,H\). The diagonal representation is faithful and normal. WH-02 makes its image a von Neumann algebra, so \(L'=\mathcal N\). Its corners are
\[
eLe=B,\qquad fLf=M,\qquad fLe=\mathcal X.
\tag{SI.19}
\]
Both \(e\) and \(f\) have central support \(1\) in \(L\): a central projection annihilating either coordinate belongs to \(L'=\mathcal N\), and faithfulness of that coordinate representation makes it zero.

Apply SI-05 with \(\alpha=\chi=\psi^{\mathrm{opp}}\), \(\beta=\varphi\). Its first column \(Q_eH_\rho=H_{ee}\oplus H_{fe}\) identifies with \(K\oplus H\) by
\[
\Lambda_\rho\begin{pmatrix}b&0\\X&0\end{pmatrix}
\longmapsto\Gamma(b)\oplus\eta(X).
\tag{SI.20}
\]
Indeed the finite condition is exactly \(\chi(b^*b)<\infty\), \(\chi(X^*X)<\infty\), and (SI.5), (SI.11) give equality of squared norms. The range is dense: \(\Gamma(\mathfrak n_\chi)\) is dense in \(K\), and \(D_\psi\) is dense in \(H\) by SC. The map therefore extends to a unitary.

This unitary intertwines the entire left action of \(L\). To see this without an unproved module formula, identify a finite column \(Z\) with the map \(K\to K\oplus H\) satisfying
\[
Z\Lambda_\psi(y)=(\pi_\psi(y)\oplus y)\zeta,
\]
where \(\zeta\) is its image in (SI.20). For \(a\in L\), the column \(aZ\) has the same equation with \(a\zeta\). The finite left ideal is stable under \(a\), and uniqueness in SI-04 identifies its vector. Thus (SI.20) carries \(\pi_\rho(a)\) to \(a\).

Under this identification,
\[
\Delta_\rho^{it}|_{Q_eH_\rho}
=\Delta_\psi^{-it}\oplus U_t,
\tag{SI.21}
\]
for a strongly continuous unitary group \(U_t\) on \(H=H_{fe}\). The first component is SI-02, and the two components are reducing by SI-05. We next identify the generator of the second component.

<a id="OA-MOD-SI-07"></a>
<span id="oa-mod-si-07-the-relative-map-has-exactly-the-coefficient-form"></span>
<span id="oa-mod-si-07"></span>
## OA-MOD-SI-07. The relative map has exactly the coefficient form

Let \(K_{\varphi,\psi}=H_{ef}\). For
\[
E_{\varphi,\psi}=\{\xi\in D_\psi:
\varphi(\theta_\psi(\xi))<\infty\},
\tag{SI.22}
\]
define the antilinear map
\[
T^0_{\varphi,\psi}\xi
=\Lambda_\rho(R_\psi(\xi)^*)\in H_{ef}.
\tag{SI.23}
\]
Here \(R_\psi(\xi)\) is placed in the \(fe\) operator corner. The source and target Hilbert spaces in this formula are different.

**Theorem.** The map is closable, its closure \(T_{\varphi,\psi}\) is the restricted closed Tomita block of SI-05, and
\[
D(T_{\varphi,\psi})=V_\varphi=D(A^{1/2}),
\qquad
T_{\varphi,\psi}^*T_{\varphi,\psi}=A,
\tag{SI.24}
\]
where \(A=d\varphi/d\psi\) denotes SC's direct operator. Its polar factor
\[
C_{\varphi,\psi}=J_\rho|_{H_{fe}}:H\longrightarrow K_{\varphi,\psi}
\tag{SI.25}
\]
is antiunitary, and
\[
T_{\varphi,\psi}=C_{\varphi,\psi}A^{1/2},
\qquad A=\Delta_\rho|_{H_{fe}}.
\tag{SI.26}
\]

**Proof.** SI-04 identifies all finite \(fe\) columns with \(D_\psi\). An \(fe\) operator \(X\) is in the finite-star domain precisely when both \(\chi(X^*X)\) and \(\varphi(XX^*)\) are finite. Thus (SI.22) corresponds to exactly the graph core (SI.16), not merely a subspace of it. On that core the Tomita map is (SI.23), and
\[
\|T^0_{\varphi,\psi}\xi\|^2
=\rho(R_\psi(\xi)R_\psi(\xi)^*)
=\varphi(\theta_\psi(\xi)).
\tag{SI.27}
\]
The graph norm of this map is consequently SC's initial form norm. SI-05 proves that its graph closure is the entire restricted block. Its closed energy form is therefore the canonical completion of the same initial form used in SC. Uniqueness of that completion and of the represented operator gives (SI.24). The reducing-corner polar decomposition gives (SI.25–26). Both corners are exchanged by the involutive antiunitary \(J_\rho\), so this polar factor is onto. ∎

In particular \(U_t=A^{it}\) in (SI.21). The identification is a consequence of equality of the actual closed graph completions; using the same symbol for two constructions would not prove it.

<a id="OA-MOD-SI-08"></a>
<span id="oa-mod-si-08-the-two-modular-actions-and-the-relative-conjugation"></span>
<span id="oa-mod-si-08"></span>
## OA-MOD-SI-08. The two modular actions and the relative conjugation

**Theorem.** For NSF \(\varphi,\psi\), the positive operator \(A\) is injective and
\[
A^{it}xA^{-it}=\sigma_t^\varphi(x)\quad(x\in M),
\tag{SI.28}
\]
\[
A^{it}yA^{-it}=\sigma_{-t}^\psi(y)\quad(y\in N).
\tag{SI.29}
\]

**Proof.** SC identifies the kernel as \(f_\varphi H=0\). On the first GNS column, MF and (SI.21) show that \(\Delta_\psi^{-it}\oplus A^{it}\) normalizes \(L\). Its action on the \(ff\) corner is \(\sigma_t^\varphi\), by SI-05, proving (SI.28).

The same unitary therefore normalizes \(L'=\mathcal N\). For \(y\in N\), its first diagonal component after conjugation is
\[
\Delta_\psi^{-it}\pi_\psi(y)\Delta_\psi^{it}
=\pi_\psi(\sigma_{-t}^\psi(y)).
\]
Faithfulness of \(\pi_\psi\) determines the element of \(N\) in this diagonal operator. Its second component must be \(\sigma_{-t}^\psi(y)\), proving (SI.29). ∎

The relative conjugation can also be specified as an action between corners. Put
\[
j_\psi(y)=J_\psi\pi_\psi(y^*)J_\psi\in B.
\tag{SI.30}
\]
This is a complex-linear *-anti-isomorphism \(N\to B\). On the first column, the right action of \(b\in eLe=B\) is
\[
\mathcal R(b)=J_\rho\pi_\rho(b^*)J_\rho.
\]
On its \(ee\) component, SI-02 gives the action \(J_\psi b^*J_\psi\). Hence
\[
\mathcal R(j_\psi(y))=\pi_\psi(y)\oplus y.
\tag{SI.31}
\]
To justify the second component, both operators commute with \(L\), so belong to \(\mathcal N\); their first components agree, and that component is faithful. Consequently, with \(C=C_{\varphi,\psi}\),
\[
C y C^{-1}=\pi_\rho(j_\psi(y)^*)|_{H_{ef}},
\tag{SI.32}
\]
\[
C x C^{-1}
=J_\rho\pi_\rho(x)J_\rho|_{H_{ef}}
\quad(x\in M=fLf).
\tag{SI.33}
\]
The latter is the right \(fLf\)-action corresponding to \(x^*\). These are conjugate-linear transformations of algebras, as required by the antiunitary \(C\). They specify the two actions without postulating a modular conjugation \(H\to H\) for the given representation.



<span id="oa-mod-si-12-ordinary-relative-gns-maps-are-a-specialization"></span>
<span id="OA-MOD-SI-12"></span>
<span id="oa-mod-si-12"></span>
## OA-MOD-SI-12. Ordinary relative GNS maps are a specialization

Let \(\omega,\varphi\) be NSF weights on an abstractly identified von Neumann algebra \(M\). Represent \(M\) faithfully on \(H_\omega\), and use \(\omega^{\mathrm{opp}}\) as the denominator on its commutant. By SI-02 its GNS space canonically identifies with \(H_\omega\), and its opposite weight is \(\omega\). The linking algebra is therefore \(M_2(M)\), with diagonal weight \(\omega\oplus\varphi\).

For a column \(j\), every one of its two row spaces identifies with \(H_{\omega_j}\), where \(\omega_1=\omega\), \(\omega_2=\varphi\), through
\[
\Lambda_{\omega_j}(x)\longmapsto\Lambda_{\omega\oplus\varphi}(xE_{ij}).
\tag{SI.53}
\]
The norm equality is immediate from the \(jj\) diagonal of \((xE_{ij})^*(xE_{ij})\); the full finite-left ideal gives dense range. The off-diagonal Tomita block from column \(1\) to column \(2\) is therefore the closure of
\[
S^0_{\varphi,\omega}\Lambda_\omega(x)
=\Lambda_\varphi(x^*),
\qquad x\in\mathfrak n_\omega\cap\mathfrak n_\varphi^*.
\tag{SI.54}
\]
Its initial domain is dense, and it is a graph core for its closure by SI-05, applied to this exact matrix corner. The reverse block is the inverse on its actual range, because the full closed Tomita map is involutive. In particular both block polar factors are antiunitaries, inverse to one another, and
\[
S_{\varphi,\omega}^*S_{\varphi,\omega}
=\frac{d(\varphi\circ\pi_\omega^{-1})}{d\omega^{\mathrm{opp}}}
\quad\text{on }H_\omega.
\tag{SI.55}
\]
This proves the ordinary relative-modular identification with the direct spatial derivative, including the mixed finite-star graph core. It does not identify the two GNS spaces by an unconstructed common natural cone. Such a standard-form identification is a further possible representation of these already specified maps.

<a id="OA-MOD-SI-13"></a>


<span id="oa-mod-si-14-the-balanced-matrix-cocycle-is-independent-of-the-reference"></span>
<span id="OA-MOD-SI-14"></span>
<span id="oa-mod-si-14"></span>
## OA-MOD-SI-14. The balanced-matrix cocycle is independent of the reference

Let \(\varphi_1,\varphi_2\) be NSF on \(M\), and put \(A_j=d\varphi_j/d\psi\). Define
\[
u_t=A_2^{it}A_1^{-it}.
\tag{SI.60}
\]
These are bounded products of unitaries. By (SI.29), their conjugations on \(N\) cancel, so \(u_t\in N'=M\). They are strongly* continuous in \(t\). Direct multiplication gives
\[
u_{s+t}=u_s\sigma_s^{\varphi_1}(u_t),
\qquad
\sigma_t^{\varphi_2}(x)=u_t\sigma_t^{\varphi_1}(x)u_t^*.
\tag{SI.61}
\]
For example, in the first identity replace \(\sigma_s^{\varphi_1}\) by conjugation with \(A_1^{is}\). The adjacent factors \(A_1^{-is}A_1^{is}\) and \(A_1^{-it}A_1^{-is}\) then give exactly (SI.60) at \(s+t\). No commutation between \(A_1\) and \(A_2\) is used.

To prove reference independence, define the intrinsic weight
\[
\Phi([x_{ij}])=\varphi_1(x_{11})+\varphi_2(x_{22})
\quad\text{on }M_2(M)_+.
\tag{SI.62}
\]
Represent this algebra on \(H\oplus H\). Its commutant is \(\{y\oplus y:y\in N\}\): commuting with the scalar matrix units first forces this diagonal shape, and commuting with diagonal copies of \(M\) then gives \(y\in N\). Use \(\psi\) on this commutant. A vector \((\xi_1,\xi_2)\) is bounded exactly when both components are in \(D_\psi\); its coefficient is the matrix \([R_\psi(\xi_i)R_\psi(\xi_j)^*]\). Thus its finite energy is
\[
q_{\varphi_1}[\xi_1]+q_{\varphi_2}[\xi_2].
\]
The product of the two SC cores is a core for this orthogonal sum, by separate graph approximation of its two components. Therefore
\[
\frac{d\Phi}{d\psi}=A_1\oplus A_2.
\tag{SI.63}
\]
Apply (SI.28) to this amplified pair. With \(E_{21}\) the scalar matrix unit,
\[
\sigma_t^\Phi(E_{21})=u_tE_{21}.
\tag{SI.64}
\]
The left side is defined from the weight's intrinsic GNS modular group by MF; it contains no reference \(\psi\). Hence (SI.60) is independent of the NSF commutant reference. It is also independent of the faithful normal concrete realization of \(M\): a normal *-isomorphism transports the weight's entire GNS map and its finite-star graph core, and hence its \(S,J,\Delta\) and modular group. The transported matrix-unit identity is (SI.64).

We may therefore define the balanced-matrix weight cocycle by
\[
[D\varphi_2:D\varphi_1]_tE_{21}
=\sigma_t^{\varphi_1\oplus\varphi_2}(E_{21}).
\tag{SI.65}
\]
Then the spatial formula is the exact identity
\[
A_2^{it}=[D\varphi_2:D\varphi_1]_t A_1^{it}.
\tag{SI.66}
\]
This is the balanced-weight construction used for the source cocycle. The full analytic/KMS characterization of this family, its uniqueness among families satisfying that characterization, and converse reconstruction from an arbitrary cocycle are separate theorems. None is needed to establish (SI.61), (SI.64–66).

<a id="OA-MOD-SI-15"></a>
