# Spatial energy as a corner of a modular operator

**Self-checked by the writing AI.**

The coefficient construction gives a closed energy form on the original representation space. A relative Tomita construction gives a closed antilinear map between two Hilbert spaces. To identify them, we construct an isometry between their initial domains, prove that it respects the whole graph core, and compare the resulting closed forms. A diagonal weight on an algebra of two-by-two operator blocks supplies the common setting. This also explains why the two modular actions have opposite time directions.

The mathematical antecedents are Takesaki, *Theory of Operator Algebras II*, VIII.3, the balanced-weight and relative-map construction, and IX.3, Lemmas 3.3–3.5, Definition 3.6 and Theorem 3.8. The proofs below use the completed ordinary modular theorem and the opposite-weight construction. They do not use the natural-cone vector-representation theorem or assume that an arbitrary concrete representation is standard.

## Conventions and exact inputs

Let \(M\subseteq B(H)\) be a concrete unital von Neumann algebra, put \(N=M'\), and fix an NSF weight \(\psi\) on \(N\). Here NSF means normal, semifinite and faithful. The Hilbert space and all indexing sets are arbitrary. Inner products are linear in the first variable.

Use Conventions and the actual prerequisites through Weight order is exactly closed-form order for the direct spatial form. Thus

\[
R_\psi(\xi)\Lambda_\psi(y)=y\xi,\qquad
\theta_\psi(\xi)=R_\psi(\xi)R_\psi(\xi)^*,\qquad \xi\in D_\psi.
\tag{SI.1}
\]

For a normal numerator \(\varphi\), its closed form has domain \(V_\varphi\), Hilbert closure \(e_\varphi H\), and null space \(f_\varphi H\). Its effective support is \(p_\varphi=e_\varphi-f_\varphi\). Its represented operator acts on \(e_\varphi H\); for a semifinite numerator, \(e_\varphi=1\).

The exact further inputs are WG's GNS and finite-ideal results; WS-02–06's finite and null corners; OW-03/08's opposite-weight vector criterion; WH-02–13's full Hilbert algebras, right weight, GNS identifications and existence of an NSF weight; and MF-05–06's modular conjugation and modular automorphism theorem. BK supplies bounded polar decompositions, bicommutants and operator topologies. TC supplies closed-involution polar decomposition. SK-05–09 supplies the spectral calculus with actual domains. FC and QF supply closed-form uniqueness and representation. Increasing weights, finite energy and resolvents is used for the final convergence consequence. CP's normal vector-series representation supplies its predual-topology step. MA enters through MF's already proved analytic arguments; no additional strip theorem is assumed here.

These inputs depend in turn on their stated scalar and Hilbert-space prerequisites, which are not proved here. In particular, the argument does not invoke the uniqueness part of the KMS characterization to identify a corner modular group. It identifies that group's GNS operator directly.

For a closed antilinear map \(T\), write \(|T|=(T^*T)^{1/2}\). The relative modular operator in this unit is

\[
\Delta_T=T^*T=|T|^2.
\tag{SI.2}
\]

This convention is fixed by the squared-norm energy formula. An antilinear polar factor between different Hilbert spaces is not automatically a conjugation on either space.

## The opposite weight and its modular data

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

## Unitary and antiunitary changes of representation

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

## Every finite rectangular intertwiner has a vector

Return to \(N\subseteq B(H)\), \(\psi\), and \(K=H_\psi\). Put

\[
B=\pi_\psi(N)',\qquad \chi=\psi^{\mathrm{opp}},
\qquad
\mathcal X=\{X\in B(K,H):X\pi_\psi(y)=yX\ (y\in N)\}.
\tag{SI.9}
\]

**Theorem.** The following maps are inverse bijections:

\[
\begin{split}
D_\psi&\longrightarrow\{X\in\mathcal X:\chi(X^*X)<\infty\},
&\xi&\longmapsto R_\psi(\xi),\\
\{X\in\mathcal X:\chi(X^*X)<\infty\}&\longrightarrow D_\psi,
&X&\longmapsto\eta(X).
\end{split}
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

## A diagonal weight separates four graph corners

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

## The first GNS column is the original representation

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

## The relative map has exactly the coefficient form

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

## The two modular actions and the relative conjugation

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

## Support reduction without an unspecified restricted weight

Now let \(\varphi\) be any normal weight. Put \(e=e_\varphi\), \(f=f_\varphi\), \(p=e-f\). WS identifies the restriction \(\varphi_p\) to \(pMp\) as NSF. The zero corner is allowed.

First apply the preceding linking construction to the diagonal representation

\[
\begin{gathered}
y\longmapsto\pi_\psi(y)\oplus(y|_{pH})\\
\text{on }H_\psi\oplus pH.
\end{gathered}
\tag{SI.34}
\]

This representation is faithful because its first component is faithful. Only the first coordinate projection needs full central support: a central projection commutes with the whole linking algebra and therefore lies in the diagonal image. Killing the first coordinate then makes it zero by faithfulness of that first action. The second projection need not have full central support when the action on \(pH\) has a kernel. The first-column isometry, finite-ideal inverse and compressed graph-core proofs in SI-04–07 never use fullness of that second projection, so they apply to (SI.34) without that stronger assertion from the faithful concrete case of SI-06. Its top algebra on \(pH\) is \(pMp\): an operator on \(pH\) commuting with all \(y|_{pH}\), extended by zero on \((1-p)H\), commutes with \(N\) and hence belongs to \(M\). The rectangular inverse theorem applies verbatim with \(\xi\in pH\); its finite-vector domain is \(pD_\psi=D_\psi\cap pH\), which is dense in \(pH\).

Use the diagonal weight \(\psi^{\mathrm{opp}}\oplus\varphi_p\). It is faithful even when the second component of (SI.34) has a kernel. The same graph and energy argument gives a positive injective operator \(A_p\) on \(pH\). It is the restriction of SC's operator to that subspace. Indeed its initial coefficients are \(p\theta_\psi(\xi)p\), and the weight there is \(\varphi_p\). The projection \(p\) preserves SC's finite-energy core and removes only its null part: \(e\) acts as the identity on the full form domain, and \(fH\) is the null space. Thus compression of a form-core sequence by \(p\) converges in the restricted form norm. Closed-form uniqueness identifies the two operators.

The first-component argument in SI-08 remains valid and proves

\[
\begin{gathered}
A_p^{it}xA_p^{-it}=\sigma_t^{\varphi_p}(x)\\
(x\in pMp).
\end{gathered}
\tag{SI.35}
\]

\[
\begin{gathered}
A_p^{it}(y|_{pH})A_p^{-it}
=\sigma_{-t}^\psi(y)|_{pH}\\
(y\in N).
\end{gathered}
\tag{SI.36}
\]

In particular the kernel of restriction \(N\to B(pH)\) is invariant under \(\sigma^\psi\). This is proved by (SI.36), not assumed in notation for a weight on a quotient.

The full domain and represented operator are

\[
\begin{gathered}
V_\varphi=D(A_p^{1/2})\oplus fH,\\
D(A_\varphi)=D(A_p)\oplus fH,\\
A_\varphi=A_p\oplus0_{fH}\quad\text{on }eH.
\end{gathered}
\tag{SI.37}
\]

Energy is infinite outside \(eH\). For semifinite \(\varphi\), \(e=1\) and this is the ordinary spatial operator on \(H\). For an arbitrary normal numerator, no operator with an additional zero action on \((1-e)H\) represents that extended energy.

Define \(U_t=A_p^{it}\oplus0\) on \(H=pH\oplus(1-p)H\). Equations (SI.35–36) give the unambiguous full-space identity

\[
\begin{gathered}
U_t\sigma_t^\psi(y)=yU_t,\\
U_t^*U_t=U_tU_t^*=p,\\ U_0=p.
\end{gathered}
\tag{SI.38}
\]

These are unitaries on the effective support, with their specified zero extensions.

## The nonfaithful relative map and its full graph core

Suppose that \(\varphi\) is normal semifinite, and put \(p=s(\varphi)\). We identify the relative map on all of \(H\), including its entire zero part. The initial finite domain and the domain of its closure need not coincide.

Here \(e,f\) denote the two coordinate projections of the original linking algebra in SI-06, rather than the finite and null projections of SI-09. The support \(p\), embedded in the \(ff\) corner, satisfies \(p\leq f\).

Choose an NSF weight \(\tau\) on \((1-p)M(1-p)\), using WH-13, and set

\[
\begin{gathered}
\widehat\varphi(a)=\varphi(pap)\\
{}+\tau((1-p)a(1-p)).
\end{gathered}
\tag{SI.39}
\]

WS-06 makes this NSF on \(M\). Put \(\widehat\rho=\psi^{\mathrm{opp}}\oplus\widehat\varphi\) on the original linking algebra. Its three orthogonal projections are \(e,p,f-p\). On the original \(H\), we write the last projection as \(1-p\). The norm and compression proof in SI-05 applies to this finite orthogonal family: the projections centralize the diagonal weight, their left and right GNS actions commute with its modular operator, and modular conjugation exchanges those actions. No new corner theorem is needed.

**The target, including its null quotient.** Let \(\mathfrak y_\varphi\) consist of \(Y\in eLf\) such that \(\varphi(Y^*Y)<\infty\), and let \(\mathcal Y_\varphi\) be its Hilbert completion modulo the null seminorm, with \(\|[Y]\|^2=\varphi(Y^*Y)\). Support compression gives

\[
\varphi(Y^*Y)
=\varphi((Yp)^*(Yp))
=\widehat\rho((Yp)^*(Yp)).
\]

Faithfulness on \(pMp\) shows that \([Y]=0\) precisely when \(Yp=0\). Consequently

\[
V[Y]=\Lambda_{\widehat\rho}(Yp)
\tag{SI.40}
\]

is a well-defined isometry. Every finite GNS vector in the \(ep\) corner has this form: a rectangular operator \(Z=eZp\) with finite \(\widehat\rho(Z^*Z)\) is itself an admissible \(Y\). The range is therefore dense, and completion makes \(V\) unitary onto that whole Hilbert corner.

**The exact initial-domain split.** Write

\[
\begin{gathered}
E=E_{\varphi,\psi}\\
=\{\xi\in D_\psi:\\
  \varphi(\theta_\psi(\xi))<\infty\}.
\end{gathered}
\tag{SI.43a}
\]

For every \(a\in M\), the defining equation on \(\Lambda_\psi(\mathfrak n_\psi)\) gives \(R_\psi(a\xi)=aR_\psi(\xi)\); thus \(a\) preserves \(D_\psi\). For \(a=p,1-p\), write \(c_\xi=\theta_\psi(\xi)\). Support compression gives

\[
\begin{gathered}
\varphi(c_{p\xi})=\varphi(c_\xi),\\
\varphi(c_{(1-p)\xi})=0.
\end{gathered}
\tag{SI.43b}
\]

In particular \(pE=E\cap pH\), every vector of \((1-p)D_\psi\) belongs to \(E\), and

\[
\begin{gathered}
E=(E\cap pH)\\
{}\oplus(1-p)D_\psi.
\end{gathered}
\tag{SI.43c}
\]

This is a split of the original domain, rather than just an assertion that \(E\) is dense.

Define the antilinear initial map by

\[
T^0\xi=[R_\psi(\xi)^*],\qquad \xi\in E.
\tag{SI.41}
\]

Its squared norm is exactly \(\varphi(\theta_\psi(\xi))\). Under \(V\), it is the relative Tomita block applied to \(p\xi\), and it vanishes on \((1-p)D_\psi\). We now check both graph cores needed for its closure.

**The supported graph core.** For \(\xi\in E\cap pH\), put \(X=R_\psi(\xi)\), so \(X=pXe\). The rectangular inverse in SI-04 gives

\[
\begin{gathered}
\psi^{\mathrm{opp}}(X^*X)=\|\xi\|^2,\\
\widehat\varphi(XX^*)=\varphi(XX^*),\\
\varphi(XX^*)<\infty.
\end{gathered}
\tag{SI.43d}
\]

Conversely, every \(X=pXe\) satisfying these two finite conditions has, by that inverse, a unique vector \(\xi\in pD_\psi\); its second finite condition puts \(\xi\) in \(E\). Thus \(E\cap pH\) corresponds exactly to the finite-star GNS vectors of the \(pe\) corner. Compressing the full finite-star Tomita core in SI-05 proves that these vectors are a graph core for the closed supported block. Its modulus is \(A_p^{1/2}\): SI-07 identifies the squared modulus with the coefficient form, and SI-09 identifies its supported restriction. Its antilinear polar factor is the restriction of \(J_{\widehat\rho}\) from \(pH\) onto the \(ep\) target corner.

**The zero graph core and the closure.** Faithfulness of \(\psi\) makes \(D_\psi\) dense by SC-03. Since \(1-p\) preserves this domain, \((1-p)D_\psi\) is dense in \((1-p)H\). The zero map on the latter whole space is closed, and its graph norm is the ordinary norm. Its restriction to \((1-p)D_\psi\) therefore has the whole zero map as closure.

Take the direct sum of the closed supported block and that zero map. It is closed: if \(\xi_n\to\xi\) and the images converge, then bounded projection by \(p\) gives convergence in the supported graph; closedness of that block determines \(p\xi\) and its image. The other component converges in \((1-p)H\). To see that (SI.41) has the whole sum as closure, approximate any supported-domain vector in the supported graph norm by \(E\cap pH\), and approximate its zero component in norm by \((1-p)D_\psi\). Adding the two approximating vectors gives a sequence in \(E\) by (SI.43c). The errors in the two components tend to zero simultaneously. This use of sequences concerns one metric graph approximation and imposes no countability assumption on the algebra or Hilbert space.

Writing the resulting closure as \(T:H\to\mathcal Y_\varphi\), we obtain

\[
\begin{gathered}
VT\xi=J_{\widehat\rho}A_p^{1/2}p\xi,\\
D(T)=D(A_p^{1/2})\\
{}\oplus(1-p)H.
\end{gathered}
\tag{SI.42}
\]

The initial energy identity extends to this whole graph domain. Closed-form uniqueness, or the polar decomposition of the closed supported block, now gives

\[
T^*T=A_p\oplus0_{(1-p)H}=A_\varphi.
\tag{SI.43}
\]

Its polar factor is antiunitary from \(pH\) onto \(\mathcal Y_\varphi\) and zero on \((1-p)H\). The target and initial map are defined without \(\tau\); uniqueness of their graph closure proves independence of that auxiliary choice on the entire domain. Between two auxiliary corner models the unitary is determined by their common vectors \([Y]\).

**A complete matrix calculation.** Let \(H=M_2(\mathbb C)\) with Hilbert–Schmidt norm. Let \(M\) act by left multiplication \(L_a\), and let \(N\) act by right multiplication \(r_a\xi=\xi a\). Set

\[
\begin{gathered}
D=\begin{pmatrix}1&0\\0&4\end{pmatrix},\\
h=\begin{pmatrix}9&0\\0&0\end{pmatrix},\qquad q=E_{11}.
\end{gathered}
\tag{SI.43e}
\]

On positive operators define \(\psi(r_a)=\operatorname{Tr}(Da)\) and \(\varphi(L_a)=\operatorname{Tr}(ha)\). Identify the first GNS map with \(\Lambda_\psi(r_a)=D^{1/2}a\). The defining equation gives \(R_\psi(\xi)=L_{\xi D^{-1/2}}\), so \(\theta_\psi(\xi)=L_{\xi D^{-1}\xi^*}\). All domains here are finite dimensional and hence \(E=H\). Identify the target with \(Hq\) by sending the rectangular operator \(L_b\) to \(bh^{1/2}\). Then

\[
\begin{aligned}
T\xi&=D^{-1/2}\xi^*h^{1/2},\\
|T|\xi&=h^{1/2}\xi D^{-1/2},\\
A_\varphi\xi&=h\xi D^{-1}.
\end{aligned}
\tag{SI.43f}
\]

Thus the four eigenvalues of \(A_\varphi\), on \(E_{11},E_{12},E_{21},E_{22}\), are \(9,9/4,0,0\); the corresponding values of \(|T|\) are \(3,3/2,0,0\). The squared energy is \(9|\xi_{11}|^2+(9/4)|\xi_{12}|^2\). The support is the first-row space \(qH\), the kernel is the second-row space \((1-q)H\), and the target is the first-column space \(Hq\). The polar factor on the support is \(\xi\mapsto\xi^*\). This calculation also distinguishes the derivative \(T^*T\) from its square root \(|T|\), in the convention of SI-01.

**A proper initial domain whose closure gains every zero direction.** On \(H=\ell^2(\mathbb N)\), let \(M=N=\ell^\infty(\mathbb N)\) act diagonally, with indices starting at \(1\). Put

\[
\begin{gathered}
\psi(a)=\sum_{n\geq1}4^{-n}a_n,\\
\varphi(a)=a_1\quad(a\geq0).
\end{gathered}
\tag{SI.43g}
\]

The denominator is faithful and finite. Its GNS coordinates are \(\Lambda_\psi(a)_n=2^{-n}a_n\); hence \(R_\psi(\xi)\) is multiplication by \((2^n\xi_n)_n\). Therefore

\[
\begin{gathered}
D_\psi=E=\{\xi\in\ell^2:\\
\sup_n2^n|\xi_n|<\infty\},\\
T^0\xi=2\overline{\xi_1},\\
A_\varphi\xi=4\xi_1\delta_1.
\end{gathered}
\tag{SI.43h}
\]

The target is \(\mathbb C\). Finite-support vectors belong to \(E\), but the vector with coordinates \(\xi_1=0\), \(\xi_n=1/n\) for \(n\geq2\), lies in the zero-support subspace and outside \(E\). Its finite truncations converge in norm with zero image. The closed map is consequently \(T\xi=2\overline{\xi_1}\) on all of \(H\), with kernel \(\delta_1^\perp\). If instead \(\varphi=0\), the target is zero, the initial domain is still that proper \(D_\psi\), and its closure is the zero map on all of \(H\). No initial-domain vector outside \(D_\psi\) was assumed.

For an arbitrary normal numerator, SI-09 constructs the effective-support block while retaining the original denominator in its diagonal representation. Adjoin the zero domain \(f_\varphi H\); directions outside \(e_\varphi H\) retain infinite energy. This extension is precisely (SI.37), and does not give those infinite directions an additional zero action.

## The opposite-algebra dictionary is an actual unitary

Let \(O=N^{\mathrm{op}}\), writing \(y^{\mathrm{op}}z^{\mathrm{op}}=(zy)^{\mathrm{op}}\), and define \(\upsilon(y^{\mathrm{op}})=\psi(y)\) on positive elements. Reversing products preserves the positive cone and its order, so \(\upsilon\) is NSF. The right \(O\)-action on \(H\) is

\[
\xi\,y^{\mathrm{op}}=y\xi.
\tag{SI.44}
\]

Define its right GNS map by

\[
\Lambda'_\upsilon(a)=J_\upsilon\Lambda_\upsilon(a^*),
\qquad a\in\mathfrak n_\upsilon^*.
\tag{SI.45}
\]

This map is linear. Its right action is

\[
\Lambda'_\upsilon(ab)
=J_\upsilon\pi_\upsilon(b^*)J_\upsilon\Lambda'_\upsilon(a).
\tag{SI.46}
\]

All domains in (SI.46) are legitimate: \(\mathfrak n_\upsilon^*\) is a right ideal.

**Theorem.** There is a unitary \(W:H_\psi\to H_\upsilon\) determined by

\[
W\Lambda_\psi(y)
=\Lambda'_\upsilon(y^{\mathrm{op}})
=J_\upsilon\Lambda_\upsilon((y^*)^{\mathrm{op}}).
\tag{SI.47}
\]

It satisfies

\[
W\pi_\psi(y)W^*
=J_\upsilon\pi_\upsilon((y^*)^{\mathrm{op}})J_\upsilon.
\tag{SI.48}
\]

If the right-module coefficient operator is defined by

\[
L_\upsilon(\xi)\Lambda'_\upsilon(a)=\xi a,
\]

then its bounded-vector domain is exactly \(D_\psi\), and

\[
R_\psi(\xi)=L_\upsilon(\xi)W,
\qquad L_\upsilon(\xi)L_\upsilon(\xi)^*
=\theta_\psi(\xi).
\tag{SI.49}
\]

**Proof.** The map \(C_0\Lambda_\psi(y)=\Lambda_\upsilon((y^*)^{\mathrm{op}})\) is antiunitary: its norm is \(\psi(y^*y)^{1/2}\), its range is dense, and polarization conjugates the inner product. On the finite-star cores it intertwines the two closed involutions. Those cores are transported bijectively with their graph norms, so

\[
C_0S_\psi C_0^{-1}=S_\upsilon,
\qquad C_0J_\psi C_0^{-1}=J_\upsilon.
\tag{SI.50}
\]

The second identity follows from antilinear polar uniqueness and real spectral transport. Set \(W=J_\upsilon C_0=C_0J_\psi\). This is unitary and gives (SI.47). On GNS vectors,
\(C_0\pi_\psi(y)C_0^{-1}=\pi_\upsilon((y^*)^{\mathrm{op}})\), which gives (SI.48). The bounded-vector norms and operator identities in (SI.49) now follow directly from (SI.44), (SI.47).

There is also exact agreement of the standard corner weight. If \(b\in B_+\), write \(b=J_\psi\pi_\psi(y)J_\psi\) for \(y\in N_+\). Then

\[
WbW^*=\pi_\upsilon(y^{\mathrm{op}}),
\qquad \chi(b)=\psi(y)=\upsilon(y^{\mathrm{op}}).
\tag{SI.51}
\]

For an arbitrary \(b\in\mathfrak n_\chi\), let \(\Gamma(b)=\eta\). SI-02's bounded-vector identity gives \(J_\psi\eta=\Lambda_\psi(z)\), where \(\pi_\psi(z)=J_\psi bJ_\psi\). Consequently

\[
W\Gamma(b)=\Lambda_\upsilon((z^*)^{\mathrm{op}}),
\quad WbW^*=\pi_\upsilon((z^*)^{\mathrm{op}}).
\tag{SI.52}
\]

Thus (SI.51) transports the full GNS map as well as the weight. ∎

Conjugation by \(W\oplus I_H\) carries the entire linking algebra of SI-06, its diagonal weight, the first GNS column and its finite rectangular ideal to the source's right-\(O\)-module linking construction. Equations (SI.49), (SI.52) transport the inverse rectangular GNS map. The corresponding GNS unitary sends each finite-star vector to the same algebra element in the transported triple, so it intertwines the closed Tomita maps and their graph cores. This proves equality of the relative constructions themselves. It does not rely solely on equality of two coefficient expressions.

## Ordinary relative GNS maps are a specialization

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

## Reversing the two corners proves reciprocity

We first justify a corner identification that prevents a hidden unitary ambiguity. In SI-05, suppose \(e,f\) both have central support \(1\) in \(L\). Represent \(L\) on its first GNS column. That representation is faithful: if \(a\) annihilates the column, then \(axu=0\) for every \(x\in L\) and every finite \(u\in eLe\), by faithfulness of the GNS map. Finite positive cutoffs \(u\uparrow e\) give \(axe=0\). Full central support then gives \(a=0\).

Here and below the last use of full central support can be verified by an explicit net. The projection onto the closed span of \(Le\) applied to the original representation space commutes with \(L\) and \(L'\); it is the central support of \(e\). For finite sums \(b=\sum_k x_k e x_k^*\), the contractions \(b(1+b)^{-1}\), indexed by increasing positive sums and positive scalar multiples, increase to that projection. Each is again a finite sum \(\sum_k v_k e v_k^*\). When the central support is \(1\), normality transports this increasing net to \(1\) in any normal unital representation. Thus the closed span of \(L H_{ee}\) is the entire first column.

The commutant of the first-column representation is

\[
Q_e\pi_\rho(L)'Q_e
=\{J_\rho\pi_\rho(b)J_\rho|_{Q_eH_\rho}:b\in eLe\}.
\tag{SI.56}
\]

Indeed any operator on that column commuting with the left action extends by zero on the other column to an operator commuting with \(\pi_\rho(L)\). MF then gives the displayed description. Its restriction to \(H_{ee}\) is faithful and is precisely the opposite action of \(eLe\). Every bounded intertwiner for this right action from \(H_{ee}\) to \(H_{fe}\), extended as one block on the column, commutes with (SI.56). The bicommutant theorem and the faithful normal image theorem therefore identify it with left multiplication by a unique element of \(fLe\).

The right action remains faithful when restricted to \(H_{fe}\). Indeed full central support of \(f\), using the same positive net with \(f\) in place of \(e\), gives \(\overline{LH_{fe}}=Q_eH_\rho\). A right multiplier vanishing on \(H_{fe}\) commutes with the left action and therefore vanishes on this whole column. Its faithful restriction to \(H_{ee}\) then forces its corner element to be zero. Exchanging \(e,f\) proves the corresponding assertion on the other off-diagonal corner.

Consequently the original algebra \(L\), represented on that column, is exactly the linking algebra obtained from the right \(eLe\)-action on \(H_{fe}\). The denominator on its commutant is \(\alpha^{\mathrm{opp}}\), with standard GNS space \(H_{ee}\). SI-02 gives its opposite weight \(\alpha\). Applying the finite rectangular correspondence constructs an intertwining unitary between the two column descriptions. On \(H_{ee}\) it is the canonical double-opposite GNS identification, hence the identity by (SI.5) and WH's reconstruction. It is therefore the identity on the dense span \(LH_{ee}\), and on the whole column. We have proved the literal equality

\[
\frac{d\beta}{d\alpha^{\mathrm{opp}}}
=\Delta_\rho|_{H_{fe}},
\qquad
\frac{d\alpha}{d\beta^{\mathrm{opp}}}
=\Delta_\rho|_{H_{ef}},
\tag{SI.57}
\]

where each corner weight and opposite weight acts through the specified left and right corner representations. The second equality follows by exchanging \(e,f\). This is a theorem about those actual representations, not an assertion that any abstract isomorphism of the corners preserves the weights.

**Reciprocity theorem.** If \(\varphi\) and \(\psi\) are both NSF on \(M\) and \(N\), respectively, then

\[
\frac{d\psi}{d\varphi}=A^{-1},
\qquad A=\frac{d\varphi}{d\psi},
\tag{SI.58}
\]

on the original \(H\). The domains are

\[
D(A^{-1})=\operatorname{ran}A,
\qquad D(A^{-1/2})=\operatorname{ran}A^{1/2}.
\tag{SI.59}
\]

Neither range is required to be all of \(H\).

**Proof.** Use the faithful linking construction of SI-06 and its antiunitary \(C=J_\rho|_{H_{fe}}\). Formula (SI.32) transports the positive algebra \(N\) to the left \(B=eLe\)-action on \(H_{ef}\): for \(y\geq0\), the corresponding element is \(b=J_\psi\pi_\psi(y)J_\psi\), and \(\chi(b)=\psi(y)\) by SI-02. Thus \(C\) transports the numerator \(\psi\) to \(\chi\).

Formula (SI.33) transports \(M\) to the right \(fLf\)-action on \(H_{ef}\). On the \(ff\) standard corner, this is \(x\mapsto J_\varphi\pi_\varphi(x)J_\varphi\) for positive \(x\). SI-02 says its weight is \(\varphi^{\mathrm{opp}}\). Faithfulness of the full-corner identifications in (SI.56) makes this the same transported weight on the commutant acting on \(H_{ef}\). Therefore SI-03 and the second formula of (SI.57) give

\[
C\left(\frac{d\psi}{d\varphi}\right)C^{-1}
=\Delta_\rho|_{H_{ef}}.
\]

TC and real spectral transport give \(J_\rho\Delta_\rho J_\rho=\Delta_\rho^{-1}\). Restricting to the exchanged corners yields

\[
\Delta_\rho|_{H_{ef}}=C A^{-1}C^{-1}.
\]

Cancel \(C\) to obtain (SI.58). The exact spectral domain of the reciprocal function is the range of \(A\); similarly its square-root domain is the range of \(A^{1/2}\), by SK-07. Injectivity makes these inverses single-valued, and the ranges are dense because the kernels are zero. ∎

For a nonfaithful numerator, it is not an NSF reference weight on \(M\), so the full-space swapped expression in (SI.58) is not among the defined derivatives. The supported inverse of \(A_p\) exists, but identifying a reversed weight on a quotient requires specifying that quotient and its weight. We have not suppressed those requirements.

## The balanced-matrix cocycle is independent of the reference

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

## Increasing weights and the automorphism topology

Suppose \(\varphi_i\) is an increasing net of NSF weights and \(\varphi=\sup_i\varphi_i\) is semifinite. It is faithful because it dominates any one \(\varphi_i\). Fix \(\psi\), and put \(A_i=d\varphi_i/d\psi\), \(A=d\varphi/d\psi\). SS-09 and QF-08 give

\[
A_i^{it}\xi\longrightarrow A^{it}\xi
\quad\text{uniformly for }t\text{ in compact real intervals}
\tag{SI.67}
\]

for every \(\xi\in H\); the same is true with \(-t\). For a general directed set, one may first restrict to the cofinal tail above one fixed index, as in QF-08.

**Corollary.** The modular automorphisms converge uniformly on compact time intervals in the topology of pointwise norm convergence on the predual:

\[
\sup_{|t|\leq T}
\|\omega\circ\sigma_t^{\varphi_i}
       -\omega\circ\sigma_t^\varphi\|\longrightarrow0
\quad(\omega\in M_*,\ T<\infty).
\tag{SI.68}
\]

The same assertion holds for their inverses.

**Proof.** For vectors \(\xi,\eta\), let \(\omega_{\xi,\eta}(x)=\langle x\xi,\eta\rangle\). On the unit ball of \(M\), conjugation by unitaries \(V_i,V\) gives

\[
\begin{split}
\|\omega_{\xi,\eta}\circ\operatorname{Ad}V_i
 -\omega_{\xi,\eta}\circ\operatorname{Ad}V\|
\leq{}&\|(V_i^*-V^*)\xi\|\,\|\eta\|\\
&+\|\xi\|\,\|(V_i^*-V^*)\eta\|.
\end{split}
\tag{SI.69}
\]

Every normal functional in the given concrete representation is an absolutely summable vector-pair series, by CP. More explicitly its vector families can be chosen with finite sums of squared norms, so the sum of the products of their norms is finite by Cauchy–Schwarz. Truncate that series. Formula (SI.69) and (SI.67) make the finite part tend to zero uniformly on the compact time interval. The remaining part is uniformly at most twice the sum of its vector-norm products, independently of \(i,t\), because automorphisms are isometries. First choose the truncation and then \(i\) to prove (SI.68). Formula (SI.28) identifies these conjugations with the modular automorphisms. Replacing \(t\) by \(-t\) proves the inverse assertion. ∎

This supplies the modular-automorphism consequence of the source's increasing-sequence corollary, with its semifinite limit hypothesis retained and a directed-net version. A nonsemifinite supremum has only the generalized form/resolvent conclusion of SS; this argument does not assign it an ordinary faithful modular group on \(M\).

## A block model with both time directions visible

Let \(I\) be any set. On

\[
H=\bigoplus_{i\in I}\mathrm{HS}(\mathbb C^2),
\]

let \(M=\prod_iM_2(\mathbb C)\) act on the left. Its commutant consists of bounded right multipliers \(R_y(\xi)_i=\xi_i y_i\); their multiplication is \(R_yR_z=R_{zy}\). Fix positive invertible two-by-two matrices \(a_i,b_i\), without any uniform lower or upper bound, and define

\[
\varphi(x)=\sum_i\operatorname{Tr}(a_i x_i),
\qquad
\psi(R_y)=\sum_i\operatorname{Tr}(b_i y_i)
\quad(x,y\geq0).
\tag{SI.70}
\]

Both weights are NSF. Normality follows by interchanging the supremum over finite subsets with increasing positive suprema. Faithfulness holds in each coordinate. Finite-coordinate identity projections have finite weight and increase to one, proving semifiniteness without a countable cofinal family.

The denominator GNS map can be realized coordinatewise as

\[
\Lambda_\psi(R_y)_i=b_i^{1/2}y_i.
\]

Indeed \(R_y^*R_y=R_{yy^*}\), and the squared Hilbert–Schmidt norm is \(\operatorname{Tr}(b_i yy^*)\). Its representation is right multiplication. Thus

\[
D_\psi
=\left\{\xi\in H:\sup_i\|\xi_i b_i^{-1/2}\|<\infty\right\},
\qquad
R_\psi(\xi)\eta=(\xi_i b_i^{-1/2}\eta_i)_i.
\tag{SI.71}
\]

The converse in this criterion follows by testing vectors supported at a single coordinate; the uniform bound gives its forward direction on the entire Hilbert sum. Its coefficient is left multiplication by \(\xi_i b_i^{-1}\xi_i^*\). Hence the closed energy and operator are

\[
q[\xi]=\sum_i\|a_i^{1/2}\xi_i b_i^{-1/2}\|_{\mathrm{HS}}^2,
\tag{SI.72}
\]

\[
A\xi=(a_i\xi_i b_i^{-1})_i,
\qquad
D(A)=\left\{\xi\in H:\sum_i\|a_i\xi_i b_i^{-1}\|_{\mathrm{HS}}^2<\infty\right\}.
\tag{SI.73}
\]

The form domain is exactly the finite-energy set in (SI.72). To verify closure and these domains directly, diagonalize \(a_i\) and \(b_i\) separately in each finite matrix block. The resulting matrix-unit basis has positive spectral coefficients \(\alpha_{ir}/\beta_{is}\). Coordinate spectral calculus gives (SI.72–73). Truncation to finitely many coordinates and spectral coefficients in a finite interval gives graph approximation; all resulting vectors are in (SI.71). Each fixed vector has summable tails, so this requires no countability assumption on \(I\).

Its imaginary powers are

\[
A^{it}\xi=(a_i^{it}\xi_i b_i^{-it})_i.
\tag{SI.74}
\]

Consequently the numerator action is \(x_i\mapsto a_i^{it}x_i a_i^{-it}\), whereas the denominator's own modular action is

\[
\sigma_t^\psi(R_y)=R_{(b_i^{-it}y_i b_i^{it})_i}.
\tag{SI.75}
\]

Conjugating \(R_y\) by (SI.74) gives (SI.75) at \(-t\), as required. For a concrete example take \(I=K_0\times\mathbb N\), where \(K_0\) is any nonempty set, and set \(a_{k,n}=\operatorname{diag}(1,e^n)\), \(b_{k,n}=\operatorname{diag}(e^{2n},1)\). The four spectral coefficients are \(e^{-2n},1,e^{-n},e^n\). They show that both \(A\) and \(A^{-1}\) have proper domains, while the left and right modular frequencies are \(n\) and \(2n\). No commutation between \(a_i\) and \(b_i\) as two matrices is needed: they act on different sides of the Hilbert–Schmidt vector.

## Problems with complete solutions

**1. A reciprocal can have a proper domain.** Take \(I=\mathbb N\), \(a_n=I_2\), \(b_n=n^2I_2\) in SI-16. Compute \(A\), \(A^{-1}\), their square-root domains, and the cocycle for replacing the numerator by \(c\varphi\), \(c>0\).

**Solution.** The operator \(A\) is multiplication by \(n^{-2}\) on the \(n\)-th Hilbert–Schmidt block, so \(D(A)=D(A^{1/2})=H\). It is injective but has no bounded inverse. Its reciprocal is multiplication by \(n^2\), with

\[
D(A^{-1})=\left\{\xi:\sum_n n^4\|\xi_n\|_{\mathrm{HS}}^2<\infty\right\},
\quad
D(A^{-1/2})=\left\{\xi:\sum_n n^2\|\xi_n\|_{\mathrm{HS}}^2<\infty\right\}.
\]

These are respectively \(\operatorname{ran}A\) and \(\operatorname{ran}A^{1/2}\), by solving coordinatewise for a preimage in \(H\). Numerator scaling gives \(cA\), so the cocycle is \((cA)^{it}A^{-it}=c^{it}I\). The constant weight scale changes the spatial operator but cancels from the modular automorphism group.

**2. Why the relative conjugation need not act on the original space.** Let \(M=B(\mathbb C^2)\) act on \(H=\mathbb C^2\), so \(N=\mathbb CI\). Can an antiunitary \(J:H\to H\) satisfy \(JMJ=N\)? Explain what (SI.25) provides instead.

**Solution.** Conjugation by any antiunitary bijects \(B(H)\) onto \(B(H)\): its inverse transports every bounded operator back to one on \(H\). Thus \(JMJ=B(H)\ne\mathbb CI\). The relative polar factor instead maps \(H_{fe}\) antiunitarily onto the different Hilbert corner \(H_{ef}\). It exchanges the left \(M\)-action with that corner's right \(M\)-action and the \(N\)-action with the appropriate left standard-corner action. Equations (SI.32–33) express these assertions without claiming the impossible identity on \(H\).

**3. Zero energy and infinite energy are different directions.** On \(H=\mathbb C^3\), take \(M=N=\mathbb C^3\), let \(\psi(y)=y_1+2y_2+3y_3\), and define \(\varphi(x)=5x_1+0x_2+\infty x_3\), with \(0\cdot\infty=0\). Determine the relative support and imaginary powers.

**Solution.** This is a normal weight. Its finite projection is \(e=\operatorname{diag}(1,1,0)\), its null projection is \(f=\operatorname{diag}(0,1,0)\), and its effective support is \(p=\operatorname{diag}(1,0,0)\). Coordinate coefficients give energy \(5|\xi_1|^2\) when \(\xi_3=0\), and infinity otherwise. The represented operator on \(eH\) is \(\operatorname{diag}(5,0)\); its faithful supported block is \(A_p=5I_{pH}\). Hence \(U_t=\operatorname{diag}(5^{it},0,0)\), with \(U_0=p\). The modular actions of \(\varphi_p\) on \(pMp\) and of \(\psi\) on \(N\) are trivial, so (SI.38) holds by commutation. Extending the represented operator by zero to the third coordinate would incorrectly make its energy finite there.

**4. Check the antiunitary sign rather than guessing it.** On two-by-two Hilbert–Schmidt matrices let \(A\xi=a\xi b^{-1}\), with \(a,b>0\), and let \(C\xi=\xi^*\). Compute \(CAC^{-1}\), \(CA^{it}C^{-1}\), and \(CA^{-1}C^{-1}\).

**Solution.** The adjoint reverses the two multiplication sides, so

\[
(CAC^{-1})\eta=b^{-1}\eta a,
\qquad
CA^{it}C^{-1}\eta=b^{it}\eta a^{-it}.
\]

The latter is \((CAC^{-1})^{-it}\eta\), displaying the scalar conjugation in (SI.8). The reciprocal transforms as

\[
CA^{-1}C^{-1}\eta=b\eta a^{-1},
\]

which is the reversed-corner modular operator. In an infinite block sum the same formulas hold with exactly the transported square-summability domains; finite-dimensional computations alone do not remove those domains.

**5. A cocycle is not usually a unitary group.** On \(M_2(\mathbb C)\), take faithful weights with densities \(h_1,h_2>0\). Show that \(u_t=h_2^{it}h_1^{-it}\) obeys the cocycle law, and explain why it need not obey \(u_{s+t}=u_su_t\).

**Solution.** The reference modular action is \(\sigma_s^{\varphi_1}(x)=h_1^{is}xh_1^{-is}\). Thus

\[
u_s\sigma_s^{\varphi_1}(u_t)
=h_2^{is}h_1^{-is}h_1^{is}h_2^{it}h_1^{-it}h_1^{-is}
=h_2^{i(s+t)}h_1^{-i(s+t)}.
\]

The untwisted product has the middle factors \(h_1^{-is}h_2^{it}\), which cannot generally be interchanged. For a concrete obstruction take \(h_1=e^X,h_2=e^Y\) for noncommuting self-adjoint matrices \(X,Y\), for example \(X=\operatorname{diag}(1,-1)\) and \(Y=\begin{pmatrix}0&1\\1&0\end{pmatrix}\). If \(u_t\) were a differentiable unitary group, its derivative at zero would force \(u_t=e^{it(Y-X)}\). Its second derivative from the product is \(-Y^2-X^2+2YX\), whereas the proposed exponential has second derivative \(-Y^2-X^2+YX+XY\). Equality would require \(YX=XY\), contrary to the chosen matrices. Thus this example satisfies the cocycle identity but not the group identity.

## What is identified and what remains separate

The direct coefficient construction is now identified with the actual closed rectangular relative map, including the inverse finite-intertwiner map, the linking GNS column, the supported zero part and the full graph core. The ordinary two-weight GNS construction is its matrix specialization. The source's right-module convention is transported by the explicit unitary (SI.47), including both the corner weight and its GNS map. The derivative is \(T^*T\), with square root \(|T|\), as the source's energy statement requires.

For every normal semifinite numerator, the source's support, numerator modular action, negative-time commutant action and square-root core follow with their full hypotheses. Reciprocity holds when both weights are NSF. The balanced-matrix cocycle has the spatial product formula, is independent of the commutant reference, and satisfies its stated cocycle and implementation laws. The increasing-weight result now includes the predual topology of the modular automorphisms. For arbitrary normal numerators, the additional finite-domain/null-domain distinction is (SI.37); the source's ordinary operator is not asserted on infinite-energy directions.

The construction shares the source's mathematical use of a diagonal linking weight and its four Hilbert corners. Its proof organization and details are independently written, with the opposite-weight criterion and direct closed-form uniqueness making the interfaces explicit. No source proof expression is imported. The unit does not establish the full weight KMS characterization, inverse-cocycle reconstruction, the operator-to-weight converse of IX.3.11, a prescribed common natural-cone realization, or the remaining relative-tensor-product theory. Those are separate assertions, not consequences of adopting the same symbols.
