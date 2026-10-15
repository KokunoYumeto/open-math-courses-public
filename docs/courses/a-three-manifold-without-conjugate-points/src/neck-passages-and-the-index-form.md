# Neck passages and the index form

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

By Proposition 2.3 of [Conjugate points and index forms](conjugate-points-and-index-forms.md), the metric of [A concave cometric and convex collars](a-concave-cometric-and-convex-collars.md) has no conjugate points as soon as the index form of every compactly supported field is nonnegative on every visit of a geodesic to the open neck. This lesson studies such visits. Concavity of the cometric makes the second variation of a variation that is linear in the neck coordinates nonnegative; it differs from the intrinsic index form by endpoint terms, which are nonnegative when the field is tangent to the boundary tori. Removing tangential components handles every visit except those that enter the neck, turn and return to the torus they came from; for these the lesson reduces the problem to an inequality between the coordinate energy, a boundary term and the change of the torus component of the field, proved in [Returning passages and the main theorem](returning-passages-and-the-main-theorem.md).

- Normal index forms (Section 1).
- Geodesics in the neck (Section 2).
- The coordinate second variation (Section 3).
- The possible passages (Section 4).
- Passages without a turning estimate, and the gauge on a returning passage (Section 5).

Throughout, \(\delta\in(0,\delta_0]\) is fixed, \(P\), \(Q=P^{-1}\), \(\kappa=\delta a(0)\) and \(b\) are as in [A concave cometric and convex collars](a-concave-cometric-and-convex-collars.md), and we work in the neck with coordinates \((t,x)\), \(x\in\mathbb R^2\) lifted from the torus. Near either boundary torus we may instead use the inward coordinate \(\tau\) and the end frame, in which, for \(-\frac12<\tau\le\frac14\),
\[
\begin{aligned}
&P(\tau)\\
&\quad=\operatorname{diag}(1+\delta A(\tau),\,b),\\
&P'(0)=\kappa e_1e_1^{\mathsf T} .
\end{aligned} \tag{0.1}
\]
For \(\tau\le0\) this is the metric of the collar of the core (Proposition 4.1 there), so the coordinates and (0.1) extend a little beyond each boundary torus. Changing between the coordinates of the two ends is a constant linear change of \(x\) together with \(\tau=1-t\).

## 1. Normal index forms

Let \(\gamma\) be a unit-speed geodesic of \(M\) and \(T=\dot\gamma\). For a smooth field \(V\) along \(\gamma\) and an interval \(J\) put
\[
\begin{aligned}
&q_V=\langle V,T\rangle,\\
&I_J^\perp(V)\\
&\quad=I_J(V)-\int_J|\dot q_V|^2\,ds,
\end{aligned} \tag{1.1}
\]
with \(I_J\) the index form of (2.1) in [Conjugate points and index forms](conjugate-points-and-index-forms.md). When \(J\) is unbounded we use only fields vanishing for large \(|s|\).

**Lemma 1.1** (tangential invariance; [OpenAI-NC, Lemma 4.1]). The integrand of \(I_J^\perp(V)\) is the index integrand of \(V^\perp=V-q_VT\). Consequently \(I_J^\perp(V+hT)=I_J^\perp(V)\) for every smooth function \(h\), whenever both sides are defined, with no condition on \(h\) at finite end points of \(J\). If every sectional curvature is nonpositive along \(\gamma(J)\), the integrand of \(I_J^\perp\) is nonnegative.

*Proof.* Since \(D_sT=0\) and \(\langle V^\perp,T\rangle=0\), also \(\langle D_sV^\perp,T\rangle=0\), so \(D_sV=D_sV^\perp+\dot q_VT\) and \(|D_sV|^2=|D_sV^\perp|^2+\dot q_V^2\). The curvature symmetries give \(\langle R(V,T)T,V\rangle=\langle R(V^\perp,T)T,V^\perp\rangle\). Adding \(hT\) does not change \(V^\perp\). The last assertion is (1.1) of that lesson. \(\square\)

## 2. Geodesics in the neck

On an interval of time during which \(\gamma\) stays in a coordinate region of the neck, write \(\gamma=(t,x)\). A dot denotes the derivative in the arc length \(s\) and a prime the derivative in \(t\) (or \(\tau\)).

**Lemma 2.1** (the neck geodesic equations). Along such a unit-speed geodesic,
\[
\begin{aligned}
&p=Q(t)\dot x\ \text{is constant},\\
&v:=\dot t,\qquad v^2=1-F(t),\\
&\dot v=-\tfrac12F'(t),
\end{aligned} \tag{2.1}
\]
where \(F(t)=p^{\mathsf T}P(t)p\). The function \(F\) is concave.

*Proof.* The geodesics are the critical curves of the energy \(\frac12\int(\dot t^2+\dot x^{\mathsf T}Q(t)\dot x)\,ds\). The coordinates \(x\) do not appear in the integrand, so the Euler–Lagrange equation for \(x\) says that \(Q\dot x\) is constant. The equation for \(t\) is \(\ddot t=\frac12\dot x^{\mathsf T}Q'\dot x\); since \(Q'=-QP'Q\) and \(\dot x=Pp\), this is \(-\frac12p^{\mathsf T}P'p=-\frac12F'\). Unit speed gives \(\dot t^2+\dot x^{\mathsf T}Q\dot x=v^2+p^{\mathsf T}Pp=1\). \(F''=p^{\mathsf T}P''p\le0\) by Lemma 2.1 of [A concave cometric and convex collars](a-concave-cometric-and-convex-collars.md). \(\square\)

The covector \(p\) transforms under \(x=Ty\) as \(p\mapsto T^{\mathsf T}p\), and \(F\) does not change. In the end coordinates near a boundary torus, (0.1) gives \(F(\tau)=(1+\delta A(\tau))p_1^2+bp_2^2\) and \(F'(\tau)=\delta a(\tau)p_1^2\) for \(-\frac12<\tau\le\frac14\); in particular \(F'(0)=\kappa p_1^2\).

## 3. The coordinate second variation

For a field \(V\) along \(\gamma\) in the neck, write \(V=(w,z)\): \(w\) is its \(t\)-component and \(z\in\mathbb R^2\) its torus components. Put \(|\xi|_Q^2=\xi^{\mathsf T}Q\xi\). On a compact interval \([a,c]\) of times in a coordinate region, the *coordinate energy* is
\[
\begin{aligned}
&E_{[a,c]}(V)=\int_a^c\Bigl(\dot w^2\\
&\quad+|\dot z-P'(t)p\,w|_Q^2\\
&\quad-\tfrac12F''(t)\,w^2\Bigr)ds .
\end{aligned} \tag{3.1}
\]
Every term is nonnegative, since \(F''\le0\). On an unbounded interval we use the same integral for fields vanishing for large \(|s|\).

**Lemma 3.1** (endpoint correction; [OpenAI-NC, Lemma 4.2]). For a smooth field \(V=(w,z)\) on \([a,c]\),
\[
\begin{aligned}
&I_{[a,c]}(V)=E_{[a,c]}(V)\\
&\quad-\bigl[\langle T,\Gamma(V,V)\rangle\bigr]_a^c,
\end{aligned} \tag{3.2}
\]
where \(\Gamma(V,V)\) is the vector with components \(\Gamma^k_{ij}V^iV^j\), the Christoffel symbols being those of the coordinates used, and the bracket means value at \(c\) minus value at \(a\). In the end coordinates of a boundary torus, at a time when \(\tau=0\) and \(w=0\),
\[
\begin{aligned}
\Gamma(V,V)&=\tfrac\kappa2\,z_1^2\,\partial_\tau,\\
\langle T,\Gamma(V,V)\rangle&=\tfrac\kappa2\,z_1^2\,\dot\tau .
\end{aligned} \tag{3.3}
\]
Hence the endpoint contribution in (3.2) is nonnegative at a time when \(\gamma\) enters or leaves the open neck through a boundary torus, provided \(w=0\) there.

*Proof.* Consider the variation \(\alpha(r,s)=(t(s)+rw(s),\,x(s)+rz(s))\), defined for small \(r\). Its energy is
\[
\begin{aligned}
&\frac12\int_a^c\bigl((\dot t+r\dot w)^2\\
&\qquad+(\dot x+r\dot z)^{\mathsf T}Q(t+rw)(\dot x+r\dot z)\bigr)ds,
\end{aligned}
\]
and its second derivative at \(r=0\) is
\[
\begin{aligned}
&\int_a^c\Bigl(\dot w^2+\dot z^{\mathsf T}Q\dot z+2w\,\dot z^{\mathsf T}Q'\dot x\\
&\qquad+\tfrac12w^2\,\dot x^{\mathsf T}Q''\dot x\Bigr)ds .
\end{aligned}
\]
With \(Q'=-QP'Q\), \(Q''=2QP'QP'Q-QP''Q\) and \(\dot x=Pp\), we get \(\dot z^{\mathsf T}Q'\dot x=-\dot z^{\mathsf T}QP'p\) and \(\dot x^{\mathsf T}Q''\dot x=2(P'p)^{\mathsf T}Q(P'p)-F''\); completing the square gives \(E_{[a,c]}(V)\). On the other hand, by the second variation formula ([Jacobi fields, conjugate points and the Morse index theorem](course:DG-FND/jacobi-fields-conjugate-points-and-the-morse-index-theorem), Theorem A.4) the second derivative of the energy is \(I_{[a,c]}(V)+[\langle A,T\rangle]_a^c\), where \(A=D_r\partial_r\alpha|_{r=0}\). For each \(s\), \(r\mapsto\alpha(r,s)\) has coordinate acceleration \(0\), so \(A=\Gamma(V,V)\). This proves (3.2).

For \(g=dt^2+dx^{\mathsf T}Q(t)dx\), the nonzero Christoffel symbols are, with torus indices \(i,j\),
\[
\begin{aligned}
\Gamma^t_{ij}&=-\tfrac12Q'_{ij},\\
\Gamma^i_{tj}&=\Gamma^i_{jt}=\tfrac12(PQ')^i{}_j .
\end{aligned}
\]
If \(w=0\), only \(\Gamma^t_{ij}z^iz^j=-\frac12z^{\mathsf T}Q'z\) remains. At \(\tau=0\) in end coordinates, (0.1) gives \(Q(0)e_1=e_1\) and \(Q'(0)=-Q(0)P'(0)Q(0)=-\kappa e_1e_1^{\mathsf T}\), so \(\Gamma(V,V)=\frac\kappa2z_1^2\partial_\tau\); and \(\langle T,\partial_\tau\rangle=\dot\tau\). The variation \(\alpha\) is linear in both coordinate systems, because they differ by an affine change, so \(\Gamma(V,V)\) may be computed in either. At an entry time \(a\), \(\dot\tau>0\) and the term \(+\frac\kappa2z_1(a)^2\dot\tau(a)\) appears in (3.2); at an exit time \(c\), \(\dot\tau<0\) and \(-\frac\kappa2z_1(c)^2\dot\tau(c)\) appears. Both are nonnegative. \(\square\)

## 4. The possible passages

A *neck passage* of \(\gamma\) is a connected component \(J\) of \(\{s\in\mathbb R:\gamma(s)\in U\}\), where \(U=(0,1)\times T\) is the open neck. A field along \(\gamma\) vanishing outside a compact set may have arbitrary values at the finite end points of \(J\).

**Lemma 4.1** (passage classification; [OpenAI-NC, Lemma 4.3]). At every finite end point of a neck passage, \(\gamma\) is transverse to the boundary torus: \(\dot\tau\ne0\) in the inward coordinate. Exactly one of the following holds.

1. The passage is \(\mathbb R\) and \(t\) is constant.
2. \(v=\dot t\) never vanishes on the passage. The passage is either a bounded interval joining the two boundary tori, or a half-line on which \(t\) tends monotonically to a height \(t_\infty\in(0,1)\) with \(F(t_\infty)=1\) and \(F'(t_\infty)=0\).
3. In the coordinates of one boundary torus, and after a translation of the parameter, the passage is \((0,L)\) with \(L>0\); it begins and ends at that torus and has a unique turn at \(s=L/2\).

We call passages of the third kind *returning passages*. For a returning passage, with \(\tau_*=\tau(L/2)\),
\[
\begin{aligned}
&\tau(0)=\tau(L)=0,\\
&v(0)=-v(L)=v_0>0,\\
&\tau(L-s)=\tau(s),\\
&v(L-s)=-v(s),\\
&\tau_*\in(0,1),\quad p_1\ne0,\\
&0<F'\le\kappa p_1^2\ \text{ on }[0,\tau_*],\\
&v_0^2=F(\tau_*)-F(0)\le\kappa p_1^2 .
\end{aligned} \tag{4.1}
\]
A geodesic tangent to a boundary torus at some time does not enter the open neck at that time.

*Proof.* *Transversality.* Use end coordinates at a finite end point \(s_0\), so \(\tau(s_0)=0\), and suppose \(\dot\tau(s_0)=0\). By (2.1) and \(F'(0)=\kappa p_1^2\), \(\ddot\tau(s_0)=-\frac\kappa2p_1^2\). If \(p_1\ne0\), \(s_0\) is a strict local maximum of \(\tau\), so \(\tau<0\) at nearby times on both sides, and \(s_0\) is not an end point of a passage. If \(p_1=0\), then \(F\) is constant near \(\tau=0\) by (0.1), and the solution of \(\ddot\tau=-\frac12F'(\tau)\) with \(\tau(s_0)=\dot\tau(s_0)=0\) is \(\tau\equiv0\) near \(s_0\), by uniqueness for the geodesic equations; again \(s_0\) is not an end point. The same argument shows the last assertion.

*An interior zero of \(v\).* Let \(v(s_*)=0\) inside a passage. If also \(F'(t(s_*))=0\), the constant height \(t(s_*)\) solves the equations with the same data, so \(t\) is constant for all time and the passage is \(\mathbb R\). Otherwise \(s_*\) is a strict local extremum of \(t\). Using the coordinates of the torus on the appropriate side, we may assume it is a maximum \(\tau_*\) of \(\tau\), with \(c:=F'(\tau_*)>0\). Since \(F\) is concave, \(F'\ge c\) on \([0,\tau_*]\), so \(\dot v=-\frac12F'\le-\frac c2\) while \(0\le\tau\le\tau_*\). After the turn \(v\) is negative and decreasing, so \(\tau\) cannot turn again, and \(\tau(s)\le\tau_*-\frac c4(s-s_*)^2\) as long as \(\gamma\) stays in the neck; hence \(\tau\) reaches \(0\) in finite time. Reversing time maps geodesics to geodesics with the same \(p\) up to sign, and \(F\) is even in \(p\); by uniqueness \(\tau(s_*-r)=\tau(s_*+r)\). Translating the parameter gives the first four lines of (4.1), except \(v_0>0\), which is shown at the end. Concavity gives \(F'(\tau)\le F'(0)=\kappa p_1^2\) for \(\tau\ge0\), so \(p_1\ne0\) because \(F'(\tau_*)>0\). Finally \(v^2=1-F\) vanishes at the turn, so
\[
\begin{aligned}
v_0^2&=F(\tau_*)-F(0)=\int_0^{\tau_*}F'(u)\,du\\
&\le\kappa p_1^2\tau_*\le\kappa p_1^2 ,
\end{aligned}
\]
and \(v_0>0\) by transversality.

*No zero of \(v\).* Then \(t\) is strictly monotone on the passage. If both end points are finite, they lie on boundary tori, and monotonicity forces the two different tori. At an infinite end, \(t\) has a limit \(t_\infty\) by monotonicity; \(v^2=1-F(t)\) shows that \(|v|\) has a limit, which is \(0\) because \(t\) is bounded; so \(F(t_\infty)=1\). Since \(\dot v\to-\frac12F'(t_\infty)\) and \(v\to0\), also \(F'(t_\infty)=0\). If \(t_\infty\) were \(0\) or \(1\), then in end coordinates \(F'(0)=\kappa p_1^2=0\), so \(F\) would be constant on the end portion \(0\le\tau\le\frac14\), equal to \(F(t_\infty)=1\), and \(v\) would vanish there, which is impossible on this passage. So \(t_\infty\in(0,1)\). Two infinite ends are impossible: the two limiting heights would be different, with \(F=1\) at both, so \(F\ge1\) between them by concavity, whereas \(F=1-v^2<1\) at every height the passage traverses. \(\square\)

## 5. Passages without a turning estimate, and the gauge on a returning passage

**Lemma 5.1** ([OpenAI-NC, Lemma 4.4]). Let \(V\) be the restriction to a neck passage \(J\) of a smooth field along \(\gamma\) that vanishes outside a compact set. If \(J=\mathbb R\), or \(v\) never vanishes on \(J\), or \(J\) is a returning passage with \(\tau_*\le\frac14\), then \(I_J^\perp(V)\ge0\).

*Proof.* *\(J=\mathbb R\).* Replace \(V\) by \(V^\perp\), which vanishes outside a compact set and has \(q_{V^\perp}=0\). Apply (3.2) on an interval whose end points lie outside the support: there are no endpoint terms, and \(I_J^\perp(V)=I_J(V^\perp)=E_J(V^\perp)\ge0\) by Lemma 1.1.

*\(v\ne0\) on \(J\).* On \(J\) put \(\widetilde V=V-\frac wvT\), whose \(t\)-component is \(0\). It is smooth up to the finite end points of \(J\), where \(v\ne0\) by transversality, and it vanishes where \(V\) does, in particular for large \(|s|\) at an infinite end; no bound on \(1/|v|\) is used. Write \(\widetilde V=(0,\tilde z)\); then \(q_{\widetilde V}=\tilde z^{\mathsf T}Q\dot x=p^{\mathsf T}\tilde z\). By Lemma 1.1 and by (3.2), whose endpoint terms are nonnegative at entries and exits and vanish beyond the support,
\[
\begin{aligned}
&I_J^\perp(V)=I_J^\perp(\widetilde V)\\
&\quad\ge\int_J\bigl(|\dot{\tilde z}|_Q^2-(p^{\mathsf T}\dot{\tilde z})^2\bigr)ds\\
&\quad\ge\int_J\bigl(1-F(t)\bigr)|\dot{\tilde z}|_Q^2\,ds\ge0 .
\end{aligned}
\]
The second inequality is the Cauchy–Schwarz inequality \((p^{\mathsf T}\xi)^2\le(p^{\mathsf T}Pp)(\xi^{\mathsf T}Q\xi)\) for the positive definite \(Q=P^{-1}\), and \(1-F=v^2\ge0\).

*\(\tau_*\le\frac14\).* The passage stays in the end portion, where every sectional curvature is nonpositive (Proposition 4.1 of [A concave cometric and convex collars](a-concave-cometric-and-convex-collars.md)), and Lemma 1.1 makes the integrand of \(I_J^\perp\) nonnegative. \(\square\)

Only returning passages with \(\tau_*>\frac14\) remain. On them we normalize the field without imposing anything on its values at the ends.

**Lemma 5.2** (the gauge on a returning passage; [OpenAI-NC, Lemma 4.5]). Consider a returning passage with the data (4.1). For every smooth field \(V\) on \([0,L]\) there is a smooth function \(h\) such that \(\widetilde V=V+hT=(w,z)\) satisfies
\[
\begin{aligned}
&w(0)=w(L)=0,\\
&\langle\widetilde V,T\rangle\ \text{is affine in }s .
\end{aligned}
\]
With \(\Delta z=z(L)-z(0)\), \(e=(1,0)^{\mathsf T}\) and \(\mu=\kappa v_0/4>0\),
\[
\begin{aligned}
&I_{[0,L]}^\perp(V)=E_{[0,L]}(\widetilde V)\\
&\quad+\tfrac{\kappa v_0}2\bigl(z_1(0)^2+z_1(L)^2\bigr)\\
&\quad-\frac{(p^{\mathsf T}\Delta z)^2}L\\
&\ge E_{[0,L]}(\widetilde V)+\mu\,(e^{\mathsf T}\Delta z)^2\\
&\quad-\frac{(p^{\mathsf T}\Delta z)^2}L .
\end{aligned} \tag{5.1}
\]

*Proof.* Let \(q=\langle V,T\rangle\) and \(V=(w_0,z_0)\) in coordinates. Put \(h_0=-w_0(0)/v_0\) and \(h_L=w_0(L)/v_0\), let \(\ell\) be the affine function with \(\ell(0)=q(0)+h_0\) and \(\ell(L)=q(L)+h_L\), and take \(h=\ell-q\). Then \(\langle\widetilde V,T\rangle=q+h=\ell\), and the \(t\)-component of \(\widetilde V\) is \(w_0+hv\), which vanishes at \(0\) because \(v(0)=v_0\) and at \(L\) because \(v(L)=-v_0\). If \(V\) is given along the whole geodesic, multiplying \(h\) by a smooth cutoff equal to \(1\) on \([0,L]\) gives a change vanishing outside a compact set; nothing on \([0,L]\) changes.

At \(s=0\) and \(s=L\) the field \(\widetilde V\) has \(w=0\), so \(\langle\widetilde V,T\rangle=z^{\mathsf T}Q\dot x=p^{\mathsf T}z\) there, and the slope of \(\ell\) is \(p^{\mathsf T}\Delta z/L\); hence \(\int_0^L\dot\ell^2=(p^{\mathsf T}\Delta z)^2/L\). By (3.3), with \(\dot\tau(0)=v_0\) and \(\dot\tau(L)=-v_0\), the endpoint terms of (3.2) are \(\frac\kappa2v_0z_1(0)^2\) and \(\frac\kappa2v_0z_1(L)^2\). Inserting into (1.1) and using Lemma 1.1 gives the identity in (5.1). The inequality follows from \(x^2+y^2\ge\frac12(y-x)^2\). \(\square\)

The gauges are chosen separately on each passage, and they need not match at the ends of different passages. Every inequality concerns the normal index form of the original field, which is unchanged by the gauge; only these integrals are added in Proposition 2.3 of [Conjugate points and index forms](conjugate-points-and-index-forms.md).

## 6. Exercises

**6.1.** Show that \(Q'=-QP'Q\) and \(Q''=2QP'QP'Q-QP''Q\).

**6.2.** Show that a geodesic with \(p=0\) in the neck is a straight line in the \(t\)-direction, and that it crosses the neck in time \(1\).

**6.3.** Let the cometric be constant, \(P(t)=P_0\). Show that \(E_{[a,c]}(V)=\int(\dot w^2+|\dot z|_Q^2)\) and that (3.2) has no endpoint terms. Deduce directly that the flat metric has no conjugate points.

**6.4.** In the situation of Lemma 4.1(3), show that \(L\ge4v_0/(\kappa p_1^2)\), using \(\dot v=-\frac12F'\) and \(F'\le\kappa p_1^2\).

**6.5.** Show that a unit-speed geodesic stays at a constant height \(t_0\in(0,1)\) exactly when \(F(t_0)=1\) and \(F'(t_0)=0\). Show that in an end portion \(0<\tau\le\frac14\) these are the geodesics with \(p_1=0\), which run along the circle factor, and check Lemma 5.1 for them.

## 7. Solutions

**6.1.** Differentiate \(QP=\operatorname{Id}\): \(Q'P+QP'=0\), so \(Q'=-QP'Q\). Differentiating again,
\[
\begin{aligned}
Q''&=-Q'P'Q-QP''Q-QP'Q'\\
&=2QP'QP'Q-QP''Q .
\end{aligned}
\]

**6.2.** With \(p=0\), \(\dot x=Pp=0\), \(F=0\) and \(v^2=1\), so \(t\) changes at unit speed.

**6.3.** \(P'=0\) and \(F''=0\) remove the extra terms in (3.1), and \(Q'=0\) makes all Christoffel symbols vanish. Then \(I=E\ge0\) for compactly supported fields, and Lemma 2.2 of the first lesson applies.

**6.4.** Integrating \(\dot v=-\frac12F'\) and using \(F'\le\kappa p_1^2\),
\[
\begin{aligned}
&v(L)-v(0)=-2v_0\\
&\quad=-\frac12\int_0^LF'(\tau(s))\,ds\ge-\frac12L\kappa p_1^2 ,
\end{aligned}
\]
so \(L\ge4v_0/(\kappa p_1^2)\).

**6.5.** At constant height \(v\equiv0\), so \(F(t_0)=1\) by \(v^2=1-F\) and \(F'(t_0)=0\) by \(\dot v=-\frac12F'\). Conversely, if \(F(t_0)=1\) and \(F'(t_0)=0\), then \(t\equiv t_0\), \(x(s)=x_0+sP(t_0)p\) solves (2.1) and the geodesic equations, and by uniqueness it is the geodesic with these data. In an end portion \(F'(\tau)=\delta a(\tau)p_1^2\) with \(a(\tau)>0\), so \(F'=0\) exactly when \(p_1=0\); then \(F=bp_2^2=1\) and \(\dot x=Pp\) is a multiple of \(e_2\), the direction of the circle factor. The passage is \(\mathbb R\), and \(I^\perp(V)=E(V^\perp)\ge0\) as in the proof of Lemma 5.1; here the curvature is also nonpositive.

## References

- [OpenAI-NC] OpenAI, *A Three-Manifold Without Conjugate Points and Without a Nonpositively Curved Metric*, OpenAI Math Release preprint, 24 September 2026, Section 4 (Lemmas 4.1–4.5). https://github.com/openai/math/tree/main/preprints/A-Three-Manifold-Without-Conjugate-Points-and-Without-a-Nonpositively-Curved-Metric-September-24-2026
