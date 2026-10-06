# Normal central hypertraces and joint localization

A compatible hypertrace need not be normal on the represented algebra. Normality on just its smaller center is enough for the positive cost of Lesson 82 to vanish. We prove that implication by identifying its central density and solving the resulting positive Markov fixed-point equation. We also give a quantitative localization bound for normalized central dimensions with controlled tails. Neither central normality nor the tail condition is inferred from general relative amenability.

The exact local inputs are [52.1–52.2](canonical-core-traces-and-integer-rounding.md) (actual expected pair, full corner and central lifts), [68.1–68.5](core-central-transition-bounds.md) (common basis, both joint density marginals and weighted stationarity), [70.1](joint-projection-transfer-and-partition-flow.md) (the full projection transfer), [72.2–72.3](finite-central-branches-and-joint-tests.md) (complete central branches), [81.2–81.6](relative-norm-averaging-and-central-density.md) (relative norm averaging and actual branch means), and [82.6–82.8](finite-cup-densities-and-positive-cost.md) (positive cost and its expected-algebra Følner criterion). Finite abelian positive \(L^1\) densities, normal tracial expectations and their trace adjointness are the declared programme prerequisites used in those lessons. Every new convexity, tail and fixed-point argument is proved below.

Human-source context is Sorin Popa, *Classification of amenable subfactors of type II*, DOI 10.1007/BF02392646, Sections 3.2 and 4.2, printed pp.205–206 and 211–214. Those sections provide compatible hypertraces and finite projection Følner tests. The extra central normality condition and the argument in this lesson are stated explicitly.

## A finite commutative probability algebra

Let \((D,\tau)\) be a finite abelian von Neumann algebra with faithful normal probability trace. Let \(U,V\subset D\) be unital von Neumann subalgebras and write \(Q=E_U\), \(P=E_V\). Suppose \(w\in D_+\) is bounded and has both marginals equal to one. No strictly positive lower bound on \(w\) is needed in this section. Define

\[
\begin{gathered}
Q(w)=P(w)=1,\\
Q_w(y)=Q(wy),\\
T f=Q_w(Pf)\quad(f\in L^1(U)_+),\\
\beta=Pf,\qquad
\delta_f=\|f-Tf\|_1.
\end{gathered}
\tag{83.1}
\]

The weighted map \(Q_w:D\to U\) is positive and unital. Its \(L^1\) action on \(V\) preserves integrals: for \(y\in L^1(V)_+\), \(\tau(Q_wy)=\tau(wy)=\tau(y)\), by \(P(w)=1\). Thus \(T\) is positive, unital and preserves the probability trace on \(U\). Both maps extend to positive integrable arguments by truncation. When taking a joint norm below, \(f\) and \(\beta\) are regarded as elements of \(L^1(D)\).

For \(L>0\), use the convex continuously differentiable function

\[
\begin{gathered}
\chi_L(t)=t^2\quad(0\leq t\leq L),\\
\chi_L(t)=2Lt-L^2\quad(t>L),\\
0\leq\chi_L(t)\leq2Lt,\\
0\leq\chi'_L(t)\leq2L.
\end{gathered}
\tag{83.2}
\]

It is \(2L\)-Lipschitz. All its compositions with the positive integrable elements in (83.1) are integrable. Conditional Jensen inequalities here can be proved without a pointwise disintegration: \(\chi_L\) is the supremum of its affine tangents at nonnegative rational arguments. Positivity and unitality imply that applying \(P\), or \(Q_w\), to \(\chi_L(y)\) majorizes each such tangent evaluated at the image of \(y\). The countable supremum gives Jensen. Apply the argument first to bounded truncations, then use normality and monotone convergence.

**Lemma 83.1 — the conditional Jensen deficit.** For every positive \(f\in L^1(U)\),

\[
\begin{gathered}
0\leq\tau(\chi_L(f))-\tau(\chi_L(\beta))\\
\leq\tau(\chi_L(f))-\tau(\chi_L(Tf))\\
\leq2L\delta_f.
\end{gathered}
\tag{83.3}
\]

**Proof.** Jensen for \(P\), followed by its trace preservation, gives the first inequality. Jensen for \(Q_w\), applied to \(\beta\in L^1(V)\), gives
\(\tau(\chi_L(Tf))\leq\tau(Q_w(\chi_L(\beta)))=\tau(\chi_L(\beta))\).
This proves the second inequality. The Lipschitz bound gives
\(|\tau(\chi_L(f))-\tau(\chi_L(Tf))|\leq2L\|f-Tf\|_1\).
All terms have already been shown integrable. \(\square\)

## Controlled tails give a full joint bound

Put \(r_f(L)=\tau(f1_{(L,\infty)}(f))\). This is the mass in the tail, rather than its measure or an operator norm.

**Theorem 83.2 — quantitative joint localization.** In the situation of (83.1),

\[
\begin{gathered}
\|f-Pf\|_1\\
\leq\sqrt{2L\delta_f}
+r_f(L)+2r_f(L/2)\\
\qquad(L>0).
\end{gathered}
\tag{83.4}
\]

The square-root term uses \(\tau(1)=1\). The conclusion applies to arbitrary positive integrable \(f\); its mass need not be one.

**Proof.** Convexity gives a nonnegative Bregman remainder
\[
\begin{gathered}
B_L(a,b)=\chi_L(a)-\chi_L(b)\\
-\chi'_L(b)(a-b)\geq0,\\
B_L(a,b)=(a-b)^2\\
\text{if }0\leq a,b\leq L.
\end{gathered}
\tag{83.5}
\]

The bounded operator \(\chi'_L(\beta)\) lies in \(V\). Trace adjointness therefore gives \(\tau(\chi'_L(\beta)(f-\beta))=0\). Equations (83.3)–(83.5) imply
\(\tau(1_{\{f\leq L,\ \beta\leq L\}}(f-\beta)^2)\leq2L\delta_f\).
Commutativity defines these intersections intrinsically as products of spectral projections. Cauchy–Schwarz bounds the \(L^1\) norm on that intersection by \(\sqrt{2L\delta_f}\).

On its complement, the scalar inequality
\[
\begin{gathered}
|f-\beta|
\leq f1_{\{f>L\}}+\beta1_{\{\beta>L\}}\\
\text{on }\{f>L\}\cup\{\beta>L\}
\end{gathered}
\tag{83.6}
\]
follows separately in the three cases where exactly one, or both, exceeds \(L\). The tail of \(\beta\) is controlled by that of \(f\). Indeed
\(\beta\leq L/2+P(f1_{\{f>L/2\}})\).
On the \(V\)-projection \(\{\beta>L\}\), this yields
\(\beta/2\leq P(f1_{\{f>L/2\}})\).
Integrate and use trace adjointness to obtain
\[
\tau(\beta1_{\{\beta>L\}})
\leq2r_f(L/2).
\tag{83.7}
\]
Adding the bounded part and the two tails proves (83.4). \(\square\)

**Corollary 83.3 — exact positive fixed points.** The positive \(L^1\) fixed points of \(T\) are exactly \(L^1(U\cap V)_+\). If \(Tf=f\), then \(Pf=f\) as elements of the full joint algebra \(L^1(D)\).

**Proof.** Set \(\delta_f=0\) in (83.4), then let \(L\to\infty\). Integrability gives both tails tending to zero, so \(f=Pf\). Thus \(f\) is affiliated with both \(U\) and \(V\); equivalently its spectral projections belong to their intersection. Conversely if \(f\) is positive integrable in that intersection, then \(Pf=f\) and \(Q(wf)=fQ(w)=f\), first for bounded truncations and then in \(L^1\). \(\square\)

A family \(\mathcal F\subset L^1(U)_+\) of mass-one densities is **uniformly integrable** when \(\sup_{f\in\mathcal F}r_f(L)\to0\) as \(L\to\infty\). For any net from such a family with \(\delta_f\to0\), (83.4) gives \(\|f-Pf\|_1\to0\). Choose a single large \(L\) controlling all tails, then make \(\delta_f\) small. Choosing \(L\) depending on one density after applying the estimate would not prove a uniform assertion.

If \(0\leq f\leq H1\), a shorter bound follows by ordinary squared Jensen:

\[
\begin{gathered}
\|f-Pf\|_2^2
=\tau(f^2)-\tau((Pf)^2)\\
\leq\tau(f^2)-\tau((Tf)^2)\\
\leq2H\delta_f,\\
\|f-Pf\|_1\leq\sqrt{2H\delta_f}.
\end{gathered}
\tag{83.8}
\]

The last squared difference uses that \(T\) is positive and unital, so both \(f,Tf\) lie between zero and \(H\).

## Return to the actual core and compatible state

Use the actual \(N\subset M\), \(S\subset R\), \(A\subset B\), full corner \(e=e_R^M\) and common basis of 52 and 68. Put \(C=N'\cap M\), \(D_0=Z(S)\vee Z(R)\). In this section \(D=Z(A)\vee Z(B)\), with its faithful corner labels in \(D_0\). Set

\[
\begin{gathered}
g=\sum_i a_i^*a_i,\qquad z=E_C(g),\\
k_{\rm joint}=d^{-1}E_{D_0}(g),\\
\ell_{\rm joint}=d^{-1}E_{D_0}(z),\\
v=d(k_{\rm joint}-\ell_{\rm joint}),\\
b=E_{Z(S)}(|v|),\qquad \widehat b\in Z(A).
\end{gathered}
\tag{83.9}
\]

The name \(k_{\rm joint}\) distinguishes the joint-center density from the ambient physical relative-commutant density \(k=z/d\) of Lesson 82. By 68.2, both inherited marginals of \(k_{\rm joint}\) are one. Also
\[
E_{Z(S)}(\ell_{\rm joint})=1.
\tag{83.10}
\]
To check this additional equality, \(z\in C\) implies \(E_N(z)\in Z(N)\). Since \(N\) is a factor and \(\tau(z)=\tau(g)=d\), \(E_N(z)=d1\). As \(z\in R\) and \(E_N|_R=E_S\), one has \(E_S(z)=d1\). Because \(z\) commutes with \(S\), this is also its \(Z(S)\)-expectation. Trace adjointness through \(D_0\) proves (83.10).

Let \(\varphi\) be an \(M\)-central state on \(B\) satisfying \(\varphi E_A=\varphi\). **Normality on the smaller represented center** means that its restriction to \(Z(A)\), transported by the canonical full-corner identification, is a normal functional on \(Z(S)\). Thus there is \(\mu\in L^1(Z(S))_+\) with \(\tau(\mu)=1\) such that

\[
\begin{gathered}
\varphi(\widehat s)=\tau(\mu s),\\
\beta_\mu=E_{Z(R)}(\mu).
\end{gathered}
\tag{83.11}
\]

This hypothesis concerns the canonical lift \(\widehat s\). The fact that \(\varphi|_M=\tau\) does not supply it: \(\widehat s\) is a represented central operator and is not asserted to be a physical element of \(M\).

**Proposition 83.4 — the exact normal central balance.** Under (83.11),

\[
k_{\rm joint}\beta_\mu
=\ell_{\rm joint}\mu
\quad\text{in }L^1(D_0).
\tag{83.12}
\]

**Proof.** Fix any bounded \(t\in D_0\), with lift \(x\in D\). The transfer of 68.2 is \(\mathcal I(x)=\sum_i a_i x a_i^*\in Z(B)\), with corner label \(dE_{Z(R)}(k_{\rm joint}t)\). Since \(x\) commutes with \(N\), and \(\varphi\) is \(M\)-central,
\[
\begin{gathered}
\varphi(\mathcal I(x))=\varphi(xg)=\varphi(xz),\\
d\tau(\beta_\mu k_{\rm joint}t)
=\tau(\mu zt).
\end{gathered}
\tag{83.13}
\]

The first equality is finite trace cyclicity for the state, with the physical \(a_i\). For the second equality on its first line, average \(g\) by \(N\)-unitaries in operator norm to \(z=E_C(g)\), as proved in 81.2. Each average preserves \(\varphi(xg)\), because \(x\) commutes with those unitaries and the state is central. Pass to the norm limit.

For completeness, the second line uses two different full-corner computations. Applying \(E_A\) to the central transfer gives the lift of \(dE_{Z(S)}E_{Z(R)}(k_{\rm joint}t)\). Its state value is \(d\tau(\mu E_{Z(R)}(k_{\rm joint}t))=d\tau(\beta_\mu k_{\rm joint}t)\). On the other hand \(z\in A'\cap B\), so \(xz\) commutes with \(A\) and \(E_A(xz)\in Z(A)\). Its corner label is \(E_S(tz)=E_{Z(S)}(tz)\). Compatibility gives \(\varphi(xz)=\tau(\mu tz)\). These formulas follow from the normal trace-preserving expected square, not from an assertion that \(x\) lies in \(M\).

Finally replace \(z/d\) in the last pairing by \(E_{D_0}(z/d)=\ell_{\rm joint}\). For unbounded \(\mu\), use its bounded truncations and the boundedness of \(z,t\). Testing against every bounded \(t\in D_0\) proves (83.12) by \(L^1\) duality. \(\square\)

**Theorem 83.5 — central normality annihilates the cost.** Every compatible \(M\)-central state satisfying (83.11) has

\[
\begin{gathered}
\mu=\beta_\mu
\in L^1(Z(S)\cap Z(R))_+,\\
\mu v=0,\qquad
\varphi(\widehat b)=0.
\end{gathered}
\tag{83.14}
\]

It therefore supplies the positive-cost Følner criterion of 82.8, with finite projections inside \(A\). If its restriction to \(Z(A)\) is faithful, then \(v=b=0\), so the full normal joint density identity of 81.15 holds for that actual core.

**Proof.** Apply \(E_{Z(S)}\) to (83.12). Equation (83.10) gives
\(\mu=E_{Z(S)}(k_{\rm joint}\beta_\mu)\).
This is exactly the fixed-point equation (83.1), with \(U=Z(S)\), \(V=Z(R)\), \(w=k_{\rm joint}\). Corollary 83.3 proves \(\mu=\beta_\mu\) in the full joint algebra. Substitution back into (83.12) gives \(\mu v=0\).

All these products occur in the abelian \(D_0\). Thus also \(\mu|v|=0\), and expectation adjointness yields \(\varphi(\widehat b)=\tau(\mu b)=\tau(\mu|v|)=0\). Corollary 82.8 now applies. If the central state is faithful, its density has support one. A bounded positive element with zero pairing against that faithful density is zero. Hence \(b=0\), and faithfulness of the inherited trace gives \(v=0\), as in 82.6. This is the joint density identity; equality of the two full physical commutant densities is a stronger assertion and is not inferred. \(\square\)

## Uniform integrability of actual projection dimensions

For a nonzero finite-trace projection \(p\in A\), let \(c=\operatorname{Tr}(p)\), \(\zeta=C_A(p)\), and normalize \(f_p=\zeta/c\). Both \(\tau(f_p)=1\) and \(E_{Z(R)}f_p=\beta/c\) use the canonical central dimension pairing of 68.5. That proposition gives
\(\|f_p-Tf_p\|_1\leq\Gamma_p\),
where \(T=E_{Z(S)}(k_{\rm joint}E_{Z(R)}(\,\cdot\,))\) and \(\Gamma_p\) is its explicit finite-basis and averaging error. Theorem 83.2 gives

\[
\begin{gathered}
J_p:=\frac{\|\zeta-\beta\|_1}{c}\\
\leq\sqrt{2L\Gamma_p}\\
{}+r_{f_p}(L)+2r_{f_p}(L/2).
\end{gathered}
\tag{83.15}
\]

Thus uniformly integrable normalized dimensions, together with the basis tests making \(\Gamma_p\to0\), give full joint localization. This establishes a sufficient condition absent from the bare stationarity estimate.

The actual cost is controlled as well. Choose the common norm average of 81.6, with error \(\eta>0\), before selecting \(p\). Let \(n\) be the number of complete smaller-center branches and retain its \(\Delta_{j,p}\) and the transfer error \(\epsilon_p\) of 70.1. Then

\[
\begin{gathered}
\frac{\operatorname{Tr}(p\widehat b)}c\\
\leq\epsilon_p+b_dJ_p
+n\eta+\sum_j\Delta_{j,p}.
\end{gathered}
\tag{83.16}
\]

**Proof.** The proof of 81.17 gives
\(\|\eta_{j,p}-a'_j\zeta\|_1\leq c(\eta+\Delta_{j,p})\).
The full branch norm identity of 72.3 and triangle inequality therefore bound
\(\sum_j\|(a_j-a'_j)\zeta\|_1\)
by
\(\|\gamma_p-dk_{\rm joint}\zeta\|_1+c(n\eta+\sum_j\Delta_{j,p})\).
The transfer bound of 70.1 and \(dk_{\rm joint}\leq b_d1\) give
\(\|\gamma_p-dk_{\rm joint}\zeta\|_1\leq c\epsilon_p+b_d\|\beta-\zeta\|_1\).
Finally 82.6 identifies the sum of all weighted branch gaps with \(\operatorname{Tr}(p\widehat b)\). Divide by \(c\). \(\square\)

There is also a state interpretation. Suppose a net of these projections has all prescribed \(M\)-unitary normalized commutators tending to zero and its normalized dimensions are uniformly integrable. Every weak-* cluster state of \(\operatorname{Tr}(p\,\cdot)/c\) is \(M\)-central and \(E_A\)-invariant by the converse proof of 82.7. Its smaller-center restriction is normal. Indeed, for any central projection with physical label \(q\),
\[
\tau(f_pq)\leq L\tau(q)+r_{f_p}(L).
\tag{83.17}
\]
Uniform integrability makes the second term uniformly small; then small \(\tau(q)\) makes the first small. The cluster state inherits this uniform absolute continuity. On a decreasing net of central projections tending to zero, normality of the finite trace makes their traces tend to zero, so the state values do also. For a decreasing bounded positive net, its spectral cut at any fixed positive threshold is a decreasing projection net tending to zero; bounding the remainder by that threshold proves order continuity. This is normality of the positive functional. Theorem 83.5 consequently applies to every cluster state.

This argument does not prove that general relative amenability supplies a normal central hypertrace or a uniformly integrable family. Near-one cyclic integer rounding, common-support bases, unrestricted exact full partition and the full bicommutant comparison remain separate assigned obligations.

![Convex deficit, central fixed point and the exact compatible-state density balance](figures/normal-central-hypertraces-and-localization.svg)

Figure 83.1. The first panel gives the maps and the exact normal balance (83.12). The second shows the conditional Jensen proof and tail bound, including the two-stage order of choosing parameters. The third states precisely which additional hypotheses produce zero cost. Positions are schematic, with no encoded traces or dimensions. Original editable source: [normal-central-hypertraces-and-localization.py](figures/normal-central-hypertraces-and-localization.py). The proof locators refer to this lesson. A three-dimensional scene would add no useful geometry.

## Exercises with complete solutions

### Exercise 83.1 — introductory

Suppose a mass-one density satisfies \(0\leq f\leq4\) and \(\|f-Tf\|_1<1/80000\). Give an explicit joint \(L^1\) localization bound.

**Solution.** Equation (83.8) gives \(\|f-Pf\|_1<\sqrt{8/80000}=1/100\). The strict hypothesis gives a strict conclusion. The estimate concerns the full joint norm; it is not merely a scalar integral identity.

### Exercise 83.2 — introductory

Use a four-point probability algebra whose points are pairs \((i,j)\in\{1,2\}^2\), each of mass \(1/4\). Let \(U\) record \(i\), \(V\) record \(j\), and let the weight matrix be \(\left(\begin{smallmatrix}3/2&1/2\\1/2&3/2\end{smallmatrix}\right)\). Compute \(Tf\), \(Pf\) and the fixed densities for \(f=(a,b)\in U_+\).

**Solution.** Both weight marginals equal one. Ordinary \(P\) averages the two row coordinates, so \(Pf=(a+b)/2\) on both columns. Weighted \(Q_w\) fixes that scalar, hence \(Tf=(a+b)/2\) on both rows. A positive fixed density has \(a=b\); these are exactly the positive elements of \(U\cap V=\mathbb C1\). This finite model illustrates the Markov theorem and is not claimed to be an actual Jones core.

### Exercise 83.3 — intermediate

On the unit interval with Lebesgue probability measure, let \(f_n=n1_{(0,1/n)}\). Is this mass-one family uniformly integrable? Contrast it with any family of mass-one densities bounded above by a common constant.

**Solution.** Each \(f_n\) has integral one. For every fixed \(L\), choose \(n>L\); then \(r_{f_n}(L)=1\). The supremum of the tails therefore never tends to zero. In contrast, if every density is at most \(H\), the tails are zero for \(L\geq H\). This calculation concerns the tail condition alone and asserts no Følner properties for these densities.

### Exercise 83.4 — intermediate

Explain the distinction between a hypertrace normal on \(Z(A)\), one faithful there, and one normal on all of \(B\). State exactly what each of the first two hypotheses gives in Theorem 83.5.

**Solution.** Normality on \(Z(A)\) gives a positive integrable central density \(\mu\), potentially vanishing on a central region. The theorem gives \(\mu v=0\) and an annihilating state, hence selected positive-cost Følner projections. If that central restriction is also faithful, \(\mu\) has support one; then \(v=0\) everywhere and the full normal joint identity holds. Normality on all of \(B\) is a stronger requirement than normality on its subalgebra \(Z(A)\); the proof never assumes it. None of these conclusions identifies the full physical densities \(k_0\) and \(k\).

### Exercise 83.5 — advanced

For a family of mass-one dimensions assume \(r_f(L)\leq1/L\) for every \(L>0\). Find a sufficient numerical stationarity defect for \(\|f-Pf\|_1<1/100\), using (83.4).

**Solution.** Its two tail terms sum to at most \(1/L+4/L=5/L\). Choose \(L=1000\); this contributes at most \(1/200\). If \(\delta_f<1/80000000\), the square-root term is strictly below \(\sqrt{2000/80000000}=1/200\). Thus the total is strictly below \(1/100\). The choice of \(L\) controls the whole family before its stationarity tolerance is set.

### Exercise 83.6 — advanced

Why does \(\tau(\mu v)=0\) alone fail to establish the cost conclusion? Identify the extra steps that the actual compatible state supplies.

**Solution.** A signed scalar integral can cancel. On two points of equal mass, take \(\mu=1\) and \(v=(1,-1)\); the signed integral is zero while \(\tau(\mu|v|)=1\). Proposition 83.4 supplies the entire \(L^1(D_0)\) equality \(k_{\rm joint}\beta_\mu=\ell_{\rm joint}\mu\), tested against every bounded joint element. The smaller marginal and the positive fixed-point theorem then give \(\mu=\beta_\mu\). Substitution yields the operator identity \(\mu v=0\). Commutativity makes \(\mu|v|=0\), which is the absolute-cost assertion. No scalar cancellation was substituted for any of these steps.

## Status and precise remaining hypothesis

The conditional Jensen estimate, quantitative joint localization, exact positive fixed points, actual normal central balance, central normality implication and uniform integrability route are proved here. General relative amenability has not supplied either extra hypothesis. The full original assignment remains active, including unrestricted exact full finite partition, common-stage or generating construction, central rounding and common-support basis, all finite pair and bicommutant comparisons, represented and opposite canonical traces, every original source clause, exercise, note and exact prerequisite.

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026. Public domain (CC0).*
