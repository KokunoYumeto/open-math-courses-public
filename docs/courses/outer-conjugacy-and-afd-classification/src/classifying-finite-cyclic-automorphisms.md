# Classifying finite cyclic automorphisms

*Written by GPT-6.1 Sol (OpenAI), Ultra, September 2026. Mathematical and source review by GPT-6 Astra (OpenAI), Ultra, October 2026, under the stated prerequisites. New original text is public domain (CC0).*

## Introduction

Exact clock and shift pairs can be extracted one after another. Their shifts become central, and each clock implements the part of the automorphism left on the preceding relative commutant. Summable averaging errors then produce a tensor factor carrying a concrete cyclic product action. Approximation on the predual identifies the action on its complement as the identity.

There is one further identification to make: the complement need not itself be isomorphic to the original factor. An explicit identity tensor leg inside the cyclic model repairs this. With that identification in place, a finite outer period and its implementing phase classify the approximately inner automorphisms whose outer and asymptotic periods agree.

The immediate prerequisites are [Exact Weyl pairs for cyclic actions](exact-weyl-pairs-for-cyclic-actions.md), Corollary 6.1 and formulas (6.2)–(6.3); [Finite outer period and obstruction](finite-outer-period-and-obstruction.md), Propositions 1.1, 2.1, 3.2–3.3 and Theorem 4.2; and [Comparing asymptotically aperiodic automorphisms](comparing-asymptotically-aperiodic-automorphisms.md), Lemma 2.2 and Corollary 7.1. The matrix-complement period identification is Lemma 4.2 of [Matrix eigenvectors and tensor absorption](matrix-eigenvectors-and-tensor-absorption.md); its Section 1 states the general normal-functional tensor-splitting interface and explains the extension from dense states to a norm-total family. Its Proposition 6.3 supplies outer absorption by the unperturbed model. The full programme proof of summable splitting is Strong stability and tensor absorption, Theorem 3.1; Lemma 4.1 and Theorem 5.1 supply strongly stable finite matrix complements.

For faithful normal states and their GNS representations, use [Bounded ultrastrong topology and the semifinite tracial representation](bounded-topology-and-tracial-representations.md), Lemmas 3A.1–3A.3 and Theorem 3A.4. The hyperfinite inputs are Local approximation and the hyperfinite finite factor, Theorem 6.3, for approximate innerness; and Centrally trivial automorphisms and decreasing AFD factors, Lemma 4.1 and Theorem 4.2, for \(\operatorname{Ct}(R)=\operatorname{Inn}(R)\). The exact-pair prerequisite uses [Finite free actions and unitary coboundaries](finite-free-actions-and-coboundaries.md), Sections 5 and 7–11, for the fixed-factor and projection comparisons. These links retain the providers' stated trace, projection, normal-representation and infinite-product foundations.

The general cyclic extraction and period/phase classification are treated in [Takesaki III], Theorems XVII.3.20 and XVII.3.16. The finite coefficient and summable-splitting mechanisms are [Connes outer], Lemmas 3.2.6 and 2.3.6. [Connes periodic], Theorems 5.1 and 6.2, gives the hyperfinite specialization and the tensor-product law for phases. Our organization isolates the finite tests, the infinite complement, an explicit identity tensor leg, and phase cancellation; the five solved exercises test these steps. [Takesaki II] is historical credit for the finite free-action prerequisite.

All algebras below are von Neumann algebras, and all automorphisms and isomorphisms are normal. A factor \(M\) is strongly stable when \(M\cong M\overline\otimes R\). Approximate innerness means closure of the inner automorphisms for pointwise norm convergence on the predual: \(\alpha_n\to\alpha\) when \(\|\psi\circ\alpha_n-\psi\circ\alpha\|\to0\) for every \(\psi\in M_*\). The outer period \(p_o(\theta)\) is the least positive \(q\) for which \(\theta^q\) is inner, or \(0\) if none exists. The asymptotic period \(p_a(\theta)\) is defined in the same way using central triviality: every bounded sequence \((x_n)\) satisfying \(\|[x_n,\psi]\|\to0\) for all normal \(\psi\) must have \(\theta^q(x_n)-x_n\to0\) strongly-star. Thus \(0\) denotes an infinite period, not the identity action. If \(p_o(\theta)=p>0\) and \(\theta^p=\operatorname{Ad}U\), its obstruction is the scalar \(\gamma\) in \(\theta(U)=\gamma U\); Proposition 1.1 of the obstruction lesson proves that it is well defined and \(\gamma^p=1\).

## 1. Extracting a genuine cyclic action

Let \(R\) be the hyperfinite \(\mathrm{II}_1\) factor. For \(p\geq2\), write
\[
\begin{gathered}
c_p\xi_j=\lambda^j\xi_j,
\quad\lambda=e^{2\pi i/p},\\
\qquad\sigma_p=\bigotimes_{k\geq1}\operatorname{Ad}c_p
\end{gathered}
\tag{1.1}
\]
on the tracial product of copies of \(M_p\). This is the same model as before, with its diagonal basis reordered. Set \(\sigma_1=\mathrm{id}_R\).

**Theorem 1.1 (cyclic extraction).** Suppose \(M\) is a strongly stable factor with separable predual and
\[
\begin{gathered}
\theta\in\overline{\operatorname{Inn}}M,\\
\qquad\theta^p=\mathrm{id},
\qquad p_a(\theta)=p\geq1.
\end{gathered}
\tag{1.2}
\]
There is a normal isomorphism \(\pi:M\to M\overline\otimes R\) such that
\[
\pi\theta\pi^{-1}=\mathrm{id}_M\otimes\sigma_p.
\tag{1.3}
\]

For \(p=1\), this is the identity action and strong stability. We prove the assertion for \(p\geq2\) in the next three sections.

The factor hypothesis matters. On \(R\oplus R\), the action \(\mathrm{id}_R\oplus\sigma_2\) has ordinary and asymptotic period two, but one nonzero central summand has the identity action. The action \(\mathrm{id}_{R\oplus R}\otimes\sigma_2\) has no such summand. An isomorphism preserves central summands and the identity action on them, so these actions cannot be conjugate. A single global period therefore cannot replace the factor hypothesis.

## 2. Finite tests with one extra functional

Choose a faithful normal state and average it over the cyclic group to obtain a faithful \(\theta\)-invariant state \(\varphi\). Let \(\psi_1=\varphi\), and choose \(\psi_2,\psi_3,\ldots\) so that together they are norm dense in the unit ball of \(M_*\). Put
\[
\varepsilon_v=\frac{2^{-v}}{8p^3},
\qquad d_v=\frac{\varepsilon_{v+1}}4.
\tag{2.1}
\]
We construct commuting matrix factors \(K_v\cong M_p\), generated by unitaries \(u_v,v_v\), and products \(U_v=u_1\cdots u_v\). Require
\[
\begin{aligned}
&u_v^p=v_v^p=1,
\quad\theta(u_v)=u_v,\\
&\quad\theta(v_v)=\lambda v_v=u_vv_vu_v^*,\\
&\|[u_v,\psi_j]\|<\varepsilon_v,
\quad\|[v_v,\psi_j]\|<\varepsilon_v\\
&\quad(j\leq v),\\
&\|\psi_j\circ\theta-\psi_j\circ\operatorname{Ad}U_v\|<d_v\\
&\quad(j\leq v+1).
\end{aligned}
\tag{2.2}
\]
The final line deliberately tests one more functional. It supplies the small residual action needed for the next clock's commutator test.

At the first stage, the central-pair corollary in the preceding lesson gives pairs \((u_n,v_n)\) with \(v_n\) central and \(\operatorname{Ad}u_n\to\theta\). Invariance of \(\varphi\) implies
\[
\|[u_n,\varphi]\|
=\|\varphi\circ\operatorname{Ad}u_n-\varphi\|\longrightarrow0.
\]
Thus one pair meets all the first-stage requirements, including the two approximation tests for \(\psi_1,\psi_2\).

Suppose the construction is complete through \(v-1\). Put
\[
\begin{gathered}
N=K_1\vee\cdots\vee K_{v-1},\\
\qquad C=N'\cap M,
\qquad U=U_{v-1}.
\end{gathered}
\]
The finite matrix decomposition and the exact action on its generators give
\[
M=N\overline\otimes C,
\qquad\theta=\operatorname{Ad}U|_N\otimes\beta.
\tag{2.3}
\]
The factor \(C\) is strongly stable. Its automorphism \(\beta\) is approximately inner, has \(\beta^p=\mathrm{id}\), and has asymptotic period \(p\), by the finite-complement lemmas. Define
\[
\Theta=\mathrm{id}_N\otimes\beta
=\theta\circ\operatorname{Ad}(U^*).
\tag{2.4}
\]
Here \(\theta(U)=U\), since every earlier clock is fixed. The preceding approximation tests imply
\[
\begin{aligned}
&\|\psi_j\circ\Theta-\psi_j\|\\
&=\|\psi_j\circ\theta-\psi_j\circ\operatorname{Ad}U\|\\
&<d_{v-1}=\varepsilon_v/4
\quad(j\leq v).
\end{aligned}
\tag{2.5}
\]

Apply Corollary 6.1 of the exact-Weyl lesson to \(\beta\) on \(C\). Here is the finite coefficient transfer explicitly. Write \(N\cong M_d\), let \(\omega_{ab}\) be its matrix coefficient functionals of norm one, and expand
\[
\begin{gathered}
\psi=\sum_{a,b=1}^d\omega_{ab}\otimes\psi_{ab},\\
\qquad \psi_{ab}(x)=\psi(e_{ab}\otimes x).
\end{gathered}
\]
For \(z\in C\), this gives
\[
\|[1\otimes z,\psi]\|\leq\sum_{a,b}\|[z,\psi_{ab}]\|.
\]
For an automorphism \(\delta\) of \(C\), the same expansion gives
\[
\begin{aligned}
&\|\psi\circ(\mathrm{id}_N\otimes\delta)
-\psi\circ(\mathrm{id}_N\otimes\beta)\|\\
&\leq\sum_{a,b}\|\psi_{ab}\circ\delta-\psi_{ab}\circ\beta\|.
\end{aligned}
\]
These estimates follow by the triangle inequality and \(\|\omega_{ab}\otimes f\|\leq\|f\|\); there are only \(d^2\) coefficients. Thus its central shifts have arbitrarily small commutators with the original finite list \(\psi_1,\ldots,\psi_v\), and its clocks, extended as the identity on \(N\), converge to \(\Theta\) in the predual topology. Choose one pair \((u,v')\) far enough along this sequence that
\[
\|[v',\psi_j]\|<\varepsilon_v\quad(j\leq v),
\tag{2.6}
\]
and that its clocks satisfy both
\[
\begin{aligned}
&\|\psi_j\circ\operatorname{Ad}u-\psi_j\circ\Theta\|
<\varepsilon_v/4\\
&(j\leq v),\\
&\|\psi_j\circ\operatorname{Ad}(Uu)-\psi_j\circ\theta\|
<d_v\\
&(j\leq v+1).
\end{aligned}
\tag{2.7}
\]
For the second line use the additional finite tests \(\psi_j\circ\operatorname{Ad}U\). Since \(u\in C\), it commutes with \(U\). Equations (2.5) and (2.7) give
\[
\begin{aligned}
&\|[u,\psi_j]\|\\
&=\|\psi_j\circ\operatorname{Ad}u-\psi_j\|\\
&<\varepsilon_v/2\quad(j\leq v).
\end{aligned}
\]
Set \(u_v=u\), \(v_v=v'\), and \(K_v=\{u,v'\}''\). The exact pair generates a unital \(M_p\), lies in \(C\), and has the required action. This proves the induction.

No new commutator bound is inferred merely from a new matrix generator. The small residual estimate (2.5) and the extra approximation test at the previous stage supply it.

## 3. Splitting the infinite matrix factor

The clock and shift generate all matrix units, so their adjoint actions form a finite \((\mathbb Z/p\mathbb Z)^2\)-action whose fixed algebra is \(K_v'\cap M\). The conditional expectation onto that algebra is
\[
E_v=\frac1{p^2}\sum_{r,s=0}^{p-1}
\operatorname{Ad}(u_v^r v_v^s).
\tag{3.1}
\]
It is also the Haar average over \(\mathcal U(K_v)\). A commutator telescope and predual isometry give
\[
\begin{aligned}
&\|\psi_j-\psi_j\circ E_v\|\\
&\leq\frac1{p^2}\sum_{r,s}
\bigl(r\|[u_v,\psi_j]\|+s\|[v_v,\psi_j]\|\bigr)\\
&=\frac{p-1}2
\bigl(\|[u_v,\psi_j]\|+\|[v_v,\psi_j]\|\bigr)\\
&\leq p\varepsilon_v
\quad(j\leq v).
\end{aligned}
\tag{3.2}
\]
For each fixed \(j\), the omitted finitely many initial terms have finite norm, while the remaining sum is finite by (2.1). The general summable tensor-splitting theorem therefore gives
\[
\begin{gathered}
K=\bigvee_vK_v\cong R,
\qquad C_\infty=K'\cap M,\\
\qquad M=K\overline\otimes C_\infty.
\end{gathered}
\tag{3.3}
\]
On \(K\), the action is exactly \(\sigma_p\), since every matrix block has its clock action. The last line of (2.2), norm density and predual isometry imply
\[
\operatorname{Ad}U_v\longrightarrow\theta.
\tag{3.4}
\]
Every \(x\in C_\infty\) commutes with every \(U_v\). Thus for each normal functional
\[
\psi(\theta(x))=\lim_v\psi(U_vxU_v^*)=\psi(x),
\]
so \(\theta(x)=x\). Consequently (3.3) identifies
\[
\theta=\sigma_p\otimes\mathrm{id}_{C_\infty}.
\tag{3.5}
\]
The predual limit, rather than agreement on the finite blocks alone, is what identifies the complement action.

## 4. The identity leg inside the model

**Lemma 4.1.** The cyclic model satisfies
\[
\sigma_p\cong\sigma_p\otimes\mathrm{id}_R.
\tag{4.1}
\]

*Proof.* Pair consecutive coordinates of its infinite product. On each \(M_p\otimes M_p\), the basis permutation
\[
T(\xi_i\otimes\xi_j)=\xi_{i+j}\otimes\xi_j,
\qquad i,j\in\mathbb Z/p\mathbb Z,
\tag{4.2}
\]
gives
\[
T(c_p\otimes c_p)T^*=c_p\otimes1.
\]
Indeed the old eigenvalue \(\lambda^{i+j}\) becomes \(\lambda^k\) with \(k=i+j\). The product of these finite trace-preserving identifications extends to a normal isomorphism of the infinite tracial products, by TF2–TF3 of [Normal tensor tests and tracial GNS identifications](../foundations/normal-tensor-and-tracial-product-foundations.md). Its inverse and the following regrouping are normal by the same proof; TF1 and TF4 supply the tensor-functional and approximate-innerness limits used in Section 5. Regrouping the two output coordinates gives a model leg and an identity leg, both isomorphic to \(R\). This proves (4.1). For \(p=1\), use \(R\cong R\overline\otimes R\). \(\square\)

Apply this lemma in (3.5). We obtain
\[
(M,\theta)\cong
\bigl(R\overline\otimes R\overline\otimes C_\infty,
\ \sigma_p\otimes\mathrm{id}_{R\overline\otimes C_\infty}\bigr).
\tag{4.3}
\]
The identity complement \(R\overline\otimes C_\infty\) is isomorphic to \(M\), because (3.3) already gives \(M\cong R\overline\otimes C_\infty\). Choose that isomorphism on the identity leg and flip the two factors. This yields (1.3), completing Theorem 1.1. \(\square\)

The proof does not assume \(C_\infty\cong M\). The added identity \(R\)-leg is precisely what supplies the required complement.

## 5. The implementing phase completes the classification

Write \(\alpha\sim\beta\) for outer conjugacy, allowing the stated normal isomorphism between their factors.

**Theorem 5.1.** Let \(M\) be a strongly stable factor with separable predual. Suppose
\[
\begin{gathered}
\theta_1,\theta_2\in\overline{\operatorname{Inn}}M,\\
\qquad p_o(\theta_i)=p_a(\theta_i)=p>0.
\end{gathered}
\tag{5.1}
\]
Then \(\theta_1\) and \(\theta_2\) are outer conjugate if and only if their obstructions are equal.

*Proof.* Obstruction invariance proves necessity. If \(p=1\), both automorphisms are inner and have obstruction \(1\), so sufficiency is immediate. Assume \(p\geq2\).

First suppose \(\theta\) has obstruction \(1\) and both periods \(p\). The cyclic reduction in the obstruction lesson gives an inner perturbation \(\theta'\) with \((\theta')^p=\mathrm{id}\). Inner perturbation preserves approximate innerness and asymptotic period. Theorem 1.1 therefore gives
\[
\theta\sim\mathrm{id}_M\otimes\sigma_p.
\tag{5.2}
\]
The same statement holds with any strongly stable separable factor as its identity carrier.

For \(\gamma^p=1\), choose the realized automorphism \(a_\gamma\) on \(R\) with outer period \(p\) and obstruction \(\gamma\). On \(R\), every automorphism is approximately inner and central triviality is innerness, by the exact published results imported in the comparison lesson. Thus \(p_a(a_\gamma)=p\). Choose separately the model \(a_{\overline\gamma}\). Its obstruction is the complex conjugate phase; it is not being defined as the inverse of \(a_\gamma\).

Tensor products of approximately inner automorphisms remain approximately inner: take product implementers and first test product normal functionals, then use their norm density. The slice criterion for inner tensor actions and the obstruction product formula show
\[
p_o(\theta\otimes a_{\overline\gamma})=p,
\qquad
\operatorname{Ob}(\theta\otimes a_{\overline\gamma})=1.
\tag{5.3}
\]
Their \(p\)-th power is inner, while no smaller power is inner. Their asymptotic period is also \(p\). The \(p\)-th power is inner and hence centrally trivial. For \(1\leq k<p\), choose a bounded central sequence \((x_n)\) in \(R\) for which \(a_{\overline\gamma}^k(x_n)-x_n\) does not tend strongly-star to zero. Then \((1\otimes x_n)\) is central in \(M\overline\otimes R\): on a product normal functional its commutator is the product of the first functional with the original commutator, and finite sums of product functionals are norm dense. Nonvanishing survives the embedding: if a normal positive functional \(\eta\) detects the original difference and \(\rho\) is a normal state on \(M\), then
\[
\|1\otimes y\|_{\rho\otimes\eta}^{\sharp\,2}
=\eta(y^*y)+\eta(yy^*)
=\|y\|_\eta^{\sharp\,2}.
\]
This uses the faithful-state description of bounded strong-star convergence from the topology prerequisite. The same argument applies to \(a_{\overline\gamma}\otimes a_\gamma\). Applying (5.2) gives
\[
\begin{gathered}
\theta\otimes a_{\overline\gamma}
\sim\mathrm{id}_M\otimes\sigma_p,\\
\qquad a_{\overline\gamma}\otimes a_\gamma
\sim\mathrm{id}_R\otimes\sigma_p.
\end{gathered}
\tag{5.4}
\]
The identity carriers have been identified using \(M\overline\otimes R\cong M\) and \(R\overline\otimes R\cong R\).

Outer conjugacy persists under tensoring with another automorphism: tensor the conjugating isomorphism and its correcting unitary with the identity. Proposition 6.3 of the absorption lesson, applied with model period \(p\), followed by (4.1) and (5.4), now yields
\[
\begin{aligned}
\theta
&\sim\theta\otimes\sigma_p
\sim\theta\otimes\mathrm{id}_R\otimes\sigma_p\\
&\sim\theta\otimes a_{\overline\gamma}\otimes a_\gamma
\sim\mathrm{id}_M\otimes\sigma_p\otimes a_\gamma\\
&\sim\mathrm{id}_M\otimes a_\gamma.
\end{aligned}
\tag{5.5}
\]
In the last step flip the model factors and absorb \(\sigma_p\) into \(a_\gamma\), whose asymptotic period is \(p\). Thus every automorphism with the two periods \(p\) and phase \(\gamma\) is outer conjugate to the same model. Applying this to \(\theta_1,\theta_2\) proves sufficiency. \(\square\)

The equality of outer and asymptotic periods is a hypothesis on the general factor. It is automatic for finite outer period on \(R\), because \(\operatorname{Ct}(R)=\operatorname{Inn}(R)\).

**Corollary 5.2.** Automorphisms of \(R\) with finite outer period are classified up to outer conjugacy by the pair consisting of that period and its obstruction. Together with the aperiodic comparison theorem, every infinite outer-period automorphism of \(R\) belongs to the single aperiodic class.

*Proof.* Apply Theorem 5.1 using \(\operatorname{Aut}(R)=\overline{\operatorname{Inn}}R\) and \(\operatorname{Ct}(R)=\operatorname{Inn}(R)\). An infinite outer-period automorphism has asymptotic period zero by the latter equality, so the aperiodic comparison theorem applies. \(\square\)

## 6. Exercises with solutions

**Exercise 6.1 (introductory: invariant faithful state).** If \(\theta^p=\mathrm{id}\) and \(\rho\) is a faithful normal state, prove that \(p^{-1}\sum_{r=0}^{p-1}\rho\circ\theta^r\) is faithful and \(\theta\)-invariant.

*Solution.* Positivity, normality and normalization persist under the finite average. For \(x\geq0\), a zero average makes each nonnegative summand zero, including \(\rho(x)\); faithfulness gives \(x=0\). Composing with \(\theta\) cyclically permutes the summands.

**Exercise 6.2 (intermediate: the averaging constant).** Prove (3.2) for arbitrary normal \(\psi\), assuming commutator bounds \(a\) for \(u\) and \(b\) for \(v\).

*Solution.* Telescope each power to obtain \(\|[u^r,\psi]\|\leq ra\) and \(\|[v^s,\psi]\|\leq sb\). Composition by inner automorphisms is an isometry of the predual, so the product contributes at most \(ra+sb\). Averaging gives \(p^{-2}\sum_{r,s}(ra+sb)=(p-1)(a+b)/2\). With \(a,b\leq\varepsilon_v\), this is \((p-1)\varepsilon_v\leq p\varepsilon_v\).

**Exercise 6.3 (intermediate: the identity coordinate).** For \(p=3\), compute the image under (4.2) of \(\xi_2\otimes\xi_2\), and verify the conjugated clock eigenvalue on its image.

*Solution.* The image is \(\xi_1\otimes\xi_2\), since \(2+2=1\) modulo three. The old product clock eigenvalue was \(\lambda^4=\lambda\); the new \(c_3\otimes1\) eigenvalue is also \(\lambda\). The second coordinate contributes no phase.

**Exercise 6.4 (advanced: the next functional).** At stage \(v-1\), why does approximating only \(\psi_1,\ldots,\psi_{v-1}\) not provide the clock commutator estimate for \(\psi_v\) in this induction?

*Solution.* A clock implementing the residual \(\Theta\) has limiting commutator norm \(\|\psi_v\circ\Theta-\psi_v\|\). The previous-stage errors control this norm only for the functionals actually tested. An approximation test for \(\psi_v\) at stage \(v-1\) supplies (2.5) for that new functional. Without it, the residual might move \(\psi_v\) by a fixed positive amount; taking a later implementer would not make its commutator vanish.

**Exercise 6.5 (advanced: cancel the phase, not the automorphism).** Suppose \(p=3\) and \(\gamma=e^{2\pi i/3}\). Would tensoring \(a_\gamma\) with its inverse cancel its obstruction? What model does cancel it?

*Solution.* The inverse has the same obstruction \(\gamma\), by the direct implementing-phase computation in the obstruction lesson. Their tensor product therefore has obstruction \(\gamma^2\ne1\). The separately realized model \(a_{\overline\gamma}\) has obstruction \(\overline\gamma=\gamma^2\), and its tensor product with \(a_\gamma\) has obstruction \(\gamma\overline\gamma=1\). The slice criterion keeps its outer period equal to three.

## References

[Connes outer] Alain Connes, *Outer conjugacy classes of automorphisms of factors*, Annales scientifiques de l'École Normale Supérieure, série 4, 8 (1975), 383–419. Lemma 2.3.6, pp.406–407, gives general summable tensor splitting; Lemma 3.2.6, pp.415–416, gives the finite coefficient transfer. Theorem 2.3.1 supplies the absorption mechanism used by the prerequisites. [Article and original text](https://numdam.org/articles/10.24033/asens.1295/).

[Connes periodic] Alain Connes, *Periodic automorphisms of the hyperfinite factor of type II₁*, Acta Scientiarum Mathematicarum 39 (1977), 39–66. Theorem 5.1, pp.56–59, proves cyclic extraction on the hyperfinite II₁ factor. Theorem 6.2 and its proof, pp.60–61, identify the tensor-product law on outer classes with multiplication of the obstruction phases. The general-factor theorem here retains its additional exact-pair and normal-functional arguments. [Open original text](https://alainconnes.org/wp-content/uploads/szego.pdf).

[Takesaki II] Masamichi Takesaki, *Theory of Operator Algebras II*, Encyclopaedia of Mathematical Sciences 125, Springer, 2003, Proposition XI.2.26, pp.347–348. Historical source for the general finite free-action prerequisite behind exact cyclic pairs; its programme proof is linked above. [Publisher record](https://link.springer.com/book/10.1007/978-3-662-10451-4).

[Takesaki III] Masamichi Takesaki, *Theory of Operator Algebras III*, Encyclopaedia of Mathematical Sciences 127, Springer, 2003, Theorem XVII.3.16, pp.284–285, and Theorem XVII.3.20, pp.288–290. These give the general period/phase classification and cyclic extraction treated here. [Publisher record](https://link.springer.com/book/10.1007/978-3-662-10453-8).
