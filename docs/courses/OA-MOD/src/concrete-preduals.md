# Concrete preduals from Hilbert tensors

**Self-checked by the writing AI.**

A predual turns the ultraweak topology into a weak-star topology. This unit constructs that Banach space directly from pairs of Hilbert-space vectors. It proves concrete duality, its positive-functional and corner consequences, and the continuous-dual statements needed for sigma-strong topologies. Every Hilbert space is arbitrary. Countable series describe individual functionals; they do not impose separability on the Hilbert space.

## Conventions and the precise foundations

Inner products are linear in their first variable. Thus the vector coefficient of \(T\in B(H)\) is \(\langle T\xi,\eta\rangle\). The conjugate complex vector space \(\overline H\) has vectors \(\overline\eta\) and scalar action \(\lambda\overline\eta=\overline{\overline\lambda\eta}\). Its inner product is \(\langle\overline\xi,\overline\eta\rangle_{\overline H}=\overline{\langle\xi,\eta\rangle_H}\), and its norm is \(\|\overline\eta\|=\|\eta\|\).

The Hilbert inputs are proved in The bounded prerequisite boundary: Hilbert representation and bounded operators. Every bounded sesquilinear form \(b\), linear in its first variable, has a unique representation \(b(\xi,\eta)=\langle T\xi,\eta\rangle\), and its least bound is \(\|T\|\). These written results apply to arbitrary complex Hilbert spaces, including zero spaces. Its real-to-complex Riesz conversion, bounded-form construction, adjoints and completion proof supply all of these results. The finite orthonormal-basis and linear-annihilator steps used in CP-02 and CP-05 are written at the end of NP1.

We also use **CP-DEP-HB**, real and complex norm-preserving Hahn–Banach extension, whose full dominated-extension argument, complex conversion and norming consequence are proved in NP1. For \(z\ne0\), extend the functional \(\lambda z\mapsto\lambda\|z\|\). This gives

\[
\|z\|=\sup_{\|f\|\le1}|f(z)|,\qquad f\in X^*,
\tag{CP.1}
\]

for every real or complex normed space \(X\); for \(z=0\) it is immediate. The one-dimensional extension just proved in NP1 gives this norming identity directly.

Here are the completion facts used below, so no trace-class or tensor-completion theorem is hidden in the construction. For a normed space \(X\), take Cauchy sequences in \(X\), identify two when the norm of their difference tends to zero, and set \(\|[x_n]\|=\lim_n\|x_n\|\). The reverse triangle inequality makes this well-defined, and the finite norm identities pass to limits. Constant sequences embed \(X\) isometrically and densely: \([x_n]\) is approximated by the constant sequences \(x_n\). The resulting space is complete. Indeed, from a Cauchy sequence of classes select a subsequence whose successive distances are at most \(2^{-k}\), and choose a vector of \(X\) within \(2^{-k}\) of its \(k\)-th class. These vectors form a Cauchy sequence in \(X\); its class is the limit of that subsequence, hence of the original Cauchy sequence. A bounded linear map from \(X\) to a Banach space extends uniquely to the completion by taking limits; density preserves its norm.

For reference, \(\ell^2(H)\) consists of sequences \(\xi=(\xi_n)\) with \(\sum_n\|\xi_n\|^2<\infty\), with the sum inner product. Cauchy–Schwarz for finite sums, followed by limits, proves convergence of the inner product and its usual identities. This is a Hilbert space. For a Cauchy sequence in it, take the coordinatewise limits in \(H\). The Cauchy estimates on every finite partial sum pass to those limits and then to their supremum, proving that the limit sequence is square summable and that convergence holds in the sum norm. No basis of \(H\) is used.

Bounded functional calculus and concrete operator topology are proved in **OA-MOD-BK-01**, **OA-MOD-BK-03** and **OA-MOD-BK-04**. The convex-closure corollary uses NP2: point separation in arbitrary real locally convex spaces; the bounded support theorem uses NP3 and its written BK prerequisites. Weak-star compactness and Krein–Smulian are not assumed or proved in the predual construction.

## The projective norm is a genuine norm

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

## Its dual is exactly \(B(H)\)

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
The bounded-form proof in BK-01 supplies a unique \(T\in B(H)\) representing \(b\). Equality on algebraic tensors and density give \(F=\Phi_T\). Finally,

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

## Every tensor vector is a summable vector series

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

Thus \(\sigma(B(H),E_H)\) is exactly the ultraweak topology defined by the vector-series tests in OA-MOD-BK-03. This equality holds on all of \(B(H)\), without a norm-bound restriction.

## Quotients and annihilators, with the norm checks

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

## The concrete predual and its intrinsic norm

Let \(M\subseteq B(H)\) be a weak operator closed unital *-subalgebra. It is ultraweakly closed by OA-MOD-BK-03. Under (CP.4), define

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

This establishes a concrete predual and its topology. It does not prove uniqueness among arbitrary abstract Banach preduals or construct the bidual W* algebra of a general C*-algebra.

## Positive functionals, closed cones and norm closure

Write \(M_*^+\) for the positive functionals in \(M_*\). For \(\xi\in\ell^2(H)\),

\[
\omega_\xi(x)=\sum_n\langle x\xi_n,\xi_n\rangle
\]

belongs to \(M_*^+\). These functionals separate \(M_+\): if \(a\ge0\) is nonzero, some \(\xi\in H\) satisfies
\(\langle a\xi,\xi\rangle=\|a^{1/2}\xi\|^2>0\).
Single-vector tests also detect positivity of arbitrary operators: nonnegative real diagonal coefficients imply self-adjointness by polarization and then positivity.

Every \(f\in M_*\) is a linear combination of four positive members. Use (CP.11) and put

\[
\omega_k(x)=\sum_n
 \langle x(\xi_n+i^k\eta_n),\,\xi_n+i^k\eta_n\rangle,
 \qquad k=0,1,2,3.
\]

Each sequence is square summable. Expansion gives

\[
f=\frac14\sum_{k=0}^3 i^k\omega_k.
\tag{CP.12}
\]

The identity holds for any sesquilinear form; no self-adjointness of \(x\) is required.

For a positive linear functional \(\omega\), positive/negative parts show that it is real on self-adjoint elements and preserves adjoints. Applying positivity to
\(\omega((x+\lambda y)^*(x+\lambda y))\) for every complex \(\lambda\) gives

\[
|\omega(y^*x)|^2\le\omega(x^*x)\omega(y^*y).
\tag{CP.13}
\]

If the second diagonal value is positive, minimize the scalar quadratic polynomial in \(\lambda\); if it is zero, varying the magnitude and argument of \(\lambda\) forces the mixed coefficient to vanish. With \(y=1\) and \(x^*x\le\|x\|^2 1\), this proves boundedness and

\[
|\omega(x)|\le\omega(1)\|x\|,\qquad
\|\omega\|=\omega(1).
\tag{CP.14}
\]

The reverse norm inequality tests \(1\); the zero algebra is immediate. In particular, for \(0\le\psi\le\omega\),

\[
\|\omega-\psi\|=\omega(1)-\psi(1).
\tag{CP.15}
\]

The positive cone of \(M\) is ultraweakly closed, as the intersection of the conditions
\(\langle x\xi,\xi\rangle\in[0,\infty)\).
Every closed norm ball is ultraweakly closed, since

\[
\|x\|\le R
\quad\Longleftrightarrow\quad
|\langle x\xi,\eta\rangle|\le R\|\xi\|\|\eta\|
\quad(\xi,\eta\in H).
\]

The adjoint is conjugate-linear and ultraweakly continuous:

\[
\sum_n\langle x^*\xi_n,\eta_n\rangle
=\overline{\sum_n\langle x\eta_n,\xi_n\rangle}.
\]

Fixed multiplication is ultraweakly continuous by BK-03.

Norm closure of \(M_*\) in CP-06 has a useful concrete interpretation: a norm-Cauchy sequence in the isometric quotient has a limit there; the associated functionals converge in operator norm. Any operator-norm limit in \(M^*\) must be that same predual functional. Positivity survives norm limits by evaluation on each positive element, so \(M_*^+\) is norm closed.

Finally, every \(\omega\in M_*^+\) preserves bounded increasing positive suprema. If \(a_\alpha\uparrow a\), BK-04 supplies ultraweak convergence, whence
\(\omega(a_\alpha)\uparrow\omega(a)\).
This proves the ultraweak-to-order direction without a theorem about weights. The converse is not an input to this unit.

## The sigma-strong seminorms are vector seminorms

For \(\xi\in\ell^2(H)\), set

\[
q_\xi(x)=\left(\sum_n\|x\xi_n\|^2\right)^{1/2}.
\]

This is a seminorm and
\(q_\xi(x)^2=\omega_\xi(x^*x)\).
Thus it is one of the seminorms

\[
p_\omega(x)=\omega(x^*x)^{1/2},\qquad \omega\in M_*^+,
\]

which are seminorms by (CP.13).

Conversely, choose a mixed series (CP.11) for \(\omega\in M_*^+\). For \(a\ge0\), Cauchy–Schwarz for \(a^{1/2}\) and \(2uv\le u^2+v^2\) give

\[
0\le\omega(a)\le
\frac12\sum_n\bigl(\langle a\xi_n,\xi_n\rangle+
                  \langle a\eta_n,\eta_n\rangle\bigr)
=:\theta(a).
\tag{CP.16}
\]

All sums converge absolutely and \(\theta\in M_*^+\). If \(\zeta\) concatenates \(\xi/\sqrt2\) and \(\eta/\sqrt2\), then
\(p_\omega(x)\le q_\zeta(x)\).
Therefore the sigma-strong topology generated by the \(p_\omega\) is exactly the topology generated by the \(q_\xi\). Adding the seminorms at \(x^*\) gives the sigma-strong* topology.

This proof does not assume that a positive predual functional itself extends as a positive vector series on \(B(H)\). Domination by \(\theta\) suffices.

On a norm-bounded set, strong operator convergence is equivalent to sigma-strong convergence. If \(x_\alpha\to x\) strongly and \(\|x_\alpha\|,\|x\|\le R\), the tail of
\(\sum_n\|(x_\alpha-x)\xi_n\|^2\)
is at most \(4R^2\sum_{n>N}\|\xi_n\|^2\); the finite initial sum tends to zero. This proves the forward implication, while single-vector tests prove the reverse. Applying the argument also to adjoints gives the analogous strong* and sigma-strong* statement.

## The two continuous complex duals

**Theorem.** The continuous complex-linear dual of each of the sigma-strong and sigma-strong* topologies is exactly \(M_*\).

**Proof for sigma-strong.** The estimate

\[
\left|\sum_n\langle x\xi_n,\eta_n\rangle\right|
\le q_\xi(x)\|\eta\|_{\ell^2}
\]

makes every member of \(M_*\) continuous.

Conversely, continuity at zero and homogeneity bound a continuous linear \(f\) by a constant times the maximum of finitely many defining seminorms. Concatenating their sequences gives
\(|f(x)|\le Cq_\xi(x)\)
for some \(\xi\in\ell^2(H)\). When the controlling seminorm vanishes, scaling forces \(f(x)=0\). Hence

\[
(x\xi_n)_n\longmapsto f(x)
\]

is well-defined and bounded on its linear image in \(\ell^2(H)\). Extend it continuously to the closure of that image. The Riesz representation proof in BK-01, applied to that closed Hilbert subspace, supplies \(\eta\in\ell^2(H)\) with
\(f(x)=\sum_n\langle x\xi_n,\eta_n\rangle\).
Thus \(f\in M_*\).

**Proof for sigma-strong*.** The forward inclusion remains true because this topology is finer. For the reverse, continuity and concatenation give

\[
|f(x)|\le C\bigl(q_\xi(x)^2+q_\eta(x^*)^2\bigr)^{1/2}.
\]

Use the complex-linear map

\[
J(x)=\bigl((x\xi_n)_n,\ \overline{(x^*\eta_n)_n}\bigr)
\in\ell^2(H)\oplus\overline{\ell^2(H)}.
\]

The conjugate space is essential: \(x\mapsto x^*\eta_n\) alone is conjugate-linear. Factor \(f\) through the image of \(J\), extend to its closure, and apply the Riesz proof in BK-01. There exist \(u,v\in\ell^2(H)\) with

\[
\begin{aligned}
f(x)&=\sum_n\langle x\xi_n,u_n\rangle
     +\sum_n\langle v_n,x^*\eta_n\rangle\\
    &=\sum_n\langle x\xi_n,u_n\rangle
     +\sum_n\langle xv_n,\eta_n\rangle.
\end{aligned}
\]

Concatenation is a vector-series representation, so \(f\in M_*\). ∎

Equal continuous duals do not mean that the topologies themselves are equal.

## Real duals and the convex-closure consequence

On the underlying real space of \(M\), a continuous real-linear \(r\) has continuous complexification

\[
f(x)=r(x)-i\,r(ix).
\]

Thus the common continuous real dual for these three topologies is
\(\{\operatorname{Re}f:f\in M_*\}\).

On \(M_{\rm sa}\), sigma-strong and sigma-strong* coincide. Suppose \(r\) is continuous real linear there. After finite concatenation,
\(|r(a)|\le Cq_\xi(a)\) for self-adjoint \(a\). Define

\[
f(x)=r\left(\frac{x+x^*}{2}\right)
+i\,r\left(\frac{x-x^*}{2i}\right).
\]

It is complex linear and agrees with \(r\) on self-adjoint elements. The bound

\[
|f(x)|\le C\bigl(q_\xi(x)+q_\xi(x^*)\bigr)
\]

makes it sigma-strong* continuous, hence a member of \(M_*\) by CP-09. It is hermitian. Conversely every hermitian predual functional restricts to a continuous real functional on \(M_{\rm sa}\) for all three topologies. Ultraweak continuity already implies sigma-strong continuity, so these exhaust the ultraweak real dual as well.

The argument does not presume that \(x\mapsto(x+x^*)/2\) is sigma-strong continuous on the full algebra.

**Convex-closure corollary.** By the full real locally convex separation and half-space proof in NP2, a convex subset of \(M\) has the same closure for the ultraweak, sigma-strong and sigma-strong* topologies. The same holds for convex subsets of \(M_{\rm sa}\). The empty convex set is closed for all three topologies. For a nonempty convex set, each closure is the intersection of closed half-spaces defined by its continuous real functionals; the dual identifications make those half-spaces identical. NP2 proves precisely this separation conclusion at arbitrary locally convex generality. There is no boundedness or sequential-closure restriction. Banach–Alaoglu and Krein–Smulian are different parts of that broader contract and are not needed for this conclusion.

## Corners have exactly their inherited predual

Let \(p\in M\) be a projection and let \(N=pMp\) act on \(pH\). It is a concrete von Neumann algebra there. To verify closedness, extend a weak operator convergent net on \(pH\) by zero on \((1-p)H\). The extensions converge weakly on \(H\), so a net from \(pMp\) has its limit in \(M\) and still satisfies \(x=pxp\).

Let \(j:N\to M\) be this inclusion, and let \(C:M\to N\) be \(C(x)=pxp\). Both are contractions and \(Cj=\operatorname{id}_N\). A vector-series functional on \(N\) extends through \(C\) using the same sequences in \(H\). Restricting a series from \(M\) through \(j\) replaces both vector sequences by their images under \(p\). Hence the ultraweak topology on \(N\) is exactly the inherited topology.

The maps

\[
r:M_*\to N_*,\quad r(f)=f\circ j,\qquad
s:N_*\to M_*,\quad s(g)=g\circ C
\]

are contractions, \(rs=1\), and \(s\) is isometric: restriction gives the reverse norm inequality. They preserve positivity. Every \(g\in N_*\) has an extension of exactly its norm, and therefore

\[
N_*\cong M_*/\ker r
\cong\operatorname{ran}P_*,
\qquad P_*f(x)=f(pxp),
\tag{CP.17}
\]

isometrically, where \(P_*=sr\) is a contractive idempotent. The second identification uses \(s\); a quotient is not identified with a subspace without a specified map.

At tensor level, \(p\otimes\overline p\) is contractive by (CP.2), extends to the completions, and gives the compression formulas. The construction includes \(p=0\), requires no centrality, and uses no characterization of normal maps.

## Supports and the direction toward normal weights

Let \(\omega\in M_*^+\). It is positive and ultraweakly continuous by CP-06, so the written bounded positive-functional support proof NP3 applies. That proof constructs finite joins of null projections by BK-06 range supports, then uses BK-04 for their arbitrary increasing-net supremum and proves that the limit is a projection. It gives the largest null projection and faithful complementary corner directly. Its inputs are bounded Hilbert calculus, concrete operator topologies and bounded monotone nets. No predual duality, universal-bidual construction, general weight support or NW converse is an input. The word normal in NP3 means ultraweak continuity.

The support proof supplies a largest projection \(q\) with \(\omega(q)=0\), and says that \(\omega\) is faithful on \(pMp\), where \(p=1-q\). Here is the compression consequence with our conventions. Cauchy–Schwarz (CP.13) gives

\[
|\omega(xq)|^2\le\omega(q)\,\omega(xx^*)=0,
\qquad x\in M.
\]

Since a positive functional preserves adjoints, \(\omega(qx)=\overline{\omega(x^*q)}=0\). Expanding \(x=(p+q)x(p+q)\) therefore proves

\[
\omega(x)=\omega(pxp),\qquad x\in M.
\]

This \(p\) is the least projection with that identity: if \(\omega(x)=\omega(exe)\) for every \(x\), then \(\omega(1-e)=0\), so \(1-e\le q\) and \(p\le e\). The zero functional has support zero. A nonzero functional can be normalized on its support corner by (CP.14), and CP-11 supplies its exact corner predual and inherited topology. No centrality of \(p\) is assumed.

CP-07 also proves order normality directly. As a finite-valued normal weight, \(\omega\) has all positive elements in its finite domain and finite-domain projection \(1\). Its weight support is therefore the same \(p\). The general, possibly infinite-valued null-projection and compression results WS-04–05 remain separate. They are not inputs to the bounded support proof or to the predual construction.

There is a later consequence, **conditional on the independent normal-weight characterization NW proving recovery from dominated normal positive functionals**. If a bounded positive order-normal \(\omega\) satisfies

\[
\omega(a)=\sup\{\psi(a):\psi\in M_*^+,\ \psi\le\omega\},
\]

choose \(\psi_n\le\omega\) with \(\psi_n(1)\to\omega(1)\). Equation (CP.15) gives
\(\|\omega-\psi_n\|\to0\), so norm closure of \(M_*\) puts \(\omega\) in \(M_*^+\). If \(\omega(1)=0\), it is already zero. This is a route from the completed NW theorem to the scalar order-normal-to-ultraweak implication. It is not used to construct the predual, prove CP-08–11, or justify an input of NW.

## Examples and exercises with solutions

**Example: a vector state without separability.** Let \(H=\ell^2(I)\), where \(I\) is any nonempty set, and choose \(i_0\in I\). The tensor
\(e_{i_0}\otimes\overline{e_{i_0}}\)
defines the positive norm-one functional
\(\omega(x)=\langle xe_{i_0},e_{i_0}\rangle\).
Its support is the rank-one projection onto \(\mathbb Ce_{i_0}\). The corner is scalar even if \(I\) is uncountable. This one state does not imply existence of a faithful state on \(B(H)\).

**Exercise 1: a pure tensor's functional norm.** For \(\xi,\eta\in H\), prove that \(f(x)=\langle x\xi,\eta\rangle\) on \(B(H)\) has norm \(\|\xi\|\|\eta\|\).

**Solution.** Cauchy–Schwarz gives the upper bound. If both vectors are nonzero, the norm-one rank-one operator

\[
Tx=\left\langle x,\frac{\xi}{\|\xi\|}\right\rangle
 \frac{\eta}{\|\eta\|}
\]

gives \(f(T)=\|\xi\|\|\eta\|\). If a vector is zero, the functional is zero.

**Exercise 2: the inherited quotient norm.** For \(M=\mathbb CI_H\), \(H\ne0\), identify \(M_*\) and its norm using the tensor quotient.

**Solution.** Restriction sends \(u\) to \(c=\Phi_I(u)\), since its value at \(\lambda I\) is \(\lambda c\). The kernel is \(M_\perp\). The quotient norm is \(|c|\): one inequality follows from \(|\Phi_I(u)|\le\|u\|\), and the other from the representative \(c\,\xi\otimes\overline\xi\) for any unit vector \(\xi\). Different tensors can therefore define the same restricted functional.

**Exercise 3: closure versus compactness.** Does the proof that norm balls are ultraweakly closed also prove they are compact?

**Solution.** CP-07 expresses the ball as an intersection of closed coefficient inequalities, proving closedness only. Weak-star compactness needs Banach–Alaoglu, a separately retained part of NW-DEP-CONVEX.

**Exercise 4: compressing a mixed series.** Give the extension and restriction formulas in CP-11.

**Solution.** For \(y=pyp\), restriction of \(f(x)=\sum_n\langle x\xi_n,\eta_n\rangle\) is
\(f(y)=\sum_n\langle y(p\xi_n),p\eta_n\rangle\).
A corner functional with vectors in \(pH\) extends by the same expression in \(x\), whose value is unchanged when \(x\) is replaced by \(pxp\). These formulas give both topology directions.

## Exact exports and remaining boundaries

CP-02–06 supply the concrete part of **OA-MOD-DEP-PREDUAL**: a Banach predual, onto isometric evaluation duality, and the specified ultraweak topology. CP-07, CP-11 and the complete bounded support proof NP3 and compression argument in CP-12 supply the positive-functional, support and corner clauses of **OA-MOD-NW-DEP-DUAL**. CP-08–10 supply the continuous-dual assertions of **OA-MOD-NW-DEP-TOPO**; its convex-closure consequence uses the full real locally convex separation proof NP2 linked in CP-10.

This unit does not prove uniqueness of arbitrary abstract preduals, Sakai's abstract representation theorem, the universal C*-bidual construction, Banach–Alaoglu or Krein–Smulian. It does not use the scalar order-normal-to-ultraweak converse. These distinctions keep the remaining BIDUAL and convex-analysis obligations visible.

The projective-tensor argument is a written classical functional-analysis construction. BK-01 and NP1–NP3 now supply its Hilbert, norm-extension, convex-separation and bounded-support prerequisites in this package. The free [mathlib norm-extension and norming formulations](https://github.com/leanprover-community/mathlib4/blob/71a80585ee495fc24472fd0eaffc89d94e4fd8d6/Mathlib/Analysis/Normed/Module/HahnBanach.lean#L44) retain their Apache-2.0 provenance; no Lean code, comments or source prose are copied. The needed proofs are written in NP1. The broader course remains incomplete; concrete predual duality does not supply the abstract-predual or universal-bidual theorems.
