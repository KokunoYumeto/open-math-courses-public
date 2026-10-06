# Blow-up sequences and the main theorems

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

A resolution is built one blow-up at a time, and each step depends on the previous ones. To make the construction independent of choices, the course works with whole sequences of blow-ups, together with the ideal and the divisor carried along, and with rules that assign such a sequence to every triple of data in a way compatible with smooth morphisms. This lesson sets up that language, states the theorems the course proves, and proves the one general tool that turns locally defined rules into global ones.

We use [Smooth blow-ups and transforms of ideals](smooth-blowups-and-transforms-of-ideals.md) throughout: its coordinates, orders, cosupports, smooth centres, snc divisors and transforms. Conventions are as there: \(k\) has characteristic zero and smooth schemes are smooth of finite type over \(k\).

## 1. Blow-up sequences

**Definition 1.1.** A *blow-up sequence* of length \(r\) starting with a scheme \(X\) is a chain

\[
X_r\xrightarrow{\ \pi_{r-1}\ }X_{r-1}\longrightarrow\cdots\longrightarrow X_1\xrightarrow{\ \pi_0\ }X_0=X
\]

together with closed subschemes \(Z_i\subset X_i\), the *centres*, such that \(\pi_i:X_{i+1}=B_{Z_i}X_i\to X_i\) is the blow-up, with exceptional divisor \(F_{i+1}\subset X_{i+1}\). Write \(\Pi_{ij}=\pi_j\circ\cdots\circ\pi_{i-1}:X_i\to X_j\) and \(\Pi_i=\Pi_{i0}\). The sequence is *smooth* if every \(Z_i\) is a smooth centre; then every \(X_i\) is smooth by [Smooth blow-ups and transforms of ideals, Proposition 3.1](smooth-blowups-and-transforms-of-ideals.md#3-blowing-up-a-smooth-centre). Trivial and empty blow-ups are allowed.

**Definition 1.2 (three operations).**

1. *Pull-back.* For a flat morphism \(h:Y\to X\), the pull-back \(h^*\mathbf B\) is the sequence \(X_i\times_XY\) with centres \(Z_i\times_XY\). It is a blow-up sequence because blowing up commutes with flat base change ([Stacks, Tag 0805](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/divisors.html#divisors-lemma-flat-base-change-blowing-up)), applied inductively to the flat maps \(X_i\times_XY\to X_i\). If \(h\) is smooth and \(\mathbf B\) is smooth, \(h^*\mathbf B\) is smooth. If \(h\) is not surjective, some pulled-back centres may be empty.
2. *Restriction.* For a closed subscheme \(S\subset X\), let \(S_i\subset X_i\) be the strict transforms. Then \(S_{i+1}=B_{Z_i\cap S_i}S_i\) ([Stacks, Tag 080E](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/divisors.html#divisors-lemma-strict-transform)), so the \(S_i\) with centres \(Z_i\cap S_i\) form a blow-up sequence \(\mathbf B|_S\). It need not be smooth.
3. *Push-forward.* Conversely, let \(S\subset X\) be closed and let \(\mathbf B^S\) be a blow-up sequence of \(S\) with centres \(Z^S_i\subset S_i\). Define a sequence of \(X\) inductively: \(Z_i\) is \(Z^S_i\) regarded as a closed subscheme of \(X_i\) through the strict transform \(S_i\subset X_i\). By induction the strict transform of \(S\) in \(X_{i+1}=B_{Z_i}X_i\) is \(B_{Z_i\cap S_i}S_i=B_{Z^S_i}S_i\), the next scheme of \(\mathbf B^S\). This *push-forward* is written \(j_*\mathbf B^S\) for \(j:S\to X\). It is smooth if \(\mathbf B^S\) is smooth.

## 2. Triples and the blow-ups they allow

**Definition 2.1.** A *triple* \((X,\mathcal I,E)\) consists of an equidimensional smooth scheme \(X\), possibly disconnected; a coherent ideal sheaf \(\mathcal I\) that is nonzero on every irreducible component of \(X\); and an ordered snc divisor \(E=(E^1,\ldots,E^s)\) ([Smooth blow-ups and transforms of ideals, Definition 3.2](smooth-blowups-and-transforms-of-ideals.md#3-blowing-up-a-smooth-centre)), whose members may be reducible or empty. A *marked triple* \((X,\mathcal I,m,E)\) also carries an integer \(m\ge1\).

**Definition 2.2.** Let \((X,\mathcal I,E)\) be a triple with \(\operatorname{maxord}\mathcal I\le m\), \(m\ge1\). A *blow-up of order* \(m\) is the blow-up \(\pi\) of a smooth centre \(Z\) that has snc with \(E\) and satisfies \(\operatorname{ord}_Z\mathcal I=m\). Its *transform* is

\[
\pi^{-1}_*(X,\mathcal I,E)=\bigl(B_ZX,\ \pi^{-1}_*\mathcal I,\ \pi^{-1}_{\rm tot}E\bigr),
\]

with the birational transform of [Smooth blow-ups and transforms of ideals, Definition 4.2](smooth-blowups-and-transforms-of-ideals.md#4-transforms-of-ideals-and-of-marked-ideals) and the total transform of Lemma 3.3 there, in which \(F\) is appended as the last member. For a marked triple \((X,\mathcal I,m,E)\), a *blow-up of order* \(\ge m\) is the blow-up of a smooth centre with snc with \(E\) and \(\operatorname{ord}_Z\mathcal I\ge m\), with transform \((B_ZX,\pi^{-1}_*(\mathcal I,m),\pi^{-1}_{\rm tot}E)\).

A *blow-up sequence of order* \(m\) starting with \((X,\mathcal I,E)\), and a *blow-up sequence of order* \(\ge m\) starting with \((X,\mathcal I,m,E)\), are smooth blow-up sequences in which each \(\pi_i\) is a blow-up of the required kind for the triple \((X_i,\mathcal I_i,E_i)\), respectively \((X_i,\mathcal I_i,m,E_i)\), obtained recursively as the transform of the previous one. We write \(\Pi^{-1}_*(X,\mathcal I,E)=(X_r,\mathcal I_r,E_r)\), always remembering that the transform depends on the sequence and not only on \(\Pi\) ([Smooth blow-ups and transforms of ideals, Example 4.5](smooth-blowups-and-transforms-of-ideals.md#4-transforms-of-ideals-and-of-marked-ideals)).

**Lemma 2.3.**

1. The transform of a triple, or of a marked triple, under a blow-up of order \(m\), respectively \(\ge m\), is again a triple, respectively a marked triple.
2. If \(m=\operatorname{maxord}\mathcal I\), the blow-up sequences of order \(\ge m\) starting with \((X,\mathcal I,m,E)\) are exactly the blow-up sequences of order \(m\) starting with \((X,\mathcal I,E)\), with the same transforms.

**Proof.** (1) The ideal \(\mathcal I\) has order \(0\) at the generic point of each component, so for \(m\ge1\) no centre contains a component. Hence \(B_ZX\) has the same dimension, its components are the blow-ups of those of \(X\), and the transformed ideal is nonzero on each, since \(\pi\) is an isomorphism over the dense open \(X\setminus Z\). The total transform of \(E\) is snc by [Smooth blow-ups and transforms of ideals, Lemma 3.3](smooth-blowups-and-transforms-of-ideals.md#3-blowing-up-a-smooth-centre). (2) By Lemma 4.3 there, the maximal order stays \(\le m\) along such a sequence. Hence \(\operatorname{ord}_Z\mathcal I_i\ge m\) means \(=m\), and then the marked and unmarked transforms coincide by definition. \(\square\)

**Lemma 2.4 (transforms commute with smooth pull-back).** Let \(h:Y\to X\) be a smooth morphism of smooth schemes and \(Z\subset X\) a smooth centre with \(\operatorname{ord}_Z\mathcal I\ge m\). Let \(Z_Y=h^{-1}(Z)\) and \(h_1:B_{Z_Y}Y=B_ZX\times_XY\to B_ZX\). Then \(Z_Y\) is a smooth centre, \(\operatorname{ord}_{Z_Y}h^*\mathcal I\ge m\), with equality at the generic points of \(Z_Y\) lying over generic points of \(Z\) where \(\mathcal I\) has order \(m\), and

\[
(\pi_Y)^{-1}_*(h^*\mathcal I,m)=h_1^*\,\pi^{-1}_*(\mathcal I,m),\qquad (\pi_Y)^{-1}_*h^*\mathcal I=h_1^*\,\pi^{-1}_*\mathcal I.
\]

If \(Z\) has snc with \(E\), then \(Z_Y\) has snc with \(h^{-1}E\), and \(\pi_Y^{-1}{}_{\rm tot}(h^{-1}E)=h_1^{-1}\pi^{-1}_{\rm tot}E\).

**Proof.** Here \(h^*\mathcal I\) means \(h^{-1}\mathcal I\cdot\mathcal O_Y\). The smooth morphism \(h\) is open, so the generic points of the components of \(Z_Y\) map to generic points of components of \(Z\), and the orders correspond by [Smooth blow-ups and transforms of ideals, Proposition 2.6(4)](smooth-blowups-and-transforms-of-ideals.md#2-order-of-vanishing-and-derivative-ideals). The exceptional divisor of \(B_{Z_Y}Y\) is \(h_1^{-1}F\), so \(h_1^*\mathcal O(mF)=\mathcal O(mF_Y)\), and pulled-back ideals multiply. For snc, a coordinate system on \(X\) adapted to \(E\) and \(Z\), completed by fibre coordinates as in the proof of that Proposition 2.6(4), is adapted to \(h^{-1}E\) and \(Z_Y\). For the strict transforms, the strict transform of \(E^i\) is \(B_{Z\cap E^i}E^i\) ([Stacks, Tag 080E](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/divisors.html#divisors-lemma-strict-transform)), and blowing up commutes with the flat base change \(h^{-1}(E^i)\to E^i\) ([Stacks, Tag 0805](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/divisors.html#divisors-lemma-flat-base-change-blowing-up)). \(\square\)

## 3. Blow-up sequence functors and functoriality

**Definition 3.1.** A *blow-up sequence functor* \(\mathcal B\) on a class of triples (or marked triples) assigns to each \((X,\mathcal I,E)\) in the class a blow-up sequence of a specified kind starting with it, with specified centres. The \(\mathcal I_i\) and \(E_i\) are determined by the centres, and we regard them as part of the output.

*Empty blow-up convention.* The final outputs of the named functors of this course contain no empty blow-ups. Intermediate constructions may tell us to blow up a subscheme that happens to be empty, for example an empty intersection of two members of \(E\); such steps are deleted without comment.

**Definition 3.2 (functoriality).** Let \(\mathcal B\) be a blow-up sequence functor.

1. *Smooth morphisms.* \(\mathcal B\) *commutes with smooth morphisms* if, for every smooth morphism \(h:Y\to X\) of smooth schemes with \((X,\mathcal I,E)\) in the class, the triple \((Y,h^*\mathcal I,h^{-1}E)\) is in the class and \(\mathcal B(Y,h^*\mathcal I,h^{-1}E)\) is obtained from \(h^*\mathcal B(X,\mathcal I,E)\) by deleting the blow-ups with empty centre. Here \(h^{-1}E=(h^{-1}E^1,\ldots,h^{-1}E^s)\) keeps the ordering, and its members may become empty. By Lemma 2.4 the pulled-back sequence is a sequence of the same kind. For a surjective \(h\) no blow-up is deleted.
2. *Change of field.* For a field extension \(k\subset k'\), \(\mathcal B(X_{k'},\mathcal I_{k'},E_{k'})=\mathcal B(X,\mathcal I,E)_{k'}\), the base change of all schemes and centres.
3. *Closed embeddings.* Let \(j:Y\to X\) be a closed embedding of smooth schemes, \(\mathcal I_Y\) and \(\mathcal I_X\) ideal sheaves with \(\mathcal O_X/\mathcal I_X=j_*(\mathcal O_Y/\mathcal I_Y)\), and \(E\) an snc divisor on \(X\) with \(E|_Y\) snc on \(Y\). Then \(\mathcal B\) *commutes with closed embeddings* if \(\mathcal B(X,\mathcal I_X,E)=j_*\mathcal B(Y,\mathcal I_Y,E|_Y)\), and *commutes weakly* if \(j^*\mathcal B(X,\mathcal I_X,E)=\mathcal B(Y,\mathcal I_Y,E|_Y)\).

The identifications in (1) and (2) are unique when they exist, because a blow-up sequence of \(Y\) is determined by its centres. Existence is therefore local on \(Y\). In (1), \(Y\) is required to be equidimensional, like every scheme of a triple; a smooth morphism of non-constant relative dimension is treated on each open and closed piece of constant relative dimension, as in Remark 3.3.

**Remark 3.3 (disjoint unions).** A smooth scheme is the disjoint union of its open and closed equidimensional pieces \(X_{(d)}\). A functor defined on equidimensional triples extends to all smooth \(X\) by running the pieces simultaneously: the \(i\)-th centre is the union of the \(i\)-th centres on the pieces, a piece whose sequence has already ended contributing the empty set. This extension commutes with open immersions and preserves the functoriality properties of Definition 3.2. Every construction of the course is a rule of this kind: the next centre is determined by data at its points, so on a disjoint union it is the union of the centres on the parts.

## 4. The theorems of the course

Theorems 4.1 and 4.2 are the inductive core. They are proved together by induction on \(\dim X\) in [Order reduction for ideals](order-reduction-for-ideals.md) and [Order reduction for marked ideals](order-reduction-for-marked-ideals.md).

**Theorem 4.1 (order reduction for ideals).** For every \(m\ge1\) there is a blow-up sequence functor \(\mathcal B^{\rm ord}_m\) of order \(m\), defined on triples \((X,\mathcal I,E)\) with \(\operatorname{maxord}\mathcal I\le m\), such that \(\operatorname{maxord}\mathcal I_r<m\) at its end, and which commutes with smooth morphisms and with change of field.

**Theorem 4.2 (order reduction for marked ideals).** For every \(m\ge1\) there is a blow-up sequence functor \(\mathcal B^{\rm mord}_m\) of order \(\ge m\), defined on all marked triples \((X,\mathcal I,m,E)\), such that \(\operatorname{maxord}\mathcal I_r<m\) at its end, and which commutes with smooth morphisms and with change of field. Moreover:

1. if \(m=\operatorname{maxord}\mathcal I\), then \(\mathcal B^{\rm mord}_m(X,\mathcal I,m,\emptyset)=\mathcal B^{\rm ord}_m(X,\mathcal I,\emptyset)\);
2. for a closed embedding \(j:Y\to X\) of smooth schemes and ideals with \(\mathcal O_X/\mathcal I=j_*(\mathcal O_Y/\mathcal J)\), \(\mathcal J\) nonzero on every component of \(Y\), \(\mathcal B^{\rm mord}_1(X,\mathcal I,1,\emptyset)=j_*\mathcal B^{\rm mord}_1(Y,\mathcal J,1,\emptyset)\).

The induction runs: Theorem 4.2 in dimensions \(<n\) implies Theorem 4.1 in dimension \(n\), which implies Theorem 4.2 in dimension \(n\). In dimension \(0\) every triple has \(\mathcal I=\mathcal O_X\) and both functors are empty sequences.

The final lesson, [Principalization and resolution](principalization-and-resolution.md), deduces the following.

**Theorem 4.3 (principalization).** There is a blow-up sequence functor \(\mathcal B^{\rm pri}\) on triples \((X,\mathcal I,E)\) in which the snc divisor \(E\) is not ordered, such that all centres are smooth and have snc with \(E\) and its total transforms; \(\Pi^*\mathcal I\) is the ideal sheaf \(\mathcal O(-D)\) of an effective divisor \(D\) whose support is an snc divisor; \(\Pi\) is an isomorphism over \(X\setminus\bigl(\operatorname{cosupp}(\mathcal I,1)\cup\operatorname{Sing}E\bigr)\), where \(\operatorname{Sing}E\) is the set of points on at least two components of \(E\) (empty if \(E=\emptyset\)); \(\mathcal B^{\rm pri}\) commutes with smooth morphisms and change of field; and it commutes with closed embeddings when \(E=\emptyset\).

**Theorem 4.4 (resolution of singularities).** There is a resolution functor \(X\mapsto(\rho_X:R(X)\to X)\) on all reduced schemes of finite type over \(k\) such that \(R(X)\) is smooth, \(\rho_X\) is proper and an isomorphism over the smooth locus of \(X\), \(\rho_X^{-1}(\operatorname{Sing}X)\) is an snc divisor, and \(R(X)\) is compatible with smooth morphisms and change of field: \(R(Y)=R(X)\times_XY\) canonically for smooth \(Y\to X\). For an integral quasi-projective \(X\), \(\rho_X\) is projective and is obtained by restricting a sequence of smooth blow-ups of an ambient smooth variety to strict transforms of \(X\).

## 5. From local to global

The inductive constructions produce sequences only on pieces of \(X\) where an auxiliary choice exists. The next theorem glues them.

A morphism \(g:X'\to X\) is a *local isomorphism* if \(X'\) is covered by open subsets that \(g\) maps isomorphically onto open subsets of \(X\). Local isomorphisms are étale, and they are stable under composition, base change, fibre products over \(X\) and disjoint unions.

**Theorem 5.1 (gluing).** Let \(\mathcal{GT}\supset\mathcal{LT}\) be two classes of triples (or marked triples) with the same marking. Assume:

1. \(\mathcal{LT}\) is closed under disjoint unions and under restriction to open subsets;
2. every \((X,\mathcal I,E)\in\mathcal{GT}\) is covered by open subsets on which the restricted triple lies in \(\mathcal{LT}\);
3. \(\mathcal B\) is a blow-up sequence functor on \(\mathcal{LT}\) that commutes with surjective local isomorphisms.

Then \(\mathcal B\) has a unique extension \(\overline{\mathcal B}\) to \(\mathcal{GT}\) that commutes with surjective local isomorphisms. If moreover \(\mathcal{GT}\) and \(\mathcal{LT}\) are closed under pull-back by smooth morphisms and \(\mathcal B\) commutes with smooth morphisms between triples of \(\mathcal{LT}\), then \(\overline{\mathcal B}\) commutes with smooth morphisms; the same holds for change of field.

**Proof.** Let \((X,\mathcal I,E)\in\mathcal{GT}\). Choose a finite open cover \(X=\bigcup U_\alpha\) with each restriction in \(\mathcal{LT}\), and let \(X'=\coprod U_\alpha\), with the surjective local isomorphism \(g:X'\to X\). Then \(X''=X'\times_XX'=\coprod_{\alpha,\beta}U_\alpha\cap U_\beta\) is in \(\mathcal{LT}\) by (1), and the two projections \(\tau_1,\tau_2:X''\to X'\) are surjective local isomorphisms. By (3),

\[
\tau_1^*\mathcal B(X')=\mathcal B(X'')=\tau_2^*\mathcal B(X'),
\]

writing \(\mathcal B(X')\) for the value on the pulled-back triple. We construct a sequence \(\mathbf B\) of \(X\) with \(g^*\mathbf B=\mathcal B(X')\) by induction on the step. Suppose \(X_i\) is constructed with \(X'_i=X'\times_XX_i\), the \(i\)-th scheme of \(\mathcal B(X')\). The centre \(Z'_i\subset X'_i\) is the disjoint union of its pieces over the \(U_\alpha\), and the displayed equality says that the pieces over \(U_\alpha\) and \(U_\beta\) agree over \(U_\alpha\cap U_\beta\). Closed subschemes glue along open covers, so there is a unique closed \(Z_i\subset X_i\) with \(g^{-1}(Z_i)=Z'_i\). Put \(X_{i+1}=B_{Z_i}X_i\); then \(X'\times_XX_{i+1}=B_{Z'_i}X'_i\) by flat base change. The transformed ideals and divisors also pull back correctly, by Lemma 2.4, so the conditions on the centres (smoothness, snc, order), which are local, hold for \(\mathbf B\). Set \(\overline{\mathcal B}(X)=\mathbf B\). Since \(g\) is surjective, any sequence \(\mathbf B'\) with \(g^*\mathbf B'=\mathcal B(X')\) equals \(\mathbf B\); this gives independence of the cover (compare two covers through their common refinement) and uniqueness of the extension.

For a smooth morphism \(h:Y\to X\) between triples of \(\mathcal{GT}\), let \(g:X'\to X\) be as above and \(Y'=Y\times_XX'\), with \(g_Y:Y'\to Y\) a surjective local isomorphism and \(h':Y'\to X'\) smooth. By construction \(g_Y^*\overline{\mathcal B}(Y)=\mathcal B(Y')\) (refine to a cover of \(Y\) in \(\mathcal{LT}\) if necessary, using (1)). By the hypothesis on \(\mathcal B\), \(\mathcal B(Y')\) is \(h'^*\mathcal B(X')=g_Y^*h^*\overline{\mathcal B}(X)\) with its empty blow-ups deleted. Since \(g_Y\) is surjective, a blow-up of \(h^*\overline{\mathcal B}(X)\) is empty if and only if its pull-back to \(Y'\) is empty. So \(\overline{\mathcal B}(Y)\) and \(h^*\overline{\mathcal B}(X)\) with empty blow-ups deleted have the same pull-back to \(Y'\), hence agree. The argument for change of field is the same. \(\square\)

**Remark 5.2 (why disjoint unions matter).** The theorem uses \(\mathcal B\) on the disconnected scheme \(\coprod U_\alpha\). A rule defined on connected schemes does not automatically say in which order to blow up centres in different connected components, and this order matters globally. Kollár gives the following example. Let \(C_1,C_2\) be curves in a smooth threefold \(X\) meeting in two points \(p_1,p_2\), where \(C_i\) is smooth except for a cusp at \(p_i\) whose tangent plane is transversal to the other curve. On \(X\setminus\{p_1\}\) one can blow up \(C_1\) first, after which the strict transform of \(C_2\) is smooth and can be blown up; on \(X\setminus\{p_2\}\) one proceeds the other way round. Over the overlap both give the blow-up of two disjoint smooth curves, so the two results glue to a proper morphism, which Kollár shows is locally but not globally projective. A functor commuting with open immersions has one sequence on \(X\setminus\{p_1,p_2\}\), which restricts both local choices; the two orders are incompatible there. Because a smooth centre cannot contain the singular curve \(C_2\), a functor must start by blowing up something at \(p_1\) and \(p_2\).

## 6. Exercises

**Exercise 6.1.** Let \(\mathbf B\) be the blow-up of a closed point \(p\) in \(\mathbf A^2\), and \(h:Y=\mathbf A^2\setminus\{p\}\to\mathbf A^2\) the inclusion. Describe \(h^*\mathbf B\) and the sequence obtained by deleting empty blow-ups.

*Solution.* The centre pulls back to the empty subscheme, so \(h^*\mathbf B\) is one empty blow-up of \(Y\), and deleting it gives the empty sequence. A functor commuting with smooth morphisms must therefore do nothing on \((Y,h^*\mathcal I,h^{-1}E)\) whenever it blows up only \(p\) on \(\mathbf A^2\).

**Exercise 6.2.** Let \(Z_1,Z_2\) be disjoint smooth centres in \(X\). Compare the sequences \(\mathbf B_1\): "blow up \(Z_1\), then \(Z_2\)", \(\mathbf B_2\): "blow up \(Z_2\), then \(Z_1\)", and \(\mathbf B_3\): "blow up \(Z_1\sqcup Z_2\)". Compute their pull-backs to \(X\setminus Z_1\) and \(X\setminus Z_2\), with empty blow-ups deleted.

*Solution.* All three end with \(B_{Z_1\sqcup Z_2}X\), but they are different sequences. On \(X\setminus Z_1\), all three become "blow up \(Z_2\)", and on \(X\setminus Z_2\) all three become "blow up \(Z_1\)". So the restrictions to these two opens do not determine which of the three a functor produces on \(X\); the order is extra information carried by the sequence, and Remark 5.2 shows that it cannot be chosen locally.

**Exercise 6.3.** For \(h:\mathbf A^3\to\mathbf A^2\), \((x,y,t)\mapsto(x,y)\), and \(\mathcal I=(x^2+y^3)\), verify Lemma 2.4 for the blow-up of the origin of \(\mathbf A^2\).

*Solution.* The pulled-back centre is the \(t\)-axis \(Z_Y=V(x,y)\), and \(B_{Z_Y}\mathbf A^3=B_0\mathbf A^2\times\mathbf A^1\). On the chart \(x=x_1y\) both transforms are \((x_1^2+y)\), now as an ideal on \(B_0\mathbf A^2\times\mathbf A^1\). The orders along the centres are \(2\) in both cases.

## References

- [Kollár] J. Kollár, *Resolution of singularities — Seattle lecture*, arXiv:math/0508332, sections on blow-up sequences, functoriality and the statements of the main theorems. <https://arxiv.org/abs/math/0508332>
- [Włodarczyk] J. Włodarczyk, *Simple Hironaka resolution in characteristic zero*, arXiv:math/0401401. <https://arxiv.org/abs/math/0401401>
