# Tracial multiplication actions and the preserving expectation

**Self-checked by the writing AI.** The source targets are Takesaki, *Theory of Operator Algebras I*, V.2 Theorem 2.22, printed 324–325 (PDF 331–332), and Proposition 2.36, printed 332 (PDF 339). This text supplies their full arguments at the named course inputs. The arguments below use the precise course inputs listed next.

Let \(M\) carry a normal, semifinite, faithful trace \(\tau\). No assumption is made about separability, countable decomposability or \(\tau(1)\). Write \(H_\tau=L^2(M,\tau)\), with inner product linear in its first argument. Whenever a von Neumann subalgebra \(N\subseteq M\) is considered below, it has the same identity. This is the subalgebra convention used by the source expectation proof: its finite projections have supremum \(1_M\).

The precise inputs are TI-01–03 and TI-09–11 for the finite-projection nets, complete trace spaces, bounded module estimates and cyclic integral; TI-06 and TI-14, with CP-06, for the canonical identifications \(L^1(M,\tau)=M_*\) and \((L^1(M,\tau))^*=M\); TI-15 and WG-006 for the concrete Hilbert space and trace GNS transport; WH-02 for the closed image of a faithful normal representation; WH-03–04, WH-09–12 and MF-01, MF-05–06 for unchanged full-completion data, the commutant theorem and modular covariance. These results are used at their stated scopes. The stronger uniqueness assertion in TA-04 additionally uses CE-004, the bimodule theorem for a contractive retraction. The exact input sections are Full nonunital retraction theorem, The concrete predual and its intrinsic norm, Starting data, full completion and exact inputs, The commutant and the integral orbit identity, The modular fundamental theorem, Finite pieces without a countability assumption, A scalar size function with exact operator cutoffs, Fatou estimates and concrete approximation, The trace pairing fills the whole predual, Complete norms on actual measurable operators, Products, norming tests and exact factorization, Bounded strong convergence acts on each integrable vector, Spectral tests establish global duality, The Hilbert space behind the trace, The GNS construction for an arbitrary weight, The image of a faithful normal representation, Completing the two multiplication domains, Mixed bounded vectors and fullness, From a faithful normal semifinite weight to an algebra, Closability on the full finite-star domain, Fullness and recovery of the original weight, The right weight and the variational formula. Proposition 2.36 below is proved directly from the trace predual; it is not assumed through the modular expectation theorem.

## The trace core and its entire modular domain

Put \(\mathcal A_\tau=\{a\in M:\tau(a^*a)<\infty\}\), identified with its vectors in \(H_\tau\). Traciality gives \(\tau(aa^*)=\tau(a^*a)\), so this is a star algebra and a two-sided ideal of \(M\). The left and right module estimates of TI-10 give

\[
 \|ab\|_2\leq\|a\|\|b\|_2,
 \qquad \|ba\|_2\leq\|a\|\|b\|_2
 \quad(a\in M,\ b\in\mathcal A_\tau).
 \tag{TA.1}
\]

Its inner product is \(\langle a,b\rangle_2=\tau(b^*a)\). For \(a,b,c\in\mathcal A_\tau\), the finite products and cyclic integral give

\[
 \langle ab,c\rangle_2=\langle b,a^*c\rangle_2,
 \qquad \langle a^*,b^*\rangle_2=\langle b,a\rangle_2.
 \tag{TA.2}
\]

In particular the involution is an isometry of this dense subspace. Its unique continuous extension is the antiunitary \(J_\tau x=x^*\) of TI-15. The graph closure of its restriction is exactly the graph of \(J_\tau\): any approximating net of core vectors converges together with its adjoints by the isometry. Thus the closed Tomita map has domain all of \(H_\tau\).

The finite-trace projections form a directed net \(e\uparrow1\); the join of two such projections still has finite trace. For \(a\in\mathcal A_\tau\), TI-11 gives \(ea\to a\) in \(L^2\). Every \(ea\) is the product of two elements of \(\mathcal A_\tau\). Since the core is dense by TI-09, its product span is dense in \(H_\tau\). This proves the product-density axiom rather than presuming that density of the core already implies it. Together with (TA.1–2) and the closed involution, it establishes all left Hilbert algebra axioms.

For this Hilbert algebra the closed involution and its antilinear adjoint are both \(J_\tau\). Consequently

\[
 S=F=J_\tau,
 \qquad \Delta=FS=I_{H_\tau},
 \qquad D(S)=D(F)=D(\Delta^z)=H_\tau
 \quad(z\in\mathbb C).
 \tag{TA.3}
\]

These are full operator statements, including domains. Replacing the initial algebra by its full completion changes neither these data nor its generated algebra, by WH-03–04.

For comparison with the trace weight itself, use the onto GNS unitary \(U:H_\tau^{\mathrm{GNS}}\to H_\tau\), \(U\Lambda_\tau(a)=a\), from TI-15. On the dense initial Tomita domain it sends \(\Lambda_\tau(a)\mapsto\Lambda_\tau(a^*)\) to \(a\mapsto a^*\). The latter has bounded closure \(J_\tau\). Passing to graph closures therefore gives \(US_\tau U^*=J_\tau\) and \(U\Delta_\tau U^*=I\). Modular covariance and faithfulness of the GNS representation now imply

\[
 \sigma_t^\tau(a)=a
 \quad(a\in M,\ t\in\mathbb R).
 \tag{TA.4}
\]

This computation concerns the actual trace GNS realization. It does not infer measurable or modular data from an unspecified Hilbert-space isomorphism.

## Every tracial commutant and both conjugation identities

For \(a\in M\), define \(L_ax=ax\) and \(R_ax=xa\) on all of \(H_\tau\). They are bounded by (TA.1). TI-15 proves that \(a\mapsto L_a\) is a faithful normal unital star representation. Its range is a von Neumann algebra by WH-02. For every \(a\in M\) and every finite-trace projection \(e\),

\[
 ae\in\mathcal A_\tau,
 \qquad \|ae\|_2^2\leq\|a\|^2\tau(e),
 \qquad L_{ae}=L_aL_e\longrightarrow L_a
 \text{ strongly}.
 \tag{TA.5}
\]

The last limit uses normality of the left representation on the increasing projection net \(e\uparrow1\). It follows that \(\{L_b:b\in\mathcal A_\tau\}''=L(M)\): one inclusion uses the closed image of the representation, and the other follows from the strong limit (TA.5).

On every vector of \(H_\tau\), the measurable algebra identities give

\[
 J_\tau L_aJ_\tau x=(ax^*)^*=xa^*=R_{a^*}x,
 \qquad J_\tau R_aJ_\tau x=(x^*a)^*=a^*x=L_{a^*}x.
 \tag{TA.6}
\]

There is an adjoint on each coefficient. In particular, right multiplication is a linear star antirepresentation:

\[
 R_aR_b=R_{ba},\qquad R_a^*=R_{a^*}.
 \tag{TA.7}
\]

It is faithful by (TA.6). If \(a_i\uparrow a\) is a bounded increasing positive net in \(M\), then \(L_{a_i}\to L_a\) strongly, so conjugation by \(J_\tau\) gives \(R_{a_i}\to R_a\) strongly and preserves the positive order. This proves normality of the right action, without silently treating an antirepresentation as a representation.

Apply MF-05 to the left Hilbert algebra proved in TA-01. Its generated von Neumann algebra is \(L(M)\), and its modular conjugation is precisely \(J_\tau\). The theorem yields \(L(M)'=J_\tau L(M)J_\tau\). Equation (TA.6) identifies that conjugate algebra with \(R(M)\). Taking commutants, and using that \(L(M)\) is already a von Neumann algebra, proves all the source algebra identities:

\[
 \begin{aligned}
 L(M)'&=R(M),& R(M)'&=L(M),\\
 J_\tau L(M)J_\tau&=R(M),&
 J_\tau R(M)J_\tau&=L(M).
 \end{aligned}
 \tag{TA.8}
\]

This proves the reverse conjugation equality as well as the mutual commutants. Mere commutation of the two actions would give only inclusions and would not prove (TA.8). The argument uses the full Hilbert algebra theorem at its named inputs; it assumes neither that \(1\) is an \(L^2\) vector nor that a faithful normal state exists.

## Constructing the trace-preserving projection on every positive value

Let \(N\subseteq M\) have the same identity and let \(\nu=\tau|_{N_+}\) be semifinite. Normality and faithfulness pass to the restriction. Apply the trace-space constructions to both algebras.

For a bounded element \(y\) of the finite trace ideal \(\mathfrak m_\nu\), the absolute value computed in \(N\) is the same as its absolute value in \(M\). Therefore \(\|y\|_{1,\nu}=\nu(|y|)=\tau(|y|)=\|y\|_{1,\tau}\). Inclusion on this dense finite ideal extends to a canonical isometry

\[
 j:L^1(N,\nu)\longrightarrow L^1(M,\tau).
 \tag{TA.9}
\]

This extension is defined by the complete trace norms. No arbitrary identification of the two completed spaces is involved. The bounded left and right \(N\)-module actions commute with \(j\), first on the finite ideal and then by norm continuity.

Use the canonical trace pairings to identify these \(L^1\) spaces with the actual preduals. Their Banach duals are \(N\) and \(M\). Define \(E=j^*:M\to N\). Explicitly, for \(x\in M\) and \(y\in\mathfrak m_\nu\),

\[
 \nu(E(x)y)=\tau(xy).
 \tag{TA.10}
\]

Both sides are finite linear trace integrals; this is not a subtraction of infinite weight values. This formula and norm continuity extend to the full \(L^1(N,\nu)\) pairing. Having the bounded preadjoint \(j\), the map \(E\) is ultraweakly continuous and hence normal. If \(N\ne\{0\}\), semifiniteness and faithfulness make \(L^1(N,\nu)\ne\{0\}\), so \(\|j\|=1\) and Banach duality gives \(\|E\|=1\).

For \(n\in N\), the pairings in (TA.10) agree with \(\nu(ny)\). The predual separates \(N\), so \(E(n)=n\). Thus \(E\) is onto \(N\), is a projection, and is unital. The involution and the cyclic trace pairing similarly give \(E(x^*)=E(x)^*\).

Here is a direct verification of positivity. Suppose \(x\geq0\), but the self-adjoint \(E(x)\) has a nonzero spectral projection \(q=1_{(-\infty,-\varepsilon]}(E(x))\) for some \(\varepsilon>0\). Semifiniteness of \(\nu\) supplies a nonzero finite-trace projection \(f\leq q\). It then follows from (TA.10) that

\[
 0\leq\tau(fxf)=\tau(xf)=\nu(E(x)f)
 \leq-\varepsilon\nu(f)<0,
 \tag{TA.11}
\]

a contradiction. In the first equality the cyclic integral is legitimate because \(f\) has finite trace; \(fxf\) is positive and bounded. This proves \(E(x)\geq0\).

The finite \(\nu\)-trace projections form a net \(f\uparrow1\) in \(N\), which also increases strongly to \(1_M\). For \(x\in M_+\), positivity of \(E(x)\), (TA.10) and the cyclic integrals give

\[
 \begin{aligned}
 \nu(E(x))
 &=\sup_f\nu\bigl(E(x)^{1/2}fE(x)^{1/2}\bigr)\\
 &=\sup_f\nu(fE(x)f)
 =\sup_f\tau(fxf)\\
 &=\sup_f\tau\bigl(x^{1/2}fx^{1/2}\bigr)
 =\tau(x).
 \end{aligned}
 \tag{TA.12}
\]

The first and last suprema use normality on increasing positive nets. We do not assert that \(fxf\) itself increases with \(f\); its trace is identified with the trace of the increasing positive compression \(x^{1/2}fx^{1/2}\). Equation (TA.12) includes infinite values, with no use of a finite-cone identity beyond its permitted domain. If \(E(x)=0\) for \(x\geq0\), then \(\tau(x)=0\), and faithfulness of \(\tau\) gives \(x=0\). Thus the projection is faithful.

We have proved Proposition 2.36 directly: a faithful normal norm-one projection \(E:M\to N\) satisfying \(\tau=\nu\circ E\) on the full positive cone. The norm-one assertion concerns the nonzero unital algebra case. If \(M=N=\{0\}\), the unique map is the zero map and has norm zero; that is the explicit zero-algebra extension of the statement.

## Bimodule order, uniqueness and the exact Hilbert projection

For \(a,b\in N\), \(x\in M\), and \(y\in\mathfrak m_\nu\), cyclicity of the finite \(L^1\) pairing and its bounded module actions give

\[
 \begin{aligned}
 \nu(E(axb)y)&=\tau(axby)=\tau(xbya)\\
 &=\nu(E(x)bya)=\nu(aE(x)by).
 \end{aligned}
 \tag{TA.13}
\]

The predual separates points, so \(E(axb)=aE(x)b\). In particular, expanding \(E((x-E(x))^*(x-E(x)))\geq0\) using this identity proves the Schwarz inequality

\[
 E(x)^*E(x)\leq E(x^*x).
 \tag{TA.14}
\]

This proof does not require complete positivity as an unproved intermediate assertion.

Suppose \(F:M\to N\) is another complex-linear contractive retraction preserving \(\tau\) on every positive element. CE-004 supplies positivity and bimodularity. Preservation carries the finite positive trace ideal to that of \(N\), and its linear extension preserves the trace on \(\mathfrak m_\tau\). Hence, for \(y\in\mathfrak m_\nu\),

\[
 \nu(F(x)y)=\nu(F(xy))=\tau(xy)=\nu(E(x)y).
 \tag{TA.15}
\]

Thus \(F=E\), even if normality was not assumed for \(F\). This is an additional uniqueness conclusion, not a separate source atom or an assumption in the existence proof.

The finite square-integrable elements of \(N\) have identical \(\nu\) and \(\tau\) norms. Their inclusion extends to an isometry \(V:H_\nu=L^2(N,\nu)\to H_\tau\). Its image is the closed subspace \(H_N=\overline{\mathcal A_\nu}^{\,H_\tau}\). Let \(P=VV^*\), the orthogonal projection onto that precise subspace. By (TA.12) and (TA.14), \(x\in\mathcal A_\tau\) implies

\[
 E(x)\in\mathcal A_\nu,
 \qquad \|E(x)\|_{2,\nu}^2
 \leq\nu(E(x^*x))=\|x\|_{2,\tau}^2.
 \tag{TA.16}
\]

For \(n\in\mathcal A_\nu\), the product \(n^*x\) lies in \(\mathfrak m_\tau\). The finite trace extension, preservation and bimodularity give

\[
 \langle E(x),n\rangle_{2,\nu}
 =\nu(n^*E(x))=\tau(n^*x)
 =\langle x,Vn\rangle_{2,\tau}.
 \tag{TA.17}
\]

Density of \(\mathcal A_\nu\) proves \(E(x)=V^*x\) as Hilbert vectors, and consequently

\[
 VE(x)=Px\quad(x\in\mathcal A_\tau),
 \qquad E_2=V^*:H_\tau\longrightarrow H_\nu,
 \qquad VE_2=P.
 \tag{TA.18}
\]

Here \(E_2\) denotes the continuous \(L^2\) extension on the entire Hilbert space. It is not an assertion that the original bounded-algebra map \(E:M\to N\) was already defined on arbitrary unbounded measurable operators. The Banach preadjoint \(j\), the Hilbert inclusion \(V\), and their two different adjoints have specified domains and codomains.

## Finite matrix checks with the correct orientations

For \(M=M_n(\mathbb C)\) with its usual trace, column vectorization sends the matrix unit \(E_{ij}\) to \(e_j\otimes e_i\). It is unitary from Hilbert–Schmidt space to \(\mathbb C^n\otimes\mathbb C^n\). In these coordinates,

\[
 L_A=I_n\otimes A,
 \qquad R_B=B^{\mathsf T}\otimes I_n,
 \qquad J_\tau(e_j\otimes e_i)=e_i\otimes e_j
 \text{ conjugate-linearly}.
 \tag{TA.19}
\]

The transpose in \(R_B\) is essential. The two tensor factors commute, \(R_AR_B=R_{BA}\), and \(J_\tau L_AJ_\tau=R_{A^*}\). Testing the matrix units determines both commutants in this finite example. It checks the general proof's formulas, rather than reducing that proof to matrices.

For a trace \(\tau(A\oplus B)=\alpha\operatorname{Tr}_2(A)+\beta\operatorname{Tr}_3(B)\), where \(\alpha,\beta>0\), take \(N=\mathbb C(I_2\oplus I_3)\). Equation (TA.10) forces

\[
 E(A\oplus B)=
 \frac{\alpha\operatorname{Tr}_2(A)+\beta\operatorname{Tr}_3(B)}{2\alpha+3\beta}
 (I_2\oplus I_3).
 \tag{TA.20}
\]

This map fixes \(N\), is positive and faithful, and preserves the trace. With \(\alpha=2\), \(\beta=3\), its coefficient on \(E_{11}\oplus0\) is \(2/13\), and \(\tau(E(E_{11}\oplus0))=13(2/13)=2\). Its Hilbert implementation is the orthogonal projection onto the single vector \(I_2\oplus I_3\), whose squared norm is \(13\). The coefficient is obtained from that weighted inner product, not from averaging the two block traces equally.

For the extended-positive convention used elsewhere in the course, take \(a=E_{12}\), \(c=E_{11}\), and \(\omega(x)=\langle xe_2,e_2\rangle\). Then \(a^*ca=E_{22}\) gives \(\omega(a^*ca)=1\), while \(aca^*=0\) gives \(\omega(aca^*)=0\). Thus \((a^*\widehat ca)(\omega)=\widehat c(\omega_a)\) requires \(\omega_a(x)=\omega(a^*xa)\). The historical OVW error concerned exactly this order; the current OVW formula has the corrected convention.

## Infinite trace and the indispensable restriction hypothesis

**Problem 1.** For \(M=B(\ell^2(I))\) with canonical trace, where the index set \(I\) may be uncountable, describe \(H_\tau\), its dense algebraic core and \(J_\tau\). Explain why the proof of TA-02 does not require a vector represented by \(1\).

**Solution.** The Hilbert space is the space of Hilbert–Schmidt operators, identified by its matrix units with \(\ell^2(I\times I)\). Finite matrix-unit sums are dense; finite-coordinate projections form a net directed by finite subsets, not a distinguished sequence. The antiunitary sends the coefficient at \((i,j)\) to the conjugate of the coefficient at \((j,i)\). If \(I\) is infinite, the identity has infinite squared Hilbert–Schmidt norm. Nevertheless \(L_e\uparrow I_{H_\tau}\) on the finite-projection net, which is the operator convergence used in (TA.5). The Hilbert-space identity is a bounded operator even when the algebra identity is not a Hilbert vector.

**Problem 2.** In \(B(\ell^2(\mathbb N))\), let \(N=\mathbb C1\). Show that no normal unital positive retraction onto \(N\) can preserve the canonical trace. Locate the failed hypothesis of TA-03.

**Solution.** Such a map has the form \(F(x)=\omega(x)1\) for a normal state \(\omega\). If \(p_k\) are the coordinate rank-one projections, normality gives \(\sum_k\omega(p_k)=\omega(1)=1\). Hence some \(\omega(p_k)>0\), and then \(\tau(F(p_k))=\infty\), whereas \(\tau(p_k)=1\). The restriction of \(\tau\) to \(\mathbb C1\) is not semifinite: every nonzero positive scalar multiple of \(1\) has infinite trace. Its finite-trace ideal is zero and supplies neither the predual isometry (TA.9) with the claimed trace identification nor a finite-projection net approaching the common identity.

**Problem 3.** Let \(M=L^\infty(X,\mu)\) be a von Neumann algebra carrying a faithful normal semifinite integration trace, and let \(N=M\). What are the two represented algebras, the expectation and its Hilbert extension?

**Solution.** Left and right multiplication coincide. Formula (TA.8) proves that their image is its own commutant on \(L^2(X,\mu)\). The canonical \(L^1\) inclusion and the Hilbert inclusion are both identities, so \(E\), \(E_2\) and \(P\) are identities on their respective spaces. This covers infinite total measure as well as finite measure. If the base measure is zero, all these spaces are zero and the operator norm of the zero expectation is zero, as already separated in TA-03.

The three actually inspected source pages contain the full two source statements and their proofs. The present proof route for the commutants uses the course's general Hilbert algebra theorem; the expectation proof uses the canonical trace predual and increasing positive compressions. Neither route adds a faithful-state, finite-total-trace, separability or countability hypothesis. The finite checks and solved problems verify the orientations and hypotheses used in the general proofs.
