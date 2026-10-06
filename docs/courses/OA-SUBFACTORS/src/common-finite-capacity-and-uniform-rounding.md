# Common finite capacity and uniform rounding

Finite unit capacity in the smaller canonical algebra cannot hide from the larger center. A common finite basis enlarges every finite-trace smaller central unit to a finite-trace larger central unit. We use this to identify the finite-capacity regions of both algebras, prove equality of their unit capacities, and round on a finite common block with one estimate valid for every ambient unitary. The residual general localization problem consequently concerns the infinite-capacity region.

The exact local providers are 52.1–52.4 (the actual expected pair, full corner, common matrix deletion and dimension prescription), [68.1–68.5](core-central-transition-bounds.md) (a common basis containing the identity, positive central transfer, the support bound, larger dimensions and weighted stationarity), [83.3–83.5](normal-central-hypertraces-and-localization.md) (positive integrable fixed points and central-normal cost annihilation), and [85.1–85.2](canonical-capacity-and-optimal-dimension-repair.md) (finite central unit trace and finite-capacity atomicity). We retain their declared trace, expectation and projection-comparison prerequisites. The new statements and their proofs are given below.

Human context is Sorin Popa, *Classification of amenable subfactors of type II*, DOI 10.1007/BF02392646, Theorem 4.2.2, printed pp.213–214. Its unrestricted rounding problem remains assigned. A nonzero common block does not supply a trace-near-one common bounded frame or an exact full finite partition.

## A finite central unit has a finite common hull

Let \(N\subset M\) be a proper finite-index II₁ inclusion, \(d=[M:N]>1\), with any actual core \(S\subset R\). Use

\[
\begin{gathered}
e=e_R^M,\quad A=\langle N,e\rangle,\\
B=\langle M,e\rangle,\\
U=Z(S),\quad V=Z(R),\\
W=U\cap V,\quad D_0=U\vee V,\\
D=Z(A)\vee Z(B).
\end{gathered}
\tag{86.1}
\]

The canonical trace is \(\operatorname{Tr}\), with \(\operatorname{Tr}(e)=1\). Physical labels in \(D_0\) and their represented lifts in \(D\) are related by the faithful full-corner identification of 52.2 and 68.2. We write a hat for this lift. The inherited probability trace on \(R\) is \(\tau\).

For the basis of 68.1, write \(a_1=1\), \(g=\sum_i a_i^*a_i\), and \(h=\sum_i f_i\in K_1\subset N\). Here \(E_A(g)=h\), \(\tau(h)=d\), and \(\sum_i a_i a_i^*=d1\). The positive central transfer is

\[
\begin{gathered}
\mathcal I(x)=\sum_i a_i x a_i^*,\\
\mathcal I(\widehat z)=d\,\widehat{P_\kappa z},
\quad P_\kappa=E_V(\kappa\,\cdot),\\
\kappa=d^{-1}E_{D_0}(g).
\end{gathered}
\tag{86.2}
\]

**Lemma 86.1 — a finite larger-center hull.** Suppose \(z\in U\) is a nonzero projection and \(t=\operatorname{Tr}(\widehat z)<\infty\). Let \(r=s(P_\kappa z)\in V\). Then

\[
\begin{gathered}
0\neq\widehat z\leq\widehat r,\qquad
\widehat r\in Z(B),\\
\operatorname{Tr}(\widehat r)\leq dt<\infty,\\
\dim(rV)\leq\lfloor dt\rfloor.
\end{gathered}
\tag{86.3}
\]

The individual hull \(r\) is not claimed to belong to \(W\).

**Proof.** The transfer \(\mathcal I(\widehat z)\) is positive and central in \(B\) by 68.2. Its identity basis summand is \(\widehat z\), so it majorizes \(\widehat z\). Its support is \(\widehat r\); therefore \(\widehat z\leq\widehat r\). The projection support estimate 68.11 gives \(P_\kappa z\geq r/d\). Consequently \(\mathcal I(\widehat z)\geq\widehat r\).

The trace of this transfer is exactly \(dt\). Each product involved is trace class because \(\widehat z\) is finite trace and the basis is finite and bounded. Trace cyclicity and adjointness of \(E_A\) give

\[
\begin{gathered}
\operatorname{Tr}(\mathcal I(\widehat z))
=\operatorname{Tr}(\widehat z g)\\
=\operatorname{Tr}(\widehat z h)
=dt.
\end{gathered}
\tag{86.4}
\]

For the last equality, \(x\mapsto\operatorname{Tr}(\widehat z x)\) is a finite normal trace on the factor \(N\): \(\widehat z\in Z(A)\) commutes with \(N\). Its value on \(1\) is \(t\), so its restriction to \(N\) is \(t\tau_N\). Apply this to \(h\in K_1\subset N\), whose normalized trace is \(d\). Monotonicity now gives \(\operatorname{Tr}(\widehat r)\leq dt\).

Finally apply 85.2 in the larger row to the finite central unit \(\widehat r\). Its center \(rV\) has at most \(\lfloor\operatorname{Tr}(\widehat r)\rfloor\leq\lfloor dt\rfloor\) atoms. This establishes all claims. No inclusion \(Z(B)\subset A\) is used. \(\square\)

## The maximal finite-capacity region is common

Let \(K_A=C_A(1)\in[1,\infty]^U\) and \(K_B=C_B(1)\in[1,\infty]^V\) be the extended capacities of 85.2. Their finite regions and corresponding represented projections are

\[
\begin{gathered}
f_A=1_{\{K_A<\infty\}}\in U,\\
f_B=1_{\{K_B<\infty\}}\in V,\\
\widehat f_A=\sup_{\substack{z\in U\ {\rm projection}\\
\operatorname{Tr}(\widehat z)<\infty}}\widehat z,\\
\widehat f_B=\sup_{\substack{r\in V\ {\rm projection}\\
\operatorname{Tr}(\widehat r)<\infty}}\widehat r.
\end{gathered}
\tag{86.5}
\]

These are suprema of central projections in their respective algebras. The equality with the spectral finite regions follows in each row from the increasing spectral sets \(1_{\{K\leq j\}}\), whose unit traces are at most \(j\), and from the fact that a finite integral \(\tau(Kz)\) forces \(K<\infty\) almost everywhere on \(z\).

**Theorem 86.2 — a common finite region.** The two represented projections in (86.5) agree. Their common physical label \(f\) belongs to \(W\).

**Proof.** Lemma 86.1 places each finite-trace smaller central projection below a finite-trace larger central projection. Taking their suprema gives \(\widehat f_A\leq\widehat f_B\).

For the reverse inequality, fix a finite-trace \(\widehat r\in Z(B)\). Put \(y=E_A(\widehat r)\). Bimodularity shows \(y\in Z(A)\), because \(\widehat r\) commutes with \(A\). The element \(y\) is positive, bounded and integrable, with \(\operatorname{Tr}(y)=\operatorname{Tr}(\widehat r)\). Its central spectral projection \(z_j=1_{[1/j,\infty)}(y)\) has trace at most \(j\operatorname{Tr}(y)\); thus \(z_j\leq\widehat f_A\). Normal spectral calculus gives \(s(y)\leq\widehat f_A\).

The projections \(\widehat r,\widehat f_A\) commute. Their product \(v=\widehat r(1-\widehat f_A)\) is a projection and

\[
\begin{gathered}
E_A(v)=(1-\widehat f_A)y=0,\\
v=0,\qquad \widehat r\leq\widehat f_A.
\end{gathered}
\tag{86.6}
\]

The second line uses faithfulness of the canonical expectation. It is faithful because it preserves the faithful normal semifinite trace: a positive element with zero expectation has trace zero, and hence is zero. Taking the larger-center supremum gives \(\widehat f_B\leq\widehat f_A\).

The equality is between actual represented operators. Faithful Jones-corner compression then identifies both physical labels, so \(f=f_A=f_B\in U\cap V\). The proof does not turn the individual hull from 86.1 into a common projection. \(\square\)

## The two capacities agree on that region

**Lemma 86.3 — extended capacity balance.** Extend positive conditional expectations to extended measurable functions by increasing bounded truncations. Then

\[
\begin{gathered}
K_B=P_0K_A,\qquad P_0=E_V,\\
K_Af=Q_\kappa(K_Bf),\\
Q_\kappa=E_U(\kappa\,\cdot).
\end{gathered}
\tag{86.7}
\]

The second identity is asserted on the common finite region, where both capacities are finite almost everywhere. Their integrals on the entire region can still be infinite.

**Proof of the first identity.** The finite projections of \(A\), directed by finite joins, increase strongly to \(1\), since \(\operatorname{Tr}|_A\) is semifinite. Their dimensions \(\zeta_p=C_A(p)\) increase essentially to \(K_A\), by the extended-dimension construction of 85.2. The larger dimension formula 68.12 gives \(C_B(p)=P_0\zeta_p\). Normality of the larger dimension and of the extended positive expectation therefore gives \(K_B=P_0K_A\). This uses the old unit and old traces; no matrix deletion has yet occurred.

For the second identity, put \(z_j=1_{\{K_A\leq j\}}\leq f\). Every projection \(z\leq z_j\) in \(U\) has finite unit trace. Apply (86.4) and the transfer formula (86.2). The resulting finite pairings are

\[
\begin{gathered}
d\tau(K_Az)
=\operatorname{Tr}(\mathcal I(\widehat z))\\
=d\tau(K_BP_\kappa z),\\
\tau(K_Az)=\tau(K_B\kappa z).
\end{gathered}
\tag{86.8}
\]

The last equality is expectation adjointness extended to positive arguments by normal monotone convergence. Pairing against all subprojections of \(z_j\) identifies the restricted positive density: \(z_jQ_\kappa(K_B)=z_jK_A\). Because \(f\in W\), bimodularity permits replacing \(K_B\) by \(K_Bf\) on this region. Let \(j\) increase. Since \(z_j\uparrow f\), the second identity follows. \(\square\)

**Theorem 86.4 — one common unit-capacity function.** There is a positive extended function \(K\) affiliated with \(W\) such that

\[
\begin{gathered}
K_A=K_B=K\\
\text{in the full joint algebra},\\
f=1_{\{K<\infty\}}\in W,\\
K=\infty\text{ on }1-f,\\
w_j=1_{\{K\leq j\}}\in W,\quad w_j\uparrow f,\\
\operatorname{Tr}(\widehat w_j)=\tau(Kw_j)\leq j,\\
\dim(w_jU),\ \dim(w_jV)\leq j.
\end{gathered}
\tag{86.9}
\]

An empty \(w_j\) contributes zero dimensions. Both physical and represented common finite regions are countable unions of atoms, but the complement may contain diffuse regions or infinite-capacity atoms.

**Proof.** There is nothing to prove on \(f=0\). Otherwise restrict the two expectations to \(fD_0\) and use the probability trace \(\tau_f=\tau/\tau(f)\). Common centrality of \(f\) preserves both weight marginals. The map \(T=Q_\kappa P_0\) is positive, unital and \(\tau_f\)-preserving. Lemma 86.3 gives the extended fixed-point identity \(T(K_Af)=K_Af\).

Write \(a=K_Af\), regarded as a finite almost-everywhere positive function on \(f\). For each \(L>0\), its bounded truncation \(a_L=\min(a,Lf)\) satisfies

\[
\begin{gathered}
T(a_L)\leq T(a)=a,\\
T(a_L)\leq Lf,\qquad T(a_L)\leq a_L,\\
\tau_f(T(a_L))=\tau_f(a_L),\\
T(a_L)=a_L.
\end{gathered}
\tag{86.10}
\]

The last equality follows from positivity and faithfulness of the finite trace on the nonnegative difference. Thus 83.3 applies to each bounded, integrable \(a_L\), giving \(P_0a_L=a_L\). Their spectral projections belong to \(fU\cap fV=fW\). Increasing \(L\) shows \(a\) is affiliated with \(W\), and \(P_0a=a\). The first identity of 86.7 now gives \(K_Bf=K_Af\).

By 86.2, both capacities equal infinity on \(1-f\). The full extended function obtained by joining \(a\) and that infinite value is affiliated with \(W\), proving the first three assertions. Every \(w_j\) has finite unit trace at most \(j\tau(w_j)\leq j\). Apply 85.2 in both rows for the center dimension bounds. The finite region is also the countable atomic region already supplied separately by 85.2. \(\square\)

The truncation argument is essential. We have not applied an \(L^1\) fixed-point theorem directly to a capacity of infinite integral.

## A normal state and zero canonical cost on the finite region

Let \(v=d(k_{\rm joint}-\ell_{\rm joint})\in D_0\) and \(b=E_U(|v|)\in U_+\) be the actual discrepancy and positive cost of 83.9. These use the ambient relative-commutant density in 82–83; they are not an identification of the full physical densities \(k_0\) and \(k\).

**Proposition 86.5 — automatic normal compatible states.** For every nonzero \(w_j\), the normal state

\[
\begin{gathered}
t_j=\operatorname{Tr}(\widehat w_j)>0,\\
\varphi_j(x)=t_j^{-1}\operatorname{Tr}(\widehat w_jx)
\\ (x\in B),\\
\varphi_jE_A=\varphi_j,\\
\varphi_j(uxu^*)=\varphi_j(x)
\\ (u\in\mathcal U(M)),\\
\mu_j=t_j^{-1}Kw_j,\qquad \tau(\mu_j)=1
\end{gathered}
\tag{86.11}
\]

has the indicated smaller-center density, and

\[
fv=0,\qquad fb=0.
\tag{86.12}
\]

**Proof.** The represented \(\widehat w_j\) is central in \(B\) and finite trace. Its trace pairing defines a normal positive functional of mass \(t_j\), and cyclicity proves \(M\)-centrality. Trace adjointness and \(\widehat w_j\in A\) give compatibility with \(E_A\). Its pairing with \(\widehat s\in Z(A)\) is \(\tau(Kw_js)/t_j\), establishing the density formula.

Theorem 83.5 applies to this normal compatible state and gives \(\mu_jv=0\). The function \(K\) is finite and at least one on \(w_j\); hence \(\mu_j\) is strictly positive there. Division on its support gives \(w_jv=0\). Bimodularity over \(w_j\in U\) then gives \(w_jb=E_U(w_j|v|)=0\). Let \(j\) increase and use normality to obtain (86.12). No amenability assumption was needed to construct these states. No equality \(k_0=k\) on the entire physical relative commutant is asserted. \(\square\)

## Uniform rounding on a nonzero finite-capacity block

**Theorem 86.6 — one integer works for all ambient unitaries.** Suppose \(f\neq0\). For every \(\varepsilon>0\) and positive integer \(k_0\), a common matrix deletion gives an actual core \(S^0\subset R^0\), a nonzero \(z\in Z(S^0)\cap Z(R^0)\), and a finite projection \(q\in\widetilde A=\langle N,e_{R^0}^M\rangle\) with

\[
\begin{gathered}
k\geq k_0,\\
C_{\widetilde A}(q)=C_{\widetilde B}(q)=kz,\\
\frac{\|[q,u]\|_{2,\widetilde{\operatorname{Tr}}}}
{\sqrt{\widetilde{\operatorname{Tr}}(q)}}
<\varepsilon
\\ \text{for every }u\in\mathcal U(M).
\end{gathered}
\tag{86.13}
\]

The projection is a sum of \(k\) orthogonal pieces equivalent inside \(\widetilde A\) to \(e_{R^0}^M\widehat z\). The conclusion requires no relative amenability assumption and no finite-dimensionality of the entire smaller center.

**Proof.** Some \(w_j\) is nonzero. By 86.4, its common center \(w_jW\) is finite-dimensional. Choose any of its nonzero atoms \(z\). The common capacity is a scalar \(Kz=\theta z\), with \(1\leq\theta\leq j\). The projection \(p=\widehat z\) belongs to both represented centers, has finite trace \(\theta\tau(z)\), and commutes with every ambient unitary.

Choose a common \(M_n\subset S\) and delete it as in 52.3 and 51.5. This produces an actual core, identifies the old centers with the new ones, and multiplies their capacities and old finite-projection traces by \(n^2\). The physical label \(z\) is unchanged. Pick \(n\) so large that \(k=\lfloor n^2\theta\rfloor\geq k_0\) and \(k>4/\varepsilon^2\). Prescription 52.4 inside the finite projection \(p\), now measured in the new trace, gives \(q\leq p\) with smaller dimension \(kz\). Its larger dimension is \(kz\) by 68.12, since \(z\) also belongs to the larger center.

Put \(r_n=n^2\theta-k\in[0,1)\). The removed projection \(p-q\) has trace \(r_n\tau(z)\), whereas \(q\) has trace \(k\tau(z)\). Since \(p\) commutes with every \(u\), the whole-projection estimate is

\[
\begin{gathered}
\widetilde{\operatorname{Tr}}(p-q)=r_n\tau(z),\\
\widetilde{\operatorname{Tr}}(q)=k\tau(z),\\
\delta_u(q)\leq2\sqrt{r_n/k}
<2/\sqrt{k}<\varepsilon.
\end{gathered}
\tag{86.14}
\]

For \(r_n=0\), take \(q=p\), and the defect is zero. Otherwise unitary invariance bounds the commutator of the removed projection by twice its Hilbert–Schmidt norm, giving the same estimate. This is one bound for all ambient unitaries, so no finite test set is selected.

Finally prescribe \(k\) successive orthogonal pieces of dimension \(z\) inside \(q\). Their remaining dimensions are nonnegative integer multiples of \(z\); the final remainder is zero by faithfulness. Projection comparison 52.4 identifies each piece with the new Jones-corner projection \(e_{R^0}^M\widehat z\). \(\square\)

The theorem discharges the integer rounding problem whenever the actual common finite-capacity region is nonzero. If \(f=0\), both capacities are infinite everywhere. Existence of bounded prescribed dimensions is then unrestricted, by 85.3, but obtaining a small-cost nearly scalar profile from general amenability remains necessary for the current repair route. The second near-one local form, unrestricted full finite partition, common-stage alignment, generation and all other original source residuals remain assigned.

![The common finite-capacity region, bounded truncation proof and uniform floor cut.](figures/common-finite-capacity-and-uniform-rounding.svg)

*Figure 86.1. Panel A depicts the actual central transfer and the separate faithfulness argument establishing the maximal common region; the individual larger-center support is not claimed common. Panel B shows the bounded truncations used in 86.10 and a countable probability diagnostic with finite capacity everywhere but infinite total unit trace. Panel C uses \(\theta=5/2\), \(\tau(z)=2/5\) and \(n=3\). The bar width is 20 pixels per dimension unit, and its height is \(80\tau(z)=32\) pixels; its areas therefore encode exactly the retained trace \(44/5\) and removed trace \(1/5\). These numerical parameters are not a claimed actual core realization. The universal bound is (86.14); the scope statement retains the infinite-capacity case and the full original residuals. [Editable figure source](figures/common-finite-capacity-and-uniform-rounding.py). Human context: Popa, Theorem 4.2.2, printed pp.213–214.*

## Exercises with complete solutions

### Exercise 86.1 — the hull trace

Suppose \(d=9/2\) and a represented smaller central unit has trace \(t=3/2\). What bound does 86.1 give for its larger-center support trace and the number of larger-center atoms there? Must that support itself be common central?

**Solution.** The bound is \(dt=27/4\), so its larger center has at most \(\lfloor27/4\rfloor=6\) atoms. Lemma 86.1 gives a projection in \(Z(B)\) dominating the initial unit; it does not prove that individual support belongs to \(Z(A)\). The common projection in 86.2 is the maximal finite-capacity region, proved by a separate reverse argument using \(E_A\) and faithfulness.

### Exercise 86.2 — expectation support

Let \(\widehat r\in Z(B)\) have trace \(2\), and put \(y=E_A(\widehat r)\). Bound the trace of \(1_{[1/5,\infty)}(y)\). Explain why the proof uses spectral projections of \(y\), rather than treating \(y\) as a projection.

**Solution.** Trace preservation gives \(\operatorname{Tr}(y)=2\), and \(y\geq(1/5)1_{[1/5,\infty)}(y)\), so the spectral projection has trace at most \(10\). A positive expectation of a projection need not be a projection. Bimodularity only gives that \(y\) is central in \(A\). Its nonzero spectral thresholds are actual central projections of finite trace; their supremum contains its support. Faithfulness applied to \(\widehat r(1-\widehat f_A)\) then supplies the reverse domination.

### Exercise 86.3 — an infinite integral

On \(\mathbb N\), let the probability weights be \(m_j=2^{-j}\) and put \(K(j)=2^j\). Compute \(\tau(K)\) and \(\tau(K1_{\{K\leq2^J\}})\). Does the example permit applying an \(L^1\) fixed-point theorem directly to \(K\)?

**Solution.** Each atom contributes \(m_jK(j)=1\). Thus \(\tau(K)=\sum_{j\geq1}1=\infty\), while the truncated spectral region contains \(j=1,\ldots,J\), giving unit trace \(J\). The capacity is finite on every atom but not integrable on their union. Theorem 86.4 instead proves that each bounded truncation \(\min(K,L)\) is an integrable fixed point before applying 83.3. These numerical data illustrate that distinction; no actual core realization is claimed.

### Exercise 86.4 — a subinvariant bounded truncation

Let \(T\) be positive, unital and trace preserving on a finite probability algebra. Suppose a positive extended function \(a\), finite almost everywhere, satisfies \(Ta=a\). Prove that \(a_L=\min(a,L)\) is fixed without using the integral of \(a\).

**Solution.** From \(a_L\leq a\) and \(a_L\leq L1\), positivity and unitality give \(Ta_L\leq a\) and \(Ta_L\leq L1\), hence \(Ta_L\leq a_L\). The difference is bounded positive and has trace zero because \(T\) preserves the trace of the bounded \(a_L\). Faithfulness makes the difference zero. Every integral in this argument is finite, independently of \(\tau(a)\).

### Exercise 86.5 — the exact floor loss

Take a common finite-capacity block with \(\theta=5/2\) and \(\tau(z)=2/5\). For \(n=3\), compute the rounded integer, the old and new unit traces, the retained trace, the removed trace, and the uniform bound in 86.14.

**Solution.** The old unit trace is \((5/2)(2/5)=1\). The new capacity is \(n^2\theta=45/2\), so \(k=22\) and \(r_n=1/2\). The new unit trace is \(9\); the retained trace is \(22(2/5)=44/5\); the removed trace is \((1/2)(2/5)=1/5\). The relative defect is at most \(2\sqrt{(1/5)/(44/5)}=2/\sqrt{44}=1/\sqrt{11}\) for every ambient unitary. These inputs obey the necessary unit-trace bound; the arithmetic does not construct an actual core with the proposed parameters.

### Exercise 86.6 — zero cost and its remaining scope

Assume the common finite-capacity region has positive inherited trace. Which exact joint density and cost conclusions follow there, and why do they not finish the original assignment?

**Solution.** The nonzero finite common cuts \(w_j\) carry the normal compatible states 86.11 with strictly positive central densities on those cuts. Theorem 83.5 gives \(w_jv=0\) and hence \(w_jb=0\). Increasing the cuts gives \(fv=fb=0\). This identifies the two joint-center densities on \(f\), not the entire physical densities \(k_0\) and \(k\). Uniform integer rounding on a nonzero common block follows from 86.6. Its support need not be trace-near-one. It supplies neither an exact full finite whole-tunnel partition nor common-stage alignment, unrestricted generation, the full bicommutant route, corrected arbitrary-depth reconstruction or the remaining source clauses and prerequisites.

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026. Public domain (CC0).*
