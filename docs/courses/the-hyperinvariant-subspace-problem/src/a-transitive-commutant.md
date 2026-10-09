# A backward intertwiner and a transitive commutant

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson completes the proof of OpenAI's theorem [OAI]: on every infinite-dimensional separable complex Hilbert space there is a nonzero operator \(T\) with \(\lim_n\|T^n\|^{1/n}=0\) that has no hyperinvariant subspace other than \(\{0\}\) and the whole space. Its commutant is a weakly closed, unital, transitive algebra different from \(B(H)\).

The operator is the field \(S\) of weighted shifts \(S_x\) built in [the previous lesson](measurable-fields-of-weighted-shifts.md), on \(H_0=L^2(X\times\mathbb Z,\mu\otimes\#)\), where \(X\) is the space of \(2\)-adic digit sequences, \(\mu\) its product measure and \(\theta\) the odometer. Its fibres have only the tails \(K_{\ge h}\) as invariant subspaces. We add an operator \(V\) in the commutant of \(S\) that carries the fibre over \(x\) to the fibre over \(\theta x\) and moves every tail one step backward. Section 1 records how the logarithmic weights change along \(\theta\): they increase at one end of the integer line and decrease at the other. Section 2 uses these opposite changes to solve the commutation equation for \(V\) with coefficients that decay at both ends. Section 3 proves that a strictly decreasing label along the orbits of an ergodic measure-preserving map cannot exist. Section 4 combines these facts: a closed subspace invariant under \(S\), \(V\) and the scalar multipliers is \(\{0\}\) or \(H_0\). Section 5 states the theorem and its corollary, and Section 6 describes further structure of the example.

We use the notation of the previous lesson: the residues \(T_m\), the blocks \(I_m\), the constants \(c=10\), \(D=100\), the logarithmic weights \(a_j\) and \(a^\pm_k\), the conull \(\theta\)-invariant set \(X_*\) of sequences that are not eventually constant (Exercise 5.3 there), decomposable operators (Lemma 2.1 there) and fields of projections (Theorem 2.2 there). From [the first lesson](weighted-shifts-whose-invariant-subspaces-are-tails.md) we use Lemma 1.1 on commutants. We also use: Proposition 2.1 and Definition 2.3 of [the double commutant lesson](course:foundations-of-von-neumann-algebras/the-double-commutant-theorem#oa-fnd-bi-02), and its uniqueness lemma for measures in [Section 9](course:foundations-of-von-neumann-algebras/the-double-commutant-theorem#oa-fnd-bi-18); orthonormal bases, [Theorem 4.1 of the Hilbert space lesson](course:foundations-of-von-neumann-algebras/hilbert-spaces-and-compact-operators#OA-FND-HS-04), and its Theorem 9.1 on multiplication operators; and for Section 6, Lemma 1.1 and Theorem 3.1 of [the spectral theorem lesson](course:foundations-of-von-neumann-algebras/the-spectral-theorem-for-bounded-self-adjoint-operators#OA-FND-ST-03), and the Weierstrass approximation theorem, [Corollary 14.3 of the Stone–Weierstrass lesson](course:function-algebras-and-approximation/the-stone-weierstrass-theorem-for-functions-vanishing-at-infinity#OA-FND-SW-14).

## 1. Two-ended drift

Put \(\Delta a_k(x)=a_k(\theta x)-a_k(x)\) for \(k\in\mathbb Z\).

**Lemma 1.1.** For \(k\in I_m\),
\[
a^+_k(\theta x)-a^+_k(x)=D-DN_m1_{\{T_m=N_m-1\}}(x),\qquad a^-_k(\theta x)-a^-_k(x)=-\big(a^+_k(\theta x)-a^+_k(x)\big).
\]
Both differences vanish for \(k=0\).

**Proof.** By (1.2) of the previous lesson, \(T_m(\theta x)-T_m(x)\) is \(1\), except that it is \(-(N_m-1)\) when \(T_m(x)=N_m-1\). In (3.1) of the previous lesson, \(T_m\) enters \(a^+_k\) with coefficient \(D\) and \(a^-_k\) with coefficient \(-D\). \(a^\pm_0=c\) is constant. \(\square\)

For \(x\in X_*\) only finitely many \(m\) satisfy \(T_m(x)=N_m-1\), so
\[
C(x)=D+D\sum_{m\ge1:\ T_m(x)=N_m-1}N_m|I_m|<\infty .
\]

**Lemma 1.2** (two-ended drift). For \(x\in X_*\) and all integers \(n,q\ge1\),
\[
\sum_{k=0}^{n-1}\Delta a_k(x)\ge Dn-C(x),\qquad\sum_{k=-q}^{-1}\Delta a_k(x)\le-Dq+C(x).
\]

**Proof.** For \(k\ge0\), \(\Delta a_k=a^+_k(\theta x)-a^+_k(x)\). By Lemma 1.1, grouping the indices \(1\le k<n\) by blocks,
\[
\sum_{k=0}^{n-1}\Delta a_k(x)=D(n-1)-D\sum_{m:\ T_m(x)=N_m-1}N_m\,\big|I_m\cap[1,n)\big|\ge D(n-1)-\big(C(x)-D\big).
\]
For \(k=-k'-1\le-1\), \(\Delta a_k=a^-_{k'}(\theta x)-a^-_{k'}(x)=-\Delta a_{k'}(x)\) with \(k'\ge0\). So the second sum is minus the first one with \(n=q\). \(\square\)

So along \(\theta\) the logarithmic weights increase at the right end of the integer line, at average rate \(D\) per index, and decrease at the same rate at the left end. The finitely many wrap-arounds of the residues cost at most \(C(x)\). This constant need not be bounded or integrable as a function of \(x\); only its finiteness at each point of \(X_*\) is used.

## 2. The backward intertwiner

We look for an operator \(V\) with \((Vf)(\theta x)=V_xf(x)\), where \(V_xe_j=b_j(x)e_{j-1}\) with \(b_j(x)\ge0\). On a basis vector \(e_j\) of the fibre over \(x\), the two compositions \(SV\) and \(VS\) end in the fibre over \(\theta x\):
\[
S_{\theta x}V_xe_j=b_j(x)\beta_{j-1}(\theta x)e_j,\qquad V_xS_xe_j=\beta_j(x)b_{j+1}(x)e_j .
\]
So \(V\) commutes with \(S\) exactly when
\[
b_{j+1}(x)\beta_j(x)=b_j(x)\beta_{j-1}(\theta x)\qquad(x\in X,\ j\in\mathbb Z).\tag{2.1}
\]

The base transformation is essential here. If \(\theta x\) were replaced by \(x\), (2.1) would force \(b_{j+1}/b_j=e^{a_j(x)-a_{j-1}(x)}\ge e^c\) for \(j\ge1\), by Proposition 3.1(1) of the previous lesson. Nonzero coefficients would then grow exponentially, and no bounded nonzero operator of this form could commute with a single fibre \(S_x\). Along \(\theta\), Lemma 1.2 reverses this growth at both ends.

Define \(\tilde b_0(x)=1\) and, for all \(j\in\mathbb Z\),
\[
\tilde b_{j+1}(x)=\tilde b_j(x)\,\frac{\beta_{j-1}(\theta x)}{\beta_j(x)} .
\]
This determines \(\tilde b_j(x)>0\) for all \(j\), forward and backward from \(j=0\); each \(\tilde b_j\) is a finite product of measurable functions and their reciprocals.

**Lemma 2.1.** For \(x\in X_*\) and \(n,q\ge1\),
\[
\log\tilde b_n(x)\le-(D-c)n+C(x)+4Dn^{1/3},\qquad\log\tilde b_{-q}(x)\le-(D-c)q+C(x)+4Dq^{1/3}.
\]
In particular \(\tilde b_j(x)\to0\) as \(j\to+\infty\) and as \(j\to-\infty\).

**Proof.** The recursion gives \(\log\tilde b_{j+1}-\log\tilde b_j=a_j(x)-a_{j-1}(\theta x)\). Summing over \(0\le j\le n-1\) and shifting the index in the second sum,
\[
\log\tilde b_n(x)=-\sum_{k=0}^{n-1}\Delta a_k(x)+a_{n-1}(\theta x)-a_{-1}(\theta x).
\]
Summing over \(-q\le j\le-1\) in the same way,
\[
\log\tilde b_{-q}(x)=\sum_{k=-q}^{-1}\Delta a_k(x)+a_{-q-1}(\theta x)-a_{-1}(\theta x).
\]
Here \(a_{-1}=c\), \(a_{n-1}=a^+_{n-1}\) and \(a_{-q-1}=a^-_q\). By Proposition 3.1(2) of the previous lesson, \(a^+_{n-1}(\theta x)-c\le c(n-1)+4D(n-1)^{1/3}\) (also for \(n=1\)) and \(a^-_q(\theta x)-c\le cq+4Dq^{1/3}\). Combine with Lemma 1.2. As \(D-c=90>0\), both bounds tend to \(-\infty\). \(\square\)

For \(x\in X_*\), the supremum \(L(x)=\sup_j\tilde b_j(x)\) is finite, at least \(\tilde b_0(x)=1\), and measurable as a countable supremum. Put
\[
b_j(x)=\begin{cases}\tilde b_j(x)/L(x),&x\in X_*,\\0,&x\notin X_*.\end{cases}
\]
Then \(0\le b_j\le1\), all \(b_j\) are positive on \(X_*\), and (2.1) holds for every \(x\): on \(X_*\) both sides of the recursion are divided by the same number \(L(x)\), and off \(X_*\) both sides vanish.

Let \(V_x\) be the operator \(V_xe_j=b_j(x)e_{j-1}\) on \(K\); it maps the basis to an orthogonal family, so \(\|V_x\|=\sup_jb_j(x)\le1\). Define
\[
(Vf)(y)=V_{\theta^{-1}y}\,f(\theta^{-1}y),\qquad\text{that is,}\qquad(Vf)(\theta x,j-1)=b_j(x)f(x,j).
\]

**Proposition 2.2.** \(V\) is a well-defined operator on \(H_0\) with \(\|V\|\le1\), and \(VS=SV\). For \(x\in X_*\) and \(h\in\mathbb Z\),
\[
\overline{V_xK_{\ge h}}=K_{\ge h-1},\qquad\overline{V_xK}=K .
\]

**Proof.** Since \(\theta\) maps null sets to null sets (Lemma 1.1(2) of the previous lesson), \(Vf\) does not depend on the representative of \(f\), and its coordinates are measurable because \(\theta^{-1}\) is. For a nonnegative measurable \(F\) on \(X\), \(\int F\circ\theta^{-1}d\mu=\int F\,d\mu\): for indicators this is \(\mu(\theta E)=\mu(E)\), and simple functions and monotone convergence give the general case. Hence
\[
\|Vf\|^2=\int\|V_{\theta^{-1}y}f(\theta^{-1}y)\|^2d\mu(y)=\int\|V_xf(x)\|^2d\mu(x)\le\|f\|^2 .
\]
For commutation, \((SVf)(\theta x)=S_{\theta x}V_xf(x)\) and \((VSf)(\theta x)=V_xS_xf(x)\). The operators \(S_{\theta x}V_x\) and \(V_xS_x\) agree on the basis by (2.1), so they are equal. This gives \(SVf=VSf\) at almost every point \(\theta x\), hence almost everywhere.

For \(x\in X_*\) all \(b_j(x)\) are positive. Then \(V_xK_{\ge h}\subseteq K_{\ge h-1}\), and \(V_xK_{\ge h}\) contains \(e_{j-1}=V_x(b_j(x)^{-1}e_j)\) for every \(j\ge h\), so its closure is \(K_{\ge h-1}\). Likewise \(V_xK\) contains every \(e_j\). \(\square\)

\(V_x\) need not have a bounded inverse, and \(V\) need not be invertible; dense images are all that closed invariant subspaces require.

## 3. Strict descent on a probability space

**Lemma 3.1** (strict descent). Let \((Y,\nu)\) be a probability space and \(\theta:Y\to Y\) a bijection such that \(\theta\) and \(\theta^{-1}\) are measurable and preserve \(\nu\), and which is ergodic: \(\nu(E\,\triangle\,\theta^{-1}E)=0\) implies \(\nu(E)\in\{0,1\}\). Let \(s:Y\to\mathbb Z\cup\{\pm\infty\}\) be measurable, and suppose that for almost every \(y\),
\[
s(y)=-\infty\ \Longrightarrow\ s(\theta y)=-\infty,\qquad s(y)\in\mathbb Z\ \Longrightarrow\ s(\theta y)\le s(y)-1 .
\]
Then \(s=-\infty\) almost everywhere or \(s=+\infty\) almost everywhere.

**Proof.** Let \(E=\{s=-\infty\}\). The first implication says that \(E\setminus\theta^{-1}E\) is null. As \(\nu(\theta^{-1}E)=\nu(E)\), the set \(\theta^{-1}E\setminus E\) is null too, so \(\nu(E\,\triangle\,\theta^{-1}E)=0\) and \(\nu(E)\in\{0,1\}\). If \(\nu(E)=1\) we are done.

Suppose \(\nu(E)=0\), and put \(F_j=\{s\le j\}\) for \(j\in\mathbb Z\). Both implications say that \(F_j\setminus\theta^{-1}F_{j-1}\) is null. Hence
\[
\nu(F_j)\le\nu(\theta^{-1}F_{j-1})=\nu(F_{j-1})\le\nu(F_j),
\]
so \(\nu(F_{j-r})=\nu(F_j)\) for all \(r\ge0\). Since \(F_j\supseteq F_{j-1}\supseteq\cdots\) and \(\bigcap_rF_{j-r}=E\), continuity from above gives \(\nu(F_j)=\nu(E)=0\). Then \(\{s<+\infty\}=\bigcup_jF_j\) is null. \(\square\)

A finite label that drops by at least one at every step would have to lose all of its mass; a measure-preserving map cannot push mass down forever. The lemma uses ergodicity only to exclude a mixture of the two constant values.

## 4. Common invariant subspaces

**Proposition 4.1.** Let \(L\subseteq H_0\) be a closed subspace invariant under \(S\), under \(V\), and under every scalar multiplier \(M_g\), \(g\in L^\infty(X,\mu)\). Then \(L=\{0\}\) or \(L=H_0\).

**Proof.** *A field of projections.* The set of scalar multipliers is closed under adjoints, since \(M_g^*=M_{\bar g}\). By Proposition 2.1(5) of the double commutant lesson, the projection \(P\) onto \(L\) commutes with every \(M_g\). Theorem 2.2 of the previous lesson gives a measurable field \(x\mapsto P_x\), whose values are orthogonal projections outside a null set, with \((Pf)(x)=P_xf(x)\) almost everywhere for every \(f\in H_0\). In particular
\[
L=\{f\in H_0:Pf=f\}=\{f\in H_0:f(x)\in\operatorname{ran}P_x\text{ for almost every }x\}.\tag{4.1}
\]

*Fibre identities.* Invariance means \((1-P)SP=0\) and \((1-P)VP=0\). Fix \(j\), and let \(g=P(1\otimes e_j)\); then \(g(x)=P_xe_j\) outside a null set \(N_j\). First, \(((1-P)Sg)(x)=(1-P_x)S_xP_xe_j\) almost everywhere, so
\[
(1-P_x)S_xP_xe_j=0\quad\text{for almost every }x.
\]
Second, \((Vg)(y)=V_{\theta^{-1}y}P_{\theta^{-1}y}e_j\) for \(y\notin\theta N_j\), a null set. Since \(((1-P)Vg)(y)=(1-P_y)(Vg)(y)\) almost everywhere, \((1-P_y)V_{\theta^{-1}y}P_{\theta^{-1}y}e_j=0\) for almost every \(y\). Writing \(y=\theta x\) and using that \(\theta^{-1}\) preserves null sets,
\[
(1-P_{\theta x})V_xP_xe_j=0\quad\text{for almost every }x.
\]
These are countably many conditions. Let \(X_0\) be a conull set of points of \(X_*\) at which \(P_x\) and \(P_{\theta x}\) are projections and both identities hold for every \(j\); by boundedness they then hold on all of \(K\). The set \(X_1=\bigcap_{n\in\mathbb Z}\theta^nX_0\) is conull and \(\theta X_1=X_1\). For \(x\in X_1\),
\[
S_x(\operatorname{ran}P_x)\subseteq\operatorname{ran}P_x,\qquad V_x(\operatorname{ran}P_x)\subseteq\operatorname{ran}P_{\theta x}.\tag{4.2}
\]

*Tail labels.* For \(x\in X_1\), \(\operatorname{ran}P_x\) is a closed \(S_x\)-invariant subspace. By Proposition 3.1(4) of the previous lesson, \(\operatorname{ran}P_x=K_{\ge s(x)}\) for exactly one \(s(x)\in\mathbb Z\cup\{\pm\infty\}\). Put \(s=+\infty\) off \(X_1\). For \(j\in\mathbb Z\), a tail \(K_{\ge s}\) contains \(e_j\) exactly when \(s\le j\), and a projection \(Q\) fixes a unit vector \(e\) exactly when \(\langle Qe,e\rangle=1\). So
\[
\{s\le j\}=\{x\in X_1:\langle P_xe_j,e_j\rangle=1\},
\]
which is measurable; hence \(s\) is measurable.

*Descent.* Let \(x\in X_1\), so that \(\theta x\in X_1\) and \(x\in X_*\). If \(s(x)=-\infty\), then by (4.2) the closed subspace \(K_{\ge s(\theta x)}\) contains \(V_xK\), which is dense by Proposition 2.2; so \(s(\theta x)=-\infty\). If \(s(x)=h\in\mathbb Z\), then \(K_{\ge s(\theta x)}\) contains \(V_xK_{\ge h}\), hence its closure \(K_{\ge h-1}\); so \(s(\theta x)\le h-1\). By Lemma 1.1 of the previous lesson, \(\theta\) is a measure-preserving ergodic bijection, measurable in both directions, so Lemma 3.1 applies: \(s=-\infty\) almost everywhere, or \(s=+\infty\) almost everywhere. That is, \(P_x=1\) almost everywhere or \(P_x=0\) almost everywhere, and by (4.1) \(L=H_0\) or \(L=\{0\}\). \(\square\)

## 5. The theorem

**Theorem 5.1** (OpenAI). Let \(X\), \(\mu\), \(\theta\), the weights \(\beta_j\), and the operators \(S\) and \(V\) on \(H_0=L^2(X\times\mathbb Z,\mu\otimes\#)\) be as in the previous lesson and Section 2.

1. For every \(x\in X\), the closed invariant subspaces of \(S_x\) are exactly the tails \(K_{\ge h}\), \(h\in\mathbb Z\cup\{\pm\infty\}\).
2. \(S\neq0\), \(\|S\|=e^{-10}\), and \(\|S^n\|\le\exp(-10\lfloor(n+1)^2/4\rfloor)\) for every \(n\ge1\).
3. \(V\) is a contraction commuting with \(S\), given by \((Vf)(\theta x)=V_xf(x)\) and \(V_xe_j=b_j(x)e_{j-1}\), where the \(b_j:X\to[0,1]\) are measurable and positive on the conull \(\theta\)-invariant set \(X_*\). For \(x\in X_*\), \(\overline{V_xK_{\ge h}}=K_{\ge h-1}\) (\(h\in\mathbb Z\)) and \(\overline{V_xK}=K\).
4. The unital algebra generated by \(S\), \(V\) and all scalar multipliers is transitive.

**Proof.** (1) is Proposition 3.1(4), and (2) is Proposition 4.1, of the previous lesson. (3) is Proposition 2.2. For (4), a closed subspace invariant under the algebra is invariant under its generators, so Proposition 4.1 applies. \(\square\)

**Corollary 5.2** (OpenAI). Every infinite-dimensional separable complex Hilbert space \(H\) carries a nonzero operator \(T\) with \(\lim_n\|T^n\|^{1/n}=0\) that has no hyperinvariant subspace other than \(\{0\}\) and \(H\). Its commutant \(\{T\}'\) is a unital transitive algebra, closed in the weak and in the strong operator topology, and different from \(B(H)\).

**Proof.** The operators \(S\), \(V\) (Proposition 2.2) and the scalar multipliers (Lemma 2.1 of the previous lesson) commute with \(S\), so the transitive algebra of Theorem 5.1(4) lies in \(\{S\}'\), and \(\{S\}'\) is transitive. By Proposition 4.1 of the previous lesson, \(S\) is not a scalar multiple of the identity, so Lemma 1.1 of the first lesson shows that \(\{S\}'\) is a weakly and strongly closed unital algebra different from \(B(H_0)\), and that \(S\) has no nontrivial hyperinvariant subspace.

\(H_0\) is separable and infinite-dimensional. By Lemma 1.1(5) of the previous lesson and Theorem 4.1(4) of the Hilbert space lesson, \(L^2(X,\mu)\) has a countable orthonormal basis \((\varphi_k)\). The fields \(\varphi_k\otimes e_j\colon x\mapsto\varphi_k(x)e_j\) are orthonormal in \(H_0\), and a field orthogonal to all of them has every coordinate orthogonal to every \(\varphi_k\), hence zero. So they form a countably infinite orthonormal basis of \(H_0\). The space \(H\) also has a countably infinite orthonormal basis (Theorem 4.1(4) and (5) there), and by Theorem 4.1(2) and (3) the linear map sending the one basis to the other extends to a unitary \(U:H_0\to H\). Put \(T=USU^*\). Then \(T^n=US^nU^*\), so \(\|T^n\|=\|S^n\|\); \(\{T\}'=U\{S\}'U^*\); and \(L\mapsto UL\) maps the hyperinvariant subspaces of \(S\) onto those of \(T\). \(\square\)

So the hyperinvariant subspace problem has a negative answer, and so does the transitive algebra problem: \(\{T\}'\) is a proper weakly closed unital transitive algebra.

## 6. Structure of the example

**Many invariant subspaces.** The theorem concerns hyperinvariant subspaces only. The closed subspaces invariant under \(S\) and the scalar multipliers can be listed completely.

**Proposition 6.1.** For a measurable \(\sigma:X\to\mathbb Z\cup\{\pm\infty\}\), let \(L_\sigma=\{f\in H_0:f(x)\in K_{\ge\sigma(x)}\text{ for almost every }x\}\). The closed subspaces of \(H_0\) invariant under \(S\) and all scalar multipliers are exactly the subspaces \(L_\sigma\). Such an \(L_\sigma\) is invariant under \(V\) only if \(L_\sigma=\{0\}\) or \(L_\sigma=H_0\).

**Proof.** Let \(P^\sigma_x\) be the projection onto \(K_{\ge\sigma(x)}\). Its matrix entries \(\langle P^\sigma_xe_i,e_j\rangle=\delta_{ij}1_{\{\sigma\le i\}}(x)\) are measurable, so it is a measurable field of projections. Its decomposable operator \(P^\sigma\) is a projection with range \(L_\sigma\) (Lemma 2.1 of the previous lesson), so \(L_\sigma\) is closed. \(P^\sigma\) commutes with every \(M_g\). Since \(S_xK_{\ge\sigma(x)}\subseteq K_{\ge\sigma(x)}\), the field of \((1-P^\sigma)SP^\sigma\) vanishes, so \(L_\sigma\) is \(S\)-invariant. Conversely, let \(L\) be a closed subspace invariant under \(S\) and the multipliers. The parts of the proof of Proposition 4.1 that concern \(S\) and the multipliers (the field of projections, the identity \((1-P_x)S_xP_x=0\), and the tail labels) do not use \(V\). They give a measurable label \(s\) with \(\operatorname{ran}P_x=K_{\ge s(x)}\) almost everywhere, and (4.1) says \(L=L_s\). The last statement is Proposition 4.1. \(\square\)

For instance, for \(h\in\mathbb Z\) the subspace \(L_h\) of fields with values in \(K_{\ge h}\) is invariant under \(S\) and nontrivial, and \(V(1\otimes e_h)\) has the coordinate \(b_h(\theta^{-1}y)>0\) at \((y,h-1)\) for almost every \(y\), so \(L_h\) is not \(V\)-invariant. The construction does not bear on the invariant subspace problem.

**The polar decomposition.** Let \(U\) be the unitary \((Uf)(x,j)=f(x,j-1)\) of \(H_0\), and \(|S|\) the multiplication operator \((|S|f)(x,j)=\beta_j(x)f(x,j)\). Then \(S=U|S|\), with \(|S|\ge0\) injective, and \(S^*S=|S|^2\). The operators
\[
A_n=U^{-n}|S|U^n,\qquad(A_nf)(x,j)=\beta_{j+n}(x)f(x,j)\qquad(n\in\mathbb Z),
\]
are commuting positive multiplication operators. For a set \(\mathcal F\) of self-adjoint operators, \(W^*(\mathcal F)=\mathcal F''\) is the von Neumann algebra it generates (Definition 2.3 of the double commutant lesson). A nonzero projection \(p\) in an abelian von Neumann algebra is *minimal* if the only projections \(q\le p\) in the algebra are \(0\) and \(p\).

**Proposition 6.2.**

1. For every finite \(F\subset\mathbb Z\), there is a countable family of mutually orthogonal nonzero projections \(p_v\) with \(\sum_vp_v=1\) (strong convergence) such that \(W^*(A_n:n\in F)\) consists of the operators \(\sum_vc_vp_v\) with bounded coefficients \(c_v\). Each \(p_v\) is a minimal projection of this algebra.
2. \(W^*(A_n:n\in\mathbb Z)\) is the algebra of all multiplication operators \(m_g\), \(g\in L^\infty(X\times\mathbb Z,\mu\otimes\#)\). It has no minimal projection.

**Proof.** *A diagonal calculus.* Let \(A=\sum_v\lambda_vp_v\) be a strongly convergent sum, where the \(p_v\) are countably many mutually orthogonal nonzero projections with \(\sum_vp_v=1\) and the \(\lambda_v\) are bounded real numbers. Each \(\lambda_v\) is an eigenvalue, so it lies in the spectrum \(\sigma(A)\). We claim \(f(A)=\sum_vf(\lambda_v)p_v\) for every bounded Borel function \(f\) on \(\sigma(A)\). The set \(\mathcal M\) of such \(f\) contains the polynomials, by orthogonality. Both sides have norm at most \(\sup_{\sigma(A)}|f|\) (Theorem 3.1(3) of the spectral theorem lesson), so \(\mathcal M\) contains every uniform limit of polynomials, hence every continuous function by the Weierstrass theorem. If \(f_k\to f\) boundedly, then \(f_k(A)\xi\to f(A)\xi\) (Theorem 3.1(4) there) and \(\sum_vf_k(\lambda_v)p_v\xi\to\sum_vf(\lambda_v)p_v\xi\) by dominated convergence. By Lemma 1.1 of the spectral theorem lesson, \(\mathcal M\) contains all bounded Borel functions. By Theorem 3.1(5) there, each \(f(A)\) lies in \(\{A\}''\).

*The algebra of a partition.* For \(p_v\) as above, let \(\mathcal D\) be the set of strongly convergent sums \(\sum_vc_vp_v\) with bounded \(c_v\). An operator commutes with all \(p_v\) if and only if it is block diagonal, \(R=\sum_vp_vRp_v\). Every element of \(\mathcal D\) commutes with every block diagonal operator. Conversely, an operator commuting with all block diagonal operators commutes with the projections \(p_v\) and with all operators on each block \(p_vH_0\), so it is a scalar \(c_v\) on each block. Hence \(\mathcal D=\{p_v:v\}''\), a von Neumann algebra.

(1) For fixed \(j\) and \(n\in F\), \(\beta_{j+n}(x)\) is constant if \(j+n\in\{-1,0\}\), and otherwise it is a function of one residue \(T_m(x)\). By (1.1) of the previous lesson, finitely many residues are functions of the one with the largest level. So for fixed \(j\) the tuple \(t(x,j)=(\beta_{j+n}(x))_{n\in F}\) takes finitely many values, each on a finite union of residue classes, a set of positive measure. Over all \(j\) the tuple takes countably many values \(v\). Let \(p_v\) be multiplication by the indicator of \(\{t=v\}\): these are mutually orthogonal nonzero projections with \(\sum_vp_v=1\), and \(A_n=\sum_vv_np_v\). With \(f=1_{\{\lambda\}}\), the diagonal calculus gives \(1_{\{\lambda\}}(A_n)=\sum_{v:v_n=\lambda}p_v\in W^*(A_n:n\in F)\), and
\[
p_v=\prod_{n\in F}1_{\{v_n\}}(A_n)\in W^*(A_n:n\in F).
\]
So \(\mathcal D=\{p_v\}''\subseteq W^*(A_n:n\in F)\). Conversely \(\mathcal D\) is a von Neumann algebra containing every \(A_n\), so it contains \(W^*(A_n:n\in F)\) (Proposition 2.1(4) of the double commutant lesson). A projection in \(\mathcal D\) is \(\sum_vc_vp_v\) with \(c_v\in\{0,1\}\), so the only projections below \(p_v\) are \(0\) and \(p_v\).

(2) Let \(W=W^*(A_n:n\in\mathbb Z)\) and let \(\mathcal L\) be the algebra of multiplication operators on \(L^2(X\times\mathbb Z,\mu\otimes\#)\). By Theorem 9.1 of the Hilbert space lesson, \(\mathcal L=\mathcal L'\), so \(\mathcal L''=\mathcal L\) is a von Neumann algebra containing all \(A_n\), and \(W\subseteq\mathcal L\).

*Rectangles.* Each \(A_n\) is multiplication by \(h_n(x,j)=\beta_{j+n}(x)\), which takes countably many values; the diagonal calculus gives \(f(A_n)=m_{f\circ h_n}\). By Proposition 3.1(3) of the previous lesson, \(\beta_k(x)=e^{-c}\) exactly for \(k\in\{-1,0\}\). So \(h_{-r-1}(x,j)=e^{-c}\) exactly for \(j\in\{r,r+1\}\), and \(h_{-r}(x,j)=e^{-c}\) exactly for \(j\in\{r-1,r\}\). Hence
\[
P_r=1_{\{e^{-c}\}}(A_{-r-1})\,1_{\{e^{-c}\}}(A_{-r})
\]
is multiplication by the indicator of \(X\times\{r\}\). Next fix \(m\ge1\) and \(k_m=\ell_{m-1}\in I_m\). On \(X\times\{r\}\) the function \(h_{k_m-r}\) equals \(\beta_{k_m}(x)=\lambda_{m,T_m(x)}\), where \(\lambda_{m,t}=\exp(-c(k_m+1)-J_m-Dt)\) are distinct for distinct \(t\). So \(P_r1_{\{\lambda_{m,t}\}}(A_{k_m-r})\) is multiplication by the indicator of the *rectangle* \(\{T_m=t\}\times\{r\}\), and lies in \(W\).

*All of \(\mathcal L\).* Let \(R\in W'\). For \(\xi,\eta\in H_0\) the function \(\psi=\xi\,\overline{R^*\eta}-(R\xi)\,\bar\eta\) is integrable, and
\[
\langle Rm_{1_E}\xi,\eta\rangle-\langle m_{1_E}R\xi,\eta\rangle=\int_E\psi\,d(\mu\otimes\#)
\]
for every measurable \(E\). This vanishes for every rectangle, and so, by dominated convergence, also for \(X\times\mathbb Z\), a countable disjoint union of rectangles. The rectangles, together with \(\varnothing\) and \(X\times\mathbb Z\), form a family closed under finite intersections. Applying the uniqueness lemma for measures to the positive and negative parts of the real and imaginary parts of \(\psi\), \(\int_E\psi=0\) for every \(E\) in the sigma-algebra generated by the rectangles. That sigma-algebra contains \(A\times\{r\}\) for every \(A\in\Sigma\) and \(r\in\mathbb Z\), so it contains every measurable subset of \(X\times\mathbb Z\). Thus \(R\) commutes with every \(m_{1_E}\), hence with every multiplication by a simple function, hence, by norm density, with every \(m_g\). So \(W'\subseteq\mathcal L'=\mathcal L\), and \(W=W''\supseteq\mathcal L'=\mathcal L\).

*No minimal projection.* A nonzero projection in \(\mathcal L\) is multiplication by the indicator of a set \(E\) of positive measure, so some section \(E_r\) has \(\mu(E_r)>0\). Choose \(m\) with \(2^{-m}<\mu(E_r)\). The sets \(E_r\cap\{T_m=t\}\), \(0\le t<N_m\), partition \(E_r\) into pieces of measure at most \(2^{-m}\), so one piece \(G\) satisfies \(0<\mu(G)<\mu(E_r)\). Multiplication by the indicator of \(G\times\{r\}\) is a nonzero projection of \(\mathcal L\) strictly below the given one. \(\square\)

So finitely many polar conjugates \(A_n\) generate an atomic algebra, and \(|S|\) itself has a pure point spectral decomposition, while all of them together generate a diffuse algebra. The polar conjugates are not in \(\{S\}'\): \(|S|\) does not commute with \(S\), since \(|S|S(1\otimes e_0)=e^{-c}\beta_1(1\otimes e_1)\) with \(\beta_1\le e^{-2c}\), while \(S|S|(1\otimes e_0)=e^{-2c}(1\otimes e_1)\).

## 7. Exercises

**Exercise 7.1** (easy; the commutant is large). Show that \(\{S\}'\) contains the scalar multipliers, \(V\), and \(S\), and that the scalar multipliers form a self-adjoint abelian subalgebra of \(\{S\}'\) that is not maximal abelian in \(B(H_0)\).

*Solution.* The first statement is Lemma 2.1 of the previous lesson and Proposition 2.2. Exercise 5.2 of the previous lesson exhibits the projection \(Q_0\), which commutes with all scalar multipliers and is not one of them. \(\square\)

**Exercise 7.2** (medium; the constants). Where in the construction are \(c>2\log3\) and \(D>c\) used?

*Solution.* \(c>2\log3\) is the hypothesis \(\kappa>2\log3\) of Corollary 5.2 of the first lesson, applied with \(\kappa=c\) in Proposition 3.1(4) of the previous lesson; it puts each fibre into Domar's theorem. \(D>c\) is used in Lemma 2.1: the drift \(D\) per index must beat the linear growth \(c\) of the weights, so that the coefficients \(\tilde b_j\) decay at both ends and \(V\) is bounded after normalization. The concrete values \(c=10\) and \(D=100\) leave room in both inequalities. \(\square\)

**Exercise 7.3** (medium; descent needs an infinite orbit). Let \(\theta\) be the cyclic permutation \(y\mapsto y+1\) of \(Y=\mathbb Z/N\mathbb Z\) with the uniform probability. Show that no function \(s:Y\to\mathbb Z\) satisfies \(s(\theta y)\le s(y)-1\) for all \(y\), and explain how Lemma 3.1 contains this.

*Solution.* Summing \(s(\theta y)-s(y)\le-1\) over the orbit of length \(N\) gives \(0\le-N\), a contradiction. In Lemma 3.1, the sets \(F_j=\{s\le j\}\) would satisfy \(\nu(F_j)=\nu(F_{j-1})\) for all \(j\); since \(s\) takes finitely many integer values, \(F_j=Y\) for large \(j\) and \(F_j=\varnothing\) for small \(j\), which is impossible. \(\square\)

## Where this leads

The OpenAI companion paper [OAI-C] proves a related theorem by different means: for every irrational \(\theta\in(0,1)\) there is a continuous weight \(f:\mathbb T\to[0,1]\), vanishing only at \(1\), such that the operator \(Uf(V)\) in the irrational rotation algebra \(R_\theta\), the hyperfinite II\(_1\) factor, has no invariant projection in \(R_\theta\) other than \(0\) and \(1\). By [Lemma 1.2 of the first lesson](weighted-shifts-whose-invariant-subspaces-are-tails.md#1-commutants-and-hyperinvariant-subspaces), such an operator has no nontrivial hyperinvariant subspace either. That theorem, which answers a question of Zhu, Fang and Shi, is not proved in this course.

## References

- [OAI] OpenAI, *Backward intertwiners and a transitive commutant*, OpenAI Math Release preprint, 27 September 2026. https://github.com/openai/math/blob/main/preprints/Backward-intertwiners-and-a-transitive-commutant-September-27-2026/paper.pdf. Sections 4–6 there: Lemmas 1.2 and 2.1, Propositions 2.2 and 4.1, Lemma 3.1, Theorem 5.1 (Theorem 1.1 there), Corollary 5.2 (Corollary 1.2 there) and the structural results of Section 6.
- [OAI-C] OpenAI, *Invariant-projection counterexamples for every irrational rotation*, OpenAI Math Release preprint, 27 September 2026. https://github.com/openai/math/blob/main/preprints/Invariant-projection-counterexamples-for-every-irrational-rotation-September-27-2026/paper.pdf.
