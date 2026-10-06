# Isotropy and random-operator fibres

*Written by GPT-6.1 Sol (OpenAI), Ultra, September 2026. Author self-check in progress; not independently reviewed. New original text is public domain (CC0).*

## Introduction

An operator attached to an orbit must be compatible with every arrow. An arrow from a point to itself imposes an additional commutation condition. That condition survives even if the space has just one orbit.

This lesson calculates it for countable discrete groupoids and proves a finite-isotropy version of the averaged rank-one operator theorem. It explains both the role of isotropy and why ergodicity alone does not give the invariant-scalar centre formula for an arbitrary groupoid.

We use the definitions and regular representations of [Measured groupoids and transverse measures](https://kokunoyumeto.github.io/open-math-courses-public/courses/NCG-FOLIATIONS/companions/measured-groupoids-and-transverse-measures.html) and [Square-integrable representations and random operators](https://kokunoyumeto.github.io/open-math-courses-public/courses/NCG-FOLIATIONS/companions/square-integrable-representations-and-random-operators.html). The contrast with a principal relation is developed in [Orbits, stabilizers, and relation algebras](orbits-stabilizers-and-relation-algebras.md). Basic references are [Connes] and [Takesaki].

The discrete hypotheses below also make endpoint coordinates measurably recoverable. This feature matters beyond discrete examples: [Principal groupoids with extra fibre information](principal-groupoids-with-extra-fibre-information.md) proves that trivial isotropy and one orbit alone need not give a scalar centre or generation of the full isotropy commutant at merely countably generated arrow scope. Its finite faithful counterexample does not change the discrete calculations proved here.

All groupoids in this lesson have countably many arrows and the discrete Borel structure. Every Hilbert space is separable. The measure on the unit space satisfies \(0<\mu(\{x\})<\infty\) at every unit \(x\). Countability therefore makes it sigma-finite, and no nonempty subset of the unit space is negligible. These hypotheses make every choice used below measurable.

## 1. Transport to a point on one orbit

Let \(\mathcal G\) be transitive, with unit set \(O\). Fix \(o\in O\), and choose an arrow \(t_x:o\to x\) for each \(x\), with \(t_o\) the unit. Let \(H=\mathcal G_o^o\) be the isotropy group at \(o\).

**Lemma 1.1.** Every arrow \(\gamma:x\to y\) has a unique expression

\[
\gamma=t_yht_x^{-1},\qquad h\in H.
\tag{1.1}
\]

Composition corresponds to multiplication in \(H\):

\[
(t_zkt_y^{-1})(t_yht_x^{-1})=t_zkht_x^{-1}.
\tag{1.2}
\]

*Proof.* Set \(h=t_y^{-1}\gamma t_x\). Its source and range are both \(o\), so it lies in \(H\). Multiplying by \(t_y\) and \(t_x^{-1}\) recovers \(\gamma\); these multiplications also prove uniqueness. Cancellation gives (1.2). \(\square\)

A unitary representation of \(\mathcal G\) consists of Hilbert spaces \(K_x\) and unitaries \(U(\gamma):K_x\to K_y\), compatible with composition. Set \(K=K_o\), \(T_x=U(t_x):K\to K_x\), and \(\pi(h)=U(h)\). Formula (1.1) gives

\[
U(\gamma)=T_y\pi(h)T_x^*.
\tag{1.3}
\]

Thus a representation on a single transitive orbit is described by an isotropy representation and the transport unitaries.

## 2. Equivariant operators are isotropy commutants

A bounded equivariant operator field \(A=(A_x)\) satisfies

\[
A_yU(\gamma)=U(\gamma)A_x,\qquad \gamma:x\to y.
\tag{2.1}
\]

Its norm is \(\sup_x\|A_x\|\). In the present atomic measured setting this is also its essential supremum norm with respect to the unit-space measure.

**Theorem 2.1.** The algebra of bounded equivariant fields is normally isomorphic to

\[
\pi(H)'=\{B\in B(K):B\pi(h)=\pi(h)B\text{ for every }h\in H\}.
\tag{2.2}
\]

The isomorphism sends \(B\) to the field \(A_x=T_xBT_x^*\).

*Proof.* Apply (2.1) to \(t_x\). It forces \(A_x=T_xA_oT_x^*\). Apply it to the isotropy arrows at \(o\): it forces \(A_o\in\pi(H)'\). Conversely, a \(B\) in this commutant gives an equivariant field by (1.3). The correspondence respects multiplication, adjoints, and norms.

The commutant in (2.2) is a von Neumann algebra because it is a weakly closed commutant in \(B(K)\). The field algebra has a concrete representation on \(\bigoplus_{x\in O}K_x\). Under the unitary transports \(T_x\), this is the diagonal amplification \(B\mapsto\bigoplus_xB\). It preserves suprema of bounded increasing positive nets, so the isomorphism is normal. Positive atomic weights on the unit space change this Hilbert representation by the unitary multiplying the \(x\)-coordinate by the square root of its mass; they do not change the operator field algebra. \(\square\)

This conclusion applies in particular to the square-integrable representations used to define random Hilbert spaces. In this atomic setting the equivariant field itself already gives the concrete realization.

For a groupoid with several orbits, choose one point in each orbit and repeat the construction. There are at most countably many orbits. The bounded field algebra is the bounded product of the resulting isotropy commutants.

## 3. The regular representation keeps isotropy

On the range fibre \(\mathcal G^y=r^{-1}(y)\), the left regular representation acts by left translation. Formula (1.1) identifies this fibre with \(O\times H\), through

\[
(x,h)\longmapsto t_yht_x^{-1}.
\]

Hence

\[
\ell^2(\mathcal G^y)\cong\ell^2(O)\otimes\ell^2(H).
\tag{3.1}
\]

For \(\gamma=t_zkt_y^{-1}\), translation sends \((x,h)\) to \((x,kh)\). In these coordinates its unitary is

\[
1_{\ell^2(O)}\otimes\lambda_H(k),
\tag{3.2}
\]

where \(\lambda_H\) is the left regular representation of \(H\).

**Corollary 3.1.** The regular random-operator algebra on a transitive countable discrete groupoid is

\[
\bigl(1_{\ell^2(O)}\otimes\lambda_H(H)\bigr)'.
\tag{3.3}
\]

If \(H\) is trivial, it is \(B(\ell^2(O))\). If \(H=C_2\), it is

\[
B(\ell^2(O))\oplus B(\ell^2(O)).
\tag{3.4}
\]

*Proof.* Apply Theorem 2.1 to (3.2). For \(C_2\), its regular representation has a one-dimensional \(+1\) eigenspace and a one-dimensional \(-1\) eigenspace. An operator commutes with that involution exactly when it preserves both eigenspaces, giving (3.4). \(\square\)

The second algebra has two independent central projections, despite transitivity of the groupoid. Its two spectral sectors come from isotropy. This does not conflict with the invariant-scalar centre theorem for principal groupoids, whose isotropy groups are trivial.

## 4. Averaged rank-one operators for finite isotropy

Let \(H\) now be finite, and let \(\pi\) be any unitary representation on a separable Hilbert space \(K\). For \(B\in B(K)\), define

\[
Q(B)=\frac1{|H|}\sum_{h\in H}\pi(h)B\pi(h)^*.
\tag{4.1}
\]

**Lemma 4.1.** The map \(Q\) is a normal conditional expectation onto \(\pi(H)'\).

*Proof.* Each conjugation is normal, unital, and completely positive, so the finite average has those properties. Left multiplication permutes the summation indices, showing that its range commutes with \(\pi(H)\). It fixes each element of that commutant. If \(A,C\) belong to the commutant, then \(Q(ABC)=AQ(B)C\), proving bimodularity. \(\square\)

For \(v,w\in K\), let \(|v\rangle\langle w|\) denote \(\zeta\mapsto\langle\zeta,w\rangle v\), with the inner product linear in its first variable. Put

\[
\Theta(v,w)=Q(|v\rangle\langle w|).
\tag{4.2}
\]

**Theorem 4.2.** The linear span of the operators \(\Theta(v,w)\) is ultraweakly dense in \(\pi(H)'\). It is enough to take \(v,w\) from any countable total set closed under rational complex linear combinations.

*Proof.* Choose finite-rank projections \(P_n\uparrow1\), built from such a total set by Gram–Schmidt. For \(A\in\pi(H)'\), the finite-rank operators \(P_nAP_n\) are uniformly bounded and converge strongly to \(A\). Each is a finite linear combination of rank-one operators using vectors in the span of the total set. Applying the finite sum (4.1) gives

\[
Q(P_nAP_n)\longrightarrow Q(A)=A
\]

strongly: each conjugation preserves strong convergence on this bounded sequence. This proves density using the linear span of the total set. Norm approximation of its vectors by rational complex combinations gives the last assertion, since
\(\||v\rangle\langle w|\|=\|v\|\|w\|\)
and \(Q\) is contractive. \(\square\)

The averaged rank-one operators exhaust the *isotropy commutant*. They exhaust all of \(B(K)\) precisely when that commutant is all of \(B(K)\), which happens when the isotropy representation is scalar. Trivial isotropy is one way to ensure that condition.

In the transitive groupoid, use counting measure on each range fibre and take a section supported at the base point \(o\), with value \(v\). Its coefficient operator has a sum over only \(|H|\) nonzero arrows at each target. Thus it is a bounded square-integrable coefficient section. Averaging the rank-one operators over all these arrows gives \(|H|T_y\Theta(v,w)T_y^*\) at the point \(y\). Sections supported at each \(x\), with values in \(T_x\) of a countable total subset of \(K\), give a countable total family of such coefficient sections. Theorem 4.2 consequently describes the fibre algebra generated by these groupoid coefficient operators, including finite nontrivial isotropy.

**Example 4.3.** Let \(H=C_2\), and decompose \(K=K_+\oplus K_-\) according to the two eigenspaces of its involution. Formula (4.1) deletes the off-diagonal blocks of an operator:

\[
Q\begin{pmatrix}A&B\\ C&D\end{pmatrix}
=\begin{pmatrix}A&0\\0&D\end{pmatrix}.
\]

Thus the rank-one averages generate \(B(K_+)\oplus B(K_-)\), rather than all \(B(K)\) when both spaces are nonzero.

For infinite isotropy there is no normalized finite sum in (4.1). The finite-isotropy theorem keeps its exact range. [Borel group measures and isotropy topologies](borel-group-measures-and-isotropy-topologies.md), Sections 4–6, supplies the standard range-fibre Haar product and its section-change density. [Averaged coefficients and isotropy commutants](averaged-coefficients-and-isotropy-commutants.md#6-general-square-integrable-fields), Theorem 6.1, supplies the global countable coefficient family at its stated standard Borel, square-integrability and regular-commutant inputs. Those separate proofs are needed for the general supported construction.

## 5. Exercises with solutions

Level 1 asks for a computation or a direct application. Level 2 asks for a proof using the lesson’s framework. Level 3 combines results or examines a hypothesis whose failure changes the conclusion.

**Exercise 5.1 (changing the transports).** *Level 2.* Replace \(t_x\) by \(t_xa_x\), where \(a_x\in H\). Determine the new coordinate of an arrow \(\gamma:x\to y\).

*Solution.* Its new coordinate is \(a_y^{-1}ha_x\). The transport unitary changes to \(T_x\pi(a_x)\). If \(B\in\pi(H)'\), the field \(T_xBT_x^*\) remains the same. Thus the description of the random-operator algebra does not depend on the chosen transports.

**Exercise 5.2 (a nonfaithful isotropy representation).** *Level 2.* Suppose \(H=C_2\) acts trivially on an infinite-dimensional \(K\). What is its equivariant field algebra on one transitive orbit?

*Solution.* It is \(B(K)\), because \(\pi(H)\) consists of the identity. Nontrivial isotropy of the groupoid alone does not force a nontrivial centre; the isotropy representation matters.

**Exercise 5.3 (two characters).** *Level 1.* For \(K=\mathbb C^2\) and the \(C_2\) representation \(\operatorname{diag}(1,-1)\), compute all equivariant operators at the base point.

*Solution.* They are precisely the diagonal matrices \(\operatorname{diag}(a,b)\). The commutation equation makes both off-diagonal entries zero. The algebra is \(\mathbb C\oplus\mathbb C\), with two central minimal projections.

**Exercise 5.4 (off-diagonal averages).** *Level 2.* In Example 4.3 take \(v\in K_+\) and \(w\in K_-\). Compute \(\Theta(v,w)\). Then take both vectors in \(K_+\).

*Solution.* In the first case conjugation by the involution changes the rank-one operator's sign, so its average is zero. In the second case the rank-one operator is fixed, so \(\Theta(v,w)=|v\rangle\langle w|\). This gives the two blocks separately.

**Exercise 5.5 (several orbits).** *Level 2.* A discrete groupoid has two transitive components. Its representations at chosen base points are the trivial representation of \(C_2\) on \(\mathbb C^3\) and the regular representation of \(C_2\) on \(\mathbb C^2\). Determine the random-operator algebra.

*Solution.* The first component contributes \(M_3(\mathbb C)\). The second contributes \(\mathbb C\oplus\mathbb C\). The bounded product over the two orbits is \(M_3(\mathbb C)\oplus\mathbb C\oplus\mathbb C\). Orbit decomposition and isotropy decomposition produce distinct central summands.

## References

- [Connes] Alain Connes, “Sur la théorie non commutative de l’intégration,” in *Algèbres d’opérateurs*, Lecture Notes in Mathematics 725, Springer, 1979, 19–143. [Publisher record](https://doi.org/10.1007/BFb0062614).
- [Takesaki] Masamichi Takesaki, *Theory of Operator Algebras III*, Encyclopaedia of Mathematical Sciences 127, Springer, 2003. [Publisher record](https://doi.org/10.1007/978-3-662-10453-8).
