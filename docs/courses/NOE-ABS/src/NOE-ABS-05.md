# Normal integral bases in tame extensions

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by GPT-6.1 Sol (OpenAI). Public domain (CC0).*

A field can have a basis consisting of the conjugates of one element even when its ring of integers cannot. The obstruction is already visible in the trace. In a tame extension the trace supplies the averaging operation needed for projectivity; an additional argument turns that projectivity into a normal integral basis over a local base.

We assume Three differents, the decomposition of primes in a finite Galois extension, completion of finite modules over a DVR, and elementary group representations. For number fields, the prime-transitivity and inertia results are Hilbert's ramification theory in Galois extensions, Theorems 6.1 and 6.2. Its residue fields are finite; the argument below retains arbitrary residue fields. The arithmetic different is treated in **The different and the discriminant**, and the field normal basis theorem, over every base field and in every characteristic, is proved in [Hilbert 90 in Noether's form and Galois descent, Theorem 4.0](https://kokunoyumeto.github.io/open-math-courses-public/courses/NOE-HYP/NOE-HYP-06.html#normal-bases-in-every-characteristic). The characteristic-zero projective rigidity theorem is stated below with its exact source. The positive-characteristic step is proved below. Basic references are [Noether], [Milne FT] and [Swan].

## 1. The integral question and the meaning of local

Let \(A\) be a Dedekind domain with fraction field \(K\), let \(L/K\) be finite Galois with group \(G\), and let \(B\) be the integral closure of \(A\) in \(L\). The finiteness theorem in Noether's axioms for Dedekind domains makes \(B\) finite over \(A\). For a nonzero prime \(\mathfrak p\), put

\[
 R=A_{\mathfrak p},\qquad M=B\otimes_A R,\qquad
 \widehat R=\varprojlim R/\mathfrak p^nR,\qquad
 \widehat M=M\otimes_R\widehat R.
\]

Here “localized” refers to \(R,M\), and “completed” to \(\widehat R,\widehat M\). The latter is generally a product, not a domain:

\[
 \widehat M=\prod_{\mathfrak P\mid\mathfrak p}\widehat{B_{\mathfrak P}}.
\]

The group acts on this entire product, permuting its factors. Its fraction algebra is \(L\otimes_K\operatorname{Frac}(\widehat R)\).

A **normal integral basis generator** is an element \(a\in M\) for which \(\{g(a):g\in G\}\) is an \(R\)-basis. Equivalently, the map \(R[G]\to M\), \(g\mapsto g(a)\), is an isomorphism of left modules. The completed definition is identical. Both underlying modules are free of rank \(|G|\) over their DVR bases.

The [field normal basis theorem](https://kokunoyumeto.github.io/open-math-courses-public/courses/NOE-HYP/NOE-HYP-06.html#normal-bases-in-every-characteristic) says \(L\simeq K[G]\) as left \(K[G]\)-modules [Milne FT, Theorem 5.18]. Scalar extension gives the same assertion for the fraction algebra of \(\widehat M\), including when it is a product.

We call \(\mathfrak p\) **tame** when every \(e_{\mathfrak P}\) is prime to the residue characteristic and every residue extension is separable. In residue characteristic zero, the first condition is automatic. The ramification and residue conditions are constant on the primes above \(\mathfrak p\), since \(G\) acts transitively on them. This definition allows the residue degree, and even \(|G|\), to be divisible by the residue characteristic.

For completeness, prime transitivity holds over our general Dedekind base as follows. If \(\mathfrak Q\) lies outside the orbit of \(\mathfrak P\), the Chinese remainder theorem gives \(x\in\mathfrak Q\) with \(x\equiv1\) at every prime in that orbit. The norm \(N=\prod_{g\in G}g(x)\) belongs to \(B^G=B\cap K=A\), since \(A\) is integrally closed. It lies in \(\mathfrak Q\cap A=\mathfrak p\), while no factor lies in \(\mathfrak P\), a contradiction. Conjugation then identifies the corresponding localized extensions and residue extensions, so their ramification indices and separability conditions agree. This uses no perfect-residue-field hypothesis.

## 2. Trace detects tameness

**Theorem 2.1.** With this notation,

\[
 \operatorname{Tr}_{L/K}(M)=R
 \quad\Longleftrightarrow\quad
 \mathfrak p\text{ is tame}.
\]

**Proof.** Write \(\pi\) for a uniformizer of \(R\). The trace image is an ideal, so it fails to be \(R\) precisely when it lies in \(\pi R\). By the definition of the complementary module,

\[
 \operatorname{Tr}(M)\subseteq\pi R
 \Longleftrightarrow \pi^{-1}\in M^*
 \Longleftrightarrow M\subseteq\pi M^*
 =\pi\mathfrak D^{-1}.
\tag{2.1}
\]

The middle equivalence uses that \(M^*\) is an \(M\)-module. On the \(\mathfrak P\)-component, the final containment means

\[
 d_{\mathfrak P}=v_{\mathfrak P}(\mathfrak D)\ge e_{\mathfrak P}.
\tag{2.2}
\]

The familiar different-exponent theorem gives \(d\ge e-1\), with equality precisely in the tame case. This proves the assertion using that all components have the same ramification behavior.

Here is also a direct verification covering imperfect residue fields. Trace commutes with reduction of the multiplication matrix. In the \(\mathfrak P\)-component of \(M/\pi M\), the filtration by powers of its maximal ideal has \(e_{\mathfrak P}\) successive quotients isomorphic to \(\ell_{\mathfrak P}=B/\mathfrak P\). Multiplication by \(b\) acts on each quotient as multiplication by its residue. Consequently its trace over \(k=R/\pi R\) is

\[
 e_{\mathfrak P}\operatorname{Tr}_{\ell_{\mathfrak P}/k}(\bar b).
\tag{2.3}
\]

The components can be chosen independently by the Chinese remainder theorem. A finite field extension has nonzero trace exactly when it is separable, by the trace criterion in the discriminant lesson. A nonzero linear map to \(k\) is onto. Thus the trace modulo \(\pi\) is onto precisely when at least one component has separable residue extension and \(e_{\mathfrak P}\ne0\) in \(k\). In the Galois situation this says exactly tameness. Nakayama, or the ideal criterion above, lifts surjectivity to \(R\). \(\square\)

These arguments also explain the lower bound without a perfectness assumption. After completing a component, normalize the valuation by \(v(\pi_R)=1\). Every conjugate of an element of valuation at least \(-(e-1)/e\) has the same valuation: the valuation of a complete discretely valued field extends uniquely to its algebraic closure. Its trace therefore has valuation greater than \(-1\), hence nonnegative in the base field. Applying this to its products with integral elements shows \(\mathfrak P^{-(e-1)}\subseteq M^*\), so \(d\ge e-1\). Equations (2.1)–(2.3) now show \(d=e-1\) exactly for a tame component and \(d\ge e\) otherwise.

For a non-Galois extension (2.3) gives a different statement: trace surjectivity requires **some** tame component. It need not make all components tame.

## 3. Higman's criterion: averaging an endomorphism

For a left \(R[G]\)-module \(N\), define

\[
 T_G(\phi)=\sum_{g\in G}g\phi g^{-1},\qquad
 \phi\in\operatorname{End}_R(N).
\]

The sum commutes with \(G\), even when \(|G|\) is not invertible.

**Theorem 3.1 (Higman's criterion).** If \(N\) is finitely generated projective over a commutative ring \(R\), then \(N\) is projective over \(R[G]\) if and only if \(T_G(\phi)=1_N\) for some \(R\)-linear \(\phi\).

**Proof.** Give \(F=R[G]\otimes_R N\) the action on its first factor only. It is projective over \(R[G]\), because an \(R\)-projective module is a summand of a free module and tensoring preserves that splitting. The equivariant map

\[
 \epsilon:F\longrightarrow N,\qquad g\otimes n\longmapsto g(n)
\]

is onto. Given \(\phi\), set

\[
 s(n)=\sum_g g\otimes\phi(g^{-1}n).
\]

Reindexing by \(g=hu\) proves \(s(hn)=h s(n)\), and \(\epsilon s=T_G(\phi)\). If this is the identity, \(N\) is a direct summand of \(F\).

Conversely, projectivity splits \(\epsilon\). Write an equivariant splitting as \(s(n)=\sum_g g\otimes\phi_g(n)\). Equivariance forces \(\phi_g(n)=\phi_1(g^{-1}n)\). Thus \(\epsilon s=1_N\) says \(T_G(\phi_1)=1_N\). \(\square\)

**Corollary 3.2.** In the tame situation, \(M\) is projective over \(R[G]\).

**Proof.** Choose \(t\in M\) with \(\operatorname{Tr}(t)=1\). For multiplication \(\phi(n)=tn\), its conjugate \(g\phi g^{-1}\) is multiplication by \(g(t)\). Their sum is multiplication by \(\sum_g g(t)=1\). Apply Theorem 3.1; \(M\) is free over the DVR \(R\). \(\square\)

This is averaging with an integral element of trace one. Replacing it by division by \(|G|\) would discard tame extensions with a residue degree divisible by the residue characteristic.

## 4. Why a completed projective lattice is free

We need the following precise characteristic-zero input.

**Swan's rigidity theorem, in the form used here.** If \(S\) is a complete DVR of characteristic zero, \(F\) its fraction field, and \(P,Q\) finitely generated projective \(S[G]\)-modules, then

\[
 F\otimes_S P\simeq F\otimes_S Q
 \quad\Longrightarrow\quad P\simeq Q.
\]

This is the specialization of [Swan, Section 6, Corollary 6.4, following Theorem 6.1]. It includes mixed characteristic. Its characteristic hypothesis matters; positive characteristic is handled by Lemma 4.2.

**Lemma 4.1 (descent over fields).** Let \(C\) be a finite-dimensional algebra over a field \(k\). Finite-dimensional \(C\)-modules that become isomorphic after a field extension \(E/k\) are already isomorphic over \(k\).

**Proof.** The space of module homomorphisms is the solution space of finitely many linear equations in matrix entries, so it commutes with extending the field. Choose a \(k\)-basis of \(\operatorname{Hom}_C(U,V)\); the determinant of a linear combination is a polynomial in its coefficients. An isomorphism over \(E\) means this polynomial is not zero. For infinite \(k\), successive specialization of its variables finds a nonzero value in \(k\), giving an isomorphism.

For finite \(k\), choose a finite extension \(k'/k\) large enough that its cardinality exceeds the degree in each variable. A nonzero polynomial cannot vanish on that entire grid, by induction on the variables. This gives an isomorphism over \(k'\). Restriction of scalars then gives \(U^{\oplus d}\simeq V^{\oplus d}\), where \(d=[k':k]\).

The finite-dimensional Krull–Schmidt argument cancels these multiplicities. For completeness, repeated splitting decomposes a finite-dimensional module into indecomposables. Fitting's decomposition \(W=\ker f^n\oplus\operatorname{im}f^n\), for large \(n\), shows that an endomorphism of an indecomposable is either invertible or nilpotent. Its endomorphism ring is local: a nonunit \(f\) is nilpotent, so \(1-f\) is invertible; if a sum of two nonunits were invertible, multiplying by its inverse would contradict that property. When comparing two decompositions, the identity of one summand is a sum of the maps obtained by projecting through the other summands. One such map is a unit in this local endomorphism ring. It makes that summand a direct summand of the corresponding indecomposable on the other side, hence an isomorphic summand. Align and remove the two summands, then induct. Decomposition multiplicities are therefore unique. Equality of \(d\) times every multiplicity implies equality of the original multiplicities. \(\square\)

**Lemma 4.2.** For a complete DVR \(S\) of positive characteristic, a finitely generated projective \(S[G]\)-module whose fraction-field module is \(F[G]\) is \(S[G]\).

**Proof.** The equicharacteristic Cohen structure theorem identifies \(S\) with \(k[[\pi]]\), where \(k=S/\pi S\) is embedded as a coefficient field [Stacks, Tag 0C0S]. Let \(P_0=P/\pi P\), a projective \(k[G]\)-module, and let \(Q=S\otimes_k P_0\). It is projective over \(S[G]\). The identity \(Q/\pi Q\simeq P_0\) lifts to \(Q\to P\), by projectivity of \(Q\) applied to \(P\to P_0\). Both modules are finite free over \(S\), of the same rank. The lifted map is invertible modulo \(\pi\), so its determinant is a unit, giving \(Q\simeq P\).

It follows that \(F\otimes_k P_0\simeq F[G]\). Lemma 4.1 applied to \(k[G]\) gives \(P_0\simeq k[G]\), hence \(P\simeq S[G]\). This works for finite and imperfect residue fields alike. \(\square\)

**Theorem 4.3 (local normal integral basis theorem).** The following are equivalent:

1. \(\mathfrak p\) is tame.
2. \(\widehat M\) is free of rank one over \(\widehat R[G]\).
3. \(M\) is free of rank one over \(R[G]\).

**Proof.** If tame, Corollary 3.2 and scalar extension make \(\widehat M\) projective. Its fraction algebra is the regular representation, by the field normal basis theorem. Swan's theorem, with \(Q=\widehat R[G]\), gives freeness if the fraction field has characteristic zero; Lemma 4.2 gives it otherwise.

To descend, choose a completed generator \(\hat a\). Lift its residue modulo \(\pi\) to \(a\in M\), since \(M/\pi M\simeq\widehat M/\pi\widehat M\). The map \(R[G]\to M\), \(g\mapsto g(a)\), is an isomorphism modulo \(\pi\). Its determinant between free \(R\)-modules of rank \(|G|\) is a unit, so it is an isomorphism. Localization freeness also plainly implies completion freeness.

Finally suppose \(M=R[G]a\). The invariants in the regular representation are \(R\sum_g g\), so \(M^G=R\operatorname{Tr}(a)\). But \(M^G=R\): an invariant lies in \(K\) and is integral over the integrally closed ring \(R\). Thus \(\operatorname{Tr}(a)\) is a unit and the trace is onto. Theorem 2.1 proves tameness. \(\square\)

The elementary construction behind this theorem is visible in two simpler cases. In an unramified local Galois extension, the residue extension is Galois, and [Theorem 4.0](https://kokunoyumeto.github.io/open-math-courses-public/courses/NOE-HYP/NOE-HYP-06.html#normal-bases-in-every-characteristic) supplies a normal basis over its residue field, whether finite or infinite. Lift a generator of that basis; Nakayama and a unit determinant give an integral normal basis. For a totally tamely ramified cyclic extension with \(\pi^e=c\pi_R\) and the \(e\)-th roots of unity in the base, take \(a=1+\pi+\cdots+\pi^{e-1}\). Its conjugates have coefficient matrix \((\zeta^{ij})\) in the power basis. Its Vandermonde determinant is a unit, since \(e\) is invertible and these roots remain distinct in the residue field. This explains the explicit sum construction under these additional hypotheses.

## 5. The group determinant and the global obstruction

For a local generator \(a\), use the ordered basis \((\tau^{-1}(a))_{\tau\in G}\) and all embeddings indexed by \(\sigma\in G\). Its embedding matrix is

\[
 E_{\sigma,\tau}=\sigma\tau^{-1}(a).
\]

**Proposition 5.1.** Its discriminant is \(\det(E)^2\).

**Proof.** The trace Gram matrix is \(E^{\mathsf T}E\), since its \((\tau,\upsilon)\)-entry is the sum of all conjugates of \(\tau^{-1}(a)\upsilon^{-1}(a)\). Take determinants. \(\square\)

This is the group determinant \(\Theta_G(X)=\det(X_{\sigma\tau^{-1}})\), specialized at \(X_g=g(a)\). Over a characteristic-zero splitting field it has the factorization

\[
 \Theta_G(X)=\prod_{\rho\in\operatorname{Irr}(G)}
 \det\left(\sum_gX_g\rho(g)\right)^{\dim\rho}.
\tag{5.1}
\]

Indeed, the matrix is left multiplication by \(\sum_gX_g g\) on the regular representation, which decomposes into \(\dim\rho\) copies of each irreducible \(\rho\). Taking determinants gives (5.1). We use the standard semisimple representation decomposition here; the splitting and characteristic hypotheses should not be applied silently to a modular residue field. For abelian \(G\), all factors are linear.

The arithmetic conductor-discriminant theorem says, for a finite abelian extension of number fields,

\[
 \mathfrak d_{L/K}=\prod_{\chi\in\widehat G}\mathfrak f(\chi),
\]

where \(\mathfrak f(\chi)\) is the finite Artin conductor ideal; the trivial character contributes the unit ideal. This stated input is the conductor-discriminant formula of [Artin]; for abelian extensions it is also stated in [Milne CFT, Chapter V, Theorem 3.27]. Identifying determinant factors with conductor ideals requires arithmetic information beyond the polynomial factorization.

Local generators at every prime need not glue to one global generator. For number fields the resulting obstruction is a locally free module class. Three landmarks delimit the question:

- **Hilbert–Speiser.** A finite abelian extension of \(\mathbb Q\) has a normal integral basis over \(\mathbb Z\) exactly when it is tame. The necessity follows here; the global sufficiency is stated [Bergé, introduction]. Hilbert's *Zahlbericht*, Satz 132, supplied an earlier sufficient case, extended by Speiser to the tame statement.
- **Martinet.** There are tame Galois extensions of \(\mathbb Q\) with quaternion group of order eight whose integer rings are not free over \(\mathbb Z[G]\), although all localizations are free [Martinet, Section IV].
- **Taylor (1981).** For a tame Galois extension \(L/K\) of number fields, the class \([\mathcal O_L]-[\mathcal O_K[G]]\) in \(\operatorname{Cl}(\mathbb Z[G])\) is the root number class \(W_{L/K}\), formed from the Artin root numbers of symplectic characters. This class has order dividing two [Taylor; Cassou-Noguès–Taylor, introduction, equation (1.1)]. The comparison here is after restricting scalars to \(\mathbb Z[G]\); it is not a claim about arbitrary relative \(\mathcal O_K[G]\)-class groups, nor is a stable class computation automatically a free generator.

## 6. Four computations

For \(\mathbb Q(i)\), the trace of \(a+bi\) is \(2a\), so its image on \(\mathbb Z[i]\) is \(2\mathbb Z\). The prime two is wild, with \(e=2\), and there is no localized normal integral basis there. In fact for any proposed generator \(a+bi\), the determinant of it and its conjugate in the basis \(1,i\) is \(-2ab\), never a unit over \(\mathbb Z\) or \(\mathbb Z_{(2)}\).

For \(\mathbb Q(\sqrt{-3})\), let \(\omega=(1+\sqrt{-3})/2\). Its conjugate is \(1-\omega\). These two elements have coefficient determinant \(-1\) in \(1,\omega\), so they give a global normal integral basis, hence one locally at three. Their trace is one. At three, \(e=2\) is prime to three, and the different \((\sqrt{-3})\) has exponent \(e-1=1\).

For an odd prime \(p\), the conjugates of \(\zeta_p\) are \(\zeta_p,\ldots,\zeta_p^{p-1}\). The usual power basis of \(\mathbb Z[\zeta_p]\) is \(1,\zeta_p,\ldots,\zeta_p^{p-2}\), and

\[
 \zeta_p^{p-1}=-1-\zeta_p-\cdots-\zeta_p^{p-2}.
\]

The change of basis has determinant \(\pm1\). The cyclotomic integer theorem identifies this order with the full integer ring [Milne ANT, Chapter 6]. Thus \(\zeta_p\) is a global normal integral basis generator. At \(p\), the index of ramification is \(p-1\), which is tame.

For the cyclic cubic field inside \(\mathbb Q(\zeta_7)\), take

\[
 \eta_1=\zeta_7+\zeta_7^{-1},\quad
 \eta_2=\zeta_7^2+\zeta_7^{-2},\quad
 \eta_3=\zeta_7^3+\zeta_7^{-3}.
\]

Cyclotomic multiplication gives \(\eta_1+\eta_2+\eta_3=-1\), pairwise sum of products \(-2\), and product \(1\). Their polynomial is \(T^3+T^2-2T-1\), of discriminant \(49\). Only seven can divide the index of the order \(\mathbb Z[\eta_1]\). The shift \(T=U+2\) gives \(U^3+7U^2+14U+7\), Eisenstein at seven. Its root is a uniformizer of the totally ramified completion, whose integer ring is generated by that uniformizer by the digit-and-Nakayama argument of the preceding lesson. Thus the local index at seven is one, and the order is maximal everywhere.

Now \(\operatorname{Tr}(\eta_i^2)=5\), because \(\eta_i^2=2+\eta_j\), and \(\operatorname{Tr}(\eta_i\eta_j)=-2\) for \(i\ne j\), because the product is the sum of two periods. Their Gram matrix has diagonal five and off-diagonal minus two; its eigenvalues are \(1,7,7\), so its determinant is \(49\). Their lattice consequently has index one in the full integer ring. The periods are cyclic conjugates, proving that \(\eta_1\) generates a global normal integral basis.

## 7. Exercises

1. **Easy.** For an odd prime \(p\), prove that \(\zeta_p\) generates a normal integral basis of \(\mathbb Z[\zeta_p]\) over \(\mathbb Z\).
2. **Medium.** Determine the trace image of \(\mathbb Z[i]\) and prove it has no global normal integral basis.
3. **Medium.** Prove Higman's criterion without assuming \(|G|\) invertible.
4. **Medium.** Find a normal integral basis generator at three for \(\mathbb Q(\sqrt{-3})\).
5. **Hard.** Derive the trace-tameness criterion from the different exponents, and explain the role of the Galois hypothesis.

## 8. Solutions

**1.** All nontrivial \(p\)-th roots are conjugates of \(\zeta_p\). Their powers from one through \(p-2\) already include all but the constant member of the standard power basis. The relation \(1=-\sum_{a=1}^{p-1}\zeta_p^a\) recovers that constant integrally. The replacement matrix has determinant \(\pm1\), proving both spanning and independence. Hence the associated \(\mathbb Z[G]\)-map is an isomorphism.

**2.** The trace is \(a+bi\mapsto2a\), with image exactly \(2\mathbb Z\). A normal generator would make the invariant submodule generated by its trace, whereas the invariant submodule is \(\mathbb Z\). This would force its trace to be a unit, impossible. Independently, the conjugate coefficient determinant \(-2ab\) is never \(\pm1\).

**3.** Form \(F=R[G]\otimes_R N\) with action on the first factor. It is projective, and \(\epsilon(g\otimes n)=g(n)\) is onto. The map \(s(n)=\sum_g g\otimes\phi(g^{-1}n)\) is equivariant and has composite \(T_G(\phi)\); if that is the identity, it splits. Conversely take an equivariant splitting, extract its coefficient at the identity, and use equivariance to express every other coefficient as \(\phi(g^{-1}n)\). The composite condition yields exactly the required sum. This proves both directions with no division by the group order.

**4.** Take \(\omega=(1+\sqrt{-3})/2\). The integer ring has basis \(1,\omega\); the conjugates \(\omega,1-\omega\) have coefficient columns \((0,1)^{\mathsf T},(1,-1)^{\mathsf T}\). Their determinant is \(-1\), so the same two columns give a basis after localization at three. The trace is one.

**5.** The trace fails to be onto exactly when its image lies in the base maximal ideal. By trace duality this is \(M\subseteq\pi\mathfrak D^{-1}\), which on each component is \(d_{\mathfrak P}\ge e_{\mathfrak P}\). The exponent bound says \(d\ge e-1\), with equality precisely for tame ramification; since these are integers, the strict alternative is \(d\ge e\). Galois transitivity makes all components tame together or wild together, so trace surjectivity is equivalent to tameness at the prime. Without that transitivity the containment must hold at every component for trace failure; surjectivity therefore only requires one tame component. Formula (2.3) independently confirms the same criterion with imperfect residue fields.

## What this lesson does not prove

The field normal basis theorem has the full internal proof in [Hilbert 90 in Noether's form and Galois descent, Theorem 4.0](https://kokunoyumeto.github.io/open-math-courses-public/courses/NOE-HYP/NOE-HYP-06.html#normal-bases-in-every-characteristic). The other inputs are completion and prime decomposition, the Cohen structure theorem [Stacks, Tag 0C0S], Swan's characteristic-zero rigidity [Swan, Section 6, Corollary 6.4], semisimple decomposition of a characteristic-zero splitting representation, the cyclotomic integer theorem, the conductor-discriminant theorem, and the three global outlook results. Trace-tameness, Higman's criterion, tame projectivity, positive-characteristic freeness, descent from completion, necessity and the discriminant square are proved here.

## References

- **[Noether]** Emmy Noether, [*Normalbasis bei Körpern ohne höhere Verzweigung*](https://gdz.sub.uni-goettingen.de/download/pdf/PPN243919689_0167/LOG_0021.pdf), Journal für die reine und angewandte Mathematik **167** (1932), 147–152, Sections 1–3; [English edition](https://github.com/KokunoYumeto/emmy-noether-en). Satz 5 is printed with the sufficient condition that the residue prime does not divide the extension degree. The modern tame theorem above allows divisibility of the residue degree: an unramified quadratic extension of \(\mathbb Q_2\), for example, has an integral normal basis despite \(2\mid2\).
- **[Milne FT]** J. S. Milne, [*Fields and Galois Theory*](https://www.jmilne.org/math/CourseNotes/FT.pdf), Chapter 5, Theorem 5.18.
- **[Milne ANT]** J. S. Milne, [*Algebraic Number Theory*](https://www.jmilne.org/math/CourseNotes/ANT.pdf), Chapter 6, Theorem 6.4 (cyclotomic integer rings).
- **[Stacks]** The Stacks Project, Tags [0C0S](https://stacks.math.columbia.edu/tag/0C0S), [09E3](https://stacks.math.columbia.edu/tag/09E3), and [0EXW](https://stacks.math.columbia.edu/tag/0EXW). These are read in [AI Integrated Stacks Project](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html), an edition with AI-proposed corrections and additions not reviewed by the Stacks Project's maintainers.
- **[Swan]** R. G. Swan, [*Induced representations and projective modules*](https://www.mathnet.ru/eng/mat292), Annals of Mathematics **71** (1960), 552–578, Section 6, Theorem 6.1 and Corollary 6.4; linked journal translation in Matematika **8** (1964), 3–28.
- **[Sutherland]** Andrew V. Sutherland, *Number Theory I*, MIT 18.785 lecture notes, Fall 2021: [Lecture 11](https://math.mit.edu/classes/18.785/2021fa/LectureNotes11.pdf), *Totally ramified extensions and Krasner's lemma*, on tamely ramified extensions, and [Lecture 12](https://math.mit.edu/classes/18.785/2021fa/LectureNotes12.pdf), *The different and the discriminant*.
- **[Milne CFT]** J. S. Milne, [*Class Field Theory*](https://www.jmilne.org/math/CourseNotes/CFT.pdf), version 4.03, Chapter V, Theorem 3.27 (the conductor-discriminant formula).
- **[Artin]** Emil Artin, [*Die gruppentheoretische Struktur der Diskriminanten algebraischer Zahlkörper*](https://gdz.sub.uni-goettingen.de/download/pdf/PPN243919689_0164/LOG_0004.pdf), Journal für die reine und angewandte Mathematik **164** (1931), 1–11.
- **[Cougnard]** Jean Cougnard, [*Les travaux de A. Fröhlich, Ph. Cassou-Noguès et M. J. Taylor sur les bases normales*](https://www.numdam.org/item/SB_1982-1983__25__25_0/), Séminaire Bourbaki, exposé 598, Astérisque **105–106** (1983), 25–38, Section 1.
- **[Bergé]** Anne-Marie Bergé, [*Sur l'arithmétique d'une extension diédrale*](https://www.numdam.org/item/10.5802/aif.411.pdf), Annales de l'Institut Fourier **22** (1972), 31–59, introduction, p. 31.
- **[Martinet]** Jacques Martinet, [*Modules sur l'algèbre du groupe quaternionien*](https://www.numdam.org/articles/10.24033/asens.1216/), Annales scientifiques de l'École Normale Supérieure **4** (1971), 399–408, Section IV.
- **[Taylor]** M. J. Taylor, [*On Fröhlich's conjecture for rings of integers of tame extensions*](https://gdz.sub.uni-goettingen.de/download/pdf/PPN356556735_0063/LOG_0010.pdf), Inventiones Mathematicae **63** (1981), 41–79. The precise class identity is also in Ph. Cassou-Noguès and M. J. Taylor, [*Galois module structure for wild extensions*](https://www.math.u-bordeaux.fr/~pcassoun/graz1.pdf), introduction, equation (1.1).
