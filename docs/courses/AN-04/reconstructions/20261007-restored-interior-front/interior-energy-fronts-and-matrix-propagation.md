# Interior energy fronts and matrix propagation

*AN04-U066. Written by GPT-6.1 Sol (OpenAI), Ultra. Independent original text is CC0-1.0. The current restoration and exact proof connections are recorded below.*

An interior patch of a manifold with boundary has no missing normal direction. Its energy wavefront is ordinary Sobolev wavefront with a shift of one derivative. The natural dual of the energy space has the opposite shift. Establishing both shifts lets the interior propagation theorem apply to the actual weak wave equation, including its complex matrix lower terms.

This chapter supplies the ordinary interior part of the first analytic hypothesis in [Generalized glancing flow](../20261007-restored-generalized-glancing/generalized-glancing-flow-preparation.md), Section 9. Transverse reflection and strict diffraction remain separate inputs. In particular strict diffractive points are glancing, although they lie outside the exceptional set \(D=G_g\cup G^3\).

The complete programme proofs used directly are [Graph operators, continuity and Egorov](../20261005-restored-graph-egorov/graph-operators-continuity-and-egorov.md), Sections 5–7, especially the finite-matrix conjugation (GT1)–(GT17); [Sobolev propagation](../20261005-restored-sobolev-propagation/sobolev-regularity-along-real-characteristics.md), Sections 1–4; and the common-neighborhood definition (CG2)–(CG3) in [Smooth glancing regularity](../20261007-restored-smooth-glancing/smooth-glancing-neighborhoods-and-windows.md). The exact ordinary coordinate construction is the one used in [Real principal type](../20261005-restored-real-principal/real-principal-type-kernels-and-propagation.md), Section 5. The full boundary calculus and same-space transfer are the exact current programme providers already used in [Uniform microsupport](../20261007-restored-uniform-microsupport/uniform-microsupport-and-dual-sources.md). Their complete proofs retain their stated hypotheses and component terms.

The proof map also binds the [weak-H1 domain and density foundations](../20261007-restored-boundary-form/boundary-form-localization.md), [full boundary operator calculus](../20261005-global-boundary-operators/global-boundary-operator-calculus.md), and [boundary-normal coordinate transfer](../20261007-restored-normal-window/boundary-normal-coordinates-and-window-transfer.md). The graph and Sobolev proofs retain their valid Hörmander source routes.

## 1. Restrict the weak equation to the interior

Keep \(X=[0,\infty)_x\times\mathbb R^d_y\times\mathbb R_t\), Lebesgue measure, \(D_j=-i\partial_j\), and the \(L^2\) inner product linear in its first argument. Write \(n=d+2\) for the base dimension. Let
\[
 V=H^1_0(X;\mathbb C^N)\quad\hbox{or}\quad H^1(X;\mathbb C^N),
 \qquad f\in V^*,\qquad u\in V .
 \tag{IP1}
\]
Here \(V^*\) is the continuous antidual. Retain exactly the full wave form of (GN3),
\[
 \begin{aligned}
 q(u,w)&=(D_tu,D_tw)
       -\sum_{i,j}(G_{ij}D_ju,D_iw)\\
       &\quad+\sum_j(\ell_jD_ju,w)
       +\sum_i(m_i u,D_iw)+(cu,w)=f(w).
 \end{aligned}
 \tag{IP2}
\]
Indices in the principal spatial sum are spatial; the lower sums run over all base variables. The smooth real symmetric scalar spatial matrix satisfies \(G\ge\kappa I>0\). It may depend on \(t\). The lower coefficients are arbitrary smooth complex \(N\times N\) matrices. Keep the bounded extensions assumed for the original global form.

Every compactly supported smooth interior test belongs to either domain. Consequently the restriction \(f_{\mathrm{int}}\) to such tests is an ordinary vector distribution and
\[
 P_{\mathrm{int}}u=f_{\mathrm{int}},\qquad
 P_{\mathrm{int}}
  =D_t^2I_N-\sum_{i,j}D_iG_{ij}D_j
       +\sum_j\ell_jD_j+\sum_iD_i m_i+c .
 \tag{IP3}
\]
In the last sum \(D_i m_i\) denotes the composed operator \(D_i\circ m_i\). For smooth \(u\) it is \(m_iD_iu+(D_i m_i)u\), with \(D_i m_i=-i\partial_i m_i\) in this expanded expression. It is not a matrix adjoint. Integration by parts on interior tests proves (IP3), and distributional continuity proves it for \(u\in V\). The first-argument convention accounts for this order of the factors.

The principal symbol is
\[
 pI_N,\qquad p=\tau^2-\omega^TG(x,t,y)\omega,
 \qquad \omega=(\xi,\zeta).
 \tag{IP4}
\]
At a nonzero characteristic covector, positivity implies \(\tau\ne0\), and
\[
 H_p t=\partial_\tau p=2\tau\ne0 .
 \tag{IP5}
\]
Thus the interior characteristic direction is nonradial and nonzero. A fiber dilation field has zero base component; (IP5) excludes it.

This restriction does not identify the entire source \(f\) with \(f_{\mathrm{int}}\). On the \(H^1\) domain a nonzero boundary functional can have zero interior restriction. Section 6 gives an exact example.

## 2. Compare the two localized norms

Let \(K\Subset X^\circ\), choose a real \(\chi\in C_c^\infty(X^\circ)\) equal to one near \(K\), and use extension by zero after multiplying by \(\chi\). The map
\[
 E_\chi:V\longrightarrow H^1(\mathbb R^n;\mathbb C^N),
 \qquad E_\chi w=\operatorname{ext}_0(\chi w),
 \qquad \|E_\chi w\|_{H^1}\le C_\chi\|w\|_V
 \tag{IP6}
\]
is bounded in both domains. For smooth inputs this follows from the product rule and the positive distance of the support from the boundary. Approximation in \(H^1\) gives the weak-derivative statement. A function in \(H^1(\mathbb R^n)\) supported in \(K\) restricts to \(H^1_0(X)\): mollify it with radii below the distance from \(K\) to the boundary. Its \(H^1\) norm equals the norm of its restriction. Thus the two solution norms agree on compact interior outputs.

For \(h\in V^*\), define the compact interior coefficient \(\chi h_{\mathrm{int}}\) by its antidual pairing. For \(\phi\in H^1(\mathbb R^n;\mathbb C^N)\),
\[
 (\chi h_{\mathrm{int}})(\phi)=h(\chi\phi|_X),\qquad
 |(\chi h_{\mathrm{int}})(\phi)|
       \le C_\chi\|h\|_{V^*}\|\phi\|_{H^1}.
 \tag{IP7}
\]
Therefore this coefficient belongs to \(H^{-1}(\mathbb R^n)\). Conversely a distribution \(v\in H^{-1}(\mathbb R^n)\) supported in \(K\) defines
\[
 h_v(w)=v(E_\chi w),\qquad
 \|h_v\|_{V^*}\le C_\chi\|v\|_{H^{-1}}
 \tag{IP8}
\]
on either domain. The definition is independent of \(\chi\) equal to one near \(K\), since the difference vanishes near the distributional support. On smooth tests it has coefficient \(v\); density gives the asserted functional. These are the two required bounds. They make no assertion that the two unlocalized dual spaces coincide.

**Cutoff independence on the actual H1 domain.** If \(\chi_1,\chi_2\) equal one near \(K\), put \(g=\operatorname{ext}_0((\chi_1-\chi_2)w)\). The product and zero-extension bounds in (IP6) give \(g\in H^1\) with compact support a positive distance from \(K\). Convolution with a smooth unit-integral mollifier of sufficiently small radius gives compact smooth \(g_\epsilon\) whose supports still miss \(K\), and \(g_\epsilon\to g\) in \(H^1\), by the earlier Sobolev density proof. Distributional support gives \(v(g_\epsilon)=0\), while the \(H^{-1}\)-\(H^1\) bound gives \(v(g)=0\) in the limit. Thus (IP8) is independent of the cutoff on every actual domain element, not only on smooth tests. The same approximation identifies its interior coefficient with \(v\). In (IP9), the compact interior kernel makes \(A^*w\) an interior test for smooth \(w\); it therefore pairs with \(h\) using only \(h_{\mathrm{int}}\). Density gives equality of the corresponding bounded functionals whenever the resulting order permits that assertion. The positive-order distributional action is still defined first on smooth tests as stated below.

Compact interior operators also retain the actual source action. If \(A\) has kernel supported in \(U\times U\), with \(U\Subset X^\circ\), then on smooth tests
\[
 (Ah)(w)=h(A^*w),\qquad
 (Ah)_{\mathrm{int}}=A h_{\mathrm{int}} .
 \tag{IP9}
\]
The same integral kernel and adjoint define both sides. There is no extension across the boundary in this identity. Membership in \(V^*\), when asserted for a positive-order \(A\), is part of the conclusion, not an assumed bounded map on all of \(V^*\). For outputs of finite negative Sobolev order the distributional action is defined first on smooth tests.

## 3. Identify the finite and smooth fronts

In the interior the compression map is the homogeneous diffeomorphism
\[
 \pi(x,t,y;\xi,\tau,\zeta)
       =(x,t,y;\sigma=x\xi,\tau,\zeta),\qquad x>0.
 \tag{IP10}
\]
On \(U\Subset X^\circ\), \(s=\log x\) is an ordinary smooth coordinate. Quantization in \((s,t,y)\) is the interior representative of the b-calculus. The complete coordinate and amplitude law in the existing global boundary calculus, Section 2.1, shows that compactly supported ordinary and b-operators are the same operator class under (IP10), at every order and with all remainders. This uses the full coordinate law, including the determinant; an equality of leading symbols alone would not suffice.

For each real \(k\ge0\), let \(\mathrm{WF}_b^{W,k}\) mean absence of an elliptic scalar order-\(k\) test with value in \(W\), as in (CG2). Ordinary Sobolev wavefront uses actual membership at the stated order. Then
\[
 \begin{aligned}
 \pi^{-1}\bigl(\mathrm{WF}_b^{V,k}(u)\bigr)
     &=\mathrm{WF}^{k+1}(u),\\
 \pi^{-1}\bigl(\mathrm{WF}_b^{V^*,k}(f)\bigr)
     &=\mathrm{WF}^{k-1}(f_{\mathrm{int}})
 \end{aligned}
 \quad\hbox{on }T^*X^\circ\setminus0 .
 \tag{IP11}
\]

**Proof.** If a b-test is elliptic at the given interior point and has value in the stated space, same-space transfer allows a smaller test with compact kernel support in \(U\times U\) and full microsupport in its elliptic region. This is exactly the fixed-parametrix transfer already proved in U058. The compact interior representative is an ordinary order-\(k\) operator. Equations (IP6)–(IP9) turn its value into ordinary \(H^1\), or respectively ordinary \(H^{-1}\). An order-\(k\) elliptic test with that value is equivalent to ordinary \(H^{k+1}\), or respectively \(H^{k-1}\), by the complete Sobolev mapping and conic inverse test.

For the converse, choose a proper ordinary order-\(k\) test in a smaller microlocally regular region with kernel support in \(U\times U\). The same ordinary test gives \(H^1\) or \(H^{-1}\) by the order shift. Its b-representative has identical distributional action; (IP6) and (IP8) put its output in \(V\) or \(V^*\). The compact interior output is in \(H^1_0\) in the Dirichlet case. Proper localization changes only a smoothing term on the retained cone; compact smooth outputs belong to both norms. This proves both directions. \(\square\)

For the smooth fronts the exact result is
\[
 \begin{aligned}
 \pi^{-1}\bigl(\mathrm{WF}_b^{V,\infty}(u)\bigr)&=\mathrm{WF}(u),\\
 \pi^{-1}\bigl(\mathrm{WF}_b^{V^*,\infty}(f)\bigr)
        &=\mathrm{WF}(f_{\mathrm{int}}).
 \end{aligned}
 \tag{IP12}
\]
The common-neighborhood issue matters. By (CG3) the b-front is the closure of the union of its finite integer-order fronts. Ordinary smooth wavefront likewise is the closure of the union of the Sobolev fronts with orders tending to infinity. Here is the needed converse for the latter assertion: outside that closure choose one compact phase neighborhood disjoint from every such front and one order-zero test microsupported there. Fixed-order transfer puts its output in every \(H^j\). On compact base sets, membership in all these spaces implies smoothness. For a derivative of order \(a\), choose \(j>a+n/2\); Cauchy–Schwarz makes the Fourier transform of that derivative integrable, and Fourier inversion makes it continuous. The same fixed test works for every derivative. The other inclusion follows from an ordinary smoothness test and the same transfer.

**One fixed test and its actual smooth output.** For the fixed test just chosen, insert a fixed compact output cutoff \(\chi\) inside its base patch and write \(w=\chi Au\). Its membership in every \(H^j\) implies, for every multi-index \(\alpha\) and integer \(j>|\alpha|+n/2\), that \(\xi^\alpha\widehat w\) is integrable. Indeed Cauchy–Schwarz bounds its L1 norm by the \(H^j\) norm times the square root of \(\int\langle\xi\rangle^{-2(j-|\alpha|)}d\xi\). The latter integral is finite: on the shell \(2^m\le|\xi|<2^{m+1}\), its bound is \(C2^{m(n-2(j-|\alpha|))}\), a summable geometric series; the unit ball has finite volume. Fourier inversion and dominated convergence therefore give a continuous inverse Fourier integral for each derivative of \(w\). These integrals are its distributional derivatives by testing the same inversion identity against compact smooth functions. Thus \(w\) is smooth. The cutoff and microlocal test have remained fixed; only the integrable majorant changes with \(\alpha\).

Apply (IP11) and this closure identity. The sequences \(k+1\) and \(k-1\) both tend to infinity. The interior homeomorphism \(\pi\) commutes with the local closure and union, proving (IP12). The argument does not replace one common smooth neighborhood by separate neighborhoods shrinking with the order.

## 4. Propagate with arbitrary matrix lower terms

We state explicitly the matrix version needed here. Let \(L\) be a proper ordinary order-two operator with real homogeneous principal symbol \(pI_N\). Suppose \(Lu=g\), and consider a connected nonradial characteristic interval on which \(g\) is microlocally \(H^{r-1}\), for a fixed real \(r\). Then
\[
 u\text{ is microlocally }H^r
 \text{ at one point of the interval}
 \quad\Longleftrightarrow\quad
 u\text{ is so at every point}.
 \tag{IP13}
\]
Only the principal symbol must be real scalar. All complex matrix lower terms are allowed.

**Proof.** Take a proper elliptic scalar \(Q\) of order \(-1\) with positive degree-\(-1\) principal symbol \(q\). Set \(L_1=QL\). On \(p=0\),
\[
 H_{qp}=qH_p,\qquad
 Qg\text{ is }H^r\ \Longleftrightarrow\ g\text{ is }H^{r-1}.
 \tag{IP14}
\]
The canonical coordinate construction already used in the real-principal-type lesson straightens \(qp\) to the model temporal covector. Take the scalar canonical graph componentwise in the finite fiber. The full matrix theorem (GT1)–(GT17), using ordered left multiplication throughout, gives graph operators \(A,B\) of orders \(-r,r\), with
\[
 AB-I_N,\quad BA-I_N,\quad BL_1A-D_sI_N
       \text{ smoothing on the matched cones}.
 \tag{IP15}
\]
The freedom to choose the initial graph order is explicitly part of (GT16). This applies even when the lower matrices do not commute, are not Hermitian, or are not diagonalizable.

Put \(v=Bu\). The inverse graph mapping gives \(v\in L^2\) microlocally exactly when \(u\in H^r\) at the matched point. The complete defect identity is
\[
 D_sv=(D_s-BL_1A)Bu
          +BL_1(AB-I_N)u+BQg .
 \tag{IP16}
\]
The first two terms are microlocally smooth. Nested matched cones and proper cutoffs retain the smoothing inverse and conjugation defects. The last is microlocally \(L^2\): the total order of \(BQ\) is \(r-1\), exactly the assumed forcing Sobolev order.

The model theorem in Sections 2–4 of the Sobolev propagation lesson now applies componentwise. To make this extension explicit, take one common compact temporal and angular neighborhood for the finitely many components of the \(L^2\)-regular forcing. The time-independent scalar test there acts on every component and commutes with \(D_sI_N\). Its localized forcing is an actual vector \(L^2\) function. Its primitive obeys
\[
 G(s,z)=i\int_{s_*}^s g_0(a,z)\,da,\qquad
 \|G\|_{L^2(I\times Z;\mathbb C^N)}
       \le |I|\,\|g_0\|_{L^2(I\times Z;\mathbb C^N)} .
 \tag{IP17}
\]
Fubini and the finite vector Cauchy–Schwarz inequality give this bound. The remaining vector distribution is \(1\otimes c\). Componentwise time averaging, with the same test of integral one, proves that its microlocal \(L^2\) state is independent of \(s\). There are no coupled lower terms left in this model equation: the complete matrix conjugation removed them. Inverse graph mapping and (IP14) transfer local constancy back to \(u\). Both the regular and singular subsets are relatively open along the interval, so connectedness gives (IP13). \(\square\)

## 5. Supply the ordinary singular-segment hypothesis

Return to (IP2). For every \(k\ge0\), on a connected interior characteristic interval where the source is regular in \(\mathrm{WF}_b^{V^*,k+1}\), membership in the solution's \(\mathrm{WF}_b^{V,k}\) is constant:
\[
 \begin{gathered}
 f:\quad k+1\text{ b-orders over }V^*
             \quad\longleftrightarrow\quad H^k_{\mathrm{int}},\\
 u:\quad k\text{ b-orders over }V
             \quad\longleftrightarrow\quad H^{k+1}_{\mathrm{int}} .
 \end{gathered}
 \tag{IP18}
\]
Indeed (IP3) is the equation, (IP5) supplies the nonradial hypothesis, (IP11) gives both shifts, and (IP13) applies with \(r=k+1\). This is a fixed-order result, including the order itself. No estimate of a supremum replaces membership.

For the smooth front, let \(O\) be an open interior conic region disjoint from the smooth natural-dual forcing front. By (IP12) the ordinary source is smooth microlocally throughout \(\pi^{-1}O\). At noncharacteristic points, the full matrix conic parametrix of \(P_{\mathrm{int}}\) gives smoothness of \(u\). Hence the solution front in \(O\) is characteristic. Each finite solution front is invariant along characteristic intervals in \(O\), by (IP18).

Their union and its closure are also invariant there. To verify this last step without order-dependent neighborhoods, use a small characteristic flow chart about a compact segment, contained in \(\pi^{-1}O\). The positively reduced order-one Hamilton field has a nonzero temporal base component by (IP5). The smooth flow and inverse-flow theorem give a homeomorphism \(\Phi:J\times S\to\{p=0\}\cap U\), where \(J\) is an open interval and \(S\) is an open part of one transverse section. Let \(F_k\) be the solution's finite-order front restricted to this chart. Finite-order constancy along each whole chart interval gives \(\Phi^{-1}F_k=J\times E_k\) for some \(E_k\subset S\). Therefore, with closures relative to the indicated chart,
\[
 \overline{\bigcup_{k\ge0}\Phi^{-1}F_k}
       =J\times\overline{\bigcup_{k\ge0}E_k}.
\]
This identifies the ambient characteristic closure, not merely its intersection with one section, and proves its invariance. There are no off-characteristic points in that closure within \(O\). Formula (CG3), or equivalently (IP12), now proves smooth-front invariance. The flow chart is chosen once from the source-free open region, independently of \(k\).

Consequently the exact ordinary input for the closed-set theorem is supplied:
\[
 \begin{aligned}
 F&=\{p=0\}\cap\pi^{-1}
       \bigl(\mathrm{WF}_b^{V,\infty}(u)\cap O\bigr),\\
 \gamma(0)\in F,\quad
 \gamma(I)\subset\pi^{-1}O\cap T^*X^\circ
       &\quad\Longrightarrow\quad \gamma(I)\subset F ,
 \end{aligned}
 \tag{IP19}
\]
where \(\gamma\) is an ordinary characteristic interval. The statement holds in both directions and in both weak domains, with the original natural-dual forcing.

The U065 normal-form transfer changes the Hamilton parameter by a nonzero negative factor on the characteristic set. Since (IP19) holds in both directions, it also supplies the ordinary interior part in those coordinates. It does not cross a boundary time. The transverse-reflection and strict diffractive \(G_d\) parts of the first hypothesis in U053 Section 9 are still required before combining that theorem with the already proved glancing input (NC26).

![Exact order correspondence and ordered matrix pulse example. Solution k=3 over H1 is ordinary H4; source k=4 over the energy dual is ordinary H3. For pulse integrals a=b=1, the vector coefficient changes from (0,h) to (h,h) and then (h,2h), through invertible matrices of determinant one.](figures/interior-orders-and-matrix-pulses.svg)

*Figure IP-F1.* The upper panel applies (IP11) and (IP18) at the exact orders of Exercise 1. The lower panel gives the exact three states before, between and after the two pulses in (IP23), with integrals \(a=b=1\). Its arrows represent the successive invertible linear maps, without prescribing a pulse duration or trajectory in physical space. The full vector retains its wavefront; the first component can acquire the singular distribution \(h\). Vasy's interior order comparison and the programme matrix-conjugation proof supply the source routes.

## 6. Graded exercises with complete solutions

### Exercise 1: two different order shifts, intermediate

Suppose the desired solution regularity is three b-orders over \(V\). Compute its ordinary Sobolev order and the forcing order required by interior propagation. Does three b-orders over \(V^*\) supply that forcing order?

**Solution.** In (IP11) the solution order is \(3+1=4\). Order-two propagation requires \(f_{\mathrm{int}}\in H^{4-1}=H^3\). The source test must therefore have order \(3+1=4\) over \(V^*\), since its ordinary order is \(4-1=3\). Three source b-orders give only \(H^2\) and do not meet this hypothesis:
\[
 (u,V,3)\mapsto H^4,\qquad
 (f,V^*,4)\mapsto H^3,\qquad
 (f,V^*,3)\mapsto H^2 .
 \tag{IP20}
\]
The distinct baseline spaces cause the two opposite shifts.

### Exercise 2: a boundary source invisible in the interior, advanced

On the half-space take \(g\in C_c^\infty(\partial X;\mathbb C^N)\), \(g\ne0\), and set \(f_g(w)=(g,\gamma w)_{L^2(\partial X)}\), where \(\gamma\) is the boundary trace. Prove that it is a continuous nonzero functional on \(H^1(X)\), has zero restriction to \(H^1_0(X)\), and has zero interior distributional restriction.

**Solution.** For smooth compactly supported \(w\), the fundamental theorem of calculus in the normal direction gives
\[
 \|\gamma w\|_{L^2(\partial X)}^2
       \le 2\|w\|_{L^2(X)}\|\partial_xw\|_{L^2(X)}
       \le \|w\|_{H^1(X)}^2 .
 \tag{IP21}
\]
To obtain the first inequality, integrate
\(\partial_x|w|^2=2\operatorname{Re}(\partial_xw,w)_{\mathbb C^N}\)
from zero to infinity and then apply Cauchy–Schwarz on \(X\). Smooth approximation extends the trace to \(H^1\) and gives
\(|f_g(w)|\le\|g\|_{L^2}\|w\|_{H^1}\).
Choose \(w(x,z)=\rho(x)g(z)\) with compact smooth \(\rho\) and \(\rho(0)=1\); then \(f_g(w)=\|g\|_{L^2}^2>0\). Compactly supported interior smooth functions have zero trace; closure proves that the functional vanishes on \(H^1_0\). The same test observation gives \((f_g)_{\mathrm{int}}=0\). Equation (IP12) therefore gives no interior source front, while the original nonzero boundary functional remains part of the \(H^1\) weak equation. Discarding it in a boundary propagation argument would change that equation.

### Exercise 3: noncommuting lower transport, advanced

In a straightened coordinate \(s\), take two smooth disjoint pulses \(\alpha,\beta\), the \(\alpha\)-pulse first, with integrals \(a,b\). Let
\[
 Q(s)=i\alpha(s)N_1+i\beta(s)N_2,\qquad
 N_1=\begin{pmatrix}0&1\\0&0\end{pmatrix},\quad
 N_2=\begin{pmatrix}0&0\\1&0\end{pmatrix}.
 \tag{IP22}
\]
Compute the exact transport \(M'=-iQM\), initially \(I_2\), after both pulses. Show that it preserves singularity of the full vector even though individual components may change their singularity.

**Solution.** Each nilpotent has square zero. The time order gives
\[
 M=(I_2+bN_2)(I_2+aN_1)
   =\begin{pmatrix}1&a\\b&1+ab\end{pmatrix},\qquad
 M^{-1}=\begin{pmatrix}1+ab&-a\\-b&1\end{pmatrix}.
 \tag{IP23}
\]
Both products are identities and \(\det M=1\). Reversing the pulse order puts \(ab\) in the first diagonal entry instead of the second, so a commuting exponential would be incorrect. Since \(Q\) is multiplication, \(Q\#M=QM\) exactly, and the product rule gives \(M^{-1}(D_sI_2+Q)M=D_sI_2\).

For any distribution \(c(z)\), \(v(s,z)=M(s)c(z)\) solves the homogeneous model. Smooth multiplication by \(M\) and its smooth inverse preserves every vector microlocal \(H^r\) state, and therefore its full vector wavefront. For \(c=(0,h)^T\) with singular \(h\) and \(a\ne0\), the first component becomes \(ah\) after the first pulse, although it was initially zero. The vector is singular on both sides. This example concerns the union of component wavefronts; it does not assert propagation of each component separately.

## 7. Sources and exact scope

The freely accessible human primary source is [Vasy, *Propagation of singularities for the wave equation on manifolds with corners*](https://math.stanford.edu/~andras/psmcrrb.pdf), printed/PDF 3 for the interior Sobolev interpretation, printed/PDF 17 for the two duals, and printed/PDF 22, Definition 3.17, for the common smoothness test. The [correction](https://math.stanford.edu/~andras/psmc-corr.pdf) remains attached to the source route. These passages supply definition and scope comparison; this chapter's finite-matrix interior proof uses the complete existing programme conjugation and its own receiving argument. No general extension of Vasy's metric-wave theorem is inferred from those passages. Free access is not treated as a grant to copy the paper's expression.

The results proved here are (IP11)–(IP12), the finite-matrix interior propagation statement (IP13), and its exact weak-domain singular-segment application (IP19), with three complete solutions. The chapter copies no external paper expression or asset. It does not supply transverse reflection, strict diffractive propagation, physical corners, a non-scalar principal system, or every remaining source and proof obligation in the full course.


The restoration by GPT-6 Astra (OpenAI), Ultra, reconnects the exact current programme proofs, proves cutoff independence on actual H1 tests and the fixed-test smoothness implication, and adds the exact order-and-matrix diagram. Every adopted result is proved here or in the earlier lesson identified by the proof map.  Independent new expression is CC0-1.0; linked components retain their terms. 
