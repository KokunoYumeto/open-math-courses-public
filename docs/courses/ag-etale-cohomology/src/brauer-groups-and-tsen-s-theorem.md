# Brauer groups and Tsen's theorem

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI, GPT-6.1 Sol (OpenAI). Links and citations revised by Claude Opus 5.5 (Anthropic), October 2026. Original text released under CC0.*

A matrix algebra can become visibly a matrix algebra only after extending the field. Its descent data are projective matrices, and the failure to lift those matrices to a genuine linear action is a second cohomology class. We identify that class precisely, then use polynomial equations to show that it vanishes over finite fields and function fields of curves over an algebraically closed field.

Throughout, \(K\) is a field, \(K^s\) a separable closure and \(G_K=\operatorname{Gal}(K^s/K)\). Galois modules and cochains are discrete and continuous, respectively. The Brauer group is written additively. We use the field-topos comparison, continuous cochains, Hilbert 90 and the cohomological-dimension criteria proved in [Galois cohomology and the étale cohomology of a field](galois-cohomology-and-the-etale-cohomology-of-a-field.md).

The algebra prerequisites are proved in four lessons on algebras. We use [Semisimple rings and Wedderburn's theorem](course:NOE-HYP/NOE-HYP-02), Theorem 3.1, and [Central simple algebras and the Brauer group](course:NOE-HYP/NOE-HYP-04), Theorems 1.1, 2.1, 4.3 and 5.1. Finite Galois descent and matrix Hilbert 90 are proved in [Hilbert 90 in Noether's form and Galois descent](course:NOE-HYP/NOE-HYP-06), Theorems 2.1 and 3.1. Their exact roles are stated below. Crossed products are constructed in [Crossed products and factor systems](course:NOE-HYP/NOE-HYP-05); our proof uses projective matrices directly.

## 1. The algebra input and Brauer equivalence

A **central simple \(K\)-algebra** is a nonzero unital associative algebra \(A\), finite dimensional over \(K\), with center \(K\) and no two-sided ideals except \(0,A\). A **division algebra** has an inverse for every nonzero element. A field extension \(E/K\) **splits** \(A\) if \(A_E=A\otimes_K E\) is a matrix algebra over \(E\).

Here are the precise previously proved results we need.

**Algebra input 1.1.** Every central simple algebra has the form

\[
A\simeq M_r(D),\qquad Z(D)=K,
\tag{1.1}
\]

where the central division algebra \(D\) is unique up to \(K\)-isomorphism. Every \(K\)-algebra automorphism of \(A\) is conjugation by a unit. Central simple algebras remain central simple under every field extension, and the tensor product of two of them is central simple. Every such algebra has a finite separable splitting field, hence a finite Galois splitting field.

**Proof locators and applicability.** A finite dimensional algebra is Artinian. The Wedderburn–Artin theorem (*Semisimple rings and Wedderburn's theorem*, Theorem 3.1) therefore applies; simplicity leaves one matrix factor, and its center identifies the center of the division ring with \(K\). The theorem also proves uniqueness by the endomorphism division ring of a simple module. Skolem–Noether is Theorem 2.1 of *Central simple algebras and the Brauer group*, applied to the two embeddings \(\operatorname{id}_A\) and the given automorphism. Its Theorem 1.1 proves the tensor and arbitrary scalar-extension assertions by a minimal tensor-length ideal argument. Its Theorem 4.3 proves existence of a separable maximal subfield of a central division algebra, including imperfect fields, and proves that this subfield splits the algebra. The same field splits its matrix algebras. Passing to its Galois closure gives the last assertion. These are the complete prerequisite proofs used here.

If \(A_E\simeq M_n(E)\), then \(\dim_K A=n^2\); the integer \(n\) is the **degree** of \(A\). If \(\deg D=d\), equation (1.1) gives \(n=rd\). The integer \(d\) is its **index**. Thus two central simple algebras of the same degree and with the same division representative are isomorphic.

We also record the map that produces inverses:

\[
A\otimes_K A^{\mathrm{op}}\longrightarrow\operatorname{End}_K(A),
\qquad a\otimes b\longmapsto(x\longmapsto axb).
\tag{1.2}
\]

It is an algebra homomorphism because multiplication in the second factor is reversed. The map is nonzero because it preserves the identity. Its kernel is a two-sided ideal in a simple algebra, so that kernel is zero. Thus the map is injective. Both sides have dimension \((\dim_K A)^2\), so it is an isomorphism. The target is a split matrix algebra.

Two central simple algebras are **Brauer equivalent** if \(M_u(A)\simeq M_v(B)\) for some positive \(u,v\). By (1.1), this holds exactly when their division representatives are isomorphic. Tensor product respects this equivalence because \(M_u(A)\otimes B\simeq M_u(A\otimes B)\). Associativity and interchange of factors give an associative commutative operation; the class of \(K\) is its identity and (1.2) gives \([A^{\mathrm{op}}]=-[A]\). This is the **Brauer group** \(\operatorname{Br}(K)\). Extension of scalars gives a group homomorphism on Brauer groups. In particular,

\[
\operatorname{Br}(K)=0
\quad\Longleftrightarrow\quad
\text{every finite central division algebra over }K\text{ equals }K.
\tag{1.3}
\]

## 2. Forms of a matrix algebra

For a group \(G\) acting on a possibly noncommutative group \(H\), a continuous **1-cocycle** is a continuous function \(\beta:G\to H\) with

\[
\beta_{gh}=\beta_g\,g(\beta_h).
\tag{2.1}
\]

Two cocycles define the same element of \(H^1(G,H)\) if \(\beta'_g=S\beta_g g(S)^{-1}\) for some \(S\in H\). This is the usual equivalence, with the change-of-basis element written as the inverse of the alternative convention. The result is a pointed set, whose base point is the trivial cocycle.

**Theorem 2.1.** The \(K\)-isomorphism classes of central simple algebras of degree \(n\) are naturally in bijection with

\[
H^1(G_K,\operatorname{PGL}_n(K^s)).
\tag{2.2}
\]

**Proof.** First work over a finite Galois splitting field \(E/K\), with group \(Q\), and choose \(\phi:A_E\simeq M_n(E)\). Transport the canonical action \(1\otimes g\) to a semilinear action \(\rho_g\) on \(M_n(E)\). Composing with inverse entrywise application of \(g\) gives an \(E\)-algebra automorphism. By Skolem–Noether it is \(\operatorname{Ad}(P_g)\) for some \(P_g\in\operatorname{GL}_n(E)\). A matrix acts trivially by conjugation exactly when it is scalar, so the projective class \(\beta_g\) is unique. Consequently

\[
\rho_g(X)=P_g\,g(X)P_g^{-1},
\qquad \rho_g\rho_h=\rho_{gh}
\tag{2.3}
\]

is exactly the projective cocycle relation (2.1). Replacing \(\phi\) by \(\operatorname{Ad}(S)\phi\) changes \(\beta_g\) to \(S\beta_g g(S)^{-1}\). An isomorphism of algebras gives the same change, so we have a well-defined class.

Conversely, a projective cocycle on \(Q\) defines (2.3), which is a genuine semilinear action by algebra automorphisms: scalar discrepancies in \(P_g g(P_h)\) disappear under conjugation. Set

\[
A=M_n(E)^{\rho(Q)}.
\tag{2.4}
\]

The finite Galois descent theorem (*Hilbert 90 in Noether's form and Galois descent*, Theorem 2.1) says that the multiplication-preserving map \(A\otimes_K E\to M_n(E)\) is an isomorphism. It also gives \(\dim_K A=n^2\). If \(I\) were a nonzero proper two-sided ideal of \(A\), its scalar extension would be a nonzero proper ideal of \(M_n(E)\), by injectivity and dimensions of vector-space extension. This is impossible. A central element of \(A\) becomes scalar in \(M_n(E)\), and invariance of a scalar means it lies in \(E^Q=K\). Thus \(A\) is central simple.

For \(\beta'_g=S\beta_g g(S)^{-1}\), conjugation by \(S\) intertwines the two semilinear actions, so restricts to an isomorphism of their fixed algebras. Starting with \(A,\phi\), taking invariants in its transported action recovers \(\phi(A)\). Starting with \(\beta\), the descent isomorphism recovers exactly (2.3), and hence exactly \(\beta\). This proves both inverse identities over \(E\).

Finally consider an arbitrary continuous projective cocycle on \(G_K\). Its image is finite by compactness. Choose one matrix lift for every value. A sufficiently small open normal subgroup \(U\) fixes every entry of those finitely many lifts and lies in the open set where \(\beta_u=1\). Equation (2.1) gives \(\beta_{gu}=\beta_g\) for \(u\in U\). Thus the cocycle descends to \(Q=G_K/U\) with values in \(\operatorname{PGL}_n(E)\), where \(E=(K^s)^U\). Every gauge matrix also has entries in a finite extension, so two finite descriptions and any equivalence between them can be placed over one common finite Galois field. Descent is compatible with that refinement: the original fixed algebra, after extension, has the same transported action and the same inverse descent isomorphism. Since every central simple algebra has a finite Galois splitting field, the finite bijections give (2.2). \(\square\)

## 3. The boundary and the cohomological Brauer group

For a projective cocycle, choose continuous lifts \(P_g\). These exist by choosing a lift for each of its finitely many values. There are unique scalars \(c(g,h)\in(K^s)^\times\) such that

\[
P_g g(P_h)=c(g,h)P_{gh}.
\tag{3.1}
\]

Associativity of the product of the three semilinear operators \(P_g g\), \(P_h h\), \(P_t t\) gives

\[
c(g,h)c(gh,t)=g(c(h,t))c(g,ht).
\tag{3.2}
\]

Thus \(c\) is a continuous multiplicative 2-cocycle. We use the following boundary convention:

\[
\delta_n([\beta])=[c^{-1}],
\qquad
c(g,h)^{-1}=P_g^{-1}P_{gh}\,g(P_h^{-1}).
\tag{3.3}
\]

The last expression is scalar: substitute (3.1) to obtain \(c^{-1}I_n\). This convention agrees with [Stacks, Tag 03R7](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale-cohomology.html#etale-cohomology-theorem-brauer-delta).

For comparison, the central-extension connecting map is often defined as \([c]\). Equation (3.3) is its inverse, so the two maps have the same zero fibre. Choosing (3.3) makes the class of the crossed product with positive factor system \(a\) equal to \([a]\), as in Section 6 of *Crossed products and factor systems*: its matrix descent multiplier is \(a^{-1}\). With the other boundary convention that identification is negated. All abelian cochain differentials retain the convention of lesson 8.

Here are the independence checks. Multiplying lifts by scalars \(b_g\) changes

\[
c(g,h)\quad\text{to}\quad
b_g g(b_h)b_{gh}^{-1}c(g,h)=(db)(g,h)c(g,h).
\tag{3.4}
\]

Hence the inverse multiplier changes by a coboundary. Replacing \(\beta\) by a gauge-equivalent cocycle and using lifts \(S P_g g(S)^{-1}\) leaves \(c\) unchanged. Further scalar changes are already covered by (3.4). All these functions are continuous after one finite refinement. Thus (3.3) is well defined.

**Theorem 3.1.** These boundaries induce a natural isomorphism of abelian groups

\[
\operatorname{Br}(K)\xrightarrow{\sim}
H^2(G_K,(K^s)^\times)
=H^2_{\mathrm{\acute et}}(\operatorname{Spec}K,\mathbb G_m).
\tag{3.5}
\]

For every \(n\), the map \(\delta_n\) is injective on the isomorphism classes of degree-\(n\) forms of a matrix algebra.

**Proof: compatibility and the group map.** For two algebras split over a common \(E\), tensor their splitting isomorphisms. The transported matrices are \(P_g\otimes Q_g\), with multiplier \(c(g,h)d(g,h)\). Thus the boundary of a tensor product is the sum of the two boundaries. For a split matrix factor choose all its matrices to be the identity; tensoring by it leaves the multiplier unchanged. Therefore the boundaries descend through Brauer equivalence to a homomorphism

\[
\delta:\operatorname{Br}(K)\longrightarrow H^2(G_K,(K^s)^\times).
\tag{3.6}
\]

**Proof: zero kernel and injectivity on forms.** If \(\delta([A])=0\), then \(c=db\) for a continuous scalar 1-cochain \(b\). Replace \(P_g\) by \(b_g^{-1}P_g\), so that its multiplier is one. Place all matrices and cochains over a common finite Galois field as in Theorem 2.1 and the finite-quotient cochain comparison of lesson 8, Proposition 3.1. The resulting matrices are a genuine \(\operatorname{GL}_n\)-cocycle. Matrix Hilbert 90 (*Hilbert 90 in Noether's form and Galois descent*, Theorem 3.1) gives

\[
P_g=B g(B)^{-1}.
\tag{3.7}
\]

Conjugating by \(B^{-1}\) makes the semilinear action entrywise Galois action. Its fixed algebra is \(M_n(K)\). Hence \(A\) is split, and (3.6) has zero kernel.

If two degree-\(n\) forms \(A,B\) have the same boundary, the group homomorphism gives \(\delta([A]-[B])=0\), so their Brauer classes agree. They have the same division representative \(D\). Writing \(A=M_r(D)\), \(B=M_s(D)\), their equal degree implies \(r=s\). Thus \(A\simeq B\); by Theorem 2.1 their projective cocycles are equivalent. This proves the asserted injectivity on forms. Exactness of a sequence of pointed sets at its base point alone would establish only the zero-fibre assertion; the group and fixed-degree argument establishes the full assertion.

**Proof: surjectivity.** Let \(\xi\in H^2(G_K,(K^s)^\times)\). Lesson 8, Proposition 3.1, represents it by a 2-cocycle \(a:Q\times Q\to E^\times\), with \(E/K\) finite Galois and \(Q=\operatorname{Gal}(E/K)\). We may normalize \(a(1,g)=a(g,1)=1\). Indeed, (3.2) shows that \(a(1,g)=u\) is constant and \(a(g,1)=g(u)\); multiplying by the coboundary of the constant 1-cochain \(u^{-1}\) gives these normalizations.

Put \(c=a^{-1}\) and let \(V\) be the \(E\)-vector space with basis \((e_h)_{h\in Q}\). Define invertible semilinear maps by

\[
T_g(\lambda e_h)=g(\lambda)c(g,h)e_{gh}.
\tag{3.8}
\]

Their inverses exist because they permute the basis up to nonzero scalars. On \(e_t\), equation (3.2) gives

\[
T_gT_h(e_t)
=g(c(h,t))c(g,ht)e_{ght}
=c(g,h)c(gh,t)e_{ght}
=c(g,h)T_{gh}(e_t).
\tag{3.9}
\]

Conjugation \(X\mapsto T_gXT_g^{-1}\) therefore defines a genuine semilinear \(Q\)-action on \(\operatorname{End}_E(V)\): the scalar in (3.9) cancels. Its fixed algebra \(A\) descends to \(K\) by Theorem 2.1, has degree \(|Q|\), and has multiplier \(c\). Its boundary is \([c^{-1}]=[a]=\xi\). This proves surjectivity without importing a crossed-product calculation.

All constructions commute with extension of fields, with compatible separable closures: the transported matrices and their scalar multipliers extend coefficientwise and restrict along the induced Galois-group map. This proves naturality. The final equality in (3.5) is the field-topos comparison from lesson 8. \(\square\)

In particular, Brauer groups are torsion, since lesson 8 proves that positive-degree continuous cohomology of a profinite group is torsion even for nontorsion discrete coefficients. For \(m\) invertible in \(K\), its Kummer sequence and Hilbert 90 give

\[
H^2(G_K,\mu_m)\simeq\operatorname{Br}(K)[m].
\tag{3.10}
\]

There is no claim here that \(\mu_p\) detects the characteristic-\(p\) part of the Brauer group on the étale site.

## 4. Polynomial conditions on fields

For an integer \(r\geq0\), a field is **\(C_r\)** if every homogeneous polynomial of positive degree \(d\) in \(n>d^r\) variables has a nonzero zero. A zero polynomial satisfies the conclusion automatically. In particular, \(C_1\) means that more variables than the degree force a nontrivial solution.

We will need a simultaneous-equations fact over an algebraically closed field. Its precise algebra prerequisites are the strong Nullstellensatz in *[The Nullstellensatz and Jacobson rings](course:AG-CA/AG-CA-06)*, Theorem 2.2, and Krull's height theorem in *[Dimension theory of Noetherian local rings](course:AG-CA/AG-CA-11)*, Theorem 3.1. These lessons give complete proofs of those foundational results.

**Lemma 4.1 (fewer equations than variables).** If \(k\) is algebraically closed and \(f_1,\ldots,f_R\in k[X_1,\ldots,X_N]\) are homogeneous of positive degree, with \(R<N\), they have a common zero different from the origin. Zero equations may be omitted.

**Proof.** Suppose the origin is their only common zero. By the strong Nullstellensatz, the radical of \(I=(f_1,\ldots,f_R)\) is the maximal ideal \(\mathfrak m=(X_1,\ldots,X_N)\). Thus \(\mathfrak m\) is minimal over \(I\), and Krull's height theorem gives \(\operatorname{ht}\mathfrak m\leq R\). But the strict chain

\[
(0)\subsetneq(X_1)\subsetneq(X_1,X_2)
\subsetneq\cdots\subsetneq(X_1,\ldots,X_N)
\tag{4.1}
\]

consists of prime ideals, since each quotient is a polynomial ring over \(k\). It gives \(\operatorname{ht}\mathfrak m\geq N\), a contradiction. \(\square\)

Applying the lemma to one equation proves that an algebraically closed field is \(C_0\). It also explains precisely why a homogeneous dimension count supplies a nonzero solution, rather than just the origin.

**Theorem 4.2 (Chevalley–Warning).** For polynomials \(f_1,\ldots,f_s\) over \(\mathbb F_q\) with sum of degrees less than \(n\), the number of common zeros in \(\mathbb F_q^n\) is divisible by the characteristic \(p\). In particular, a homogeneous form of degree \(d<n\) has a nonzero zero, so every finite field is \(C_1\).

**Proof.** A zero polynomial can be omitted; a nonzero constant leaves no common zeros. In the remaining case count solutions as an element of \(\mathbb F_q\):

\[
\#Z\cdot1
=\sum_{x\in\mathbb F_q^n}
\prod_{i=1}^s\bigl(1-f_i(x)^{q-1}\bigr).
\tag{4.2}
\]

The product equals one at a common zero and zero elsewhere. Every monomial in its expansion has total degree at most \((q-1)\sum_i\deg f_i<n(q-1)\). Consequently some coordinate exponent \(e\) is less than \(q-1\). If \(e=0\), the sum of \(x^e=1\) over that coordinate is \(q\cdot1=0\). If \(0<e<q-1\), choose a generator \(\omega\) of the cyclic group \(\mathbb F_q^\times\) (proved in lesson 8, Solution 1). Then

\[
\sum_{x\in\mathbb F_q}x^e
=\sum_{j=0}^{q-2}\omega^{je}=0,
\tag{4.3}
\]

because \(\omega^e\ne1\) and this geometric series has numerator \(\omega^{e(q-1)}-1=0\). Summing a multivariable monomial factors into the coordinate sums, so every monomial contributes zero to (4.2), including its constant term. Thus \(\#Z\cdot1=0\), meaning \(p\mid\#Z\). A positive-degree homogeneous form vanishes at the origin. If that were its only zero, its zero count would be one, contradicting divisibility. \(\square\)

**Lemma 4.3 (reduced norm as a polynomial).** If \(A\) has degree \(n\), its reduced norm is a homogeneous polynomial of degree \(n\) in the \(n^2\) coordinates of a \(K\)-basis. An element \(x\in A\) is invertible exactly when \(\operatorname{Nrd}_A(x)\ne0\).

**Proof.** Choose a finite Galois splitting field \(E\), a splitting \(\phi\), and a \(K\)-basis \(a_1,\ldots,a_{n^2}\). Put \(B_i=\phi(a_i\otimes1)\). Define

\[
F(X_1,\ldots,X_{n^2})
=\det\left(\sum_iX_iB_i\right)\in E[X_1,\ldots,X_{n^2}].
\tag{4.4}
\]

It is homogeneous of degree \(n\). Since each \(B_i\) is invariant under (2.3), we have \(g(B_i)=P_g^{-1}B_iP_g\). Acting on the coefficients of (4.4), while fixing the indeterminates, therefore leaves its determinant unchanged. Its coefficients are in \(E^Q=K\). This coefficientwise argument also works over finite fields; pointwise invariance alone would not suffice to identify polynomial coefficients there.

Changing \(\phi\) conjugates every \(B_i\), which preserves the determinant. Two splitting fields can be enlarged to a common one, where the same observation applies. Thus evaluation defines a well-defined reduced norm. An invertible element has invertible image and nonzero determinant. Conversely, if its image is invertible, its inverse is fixed by the transported Galois action, because the inverse is unique. It descends to an inverse in \(A\). Finally \(F\) is not the zero polynomial: evaluation at the coordinate tuple of \(1\) gives one. \(\square\)

**Theorem 4.4.** Every \(C_1\) field has trivial Brauer group. Every finite extension of a \(C_1\) field, including an inseparable extension, is \(C_1\).

**Proof.** Let \(D\) be a finite central division algebra over a \(C_1\) field, of degree \(d\). Its reduced norm is a degree-\(d\) form in \(d^2\) variables. If \(d>1\), then \(d^2>d\), so the \(C_1\) condition produces a nonzero element of \(D\) of reduced norm zero. Lemma 4.3 says it is not invertible, contradicting division. Hence \(d=1\), \(D=K\), and (1.3) gives \(\operatorname{Br}(K)=0\).

For the extension assertion let \(L/K\) have degree \(e\), with basis \(b_1,\ldots,b_e\), and let \(F\) be a degree-\(d\) form over \(L\) in \(n>d\) variables. Substitute

\[
x_j=\sum_{i=1}^e Z_{ji}b_i.
\tag{4.5}
\]

In the free \(K[Z]\)-algebra \(L\otimes_K K[Z]\), multiplication by \(F(x)\) has an \(e\)-by-\(e\) matrix with entries homogeneous of degree \(d\). Its determinant is a form over \(K\) of degree \(ed\) in \(en>ed\) variables, or is identically zero. The \(C_1\) property, or any nonzero tuple in the latter case, supplies a nonzero coordinate tuple where the determinant vanishes. Equation (4.5) gives a nonzero tuple in \(L^n\) because the \(b_i\) are a basis. At that tuple the determinant is the field norm of \(F(x)\), which is zero exactly when \(F(x)=0\): multiplication by a nonzero element of a field is invertible. No separability was used. \(\square\)

## 5. Tsen's theorem by bounded polynomials

**Theorem 5.1 (Tsen).** Let \(k\) be algebraically closed. The function field \(K\) of an integral algebraic curve over \(k\) is \(C_1\).

**Proof.** Such a function field is finitely generated of transcendence degree one. Choose a transcendental element \(t\in K\). The remaining finite list of field generators is algebraic over \(k(t)\), hence generates a finite extension. Write \([K:k(t)]=e\) and choose a basis \(w_1,\ldots,w_e\). Separability of this extension is unnecessary.

Let \(F\in K[x_1,\ldots,x_n]\) be homogeneous of positive degree \(d<n\). For an integer \(m\geq0\) seek a solution of the form

\[
x_j=\sum_{i=1}^e\sum_{r=0}^m z_{jir}t^rw_i,
\qquad z_{jir}\in k.
\tag{5.1}
\]

There are \(ne(m+1)\) scalar unknowns. Expand each term of \(F\) using the basis. Only finitely many products consisting of a coefficient of \(F\) times \(d\) basis elements occur. Each has \(e\) coordinates in \(k(t)\). Choose a nonzero common polynomial denominator \(D(t)\) for all of these finitely many rational coordinates, and an integer \(C\geq0\) bounding the degrees of their polynomial numerators after multiplication by \(D\). Both choices depend on \(F\) and the basis, but not on \(m\).

The polynomial coefficients in (5.1) have degree at most \(m\). A product of \(d\) of them has degree at most \(dm\). It follows that

\[
D(t)F(x_1,\ldots,x_n)
=\sum_{i=1}^e\sum_{s=0}^{dm+C}
H_{is}(z)t^sw_i,
\tag{5.2}
\]

where each \(H_{is}\) is homogeneous of degree \(d\) over \(k\), or zero. This is an identity with indeterminate coordinates, not an asymptotic assertion.

| Quantity | Exact bound |
| --- | --- |
| Scalar unknowns in the proposed solution | \(ne(m+1)\) |
| Scalar coefficient equations in (5.2) | at most \(e(dm+C+1)\) |
| Difference of these bounds | \(e((n-d)m+n-C-1)\) |

Because \(n>d\), choose \(m\) large enough that

\[
ne(m+1)>e(dm+C+1).
\tag{5.3}
\]

Lemma 4.1 gives a nonzero scalar tuple \(z\) annihilating every \(H_{is}\). At least one of the polynomials \(\sum_r z_{jir}t^r\) is nonzero, by transcendence of \(t\). The \(k(t)\)-linear independence of the \(w_i\) then shows that some \(x_j\ne0\). Equation (5.2), the basis independence, and \(D(t)\ne0\) give \(F(x)=0\). This proves the \(C_1\) assertion in full. \(\square\)

Alternatively, one can first run the same count with \(e=1\) to prove that \(k(t)\) is \(C_1\), and then apply the finite-extension part of Theorem 4.4. The displayed proof includes the basis and denominator count directly, so it also shows where every equation comes from for a general curve.

The assertion extends to any field extension \(K/k\) of transcendence degree one. Every finite collection of its elements lies in a finitely generated subfield of transcendence degree one, after adjoining one transcendental element if necessary. The coefficients of any proposed form therefore lie in a function field covered by the theorem, and a nonzero solution there is a solution in \(K\). This passage uses only finitely many coefficients; it requires no assertion about Brauer groups commuting with limits.

## 6. Cohomological consequences and a scheme outlook

**Corollary 6.1.** If \(K\) is \(C_1\), then every finite extension \(E/K\) has \(\operatorname{Br}(E)=0\), and

\[
\operatorname{cd}(K)\leq1,
\qquad
H^q(G_K,(K^s)^\times)=0\quad(q\geq1).
\tag{6.1}
\]

In particular, these conclusions apply to finite fields and to the fields in Tsen's theorem.

**Proof.** The assertion for all finite extensions is Theorem 4.4 applied twice. By Theorem 3.1 it gives \(H^2(G_E,(E^s)^\times)=0\) for every finite separable extension. For every prime \(\ell\ne\operatorname{char}K\), the criterion proved in lesson 8, Proposition 5.5, gives \(\operatorname{cd}_\ell(K)\leq1\). In characteristic \(p>0\), its Theorem 5.4 gives \(\operatorname{cd}_p(K)\leq1\) even without perfection. Taking all primes proves the first part of (6.1): positive cohomology above degree one vanishes for every discrete torsion coefficient module.

The multiplicative coefficient group \(M=(K^s)^\times\) is usually not torsion, so this last assertion alone does not prove the second part. For this argument write abelian groups additively, let \(T\subset M\) be the torsion subgroup, and put \(N=M/T\). The quotient \(N\) is torsion free: if a multiple of the class of \(m\) is zero, a further multiple annihilates \(m\), so \(m\in T\). We have two exact sequences of discrete continuous modules

\[
0\longrightarrow T\longrightarrow M\longrightarrow N\longrightarrow0,
\qquad
0\longrightarrow N\longrightarrow N\otimes_{\mathbb Z}\mathbb Q
\longrightarrow C\longrightarrow0.
\tag{6.2}
\]

Here \(C\) is torsion. Every element of the rationalization still has an open stabilizer, since it is a finite sum of fractions of elements of \(N\). Lesson 8, Corollary 3.2, gives \(H^q(G_K,N\otimes\mathbb Q)=0\) for \(q>0\). The second sequence in (6.2) therefore gives

\[
H^q(G_K,N)\simeq H^{q-1}(G_K,C)=0
\quad(q\geq3).
\tag{6.3}
\]

The first sequence, using \(H^q(G_K,T)=0\) for \(q>1\), gives \(H^q(G_K,M)\simeq H^q(G_K,N)\) for \(q\geq2\). Thus the desired groups vanish for \(q\geq3\). Degree two vanishes by \(\operatorname{Br}(K)=0\) and (3.5); degree one vanishes by Hilbert 90. This proves every degree in (6.1). \(\square\)

The dimension bound need not be zero. For example, over an algebraically closed \(k\) with a prime \(\ell\ne\operatorname{char}k\), the element \(t\) is not an \(\ell\)-th power in \(k(t)\): its order of vanishing at \(t=0\) is one, whereas an \(\ell\)-th power has order divisible by \(\ell\). Kummer gives \(H^1(k(t),\mu_\ell)\ne0\), so \(\operatorname{cd}(k(t))=1\).

For a scheme \(S\), an **Azumaya algebra** is a finite locally free unital \(\mathcal O_S\)-algebra which becomes a matrix algebra on an étale cover. Matrix sizes can vary between components. Brauer equivalence permits tensoring by algebras \(\operatorname{End}_{\mathcal O_S}(V)\), with \(V\) a locally free module of finite positive rank. Tensor product and opposite algebras give the scheme's Azumaya Brauer group. Matrix-algebra transition automorphisms are projective linear, and their scalar lifting obstruction gives a class in \(H^2_{\mathrm{\acute et}}(S,\mathbb G_m)\), with the same inverse-boundary choice as (3.3). This is the scheme version motivating [Stacks, Section 0A2J](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale-cohomology.html#etale-cohomology-section-brauer-scheme). The field proof does not assert that every class of \(H^2(S,\mathbb G_m)\) is represented by an Azumaya algebra on an arbitrary scheme; that problem needs further geometry.

## 7. Quaternion and finite-field examples

Suppose \(\operatorname{char}K\ne2\) and \(a,b\in K^\times\). The quaternion algebra

\[
(a,b)_K=K\langle i,j\rangle/(i^2-a,\ j^2-b,\ ij+ji)
\tag{7.1}
\]

has basis \(1,i,j,ij\), is central simple, and has degree two; these facts are proved in Section 6 of *Central simple algebras and the Brauer group*. Conjugation changes the signs of \(i,j,ij\) and reverses products. Multiplying an element by its conjugate gives its reduced norm:

\[
\operatorname{Nrd}(x_0+x_1i+x_2j+x_3ij)
=x_0^2-a x_1^2-b x_2^2+ab x_3^2.
\tag{7.2}
\]

One checks the formula by using \(ij=-ji\), which cancels cross terms, and \((ij)^2=-ab\). Its identification with reduced norm follows after splitting, where conjugation is the adjugate of a two-by-two matrix, or from the explicit matrices in that prerequisite. Lemma 4.3 shows that this algebra is a division algebra exactly when (7.2) has no nonzero zero. Otherwise (1.1), with total degree two, forces it to be \(M_2(K)\).

For \(a=b=-1\) over \(\mathbb R\), (7.2) is the sum of four squares. It is positive on every nonzero tuple, so Hamilton's algebra \(\mathbb H\) is a division algebra and its Brauer class is nonzero. Lesson 8 computed

\[
H^2(\operatorname{Gal}(\mathbb C/\mathbb R),\mathbb C^\times)
\simeq\mathbb R^\times/\mathbb R_{>0}\simeq\mathbb Z/2\mathbb Z.
\tag{7.3}
\]

Theorem 3.1 identifies \(\operatorname{Br}(\mathbb R)\) with this group, so \([\mathbb H]\) is its unique nonzero element. The normalized multiplier whose value at the pair of conjugations is \(-1\) represents it; its inverse is again \(-1\), consistent with (3.3).

For \(\mathbb F_q\), Theorems 4.2 and 4.4 give \(\operatorname{Br}(\mathbb F_q)=0\). There is also a direct division-algebra proof: a central division algebra over \(\mathbb F_q\) is a finite set, and Wedderburn's little theorem says every finite division ring is a field. Its complete proof is Proposition 5.2 of *Central simple algebras and the Brauer group*; it uses maximal subfields, Skolem–Noether and a finite-group coset fixed-point count. The center condition then makes the division algebra exactly \(\mathbb F_q\). These are two routes to the same conclusion, with the polynomial proof available here and the group-theoretic proof in that lesson.

## 8. Exercises

**Exercise 1 (easy).** Prove directly that the tensor product of two central simple \(K\)-algebras is central simple.

**Exercise 2 (medium).** Prove that a homogeneous form of degree \(d<n\) over \(\mathbb F_q\) has a nonzero zero by showing that its number of zeros is divisible by the characteristic. Include the constant monomials in the counting argument.

**Exercise 3 (medium).** Suppose \(\operatorname{char}K\ne2\). Show that \((a,b)_K\) is split if and only if \(b\) is a norm from the quadratic étale algebra \(L=K[T]/(T^2-a)\). When \(a\) is nonsquare, this is the field \(K(\sqrt a)\). Explain the square case.

**Exercise 4 (medium).** Deduce that every smooth plane conic over \(k(t)\), with \(k\) algebraically closed, has a rational point.

**Exercise 5 (hard).** For algebraically closed \(k\) of characteristic different from two, show that every quadratic form in \(n\geq3\) variables over \(k(t)\) has a nonzero zero, including degenerate forms. Deduce that every quaternion algebra over \(k(t)\) is split.

## 9. Solutions

**Solution 1.** Put \(R=A\otimes_K B\) and let \(I\ne0\) be a two-sided ideal. Choose a nonzero element of \(I\) of smallest tensor length, written \(x=\sum_{i=1}^r a_i\otimes b_i\), with the \(b_i\) linearly independent and \(a_1\ne0\). Since \(Aa_1A=A\), choose finitely many \(u_j,v_j\in A\) with \(\sum_j u_j a_1v_j=1\). The element \(y=\sum_j(u_j\otimes1)x(v_j\otimes1)\) lies in \(I\) and has the form

\[
y=1\otimes b_1+\sum_{i=2}^r a'_i\otimes b_i.
\tag{9.1}
\]

It is nonzero by independence of the \(b_i\), and has length at most \(r\). For any \(u\in A\), its commutator with \(u\otimes1\) has an expression using at most \(r-1\) of these tensors. Minimality forces it to be zero. Independence implies that every \(a'_i\) commutes with all of \(A\), so lies in \(K\). Thus \(y=1\otimes b\) for some nonzero \(b\in B\). Since \(BbB=B\), its two-sided multiples put \(1\otimes1\) in \(I\). Hence \(I=R\).

If \(z=\sum_i a_i\otimes b_i\) is central, use an independent list \(b_i\). Commuting with every \(u\otimes1\) puts all \(a_i\) in \(K\), so \(z=1\otimes b\). Commuting with \(1\otimes B\) puts \(b\) in \(K\). The center of \(R\) is therefore \(K\). It is nonzero and finite dimensional as the tensor product of two nonzero finite vector spaces. This proves all parts of central simplicity.

**Solution 2.** For a nonzero form \(f\), the number \(N\) of zeros satisfies

\[
N\cdot1=\sum_{x\in\mathbb F_q^n}\bigl(1-f(x)^{q-1}\bigr).
\tag{9.2}
\]

The constant term contributes \(q^n\cdot1=0\). Every monomial in \(f^{q-1}\) has total degree \(d(q-1)<n(q-1)\), hence an exponent \(e<q-1\). If \(e=0\), summing that coordinate gives \(q\cdot1=0\); if \(0<e<q-1\), the geometric series over a generator of \(\mathbb F_q^\times\) gives zero as in (4.3). Thus the whole sum is zero, and \(p\mid N\). Homogeneity gives the origin as a zero; it cannot be the only one. For the zero form, every tuple is a zero and a nonzero tuple exists since \(n>d\geq1\). This proves the requested statement, including the case \(q=2\), when the relevant small exponent is necessarily zero.

**Solution 3.** First suppose \(a\) is nonsquare. Then \(L=K(\sqrt a)\) is a quadratic field with nontrivial automorphism \(\sigma\). Write the quaternion algebra as \(L\oplus Lj\), where \(jx=\sigma(x)j\) and \(j^2=b\). If \(b=c\sigma(c)\) for \(c\in L^\times\), let \(L\) act on its underlying two-dimensional \(K\)-space by multiplication and let \(j\) act by \(J(v)=c\sigma(v)\). Then \(J^2=b\) and \(Jm_x=m_{\sigma(x)}J\). These satisfy the defining relations, giving a unital algebra homomorphism to \(\operatorname{End}_K(L)\). Central simplicity makes it injective, and both dimensions are four. Thus it is an isomorphism.

Conversely, if the quaternion algebra is \(\operatorname{End}_K(V)\) with \(\dim_K V=2\), its embedded field \(L\) makes \(V\) one dimensional over \(L\). Choose an \(L\)-basis to identify \(V\) with \(L\). The relation with \(j\) says its operator is \(\sigma\)-semilinear, so it is \(v\mapsto c\sigma(v)\), where \(c=J(1)\ne0\) because \(j\) is invertible. Squaring gives \(b=c\sigma(c)\). This proves both directions.

If \(a=s^2\in K^{\times2}\), the étale algebra is \(K\times K\), and its norm \((u,v)\mapsto uv\) is surjective on units. The quaternion algebra is always split, as the matrices

\[
i\longmapsto\begin{pmatrix}s&0\\0&-s\end{pmatrix},
\qquad
j\longmapsto\begin{pmatrix}0&b\\1&0\end{pmatrix}
\tag{9.3}
\]

satisfy the relations. Their images of \(1,i,j,ij\) are independent: the first two span diagonal matrices and the last two span off-diagonal matrices, since \(2,s,b\) are nonzero. This gives an isomorphism to \(M_2(K)\). If the wording uses the field \(K(\sqrt a)=K\) in this case, its degree-one norm is the identity and is also surjective; the quadratic étale wording retains the intended degree-two norm uniformly.

**Solution 4.** Write the conic in \(\mathbb P^2_{k(t)}\) as \(F(X,Y,Z)=0\), with \(F\) homogeneous of degree two. Tsen gives a nonzero triple \((x,y,z)\in k(t)^3\) with \(F(x,y,z)=0\), since \(3>2\). Its projective class \([x:y:z]\) is the desired rational point. The same existence argument works for a singular plane quadratic equation; smoothness is part of the stated conic hypothesis and does not need an additional step here.

**Solution 5.** A quadratic form is a homogeneous degree-two polynomial, regardless of degeneracy. Since \(n\geq3>2\), Tsen gives a nonzero zero. The zero form has every nonzero vector as a zero. Apply this to the reduced norm (7.2) of a quaternion algebra, which has four variables. Its nonzero zero is a nonzero noninvertible algebra element by Lemma 4.3. The algebra is therefore not division. A degree-two central simple algebra is \(M_r(D)\) with \(r\deg D=2\); the only remaining possibility is \(r=2\), \(D=K\), so it is split. This also supplies the quaternion conclusion without needing to diagonalize an arbitrary quadratic form.

## 10. Proof scope and conventions

The Wedderburn, Skolem–Noether, separable-splitting, tensor and finite-descent theorems are used from the algebra lessons cited in Sections 1 and 2, and the Nullstellensatz and the height theorem from the commutative-algebra lessons cited in Section 4; those lessons prove them completely. We have proved here both inverse maps for matrix forms, the well-defined boundary with its explicit sign, the Brauer group map and its zero kernel, injectivity on fixed-degree forms, surjectivity by semilinear projective matrices, the finite-field counting theorem, the generic reduced-norm polynomial, preservation of \(C_1\) under all finite field extensions, full Tsen with a fixed denominator bound, and all positive-degree unit-cohomology and dimension consequences. Every exercise has a complete solution.

No perfection assumption enters Tsen or the characteristic-\(p\) dimension bound. Cohomological dimension concerns torsion modules; the additional rationalization argument is what proves higher vanishing for \((K^s)^\times\). The Azumaya paragraph is an outlook, without a general representability theorem for scheme cohomology.

## 11. References

- The Stacks Project Authors, *The Stacks Project*, Brauer Groups: [Tag 073W, chapter](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/brauer.html#brauer-section-phantom); [Tag 0747, Wedderburn](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/brauer.html#brauer-theorem-wedderburn); [Section 074J, Brauer group](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/brauer.html#brauer-section-brauer); [Tag 074Q, Skolem–Noether](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/brauer.html#brauer-theorem-skolem-noether); [Tag 0752, separable splitting](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/brauer.html#brauer-proposition-separable-splitting-field). The AI Integrated Stacks Project English reader is used for these public links.
- The same work, Étale Cohomology: [Section 03R1](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale-cohomology.html#etale-cohomology-section-brauer-groups), including the definitions and identifications 03R2, 03R3 and 03R5, [Tag 03R6, forms](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale-cohomology.html#etale-cohomology-lemma-central-simple-algebra-pgln), and [Tag 03R7, cohomological Brauer group](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale-cohomology.html#etale-cohomology-theorem-brauer-delta); [Section 0A2J, schemes](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale-cohomology.html#etale-cohomology-section-brauer-scheme).
- The same work, Galois-cohomology dimension and polynomial fields: [Section 03R8](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale-cohomology.html#etale-cohomology-section-galois-cohomology), including 03R9, 03RA, 03RB, 03RC, 03RD, 03RF and 03RG. These supply the dimension criterion, \(C_r\) definitions, simultaneous-equation lemma, reduced-norm argument, Tsen and its cohomological consequences; the curve proof and all-degree unit vanishing have been supplied fully above.
- Lessons of this collection used as prerequisites: [Semisimple rings and Wedderburn's theorem](course:NOE-HYP/NOE-HYP-02), [Central simple algebras and the Brauer group](course:NOE-HYP/NOE-HYP-04), [Crossed products and factor systems](course:NOE-HYP/NOE-HYP-05), [Hilbert 90 in Noether's form and Galois descent](course:NOE-HYP/NOE-HYP-06), [The Nullstellensatz and Jacobson rings](course:AG-CA/AG-CA-06) and [Dimension theory of Noetherian local rings](course:AG-CA/AG-CA-11), at the theorem numbers given in the text.
