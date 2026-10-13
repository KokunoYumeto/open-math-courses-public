# Bounded vectors, affiliated multipliers and the complete dual Hilbert algebra

*CC0-1.0 to the extent of rights in this exposition.*

The Hilbert space is arbitrary. Inner products are linear in the first variable. The inputs are [CI-1–3](OA-FLOW-CI.md#oa-flow.ci.1), [BD-1–4](OA-FLOW-BD.md#oa-flow.bd.1), their exact spectral inputs, and only the closed-form representation proved in [FF-4](OA-FLOW-FF.md#oa-flow.ff.5). In particular the Fourier and modular parts of those later applications are not inputs here. The earlier Hilbert facts are [SF-0](OA-FLOW-SF.md#oa-flow.shared-foundations.sf-0) and [SB-0](OA-FLOW-SF.md#OA-FLOW.SF.SB0); the full spectral-domain proof is [SB-1–SB-6](OA-FLOW-SF.md#OA-FLOW.SF.SB1). Scalar spectral convergence uses [SC-04–05](OA-FLOW-SC.md#sc-04).

A free human development route is [Boey's institutional thesis, Definitions 4.1/4.3 and Lemmas 4.6–4.10, printed pp.25–31](https://dspacemainprd01.lib.uwaterloo.ca/server/api/core/bitstreams/245c2a41-48ee-4c8d-ad38-95a8353dc3d1/content#page=31). The bounded-vector construction has this mathematical antecedent. Here the graph-core proof uses an explicit pair of resolvents and an adjoint-product calculation; the compact-cutoff identities are then derived for the later modular application.

<a id="oa-flow.ha-r.1"></a>

## HA-R1. The initial algebra and its bounded right vectors

Let \(\mathcal A\) be a dense complex algebra in \(H\), with a conjugate-linear involution \(a\mapsto a^\#\), such that \(\mathcal A^2\) is dense, each left multiplication \(\lambda_a b=ab\) is bounded in the Hilbert norm, \(\langle ab,c\rangle=\langle b,a^\#c\rangle\), and the involution is closable. Here \(\mathcal A^2\) means the linear span of products. Then
\(\lambda_{ab}=\lambda_a\lambda_b\) and \(\lambda_{a^\#}=\lambda_a^*\). The representation is nondegenerate because the span of its ranges contains \(\mathcal A^2\). It is faithful: if \(\lambda_a=0\), then \(b^\#a^\#=0\) for all \(b\); nondegeneracy makes the common kernel zero, hence \(a^\#=a=0\).

Let \(M=\lambda(\mathcal A)''\), \(N=M'\), \(S=\overline{\#}\) and \(F=S^*\). CI proves that both \(S,F\) are closed densely defined conjugate-linear involutions. Call \(\eta\in H\) right bounded when the map \(a\mapsto\lambda_a\eta\) on \(\mathcal A\) is bounded in \(\|a\|_H\); denote its extension by \(R_\eta\). Write \(B_r\) for these vectors. Associativity on \(\mathcal A\) gives \(R_\eta\in N\). The map \(\eta\mapsto R_\eta\) is injective, because \(R_\eta=0\) implies \(\lambda_a\eta=0\) for every \(a\). For \(x\in N\),
\[
x\eta\in B_r,\qquad R_{x\eta}=xR_\eta.
\tag{HR1}
\]
Consequently \(I=\{R_\eta:\eta\in B_r\}\) is a linear left ideal of \(N\).

<a id="oa-flow.ha-r.2"></a>

## HA-R2. Adjoint products and the candidate dual algebra

For \(\eta,\zeta\in B_r\), one has
\[
R_\eta^*\zeta\in D(F),\qquad F(R_\eta^*\zeta)=R_\zeta^*\eta.
\tag{HR2}
\]
Indeed for \(a\in\mathcal A\),
\[
\langle R_\eta^*\zeta,Sa\rangle
=\langle\zeta,\lambda_{a^\#}\eta\rangle
=\langle\lambda_a\zeta,\eta\rangle
=\langle a,R_\zeta^*\eta\rangle.
\]
Since \(\mathcal A\) is a graph core for \(S\), the identity extends to \(D(S)\) and is exactly the conjugate-linear adjoint criterion. By (HR1), this vector is also right bounded, with multiplier \(R_\eta^*R_\zeta\).

Put \(\mathcal D=B_r\cap D(F)\). For \(\eta\in\mathcal D\), the identity
\(\langle R_\eta a,b\rangle=\langle\eta,a^\#b\rangle
=\langle b^\#a,F\eta\rangle=\langle a,\lambda_bF\eta\rangle\)
shows that
\[
F\eta\in B_r,\qquad R_{F\eta}=R_\eta^*.
\tag{HR3}
\]
Thus \(\mathcal D\) is invariant under the involution \(F\). Define
\[
\eta\zeta=R_\zeta\eta\quad(\eta,\zeta\in\mathcal D),\qquad
R_{\eta\zeta}=R_\zeta R_\eta.
\tag{HR4}
\]
Membership in \(\mathcal D\) follows before any involution calculation: the vector is \(R_{F\zeta}^*\eta\), to which (HR2) applies. That formula then gives
\[
F(\eta\zeta)=R_\eta^*F\zeta=(F\zeta)(F\eta).
\tag{HR5}
\]
Associativity follows either by applying the bounded multipliers or by their injective reversed representation. Right multiplication is bounded, and its adjoint is right multiplication by \(F\zeta\), by (HR3). Also
\[
I^*I\subseteq R(\mathcal D).
\tag{HR6}
\]
Here and below products of linear operator spaces denote finite sums of products. Density and the core assertion will be proved, rather than included in the definition of \(\mathcal D\).

<a id="oa-flow.ha-r.3"></a>

## HA-R3. The closed multiplier associated to any adjoint-domain vector

For \(\eta\in D(F)\), define \(T_\eta^0a=\lambda_a\eta\) on \(\mathcal A\). The same adjoint pairing as above gives
\[
\mathcal A\subseteq D((T_\eta^0)^*),\qquad
(T_\eta^0)^*a=\lambda_aF\eta.
\tag{HR7}
\]
Thus \(T_\eta^0\) is closable. Write \(T_\eta=\overline{T_\eta^0}\). Then
\[
\mathcal A\subseteq D(T_\eta)\cap D(T_\eta^*),\qquad
T_\eta a=\lambda_a\eta,\quad T_\eta^*a=\lambda_aF\eta.
\tag{HR8}
\]
The second formula uses equality of the adjoints of an operator and its closure. It does not assert that \(\mathcal A\) is a core for \(T_\eta^*\), or that \(T_{F\eta}=T_\eta^*\).

The graph of \(T_\eta^0\), and then its closure, is invariant under every \(\lambda_b\oplus\lambda_b\), by associativity and boundedness. It is invariant under their adjoints as well. Hence its orthogonal projection has all four entries in \(N\). It therefore commutes with \(x\oplus x\) for \(x\in M\). For every unitary \(x\in M\),
\[
xD(T_\eta)=D(T_\eta),\qquad T_\eta x=xT_\eta.
\tag{HR9}
\]
This is affiliation with \(N\). Taking adjoints gives the corresponding statement for \(T_\eta^*\).

BD-1 supplies a net \(\lambda_{a_i}\to I\) strongly; no norm bound is needed here. Testing only the fixed vectors \(\eta,F\eta\) in (HR8) gives
\[
T_\eta a_i\longrightarrow\eta,\qquad
T_\eta^*a_i\longrightarrow F\eta.
\tag{HR10}
\]
Thus \(\eta\in\overline{\operatorname{Ran}T_\eta}\) and
\(F\eta\in\overline{\operatorname{Ran}T_\eta^*}\). Actual range membership is neither proved nor used.

<a id="oa-flow.ha-r.4"></a>

## HA-R4. Closed linear polar decomposition with its domains

We supply the precise unbounded linear polar result needed next. Let \(T\) be any closed densely defined linear operator on \(H\). Its closed form \(q(v,w)=\langle Tv,Tw\rangle\) on \(D(T)\) has, by FF-4, a positive self-adjoint representative \(A\) with
\[
D(A^{1/2})=D(T),\qquad
\langle Tv,Tw\rangle=\langle A^{1/2}v,A^{1/2}w\rangle.
\tag{HR11}
\]
The representative satisfies \(v\in D(A)\) exactly when \(v\in D(A^{1/2})\) and there is \(z\in H\) such that \(q(v,w)=\langle z,w\rangle\) for every \(w\in D(A^{1/2})\), and then \(Av=z\). To check the nontrivial implication directly, test on each spectral subspace \(E_A([0,n])H\). One obtains \(E_A([0,n])z=A E_A([0,n])v\). These norms are bounded by \(\|z\|\); spectral monotone convergence gives \(v\in D(A)\) and \(Av=z\). Applied to \(q\), this criterion is exactly \(Tv\in D(T^*)\), with \(z=T^*Tv\). Hence \(A=T^*T\) on the full product domain.

Set \(h=A^{1/2}\). The rule \(u(hv)=Tv\) defines an isometry from \(\operatorname{Ran}h\) onto \(\operatorname{Ran}T\), extends to their closures, and is set to zero on \(\ker h\). The resulting partial isometry has initial space \((\ker T)^\perp\) and final space \(\overline{\operatorname{Ran}T}\). The adjoint pairing gives
\[
T=uh,\qquad T^*=hu^*,\qquad
D(T^*)=\{w:u^*w\in D(h)\}.
\tag{HR12}
\]
Write \(p=u^*u,q=uu^*\). Transport \(h|_{pH}\) by the unitary \(u:pH\to qH\), and set it equal to zero on \(q^\perp H\). This defines a positive self-adjoint \(k\). Direct substitution in (HR12) shows \(k^2=TT^*\), with the full product domain, so \(k=(TT^*)^{1/2}\). It also proves
\[
T=ku,\qquad u f(h)=f(k)u
\tag{HR13}
\]
for Borel functions with \(f(0)=0\), including equality of the transported domains. The first equality has domain \(\{v:uv\in D(k)\}=D(h)=D(T)\); the kernel summands cause no loss.

If \(T\) is affiliated with \(N\), every unitary of \(N'\) commutes with \(T,T^*\), their positive products and their spectral projections. Uniqueness of the isometry defined on \(\operatorname{Ran}h\) makes it commute with \(u\) as well. The commutant-unitary test proved in SF-0 then gives \(u,p,q\in N\), and \(h,k\) are affiliated with \(N\).

<a id="oa-flow.ha-r.5"></a>

## HA-R5. Resolvent pairs give the graph core

Fix \(\eta\in D(F)\), and use HA-R4 for \(T=T_\eta=uh=ku\). We first record a bounded multiplier calculation. If \(\phi\) is a bounded Borel function on \([0,\infty)\) and \(t\phi(t)\) is bounded, then
\[
 R_{\phi(k)\eta}=k\phi(k)u,\qquad
 R_{\phi(h)F\eta}=h\phi(h)u^*.
 \tag{HR14}
\]
In particular both vectors are right bounded. To prove this, commute the bounded operator \(\phi(k)\) past \(\lambda_a\), for \(a\in\mathcal A\), and use (HR8): \(\lambda_a\phi(k)\eta=\phi(k)T a=k\phi(k)u a\). The other formula uses \(T^*a=\lambda_a F\eta\), only on its already proved test domain. This calculation makes no assertion about \(F\phi(k)\eta\); that domain statement comes next.

**Two resolvents and one adjoint pairing.** For \(\epsilon,\delta>0\), put
\[
 r(t)=\frac1{1+\epsilon t^2},\qquad
 s(t)=\frac1{\delta+t^2},\qquad
 \chi(t)=t^2r(t)s(t).
 \tag{HR-R1}
\]
The functions \(r,s,ts\), as well as their products with \(t\), are bounded. Define three right-bounded vectors
\[
 a=u r(h)F\eta,\qquad b=u s(h)F\eta,\qquad c=k s(k)\eta .
\]
Equations (HR1), (HR13) and (HR14) give
\[
 R_a=k r(k),\qquad R_b=k s(k),\qquad R_c=k^2s(k)u.
\]
All operators displayed here are bounded; in transporting \(h\) and \(k\), the scalar functions being transported vanish at zero. Now apply (HR2), rather than assume that \(F\) commutes with a spectral multiplier:
\[
 R_a^*c=\chi(k)\eta\in\mathcal D,\qquad
 F(\chi(k)\eta)=R_c^*a=\chi(h)F\eta .
 \tag{HR-R2}
\]
For the last equality, substitute the three bounded formulas to obtain
\(u^*k^2s(k)u r(h)F\eta=h^2s(h)r(h)F\eta\).
Also
\(R_a^*R_b=\chi(k)\in I^*I\subseteq R(\mathcal D)\).
The vectors \(u^*r(k)\eta,u^*s(k)\eta\) have multipliers \(hr(h),hs(h)\), respectively. Their adjoint product similarly proves \(\chi(h)\in R(\mathcal D)\).

Thus \(\chi(k)^2\eta\) is a product of two members of \(\mathcal D\): one application of \(\chi(k)\) puts the vector in \(\mathcal D\), and the second is multiplication by a represented member of \(\mathcal D\). The same holds for \(\chi(h)^2F\eta\). Their bounded right multipliers, computed by (HR14), are adjoints:
\[
 \big(k\chi(k)^2u\big)^*=h\chi(h)^2u^* .
\]
Using (HR3) and injectivity of \(R\), we obtain the full-domain identity
\[
 \chi(k)^2\eta\in\mathcal D^2,\qquad
 F(\chi(k)^2\eta)=\chi(h)^2F\eta .
 \tag{HR-R3}
\]

Choose \(\epsilon=\delta=1/n\), and denote the resulting function by
\[
 \chi_n(t)=\frac{t^2}{(t^2+1/n)(1+t^2/n)}.
\]
For \(t>0\), both factors \(t^2/(t^2+1/n)\) and \(1/(1+t^2/n)\) increase to one; hence \(0\leq\chi_n(t)\uparrow1\). At zero, \(\chi_n(0)=0\). By (HR10), \(\eta\) is in the support of \(k\) and \(F\eta\) is in the support of \(h\). Spectral dominated convergence therefore gives
\[
 \big(\chi_n(k)^2\eta,\ F(\chi_n(k)^2\eta)\big)
 \longrightarrow(\eta,F\eta).
 \tag{HR-R4}
\]
This proves that \(\mathcal D^2\), and consequently \(\mathcal D\), are graph cores for \(F\). In particular they are dense in \(H\). The sequence depends on the fixed vector \(\eta\); it imposes no separability assumption on \(H\).

**Compact cutoffs for the later modular argument.** We also prove the precise compact-cutoff statements used downstream. Let \(f\in C_c((0,\infty))\), extended by zero. Set
\[
 v(t)=\frac{(1+t^2)f(t)}{t^2},\qquad
 w(t)=\frac{(1+t^2)f(t)}t,
\]
with value zero at zero. Both functions are bounded and supported away from zero, and so are \(tv\) and \(tw\). The right-bounded vectors
\[
 a=u(1+h^2)^{-1}F\eta,\qquad b=u v(h)F\eta,\qquad c=w(k)\eta
\]
have multipliers \(k(1+k^2)^{-1},kv(k),kw(k)u\). Consequently
\[
 R_a^*R_b=f(k)\in R(\mathcal D),\qquad
 R_a^*c=f(k)\eta\in\mathcal D,\qquad
 F(f(k)\eta)=R_c^*a=\overline f(h)F\eta .
\]
The symmetric operator calculation, using \(u^*(1+k^2)^{-1}\eta\) and \(u^*v(k)\eta\), gives \(f(h)\in R(\mathcal D)\).
Choose a real compactly supported \(f_1\) equal to one on the support of \(f\). Then \(f(k)\eta=f_1(k)[f(k)\eta]\in\mathcal D^2\). The same reasoning gives \(\overline f(h)F\eta\in\mathcal D^2\). It also gives \(f(h),f(k)\in R(\mathcal D^2)\), by factoring \(f=f_1 f\) within the represented algebra. In particular, for real \(f\),
\[
 F(f(k)\eta)=f(h)F\eta .
 \tag{HR15}
\]
Every vector in this equality has already been placed in its domain.

For an explicit compact family, define \(g(t)=1\) on \(0<t\leq1\), \(g(t)=2-t\) on \(1\leq t\leq2\), and \(g(t)=0\) on \(t\geq2\). Set \(f_n(t)=g(t/n)g(1/(nt))\). These functions have support in \([1/(2n),2n]\), satisfy \(0\leq f_n\uparrow1\) on \((0,\infty)\), and give
\[
 f_n(k)\eta\in\mathcal D^2,\qquad
 f_n(k)\eta\longrightarrow\eta,\qquad
 F(f_n(k)\eta)=f_n(h)F\eta\longrightarrow F\eta .
 \tag{HR16}
\]
This supplies the compact family as a consequence of the explicit adjoint-pairing calculation; the graph-core proof above already follows from the resolvents.

<a id="oa-flow.ha-r.6"></a>

## HA-R6. The represented dual generates the whole commutant

The algebra \(\mathcal D\), with its involution \(F\), is now a right Hilbert algebra: all its algebra/adjoint axioms were proved in HA-R2, its products are dense by HA-R5, and its involution has closure \(F\). Its right representation is nondegenerate. BD-3 gives positive contractions \(c_i\in R(\mathcal D)\) converging strongly to \(I\). For \(x\in N_+\), (HR1) gives \(x^{1/2}c_i\in I\), so
\[
c_i x c_i=(x^{1/2}c_i)^*(x^{1/2}c_i)\in I^*I\subseteq R(\mathcal D).
\tag{HR17}
\]
The common bound on \(c_i\) makes \(c_i x c_i\to x\) strongly. Every element of \(N\) is a complex linear combination of four positive elements, by the positive/negative spectral parts of its real and imaginary parts. The reverse inclusion was established in HA-R1. Hence
\[
R(\mathcal D)''=N=M'.
\tag{HR18}
\]

<a id="oa-flow.ha-r.7"></a>

## HA-R7. The original product core and the full adjoint intersection

We still need the graph core of the original products; using only their Hilbert density would be insufficient. Fix \(a\in\mathcal A\), rescaling so that \(\|\lambda_a\|\leq1\). Let \(p\in M\) be the projection onto \(\overline{\operatorname{Ran}\lambda_a}\). For \(d\in\mathcal D\), \(R_da=\lambda_a d\in pH\). Since \(p\) commutes with \(R_d\), this implies \(R_d(pa-a)=0\) for every \(d\). Nondegeneracy of \(R(\mathcal D)\) makes its common kernel zero, so \(pa=a\). Applying the same argument to \(a^\#\) gives the corresponding support statement for \(\lambda_a^*\).

Put \(p_n(t)=1-(1-t)^n\) on \([0,1]\). These polynomials vanish at zero and increase to one on \((0,1]\). Algebraic expansion gives
\[
a_n=p_n(\lambda_a\lambda_a^*)a\in\mathcal A^2,\qquad
a_n^\#=p_n(\lambda_a^*\lambda_a)a^\#.
\tag{HR19}
\]
For the second identity, a monomial on the left is \((aa^\#)^j a\); its involution is \(a^\#(aa^\#)^j=(a^\#a)^j a^\#\). The support statements and spectral dominated convergence show \(a_n\to a\), \(a_n^\#\to a^\#\). As \(\mathcal A\) itself is a core for \(S\), a diagonal choice of these approximants proves that \(\mathcal A^2\) is a graph core for \(S\).

Suppose \(\eta,\zeta\in B_r\) and \(R_\eta^*=R_\zeta\). For \(b,c\in\mathcal A\),
\[
\langle\eta,b^\#c\rangle
=\langle R_\eta b,c\rangle
=\langle b,R_\zeta c\rangle
=\langle c^\#b,\zeta\rangle.
\tag{HR20}
\]
Set \(a=c^\#b\); linearity extends this to the span \(\mathcal A^2\). The preceding graph core extends it to all \(a\in D(S)\), proving \(\eta\in D(F)\) and \(F\eta=\zeta\). Together with (HR3), this gives the exact operator-space equality
\[
R(\mathcal D)=I\cap I^*.
\tag{HR21}
\]

<a id="oa-flow.ha-r.8"></a>

## HA-R8. Exact modular uses and the arbitrary-weight boundary

HA-R1–2 and HA-R7 supply the bounded-vector ideal, adjoint-product and adjoint-intersection inputs previously taken from HA-05, HA-08 and RD-07. HA-R3–6 supply the affiliated multiplier, its test-domain adjoint formulas, both polar decompositions, cutoff involution identity, graph-core density and commutant-generation inputs previously taken from RD-02–06. The opposite-algebra version has the same proof with left and right exchanged; it uses the same arbitrary Hilbert space and no countability assumption.

In the later application, the WH-04 proof supplies the second-dual fullness statement and equality of its closed involution with \(S\). Applied to a full left Hilbert algebra, HA-R3–5 give precisely the closed left-multiplier and cutoff identities needed in MF-06's resolvent argument; CI supplies its polar and imaginary-power facts. Thus the replacement preserves the general Hilbert-algebra scope of those analytic inputs. It does not replace the later MF-06 modular averaging certificate or its whole bounded-vector conclusion.

These constructions do not assert that an arbitrary n.s.f. weight's finite-star GNS algebra satisfies the initial Hilbert-algebra axioms, do not reconstruct a weight from a full left Hilbert algebra, and do not prove the order/ultraweak characterization of arbitrary normal weights. The later [WF construction and domain transport](OA-FLOW-WF.md#oa-flow.wf.6), [all-weight normality](OA-FLOW-EW.md#ew-5) and [faithful finite-star closability](OA-FLOW-WR.md#wr-3)–[reverse/opposite finite-cone correspondence](OA-FLOW-WR.md#wr-6) supply these separate branches. They are not premises of this pure Hilbert-algebra provider.

![Exact graph spectrum and cutoff functions](../assets/modular-ancestry/assets/graph-polar-cutoff.png)

Original CC0 illustration. The left panel shows the reciprocal scalar spectrum in CI-2–3; the upper-right panel shows the exact compact cutoff functions of HA-R5, HR14–HR16; the middle row shows the squared rational regularizers and adjoint-pairing mechanism of HR-R1–HR-R4. The bottom row retains both Hilbert spaces and the full graph-domain identities. The sampled curves illustrate the proved formulas. [Reproduction source](../assets/modular-ancestry/render_graph_polar_cutoff.py) and [editable SVG](../assets/modular-ancestry/assets/graph-polar-cutoff.svg).
