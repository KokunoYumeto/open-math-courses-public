# The functor of points and representability

*Written by OpenAI GPT-6.1 Sol in Codex at Ultra; writing-AI self-check completed. No independent review is claimed. Original exposition, proofs and exercises: CC0.*

A scheme can be studied by the maps into it. Testing only with fields records its points and residue fields; testing with dual numbers also records tangent directions. Testing with every scheme records the entire scheme, including its morphisms. The functor of points makes this statement precise, and its gluing criterion lets us build a scheme from a geometric description of its families.

The prerequisite is Schemes, gluing and immersions. In particular we use its mapping gluing theorem and its nontrivial invertible sheaf on the projective line. The affine-target mapping theorem from Affine schemes turns the examples below into ring calculations. We work in fixed nested universes so that schemes in the smaller universe form an admissible category and their set-valued functors live in the larger one. This size convention does not affect any calculation.

## 1. A scheme through all its test maps

For a scheme \(X\), its **functor of points** is the contravariant functor

\[
h_X(T)=\operatorname{Hom}(T,X),\qquad
h_X(a)(f)=f\circ a\quad(a:T'\to T).
\]

An element of \(h_X(T)\) is a **\(T\)-valued point**. It is a morphism, not generally one point of the underlying topological space. Over a base \(S\), replace every Hom by \(\operatorname{Hom}_S\) and take test schemes over \(S\). A functor \(F\) is **represented** by a scheme \(X\) if there is a natural isomorphism \(h_X\cong F\).

**Theorem 1.1 (Yoneda).** For every contravariant set-valued functor \(F\) on schemes,

\[
\operatorname{Nat}(h_X,F)\cong F(X),\qquad
\alpha\longmapsto\alpha_X(1_X).
\tag{1.1}
\]

Consequently \(X\mapsto h_X\) is fully faithful. The same assertion holds over a base scheme.

**Proof.** For \(\xi\in F(X)\), define \(\alpha_T(f)=F(f)(\xi)\) for every \(f:T\to X\). If \(a:T'\to T\), the functor identity gives
\(F(a)\alpha_T(f)=F(fa)(\xi)=\alpha_{T'}(fa)\),
so \(\alpha\) is natural. Conversely naturality of any \(\alpha\), applied to \(f:T\to X\) and \(1_X\), gives exactly this formula with \(\xi=\alpha_X(1_X)\). Thus the constructions are inverse. Taking \(F=h_Y\), the element \(\xi\) is a morphism \(X\to Y\), and the associated transformation is postcomposition with it. This proves full faithfulness. The argument works in the category of schemes over \(S\) without change. \(\square\)

If \((X,\xi)\) represents \(F\), every \(\eta\in F(T)\) is uniquely \(f^*\xi=F(f)(\xi)\) for a map \(f:T\to X\). The element \(\xi\) is the **universal element**, often called the universal family. A representing scheme together with this identification is unique up to a unique isomorphism. Without a specified identification it can have nontrivial automorphisms.

The identity test in Yoneda is unavailable if we only test a nonaffine \(X\) with affines. Nevertheless those tests suffice.

**Theorem 1.2 (affine tests suffice).** For any schemes \(X,Y\), postcomposition gives a bijection

\[
\operatorname{Hom}(X,Y)\cong
\operatorname{Nat}\bigl(h_X|_{\mathrm{Aff}},h_Y|_{\mathrm{Aff}}\bigr).
\tag{1.2}
\]

**Proof.** Let \(\alpha\) be a transformation on affine test schemes, and choose an affine open cover \(X=\bigcup U_i\), with inclusions \(j_i\). Put \(f_i=\alpha_{U_i}(j_i):U_i\to Y\). On an affine open \(W\subset U_i\cap U_j\), naturality for both inclusions says that \(f_i|_W=f_j|_W\). Such \(W\) cover the intersection, even when that intersection is not affine. Morphism gluing makes \(f_i=f_j\) there, and then gives a unique \(f:X\to Y\).

For any affine \(T\) and any \(g:T\to X\), cover \(T\) by affine opens \(V_a\) lying in some \(g^{-1}U_i\). Naturality for \(V_a\to T\) and for the factor \(V_a\to U_i\) gives

\[
\alpha_T(g)|_{V_a}=
\alpha_{V_a}(g|_{V_a})=f_i\circ g|_{V_a}=f\circ g|_{V_a}.
\]

The gluing uniqueness theorem implies \(\alpha_T(g)=fg\). Thus the transformation is postcomposition with \(f\). Uniqueness of \(f\) follows already by testing on the affine chart inclusions. \(\square\)

In particular, a natural isomorphism of the restricted functors determines an isomorphism of schemes: the transformations in both directions come from morphisms, and their composites are identities by full faithfulness. Remember that this requires every affine test ring and every homomorphism between them, not just field-valued points.

## 2. Equations as representing schemes

Fix a ring \(R\), and work on schemes over \(\operatorname{Spec}R\). Put \(A_T=\Gamma(T,\mathcal O_T)\), with its specified \(R\)-algebra structure. The affine-target theorem gives

\[
\operatorname{Hom}_R(T,\operatorname{Spec}B)
\cong\operatorname{Hom}_{R\text{-alg}}(B,A_T).
\tag{2.1}
\]

This holds for nonaffine \(T\) too. The over-\(R\) condition is precisely that the global ring map commute with the given map from \(R\).

**Theorem 2.1 (polynomial solution functors).** For polynomials \(f_1,\ldots,f_r\in R[x_1,\ldots,x_n]\), the closed subscheme

\[
V(f_1,\ldots,f_r)=\operatorname{Spec}R[x_1,\ldots,x_n]/(f_1,\ldots,f_r)
\subset\mathbb A^n_R
\]

represents the functor

\[
T\longmapsto\{(a_1,\ldots,a_n)\in A_T^n:
f_j(a_1,\ldots,a_n)=0\text{ for every }j\}.
\tag{2.2}
\]

**Proof.** A homomorphism from the polynomial ring is determined uniquely by the images \(a_i\) of its variables. It factors through the quotient precisely when all the \(f_j\) map to zero. Formula (2.1) gives the required bijection. Pulling back a section tuple along \(T'\to T\) applies the induced ring homomorphism to its entries, which commutes with polynomial evaluation. Thus the bijections are natural. The inclusion is the closed immersion associated with the quotient map, proved in the preceding lesson. \(\square\)

The argument also permits an arbitrary set of equations, with its generated ideal; no finite-presentation conclusion should be inferred in that case. For no equations it says \(\mathbb A^n_R(T)=A_T^n\). A regular function is a map to affine one-space over the base, even on a nonaffine test scheme.

Here are several useful instances. The universal coordinates provide their universal elements.

| Scheme over \(R\) | Coordinate ring | Its \(T\)-valued points |
|---|---|---|
| \(\mathbb G_{m,R}\) | \(R[t,t^{-1}]\) | \(A_T^*\) |
| \(\mu_{n,R}\), \(n\ge1\) | \(R[t]/(t^n-1)\) | \(\{a\in A_T:a^n=1\}\) |
| \(\mathrm{GL}_{n,R}\), \(n\ge1\) | \(R[x_{ij},d^{-1}]\), \(d=\det(x_{ij})\) | invertible \(n\times n\) matrices over \(A_T\) |
| Two copies of \(\operatorname{Spec}R\) | \(R\times R\) | idempotents in \(A_T\) |

For the first row, localization forces the image of \(t\) to be a unit, and every unit defines a unique map. For \(\mu_n\), a solution of \(a^n=1\) is automatically a unit with inverse \(a^{n-1}\). For matrices, localization at \(d\) asks exactly that the determinant be a unit. The adjugate formula proves sufficiency for invertibility, and taking determinants of a matrix inverse proves necessity. Both directions hold over arbitrary commutative rings, including those with zero divisors. The last row is proved in Solution 2.

These functors have natural group operations in the first three rows: multiplication of units, multiplication of roots of unity, and matrix multiplication. The corresponding morphisms are forced by Yoneda. For example inversion on \(\mathbb G_m\) is induced by \(t\mapsto t^{-1}\); the determinant gives a morphism \(\mathrm{GL}_n\to\mathbb G_m\). Construction of products in the next lesson lets us formulate all group-scheme axioms as diagrams of morphisms.

## 3. The sheaf property and geometric openness

A contravariant functor \(F\) is a **Zariski sheaf on schemes** if for every open cover \(T=\bigcup V_a\), restriction induces a bijection between \(F(T)\) and the compatible families of elements of \(F(V_a)\). Explicitly,

\[
F(T)\longrightarrow\prod_a F(V_a)\rightrightarrows
\prod_{a,b}F(V_a\cap V_b)
\tag{3.1}
\]

is an equalizer. Include the empty cover of the empty scheme; it requires \(F(\varnothing)\) to have one element.

**Theorem 3.1.** Every representable functor is a Zariski sheaf.

**Proof.** For \(F=h_X\), a compatible family in (3.1) is a family of maps \(V_a\to X\) agreeing on overlaps. The preceding lesson's morphism gluing theorem gives precisely one map \(T\to X\). For the empty scheme there is exactly one morphism to \(X\). A natural isomorphism transfers the assertion to any representable \(F\). \(\square\)

A **subfunctor** \(H\subset F\) assigns a subset \(H(T)\subset F(T)\) preserved by every pullback. Call it an **open subfunctor** if for every \(\xi\in F(T)\) there is an open subscheme \(V_\xi\subset T\) such that, for every morphism \(a:T'\to T\),

\[
a^*\xi\in H(T')\quad\Longleftrightarrow\quad
a\text{ factors through }V_\xi.
\tag{3.2}
\]

The factorization is unique because open immersions are monomorphisms. Thus (3.2) says that the set-valued fibre product \(h_T\times_F H\) is represented by that open of \(T\). This notation does not assume scheme fibre products already exist.

The open is unique: each candidate's inclusion factors through the other by (3.2). It is the largest open on which the restricted element belongs to \(H\). The same property also gives pullback compatibility, since the open attached to \(a^*\xi\) is \(a^{-1}V_\xi\). Finally an open subfunctor of a Zariski sheaf is a sheaf: a compatible local family first glues in \(F\); its associated membership open contains all the cover opens, so is all of \(T\), forcing the glued element into \(H(T)\).

**Theorem 3.2 (open subfunctors of a scheme).** Open subfunctors of \(h_X\) correspond bijectively to open subschemes of \(X\).

**Proof.** For an open \(U\subset X\), identify \(h_U\) with its image in \(h_X\), using the monomorphism assertion. For \(\xi=f:T\to X\), the membership open is \(f^{-1}U\). A morphism \(a:T'\to T\) has \(fa\) factoring through \(U\) exactly when \(a\) factors through \(f^{-1}U\): the continuous image condition determines factorization through an open subscheme, and its structure map is the restriction. Hence this is an open subfunctor.

Conversely let \(H\subset h_X\) be open and apply its definition to \(1_X\). Obtain \(U\subset X\). Formula (3.2), now with arbitrary \(f:T\to X\), says \(f\in H(T)\) if and only if \(f\) factors through \(U\). Thus \(H=h_U\) inside \(h_X\). These constructions reverse each other, including empty and full opens. \(\square\)

A family of open subfunctors \((F_i)\) **covers** \(F\) if for every \(\xi\in F(T)\) its membership opens \(V_i(\xi)\) cover \(T\). This allows an element to need several charts. It does not require that one chart contain the whole element on every test scheme.

It suffices to test this cover condition on spectra of fields. For each \(t\in T\), pull \(\xi\) back by \(\operatorname{Spec}\kappa(t)\to T\). If it belongs to an \(F_i\), (3.2) forces this map to factor through \(V_i(\xi)\), and hence \(t\in V_i(\xi)\). The converse follows immediately because a one-point field spectrum must lie in one covering open. Openness itself still requires all test schemes.

## 4. Representing a functor by its open charts

**Theorem 4.1 (representability by gluing).** Suppose \(F\) is a Zariski sheaf and has a set-indexed cover by open subfunctors \(F_i\), each represented by a scheme \(X_i\). Then \(F\) is represented by a scheme \(X\), in which the \(X_i\) occur as open subschemes. The overlap of charts represents \(F_i\cap F_j\).

**Proof.** Let \(\xi_i\in F_i(X_i)\subset F(X_i)\) be the universal element. Openness of \(F_j\) gives an open \(U_{ij}\subset X_i\) characterized by

\[
a:T\to X_i\text{ factors through }U_{ij}
\quad\Longleftrightarrow\quad a^*\xi_i\in F_j(T).
\tag{4.1}
\]

The left-hand element automatically belongs to \(F_i(T)\). Thus \(U_{ij}\) represents \(F_i\cap F_j\). In particular \(\xi_i|_{U_{ij}}\), viewed in \(F_j(U_{ij})\), determines a unique map \(g_{ij}:U_{ij}\to X_j\). Its element also belongs to \(F_i\), so (4.1) on \(X_j\) makes this map factor through \(U_{ji}\). The reversed map is its inverse: their composite preserves the universal element, and uniqueness of the representing map forces it to be the identity.

On \(U_{ij}\), belonging additionally to \(F_k\) cuts out \(U_{ij}\cap U_{ik}\). Under \(g_{ij}\) this condition cuts out \(U_{ji}\cap U_{jk}\). This proves the gluing domain identity. On that open, both \(g_{jk}g_{ij}\) and \(g_{ik}\), as maps to \(X_k\), pull \(\xi_k\) back to the same element. Representability of \(F_k\) proves equality, hence the cocycle. Also \(U_{ii}=X_i\) and \(g_{ii}=1\).

The scheme gluing theorem now constructs \(X\) with open chart maps \(j_i:X_i\to X\). Transport the \(\xi_i\) to these open charts. They agree on the overlaps by construction. Since \(F\) is a sheaf, they glue to \(\xi\in F(X)\). This element defines the natural transformation \(h_X\to F\), \(f\mapsto f^*\xi\). We prove it is a bijection on every test scheme.

Given \(\eta\in F(T)\), its membership opens \(V_i\) cover \(T\). On \(V_i\), representability of \(F_i\) gives a unique map \(f_i:V_i\to X_i\) pulling back \(\xi_i\) to \(\eta|_{V_i}\). On \(V_i\cap V_j\), the element belongs to both subfunctors. Thus \(f_i\) factors through \(U_{ij}\), and \(g_{ij}f_i=f_j\) by uniqueness in \(F_j\). The maps \(j_i f_i\) glue to \(f:T\to X\), and its pullback of \(\xi\) equals \(\eta\) by the sheaf uniqueness axiom.

For injectivity, suppose \(f,g:T\to X\) give the same element. Cover \(T\) by the opens
\(W_{ij}=f^{-1}(j_iX_i)\cap g^{-1}(j_jX_j)\).
On such an open their common element belongs to both \(F_i\) and \(F_j\). The two chart maps therefore factor through \(U_{ij}\) and \(U_{ji}\) by (4.1), and agree after the transition, by representability. Hence \(f=g\) there. Morphism gluing gives \(f=g\) globally. This proves the required natural isomorphism and the asserted overlap description. \(\square\)

This criterion isolates what a geometric construction must establish: local representing objects, a genuinely open membership condition, and the ability to glue its families uniquely. Merely having a collection of familiar-looking charts does not suffice. In particular the sheaf hypothesis is essential.

**Example 4.2 (the Picard functor fails even uniqueness).** The functor
\(T\mapsto\operatorname{Pic}(T)\),
with pullback of invertible sheaves, is not a Zariski sheaf. Take the nontrivial invertible sheaf \(\mathcal L\) on \(\mathbb P^1_k\) constructed in the preceding lesson's Solution 6. Its class and the class of \(\mathcal O\) are distinct globally but restrict to the same class on both affine charts. Restriction is therefore not injective in the equalizer diagram (3.1). By Theorem 3.1 this functor is not represented by a scheme. The issue here is the functor of isomorphism classes with its stated values; later Picard constructions use additional structure and sheafification.

## 5. Exercises

1. **Easy.** Prove that \(\operatorname{Spec}R[t,t^{-1}]\) represents the unit functor on \(R\)-schemes, identify the universal unit, and compute its inverse morphism.
2. **Easy.** Prove that \(\operatorname{Spec}\mathbb Z\amalg\operatorname{Spec}\mathbb Z\) represents idempotent global sections. Relate the idempotent to a decomposition of the test scheme into two open and closed pieces.
3. **Medium.** Use the projective-line transition \(e_\infty=t e_0\) to prove that the Picard functor is not a Zariski sheaf. Specify which sheaf axiom fails.
4. **Medium.** Suppose \(h_X|_{\mathrm{Aff}}\cong h_Y|_{\mathrm{Aff}}\) naturally. Construct the corresponding scheme isomorphism, and explain why nonaffine chart intersections cause no problem.
5. **Medium.** Given the open-chart gluing data of the preceding lesson, construct the functor of compatible local maps to those charts, and apply Theorem 4.1 to recover their gluing as a representing scheme. Check the sheaf and openness conditions.
6. **Medium.** Over a field \(k\) of characteristic \(p>0\), describe \(\mu_p\), its reduction, its field-valued points and its dual-number points over \(k\). What information is absent from its field-valued points?

## 6. Solutions

**Solution 1.** By (2.1), a map from \(T\) to this spectrum is an \(R\)-algebra map to \(A_T\). Such a map is determined by a unit \(a\), the image of \(t\), and then sends \(t^{-1}\) to \(a^{-1}\). Conversely each unit gives this map by the localization universal property. Ring homomorphisms preserve units and inverses, so the bijection is natural. The universal element is \(t\) in the coordinate ring, the image of the identity morphism under this bijection. The ring map \(t\mapsto t^{-1}\) gives inversion, since pullback sends the universal unit to its inverse.

**Solution 2.** The polynomial \(e^2-e=e(e-1)\) has comaximal factors, since \(e-(e-1)=1\). Evaluation at \(0,1\) gives an isomorphism
\(\mathbb Z[e]/(e^2-e)\cong\mathbb Z\times\mathbb Z\)
by the Chinese remainder theorem; explicitly, the inverse sends \((a,b)\) to \(a(1-e)+be\), using \(e^2=e\). A prime of a product contains one of its two complementary idempotents, so its spectrum is the disjoint union of the two spectra; on each piece localization gives the appropriate factor ring and its structure sheaf. Thus Theorem 2.1 proves the representation.

For an idempotent section on any \(T\), its image in each residue field is \(0\) or \(1\). The unit loci of \(e\) and \(1-e\), open by the local-ring unit criterion, are disjoint and cover \(T\). On the first open, idempotence and invertibility force \(e=1\); on the second \(e=0\). Both are open and closed, and the map to the two-copy scheme labels them by \(1\) and \(0\). Conversely any decomposition into two such opens glues the corresponding constant sections. This also treats empty pieces.

**Solution 3.** The sheaf \(\mathcal L\) is trivial on each chart. If it were globally trivial, a global frame would be \(a e_0\) and \(b e_\infty\) with unit polynomial coefficients. Those units are nonzero constants, and agreement would require \(a=b t\), impossible in \(k[t,t^{-1}]\). Thus \([\mathcal L]\ne[\mathcal O]\) in \(\operatorname{Pic}(\mathbb P^1_k)\), but their restrictions agree on both charts. The uniqueness, or separatedness, part of the sheaf axiom fails. This is already enough to rule out a representing scheme.

**Solution 4.** Apply the natural transformation to every inclusion of an affine chart of \(X\) to obtain its map to \(Y\). On an arbitrary chart intersection, choose an affine open cover; naturality identifies the two maps on each member of that cover, and morphism gluing identifies them on the whole intersection. Glue the chart maps to \(f:X\to Y\). The inverse transformation similarly produces \(g:Y\to X\). Theorem 1.2 identifies their composites with the identity transformations, so its injectivity gives \(gf=1_X\) and \(fg=1_Y\). This constructs the isomorphism without treating any nonaffine overlap as affine.

**Solution 5.** Define a presentation on \(T\) to be an open cover \((V_a)\), chart labels \(i_a\), and maps \(f_a:V_a\to X_{i_a}\) such that on each overlap the first map lands in \(U_{i_ai_b}\) and becomes the second under \(g_{i_ai_b}\). Two presentations are equivalent if the same compatibility holds on all intersections between members of their covers. Reflexivity and symmetry follow from the gluing data. For transitivity, cover any intersection of the first and third covers by its intersections with the middle cover; the domain identity and cocycle show compatibility there, and the point-image and morphism-equality conditions are local. Thus this defines an equivalence relation. Let \(F(T)\) be the set of classes, with pullback of covers and maps along a morphism of test schemes.

Restriction classes agreeing over a cover can be represented there and their presentations combined into one presentation: on cross overlaps, agreement of the classes is exactly the required compatibility. This gives existence of gluing. If two global classes restrict equally, the same local condition gives their mutual compatibility, hence equality. Therefore \(F\) is a Zariski sheaf, with a unique empty presentation class on the empty scheme.

A map \(T\to X_i\), viewed as a one-member presentation, defines a subfunctor \(F_i\cong h_{X_i}\): equality of two such presentations is equality of their maps, since \(g_{ii}=1\). For a presentation of \(\eta\in F(T)\), the membership open for \(F_i\) is

\[
V_i=\bigcup_a f_a^{-1}(U_{i_ai})\subset T.
\]

The transported maps to \(X_i\) agree by the cocycle and glue uniquely on \(V_i\). Hence the class restricted there lies in \(F_i\). Conversely, membership after any \(b:T'\to T\) means its pulled-back presentation is compatible with a single map to \(X_i\); compatibility forces \(b\) to land in \(V_i\). If \(b\) lands there, the glued transported map gives that membership. This proves (3.2); the formula is independent of presentation by its characterization. The \(V_i\) cover \(T\), since each original \(V_a\) lies in \(V_{i_a}\). Theorem 4.1 gives a representing scheme with exactly these charts, overlaps and transitions. This recovers the scheme gluing statement in functor language.

**Solution 6.** In characteristic \(p\), the binomial identity gives \(t^p-1=(t-1)^p\). Put \(u=t-1\); the coordinate ring is \(k[u]/(u^p)\), with reduction \(k\). Every map to a field extension of \(k\) must kill \(u\), so it gives only \(t=1\). A dual-number point has \(t=a+\epsilon b\). Its \(p\)-th power is \(a^p\), since \(\epsilon^p=0\) and the intervening binomial coefficients vanish. The equation \(a^p=1\) forces \(a=1\) in the field, while \(b\) is arbitrary. Thus all \(1+\epsilon b\) occur. These first-order directions and the nonzero nilpotent structure cannot be recovered from field-valued points alone.

## Proof dependencies

The scheme-specific affine-test theorem, open-subfunctor theorem and representability criterion are proved here. The full Yoneda calculation is included, with [Stacks, Tag 001P] as the primary reference. Maps into spectra and open-chart gluing use the written proofs in the preceding two lessons. The Picard example uses the preceding lesson's actual solved exercise rather than a future Picard-group calculation. No general descent for modules, quotient construction or projective representability theorem is being assumed.

## References

- **[Stacks]** The Stacks project authors, *The Stacks project*, read in the AI Integrated Stacks Project English edition: *Categories*, [Tag 001P](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/categories.html#lemma-yoneda); *Schemes*, [Tag 01JG](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/schemes.html#definition-representable-functor), [Tag 01JI](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/schemes.html#definition-representable-by-open-immersions), and [Tag 01JJ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/schemes.html#lemma-glue-functors).
- **[Vakil]** Ravi Vakil, *The Rising Sea: Foundations of Algebraic Geometry*, public draft of 27 July 2024, Section 7.6. [Author's book page](https://math.stanford.edu/~vakil/216blog/); [consulted public draft](https://math.stanford.edu/~vakil/216blog/FOAGjul2724public.pdf) (personal viewing and downloading only; no redistribution or derivative works).
