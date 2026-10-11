# Relation symmetries and weight covariance

A symmetry of a measured relation has two effects on its operator algebra. It moves the diagonal functions, and it may attach phases to arrows. Only the motion changes the diagonal weight. We identify its standard unitary, transport the entire finite left ideal, and compute the resulting relative modular operators and normalized Connes cocycles. The formulas allow infinite total measure and unbounded Radon–Nikodym densities.

The algebraic symmetry theorems are already proved in Normalizers, phases, and orbit cocycles. We use those complete programme proofs at the locators below. The added arguments connect them to relation weights and change of measure, especially RWT-03–06, and canonical standard implementation, SF-12–13. The topology convention is proved equivalent to the usual u-topology in The precise topology of a standard implementation.

## 1. Objects and the existing symmetry proofs

Let a countable group act nonsingularly on a nonzero standard Borel sigma-finite measured space \((X,\mu)\). Write \(R\) for its principal orbit relation, \(M=M(R,\mu)\), and \(D=L^\infty(X,\mu)\subset M\). No freeness or ergodicity is assumed unless specified. Arrows are \((y,x):x\to y\). Source counting gives

\[
 H_\mu=L^2(R,\nu_s),\qquad
 \int_R F\,d\nu_s=\int_X\sum_{y\sim x}F(y,x)\,d\mu(x).
 \tag{RSY.1}
\]

Write \(\delta=d\nu_r/d\nu_s\), \(M_f\xi(y,x)=f(y)\xi(y,x)\), and \(N_f\xi(y,x)=f(x)\xi(y,x)\). The weight and modular conjugation are

\[
 \varphi_\mu(T)=\int_XE(T)\,d\mu,\qquad
 J_\mu\xi(y,x)=\delta(y,x)^{1/2}\overline{\xi(x,y)}.
 \tag{RSY.2}
\]

Their full domains and faithful normal semifinite construction are RWT-01–02.

We distinguish the full group \([R]\), whose maps move each point within its orbit, from \(\operatorname{Aut}(R)\), whose measure-class Borel maps may permute entire orbits. All maps are taken modulo null sets. Circle-valued relation cocycles satisfy

\[
 c(z,x)=c(z,y)c(y,x).
 \tag{RSY.3}
\]

For each particular finite or countable list of maps and identities, remove the exceptional null sets and close their union under the presenting group and the listed maps and inverses. The remaining conull space supports the simultaneous identities. We do not require one conull representative for an uncountable family of all symmetries.

Here are the earlier complete proofs used below.

| Result | Exact programme proof |
| --- | --- |
| Normal diagonal isomorphisms come from measure-class Borel maps | *Normalizers, phases, and orbit cocycles*, Lemma 0.1 |
| Every unitary normalizer is \(M_bV_\theta\), with \(\lvert b\rvert=1\) and \(\theta\in[R]\) | Same lesson, Theorem 1.1, including its uniqueness and multiplication law |
| A diagonal-preserving isomorphism recovers an orbit equivalence | Same lesson, Theorem 2.1; the reverse direction is *Orbits, stabilizers, and relation algebras*, Theorem 5.2 |
| \(c\mapsto\alpha_c=\operatorname{Ad}(U_c)\vert_M\) identifies cocycles with diagonal-fixing automorphisms | Same lesson, Section 3, equation (3.2a) and Theorem 3.1, including stabilizer compatibility |
| \(\alpha_c\) is inner precisely for coboundaries | Same lesson, Theorem 4.1 |
| A diagonal automorphism extends precisely when its point map preserves \(R\) | Same lesson, Corollary 5.0 |
| Diagonal-preserving automorphisms split as cocycle times geometric motion | Same lesson, Proposition 5.1 |
| Geometric symmetries form a closed Polish group; in the ergodic case its inner subgroup is the Borel image of \([R]\) | Same lesson, Lemma 5.2 and Theorem 5.3 |

The second prerequisite in the table is Orbits, stabilizers, and relation algebras. Its Theorem 4.2 and Corollary 4.3 also prove that \(D\) is maximal abelian and that ergodicity is equivalent to factoriality. None of these statements identifies the principal relation with a transformation groupoid having extra stabilizer arrows.

For the Borel facts in Lemma 0.1 and Theorem 5.3, the precise earlier proof is Borel models, measurable inversion and Polish group quotients, Theorem 4.3(5), with its complete proof through Theorem 3.6 and Corollary 3.7. It says that an injective Borel map from a standard Borel space into a separable metrizable space has Borel image and Borel inverse on that image. A countable Borel separating family \((B_n)\) gives the injection into \([0,1]\) used in Lemma 0.1 explicitly by \(x\mapsto\sum_{n\ge1}2\,3^{-n}\mathbf1_{B_n}(x)\); at the first differing digit, its contribution strictly exceeds the maximum possible tail difference. The theorem supplies the Borel inverse. It also applies to the Borel scalar-phase transversal in the Polish unitary group in Theorem 5.3; a Borel subset of a standard Borel space is standard by the same prerequisite's change-of-topology theorem F4.

## 2. Applying the symmetry theorems at infinite mass

The probability-space arguments in the symmetry lesson apply to every measure class in Section 1. Here is the precise reduction. Partition \(X\), up to a null set, into Borel sets \(B_n\) of finite measure. The function

\[
 q_0(x)=\sum_{n\ge1}
       \frac{2^{-n}}{1+\mu(B_n)}\,\mathbf1_{B_n}(x)
\]

is positive and finite almost everywhere, with \(0<\int q_0\,d\mu<\infty\). Normalize it to a density \(q\) of total integral one. By RWT-03 and RWT-05,

\[
 V_q:H_{q\mu}\longrightarrow H_\mu,\qquad
 V_q\xi(y,x)=q(x)^{1/2}\xi(y,x)
 \tag{RSY.4}
\]

is the canonical standard-form comparison for the identity on \(M\). It fixes the represented \(M_f,V_\theta\) by intertwining them, and preserves their algebraic relations. Null classes of point maps and cocycles are unchanged. Thus the normalizer theorem, reconstruction, cocycle classification and extension criterion transfer without any finite-weight hypothesis. A diagonal cyclic vector is used only in the probability coordinates.

For \(\theta\in[R]\),

\[
 (V_\theta\xi)(y,x)=\xi(\theta^{-1}y,x).
\]

Every normalizer is \(M_bV_\theta\), uniquely modulo null sets. The product is

\[
 (M_bV_\theta)(M_dV_\psi)
 =M_{b(d\circ\theta^{-1})}V_{\theta\psi}.
 \tag{RSY.5}
\]

In particular the quotient of the unitary normalizer by \(\mathcal U(D)\) is \([R]\). A scalar \(i1\) already prevents replacing the normalizer by the bare set of \(V_\theta\)'s.

For a cocycle, \(U_c=m_c\) on \(H_\mu\). Its induced automorphism fixes \(D\) and sends a bounded left kernel \(T_a\) to \(T_{ca}\). The complete row-sum argument for all bounded kernels is equation (3.2a) of the prerequisite, not only its generator computation. Conversely its Theorem 3.1 reconstructs \(c\) from
\(\alpha(V_g)=M_{b_g}V_g\), using

\[
 b_{gh}(y)=b_g(y)b_h(g^{-1}y),\qquad
 b_g(gx)=b_h(hx)\quad\text{when }gx=hx.
 \tag{RSY.6}
\]

The second identity is essential when the action has stabilizers.

These proofs give the corrected content of Takesaki XIII.2.16–2.21. The printed XIII.2.17 omits the diagonal phase: its matrix intertwining determines support on a graph, and unitarity determines modulus one, not the value one. The existing programme proof already supplies this correction. The next sections retain the full sigma-finite scope while identifying the standard implementations and their weight derivatives.

## 3. The geometric unitary and its density

For \(\phi\in\operatorname{Aut}(R)\), put

\[
 h_\phi=\frac{d(\phi_*\mu)}{d\mu}.
\]

This is positive and finite almost everywhere. It satisfies

\[
 \int_X F(x)h_\phi(x)\,d\mu(x)
       =\int_X F(\phi x)\,d\mu(x)
 \tag{RSY.7}
\]

for nonnegative measurable \(F\), including infinite integrals. Define

\[
 (W_\phi\xi)(y,x)
   =h_\phi(x)^{1/2}
      \xi(\phi^{-1}y,\phi^{-1}x).
 \tag{RSY.8}
\]

For each source \(x\), \(\phi^{-1}\) bijects its orbit with the orbit of \(\phi^{-1}x\). Reindexing that counting sum and then using (RSY.7) proves

\[
 \|W_\phi\xi\|^2
 =\int_Xh_\phi(x)
       \sum_{z\sim\phi^{-1}x}
           |\xi(z,\phi^{-1}x)|^2\,d\mu(x)
 =\|\xi\|^2.
\]

Change of variables also proves the density chain rule

\[
 h_{\phi\psi}(x)
 =h_\phi(x)h_\psi(\phi^{-1}x).
 \tag{RSY.9}
\]

For example insert \(F(\phi z)\) into (RSY.7) for \(\psi\), then insert
\(F(x)h_\psi(\phi^{-1}x)\) into it for \(\phi\). The two integrals agree, so uniqueness of the derivative gives (RSY.9). Consequently
\(W_\phi W_\psi=W_{\phi\psi}\) and \(W_\phi^{-1}=W_{\phi^{-1}}\); (RSY.8) is an onto unitary.

Direct substitution on the generators gives

\[
 \begin{aligned}
 W_\phi M_fW_\phi^*&=M_{f\circ\phi^{-1}},\\
 W_\phi V_\theta W_\phi^*
      &=V_{\phi\theta\phi^{-1}}.
 \end{aligned} \tag{RSY.10}
\]

Thus \(\beta_\phi=\operatorname{Ad}(W_\phi)|_M\) is a normal automorphism. On a bounded kernel it replaces \(a(y,x)\) by
\(a(\phi^{-1}y,\phi^{-1}x)\): in the convolution sum the two factors at the unchanged source cancel. This also follows for every bounded orbit matrix by reindexing its rows and columns.

We will need the derivative identity

\[
 \delta(\phi^{-1}y,\phi^{-1}x)
   =\frac{h_\phi(y)}{h_\phi(x)}\delta(y,x).
 \tag{RSY.11}
\]

To prove it, push the counting measures forward by
\(\Phi(y,x)=(\phi y,\phi x)\). Reindexing fibres gives
\(\Phi_*\nu_s=h_\phi(x)\nu_s\) and
\(\Phi_*\nu_r=h_\phi(y)\nu_r\). The derivative of the second pushed measure with respect to the first is therefore the right side of (RSY.11). Transporting the original derivative gives its left side. This proves the identity, including both endpoints, rather than assuming that \(\phi\) preserves the measure.

For an arbitrary orbit symmetry the pair \((\phi^{-1}x,x)\) need not belong to \(R\). Hence an expression \(\delta(\phi^{-1}x,x)\) cannot define its density in general. If \(\phi\in[R]\), the partial-map formula RWT.4 gives
\(h_\phi(x)=\delta(\phi^{-1}x,x)\). Formula (RSY.8) remains meaningful in the larger group.

## 4. Weight transport on the entire finite left ideal

Every diagonal-preserving normal automorphism has the unique form

\[
 \alpha=\alpha_c\beta_\phi,\qquad U=U_cW_\phi.
 \tag{RSY.12}
\]

The classification follows from Section 2: the restriction determines \(\phi\), and \(\alpha\beta_\phi^{-1}\) fixes \(D\) pointwise, hence determines \(c\). Our order means

\[
 \alpha(T_a)=T_{\,c(y,x)a(\phi^{-1}y,\phi^{-1}x)}.
 \tag{RSY.13}
\]

Since \(c(x,x)=1\), the diagonal expectation satisfies

\[
 E(\alpha(T))=E(T)\circ\phi^{-1}\qquad(T\in M).
 \tag{RSY.14}
\]

This is an identity of the diagonal entries of the full bounded orbit matrices; it is not limited to a dense set of finite kernels.

For a positive finite measurable density \(q\), set

\[
 \varphi_q(T)=\int_Xq\,E(T)\,d\mu,\qquad
 q^\alpha(x)=h_\phi(x)q(\phi^{-1}x).
 \tag{RSY.15}
\]

The phase is absent from \(q^\alpha\). Applying (RSY.14) to \(\alpha^{-1}(T)\) and (RSY.7) gives, for every \(T\ge0\),

\[
 \varphi_q\circ\alpha^{-1}=\varphi_{q^\alpha}.
 \tag{RSY.16}
\]

Both sides may be infinite. They are faithful normal semifinite weights by RWT-02–03.

The identity on squared norms gives the exact domain equality

\[
 \mathfrak n_{\varphi_{q^\alpha}}
       =\alpha(\mathfrak n_{\varphi_q}).
 \tag{RSY.17}
\]

In the fixed standard coordinates of RWT-05 their GNS maps are
\(\Lambda_q(T)(y,x)=q(x)^{1/2}(T_x)_{y,x}\). Equations (RSY.8), (RSY.13) and (RSY.15) now give

\[
 U\Lambda_q(T)
       =\Lambda_{q^\alpha}(\alpha(T))
       \quad(T\in\mathfrak n_{\varphi_q}).
 \tag{RSY.18}
\]

Indeed both coefficients are
\(c(y,x)h_\phi(x)^{1/2}q(\phi^{-1}x)^{1/2}
 (T_{\phi^{-1}x})_{\phi^{-1}y,\phi^{-1}x}\).
The equality is in \(H_\mu\), with integrability ensured by (RSY.17).

SF-12–13 prove that the canonical standard implementer acts by precisely (RSY.18). These GNS vectors are dense. Therefore \(U_cW_\phi\) is that implementer: it preserves the natural cone onto itself and commutes with \(J_\mu\). This proof uses the complete finite left ideal and works at infinite mass. As a direct check on the conjugation, (RSY.11) gives \(W_\phi J_\mu=J_\mu W_\phi\), while
\(c(y,x)=\overline{c(x,y)}\) gives \(U_cJ_\mu=J_\mu U_c\).

For two symmetries \((c,\phi)\) and \((d,\psi)\), their product is

\[
 (c,\phi)(d,\psi)
 =\bigl(c(d\circ\Phi^{-1}),\,\phi\psi\bigr),
 \qquad \Phi^{-1}(y,x)=(\phi^{-1}y,\phi^{-1}x).
 \tag{RSY.19}
\]

Conjugating \(m_d\) by \(W_\phi\) proves the formula, and (RSY.9) proves its density part. Thus the algebraic semidirect product has its stated order.

## 5. Relative operators with their transported domains

For two densities \(q_1,q_2\), RWT-04–05 prove

\[
 \begin{gathered}
 \kappa_{21}(y,x)=\frac{q_2(y)}{q_1(x)}\delta(y,x),\\
 \Delta_{\varphi_{q_2},\varphi_{q_1}}=m_{\kappa_{21}},\qquad
 D(m_{\kappa_{21}})=\{\xi:\kappa_{21}\xi\in H_\mu\}.
 \end{gathered} \tag{RSY.20}
\]

For any real \(a\), its \(a\)-th power has domain
\(\{\xi:\kappa_{21}^{a}\xi\in H_\mu\}\), including negative powers. Put \(q_i'=q_i^\alpha\). Equation (RSY.11) gives

\[
 \begin{aligned}
 \kappa_{21}(\phi^{-1}y,\phi^{-1}x)
 &=\frac{q_2(\phi^{-1}y)}{q_1(\phi^{-1}x)}
     \frac{h_\phi(y)}{h_\phi(x)}\delta(y,x)\\
 &=\frac{q_2'(y)}{q_1'(x)}\delta(y,x)
 =\kappa'_{21}(y,x).
 \end{aligned} \tag{RSY.21}
\]

For any measurable multiplier \(b\), the defining formula and unitarity give

\[
 \|(b\circ\Phi^{-1})U\xi\|_2=\|b\xi\|_2
 \tag{RSY.22}
\]

whenever either side is finite; the same change-of-variables equality holds with value \(+\infty\). It follows that

\[
 \begin{gathered}
 U D(m_{\kappa_{21}}^{\,a})=D(m_{\kappa'_{21}}^{\,a}),\\
 U\Delta_{\varphi_{q_2},\varphi_{q_1}}^{\,a}U^*
   =\Delta_{\varphi_{q_2'},\varphi_{q_1'}}^{\,a}.
 \end{gathered} \tag{RSY.23}
\]

These are equalities of closed operators on their full domains. Taking \(a=1/2\) and using \(UJ_\mu=J_\mu U\) also transports the full relative Tomita graph, not just its algebraic kernel core. The corresponding logarithm identity uses the domain
\(\{\xi:(\log\kappa_{21})\xi\in H_\mu\}\) and the same argument.

For imaginary powers the multipliers have modulus one and act everywhere. The normalized cocycle from RWT-06 consequently obeys

\[
 \begin{aligned}
 [D\varphi_{q_2'}:D\varphi_{q_1'}]_t
 &=M_{\left[(q_2/q_1)\circ\phi^{-1}\right]^{it}}\\
 &=\alpha\bigl([D\varphi_{q_2}:D\varphi_{q_1}]_t\bigr).
 \end{aligned} \tag{RSY.24}
\]

Both transported densities contain the same \(h_\phi\), which cancels. Normalization here is inherited from RWT-06's relative-operator definition; a modular intertwining formula by itself would allow an undetermined scalar character.

Taking \(q=1\) gives the useful special case

\[
 \begin{gathered}
 \varphi_\mu\circ\alpha^{-1}=\varphi_{h_\phi},\qquad
 [D(\varphi_\mu\circ\alpha^{-1}):D\varphi_\mu]_t=M_{h_\phi^{it}},\\
 U\Delta_{\varphi_\mu}U^*
   =m_{\,[h_\phi(y)/h_\phi(x)]\delta(y,x)},\\
 \Delta_{\varphi_{h_\phi},\varphi_\mu}
   =m_{\,h_\phi(y)\delta(y,x)}.
 \end{gathered} \tag{RSY.25}
\]

The last two operators are different: one is the transported individual modular operator, the other compares two weights in the fixed standard form.

The automorphism preserves \(\varphi_\mu\) exactly when \(h_\phi=1\). Indeed equality of these weights on every diagonal indicator gives
\(\int_Bh_\phi\,d\mu=\mu(B)\) for all finite-measure \(B\), and uniqueness of densities gives the assertion. It commutes with the modular flow exactly when

\[
 h_\phi(y)=h_\phi(x)\quad\text{on }R.
 \tag{RSY.26}
\]

For the forward direction, covariance of the modular action and (RSY.25) give
\(\operatorname{Ad}(M_{h_\phi^{it}})=\mathrm{id}_M\) for every \(t\). Thus these unitaries are central, so their functions are orbit invariant by the center theorem in Section 1. Intersecting the conull sets for rational \(t\), continuity of \(t\mapsto e^{it\log h_\phi(x)}\) gives (RSY.26). The reverse implication makes every such unitary central, proving equality of the two modular flows. Hence preservation of the flow need not preserve the weight: even an invariant nonunit density changes the latter.

## 6. Changing coordinates and recognizing geometric symmetries

Replace \(\mu\) by \(q\mu\). Its geometric density is

\[
 h_\phi^{(q)}(x)
   =\frac{q(\phi^{-1}x)}{q(x)}h_\phi(x).
 \tag{RSY.27}
\]

Integrating against \(q\mu\) and using (RSY.7) proves this identity. In the coordinates (RSY.4),

\[
 V_qW_\phi^{(q)}V_q^*=W_\phi,\qquad
 V_qU_c^{(q)}V_q^*=U_c.
 \tag{RSY.28}
\]

For the first formula the scalar factor is
\(q(x)^{1/2}
 [q(\phi^{-1}x)h_\phi(x)/q(x)]^{1/2}
 q(\phi^{-1}x)^{-1/2}=h_\phi(x)^{1/2}\).
All maps in (RSY.28) are unitaries between the specified spaces, even when the individual scalar functions are unbounded.

This proves that the standard implementers and their strong topology are independent of the equivalent measure used for the earlier probability-space symmetry proofs. The u-topology is pointwise norm convergence on \(M_*\); CL-01 proves that it agrees exactly with the strong topology of these canonical implementers.

Let

\[
 C_\mu=\{\xi\in H_\mu:\xi(y,x)\ge0\text{ almost everywhere}\}.
\]

The positive density and reindexing in \(W_\phi\) preserve this cone onto itself. Therefore \(U_cW_\phi C_\mu=C_\mu\) exactly when \(c=1\). For necessity, test multiplication by \(c\) on indicators from a countable finite-\(\nu_s\)-measure cover of \(R\). It must be nonnegative almost everywhere; its modulus is one, so it equals one. Sufficiency is immediate. Notice that every standard implementer preserves the natural cone, whereas only geometric ones preserve \(C_\mu\). These two cones are different.

It follows, with the complete closedness and Polish-group proof in the prerequisite's Theorem 5.3, that
\(\mathcal G=\{\beta_\phi:\phi\in\operatorname{Aut}(R)\}\)
is closed in \(\operatorname{Aut}(M)\) and is Polish. The closedness proof uses both a convergent standard unitary and its convergent adjoint, so cone preservation is onto at the limit. Its separable complete metric comes from testing both unitaries and adjoints on a countable dense set of Hilbert vectors. Standard Borel sigma-finite measure and a countable graph cover make \(H_\mu\) separable, just as in the probability model.

In the ergodic case,

\[
 \mathcal G\cap\operatorname{Int}(M)=\{\beta_\theta:\theta\in[R]\}
 \tag{RSY.29}
\]

is Borel. The same theorem proves this through a Borel scalar-phase transversal for \(\mathcal U(M)\) and the one-to-one Borel image theorem; factoriality is used in identifying equal inner automorphisms modulo scalars. It does not assert this subgroup is closed. The explicit binary-tail counterexample and its strong convergence proof are Exercise 6.7 of that lesson.

For later use we can also read off all inner automorphisms within (RSY.12):

\[
 \begin{gathered}
 \alpha_c\beta_\phi\text{ is inner}\quad\Longleftrightarrow\\
 \phi\in[R]\text{ and }c(y,x)=b(y)\overline{b(x)}\\
 \text{for some measurable }b:X\to\mathbb T.
 \end{gathered} \tag{RSY.30}
\]

This equivalence does not need ergodicity. If the product is \(\operatorname{Ad}u\), then \(u\) normalizes \(D\), so its diagonal motion \(\phi\) is in \([R]\) by the normalizer theorem. For such a \(\phi\), \(\beta_\phi=\operatorname{Ad}V_\phi\): both sides conjugate diagonal functions and partial orbit maps in the same way. Removing this inner automorphism leaves \(\alpha_c\) inner, hence a coboundary by Theorem 4.1. Conversely the two indicated factors are \(\operatorname{Ad}M_b\) and \(\operatorname{Ad}V_\phi\), so their product is \(\operatorname{Ad}(M_bV_\phi)\).

## 7. Finite and infinite checks

**A symmetry between different orbits.** Let \(X=\{a,b\}\), \(R=\{(a,a),(b,b)\}\), \(\mu(a)=1/3,\mu(b)=2/3\), and let \(\phi\) exchange the points. It preserves \(R\), but belongs to neither orbit's full group. Its density is \(h_\phi(a)=2,h_\phi(b)=1/2\). Formula (RSY.8) is a unitary on the two-dimensional weighted space: it sends the normalized diagonal vector at either point to that at the other. The expression \(\delta(\phi^{-1}x,x)\) is undefined at both points. Here every individual modular operator is \(1\), whereas the relative operator for the transported weight is \(\operatorname{diag}(2,1/2)\), and its normalized cocycle is \(\operatorname{diag}(2^{it},2^{-it})\). The automorphism commutes with the trivial modular flow but does not preserve the weight.

**Unbounded density at infinite mass.** Let \(X=\mathbb Z\), give \(n\) mass \(p_n=e^{n^2}\), and take the complete relation, presented by the countable group of finite permutations. The shift \(\phi(n)=n+1\) is in its full group, even though it need not be a chosen presenting generator. Then

\[
 \delta(i,j)=e^{i^2-j^2},\qquad
 h_\phi(n)=e^{1-2n}.
 \tag{RSY.31}
\]

Both \(\mu\) and \(\phi_*\mu\) have infinite mass. The normalized arrow vectors
\(f_{ij}=p_j^{-1/2}\mathbf1_{\{(i,j)\}}\) form an orthonormal basis, and

\[
 \begin{aligned}
 W_\phi f_{ij}&=f_{i+1,j+1},\\
 \Delta_{\varphi_\mu}f_{ij}&=e^{i^2-j^2}f_{ij},\\
 U\Delta_{\varphi_\mu}U^*f_{ij}
     &=e^{(i-1)^2-(j-1)^2}f_{ij},\\
 \Delta_{\varphi_{h_\phi},\varphi_\mu}f_{ij}
     &=e^{1-2i+i^2-j^2}f_{ij}.
 \end{aligned} \tag{RSY.32}
\]

For each multiplier the full operator domain consists of coefficient arrays for which the sum of squared coefficients times the square of its displayed eigenvalue is finite. The shift permutes exactly these domains as asserted in (RSY.23).

The vector

\[
 \xi=\sum_{k\ge1}\frac{e^{-k}}{\sqrt{k}}\,f_{-k,-k}
\]

has finite squared norm \(\sum e^{-2k}/k\), but

\[
 \bigl\|\Delta_{\varphi_{h_\phi},\varphi_\mu}^{1/2}\xi\bigr\|^2
       =e\sum_{k\ge1}\frac1k=+\infty.
 \tag{RSY.33}
\]

Thus even the relative square-root domain is proper. Nevertheless
\([D\varphi_{h_\phi}:D\varphi_\mu]_t=M_{e^{it(1-2n)}}\)
is an everywhere-defined strongly continuous unitary group, by dominated convergence. Unbounded density causes a real-power domain restriction, not a failure of the imaginary powers.

**Phases versus measured arrows.** On a full two-point relation, \(M_{\operatorname{diag}(1,i)}\) is a normalizer with identity motion. Its inner automorphism fixes every diagonal weight. If a presenting group has a nontrivial stabilizer character, that character need not give a relation cocycle: the unit arrow must have value one. Equation (RSY.6), and the explicit \(\mathbb Z\times C_2\) example in prerequisite Exercise 6.3, detect the obstruction.

## 8. Problems with complete solutions

**Problem 1.** Determine the inverse of \((c,\phi)\) in (RSY.19), and check the inverse density.

**Solution.** It is

\[
 (c,\phi)^{-1}=(\overline c\circ\Phi,\phi^{-1}),
 \qquad \Phi(y,x)=(\phi y,\phi x).
\]

Insert this into (RSY.19); the phase becomes \(c\overline c=1\) in either order. Taking \(\psi=\phi^{-1}\) in (RSY.9) gives
\(h_{\phi^{-1}}(\phi^{-1}x)=h_\phi(x)^{-1}\).
This is the reciprocal needed in the inverse of (RSY.8).

**Problem 2.** For \(\alpha=\alpha_c\beta_\phi\), compute
\([D(\varphi_q\circ\alpha^{-1}):D\varphi_q]_t\). Does it depend on \(c\)?

**Solution.** RWT-06 and (RSY.15–16) give

\[
 [D(\varphi_q\circ\alpha^{-1}):D\varphi_q]_t
   =M_{\left[h_\phi(q\circ\phi^{-1})/q\right]^{it}}.
\]

It is independent of the phase. All ratios are positive and finite almost everywhere, so every imaginary power is defined on all of \(H_\mu\), whether or not the ratio or its logarithm is bounded.

**Problem 3.** Let \(B\subset X\) have positive measure. Identify the image of the standard corner for \(B\) under \(U_cW_\phi\), with no finite-mass assumption.

**Solution.** RWT-07 identifies it with \(L^2(R_B,\nu_s)\), where both endpoints lie in \(B\). Formula (RSY.8) sends this support to \(R_{\phi B}\); multiplication by \(c\) does not change support. Hence

\[
 U(eJ_\mu eJ_\mu)U^*
    =e'J_\mu e'J_\mu,\qquad
 e=M_{\mathbf1_B},\quad e'=M_{\mathbf1_{\phi B}}.
\]

The same unitary restricts onto these corner spaces. Formula (RSY.22) with the support indicators proves transport of every full relative-power domain in the corner, and (RSY.17) transports the corner finite ideals. The weights on these corners can be infinite.

**Problem 4.** State the additional condition for a diagonal-fixing automorphism to be inner. Explain why the one-orbit argument does not automatically establish that condition on a general measured relation.

**Solution.** Formula (RSY.16) with \(\phi=\mathrm{id}\) fixes each \(\varphi_q\), for every relation cocycle \(c\). Innerness additionally requires \(c\) to be a coboundary by Theorem 4.1. On a countable single orbit every cocycle is a coboundary, by choosing a basepoint and putting \(b(y)=c(y,x_0)\). On a general measured relation this construction would require a measurable choice of basepoints; the argument for one orbit does not provide it. Thus weight preservation establishes no such extra condition.

## References

The symmetry statements correspond to Masamichi Takesaki, *Theory of Operator Algebras III*, Chapter XIII, Section 2, Propositions 2.16–2.17, Corollary 2.19, Theorem 2.21 and Proposition 2.22, pp. 24–27. [Publisher record](https://doi.org/10.1007/978-3-662-10453-8). The phase correction to Proposition 2.17 and the general Radon–Nikodym implementer replacing equation (36′) are already explained in the cited programme symmetry lesson. The complete programme arguments are located in Section 1; Sections 3–6 above prove the explicit weight and domain covariance. New exposition is independently written and released under CC0.

