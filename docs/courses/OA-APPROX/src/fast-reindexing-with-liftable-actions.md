# Fast reindexing with liftable actions

*Written by GPT-6.1 Sol (OpenAI), Ultra, September 2026. Self-checked by the writing AI. New original text: public domain (CC0).*

Reindexing lets a separable part of an ultraproduct move farther out along its representatives. The finite tests must preserve multiplication, the multiplier condition and the desired action. This lesson proves the fast construction with hypotheses that survive the [semi-lift counterexample](ultraproduct-expectations-and-semilift-ambiguity.md#proposition-5-1).

Let \(M\) have separable predual and a faithful normal state \(\varphi\). It need not be a factor or finite. Use the [multiplier ultraproduct](multiplier-ultraproducts-and-normal-embeddings.md) \(M^\omega=N_\omega/I_\omega\), its normal centralizing subalgebra \(M_\omega\), and the [canonical expectation](ultraproduct-expectations-and-semilift-ambiguity.md#theorem-1-1) \(E_\omega:M^\omega\to M\). Write \(\|\cdot\|_\#\) for the symmetric seminorm associated to \(\varphi\), and \(\|\cdot\|_{\varphi^\omega,\#}\) for its quotient version. On bounded subsets these describe strong* convergence.

## 1. The corrected theorem

**Theorem 1.1.** Let \(P,Q\subset M^\omega\) be von Neumann subalgebras with separable predual. Let \(G\) be a countable group of **liftable** automorphisms of \(M^\omega\), meaning constant lifts \(\theta^\omega\) of normal automorphisms \(\theta\) of \(M\). Suppose \(G\) leaves \(P\) invariant. There is a normal unital injective *-homomorphism \(\Phi:P\to M^\omega\) such that
\[
\begin{aligned}
\Phi(x)&=x &&(x\in P\cap M),\\
\Phi(P\cap M_\omega)&\subset Q'\cap M_\omega,\\
E_\omega(a\Phi(x))&=E_\omega(a)E_\omega(x)
&&(x\in P,\ a\in Q),\\
\theta^\omega\Phi(x)&=\Phi(\theta^\omega(x))
&&(x\in P,\ \theta^\omega\in G).
\end{aligned}
\tag{1}
\]
In particular \(E_\omega\Phi=E_\omega|_P\), and \(\Phi\) preserves the faithful normal state \(\varphi^\omega|_P\).

The expectation identity keeps the nonfactor and nontracial cases. For a factor and \(x\in P\cap M_\omega\), it implies
\[
\varphi^\omega(a\Phi(x))
=\varphi^\omega(a)\tau_\omega(x).
\tag{2}
\]
For \(a\in Q\cap M_\omega\) as well, (2) is trace factorization on the finite centralizing algebra. Full scalar factorization for every \(x\in P\) would contradict fixed constants, even for \(M=R\).

We prove all assertions, including membership of the reindexed representatives in \(N_\omega\). An arbitrary reindexing of a multiplier sequence need not preserve that membership.

## 2. Countable data and bounded representatives

Replace \(P,Q\) by \(P\vee M,Q\vee M\), and eventually restrict the constructed map back to the original \(P\). These joins still have separable predual. Indeed each original algebra, and \(M\), has a countable set generating it as a von Neumann algebra. Their union generates each join. In the faithful normal state GNS representation of that join, countably many rational *-words applied to the cyclic vector have dense span, by strong density. The representation Hilbert space is separable, so its represented algebra has separable predual. The enlarged \(P\) remains \(G\)-invariant because constant lifts preserve \(M\).

Choose countable unital *-algebras over \(\mathbb Q(i)\),
\[
\mathcal A\subset P,\qquad \mathcal B\subset Q,
\tag{3}
\]
ultraweakly dense in their ambient algebras. Arrange that
\(\mathcal A\cap M\) and \(\mathcal B\cap M\) are dense in \(M\), and that
\(\mathcal A\cap M_\omega\) and \(\mathcal B\cap M_\omega\) are dense in their respective intersections. Include countable strong* dense sets from the unit balls of those intersections before generating the algebras. Include all \(G\)-translates of the generators for \(\mathcal A\); countability of \(G\) makes \(\mathcal A\) countable and invariant.

Exhaust these data by increasing finite sets
\[
\mathcal A_n,\quad\mathcal B_n,\quad G_n,\qquad
1\in\mathcal A_n\cap\mathcal B_n,
\tag{4}
\]
and let \(\psi_j\) be norm dense in \(M_*\). The finite sets need not themselves be algebras: all resulting sums, products and translates already have representatives indexed by the whole countable algebra.

For each \(x\in\mathcal A\), choose a representative \(u_x(k)\in N_\omega\), uniformly bounded by \(\|x\|\). Such a lift exists by continuous radial clipping of any lift: for \(C=\|x\|>0\), replace a lift \(b\) by \(b f(b^*b)\), where \(f(t)=\min(1,C/\sqrt t)\), with \(f(0)=1\). Its image is unchanged and its norm is at most \(C\). Choose \(u_0=0\). For \(x\in M\) choose the constant representative. For \(x\in M_\omega\) choose a representative in \(C_\omega\), using the same quotient lifting inside that \(C^*\)-algebra.

Likewise choose bounded multiplier representatives \(v_a(k)\) for \(a\in\mathcal B\), and use constants for \(a\in M\). Exact algebraic coherence of the representatives is unnecessary. For example
\[
u_x(k)u_y(k)-u_{xy}(k)\in I_\omega,\qquad
u_x(k)^*-u_{x^*}(k)\in I_\omega.
\tag{5}
\]
Addition and rational complex scalar multiplication have the same null-error property.

## 3. Multiplier moduli and the finite selection

For every \(x\in\mathcal A\) and positive integer \(l\), the multiplier criterion gives \(\delta_l(x)>0\) and \(W_l(x)\in\omega\) such that
\[
\begin{gathered}
k\in W_l(x),\quad \|z\|\le1,\quad \|z\|_\#<\delta_l(x)\\
\Longrightarrow\
\|u_x(k)z\|_\#+\|zu_x(k)\|_\#<1/l.
\end{gathered}
\tag{6}
\]
Shrinking the moduli and taking finite intersections lets us assume they decrease with \(l\). No countable intersection is used.

At outer index \(n\), choose an inner index \(p(n)\ge n\) satisfying the following finite list:

1. \(p(n)\in W_l(x)\) for \(x\in\mathcal A_n,\ l\le n\).
2. Each addition, adjoint, multiplication and rational scalar relation for operands in \(\mathcal A_n\) has symmetric seminorm error below \(1/n\) at \(p(n)\). For scalars, test the first \(n\) elements of a fixed enumeration of \(\mathbb Q(i)\).
3. For \(x\in\mathcal A_n\cap M_\omega,\ j\le n\),
\(\|[u_x(p(n)),\psi_j]\|<1/n\).
4. For \(x\in\mathcal A_n\cap M_\omega,\ a\in\mathcal B_n\),
\(\|[u_x(p(n)),v_a(n)]\|_\#<1/n\).
5. For \(x\in\mathcal A_n,\ a\in\mathcal B_n,\ j\le n\),
\[
|\psi_j(v_a(n)(u_x(p(n))-E_\omega(x)))|<1/n.
\tag{7}
\]
6. For \(x\in\mathcal A_n,\ \theta^\omega\in G_n\),
\[
\|\theta(u_x(p(n)))-u_{\theta^\omega(x)}(p(n))\|_\#<1/n.
\tag{8}
\]

**Lemma 3.1.** Such a choice exists for every \(n\).

**Proof.** Every condition specifies an \(\omega\)-large set of admissible inner indices. The first uses (6); the second uses null quotient relations such as (5). The third uses the centralizing representative.

For the fourth, \(v_a(n)\) is a fixed element of \(M\) while choosing the inner index. Centralizing sequences commute strong* along \(\omega\) with every fixed element of \(M\), by the normal-functional centrality criterion proved in the [ordinary central sequence lesson](central-sequences-and-free-group-factors.md#1-two-meanings-of-almost-commuting). Thus the fourth condition is also available.

For the fifth, \(u_x(k)\) converges ultraweakly along \(\omega\) to \(E_\omega(x)\); at this fixed \(n\), the functional \(y\mapsto\psi_j(v_a(n)y)\) is normal and fixed. For the sixth, the difference represents zero because \(\theta^\omega\) is the constant lift of \(\theta\). It therefore lies in \(I_\omega\).

Intersect these finitely many sets with the cofinite set \(\{k\ge n\}\). A free ultrafilter contains the resulting nonempty infinite set, so a choice is possible. \(\square\)

The normal functional in (7) varies when \(n\) changes, but it is fixed during each individual selection. This is the reason fast selection handles its moving coefficient \(v_a(n)\).

## 4. The map on the countable algebra

Set
\[
w_x(n)=u_x(p(n)),\qquad \Phi_0(x)=\pi(w_x),\quad x\in\mathcal A.
\tag{9}
\]

**Lemma 4.1.** Every \(w_x\) belongs to \(N_\omega\). For \(x\in\mathcal A\cap M_\omega\), it is an ordinary centralizing sequence.

**Proof.** Fix \(x,l\). Once \(n\) is large enough that \(x\in\mathcal A_n\) and \(n\ge l\), the selected index lies in \(W_l(x)\). Thus (6), with its fixed positive \(\delta_l(x)\), holds for every sufficiently large outer index. If \(z_n\) is a contraction sequence in \(I_\omega\), its seminorm is below this fixed modulus on an \(\omega\)-large set. Both products with \(w_x(n)\) have seminorm below \(1/l\) there. Let \(l\to\infty\), and rescale to handle any bounded null sequence. This proves both multiplier conditions.

For centralizing \(x\), condition 3 gives ordinary convergence of its commutators with each \(\psi_j\). The bound
\(\|[w_x(n),\rho]\|\le2\|x\|\|\rho\|\) and norm density give ordinary convergence for every \(\rho\in M_*\). \(\square\)

The finite relation tests make \(\Phi_0\) a unital *-homomorphism over \(\mathbb Q(i)\). Its operator bound is
\[
\|\Phi_0(x)\|\le\sup_n\|u_x(p(n))\|\le\|x\|.
\tag{10}
\]
Taking \(a=1\) in (7), and using norm density of the normal functionals, gives
\[
E_\omega(\Phi_0(x))=E_\omega(x).
\tag{11}
\]
It follows that \(\varphi^\omega\Phi_0=\varphi^\omega|_{\mathcal A}\). Applying this to \(x^*x\) and \(xx^*\) gives the exact isometry
\[
\|\Phi_0(x)\|_{\varphi^\omega,\#}
=\|x\|_{\varphi^\omega,\#}.
\tag{12}
\]
In particular the map is injective on \(\mathcal A\).

The remaining tests already imply, on the countable data,
\[
\begin{aligned}
[\Phi_0(x),a]&=0
&&(x\in\mathcal A\cap M_\omega,\ a\in\mathcal B),\\
E_\omega(a\Phi_0(x))&=E_\omega(a)E_\omega(x)
&&(x\in\mathcal A,\ a\in\mathcal B),\\
\theta^\omega\Phi_0(x)&=\Phi_0(\theta^\omega(x))
&&(x\in\mathcal A,\ \theta^\omega\in G).
\end{aligned}
\tag{13}
\]
For the middle equality, (7) makes the representative error ultraweakly null, while \(v_a(n)E_\omega(x)\) has ultraweak ultralimit \(E_\omega(a)E_\omega(x)\). All products are legitimate multiplier products by Lemma 4.1. The first equality follows from condition 4, and the last from (8). Constants in \(\mathcal A\cap M\) are fixed exactly.

## 5. Normal extension and all assertions

**Lemma 5.1.** A norm-contractive unital *-homomorphism on an ultraweakly dense countable rational *-algebra, preserving a faithful normal state as above, extends uniquely to a normal injective *-homomorphism on its von Neumann closure.

**Proof.** First extend by norm continuity to the \(C^*\)-closure \(A=\overline{\mathcal A}^{\,\|\cdot\|}\). Continuity with respect to rational complex scalars gives complex linearity. Multiplication, adjoints, the state identity and (12) survive norm limits.

For \(x\in P\), Kaplansky density supplies a bounded net \(x_i\in A\) converging strong* to \(x\), with \(\|x_i\|\le\|x\|\). The symmetric state seminorm makes it Cauchy; (12) makes its image Cauchy in the same seminorm, with the same uniform operator bound. In the von Neumann algebra \(M^\omega\), a bounded strong*-Cauchy net has a strong* limit. The faithful normal state criterion therefore gives an image limit \(\Phi(x)\).

If two nets approximate \(x\), their differences have vanishing symmetric seminorm, so (12) makes the image limits equal. The construction is thus well-defined and agrees with the original map. Using simultaneous bounded approximating nets for two elements, joint strong* continuity of multiplication on bounded sets and continuity of adjoints give multiplicativity, linearity and the *-identity. The operator bound and the state identity survive. Faithfulness of the state makes \(\Phi\) injective.

For normality, let \(0\le x_i\uparrow x\) in \(P\). In \(M^\omega\), put \(Y=\sup_i\Phi(x_i)\le\Phi(x)\). Preservation and normality of the state give
\[
\varphi^\omega(\Phi(x)-Y)
=\varphi^\omega(x)-\lim_i\varphi^\omega(x_i)=0.
\tag{14}
\]
Its faithfulness gives \(Y=\Phi(x)\). Thus \(\Phi\) is normal. Uniqueness follows from ultraweak density and normality. \(\square\)

Apply this lemma to (9). The constant restriction extends from \(\mathcal A\cap M\) to \(M\). For the second assertion of (1), use bounded strong* density of \(\mathcal A\cap M_\omega\) in \(P\cap M_\omega\). Its images are centralizing by Lemma 4.1 and commute with the ultraweakly dense algebra \(\mathcal B\). The normal subalgebra \(M_\omega\) and the relative commutant \(Q'\cap M^\omega\) are both strongly closed, so the full image has the required inclusion.

The expectation equality in (13) extends separately: first in \(x\), for each fixed \(a\in\mathcal B\), because \(x\mapsto E_\omega(a\Phi(x))\) and \(x\mapsto E_\omega(a)E_\omega(x)\) are normal linear maps. Then extend in \(a\), for each fixed \(x\in P\), by the same normality. This uses no joint ultraweak continuity of multiplication. Equivariance extends by normality of \(\Phi\) and the constant lifts. These arguments prove every part of Theorem 1.1.

Restricting from the enlarged \(P\) to the original algebra proves the originally stated version. The countable group hypothesis governs the finite action tests; separable predual governs the countable algebra and functional tests.

## 6. Exercises with complete solutions

**Exercise 1.** Why does adjoining \(M\) preserve separable predual here?

*Solution.* The two algebras have countable generating sets, so their join has one. Its faithful normal state GNS space is the closure of the span of countably many rational *-words applied to its cyclic vector. Kaplansky density makes that span dense. Hence this space is separable. The represented algebra has predual a quotient of the trace-class operators on that space, and therefore separable predual.

**Exercise 2.** Why can arbitrary bounded representatives be used instead of an exactly linear choice of lifts?

*Solution.* Every rational algebraic relation holds in the quotient, so the discrepancy of any chosen bounded lifts is in \(I_\omega\). At each stage only finitely many such discrepancies are tested. Making their symmetric seminorms less than \(1/n\) at the selected coordinate makes the reindexed discrepancy ordinarily null. The quotient map then respects the relation exactly.

**Exercise 3.** What is the role of the fixed modulus \(\delta_l(x)\)?

*Solution.* It controls multiplication for all contraction inputs whose seminorm is small, rather than just a finite selected set of inputs. For every sufficiently large outer index it applies to \(u_x(p(n))\). Every null input sequence eventually satisfies the fixed modulus on an ultrafilter set. This proves the full multiplier condition; finite algebraic tests alone would not.

**Exercise 4.** Why is it legitimate to test a moving representative \(v_a(n)\) in condition 4?

*Solution.* At the selection for a given \(n\), \(v_a(n)\) is a single fixed operator of \(M\). The centralizing inner sequence commutes strong* with that operator as its inner index tends along \(\omega\). Thus an \(\omega\)-large set satisfies this one test. The selected inner index can change at the next stage, allowing a different fixed operator there.

**Exercise 5.** Explain why no countable intersection of ultrafilter sets is needed.

*Solution.* At stage \(n\), only finite sets of elements, group actions, functionals, moduli and algebraic relations are used. Their finite intersection is in the ultrafilter and is nonempty. Every fixed datum is included at all sufficiently large stages, so its errors vanish ordinarily along the outer index. This sequence of finite choices supplies the countable conclusion.

**Exercise 6.** Derive the symmetric state isometry (12).

*Solution.* Multiplicativity and state preservation give
\(\varphi^\omega(\Phi_0(x)^*\Phi_0(x))=\varphi^\omega(x^*x)\).
Applying the same identity to \(xx^*\) gives the adjoint square. Averaging the two equalities and taking square roots gives (12). This supplies the bounded strong* continuity required for the extension.

**Exercise 7.** Why is the extension multiplicative although strong convergence is not jointly continuous without bounds?

*Solution.* The Kaplansky approximants and their images have uniform norm bounds. On such bounded sets, products converge strong*, by splitting \(a_i b_i-ab=a_i(b_i-b)+(a_i-a)b\), and applying the adjoint version too. The same estimates hold for the image nets, so the products of their limits agree with the limit of the products.

**Exercise 8.** Explain the separate extension of the expectation identity.

*Solution.* For each fixed \(a\), left multiplication by \(a\), \(\Phi\) and \(E_\omega\) are normal linear maps. Thus the equality extends ultraweakly in \(x\). After doing so, fix \(x\); right multiplication by the fixed \(\Phi(x)\) and multiplication by the fixed \(E_\omega(x)\) are normal in \(a\). This extends to all \(a\in Q\) without asserting a jointly ultraweakly continuous product.

**Exercise 9.** Why does the equivariance test fail for a general semi-lift represented by \(\theta_k\to\theta\)?

*Solution.* The representative of its action on \(x\) is \(\theta_k(u_x(k))\). After reindexing, equivariance would compare this with \(\theta_n(u_x(p(n)))\), whose automorphism index is the outer \(n\), rather than the selected inner \(p(n)\). Convergence on fixed elements does not control this varying input. The tensor-tail example supplies an exact contradiction to imposing all those equivariance requirements together with relative commutation.

**Exercise 10.** Give the correct factor trace conclusion and explain the failure for arbitrary constants.

*Solution.* For a factor and centralizing \(x\), \(E_\omega(x)=\tau_\omega(x)1\); applying \(\varphi\) to (1) gives (2). If \(a\) is centralizing too, this is trace factorization on \(M_\omega\). For a constant trace-zero self-adjoint unitary \(x=a\), fixing constants instead gives \(\tau^\omega(a\Phi(x))=1\), whereas the product of scalar traces is zero. The expectation identity correctly gives \(E_\omega(a)E_\omega(x)=a^2=1\).

## References

The freely accessible construction source is Adrian Ocneanu, [*Actions of discrete amenable groups on factors*](https://wrap.warwick.ac.uk/id/eprint/110062/1/WRAP_Theses_Ocneanu_1982.pdf), thesis, Chapter 5, Section 5.3, Fast Reindexation Trick, printed pp.53–54 (PDF pp.67–68). Its hypothesis is a countable family of liftable automorphisms. Its product formula uses the canonical expectation, with the input in the map's domain and the prescribed coefficient in the other algebra. The full source argument was read, including its uniform multiplier tests and normal extension.

The lesson supplies the finite intersections, two-sided multiplier estimates, rational-algebra relations, faithful-state normal extension and separately normal passage to every expectation identity in full. It retains arbitrary separable-predual algebras, without a factor or tracial restriction. The preceding explicit tensor-tail obstruction explains why general semi-lifts cannot replace constant lifts in this theorem. The exact local prerequisite bindings and remaining free foundation dependencies are recorded separately.
