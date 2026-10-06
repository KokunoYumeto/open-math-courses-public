# Finite pieces and invariant modular observations

A faithful normal state always provides a fixed normal observation for its own modular flow. An infinite weight need not do so. The useful question is whether enough finite observations remain fixed to detect every positive element. We will connect that question to a decomposition of the weight and to compactness of the flow on the predual.

Throughout, \(M\) is a von Neumann algebra and \(\varphi\) is a faithful normal semifinite weight on it. Put

\[
 \sigma_t=\sigma_t^\varphi,\qquad
 N=\{a\in M:\sigma_t(a)=a\text{ for every }t\in\mathbb R\}.
 \tag{SN.1}
\]

The algebra \(N\) is the centralizer. The predual has its Banach-space weak topology \(\sigma(M_*,M)\). Relative weak compactness means compactness of the closure in this topology. Neither separability nor existence of a faithful normal state on all of \(M\) is assumed.

For arbitrary index sets, sums of nonnegative scalars are suprema of finite subsums. Sums of orthogonal projections are strong sums. A family \(\mathcal I\) of invariant normal states will be called **sufficient** when

\[
 x\in M_+,\quad \rho(x)=0\ (\rho\in\mathcal I)
       \quad\Longrightarrow\quad x=0.
 \tag{SN.2}
\]

Equivalently, \(\bigvee_{\rho\in\mathcal I}s(\rho)=1\). Indeed, \(\rho(x)=0\) implies \(s(\rho)xs(\rho)=0\), since the state is faithful on its support corner. Thus \(x^{1/2}s(\rho)=0\). A join of these supports equal to one forces \(x=0\). Conversely, a nonzero projection orthogonal to all supports is undetected.

## The four descriptions

**Theorem.** The following assertions are equivalent.

1. There are \(\omega_i\in M_*^+\) whose support projections are pairwise orthogonal and

   \[
    \varphi(x)=\sum_{i\in I}\omega_i(x)\qquad(x\in M_+).
    \tag{SN.3}
   \]

   Such a weight is called **strictly semifinite**.
2. The restricted weight \(\varphi|_{N_+}\) is semifinite. Here semifiniteness means that its finite linear domain is ultraweakly dense in \(N\).
3. There is a sufficient family of normal states \(\rho\) satisfying \(\rho\circ\sigma_t=\rho\) for every real \(t\).
4. For every \(\omega\in M_*\), the set

   \[
    \mathcal O(\omega)=\{\omega\circ\sigma_t:t\in\mathbb R\}
    \tag{SN.4}
   \]

   is relatively weakly compact in \(M_*\).

The zero algebra is included: the empty projection and state families suffice, and every orbit is \(\{0\}\).

We use exact previously written proofs for the following inputs. Finite positive cutoffs characterize semifiniteness. The bounded-density sum and continuity results, with their projection and corner lemma, give, for \(a\in N_+\),

\[
 \varphi_a(x)=\varphi(a^{1/2}xa^{1/2}),\quad
 a\le b\Longrightarrow\varphi_a\le\varphi_b,
 \quad \varphi_{a+b}=\varphi_a+\varphi_b.
 \tag{SN.5}
\]

They also give \(\varphi_{a_j}(x)\uparrow\varphi_a(x)\) for a bounded increasing net \(a_j\uparrow a\) in \(N_+\), including infinite values. A projection \(p\) whose sign unitary \(2p-1\) preserves the weight belongs to \(N\). This is the projection lemma based on the centralizer criterion.

The full invariant-density theorem applies to nonfaithful normal semifinite weights: an invariant such weight is uniquely \(\varphi_h\), for a positive self-adjoint \(h\) affiliated with \(N\), and \(s(h)\) is its support. The form-order criterion and affiliated-density construction include form domains and possible kernels.

The normal GNS representation and its coefficient functionals are supplied by The GNS construction for an arbitrary weight and Normality is a net argument. The functional-analytic inputs are predual duality and its norm-closed embedding, positive-functional decomposition and Cauchy–Schwarz, supports and support-corner reconstruction (Removing null directions without subtracting infinities, The faithful semifinite support corner), weak compactness of normal-functional order intervals, and dual-ball compactness. For the final implication we use the exact decreasing-projection compactness criterion at Conventions and the exact compactness input and the complete affine isometric group fixed-point proof at The complete existing programme fixed-point proof. This theorem does not give a new proof of those general results.

Further exact inputs are the faithful finite-state GNS specialization, normal faithful image theorem, and bicommutant theorem. The spectral operations use bounded Borel calculus, self-adjoint recovery, power domains, affiliated membership, and spectral cutoffs. Invariance of the reference weight on the entire positive cone is part of the modular fundamental theorem. The norm-density separation argument uses the Hahn–Banach annihilator criterion for a norm-closed linear subspace, at exact contract OA-MOD-OPEN-CONVEX-HB-NORM.

## Build the finite pieces in the centralizer

Introduce the intermediate condition

\[
 \begin{gathered}
 e_i\in N\text{ are nonzero pairwise orthogonal projections},\\
 \varphi(e_i)<\infty,\qquad \sum_{i\in I}e_i=1.
 \end{gathered}
 \tag{SN.6}
\]

We first prove that it is equivalent to assertions 1 and 2.

Suppose (SN.3) holds and discard zero functionals. Let \(e_i=s(\omega_i)\), and put \(e=\sum_i e_i\). Every \(\omega_i\) vanishes at \(1-e\), so faithfulness of the weight gives \(e=1\). Also

\[
 \varphi(e_i)=\omega_i(e_i)=\omega_i(1)<\infty.
 \tag{SN.7}
\]

For the sign unitary \(u_i=2e_i-1\), its restriction to each support \(e_j\) is either \(1\) or \(-1\). Therefore \(\omega_j(u_i x u_i)=\omega_j(x)\) for \(x\ge0\). Summing shows that \(u_i\) preserves \(\varphi\) on the entire positive cone. The projection lemma puts \(e_i\) in \(N\). This proves (SN.6), including the fixedness which an arbitrary orthogonal decomposition would not automatically supply.

Conversely assume (SN.6). Define

\[
 \omega_i(x)=\varphi(e_i x e_i)\qquad(x\in M_+).
 \tag{SN.8}
\]

This is a bounded positive functional: \(\omega_i(x)\le\|x\|\varphi(e_i)\). It is normal as the GNS coefficient
\(\langle\pi_\varphi(x)\Lambda_\varphi(e_i),\Lambda_\varphi(e_i)\rangle\) of the normal weight GNS representation. Faithfulness of \(\varphi\) makes its restriction to \(e_iMe_i\) faithful, so its support is exactly \(e_i\).

For finite \(F\subset I\), set \(e_F=\sum_{i\in F}e_i\). The bounded-density identities (SN.5) give

\[
 \varphi_{e_F}(x)=\sum_{i\in F}\omega_i(x),
 \qquad \varphi_{e_F}(x)\uparrow\varphi_1(x)=\varphi(x).
 \tag{SN.9}
\]

Thus (SN.3) holds on every positive element, also when its weight is infinite. No convergence of the nonmonotone operators \(e_Fxe_F\) is being substituted for this monotone convergence of weight values.

Condition (SN.6) immediately implies assertion 2: \(e_F\in N_+\), \(\varphi(e_F)<\infty\), and \(e_F\uparrow1\). The finite-cutoff characterization applies to \(\varphi|_{N_+}\).

For the converse, assume assertion 2. Its finite-cutoff theorem gives positive contractions \(a_\alpha\in N\) with finite weight and \(a_\alpha\uparrow1\). We claim that every nonzero projection \(q\in N\) contains a nonzero finite-weight projection in \(N\). Some

\[
 b=q a_\alpha q
 \tag{SN.10}
\]

is nonzero, since these positive operators increase strongly to \(q\). By (SN.5),
\(\varphi(b)=\varphi_q(a_\alpha)\le\varphi(a_\alpha)<\infty\).
Choose \(\delta>0\) so that \(r=1_{[\delta,\infty)}(b)\ne0\). Spectral calculus gives \(r\le q\) and

\[
 r\le\delta^{-1}b,
 \qquad \varphi(r)\le\delta^{-1}\varphi(b)<\infty.
 \tag{SN.11}
\]

All spectral projections of \(b\in N\) belong to \(N\).

Now choose a maximal orthogonal family of nonzero finite-weight projections in \(N\), using Zorn's lemma. Its strong sum \(p\) belongs to \(N\). If \(1-p\ne0\), the claim supplies a further member orthogonal to the family, contradicting maximality. Hence \(p=1\), proving (SN.6). This argument does not assume that all finite-weight projections of a general weight form a directed set.

## Fixed states detect precisely the same finite pieces

Under (SN.6), each functional (SN.8) is invariant:

\[
 \omega_i(\sigma_t(x))
 =\varphi(\sigma_t(e_i x e_i))=\omega_i(x).
 \tag{SN.12}
\]

Its normalization \(\rho_i=\omega_i/\varphi(e_i)\) is a normal state with support \(e_i\). The supports sum to one, so these states are sufficient. This proves assertion 2 implies assertion 3.

Assume now assertion 3. For each invariant normal state \(\rho\), the full invariant-density theorem supplies a positive self-adjoint operator \(h_\rho\), affiliated with \(N\), such that

\[
 \rho=\varphi_{h_\rho},\qquad s(h_\rho)=s(\rho).
 \tag{SN.13}
\]

A normal state is a normal semifinite weight; it need not be faithful on all of \(M\). The kernel clause in the theorem is therefore essential.

Let

\[
 q_{\rho,n}=1_{[1/n,n]}(h_\rho)\in N.
 \tag{SN.14}
\]

These projections increase to \(s(\rho)\). The spectral form inequality
\(h_\rho\ge n^{-1}q_{\rho,n}\), with the full domain of \(h_\rho^{1/2}\), and the density order theorem yield

\[
 n^{-1}\varphi(q_{\rho,n})
   =\varphi_{n^{-1}q_{\rho,n}}(1)
   \le\varphi_{h_\rho}(1)=1.
 \tag{SN.15}
\]

Thus \(\varphi(q_{\rho,n})\le n\). Sufficiency says that the join of all these finite-weight centralizer projections is one.

Take a maximal orthogonal family of finite-weight projections in \(N\), and suppose its complementary projection \(q\) is nonzero. Since the projections (SN.14) have join one, \(q q_{\rho,n}q\ne0\) for some \(\rho,n\). Its weight is at most \(\varphi(q_{\rho,n})\), again by (SN.5). Applying the spectral extraction (SN.11) inside \(qNq\) supplies a nonzero finite-weight projection orthogonal to the maximal family. This contradiction proves (SN.6). Therefore assertion 3 implies assertion 2.

## A fixed faithful state controls a corner's predual

We need a norm-density fact before considering compact orbits.

**Lemma.** If \(P\) is a von Neumann algebra with a faithful normal state \(\rho\), the complex linear span of

\[
 D_\rho=\{\nu\in P_*^+:\nu\le C\rho
                       \text{ for some finite }C\ge0\}
 \tag{SN.16}
\]

is norm dense in \(P_*\).

**Proof.** Let \((H,\pi,\Omega)\) be the normal GNS representation of \(\rho\). It is faithful and its image is a von Neumann algebra. Faithfulness of the state makes \(\Omega\) separating for \(\pi(P)\). It is consequently cyclic for \(\pi(P)'\): the projection onto \(\overline{\pi(P)'\Omega}\) belongs to \(\pi(P)\), fixes \(\Omega\), and must be one by separation.

For \(0\le T\le1\) in \(\pi(P)'\), define

\[
 \nu_T(a)=\langle\pi(a)T\Omega,\Omega\rangle
         =\langle\pi(a)T^{1/2}\Omega,T^{1/2}\Omega\rangle.
 \tag{SN.17}
\]

It is normal and \(0\le\nu_T\le\rho\). Suppose \(a\in P=(P_*)^*\) annihilates the linear span in the lemma. Then (SN.17) vanishes for every such \(T\), and hence for every \(T\in\pi(P)'\), since positive contractions span that algebra. For \(b',c'\in\pi(P)'\),

\[
 \langle\pi(a)b'\Omega,c'\Omega\rangle
 =\langle\pi(a)c'^*b'\Omega,\Omega\rangle=0.
 \tag{SN.18}
\]

Cyclicity of the commutant gives \(\pi(a)=0\), and faithfulness gives \(a=0\). Hahn–Banach separation of a proper norm-closed linear subspace now proves the asserted density. \(\square\)

If \(\rho\) is fixed by an automorphism group, the orbit of any \(\nu\le C\rho\) is contained in \([0,C\rho]\). That order interval is weakly compact. A finite linear combination of such functionals has its orbit in a finite sum of scalar multiples of these intervals. The latter set is weakly compact: it is the continuous image of a finite product of compact sets.

There is a second useful fact. Let \(T_t\) be linear isometries of \(M_*\). If \(\omega\) is a norm limit of functionals whose \(T_t\)-orbits are relatively weakly compact, its orbit is relatively weakly compact as well. Here is the argument, since a norm approximation alone is not a compactness proof.

View \(M_*\) as its norm-closed subspace in \(M^*=(M_*)^{**}\). The weak-star closure \(L\) in \(M^*\) of the bounded orbit of \(\omega\) is compact by Banach–Alaoglu. Fix \(f\in L\) and \(\varepsilon>0\). Choose \(\eta\) with relatively weakly compact orbit and \(\|\omega-\eta\|<\varepsilon\). There is a net \(t_\alpha\) for which \(T_{t_\alpha}\omega\to f\) weak-star. A subnet of \(T_{t_\alpha}\eta\) converges weakly to some \(g\in M_*\). The isometry bound passes to scalar evaluations and gives

\[
 |(f-g)(x)|\le\varepsilon\|x\|\qquad(x\in M).
 \tag{SN.19}
\]

Thus \(f\) is within \(\varepsilon\) in norm of \(M_*\). This holds for every \(\varepsilon\), so norm closedness puts \(f\) in \(M_*\). The topology on \(L\) is now exactly the weak topology of \(M_*\). Therefore \(L\) is the required weakly compact orbit closure.

## Pass from finite corners to every functional

Assume assertion 2 and choose (SN.6). For a nonempty finite \(F\subset I\), the corner \(P_F=e_FMe_F\) has the invariant faithful normal state

\[
 \rho_F(a)=\frac{\varphi(a)}{\varphi(e_F)}
       \qquad(a\in(P_F)_+).
 \tag{SN.20}
\]

Its invariance uses \(e_F\in N\) and invariance of \(\varphi\). The compression map \(C_F:M\to P_F\), \(C_F(x)=e_Fxe_F\), commutes with the modular flow. Precomposition with \(C_F\) embeds \((P_F)_*\) isometrically in \(M_*\). In particular, domination by \(C\rho_F\) lifts to domination by the invariant normal functional \(C(\rho_F\circ C_F)\).

The preceding lemma consequently gives relatively weakly compact orbits for a norm-dense subspace of the compressed functionals supported in \(e_F\).

These compressed spaces together are norm dense in all of \(M_*\). To check this directly, let \(\omega\in M_*^+\) and set \(\omega^F(x)=\omega(e_Fxe_F)\). For \(\|x\|\le1\), write

\[
 x-e_Fxe_F=(1-e_F)x+e_Fx(1-e_F).
 \tag{SN.21}
\]

Cauchy–Schwarz for \(\omega\) bounds each term's value by
\(\sqrt{\omega(1)\omega(1-e_F)}\). Hence

\[
 \|\omega-\omega^F\|
 \le2\sqrt{\omega(1)\omega(1-e_F)}\longrightarrow0.
 \tag{SN.22}
\]

Normality and \(e_F\uparrow1\) give the limit. Every complex normal functional is a linear combination of positive normal functionals, so the same norm-density conclusion holds for all of \(M_*\).

Finally the maps \(T_t\omega=\omega\circ\sigma_t\) are linear norm isometries of \(M_*\). Every \(\omega\) can first be approximated by a compression, then by a finite linear combination from (SN.16) in that corner. Its approximants have relatively weakly compact orbits. The closure argument (SN.19) now proves assertion 4 for \(\omega\). Thus assertion 2 implies assertion 4.

## A compact orbit cannot leave a fixed corner undetected

Assume assertion 4. Let

\[
 e=\bigvee\{s(\rho):\rho\text{ is an invariant normal state}\}.
 \tag{SN.23}
\]

Every support in this join is fixed: if \(\rho\circ\sigma_t=\rho\), transporting its least supporting projection by \(\sigma_t\) gives the same least projection. Therefore \(e\in N\).

Suppose \(q=1-e\ne0\). Choose a unit vector in \(qH\) in a faithful normal concrete representation of \(M\); its vector state \(\omega\) is normal and satisfies \(\omega(q)=1\), with support at most \(q\). Because \(q\) is fixed, every member of its orbit has value one at \(q\).

We require a compact **convex** set to apply the fixed-point theorem. Here its compactness follows from the exact predual criterion, without assuming a general convex-hull theorem. Let \(K=\overline{\mathcal O(\omega)}^{\,w}\), which is compact by assertion 4. It consists of positive normal states. For any decreasing projection sequence \(p_n\downarrow0\), the continuous functions

\[
 f_n(\eta)=\eta(p_n)\quad(\eta\in K)
 \tag{SN.24}
\]

decrease pointwise to zero. They do so uniformly: for any \(\varepsilon>0\), the increasing open sets \(\{\eta:f_n(\eta)<\varepsilon\}\) cover \(K\), and compactness supplies a finite subcover, which is contained in one such set. Thus

\[
 \sup_{\eta\in K}\eta(p_n)\longrightarrow0.
 \tag{SN.25}
\]

Put \(C=\overline{\operatorname{co}}^{\,w}\mathcal O(\omega)\), taking this closure in \(M_*\). Positivity, evaluation at one and evaluation at \(q\) persist under this closure. Consequently every member of \(C\) is a normal state with value one at \(q\), so \(C\) is bounded and nonempty. For each \(n\), the upper bound in (SN.25) also bounds every finite convex combination and every weak limit. The decreasing-projection compactness criterion at TE-01, precisely the programme theorem's implication \(3\) to \(1\), therefore makes \(C\) relatively weakly compact. It is weakly closed, so it is weakly compact.

The group \(T_t\eta=\eta\circ\sigma_t\) preserves \(C\). Each map is weakly continuous, since evaluation at \(x\) after applying it is evaluation at \(\sigma_t(x)\) before applying it. Each is an affine bijection preserving norm distances. The complete group fixed-point theorem at TE-14 gives \(\rho\in C\) with \(T_t\rho=\rho\) for every \(t\).

This is an invariant normal state and has support at most \(q\), because \(\rho(q)=\rho(1)=1\). Its definition in (SN.23) also puts its support under \(e\). Thus its support is zero, contradicting \(\rho(1)=1\). We conclude \(e=1\), which is assertion 3.

The implications proved above connect all four assertions. Their proofs cover the full positive cone, arbitrary support families, and every complex functional in the predual. \(\square\)

## Test the distinction between one state and a sufficient family

**Problem.** Let \(I\) be an uncountable set, let \(M=\ell^\infty(I)\), and define

\[
 \varphi(x)=\sum_{i\in I}x_i\qquad(x\in M_+).
 \tag{SN.26}
\]

Determine the four assertions above, and decide whether they produce a faithful normal state on \(M\).

**Solution.** The finite-coordinate projections \(e_F=1_F\) increase to one and have finite weight. Normality follows by interchanging the increasing supremum with the supremum of finite sums; faithfulness follows from positive-coordinate detection. This is a faithful normal semifinite trace, whose modular flow is the identity. Its centralizer is all of \(M\).

The coordinate functionals \(\delta_i(x)=x_i\) have pairwise orthogonal supports and their sum is the weight. They are invariant and sufficient. Every predual orbit is a singleton. Hence all four assertions hold.

A normal state nevertheless has at most countably many nonzero coordinate masses. Indeed, the masses \(\rho(e_i)\ge0\) have sum one by normality, and for each positive integer \(n\), at most finitely many are at least \(1/n\). Their union contains every positive mass. Since \(I\) is uncountable, some \(e_i\ne0\) has zero mass. Therefore the state is not faithful. A sufficient family of invariant states cannot be replaced by one faithful invariant state at this generality.

**Problem.** Suppose \(\varphi(1)<\infty\). Show directly how the finite pieces and invariant states can be chosen.

**Solution.** For a nonzero algebra, the single projection \(e_1=1\) satisfies (SN.6), and \(\varphi/\varphi(1)\) is a faithful invariant normal state. The theorem then gives weakly compact predual orbits. This special case does not justify the single-state reduction for an arbitrary infinite weight.

## Sources and mathematical credit

The finite-projection characterization is discussed and proved in Aldo Garcia Guinto, Matthew Lorentz and Brent Nelson, [*Murray–von Neumann dimension for strictly semifinite weights*, Section 1.2, Lemma 1.2](https://arxiv.org/html/2405.15725v2#S1.SS2). The finite-projection extraction above uses the spectral inequality \(1_{[\delta,\infty)}(b)\le b/\delta\). The direct bounded-density sum (SN.9) explains how to recover the entire weight from its pieces.

Gert K. Pedersen and Masamichi Takesaki, [*The Radon–Nikodym theorem for von Neumann algebras*, Acta Mathematica 130 (1973), Theorem 5.12](https://projecteuclid.org/euclid.acta/1485889766), is the primary antecedent for invariant affiliated densities. We use the course's complete support-sensitive invariant-density proof, with its own prerequisite status, for (SN.13).

François Combes, [*Poids associé à une algèbre hilbertienne à gauche*, Compositio Mathematica 23 (1971), Theorem 3.4, pp. 60–63](https://www.numdam.org/item/CM_1971__23_1_49_0/), is an earlier freely readable antecedent for assertions 1–3. Its group-finiteness condition means that invariant positive normal functionals detect every nonzero positive element; normalization gives the sufficient states used here. Its proof uses an invariant normal expectation and convex modular-orbit averages. The proof above instead treats invariant states through their complete affiliated-density supports. The theorem concerns arbitrary index families.

Kazuyuki Saitô, [*Groups of *-automorphisms and invariant maps of von Neumann algebras*, Pacific Journal of Mathematics 57 (1975), §2–3, pp. 554–556](https://msp.org/pjm/1975/57-2/pjm-v57-n2-p28-s.pdf), gives the freely readable group-theoretic antecedent connecting sufficient invariant normal states to weakly compact predual orbits. The theorem is stated for the orbit of every relatively weakly compact set; the opening of §3 explicitly says that positive singleton orbits suffice for the reverse implication. Here the compactness approximation and fixed-corner argument are written in full at the named functional-analytic inputs.

The predual compactness and affine fixed-point proofs are the exact programme and course providers linked above. The fixed-point proof at TE-14 credits its classical Namioka–Asplund geometry and its existing GPT-6.1 Sol programme author. The exposition, applications, approximation arguments and solved problems here are OpenAI Codex contributions, GPT-6.1 Sol, Ultra, October 2026, CC0-1.0. No human-authored source text has been imported into this lesson.
