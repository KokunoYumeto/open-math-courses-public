# Smooth local representations and the Hecke-module dictionary

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Author self-check complete. Public domain (CC0).*

At a finite place there are compact open subgroups arbitrarily close to the identity. Averaging over one of them is therefore an exact algebraic operation: it fixes a vector once the subgroup is small enough. This replaces the real Lie derivatives and compact-type projections used in the previous lesson. We will use these averages to reconstruct a smooth representation from its Hecke module, prove Schur's lemma without assuming admissibility, and identify the correct dual.

Let \(F\) be a nonarchimedean local field, \(\mathcal O\) its integers, \(\varpi\) a uniformizer, and \(q=|\mathcal O/\varpi\mathcal O|\). Put \(G=\mathrm{GL}_2(F)\) and normalize Haar measure by \(\operatorname{vol}(K_0)=1\), where \(K_0=\mathrm{GL}_2(\mathcal O)\). For the local topology and valuation, use Local fields: classification and Haar measure, Proposition 3.1; its Proposition 6.1 fixes the additive and multiplicative measure conventions. Finite-group Maschke theory is Representations and complete reducibility, Theorem 2.3. We also use Haar integration and algebraic tensor products. The finite-group theorem does not itself assert exactness for an arbitrary infinite-dimensional smooth representation: the compact averages needed here are constructed and proved exact in Section 1. The double-coset basis and multiplication of a fixed-level Hecke algebra belong to the adèle prerequisite, NT-ADL-12, Proposition 12.1; only that basis description is recalled here. The representation-theoretic projection, reconstruction and simple-module assertions are proved below. For GL₂, admissibility of irreducible smooth representations is proved in the next lesson, Theorem 5.4, using compact averaging and the two cases of the Jacquet module. It is a conclusion rather than part of the definition. The Hilbert compact decomposition used in Lemma 3.2 is proved in Representations of compact groups, Theorem 3.1; its Schur and isotypic results are Theorems 4.1–4.2. The compression and convolution assertions for the noncompact group are proved here.

## 1. Exact averages and local units

For \(n\geq1\),

\[
K_n=1+\varpi^n M_2(\mathcal O)
\tag{1.1}
\]

is a compact open subgroup. Products have the form \(1+\varpi^n(A+B+\varpi^nAB)\), and the convergent inverse series retains that form. Compactness follows from the four compact entry sets, and openness from the entry topology. These groups form a neighbourhood basis of the identity. The field, and hence \(G\), is second countable: countably many valuation balls cover it, with finite residue digits at each precision. Any disjoint family of open cosets is consequently countable.

A complex algebraic representation \((\pi,V)\) is **smooth** when every vector has an open stabilizer, equivalently \(V=\bigcup_K V^K\) over compact open subgroups. It is **admissible** when additionally \(\dim V^K<\infty\) for each such \(K\). Neither condition asks for a Hilbert norm.

Let \(A=\mathcal H(G)=C_c^\infty(G)\), where smooth means locally constant, with

\[
(f_1*f_2)(g)=\int_G f_1(t)f_2(t^{-1}g)\,dt,
\qquad \pi(f)v=\int_G f(g)\pi(g)v\,dg.
\tag{1.2}
\]

The last integral is a finite sum of vectors: intersect the locally constant pieces of \(f\) on its compact support with the open stabilizer of \(v\). Fubini on these finite decompositions proves \(\pi(f_1*f_2)=\pi(f_1)\pi(f_2)\). The group is unimodular. Indeed \(|\det g|^{-2}d^4g\), obtained from additive Haar measure on matrices, is both left and right invariant: left or right multiplication scales the four-entry measure by \(|\det g|^2\), cancelling the determinant density.

For compact open \(K\), write \(e_K=\operatorname{vol}(K)^{-1}1_K\).

**Proposition 1.1 — averages and corners.** We have

\[
e_K*e_K=e_K,\qquad \pi(e_K)V=V^K,
\qquad e_K*A*e_K=\mathcal H(G,K),
\tag{1.3}
\]

where \(\mathcal H(G,K)\) consists of the compactly supported bi-\(K\)-invariant functions. Its identity is \(e_K\).

**Proof.** Averaging a \(K\)-invariant vector leaves it fixed; averaging any vector makes it invariant, by Haar translation. This proves the projection and idempotence assertions, including idempotence within the algebra by the same convolution calculation. Left convolution by \(e_K\) averages left translations of a function, and right convolution averages right translations. Thus the corner consists of bi-invariant functions. Conversely those two averages fix every bi-invariant function, proving equality and the identity assertion. \(\square\)

The double-coset characteristic functions \(1_{KgK}\) give a basis of that corner: the double cosets are open and compact, and a compact support meets finitely many of them. Their product counts the appropriate finite cosets with the Haar factors; its detailed counting formula is the prerequisite result identified above. One must retain \(\operatorname{vol}(K)\) when \(K\ne K_0\).

Every \(f\in A\) is bi-invariant under some compact open subgroup. For the right side, cover its compact support by finitely many cosets on which it is constant, and intersect their fixing subgroups. The support is a finite union of those cosets, so its complement is preserved as well. Do the same on the left and intersect again. For finitely many functions choose a common smaller subgroup. Consequently the \(e_K\) are **local units**: a given finite set of algebra elements satisfies \(e_K*f_i=f_i=f_i*e_K\) for some \(K\).

The full algebra has no identity for this nondiscrete \(G\). For if an identity \(u\) existed, it would be fixed on both sides by some \(e_J\), so \(u=e_J*u=e_J\). But for any proper compact open \(L\subset J\), \(e_J*e_L=e_J\ne e_L\), contradicting the identity property. The exact identities are in the fixed-level corners.

## 2. Recovering the group action

Call an \(A\)-module **nondegenerate** if \(AM=M\), meaning each vector is a finite sum of algebra actions. Local units imply the useful equivalent statement: every \(m\in M\) satisfies \(e_Km=m\) for some \(K\). To see it for \(m=\sum f_im_i\), use a common left local unit of the \(f_i\).

**Proposition 2.1.** Smooth \(G\)-representations and nondegenerate \(A\)-modules are equivalent, with the same invariant subspaces and intertwining maps.

**Proof.** A smooth representation gives (1.2), and a subgroup fixing \(v\) supplies \(e_Kv=v\), so its module is nondegenerate. Conversely, given a nondegenerate module, define

\[
\pi(g)m=(L_ge_K)m,
\qquad (L_gf)(t)=f(g^{-1}t),\qquad e_Km=m.
\tag{2.1}
\]

This is independent of the choice of \(K\). If \(J\subset K\), then \(e_Je_K=e_K=e_Ke_J\), so \(e_Jm=m\) and
\((L_ge_J)m=(L_ge_J)e_Km=(L_ge_K)m\).
For two choices take a common subgroup contained in both. The same argument proves linearity on vectors with different fixing subgroups.

For \(b\in A\), choose a common local unit \(e_J\) fixing \(m\) and satisfying \(e_Jb=b\). The identity
\((L_g f)*b=L_g(f*b)\) then gives
\(\pi(g)(bm)=(L_gb)m\).
Applying it to \(b=L_he_K\) proves \(\pi(g)\pi(h)m=(L_{gh}e_K)m\). The identity acts as the identity. Also \(K\) fixes \(m\), since \(L_ke_K=e_K\) for \(k\in K\); hence the recovered action is smooth.

Integration of (2.1) gives the original module action: \(\int f(g)L_ge_Kdg=f*e_K\), and choosing \(K\) also a right local unit for \(f\) gives \(\pi(f)m=fm\). Starting from a smooth representation, \(\pi(L_ge_K)m=\pi(g)\pi(e_K)m=\pi(g)m\), recovering its original group action. A subspace stable under the group is stable under finite-sum integrals. A subspace stable under \(A\) is stable under (2.1). The same formulas prove the assertion for morphisms. \(\square\)

There is no assertion here that all smooth representations are admissible. The equivalence applies to infinite-dimensional fixed spaces as well.

## 3. A fixed subgroup and all simple modules

Fix compact open \(K\), and abbreviate \(e=e_K\), \(B=eAe\). Modules for the unital algebra \(B\) are understood to have its identity \(e\) act as one. A simple module or irreducible representation is nonzero.

**Theorem 3.1 — Hecke-module dictionary.** The map
\(V\longmapsto V^K=eV\)
gives a bijection between the isomorphism classes of irreducible smooth \(G\)-representations with \(V^K\ne0\) and simple \(B\)-modules.

**Proof of the forward assertion.** If \(0\ne W\subset eV\) is a \(B\)-submodule, the \(A\)-submodule \(AW\) is nonzero and therefore all of \(V\). Multiplying by \(e\) gives
\(eV=eAW=eAeW=BW=W\).
Thus \(eV\) is simple. Conversely an irreducible representation with nonzero fixed vectors is generated by them, since \(AeV\) is a nonzero invariant subspace.

**Construction of the inverse.** Given a simple \(B\)-module \(M\), form

\[
P=Ae\otimes_B M.
\tag{3.1}
\]

It is a nondegenerate \(A\)-module, by local units on the finitely many first tensor factors of a vector. Its fixed part is exactly \(eP\simeq M\): send \(eae\otimes m\) to \((eae)m\), with inverse \(m\mapsto e\otimes m\). The tensor relations prove that these maps are inverse. Further, \(P=A(eP)\).

Define the submodule

\[
N=\{x\in P:eAx=0\}.
\tag{3.2}
\]

It is stable under \(A\), and \(eN=0\), taking the algebra element \(e\) in its defining condition. Every submodule \(U\) with \(eU=0\) lies in \(N\), since then \(eAU=0\). Thus \(N\) is the largest submodule invisible to \(e\), and \(N\cap eP=0\). Put \(V_M=P/N\). It is nonzero and its fixed part is \(M\).

If \(U\subset V_M\) is a nonzero submodule, \(eU\) is either zero or all of \(eV_M=M\). In the first case the inverse image \(\widetilde U\subset P\) has \(e\widetilde U\subset N\cap eP=0\); maximality in (3.2) forces \(\widetilde U\subset N\), contrary to \(U\ne0\). In the second case \(U\) contains \(eV_M\) and hence \(A(eV_M)=V_M\). This proves simplicity. Proposition 2.1 converts it to an irreducible smooth representation.

**Uniqueness.** If \(V\) is irreducible and \(eV=M\), the map \(P\to V\), \(ae\otimes m\mapsto am\), is surjective and an isomorphism on fixed parts. Its kernel has fixed part zero and hence lies in \(N\). The image of \(N\) in \(V\) also has fixed part zero, so irreducibility makes it zero, giving the opposite inclusion. Therefore its kernel is exactly \(N\). This proves uniqueness and both inverse assertions. \(\square\)

The quotient by \(N\) is essential. The induced module (3.1) can have additional submodules with no \(K\)-fixed vectors; simply declaring that tensor product irreducible would skip the reconstruction problem. This theorem classifies simple objects with fixed vectors, rather than claiming an equivalence between all \(G\)-representations and all modules of one fixed corner.

**Smooth admissibility.** Every irreducible smooth complex representation of \(G\) is admissible, by the complete proof in Normalized induction and Jacquet modules, Theorem 5.4. Its noncuspidal case embeds into an explicitly admissible principal series. In the zero-Jacquet case, Theorem 5.3 proves a uniform support bound for the vector-valued compact projection of a cyclic vector, then uses compactness to bound the fixed space. That argument needs the countable Schur lemma in Section 4 and the exact averages above, without assuming admissibility. Consequently Theorem 3.1 implies that every simple \(\mathcal H(G,K)\)-module is finite dimensional.

**Lemma 3.2 — compact conjugacy and Hilbert multiplicity.** Let \(G\) be a unimodular locally compact group and \(K\) a compact subgroup. Suppose a Haar-preserving continuous anti-automorphism \(\tau\) sends each \(g\) to a \(K\)-conjugate of \(g\). Then every irreducible strongly continuous unitary representation of \(G\) contains each irreducible compact \(K\)-type at most once.

**Proof.** Let \(\mathcal C\) be the continuous compactly supported functions invariant under \(K\)-conjugation. It is a convolution algebra closed under the adjoint
\(f^*(g)=\overline{f(g^{-1})}\). Every \(f\in\mathcal C\) satisfies \(f\circ\tau=f\). Reversing products and changing Haar variables gives
\[
(f*h)\circ\tau=(h\circ\tau)*(f\circ\tau).
\]
Convolution is again \(K\)-conjugation invariant. Thus \(\mathcal C\) is commutative.

Here is the full multiplicity argument, since commutativity alone does not make a compact isotypic space one dimensional. Compact Hilbert decomposition writes that space as
\[
E_\rho=P_\rho\mathcal H=V_\rho\otimes M_\rho,\qquad
d=\dim V_\rho<\infty.
\]
Every \(\pi(f)\), \(f\in\mathcal C\), restricts there to \(I\otimes b_f\).
For an arbitrary \(f\in C_c(G)\), its compression
\(A=P_\rho\pi(f)P_\rho\) is a \(d\times d\) matrix of bounded operators on \(M_\rho\). Average \(\pi(k)\pi(f)\) under compact conjugation. Its kernel is continuous, compactly supported and in \(\mathcal C\); its restriction is
\[
I\otimes\frac1d
 \operatorname{Tr}_{V_\rho}\bigl((\rho(k)\otimes I)A\bigr).
\]
The normalization follows from compact Schur averaging:
\[
\int_K\rho(k)B\rho(k)^*\,dk
 =\frac{\operatorname{tr}B}{d}I.
\]
To justify both this identity and the needed matrix extraction, its average commutes with \(\rho(K)\), hence is scalar by finite-dimensional Schur, and its trace is \(\operatorname{tr}B\). Taking \(B\) to be a matrix unit gives matrix-coefficient orthogonality
\[
\int_K\rho(k)_{ij}\overline{\rho(k)_{\ell m}}\,dk
 =\frac1d\delta_{i\ell}\delta_{jm}.
\]
Integrating \(\rho(k)\) against those coefficients produces every matrix unit. Its linear span is therefore all \(\operatorname{End}(V_\rho)\), and the partial traces in the preceding display extract every entry of \(A\).

Suppose a closed nonzero proper \(M_0\subset M_\rho\) reduced all \(b_f\). Every entry of every compression \(A\) would preserve \(M_0\) and its orthogonal complement, so \(V_\rho\otimes M_0\) would reduce every compressed \(\pi(f)\). Approximate a point mass at \(g\) by compactly supported continuous probability kernels. Strong continuity and unitarity make their integrated operators converge strongly to \(\pi(g)\), so the same reduction holds for \(P_\rho\pi(g)P_\rho\). If \(v\) is in this subspace and \(w\) in its orthogonal complement inside \(E_\rho\), then
\[
\langle\pi(g)v,\pi(h)w\rangle
 =\langle P_\rho\pi(h^{-1}g)P_\rho v,w\rangle=0.
\]
Their closed group spans are nonzero orthogonal invariant subspaces, contradicting irreducibility. Thus the commutative adjoint-closed algebra of the \(b_f\) acts irreducibly on \(M_\rho\). Spectral projections of each of its self-adjoint elements commute with the algebra and must be zero or the identity; that element is scalar. Real and imaginary parts make every \(b_f\) scalar. If \(\dim M_\rho>1\), a nonzero proper closed subspace would then reduce them all. Hence \(\dim M_\rho=1\) whenever the type occurs. \(\square\)

**Lemma 3.3 — integral transpose conjugacy.** Every \(2\times2\) matrix over \(F\) is conjugate to its transpose by a matrix in \(\mathrm{GL}_2(\mathcal O)\).

**Proof.** A scalar matrix needs no conjugation. Otherwise set
\[
r=\min\{v(A_{12}),v(A_{21}),v(A_{22}-A_{11})\},\qquad
B=\varpi^{-r}(A-A_{11}I),
\]
using \(v(0)=+\infty\). This \(r\) is finite, \(B\) is integral, and its reduction is nonscalar: its upper-left entry is zero and at least one of the other displayed entries is a unit.

A nonscalar \(2\times2\) matrix over the residue field has a cyclic vector among \(e_1,e_2,e_1+e_2\). Indeed if none were cyclic, the first two would be eigenvectors, making the matrix diagonal, and the third being an eigenvector would make its diagonal entries equal. Choose such a vector and lift it integrally. Then
\(P=(v,Bv)\in\mathrm{GL}_2(\mathcal O)\). Cayley–Hamilton gives
\[
P^{-1}BP=C=
 \begin{pmatrix}0&-\det B\\1&\operatorname{tr}B\end{pmatrix}.
\]
Put
\[
Q=\begin{pmatrix}0&1\\1&\operatorname{tr}B\end{pmatrix}.
\]
It has determinant \(-1\), a unit in every residue characteristic. Multiplication gives
\[
QC=\begin{pmatrix}
1&\operatorname{tr}B\\
\operatorname{tr}B&(\operatorname{tr}B)^2-\det B
\end{pmatrix},
\]
which is symmetric. Thus \(C^{\mathsf T}Q=QC\). The integral invertible matrix
\(S=PQ^{-1}P^{\mathsf T}\) satisfies
\(SB^{\mathsf T}S^{-1}=B\), hence
\(SA^{\mathsf T}S^{-1}=A\). Nothing used odd characteristic or a separability hypothesis. \(\square\)

**Theorem 3.4 — full unitary admissibility and the smooth module.** Every irreducible strongly continuous unitary representation of \(\mathrm{GL}_2(F)\) has finite-dimensional fixed spaces for all compact open subgroups. Its smooth vectors are dense and form an irreducible admissible smooth representation. In fact every irreducible \(K_0\)-type occurs at most once.

**Proof.** Transpose is a continuous anti-automorphism. The Haar density
\(|\det g|^{-2}d^4g\) in Section 1 is unchanged by it: transpose permutes the additive matrix coordinates and preserves determinant. Lemma 3.3 supplies the compact conjugacy required by Lemma 3.2. That lemma therefore proves the compact multiplicity bound without assuming smooth admissibility.

Let \(J\subset K_0\) be compact open. Its normal core
\(J_0=\bigcap_{k\in K_0}kJk^{-1}\) is open: the finite coset space \(K_0/J\) makes this a finite intersection. The \(J\)-fixed space is contained in the \(J_0\)-fixed space. Only compact types factoring through the finite group \(K_0/J_0\) can contribute to the latter, and each occurs at most once. There are finitely many such types and each is finite dimensional, so both spaces are finite dimensional. More explicitly,
\[
\dim\mathcal H^J
 \le\sum_{\rho\in\widehat{K_0/J_0}}\dim\rho
 \le [K_0:J_0].
\]
For the last bound embed one matrix-coefficient column of each irreducible type in the finite regular function space; compact orthogonality makes these subspaces independent. If \(J\) is not contained in \(K_0\), use \(J\cap K_0\), whose fixed space contains \(\mathcal H^J\).

Averaging over the shrinking \(K_n\) converges strongly to the identity: the norm difference on a vector is bounded by
\(\sup_{k\in K_n}\|\pi(k)v-v\|\), which tends to zero. Thus the smooth vectors
\(\mathcal H_{\rm sm}=\bigcup_J\mathcal H^J\) are dense.

Finally let \(W\) be a nonzero invariant algebraic subspace of \(\mathcal H_{\rm sm}\). Its Hilbert closure is group invariant and is all of \(\mathcal H\). Compact averaging preserves \(W\) algebraically, since the compact orbit of a smooth vector has finitely many values. Its averaged image in \(\mathcal H^J\) is dense; finite dimension makes it equal to \(\mathcal H^J\). Taking all \(J\) yields \(W=\mathcal H_{\rm sm}\). This proves smooth irreducibility as well as admissibility. The proof works over every nonarchimedean local field, including characteristic two. Getz–Hahn, Theorem 5.3.7, remains historical credit for the unitary admissibility assertion now proved here. \(\square\)


## 4. Schur's lemma before admissibility

**Theorem 4.1.** For an irreducible smooth representation of \(G\),
\(\operatorname{End}_G(V)=\mathbb C\).
It has a smooth central character.

**Proof.** Choose \(0\ne v\in V^J\). The cosets \(G/J\) are countable, because they are disjoint open sets in a second-countable space. The orbit span of \(v\) is all of \(V\) by irreducibility. Hence \(V\) has countable dimension.

Any nonzero commuting endomorphism has invariant kernel and image, so it is invertible. Suppose a commuting \(T\) is not scalar. Then every \(T-\lambda I\), \(\lambda\in\mathbb C\), is nonzero and invertible. For a fixed \(v\ne0\), the uncountable family
\((T-\lambda I)^{-1}v\)
is linearly independent. Indeed a finite relation with distinct \(\lambda_i\), after multiplication by \(\prod_i(T-\lambda_iI)\), gives \(p(T)v=0\), where
\(p(z)=\sum_i c_i\prod_{j\ne i}(z-\lambda_j)\).
If some \(c_i\ne0\), evaluation at \(\lambda_i\) makes \(p\ne0\). Over \(\mathbb C\), every nonzero polynomial factors into linear factors, each invertible at \(T\), so \(p(T)\) is invertible. This contradicts \(v\ne0\). Countable dimension cannot contain an uncountable independent family. Thus \(T\) is scalar.

Central matrices commute with the representation and act by scalars \(\omega(a)\). Multiplication makes \(\omega:F^\times\to\mathbb C^\times\) a character. A nonzero smooth vector is fixed by an open subgroup, so \(\omega\) is one on an open subgroup of the centre. It is therefore a smooth character. \(\square\)

This is the countable-dimension form of Schur's lemma, often called the Dixmier argument. It avoids using the admissibility theorem to supply an eigenvector in a finite-dimensional fixed space. If admissibility is already known, that shorter proof is available too.

## 5. The smooth dual and bidual

The full algebraic dual \(V^*=\operatorname{Hom}_{\mathbb C}(V,\mathbb C)\) has action
\((\pi^\vee(g)\ell)(v)=\ell(\pi(g^{-1})v)\), but most of its functionals need not have open stabilizers. Define the **contragredient** by

\[
V^\vee=(V^*)_{\rm sm}=\bigcup_K(V^*)^K.
\tag{5.1}
\]

This is a smooth representation. The pairing satisfies
\(\langle\pi(g)v,\ell\rangle=\langle v,\pi^\vee(g^{-1})\ell\rangle\).

**Lemma 5.1 — fixed-space duality.** Restriction gives a natural isomorphism

\[
(V^\vee)^K\simeq(V^K)^*.
\tag{5.2}
\]

**Proof.** For a \(K\)-fixed functional, averaging yields \(\ell(v)=\ell(e_Kv)\), so its restriction determines it. Any functional \(a\) on \(V^K\) extends to the \(K\)-fixed functional \(a\circ e_K\). These constructions are inverse. In particular smooth functionals separate all vectors: choose a subgroup fixing a given nonzero vector and a fixed-space functional nonzero on it. \(\square\)

**Theorem 5.2 — admissible reflexivity.** If \(V\) is admissible, \(V^\vee\) is admissible and the evaluation map

\[
V\longrightarrow(V^\vee)^\vee,
\qquad v\longmapsto(\ell\mapsto\ell(v)),
\tag{5.3}
\]

is a representation isomorphism. Moreover \(V\) is irreducible if and only if \(V^\vee\) is irreducible.

**Proof of reflexivity.** Equation (5.2) proves admissibility of the dual. A vector fixed by \(K\) gives a \(K\)-fixed evaluation functional, so (5.3) takes values in the smooth bidual. It is equivariant and injective by separation. On the \(K\)-fixed spaces it is exactly
\(V^K\to((V^K)^*)^*\): if \(v\in V^K\), evaluating a general \(\ell\) at \(v\) equals evaluating \(e_K\ell\). Finite dimension makes this map an isomorphism. Every smooth bidual vector is fixed by some \(K\), proving surjectivity.

**Proof of irreducibility.** Suppose \(V\) is irreducible and \(0\ne U\subset V^\vee\) is a submodule. Its annihilator in \(V\) is invariant and proper, hence zero. For a fixed \(K\), the annihilator of \(U^K=e_KU\) in \(V^K\) is also zero: for \(v\in V^K\), \((e_K\ell)(v)=\ell(v)\). Finite-dimensional duality now gives \(U^K=(V^\vee)^K\). Taking the union over \(K\) gives \(U=V^\vee\). Conversely apply this conclusion to the admissible \(V^\vee\) and use (5.3). \(\square\)

The same averages show that the smooth-dual functor is exact on admissible representations. Given a smooth functional on a subrepresentation \(W\subset V\) fixed by \(K\), extend its functional on \(W^K\) to \(V^K\), and compose with \(e_K\). This extends it smoothly to \(V\). The kernel of restriction consists exactly of the smooth functionals on \(V/W\). Thus
\(0\to(V/W)^\vee\to V^\vee\to W^\vee\to0\)
is exact. Subrepresentations and quotients remain admissible because taking compact invariants is exact: average a lift of any invariant quotient vector.

## 6. Finite-dimensional representations and examples

**Lemma 6.1.** Every open normal subgroup of \(\mathrm{GL}_2(F)\) contains \(\mathrm{SL}_2(F)\).

**Proof.** An open subgroup contains \(K_n\) for some \(n\), hence every upper unipotent \(n(x)\) with \(x\in\varpi^n\mathcal O\). Normality and
\(\operatorname{diag}(a,1)n(x)\operatorname{diag}(a^{-1},1)=n(ax)\)
then include every upper unipotent: scale any prescribed parameter into that ideal and conjugate back. Conjugation by the matrix interchanging the two coordinates includes every lower unipotent as well. Elementary row elimination over a field shows that these generate \(\mathrm{SL}_2(F)\). Explicitly, eliminate a nonzero pivot to leave \(\operatorname{diag}(a,a^{-1})\), and write this last matrix as \(w(a)w(-1)\), with
\(w(a)=n(a)\begin{pmatrix}1&0\\ -a^{-1}&1\end{pmatrix}n(a)=\begin{pmatrix}0&a\\ -a^{-1}&0\end{pmatrix}\).
A zero pivot is exchanged using \(w(1)\). This proves the claim. \(\square\)

**Proposition 6.2.** Every finite-dimensional irreducible smooth representation of \(G\) is \(\chi\circ\det\) for a smooth character \(\chi:F^\times\to\mathbb C^\times\).

**Proof.** Intersect the open stabilizers of a finite basis. This gives an open kernel, which is normal. By Lemma 6.1 it contains \(\mathrm{SL}_2(F)\), so the representation factors through the determinant quotient \(F^\times\). The image is commuting. Schur's lemma makes every image matrix scalar, and irreducibility makes the space one dimensional. The resulting character is smooth: \(a\mapsto\operatorname{diag}(a,1)\) is continuous and its inverse image of the open kernel is open. Conversely every such determinant character is one-dimensional smooth and irreducible. \(\square\)

The trivial representation has a one-dimensional fixed space for every compact open subgroup and \(\pi(f)=\int f\). For \(\chi\circ\det\), the fixed space for \(K\) is the whole line if \(\chi(\det K)=1\), and zero otherwise. In particular
\(\det K_n=1+\varpi^n\mathcal O\) for \(n\geq1\): the entry determinant is in this set, and \(\operatorname{diag}(u,1)\) realizes every \(u\) in it. Thus its fixed spaces record the conductor of \(\chi\). Its central character is \(\chi^2\) and its contragredient is \(\chi^{-1}\circ\det\). Admissibility is immediate.

As a first corner eigenvalue, take unramified \(\chi\) and \(T=1_{K_0\operatorname{diag}(\varpi,1)K_0}\). The familiar \(q+1\) right-coset decomposition from the lift lesson, Section 5, gives volume \(q+1\). On this support the determinant is \(\varpi\) times a unit, so

\[
\pi(T)=(q+1)\chi(\varpi).
\tag{6.1}
\]

This is an unnormalized characteristic-function eigenvalue. Dividing the operator by a power of \(q\) changes it; Haar normalization alone does not insert that factor.

For an example separating smoothness from admissibility, let the additive group \(F\) act on \(C_c^\infty(F)\) by \((\tau(t)f)(x)=f(x-t)\). A locally constant compact support is a finite union of cosets of one sufficiently small additive compact open subgroup, so every function has an open translation stabilizer. Yet the \(\mathcal O\)-fixed functions include \(1_{a+\mathcal O}\) for all \(a\in F/\mathcal O\). Their disjoint supports make them linearly independent, and \(F/\mathcal O\) is infinite. The fixed space is infinite dimensional, so this smooth representation of the additive group is not admissible. This does not contradict the proved theorem for irreducible smooth representations of GL₂.

## 7. Exercises with complete solutions

**Exercise 7.1 — compact-group semisimplicity.** Show that every smooth complex representation of a compact totally disconnected group is an algebraic direct sum of irreducible representations.

**Solution 7.1.** For a vector \(v\), its open stabilizer has finite index by compactness. The orbit span is finite dimensional. Intersect the finitely many conjugates of its stabilizer to obtain an open normal subgroup fixing that span, so it factors through a finite group. Maschke's theorem decomposes the span into simple submodules. As every vector belongs to such a span, the whole representation is a sum of simple submodules. Choose a maximal family whose sum is direct. If that sum were proper, some simple submodule in the preceding spanning family would not be contained in it. Its intersection with the sum is zero by simplicity, so it could be adjoined, a contradiction. Thus the maximal direct sum is the whole space. Multiplicities may be infinite; smoothness alone does not imply finite multiplicities.

**Exercise 7.2 — countable Schur.** Prove that every commuting endomorphism of an irreducible countable-dimensional complex representation is scalar, without assuming a fixed-space dimension bound.

**Solution 7.2.** Its nonzero commuting endomorphisms are invertible by their kernels and images. A nonscalar \(T\) would therefore have invertible \(T-\lambda I\) for every complex \(\lambda\). Fix \(v\ne0\). A finite linear relation among the vectors \((T-\lambda_iI)^{-1}v\) clears denominators to \(p(T)v=0\), with \(p(z)=\sum_i c_i\prod_{j\ne i}(z-\lambda_j)\). Distinct parameters and a nonzero coefficient make this polynomial nonzero by evaluation at that parameter. Factor it over \(\mathbb C\); every factor is invertible at \(T\), giving a contradiction. Hence the uncountable parameter set would produce uncountably many independent vectors, which countable dimension excludes. For \(\mathrm{GL}_2(F)\), countable dimension follows because one smooth cyclic vector has an open stabilizer and the corresponding coset set is countable. This proves Theorem 4.1 independently of admissibility.

**Exercise 7.3 — open normal subgroups.** Prove Lemma 6.1 and identify where normality is used.

**Solution 7.3.** Openness includes all upper unipotents with sufficiently small parameter. For arbitrary \(t\in F\), choose \(a\in F^\times\) with \(at\) sufficiently small. Conjugate \(n(at)\) by \(\operatorname{diag}(a^{-1},1)\) to get \(n(t)\). Normality is exactly what retains membership under this conjugation. Conjugation by the coordinate-interchange matrix similarly gives every lower unipotent. The explicit elementary-elimination and diagonal factorization in Lemma 6.1 express every determinant-one matrix as their product, so the normal subgroup contains \(\mathrm{SL}_2(F)\). Openness without normality would supply only the small parameters, as \(K_n\) illustrates.

**Exercise 7.4 — contragredient and irreducibility.** For admissible \(V\), prove smooth biduality and the equivalence of irreducibility with irreducibility of the smooth dual.

**Solution 7.4.** A \(K\)-fixed functional is uniquely determined by its restriction to \(V^K\), with inverse extension \(a\mapsto a\circ e_K\). Hence \((V^\vee)^K=(V^K)^*\), which is finite dimensional. Evaluation is equivariant, smooth and injective because these fixed-space functionals separate vectors. On each \(K\)-fixed space the evaluation map to the smooth bidual is the ordinary finite-dimensional bidual isomorphism. Taking the union proves its surjectivity.

If \(V\) is irreducible and \(U\ne0\) is a submodule of \(V^\vee\), its annihilator in \(V\) is an invariant proper subspace and thus zero. The annihilator of \(U^K\) in \(V^K\) is zero as well, since averaging a functional does not change its value on a fixed vector. Finite dimension gives \(U^K=(V^\vee)^K\). The union gives \(U=V^\vee\). Apply this implication to \(V^\vee\), which is admissible, and use biduality for the converse. The finite-dimensional argument is why the smooth bidual statement was made with admissibility rather than with smoothness alone.

## References

- H. Jacquet and R. P. Langlands, [*Automorphic Forms on GL(2)*](https://publications.ias.edu/sites/default/files/Automorphic-forms-on-GL2.pdf) (1970), §2, conditions (2.1)–(2.4), Lemma 2.5 and Proposition 2.7(a), for the foundational local framework and contragredients. This lesson proves the simple-corner reconstruction and countable Schur statement explicitly rather than incorporating admissibility into irreducibility.
- J. R. Getz and H. Hahn, *An Introduction to Automorphic Representations*, draft of 22 April 2022, §§5.1–5.4, especially Theorem 5.3.4 for smooth admissibility, proved for GL₂ in Lesson 6, Theorem 5.4, and Theorem 5.3.7 for unitary admissibility, proved directly here in Theorem 3.4. The [author's graduate-text page](https://sites.duke.edu/jgetz/graduate-text/) supplies the reference.
- NT-ADL-12, Proposition 12.1, owns the fixed-level Hecke double-coset algebra and its multiplication; From modular forms to adelic functions, Section 5, supplies the GL₂ right-coset calculation used in (6.1).
