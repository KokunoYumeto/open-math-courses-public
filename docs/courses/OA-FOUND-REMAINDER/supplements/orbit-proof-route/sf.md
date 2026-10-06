<span id="the-positive-cone-of-a-standard-representation"></span>
# The positive cone of a standard representation



A normal positive functional has a canonical square-root vector once its representation carries the appropriate cone. Constructing that cone requires more than taking positive elements in a GNS domain: the modular quarter power changes the geometry. We first prove the required duality of multiplication cones, then identify the self-dual cone. Its geometry gives supports and uniqueness before any comparison of weights. A finite matrix-weight construction supplies the comparison and, finally, all normal positive functionals.

The mathematical antecedents are Takesaki, *Theory of Operator Algebras II*, IX.1, especially Definition 1.1, Theorem 1.2, Lemmas 1.3–1.6 and 1.12, and the standard implementation in 1.15–1.17; the finite matrix construction uses the mathematical setting of VIII.3. Arbitrary Hilbert spaces and possibly infinite faithful normal semifinite weights are retained throughout. No faithful state on the whole algebra is assumed.

<span id="oa-mod-sf-01--objects-conventions-and-exact-inputs"></span>
<span id="OA-MOD-SF-01"></span>
<span id="oa-mod-sf-01"></span>
## OA-MOD-SF-01 — Objects, conventions and exact inputs

Let \(\varphi\) be a normal semifinite faithful weight on a concrete von Neumann algebra \(M\). Use its faithful normal GNS representation to identify \(M\) with its image on \(H\), as justified by WG-007/010 and WH-02 with BA-01. Inner products are linear in their first variable.

Write
\[
 \mathcal A=\Lambda_\varphi(\mathfrak n_\varphi\cap\mathfrak n_\varphi^*),
 \qquad S=\overline{\sharp},\quad F=S^*,\quad
 S=J\Delta^{1/2},\quad F=J\Delta^{-1/2}.
 \tag{SF.1}
\]
WH-09–11 makes \(\mathcal A\) a full left Hilbert algebra. Let \(\mathcal D\) be its full right algebra. Write \(\lambda_\xi\) for a left-bounded multiplier and \(R_\eta\) for a right-bounded multiplier. On the algebras, \(\xi\zeta=\lambda_\xi\zeta\) and \(\eta\theta=R_\theta\eta\); their involutions are \(\sharp=S\) and \(\flat=F\). WH-03–04 gives
\[
 \lambda_\xi\eta=R_\eta\xi,\qquad
 \lambda_{x\xi}=x\lambda_\xi,
 \qquad
 \lambda(\mathcal A)=\mathfrak n_l\cap\mathfrak n_l^* .
 \tag{SF.2}
\]
The last identity includes the adjoint formula and injectivity.

The exact advanced inputs are MF-05–09: \(JMJ=M'\), modular covariance, the common analytic algebra \(\mathcal A_0\), Gaussian graph approximation with bounded multipliers, and its product/core properties. HAP-05 supplies bounded strong* approximation from a nondegenerate algebra, and HAP-08 supplies central conjugation. RD-06 supplies the product graph-core pairing criterion, and HA-07 supplies closed affiliated multipliers, also applied to the opposite right algebra. QF-03–04 supplies representation and symmetry of closed positive forms. SK-05 and SK-07–09 supply all spectral domains, transport and cutoffs. MA-03 and MA-16 supply Gaussian averages for arbitrary Hilbert vectors. CP-06–08 supplies predual norms, vector functionals and positive spanning; CP-12 supplies support projections. WH-13 supplies an n.s.f. weight on any corner when needed.

Each use is at the exact stated level. In particular, the positive symmetric form bridge in SF-02 is proved here rather than hidden inside a general closed-form theorem. No relative modular or cocycle theorem is a prerequisite of this unit.

For \(C\subset H\), put
\[
 C^\vee=\{\eta\in H : \langle\xi,\eta\rangle
                    \text{ is real and nonnegative for all }\xi\in C\}.
 \tag{SF.3}
\]
This is complex Hilbert-space cone duality, not a dual using only real parts on all of \(H\). Norm closures below are in \(H\). A cone is closed under addition and nonnegative real scalar multiplication. The zero algebra and zero Hilbert space cause no exception to any formula.

<span id="oa-mod-sf-02--a-positive-symmetric-multiplier-has-a-positive-extension"></span>
<span id="OA-MOD-SF-02"></span>
<span id="oa-mod-sf-02"></span>
## OA-MOD-SF-02 — A positive symmetric multiplier has a positive extension

**Lemma.** A densely defined positive symmetric operator \(T\) has a positive self-adjoint extension obtained from closure of its quadratic form. If \(T\) is closed and affiliated with \(M\), this extension is affiliated with \(M\).

**Proof.** On \(D(T)\), put
\[
 q(u,v)=\langle Tu,v\rangle,\qquad
 \langle u,v\rangle_V=\langle u,v\rangle+q(u,v).
 \tag{SF.4}
\]
Positivity and polarization give a Hermitian positive form and its Cauchy–Schwarz inequality. Complete this inner-product space to \(V\). The inclusion into \(H\) extends to a contraction \(j:V\to H\). We claim \(j\) is injective. If \(v\in\ker j\), choose \(u_n\in D(T)\) converging to \(v\) in \(V\). Then \(u_n\to0\) in \(H\). For \(w\in D(T)\), symmetry gives
\[
 \langle u_n,w\rangle_V=\langle u_n,(I+T)w\rangle_H\longrightarrow0.
\]
Thus \(v\) is orthogonal in \(V\) to its dense subspace \(D(T)\), so \(v=0\).

Identify \(V\) with \(j(V)\subset H\) and extend \(q\) there by
\(\bar q(u,v)=\langle j^{-1}u,j^{-1}v\rangle_V-\langle u,v\rangle_H\).
This form is nonnegative, by limits from \(D(T)\), and closed by completeness of \(V\). Its domain is dense in \(H\). This constructs the form closure, including its embedding; it does not assume that a Hilbert-space limit alone determines a form limit.

QF-03 gives its positive self-adjoint operator \(h\). For \(u\in D(T)\) and \(v\in D(\bar q)\), approximation of \(v\) in form norm gives
\(\bar q(u,v)=\langle Tu,v\rangle\). The operator-domain characterization in QF-03 therefore gives \(u\in D(h)\) and \(hu=Tu\).

If \(T\) is affiliated with \(M\), every unitary \(w\in M'\) preserves \(D(T)\) and \(q\). It acts isometrically on \(V\), also with inverse \(w^*\), and the extended action agrees with \(w\) under \(j\). Thus it preserves the closed form and its domain. QF-04 implies \(whw^*=h\). Its spectral projections belong to \(M\), proving affiliation. \(\square\)

We will apply the lemma to the closed positive symmetric extension of an initially defined multiplier. Positivity passes through graph closure, so this application has all the stated hypotheses.

<span id="oa-mod-sf-03--the-two-multiplication-cones-are-dual"></span>
<span id="OA-MOD-SF-03"></span>
<span id="oa-mod-sf-03"></span>
## OA-MOD-SF-03 — The two multiplication cones are dual

Define
\[
 C_l=\overline{\{\xi S\xi:\xi\in\mathcal A\}},\qquad
 C_r=\overline{\{\eta F\eta:\eta\in\mathcal D\}}.
 \tag{SF.5}
\]
Both sets are initially defined as closures of square sets. Their convexity will follow from the theorem, so it is not assumed in its proof.

**Theorem.**
\[
 C_l=C_r^\vee,\qquad C_r=C_l^\vee.
 \tag{SF.6}
\]
They are closed pointed convex cones, \(S\) fixes \(C_l\), \(F\) fixes \(C_r\), and
\[
 JC_l=C_r,\qquad \Delta^{1/2}C_l=C_r.
 \tag{SF.7}
\]

**Proof of the duality.** For \(\xi\in\mathcal A,\eta\in\mathcal D\), move the left and right bounded multipliers in
\(\langle\lambda_\xi S\xi,R_{F\eta}\eta\rangle\):
\[
 \langle\xi S\xi,\eta F\eta\rangle
 =\langle R_\eta\lambda_\xi S\xi,\eta\rangle
 =\langle\lambda_\xi R_\eta S\xi,\eta\rangle
 =\langle\lambda_\xi\lambda_\xi^*\eta,\eta\rangle
 =\|\lambda_\xi^*\eta\|^2\ge0.
 \tag{SF.8}
\]
Here \(R_\eta S\xi=\lambda_{S\xi}\eta=\lambda_\xi^*\eta\). Thus \(C_l\subseteq C_r^\vee\).

Take \(\zeta\in C_r^\vee\). The map
\[
 B(\eta,\theta)=\langle\zeta,\theta F\eta\rangle
 \quad(\eta,\theta\in\mathcal D)
\]
is sesquilinear, with nonnegative diagonal. Its Hermitian symmetry gives
\(\langle\theta F\eta,\zeta\rangle=\langle\zeta,\eta F\theta\rangle\).
This is exactly RD-06's pairing criterion applied to the opposite right algebra. Its closed involution is \(F\), its adjoint is \(S\), and its product is reversed. Hence \(\zeta\in D(S)\) and \(S\zeta=\zeta\).

Mirrored HA-07 says that
\[
 T_0\eta=R_\eta\zeta,\qquad \eta\in\mathcal D,
\]
is closable, its closure \(T\) is affiliated with \(M\), and its adjoint contains the same test formula because \(S\zeta=\zeta\). Moreover
\[
 \langle T_0\eta,\eta\rangle
 =\langle\zeta,R_\eta^*\eta\rangle
 =\langle\zeta,\eta F\eta\rangle\ge0.
\]
Thus \(T\) is positive symmetric. SF-02 supplies a positive self-adjoint affiliated extension \(h\). Put \(E_n=1_{[0,n]}(h)\in M\). Since \(R_\eta\in M'\), for \(\eta\in\mathcal D\),
\[
 R_\eta E_n\zeta=E_nR_\eta\zeta=E_nh\eta.
 \tag{SF.9}
\]
The right side is a bounded operator applied to \(\eta\). Therefore \(\zeta_n=E_n\zeta\) is left bounded and \(\lambda_{\zeta_n}=E_nh\ge0\). The adjoint/ideal intersection in WH-03 puts \(\zeta_n\) in \(\mathcal A\), with \(S\zeta_n=\zeta_n\). Spectral convergence gives \(\zeta_n\to\zeta\).

We now show that every left-bounded vector \(\theta\) with positive multiplier \(a=\lambda_\theta\) belongs to \(C_l\). WH-11 identifies \(\theta=\Lambda_\varphi(a)\) and gives \(\varphi(a^2)=\|\theta\|^2<\infty\). Set
\[
 p_n=1_{[1/n,\infty)}(a),\qquad c_n=p_n a^{1/2}.
\]
The inequality \(c_n^2\le n a^2\) gives \(c_n=c_n^*\in\mathfrak n_\varphi\). For \(\xi_n=\Lambda_\varphi(c_n)\in\mathcal A\),
\[
 \xi_n S\xi_n=\Lambda_\varphi(c_n^2)
             =p_n\Lambda_\varphi(a)=p_n\theta.
 \tag{SF.10}
\]
If \(p=s(a)\), then \(\lambda_{(1-p)\theta}=0\); injectivity gives \(p\theta=\theta\). Hence \(p_n\theta\to\theta\), proving the claim. Apply it to each \(\zeta_n\), then take the limit to obtain \(\zeta\in C_l\). This proves \(C_l=C_r^\vee\). The proved argument applied to \(\mathcal D^{\mathrm{op}}\) gives \(C_r=C_l^\vee\); the weight and GNS identification needed in its square-approximation step are WH-08/12's canonical right-hand construction.

Dual sets in (SF.3) are closed convex cones. The square spans are dense: the complex polarization identity spans \(\mathcal A^2\) by the left squares, and MF-09/RD-06 gives density; the same holds on the right. If both \(v,-v\) belong to one cone, duality forces \(v\) orthogonal to the dense span of the other, so \(v=0\).

Each left square is \(S\)-fixed. Passing to limits in its closed graph gives \(C_l\subset D(S)\), \(S|_{C_l}=I\); similarly \(F\) fixes \(C_r\). MF's product reversal sends the left square set to the right square set, so \(JC_l=C_r\). Finally \(\Delta^{1/2}\xi=JS\xi=J\xi\) on \(C_l\), proving (SF.7). \(\square\)

<span id="oa-mod-sf-04--quarter-powers-produce-a-self-dual-cone"></span>
<span id="OA-MOD-SF-04"></span>
<span id="oa-mod-sf-04"></span>
## OA-MOD-SF-04 — Quarter powers produce a self-dual cone

Define the natural cone by
\[
 P_\varphi=\overline{\{q(\xi):\xi\in\mathcal A_0\}},
 \qquad q(\xi)=\lambda_\xi J\xi=\xi J\xi.
 \tag{SF.11}
\]
All products here are permitted by MF-07. Then
\[
 P_\varphi=\overline{\Delta^{1/4}C_l}
          =\overline{\Delta^{-1/4}C_r},\qquad
 P_\varphi=P_\varphi^\vee.
 \tag{SF.12}
\]
It is a closed convex cone, \(J\) fixes it pointwise, and
\(\Delta^{it}P_\varphi=P_\varphi\) for every real \(t\).

**Proof of the descriptions.** On \(\mathcal A_0\), MF-07's analytic product identity and \(S=J\Delta^{1/2}\) give
\[
 \Delta^{1/4}(\xi S\xi)
 =(\Delta^{1/4}\xi)\,J(\Delta^{1/4}\xi).
 \tag{SF.13}
\]
The map \(\Delta^{1/4}\) maps \(\mathcal A_0\) bijectively onto itself. MF-08's Gaussian approximants \(\xi_r\) converge to \(\xi\in\mathcal A\) together with \(S\xi_r\), and their left multipliers converge strongly with a uniform bound. Thus \(\xi_rS\xi_r\to\xi S\xi\). Analytic squares are consequently dense in \(C_l\).

For \(\theta_n,\theta\in C_l\) with \(\theta_n\to\theta\), SF-03 gives
\(\Delta^{1/2}(\theta_n-\theta)=J(\theta_n-\theta)\to0\).
Spectral Cauchy–Schwarz gives
\[
 \|\Delta^{1/4}(\theta_n-\theta)\|^2
 \le\|\Delta^{1/2}(\theta_n-\theta)\|\,\|\theta_n-\theta\|
 \longrightarrow0.
\]
Combining this with (SF.13) gives the first closure description. The right-hand argument gives the second, or use
\(\Delta^{1/2}C_l=C_r\). These are images of convex cones under a linear operator defined on the whole cone, so their closures are convex.

For \(\xi\in\mathcal A_0\), the multiplier conjugation identity gives
\(Jq(\xi)=(J\lambda_\xi J)\xi=R_{J\xi}\xi=q(\xi)\).
Also
\(\Delta^{it}q(\xi)=q(\Delta^{it}\xi)\).
Thus \(J\) fixes \(P_\varphi\), and real modular powers preserve it in both directions.

**Proof of self-duality.** For \(\theta\in C_l,\eta\in C_r\), the spectral pairing identity gives
\[
 \langle\Delta^{1/4}\theta,\Delta^{-1/4}\eta\rangle
 =\langle\theta,\eta\rangle\ge0.
\]
It is justified first on bounded spectral bands and then by convergence in each specified domain. The two closure descriptions imply \(P_\varphi\subseteq P_\varphi^\vee\).

Conversely, suppose \(\zeta\in P_\varphi^\vee\). Define
\[
 \zeta_r=\sqrt{r/\pi}\int_{\mathbb R}e^{-rt^2}\Delta^{it}\zeta\,dt
        =g_r(\Delta)\zeta,\qquad
 g_r(s)=e^{-(\log s)^2/(4r)} .
 \tag{SF.14}
\]
MA-16 and SK give every real-power domain of \(\zeta_r\) and \(\zeta_r\to\zeta\). Positivity of the scalar kernel and real modular invariance give \(\zeta_r\in P_\varphi^\vee\). For an analytic right square \(\eta F\eta\),
\[
 \langle\Delta^{-1/4}\zeta_r,\eta F\eta\rangle
 =\langle\zeta_r,\Delta^{-1/4}(\eta F\eta)\rangle\ge0.
\]
Analytic right squares are dense in \(C_r\). SF-03 implies
\(\Delta^{-1/4}\zeta_r\in C_l\), so \(\zeta_r\in P_\varphi\).
Closedness now gives \(\zeta\in P_\varphi\), proving (SF.12). \(\square\)

The same cone is obtained by closing \(q(\mathcal A)\): Gaussian approximation has both \(\xi_r\to\xi\) and uniformly bounded \(\lambda_{\xi_r}\to\lambda_\xi\), so \(q(\xi_r)\to q(\xi)\). This larger generating set is useful when comparing weights.

<span id="oa-mod-sf-05--the-standard-form-axioms"></span>
<span id="OA-MOD-SF-05"></span>
<span id="oa-mod-sf-05"></span>
## OA-MOD-SF-05 — The standard-form axioms

For every \(x\in M\) and \(z\in Z(M)\),
\[
 JMJ=M',\qquad JzJ=z^*,\qquad
 J\xi=\xi\ (\xi\in P_\varphi),\qquad
 xJxJ\,P_\varphi\subseteq P_\varphi .
 \tag{SF.15}
\]

The first identity is MF-05, the central identity is the fully proved HAP-08, and pointwise fixedness is SF-04. To prove the final inclusion, first take \(x=\lambda_a\), \(a\in\mathcal A_0\). Commutant membership and the analytic product identities give
\[
 \lambda_aJ\lambda_aJ\,q(\xi)
 =\lambda_a\lambda_\xi J(\lambda_a\xi)
 =q(a\xi)\in P_\varphi
 \quad(\xi\in\mathcal A_0).
\]
Continuity extends this to the closed cone. The algebra \(\lambda(\mathcal A_0)\) is nondegenerate and generates \(M\), by MF-09. HAP-05 supplies a net \(x_i\) from that algebra with \(x_i\to x\) strongly* and \(\|x_i\|\le\|x\|\). Therefore \(x_iJx_iJ\to xJxJ\) strongly, by the uniform bounds and fixed-vector estimates for products. Closedness of the cone gives the desired inclusion.

This proof does not assert that \(x\xi\) lies in the finite-star algebra for arbitrary \(x\in M\). That domain need not be a left ideal. Approximation is applied to bounded operators acting on fixed cone vectors.

A quadruple satisfying (SF.15) with a self-dual cone is called a standard form. We have therefore constructed a standard form for every n.s.f. weight and, by WH-13, for every von Neumann algebra. Starting from any left Hilbert algebra gives the same conclusion after WH-03–08's full completion and canonical weight construction.

<span id="oa-mod-sf-06--real-decomposition-and-orthogonal-supports"></span>
<span id="OA-MOD-SF-06"></span>
<span id="oa-mod-sf-06"></span>
## OA-MOD-SF-06 — Real decomposition and orthogonal supports

Let \(P=P_\varphi\) and \(H_J=\{\xi:J\xi=\xi\}\), a real Hilbert space. Every \(v\in H_J\) has a unique decomposition
\[
 v=v_+-v_-,\qquad v_\pm\in P,\qquad
 \langle v_+,v_-\rangle=0.
 \tag{SF.16}
\]
Consequently every vector in \(H\) is a complex linear combination of four cone vectors.

Here are the needed projection details. A minimizing sequence for the distance from \(v\) to a nonempty closed convex set is Cauchy, by the parallelogram identity applied to its midpoints. Its limit is the unique closest point \(p\). For the cone \(P\), comparison with \(tp\), \(t\ge0\), gives \(\langle v-p,p\rangle=0\). Comparison with \(p+t\eta\), \(t\ge0,\eta\in P\), gives \(\langle v-p,\eta\rangle\le0\). Thus \(m=p-v\) belongs to the real dual cone in \(H_J\), which is \(P\) by SF-04, and \(p\perp m\). Conversely, if \(v=p-m\) with \(p,m\in P\) orthogonal, then for every \(\eta\in P\),
\[
 \|v-\eta\|^2=\|p-\eta\|^2+\|m\|^2+2\langle\eta,m\rangle
 \ge\|m\|^2,
\]
with equality only at \(\eta=p\). This proves uniqueness. Apply (SF.16) to
\((v+Jv)/2\) and \((v-Jv)/(2i)\) to obtain the spanning assertion.

For \(\xi\in H\), write \(\omega_\xi(x)=\langle x\xi,\xi\rangle\). This is a bounded positive normal functional by CP. Its support \(e_\xi=s_M(\omega_\xi)\) is the projection onto \(\overline{M'\xi}\). Indeed that subspace reduces \(M'\), so its projection belongs to \(M\), and it is the smallest projection of \(M\) fixing \(\xi\). A projection \(e\) fixes \(\xi\) exactly when \(\omega_\xi(1-e)=0\). For \(\xi\in P\), \(J\xi=\xi\) consequently gives
\[
 \overline{M'\xi}=e_\xi H,\qquad
 \overline{M\xi}=Je_\xi JH.
 \tag{SF.17}
\]

**Orthogonality theorem.** For \(\xi,\eta\in P\),
\[
 \langle\xi,\eta\rangle=0
 \quad\Longleftrightarrow\quad e_\xi e_\eta=0.
 \tag{SF.18}
\]

The reverse implication follows because \(e_\xi\xi=\xi\), \(e_\eta\eta=\eta\). For the forward implication, fix \(x\in M\). Cone invariance and self-duality imply, for every complex \(t\),
\[
 0\le\langle(1+tx)J(1+tx)J\xi,\eta\rangle
 =2\operatorname{Re}\bigl(t\langle x\xi,\eta\rangle\bigr)
   +|t|^2\langle xJxJ\xi,\eta\rangle .
 \tag{SF.19}
\]
To check the linear terms, use antiunitarity and \(J\xi=\xi,J\eta=\eta\), which give
\(\langle JxJ\xi,\eta\rangle=\overline{\langle x\xi,\eta\rangle}\).
Small \(t\) with arbitrary phase in (SF.19) forces \(\langle x\xi,\eta\rangle=0\). Thus \(\eta\perp M\xi\), so \(Je_\xi J\eta=0\) by (SF.17). Applying \(J\) gives \(e_\xi\eta=0\). The support characterization yields \(e_\eta\le1-e_\xi\). This proves (SF.18), without assuming that all normal functionals have cone representatives.

<span id="oa-mod-sf-07--norm-estimates-and-uniqueness-before-existence"></span>
<span id="OA-MOD-SF-07"></span>
<span id="oa-mod-sf-07"></span>
## OA-MOD-SF-07 — Norm estimates and uniqueness before existence

For \(\xi,\eta\in P\),
\[
 \|\xi-\eta\|^2
 \le\|\omega_\xi-\omega_\eta\|
 \le\|\xi-\eta\|\,\|\xi+\eta\|.
 \tag{SF.20}
\]
In particular the map \(\xi\mapsto\omega_\xi\) is injective.

**Proof.** Put \(d=\xi-\eta\), \(s=\xi+\eta\), and let \(d=p-m\) be (SF.16). By (SF.18), \(e_p e_m=0\), so \(a=e_p-e_m\) is a self-adjoint contraction and \(ad=p+m\). The case \(d=0\) is immediate; no assertion that \(\|a\|=1\) is needed. For \(\delta=\omega_\xi-\omega_\eta\),
\[
 \delta(a)=\operatorname{Re}\langle as,d\rangle
 =\langle s,p+m\rangle
 =\|d\|^2+2\langle\xi,m\rangle+2\langle\eta,p\rangle
 \ge\|d\|^2 .
\]
All cone pairings are real nonnegative. Since \(\|a\|\le1\), this proves the lower bound.

The norm of a Hermitian functional is its supremum on self-adjoint contractions. To verify this, for an arbitrary contraction \(b\), choose a scalar of modulus one making \(\delta(b)\) real nonnegative; its real part is a self-adjoint contraction with the same functional value. For such a self-adjoint \(b\), polarization gives
\[
 \delta(b)=\operatorname{Re}\langle bs,d\rangle,
\]
whose absolute value is at most \(\|s\|\|d\|\). This proves the upper bound. \(\square\)

It follows already that a cone-preserving intertwining unitary between two representations equipped with these cones is unique. If \(U_1,U_2:H_2\to H_1\) are two such unitaries, then \(V=U_2^*U_1\) commutes with the represented algebra on \(H_2\) and maps its cone onto itself. For \(\xi\) in that cone, \(\omega_{V\xi}=\omega_\xi\). Inequality (SF.20) gives \(V\xi=\xi\). Cone spanning from SF-06 gives \(V=I\).

<span id="oa-mod-sf-08--a-finite-matrix-weight-and-its-four-closed-graphs"></span>
<span id="OA-MOD-SF-08"></span>
<span id="oa-mod-sf-08"></span>
## OA-MOD-SF-08 — A finite matrix weight and its four closed graphs

Let \(\varphi_1,\varphi_2\) be n.s.f. weights on \(M\). On \(N=M_2(M)\), define
\[
 \rho(X)=\varphi_1(X_{11})+\varphi_2(X_{22})
 \quad(X\in N_+).
 \tag{SF.21}
\]
This is a finite amplification construction; no general tensor-product-weight theorem is used.

Each diagonal compression is positive linear and preserves increasing positive suprema. Thus additivity, homogeneity and normality of \(\rho\) follow directly from those of the two weights, with infinite values retained. If \(\rho(X)=0\) for \(X\ge0\), faithfulness makes both diagonal corners zero. Writing \(X=Y^*Y\), its diagonal entries are sums of positive \(Y_{ki}^*Y_{ki}\), so all entries of \(Y\) vanish. Thus \(\rho\) is faithful.

The finite left ideal is exactly
\[
 \mathfrak n_\rho=
 \{X:X_{ij}\in\mathfrak n_{\varphi_j}\text{ for }i,j=1,2\}.
 \tag{SF.22}
\]
Indeed \(\rho(X^*X)=\sum_{i,j}\varphi_j(X_{ij}^*X_{ij})\).
If \(e_\alpha^{(j)}\) are WG-008's finite positive contraction nets for the two weights, their diagonal matrices form a finite positive contraction net for \(\rho\) converging strongly to \(1_N\). WG-008's converse proves semifiniteness. WH therefore supplies its full GNS Hilbert algebra and closed involution.

For precision, denote a copy of \(H_j=H_{\varphi_j}\) in position \((i,j)\) by \(H_{ij}\). The GNS map identifies its Hilbert space with the four orthogonal slots
\[
 H_\rho=\bigoplus_{i,j=1}^2 H_{ij},\qquad
 \Lambda_\rho(X)_{ij}=\Lambda_{\varphi_j}(X_{ij}).
 \tag{SF.23}
\]
The norm identity above and density of every separate GNS range prove this unitary identification. The algebra action is
\[
 (\pi_\rho(A)v)_{ij}=\sum_{k=1}^2\pi_{\varphi_j}(A_{ik})v_{kj}.
 \tag{SF.24}
\]

Let \(P_{ij}\) be the orthogonal slot projections. On the full finite-star core,
\[
 S_{\rho,0}P_{ij}=P_{ji}S_{\rho,0},
 \qquad
 X_{ij}\in\mathfrak n_{\varphi_j}
               \cap\mathfrak n_{\varphi_i}^* .
 \tag{SF.25}
\]
A single-entry matrix has exactly this domain condition. Since both slot projections are bounded, applying them to a convergent graph sequence gives
\(S_\rho P_{ij}=P_{ji}S_\rho\) on \(D(S_\rho)\). Conversely, graph approximation of a vector in one slot followed by \(P_{ij}\) shows that the corresponding restriction is precisely the closure of the initial map
\[
 T_{ij,0}\Lambda_{\varphi_j}(x)
       =\Lambda_{\varphi_i}(x^*),
 \quad x\in\mathfrak n_{\varphi_j}
                 \cap\mathfrak n_{\varphi_i}^* .
 \tag{SF.26}
\]
Thus its domain is dense, its closure \(T_{ij}:H_j\to H_i\) is closed antilinear, and its domain is the actual closure of this graph, not a formal common-domain declaration.

The closed involution \(S_\rho^2=I\) shows that \(T_{ji}=T_{ij}^{-1}\), including domains and ranges. The quadratic form of \(S_\rho\) is an orthogonal sum of its four slot forms, because different slots are sent to different slots. Hence \(\Delta_\rho=S_\rho^*S_\rho\) reduces every slot, and its restriction on \(H_{ij}\) is a positive injective self-adjoint operator \(D_{ij}\). Its half-power has domain \(D(T_{ij})\). Polar decomposition gives
\[
 T_{ij}=K_{ij}D_{ij}^{1/2},
 \tag{SF.27}
\]
where \(K_{ij}:H_j\to H_i\) is antiunitary. Indeed \(T_{ij}\) has zero kernel and dense range, as follows from the inverse and dense-domain assertions. The polar antiunitary \(J_\rho\) sends slot \((i,j)\) to \((j,i)\) by \(K_{ij}\). Since \(J_\rho^2=I\), \(K_{ji}=K_{ij}^{-1}\). On the diagonal,
\[
 T_{jj}=S_{\varphi_j},\qquad K_{jj}=J_{\varphi_j},
 \qquad D_{jj}=\Delta_{\varphi_j}.
\]

Apply MF-05 to \(\rho\). Then
\(Q=J_\rho\pi_\rho(e_{12})J_\rho\in\pi_\rho(N)'\).
Its action maps column \(2\) to column \(1\), leaving the row fixed. In row \(i\) its coefficient is
\[
 U_i=K_{1i}K_{i2}:H_2\longrightarrow H_1.
\]
This follows by applying in order the three factors defining \(Q\): slot \((i,2)\) goes to \((2,i)\), then \((1,i)\), then \((i,1)\).
Commutation with \(\pi_\rho(e_{21})\) gives \(U_1=U_2\); commutation with \(\pi_\rho(\operatorname{diag}(x,x))\) gives
\[
 U:=J_{\varphi_1}K_{12}=K_{12}J_{\varphi_2},
 \qquad U\pi_{\varphi_2}(x)=\pi_{\varphi_1}(x)U.
 \tag{SF.28}
\]
The map \(U\) is unitary, being a product of antiunitaries. This proves the needed representation equivalence from a finite matrix weight and the already established modular commutant theorem.

<span id="oa-mod-sf-09--canonical-comparison-of-the-positive-cones"></span>
<span id="OA-MOD-SF-09"></span>
<span id="oa-mod-sf-09"></span>
## OA-MOD-SF-09 — Canonical comparison of the positive cones

Write \(\varphi=\varphi_1\), \(\psi=\varphi_2\), and retain the indices of SF-08. The unitary \(U:H_\psi\to H_\varphi\) in (SF.28) satisfies
\[
 UJ_\psi=J_\varphi U,\qquad UP_\psi=P_\varphi.
 \tag{SF.29}
\]
The first identity follows by multiplying either expression for \(U\) by the indicated conjugation. We prove the cone assertion directly, including the relative-operator domain which it uses.

Put \(\mathfrak a_\chi=\mathfrak n_\chi\cap\mathfrak n_\chi^*\) and
\(g_\chi(x)=\pi_\chi(x)J_\chi\Lambda_\chi(x)\), \(x\in\mathfrak a_\chi\).
By SF-04 these vectors generate \(P_\chi\) after closure. For \(x\in\mathfrak a_\varphi\), \(y\in\mathfrak a_\psi\), the left-ideal property gives
\[
 y^*x\in\mathfrak n_\varphi\cap\mathfrak n_\psi^*,
 \qquad x^*y\in\mathfrak n_\psi\cap\mathfrak n_\varphi^*.
 \tag{SF.30}
\]
Thus \(T_{21}\Lambda_\varphi(y^*x)=\Lambda_\psi(x^*y)\) is an equality on the original core of that closed operator.

Use pointwise \(J\)-fixedness of the generators, (SF.28), and commutation of the left algebra with its \(J\)-conjugate. With inner products linear in the first variable, the full calculation is
\[
\begin{aligned}
 \langle g_\varphi(x),Ug_\psi(y)\rangle
 &=\langle J_\varphi\Lambda_\varphi(x),
      U\pi_\psi(x^*)J_\psi\pi_\psi(y)J_\psi\Lambda_\psi(y)\rangle\\
 &=\langle J_\varphi\Lambda_\varphi(x),
      J_\varphi U\pi_\psi(y)J_\psi\Lambda_\psi(x^*y)\rangle\\
 &=\langle U\pi_\psi(y)J_\psi\Lambda_\psi(x^*y),
             \Lambda_\varphi(x)\rangle\\
 &=\langle K_{12}\Lambda_\psi(x^*y),\Lambda_\varphi(y^*x)\rangle\\
 &=\langle D_{21}^{1/2}\Lambda_\varphi(y^*x),
             \Lambda_\varphi(y^*x)\rangle\ge0.
\end{aligned}
 \tag{SF.31}
\]
The penultimate equality uses \(UJ_\psi=K_{12}\). The last uses
\(K_{12}T_{21}=K_{21}^{-1}K_{21}D_{21}^{1/2}\), with the domain already checked in (SF.30). This is positivity of an operator on \(H_\varphi\), not on \(H_\psi\).

Taking closures and using self-duality gives \(UP_\psi\subseteq P_\varphi\). Interchanging the weights gives the reverse inclusion: the resulting comparison unitary is \(U^*\), since
\((J_\varphi K_{12})^*=K_{21}J_\varphi=J_\psi K_{21}\).
This proves (SF.29).

Denote this unique cone-preserving intertwiner by \(I_{\varphi\leftarrow\psi}\). SF-07 now gives, without further operator computation,
\[
 I_{\varphi\leftarrow\psi}I_{\psi\leftarrow\chi}
       =I_{\varphi\leftarrow\chi},\qquad
 I_{\varphi\leftarrow\varphi}=1,\qquad
 I_{\varphi\leftarrow\psi}^*=I_{\psi\leftarrow\varphi}.
 \tag{SF.32}
\]
This proves weight independence for the standard forms constructed here.

<span id="oa-mod-sf-10--every-normal-positive-functional-has-a-cone-vector"></span>
<span id="OA-MOD-SF-10"></span>
<span id="oa-mod-sf-10"></span>
## OA-MOD-SF-10 — Every normal positive functional has a cone vector

For each \(\omega\in M_*^+\), there is exactly one \(\xi_\omega\in P_\varphi\) such that
\[
 \omega(x)=\langle\pi_\varphi(x)\xi_\omega,\xi_\omega\rangle
 \quad(x\in M).
 \tag{SF.33}
\]
Uniqueness is SF-07. Here is a construction of existence which does not assume that \(M\) has a faithful normal state.

For \(\omega=0\), take zero. Otherwise let \(e=s_M(\omega)\), \(q=1-e\). The restriction of \(\omega\) to \(eMe\) is faithful, and \(\omega(x)=\omega(exe)\) for every \(x\in M\), by CP's support characterization and Cauchy–Schwarz. Choose an n.s.f. weight \(\tau\) on \(qMq\) by WH-13, using the zero weight on the zero algebra if \(q=0\). Define
\[
 \psi(a)=\omega(eae)+\tau(qaq),\qquad a\in M_+.
 \tag{SF.34}
\]
This is a normal weight. If \(\psi(a)=0\), faithfulness on the two corners gives \(eae=qaq=0\); applying these equalities to \(a^{1/2}\) gives \(a^{1/2}e=a^{1/2}q=0\), hence \(a=0\). If \(f_i\) are finite positive contractions for \(\tau\) tending strongly to \(q\), the finite positive contractions \(e+f_i\) tend strongly to \(1\). WG-008 proves that \(\psi\) is semifinite.

In particular \(e\in\mathfrak a_\psi\). Set \(\zeta=\Lambda_\psi(e)\). It represents \(\omega\), since
\[
 \langle\pi_\psi(x)\zeta,\zeta\rangle
 =\widetilde\psi(exe)=\omega(exe)=\omega(x).
 \tag{SF.35}
\]
The finite linear extension \(\widetilde\psi\) is legitimate here: both \(xe\) and \(e\) belong to \(\mathfrak n_\psi\).

We check that \(\zeta\) is a cone vector, rather than inferring that fact from (SF.35). Right multiplication by \(e\) defines a bounded map on the GNS range, because for \(a\in\mathfrak n_\psi\),
\[
 \psi((ae)^*ae)=\omega(ea^*ae)\le\psi(a^*a).
\]
Its extension \(R_e\) is a projection. It is self-adjoint: for \(a,b\in\mathfrak n_\psi\), the two finite products \(b^*ae\) and \(eb^*a\) have equal \(\widetilde\psi\)-values, both \(\omega(eb^*ae)\). To justify this directly, the diagonal compression formula (SF.34) extends linearly to the finite algebra \(\mathfrak m_\psi\); the \(q\)-corner of both products is zero. Polarization therefore gives
\(\langle R_e\Lambda_\psi(a),\Lambda_\psi(b)\rangle
=\langle\Lambda_\psi(a),R_e\Lambda_\psi(b)\rangle\).

On the full Hilbert algebra, \(R_e\Lambda_\psi(a)=\lambda_{\Lambda_\psi(a)}\zeta\). Thus \(\zeta\) is right bounded, with self-adjoint right multiplier. The right-hand full-algebra characterization RD-07, using RD-06's pairing test, yields \(\zeta\in D(F_\psi)\) and \(F_\psi\zeta=\zeta\). Also \(S_\psi\zeta=\zeta\), because \(e=e^*\). Consequently \(\zeta\in D(\Delta_\psi)\) and \(\Delta_\psi\zeta=\zeta\).

The left multiplier of \(\zeta\) is the positive projection \(\pi_\psi(e)\), so SF-03 gives \(\zeta\in C_l\). SF-04 and the preceding fixed-vector identity give
\(\zeta=\Delta_\psi^{1/4}\zeta\in P_\psi\).
Now take
\[
 \xi_\omega=I_{\varphi\leftarrow\psi}\zeta.
\]
By SF-09 this belongs to \(P_\varphi\), and its represented functional is (SF.35). This proves (SF.33) in arbitrary dimension. The auxiliary choices disappear by uniqueness.

<span id="oa-mod-sf-11--norm-topology-supports-and-monotone-limits"></span>
<span id="OA-MOD-SF-11"></span>
<span id="oa-mod-sf-11"></span>
## OA-MOD-SF-11 — Norm topology, supports and monotone limits

The map \(P_\varphi\to M_*^+\), \(\xi\mapsto\omega_\xi\), is a homeomorphism for the Hilbert norm and the predual norm. Its inverse satisfies
\[
 \|\xi_\omega-\xi_\nu\|\le\|\omega-\nu\|^{1/2},\qquad
 \|\xi_\omega\|^2=\omega(1),\qquad
 \xi_{c\omega}=\sqrt c\,\xi_\omega\quad(c\ge0).
 \tag{SF.36}
\]
These statements follow respectively from SF-07, evaluation at the identity, and uniqueness. The upper bound in (SF.20) gives continuity in the other direction.

The support of \(\omega\) is exactly the projection onto \(\overline{M'\xi_\omega}\); the projection onto \(\overline{M\xi_\omega}\) is its \(J\)-conjugate. In particular
\[
 \omega\perp\nu\ \text{in the sense }s(\omega)s(\nu)=0
 \quad\Longleftrightarrow\quad
 \langle\xi_\omega,\xi_\nu\rangle=0.
 \tag{SF.37}
\]
This is SF-06, now applicable to every normal positive functional. If \(\omega\) is faithful, its vector is cyclic and separating for \(M\), by the two projection formulas. Conversely, a separating representative has support \(1\), so its functional is faithful.

Let \((\omega_i)\) be an increasing net in \(M_*^+\) with pointwise supremum \(\omega\in M_*^+\). Positivity gives
\[
 \|\omega-\omega_i\|=(\omega-\omega_i)(1)\longrightarrow0,
 \qquad \xi_{\omega_i}\longrightarrow\xi_\omega.
 \tag{SF.38}
\]
The same conclusion holds for a decreasing net with pointwise infimum \(\omega\in M_*^+\), since then \(\omega_i-\omega\ge0\). These are assertions for arbitrary nets, with no countability assumption. The finite value of the limiting functional is part of the increasing-net hypothesis. We do not use a vector to represent an infinite weight: every Hilbert-space vector has the finite value \(\|\xi\|^2\) at \(1\).

Cone order and functional order must be kept distinct. Equations (SF.36)–(SF.38) assert norm continuity along monotone functional nets; they do not assert that \(\xi\mapsto\omega_\xi\) is an order isomorphism. SF-15 below gives a concrete reason.

<span id="oa-mod-sf-12--canonical-implementation-of-automorphisms"></span>
<span id="OA-MOD-SF-12"></span>
<span id="oa-mod-sf-12"></span>
## OA-MOD-SF-12 — Canonical implementation of automorphisms

Every normal automorphism \(\alpha\) of \(M\) has a unique unitary \(u_\alpha\) on \(H_\varphi\) such that
\[
 u_\alpha\pi_\varphi(x)u_\alpha^*=\pi_\varphi(\alpha(x)),
 \qquad u_\alpha P_\varphi=P_\varphi.
 \tag{SF.39}
\]
It commutes with \(J_\varphi\), and
\[
 u_{\alpha\beta}=u_\alpha u_\beta,\qquad
 u_\alpha\xi_\omega=\xi_{\omega\circ\alpha^{-1}}.
 \tag{SF.40}
\]

**Proof.** Put \(\psi=\varphi\circ\alpha^{-1}\), an n.s.f. weight. The formula
\[
 W_\alpha\Lambda_\varphi(x)=\Lambda_\psi(\alpha(x))
 \quad(x\in\mathfrak n_\varphi)
 \tag{SF.41}
\]
defines a unitary from \(H_\varphi\) onto \(H_\psi\): it preserves squared norms by the definition of \(\psi\), and \(\alpha\) maps \(\mathfrak n_\varphi\) onto \(\mathfrak n_\psi\). It intertwines \(\pi_\varphi(x)\) with \(\pi_\psi(\alpha(x))\). It maps the finite-star algebra bijectively onto the finite-star algebra and intertwines the initial involutions. Graph closure and uniqueness of polar decomposition therefore give
\[
 W_\alpha S_\varphi W_\alpha^*=S_\psi,\quad
 W_\alpha J_\varphi W_\alpha^*=J_\psi,\quad
 W_\alpha\Delta_\varphi W_\alpha^*=\Delta_\psi,
\]
including the transported domains. Applying this to the generators \(g_\varphi(x)\) gives \(W_\alpha P_\varphi=P_\psi\). Thus
\(u_\alpha=I_{\varphi\leftarrow\psi}W_\alpha\) satisfies (SF.39) and commutes with \(J_\varphi\).

The ratio of two unitaries satisfying (SF.39) commutes with \(\pi_\varphi(M)\) and preserves its cone. SF-07 makes the ratio the identity. The product \(u_\alpha u_\beta\) satisfies (SF.39) for \(\alpha\beta\), proving the first equality in (SF.40). For \(x\in M\),
\[
 \langle\pi_\varphi(x)u_\alpha\xi_\omega,u_\alpha\xi_\omega\rangle
 =\omega(\alpha^{-1}(x)).
\]
SF-10's uniqueness proves the second equality. \(\square\)

Equip \(\operatorname{Aut}(M)\) with the topology of pointwise predual-norm convergence of both maps
\(\omega\mapsto\omega\circ\alpha\) and \(\omega\mapsto\omega\circ\alpha^{-1}\).
Then \(\alpha\mapsto u_\alpha\) is a topological group isomorphism onto the group of unitaries which normalize \(M\) and preserve \(P_\varphi\), equipped with the strong operator topology.

To check the topological assertion, a net converging in the stated automorphism topology sends every \(\xi_\omega\) to its limiting vector in norm, by (SF.36) and (SF.40). The complex span of these vectors is all of \(H\), and the operators are unitaries. Approximation therefore gives strong convergence on every vector. Conversely, if \(u_{\alpha_i}\to u_\alpha\) strongly, their adjoints converge strongly too, since
\[
 \|(u_{\alpha_i}^*-u_\alpha^*)\eta\|
 =\|\eta-u_{\alpha_i}u_\alpha^*\eta\|\longrightarrow0.
\]
The upper bound of (SF.20), applied to the vectors in (SF.40) and to the inverse automorphisms, proves predual-norm convergence for every positive normal functional. General normal functionals follow by their linear decomposition into positive normal functionals, as in CP's concrete predual description. Finally a cone-preserving normalizing unitary implements a normal automorphism (unitary conjugation preserves increasing positive suprema), and uniqueness identifies it with the corresponding \(u_\alpha\).

In particular, an action of an arbitrary topological group which is continuous in this predual automorphism topology has a canonical strongly continuous unitary implementation. This statement specifies its topology; conversion from other definitions of continuity for actions is a separate question.

<span id="oa-mod-sf-13--one-hilbert-space-for-all-nsf-gns-maps"></span>
<span id="OA-MOD-SF-13"></span>
<span id="oa-mod-sf-13"></span>
## OA-MOD-SF-13 — One Hilbert space for all n.s.f. GNS maps

Fix a base n.s.f. weight \(\varphi\). For every n.s.f. weight \(\psi\), put
\[
 \Lambda_\psi^{\mathrm{std}}(x)
   =I_{\varphi\leftarrow\psi}\Lambda_\psi(x)
 \quad(x\in\mathfrak n_\psi).
 \tag{SF.42}
\]
All these maps take values in the same \(H_\varphi\), have the same represented algebra, and have the same conjugation \(J=J_\varphi\). Their ranges are dense, and each retains exactly its original GNS norm and left-multiplication rule. Equation (SF.32) proves independence of intermediate comparisons.

There are two useful domain-sensitive consequences. First, for a normal automorphism \(\alpha\),
\[
 u_\alpha\Lambda_\psi^{\mathrm{std}}(x)
   =\Lambda_{\psi\circ\alpha^{-1}}^{\mathrm{std}}(\alpha(x))
 \quad(x\in\mathfrak n_\psi).
 \tag{SF.43}
\]
Indeed, conjugate the weight-transport unitary (SF.41), with \(\psi\) in place of \(\varphi\), by the two comparison unitaries. It implements \(\alpha\) on \(H_\varphi\) and maps the cone onto itself. SF-12 identifies it with \(u_\alpha\). In the frequently useful reversed form,
\[
 u_\alpha^*\Lambda_\psi^{\mathrm{std}}(\alpha(x))
 =\Lambda_{\psi\circ\alpha}^{\mathrm{std}}(x),
 \qquad x\in\mathfrak n_{\psi\circ\alpha}.
 \tag{SF.44}
\]
This equality is for arbitrary n.s.f. weights, including weights infinite at the identity.

Second, for n.s.f. weights \(\chi,\psi\), the map
\[
 \Lambda_\psi^{\mathrm{std}}(x)
       \longmapsto\Lambda_\chi^{\mathrm{std}}(x^*),
 \qquad x\in\mathfrak n_\psi\cap\mathfrak n_\chi^*,
 \tag{SF.45}
\]
is densely defined and closable. Its closure is
\[
 S_{\chi,\psi}=J\Delta_{\chi,\psi}^{1/2},
 \qquad
 \Delta_{\chi,\psi}
   =I_{\varphi\leftarrow\psi}D_{\chi,\psi}
        I_{\varphi\leftarrow\psi}^*.
 \tag{SF.46}
\]
Here \(D_{\chi,\psi}\) is SF-08's \(D_{ij}\) for the two weights, acting initially on \(H_\psi\). Thus \(\Delta_{\chi,\psi}\) is positive injective self-adjoint and
\(D(\Delta_{\chi,\psi}^{1/2})=D(S_{\chi,\psi})\).
The graph of \(S_{\chi,\psi}\) is precisely the closure in \(H_\varphi\oplus H_\varphi\) of the pairs displayed in (SF.45).

For the polar-factor assertion, (SF.28) applied with first weight \(\chi\) gives
\(I_{\chi\leftarrow\psi}=J_\chi K_{\chi,\psi}\). Consequently
\[
 I_{\varphi\leftarrow\chi}K_{\chi,\psi}
 =I_{\varphi\leftarrow\chi}J_\chi I_{\chi\leftarrow\psi}
 =J I_{\varphi\leftarrow\psi}.
\]
Transporting (SF.27) proves (SF.46). Closure and exact graph domains follow from SF-08, rather than from a formal expression involving powers. In particular \(S_{\psi,\chi}=S_{\chi,\psi}^{-1}\), including its range domain. This construction does not claim any imaginary-power implementation identity for the relative operator; that additional theorem has separate hypotheses and proof obligations.

<span id="oa-mod-sf-14--an-arbitrary-cardinality-matrix-model"></span>
<span id="OA-MOD-SF-14"></span>
<span id="oa-mod-sf-14"></span>
## OA-MOD-SF-14 — An arbitrary-cardinality matrix model

Let \(I\) be any index set, and choose positive invertible matrices \(d_i\in M_2(\mathbb C)\). On \(M=\prod_{i\in I}M_2(\mathbb C)\), define
\[
 \varphi(a)=\sum_{i\in I}\operatorname{Tr}(d_i a_i),
 \quad a\in M_+,
\]
where the sum is the supremum of finite subsums. This is n.s.f.: each summand is faithful and normal; finite coordinate truncations increase to a positive element and have finite weight. Its GNS realization is
\[
 H=\bigoplus_{i\in I}\operatorname{HS}_2,\qquad
 \Lambda_\varphi(x)_i=x_i d_i^{1/2},\qquad
 \pi(a)h=(a_i h_i)_i.
 \tag{SF.47}
\]
Finite-coordinate vectors prove density. Direct calculation followed by closure on these finite-coordinate cores gives
\[
 Jh=(h_i^*)_i,\qquad
 \Delta^t h=(d_i^t h_i d_i^{-t})_i
 \quad(t\in\mathbb R),
 \tag{SF.48}
\]
with domain determined by square summability of the displayed entries. These domains may be proper if the ratios of eigenvalues of \(d_i\) are unbounded.

The natural cone is exactly
\[
 P=\{h\in H:h_i\ge0\text{ for every }i\}.
 \tag{SF.49}
\]
For a finite-coordinate square \(\Lambda_\varphi(xx^*)\), its quarter-power image is
\(d_i^{1/4}x_i x_i^*d_i^{1/4}\), a positive matrix. Conversely, a positive matrix \(h_i\) on one coordinate has this form: take
\(x_i=(d_i^{-1/4}h_i d_i^{-1/4})^{1/2}\).
Finite-coordinate positive vectors are dense in the right side of (SF.49), by square summability. The cone description therefore follows from SF-04 and closedness of coordinate positivity. In particular it is independent of the chosen densities.

A normal positive functional has a family of positive density matrices \((r_i)\) with \(\sum_i\operatorname{Tr}(r_i)<\infty\), and its representative is
\[
 \xi_\omega=(r_i^{1/2})_i.
 \tag{SF.50}
\]
To verify the asserted description, restrict the functional to each finite-dimensional central summand. Normality at the increasing net of finite central sums gives the total mass and the sum formula on positive elements; linearity gives the formula everywhere. Conversely a summable positive family defines a normal positive functional by that sum, using monotone convergence of finite subsums. Matrix trace then gives
\(\langle a\xi_\omega,\xi_\omega\rangle=\sum_i\operatorname{Tr}(r_i a_i)\), proving (SF.50).

If \(I\) is uncountable, no normal positive functional is faithful: a summable family of strictly positive masses has at most countably many nonzero entries. Nevertheless the n.s.f. weight above exists, and (SF.49)–(SF.50) remain valid. This model illustrates the general theorem's hypotheses; it is not used to replace its proof.

<span id="oa-mod-sf-15--problems-and-complete-solutions"></span>
<span id="OA-MOD-SF-15"></span>
<span id="oa-mod-sf-15"></span>
## OA-MOD-SF-15 — Problems and complete solutions

**Problem 1: sharp bounds.** Show that the lower constant in (SF.20) cannot be improved. Find a different family attaining its upper bound.

**Solution.** Take nonzero cone vectors \(\xi,\eta\) with orthogonal support projections \(e,f\). Then \(\|\xi-\eta\|^2=\|\xi\|^2+\|\eta\|^2\). The functional difference has norm at most this sum by the triangle inequality, and evaluation on the self-adjoint contraction \(e-f\) attains the sum. Thus equality holds in the lower bound. Such vectors already occur on two scalar central summands. For the upper bound, take \(\xi=a\zeta,\eta=b\zeta\), where \(a,b\ge0\) and \(\zeta\in P\). The functional difference has norm \(|a^2-b^2|\|\zeta\|^2=\|\xi-\eta\|\|\xi+\eta\|\). Both calculations also include zero vectors.

**Problem 2: two orders.** In the standard Hilbert–Schmidt form of \(M_2(\mathbb C)\), find positive matrices \(A\le B\) for which \(\omega_A\not\le\omega_B\).

**Solution.** Set
\[
 A=\begin{pmatrix}1&0\\0&0\end{pmatrix},\qquad
 B=\begin{pmatrix}2&1\\1&1\end{pmatrix}.
\]
Both are positive, and \(B-A\) is the positive rank-one matrix with all entries one. The represented functionals have density matrices \(A^2\) and \(B^2\), respectively. But
\[
 B^2-A^2=\begin{pmatrix}4&3\\3&2\end{pmatrix}
\]
has determinant \(-1\), hence a negative eigenvalue. A rank-one projection onto a negative eigenvector makes \(\omega_B-\omega_A\) negative. Thus the cone-to-functional map is not order preserving, and in particular is not an order isomorphism. This does not contradict SF-11's norm continuity along monotone nets of functionals.

**Problem 3: inner automorphisms.** For a unitary \(v\in M\), compute the canonical implementation of \(\operatorname{Ad}v\). Show that the answer depends only on the automorphism, even if its implementing unitary is multiplied by a central unitary.

**Solution.** The operator \(vJvJ\) is unitary, because its two unitary factors commute. It implements \(\operatorname{Ad}v\), since its \(JvJ\) factor belongs to \(M'\). SF-05 applied to \(v\) and \(v^*\) shows that it maps \(P\) onto itself. Thus SF-12 gives \(u_{\operatorname{Ad}v}=vJvJ\). If \(z\) is central unitary, then \(JzJ=z^*\), so
\((vz)J(vz)J=vzJvJz^*=vJvJ\).
This also explains the role of the central-conjugation axiom in a concrete computation.

**Problem 4: why an infinite weight needs a GNS map.** On an infinite product of matrix blocks with \(d_i=1\), prove that the trace weight cannot be represented by one Hilbert vector, although all its bounded normal positive subfunctionals have cone representatives.

**Solution.** The weight has value \(+\infty\) at \(1\), since the finite subsums of the block traces are unbounded. A vector functional has the finite value \(\|\xi\|^2\) at \(1\), so it cannot equal this weight. A bounded normal positive subfunctional is represented by (SF.50), since its positive densities have finite total trace. The whole weight instead uses the dense-domain map (SF.47), defined on exactly the elements of finite squared weight. This distinguishes the two constructions without imposing a finiteness hypothesis on the general GNS comparison theorem.

<span id="oa-mod-sf-16--exact-scope-of-the-construction"></span>
<span id="OA-MOD-SF-16"></span>
<span id="oa-mod-sf-16"></span>
## OA-MOD-SF-16 — Exact scope of the construction

SF-02–05 construct the self-dual natural cone and prove all four standard-form axioms from the full Hilbert-algebra and modular fundamental theorems. SF-06–11 prove orthogonal-support geometry, the two norm estimates, weight-independent comparison, and existence, uniqueness and norm continuity of representatives of every bounded normal positive functional. SF-12–13 give canonical automorphism implementation, its specified topology, compatible GNS maps for every n.s.f. weight, and the common conjugation in the relative closed graph. These proofs use no separability, countable decomposability, faithful-state reduction, KMS uniqueness, spatial derivative identification, or cocycle theorem.

The construction has the following mathematical boundaries. We have not proved that every quadruple satisfying only the abstract standard-form axioms is unitarily equivalent to a weight-constructed form. Existence of a cone-preserving unitary implementing an isomorphism between arbitrary axiomatic forms therefore remains a separate obligation. Uniqueness whenever such a unitary exists follows from SF-06–07's geometric argument, which uses only the standard-form axioms; SF-09 proves existence for the weight-constructed forms of the same algebra. The full correspondence between closed cone faces and projections, the corner natural-cone identification, the order-preservation of the inverse map \(\omega\mapsto\xi_\omega\), and the later relative-operator continuity and cone-isometry/Jordan results are also separate. Support projections, orthogonality and monotone-net norm continuity established here do not silently supply those stronger assertions.

The construction uses the analytic, spectral, bounded-approximation, Hilbert-algebra and weight results specified in SF-01, with their full hypotheses and domains.


