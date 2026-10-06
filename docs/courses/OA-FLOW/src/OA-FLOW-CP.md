# Concrete preduals from Hilbert tensors: the bounded CP-01–06 provider

*Retained original programme exposition: OpenAI Codex (AI), CC0-1.0. Exact prerequisite rebinding and this bounded selection: GPT-6 Astra (OpenAI), Ultra, 2026-10-04. Historical model variants are not inferred. See [component terms](../LICENSE.md) and the exact adoption record.*

This is an adoptable selection of the actual CP-01–06 proof bodies, with their Hilbert, Hahn–Banach and concrete-topology prerequisites rebound to precise local CF/SF proofs. It includes no CP-07–14 body or conclusion. It is not a newly invented account of the original development history. Every later use must refer to these earlier proofs and the exact corresponding normality convention.

<a id="oa-flow.cp.1"></a>

## OA-MOD-CP-01 — Conventions and the precise foundations

Inner products are linear in their first variable. Thus the vector coefficient of \(T\in B(H)\) is \(\langle T\xi,\eta\rangle\). The conjugate complex vector space \(\overline H\) has vectors \(\overline\eta\) and scalar action \(\lambda\overline\eta=\overline{\overline\lambda\eta}\). Its inner product is \(\langle\overline\xi,\overline\eta\rangle_{\overline H}=\overline{\langle\xi,\eta\rangle_H}\), and its norm is \(\|\overline\eta\|=\|\eta\|\).

The Hilbert inputs are now the local proofs in [SF-0 and SB-0](OA-FLOW-SF.md#oa-flow.shared-foundations.sf-0): orthogonal projection, Hilbert representation and bounded adjoints. A bounded sesquilinear form \(b\), linear in its first variable, has a unique representing bounded operator: for fixed \(\xi\), apply Hilbert representation to the conjugate-linear functional \(\eta\mapsto b(\xi,\eta)\), obtaining a vector \(T\xi\) with \(b(\xi,\eta)=\langle T\xi,\eta\rangle\). Uniqueness proves linearity of \(T\), and the form bound proves boundedness with the same least bound. This proves the bounded-form input for arbitrary Hilbert spaces, including zero spaces.

We use the complete real and complex norm-preserving Hahn–Banach proof in [CF Section 1](OA-FLOW-CF.md#OA-FLOW.CF.1). For \(z\ne0\), extend the functional \(\lambda z\mapsto\lambda\|z\|\). This gives
\[
\|z\|=\sup_{\|f\|\le1}|f(z)|,\qquad f\in X^*,
\tag{CP.1}
\]
for every real or complex normed space \(X\); for \(z=0\) it is immediate.

Here are the completion facts used below, so no trace-class or tensor-completion theorem is hidden in the construction. For a normed space \(X\), take Cauchy sequences in \(X\), identify two when the norm of their difference tends to zero, and set \(\|[x_n]\|=\lim_n\|x_n\|\). The reverse triangle inequality makes this well-defined, and the finite norm identities pass to limits. Constant sequences embed \(X\) isometrically and densely: \([x_n]\) is approximated by the constant sequences \(x_n\). The resulting space is complete. Indeed, from a Cauchy sequence of classes select a subsequence whose successive distances are at most \(2^{-k}\), and choose a vector of \(X\) within \(2^{-k}\) of its \(k\)-th class. These vectors form a Cauchy sequence in \(X\); its class is the limit of that subsequence, hence of the original Cauchy sequence. A bounded linear map from \(X\) to a Banach space extends uniquely to the completion by taking limits; density preserves its norm.

For reference, \(\ell^2(H)\) consists of sequences \(\xi=(\xi_n)\) with \(\sum_n\|\xi_n\|^2<\infty\), with the sum inner product. Cauchy–Schwarz for finite sums, followed by limits, proves convergence of the inner product and its usual identities. This is a Hilbert space. For a Cauchy sequence in it, take the coordinatewise limits in \(H\). The Cauchy estimates on every finite partial sum pass to those limits and then to their supremum, proving that the limit sequence is square summable and that convergence holds in the sum norm. No basis of \(H\) is used.

The ultraweak topology of \(B(H)\) is defined by the vector-series tests \(\sum_n\langle x\xi_n,\eta_n\rangle\) with square-summable vector sequences; their absolute convergence follows from Cauchy–Schwarz. The weak operator topology uses single vector coefficients and is therefore weaker. Commutation with any fixed bounded operator is weak-operator closed by its vector-pairing identities, so a bicommutant is weak-operator closed. An algebra already specified as weak-operator closed is ultraweakly closed because its complement is open also for the finer topology. These elementary facts replace all BK topology references actually needed by CP-01–06. No order-normality, support, positive extension, compactness, separation of convex sets or result from CP-07–14 is used.

<a id="oa-flow.cp.2"></a>

## OA-MOD-CP-02 — The projective norm is a genuine norm

Let \(V=H\otimes_{\mathbb C}\overline H\) be the algebraic tensor product: the free complex vector space on pairs \((\xi,\overline\eta)\), divided by the bilinearity relations. A bilinear function of those two variables therefore defines a unique linear function on \(V\).

Define
\[
\pi(u)=\inf\left\{
 \sum_{j=1}^m\|\xi_j\|\|\eta_j\|:
 u=\sum_{j=1}^m\xi_j\otimes\overline{\eta_j}
\right\}.
\tag{CP.2}
\]
The zero sum is allowed. Every tensor has a finite representation, so this is finite. Rescaling representations proves absolute homogeneity; concatenating representations within any prescribed error of the two infima proves the triangle inequality.

For nondegeneracy, write a given tensor using finite-dimensional spans of its first and second vectors, and choose orthonormal bases \(e_1,\ldots,e_r\) and \(f_1,\ldots,f_s\) for those spans. Expansion gives
\[
u=\sum_{i,j}c_{ij}\,e_i\otimes\overline{f_j}.
\]
The bilinear coefficient test
\[
L_{ij}(\xi\otimes\overline\eta)
  =\langle\xi,e_i\rangle\langle f_j,\eta\rangle
\]
has \(|L_{ij}(u)|\le\pi(u)\), since its value on a pure tensor is at most \(\|\xi\|\|\eta\|\). It reads off \(c_{ij}\). If \(u\ne0\), some coefficient is nonzero: an expansion with all coefficients zero is the zero tensor. Thus \(\pi(u)>0\).

The same test with \(e=\xi/\|\xi\|\) and \(f=\eta/\|\eta\|\), when neither vector is zero, proves
\[
\pi(\xi\otimes\overline\eta)=\|\xi\|\|\eta\|.
\tag{CP.3}
\]
If a factor is zero, both sides vanish. Only finite-dimensional orthonormal bases were used.

Let \(E_H\) be the Banach completion of \((V,\pi)\) constructed in CP-01. We do not identify this completion with a space of trace-class operators.

<a id="oa-flow.cp.3"></a>

## OA-MOD-CP-03 — Its dual is exactly \(B(H)\)

For \(T\in B(H)\), define on algebraic tensors
\[
\Phi_T\left(\sum_j\xi_j\otimes\overline{\eta_j}\right)
 =\sum_j\langle T\xi_j,\eta_j\rangle.
\]
Bilinearity makes this independent of the representation. Taking the infimum of the bound over all representations gives
\(|\Phi_T(u)|\le\|T\|\pi(u)\), so \(\Phi_T\) extends to \(E_H\).

Conversely, \(F\in E_H^*\) defines
\(b(\xi,\eta)=F(\xi\otimes\overline\eta)\).
This is sesquilinear with
\(|b(\xi,\eta)|\le\|F\|\|\xi\|\|\eta\|\).
The bounded-form Hilbert import supplies a unique \(T\in B(H)\) representing \(b\). Equality on algebraic tensors and density give \(F=\Phi_T\). Finally,
\[
\|\Phi_T\|
\ge\sup_{\|\xi\|\le1,\ \|\eta\|\le1}
 |\langle T\xi,\eta\rangle|
=\|T\|.
\]
Here (CP.3) justifies the test tensors; no norm-attaining vector for \(T\) is presumed. Together with the upper bound this proves a complex-linear onto isometry
\[
B(H)\cong E_H^*,\qquad T\longmapsto\Phi_T.
\tag{CP.4}
\]
All assertions include \(H=\{0\}\). Injectivity of a completed map from \(E_H\) into an operator space is neither assumed nor needed.

<a id="oa-flow.cp.4"></a>

## OA-MOD-CP-04 — Every tensor vector is a summable vector series

**Lemma.** Every \(u\in E_H\) has a norm-convergent representation
\[
u=\sum_{n=1}^\infty\xi_n\otimes\overline{\eta_n},
\qquad
\sum_n\|\xi_n\|\|\eta_n\|<\infty.
\tag{CP.5}
\]
The factors can be chosen so that both sequences lie in \(\ell^2(H)\).

**Proof.** Choose algebraic \(v_k\) with \(\|u-v_k\|\le2^{-k}\). Put \(d_1=v_1\) and \(d_k=v_k-v_{k-1}\) for \(k\ge2\). Then \(\sum_k\pi(d_k)<\infty\), since
\(\pi(d_k)\le2^{-k}+2^{-(k-1)}\) for \(k\ge2\).
Represent each \(d_k\) as a finite sum with total cost at most \(\pi(d_k)+2^{-k}\). List those finite sums consecutively. Their total cost is finite; (CP.3) and completeness imply absolute convergence. The partial sums at the block ends are \(v_k\), so the sum is \(u\).

Discard zero terms and replace each remaining pair by
\[
\xi'_n=\left(\frac{\|\eta_n\|}{\|\xi_n\|}\right)^{1/2}\xi_n,
\qquad
\eta'_n=\left(\frac{\|\xi_n\|}{\|\eta_n\|}\right)^{1/2}\eta_n.
\]
The positive real multipliers are reciprocal, so the tensor is unchanged. Both new squared norms equal the original product \(\|\xi_n\|\|\eta_n\|\). The two new sequences are square summable. ∎

Conversely, \(\xi,\eta\in\ell^2(H)\) define a vector of \(E_H\) by (CP.5), since scalar Cauchy–Schwarz bounds the sum of the products. Evaluation gives
\[
\Phi_T(u)=\sum_n\langle T\xi_n,\eta_n\rangle.
\tag{CP.6}
\]
Thus \(\sigma(B(H),E_H)\) is exactly the ultraweak topology defined by the vector-series tests in CP-01. This equality holds on all of \(B(H)\), without a norm-bound restriction.

<a id="oa-flow.cp.5"></a>

## OA-MOD-CP-05 — Quotients and annihilators, with the norm checks

Let \(E\) be a Banach space and \(F\subseteq E\) a closed linear subspace. The quotient norm on \(Q=E/F\) is
\[
\|e+F\|_Q=\inf_{f\in F}\|e+f\|.
\]
Norm zero means \(e\) belongs to the closure of \(F\), hence to \(F\); its other norm properties follow by adding and rescaling representatives.

The quotient is complete. Given a Cauchy sequence in \(Q\), select a subsequence \(z_k\) with
\(\|z_{k+1}-z_k\|_Q\le2^{-k}\).
Choose representatives \(d_k\in E\) of those differences with
\(\|d_k\|\le2^{1-k}\), and a representative \(e_1\) of \(z_1\).
The convergent series \(e_1+\sum_kd_k\) represents the limit of the subsequence. The Cauchy property gives convergence of the full sequence.

For the quotient map \(q:E\to Q\), composition gives an onto isometry
\[
q^*:Q^*\longrightarrow F^\perp
 =\{T\in E^*:T|_F=0\}.
\tag{CP.7}
\]
Indeed, a functional annihilating \(F\) defines a functional on \(Q\). Taking the infimum over representatives bounds its quotient norm by its norm on \(E\). The reverse bound follows because \(q\) is contractive. The same bounds prove that composition is isometric.

If a linear subspace \(M\subseteq E^*\) is weak-star closed, then
\[
M=(M_\perp)^\perp,\qquad
M_\perp=\{e\in E:T(e)=0\ \text{for all }T\in M\}.
\tag{CP.8}
\]
For the nontrivial inclusion, take \(T_0\notin M\). A basic weak-star neighborhood disjoint from \(M\) tests finitely many vectors \(e_1,\ldots,e_n\). Let
\(L(T)=(T(e_1),\ldots,T(e_n))\).
Then \(L(T_0)\notin L(M)\), since equality would put an element of \(M\) in that neighborhood. Finite-dimensional linear algebra supplies \(\lambda\) on \(\mathbb C^n\) vanishing on \(L(M)\) but not at \(L(T_0)\). Write \(\lambda(z)=\sum_jc_jz_j\). The vector \(e=\sum_jc_je_j\) belongs to \(M_\perp\), but \(T_0(e)\ne0\). This proves (CP.8) without locally convex separation.

<a id="oa-flow.cp.6"></a>

## OA-MOD-CP-06 — The concrete predual and its intrinsic norm

Let \(M\subseteq B(H)\) be a weak operator closed unital \*-subalgebra. It is ultraweakly closed by CP-01. Under (CP.4), define
\[
F=M_\perp\subseteq E_H,\qquad M_*=E_H/F.
\tag{CP.9}
\]
The subspace \(F\) is norm closed, being an intersection of kernels of bounded functionals. Equations (CP.7)–(CP.8) prove that canonical evaluation is an onto isometry
\[
M\cong(M_*)^*.
\tag{CP.10}
\]

Identify \(u+F\) with \(x\mapsto\Phi_x(u)\) on \(M\). This is injective by the definition of \(F\). Its operator norm is exactly the quotient norm: apply the norming identity (CP.1) to \(M_*\), and identify its dual unit ball with the unit ball of \(M\) by (CP.10). Thus \(M_*\) is an isometric Banach subspace of \(M^*\), and is norm closed there.

By CP-04 its elements are exactly the restricted vector-series functionals
\[
f(x)=\sum_n\langle x\xi_n,\eta_n\rangle,\qquad
\xi,\eta\in\ell^2(H).
\tag{CP.11}
\]
The weak-star topology from this pairing is therefore the inherited ultraweak topology.

Moreover \(M_*\) is exactly the space of ultraweakly continuous complex-linear functionals. One inclusion is immediate. For the other, continuity of a linear \(f\) implies that it vanishes whenever finitely many controlling vector-series functionals \(f_1,\ldots,f_r\) all vanish: rescale such a vector and use continuity at zero. Hence \(f\) factors through
\(x\mapsto(f_1(x),\ldots,f_r(x))\).
A linear functional on this finite-dimensional image extends algebraically to \(\mathbb C^r\), so \(f\) is a finite linear combination of the \(f_j\). It belongs to \(M_*\).

This establishes a concrete predual and its topology. It does not prove uniqueness among arbitrary abstract Banach preduals or construct the bidual W* algebra of a general C\*-algebra.

