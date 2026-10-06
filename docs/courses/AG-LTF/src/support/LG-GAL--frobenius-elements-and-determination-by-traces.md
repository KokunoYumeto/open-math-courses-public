# Frobenius elements and determination by traces

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

An unramified prime supplies a conjugacy class in a Galois group. Chebotarev's theorem says that these classes test every finite quotient. Continuity then lets them test ℓ-adic representations, and semisimplicity turns equality of traces into an isomorphism. These are three separate steps: the construction of a local subgroup, the density argument, and the linear algebra of characters.

We assume the preceding lesson, Profinite groups and ℓ-adic representations, and the prerequisite lessons *Hilbert's ramification theory in Galois extensions*, *Places of number fields in extensions and the product formula*, and *The Chebotarev density theorem*. Basic references are [Taylor 2004], [Milne 2020a] and [Deligne–Serre 1974]. We use arithmetic Frobenius throughout: it acts by \(x\mapsto x^{q_v}\) on the residue field. The inverse element is geometric Frobenius.

## 1. A local Galois group inside a global one

Let \(K\) be a number field, \(v\) a finite place, and \(K_v\) its completion. Choose an embedding \(\iota:\bar K\hookrightarrow\overline{K_v}\) extending the embedding of \(K\). It selects a prolongation \(\bar v\) of the valuation to \(\bar K\). Define
\[
 D_{\bar v}=\{g\in G_K:g\bar v=\bar v\}.
\]
The inertia subgroup \(I_{\bar v}\) consists of those elements of \(D_{\bar v}\) which act trivially on the residue field of \(\bar K\) at \(\bar v\).

For a finite Galois extension \(L/K\) inside \(\bar K\), the restriction \(w=\bar v|_L\) has decomposition and inertia groups \(D_w\) and \(I_w\). Finite ramification theory gives
\[
 D_w\simeq\operatorname{Gal}(L_w/K_v),
 \qquad I_w\simeq\operatorname{Gal}(L_w/L_w^{\mathrm{ur}}).
 \tag{1}
\]
Here the second notation means the inertia subgroup of the finite local Galois extension; \(L_w^{\mathrm{ur}}\) is its maximal unramified subextension. We now justify the passage to absolute groups, including the cofinality it requires.

**Lemma 1.1 (local cofinality).** Every finite extension of \(K_v\) inside \(\overline{K_v}\) is contained in the completion, at the chosen place, of a finite Galois extension of \(K\).

**Proof.** Let \(M/K_v\) be finite. Characteristic zero makes it separable. Choose a primitive element \(\alpha\), with minimal polynomial \(f\in K_v[X]\) of degree \(d\). Approximate the coefficients of this monic polynomial by coefficients in the dense subfield \(K\), obtaining \(h\in K[X]\) of degree \(d\). For sufficiently close coefficients, Hensel's lemma in the complete field \(M\), applied near the simple root \(\alpha\), gives a root \(\beta\in M\) of \(h\) arbitrarily close to \(\alpha\). Choose it close enough that Krasner's lemma gives \(K_v(\alpha)\subset K_v(\beta)\). The reverse inclusion holds because \(\beta\in M\); thus \(K_v(\beta)=M\).

The element \(\beta\) is algebraic over \(K\). Take the splitting field \(L/K\) of \(h\), embedded in \(\overline{K_v}\) so that it contains \(\beta\). Its completion contains \(K_v(\beta)=M\). This proves cofinality. \(\square\)

**Theorem 1.2.** Restriction along \(\iota\) gives an isomorphism of topological groups
\[
 G_{K_v}\simeq D_{\bar v}\subset G_K,
 \qquad I_{K_v}\simeq I_{\bar v}.
\]
The subgroup \(D_{\bar v}\) is closed. Changing \(\iota\) conjugates the pair \((D_{\bar v},I_{\bar v})\) in \(G_K\).

**Proof.** A \(K_v\)-automorphism of \(\overline{K_v}\) preserves the elements algebraic over \(K\), hence preserves \(\iota(\bar K)\), and preserves the valuation. This defines restriction into \(D_{\bar v}\). Formula (1) identifies the restrictions at every finite Galois level. By Lemma 1.1, the local completions in those levels are cofinal among finite local extensions. Consequently their finite Galois groups have inverse limit \(G_{K_v}\). On the global side the inverse limit of the \(D_w\) is exactly the group preserving \(\bar v\): preserving a valuation can be tested on every finite subextension. The finite-level identifications therefore give the asserted isomorphism. They also identify inertia, because triviality of the residue-field action can be tested on every finite residue extension.

Each \(D_w\) is closed in a finite discrete quotient. The inverse image conditions defining \(D_{\bar v}\) show that it is closed in \(G_K\). For conjugacy, prolongations of \(v\) in a finite Galois extension are conjugate. To arrange the conjugating element compatibly, for each finite Galois \(L\) consider the nonempty closed subset of \(G_K\) sending one selected place of \(L\) to the other. These subsets have the finite intersection property, by passing to a common finite Galois overfield. Compactness produces an element in their intersection. It conjugates both decomposition groups and both inertia groups. \(\square\)

For a finite place the residue field is \(\mathbb F_{q_v}\). The quotient is
\[
 D_{\bar v}/I_{\bar v}\simeq
 \operatorname{Gal}(\overline{\mathbb F}_{q_v}/\mathbb F_{q_v})
 \simeq\widehat{\mathbb Z}.
\]
The arithmetic Frobenius is the element corresponding to \(1\), characterized by \(x\mapsto x^{q_v}\). A **Frobenius lift** is any preimage of this element in \(D_{\bar v}\). There is generally no distinguished lift before one kills inertia.

## 2. Frobenius invariants of an unramified representation

A representation \(\rho:G_K\to\operatorname{GL}(V)\) is **unramified at \(v\)** if it is trivial on \(I_{\bar v}\). Conjugacy makes this condition independent of the chosen embedding. In this case put
\[
 P_v(X)=\det(X-\rho(\operatorname{Frob}_v)).
\]

**Proposition 2.1.** The polynomial \(P_v\), and consequently its trace and determinant, are independent of both the Frobenius lift and the prolongation of \(v\).

**Proof.** Two lifts differ by an element of inertia, which acts as the identity. Changing the prolongation conjugates the local subgroup and the Frobenius coset. Their images under \(\rho\) are conjugate matrices. A characteristic polynomial is invariant under conjugation. \(\square\)

**Example 2.2 (quadratic splitting).** In \(\mathbb Q(\sqrt d)/\mathbb Q\), with \(d\) squarefree, an odd prime not dividing \(d\) has arithmetic Frobenius equal to \(1\) when \(d\) is a square modulo \(p\), and equal to the nontrivial automorphism otherwise. Indeed \(\sqrt d\) lies in the residue field exactly in the first case; in the second case Frobenius exchanges the two roots in \(\mathbb F_{p^2}\). The sign is \(\left(\frac dp\right)\). For \(d=-1\), this recovers the calculation in the preceding lesson: the traces are \(1,-1,-1,1\) at \(p=5,3,7,13\), respectively.

**Example 2.3 (a cyclotomic quotient).** For \(p\nmid N\), arithmetic Frobenius in \(\operatorname{Gal}(\mathbb Q(\zeta_N)/\mathbb Q)\simeq(\mathbb Z/N\mathbb Z)^\times\) is \(p\bmod N\). The proof is reduction of roots of unity followed by the unique unramified lift, exactly as in Proposition 3.1 of the preceding lesson. With \(N=7\), Frobenius at \(2\) has order \(3\), since \(2,4,1\) are its successive powers modulo \(7\). Frobenius at \(3\) has order \(6\): its successive powers are \(3,2,6,4,5,1\).

## 3. What Chebotarev makes dense

Let \(S\) be a finite set of finite places. Let \(K_S\subset\bar K\) be the compositum of the finite extensions unramified at every finite place outside \(S\), and write \(G_{K,S}=\operatorname{Gal}(K_S/K)\). It is the quotient of \(G_K\) by the closed normal subgroup generated by the inertia groups outside \(S\). At \(v\notin S\), the Frobenius image in \(G_{K,S}\) is a well-defined conjugacy class.

We use the finite-extension Chebotarev theorem in the following precise form. If \(L/K\) is finite Galois with group \(H\), and \(C\subset H\) is a conjugacy class, the unramified places with Frobenius class \(C\) have Dirichlet density \(|C|/|H|>0\). Here Dirichlet density is computed with the weight \((Nv)^{-s}\), as \(s\to1^+\). A density-one set has complement of Dirichlet density zero. Removing finitely many places does not change the density.

**Theorem 3.1 (density of Frobenius elements).** Let \(T\) be a set of finite places of Dirichlet density one. The union of the Frobenius conjugacy classes at \(v\in T\setminus S\) is dense in \(G_{K,S}\).

**Proof.** It suffices to meet every basic open set. Such a set is the inverse image of a particular element \(h\) in a finite quotient \(H\) of \(G_{K,S}\). This quotient corresponds to a finite Galois extension \(L/K\) unramified outside \(S\). Chebotarev gives positive density to the places whose Frobenius belongs to the conjugacy class of \(h\). The complement of \(T\), and the finite set \(S\), cannot contain all these places. Choose one in \(T\setminus S\). Conjugating its Frobenius image gives an element mapping exactly to \(h\). It therefore lies in the specified basic open set. \(\square\)

This proof explains why the conjugates are included. Choosing one Frobenius representative at each prime does not by itself guarantee a dense subset of a nonabelian group. It also explains why equality on an arbitrary positive-density set is insufficient. In a quadratic extension, the trivial character and its nontrivial quadratic character agree at the split primes, a set of density \(1/2\).

## 4. The linear algebra behind trace comparison

The following lemma is the characteristic-zero trace form of Brauer–Nesbitt. Its proof works for an arbitrary group, with no topology or finiteness assumption on that group.

**Lemma 4.1.** Let \(V,W\) be finite-dimensional semisimple representations of a group \(G\) over a characteristic-zero field \(E\). If
\[
 \operatorname{tr}(g\mid V)=\operatorname{tr}(g\mid W)
 \quad\text{for every }g\in G,
\]
then \(V\simeq W\) over \(E\).

**Proof.** Set \(M=V\oplus W\), and let \(A\) be the \(E\)-linear span of the image of \(G\) in \(\operatorname{End}_E(M)\). Products of image elements are image elements, so \(A\) is a finite-dimensional algebra with identity. Its invariant subspaces are exactly the \(G\)-invariant subspaces. Hence \(M\) is a faithful semisimple \(A\)-module.

We describe the central projectors needed in the argument. Choose an \(E\)-basis \(m_1,\dots,m_d\) of \(M\). The map
\[
 A\longrightarrow M^d,\qquad a\longmapsto(am_1,\dots,am_d)
\]
is an injective map of left \(A\)-modules. A submodule of a finite direct sum of simple modules is again a direct sum of simple modules, so the left regular module \(A\) is semisimple. This elementary module fact can be proved by induction on the number of simple summands: project to the last simple summand, split off the kernel in the other summands, and, when the image is nonzero, represent the remaining submodule as the graph of a homomorphism to the complementary kernel summand.

Decompose the regular module into its isotypic parts \(A=\bigoplus_i A_i\), one for each isomorphism class of simple module occurring. Every right multiplication is a left-module homomorphism, so it preserves these isotypic parts. Thus each \(A_i\) is a two-sided ideal. The projection onto \(A_i\) commutes with left and right multiplication. If \(e_i\) is the projection of \(1\), its value at \(a\) is both \(ae_i\) and \(e_i a\). Consequently the \(e_i\) are central orthogonal idempotents, their sum is \(1\), and \(e_i\) acts as the identity on a simple module of type \(i\) and as zero on every other type. Every simple type in \(M\) occurs in \(A\), since \(A\to S\), \(a\mapsto as\), is a surjection for a nonzero vector in a simple module \(S\).

Equality of traces on \(G\) implies equality on its linear span \(A\). If \(S_i\) is the simple module of type \(i\), evaluation at \(e_i\) gives
\[
 m_i(V)\dim_ES_i=m_i(W)\dim_ES_i.
\]
Characteristic zero allows cancellation of the positive integer \(\dim_ES_i\). Thus all simple multiplicities agree, proving the isomorphism. The proof does not require \(E\) to be a splitting field. \(\square\)

**Theorem 4.2 (determination by Frobenius traces).** Let \(E/\mathbb Q_\ell\) be finite. Let \(\rho_1,\rho_2\) be semisimple continuous finite-dimensional representations of \(G_K\) over \(E\), both unramified outside a finite set \(S\). If their arithmetic-Frobenius traces agree at every prime in a Dirichlet-density-one set outside \(S\), then \(\rho_1\simeq\rho_2\).

**Proof.** Both representations factor through \(G_{K,S}\). Their trace functions are continuous, because matrix trace is continuous, and are invariant under conjugation. The hypothesis and Theorem 3.1 make them equal on a dense subset. Their difference is a continuous function into the Hausdorff field \(E\), with closed zero set. It therefore vanishes everywhere. Apply Lemma 4.1. \(\square\)

Equality of characteristic polynomials implies equality of traces and hence the same conclusion. Conversely an isomorphism implies equality of all such polynomials. Two representations which are not assumed semisimple still have isomorphic semisimplifications under the trace hypothesis; replacing each by its semisimplification preserves traces and characteristic polynomials. The unipotent representation of \(\mathbb Z_\ell\) in the preceding lesson and the two-dimensional trivial representation have identical traces and characteristic polynomials, but are not isomorphic. This exhibits the lost extension data.

For a one-dimensional representation, semisimplicity is automatic. Thus two ℓ-adic characters that agree at a density-one set of Frobenius elements are equal. In particular, a finite-order character of \(G_{\mathbb Q}\) trivial at almost all Frobenius elements is trivial. Such a character factors through a finite extension, so its finite ramification set supplies the required \(S\).

## 5. Exercises and complete solutions

**Exercise 5.1 (easy).** Prove that an unramified Frobenius characteristic polynomial is unaffected by changing the embedding or the lift.

**Solution.** A change of lift multiplies by an inertia element, which lies in the kernel of the representation. A change of embedding conjugates the decomposition and inertia groups and the chosen Frobenius class. The resulting matrices are conjugate. Taking \(\det(X-A)\) proves invariance, as in Proposition 2.1. If inertia acts nontrivially, the first argument fails and different lifts can have different characteristic polynomials.

**Exercise 5.2 (medium).** Deduce that a finite-order character of \(G_{\mathbb Q}\) which is trivial on almost all arithmetic Frobenius elements is trivial.

**Solution.** Its kernel cuts out a finite abelian extension \(L/\mathbb Q\). Take any element \(h\) of its Galois group. Chebotarev supplies positive density to the primes with Frobenius \(h\). Removing the finite exceptional set leaves a prime at which the character value is both the value at \(h\) and \(1\). Thus the character is \(1\) on every element of the finite quotient, and consequently on \(G_{\mathbb Q}\).

**Exercise 5.3 (medium).** Prove density of the Frobenius conjugacy classes in \(G_{K,S}\), retaining only a density-one set of primes.

**Solution.** A basic open neighbourhood specifies an element in a finite Galois quotient. Chebotarev supplies a positive-density set of primes for its conjugacy class. A zero-density complement cannot exhaust that set. Choose an allowed prime and conjugate its Frobenius representative to the specified element of the quotient. This meets the neighbourhood. This is exactly the finite-quotient argument of Theorem 3.1; no version of Chebotarev for an infinite extension is needed.

**Exercise 5.4 (hard).** Prove determination by traces for semisimple ℓ-adic representations over a finite extension of \(\mathbb Q_\ell\). Explain why neither an algebraically closed coefficient field nor finite image is necessary.

**Solution.** Pass to the common unramified-outside-\(S\) quotient. Use Exercise 5.3, conjugacy invariance, and continuity to deduce trace equality at every group element. Form the finite-dimensional algebra spanned by the images on the direct sum of the two spaces. Its regular module embeds in a finite direct sum of the faithful semisimple representation. The central isotypic projectors constructed in Lemma 4.1 compare each simple multiplicity by trace. This proves an isomorphism over the original field. Finite dimensionality of the image algebra follows from its inclusion in a matrix algebra, even when the group image is infinite. The projector argument uses simple modules over \(E\) itself, so scalar extension to an algebraic closure is unnecessary.

## What this lesson does not prove

Finite decomposition and inertia theory, including (1), is the prerequisite *Hilbert's ramification theory in Galois extensions* and its local-completion identification in *Places of number fields in extensions and the product formula*; see [Milne 2020a, Chapter 8, section on decomposition groups]. The finite-extension Chebotarev theorem is taken from *The Chebotarev density theorem*, also [Milne 2020b, Chapter VIII, §7]. Hensel's and Krasner's lemmas are the results of *Extensions of complete valued fields*, also [Milne 2020a, Chapter 7, Theorem 7.33 and Proposition 7.60]. Continuity of the roots under coefficient approximation is [Milne 2020a, Chapter 7, Propositions 7.61–7.63], and follows from the simple-root form of Hensel's lemma used in Lemma 1.1. The elementary classification of finite extensions of finite fields and the compactness of profinite groups are prerequisites. The passage to absolute decomposition groups, density deduction, and characteristic-zero trace comparison are proved here.

## References

- [Taylor 2004] Richard Taylor, *Galois representations*, Annales de la Faculté des sciences de Toulouse, series 6, 13 (2004), 73–119, §1. [Published article](https://www.numdam.org/item/AFST_2004_6_13_1_73_0/).
- [Deligne–Serre 1974] Pierre Deligne and Jean-Pierre Serre, *Formes modulaires de poids 1*, Annales scientifiques de l'École Normale Supérieure, series 4, 7 (1974), 507–530, §3, Lemma 3.2. [Published article](https://www.numdam.org/item/ASENS_1974_4_7_4_507_0/).
- [Milne 2020a] J. S. Milne, *Algebraic Number Theory*, version 3.08, 2020, Chapters 7–8. [Author's notes](https://www.jmilne.org/math/CourseNotes/ANT.pdf).
- [Milne 2020b] J. S. Milne, *Class Field Theory*, version 4.03, 2020, Chapter VIII, §7. [Author's notes](https://www.jmilne.org/math/CourseNotes/CFT.pdf).
