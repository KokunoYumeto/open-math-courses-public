# Selecting a compatible hypertrace

This reading gives an exact compact variational formulation of the one-state goal and proves the actual preservation conditions for represented-center reweighting. A new finite-basis estimate permits approximate centrality rather than imposing exact invariance on every selected cut. We also identify the precise conditional-expectation change when a singular functional is made normal in its own abelian GNS representation.

These results do not establish the unrestricted amenability-to-zero-cost implication. They isolate an actual finite family of quadratic tests for a low-cost selection, and an exact operator-order obstruction to that selection. No condition requiring every singular state to have zero cost is imposed.

## The actual inclusion and its providers

Use the actual proper finite-index II₁ inclusion \(N\subset M\), actual core \(S\subset R\), and
\[
\begin{gathered}
e=e_R^M,\quad A=\langle N,e\rangle,\quad B=\langle M,e\rangle,\\
E=E_A:B\longrightarrow A,\quad D=Z(A)\vee Z(B),\\
U=Z(S),\quad V=Z(R),\quad D_0=U\vee V,\\
Q=E_U,\quad P=E_V,\quad C=N'\cap M .
\end{gathered}
\tag{AS.1}
\]
The normal semifinite tracial expectation \(E\), finite tracial expectations \(P,Q\), actual full joint lift \(t\mapsto\widehat t\), and common partial orthonormal basis \((a_i)_{i=1}^{t_0}\subset K\subset R\) are the precise providers 52.1–52.2, 58.1's basis-extension part and 68.1–68.2. In particular
\[
\begin{gathered}
a_1=1,\quad \|a_i\|\leq\sqrt d,\quad t_0=\lceil d\rceil,\\
m=\sum_i a_iE_N(a_i^*m)\quad(m\in M),\\
E|_M=E_N,\qquad E(\widehat t)=\widehat{Q(t)} .
\end{gathered}
\tag{AS.2}
\]
Neither core is assumed factorial; no extremality, finite-depth or separability hypothesis is added.

At \(d=4\) the completed actual cost computation gives zero already. For \(d>4\), retain the exact actual tail projection \(f\in K\), \(\tau(f)=p\), and
\[
\begin{gathered}
p=(1-\sqrt{1-4/d})/2,\quad q=1-p,\\
k_F=(q/p)f+(p/q)(1-f),\\
w=E_{D_0}(k_F),\quad \ell=E_{D_0}(E_C(k_F)),\\
r=p/q,\quad R_*=q/p,\quad H=(q/p)^2,\\
r1\leq w,\ell\leq R_*1,\quad Q(w)=P(w)=Q(\ell)=1,\\
b=dQ(|w-\ell|)
=d^2\sqrt{1-4/d}\,Q(|E_{D_0}(f-E_C(f))|),\\
a=\widehat b\in Z(A)_+,\quad
\theta=\ell/w,\quad H^{-1}\leq\theta\leq H .
\end{gathered}
\tag{AS.3}
\]
No original larger marginal \(P(\ell)=1\) is asserted.

The [completed normal-component reading](hypertraces-and-normal-central-components.md), JC.3–JC.14, and [singular-state reading](singular-hypertraces-jones-ideals-and-entropy.md), SC.1–SC.15, supply the normal-component and singular-state reductions used below. General relative amenability supplies a state \(\psi\) with
\[
\begin{gathered}
\psi E=\psi,\qquad \psi(mx)=\psi(xm)\quad(m\in M,\ x\in B),\\
\psi|_M=\tau .
\end{gathered}
\tag{AS.4}
\]
If one such state has a nonzero normal represented-center component, JC already supplies a zero-cost state. Otherwise every compatible state has purely singular center restrictions, and SC supplies \(\psi(J_e)=0\), where \(J_e=\overline{\operatorname{span}(BeB)}^{\|\cdot\|}\). For a fixed normalized state in this remaining branch,
\[
\begin{gathered}
\nu(s)=\psi(\widehat s),\quad \alpha=\nu Q,\quad \gamma=\alpha P,\\
\gamma(wt)=\alpha(\ell t),\qquad \gamma(t)=\alpha(\theta t),\\
b_{\log}=Q((\theta-1)\log\theta),\\
\nu(b_{\log})=\gamma(\log\theta)-\alpha(\log\theta),\\
\nu(b)\leq dR_*\sqrt{H\,\nu(b_{\log})}.
\end{gathered}
\tag{AS.5}
\]
All these tests are bounded. No inherited-trace density for a singular functional is assumed.

## A minimizer exists, and its exact dual is an operator order floor

Let \(\mathcal K\) be the original compatible states satisfying (AS.4). It is nonempty. Let \(\mathcal K_e\) impose in addition annihilation of \(J_e\), and use the actual real constraint space
\[
\begin{gathered}
\mathcal L=\overline{\operatorname{span}_{\mathbb R}}^{\|\cdot\|}
\bigl\{uxu^*-x,\ x-E(x),\\
y:\ y\in M_{\rm sa},\ \tau(y)=0;\quad
z:\ z\in(J_e)_{\rm sa}\bigr\},\\
x\in B_{\rm sa},\quad u\in\mathcal U(M).
\end{gathered}
\tag{AS.6}
\]
This is the same actual space as SC.14. Its annihilating states are exactly \(\mathcal K_e\): selfadjoint tests extend complex linearly, and unitary conjugation invariance is equivalent to \(M\)-centrality. For the latter equivalence, every bounded selfadjoint contraction is the real part of a unitary \(x+i(1-x^2)^{1/2}\); real and imaginary parts handle every element of \(M\).

**Theorem AS.1 — one-state variational dual.** Whenever \(\mathcal K_e\ne\varnothing\),
\[
\begin{gathered}
m_e=\min_{\sigma\in\mathcal K_e}\sigma(a)\geq0,\\
m_e=\sup\{\lambda\in\mathbb R:
a+L\geq\lambda1\text{ for some }L\in\mathcal L\}.
\end{gathered}
\tag{AS.7}
\]
Consequently one state in this face annihilates \(a\) exactly when there is no strictly positive operator order floor modulo the actual constraints.

**Proof of attainment.** The state space of the \(C^*\)-algebra \(B\) is weak-star compact in \(B^*\). Positivity and value one at the identity are closed conditions in the dual unit ball. Each centrality, compatibility, physical trace and ideal-annihilation requirement is a family of closed linear equalities. Thus \(\mathcal K_e\) is compact. Evaluation at the fixed bounded \(a\) is continuous and attains its minimum. No claim that the purely singular state set itself is weak-star closed is used.

**Proof of the dual equality.** Any displayed order inequality, evaluated on any \(\sigma\in\mathcal K_e\), gives \(\sigma(a)\geq\lambda\). This proves one direction.

For the converse, fix \(\lambda<m_e\) and work in the real Banach space \(B_{\rm sa}\). The convex cone \(B_++\mathcal L\) has nonempty interior, since \(1\) is an interior point of \(B_+\). If \(a-\lambda1\) lay outside that interior, real Hahn–Banach separation of a point from an open convex set would give a nonzero continuous real functional \(F\) nonnegative on the cone and satisfying \(F(a-\lambda1)\leq0\). Here are the signs and normalization explicitly. Scaling elements of the open cone by arbitrary positive scalars forces its separating lower values to be nonnegative, and taking those scalars to zero forces the point's value to be nonpositive. Approximation by \(p+\varepsilon1\), \(p\geq0\), makes \(F\) positive on \(B_+\). Since \(\varepsilon1+L\) is in the interior for every \(L\in\mathcal L\), varying both signs and scalar multiples of \(L\) gives \(F(L)=0\).

Its complex linear extension is a nonzero positive bounded functional on \(B\). Positivity gives \(\|F\|=F(1)>0\): if \(F(1)=0\), the inequalities \(-\|x\|1\leq x\leq\|x\|1\) kill every selfadjoint value. Normalize by \(F(1)\). The resulting state lies in \(\mathcal K_e\) and has value at most \(\lambda\) on \(a\), contradicting \(\lambda<m_e\).

Therefore \(a-\lambda1\in B_++\mathcal L\). Rearranging its decomposition supplies \(a+L\geq\lambda1\). Every \(\lambda<m_e\) is admissible, proving (AS.7). If \(m_e>0\), approximating this \(L\) by a finite real combination of the actual generators, with norm error below \(\lambda/2\), gives a finite combination with a still positive floor \(\lambda/2\). No attainment of the supremum by an order certificate is asserted. \(\square\)

The general-state version is identical with the \(J_e\) generators omitted and \(\mathcal K\) replacing \(\mathcal K_e\). In the remaining alternative where no state of \(\mathcal K\) has a nonzero normal central component, JC and SC imply \(\mathcal K=\mathcal K_e\). If only one particular pure state has been exhibited, a positive \(m_e\) would exclude selection in this ideal-annihilating face, not exclude a possible normal-component route elsewhere in \(\mathcal K\).

The compactness and real separation inputs are the same standard functional-analytic prerequisites used in 49 and 82.7; their proofs are not given here.

## Exact bounded reweighting has finite actual tests

**Lemma AS.2 — the whole joint algebra is in the centralizer.** For \(h\in D\) and \(x\in B\),
\[
E(hx)=E(xh),\qquad \psi(hx)=\psi(xh).
\tag{AS.8}
\]

**Proof.** The whole \(D\), including its von Neumann closure, commutes with \(A\). Let \(T\) be any bounded trace-integrable element of \(A\). Trace adjointness, commutation of \(h,T\), and cyclicity with an integrable factor give
\[
\operatorname{Tr}(T E(hx))
=\operatorname{Tr}(Thx)
=\operatorname{Tr}(Txh)
=\operatorname{Tr}(T E(xh)).
\]
These finite trace tests separate bounded elements of \(A\). For example, a nonzero positive or negative spectral part of a bounded selfadjoint difference has a nonzero finite-trace subprojection, by semifiniteness, giving a nonzero pairing; real and imaginary parts handle a general difference. Thus the first identity holds. Apply \(\psi=\psi E\) to obtain the second.

This proof uses normal tracial expectation before applying the singular state. It does not infer centralizer membership by taking an ultraweak limit in a nonnormal functional. Physical \(M\) is also in the centralizer by (AS.4). The centralizer is a norm-closed star algebra: cyclicity for two elements successively proves cyclicity for their product, and taking adjoints proves star closure. The restriction of \(\psi\) to it is tracial. \(\square\)

For \(h\in D_+\) with \(c=\psi(h)>0\), define the state
\[
\psi_h(x)=c^{-1}\psi(h^{1/2}xh^{1/2})
=c^{-1}\psi(hx),\qquad
0\leq\psi_h\leq(\|h\|/c)\psi .
\tag{AS.9}
\]
Positivity and domination follow by applying the centralizer identity also to \(h^{1/2}\) and to \(\|h\|1-h\).

**Theorem AS.3 — exact constraint preservation.** This state is compatible and \(M\)-central if and only if
\[
\begin{gathered}
V_h:=\psi((h-E(h))^2)=0,\\
W_{h,i}:=\psi([h,a_i]^*[h,a_i])=0
\quad(1\leq i\leq t_0).
\end{gathered}
\tag{AS.10}
\]
When both conditions hold, \(\psi_h|_M=\tau\). In the pure branch its center restrictions stay purely singular and it kills \(J_e\).

**Compatibility.** Put \(h_0=E(h)\in Z(A)\). Bimodularity and compatibility give
\[
c(\psi_h(x)-\psi_h(E(x)))=\psi((h-h_0)x).
\]
The selfadjoint difference has zero such functional exactly when its squared value is zero: necessity follows by testing \(x=h-h_0\), and sufficiency is Cauchy–Schwarz.

For a full joint lift \(h=\widehat t\), its exact variance is
\[
V_h=\nu\bigl(Q(t^2)-(Q(t))^2\bigr).
\tag{AS.11}
\]
Indeed \(h\) commutes with \(h_0\), and \(\psi(hh_0)=\psi(h_0^2)\) by expectation adjointness. This also proves positivity of that variance without a trace density.

**Centrality.** Original centrality gives
\[
c(\psi_h(mx)-\psi_h(xm))=\psi([h,m]x).
\]
All commutators here are in the centralizer. Thus their two quadratic norms agree. Necessity follows by taking \(m=a_i\) and testing against the adjoint commutator. Conversely (AS.10) and Cauchy–Schwarz kill \(\psi([h,a_i]x)\) for every \(x\). Since \(h\) commutes with \(N\), expansion (AS.2) gives
\([h,m]=\sum_i[h,a_i]E_N(a_i^*m)\), proving centrality for every \(m\in M\).

**Physical trace and the singular branch.** Even before \(M\)-centrality is known, \(h\) commutes with \(N\), so \(\psi_h|_N\) is tracial. Domination in (AS.9) makes it normal; it is the normalized normal trace of the II₁ factor \(N\). Compatibility now gives
\(\psi_h(x)=\psi_h(E_N(x))=\tau(x)\) for \(x\in M\).
Domination prevents a new normal central minorant for any one bounded reweighting of a pure state, and preserves annihilation of \(J_e\). \(\square\)

For \(h\in Z(A)_+\), variance is automatically zero, but the finite commutator tests remain. For \(h\in Z(B)_+\), centrality is automatic, but variance remains. On the intersection \(Z(A)\cap Z(B)\), both are automatic. None of these statements declares a general low-cost smaller-center cut admissible.

## Approximate cuts can select one state

Exact commutator nullity is stronger than necessary. Here is a quantified selection argument that retains all actual constraints at the limiting state.

**Theorem AS.4 — finite-basis cut estimate.** Let \(q_0\in D\) be a projection with \(c=\psi(q_0)>0\). Set
\[
\begin{gathered}
\sigma_{q_0}(x)=\psi(q_0x)/c,\\
V=\psi((q_0-E(q_0))^2),\quad
W_i=\psi([q_0,a_i]^*[q_0,a_i]),\\
\eta=2V/c,\qquad
\delta=2\sum_i\|a_i\|\sqrt{W_i/c}.
\end{gathered}
\tag{AS.12}
\]
Then
\[
\begin{gathered}
\|\sigma_{q_0}-\sigma_{q_0}E\|=\eta,\\
\sup_{u\in\mathcal U(M)}
\|\sigma_{q_0}\operatorname{Ad}u-\sigma_{q_0}\|
\leq\delta,\\
\|\sigma_{q_0}|_M-\tau\|\leq\eta .
\end{gathered}
\tag{AS.13}
\]
For \(q_0\in Z(A)\), both compatibility and physical trace restriction are exact.

**Exact compatibility error.** Put \(q_1=E(q_0)\). It is a positive contraction in \(Z(A)\) commuting with \(q_0\). Since \(\psi(q_0q_1)=\psi(q_1^2)\) and \(\psi(q_1)=c\),
\[
\begin{gathered}
|q_0-q_1|=q_0(1-q_1)+(1-q_0)q_1,\\
\psi(|q_0-q_1|)=2(c-\psi(q_1^2))=2V .
\end{gathered}
\]
For a selfadjoint centralizer element \(z\), the functional \(x\mapsto\psi(zx)\) has norm \(\psi(|z|)\): its positive and negative parts give the upper bound, and evaluation at \(\operatorname{sign}(z)\) gives equality. The difference functional in AS.3 therefore has precisely the first norm in (AS.13).

**Centrality estimate.** In the GNS Hilbert space of \(\psi\), write \(x\Omega_\psi\) for its dense vectors. Right multiplication by a physical \(M\)-unitary is unitary, since that unitary lies in the centralizer; left multiplication is unitary as well. Conjugation therefore implements \(\operatorname{Ad}u\) and fixes \(\Omega_\psi\). The state \(\sigma_{q_0}\) is the vector state of \(q_0\Omega_\psi/\sqrt c\). Its conjugate is the vector state of \(u^*q_0u\Omega_\psi/\sqrt c\). Both vectors are unit vectors, so
\[
\|\sigma_{q_0}\operatorname{Ad}u-\sigma_{q_0}\|
\leq 2\|[q_0,u]\|_{2,\psi}/\sqrt c .
\]
Expand \(u=\sum_i a_i n_i\), where \(n_i=E_N(a_i^*u)\) and \(\|n_i\|\leq\|a_i\|\). Since \(q_0\) commutes with \(N\),
\([q_0,u]=\sum_i[q_0,a_i]n_i\).
Traciality on the centralizer gives
\(\|[q_0,a_i]n_i\|_{2,\psi}\leq\|n_i\|\sqrt{W_i}\).
The triangle inequality proves the second estimate uniformly over all physical unitaries. No enumeration of those unitaries is used.

**Physical trace estimate.** The state \(\sigma_{q_0}|_N\) is the normalized normal trace, by the domination and \(N\)-centrality argument of AS.3. For \(x\in M\),
\(\sigma_{q_0}(E(x))=\sigma_{q_0}(E_N(x))=\tau(x)\).
The first norm bound gives the last estimate. If \(q_0\in Z(A)\), \(E(q_0)=q_0\), so \(\eta=0\). \(\square\)

**Corollary AS.5 — an actual one-state selection route.** Suppose, for a single available compatible state \(\psi\), there are projections \(q_j\in D\), positive masses \(c_j=\psi(q_j)\), and positive numbers \(\varepsilon_j\to0\), such that
\[
\begin{gathered}
q_j\leq1_{[0,\varepsilon_j]}(a),\\
V_j/c_j\longrightarrow0,\qquad
\sum_i\|a_i\|\sqrt{W_{j,i}/c_j}\longrightarrow0 .
\end{gathered}
\tag{AS.14}
\]
Then the actual \(B\) has a compatible \(M\)-central state \(\sigma\) with \(\sigma(a)=0\). If the starting state kills \(J_e\), the selected state does too.

**Proof.** The normalized states of AS.4 obey every linear constraint with errors tending to zero, and have cost at most \(\varepsilon_j\), because \(q_j,a\in D\) commute. Weak-star compactness provides a convergent subnet with a state limit. Equations (AS.13) pass all bounded compatibility and centrality tests to that limit, and preserve physical trace restriction. Evaluation at the fixed bounded \(a\) gives zero. Domination by \(c_j^{-1}\psi\), separately for each \(j\), makes each state vanish on \(J_e\), so their limit does too.

No limit of the unnormalized singular functionals, no pairing with a strong approximation, and no assertion that a singular band is weak-star closed is needed. The limiting state may acquire a normal component; it still satisfies the required exact constraints and zero cost. \(\square\)

The especially concrete choice \(q_j=1_{[0,\varepsilon_j]}(a)\in Z(A)\) has \(V_j=0\). What remains is positive mass and the finite relative quadratic commutator bounds. General amenability has not proved those two properties. This route is for one state and selected cuts, rather than all-state cost annihilation.

At a minimizer \(\sigma\in\mathcal K_e\), every selfadjoint \(k\in D\) passing the two null tests of AS.3 satisfies the exact first-variation equation
\[
\sigma(ka)=m_e\,\sigma(k).
\tag{AS.15}
\]
Indeed \(1\pm tk\), for sufficiently small \(t>0\), are positive admissible weights with positive mass. Applying minimality to both normalized reweightings gives both signs of the displayed equality. This establishes stationarity only in constraint-preserving directions; it does not force \(m_e=0\).

## Making a singular state normal changes the larger expectation

One might try to normalize a singular state by passing to its abelian GNS representation and then apply the normal fixed-point theorem. The precise maps show why that alone does not supply the original cost.

**Proposition AS.6 — exact GNS expectation correction.** Let \(\mathscr D=\pi_\alpha(D_0)''\), with its faithful normal vector trace still denoted \(\alpha\), and let \(\mathscr U=\pi_\alpha(U)''\), \(\mathscr V=\pi_\alpha(V)''\). Original bounded functions and maps below denote their images in this completion. Then \(\gamma=\theta\alpha\) is an equivalent faithful normal trace. The original \(Q\) extends as the \(\alpha\)-preserving expectation onto \(\mathscr U\), and the original \(P\) extends as the \(\gamma\)-preserving expectation onto \(\mathscr V\). The \(\alpha\)-preserving larger expectation is
\[
\begin{gathered}
P_\alpha(t)=P(\theta^{-1}t),\qquad P(\theta^{-1})=1,\\
Q(\ell)=P_\alpha(\ell)=1,\qquad
P_\alpha(\ell t)=P(wt),\\
\alpha(P(\log\theta)-P_\alpha(\log\theta))
=\nu(b_{\log}).
\end{gathered}
\tag{AS.16}
\]
Neither \(P_\alpha=P\), \(P_\alpha(w)=1\), nor the original \(P(\ell)=1\) is inferred.

**Proof of the representation and extension.** The abelian GNS vector is cyclic and separating for \(\mathscr D\), because the algebra is abelian and the vector is cyclic. Its normal vector trace is therefore faithful. The ratio bounds in (AS.3)–(AS.5) give \(H^{-1}\alpha\leq\gamma\leq H\alpha\), so \(\gamma\) is an equivalent faithful normal trace in this new representation. This is not a density relative to the inherited trace on the original \(D_0\).

The identities \(\alpha Q=\alpha\), \(\gamma P=\gamma\), and bimodularity of the original expectations give their tracial pairings against \(U\) and \(V\), respectively. Their GNS null ideals are respected. More explicitly, Schwarz gives
\(\alpha(|Qt|^2)\leq\alpha(|t|^2)\).
Since \(\alpha=\gamma\) on \(V\), it also gives
\(\alpha(|Pt|^2)=\gamma(|Pt|^2)\leq\gamma(|t|^2)\leq H\alpha(|t|^2)\).
Thus both maps descend and are bounded on the tracial Hilbert space. The finite-trace expectation construction identifies them with the normal expectations onto \(\mathscr U,\mathscr V\), using their respective faithful traces. Agreement on the dense original algebra follows from the tracial pairings; bounded Hilbert-space extension or bounded approximation passes to the closures. This uses the proved finite expectation construction, not a general singular-state modular theorem.

**The new larger map.** For \(v\in\mathscr V\), equality of \(\alpha,\gamma\) on that algebra gives
\[
\gamma(vP(\theta^{-1}))
=\gamma(v\theta^{-1})
=\alpha(v)=\gamma(v).
\]
Faithfulness makes \(P(\theta^{-1})=1\). Therefore \(P_\alpha\) is positive, unital, \(\mathscr V\)-bimodular and fixes \(\mathscr V\). Also
\(\alpha(P_\alpha t)=\gamma(P_\alpha t)=\gamma(\theta^{-1}t)=\alpha(t)\).
It is the normal \(\alpha\)-preserving expectation. Finally \(\ell/\theta=w\), giving \(P_\alpha(\ell)=P(w)=1\) and the transfer formula in (AS.16). Since \(P_\alpha\) preserves \(\alpha\), the last equality is exactly (AS.5). \(\square\)

In this new finite probability representation, the correctly normalized weight is \(\ell\) with maps \(Q,P_\alpha\). Applying the existing normal fixed-point argument to these maps has the trivial fixed density one. It does not identify the original \(P\) with \(P_\alpha\) or identify \(w\) with \(\ell\). The original state has zero cost precisely when \(w=\ell\) in this GNS representation, equivalently when the last scalar test in (AS.16) is zero. Positivity of that test is already known; the required equality remains unproved.

## Exact remaining obligation and source comparison

The new completed statements are the minimizer/order-floor dual, the finite actual reweighting tests, the quantified finite-basis cut selection, and the GNS expectation correction. General amenability proves nonemptiness of the constrained state space. It has not supplied low-cost positive-mass cuts with the required relative quadratic errors, excluded a positive dual order floor, or supplied the equality of the two larger-expectation values on the canonical logarithmic test.

This is an exact operator-level obstruction, not an abstract numerical Jones counterexample. The dual tests and cuts are elements of the actual \(B\), and the finite commutators use the actual common cup basis. The sufficient cut route does not replace the unrestricted goal or impose any universal-state norm-distance requirement.

Sorin Popa, *Classification of amenable subfactors of type II*, Acta Mathematica 172 (1994), [DOI10.1007/BF02392646](https://doi.org/10.1007/BF02392646), provides the original source context. Definitions 3.1.1–3.1.2, pages 203–204, and Proposition 3.2.2, page 205, give the actual compatibility and expectation conditions. Section 4.2 and Theorem 4.2.2, pages 211–214, give the original finite-projection and integer-rounding outcome. Those source definitions supply the compatible-state input; they add no central normality or zero-cost requirement. The [finite-partition reading](finite-residual-cells-and-canonical-overlap.md) retains the unrestricted full-partition statement and its conditional constructions.

Full common-support BF, near-one support, unrestricted exact full finite partition, common-stage alignment and generation, every original finite-pair/bicommutant comparison, represented/opposite canonical trace and model, arbitrary-depth reconstruction, source clause, note, exercise and prerequisite remain assigned. No admitted normal, finite-capacity, cut, index-four or special-factor result is reopened or counted as the general missing implication.

## Solved learner checks

**Exercise AS.1.** Suppose \(q_n\in D\) has positive state mass \(c_n\), is supported where \(a\leq1/n\), and satisfies \(V_n/c_n\leq1/n^2\) and \(W_{n,i}/c_n\leq1/n^2\) for every basis entry. Prove that a compatible zero-cost cluster state exists, and state exactly which errors are uniform over all physical unitaries. Does a nonseparable algebra prevent the conclusion?

**Solution.** AS.4 gives compatibility error at most \(2/n^2\), physical trace restriction error at most \(2/n^2\), and conjugation error at most \(2t_0\sqrt d/n\), uniformly over the whole \(\mathcal U(M)\). The selected state has cost at most \(1/n\). Compactness supplies a subnet on which all bounded evaluations converge; AS.5 gives all exact constraints and zero cost. The subnet need not be a convergent subsequence. No countable enumeration of \(M\), its unitaries or the Hilbert space is required. If \(q_n\in Z(A)\), the compatibility and physical trace errors are already zero.

**Exercise AS.2.** In AS.6, prove that equality \(P=P_\alpha\) on the whole new joint algebra would force zero original cost. Show that equality of just their \(\alpha\)-values on \(\log\theta\) already suffices. Explain why replacing the inherited trace by the GNS trace cannot silently preserve the original larger expectation.

**Solution.** If the maps coincide, then \(\gamma=\alpha P=\alpha P_\alpha=\alpha\). Since \(\gamma=\theta\alpha\) and \(\alpha\) is faithful in this representation, \(\theta=1\), so \(w=\ell\) there and the cost is zero. Equality of their two scalar values on \(\log\theta\) makes \(\nu(b_{\log})=0\) by (AS.16); SC's exact estimate makes \(\nu(b)=0\). That is weaker than equality of the whole maps. The original \(P\) preserves \(\gamma\), while the new trace-preserving map is \(P(\theta^{-1}\,\cdot)\). Only \(\ell\) has the proved larger marginal one for that new map. Assuming the same property for \(w\), or assuming original \(P(\ell)=1\), would insert an unproved assertion.

![Compatible-state minimization, finite preservation tests and the corrected GNS expectation](figures/compatible-hypertrace-state-selection-v3.svg)

Figure AS.1. The top panel distinguishes minimization over one compatible state from a universal annihilation assertion. The middle panels display the actual finite preservation tests and every projection-selection error constant. The lower panel records both trace-preserving larger expectations and their exact normalized weights. All residual hypotheses and original outcomes are retained. Human context: Popa, Definitions3.1.1–3.1.2 and Theorem4.2.2, cited above. [Editable figure source](figures/compatible-hypertrace-state-selection-v3.py). The layout is schematic and encodes no trace areas.

Original independently written programme text and SVG: public domain, CC0 1.0.
