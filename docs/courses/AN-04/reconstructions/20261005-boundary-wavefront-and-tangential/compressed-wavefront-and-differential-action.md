# Compressed wave fronts and all differential actions

Original source: AN03-U034, *Global boundary operators, compressed wave fronts, and normal extension*, written by Codex, September 2026, CC0. Current complete proof connections and clarifications: AN-04 course-writing task and OpenAI Codex, 5 October 2026, CC0. All original mathematical displays in the selected sections remain unchanged.

Use \(D=-i\partial\), forward Fourier exponential \(e^{-ix\cdot\xi}\) and inverse factor \((2\pi)^{-n}\), on smooth Hausdorff second-countable manifolds with boundary and finite-rank bundles. The [global geometry](../20261005-global-boundary-operators/stretched-kernels-and-compressed-geometry.md) and [complete operator calculus](../20261005-global-boundary-operators/global-boundary-operator-calculus.md) prove (GL1)–(GL24), (GC1)–(GC14), (GA1)–(GA5), (GD13)–(GD14) and (GW1)–(GW5), including exact proper support, residual receiving and ordered elliptic parametrices. The [conormal test spaces](../20261005-conormal-test-foundations/conormal-amplitudes-and-test-spaces.md), [dual distributions and intrinsic jets](../20261005-conormal-test-foundations/dual-conormal-distributions-and-jets.md), and [full conormal intersection proof](../20261005-conormal-test-foundations/conormal-duality-implies-smoothness.md) supply (C1)–(C17), (GD1)–(GD12), and (SP1)–(SP15). A smooth boundary function is represented by its zero extension when paired with ambient supported distributions.

The exact [local boundary action](../20261005-local-boundary-calculus/boundary-tests-and-lacunary-symbols.md) and [distributional calculus](../20261005-local-boundary-calculus/boundary-adjoints-composition-and-distributions.md) supply all commutators, boundary jets and weak approximation, including distributions supported entirely on the boundary. The [ordinary wave-front proof](../20261004-free-intrinsic-graph/prerequisites/coordinate-and-wavefront-localization.md) and [conic parametrices](../20261004-free-intrinsic-graph/prerequisites/conic-parametrices-and-localization.md) give the interior and tangential boundary calculus. The [locally finite partition PS5](../20261004-free-intrinsic-graph/prerequisites/global-principal-symbol.md), [Fourier](../20261004-free-intrinsic-graph/prerequisites/fourier-l2.md), and [measure proofs](../20261004-free-intrinsic-graph/prerequisites/measure-and-l2.md) supply the remaining foundations. Source credit: the approved Hörmander III, 2007 eBook, ISBN 978-3-540-49938-1, Section 18.3. Its use and ordinary citation are valid; the mathematical arguments and exact prerequisites are included.

## Compact localization and the meaning of the tests

This component retains Sections 4.2–4.4. Every argument at a covector may use a tester with compact output support: multiply a given tester on the left by a compact smooth cutoff equal to one near the point. This preserves ellipticity and the conormal target by (GA3). Proper support then confines all relevant input variables to a compact set. For a residual operator \(R\) with this localized output support, choose \(\psi=1\) on that compact input set; its actual action is \(Ru=R(\psi u)\). Formula (GA5) then applies to the compact distribution \(\psi u\). Apply this convention to every residual term below, including those acting on \(D_nu\). It proves a single conormal order on each localized output, without imposing a global finite order on a noncompact input.

The notation \(\mathcal A=\bigcup_m\mathcal A^m\) always requires one order on the whole manifold; its local enlargement is defined explicitly below. Matrix products are never commuted.

### 4.2. The compressed wave-front set

For a supported distribution \(u\in\mathcal D'_X\), define
\[
 \operatorname{WF}_b(u)
 :=\bigcap_{\substack{B\in\Psi_b^0(X;E,E)\text{ proper}\\
                         Bu\in\mathcal A(X;E)}}
       \operatorname{Char}B
 \quad\subset\widetilde T^*X\setminus0 .
 \tag{GW6}
\]
The zero operator is always an admissible test, with characteristic
set equal to the whole nonzero compressed bundle. The identity is an
admissible test exactly when \(u\in\mathcal A(X)\). Thus the family
of tests is never empty. Every characteristic set is closed and conic by (GW1), and so
is its intersection. At a covector outside \(\operatorname{WF}_b(u)\)
there is one properly supported order-zero \(B\), elliptic there,
with \(Bu\in\mathcal A\). The target cannot be changed to
\(C^\infty(X)\) for arbitrary supported distributions: (GA5)
receives a residual operator into \(\mathcal A\), and its original
corner kernel may fail to smooth at the boundary.

For later use we prove the finite-cover consequence of (GW6). If
\(\operatorname{WF}_b(u)\) is empty above a compact \(K\subset X\),
the compressed unit cosphere above \(K\) has a finite cover by cones
where order-zero operators \(B_1,\ldots,B_N\) are elliptic and
\(B_ju\in\mathcal A\). Choose a smooth partition of unity
\(\chi_j\) in those cones at \(|\zeta|\ge R\), summing to a spatial
cutoff \(\varphi=1\) near \(K\). Apply (GW3)–(GW4) separately to the
symbols \(\chi_j b_j^{-1}\), preserving their factor order.
Asymptotic summation gives properly supported \(C_j\) and a residual
\(R\) such that
\[
 \sum_{j=1}^N C_jB_j=\varphi+R.
 \tag{GW7}
\]
The missing compact-frequency part is a residual kernel and is included
in \(R\). Choose the output supports of all \(C_j\) in one compact
neighborhood of \(\operatorname{supp}\varphi\). Then \(R\) has
compact output support; proper support gives one compact input set.
Choose a compact smooth \(\psi\) equal to one on that input set.
The exact identity \(Ru=R(\psi u)\) lets (GA5) apply to the compact
distribution \(\psi u\), even when the original \(u\) is not compact.
Acting on \(u\), every \(C_j(B_ju)\) belongs to
\(\mathcal A\) by (GA3), and \(Ru\in\mathcal A\) by (GA5).
Thus \(\varphi u\in\mathcal A\). On a noncompact manifold the
order obtained from this finite cover may depend on the compact set.
Retain the original class \(\mathcal A=\bigcup_m\mathcal A^m\), and
define its exact local enlargement by

\[
 \mathcal A_{\mathrm{loc}}(X)
 =\{u\in\mathcal D'_X:
       \chi u\in\mathcal A(X)\text{ for every }\chi\in C_c^\infty(X)\}.
 \tag{GW8a}
\]

Multiplication and restriction give the injective map
\(\mathcal A\hookrightarrow\mathcal A_{\mathrm{loc}}\). The preceding
finite-cover argument proves the exact replacement for the global-order
assertion:

\[
 \operatorname{WF}_b(u)=\varnothing
       \quad\Longleftrightarrow\quad u\in\mathcal A_{\mathrm{loc}}(X).
 \tag{GW8}
\]

For the converse, at any compressed covector over \(x\), choose a
compact smooth \(\chi\) equal to one near \(x\). The multiplication
operator \(\chi I\) is properly supported, elliptic at that covector,
and maps \(u\) into the original \(\mathcal A\), by (GW8a). These
testers exclude every covector. For the forward implication, apply
(GW7) on a compact neighborhood of \(\operatorname{supp}\chi\), then
multiply its conormal output by \(\chi\). The maximum of the finitely
many conormal orders is one valid order for that compact output.
If \(u\) has compact support, choose \(\chi=1\) on its support;
then \(\chi u=u\) and (GW8) does imply \(u\in\mathcal A\).
In particular the original global-order equivalence holds on compact
\(X\). No single order is asserted after an infinite exhaustion.

The distinction is necessary. On
\(X=\mathbb R_y\times[0,\infty)_t\), of dimension two, choose
nonzero \(\theta\in C_c^\infty((-1/4,1/4))\) and form the actual
locally finite supported distribution

\[
 u(y,t)=\sum_{j=1}^\infty\theta(y-j)\otimes\delta^{(j)}(t).
 \tag{GW8b}
\]

Each compact set meets only finitely many summands. The \(j\)-th
summand has normal amplitude \((i\tau)^j\theta(y-j)\) with inverse
factor \((2\pi)^{-1}\), so its conormal order is exactly \(j\), by
the original codimension-one shift \(m+(n-2)/4\) with \(n=2\).
It belongs to \(\mathcal A^j\), including all tangent derivatives.
It does not belong to \(\mathcal A^m\) when \(m<j\). To verify the
last statement directly, select a bounded interval in tangential
frequency on which the squared Fourier transform of \(\theta\) has
positive integral. On the full sharp dyadic annulus, restrict the
normal frequency to \(c_1 2^l<|\tau|<c_2 2^l\) strictly inside
that annulus. Its squared Fourier integral is bounded below by
\(c_j2^{l(2j+1)}\). The (GA1) Besov factor is
\(2^{l(-m-1/2)}\), so the resulting norm is at least
\(c'_j2^{l(j-m)}\), which diverges for \(m<j\).
Multiplying (GW8b) by a compact cutoff equal to one around its
\(j\)-th boundary support isolates that summand. Thus (GW8b) lies
in \(\mathcal A_{\mathrm{loc}}\) and has empty compressed wave front,
but lies in no \(\mathcal A^m\). This proves strictness of the
displayed injection. The quotient
\(\mathcal A_{\mathrm{loc}}/\mathcal A\) records precisely this
failure of one globally bounded order, with kernel of the quotient
map equal to the original \(\mathcal A\).

The stronger smoothness conclusion for \(u\in\mathcal A'\) needs
the separate local intersection theorem proved below. It is not
being inferred from conormality alone.

### 4.3. Residual localization and elliptic inclusion

Let \(A\in\Psi_b^m\) have a full symbol of order \(-\infty\)
in a conic neighborhood of a closed conic set \(\Gamma\). At each
\(q\in\Gamma\) choose an order-zero cutoff \(D_q\) elliptic at
\(q\) whose large-frequency symbol is supported in a smaller cone
inside that neighborhood. The full ordered product expansion (GC9)
has every term residual there: derivatives of the cutoff stay in the
smaller cone, derivatives of the full symbol of \(A\) have arbitrary
negative order there, and the exact far product term is residual.
The coordinate-invariant remainders (GC13) therefore give
\(D_qA\in\Psi_b^{-\infty}\), after harmless compact spatial
localization. By (GA5), \(D_qAu\in\mathcal A\). Hence
\[
 \operatorname{WF}_b(Au)\cap\Gamma=\varnothing.
 \tag{GW9}
\]
This proves precisely the conormal residual target; it makes no
unsupported boundary smoothness claim.

For the elliptic inclusion, let \(q\) be outside both
\(\operatorname{Char}B\) and \(\operatorname{WF}_b(Bu)\), where
\(B\in\Psi_b^m\) is proper. Select an order-zero tester \(D\)
elliptic at \(q\) with \(DBu\in\mathcal A\). The product \(DB\)
has invertible principal symbol \(d b\) near \(q\) in the original
order; its inverse is \(b^{-1}d^{-1}\). Apply (GW3)–(GW5) to
\(DB\), choosing \(\chi\) supported in the common elliptic cone
and equal to one near \(q\). There is an order-zero tester \(Q\)
elliptic at \(q\) and a residual \(R\) with the exact identity
\(Q=E DB+R\). The first term is conormal by (GA3), and the residual term by
(GA5). Thus \(Qu\in\mathcal A\), giving
\[
 \operatorname{WF}_b(u)
   \subset\operatorname{WF}_b(Bu)\cup\operatorname{Char}B.
 \tag{GW10}
\]
Every inverse and product has retained the bundle map order.

For a properly supported \(B\in\Psi_b^m\), the forward inclusion
follows by the complementary microlocal division. If
\(q\notin\operatorname{WF}_b(u)\), take an order-zero elliptic
\(C\) there with \(Cu\in\mathcal A\). Construct its left local
parametrix \(P_C\) as above, so \(P_CC=Q_0+R_0\), where \(R_0\)
is residual and \(Q_0\) has full symbol equal to the identity modulo a residual symbol on a
smaller cone about \(q\) at high frequency. Choose \(D\) of order
zero, elliptic at \(q\), with full symbol supported inside that
smaller cone. Put \(E=DBP_C\). Since \(D\) is supported where the
full symbol of \(Q_0\) is the identity, the exact product (GC9)
and its far residual give \(DB(I-Q_0)\in\Psi_b^{-\infty}\).
The product \(DBR_0\) is residual by (GC10). Therefore
\[
 DB=E C+R,
 \qquad E\in\Psi_b^m,\quad R\in\Psi_b^{-\infty}
 \tag{GW11}
\]
with \(R=DB(I-Q_0)-DBR_0\). Thus
\(DBu=E(Cu)+Ru\in\mathcal A\), so
\[
 \operatorname{WF}_b(Bu)\subset\operatorname{WF}_b(u)
 \quad(B\in\Psi_b^m\text{ proper}).
 \tag{GW12}
\]
For completeness, finite sums have a common tester. Suppose \(q\) is regular for each of finitely many \(u_i\), with \(C_i u_i\in\mathcal A\) and \(C_i\) elliptic at \(q\). The actual left parametrices give \(P_iC_i=Q_i+R_i\), with \(Q_i=I\) modulo residual symbols on a common smaller cone. Choose one compactly supported order-zero \(D\), elliptic at \(q\), whose full symbol is supported modulo residual terms in that cone. The complete product formula makes \(D(I-Q_i)\) residual, so
\[
 Du_i=DP_i(C_iu_i)-DR_iu_i+D(I-Q_i)u_i\in\mathcal A.
 \tag{BW1}
\]
All residual inputs are compactly localized as above. The finite maximum of the resulting orders is a valid order for the sum. Thus \(\operatorname{WF}_b(\sum_i u_i)\subset\bigcup_i\operatorname{WF}_b(u_i)\). Adding an element of \(\mathcal A_{\mathrm{loc}}\) preserves the wave-front set, by localizing it into \(\mathcal A\) and applying this assertion in both directions.

The same inclusion holds for an arbitrary ordinary smooth differential
operator, including the unweighted normal derivative. We prove this
separately because \(D_n\) itself is not a totally characteristic
operator. For \(q\notin\operatorname{WF}_b(u)\), choose \(C\)
elliptic at \(q\) with \(Cu\in\mathcal A\). The left localized
parametrix gives \(P_CC=Q+R\), where the full symbol of \(Q\)
is one modulo a residual symbol on a high-frequency cone about \(q\) and \(R\) is
residual. Thus
\[
 Qu=P_C(Cu)-Ru\in\mathcal A.
 \tag{GW12a}
\]
Choose an order-zero tester \(D\), elliptic at \(q\), with full
symbol supported in a smaller cone where \(Q=I\) microlocally.
Then \(D(I-Q)\) is residual by (GC9), including its exact far term.
The ambient supported distribution \(D_j u\) is again supported in
the closed half-space. The local commutators are exactly
\[
 [D_j,T_a]=T_{D_{x_j}a}\quad(j<n),\qquad
 [D_n,T_a]=T_{D_{x_n}a}+T_{D_{\xi_n}a}D_n .
 \tag{GW12b}
\]
These are the unmodified (5.1), with \(D=-i\partial\) and all signs
retained. They first hold on interior compact smooth functions.
Theorem 9.1(e) in the local prerequisite approximates every supported
distribution weakly by such functions; each term in (GW12b) is a
composition of weakly continuous operators on supported distributions.
Taking that limit proves the same identity for the actual supported
representatives, including any boundary deltas.

Write \(w=(I-Q)u\). Since the full symbol of \(Q\) is constant one modulo a residual symbol
on the working cone, the symbols \(D_{x_j}q\) and
\(D_{\xi_n}q\) vanish there to every symbol order. Apply \(D\)
on the left in (GW12b) and use (GC9): each resulting product is
residual. The exact identity
\[
 D D_jw
   =D(I-Q)D_ju+D[D_j,I-Q]u
 \tag{GW12c}
\]
is therefore a sum of residual operators applied to supported
distributions, \(u\) or \(D_nu\). It belongs to \(\mathcal A\)
by (GA5). On the other hand \(Qu\in\mathcal A\) by (GW12a), and
the ordinary differential map (C17) gives \(D_jQu\in\mathcal A\);
applying \(D\) preserves that class by (GA3). Hence
\(DD_ju\in\mathcal A\), so
\[
 \operatorname{WF}_b(D_ju)\subset\operatorname{WF}_b(u)
 \quad(j=1,\ldots,n).
 \tag{GW12d}
\]
Smooth coefficient multiplication is in \(\Psi_b^0\), and (GW12)
applies to it. Finite sums and products of the \(D_j\) with such
coefficients therefore give the same inclusion for every ordinary
smooth differential operator. The proof has kept the normal
\(T_{D_{\xi_n}a}D_n\) term in (GW12b); omitting it would make the
boundary claim unjustified.

### 4.4. Interior comparison and a noncharacteristic boundary

In the interior, (GL8) is the ordinary cotangent identification.
Localized global \(b\)-operators are ordinary pseudodifferential
operators there by (GL13)–(GL15), and every ordinary properly
supported local operator can be realized with the same interior
kernel in the global class, using (GC7). Also
\(\mathcal A\) restricts to \(C^\infty\) in the interior by (GA1):
every derivative is a combination of tangent derivatives on a compact
interior chart, and the local Sobolev estimates give all smooth
derivatives. Both implications in the tester definition therefore
give the exact equality
\[
 \operatorname{WF}_b(u)|_{T^*X^\circ}
       =\operatorname{WF}(u|_{X^\circ}).
 \tag{GW13}
\]

Let \(P=\sum_{|\alpha|\le m}a_\alpha(x)D^\alpha\) be a smooth
ordinary differential operator of positive integer order \(m\), and
let \(\phi\) vanish simply at the boundary, with \(\phi=c x_n\),
\(c(x',0)>0\), in a chart. No original coefficient is removed.
The complete differential expression
\[
 \phi^mP
   =\sum_{|\alpha|\le m}
      c(x)^m x_n^{m-\alpha_n}
      a_\alpha(x)D'^{\alpha'}
       \bigl(x_n^{\alpha_n}D_n^{\alpha_n}\bigr)
 \tag{GW14}
\]
retains every lower-order and tangential term; the displayed factor
order is valid because \(D'\) commutes with \(x_n\). Thus
\(\phi^mP\in\operatorname{Diff}_b^m\). At \(x_n=0\), all principal
terms except \(\alpha=(0,m)\) contain a positive power of \(x_n\).
Its complete boundary principal compressed symbol is
\[
 \sigma_m(\phi^mP)(x',0,\xi',\rho)
     =c(x',0)^m a_{(0,m)}(x',0)\rho^m.
 \tag{GW15}
\]
If the boundary is noncharacteristic, the original leading normal
coefficient \(a_{(0,m)}(x',0)\) is invertible. Equation (GW15) is
invertible exactly when \(\rho\ne0\); its boundary characteristic
set is precisely the embedded tangential hyperplane
\(T^*\partial X=\{\rho=0\}\), with the zero section excluded.
Applying the full inclusion (GW10) to the actual operator
\(\phi^mP\) yields
\[
 \operatorname{WF}_b(u)|_{\partial X}
  \subset
  \operatorname{WF}_b(\phi^mPu)|_{\partial X}
        \cup(T^*\partial X\setminus0).
 \tag{GW16}
\]
For \(m=0\), \(P\) is multiplication by its original invertible
coefficient under the corresponding noncharacteristic hypothesis;
the same parametrix gives (GW16) with an empty boundary
characteristic set. Formula (GW14) is not used with a negative power.

