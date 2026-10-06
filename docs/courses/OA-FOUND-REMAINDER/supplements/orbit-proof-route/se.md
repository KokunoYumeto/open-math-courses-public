<span id="recovering-a-representation-from-its-positive-cone"></span>
# Recovering a representation from its positive cone

<span id="oa-mod-se-01--axioms-and-the-geometric-facts-available-before-comparison"></span>
<span id="OA-MOD-SE-01"></span>
<span id="oa-mod-se-01"></span>
## OA-MOD-SE-01 — Axioms and the geometric facts available before comparison

Let \(M\subset B(H)\) be a von Neumann algebra. A standard form is a quadruple \((M,H,J,P)\), where \(J\) is an antiunitary involution, \(P\) is a self-dual cone, and
\[
 JMJ=M',\qquad JzJ=z^*\quad(z\in Z(M)),\qquad
 J\xi=\xi\quad(\xi\in P),\qquad xJxJ P\subset P\quad(x\in M).
 \tag{SE.1}
\]
Inner products are linear in the first variable. Self-duality means that \(\eta\in P\) exactly when every \(\langle\xi,\eta\rangle\), \(\xi\in P\), is real and nonnegative. Thus \(P\) is norm closed, convex and pointed. This is the complex Hilbert-space dual cone convention of SF-01.

We use the proofs of SF-06–07 at their axiomatic level. They require self-duality, pointwise \(J\)-fixedness, the commutant identity and \(xJxJ\)-invariance, but not the central identity or the existence of representatives for every normal functional. Consequently, in every form under discussion, the following statements hold before any equivalence theorem:
\[
 H=\operatorname{span}_{\mathbb C}P,\qquad
 \overline{M'\xi}=s_\xi H,\qquad
 \overline{M\xi}=Js_\xi JH\quad(\xi\in P),
 \tag{SE.2}
\]
where \(s_\xi=s_M(\omega_\xi)\) and \(\omega_\xi(x)=\langle x\xi,\xi\rangle\). Moreover,
\[
 \langle\xi,\eta\rangle=0\iff s_\xi s_\eta=0,
 \qquad
 \|\xi-\eta\|^2\le\|\omega_\xi-\omega_\eta\|
       \le\|\xi-\eta\|\,\|\xi+\eta\| .
 \tag{SE.3}
\]
In particular a unitary intertwining the algebra and mapping one cone onto another is unique if it exists. Indeed the ratio of two such unitaries commutes with the algebra and preserves every cone-vector functional; the first inequality makes it fix every cone vector, and (SE.2) makes it the identity.

For clarity about prerequisites, the analytic inputs are the finite GNS construction WG-004–006, the cyclic involution and antilinear adjoint conventions TC-03–05/08, right-bounded multipliers HA-05/08 and the actual right-involution graph core RD-04. SF-04 supplies the cone generators in a weight form; SF-09 supplies comparison between two weight forms. NW-03 supplies the directed family of sigma-finite projections. These results are used at their stated mathematical scope. No spatial derivative, relative modular identification, cocycle theorem or assumption of a faithful normal state on \(M\) is used.

<span id="oa-mod-se-02--compression-and-the-commutant"></span>
<span id="OA-MOD-SE-02"></span>
<span id="oa-mod-se-02"></span>
## OA-MOD-SE-02 — Compression and the commutant

We first prove a bounded-operator fact independently of cone geometry. If \(A\) is a von Neumann algebra on \(L\) and \(p\in A\) is a projection, then
\[
 (pAp\text{ on }pL)'=A'|_{pL}.
 \tag{SE.4}
\]
Here the right side is the set of restrictions; elements of \(A'\) commute with \(p\), so these restrictions make sense.

**Proof.** Let \(T\in B(pL)\) commute with \(pAp\). On finite sums prescribe
\[
 \widetilde T\left(\sum_{i=1}^n a_i v_i\right)
       =\sum_{i=1}^n a_iTv_i,
 \qquad a_i\in A,\quad v_i\in pL.
 \tag{SE.5}
\]
Let \(X:(pL)^n\to L\) be the row operator with entries \(a_i|_{pL}\). The entries of \(B=X^*X\) are \(pa_i^*a_jp\). The diagonal operator \(D_T\) commutes with this positive matrix and its square root. Bounded continuous functional calculus therefore gives
\[
 \|XD_Tv\|=\|B^{1/2}D_Tv\|
   =\|D_TB^{1/2}v\|\le\|T\|\,\|Xv\|.
 \tag{SE.6}
\]
Thus (SE.5) is well-defined and bounded. Extend it to \(L_0=\overline{A(pL)}\), then by zero on \(L_0^\perp\). The space \(L_0\) reduces \(A\), and the defining formula commutes with each element of \(A\) on its dense finite-sum domain. The extension lies in \(A'\) and restricts to \(T\). The other inclusion in (SE.4) follows by multiplication. \(\square\)

If \(B\) is a unital *-algebra on \(L\) and \(q\in B'\) is a projection, one also has
\[
 (B|_{qL})'=(qB'q)|_{qL}.
 \tag{SE.7}
\]
To see the nontrivial inclusion, extend a commuting operator on \(qL\) by zero on \((1-q)L\); the reducing decomposition shows that it commutes with \(B\).

For a standard form and a projection \(e\in M\), put
\[
 f=JeJ,\qquad Q_e=ef,
 \qquad K_e=Q_eH,
 \qquad N_e=(eMe)|_{K_e}.
 \tag{SE.8}
\]
The two factors of \(Q_e\) commute. Apply (SE.4) on \(eH\), then (SE.7) with \(f|_{eH}\), to obtain
\[
 N_e'=(fM'f)|_{K_e}.
 \tag{SE.9}
\]
The same two arguments with \(M,M'\) exchanged give the reverse commutant identity. Thus \(N_e=N_e''\) on \(K_e\), in particular it is a von Neumann algebra. Since \(JQ_eJ=Q_e\), the restricted conjugation \(J_e\) satisfies \(J_eN_eJ_e=N_e'\). No assertion about the image of a general normal representation is needed for this argument.

<span id="oa-mod-se-03--every-projection-has-a-faithful-cone-corner"></span>
<span id="OA-MOD-SE-03"></span>
<span id="oa-mod-se-03"></span>
## OA-MOD-SE-03 — Every projection has a faithful cone corner

For a projection \(e\in M\), define
\[
 P_e=P\cap K_e.
 \tag{SE.10}
\]
Then \(P_e=Q_eP\), this cone is self-dual in \(K_e\), and the restriction of \(eMe\) to \(K_e\) is faithful. Together with \(J_e\), these objects form a standard form of \(eMe\), even when this corner has no faithful normal state.

**Detection of a support.** Cone invariance gives \(Q_eP\subset P\). For \(\eta\in P\) and real \(t\), expand the nonnegative cone pairing
\[
 0\le\langle(1+te)J(1+te)J\eta,\eta\rangle
   =\|\eta\|^2+2t\|e\eta\|^2+t^2\|Q_e\eta\|^2.
 \tag{SE.11}
\]
The equality of the two linear coefficients follows from \(J\eta=\eta\); the quadratic coefficient is that of the orthogonal projection \(Q_e\). If \(Q_e\eta=0\), positivity for every real \(t\) forces \(e\eta=0\). In particular
\[
 Q_e=0\quad\Longrightarrow\quad e=0,
 \tag{SE.12}
\]
because cone vectors span \(H\).

Every vector in \(P\cap K_e\) is fixed by \(Q_e\), proving \(P_e=Q_eP\). For \(v\in K_e\), its pairings against \(Q_eP\) are its pairings against \(P\). Hence if they are all real nonnegative, \(v\in P\cap K_e\). This proves self-duality in the smaller Hilbert space and thus spanning of \(K_e\).

Suppose \(x\in eMe\) acts by zero on \(K_e\). Then \(xQ_e=0\). Its right support \(r=s(x^*x)\le e\) has \(rQ_e=0\); this follows either from the kernel of \(x\) or its spectral projections. Thus \(rJeJ=0\), and \(JrJ\le JeJ\) gives \(Q_r=0\). Equation (SE.12) makes \(r=0\), hence \(x=0\). This proves faithfulness.

Pointwise \(J_e\)-fixedness follows by restriction. If \(x\in eMe\), then \(xJxJ\) preserves both \(P\) and \(K_e\), giving the cone-invariance axiom. The commutant identity was proved in SE-02. To verify the central axiom without assuming a description of \(Z(eMe)\), we record why it follows from the other axioms. For a central unitary \(u\) in a represented algebra with those axioms, \(uJuJ\) is a unitary commuting with that algebra and mapping its cone onto itself; its inverse is \(u^*Ju^*J\). The geometric uniqueness in SE-01 makes \(uJuJ=I\), so \(JuJ=u^*\). A central self-adjoint contraction \(a\) is the real part of the central unitary \(a+i(1-a^2)^{1/2}\). Real linearity therefore gives \(JaJ=a\), and decomposition into real and imaginary self-adjoint parts gives \(JzJ=z^*\) for every central \(z\). Apply this to \(N_e\), using its identity on \(K_e\), to complete all the corner axioms. \(\square\)

<span id="oa-mod-se-04--the-two-cyclic-domains-are-graph-cores"></span>
<span id="OA-MOD-SE-04"></span>
<span id="oa-mod-se-04"></span>
## OA-MOD-SE-04 — The two cyclic domains are graph cores

Let \(N\subset B(K)\) have a cyclic separating vector \(\Omega\). Define the antilinear maps
\[
 S_0(a\Omega)=a^*\Omega\quad(a\in N),\qquad
 F_0(b\Omega)=b^*\Omega\quad(b\in N'),
 \qquad S=\overline{S_0},\quad F=S^*.
 \tag{SE.13}
\]
Then
\[
 \overline{F_0}=F.
 \tag{SE.14}
\]
In particular both \(N\Omega\) and \(N'\Omega\) are graph cores for the corresponding closed involutions. Hilbert-space density alone would not imply this assertion.

**Proof.** TC-04 proves closability and \(F_0\subset S_0^*=F\). The space \(\mathcal A=N\Omega\), with product \((a\Omega)(b\Omega)=ab\Omega\) and involution \(a\Omega\mapsto a^*\Omega\), is a left Hilbert algebra: left multiplication is bounded, its adjoint relation follows from the Hilbert inner product, its involution is closable, and its algebra identity vector \(\Omega\) makes \(\mathcal A^2=\mathcal A\). Its left von Neumann algebra is \(N\).

HA-05 assigns to every right-bounded vector \(\eta\) a multiplier \(R_\eta\in N'\). Substituting the algebra unit in its defining formula gives \(\eta=R_\eta\Omega\). Conversely, for \(b\in N'\), the vector \(b\Omega\) is right bounded: its multiplier on \(a\Omega\) is \(a b\Omega=b a\Omega\), hence is the bounded operator \(b\). Thus the right-bounded space equals \(N'\Omega\). TC-04 puts every such vector in \(D(F)\), with \(F(b\Omega)=b^*\Omega\). The full right algebra \(\mathcal A_r=\mathcal B_r\cap D(F)\) of HA-08 is consequently exactly \(N'\Omega\). RD-04 says that this algebra is a graph core for \(F\). This proves (SE.14). The core assertion for \(S\) is its definition. \(\square\)

<span id="oa-mod-se-05--recognizing-a-modular-conjugation-by-its-exact-graph"></span>
<span id="OA-MOD-SE-05"></span>
<span id="oa-mod-se-05"></span>
## OA-MOD-SE-05 — Recognizing a modular conjugation by its exact graph

For \(N,\Omega\) as in SE-04, let \(C\) be an antiunitary involution such that
\[
 C\Omega=\Omega,\qquad CNC=N',\qquad
 \langle C a C a\Omega,\Omega\rangle\ge0\quad(a\in N).
 \tag{SE.15}
\]
Then \(C\) is the modular conjugation \(J_\Omega\). Conversely \(J_\Omega\) has these properties.

**Proof, including self-adjointness.** The first two hypotheses send \(N\Omega\) onto \(N'\Omega\), and direct calculation on the latter gives \(CS_0C=F_0\). Antiunitary transport preserves graph closure. Equation (SE.14) therefore gives the equality of closed antilinear operators
\[
 CSC=F=S^*,\qquad D(F)=CD(S).
 \tag{SE.16}
\]
The operator \(L=CS\) is closed, densely defined and complex-linear. The antilinear adjoint convention is \(\langle Su,v\rangle=\langle Fv,u\rangle\). For its ordinary linear adjoint one consequently has
\[
 D(L^*)=\{v\in K\mid Cv\in D(F)\},\qquad L^*v=FCv.
 \tag{SE.17}
\]
Indeed \(\langle CSu,v\rangle=\langle Cv,Su\rangle\); conjugate the antilinear adjoint test to obtain exactly (SE.17), including its necessity. Equation (SE.16) makes this domain \(D(S)\) and its action \(CS\). Hence \(L=L^*\).

For \(a\in N\), its quadratic form on the graph core is
\[
 \langle L(a\Omega),a\Omega\rangle
  =\langle Ca^*\Omega,a\Omega\rangle
  =\langle a^*Ca^*C\Omega,\Omega\rangle\ge0.
 \tag{SE.18}
\]
The two bounded factors \(a^*\) and \(Ca^*C\) commute, so the last inequality is (SE.15) with \(a^*\). The graph norms of \(L\) and \(S\) agree; graph approximation makes this inequality hold throughout \(D(L)\). Thus \(L\) is positive self-adjoint, not just positive symmetric. The factorization \(S=CL\) has a positive self-adjoint second factor. Both \(S\) and its range are dense with zero kernel, by TC-05, so polar uniqueness TC-08 gives \(C=J_\Omega\), \(L=\Delta_\Omega^{1/2}\).

Conversely \(S\Omega=F\Omega=\Omega\) implies \(\Omega\in D(S^*S)\) and \(\Delta_\Omega\Omega=\Omega\), hence \(J_\Omega\Omega=\Omega\). The commutant identity is MF-05, applied to the cyclic GNS Hilbert algebra. Positivity of \(\Delta_\Omega^{1/2}\) in (SE.18), with \(a^*\) in place of \(a\), gives the final condition in (SE.15). \(\square\)

The equality in (SE.16) is essential. Positivity on \(N\Omega\) by itself would only produce a positive symmetric operator; it would not identify the self-adjoint square root in a polar decomposition.

<span id="oa-mod-se-06--the-corner-seen-by-a-positive-vector"></span>
<span id="OA-MOD-SE-06"></span>
<span id="oa-mod-se-06"></span>
## OA-MOD-SE-06 — The corner seen by a positive vector

Fix \(\xi\in P\), put \(e=s_\xi\), and let \(\omega_e\) be \(\omega_\xi\) restricted to \(eMe\). It is faithful, normal and finite. The GNS map defines a unique unitary
\[
 U_\xi:H_{\omega_e}\longrightarrow K_e,
 \qquad U_\xi\Lambda_{\omega_e}(a)=a\xi\quad(a\in eMe),
 \tag{SE.19}
\]
and it satisfies
\[
 U_\xi\pi_{\omega_e}(a)=aU_\xi,
 \quad U_\xi J_{\omega_e}=J_eU_\xi,
 \quad U_\xi P_{\omega_e}=P_e.
 \tag{SE.20}
\]
Among unitaries to \(K_e\), the algebra-intertwining and cone-mapping properties alone characterize \(U_\xi\).

**Proof.** If \(e=0\), the spaces and map are zero. Otherwise (SE.2) gives
\[
 \overline{eMe\xi}=e\overline{M\xi}=eJeJH=K_e.
 \tag{SE.21}
\]
The equality uses \(e\xi=\xi\). The norm identity \(\omega_e(a^*a)=\|a\xi\|^2\) and polarization give the isometry and its onto extension. Multiplication proves intertwining. If \(a\in eMe\) kills \(\xi\), it kills \(M'\xi\) and hence \(eH\), so \(a=0\). Thus \(\xi\) is separating for the represented corner; it is cyclic by (SE.21). Faithfulness of \(\omega_e\) follows by applying this argument to positive square roots.

The restriction \(J_e\) fixes \(\xi\) and exchanges the corner and its commutant by SE-02. The last condition in (SE.15) holds because \(aJaJ\xi\in P\), \(\xi\in P\), and the bounded left and right factors commute. SE-05 now identifies \(J_e\) with the transported modular conjugation, with all closed domains accounted for.

Because \(\omega_e\) is finite, its finite-star algebra is all of \(eMe\). SF-04 describes its cone as the closure of \(\pi_{\omega_e}(a)J_{\omega_e}\Lambda_{\omega_e}(a)\), \(a\in eMe\). Their images are \(aJaJ\xi\in P_e\). The cone \(U_\xi P_{\omega_e}\) is self-dual in \(K_e\). Every vector of \(P_e\) pairs nonnegatively with it and therefore belongs to it, proving the reverse inclusion. This cone equality follows from the graph identification; it was not a premise of that identification. Uniqueness follows from SE-01. \(\square\)

<span id="oa-mod-se-07--closing-one-order-ideal-gives-its-entire-supported-face"></span>
<span id="OA-MOD-SE-07"></span>
<span id="oa-mod-se-07"></span>
## OA-MOD-SE-07 — Closing one order ideal gives its entire supported face

For \(\xi\in P\), define its principal cone ideal by
\[
 I_\xi=\bigcup_{c\ge0}[0,c\xi]_P,
 \qquad [0,c\xi]_P=\{\eta\in P\mid c\xi-\eta\in P\}.
 \tag{SE.22}
\]
Then
\[
 \overline{I_\xi}=P_{s_\xi}.
 \tag{SE.23}
\]
The closure is in the Hilbert norm. The right side is the smallest closed cone face containing \(\xi\). Here a cone face is a subcone \(F\subset P\) such that \(\eta+\zeta\in F\), \(\eta,\zeta\in P\), implies \(\eta,\zeta\in F\).

**Proof.** Let \(e=s_\xi\), \(q=1-e\). If \(\eta\in[0,c\xi]_P\), the two cone vectors \(Q_q\eta\) and \(Q_q(c\xi-\eta)\) sum to zero. Pointedness makes \(Q_q\eta=0\), and (SE.11) gives \(q\eta=0\). Since \(J\eta=\eta\), both \(e\) and \(JeJ\) fix it; hence \(\eta\in P_e\). This proves one inclusion after closure.

For the other inclusion use SE-06 to work in the finite faithful GNS corner, with \(\xi\) as its GNS identity vector. Its norm need not be one. The proof in SE-05 gives \(\Delta\xi=\xi\). SF-03 identifies the left square cone here with \(\overline{(eMe)_+\xi}\): every positive bounded \(a\) is a square of its positive square root, and every algebra square is of this kind. SF-04 and its graph-continuity proof consequently give
\[
 P_e=\overline{\{\Delta^{1/4}a\xi\mid a\in(eMe)_+\}}.
 \tag{SE.24}
\]
The vectors \(a\xi\) lie in \(D(\Delta^{1/2})\), because they lie in the initial involution domain; thus the quarter powers are defined. Each generator satisfies
\[
 \|a\|\xi-\Delta^{1/4}a\xi
    =\Delta^{1/4}(\|a\|e-a)\xi\in P_e.
 \tag{SE.25}
\]
It therefore belongs to \(I_\xi\). This proves density.

For any projection \(e\), if \(\eta+\zeta\in P_e\) with \(\eta,\zeta\in P\), apply \(Q_{1-e}\), pointedness and (SE.11) to conclude that both summands belong to \(P_e\). Thus \(P_e\) is a closed face. Every cone face containing \(\xi\) contains every \([0,c\xi]_P\), and every closed such face contains their closure. This proves minimality. \(\square\)

<span id="oa-mod-se-08--projections-and-all-closed-cone-faces"></span>
<span id="OA-MOD-SE-08"></span>
<span id="oa-mod-se-08"></span>
## OA-MOD-SE-08 — Projections and all closed cone faces

The map \(e\mapsto P_e\) is an order-preserving bijection between projections of \(M\) and norm-closed cone faces of \(P\), and its inverse is
\[
 F\longmapsto\bigvee_{\xi\in F}s_\xi.
 \tag{SE.26}
\]
For projections \(e,f\),
\[
 P_e\perp P_f\iff ef=0,
 \qquad P\cap P_e^\perp=P_{1-e}.
 \tag{SE.27}
\]
In particular, for positive vectors \(\xi,\eta\), all three conditions are equivalent: \(\xi\perp\eta\), \(s_\xi s_\eta=0\), and \(P_{s_\xi}\perp P_{s_\eta}\).

**Proof.** Supports of vectors in \(P_e\) have supremum \(e\). They are at most \(e\). If their supremum \(r\) were smaller than \(e\), put \(q=e-r\). By (SE.12), \(K_q\ne0\); self-duality and spanning of \(P_q\) give a nonzero vector in \(P_q\subset P_e\). Its nonzero support would be both below \(q\) and below \(r\), a contradiction.

For a finite family \(\xi_1,\ldots,\xi_n\in P\),
\[
 s_{\xi_1+\cdots+\xi_n}=s_{\xi_1}\vee\cdots\vee s_{\xi_n}.
 \tag{SE.28}
\]
The right side fixes the sum, giving one inequality. If \(s\) is the support of the sum, apply \(Q_{1-s}\) to the summands. They are cone vectors with sum zero, so each is zero. Detection (SE.11) says that \(1-s\) kills every \(\xi_j\), giving the other inequality.

Let \(F\) be a closed cone face and \(e=\bigvee_{\xi\in F}s_\xi\). It is contained in \(P_e\). For each finite subset \(A\subset F\), let \(\xi_A=\sum_{\xi\in A}\xi\) and \(e_A=s_{\xi_A}\), allowing the empty sum. SE-07 shows \(P_{e_A}\subset F\). The projections \(e_A\) increase strongly to \(e\). Their conjugates do also, and the products \(Q_{e_A}\) increase strongly to \(Q_e\). To verify the product convergence, subtract the two products and use that all factors are contractions and each factor converges strongly. For \(\eta\in P_e\), the vectors \(Q_{e_A}\eta\in P_{e_A}\subset F\) converge to \(\eta\). Closedness gives \(P_e\subset F\).

If \(e\le f\), then \(Q_e\le Q_f\), giving \(P_e\subset P_f\). Conversely the support-supremum characterization just proved implies \(e\le f\) from that inclusion. This establishes the order bijection.

If \(ef=0\), vectors in the two cones have orthogonal left supports, proving orthogonality. Conversely, if the two cones are orthogonal, (SE.3) makes every support from the first orthogonal to every support from the second. Their suprema are \(e,f\), so \(ef=0\). The same argument with the support of one arbitrary vector gives the second formula in (SE.27). Apply these facts to \(e=s_\xi,f=s_\eta\) and use (SE.3) for the last assertion. \(\square\)

<span id="oa-mod-se-09--finding-a-full-support-vector-on-each-small-corner"></span>
<span id="OA-MOD-SE-09"></span>
<span id="oa-mod-se-09"></span>
## OA-MOD-SE-09 — Finding a full-support vector on each small corner

A projection \(e\) is called sigma-finite when \(eMe\) has a faithful normal state; include \(0\). Every such \(e\) is the support of a vector in \(P\). This conclusion concerns an arbitrary axiomatic form, so a normal-functional cone representation theorem cannot be assumed in its proof.

**Proof.** For \(e\ne0\), choose a faithful normal state \(\rho\) on \(eMe\). Supports of vectors in \(P_e\) have join \(e\), by SE-08. For finite subsets \(A\subset P_e\), the projections \(r_A=\bigvee_{\eta\in A}s_\eta\) increase to \(e\); normality gives \(\rho(r_A)\uparrow1\). Choose finite \(A_n\) with \(\rho(r_{A_n})>1-2^{-n}\). Their countable join is \(e\): its complement has \(\rho\)-value at most \(2^{-n}\) for every \(n\), and faithfulness removes that complement.

Enumerate the union of these finite sets as a sequence \((\eta_n)\), with repetitions or zeros if it is finite. The norm-convergent positive series
\[
 \xi=\sum_{n\ge1}\frac{2^{-n}}{1+\|\eta_n\|}\eta_n
 \tag{SE.29}
\]
belongs to \(P_e\). Let \(s=s_\xi\). For each \(n\), separate the corresponding positive multiple of \(\eta_n\) from the series; the remainder lies in \(P\) by closedness. Applying \(Q_{1-s}\) makes two cone vectors sum to zero. Pointedness and (SE.11) imply \((1-s)\eta_n=0\). Thus every selected support lies below \(s\), so \(s=e\). This also proves that \(\xi\) is cyclic and separating for \(eMe\) on \(K_e\), by SE-06. The zero corner is immediate. \(\square\)

NW-03 proves that the sigma-finite projections form an upward-directed set \(\mathcal E\) with supremum \(1\). Finite joins need not commute: the support of a positive linear combination of their faithful corner states is their join. Every nonzero projection contains the nonzero support of an ordinary normal positive functional, which proves exhaustion. Consequently
\[
 Q_e\uparrow I\text{ strongly as }e\in\mathcal E,
 \qquad \overline{\bigcup_{e\in\mathcal E}K_e}=H.
 \tag{SE.30}
\]
There is also an exact cone union \(P=\bigcup_{e\in\mathcal E}P_e\), since a positive vector's finite normal functional is faithful on its support corner. By four-vector spanning and finite directed joins, the union of the \(K_e\) is in fact all of \(H\). The density statement alone will suffice below. The index set \(\mathcal E\) need not have a countable cofinal subset.

<span id="oa-mod-se-10--patching-the-unique-comparisons"></span>
<span id="OA-MOD-SE-10"></span>
<span id="oa-mod-se-10"></span>
## OA-MOD-SE-10 — Patching the unique comparisons

Let \((M_1,H_1,J_1,P_1)\) and \((M_2,H_2,J_2,P_2)\) be arbitrary standard forms, and let \(\theta:M_1\to M_2\) be a unital *-isomorphism. There is exactly one unitary \(V:H_1\to H_2\) such that
\[
 VxV^*=\theta(x)\quad(x\in M_1),\qquad
 VJ_1=J_2V,\qquad VP_1=P_2.
 \tag{SE.31}
\]
It is enough for uniqueness to require the first and third properties.

**Proof.** A *-isomorphism preserves the positive order in both directions. It therefore preserves bounded increasing positive suprema and is normal. Identify the two algebras abstractly through \(\theta\), writing them as representations \(\pi_i\) of one \(M\). In each representation form the corner spaces \(K_{i,e}\), conjugations and cones, for \(e\in\mathcal E\).

SE-09 gives \(\xi_i\in P_{i,e}\) with support exactly \(e\). SE-06 identifies this corner with the natural-cone GNS form of a faithful finite functional on \(eMe\). SF-09 compares these two weight forms. Composing the three actual unitaries gives a unitary
\[
 V_e:K_{1,e}\longrightarrow K_{2,e}
 \tag{SE.32}
\]
intertwining \(eMe\) and mapping \(P_{1,e}\) onto \(P_{2,e}\). It is unique by SE-01 and therefore independent of the chosen vectors. Since the cones span their Hilbert spaces and their conjugations fix them pointwise, \(V_eJ_{1,e}=J_{2,e}V_e\).

If \(f\le e\) are in \(\mathcal E\), intertwining of \(\pi_i(f)\) and of the conjugations gives
\[
 V_e Q_{1,f}=Q_{2,f}V_e\quad\text{on }K_{1,e}.
 \tag{SE.33}
\]
Thus \(V_e\) maps \(K_{1,f}\) onto \(K_{2,f}\). Its restriction maps the intersection cones onto one another and intertwines \(fMf\). Uniqueness identifies this restriction with \(V_f\). These statements check both range and cone equality, not merely inclusion of the corner spaces.

Directedness and (SE.33) define a single linear isometry on \(\bigcup_eK_{1,e}\). Its range contains \(\bigcup_eK_{2,e}\), so completeness and (SE.30) extend it to a surjective unitary \(V\). It intertwines the conjugations there by continuity. If \(\xi\in P_1\), the vectors \(Q_{1,e}\xi\) are in the local cones and converge to \(\xi\); their images are in \(P_2\). Closedness gives \(VP_1\subset P_2\), and the same argument for the inverse proves equality.

To prove the identity for the whole algebra, fix \(\eta\in K_{1,e}\) and \(x\in M\). For \(f\in\mathcal E\) above \(e\), the local intertwining gives
\[
 V\pi_1(fxf)\eta=\pi_2(fxf)V\eta.
 \tag{SE.34}
\]
Both normal representations send \(f\uparrow1\) to strongly increasing projections with supremum \(I\). Hence \(\pi_i(fxf)\to\pi_i(x)\) strongly, with norms bounded by \(\|x\|\). Pass to the limit in (SE.34), then use density of the union of the corners. This proves the algebra identity in (SE.31). Uniqueness is SE-01, completing the proof. \(\square\)

Compositions of these unitaries implement compositions of isomorphisms and map the cones onto each other, so uniqueness makes the construction compatible with composition and inverses. It also proves that every arbitrary axiomatic standard form is equivalent to the form produced by any n.s.f. weight: WH-13 supplies such a weight, and SF-05 supplies its standard form. This conclusion is obtained after the local patching argument, not used to justify it.

<span id="oa-mod-se-11--transporting-positive-functionals-and-automorphisms"></span>
<span id="OA-MOD-SE-11"></span>
<span id="oa-mod-se-11"></span>
## OA-MOD-SE-11 — Transporting positive functionals and automorphisms

In every axiomatic standard form, each \(\omega\in M_*^+\) has a unique representative \(\xi_\omega\in P\) with
\[
 \omega(x)=\langle x\xi_\omega,\xi_\omega\rangle,
 \qquad \|\xi_\omega\|^2=\omega(1).
 \tag{SE.35}
\]
Existence follows by SE-10 from SF-10's weight-constructed form; uniqueness is already (SE.3). In this transport, the equality for all \(x\) follows from the algebra intertwining, and cone membership follows from the onto cone identity. Thus no functional changes when the representation is changed. The inequalities (SE.3), positive homogeneity \(\xi_{c\omega}=\sqrt c\,\xi_\omega\) for \(c\ge0\), and the norm-continuous and bounded monotone-net conclusions of SF-11 hold unchanged.

For a normal automorphism \(\alpha\), let \(u_\alpha\) be SE-10's unique unitary in the given form. Then
\[
 u_\alpha x u_\alpha^*=\alpha(x),\qquad
 u_\alpha J=Ju_\alpha,\qquad
 u_\alpha\xi_\omega=\xi_{\omega\circ\alpha^{-1}},\qquad
 u_{\alpha\beta}=u_\alpha u_\beta.
 \tag{SE.36}
\]
The functional formula follows by evaluating the vector functional of \(u_\alpha\xi_\omega\), and the product formula follows from uniqueness. SF-12's topology proof now applies to every form: convergence of \(\alpha_i\) and \(\alpha_i^{-1}\) pointwise in the predual norm is equivalent to strong convergence of \(u_{\alpha_i}\) to \(u_\alpha\). Indeed (SE.3) applied to (SE.36) proves convergence on cone vectors, hence on \(H\). Conversely, strong convergence of unitaries to a unitary gives strong convergence of their adjoints, and the upper bound in (SE.3) gives predual norm convergence on positive normal functionals in both directions. Decompose a general normal functional into a linear combination of positive ones to finish. This is a specified topology assertion; no completeness assertion for an unspecified uniformity is implicit in it.

The transported cone is intrinsic even when \(M\) is not sigma-finite. A normal positive functional sees one sigma-finite support corner; different functionals need not share a common faithful normal state on the whole algebra.

