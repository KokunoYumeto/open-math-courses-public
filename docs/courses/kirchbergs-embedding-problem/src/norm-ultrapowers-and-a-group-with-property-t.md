# Norm ultrapowers and a group with property (T)

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

A theorem of Kirchberg and Phillips, quoted in [OpenAI-K, Section 1] and not used in this course, says that every separable unital exact C\*-algebra has a unital embedding into the Cuntz algebra \(\mathcal O_2\). *Kirchberg's embedding problem* asks whether every separable C\*-algebra embeds into a larger algebra built from \(\mathcal O_2\): its norm ultrapower \(\mathcal O_2^\omega\), in which a sequence of elements of \(\mathcal O_2\) is identified with another sequence if their difference tends to zero in norm along an ultrafilter \(\omega\). [OpenAI-K] gives a negative answer: an explicit group \(G\) whose full group C\*-algebra does not embed, with its unit, into \(B^\omega\) for any nuclear C\*-algebra \(B\) with a unit. This course gives the proof.

This lesson collects the facts on C\*-algebras that are used, introduces norm ultrapowers and full group C\*-algebras, states the theorem, and studies the group. One property of the group is taken from the literature as a named hypothesis: property (T) of the subgroup \(\Gamma=\mathbb Z^3\rtimes\mathrm{SL}_3(\mathbb Z)\).

- Facts on C\*-algebras (Section 1).
- Limits along an ultrafilter, norm ultrapowers, unitary lifts (Section 2).
- The full C\*-algebra of a group (Proposition 3.1).
- The embedding problem and the theorem (Section 4).
- The group \(G\), its subgroup \(\Gamma\), the endomorphism \(\theta\), a representation \(\pi_*\) (Section 5).
- Property (T) and the spectral gap (Section 6).

The lesson follows [OpenAI-K, Sections 1 and 2]. The prerequisites are named in Section 1.

## 1. Facts on C\*-algebras

All C\*-algebras are complex. A *unital* C\*-algebra has a unit \(1\ne0\). An *embedding* is an injective \(*\)-homomorphism; it is *unital* if it maps \(1\) to \(1\). The spectrum of an element \(x\) of a unital C\*-algebra is \(\operatorname{spec}x\). Inner products are linear in the first variable.

We use the following facts from the lesson [Order, local units and quotients of C\*-algebras](course:foundations-of-von-neumann-algebras/c-star-algebras-continuous-functional-calculus-automatic-continuity-positive-cones) (course *Foundations of von Neumann algebras*).

- (C1) A \(*\)-homomorphism between C\*-algebras is contractive (Theorem 4.2 there). A unital \(*\)-homomorphism does not enlarge spectra and commutes with the continuous functional calculus of normal elements (Corollary 5.4 there).
- (C2) An injective \(*\)-homomorphism is isometric (Corollary 4.6 there). Together with spectral permanence (Theorem 3.2 there): a unital embedding keeps the spectrum of every element.
- (C3) A self-adjoint element \(h\) is *positive*, \(h\ge0\), if its spectrum lies in \([0,\infty)\); the elements \(y^*y\) are positive (Theorem 8.2 there). The norm of a normal element is its spectral radius (Theorem 1.3 there).
- (C4) The quotient of a C\*-algebra by a closed two-sided ideal is a C\*-algebra (Theorem 15.1 there).

From (C3): if \(0\le h\le R\cdot1\) for a number \(R\), then \(R-h\) is positive with the spectrum \(R-\operatorname{spec}h\), so
\[
\min\operatorname{spec}h=R-\|R\cdot1-h\| .
\]
We refer to this as the *formula for the spectral minimum*.

- (C5) Every C\*-algebra has an injective \(*\)-homomorphism into the bounded operators \(\mathcal B(H)\) of a Hilbert space (the Gelfand–Naimark theorem: Theorem 7.2 of [Building representations from positive functionals](course:foundations-of-von-neumann-algebras/representations-and-positive-functionals-the-gns-construction-and-the-gelfand-naimark), same course). For a unital algebra, restricting to the range of the image of \(1\) gives a unital one. We call this a *faithful unital representation*.
- (C6) For a unital C\*-algebra \(C\) and \(d\ge1\), the algebra \(M_d(C)\) of the \(d\times d\) matrices over \(C\) is a C\*-algebra: if \(C\subseteq\mathcal B(H)\), then \(M_d(C)\) acts on \(H^d\), and by (C2) the norm does not depend on the choice of \(H\). For a matrix \(c=(c_{kl})\),
\[
\max_{k,l}\|c_{kl}\|\le\|c\|\le\sum_{k,l}\|c_{kl}\| .
\]
A unital \(*\)-homomorphism \(\Phi\) from \(C\) to \(C'\) induces the unital \(*\)-homomorphism \((c_{kl})\mapsto(\Phi(c_{kl}))\) from \(M_d(C)\) to \(M_d(C')\), which is injective if \(\Phi\) is.

An element \(u\) of a unital C\*-algebra is *unitary* if \(u^*u=uu^*=1\); the unitaries form a group \(\mathcal U(C)\).

## 2. Ultrafilters and norm ultrapowers

**Definition.** An *ultrafilter* on \(\mathbb N=\{1,2,\dots\}\) is a family \(\omega\) of subsets of \(\mathbb N\) such that: the empty set is not in \(\omega\); with two sets their intersection is in \(\omega\); with a set every larger set is in \(\omega\); and for every \(E\subseteq\mathbb N\), either \(E\) or its complement is in \(\omega\). It is *free* if it contains no finite set. The sets in \(\omega\) are called *large*.

Finitely many large sets have a large intersection, and of finitely many sets with union \(\mathbb N\) at least one is large.

**Lemma 2.1** (limits along \(\omega\)). Let \((a_n)\) be a bounded sequence of real numbers. There is exactly one real number \(a\), written \(\lim_\omega a_n\), such that \(\{n:|a_n-a|<\varepsilon\}\) is large for every \(\varepsilon>0\). The map \((a_n)\mapsto\lim_\omega a_n\) is linear and monotone, and:

1. if \(a_n\le c\) for all \(n\) in a large set, then \(\lim_\omega a_n\le c\); likewise for \(\ge\);
2. if \(\lim_\omega a_n<c\), then \(\{n:a_n<c\}\) is large;
3. if \(\omega\) is free and \(a_n\to a\) in the ordinary sense, then \(\lim_\omega a_n=a\).

**Proof.** Let \(|a_n|\le m\). Halve the interval \([-m,m]\); the indices \(n\) with \(a_n\) in the left half, or those with \(a_n\) in the right half, form a large set. Keep such a half and repeat. This gives nested closed intervals of lengths \(2m/2^k\), each containing \(a_n\) for a large set of \(n\); let \(a\) be their common point. For \(\varepsilon>0\) one of the intervals lies in \((a-\varepsilon,a+\varepsilon)\). If \(a'\ne a\) had the same property, the two large sets for \(\varepsilon=|a-a'|/2\) would be disjoint, and their intersection, the empty set, would be large. Linearity and monotonicity follow by intersecting large sets. Parts 1 and 2 are immediate from the definition. For part 3, the set \(\{n:|a_n-a|<\varepsilon\}\) has a finite complement, and a free ultrafilter contains the complements of finite sets. \(\blacksquare\)

Let \(C_1,C_2,\dots\) be unital C\*-algebras. The bounded sequences \((c_n)\) with \(c_n\in C_n\) form a unital C\*-algebra \(\prod_nC_n\) with the operations in each coordinate and the norm \(\sup_n\|c_n\|\). The set
\[
I_\omega=\bigl\{(c_n):\ \lim_\omega\|c_n\|=0\bigr\}
\]
is a closed two-sided ideal, closed under the adjoint. The quotient \(\prod_nC_n/I_\omega\) is a unital C\*-algebra by (C4), the *ultraproduct* of the \(C_n\). The class of \((c_n)\) is written \([(c_n)]\). If all \(C_n\) are one algebra \(B\), the ultraproduct is the *norm ultrapower* \(B^\omega\).

**Lemma 2.2.** \(\|[(c_n)]\|=\lim_\omega\|c_n\|\).

**Proof.** Let \(c=\lim_\omega\|c_n\|\). If \((e_n)\in I_\omega\), then \(\sup_n\|c_n+e_n\|\ge\lim_\omega\|c_n+e_n\|=c\). So the quotient norm is at least \(c\). For \(\varepsilon>0\) the set \(E\) of the \(n\) with \(\|c_n\|<c+\varepsilon\) is large; replacing \(c_n\) by \(0\) outside \(E\) changes the sequence by an element of \(I_\omega\) and gives a sequence of norm at most \(c+\varepsilon\). \(\blacksquare\)

**Lemma 2.3.** Let \(R>0\) and let \(P_n\in C_n\) be self-adjoint with \(0\le P_n\le R\cdot1\). Then \(P=[(P_n)]\) satisfies \(0\le P\le R\cdot1\) and
\[
\min\operatorname{spec}P=\lim_\omega\,\min\operatorname{spec}P_n .
\]

**Proof.** \(P_n=y_n^*y_n\) with \(\|y_n\|^2\le R\), so \(P=[(y_n)]^*[(y_n)]\ge0\); likewise \(R-P\ge0\). By the formula for the spectral minimum and Lemma 2.2,
\[
\begin{aligned}
\min\operatorname{spec}P&=R-\|R\cdot1-P\|\\
&=\lim_\omega\bigl(R-\|R\cdot1-P_n\|\bigr) ,
\end{aligned}
\]
and \(R-\|R\cdot1-P_n\|=\min\operatorname{spec}P_n\). \(\blacksquare\)

**Lemma 2.4** (unitary lifts). Every unitary of \(\prod_nC_n/I_\omega\) is the class of a sequence \((x_n)\) of unitaries \(x_n\in C_n\).

**Proof.** Let \([(y_n)]\) be unitary. Then \(\lim_\omega\|y_n^*y_n-1\|=0\) and \(\lim_\omega\|y_ny_n^*-1\|=0\). Let \(E\) be the large set of the \(n\) for which both norms are less than \(\tfrac12\). For \(n\in E\) the elements \(y_n^*y_n\) and \(y_ny_n^*\) are invertible, so \(y_n\) has a left and a right inverse and is invertible. Put \(x_n=y_n(y_n^*y_n)^{-1/2}\). Then \(x_n^*x_n=1\) and \(x_n\) is invertible, so \(x_n\) is unitary. With \(\varepsilon_n=\|y_n^*y_n-1\|\), the spectrum of \(y_n^*y_n\) lies in \([1-\varepsilon_n,1+\varepsilon_n]\), and the functional calculus gives
\[
\|x_n-y_n\|\le\|y_n\|\,\sup_{|r-1|\le\varepsilon_n}\bigl|r^{-1/2}-1\bigr| ,
\]
which tends to \(0\) along \(\omega\). For \(n\notin E\) put \(x_n=1\). Then \((x_n-y_n)\in I_\omega\). \(\blacksquare\)

**Lemma 2.5** (matrices). For \(d\ge1\), the map that sends the matrix \(([(c^{kl}_n)])_{k,l}\) to the class of the sequence of the matrices \((c^{kl}_n)_{k,l}\) is a \(*\)-isomorphism
\[
M_d\Bigl(\prod_nC_n/I_\omega\Bigr)\ \cong\ \prod_nM_d(C_n)/I_\omega .
\]

**Proof.** By the two bounds of (C6), a sequence of matrices is bounded exactly if each of its \(d^2\) sequences of entries is bounded, and its norms tend to \(0\) along \(\omega\) exactly if this holds for each sequence of entries. So the map is well defined, injective and surjective; it respects the operations. \(\blacksquare\)

## 3. The full C\*-algebra of a group

Let \(G\) be a group; it carries no topology. A *unitary representation* of \(G\) on a Hilbert space \(H\) is a homomorphism \(\sigma\) from \(G\) into the unitary group of \(\mathcal B(H)\). More generally we consider homomorphisms from \(G\) into the unitary group \(\mathcal U(C)\) of a unital C\*-algebra.

The *group algebra* \(\mathbb C[G]\) consists of the formal sums \(x=\sum_ga_g\,g\) with finitely many coefficients \(a_g\ne0\), with the product that extends the product of \(G\) and with \(x^*=\sum_g\overline{a_g}\,g^{-1}\). A unitary representation \(\sigma\) extends to \(\sigma(x)=\sum_ga_g\sigma(g)\), and \(\|\sigma(x)\|\le\sum_g|a_g|\). Put
\[
\|x\|=\sup_\sigma\|\sigma(x)\| ,
\]
the supremum over all unitary representations of \(G\) on Hilbert spaces; this is the supremum of a set of real numbers bounded by \(\sum_g|a_g|\). It is a seminorm with \(\|xy\|\le\|x\|\|y\|\) and \(\|x^*x\|=\|x\|^2\), because each \(\|\sigma(\cdot)\|\) has these properties. It is a norm: in the representation \(\lambda\) of \(G\) on \(\ell^2(G)\) by left translation, \(\lambda(x)\) maps the basis vector of the unit element to the vector with the coordinates \(a_g\).

**Definition.** The *full group C\*-algebra* \(C^*(G)\) is the completion of \(\mathbb C[G]\) for this norm. The image of \(g\in G\) is a unitary \(u_g\in C^*(G)\).

**Proposition 3.1.** \(C^*(G)\) is a unital C\*-algebra, and \(g\mapsto u_g\) is a homomorphism into its unitary group. For every homomorphism \(\varrho\) from \(G\) into the unitary group of a unital C\*-algebra \(C\) there is exactly one unital \(*\)-homomorphism from \(C^*(G)\) to \(C\) with \(u_g\mapsto\varrho(g)\) for all \(g\). If \(G\) is countable, \(C^*(G)\) is separable.

**Proof.** The completion of a normed \(*\)-algebra with \(\|xy\|\le\|x\|\|y\|\) and \(\|x^*x\|=\|x\|^2\) is a C\*-algebra. Let \(\varrho\) be given, and choose a faithful unital representation of \(C\) on a Hilbert space by (C5). Then \(\varrho\) is a unitary representation of \(G\), so \(\|\varrho(x)\|\le\|x\|\) for \(x\in\mathbb C[G]\) by the definition of the norm. So \(x\mapsto\varrho(x)\) extends by continuity to \(C^*(G)\), with values in the closed subalgebra \(C\). It is unique because \(\mathbb C[G]\) is dense. For countable \(G\) the sums with coefficients in \(\mathbb Q+i\mathbb Q\) are countable and dense. \(\blacksquare\)

In particular every unitary representation of \(G\) on a Hilbert space extends to a unital \(*\)-homomorphism of \(C^*(G)\) into \(\mathcal B(H)\).

## 4. The embedding problem and the theorem

A C\*-algebra \(B\) is *nuclear* if for every C\*-algebra \(C\) the algebraic tensor product of \(B\) and \(C\) has only one C\*-norm; the precise form in which this is used, and examples, are given in the next lesson. The *Cuntz algebra* \(\mathcal O_2\) is the universal unital C\*-algebra generated by two isometries \(s_1,s_2\) with \(s_1s_1^*+s_2s_2^*=1\).

**Hypothesis (O)** (Cuntz). The C\*-algebra \(\mathcal O_2\) is nuclear.

This statement is not proved in the programme. It is used only to pass from Theorem 4.1 to Corollary 4.2.

*Kirchberg's embedding problem* asks whether every separable unital C\*-algebra has a unital embedding into \(\mathcal O_2^\omega\) for a free ultrafilter \(\omega\) on \(\mathbb N\) [GS, Section 3.1].

Let \(\mathbb Z[\tfrac12]\) be the ring of the rational numbers whose denominator is a power of \(2\). Let \(G\) be the set of the triples \((v,M,k)\) with \(v\in\mathbb Z[\tfrac12]^3\) (a column vector), \(M\in\mathrm{SL}_3(\mathbb Z)\) and \(k\in\mathbb Z\), with the product
\[
\begin{aligned}
&(v,M,k)\,(w,N,l)\\
&\qquad=(v+2^kMw,\ MN,\ k+l) .
\end{aligned}
\]
This is the semidirect product \(\mathbb Z[\tfrac12]^3\rtimes(\mathrm{SL}_3(\mathbb Z)\times\mathbb Z)\), in which \((M,k)\) acts on vectors by \(v\mapsto2^kMv\) (Lemma 5.1). The group \(G\) is countable.

**Theorem 4.1** ([OpenAI-K, Section 1]). Assume the hypothesis (T) of Section 6. Let \(A=C^*(G)\). For every nuclear unital C\*-algebra \(B\) and every free ultrafilter \(\omega\) on \(\mathbb N\) there is no unital embedding of \(A\) into \(B^\omega\).

**Corollary 4.2.** Assume (T) and (O). The separable unital C\*-algebra \(C^*(G)\) has no unital embedding into \(\mathcal O_2^\omega\), for any free ultrafilter \(\omega\). So the answer to Kirchberg's embedding problem is negative.

The group and the algebra do not depend on \(B\) or on \(\omega\). The theorem is proved in [Predecessors and the contradiction](predecessors-and-the-contradiction.md), with the tools of [A spectral test and nuclear finiteness](a-spectral-test-and-nuclear-finiteness.md).

## 5. The group

**Lemma 5.1.** 1. \(G\) is a group, with the unit \((0,I,0)\).

2. \(\Gamma=\{(v,M,0):v\in\mathbb Z^3\}\) is a subgroup. We write its elements as \((v,M)\); then \((v,M)(w,N)=(v+Mw,MN)\).

3. Let \(t=(0,I,1)\). The map \(\theta(v,M)=(2v,M)\) is an injective homomorphism from \(\Gamma\) to \(\Gamma\), and
\[
t\,\gamma\,t^{-1}=\theta(\gamma)\qquad(\gamma\in\Gamma) .
\]

4. The image \(\Lambda=\theta(\Gamma)\) consists of the \((v,M)\) with \(v\in2\mathbb Z^3\). The eight elements \(r_a=(a,I)\), \(a\in\{0,1\}^3\), represent the left cosets of \(\Lambda\): every \(\gamma\in\Gamma\) is \(r_a\lambda\) for exactly one \(a\) and one \(\lambda\in\Lambda\).

**Proof.** *Part 1.* The map \((M,k)\mapsto(v\mapsto2^kMv)\) is a homomorphism from \(\mathrm{SL}_3(\mathbb Z)\times\mathbb Z\) into the automorphisms of the additive group \(\mathbb Z[\tfrac12]^3\), because \(2^kM\) and \(2^lN\) multiply to \(2^{k+l}MN\). The product of \(G\) is the semidirect product for this action; associativity follows from this, and the inverse of \((v,M,k)\) is \((-2^{-k}M^{-1}v,M^{-1},-k)\).

*Part 2.* For \(k=l=0\) and integer vectors the product has an integer vector, and so has the inverse.

*Part 3.* The product \((v,M)(w,N)=(v+Mw,MN)\) is mapped by \(\theta\) to \((2v+2Mw,MN)\), which is \(\theta(v,M)\,\theta(w,N)\); and \(\theta\) is injective. Further \(t\,(v,M,0)=(2v,M,1)\) and \(t^{-1}=(0,I,-1)\), so \(t(v,M,0)t^{-1}=(2v+2M\cdot0,\ M,\ 0)\).

*Part 4.* Write \(v=a+2w\) with \(a\in\{0,1\}^3\) and \(w\in\mathbb Z^3\); then \((v,M)=(a,I)(2w,M)\). The vector \(a\) is the residue of \(v\) modulo \(2\), so it is determined. \(\blacksquare\)

So \(\theta\) is an isomorphism of \(\Gamma\) onto its subgroup \(\Lambda\) of index \(8\), and inside the larger group \(G\) it is a conjugation. This is the feature of \(G\) that the proof uses.

**Lemma 5.2.** The group \(\mathrm{SL}_3(\mathbb Z)\) is generated by the six matrices \(I+E_{ij}\), \(i\ne j\), where \(E_{ij}\) has the entry \(1\) at the place \((i,j)\) and \(0\) elsewhere. So \(\Gamma\) is generated by the nine elements \((e_i,I)\), \(i=1,2,3\), and \((0,I+E_{ij})\), where \(e_i\) are the unit vectors.

**Proof.** Multiplying a matrix from the left by \((I+E_{ij})^c\), \(c\in\mathbb Z\), adds \(c\) times the row \(j\) to the row \(i\). We show that every \(M\in\mathrm{SL}_3(\mathbb Z)\) can be brought to \(I\) by such operations; then \(M\) is a product of the inverses.

The entries of the first column have the greatest common divisor \(1\), because \(\det M=1\). As long as two entries of the first column are nonzero, subtract a multiple of the row with the entry of smaller absolute value from the other row to make its entry smaller in absolute value. This ends with a first column with one nonzero entry \(\epsilon=\pm1\). If it stands in a row \(i\ne1\): add \(\epsilon\) times the row \(i\) to the row \(1\), then subtract \(\epsilon\) times the row \(1\) from the row \(i\); the column is \((1,0,0)\). If it stands in the row \(1\) and \(\epsilon=-1\): add the row \(1\) to the row \(2\), subtract twice the row \(2\) from the row \(1\), add the row \(1\) to the row \(2\); the column is \((1,0,0)\).

Operations among the rows \(2\) and \(3\) keep the first column. The lower right \(2\times2\) block has the determinant \(1\). The same procedure for its first column gives the second column \((*,1,0)\). The matrix is upper triangular with the diagonal \((1,1,\delta)\) and determinant \(1\), so \(\delta=1\). Subtracting multiples of the lower rows from the upper rows clears the entries above the diagonal.

For \(\Gamma\): \((v,M)=(v,I)(0,M)\), and \((v,I)\) is a product of powers of the \((e_i,I)\). \(\blacksquare\)

A unitary representation \(\pi\) of a group on a nonzero Hilbert space \(V\) of finite dimension is *irreducible* if \(V\) has no invariant subspace other than \(\{0\}\) and \(V\). Two representations \(\pi\) on \(V\) and \(\pi'\) on \(V'\) are *equivalent*, \(\pi\simeq\pi'\), if there is a unitary \(w\) from \(V\) onto \(V'\) with \(w\pi(g)=\pi'(g)w\) for all \(g\). The orthogonal complement of an invariant subspace of a unitary representation is invariant; so every unitary representation of finite dimension is an orthogonal direct sum of irreducible ones.

**Lemma 5.3.** There is an irreducible unitary representation \(\pi_*\) of \(\Gamma\) of finite dimension such that \(\pi_*(v,M)\) depends only on the residues of \(v\) and \(M\) modulo \(2\), and \(\pi_*(v,I)\ne1\) for some \(v\in\mathbb Z^3\). For every \(j\ge1\), the representation \(\pi_*\circ\theta^j\) is not equivalent to \(\pi_*\).

**Proof.** Reducing the entries modulo \(2\) is a homomorphism from \(\Gamma\) into the finite group of the pairs \((\bar v,\bar M)\), \(\bar v\in(\mathbb Z/2)^3\), \(\bar M\in\mathrm{SL}_3(\mathbb Z/2)\), with the product \((\bar v,\bar M)(\bar w,\bar N)=(\bar v+\bar M\bar w,\bar M\bar N)\). Let \(F\) be its image. The representation of \(F\) on \(\ell^2(F)\) by left translation is injective. Decompose it into irreducible representations of \(F\). The image \(f\) of \((e_1,I)\) is not the unit of \(F\), so it acts nontrivially in one of the irreducible summands. Let \(\pi_*\) be this summand, composed with the reduction. It is irreducible because the reduction maps \(\Gamma\) onto \(F\).

For \(j\ge1\), \(\theta^j(v,I)=(2^jv,I)\) has the residues \((0,I)\). So \(\pi_*\circ\theta^j\) is trivial on all \((v,I)\), while \(\pi_*\) is not. Equivalent representations are trivial on the same elements. \(\blacksquare\)

An explicit choice of dimension \(7\) is given in Exercise 7.5.

## 6. Property (T)

Let \(\sigma\) be a unitary representation of a group \(\Gamma\) on \(H\). A vector \(\xi\) is *invariant* if \(\sigma(g)\xi=\xi\) for all \(g\in\Gamma\).

**Definition.** A group \(\Gamma\) has *property (T)* if there are a finite set \(S_0\subseteq\Gamma\) and \(\varepsilon_0>0\) such that every unitary representation \(\sigma\) of \(\Gamma\) that has a unit vector \(\xi\) with \(\|\sigma(s)\xi-\xi\|<\varepsilon_0\) for all \(s\in S_0\) has a nonzero invariant vector. The pair \((S_0,\varepsilon_0)\) is a *Kazhdan pair*.

For countable groups this is equivalent to the usual definition, that every unitary representation with almost invariant vectors has a nonzero invariant vector (Exercise 7.1).

**Hypothesis (T)** (Kazhdan; in this form [dC, Proposition 1.1] with \(n=3\), \(m=1\)). The group \(\Gamma=\mathbb Z^3\rtimes\mathrm{SL}_3(\mathbb Z)\) of Lemma 5.1 has property (T).

This statement is not proved in the programme. The group \(\mathbb Z\) does not have property (T) (Exercise 7.2), and neither does \(\mathbb Z^3\); the hypothesis rests on the interplay of \(\mathrm{SL}_3(\mathbb Z)\) with the translations.

**Lemma 6.1** (the gap). Assume (T). There are a finite set \(S\) that generates \(\Gamma\) and a number \(\kappa\) with \(0<\kappa\le4|S|\) such that for every unitary representation \(\sigma\) of \(\Gamma\) on \(H\) without nonzero invariant vectors and every \(\xi\in H\),
\[
\sum_{s\in S}\|\sigma(s)\xi-\xi\|^2\ge\kappa\,\|\xi\|^2 .
\]

**Proof.** Let \((S_0,\varepsilon_0)\) be a Kazhdan pair, let \(S\) be the union of \(S_0\) and the nine generators of Lemma 5.2, and \(\kappa=\min\{\varepsilon_0^2,4|S|\}\). If \(\sigma\) has no nonzero invariant vector, then for every unit vector \(\xi\) there is \(s\in S_0\) with \(\|\sigma(s)\xi-\xi\|\ge\varepsilon_0\). So the sum is at least \(\varepsilon_0^2\) for unit vectors. \(\blacksquare\)

From here on \(S\) and \(\kappa\) are fixed as in Lemma 6.1, and \(R=4|S|\).

## 7. Exercises

**7.1.** Let \(\Gamma\) be a countable group. Say that a unitary representation has *almost invariant vectors* if for every finite \(S_0\subseteq\Gamma\) and every \(\varepsilon>0\) it has a unit vector \(\xi\) with \(\|\sigma(s)\xi-\xi\|<\varepsilon\) for all \(s\in S_0\). Show that \(\Gamma\) has a Kazhdan pair if and only if every unitary representation with almost invariant vectors has a nonzero invariant vector.

**7.2.** Show that \(\mathbb Z\) does not have property (T).

**7.3.** Let \(\omega\) be a free ultrafilter. Show that \(\lim_\omega(-1)^n\) is \(1\) or \(-1\), and that both cases occur for suitable \(\omega\), given that free ultrafilters containing a prescribed infinite set exist.

**7.4.** Show that \(b\mapsto[(b,b,b,\dots)]\) is a unital embedding of \(B\) into \(B^\omega\), and that \(\mathbb C^\omega=\mathbb C\).

**7.5.** Let \(\Gamma\) act on the eight points of \(X=(\mathbb Z/2)^3\) by \((v,M)\cdot x=\bar Mx+\bar v\), and let \(\pi_7\) be the representation of \(\Gamma\) on the functions on \(X\) with sum zero, \((\pi_7(g)\varphi)(x)=\varphi(g^{-1}\cdot x)\). Show that \(\pi_7\) is irreducible and has the properties of \(\pi_*\) in Lemma 5.3.

## 8. Solutions

**7.1.** If \((S_0,\varepsilon_0)\) is a Kazhdan pair, a representation with almost invariant vectors has a unit vector as in the definition, so a nonzero invariant vector. Conversely suppose there is no Kazhdan pair. List \(\Gamma=\{g_1,g_2,\dots\}\). For every \(m\) the pair \((\{g_1,\dots,g_m\},1/m)\) is not a Kazhdan pair: there is a representation \(\sigma_m\) on \(H_m\) without nonzero invariant vectors and with a unit vector \(\xi_m\) such that \(\|\sigma_m(g_i)\xi_m-\xi_m\|<1/m\) for \(i\le m\). The direct sum of the \(\sigma_m\) has almost invariant vectors, the \(\xi_m\). An invariant vector of the direct sum has invariant components, so it is \(0\).

**7.2.** Let \(\sigma\) be the representation of \(\mathbb Z\) on \(\ell^2(\mathbb Z)\) by translation. An invariant vector has constant coordinates, so it is \(0\). Let \(\xi_N\) be \(N^{-1/2}\) times the indicator function of \(\{1,\dots,N\}\). Then \(\|\sigma(k)\xi_N-\xi_N\|^2=2|k|/N\) for \(|k|\le N\), which tends to \(0\) for every fixed \(k\). So for every finite \(S_0\) and \(\varepsilon_0\) some \(\xi_N\) violates the definition.

**7.3.** The even numbers or the odd numbers form a large set; on it the sequence is constant. An ultrafilter that contains the set of even numbers gives \(1\), one that contains the odd numbers gives \(-1\).

**7.4.** The map is a unital \(*\)-homomorphism, and \(\|[(b,b,\dots)]\|=\|b\|\) by Lemma 2.2. For \(B=\mathbb C\), a bounded sequence \((c_n)\) differs from the constant sequence \(\lim_\omega c_n\) by an element of \(I_\omega\): apply Lemma 2.1 to the real and imaginary parts.

**7.5.** The action is well defined and depends only on residues modulo \(2\); the translation by \(e_1\) moves every point, so \(\pi_7(e_1,I)\ne1\): for instance it maps the function with the values \(1\) at \(0\) and \(-1\) at \(\bar e_1\) to its negative. For irreducibility let \(P\) be the representation on all functions on \(X\). An operator that commutes with \(P\) has a matrix \((m_{xy})\) with \(m_{g\cdot x,g\cdot y}=m_{xy}\). The group acts transitively on the pairs \((x,x)\) and transitively on the pairs \((x,y)\) with \(x\ne y\): translations move any point to \(0\), and for \(y,y'\ne0\) there is a matrix in \(\mathrm{SL}_3(\mathbb Z)\) whose reduction maps \(y\) to \(y'\), because the reductions of the matrices \(I+E_{ij}\) add one coordinate to another and connect all nonzero vectors of \((\mathbb Z/2)^3\). So the commuting operators form a space of dimension \(2\). If the functions of sum zero had a proper nonzero invariant subspace, the orthogonal projections onto it, onto its complement in the functions of sum zero, and onto the constants would be three linearly independent commuting operators.

## References

- [OpenAI-K] OpenAI, *An explicit obstruction to nuclear norm-ultrapower embeddings*, OpenAI Math Release preprint, 23 September 2026, Sections 1 and 2. https://github.com/openai/math/tree/main/preprints/An-explicit-obstruction-to-nuclear-norm-ultrapower-embeddings-September-23-2026
- [GS] I. Goldbring and T. Sinclair, *On Kirchberg's embedding problem*, arXiv:1404.1861, version 6, Section 3.1. https://arxiv.org/abs/1404.1861
- [dC] Y. de Cornulier, *Finitely presentable, non-Hopfian groups with Kazhdan's Property (T) and infinite outer automorphism group*, arXiv:math/0502140, version 4, Proposition 1.1. https://arxiv.org/abs/math/0502140
