# Positive implementation from spectral tails

For a one-parameter automorphism action, the left supports of positive-frequency spectral subspaces form a decreasing family of central projections in the fixed-point algebra. Their high-frequency intersection detects whether the action has a positive-energy unitary implementation inside the algebra. When that intersection is zero, a left-continuous regularization of the support tails constructs a particular spectral measure and unitary group. The proof then verifies that the constructed group implements the original action by tracing how spectral elements move its tail ranges. This is Takesaki II, Theorem XI.1.10, with its choice of implementer and the compact-spectrum recovery step made explicit.

*New expression is dedicated under CC0 to the extent of rights held; inherited component terms remain in force.*

<a id="positiveflow.setting"></a>

## Criterion and spectral tail ranges

Let \(M\) be a von Neumann algebra with a point-ultraweakly continuous action \(\alpha:\mathbb R\to\operatorname{Aut}(M)\). Represent \(M\) faithfully and normally on a Hilbert space \(\mathcal H\), without a separability assumption. Use the positive Fourier convention of [MX1](OA-FLOW-MX.md#equation-mx1):
\[
 \mathcal Fa(p)=\int_{\mathbb R}a(t)e^{itp}\,dt,\qquad
 \alpha_f(x)=\int_{\mathbb R}a(t)\alpha_t(x)\,dt
 \quad(f=\mathcal Fa).
 \tag{C1}
\]
The integral on \(M\) is ultraweak. [AT3](OA-FLOW-AT.md#oa-flow.at.3) gives the norm-continuous predual orbits needed for the [BS1–BS3 filter laws](OA-FLOW-BS.md#bs-1). The positive-character spectrum here is the reflection of the negative-character spectrum in [GL](OA-FLOW-GL.md#gl-0): the two transforms of the same kernel satisfy \(\mathcal Fa(p)=\widehat a(-p)\), so their annihilator hulls have exactly opposite frequency coordinates. Hence our \(M_\alpha(E)\) is GL's \(M(-E)\). Reflection preserves addition and the fixed frequency zero. The product rule, adjoint reflection, closed-space test, compact cutoffs and empty-spectrum criterion all transport with this convention.

Let \(q(E)\) be the join of **left** supports of \(M_\alpha(E)\). The [FS2 support theorem](OA-FLOW-FS.md#fs-2), with its spectral set reflected, puts this join in \(Z(M^\alpha)\). It is the projection called \(p_{-E}\) in FS's notation; that lesson uses \(q\) for the right-support join. We use \(q(E)\) for the left join consistently throughout this lesson. Put

$$Q_t=q([t,\infty))\qquad(t\in\mathbb R). \tag{U1}$$

The family \(Q_t\) is decreasing, consists of projections in \(Z(M^\alpha)\), and satisfies \(Q_t=1\) for \(t\le0\) because \(1\in M_\alpha(\{0\})\). By the definition of a join of left supports,

$$Q_t\mathcal H
=\overline{\operatorname{span}}
\{x\eta:x\in M_\alpha([t,\infty)),\ \eta\in\mathcal H\}. \tag{U2}$$

For a family of projections, its join has range the closed span of their ranges; the range of \(l(x)\) is \(\overline{x\mathcal H}\). These two facts prove (U2), including when the spectral space is \(\{0\}\).

**Positive-implementation criterion.** The following are equivalent:

1. There is a strongly continuous unitary group \(u_s\in M\) with \(\alpha_s=\operatorname{Ad}u_s\) and nonnegative self-adjoint generator in the faithful representation.
2. \(\displaystyle\bigwedge_{t\in\mathbb R}Q_t=0\).

The first condition means that \(u_s=\int_{[0,\infty)}e^{is\lambda}\,dP(\lambda)\) for a projection-valued measure \(P\). The resulting generator may be unbounded; no norm continuity of \(s\mapsto u_s\) is claimed. The zero algebra has the unique zero-Hilbert-space implementation and satisfies both conditions. Below, arbitrary projection meets and their strong limits are the concrete ones proved in [PC1](OA-FLOW-PC.md#oa-flow.projection.pc1).

<a id="positiveflow.models"></a>

## Hilbert spectral spaces and normal inclusions

Here are the representation and topology facts used in both directions. A Hilbert space \(\mathcal H\), with inner product linear in its first variable, is the Banach dual of its conjugate Hilbert space under \(\langle\xi,\eta\rangle\), by [CF8](OA-FLOW-CF.md#oa-flow.cf.8). For a strongly continuous unitary group \(U_t\), the preadjoint is induced by \(U_t^*\), and its orbits are norm continuous. Every bounded operator between Hilbert spaces is weak-to-weak continuous because it has an adjoint. Thus these groups and all bounded operators satisfy the specified-dual hypotheses of [L80](OA-FLOW-L80.md#sum-claim) and [L81](OA-FLOW-L81.md#transfer-claim), at arbitrary Hilbert dimension.

Suppose \(U_t=\int e^{it\lambda}\,dP(\lambda)\). For \(a\in L^1(\mathbb R)\), scalar Fubini against the finite spectral coefficient measures gives
\[
 \int_{\mathbb R}a(t)U_t\,dt
       =\int_{\mathbb R}\mathcal Fa(\lambda)\,dP(\lambda).
 \tag{C2}
\]
The left integral exists strongly on each vector, with norm at most \(\|a\|_1\); [SF1–SF2](OA-FLOW-SF.md#oa-flow.sf.sf1) give the spectral calculus and unitary-group representation. The scalar interchange is justified by \(\int |a(t)|\,dt\) times the finite total variation of the coefficient measure. Consequently, for every closed \(E\subset\mathbb R\),
\[
 \mathcal H_U(E)=P(E)\mathcal H.
 \tag{C3}
\]
For one inclusion, a filter whose transform vanishes near \(E\) annihilates every vector in \(P(E)\mathcal H\). For the other, cover \(\mathbb R\setminus E\) by countably many compact intervals \(J\) with rational endpoints inside that open set. [LF1](OA-FLOW-LF.md#lf-1) supplies a compactly supported Fourier-algebra plateau equal to one on each \(J\), supported off \(E\). The closed-space annihilator test kills its filter on \(\xi\in\mathcal H_U(E)\); multiplying (C2) by \(P(J)\) gives \(P(J)\xi=0\). Countable additivity then gives \(P(\mathbb R\setminus E)\xi=0\), proving (C3). The empty set and whole line are included.

If \(U_t\) normalizes \(M\), the filter of \(x\in M\) computed in \(M\) and the filter computed in \(B(\mathcal H)\) agree. Indeed the normal inclusion carries the ultraweak integral to the same operator: pair with each vector functional, and then with the full summable vector series of [CP4–CP6](OA-FLOW-CP.md#oa-flow.cp.4). Absolute integrability is bounded by \(\|a\|_1\|x\|\) times the functional norm. Since the inclusion is injective, the two annihilator ideals, and therefore the two operator spectra, are identical. This justifies applying the Hilbert-space transfer theorems to an element originally described by its intrinsic \(M\)-spectrum.

<a id="positiveflow.necessity"></a>

## Necessity of the vanishing high-frequency tail

Suppose a positive-energy unitary group \(u\) implements \(\alpha\), and let \(P\) be its spectral measure. For \(t\le0\), the desired comparison \(Q_t\le P([t,\infty))\) is immediate because both sides equal \(1\). For general \(t\), take \(x\in M_\alpha([t,\infty))\) and \(\eta\in P([0,\infty))\mathcal H=\mathcal H\). The spectral theorem identifies the Hilbert-vector spectral space of the unitary action \(u\) at \([0,\infty)\) with \(P([0,\infty))\mathcal H\). Applying the [closed-set operator/vector spectral-sum theorem (T1)](OA-FLOW-L80.md#sum-claim) to \(x\) as an operator on \(\mathcal H\) gives

$$x\eta\in P([t,\infty))\mathcal H. \tag{U3}$$

The operator spectrum of \(x\) under \(\operatorname{Ad}u\) in \(B(\mathcal H)\) agrees with its spectrum under \(\alpha\) in \(M\): each Fourier filter has the same ultraweak integral in the normal inclusion \(M\subset B(\mathcal H)\). Taking the closed span in (U2) yields

$$Q_t\le P([t,\infty))\qquad(t\in\mathbb R). \tag{U4}$$

The tails of a projection-valued measure decrease strongly to zero as \(t\to+\infty\). Thus \(\bigwedge_t Q_t\le\bigwedge_tP([t,\infty))=0\), proving necessity. This argument would also work for a positive unitary group merely normalizing \(M\); the criterion itself asks for one inside \(M\).

<a id="positiveflow.measure"></a>

## Constructing the canonical positive measure

Assume \(\bigwedge_tQ_t=0\). Define a regularized decreasing family

$$E_t=\bigwedge_{r<t}Q_r\qquad(t\in\mathbb R). \tag{U5}$$

All \(Q_r\) lie in the abelian center \(Z(M^\alpha)\), so these meets commute and remain in that center. Also \(E_t=1\) for \(t\le0\), and \(\bigwedge_tE_t=0\): the latter follows because for every \(r\) some \(t>r\) has \(E_t\le Q_r\). The regularization is left-continuous in the order/strong-operator sense:

$$E_t=\bigwedge_{s<t}E_s. \tag{U6}$$

Indeed the right side is the meet of \(Q_r\) over all \(r<s<t\), the same index set as \(r<t\). We construct the projection-valued measure, including its endpoint convention. This avoids assuming a measure-extension theorem for a projection family.

Put \(F_0=1\), \(F_1=0\), and
\[
 F_a=E_{a/(1-a)}\quad(0<a<1).
 \tag{M1}
\]
These commuting projections decrease, satisfy \(F_a=\bigwedge_{b<a}F_b\) for \(0<a<1\), and have \(\bigwedge_{a<1}F_a=0\). For \(N=2^n\), form
\[
 A_n=\frac1N\sum_{k=1}^{N-1}F_{k/N}.
 \tag{M2}
\]
All sums are finite and belong to \(Z(M^\alpha)\). Comparing one interval with its two halves shows
\[
 0\le A_{n+1}-A_n\le 2^{-n-1}1.
 \tag{M3}
\]
For an explicit verification, the difference is \(1/(2N)\) times
\(\sum_{j=0}^{N-1}(F_{(2j+1)/(2N)}-F_{(j+1)/N})\), where \(F_1=0\). Each difference is a projection, and these projections are pairwise orthogonal because the underlying family is decreasing. Their sum is at most \(1\). Thus \(A_n\) converges in norm to a positive contraction \(A\in Z(M^\alpha)\), with
\[
 0\le A-A_n\le 2^{-n}1.
 \tag{M4}
\]

Fix \(0<a<1\). The projection \(F_a\) commutes with every \(A_n\), hence with \(A\). On \(F_a\mathcal H\), every grid term with \(k/N\le a\) is the identity, so \(A_n\ge(\lfloor Na\rfloor/N)F_a\) on this reducing subspace. On \((1-F_a)\mathcal H\), every term with \(k/N\ge a\) vanishes; at most \(\lceil Na\rceil-1\) terms remain. Passing to the limit gives
\[
 A|_{F_a\mathcal H}\ge a,\qquad
 A|_{(1-F_a)\mathcal H}\le a.
\]
The bounded spectral calculus from [SF, SB4 and SB6](OA-FLOW-SF.md#oa-flow.sf.sb4) therefore gives
\[
 1_{(a,1]}(A)\le F_a\le1_{[a,1]}(A).
 \tag{M5}
\]
For \(0<b<a\), \(1_{[a,1]}(A)\le1_{(b,1]}(A)\le F_b\). Taking the meet over \(b<a\) and using left continuity proves the exact equality
\[
 F_a=1_{[a,1]}(A)\quad(0<a<1).
 \tag{M6}
\]
The meet as \(a\uparrow1\) gives \(1_{\{1\}}(A)=0\). A zero eigenvalue is allowed.

Define \(g(a)=a/(1-a)\) for \(0\le a<1\), and assign any finite value at \(a=1\), whose spectral projection is zero. The full-domain measurable calculus of [SF1](OA-FLOW-SF.md#oa-flow.sf.sf1) constructs
\[
 L=g(A),\qquad
 D(L)=\left\{\xi:\int_{[0,1)}g(a)^2\,d\langle1_{da}(A)\xi,\xi\rangle<\infty\right\}.
 \tag{M7}
\]
It is positive and selfadjoint. Density of the domain also follows directly from the bounded cutoffs \(1_{[0,1-1/j]}(A)\uparrow1\). Define \(P_0(S)=1_{g^{-1}(S)}(A)\) for Borel \(S\subset\mathbb R\). The already proved spectral calculus makes \(P_0\) strongly countably additive; its total projection is \(1\), its support is in \([0,\infty)\), and (M6) gives
\[
 P_0([t,\infty))=E_t,\qquad
 P_0([a,b))=E_a-E_b\quad(a<b).
 \tag{U7}
\]
For \(t\le0\) the first identity is the endpoint \(E_t=1\); for \(t>0\) it is (M6) at \(a=t/(1+t)\).

These formulas determine \(P_0\) uniquely. If two projection measures agree on all half-open intervals, their finite scalar vector measures agree there and on rays by increasing limits. Let \(\Pi\) be this intersection-closed family together with the empty set and the whole line. For each fixed vector, the class where the two finite measures agree contains \(\Pi\) and is closed under complements and countable disjoint unions. Let \(\mathcal D\) be the smallest class with those closure properties containing \(\Pi\). Such a class is also closed under differences of nested members. For fixed \(A\in\Pi\), the class of \(B\) with \(A\cap B\in\mathcal D\) has the same closure properties and contains \(\Pi\), hence contains \(\mathcal D\). Now fix \(B\in\mathcal D\) and repeat with the class of \(A\) satisfying \(A\cap B\in\mathcal D\). Thus \(\mathcal D\) is intersection-closed; disjointifying any countable union makes it a sigma-algebra. Since \(\Pi\) generates the Borel sets, the two scalar measures agree on every Borel set. Polarization of their equal quadratic vector values gives equality of the projections.

Every spectral projection lies in \(Z(M^\alpha)\), by the bounded Borel calculus for \(A\) in this von Neumann algebra. Define

$$u_s=\int_{[0,\infty)}e^{is\lambda}\,dP_0(\lambda). \tag{U8}$$

The spectral theorem gives a strongly continuous unitary group in \(Z(M^\alpha)\subset M\) with nonnegative generator. Strong continuity follows by dominated convergence on each vector for the finite scalar measure \(\langle P_0(\cdot)\eta,\eta\rangle\). Applying this also to \(u_s^*=u_{-s}\) gives strong-star continuity. [CP4](OA-FLOW-CP.md#oa-flow.cp.4) extends bounded vector convergence to the normal vector-series seminorms, so this is the intrinsic sigma-strong-star continuity in \(M\). All projections of \(L\) are in \(M\), so \(L\) is affiliated with \(M\). [ST2](OA-FLOW-ST12.md#oa-flow.st.2) transports these bounded spectral projections, their normal integrals and the group continuity through any faithful normal representation; the criterion is intrinsic. Put \(\beta_s=\operatorname{Ad}u_s\). We still have to prove \(\beta=\alpha\); membership of \(u_s\) in the fixed-point algebra alone does not give this.

<a id="positiveflow.shift"></a>

## Spectral elements shift the constructed tails

Let \(x\in M_\alpha([r,\infty))\). The [GL6 product rule](OA-FLOW-GL.md#gl-6), with the frequency reflection specified in (C1), says

$$xM_\alpha([t,\infty))
\subset M_\alpha([r+t,\infty)). \tag{U9}$$

Apply (U9) to the spanning ranges in (U2). Boundedness of \(x\) permits closure, giving

$$xQ_t\mathcal H\subset Q_{r+t}\mathcal H. \tag{U10}$$

For every \(s<t\), \(E_t\le Q_s\), so (U10) gives \(xE_t\mathcal H\subset Q_{r+s}\mathcal H\). Intersecting over \(s<t\) and using (U5),

$$xE_t\mathcal H\subset E_{r+t}\mathcal H
\qquad(r,t\in\mathbb R). \tag{U11}$$

Under the unitary action \(u\) on \(\mathcal H\), the closed spectral space \(\mathcal H_u([t,\infty))\) is exactly \(P_0([t,\infty))\mathcal H=E_t\mathcal H\). The forward inclusion follows by filtering the spectral integral; the reverse follows because Fourier filters supported off the set separate its complementary spectral projection. Thus (U11) is a spectral-transfer statement for every translated half-line.

<a id="positiveflow.inclusion"></a>

## From a shifted transfer criterion to half-line inclusion

To obtain the correct frequency shift, fix \(r\) and define a target unitary action \(v_s=e^{-irs}u_s\) on \(\mathcal H\). Its spectral spaces satisfy \(\mathcal H_v([t,\infty))=\mathcal H_u([r+t,\infty))\). Equation (U11) becomes

$$x\mathcal H_u([t,\infty))
\subset\mathcal H_v([t,\infty))
\qquad(t\in\mathbb R). \tag{U12}$$

The regular closed set \([0,\infty)\) has translation semigroup \([0,\infty)\). Apply the reverse implication of Theorem XI.1.5, proved in [lesson 81](OA-FLOW-L81.md#transfer-claim), to \(x:\mathcal H\to\mathcal H\), input action \(u\), target action \(v\), and every translate of this half-line. The induced operator action is \(T\mapsto v_sTu_{-s}=e^{-irs}\beta_s(T)\). Character twisting shifts its spectrum by \(-r\). Explicitly, replacing a kernel \(a(s)\) by \(a(s)e^{-irs}\) replaces its positive Fourier transform \(f(p)\) by \(f(p-r)\); a frequency \(\lambda\) for \(\beta\) is therefore a frequency \(\lambda-r\) for the twisted action. Thus

$$\operatorname{Sp}_\beta(x)\subset[r,\infty)
\qquad\text{whenever}\qquad
x\in M_\alpha([r,\infty)). \tag{U13}$$

The spectrum can be computed in \(M\) or \(B(\mathcal H)\) for \(x\in M\), because the relevant integrated actions agree under the normal inclusion. Therefore (U13) is the one-sided half-line spectral-space inclusion

$$M_\alpha([r,\infty))\subset M_\beta([r,\infty))
\qquad(r\in\mathbb R). \tag{U14}$$

The twist in (U12)–(U13) is necessary: applying the unshifted criterion directly would only detect nonnegative operator frequencies and lose the threshold \(r\).

<a id="positiveflow.recovery"></a>

## Recovering compact spectral sets and the action

The [action-determination theorem BS7](OA-FLOW-BS.md#bs-7) asks for inclusion at every compact set, not just half-lines. We derive it. [GL2's adjoint reflection](OA-FLOW-GL.md#gl-2), reflected to (C1), and (U14) imply that for \(a\le b\),

$$M_\alpha([a,b])\subset M_\beta([a,b]). \tag{U15}$$

Indeed an \(\alpha\)-spectral element in \([a,b]\) lies in its lower half-line, while its adjoint lies in the lower half-line \([-b,\infty)\). Apply (U14) to both and reflect the adjoint back. The intersection of the resulting \(\beta\)-spectral half-lines is \([a,b]\).

Let \(K\subset\mathbb R\) be compact and \(x\in M_\alpha(K)\). If \(K\) is empty, the empty-spectrum criterion gives \(x=0\). Otherwise, fix an open neighborhood \(U\supset K\) and cover \(K\) by the interiors of finitely many compact intervals \(I_1,\ldots,I_N\subset U\). [LF4's local Fourier cutoffs and subordinate finite partition](OA-FLOW-LF.md#lf-4) produce \(c_i\in A_c(\mathbb R)\) with \(\operatorname{supp}c_i\subset I_i\) and \(c=\sum_i c_i=1\) on a neighborhood of \(K\). This is the same finite cutoff construction used in [LF6–LF7's local ideal lemma](OA-FLOW-LF.md#lf-6).

The filter \(\alpha_c\) fixes \(x\). To justify this without treating \(1\) as an element of \(A(\mathbb R)\), take any \(f\in A(\mathbb R)\) and approximate it in \(A\)-norm by \(A_c\)-functions \(f_n\). Each \(f_n(1-c)\) is compactly supported away from \(K\), so the local ideal lemma makes its filter annihilate \(x\). Passing to the \(A\)-norm limit gives \(\alpha_f(x-\alpha_cx)=0\) for every \(f\); the empty-spectrum criterion gives \(x=\alpha_cx\). Hence

$$x=\sum_{i=1}^N\alpha_{c_i}x. \tag{U16}$$

Each summand has \(\alpha\)-spectrum in \(I_i\) by [BS3 filter localization](OA-FLOW-BS.md#bs-3), hence \(\beta\)-spectrum in \(I_i\) by (U15). The spectrum of a finite sum lies in the union of the summands' spectra, so \(\operatorname{Sp}_\beta(x)\subset\bigcup_iI_i\subset U\). As this holds for every open \(U\supset K\), closedness gives \(\operatorname{Sp}_\beta(x)\subset K\). Thus

$$M_\alpha(K)\subset M_\beta(K)
\qquad\text{for every compact }K\subset\mathbb R. \tag{U17}$$

[BS7](OA-FLOW-BS.md#bs-7), applied to the identity map on the specified dual \(M=(M_*)^*\), now gives \(\alpha=\beta=\operatorname{Ad}u\). This completes sufficiency and the criterion. \(\square\)

<a id="positiveflow.choice"></a>

## The constructed measure is a choice, not every choice

Formula (U5) determines the particular measure \(P_0\) constructed from the action's intrinsic support tails. It does not identify the spectral measure of every positive-energy implementing unitary group. For the trivial action on a nonzero algebra, the only frequency of a nonzero spectral element is \(0\). Thus \(Q_t=1\) for \(t\le0\) and \(Q_t=0\) for \(t>0\); (U5) gives a point mass at \(0\), and (U8) gives \(u_s=1\). Yet \(e^{ics}1\), for any \(c>0\), also implements the trivial action and has positive spectral mass at \(c\). The criterion asserts existence, and (U5) selects one implementation.


<a id="positiveflow.examples"></a>

## Two exact tail computations

**A finite positive gap.** In \(M_2(\mathbb C)\), let \(H=\operatorname{diag}(0,3)\) and \(\alpha_t=\operatorname{Ad}(e^{itH})\). The matrix unit \(e_{ij}\) has frequency \(h_i-h_j\) under (C1), since \(\alpha_t(e_{ij})=e^{it(h_i-h_j)}e_{ij}\); applying filters and LF1 proves this singleton spectrum exactly. Thus
\[
 Q_t=
 \begin{cases}
 1,&t\le0,\\
 e_{22},&0<t\le3,\\
 0,&t>3.
 \end{cases}
 \tag{D1}
\]
The regularized tails \(E_t\) have the same values, including \(E_3=e_{22}\). Hence the constructed generator is exactly \(\operatorname{diag}(0,3)\). The mass at the endpoint \(3\) confirms why (U7) uses closed tails and left continuity.

**An unbounded lower energy cannot be removed.** On \(\ell^2(\mathbb Z)\), let \(He_n=ne_n\) on the square-summable weighted domain and let \(M=B(\ell^2(\mathbb Z))\). This diagonal operator is selfadjoint by the explicit multiplication calculus, and \(U_t e_n=e^{itn}e_n\) is strongly continuous by dominated convergence. Its conjugation action is point-ultraweakly continuous by the same vector-series estimate used above. For any real threshold \(t\) and every integer \(n\), choose an integer \(m\le n-t\). Then \(e_{nm}\) has frequency \(n-m\ge t\) and left support \(e_{nn}\). Their left supports join to \(1\), so \(Q_t=1\) at every threshold. The criterion proves that this action has no positive internal implementing group. This conclusion is stronger than observing that the displayed \(H\) is unbounded below: it rules out every other positive internal choice.

The mathematical source is M. Takesaki, *Theory of Operator Algebras II*, Theorem XI.1.10 and equation (12), printed pages 320–321 ([edition record](https://doi.org/10.1007/978-3-662-10451-4)). The criterion retains arbitrary von Neumann algebras and faithful normal representations, with no separability, factor or finite-state assumption.
