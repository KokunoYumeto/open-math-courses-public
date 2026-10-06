<span id="recovering-the-commutant-from-right-bounded-vectors"></span>
# Recovering the commutant from right-bounded vectors



The elementary multiplication construction produces a right algebra inside the Hilbert completion, but it does not yet show that this algebra is dense. The missing approximation must control a vector and its adjoint-involution image at the same time. This unit constructs such approximations from the spectral cutoffs of a closed right multiplier. It then recovers the full commutant and proves the product-core and ideal-intersection statements needed for left/right dualization.

The mathematical antecedents are Takesaki, *Theory of Operator Algebras II*, Chapter VI, Lemmas 1.12–1.15. The arguments use closed operator domains, a cutoff ideal, and explicit contractive approximants. No modular commutant theorem is a premise.

<span id="oa-mod-rd-01--the-exact-starting-interface"></span>
<span id="OA-MOD-RD-01"></span>
<span id="oa-mod-rd-01"></span>
## OA-MOD-RD-01 — The exact starting interface

Use the arbitrary left Hilbert algebra \(\mathcal A\subseteq H\) of OA-MOD-HA. Inner products are linear in the first variable. The algebra need not have a unit, and \(H\) need not be separable. Write
\[
M=L(\mathcal A)'',\qquad
S=\overline{(a\mapsto a^\sharp)},\qquad F=S^*,
\]
\[
\mathcal B_r=\{\eta:a\mapsto L_a\eta\text{ is bounded for the Hilbert norm}\},
\quad
\mathfrak n_r=\{R_\eta:\eta\in\mathcal B_r\},
\quad
\mathcal A_r=\mathcal B_r\cap D(F).
\tag{RD.1}
\]
Here \(R_\eta a=L_a\eta\) for \(a\in\mathcal A\). OA-MOD-HA-05–08 prove that \(R\) is linear and injective, that \(\mathfrak n_r\) is a left ideal of \(M'\), and that
\[
R_{x\eta}=xR_\eta,\qquad
R_\eta^*\zeta\in\mathcal A_r,\qquad
F(R_\eta^*\zeta)=R_\zeta^*\eta
\tag{RD.2}
\]
for \(x\in M'\), \(\eta,\zeta\in\mathcal B_r\). For \(\eta\in\mathcal A_r\),
\[
F\eta\in\mathcal A_r,\qquad R_{F\eta}=R_\eta^*.
\tag{RD.3}
\]
The product \(\eta\zeta=R_\zeta\eta\) makes \(\mathcal A_r\) an involutive algebra with bounded right multiplication. Its density is the first target here.

An immediate operator form of (RD.2) will be useful:
\[
\mathfrak n_r^*\mathfrak n_r\subseteq R(\mathcal A_r).
\tag{RD.4}
\]
This means every product \(b^*c\), \(b,c\in\mathfrak n_r\), belongs to \(R(\mathcal A_r)\), and therefore so does its finite linear span. Indeed, write \(b=R_\eta,c=R_\zeta\); covariance gives
\(b^*c=R_{R_\eta^*\zeta}\), and (RD.2) gives the required vector.

For \(\eta\in D(F)\), OA-MOD-HA-07 supplies a closed densely defined operator
\[
T_\eta=\overline{\,a\mapsto L_a\eta\,},\qquad
\mathcal A\subseteq D(T_\eta),\quad T_\eta a=L_a\eta.
\tag{RD.5}
\]
It is affiliated with \(M'\), and
\[
\mathcal A\subseteq D(T_\eta^*),\qquad
T_\eta^*a=L_aF\eta.
\tag{RD.6}
\]
Only the restriction in (RD.6) is assumed; equality between \(T_\eta^*\) and the closure of the map for \(F\eta\) is not a premise.

The other dependencies are OA-MOD-TC-03 for ordinary and conjugate-linear graph adjoints, OA-MOD-QF-03–04 for closed nonnegative forms and unitary symmetry, and OA-MOD-BK-02–08 for bounded operators, topology, inverse order, support cutoffs, and unitary tests. The unbounded self-adjoint spectral calculus is the explicit **RD-DEP-SPECTRAL** contract: on arbitrary Hilbert spaces it includes spectral integral domains, positive square roots, unitary transport, and dominated convergence for each vector's finite spectral measure. Uniform polynomial approximation on a compact real interval is also used in OA-MOD-RD-06. These are also the analytic prerequisites of [Recovering operators from energy forms](../../../OA-MOD/OA-MOD-QF.html) and [Closing an involution and recovering its modular data](../../../OA-MOD/OA-MOD-TC.html).

<span id="oa-mod-rd-02--polar-cutoffs-for-a-closed-linear-operator"></span>
<span id="OA-MOD-RD-02"></span>
<span id="oa-mod-rd-02"></span>
## OA-MOD-RD-02 — Polar cutoffs for a closed linear operator

The right multiplier in (RD.5) need not be bounded or injective. We first establish the exact polar facts needed in that generality.

**Lemma.** Let \(T:D(T)\subseteq H\to H\) be closed and densely defined. There are nonnegative self-adjoint operators \(h,k\) and a bounded partial isometry \(u\) such that
\[
\begin{aligned}
h&=(T^*T)^{1/2},&D(h)&=D(T),\\
T&=uh=ku,&D(ku)&=D(h),\\
T^*&=hu^*,&
D(T^*)&=\{\zeta:u^*\zeta\in D(h)\}=D(k),\\
k&=(TT^*)^{1/2}.&&
\end{aligned}
\tag{RD.7}
\]
The initial and final projections are
\[
p=u^*u=P_{\overline{\operatorname{ran}T^*}},
\qquad
q=uu^*=P_{\overline{\operatorname{ran}T}}.
\tag{RD.8}
\]
If \(T\) is affiliated with a von Neumann algebra \(N\), then \(u,p,q\in N\), and all spectral projections of \(h,k\) belong to \(N\).

For every bounded Borel \(f:[0,\infty)\to\mathbb C\),
\[
f(k)=u f(h)u^*+f(0)(I-q),\qquad f(k)u=u f(h).
\tag{RD.9}
\]
In particular, for \(f\in C_c(0,\infty)\), extended by zero at zero,
\[
f(k)T\subseteq kf(k)u,\qquad
f(h)T^*\subseteq hf(h)u^*,
\tag{RD.10}
\]
where the operators on the right are bounded on \(H\). Their norms are at most
\(\sup_{t>0}|t f(t)|\).

**Proof.** The form
\[
q_T(\xi,\zeta)=\langle T\xi,T\zeta\rangle,\qquad D(q_T)=D(T),
\]
is closed because its form norm is the graph norm of \(T\). Its representing operator in OA-MOD-QF-03 is \(T^*T\): for \(\xi\in D(T)\), existence of \(y\) with
\(\langle T\xi,T\zeta\rangle=\langle y,\zeta\rangle\) for all \(\zeta\in D(T)\)
is precisely \(T\xi\in D(T^*)\), \(T^*T\xi=y\). Consequently
\[
D(h)=D(T),\qquad
\langle h\xi,h\zeta\rangle=\langle T\xi,T\zeta\rangle.
\tag{RD.11}
\]
Thus \(\ker h=\ker T\). The rule \(h\xi\mapsto T\xi\) is well-defined and isometric. Extend it to a unitary \(U:pH\to qH\), where initially \(p\) projects onto \(\overline{\operatorname{ran}h}\) and \(q\) onto \(\overline{\operatorname{ran}T}\); set \(u=U\) on \(pH\) and zero on \((I-p)H=\ker h\). This gives \(T=uh\).

For \(\zeta\in H\), the pairing
\[
\langle T\xi,\zeta\rangle=\langle h\xi,u^*\zeta\rangle
\quad(\xi\in D(h))
\]
is bounded in \(\|\xi\|\) exactly when \(u^*\zeta\in D(h^*)=D(h)\). This proves the asserted domain and action of \(T^*\). Its range equals \(\operatorname{ran}h\): for any \(h\xi\), replacing \(\xi\) by \(p\xi\) changes neither membership in \(D(h)\) nor its image, and \(T^*(u p\xi)=h p\xi=h\xi\). Thus the projection \(p\) also has the description in (RD.8).

The spectral projection \(p\) reduces \(h\), so its restriction \(h_p\) is self-adjoint on \(pH\). Define
\[
k=(Uh_pU^*)\oplus0
\quad\text{on }qH\oplus(I-q)H.
\]
This is nonnegative self-adjoint with
\[
D(k)=\{\zeta:u^*\zeta\in D(h)\},\qquad k\zeta=uh u^*\zeta.
\]
Its square has domain \(\{\zeta:u^*\zeta\in D(h^2)\}\). The product \(TT^*\) has exactly the same domain and action \(uh^2u^*\), by the already-proved formulas for \(T,T^*\). Thus \(k^2=TT^*\), including domains. Also
\[
u\xi\in D(k)\ \Longleftrightarrow\ p\xi\in D(h)
\ \Longleftrightarrow\ \xi\in D(h),
\]
because \(\ker h\subseteq D(h)\). On that domain \(ku\xi=uh\xi=T\xi\). This proves all of (RD.7).

Spectral calculus on the displayed orthogonal decomposition of \(k\) proves (RD.9). Multiplication by \(tf(t)\), for the compactly supported \(f\) in (RD.10), is a bounded spectral function. On \(D(T)\), the first identity in (RD.10) follows from \(T=ku\); on \(D(T^*)\), the second follows from \(T^*=hu^*\). They are inclusions because the bounded extensions on the right have domain all of \(H\).

Finally suppose \(T\) is affiliated with \(N\). For each unitary \(v\in N'\), the form \(q_T\) has invariant domain and satisfies \(q_T[v\xi]=q_T[\xi]\). Uniqueness and unitary symmetry of closed-form representation imply that \(v\) commutes with \(h\) and its spectral projections. On \(\operatorname{ran}h\),
\[
uvh\xi=uhv\xi=Tv\xi=vT\xi=vuh\xi.
\]
On \(\ker h\) the two sides also agree, since that kernel is invariant under \(v\). Hence \(u\) commutes with every unitary of \(N'\), so \(u\in N\) by the unitary test and bicommutant theorem. This gives \(p,q\in N\), and spectral transport in (RD.9) gives the spectral projections of \(k\) in \(N\). No range or kernel has been assumed trivial. \(\square\)

<span id="oa-mod-rd-03--bounded-cutoffs-land-in-the-operator-ideal"></span>
<span id="OA-MOD-RD-03"></span>
<span id="oa-mod-rd-03"></span>
## OA-MOD-RD-03 — Bounded cutoffs land in the operator ideal

Fix \(\eta\in D(F)\). Apply OA-MOD-RD-02 to \(T=T_\eta\), and retain \(h,k,u,p,q\). All their bounded spectral functions and \(u\) lie in \(M'\).

**Cutoff theorem.** For \(f\in C_c(0,\infty)\), extended by zero at zero,
\[
\begin{aligned}
f(k)\eta&\in\mathcal B_r,
&R_{f(k)\eta}&=kf(k)u,\\
f(h)F\eta&\in\mathcal B_r,
&R_{f(h)F\eta}&=hf(h)u^*.
\end{aligned}
\tag{RD.12}
\]
Moreover,
\[
f(h),f(k)\in R(\mathcal A_r),
\tag{RD.13}
\]
and both cutoff vectors in (RD.12) belong to \(\mathcal A_r^2\). Their adjoint-involution relation is
\[
F(f(k)\eta)=\overline f(h)F\eta.
\tag{RD.14}
\]
Here \(\overline f(t)=\overline{f(t)}\), and \(\mathcal A_r^2\) denotes the linear span of products.

**Proof of the bounded formulas.** For \(a\in\mathcal A\), the cutoff operators commute with \(L_a\). Equations (RD.5–6) and (RD.10) give
\[
\begin{aligned}
L_a f(k)\eta&=f(k)T a=kf(k)u a,\\
L_a f(h)F\eta&=f(h)T^*a=hf(h)u^*a.
\end{aligned}
\]
The final operators are bounded on \(H\), proving (RD.12) directly from the definition of right boundedness.

**Proof of the ideal assertion.** By covariance (RD.2),
\[
u^*R_{f(k)\eta}=h f(h)\in\mathfrak n_r,
\qquad
uR_{f(h)F\eta}=k f(k)\in\mathfrak n_r.
\tag{RD.15}
\]
The polar transport identities justify these equalities also on the kernel subspaces, since \(f(0)=0\). Now \(g(t)=f(t)/t\) is again in \(C_c(0,\infty)\). Apply (RD.15) to \(g\) to conclude \(f(h),f(k)\in\mathfrak n_r\).

Choose a real \(\chi\in C_c(0,\infty)\) that equals one on \(\operatorname{supp}f\). Such a function can be chosen piecewise linear on an interval with positive endpoints containing that compact support. Both \(\chi(h)\) and \(f(h)\) lie in \(\mathfrak n_r\), and
\[
f(h)=\chi(h)^*f(h)\in\mathfrak n_r^*\mathfrak n_r
\subseteq R(\mathcal A_r).
\]
The same argument applies to \(k\), proving (RD.13).

**Proof of the vector and domain assertions.** Set \(v=f(k)\eta\), already known to lie in \(\mathcal B_r\). As \(\chi(k)\) is self-adjoint and belongs to \(R(\mathcal A_r)\), it can be written \(R_\alpha^*\) for some \(\alpha\in\mathcal A_r\), by (RD.3). Since \(\chi(k)v=v\), equation (RD.2) gives \(v\in\mathcal A_r\). Write also \(\chi(k)=R_\beta\), \(\beta\in\mathcal A_r\). Then
\[
v=\chi(k)v=R_\beta v=v\beta\in\mathcal A_r^2.
\]
The same reasoning using \(h\) proves \(f(h)F\eta\in\mathcal A_r^2\).

We may now apply (RD.3) to \(v\). Taking adjoints in its bounded formula in (RD.12) gives
\[
R_{Fv}=R_v^*=h\overline f(h)u^*
=R_{\overline f(h)F\eta}.
\]
Both vectors are right bounded, so injectivity of \(R\) proves (RD.14). The argument established membership in \(D(F)\) before computing this value. \(\square\)

<span id="oa-mod-rd-04--graph-density-of-the-right-algebra"></span>
<span id="OA-MOD-RD-04"></span>
<span id="oa-mod-rd-04"></span>
## OA-MOD-RD-04 — Graph density of the right algebra

The graph norm of \(F\) is
\[
\|\eta\|_F^2=\|\eta\|^2+\|F\eta\|^2.
\tag{RD.16}
\]

**Theorem.** Both \(\mathcal A_r\) and \(\mathcal A_r^2\) are graph cores for \(F\). In particular, both are dense in \(H\), \(\mathcal A_r\) is a right Hilbert algebra, and
\[
\overline{F|_{\mathcal A_r}}=F,\qquad
(F|_{\mathcal A_r})^*=F^*=S.
\tag{RD.17}
\]

**Proof.** Fix \(\eta\in D(F)\) and its polar data from OA-MOD-RD-03. First we need the support identities
\[
q\eta=\eta,\qquad pF\eta=F\eta.
\tag{RD.18}
\]
For \(a\in\mathcal A\), the vector \(L_a\eta=T a\) lies in \(qH\). Since \(q\in M'\),
\[
L_a(I-q)\eta=(I-q)L_a\eta=0.
\]
The common-kernel criterion OA-MOD-HA-02 gives \((I-q)\eta=0\). Similarly \(L_aF\eta=T^*a\in pH\), and the same criterion proves \(pF\eta=F\eta\). Thus the support projections need not be the identity, but they fix the two particular vectors we approximate.

For \(n\geq1\), define on \((0,\infty)\)
\[
f_n(t)=\max\!\left(0,\min\!\left(1,\,2-\frac{|\log t|}{n}\right)\right).
\tag{RD.19}
\]
Each function is continuous, supported in \([e^{-2n},e^{2n}]\), takes values in \([0,1]\), and increases pointwise to one on \((0,\infty)\). Extend it by zero at zero. The spectral calculus and scalar dominated convergence give
\[
f_n(k)\longrightarrow q,\qquad
f_n(h)\longrightarrow p
\quad\text{strongly}.
\tag{RD.20}
\]
OA-MOD-RD-03 supplies \(\eta_n=f_n(k)\eta\in\mathcal A_r^2\) and
\(F\eta_n=f_n(h)F\eta\). Equations (RD.18–20) therefore imply
\[
\|\eta_n-\eta\|^2+\|F\eta_n-F\eta\|^2\longrightarrow0.
\tag{RD.21}
\]
This proves that \(\mathcal A_r^2\) is a graph core. Since
\(\mathcal A_r^2\subseteq\mathcal A_r\subseteq D(F)\), the same is true of \(\mathcal A_r\). The domain \(D(F)\) is dense in \(H\), so both subspaces are Hilbert-norm dense too.

OA-MOD-HA-08 established the first three right Hilbert algebra properties; density of \(\mathcal A_r^2\) supplies the fourth. Graph density proves the first equality in (RD.17), and taking adjoints gives the second by \(F=S^*\), \(S^{**}=S\). \(\square\)

The approximating sequence depends on \(\eta\), through its multiplier \(T_\eta\). It is not a countable dense family for \(H\), nor an assertion that a global net of algebra operators has a sequential replacement.

<span id="oa-mod-rd-05--contractive-approximation-of-the-entire-commutant"></span>
<span id="OA-MOD-RD-05"></span>
<span id="oa-mod-rd-05"></span>
## OA-MOD-RD-05 — Contractive approximation of the entire commutant

Put \(\mathcal D=R(\mathcal A_r)\subseteq M'\). It is a *-algebra, by the anti-representation and adjoint formulas in OA-MOD-HA-08. It is nondegenerate because its action on \(\mathcal A_r\) contains the dense product span \(\mathcal A_r^2\).

**Theorem.** There is a net of positive contractions \(e_i\in\mathcal D\) with \(e_i\to I\) strongly. For every \(x\in M'\),
\[
e_i x e_i\in\mathcal D,\qquad
\|e_i x e_i\|\leq\|x\|,\qquad
e_i x e_i\longrightarrow x
\quad\text{strongly*}.
\tag{RD.22}
\]
Consequently
\[
R(\mathcal A_r)''=M'.
\tag{RD.23}
\]
Strong* convergence means strong convergence of both the operators and their adjoints.

**Proof.** Index a net by pairs \((E,\varepsilon)\), where \(E\) is a finite subset of \(\mathcal D\) and \(\varepsilon>0\); enlarge \(E\) and decrease \(\varepsilon\). Put
\[
b_E=\sum_{r\in E}r^*r,\qquad
c_{E,\varepsilon}=b_E(b_E+\varepsilon I)^{-1}.
\tag{RD.24}
\]
These are positive contractions \(c_{E,\varepsilon}\in M'\). By inverse order, they increase when \(E\) enlarges and \(\varepsilon\) decreases. For fixed \(E\), letting \(\varepsilon\downarrow0\) gives the support projection \(s(b_E)\), by OA-MOD-BK-06.

The family of these supports spans \(H\). Indeed,
\[
\bigcap_E\ker b_E=\bigcap_{r\in\mathcal D}\ker r=\{0\}.
\tag{RD.25}
\]
The first equality follows by expanding
\(\langle b_E\xi,\xi\rangle=\sum_{r\in E}\|r\xi\|^2\).
For the second, a common-kernel vector is orthogonal to every \(r^*\zeta\); *-closure and nondegeneracy of \(\mathcal D\) make these vectors span a dense subspace.

The increasing contraction net \(c_{E,\varepsilon}\) has a strong limit \(c\) by OA-MOD-BK-04. This limit satisfies \(s(b_E)\leq c\leq I\) for every \(E\). A positive contraction dominating a projection acts as the identity on its range, by OA-MOD-BK-06. Equations (RD.25) thus imply \(c=I\).

We next make approximants that lie in \(\mathcal D\) itself. Since \(b_E\in\mathcal D\subseteq\mathfrak n_r\), the left-ideal property gives \(c_{E,\varepsilon}\in\mathfrak n_r\). Define
\[
e_{E,\varepsilon}=c_{E,\varepsilon}^*c_{E,\varepsilon}
=c_{E,\varepsilon}^{\,2}.
\tag{RD.26}
\]
Equation (RD.4) puts \(e_{E,\varepsilon}\) in \(\mathcal D\). It is a positive contraction, and
\[
\|(e_{E,\varepsilon}-I)\xi\|
\leq 2\|(c_{E,\varepsilon}-I)\xi\|\longrightarrow0.
\]
These self-adjoint operators converge strongly*. Their squares are not asserted to form an increasing net.

Finally \(e_i\in\mathfrak n_r\) and \(xe_i\in\mathfrak n_r\), so
\[
e_i x e_i=e_i^*(xe_i)\in\mathfrak n_r^*\mathfrak n_r
\subseteq\mathcal D.
\]
Their norms are at most \(\|x\|\), and
\[
\|(e_i x e_i-x)\xi\|
\leq\|x\|\|(e_i-I)\xi\|+\|(e_i-I)x\xi\|\longrightarrow0.
\]
Replace \(x\) by \(x^*\) to obtain the adjoint convergence. Since \(\mathcal D\subseteq M'\), (RD.22) proves that its strong closure is \(M'\), and hence its bicommutant is \(M'\), using the nondegenerate density lemma OA-MOD-HA-03. \(\square\)

This explicit net proves the bounded approximation needed here without assuming a density theorem for unit balls. On a bounded set, its strong convergence is also ultraweak convergence by OA-MOD-BK-03.

<span id="oa-mod-rd-06--products-form-a-core-for-the-original-involution"></span>
<span id="OA-MOD-RD-06"></span>
<span id="oa-mod-rd-06"></span>
## OA-MOD-RD-06 — Products form a core for the original involution

**Theorem.** The product span \(\mathcal A^2\) is dense in \(D(S)\) for the graph norm of \(S\). Equivalently, for \(v,w\in H\),
\[
\left[
\langle a^\sharp b,v\rangle=\langle w,b^\sharp a\rangle
\quad\text{for every }a,b\in\mathcal A
\right]
\quad\Longleftrightarrow\quad
v\in D(F),\ Fv=w.
\tag{RD.27}
\]

**Proof of graph density.** It suffices to approximate each \(a\in\mathcal A\), because \(\mathcal A\) is already a graph core for \(S\). Write \(A=L_a\). The net in OA-MOD-RD-05 has \(e_i=R_{\beta_i}\), \(\beta_i\in\mathcal A_r\). Therefore
\[
e_i a=L_a\beta_i=A\beta_i\longrightarrow a.
\]
This proves \(a\in\overline{\operatorname{ran}A}\). Applying the same argument to \(a^\sharp\) gives \(a^\sharp\in\overline{\operatorname{ran}A^*}\).

For \(\delta>0\), let \(g_\delta(t)=t/(t+\delta)\) on \([0,\infty)\). The support-cutoff theorem gives
\[
g_\delta(AA^*)a\longrightarrow a,\qquad
g_\delta(A^*A)a^\sharp\longrightarrow a^\sharp
\quad(\delta\downarrow0).
\tag{RD.28}
\]
These cutoffs need not themselves be left multipliers of vectors in \(\mathcal A\), so we approximate their scalar functions by polynomials.

Take \(\delta_n=1/n\). If \(A=0\), faithfulness gives \(a=0\), and there is nothing to prove. Otherwise choose real polynomials \(p_n\) with \(p_n(0)=0\) such that
\[
\sup_{0\leq t\leq\|A\|^2}
|p_n(t)-g_{\delta_n}(t)|\leq n^{-1}.
\tag{RD.29}
\]
Uniform polynomial approximation supplies these: approximate the real function with error \(1/(2n)\), then subtract the value of the approximating polynomial at zero. Since \(g_{\delta_n}(0)=0\), the final error is at most \(1/n\).

Define the algebra vector
\[
a_n=p_n(aa^\sharp)a.
\tag{RD.30}
\]
Because the polynomial has zero constant term, this is a finite linear combination of products of at least three algebra vectors and hence belongs to \(\mathcal A^2\). Algebraic associativity and the real coefficients give
\[
a_n=p_n(AA^*)a,\qquad
a_n^\sharp=p_n(A^*A)a^\sharp.
\tag{RD.31}
\]
For the second identity, each term satisfies
\(\bigl((aa^\sharp)^m a\bigr)^\sharp
=a^\sharp(aa^\sharp)^m=(a^\sharp a)^m a^\sharp\).
Uniform functional calculus and (RD.28–29) now prove
\(a_n\to a\) and \(a_n^\sharp\to a^\sharp\).
Thus \(\mathcal A^2\) is graph dense in \(\mathcal A\), and therefore in \(D(S)\). Explicitly, approximate a vector of \(D(S)\) by algebra vectors with graph error \(1/n\), and for each of those choose a product-span vector with a further graph error \(1/n\).

**Proof of the pairing characterization.** The forward implication of the right side of (RD.27) to the left follows from the adjoint identity, applied to \(b^\sharp a\), whose image under \(S\) is \(a^\sharp b\). Conversely, the assumed pairings extend by linearity to
\[
\langle S\xi,v\rangle=\langle w,\xi\rangle
\quad(\xi\in\mathcal A^2).
\]
Graph density extends this equality to all \(\xi\in D(S)\). It is exactly the adjoint-domain test \(v\in D(S^*)\), \(S^*v=w\). Since \(F=S^*\), this proves (RD.27). \(\square\)

In the modular notation of OA-MOD-TC, the equality of graph norms
\(\|\xi\|^2+\|S\xi\|^2=\|\xi\|^2+\|\Delta^{1/2}\xi\|^2\)
also makes \(\mathcal A^2\) a form core for \(\Delta\). This does not assert that every product vector belongs to \(D(\Delta)\), or that \(\mathcal A^2\) is an operator core for \(\Delta\).

<span id="oa-mod-rd-07--the-adjoint-intersection-of-the-right-ideal"></span>
<span id="OA-MOD-RD-07"></span>
<span id="oa-mod-rd-07"></span>
## OA-MOD-RD-07 — The adjoint intersection of the right ideal

**Theorem.** With \(\mathfrak n_r^*=\{b^*:b\in\mathfrak n_r\}\),
\[
R(\mathcal A_r)=\mathfrak n_r\cap\mathfrak n_r^*.
\tag{RD.32}
\]
More precisely, if \(\eta,\zeta\in\mathcal B_r\), then
\[
R_\eta^*=R_\zeta
\quad\Longleftrightarrow\quad
\eta\in D(F)\text{ and }F\eta=\zeta.
\tag{RD.33}
\]

**Proof.** If \(\eta\in\mathcal A_r\), (RD.3) gives \(R_\eta^*=R_{F\eta}\), proving one inclusion in (RD.32) and one implication in (RD.33).

Conversely suppose \(\eta,\zeta\in\mathcal B_r\) and \(R_\eta^*=R_\zeta\). For \(a,b\in\mathcal A\),
\[
\begin{aligned}
\langle a^\sharp b,\eta\rangle
&=\langle b,L_a\eta\rangle
=\langle b,R_\eta a\rangle\\
&=\langle R_\eta^*b,a\rangle
=\langle L_b\zeta,a\rangle
=\langle\zeta,b^\sharp a\rangle.
\end{aligned}
\]
The graph-core characterization (RD.27) proves \(\eta\in D(F)\), \(F\eta=\zeta\). Finally every operator in \(\mathfrak n_r\cap\mathfrak n_r^*\) has such a pair of representing right-bounded vectors, by the definitions, proving the remaining inclusion. \(\square\)

The theorem applies to any left Hilbert algebra satisfying the original four axioms. In particular, after OA-MOD-RD-04, it can be applied to the opposite algebra of the right Hilbert algebra \(\mathcal A_r\). That supplies the corresponding left-ideal statement once the left-bounded-vector spaces for that application have been defined. No identification of a full left completion is implicit in this observation.

<span id="oa-mod-rd-08--a-weighted-discrete-model-of-the-approximations"></span>
<span id="OA-MOD-RD-08"></span>
<span id="oa-mod-rd-08"></span>
## OA-MOD-RD-08 — A weighted discrete model of the approximations

Let \(I\) be any set and let \(\mu_i>0\). On \(\mathcal A=c_{00}(I)\), use pointwise products, complex conjugation, and
\[
\langle a,b\rangle=\sum_{i\in I}\mu_i a_i\overline{b_i},
\qquad H=\ell^2(I,\mu).
\tag{RD.34}
\]
Every nonnegative sum is the supremum of its finite subsums. Left multiplication by \(a\) has norm \(\sup_i|a_i|\), as follows by the coordinatewise upper bound and testing one coordinate. Pointwise products give the adjoint compatibility. Conjugation extends to an antiunitary involution on \(H\), so is closable. Each finite-support vector is its product with the indicator of its support, giving \(\mathcal A^2=\mathcal A\). These verify the four left Hilbert algebra axioms.

Both \(S,F\) are conjugation on all of \(H\). Right boundedness is exactly
\[
\mathcal B_r=\mathcal A_r=\ell^2(I,\mu)\cap\ell^\infty(I),
\qquad R_\eta=\operatorname{diag}(\eta_i),\quad
\|R_\eta\|=\sup_i|\eta_i|.
\tag{RD.35}
\]
Testing coordinate vectors proves necessity of the bound; summing the coordinate inequalities proves sufficiency.

For an arbitrary \(\eta\in H=D(F)\), the closed operator \(T_\eta\) is multiplication by \(\eta_i\), with exact domain
\[
D(T_\eta)=
\left\{\xi\in H:\sum_i\mu_i|\eta_i\xi_i|^2<\infty\right\}.
\tag{RD.36}
\]
This operator is closed by coordinatewise limits, and finite-coordinate truncations approximate both \(\xi\) and its displayed image, so \(c_{00}(I)\) is a graph core. Its polar data are
\[
h=k=\operatorname{diag}(|\eta_i|),\qquad
u_i=\begin{cases}\eta_i/|\eta_i|,&\eta_i\neq0,\\0,&\eta_i=0.\end{cases}
\tag{RD.37}
\]
The cutoff vector has entries \(f_n(|\eta_i|)\eta_i\); it is bounded because \(t f_n(t)\) has compact support. The graph convergence for \(F\) is simply
\[
2\sum_i\mu_i|f_n(|\eta_i|)-1|^2|\eta_i|^2\longrightarrow0.
\tag{RD.38}
\]
The zero coordinates contribute zero, and scalar dominated convergence applies to the summable family.

The product span has the exact description
\[
\mathcal A_r^2=\ell^1(I,\mu)\cap\ell^\infty(I).
\tag{RD.39}
\]
A product of two \(\ell^2(I,\mu)\) vectors belongs to \(\ell^1(I,\mu)\) by Cauchy–Schwarz, and a product of bounded vectors is bounded. Conversely, for \(v\in\ell^1(I,\mu)\cap\ell^\infty(I)\), let \(b_i=|v_i|^{1/2}\) and let \(a_i=v_i/|v_i|^{1/2}\) when \(v_i\neq0\), with \(a_i=0\) otherwise. Both factors are bounded and square summable, and \(v=ab\). Also \(v\in H\), since \(\sum_i\mu_i|v_i|^2\leq\|v\|_\infty\sum_i\mu_i|v_i|\). This proves (RD.39).

For counting weights on \(\mathbb N\), the vector \(v_n=1/n\) belongs to \(\mathcal A_r\) but not to \(\mathcal A_r^2\). Nevertheless its finite truncations converge in the graph norm of \(F\), which is \(\sqrt2\) times the Hilbert norm. Thus a product core can be a proper subspace.

Here \(M=M'\) is the algebra of all bounded diagonal multipliers. To check the commutant statement directly, an operator commuting with every one-coordinate projection preserves each coordinate line and hence is diagonal; boundedness bounds its diagonal coefficients. Conversely every bounded diagonal multiplier commutes with \(\mathcal A\). The finite-support indicators give positive contractions in \(R(\mathcal A_r)\) converging strongly to the identity. When \(I\) is uncountable, no sequence of finite-support indicators can do so, since a coordinate outside the union of its supports is annihilated by the whole sequence. Thus the global net in OA-MOD-RD-05 and the vectorwise sequence in OA-MOD-RD-04 serve different purposes.

<span id="oa-mod-rd-09--problems-and-worked-solutions"></span>
<span id="OA-MOD-RD-09"></span>
<span id="oa-mod-rd-09"></span>
## OA-MOD-RD-09 — Problems and worked solutions

**Problem 1: a genuine unbounded multiplier with a nontrivial kernel.** In the weighted discrete model take \(I=\{0\}\cup\mathbb N\), \(\mu_0=1\), \(\mu_n=n^{-4}\), and \(\eta_0=0,\eta_n=n\). Find its right multiplier and polar supports. Explain why the spectral cutoffs converge strongly to a proper projection but still approximate \(\eta\) in the graph norm of \(F\).

**Solution.** The vector belongs to \(H\), since \(\sum_{n\geq1}n^{-4}n^2=\sum_n n^{-2}<\infty\), but it is unbounded and hence not right bounded. Its closed right multiplier has
\[
(T_\eta\xi)_0=0,\quad (T_\eta\xi)_n=n\xi_n,\qquad
D(T_\eta)=\left\{\xi\in H:\sum_{n\geq1}n^{-2}|\xi_n|^2<\infty\right\}.
\]
This is a nonnegative self-adjoint diagonal operator, with \(h=k=T_\eta\). Its partial isometry is \(u=p=q=I-P_0\), where \(P_0\) projects onto coordinate zero. Thus \(f_n(k)\to I-P_0\), not to \(I\). Since \(\eta_0=0\), this projection fixes both \(\eta\) and \(F\eta=\eta\). Formula (RD.38) proves graph convergence. Each cutoff vector has finite support in the positive coordinates, because \(f_n(m)=0\) for integers \(m>e^{2n}\), so in this example the approximants even lie in \(c_{00}(I)\).

**Problem 2: Hilbert-norm approximation alone does not control the involution.** In OA-MOD-HA-09 take \(I=\mathbb N\), \(D_n=\operatorname{diag}(1,n^4)\). Let \(v^{(n)}\) have only one nonzero block, its \(n\)-th block equal to \(n^{-3}e_{12}\). Show that \(v^{(n)}\to0\) in \(H\) but not in the graph norm of \(F\).

**Solution.** The weighted squared norm of \(e_{12}\) in block \(n\) is \(n^4\), so \(\|v^{(n)}\|=n^{-1}\to0\). The exact formula in OA-MOD-HA-09 gives
\[
Fv^{(n)}=n e_{21}
\]
in that block and zero elsewhere. The weighted norm of \(e_{21}\) is one, so \(\|Fv^{(n)}\|=n\). All these vectors have finite support and lie in \(\mathcal A_r^2\), but their graph norms diverge. This does not conflict with graph density: a core theorem provides appropriate approximating vectors, and does not make every norm-convergent sequence converge in graph norm.

**Problem 3: squaring a monotone contraction family needs care.** Set
\[
c=\frac14\begin{pmatrix}2&0\\0&0\end{pmatrix},
\qquad
d=\frac14\begin{pmatrix}3&1\\1&1\end{pmatrix}.
\]
Verify \(0\leq c\leq d\leq I\), but \(c^2\not\leq d^2\). Explain which conclusion about the squared approximants in (RD.26) is valid.

**Solution.** The difference \(d-c=\frac14\begin{pmatrix}1&1\\1&1\end{pmatrix}\) is positive. The matrices \(d\) and \(I-d=\frac14\begin{pmatrix}1&-1\\-1&3\end{pmatrix}\) have nonnegative diagonal entries and positive determinants, so both are positive. However,
\[
d^2-c^2=\frac1{16}\begin{pmatrix}6&4\\4&2\end{pmatrix},
\qquad
\left\langle(d^2-c^2)\binom1{-2},\binom1{-2}\right\rangle=-\frac18.
\]
Thus the square map does not preserve this order. In (RD.26), positivity and contractivity of each square remain true. Strong convergence \(c_i\to I\) and the uniform contraction bound give \(c_i^2\to I\) strongly, by the displayed estimate there; self-adjointness gives strong* convergence. Monotonicity of the squares is unnecessary.

<span id="oa-mod-rd-10--exported-conclusions-and-the-remaining-modular-boundary"></span>
<span id="OA-MOD-RD-10"></span>
<span id="oa-mod-rd-10"></span>
## OA-MOD-RD-10 — Exported conclusions and the remaining modular boundary

This unit closes the general cutoff, right-algebra density, commutant-generation, original product-core, and ideal-intersection statements:

| Result | Exact exported conclusion |
| --- | --- |
| OA-MOD-RD-03 | Compact spectral cutoffs of a closed right multiplier produce right-algebra products with the exact adjoint-domain formula |
| OA-MOD-RD-04 | \(\mathcal A_r^2\) and \(\mathcal A_r\) are graph cores for \(F\); \(\mathcal A_r\) is a right Hilbert algebra; its closed involution is \(F\), whose adjoint is \(S\) |
| OA-MOD-RD-05 | \(R(\mathcal A_r)''=M'\), with explicit norm-controlled strong* approximants to every \(x\in M'\) |
| OA-MOD-RD-06 | \(\mathcal A^2\) is a graph core for \(S\), with the complete product-pairing test for \(D(F)\) |
| OA-MOD-RD-07 | \(R(\mathcal A_r)=\mathfrak n_r\cap\mathfrak n_r^*\), including the representing-vector involution |

All proofs retain arbitrary Hilbert spaces, nonunital algebras, nontrivial operator kernels, and possibly unbounded right multipliers. The graph-density sequence and the global operator-approximation net have their separate topologies stated. The analytic prerequisites remain the explicit contracts in OA-MOD-RD-01.

Further work must define the left-bounded-vector completion, prove its repeated-dualization and fullness identities, establish the modular resolvent estimates and the fundamental modular theorem, and construct the analytic Tomita algebra. The equality \(R(\mathcal A_r)''=M'\) proved here does not identify \(R(\mathcal A_r)\) with \(J M J\). No assertion \(JMJ=M'\) or \(\Delta^{it}M\Delta^{-it}=M\) has entered the proof. The general weight-to-Hilbert-algebra and weight-reconstruction theorems also retain their separate obligations.
