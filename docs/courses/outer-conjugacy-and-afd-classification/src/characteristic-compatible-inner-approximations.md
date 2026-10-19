# Inner approximations compatible with characteristic data

*Exposition, relative approximation argument and exercises by GPT-6.1 Sol (OpenAI); topology and fixed-ultrafilter details by GPT-6 Astra (OpenAI). Original programme expression: CC0-1.0.*

## Introduction

Approximating an automorphism by inner automorphisms need not approximate the unitaries that compare its action on a group. Those unitaries carry characteristic information. We retain them while correcting the inner approximants.

The correction has two parts. First, the discrepancy between an inner approximant and the prescribed unitaries becomes a cocycle in the asymptotic centralizer. Compatibility on the inner subgroup makes that cocycle descend to the quotient group. Second, a unitary coboundary in the centralizer corrects the approximants. We prove the estimates which return this correction to the original algebra, where the multiplying unitaries vary with the approximant.

For every countable amenable action on the hyperfinite semifinite factor, the Gaussian tower theorem supplies the required centralizer coboundary. We obtain simultaneous approximation of the automorphism and its prescribed cocycle. Cyclic actions of every outer period, including zero, and trace-scaling actions are included. The general approximation implication also applies to other factors whenever their quotient action has the stated cohomology property.

The classical relative-density argument is [Jones–Takesaki], Lemma 2.5.6; [Sutherland–Takesaki], Lemma 4.3, explains the characteristic-compatible form for general amenable groups. The exact centralizer construction and unitary lifts used here are [Central sequence algebras and exact lifts](../../OA-APPROX/central-sequence-algebras-and-exact-lifts.html), Proposition 2.1 and Theorems 3.1 and 5.1. [Bounded topology and tracial representations](bounded-topology-and-tracial-representations.md#3a-faithful-state-tests-and-ordinary-extraction), Section 3A, supplies faithful-state strong-star tests and ordinary extraction. [Trace scaling on the hyperfinite semifinite factor](trace-scaling-on-the-hyperfinite-semifinite-factor.md), Theorem 4.2 and Proposition 5.1, supplies central triviality and trace-preserving approximate innerness. The amenable cocycle input is [Gaussian models and amenable towers](gaussian-models-and-amenable-towers.md), Theorem 8.1, at its exact faithful induced-action hypotheses. Section 6 also uses the elementary abelian Følner proof in [Relative character eigenunitaries](relative-character-eigenunitaries.md), Lemma 3.1. The direct proofs and their separately stated analytic foundations retain their full scope.

## 1. Small errors between moving unitaries

The u-topology on automorphisms is pointwise norm convergence of their actions on the predual. Inversion and composition are continuous. On uniformly bounded sets, strong-star convergence can be tested by the seminorms
\[
\begin{gathered}
\|x\|_\varphi^\sharp
=\bigl(\varphi(x^*x)+\varphi(xx^*)\bigr)^{1/2},\\
\varphi\in M_*^+.
\end{gathered}
\tag{1.1}
\]

Here are the topology details used below. Suppose that \(\alpha_i\to\alpha\) and \(\beta_i\to\beta\) in the u-topology. For a fixed normal functional \(\psi\), composition by an automorphism is an isometry, so
\[
\begin{aligned}
\|\psi\alpha_i\beta_i-\psi\alpha\beta\|
&\leq\|\psi\alpha_i-\psi\alpha\|\\
&\quad+\|(\psi\alpha)\beta_i-(\psi\alpha)\beta\|,\\
\|\psi\alpha_i^{-1}-\psi\alpha^{-1}\|
&=\|\psi-(\psi\alpha^{-1})\alpha_i\|.
\end{aligned}
\tag{1.1a}
\]
Both right sides tend to zero. In particular group composition and inversion are continuous. U-convergence also gives strong-star convergence on every fixed algebra element. To see this directly, first let \(\theta_i\to\operatorname{id}\), fix \(x\in M\), and put \(y_i=\theta_i(x)-x\). For every normal positive \(\varphi\),
\[
\begin{aligned}
\varphi(y_i^*y_i)
&=\varphi(\theta_i(x^*x))
 -\varphi(\theta_i(x)^*x)\\
&\quad-\varphi(x^*\theta_i(x))+\varphi(x^*x)
 \longrightarrow0.
\end{aligned}
\tag{1.1b}
\]
U-convergence implies ultraweak convergence on each fixed element, and multiplication by a fixed element is globally normal. Thus each term has the displayed limit. Applying the same computation to the adjoint gives the other squared seminorm. Uniform boundedness and the strong-star criterion prove the assertion. For a general limit, apply this to the inverse of the limit composed with each approximating automorphism, then use normality of the fixed limit automorphism. These arguments work for nets and for a fixed ultrafilter as well as for ordinary sequences.

**Lemma 1.1.** Let \(x_j\) be uniformly bounded and tend strongly-star to zero. Let \(b_j,c_j\) be unitaries such that \(\operatorname{Ad}b_j\to\beta\) and \(\operatorname{Ad}c_j^*\to\eta\) in the u-topology. Then \(b_jx_jc_j\to0\) strongly-star. The assertion also holds along a fixed ultrafilter.

*Proof.* Put \(C=\sup_j\|x_j\|\). For \(\varphi\in M_*^+\), the two squared seminorm terms satisfy
\[
\begin{aligned}
\varphi(c_j^*x_j^*x_jc_j)
&\leq(\varphi\circ\eta)(x_j^*x_j)\\
&\quad{}+C^2\|\varphi\circ\operatorname{Ad}c_j^*
                         -\varphi\circ\eta\|,\\
\varphi(b_jx_jx_j^*b_j^*)
&\leq(\varphi\circ\beta)(x_jx_j^*)\\
&\quad{}+C^2\|\varphi\circ\operatorname{Ad}b_j
                         -\varphi\circ\beta\|.
\end{aligned}
\tag{1.2}
\]
The first terms vanish because their functionals are fixed. The second terms vanish in predual norm. These are exactly the two terms for \(b_jx_jc_j\). The same reasoning applies to ultrafilter limits. \(\square\)

The convergence of the surrounding inner automorphisms is essential. If \(p_j\) projects onto the \(j\)-th vector in \(\ell^2(\mathbb N_0)\), then \(p_j\to0\) strongly-star. A unitary \(c_j\) swapping vectors zero and \(j\) gives \(\|p_jc_je_0\|=1\). Arbitrary moving right multiplication does not preserve a strong limit.

## 2. Keep the implementing cocycle

Let \(M\) be a factor with separable predual, and let \(\sigma:G\to\operatorname{Aut}(M)\) be an action of a countable discrete group. A comparison pair consists of an automorphism \(\pi\) and a genuine unitary \(\sigma\)-cocycle \(w\) with
\[
\begin{aligned}
w_{gh}&=w_g\sigma_g(w_h),\qquad w_e=1,\\
\pi\sigma_g\pi^{-1}
&=\operatorname{Ad}w_g\circ\sigma_g.
\end{aligned}
\tag{2.1}
\]
Its inner subgroup is the normal subgroup
\[
N=\{n\in G:\sigma_n\text{ is inner}\}.
\tag{2.2}
\]
Choose normalized implementing unitaries \(U_n\) with \(\sigma_n=\operatorname{Ad}U_n\). Their multiplication has scalar factors:
\[
U_nU_m=\mu(n,m)U_{nm}.
\tag{2.3}
\]
The compatibility needed below is
\[
\pi(U_n)=w_nU_n
\qquad(n\in N).
\tag{2.4}
\]
This equality is independent of the scalar chosen for \(U_n\). It specifies an actual phase of \(w_n\), rather than only its inner automorphism.

Every unitary \(a\in M\) gives a compatible inner pair
\[
\iota(a)=
\bigl(\operatorname{Ad}a,\{a\sigma_g(a^*)\}_{g\in G}\bigr).
\tag{2.5}
\]
The approximation sought is simultaneous:
\[
\begin{gathered}
\operatorname{Ad}a_j\longrightarrow\pi
\quad\text{in the u-topology},\\
a_j\sigma_g(a_j^*)\longrightarrow w_g,\\
\text{strongly-star for each }g.
\end{gathered}
\tag{2.6}
\]

Comparison pairs have multiplication
\[
(\pi,w)(\rho,v)
=\bigl(\pi\rho,\{\pi(v_g)w_g\}_{g\in G}\bigr).
\tag{2.7}
\]
The intertwining identity in (2.1) verifies that the resulting unitaries are again a genuine cocycle. It also gives
\[
(\pi,w)\iota(a)(\pi,w)^{-1}=\iota(\pi(a)).
\tag{2.8}
\]
Thus the inner pairs form a normal subgroup. Conditions (2.4) are preserved by (2.7) and inversion.

For example, if both pairs are compatible, then
\(\pi\rho(U_n)=\pi(v_n)\pi(U_n)=\pi(v_n)w_nU_n\).
For the inverse pair, apply \(\pi^{-1}\) to
\(w_n^*\pi(U_n)=U_n\). This gives
\(\pi^{-1}(U_n)=\pi^{-1}(w_n^*)U_n\), the required inverse compatibility.

## 3. A discrepancy descends to the quotient

Assume \(\pi\) is approximately inner. Choose unitaries \(a_j\) with \(\pi_j:=\operatorname{Ad}a_j\to\pi\), and define
\[
v_{g,j}=a_j^*w_g\sigma_g(a_j).
\tag{3.1}
\]
The index \(j\) is the same in all three factors.

**Lemma 3.1.** For each \(g\), \((v_{g,j})_j\) is a strongly central unitary sequence. For every \(j\) it is an exact \(\sigma\)-cocycle:
\[
v_{g,j}\sigma_g(v_{h,j})=v_{gh,j}.
\tag{3.2}
\]
If (2.4) holds, then \(v_{n,j}\to1\) strongly-star for every \(n\in N\).

*Proof.* The inner automorphism of (3.1) is
\[
\operatorname{Ad}v_{g,j}
=\pi_j^{-1}\pi\sigma_g\pi^{-1}\pi_j\sigma_g^{-1}
\longrightarrow\mathrm{id}.
\tag{3.3}
\]
For a unitary \(v\), right multiplication of a normal-functional commutator by \(v^*\) gives
\[
\|v\varphi-\varphi v\|
=\|\varphi-\varphi\circ\operatorname{Ad}v\|.
\tag{3.4}
\]
Indeed the two functionals agree up to sign after composing their argument with \(x\mapsto xv^*\), an isometry of the unit ball. Equation (3.3) therefore proves strong centrality. Multiplying (3.1) twice and canceling \(\sigma_g(a_j)\sigma_g(a_j^*)\) proves (3.2).

For \(n\in N\), compatibility gives the stronger identity
\[
v_{n,j}
=\pi_j^{-1}\bigl(\pi(U_n)\bigr)U_n^*
\longrightarrow1.
\tag{3.5}
\]
The convergence follows from \(\pi_j^{-1}\pi\to\mathrm{id}\) on the fixed \(U_n\). \(\square\)

Fix a free ultrafilter \(\omega\). Write \(F=M_\omega\) for the asymptotic centralizer and \(V_g=[(v_{g,j})]\). Inner automorphisms act trivially on \(F\), since their fixed implementing unitary commutes asymptotically with every central sequence. Thus the action induced by \(\sigma\) factors through \(Q=G/N\).

Equation (3.5) gives \(V_n=1\). The cocycle law then gives \(V_{gn}=V_g=V_{ng}\). Consequently \(V\) is a genuine cocycle for the induced action \(\gamma\) of \(Q\) on \(F\).

The factor's canonical tracial state on \(F\) is invariant under every induced automorphism, even when \(\sigma_g\) scales a semifinite trace on \(M\). This is the state-independence argument in Section 1 of [Central towers and unitary cocycles](central-towers-and-unitary-cocycles.md). The two traces serve different purposes.

## 4. Correct the approximants in their original coordinates

The exact cohomology hypothesis for the quotient action is:

Every unitary \(\gamma\)-cocycle \(V\) in \(F\) has a unitary \(Z\in F\) such that
\[
V_q=Z\gamma_q(Z^*)
\qquad(q\in Q).
\tag{4.1}
\]

**Theorem 4.1.** Suppose \(\pi\) is approximately inner, (2.4) holds, and the quotient action on \(M_\omega\) has property (4.1). Then a sequence of compatible inner pairs converges to \((\pi,w)\) as in (2.6).

*Proof.* Apply (4.1) to the cocycle in Section 3. Lift \(Z\) to exactly unitary representatives \(z_j\) which are strongly central along \(\omega\). Set
\[
b_j=a_jz_j,\qquad
t_{g,j}=b_j^*w_g\sigma_g(b_j).
\tag{4.2}
\]
Strong centrality gives \(\operatorname{Ad}z_j\to\mathrm{id}\) in the u-topology along \(\omega\). Hence \(\operatorname{Ad}b_j\to\pi\). In the quotient, (4.1) gives
\[
[(t_{g,j})]
=Z^*V_g\gamma_g(Z)=1.
\tag{4.3}
\]
Thus \(t_{g,j}-1\to0\) strongly-star along \(\omega\). The exact equation back in \(M\) is
\[
w_g-b_j\sigma_g(b_j^*)
=b_j(t_{g,j}-1)\sigma_g(b_j^*).
\tag{4.4}
\]
Apply Lemma 1.1. The left surrounding automorphisms converge to \(\pi\), and the right ones required by that lemma satisfy
\[
\operatorname{Ad}\sigma_g(b_j)
\longrightarrow\sigma_g\pi\sigma_g^{-1}.
\tag{4.5}
\]
Both limits are in the u-topology along \(\omega\). Therefore the difference in (4.4) tends strongly-star to zero.

We finally choose an ordinary subsequence. Enumerate \(G\) and choose norm-dense countable families of normal functionals and positive normal functionals. At step \(r\), impose error less than \(1/r\) for the first \(r\) automorphism tests and for the first \(r\) group elements in the first \(r\) strong-star seminorms. Each finite intersection of these requirements belongs to \(\omega\). Choose its index larger than the preceding one. The resulting subsequence has ordinary convergence for every enumerated test.

The estimate \(2\|\varphi-\psi\|\) extends the automorphism convergence to every normal functional. Uniform boundedness of the unitary differences extends the strong-star tests from the dense positive family to every positive normal functional. Relabeling the selected \(b_j\) gives (2.6). Each \(\iota(b_j)\) is an actual compatible inner pair. \(\square\)

The prescribed cocycle has not been reindexed independently of its correcting representatives. The proof also does not discard the moving right unitary in (4.4); its predual images are controlled by (4.5).

## 5. All cyclic periods on the semifinite factor

The approximation theorem holds for every countable amenable group, so the cyclic cases follow together. Let \(R_\infty\) be the hyperfinite type \(\mathrm{II}_\infty\) factor with separable predual. Let \(G\) be a countable amenable group acting on it by \(\sigma\), and let \((\pi,w)\) satisfy (2.1) and (2.4). Suppose \(\pi\) preserves a faithful normal semifinite trace.

**Theorem 5.1.** Under the stated programme prerequisites, compatible inner pairs approximate \((\pi,w)\) as in (2.6).

*Proof.* Proposition 5.1 of [Trace scaling on the hyperfinite semifinite factor](trace-scaling-on-the-hyperfinite-semifinite-factor.md#5-straightening-a-trace-preserving-automorphism) makes \(\pi\) approximately inner. It straightens a trace-one corner and then all type-I matrix units, leaving an automorphism of the finite hyperfinite factor. [Local approximation and the hyperfinite finite factor](../../OA-APPROX/hyperfinite-finite-factors.html#6-subfactors-and-automorphisms), Theorem 6.3, supplies inner approximants on that finite corner; normal product-functional density gives their amplified u-convergence. Theorem 4.2 of [Trace scaling on the hyperfinite semifinite factor](trace-scaling-on-the-hyperfinite-semifinite-factor.md) gives
\[
\operatorname{Ct}(R_\infty)=\operatorname{Inn}(R_\infty).
\tag{5.1}
\]
For this fixed free ultrafilter, an induced automorphism on \(F=(R_\infty)_\omega\) is the identity exactly when the original automorphism is centrally trivial. Here is the full quantifier check. If an ordinary bounded central sequence is displaced, pass to a subsequence whose faithful-state sharp displacement is bounded below by one positive number. The subsequence is still ordinarily central, so it is central along the prescribed ultrafilter and defines a displaced class there. Conversely, a displaced class has bounded central representatives and a positive displacement lower bound on an ultrafilter-large set. At stage \(r\), intersect that set with the first \(r\) predual centrality tests, each with tolerance \(1/r\), and with the indices larger than the preceding choice. The intersection is ultrafilter-large. The selected ordinary sequence is central by predual norm density and remains displaced by the faithful-state criterion. Thus no change of the chosen ultrafilter is needed in either direction. Consequently
\[
\begin{aligned}
\ker(G\longrightarrow\operatorname{Aut}F)
&=\{g:\sigma_g\in\operatorname{Ct}(R_\infty)\}\\
&=N.
\end{aligned}
\tag{5.2}
\]
The quotient action of \(Q=G/N\) on \(F\) is therefore faithful. In particular every nonidentity \(\gamma_q\) is nontrivial; no assumption that the original action of \(G\) is outer is needed.

The quotient \(Q\) is countable and amenable. For a prescribed finite set of quotient translations, choose lifts in \(G\) and a Følner set for these lifts with arbitrarily small total relative boundary. Push its normalized indicator forward to a finitely supported probability function on \(Q\). Each translation defect in \(\ell^1\) can only decrease. For a nonnegative finitely supported function \(f\), write its superlevel sets as \(S_t=\{q:f(q)>t\}\). The identities
\(\int_0^\infty |S_t|\,dt=\|f\|_1\) and
\(\int_0^\infty |qS_t\mathbin\triangle S_t|\,dt=\|qf-f\|_1\)
show that one nonempty superlevel set has simultaneously small total relative boundary for any prescribed finite set of translations. This gives the finite Følner criterion for \(Q\).

Choose one representative of each quotient element and use its \(\sigma_g\) as a lift of \(\gamma_q\). These lifts need not multiply on \(R_\infty\); their induced maps do multiply on \(F\). Theorem 8.1 of [Gaussian models and amenable towers](gaussian-models-and-amenable-towers.md), with prescribed coefficient algebra \(P=\mathbb C1\), applies to precisely this setting: a separable-predual factor, its canonical tracial centralizer, a countable amenable group, and nontrivial induced automorphisms for every nonidentity element. It gives (4.1) for the discrepancy cocycle of Section 3. If \(Q\) is trivial, take \(Z=1\) directly. Theorem 4.1 now proves (2.6). \(\square\)

For a \(\mathbb Z\)-action write \(N=p\mathbb Z\), with \(0\mathbb Z=\{0\}\). The theorem includes \(p=0\), \(p=1\) and every positive finite \(p\). It requires neither a finite-order generator on \(R_\infty\) nor a trace-preserving generator.

In particular, if \(\tau\circ\sigma_1=\lambda\tau\) with \(\lambda\ne1\), no nonzero power can be inner. Otherwise innerness of \(\sigma_m\) would give \(\lambda^m=1\), contradicting positive \(\lambda\ne1\). Thus this trace-scaling case has infinite cyclic quotient. For a general amenable group the same theorem retains the entire inner subgroup and the exact phases (2.4).

## 6. Correcting a scalar phase on the inner subgroup

An arbitrary comparison pair need not satisfy (2.4). It always has scalars \(c_n\in\mathbb T\) with
\[
\pi(U_n)=c_nw_nU_n.
\tag{6.1}
\]

**Lemma 6.1.** The function \(c:N\to\mathbb T\) is a character.

*Proof.* Use (2.3) and the genuine cocycle law to obtain
\[
\begin{aligned}
\pi(U_n)\pi(U_m)
&=c_nc_mw_nU_nw_mU_m\\
&=\mu(n,m)c_nc_mw_{nm}U_{nm}.
\end{aligned}
\tag{6.2}
\]
Applying \(\pi\) directly to \(U_nU_m\) gives the same expression with \(c_{nm}\) instead of \(c_nc_m\). Cancel the scalar multiplier and unitary to get \(c_{nm}=c_nc_m\). \(\square\)

**Lemma 6.2.** Every character of a subgroup of a countable discrete abelian group extends to the whole group.

*Proof.* Use additive notation and enumerate the ambient group. Suppose a character is defined on a subgroup \(H\), and the next element is \(g\). If a positive multiple of \(g\) belongs to \(H\), let \(k\) be the least such positive integer. Choose \(\zeta\in\mathbb T\) with \(\zeta^k=c(kg)\). Define on \(H+\mathbb Zg\)
\[
c'(h+mg)=c(h)\zeta^m.
\tag{6.3}
\]
Two expressions for the same element differ by a multiple of \(kg\), so the defining root identity makes the values equal. If no positive multiple belongs to \(H\), the expression is unique and any \(\zeta\in\mathbb T\) works. In either case this is a character extending \(c\). Repeating the extension along the enumeration gives the desired character on the union, which is the whole group. \(\square\)

If \(G\) is abelian, extend the character in (6.1) to \(\chi:G\to\mathbb T\), and put \(w'_g=\chi(g)w_g\). This remains a genuine cocycle, implements the same automorphism in (2.1), and satisfies (2.4).

**Corollary 6.3.** For every trace-preserving comparison automorphism \(\pi\) of a countable abelian action on \(R_\infty\), there are a character \(\chi\) and unitaries \(a_j\) with
\[
\begin{gathered}
\operatorname{Ad}a_j\longrightarrow\pi,\\
a_j\sigma_g(a_j^*)\longrightarrow\chi(g)w_g
\quad(g\in G).
\end{gathered}
\tag{6.4}
\]

*Proof.* A countable abelian group is amenable by [Relative character eigenunitaries](relative-character-eigenunitaries.md), Lemma 3.1. That proof pushes the uniform measure on an integer box onto the subgroup generated by the finite test set. Translation errors decrease under pushforward, even when labels collide, and a finite weighted average of superlevel sets supplies a nonempty Følner set. Thus the statement includes torsion and arbitrary relations without requiring a chosen decomposition of the finitely generated subgroup. Lemmas 6.1–6.2 provide the compatible cocycle \(w'\). Apply Theorem 5.1 to \((\pi,w')\). \(\square\)

The scalar character can be necessary. For the trivial \(\mathbb Z\)-action and \(\pi=\mathrm{id}\), take \(w_m=i^m1\). Every inner pair has generator cocycle \(a\sigma_1(a^*)=1\); it cannot converge to \(i1\). Choosing \(\chi(m)=i^{-m}\) gives the compatible representative. In action classification, compatibility must be imposed with the characteristic data being compared, rather than rephasing unrelated data independently.

## 7. Exercises with complete solutions

**Exercise 7.1. A transported functional. Level 2.** Derive the first inequality in (1.2) and explain the appearance of \(C^2\).

*Solution.* Subtract the fixed functional \(\varphi\circ\eta\) from \(\varphi\circ\operatorname{Ad}c_j^*\), and evaluate the difference at \(x_j^*x_j\). Its absolute value is bounded by the functional norm times \(\|x_j^*x_j\|\le C^2\). Adding the fixed positive term gives the inequality.

**Exercise 7.2. Which side corrects the cocycle? Level 2.** For \(b_j=a_jz_j\), derive \(t_{g,j}=z_j^*v_{g,j}\sigma_g(z_j)\). What equation for \(Z\) makes its quotient class one?

*Solution.* Expand \(b_j^*w_g\sigma_g(b_j)\), and use (3.1). Its class is \(Z^*V_g\gamma_g(Z)\). It equals one when \(V_g=Z\gamma_g(Z^*)\). Multiplication on the right of \(a_j\) retains this exact order; arbitrary exchange of the factors is invalid.

**Exercise 7.3. Negative generator values. Level 1.** For a cocycle \(V\) of a \(\mathbb Z\)-action \(\gamma\), compute \(V_{-1}\) from \(V_1\). Check it when \(V_1=Z\gamma_1(Z^*)\).

*Solution.* From \(V_0=V_{-1}\gamma_{-1}(V_1)=1\), we get \(V_{-1}=\gamma_{-1}(V_1^*)\). Substitution gives \(Z\gamma_{-1}(Z^*)\), as required by (4.1).

**Exercise 7.4. A finite cyclic consistency condition. Level 2.** If \(Q=\mathbb Z/p\mathbb Z\), show that the generator value of \(V\) satisfies \(V_1\gamma_1(V_1)\cdots\gamma_1^{p-1}(V_1)=1\). Why does the descended cocycle in Section 3 satisfy this condition?

*Solution.* Iterating the cocycle identity gives the displayed product as \(V_p\). The element \(p\) is zero in \(Q\), hence \(V_p=V_0=1\). In the \(\mathbb Z\)-action before descent, \(p\in N\) and (3.5) gives \(V_p=1\). An arbitrary unitary chosen as generator would not automatically meet this finite-order condition.

**Exercise 7.5. Extend an inner-subgroup phase. Level 2.** Let \(G=\mathbb Z\), \(N=6\mathbb Z\), and \(c(6)=\exp(2\pi i/5)\). Give all possible values of an extending character at \(1\).

*Solution.* The value \(\zeta=\chi(1)\) must satisfy \(\zeta^6=\exp(2\pi i/5)\). The six choices are
\[
\begin{gathered}
\zeta_k=\exp\!\left(2\pi i\left(\frac1{30}+\frac{k}{6}\right)\right),\\
0\le k<6.
\end{gathered}
\tag{7.1}
\]
Each defines \(\chi(m)=\zeta_k^m\). The extension is generally not unique.

**Exercise 7.6. The nonabelian extension problem. Level 3.** In the quaternion group \(Q_8=\{\pm1,\pm i,\pm j,\pm k\}\), let \(N=\{\pm1\}\) and \(c(-1)=-1\). Show that \(c\) does not extend to a scalar character of \(Q_8\).

*Solution.* Every homomorphism to the abelian group \(\mathbb T\) kills commutators. In \(Q_8\), \(iji^{-1}j^{-1}=-1\). Therefore any scalar character has value one at \(-1\), contrary to the prescribed \(c\). Lemma 6.2 uses abelianness; this example makes no claim that arbitrary character extension is available in the general relative approximation theorem.

**Exercise 7.7. Finite period forces trace preservation. Level 1.** Suppose \(\tau\circ\sigma_1=\lambda\tau\), \(\lambda>0\), and \(\sigma_p\) is inner for some positive \(p\). Prove \(\lambda=1\).

*Solution.* Iteration gives \(\tau\circ\sigma_p=\lambda^p\tau\). An inner automorphism preserves the trace, so \(\lambda^p=1\). A positive real number with a positive integral power equal to one is one.

**Exercise 7.8. A normal subgroup of pairs. Level 3.** Verify the cocycle component in (2.8).

*Solution.* The inverse pair is \((\pi^{-1},\{\pi^{-1}(w_g^*)\})\). Put \(d=\pi(a)\). Multiplication by (2.7) gives the cocycle of the conjugated pair as
\[
\begin{aligned}
\operatorname{Ad}d(w_g^*)\,&\pi(a\sigma_g(a^*))w_g\\
&=d w_g^*d^*\,d w_g\\
&\quad{}\cdot\sigma_g(d^*)w_g^*w_g\\
&=d\sigma_g(d^*).
\end{aligned}
\tag{7.2}
\]
Here (2.1) gives \(\pi\sigma_g(a^*)=w_g\sigma_g(\pi(a^*))w_g^*\). The automorphism component is \(\operatorname{Ad}d\), proving (2.8).

## References

[Jones–Takesaki] Vaughan F. R. Jones and Masamichi Takesaki, *Actions of compact abelian groups on semifinite injective factors*, Acta Mathematica 153 (1984), 213–258. Equations (2.5.3)–(2.5.4), printed page 242, define the comparison pairs. Lemma 2.5.6 and its full proof, printed pages 243–245, gives the classical relative-density argument and the abelian scalar-character correction. Sections 1–5 above give the general conditional approximation argument with its moving-multiplier estimates; Section 6 handles the scalar correction separately. [Article identifier](https://doi.org/10.1007/BF02392378) · [Complete archive PDF](https://archive.ymsc.tsinghua.edu.cn/pacm_download/117/6360-11511_2006_Article_BF02392378.pdf).

[Sutherland–Takesaki] Colin E. Sutherland and Masamichi Takesaki, *Actions of discrete amenable groups and groupoids on von Neumann algebras*, Publications of the Research Institute for Mathematical Sciences 21 (1985), 1087–1120. Section 4, equations (8)–(12) and Lemma 4.3, printed pages 1108–1110, gives the characteristic-compatible density context for general amenable groups. Its measurable-groupoid assertions are separate from the fixed-group theorem proved here. [Open publisher article and PDF](https://ems.press/journals/prims/articles/3261).

[Connes] Alain Connes, *Periodic automorphisms of the hyperfinite factor of type II-one*, Acta Scientiarum Mathematicarum 39 (1977), 39–66. The introduction, printed pages 39–41, describes the outer-period and obstruction classification underlying the cyclic background. Its classification theorem is not substituted for the direct approximation proof above. [Complete author-hosted PDF](https://alainconnes.org/wp-content/uploads/szego.pdf).

[Programme] The linked quotient/lifting, bounded-topology, trace-scaling, Gaussian-tower and elementary Følner proofs supply the exact inputs identified above. Their actual classical sources and component terms remain those stated in each provider. Human works retain their own rights; no reproduction permission is inferred from access to them.
