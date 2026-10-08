# Products, analytic powers and exact dual partners

<a id="hd-setting"></a>

The small spectral values of a homogeneous operator encode its graded size. Capping its large values makes it an ordinary trace-integrable operator, and the graded size is recovered as a residue of ordinary trace norms. This gives the sharp product inequality before interpolation or duality is used. We then prove continuity of complex powers, cyclicity, the Banach range and onto duality.

We use the arbitrary-algebra construction of [Finite densities and the graded integral](OA-FLOW-MGI.md#gi-finite-cut). Thus \(S_\alpha\) is the closed measurable grade, \(\mathcal I:S_1\to\mathbb C\) is the predual integral, and
\[
 K=\frac1{2\pi},\qquad
 g_\alpha(A)=\bigl(\mathcal I(|A|^{1/p})\bigr)^p,
 \quad p=\Re\alpha>0.
 \tag{HD1}
\]
At \(p=0\), \(S_\alpha\) consists of bounded operators and its gauge is the operator norm. We retain full operator domains and the closed measurable products throughout. The zero algebra and nonfaithful densities are included.

The ordinary tracial input is the complete [trace-integration product theorem TI.8–10](../../OA-MOD/OA-MOD-TI.html#sharp-trace-estimates-from-finite-corners): for a faithful normal semifinite trace on any von Neumann algebra, ordinary measurable \(L^r\) spaces are Banach for \(1\le r<\infty\), and
\[
 \|X_1\cdots X_m\|_{r,\tau}
       \le\prod_j\|X_j\|_{r_j,\tau},\qquad
 \frac1r=\sum_j\frac1{r_j},\quad 1\le r,r_j\le\infty.
 \tag{HD2}
\]
TI.8 proves its scalar strip estimate and finite-corner norming tests; TI.9 passes to actual measurable limits with spectral Fatou; TI.10 proves the product theorem. The finite-product form follows by induction, since every partial sum of the nonnegative reciprocals remains at most \(1/r\). This is an earlier written programme proof, rather than an external assertion of Hölder's inequality.

<a id="hd-residue"></a>
## 1. A trace-norm residue measures the homogeneous product

For measurable \(A=v|A|\), define the capped operator
\[
 A^{\mathrm c}=v\min(|A|,1).
\]
This notation means spectral capping, not a complex power. If \(A\in S_\alpha\), \(p=\Re\alpha>0\), then (GI18) and scalar layer cake give, for \(\varepsilon>0\),
\[
 \begin{aligned}
 \tau\bigl(|A^{\mathrm c}|^{(1+\varepsilon)/p}\bigr)
 &=\int_0^1\frac{1+\varepsilon}{p}
       a^{(1+\varepsilon)/p-1}d_A(a)\,da\\
 &=K g_\alpha(A)^{1/p}\frac{1+\varepsilon}{\varepsilon}.
 \end{aligned}
 \tag{HD3}
\]
At the possible atom at one, the layer-cake integral still gives its full contribution; the strict tail formula is used only for \(0<a<1\). In particular, for \(X\in S_1\),
\[
 \lim_{\varepsilon\downarrow0}
 \varepsilon^{1/(1+\varepsilon)}
       \|X^{\mathrm c}\|_{1+\varepsilon,\tau}
   =K g_1(X).
 \tag{HD4}
\]

We need an elementary finite-rank fact in the trace sense. Say a measurable operator has finite trace rank if its right support has finite trace. Its left support has the same trace by polar equivalence. These operators form a two-sided ideal in the measurable algebra: a product \(BE\) with a finite projection \(E\) has right support at most \(E\); a product \(EB\) has left support at most \(E\); polar equivalence then gives the other support bound. Factoring through the support of a finite-rank operator proves the assertion for any measurable factors on either side. A finite sum has right support at most the join of the right supports, whose trace is at most their sum. These statements use the actual measurable algebra, so no everywhere-defined unbounded product is assumed.

Let \(A_j\in S_{\alpha_j}\), \(p_j=\Re\alpha_j\ge0\), and
\[
 \sum_{j=1}^m\alpha_j=1.
 \tag{HD5}
\]
Then \(X=A_1\cdots A_m\in S_1\). Normalize each nonzero factor to gauge one; a zero factor makes the conclusion immediate. For \(p_j>0\), set \(B_j=A_j^{\mathrm c}\); for \(p_j=0\), set \(B_j=A_j\). All \(B_j\) are contractions. Put \(Q=B_1\cdots B_m\). Each \(A_j-B_j\), with \(p_j>0\), has right support \(1_{(1,\infty)}(|A_j|)\) of finite trace. The telescoping identity for the product, and the finite-rank ideal just proved, show that \(X-Q\) has finite trace rank. The same holds for \(X-X^{\mathrm c}\). Thus
\[
 Q-X^{\mathrm c}\text{ is bounded, has norm at most }2,
 \text{ and has right support of finite trace }d.
\]
Consequently
\[
 \varepsilon^{1/(1+\varepsilon)}
 \|Q-X^{\mathrm c}\|_{1+\varepsilon,\tau}
       \le 2(\varepsilon d)^{1/(1+\varepsilon)}\longrightarrow0.
 \tag{HD6}
\]
Apply (HD2) with \(r=1+\varepsilon\) and \(r_j=(1+\varepsilon)/p_j\) for positive \(p_j\), using \(r_j=\infty\) otherwise. Since \(p_j\le1\), all these exponents are in its proved range. Formula (HD3) gives
\[
 \|Q\|_{1+\varepsilon,\tau}
 \le\left(K\frac{1+\varepsilon}{\varepsilon}\right)^{1/(1+\varepsilon)}.
\]
The trace-norm triangle inequality, (HD4) and (HD6) imply \(K g_1(X)\le K\). Restoring the scalar normalizations proves
\[
 \boxed{\quad
 g_1(A_1\cdots A_m)\le\prod_{j=1}^m g_{\alpha_j}(A_j),\qquad
 |\mathcal I(A_1\cdots A_m)|\le\prod_{j=1}^m g_{\alpha_j}(A_j).
 \quad}
 \tag{HD7}
\]
Both the \(K\) on the output and the product of the input factors \(K^{p_j}\) were retained; they cancel because \(\sum p_j=1\). The proof handles arbitrary ordering and zero-real-part factors. No assertion that a spectral cap stays homogeneous was made.

<a id="hd-norms"></a>
## 2. Polar tests prove the exact Banach range

Let \(0<p<1\), \(\alpha=p+it\), and write \(A=v h^p\), where \(h\in S_1^+\), \(v^*v=s(h)\), and \(v\) has grade \(it\). Set \(m=\mathcal I(h)\). If \(m>0\), define
\[
 B=m^{-(1-p)}h^{1-p}v^*\in S_{1-\alpha}.
 \tag{HD8}
\]
Its gauge is one. The closed products are
\(AB=m^{-(1-p)}v h v^*\) and \(BA=m^{-(1-p)}h\). Polar spectral transport preserves the nonzero tail traces; (GI3) therefore gives
\[
 \mathcal I(AB)=\mathcal I(BA)=m^p=g_\alpha(A).
 \tag{HD9}
\]
This argument does not invoke cyclicity before it is proved. Together with (HD7), it proves
\[
 g_\alpha(A)=\sup_{g_{1-\alpha}(B)\le1}|\mathcal I(AB)|.
 \tag{HD10}
\]
For \(A=0\), the assertion follows directly. Linearity of the product and integral now gives
\(g_\alpha(A+C)\le g_\alpha(A)+g_\alpha(C)\).
Thus \(g_\alpha\) is a norm. Its completeness has already been proved from the closed measure grade in (GI20) and the argument following it. At \(p=1\), use the predual isometry and the imaginary-grade unitary isometry (GI9). At \(p=0\), use the isometric bounded fiber and the completeness of \(M\).

Hence each grade with \(0\le\Re\alpha\le1\) is a Banach space. For \(\Re\alpha>1\), the complete quasi-norm and the exact \(2^p\) counterexample are (GI20)–(GI22). No universal Banach assertion is made there.

<a id="hd-powers"></a>
## 3. Complex powers on the whole closed strip

For a positive density \(h\), use the supported powers: \(h^z\) is zero on \(\ker h\), including when \(\Re z=0\), and is the usual spectral power on its support. Thus \(h^{i0}=s(h)\). Its full domain is
\[
 D(h^z)=\left\{\xi:\int_{(0,\infty)}r^{2\Re z}\,d\langle E_h(r)\xi,\xi\rangle<\infty\right\}
\]
when \(\Re z>0\); at zero real part it is bounded and everywhere defined.

For \(h,k\in S_1^+\) and \(0\le\Re z\le1\), put
\[
 F(z)=h^z k^{1-z}\in S_1.
 \tag{HD11}
\]
Measurability, support conventions and the closed product give membership, also on the two edges. Formula (HD7) gives the sharp bound
\[
 \|F(z)\|_1\le\mathcal I(h)^{\Re z}\mathcal I(k)^{1-\Re z}.
 \tag{HD12}
\]
If a density is zero the product is zero. For the scalar right side at the endpoints one may use \(c^0=1\); that convention does not replace the supported operator power by the identity on its kernel.

We prove that \(F\) is norm holomorphic in the open strip and norm continuous on the closed strip, including nonfaithful endpoints. For any positive measurable \(b\), the map \(z\mapsto b^z\) is differentiable in measure when \(\Re z>0\), with derivative \(b^z\log b\), interpreted as zero at spectral value zero. To see this, fix a small closed disk in that half-plane. On \([0,R]\), the first two scalar derivatives of \(r^z\) are uniformly bounded, since \(r^a|\log r|^j\to0\) as \(r\downarrow0\) for \(a>0\). The difference-quotient remainders tend uniformly to zero there. Spectral calculus proves norm convergence on that bounded cut. Its omitted high spectral projection has trace tending to zero as \(R\to\infty\), proving differentiability in measure.

Continuity of multiplication in the measure algebra proves the product rule, so
\[
 F'(z)=(h^z\log h)k^{1-z}-h^z(k^{1-z}\log k)
 \tag{HD13}
\]
is the measure limit of difference quotients. Each quotient has grade one. The fixed-time continuity of \(\theta_s\), not an assertion of time continuity on the entire measure algebra, makes that grade closed. Formula (GI18) converts convergence within this grade into predual norm convergence. Thus (HD13) is the norm derivative. The two logarithmic spectral products in (HD13) are measurable; this makes no claim that \(\log h\) or \(\log k\) alone is measurable.

Here is the additional endpoint argument. Call a measurable operator \(B\) trace-compact if \(d_B(a)<\infty\) for every \(a>0\). Every positive-real homogeneous operator has this property by (GI18). If \(a_i\) is a uniformly bounded net in \(C\) converging strongly to \(a\), then
\[
 (a_i-a)B\longrightarrow0\text{ in measure}
 \quad\text{for every trace-compact }B.
 \tag{HD14}
\]
To prove it, first take \(B\) bounded with finite trace support. The functional \(Y\mapsto\tau(B^*YB)\) is bounded and normal. Bounded strong convergence of \(a_i-a\) implies that its value on \((a_i-a)^*(a_i-a)\) tends to zero. Indeed in any faithful normal representation a normal positive functional is a sum of vector functionals; truncate that sum and use the common norm bound for the remainder. The spectral Markov bound then gives convergence in measure. For general trace-compact \(B\), split its polar spectral representation into \(|B|\le\eta\), \(\eta<|B|\le R\), and \(|B|>R\). The first part gives a uniform operator-norm error bounded by a constant times \(\eta\); the second has finite trace support and is bounded; the third product has trace rank at most \(d_B(R)\to0\). Let \(\eta\downarrow0\) and \(R\to\infty\), using the measure sum estimate. This proves (HD14). Applying adjoints gives the analogous right-multiplier statement for bounded strong-adjoint convergence.

Fix an edge point \(z_0=it\), and let \(z_i\to z_0\) within the closed strip. It suffices to work in a neighborhood with \(0\le\Re z_i\le1/2\). The factors \(h^{z_i}\) are uniformly bounded in measure: on \(1_{[0,R]}(h)\) their norms are at most \(\max(1,R^{1/2})\), and the omitted trace tends to zero. Also \(k^{1-z_i}\to k^{1-it}\) in measure by the positive-real-part argument above. The product of the first bounded-in-measure family with this difference tends to zero by the cutoff product estimates. For the remaining fixed trace-compact factor \(B=k^{1-it}\), cut \(h^{z_i}\) at height \(R\). Those capped-domain operators are uniformly bounded and converge strongly to \(h^{it}1_{[0,R]}(h)\) by bounded spectral dominated convergence, with zero values retained on \(\ker h\). Formula (HD14) applies. Removing the cap changes the product only by an operator of trace rank at most \(d_h(R)\). Hence \(F(z_i)\to F(it)\) in measure and, since all products have grade one, in norm. On the edge \(z_0=1+it\), apply the right-multiplier version after taking adjoints. The same proof handles motion along either edge. This establishes the asserted closed-strip continuity.

<a id="hd-cyclicity"></a>
## 4. Cyclicity, including nonreal grades

For \(A\in S_{1/2+it}\), the positive operators \(A^*A\) and \(AA^*\) have the same nonzero spectral distribution. Section 1 of the density lesson gives
\(\mathcal I(A^*A)=\mathcal I(AA^*)\).
Apply this equality to \(A+B\), \(A-B\), \(A+iB\), and \(A-iB\), for \(A,B\) in the same half-real-part grade. Expansion and subtraction give
\[
 \mathcal I(A^*B)=\mathcal I(BA^*).
 \tag{HD15}
\]
In particular cyclicity holds for complementary grades on the middle line.

For positive \(h,k\in S_1\), both
\(z\mapsto\mathcal I(h^z k^{1-z})\) and
\(z\mapsto\mathcal I(k^{1-z}h^z)\)
are holomorphic in the open strip by Section 3. Formula (HD15) makes them equal on \(\Re z=1/2\). Their difference vanishes everywhere: a holomorphic function with zeros accumulating in its domain has all local power-series coefficients zero, and overlapping disks propagate zero through the connected strip. Thus cyclicity holds for the two positive powers at every real \(0<p<1\).

Every element of a real grade \(S_p\), \(p>0\), is a complex linear combination of four positive elements of that grade. In detail, its real and imaginary parts are measurable selfadjoint operators of grade \(p\). Their positive and negative spectral parts remain measurable of that grade, and Section 2 of the density lesson writes each as a finite functional density to the power \(p\). Bilinearity now proves cyclicity for all \(A\in S_p\), \(B\in S_{1-p}\).

For \(\alpha=p+it\), choose the unitary \(u=h_\psi^{it}\) from (GI9). Put \(A_0=Au^*\in S_p\) and \(B_0=uB\in S_{1-p}\). Then
\[
 AB=A_0B_0,\qquad BA=u^*B_0A_0u.
\]
Use real-grade cyclicity and the integral's homogeneous-unitary invariance (GI21). This proves
\[
 \mathcal I(AB)=\mathcal I(BA),\qquad
 A\in S_\alpha,\ B\in S_{1-\alpha},\quad0\le\Re\alpha\le1.
 \tag{HD16}
\]
At \(p=0\) or \(p=1\), the same reduction uses the already proved \(M\)-\(S_1\) module identity (GI15); no analytic endpoint limit is required for those cases. Repeatedly group one factor against the product of the others to obtain cyclic invariance of every finite product in (HD5). Its integrability and the bound (HD7) were proved before applying this argument.

<a id="hd-duality"></a>
## 5. Every interior bounded functional comes from a complementary grade

The bilinear pairing \((A,B)\mapsto\mathcal I(AB)\) defines a linear isometric embedding
\[
 J_\alpha:S_{1-\alpha}\longrightarrow S_\alpha^*,\qquad
 J_\alpha(B)(A)=\mathcal I(AB),\quad0<\Re\alpha<1,
 \tag{HD17}
\]
by (HD7), (HD9), and cyclicity. A norming pairing alone does not prove that this embedding is onto. We supply the remaining argument.

First suppose \(\alpha=p\) is real and \(0<p\le1/2\). Set \(r=1/p\ge2\) and \(r'=1/(1-p)\). We prove
\[
 \|A+B\|_p^r+\|A-B\|_p^r
 \le2^{r-1}\bigl(\|A\|_p^r+\|B\|_p^r\bigr).
 \tag{HD18}
\]
Normalize the parenthesis on the right to one, and write \(A=vH^p\), \(B=wL^p\). Then \(\mathcal I(H)+\mathcal I(L)=1\). Test the two output components against \(P^{1-p}a\), \(Q^{1-p}b\), with partial isometries \(a,b\in M\) satisfying \(aa^*=s(P)\) and \(bb^*=s(Q)\), normalized by \(\mathcal I(P)+\mathcal I(Q)=1\). These are all polar norming tests: (HD9), together with the elementary conjugate-exponent scalar weights, identifies their supremum with the \(\ell^r\) sum of the two output norms. To verify the scalar assertion directly, if the two output norms are \(x,y\), choose nonnegative weights proportional to \(x^{r-1},y^{r-1}\), normalized in \(\ell^{r'}\); their pairing is \((x^r+y^r)^{1/r}\). The reverse bound is the scalar Hölder inequality, obtained from \(ab\le a^r/r+b^{r'}/r'\) after scaling. The latter follows by maximizing \(ab-a^r/r\) in the single real variable \(a\ge0\).

Consider the holomorphic scalar function
\[
 G(z)=\mathcal I\bigl((vH^z+wL^z)P^{1-z}a
                   +(vH^z-wL^z)Q^{1-z}b\bigr).
 \tag{HD19}
\]
Section 3 and bounded module multiplication justify holomorphy. On each line \(\Re z=\delta>0\), (HD7) gives
\[
 |G(z)|\le
 (\mathcal I(H)^\delta+\mathcal I(L)^\delta)
 (\mathcal I(P)^{1-\delta}+\mathcal I(Q)^{1-\delta})\le2.
 \tag{HD20}
\]
For example, concavity of \(s^\delta\) gives the first parenthesis at most \(2^{1-\delta}\), and the second at most \(2^\delta\). The limiting cases with zero mass follow by continuity or direct omission of a zero density.

On \(\Re z=1/2\), the common-half-grade space has inner product
\(\langle X,Y\rangle=\mathcal I(Y^*X)\). Positivity, (HD15), and the polarization identity identify its squared norm with \(g(X)^2=\mathcal I(X^*X)\); Section 2 gives completeness. Cauchy–Schwarz follows by expanding \(\mathcal I((X+cY)^*(X+cY))\ge0\) and minimizing over \(c\). The parallelogram identity makes the sum of squared norms of \(vH^z+wL^z\) and \(vH^z-wL^z\) equal to two. The squared norms of the two dual test components sum to one. Indeed polar support identities give equality of their individual positive masses. Cauchy–Schwarz in this two-component Hilbert space gives \(|G(z)|\le\sqrt2\).

For \(p<1/2\), the bounded-strip theorem [CI.2](../../OA-MOD/OA-MOD-CI.html#oa-mod-ci-02), on \(\delta\le\Re z\le1/2\), gives in the limit \(\delta\downarrow0\)
\[
 |G(p)|\le2^{1-2p}(\sqrt2)^{2p}=2^{1-p}.
\]
At \(p=1/2\) use the Hilbert estimate itself. Boundedness on these inner strips follows from (HD20), so no missing boundary growth condition is assumed. Taking the norming supremum and restoring the original scale proves (HD18).

For unit vectors satisfying \(\|A-B\|_p\ge\eta\), (HD18) gives
\[
 \left\|\frac{A+B}2\right\|_p^r\le1-(\eta/2)^r.
 \tag{HD21}
\]
This proves uniform convexity. The same midpoint conclusion for vectors of norm at most one follows directly from (HD18), without a separate normalization argument. The imaginary-grade isometry (GI9) extends uniform convexity to every \(\alpha\) with \(0<\Re\alpha\le1/2\).

For completeness, here is the reflexivity step from the programme Hahn–Banach theorem [CV.1](OA-FLOW-CV.md#cv-1). For any Banach space \(E\), the canonical image of its unit ball is weak-star dense in the unit ball of \(E^{**}\). If finitely many dual coordinates of some unit \(x^{**}\) could not be approximated by unit vectors of \(E\), finite-dimensional real separation would give an \(f\in E^*\) with
\(\Re x^{**}(f)>\sup_{\|x\|\le1}\Re f(x)=\|f\|\), contradicting its norm bound. This supplies a net \(x_i\) of unit-ball vectors converging to any such \(x^{**}\) in those coordinates.

If \(E\) is uniformly convex and \(\|x^{**}\|=1\), choose for each \(\eta>0\) a positive midpoint deficit \(d\) such that midpoint norm greater than \(1-d\) forces distance less than \(\eta\) in the unit ball. Choose \(f\) of norm one with \(\Re x^{**}(f)>1-d/2\). Eventually \(\Re f(x_i)>1-d\). Every midpoint of two elements of that tail has norm greater than \(1-d\), so \(\|x_i-x_j\|<\eta\). Thus the net is norm-Cauchy; its norm limit represents \(x^{**}\). Scaling and the zero case prove onto canonical embedding, hence reflexivity. Its dual is reflexive too: an element of \(E^{***}\) restricts to a functional on the onto canonical copy of \(E\), so is represented by an element of \(E^*\) on all of \(E^{**}\).

Now the range of (HD17) is norm closed, since its domain is Banach. Hahn–Banach makes this linear subspace weakly closed. It is weak-star dense: otherwise separation using finitely many evaluations would give a nonzero \(A\in S_\alpha\) annihilating the whole range, contrary to the polar test (HD9). When \(\Re\alpha\le1/2\), reflexivity of \(S_\alpha\) makes the weak and weak-star topologies of its dual coincide. The closed dense range is therefore the whole dual. When \(\Re\alpha>1/2\), apply that result to \(1-\alpha\). It identifies \(S_\alpha\) with the dual of its reflexive complementary grade. Dualizing this isometry and using reflexivity and (HD16) gives (HD17) onto in the original orientation. We have proved
\[
 \boxed{\quad S_\alpha^*=S_{1-\alpha}
 \text{ isometrically by }B\mapsto[A\mapsto\mathcal I(AB)],
 \quad0<\Re\alpha<1.\quad}
 \tag{HD22}
\]
Equality here denotes the specified canonical pairing, not an identification of a Banach dual merely from a matching norm formula.

<a id="hd-endpoints"></a>
## 6. Endpoints and solved diagnostics

The density lesson gives \(S_1\cong M_*\), so \(S_1^*\cong M=S_0\). The latter is the onto evaluation isometry proved in [the concrete predual construction](OA-FLOW-CP.md#oa-flow.cp.6), with its usual pairing. Imaginary-grade unitary transport gives the corresponding dual of \(S_{1+it}\) as \(S_{-it}\): write \(A=A_0u\), so a representing \(x\in M\) corresponds to \(B=u^*x\), and \(\mathcal I(AB)=\mathcal I(A_0x)\). The reverse endpoint does not identify every bounded functional on \(M\) with a normal one.

**1. A concrete failure of the reverse endpoint.**  
Let \(M=\ell^\infty(\mathbb N)\). The ordinary limit on its subspace of convergent sequences is a norm-one functional; Hahn–Banach extends it to \(F\in M^*\) with the same norm. It vanishes on each finitely supported sequence and has \(F(1)=1\). If it were normal, the increasing finite-support projections \(e_n\uparrow1\) would give \(F(e_n)\to F(1)\). The left side is zero and the right side one, a contradiction. Thus \(S_1=M_*\) is in general a proper subspace of \(S_0^*\).

**2. Why are caps permitted in the proof of (HD7)?**  
They need not have a grade. They enter only the ordinary trace inequality (HD2). The difference between their product and the cap of the homogeneous product is bounded of finite trace rank; its scaled trace norm disappears by (HD6). Homogeneity is used on the original product in the exact residue (HD4).

**3. Where is onto duality proved?**  
The polar test makes (HD17) an isometric embedding and separates its variables. Reflexivity changes its weak-star density into weak density, while Banach completeness makes its range norm closed and Hahn–Banach makes it weakly closed. These additional arguments force surjectivity. A separating pairing by itself would not do so.

**4. What happens at a nonfaithful strip endpoint?**  
If \(h\) has support \(e<1\), then \(F(0)=e k\), not \(k\) in general. Section 3 proves convergence to exactly this supported value. It uses finite trace spectral pieces of \(k\), not time continuity of every bounded core operator in global measure topology.

**5. How sharp is the product constant?**  
For any nonzero \(h\in S_1^+\), the factors \(h^p\) and \(h^{1-p}\) have product \(h\), and the product of their gauges is \(\mathcal I(h)\). The constant one in (HD7) is attained. The same density split into finitely many nonnegative real grades of sum one attains equality for that many factors, with supported zero powers at zero grades.

The homogeneous-space source questions are Takesaki, *Theory of Operator Algebras II*, XII.6, Exercise 7, printed p.457. A free comparison for analytic powers, cyclicity, norming and duality is Fumio Hiai, [*Concise lectures on selected topics of von Neumann algebras*, Lemmas 11.17–19 and Theorems 11.22, 11.25, 11.28, pp.109–114](https://arxiv.org/pdf/2004.02383v1#page=109). The complete ordinary trace estimates used here have their exact programme proofs above. The graded product proof is organized through the capped trace residue; neither an external citation nor a conditional interpolation identification substitutes for any of its steps.
