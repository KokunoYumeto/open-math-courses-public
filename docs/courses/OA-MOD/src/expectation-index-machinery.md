# Expectation index and the basic construction

The commutant dual of an expectation produces a scalar index. We prove that this scalar is independent of the faithful normal representation, construct the basic expectation and iterate it to obtain the Jones relations. The spatial-form compression argument keeps the bounded-vector domains and completed form cores explicit. Zorn's lemma is used for arbitrary projection families.

Let \(N\subseteq M\subseteq B(H)\) be a unital inclusion of nonzero factors, represented faithfully and normally. Let \(E:M\to N\) be a **faithful normal** conditional expectation. These hypotheses place \(E\) in the faithful normal semifinite operator-valued-weight class: its value at every bounded positive is bounded. The commutant-duality theorem OD01–04 supplies
\[
 E':N'_+\longrightarrow\widehat{M'}_+.
\tag{EI.1}
\]
Initially this is a map on positive elements with extended-positive values. It must not be applied to arbitrary complex elements before its finite domain has been established.

## The value at the identity is scalar, including infinity

Put \(h=E'(1)\). For every unitary \(u\in M'\), operator-valued covariance gives
\[
 u^*hu=E'(u^*u)=E'(1)=h.
\tag{EI.2}
\]
Use the unique spectral-form representation and canonical bounded truncations \(h_k\) of CW02. Unitary invariance of the extended positive preserves its finite-energy space and closed form. Uniqueness of the representing operator therefore gives \(u^*h_ku=h_k\). Thus \(h_k\), already in \(M'\), commutes with every unitary of \(M'\). The bounded unitary test gives
\[
 h_k\in Z(M')=M'\cap M''=Z(M)=\mathbb C1.
\tag{EI.3}
\]
Write \(h_k=c_k1\). These scalars are nonnegative and increasing. Evaluation on any normal positive functional, followed by CW02, proves
\[
 E'(1)=\kappa1,\qquad \kappa=\sup_k c_k\in(0,\infty].
\tag{EI.4}
\]
Here \(\infty1\) means the extended positive taking infinity at every nonzero normal positive functional and zero at the zero functional. The value \(\kappa=0\) is excluded by faithfulness of \(E'\), since it would give \(E'(1)=0\) in a nonzero algebra. This argument needs neither sigma-finiteness nor a finite trace. It establishes scalarity in the given representation; EI09 proves independence of that representation.

## Scaling the spatial derivative and the dual

We first justify the scale, including the form domain. For faithful normal semifinite scalar weights \(\alpha\) and \(\beta\) on opposite commutants and \(a,b>0\),
\[
 \frac{d(a\alpha)}{d(b\beta)}=\frac ab\frac{d\alpha}{d\beta}.
\tag{EI.5}
\]
For the numerator, the defining bounded-vector energy is multiplied by \(a\). For the denominator, the unitary from the GNS space of \(b\beta\) to that of \(\beta\) is
\[
 U\Lambda_{b\beta}(x)=\sqrt b\,\Lambda_\beta(x).
\tag{EI.6}
\]
Indeed both squared norms equal \(b\beta(x^*x)\), and the two dense GNS ranges give surjectivity. If \(R_\beta(\xi)\Lambda_\beta(x)=x\xi\), then
\[
 R_{b\beta}(\xi)U^{-1}=b^{-1/2}R_\beta(\xi).
\tag{EI.7}
\]
The bounded-vector domains agree, and their coefficient operators satisfy
\(\theta_{b\beta}(\xi,\xi)=b^{-1}\theta_\beta(\xi,\xi)\).
The original energies are consequently multiplied by \(a/b\). Their finite-energy domains agree, their form norms are equivalent, and completing the common core in SC07 gives exactly the scaled closed form. Uniqueness in SC09 gives the displayed operator identity, with the same operator and square-root domains under this positive finite scaling.

For a faithful normal semifinite operator-valued weight \(T:M\to N\), this implies
\[
 (aT)'=a^{-1}T'.
\tag{EI.8}
\]
To prove it, test the candidate on arbitrary scalar references \(\varphi\) on \(N\) and \(\psi\) on \(M'\). OD01–03 and the scalar scaling identity give
\[
 \frac{d\varphi}{d(\psi\circ(a^{-1}T'))}
 =a\frac{d\varphi}{d(\psi\circ T')}
 =a\frac{d(\varphi\circ T)}{d\psi}
 =\frac{d(\varphi\circ(aT))}{d\psi}.
\tag{EI.9}
\]
Multiplication by a positive finite scalar preserves normality, faithfulness and the finite ideal. The uniqueness clause of commutant duality therefore identifies the candidate with \((aT)'\).

## Finite scalar value gives a normal dual expectation

Suppose \(\kappa<\infty\). For \(x\in N'_+\), monotonicity gives
\[
 0\leq E'(x)\leq\|x\|\kappa1.
\tag{EI.10}
\]
By CW02 this extended positive is bounded. In particular the finite ideal of \(E'\) is all of \(N'\). The real-difference and polarization construction in OVW01 extends \(E'\) uniquely to a complex-linear map \(N'\to M'\). It is normal, faithful and \(M'\)-bimodular. Define
\[
 F=\kappa^{-1}E':N'\longrightarrow M'.
\tag{EI.11}
\]
Covariance at the identity gives \(E'(a)=\kappa a\) for positive \(a\in M'\), and hence for every \(a\in M'\) by linearity. Therefore \(F\) is unital, fixes \(M'\), is idempotent and has range \(M'\).

For clarity, complete positivity follows from the finite-domain Gram-matrix proof in OVW01: each matrix \([F(z_i^*z_j)]\) is positive. An arbitrary positive matrix over \(N'\) is the square of its positive square root and hence is a sum of such Gram matrices, one per row of the square root. Applying \(F\) entrywise preserves positivity. Applying its two-by-two amplification to the Gram matrix of \((x,1)\) gives \(F(x)^*F(x)\leq F(x^*x)\). Since \(F(x^*x)\leq\|x\|^2 1\), the map is contractive. Thus \(F\) is a faithful normal conditional expectation.

The scaling formula in EI02 and OD04 give an exact identity of operator-valued weights on the double commutant inclusion:
\[
 F'=\kappa(E')'=\kappa E.
\tag{EI.12}
\]
In particular \(F'(1)=\kappa1\). The normalized expectation on the reversed commutant inclusion has the same scalar value of its dual. No change of Hilbert-space representation is used in this assertion.

## Transport through an antiunitary requires a map on both sides

Assume \(J\) is an antiunitary involution on \(H\) such that \(JMJ=M'\), and put
\[
 M_1=(JNJ)'=JN'J.
\tag{EI.13}
\]
There are linear star anti-isomorphisms
\[
 j_1:M_1\to N',\quad j_1(x)=Jx^*J,
 \qquad
 j_0:M'\to M,\quad j_0(y)=Jy^*J.
\tag{EI.14}
\]
Conjugation by \(J\) is conjugate-linear and multiplicative, while taking the adjoint is conjugate-linear and reverses products; their composition gives precisely these assertions. Involutivity supplies the inverse maps. Both preserve positivity and increasing positive suprema, which can also be checked on vectors.

For finite \(\kappa\), define the correctly typed map
\[
 \widehat E= j_0\circ E'\circ j_1:M_1\to M,
 \qquad
 E_1=\kappa^{-1}\widehat E.
\tag{EI.15}
\]
It is positive, normal and faithful. If \(a,b\in M\) and \(x\in M_1\), the two reversals of order give
\[
 \widehat E(axb)=a\widehat E(x)b.
\tag{EI.16}
\]
Indeed \(j_1(axb)=j_1(b)j_1(x)j_1(a)\), the outside factors lie in \(M'\), and \(j_0\) reverses their order again. Also \(\widehat E(a)=\kappa a\) for \(a\in M\). Thus \(E_1\) is a normal positive unital \(M\)-bimodule projection. The same Gram-matrix argument as in EI03, using its bimodule covariance and positivity, proves complete positivity and contractivity. This is a faithful normal conditional expectation onto \(M\).

On positive inputs the formula can be written
\[
 \widehat E(x)=J E'(JxJ)J.
\tag{EI.17}
\]
On arbitrary inputs the fully typed linear formula is \(j_0(E'(j_1(x)))\). Merely writing \(E'(Jx^*J)\) leaves the result in \(M'\) and omits the return map to \(M\). Before finite \(\kappa\) is assumed, the same transport is defined on the positive cone with extended-positive values, not on every complex input.

## The Jones projection belongs to both relevant commutants

Suppose \(N\) has a faithful normal state \(\varphi\), put \(\psi=\varphi E\), and use the faithful GNS representation of \(M\) on \(H_\psi\). Let \(\Omega=\Lambda_\psi(1)\), and let \(e\) project onto \(K=\overline{N\Omega}\). The vector \(\Omega\) is cyclic and separating for \(M\). The subspace \(K\) is invariant under \(N\) and its adjoints, so
\[
 e\in N'.
\tag{EI.18}
\]
In particular the expression \(E'(e)\) **is** typed in this representation. This follows directly from the reducing-subspace argument.

For \(x\in M\) and \(n\in N\), preservation and bimodularity give
\[
 \langle x\Omega,n\Omega\rangle=\psi(n^*x)
 =\varphi(n^*E(x))=\langle E(x)\Omega,n\Omega\rangle.
\tag{EI.19}
\]
Consequently
\[
 e x\Omega=E(x)\Omega,\qquad e x e=E(x)e.
\tag{EI.20}
\]
The second identity follows first on the dense vectors \(n\Omega\) in \(K\), using \(E(xn)=E(x)n\); both sides vanish on \(K^\perp\).

Writing \(S_0x\Omega=x^*\Omega\), the same formula gives \(eS_0=S_0e\) on the full Tomita core \(M\Omega\). Both \(e\) and \(1-e\) preserve that core. Projecting graph approximations therefore gives reduction of the closed \(S\). The adjoint-domain argument and polar decomposition in ME09 then give
\[
 eJ=Je,\qquad e\Delta^{it}=\Delta^{it}e,
\tag{EI.21}
\]
including reduction of all real power domains. In particular \(JeJ=e\).

We now identify the algebra generated by \(M\) and \(e\). If \(x\in M\) commutes with \(e\), then
\(x\Omega=e x\Omega=E(x)\Omega\), because \(e\Omega=\Omega\). Separation by \(\Omega\) gives \(x=E(x)\in N\). The converse follows from \(e\in N'\). Thus \(M\cap\{e\}'=N\). Using \(M'=JMJ\) and \(JeJ=e\),
\[
 \{M,e\}'=M'\cap\{e\}'=J N J.
\tag{EI.22}
\]
The bicommutant theorem proves
\[
 \{M,e\}''=(JNJ)'=M_1.
\tag{EI.23}
\]
This construction does not assume that the index is finite.

## The dual takes the Jones projection to the identity

Let \(\psi'\) be the vector state of \(\Omega\) on \(M'\). To check the fixed-vector fact used here, \(S\Omega=\Omega\), and the adjoint pairing on the core gives
\[
\langle Sx\Omega,\Omega\rangle=\psi(x^*)=\langle\Omega,x\Omega\rangle.
\tag{EI.24}
\]
Thus \(\Omega\in D(S^*)\) with \(S^*\Omega=\Omega\). It follows that \(\Delta\Omega=\Omega\) and \(J\Omega=\Omega\). SI02 now identifies \(\psi'\) with the opposite weight of \(\psi\): its value at \(JaJ\), for positive \(a\in M\), is \(\psi(a)\). Put
\[
 \chi=\psi'\circ E'\quad\hbox{on }N'.
\tag{EI.25}
\]
Composition preserves faithful normal semifinite weights by OVW04. OD01, SI12 and reciprocity SI13 give exact positive self-adjoint operators on \(H_\psi\):
\[
 \frac{d\varphi}{d\chi}
 =\frac{d\psi}{d\psi'}=\Delta_\psi,
 \qquad
 \frac{d\chi}{d\varphi}=\Delta_\psi^{-1}.
\tag{EI.26}
\]

The map \(V:H_\varphi\to H_\psi\), initially \(V\Lambda_\varphi(n)=n\Omega\), is an isometry onto \(K\), so \(VV^*=e\). For every \(y'\in M'\), the vector \(y'\Omega\) is \(\varphi\)-bounded for the action of \(N\), with
\[
 R_\varphi(y'\Omega)=y'V,
 \qquad \theta_\varphi(y'\Omega,y'\Omega)=y'e y'^*.
\tag{EI.27}
\]
Indeed \(n y'\Omega=y'n\Omega\), and the formula follows on all GNS vectors. The opposite Tomita operator is \(J\Delta_\psi^{-1/2}\), with \(M'\Omega\) as its graph core by SI02. Hence every \(y'\Omega\) belongs to its domain and
\[
 \|\Delta_\psi^{-1/2}y'\Omega\|^2=\|y'^*\Omega\|^2.
\tag{EI.28}
\]
The full bounded-vector energy formula SC07 now yields
\[
 \psi'\bigl(y'E'(e)y'^*\bigr)
 =\chi(y'e y'^*)
 =\|y'^*\Omega\|^2.
\tag{EI.29}
\]
The first expression is interpreted as an extended-positive evaluation; boundedness of \(E'(e)\) has not been assumed.

Let \(q\) be the extended closed form representing \(E'(e)\), as in EI03W02. The last equation says \(q[\eta]=\|\eta\|^2\) on the linear subspace \(M'\Omega\), which is dense because \(\Omega\) is cyclic for \(M'\). This suffices here to identify the entire form: any Hilbert-norm Cauchy sequence from that subspace is also form-norm Cauchy, since the same equality applies to its differences. Closedness therefore places its limit in the finite form domain with the same energy. Every vector is such a limit. Thus
\[
 E'(e)=1,\qquad \widehat E(e)=J E'(e)J=1.
\tag{EI.30}
\]
Since \(0\leq e\leq1\), positivity gives \(1\leq E'(1)=\kappa1\), so \(\kappa\geq1\). If \(\kappa<\infty\), the normalized basic-construction expectation of EI04 satisfies \(E_1(e)=\kappa^{-1}1\).

## Duality respects antiunitary transport

Let \(C:H\to\widetilde H\) be unitary or antiunitary. Transport an operator-valued weight on positive elements by
\[
 T^C(CxC^{-1})=CT(x)C^{-1}.
\tag{EI.31}
\]
For extended positives this means the corresponding transported closed form or, equivalently, its evaluations on transported positive normal functionals. The weight remains faithful, normal and semifinite, with transported finite ideals. SI03 proves transport of the full spatial forms and their operator domains. Applying that theorem to both sides of OD01 shows that \((T')^C\) satisfies the defining spatial identity for the dual of \(T^C\). Uniqueness in OD03 therefore gives
\[
 (T^C)'=(T')^C.
\tag{EI.32}
\]
This proof uses positive operators and their forms. It does not use the incorrect rule that antiunitary conjugation preserves imaginary powers without reversing the sign of time.

Apply the identity to \(T=E'\) and \(C=J\). On positive inputs \((E')^J=\widehat E\), while \((E')'=E\). Combining with EI02 gives
\[
 E_1'=\kappa E^J:M'_+\longrightarrow\widehat{JNJ}_+.
\tag{EI.33}
\]
Here \(JNJ=M_1'\), so the domain and codomain are exactly the commutant inclusion dual to \(E_1:M_1\to M\). Since \(E^J(1)=1\), one obtains \(E_1'(1)=\kappa1\). The basic-construction expectation has the same dual scalar.

## Compressing a spatial derivative: the bounded-vector proof

We need a representation-comparison lemma, not only scalar-reference independence. Let \(A\subseteq B(H)\) be a nonzero factor with commutant \(B=A'\). Fix a nonzero projection \(p\in B\), put \(q=1-p\), and take faithful normal semifinite weights \(\beta_p,\beta_q\) on the two corners. CW06 supplies the block-diagonal weight
\[
 \beta(b)=\beta_p(pbp)+\beta_q(qbq),\qquad b\in B_+.
\tag{EI.34}
\]
The zero complementary corner is allowed. Write \(A_p=A|_{pH}\), and transport a faithful normal semifinite weight \(\alpha\) on \(A\) to \(\alpha_p\) on \(A_p\). We will prove
\[
 p\frac{d\alpha}{d\beta}=\frac{d\alpha}{d\beta}p,
 \qquad
 \left.\frac{d\alpha}{d\beta}\right|_{pH}
 =\frac{d\alpha_p}{d\beta_p},
\tag{EI.35}
\]
where the first equality denotes reduction, including the domains.

First justify faithfulness of the compression. The projection onto \(\overline{BpH}\) commutes with both \(B\) and \(B'\), hence is central in the factor \(B\). It is nonzero, so this closed span is all of \(H\). If \(a\in A\) annihilates \(pH\), it annihilates \(BpH\), since \(a\) commutes with \(B\), and is zero. Compression is therefore a faithful normal representation of \(A\). WH02 gives its von Neumann image. An operator on \(pH\) commuting with this image extends by zero on \(qH\) to an element of \(B\); hence its commutant is exactly \(pBp\).

In the GNS representation \((K_\beta,\pi_\beta,\Lambda_\beta)\), right multiplication by \(p\) defines an orthogonal projection \(P_r\). In fact block diagonality gives
\[
 \|\Lambda_\beta(b)\|^2
 =\|\Lambda_\beta(bp)\|^2+\|\Lambda_\beta(bq)\|^2
 \quad(b\in\mathfrak n_\beta).
\tag{EI.36}
\]
Thus both right multiplications extend as complementary contractive projections, and hence are orthogonal. They commute with the left representation of \(B\). The corner GNS space identifies isometrically with
\[
 K_p=\pi_\beta(p)P_rK_\beta,
 \qquad \Lambda_{\beta_p}(b)\longmapsto\Lambda_\beta(b).
\tag{EI.37}
\]
The range is all of \(K_p\), since projecting the dense GNS vectors gives \(\Lambda_\beta(pbp)\), precisely the corner finite-domain vectors.

The bounded-vector domains have the exact relation
\[
 D_\beta(H)\cap pH=D_{\beta_p}(pH).
\tag{EI.38}
\]
One inclusion follows by restriction. If \(\xi\in D_\beta\cap pH\), then \(R_\beta(\xi)=R_\beta(\xi)P_r\). Its restriction \(S\) to \(K_p\) is the corner coefficient map. Intertwining the left actions gives
\[
 SS^*=\left.R_\beta(\xi)R_\beta(\xi)^*\right|_{pH}.
\tag{EI.39}
\]

For the converse we give the bounded extension, including its norm. Choose partial isometries \((v_i)_{i\in I}\) in \(B\), with \(v_0=p\), initial projections at most \(p\), mutually orthogonal final projections, and
\[
 \sum_i v_iv_i^*=1\quad\hbox{strongly}.
\tag{EI.40}
\]
Such a family follows from Zorn's lemma and BK07. A maximal family could not leave a nonzero complementary projection \(r\): the density of \(BpH\) gives a nonzero \(rbp\), whose polar part supplies another partial isometry with final projection under \(r\) and initial projection under \(p\). No countability is required.

Let \(\xi\in D_{\beta_p}(pH)\), and let \(S:K_p\to pH\) be its coefficient map. For \(\zeta\in K_\beta\), define
\[
 R\zeta=\sum_i v_i S\pi_\beta(v_i^*)P_r\zeta.
\tag{EI.41}
\]
Each input to \(S\) lies in \(K_p\). The output summands have orthogonal ranges. Since \(S\) intertwines \(pBp\), its value on the \(i\)-th input is in the initial space of \(v_i\). Therefore
\[
 \|R\zeta\|^2
 \leq\|S\|^2\sum_i\|\pi_\beta(v_i^*)P_r\zeta\|^2
 =\|S\|^2\|P_r\zeta\|^2.
\tag{EI.42}
\]
The sums are limits over finite subsets; the displayed estimate proves convergence. For \(b\in\mathfrak n_\beta\), the element \(v_i^*bp\) belongs to the finite left ideal of \(pBp\). Hence
\[
 R\Lambda_\beta(b)
 =\sum_i v_i(v_i^*bp)\xi=b\xi.
\tag{EI.43}
\]
This proves \(\xi\in D_\beta(H)\) and identifies \(R\) with its coefficient map. On \(K_p\), only the \(v_0=p\) summand remains, so its restriction is exactly \(S\). Thus the coefficient restriction identity holds in both directions. Since \(\alpha_p\) is the transported weight, the initial spatial energies on this common corner domain are equal, including infinity.

It remains to verify the closure domains. For arbitrary \(\xi\in D_\beta(H)\),
\[
 R_\beta(p\xi)=R_\beta(\xi)P_r,
 \qquad R_\beta(q\xi)=R_\beta(\xi)(1-P_r).
\tag{EI.44}
\]
Consequently the coefficient cross terms vanish, and the initial energy is the sum of the two corner energies. Both \(p\) and \(q\) preserve the finite-energy core and are contractions for its form norm. Passing to its canonical completion in SC07 proves that the closed form is their orthogonal direct sum. In particular its restriction to \(pH\) is exactly the closure of the common corner core already identified, not a possibly larger closed extension. SC09 then proves the claimed operator equality and reduction of the full operator and square-root domains.

## A two-representation comparison proves independence of the scalar

Take any two faithful normal representations of the abstract inclusion \(N\subseteq M\), on \(H_1\) and \(H_2\). On \(H=H_1\oplus H_2\), represent both algebras diagonally and identify them with \(N,M\). Their commutants
\[
 B=M',\qquad C=N'
\tag{EI.45}
\]
are factors: each commutant has the same center as its double commutant. Let \(p\) project onto either summand. Then \(p\in B\subseteq C\), and both nonzero corners have full central support. The compressed algebras are precisely the original representations, by the corner-commutant argument in EI08.

Write \(T=E':C_+\to\widehat B_+\) for the dual in the direct-sum representation. Its restriction
\[
 T_p:(pCp)_+\to\widehat{pBp}_+
\tag{EI.46}
\]
is well defined, because covariance gives \(T(pxp)=pT(x)p\). It is normal and faithful. It is also semifinite: the finite ideal of \(T\) is a linear left ideal and right \(B\)-module by OVW01, so \(p\mathfrak N_Tp\) lies in the finite ideal of \(T_p\) and is ultraweakly dense in \(pCp\). This verifies the full class required by duality.

Choose a block-diagonal faithful normal semifinite weight \(\rho\) on \(B\), using CW06, and a faithful normal semifinite \(\varphi\) on \(N\). Put \(\chi=\rho T\), which is faithful normal semifinite by OVW04. It too is block diagonal for \(p\): extended-positive evaluation and covariance give, for \(x\in C_+\),
\[
 \chi(x)=\rho_p(T(pxp))+\rho_q(T(qxq))
 =\chi(pxp)+\chi(qxq).
\tag{EI.47}
\]
Its corner weights are \(\chi_p=\rho_pT_p\) and \(\chi_q=\rho_qT_q\); these are faithful normal semifinite by the preceding paragraph and OVW04.

The spatial identity for \(T\) is
\[
 \frac{d\varphi}{d\chi}=\frac{d(\varphi E)}{d\rho}.
\tag{EI.48}
\]
Apply EI08 to both sides. On \(pH\), it becomes
\[
 \frac{d\varphi_p}{d(\rho_pT_p)}
 =\frac{d(\varphi_pE_p)}{d\rho_p},
\tag{EI.49}
\]
where \(E_p\) is the original expectation in the selected representation. The fixed-reference uniqueness argument of OD03 identifies \(T_p\) with \(E_p'\). More explicitly, comparison with the dual of \(E_p\), reciprocity and spatial injectivity give equality of their scalar composites with \(\rho_p\); OR02 then gives equality of the operator-valued weights.

By EI01, \(T(1)=\kappa1\). Covariance now yields
\[
 E_p'(p)=T_p(p)=pT(1)p=\kappa p.
\tag{EI.50}
\]
This holds for both summands and includes \(\kappa=\infty\). Their dual scalars are therefore equal. We may call their common value \(\operatorname{Idx}(E)\), independently of the faithful normal representation. The argument uses a direct sum and exact full-corner compression; it does not need an unproved amplification theorem or a separable representation.

## Iteration and both neighboring Jones relations

Assume the finite value \(\kappa=\operatorname{Idx}(E)\), put \(\lambda=\kappa^{-1}\), and retain the faithful normal state setting of EI05. Write
\[
 A_{-1}=N,\quad A_0=M,\quad E_0=E.
\tag{EI.51}
\]
Repeat the basic construction and normalized dual expectation:
\[
 A_{-1}\subseteq A_0\subseteq A_1\subseteq A_2\subseteq\cdots,
 \qquad E_k:A_k\to A_{k-1}.
\tag{EI.52}
\]
At each stage compose the state on \(A_{k-1}\) with \(E_k\) to obtain a faithful normal state on \(A_k\). EI05–07 construct a factor \(A_{k+1}\), its projection \(e_k\in A_{k+1}\), and a faithful normal expectation \(E_{k+1}\). EI09 makes the index independent of the faithful representations used at successive stages. Inductively, all \(E_k\) have index \(\kappa\), and
\[
 \begin{gathered}
 A_{k+1}=\{A_k,e_k\}'',\qquad
 e_k x e_k=E_k(x)e_k\quad(x\in A_k),\\
 e_k\in A_{k-1}',\qquad E_{k+1}(e_k)=\lambda1.
 \end{gathered}
\tag{EI.53}
\]
Each smaller algebra is identified with its faithful normal image at the next stage; these identities therefore persist along the abstract inclusion chain.

If \(j\geq i+2\), then \(e_i\in A_{i+1}\subseteq A_{j-1}\), which commutes with \(e_j\). Hence \(e_ie_j=e_je_i\). Applying the projection relation for \(e_{k+1}\) to \(e_k\in A_{k+1}\) gives
\[
 e_{k+1}e_k e_{k+1}=\lambda e_{k+1}.
\tag{EI.54}
\]
We must also prove the relation in the other order; it does not follow for an arbitrary pair of projections from this equation alone.

Work in the GNS representation used to construct \(A_{k+2}\) from \(E_{k+1}\), with cyclic vector \(\Omega_{k+1}\). Put \(e=e_k\) and \(f=e_{k+1}\). The range of \(f\) is \(\overline{A_k\Omega_{k+1}}\). Algebraic words in \(A_k\) and \(e\) generate a strongly dense star algebra in \(A_{k+1}\), by BK02. Multiplying such a word on the left by \(e\) and repeatedly using \(exe=E_k(x)e\), with \(E_k(x)\in A_{k-1}\) commuting with \(e\), reduces it to an element of \(eA_k\). Cyclicity and strong approximation therefore give
\[
 \overline{eA_k\Omega_{k+1}}=eH_{k+1},
 \qquad \overline{efH_{k+1}}=eH_{k+1}.
\tag{EI.55}
\]
The bounded operator \(v=\lambda^{-1/2}ef\) satisfies
\[
 v^*v=\lambda^{-1}fef=f.
\tag{EI.56}
\]
It is consequently a partial isometry, whose final projection is the projection onto \(\overline{efH_{k+1}}\), namely \(e\). Thus \(vv^*=e\), proving
\[
 e_k e_{k+1}e_k=\lambda e_k.
\tag{EI.57}
\]
We have obtained both adjacent relations and every distant commutation relation. These are general finite-index expectation identities. No assertion about the possible index range or classification of the resulting tower is used in their proof.

## Sources and scope

Masamichi Takesaki, *Theory of Operator Algebras III*, XIX.2, Exercise 5(b)–(e), provides the comparison statements. The expectation is faithful and normal, as required by its commutant dual. Scalarity and representation independence above hold for arbitrary factors; the Jones-projection and tower constructions use the faithful normal state specified in EI05. The separate II1 dimension identification in part (a), index-range theorem in part (f), and principal-graph assertions require their own proofs.
