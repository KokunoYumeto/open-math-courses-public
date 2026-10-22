# Classifying modular cyclic returns

*Mathematical exposition: GPT-6.1 Sol and GPT-6 Astra (OpenAI). Original programme expression: CC0. Cited works and separately licensed components retain their own terms.*

## Introduction

Central triviality and modular powers constructed automorphisms with prescribed module, asymptotic period, modular return time and corrected obstruction. We now prove that these data determine outer conjugacy. The proof records two commuting directions on a semifinite factor: the automorphism being classified and the trace contraction that builds the type III factor. One rank-one subgroup records their inner returns.

The classification input is the one-factor corollary of [Characteristic classification of semifinite actions](characteristic-classification-of-semifinite-actions.md#4-normal-reconstruction-and-the-one-point-criterion). Its proof uses the programme’s common-associator comparison, with the finite and semifinite approximation, central-sequence and tower foundations stated there. Section 1 spells out the one-point specialization. The classical theorem is due to Sutherland–Takesaki; Takesaki III, XVIII.1.12–1.13, treats the modular-return classification and its models. The proofs below organize the return data as a lattice character and then lift a genuine two-generator cocycle.

Read [Central triviality and modular powers](central-triviality-and-modular-powers.md), Sections 3–5; [Trace scaling on the hyperfinite semifinite factor](trace-scaling-on-the-hyperfinite-semifinite-factor.md), Theorem 4.2 and Proposition 5.1; and [Finite outer period and obstruction](finite-outer-period-and-obstruction.md). The finite models, generalized-trace normalization and centrally trivial converse retain their exact prerequisites. The classification below is conditional on these foundations and on the comparison theorem named in Section 1. Normality of the lift uses the standard-form and regular-representation proofs linked in Section 4.

Throughout, fix \(0<\lambda<1\) and put
\[
L=-\log\lambda,\qquad P=2\pi/L.
\tag{1.1}
\]
Use generalized-trace decompositions
\[
\begin{gathered}
M_i=N_i\rtimes_{\theta_i}\mathbb Z,\quad N_i=R_\infty,\\
U_i xU_i^*=\theta_i(x),\quad\tau_i\theta_i=\lambda\tau_i,\\
\phi_i=\tau_i E_i,\quad
\sigma_r^{\phi_i}(U_i)=e^{-iLr}U_i.
\end{gathered}
\tag{1.2}
\]
Each \(M_i\) is the hyperfinite type \(III_\lambda\) factor with separable predual. Its modular outer period is \(P\), whereas the period of its flow of weights is \(L\).

## 1. The precise comparison input

Let a countable discrete amenable group \(G\) act genuinely on a hyperfinite semifinite factor \(N\), by a homomorphism \(b:G\to\operatorname{Aut}(N)\). Its inner kernel is
\[
K_b=\{h\in G:b_h\in\operatorname{Inn}(N)\}.
\tag{1.3}
\]
Choose unitaries \(u_h\) implementing the inner action. For an abelian \(G\), the characteristic functions are defined by
\[
\begin{gathered}
u_hu_k=\mu(h,k)u_{h+k},\\
b_g(u_h)=\Lambda(g,h)u_h.
\end{gathered}
\tag{1.4}
\]
Both coefficients are scalar because \(N\) is a factor. Changing the implementers changes the pair by its characteristic coboundary; its class is the characteristic invariant. The primary source orders the variables of its first function as \((h,g)\), so its \(\lambda(h,g)\) is our \(\Lambda(g,h)\).

The trace multiplier is the positive homomorphism
\[
\tau b_g=\Delta_b(g)\tau.
\tag{1.5}
\]
Multiplying \(\tau\) by a positive constant does not change it.

<a id="one-point-comparison"></a>
**Proposition 1.1 (one-factor comparison).** In the abelian case above, under the stated programme foundations, for two such actions \(b^{(i)}\) on \(N_i=R_\infty\), equality of their inner kernels, characteristic classes and trace multipliers implies the existence of a normal isomorphism \(\pi:N_1\to N_2\) and unitaries \(w_g\in N_2\) satisfying
\[
\begin{gathered}
\pi b^{(1)}_g\pi^{-1}
 =\operatorname{Ad}(w_g)b^{(2)}_g,\\
w_{g+h}=w_g b^{(2)}_g(w_h).
\end{gathered}
\tag{1.6}
\]
The second equation is a genuine unitary cocycle identity, with no scalar defect.

*Proof from the programme comparison.* Identify the two traced factors with the common model of [Characteristic classification of semifinite actions](characteristic-classification-of-semifinite-actions.md#4-normal-reconstruction-and-the-one-point-criterion), Corollary 4.1. Multiplying either trace by a scalar does not change (1.5). Choose the base to be one point and its positive trace cochain to be one. The principal orbit relation is the diagonal, with its constant finite exhaustion; every group label is an isotropy arrow. Equality of the two characteristic classes supplies one scalar cochain on the countable inner subgroup, so both multiplication and transport phases can be made equal simultaneously.

Section 2 of that lesson gives the remaining hypotheses explicitly: central triviality equals innerness on \(R_\infty\), including at the fixed central-sequence ultrafilter, and every trace-preserving automorphism is approximately inner. Equal trace multipliers make \(b^{(1)}_g(b^{(2)}_g)^{-1}\) trace preserving. Thus the induced centralizer kernels are exactly the common inner subgroup, and the action differences are approximately inner. The [joint quotient comparison](joint-quotient-comparisons-with-a-common-associator.md#1-the-general-matched-phase-classification-component), Theorem 1.1 and Sections 2–7, applies with the common scalar associator retained. Its full-group reconstruction gives a genuine cocycle. Corollary 4.1 puts this conclusion in the orientation (1.6), with a trace-preserving normal comparison in the common model. Transporting back gives \(\pi\) and \(w\) on \(N_1,N_2\). This argument also includes an entirely inner action. \(\square\)

The classical statement is [Sutherland–Takesaki], Theorem 1.2, on the groupoid with one unit and arrows \(G\). It is countable, amenable, orbitally discrete and ergodic; its algebra is semifinite, injective and has separable predual. The trace cohomology class is the actual homomorphism (1.5), since a one-point positive coboundary is trivial. The isotropy comparison at the start of the source’s Section 4 is the group comparison used here. The programme proof has the finite/semifinite foundations of Corollary 4.1; neither the source citation nor this one-point specialization removes those hypotheses.

We will compute representatives of the characteristic pairs that agree exactly. Consequently no unresolved characteristic cohomology calculation enters our application of (1.6).

## 2. Finding the inner-return subgroup

Normalize an automorphism \(\alpha\) of \(M\) by an inner perturbation, using the generalized-trace comparison and exact cohomology established earlier. Write
\[
\begin{gathered}
\phi\alpha=a\phi,\quad a=e^{-s},\quad0\le s<L,\\
\alpha(U)=U,\quad\beta=\alpha|_N,\\
\beta\theta=\theta\beta,\quad\tau\beta=a\tau.
\end{gathered}
\tag{2.1}
\]
The additive module coordinate is \([s]\in\mathbb R/L\mathbb Z\), with the convention of [the module-circle lesson](central-sequences-and-the-module-circle.md#module-and-dual-flow). The representative \(s\in[0,L)\) makes \(a\) unique. For the negative dual flow \(\vartheta_r\), the canonical core extension acts on the centre as \(\vartheta_{-s}\); the logarithmic coordinate and the dual-flow time consequently have opposite signs. All formulas below use \(a=e^{-s}\).

Put \(p=p_a(\alpha)\). Thus \(p>0\) is the least positive centrally trivial power, and \(p=0\) means there is no such power. The centrally trivial converse from the preceding lesson gives, when \(p>0\),
\[
\begin{gathered}
\alpha^p=\operatorname{Ad}(u)\sigma_t^\phi,
\quad0\le t<P,\\
a^p=\lambda^q,\quad ps=qL,\quad0\le q<p,\\
u=vU^q,\quad v\in\mathcal U(N).
\end{gathered}
\tag{2.2}
\]
Here \([t]\) is the modular return time. The integer \(q\) follows from the module of \(\alpha^p\); the homogeneous form of \(u\) follows from its modular eigenvalue, proved in that lesson.

Let \(\alpha(u)=\gamma u\). The corrected obstruction is
\[
\delta=\gamma a^{-it},\qquad\delta^p=1.
\tag{2.3}
\]
The convention \(0\le t<P\) is part of this definition. In particular, the raw phase \(\gamma\) need not be a \(p\)-th root of unity.

Restricting (2.2) to \(N\), and applying it to \(U\), gives
\[
\begin{gathered}
\beta^p=\operatorname{Ad}(v)\theta^q,\\
\theta(v)=cv,\quad c=e^{-iLt},\\
\beta(v)=\gamma v,\quad\gamma=\delta e^{-ist}.
\end{gathered}
\tag{2.4}
\]
For example, \(\alpha^p(U)=U\) says \(\operatorname{Ad}(v)(U)=e^{iLt}U\). Since \(vUv^*=c^{-1}U\), this has exactly the sign displayed in (2.4).

Consider the genuine action
\[
b_{(n,m)}=\beta^n\theta^m
\quad\bigl((n,m)\in\mathbb Z^2\bigr).
\tag{2.5}
\]

**Lemma 2.1.** Its inner kernel is
\[
K_b=
\begin{cases}
\mathbb Z(p,-q),&p>0,\\
\{(0,0)\},&p=0.
\end{cases}
\tag{2.6}
\]

*Proof.* Suppose \(b_{(n,m)}=\operatorname{Ad}(z)\), with \(z\in\mathcal U(N)\). Since this action commutes with \(\theta\), factoriality gives \(\theta(z)=\zeta z\) for some \(\zeta\in\mathbb T\). Also
\[
\beta^n=\operatorname{Ad}(z)\theta^{-m}.
\tag{2.7}
\]
Choose \(r\) with \(e^{-iLr}=\zeta\). On \(N\), the automorphisms \(\alpha^n\) and \(\operatorname{Ad}(zU^{-m})\sigma_r^\phi\) agree by (2.7). On \(U\), the inner factor contributes \(\zeta^{-1}\) and the modular factor contributes \(\zeta\). Both therefore fix \(U\). Normality and generation yield
\[
\alpha^n=\operatorname{Ad}(zU^{-m})\sigma_r^\phi.
\tag{2.8}
\]
It is centrally trivial. If \(p>0\), the subgroup of centrally trivial powers is \(p\mathbb Z\), so \(n=kp\). Taking trace multipliers of the original inner relation gives
\[
1=a^n\lambda^m=\lambda^{kq+m}.
\tag{2.9}
\]
Thus \(m=-kq\). Conversely, (2.4) gives \(b_{(p,-q)}=\operatorname{Ad}(v)\), so all its integer multiples are inner.

When \(p=0\), (2.8) forces \(n=0\). The trace relation then forces \(m=0\). This proves both cases. \(\square\)

The trace multiplier alone does not determine the inner kernel. If \(g=\gcd(p,q)\), its kernel is the larger primitive subgroup generated by \((p/g,-q/g)\). The index of the inner-return subgroup in that trace kernel is \(g\).

## 3. The characteristic invariant in coordinates

Suppose \(p>0\), and put \(h_0=(p,-q)\). Choose the coherent implementers
\[
u_{kh_0}=v^k\quad(k\in\mathbb Z).
\tag{3.1}
\]
They immediately give \(\mu=1\). For \(g=(n,m)\), (2.4) gives
\[
\begin{gathered}
\Lambda(g,kh_0)=\gamma^{nk}c^{mk},\\
\Delta_b(n,m)=a^n\lambda^m.
\end{gathered}
\tag{3.2}
\]
The necessary compatibility on the inner kernel is
\[
\gamma^p c^{-q}
 =\delta^p e^{-ipst}e^{iqLt}=1.
\tag{3.3}
\]
It also follows directly because \(b_{h_0}=\operatorname{Ad}(v)\) fixes \(v\). This explains how the raw phase twist enters the characteristic invariant.

Replacing \(v\) by a scalar multiple does not change (3.2). More generally, replacing \(u_{kh_0}\) by \(\eta_kv^k\), with \(\eta_k\in\mathbb T\), leaves \(\Lambda\) unchanged and gives
\[
\mu(kh_0,lh_0)=\eta_k\eta_l\eta_{k+l}^{-1}.
\tag{3.4}
\]
It is the explicit coboundary removed by (3.1).

Consequently two normalized automorphisms with the same
\[
\bigl(p,\delta,[t],[s]\bigr),\qquad p>0,
\tag{3.5}
\]
have the same \(q,a,\gamma,c\), the same inner kernel, and exactly the same representatives (3.2) of their characteristic and trace invariants. When \(p=0\), the inner kernel is trivial, so its characteristic invariant is trivial. Only the trace multiplier, hence the module \([s]\), remains for this comparison.

**Example 3.1.** Take \(p=3\), \(q=1\), \(s=L/3\), \(t=P/2\) and \(\delta=e^{2\pi i/3}\). Then
\[
\begin{gathered}
h_0=(3,-1),\quad c=-1,\quad\gamma=e^{i\pi/3},\\
\Lambda((n,m),h_0)=e^{i\pi n/3}(-1)^m,\\
\gamma^3c^{-1}=(-1)(-1)=1.
\end{gathered}
\tag{3.6}
\]
The raw phase has order six. Its corrected obstruction has order three. Both characteristic factors are needed to make the inner-return relation have phase one.

<a id="return-characters"></a>
**Lemma 3.2 (characters of the return quotient).** Fix \(p>0\), \(0\le q<p\), \(s=qL/p\) and \(K=\mathbb Z(p,-q)\). The characters of \(\mathbb Z^2/K\) are precisely
\[
 \chi(n,m)=\gamma^n c^m,
 \qquad \gamma^pc^{-q}=1.
 \tag{3.7}
\]
Each pair has a unique parametrization
\[
 \begin{gathered}
 c=e^{-iLt},\quad 0\le t<P,\\
 \gamma=\delta e^{-ist},\quad \delta^p=1.
 \end{gathered}
 \tag{3.8}
\]

*Proof.* A character of \(\mathbb Z^2\) is determined by its values \(\gamma,c\) on the two coordinate generators. It descends through the quotient exactly when it is one on its relation \((p,-q)\), which is (3.7). The half-open interval \([0,P)\) parametrizes \(c\) uniquely. Put \(\delta=\gamma e^{ist}\). Then
\[
 \delta^p=\gamma^p e^{ipst}
          =c^q e^{iqLt}=1.
 \tag{3.9}
\]
Conversely these equations give (3.7). Thus (3.8) is a bijective coordinate convention. It need not be a continuous product coordinate across the endpoint of the half-open interval. Exercise 6.7 computes its transition there. \(\square\)

This describes exactly the phase in (3.2): \(\Lambda(g,kh_0)=\chi(g)^k\). The finite component of the quotient itself has order \(\gcd(p,q)\), as the integer-basis proof in Exercise 6.6 shows. For a fixed \(c\), equation (3.7) instead has \(p\) possible values of \(\gamma\). These statements concern different projections of the same character group.

## 4. Lifting a genuine two-generator cocycle

Apply (1.6) to the actions (2.5) on \(N_1,N_2\). Write
\[
A=w_{(1,0)},\qquad B=w_{(0,1)}.
\tag{4.1}
\]
Computing \(w_{(1,1)}\) in the two orders gives
\[
A\beta_2(B)=B\theta_2(A).
\tag{4.2}
\]
This equality is the coherence needed to lift both directions together.

**Lemma 4.1.** There is a normal isomorphism \(\Pi:M_1\to M_2\) determined by
\[
\Pi(x)=\pi(x)\ (x\in N_1),\qquad\Pi(U_1)=BU_2.
\tag{4.3}
\]
It satisfies
\[
\Pi\alpha_1\Pi^{-1}=\operatorname{Ad}(A)\alpha_2.
\tag{4.4}
\]

*Proof.* The second generator of (1.6) gives
\[
\pi\theta_1\pi^{-1}=\operatorname{Ad}(B)\theta_2,
\tag{4.5}
\]
so (4.3) preserves covariance. We verify normality with the regular representations, rather than relying on covariance for the von Neumann closure.

Represent \(N_i\) in standard form on \(H_i\), and let \(S:H_1\to H_2\) be the unitary implementing \(\pi\). On \(\ell^2(\mathbb Z,H_i)\), the regular crossed product is generated by
\[
\begin{gathered}
(\iota_i(x)\xi)_k=\theta_i^{-k}(x)\xi_k,\\
(U_i\xi)_k=\xi_{k-1}.
\end{gathered}
\tag{4.6}
\]
The spatial implementation of a normal isomorphism is MC-1. The normal independence of the regular realization is NR-4, specialized to the discrete group of integers. Their natural-cone and bounded-density foundations remain in force.

Set \(c_j=w_{(0,j)}\). Define a unitary \(T\) between the regular Hilbert spaces by
\[
(T\xi)_k=c_{-k}^*S\xi_k.
\tag{4.7}
\]
Each coordinate is unitary. From (1.6),
\[
\pi\theta_1^{-k}(x)
 =c_{-k}\theta_2^{-k}(\pi(x))c_{-k}^*.
\tag{4.8}
\]
Therefore \(T\iota_1(x)T^*=\iota_2(\pi(x))\). The cocycle identity also gives
\[
c_{1-k}=c_{-k}\theta_2^{-k}(B).
\tag{4.9}
\]
Using this in the shift calculation yields
\[
TU_1T^*=\iota_2(B)U_2.
\tag{4.10}
\]
Thus conjugation by \(T\) supplies the normal map (4.3). Its range contains \(N_2\) and \(U_2=B^*\Pi(U_1)\), so it is onto. The inverse is conjugation by \(T^*\), where \((T^*\eta)_k=S^*c_{-k}\eta_k\), and has the generator formulas
\[
 \begin{gathered}
 \Pi^{-1}(y)=\pi^{-1}(y)\quad(y\in N_2),\\
 \Pi^{-1}(U_2)=\pi^{-1}(B^*)U_1.
 \end{gathered}
 \tag{4.10a}
\]
Both maps preserve bounded increasing positive suprema because they are spatial conjugations. This verifies normality in both directions on the complete generated algebras.

On \(N_2\), (4.4) is the first generator of (1.6). It remains to check the generator \(\Pi(U_1)=BU_2\). The left side of (4.4) fixes it, because \(\alpha_1(U_1)=U_1\). The right side sends it to
\[
\begin{aligned}
A\alpha_2(BU_2)A^*
 &=A\beta_2(B)\theta_2(A^*)U_2\\
 &=BU_2,
\end{aligned}
\tag{4.11}
\]
by (4.2). Equality on the generators proves (4.4). \(\square\)

The negative index in (4.7) follows from the regular representation (4.6). The order of the three unitary factors in (4.11) follows from moving \(A^*\) past \(U_2\). These two details make the lift exact.

## 5. The classification theorem and its realizations

Two automorphisms are outer conjugate if some normal isomorphism conjugates one to an inner perturbation of the other.

**Theorem 5.1.** Under the stated prerequisites, outer-conjugacy classes of automorphisms of \(R_\lambda\) are classified as follows.

| Asymptotic period | Complete data | Compatibility |
| --- | --- | --- |
| \(p>0\) | \((p,\delta,[t],[s])\) | \(\delta^p=1\), \(p[s]=0\) |
| \(p=0\) | \([s]\in\mathbb R/L\mathbb Z\) | none |

The modular return time lies in \(\mathbb R/P\mathbb Z\). In the finite row, \(\delta\) is defined using its unique representative \(t\in[0,P)\) as in (2.3). Every listed compatible datum occurs.

*Proof of completeness.* The asymptotic period and module are invariant under inner perturbation and conjugacy. Intrinsic modular outer classes are independent of the chosen weight and central in the outer automorphism group. Therefore \([t]\), and then the ordinary obstruction of the untwisted finite-order outer class, are invariant as proved in the preceding lesson. This proves necessity, including the fixed-representative convention for \(\delta\).

The corrected obstruction can be seen directly in the normalized model. Since \(\phi\alpha=a\phi\), the automorphism \(\alpha\) commutes with \(\sigma^\phi\). Put
\[
 \rho=\alpha\sigma_{-t/p}^\phi.
 \tag{5.0a}
\]
The modular eigenvalue of \(u\), proved in the preceding lesson, gives
\[
 \begin{gathered}
 \rho^p=\operatorname{Ad}(u),\\
 \rho(u)=\gamma a^{-it}u=\delta u.
 \end{gathered}
 \tag{5.0b}
\]
No smaller positive power of \(\rho\) is inner, since such a power would make the corresponding power of \(\alpha\) centrally trivial. Therefore \(\rho\) has outer period exactly \(p\), and \(\delta\) is its ordinary finite-period obstruction. The centrality and naturality of the intrinsic modular outer class make \([\rho]=[\alpha][\sigma_{-t/p}^\phi]\) invariant under the same outer conjugacies. The ordinary obstruction theorem consequently proves the claimed invariance, with the fixed representative \(t\).

For sufficiency, normalize two automorphisms with matching data by (2.1). If \(p>0\), Lemma 2.1 and (3.2) give matching inner kernels, characteristic classes and trace multipliers. If \(p=0\), the inner kernels and characteristic classes are trivial, and their modules again give matching trace multipliers. Apply Proposition 1.1 with \(G=\mathbb Z^2\), then Lemma 4.1. Restoring the initial inner perturbations preserves outer conjugacy. \(\square\)

*Proof of realization.* For \(p>0\), the preceding lesson has already constructed every compatible datum. More explicitly, choose its finite-factor model \(a_\delta\) on \(R\), with
\[
\begin{gathered}
p_a(a_\delta)=p_o(a_\delta)=p,\\
a_\delta^p=\operatorname{Ad}(v),\quad a_\delta(v)=\delta v.
\end{gathered}
\tag{5.1}
\]
Let \(b_r\) be the continuous trace-scaling flow on \(R_\infty\), so \(\tau b_r=e^{-r}\tau\). On \(N=R\bar\otimes R_\infty\), put
\[
\theta=\mathrm{id}\otimes b_L,\qquad
\beta=a_\delta\otimes b_s.
\tag{5.2}
\]
With \(ps=qL\), its canonical extension \(\widehat\beta\), fixing \(U\), has \(\widehat\beta^p=\operatorname{Ad}(vU^q)\). Set
\[
\alpha=\widehat\beta\,\sigma_{t/p}^{\phi}.
\tag{5.3}
\]
Its finite central-sequence witnesses, module, modular return and raw phase are checked in the preceding lesson. In particular its raw phase is \(\delta e^{-ist}\), as required by (2.3). The factor \(R\bar\otimes R_\lambda\) is identified with \(R_\lambda\) by the established factorial-centralizer spectrum and AFD uniqueness prerequisites.

For \(p=0\), choose the product automorphism \(a_\infty\) of \(R\) in Lemma 3.3 of [Comparing asymptotically aperiodic automorphisms](comparing-asymptotically-aperiodic-automorphisms.md), and replace \(a_\delta\) in (5.2) by \(a_\infty\). Let \(\alpha=\widehat\beta\). It has module \([s]\). For each nonzero integer \(n\), that lemma supplies ordinary centralizing tail unitaries \(x_j\in R\) with \(\|a_\infty^n(x_j)-x_j\|_2\to2\). Tensoring these unitaries with the identity gives central sequences in \(R\bar\otimes R_\lambda\), by the product-predual density argument used in the preceding realization proof. Their displacement is still detected by the trace state tensored with a normal state on \(R_\lambda\), so the corresponding power of \(\alpha\) is not centrally trivial. Thus \(p_a(\alpha)=0\), for every \([s]\). \(\square\)

No finite-return phase is assigned in the \(p=0\) row. There is no positive return power from which to define one.

## 6. Exercises with solutions

**Exercise 6.1 (inner kernel versus trace kernel).** Suppose \(p=4\), \(q=2\). Compute both kernels from Section 2 and the quotient of the trace kernel by the inner kernel.

*Solution.* The trace equation is \(2n+4m=0\), so its kernel is \(\mathbb Z(2,-1)\). Lemma 2.1 gives the inner kernel \(\mathbb Z(4,-2)\). The former modulo the latter is \(\mathbb Z/2\mathbb Z\). In particular trace preservation of \(\beta^2\theta^{-1}\) does not prove that it is inner.

**Exercise 6.2 (a characteristic relation).** For Example 3.1, compute the values of \(\Lambda(\cdot,h_0)\) on the two coordinate generators, on \((2,-1)\), and on \(h_0\).

*Solution.* They are \(e^{i\pi/3}\), \(-1\), \(-e^{2\pi i/3}\), and \(1\), respectively. The last value uses both coordinate phases. Retaining only the raw phase would give \(\gamma^3=-1\), which fails the inner-implementer compatibility.

**Exercise 6.3 (explicit characteristic coboundary).** Let \(\eta_k=e^{i\vartheta k^2}\). Calculate (3.4) and verify its scalar cocycle identity on the inner kernel.

*Solution.* Direct subtraction of exponents gives
\[
\mu(kh_0,lh_0)=e^{-2i\vartheta kl}.
\tag{6.1}
\]
Both sides of \(\mu(k,l)\mu(k+l,j)=\mu(l,j)\mu(k,l+j)\) have exponent \(-2i\vartheta(kl+kj+lj)\). Replacing \(\eta_kv^k\) by \(v^k\) removes this coboundary. Scalars are fixed by every automorphism, so \(\Lambda\) is unchanged.

**Exercise 6.4 (why a scalar defect matters).** In the lift calculation, replace (4.2) by
\[
A\beta_2(B)=\kappa B\theta_2(A),\qquad\kappa\in\mathbb T.
\tag{6.2}
\]
What does \(\operatorname{Ad}(A)\alpha_2\) do to \(BU_2\)? Why do separate inner intertwiners for the two generators not suffice?

*Solution.* The calculation (4.11) now gives \(\kappa BU_2\), whereas \(\Pi\alpha_1\Pi^{-1}\) fixes \(BU_2\). Hence the desired equality on the crossing generator fails unless \(\kappa=1\). A concrete algebraic example uses Weyl unitaries \(A,B\) in \(M_d(\mathbb C)\) with \(AB=\kappa BA\), \(\kappa\ne1\). The inner actions \(\operatorname{Ad}(A)\) and \(\operatorname{Ad}(B)\) commute, and each has an inner intertwiner with the identity action. These two intertwiners have the scalar defect (6.2). They cannot be the generator values of a genuine cocycle for the identity \(\mathbb Z^2\)-action. This finite example checks the coherence issue; it is not a type III classification example.

**Exercise 6.5 (the regular shift).** Derive (4.10) directly on the \(k\)-th coordinate. Include the inverse of \(T\).

*Solution.* We have \((T^*\eta)_j=S^*c_{-j}\eta_j\). Thus
\[
\begin{aligned}
(TU_1T^*\eta)_k
 &=c_{-k}^*c_{1-k}\eta_{k-1}\\
 &=\theta_2^{-k}(B)\eta_{k-1},
\end{aligned}
\tag{6.3}
\]
by (4.9). This is precisely \((\iota_2(B)U_2\eta)_k\). The cocycle index \(1-k\) comes from shifting the input coordinate from \(k\) to \(k-1\).

**Exercise 6.6 (a nonprimitive return).** Prove
\[
\begin{gathered}
\mathbb Z^2/\mathbb Z(p,-q)
 \cong\mathbb Z\oplus\mathbb Z/g\mathbb Z,\\
g=\gcd(p,q),
\end{gathered}
\tag{6.4}
\]
for \(p>0\), including \(q=0\). Explain the finite summand.

*Solution.* Write \(p=gp'\), \(q=gq'\), with \(\gcd(p',q')=1\). Choose integers \(r,t\) with \(p't+q'r=1\). The vectors \((p',-q')\) and \((r,t)\) have determinant one and form an integer basis of \(\mathbb Z^2\). In this basis the relation is \(g\) times the first vector, proving (6.4). When \(q=0\), one has \(g=p\), \(p'=1\), and the same construction applies. The finite summand is exactly the trace-kernel quotient in Exercise 6.1, with its general order \(g\).

**Exercise 6.7 (changing the real return representative).** Keep a normalized automorphism and its raw phase \(\gamma\) fixed, but replace \(t\) by \(t+Pj\). Determine the corrected phase, and decide when it is unchanged for every integer \(j\).

*Solution.* Since \(a=e^{-s}\) and \(s=qL/p\),
\[
\delta'=
\gamma a^{-i(t+Pj)}
 =\delta e^{2\pi iqj/p}.
\tag{6.5}
\]
It remains a \(p\)-th root of unity. It is unchanged for every \(j\) exactly when \(p\) divides \(q\). With \(0\le q<p\), this is \(q=0\), equivalently trivial module. The invariant convention in Theorem 5.1 fixes \(t\in[0,P)\), so a representative change is not silently treated as the same obstruction coordinate.

## References and proof scope

The lesson proves the inner-kernel calculation, the characteristic-coordinate specialization, the normal crossed-product lift, and the resulting conditional completeness and realization statements. Its prerequisite list retains generalized-trace normalization, exact trace-scaling cohomology, the centrally trivial converse, finite-factor models and the semifinite amenable-action comparison theorem.

[Sutherland–Takesaki]: https://doi.org/10.2977/PRIMS/1195178510

* C. E. Sutherland and M. Takesaki, “Actions of Discrete Amenable Groups and Groupoids on von Neumann Algebras,” *Publications of the Research Institute for Mathematical Sciences* **21** (1985), 1087–1120. [Publisher DOI](https://doi.org/10.2977/PRIMS/1195178510), [primary paper](https://ems.press/content/serial-article-files/42299). Theorem 1.2 (p.1092), the definitions in Section 1 and the isotropy comparison at the start of Section 4 (p.1107) are the classical sources for Proposition 1.1. The programme proof is the one-point specialization specified there.
* Y. Kawahigashi, C. E. Sutherland and M. Takesaki, “The structure of the automorphism group of an injective factor and the cocycle conjugacy of discrete abelian group actions,” *Acta Mathematica* **169** (1992), 105–130. [Publisher DOI](https://doi.org/10.1007/BF02392758). Lemma 18 underlies the centrally trivial converse used from the preceding lesson; Lemma 14 and Corollary 15 concern factor alignment.
* A. Connes, “Outer conjugacy classes of automorphisms of factors,” *Annales scientifiques de l'École Normale Supérieure* (4) **8** (1975), 383–419. [Primary publication](https://numdam.org/articles/10.24033/asens.1295/). The earlier finite-factor constructions and obstruction arguments retain their stated Connes prerequisites.

* M. Takesaki, *Theory of Operator Algebras III*, Springer, 2003, Definition XVIII.1.12 and Theorem XVIII.1.13, pp.310–313. [Publisher record](https://doi.org/10.1007/978-3-662-10453-8). Source for the modular-return classification and the finite-factor/trace-flow realization. The source normalizes \(\phi\circ\alpha^{-1}\), whereas (2.1) normalizes \(\phi\circ\alpha\); their positive scalars are reciprocals before the choice of representatives. The obstruction used here is the ordinary obstruction after modular untwisting, (5.0a)–(5.0b).
