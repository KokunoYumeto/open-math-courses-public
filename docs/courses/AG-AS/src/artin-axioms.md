# Artin's axioms

*Retained source proofs by the Stacks Project authors, as distributed in the AI Integrated Stacks Project. Source copyright: Copyright (C) 2005 -- 2025 Johan de Jong. This modified course edition is published by the Open Math Courses project, `KokunoYumeto/open-math-courses`. Writing, adaptation and integration: GPT-6.1 Sol (OpenAI), Codex, Ultra, October 2026. Independent replacements and mathematical corrections: GPT-6 Astra (OpenAI), Codex, Ultra, 8 October 2026. Permission is granted to copy, distribute and modify this modified chapter under the GNU Free Documentation License, Version 1.2 or any later version, with no Invariant Sections, Front-Cover Texts or Back-Cover Texts. Eligible independently written additions retain their CC0 1.0 dedication. Self-checked by the writing AI. The [complete licence](../licenses/GFDL-1.2.txt) accompanies this edition.*

An algebraic stack has smooth coordinates, whereas a moduli problem usually arrives as a rule assigning a groupoid to each scheme. Artin's criterion constructs coordinates from that rule. The construction has three stages: obtain a versal deformation over a complete local ring, approximate it by a family of finite type, and enlarge its versal locus to an open set. A second argument explains why a flat presentation, even one with inseparable fibres, can be replaced by a smooth presentation.

Read [Algebraic stacks](algebraic-stacks.md) first. We use the quotient and bootstrap theorems of [The bootstrap theorem](bootstrap-theorem.md), Schlessinger's existence theorem for versal formal objects, the deformation theory of square-zero extensions and the naive cotangent complex, and the commutative algebra of completion and henselization. Precise imported statements appear at the end. All fibre products of groupoids below are 2-fibre products.

## 1. Infinitesimal objects, arrows and patching

Except in Section 6, let \(S\) be locally Noetherian and let \(\mathcal X\) be a category fibred in groupoids on schemes over \(S\). The subscript “fppf” on this category specifies its underlying site; it does not by itself assert descent.

A **finite type field over \(S\)** means a field \(k\) with a morphism \(\operatorname{Spec}k\to S\) of finite type. This is more restrictive than being a finitely generated extension of the residue field at an arbitrary point of \(S\). A point of a scheme is a **finite type point** if its inclusion as the spectrum of its residue field is of finite type. Such a point is closed in some open neighbourhood.

Fix \(x_0\in\mathcal X(k)\). Its predeformation groupoid \(\mathcal F_{k,x_0}(A)\), for an Artinian local \(S\)-algebra \(A\) with specified residue field \(k\), consists of pairs

\[
(x,\iota),\qquad x\in\mathcal X(A),\quad
\iota:x|_k\xrightarrow{\sim}x_0.
\]

An arrow respects \(\iota\). Pullback along a ring map gives a covariant functor on Artinian rings. The fibre at \(k\) is equivalent to the terminal groupoid: the marking removes the automorphisms of the chosen special object. Automorphisms of its deformations can remain.

### 1.1. The Rim–Schlessinger condition

For a diagram of Artinian local \(S\)-algebras

\[
A_1\longrightarrow A\longleftarrow A_2,\qquad
A_2\twoheadrightarrow A,\qquad P=A_1\times_A A_2,
\tag{1.1}
\]

whose spectra are of finite type over \(S\), condition **(RS)** requires the restriction functor

\[
\mathcal X(P)\longrightarrow
\mathcal X(A_1)\times_{\mathcal X(A)}\mathcal X(A_2)
\tag{1.2}
\]

to be an equivalence. The right side remembers the identification on \(A\). Applying (1.2) to marked objects proves that \(\mathcal F_{k,x_0}\) is a deformation category whenever \(\mathcal X\) has (RS).

Condition **(RS\(^*\))** requires the same equivalence for arbitrary \(S\)-algebras, with \(A_2\to A\) surjective and its kernel square zero. Filtering a nilpotent ideal into square-zero quotients shows that it implies (RS). The quantifier “arbitrary” is essential in Section 5, where products of modules need not be finite. These definitions are [Stacks, Tags 06L9 and 0CXN].

**Lemma 1.1 (the groupoid operations preserve patching).** If \(\mathcal X,\mathcal Y,\mathcal Z\) satisfy (RS), then \(\mathcal X\times_{\mathcal Y}\mathcal Z\) does too. The assertion also holds for (RS\(^*\)).

**Proof.** A patched object consists of an \(\mathcal X\)-object and a \(\mathcal Z\)-object on each side, and an arrow between their images in \(\mathcal Y\). Patch the two objects by essential surjectivity for \(\mathcal X\) and \(\mathcal Z\). Full faithfulness for \(\mathcal Y\) supplies the unique arrow between their images which restricts to the specified arrows. For morphisms, patch the two component arrows by full faithfulness and test their compatibility after restriction; faithfulness for \(\mathcal Y\) proves the compatibility upstairs. This proves both essential surjectivity and full faithfulness. \(\square\)

**Lemma 1.2 (algebraic stacks have (RS)).** Every algebraic stack satisfies (RS).

**Proof.** First, a diagram (1.1) is a pushout of affine schemes, and maps from its pushout to an algebraic space patch uniquely. One can check the latter assertion on étale scheme coordinates: after a finite étale cover of the Artinian local pushout, lift the common residue-field point to an étale chart; formal étaleness lifts that choice through the nilpotent thickenings. The two maps then land in a common affine chart, where the assertion is exactly the fibre product identity for rings. Unique lifts make the resulting maps compatible on overlaps, and the algebraic-space sheaf condition descends them. This also proves uniqueness.

For objects of an algebraic stack, use a smooth scheme atlas. After a finite étale cover of \(\operatorname{Spec}P\), the object over \(A_1\) lifts to the atlas: choose a finite separable residue-field point of its smooth atlas fibre and lift through the Artinian thickening. Its restriction to \(A\), together with the given identification, lifts across \(A_2\to A\) by smoothness. The two atlas maps agree on \(A\), and their closed points lie in a common affine atlas chart. The affine pushout patches them to a map from \(\operatorname{Spec}P\).

This constructs the desired object étale locally. The Isom spaces of two such objects are algebraic spaces, so the first paragraph proves that (1.2) is fully faithful. Consequently the local objects have unique compatible descent identifications, including the cocycle equality, and descend to the required object. \(\square\)

The stronger assertion for arbitrary affine pushouts along a thickening is [Stacks, Tag 07WM]. Its general flat-space patching input is not needed for the proof just given.

### 1.2. Two linear invariants

Write \(k[\epsilon]=k[\epsilon]/(\epsilon^2)\). For a deformation category, define

\[
T_{x_0}\mathcal X=
\pi_0\mathcal F_{k,x_0}(k[\epsilon]),\qquad
\operatorname{Inf}_{x_0}\mathcal X=
\ker\bigl(\operatorname{Aut}(x_0|_{k[\epsilon]})
 \to\operatorname{Aut}(x_0)\bigr).
\tag{1.3}
\]

Patching the split extensions \(k\oplus M\) makes these \(k\)-vector spaces. Addition uses the map \(k[M\oplus N]\to k[M]\) induced by addition of vectors, and scalar multiplication uses multiplication on the square-zero ideal. For infinitesimal automorphisms, addition agrees with composition; terms involving two elements of that ideal vanish.

More generally, under (RS\(^*\)) there are \(A\)-linear functors \(T_x(M)\) and \(\operatorname{Inf}_x(M)\) for \(x\in\mathcal X(A)\). The first is the set of marked lifts to \(A[M]=A\oplus M\), and the second is the automorphism group of the trivial marked lift. If \(A'\twoheadrightarrow A\) has square-zero kernel \(I\), then, when lifts exist, their isomorphism classes form a torsor under \(T_x(I)\). The automorphisms of every marked lift are canonically \(\operatorname{Inf}_x(I)\).

To see the torsor assertion, use

\[
A'\times_A A'\simeq A'\times_A A[I],
\quad
(a_1,a_2)\longmapsto
\bigl(a_1,(\overline a_1,a_2-a_1)\bigr).
\tag{1.4}
\]

Applying (RS\(^*\)) produces a difference between two lifts. On three lifts, the identity
\((a_3-a_1)=(a_2-a_1)+(a_3-a_2)\)
proves the addition law. Fixing one lift converts differences into the claimed simply transitive action. All constructions commute with maps of square-zero extensions. This is the mechanism behind [Stacks, Tag 07Y6].

**Lemma 1.3 (field change and fibre products).** Under (RS), a finite extension \(l/k\) gives

\[
T_{x_0}\mathcal X\otimes_k l\simeq
T_{x_0|_l}\mathcal X,\qquad
\operatorname{Inf}_{x_0}\mathcal X\otimes_k l\simeq
\operatorname{Inf}_{x_0|_l}\mathcal X.
\tag{1.5}
\]

For \(w=(x,z,\alpha)\) in \(\mathcal W=\mathcal X\times_{\mathcal Y}\mathcal Z\) there is an exact sequence

\[
\begin{aligned}
0\longrightarrow\operatorname{Inf}_w\mathcal W
&\longrightarrow\operatorname{Inf}_x\mathcal X\oplus
 \operatorname{Inf}_z\mathcal Z
\longrightarrow\operatorname{Inf}_y\mathcal Y\\
&\longrightarrow T_w\mathcal W
\longrightarrow T_x\mathcal X\oplus T_z\mathcal Z
\longrightarrow T_y\mathcal Y.
\end{aligned}
\tag{1.6}
\]

**Proof.** For an Artinian \(l\)-algebra \(B\), apply (RS) to \(B\times_l k\). It identifies marked \(k\)-deformations over that ring with marked \(l\)-deformations over \(B\). The field-change result for linear deformation functors then gives (1.5), including inseparable finite extensions.

In (1.6), the second map is the difference between the two induced infinitesimal automorphisms in \(\mathcal Y\). The boundary twists the trivial pair of deformations by an infinitesimal automorphism of its identifying arrow. Its kernel consists precisely of twists obtainable from component automorphisms. A pair of component deformations comes from \(\mathcal W\) exactly when their \(\mathcal Y\)-images are isomorphic as marked deformations; choices of such an isomorphism differ by the boundary. These observations verify exactness at each term. The constructions by split extensions make all the maps linear. The same proof gives (1.6) with \(T_x(M)\) and \(\operatorname{Inf}_x(M)\) under (RS\(^*\)). \(\square\)

*References:* [Stacks, Tags 07WW, 07WY and 07YT]. For a naive obstruction complex \(E_x\) as in Section 5.3, the analogous field-change maps on \(H^i(E_x\otimes^{\mathbf L}k)\) are isomorphisms for \(i=0,1\): they are dual to the identifications of \(T\) and \(\operatorname{Inf}\). The indices here are \(0,1\), not \(-1,0\).

**Lemma 1.4 (finiteness for an algebraic stack).** If an algebraic stack has a smooth atlas locally of finite type over \(S\), the two spaces (1.3) are finite dimensional.

**Proof.** After a finite separable field extension, lift the object to the atlas. Its tangent space is a quotient of the atlas tangent space, since smoothness lifts deformations. On an affine atlas chart \(\operatorname{Spec}B\) over \(\operatorname{Spec}\Lambda\), that space is
\(\operatorname{Hom}_B(\Omega_{B/\Lambda},k)\), which is finite dimensional because \(B\) is of finite type. The infinitesimal automorphisms inject into the tangent space at the identity point of the relation space; an étale scheme chart of that space is again locally of finite type. Apply the same argument and descend finiteness by (1.5). \(\square\)

This proof uses the finite module of differentials, so it also covers inseparable residue-field extensions. The reference is [Stacks, Tag 07X1].

## 2. Limits, complete local rings and approximation

### 2.1. Limit preservation includes arrows

The category \(\mathcal X\) is **limit preserving** if, for every directed inverse system of affine \(S\)-schemes with limit \(T=\lim T_i\),

\[
\mathop{\operatorname{colim}}_i\mathcal X(T_i)
\longrightarrow\mathcal X(T)
\tag{2.1}
\]

is an equivalence. An object must descend to some stage. An arrow between descended objects must descend after increasing that stage, and two arrows equal on \(T\) must become equal at a later stage. Requiring only descent of objects is weaker. For a morphism \(\mathcal X\to\mathcal Y\), “limit preserving on objects” refers to descent of a lift of an already descended \(\mathcal Y\)-object, including its specified identifying arrow. See [Stacks, Tags 07XK and 06CT].

Finite presentation of algebras, modules, étale charts and their finite diagrams gives the following useful test. An algebraic space \(Z\to B\) is locally of finite presentation exactly when its functor on affine \(B\)-schemes preserves directed limits. One checks this on étale affine charts; finite presentation descends the chart and its equality data, and the étale sheaf condition glues the descended morphisms. The converse on an affine chart is the ring criterion for finite presentation, followed by étale descent.

**Lemma 2.1 (testing on finite presentation bases).** Suppose \(\mathcal Y\) is limit preserving on objects and both categories are Zariski stacks. To establish representability of \(f:\mathcal X\to\mathcal Y\) by algebraic spaces, it suffices to establish it over affine tests \(V\) locally of finite presentation over \(S\), with a uniform allowable size bound. Once representability is known, any property stable under base change and fppf local on the target can be tested on those same \(V\).

**Proof.** An affine \(V\) mapping into \(\operatorname{Spec}\Lambda\subset S\) is a limit of affine schemes of finite presentation over \(\Lambda\). The object testing \(f\) descends to a stage \(V_i\); its entire fibre category is therefore represented by the base change of the representing space over \(V_i\). For general \(V\), do this on affine opens. On overlaps the representing spaces have canonical compatible isomorphisms, since they represent the same category. Zariski descent glues them. The size bound permits the coproduct of their charts in the chosen site.

For the property assertion, the same calculation identifies the general fibre morphism with a base change of a finite presentation test. Base change and locality prove the claim. \(\square\)

*References:* [Stacks, Tags 07WI and 06CT]. Fibre products preserve limit preservation: descend both component objects, then their identifying arrow, and finally the finitely many equalities required for a morphism.

### 2.2. Formal effectiveness is a groupoid assertion

A formal object over a Noetherian complete local \(S\)-algebra \(R\), with residue field of finite type over \(S\), is a compatible system
\(\xi_n\in\mathcal X(R/\mathfrak m^n)\), including its transition isomorphisms. It is **effective** if it is the completion of an object of \(\mathcal X(R)\). The stronger assertion used in axiom [4] is the equivalence

\[
\mathcal X(R)\xrightarrow{\ \sim\ }
\varprojlim_n\mathcal X(R/\mathfrak m^n).
\tag{2.2}
\]

The limit on the right is a groupoid of compatible systems. The equivalence must include all compatible arrows, not only the existence of algebraizations. These equivalences also respect the local base morphisms in the category of formal objects. See [Stacks, Tag 07X3].

**Lemma 2.2 (formal objects of algebraic stacks).** Every algebraic stack satisfies (2.2).

**Proof.** A compatible system of maps to a scheme has its closed point in one affine open. Ring maps into the complete ring \(R=\lim R/\mathfrak m^n\) then give the unique algebraized map. For an algebraic space, choose an étale chart at the formal closed point. After a finite étale extension \(R'/R\), formal étaleness gives compatible lifts to that chart. The scheme assertion algebraizes them. Their identifying arrows algebraize by the same argument on the chart relation, and faithfulness verifies the cocycle. Étale descent gives the unique map over \(R\).

For a stack, two objects have an algebraic-space Isom sheaf. The preceding paragraph proves full faithfulness in (2.2). To algebraize a formal object, choose a smooth atlas and a finite separable residue-field point of its first fibre. The corresponding finite étale extension \(R'\) of the complete local ring lifts this point. Smoothness successively lifts it at every order. The resulting maps to the scheme atlas algebraize. Over \(R'\otimes_RR'\), a finite product of complete local rings, full faithfulness algebraizes the formal descent arrows. It also proves their cocycle on the triple product and identifies the descended object's completion with the specified formal object. Effective étale descent finishes the proof. \(\square\)

Equivalences commute with 2-fibre products. Thus (2.2), just like (RS), passes to a fibre product of three categories satisfying it.

### 2.3. The approximation input and its use

A Noetherian ring is a **G-ring** when the completion map of each of its local rings has geometrically regular fibres. The approximation results used here are proved in Appendix B, with both separable and inseparable residue-field arguments included.

**Artin approximation.** For a regular homomorphism between Noetherian rings, Popescu's theorem expresses the target as a filtered colimit of smooth algebras over the source. Consequently, let $B$ be a henselian Noetherian local G-ring and let a finite polynomial system with coefficients in $B$ have a solution in $\widehat B$. For each $N\geq1$, there is an exact solution in $B$ with the same reduction modulo $\mathfrak m_B^N$. If $B$ is local without the henselian assumption, one obtains the solution in a pointed étale neighbourhood with unchanged residue field. See the proofs of [Popescu's theorem](#native-smoothing-theorem-popescu), [henselian approximation](#native-smoothing-theorem-approximation-property), and [pointed approximation](#native-smoothing-theorem-approximation-property-variant); the source locators are Stacks Tags 07GC, 07QY and 07QZ.

For families, it is useful to preserve the tangent cone together with the prescribed finite-order object.

**Lemma 2.3 (approximating a family).** Suppose $\mathcal X$ is limit preserving on objects. Let $x_R\in\mathcal X(R)$, where $R$ satisfies the complete local and finite-type residue-field hypotheses in (2.2), and let $s\in S$ be the image of its closed point. Assume that $\mathcal O_{S,s}$ is a G-ring. Given $N\geq1$, there are an $S$-algebra $A$ of finite type, a maximal ideal $\mathfrak n$ of $A$, and an object $x_A\in\mathcal X(A)$ with compatible identifications
$$
\begin{gathered}
A/\mathfrak n^N\simeq R/\mathfrak m_R^N,\qquad
x_A|_{A/\mathfrak n^N}\simeq x_R|_{R/\mathfrak m_R^N},\\
\operatorname{gr}_{\mathfrak n}A\simeq\operatorname{gr}_{\mathfrak m_R}R.
\end{gathered}
\tag{2.3}
$$
The first map is an $S$-algebra isomorphism, the second is an isomorphism over that map, and the last is an isomorphism of graded algebras over the common residue field.

**Proof.** Apply [Theorem 6.1 in B.6.1, including its complete proof](#reader-family-approximation), to $x=x_R$ and the specified $N$. Its hypotheses are exactly those stated here: it uses limit preservation on objects, the G-ring condition at $s$, and the finite-type residue field, without an additional requirement on characteristic or on descent of arrows.

The proof there approximates a finite presentation together with its syzygy matrix at an order $M\geq\max(N,c+1)$, where $c$ is a common Artin–Rees constant. The exact perturbed syzygies and [Lemma A.2](#appendix-a-artin-rees-perturbation-and-graded-quotients) identify the initial ideals, giving the graded **algebra** isomorphism. Its final finite-type descent preserves the residue field, every maximal-ideal quotient, and the selected marking on the object. Restriction from order $M$ to order $N$ therefore yields all three identifications in (2.3). ∎

The source result is Stacks Tag 07XB. The complete family construction is kept at B.6.1, and its finite-complex perturbation argument is proved in Appendix A.

## 3. From versality to a smooth chart

A formal object \(\xi\) over \(R\) is **versal** if its functor of marked pullbacks to Artinian local rings is smooth: a pullback over \(B\) can be lifted across every small extension \(B'\twoheadrightarrow B\), together with the specified identification with a deformation over \(B'\). A small extension has one-dimensional residue-field kernel.

For \(x\in\mathcal X(U)\), with \(U\) locally of finite type over \(S\), say that \(x\) is **versal at \(u\)** when

\[
\mathcal F_{U,\kappa(u),u}\longrightarrow
\mathcal F_{\mathcal X,\kappa(u),x_u}
\tag{3.1}
\]

is smooth. Maps from Artinian local rings with that closed point factor uniquely through the completion of \(\mathcal O_{U,u}\); thus (3.1) is exactly versality of the completed object.

The Schlessinger theorem used as a prerequisite says that (RS) and finite-dimensional tangent space give a versal formal object with Noetherian complete local parameter ring [Stacks, Tag 06IW]. It concerns groupoids and retains their markings; it does not require absence of automorphisms.

**Lemma 3.1 (algebraizing a versal chart).** If \(\xi\) is effective and versal, \(\mathcal X\) is limit preserving on objects, and \(\mathcal O_{S,s}\) is a G-ring at its image point, then \(\xi\) is isomorphic to the completion of a finite type family \(x_A\) at a point with the same residue field.

**Proof.** Apply Lemma 2.3 with \(N=2\). Versality successively lifts the identifying map at order two to a compatible map from \(\xi\) to the completion of \(x_A\). Its ring map
\(R\to\widehat{A_{\mathfrak n}}\)
is surjective: it is surjective on the residue field and cotangent space, and complete Nakayama gives surjectivity at each order, then on the inverse limit. The two rings have equal dimensions of all graded pieces by (2.3). The surjections on their Artinian quotients therefore have equal finite lengths and are isomorphisms. Their inverse limit is an isomorphism, including the family and its transition identifications. \(\square\)

*Reference:* [Stacks, Tag 07XH]. Approximation alone would not preserve versality; the graded-ring comparison supplies the missing step.

**Lemma 3.2 (versal everywhere implies smooth).** Suppose \(\mathcal X\) has representable diagonal, satisfies (RS), and is limit preserving. If \(U\) is locally of finite type over \(S\) and \(x\in\mathcal X(U)\) is versal at every finite type point, then \(U\to\mathcal X\) is smooth.

**Proof.** Its base change by an affine \(V\to\mathcal X\) locally of finite presentation over \(S\) is an algebraic space \(Z=U\times_{\mathcal X}V\). The finite presentation limit test and the fibre product argument in Section 2 show that \(Z\) is locally of finite presentation over \(S\). Choose an étale scheme chart \(W\to Z\).

At a finite type point \(w\), the induced field-valued point of \(U\) has finite residue extension of the image point. Lemma 1.3 and smoothness under field change for deformation categories therefore preserve versality. The deformation category of \(Z\) is the fibre product of those of \(U\) and \(V\) over that of \(\mathcal X\). Smoothness of (3.1) passes to this fibre product and then through \(W\to Z\). The Artinian lifting test for a morphism of schemes locally of finite type over a locally Noetherian scheme [Stacks, Tag 02HX] makes \(W\to V\) smooth at \(w\).

The smooth locus is open. Every nonempty closed subset of a scheme contains a point closed in an affine open, hence a finite type point. Thus this locus is all of \(W\). Smoothness descends through the étale chart to \(Z\to V\). Lemma 2.1 extends the conclusion to arbitrary tests \(V\). \(\square\)

The same argument at a single finite type point proves the version used later: for finite type \(U,V\), versality at \(u\) makes \(U\times_{\mathcal X}V\to V\) smooth at each finite type point above \(u\). The representable diagonal is locally of finite type because its Isom functors preserve limits. These statements explain [Stacks, Tags 07XD and 07XP].

**Openness of versality** asks that a versal finite type point of every finite type family have an open neighbourhood on whose finite type points the family is versal. For \(f:\mathcal X\to\mathcal Y\), it means openness for every base change by a finite type scheme over \(\mathcal Y\). In particular, openness for a diagonal is a separate condition.

## 4. The axioms and the two Artin criteria

Here is the numbering of [Stacks, Tag 07XJ].

| Axiom | Requirement |
|---|---|
| [−1] | One allowable cardinal bounds the object isomorphism classes and arrow sets of all finite type field fibres, so the required family of charts belongs to the chosen site. |
| [0] | \(\mathcal X\) is a stack for the étale topology. |
| [1] | The full groupoid equivalence (2.1) holds. |
| [2] | \(\mathcal X\) satisfies (RS). |
| [3] | Both spaces (1.3) are finite dimensional at every finite type field object. |
| [4] | Completion to formal objects is an equivalence, including arrows, as in (2.2). |
| [5] | Openness of versality holds for \(\mathcal X\) and for \(\Delta_{\mathcal X}\). |

Fix small models of the field groupoids when recording the bound in [−1]; the construction chooses representatives of their isomorphism classes. For a functor in sets, [0] says étale sheaf, [3] concerns only tangents, [4] is bijectivity of completion, and [5] asks openness for the functor itself. This is [Stacks, Tag 07XZ].

**Theorem 4.1 (Artin with representable diagonal).** Suppose \(\mathcal O_{S,s}\) is a G-ring for every finite type point \(s\) of \(S\). Suppose \(\mathcal X\) has representable diagonal, satisfies [−1]–[3], every formal object is effective, and openness of versality holds for \(\mathcal X\). Then \(\mathcal X\) is an algebraic stack. If it is a functor in sets, it is an algebraic space.

**Proof.** For every finite type field object \(x_0\), Schlessinger's theorem gives a versal formal object. Effectiveness and Lemma 3.1 give a finite type scheme family through \(x_0\), at a point with exactly its residue field. Shrink that scheme by openness of versality. Lemma 3.2 makes the resulting morphism to \(\mathcal X\) smooth. Axiom [−1] allows their disjoint union \(U\).

For an affine finite presentation test \(V\to\mathcal X\), the image of \(U\times_{\mathcal X}V\to V\) is open. It contains every finite type point \(v\): the chart chosen for the object over \(\kappa(v)\), and its specified special point, give a point of this fibre product above \(v\). The complement must consequently be empty. Lemma 2.1 proves surjectivity on every test.

The relation \(R=U\times_{\mathcal X}U\) is an algebraic space, with smooth projections. The quotient stack of this smooth groupoid is algebraic by Lesson 5. It agrees with \(\mathcal X\) as an étale stack: smooth surjections have local sections for the étale topology, so every \(\mathcal X\)-object has local coordinates in \(U\); its arrows and their composition are exactly \(R\). Étale descent identifies the two stacks, proving also the fppf stack condition.

For a functor in sets the quotient has no automorphisms. The smooth relation is an equivalence relation. The flat bootstrap of Lesson 2 identifies its sheaf quotient as an algebraic space, and the same étale local-coordinate argument identifies that space with the original functor. \(\square\)

This proves [Stacks, Tags 07Y1 and 07Y4], including the functor criterion's assumption that its diagonal is representable by algebraic spaces.

### 4.1. Recovering the diagonal

The **second diagonal**

\[
\Delta_\Delta:\mathcal X\longrightarrow
\mathcal X\times_{\mathcal X\times_S\mathcal X}\mathcal X
\tag{4.1}
\]

is the identity section of the inertia category. Its representability says that the condition \(\alpha=\operatorname{id}\), for a family of automorphisms, is represented by an algebraic space over its parameter scheme. For two isomorphisms \(\alpha,\beta:x\to y\), equality is the condition \(\alpha^{-1}\beta=\operatorname{id}_x\). Consequently (4.1) is representable exactly when every Isom functor has representable diagonal. This is the direct equality test in [Stacks, Tag 07WG].

**Theorem 4.2 (Artin's stack criterion).** Let \(S\) be locally Noetherian, with \(\mathcal O_{S,s}\) a G-ring at every finite type point. Let \(\mathcal X\) satisfy [−1]–[5]. If its second diagonal (4.1) is representable by algebraic spaces, then \(\mathcal X\) is an algebraic stack.

**Proof.** Take an affine \(V\) locally of finite presentation over \(S\), and two objects \(x_1,x_2\in\mathcal X(V)\). Their Isom category is a setoid: an object is an isomorphism between the two fixed objects, and it has no nontrivial automorphisms after the two identifications are fixed. Thus its isomorphism-class functor \(I\) is an étale sheaf, by [0]. Its diagonal is representable by the equality test above.

We verify the remaining functor axioms for \(I\). The bound [−1] follows from the bound on arrows in \(\mathcal X\). Limits and (RS) follow by forming the fibre product of \(\mathcal X\to\mathcal X\times_S\mathcal X\) with \(V\), using Lemma 1.1 and the full arrow version of limit preservation. The six-term sequence (1.6) shows that its tangent space is an extension of subquotients of the tangents and infinitesimal automorphisms of \(\mathcal X\) and \(V\); all are finite dimensional. Lemma 2.2 gives effectiveness for the scheme \(V\), and axiom [4] for \(\mathcal X\), together with full faithfulness, algebraizes the identifying arrows. Completion therefore commutes with this fibre product. Finally [5] for \(\Delta_{\mathcal X}\) is exactly openness of versality for \(I\).

The base \(V\) is locally Noetherian. Its local rings at finite type points are essentially of finite type over the corresponding local rings of \(S\), so they are G-rings [Stacks, Tag 07PV]. The functor case of Theorem 4.1 now makes \(I\) an algebraic space over \(V\). Lemma 2.1 extends this assertion from finite presentation tests to all tests; its size bound is the field-arrow bound just used, together with the size of the finite type charts constructed in Theorem 4.1. Thus \(\Delta_{\mathcal X}\) is representable.

Apply the stack case of Theorem 4.1. Its hypotheses are now established, and its smooth atlas proves the conclusion. \(\square\)

*Reference:* [Stacks, Tag 07Y5]. Neither representability of the first diagonal nor algebraicity is assumed in this argument. The G-ring condition is used at the approximation stage, before constructing the atlas.

## 5. Two ways to prove openness

### 5.1. A failed lift can be placed in a family

We first isolate the argument which lets infinitesimal information detect an open locus. Suppose \(\mathcal X\) has (RS\(^*\)), representable diagonal, and limit preservation. Work with \(x\in\mathcal X(A)\), where \(U=\operatorname{Spec}A\) is of finite type over \(\operatorname{Spec}\Lambda\subset S\).

**Lemma 5.1 (a witness to nonversality).** If \(x\) is not versal at a finite type point \(u\), there is a square-zero extension \(C\twoheadrightarrow A\) with kernel \(\kappa(u)\), and a marked lift \(y\in\mathcal X(C)\), which admits no retraction to the family \(x\) on any open neighbourhood of \(u\).

Here a retraction means a morphism \(r:\operatorname{Spec}C\to U\) restricting to the identity on \(U\), and an isomorphism \(y\simeq r^*x\) restricting to the marking \(y|_U\simeq x\).

**Proof.** Failure of versality is witnessed by a small extension \(B'\twoheadrightarrow B\), a map \(A\to B\) with closed point \(u\), and a lift of the resulting object over \(B'\), for which the specified lifting problem has no solution. Take
\(C=A\times_B B'\).
Its kernel is the one-dimensional \(\kappa(u)\)-module of the small extension. Condition (RS\(^*\)) patches \(x\) and the object over \(B'\) to \(y\). A retraction near \(u\) pulls back to \(\operatorname{Spec}B'\), whose sole point lies over \(u\). It would supply exactly the forbidden lift, with its required identification. \(\square\)

**Lemma 5.2 (retraction near a versal point).** Let \(u_0\) be a versal finite type point. Every marked lift of \(x\) over a square-zero extension \(D\twoheadrightarrow A\) which is of finite type over \(\Lambda\) admits a retraction after shrinking around \(u_0\). The same assertion holds for a possibly infinite extension whenever its marked lift descends to such a finite type extension.

**Proof.** For the descended family \(x_D\), form
\(Z=U\times_{\mathcal X}\operatorname{Spec}D\).
The marking gives a section \(i:U\to Z\) over the thickening \(U\subset\operatorname{Spec}D\). The single-point version of Lemma 3.2 shows that \(Z\to\operatorname{Spec}D\) is smooth at \(i(u_0)\). Shrink \(U\) so it is smooth along the whole section. The infinitesimal lifting property of this smooth algebraic space lifts \(i\) across the affine square-zero thickening. The lifted map to \(Z\) supplies both a retraction to \(U\) and the desired isomorphism of objects. Pullback gives the final assertion. \(\square\)

These lemmas also show that versality is preserved under generalization among finite type points. Indeed, descend the witness of Lemma 5.1 to a finite type \(\Lambda\)-subalgebra of \(C\) containing lifts of generators of \(A\). Its map to \(A\) is surjective and its kernel square zero. If \(u\) specialized to a versal \(u_0\), Lemma 5.2 would retract it on a neighbourhood of \(u_0\), hence on a neighbourhood of \(u\), a contradiction.

The following modest Noetherian topological facts will be used. Every subset has the same closure as its points maximal under generalization, and an infinite dense subset of a Noetherian scheme has a countable dense subset [Stacks, Tags 0G2R and 0G2F]. Consequently, if the nonversal finite type points accumulate at a versal \(u_0\), one can choose a countable sequence \(u_i\) of nonversal points, with no specializations between them, whose closure contains \(u_0\). No individual \(u_i\) specializes to \(u_0\).

This gives the strong-effectiveness criterion of [Stacks, Tag 0CXU]. If every compatible system over surjective ring towers \(R_n\), with square-zero \(\ker(R_m\to R_n)\) for \(m\geq n\), is effective over \(\lim R_n\), then openness of versality holds. To prove it, take the witnesses \(C_i\to A\) just constructed and their finite fibre products

\[
R_n=C_1\times_A\cdots\times_A C_n.
\tag{5.1}
\]

Their kernels over \(A\) are direct sums of \(\kappa(u_i)\), with square-zero multiplication. Condition (RS\(^*\)) patches their marked objects compatibly. Strong effectiveness gives an object over \(\lim R_n\). Limit preservation descends that object to a finite type subalgebra surjecting onto \(A\). Lemma 5.2 gives a retraction near \(u_0\). Pulling it to any \(C_i\) whose point lies in that neighbourhood contradicts Lemma 5.1. Thus the accumulating sequence cannot exist. This proves the criterion, with its stronger tower hypothesis explicitly distinguished from axiom [4].

### 5.2. Product-compatible obstruction modules

An **obstruction theory** consists of \(A\)-linear functors
\(\mathcal O_x:\operatorname{Mod}_A\to\operatorname{Mod}_A\),
functorial in the object, base ring and module, and elements

\[
o_x(A')\in\mathcal O_x(I),\qquad I=\ker(A'\to A),
\tag{5.2}
\]

for each square-zero extension. They must commute with maps of deformation situations, and must satisfy

\[
x\text{ has a marked lift to }A'
\quad\Longleftrightarrow\quad o_x(A')=0.
\tag{5.3}
\]

Functoriality includes the identity and composition laws for maps \((A,x,M)\to(B,x|_B,N)\), with an \(A\)-linear map \(M\to N\). An obstruction module without the equivalence (5.3) is insufficient for the theorem below. See [Stacks, Tag 07YG].

**Theorem 5.3 (the product criterion).** Suppose \(\mathcal X\) has representable diagonal, (RS\(^*\)), and limit preservation. Suppose it has an obstruction theory such that for every object \(x\) and every countable collection of modules \(M_i\),

\[
T_x\Bigl(\prod_i M_i\Bigr)\xrightarrow{\sim}
\prod_iT_x(M_i),\qquad
\mathcal O_x\Bigl(\prod_i M_i\Bigr)\longrightarrow
\prod_i\mathcal O_x(M_i)\ \text{is injective}.
\tag{5.4}
\]

Then \(\mathcal X\) satisfies openness of versality.

**Proof.** If openness fails at \(u_0\), choose the sequence and marked witnesses \(y_i/C_i\) of Section 5.1. Form the ring

\[
D=\prod_A C_i
=\{(c_i)\in\prod_iC_i:\text{all images in }A\text{ agree}\}.
\]

It surjects onto \(A\) with square-zero kernel \(M=\prod_i\kappa(u_i)\). The obstruction \(o_x(D)\) maps to \(o_x(C_i)=0\) for every \(i\). Injectivity in (5.4) makes it zero, so choose a marked lift \(y/D\).

For each \(i\), its restriction and \(y_i\) differ by \(t_i\in T_x(\kappa(u_i))\), using the torsor of Section 1.2. The first condition of (5.4) supplies \(t\in T_x(M)\) with all these components. Replace \(y\) by \(t\cdot y\). Its restrictions are now isomorphic to the specified \(y_i\) as marked lifts. In particular the isomorphisms respect \(x\), which is necessary for the next step.

Limit preservation descends \(y\) to a finite type \(\Lambda\)-subalgebra \(D_0\subset D\). Increase \(D_0\) to include lifts of generators of \(A\). Then \(D_0\twoheadrightarrow A\) is a finite type square-zero extension, and its family restricts to \(x\) with the inherited marking. Lemma 5.2 retracts it near \(u_0\). Pull this retraction through \(D_0\to D\to C_i\). Since \(u_0\) lies in the closure of the \(u_i\), some \(u_i\) lies in that neighbourhood. The retraction of the corresponding marked \(y_i\) contradicts its defining property.

This proves the theorem directly; no effectiveness assertion for objects over infinite towers is assumed. \(\square\)

This is [Stacks, Tag 0CYF]. The proof only needs compatibility of obstruction classes for maps with fixed quotient \(A\), but (5.2) has been stated with the usual full functoriality.

### 5.3. Naive cotangent obstruction theories

Use cohomological indexing. For \(A=\Lambda[z_1,\ldots,z_r]/J\), the naive cotangent complex is

\[
\mathrm{NL}_{A/\Lambda}=
\bigl[J/J^2\longrightarrow A^{\oplus r}\bigr]
\quad\text{in degrees }-1,0.
\tag{5.5}
\]

A square-zero surjection \(A'\to A\) with kernel \(I\) gives
\(\mathrm{NL}_{A/A'}\simeq I[1]\).
The successive maps of naive cotangent complexes have zero composition, but in general do not form a distinguished transitivity triangle.

A **naive obstruction theory** assigns \(E_x\in D^-(A)\) and
\(\xi_x:E_x\to\mathrm{NL}_{A/\Lambda}\), together with

\[
\operatorname{Inf}_x(M)\simeq
\operatorname{Ext}^{-1}_A(E_x,M),\qquad
T_x(M)\simeq\operatorname{Ext}^{0}_A(E_x,M).
\tag{5.6}
\]

Its required compatibilities are as follows. Base change \(A\to B\) gives maps \(E_x\to E_{x|_B}\) in \(D(A)\), compatible with \(\xi\), identities and compositions. The identifications (5.6) respect the module and base-change maps of Section 1.2. The class of \(E_x\to\mathrm{NL}_{A/\Lambda}\to\Omega_{A/\Lambda}\) is the canonical deformation obtained by pulling \(x\) along
\(a\mapsto(a,da)\) into \(A[\Omega_{A/\Lambda}]\). Finally, \(x\) lifts across \(A'\to A\) exactly when

\[
E_x\longrightarrow\mathrm{NL}_{A/\Lambda}
\longrightarrow \mathrm{NL}_{A/A'}\simeq I[1]
\tag{5.7}
\]

is zero in \(D(A)\). All these requirements, not just a complex of finite modules, enter the definition [Stacks, Tag 07YP].

**Lemma 5.4 (the fibre criterion).** Assume (RS\(^*\)) and the tangent and obstruction properties just specified for \(x/A\). At a finite type point \(u\) with residue field \(k\), consider

\[
\begin{split}
H^{-1}(E_x\otimes_A^{\mathbf L}k)&\twoheadrightarrow
H^{-1}(\mathrm{NL}_{A/\Lambda}\otimes_A^{\mathbf L}k),\\
H^0(E_x\otimes_A^{\mathbf L}k)&\hookrightarrow
H^0(\mathrm{NL}_{A/\Lambda}\otimes_A^{\mathbf L}k).
\end{split}
\tag{5.8}
\]

These conditions imply versality. If \(u\) is closed in \(U\), versality implies them.

**Proof.** For a bounded-above complex \(E\),
\[
\operatorname{Ext}^i_A(E,k)
\simeq\operatorname{Hom}_k(H^{-i}(E\otimes_A^{\mathbf L}k),k).
\tag{5.9}
\]
Resolve by free modules and split the resulting complex of vector spaces to obtain this identity.

The second condition of (5.8), by (5.9) and the canonical-element compatibility, says that
\(\operatorname{Der}_\Lambda(A,k)\to T_x(k)\)
is surjective. For a small extension \(B'\to B\) with residue field \(k\), the obstruction to lifting \(A\to B\) is in
\(\operatorname{Ext}^1_A(\mathrm{NL}_{A/\Lambda},k)\).
The first condition makes its map to \(\operatorname{Ext}^1_A(E_x,k)\) injective. If the pulled-back object lifts to \(B'\), (RS\(^*\)) gives a lift of \(x\) to \(A\times_BB'\), so (5.7) kills that image. The ring obstruction is therefore zero. Choose a lift of the ring map. Its object may differ from the prescribed marked object by a tangent class, but the surjectivity on tangents adjusts the lift by a derivation to remove the difference. This solves the lifting problem, including its identifying arrow, and proves sufficiency.

For necessity, tangent surjectivity follows immediately from versality. Suppose the first map in (5.8) were not onto. Choose a functional on
\(H^{-1}(\mathrm{NL}\otimes^{\mathbf L}k)\)
which kills the image and is nonzero. Extend it to \(J/J^2\otimes_Ak\), and denote the resulting functional by \(\lambda\). With \(P=\Lambda[z_1,\ldots,z_r]\), set

\[
A'=P/\ker\bigl(J\longrightarrow J/J^2\otimes_Ak
 \xrightarrow{\lambda}k\bigr).
\tag{5.10}
\]

Since \(u\) is closed, the nonzero image is all of \(k\); the kernel \(I\) of \(A'\to A\) is \(k\) and has square zero. The differential of the discarded relation lies in the kernel of \(J/J^2\otimes k\to k^{\oplus r}\). Equivalently, the image under this differential of \(\ker\lambda\) equals the image of all \(J/J^2\otimes k\): subtract a multiple of an element in the differential kernel on which \(\lambda=1\). Thus \(\Omega_{A'/\Lambda}\otimes k\to\Omega_{A/\Lambda}\otimes k\) is an isomorphism. The extension is essential: a section would add the nonzero derivation to \(I=k\), contrary to that isomorphism of differential fibres.

By (5.9), the choice of \(\lambda\) makes \(E_x\to I[1]\) zero. Therefore \(x\) lifts to \(A'\). Artin–Rees gives \(n\) with \((\mathfrak m')^n\cap I=0\). The extension
\[
B'=A'/(\mathfrak m')^n\longrightarrow
B=A/\mathfrak m^n
\]
still has kernel \(k\), and remains essential. Versality lifts the quotient map from the completed local ring of \(A\) to \(B\) to a map into \(B'\), with the lifted object. Because the maximal ideal of \(B'\) has \(n\)-th power zero, that map factors through \(B\) and is a section, a contradiction. The first map of (5.8) must be surjective. \(\square\)

This supplies the essential-extension argument behind [Stacks, Tags 07YJ and 07YN], without assuming a transitivity triangle for (5.5).

**Theorem 5.5 (naive obstruction theory gives openness).** Suppose \(\mathcal X\) has (RS\(^*\)) and a naive obstruction theory. If every \(E_x\) over a finite type base has finitely generated cohomology modules, then \(\mathcal X\) satisfies openness of versality.

**Proof.** Shrink a finite type family so its versal point \(u_0\) is closed and the base is affine. Set \(C=\operatorname{Cone}(\xi_x)\). It is bounded above with finite cohomology, since \(A\) is Noetherian and the naive cotangent complex has finite modules. By Lemma 5.4 and the cohomology exact sequence of the cone,
\(H^{-1}(C\otimes^{\mathbf L}k(u_0))=0\).

Represent \(C\) by a bounded-above complex of finite free modules locally near \(u_0\). Over the residue field it is exact in degree \(-1\). Choose bases for the image of the incoming differential and a complement mapping isomorphically onto the image of the outgoing differential. Invert the finitely many corresponding matrix minors. Cancelling these invertible blocks removes the whole degree \(-1\) term. The remaining complex consequently has
\(H^{-1}(C\otimes^{\mathbf L}M)=0\)
for every module on that open neighbourhood.

In particular the fibre cone has zero \(H^{-1}\) at every point there. Its cohomology sequence gives both conditions (5.8), and their sufficient direction proves versality at every finite type point in the neighbourhood. \(\square\)

*Reference:* [Stacks, Tag 07YU]. This criterion needs the functoriality and canonical tangent class in (5.6)–(5.7). It does not replace them by the bare assertion that obstructions happen to lie in a finite module.

## 6. Flat groupoids over an arbitrary base

In this section \(S\) is any scheme. No Noetherian or G-ring hypothesis is imposed. The flat bootstrap for sheaves from Lesson 2 will be used, while the stack version will be proved.

### 6.1. Finite sources and restriction of scalars

**Lemma 6.1 (maps from a finite locally free space).** If \(Z\to B\) is finite locally free and \(X\to Z\) is an algebraic space, the functor
\[
\operatorname{Res}_{Z/B}(X)(T)=
\operatorname{Mor}_{Z}(Z_T,X)
\tag{6.1}
\]
is an algebraic space. Restriction of scalars carries a surjective étale morphism to a surjective étale morphism.

**Proof.** We explain the étale assertion first. For \(W\to Z\) étale, its section functor over \(B\) is étale and representable. This can be checked over an affine \(B\). If \(W\to Z\) is separated, a section is an open-and-closed subscheme of \(W_T\), finite locally free over \(T\), mapping isomorphically to \(Z_T\).

The finite-part construction of Lesson 2 applies to the separated, flat, locally finitely presented, locally quasi-finite map \(W\to B\), without the extra requirement of containing an identity section. Over the affine base, separated locally quasi-finite recognition first makes \(W\) a scheme. The construction's proof is unchanged: over a henselian local base, isolate a selected finite union of fibre components; scheme Zariski main and idempotent lifting extend it to a finite open-and-closed part; finite presentation descends it to an étale neighbourhood. Equality of two such parts is an open-and-closed condition, computed by the ranks of their two finite locally free differences. The étale quotient of these charts represents the finite-part functor.

Within that functor, the condition of mapping isomorphically to \(Z_T\) is open. The map from a selected finite part to \(Z_T\) is finite étale. Its rank is one exactly on the isomorphism locus; the complement of that locus is closed in \(Z_T\), and its finite image in \(T\) is closed. Thus the section functor is an open subspace of the finite-part space and is étale over \(B\).

For a general \(W\), cover it by a disjoint union \(W'\) of affine schemes over the affine base. Its map to \(Z\), and its map to \(W\), are separated. Sections of \(W'\to Z\) therefore form an algebraic space by the preceding argument. They cover the section functor of \(W\to Z\) étale locally: over a strictly henselian local base, the finite scheme \(Z\) is a product of henselian local factors with separably closed residue fields. A surjective étale cover has a section on each factor. Their finite union of choices descends to an étale neighbourhood of the base. The same separated calculation describes every fibre of the map of section functors. The étale bootstrap of Lesson 2 now proves the general assertion.

For an étale map \(X'\to X\), the fibre of its restriction of scalars at a map \(Z_T\to X\) is precisely the section functor of \(Z_T\times_XX'\to Z_T\). This proves representability and étaleness, and the preceding local section argument proves surjectivity when the original map is surjective.

Now trivialize the finite locally free algebra of \(Z\) on affine base opens, and take an étale cover \(X'\to X\) with \(X'\) a disjoint union of affine schemes. For a finite union of these affines, maps from \(Z_T\) are described by algebra maps into the finite free algebra of \(Z_T\). Choose its basis; coordinates for the images of generators and polynomial relations describe an affine scheme. The requirement that a map be over \(Z\) imposes the corresponding equations. Infinite presentations cause no difficulty for representability. Every map from a quasi-compact \(Z_T\) uses only finitely many of the affine components. The finite-component functors are open subfunctors, since \(Z_T\to T\) is finite and the excluded image has closed image in \(T\). They glue to represent restriction of scalars for \(X'\).

The étale assertion already proved gives a representable surjective étale map from that space to (6.1). The sheaf condition follows from descent of morphisms. The étale bootstrap proves (6.1). \(\square\)

This proves the restriction-of-scalars input [Stacks, Tag 05YF], including the étale assertion [Stacks, Tag 05YD]. The finite-part argument also explains why separatedness was needed only in an intermediate chart. No separatedness of \(X\) is assumed.

### 6.2. The finite Hilbert stack used here

Let \(\mathcal H_d\), for \(d\geq1\), classify finite locally free schemes \(Z\to T\) of degree \(d\). Let \(\mathcal H_d(X)\) also remember a map \(Z\to X\). These objects are finite maps, not necessarily closed subschemes.

**Lemma 6.2.** Both \(\mathcal H_d\) and \(\mathcal H_d(X)\), for an algebraic space \(X\), are algebraic stacks.

**Proof.** Put an arbitrary commutative unital algebra structure on the free module of rank \(d\). Its multiplication coefficients \(c_{ij}^k\) and unit coefficients satisfy finitely many equations expressing commutativity, associativity and the two unit identities. They define an affine scheme \(\operatorname{Alg}_d\) over \(\mathbf Z\). Change of basis gives an action of the smooth group \(\operatorname{GL}_d\).

A finite locally free algebra has a Zariski locally chosen basis. The basis changes and all their compatibility equations identify its stack with
\([\operatorname{Alg}_d/\operatorname{GL}_d]\), after base change to \(S\). This quotient is algebraic by the smooth quotient theorem of Lesson 5. Passing between the algebra groupoid and the finite-scheme groupoid uses \(\varphi\mapsto\operatorname{Spec}(\varphi^{-1})\) on isomorphisms; this inversion makes the functor covariant.

For a fixed finite scheme \(Z/T\), the fibre of
\(\mathcal H_d(X)\to\mathcal H_d\)
is the space of maps \(Z\to X\). Lemma 6.1 represents it. Pull back a smooth atlas of \(\mathcal H_d\); its fibre is an algebraic space, and its smooth scheme atlas supplies a smooth atlas of \(\mathcal H_d(X)\). The diagonal is represented by the same finite-source equality construction. \(\square\)

*References:* [Stacks, Tags 05YQ and 05YS]. Finite locally free algebras and their isomorphisms descend because their modules, multiplication and unit descend.

Suppose \(q:U\to\mathcal Y\) is representable, surjective, flat and locally of finite presentation, with \(U\) an algebraic space and \(\mathcal Y\) an fppf stack. Define \(\mathcal H_d(U/\mathcal Y)\) to have objects

\[
(Z/T,\ y\in\mathcal Y(T),\ f:Z\to U,\
\alpha:y|_Z\xrightarrow{\sim}q(f)).
\tag{6.2}
\]

**Lemma 6.3.** The diagonal of \(\mathcal Y\) is representable, and every \(\mathcal H_d(U/\mathcal Y)\) is an algebraic stack.

**Proof.** For two objects over a scheme \(T\), choose an fppf scheme cover \(T'\to T\) lifting both to \(U\). Their Isom sheaf over \(T'\) is the pullback of the algebraic space \(U\times_{\mathcal Y}U\) along their two coordinate maps. Its map to the original Isom sheaf is representable, flat, locally of finite presentation and surjective, being the base change of \(T'\to T\). The flat sheaf bootstrap makes the original Isom sheaf algebraic. Thus the diagonal is representable.

The map
\[
\mathcal H_d(U/\mathcal Y)\longrightarrow
\mathcal H_d(U)\times\mathcal Y
\tag{6.3}
\]
is representable: over a fixed \((Z/T,f,y)\), it is
\(\operatorname{Res}_{Z/T}\operatorname{Isom}_{\mathcal Y}(y|_Z,q(f))\),
an algebraic space by Lemma 6.1.

Choose a smooth scheme atlas \(P\to\mathcal H_d(U)\), and set
\(W=P\times_{\mathcal H_d(U)}\mathcal H_d(U/\mathcal Y)\).
This is a stack in setoids. An automorphism over the fixed \(Z\) and \(f\) restricts to the identity on \(y|_Z\); the finite locally free map \(Z\to T\) is an fppf cover because \(d>0\), so descent of arrows makes it the identity on \(y\).

By (6.3), \(V=W\times_{\mathcal Y}U\) is an algebraic space over \(P\times_SU\). Its map to the sheaf associated to \(W\) is representable, flat, locally of finite presentation and surjective. The flat sheaf bootstrap makes \(W\) an algebraic space. Finally \(W\to\mathcal H_d(U/\mathcal Y)\) is representable smooth and surjective, as the base change of \(P\). The smooth stack recognition of Lesson 5 proves algebraicity. \(\square\)

This proves the inputs [Stacks, Tags 05XW, 05YH and 06CI] without presupposing the flat stack theorem.

### 6.3. Why complete intersections give smooth coordinates

In (6.2), the pair \((f,\alpha)\) is a map
\(Z\to U_y=U\times_{\mathcal Y}T\).
Let \(\mathcal H_{d,\mathrm{lci}}(U/\mathcal Y)\) be the subcategory where this map is unramified and a local complete intersection.

This is an open substack. To check it over a family, use étale scheme charts. Unramifiedness is the vanishing condition for the finite module of relative differentials, and the complete-intersection locus in a flat finitely presented family is open and commutes with base change. The scheme versions follow from finite presentations and the regular-sequence criterion; their algebraic-space formulations are [Stacks, Tags 05X8 and 06CE]. Since \(Z\to T\) is finite, the image of the bad locus is closed in \(T\). Its complement represents exactly the indicated subfunctor. Thus the inclusion is a representable open immersion, including arbitrary base changes.

**Lemma 6.4 (lifting the finite slice).** Let \(T\subset T'\) be an affine square-zero thickening. Let \(X'\to T'\) be flat and locally of finite presentation, put \(X=X'\times_{T'}T\), and let \(Z\to X\) be unramified lci with \(Z\to T\) finite locally free of degree \(d\). Then it extends to \(Z'\to X'\), with \(Z'\to T'\) finite locally free of the same degree and \(Z=Z'\times_{T'}T\).

**Proof.** If \(I\) is the ideal of \(T\) in \(T'\), flatness and the regular-immersion conormal calculation give

\[
0\longrightarrow I\otimes_{\mathcal O_T}\mathcal O_Z
\longrightarrow\mathcal C_{Z/X'}
\longrightarrow\mathcal C_{Z/X}
\longrightarrow0.
\tag{6.4}
\]

The last module is finite locally free because \(Z\to X\) is unramified lci. The scheme conormal statements, transported by étale charts, are [Stacks, Tags 06CB and 06CC]. Since \(Z\) is affine, (6.4) splits.

Construct the universal first-order neighbourhood of \(Z\) over \(X'\). Étale locally an unramified map is a closed immersion into an étale neighbourhood, and this neighbourhood is cut out by the square of its ideal. Uniqueness of infinitesimal lifts between the étale neighbourhoods glues these constructions. Its square-zero ideal on \(Z\) is \(\mathcal C_{Z/X'}\). Quotient this ideal by the chosen summand \(\mathcal C_{Z/X}\). The resulting neighbourhood \(Z'\) has ideal
\(I\otimes\mathcal O_Z\) and a map to \(X'\).

The natural multiplication map identifies its ideal with the image of \(I\), so the square-zero flatness criterion gives flatness of \(Z'\to T'\) and the stated base-change identity. A nilpotent thickening of an affine scheme is affine. Lift finitely many module generators for the finite algebra of \(Z/T\); they generate the algebra of \(Z'/T'\), since the cokernel equals \(I\) times itself and \(I^2=0\). Thus \(Z'\to T'\) is finite. Locally lift a basis of its reduction of rank \(d\). The resulting map from the free module of rank \(d\) is surjective by the same argument. Flatness makes its kernel remain exact after reduction modulo \(I\), so that kernel is equal to \(I\) times itself and is zero. The algebra is therefore finite locally free of rank \(d\). The open lci condition above ensures that its map to \(X'\) still belongs to the indicated substack. \(\square\)

This is the independently established lifting argument of [Stacks, Tag 06D8]. It also proves that
\(\mathcal H_{d,\mathrm{lci}}(U/\mathcal Y)\to\mathcal Y\)
is formally smooth on objects: apply the lemma to \(U_{y'}\to T'\) for a lift \(y'\) of the base object.

These morphisms are limit preserving on objects. A finite locally free algebra, its map into the fixed locally finitely presented algebraic space \(U_y\), and its finitely many compatibility data descend along affine limits. The finite source uses only finitely many charts; the coefficient construction in Lemma 6.1 then involves finite presentations. The open unramified lci condition descends after increasing the stage. This is the finite presentation argument of [Stacks, Tag 06CH].

Their union over \(d\geq1\) is surjective on field objects. Indeed \(U_y\) is a nonempty algebraic space locally of finite presentation over a field \(k\). Take an affine étale chart and a closed point in its Cohen–Macaulay locus, which is nonempty on a finite type scheme. A system of parameters in the Cohen–Macaulay local ring is a regular sequence. After shrinking the chart, its zero scheme is supported only at that point and is finite over \(k\). Call it \(Z\). The regular immersion followed by the étale map is unramified lci; \(Z\) is a nonzero finite \(k\)-algebra, so it is finite locally free of some degree \(d\). It gives an object (6.2). The scheme inputs are [Stacks, Tags 045U and 0570]; they impose no perfection assumption on \(k\).

**Theorem 6.5 (flat stack bootstrap).** If \(q:U\to\mathcal Y\) is a representable surjective flat locally finitely presented morphism from an algebraic space to an fppf stack, then \(\mathcal Y\) is an algebraic stack.

**Proof.** Lemma 6.3 gives its representable diagonal and the algebraic stacks \(\mathcal H_d(U/\mathcal Y)\). Their lci opens are algebraic too. Choose smooth scheme atlases for these opens, and take their union \(P\).

The map \(P\to\mathcal Y\) is representable because \(\mathcal Y\) has representable diagonal. It is limit preserving on objects and formally smooth on objects: both properties compose, using the lifted identifying arrows in their definitions, and the atlases are smooth. For a representable morphism these two properties mean locally finite presentation and formal smoothness respectively. Test the definitions on \(P\times_{\mathcal Y}T\); its objects are actual morphisms to that algebraic space, so the limit and infinitesimal criteria apply. The infinitesimal criterion for a finitely presented morphism makes \(P\to\mathcal Y\) smooth.

The finite slices above cover every field object, allowing field extensions to lift to \(P\). This is surjectivity for a representable morphism. Thus \(P\to\mathcal Y\) is a smooth surjective scheme atlas. Lesson 5's recognition theorem proves the conclusion. \(\square\)

This proves [Stacks, Tag 06DC]. The uses of limits, formal smoothness and field-surjectivity are the precise notions of [Stacks, Tags 06CT, 06CZ and 06D4].

**Theorem 6.6 (flat groupoids are algebraic).** For any groupoid \(R\rightrightarrows U\) in algebraic spaces over \(S\), if both projections are flat and locally of finite presentation, then \([U/R]\) is an algebraic stack.

**Proof.** Lesson 5's diagonal calculation represents the Isom sheaves of the quotient: they are locally the pullbacks of the endpoint map \(R\to U\times_SU\), and the flat sheaf bootstrap descends them. In particular \(U\to[U/R]\) is representable.

On an fppf local chart \(a:T\to U\) of a quotient object, its pullback is \(R\times_{s,U,a}T\to T\). This is flat and locally of finite presentation by base change, and is surjective because the identity gives a section. These properties descend fppf locally. Theorem 6.5 therefore applies to \(U\to[U/R]\). \(\square\)

*Reference:* [Stacks, Tags 06FG and 06FI]. This completes the flat-groupoid theorem used as a stated forward reference in [Quotient stacks and Deligne–Mumford stacks](quotient-and-dm-stacks.md), including examples such as \(B\mu_p\).

For orientation, call a map of stacks **algebraic** when all its scheme-base fibres are algebraic stacks [Stacks, Tag 05XX]. If the target is algebraic, an algebraic map has algebraic source: pull back an atlas and then take an atlas of that fibre. A map from an algebraic stack to a stack with representable diagonal is algebraic for the same reason, using a source atlas. Finally an algebraic map with target having representable diagonal gives representable source diagonal: over each target Isom space, the source Isom fibre is the Isom space of the corresponding algebraic fibre stack. These atlas and Isom calculations prove the three permanence statements without changing the meaning of “representable”.

## 7. A complete example and a failure of effectiveness

### 7.1. Line bundles on a proper flat curve

Let \(C\to S\) be proper, flat and of finite presentation, with fibres of dimension at most one. Let \(S\) be locally Noetherian with the G-ring condition of Theorem 4.2. Define
\(\mathcal{Pic}_{C/S}(T)\)
to be the groupoid of invertible sheaves on \(C_T\), with all their isomorphisms. This is the Picard **stack**; we do not divide out line bundles pulled back from \(T\).

We will use two precise scheme results. For a proper flat finitely presented scheme and a finitely presented sheaf flat over the base, its derived direct image is perfect and commutes with arbitrary base change [Stacks, Tag 0B91]. For a proper scheme over a complete Noetherian ring, completion gives an equivalence between coherent sheaves and compatible systems of coherent sheaves on its infinitesimal neighbourhoods [Stacks, Tag 088C; EGA III, Theorem 5.1.5]. The latter includes morphisms.

For a line bundle \(N\) on \(C_A\), the first result and the dimension bound give

\[
R\Gamma(C_A,N)\simeq[P^0\longrightarrow P^1]
\tag{7.1}
\]

with \(P^i\) finite projective \(A\)-modules. To justify the two-term range, its derived fibres have cohomology only in degrees \(0,1\), by coherent cohomology on proper schemes of dimension at most one. A bounded finite-projective representative can then be shortened: cancel the split surjections at its highest excessive degrees and the split injections at its lowest excessive degrees. Fibrewise exactness and Nakayama make these cancellations valid on the base. On an affine base they give (7.1); the construction also shows the asserted Tor amplitude. Thus (7.1) computes base change to every \(A\)-algebra and tensoring with every \(A\)-module.

**[−1].** A finite affine cover of \(C_k\), finite presentations of line bundles on that cover, and matrices describing their transitions give a uniform cardinal bound for their isomorphism classes and arrows as \(k\) ranges over finite type fields over \(S\). The cardinal can be enlarged once to contain the affine base presentations and the field models. This supplies the site-size condition.

**[0].** Invertible sheaves and their isomorphisms have effective fpqc descent, by descent of quasi-coherent modules followed by the local rank-one condition. In particular this is an étale stack.

**[1].** A line bundle on \(C_A\), with \(A=\operatorname{colim}A_i\), is of finite presentation. Finite affine covers, its local presentations and the finitely many transition maps descend to a stage. Their inverse identities and the rank-one condition hold after increasing the stage. The same finite-presentation argument descends isomorphisms and tests equality of isomorphisms. Thus the full groupoids preserve limits.

**[2].** Flatness of \(C/S\) makes the structure rings of its affine charts preserve the fibre product (1.1) under base change. Finite projective modules patch over that fibre product, as proved in Exercise 8.2 below. Apply this to the locally free rank-one modules on the charts. Full faithfulness patches their transition maps and checks the cocycle, so the patched sheaf is invertible. This proves (RS), and the same argument with arbitrary square-zero extensions proves (RS\(^*\)).

**[3].** The transition-function calculation gives

\[
T_L\mathcal{Pic}_{C/S}=H^1(C_k,\mathcal O_{C_k}),\qquad
\operatorname{Inf}_L\mathcal{Pic}_{C/S}
=H^0(C_k,\mathcal O_{C_k}).
\tag{7.2}
\]

Indeed, write a first-order change of transition units as
\(g_{ij}(1+\epsilon a_{ij})\). The cocycle equation is the additive Čech cocycle equation for \(a_{ij}\); changing frames adds a coboundary. An automorphism reducing to the identity is \(1+\epsilon a\) with a global section \(a\). The spaces are finite dimensional by proper coherent cohomology.

**[4].** For a complete Noetherian local ring \(R\), apply Grothendieck existence to \(C_R\) and a compatible system \(L_n\). It gives a coherent \(L\), including all compatible morphisms. It is invertible near the closed fibre: completing the local stalk along the base ideal gives a free module of rank one, and the local adic criterion, or faithful flatness of completion after localization at the point, gives local freeness there. The non-invertible locus is closed. Its image in \(\operatorname{Spec}R\) is closed by properness and misses the closed point. A nonempty closed subset of a local spectrum contains that point, so the locus is empty. Thus \(L\) is invertible everywhere. Full faithfulness algebraizes isomorphisms and their inverses, proving (2.2).

**[5] for the stack.** For \(L\in\mathcal{Pic}_{C/S}(A)\) and an \(A\)-module \(M\), the same Čech calculation gives
\[
T_L(M)=H^1(C_A,p^*M),\qquad
\operatorname{Inf}_L(M)=H^0(C_A,p^*M).
\tag{7.3}
\]
The obstruction to lifting \(L\) across \(A'\to A\) lies in \(H^2(C_A,p^*I)\): lift local frames and transition units; their failure to satisfy the cocycle is a Čech 2-cocycle, and changing the transitions changes it by a coboundary. Its vanishing is precisely the ability to glue a lift. Formula (7.1) for \(\mathcal O_C\) shows that this \(H^2\) is zero for every \(I\). Thus zero obstruction modules give a functorial obstruction theory.

Furthermore \(H^1(C_A,p^*M)=\operatorname{coker}(P^0\otimes_AM\to P^1\otimes_AM)\). Finite projective modules commute with products under tensoring, and products of module sequences are exact. Hence \(T_L\) commutes with countable products, and the zero obstruction functor has the required injectivity. Theorem 5.3 proves openness.

**[5] for the diagonal, and the second diagonal.** For two line bundles \(L_1,L_2\), put \(N=L_1^\vee\otimes L_2\). Their Hom functor is the affine scheme of vectors in \(P^0\) annihilated by the differential in (7.1). The universal vector gives a section of \(N\). It is an isomorphism exactly where its zero locus in the proper curve has empty image in the parameter scheme. That condition is open, so \(\operatorname{Isom}(L_1,L_2)\) is a scheme locally of finite presentation over the base.

Its diagonal is representable, hence the stack's second diagonal is representable. Openness of versality for these Isom schemes follows from the ordinary Artinian smoothness criterion and the open smooth locus, using étale scheme charts if necessary. This checks the other part of [5].

All the axioms, including their arrow conditions, have now been verified. Theorem 4.2 proves that \(\mathcal{Pic}_{C/S}\) is an algebraic stack. The proof did not replace this stack by its sheaf of isomorphism classes.

### 7.2. The affine line loses a formal automorphism

Let \(R\) be a complete discrete valuation ring with uniformizer \(t\). On \(\mathbf A^1_R\), the trivial line bundle has automorphism group \(R[x]^\times=R^\times\): \(R\) is a domain, so a unit polynomial has degree zero.

Over \(R/t^n\), however, \(1+tx\) is a unit, with inverse

\[
(1+tx)^{-1}=\sum_{j=0}^{n-1}(-tx)^j.
\tag{7.4}
\]

The units and their inverses form compatible systems. They give an automorphism of the formal trivial line bundle in
\(\lim_n\mathcal{Pic}_{\mathbf A^1/R}(R/t^n)\).
The corresponding element \(1+tx\) in
\(\lim_n(R/t^n)[x]\)
is not the image of a unit of \(R[x]\), since that image would be constant. Thus completion is not full on automorphisms, even though the formal object under discussion is already the completion of a trivial line bundle. Axiom [4] fails. This is exactly the groupoid distinction needed in (2.2).

## 8. Exercises and complete solutions

**Exercise 8.1 (medium: limits of algebraic stacks).** Show that an algebraic stack locally of finite presentation over \(S\) is limit preserving. Do not assume quasi-compactness or quasi-separatedness.

**Solution.** Choose a smooth atlas \(U\to\mathcal X\) with \(U\) locally of finite presentation over \(S\). Then \(R=U\times_{\mathcal X}U\) is smooth over \(U\), hence locally of finite presentation over \(S\). The morphism \(R\to U\times_SU\) is locally of finite presentation by the finite-presentation permanence rule on charts. Descent along the atlas therefore shows that the diagonal of \(\mathcal X\) is locally of finite presentation.

For descended objects over \(T_i\), their Isom space is locally of finite presentation over \(T_i\); its affine limit criterion gives descent and eventual equality of all arrows. This proves full faithfulness in (2.1).

For essential surjectivity, pull the atlas back to an object over an affine \(T\). Choose an étale scheme chart of that smooth algebraic-space cover and finitely many affine opens whose images cover \(T\). Their disjoint union \(V\to T\) is a smooth surjection of finite presentation, with a map to \(U\) and descent arrows in \(R\). The affine schemes \(V\), \(V\times_TV\) and its triple product are of finite presentation over \(T\). Their finite equations descend to a sufficiently late \(T_i\), as do their maps to the locally finitely presented spaces \(U\) and \(R\). The finitely many identity and cocycle equalities descend after a further increase. Smoothness and surjectivity of the covering descend too. Effective fppf descent in the already algebraic stack produces the object over that \(T_i\). Its pullback is the original object. Only a finite portion of the atlas was used for this affine test, so no global compactness assumption was introduced.

**Exercise 8.2 (medium: module patching).** Verify (RS) for finite locally free modules, including the arrows.

**Solution.** For (1.1), the ring \(P\) is local, with residue field that of \(A_1\). A patched pair of finite free modules must have equal rank, since their restrictions to \(A\) are isomorphic. Choose bases. The gluing isomorphism is an invertible matrix \(g\) over \(A\). Lift its entries to \(A_2\); its determinant lifts a unit because \(\ker(A_2\to A)\) is nilpotent, so the lifted matrix is invertible. Change the second basis by that matrix. The gluing is now the identity, and the pair is the restriction of \(P^r\).

An arrow between two such pairs is a pair of matrices over \(A_1,A_2\) which agree over \(A\). Entrywise it is a unique matrix over \(P\). If the arrow is an isomorphism, its compatible inverse matrices patch as well. This proves full faithfulness and essential surjectivity. Markings at the residue field are preserved by doing the same construction with their specified identifications.

The general finite-projective version, used for (RS\(^*\)) in Section 7, is obtained by adding complements. Write the module over \(A_1\) as the image of an idempotent in \(A_1^n\). Lift its restriction to an idempotent in \(A_2^n\). Its image is isomorphic to the given second module with its specified reduction: maps between finite projectives lift across the nilpotent ideal, and maps inverse modulo that ideal are inverse after multiplying by an invertible correction. Add the two complementary summands. The enlarged pair is free on both sides, and its gluing matrix lifts as above. Its two projection idempotents, now equal over \(A\), patch to an idempotent over \(P\). Its image is the desired finite projective module. Equivalently that image is the fibre product of the original two modules. Maps patch entrywise in the free ambient modules and respect the idempotents. This proves the finite-projective Milnor patching lemma for arbitrary \(A_1\) and a square-zero surjection \(A_2\to A\), including all arrows.

**Exercise 8.3 (medium: vector-bundle tangents).** For a vector bundle \(E\) on a proper curve \(C/k\), prove
\[
T_E\mathcal{Bun}_C=\operatorname{Ext}^1_C(E,E)
=H^1(C,\mathcal E nd(E)).
\tag{8.1}
\]

**Solution.** On a finite affine trivializing cover, write its matrices as \(g_{ij}\). A first-order change has the form \(g_{ij}+\epsilon h_{ij}\). Linearizing the cocycle and the frame changes identifies its class with an additive Čech 1-cocycle in \(\mathcal E nd(E)\), modulo coboundaries. Since \(C\) is separated, affine intersections compute the cohomology of this quasi-coherent sheaf. This gives the last term of (8.1), and addition is exactly the split-extension addition of Section 1.

There is also an intrinsic description. A first-order bundle \(E'\) gives the extension
\[
0\to E\xrightarrow{\epsilon}E'\to E\to0
\]
as an \(\mathcal O_C\)-module; flatness over \(k[\epsilon]\) identifies the kernel with \(E\). Conversely, an extension gives the middle term an \(\epsilon\)-action by the composite of its quotient to \(E\) and its inclusion of \(E\). Locally the extension splits because \(E\) is locally free, and the resulting module is a free deformation over \(\mathcal O_C[\epsilon]\). Thus extensions and marked first-order bundles are equivalent on isomorphism classes. Their Baer addition matches the cocycle addition. Finally \(\mathcal H om(E,-)\) is exact locally, so global derived Hom from \(E\) is cohomology of \(E^\vee\otimes-\). This identifies \(\operatorname{Ext}^1(E,E)\) with \(H^1(\mathcal E nd(E))\). Infinitesimal automorphisms, for comparison, are \(H^0(\mathcal E nd(E))\).

**Exercise 8.4 (hard: the formal Picard groupoid).** For a smooth proper curve \(C/k\), verify [3] and [4] for its line-bundle stack.

**Solution.** Formula (7.2) gives the tangent and infinitesimal automorphism spaces at any line bundle after every finite field extension. Proper coherent cohomology makes \(H^0\) and \(H^1\) finite dimensional, proving [3]. No assumption that automorphisms vanish is made.

Given a complete Noetherian local \(k\)-algebra \(R\), Grothendieck existence on the proper scheme \(C_R\) algebraizes every compatible system of line bundles to a coherent sheaf. The completed local modules along the closed fibre are free of rank one, so the sheaf is invertible near that fibre. Its closed non-invertible locus has proper closed image in \(\operatorname{Spec}R\); such an image cannot be nonempty while missing the closed point. The sheaf is therefore a line bundle on all of \(C_R\). Full faithfulness of existence algebraizes every compatible isomorphism. Applying it also to the inverse and using faithfulness proves that the algebraized map is an isomorphism. Consequently completion is an equivalence of groupoids, not merely a surjection on objects. This proves [4], and explains precisely where properness excludes the phenomenon in (7.4).

## Appendix A. Artin–Rees perturbation and graded quotients

The approximation in Lemma 2.3 preserves an entire finite relation complex. We prove the two perturbation facts that make its associated graded conclusion valid, with their exact congruence order.

### A.1. The perturbation theorem

Let \(A\) be Noetherian and let \(I\subset\operatorname{Jac}(A)\). For a map \(q\colon M\to N\) of finite modules, say that \(c\geq0\) is an **Artin–Rees constant for \(q\)** when
\[
 q(M)\cap I^nN\subset q(I^{n-c}M)\qquad(n\geq c).
\]
Artin–Rees applied to the finite submodule \(q(M)\subset N\) gives such a constant. We may enlarge a constant, so two given maps admit one common constant.

**Lemma A.1.** Suppose
\[
 L\xrightarrow f M\xrightarrow g N,
 \qquad L\xrightarrow{f'}M\xrightarrow{g'}N
\]
are complexes of finite \(A\)-modules, the first is exact at \(M\), and \(c\) is an Artin–Rees constant for both \(f\) and \(g\). Assume
\[
 (f-f')(L)\subset I^{c+1}M,
 \qquad(g-g')(M)\subset I^{c+1}N.
\tag{AR.1}
\]
Then the second complex is exact at \(M\), and the same \(c\) is an Artin–Rees constant for \(g'\).

**Proof.** Fix \(n\geq c\) and \(a\in M\) such that \(g'(a)\in I^nN\). We show that we can subtract elements of \(f'(L)\) until the remaining element lies in \(I^{n-c}M\). Such subtractions do not change \(g'(a)\), because the perturbed sequence is a complex.

Suppose at an intermediate step that \(a\in I^rM\), with \(0\leq r<n-c\). Equation (AR.1) gives
\[
 g(a)=g'(a)+(g-g')(a)
 \in I^nN+I^{r+c+1}N=I^{r+c+1}N.
\]
Artin–Rees for \(g\) supplies \(a_1\in I^{r+1}M\) with \(g(a_1)=g(a)\). Exactness of the first sequence supplies \(b\in L\) with \(a-a_1=f(b)\). If \(r\geq c\), Artin–Rees for \(f\) permits choosing \(b\in I^{r-c}L\), since \(f(b)\in I^rM\). If \(r<c\), keep any such \(b\).

In either case
\[
 a=f'(b)+a_2,
 \qquad a_2=a_1+(f-f')(b)\in I^{r+1}M.
\]
Indeed, for \(r\geq c\) the error is in \(I^{c+1}I^{r-c}M=I^{r+1}M\); for \(r<c\) it is in \(I^{c+1}M\subset I^{r+1}M\). Replace \(a\) by \(a_2\). The order rises by one while \(g'(a)\) remains fixed. After finitely many steps we obtain
\[
 (g')^{-1}(I^nN)\subset f'(L)+I^{n-c}M.
\tag{AR.2}
\]
Applying \(g'\) proves \(g'(M)\cap I^nN\subset g'(I^{n-c}M)\), including the case \(n=c\), when no adjustment was needed.

If \(g'(a)=0\), (AR.2) holds for every \(n\geq c\). Its class in the finite module \(M/f'(L)\) lies in every power of \(I\). The Krull-intersection theorem, with \(I\subset\operatorname{Jac}(A)\), makes that class zero. Hence \(\ker g'\subset\operatorname{im}f'\). The converse follows from \(g'f'=0\). No completeness of \(A\), freeness of the modules, or exactness at an endpoint has been used. \(\square\)

### A.2. Equality of the initial submodules

**Lemma A.2.** Under the preceding hypotheses put \(Q=N/g(M)\) and \(Q'=N/g'(M)\). The identity on \(\operatorname{gr}_I N\) induces a canonical isomorphism
\[
 \operatorname{gr}_I Q\simeq\operatorname{gr}_I Q'
\]
of graded \(\operatorname{gr}_I A\)-modules. If \(N=A\) and the two images are ideals, this is an isomorphism of graded algebras.

**Proof.** In degree \(n\geq0\) the quotient filtration gives
\[
 (\operatorname{gr}_I Q)_n
 =I^nN/\bigl(I^{n+1}N+(g(M)\cap I^nN)\bigr).
\tag{AR.3}
\]
We compare the two denominator submodules inside \(I^nN\). If \(n\leq c\), (AR.1) says that \(g(a)\) and \(g'(a)\) differ by an element of \(I^{n+1}N\). For \(g(a)\in I^nN\), its perturbed image is therefore also in \(I^nN\). This gives one containment of denominators.

If \(n>c\), write an element of \(g(M)\cap I^nN\) as \(g(a)\) with \(a\in I^{n-c}M\), using the constant for \(g\). Then
\[
 g(a)-g'(a)\in I^{c+1}I^{n-c}N=I^{n+1}N.
\]
Again \(g'(a)\in I^nN\), giving the containment. The perturbation lemma supplies the same constant for \(g'\), so exchanging \(g\) and \(g'\) proves the reverse containment in every degree. The quotients in (AR.3) are thus identical subquotients of \(\operatorname{gr}_I N\). Their identifications respect its graded module action. For ideals in \(A\), they respect multiplication as well, proving the algebra assertion. \(\square\)

### A.3. Flat base change of the constant

**Lemma A.3.** Let \(A\to B\) be flat, with both rings Noetherian. An Artin–Rees constant \(c\) for \(q\colon M\to N\) remains a constant for \(q_B\) relative to \(IB\).

**Proof.** For \(n\geq c\), the constant condition is equivalent to
\[
 q^{-1}(I^nN)\subset\ker q+I^{n-c}M.
\]
The left side is the kernel of \(M\to N/I^nN\). Flat tensor product preserves that kernel and the kernel of \(q\), and identifies the quotients and powers with their base changes. Tensor the displayed inclusion with \(B\), then apply \(q_B\); the desired containment follows. \(\square\)

### A.4. Use in family approximation

In Lemma 2.3 the relation presentation is a complex of finite free modules over the complete local presentation ring \(P\):
\[
 P^{\oplus t}\xrightarrow f P^{\oplus r}
 \xrightarrow{(b_1,\ldots,b_r)}P\longrightarrow R\longrightarrow0.
\]
The columns of \(f\) generate the syzygies of the ideal generators. Choose a common constant \(c\) for its two displayed maps, relative to the maximal ideal of \(P\). Polynomial approximation must preserve the equations saying that the new generators and new syzygies still form a complex, and must approximate all these coefficients to order at least \(c+1\). Its order must also be at least the requested \(N\).

The perturbation lemma gives exactness at \(P^{\oplus r}\). The graded quotient lemma identifies the two associated graded quotient **algebras**, rather than merely their Hilbert functions. The quotient filtration is the maximal-ideal filtration of the local quotient, so this is precisely the graded comparison asserted in (2.3). Completion of the approximating Noetherian local ring preserves its residue quotients and associated graded algebra; thus the comparison returns to that local ring. For a finite type ring and its localization at a maximal ideal, every quotient by a power of that maximal ideal is unchanged by localization, since each element outside the ideal is already a unit in the quotient. The comparison consequently survives the finite-stage descent of the approximating object.

This argument explains why approximating only the ideal generators is insufficient: the exact perturbed syzygy equations supply (AR.2), and (AR.2) supplies the Artin–Rees constant for the perturbed map needed for the reverse graded containment.

The mathematical source is the Stacks Project authors, *More on Algebra*, labels `lemma-approximate-complex` and `lemma-approximate-complex-graded` (Tags 07VE–07VF), and `lemma-works-flat-extension`, at AI Integrated Stacks Project revision `565b10e987aba5969b21145a0833f42d69f96790`. That section credits Conrad–de Jong for part of the material. This independently expressed proof is eligible CC0 programme writing; the consulted human source retains its attribution and GFDL terms.

## Prerequisites and proof scope

All four acceptance results—Artin's space and stack criteria, openness from naive obstruction theories, and algebraicity of flat groupoid quotients—have been proved above. The product-compatible obstruction criterion and the stronger-effectiveness criterion have also been proved. The imported inputs are:

- Schlessinger's existence theorem for a versal formal object in a predeformation category satisfying (S1), (S2), and finite-dimensional tangent space [Stacks, Tag 06IW], and its field-change, linearity and small-extension tests. These are the assigned formal-deformation prerequisites. The cotangent obstruction to lifting a ring map, the regular-immersion conormal calculation and square-zero flatness criterion are the assigned deformation prerequisites; the space versions are obtained on étale charts [Stacks, Tags 06CB, 06CC and 06BH].
- Appendix B supplies Popescu's desingularization, both polynomial-approximation forms and G-ring permanence [Stacks, Tags 07GC, 07QY, 07QZ and 07PV]. Section 2.3 and Appendix B §B.6.1 give the full marked-family construction. Appendix A proves the finite-complex Artin–Rees perturbation statements [Stacks, Tags 07VE and 07VF]. Lower predecessor references retain the exact written, partial or unbound states recorded in Appendix B.
- Appendix B includes the ordinary-scheme Artinian lifting-at-a-point chain used by the smoothness test [Stacks, Tag 02HX]. The remaining scheme prerequisites include étale lifting over henselian local rings, finite presentation descent along affine limits, scheme Zariski main and idempotent lifting from the earlier lessons. The openness criteria for unramified and lci families with flat finitely presented source and target, and the Cohen–Macaulay slicing inputs, have their precise space or scheme formulations in [Stacks, Tags 05X8, 06CE, 045U and 0570].
- The Noetherian topological statements in Section 5.1 [Stacks, Tags 0G2F and 0G2R]; coherent cohomology finiteness and the dimension bound; perfect direct image with arbitrary base change [Stacks, Tag 0B91]; and Grothendieck existence for proper schemes [Stacks, Tag 088C; the proper-support extension is Tag 088E]. Existence is used with all its morphisms. Its conversion from coherent sheaves to invertible sheaves was proved in Section 7.

The general pushout theorem for algebraic stacks along arbitrary affine thickenings [Stacks, Tag 07WM] is mentioned as a stronger statement. The Artinian assertion needed here was proved in Lemma 1.2. The general theorem's flat-space patching input is not developed in this lesson.

## References

- **[Stacks]** The Stacks project, *Artin's Axioms*: Tags 07T0, 07T2, 07WM, 06L9, 07WT, 07WW, 07WY, 07X3, 07XA, 07XK, 07XD, 07XP, 07XJ, 07XZ, 07Y0, 07Y1, 07Y3, 07Y4, 07Y5, 0CXN, 0CXR, 07Y6, 07YF, 07YG, 0CYF, 07YJ, 07YP, 07YT and 07YU. Read the chapter in [AI Integrated Stacks Project, Artin's Axioms](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/artin.html).
- **[Stacks]** *Criteria for Representability*: Tags 05XF, 05XH, 06CT, 06CZ, 06D4, 05XX, 06DB, 06DC, 06FG and 06FI, and the finite Hilbert and restriction-of-scalars constructions used in Section 6. See [AI Integrated Stacks Project, Criteria for Representability](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/criteria.html).
- **[Stacks]** *Smoothing Ring Maps*, Tags 07GC, 07QY and 07QZ; *More on Algebra*, Tags 07PV, 07VE and 07VF; *Formal Deformation Theory*, Tag 06IW; and the scheme-theory inputs listed above. See [AI Integrated Stacks Project, Smoothing Ring Maps](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/smoothing.html). AI Integrated Stacks Project retains the upstream tags; its additions and corrections are not reviewed by the Stacks project's maintainers.
- **[EGA]** A. Grothendieck, with J. Dieudonné, *Éléments de géométrie algébrique III*, Theorem 5.1.5, for the existence theorem invoked through its proper-scheme form in [Stacks, Tag 088C].

## Appendix B. Artin approximation and general Néron desingularization

Section and statement numbers within this appendix are local to the appendix; an explicit course or provider title qualifies every outside reference.

This foundation retains the full assertion needed in Lesson 7: a regular map between arbitrary Noetherian rings is a filtered colimit of smooth algebras; consequently every formal solution over a henselian Noetherian local G-ring can be approximated to every prescribed order. The positive-characteristic argument below includes inseparable residue fields. The version over a local G-ring without henselianity produces a pointed étale neighborhood with the same residue field.

The geometric idea is to replace a finite algebraic problem by a smooth one and then use smooth coordinates to impose an exact solution with a prescribed finite-order residue. The proof develops singularity ideals, lifting and desingularization before separating the two residue-field cases. Supporting commutative-algebra constructions and their precise prerequisites accompany that argument.

### B.1. Sources, authorship and proof status

The incorporated proofs adapt the Stacks Project Authors' *Smoothing Ring Maps* chapter, the marked family-approximation proof from *Artin's Axioms*, and the specified predecessor proofs from *More on Algebra* and *Commutative Algebra*, as distributed by [AI Integrated Stacks Project](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/tree/565b10e987aba5969b21145a0833f42d69f96790). Popescu proved the main theorem; the Stacks exposition follows Richard Swan's treatment, which credits André's notes and Ogoma's arguments. This appendix reuses the Stacks exposition; it does not draw directly on the separately cited papers.

Human source credit: the Stacks Project Authors, with the source copyright notice Copyright (C) 2005–2025 Johan de Jong. AI source credit: the credited contributors to the pinned AI Integrated Stacks Project edition, to the extent their contributions occur in the retained material. Adaptation, dependency comparison and the explicit supplementary verifications here: OpenAI Codex, GPT-6.1 Sol, Ultra, 5 October 2026. These credits do not assert that an AI independently reviewed the unchanged human proof.

The incorporated and adapted human-source component is distributed under GNU FDL version 1.2 or later, with no Invariant Sections, no Front-Cover Texts and no Back-Cover Texts. The complete licence text accompanies this draft below. Independently written programme material retains the user's CC0 1.0 dedication; no AI rights holder is invented. The combined derivative preserves the human-source terms.

| Source ID | Native file at the pinned revision | SHA-256 |
| --- | --- | --- |
| AGAS-NATIVE-STACKS-565B-SMOOTHING | `smoothing.tex` | `85a37c95d5591632d11e7be6775039638b6f5200b44729abcea1a644d9f5b056` |
| AGAS-NATIVE-STACKS-565B-MORE-ALGEBRA | `more-algebra.tex` | `9b91629d8401d8f4fc439ef834cd69adc75e89b1ed59a75ba4fdd01daff52ad4` |
| AGAS-NATIVE-STACKS-565B-ALGEBRA | `algebra.tex` | `eb0db6ee32deab7b24e055a73cf2cc19904394e516a5b22567e7ef895a7b9cec` |

### B.2. The finite factorization criterion

All rings and maps in this chapter are commutative and unital. Smooth means finitely presented and formally smooth; the equivalent standard Jacobian presentations and flat-fibre characterization are predecessor results identified in §8. A regular map $R\to\Lambda$ is flat and has geometrically regular Noetherian fibres. A Noetherian algebra over a field is geometrically regular if it remains regular after every finite purely inseparable extension of that field. This does not mean that the residue fields at all its primes are separable over the base field.

**Lemma 2.1.** A ring map $R\to\Lambda$ is a filtered colimit of smooth $R$-algebras if and only if every $R$-algebra map $A\to\Lambda$ from a finitely presented $R$-algebra factors as $A\to B\to\Lambda$, with $B$ smooth over $R$.

**Proof.** A finitely presented algebra has finitely many generators and relations. A map from it into a filtered colimit descends to a stage: choose a common stage containing the finitely many images, and then a later common stage where all relations vanish. This proves one implication.

For the converse take the category of smooth $R$-algebras equipped with an $R$-algebra map to $\Lambda$, taking a set of representatives. It is nonempty, since $R$ is smooth over itself. Two objects map to a common object: their tensor product is finitely presented, maps to $\Lambda$, and hence factors through a smooth algebra by the hypothesis. Two parallel morphisms $u,v\colon B\rightrightarrows C$ become equal after a morphism to a smooth algebra: quotient $C$ by the differences $u(b_i)-v(b_i)$ for finitely many algebra generators of $B$; this quotient is finitely presented and maps to $\Lambda$, so apply the hypothesis. The category is therefore filtered.

Its colimit maps to $\Lambda$. Each $\lambda\in\Lambda$ occurs in a stage by applying the hypothesis to $R[T]\to\Lambda$, $T\mapsto\lambda$. If two stage elements have the same image, pass to a common stage $C$, quotient it by their difference, and apply the hypothesis again; they become equal in a later smooth stage. The map on colimits is bijective and is a ring homomorphism, so is an isomorphism. This proves the precise criterion, including its filteredness assertion. ∎

This supplies the categorical verification implicit in the native `algebra-lemma-when-colimit`. The proof uses no Popescu theorem.

### B.3. Popescu's theorem and the proof mechanism

**Theorem 3.1 (Popescu).** Every regular homomorphism $R\to\Lambda$ of Noetherian rings is a filtered colimit of smooth $R$-algebras.

The complete algebraic constructions establishing the theorem appear in §9, not merely its last paragraph. Their logical order is as follows.

For a finitely presented $R$-algebra $A$, write $H_{A/R}$ for the radical ideal defining its nonsmooth locus, and $\mathfrak h_A=\sqrt{H_{A/R}\Lambda}$ after a specified map $A\to\Lambda$. A resolution at a prime $\mathfrak q\supseteq\mathfrak h_A$ is a factorization $A\to B\to\Lambda$ with $B$ finitely presented, $\mathfrak h_A\subseteq\mathfrak h_B$, and $\mathfrak h_B\nsubseteq\mathfrak q$. Thus a resolution strictly increases the radical ideal. It does not require the target $\Lambda$ to be finitely presented.

The singular-ideal construction expresses its generators through minors of a Jacobian presentation and the relations among the equations. An improved presentation, obtained from the symmetric algebra of the conormal module, admits an algebra retraction and has free differentials wherever the original map is smooth. The comparison lemma then makes suitable powers of an element into strictly standard elements. These constructions are the input to the two principal algebraic steps.

First, flat nilpotent deformations of a filtered colimit of smooth algebras remain such colimits. In the square-zero case, a presentation is lifted and finitely many relations are killed using the equational criterion for flatness; the general nilpotent case follows by successive square-zero quotients. Second, the lifting and desingularization lemmas turn a smooth factorization modulo $\pi^8$ into a factorization whose smooth locus expands, assuming the stated annihilator equalities. The powers $\pi^8,\pi^4,\pi^2$ are retained in the actual constructions. Neither step is a simple-root Hensel argument.

These lemmas reduce the theorem to a geometrically regular Noetherian algebra over a field. To justify the reduction, assume failure and choose, among its failing quotient ideals, an ideal $I\subset R$ maximal under inclusion, such that the regular map $R/I\to\Lambda/I\Lambda$ fails the factorization property. Every quotient by a nonzero ideal now has the property. If the nilradical of this new $R$ were nonzero, it would be nilpotent because $R$ is Noetherian; nilpotent lifting and flatness would give the property for $R$, a contradiction. Thus $R$ is reduced. Its total ring of fractions is a finite product of fields, and the field theorem yields a smooth factorization there. Clearing finitely many denominators produces a strictly standard nonzerodivisor $\pi$ in a finite presentation. The property for $R/\pi^8R$, followed by lifting and desingularization, returns a smooth factorization over $R$. The target is flat over $R$, so a nonzerodivisor of $R$ remains a nonzerodivisor of $\Lambda$, giving the required annihilator equalities. This proves the transfer back from the field case to the original map.

Over a field $k$, choose a prime minimal over $\mathfrak h_A$. In characteristic zero the regular local target has a separable residue field, and the regular-parameter construction resolves it. In characteristic $p>0$, the inseparable proof constructs a finite polynomial subalgebra and a local Artinian approximation which captures the finitely many needed coefficients. The injective map $H_1(L_{K/k})\to\mathfrak m/\mathfrak m^2$, furnished by geometric regularity, gives the finite-dimensional condition needed for this construction even when $K/k$ is inseparable or infinitely generated. Ogoma's annihilator lemma makes the localized parameters usable before localization. The construction with auxiliary variables $t_i$ returns from these Artinian data to the original finitely presented algebra. Both complete proofs and their return maps are retained in §9.

Every resolution strictly increases $\mathfrak h_A$. The ascending-chain condition in the Noetherian target terminates this process at $\mathfrak h_B=\Lambda$. At that point choose $f_i\in H_{B/R}$ and $\lambda_i\in\Lambda$ with $\sum_i f_i\lambda_i=1$. The algebra

$$C=B[Z_1,\ldots,Z_r]/(\textstyle\sum_i f_iZ_i-1)$$

maps to $\Lambda$ by $Z_i\mapsto\lambda_i$ and is smooth over $R$. Indeed the opens $D(f_i)$ cover its spectrum, and $C_{f_i}$ is a polynomial algebra in the other $Z_j$ over the smooth algebra $B_{f_i}$. This establishes smoothness on a covering and hence smoothness of $C$. Lemma 2.1 now proves the theorem. The zero target gives the trivial smooth zero-algebra factorization; zero-dimensional local targets are covered explicitly in the supplementary verifications below. ∎

### B.4. Approximating a finite polynomial system

**Theorem 4.1.** Let $(R,\mathfrak m,k)$ be a henselian Noetherian local G-ring and $\widehat R=\varprojlim R/\mathfrak m^q$. Given polynomials $f_1,\ldots,f_s\in R[X_1,\ldots,X_n]$ and $a\in\widehat R^n$ with $f_j(a)=0$, for every integer $N\geq1$ there is $b\in R^n$ with $f_j(b)=0$ and $a_i-b_i\in\mathfrak m^N\widehat R$ for all $i$.

**Proof.** The G-ring hypothesis at the maximal ideal says precisely that $R\to\widehat R$ is regular; completion is Noetherian and flat by the actual completion provider. Choose $c_i\in R$ with $a_i-c_i\in\mathfrak m^N\widehat R$, and generators $d_1,\ldots,d_M$ of $\mathfrak m^N$. Write $a_i=c_i+\sum_\ell d_\ell a_{i\ell}$. Define the finite polynomial system

$$g_j(Y)=f_j\bigl(c_1+\sum_\ell d_\ell Y_{1\ell},\ldots,
c_n+\sum_\ell d_\ell Y_{n\ell}\bigr).$$

It has the formal solution $Y_{i\ell}=a_{i\ell}$. It therefore suffices to prove that every finite polynomial system with a solution in $\widehat R$ has a solution in $R$: any solution $y$ of the new system gives $b_i=c_i+\sum_\ell d_\ell y_{i\ell}$, with the prescribed congruences.

For that existence assertion, let $A\subseteq\widehat R$ be the $R$-subalgebra generated by the finitely many solution coordinates. Since $R$ is Noetherian it is finitely presented over $R$. Popescu's theorem and Lemma 2.1 give $A\to B\to\widehat R$ with $B$ smooth over $R$. Reducing the last map modulo the maximal ideal gives an $R$-algebra map $B\to k$.

The smooth-section lifting lemma supplies an étale $R$-algebra $R'$, an identification $R'/\mathfrak mR'=k$, and an $R$-algebra map $B\to R'$ reducing to that evaluation. Its complete proof is included in §10; it is the finite-projective-conormal and slicing argument, so makes no assumption that $B$ already has a single simple-root presentation. Henselianity, using the proved section criterion AG-CA, Theorem 1.2, gives an $R$-algebra section $R'\to R$. The coordinates' images under $A\to B\to R'\to R$ solve the polynomial system. Apply this assertion to the $g_j$ to obtain the required $b$. ∎

For order $N=0$, a solution given at order one also suffices. The assertion holds for every positive order; no uniform finite upper bound on the requested order is imposed.

### B.5. The pointed étale-neighborhood version

**Theorem 5.1.** Let $(R,\mathfrak m,k)$ be a Noetherian local G-ring, without a henselianity assumption. For the same $f_j$ and formal solution $a$, every $N\geq1$ admits an étale $R$-algebra $R'$, a maximal ideal $\mathfrak m'\subset R'$ over $\mathfrak m$ with specified residue isomorphism $\kappa(\mathfrak m')=k$, and a tuple $b\in(R')^n$ solving $f_j=0$. Under the corresponding local map $R'_{\mathfrak m'}\to\widehat R$, one has $a_i-b_i\in\mathfrak m^N\widehat R$. Equivalently, with the canonical pointed identification $\widehat{R'_{\mathfrak m'}}=\widehat R$, the differences lie in $(\mathfrak m')^N\widehat{R'_{\mathfrak m'}}$.

**Proof.** Make the same substitution $X_i=c_i+\sum_\ell d_\ell Y_{i\ell}$ as in Theorem 4.1. Factor the finitely presented algebra generated by the new formal coordinates through a smooth $B$. Lift the residue evaluation $B\to k$ to $B\to R'$, where $R\to R'$ is étale and $R'/\mathfrak mR'=k$. Define $b_i=c_i+\sum_\ell d_\ell y_{i\ell}$, where $y_{i\ell}$ are the images of the new coordinates in $R'$. Every $g_j(y)$ vanishes, hence $f_j(b)=0$.

Set $\mathfrak m'=\mathfrak mR'$. The quotient is $k$, so this is maximal with the asserted residue isomorphism. Since $\widehat R$ is complete local it is henselian. Its proved section criterion, applied to $R'\otimes_R\widehat R$ with the selected residue evaluation, gives the local $R$-algebra map $R'_{\mathfrak m'}\to\widehat R$. Each difference is a sum of the $d_\ell\in\mathfrak m^N$ times elements of $\widehat R$, proving the congruence.

For completeness, formal étaleness gives a unique compatible lift of the residue evaluation $R'\to k$ to $R'\to R/\mathfrak m^q$ for each $q$. The selected local branch is thereby identified modulo $\mathfrak m^q$ with $R/\mathfrak m^q$. One way to verify the identification is to pass to the Artinian base $R/\mathfrak m^q$: its selected local étale algebra is finite étale, since its field fibre is finite and the maximal ideal of the base is nilpotent. As a finite flat module over the local Artinian base it is free; its rank is the dimension of its residue algebra, namely one. Its unit generates it by Nakayama, so the structural map is an isomorphism. These identifications respect reduction maps by uniqueness. Taking limits gives $\widehat{R'_{\mathfrak m'}}=\widehat R$ and identifies $\mathfrak m'$ with $\mathfrak m$. This also follows from the same-residue-field pointed neighborhoods used in the written henselization construction AG-CA, §§4 and 6. ∎

**Corollary 5.2.** If $R$ is Noetherian, $\mathfrak p\subset R$ is a prime, and $R_{\mathfrak p}$ is a G-ring, a formal solution in $\widehat{R_{\mathfrak p}}$ can be approximated to any order in an étale $R$-algebra $R'$ at a prime $\mathfrak p'$ with $\kappa(\mathfrak p')=\kappa(\mathfrak p)$.

**Proof.** Apply Theorem 5.1 to $R_{\mathfrak p}$. The resulting étale algebra has a finite presentation and its étale equations and selected Jacobian inverses contain only finitely many coefficients from $R_{\mathfrak p}$. Clearing their denominators produces an étale algebra over some $R_s$, $s\notin\mathfrak p$, and hence an étale $R$-algebra. Clear also the finitely many denominators in the solution coordinates and the finitely many relations $f_j(b)=0$ by one further principal localization away from the selected prime. The localized ring at that prime is unchanged, so its completion, residue isomorphism and congruences are unchanged. This is the finite-presentation descent used in the native `lemma-approximation-property-variant`, whose full proof is retained below. ∎

### B.6. Approximation of finite algebraic data

#### B.6.1. A marked family and its associated graded algebra

**Theorem 6.1 (family approximation).** Let $S$ be locally Noetherian and let $\mathcal X\to(\mathrm{Sch}/S)_{fppf}$ be a category fibred in groupoids that is limit preserving on objects. Let $x\in\mathcal X(R)$, where $(R,\mathfrak m_R)$ is complete Noetherian local and its residue field $k$ is of finite type over $S$. Write $s$ for the image of its closed point, and assume $\mathcal O_{S,s}$ is a G-ring. For each $N\geq1$ there are a finite-type $S$-algebra $A$, a maximal ideal $\mathfrak m_A$, an object $x_A\in\mathcal X(A)$, and

$$R/\mathfrak m_R^N\simeq A/\mathfrak m_A^N,$$

as $S$-algebras, together with a specified isomorphism of the restricted objects and an isomorphism

$$\operatorname{gr}_{\mathfrak m_R}R\simeq\operatorname{gr}_{\mathfrak m_A}A$$

of graded $k$-algebras. Neither a perfect residue field nor characteristic zero is assumed.

**Proof.** Choose an affine open $\operatorname{Spec}\Lambda\subset S$ containing $s$. The map from the local scheme $\operatorname{Spec}R$ factors through it: its inverse image is an open containing the closed point of a local spectrum, hence the entire spectrum. The finite-type hypothesis on the residue field says that $k$ is a finitely generated $\Lambda$-algebra on this chart. Since $S$ is locally Noetherian, $\Lambda$ is Noetherian.

Write $R$ as the filtered colimit of its finite-type $\Lambda$-subalgebras. Limit preservation on objects gives a finite-type algebra $C$, a map $C\to R$, and an object $x_C$, with a chosen isomorphism $x_C|_R\simeq x$. No descent assertion about all arrows of $\mathcal X$ is being assumed. Choose a finite presentation

$$C=\Lambda[y_1,\ldots,y_u]/(f_1,\ldots,f_v),$$

and write $\bar a_i\in R$ for the images of its generators.

Choose finitely many generators of $k$ as a $\Lambda$-algebra and lift them to $R$. Add lifts of a finite generating set of $\mathfrak m_R$. These choices define a polynomial ring $T=\Lambda[z_1,\ldots,z_e]$ and a map $T\to R$ whose reduction to $k$ is surjective and whose image contains generators of $\mathfrak m_R$. Thus $\mathfrak n=\ker(T\to k)$ is maximal. Elements outside $\mathfrak n$ map to units of $R$, so the map extends to the local ring $Q=T_{\mathfrak n}$ and then continuously to

$$P=\widehat Q\longrightarrow R.$$

Here is a direct proof of its surjectivity. The chosen elements generate $\mathfrak m_R^j/\mathfrak m_R^{j+1}$ by their degree-$j$ monomials with coefficients in $k$. Those coefficients lift through $Q\to k$. Starting with any element of $R$, lift its residue and then its successive errors by such monomials. At the $j$th correction the added element lies in $\mathfrak m_Q^j$. The partial lifts are Cauchy in $Q$, hence define an element of $P$, and their images converge to the prescribed element of the complete ring $R$. This proves surjectivity; it also proves the usual surjective-cotangent-space criterion in this instance.

The complete ring $P$ is Noetherian. Choose generators $b_1,\ldots,b_r$ of the kernel, and lifts $a_i\in P$ of the $\bar a_i$. Choose coefficients $c_{ji}$ such that

$$f_j(a_1,\ldots,a_u)=\sum_{i=1}^r c_{ji}b_i.$$

The syzygy module of $(b_1,\ldots,b_r)$ is finite. Choose generators $k_\ell=(k_{\ell1},\ldots,k_{\ell r})$, giving an exact presentation

$$P^{\oplus t}\xrightarrow K P^{\oplus r}
 \xrightarrow{(b_1,\ldots,b_r)}P\longrightarrow R\longrightarrow0.$$

The map $K$ sends the $\ell$th basis vector to $k_\ell$; in particular $\sum_i k_{\ell i}b_i=0$.

Let $c$ be one Artin–Rees constant for both displayed maps relative to $\mathfrak m_P$, and choose $M\geq\max(N,c+1)$. The common constant exists by Artin–Rees for finite modules, and increasing a constant preserves its defining inclusions. The finite-complex perturbation and canonical graded-quotient statements are the written [Lesson 7, Appendix A, Lemmas A.1–A.2](artin-axioms.md#appendix-a-artin-rees-perturbation-and-graded-quotients). We use their full statements here and do not reproduce their proof.

Put $\mathfrak p=\mathfrak n\cap\Lambda$. The hypothesis says that $\Lambda_{\mathfrak p}$ is a G-ring. The permanence theorem proved below makes its essentially finite-type algebra $Q$ a G-ring. Apply the pointed étale-neighbourhood approximation theorem of Section 5 simultaneously to the following finite polynomial system:

$$f_j(A_1,\ldots,A_u)=\sum_i C_{ji}B_i,
 \qquad \sum_i K_{\ell i}B_i=0.$$

The tuple $(a_i,b_i,c_{ji},k_{\ell i})$ is an exact formal solution in $P$. We obtain an étale $Q$-algebra $B$, a maximal ideal $\mathfrak q$ above $\mathfrak n$ with residue field exactly $k$, and a solution $(a'_i,b'_i,c'_{ji},k'_{\ell i})$ whose entries differ from the old ones by $\mathfrak m_P^M$. The induced identification $\widehat{B_{\mathfrak q}}=P$ preserves the map from $Q$, its residue field and every finite-order quotient. There is no need to inject the entire possibly disconnected algebra $B$ into $P$.

Because $b_i$ lies in $\mathfrak m_P$ and $M\geq1$, each $b'_i$ lies in $\mathfrak q$. Set

$$A^*=B/(b'_1,\ldots,b'_r),\qquad
 \mathfrak m^*=\mathfrak q/(b'_1,\ldots,b'_r).$$

The exact polynomial relations define $C\to A^*$ by $y_i\mapsto a'_i$, so they give $x^*=x_C|_{A^*}$. Completion of a quotient of a Noetherian local ring gives

$$\widehat{(A^*)_{\mathfrak m^*}}=P/(b'_1,\ldots,b'_r).$$

This uses exactness of Noetherian completion for finite modules, supplied by the written completion prerequisite. As $b'_i-b_i\in\mathfrak m_P^M$, the ideals generated by the two lists become identical after adding $\mathfrak m_P^M$. Consequently

$$A^*/(\mathfrak m^*)^M
 \simeq P/((b'_1,\ldots,b'_r)+\mathfrak m_P^M)
 =P/((b_1,\ldots,b_r)+\mathfrak m_P^M)
 \simeq R/\mathfrak m_R^M.$$

Localization at the selected maximal ideal does not change these quotients: every element outside that ideal is already a unit modulo any of its powers. The two maps from $C$ to the displayed common quotient agree, because $a'_i-a_i\in\mathfrak m_P^M$. Restricting the chosen $x_C|_R\simeq x$ therefore gives the required marked comparison of objects at order $M$, hence at order $N$.

The matrix $K'$ and row $(b'_i)$ still form a complex, since all the syzygy equations were preserved exactly. Their entries differ from those of the original exact presentation by $\mathfrak m_P^M\subset\mathfrak m_P^{c+1}$. Lesson 7, Lemma A.2 now identifies the initial ideals inside $\operatorname{gr}_{\mathfrak m_P}P$. Its canonical identity on that graded algebra yields

$$\operatorname{gr}_{\mathfrak m_R}R
 \simeq\operatorname{gr}_{\mathfrak m_P}
     \bigl(P/(b'_1,\ldots,b'_r)\bigr).$$

This is an isomorphism of graded algebras. The quotient filtration is the maximal-ideal filtration, so completion identifies its right side with $\operatorname{gr}_{\mathfrak m^*}A^*$. This explains why the entire relation complex was approximated: approximating only the ideal generators would not provide the reverse initial-ideal containment.

It remains to obtain a finite-type algebra over the original affine chart. The algebra $A^*$ is of finite presentation over $Q=T_{\mathfrak n}$. Its finitely many generators, relations and denominators descend to a finite-type $T$-algebra $A_0$ with

$$A^*=(A_0)_{T\setminus\mathfrak n}
      =\operatorname{colim}_{f\in T\setminus\mathfrak n}(A_0)_f.$$

Products of denominators direct this system. Limit preservation on objects descends $x^*$ to an object $x_A$ at some stage $A=(A_0)_f$, with a specified isomorphism after base change to $A^*$. This algebra is finite type over $\Lambda$ and hence over $S$. Let $\mathfrak m_A$ be the inverse image of $\mathfrak m^*$. The image of $A\to k$ contains the image of $T$, which already surjects onto $k$ by the original residue-field generators. Thus $A/\mathfrak m_A=k$: the selected prime is maximal and has exactly the prescribed residue field.

Since $A^*$ is a localization of $A$ away from elements outside the selected point,

$$A_{\mathfrak m_A}\simeq (A^*)_{\mathfrak m^*}.$$

Localization at a maximal ideal preserves every quotient by its powers and therefore its associated graded algebra. All the ring comparisons constructed above consequently descend to $A$. Restricting the specified isomorphism $x_A|_{A^*}\simeq x^*$ to their common finite-order quotient supplies the required marking on objects; no finite-stage descent of an arbitrary arrow was needed. This proves all assertions. $\square$

The mathematical source is the Stacks Project, [Tag 07XB](https://stacks.math.columbia.edu/tag/07XB). The complete argument above uses the independently written desingularization and G-ring proofs in this appendix, the pointed approximation result in B.5, and the exact graded comparison in Appendix A. In particular, the graded-algebra conclusion and finite-type return are both part of this proof.

### B.7. Jacobian, parameter and cotangent calculations

The following additions are made in the incorporated proof, at the stated native labels. Each concerns an actual inference used by the theorem.

1. `lemma-final-solve`: replace the omitted verification by the covering $D(f_i)$ and elimination of $Z_i$ given in §3 above.
2. `lemma-product`: if $\Lambda_i=\varinjlim B_{i,\alpha}$ with $B_{i,\alpha}$ smooth over $R_i$, use the product of the two filtered index categories. Then $\Lambda_1\times\Lambda_2=\varinjlim(B_{1,\alpha}\times B_{2,\beta})$; each product algebra is smooth over $R_1\times R_2$, since the source and target split into the two open-and-closed idempotent components and smoothness holds on both. All maps are product algebra maps. This proves the product assertion rather than assuming preservation of filteredness.
3. `lemma-desingularize-lifting-apply`: let $\eta\in\operatorname{Spec}\Lambda$ lie over a point where $\bar C$ is smooth. If $\pi\notin\eta$, the lifting lemma makes $D$ smooth over $R$ there. If $\pi\in\eta$, use the compatible factorization $\bar C/\pi^4\to D/\pi^4\to\Lambda/\pi^4$; the same lifting lemma again makes $D$ smooth at the relevant inverse-image prime. Thus the image of $H_{D/R}$ is not contained in $\eta$. The inclusion $H_{D/R}B\subset H_{B/R}$ implies the same for $H_{B/R}$. On $\operatorname{Spec}(\Lambda/\pi^8)$, the open defined by $H_{\bar C/(R/\pi^8)}$ is therefore contained in the open defined by $H_{B/R}$. Reversing closed complements is precisely the claimed radical ideal inclusion. Away from $\pi$, the construction is smooth everywhere. This supplies the native omitted verification.
4. `lemma-ogoma`: if $(s^n\pi)^2m=0$, then $\pi^2m$ vanishes after localization, so $m\in K'$. Since $s(K'/K)=0$, one has $s\pi m=0$, and hence $s^n\pi m=0$. The converse is immediate. This proves the assertion for every $n>0$.
5. `lemma-enlarge-solution-modulo`: choose a power $q=p^r$ at least the nilpotence order. For $u\in\mathfrak m_{\bar\Lambda}$, $(1+u)^{p^r}=1+u^{p^r}=1$. Merely saying that $q$ is divisible by $p$ does not prove the displayed identity. If $\alpha$ is algebraic over $F$, write its irreducible polynomial as $h(T^{p^r})$ with $h'\ne0$; then $\alpha^{p^r}$ is separable over $F$. This proves the field step formerly referenced to an external Fields section. Enlarge $r$ if needed and use the finite-étale lifting of the separable residue extension.
6. `lemma-resolve-general`: set $e=8c$, and choose

$$n\geq\max\{N+dc,\ d(e-1)+1\}.$$

   The native choice $n=N+dc$ alone does not imply its later inclusion $\mathfrak p^n\subseteq(\pi_1^e,\ldots,\pi_d^e)$. A regular system of parameters generates $\mathfrak p$ after localization, and every monomial of degree $d(e-1)+1$ has an exponent at least $e$. This proves the inclusion and, because $\mathfrak p\Lambda_{\mathfrak q}=\mathfrak q\Lambda_{\mathfrak q}$, the corresponding target inclusion. Increasing $n$ changes none of the earlier constructions: choose the Artinian approximation at this larger order, keep the same $N,c,e$, and use $\mathfrak q^n\subseteq\mathfrak q^{n-N}H_{A/k}\Lambda_{\mathfrak q}$. The source proof's fifth/sixth-step cross-references are also corrected to express the actual direction: solve modulo $\mathfrak p^n$, then quotient the solution by $J$ to solve modulo $J$.
7. In the induction choosing $\delta_i$, write $v_j=\pi_{t+1}^Nc_j+\pi_{t+1}^Nc'_j\in\Lambda_{\mathfrak q}$. Choose a common $s_0\notin\mathfrak q$ for their finitely many denominators, so $v_j=a_j'/s_0$. The equality $\pi_{t+1}^{2N}=\sum_j a_jv_j$ holds after localization; multiply by one further $u\notin\mathfrak q$ killing the error in $\Lambda$. Choose $s$ divisible by $us_0$, put $\mu_j=(s^{2N}/s_0)a'_j$, and obtain $(s\pi_{t+1})^{2N}=\sum_j a_j\mu_j$ in $\Lambda$. In $\bar\Lambda$, the coefficient $\mu_j$ has image $s^{2N}\pi_{t+1}^Nd_j$, which lies in $D'$ after adjoining the permitted power of $s$. The native text misses the factor $\pi_{t+1}^N$; membership, rather than equality with $s^{2N}d_j$, is what is needed. Multiplying $s$ by a further power preserves the equality after scaling all coefficients, so the enlargement lemma can enforce membership of $s$ itself.
8. At the passage from $R/JR$ to $(R/I)_{\mathfrak r}$, every $t_i$ becomes a unit, because its image $\delta_i\notin\mathfrak q$. Hence $I_{\mathfrak r}=JR_{\mathfrak r}$ and $I\Lambda_{\mathfrak q}=J\Lambda_{\mathfrak q}$. Localizing the solution over $(R/JR)_{\mathfrak p}$ at the remaining elements of $R\setminus\mathfrak r$ therefore gives a solution over $(R/I)_{\mathfrak r}$. The source and target maps are the specified polynomial-algebra maps; their localizations type-check.
9. In the final factorization, $\delta_i\in D'$ has nonzero residue because $D'\to\bar\Lambda$ is a flat local map, hence faithfully flat. It is a unit in the Artinian local ring $D'$. The formula $z_{ij}\mapsto\lambda_{ij}t_i^{2N}/\delta_i^{2N}$ is therefore defined. Its relations follow from $(\pi_i\delta_i)^{2N}=\sum_j a_j\lambda_{ij}$, and evaluation $t_i\mapsto\delta_i$ gives the original coefficients. This establishes both commutative triangles required by the last step.
10. If $d=0$, omit the empty parameter-lifting step (whose stated lemma assumes $r\geq1$). In the separable proof, the localized target is a field with separable extension over $k$, hence a filtered colimit of smooth algebras by the retained field lemma; the height-zero delocalization lemma then gives the resolution. In the inseparable proof, take $c=1$, use the Artinian approximation with no $\pi_i,t_i$, and retain the same localization/height-zero argument. The solution-modulo lemma supplies a factorization through an essentially smooth algebra at order $n\geq1$; its finitely presented source factors through a smooth stage. No positive-dimensional regular-parameter argument is invoked in this case.

11. In `more-algebra-lemma-symmetric-algebra-smooth`, the two-term presentation complex is $K\to A^{\oplus n}$, tensored with $C$, rather than $K\to M$. It splits because $M$ is projective; its cokernel is $M\otimes_A C$, exactly as the displayed conormal computation says. The derivative corrects this typed-complex typo and the adjacent $R/I$ typo in the projective-lifting lemma.
12. The omitted verification in composition of regular maps is supplied in the retained derivative: localize and quotient at a source prime, then make a finite purely inseparable extension of its residue field. Both resulting intermediate and target rings are Noetherian by the regular-map fibre hypotheses, and the intermediate ring is regular. The base-changed second map has regular fibres. A flat map of Noetherian rings with regular source and regular fibres has regular target, by its exact local regularity predecessor. This verifies every geometric fibre of the composite; composition of flat maps verifies its flatness.

The exponent correction repairs this proof; it is not a counterexample to Popescu's theorem. The native source bodies remain unchanged, and these changes are confined to the incorporated derivative.

### B.8. Commutative-algebra prerequisites

We use the following written commutative-algebra proofs at their matched scope. The lesson title and source file identify the provider independently of the course's current numbering. Each provider retains its own prerequisites; the exact file bytes and theorem correspondence are recorded in the conversion manifest.

| Written programme proof | Matched mathematical claims |
| --- | --- |
| Completion, Theorems 3.1–3.3, 4.1 and 5.1 | Complete rings, formal power series and tensor products and direct sums; Complete rings, formal power series and flatness; Henselian rings and complete rings and formal power series |
| Coefficient rings and the Cohen structure theorem, Theorem 6.1 and its Noetherianity consequence | Complete rings, formal power series and Noetherian rings |
| Henselian local rings and henselization, Sections 4 and 6, Proposition 6.1 | Henselian rings; Henselian rings; Henselian rings and proper morphisms |
| Formally smooth, unramified and étale ring maps, Theorem 3.1 and Sections 4–7 | Étale morphisms; Étale morphisms and local algebra; Étale morphisms and field extensions |
| Smooth algebras over a field and the Jacobian criterion, Theorems 5.1–6.1 and Sections 1–3 | Criteria for smooth morphisms and field extensions; Smooth morphisms and field extensions |
| Regular sequences, depth and Cohen–Macaulay modules, Propositions 1.1–1.3 and Theorem 6.1 | Koszul complexes, regular sequences and regular rings |
| Regular local rings, Theorem 1.1 | Regular rings |
| Kähler differentials, Theorems 3.1–3.3, Proposition 3.4 and Theorem 7.1 | Cotangent complexes and differentials; Cotangent complexes and differentials; Cotangent complexes, differentials and finite presentation; Cotangent complexes and differentials |
| Faithful flatness and the local criterion for flatness, Theorems 2.1–3.1, 4.2, 5.2 and 5.4 | Flatness and local algebra |
| [Lesson 7, Appendix A, Lemma A.3](artin-axioms.md#appendix-a-artin-rees-perturbation-and-graded-quotients) | Derived categories; Derived categories; Flatness |

The following proofs supply the conormal and Koszul transitivity arguments, finite projective and smooth-section lifting, geometric regularity, the finite-over-regular complete-local construction, and G-ring permanence. In particular the first-homology quotient argument is included at its own scope; the AG-CA cotangent-presentation comparison is not substituted for it. Formal smoothness of arbitrary separable field extensions is proved in the included algebraic chain, while the coefficient-ring lesson is used only for the prime-field assertion it actually proves.

Section 6.1 proves the full family-approximation construction used in Lesson 7, Lemma 2.3. Its finite-complex Artin–Rees comparison (Tags 07VE/07VF) is the actual written Lesson 7, Appendix A, Lemmas A.1–A.2; its presentation, completion, point and finite-stage object comparisons are supplied here. The concise prerequisite record below identifies the still unbound lower foundations.

### B.9. Desingularization from singularity ideals

We now give the full proof chain from the Stacks source `smoothing.tex`: singular ideals and improved presentations; flat nilpotent lifting; lifting and desingularization; reduction to fields; localization; separable and inseparable residue fields; Popescu's theorem; both approximation theorems and the prime-localized variant. The independent Néron-DVR interlude is not needed for this chain and has not been imported into this assigned support chapter. Its omission does not narrow the regular Noetherian map theorem. All corrections are identified in §7 and applied in the incorporated derivative.

#### Singular ideals

The proof will measure progress by the open subset on which a finite presentation is smooth. We need a way to express that open subset using equations that can be transported to another ring. Jacobian minors provide such equations, provided we also control the relations omitted from the chosen minor. The constructions below make both requirements explicit.

The relevant mathematical references are the Stacks Project, Tags [07C5](https://stacks.math.columbia.edu/tag/07C5), [07C6](https://stacks.math.columbia.edu/tag/07C6), [07C7](https://stacks.math.columbia.edu/tag/07C7), [07ET](https://stacks.math.columbia.edu/tag/07ET), [07CA](https://stacks.math.columbia.edu/tag/07CA), [07CC](https://stacks.math.columbia.edu/tag/07CC) and [07EU](https://stacks.math.columbia.edu/tag/07EU), together with the corresponding results in the [AI Integrated Stacks Project, *Smoothing Ring Maps*](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/smoothing.tex).

#### Definition. The singularity ideal

For a homomorphism $R\to A$, let $U$ consist of the prime ideals of $A$ at which this homomorphism is smooth. Smoothness at a prime means smoothness on a principal neighbourhood of that prime, so $U$ is open; see [Smoothness at a prime ideal](#native-algebra-definition-smooth-at-prime). Define $H_{A/R}$ by

$$H_{A/R}=\bigcap_{\mathfrak q\notin U}\mathfrak q.$$

We use the convention that the intersection of an empty family of ideals is $A$. Since the complement of $U$ is closed, $H_{A/R}$ is its defining radical ideal. In particular,

$$D(H_{A/R})=U,\qquad
V(H_{A/R})=\{\mathfrak q:R\to A\text{ is not smooth at }\mathfrak q\}.$$

This characterizes the singularity ideal uniquely. It does not assert that the ideal is finitely generated or that $U$ is quasi-compact.

#### Lemma. A Jacobian presentation near a smooth point

Fix a presentation $A=R[x_1,\ldots,x_n]/I$, with $I=(f_1,\ldots,f_m)$. Suppose that $R\to A$ is smooth at $\mathfrak q$. One can select $c$ equations and $c$ variables, where $0\leq c\leq\min(m,n)$, whose Jacobian minor $\Delta$ has the following property: there is an element $a\notin\mathfrak q$ divisible by $\Delta$ in $A$ such that

$$a f_\ell\in(f_j:j\text{ is one of the selected equations})+I^2
\quad(1\leq\ell\leq m).$$

Here multiplication by an element of $A$ means multiplication on $I/I^2$; the displayed assertion is independent of a lift of $a$ to the polynomial ring. Equivalently, for the selected sets $U,V$ of column and row indices,

$$a=a'\det(\partial f_j/\partial x_i)_{j\in V,\ i\in U}
\quad\text{for some }a'\in A.$$

**Proof.** Work first over $A_{\mathfrak q}$. The presentation of the [naive cotangent complex](#context-algebra-section-netherlander) is

$$I/I^2\longrightarrow\bigoplus_{i=1}^n A\,\mathrm dx_i.$$

By [smoothness](#native-algebra-definition-smooth), this map becomes a split injection near $\mathfrak q$, with finite projective cokernel. Its source is therefore finite projective there as well. Choose from the classes of the $f_j$ a basis of $(I/I^2)\otimes_A\kappa(\mathfrak q)$; call its size $c$. Choose $n-c$ of the coordinate differentials whose images form a basis of $\Omega_{A/R}\otimes_A\kappa(\mathfrak q)$. The remaining $c$ coordinates give the desired minor: projection onto them identifies the span of the selected relation differentials with a $c$-dimensional vector space. Thus $\Delta\notin\mathfrak q$.

Finite projectivity permits both chosen bases and the splitting to be used after inverting one element $h\notin\mathfrak q$. In particular, the selected equations generate $(I/I^2)_h$. For each of the finitely many $f_\ell$, clear the denominators in an expression for its class in this generating set. There is consequently a single exponent $N$ with

$$h^N I\subseteq(f_j:j\in V)+I^2.$$

Take $a=h^N\Delta$. This element stays outside $\mathfrak q$, is divisible by the specified minor, and satisfies all the required containments. Localization of the presentation used above is justified by [Localization of the naive cotangent complex](#native-algebra-lemma-localize-nl). If $c=0$, the minor is the empty determinant $1$; the same argument gives $h^N I\subseteq I^2$. ∎

#### Definition. Strict standard smoothness

Let $A$ be finitely presented over $R$. The following definitions concern an element $a\in A$, but allow the choice of a presentation. Write such a presentation as

$$A=R[x_1,\ldots,x_n]/(f_1,\ldots,f_m),\qquad I=(f_1,\ldots,f_m),$$

and choose an integer $c$ between $0$ and $\min(m,n)$. Both definitions require the first $c$ equations to control the remaining relations after multiplication by $a$:

$$a f_{c+j}\in(f_1,\ldots,f_c)+I^2
\quad(1\leq j\leq m-c).$$

An element is **elementary standard** if these data can be chosen so that it is a multiple of the first $c$-by-$c$ Jacobian minor:

$$a=a'\det(\partial f_j/\partial x_i)_{1\leq j,i\leq c},\qquad a'\in A.$$

It is **strictly standard** if, with the same condition on the relations, it belongs to the ideal of all maximal minors of the $c$ selected relation differentials:

$$a=\sum_{\substack{U\subseteq\{1,\ldots,n\}\\|U|=c}}
a_U\det(\partial f_j/\partial x_i)_{1\leq j\leq c,\ i\in U},
\qquad a_U\in A.$$

We order the column indices in each determinant increasingly. Elementary standard implies strictly standard by assigning coefficient zero to the unused minors. Empty minors have determinant $1$; thus the definitions also cover $c=0$. The preceding lemma shows that every smooth prime has an elementary standard element outside it, after renumbering the selected equations and variables.

#### Lemma. The Jacobian relation in a strict presentation

Keep the presentation and the integer $c$ above. Let

$$u:A^c\longrightarrow I/I^2,\qquad e_j\longmapsto[f_j],
\qquad d:I/I^2\longrightarrow A^n,\qquad[f]\longmapsto\mathrm df.$$

If $a$ is an $A$-linear combination of the $c$-by-$c$ minors of $du$, there is an $A$-linear map $\psi:A^n\to A^c$ satisfying $\psi du=a\,1_{A^c}$. Conversely, the existence of such a map implies that $a^c$ belongs to the ideal of these minors.

**Proof.** Put $J=du$, regarded as an $n$-by-$c$ matrix. For a set $U$ of $c$ row indices, let $P_U:A^n\to A^c$ be coordinate projection and let $J_U=P_UJ$. The adjugate identity gives

$$\operatorname{adj}(J_U)P_UJ=\det(J_U)1_{A^c}.$$

If $a=\sum_U a_U\det(J_U)$, use

$$\psi=\sum_U a_U\operatorname{adj}(J_U)P_U.$$

This has the asserted source and target, and its composite with $J$ is multiplication by $a$. For the converse, take determinants in $\psi J=a1_{A^c}$. Expanding the determinant of a product by its minors gives

$$a^c=\det(\psi J)=\sum_{|U|=c}\det(\psi_{*,U})\det(J_U).$$

The minor expansion follows directly from the multilinear determinant formula: terms with a repeated intermediate index cancel by alternation, and the remaining terms group according to $U$. This works over every commutative ring. For $c=0$, both the determinant of the identity on the zero module and the empty minor are $1$, so the assertion has the same interpretation. This is also the calculation underlying [A left inverse for a matrix](#native-algebra-lemma-matrix-left-inverse). ∎

#### Lemma. Controlling a power of the Jacobian determinant (Elkik)

For a finitely presented homomorphism $R\to A$, the elementary standard elements generate an ideal whose radical is $H_{A/R}$. The same is true if one uses all strictly standard elements.

**Proof.** We first check what happens after inverting a strictly standard element $a$. The relation condition says that the map

$$u_a:A_a^c\longrightarrow(I/I^2)_a$$

is surjective. The preceding matrix calculation gives $\psi_a d_a u_a=a1$. As $a$ is a unit, $u_a$ is also injective. Moreover $a^{-1}u_a\psi_a$ is a left inverse for $d_a$: this can be checked after precomposition with the surjection $u_a$. Hence $d_a$ is split injective. Its cokernel is a direct summand of the finite free module $A_a^n$. The finite-presentation cotangent criterion therefore proves that $R\to A_a$ is smooth. In particular, every strictly standard element belongs to $H_{A/R}$.

Let $J_e$ and $J_s$ be the ideals generated by elementary and strictly standard elements, respectively. We have

$$J_e\subseteq J_s\subseteq H_{A/R}.$$

At every prime in the smooth locus, the Jacobian presentation lemma supplies an elementary standard element which is not in that prime. Thus $D(J_e)$ contains the entire smooth locus. The previous inclusion gives the reverse containment. Taking complements and then defining radical ideals yields

$$\sqrt{J_e}=\sqrt{J_s}=H_{A/R}.$$

Neither this argument nor the preceding cotangent calculation requires a Noetherian base. ∎

#### Example. A smooth locus that is not quasi-compact

Let $k$ be a field and consider

$$R=k[x,y_1,y_2,\ldots]/(xy_i:i\geq1),\qquad A=R/(x)=k[y_1,y_2,\ldots].$$

The smooth locus of $\operatorname{Spec}A\to\operatorname{Spec}R$ is exactly $\bigcup_{i\geq1}D(y_i)$. Indeed, where $y_i$ is a unit the relation $xy_i=0$ forces $x=0$, so the morphism is an isomorphism. At the prime $(y_1,y_2,\ldots)$, its inverse image in $R$ is $(x,y_1,y_2,\ldots)$. In that local ring the ideal $(x)$ is nonzero: its annihilator is generated by all the $y_i$, so no element outside the prime kills $x$. This principal ideal is proper and cannot be idempotent, by Nakayama's lemma. The quotient by it is therefore not flat. To see the last implication directly, if $R/(x)$ were flat, tensoring $(x)\hookrightarrow R$ with the quotient would be injective; its resulting map is zero, forcing $(x)/(x)^2=0$. Smoothness consequently fails at this point.

Every prime of $A$ outside that one omits some $y_i$, proving the asserted description. No finite subcollection of these principal opens covers their union: for a finite set $E$ of indices, the prime $(y_i:i\in E)$ belongs to $D(y_j)$ for every $j\notin E$, while belonging to none of the selected $D(y_i)$. Thus even a finitely presented ring homomorphism can have a smooth locus which is not quasi-compact.

#### Lemma. Base change of a strict standard presentation

For a homomorphism $R\to R'$ and a finitely presented $R$-algebra $A$, write $A'=A\otimes_R R'$. If $a\in A$ is elementary standard, its image $a\otimes1$ is elementary standard over $R'$. The corresponding assertion holds for strictly standard elements.

**Proof.** Use a presentation witnessing the property of $a$. Tensoring the presentation with $R'$ gives

$$A'=R'[x_1,\ldots,x_n]/(f'_1,\ldots,f'_m).$$

Formal differentiation of a polynomial commutes with mapping its coefficients from $R$ to $R'$. Consequently every relevant Jacobian minor maps to the corresponding minor of the new presentation. The equalities expressing $a$ as a multiple, or a linear combination, of these minors remain equalities after this coefficient map. So do the finitely many containments $a f_{c+j}\in(f_1,\ldots,f_c)+I^2$: map expressions witnessing those containments to the new polynomial ring. These are exactly the required conditions for $a\otimes1$. No flatness of $R'$ over $R$ is needed. ∎

#### Lemma. Solving the strict-standard Jacobian relations

Suppose $R\to A\to\Lambda$ is given, $A$ is finitely presented over $R$, and $H_{A/R}\Lambda=\Lambda$. There is a smooth $R$-algebra $B$ through which the specified map $A\to\Lambda$ factors.

**Proof.** The equality of ideals means that finitely many elements $f_i\in H_{A/R}$ and $\lambda_i\in\Lambda$ satisfy $\sum_i f_i\lambda_i=1$. Introduce variables $Z_i$ and set

$$B=A[Z_1,\ldots,Z_r]/\left(\sum_{i=1}^r f_iZ_i-1\right).$$

Evaluation $Z_i\mapsto\lambda_i$ defines an $A$-algebra homomorphism $B\to\Lambda$. In $B$ the elements $f_i$ generate the unit ideal, so their principal opens cover $\operatorname{Spec}B$. On the $i$th open, eliminate $Z_i$ using the displayed equation:

$$B_{f_i}\simeq A_{f_i}[Z_1,\ldots,\widehat{Z_i},\ldots,Z_r].$$

The definition of $H_{A/R}$ says that $A_{f_i}$ is smooth over $R$. A polynomial algebra over it is smooth as well, so these covering opens establish smoothness of $B/R$. The presentation of $B$ is finite, as required. If the target is the zero ring, the smooth zero algebra supplies the factorization directly. ∎

#### Presentations of algebras

A presentation records more than generators of an algebra: its conormal module records which equations remain independent to first order. Adding the vector bundle associated with this module makes the conormal data free while retaining a section back to the original algebra. This gives a convenient route from arbitrary smooth or syntomic algebras to explicit equations.

We use the convention that a relative global complete intersection is a quotient of a polynomial algebra by $c$ equations which is flat over the base and whose nonempty fibres have pure dimension equal to the number of variables minus $c$. The corresponding local criteria, including the conormal statements used below, are supplied by [Local criteria for a syntomic algebra](#native-algebra-lemma-syntomic), [Local criteria for complete intersections](#native-algebra-lemma-lci), and [Finite projectivity of a quasi-regular conormal module](#native-more-algebra-lemma-quasi-regular-ideal-finite-projective).

#### Lemma. Improving a finite presentation

Let $A$ be a finitely presented algebra over a ring $R$. There is a finite-type $A$-algebra $C$ with an $A$-algebra augmentation $C\to A$ such that the following assertions hold.

1. If $A_a/R$ is a local complete intersection, then $C_a/A_a$ is smooth and $C_a$ has a polynomial presentation over $R$ with a free conormal module.
2. If $A_a/R$ is smooth, then $\Omega_{C_a/R}$ is free.

The composite $A\to C\to A$ is the identity. If $R$ is Noetherian, $C$ is also finitely presented over $R$.

**Proof.** Choose $P=R[x_1,\ldots,x_n]\twoheadrightarrow A$ with kernel $I=(f_1,\ldots,f_m)$, and put $M=I/I^2$. Define

$$C=\operatorname{Sym}_A(M).$$

Projection to degree zero supplies the required augmentation. The images of the $m$ chosen equations generate $M$, so they give $m$ algebra generators for $C/A$. Thus $C$ has finite type over $A$ and over $R$. Over a Noetherian base its relation ideal in a finite polynomial presentation is finitely generated, giving the last assertion.

To check the first assertion, fix $a$ with $A_a/R$ a local complete intersection and work with

$$0\longrightarrow K_a\longrightarrow A_a^m\longrightarrow M_a\longrightarrow0.$$

The conormal criterion says that $M_a$ is finite projective. The sequence therefore splits, and $K_a\oplus M_a\simeq A_a^m$. In particular both summands are finite projective. Since $C_a=\operatorname{Sym}_{A_a}(M_a)$, it is a polynomial algebra on a free module locally on $\operatorname{Spec}A_a$. It follows that $C_a/A_a$ is smooth; see also [Smoothness of a symmetric algebra](#native-more-algebra-lemma-symmetric-algebra-smooth).

Choose a polynomial $h\in P$ representing $a$. A polynomial presentation over $R$ for $A_a$ is obtained by adjoining $x_0$ and imposing $hx_0-1$ in addition to $I$. A presentation for $C_a$ further adjoins variables $y_1,\ldots,y_m$ representing the chosen generators of $M$. Write its relation ideal as $J'$. Cotangent transitivity for these presentations gives

$$0\longrightarrow C_a\oplus(M_a\otimes_{A_a}C_a)
\longrightarrow J'/(J')^2
\longrightarrow K_a\otimes_{A_a}C_a\longrightarrow0.$$

Here the first summand is the relation $hx_0-1$. The right-hand term comes from the linear relations among the $y_j$. To see why there is no extra term on the left, locally split $A_a^m=M_a\oplus K_a$: the quotient defining its symmetric algebra then sets precisely the coordinates of $K_a$ equal to zero, a regular sequence. The complete-intersection conormal sequence is therefore left exact. These local identifications describe the same presentation maps and hence glue. This is the instance of [Cotangent transitivity with a complete-intersection terminal map](#native-more-algebra-lemma-transitive-lci-at-end) and [The cotangent complex of a symmetric algebra](#native-more-algebra-lemma-cotangent-complex-symmetric-algebra) used here.

The right-hand module is projective, so the sequence splits. Consequently

$$J'/(J')^2\simeq C_a\oplus(M_a\oplus K_a)\otimes_{A_a}C_a
\simeq C_a^{m+1}.$$

This proves the first assertion, including a presentation over $R$ itself.

If $A_a/R$ is smooth, the differential sequence for $R\to A_a\to C_a$ is split exact:

$$0\longrightarrow\Omega_{A_a/R}\otimes_{A_a}C_a
\longrightarrow\Omega_{C_a/R}
\longrightarrow M_a\otimes_{A_a}C_a\longrightarrow0.$$

The right-hand identification is the differential calculation for a symmetric algebra; projectivity gives a splitting. The original smooth presentation also gives $M_a\oplus\Omega_{A_a/R}\simeq A_a^n$. Thus $\Omega_{C_a/R}\simeq C_a^n$. This is an existence of a free-module identification, not a claimed canonical choice of its basis. ∎

#### Proposition. Lifting a smooth algebra over a quotient

Let $R\twoheadrightarrow R_0=R/I$ be any quotient. Every syntomic $R_0$-algebra $A_0$ is the reduction of a syntomic $R$-algebra: there are $A/R$ syntomic and an $R_0$-algebra isomorphism $A/IA\simeq A_0$. If $A_0/R_0$ is smooth, $A$ can be chosen smooth. There is no nilpotence assumption on $I$.

**Proof.** First suppose $A_0/R_0$ is syntomic. For a finite polynomial presentation of $A_0$, its conormal module $P_0$ is finite projective. The preceding construction gives

$$C_0=\operatorname{Sym}_{A_0}(P_0),$$

smooth over $A_0$, with a presentation over $R_0$ whose conormal module is free. The [presentation lemma for a conormal basis](#native-algebra-lemma-huber) allows the equations to be chosen as lifts of a basis. Hence

$$C_0=R_0[y_1,\ldots,y_m]/(\bar f_1,\ldots,\bar f_c).$$

Lift these finitely many polynomials to $R[y_1,\ldots,y_m]$. Their quotient reduces to $C_0$. The [localization criterion for relative complete intersections](#native-algebra-lemma-localize-relative-complete-intersection) permits a localization by an element equal to $1$ modulo $I$ after which the quotient is syntomic over $R$. Denote this quotient by $C$, retaining the specified identification $C/IC=C_0$.

Choose a finite projective complement $Q_0$ with $P_0\oplus Q_0\simeq A_0^n$. The [projective-module lifting lemma](#native-more-algebra-lemma-lift-projective-module) gives an étale map $C\to C'$ whose reduction modulo $I$ is an isomorphism and a finite projective $C'$-module $Q$ lifting $Q_0\otimes_{A_0}C_0$. Put $D=\operatorname{Sym}_{C'}(Q)$. Then $D/C'$ is smooth, and composition shows that $D/R$ is syntomic. The chosen identifications give

$$\begin{aligned}
D/ID
&\simeq\operatorname{Sym}_{C_0}(Q_0\otimes_{A_0}C_0)\\
&\simeq\operatorname{Sym}_{A_0}(Q_0)\otimes_{A_0}\operatorname{Sym}_{A_0}(P_0)\\
&\simeq\operatorname{Sym}_{A_0}(Q_0\oplus P_0)
\simeq A_0[t_1,\ldots,t_n].
\end{aligned}$$

All these maps are algebra maps over $A_0$; the last depends on the chosen complement and basis. Choose lifts $d_i\in D$ of the coordinates $t_i$, and set $A'=D/(d_1,\ldots,d_n)$. Its reduction is $A_0$, with its specified $R_0$-algebra structure.

The map $A'/R$ is syntomic in an open neighbourhood of $V(IA')$. Indeed, around any such point write the syntomic algebra $D$ as a relative complete intersection. In its reduction, the additional equations are the polynomial coordinates $t_i$, a regular sequence with quotient $A_0$ flat over $R_0$. Applying the same relative complete-intersection localization criterion to the combined equations proves the assertion at that point. This argument uses the [composition criterion](#native-algebra-lemma-composition-syntomic) and [local syntomic presentations](#native-algebra-lemma-syntomic), and therefore retains flatness as well as the complete-intersection condition.

Here and below a localization can preserve the entire closed fibre. If an open $U\subseteq\operatorname{Spec}A'$ contains $V(IA')$, write its closed complement as $V(J)$. The containment says $IA'+J=A'$. Choose $g\in J$ with $g\equiv1\pmod{IA'}$. Then $D(g)\subseteq U$ and $(A'_g)/I(A'_g)\simeq A'/IA'$. Apply this to the syntomic neighbourhood to obtain the desired syntomic $A$.

For the smooth assertion, start with this syntomic lift. It is flat and finitely presented over $R$. At every point of $V(IA)$, its fibre is a fibre of the given smooth algebra $A_0/R_0$. By [flatness and smooth fibres](#native-algebra-lemma-flat-fibre-smooth), $A/R$ is smooth at all these points. The smooth locus is open. A further localization equal to $1$ on the closed fibre, chosen as above, therefore gives a smooth lift without changing $A/IA$. ∎

#### Lemma. Complete-intersection presentations of syntomic algebras

For every syntomic $R$-algebra $A$ there is a smooth $A$-algebra $C$ with an $A$-algebra augmentation such that $C/R$ is a relative global complete intersection. In particular it has a presentation

$$C=R[x_1,\ldots,x_n]/(f_1,\ldots,f_c)$$

which is flat over $R$ and has fibres of pure dimension $n-c$ wherever they are nonempty.

**Proof.** Apply the improving-presentation lemma with $a=1$. Syntomic implies local complete intersection, so the resulting $C/A$ is smooth and its conormal module has a finite basis. The [conormal-basis presentation lemma](#native-algebra-lemma-huber) gives a presentation in which the defining equations lift that basis. Since smooth algebras are syntomic and syntomic maps compose, $C/R$ is syntomic, in particular flat. On each fibre the equations are a local complete-intersection sequence of length $c$ in a polynomial algebra on $n$ variables. The [complete-intersection dimension criterion](#native-algebra-lemma-lci) therefore gives dimension $n-c$ at every component. The augmentation is the degree-zero map in the original symmetric-algebra construction and has not been changed by choosing the presentation. ∎

#### Lemma. Standard presentations of smooth algebras

If $A/R$ is smooth, there is a smooth $A$-algebra $B$ with an $A$-algebra augmentation $B\to A$ such that $B/R$ is standard smooth: it admits a finite polynomial presentation with an invertible square Jacobian minor of size equal to the number of equations.

**Proof.** The preceding lemma gives a smooth $A$-algebra $C$, with augmentation, and a relative complete-intersection presentation

$$C=R[x_1,\ldots,x_n]/(f_1,\ldots,f_c).$$

Because $C/R$ is smooth, the matrix

$$J=(\partial f_j/\partial x_i)_{1\leq j\leq c,\ 1\leq i\leq n}$$

has a right inverse $T=(t_{i\ell})$ over $C$, so $JT=1_c$. This is the splitting of the conormal differential sequence. Introduce $c$ variables $y_\ell$ and set $B'=C[y_1,\ldots,y_c]$. Choose polynomial lifts of the $t_{i\ell}$ and define a map

$$R[z_1,\ldots,z_n]\longrightarrow B',\qquad
z_i\longmapsto x_i-\sum_{\ell=1}^c t_{i\ell}y_\ell.$$

We verify directly that this map is étale near the zero section $y=0$. Regard $B'$ as an algebra over $R[z_1,\ldots,z_n]$ with variables $y_1,\ldots,y_c,x_1,\ldots,x_n$ and equations

$$f_j(x)=0\quad(1\leq j\leq c),\qquad
x_i-\sum_\ell t_{i\ell}(x)y_\ell-z_i=0\quad(1\leq i\leq n).$$

The square Jacobian matrix in those variables reduces modulo $(y_1,\ldots,y_c)$ to

$$\begin{pmatrix}0&J\\-T&1_n\end{pmatrix}.$$

Its determinant is $\det(JT)=1$. Let $g\in B'$ be the determinant before reduction. Then $g\equiv1\pmod{(y_1,\ldots,y_c)}$. On $B=B'_g$ the square minor is invertible, so this is a standard étale algebra over $R[z_1,\ldots,z_n]$. This follows from the [standard smooth Jacobian criterion](#native-algebra-lemma-standard-smooth): the relative dimension is zero. If one writes localization as a polynomial presentation by adjoining $v$ with $gv-1=0$, the enlarged minor is the old one times $g$, hence is still invertible. Viewing the $z_i$ as additional free variables exhibits $B$ as standard smooth over $R$.

The map $C\to B$ is a polynomial extension followed by localization, hence smooth. The evaluation $y_\ell\mapsto0$ extends through that localization because $g$ evaluates to $1$. It gives a retraction $B\to C$. Composing with the original maps between $A$ and $C$ proves all the assertions about $A\to B\to A$. In particular, the localization has not removed the section needed for the return to $A$. ∎

#### Lemma. Standard smooth presentations in a filtered colimit

An $R$-algebra which is a filtered colimit of smooth $R$-algebras can also be expressed as a filtered colimit of standard smooth $R$-algebras.

**Proof.** Use the [finite factorization criterion](#reader-section-2). A map $P\to\Lambda$ from a finitely presented $R$-algebra first factors through a smooth algebra $C$. Choose the standard smooth algebra $B$ with maps $C\to B\to C$ whose composite is the identity, as in the preceding lemma. The composite

$$P\longrightarrow C\longrightarrow B\longrightarrow C\longrightarrow\Lambda$$

has the original value on $P$. Thus every finite presentation mapping into $\Lambda$ factors through a standard smooth algebra. The same finite factorization proof applies to this class: tensor products and coequalizers need only be finitely presented before one applies the factorization property. It therefore constructs a filtered indexing category of standard smooth algebras with colimit $\Lambda$. ∎

#### Lemma. Including prescribed generators in a smooth presentation

Let $A/R$ be standard smooth and let $E=\{a_1,\ldots,a_n\}$ be a finite subset. There is a standard smooth presentation whose first $n$ variables represent these elements and whose invertible Jacobian minor includes these $n$ variables. In particular the number $c$ of equations can be chosen at least $n$.

**Proof.** Start with

$$A=R[y_1,\ldots,y_m]/(g_1,\ldots,g_d),$$

where the minor in $y_1,\ldots,y_d$ is a unit. Choose polynomials $h_i(y)$ representing $a_i$. Adjoin $x_1,\ldots,x_n$ and impose $x_i-h_i(y)=0$ as well as the $g_j$. Eliminating the $x_i$ identifies the new quotient with $A$, with the required specified images. Taking derivatives with respect to $x_1,\ldots,x_n,y_1,\ldots,y_d$ gives a block triangular matrix with diagonal blocks $1_n$ and the original Jacobian minor. Its determinant is a unit. Thus the new presentation is standard smooth and has $c=n+d$ equations. ∎

#### Lemma. Comparing standard smooth presentations
 Let $R \to A$ be a ring map of finite presentation. Let $a \in A$. Consider the following conditions on $a$:

1.  $A_a$ is smooth over $R$,

2.  $A_a$ is smooth over $R$ and $\Omega_{A_a/R}$ is stably free,

3.  $A_a$ is smooth over $R$ and $\Omega_{A_a/R}$ is free,

4.  $A_a$ is standard smooth over $R$,

5.  $a$ is strictly standard in $A$ over $R$,

6.  $a$ is elementary standard in $A$ over $R$.

Then we have

1.  $4$ $\Rightarrow$ (3) $\Rightarrow$ (2) $\Rightarrow$ (1),

2.  $6$ $\Rightarrow$ (5),

3.  $6$ $\Rightarrow$ (4),

4.  $5$ $\Rightarrow$ (2),

5.  $2$ $\Rightarrow$ the elements $a^e$, $e \geq e_0$ are strictly standard in $A$ over $R$,

6.  $4$ $\Rightarrow$ the elements $a^e$, $e \geq e_0$ are elementary standard in $A$ over $R$.

**Proof.** Part (a) is clear from the definitions and Algebra, Lemma [Standard smooth algebras](#native-algebra-lemma-standard-smooth). Part (b) is clear from Definition [Strict standard smoothness](#native-smoothing-definition-strictly-standard).

Proof of (c). Choose a presentation $A = R[x_1, \ldots, x_n]/(f_1, \ldots, f_m)$ such that ([the displayed identity](#native-smoothing-equation-elementary-standard-one)) and ([the displayed identity](#native-smoothing-equation-elementary-standard-two)) hold. Choose $h \in R[x_1, \ldots, x_n]$ mapping to $a$. Then $$A_a = R[x_0, x_1, \ldots, x_n]/(x_0h - 1, f_1, \ldots, f_m).$$ Write $J = (x_0h - 1, f_1, \ldots, f_m)$. By ([the displayed identity](#native-smoothing-equation-elementary-standard-two)) we see that the $A_a$-module $J/J^2$ is generated by $x_0h - 1, f_1, \ldots, f_c$ over $A_a$. Hence, as in the proof of Algebra, Lemma [A presentation realizing a basis of the conormal module](#native-algebra-lemma-huber), we can choose a $g \in 1 + J$ such that $$A_a = R[x_0, \ldots, x_n, x_{n + 1}]/
(x_0h - 1, f_1, \ldots, f_c, gx_{n + 1} - 1).$$ At this point ([the displayed identity](#native-smoothing-equation-elementary-standard-one)) implies that $R \to A_a$ is standard smooth (use the coordinates $x_0, x_1, \ldots, x_c, x_{n + 1}$ to take derivatives).

Proof of (d). Choose a presentation $A = R[x_1, \ldots, x_n]/(f_1, \ldots, f_m)$ such that ([the displayed identity](#native-smoothing-equation-strictly-standard-one)) and ([the displayed identity](#native-smoothing-equation-strictly-standard-two)) hold. Write $I = (f_1, \ldots, f_m)$. We already know that $A_a$ is smooth over $R$, see Lemma [Controlling a power of the Jacobian determinant](#native-smoothing-lemma-elkik). By Lemma [The Jacobian relation in a strict presentation](#native-smoothing-lemma-parse-equation-strictly-standard-one) we see that $(I/I^2)_a$ is free on $f_1, \ldots, f_c$ and maps isomorphically to a direct summand of $\bigoplus A_a \text{d}x_i$. Since $\Omega_{A_a/R} = (\Omega_{A/R})_a$ is the cokernel of the map $(I/I^2)_a \to \bigoplus A_a \text{d}x_i$ we conclude that it is stably free.

Proof of (e). Choose a presentation $A = R[x_1, \ldots, x_n]/I$ with $I$ finitely generated. By assumption we have a short exact sequence $$0 \to (I/I^2)_a \to \bigoplus\nolimits_{i = 1, \ldots, n} A_a\text{d}x_i \to
\Omega_{A_a/R} \to 0$$ which is split exact. Hence we see that $(I/I^2)_a \oplus \Omega_{A_a/R}$ is a free $A_a$-module. Since $\Omega_{A_a/R}$ is stably free we see that $(I/I^2)_a$ is stably free as well. Thus replacing the presentation chosen above by $A = R[x_1, \ldots, x_n, x_{n + 1}, \ldots, x_{n + r}]/J$ with $J = (I, x_{n + 1}, \ldots, x_{n + r})$ for some $r$ we get that $(J/J^2)_a$ is (finite) free. Choose $f_1, \ldots, f_c \in J$ which map to a basis of $(J/J^2)_a$. Extend this to a list of generators $f_1, \ldots, f_m \in J$. Consider the presentation $A = R[x_1, \ldots, x_{n + r}]/(f_1, \ldots, f_m)$. Then ([the displayed identity](#native-smoothing-equation-strictly-standard-two)) holds for $a^e$ for all sufficiently large $e$ by construction. Moreover, since $(J/J^2)_a \to \bigoplus\nolimits_{i = 1, \ldots, n + r} A_a\text{d}x_i$ is a split injection we can find an $A_a$-linear left inverse. Writing this left inverse in terms of the basis $f_1, \ldots, f_c$ and clearing denominators we find a linear map $\psi_0 : A^{\oplus n + r} \to A^{\oplus c}$ such that $$A^{\oplus c} \xrightarrow{(f_1, \ldots, f_c)}
J/J^2 \xrightarrow{f \mapsto \text{d}f}
\bigoplus\nolimits_{i = 1, \ldots, n + r} A \text{d}x_i
\xrightarrow{\psi_0}
A^{\oplus c}$$ is multiplication by $a^{e_0}$ for some $e_0 \geq 1$. By Lemma [The Jacobian relation in a strict presentation](#native-smoothing-lemma-parse-equation-strictly-standard-one) we see ([the displayed identity](#native-smoothing-equation-strictly-standard-one)) holds for all $a^{ce_0}$ and hence for $a^e$ for all $e$ with $e \geq ce_0$.

Proof of (f). Choose a presentation $A_a = R[x_1, \ldots, x_n]/(f_1, \ldots, f_c)$ such that $\det(\partial f_j/\partial x_i)_{i, j = 1, \ldots, c}$ is invertible in $A_a$. We may assume that for some $m < n$ the classes of the elements $x_1, \ldots, x_m$ correspond to $a_i/1$ where $a_1, \ldots, a_m \in A$ are generators of $A$ over $R$, see Lemma [Including prescribed generators in a smooth presentation](#native-smoothing-lemma-standard-smooth-include-generators). After replacing $x_i$ by $a^Nx_i$ for $m < i \leq n$ we may assume the class of $x_i$ is $a_i/1 \in A_a$ for some $a_i \in A$. Consider the ring map $$\Psi : R[x_1, \ldots, x_n] \longrightarrow A,\quad
x_i \longmapsto a_i.$$ This is a surjective ring map. By replacing $f_j$ by $a^Nf_j$ we may assume that $f_j \in R[x_1, \ldots, x_n]$ and that $\Psi(f_j) = 0$ (since after all $f_j(a_1/1, \ldots, a_n/1) = 0$ in $A_a$). Let $J = \operatorname{Ker}(\Psi)$. Then $A = R[x_1, \ldots, x_n]/J$ is a presentation and $f_1, \ldots, f_c \in J$ are elements such that $(J/J^2)_a$ is freely generated by $f_1, \ldots, f_c$ and such that $\det(\partial f_j/\partial x_i)_{i, j = 1, \ldots, c}$ maps to an invertible element of $A_a$. It follows that ([the displayed identity](#native-smoothing-equation-elementary-standard-one)) and ([the displayed identity](#native-smoothing-equation-elementary-standard-two)) hold for $a^e$ and all large enough $e$ as desired. $\square$

**The denominator step in part (6).** Scaling polynomial coordinates by powers of an element of the presented algebra can change their relative derivatives. In particular, the assertion of invertibility in the last paragraph requires an additional argument. For example, over a field of characteristic $p>0$, present $k[x,x^{-1}]$ with coordinates $Z=x$, $Y=x^{-1}$, $X=x$ and equations $Z-X$, $XY-1$. The minor in the $Z,Y$ columns is $X$, a unit. Keep the prescribed generator $Z$ and replace the other coordinates by $U=x^{N+1}$, $V=x^{N-1}$. After inverting $Z$, the equations $Z^{N+1}-U$, $UV-Z^{2N}$ give the same algebra. Their minor in the $Z,V$ columns is $(N+1)Z^NU$, which is zero when $p$ divides $N+1$. Thus the stated scaling operation does not by itself preserve the selected invertible minor. This example refutes that inference, not the existence assertion in part (6). The general assertion in part (6) remains an unresolved proof obligation in this treatment. The desingularization arguments below use the established strict-standard conclusion in part (5); the localized-base argument proves its elementary-standard case separately, using scalars from the base whose relative differentials vanish.

#### The lifting problem

We next show that ind-smoothness survives a flat nilpotent deformation. Here **ind-smooth** means a filtered colimit of smooth algebras. Two different operations are needed. First one lifts a finite diagram, allowing an error ideal inside the nilpotent ideal. Then flatness expresses the coefficients of that error through relations over the base, making it possible to eliminate the error without losing smoothness.

#### Lemma. A first lifting step

Suppose $R\to\Lambda$ is a ring map and $I\subseteq R$ satisfies $I^2=0$. Assume that $\Lambda/I\Lambda$ is ind-smooth over $R/I$. For every finitely presented $R$-algebra $A$ and every $R$-algebra map $\varphi:A\to\Lambda$, there are a smooth $R$-algebra $B$, a finitely generated ideal $J\subseteq IB$, and a factorization

$$A\longrightarrow B/J\longrightarrow\Lambda$$

of $\varphi$. Flatness of $\Lambda$ is not required for this first step.

**Proof.** The [finite factorization criterion](#reader-section-2), together with [standard smooth replacements](#native-smoothing-lemma-colimit-standard-smooth), supplies a factorization of the reduction of $\varphi$ through a standard smooth $(R/I)$-algebra $\bar B$. The map $A/IA\to\bar B$ has finite presentation: both algebras have finite presentation over $R/I$, and one obtains a relative presentation by adjoining their finitely many generators and the equations identifying the images of the generators of $A/IA$. Choose such a presentation

$$\bar B=(A/IA)[t_1,\ldots,t_r]/(\bar g_1,\ldots,\bar g_s).$$

Lift the image of each $t_i$ to an element $\lambda_i\in\Lambda$, and lift $\bar g_j$ to $g_j\in A[t_1,\ldots,t_r]$. Evaluating a lifted relation gives an element of $I\Lambda$. For each $j$, choose a finite expression

$$g_j(\lambda)=\sum_{\ell}\epsilon_{j\ell}\mu_{j\ell},\qquad
\epsilon_{j\ell}\in I,\quad\mu_{j\ell}\in\Lambda.$$

Introduce one variable $u_{j\ell}$ for each chosen summand and define

$$A'=A[t_1,\ldots,t_r,(u_{j\ell})]/
\bigl(g_j-\sum_\ell\epsilon_{j\ell}u_{j\ell}:1\leq j\leq s\bigr).$$

This is finitely presented over $R$. Evaluation at $t_i=\lambda_i$ and $u_{j\ell}=\mu_{j\ell}$ gives $A'\to\Lambda$ extending $\varphi$. Reduction modulo $I$ identifies $A'/IA'$ with the polynomial algebra $\bar B[(u_{j\ell})]$, which is standard smooth over $R/I$.

Choose a standard smooth presentation of $A'/IA'$ and lift its equations to $R$. Localize the lifted quotient at the same Jacobian minor. The [Jacobian criterion](#native-algebra-lemma-standard-smooth) gives a smooth $R$-algebra $B$ and an isomorphism $B/IB\simeq A'/IA'$. Concretely, if the equations are $f_1,\ldots,f_c$ and the chosen minor is $\Delta$, one can take

$$B=R[x_1,\ldots,x_n,v]/(f_1,\ldots,f_c,v\Delta-1).$$

The last equation makes the enlarged Jacobian minor invertible. Its reduction gives exactly the chosen algebra because $\bar\Delta$ was already invertible there.

By [formal smoothness](#native-algebra-proposition-smooth-formally-smooth), the map $B\to A'/IA'$ lifts through the square-zero quotient $A'\to A'/IA'$ to $\theta:B\to A'$. We check its surjectivity without a finite-generation assumption on its cokernel. Since the reduced map is surjective, write any $x\in A'$ as

$$x=\theta(b)+\sum_k\epsilon_kx_k,\qquad \epsilon_k\in I.$$

For each of the finitely many $x_k$, write $x_k=\theta(b_k)+z_k$ with $z_k\in IA'$. Then $\epsilon_kz_k=0$, so $x=\theta(b+\sum_k\epsilon_kb_k)$. Thus $\theta$ is surjective. Its kernel $J$ is contained in $IB$ because the reduction of $\theta$ is an isomorphism. Finally $J$ is finitely generated: a surjection between finitely presented $R$-algebras has a finitely generated kernel, by [independence of finite presentation from the chosen generators](#native-algebra-lemma-finite-presentation-independent). Now $A'=B/J$, and the maps already constructed give the required factorization. ∎

#### Lemma. A second lifting step

Retain $I^2=0$ and the ind-smoothness of $\Lambda/I\Lambda$ over $R/I$, and assume in addition that $\Lambda$ is flat over $R$. Suppose $B/R$ is smooth, $\varphi:B\to\Lambda$ is an $R$-algebra map, and $J\subseteq IB$ is a finitely generated ideal annihilated by $\varphi$. There exist a smooth $R$-algebra $B'$ and maps

$$B\xrightarrow{\alpha}B'\xrightarrow{\beta}\Lambda,
\qquad \beta\alpha=\varphi,\qquad\alpha(J)=0.$$

**Proof.** It suffices to eliminate one generator $h$ of $J$. Indeed, after eliminating it, the images of the remaining generators still lie in the ideal generated by $I$ and still vanish in $\Lambda$. Repetition therefore handles any finite generating set.

Write $h=\sum_{i=1}^q\epsilon_i b_i$ with $\epsilon_i\in I$ and $b_i\in B$. Its image is the relation $\sum_i\epsilon_i\varphi(b_i)=0$. The [equational criterion for flatness](#native-algebra-lemma-flat-eq) gives finitely many $\lambda_j\in\Lambda$ and scalars $a_{ij}\in R$ such that

$$\varphi(b_i)=\sum_j a_{ij}\lambda_j,
\qquad \sum_i\epsilon_i a_{ij}=0\quad\text{for every }j.$$

Thus the relation among the images of the $b_i$ is generated by relations among the coefficients in $R$. Encode these identities in the finitely presented algebra

$$C=B[x_1,\ldots,x_m]/\bigl(b_i-\sum_j a_{ij}x_j:1\leq i\leq q\bigr).$$

It maps to $\Lambda$ by $x_j\mapsto\lambda_j$. The first lifting step factors this map through $B'/J'$, where $B'/R$ is smooth and $J'\subseteq IB'$. In particular $(J')^2=0$. Formal smoothness of $B/R$ lifts $B\to C\to B'/J'$ to a map $\alpha:B\to B'$. Let $\beta$ be the composite $B'\to B'/J'\to\Lambda$; then $\beta\alpha=\varphi$.

Choose $\xi_j\in B'$ lifting the image of $x_j$ in $B'/J'$. The defining equations of $C$ say that

$$\alpha(b_i)=\sum_j a_{ij}\xi_j+\eta_i,
\qquad\eta_i\in J'\subseteq IB'.$$

Consequently

$$\alpha(h)=\sum_j\left(\sum_i\epsilon_i a_{ij}\right)\xi_j
+\sum_i\epsilon_i\eta_i=0.$$

The first sum vanishes by the relations over $R$, and the second vanishes by $I^2=0$. This eliminates $h$, and the finite iteration described at the start proves the lemma. ∎

#### Proposition. Lifting an algebraic factorization

Let $\Lambda$ be a flat $R$-algebra, and let $I\subseteq R$ be nilpotent. If $\Lambda/I\Lambda$ is ind-smooth over $R/I$, then $\Lambda$ is ind-smooth over $R$.

**Proof.** Suppose first that $I^2=0$. Apply the first lifting step to an arbitrary map $A\to\Lambda$ with $A/R$ finitely presented. We obtain $A\to B/J\to\Lambda$, with $B/R$ smooth and $J\subseteq IB$ finitely generated. Apply the second lifting step to the induced map $B\to\Lambda$. The resulting map $B\to B'$ annihilates $J$, hence descends to $B/J\to B'$. Thus

$$A\longrightarrow B/J\longrightarrow B'\longrightarrow\Lambda$$

factors the original map through a smooth $R$-algebra. The finite factorization criterion proves the square-zero case.

For the general case choose $N$ with $I^N=0$. Starting with the assumed ind-smooth algebra $\Lambda/I\Lambda$, successively pass from the base $R/I^r$ to $R/I^{r+1}$ for $r=1,\ldots,N-1$. The kernel $I^r/I^{r+1}$ has square zero, because $2r\geq r+1$. Flatness of $\Lambda/I^{r+1}\Lambda$ over $R/I^{r+1}$ follows by base change from the flatness of $\Lambda/R$. The square-zero case therefore applies at each step. At $r+1=N$ it yields the desired conclusion for $R$ and $\Lambda$. ∎

#### The lifting lemma

The next construction lifts a diagram modulo $\pi^2$ to an actual map into the target. It deliberately allows the new algebra to be singular over the singular part of the original diagram. Over its smooth part, extra variables record the divided errors in the equations, and compatibility relations make the different local presentations agree.

#### Lemma. The lifting lemma

Let $R$ be Noetherian, let $\Lambda$ be an $R$-algebra, and let $\pi\in R$ satisfy

$$\operatorname{Ann}_R(\pi)=\operatorname{Ann}_R(\pi^2),
\qquad
\operatorname{Ann}_\Lambda(\pi)=\operatorname{Ann}_\Lambda(\pi^2).$$

Suppose $\bar C$ is finitely presented over $R/\pi^2R$ and is equipped with an $(R/\pi^2R)$-algebra map to $\Lambda/\pi^2\Lambda$. Then there is a finitely presented $R$-algebra $D$ and compatible maps

$$D\longrightarrow\Lambda,
\qquad \bar C/\pi\bar C\longrightarrow D/\pi D.$$

Compatibility means that the two resulting maps $\bar C\to\Lambda/\pi\Lambda$ coincide. They also commute with the structure maps from $R/\pi^2R$ and $R/\pi R$. These maps have the following properties.

1. $D[1/\pi]$ is smooth over $R$.
2. At every prime of $D$ containing $\pi$ whose image in $\operatorname{Spec}\bar C$ is smooth over $R/\pi^2R$, the map $R\to D$ is smooth.
3. The map $\bar C/\pi\bar C\to D/\pi D$ is smooth at every prime above that same smooth locus.

**Proof.** Put $P=R[x_1,\ldots,x_n]$ and choose a surjection $P\to\bar C$. Its kernel $I=(f_1,\ldots,f_m)$ contains $\pi^2$. Write $\bar P=P/\pi^2P$ and $\bar I=I/\pi^2P$. We first choose finitely many local presentations of the smooth locus.

Since $\bar C$ is Noetherian, that open locus is quasi-compact. The [Jacobian presentation lemma](#native-smoothing-lemma-find-strictly-standard) therefore supplies finitely many elements $a_k\in P$ and subsets $E_k\subseteq\{1,\ldots,m\}$ such that the opens $D(a_k)$ cover precisely this locus and, on each of them, the classes of $f_j$ for $j\in E_k$ form a basis of $\bar I/\bar I^2$. We can also choose $|E_k|$ of the $x$-coordinates so that the corresponding Jacobian minor of these equations is invertible there. In fact the construction of that lemma chooses $a_k$ divisible by such a minor.

Let $I_k=(f_j:j\in E_k)$. We may arrange

$$\bar I_{a_k}=(\bar I_k)_{a_k}.$$

Here is the needed refinement. Before this equality is imposed, the finite module $(\bar I/\bar I_k)_{a_k}$ equals its product with $\bar I_{a_k}$, because the chosen classes generate the conormal module. The determinant form of [Nakayama's lemma](#native-algebra-lemma-nak) gives an element $1+b'_k$, with $b'_k\in\bar I_{a_k}$, annihilating this module. Write $b'_k=b_k/a_k^N$ after increasing $N$. Replacing $a_k$ by $a_k(a_k^N+b_k)$ imposes the desired equality. Its image in $\bar C$ is $a_k^{N+1}$, so it defines the same open subset there and retains the invertibility of the chosen minor.

After a further power of each $a_k$, all the finitely many relations can be written in $P$ as

$$a_k f_\ell=\sum_{j\in E_k}h_{k\ell}^{j}f_j+\pi^2g_{k\ell}
\quad(1\leq\ell\leq m).\tag{L1}$$

For $\ell\in E_k$, choose $h_{k\ell}^{j}=a_k\delta_{\ell j}$ and $g_{k\ell}=0$. Define polynomials in $P[z_1,\ldots,z_m]$ by

$$q_j=f_j-\pi z_j,
\qquad
p_{k\ell}=a_kz_\ell-\sum_{j\in E_k}h_{k\ell}^{j}z_j-\pi g_{k\ell},$$

and set

$$D=P[z_1,\ldots,z_m]/(q_j,p_{k\ell}:j,k,\ell).$$

All index sets are finite, so $D/R$ is finitely presented. Notice that $p_{k\ell}=0$ when $\ell\in E_k$. An identity that will control both the generic and the closed fibre is

$$\pi p_{k\ell}=-a_kq_\ell+\sum_{j\in E_k}h_{k\ell}^{j}q_j.\tag{L2}$$

It follows by substituting (L1) into the definitions, without dividing by $\pi$.

Choose $\lambda_i\in\Lambda$ lifting the specified images of $x_i$ modulo $\pi^2$. For each $j$, choose $\mu_j$ with $f_j(\lambda)=\pi^2\mu_j$. Send $x_i$ to $\lambda_i$ and $z_j$ to $\pi\mu_j$. The polynomials $q_j$ vanish under this assignment. The image of $p_{k\ell}$ is $\pi$ times

$$a_k(\lambda)\mu_\ell-\sum_{j\in E_k}h_{k\ell}^{j}(\lambda)\mu_j-g_{k\ell}(\lambda).$$

Equation (L1) says that $\pi^2$ annihilates this expression. The annihilator hypothesis in $\Lambda$ says that $\pi$ annihilates it as well. Hence we obtain $D\to\Lambda$. Modulo $\pi$, the relations $q_j$ reduce to $f_j$, giving the required map $\bar C/\pi\bar C\to D/\pi D$. Its compatibility with the specified target map is immediate from the chosen lifts of the $x_i$.

After inverting $\pi$, (L2) makes every $p_{k\ell}$ redundant, and the equations $q_j$ eliminate $z_j$ as $f_j/\pi$. Thus

$$D[1/\pi]\simeq R[1/\pi][x_1,\ldots,x_n],$$

which proves the first smoothness assertion.

For the assertions near the closed fibre, fix $k$ and retain only the equations belonging to that chart:

$$D_k=P[z_1,\ldots,z_m]/(q_j:j\in E_k,\ p_{k\ell}:\ell\notin E_k).$$

There is a surjection $D_k\to D$. Modulo $\pi$ and after inverting $a_k$, the equations $p_{k\ell}$ eliminate the $z_\ell$ with $\ell\notin E_k$. The equality of the localized ideals chosen above therefore gives

$$ (D_k/\pi D_k)_{a_k}
\simeq(\bar C/\pi\bar C)_{a_k}[z_j:j\in E_k].\tag{L3}$$

In particular this is smooth over $(\bar C/\pi\bar C)_{a_k}$.

We can verify smoothness of $D_k/R$ directly at a prime containing $\pi$ but not $a_k$. Put $c=|E_k|$. Take derivatives of its $m$ equations with respect to the $c$ chosen $x$-coordinates and the $m-c$ variables $z_\ell$ with $\ell\notin E_k$. Modulo $\pi$, the resulting square matrix has block form

$$\begin{pmatrix}J_k&0\\ *&a_k1_{m-c}\end{pmatrix},$$

where $\det J_k$ is the chosen invertible minor. Its determinant is therefore a unit at the prime. The [Jacobian criterion](#native-algebra-lemma-standard-smooth) proves that $D_k/R$ is smooth there. This also proves flatness at that prime.

It remains to show that the additional equations defining $D$ do not alter this local ring. Let $\mathfrak q\subset D$ contain $\pi$, with image in the smooth locus of $\bar C$, choose $k$ with $a_k\notin\mathfrak q$, and let $\mathfrak q_k$ be its inverse image in $D_k$. Set $T=(D_k)_{\mathfrak q_k}$. Equation (L2), together with the already imposed $p_{k\ell}$ and $q_j$ for $j\in E_k$, shows that $a_kq_\ell=0$ in $T$. Hence every $q_\ell$ is zero there.

For another chart $k'$, compare the two ways of expressing the class of $a_ka_{k'}f_\ell$ in $(\bar I/\bar I^2)_{a_k}$. Since the classes indexed by $E_k$ are a basis, this comparison gives, for every $j\in E_k$,

$$\delta_j:=a_{k'}h_{k\ell}^{j}
-\sum_{j'\in E_{k'}}h_{k'\ell}^{j'}h_{kj'}^{j}=0
\quad\text{in }\bar C_{a_k}.$$

Thus $\delta_j$ belongs to $(I_k+\pi^2P)_{a_k}$, because $I_{a_k}=(I_k+\pi^2P)_{a_k}$. In $T$ the elements $f_j$ for $j\in E_k$ equal $\pi z_j$, so every $\delta_j$ lies in $\pi T$. Reducing the equations for chart $k$ modulo $\pi$ and substituting them into $p_{k'\ell}$ gives

$$a_kp_{k'\ell}\equiv\sum_{j\in E_k}\delta_jz_j
\equiv0\pmod{\pi T}.$$

Since $a_k$ is a unit, $p_{k'\ell}\in\pi T$. Meanwhile (L2) for chart $k'$ shows $\pi p_{k'\ell}=0$, because all the $q_j$ have already vanished in $T$.

Finally $T$ is flat over $R$. Tensoring the kernels of multiplication by $\pi$ and by $\pi^2$ with $T$ therefore transfers the annihilator equality in $R$ to $T$. If $p_{k'\ell}=\pi t$, the equality $\pi p_{k'\ell}=0$ says $\pi^2t=0$, and hence $\pi t=0$. Thus every $p_{k'\ell}$ vanishes in $T$. The surjection $D_k\to D$ induces an isomorphism $T\simeq D_{\mathfrak q}$.

The Jacobian calculation for $T/R$ and the polynomial description (L3) now give the second and third assertions. Both annihilator hypotheses have been used explicitly: the one in $\Lambda$ constructs the actual target map, and the one in $R$ removes the remaining compatibility equations in the smooth local model. ∎

#### The desingularization lemma

A section known to order $\pi^4$ allows a strict Jacobian presentation to be replaced by equations with an invertible minor along $\pi=0$. The construction below also tracks the precise obstruction when the annihilators of $\pi$ and $\pi^2$ in the base are unequal.

#### Lemma. The desingularization lemma

Let $R$ be Noetherian, let $\Lambda$ be an $R$-algebra, and assume

$$\operatorname{Ann}_\Lambda(\pi)=\operatorname{Ann}_\Lambda(\pi^2)
\quad\text{for some }\pi\in R.$$

Suppose a finitely presented $R$-algebra $A$ maps to $\Lambda$, the image of $\pi$ is strictly standard for $A/R$, and there is an $R/\pi^4R$-algebra retraction

$$\rho:A/\pi^4A\longrightarrow R/\pi^4R$$

whose composite with $R/\pi^4R\to\Lambda/\pi^4\Lambda$ is the prescribed map from $A/\pi^4A$. Define

$$\mathfrak a=\operatorname{Ann}_R\bigl(
\operatorname{Ann}_R(\pi^2)/\operatorname{Ann}_R(\pi)\bigr).$$

Then the map $A\to\Lambda$ factors through a finitely presented $R$-algebra $B$ such that $\mathfrak aB\subseteq H_{B/R}$.

**Proof.** Choose a strict presentation $A=R[x_1,\ldots,x_n]/(f_1,\ldots,f_m)$ and its distinguished equations $f_1,\ldots,f_c$. Translate the $x_i$ by lifts of their images under $\rho$. Thus $\rho(x_i)=0$, the constant term of every $f_j$ belongs to $\pi^4R$, and the image of each $x_i$ in $\Lambda$ has the form $\pi^4\lambda_i$.

Write $r_{ji}$ for the coefficient of $x_i$ in $f_j$. Apply $\rho$ to the strict Jacobian identity expressing $\pi$ as a combination of the $c$-row minors. The resulting identity over $R/\pi^4R$ lifts to an identity over $R$ expressing $u\pi$ as a combination of the minors of $(r_{ji})$, for some $u\in1+\pi^3R$. The [adjugate calculation](#native-smoothing-lemma-parse-equation-strictly-standard-one) therefore gives an $n$-by-$c$ matrix $S=(s_{ik})$ satisfying

$$\sum_{i=1}^n r_{ji}s_{ik}=u\pi\delta_{jk}
\quad(1\leq j,k\leq c).$$

Introduce variables $v_1,\ldots,v_c,w_1,\ldots,w_n$ and substitute

$$x_i=\pi^2\sum_{k=1}^c s_{ik}v_k+\pi^3w_i.\tag{D1}$$

For $j\leq c$, the linear part of $f_j$ becomes $u\pi^3v_j+\pi^3\sum_i r_{ji}w_i$. Its constant term and every term of degree at least two are divisible by $\pi^4$. Consequently we can choose actual polynomials $g_j\in R[v,w]$ such that, after (D1),

$$f_j=\pi^3g_j,
\qquad g_j\equiv v_j+\sum_i r_{ji}w_i\pmod\pi.\tag{D2}$$

This is an identity obtained by factoring the displayed coefficients, so it does not require cancellation of $\pi$. Let $h_i=x_i-\pi^2\sum_k s_{ik}v_k-\pi^3w_i$ and put

$$B=R[x,v,w]/(f_1,\ldots,f_m,h_1,\ldots,h_n,g_1,\ldots,g_c).$$

The map $A\to B$ is induced by the $x$-coordinates. Define its prospective map to $\Lambda$ by

$$x_i\mapsto\pi^4\lambda_i,
\qquad v_j\mapsto0,
\qquad w_i\mapsto\pi\lambda_i.$$

The $f_j$ and $h_i$ vanish. By (D2), the image $t$ of each $g_j$ belongs to $\pi\Lambda$ and satisfies $\pi^3t=0$. The assumed equality of annihilators implies

$$\operatorname{Ann}_\Lambda(\pi^e)=\operatorname{Ann}_\Lambda(\pi)
\quad(e\geq1):$$

if $\pi^{e+1}z=0$, apply the equality for $\pi$ and $\pi^2$ to $\pi^{e-1}z$, then induct. Writing $t=\pi z$ now gives $\pi^4z=0$, hence $t=\pi z=0$. Thus $B\to\Lambda$ is well-defined.

Away from $\pi=0$, (D1) eliminates the $w_i$, and the equations $g_j$ follow from $f_j$. Hence $B_\pi\simeq A_\pi[v_1,\ldots,v_c]$. Strictness makes $A_\pi/R$ smooth by [Elkik's singularity-ideal criterion](#native-smoothing-lemma-elkik), so $B_\pi/R$ is smooth.

To work along $\pi=0$, let $B'=R[v,w]/(g_1,\ldots,g_c)$. The Jacobian matrix of these equations in the variables $v_j$ is the identity modulo $\pi$. The [Jacobian criterion](#native-algebra-lemma-standard-smooth) therefore shows that $B'/R$ is smooth at every prime containing $\pi$. The map $B'\to B$ is surjective, with kernel generated by the substituted equations $f_{c+1},\ldots,f_m$.

Take a prime $\mathfrak q\subset B$ containing $\pi$ and an element $r\in\mathfrak a$ outside $\mathfrak q$. Let $T$ be the local ring of $B'$ at the inverse image of $\mathfrak q$, and let $K\subseteq T$ be the ideal generated by those remaining equations. We will prove $K=0$.

Every substituted $f_j$ belongs to $\pi^2T$: its constant term lies in $\pi^4R$, and each substituted $x_i$ is divisible by $\pi^2$. The relation condition in the strict presentation says that $\pi f_{c+j}$ belongs to $(f_1,\ldots,f_c)+(f_1,\ldots,f_m)^2$. Since the first $c$ equations vanish in $T$ by (D2), we get

$$K\subseteq\pi^2T,
\qquad\pi K\subseteq K^2\subseteq\pi^2K.$$

The finite $T$-module $M=\pi K$ thus satisfies $M=\pi M$. Because $\pi$ is in the maximal ideal, [Nakayama's lemma](#native-algebra-lemma-nak) gives $\pi K=0$. Equivalently, one can iterate the last containment and use [Krull intersection](#native-algebra-lemma-intersect-powers-ideal-module-zero) in the Noetherian local ring $T$.

Smoothness makes $T$ flat over $R$. Hence

$$\bigl(\operatorname{Ann}_R(\pi^2)/\operatorname{Ann}_R(\pi)\bigr)\otimes_RT
\simeq\operatorname{Ann}_T(\pi^2)/\operatorname{Ann}_T(\pi).$$

The left side is zero because it is annihilated by $r$, which is a unit in $T$. Thus the annihilators in $T$ are equal, and their powers stabilize as above. For $f\in K$, write $f=\pi^2z$. Since $\pi f=0$, we have $\pi^3z=0$, hence $\pi z=0$ and $f=0$. This proves $K=0$.

We have shown that $B_{\mathfrak q}\simeq T$ is smooth over $R$ at every prime in $D(\mathfrak aB)$ lying over $\pi=0$, and we already proved smoothness away from $\pi=0$. Therefore $D(\mathfrak aB)$ is contained in the smooth locus, which is exactly the ideal containment $\mathfrak aB\subseteq H_{B/R}$. ∎

#### Lemma. Desingularization of a strict presentation

Let $R$ be Noetherian and let $\Lambda$ be an $R$-algebra. Suppose

$$\operatorname{Ann}_R(\pi)=\operatorname{Ann}_R(\pi^2),
\qquad\operatorname{Ann}_\Lambda(\pi)=\operatorname{Ann}_\Lambda(\pi^2).$$

Let $A,D$ be finitely presented $R$-algebras with maps to $\Lambda$. Assume $\pi$ is strictly standard in $A/R$ and there is a compatible $R$-algebra map $A/\pi^4A\to D/\pi^4D$. Then there are maps $A\to B$, $D\to B$, and $B\to\Lambda$, all compatible with the given target maps, such that $B/R$ is finitely presented and

$$H_{D/R}B\subseteq H_{B/D},
\qquad H_{D/R}B\subseteq H_{B/R}.$$

**Proof.** Use $D$ as the base ring and $A\otimes_RD$ as the algebra to which the preceding lemma is applied. The base $D$ is Noetherian, strictness survives [arbitrary base change](#native-smoothing-lemma-strictly-standard-base-change), and the prescribed map modulo $\pi^4$ defines a $D/\pi^4D$-algebra retraction

$$ (A\otimes_RD)/\pi^4(A\otimes_RD)\longrightarrow D/\pi^4D.$$

Multiplication of the two given maps into $\Lambda$ supplies the map from the tensor product. The compatibility hypothesis gives exactly the required compatibility of the retraction. The preceding lemma yields $A\otimes_RD\to B\to\Lambda$ and

$$\mathfrak bB\subseteq H_{B/D},\qquad
\mathfrak b=\operatorname{Ann}_D\bigl(
\operatorname{Ann}_D(\pi^2)/\operatorname{Ann}_D(\pi)\bigr).$$

If $D_{\mathfrak p}$ is flat over $R$, the equality of annihilators in $R$ transfers to $D_{\mathfrak p}$. The finite $D$-module inside the last annihilator is therefore zero after localization at $\mathfrak p$. Finiteness implies that some element outside $\mathfrak p$ annihilates it, so $\mathfrak b\nsubseteq\mathfrak p$. Every smooth prime of $D/R$ is such a flat prime. Thus every prime of $B$ above the smooth locus of $D/R$ belongs to the smooth locus of $B/D$. In ideal language this is the first asserted containment. Smooth maps compose, so the same primes are smooth for $B/R$, proving the second. Finite presentation over $R$ follows by composing the finite presentations over $D$ and over $R$. ∎

#### Lemma. Combining lifting with desingularization

Let $R$ be Noetherian and let $\Lambda$ be an $R$-algebra. Assume the annihilators of $\pi$ and $\pi^2$ agree both in $R$ and in $\Lambda$. Let $A/R$ be finitely presented, with a map to $\Lambda$, and suppose $\pi$ is strictly standard for $A/R$. Given a factorization

$$A/\pi^8A\longrightarrow\bar C\longrightarrow\Lambda/\pi^8\Lambda$$

through a finitely presented $(R/\pi^8R)$-algebra, there exists $A\to B\to\Lambda$ with $B/R$ finitely presented, $B_\pi/R_\pi$ smooth, and

$$H_{\bar C/(R/\pi^8R)}(\Lambda/\pi^8\Lambda)
\subseteq
\bigl(\sqrt{H_{B/R}\Lambda}+\pi^8\Lambda\bigr)/\pi^8\Lambda.$$

**Proof.** The annihilator equalities for $\pi$ imply those for all its positive powers, by the induction used in the preceding proof. Apply the [lifting lemma](#native-smoothing-lemma-lifting) with $\pi^4$ in place of its parameter. It gives a finitely presented $D/R$, a map $D\to\Lambda$, and compatible maps

$$\bar C/\pi^4\bar C\longrightarrow D/\pi^4D\longrightarrow\Lambda/\pi^4\Lambda.$$

The algebra $D$ is smooth over $R$ away from $\pi=0$, and it is smooth along the inverse image of the smooth locus of $\bar C/(R/\pi^8R)$. Compose the given map from $A$ with this diagram. The preceding strict-desingularization lemma then gives compatible maps $A\to B\to\Lambda$ and $D\to B\to\Lambda$, with $H_{D/R}B\subseteq H_{B/R}$. It follows immediately that $B_\pi/R_\pi$ is smooth.

For the remaining assertion, let $\eta\subset\Lambda$ contain $\pi$, and suppose its image in $\operatorname{Spec}\bar C$ is smooth over $R/\pi^8R$. The compatibility modulo $\pi^4$ and the lifting lemma show that its inverse image in $D$ is smooth over $R$. Therefore $H_{D/R}\Lambda\nsubseteq\eta$, and the containment just proved implies $H_{B/R}\Lambda\nsubseteq\eta$. This proves the required containment of smooth opens in $\operatorname{Spec}(\Lambda/\pi^8\Lambda)$, hence the corresponding radical containment of ideals.

To identify that radical with the right side displayed in the statement, note also that smoothness of $B_\pi/R_\pi$ implies $\pi\in H_{B/R}$. Thus $\pi^8\Lambda$ already lies in $H_{B/R}\Lambda$, and passage to the quotient commutes with taking the radical of this ideal. This gives precisely the stated formula. ∎

#### Reduction to the field case

We now reduce the global theorem to a regular algebra over a field. The two return steps matter: a smooth factorization over the total ring of fractions must first be expressed over the original base, and a factorization modulo a power of a nonzerodivisor must then be lifted back to that base.

#### Situation. The global desingularization problem

In this section $R\to\Lambda$ is a regular homomorphism between Noetherian rings. We write $\operatorname{PT}(R,\Lambda)$ for the assertion that $\Lambda$ is ind-smooth over $R$. Equivalently, every map to $\Lambda$ from a finitely presented $R$-algebra factors through a smooth $R$-algebra, by the [finite factorization criterion](#reader-section-2).

#### Lemma. Products of ind-smooth maps

For $i=1,2$, let $R_i\to\Lambda_i$ be regular maps of Noetherian rings satisfying $\operatorname{PT}(R_i,\Lambda_i)$. Then their product map satisfies $\operatorname{PT}(R_1\times R_2,\Lambda_1\times\Lambda_2)$.

**Proof.** Express $\Lambda_i$ as a filtered colimit of smooth $R_i$-algebras $B_{i,\alpha}$. Index the algebras $B_{1,\alpha}\times B_{2,\beta}$ by the product of the two indexing categories. This category is filtered: common targets and equalizers of parallel arrows can be chosen separately in its two factors. An element of the product of the two colimits comes from some pair of stages, and equality can also be checked at a pair of later stages. Thus the colimit is $\Lambda_1\times\Lambda_2$. Each stage is smooth over $R_1\times R_2$, because the two complementary idempotents split its spectrum into the two given smooth morphisms. This proves the assertion. ∎

#### Lemma. Returning from a localized base

Let $R\to A\to\Lambda$ be ring maps, with $A/R$ finitely presented, and let $S\subseteq R$ be multiplicative. Suppose $S^{-1}A\to C\to S^{-1}\Lambda$ factors the localized map and $C/S^{-1}R$ is smooth. Then $A\to\Lambda$ factors through a finitely presented $R$-algebra $B$ in which the image of some $s\in S$ is elementary standard.

**Proof.** Replace $C$ by a standard smooth algebra with a retraction to $C$, using the [standard presentation lemma](#native-smoothing-lemma-smooth-standard-smooth). Composing with that retraction preserves the required map to $S^{-1}\Lambda$. Present $A=R[x_1,\ldots,x_n]/(g_1,\ldots,g_t)$, and let $\lambda_i\in\Lambda$ be the images of its generators. The [prescribed-generators lemma](#native-smoothing-lemma-standard-smooth-include-generators) gives

$$C=(S^{-1}R)[x_1,\ldots,x_{n+m}]/(f_1,\ldots,f_c),\qquad c\geq n,$$

with the prescribed first $n$ images and with the minor $\Delta=\det(\partial f_j/\partial x_i)_{1\leq j,i\leq c}$ invertible in $C$.

For each additional variable, multiply it by a suitable element of $S$ so that its target image is represented by an element $\lambda_i\in\Lambda$. These changes of variables are invertible diagonal changes over $S^{-1}R$. Their scaling factors are base scalars, so their differentials relative to the base vanish; consequently the chosen Jacobian minor changes only by a unit. Clear the coefficients in the finitely many equations. Multiplying an equation by an element of $S$ again changes its Jacobian row only by a base unit. We now have $f_j\in R[x_1,\ldots,x_{n+m}]$ presenting $C$ after localization, with the indicated generator images.

The inverse of $\Delta$ in the localized quotient can be represented by a polynomial. Clear its coefficients and the coefficients of the finitely many equations witnessing this inverse. Clearing also any remaining equality in the localized polynomial ring gives polynomials $b_0,b_1,\ldots,b_c$ and $s_0\in S$ with

$$s_0=b_0\Delta+\sum_{j=1}^c b_jf_j.$$

Since each $g_\ell$ vanishes in $C$, choose $s_\ell\in S$ with $s_\ell g_\ell\in(f_1,\ldots,f_c)$ in the polynomial ring over $R$. Since each $f_j(\lambda)$ vanishes in $S^{-1}\Lambda$, choose $u_j\in S$ with $u_jf_j(\lambda)=0$ in $\Lambda$. Set

$$B=R[x_1,\ldots,x_{n+m}]/
(u_1f_1,\ldots,u_cf_c,g_1,\ldots,g_t).$$

Evaluation at the $\lambda_i$ gives a factorization $A\to B\to\Lambda$. Let

$$s=s_0\left(\prod_{\ell=1}^t s_\ell\right)
\left(\prod_{j=1}^c u_j\right)\in S.$$

The first $c$ equations of $B$ have minor $(\prod_j u_j)\Delta$. Multiplying the identity for $s_0$ by $\prod_j u_j$ and reducing in $B$ shows that $s$ is a multiple of this minor. Moreover, $sg_\ell\in(u_1f_1,\ldots,u_cf_c)$ for each $\ell$: multiply its earlier expression by the factors $u_j$, which supply every needed coefficient. These are the two conditions for $s$ to be elementary standard, with an even stronger relation containment than the definition requires. ∎

#### Lemma. Reducing desingularization to field bases

If $\operatorname{PT}(k,\Lambda)$ holds for every regular homomorphism from a field to a Noetherian ring, then $\operatorname{PT}(R,\Lambda)$ holds for every regular homomorphism of Noetherian rings.

**Proof.** Suppose a counterexample exists. For its fixed map $R\to\Lambda$, consider the ideals $I\subseteq R$ for which $R/I\to\Lambda/I\Lambda$ fails the assertion. Such quotient maps remain regular by [base change of regular maps](#native-more-algebra-lemma-regular-base-change). The ascending-chain condition supplies a maximal failing ideal. Replace the map by its quotient by that ideal. Now every quotient by a nonzero ideal satisfies the assertion.

The new base $R$ is reduced. Otherwise its nonzero nilradical is nilpotent, since $R$ is Noetherian, and the quotient by that ideal satisfies $\operatorname{PT}$. Flatness of the regular map and [nilpotent lifting](#native-smoothing-proposition-lift) would imply $\operatorname{PT}(R,\Lambda)$, a contradiction.

Let $S$ be the nonzerodivisors of this reduced Noetherian ring. Its total ring of fractions $S^{-1}R$ is a finite product of fields: there are finitely many minimal primes, no embedded associated primes in a reduced Noetherian ring, and localization at the nonzerodivisors gives their fraction fields. The precise algebraic statements are [the total quotient ring without embedded primes](#native-algebra-lemma-total-ring-fractions-no-embedded-points) and [finiteness of the irreducible components](#native-algebra-lemma-noetherian-irreducible-components). Localization preserves regularity. The assumed field case and the product lemma therefore give $\operatorname{PT}(S^{-1}R,S^{-1}\Lambda)$.

Take any finitely presented $A/R$ mapping to $\Lambda$. There is a smooth factorization after localization at $S$. The preceding return lemma replaces it by an actual factorization over $R$ whose intermediate algebra has an elementary standard element $\pi\in S$. We may replace $A$ by that intermediate algebra, since a smooth factorization of the new map will also factor the original one. Thus $\pi$ is strictly standard in $A/R$ and is a nonzerodivisor of $R$. It remains a nonzerodivisor of $\Lambda$, because $\Lambda/R$ is flat.

The ideal $(\pi^8)$ is nonzero unless $R=0$, whose conclusion is immediate. Hence maximality of the failing ideal gives $\operatorname{PT}(R/\pi^8R,\Lambda/\pi^8\Lambda)$. Factor the reduced map from $A/\pi^8A$ through a smooth algebra $\bar C$ over $R/\pi^8R$. Apply the [combined lifting and desingularization lemma](#native-smoothing-lemma-desingularize-lifting-apply). It gives $A\to B\to\Lambda$, with $B/R$ finitely presented and $B_\pi/R_\pi$ smooth, and its radical-ideal conclusion reads

$$\Lambda/\pi^8\Lambda
\subseteq\sqrt{H_{B/R}\Lambda}/\pi^8\Lambda,$$

because $\bar C$ is smooth everywhere. Thus $H_{B/R}\Lambda=\Lambda$. The [smooth factorization construction](#native-smoothing-lemma-final-solve) replaces $B$ by a smooth $R$-algebra still mapping to $\Lambda$. This factors every finite presentation into $\Lambda$ through a smooth algebra. The finite factorization criterion contradicts the assumed failure. ∎

#### Localization and descent of resolutions

The next arguments preserve two kinds of progress at once: they remove a specified prime from the nonsmooth locus, while retaining every point already known to be smooth. This second requirement explains the additional variables in the height-zero return construction.

#### Situation. The local desingularization problem

Fix a Noetherian ring $R$, a finitely presented $R$-algebra $A$, a map $A\to\Lambda$, and a prime $\mathfrak q\subset\Lambda$. No Noetherian hypothesis on $\Lambda$ is included in this setup. Put

$$\mathfrak h_A=\sqrt{H_{A/R}\Lambda}.$$

A **resolution at $\mathfrak q$** is a factorization $A\to B\to\Lambda$ with $B/R$ finitely presented and

$$\mathfrak h_A\subseteq\mathfrak h_B,
\qquad\mathfrak h_B\nsubseteq\mathfrak q.$$

Thus the smooth open in the target grows, and the new open contains $\mathfrak q$. The word resolution here refers to this factorization property, not to a proper birational resolution of a variety.

#### Lemma. Lifting a local desingularization solution

In the local setup, let $r\geq1$ and choose $\pi_1,\ldots,\pi_r\in R$ mapping into $\mathfrak q$. Assume each $\pi_i$ is strictly standard for $A/R$. For each $i$, assume also that the annihilators of $\pi_i$ and $\pi_i^2$ agree both in

$$R/(\pi_1^8,\ldots,\pi_{i-1}^8)R
\quad\text{and in}\quad
\Lambda/(\pi_1^8,\ldots,\pi_{i-1}^8)\Lambda.$$

If the induced local problem modulo $(\pi_1^8,\ldots,\pi_r^8)$ admits a resolution, then the original local problem admits a resolution.

**Proof.** Consider first one element $\pi$. Let $A/\pi^8A\to\bar C\to\Lambda/\pi^8\Lambda$ be a resolving factorization. The [combined lifting lemma](#native-smoothing-lemma-desingularize-lifting-apply) supplies $A\to B\to\Lambda$, with $B_\pi/R_\pi$ smooth and with the image of $H_{\bar C/(R/\pi^8R)}$ contained in the reduction of $\mathfrak h_B$. Since the reduced factorization resolves the selected prime, this containment gives $\mathfrak h_B\nsubseteq\mathfrak q$.

It also retains the original smooth locus. Smoothness is preserved by base change, so the reduction of $H_{A/R}$ belongs to $H_{(A/\pi^8A)/(R/\pi^8R)}$. The resolving property of $\bar C$ and the radical containment therefore place its target image inside $\mathfrak h_B$ modulo $\pi^8$. Since $B_\pi$ is smooth, $\pi\in H_{B/R}$; thus this containment lifts to $H_{A/R}\Lambda\subseteq\mathfrak h_B$. Taking radicals gives $\mathfrak h_A\subseteq\mathfrak h_B$, as required.

For several elements, first apply induction to the last $r-1$ elements over $R/\pi_1^8R$. The stated annihilator conditions are precisely those needed for this quotient setup, and strictness survives arbitrary base change. We obtain a resolution modulo $\pi_1^8$, to which the one-element argument applies. ∎

#### Lemma. Returning from a localized target

In the local setup, set $\mathfrak p=\mathfrak q\cap R$. Suppose $\mathfrak q$ is minimal over $\mathfrak h_A$ and the localized problem

$$R_{\mathfrak p}\longrightarrow A_{\mathfrak p}
\longrightarrow\Lambda_{\mathfrak q}$$

admits a resolution at its maximal ideal. Then $A\to\Lambda$ factors through a finitely presented $R$-algebra $B$ for which $H_{B/R}\Lambda\nsubseteq\mathfrak q$. This conclusion alone does not assert $\mathfrak h_A\subseteq\mathfrak h_B$.

**Proof.** In the local target, a resolving algebra has singularity ideal generating the unit ideal: an ideal avoiding the maximal ideal contains a unit. The [smooth factorization lemma](#native-smoothing-lemma-final-solve) therefore replaces it by a smooth $R_{\mathfrak p}$-algebra. The standard presentation lemma and the prescribed-generators lemma further give a factorization through

$$C=R_{\mathfrak p}[x_1,\ldots,x_n,y_1,\ldots,y_m]/(f_1,\ldots,f_c),$$

where $A=R[x_1,\ldots,x_n]/(g_1,\ldots,g_t)$, the first $n$ generators retain their given images, and a specified $c$-by-$c$ minor is invertible in $C$. Clearing base denominators makes the $f_j$ polynomials over $R$. Choose $s_0\notin\mathfrak p$ so that this minor is invertible in their quotient after inverting $s_0$. For each $g_\ell$, choose $s_\ell\notin\mathfrak p$ with $s_\ell g_\ell\in(f_1,\ldots,f_c)$.

Write the target images of the $y_i$ with one common denominator $\delta\in\Lambda\setminus\mathfrak q$, say $y_i\mapsto\nu_i/\delta$. Homogenize each $f_j(x,y)$ in the $y$-variables, using one extra variable $w$: let $F_j(x,Y,w)$ have degree $d_j$ in $(Y,w)$ and satisfy $F_j(x,y,1)=f_j(x,y)$. If $\lambda_i$ are the given images of $x_i$, then

$$F_j(\lambda,\nu,\delta)
=\delta^{d_j}f_j(\lambda,\nu/\delta)=0
\quad\text{in }\Lambda_{\mathfrak q}.$$

There is a single $\epsilon\notin\mathfrak q$ annihilating all these finitely many values in $\Lambda$. Define

$$B=R[x_1,\ldots,x_n,Y_1,\ldots,Y_m,w,u]/
(g_1,\ldots,g_t,uF_1,\ldots,uF_c).$$

It receives $A$ and maps to $\Lambda$ by $x_i\mapsto\lambda_i$, $Y_i\mapsto\nu_i$, $w\mapsto\delta$, and $u\mapsto\epsilon$. Set $s=s_0s_1\cdots s_t$ and $b=suw\in B$. Its image avoids $\mathfrak q$.

After inverting $b$, all three factors $s,u,w$ are units. Use the coordinates $y_i=Y_i/w$ to remove the homogenization factors, which are powers of $w$. The equations $g_\ell$ are redundant because $s_\ell$ is invertible. We obtain the explicit isomorphism

$$B_b\simeq
\bigl(R_s[x,y]/(f_1,\ldots,f_c)\bigr)[u,u^{-1},w,w^{-1}].$$

The algebra inside parentheses is standard smooth by the choice of $s_0$, and adjoining two invertible variables preserves smoothness. Hence $b\in H_{B/R}$, proving the claimed avoidance of $\mathfrak q$. ∎

#### Lemma. Returning from a height-zero localization

In the local setup, assume $\mathfrak q$ is minimal over $\mathfrak h_A$, the localized problem over $R_{\mathfrak p}\to\Lambda_{\mathfrak q}$ admits a resolution, and $\dim\Lambda_{\mathfrak q}=0$. Then the original problem admits a resolution.

**Proof.** Since $A$ is Noetherian, choose finite generators $a_1,\ldots,a_r$ of $H_{A/R}$. Their images lie in $\mathfrak q$. A zero-dimensional local ring has only its maximal ideal as a prime, so that maximal ideal is its nilradical. Each $a_i/1$ is consequently nilpotent in $\Lambda_{\mathfrak q}$. Choose a common positive power $N$ killing these finitely many elements there, and then choose $\lambda\notin\mathfrak q$ with

$$\lambda a_i^N=0\quad\text{in }\Lambda\quad(1\leq i\leq r).$$

This uses only finitely many nilpotent elements; it does not require $\Lambda_{\mathfrak q}$ to be Artinian.

The preceding lemma gives $A\to C\to\Lambda$, with $C/R$ finitely presented, and $c\in H_{C/R}$ whose target image avoids $\mathfrak q$. Choose a finite relative presentation $C=A[x_1,\ldots,x_n]/(f_1,\ldots,f_m)$. Form

$$B=A[x_1,\ldots,x_n,y_1,\ldots,y_r,z,(t_{ij})]/
\bigl(f_j-\sum_{i=1}^r y_it_{ij},\ zy_i\bigr).$$

The map to $\Lambda$ sends the $x$-coordinates through $C$, sends $t_{ij}$ to zero, sends $y_i$ to the image of $a_i^N$, and sends $z$ to $\lambda$. The identities just chosen make this well-defined.

Inverting $z$ forces all the $y_i$ to zero, so

$$B_z\simeq C[z,z^{-1},(t_{ij})].$$

Choose a polynomial in the original variables $A[x_1,\ldots,x_n]$ representing $c$, and denote its image in $B$ by $\widetilde c$. Under the displayed isomorphism it is precisely the coefficient $c\in C$, and its image in $\Lambda$ is the given image of $c$. Thus $B_{z\widetilde c}$ is smooth over $R$, and the image of $z\widetilde c$ in $\Lambda$ avoids $\mathfrak q$.

On the other hand, after inverting $y_\ell$, the equation $zy_\ell=0$ gives $z=0$, and the remaining relations solve uniquely for all $t_{\ell j}$. Thus $B_{y_\ell}$ is a polynomial algebra over $A$ with $y_\ell$ inverted. After also inverting $a_\ell$, it is smooth over $R$. Hence $a_\ell y_\ell\in H_{B/R}$. Its image in $\Lambda$ is $a_\ell^{N+1}$, showing $a_\ell\in\mathfrak h_B$ for every $\ell$. Therefore $\mathfrak h_A\subseteq\mathfrak h_B$. The element $z\widetilde c$ shows $\mathfrak h_B\nsubseteq\mathfrak q$, so this factorization is a resolution. ∎

#### Separable residue fields

At a regular local target with separable residue field, a system of parameters reduces the resolution problem to a nilpotent thickening of that field. Before making this reduction, we must choose representatives of the parameters whose annihilator properties hold in the original ring, not only in its localization.

#### Lemma. The annihilator stabilization step (Ogoma)

Let $M$ be finite over a Noetherian ring $A$, let $S\subseteq A$ be multiplicative, and let $\pi\in A$. Assume multiplication by $\pi$ and by $\pi^2$ have the same kernel on $S^{-1}M$. There exists $s\in S$ such that, for every $n\geq1$, multiplication by $s^n\pi$ and by $(s^n\pi)^2$ have the same kernel on $M$.

**Proof.** Let $K$ be the kernel of multiplication by $\pi$ on $M$, and let $K'$ be the inverse image in $M$ of the kernel of multiplication by $\pi^2$ on $S^{-1}M$. The assumption says $(K'/K)_S=0$. This quotient is finite, since it is a quotient of submodules of the finite module $M$ over a Noetherian ring. Some $s\in S$ therefore annihilates $K'/K$.

Fix $n\geq1$ and suppose $s^{2n}\pi^2m=0$. After localization, $s$ is a unit, so $m\in K'$. Our choice of $s$ gives $sm\in K$, hence $s\pi m=0$. Multiplying by $s^{n-1}$ gives $s^n\pi m=0$. The converse implication follows by multiplying once more by $s^n\pi$. Thus this single choice of $s$ works for every $n$. ∎

#### Lemma. Parameters adapted to the singularity ideal

Let $\Lambda$ be Noetherian, let $I\subseteq\mathfrak q\subset\Lambda$ with $\mathfrak q$ prime, and suppose $\Lambda_{\mathfrak q}$ is a regular local ring of dimension $d$. Given positive integers $n,e$ such that $\mathfrak q^n\Lambda_{\mathfrak q}\subseteq I\Lambda_{\mathfrak q}$, one can choose $\pi_1,\ldots,\pi_d\in\Lambda$ with

$$\mathfrak q\Lambda_{\mathfrak q}=(\pi_1,\ldots,\pi_d)\Lambda_{\mathfrak q},
\qquad \pi_i^n\in I,$$

and, for each $i$, with equal annihilators of $\pi_i$ and $\pi_i^2$ in $\Lambda/(\pi_1^e,\ldots,\pi_{i-1}^e)\Lambda$.

**Proof.** Choose a regular system of parameters in $\Lambda_{\mathfrak q}$ and clear the denominators of its finitely many entries to obtain representatives in $\Lambda$. Multiplying an entry by an element outside $\mathfrak q$ does not change the parameter ideal in the localization. The hypothesis on $I$ allows such a multiplication for each entry so that its $n$th power belongs to $I$: if $s\pi_i^n\in I$, replace $\pi_i$ by $s\pi_i$ and use $s^n\pi_i^n\in I$.

Now adjust the entries successively. Suppose entries before $i$ have already been fixed. A regular local ring is Cohen–Macaulay, and powers of the initial terms of a regular sequence remain regular; see [regular rings](#native-algebra-lemma-regular-ring-cm) and [powers of regular sequences](#native-algebra-lemma-regular-sequence-powers). Thus $\pi_i$ is a nonzerodivisor on

$$\Lambda_{\mathfrak q}/(\pi_1^e,\ldots,\pi_{i-1}^e)\Lambda_{\mathfrak q}.$$

Apply Ogoma's lemma to the finite module $\Lambda/(\pi_1^e,\ldots,\pi_{i-1}^e)\Lambda$, with $S=\Lambda\setminus\mathfrak q$. Multiplying $\pi_i$ by the resulting element of $S$ gives the desired annihilator equality before localization. Its $n$th-power containment persists, as does the parameter ideal. Earlier equalities are unaffected because their quotient ideals involve only earlier entries. After $d$ steps all the requirements hold. For $d=0$ the empty sequence satisfies them. ∎

#### Lemma. Desingularization with separable residue fields

Let $k\to A\to\Lambda$ be maps with $k$ a field, $A/k$ finitely presented, and $\Lambda$ Noetherian. Suppose $\mathfrak q$ is minimal over $\sqrt{H_{A/k}\Lambda}$, the local ring $\Lambda_{\mathfrak q}$ is regular, and $\kappa(\mathfrak q)/k$ is separable. Then the local desingularization problem at $\mathfrak q$ admits a resolution.

**Proof.** Set $d=\dim\Lambda_{\mathfrak q}$. If $d=0$, the localized target is the separable field extension $\kappa(\mathfrak q)/k$. Such an extension is ind-smooth over $k$, as in [the field case of the smooth-colimit criterion](#native-algebra-lemma-colimit-syntomic). A map from the finite presentation $A$ therefore factors through a smooth algebra after localization. The [height-zero return lemma](#native-smoothing-lemma-delocalize-height-zero) gives a resolution before localization.

Assume $d>0$, and choose generators $a_1,\ldots,a_r$ of $H_{A/k}$. Put $I=H_{A/k}\Lambda$. Minimality of $\mathfrak q$ means that $I\Lambda_{\mathfrak q}$ has radical the maximal ideal. Since the local ring is Noetherian, choose $n\geq1$ with

$$\mathfrak q^n\Lambda_{\mathfrak q}\subseteq I\Lambda_{\mathfrak q}.$$

Using the actual ideal $I$ here will ensure expressions in the generators $a_j$, rather than only membership in their radical.

Let $R=k[x_1,\ldots,x_d]$ and define an $R$-algebra

$$B=A[x_1,\ldots,x_d,(z_{ij})]/
\bigl(x_i^n-\sum_{j=1}^r z_{ij}a_j:1\leq i\leq d\bigr).$$

On $D(a_j)$ one can eliminate $z_{ij}$ for each $i$, leaving a polynomial algebra over $A_{a_j}\otimes_kR$. It is smooth over $R$, since $A_{a_j}/k$ is smooth. The opens $D(a_j)$ cover $D(x_i)$, by the displayed relations. Hence $B_{x_i}/R$ is smooth for every $i$.

Apply [improvement of presentations](#native-smoothing-lemma-improve-presentation) to obtain $B\to C\to B$ with composite the identity. Since $R$ is Noetherian, $C/R$ is finitely presented. Each $C_{x_i}/R$ is smooth with free differentials. The strict part of the [comparison lemma](#native-smoothing-lemma-compare-standard) supplies a common $c\geq1$ such that every $x_i^c$ is strictly standard for $C/R$.

Apply the parameter lemma with the ideal $I$, the chosen $n$, and exponent $e=8c$. We obtain $\pi_1,\ldots,\pi_d\in\Lambda$ forming a parameter system after localization, with $\pi_i^n\in I$ and the required successive annihilator equalities. Choose coefficients $\lambda_{ij}$ with $\pi_i^n=\sum_j\lambda_{ij}a_j$ in $\Lambda$. Sending $x_i\mapsto\pi_i$ and $z_{ij}\mapsto\lambda_{ij}$ gives $B\to\Lambda$. Compose with the augmentation $C\to B$ to get the map from $C$.

The [successive lifting lemma](#native-smoothing-lemma-lift-solution), applied over $R$ to the parameters $x_i^c$, reduces the problem for $C$ to its quotient by $(x_1^e,\ldots,x_d^e)$. In the polynomial base the required elements are nonzerodivisors in the successive quotients, since each new variable is independent of its predecessors. In $\Lambda$ the parameter lemma gives the equalities for $\pi_i$ modulo the preceding $e$th powers, and stabilization of annihilators gives those for $\pi_i^c$ as well.

We verify that the quotient problem can be resolved. Write $\mathfrak p=(x_1,\ldots,x_d)\subset R$. Its local ring is regular, and the images of its parameters form a regular sequence in $\Lambda_{\mathfrak q}$. The [flatness criterion over a regular local ring](#native-algebra-lemma-flat-over-regular) makes $R_{\mathfrak p}\to\Lambda_{\mathfrak q}$ flat. Therefore

$$R_{\mathfrak p}/(x_1^e,\ldots,x_d^e)
\longrightarrow
\Lambda_{\mathfrak q}/(\pi_1^e,\ldots,\pi_d^e)$$

is a flat map of Artinian local rings. Reducing by the maximal ideal of its base gives precisely the separable extension $k\to\kappa(\mathfrak q)$, since the $\pi_i$ generate the localized maximal ideal. The base maximal ideal is nilpotent. The field smooth-colimit criterion followed by [nilpotent lifting](#native-smoothing-proposition-lift) therefore makes this Artinian target ind-smooth over that base. This supplies a smooth factorization of the localized quotient problem.

The selected prime in the quotient target has height zero, because the localized quotient is Artinian. If it is already outside the singularity ideal of the quotient of $C$, the identity factorization resolves it. Otherwise its height-zero property makes it minimal over that ideal, and the height-zero return lemma applies to the smooth localized factorization just obtained. In either case the quotient problem is resolved. Successive lifting now yields $C\to D\to\Lambda$ resolving the problem over $R$.

Finally this also resolves the original problem over $k$. Indeed $C_{a_j}/R$ is smooth: $B_{a_j}/R$ is smooth, and the improvement construction is smooth over $B$ there. Hence the images of all the $a_j$ belong to $H_{C/R}\Lambda$. The resolution over $R$ retains their radical and avoids $\mathfrak q$. As $R/k$ is a polynomial algebra, composition of smooth maps gives $H_{D/R}\subseteq H_{D/k}$. Thus

$$\sqrt{H_{A/k}\Lambda}\subseteq\sqrt{H_{D/k}\Lambda},
\qquad H_{D/k}\Lambda\nsubseteq\mathfrak q.$$

Together with $A\to B\to C\to D\to\Lambda$, these are the required conclusions. ∎

#### Inseparable residue fields

In positive characteristic, the residue field need not be separable over the ground field, even for a geometrically regular local algebra. The construction therefore first captures the required infinitesimal data in a finite-dimensional local algebra. The key finiteness hypothesis concerns the first homology of the cotangent complex of the residue extension.

#### Lemma. Compatibility of the local approximation data

Let $k$ have characteristic $p>0$, and let $(\Lambda,\mathfrak m,K)$ be an Artinian local $k$-algebra. Suppose $H_1(L_{K/k})$ is finite-dimensional over $K$. Then $\Lambda$ is a filtered colimit of local Artinian $k$-algebras $A$ essentially of finite type over $k$, with $A\to\Lambda$ flat and $\mathfrak m_A\Lambda=\mathfrak m$. The maps can be taken to be inclusions, so this is a directed union of subalgebras. In particular, any finite subset of $\Lambda$ is contained in one such $A$.

**Proof.** Choose generators $\lambda_1,\ldots,\lambda_d$ of $\mathfrak m$, and let $n$ be the least positive integer with $\mathfrak m^n=0$. Every field of characteristic $p$ is formally smooth over its prime field, by [formal smoothness over a perfect field](#native-algebra-lemma-formally-smooth-extensions-easy). Thus the residue map admits a coefficient-field section $\sigma:K\to\Lambda$. Such a section is an $\mathbf F_p$-algebra map; it need not respect the given $k$-algebra structure.

For a chosen section, evaluation gives a surjection

$$\Psi_\sigma:K[x_1,\ldots,x_d]\longrightarrow\Lambda,
\qquad x_i\longmapsto\lambda_i.$$

Surjectivity follows by successively expressing an element modulo $\mathfrak m$, then modulo $\mathfrak m^2$, and so on, using coefficients from $\sigma(K)$. Nilpotence makes this a finite procedure.

We claim that one can choose $\sigma$ and a finitely generated subextension $k\subseteq F\subseteq K$ such that the image of the given map $k\to\Lambda$ is contained in $\Psi_\sigma(F[x])$. This is the step that retains the actual $k$-structure. We prove it by induction on $n$. For $n=1$, use $\Lambda=K$ and $F=k$.

For $n>1$, set $J=\mathfrak m^{n-1}$ and $\Lambda'=\Lambda/J$. By induction choose a coefficient section $\sigma':K\to\Lambda'$ and a finite subextension $F'/k$ whose polynomial image contains the image of $k$. Let $A'$ denote that polynomial image, with induced map $\tau':k\to A'$. Lift $\sigma'$ to a coefficient section $\sigma:K\to\Lambda$. The truncated polynomial algebra

$$T=F'[x_1,\ldots,x_d]/(x_1,\ldots,x_d)^n$$

maps to $\Lambda$, and its composite onto $A'$ has nilpotent kernel: on residue fields it is the inclusion of $F'$ in $K$, so its kernel is contained in the nilpotent ideal generated by the $x_i$. Formal smoothness of $k/\mathbf F_p$ lifts $\tau'$ to a map $\tau:k\to T$.

Let $i:k\to\Lambda$ be the given structure map. The two maps $i$ and $\Psi_\sigma\tau$ agree modulo $J$. Their difference

$$\theta=i-\Psi_\sigma\tau:k\longrightarrow J$$

is therefore a derivation, with the $k$-action on $J$ given through its residue field. Here $\mathfrak mJ=0$ and $J^2=0$.

The [Jacobi–Zariski sequence for fields](#native-more-algebra-lemma-transitivity-gamma), using formal smoothness over $\mathbf F_p$, gives the exact sequence

$$0\longrightarrow H_1(L_{K/k})
\longrightarrow\Omega_{k/\mathbf F_p}\otimes_kK
\longrightarrow\Omega_{K/\mathbf F_p}
\longrightarrow\Omega_{K/k}\longrightarrow0.$$

Choose a basis $\{\mathrm dy_j:j\in S\}$ of $\Omega_{k/\mathbf F_p}$ from its generating differentials. The finite-dimensional kernel in this sequence is contained in the span of finitely many of these basis vectors, indexed by $S_0\subset S$. The images of the remaining $\mathrm dy_j$ in $\Omega_{K/\mathbf F_p}$ are linearly independent over $K$: a relation would lie both in their span and in the span indexed by $S_0$.

Extend this independent set to a basis of $\Omega_{K/\mathbf F_p}$ and choose a $K$-linear map to $J$ taking $\mathrm dy_j$ to $\theta(y_j)$ for $j\notin S_0$. It corresponds to a derivation $D:K\to J$. Since $J^2=0$, $\sigma+D$ is again a coefficient-field section. This change replaces $\theta$ by $\theta-D|_k$. Indeed, only the constant term of $\tau(a)$ contributes to the change: every positive-degree monomial maps into $\mathfrak m$, which annihilates $J$. The residue of that constant term is $a$.

After making this change, $\theta$ vanishes on every $y_j$ outside $S_0$. Thus it is determined by the finitely many elements $\theta(y_j)\in J$ for $j\in S_0$. The degree-$n-1$ monomials in the $\lambda_i$ span $J$ over $K$, so write these elements as finite linear combinations of those monomials. Adjoin their finitely many coefficients to $F'$, obtaining $F$. Every value $\theta(a)$ then belongs to $\Psi_\sigma(F[x])$, as do all values of $\Psi_\sigma\tau$. This proves the claim for the actual map $i$.

Fix such a section $\sigma$. The kernel of $\Psi_\sigma$ is finitely generated, since $K[x]$ is Noetherian. Choose generators $g_1,\ldots,g_t$, including all degree-$n$ monomials if needed, and enlarge $F$ to contain their coefficients. For every further finitely generated intermediate field $F\subseteq F_1\subseteq K$, set

$$A_{F_1}=F_1[x_1,\ldots,x_d]/(g_1,\ldots,g_t).$$

Extension of scalars identifies $K\otimes_{F_1}A_{F_1}$ with $\Lambda$. Hence $A_{F_1}\to\Lambda$ is faithfully flat and injective. All the $g_j$ have zero constant term, and the ideal $(x_1,\ldots,x_d)$ is nilpotent. Thus $A_{F_1}$ is local Artinian with residue field $F_1$, and its maximal ideal generates $\mathfrak m$ in $\Lambda$. The claim shows that its image contains the given image of $k$, making it a $k$-subalgebra.

For completeness, its finite-type assertion uses this actual $k$-structure, not the possibly different embedding of $k$ in the coefficient field. Choose finitely many elements of $A_{F_1}$ lifting field generators of $F_1/k$, and adjoin the images of $x_1,\ldots,x_d$. Localize the resulting finitely generated $k$-subalgebra at the inverse image of the maximal ideal of $A_{F_1}$. Its residue map is onto $F_1$. For any element of $A_{F_1}$, subtract an element of this local subalgebra with the same residue. The difference is a combination of the $x_i$. Replace its finitely many coefficients in the same way and repeat. After $n$ repetitions the remaining error is zero. Therefore this local subalgebra surjects onto $A_{F_1}$, proving that $A_{F_1}$ is essentially of finite type over $k$. This is the finite nilpotent-expansion argument behind [the Artinian finite-type criterion](#native-algebra-lemma-essentially-of-finite-type-into-artinian-local).

Finally, the finitely generated fields $F_1$ containing the fixed $F$ form a directed family: use their compositum for a common enlargement. Every element of $\Lambda$ has a polynomial expression in the $\lambda_i$ with finitely many coefficients from $K$, so it belongs to one of these subalgebras. Their union is $\Lambda$, completing the proof. ∎

#### Lemma. A factorization modulo a prescribed ideal

Let $k$ be a field of characteristic $p>0$, let $\Lambda$ be a Noetherian geometrically regular $k$-algebra, and let $\mathfrak q\subset\Lambda$ be prime. For every $n\geq1$ and finite subset $E\subset\Lambda_{\mathfrak q}/\mathfrak q^n\Lambda_{\mathfrak q}$ there is a map

$$\varphi:P=k[y_1,\ldots,y_m]\longrightarrow\Lambda$$

for some $m\geq0$ with the following properties. If $\mathfrak p=\varphi^{-1}(\mathfrak q)$, then $P_{\mathfrak p}\to\Lambda_{\mathfrak q}$ is flat and $\mathfrak p\Lambda_{\mathfrak q}=\mathfrak q\Lambda_{\mathfrak q}$. There is a factorization of local Artinian rings

$$P_{\mathfrak p}/\mathfrak p^nP_{\mathfrak p}
\longrightarrow D\longrightarrow
\Lambda_{\mathfrak q}/\mathfrak q^n\Lambda_{\mathfrak q}$$

in which the first map is essentially smooth, the second is flat, and the image of $D$ contains $E$.

**Proof.** Put $L=\Lambda_{\mathfrak q}/\mathfrak q^n\Lambda_{\mathfrak q}$ and $K=\kappa(\mathfrak q)$. We first establish a coefficient-enlargement fact, independently of the desired polynomial factorization.

Suppose $A\subset L$ is local Artinian, $A\to L$ is flat, and $\mathfrak m_AL=\mathfrak m_L$. Given a unit $u\in L$, there is an essentially smooth local Artinian extension $A\to A'\subset L$ such that $A'\to L$ remains flat, $\mathfrak m_{A'}L=\mathfrak m_L$, and $u^q\in A'$ for some integer $q>0$. Write $F$ for the residue field of $A$ and $\alpha$ for the residue of $u$.

If $\alpha\in F$, choose a unit $x\in A$ whose residue is $\alpha^{-1}$. Then $xu=1+v$ with $v$ nilpotent. For a power $q=p^r$ at least the nilpotence order, $(1+v)^q=1$. Hence $u^q=x^{-q}\in A$, and no extension is necessary.

If $\alpha$ is transcendental over $F$, use

$$A'=A[t]_{\mathfrak m_AA[t]},\qquad t\longmapsto u.$$

This map to $L$ is defined because every inverted polynomial has nonzero residue at the transcendental element $\alpha$. The ring $A'$ is local Artinian with residue field $F(\alpha)$, and it is essentially smooth over $A$. The [Noetherian fibrewise flatness criterion](#native-algebra-lemma-criterion-flatness-fibre-noetherian), applied to $A\to A'\to L$ and the finite $L$-module $L$, proves $L$ flat over $A'$: it is flat over $A$ by assumption, and its closed fibre $K$ is flat over the field $F(\alpha)$. The map is local, hence faithfully flat and injective. This identifies $A'$ with a subring of $L$ containing $u$, so take $q=1$.

If $\alpha$ is algebraic over $F$, its irreducible polynomial has the form $h(T^{p^r})$ with $h'\ne0$. Thus $\alpha^{p^r}$ is separable over $F$. Since Artinian local rings are henselian, lift the finite separable residue extension $F(\alpha^{p^r})/F$ to a finite étale local $A$-algebra $A'$, and lift its residue embedding into $K$ to a map $A'\to L$. These are the [henselian lifting](#native-algebra-lemma-local-dimension-zero-henselian) and [finite étale classification](#native-algebra-lemma-henselian-cat-finite-etale) statements. The same fibrewise flatness criterion shows this local map is faithfully flat. Apply the first case to $u^{p^r}$ and this enlarged coefficient ring to obtain a further power lying in $A'$. In all three cases $\mathfrak m_{A'}=\mathfrak m_AA'$, so the asserted maximal-ideal equality is preserved. This proves the enlargement fact. Successive enlargements handle any finite list of units.

Geometric regularity gives an injection $H_1(L_{K/k})\to\mathfrak q\Lambda_{\mathfrak q}/\mathfrak q^2\Lambda_{\mathfrak q}$, by the [cotangent criterion](#native-more-algebra-proposition-characterization-geometrically-regular). In particular this homology is finite-dimensional. Choose representatives $\tau_1,\ldots,\tau_d\in\Lambda$ of a regular system of parameters of $\Lambda_{\mathfrak q}$, clearing denominators if necessary. Apply the [Artinian approximation lemma](#native-smoothing-lemma-helper) to a finite subset consisting of $E$ and the images of these representatives. We obtain a local Artinian $k$-subalgebra $A\subset L$, essentially of finite type, flatly embedded, with $\mathfrak m_AL=\mathfrak m_L$. Let $F$ be its residue field.

We next choose the polynomial coordinates in $\Lambda$ itself. Choose elements $b_1,\ldots,b_t\in A$ whose residues have differentials forming an $F$-basis of $\Omega_{F/k}$. Express each image in $L$ as $\ell_i/s_i$ with $\ell_i,s_i\in\Lambda$ and $s_i\notin\mathfrak q$. Apply the enlargement fact to the finitely many units represented by the $s_i$. This yields $A'\subset L$ containing powers $s_i^{q_i}$ and hence containing the images of the global elements

$$v_i=\ell_i s_i^{q_i-1}\in\Lambda.$$

It is still essentially of finite type over $k$, since each enlargement is essentially smooth and therefore essentially of finite type, and it still contains $E$ and the parameter images. Write $F'$ for its residue field. In each transcendental enlargement the new residue-field differential is that of the adjoined global unit; in each finite separable enlargement no new relative differential is needed. It follows that $\Omega_{F'/k}$ is generated by the old $\mathrm db_i$ and the differentials of the adjoined powers of the $s_i$. Since in $F'$ we have $v_i=b_i s_i^{q_i}$, the identity

$$\mathrm dv_i=s_i^{q_i}\mathrm db_i+b_i\,\mathrm d(s_i^{q_i})$$

and invertibility of $s_i^{q_i}$ show that it is generated by differentials of finitely many global elements of $\Lambda$ whose images belong to $A'$. Select a subset whose differentials form a basis. Denote these global elements by $\lambda_1,\ldots,\lambda_a$.

Apply [geometric regularity over a field](#native-more-algebra-lemma-geometrically-regular-over-field) to these elements and the finite subextension $F'/k$ of $K$. For

$$P'=k[y_1,\ldots,y_a],\qquad y_i\mapsto\lambda_i,$$

and $\mathfrak p'=(P'\to\Lambda)^{-1}(\mathfrak q)$, the map $P'_{\mathfrak p'}\to\Lambda_{\mathfrak q}$ is flat with regular closed fibre. Its proof also shows that a regular system of parameters of $P'_{\mathfrak p'}$ maps to part of one for $\Lambda_{\mathfrak q}$. Complete it by a suitable subset of the $\tau_i$: their images generate the maximal ideal, so a subset supplies a basis of the remaining cotangent space. Adjoin these selected $\tau_i$ as further polynomial coordinates. The resulting $P\to\Lambda$ has $\mathfrak p\Lambda_{\mathfrak q}=\mathfrak q\Lambda_{\mathfrak q}$, and a parameter system of the regular local ring $P_{\mathfrak p}$ maps to a parameter system of $\Lambda_{\mathfrak q}$. The [regular-local flatness criterion](#native-algebra-lemma-flat-over-regular) proves the required flatness. All its coordinate images in $L$ belong to $A'$.

Consequently $Q=P_{\mathfrak p}/\mathfrak p^nP_{\mathfrak p}$ maps to $A'$: elements outside $\mathfrak p$ have nonzero residue and are units there, while $\mathfrak p^n$ vanishes in $L$ and hence in its subring $A'$. The map $Q\to L$ is flat, by the flatness just proved and the equality of the extended maximal ideals. Since $A'\to L$ is faithfully flat, [descent of flatness](#native-algebra-lemma-flatness-descends-more-general) gives $A'/Q$ flat.

Moreover $\mathfrak m_QA'=\mathfrak m_{A'}$: both ideals become $\mathfrak m_L$ after the faithfully flat extension. The extension $F'/\kappa(\mathfrak p)$ is finitely generated and has zero differentials, since the selected coordinates span $\Omega_{F'/k}$ and the additional parameter coordinates have residue zero. The [field differential criterion](#native-more-algebra-lemma-cartier-equality) makes it finite separable. Lifting a finite basis of this residue extension generates $A'$ as a $Q$-module: subtract a linear combination modulo $\mathfrak m_Q$, then repeat on the coefficients; nilpotence of $\mathfrak m_Q$ terminates the process. Thus $A'/Q$ is finite flat with finite separable closed fibre. The [étale criterion](#native-algebra-lemma-characterize-etale) makes it finite étale, in particular essentially smooth. Taking $D=A'$ proves every assertion, including containment of the prescribed set $E$. ∎

#### Lemma. Enlarging a factorization in positive characteristic

Retain a factorization supplied by the preceding lemma,

$$P_{\mathfrak p}/\mathfrak p^nP_{\mathfrak p}\longrightarrow D\longrightarrow L,
\qquad L=\Lambda_{\mathfrak q}/\mathfrak q^n\Lambda_{\mathfrak q}.$$

For every $\lambda\in\Lambda\setminus\mathfrak q$, there is an integer $q>0$ and a local Artinian factorization $D\to D'\to L$ such that $D'/D$ is essentially smooth, $D'\to L$ is flat, and the image of $\lambda^q$ lies in $D'$.

**Proof.** The flat local map $D\to L$ is injective, so identify $D$ with its image. Since the source $P_{\mathfrak p}/\mathfrak p^n$ maps essentially smoothly to the Artinian local ring $D$, its fibre is a zero-dimensional local essentially smooth algebra, hence a field. Its maximal ideal therefore generates $\mathfrak m_D$. The equality $\mathfrak p\Lambda_{\mathfrak q}=\mathfrak q\Lambda_{\mathfrak q}$ gives $\mathfrak m_DL=\mathfrak m_L$. The image of $\lambda$ is a unit in $L$. Apply the coefficient-enlargement fact proved at the start of the preceding proof with $A=D$ and this unit. It gives exactly the asserted factorization and power, with no change to the original maps from $P_{\mathfrak p}/\mathfrak p^n$. ∎

#### Lemma. Desingularization with inseparable residue fields

Let $k$ have characteristic $p>0$, let $A/k$ be finitely presented, and let $A\to\Lambda$ be a $k$-algebra map with $\Lambda$ Noetherian and geometrically regular over $k$. If $\mathfrak q$ is minimal over $\mathfrak h_A=\sqrt{H_{A/k}\Lambda}$, then the local desingularization problem at $\mathfrak q$ admits a resolution.

**Proof.** Put $d=\dim\Lambda_{\mathfrak q}$. If $d=0$, this local ring is a geometrically regular field extension of $k$, hence separable, and the preceding separable-residue-field argument applies. One may also use the finite-jet factorization at order one: its polynomial local base then has dimension zero and is a rational function field over $k$; its essentially smooth intermediate algebra supplies a smooth stage containing the finitely many source generators. The height-zero return lemma gives the desired global factorization. In particular, no positive-length parameter-lifting argument is needed in this case.

Assume $d>0$. We organize the construction around a strict presentation, an Artinian approximation, and the return from that approximation.

**Preparing a strict presentation.** Choose $N\geq1$ with

$$\mathfrak q^N\Lambda_{\mathfrak q}\subseteq H_{A/k}\Lambda_{\mathfrak q},$$

which is possible by minimality and Noetherianity. Write $H_{A/k}=(a_1,\ldots,a_s)$, set $P_0=k[x_1,\ldots,x_d]$, and form

$$B=A[x_1,\ldots,x_d,(z_{ij})]/
\bigl(x_i^{2N}-\sum_{j=1}^s a_jz_{ij}:1\leq i\leq d\bigr).$$

Each $B_{a_j}/P_0$ is smooth, by eliminating the corresponding $z_{ij}$ and using smoothness of $A_{a_j}/k$. The equations imply that the opens $D(a_j)$ cover every $D(x_i)$, so $B_{x_i}/P_0$ is smooth. Improve this presentation to $B\to C\to B$ with composite the identity. Then $C/P_0$ is finitely presented, and $C_{x_i}/P_0$ is smooth with free differentials. The strict part of the comparison lemma gives a common integer $c\geq1$ for which every $x_i^c$ is strictly standard for $C/P_0$.

Set $e=8c$ and choose

$$n\geq\max\{N+dc,\ d(e-1)+1\}.$$

Apply the [finite-jet factorization](#native-smoothing-lemma-solution-modulo) at this order, requiring its intermediate algebra to contain the images of generators of $A$. We obtain a polynomial algebra $P=k[y_1,\ldots,y_m]$, a map $P\to\Lambda$, a prime $\mathfrak p$ over $\mathfrak q$, and

$$P_{\mathfrak p}/\mathfrak p^nP_{\mathfrak p}
\longrightarrow D\longrightarrow L:=\Lambda_{\mathfrak q}/\mathfrak q^n\Lambda_{\mathfrak q}.$$

The first map is essentially smooth, the second is flat local, and $\mathfrak p\Lambda_{\mathfrak q}=\mathfrak q\Lambda_{\mathfrak q}$. Since the flat map $P_{\mathfrak p}\to\Lambda_{\mathfrak q}$ has a field as closed fibre, the [dimension formula](#native-algebra-lemma-dimension-base-fibre-equals-total) gives $\dim P_{\mathfrak p}=d$. Choose $\pi_1,\ldots,\pi_d\in\mathfrak p$ representing a regular system of parameters there. They also form a parameter system in $\Lambda_{\mathfrak q}$. Identify $D$ with its image in $L$, using faithful flatness. Containment of the source generators defines a map $A\to D$: all their polynomial relations already vanish in the containing ring $L$.

**Arranging annihilators over the polynomial base.** Put $R=P[t_1,\ldots,t_d]$ and $\gamma_i=\pi_it_i$. Let $S=P\setminus\mathfrak p$, so $S^{-1}R=P_{\mathfrak p}[t]$. The parameters $\pi_i$ are a permutable regular sequence in $P_{\mathfrak p}$. Therefore the products $\pi_it_i$, and the successive powers needed here, are regular sequences in this polynomial algebra, by [regular sequences with separate polynomial variables](#native-algebra-lemma-regular-sequence-in-polynomial-ring) and [powers of regular sequences](#native-algebra-lemma-regular-sequence-powers).

Use [Ogoma's lemma](#native-smoothing-lemma-ogoma) successively on the finite $R$-modules $R/(\gamma_1^e,\ldots,\gamma_{i-1}^e)$. Multiplying $\pi_i$ by an appropriate element of $S$ ensures

$$\operatorname{Ann}_{R/(\gamma_1^e,\ldots,\gamma_{i-1}^e)}(\gamma_i)
=\operatorname{Ann}_{R/(\gamma_1^e,\ldots,\gamma_{i-1}^e)}(\gamma_i^2).\tag{I1}$$

These successive changes leave earlier equalities intact and do not alter either localized parameter system. They also leave every $\pi_i$ in the image of $P$ in $D$.

**Arranging coefficients and annihilators in the target.** We construct units $\delta_i\in\Lambda\setminus\mathfrak q$ and coefficients $\lambda_{ij}\in\Lambda$, together with an essentially smooth local Artinian enlargement $D\to D'\subset L$, such that

$$ (\delta_i\pi_i)^{2N}=\sum_j a_j\lambda_{ij},\tag{I2}$$

all the images of $\delta_i,\lambda_{ij}$ belong to $D'$, and the annihilators of $\delta_i\pi_i$ and its square agree modulo the preceding $(\delta_h\pi_h)^e$. The map $D'\to L$ will remain flat throughout.

Suppose the construction has been completed for indices before $i$. The element $\pi_i^N$ belongs to $(a_1,\ldots,a_s)L$, so faithful flatness contracts this membership to the current coefficient ring: write

$$\pi_i^N=\sum_j a_jd_j\quad\text{in }D'.$$

Lift the $d_j$ to $b_j\in\Lambda_{\mathfrak q}$. The error lies in $\mathfrak q^n\Lambda_{\mathfrak q}$, which is contained in $\mathfrak q^{n-N}(a_1,\ldots,a_s)\Lambda_{\mathfrak q}$. Hence choose $b'_j\in\mathfrak q^{n-N}\Lambda_{\mathfrak q}$ with

$$\pi_i^N=\sum_j a_j(b_j+b'_j).$$

After multiplying by $\pi_i^N$, put $v_j=\pi_i^N(b_j+b'_j)$. Its image in $L$ is $\pi_i^Nd_j$, since $\pi_i^Nb'_j\in\mathfrak q^n\Lambda_{\mathfrak q}$. Write all $v_j=w_j/s_0$ with $w_j\in\Lambda$ and $s_0\notin\mathfrak q$. Some $u\notin\mathfrak q$ annihilates the error in the equality $s_0\pi_i^{2N}=\sum_j a_jw_j$. Choose $s\notin\mathfrak q$ divisible by $us_0$ and set

$$\mu_j=(s^{2N}/s_0)w_j.$$

This is an element of $\Lambda$, and the chosen divisibility gives the exact equality

$$ (s\pi_i)^{2N}=\sum_j a_j\mu_j\quad\text{in }\Lambda.$$

Its coefficient images in $L$ are $s^{2N}\pi_i^Nd_j$. By the [enlargement lemma](#native-smoothing-lemma-enlarge-solution-modulo), replace $s$ by a positive power and enlarge $D'$ so its image lies in $D'$. Scale the $\mu_j$ by the corresponding $2N$th power; both the equality and the displayed coefficient formula persist. Thus the new coefficient images lie in $D'$ as well.

In $\Lambda_{\mathfrak q}$, the preceding $(\delta_h\pi_h)^e$ followed by $s\pi_i$ form a regular sequence. Apply Ogoma's lemma to the finite module $\Lambda/((\delta_h\pi_h)^e:h<i)$ to find $s'\notin\mathfrak q$ such that every $(s')^q s\pi_i$, $q>0$, has equal first and second annihilators there. Enlarge $D'$ once more so that some $(s')^q$ belongs to it. Taking

$$\delta_i=(s')^q s,
\qquad\lambda_{ij}=(s')^{2Nq}\mu_j$$

establishes all requirements for index $i$. The finitely many successive essentially smooth enlargements compose, completing this induction.

**Constructing the compatible finite-jet map.** Send $x_i\mapsto\delta_i\pi_i$ and $z_{ij}\mapsto\lambda_{ij}$ to obtain $B\to\Lambda$, then use the augmentation $C\to B$ to define $C\to\Lambda$. Give $R$ its map to $\Lambda$ by $t_i\mapsto\delta_i$, and map $P_0\to R$ by $x_i\mapsto\gamma_i$. Let $C_R=C\otimes_{P_0}R$ and $B_R=B\otimes_{P_0}R$.

Write $Q=P_{\mathfrak p}/\mathfrak p^nP_{\mathfrak p}$. Define a $Q[t]$-algebra map

$$B_R\otimes_RQ[t]\longrightarrow D'[t_1,\ldots,t_d]$$

using the given map $A\to D'$ and the formulas

$$x_i\longmapsto\pi_it_i,
\qquad z_{ij}\longmapsto\lambda_{ij}\,t_i^{2N}/\delta_i^{2N}.\tag{I3}$$

Each $\delta_i$ is a unit in $D'$: its image in the residue field of $L$ is nonzero and the map is local. Equation (I2), multiplied by $t_i^{2N}/\delta_i^{2N}$, verifies every relation of $B$. Evaluation $t_i\mapsto\delta_i$ gives the specified map to $L$, including the original values of $z_{ij}$. Thus both the base map and the target map commute. Compose with the retraction from $C_R$ to obtain the same factorization for $C_R\otimes_RQ[t]$.

The algebra $D'/Q$ is essentially smooth, so $D'[t]$ is a filtered colimit of smooth $Q[t]$-algebras, by writing its localization as a filtered colimit of principal localizations. Since $C_R\otimes_RQ[t]$ is finitely presented, its map factors through one smooth stage $T\to L$. This gives an actual smooth factorization over $Q[t]$.

**Returning to the original rings.** Set $J=(\pi_1^e,\ldots,\pi_d^e)\subset P$ and $I=(\gamma_1^e,\ldots,\gamma_d^e)\subset R$. Because the parameters generate $\mathfrak pP_{\mathfrak p}$, every monomial of degree $d(e-1)+1$ in them contains an $e$th power. Our choice of $n$ therefore gives

$$\mathfrak p^nP_{\mathfrak p}\subseteq JP_{\mathfrak p},
\qquad\mathfrak q^n\Lambda_{\mathfrak q}\subseteq J\Lambda_{\mathfrak q}.$$

Base-change the smooth stage $T$ from $Q[t]$ to $P_{\mathfrak p}[t]/J$. Its target is now $\Lambda_{\mathfrak q}/J\Lambda_{\mathfrak q}$. Let $\mathfrak r$ be the inverse image of $\mathfrak q$ in $R$. Every $t_i$ is a unit in $R_{\mathfrak r}$, because its target image is $\delta_i\notin\mathfrak q$. Thus

$$IR_{\mathfrak r}=JR_{\mathfrak r},
\qquad I\Lambda_{\mathfrak q}=J\Lambda_{\mathfrak q}.$$

Localizing the smooth factorization accordingly gives one for $C_R\otimes_R(R/I)_{\mathfrak r}$ into $\Lambda_{\mathfrak q}/I\Lambda_{\mathfrak q}$. This target is Artinian, since $J$ consists of positive powers of a full parameter system. The [height-zero return lemma](#native-smoothing-lemma-delocalize-height-zero) therefore resolves the quotient problem before localization. If its selected prime is already smooth, use the identity factorization; otherwise height zero makes it minimal over the singularity ideal, as required by that lemma.

By arbitrary base change, every $\gamma_i^c$ is strictly standard for $C_R/R$. Equalities (I1) and the target equalities arranged above imply the corresponding annihilator equalities for their $c$th powers, since first-power stabilization implies stabilization of all positive powers. Apply [successive lifting](#native-smoothing-lemma-lift-solution) with these elements. Their eighth powers generate $I$, so it gives a resolution $C_R\to V\to\Lambda$ over $R$.

Finally the images of $a_j$ lie in $H_{C_R/R}$: they already make $B/P_0$ smooth, the improvement is smooth there, and base change preserves smoothness. The resolution over $R$ retains their radical and avoids $\mathfrak q$. Since $R/k$ is polynomial, $H_{V/R}\subseteq H_{V/k}$ by composition of smooth maps. The composite $A\to B\to C\to C_R\to V\to\Lambda$ therefore satisfies $\mathfrak h_A\subseteq\mathfrak h_V\nsubseteq\mathfrak q$, proving the lemma. ∎

#### The main theorem

The local constructions now give a terminating global procedure: unless the target is already covered by the smooth locus of the current presentation, resolve a minimal prime of its remaining nonsmooth locus. Each step strictly enlarges a radical ideal in the Noetherian target.

#### Theorem. General Néron desingularization (Popescu)

For a regular homomorphism $R\to\Lambda$ between Noetherian rings, the $R$-algebra $\Lambda$ is a filtered colimit of smooth $R$-algebras.

**Proof.** By the [field reduction](#native-smoothing-lemma-reduce-to-field), it is enough to take $R=k$ a field and $\Lambda/k$ Noetherian and geometrically regular. Fix a finitely presented $k$-algebra $A$ mapping to $\Lambda$, and set $\mathfrak h_A=\sqrt{H_{A/k}\Lambda}$.

If this radical is proper, choose a prime minimal over it. In characteristic zero its residue extension is separable, so the [separable resolution lemma](#native-smoothing-lemma-resolve-special) applies. In positive characteristic use the [inseparable resolution lemma](#native-smoothing-lemma-resolve-general). Either gives a finitely presented algebra $B$ through which the map factors, with $\mathfrak h_A\subseteq\mathfrak h_B$ and $\mathfrak h_B$ avoiding the selected prime. This containment is strict, because the selected prime contains $\mathfrak h_A$.

Repeat if the new radical is still proper. An infinite repetition would be an infinite strictly ascending chain of ideals in the Noetherian ring $\Lambda$, which is impossible. Thus a finite sequence of factorizations reaches $B$ with $\sqrt{H_{B/k}\Lambda}=\Lambda$, equivalently $H_{B/k}\Lambda=\Lambda$. The [smooth factorization lemma](#native-smoothing-lemma-final-solve) replaces it by a smooth algebra still factoring the original map $A\to\Lambda$. Every finite presentation has therefore been factored through a smooth algebra. The [finite factorization criterion](#reader-section-2) proves the theorem, including the filteredness of the resulting presentation. The zero target is covered by the smooth zero algebra. ∎

#### The approximation property for G-rings

For a Noetherian local ring $(R,\mathfrak m)$, the G-ring condition can be tested on the completion map $R\to\widehat R$: it is equivalent to regularity of that map. See [the maximal-ideal test for G-rings](#native-more-algebra-lemma-check-g-ring-maximal-ideals). Henselization and strict henselization preserve this condition, by [henselian permanence](#native-more-algebra-lemma-henselization-g-ring).

The examples used here include algebras essentially of finite type over a field, over a complete Noetherian local ring, over $\mathbf Z$, or over a characteristic-zero Dedekind ring. Their G-ring property is supplied by [examples and permanence](#native-more-algebra-proposition-ubiquity-g-ring). These examples are not an extra hypothesis on the following results: the stated G-ring condition is sufficient.

For polynomials $f_1,\ldots,f_m\in R[X_1,\ldots,X_n]$, a solution in an $R$-algebra $S$ is a tuple $a\in S^n$ with $f_j(a)=0$ for every $j$. Approximation asks for exact solutions with specified finite-order agreement with a solution in the completion.

#### Theorem. Artin approximation for henselian local G-rings

Let $(R,\mathfrak m)$ be a henselian Noetherian local G-ring. Given $f_1,\ldots,f_m\in R[X_1,\ldots,X_n]$ and a solution $a\in\widehat R^n$, for every $N\geq0$ there is a solution $b\in R^n$ satisfying

$$a_i-b_i\in\mathfrak m^N\widehat R\quad(1\leq i\leq n).$$

**Proof.** First reduce finite-order approximation to existence of an exact solution. Choose $c_i\in R$ representing $a_i$ modulo $\mathfrak m^N\widehat R$, choose generators $d_1,\ldots,d_s$ of $\mathfrak m^N$, and write $a_i=c_i+\sum_\ell d_\ell u_{i\ell}$ in $\widehat R$. Substitute

$$X_i=c_i+\sum_\ell d_\ell U_{i\ell}$$

in each $f_j$. The resulting finite polynomial system has the solution $(u_{i\ell})$ in $\widehat R$. Any solution of that new system in $R$ gives an exact solution of the original system with the desired congruence. Thus it remains to prove existence in $R$ for any finite system solvable in $\widehat R$.

Let $C\subseteq\widehat R$ be the $R$-subalgebra generated by its finitely many solution coordinates. It is finitely presented, because $R$ is Noetherian. The G-ring condition makes $R\to\widehat R$ regular, so Popescu's theorem and finite factorization give

$$C\longrightarrow B\longrightarrow\widehat R$$

with $B/R$ smooth. Composing the second map with the residue map gives a point $B\to R/\mathfrak m$. The [smooth-section lifting lemma](#native-more-algebra-lemma-lift-section-smooth-morphism) gives an étale $R$-algebra $R'$ with $R'/\mathfrak mR'\simeq R/\mathfrak m$ and a map $B\to R'$ lifting this point. The [henselian section criterion](#native-algebra-lemma-characterize-henselian) supplies an $R$-algebra map $R'\to R$. The composite $C\to B\to R'\to R$ sends the coordinates to a solution in $R$. Apply this existence assertion to the substituted system to obtain the required $b$. ∎

Order zero imposes no congruence restriction. If negative orders are included with the convention $\mathfrak m^N=R$, the same existence assertion covers them as well.

A pointed étale neighbourhood also has a canonical comparison with the completion. If $R\to R'$ is étale and $\mathfrak m'\subset R'$ lies over $\mathfrak m$ with unchanged residue field, then

$$R\longrightarrow R'_{\mathfrak m'}\longrightarrow R^h\longrightarrow\widehat R$$

are injective local maps, and the completions of the first two local rings are canonically isomorphic. These are the pointed étale and henselization comparisons in [the henselian construction](#native-algebra-lemma-henselian-functorial-prepare) and [Noetherian henselization](#native-more-algebra-lemma-henselization-noetherian). The ring being localized is $R'$, so the second term is $R'_{\mathfrak m'}$.

#### Theorem. Artin approximation in an étale neighbourhood

Let $(R,\mathfrak m)$ be a Noetherian local G-ring, and suppose a finite polynomial system over $R$ has a solution $a\in\widehat R^n$. For every $N\geq0$ there are an étale $R$-algebra $R'$, a maximal ideal $\mathfrak m'$ over $\mathfrak m$ with $\kappa(\mathfrak m')=\kappa(\mathfrak m)$, and a solution $b\in(R')^n$ such that

$$a_i-b_i\in(\mathfrak m')^N\widehat R$$

under the pointed completion comparison just described.

**Proof.** Perform the same substitution $X_i=c_i+\sum_\ell d_\ell U_{i\ell}$ with $d_\ell$ generating $\mathfrak m^N$. Apply Popescu factorization and smooth-section lifting to the new system, obtaining $C\to B\to R'$ with $R'$ étale over $R$ and $R'/\mathfrak mR'\simeq R/\mathfrak m$. This gives an exact solution of the substituted system in $R'$, without needing a henselian section back to $R$.

Let $\mathfrak m'$ be the kernel of its given residue map. The resulting original coordinates $b_i=c_i+\sum_\ell d_\ell v_{i\ell}$ solve all the equations. Under $R'\to R'_{\mathfrak m'}\to\widehat R$, the difference from $a_i=c_i+\sum_\ell d_\ell u_{i\ell}$ belongs to $\mathfrak m^N\widehat R=(\mathfrak m')^N\widehat R$. This proves the assertion. As an alternative, one can apply the henselian theorem to $R^h$, which is a G-ring, and descend the finitely many solution coordinates and equations to a pointed étale stage in its filtered presentation. ∎

#### Lemma. Approximation after localization at a prime

Let $R$ be Noetherian, let $\mathfrak p\subset R$ be prime, and assume $R_{\mathfrak p}$ is a G-ring. Suppose polynomials over $R$ have a solution $a\in\widehat{R_{\mathfrak p}}^{,n}$. For each $N\geq0$ there are an étale $R$-algebra $R'$, a prime $\mathfrak p'$ above $\mathfrak p$ with the same residue field, and a solution $b\in(R')^n$ satisfying

$$a_i-b_i\in(\mathfrak p')^N\widehat{R'_{\mathfrak p'}}$$

after identifying this completion with $\widehat{R_{\mathfrak p}}$.

**Proof.** Apply the preceding theorem over $R_{\mathfrak p}$. It gives a pointed étale algebra $R''/R_{\mathfrak p}$ and a solution there. The finite presentation of $R''$, its étale presentation data, and the inverse of the chosen Jacobian determinant involve only finitely many elements of $R_{\mathfrak p}$. Clear their denominators to descend the algebra to an étale algebra over $R_s$ for some $s\notin\mathfrak p$. Since $R_s/R$ is étale, this is an étale $R$-algebra $R'$; see also [finite-presentation descent of étale algebras](#native-algebra-lemma-etale).

The finitely many solution coordinates descend after one further localization away from the chosen prime. Clear the finitely many relations asserting that they solve the equations at the same time. Such localizations preserve the selected local ring and the residue identification. If $\mathfrak p'$ is the inverse image of the chosen prime of $R''$, the local rings $R'_{\mathfrak p'}$ and the selected localization of $R''$ are identical. Their completions and the order-$N$ congruences are therefore the ones already obtained. ∎

### B.10. Predecessor constructions used in the proof

These are the complete selected statements and proofs from the native Stacks source files. Their source labels are retained for precise cross-references. Remaining lower dependencies are listed in §12; not all of them are proved in this lesson.

#### B.10.1. More on Algebra

The lifting arguments below preserve the entire quotient by the given ideal. The ideal need not be nilpotent or lie in the Jacobson radical. The permitted change of base is an étale map whose reduction is the identity on that quotient.

#### Lemma. Localizing an algebra while preserving its closed fibre

Suppose $A\to B$ is étale at all primes of $B$ containing an ideal $J$. There is an element $g\in B$, with $g\equiv1\pmod J$, for which $B_g$ is étale over $A$. In particular localization at $g$ leaves $B/J$ unchanged.

**Proof.** The étale locus is open; this is part of the local characterization in [Étale ring maps](#native-algebra-definition-etale). Write its complement as $V(L)$. The hypothesis says $V(L+J)=\varnothing$, so $L+J=B$. Choose $g\in L$ with $1-g\in J$. Then $D(g)$ lies in the étale locus and contains $V(J)$. These are exactly the two required properties. ∎

#### Lemma. Lifting a monic polynomial factorization

Let $I\subset A$ be any ideal, and let $f\in A[t]$ be monic. Suppose its reduction has a factorization $\overline f=\overline g\,\overline h$ into monic polynomials generating $(A/I)[t]$ as an ideal. There are an étale $A$-algebra $A'$, an isomorphism $A'/IA'\simeq A/I$ compatible with $A$, and monic factors $g',h'\in A'[t]$ of $f$ reducing to $\overline g,\overline h$.

**Proof.** Put $n=\deg\overline g$ and $m=\deg\overline h$. Introduce coefficients for two monic polynomials $G,H$ of these degrees. Equating the $n+m$ remaining coefficients of $GH$ with those of $f$ defines a finitely presented $A$-algebra $B$. The specified factors define an $A$-algebra surjection $\epsilon:B\to A/I$.

At these coefficients, the derivative of the multiplication map is
$$
(A/I)[t]_{<n}\oplus(A/I)[t]_{<m}\longrightarrow(A/I)[t]_{<n+m},
\qquad (u,v)\longmapsto\overline h u+\overline g v.
$$
This map is an isomorphism. Indeed, for a polynomial $w$ on the right, invert $\overline h$ modulo the monic polynomial $\overline g$ to obtain the unique $u$ of degree less than $n$ with $\overline h u\equiv w\pmod{\overline g}$. Then $v=(w-\overline h u)/\overline g$ has degree less than $m$. This construction is linear and also proves uniqueness. It includes the degree-zero cases, with the corresponding polynomial module equal to zero.

Consequently the determinant $d$ of the coefficient Jacobian maps to a unit under $\epsilon$. The standard étale criterion makes $B_d$ étale over $A$; this is also the construction in [Étale algebras from polynomial factorizations](#native-algebra-example-factor-polynomials-etale). Put $D=B_d/IB_d$. The surjection $D\to A/I$ is a map between étale $A/I$-algebras, hence is étale by [Morphisms between étale algebras](#native-algebra-lemma-map-between-etale). A surjective flat map of finite presentation selects an open and closed component: by [Finite presentation and flatness](#native-algebra-lemma-surjective-flat-finitely-presented), there is an idempotent $e\in D$ with $D_e\simeq A/I$. Lift $e$ to $v\in B_d$ and set $A'=(B_d)_v$. This remains étale over $A$, has the specified quotient, and carries the required images of $G,H$. ∎

#### Lemma. Lifting a coprime factorization

The same conclusion holds when the two factors of $\overline f$ are coprime and the leading coefficient of $\overline g$ is a unit, without requiring the factors themselves to be monic.

**Proof.** Lift that leading coefficient to $u\in A$. Since $u$ becomes a unit in $A/I$, the localization $A\to A_u$ is étale and induces an isomorphism on quotients by $I$. Over this localization replace the prescribed factors by $\overline u^{-1}\overline g$ and $\overline u\,\overline h$. Both are monic: the degree and leading coefficient of a product with a monic factor are determined without cancellation. Apply the preceding lemma, then multiply the lifted factors by $u$ and $u^{-1}$ respectively. Their product is still $f$ and their reductions are the original factors. ∎

#### Lemma. Separating a closed image from another closed subset

For a map $R\to S$ and ideals $I\subset R$, $J\subset S$, assume that the closure of the image of $V(J)$ in $\operatorname{Spec}R$ avoids $V(I)$. Then some $f\in R$ satisfies $f\equiv1\pmod I$ and has image in $J$.

**Proof.** Express that closure as $V(L)$. The disjointness gives $I+L=R$, so choose $b\in L$ congruent to $1$ modulo $I$. Every prime of $S$ containing $J$ contains the image of $b$. Thus that image lies in $\sqrt J$, and a power $f=b^r$ has image in $J$. The same power remains congruent to $1$ modulo $I$. This uses the ideal–closed-set correspondence in [the affine Zariski topology](#native-algebra-lemma-zariski-topology). ∎

#### Lemma. Integral elements compatible with a lifted factorization

Let $B$ be integral over $A$, and suppose the image of $b\in B$ in $B/IB$ is idempotent. Then a monic polynomial $f\in A[t]$ annihilates $b$ and satisfies
$$\overline f=t^d(t-1)^d\quad\text{for some }d\geq1.$$

**Proof.** The element $z=b^2-b$ belongs to $IB$. Choose a finite expression for $z$ with coefficients in $I$ and elements of $B$. Adjoining those elements and $b$ to $A$ gives a finite $A$-algebra $B_0\subset B$, since each adjoined element is integral. Moreover $zB_0\subset IB_0$. On a finite set of module generators for $B_0$, multiplication by $z$ is therefore represented by a matrix with entries in $I$. The determinant trick produces a monic polynomial
$$q(t)=t^d+c_{d-1}t^{d-1}+\cdots+c_0,\qquad c_i\in I,$$
that annihilates multiplication by $z$, and hence annihilates $z$ itself. Take a nonempty generating set so that $d\geq1$. Now $f(t)=q(t^2-t)$ has all the asserted properties. This is the integral-over-an-ideal argument of [Integral extensions](#native-algebra-lemma-integral-integral-over-ideal), applied inside the finite subalgebra containing the data. ∎

#### Lemma. Lifting an idempotent after localization

If $B$ is an integral $A$-algebra and $\overline e\in B/IB$ is idempotent, then after an étale base change $A\to A'$ inducing $A'/IA'\simeq A/I$, the element $\overline e$ lifts to an idempotent of $B\otimes_A A'$.

**Proof.** Choose $y\in B$ reducing to $\overline e$ and use the preceding lemma to obtain $f(y)=0$ with $\overline f=t^d(t-1)^d$. Lift this coprime factorization by an étale change of base preserving $A/I$. Temporarily rename the new rings $A,B$; then
$$
f=gh,\qquad \overline g=t^d,\qquad \overline h=(t-1)^d.
$$
Set $b_1=g(y)$, $b_2=h(y)$. Their product is zero, and their reductions are $\overline e$ and $(-1)^d(1-\overline e)$. Thus $V(b_1,b_2)$ avoids $V(IB)$.

An integral morphism of spectra is closed, by [going up](#native-algebra-lemma-integral-going-up) and [the closed-map criterion](#native-algebra-lemma-going-up-closed). Its image here avoids $V(I)$. The preceding separation lemma supplies $a\equiv1\pmod I$ whose image lies in $(b_1,b_2)B$. Localizing $A$ at $a$ is another permitted étale change. In the resulting $B$, choose $u,v$ with $ub_1+vb_2=1$. The element $e=ub_1$ is idempotent because
$$e(1-e)=uvb_1b_2=0.$$
Reducing the displayed Bézout identity modulo $IB$ and multiplying it by $\overline e$ gives $\overline u\,\overline e=\overline e$. Therefore $e$ reduces to the prescribed idempotent. The composite base change is étale and still induces the identity quotient by $I$. ∎

#### Lemma. Lifting a finite projective module

A finite projective module $\overline P$ over $A/I$ lifts to a finite projective module over some étale $A$-algebra $A'$ satisfying $A'/IA'\simeq A/I$.

**Proof.** Realize $\overline P$ as the image of an idempotent endomorphism $\overline p$ of $(A/I)^n$. If $n=0$, there is nothing to lift. Otherwise choose a matrix $\varphi\in M_n(A)$ lifting $\overline p$ and let $f(t)$ be its characteristic polynomial. The finite integral algebra $B=A[t]/(f)$ acts on $A^n$ by $t\mapsto\varphi$, by [Cayley–Hamilton](#native-algebra-lemma-charpoly).

In each residue field of $A/I$, the characteristic polynomial of $\overline p$ is $t^{n-r}(t-1)^r$, where $r$ is its rank at that point. It follows that the image of $t(1-t)$ in $B/IB$ belongs to every prime: for a prime of $B/IB$, pass to the residue field at its contraction in $A/I$ and then use this factorization. Choose $N\geq1$ for which $t^N(1-t)^N=0$ in $B/IB$. The two terms $t^N$ and $(1-t)^N$ generate the unit ideal, so their sum is a unit when their product is zero. Consequently
$$
\overline e=\frac{t^N}{t^N+(1-t)^N}\in B/IB
$$
is idempotent. Under the action on $(A/I)^n$, it maps to $\overline p$, since $\overline p^N=\overline p$ and $(1-\overline p)^N=1-\overline p$.

Apply the idempotent-lifting lemma to $B/A$. The lifted idempotent in $B\otimes_A A'$ acts as a projector $p'$ on $(A')^n$. Its image $P'$ is a finite projective direct summand, and the direct-sum decomposition remains split after reduction modulo $IA'$. Thus $P'/IP'\simeq\overline P$, as required. ∎

#### Lemma. The cotangent complex of a symmetric algebra

Write $F=A^m$, choose an exact sequence $0\to K\to F\to M\to0$, and put
$$
P=\operatorname{Sym}_A(F),\qquad C=\operatorname{Sym}_A(M),\qquad
J=\ker(P\to C).
$$
For $k=(k_1,\ldots,k_m)\in K$, let $\ell_k=\sum_i k_i y_i\in P$. Define the $P$-module of relations among these linear equations by
$$
S=\ker\bigl(K\otimes_A P\longrightarrow P,\quad
k\otimes p\longmapsto p\ell_k\bigr).
$$
There is a right-exact sequence
$$
S\otimes_P C\longrightarrow K\otimes_A C
\longrightarrow J/J^2\longrightarrow0.
\tag{SA1}
$$
Thus the naive cotangent complex of this presentation, in degrees $-1,0$, is
$$
\left[
\frac{K\otimes_A C}{\operatorname{im}(S\otimes_P C)}
\xrightarrow{\ d\ } C^m
\right],\qquad
d([k\otimes c])=(ck_1,\ldots,ck_m).
\tag{SA2}
$$
In every case there is a canonical identification
$$\Omega_{C/A}\simeq M\otimes_A C.$$
If $M$ is projective, the second arrow in (SA1) is an isomorphism, so (SA2) simplifies to $[K\otimes_A C\to C^m]$.

**Proof.** The universal property of the symmetric algebra identifies $C$ with the quotient of $P$ by the linear forms $\ell_k$. Hence $K\otimes_A P\to J$ is surjective with kernel $S$. Tensor this presentation with $C=P/J$. Right exactness gives (SA1), because $J\otimes_P C=J/J^2$. Differentiating a relation $\sum p_i\ell_{k_i}=0$ and then reducing modulo $J$ gives $\sum \overline p_i k_i=0$ in $C^m$. Consequently the displayed differential descends to the quotient in (SA2). This is exactly the defining conormal presentation of the [naive cotangent complex](#context-algebra-section-netherlander).

For any $C$-module $N$, an $A$-derivation $C\to N$ is uniquely determined by its restriction to $M\subset C$, and that restriction can be any $A$-linear map $M\to N$. The universal properties of differentials and tensor products therefore give $\Omega_{C/A}\simeq C\otimes_A M$. This argument also applies when $M$ has no finite generating set.

When $M$ is projective, $F\to M$ splits. Both $M$ and $K$ are then finite projective. Locally on $\operatorname{Spec}A$, choose bases for the two summands in $F=M\oplus K$. The resulting polynomial coordinates identify $J$ with the ideal generated by the coordinates corresponding to $K$. Its conormal module is free on those coordinates, and the canonical map $K\otimes_A C\to J/J^2$ is an isomorphism. These are local checks of a single globally defined map, so they prove the assertion over $A$. ∎

**Why the relation term is necessary.** The unrestricted formula $J/J^2\simeq K\otimes_A C$ in [Stacks, Tag 07EV](https://stacks.math.columbia.edu/tag/07EV) fails already over $A=\mathbb Z$. Take
$$
M=(\mathbb Z/2)^2,\qquad K=2\mathbb Z\oplus2\mathbb Z,
\qquad C=\mathbb Z[x,y]/(2x,2y).
$$
Using $(2,0)$ and $(0,2)$ as a basis of $K$, the natural map is
$$
C^2\longrightarrow (2x,2y)/(2x,2y)^2,\qquad
(u,v)\longmapsto[2ux+2vy].
$$
It kills $(y,-x)$. This vector is nonzero, as is seen after reducing to $\mathbb F_2[x,y]^2$. Thus the proposed canonical map is not injective. More explicitly, in graded degree two its domain has dimension four over $\mathbb F_2$, whereas its codomain has dimension three. The missing relation is $y(2x)-x(2y)=0$. Replacing the image of a map by its domain before taking a cokernel loses precisely such relations.

The corrected statement retains the arbitrary-module case through (SA1)–(SA2), rather than using the projective case as a substitute for it. The [improved smooth presentation](#native-smoothing-lemma-improve-presentation) uses the projective case after localization at the specified smooth locus.

#### Lemma. Smoothness of a symmetric algebra

For any $A$-module $M$, its symmetric algebra $C=\operatorname{Sym}_A(M)$ is smooth over $A$ exactly when $M$ is finite projective.

**Proof.** Suppose first that $C/A$ is smooth. Then $\Omega_{C/A}$ is a finite projective $C$-module. Pull it back along the augmentation $C\to A$ and use the preceding differential calculation:
$$
\Omega_{C/A}\otimes_C A\simeq (M\otimes_A C)\otimes_C A\simeq M.
$$
Base change preserves finite projectivity, so $M$ has the required property. Equivalently, the augmentation ideal has conormal module $M$, and the same conclusion follows from [the conormal module of a smooth section](#native-algebra-lemma-section-smooth).

Conversely, choose a finite free module surjecting onto the finite projective module $M$. Its kernel $K$ is a finite projective direct summand. Thus $C$ has a finite presentation, with equations given by a finite generating set of $K$. Locally on $\operatorname{Spec}A$, the module $M$ is free of finite rank and $C$ is a polynomial algebra. Smoothness is local on the base, which proves the claim. One may also use the projective case of (SA2): the inclusion $K\otimes_A C\to C^m$ splits and its cokernel is the finite projective module $M\otimes_A C$. The [cotangent criterion for smoothness](#native-algebra-definition-smooth) gives the same conclusion. ∎

#### Lemma. Lifting a section of a smooth morphism

Let $A\to B$ be smooth, let $I\subset A$ be an ideal, and fix an $A$-algebra map $\epsilon:B\to A/I$. There exist an étale $A$-algebra $A'$ with $A'/IA'\simeq A/I$ and an $A$-algebra map $B\to A'$ whose reduction is $\epsilon$.

**Proof.** Put $J=\ker\epsilon$. The chosen map is surjective because it extends $A\to A/I$. The augmentation $B/IB\to A/I$ identifies
$$
P_0=J/(J^2+IB)\simeq\Omega_{B/A}\otimes_B A/I.
\tag{SL1}
$$
For completeness, this is the conormal identity for an augmented algebra: modulo the square of its augmentation ideal, the map taking an element to that element minus its constant term is a derivation. It gives the inverse to the universal differential map on the augmentation ideal. Thus (SL1) does not require a nilpotence assumption on $I$. Smoothness makes $P_0$ finite projective.

Choose a finite projective complement $K_0$ with $P_0\oplus K_0\simeq(A/I)^n$. By [Lifting a finite projective module](#native-more-algebra-lemma-lift-projective-module), an étale change $A\to A_1$ preserving $A/I$ lifts $K_0$ to a finite projective $A_1$-module $K$. Replace $B$ by
$$
B_1=(B\otimes_A A_1)\otimes_{A_1}\operatorname{Sym}_{A_1}(K).
$$
This is smooth over $A_1$, by [Smoothness of a symmetric algebra](#native-more-algebra-lemma-symmetric-algebra-smooth), [base change](#native-algebra-lemma-base-change-smooth), and [composition of smooth maps](#native-algebra-lemma-locally-smooth). The original section and the symmetric-algebra augmentation define $B_1\to A/I$. Its module (SL1) is $P_0\oplus K_0$, because relative differentials of the tensor product split as the sum of the two pulled-back differential modules. Every map from $B_1$ extending this section also gives the required map from the original $B$. We can therefore rename $A_1,B_1$ as $A,B$ and assume that $P_0$ is free of rank $n$.

Choose $f_1,\ldots,f_n\in J$ whose classes form a basis of $P_0$, and let $C=B/(f_1,\ldots,f_n)$. We claim that $C/A$ is étale along the closed subset defined by $JC$. Let $\mathfrak q\supset J$ be a prime of $B$, and let $\mathfrak r$ be its image in $C$. Since $\Omega_{B/A}$ is finite projective and has rank $n$ at this section, its localization at $\mathfrak q$ is free of rank $n$. The differentials $df_i$ reduce to a basis modulo $J$, so Nakayama's lemma makes the map
$$
C_{\mathfrak r}^n\longrightarrow
\Omega_{B/A}\otimes_B C_{\mathfrak r},\qquad e_i\longmapsto df_i,
$$
an isomorphism: it is a surjection between free modules of the same finite rank over a local ring.

Write $L=(f_1,\ldots,f_n)\subset B$. The conormal map
$$
(L/L^2)_{\mathfrak r}\longrightarrow
\Omega_{B/A}\otimes_B C_{\mathfrak r}
$$
factors the preceding isomorphism through the surjection $C_{\mathfrak r}^n\to(L/L^2)_{\mathfrak r}$. Both arrows in this factorization are consequently isomorphisms. The [cotangent transitivity sequence](#native-algebra-lemma-exact-sequence-nl), with $B/A$ smooth and $\Omega_{B/A}$ projective, now gives
$$H_1(L_{C/A})_{\mathfrak r}=0,\qquad\Omega_{C/A,\mathfrak r}=0.$$
The algebra $C$ is finitely presented over $A$. The [pointwise smoothness criterion](#native-algebra-lemma-smooth-at-point) therefore gives smoothness at $\mathfrak r$, and the vanishing of relative differentials gives étaleness there.

By [Localizing an algebra while preserving its closed fibre](#native-more-algebra-lemma-localize-upstairs), choose a localization $C_g$ that is étale over $A$ and still maps onto $C/JC=A/I$. The quotient map $C_g/IC_g\to A/I$ is a surjection between étale $A/I$-algebras. As in [Lifting a monic polynomial factorization](#native-more-algebra-lemma-lift-factorization-monic), isolate its open and closed component by localizing at a lift of the corresponding idempotent. The result is an étale $A$-algebra $A'$ with $A'/IA'\simeq A/I$ and a map $B\to C_g\to A'$ reducing to $\epsilon$.

Finally compose with the initial base change $A\to A_1$ if one was made. Étaleness and the asserted quotient identification are preserved by that composition, so this proves the claim for the original rings and section. ∎

#### Lemma. The conormal sequence for a first-homology regular sequence

Suppose $I\subset J$ are ideals of $A$, and $J/I$ is generated by a finite sequence with vanishing first Koszul homology over $A/I$. Then
$$I\cap J^2=IJ.$$

**Proof.** Lift the sequence to $g_1,\ldots,g_m\in J$ and put $G=(g_1,\ldots,g_m)$, so $J=I+G$. First observe that $I\cap G=IG$. Indeed, the short exact sequence of Koszul complexes
$$
0\longrightarrow I\otimes_A K_\bullet(A;g)
\longrightarrow K_\bullet(A;g)
\longrightarrow K_\bullet(A/I;\overline g)\longrightarrow0
$$
is exact term by term because Koszul terms are free. The hypothesis on $H_1$ makes $I/IG\to A/G$ injective in its homology sequence. This gives the asserted intersection equality; see also [First cotangent homology after a regular quotient](#native-more-algebra-lemma-h1-regular-in-quotient).

Now $J^2=I^2+IG+G^2$. If $x\in I\cap J^2$, subtract its terms in $I^2+IG$ to obtain an element of $I\cap G^2\subset I\cap G=IG$. Thus $x\in I^2+IG=IJ$. The reverse inclusion follows directly from $I\subset J$. ∎

#### Lemma. The conormal sequence for a first-homology regular ideal

The equality $I\cap J^2=IJ$ also holds if $J/I$ is an $H_1$-regular ideal of $A/I$.

**Proof.** At a prime containing $J$, the definition supplies a neighborhood where $J/I$ has the finite sequence required in the preceding lemma. At a prime outside $V(J)$, the localized ideal $J$ is the whole ring, and both sides become $I$. Intersections, products and squares of these ideals commute with localization. The two submodules therefore agree at every prime and hence agree globally. ∎

#### Lemma. Finite projectivity of a quasi-regular conormal module

If $I$ is a quasi-regular ideal of $R$, then $I/I^2$ is finite projective over $R/I$.

**Proof.** On the neighborhoods in the definition of a quasi-regular ideal, its chosen generators give a basis of $I/I^2$: this is the degree-one part of the quasi-regularity isomorphism with the associated graded algebra. Thus $I/I^2$ is locally free of finite rank on $\operatorname{Spec}(R/I)$. Quasi-compactness permits a finite such cover. The [finite-projective criterion](#native-algebra-lemma-finite-projective) then applies, without requiring that the rank be the same on different connected components. ∎

#### Lemma. Syntomic algebras and local complete intersections

A ring map $R\to S$ is syntomic if and only if it is flat and a local complete intersection.

**Proof.** A syntomic map is flat by definition. Its local presentations are relative global complete intersections, by [Local criteria for a syntomic algebra](#native-algebra-lemma-syntomic). Their defining equations are Koszul-regular by [Koszul complexes of global complete intersections](#native-more-algebra-lemma-relative-global-complete-intersection-koszul). The [locality of the complete-intersection condition](#native-more-algebra-lemma-lci-local) therefore makes $R\to S$ a local complete intersection.

For the converse, choose a finite polynomial presentation $S=R[x_1,\ldots,x_n]/I$. The local complete-intersection hypothesis says that $I$ is locally generated by finite Koszul-regular sequences around its zero set. Away from that set it is locally the unit ideal. A finite principal-open cover of the polynomial spectrum consequently shows that $I$ is finitely generated, so $S$ is finitely presented over $R$.

It remains to check the fibres. For a field $k$ over $R$ and a prime of $S\otimes_R k$, choose a neighborhood in $R[x]$ where $I$ is generated by a Koszul-regular sequence $f_1,\ldots,f_r$. Write the localized polynomial ring as $Q$ and its quotient as $T$. The ring $Q$ is flat over $R$, and $T$ is flat over $R$ by the assumed flatness of $S$. The Koszul resolution of $T$ consists of finite free $Q$-modules. Its successive kernels are flat over $R$: start with the exact sequence ending in the flat module $T$ and proceed through the resolution, using closure of flat modules under kernels of surjections between flat modules. Tensoring the resolution with $k$ is therefore still exact in positive degrees. Hence the images of the $f_i$ are Koszul-regular in $Q\otimes_R k$.

At the chosen prime this is a sequence in the maximal ideal of a Noetherian local ring. The [Noetherian equivalence of regularity conditions](#native-more-algebra-lemma-noetherian-finite-all-equivalent) makes it a regular sequence. The [local complete-intersection criterion over a field](#native-algebra-lemma-lci) gives a complete-intersection neighborhood of this prime in the fibre. Since the prime and field were arbitrary, all fibres are local complete intersections. Together with flatness and finite presentation, this is [the syntomic criterion](#native-algebra-definition-lci).

Alternatively, the same fibre step follows from [Relative regular immersions in affine algebra](#native-more-algebra-lemma-relative-regular-immersion-algebra): it preserves $H_1$-regularity under this base change because the quotient is flat. The same Noetherian local criterion then gives the regular sequence in the fibre. ∎

#### Lemma. Cotangent transitivity with a complete-intersection terminal map

Let $A\to B\to C$ be ring maps with $B\to C$ a local complete intersection. Choose presentations
$$
P=A[x_s\mid s\in S]\twoheadrightarrow B,\qquad
B[y_1,\ldots,y_m]\twoheadrightarrow C,
$$
whose kernels are $I$ and $J$. Put $Q=P[y_1,\ldots,y_m]$ and $K=\ker(Q\to C)$. The presentation maps give the following commutative diagram with exact rows; all tensor products in the differential row are along the indicated polynomial maps to $C$:
$$
\begin{array}{ccccccccc}
0&\longrightarrow&(I/I^2)\otimes_B C&\longrightarrow&K/K^2&\longrightarrow&J/J^2&\longrightarrow&0\\
&&\downarrow d&&\downarrow d&&\downarrow d&&\\
0&\longrightarrow&\Omega_{P/A}\otimes_P C&\longrightarrow&\Omega_{Q/A}\otimes_Q C&\longrightarrow&\Omega_{B[y]/B}\otimes_{B[y]} C&\longrightarrow&0.
\end{array}
\tag{CT1}
$$
Consequently the cotangent transitivity sequence begins with zero:
$$
\begin{aligned}
0\longrightarrow H_1(\mathrm{NL}_{B/A}\otimes_B C)
&\longrightarrow H_1(L_{C/A})\longrightarrow H_1(L_{C/B})\\
&\longrightarrow\Omega_{B/A}\otimes_B C
\longrightarrow\Omega_{C/A}\longrightarrow\Omega_{C/B}\longrightarrow0.
\end{aligned}
\tag{CT2}
$$
Here $\mathrm{NL}_{B/A}\otimes_B C$ means the ordinary tensor product of the two-term presentation complex; the tensor symbol in this term is not being replaced by a derived tensor product.

**Proof.** Let $I_Q=IQ$. Then $Q/I_Q=B[y]$ and $K/I_Q=J$. The complete-intersection hypothesis makes $J$ Koszul-regular, and therefore $H_1$-regular. The preceding intersection lemma gives
$$I_Q\cap K^2=I_QK.$$
It follows that the usual conormal sequence is left exact, because its left-hand term and kernel identify as
$$
(I/I^2)\otimes_B C=I_Q/I_QK
\xrightarrow{\ \sim\ }(I_Q+K^2)/K^2
\subset K/K^2.
$$
Its cokernel is $J/J^2$. The differential row is split exact by separating the $dx_s$ and $dy_i$ coordinates. Applying universal derivations makes the three squares commute, so (CT1) is proved. Taking homology of this short exact sequence of two-term complexes gives (CT2), including the initial zero. This refines the general [cotangent transitivity sequence](#native-algebra-lemma-exact-sequence-nl) precisely at its left end. ∎

#### Lemma. Cotangent transitivity for filtered complete intersections

The conormal diagram and exact sequence just proved remain valid when $C$ is a filtered colimit of local complete-intersection $B$-algebras. Polynomial presentations may use arbitrary sets of variables when finite sets do not suffice.

**Proof.** Write $C=\varinjlim C_\lambda$. For presentations chosen compatibly with this system, formation of the two-term cotangent complexes and their maps commutes with the filtered colimit; see [Filtered colimits of naive cotangent complexes](#native-algebra-lemma-colimits-nl). Filtered colimits of modules are exact, so the preceding result at each stage gives (CT2).

One can also check directly the only potentially missing injection in (CT1), for any chosen polynomial presentation $Q\twoheadrightarrow C$. An element of $I_Q\cap K^2$ is witnessed by a finite expression as a sum of products of elements of $K$. Only finitely many polynomial variables, coefficients in $C$, and relations equal to zero in $C$ occur in this expression. Lift the coefficients to some $C_\lambda$ and move to a later stage where those finitely many relations vanish. Present that stage over $B$ with the selected elements among its polynomial generators. Apply the preceding intersection equality there. Map its additional polynomial generators back to any chosen polynomial representatives of their images in $C$, leaving the original selected variables fixed. Its relation ideal maps into $K$, and its equality expresses the original element as an element of $I_QK$. Hence $I_Q\cap K^2=I_QK$ also in the chosen presentation of $C$. The rest of (CT1) and its homology sequence follows exactly as above. ∎

#### Lemma. Cartier's equality for differentials (Cartier equality)

For a finitely generated extension of fields $K/k$, both $\Omega_{K/k}$ and $H_1(L_{K/k})$ have finite dimension over $K$, and
$$
\dim_K\Omega_{K/k}-\dim_K H_1(L_{K/k})
=\operatorname{trdeg}_kK.
\tag{FC1}
$$

**Proof.** Let $t_1,\ldots,t_d$ be a transcendence basis and write $E_0=k(t_1,\ldots,t_d)$. Choose a finite tower $E_i=E_{i-1}(\alpha_i)$ ending in $E_r=K$. No separability is assumed. At step $i$, express the coefficients of the monic minimal polynomial of $\alpha_i$ as polynomials in $\alpha_1,\ldots,\alpha_{i-1}$ with coefficients in $E_0$. This is possible because a finite algebraic field extension is generated as an algebra by these elements. Lift those coefficient expressions to obtain triangular polynomials $f_i(T_1,\ldots,T_i)$, monic in $T_i$.

A single nonzero $D\in k[t_1,\ldots,t_d]$ clears all coefficients' denominators. Over $R=k[t_1,\ldots,t_d]_D$, form
$$A=R[T_1,\ldots,T_r]/(f_1,\ldots,f_r).$$
Each successive quotient is finite free over the preceding one because the next equation is monic. After tensoring with $E_0$ these quotients are exactly the fields $E_i$. Their freeness over the domain $R$ makes the map to this localization injective. Thus $A$ is a domain with fraction field $K$.

As a finitely presented $k$-algebra, $A$ has variables $t_1,\ldots,t_d,U,T_1,\ldots,T_r$ and equations $UD-1,f_1,\ldots,f_r$. The first equation is a nonzerodivisor in the polynomial ring; after taking its quotient, each subsequent monic equation is a nonzerodivisor in the corresponding polynomial variable. This explicitly produces a global complete-intersection model with $d+r+1$ variables and $r+1$ equations.

The conormal module is free on those equations by [The conormal module of a global complete intersection](#native-algebra-lemma-relative-global-complete-intersection-conormal). Localize the presentation at the fraction field, using [Localization of the naive cotangent complex](#native-algebra-lemma-localize-nl). The resulting two-term complex is
$$K^{r+1}\longrightarrow K^{d+r+1}.$$
Its kernel is $H_1(L_{K/k})$ and its cokernel is $\Omega_{K/k}$. Both are finite dimensional, and rank-nullity gives (FC1). Equivalently, the complete-intersection dimension calculation gives $\dim A=d$, by [dimension in a polynomial ring](#native-algebra-lemma-dimension-prime-polynomial-ring), and the same Euler characteristic equals that dimension. ∎

#### Lemma. Transitivity of first cotangent homology

For any tower of fields $K\subset L\subset M$, the sequence
$$
\begin{aligned}
0\longrightarrow H_1(L_{L/K})\otimes_L M
&\longrightarrow H_1(L_{M/K})\longrightarrow H_1(L_{M/L})\\
&\longrightarrow\Omega_{L/K}\otimes_L M
\longrightarrow\Omega_{M/K}\longrightarrow\Omega_{M/L}\longrightarrow0
\end{aligned}
\tag{FC2}
$$
is exact, including its first zero. The extensions need not be finitely generated.

**Proof.** Every finitely generated subextension of $M/L$ is the fraction field of a complete-intersection $L$-algebra by the preceding construction. A fraction field is the filtered colimit of localizations at single nonzero elements. Each such localization is again a complete intersection: adjoin a variable $v$ and the equation $vs-1$ after the existing regular sequence. For any two of these subalgebras, choose a finitely generated subfield containing both and then localize its complete-intersection model enough to contain their finite sets of generators. This proves the required directedness under inclusion. Their union is $M$, so $M$ is a filtered colimit of local complete-intersection $L$-algebras. Apply [Cotangent transitivity for filtered complete intersections](#native-more-algebra-lemma-transitive-colimit-lci-at-end) to $K\to L\to M$. Since tensoring an $L$-vector space with $M$ is exact, the leftmost homology term there is $H_1(L_{L/K})\otimes_L M$. This gives (FC2). ∎

#### Lemma. Compatibility of cotangent homology with a quotient

Consider field inclusions $k\subset K\subset K'$ and $k\subset k'\subset K'$ with the same composite map $k\to K'$. Assume that $k'/k$ and $K'/K$ are finitely generated. For the natural comparison maps
$$
\alpha:\Omega_{K/k}\otimes_K K'\longrightarrow\Omega_{K'/k'},\qquad
\beta:H_1(L_{K/k})\otimes_K K'\longrightarrow H_1(L_{K'/k'}),
$$
their four kernel and cokernel spaces are finite dimensional over $K'$, and
$$
\dim\ker\alpha-\dim\operatorname{coker}\alpha
-\dim\ker\beta+\dim\operatorname{coker}\beta
=\operatorname{trdeg}_k k'-\operatorname{trdeg}_K K'.
\tag{FC3}
$$

**Proof.** Factor both maps through the cotangent spaces for $K'/k$:
$$
\begin{aligned}
\alpha&=\alpha_2\alpha_1:
\Omega_{K/k}\otimes_K K'\longrightarrow\Omega_{K'/k}
\longrightarrow\Omega_{K'/k'},\\
\beta&=\beta_2\beta_1:
H_1(L_{K/k})\otimes_K K'\longrightarrow H_1(L_{K'/k})
\longrightarrow H_1(L_{K'/k'}).
\end{aligned}
$$
These factorizations follow from functoriality of derivations and of the presentation cotangent complex.

For the tower $k\subset K\subset K'$, sequence (FC2) shows that $\beta_1$ is injective and that its cokernel embeds in $H_1(L_{K'/K})$. It also identifies $\operatorname{coker}\alpha_1$ with $\Omega_{K'/K}$ and gives
$$
\dim\ker\alpha_1
=\dim H_1(L_{K'/K})-\dim\operatorname{coker}\beta_1.
$$
All these dimensions are finite by (FC1). If $\operatorname{ind}(u)=\dim\ker u-\dim\operatorname{coker}u$ for a map with finite kernel and cokernel, we obtain
$$\operatorname{ind}(\alpha_1)-\operatorname{ind}(\beta_1)
=-\operatorname{trdeg}_K K'.$$

For the tower $k\subset k'\subset K'$, sequence (FC2) identifies $\ker\beta_2$ with $H_1(L_{k'/k})\otimes_{k'}K'$ and embeds $\operatorname{coker}\beta_2$ into $\Omega_{k'/k}\otimes_{k'}K'$. The map $\alpha_2$ is surjective, with
$$
\dim\ker\alpha_2
=\dim_{k'}\Omega_{k'/k}-\dim\operatorname{coker}\beta_2.
$$
Again the spaces involved are finite dimensional, and (FC1) now gives
$$\operatorname{ind}(\alpha_2)-\operatorname{ind}(\beta_2)
=\operatorname{trdeg}_k k'.$$

Finally, finite kernel and cokernel are preserved under composition, and the index is additive. Both assertions follow from the exact sequence
$$
0\to\ker u\to\ker(vu)\to\ker v\to
\operatorname{coker}u\to\operatorname{coker}(vu)\to\operatorname{coker}v\to0.
$$
Apply this to the two factorizations and add the index identities to obtain (FC3). This argument never subtracts dimensions of the potentially infinite spaces $\Omega_{K/k}$ or $H_1(L_{K/k})$ themselves. ∎

#### Proposition. Characterizations of geometric regularity

Let $k$ have characteristic $p>0$, and let $(A,\mathfrak m,K)$ be a Noetherian local $k$-algebra. The following conditions are equivalent:

1. $A$ is geometrically regular over $k$.
2. $A\otimes_k k'$ is regular for every finite intermediate field $k\subset k'\subset k^{1/p}$.
3. $A$ is regular and the boundary $H_1(L_{K/k})\to\mathfrak m/\mathfrak m^2$ is injective.
4. $A$ is regular and the natural map $\Omega_{k/\mathbb F_p}\otimes_k K\to\Omega_{A/\mathbb F_p}\otimes_A K$ is injective.

**Proof.** We first prove that (3) implies (1). It suffices to test finite purely inseparable extensions $k'/k$, by [Criteria for geometric regularity](#native-algebra-lemma-geometrically-regular). For such an extension put $A'=A\otimes_k k'$. The finite faithfully flat map $A\to A'$ is a universal homeomorphism, so $A'$ is local and $\dim A'=\dim A=d$. Write its maximal ideal and residue field as $\mathfrak m'$ and $K'$. The extension $K'/K$ is finite.

For this paragraph all vector spaces are over $K'$. Set
$$
\begin{aligned}
H&=H_1(L_{K/k})\otimes_K K',& H'&=H_1(L_{K'/k'}),\\
U&=(\mathfrak m/\mathfrak m^2)\otimes_K K',& U'&=\mathfrak m'/\mathfrak m'^2,\\
W&=\Omega_{A/k}\otimes_A K',& W'&=\Omega_{A'/k'}\otimes_{A'}K',\\
V&=\Omega_{K/k}\otimes_K K',& V'&=\Omega_{K'/k'}.
\end{aligned}
$$
The quotient cotangent sequences and base change for differentials give a commutative diagram
$$
\begin{array}{cccccccccc}
0\longrightarrow&H&\longrightarrow&U&\longrightarrow&W&\longrightarrow&V&\longrightarrow&0\\
&\downarrow\beta&&\downarrow&&\downarrow\simeq&&\downarrow\alpha&&\\
&H'&\longrightarrow&U'&\longrightarrow&W'&\longrightarrow&V'&\longrightarrow&0.
\end{array}
\tag{GR1}
$$
Only the upper row is asserted to be left exact at $H$; that is hypothesis (3). In particular $H$ is finite dimensional. The middle isomorphism makes $\alpha$ surjective. The [field comparison formula](#native-more-algebra-lemma-gamma-commutative-diagram) gives finite kernel and cokernel for $\beta$ and gives
$$\dim\ker\alpha=\dim\ker\beta-\dim\operatorname{coker}\beta
=\dim H-\dim H'.$$
Thus $H'$ is also finite dimensional. Since $W\simeq W'$ and $\alpha$ is surjective, the kernels of the maps from these middle spaces fit into
$$0\to\ker(W\to V)\to\ker(W'\to V')\to\ker\alpha\to0.$$
The first kernel has dimension $d-\dim H$. The lower row of (GR1) consequently bounds
$$
\dim U'\leq\dim H'+d-\dim H+\dim\ker\alpha=d.
$$
The embedding dimension of a Noetherian local ring is at least its Krull dimension. Hence $A'$ has both dimensions equal to $d$ and is regular. This proves the required purely inseparable tests. Notice that no dimension of $W$ or $V$ was assumed finite.

Next compare (3) and (4). Every field over $\mathbb F_p$ is separable, so its first cotangent homology over $\mathbb F_p$ vanishes; see [Characterizations of separable field extensions](#native-algebra-proposition-characterize-separable-field-extensions). Apply cotangent transitivity to $\mathbb F_p\to A\to K$ and $\mathbb F_p\to k\to K$. It gives exact rows and their natural vertical maps:
$$
\begin{array}{cccccccccc}
0\longrightarrow&H_1(L_{K/k})&\longrightarrow&\Omega_{k/\mathbb F_p}\otimes_k K&\longrightarrow&\Omega_{K/\mathbb F_p}&\longrightarrow&\Omega_{K/k}&\longrightarrow0\\
&\downarrow&&\downarrow&&\Vert&&\downarrow&&\\
0\longrightarrow&\mathfrak m/\mathfrak m^2&\longrightarrow&\Omega_{A/\mathbb F_p}\otimes_A K&\longrightarrow&\Omega_{K/\mathbb F_p}&\longrightarrow&0.&
\end{array}
\tag{GR2}
$$
The kernel of the middle vertical map lies in the image of the upper left injection, because the next vertical map is the identity. The lower left injection then identifies it with the kernel of the first vertical map. Thus those kernels are canonically isomorphic. With the shared regularity hypothesis on $A$, (3) and (4) are equivalent.

We now prove (2) implies (4), by adjoining $p$th roots. Taking $k'=k$ first shows that $A$ is regular. Choose $a_1,\ldots,a_n\in k$ such that $da_1,\ldots,da_n$ are linearly independent in $\Omega_{k/\mathbb F_p}$. By [Degrees of extensions obtained by adjoining p-th roots](#native-algebra-lemma-size-extension-pth-roots),
$$
k'=k(a_1^{1/p},\ldots,a_n^{1/p})
=k[x_1,\ldots,x_n]/(x_1^p-a_1,\ldots,x_n^p-a_n).
$$
Set $A'=A\otimes_k k'$ and use the same notation $\mathfrak m',K'$ as above. Both $A$ and $A'$ are regular of dimension $d$. The equations are a regular sequence, successively monic in distinct variables. For the conormal basis choose $g_i=a_i-x_i^p$, the negatives of the displayed equations. Their differentials relative to $A$ vanish. Hence
$$H_1(L_{A'/A})\simeq(A')^n,\qquad\Omega_{A'/A}\simeq(A')^n.$$
In transitivity over $\mathbb F_p$, the class of $g_i$ maps to $da_i$ in $\Omega_{A/\mathbb F_p}\otimes_A A'$. This specifies the sign of the boundary with the chosen equations. Since $\Omega_{A'/A}$ is free, the terminal short exact sequence splits and remains exact after tensoring with $K'$. Right exactness on the preceding terms gives
$$
(K')^n\xrightarrow{\ e_i\mapsto da_i\ }\Omega_{A/\mathbb F_p}\otimes_A K'
\xrightarrow{v}\Omega_{A'/\mathbb F_p}\otimes_{A'}K'
\longrightarrow(K')^n\longrightarrow0.
\tag{GR3}
$$
In particular $\dim\operatorname{coker}v=n$.

The quotient cotangent sequences over $\mathbb F_p$ are short exact:
$$
\begin{array}{ccccccccc}
0&\longrightarrow&(\mathfrak m/\mathfrak m^2)\otimes_K K'&\longrightarrow&\Omega_{A/\mathbb F_p}\otimes_A K'&\longrightarrow&\Omega_{K/\mathbb F_p}\otimes_K K'&\longrightarrow&0\\
&&\downarrow u&&\downarrow v&&\downarrow w&&\\
0&\longrightarrow&\mathfrak m'/\mathfrak m'^2&\longrightarrow&\Omega_{A'/\mathbb F_p}\otimes_{A'}K'&\longrightarrow&\Omega_{K'/\mathbb F_p}&\longrightarrow&0.
\end{array}
\tag{GR4}
$$
The two spaces for $u$ have dimension $d$, so $u$ has index zero. For $w$, sequence (FC2) for $\mathbb F_p\subset K\subset K'$ and Cartier's equality for the finite extension $K'/K$ show that its kernel and cokernel are finite dimensional of equal dimension. The snake lemma applied to (GR4) therefore gives finite kernel and cokernel for $v$, with index zero. Combining this with (GR3) yields $\dim\ker v=n$. The first map in (GR3) is consequently an isomorphism onto this kernel. In particular the $da_i$ remain independent after mapping into $\Omega_{A/\mathbb F_p}\otimes_A K'$ and hence after mapping into $\Omega_{A/\mathbb F_p}\otimes_A K$.

The differentials $da$, $a\in k$, span $\Omega_{k/\mathbb F_p}$. Every finite-dimensional subspace generated by them has a basis chosen from them. The independence just proved therefore establishes the full injection in (4). Finally (1) immediately implies (2). All four conditions are now equivalent. ∎

#### Lemma. Geometric regularity over a field

Let $(A,\mathfrak m,K)$ be a Noetherian local algebra geometrically regular over a field $k$ of characteristic $p>0$. Let $k\subset F\subset K$ with $F/k$ finitely generated. Suppose a $k$-algebra map $\varphi:k[y_1,\ldots,y_m]\to A$ has residues $\overline y_i\in F$ whose differentials form an $F$-basis of $\Omega_{F/k}$. If $\mathfrak p=\varphi^{-1}(\mathfrak m)$, then
$$k[y_1,\ldots,y_m]_{\mathfrak p}\longrightarrow A$$
is flat, and $A/\mathfrak pA$ is regular.

**Proof.** Write $A_0=k[y]_{\mathfrak p}$, with maximal ideal $\mathfrak m_0$ and residue field $K_0=k(\overline y_1,\ldots,\overline y_m)\subset F$. The natural surjection
$$K_0^m=\Omega_{A_0/k}\otimes_{A_0}K_0\longrightarrow\Omega_{K_0/k}$$
is an isomorphism. Indeed, after extending scalars to $F$ and mapping to $\Omega_{F/k}$, its coordinate vectors become the given basis, so its kernel is zero. The regular local ring $A_0$ is geometrically regular over $k$. The proposition and the quotient cotangent sequence therefore identify
$$H_1(L_{K_0/k})\simeq\mathfrak m_0/\mathfrak m_0^2.$$
In the natural square
$$
\begin{array}{ccc}
H_1(L_{K_0/k})\otimes_{K_0}K&\xrightarrow{\ \sim\ }&(\mathfrak m_0/\mathfrak m_0^2)\otimes_{K_0}K\\
\downarrow&&\downarrow\\
H_1(L_{K/k})&\longrightarrow&\mathfrak m/\mathfrak m^2,
\end{array}
$$
the left arrow is injective by [field cotangent transitivity](#native-more-algebra-lemma-transitivity-gamma), and the bottom arrow is injective by geometric regularity of $A$. Thus the right arrow is injective.

A regular system of parameters of $A_0$ consequently maps to linearly independent cotangent vectors in the regular local ring $A$. Extend those vectors to a basis of $\mathfrak m/\mathfrak m^2$; any lifts form a regular system of parameters of $A$. The chosen images are therefore an $A$-regular sequence, and their quotient is regular. The [flatness criterion over a regular local ring](#native-algebra-lemma-flat-over-regular), together with [regular rings being Cohen–Macaulay](#native-algebra-lemma-regular-ring-cm), proves flatness of $A_0\to A$. Its parameter ideal is $\mathfrak pA$, so the quotient just considered is precisely $A/\mathfrak pA$. ∎

#### Lemma. Base change of regular ring maps (Regular maps and base change)

If $R\to\Lambda$ is regular and $R'$ is a finite type $R$-algebra, then $R'\to\Lambda\otimes_R R'$ is regular.

**Proof.** Flatness survives the base change. For $\mathfrak p'\in\operatorname{Spec}R'$ over $\mathfrak p\in\operatorname{Spec}R$, its fibre is
$$
(\Lambda\otimes_R\kappa(\mathfrak p))
\otimes_{\kappa(\mathfrak p)}\kappa(\mathfrak p').
$$
The first factor is Noetherian and geometrically regular by hypothesis. The residue extension is finitely generated, since $R'/R$ is finite type. The fibre is consequently Noetherian by [Noetherianity under extension of the ground field](#native-algebra-lemma-noetherian-field-extension). Every further finitely generated field extension of $\kappa(\mathfrak p')$ is still finitely generated over $\kappa(\mathfrak p)$, so the same fibre is geometrically regular by the field criterion. This checks every fibre and proves regularity of the base-changed map. ∎

#### Lemma. Composition of regular ring maps (Composition of regular maps)

For regular maps $A\to B\to C$, the composite is regular provided all its fibre rings are Noetherian.

**Proof.** The composite is flat. Fix $\mathfrak p\in\operatorname{Spec}A$ and a finite purely inseparable extension $k/\kappa(\mathfrak p)$. Put
$$B'=B\otimes_A k,\qquad C'=C\otimes_A k.$$
The ring $B'$ is Noetherian and regular by the geometric regularity of the fibre of $B/A$. The ring $C'$ is Noetherian by the assumed Noetherianity of the composite fibre and the finite field extension. The map $B'\to C'$ is flat.

Its fibres are regular as well. In fact, for a prime $\mathfrak q'$ of $B'$ contracting to $\mathfrak q$ of $B$, the residue extension $\kappa(\mathfrak q')/\kappa(\mathfrak q)$ is finite. To see this, obtain $B'$ by first passing to $B\otimes_A\kappa(\mathfrak p)$, a localization of $B/\mathfrak pB$, and then making the finite extension $k/\kappa(\mathfrak p)$. The first operation preserves the residue field at the corresponding prime; the second gives a finite ring extension. Thus
$$C'\otimes_{B'}\kappa(\mathfrak q')
=(C\otimes_B\kappa(\mathfrak q))\otimes_{\kappa(\mathfrak q)}\kappa(\mathfrak q')$$
is regular by the regular-map hypothesis on $B\to C$.

The [flat regular-base and regular-fibre criterion](#native-algebra-lemma-flat-over-regular-with-regular-fibre) now makes $C'$ regular. Since these tests cover every finite purely inseparable extension of every composite residue field, the composite fibres are geometrically regular. Together with flatness and their stated Noetherianity, this proves the claim. The argument does not assume that $A\to\kappa(\mathfrak p)$ is of finite type. ∎

#### Lemma. Permanence of regular ring maps

Suppose $A\to C$ is regular and $B\to C$ is faithfully flat, where $A\to B\to C$ is a factorization. Then $A\to B$ is regular. Equivalently, it is enough that $B\to C$ be flat and surjective on spectra.

**Proof.** Flatness of $A\to B$ follows by faithfully flat descent from flatness of $A\to C$; see [Permanence of flat ring maps](#native-algebra-lemma-flat-permanence). At each $\mathfrak p\in\operatorname{Spec}A$ the fibre map
$$B\otimes_A\kappa(\mathfrak p)\longrightarrow C\otimes_A\kappa(\mathfrak p)$$
is faithfully flat. Its target is Noetherian, so its source is Noetherian by [descent of Noetherianity](#native-algebra-lemma-descent-noetherian). After any finite purely inseparable extension of $\kappa(\mathfrak p)$, the fibre map remains faithfully flat and its target is regular. [Descent of regularity](#native-algebra-lemma-descent-regular) gives regularity of the corresponding source. The field criterion proves that the original source fibre is geometrically regular. This is also the fibrewise [descent of geometric regularity](#native-algebra-lemma-geometrically-regular-descent). ∎

#### B.10.2. Commutative Algebra

These algebraic facts supply the matrix, flatness and finite-generation steps used above. All ring maps preserve the identity, and a regular sequence is required to generate a proper ideal.

#### Lemma. A left inverse for a matrix

Let $A$ be an $n\times m$ matrix over a ring $R$, with $n\geq m$, and let $J$ be the ideal of its maximal minors. Then:

1. Every $f\in J$ admits an $m\times n$ matrix $B$ with $BA=fI_m$.
2. Conversely, such an identity implies $f^m\in J$.

**Proof.** For each set $E$ of $m$ row indices, let $p_E:R^n\to R^m$ be the coordinate projection in increasing index order. Put $A_E=p_EA$. The adjugate identity gives
$$\operatorname{adj}(A_E)p_EA=(\det A_E)I_m.$$
Write $f=\sum_E c_E\det A_E$. Then $B=\sum_E c_E\operatorname{adj}(A_E)p_E$ has the property in (1).

For (2), take determinants in $BA=fI_m$ and use [Cauchy–Binet](#context-algebra-item-cauchy-binet):
$$f^m=\det(BA)=\sum_E\det(B^E)\det(A_E),$$
where $B^E$ selects the columns with indices in $E$. This lies in $J$. If $m=0$, the empty minor is $1$, so $J=R$; the empty matrices and the convention $f^0=1$ make both assertions valid. ∎

#### Lemma. Flatness over a regular local ring

Let $R\to S$ be a homomorphism of Noetherian local rings. Suppose $R$ is regular and a regular system of parameters $x_1,\ldots,x_d$ of $R$ maps to an $S$-regular sequence. Then $S$ is flat over $R$.

**Proof.** The last quotient $S/(x_1,\ldots,x_d)S$ is flat over the field $R/(x_1,\ldots,x_d)$. Now lift flatness one parameter at a time. At step $i$, multiplication by $x_i$ is injective on both $R/(x_1,\ldots,x_{i-1})$ and $S/(x_1,\ldots,x_{i-1})S$, and the quotient of the latter by $x_i$ is already flat over the corresponding quotient of the former. The [local criterion for flatness](#native-algebra-lemma-variant-local-criterion-flatness) therefore gives flatness before that last quotient. Apply this for $i=d,d-1,\ldots,1$.

All these quotient rings are Noetherian local, and the parameters lie in their maximal ideals: properness of the regular-sequence ideal in the local ring $S$ ensures this on the target. Thus the local criterion applies at every step. For $d=0$, the initial field argument is already the conclusion. ∎

#### Lemma. Regular sequences in a polynomial ring

Let $f_1,\ldots,f_r\in R$ generate a proper ideal. The following conditions are equivalent:

1. Every permutation of the sequence is regular.
2. Every subsequence, in its original order, is regular.
3. The sequence $f_1x_1,\ldots,f_rx_r$ is regular in $R[x_1,\ldots,x_r]$.

**Proof.** Under (1), place any chosen subsequence first in a permutation and take that initial segment. This proves (2).

To recover (1) from (2), first note a two-element interchange rule. If $a,b$ are nonzerodivisors and $a,b$ is regular, then $b,a$ is regular. Indeed, if $au=bv$, reduction modulo $a$ gives $v=aw$ because $b$ is a nonzerodivisor modulo $a$. Cancelling $a$ in $a(u-bw)=0$ gives $u=bw$. Thus $a$ is a nonzerodivisor modulo $b$.

Proceed by induction on $r$. All proper subsequences may be permuted by induction. To put $f_s$ last, only its injectivity modulo the other terms remains to be checked. If $s=r$, this is already known. Otherwise quotient by the terms with indices outside $\{s,r\}$. Induction shows that both remaining terms are nonzerodivisors there, and that they occur as the regular pair $f_s,f_r$: permute the first $r-1$ terms to put $f_s$ last among them, without changing their generated ideal. The interchange rule makes $f_r,f_s$ regular in that quotient. This proves injectivity of the desired final term. Any order of its predecessors is regular by induction, proving (1).

For the polynomial assertion, after quotienting by the first $i$ elements $f_jx_j$, the underlying $R$-module splits by monomials:
$$
R[x]/(f_1x_1,\ldots,f_ix_i)
\simeq\bigoplus_{e\in\mathbb N^r}
\left(R/(f_j\mid j\leq i,\ e_j>0)\right)x^e.
$$
Multiplication by $f_{i+1}x_{i+1}$ sends the summand for $e$ to that for $e+(0,\ldots,1,\ldots,0)$, by multiplication by $f_{i+1}$ on its coefficient module. The coefficient ideal depends only on the first $i$ exponents and hence is unchanged. Distinct source monomials have distinct targets. The multiplication is therefore injective exactly when $f_{i+1}$ is a nonzerodivisor modulo every ideal generated by a subset of $f_1,\ldots,f_i$. These are precisely the successive injectivity conditions for all ordered subsequences in (2). Every such subset occurs by taking its exponents positive and the others zero. This proves (2) iff (3). The relevant quotient ideals are proper, by the hypothesis in $R$ and by evaluation at $x_1=\cdots=x_r=0$ in the polynomial ring. ∎

#### Lemma. Finite generation in an Artinian local target

Let $R\to S$ be a ring map, with $S$ Artinian local and residue field $K=S/\mathfrak m$. The map to $S$ is finite, finite type, or essentially finite type, respectively, if and only if the composite map to $K$ has that property.

**Proof.** Each of the three properties passes to a quotient, so consider the converse directions.

If $K$ is a finite $R$-module, take a composition series of $S$ as an $S$-module. Such a finite series exists by [Finite length over an Artinian ring](#native-algebra-lemma-artinian-finite-length), and every factor is $K$. Viewed as a series of $R$-modules, it shows that $S$ is finite over $R$: extensions of finite modules are finite.

If $K$ is a finite type $R$-algebra, lift a finite set of algebra generators to $s_1,\ldots,s_n\in S$. The map $R[X_1,\ldots,X_n]\to K$ defined by their residues is surjective. The finite-module case applied to $R[X]\to S$ makes $S$ finite over this polynomial ring, and hence finite type over $R$.

Finally, suppose $K$ is a localization of a finite type $R$-algebra. Choose lifts to $S$ of a finite generating set for the image of that algebra in $K$, and let $A\subset S$ be the $R$-subalgebra they generate. Put $\mathfrak p=A\cap\mathfrak m$. Then $A/\mathfrak p$ is that same image, and its fraction field is $K$: the given localization is already a field. Elements of $A\setminus\mathfrak p$ map to units of $S$, so the inclusion extends to $A_{\mathfrak p}\to S$. Its map to $K$ is surjective, and the first case makes $S$ finite over $A_{\mathfrak p}$. Since $A$ is finite type over $R$, [composition of essentially finite-type maps](#native-algebra-lemma-composition-essentially-of-finite-type) now shows that $S/R$ is essentially finite type. No finite-generation assumption on the ring $R$ is used. ∎

#### Lemma. Syntomic algebras in a filtered colimit

Any field extension $K/k$ is a filtered colimit of global complete-intersection $k$-algebras. If the extension is separable, smooth $k$-algebras suffice.

**Proof.** We construct such subalgebras containing any given finite subset $E\subset K$. Let $L=k(E)$. The triangular monic construction in the proof of [Cartier's equality](#native-more-algebra-lemma-cartier-equality) gives a domain $A\subset L$ that is a global complete intersection over $k$ and has fraction field $L$. Express each element of $E$ as a fraction in $A$, and invert the product of its finitely many nonzero denominators. The resulting algebra contains $E$. It remains a global complete intersection: for a localization at $s$, adjoin a variable $v$ and append the equation $vs-1$ to the regular sequence presenting $A$.

In the separable case, the finitely generated extension $L/k$ has a separating transcendence basis $t_1,\ldots,t_d$, and $L/k(t)$ is finite separable. Choose a primitive element $\alpha$ with monic minimal polynomial $f(T)\in k(t)[T]$. Clear its coefficients' denominators by a nonzero $D\in k[t]$. The ring $A=k[t]_D[T]/(f)$ embeds in $L$ and has fraction field $L$. Since $f'(\alpha)\ne0$, localizing $A$ at $f'(\alpha)$ makes it étale over the smooth algebra $k[t]_D$ and therefore smooth over $k$. Further localization at the finitely many denominators of the elements of $E$ preserves smoothness and puts $E$ in the algebra. This is the explicit construction behind [Smooth localizations of separable extensions](#native-algebra-lemma-localization-smooth-separable).

The family is directed under inclusion: for two constructed finite type subalgebras, apply the appropriate construction to the union of their finite generating sets. Its union contains every element of $K$ and is contained in $K$, so its filtered colimit is exactly $K$. ∎

### B.11. The additional G-ring permanence argument

Artin approximation over the local polynomial algebra requires permanence of the G-ring condition under essentially finite-type extensions. We prove that permanence through formal-fibre calculations, beginning with the reductions used to test those fibres.

#### G-rings

For a Noetherian local ring $A$ and a prime $\mathfrak q\subset A$, the **formal fibre at $\mathfrak q$** is the $\kappa(\mathfrak q)$-algebra
$$
\widehat A\otimes_A\kappa(\mathfrak q)
=\left((A\setminus\mathfrak q)^{-1}\widehat A\right)\big/\mathfrak q
\left((A\setminus\mathfrak q)^{-1}\widehat A\right).
$$
Here completion uses the maximal ideal of $A$. Completion of a Noetherian ring commutes with quotient by a finitely generated ideal, so this is also
$$\widehat{A/\mathfrak q}\otimes_{A/\mathfrak q}\operatorname{Frac}(A/\mathfrak q).$$
The completion map is flat and its fibres are Noetherian. It is therefore regular exactly when these formal fibres are geometrically regular over their indicated residue fields. In particular, a formal fibre is generally a localization of a **quotient** of $\widehat A$; the quotient cannot be omitted when $\mathfrak q\ne0$.

#### Definition. G-rings

A **G-ring** is a Noetherian ring $R$ such that, for every prime $\mathfrak p$, the local completion map
$$R_{\mathfrak p}\longrightarrow\widehat{R_{\mathfrak p}}$$
is regular. Equivalently, every local ring of $R$ has geometrically regular formal fibres. If $R$ contains $\mathbb Q$, geometric regularity in this test is equivalent to regularity, since all the residue fields have characteristic zero; apply [the field criterion](#native-algebra-lemma-geometrically-regular) and regularity under separable field extension.

#### Lemma. Recognizing a G-ring from a completion

A Noetherian ring $R$ is a G-ring if and only if, for every chain $\mathfrak q\subset\mathfrak p$ of primes, the ring
$$
\widehat{(R/\mathfrak q)_{\mathfrak p}}\otimes_{R/\mathfrak q}\kappa(\mathfrak q)
$$
is geometrically regular over $\kappa(\mathfrak q)$. The completion on the left is at the maximal ideal of $(R/\mathfrak q)_{\mathfrak p}$.

**Proof.** Quotient compatibility of Noetherian completion gives
$$
\widehat{R_{\mathfrak p}}/\mathfrak q\widehat{R_{\mathfrak p}}
\simeq\widehat{(R/\mathfrak q)_{\mathfrak p}}.
$$
Localizing away from $\mathfrak q$ identifies the stated ring with $\widehat{R_{\mathfrak p}}\otimes_R\kappa(\mathfrak q)$. As $\mathfrak q$ runs through the primes contained in $\mathfrak p$, these are exactly the fibres of the completion map of $R_{\mathfrak p}$. The definition now gives both implications. ∎

#### Lemma. G-rings under quasi-finite extensions

Suppose $R\to R'$ is a finite type map of Noetherian rings. Let $\mathfrak q'\subset\mathfrak p'$ be primes of $R'$ contracting to $\mathfrak q\subset\mathfrak p$ in $R$, and assume the map is quasi-finite at $\mathfrak p'$. Then:

1. Geometric regularity of $\widehat{R_{\mathfrak p}}\otimes_R\kappa(\mathfrak q)$ over $\kappa(\mathfrak q)$ implies geometric regularity of $\widehat{R'_{\mathfrak p'}}\otimes_{R'}\kappa(\mathfrak q')$ over $\kappa(\mathfrak q')$.
2. If every formal fibre of $R_{\mathfrak p}$ is geometrically regular, the same holds for $R'_{\mathfrak p'}$.
3. If $R\to R'$ is quasi-finite everywhere and $R$ is a G-ring, then $R'$ is a G-ring.

**Proof.** By [Completion at a quasi-finite prime](#native-algebra-lemma-completion-at-quasi-finite-prime), the completed local ring at $\mathfrak p'$ is a direct factor of the indicated base change:
$$\widehat{R_{\mathfrak p}}\otimes_R R'
\simeq\widehat{R'_{\mathfrak p'}}\times D.$$
Tensor this decomposition, as one of $R'$-algebras, with $\kappa(\mathfrak q')$. Its left-hand side becomes
$$
\bigl(\widehat{R_{\mathfrak p}}\otimes_R\kappa(\mathfrak q)\bigr)
\otimes_{\kappa(\mathfrak q)}\kappa(\mathfrak q').
$$
The residue extension is finitely generated, so this is Noetherian and geometrically regular under the hypothesis of (1), by [Noetherianity under field extension](#native-algebra-lemma-noetherian-field-extension) and [the geometric-regularity criterion](#native-algebra-lemma-geometrically-regular). A direct factor has the same property, since it is localization at an idempotent, before and after every finite field extension. This proves (1). Applying it to every prime $\mathfrak q'\subset\mathfrak p'$ proves (2), and then applying (2) at every $\mathfrak p'$ proves (3). ∎

#### Lemma. Testing geometric regularity of formal fibres

For a Noetherian ring $R$, the G-ring condition is equivalent to the following test: every finite free $R$-algebra $S$ has regular formal fibres at all its local rings.

**Proof.** If $R$ is a G-ring, a finite free algebra is a finite, hence quasi-finite, algebra over $R$. The preceding lemma makes $S$ a G-ring, so its formal fibres are geometrically regular and in particular regular.

Conversely, assume the test. Fix primes $\mathfrak q\subset\mathfrak p$ of $R$ and a finite purely inseparable extension $L/\kappa(\mathfrak q)$. By [Finite free algebras with a prescribed residue extension](#native-algebra-lemma-finite-free-given-residue-field-extension), choose a finite free $R$-algebra $R'$ for which $\mathfrak q'=\mathfrak qR'$ is prime and $\kappa(\mathfrak q')\simeq L$ over $\kappa(\mathfrak q)$.

The finite-extension completion decomposition gives
$$
\widehat{R_{\mathfrak p}}\otimes_R R'
\simeq\prod_{\mathfrak p_i'\mid\mathfrak p}\widehat{R'_{\mathfrak p_i'}},
$$
with a finite index set; see [Completion of a finite ring extension](#native-algebra-lemma-completion-finite-extension). After tensoring over $R'$ with $\kappa(\mathfrak q')=L$, its left side is
$$\bigl(\widehat{R_{\mathfrak p}}\otimes_R\kappa(\mathfrak q)\bigr)
\otimes_{\kappa(\mathfrak q)}L.$$
On the right, a factor is zero unless $\mathfrak q'\subset\mathfrak p_i'$: otherwise some element of $\mathfrak q'$ is already invertible in $R'_{\mathfrak p_i'}$ and is killed by the tensor product. Each remaining factor is the formal fibre of $R'_{\mathfrak p_i'}$ at $\mathfrak q'R'_{\mathfrak p_i'}$, hence regular by the test. The finite product is therefore regular. Every finite purely inseparable extension $L$ has now been checked, so the field criterion makes the original formal fibre geometrically regular. Apply the preceding characterization for all $\mathfrak q\subset\mathfrak p$ to conclude that $R$ is a G-ring. ∎

#### Lemma. Geometric regularity of generic formal fibres in positive characteristic

For a field $k$ of characteristic $p>0$, put $A=k[[x_1,\ldots,x_n]][y_1,\ldots,y_m]$ and $K=\operatorname{Frac}A$. For every prime $\mathfrak p$ of $A$, the generic formal fibre $\widehat{A_{\mathfrak p}}\otimes_A K$ is geometrically regular over $K$.

**Proof.** For a finite purely inseparable extension $L/K$, we prove regularity of $\widehat{A_{\mathfrak p}}\otimes_A L$ by induction on its degree. At degree one, $A$ is regular, its local ring and completion are regular, and the ring in question is a localization of that completion. Use [Regularity and completion](#native-more-algebra-lemma-completion-regular).

For the induction step choose $K\subset M\subset L$ with $[L:M]=p$, and write $L=M(z)$ with $z^p=f\in M\setminus M^p$. Choose a finite domain $B\subset M$ over $A$, with fraction field $M$, such that a $p$-power of every element of $B$ belongs to $A$. Here is a construction: take finitely many generators $\alpha_i$ of $M/K$, choose powers $\alpha_i^{p^{e_i}}=a_i/b_i$ in $K$, and put $B=A[b_i\alpha_i\mid i]$. Each displayed generator has a $p$-power in $A$, so it is integral; a common Frobenius power works for every polynomial in them. The resulting finite algebra has fraction field $M$.

Write $f=b/c$ with $b,c\in B$, $c\ne0$. Replacing $z$ by $cz$ replaces $f$ by $c^pf=c^{p-1}b\in B$ and gives the same extension $L/M$. The new $f$ is still not a $p$th power in $M$. Thus we may assume $f\in B$. Put $C=B[z]/(z^p-f)\subset L$. It is a finite domain over $B$, and every element of $C$ also has a $p$-power in $A$. These integral radicial extensions have unique primes $\mathfrak r\subset B$ and $\mathfrak q\subset C$ above $\mathfrak p$.

The [finite-extension completion formula](#native-algebra-lemma-completion-finite-extension) and uniqueness of these primes identify
$$
T:=\widehat{A_{\mathfrak p}}\otimes_A M
\simeq\widehat{B_{\mathfrak r}}\otimes_B M,
\qquad
\widehat{A_{\mathfrak p}}\otimes_A L\simeq T[z]/(z^p-f).
$$
The induction hypothesis says that $T$ is regular. The domain $B$ is finite type over the complete local ring $k[[x_1,\ldots,x_n]]$. The [derivation lemma in positive characteristic](#native-more-algebra-lemma-find-d) supplies a derivation $D:B\to B$ with $D(f)\ne0$. By [Extending a derivation](#native-more-algebra-lemma-derivation-extends), it extends first to $B_{\mathfrak r}$, then to its completion, and finally to $T$. In the last ring, the nonzero element $D(f)\in B$ is invertible because we have tensored with the fraction field $M$.

Extend $D$ to $T[z]$ by $D(z)=0$. It sends $z^p-f$ to the unit $-D(f)$. The [regular-quotient criterion by a derivation](#native-more-algebra-lemma-degree-p-extension-regular) therefore makes $T[z]/(z^p-f)$ regular. This completes the induction. The purely inseparable field criterion proves geometric regularity of the original generic formal fibre. ∎

#### Proposition. Complete Noetherian rings are G-rings

Every Noetherian complete local ring is a G-ring.

**Proof.** Let $A$ be such a ring and fix $\mathfrak q\subset\mathfrak p$ in $\operatorname{Spec}A$. By quotient compatibility of completion, the formal fibre to be tested is the generic formal fibre of the complete local domain $B=A/\mathfrak q$ at $\mathfrak p/\mathfrak q$. Thus it suffices to establish geometric regularity of all generic formal fibres of every complete local domain.

For such a domain $B$, [the complete-domain structure theorem](#native-algebra-lemma-complete-local-noetherian-domain-finite-over-regular) gives a regular complete local subring $B_0\subset B$, finite in $B$, where $B_0$ is a power-series ring over a field or over a Cohen ring. The generic prime of $B$ contracts to the generic prime of $B_0$. Part (1) of [G-rings under quasi-finite extensions](#native-more-algebra-lemma-g-ring-goes-up-quasi-finite), applied at each chosen upper prime, therefore transfers geometric regularity of the generic formal fibres of $B_0$ to those of $B$. This use requires only the indicated generic fibres of $B_0$, not the whole G-ring assertion for $B_0$.

Let $K_0=\operatorname{Frac}B_0$. The ring $\widehat{(B_0)_{\mathfrak p_0}}\otimes_{B_0}K_0$ is regular: it is a localization of the completion of a regular local ring. If $K_0$ has characteristic zero, this is already geometric regularity. If its characteristic is positive, $B_0$ is a power-series ring over a field, and the preceding lemma, with no polynomial variables, proves geometric regularity. Every required generic fibre is now covered. Returning through $B=A/\mathfrak q$ proves the G-ring condition for all pairs $\mathfrak q\subset\mathfrak p$ of the original $A$. ∎

#### Lemma. Testing the G-ring property at maximal ideals

A Noetherian ring $R$ is a G-ring if and only if every maximal localization $R_{\mathfrak m}$ has geometrically regular formal fibres.

**Proof.** The forward implication is part of the definition. For the converse fix $\mathfrak p\subset\mathfrak m$, with $\mathfrak m$ maximal, and write $S=\widehat{R_{\mathfrak m}}$. Faithful flatness of completion supplies a prime $\mathfrak p'\subset S$ over $\mathfrak pR_{\mathfrak m}$. Put $T=S_{\mathfrak p'}$ and $D=\widehat T$.

By hypothesis $R_{\mathfrak m}\to S$ is regular. The localization $S\to T$ is regular, and $T\to D$ is regular because the preceding proposition makes the complete local ring $S$ a G-ring. Composition gives a regular map $R_{\mathfrak m}\to D$; its fibres are Noetherian since $D$ is Noetherian. The map factors through $R_{\mathfrak p}$, and its fibres and flatness at primes of that localization are unchanged. Hence $R_{\mathfrak p}\to D$ is regular.

There is a compatible local map $\widehat{R_{\mathfrak p}}\to D$. We verify that it is faithfully flat before applying descent. More generally, if $U\to V$ is a flat local map of Noetherian local rings and $W=\widehat V$, then the induced map $\widehat U\to W$ is flat. Indeed $W$ is flat over $U$. A free resolution of the residue field $\kappa_U$ over $U$, tensored with the flat ring $\widehat U$, is a free resolution of the same residue field over $\widehat U$. Consequently
$$\operatorname{Tor}_1^{\widehat U}(W,\kappa_U)
=\operatorname{Tor}_1^U(W,\kappa_U)=0.$$
Apply [the local flatness criterion](#native-algebra-lemma-variant-local-criterion-flatness) to the finite $W$-module $W$, the local map $\widehat U\to W$, and the maximal ideal of $\widehat U$. The residue quotient is a vector space over $\kappa_U$ and hence flat, so $W$ is flat over $\widehat U$. As a local flat map of nonzero local rings, the map is faithfully flat.

Use this observation with $U=R_{\mathfrak p}$ and $V=T$. The original map $U\to T$ is flat and local, as follows from the completion and localization construction. Thus $\widehat{R_{\mathfrak p}}\to D$ is faithfully flat. [Permanence of regular ring maps](#native-more-algebra-lemma-regular-permanence) applied to
$$R_{\mathfrak p}\longrightarrow\widehat{R_{\mathfrak p}}\longrightarrow D$$
now proves regularity of the first map. Since $\mathfrak p$ was arbitrary, $R$ is a G-ring. ∎

#### Lemma. The G-ring property under henselization

If $R$ is a Noetherian local G-ring, both its henselization $R^h$ and its strict henselization $R^{sh}$ are G-rings.

**Proof.** Let $H$ be either henselization and put $D=\widehat H$. The [Noetherian henselization theorem](#native-more-algebra-lemma-henselization-noetherian) says that $H$ is Noetherian local. In the ordinary case it identifies $D$ with $\widehat R$. In the strict case it gives a formally smooth local map $\widehat R\to D$, for the maximal-ideal topology on $D$. By [Formal smoothness and regularity](#native-more-algebra-proposition-fs-regular), this map is regular. Since $R\to\widehat R$ is regular, composition shows in both cases that $R\to D$ is regular; the required Noetherian fibre condition holds because $D$ is Noetherian.

Fix $\mathfrak p\in\operatorname{Spec}R$. The [henselization fibre description](#native-more-algebra-lemma-fibres-henselization) gives a finite product
$$H\otimes_R\kappa(\mathfrak p)
\simeq\prod_{i=1}^s\kappa(\mathfrak q_i),$$
where the $\mathfrak q_i$ are the primes of $H$ over $\mathfrak p$ and each residue extension is separable algebraic. Tensoring this equality over $H$ with $D$ yields
$$D\otimes_R\kappa(\mathfrak p)
\simeq\prod_{i=1}^s\left(D\otimes_H\kappa(\mathfrak q_i)\right).$$
The left-hand side is geometrically regular over $\kappa(\mathfrak p)$, since $R\to D$ is regular. Each factor has that same property. The coefficient-field change from $\kappa(\mathfrak p)$ to the separable algebraic field $\kappa(\mathfrak q_i)$ preserves geometric regularity in this situation, by [Geometric regularity under separable algebraic extensions](#native-algebra-lemma-geometrically-regular-over-separable-algebraic). Thus every formal fibre of the local ring $H$ is geometrically regular over its own residue field. The maximal-ideal test proves that $H$ is a G-ring, in both cases. ∎

#### Lemma. Geometric regularity of polynomial formal fibres in positive characteristic

Let $A$ be a Noetherian complete local domain whose fraction field $K$ has characteristic $p>0$. Let $\mathfrak q\subset A[x]$ be maximal, with contraction the maximal ideal of $A$. If $0\ne\mathfrak r\subset\mathfrak q$ and $\mathfrak r\cap A=0$, then
$$F=\widehat{A[x]_{\mathfrak q}}\otimes_{A[x]}\kappa(\mathfrak r)$$
is geometrically regular over $\kappa(\mathfrak r)$.

**Proof.** Localizing by the nonzero elements of $A$ sends $\mathfrak r$ to a nonzero prime of the principal ideal domain $K[x]$. Thus $\kappa(\mathfrak r)$ is finite over $K$. Fix a finite purely inseparable extension $L/\kappa(\mathfrak r)$; we will show that $F\otimes_{\kappa(\mathfrak r)}L$ is regular.

First choose a domain $B$, finite over $A$, contained in $L$, with fraction field $L$. To construct it, take finitely many algebraic generators of $L/K$ and multiply each by a nonzero element of $A$ that clears the denominators of its monic equation. The scaled generators are integral over $A$ and still generate $L$ as a field. Their $A$-algebra is the required $B$. A finite algebra over a complete Noetherian local ring is a product of complete local rings; because $B$ is a domain, it has just one factor. Hence $B$ is itself complete local.

Map $B[x]$ to $L$ by sending $x$ to its image in $\kappa(\mathfrak r)\subset L$, and denote the kernel by $\mathfrak r'$. The fraction field of the image is $L$, so $\kappa(\mathfrak r')=L$. Moreover $\mathfrak r'\cap B=0$ and $\mathfrak r'\ne0$: over $\operatorname{Frac}B=L$ its ideal is generated by a linear polynomial. Write $\mathfrak q_i$ for the finitely many primes of $B[x]$ above $\mathfrak q$. By [Completion of a finite ring extension](#native-algebra-lemma-completion-finite-extension),
$$
\begin{aligned}
F\otimes_{\kappa(\mathfrak r)}L
&=\widehat{A[x]_{\mathfrak q}}\otimes_{A[x]}L\\
&\simeq\prod_i\left(\widehat{B[x]_{\mathfrak q_i}}
\otimes_{B[x]}\kappa(\mathfrak r')\right).
\end{aligned}
$$
Terms with $\mathfrak r'\not\subset\mathfrak q_i$ vanish, since some element killed in $\kappa(\mathfrak r')$ is already invertible in that factor. Every remaining $\mathfrak q_i$ is maximal and lies over the maximal ideal of $B$. Thus it suffices to prove ordinary regularity in the special case $K=\kappa(\mathfrak r)$: the replacement $(B,\mathfrak q_i,\mathfrak r')$ has precisely that property.

In this special case $\mathfrak rK[x]=(x-f)$ for some $f\in K$. Set
$$T=\widehat{A[x]_{\mathfrak q}}\otimes_A K.$$
The map $A\to A[x]_{\mathfrak q}$ is formally smooth: polynomial algebras have the lifting property, and localization preserves it because a lift of a unit modulo a nilpotent ideal is a unit. Its composite with completion is formally smooth for the maximal-ideal topology, by [Formal smoothness and completion](#native-more-algebra-lemma-formally-smooth-completion). [Formal smoothness and regularity](#native-more-algebra-proposition-fs-regular) makes this composite regular; hence its generic fibre $T$ is regular.

The $A$-derivation $\partial/\partial x$ extends through localization and completion and then to $T$, by [Extending a derivation](#native-more-algebra-lemma-derivation-extends). It kills $K$ and sends $x-f$ to $1$. Therefore [Regularity of a quotient](#native-more-algebra-lemma-quotient-regular) shows that
$$F=T/(x-f)$$
is regular. Applying this argument to all the surviving factors above proves regularity after every finite purely inseparable extension $L$. The field criterion now gives the asserted geometric regularity. ∎

#### Proposition. The G-ring property for finite-type algebras

If $R$ is a G-ring and $S$ is an essentially finite-type $R$-algebra, then $S$ is a G-ring.

**Proof.** A localization of a G-ring satisfies the definition, since its local rings are local rings of the original ring. Quotients preserve the G-ring property by [G-rings under quasi-finite extensions](#native-more-algebra-lemma-g-ring-goes-up-quasi-finite). Presenting a finite-type algebra as a quotient of a polynomial algebra, and then adding its variables one at a time, reduces the assertion to $S=R[x]$.

By [Testing the G-ring property at maximal ideals](#native-more-algebra-lemma-check-g-ring-maximal-ideals), fix a maximal $\mathfrak q\subset R[x]$ and prove regularity of the completion map of $T=R[x]_{\mathfrak q}$. Put $\mathfrak p=\mathfrak q\cap R$. Replacing $R$ by $R_{\mathfrak p}$ does not change $T$; thus $R$ is now local, with maximal ideal $\mathfrak m=\mathfrak pR_{\mathfrak p}$, and $\mathfrak q$ lies over $\mathfrak m$. In $\widehat R[x]$ there is a unique prime $\mathfrak q'$ over $\mathfrak q$: modulo $\mathfrak m$ the extension is the identity on $(R/\mathfrak m)[x]$. This prime is maximal. Put $T'=\widehat R[x]_{\mathfrak q'}$.

The map $T\to T'$ is regular, since it is obtained from the regular map $R\to\widehat R$ by polynomial base change and localization. It is also local. The induced map $\widehat T\to\widehat{T'}$ is faithfully flat, by the completion argument proved in the maximal-ideal test. Consequently, if $T'\to\widehat{T'}$ is regular, composition and faithfully flat descent of regularity give regularity of $T\to\widehat T$. We have reduced the problem to a complete Noetherian local base $R$.

Fix a prime $\mathfrak r\subset\mathfrak q$. We must prove geometric regularity of
$$\widehat{R[x]_{\mathfrak q}}\otimes_{R[x]}\kappa(\mathfrak r).$$
Let $\mathfrak p=\mathfrak r\cap R$. Quotient compatibility of completion identifies this ring with the corresponding formal fibre for $(R/\mathfrak p)[x]$, at the images of $\mathfrak r$ and $\mathfrak q$; its residue field is unchanged. We may therefore assume that $R$ is a complete local domain and $\mathfrak r\cap R=0$.

Choose a regular complete local subring $R_0\subset R$, finite in $R$, using [A complete local domain finite over a regular ring](#native-algebra-lemma-complete-local-noetherian-domain-finite-over-regular). Contraction sends our chain to $\mathfrak r_0\subset\mathfrak q_0\subset R_0[x]$, with $\mathfrak r_0\cap R_0=0$ and $\mathfrak q_0$ maximal over the maximal ideal of $R_0$. Part (1) of the quasi-finite extension lemma transfers geometric regularity of this particular formal fibre of $R_0[x]$ to the desired fibre of $R[x]$. Thus we need only treat a regular complete local base. This reduction uses the stated fibre-transfer result, without assuming the G-ring property for the polynomial algebra being proved.

For such a base, put $K=\operatorname{Frac}R$ and $C=\widehat{R[x]_{\mathfrak q}}$. The ring $R[x]$ is regular, as are its local ring at $\mathfrak q$ and the completion $C$; use [Regularity ascends along a regular ring map](#native-algebra-lemma-regular-goes-up) and [Regularity and completion](#native-more-algebra-lemma-completion-regular). There are the following cases.

If $\operatorname{char}K=0$ and $\mathfrak r=0$, the formal fibre is a localization of $C$, hence regular and geometrically regular over the characteristic-zero field $K(x)$.

If $\operatorname{char}K=0$ and $\mathfrak r\ne0$, write $\mathfrak rK[x]=(f)$ for a monic irreducible polynomial $f\in K[x]$. Then $\kappa(\mathfrak r)=K[x]/(f)$, and the formal fibre is
$$\left(C\otimes_R K\right)/(f).$$
The ambient ring $C\otimes_R K$ is regular. Extend $\partial/\partial x$ from $R[x]$ to it by localization and completion. Since $f$ is separable, its derivative has nonzero image in the field $K[x]/(f)$, so this derivative becomes a unit in the displayed quotient. The regular-quotient criterion proves regularity of the fibre. Its coefficient field has characteristic zero, which gives geometric regularity. This quotient argument is essential: for nonzero $\mathfrak r$ the formal fibre is not merely a localization of $C$.

Finally suppose $\operatorname{char}K=p>0$. The regular complete local ring has the form $R=k[[x_1,\ldots,x_n]]$. If $\mathfrak r=0$, apply [Geometric regularity of generic formal fibres in positive characteristic](#native-more-algebra-lemma-helper-g-ring), with the one polynomial variable $x$. If $\mathfrak r\ne0$, apply the preceding lemma on polynomial formal fibres. Thus all the formal fibres of $T$ are geometrically regular. The completion map is flat, so it is regular. Returning through the reductions proves the proposition. ∎

#### Remark. Failure of the G-ring property under completion

The G-ring property does not persist under completion with respect to an arbitrary ideal. In particular, there are a G-ring $R$ and an ideal $I$ for which the $I$-adic completion is not a G-ring. A construction is given by Jun-ichi Nishimura, [*On ideal-adic completion of Noetherian rings*](https://stacks.math.columbia.edu/bibliography/Nishimura), *J. Math. Kyoto Univ.* **21** (1981), no. 1, 153–169. The final section of Tiberiu Dumitrescu, [*On some examples of atomic domains and of $G$-rings*](https://stacks.math.columbia.edu/bibliography/Dumitrescu), *Comm. Algebra* **28** (2000), no. 3, 1115–1123, develops this example further. These are references for the counterexamples; no counterexample construction is supplied in this remark.

#### Proposition. Examples and permanence of G-rings

Each of the following is a G-ring:

1. a field;
2. a Noetherian complete local ring;
3. $\mathbb Z$;
4. a Dedekind domain whose fraction field has characteristic zero;
5. a finite-type algebra over any ring in the preceding classes.

**Proof.** A field is a complete Noetherian local ring. The second assertion was proved in [Complete Noetherian rings are G-rings](#native-more-algebra-proposition-noetherian-complete-g-ring).

For a Dedekind domain $R$ as in (4), localization at the zero prime is a field. At a nonzero prime it is a discrete valuation ring $V$, and $\widehat V$ is again a discrete valuation ring. The closed formal fibre is the residue field of $V$, over itself. The generic formal fibre is $\operatorname{Frac}(\widehat V)$ over $\operatorname{Frac}V$; it is geometrically regular because the latter field has characteristic zero. Both formal fibres are therefore geometrically regular, proving (4). The case $\mathbb Z$ follows since it is such a Dedekind domain. The finite-type assertion is the preceding proposition. ∎

### Additional proofs of the supporting constructions

The following results give the supporting arguments for the approximation theorem. Where a complete proof already appears earlier in this lesson, the reference identifies that result and explains the match of hypotheses and conclusions. The remaining supporting units retain their individual source references.

#### Versality and algebraicity criteria

#### Lemma. Approximation of a marked family with its associated graded algebra

Let $S$ be locally Noetherian and let $\mathcal X\to(\mathrm{Sch}/S)_{fppf}$ be a category fibred in groupoids. Suppose $x\in\mathcal X(R)$, where $(R,\mathfrak m_R)$ is a complete Noetherian local ring and its residue field $k$ defines a finite-type morphism $\operatorname{Spec}k\to S$. Denote the image point by $s$. Assume that $\mathcal O_{S,s}$ is a G-ring and that $\mathcal X$ is limit preserving on objects.

For every $N\geq1$ there are an $S$-algebra $A$ of finite type, a maximal ideal $\mathfrak m_A$, an object $x_A\in\mathcal X(A)$, and an $S$-algebra isomorphism
$$R/\mathfrak m_R^N\simeq A/\mathfrak m_A^N$$
under which the restricted objects $x$ and $x_A$ are isomorphic. One can require, in addition, an isomorphism of graded $k$-algebras
$$\operatorname{gr}_{\mathfrak m_R}R\simeq\operatorname{gr}_{\mathfrak m_A}A,$$
using the residue-field identification induced by the first map.

**Proof.** This is [Theorem 6.1 in B.6.1](#reader-family-approximation), whose full proof applies to precisely this category, base, object and integer $N$. To identify every step of the construction: it first descends $x$ to a finite-type algebra $C$ on an affine chart $\operatorname{Spec}\Lambda\subset S$. Residue-field generators and generators of $\mathfrak m_R$ then give a surjection
$$P=\widehat{\Lambda[z_1,\ldots,z_e]_{\mathfrak n}}\longrightarrow R.$$
The successive-order lifting argument in that proof establishes this surjection directly. Finite generators of its kernel and of their relation module turn the presentation and the map from $C$ into one finite polynomial system.

The G-ring theorem and pointed approximation solve this system in an étale neighbourhood, retaining its exact relations and matching the formal coefficients to any chosen sufficiently high order. [Appendix A, Lemmas A.1–A.2](#appendix-a-artin-rees-perturbation-and-graded-quotients) then give the associated graded algebra comparison. Finally the last two paragraphs of B.6.1 descend the algebra and object to a finite-type $\Lambda$-algebra, prove that the selected point is maximal with residue field exactly $k$, and carry back both the finite-order marking and the graded isomorphism. Thus none of the six requested data is lost in the passage from the essentially finite-type intermediate ring to $A$. ∎

#### Commutative algebra and regularity

#### Definition. Smoothness at a prime ideal

For a homomorphism $R\to S$ and $\mathfrak q\in\operatorname{Spec}S$, smoothness **at $\mathfrak q$** means that $R\to S_g$ is smooth for some $g\in S\setminus\mathfrak q$. Thus the definition requires a smooth principal neighbourhood of the point.

#### Lemma. Localization of the naive cotangent complex

For $A\to B$ and a multiplicative subset $U\subset B$, localization gives a quasi-isomorphism
$$\mathrm{NL}_{B/A}\otimes_B U^{-1}B\longrightarrow\mathrm{NL}_{U^{-1}B/A}.$$

**Proof.** The principal localizations $B_u$, indexed by $u\in U$ with common later terms obtained by taking products, have colimit $U^{-1}B$. For each $u$, [The cotangent complex of a principal localization](#native-algebra-lemma-principal-localization-nl) gives the required comparison over $B_u$. Take their filtered colimit. Tensor product commutes with this colimit on the left; [Filtered colimits of naive cotangent complexes](#native-algebra-lemma-colimits-nl) identifies the right-hand side. Filtered colimits of modules are exact, so they preserve the homology isomorphisms of these two-term complexes. This proves the assertion for any multiplicative set, without a finiteness hypothesis on it. ∎

#### Definition. Smooth ring maps

A homomorphism $R\to S$ is **smooth** if it is finitely presented and its naive cotangent complex has zero first homology and finite projective degree-zero homology. Equivalently,
$$H_1(\mathrm{NL}_{S/R})=0,\qquad \Omega_{S/R}\text{ is finite projective over }S,$$
and $S$ is finitely presented over $R$. This says that the complex is quasi-isomorphic to a finite projective module concentrated in degree zero.

#### Lemma. The transitivity sequence for the naive cotangent complex (Jacobi-Zariski sequence)

Let $A\to B\to C$ be homomorphisms. Choose polynomial presentations
$$P=A[x_s\mid s\in S]\twoheadrightarrow B,\qquad B[y_t\mid t\in T]\twoheadrightarrow C$$
with kernels $I$ and $J$. The variable sets may be infinite. Put $Q=P[y_t\mid t\in T]$ and $K=\ker(Q\to C)$. There is a canonical commutative diagram with exact rows
$$
\begin{array}{ccccccccc}
&&(I/I^2)\otimes_B C&\longrightarrow&K/K^2&\longrightarrow&J/J^2&\longrightarrow&0\\
&&\downarrow d&&\downarrow d&&\downarrow d&&\\
0&\longrightarrow&\Omega_{P/A}\otimes_P C&\longrightarrow&\Omega_{Q/A}\otimes_Q C&\longrightarrow&\Omega_{B[y]/B}\otimes_{B[y]} C&\longrightarrow&0.
\end{array}
$$
It gives the exact sequence
$$
\begin{aligned}
H_1(\mathrm{NL}_{B/A}\otimes_B C)&\longrightarrow H_1(L_{C/A})
\longrightarrow H_1(L_{C/B})\\
&\longrightarrow\Omega_{B/A}\otimes_B C
\longrightarrow\Omega_{C/A}\longrightarrow\Omega_{C/B}\longrightarrow0.
\end{aligned}
$$
The first tensor product is the ordinary tensor product of a two-term presentation complex. If
$$\operatorname{Tor}_1^B(\Omega_{B/A},C)=\operatorname{Tor}_2^B(\Omega_{B/A},C)=0,$$
its first homology identifies with $H_1(L_{B/A})\otimes_B C$.

**Proof.** The differential row separates the free basis $\{dx_s,dy_t\}$ into its two groups. Its first map includes the $dx_s$ summands, and its last map kills those summands and carries each $dy_t$ to the corresponding relative differential.

For the conormal row, put $I_Q=IQ$. The surjection $Q\to B[y]$ has kernel $I_Q$, so $K/I_Q=J$. The map $K/K^2\to J/J^2$ is onto and has kernel $(I_Q+K^2)/K^2$. The left-hand module is canonically
$$E=(I/I^2)\otimes_B C=I_Q/I_QK,$$
and inclusion of $I_Q$ into $K$ induces its surjection onto that kernel. These are the asserted maps. Universal derivations commute with the polynomial maps and with passage to $C$, proving commutativity.

To obtain the homology sequence without assuming that $E\to K/K^2$ is injective, let $D$ be its image. Its kernel consists of elements represented in $I_Q\cap K^2$, whose differential is zero after tensoring with $C$. Therefore the left vertical differential factors through $D$. Replacing $E$ by $D$ gives a short exact sequence of two-term complexes, with the middle and right complexes representing $\mathrm{NL}_{C/A}$ and $\mathrm{NL}_{C/B}$. The homology sequence of that short exact sequence has the claimed form with $H_1(D\to\Omega_{P/A}\otimes_P C)$ at the left.

Every degree-one cycle of this last complex lifts to a degree-one cycle of $E\to\Omega_{P/A}\otimes_P C$, because the map in degree zero is the identity. Their first homologies thus map surjectively. Their degree-zero homologies agree, and are $\Omega_{B/A}\otimes_B C$. Substitution gives the displayed exact sequence with its stated first term. The comparison of polynomial presentations identifies all these homology modules with the indicated cotangent homology groups.

For the last assertion, write a presentation complex for $B/A$ as $N^{-1}\to N^0$, with $N^0$ free, and denote its image by $M$. The exact sequence
$$0\longrightarrow M\longrightarrow N^0\longrightarrow\Omega_{B/A}\longrightarrow0$$
remains left exact after tensoring with $C$ when $\operatorname{Tor}_1^B(\Omega_{B/A},C)=0$. Since $N^0$ is free, its Tor sequence also gives
$$\operatorname{Tor}_1^B(M,C)\simeq\operatorname{Tor}_2^B(\Omega_{B/A},C)=0.$$
Tensoring $0\to H_1(L_{B/A})\to N^{-1}\to M\to0$ consequently remains exact on the left as well. Combining the two sequences identifies the kernel of $N^{-1}\otimes_B C\to N^0\otimes_B C$ with $H_1(L_{B/A})\otimes_B C$, as required. ∎

#### Lemma. The conormal module of a syntomic presentation

Suppose $S=R[x_1,\ldots,x_n]/I$ with $I$ finitely generated, and let $g\in S$. If $S_g$ is syntomic over $R$, then $(I/I^2)_g$ is finite projective as an $S_g$-module.

**Proof.** The [local syntomic criterion](#native-algebra-lemma-syntomic) covers $\operatorname{Spec}S_g$ by principal opens on which the algebra is a relative global complete intersection. On each such open, compare its complete-intersection presentation with the given presentation. [Localization of a conormal module](#native-algebra-lemma-conormal-module-localize) gives the comparison after adding finite free summands, and [The conormal module of a global complete intersection](#native-algebra-lemma-relative-global-complete-intersection-conormal) makes the complete-intersection conormal finite free. Hence the conormal for the given presentation is finite projective on each open. Take a finite subcover and apply the local [finite-projective criterion](#native-algebra-lemma-finite-projective). This proves the claim over the whole ring $S_g$. ∎

#### Lemma. A presentation realizing a basis of the conormal module

Let $S$ be a finitely presented $R$-algebra. If it has a presentation $S=R[x_1,\ldots,x_n]/I$ with $I/I^2$ free over $S$, then it has a finite presentation whose defining equations themselves give a basis of its conormal module.

**Proof.** Put $P=R[x_1,\ldots,x_n]$. Finite presentation of $S$ makes $I$ finitely generated, by [Independence of finite presentation](#native-algebra-lemma-finite-presentation-independent). Choose $f_1,\ldots,f_c\in I$ whose classes are a basis of the finite free module $I/I^2$, and set $F=(f_1,\ldots,f_c)$. Then $I=F+I^2$, so the finite $P$-module $I/F$ satisfies $I(I/F)=I/F$. The determinant form of [Nakayama's lemma](#native-algebra-lemma-nak) gives $g\in1+I$ with $gI\subset F$. Thus $I_g=F_g$, while $g$ has image $1$ in $S$.

It follows that
$$S\simeq P_g/F_g\simeq P[t]/(f_1,\ldots,f_c,gt-1).$$
Write $J=(f_1,\ldots,f_c,gt-1)\subset P[t]$. To verify the promised basis explicitly, consider
$$J/J^2\longrightarrow (I/I^2)\oplus S,\qquad
[h]\longmapsto\left([h(1)],\left[\frac{\partial h}{\partial t}(1)\right]\right).$$
For $h\in J$, evaluation at $1$ lies in $I$. Evaluation of a product of two elements of $J$ lies in $I^2$, and its derivative evaluates into $I$, so the map is well-defined. It is $S$-linear by the product rule. The images of the defining equations are $([f_i],0)$ and $([g-1],1)$. These form a basis of $(I/I^2)\oplus S$. Since their classes also generate $J/J^2$, the map is an isomorphism and their classes are a basis there. The new presentation has $c+1$ equations and $n+1$ variables, proving the assertion. ∎

#### Lemma. Localization of a relative complete intersection

Write $S=R[x_1,\ldots,x_n]/(f_1,\ldots,f_c)$. In each situation below, there is a polynomial $h$ with image $g\in S$ such that
$$S_g\simeq R[x_1,\ldots,x_n,z]/(f_1,\ldots,f_c,hz-1)$$
is a relative global complete intersection, with the stated control on $g$:

1. If $I\subset R$ and every nonempty fibre of $S/IS$ over $R/I$ has dimension $n-c$, one can arrange $g\equiv1\pmod{IS}$.
2. If $\mathfrak p\subset R$ and $\dim(S\otimes_R\kappa(\mathfrak p))=n-c$, one can arrange that $g$ is a unit on this entire fibre.
3. If $\mathfrak q\subset S$ lies over $\mathfrak p$ and $\dim_{\mathfrak q}(S/R)=n-c$, one can arrange $g\notin\mathfrak q$.

**Proof.** By [The open fibre-dimension bound](#native-algebra-lemma-dimension-fibres-bounded-open-upstairs), the points where the fibre dimension is at most $n-c$ form an open set $W\subset\operatorname{Spec}S$. Write its complement as $V(J)$.

In (1), $W$ contains $V(IS)$, so $J+IS=S$. Choose $g\in J$ with $g\equiv1$ modulo $IS$. In (2), the extension of $J$ to $S\otimes_R\kappa(\mathfrak p)$ is the unit ideal. Express $1$ as a finite combination of images of elements of $J$, and clear the denominators from $R\setminus\mathfrak p$. This gives $g\in J$ whose image in the fibre is the image of an element of $R\setminus\mathfrak p$, hence a unit. In (3), choose $g\in J\setminus\mathfrak q$, since $\mathfrak q\in W$.

In every case $D(g)\subset W$. Lift $g$ to $h\in R[x]$. The displayed presentation has $n+1$ variables and $c+1$ equations, and every nonempty fibre has dimension at most $n-c$ by its construction. Conversely a nonzero quotient of a polynomial ring in $n+1$ variables over a field by $c+1$ equations has dimension at least $n-c$, by the height bound for a finitely generated ideal. Thus each such fibre has dimension exactly $n-c$. This is the required relative global complete-intersection presentation, with all the claimed conditions on $g$. ∎

#### Lemma. Composition of syntomic ring maps

For homomorphisms $R\to S\to T$:

1. If both maps are syntomic, so is $R\to T$.
2. If both maps are relative global complete intersections, so is $R\to T$.

**Proof.** First suppose
$$S=R[x_1,\ldots,x_n]/(f_1,\ldots,f_c),\qquad
T=S[y_1,\ldots,y_m]/(h_1,\ldots,h_d)$$
are presentations of the kind in (2). Lifting the coefficients of the $h_j$ to $R[x]$ gives
$$T=R[x_1,\ldots,x_n,y_1,\ldots,y_m]/(f_1,\ldots,f_c,\widetilde h_1,\ldots,\widetilde h_d).$$
For a residue field $k$ of $R$, the nonempty base fibre has dimension $n-c$, and the nonempty fibres above it of the second map have dimension $m-d$. [The base–fibre dimension bound](#native-algebra-lemma-dimension-base-fibre-total) therefore gives dimension at most $(n-c)+(m-d)$ for $T\otimes_R k$. When this algebra is nonzero, its displayed presentation gives the reverse inequality by the height bound. Hence each nonempty fibre has exactly that dimension, proving (2).

Now assume the maps are syntomic and choose $\mathfrak q'\in\operatorname{Spec}T$, with image $\mathfrak q$ in $S$. The [local syntomic criterion](#native-algebra-lemma-syntomic) supplies $g'\in T\setminus\mathfrak q'$ and $g\in S\setminus\mathfrak q$ for which $S\to T_{g'}$ and $R\to S_g$ are relative global complete intersections. [Base change](#native-algebra-lemma-base-change-relative-global-complete-intersection) makes $S_g\to T_{gg'}$ one as well. By (2), $R\to T_{gg'}$ is a relative global complete intersection, hence syntomic. These neighbourhoods cover $\operatorname{Spec}T$; choose a finite subcover and apply [Locality of syntomic ring maps](#native-algebra-lemma-local-syntomic). This proves (1). ∎

#### Lemma. Smooth algebras are syntomic

If $R\to S$ is smooth, then $\operatorname{Spec}S$ admits a cover by principal opens $D(g)$ for which $S_g$ is standard smooth over $R$. In particular, every smooth ring map is syntomic.

**Proof.** The full local-standard-form argument is *Formally smooth, unramified and étale ring maps*, Theorem 5.1. It applies to an arbitrary base ring. Section 4 of that lesson proves that its definition of smoothness agrees with the naive-cotangent definition used here. The theorem's proof starts with the finite projective conormal module, chooses a basis at the given prime, uses Nakayama in the localized polynomial ring to generate the actual ideal, clears finitely many denominators, and adjoins an inverse variable to give a standard smooth presentation. Thus it supplies the asserted principal neighbourhood at every prime, including rank zero.

By [Standard smooth algebras](#native-algebra-lemma-standard-smooth), each resulting chart is a relative global complete intersection. [The complete-intersection criterion](#native-algebra-lemma-relative-global-complete-intersection) makes every chart syntomic. A finite subcover and [locality](#native-algebra-lemma-local-syntomic) then make $R\to S$ syntomic. For the zero algebra the spectrum is empty and the same local assertion is vacuous. ∎

#### Lemma. Local criteria for a syntomic algebra

Let $R\to S$, and let $\mathfrak q\subset S$ contract to $\mathfrak p\subset R$. The following conditions are equivalent:

1. Some $g\in S\setminus\mathfrak q$ makes $R\to S_g$ syntomic.
2. Some $g\in S\setminus\mathfrak q$ makes $S_g$ a relative global complete intersection over $R$.
3. There is a finitely presented neighbourhood $R\to S_g$ with $g\notin\mathfrak q$, the map $R_{\mathfrak p}\to S_{\mathfrak q}$ is flat, and the fibre local ring $S_{\mathfrak q}/\mathfrak pS_{\mathfrak q}$ is a complete intersection over $\kappa(\mathfrak p)$.

**Proof.** Condition (1) gives (3) by [Complete intersections at a prime](#native-algebra-lemma-lci-at-prime). The implication (2) to (1) is the [relative global complete-intersection criterion](#native-algebra-lemma-relative-global-complete-intersection). It remains to start with (3) and construct the presentation in (2).

First replace $S$ by its finitely presented neighbourhood, and write $S=P/I$, where $P=R[x_1,\ldots,x_n]$ and $I$ is finitely generated. Let $\mathfrak q'$ be the inverse image of $\mathfrak q$ in $P$, and put $k=\kappa(\mathfrak p)$. The fibre presentation has ideal $\overline I\subset k[x]$, and let $\overline{\mathfrak q}'$ be its indicated prime. By [The field complete-intersection criterion](#native-algebra-lemma-lci), choose $f_1,\ldots,f_c\in I$ whose images form a minimal generating set of $\overline I_{\overline{\mathfrak q}'}$. They generate that ideal and are a regular sequence there. Such lifts can be chosen in $I$ because the images of $I$ span its minimal-generator vector space.

Set $S'=P/(f_1,\ldots,f_c)$ and $J=\ker(S'\to S)$. This kernel is finitely generated. Localize the exact sequence $0\to J\to S'\to S\to0$ at $\mathfrak q'$. Its last term is $S_{\mathfrak q}$, which is flat over $R$ by (3) and localization of the base. Tensoring with $k$ is therefore still injective at its first term. By the chosen generators, the map between the two fibre local rings is an isomorphism. Hence
$$J_{\mathfrak q'}\otimes_R k=J_{\mathfrak q'}/\mathfrak pJ_{\mathfrak q'}=0.$$
Nakayama applies to this finite module over the local ring $S'_{\mathfrak q'}$, since $\mathfrak p$ is contained in its maximal ideal. It gives $J_{\mathfrak q'}=0$. A product of annihilating denominators for a finite generating set of $J$ now gives $h\in P\setminus\mathfrak q'$ with $J_h=0$, so $S'_h\simeq S_h$.

The regular sequence in the fibre polynomial local ring gives fibre dimension $n-c$ at the chosen point. Apply the preceding localization lemma to $S'$ and that point, and combine its denominator with $h$. The resulting neighbourhood is a relative global complete intersection and still contains $\mathfrak q$. This proves (2). ∎

#### Lemma. Smoothness from flatness and smooth fibres

For $R\to S$ and $\mathfrak q\subset S$ over $\mathfrak p\subset R$, suppose that $S$ is finitely presented over $R$ on a neighbourhood of $\mathfrak q$, that $R_{\mathfrak p}\to S_{\mathfrak q}$ is flat, and that $S\otimes_R\kappa(\mathfrak p)$ is smooth at the fibre point defined by $\mathfrak q$. Then $R\to S$ is smooth at $\mathfrak q$.

**Proof.** A smooth algebra over a field has complete-intersection local rings, by the field Jacobian criterion. The preceding syntomic criterion therefore replaces $S$, near $\mathfrak q$, by a relative global complete-intersection presentation
$$S=R[x_1,\ldots,x_n]/(f_1,\ldots,f_c).$$
For each set $E$ of $c$ variable indices, let $\Delta_E$ be the corresponding Jacobian minor. On passing to the residue field $\kappa(\mathfrak p)$, the same coefficient map sends $\Delta_E$ to the Jacobian minor of the images of the $f_i$: differentiation and determinants commute with coefficient change.

Apply [Smoothness of a global complete intersection](#native-algebra-lemma-relative-global-complete-intersection-smooth) first to the fibre. Its smoothness at the selected point gives an $E$ for which $\Delta_E\notin\mathfrak q$. Apply the same result to the displayed presentation over $R$. It says that this principal neighbourhood is smooth. Thus the original map is smooth at $\mathfrak q$. ∎

#### Lemma. Local criteria for complete intersections

Let $S$ be a finite-type algebra over a field $k$, fix $\mathfrak q\in\operatorname{Spec}S$, and choose any polynomial presentation $S=P/I$ with $P=k[x_1,\ldots,x_n]$. Denote the inverse image of $\mathfrak q$ by $\mathfrak q'$. Put
$$c=\operatorname{ht}(\mathfrak q')-\operatorname{ht}(\mathfrak q)
=n-\dim_{\mathfrak q}\operatorname{Spec}S.$$
Here dimension at a point means the minimum dimension of its open neighbourhoods; the equality is the finite-type field dimension formula. The following are equivalent:

1. There is $g\in S\setminus\mathfrak q$ such that $S_g$ is a global complete intersection over $k$.
2. The ideal $I_{\mathfrak q'}$ in $P_{\mathfrak q'}$ admits a generating list of $c$ elements.
3. The conormal module $(I/I^2)_{\mathfrak q}$ admits a generating list of $c$ elements over $S_{\mathfrak q}$.
4. The module $(I/I^2)_{\mathfrak q}$ is free of rank $c$.
5. The ideal $I_{\mathfrak q'}$ is generated by a regular sequence in $P_{\mathfrak q'}$.

When these conditions hold, any $c$ elements of $I_{\mathfrak q'}$ that generate $I_{\mathfrak q'}/\mathfrak q'I_{\mathfrak q'}$ form a regular sequence.

**Proof.** Write $Q=P_{\mathfrak q'}$ and $H=I_{\mathfrak q'}$. The ring $Q$ is regular local, hence Cohen–Macaulay, and
$$\dim(Q/H)=\dim Q-c.$$
If $c$ elements generate $H/H^2$, Nakayama applied to their quotient in the finite $Q$-module $H$ shows that they generate $H$: the remaining module equals its product with $H\subset\mathfrak q'Q$. Thus (3) implies (2); the converse follows by taking the quotient by $H^2$.

In a Cohen–Macaulay local ring, $c$ generators of an ideal whose quotient has dimension $\dim Q-c$ form a regular sequence, by [The Cohen–Macaulay parameter criterion](#native-algebra-proposition-cm-module). Consequently (2) implies (5). A regular sequence has a free conormal module on its classes, by [Regular sequences are quasi-regular](#native-algebra-lemma-regular-quasi-regular). If its length is $e$, successive regular quotients have dimension $\dim Q-e$, so the displayed equality forces $e=c$. This proves (5) implies (4), which immediately implies (3). The same Nakayama and parameter argument proves the final assertion for every generating list of the specified residue vector space.

To obtain (1) from (2), clear the denominators of the local generators and choose $f_1,\ldots,f_c\in I$ that still generate $H$. Since $I$ is finitely generated, there is $h\in P\setminus\mathfrak q'$ with $I_h=(f_1,\ldots,f_c)_h$. The rings $P/(f_1,\ldots,f_c)$ and $S$ therefore agree near the chosen point, where their dimension at the point is $n-c$. [Localization of a relative complete intersection](#native-algebra-lemma-localize-relative-complete-intersection), case (3), supplies a further principal neighbourhood that is a global complete intersection over $k$. Combining its denominator with $h$ gives (1).

Conversely, suppose (1) and present
$$S_g=k[y_1,\ldots,y_m]/(h_1,\ldots,h_t)$$
as a global complete intersection. Its conormal module $J/J^2$ is free of rank $t$, where $J=(h_1,\ldots,h_t)$, and every component has dimension $m-t$. At the specified point this gives $m-t=\dim_{\mathfrak q}\operatorname{Spec}S$. The [comparison of conormal modules for two presentations](#native-algebra-lemma-conormal-module-localize) gives
$$ (I/I^2)_g\oplus S_g^{\oplus m}
\simeq (J/J^2)\oplus S_g^{\oplus n}.$$
Localizing at $\mathfrak q$ makes $(I/I^2)_{\mathfrak q}$ finite projective over a local ring, hence free, of rank
$$t+n-m=n-\dim_{\mathfrak q}\operatorname{Spec}S=c.$$
Thus (1) implies (4), completing the equivalences. ∎

#### Definition. Unramified ring maps

For a homomorphism $R\to S$:

1. **Unramified** means finite type with $\Omega_{S/R}=0$.
2. **G-unramified** means finite presentation with $\Omega_{S/R}=0$.
3. It is **unramified at $\mathfrak q$**, for a prime $\mathfrak q$ of $S$, if some $g\notin\mathfrak q$ makes $R\to S_g$ unramified.
4. It is **G-unramified at $\mathfrak q$** if some such principal neighbourhood is G-unramified.

The two finiteness requirements are kept distinct over a non-Noetherian base.

#### Lemma. Flatness from Cohen--Macaulayness over a regular base

Let $(R,\mathfrak m_R)\to(S,\mathfrak m_S)$ be a local homomorphism of Noetherian local rings. If $R$ is regular, $S$ is Cohen–Macaulay, and
$$\dim S=\dim R+\dim(S/\mathfrak m_RS),$$
then $S$ is flat over $R$.

**Proof.** Induct on $d=\dim R$. At $d=0$, the regular local ring $R$ is a field, so flatness is automatic. Suppose $d>0$. For every minimal prime $\mathfrak q_i$ of $S$, Cohen–Macaulayness gives $\dim(S/\mathfrak q_i)=\dim S$, by [The Cohen–Macaulay chain theorem](#native-algebra-lemma-maximal-chain-cm). Thus $\mathfrak m_RS$ cannot be contained in $\mathfrak q_i$: otherwise the quotient $S/\mathfrak q_i$ would have dimension at most $\dim(S/\mathfrak m_RS)$, contrary to the displayed equality and $d>0$.

Each contraction $\mathfrak p_i=R\cap\mathfrak q_i$ is therefore a proper subprime of $\mathfrak m_R$. [Prime avoidance with the square of the maximal ideal](#native-algebra-lemma-silly) provides
$$x\in\mathfrak m_R\setminus\left(\mathfrak m_R^2\cup\bigcup_i\mathfrak p_i\right).$$
Since $R$ is regular, $x$ is part of a regular system of parameters. Hence $R/xR$ is regular of dimension $d-1$. The associated primes of the Cohen–Macaulay local ring $S$ are its minimal primes, and $x$ avoids all of them. Thus $x$ is also a nonzerodivisor on $S$, and $S/xS$ is Cohen–Macaulay of dimension $\dim S-1$.

The closed fibre of $R/xR\to S/xS$ is still $S/\mathfrak m_RS$. Subtracting one from both ring dimensions preserves the required dimension equality, so induction makes $S/xS$ flat over $R/xR$. The free resolution $0\to R\xrightarrow{x}R\to R/xR\to0$ shows
$$\operatorname{Tor}_1^R(S,R/xR)=\ker(x:S\to S)=0.$$
Apply [The local flatness criterion for an ideal](#native-algebra-lemma-variant-local-criterion-flatness) with the ideal $(x)$ and the finite $S$-module $S$. Its two hypotheses are exactly this Tor vanishing and the established flatness of $S/xS$ over $R/xR$. It follows that $S$ is flat over $R$. ∎

#### Lemma. Smoothness after an algebraic closure of the ground field

Let $k$ be algebraically closed, $S$ a finite-type $k$-algebra, and $\mathfrak m$ a maximal ideal of $S$. The following are equivalent:

1. $S_{\mathfrak m}$ is regular local.
2. $\dim_{\kappa(\mathfrak m)}(\Omega_{S/k}\otimes_S\kappa(\mathfrak m))\leq\dim S_{\mathfrak m}$.
3. The two dimensions in (2) are equal.
4. Some $g\in S\setminus\mathfrak m$ makes $S_g$ smooth over $k$.

**Proof.** The Nullstellensatz gives $\kappa(\mathfrak m)=k$. The exact cotangent calculation and the closed-point smoothness criterion are proved in *Smooth algebras over a field and the Jacobian criterion*, Proposition 3.1, using the full field criterion of its Theorem 2.1. In the present notation the calculation identifies
$$\Omega_{S/k}\otimes_S k\simeq\mathfrak m/\mathfrak m^2.$$
Its dimension is the embedding dimension of $S_{\mathfrak m}$, which is at least its Krull dimension. Therefore (2) is equivalent to (3), and (3) is precisely regularity, proving equivalence with (1). Proposition 3.1 identifies that regularity with smoothness at this closed point, meaning the principal neighbourhood in (4). Its hypotheses are exactly a finite-type algebra, an algebraically closed field and a closed point; thus all four assertions follow at their stated scope. ∎

#### Lemma. The fibrewise criterion for flatness (Critère de platitude par fibres)

Let $R\to S\to S'$ be local homomorphisms of local rings, and let $\mathfrak m$ be the maximal ideal of $R$. Suppose that both $S$ and $S'$ are essentially finitely presented over $R$, and that $M\ne0$ is a finitely presented $S'$-module. If $M$ is flat over $R$ and $M/\mathfrak mM$ is flat over $S/\mathfrak mS$, then $S$ is flat over $R$ and $M$ is flat over $S$.

**Proof.** We reduce the data, including both flatness conditions, to Noetherian local models. Express $R$ as a filtered colimit of local rings $R_\lambda$ essentially of finite type over $\mathbb Z$, with local transition maps and local maps to $R$. Denote their maximal ideals by $\mathfrak m_\lambda$. One construction takes finite-type subrings of $R$ and localizes at the inverse images of $\mathfrak m$. The [essential finite-presentation model lemma](#native-algebra-lemma-limit-essentially-finite-presentation) permits a common later index at which both ring maps and their composite have compatible finite presentations.

More explicitly, after fixing finite lists of coefficients we obtain local rings
$$
\begin{aligned}
S_\lambda&=\bigl(R_\lambda[x_1,\ldots,x_n]/(f_{1,\lambda},\ldots,f_{u,\lambda})\bigr)_{\mathfrak q_\lambda},\\
S'_\lambda&=\bigl(S_\lambda[y_1,\ldots,y_m]/(\overline g_{1,\lambda},\ldots,\overline g_{v,\lambda})\bigr)_{\mathfrak q'_\lambda},
\end{aligned}
$$
with colimits $S$ and $S'$. The indicated primes are the inverse images of the final maximal ideals. Lift a finite presentation matrix for $M$ at a further index and set $M_\lambda$ to be its cokernel over $S'_\lambda$. Then
$$M_\mu=M_\lambda\otimes_{S'_\lambda}S'_\mu,\qquad
M=M_\lambda\otimes_{S'_\lambda}S'$$
for all sufficiently late indices. Every $M_\lambda$ is nonzero, since a zero one would make its base change $M$ zero.

For $\mu\geq\lambda$, the maps
$$S_\lambda\otimes_{R_\lambda}R_\mu\longrightarrow S_\mu,
\qquad S'_\lambda\otimes_{S_\lambda}S_\mu\longrightarrow S'_\mu$$
are localizations. The same is true of $S'_\lambda\otimes_{R_\lambda}R_\mu\to S'_\mu$. Apply [Eventual flatness in a filtered colimit](#native-algebra-lemma-colimit-eventually-flat) to the models $R_\lambda\to S'_\lambda,M_\lambda$. The flatness of $M$ over $R$ gives flatness of $M_\lambda$ over $R_\lambda$ at all sufficiently late indices.

The maximal ideals have colimit $\mathfrak m$, so quotienting gives
$$S/\mathfrak mS=\varinjlim S_\lambda/\mathfrak m_\lambda S_\lambda,\qquad
M/\mathfrak mM=\varinjlim M_\lambda/\mathfrak m_\lambda M_\lambda,$$
and likewise for $S'$. These quotient models still have the required localization and module base-change properties. Indeed, quotienting the preceding localized tensor products by $\mathfrak m_\mu$ identifies their source with
$$
\bigl(S'_\lambda/\mathfrak m_\lambda S'_\lambda\bigr)
\otimes_{S_\lambda/\mathfrak m_\lambda S_\lambda}
\bigl(S_\mu/\mathfrak m_\mu S_\mu\bigr),
$$
and its map to $S'_\mu/\mathfrak m_\mu S'_\mu$ is a localization. The presentation matrix gives the analogous base-change isomorphism for the quotient modules. Thus these are [essentially finitely presented module models](#native-algebra-lemma-limit-module-essentially-finite-presentation). Applying eventual flatness a second time, now to the assumed flatness of $M/\mathfrak mM$, makes
$$M_\lambda/\mathfrak m_\lambda M_\lambda
\quad\text{flat over}\quad S_\lambda/\mathfrak m_\lambda S_\lambda$$
at all sufficiently late indices.

Choose one index at which both conclusions hold. The rings $R_\lambda,S_\lambda,S'_\lambda$ are Noetherian local, and $M_\lambda$ is finite and nonzero. The [Noetherian fibrewise criterion](#native-algebra-lemma-criterion-flatness-fibre-noetherian) gives flatness of $S_\lambda$ over $R_\lambda$ and of $M_\lambda$ over $S_\lambda$. Finally $S$ is a localization of $S_\lambda\otimes_{R_\lambda}R$, and $M$ is obtained from $M_\lambda\otimes_{S_\lambda}S$ by the corresponding further localization. Flatness survives both base change and localization, yielding the two required conclusions over the original, possibly non-Noetherian rings. ∎

#### Lemma. Characterizations of étale algebras

Let $R\to S$ be finitely presented, and let $\mathfrak q\subset S$ lie over $\mathfrak p\subset R$. Suppose $R_{\mathfrak p}\to S_{\mathfrak q}$ is flat, $\mathfrak pS_{\mathfrak q}$ is the maximal ideal of $S_{\mathfrak q}$, and $\kappa(\mathfrak q)/\kappa(\mathfrak p)$ is finite separable. Then $R\to S$ is étale at $\mathfrak q$.

**Proof.** The fibre local ring is the field $\kappa(\mathfrak q)$. By [An isolated point of a fibre](#native-algebra-lemma-isolated-point-fibre), a principal neighbourhood of $\mathfrak q$ has no other point in that fibre. Replace $S$ by this neighbourhood. Its fibre algebra is local and equals its localization at that one point, hence equals $\kappa(\mathfrak q)$. The finite separable field extension is étale, so this fibre is smooth.

[Smoothness from flatness and smooth fibres](#native-algebra-lemma-flat-fibre-smooth) now gives a smooth principal neighbourhood. Refine it by [the standard smooth neighbourhood theorem](#native-algebra-lemma-smooth-syntomic) to a presentation
$$S_g=R[x_1,\ldots,x_n]/(f_1,\ldots,f_c)$$
with an invertible $c$-column Jacobian minor. Its fibre at the retained point is still the same field. A nonempty fibre of this standard presentation has dimension $n-c$, by [Standard smooth algebras](#native-algebra-lemma-standard-smooth), so $n=c$. The presentation therefore has invertible full square Jacobian and zero differentials. It is smooth and unramified, hence étale, proving the assertion at $\mathfrak q$. ∎

#### Lemma. Étale algebras in standard smooth form

Every étale $R$-algebra $S$ admits a presentation
$$S=R[x_1,\ldots,x_n]/(f_1,\ldots,f_n)$$
whose full Jacobian determinant is invertible in $S$. In particular, the algebra is standard smooth globally.

**Proof.** Choose any finite polynomial presentation $S=P/I$. Étaleness says that its conormal differential
$$I/I^2\longrightarrow\Omega_{P/R}\otimes_P S=S^{\oplus n}$$
is an isomorphism. In particular, the conormal module is free. Apply [A presentation realizing a conormal basis](#native-algebra-lemma-huber) to obtain a presentation whose defining equations are a basis of that module. In this new presentation the conormal differential is still an isomorphism. For $S\ne0$, equality of the ranks of finite free modules gives as many equations as variables, and the matrix of the differential is the full Jacobian. Its determinant is a unit, as asserted. The zero algebra has the presentation $R[t]/(1)$; its Jacobian image is the identity element of the zero ring and hence is a unit there. This also covers that case. ∎

#### Lemma. Recognizing a filtered colimit of finite presentations

Let $R\to\Lambda$ be a homomorphism and let $\mathcal E$ be a set of finitely presented $R$-algebras. Then $\Lambda$ is a filtered colimit of algebras in $\mathcal E$ if and only if every homomorphism $A\to\Lambda$ from a finitely presented $R$-algebra factors as $A\to B\to\Lambda$ with $B\in\mathcal E$.

**Proof.** In the forward direction, a map from a finitely presented algebra into a filtered colimit factors through a stage, by [The finite-presentation criterion](#native-algebra-lemma-characterize-finite-presentation).

Conversely, form the category of pairs $(B,\phi)$ with $B\in\mathcal E$ and $\phi:B\to\Lambda$; arrows are $R$-algebra maps compatible with these structure maps. This category is small. Applying the factorization hypothesis to $R\to\Lambda$ makes it nonempty. Two objects have a common target: their maps give $B_1\otimes_R B_2\to\Lambda$, and this finitely presented algebra factors through an object of the category.

To equalize two parallel arrows $u,v:B_1\to B_2$, choose a finite list of algebra generators $b_i$ of $B_1$. The quotient
$$B_2/(u(b_i)-v(b_i)\mid i)$$
is still finitely presented over $R$, and its map to $\Lambda$ factors through an object of $\mathcal E$. The resulting arrow out of $B_2$ equalizes $u$ and $v$ on the generators, hence on all of $B_1$. The category is therefore filtered.

Its colimit maps to $\Lambda$. This map is surjective: for any $\lambda\in\Lambda$, apply the hypothesis to $R[t]\to\Lambda$, $t\mapsto\lambda$. It is injective as well. If an element $b$ represented at a stage $B$ maps to zero, the finitely presented quotient $B/(b)$ maps to $\Lambda$ and factors through another stage; that transition kills $b$. Filteredness first puts any two representatives at a common stage, so this kernel calculation proves injectivity in general. Thus the colimit is $\Lambda$, with exactly the required kind of stages. ∎

#### Lemma. Standard smooth algebras

Suppose $S=R[x_1,\ldots,x_n]/(f_1,\ldots,f_c)=P/I$ is standard smooth, with its invertible Jacobian minor in the first $c$ variable columns. Then:

1. $R\to S$ is smooth.
2. $\Omega_{S/R}$ is free with basis $dx_{c+1},\ldots,dx_n$.
3. $I/I^2$ is free with basis the classes of $f_1,\ldots,f_c$.
4. Every principal localization $S_g$ is standard smooth over $R$.
5. Every base change $R'\to R'\otimes_R S$ is standard smooth.
6. If $f\in R$ is invertible in $S$, the induced map $R_f\to S$ is standard smooth.
7. $S$ is a relative global complete intersection over $R$.

**Proof.** Parts (1)–(5) are proved, with these exact bases and the polynomial-quotient convention, in *Formally smooth, unramified and étale ring maps*, Theorem 4.1. Its square-zero correction solves the equations by the invertible Jacobian block. Projection onto that block proves independence of the conormal generators, and eliminating those differential coordinates gives the stated basis of $\Omega$. Its localization proof adjoins a variable $z$ with equation $hz-1$, where $h$ lifts $g$, and uses the block determinant $h\Delta$. Its base-change proof applies the coefficient map to the equations and to $\Delta$. Thus the full proof includes both preservation assertions, not just smoothness itself.

For (6), apply (5) with $R'=R_f$. Since $f$ already has an inverse in $S$, the canonical map $R_f\otimes_R S\to S$ is an isomorphism. This gives the asserted standard smooth presentation over $R_f$.

For (7), take a residue field $k$ of $R$. Part (5) gives the same standard smooth presentation for $S\otimes_R k$, and part (2) gives differential rank $n-c$ at every point of a nonempty fibre. The full field criterion in *Smooth algebras over a field and the Jacobian criterion*, Theorem 2.1 identifies that rank with dimension at the point. Hence the fibre has dimension $n-c$. Every nonempty fibre has now been checked, which is exactly the relative global complete-intersection condition for the given presentation. ∎

#### Proposition. Formal smoothness of smooth algebras

For any ring homomorphism $R\to S$, the following are equivalent:

1. The algebra $S$ is finitely presented over $R$ and is formally smooth over $R$.
2. The map $R\to S$ is smooth.

**Proof.** Choose a finite polynomial presentation $S=P/I$. Its conormal sequence is
$$I/I^2\xrightarrow d\Omega_{P/R}\otimes_P S\longrightarrow\Omega_{S/R}\longrightarrow0.$$
The complete equivalence between formal smoothness and this sequence being split exact with an initial zero is *Formally smooth, unramified and étale ring maps*, Theorem 3.1. Its proof constructs the lift from a section of $P/I^2\to S$ and constructs that section from the splitting by subtracting the induced derivation.

If (1) holds, the sequence is split exact. The middle term is finite free, so its quotient $\Omega_{S/R}$ is finite projective, and injectivity on the left says $H_1(\mathrm{NL}_{S/R})=0$. These are the smoothness conditions. Conversely, smoothness makes that conormal map injective and its cokernel finite projective. The sequence therefore splits, so Theorem 3.1 gives formal smoothness. Finite presentation is already included in smoothness. This proves both implications. ∎

#### Lemma. Nakayama's lemma

The lemma is associated with Nakayama, Azumaya and Krull; see the historical attribution accompanying [Stacks, Tag 00DV](https://stacks.math.columbia.edu/tag/00DV).

Fix a commutative ring $R$, an ideal $I$, and an $R$-module $M$. Write $J(R)$ for the Jacobson radical. The following forms will be used:

1. A finite module satisfying $M=IM$ is annihilated by some $f\in1+I$.
2. In (1), the additional containment $I\subseteq J(R)$ forces $M=0$.
3. Suppose $N,N'\subseteq M$, the module $N'$ is finite, and $M=N+IN'$. Some $f\in1+I$ then satisfies $fM\subseteq N$; in particular, $N_f=M_f$.
4. Under the hypotheses of (3), if $I\subseteq J(R)$, then $N=M$.
5. Let $u:N\to M$ be linear, with $M$ finite. Surjectivity of $N/IN\to M/IM$ implies surjectivity of $u_f:N_f\to M_f$ for some $f\in1+I$.
6. Under the hypotheses of (5), $u$ itself is surjective when $I\subseteq J(R)$.
7. If $M$ is finite and the images of $x_1,\ldots,x_n\in M$ span $M/IM$, these elements span $M_f$ over $R_f$ for a suitable $f\in1+I$.
8. With the hypotheses of (7) and $I\subseteq J(R)$, the elements already span $M$ over $R$.
9. For nilpotent $I$, the equality $M=IM$ implies $M=0$, without a finiteness condition on $M$.
10. For nilpotent $I$, any equality $M=N+IN'$ with submodules $N,N'\subseteq M$ implies $M=N$; neither submodule needs to be finite.
11. For nilpotent $I$, a linear map $u:N\to M$ is surjective whenever its reduction $N/IN\to M/IM$ is surjective.
12. For nilpotent $I$, an arbitrary family $(x_\alpha)_{\alpha\in A}$ spanning $M/IM$ spans $M$ itself.

**Proof.** The determinant argument for a finite module is proved in *Localization, local properties and support*, Lemma 4.1 and Theorem 4.2. Apply that lemma to the identity endomorphism of $M$, whose image lies in $IM$. Evaluation of its monic annihilating polynomial at $1$ gives an annihilator in $1+I$, proving (1). When $I\subseteq J(R)$, such an element is a unit: it belongs to no maximal ideal. This proves (2).

Here are the quotient arguments that give the remaining forms. Under (3), put $Q=M/N$. The map $N'\to Q$ is surjective, since $M=N+IN'\subseteq N+N'$, so $Q$ is finite. Also $Q=IQ$. Part (1) supplies $fQ=0$, which is exactly $fM\subseteq N$. Localizing makes $Q_f=0$, hence $M_f=N_f$. Part (2) instead gives $Q=0$ under (4).

For (5) and (6), use $Q=\operatorname{coker}(u)$. It is finite as a quotient of $M$, and the surjectivity modulo $I$ says $Q/IQ=0$. Thus (1) and (2) give the respective conclusions. Apply these conclusions to the map $R^n\to M$ taking its standard basis to the $x_i$ to obtain (7) and (8).

If $I^a=0$ and $Q=IQ$, iteration gives $Q=I^aQ=0$ for every module $Q$. This proves (9). Apply it to $M/N$, to $\operatorname{coker}(u)$, and to the cokernel of $R^{(A)}\to M$, respectively. Their reductions modulo $I$ vanish under (10), (11), and (12). The direct sum $R^{(A)}$ permits any indexing set, so no finite-generation assumption has entered these last four assertions. ∎

#### Lemma. Finite presentation and finite algebras

If $S$ is a finitely presented $R$-algebra, the kernel of every surjection $\alpha:R[x_1,\ldots,x_n]\to S$ is finitely generated as an ideal.

**Proof.** Take one finite presentation $S=R[y_1,\ldots,y_m]/(f_1,\ldots,f_s)$. Choose polynomials $g_i(y)$ representing $\alpha(x_i)$, and choose polynomials $h_j(x)$ whose images under $\alpha$ are the classes of $y_j$. In $R[x]$, form the finite ideal
$$L=\bigl(f_\ell(h(x)),\ x_i-g_i(h(x))\ :\ 1\leq\ell\leq s,\ 1\leq i\leq n\bigr).$$
Each displayed generator maps to zero in $S$, so $\alpha$ descends to $\bar\alpha:R[x]/L\to S$. In the other direction, the substitution $y_j\mapsto h_j(x)\bmod L$ kills every $f_\ell$ and defines $\beta:S\to R[x]/L$.

On the generators $y_j$ of $S$, the composite $\bar\alpha\beta$ is the identity by the choice of $h_j$. On the generators $x_i$ of $R[x]/L$, the composite $\beta\bar\alpha$ takes $x_i$ to $g_i(h(x))=x_i\bmod L$. Thus these maps are inverse $R$-algebra isomorphisms. It follows that $\ker\alpha=L$, giving the required finite generators over an arbitrary base ring. ∎

#### Lemma. The equational criterion for flatness (Equational criterion of flatness)

For any ring $R$ and any $R$-module $M$, flatness is equivalent to the following condition. Whenever a finite list satisfies $\sum_{i=1}^n a_i x_i=0$ in $M$, there are a finite list $y_1,\ldots,y_s\in M$ and a matrix $(b_{ij})$ over $R$ such that
$$x_i=\sum_{j=1}^s b_{ij}y_j\quad(1\leq i\leq n),\qquad
\sum_{i=1}^n a_i b_{ij}=0\quad(1\leq j\leq s).$$
A relation admitting this factorization is called *trivial*.

**Proof.** This is the full generality of *Tor and flat modules*, Theorem 5.1. Its forward argument lifts the relation through $\ker(R^n\to(a_1,\ldots,a_n))\otimes_R M$, producing exactly the matrix above. In the reverse direction that factorization kills every kernel tensor for $I\otimes_R M\to M$. Theorem 2.1 in the same lesson, Section 2, supplies the complete ideal criterion: it passes from finitely generated ideals to all ideals, then to submodules of finite free modules, arbitrary free modules, and finally arbitrary inclusions. These proofs impose no finite-presentation condition on the ideal or module and no Noetherian condition on $R$. ∎

#### Lemma. Krull's intersection theorem

If $(R,\mathfrak m)$ is Noetherian local, $M$ is a finite $R$-module, and $I\subsetneq R$ is an ideal, then
$$\bigcap_{n\geq0}I^nM=0.$$

**Proof.** The more general *Noetherian and Artinian rings*, Theorem 6.1, proves that this intersection $K$ satisfies $IK=K$ and is annihilated by one element of $1+I$. Its preceding Section 5 proves the Artin–Rees identity used to obtain $IK=K$; thus the theorem includes the proof of the intersection assertion. Here $I\subseteq\mathfrak m=J(R)$, so its annihilator is a unit. Consequently $K=0$. ∎

#### Lemma. Composition of smooth ring maps

Given smooth maps $R\to S$ and $S\to T$, the composite $R\to T$ is smooth.

**Proof by the cotangent sequence.** First, $T$ is finitely presented over $R$: combine a finite presentation of $S$ over $R$ with a finite presentation of $T$ over $S$, lifting the coefficients of the latter equations to the former polynomial ring. The module $\Omega_{S/R}$ is projective, so its first and second Tor groups with $T$ vanish. The [transitivity sequence](#native-algebra-lemma-exact-sequence-nl), including its comparison of the first homology after tensoring, therefore gives
$$H_1(\mathrm{NL}_{S/R})\otimes_S T\longrightarrow
H_1(\mathrm{NL}_{T/R})\longrightarrow H_1(\mathrm{NL}_{T/S})\longrightarrow
\Omega_{S/R}\otimes_S T\longrightarrow\Omega_{T/R}\longrightarrow\Omega_{T/S}\longrightarrow0.$$
Smoothness of the two given maps makes both outside $H_1$ terms zero. Hence $H_1(\mathrm{NL}_{T/R})=0$, and the differential terms form a short exact sequence with initial term $\Omega_{S/R}\otimes_S T$. That term is finite projective by scalar extension, and the last term $\Omega_{T/S}$ is finite projective. Projectivity of the last term splits the sequence, so the middle term is finite projective as well. These are precisely the smoothness conditions for $R\to T$.

**Proof using standard presentations.** This also makes the local geometric mechanism explicit. Let $\mathfrak q\in\operatorname{Spec}(T)$ and $\mathfrak p$ its inverse image in $S$. The [standard-neighborhood theorem for a smooth algebra](#native-algebra-lemma-smooth-syntomic) gives a principal neighborhood $S_f$ of $\mathfrak p$ standard smooth over $R$. The map $S_f\to T_f$ is smooth by localization, and a further principal neighborhood $(T_f)_g$ of $\mathfrak q$ is standard smooth over $S_f$. The [composition calculation for standard smooth presentations](#native-algebra-lemma-compose-standard-smooth) makes $(T_f)_g$ standard smooth over $R$: its Jacobian has the two invertible diagonal blocks. If $g=t/f^a$, this is a principal neighborhood $T_{ft}$ of $\mathfrak q$. Such neighborhoods cover $\operatorname{Spec}(T)$, so [locality of smoothness](#native-algebra-lemma-locally-smooth) proves the assertion. This route uses the previously proved standard-neighborhood and locality statements, with their finite-presentation hypotheses retained. ∎

#### Lemma. Total rings of fractions without embedded primes

Suppose that a ring $R$ has a finite set of minimal primes $\{\mathfrak q_1,\ldots,\mathfrak q_t\}$ and that its zero divisors are exactly $\bigcup_i\mathfrak q_i$. Then the localization maps induce an isomorphism
$$Q(R)\xrightarrow{\ \sim\ }\prod_{i=1}^t R_{\mathfrak q_i}.$$
No Noetherian assumption is required.

**Proof.** Write $U$ for the multiplicative set of nonzerodivisors. Every $u\in U$ lies outside each $\mathfrak q_i$, giving the indicated maps from $U^{-1}R=Q(R)$. By [the prime correspondence for localization](#native-algebra-lemma-spec-localization), a prime of $Q(R)$ comes from a prime $\mathfrak p$ of $R$ disjoint from $U$. Such a $\mathfrak p$ is contained in $\bigcup_i\mathfrak q_i$, and [finite prime avoidance](#native-algebra-lemma-silly) puts it inside one $\mathfrak q_i$. Minimality then gives $\mathfrak p=\mathfrak q_i$. Conversely, each $\mathfrak q_i$ is disjoint from $U$.

Thus all primes of $Q(R)$ are the finitely many points corresponding to the $\mathfrak q_i$, and each is maximal. Each singleton is closed; its finite complement is also closed, so the spectrum is discrete. The [idempotent decomposition for a disjoint spectrum](#native-algebra-lemma-disjoint-implies-product) expresses $Q(R)$ as a product with one local factor at each of these points. Localizing that product at its $i$th prime keeps exactly its $i$th factor. Transitivity of localization identifies it with $R_{\mathfrak q_i}$. These identifications intertwine the factor projections with the original localization maps, proving the stated canonical isomorphism. If $R=0$, the spectrum is empty and the assertion is the empty product, namely the zero ring. ∎

#### Lemma. Irreducible components of a Noetherian spectrum

A Noetherian ring has only finitely many minimal prime ideals. Equivalently, its spectrum has finitely many irreducible components and therefore finitely many component generic points.

**Proof.** For $X=\operatorname{Spec}(R)$, a descending sequence of closed sets gives an ascending sequence of their radical ideals. The Noetherian condition makes that sequence stabilize. Thus $X$ satisfies the descending chain condition on closed sets.

Every closed subset of such a space is a finite union of irreducible closed subsets. Indeed, otherwise choose a minimal closed counterexample $Z$ by the descending chain condition. It is nonempty and cannot itself be irreducible. Write $Z=Z_1\cup Z_2$ with both $Z_i$ proper closed subsets of $Z$. Minimality gives finite irreducible decompositions of both $Z_i$, which together give one of $Z$, a contradiction. Apply this to $X$ and discard members contained in others. The remaining sets are exactly its irreducible components: any irreducible subset of a finite union of closed sets lies in one member.

For the [affine irreducibility criterion](#native-algebra-lemma-irreducible), an irreducible closed set is $V(\mathfrak p)$ for a prime $\mathfrak p$, with generic point $\mathfrak p$. A component corresponds to a prime minimal under inclusion. Hence the finite component decomposition gives the asserted finite set of minimal primes. The zero ring gives the empty decomposition. ∎

#### Lemma. Regular rings are Cohen--Macaulay

Let $(R,\mathfrak m)$ be regular local of dimension $d$, and choose any minimal generating list $x_1,\ldots,x_d$ for $\mathfrak m$. This list is $R$-regular. For each $0\leq c\leq d$, the local ring $R/(x_1,\ldots,x_c)$ is regular of dimension $d-c$. In particular, $R$ is Cohen–Macaulay.

**Proof.** Use the complete proof of *Regular sequences, depth and Cohen–Macaulay modules*, Theorem 6.1 and Corollary 6.2. The theorem begins with any minimal generating list. It proves that $\operatorname{gr}_{\mathfrak m}R$ is the polynomial ring on the initial forms of that list, then uses Krull separation to obtain injectivity successively in the quotients. It therefore proves regularity of the given list, not merely the existence of some regular list, and proves that $R$ is Cohen–Macaulay.

For completeness, the quotient conclusion follows within that same proof route as follows. Corollary 6.2 gives dimension $d-c$ after a prefix of length $c$. The remaining $d-c$ elements generate its maximal ideal, so its embedding dimension is at most $d-c$. Embedding dimension is at least Krull dimension for a Noetherian local ring. Equality follows, which is exactly regularity. At $c=d$ the quotient is the residue field, and $d=0$ is already the field case of Theorem 6.1. ∎

#### Lemma. Powers of a regular sequence

For an arbitrary ring $R$, an arbitrary $R$-module $M$, and positive integers $e_1,\ldots,e_r$, one has
$$f_1,\ldots,f_r\text{ is }M\text{-regular}
\quad\Longleftrightarrow\quad
f_1^{e_1},\ldots,f_r^{e_r}\text{ is }M\text{-regular}.$$
Regularity includes nonvanishing of the final quotient.

**Proof.** This is *Regular sequences, depth and Cohen–Macaulay modules*, Proposition 1.3, with exactly the arbitrary-ring and arbitrary-module hypotheses above. Its proof treats both directions by the finite filtration of $M/f_1^{e_1}M$ whose factors are $M/f_1M$. After each later equation, it proves exactness of the quotient filtration; in the reverse direction the embedded first factor detects the next injectivity condition. The final filtration also proves equivalence of nonvanishing of the last quotient. Induction then changes the other exponents. The proof includes the empty list and does not use permutation of a regular sequence, which would require additional hypotheses. ∎

#### Lemma. Elementary formally smooth extensions

For a field extension $K/k$, each of the following hypotheses implies formal smoothness of $k\to K$:

1. $K$ is purely transcendental over $k$, with any cardinality of transcendence basis.
2. $K/k$ is separable algebraic, without a finite-degree assumption.
3. $K/k$ is separable, in the sense that every finitely generated intermediate extension is separably generated.

**Proof.** For (1), write $K=k(t_j\mid j\in J)$. Polynomial algebras on an arbitrary set of variables are formally smooth, and localization preserves formal smoothness, by the complete proof of *Formally smooth, unramified and étale ring maps*, Theorem 1.2. Its localization step applies here because every nonzero polynomial has a unit image under any test map from the field; units lift across a square-zero ideal. Thus it treats arbitrary $J$ and every required denominator.

For (2), every finite intermediate field $E/k$ is formally étale by the same lesson, Proposition 6.3, whose proof lifts a separable generating tower by unique root corrections. The fields $E$ form a directed system with union $K$. Given a square-zero lifting problem for $K$, lift its restriction to each $E$. Uniqueness makes these lifts agree under every inclusion, so they define a lift on the union. Restriction to each $E$ also proves uniqueness. Hence $K/k$ is in fact formally étale.

For (3), let $E$ range over all intermediate fields finitely generated over $k$. Separability supplies a transcendence basis $\mathbf t$ of $E/k$ with $E/k(\mathbf t)$ separable algebraic. Parts (1) and (2), followed by the composition assertion of Theorem 1.2, give formal smoothness of each $E/k$.

To pass to their union, use [the cotangent criterion for a field extension](#native-algebra-lemma-characterize-formally-smooth-field-extension): it gives $H_1(L_{E/k})=0$. The [filtered-colimit comparison](#native-algebra-lemma-colimits-nl) for naive cotangent complexes then gives $H_1(L_{K/k})=0$. More explicitly, tensor each presentation complex with the field $K$; this is exact on $E$-modules, and the resulting filtered colimit is the presentation complex for $K/k$. Exactness of filtered colimits therefore gives the stated homology vanishing. Apply the field criterion again to conclude formal smoothness. This argument does not require arbitrary choices of smooth lifts at different stages to be compatible. ∎

#### Lemma. Descent of flatness

Let $R$ be a ring, let $S\to S'$ be a flat homomorphism of $R$-algebras, and let $M$ be an $S$-module. Set $M'=M\otimes_S S'$.

1. If $M$ is flat as an $R$-module, then so is $M'$.
2. If $S\to S'$ is faithfully flat, then $M$ is flat over $R$ exactly when $M'$ is flat over $R$.

**Proof.** For any inclusion $U\hookrightarrow V$ of $R$-modules, let
$$K=\ker(U\otimes_R M\longrightarrow V\otimes_R M).$$
This is an $S$-module. Exactness of $-\otimes_S S'$ and the associative tensor identifications give
$$K\otimes_S S'\cong\ker(U\otimes_R M'\longrightarrow V\otimes_R M').$$
If $M$ is $R$-flat, then $K=0$ for every inclusion, so the right-hand kernels vanish; this proves (1). Conversely, if $M'$ is $R$-flat, the right-hand kernel always vanishes. Under faithful flatness this implies $K=0$. Tensoring with $M$ therefore preserves every inclusion of $R$-modules, which proves (2). No finiteness hypothesis on any of these rings or modules is used. ∎

#### Lemma. Henselianity in local dimension zero

Every local ring $(R,\mathfrak m)$ of dimension zero is henselian, including rings that are not Noetherian.

**Proof by root correction.** The only prime of $R$ is $\mathfrak m$, so $\mathfrak m$ is its nilradical. Take a monic polynomial $f\in R[T]$ with a simple root $\bar a\in R/\mathfrak m$, and choose a lift $a_0\in R$. The element $e=f(a_0)$ is nilpotent, while $f'(a_0)$ is a unit. Define
$$a_{n+1}=a_n-f'(a_n)^{-1}f(a_n).$$
All $a_n$ have residue $\bar a$, so all displayed inverses exist. Polynomial expansion shows
$$f(a_{n+1})\in f(a_n)^2R\subseteq e^{2^{n+1}}R.$$
For sufficiently large $n$ this error is zero. The resulting $a_n$ is a root lifting $\bar a$, as required. Only the single element $e$ has been assumed nilpotent; a common nilpotence exponent for $\mathfrak m$ is unnecessary.

**Proof by finite algebras.** If $S$ is finite over $R$, each of its primes contracts to $\mathfrak m$. The fibre $S/\mathfrak mS$ is finite-dimensional over $R/\mathfrak m$, so there are finitely many such primes. Incomparability for an integral extension makes them all maximal. Its finite spectrum is therefore discrete, and the [idempotent decomposition](#native-algebra-lemma-disjoint-implies-product) writes $S$ as a finite product of local rings. The complete finite-algebra criterion in *Henselian local rings and henselization*, Theorem 2.2, now also gives henselianity of $R$. ∎

#### Lemma. Finite étale algebras over a henselian ring

For a henselian local ring $(R,\mathfrak m,\kappa)$, the functor
$$S\longmapsto S/\mathfrak mS$$
from finite étale $R$-algebras to finite étale $\kappa$-algebras is an equivalence of categories. Its action on morphisms is reduction modulo $\mathfrak m$.

**Proof.** Apply *Étale neighbourhoods, henselization and quasi-finite morphisms*, Theorem 5.2. Its complete proof has exactly this arbitrary-local-ring scope. For essential surjectivity it lifts a separable monic polynomial for each residue-field factor and proves that its derivative is a unit throughout the finite lift. For full faithfulness it decomposes the target into henselian local factors, then lifts each specified residue map by the unique section through the corresponding rational fibre point. Combining those lifts recovers every morphism and proves its uniqueness. The theorem even proves this morphism assertion when the target is any finite $R$-algebra.

The algebraic inputs to that argument are the complete finite-algebra criterion and permanence for finite local algebras. Thus the local factors used in the proof are finite over $R$ and henselian; in the finite étale case they remain étale over $R$. The equivalence retains residue-field automorphisms, rather than identifying all lifts by an unspecified unique isomorphism. ∎

#### Lemma. Dimension of a flat family

Suppose $R\to S$ is a homomorphism of Noetherian rings with going down. Let $\mathfrak q\subset S$ contract to $\mathfrak p\subset R$. Then
$$\dim S_{\mathfrak q}=\dim R_{\mathfrak p}+\dim(S_{\mathfrak q}/\mathfrak pS_{\mathfrak q}).$$
In particular this holds for a flat map, by [going down for flat ring maps](#native-algebra-lemma-flat-going-down).

**Proof.** Put $A=R_{\mathfrak p}$, $B=S_{\mathfrak q}$, with maximal ideals $\mathfrak m,\mathfrak n$, and let $d=\dim A$, $e=\dim(B/\mathfrak mB)$. These dimensions are finite. Choose $d$ parameters in $A$ and lift a system of $e$ parameters of $B/\mathfrak mB$ to $B$. The ideal they together generate in $B$ has radical $\mathfrak n$. Indeed, a power of $\mathfrak m$ is contained in the ideal of the first parameters, and the second parameters cut the fibre down to its closed point. The height bound for an ideal generated by $d+e$ elements therefore gives $\dim B\leq d+e$. This is the parameter proof of [the base–fibre dimension bound](#native-algebra-lemma-dimension-base-fibre-total).

For the reverse inequality, take a chain of length $e$ in $\operatorname{Spec}(B/\mathfrak mB)$ ending at its maximal ideal. Its inverse images are
$$\mathfrak q_0\subsetneq\mathfrak q_1\subsetneq\cdots\subsetneq\mathfrak q_e=\mathfrak n,$$
all contracting to $\mathfrak m$ in $A$. Choose a chain of length $d$ in $A$ ending at $\mathfrak m$. Going down, which persists under these localizations, successively extends the chain below $\mathfrak q_0$ by one prime over each earlier member of the chosen base chain. Those $d$ new inclusions are strict because their contractions are distinct. The resulting chain in $B$ has length $d+e$. Hence $\dim B\geq d+e$, proving equality, including $d=0$ or $e=0$. ∎

#### Lemma. Universal injectivity of a faithfully flat ring map

For a faithfully flat homomorphism $R\to S$, the map $R\to S$ remains injective after tensoring with any $R$-module. In particular it identifies $R$ with a subring of $S$, and for every ideal $I\subset R$ one has $R\cap IS=I$.

**Proof.** These are precisely the conclusions of *Faithful flatness and the local criterion for flatness*, Theorem 2.2. Its proof tensors $N\to N\otimes_R S$ once more with $S$, exhibits multiplication on the two $S$-factors as a retraction, and reflects injectivity by faithful flatness. Taking $N=R/I$ gives the asserted contraction, for every ideal without a finite-generation condition. ∎

#### Lemma. Characterizations of henselian local rings

Let $(R,\mathfrak m,\kappa)$ be a local ring. Bars denote reduction to $\kappa$. The following thirteen conditions are equivalent:

1. $R$ is henselian: every simple residue root of a monic polynomial over $R$ lifts to a root in $R$.
2. For every $f\in R[T]$, with no monicity requirement, each $a_0\in\kappa$ satisfying $\bar f(a_0)=0$ and $\overline{f'}(a_0)\ne0$ lifts to a root of $f$.
3. For monic $f\in R[T]$, every factorization $\bar f=g_0h_0$ with $g_0,h_0\in\kappa[T]$ coprime lifts to $f=gh$ with $\bar g=g_0$, $\bar h=h_0$.
4. The factors in (3) can always be chosen with $\deg g=\deg g_0$.
5. The factorization assertion of (3) holds for every $f\in R[T]$, not necessarily monic.
6. The factors in (5) can always be chosen with $\deg g=\deg g_0$ whenever $g_0\ne0$.
7. Whenever an étale $R$-algebra $S$ has a prime $\mathfrak q$ above $\mathfrak m$ with canonical residue extension $\kappa\to\kappa(\mathfrak q)$ an isomorphism, $R\to S$ has an $R$-algebra retraction $S\to R$.
8. For each $(S,\mathfrak q)$ in (7), there is exactly one such retraction $\tau$ with $\tau^{-1}(\mathfrak m)=\mathfrak q$.
9. Every finite $R$-algebra is a product of local rings.
10. Every finite $R$-algebra is a finite product of local rings.
11. Each finite type $R$-algebra $S$ has a decomposition $S=A\times B$, with $A$ finite over $R$, such that $R\to B$ is not quasi-finite at any point above $\mathfrak m$.
12. Each finite type $R$-algebra $S$ has a decomposition $S=A\times B$, with $A$ finite over $R$, such that every irreducible component of $\operatorname{Spec}(B\otimes_R\kappa)$ has dimension at least one.
13. Each quasi-finite $R$-algebra $S$ has a decomposition $S=A\times B$, with $A$ finite over $R$ and $B\otimes_R\kappa=0$.

Empty products are allowed for the zero algebra. No Noetherian condition is imposed on $R$.

**Proof.** We first connect the root, section and finite-algebra conditions, then treat arbitrary polynomial factorizations.

The equivalence of (1) and (8), including uniqueness through the specified point, is the complete section criterion in *Henselian local rings and henselization*, Theorem 1.2. Its proof uses a standard étale neighborhood to turn the section problem into the specified simple-root problem. Lemma 1.1 there proves uniqueness by applying Nakayama to the finite ideal of differences of two evaluations. The equivalence of (1) and (10) is the complete Theorem 2.2 of that lesson: coprime factorization lifts idempotents in every finite algebra, and a lifted rank-one factor recovers a simple root.

Certainly (8) implies (7). Conversely, suppose (7) and fix its point $\mathfrak q$. The closed fibre of $S$ is a finite product of finite separable fields. Choose an element of $S$ whose image is one in the factor belonging to $\mathfrak q$ and zero in all other factors. Inverting it gives an étale algebra with exactly one point above $\mathfrak m$, still with residue field $\kappa$. Apply (7) to that algebra. Any resulting retraction has inverse image of $\mathfrak m$ equal to its sole closed-fibre point. Restrict to $S$ to get the required retraction through $\mathfrak q$. Uniqueness is Lemma 1.1 just cited. Thus (7) implies (8).

Conditions (9) and (10) are equivalent. A finite algebra over a local ring has only finitely many maximal ideals: all contract to $\mathfrak m$ by integrality and correspond to maximal ideals in its finite-dimensional residue algebra. A product of nonzero local rings has at least as many distinct maximal ideals as factors, using the coordinate projections. Therefore any product decomposition as in (9) already has finitely many factors. The reverse implication is immediate.

Under (8), let $f$ and $a_0$ be as in (2). The algebra $R[T]_{f'}/(f)$ is étale, by its invertible one-by-one Jacobian; evaluation at $a_0$ defines a closed-fibre point of residue field $\kappa$. The retraction supplied by (8) sends $T$ to the desired root. Hence (8) implies (2), and (2) plainly implies (1).

We next connect the finite-type conditions. The full finite-branch decomposition, *Étale neighbourhoods, henselization and quasi-finite morphisms*, Lemma 4.1, proves (1) implies (11). Its argument isolates each quasi-finite point by algebraic Zariski's Main Theorem, chooses a finite algebra of integral numerators, and uses its henselian local factors to obtain the actual idempotent decomposition of $S$. It applies to finite type algebras without assuming finite presentation. A finite type scheme over a field has a zero-dimensional irreducible component exactly at an isolated point, and its quasi-finite points are exactly those isolated points. Thus the conditions on $B$ in (11) and (12) agree. When $S$ is quasi-finite everywhere, (11) forces its residual closed fibre to be empty, giving (13).

The étale-neighborhood route to (11) and (10) is also useful. Under (8), apply [Making a quasi-finite algebra finite étale locally](#native-algebra-lemma-etale-makes-quasi-finite-finite) to $S$ and $\mathfrak m$. It gives an étale $R\to R'$ with a point $\mathfrak m'$ of residue field $\kappa$ and
$$S\otimes_R R'=A'_1\times\cdots\times A'_n\times B',$$
where each $A'_i$ is finite with one point over $\mathfrak m'$, while $B'$ has no quasi-finite point there. The retraction $\tau:R'\to R$ through $\mathfrak m'$ gives
$$S\cong(S\otimes_R R')\otimes_{R',\tau}R
\cong\prod_i(A'_i\otimes_{R',\tau}R)\times(B'\otimes_{R',\tau}R).$$
The residue map of $\tau$ is the prescribed identity on $\kappa$. Consequently the closed fibres of these factors identify with their old fibres at $\mathfrak m'$. Finiteness is preserved by this base change, so their product is the required $A$ and the last factor is the required $B$. If $S$ was finite, the last factor is finite with empty closed fibre and hence zero by Nakayama. Each remaining finite factor has one maximal ideal, giving (10) by this second route as well.

To prove (13) implies (1), start with monic $f$ and a simple root $a_0$ of $\bar f$. Choose a polynomial $u\in R[T]$ reducing to $\bar f/(T-a_0)$, and put
$$S=(R[T]/(f))_u.$$
This algebra is quasi-finite, being a principal localization of a finite algebra, and its closed fibre is $\kappa$: the polynomial $u$ removes all factors except the simple root $a_0$. It is flat over $R$, since $R[T]/(f)$ is finite free and localization is flat. Under (13), write $S=A\times B$ with $A$ finite and $B/\mathfrak mB=0$. Then $A/\mathfrak mA=\kappa$. The factor $A$ is flat over $R$, hence finite free by [the finite-flat local theorem](#native-algebra-lemma-finite-flat-local), and its rank is one. Its unit is a basis: it spans the reduction, so Nakayama makes it a generator, and a generator of a rank-one free module is a basis. The map $R\to A$ is therefore an algebra isomorphism. The image of $T$ in $A=R$ is the requested root. This completes the equivalence of (1), (2), (7)–(13).

It remains to include the four factorization conditions. There are immediate implications
$$ (6)\Longrightarrow(5)\Longrightarrow(3),\qquad
(6)\Longrightarrow(4)\Longrightarrow(3).$$
We will prove (3) implies (1) and (1) implies (6).

Assume (3), and write $\bar f=(T-a_0)h_0$ for a monic simple-root problem. Lift this factorization to $f=gh$, without imposing degree or monicity on the lifted factors. In the finite free algebra $D=R[T]/(f)$, the images of $g$ and $h$ generate the unit ideal: the quotient by both is finite and has zero reduction, so Nakayama applies. Since their product is zero, their generated ideals have zero intersection. Chinese remainders give
$$D=D/(g)\times D/(h).$$
The first factor is finite projective over $R$, hence free because $R$ is local. Its reduction is $\kappa[T]/(T-a_0)=\kappa$, so it has rank one. The unit-basis argument of the preceding paragraph identifies it with $R$ and gives a root of $f$ lifting $a_0$. Thus (3) implies (1).

Finally assume (1) and take $\bar f=g_0h_0$ with coprime factors, allowing $f$ to be nonmonic. If either residue factor vanishes, coprimality makes the other a nonzero scalar. Choose a unit of $R$ representing that scalar and use it as the corresponding factor of $f$; division of $f$ by this unit supplies the remaining factor. Their residues are the prescribed pair. In the case $g_0\ne0$ this construction makes $g$ a unit constant, so its degree is the required zero. This proves (6) for all vanishing-factor cases.

Now both residue factors are nonzero. If the leading coefficient of $g_0$ is $\lambda\in\kappa^\times$, choose a unit $v\in R$ lifting $\lambda$ and replace the prescribed pair by $(\lambda^{-1}g_0,\lambda h_0)$. Once this normalized pair is lifted, multiplication of its first lift by $v$ and its second by $v^{-1}$ restores the original residues and degrees. We may thus construct the lift with $g_0$ monic.

Some coefficient of $f$ is a unit of $R$, because $\bar f\ne0$. Hence the image of $f$ in $\kappa(\mathfrak p)[T]$ is nonzero for every $\mathfrak p\subset R$. It follows that $S=R[T]/(f)$ has finite fibres and is quasi-finite. It is also flat over $R$: at each prime of $R[T]$ containing $f$, apply [the fibrewise nonzerodivisor criterion](#native-algebra-lemma-grothendieck-general) to the essentially finitely presented flat local map from the corresponding localization of $R$. Its fibre is a localization of a polynomial ring over a field, where this nonzero polynomial is a nonzerodivisor. The criterion gives flatness of the quotient at every prime, and locality of flatness gives the assertion for $S$.

By (13) and (10), decompose $S$ into finite local factors and a factor with empty closed fibre. The coprime factorization gives
$$S/\mathfrak mS\cong\kappa[T]/(g_0)\times\kappa[T]/(h_0).$$
The finite local factors of $S$ reduce to exactly the local factors of this Artinian algebra. Let $A$ be the product of those belonging to $\kappa[T]/(g_0)$. It is finite flat over $R$, hence free, of rank $r=\deg g_0$. Let $g$ be the characteristic polynomial of multiplication by the image of $T$ on $A$. It is monic of degree $r$ and reduces to $g_0$, since multiplication by $T$ on $\kappa[T]/(g_0)$ has characteristic polynomial $g_0$.

Cayley–Hamilton gives a surjection $R[T]/(g)\to A$. Both modules are free of rank $r$, and reduction makes this map an isomorphism. Its matrix has unit determinant, so it is an isomorphism over $R$; the rank-zero case is the isomorphism of zero modules. Since $f$ vanishes in $A$, we obtain $f=gh$ in $R[T]$. Reducing and cancelling the nonzero polynomial $g_0$ in $\kappa[T]$ gives $\bar h=h_0$. The normalization step then restores any original leading coefficient. This proves (6) and finishes all thirteen equivalences. ∎

#### Lemma. Extending a henselian lifting problem to a finite algebra

Let $R\to S$ be a local homomorphism of local rings, and write $S\to S^h$ for the henselization. Suppose $R\to A$ is étale and $\mathfrak q\subset A$ lies above $\mathfrak m_R$ with canonical isomorphism $R/\mathfrak m_R\cong\kappa(\mathfrak q)$. There is exactly one $R$-algebra map $f:A\to S^h$ with
$$f^{-1}(\mathfrak m_{S^h})=\mathfrak q.$$
In particular $R\to A\xrightarrow f S^h$ agrees with $R\to S\to S^h$.

**Proof.** The residue field of $S^h$ is canonically that of $S$. Locality of $R\to S$ and the given residue isomorphism specify the evaluation
$$A\longrightarrow\kappa(\mathfrak q)\cong R/\mathfrak m_R
\longrightarrow S/\mathfrak m_S=\kappa(S^h).$$
Apply the general evaluation assertion in *Henselian local rings and henselization*, Theorem 1.2, to the henselian target $S^h$. It gives the unique $R$-algebra lift of this evaluation. Its residue kernel is $\mathfrak q$, proving the asserted inverse-image condition. Conversely, every $R$-algebra map with that inverse image induces this same evaluation, because $\kappa(\mathfrak q)=\kappa(R)$ and its action on $R$ is fixed. The theorem's uniqueness therefore proves uniqueness in the exact scope stated here. ∎

#### Lemma. Étale morphisms

The following properties hold for étale ring maps.

1. Every principal localization $R\to R_f$ is étale, including $f=0$.
2. The composite of two étale maps is étale.
3. Any base change of an étale map is étale.
4. Suppose $g_1,\ldots,g_m\in S$ generate the unit ideal. If every $R\to S_{g_i}$ is étale, then $R\to S$ is étale.
5. If $R\to S$ is finitely presented and $R\to R'$ is flat, put $S'=R'\otimes_R S$. The étale locus of $S'/R'$ is exactly the inverse image of the étale locus of $S/R$.
6. Every étale map is syntomic and hence flat.
7. For a finite type algebra $S$ over a field $k$, étaleness is equivalent to $\Omega_{S/k}=0$.
8. Every étale $R$-algebra $S$ is obtained by base change from an étale $R_0$-algebra $S_0$, where $R_0\subseteq R$ is a finite type $\mathbf Z$-algebra.
9. If $A=\operatorname{colim}_i A_i$ is a filtered colimit of rings and $B$ is étale over $A$, some stage has an étale algebra $B_i/A_i$ with $A\otimes_{A_i}B_i\cong B$.
10. If $U\subset A$ is multiplicative and $B'$ is étale over $U^{-1}A$, there is an étale $A$-algebra $B$ such that $U^{-1}B\cong B'$.
11. For $B=B'\times B''$ as $A$-algebras, $B/A$ is étale if and only if both factors are étale over $A$.

**Proof of (1)–(4) and (6).** An étale algebra is a smooth algebra with zero differentials. The presentation $R_f=R[z]/(fz-1)$ is smooth and has zero differential module, since $f$ is invertible there. It also covers $f=0$, when the quotient is the zero ring.

Smoothness is preserved by [composition](#native-algebra-lemma-compose-smooth) and [base change](#native-algebra-lemma-base-change-smooth). The differential transitivity sequence makes $\Omega_{T/R}=0$ for étale $R\to S\to T$, since both neighboring differential modules vanish. The base-change isomorphism
$$\Omega_{(R'\otimes_R S)/R'}\cong R'\otimes_R\Omega_{S/R}$$
proves the same vanishing after any base change. These give (2) and (3).

For (4), the principal opens $D(g_i)$ cover $\operatorname{Spec}(S)$. Locality of smoothness, including its finite-presentation assertion, makes $S$ smooth over $R$. Localization of differentials gives $(\Omega_{S/R})_{g_i}=0$ on that cover, so local detection makes $\Omega_{S/R}=0$. Finally [smooth algebras are syntomic](#native-algebra-lemma-smooth-syntomic), and the syntomic criterion includes flatness. This proves (6).

**Proof of (5).** Base change gives one inclusion of loci. For the reverse inclusion, fix $\mathfrak q'\in\operatorname{Spec}(S')$ over $\mathfrak q\in\operatorname{Spec}(S)$ and suppose $S'/R'$ is étale there. The [smooth-locus comparison under flat base change](#native-algebra-lemma-flat-base-change-locus-smooth) makes $S/R$ smooth at $\mathfrak q$. Moreover, $S_{\mathfrak q}\to S'_{\mathfrak q'}$ is a flat local map, hence faithfully flat. The differential base-change formula and faithful detection give
$$0=(\Omega_{S'/R'})_{\mathfrak q'}
\cong(\Omega_{S/R})_{\mathfrak q}\otimes_{S_{\mathfrak q}}S'_{\mathfrak q'}
\quad\Longrightarrow\quad(\Omega_{S/R})_{\mathfrak q}=0.$$
The module $\Omega_{S/R}$ is finite because $S/R$ is finitely presented. A product of denominators annihilating a finite generating list therefore makes it zero on a principal neighborhood of $\mathfrak q$. Intersect with a smooth neighborhood. There the algebra is smooth with zero differentials, hence étale, proving the locus equality. Faithfulness was needed only for the localized map at the given pair of points; the base map need not be faithfully flat globally.

**Proof of (7).** The forward implication follows from the definition. Conversely, a finite type $k$-algebra is finitely presented by the Hilbert basis theorem and is flat over the field $k$. Together with $\Omega_{S/k}=0$, these are the hypotheses of *Smooth algebras over a field and the Jacobian criterion*, Theorem 6.2 (flat and unramified). Its complete proof produces square Jacobian neighborhoods by killing the finite kernel after the fibre comparison, then glues the unique lifts. Thus it proves the asserted étaleness, including the zero algebra.

**Proof of (8) and (9).** Use the [global square presentation](#native-algebra-lemma-etale-standard-smooth)
$$S=R[x_1,\ldots,x_n]/(f_1,\ldots,f_n),\qquad
\Delta=\det\left(\frac{\partial f_i}{\partial x_j}\right).$$
Since $\Delta$ is a unit in the quotient, there are polynomials $w,a_1,\ldots,a_n$ satisfying the polynomial identity
$$w\Delta-1=\sum_{i=1}^n a_i f_i.$$
Let $R_0$ be the subring generated over $\mathbf Z$ by all coefficients of these finitely many polynomials. The determinant also has coefficients in $R_0$, and the identity holds in $R_0[x]$. Hence $S_0=R_0[x]/(f_1,\ldots,f_n)$ has invertible square Jacobian and is étale over $R_0$. Base change recovers $S$, proving (8).

The smooth-descent route gives the same conclusion: descend $S/R$ to a smooth algebra over a finite type $\mathbf Z$-subring by [the formal-section construction](#native-algebra-lemma-finite-presentation-fs-noetherian). Its finite projective differential module has locally constant finite rank. The rank-zero locus is a clopen factor, by [the relative-dimension decomposition](#native-algebra-lemma-relative-dimension-cm). Keep that factor. After base change to $R$, all positive-rank factors have empty spectrum because the resulting differential module is zero; thus the retained factor still recovers all of $S$ and is étale.

For (9), choose the same square presentation for $B/A$, together with the polynomials giving the determinant identity. Represent their finitely many coefficients at a common stage $A_i$. The finitely many coefficient equalities in that identity hold after passing to a further stage, by filteredness. The corresponding square presentation there is étale and base changes to $B$. This argument works for a filtered indexing category: its finite diagrams have a common receiving object, and parallel arrows can be equalized.

**Proof of (10) and (11).** The localization $U^{-1}A$ is the filtered colimit of the principal localizations $A_u$ for $u\in U$. Part (9) descends $B'$ to an étale algebra over one $A_u$. Regard that algebra as $B$ over $A$; parts (1) and (2) show it is étale, and localizing it along $U$ gives $B'$. If $0\in U$, the only algebra over $U^{-1}A=0$ is zero, and $B=0$ also gives the assertion.

For (11), the two factors are principal localizations of $B$ at its complementary idempotents $(1,0)$ and $(0,1)$. If $B/A$ is étale, their étaleness follows by (1) and (2). Conversely these two idempotents give a principal cover of $\operatorname{Spec}(B)$, so (4) applies. Equivalently, the product criterion for smoothness and the two components of $\Omega_{B/A}$ give the same conclusion. ∎

#### Definition. Étale ring maps

A homomorphism $R\to S$ is **étale** when $S$ is finitely presented over $R$ and its naive cotangent complex is acyclic:
$$H_1(\mathrm{NL}_{S/R})=0,\qquad\Omega_{S/R}=0.$$
It is **étale at** $\mathfrak q\in\operatorname{Spec}(S)$ if there is a $g\in S\setminus\mathfrak q$ for which $R\to S_g$ is étale. Thus the pointwise condition requires an étale principal neighborhood.

#### Lemma. The Zariski topology on an affine spectrum

Let $R$ be any ring. For a subset $T\subseteq R$, write $V(T)$ for its common vanishing locus in $\operatorname{Spec}(R)$ and $D(f)$ for the complement of $V(f)$.

1. The spectrum is empty precisely for the zero ring.
2. A nonzero ring has a maximal ideal.
3. A nonzero ring has a minimal prime.
4. Given an ideal $I\subseteq\mathfrak p$ with $\mathfrak p$ prime, there is a prime $\mathfrak q$ minimal over $I$ with $\mathfrak q\subseteq\mathfrak p$.
5. For any subset $T$, one has $V(T)=V((T))$, where $(T)$ is its generated ideal.
6. Taking a radical does not change a vanishing locus: $V(I)=V(\sqrt I)$.
7. The radical has the description $\sqrt I=\bigcap_{\mathfrak p\supseteq I}\mathfrak p$, with the empty intersection interpreted as $R$.
8. The equality $V(I)=\varnothing$ is equivalent to $I=R$.
9. For ideals $I,J$, one has $V(I)\cup V(J)=V(I\cap J)$.
10. For any family $(I_a)_{a\in A}$, one has $\bigcap_aV(I_a)=V(\bigcup_a I_a)$.
11. The sets $D(f)$ and $V(f)$ form a disjoint partition of $\operatorname{Spec}(R)$.
12. The open set $D(f)$ is empty precisely when $f$ is nilpotent.
13. Multiplication by a unit does not change a principal open: $D(uf)=D(f)$ for $u\in R^\times$.
14. If $\mathfrak p\notin V(I)$, some $f\in R$ satisfies $\mathfrak p\in D(f)$ and $D(f)\cap V(I)=\varnothing$.
15. Principal opens satisfy $D(fg)=D(f)\cap D(g)$.
16. For any family $(f_i)_{i\in J}$, its union $\bigcup_iD(f_i)$ is the complement of $V(\{f_i:i\in J\})$.
17. If $D(f)=\operatorname{Spec}(R)$, then $f$ is invertible.

**Proof.** The three underlying prime-ideal arguments are written in full in *Spectra of rings*: Lemma 1.1 and Theorem 1.2 prove maximal-ideal existence and the radical intersection formula, while Lemma 4.2 proves the minimal-prime assertion inside a prescribed prime. The first argument applies Zorn's lemma to ideals avoiding a multiplicative set. The second applies it with reversed inclusion to primes between $I$ and $\mathfrak p$, proving that a descending-chain intersection is still prime. These results hold for arbitrary rings. They give (2), (4), and (7) directly. A maximal ideal is prime, so (2) followed by (4) gives (3). Since primes are proper, the zero ring has none; (2) gives the converse in (1).

We record all the topological deductions to specify exactly how these algebraic results are used. Containment of $T$ in a prime is equivalent to containment of $(T)$, which proves (5). A prime containing $I$ contains every element whose power belongs to $I$; hence it contains $\sqrt I$, proving (6). For (8), a proper $I$ is contained in a maximal ideal, by applying (2) to $R/I$, whereas no prime contains the unit ideal.

If a prime contains $I$ or $J$, it contains $I\cap J$. Conversely, if it contains $I\cap J$, it contains $IJ$. If some $a\in I$ lies outside that prime, the products $ab$ for all $b\in J$ force all of $J$ into the prime. This proves (9). A prime contains every $I_a$ exactly when it contains their union, proving (10), also for an empty family.

Part (11) is the definition of $D(f)$. For (12), emptiness means that $f$ lies in every prime, which by (7) for $I=0$ is equivalent to nilpotence. A prime contains $uf$ exactly when it contains $f$ if $u$ is a unit, giving (13). To prove (14), choose $f\in I\setminus\mathfrak p$. It avoids $\mathfrak p$, while every point of $V(I)$ contains it. This gives the claimed neighborhood and disjointness.

A prime avoids $fg$ exactly when it avoids both factors; this proves (15). It lies outside $\bigcup_iD(f_i)$ exactly when it contains every $f_i$, proving (16). Finally, (17) says $V((f))$ is empty. Part (8) then gives $(f)=R$, so $f$ is a unit. These identities agree with the full topology proof in *Spectra of rings*, Proposition 2.1. ∎

#### Example. Étale algebras from polynomial factorizations

Fix $n,m\geq1$. Put
$$R=\mathbf Z[a_1,\ldots,a_{n+m}],\qquad
S=\mathbf Z[b_1,\ldots,b_n,c_1,\ldots,c_m],$$
and introduce the monic polynomials
$$g(x)=x^n+b_1x^{n-1}+\cdots+b_n,\qquad
h(x)=x^m+c_1x^{m-1}+\cdots+c_m.$$
Write $A_k(b,c)$ for the coefficient of $x^{n+m-k}$ in $gh$. The coefficient map $R\to S$ sends $a_k$ to $A_k(b,c)$; thus $a_1\mapsto b_1+c_1$, $a_2\mapsto b_2+b_1c_1+c_2$ when those coefficients occur, and $a_{n+m}\mapsto b_nc_m$. Missing coefficients are interpreted as zero. Equivalently,
$$S=R[b_1,\ldots,b_n,c_1,\ldots,c_m]/(A_k(b,c)-a_k)_{1\leq k\leq n+m}.$$

Use the input order $(b_1,\ldots,b_n,c_1,\ldots,c_m)$ and output order $(A_1,\ldots,A_{n+m})$. Let $J$ be this coefficient Jacobian and let $\Delta=\det J$. A variation of the coefficients of $g$ is a polynomial $u\in S[x]_{<n}$, and one of $h$ is $v\in S[x]_{<m}$. Differentiating the product identifies $J$ with the matrix of
$$\Phi:S[x]_{<n}\oplus S[x]_{<m}\longrightarrow S[x]_{<n+m},
\qquad (u,v)\longmapsto uh+gv,$$
using decreasing-degree monomial bases in both source summands and the target. Thus $J^{\mathsf t}$ has the coefficient rows of
$$x^{n-1}h,\ldots,h,\quad x^{m-1}g,\ldots,g.$$
This specifies every entry and its order without an ambiguous ellipsis pattern.

To fix the resultant convention, define $\operatorname{Res}(g,h)$ by the Sylvester determinant with the $m$ shifted rows of $g$ first and the $n$ shifted rows of $h$ second, again in decreasing degrees. Swapping these two blocks gives the exact comparison
$$\boxed{\Delta=(-1)^{nm}\operatorname{Res}(g,h).}$$
For example, when $n=m=1$,
$$J=\begin{pmatrix}1&1\\c_1&b_1\end{pmatrix},\qquad
\Delta=b_1-c_1,\qquad\operatorname{Res}(x+b_1,x+c_1)=c_1-b_1.$$
The ordered matrix in [Stacks, Tag 00UA](https://stacks.math.columbia.edu/tag/00UA) places the $h$ block first. Its determinant has the comparison above under the stated resultant convention. The map $(a,b)\mapsto ag+bh$ on $S[x]_{<m}\oplus S[x]_{<n}$ uses the opposite block order. Keeping this permutation explicit resolves the sign while preserving all invertibility conclusions.

For a prime $\mathfrak q\subset S$, the following conditions are equivalent:

1. The coefficient map $R\to S$ is étale at $\mathfrak q$.
2. $\Delta\notin\mathfrak q$, equivalently $\operatorname{Res}(g,h)\notin\mathfrak q$.
3. The polynomials $\bar g,\bar h\in\kappa(\mathfrak q)[x]$ are coprime.

Indeed, if $\Delta$ is invertible near the point, the displayed square presentation is standard smooth with zero differential rank and hence étale. Conversely, étaleness makes its differential module vanish at $\mathfrak q$. That module has the square presentation given by $J^{\mathsf t}$. After tensoring with $\kappa(\mathfrak q)$ the square matrix is surjective and therefore invertible, giving (2).

To compare (2) and (3), reduce $\Phi$ to the field $\kappa(\mathfrak q)$. If $\bar g$ and $\bar h$ are coprime and $u\bar h+\bar g v=0$, divisibility by $\bar g$ implies $\bar g\mid u$. Since $\deg u<n$, one has $u=0$, then $v=0$. Thus $\Phi$ is injective and, between vector spaces of the same dimension $n+m$, invertible. If they have a common factor $d$ of positive degree, the nonzero pair
$$u=\bar g/d,\qquad v=-\bar h/d$$
belongs to the two degree-bounded summands and lies in the kernel. This proves the equivalence. Consequently
$$R\longrightarrow S[1/\Delta]=S[1/\operatorname{Res}(g,h)]$$
is étale. Inverting either determinant gives the identical localization because they differ by the unit $(-1)^{nm}$.

#### Lemma. Morphisms between étale algebras

If $S$ and $S'$ are étale $R$-algebras, every $R$-algebra map $S'\to S$ is étale.

**Proof by infinitesimal lifting.** The complete proof is *Formally smooth, unramified and étale ring maps*, Proposition 7.4. It first gives a finite presentation of $S$ over $S'$ by adjoining the finite generators of $S$ and equations for the images of generators of $S'$. In a square-zero lifting problem it lifts $S$ as an $R$-algebra, then uses formal unramifiedness of $S'/R$ to prove that the lift respects the specified $S'$-structure. Existence and uniqueness of the required $S'$-algebra lift, together with that presentation, prove étaleness.

**Proof by fibres and flatness.** Keep the finite presentation just described. Given $\mathfrak q\subset S$, let $\mathfrak q'\subset S'$ and $\mathfrak p\subset R$ be its contractions. The local fibre rings
$$S'_{\mathfrak q'}/\mathfrak pS'_{\mathfrak q'},\qquad
S_{\mathfrak q}/\mathfrak pS_{\mathfrak q}$$
are finite separable extensions of $\kappa(\mathfrak p)$ by the field classification of étale algebras. Their induced homomorphism is a field embedding, hence flat, and the upper field is finite separable over the lower one. Since $R_{\mathfrak p}\to S_{\mathfrak q}$ is flat, the [fibrewise flatness criterion](#native-algebra-lemma-criterion-flatness-fibre), applied with the nonzero module $S_{\mathfrak q}$ over itself, makes $S'_{\mathfrak q'}\to S_{\mathfrak q}$ flat. Both essential finite-presentation conditions hold because the original algebras are étale over $R$.

Also $\mathfrak q'S'_{\mathfrak q'}=\mathfrak pS'_{\mathfrak q'}$ and $\mathfrak qS_{\mathfrak q}=\mathfrak pS_{\mathfrak q}$, so $\mathfrak q'S_{\mathfrak q}=\mathfrak qS_{\mathfrak q}$. The flat local map therefore has the maximal-ideal equality and finite separable residue extension required by [the étale criterion](#native-algebra-lemma-characterize-etale). It is étale at every $\mathfrak q$, and locality proves the result globally. ∎

#### Lemma. Finite presentation and flatness

For a surjective, flat, finitely presented homomorphism $R\to S$, some idempotent $e\in R$ gives an $R$-algebra identification $S\cong R_e$.

**Proof by the defining ideal.** The full algebraic proof is *Formally smooth, unramified and étale ring maps*, Lemma 7.5. With $I=\ker(R\to S)$, finite presentation makes $I$ finite. Flatness gives $I/I^2=0$, and the determinant argument produces an idempotent $a\in I$ generating $I$. Thus $S=R/(a)=R_{1-a}$; take $e=1-a$. This also fixes which of the two complementary idempotents is inverted.

**Proof from the image of the spectrum.** Surjectivity identifies $\operatorname{Spec}(S)$ with a closed subset of $\operatorname{Spec}(R)$. [A flat finitely presented map is open](#native-algebra-proposition-fppf-open), so that subset is clopen and is $D(e)$ for an idempotent $e$. The image of $e$ in $S$ belongs to no maximal ideal and is therefore a unit. Hence the quotient map factors as a surjection $R_e\to S$ whose spectrum is bijective onto $\operatorname{Spec}(R_e)$.

At any prime $\mathfrak p$ of $R_e$, the corresponding localized quotient is nonzero, finite and flat over $(R_e)_{\mathfrak p}$. The finite-flat local theorem makes it free. It is generated by its unit and its residue vector space has dimension one, so it is free of rank one and the quotient homomorphism is an isomorphism. Every localization of the kernel of $R_e\to S$ is consequently zero. Local detection makes that kernel zero, proving the claimed algebra isomorphism. ∎

#### Lemma. Integral extensions

Let $R\to S$ be integral, and let $I$ be an ideal of $R$. Each $z\in IS$ satisfies an equation

$$z^n+a_1z^{n-1}+\cdots+a_n=0,\qquad a_j\in I^j,$$

for some $n\geq1$. Thus $z$ is integral over the ideal $I$.

**Proof.** This is *Integral extensions: lying over, going up and going down*, Lemma 4.2, whose determinant proof applies to arbitrary ring maps. In that proof one writes $z$ as a finite sum of elements of $I$ times integral elements, puts those elements in a finite $R$-subalgebra containing $1$, and represents multiplication by $z$ using a matrix with entries in $I$. Its characteristic coefficients have the required powers of $I$. The adjugate identity annihilates the finite subalgebra, including its identity element, so the resulting equation holds in $S$. Neither injectivity of $R\to S$ nor finite generation of $I$ is needed. ∎

#### Lemma. Going up for integral ring maps

Suppose $R\to S$ is integral. Given primes $\mathfrak p\subset\mathfrak p'$ of $R$ and $\mathfrak q\in\operatorname{Spec}(S)$ above $\mathfrak p$, there is a prime $\mathfrak q'\supset\mathfrak q$ above $\mathfrak p'$.

**Proof.** The full lying-over and going-up argument is *Integral extensions: lying over, going up and going down*, Theorem 3.2. Apply its lying-over assertion to the injective integral map $R/\mathfrak p\to S/\mathfrak q$ and the prime $\mathfrak p'/\mathfrak p$. Pulling the resulting prime back to $S$ gives $\mathfrak q'$. The original map need not be injective; the quotient map used here is injective precisely because $\mathfrak q$ contracts to $\mathfrak p$. ∎

#### Lemma. Going up and closed maps of spectra

For any ring homomorphism $\varphi:R\to S$, going up holds exactly when the induced continuous map

$$f:\operatorname{Spec}(S)\longrightarrow\operatorname{Spec}(R)$$

is closed.

**Proof.** First suppose $f$ is closed. If $\mathfrak q$ contracts to $\mathfrak p$, the closed set $f(V_S(\mathfrak q))$ contains $\mathfrak p$, and therefore contains every $\mathfrak p'\supset\mathfrak p$. Membership in that image supplies a prime $\mathfrak q'\supset\mathfrak q$ contracting to $\mathfrak p'$. This is going up.

Conversely, assume going up, and fix an ideal $J\subset S$. Put $K=\varphi^{-1}(J)$. We prove the exact image formula

$$f(V_S(J))=V_R(K).$$

Only the inclusion from right to left needs proof. Take $\mathfrak p\supset K$ and set $U=R\setminus\mathfrak p$. The ring $U^{-1}(S/J)$ is nonzero: otherwise some $u\in U$ would have image zero in $S/J$, contradicting $K\subset\mathfrak p$. Choose a prime of this localization. Its inverse image is a prime $\mathfrak q_0$ of $S$ containing $J$, whose contraction $\mathfrak p_0$ is contained in $\mathfrak p$. Going up produces $\mathfrak q\supset\mathfrak q_0$ over $\mathfrak p$. It still contains $J$, as required. Existence of a prime in a nonzero ring and the localization correspondence apply without finiteness hypotheses. If $V_R(K)$ is empty, the same equality is immediate. Thus every closed subset has closed image. ∎

#### Lemma. Product decompositions from disjoint closed subsets

For every ring $R$, the assignment $e\mapsto D(e)$ bijects its idempotents with the clopen subsets of $\operatorname{Spec}(R)$. In particular, each such subset is represented by one and only one idempotent.

**Proof using nilpotent correction.** *Spectra of rings*, Lemma 5.1 and Theorem 5.2 prove this at the stated scope. They construct an element with residue value $1$ on the chosen subset and $0$ on its complement, then correct its nilpotent idempotency error. Only that error must be nilpotent; no nilpotence assumption on the whole nilradical is made.

**Proof using finite principal-open covers.** A clopen subset $U$ and its complement are quasi-compact. Choose finite lists with

$$U=\bigcup_iD(f_i),\qquad U^c=\bigcup_jD(g_j),$$

and write $I=(f_i)$ and $J=(g_j)$. These opens cover the spectrum, so $I+J=R$. Each $f_ig_j$ lies in every prime, hence is nilpotent. There are only finitely many such generators of $IJ$, so $(IJ)^N=0$ for some $N\geq1$: if their individual nilpotence exponents are $r_1,\ldots,r_t$, any product of more than $\sum(r_i-1)$ generators vanishes. The binomial expansion of $(I+J)^{2N-1}$ gives $I^N+J^N=R$.

Choose $e\in I^N$ and $h\in J^N$ with $e+h=1$. Since $eh=0$, the element $e$ is idempotent. On $U=V(J)$ its residue is $1$, and on $U^c=V(I)$ its residue is $0$. Hence $D(e)=U$.

Finally, every idempotent has residue value either $0$ or $1$ at each prime, so $D(e)$ and $D(1-e)$ are complementary opens. If $D(e)=D(e')$, both $e(1-e')$ and $e'(1-e)$ have zero image at every prime. They are nilpotent idempotents, hence zero, and therefore $e=ee'=e'$. The empty covers and the zero ring cause no exceptions. ∎

#### Lemma. The characteristic polynomial

For a matrix $A\in\operatorname{Mat}_n(R)$ over any commutative ring, let $P(T)=\det(TI_n-A)$. Then $P(A)=0$.

**Proof by the adjugate identity.** For $n\geq1$, write

$$P(T)=T^n+\sum_{j=0}^{n-1}p_jT^j,\qquad
\operatorname{adj}(TI_n-A)=\sum_{j=0}^{n-1}B_jT^j.$$

Comparing coefficients in $(TI_n-A)\operatorname{adj}(TI_n-A)=P(T)I_n$ gives

$$B_{n-1}=I_n,\qquad B_{j-1}-AB_j=p_jI_n\quad(0\leq j<n),$$

where $B_{-1}=0$. Multiply the identity indexed by $j$ on the left by $A^j$ and add. All intermediate terms cancel, leaving

$$\sum_{j=0}^{n-1}p_jA^j=-A^nB_{n-1}=-A^n.$$

This is the desired equation. The computation avoids substituting a matrix into a polynomial with arbitrary matrix coefficients. For $n=0$, the unique endomorphism of the zero module is zero, so the assertion also holds.

**Universal-matrix route.** The original specialization argument is available as well. Form the matrix $X=(X_{ij})$ over $\mathbb Z[X_{ij}]$ and embed that domain in $\mathbb Q(X_{ij})$. Cayley–Hamilton over this field follows from the adjugate computation just given. Its entries are polynomial identities over $\mathbb Z[X_{ij}]$, so injectivity brings the identities back to that ring. Evaluating $X_{ij}$ at $a_{ij}\in R$ proves the assertion over $R$. Determinants, characteristic coefficients and matrix products all commute with this evaluation. ∎

#### Lemma. Presentations of symmetric and exterior powers

Let $M_2\xrightarrow{u}M_1\to M\to0$ be exact over $R$. For each integer $n\geq1$ there are exact sequences

$$M_2\otimes_R\operatorname{Sym}^{n-1}(M_1)
\longrightarrow\operatorname{Sym}^n(M_1)
\longrightarrow\operatorname{Sym}^n(M)\longrightarrow0$$

and

$$M_2\otimes_R\bigwedge^{n-1}M_1
\longrightarrow\bigwedge^nM_1
\longrightarrow\bigwedge^nM\longrightarrow0.$$

The first arrows send $a\otimes v$ respectively to $u(a)v$ and $u(a)\wedge v$. There is no flatness or finiteness assumption on these modules.

**Proof.** Put $N=\operatorname{im}(u)$, so $M=M_1/N$. The universal property of the symmetric algebra identifies $\operatorname{Sym}_R(M)$ with the quotient of $\operatorname{Sym}_R(M_1)$ by the homogeneous ideal generated by $N$ in degree one: a linear map on $M_1$ factors through $M$ exactly when it kills $N$. Its degree-$n$ part is generated by products of an element of $N$ and an element of degree $n-1$. This is precisely the image of the first displayed arrow. Taking degree $n$ proves the first sequence.

For exterior powers, use the tensor-algebra presentation with the relations $v\otimes v=0$ for every $v\in M_1$. Passing from $M_1$ to $M_1/N$ adds exactly the degree-one relations $N=0$. In the exterior algebra, the identity $v\wedge w=-w\wedge v$ follows by expanding $(v+w)\wedge(v+w)=0$, including in characteristic two. Thus a product containing a factor from $N$ can move that factor to the first position, with the appropriate sign. The degree-$n$ part of the added ideal is consequently the image of $M_2\otimes_R\bigwedge^{n-1}M_1$. This proves the second sequence. In degree zero both quotient maps are the identity of $R$. ∎

#### Lemma. Sections of smooth ring maps

Suppose $\varphi:R\to S$ is smooth and $\sigma:S\to R$ is an $R$-algebra retraction. For $I=\ker(\sigma)$, the $R$-module $I/I^2$ is finite locally free. If it is free of rank $d$, then

$$\widehat S_I\cong R[[t_1,\ldots,t_d]]$$

as $R$-algebras, compatibly with their adic topologies.

**Proof.** The augmentation gives a canonical isomorphism

$$I/I^2\xrightarrow{\ \sim\ }\Omega_{S/R}\otimes_{S,\sigma}R,\qquad [f]\longmapsto df.$$

Indeed, $s\mapsto s-\varphi\sigma(s)\pmod{I^2}$ is an $R$-derivation into $I/I^2$, where $S$ acts through $\sigma$. The product rule follows because the product of two augmentation errors lies in $I^2$. Its map from differentials is inverse to the displayed map. Smoothness makes $\Omega_{S/R}$ finite projective, and hence makes $I/I^2$ finite locally free over $R$.

If $I/I^2$ is free, choose representatives $f_1,\ldots,f_d\in I$ of a basis. Put $P=R[[t_1,\ldots,t_d]]$ and $J=(t_1,\ldots,t_d)$. Substitution $t_i\mapsto f_i$ defines compatible maps

$$\Psi_n:P/J^n\longrightarrow S/I^n\qquad(n\geq1).$$

Every $\Psi_n$ is surjective. To see this, the classes of products $f_{i_1}\cdots f_{i_k}$ generate $I^k/I^{k+1}$ over $R$: expand each factor modulo $I^2$, and reduce the coefficients modulo $I$. Starting with $S/I=R$, successive subtraction in these graded pieces represents every class modulo $I^n$ by a polynomial of degree below $n$.

The map $\Psi_2$ is an isomorphism because both sides are the split square-zero extension of $R$ by the free module with basis $t_i$ or $[f_i]$. Suppose inductively that $n\geq3$ and $\Psi_{n-1}$ is an isomorphism, with inverse $\sigma_{n-1}$. The kernel of $P/J^n\to P/J^{n-1}$ is square-zero. [Formal smoothness of $S/R$](#native-algebra-proposition-smooth-formally-smooth) lifts the composite $S\to S/I^{n-1}\xrightarrow{\sigma_{n-1}}P/J^{n-1}$ to an $R$-algebra map $\tau:S\to P/J^n$.

Reduction modulo $J$ is $\sigma$, so $\tau(I)\subset J/J^n$ and $\tau(I^n)=0$. Hence $\tau$ induces $\bar\tau:S/I^n\to P/J^n$. The endomorphism $\bar\tau\Psi_n$ sends

$$t_i\longmapsto t_i+\delta_i,\qquad \delta_i\in J^{n-1}/J^n.$$

It is an automorphism: the substitution $t_i\mapsto t_i-\delta_i$ is its inverse. Substituting such corrections in a monomial of degree $n-1$ changes it only in degree at least $2n-3\geq n$, so both composites are the identity modulo $J^n$. Therefore $\Psi_n$ is injective, and its already proved surjectivity makes it an isomorphism.

These isomorphisms commute with the quotient maps by their construction; their inverses consequently do as well. Taking inverse limits yields the asserted topological isomorphism. It depends on the chosen basis and its lifts. The same argument includes $d=0$. ∎

#### Lemma. Smoothness and the naive cotangent complex

Let $A\to B\to C$ have surjective composite, and assume $B$ is smooth over $A$. With $I=\ker(A\to C)$ and $J=\ker(B\to C)$, the canonical conormal sequence is short exact:

$$0\longrightarrow I/I^2\longrightarrow J/J^2
\xrightarrow{d}\Omega_{B/A}\otimes_B C\longrightarrow0.$$

**Proof.** The surjection $A\to C$ also makes $B\to C$ surjective. The general [conormal transitivity sequence](#native-algebra-lemma-application-nl) is right exact at the last two terms. To establish injectivity at the first term, apply formal smoothness of $B/A$ to the square-zero extension $A/I^2\to A/I=C$. It gives an $A$-algebra map $\tau:B\to A/I^2$ lifting the given map to $C$. For $b\in J$, its image lies in $I/I^2$; products of two such images vanish. Thus $\tau$ induces $J/J^2\to I/I^2$, and its composite with the canonical map from $I/I^2$ is the identity because $\tau$ is an $A$-algebra map. This proves injectivity. The lifting property used here follows from [smoothness and formal smoothness](#native-algebra-proposition-smooth-formally-smooth). ∎

#### Lemma. Base change of smooth ring maps

If $S$ is smooth over $R$ and $R\to R'$ is any homomorphism, then $S'=S\otimes_RR'$ is smooth over $R'$.

**Proof.** Choose a finite presentation $S=Q/I$, with $Q=R[x_1,\ldots,x_m]$, and put $Q'=R'[x_1,\ldots,x_m]$ and $I'=\ker(Q'\to S')$. Tensoring the presentation shows that $R'\otimes_RI\to I'$ is surjective. Consequently there is a natural surjection

$$E=(I/I^2)\otimes_SS'\longrightarrow E'=I'/(I')^2.$$

Smoothness gives a split exact conormal sequence for $S/R$,

$$0\longrightarrow I/I^2\xrightarrow{d}
\Omega_{Q/R}\otimes_QS\longrightarrow\Omega_{S/R}\longrightarrow0,$$

with finite projective last term. After tensoring with $S'$, it remains split exact. In particular its first map embeds $E$ as a direct summand of $F=(S')^m$. Under the natural identification $F=\Omega_{Q'/R'}\otimes_{Q'}S'$, that map factors as

$$E\twoheadrightarrow E'\xrightarrow{d}F.$$

Since the composite is injective, the first arrow is also injective and hence an isomorphism. It follows that the conormal map for $S'/R'$ is split injective and that its cokernel is $\Omega_{S/R}\otimes_SS'$, a finite projective module. The base-changed algebra is finitely presented, so the naive-cotangent criterion proves smoothness. Split exactness justifies tensoring here even when $R'$ is not flat over $R$. ∎

#### Lemma. Smooth morphisms and local algebra

Smoothness of $R\to S$ is equivalent to smoothness at each point $\mathfrak q\in\operatorname{Spec}(S)$.

**Proof.** A smooth algebra stays smooth after inverting a single element, so the forward direction follows. For the converse, smoothness at each prime supplies principal-open neighborhoods $D(g)$ on which the localized algebra is smooth. Quasi-compactness gives finitely many of them, say $D(g_1),\ldots,D(g_r)$, covering $\operatorname{Spec}(S)$.

The [finite-presentation criterion on a cover of the target](#native-algebra-lemma-cover-upstairs) makes $S$ finitely presented over $R$. By [localization of the naive cotangent complex](#native-algebra-lemma-localize-nl), its degree-one homology vanishes after localization at every $g_i$, hence vanishes globally. Also $\Omega_{S/R}$ localizes to the finite projective modules $\Omega_{S_{g_i}/R}$. The [local criterion for finite projectivity](#native-algebra-lemma-finite-projective) therefore makes $\Omega_{S/R}$ finite projective. These are precisely the finite-presentation and cotangent conditions for smoothness. If $S=0$, the same conclusion holds directly: it is finitely presented and its cotangent complex is zero. ∎

#### Lemma. Characterizations of finite projective modules

*Historical source:* FAC, Chapter II, §4, no. 50, Proposition 4 and its final paragraph, pp. 242–243. There the setting is a finite module on a classical affine variety, and freeness is tested at classical closed points. The arbitrary-ring statement below includes the finite-presentation hypotheses needed to pass from stalks to neighborhoods. The local-to-global formula in that source concerns projective dimension, a homological invariant, rather than module rank. Its closing question about freeness of finite projective modules over a polynomial algebra over a field is the question answered by the Quillen–Suslin theorem; that theorem is outside the present argument.

For an arbitrary $R$-module $M$, the following eight conditions are equivalent:

1. $M$ is flat and finitely presented over $R$.
2. $M$ is finitely generated and projective.
3. There is a module $N$ and a finite integer $n$ with $M\oplus N\cong R^n$.
4. $M$ has a finite presentation, and $M_{\mathfrak p}$ is free for every prime $\mathfrak p$.
5. $M$ has a finite presentation, and $M_{\mathfrak m}$ is free for every maximal ideal $\mathfrak m$.
6. $M$ is finitely generated and locally free.
7. A principal-open cover of $\operatorname{Spec}(R)$ makes $M$ free of finite rank on each member; in other words, $M$ is finite locally free.
8. $M$ is finitely generated, all its prime localizations are free, and the function

   $$\rho_M(\mathfrak p)=\dim_{\kappa(\mathfrak p)}\bigl(M\otimes_R\kappa(\mathfrak p)\bigr)$$

   is locally constant on $\operatorname{Spec}(R)$.

**Proof.** A finite generating map $R^n\twoheadrightarrow M$ splits when $M$ is projective. Conversely, a summand of a free module is projective, since a map out of it can be extended to the free module and lifted across any surjection. This proves (2)$\Leftrightarrow$(3). In a decomposition as in (3), the complementary summand $N$ is finite: project the standard basis of $R^n$ onto it. Hence the quotient presentation of $M$ has finitely many relations. Direct summands of free modules are flat, so (3)$\Rightarrow$(1).

The complete equational proof of (1)$\Rightarrow$(2), including the construction of a splitting that kills every defining relation, is *Tor and flat modules*, Theorem 5.3. That theorem also proves (1)$\Rightarrow$(7). Here is the local Nakayama route to the latter implication. Choose elements of $M$ whose residues form a basis at $\mathfrak p$. They generate on a principal neighborhood, giving a surjection $R_f^r\to M_f$ with finite kernel $K$, because $M$ is finitely presented. Flatness makes

$$0\longrightarrow K\otimes_{R_f}\kappa(\mathfrak p)
\longrightarrow\kappa(\mathfrak p)^r
\longrightarrow M\otimes_R\kappa(\mathfrak p)\longrightarrow0$$

exact. The last arrow is the chosen basis isomorphism. Nakayama gives $K_{\mathfrak p}=0$, and finite generation of $K$ kills it after one further localization away from $\mathfrak p$. The selected elements therefore form a basis on an actual neighborhood.

Quasi-compactness turns a cover as in (7) into a finite one. Finite generation and finite presentation then glue, by the full argument in *Localization, local properties and support*, §5. This proves (7)$\Rightarrow$(6) and (7)$\Rightarrow$(4). Condition (6) implies (7), since finite generation forces each local free rank to be finite. The implication (4)$\Rightarrow$(5) is immediate, and (5)$\Rightarrow$(1) follows from the maximal-local test for flatness in *Tor and flat modules*, Theorem 3.3. A local free basis also makes its rank constant on that neighborhood, giving (7)$\Rightarrow$(8).

One can also obtain projectivity from these local bases through the Hom functor. Once finite presentation has been established, localization of Hom identifies the localization of $\operatorname{Hom}_R(M,-)$ with $\operatorname{Hom}_{R_f}(M_f,-_f)$. Applied to any short exact sequence, the latter functor is exact where $M_f$ is free. Local detection of the resulting kernel and cokernel proves exactness globally. Thus $M$ is projective. This retains the local-to-global proof independently of the equational splitting route.

It remains to prove (8)$\Rightarrow$(7). At a prime $\mathfrak p$, choose $r=\rho_M(\mathfrak p)$ elements lifting a residue basis. Finite generation and Nakayama make them generators on some $D(f)$ containing $\mathfrak p$. Shrink further so that $\rho_M=r$ throughout that open. The resulting surjection $R_f^r\to M_f$ localizes at every prime of $R_f$ to a surjection between free modules of the same rank $r$. Its matrix has determinant outside the local maximal ideal, so is invertible by the adjugate formula. Its kernel and cokernel vanish at all these primes, hence globally. This gives the desired local basis without assuming a finite presentation in (8). All arguments include rank zero and the zero ring. ∎

#### Lemma. Surjective endomorphisms of finite modules

Every surjective endomorphism $\varphi:M\to M$ of a finitely generated module over a commutative ring is invertible.

**Proof by a polynomial annihilator.** Give $M$ an $R[t]$-module structure by letting $t$ act as $\varphi$. It is finite over $R[t]$, and surjectivity says $(t)M=M$. The determinant form of Nakayama supplies an annihilator $1+tq(t)$, with $q(t)\in R[t]$. Thus

$$\operatorname{id}_M+\varphi q(\varphi)=0.$$

Since $q(\varphi)$ commutes with $\varphi$, the endomorphism $-q(\varphi)$ is a two-sided inverse. The zero module is included.

**Proof by induction on a generating list.** For a cyclic module $M\cong R/I$, an endomorphism is multiplication by an element of $R/I$. Surjectivity makes that element a unit. Assume the claim for modules generated by fewer than $n$ elements, over every commutative ring, and let $M$ have $n$ generators. Again view it over $A=R[t]$, with $t$ acting as $\varphi$. Let $M'$ be the $A$-submodule generated by the first $n-1$ generators. The quotient $M/M'$ is cyclic, so its surjective multiplication-by-$t$ map is injective as well.

For $y\in M'$, choose $x\in M$ with $tx=y$. The class of $x$ in $M/M'$ is killed by $t$, hence is zero. This proves $tM'=M'$, so the induction hypothesis over $A$ makes multiplication by $t$ injective on $M'$. If $tx=0$ in $M$, injectivity on the quotient first puts $x$ in $M'$, and injectivity there gives $x=0$. Thus $\varphi$ is injective and therefore an isomorphism. Starting with the zero module covers an empty generating list. ∎

#### Lemma. Smoothness at a point

Let $S$ be a finitely presented $R$-algebra and let $\mathfrak q\in\operatorname{Spec}(S)$. These four conditions are equivalent:

1. The map $R\to S$ is smooth at $\mathfrak q$.
2. $H_1(L_{S/R})_{\mathfrak q}=0$ and $\Omega_{S/R,\mathfrak q}$ is finite free over $S_{\mathfrak q}$.
3. $H_1(L_{S/R})_{\mathfrak q}=0$ and $\Omega_{S/R,\mathfrak q}$ is projective over $S_{\mathfrak q}$.
4. $H_1(L_{S/R})_{\mathfrak q}=0$ and $\Omega_{S/R,\mathfrak q}$ is flat over $S_{\mathfrak q}$.

Here degree-one cotangent homology is computed by the naive cotangent complex.

**Proof.** A finite algebra presentation makes $\Omega_{S/R}$ finitely presented. Over the local ring $S_{\mathfrak q}$, its flatness, projectivity and finite freeness are equivalent: use *Tor and flat modules*, Theorems 5.2–5.3, or the preceding finite-projectivity criterion together with the local finite-flat theorem. This proves the equivalence of (2), (3) and (4). Smoothness on a neighborhood implies these conditions by localization of the naive cotangent complex.

Assume (2). Finite presentation of $\Omega_{S/R}$ spreads its chosen free stalk basis to some $S_g$, with $g\notin\mathfrak q$: first kill the finite cokernel of the map defined by basis representatives, then kill its finite kernel. Choose $S=R[x_1,\ldots,x_n]/I$, with $I$ finitely generated. Over $S_g$, the surjection

$$S_g^n\longrightarrow(\Omega_{S/R})_g$$

splits because its target is free. Its kernel $E$ is a finite projective summand of $S_g^n$. The conormal differential maps $(I/I^2)_g$ onto $E$, and this surjection also splits. Therefore its kernel, $H_1(L_{S/R})_g$, is a direct summand of the finite module $(I/I^2)_g$, and is finite.

That kernel vanishes at $\mathfrak q$ by hypothesis. A further localization away from $\mathfrak q$ kills a finite list of generators of it. On the resulting principal neighborhood, the naive cotangent complex has zero degree-one homology and finite free degree-zero homology. The localized algebra remains finitely presented, so it is smooth. This proves (1). The finiteness of the cotangent kernel was established after splitting the differential sequence; no Noetherian hypothesis on $S$ was used. ∎

#### Definition. Local complete intersections

A homomorphism $R\to S$ is **syntomic**, also called a **flat local complete intersection over $R$**, when it has all three properties: it is flat, it is finitely presented, and for every prime $\mathfrak p$ of $R$ the fibre algebra $S\otimes_R\kappa(\mathfrak p)$ is a local complete intersection over $\kappa(\mathfrak p)$ in the following sense.

#### Definition. Complete intersections over a field

For a finite type algebra $S$ over a field $k$, a **global complete intersection over $k$** means that one can choose a presentation

$$S\cong k[x_1,\ldots,x_n]/(f_1,\ldots,f_c)$$

with $\dim S=n-c$. We also include the zero algebra as a global complete intersection by convention. A finite type $k$-algebra $S$ is a **local complete intersection over $k$** when it admits a principal-open cover $\operatorname{Spec}(S)=\bigcup_iD(g_i)$ for which each $S_{g_i}$ is a global complete intersection. The existence of a suitable presentation or cover is part of these definitions; no particular presentation is prescribed.

#### Lemma. Filtered colimits of naive cotangent complexes

Let $(R_\lambda\to S_\lambda)_{\lambda\in\Lambda}$ be a compatible directed system of ring homomorphisms, and put $R=\varinjlim_\lambda R_\lambda$ and $S=\varinjlim_\lambda S_\lambda$. The functorial canonical presentations give an identification of complexes

$$\mathrm{NL}_{S/R}\cong\varinjlim_\lambda\mathrm{NL}_{S_\lambda/R_\lambda}.$$

**Proof.** Write $P_\lambda=R_\lambda[S_\lambda]$ for the polynomial algebra with one variable $[s]$ for each element $s\in S_\lambda$, and $I_\lambda=\ker(P_\lambda\to S_\lambda)$. Let $P=R[S]$ and $I=\ker(P\to S)$.

A polynomial uses only finitely many coefficients and variables. They can all be represented at one stage of the system, and any equality between finitely many such representatives holds at a later common stage. Hence $P=\varinjlim P_\lambda$. An element represented in $P_\lambda$ lies in $I$ precisely when its image in $S$ is zero, which means its image in some later $S_\mu$ is zero. This gives $I=\varinjlim I_\lambda$. The same finite-witness argument applied to finite sums of products gives $I^2=\varinjlim I_\lambda^2$, and consequently

$$I/I^2\cong\varinjlim_\lambda(I_\lambda/I_\lambda^2).$$

Likewise, finite support in the free modules of differentials gives

$$\bigoplus_{s\in S}S\,d[s]
\cong\varinjlim_\lambda\left(\bigoplus_{s\in S_\lambda}S_\lambda\,d[s]\right).$$

Polynomial differentiation commutes with every transition map. The two identifications therefore respect the conormal differentials and identify the complexes term by term. The module colimits carry the natural $S$-action induced by the compatible $S_\lambda$-actions; neither flat transition maps nor finite presentations are required. ∎

#### Lemma. Prime ideals and dimension in a polynomial ring

Let $S$ be a finite type domain over a field $k$, and write $K=\operatorname{Frac}(S)$ and $r=\operatorname{trdeg}_kK$. Then

$$\dim S=r,\qquad\dim S_{\mathfrak m}=r\quad\text{for every maximal ideal }\mathfrak m\subset S.$$

**Proof.** Both assertions, including the arbitrary ground field, are proved in *Krull dimension and Noether normalization*, Theorem 4.2 and Corollary 4.4. The normalization used there is constructed in §§2–3, with a coordinate argument that works over finite fields as well.

To identify the parameters in that proof, a finite inclusion $k[y_1,\ldots,y_d]\subset S$ gives $\dim S=d$ by integral-extension dimension theory. Localizing at the nonzero polynomials gives a finite-dimensional domain over $k(y_1,\ldots,y_d)$, hence a field. It contains $S$ and is contained in $K$, so equals $K$. Consequently $r=d$. For the assertion at a specified maximal ideal, the complete height-formula proof in Theorem 4.3 uses normalization adapted to that ideal and going down over the normal polynomial base. It gives

$$\operatorname{ht}(\mathfrak m)+\dim(S/\mathfrak m)=\dim S.$$

The quotient is a field and has dimension zero. Since $\operatorname{ht}(\mathfrak m)=\dim S_{\mathfrak m}$, the second assertion follows. Thus the statement concerns every maximal localization, not just the supremum of their dimensions. ∎

#### Lemma. Base change of Kähler differentials

For homomorphisms $R\to S$ and $R\to R'$, put $S'=S\otimes_RR'$. The canonical $S'$-linear map

$$\Omega_{S/R}\otimes_RR'\longrightarrow\Omega_{S'/R'},
\qquad ds\otimes r'\longmapsto r'\,d(s\otimes1)$$

is an isomorphism.

**Proof.** The full universal-property proof is *Kähler differentials*, Theorem 2.1. For clarity, the derivation represented on the left sends $s\otimes r'$ to $ds\otimes r'$. Balancing follows from $d(rs)=r\,ds$ for $r\in R$, and the product rule follows on pure tensors and then on their sums. Restricting an $R'$-derivation of $S'$ to $S$ and extending an $R$-derivation by $s\otimes r'\mapsto r'D(s)$ are inverse operations. They identify the universal derivation modules by exactly the displayed map. No flatness or finite-presentation assumption enters this identification. ∎

#### Lemma. Dimensions of a base, fibre and total space

For a homomorphism $R\to S$ of Noetherian rings and a prime $\mathfrak q$ of $S$ contracting to $\mathfrak p$ of $R$,

$$\dim S_{\mathfrak q}\leq\dim R_{\mathfrak p}
+\dim\bigl(S_{\mathfrak q}/\mathfrak pS_{\mathfrak q}\bigr).$$

**Proof.** This is the upper-bound part of *Dimension theory of Noetherian local rings*, Theorem 5.1. Its proof requires only the stated Noetherian hypotheses. Let $A=R_{\mathfrak p}$, $B=S_{\mathfrak q}$, and denote their maximal ideals by $\mathfrak m$ and $\mathfrak n$. Choose $d=\dim A$ parameters in $A$, and choose $e=\dim(B/\mathfrak mB)$ parameters in the local fibre, with lifts $y_1,\ldots,y_e\in B$. These choices are justified by the local dimension theorem in §2 of the same lesson.

The images of the $d$ base parameters together with the $e$ lifts generate an ideal $J$ whose radical is $\mathfrak n$. Indeed, a prime containing $J$ contains $\mathfrak mB$ because a power of $\mathfrak m$ is contained in the base parameter ideal. Its image in the fibre contains the fibre parameter ideal, and must therefore be the fibre's maximal ideal. Pulling back gives $\mathfrak n$. The parameter characterization of local dimension now bounds $\dim B$ by $d+e$, as claimed. There is no finite-type assumption on the homomorphism. ∎

#### Proposition. Characterizations of separable field extensions

Let $K/k$ be an extension of fields. In characteristic zero all five assertions below hold:

1. $K/k$ is separable.
2. $K$ is geometrically reduced over $k$.
3. The homomorphism $k\to K$ is formally smooth.
4. $H_1(L_{K/k})=0$.
5. The canonical map $K\otimes_k\Omega_{k/\mathbb Z}\to\Omega_{K/\mathbb Z}$ is injective.

If $\operatorname{char}(k)=p>0$, the following six assertions are equivalent:

1. $K/k$ is separable.
2. $K\otimes_k k^{1/p}$ is reduced.
3. $K$ is geometrically reduced over $k$.
4. The canonical map $K\otimes_k\Omega_{k/\mathbb F_p}\to\Omega_{K/\mathbb F_p}$ is injective.
5. $H_1(L_{K/k})=0$.
6. The homomorphism $k\to K$ is formally smooth.

These statements allow arbitrary field extensions, without finite generation.

**Proof.** In positive characteristic, [the reducedness criterion](#native-algebra-lemma-characterize-separable-field-extensions) proves (1)$\Leftrightarrow$(2)$\Leftrightarrow$(3), and [the differential criterion for separability](#native-algebra-lemma-separable-differentials) proves (1)$\Leftrightarrow$(4). Both criteria treat the general extension through its finitely generated subextensions. The [field-lifting argument](#native-algebra-lemma-formally-smooth-extensions-easy) gives (1)$\Rightarrow$(6), including the passage through arbitrary directed unions using degree-one cotangent homology.

For completeness, formal smoothness also explains directly why (6) implies (4). Given a derivation of $k$ over $\mathbb F_p$ into a $K$-vector space $V$, equip $K\oplus V$ with its square-zero multiplication and the $k$-algebra structure $a\mapsto(a,Da)$. Formal smoothness lifts the identity of $K$ through $K\oplus V\to K$. The second component of the lift extends $D$ to $K$. Applying this to the universal derivation into $K\otimes_k\Omega_{k/\mathbb F_p}$ gives a left inverse of the map in (4). Finally [the cotangent criterion for a field extension](#native-algebra-lemma-characterize-formally-smooth-field-extension) identifies (5) and (6), since every $K$-vector space, in particular $\Omega_{K/k}$, is projective.

In characteristic zero, each finitely generated subextension is separably generated, giving separability of the whole extension. The same field-lifting argument gives formal smoothness and then the vanishing of $H_1$. Replacing $\mathbb F_p$ by $\mathbb Z$ in the square-zero derivation argument proves the final injection. Geometric reducedness follows from [preservation of reducedness under separable field extension](#native-algebra-lemma-separable-extension-preserves-reducedness), applied to each extension field of $k$ as a reduced $k$-algebra. ∎

#### Lemma. Degrees of extensions obtained by adjoining p-th roots

Suppose $\operatorname{char}(k)=p>0$ and the differentials $da_1,\ldots,da_n$ are linearly independent in $\Omega_{k/\mathbb F_p}$. Then

$$[k(a_1^{1/p},\ldots,a_n^{1/p}):k]=p^n.$$

**Proof.** For $n=0$ the assertion is the identity extension. Inductively let $L=k(a_1^{1/p},\ldots,a_{n-1}^{1/p})$ have degree $p^{n-1}$. Its monomials

$$\prod_{j<n}a_j^{i_j/p},\qquad 0\leq i_j<p,$$

form a $k$-basis: they span by reducing $p$-th powers, and their number equals the known degree. If $a_n=b^p$ for $b\in L$, express $b$ in this basis, with coefficients $\lambda_I\in k$. Frobenius then gives

$$a_n=\sum_I\lambda_I^p\prod_{j<n}a_j^{i_j}.$$

Differentiating over $\mathbb F_p$ puts $da_n$ in the span of $da_1,\ldots,da_{n-1}$, contrary to the hypothesis. Therefore $a_n$ has no $p$-th root in $L$.

The polynomial $T^p-a_n$ is consequently irreducible over $L$. Indeed, in an algebraic closure it is $(T-b)^p$. If the minimal polynomial of $b$ had degree $d<p$, it would be $(T-b)^d$; its next-to-leading coefficient $-db\in L$ would force $b\in L$, because $1\leq d<p$. Thus adjoining the root has degree $p$, and the tower formula finishes the induction. This argument also supplies the initial one-element case. ∎

#### Lemma. Base change of the naive cotangent complex (Flat base change)

Let $P\twoheadrightarrow S$ be a polynomial presentation over $R$, with kernel $I$, and let $R\to R'$ be flat. Write $P'=P\otimes_RR'$, $S'=S\otimes_RR'$, and let $\alpha'$ be the induced presentation. Then

$$\mathrm{NL}(P\to S)\otimes_RR'
\cong\mathrm{NL}(P\to S)\otimes_SS'
\cong\mathrm{NL}(\alpha').$$

In particular, the canonical comparison $\mathrm{NL}_{S/R}\otimes_SS'\to\mathrm{NL}_{S'/R'}$ is a homotopy equivalence.

**Proof.** Flatness preserves the exact sequence defining $I$, so $I'=\ker(P'\to S')$ is $I\otimes_RR'$. Its square is the image of $I^2\otimes_RR'$: products of tensors generate the ideal on both sides. Right exactness therefore identifies

$$I'/(I')^2\cong(I/I^2)\otimes_RR'.$$

The degree-zero terms agree by base change of polynomial differentials. These identifications send the conormal differential of $i$ to the differential of its image, so they identify the complexes, not only their homology. To pass to canonical presentations, use the full comparison-of-presentations proof: its polynomial lifts give homotopy equivalences, and tensoring preserves their homotopy identities. This also identifies the resulting map with the canonical comparison. Arbitrarily many polynomial variables are allowed. ∎

#### Lemma. Base change of flat modules

Extension of scalars along any $R\to R'$ carries flat $R$-modules to flat $R'$-modules and preserves faithful flatness as well. Thus $M'=R'\otimes_RM$ has the corresponding property over $R'$ whenever $M$ has it over $R$.

**Proof.** For each $R'$-module $N$, associativity gives a natural isomorphism

$$N\otimes_{R'}M'\cong N\otimes_RM.$$

An injection of $R'$-modules is an injection of their underlying $R$-modules, so flatness on the right proves flatness on the left. If $M$ is faithfully flat and $N\ne0$, the underlying $R$-module is nonzero and $N\otimes_RM\ne0$. Thus tensoring with $M'$ also detects nonzero modules, which proves faithful flatness. ∎

#### Lemma. Noetherianity under extension of the ground field

If $A$ is a Noetherian $k$-algebra and $K/k$ is a finitely generated field extension, then $K\otimes_kA$ is Noetherian.

**Proof.** Choose finitely many field generators $u_1,\ldots,u_r$ for $K/k$ and set $B=k[u_1,\ldots,u_r]\subset K$. Its fraction field is $K$. With $U=B\setminus\{0\}$,

$$K\otimes_kA\cong U^{-1}(B\otimes_kA).$$

The algebra $B\otimes_kA$ has finitely many generators over $A$, hence is Noetherian by the Hilbert basis theorem and passage to a quotient. Its localization is Noetherian as well. The images of elements of $U$ may be zero divisors in the tensor algebra; localization preserves Noetherianity in that case too. ∎

#### Lemma. Criteria for geometric regularity

Let $A$ be a Noetherian algebra over a field $k$. The following tests are equivalent:

1. $A\otimes_kK$ is regular for every finitely generated field extension $K/k$.
2. $A\otimes_kk'$ is regular for every finite purely inseparable extension $k'/k$.

Regularity here is regularity of a Noetherian ring. The preceding Noetherianity lemma ensures that all rings appearing in these tests are Noetherian.

**Proof.** Every finite purely inseparable extension is finitely generated, so the first test implies the second. Conversely, assume the second and fix $K/k$ finitely generated. The [purely inseparable adjustment lemma](#native-algebra-lemma-make-separable) gives a commutative square of field inclusions

$$\begin{matrix}k&\longrightarrow&K\\
\big\downarrow&&\big\downarrow\\
k'&\longrightarrow&K',\end{matrix}$$

where both vertical extensions are finite purely inseparable and $K'/k'$ is separable. The extension $K'/k'$ is still finitely generated. Choose a smooth $k'$-domain $B$ with fraction field $K'$, as in [the smooth-model lemma for separable extensions](#native-algebra-lemma-localization-smooth-separable).

Put $F=A\otimes_kk'$. The second test makes $F$ regular. The algebra $F\otimes_{k'}B$ is smooth over $F$, by base change, so it is regular by [ascent along a regular ring map](#native-algebra-lemma-regular-goes-up). Localizing at the nonzero elements of $B$ gives the regular ring

$$F\otimes_{k'}K'\cong A\otimes_kK'.$$

Finally, $A\otimes_kK\to A\otimes_kK'$ is faithfully flat, being obtained from the field extension $K\to K'$ by base change. [Descent of regularity](#native-algebra-lemma-descent-regular) makes $A\otimes_kK$ regular. Since $K$ was arbitrary, the first test holds. In characteristic zero the purely inseparable extensions in the construction are trivial. ∎

#### Lemma. Regularity over a regular base with regular fibre

Suppose $(R,\mathfrak m)\to(S,\mathfrak n)$ is a flat local map of Noetherian local rings. If $R$ and $S/\mathfrak mS$ are regular, then $S$ is regular.

**Proof.** Write $d=\dim R$ and $e=\dim(S/\mathfrak mS)$. Regularity supplies generators $x_1,\ldots,x_d$ of $\mathfrak m$ and generators $\bar y_1,\ldots,\bar y_e$ of the maximal ideal in the fibre. Lift the latter to $y_j\in\mathfrak n$. Every element of $\mathfrak n$ is a linear combination of these lifts modulo $\mathfrak mS$, and $\mathfrak mS$ is generated by the images of the $x_i$. Thus the combined list generates $\mathfrak n$.

The flat local dimension formula gives $\dim S=d+e$. The embedding dimension of a Noetherian local ring is at least its dimension, while the displayed list bounds it above by $d+e$. Equality follows, which is the defining criterion for regularity of $S$. Empty parameter lists cause no exception. ∎

#### Lemma. Permanence of flat ring maps

Let $R\to S$ be a homomorphism, and let $M$ be an $S$-module which is flat over $R$ and faithfully flat over $S$. Then $S$ is flat over $R$.

**Proof.** For an injection $N_1\hookrightarrow N_2$ of $R$-modules, consider its tensor with $S$. Tensoring that map further over $S$ with $M$ identifies it with

$$N_1\otimes_RM\longrightarrow N_2\otimes_RM,$$

which is injective by $R$-flatness. Exactness of tensoring with the flat $S$-module $M$ identifies its kernel with the tensor of the original kernel. Faithfulness detects a zero module, so the original kernel is zero. Every injection is therefore preserved by tensoring with $S$, proving $R$-flatness. No finiteness or local hypothesis is needed. ∎

#### Lemma. Descent of geometric regularity

If $A\to B$ is faithfully flat over a field $k$ and $B$ is geometrically regular over $k$, then $A$ is geometrically regular over $k$.

**Proof.** First $B$ is Noetherian, and faithful flatness descends this property to $A$. Explicitly, for any ideal $J\subset A$, finitely many elements of $J$ already generate $JB$ because $B$ is Noetherian. Let $J_0\subset J$ be the ideal they generate. Flatness identifies $(J/J_0)\otimes_AB$ with $JB/J_0B=0$, and faithfulness gives $J=J_0$. Thus every ideal of $A$ is finitely generated.

Now let $k'/k$ be finite purely inseparable. Base change preserves faithful flatness, giving

$$A\otimes_kk'\longrightarrow B\otimes_kk'.$$

Its target is regular by the hypothesis on $B$. [Faithfully flat descent of regularity](#native-algebra-lemma-descent-regular) makes its source regular. The preceding criterion for geometric regularity, now applicable because $A$ is Noetherian, proves the result. ∎

#### Lemma. A variant of the local criterion for flatness

Let $R\to S$ be a local map of Noetherian local rings, let $I\subsetneq R$, and let $M$ be a finite $S$-module. If

$$\operatorname{Tor}_1^R(M,R/I)=0\qquad\text{and}\qquad
M/IM\text{ is flat over }R/I,$$

then $M$ is flat over $R$.

**Proof through the residue field.** The complete quotient argument and local criterion are *Faithful flatness and the local criterion for flatness*, Lemma 4.3, Corollary 4.4 and Theorem 4.2. With $\mathfrak m$ the maximal ideal of $R$, the proper ideal $I$ is contained in $\mathfrak m$. Hence it annihilates $\kappa=R/\mathfrak m$. Lemma 4.3 gives $\operatorname{Tor}_1^R(\kappa,M)=0$, and Theorem 4.2 gives flatness. Symmetry of Tor over a commutative ring identifies the hypothesis here with the order of its arguments in that lemma. Finiteness is required over $S$, as stated, rather than over $R$.

**Proof using a tensor relation.** The same local criterion reduces the problem to injectivity of $\mathfrak m\otimes_RM\to M$. Suppose

$$z=\sum_i f_i\otimes x_i,\qquad f_i\in\mathfrak m,\qquad\sum_i f_ix_i=0.$$

Apply the equational flatness criterion to this relation in $M/IM$ over $R/I$. Lift its finite factorization to elements $a_{ij}\in R$ and $y_j\in M$. Then

$$x_i-\sum_j a_{ij}y_j\in IM,\qquad
c_j=\sum_i f_ia_{ij}\in I.$$

In $\mathfrak m\otimes_RM$ the original tensor can therefore be written as

$$z=\sum_i f_i\otimes\left(x_i-\sum_j a_{ij}y_j\right)
+\sum_j c_j\otimes y_j.$$

Each term comes from $I\otimes_RM$. For the first sum, express its parenthesized element as a finite sum $\sum_\ell b_{i\ell}v_{i\ell}$ with $b_{i\ell}\in I$ and move the coefficients across the tensor sign; then $f_ib_{i\ell}\in I$. The second sum already has coefficients in $I$. Thus $z$ is the image of some $w\in I\otimes_RM$.

Multiplication sends $w$ to the same zero element of $M$ as $z$. The Tor hypothesis makes $I\otimes_RM\to M$ injective, by the exact sequence of $0\to I\to R\to R/I\to0$. Hence $w=0$ and $z=0$. The maximal-ideal tensor map is injective, so the Noetherian local criterion proves flatness. ∎

#### Lemma. Transitivity of finite ring extensions

For ring homomorphisms $R\to S\to T$, finiteness of both successive maps implies finiteness of their composite.

**Proof.** Choose finite module generators $s_1,\ldots,s_a$ of $S$ over $R$ and $t_1,\ldots,t_b$ of $T$ over $S$. Expanding an element of $T$ first in the $t_i$ and then expanding its coefficients in the $s_j$ expresses it as an $R$-linear combination of the $ab$ products $s_jt_i$. This is also the special case $M=T$ of [finite modules over a finite extension](#native-algebra-lemma-finite-module-over-finite-extension). ∎

#### Lemma. Finite length over an Artinian ring

A commutative ring is Artinian exactly when its underlying module has finite length. It is then Noetherian, every prime is maximal, and the canonical homomorphism

$$R\longrightarrow\prod_{\mathfrak m\in\operatorname{Max}(R)}R_{\mathfrak m}$$

is an isomorphism with finitely many factors. The empty product gives the zero ring.

**Proof.** The full argument is *Noetherian and Artinian rings*, Lemma 4.1 and Theorem 4.2. In particular, its radical-nilpotence proof uses the descending chain condition directly; it does not assume finite generation before proving that an Artinian ring is Noetherian.

Here is how the length calculation and the local factors enter. For an Artinian ring the cited lemma proves that all primes are maximal, there are finitely many of them, and their intersection $J$ satisfies $J^N=0$. The Chinese remainder theorem decomposes $R/J$ into its residue fields. Each layer $J^i/J^{i+1}$ is Artinian over this product and thus splits into finitely many Artinian vector spaces. Each vector space has finite dimension: an infinite basis would produce a strictly descending sequence of subspaces by deleting one basis vector at each step. These layers therefore have finite length, and their finite filtration gives finite length to $R$.

For the product assertion, the powers $\mathfrak m^N$ of the distinct maximal ideals are pairwise comaximal, and their product is $J^N=0$. Chinese remainders give $R\cong\prod R/\mathfrak m^N$. Each factor is local; localizing the product at the corresponding maximal ideal keeps that factor and kills the others. Hence the displayed isomorphism is the natural localization map. Finally, finite length implies both chain conditions, so it implies both the Artinian and Noetherian properties. ∎

#### Lemma. Finiteness in short exact sequences

Consider an exact sequence of modules over an arbitrary ring $R$:

$$0\longrightarrow M_1\longrightarrow M_2\longrightarrow M_3\longrightarrow0.$$

The following implications hold:

1. Finite generation of $M_1$ and $M_3$ implies finite generation of $M_2$.
2. Finite presentation of $M_1$ and $M_3$ implies finite presentation of $M_2$.
3. A finitely generated $M_2$ has finitely generated quotient $M_3$.
4. If $M_2$ is finitely presented and $M_1$ is finitely generated, then $M_3$ is finitely presented.
5. If $M_3$ is finitely presented and $M_2$ is finitely generated, then $M_1$ is finitely generated.

**Proof.** For (1), use generators of $M_1$ together with lifts of generators of $M_3$. Their span contains the kernel and maps onto the quotient, so it is all of $M_2$. For (3), take the images of a generating set.

To prove (5), take a finite presentation $R^a\xrightarrow{d}R^b\to M_3\to0$ and lift the basis of $R^b$ to $M_2$. Write $v:R^b\to M_2$ for the resulting map. The image of $vd$ lies in $M_1$, giving $w:R^a\to M_1$. There is a canonical isomorphism

$$M_1/\operatorname{im}(w)\ \cong\ M_2/\operatorname{im}(v).$$

Indeed, every element of $M_2$ differs from an element of $\operatorname{im}(v)$ by one of $M_1$, since $R^b\to M_3$ is onto. If $v(x)$ belongs to $M_1$, then $x\in\operatorname{im}(d)$, so the intersection $M_1\cap\operatorname{im}(v)$ equals $\operatorname{im}(w)$. The right-hand quotient is finite by (3), and $\operatorname{im}(w)$ is finite because $R^a$ is. Applying (1) proves (5). This is the explicit kernel-and-cokernel calculation underlying the snake-lemma argument.

For (4), start with $R^a\to R^b\to M_2\to0$. Lift a finite generating list of $M_1$ to $R^b$. The original $a$ relation vectors together with these finitely many lifts generate the kernel of $R^b\to M_3$, and therefore give a finite presentation of $M_3$.

For (2), choose finite free modules $F_1,F_3$ surjecting onto $M_1,M_3$, and lift the basis of $F_3$ to $M_2$. This gives a surjection $F_1\oplus F_3\to M_2$. If $K_1,K_2,K_3$ are the kernels of these three surjections, projection onto $F_3$ gives

$$0\longrightarrow K_1\longrightarrow K_2\longrightarrow K_3\longrightarrow0.$$

Surjectivity on the right follows by correcting a lift of an element of $K_3$ with an element of $F_1$. Part (5) makes $K_1$ and $K_3$ finite, since the corresponding quotients are finitely presented. Part (1) then makes $K_2$ finite, which is precisely a finite set of relations for the chosen finite free cover of $M_2$. ∎

#### Lemma. Composition of finite-type ring maps

Finite type and finite presentation satisfy these four rules:

1. Two successive finite type homomorphisms have finite type composite.
2. Two successive finitely presented homomorphisms have finitely presented composite.
3. In $R\to S'\to S$, finite type of $S$ over $R$ implies finite type over $S'$.
4. In the same diagram, if $S$ is finitely presented over $R$ and $S'$ is of finite type over $R$, then $S$ is finitely presented over $S'$.

**Proof.** For (1), join a finite list of algebra generators for the first map to a list for the second. For (3), the original $R$-algebra generators also generate over $S'$.

For (2), write $S=R[x_1,\ldots,x_a]/(f_1,\ldots,f_b)$ and $T=S[y_1,\ldots,y_c]/(g_1,\ldots,g_d)$. Lift each coefficient of each $g_j$ to a polynomial in the $x_i$, producing $\widetilde g_j\in R[x,y]$. Then

$$T\cong R[x,y]/(f_1,\ldots,f_b,\widetilde g_1,\ldots,\widetilde g_d),$$

which is a finite presentation over $R$.

For (4), choose $S=R[x]/(f_1,\ldots,f_b)$ and $S'=R[y_1,\ldots,y_c]/I$, with finite lists $x,y$. Represent the image of $\bar y_j$ in $S$ by $h_j(x)\in R[x]$. The given homomorphism induces

$$S\cong S'[x]/(f_1,\ldots,f_b,\ h_1(x)-\bar y_1,\ldots,h_c(x)-\bar y_c).$$

To verify this presentation, the displayed relations force every coefficient from $S'$ to have its prescribed expression in the $x_i$. Relations from $I$ already vanish in $S$, so impose no additional relations beyond $(f_1,\ldots,f_b)$ after that substitution. The resulting maps in both directions fix $R$, all $x_i$, and all $\bar y_j$. They are inverse, proving the assertion without a finite-generation assumption on $I$. ∎

#### Lemma. Composition of essentially finite-type ring maps

Composites of essentially finite type homomorphisms are essentially of finite type. The same assertion holds with “finite presentation” in place of “finite type.” Localization may be at an arbitrary multiplicative set.

**Proof.** Write the first algebra as $S=U^{-1}A$, where $A$ is of finite type over $R$, and the second as $T=V^{-1}C$, where $C$ is of finite type over $S$. Choose $C=S[x_1,\ldots,x_n]/J$. Let $J_0$ be the contraction of $J$ to $A[x]$, and set $B=A[x]/J_0$. The correspondence for ideals in a localization gives $C=U^{-1}B$. Thus $T$ is a localization of the finite type $R$-algebra $B$, proving the first assertion.

For the second assertion choose $A$ finitely presented over $R$ and $C=S[x]/(f_1,\ldots,f_m)$. Only finitely many coefficients occur in these polynomials. There is consequently $u\in U$ such that they all lift to $A_u$. Choose lifted polynomials $\widetilde f_i\in A_u[x]$ and put

$$B=A_u[x]/(\widetilde f_1,\ldots,\widetilde f_m).$$

The algebra $A_u$ has a finite presentation obtained by adjoining $z$ with $uz-1=0$, so the preceding composition lemma makes $B$ finitely presented over $R$. Again $C=U^{-1}B$, and $T$ is a further localization. More explicitly, if $v\in V$ is represented by $b/u'$ in $U^{-1}B$, then after inverting $U$ it suffices to invert the numerator $b$. Inverting all these numerators along with $U$ exhibits $T$ as one localization of $B$. No finiteness of either multiplicative set is required. ∎

#### Lemma. Smooth localizations of separable extensions

For a finitely generated extension of fields $K/k$, separability is equivalent to the existence of a smooth $k$-algebra $B$ whose localization is $K$.

**Proof.** Suppose first that $K/k$ is separable. Choose a separating transcendence basis $t_1,\ldots,t_r$. The finite separable extension of $F=k(t_1,\ldots,t_r)$ is simple, say $K=F(\alpha)$; this is the [finite-generation and primitive-element description](#native-algebra-lemma-generating-finitely-generated-separable-field-extensions). Let $f\in F[X]$ be the monic minimal polynomial of $\alpha$. Choose a nonzero $h\in k[t_1,\ldots,t_r]$ so that every coefficient of $f$ belongs to $A=k[t_1,\ldots,t_r]_h$. Then

$$B=\bigl(A[X]/(f)\bigr)_{f'}$$

is standard smooth over $A$ because its one equation has invertible derivative. The algebra $A$ is smooth over $k$, so composition gives smoothness of $B$ over $k$. Monicity makes $A[X]/(f)$ free over $A$ and embeds it into its scalar extension $F[X]/(f)=K$. Since $f'(\alpha)\ne0$, the localization defining $B$ is a subring of $K$ with fraction field $K$. Thus inverting its nonzero elements gives the desired localization. When $K=F$, one may take $\alpha=0$ and $f=X$.

Conversely, a localization of a smooth algebra is formally smooth. Indeed, lift a map from the smooth algebra across a nilpotent ideal; every element inverted in the target remains invertible in the lift, because invertibility lifts across nilpotent ideals. The lift therefore extends to the localization. The [formal-smoothness criterion for fields](#native-algebra-lemma-fields-are-formally-smooth) now gives separability of $K/k$.

The generic-point proof gives another description of the same result. Choose a finite type $k$-domain $A_0$ with fraction field $K$. The [generic smoothness criterion](#native-algebra-lemma-smooth-at-generic-point) says that its generic point is smooth precisely when $K/k$ is separable. A smooth principal neighborhood of that point has fraction field $K$, so its further localization is $K$. This retains the generic-point route as well as the explicit standard-smooth model. ∎

#### Lemma. Completion at a quasi-finite prime

Let $R$ be Noetherian, let $S$ be an $R$-algebra of finite type, and let $\mathfrak q\subset S$ contract to $\mathfrak p\subset R$. Assume the homomorphism is quasi-finite at $\mathfrak q$. There is an $\widehat{R_{\mathfrak p}}$-algebra $B$ and a decomposition

$$\widehat{R_{\mathfrak p}}\otimes_RS
\ \cong\ \widehat{S_{\mathfrak q}}\times B$$

whose first projection is the natural homomorphism to the completed local ring. Both local completions use their maximal ideals.

**Proof.** First obtain a finite algebra model near the specified prime. The pointwise [affine Zariski main theorem](#native-algebra-theorem-main-theorem) gives an element $g$ of the integral closure $\overline R\subset S$, outside $\mathfrak q$, with $\overline R_g=S_g$. Take finite $R$-algebra generators $s_i$ of $S$ and write each $s_i=a_i/g^{n_i}$ in $S_g$, with $a_i\in\overline R$. Set $C=R[g,a_1,\ldots,a_l]\subset S$. All these generators are integral over $R$, so $C$ is finite over $R$. The inclusion induces $C_g\cong S_g$: surjectivity follows from the chosen expressions, and injectivity follows by localizing the inclusion. For $\mathfrak r=\mathfrak q\cap C$, this gives $C_{\mathfrak r}\cong S_{\mathfrak q}$. If the original map is quasi-finite everywhere, the [quasi-finite open in the integral closure](#native-algebra-lemma-quasi-finite-open-integral-closure) gives the same finite model directly. The pointwise theorem supplies exactly the weaker hypothesis used here.

Put $\widehat R=\widehat{R_{\mathfrak p}}$ and $D=\widehat{C_{\mathfrak r}}$. The finite-extension completion lemma below gives

$$E=\widehat R\otimes_RC\cong D\times E'.$$

The $D$-component of $g$ is a unit. Tensoring this decomposition over $C$ with $S$ gives

$$\widehat R\otimes_RS\cong A\times B,
\qquad A=D\otimes_CS.$$

The image of $g$ is already invertible in $A$, since it is invertible in $D$. As $C_g\cong S_g$,

$$A\cong A_g
\cong D\otimes_{C_g}S_g
\cong D
\cong\widehat{S_{\mathfrak q}}.$$

It remains to identify the first projection. On the factor $\widehat R$ it is the map induced by $R_{\mathfrak p}\to C_{\mathfrak r}\cong S_{\mathfrak q}$. For $s\in S$, equality after localizing at $g$ means that some power $g^Ns$ equals an element of $C$ in $S$; if necessary, increase the exponent to kill the localization error. The two candidate maps agree on this element and on $g$. Its image is a unit in $\widehat{S_{\mathfrak q}}$, so cancellation shows that the maps agree on $s$. They agree on both tensor factors and hence are identical. ∎

#### Lemma. Finite free algebras with a prescribed residue extension

Let $\mathfrak p$ be a prime of an arbitrary ring $R$, and let $L/\kappa(\mathfrak p)$ be finite. One can find an $R$-algebra $S$, finite free as an $R$-module, such that $\mathfrak q=\mathfrak pS$ is prime and the induced extension $\kappa(\mathfrak q)/\kappa(\mathfrak p)$ is the given extension.

**Proof.** Begin with a simple extension $L=\kappa(\mathfrak p)(\alpha)$ of degree $d$. Write its monic minimal polynomial as

$$X^d+\sum_{i<d}a_iX^i.$$

Choose one common denominator $g\in R\setminus\mathfrak p$ for the finitely many coefficients, writing $a_i$ as the residue of $f_i/g$. Replacing $\alpha$ by $\beta=g\alpha$ preserves the generated field and changes the coefficient of $X^i$ to $g^{d-i}a_i$, which is the residue of $g^{d-i-1}f_i\in R$. Choose these lifts $b_i$ and set

$$S=R[X]/\left(X^d+\sum_{i<d}b_iX^i\right).$$

Monic division gives the free $R$-basis $1,X,\ldots,X^{d-1}$. Moreover, $S/\mathfrak pS$ is free over the domain $R/\mathfrak p$, so it injects into its localization at the nonzero elements of $R/\mathfrak p$. That localization is $L$, by the minimal polynomial of $\beta$. Consequently $S/\mathfrak pS$ is a domain with fraction field $L$. This proves both primeness and the required identification of residue fields, even when $\mathfrak p$ is not maximal.

For a general finite extension, induct on its degree. Degree one uses $S=R$. If a proper nontrivial intermediate field $L'$ exists, construct a finite free $R$-algebra $S'$ for $L'/\kappa(\mathfrak p)$ and then a finite free $S'$-algebra $S$ for $L/L'$. Products of the two free bases give a finite free $R$-basis. The final prime is $(\mathfrak pS')S=\mathfrak pS$, and the residue identifications compose. If no such intermediate field exists, any element of $L\setminus\kappa(\mathfrak p)$ generates $L$, reducing to the simple case. No separability assumption is needed. ∎

#### Lemma. Completion of a finite ring extension

Suppose $R$ is Noetherian and $S$ is finite over $R$. For a prime $\mathfrak p\subset R$, let $\mathfrak q_1,\ldots,\mathfrak q_m$ be the finitely many primes of $S$ above it. Then the canonical maps give

$$\widehat{R_{\mathfrak p}}\otimes_RS
\ \cong\ \widehat{S\otimes_RR_{\mathfrak p}}
\ \cong\ \prod_{i=1}^m\widehat{S_{\mathfrak q_i}}.$$

The middle completion is for the extended ideal $\mathfrak pR_{\mathfrak p}$; those on the right are for the respective maximal ideals.

**Proof.** Replace $R$ by $R_{\mathfrak p}$ and $S$ by $S\otimes_RR_{\mathfrak p}$, and denote the maximal ideal of the new base by $\mathfrak m$. The finite algebra $S/\mathfrak mS$ is finite-dimensional over $R/\mathfrak m$. It is Artinian, and its finitely many primes give exactly the primes $\mathfrak q_i$ above $\mathfrak m$. Integrality of $S$ over the local ring $R$ implies that these are all the maximal ideals of $S$.

For each $n\geq1$, the ring $R/\mathfrak m^n$ has finite length: the layers of its maximal-ideal filtration are finite-dimensional residue-field spaces, since $R$ is Noetherian. Thus the finite module $S/\mathfrak m^nS$ also has finite length over $R/\mathfrak m^n$, and its ideals satisfy the descending chain condition. The Artinian decomposition proved above gives, naturally at every order,

$$S/\mathfrak m^nS
\ \cong\ \prod_{i=1}^m S_{\mathfrak q_i}/\mathfrak m^nS_{\mathfrak q_i}.$$

These maps are the localization maps, so commute with reduction in $n$. Taking inverse limits commutes with this finite product. In each Noetherian local ring $S_{\mathfrak q_i}$, the radical of $\mathfrak mS_{\mathfrak q_i}$ is its maximal ideal $\mathfrak q_iS_{\mathfrak q_i}$: the quotient is the corresponding local factor of the zero-dimensional fibre. Some power of the maximal ideal is therefore contained in $\mathfrak mS_{\mathfrak q_i}$. The two adic filtrations are cofinal, and their completions agree. This proves the second isomorphism.

Finally, *Completion*, Theorem 3.1 proves the natural tensor-completion isomorphism for every finite module over a Noetherian ring. Applied to $S$, it supplies the first isomorphism. Its proof uses Artin–Rees and a finite free presentation, so it applies to the present finite algebra without any flatness assumption on $S$. If the fibre is empty, Nakayama gives $S=0$ after the initial localization, and the empty product agrees with the zero ring. ∎

#### Lemma. A complete local domain finite over a regular ring

Every complete Noetherian local domain $(R,\mathfrak m,k)$ contains a complete regular local subring $R_0$ such that $R$ is finite over $R_0$ and their residue fields agree. The subring can be chosen in one of the forms

$$k[[X_1,\ldots,X_d]]\qquad\text{or}\qquad C[[X_1,\ldots,X_d]],$$

where $C$ is a Cohen ring. The number of variables is $\dim R$ in the first case and $\dim R-1$ in the second.

**Proof.** Use the complete coefficient-ring construction in *Coefficient rings and the Cohen structure theorem*, Theorem 5.1, whose preceding §§1–4 supply its lifting arguments. Its image in a domain is either a coefficient field or an embedded Cohen DVR. Indeed, in residue characteristic $p>0$ the coefficient map has kernel either zero or $(p^e)$ in a DVR. A domain cannot contain the nonzero nilpotents of a quotient with $e>1$. Thus either $e=1$, giving a field, or the kernel is zero. In residue characteristic zero it gives a field directly.

First suppose the coefficient subring is the field $k$. Put $d=\dim R$ and choose a system of parameters $x_1,\ldots,x_d\in\mathfrak m$, so $I=(x_1,\ldots,x_d)$ has radical $\mathfrak m$. The complete parameter theorem is *Dimension theory of Noetherian local rings*, §2. Powers of $I$ and $\mathfrak m$ are cofinal, so $R$ is complete and separated for $I$ as well. Substitution of the $x_i$ gives a homomorphism

$$\phi:k[[X_1,\ldots,X_d]]\longrightarrow R.$$

The quotient $R/I$ has finite length and residue field $k$, so is finite-dimensional over the coefficient field. Apply the [complete-base finiteness lemma](#native-algebra-lemma-finite-over-complete-ring) to $R$ as a module over the power-series ring, with ideal $(X_1,\ldots,X_d)$. Completeness of the base, separatedness of $R$, and the just-proved finiteness modulo that ideal give finiteness of $\phi$.

Now suppose the coefficient subring is a Cohen ring $C$ with uniformizer $p$. The nonzero element $p\in R$ is a nonzerodivisor. The [one-equation dimension lemma](#native-algebra-lemma-one-equation) gives $\dim(R/pR)=\dim R-1=d$. Choose lifts $x_1,\ldots,x_d\in\mathfrak m$ of parameters of $R/pR$. Then $I=(p,x_1,\ldots,x_d)$ has radical $\mathfrak m$. Substitution defines

$$\phi:C[[X_1,\ldots,X_d]]\longrightarrow R.$$

The source is complete for $(p,X_1,\ldots,X_d)$, and $R$ is separated for its image ideal $I$. The quotient $R/I$ has finite length over its residue field $k=C/pC$. The same complete-base finiteness lemma again proves that $\phi$ is finite.

In both cases the source $A$ is a complete regular local domain, of the stated dimension. For a field its maximal ideal is generated by the variables; for a Cohen DVR it is generated by $p$ and the variables. The formal power-series Noetherian theorem and these generating lists give the upper dimension bound, while the chains obtained by adjoining the variables successively, preceded by $(p)$ in the DVR case, give the matching lower bound. The coefficient construction's §6 records the formal power-series Noetherian input. Completeness follows by comparing coefficients modulo the powers of the displayed maximal ideal.

Finally $\phi$ is injective. Let $K=\ker\phi$. Finiteness makes $R$ integral over $A/K$, so dimension for integral extensions gives $\dim(A/K)=\dim R=\dim A$. If $K\ne0$, any chain of primes containing $K$ can be extended downward by the zero prime of the domain $A$. This would give $\dim(A/K)\leq\dim A-1$, a contradiction. Identify $R_0=A$ with its image. Its maximal ideal maps into $\mathfrak m$, and the coefficient map induces the prescribed residue-field isomorphism. ∎

#### Definition. Regular Noetherian rings

A Noetherian ring $R$ is **regular** when $R_{\mathfrak p}$ is a regular local ring for every prime $\mathfrak p\subset R$.

#### Lemma. Geometric regularity under separable algebraic extensions

Let $k'/k$ be algebraic and separable, with no finiteness assumption, and let $A$ be a $k'$-algebra. Then geometric regularity of $A$ over $k$ is equivalent to geometric regularity over $k'$.

**Proof.** Suppose $A$ is geometrically regular over $k'$, and take a finite purely inseparable extension $L/k$. Separability and pure inseparability are linearly disjoint, so $L'=k'\otimes_kL$ is a field, finite purely inseparable over $k'$. Thus

$$A\otimes_kL\cong A\otimes_{k'}L'$$

is regular. The purely inseparable test proves geometric regularity over $k$.

Conversely, suppose $A$ is geometrically regular over $k$. First take a finite intermediate extension $E/k$ in $k'/k$, and regard $A$ as an $E$-algebra. Base extension makes $A\otimes_kE$ geometrically regular over $E$. Multiplication gives

$$A\otimes_kE\longrightarrow A,\qquad a\otimes e\longmapsto ae.$$

This is the base change, along $E\to A$, of $E\otimes_kE\to E$. Since $E/k$ is finite separable, both $E\otimes_kE$ and $E$ are étale over $E$ (using the first factor on the source). The [permanence theorem for étale maps](#native-algebra-lemma-etale) makes this multiplication homomorphism étale. Its base change is therefore étale, and [ascent of geometric regularity](#native-algebra-lemma-geometrically-regular-goes-up) shows that $A$ is geometrically regular over $E$.

The finite intermediate extensions form a directed union equal to $k'$. Apply [geometric regularity over a directed union of subfields](#native-algebra-lemma-geometrically-regular-over-subfields). The finite purely inseparable tests there descend to one finite intermediate field, so geometric regularity over every such $E$ gives geometric regularity over $k'$. This treats an infinite separable algebraic extension without taking an unqualified limit of regular rings. ∎

#### Lemma. Regularity ascends along a regular ring map

If $R$ is a regular Noetherian ring and $R\to S$ is smooth, then $S$ is regular.

**Proof.** Finite presentation makes $S$ Noetherian. Fix $\mathfrak q\subset S$ and let $\mathfrak p$ be its contraction. Smoothness gives a flat local map $R_{\mathfrak p}\to S_{\mathfrak q}$. Its base is regular by assumption. Its closed fibre is a localization of the smooth $\kappa(\mathfrak p)$-algebra $S\otimes_R\kappa(\mathfrak p)$, and is regular by the smoothness criterion over a field. The already proved [regular-base and regular-fibre lemma](#native-algebra-lemma-flat-over-regular-with-regular-fibre) now makes $S_{\mathfrak q}$ regular. The prime was arbitrary, so $S$ is regular.

Equivalently, the [ascent criterion for $(R_k)$](#native-algebra-lemma-rk-goes-up) applies for every $k\geq0$: a smooth map is flat, and all its fibre local rings are regular. This is the same ascent argument expressed through the height-bounded regularity conditions. ∎

#### Lemma. Filtered limits and finite presentation

Every $R$-algebra $A$ is a directed colimit of finitely presented $R$-algebras. If $A$ is of finite type, the system can be chosen with all transition homomorphisms surjective.

**Proof by finite data.** For each finite subset $F\subset A$, form $R[X_a:a\in F]$ with its evaluation map to $A$. Choose any finite set $E$ of elements of its kernel, and put

$$A_{F,E}=R[X_a:a\in F]/(E).$$

Order the pairs by adjoining elements to $F$ and adjoining relations to $E$, viewing the old polynomial ring inside the new one. Any two pairs have an upper bound given by the unions of their variables and relations. Thus this is a directed partially ordered set of finitely presented algebras, with compatible maps to $A$.

The induced map from their colimit to $A$ is onto: an element $a\in A$ is represented by its variable at a stage containing $a$. It is injective because a polynomial representing zero in $A$ can itself be added as one further relation. If two representatives have the same image, first put them at a common stage and apply this argument to their difference. Hence the colimit is $A$.

If $A$ is generated by a fixed finite list, keep that list of variables and let $E$ run through the finite subsets of the kernel ideal of the resulting polynomial presentation. The same argument identifies the colimit, and every transition is a quotient map, hence surjective.

**Categorical proof.** The [category of finite presentations mapping to $A$](#native-algebra-lemma-ring-colimit-fp-category) is filtered and has colimit $A$. Replacing it by a cofinal directed system, as in the [directed-system replacement theorem](#uncovered-categories-lemma-directed-category-system), yields the first assertion. The finite-data construction above gives that directed system explicitly and also supplies the surjective-transition refinement. ∎

#### Lemma. Localization as a filtered colimit

For a multiplicative subset $U\subset R$ and an $R$-module $M$,

$$U^{-1}M\cong\mathop{\operatorname{colim}}_{f\in U}M_f.$$

Use the divisibility preorder: $f'\preceq f$ when $f=f'h$ for some $h\in R$. The transition homomorphism is

$$M_{f'}\longrightarrow M_f,\qquad
\frac{m}{(f')^e}\longmapsto\frac{h^em}{f^e}.$$

**Proof.** In $R_f$, the element $f'$ is a unit, with inverse $h/f$. Thus the universal property of localization defines the displayed map. It is independent of the chosen $h$ and respects compositions, because in each case it is the unique extension of $M\to M_f$ for which $f'$ becomes invertible. The product of two elements of $U$ is an upper bound, so the preorder is directed.

Every fraction $m/u\in U^{-1}M$ comes from $M_u$. If $m/f^e$ maps to zero, some $u\in U$ kills $m$. At the later stage $M_{fu}$, the element $u$ is invertible, so the representative is zero there. These two facts prove surjectivity and injectivity of the colimit map. They also cover $0\in U$, when the localization is zero. ∎

#### Lemma. The cotangent complex of a principal localization

Let $A\to B$ be a ring homomorphism and $P\twoheadrightarrow B$ a polynomial presentation with kernel $I$. Choose $f\in P$ mapping to $g\in B$. Extending the presentation by $x\mapsto g^{-1}$ gives

$$\beta:P[x]\twoheadrightarrow B_g,\qquad J=\ker\beta=(I,fx-1).$$

There are decompositions

$$J/J^2\cong (I/I^2)_g\oplus B_g[fx-1],$$

$$\Omega_{P[x]/A}\otimes_{P[x]}B_g
\cong (\Omega_{P/A}\otimes_PB_g)\oplus B_g\,dx,$$

and, after a change of basis in the second summand,

$$\mathrm{NL}(\beta)\cong
\bigl(\mathrm{NL}(P\to B)\otimes_BB_g\bigr)
\oplus\bigl(B_g\xrightarrow{\,g\,}B_g\bigr).$$

Consequently the canonical comparison $\mathrm{NL}_{B/A}\otimes_BB_g\to\mathrm{NL}_{B_g/A}$ is a homotopy equivalence.

**Proof.** The presentation of the localization as $B[x]/(gx-1)$ gives the formula for $J$. The conormal sequence for $P[x]\to B[x]\to B_g$ gives a right exact sequence

$$ (I/I^2)_g\longrightarrow J/J^2
\longrightarrow (gx-1)/(gx-1)^2\longrightarrow0.$$

The last module is free of rank one over $B_g$, with the displayed generator. To see this directly, $gx-1$ is a nonzerodivisor in $B[x]$: in an equality $(gx-1)\sum_{i=0}^n b_ix^i=0$, the constant coefficient gives $b_0=0$ and the successive coefficients give every $b_i=0$. Multiplication by $gx-1$ therefore identifies its ideal modulo its square with $B[x]/(gx-1)=B_g$.

The first arrow is injective. Map $P[x]$ to $(P/I^2)_f$ by $x\mapsto f^{-1}$. The ideal $J$ maps into the square-zero ideal $(I/I^2)_g$, and $J^2$ maps to zero. The resulting map $J/J^2\to(I/I^2)_g$ is a retraction of the first arrow. Lifting the generator on the right by $fx-1$ splits the sequence and gives the first decomposition. Polynomial differentials give the second decomposition directly.

To split the differential as well, retain the first differential summand and replace the other basis vector $dx$ by

$$e=dx+g^{-2}df.$$

In the tensor product with $B_g$, one has $x=g^{-1}$ and $f=g$, and hence

$$d(fx-1)=g^{-1}df+g\,dx=g e.$$

This proves the decomposition of complexes. The added complex is contractible, with contracting homotopy multiplication by $g^{-1}$. Finally, the complete comparison of polynomial presentations identifies this presentation map with the canonical comparison up to homotopy, proving the final assertion. The argument allows an arbitrary variable set in $P$. ∎

#### Lemma. Localization of a conormal module

Let $S$ be a finite type $R$-algebra and let $g\in S$. For presentations

$$\alpha:R[x_1,\ldots,x_n]\twoheadrightarrow S,\qquad
\beta:R[y_1,\ldots,y_m]\twoheadrightarrow S_g$$

with kernels $I$ and $J$, respectively, there is an isomorphism of $S_g$-modules

$$ (I/I^2)_g\oplus S_g^m\cong J/J^2\oplus S_g^n.$$

**Proof.** Adjoin an inverse variable to $\alpha$. The preceding lemma compares its localized cotangent complex by a homotopy equivalence to the complex of this enlarged presentation of $S_g$. The complete presentation-comparison theorem compares the latter to the complex of $\beta$. Thus the two complexes

$$[(I/I^2)_g\longrightarrow S_g^n],\qquad
[J/J^2\longrightarrow S_g^m]$$

are homotopy equivalent. The [two-term direct-sum lemma](#native-algebra-lemma-sum-two-terms) then identifies the first degree-one term plus the second degree-zero term with the second degree-one term plus the first degree-zero term. This is exactly the asserted isomorphism, and requires no projectivity assumption on either conormal module. ∎

#### Lemma. The conormal module of a global complete intersection

Let

$$S=R[x_1,\ldots,x_n]/(f_1,\ldots,f_c)$$

be a relative global complete intersection over an arbitrary ring $R$. Write $P=R[x_1,\ldots,x_n]$ and $I=(f_1,\ldots,f_c)$. For $\mathfrak q\in\operatorname{Spec}S$, let $\mathfrak q'$ be its inverse image in $P$. Then:

1. The displayed list $f_1,\ldots,f_c$ is a regular sequence in $P_{\mathfrak q'}$.
2. For every $0\leq i\leq c$, the ring $P_{\mathfrak q'}/(f_1,\ldots,f_i)$ is flat over $R$.
3. The classes of the $f_i$ give an $S$-basis of $I/I^2$.

**Proof over a Noetherian base.** Let $\mathfrak p=\mathfrak q'\cap R$. The fibre presentation has $n$ variables and $c$ equations and has dimension $n-c$. The height bound on its minimal primes makes every irreducible component have dimension at least $n-c$; the dimension of the whole fibre gives the reverse bound. Hence the dimension at every fibre point is $n-c$. Apply implication (2)$\Rightarrow$(5) of the [field complete-intersection criterion](#native-algebra-lemma-lci), together with its assertion for every generating list: the $c$ displayed equations form a regular sequence in the fibre local polynomial ring. This implication uses the Cohen–Macaulay parameter criterion and does not use the conormal conclusion being proved here.

The local polynomial ring $P_{\mathfrak q'}$ is flat over $R_{\mathfrak p}$. The complete successive slicing argument in *Faithful flatness and the local criterion for flatness*, §5 lifts the fibre regular sequence and proves flatness of each successive quotient over $R_{\mathfrak p}$. Localization of the base is flat, so these quotients are flat over $R$ as well. All local rings involved are Noetherian in this step, as required by that argument.

**Passage to an arbitrary base.** The [finite Noetherian-model lemma](#native-algebra-lemma-relative-global-complete-intersection-noetherian) gives a finite type $\mathbb Z$-subalgebra $R_0\subset R$ containing the equation coefficients for which the same presentation is already a relative global complete intersection. Consider the directed family of finite type $\mathbb Z$-subalgebras $R_\lambda\subset R$ containing $R_0$. Their union is $R$. Base change preserves the fibre-dimension condition, so the corresponding $S_\lambda$ are relative global complete intersections. Contract $\mathfrak q'$ to $\mathfrak q'_\lambda\subset R_\lambda[x]$ and put

$$T_{\lambda,i}=R_\lambda[x]_{\mathfrak q'_\lambda}/(f_1,\ldots,f_i).$$

At each stage, the Noetherian case proves $R_\lambda$-flatness of $T_{\lambda,i}$ and injectivity of multiplication by $f_{i+1}$ on it. There are natural identifications

$$\mathop{\operatorname{colim}}_\lambda T_{\lambda,i}
\cong P_{\mathfrak q'}/(f_1,\ldots,f_i).$$

Indeed, each polynomial coefficient and each inverted denominator occurs at a finite stage; a denominator outside $\mathfrak q'$ remains outside its contracted prime. Relations in these localized quotients also involve only finitely many coefficients and witnesses, so equality is detected at a later stage.

The [flatness theorem for a directed system of rings and modules](#native-algebra-lemma-colimit-rings-flat) makes each displayed colimit flat over $R$. Exactness of directed colimits preserves the injective multiplication maps. Since all the $f_i$ lie in $\mathfrak q'$, their successive ideals in the local ring are proper. This proves the regular-sequence assertion as well as (2), without imposing a Noetherian hypothesis on $R$.

**The conormal basis.** At a fixed $\mathfrak q$, the regular sequence just obtained gives a free conormal module with the indicated basis. One can check this without a flatness assumption on the conormal module. Relations among a regular sequence are generated by the Koszul relations: in $\sum a_if_i=0$, reduction modulo $(f_1,\ldots,f_{c-1})$ puts $a_c$ in that ideal; subtract the corresponding relations $f_ie_c-f_ce_i$ and apply induction to the first $c-1$ terms. Thus every coefficient of a relation belongs to $I$.

If $\sum a_if_i\in I^2$, subtract coefficients in $I$ to turn it into an exact relation. The preceding observation then gives every $a_i\in I$. It follows that $S_{\mathfrak q}^c\to(I/I^2)_{\mathfrak q}$ is injective as well as surjective. The global map $S^c\to I/I^2$ therefore has zero kernel and cokernel after localization at every prime; [local detection of zero modules](#native-algebra-lemma-characterize-zero-local) makes it an isomorphism. The empty regular sequence and the zero algebra are included. ∎

#### Definition. Relative global complete intersections

A homomorphism $R\to S$ is a **relative global complete intersection** if it has a finite presentation

$$S=R[x_1,\ldots,x_n]/(f_1,\ldots,f_c)$$

for which every nonempty fibre has dimension $n-c$. Referring to a displayed presentation as a relative global complete intersection means that this dimension condition holds for that presentation. Empty fibres impose no condition.

#### Lemma. An open neighbourhood with bounded fibre dimension

Let $R\to S$ be of finite type and let $\mathfrak q\in\operatorname{Spec}S$ have fibre dimension $n$ at that point. There is an open neighborhood $V$ of $\mathfrak q$ such that every $\mathfrak q'\in V$ has fibre dimension at most $n$.

**Proof.** The [polynomial-model lemma](#native-algebra-lemma-quasi-finite-over-polynomial-algebra) provides $g\notin\mathfrak q$ and a quasi-finite map $R[t_1,\ldots,t_n]\to S_g$. Set $V=D(g)$. After taking the fibre over any prime of $R$, this remains quasi-finite over a polynomial ring in $n$ variables over a field. The [dimension bound for a quasi-finite algebra over affine space](#native-algebra-lemma-dimension-quasi-finite-over-polynomial-algebra) bounds the whole nonempty fibre by $n$. Its dimension at each of its points is consequently at most $n$, which proves the assertion. ∎

#### Lemma. Base change of a global complete intersection

Suppose $S=R[x_1,\ldots,x_n]/(f_1,\ldots,f_c)$ is a relative global complete intersection.

1. For any $R\to R'$, the displayed base-change presentation of $S\otimes_RR'$ over $R'$ is a relative global complete intersection.
2. If $g\in S$ is represented by $h\in R[x]$, the presentation
   $$S_g\cong R[x_1,\ldots,x_n,z]/(f_1,\ldots,f_c,hz-1)$$
   is a relative global complete intersection over $R$.
3. If the structure map factors through $R_a$ for an element $a\in R$, then the same equations present a relative global complete intersection over $R_a$.

**Proof.** A fibre of the base-changed algebra is the extension of an original fibre by a field extension. The [field-extension dimension theorem](#native-algebra-lemma-dimension-preserved-field-extension) preserves its dimension, and a nonzero vector space stays nonzero on extending the ground field. This proves (1).

For (2), the displayed presentation is the usual presentation of a localization. Each of its fibres is a principal localization of an original fibre, so its dimension is at most $n-c$. If it is nonzero, the height bound for an ideal generated by $c+1$ elements in a polynomial ring in $n+1$ variables gives the reverse inequality

$$\dim\bigl(S_g\otimes_R\kappa(\mathfrak p)\bigr)
\geq (n+1)-(c+1)=n-c.$$

Thus every nonempty localized fibre has exactly the required dimension. Finally, the factorization in (3) makes $a$ invertible in $S$, giving $R_a\otimes_RS\cong S$. Apply (1) to this base change. ∎

#### Lemma. Locality of syntomic ring maps

Suppose $g_1,\ldots,g_m\in S$ generate the unit ideal and every $R\to S_{g_i}$ is syntomic. Then $R\to S$ is syntomic.

**Proof.** The opens $D(g_i)$ cover the target spectrum. Flatness is local on that spectrum, so the localized flatness assertions imply that $S$ is flat over $R$. Finite presentation glues across this finite principal cover by the [finite-presentation gluing lemma](#native-algebra-lemma-cover-upstairs). In every fibre, the same opens cover, and being a local complete intersection means precisely that each fibre local ring has that property. Each such local ring occurs in one of the syntomic charts. The three defining conditions—flatness, finite presentation and local complete-intersection fibres—therefore hold for $R\to S$. ∎

#### Lemma. Quasi-compactness of an affine spectrum

For every ring $R$, the space $\operatorname{Spec}R$ is quasi-compact.

**Proof.** Refine an open cover by basic opens $D(f_i)$. Their union is the spectrum exactly when no prime contains all the $f_i$. By [prime separation and the affine topology](#native-algebra-lemma-zariski-topology), this says that their generated ideal is $R$. An expression for $1$ in that ideal is a finite sum

$$1=\sum_{i\in F}r_if_i.$$

No prime can contain all the $f_i$ for $i\in F$, so these finitely many basic opens cover the spectrum. Selecting their containing members gives a finite subcover of the original cover. The empty spectrum of the zero ring satisfies the assertion as well. ∎

#### Lemma. Flatness of a cokernel

Let $\varphi:P_1\to P_2$ be a homomorphism of finite projective modules over $R$. Define subsets of $\operatorname{Spec}R$ by

$$U=\{\mathfrak p:\varphi\otimes_R\kappa(\mathfrak p)\text{ is injective}\},$$
$$W=\{\mathfrak p:\varphi\otimes_R\kappa(\mathfrak p)\text{ is surjective}\},
\qquad V=U\cap W.$$

All three are open. For any principal open $D(f)$ contained in $U$, the localized map $P_{1,f}\to P_{2,f}$ is injective with finite projective cokernel. For $D(f)\subset W$, it is surjective with finite projective kernel. For $D(f)\subset V$, it is an isomorphism.

**Proof.** Work on an open neighborhood where $P_1$ and $P_2$ are free of ranks $a$ and $b$, using the [finite-projectivity criteria](#native-algebra-lemma-finite-projective). If $a\leq b$, fibrewise injectivity means that some $a\times a$ minor of the matrix is nonzero in the residue field. The corresponding principal opens are precisely $U$ in this chart; if $a>b$, that locus is empty. Where one such minor is a unit, invertible row operations put the map in the form

$$R^a\longrightarrow R^a\oplus R^{b-a},\qquad v\longmapsto(v,0).$$

It is therefore injective and its cokernel is free there. This proves openness of $U$ and the local splitting assertion. If $D(f)\subset U$, local detection makes the kernel of $\varphi_f$ zero. The cokernel is finitely presented and locally free by these charts, hence finite projective by the same projectivity criteria. This proves the entire assertion over $R_f$.

For surjectivity interchange the role of the two ranks in the maximal-minor test: when $a\geq b$, the nonvanishing $b\times b$ minors define $W$. Where such a minor is invertible, the matrix is a split surjection. Thus $W$ is open, and if $D(f)\subset W$, the cokernel of $\varphi_f$ vanishes at every prime of $R_f$, hence vanishes. Projectivity of $P_{2,f}$ supplies a global section over $R_f$. The kernel is then a direct summand of the finite projective module $P_{1,f}$, so is finite projective. This also gives the surjectivity proof through the vanishing locus of the finite cokernel.

The isomorphism locus is $V=U\cap W$. On a principal open contained in it, the two conclusions give injectivity and surjectivity. The rank-zero cases use the determinant of the empty matrix, which is $1$, and fit all the same assertions. ∎

#### Lemma. Criteria for global complete intersections

Every relative global complete-intersection homomorphism is syntomic; in particular, it is flat.

**Proof.** Its presentation is finite, and each nonempty fibre is a global complete intersection over the residue field, hence has complete-intersection local rings. The [conormal and successive-flatness lemma](#native-algebra-lemma-relative-global-complete-intersection-conormal), with $i=c$, makes $S_{\mathfrak q}$ flat over $R$ for every prime $\mathfrak q$ of $S$. Flatness can be checked at these localizations, so $S$ is flat over $R$. These are exactly the three syntomic conditions. The zero algebra is also flat and finitely presented, with no fibre local rings to check. ∎

#### Definition. Complete-intersection local rings

Let $k$ be a field and let $S$ be a local $k$-algebra essentially of finite type. It is a **complete intersection over $k$** if it admits a presentation

$$S\cong T/(f_1,\ldots,f_c)$$

as a $k$-algebra, where $T$ is a regular local $k$-algebra essentially of finite type, and $f_1,\ldots,f_c$ is a regular sequence contained in the maximal ideal of $T$. The empty sequence is allowed, in which case the presenting ring itself is $S$.

#### Lemma. Complete intersections at a prime ideal

Let $S$ be a finite type algebra over a field $k$, and let $\mathfrak q\subset S$ be prime. The following four conditions are equivalent:

1. The local $k$-algebra $S_{\mathfrak q}$ is a complete intersection.
2. Some $g\in S\setminus\mathfrak q$ makes $S_g$ a local complete intersection over $k$.
3. Some $g\in S\setminus\mathfrak q$ makes $S_g$ a global complete intersection over $k$.
4. For every polynomial presentation $S=k[x_1,\ldots,x_n]/I$, with inverse-image prime $\mathfrak q'$, the five equivalent tests in the [local complete-intersection criterion](#native-algebra-lemma-lci) hold at $\mathfrak q$.

**Proof.** Start with (1). The intrinsic [locality and presentation-independence theorem](#native-algebra-lemma-lci-local), condition (2), says that the kernel of any surjection from a regular local $k$-algebra essentially of finite presentation to $S_{\mathfrak q}$ is generated by a regular sequence. Apply this to $k[x]_{\mathfrak q'}\to S_{\mathfrak q}$ for any chosen polynomial presentation. This gives condition (5) of the five-test criterion, hence all its conditions. Thus (1) implies (4).

Condition (4), applied to one presentation, gives a global complete-intersection principal neighborhood by condition (1) of that same criterion. Hence (4) implies (3). Every global complete intersection is locally a complete intersection, so (3) implies (2). Finally, localizing the neighborhood in (2) at its point $\mathfrak q$ gives the complete-intersection local ring in (1). The final step also follows directly from conditions (5) and (1) of the intrinsic locality theorem. ∎

#### Lemma. Tor vanishing for a flat module

Let $0\to M''\xrightarrow{i}M'\xrightarrow{p}M\to0$ be exact over a ring $R$, and assume $M$ is flat. For every $R$-module $N$, tensoring gives an exact sequence

$$0\longrightarrow N\otimes_RM''\longrightarrow N\otimes_RM'
\longrightarrow N\otimes_RM\longrightarrow0.$$

No finiteness hypothesis is imposed on any of the modules.

**Proof.** Tensor products are right exact, so only the first injection needs proof. Choose a free module $F$ surjecting onto $N$, with kernel $K$. Given $z\in M''\otimes_RN$ mapping to zero, lift it to $\widetilde z\in M''\otimes_RF$. Its image in $M'\otimes_RF$ comes from an element $y\in M'\otimes_RK$, because it becomes zero after passing to $N$.

The image of $y$ in $M\otimes_RK$ maps to zero in $M\otimes_RF$: it agrees there with the image of $\widetilde z$, which is zero after applying $p$. Flatness of $M$ makes $M\otimes_RK\to M\otimes_RF$ injective. Therefore $y$ has zero image in $M\otimes_RK$. By right exactness there is $w\in M''\otimes_RK$ mapping to $y$.

In $M''\otimes_RF$, the difference between $\widetilde z$ and the image of $w$ becomes zero in $M'\otimes_RF$. Tensoring with the free module $F$ preserves the injection $i$, so that difference is zero. Passing to $M''\otimes_RN$ kills the image of $w$, and gives $z=0$. This is the free-presentation diagram chase; it remains valid for an infinite free basis. ∎

#### Lemma. Smoothness of a global complete intersection

Suppose $S=R[x_1,\ldots,x_n]/(f_1,\ldots,f_c)$ is a relative global complete intersection and $\mathfrak q$ is a prime of $S$. Then $R\to S$ is smooth at $\mathfrak q$ exactly when one of the $c\times c$ Jacobian minors

$$\Delta_E=\det\left(\frac{\partial f_j}{\partial x_i}\right)_{
1\leq j\leq c,\ i\in E},\qquad E\subset\{1,\ldots,n\},\quad |E|=c,$$

has image outside $\mathfrak q$. Order $E$ increasingly to fix the displayed determinant.

**Proof.** The [conormal-basis lemma](#native-algebra-lemma-relative-global-complete-intersection-conormal) identifies the presentation complex with

$$S^c\longrightarrow S^n,\qquad
e_j\longmapsto\sum_{i=1}^n\frac{\partial f_j}{\partial x_i}\,dx_i.$$

If the image of $\Delta_E$ is $g\notin\mathfrak q$, elementary row operations over $S_g$ split this map as the inclusion of a free rank-$c$ summand. Its kernel is zero and its cokernel is free of rank $n-c$. The [principal-localization comparison](#native-algebra-lemma-principal-localization-nl) identifies this localized complex, up to homotopy, with the cotangent complex of the finite presentation of $S_g$ obtained by adjoining an inverse variable. The cotangent criterion for smoothness therefore makes $S_g$ smooth over $R$.

Conversely, smoothness on a neighborhood of $\mathfrak q$ makes the presentation's conormal map a split injection there. This follows from the smooth cotangent sequence: its kernel vanishes and its differential cokernel is projective. Tensor the splitting with $\kappa(\mathfrak q)$. The resulting matrix has rank $c$, so at least one of the displayed minors is nonzero in that field. Its image in $S$ is consequently outside $\mathfrak q$. When $c=0$, the empty minor is $1$ and the polynomial presentation is smooth. ∎

#### Lemma. Dimension and codimension

For a surjection $S'\twoheadrightarrow S$ of finite type algebras over a field $k$, let $\mathfrak p'\subset S'$ correspond to $\mathfrak p\subset S$. Write $x',x$ for the associated points of $X'=\operatorname{Spec}S'$ and $X=\operatorname{Spec}S$. Then

$$\dim_{x'}X'-\dim_xX
=\operatorname{ht}(\mathfrak p')-\operatorname{ht}(\mathfrak p).$$

**Proof.** The surjection identifies $\kappa(\mathfrak p')$ with $\kappa(\mathfrak p)$. The [dimension formula at a point of a finite type algebra over a field](#native-algebra-lemma-dimension-at-a-point-finite-type-field) gives

$$\dim_{x'}X'=\operatorname{ht}(\mathfrak p')+
\operatorname{trdeg}_k\kappa(\mathfrak p'),\qquad
\dim_xX=\operatorname{ht}(\mathfrak p)+\operatorname{trdeg}_k\kappa(\mathfrak p).$$

Subtract these finite integers. The residue-field terms cancel, yielding the assertion. Here dimension at a point is the minimum dimension of its open neighborhoods, as in that formula. ∎

#### Lemma. Complete intersections are Cohen–Macaulay

A finite type $k$-algebra which is a local complete intersection is a Cohen–Macaulay ring.

**Proof.** At any prime, choose a complete-intersection chart. The local ring is a quotient of a regular local polynomial ring by a regular sequence, by the [global conormal and regular-sequence lemma](#native-algebra-lemma-relative-global-complete-intersection-conormal). A regular local ring is Cohen–Macaulay, and a quotient by a regular sequence remains Cohen–Macaulay. Complete proofs of both assertions are *Regular sequences, depth and Cohen–Macaulay modules*, Theorem 6.1 and Corollary 6.2. Thus every prime localization is Cohen–Macaulay, as required.

The dimension calculation at maximal ideals gives the original alternative route. On a chart $S=k[x_1,\ldots,x_n]/(f_1,\ldots,f_c)$ of dimension $n-c$, let $\mathfrak m'$ be the inverse image of a maximal ideal $\mathfrak m$. The regular local ring $k[x]_{\mathfrak m'}$ has dimension $n$. Quotienting by the $c$ equations lowers dimension by at most $c$, whereas $\dim S=n-c$ bounds $\dim S_{\mathfrak m}$ above. Hence $\dim S_{\mathfrak m}=n-c$. The expected-dimension criterion of §4 of the cited lesson makes the equations regular and the quotient Cohen–Macaulay. Localization of Cohen–Macaulay local rings, proved in its §5, gives the result at all primes. ∎

#### Proposition. Characterizations of Cohen–Macaulay modules

Let $(R,\mathfrak m)$ be Noetherian local and let $M$ be a nonzero finite Cohen–Macaulay $R$-module with support dimension $d$. If $g_1,\ldots,g_c\in\mathfrak m$ satisfy

$$\dim\operatorname{Supp}\bigl(M/(g_1,\ldots,g_c)M\bigr)=d-c,$$

then the displayed list is $M$-regular and extends to a maximal $M$-regular sequence.

**Proof.** The full module argument is *Regular sequences, depth and Cohen–Macaulay modules*, Theorem 4.2 and Corollary 4.3. Its support and depth inputs are proved in §§2–3. Each successive quotient here is nonzero by Nakayama. One equation lowers support dimension by at most one, so the total drop of $c$ forces a drop of exactly one at each step.

For a Cohen–Macaulay module, every associated component has the full support dimension. An element causing a one-dimensional drop cannot lie in an associated prime: otherwise that entire component would remain in the quotient support. It is therefore a nonzerodivisor. Both depth and support dimension drop by one, leaving a Cohen–Macaulay quotient. Repeating this argument proves regularity of the whole list.

The final quotient is Cohen–Macaulay of dimension $d-c$. Choose a system of parameters for its support and lift it to $\mathfrak m$. Corollary 4.3 proves that these parameters are regular on the quotient, so appending them gives a regular sequence on $M$ of length $d$. No longer regular sequence is possible because depth is bounded by support dimension. This proves the stated extension to a maximal sequence, including the case $c=d$ when nothing is appended. ∎

#### Lemma. Regular sequences are quasi-regular

Let $R$ be any ring.

1. Every regular sequence in $R$ is quasi-regular.
2. More generally, an $M$-regular sequence is $M$-quasi-regular for any $R$-module $M$.

Explicitly, if the list is $f_1,\ldots,f_c$ and $J=(f_1,\ldots,f_c)$, the canonical graded map

$$ (M/JM)[T_1,\ldots,T_c]\longrightarrow
\bigoplus_{n\geq0}J^nM/J^{n+1}M,\qquad
[m]T^I\longmapsto[mf^I]$$

is an isomorphism. No Noetherian or finite-generation hypothesis is needed.

**Proof.** Prove the module statement; taking $M=R$ then gives (1). The graded map is surjective by the definition of an ideal power. In degree $n$, injectivity means that

$$\sum_{|I|=n}m_If^I\in J^{n+1}M
\quad\Longrightarrow\quad m_I\in JM\text{ for every }I.$$

Every element of $J^{n+1}M$ can be expressed in the same degree-$n$ monomials with coefficients in $JM$. Subtracting such coefficients reduces the problem to a relation whose sum is exactly zero.

Induct on the length $c$. For $c=0$, the map is the identity in degree zero and both sides vanish in positive degrees. Suppose the assertion is known for the first $c-1$ elements, and put $J'=(f_1,\ldots,f_{c-1})$. For a fixed degree $n$, write a relation as

$$\sum_{e=0}^{l}\left(\sum_{|I'|=n-e}m_{I',e}f^{I'}\right)f_c^e=0,$$

where $I'$ ranges over the first $c-1$ variables and initially $l=n$. We show by a second induction on $l$ that all its coefficients belong to $JM$. For $l=0$, this is the induction hypothesis for $J'$.

For $l>0$, all terms with $e<l$ belong to $(J')^{n-l+1}M$. Consequently

$$\sum_{|I'|=n-l}(f_c^lm_{I',l})f^{I'}
\in(J')^{n-l+1}M.$$

The first induction gives $f_c^lm_{I',l}\in J'M$ for each top coefficient. Multiplication by $f_c$ is injective on $M/J'M$, because the given list is regular. Hence $m_{I',l}\in J'M$. Write these coefficients as sums $\sum_{j<c}f_jb_{j,I'}$. Substitution absorbs the entire term with exponent $l$ into the terms with exponent $l-1$: their degree in the first variables increases by one and their coefficients acquire a factor $f_c$.

We now have a relation of the same total degree with largest exponent at most $l-1$. By the second induction its coefficients lie in $JM$. Those coefficients differ from the old ones only by multiples of $f_c$, which also lie in $JM$. Thus every old coefficient with $e<l$ lies in $JM$, and the top ones already lie in $J'M\subset JM$. This completes both inductions and proves the graded isomorphism. The argument applies verbatim to arbitrary module coefficients and includes degree zero. ∎

#### Lemma. Maximal prime chains in a Cohen–Macaulay ring

If $R$ is a Noetherian Cohen–Macaulay local ring of dimension $d$, every maximal chain of prime ideals has length $d$.

**Proof.** The complete localization and dimension argument is *Regular sequences, depth and Cohen–Macaulay modules*, §5, especially Lemma 5.4. Write a maximal chain as

$$\mathfrak p_0\subsetneq\mathfrak p_1\subsetneq\cdots
\subsetneq\mathfrak p_r.$$

It starts at a minimal prime and ends at the maximal ideal, since otherwise it could be extended. Each adjacent pair is saturated. The local ring $R_{\mathfrak p_{i+1}}$ is Cohen–Macaulay, and its quotient by $\mathfrak p_iR_{\mathfrak p_{i+1}}$ has dimension one: saturation leaves just the two endpoints in that prime interval. Lemma 5.4 applied in this local ring yields

$$\dim R_{\mathfrak p_{i+1}}-\dim R_{\mathfrak p_i}=1.$$

The dimensions telescope from $\dim R_{\mathfrak p_0}=0$ to $\dim R_{\mathfrak p_r}=d$, giving $r=d$. All chains are finite, since their lengths are bounded by the finite dimension of the Noetherian local ring. This supplies the stated consequence of the more general [maximal-chain theorem for Cohen–Macaulay modules](#native-algebra-lemma-maximal-chain-maximal-cm). ∎

#### Lemma. An elementary algebraic comparison (Prime avoidance)

Let $J,I_1,\ldots,I_r$ be ideals of a ring $R$. Suppose $J$ is contained in none of the $I_i$, and at most two of the $I_i$ fail to be prime. Then some $x\in J$ belongs to none of the $I_i$.

Consequently, if an open subset of an affine scheme contains finitely many specified points, a principal open contains those points and is contained in that open subset. In particular, affine open neighborhoods are cofinal among neighborhoods of a finite set in an affine scheme.

**Proof.** For no ideals there is nothing to avoid. For one ideal use the assumption. For two ideals choose $a\in J\setminus I_1$ and $b\in J\setminus I_2$. Unless one of these already avoids both, one has $a\in I_2$ and $b\in I_1$; then $a+b$ avoids both, by subtracting the summand already in the ideal.

Proceed by induction on $r$. Delete any ideal contained in another ideal on the list: avoiding the larger ideal automatically avoids the smaller one. If this shortens the list, induction applies. Otherwise the ideals are pairwise incomparable. When $r\geq3$, at least one is prime; number such an ideal last, as $I_r$. Induction supplies $a\in J$ avoiding $I_1,\ldots,I_{r-1}$. If $a\notin I_r$, it is the required element.

If $a\in I_r$, choose $b_0\in J\setminus I_r$ and $b_i\in I_i\setminus I_r$ for $1\leq i<r$, using incomparability. Primality makes $b=b_0b_1\cdots b_{r-1}$ lie outside $I_r$. It lies in $J$ and in every earlier $I_i$. Thus $a+b$ avoids the earlier ideals because $a$ does, and avoids $I_r$ because $b$ does. This proves the assertion with the two possible nonprime exceptions intact.

For the geometric consequence, write the complement of the given open $U\subset\operatorname{Spec}R$ as $V(J)$. If the specified primes are $\mathfrak p_1,\ldots,\mathfrak p_s$, containment in $U$ means $J\not\subset\mathfrak p_i$ for each $i$. Apply the assertion to choose $f\in J$ outside every $\mathfrak p_i$. Then

$$\{\mathfrak p_1,\ldots,\mathfrak p_s\}\subset D(f)\subset U.$$

The open $D(f)$ is affine, giving the second formulation. For an empty specified set one may use the empty principal open $D(0)$. ∎

#### Lemma. Equivalent Cohen–Macaulay conditions

Let $(R,\mathfrak m)$ be a Noetherian Cohen–Macaulay local ring of dimension $d$. For $x_1,\ldots,x_c\in\mathfrak m$,

$$x_1,\ldots,x_c\text{ is regular}
\quad\Longleftrightarrow\quad
\dim R/(x_1,\ldots,x_c)=d-c.$$

Under these conditions the list extends to a regular sequence of length $d$, and every intermediate quotient $R/(x_1,\ldots,x_i)$ is Cohen–Macaulay of dimension $d-i$.

**Proof.** Apply the preceding [module support-dimension criterion](#native-algebra-proposition-cm-module) to $M=R$. It proves the reverse implication and the extension to length $d$. In the forward direction, each nonzerodivisor in the maximal ideal lowers both dimension and depth by exactly one; its quotient is therefore again Cohen–Macaulay. Iteration gives all the stated intermediate dimensions and the final equality. These depth and dimension assertions are proved in the full CM-module argument cited in that proposition. ∎

#### Lemma. The rank of Kähler differentials

Let $S$ be of finite type over an algebraically closed field $k$, and let $\mathfrak m\subset S$ be maximal. Then

$$\dim_{\kappa(\mathfrak m)}\bigl(\Omega_{S/k}\otimes_S\kappa(\mathfrak m)\bigr)
=\dim_{\kappa(\mathfrak m)}\mathfrak m/\mathfrak m^2.$$

**Proof.** The Nullstellensatz identifies the residue field with $k$, so the residue map $\epsilon:S\to k$ is a $k$-algebra retraction of the structure map. The exact cotangent calculation is *Smooth algebras over a field and the Jacobian criterion*, Proposition 3.1.

Explicitly, the usual conormal map sends $a\bmod\mathfrak m^2$ to $da\otimes1$. An inverse is induced by the $k$-derivation

$$D:S\longrightarrow\mathfrak m/\mathfrak m^2,
\qquad D(s)=s-\epsilon(s)\pmod{\mathfrak m^2}.$$

The target has $S$-action through $\epsilon$. The product rule follows on expanding $st$ and discarding the product of $s-\epsilon(s)$ and $t-\epsilon(t)$, which lies in $\mathfrak m^2$. This derivation factors through $\Omega_{S/k}\otimes_Sk$. The two maps are inverse because $D(a)=a$ for $a\in\mathfrak m$, while $d(s-\epsilon(s))=ds$. Thus the vector spaces themselves are canonically isomorphic, proving the equality. This also exhibits the left exactness supplied by the split residue map in the conormal sequence. ∎

#### Definition. Regular local rings

Let $(R,\mathfrak m)$ be Noetherian local of dimension $d$. A **system of parameters** is a list $x_1,\ldots,x_d\in\mathfrak m$ whose ideal has radical $\mathfrak m$, equivalently an ideal of definition. The ring is **regular local** if its maximal ideal can be generated by $d$ elements. Any such generating list is called a **regular system of parameters**. The empty list is permitted when $d=0$.

#### Lemma. Essentially finite presentations in a filtered limit

Let $R\to S$ be a local homomorphism of local rings, essentially of finite presentation. There is a directed system of local homomorphisms $R_\lambda\to S_\lambda$ with the following properties:

1. Its colimit is the given map $R\to S$.
2. The source homomorphism $\mathbb Z\to R_\lambda$ is essentially of finite type.
3. The target $S_\lambda$ is a localization of a finite type $R_\lambda$-algebra.
4. For $\lambda\leq\mu$, the map
   $$S_\lambda\otimes_{R_\lambda}R_\mu\longrightarrow S_\mu$$
   identifies $S_\mu$ with localization at a prime of its source.

**Proof.** Write $S=B_{\mathfrak q}$ with

$$B=R[x_1,\ldots,x_n]/(f_1,\ldots,f_m).$$

Such a prime localization can be used because $S$ is local: any local localization of a ring equals localization at the inverse image of its maximal ideal. Locality of $R\to S$ makes $\mathfrak q$ contract to the maximal ideal $\mathfrak m$ of $R$.

For every finite type $\mathbb Z$-subalgebra $A_\lambda\subset R$, put

$$R_\lambda=(A_\lambda)_{A_\lambda\cap\mathfrak m}.$$

These are local subrings of $R$, since all denominators are units in $R$. They form a directed system under inclusion, have local transition maps, and have union $R$. Restrict to the cofinal family containing the finitely many coefficients of all the $f_j$. Define $B_\lambda$ by the same polynomial presentation over $R_\lambda$, let $\mathfrak q_\lambda$ be the inverse image of the maximal ideal of $S$ under $B_\lambda\to S$, and set

$$S_\lambda=(B_\lambda)_{\mathfrak q_\lambda}.$$

The contraction of $\mathfrak q_\lambda$ to $R_\lambda$ is its maximal ideal, so $R_\lambda\to S_\lambda$ is local. Contractions of the fixed maximal ideal of $S$ also make all transition maps local.

The colimit is $S$: every coefficient and every denominator of an element of $B_{\mathfrak q}$ occurs at a finite stage, and any equality between two fractions has a polynomial relation and a denominator witness at a later stage. For $\lambda\leq\mu$, one has $B_\lambda\otimes_{R_\lambda}R_\mu=B_\mu$. Tensoring $S_\lambda$ first inverts the images of $B_\lambda\setminus\mathfrak q_\lambda$. These images avoid $\mathfrak q_\mu$. Localizing the resulting ring at the prime induced by $\mathfrak q_\mu$ inverts all of $B_\mu\setminus\mathfrak q_\mu$ and gives exactly $S_\mu$. This proves (4). The displayed finite presentations and localizations prove (2) and (3). ∎

#### Lemma. Eventual flatness in a filtered colimit

Use a system $R_\lambda\to S_\lambda$, $M_\lambda$ with the six properties of the module-model lemma below, with colimit $R\to S$, $M$. If $M$ is flat over $R$, then $M_\mu$ is flat over $R_\mu$ at some stage $\mu$.

**Proof.** Fix a stage $\lambda$ and let $\mathfrak m_\lambda$ be the maximal ideal of $R_\lambda$. Both rings at this stage are Noetherian. The module

$$T_\lambda=\operatorname{Tor}_1^{R_\lambda}
(M_\lambda,R_\lambda/\mathfrak m_\lambda)
=\ker(\mathfrak m_\lambda\otimes_{R_\lambda}M_\lambda\to M_\lambda)$$

is finite over $S_\lambda$: the ideal $\mathfrak m_\lambda$ is finite, $M_\lambda$ is finite over $S_\lambda$, and a submodule of a finite module over the Noetherian ring $S_\lambda$ is finite. Choose generators $\xi_1,\ldots,\xi_a$.

Flatness of $M$ gives injectivity of

$$\mathfrak m_\lambda R\otimes_RM\longrightarrow M.$$

For $\mu\geq\lambda$, the ideals $\mathfrak m_\lambda R_\mu$ and modules $M_\mu$ form directed systems whose tensor products have this source as their colimit. Each $\xi_i$ therefore becomes zero in $\mathfrak m_\lambda R_\mu\otimes_{R_\mu}M_\mu$ at some later stage. Choose one common stage $\mu$ for the finite list. The natural map

$$T_\lambda\longrightarrow
\operatorname{Tor}_1^{R_\mu}(M_\mu,R_\mu/\mathfrak m_\lambda R_\mu)$$

is then zero.

The [change-of-base local flatness lemma](#native-algebra-lemma-another-variant-local-criterion-flatness) now applies. Its ideal is $\mathfrak m_\lambda$, its base change is $R_\lambda\to R_\mu$, and its localized tensor-product algebra is $S_\mu$. Its quotient-flatness hypothesis holds because $M_\lambda/\mathfrak m_\lambda M_\lambda$ is a vector space over the field $R_\lambda/\mathfrak m_\lambda$. Its Tor-map hypothesis is the vanishing just arranged. All maps are local, so the extended ideal is proper. The conclusion is flatness of $M_\mu$ over $R_\mu$.

For completeness, the Tor-surjectivity step in that criterion can be seen with free presentations. Write $0\to K\to F\to N\to0$, with $F$ free over a base ring $A$, and suppose $N/JN$ is flat over $A/J$. Modulo $J$, put $L=\operatorname{im}(K/JK\to F/JF)$ and $T=\operatorname{Tor}_1^A(N,A/J)$. The quotient in $0\to L\to F/JF\to N/JN\to0$ is flat, so this sequence remains injective on the left after tensoring with any $A/J$-module $Q$. Right exactness of tensoring $T\to K/JK\to L\to0$ consequently gives a surjection

$$T\otimes_{A/J}Q\twoheadrightarrow\operatorname{Tor}_1^A(N,Q).$$

For a ring map $A\to A'$ and an $A'$-module $Q$, the kernel of $F\otimes_AA'\to N\otimes_AA'$ is the image of $K\otimes_AA'$. Tensoring that surjection with $Q$ shows that every element of $\operatorname{Tor}_1^{A'}(N\otimes_AA',Q)$ lifts to the kernel of $K\otimes_AQ\to F\otimes_AQ$. Thus there is also a surjection

$$\operatorname{Tor}_1^A(N,Q)\twoheadrightarrow
\operatorname{Tor}_1^{A'}(N\otimes_AA',Q).$$

Take $Q=A'/JA'$ and then localize in the tensor-product algebra. These surjections show that a zero map from the old Tor module forces the new Tor module to vanish. Quotient flatness survives this base change and localization, so the [ideal form of the local flatness criterion](#native-algebra-lemma-variant-local-criterion-flatness) completes the argument. This supplies the transport step without assuming that $A\to A'$ is flat. ∎

#### Lemma. Essentially finitely presented module models

Let $R\to S$ be a local homomorphism of local rings, with $S$ essentially of finite presentation over $R$, and let $M$ be finitely presented over $S$. There is a directed system $R_\lambda\to S_\lambda$, $M_\lambda$ such that:

1. The ring-map colimit is $R\to S$ and the module colimit is $M$.
2. Each local ring $R_\lambda$ is essentially of finite type over $\mathbb Z$.
3. Each local ring $S_\lambda$ is essentially of finite type over $R_\lambda$.
4. The module $M_\lambda$ is finite over $S_\lambda$.
5. Each $S_\lambda\otimes_{R_\lambda}R_\mu\to S_\mu$ is localization at a prime.
6. The canonical map $M_\lambda\otimes_{S_\lambda}S_\mu\to M_\mu$ is an isomorphism whenever $\lambda\leq\mu$.

**Proof.** Use the ring system constructed in the preceding finite-presentation lemma. Choose a finite matrix presentation

$$S^a\xrightarrow{H}S^b\longrightarrow M\longrightarrow0.$$

Its finitely many entries lift to a common $S_{\lambda_0}$. Restrict to stages $\lambda\geq\lambda_0$, let $H_\lambda$ be the image of that lifted matrix, and define

$$M_\lambda=\operatorname{coker}(S_\lambda^a\xrightarrow{H_\lambda}S_\lambda^b).$$

The ring conclusions were proved in that lemma and survive passage to this cofinal tail. These module presentations are finite, proving (4). Right exactness of tensor products identifies their base changes with the cokernels of the same matrices over $S_\mu$, proving (6), without requiring flat transition maps. Directed colimits commute with the finite free modules and their cokernels, so their module colimit is the cokernel of $H$, namely $M$. This proves (1) and all six assertions. ∎

#### Lemma. The Noetherian fibrewise criterion for flatness (Critère de platitude par fibres; Noetherian case)

Let $R\to S\to S'$ be local homomorphisms of Noetherian local rings. Denote the maximal ideal of $R$ by $\mathfrak m$. Suppose $M$ is a nonzero finite $S'$-module, is flat over $R$, and has $M/\mathfrak mM$ flat over $S/\mathfrak mS$. Then $M$ is flat over $S$, and $S$ is flat over $R$.

**Proof.** This is the forward implication of the complete *Faithful flatness and the local criterion for flatness*, Theorem 5.4. Its finiteness hypothesis is over $S'$, exactly as here.

To track the two flatness conclusions, put $I=\mathfrak mS$. The canonical map $\mathfrak m\otimes_RM\to I\otimes_SM$ is surjective. Its composite with multiplication into $M$ is injective by $R$-flatness. Thus the first map is an isomorphism and $I\otimes_SM\to M$ is injective. Equivalently, $\operatorname{Tor}_1^S(M,S/I)=0$. The assumed flatness modulo $I$ and the local ideal criterion give $S$-flatness of $M$.

This flat module is faithful over the local ring $S$. If $\mathfrak n'$ is the maximal ideal of $S'$, Nakayama gives $M/\mathfrak n'M\ne0$. It is a quotient of $M/\mathfrak nM$, where $\mathfrak n$ is the maximal ideal of $S$. Hence the latter quotient is nonzero, which is the local faithful-flatness criterion.

A Tor argument now proves flatness of $S$ over $R$. Tensor the exact sequence

$$0\longrightarrow\operatorname{Tor}_1^R(R/\mathfrak m,S)
\longrightarrow\mathfrak m\otimes_RS\longrightarrow I\longrightarrow0$$

over $S$ with the flat module $M$. The resulting map $\mathfrak m\otimes_RM\to I\otimes_SM$ is the isomorphism already proved, so

$$\operatorname{Tor}_1^R(R/\mathfrak m,S)\otimes_SM=0.$$

Faithfulness gives zero for this Tor module itself. The Noetherian local flatness criterion applied to $R\to S$ and the finite $S$-module $S$ makes $S$ flat over $R$.

Equivalently, the proof of Theorem 5.4 descends preservation of injections: tensor any injection of $R$-modules first with $S$, then with $M$. The second tensor is injective by $R$-flatness of $M$, and faithful $S$-flatness reflects that injection. Both routes give the same base-flatness conclusion. ∎

#### Lemma. An isolated point of a fibre

Let $R\to S$ be of finite type and let $\mathfrak q\subset S$ lie above $\mathfrak p\subset R$. Put $B=S\otimes_R\kappa(\mathfrak p)$, write $F=\operatorname{Spec}B$, and let $\bar{\mathfrak q}$ be its point corresponding to $\mathfrak q$. These six conditions are equivalent:

1. The singleton $\{\bar{\mathfrak q}\}$ is open in $F$.
2. The algebra $S_{\mathfrak q}/\mathfrak pS_{\mathfrak q}$ is finite-dimensional over $\kappa(\mathfrak p)$.
3. There exists $g\in S\setminus\mathfrak q$ such that $\mathfrak q$ is the only prime in $D(g)$ lying above $\mathfrak p$.
4. The dimension of $F$ at $\bar{\mathfrak q}$ is zero.
5. The point $\bar{\mathfrak q}$ is closed in $F$ and $\dim(S_{\mathfrak q}/\mathfrak pS_{\mathfrak q})=0$.
6. The residue extension $\kappa(\mathfrak q)/\kappa(\mathfrak p)$ is finite and $\dim(S_{\mathfrak q}/\mathfrak pS_{\mathfrak q})=0$.

**Proof.** There is a canonical identification

$$S_{\mathfrak q}/\mathfrak pS_{\mathfrak q}=B_{\bar{\mathfrak q}},$$

and $B$ is a finite type algebra over the field $\kappa(\mathfrak p)$. Thus these are the six tests of the [isolated-point lemma for affine spectra](#native-algebra-lemma-isolated-point). The following details also verify the principal-open statement in the original algebra $S$.

A basic open of the fibre can be defined by an element represented as $s/r$, with $s\in S$ and $r\in R\setminus\mathfrak p$. Since $r$ is a unit on the fibre, this basic open is the intersection of $F$ with $D(s)$. Basic opens are a basis, so (1) and (3) are equivalent. Either gives an open neighborhood with just one point, proving (4).

Conversely, (4) gives a basic neighborhood of dimension zero. Its coordinate ring is Noetherian and zero-dimensional, hence Artinian by *Noetherian and Artinian rings*, Theorem 4.2. Its spectrum is finite and discrete, so the specified point is isolated. This proves (4)$\Rightarrow$(1).

Under (3), the localized fibre ring has one prime and is Artinian local. It equals $B_{\bar{\mathfrak q}}$ and has finite length. Its residue field is finite over $\kappa(\mathfrak p)$ by the Nullstellensatz, since this principal localization is still of finite type. A composition series therefore makes it finite-dimensional over the ground field. Thus (3) implies (2), and (2) immediately implies (6).

The Nullstellensatz identifies closed points of $\operatorname{Spec}B$ with primes having finite residue field over the ground field, so (5) and (6) are equivalent. Under (5), the prime $\bar{\mathfrak q}$ is also minimal, because its local ring has dimension zero. The Noetherian ring $B$ has finitely many minimal primes. For each other minimal prime choose an element in it but outside $\bar{\mathfrak q}$, and multiply the choices. The resulting element avoids $\bar{\mathfrak q}$ and its basic open misses all other irreducible components. The remaining component is $V(\bar{\mathfrak q})$, a singleton since this prime is maximal. Thus (5) implies (1). All six assertions follow. ∎

#### Lemma. Characterizations of finite presentation

For an $R$-algebra $S$, the following conditions are equivalent:

1. $S$ is finitely presented over $R$.
2. For every directed system of $R$-algebras $(A_\lambda)$, the canonical map
   $$\mathop{\operatorname{colim}}_\lambda\operatorname{Hom}_R(S,A_\lambda)
   \longrightarrow\operatorname{Hom}_R(S,\mathop{\operatorname{colim}}_\lambda A_\lambda)$$
   is bijective.
3. The same canonical map is surjective for every such system.

**Proof.** Suppose $S=R[x_1,\ldots,x_n]/(f_1,\ldots,f_m)$. A map from $S$ into a colimit is given by the images of the finite variable list. Choose representatives at one common stage. Each of the finitely many equations vanishes at some later stage, so a common upper bound gives a map from $S$ at that stage. This proves surjectivity. If two maps have the same colimit image, their values on the finitely many generators agree at a common later stage. The maps themselves then agree there. This proves injectivity and hence (1)$\Rightarrow$(2). The implication (2)$\Rightarrow$(3) is immediate.

Assume (3). Write $S=\operatorname{colim}S_\lambda$ with $S_\lambda$ finitely presented, using the [finite-data construction](#native-algebra-lemma-ring-colimit-fp). The identity of $S$ factors through one stage:

$$S\xrightarrow{\sigma}S_\lambda\xrightarrow{\rho}S,
\qquad\rho\sigma=1_S.$$

Here is an explicit finite presentation of this retract. Choose algebra generators $a_1,\ldots,a_n$ of $S_\lambda$ over $R$ and put $e=\sigma\rho$. The kernel of $\rho$ is the ideal generated by $a_i-e(a_i)$. Indeed, modulo that ideal the two endomorphisms $1$ and $e$ agree on every generator, hence on every element; if $\rho(a)=0$, then $e(a)=0$, so $a$ belongs to the ideal. The reverse inclusion follows from $\rho e=\rho$. Thus $S$ is a quotient of the finitely presented algebra $S_\lambda$ by finitely many relations, and is finitely presented over $R$.

The finite-type permanence argument gives the same conclusion: $S_\lambda$ is of finite type over $S$ through $\sigma$, and the composite $S\to S_\lambda\to S$ is the finitely presented identity. Part (4) of [finite-presentation permanence](#native-algebra-lemma-compose-finite-type) makes $S$ finitely presented over $S_\lambda$; composition with $R\to S_\lambda$ then proves (1). ∎

#### Lemma. The filtered category of finite ring presentations

For an $R$-algebra $A$, consider the category of finitely presented $R$-algebras $A'$ equipped with a map $A'\to A$; arrows commute with those maps. With the size convention below,[^1] this category is filtered and its algebra colimit is canonically $A$.

**Proof.** The object $R\to A$ makes it nonempty. Two objects have a common target, their tensor product over $R$ with the map to $A$ induced by multiplication. Tensor products of two finitely presented algebras have finite presentations, obtained by joining their variables and relations.

For parallel arrows $u,v:A'\to A''$, choose finite algebra generators $a_1,\ldots,a_n$ of $A'$. The quotient

$$A'''=A''/(u(a_i)-v(a_i):1\leq i\leq n)$$

is finitely presented over $R$, still maps to $A$, and the quotient arrow equalizes $u$ and $v$. They agree after quotienting on generators and hence everywhere. This verifies all filteredness conditions.

One may compute a filtered algebra colimit using representatives from its objects. Sums and products of two representatives are formed in a common later object, and equality is witnessed in a further object; filteredness makes these operations well-defined. The resulting ring has the required universal property. Its canonical map to $A$ is onto because $a\in A$ is represented by the object $R[T]\to A$ with $T\mapsto a$. If a representative $a'\in A'$ maps to zero in $A$, the object $A'/(a')\to A$ kills it and is still finitely presented. Thus the colimit map is injective as well, proving the assertion. ∎

#### Definition. Standard smooth presentations

Choose $n\geq c\geq0$ and polynomials $f_1,\ldots,f_c\in R[x_1,\ldots,x_n]$. The presentation

$$S=R[x_1,\ldots,x_n]/(f_1,\ldots,f_c)$$

is **standard smooth** if the image in $S$ of

$$\Delta=\det\left(\frac{\partial f_j}{\partial x_i}\right)_{1\leq i,j\leq c}$$

is a unit. Thus the determinant uses the first $c$ variables; ordering other chosen variables first gives the corresponding presentation. For $c=0$ the determinant is $1$. An $R$-algebra, or its structure homomorphism, is called standard smooth if it admits an $R$-algebra isomorphism with such a presentation.

#### Proposition. Characterizations of formal smoothness

Let $R\to S$ be any ring map. In the conditions below, $P\twoheadrightarrow S$ ranges over surjections of $R$-algebras for which $P$ is formally smooth over $R$, and $J$ denotes the kernel. The following are equivalent:

1. $S$ is formally smooth over $R$.
2. For at least one such surjection, $P/J^2\to S$ has an $R$-algebra section.
3. Every such surjection has that section.
4. For at least one such surjection, the sequence
   $$0\longrightarrow J/J^2\longrightarrow\Omega_{P/R}\otimes_PS
   \longrightarrow\Omega_{S/R}\longrightarrow0$$
   is split exact.
5. This sequence is split exact for every such surjection.
6. The naive cotangent complex $\mathrm{NL}_{S/R}$ is quasi-isomorphic to a projective $S$-module in degree zero; equivalently,
   $$H_1(\mathrm{NL}_{S/R})=0\quad\text{and}\quad\Omega_{S/R}\text{ is projective}.$$

Polynomial algebras on arbitrary sets of variables provide examples of the allowed $P$, so the existence conditions always range over a nonempty class.

**Proof.** The complete polynomial-presentation criterion is *Formally smooth, unramified and étale ring maps*, Theorem 3.1 and §4. Its proof permits infinitely many variables. It identifies (1) and (6): for a polynomial presentation the degree-zero term is free, and vanishing of degree-one homology together with projectivity of the cokernel is exactly a split conormal sequence. The presentation-comparison theorem identifies this with the canonical naive complex.

We verify the assertions for a general formally smooth $P$. Condition (1) lifts $1_S$ across the square-zero kernel of $P/J^2\to S$, giving (3), and (3) implies (2). Conversely, given the section in (2), test a map $S\to A/I$ with $I^2=0$. Formal smoothness of $P$ lifts its composite with $P\to S$ to $P\to A$. This lift kills $J^2$ because it sends $J$ into $I$. Composing the induced map $P/J^2\to A$ with the section lifts $S\to A/I$. Thus (2) implies (1).

A section $\sigma:S\to P/J^2$ gives the derivation

$$D:P\longrightarrow J/J^2,\qquad
D(p)=p\bmod J^2-\sigma(\bar p),$$

where the target is an $S$-module. Its restriction to $J$ is the quotient map to $J/J^2$. The induced map on $\Omega_{P/R}\otimes_PS$ is therefore a left inverse of the conormal map. The right exact conormal sequence is consequently split exact. Applied to all sections from (3), this proves (5), and (5) implies (4).

For the converse, a splitting in (4) has an $S$-linear retraction $r:\Omega_{P/R}\otimes_PS\to J/J^2$. The derivation $D=r\circ d$ satisfies $D(j)=j\bmod J^2$ for $j\in J$. In the ring $P/J^2$, define

$$\theta(p)=p\bmod J^2-D(p).$$

The product rule and the square-zero product of two values of $D$ make $\theta$ an $R$-algebra map. It kills $J$, so descends to a section $S\to P/J^2$. This proves (4)$\Rightarrow$(2) and completes the equivalences.

For another proof of (4)$\Rightarrow$(6), use transitivity. Formal smoothness of $P$ gives a split polynomial cotangent complex with projective degree-zero homology $\Omega_{P/R}$. Tensoring its split decomposition with $S$ leaves no degree-one homology. Since $P\to S$ is surjective, its relative naive complex is $J/J^2$ in degree one. Cotangent transitivity yields

$$0\longrightarrow H_1(\mathrm{NL}_{S/R})\longrightarrow J/J^2
\longrightarrow\Omega_{P/R}\otimes_PS
\longrightarrow\Omega_{S/R}\longrightarrow0.$$

The splitting in (4) makes the first homology zero. The middle differential module is projective, since $\Omega_{P/R}$ is projective and projectivity survives base change. Its direct summand $\Omega_{S/R}$ is projective, giving (6). The split decomposition just used justifies tensoring here without any flatness assumption on $S$ over $P$. ∎

#### Lemma. Containment in the Jacobson radical

For an ideal $I\subset R$, the following conditions are equivalent:

1. $I\subset\operatorname{Jac}(R)$.
2. Every element of $1+I$ is invertible in $R$.

When these hold, an element which is invertible modulo $I$ is already invertible in $R$.

**Proof.** If $a$ belongs to every maximal ideal, $1+a$ belongs to none: otherwise subtraction would put $1$ in that maximal ideal. An element in no maximal ideal generates the unit ideal and is a unit. This proves (1)$\Rightarrow$(2).

If (1) fails, choose a maximal ideal $\mathfrak m$ with $I\not\subset\mathfrak m$. Then $I+\mathfrak m=R$, so some $a\in I$ satisfies $1-a\in\mathfrak m$. The element $1-a\in1+I$ is not a unit, contradicting (2). Finally, if $f$ is a unit modulo $I$, choose $g$ with $fg=1+a$, $a\in I$. The latter is a unit by (2), and $g(fg)^{-1}$ is an inverse of $f$. ∎

#### Lemma. The Artin–Rees lemma (Artin-Rees)

Let $R$ be Noetherian, $I\subset R$ an ideal, and $N\subset M$ finite $R$-modules. Some integer $c>0$ satisfies

$$I^nM\cap N=I^{n-c}(I^cM\cap N)\qquad(n\geq c).$$

**Proof.** The full graded argument is *Noetherian and Artinian rings*, Theorem 5.1. Introduce the Rees algebra and its module

$$\mathcal R=\bigoplus_{n\geq0}I^nt^n,\qquad
\mathcal M=\bigoplus_{n\geq0}I^nM\,t^n.$$

Generators of the finite ideal $I$ make $\mathcal R$ a finite type $R$-algebra, hence Noetherian. Generators of $M$ in degree zero make $\mathcal M$ finite over it. Its graded submodule

$$\mathcal N=\bigoplus_{n\geq0}(I^nM\cap N)t^n$$

therefore has a finite homogeneous generating list. Choose $c\geq1$ at least as large as every generator degree. If a generator has degree $d\leq c$, its contribution in degree $n\geq c$ lies in

$$I^{n-d}(I^dM\cap N)
\subset I^{n-c}(I^cM\cap N).$$

This gives one inclusion in the assertion. The reverse inclusion follows because multiplication by $I^{n-c}$ sends $I^cM\cap N$ into both $I^nM$ and $N$. If the graded submodule is zero, take $c=1$. Thus the strictly positive choice in the statement is always available. ∎

#### Lemma. The snake lemma

*Historical source citation:* Cartan–Eilenberg, III, Lemma 3.3.

Take exact rows of abelian groups

$$X\xrightarrow{u}Y\xrightarrow{v}Z\longrightarrow0,
\qquad 0\longrightarrow U\xrightarrow{a}V\xrightarrow{b}W,$$

and homomorphisms $\alpha:X\to U$, $\beta:Y\to V$, $\gamma:Z\to W$ with

$$\beta u=a\alpha,\qquad \gamma v=b\beta.$$

There is a canonical exact sequence

$$\ker\alpha\longrightarrow\ker\beta\longrightarrow\ker\gamma
\xrightarrow{\partial}\operatorname{coker}\alpha
\longrightarrow\operatorname{coker}\beta
\longrightarrow\operatorname{coker}\gamma.$$

If $u$ is injective, its first arrow is injective. If $b$ is surjective, the final arrow is surjective.

**Construction of the connecting map.** For $z\in\ker\gamma$, choose $y\in Y$ with $v(y)=z$. Then $b\beta(y)=\gamma(z)=0$, so exactness of the lower row gives a unique $w\in U$ with $a(w)=\beta(y)$. Set $\partial(z)=[w]$ modulo $\alpha(X)$. Changing the lift to $y+u(x)$ changes $w$ to $w+\alpha(x)$, so the class is independent of the lift. Choosing lifts for two elements and adding them proves additivity. The remaining maps are induced by $u,v,a,b$.

**Exactness.** At $\ker\beta$, suppose $y$ satisfies $\beta(y)=0$ and $v(y)=0$. Write $y=u(x)$. Then $a\alpha(x)=0$, and injectivity of $a$ gives $\alpha(x)=0$. Conversely $u$ carries $\ker\alpha$ into $\ker\beta$ and $vu=0$.

At $\ker\gamma$, an element coming from $\ker\beta$ has zero connecting class. If $\partial(z)=0$, choose $y,w$ as above and write $w=\alpha(x)$. Replacing $y$ by $y-u(x)$ gives an element of $\ker\beta$ still mapping to $z$. This proves exactness there.

At $\operatorname{coker}\alpha$, a class $[w]$ maps to zero precisely when $a(w)=\beta(y)$ for some $y\in Y$. Then $z=v(y)$ belongs to $\ker\gamma$, because $\gamma v(y)=b\beta(y)=ba(w)=0$, and its connecting class is $[w]$. Conversely the construction of $\partial$ makes every connecting class map to zero in $\operatorname{coker}\beta$.

At $\operatorname{coker}\beta$, let $[t]$, $t\in V$, map to zero in $\operatorname{coker}\gamma$. Write $b(t)=\gamma(z)$ and lift $z$ to $y\in Y$. Then $b(t-\beta(y))=0$, so $t-\beta(y)=a(w)$ for some $w\in U$. Thus $[t]$ is the image of $[w]$. The reverse inclusion follows from $ba=0$.

If $u$ is injective, its restriction to $\ker\alpha$ is injective. If $b$ is surjective, every class in $W/\gamma(Z)$ has a representative lifted from $V$, giving surjectivity at the other endpoint. Finally, any homomorphism between two such diagrams carries the chosen lifts into compatible lifts. It therefore preserves $\partial$, proving naturality and the claimed canonical character. ∎

#### Lemma. Characterizations of projective modules

For an arbitrary $R$-module $P$, these conditions are equivalent:

1. $P$ is projective.
2. There is an $R$-module $Q$ such that $P\oplus Q$ is free.
3. $\operatorname{Ext}^1_R(P,M)=0$ for every $R$-module $M$.

**Proof.** Take a free surjection $\pi:F\to P$. If $P$ is projective, its identity lifts to $i:P\to F$, with $\pi i=1_P$. Every $f\in F$ has the unique decomposition

$$f=i\pi(f)+(f-i\pi(f)),\qquad f-i\pi(f)\in\ker\pi.$$

Thus $F=i(P)\oplus\ker\pi$, proving (1)$\Rightarrow$(2). Conversely, maps from a free module lift across every surjection: lift the images of a basis independently. If $F=P\oplus Q$, extend a map from $P$ to $F$ by zero on $Q$, lift it from $F$, and restrict the lift to $P$. This proves projectivity of $P$. Equivalently, $\operatorname{Hom}_R(F,-)$ is a product of copies of the identity functor, hence exact, and $\operatorname{Hom}_R(P,-)$ is a direct summand of that functor.

For (2)$\Rightarrow$(3), one can compute Ext by an explicit free resolution. On $F=P\oplus Q$, let $e_P$ and $e_Q$ be the complementary projections, viewed as endomorphisms of $F$. The sequence

$$\cdots\longrightarrow F\xrightarrow{e_P}F
\xrightarrow{e_Q}F\xrightarrow{\pi}P\longrightarrow0$$

continues with alternating $e_Q,e_P$. It is exact because each projector has image equal to the kernel of the other, and $\ker\pi=Q$. Applying $\operatorname{Hom}_R(-,M)$ gives complementary projections again. The complex is split exact in positive degrees, so its first cohomology, $\operatorname{Ext}^1_R(P,M)$, vanishes.

Assume (3), and choose any free resolution with differentials $d_j:F_j\to F_{j-1}$ and augmentation $F_0\to P$. Set $K=\ker(F_0\to P)$, and write $d_1=iq$, where $i:K\hookrightarrow F_0$ and $q\colon F_1\twoheadrightarrow K$. Since $q d_2=0$, the map $q$ is a degree-one cocycle in $\operatorname{Hom}_R(F_\bullet,K)$. Its class vanishes by (3), so there is $s:F_0\to K$ with $q=s d_1=s i q$. Surjectivity of $q$ implies $si=1_K$. Hence

$$F_0=\ker s\oplus i(K),\qquad \ker s\simeq P.$$

This is (2). No finite-generation hypothesis was used. ∎

#### Lemma. Composition of standard smooth presentations

If $R\to S$ and $S\to T$ are standard smooth, their composite $R\to T$ is standard smooth.

**Proof.** Choose presentations

$$S=R[x_1,\ldots,x_n]/(f_1,\ldots,f_c),\qquad
T=S[y_1,\ldots,y_m]/(g_1,\ldots,g_d),$$

with the invertible minors given by the first $c$ of the $x$ variables and the first $d$ of the $y$ variables. Lift each coefficient of $g_j$ to $R[x_1,\ldots,x_n]$, giving a polynomial $\widetilde g_j$. Then

$$T=R[x_1,\ldots,x_n,y_1,\ldots,y_m]/
(f_1,\ldots,f_c,\widetilde g_1,\ldots,\widetilde g_d).$$

Order the selected variables first: $x_1,\ldots,x_c,y_1,\ldots,y_d$. For these rows and the displayed equation columns, the Jacobian block is

$$\begin{pmatrix}A&C\\0&D\end{pmatrix},\qquad
A=\left(\frac{\partial f_j}{\partial x_i}\right)_{i,j\leq c},
\quad D=\left(\frac{\partial\widetilde g_j}{\partial y_i}\right)_{i,j\leq d}.$$

The zero block occurs because the $f_j$ use no $y$ variables. In $T$, the block $D$ is the Jacobian block of the $g_j$ over $S$. Thus the determinant is the product of the two prescribed units. The combined presentation is standard smooth. The same argument includes $c=0$ or $d=0$, with empty determinant equal to one. ∎

#### Lemma. The spectrum of a localization

For a multiplicative subset $S$ of a ring $R$, contraction gives a homeomorphism

$$\operatorname{Spec}(S^{-1}R)\ \xrightarrow{\sim}
D_S:=\{\mathfrak p\in\operatorname{Spec}R: \mathfrak p\cap S=\varnothing\},$$

where $D_S$ has the subspace topology. Its inverse sends $\mathfrak p$ to $S^{-1}\mathfrak p$.

**Proof.** A prime of the localized ring contracts to a prime avoiding $S$, because the images of elements of $S$ are units. Conversely, if $\mathfrak p$ avoids $S$, the quotient

$$S^{-1}R/S^{-1}\mathfrak p\simeq \bar S^{-1}(R/\mathfrak p)$$

is a nonzero domain. Thus $S^{-1}\mathfrak p$ is prime. The domain $R/\mathfrak p$ injects into this localization, so contraction returns $\mathfrak p$. Extension also returns any prime $\mathfrak q$ of $S^{-1}R$: membership of $a/s$ in $\mathfrak q$ is equivalent to membership of $a/1$, as $s/1$ is a unit. These observations prove the bijection.

Finally, a basic open $D(a/s)$ corresponds exactly to $D(a)\cap D_S$. Such opens form bases on both sides, which proves the homeomorphism. If $0\in S$, both spaces are empty and the assertion still applies. ∎

#### Lemma. A disjoint spectrum and a product of rings

Suppose $\operatorname{Spec}R=U\amalg V$ and both subsets are open. There are rings $R_1,R_2$ and an isomorphism $R\simeq R_1\times R_2$ whose two spectral components are $U$ and $V$. Each factor is both a quotient and a localization of $R$.

**Proof.** The [clopen-idempotent correspondence](#native-algebra-lemma-disjoint-decomposition) supplies $e^2=e$ with $U=D(e)$ and $V=D(1-e)$. Multiplication gives mutually inverse maps

$$R\longrightarrow eR\times(1-e)R,\quad r\longmapsto(er,(1-e)r),
\qquad (a,b)\longmapsto a+b.$$

The identities in the two factor rings are $e$ and $1-e$; their cross products vanish. Moreover,

$$eR\simeq R/(1-e)R\simeq R_e,\qquad
(1-e)R\simeq R/eR\simeq R_{1-e}.$$

Indeed, an invertible idempotent is one, so inverting $e$ imposes exactly $1-e=0$, and likewise for the other factor. The localization lemma identifies their spectra with $U,V$.

One may also obtain the same isomorphism by the [affine gluing sequence](#native-algebra-lemma-standard-covering) for $D(e),D(1-e)$. Its compatibility condition is empty because the intersection has coordinate ring $R_{e(1-e)}=0$. Both descriptions include an empty component, represented by the zero ring. ∎

#### Lemma. The topology of a Noetherian spectrum

If $R$ is Noetherian, its prime spectrum is a Noetherian topological space: every descending sequence of closed subsets eventually stabilizes.

**Proof.** Write a descending sequence as $V(I_0)\supseteq V(I_1)\supseteq\cdots$, choosing each $I_j$ radical. The correspondence between radical ideals and closed sets reverses inclusion, so $I_0\subseteq I_1\subseteq\cdots$. The ascending chain condition on ideals makes this sequence, and hence the original closed sequence, stationary. ∎

#### Lemma. Irreducibility of an affine spectrum

For every ring $R$:

1. The closure of a point $\mathfrak p$ is $V(\mathfrak p)$.
2. The irreducible closed subsets are precisely $V(\mathfrak p)$ for prime ideals $\mathfrak p$.
3. The irreducible components are precisely $V(\mathfrak p)$ for minimal prime ideals $\mathfrak p$.

**Proof.** A closed set $V(I)$ contains $\mathfrak p$ exactly when $I\subseteq\mathfrak p$. It then contains $V(\mathfrak p)$, which itself contains the point. This proves (1). A singleton is irreducible, and so is its closure, proving that all sets in (2) are irreducible.

Conversely, take a nonempty irreducible $V(I)$ and replace $I$ by its radical. If $I$ were not prime, there would be $a,b\notin I$ with $ab\in I$. Every prime containing $I$ contains $a$ or $b$, whence

$$V(I)=V(I+(a))\cup V(I+(b)).$$

Both pieces are proper: equality with either would put $a$ or $b$ in $\sqrt I=I$, by the radical-ideal correspondence. This contradicts irreducibility, so $I$ is prime. Finally, among these closed irreducible sets, maximality under inclusion is exactly minimality of the prime ideal, proving (3). ∎

#### Lemma. A single polynomial equation

Let $(R,\mathfrak m)$ be Noetherian local and let $x\in\mathfrak m$. Then

$$\dim R\leq\dim(R/xR)+1.$$

Equality holds if $x$ lies in no minimal prime of $R$; in particular, it holds when $x$ is a nonzerodivisor.

**Proof.** Put $d=\dim(R/xR)$. The complete parameter theorem is *Dimension theory of Noetherian local rings*, Theorem 2.1, with its growth bound in §1. Choose $d$ elements of the quotient generating an ideal with maximal radical, and lift them to $a_1,\ldots,a_d\in R$. The ideal $(x,a_1,\ldots,a_d)$ has radical $\mathfrak m$. The same theorem bounds $\dim R$ by its $d+1$ generators.

Now assume $x$ avoids every minimal prime. A prime chain in $R/xR$ lifts to a chain in $R$ whose bottom prime contains $x$. Choose a minimal prime below that bottom prime. It does not contain $x$, so prepending it extends the chain strictly by one. Thus $\dim R\geq d+1$, proving equality.

For the final example, a nonzerodivisor stays a nonzerodivisor after localization. If it lay in a minimal prime $\mathfrak p$, its image in the zero-dimensional local ring $R_{\mathfrak p}$ would be nilpotent. A nilpotent element cannot act injectively on this nonzero ring. Hence a nonzerodivisor avoids all minimal primes. ∎

#### Lemma. Formal étaleness in a filtered colimit

Let $(S_\lambda)$ be a directed system of formally étale $R$-algebras. Then $S=\operatorname{colim}_\lambda S_\lambda$ is formally étale over $R$.

**Proof.** Given an $R$-algebra $A$, a square-zero ideal $I\subset A$ and a map $S\to A/I$, its restriction to each $S_\lambda$ has a unique lift $h_\lambda:S_\lambda\to A$. If $\lambda\leq\mu$, the composite of $h_\mu$ with the transition map is another lift of the same restriction. Uniqueness forces it to equal $h_\lambda$. The lifts are therefore compatible and define $h:S\to A$. A second lift would agree on every $S_\lambda$ and hence everywhere. This proves existence and uniqueness. The equivalent formulation with a nilpotent ideal follows by successive square-zero quotients. ∎

#### Definition. Separable field extensions

For a field extension $K/k$:

1. It is **separably generated** when some transcendence basis $(x_i)_{i\in I}$ makes $K/k(x_i:i\in I)$ algebraic and separable.
2. It is **separable** when every intermediate field finitely generated over $k$ is separably generated over $k$.

The first definition permits an arbitrary set of transcendence-basis elements, and the second tests all finite lists of field generators.

#### Lemma. Composition of formally smooth maps

Formal smoothness is preserved by composition of ring maps.

**Proof.** Let $R\to S\to T$ be formally smooth, and consider an $R$-algebra map $T\to A/I$ with $I^2=0$. First lift its restriction on $S$ to an $R$-algebra map $S\to A$. Use this lift to regard $A$ as an $S$-algebra. The given map $T\to A/I$ is now a map of $S$-algebras, so formal smoothness of $S\to T$ lifts it to $T\to A$. This is also an $R$-algebra lift, proving the claim. ∎

#### Lemma. Formal smoothness of field extensions

A field extension $K/k$ is formally smooth exactly when $H_1(L_{K/k})=0$.

**Proof.** The degree-one homology here is the same as that of the naive cotangent complex. The [formal-smoothness criterion](#native-algebra-proposition-characterize-formally-smooth) requires this vanishing and projectivity of $\Omega_{K/k}$ over $K$. The latter always holds: a vector space has a basis and is free, whether or not its dimension is finite. ∎

#### Lemma. Flatness

For any $R$-module $M$, the following conditions are equivalent:

1. $M$ is flat over $R$.
2. Every injection $N\hookrightarrow N'$ stays injective after tensoring with $M$.
3. For every ideal $I\subset R$, the multiplication map $I\otimes_R M\to M$ is injective.
4. The map in (3) is injective whenever $I$ is finitely generated.

**Proof.** The complete ideal criterion, with no finiteness assumption on $M$ or Noetherian assumption on $R$, is *Tor and flat modules*, Theorem 2.1. We give its tensor argument, including the reduction to finite modules.

The implications (1)$\Rightarrow$(2)$\Rightarrow$(3)$\Rightarrow$(4) follow by applying the definitions to the indicated inclusions. Tensor is right exact, so preservation of injections also implies flatness. More explicitly, for an exact sequence $N_1\to N_2\to N_3$, set $K=\ker(N_2\to N_3)$ and $Q=\operatorname{im}(N_2\to N_3)$. The surjection $N_1\to K$ remains surjective, and

$$K\otimes_RM\longrightarrow N_2\otimes_RM
\longrightarrow Q\otimes_RM\longrightarrow0$$

is right exact. If injections are preserved, the inclusions $K\hookrightarrow N_2$ and $Q\hookrightarrow N_3$ identify the first image with exactly the kernel needed for exactness at $N_2\otimes_RM$.[^2]

It remains to derive preservation of injections from (4). First extend (4) to every ideal. An ideal is the directed union of its finitely generated subideals, and tensor commutes with that colimit. Concretely, a tensor in $I\otimes_RM$ uses a finite list of elements of $I$, so is represented in $J\otimes_RM$ for their finitely generated ideal $J$. If its image in $M$ is zero, (4) makes that representative zero. This proves (3).

Next, for any submodule $G\subset R^n$, prove by induction on $n$ that $G\otimes_RM\to M^n$ is injective. For $n=0$ this is immediate, and for $n=1$ it is the all-ideal assertion. For $n>1$, let

$$G'=G\cap(R\oplus0^{n-1}),\qquad
G''=\operatorname{im}(G\to R^{n-1}).$$

Here $G'$ is an ideal in the first copy of $R$, and $G''\subset R^{n-1}$. Tensoring $G'\to G\to G''\to0$ is right exact. If $z\in G\otimes_RM$ maps to zero in $M^n$, its image in $G''\otimes_RM$ is zero by induction. Thus it comes from $z'\in G'\otimes_RM$. The image of $z'$ in the first copy of $M$ is zero, since the inclusion of that copy in $M^n$ is injective. The all-ideal assertion makes $z'=0$, and hence $z=0$.

Finally consider $K\subset N$ and a tensor $z\in K\otimes_RM$ killed in $N\otimes_RM$. A finite submodule $K_0\subset K$ contains all elements used in a representative $z_0$ of $z$. The module $N$ is the directed union of finite submodules containing $K_0$. Because $z_0$ becomes zero in the colimit of their tensors, it is already zero in $N_0\otimes_RM$ for one such finite $N_0$. It suffices to handle the inclusion $K_0\subset N_0$.

Choose a finite free surjection $R^n\to N_0$, let $L$ be its kernel and let $L'$ be the inverse image of $K_0$. The preceding induction embeds both $L\otimes_RM$ and $L'\otimes_RM$ in $M^n$. These embeddings are compatible with $L\subset L'$. Right exactness then identifies the map for $K_0\subset N_0$ with

$$\frac{L'\otimes_RM}{L\otimes_RM}\ \longrightarrow
\frac{M^n}{L\otimes_RM},$$

which is injective.[^3] Therefore $z_0=0$, so $z=0$. This proves (2), and finishes all four equivalences. ∎

#### Lemma. Fibres of a finite ring map

Suppose $R \to S$ is finite. Then the fibres of $\operatorname{Spec}(S) \to \operatorname{Spec}(R)$ are finite.

**Proof.** By the discussion in Remark [Commutative algebra](#native-algebra-remark-fundamental-diagram) the fibres are the spectra of the rings $S \otimes_R \kappa(\mathfrak p)$. As $R \to S$ is finite, these fibre rings are finite over $\kappa(\mathfrak p)$ hence Noetherian by Lemma [Permanence of Noetherian rings](#native-algebra-lemma-noetherian-permanence). By Lemma [Incomparability for an integral ring map](#native-algebra-lemma-integral-no-inclusion) every prime of $S \otimes_R \kappa(\mathfrak p)$ is a minimal prime. Hence by Lemma [Irreducible components of a Noetherian spectrum](#native-algebra-lemma-noetherian-irreducible-components) there are at most finitely many. $\square$

#### Lemma. Incomparability for an integral ring map
 Suppose $R \to S$ is integral. Let $\mathfrak q, \mathfrak q' \in \operatorname{Spec}(S)$ be distinct primes having the same image in $\operatorname{Spec}(R)$. Then neither $\mathfrak q \subset \mathfrak q'$ nor $\mathfrak q' \subset \mathfrak q$.

**Proof.** Let $\mathfrak p \subset R$ be the image. By Remark [Commutative algebra](#native-algebra-remark-fundamental-diagram) the primes $\mathfrak q, \mathfrak q'$ correspond to ideals in $S \otimes_R \kappa(\mathfrak p)$. Thus the lemma follows from Lemma [Integral extensions and field extensions](#native-algebra-lemma-integral-over-field). $\square$

#### Lemma. Local factors of a product ring
 Any ring with finitely many maximal ideals and locally nilpotent Jacobson radical is the product of its localizations at its maximal ideals. Also, all primes are maximal.

**Proof.** Let $R$ be a ring with finitely many maximal ideals $\mathfrak m_1, \ldots, \mathfrak m_n$. Let $I = \bigcap_{i = 1}^n \mathfrak m_i$ be the Jacobson radical of $R$. Assume $I$ is locally nilpotent. Let $\mathfrak p$ be a prime ideal of $R$. Since every prime contains every nilpotent element of $R$ we see $\mathfrak p \supset \mathfrak m_1 \cap \ldots \cap \mathfrak m_n$. Since $\mathfrak m_1 \cap \ldots \cap \mathfrak m_n \supset
\mathfrak m_1 \ldots \mathfrak m_n$ we conclude $\mathfrak p \supset \mathfrak m_1 \ldots \mathfrak m_n$. Hence $\mathfrak p \supset \mathfrak m_i$ for some $i$, and so $\mathfrak p = \mathfrak m_i$. Thus the spectrum of $R$ is the discrete topological space $\{\mathfrak m_1, \ldots, \mathfrak m_n\}$. By Lemma [A disjoint spectrum and a product of rings](#native-algebra-lemma-disjoint-implies-product) applied $n - 1$ times we find that $R = R_1 \times \ldots \times R_n$ where the spectrum of $R_i$ is a singleton for each $i$. Thus $R_i$ is a local ring and since it is a localization of $R$ (by the lemma), it is one of the local rings of $R$ as desired. $\square$

#### Lemma. Completing the étale-local reduction
 Let $(R, \mathfrak m, \kappa)$ be a henselian local ring. Any finite type $R$-algebra $S$ can be written as $S = A_1 \times \ldots \times A_n \times B$ with $A_i$ local and finite over $R$ and $R \to B$ not quasi-finite at any prime of $B$ lying over $\mathfrak m$.

**Proof.** This is a combination of parts (11) and (10) of Lemma [Characterizations of henselian local rings](#native-algebra-lemma-characterize-henselian). $\square$

#### Lemma. Étaleness at a prime ideal
 Let $R \to S$ be a ring map. Let $\mathfrak q \subset S$ be a prime lying over $\mathfrak p$ in $R$. If $S/R$ is étale at $\mathfrak q$ then

1.  $\mathfrak p S_{\mathfrak q} = \mathfrak qS_{\mathfrak q}$ is the maximal ideal of the local ring $S_{\mathfrak q}$, and

2.  the field extension $\kappa(\mathfrak q)/\kappa(\mathfrak p)$ is finite separable.

**Proof.** First we may replace $S$ by $S_g$ for some $g \in S$, $g \not \in \mathfrak q$ and assume that $R \to S$ is étale. Then the lemma follows from Lemma Formally smooth, unramified and étale ring maps, Theorem 3.1 and Sections 4–7 by unwinding the fact that $S \otimes_R \kappa(\mathfrak p)$ is étale over $\kappa(\mathfrak p)$. $\square$

#### Lemma. An étale map with a prescribed residue extension
 Let $R$ be a ring. Let $\mathfrak p$ be a prime of $R$. Let $L/\kappa(\mathfrak p)$ be a finite separable field extension. There exists an étale ring map $R \to R'$ together with a prime $\mathfrak p'$ lying over $\mathfrak p$ such that the field extension $\kappa(\mathfrak p')/\kappa(\mathfrak p)$ is isomorphic to $\kappa(\mathfrak p) \subset L$.

**Proof.** By the theorem of the primitive element we may write $L = \kappa(\mathfrak p)[\alpha]$. Let $\overline{f} \in \kappa(\mathfrak p)[x]$ denote the minimal polynomial for $\alpha$ (in particular this is monic). After replacing $\alpha$ by $c\alpha$ for some $c \in R$, $c\not \in \mathfrak p$ we may assume all the coefficients of $\overline{f}$ are in the image of $R \to \kappa(\mathfrak p)$ (verification omitted). Thus we can find a monic polynomial $f \in R[x]$ which maps to $\overline{f}$ in $\kappa(\mathfrak p)[x]$. Since $\kappa(\mathfrak p) \subset L$ is separable, we see that $\gcd(\overline{f}, \overline{f}') = 1$. Hence there is an element $\gamma \in L$ such that $\overline{f}'(\alpha) \gamma = 1$. Thus we get a $R$-algebra map $$\begin{eqnarray*}
R[x, 1/f']/(f) & \longrightarrow & L \\
x & \longmapsto & \alpha \\
1/f' & \longmapsto & \gamma
\end{eqnarray*}$$ The left hand side is a standard étale algebra $R'$ over $R$ and the kernel of the ring map gives the desired prime. $\square$

#### Lemma. Going down for flat ring maps
 Let $R \to S$ be flat. Let $\mathfrak p \subset \mathfrak p'$ be primes of $R$. Let $\mathfrak q' \subset S$ be a prime of $S$ mapping to $\mathfrak p'$. Then there exists a prime $\mathfrak q \subset \mathfrak q'$ mapping to $\mathfrak p$.

**Proof.** By Lemma [Localization of a flat module](#native-algebra-lemma-flat-localization) the local ring map $R_{\mathfrak p'} \to S_{\mathfrak q'}$ is flat. By Lemma [Flatness and local algebra](#native-algebra-lemma-local-flat-ff) this local ring map is faithfully flat. By Lemma [Faithfully flat ring maps](#native-algebra-lemma-ff-rings) there is a prime mapping to $\mathfrak p R_{\mathfrak p'}$. The inverse image of this prime in $S$ does the job. $\square$

#### Lemma. Uniqueness of an étale lifting
 Let $(R, \mathfrak m, \kappa)$ be a local ring. Let $f \in R[T]$. Let $a, b \in R$ such that $f(a) = f(b) = 0$, $a = b \bmod \mathfrak m$, and $f'(a) \not \in \mathfrak m$. Then $a = b$.

**Proof.** Write $f(x + y) - f(x) = f'(x)y + g(x, y) y^2$ in $R[x, y]$ (this is possible as one sees by expanding $f(x + y)$; details omitted). Then we see that $0 = f(b) - f(a) = f(a + (b - a)) - f(a) =
f'(a)(b - a) + c (b - a)^2$ for some $c \in R$. By assumption $f'(a)$ is a unit in $R$. Hence $(b - a)(1 + f'(a)^{-1}c(b - a)) = 0$. By assumption $b - a \in \mathfrak m$, hence $1 + f'(a)^{-1}c(b - a)$ is a unit in $R$. Hence $b - a = 0$ in $R$. $\square$

#### Lemma. Making a quasi-finite algebra finite étale locally

Let $R \to S$ be a ring map. Let $\mathfrak p \subset R$ be a prime. Assume $R \to S$ is finite type. Then there exists

1.  an étale ring map $R \to R'$,

2.  a prime $\mathfrak p' \subset R'$ lying over $\mathfrak p$,

3.  a product decomposition $$R' \otimes_R S = A_1 \times \ldots \times A_n \times B$$

with the following properties

1.  we have $\kappa(\mathfrak p) = \kappa(\mathfrak p')$,

2.  each $A_i$ is finite over $R'$,

3.  each $A_i$ has exactly one prime $\mathfrak r_i$ lying over $\mathfrak p'$, and

4.  $R' \to B$ is not quasi-finite at any prime lying over $\mathfrak p'$.

**Proof.** Denote by $F = S \otimes_R \kappa(\mathfrak p)$ the fibre ring of $S/R$ at the prime $\mathfrak p$. As $F$ is of finite type over $\kappa(\mathfrak p)$ it is Noetherian and hence $\operatorname{Spec}(F)$ has finitely many isolated closed points. If there are no isolated closed points, i.e., no primes $\mathfrak q$ of $S$ over $\mathfrak p$ such that $S/R$ is quasi-finite at $\mathfrak q$, then the lemma holds. If there exists at least one such prime $\mathfrak q$, then we may apply Lemma [Étale morphisms and prime spectra and associated points](#native-algebra-lemma-etale-makes-quasi-finite-finite-one-prime). This gives a diagram $$\begin{gathered}\begin{matrix}S & R'\otimes_R S & A_1 \times B' \\ R & R'\end{matrix} \\[6pt] \begin{aligned}S & \longrightarrow R'\otimes_R S \\ R'\otimes_R S & \mathrel{=} A_1 \times B' \\ R & \longrightarrow R' \\ R & \longrightarrow S \\ R' & \longrightarrow R'\otimes_R S \\ R' & \longrightarrow A_1 \times B'\end{aligned}\end{gathered}$$ as in said lemma. Since the residue fields at $\mathfrak p$ and $\mathfrak p'$ are the same, the fibre rings of $S/R$ and $(A_1 \times B')/R'$ are the same. Hence, by induction on the number of isolated closed points of the fibre we may assume that the lemma holds for $R' \to B'$ and $\mathfrak p'$. Thus we get an étale ring map $R' \to R''$, a prime $\mathfrak p'' \subset R''$ and a decomposition $$R'' \otimes_{R'} B' = A_2 \times \ldots \times A_n \times B.$$ We omit the verification that the ring map $R \to R''$, the prime $\mathfrak p''$ and the resulting decomposition $$R'' \otimes_R S = (R'' \otimes_{R'} A_1) \times
A_2 \times \ldots \times A_n \times B$$ is a solution to the problem posed in the lemma. $\square$

#### Lemma. Grothendieck's fibrewise nonzerodivisor criterion

Suppose that $R \to S$ is a local ring homomorphism of local rings. Denote by $\mathfrak m$ the maximal ideal of $R$. Suppose

1.  $S$ is essentially of finite presentation over $R$,

2.  $S$ is flat over $R$, and

3.  $f \in S$ is a nonzerodivisor in $S/{\mathfrak m}S$.

Then $S/fS$ is flat over $R$, and $f$ is a nonzerodivisor in $S$.

**Proof.** Follows directly from Lemma [The general fibrewise injectivity criterion for module maps](#native-algebra-lemma-mod-injective-general). $\square$

#### Lemma. Finite flat modules over a local ring
 (Warning: see Remark [Finite generation and finite presentation over a general ring](#native-algebra-remark-warning).) Suppose $R$ is a local ring, and $M$ is a finite flat $R$-module. Then $M$ is finite free.

**Proof.** Follows from the equational criterion of flatness, see Lemma [The equational criterion for flatness](#native-algebra-lemma-flat-eq). Namely, suppose that $x_1, \ldots, x_r \in M$ map to a basis of $M/\mathfrak mM$. By Nakayama's Lemma [Nakayama's lemma](#native-algebra-lemma-nak) these elements generate $M$. We want to show there is no relation among the $x_i$. Instead, we will show by induction on $n$ that if $x_1, \ldots, x_n \in M$ are linearly independent in the vector space $M/\mathfrak mM$ then they are independent over $R$.

The base case of the induction is where we have $x \in M$, $x \not\in \mathfrak mM$ and a relation $fx = 0$. By the equational criterion there exist $y_j \in M$ and $a_j \in R$ such that $x = \sum a_j y_j$ and $fa_j = 0$ for all $j$. Since $x \not\in \mathfrak mM$ we see that at least one $a_j$ is a unit and hence $f = 0$.

Suppose that $\sum f_i x_i$ is a relation among $x_1, \ldots, x_n$. By our choice of $x_i$ we have $f_i \in \mathfrak m$. According to the equational criterion of flatness there exist $a_{ij} \in R$ and $y_j \in M$ such that $x_i = \sum a_{ij} y_j$ and $\sum f_i a_{ij} = 0$. Since $x_n \not \in \mathfrak mM$ we see that $a_{nj}\not\in \mathfrak m$ for at least one $j$. Since $\sum f_i a_{ij} = 0$ we get $f_n = \sum_{i = 1}^{n-1} (-a_{ij}/a_{nj}) f_i$. The relation $\sum f_i x_i = 0$ now can be rewritten as $\sum_{i = 1}^{n-1} f_i( x_i + (-a_{ij}/a_{nj}) x_n) = 0$. Note that the elements $x_i + (-a_{ij}/a_{nj}) x_n$ map to $n-1$ linearly independent elements of $M/\mathfrak mM$. By induction assumption we get that all the $f_i$, $i \leq n-1$ have to be zero, and also $f_n = \sum_{i = 1}^{n-1} (-a_{ij}/a_{nj}) f_i$. This proves the induction step. $\square$

#### Lemma. Maps into a henselian local ring
 Let $R \to S$ be a ring map with $S$ henselian local. Given

1.  an étale ring map $R \to A$,

2.  a prime $\mathfrak q$ of $A$ lying over $\mathfrak p = R \cap \mathfrak m_S$,

3.  a $\kappa(\mathfrak p)$-algebra map $\tau : \kappa(\mathfrak q) \to S/\mathfrak m_S$,

then there exists a unique homomorphism of $R$-algebras $f : A \to S$ such that $\mathfrak q = f^{-1}(\mathfrak m_S)$ and $f$ induces the map $\tau$ on residue fields.

**Proof.** Consider $A \otimes_R S$. This is an étale algebra over $S$, see Lemma [Étale morphisms](#native-algebra-lemma-etale). Moreover, the kernel $$\mathfrak q' = \operatorname{Ker}(A \otimes_R S \to
\kappa(\mathfrak q) \otimes_{\kappa(\mathfrak p)} \kappa(\mathfrak m_S)
\xrightarrow{\tau \otimes 1}
\kappa(\mathfrak m_S))$$ is a prime ideal lying over $\mathfrak m_S$ with residue field equal to the residue field of $S$. Hence by Lemma [Characterizations of henselian local rings](#native-algebra-lemma-characterize-henselian) there exists a unique retraction $\sigma : A \otimes_R S \to S$ with $\sigma^{-1}(\mathfrak m_S) = \mathfrak q'$. Set $f$ equal to the composition $A \to A \otimes_R S \to S$. We omit the verification of the properties of $f$; the uniqueness of $f$ comes from the uniqueness of $\sigma$ (details omitted). $\square$

#### Lemma. Descent of Noetherianity

Let $R \to S$ be a ring map. Assume that

1.  $R \to S$ is faithfully flat, and

2.  $S$ is Noetherian.

Then $R$ is Noetherian.

**Proof.** Let $I_0 \subset I_1 \subset I_2 \subset \ldots$ be a growing sequence of ideals of $R$. By assumption we have $I_nS = I_{n+1}S = I_{n+2}S = \ldots$ for some $n$. By faithful flatness, extending and contracting gives the same ideal, meaning that $I = R \cap IS$ for each ideal $I$ in $R$ (Lemma [Universal injectivity of a faithfully flat ring map](#native-algebra-lemma-faithfully-flat-universally-injective)). So $I_n = I_{n+1} = I_{n+2} = \ldots$ as desired. $\square$

#### Lemma. Flatness in a filtered ring colimit
 Let $\{R_i, \varphi_{ii'}\}$ be a system of rings over the directed set $I$. Let $R = \mathop{\operatorname{colim}}_i R_i$.

1.  If $M$ is an $R$-module such that $M$ is flat as an $R_i$-module for all $i$, then $M$ is flat as an $R$-module.

2.  For $i \in I$ let $M_i$ be a flat $R_i$-module and for $i' \geq i$ let $f_{ii'} : M_i \to M_{i'}$ be a $\varphi_{ii'}$-linear map such that $f_{i' i''} \circ f_{i i'} = f_{i i''}$. Then $M = \mathop{\operatorname{colim}}_{i \in I} M_i$ is a flat $R$-module.

**Proof.** Part (1) is a special case of part (2) with $M_i = M$ for all $i$ and $f_{i i'} = \text{id}_M$. Proof of (2). Let $\mathfrak a \subset R$ be a finitely generated ideal. By Lemma [Flatness](#native-algebra-lemma-flat) it suffices to show that $\mathfrak a \otimes_R M \to M$ is injective. We can find an $i \in I$ and a finitely generated ideal $\mathfrak a' \subset R_i$ such that $\mathfrak a = \mathfrak a'R$. Then $\mathfrak a = \mathop{\operatorname{colim}}_{i' \geq i} \mathfrak a'R_{i'}$. Since $\otimes$ commutes with colimits the map $\mathfrak a \otimes_R M \to M$ is the colimit of the maps $$\mathfrak a'R_{i'} \otimes_{R_{i'}} M_{i'} \longrightarrow M_{i'}$$ These maps are all injective by assumption. Since colimits over $I$ are exact by Lemma [Filtered limits and commutative algebra](#native-algebra-lemma-directed-colimit-exact) we win. $\square$

#### Lemma. A strict henselization map extending a henselization map

Let $R \to S$ be a ring map. Let $\mathfrak q \subset S$ be a prime lying over $\mathfrak p \subset R$ such that $\kappa(\mathfrak p) \to \kappa(\mathfrak q)$ is an isomorphism. Choose a separable algebraic closure $\kappa^{sep}$ of $\kappa(\mathfrak p) = \kappa(\mathfrak q)$. Then $$(S_\mathfrak q)^{sh} =
(S_\mathfrak q)^h \otimes_{(R_\mathfrak p)^h} (R_\mathfrak p)^{sh}$$

**Proof.** This follows from the alternative construction of the strict henselization of a local ring in Remark [Derived Hom and Ext](#native-algebra-remark-construct-sh-from-h) and the fact that the residue fields are equal. Some details omitted. $\square$

#### Lemma. Functoriality of strict henselization
 Let $R \to S$ be a local map of local rings. Choose separable algebraic closures $R/\mathfrak m_R \subset \kappa_1^{sep}$ and $S/\mathfrak m_S \subset \kappa_2^{sep}$. Let $R \to R^{sh}$ and $S \to S^{sh}$ be the corresponding strict henselizations. Given any commutative diagram $$\begin{gathered}\begin{matrix}\kappa_1^{sep} & \kappa_2^{sep} \\ R/\mathfrak m_R & S/\mathfrak m_S\end{matrix} \\[6pt] \begin{aligned}\kappa_1^{sep} & \xrightarrow{\phi} \kappa_2^{sep} \\ R/\mathfrak m_R & \xrightarrow{\varphi} S/\mathfrak m_S \\ R/\mathfrak m_R & \longrightarrow \kappa_1^{sep} \\ S/\mathfrak m_S & \longrightarrow \kappa_2^{sep}\end{aligned}\end{gathered},$$ there exists a unique local ring map $R^{sh} \to S^{sh}$ fitting into the commutative diagram $$\begin{gathered}\begin{matrix}R^{sh} & S^{sh} \\ R & S\end{matrix} \\[6pt] \begin{aligned}R^{sh} & \xrightarrow{f} S^{sh} \\ R & \longrightarrow R^{sh} \\ R & \longrightarrow S \\ S & \longrightarrow S^{sh}\end{aligned}\end{gathered}$$ and inducing $\phi$ on the residue fields of $R^{sh}$ and $S^{sh}$.

**Proof.** Follows immediately from Lemma [Filtered limits and henselian rings](#native-algebra-lemma-map-into-henselian-colimit). $\square$

#### Lemma. A finite cover by affine localizations

Zariski-local properties of modules and algebras

Let $R$ be a ring. Let $M$ be an $R$-module. Let $S$ be an $R$-algebra. Suppose that $f_1, \ldots, f_n$ is a finite list of elements of $R$ such that $\bigcup D(f_i) = \operatorname{Spec}(R)$, in other words $(f_1, \ldots, f_n) = R$.

1.  If each $M_{f_i} = 0$ then $M = 0$.

2.  If each $M_{f_i}$ is a finite $R_{f_i}$-module, then $M$ is a finite $R$-module.

3.  If each $M_{f_i}$ is a finitely presented $R_{f_i}$-module, then $M$ is a finitely presented $R$-module.

4.  Let $M \to N$ be a map of $R$-modules. If $M_{f_i} \to N_{f_i}$ is an isomorphism for each $i$ then $M \to N$ is an isomorphism.

5.  Let $0 \to M'' \to M \to M' \to 0$ be a complex of $R$-modules. If $0 \to M''_{f_i} \to M_{f_i} \to M'_{f_i} \to 0$ is exact for each $i$, then $0 \to M'' \to M \to M' \to 0$ is exact.

6.  If each $R_{f_i}$ is Noetherian, then $R$ is Noetherian.

7.  If each $S_{f_i}$ is a finite type $R_{f_i}$-algebra, then $S$ is a finite type $R$-algebra.

8.  If each $S_{f_i}$ is of finite presentation over $R_{f_i}$, then $S$ is a finitely presented $R$-algebra.

**Proof.** We prove each of the parts in turn.

1.  By Proposition [Successive localizations](#native-algebra-proposition-localize-twice) this implies $M_\mathfrak p = 0$ for all $\mathfrak p \in \operatorname{Spec}(R)$, so we conclude by Lemma [Detecting a zero module by localization](#native-algebra-lemma-characterize-zero-local).

2.  For each $i$ take a finite generating set $X_i$ of $M_{f_i}$. Without loss of generality, we may assume that the elements of $X_i$ are in the image of the localization map $M \rightarrow M_{f_i}$, so we take a finite set $Y_i$ of preimages of the elements of $X_i$ in $M$. Let $Y$ be the union of these sets. This is still a finite set. Consider the obvious $R$-linear map $R^Y \rightarrow M$ sending the basis element $e_y$ to $y$. By assumption this map is surjective after localizing at an arbitrary prime ideal $\mathfrak p$ of $R$, so it is surjective by Lemma [Detecting a zero module by localization](#native-algebra-lemma-characterize-zero-local) and $M$ is finitely generated.

3.  By (2) we have a short exact sequence $$0 \rightarrow K \rightarrow R^m \rightarrow M \rightarrow 0$$ Since localization is an exact functor and $M_{f_i}$ is finitely presented we see that $K_{f_i}$ is finitely generated for all $1 \leq i \leq n$ by Lemma [Commutative algebra](#native-algebra-lemma-extension). By (2) this implies that $K$ is a finite $R$-module and therefore $M$ is finitely presented.

4.  By Proposition [Successive localizations](#native-algebra-proposition-localize-twice) the assumption implies that the induced morphism on localizations at all prime ideals is an isomorphism, so we conclude by Lemma [Detecting a zero module by localization](#native-algebra-lemma-characterize-zero-local).

5.  By Proposition [Successive localizations](#native-algebra-proposition-localize-twice) the assumption implies that the induced sequence of localizations at all prime ideals is short exact, so we conclude by Lemma [Detecting a zero module by localization](#native-algebra-lemma-characterize-zero-local).

6.  We will show that every ideal of $R$ has a finite generating set: For this, let $I \subset R$ be an arbitrary ideal. By Proposition [Exactness of localization](#native-algebra-proposition-localization-exact) each $I_{f_i} \subset R_{f_i}$ is an ideal. These are all finitely generated by assumption, so we conclude by (2).

7.  For each $i$ take a finite generating set $X_i$ of $S_{f_i}$. Without loss of generality, we may assume that the elements of $X_i$ are in the image of the localization map $S \rightarrow S_{f_i}$, so we take a finite set $Y_i$ of preimages of the elements of $X_i$ in $S$. Let $Y$ be the union of these sets. This is still a finite set. Consider the algebra homomorphism $R[X_y]_{y \in Y} \rightarrow S$ induced by $Y$. Since it is an algebra homomorphism, the image $T$ is an $R$-submodule of the $R$-module $S$, so we can consider the quotient module $S/T$. By assumption, this is zero if we localize at the $f_i$, so it is zero by (1) and therefore $S$ is an $R$-algebra of finite type.

8.  By the previous item, there exists a surjective $R$-algebra homomorphism $R[X_1, \ldots, X_n] \rightarrow S$. Let $K$ be the kernel of this map. This is an ideal in $R[X_1, \ldots, X_n]$, finitely generated in each localization at $f_i$. Since the $f_i$ generate the unit ideal in $R$, they also generate the unit ideal in $R[X_1, \ldots, X_n]$, so an application of (2) finishes the proof.

$\square$

#### Lemma. The smooth locus under flat base change

Let $R \to S$ be a ring map of finite presentation. Let $R \to R'$ be a flat ring map. Let $S' = R' \otimes_R S$ be the base change. Let $U \subset \operatorname{Spec}(S)$ be the set of primes at which $R \to S$ is smooth. Let $V \subset \operatorname{Spec}(S')$ be the set of primes at which $R' \to S'$ is smooth. Then $V$ is the inverse image of $U$ under the map $f : \operatorname{Spec}(S') \to \operatorname{Spec}(S)$.

**Proof.** By Lemma [Base change of the naive cotangent complex](#native-algebra-lemma-change-base-nl) we see that $\mathrm{NL}_{S/R} \otimes_S S'$ is homotopy equivalent to $\mathrm{NL}_{S'/R'}$. This already implies that $f^{-1}(U) \subset V$.

Let $\mathfrak q' \subset S'$ be a prime lying over $\mathfrak q \subset S$. Assume $\mathfrak q' \in V$. We have to show that $\mathfrak q \in U$. Since $S \to S'$ is flat, we see that $S_{\mathfrak q} \to S'_{\mathfrak q'}$ is faithfully flat (Lemma [Flatness and local algebra](#native-algebra-lemma-local-flat-ff)). Thus the vanishing of $H_1(L_{S'/R'})_{\mathfrak q'}$ implies the vanishing of $H_1(L_{S/R})_{\mathfrak q}$. By Lemma [Projective, locally free modules and finite algebras](#native-algebra-lemma-finite-projective-descends) applied to the $S_{\mathfrak q}$-module $(\Omega_{S/R})_{\mathfrak q}$ and the map $S_{\mathfrak q} \to S'_{\mathfrak q'}$ we see that $(\Omega_{S/R})_{\mathfrak q}$ is projective. Hence $R \to S$ is smooth at $\mathfrak q$ by Lemma [Smoothness at a point](#native-algebra-lemma-smooth-at-point). $\square$

#### Lemma. Support under base change

Let $R \to R'$ be a ring map and let $M$ be a finite $R$-module. Then $\text{Supp}(M \otimes_R R')$ is the inverse image of $\text{Supp}(M)$.

**Proof.** Let $\mathfrak p \in \text{Supp}(M)$. By Nakayama's lemma (Lemma [Nakayama's lemma](#native-algebra-lemma-nak)) we see that $$M \otimes_R \kappa(\mathfrak p) = M_\mathfrak p/\mathfrak p M_\mathfrak p$$ is a nonzero $\kappa(\mathfrak p)$ vector space. Hence for every prime $\mathfrak p' \subset R'$ lying over $\mathfrak p$ we see that $$(M \otimes_R R')_{\mathfrak p'}/\mathfrak p' (M \otimes_R R')_{\mathfrak p'} =
(M \otimes_R R') \otimes_{R'} \kappa(\mathfrak p') =
M \otimes_R \kappa(\mathfrak p) \otimes_{\kappa(\mathfrak p)}
\kappa(\mathfrak p')$$ is nonzero. This implies $\mathfrak p' \in \text{Supp}(M \otimes_R R')$. For the converse, if $\mathfrak p' \subset R'$ is a prime lying over an arbitrary prime $\mathfrak p \subset R$, then $$(M \otimes_R R')_{\mathfrak p'} =
M_\mathfrak p \otimes_{R_\mathfrak p} R'_{\mathfrak p'}.$$ Hence if $\mathfrak p' \in \text{Supp}(M \otimes_R R')$ lies over the prime $\mathfrak p \subset R$, then $\mathfrak p \in \text{Supp}(M)$. $\square$

#### Lemma. Finite presentation and formal smoothness over a Noetherian ring
 Let $R \to S$ be a smooth ring map. Then there exists a subring $R_0 \subset R$ of finite type over $\mathbf{Z}$ and a smooth ring map $R_0 \to S_0$ such that $S \cong R \otimes_{R_0} S_0$.

**Proof.** We are going to use that smooth is equivalent to finite presentation and formally smooth, see Proposition [Formal smoothness of smooth algebras](#native-algebra-proposition-smooth-formally-smooth). Write $S = R[x_1, \ldots, x_n]/(f_1, \ldots, f_m)$ and denote $I = (f_1, \ldots, f_m)$. Choose a right inverse $\sigma : S \to R[x_1, \ldots, x_n]/I^2$ to the projection to $S$ as in Lemma [Criteria for formal smoothness and smooth morphisms](#native-algebra-lemma-characterize-formally-smooth). Choose $h_i \in R[x_1, \ldots, x_n]$ such that $\sigma(x_i \bmod I) = h_i \bmod I^2$. Since $x_i - h_i \in I$, there exist $b_{ij} \in R[x_1, \ldots, x_n]$ such that $$x_i - h_i = \sum\nolimits_j b_{ij} f_j$$ The fact that $\sigma$ is an $R$-algebra homomorphism $R[x_1, \ldots, x_n]/I \to R[x_1, \ldots, x_n]/I^2$ is equivalent to the condition that $$f_j(h_1, \ldots, h_n) = \sum\nolimits_{j_1 j_2} a_{j_1 j_2} f_{j_1} f_{j_2}$$ for certain $a_{kl} \in R[x_1, \ldots, x_n]$. Let $R_0 \subset R$ be the subring generated over $\mathbf{Z}$ by all the coefficients of the polynomials $f_j, h_i, a_{kl}, b_{ij}$. Set $S_0 = R_0[x_1, \ldots, x_n]/(f_1, \ldots, f_m)$, with $I_0 = (f_1, \ldots, f_m)$. Since the second displayed equation holds in $R_0[x_1, \ldots, x_n]$ we can let $\sigma_0 : S_0 \to R_0[x_1, \ldots, x_n]/I_0^2$ be the $R_0$-algebra map defined by the rule $x_i \mapsto h_i \bmod I_0^2$. Since the first displayed equation holds in $R_0[x_1, \ldots, x_n]$ we see that $\sigma_0$ is a right inverse to the projection $R_0[x_1, \ldots, x_n] / I_0^2 \to R_0[x_1, \ldots, x_n] / I_0 = S_0$. Thus by Lemma [Criteria for formal smoothness and smooth morphisms](#native-algebra-lemma-characterize-formally-smooth) the ring $S_0$ is formally smooth over $R_0$. $\square$

#### Lemma. Relative dimension in a Cohen--Macaulay family
 Let $R$ be a ring. Let $R \to S$ be a ring map which (a) is flat, (b) is of finite presentation, and (c) has Cohen-Macaulay fibres. Then we can write $S = S_0 \times \ldots \times S_n$ as a product of $R$-algebras $S_d$ such that each $S_d$ satisfies (a), (b), (c) and has all nonempty fibres equidimensional of dimension $d$.

**Proof.** For each integer $d$ denote by $W_d \subset \operatorname{Spec}(S)$ the set defined in Lemma [Finite presentation and flatness](#native-algebra-lemma-finite-presentation-flat-cm-locus-open). Clearly we have $\operatorname{Spec}(S) = \coprod W_d$, and each $W_d$ is open by the lemma we just quoted. Hence the result follows from Lemma [A disjoint spectrum and a product of rings](#native-algebra-lemma-disjoint-implies-product). $\square$

#### Lemma. Products of smooth algebras
 Let $R$ be a ring. Let $S = S' \times S''$ be a product of $R$-algebras. Then $S$ is smooth over $R$ if and only if both $S'$ and $S''$ are smooth over $R$.

**Proof.** Omitted. Hints: By Lemma [Smooth morphisms and local algebra](#native-algebra-lemma-locally-smooth) we can check smoothness one prime at a time. Since $\operatorname{Spec}(S)$ is the disjoint union of $\operatorname{Spec}(S')$ and $\operatorname{Spec}(S'')$ by Lemma [The spectrum of a product of rings](#native-algebra-lemma-spec-product) we find that smoothness of $R \to S$ at $\mathfrak q$ corresponds to either smoothness of $R \to S'$ at the corresponding prime or smoothness of $R \to S''$ at the corresponding prime. $\square$

#### Example. Factorization of polynomials

Let $n , m \geq 1$ be integers. Consider the ring map $$\begin{eqnarray*}
R = \mathbf{Z}[a_1, \ldots, a_{n + m}]
& \longrightarrow &
S = \mathbf{Z}[b_1, \ldots, b_n, c_1, \ldots, c_m] \\
a_1 & \longmapsto & b_1 + c_1 \\
a_2 & \longmapsto & b_2 + b_1 c_1 + c_2 \\
\ldots & \ldots & \ldots \\
a_{n + m} & \longmapsto & b_n c_m
\end{eqnarray*}$$ In other words, this is the unique ring map of polynomial rings as indicated such that the polynomial factorization $$x^{n + m} + a_1 x^{n + m - 1} + \ldots + a_{n + m}
=
(x^n + b_1 x^{n - 1} + \ldots + b_n)
(x^m + c_1 x^{m - 1} + \ldots + c_m)$$ holds. Note that $S$ is generated by $n + m$ elements over $R$ (namely, $b_i, c_j$) and that there are $n + m$ equations (namely $a_k = a_k(b_i, c_j)$). In order to show that $S$ is a relative global complete intersection over $R$ it suffices to prove that all fibres have dimension $0$.

To prove this, let $R \to k$ be a ring map into a field $k$. Say $a_i$ maps to $\alpha_i \in k$. Consider the fibre ring $S_k = k \otimes_R S$. Let $k \to K$ be a field extension. A $k$-algebra map $S_k \to K$ is the same thing as finding $\beta_1, \ldots, \beta_n, \gamma_1, \ldots, \gamma_m \in K$ such that $$x^{n + m} + \alpha_1 x^{n + m - 1} + \ldots + \alpha_{n + m}
=
(x^n + \beta_1 x^{n - 1} + \ldots + \beta_n)
(x^m + \gamma_1 x^{m - 1} + \ldots + \gamma_m).$$ Hence we see there are at most finitely many choices of such $n + m$-tuples in $K$. This proves that all fibres have finitely many closed points (use Hilbert's Nullstellensatz to see they all correspond to solutions in $\overline{k}$ for example) and hence that $R \to S$ is a relative global complete intersection.

Another way to argue this is to show $\mathbf{Z}[a_1, \ldots, a_{n + m}] \to
\mathbf{Z}[b_1, \ldots, b_n, c_1, \ldots, c_m]$ is actually also a *finite* ring map. Namely, by Lemma [Divisibility of polynomials](#native-algebra-lemma-polynomials-divide) each of $b_i, c_j$ is integral over $R$, and hence $R \to S$ is finite by Lemma [Criteria for integral extensions](#native-algebra-lemma-characterize-integral).

#### Lemma. Idempotent ideals and connected components
 Let $I \subset R$ be a finitely generated ideal of a ring $R$ such that $I = I^2$. Then

1.  there exists an idempotent $e \in R$ such that $I = (e)$,

2.  $R/I \cong R_{e'}$ for the idempotent $e' = 1 - e \in R$, and

3.  $V(I)$ is open and closed in $\operatorname{Spec}(R)$.

**Proof.** By Nakayama's Lemma [Nakayama's lemma](#native-algebra-lemma-nak) there exists an element $f = 1 + i$, $i \in I$ such that $fI = 0$. Then $f^2 = f + fi = f$ is an idempotent. Consider the idempotent $e = 1 - f = -i \in I$. For $j \in I$ we have $ej = j - fj = j$ hence $I = (e)$. This proves (1).

Parts (2) and (3) follow from (1). Namely, we have $V(I) = V(e) = \operatorname{Spec}(R) \setminus D(e)$ which is open and closed by either Lemma [Idempotents and open-and-closed subsets of a spectrum](#native-algebra-lemma-idempotent-spec) or Lemma [Product decompositions from disjoint closed subsets](#native-algebra-lemma-disjoint-decomposition). This proves (3). For (2) observe that the map $R \to R_{e'}$ is surjective since $x/(e')^n = x/e' = xe'/(e')^2 = xe'/e' = x/1$ in $R_{e'}$. The kernel of the map $R \to R_{e'}$ is the set of elements of $R$ annihilated by a positive power of $e'$. Since $e'$ is idempotent this is the ideal of elements annihilated by $e'$ which is the ideal $I = (e)$ as $e + e' = 1$ is a pair of orthogonal idempotents. This proves (2). $\square$

#### Lemma. Closed subsets of an affine spectrum
 Let $R$ be a ring. Let $I \subset R$ be an ideal. The map $R \to R/I$ induces via the functoriality of $\operatorname{Spec}$ a homeomorphism $$\operatorname{Spec}(R/I) \longrightarrow V(I) \subset \operatorname{Spec}(R).$$ The inverse is given by $\mathfrak p \mapsto \mathfrak p / I$.

**Proof.** It is immediate that the image is contained in $V(I)$. On the other hand, if $\mathfrak p \in V(I)$ then $\mathfrak p \supset I$ and we may consider the ideal $\mathfrak p /I \subset R/I$. Using basic notion ([Commutative algebra](#context-algebra-item-isomorphism-theorem)) we see that $(R/I)/(\mathfrak p/I) = R/\mathfrak p$ is a domain and hence $\mathfrak p/I$ is a prime ideal. From this and Lemma [Prime spectra and associated points](#native-algebra-lemma-spec-homeomorphism-onto-image-units), applied to the surjection $R \to R/I$, the result follows. $\square$

#### Proposition. Openness of flat finitely presented maps

Let $R \to S$ be flat and of finite presentation. Then $\operatorname{Spec}(S) \to \operatorname{Spec}(R)$ is open. More generally this holds for any ring map $R \to S$ of finite presentation which satisfies going down.

**Proof.** If $R \to S$ is flat, then $R \to S$ satisfies going down by Lemma [Going down for flat ring maps](#native-algebra-lemma-flat-going-down). Thus to prove the lemma we may assume that $R \to S$ has finite presentation and satisfies going down.

Since the standard opens $D(g) \subset \operatorname{Spec}(S)$, $g \in S$ form a basis for the topology, it suffices to prove that the image of $D(g)$ is open. Recall that $\operatorname{Spec}(S_g) \to \operatorname{Spec}(S)$ is a homeomorphism of $\operatorname{Spec}(S_g)$ onto $D(g)$ (Lemma [Principal open subsets of a spectrum](#native-algebra-lemma-standard-open)). Since $S \to S_g$ satisfies going down (see above), we see that $R \to S_g$ satisfies going down by Lemma [Composition of going-up and going-down maps](#native-algebra-lemma-going-up-down-composition). Thus after replacing $S$ by $S_g$ we see it suffices to prove the image is open. By Chevalley's theorem (Theorem [Chevalley's constructibility theorem](#native-algebra-theorem-chevalley)) the image is a constructible set $E$. And $E$ is stable under generalization because $R \to S$ satisfies going down, see Topology, Lemmas [The geometric construction (programme binding)](#uncovered-topology-lemma-open-closed-specialization) and [Lifting the geometric construction (uncovered prerequisite)](#uncovered-topology-lemma-lift-specializations-images). Hence $E$ is open by Lemma [Commutative algebra](#native-algebra-lemma-constructible-stable-specialization-closed). $\square$

#### Lemma. Detecting a zero module by localization

Let $R$ be a ring.

1.  For an element $x$ of an $R$-module $M$ the following are equivalent

    1.  $x = 0$,

    2.  $x$ maps to zero in $M_\mathfrak p$ for all $\mathfrak p \in \operatorname{Spec}(R)$,

    3.  $x$ maps to zero in $M_{\mathfrak m}$ for all maximal ideals $\mathfrak m$ of $R$.

    In other words, the map $M \to \prod_{\mathfrak m} M_{\mathfrak m}$ is injective.

2.  Given an $R$-module $M$ the following are equivalent

    1.  $M$ is zero,

    2.  $M_{\mathfrak p}$ is zero for all $\mathfrak p \in \operatorname{Spec}(R)$,

    3.  $M_{\mathfrak m}$ is zero for all maximal ideals $\mathfrak m$ of $R$.

3.  Given a complex $M_1 \to M_2 \to M_3$ of $R$-modules the following are equivalent

    1.  $M_1 \to M_2 \to M_3$ is exact,

    2.  for every prime $\mathfrak p$ of $R$ the localization $M_{1, \mathfrak p} \to M_{2, \mathfrak p} \to M_{3, \mathfrak p}$ is exact,

    3.  for every maximal ideal $\mathfrak m$ of $R$ the localization $M_{1, \mathfrak m} \to M_{2, \mathfrak m} \to M_{3, \mathfrak m}$ is exact.

4.  Given a map $f : M \to M'$ of $R$-modules the following are equivalent

    1.  $f$ is injective,

    2.  $f_{\mathfrak p} : M_\mathfrak p \to M'_\mathfrak p$ is injective for all primes $\mathfrak p$ of $R$,

    3.  $f_{\mathfrak m} : M_\mathfrak m \to M'_\mathfrak m$ is injective for all maximal ideals $\mathfrak m$ of $R$.

5.  Given a map $f : M \to M'$ of $R$-modules the following are equivalent

    1.  $f$ is surjective,

    2.  $f_{\mathfrak p} : M_\mathfrak p \to M'_\mathfrak p$ is surjective for all primes $\mathfrak p$ of $R$,

    3.  $f_{\mathfrak m} : M_\mathfrak m \to M'_\mathfrak m$ is surjective for all maximal ideals $\mathfrak m$ of $R$.

6.  Given a map $f : M \to M'$ of $R$-modules the following are equivalent

    1.  $f$ is bijective,

    2.  $f_{\mathfrak p} : M_\mathfrak p \to M'_\mathfrak p$ is bijective for all primes $\mathfrak p$ of $R$,

    3.  $f_{\mathfrak m} : M_\mathfrak m \to M'_\mathfrak m$ is bijective for all maximal ideals $\mathfrak m$ of $R$.

**Proof.** Let $x \in M$ as in (1). Let $I = \{f \in R \mid fx = 0\}$. It is easy to see that $I$ is an ideal (it is the annihilator of $x$). Condition (1)(c) means that for all maximal ideals $\mathfrak m$ there exists an $f \in R \setminus \mathfrak m$ such that $fx =0$. In other words, $V(I)$ does not contain a closed point. By Lemma [The Zariski topology on an affine spectrum](#native-algebra-lemma-zariski-topology) we see $I$ is the unit ideal. Hence $x$ is zero, i.e., (1)(a) holds. This proves (1).

Part (2) follows by applying (1) to all elements of $M$ simultaneously.

Proof of (3). Let $H$ be the homology of the sequence, i.e., $H = \operatorname{Ker}(M_2 \to M_3)/\operatorname{Im}(M_1 \to M_2)$. By Proposition [Exactness of localization](#native-algebra-proposition-localization-exact) we have that $H_\mathfrak p$ is the homology of the sequence $M_{1, \mathfrak p} \to M_{2, \mathfrak p} \to M_{3, \mathfrak p}$. Hence (3) is a consequence of (2).

Parts (4) and (5) are special cases of (3). Part (6) follows formally on combining (4) and (5). $\square$

#### Lemma. Elements integral over an ideal form a submodule
 Let $\varphi : R \to S$ be a ring map. Let $I \subset R$ be an ideal. The set of elements of $S$ which are integral over $I$ forms an $R$-submodule of $S$. Furthermore, if $s \in S$ is integral over $R$, and $s'$ is integral over $I$, then $ss'$ is integral over $I$.

**Proof.** We will use Lemma [Integral extensions](#native-algebra-lemma-integral-closure-is-ring) without further mention. Closure under addition is clear from the characterization of Lemma [Criteria for integral extensions](#native-algebra-lemma-characterize-integral-ideal) whose notation we adopt. Any element $s \in S$ which is integral over $R$ corresponds to the degree $0$ element $s$ of $S[t]$ which is integral over $A$ (because $R \subset A$). Hence we see that multiplication by $s$ on $S[t]$ preserves the property of being integral over $A$, $\square$

#### Lemma. Surjectivity on spectra of an integral overring

Suppose that $R \to S$ is an integral ring extension with $R \subset S$. Then $\varphi : \operatorname{Spec}(S) \to \operatorname{Spec}(R)$ is surjective.

**Proof.** Let $\mathfrak p \subset R$ be a prime ideal. We have to show $\mathfrak pS_{\mathfrak p} \not = S_{\mathfrak p}$, see Lemma [A point in the image of a spectrum map](#native-algebra-lemma-in-image). The localization $R_{\mathfrak p} \to S_{\mathfrak p}$ is injective (as localization is exact) and integral by Lemma [Integral extensions and local algebra](#native-algebra-lemma-integral-closure-localize) or [Base change for integral extensions](#native-algebra-lemma-base-change-integral). Hence we may replace $R$, $S$ by $R_{\mathfrak p}$, $S_{\mathfrak p}$ and we may assume $R$ is local with maximal ideal $\mathfrak m$ and it suffices to show that $\mathfrak mS \not = S$. Suppose $1 = \sum f_i s_i$ with $f_i \in \mathfrak m$ and $s_i \in S$ in order to get a contradiction. Let $R \subset S' \subset S$ be such that $R \to S'$ is finite and $s_i \in S'$, see Lemma [Criteria for integral extensions](#native-algebra-lemma-characterize-integral). The equation $1 = \sum f_i s_i$ implies that the finite $R$-module $S'$ satisfies $S' = \mathfrak m S'$. Hence by Nakayama's Lemma [Nakayama's lemma](#native-algebra-lemma-nak) we see $S' = 0$. Contradiction. $\square$

#### Lemma. Composition of going-up and going-down maps
 Suppose $R \to S$ and $S \to T$ are ring maps satisfying going down. Then so does $R \to T$. Similarly for going up.

**Proof.** According to Lemma [Commutative algebra](#native-algebra-lemma-going-up-down-specialization) this follows from Topology, Lemma [Lifting the geometric construction (uncovered prerequisite)](#uncovered-topology-lemma-lift-specialization-composition) $\square$

#### Lemma. Closed images stable under specialization
 Let $R \to S$ be a ring map. Let $T \subset \operatorname{Spec}(R)$ be the image of $\operatorname{Spec}(S)$. If $T$ is stable under specialization, then $T$ is closed.

**Proof.** We give two proofs.

First proof. Let $\mathfrak p \subset R$ be a prime ideal such that the corresponding point of $\operatorname{Spec}(R)$ is in the closure of $T$. This means that for every $f \in R$, $f \not \in \mathfrak p$ we have $D(f) \cap T \not = \emptyset$. Note that $D(f) \cap T$ is the image of $\operatorname{Spec}(S_f)$ in $\operatorname{Spec}(R)$. Hence we conclude that $S_f \not = 0$. In other words, $1 \not = 0$ in the ring $S_f$. Since $S_{\mathfrak p}$ is the directed colimit of the rings $S_f$ we conclude that $1 \not = 0$ in $S_{\mathfrak p}$. In other words, $S_{\mathfrak p} \not = 0$ and considering the image of $\operatorname{Spec}(S_{\mathfrak p})
\to \operatorname{Spec}(S) \to \operatorname{Spec}(R)$ we see there exists a $\mathfrak p' \in T$ with $\mathfrak p' \subset \mathfrak p$. As we assumed $T$ closed under specialization we conclude $\mathfrak p$ is a point of $T$ as desired.

Second proof. Let $I = \operatorname{Ker}(R \to S)$. We may replace $R$ by $R/I$. In this case the ring map $R \to S$ is injective. By Lemma [Injective resolutions and prime spectra and associated points](#native-algebra-lemma-injective-minimal-primes-in-image) all the minimal primes of $R$ are contained in the image $T$. Hence if $T$ is stable under specialization then it contains all primes. $\square$

#### Lemma. Cotangent complexes and differentials
 Let $A \to B \to C$ be ring maps. Assume $A \to C$ is surjective (so also $B \to C$ is). Denote $I = \operatorname{Ker}(A \to C)$ and $J = \operatorname{Ker}(B \to C)$. Then the sequence $$I/I^2 \to J/J^2 \to \Omega_{B/A} \otimes_B B/J \to 0$$ is exact.

**Proof.** Follows from Lemma [The transitivity sequence for the naive cotangent complex](#native-algebra-lemma-exact-sequence-nl) and the description of the naive cotangent complexes $\mathrm{NL}_{C/B}$ and $\mathrm{NL}_{C/A}$ in Lemma [Cotangent complexes and differentials](#native-algebra-lemma-nl-surjection). $\square$

#### Lemma. Cotangent complexes, differentials and formal smoothness
 Let $A \to B \to C$ be ring maps. Assume $A \to C$ is surjective (so also $B \to C$ is) and $A \to B$ formally smooth. Let $I = \operatorname{Ker}(A \to C)$ and $J = \operatorname{Ker}(B \to C)$. Then the sequence $$0 \to I/I^2 \to J/J^2 \to \Omega_{B/A} \otimes_B B/J \to 0$$ of Lemma [Cotangent complexes and differentials](#native-algebra-lemma-application-nl) is split exact.

**Proof.** Since $A \to B$ is formally smooth there exists a ring map $\sigma : B \to A/I^2$, lifting $B \to C$, whose composition with $A \to B$ equals the quotient map $A \to A/I^2$. Then $\sigma$ induces a map $J/J^2 \to I/I^2$ which is a left inverse to the map $I/I^2 \to J/J^2$. $\square$

#### Lemma. A cover of the target spectrum
 Let $R \to S$ be a ring map. Suppose that $g_1, \ldots, g_n$ is a finite list of elements of $S$ such that $\bigcup D(g_i) = \operatorname{Spec}(S)$ in other words $(g_1, \ldots, g_n) = S$.

1.  If each $S_{g_i}$ is of finite type over $R$, then $S$ is of finite type over $R$.

2.  If each $S_{g_i}$ is of finite presentation over $R$, then $S$ is of finite presentation over $R$.

**Proof.** Choose $h_1, \ldots, h_n \in S$ such that $\sum h_i g_i = 1$.

Proof of (1). For each $i$ choose a finite list of elements $x_{i, j} \in S_{g_i}$, $j = 1, \ldots, m_i$ which generate $S_{g_i}$ as an $R$-algebra. Write $x_{i, j} = y_{i, j}/g_i^{n_{i, j}}$ for some $y_{i, j} \in S$ and some $n_{i, j} \ge 0$. Consider the $R$-subalgebra $S' \subset S$ generated by $g_1, \ldots, g_n$, $h_1, \ldots, h_n$ and $y_{i, j}$, $i = 1, \ldots, n$, $j = 1, \ldots, m_i$. Since localization is exact (Proposition [Exactness of localization](#native-algebra-proposition-localization-exact)), we see that $S'_{g_i} \to S_{g_i}$ is injective. On the other hand, it is surjective by our choice of $y_{i, j}$. The elements $g_1, \ldots, g_n$ generate the unit ideal in $S'$ as $h_1, \ldots, h_n \in S'$. Thus $S' \to S$ viewed as an $S'$-module map is an isomorphism by Lemma [A finite cover by affine localizations](#native-algebra-lemma-cover).

Proof of (2). We already know that $S$ is of finite type. Write $S = R[x_1, \ldots, x_m]/J$ for some ideal $J$. For each $i$ choose a lift $g'_i \in R[x_1, \ldots, x_m]$ of $g_i$ and we choose a lift $h'_i \in R[x_1, \ldots, x_m]$ of $h_i$. Then we see that $$S_{g_i} = R[x_1, \ldots, x_m, y_i]/(J_i + (1 - y_ig'_i))$$ where $J_i$ is the ideal of $R[x_1, \ldots, x_m, y_i]$ generated by $J$. Small detail omitted. By Lemma [Finite presentation and finite algebras](#native-algebra-lemma-finite-presentation-independent) we may choose a finite list of elements $f_{i, j} \in J$, $j = 1, \ldots, m_i$ such that the images of $f_{i, j}$ in $J_i$ and $1 - y_ig'_i$ generate the ideal $J_i + (1 - y_ig'_i)$. Set $$S' = R[x_1, \ldots, x_m]/\left(\sum h'_ig'_i - 1, f_{i, j}; 
i = 1, \ldots, n, j = 1, \ldots, m_i\right)$$ There is a surjective $R$-algebra map $S' \to S$. The classes of the elements $g'_1, \ldots, g'_n$ in $S'$ generate the unit ideal and by construction the maps $S'_{g'_i} \to S_{g_i}$ are injective. Thus we conclude as in part (1). $\square$

#### Lemma. Nakayama's lemma after localization
 Let $R$ be a ring, let $S \subset R$ be a multiplicative subset, let $I \subset R$ be an ideal, and let $M$ be a finite $R$-module. If $x_1, \ldots, x_r \in M$ generate $S^{-1}(M/IM)$ as an $S^{-1}(R/I)$-module, then there exists an $f \in S + I$ such that $x_1, \ldots, x_r$ generate $M_f$ as an $R_f$-module.[^4]

**Proof.** Special case $I = 0$. Let $y_1, \ldots, y_s$ be generators for $M$ over $R$. Since $S^{-1}M$ is generated by $x_1, \ldots, x_r$, for each $i$ we can write $y_i = \sum (a_{ij}/s_{ij})x_j$ in $S^{-1}M$ for some $a_{ij} \in R$ and $s_{ij} \in S$. Multiplying by the product $s \in S$ of the $s_{ij}$ we see that $sy_i = \sum a'_{ij}x_j$ in $S^{-1}M$ for some $a'_{ij} \in R$. This in turn means there exist $t_i \in S$ such that $t_isy_i = \sum t_ia'_{ij}x_j$ in $M$. Thus if $t \in S$ is the product of the $t_i$, then we see that $y_i$ is in the $R_{st}$-submodule generated by $x_1, \ldots, x_r$ of $M_{st}$. Hence $x_1, \ldots, x_r$ generate $M_{st}$.

General case. By the special case, we can find an $s \in S$ such that $x_1, \ldots, x_r$ generate $(M/IM)_s$ over $(R/I)_s$. By Lemma [Nakayama's lemma](#native-algebra-lemma-nak) we can find a $g \in 1 + I_s \subset R_s$ such that $x_1, \ldots, x_r$ generate $(M_s)_g$ over $(R_s)_g$. Write $g = 1 + i/s'$. Then $f = ss' + is$ works; details omitted. $\square$

#### Lemma. Localization of a flat module

Let $R$ be a ring. Let $S \subset R$ be a multiplicative subset.

1.  The localization $S^{-1}R$ is a flat $R$-algebra.

2.  If $M$ is an $S^{-1}R$-module, then $M$ is a flat $R$-module if and only if $M$ is a flat $S^{-1}R$-module.

3.  Suppose $M$ is an $R$-module. Then $M$ is a flat $R$-module if and only if $M_{\mathfrak p}$ is a flat $R_{\mathfrak p}$-module for all primes $\mathfrak p$ of $R$.

4.  Suppose $M$ is an $R$-module. Then $M$ is a flat $R$-module if and only if $M_{\mathfrak m}$ is a flat $R_{\mathfrak m}$-module for all maximal ideals $\mathfrak m$ of $R$.

5.  Suppose $R \to A$ is a ring map, $M$ is an $A$-module, and $g_1, \ldots, g_m \in A$ are elements generating the unit ideal of $A$. Then $M$ is flat over $R$ if and only if each localization $M_{g_i}$ is flat over $R$.

6.  Suppose $R \to A$ is a ring map, and $M$ is an $A$-module. Then $M$ is a flat $R$-module if and only if the localization $M_{\mathfrak q}$ is a flat $R_{\mathfrak p}$-module (with $\mathfrak p$ the prime of $R$ lying under $\mathfrak q$) for all primes $\mathfrak q$ of $A$.

7.  Suppose $R \to A$ is a ring map, and $M$ is an $A$-module. Then $M$ is a flat $R$-module if and only if the localization $M_{\mathfrak m}$ is a flat $R_{\mathfrak p}$-module (with $\mathfrak p = R \cap \mathfrak m$) for all maximal ideals $\mathfrak m$ of $A$.

**Proof.** Let us prove the last statement of the lemma. In the proof we will use repeatedly that localization is exact and commutes with tensor product, see Sections [Localization of local algebra](#context-algebra-section-localization) and [Tensor products and direct sums](#context-algebra-section-tensor-product).

Suppose $R \to A$ is a ring map, and $M$ is an $A$-module. Assume that $M_{\mathfrak m}$ is a flat $R_{\mathfrak p}$-module for all maximal ideals $\mathfrak m$ of $A$ (with $\mathfrak p = R \cap \mathfrak m$). Let $I \subset R$ be an ideal. We have to show the map $I \otimes_R M \to M$ is injective. We can think of this as a map of $A$-modules. By assumption the localization $(I \otimes_R M)_{\mathfrak m} \to M_{\mathfrak m}$ is injective because $(I \otimes_R M)_{\mathfrak m} =
I_{\mathfrak p} \otimes_{R_{\mathfrak p}} M_{\mathfrak m}$. Hence the kernel of $I \otimes_R M \to M$ is zero by Lemma [Detecting a zero module by localization](#native-algebra-lemma-characterize-zero-local). Hence $M$ is flat over $R$.

Conversely, assume $M$ is flat over $R$. Pick a prime $\mathfrak q$ of $A$ lying over the prime $\mathfrak p$ of $R$. Suppose that $I \subset R_{\mathfrak p}$ is an ideal. We have to show that $I \otimes_{R_{\mathfrak p}} M_{\mathfrak q} \to M_{\mathfrak q}$ is injective. We can write $I = J_{\mathfrak p}$ for some ideal $J \subset R$. Then the map $I \otimes_{R_{\mathfrak p}} M_{\mathfrak q} \to M_{\mathfrak q}$ is just the localization (at $\mathfrak q$) of the map $J \otimes_R M \to M$ which is injective. Since localization is exact we see that $M_{\mathfrak q}$ is a flat $R_{\mathfrak p}$-module.

This proves (7) and (6). The other statements follow in a straightforward way from the last statement (proofs omitted). $\square$

#### Lemma. Hom from a finitely presented module
 Let $R$ be a ring. Let $M$ be a finitely presented $R$-module. Let $N$ be an $R$-module.

1.  For $f \in R$ we have $\operatorname{Hom}_R(M, N)_f = \operatorname{Hom}_{R_f}(M_f, N_f) = \operatorname{Hom}_R(M_f, N_f)$,

2.  for a multiplicative subset $S$ of $R$ we have $$S^{-1}\operatorname{Hom}_R(M, N) = \operatorname{Hom}_{S^{-1}R}(S^{-1}M, S^{-1}N) =
    \operatorname{Hom}_R(S^{-1}M, S^{-1}N).$$

**Proof.** Part (1) is a special case of part (2). The second equality in (2) follows from Lemma [Localization of modules and local algebra](#native-algebra-lemma-localization-and-modules). Choose a presentation $$\bigoplus\nolimits_{j = 1, \ldots, m} R
\longrightarrow
\bigoplus\nolimits_{i = 1, \ldots, n} R
\to M \to 0.$$ By Lemma [Exactness of Hom from a projective module](#native-algebra-lemma-hom-exact) this gives an exact sequence $$0 \to
\operatorname{Hom}_R(M, N) \to
\bigoplus\nolimits_{i = 1, \ldots, n} N
\longrightarrow
\bigoplus\nolimits_{j = 1, \ldots, m} N.$$ Inverting $S$ and using Proposition [Exactness of localization](#native-algebra-proposition-localization-exact) we get an exact sequence $$0 \to
S^{-1}\operatorname{Hom}_R(M, N) \to
\bigoplus\nolimits_{i = 1, \ldots, n} S^{-1}N
\longrightarrow
\bigoplus\nolimits_{j = 1, \ldots, m} S^{-1}N$$ and the result follows since $S^{-1}M$ sits in an exact sequence $$\bigoplus\nolimits_{j = 1, \ldots, m} S^{-1}R
\longrightarrow
\bigoplus\nolimits_{i = 1, \ldots, n} S^{-1}R \to S^{-1}M \to 0$$ which induces (by Lemma [Exactness of Hom from a projective module](#native-algebra-lemma-hom-exact)) the exact sequence $$0 \to
\operatorname{Hom}_{S^{-1}R}(S^{-1}M, S^{-1}N) \to
\bigoplus\nolimits_{i = 1, \ldots, n} S^{-1}N
\longrightarrow
\bigoplus\nolimits_{j = 1, \ldots, m} S^{-1}N$$ which is the same as the one above. $\square$

#### Lemma. A characteristic polynomial with coefficients in an ideal
 Let $R$ be a ring. Let $I \subset R$ be an ideal. Let $M$ be a finite $R$-module. Let $\varphi : M \to M$ be an endomorphism such that $\varphi(M) \subset IM$. Then there exists a monic polynomial $P = T^n + a_1 T^{n - 1} + \ldots + a_n \in R[T]$ such that $a_j \in I^j$ and $P(\varphi) = 0$ as an endomorphism of $M$.

**Proof.** Choose a surjective $R$-module map $R^{\oplus n} \to M$, given by $(a_1, \ldots, a_n) \mapsto \sum a_ix_i$ for some generators $x_i \in M$. Choose $(a_{i1}, \ldots, a_{in}) \in I^{\oplus n}$ such that $\varphi(x_i) = \sum a_{ij} x_j$. In other words the diagram $$\begin{gathered}\begin{matrix}R^{\oplus n} & M \\ I^{\oplus n} & M\end{matrix} \\[6pt] \begin{aligned}R^{\oplus n} & \xrightarrow{A} I^{\oplus n} \\ R^{\oplus n} & \longrightarrow M \\ M & \xrightarrow{\varphi} M \\ I^{\oplus n} & \longrightarrow M\end{aligned}\end{gathered}$$ is commutative where $A = (a_{ij})$. By Lemma [The characteristic polynomial](#native-algebra-lemma-charpoly) the polynomial $P(t) = \det(t\text{id}_{n \times n} - A)$ has all the desired properties. $\square$

#### Lemma. Finite module presentations in a filtered colimit
 Suppose that $R = \mathop{\operatorname{colim}}_{\lambda \in \Lambda} R_\lambda$ is a directed colimit of rings. Then the category of finitely presented $R$-modules is the colimit of the categories of finitely presented $R_\lambda$-modules. More precisely

1.  Given a finitely presented $R$-module $M$ there exists a $\lambda \in \Lambda$ and a finitely presented $R_\lambda$-module $M_\lambda$ such that $M \cong M_\lambda \otimes_{R_\lambda} R$.

2.  Given a $\lambda \in \Lambda$, finitely presented $R_\lambda$-modules $M_\lambda, N_\lambda$, and an $R$-module map $\varphi : M_\lambda \otimes_{R_\lambda} R \to N_\lambda \otimes_{R_\lambda} R$, then there exists a $\mu \geq \lambda$ and an $R_\mu$-module map $\varphi_\mu : M_\lambda \otimes_{R_\lambda} R_\mu \to
    N_\lambda \otimes_{R_\lambda} R_\mu$ such that $\varphi = \varphi_\mu \otimes 1_R$.

3.  Given a $\lambda \in \Lambda$, finitely presented $R_\lambda$-modules $M_\lambda, N_\lambda$, and $R_\lambda$-module maps $\varphi, \psi : M_\lambda \to N_\lambda$ such that $\varphi \otimes 1_R = \psi \otimes 1_R$, then $\varphi \otimes 1_{R_\mu} = \psi \otimes 1_{R_\mu}$ for some $\mu \geq \lambda$.

**Proof.** To prove (1) choose a presentation $R^{\oplus m} \to R^{\oplus n} \to M \to 0$. Suppose that the first map is given by the matrix $A = (a_{ij})$. We can choose a $\lambda \in \Lambda$ and a matrix $A_\lambda = (a_{\lambda, ij})$ with coefficients in $R_\lambda$ which maps to $A$ in $R$. Then we simply let $M_\lambda$ be the $R_\lambda$-module with presentation $R_\lambda^{\oplus m} \to R_\lambda^{\oplus n} \to M_\lambda \to 0$ where the first arrow is given by $A_\lambda$.

Parts (2) and (3) follow from Lemma [Filtered limits and proper morphisms and modules](#native-algebra-lemma-module-map-property-in-colimit). $\square$

#### Lemma. Flat modules in a short exact sequence
 Suppose that $0 \to M' \to M \to M'' \to 0$ is a short exact sequence of $R$-modules. If $M'$ and $M''$ are flat so is $M$. If $M$ and $M''$ are flat so is $M'$.

**Proof.** We will use the criterion that a module $N$ is flat if for every ideal $I \subset R$ the map $N \otimes_R I \to N$ is injective, see Lemma [Flatness](#native-algebra-lemma-flat). Consider an ideal $I \subset R$. Consider the diagram $$\begin{matrix}
0 & \to & M' & \to & M & \to & M'' & \to & 0 \\
& & \uparrow & & \uparrow & & \uparrow & & \\
& & M'\otimes_R I & \to & M \otimes_R I & \to & M''\otimes_R I & \to & 0
\end{matrix}$$ with exact rows. This immediately proves the first assertion. The second follows because if $M''$ is flat then the lower left horizontal arrow is injective by Lemma [Tor vanishing for a flat module](#native-algebra-lemma-flat-tor-zero). $\square$

#### Lemma. Quasi-regular and regular ideals in a Noetherian ring

Let $(R, \mathfrak m)$ be a local Noetherian ring. Let $M$ be a nonzero finite $R$-module. Let $f_1, \ldots, f_c \in \mathfrak m$ be an $M$-quasi-regular sequence. Then $f_1, \ldots, f_c$ is an $M$-regular sequence.

**Proof.** Set $J = (f_1, \ldots, f_c)$. Let us show that $f_1$ is a nonzerodivisor on $M$. Suppose $x \in M$ is not zero. By Krull's intersection theorem there exists an integer $r$ such that $x \in J^rM$ but $x \not \in J^{r + 1}M$, see Lemma [Krull's intersection theorem](#native-algebra-lemma-intersect-powers-ideal-module-zero). Then $f_1 x \in J^{r + 1}M$ is an element whose class in $J^{r + 1}M/J^{r + 2}M$ is nonzero by the assumed structure of $\bigoplus J^nM/J^{n + 1}M$. Whence $f_1x \not = 0$.

Now we can finish the proof by induction on $c$ using Lemma [Regular rings](#native-algebra-lemma-truncate-quasi-regular). $\square$

#### Lemma. Height and dimension in a polynomial ring

Let $k$ be a field. Let $\mathfrak p \subset \mathfrak q \subset k[x_1, \ldots, x_n]$ be a pair of primes. Any maximal chain of primes between $\mathfrak p$ and $\mathfrak q$ has length $\text{height}(\mathfrak q) - \text{height}(\mathfrak p)$.

**Proof.** By Proposition [Dimension, codimension and finite algebras](#native-algebra-proposition-finite-gl-dim-polynomial-ring) any local ring of $k[x_1, \ldots, x_n]$ is regular. Hence all local rings are Cohen-Macaulay, see Lemma [Regular rings are Cohen–Macaulay](#native-algebra-lemma-regular-ring-cm). The local rings at maximal ideals have dimension $n$ hence every maximal chain of primes in $k[x_1, \ldots, x_n]$ has length $n$, see Lemma [Maximal prime chains in a Cohen–Macaulay ring](#native-algebra-lemma-maximal-chain-cm). Hence every maximal chain of primes between $(0)$ and $\mathfrak p$ has length $\text{height}(\mathfrak p)$, see Lemma [Dimension and codimension](#native-algebra-lemma-cm-dim-formula) for example. Putting these together leads to the assertion of the lemma. $\square$

#### Lemma. Noether normalization

Noether normalization

Let $k$ be a field. Let $S = k[x_1, \ldots, x_n]/I$ for some ideal $I$. If $I \neq (1)$, there exist $r\geq 0$, and $y_1, \ldots, y_r \in k[x_1, \ldots, x_n]$ such that (a) the map $k[y_1, \ldots, y_r] \to S$ is injective where the source is the polynomial ring on $y_1, \ldots, y_r$, and (b) the map $k[y_1, \ldots, y_r] \to S$ is finite. In this case the integer $r$ is the dimension of $S$. Moreover we may choose $y_i$ to be in the $\mathbf{Z}$-subalgebra of $k[x_1, \ldots, x_n]$ generated by $x_1, \ldots, x_n$.

**Proof.** By induction on $n$, with $n = 0$ being trivial. If $I = 0$, then take $r = n$ and $y_i = x_i$. If $I \not = 0$, then choose $y_1, \ldots, y_{n-1}$ as in Lemma [The equational criterion for a single module relation](#native-algebra-lemma-one-relation). Let $S' \subset S$ be the subring generated by the images of the $y_i$. By induction we can choose $r$ and $z_1, \ldots, z_r \in k[y_1, \ldots, y_{n-1}]$ such that (a), (b) hold for $k[z_1, \ldots, z_r]
\to S'$. Since $S' \to S$ is injective and finite we see (a), (b) hold for $k[z_1, \ldots, z_r]
\to S$. The assertion that $r = \dim(S)$ follows from Lemma [Dimension, codimension and integral extensions](#native-algebra-lemma-integral-sub-dim-equal). $\square$

#### Proposition. Dimension and codimension

Let $R$ be a local Noetherian ring. Let $d \geq 0$ be an integer. The following are equivalent:

1.   $\dim(R) = d$,

2.   $d(R) = d$,

3.   there exists an ideal of definition generated by $d$ elements, and no ideal of definition is generated by fewer than $d$ elements.

**Proof.** This proof is really just the same as the proof of Lemma [Dimension and codimension](#native-algebra-lemma-height-1). We will prove the proposition by induction on $d$. By Lemmas [Dimension and codimension](#native-algebra-lemma-dimension-0-d-0) and [Dimension and codimension](#native-algebra-lemma-height-1) we may assume that $d > 1$. Denote the minimal number of generators for an ideal of definition of $R$ by $d'(R)$. We will prove the inequalities $\dim(R) \geq d'(R) \geq d(R) \geq \dim(R)$, and hence they are all equal.

First, assume that $\dim(R) = d$. Let $\mathfrak p_i$ be the minimal primes of $R$. According to Lemma [Irreducible components of a Noetherian spectrum](#native-algebra-lemma-noetherian-irreducible-components) there are finitely many. Hence we can find $x \in \mathfrak m$, $x \not \in \mathfrak p_i$, see Lemma [An elementary algebraic comparison](#native-algebra-lemma-silly). Note that every maximal chain of primes starts with some $\mathfrak p_i$, hence the dimension of $R/xR$ is at most $d-1$. By induction there are $x_2, \ldots, x_d$ which generate an ideal of definition in $R/xR$. Hence $R$ has an ideal of definition generated by (at most) $d$ elements.

Assume $d'(R) = d$. Let $I = (x_1, \ldots, x_d)$ be an ideal of definition. Note that $I^n/I^{n + 1}$ is a quotient of a direct sum of $\binom{d + n - 1}{d - 1}$ copies $R/I$ via multiplication by all degree $n$ monomials in $x_1, \ldots, x_d$. Hence $\text{length}_R(I^n/I^{n + 1})$ is bounded by a polynomial of degree $d-1$. Thus $d(R) \leq d$.

Assume $d(R) = d$. Consider a chain of primes $\mathfrak p \subset \mathfrak q \subset
\mathfrak q_2 \subset \ldots \subset \mathfrak q_e = \mathfrak m$, with all inclusions strict, and $e \geq 2$. Pick some ideal of definition $I \subset R$. We will repeatedly use Lemma [Commutative algebra](#native-algebra-lemma-hilbert-ses-chi). First of all it implies, via the exact sequence $0 \to \mathfrak p \to R \to R/\mathfrak p \to 0$, that $d(R/\mathfrak p) \leq d$. But it clearly cannot be zero. Pick $x\in \mathfrak q$, $x\not \in \mathfrak p$. Consider the short exact sequence $$0 \to R/\mathfrak p \xrightarrow{x} R/\mathfrak p \to R/(xR + \mathfrak p) \to 0.$$ This implies that $\chi_{I, R/\mathfrak p} - \chi_{I, R/\mathfrak p}
- \chi_{I, R/(xR + \mathfrak p)} = - \chi_{I, R/(xR + \mathfrak p)}$ has degree $< d$. In other words, $d(R/(xR + \mathfrak p)) \leq d - 1$, and hence $\dim(R/(xR + \mathfrak p)) \leq d - 1$, by induction. Now $R/(xR + \mathfrak p)$ has the chain of prime ideals $\mathfrak q/(xR + \mathfrak p) \subset \mathfrak q_2/(xR + \mathfrak p)
\subset \ldots \subset \mathfrak q_e/(xR + \mathfrak p)$ which gives $e - 1 \leq d - 1$. Since we started with an arbitrary chain of primes this proves that $\dim(R) \leq d(R)$.

Reading back the reader will see we proved the circular inequalities as desired. $\square$

#### Lemma. Criteria for a separable field extension

Let $k$ be a field of characteristic $p > 0$. Let $K/k$ be a field extension. The following are equivalent:

1.  $K$ is separable over $k$,

2.  for every $k$-linearly independent subset $\{a_1, \ldots, a_m\}$ of $K$ the set $\{a^p_1, \ldots, a_m^p\}$ is $k$-linearly independent,

3.  the ring $K \otimes_k k^{1/p}$ is reduced, and

4.  $K$ is geometrically reduced over $k$.

**Proof.** The implication (1) $\Rightarrow$ (4) follows from Lemma [Field extensions](#native-algebra-lemma-separable-extension-preserves-reducedness). The implication (4) $\Rightarrow$ (3) is immediate.

Assume (3). Consider the ring homomorphism $m : K \otimes_k k^{1/p} \rightarrow K$ given by $$\lambda \otimes \mu \rightarrow \lambda^p \mu^p$$ Note that $x^p = m(x) \otimes 1$ for all $x \in K \otimes_k k^{1/p}$. Since $K \otimes_k k^{1/p}$ is reduced we see $m$ is injective. If $\{a_1, \ldots, a_m\} \subset K$ is $k$-linearly independent, then $\{a_1 \otimes 1, \ldots, a_m \otimes 1\}$ is $k^{1/p}$-linearly independent. By injectivity of $m$ we deduce that no nontrivial $k$-linear combination of $a_1^p, \ldots, a_m^p$ is is zero. Hence (3) implies (2).

Assume (2). To prove (1) we may assume that $K$ is finitely generated over $k$ and we have to prove that $K$ is separably generated over $k$. Let $\{x_1, \ldots, x_d\}$ be a transcendence base of $K/k$. By Fields, Lemma [Finite algebras (programme binding)](#uncovered-fields-lemma-algebraic-finitely-generated) we have $[K : K'] < \infty$ where $K' = k(x_1, \ldots, x_d)$. Choose the transcendence base such that the degree of inseparability $[K : K']_i$ is minimal. If $K / K'$ is separable then we win. Assume this is not the case to get a contradiction. Then there exists $x_{d + 1} \in K$ which is not separable over $K'$, and in particular $[K'(x_{d+1}) : K']_i > 1$. Then by Lemma [An elementary separability criterion](#native-algebra-lemma-mini-separability) there is $1 \leq j \leq n + 1$ such that $K'' = k(x_1, \ldots, \widehat{x}_j, \ldots, x_{d+1})$ satisfies $[K'(x_{d+1}) : K'']_i = 1$. By multiplicativity $[K : K'']_i < [K : K']_i$ and we obtain the contradiction. $\square$

#### Lemma. Formal smoothness over a prime field

Formally smooth equals separable for field extensions.

Let $k$ be a field.

1.  If the characteristic of $k$ is zero, then any extension field of $k$ is formally smooth over $k$.

2.  If the characteristic of $k$ is $p > 0$, then $K/k$ is formally smooth if and only if it is a separable field extension.

**Proof.** Combine Lemmas [A formally smooth field extension is separable](#native-algebra-lemma-formally-smooth-implies-separable) and [Elementary formally smooth extensions](#native-algebra-lemma-formally-smooth-extensions-easy). $\square$

#### Lemma. A formally smooth field extension is separable
 Let $K/k$ be an extension of fields. If $K$ is formally smooth over $k$, then $K$ is a separable extension of $k$.

**Proof.** Assume $K$ is formally smooth over $k$. If $k$ has characteristic zero, then $K/k$ is separable. Thus we may assume that $k$ has characteristic $p > 0$. By Lemma [Formal smoothness and smooth morphisms](#native-algebra-lemma-ses-formally-smooth) we see that $K \otimes_k \Omega_{k/\mathbf{F}_p} \to
\Omega_{K/\mathbf{F}_p}$ is injective. Hence $K$ is separable over $k$ by Lemma [Differentials of a separable field extension](#native-algebra-lemma-separable-differentials). $\square$

#### Lemma. Differentials of a separable field extension
 Let $k$ be a field of characteristic $p > 0$. Let $K/k$ be a field extension. The following are equivalent:

1.  the field extension $K/k$ is separable (see Definition [Separable field extensions](#native-algebra-definition-separable-field-extension)), and

2.  the map $K \otimes_k \Omega_{k/\mathbf{F}_p} \to \Omega_{K/\mathbf{F}_p}$ is injective.

**Proof.** Write $K$ as a directed colimit $K = \mathop{\operatorname{colim}}_i K_i$ of finitely generated field extensions $K_i/k$. By definition $K$ is separable if and only if each $K_i$ is separable over $k$, and by Lemma [Filtered limits and cotangent complexes and differentials](#native-algebra-lemma-colimit-differentials) we see that $K \otimes_k \Omega_{k/\mathbf{F}_p} \to \Omega_{K/\mathbf{F}_p}$ is injective if and only if each $K_i \otimes_k \Omega_{k/\mathbf{F}_p} \to \Omega_{K_i/\mathbf{F}_p}$ is injective. Hence we may assume that $K/k$ is a finitely generated field extension.

Assume \(K/k\) is a finitely generated field extension which is separable. Choose \(x_1, \ldots, x_{r + 1} \in K\) as in Lemma [Field extensions and finite algebras](#native-algebra-lemma-generating-finitely-generated-separable-field-extensions). In this case there exists an irreducible polynomial \(G(X_1, \ldots, X_{r + 1}) \in k[X_1, \ldots, X_{r + 1}]\) such that \(G(x_1, \ldots, x_{r + 1}) = 0\) and such that \(\partial G/\partial X_{r + 1}\) is not identically zero. Moreover \(K\) is the field of fractions of the domain \(S = k[X_1, \ldots, X_{r + 1}]/(G)\). Write 

\[
G = \sum a_I X^I, \quad X^I = X_1^{i_1}\ldots X_{r + 1}^{i_{r + 1}}.
\]

 Using the presentation of \(S\) above we see that 

\[
\Omega_{S/\mathbf{F}_p}
=
\frac{
S \otimes_k \Omega_{k/\mathbf{F}_p} \oplus
\bigoplus\nolimits_{i = 1, \ldots, r + 1} S\text{d}X_i
}{
\langle
\sum X^I \text{d}a_I + \sum \partial G/\partial X_i \text{d}X_i
\rangle
}
\]

 Since \(\Omega_{K/\mathbf{F}_p}\) is the localization of the \(S\)-module \(\Omega_{S/\mathbf{F}_p}\) (see Lemma [Cotangent complexes, differentials and local algebra](#native-algebra-lemma-differentials-localize)) we conclude that 

\[
\Omega_{K/\mathbf{F}_p}
=
\frac{
K \otimes_k \Omega_{k/\mathbf{F}_p} \oplus
\bigoplus\nolimits_{i = 1, \ldots, r + 1} K\text{d}X_i
}{
\langle
\sum X^I \text{d}a_I + \sum \partial G/\partial X_i \text{d}X_i
\rangle
}
\]

 Now, since the polynomial \(\partial G/\partial X_{r + 1}\) is not identically zero we conclude that the map \(K \otimes_k \Omega_{k/\mathbf{F}_p} \to \Omega_{K/\mathbf{F}_p}\) is injective as desired.

Assume $K/k$ is a finitely generated field extension and that $K \otimes_k \Omega_{k/\mathbf{F}_p} \to \Omega_{K/\mathbf{F}_p}$ is injective. (This part of the proof is the same as the argument proving Lemma [Criteria for a separable field extension](#native-algebra-lemma-characterize-separable-field-extensions).) Let $x_1, \ldots, x_r$ be a transcendence basis of $K$ over $k$ such that the degree of inseparability of the finite extension $k(x_1, \ldots, x_r) \subset K$ is minimal. If $K$ is separable over $k(x_1, \ldots, x_r)$ then we win. Assume this is not the case to get a contradiction. Then there exists an element $\alpha \in K$ which is not separable over $k(x_1, \ldots, x_r)$. Let $P(T) \in k(x_1, \ldots, x_r)[T]$ be its minimal polynomial. Because $\alpha$ is not separable actually $P$ is a polynomial in $T^p$. Clear denominators to get an irreducible polynomial $$G(X_1, \ldots, X_r, T) = \sum a_{I, i} X^I T^i \in k[X_1, \ldots, X_r, T]$$ such that $G(x_1, \ldots, x_r, \alpha) = 0$ in $K$. Note that this means $k[X_1, \ldots, X_r, T]/(G) \subset K$. We may assume that for some pair $(I_0, i_0)$ the coefficient $a_{I_0, i_0} = 1$. We claim that $\text{d}G/\text{d}X_i$ is not identically zero for at least one $i$. Namely, if this is not the case, then $G$ is actually a polynomial in $X_1^p, \ldots, X_r^p, T^p$. Then this means that $$\sum\nolimits_{(I, i) \not = (I_0, i_0)} x^I\alpha^i \text{d}a_{I, i}$$ is zero in $\Omega_{K/\mathbf{F}_p}$. Note that there is no $k$-linear relation among the elements $$\{x^I\alpha^i \mid a_{I, i} \not = 0 \text{ and } (I, i) \not = (I_0, i_0)\}$$ of $K$. Hence the assumption that $K \otimes_k \Omega_{k/\mathbf{F}_p} \to \Omega_{K/\mathbf{F}_p}$ is injective implies that $\text{d}a_{I, i} = 0$ in $\Omega_{k/\mathbf{F}_p}$ for all $(I, i)$. By Lemma [Polynomials with zero derivative in characteristic p](#native-algebra-lemma-derivative-zero-pth-power) we see that each $a_{I, i}$ is a $p$th power, which implies that $G$ is a $p$th power contradicting the irreducibility of $G$. Thus, after renumbering, we may assume that $\text{d}G/\text{d}X_1$ is not zero. Then we see that $x_1$ is separably algebraic over $k(x_2, \ldots, x_r, \alpha)$, and that $x_2, \ldots, x_r, \alpha$ is a transcendence basis of $K$ over $k$. This means that the degree of inseparability of the finite extension $k(x_2, \ldots, x_r, \alpha) \subset K$ is less than the degree of inseparability of the finite extension $k(x_1, \ldots, x_r) \subset K$, which is a contradiction. $\square$

#### Lemma. Polynomials with zero derivative in characteristic p
 Let $k$ be a perfect field of characteristic $p > 0$. Let $K/k$ be an extension. Let $a \in K$. Then $\text{d}a = 0$ in $\Omega_{K/k}$ if and only if $a$ is a $p$th power.

**Proof.** By Lemma [Filtered limits and cotangent complexes and differentials](#native-algebra-lemma-colimit-differentials) we see that there exists a subfield $k \subset L \subset K$ such that $L/k$ is a finitely generated field extension and such that $\text{d}a$ is zero in $\Omega_{L/k}$. Hence we may assume that $K$ is a finitely generated field extension of $k$.

Choose a transcendence basis $x_1, \ldots, x_r \in K$ such that $K$ is finite separable over $k(x_1, \ldots, x_r)$. This is possible by the definitions, see Definitions [Perfect complexes](#native-algebra-definition-perfect) and [Separable field extensions](#native-algebra-definition-separable-field-extension). We remark that the result holds for the purely transcendental subfield $k(x_1, \ldots, x_r) \subset K$. Namely, $$\Omega_{k(x_1, \ldots, x_r)/k} =
\bigoplus\nolimits_{i = 1}^r k(x_1, \ldots, x_r) \text{d}x_i$$ and any rational function all of whose partial derivatives are zero is a $p$th power. Moreover, we also have $$\Omega_{K/k} =
\bigoplus\nolimits_{i = 1}^r K\text{d}x_i$$ since $k(x_1, \ldots, x_r) \subset K$ is finite separable (computation omitted). Suppose $a \in K$ is an element such that $\text{d}a = 0$ in the module of differentials. By our choice of $x_i$ we see that the minimal polynomial $P(T) \in k(x_1, \ldots, x_r)[T]$ of $a$ is separable. Write $$P(T) = T^d + \sum\nolimits_{i = 1}^d a_i T^{d - i}$$ and hence $$0 = \text{d}P(a) = \sum\nolimits_{i = 1}^d a^{d - i}\text{d}a_i$$ in $\Omega_{K/k}$. By the description of $\Omega_{K/k}$ above and the fact that $P$ was the minimal polynomial of $a$, we see that this implies $\text{d}a_i = 0$. Hence $a_i = b_i^p$ for each $i$. Therefore by Fields, Lemma [Field extensions (programme binding)](#uncovered-fields-lemma-pth-root) we see that $a$ is a $p$th power. $\square$

#### Lemma. Noetherianity under finite-type base change

Let $R \to S$ be a ring map. Let $R \to R'$ be of finite type. If $S$ is Noetherian, then the base change $S' = R' \otimes_R S$ is Noetherian.

**Proof.** By Lemma [Base change for finite algebras](#native-algebra-lemma-base-change-finiteness) finite type is stable under base change. Thus $S \to S'$ is of finite type. Since $S$ is Noetherian we can apply Lemma [Permanence of Noetherian rings](#native-algebra-lemma-noetherian-permanence). $\square$

#### Lemma. Permanence of Noetherian rings

Noetherian property is stable by passage to finite type extension and localization.

Any finitely generated ring over a Noetherian ring is Noetherian. Any localization of a Noetherian ring is Noetherian.

**Proof.** The statement on localizations follows from the fact that any ideal $J \subset S^{-1}R$ is of the form $I \cdot S^{-1}R$. Any quotient $R/I$ of a Noetherian ring $R$ is Noetherian because any ideal $\overline{J} \subset R/I$ is of the form $J/I$ for some ideal $I \subset J \subset R$. Thus it suffices to show that if $R$ is Noetherian so is $R[X]$. Suppose $J_1 \subset J_2 \subset \ldots$ is an ascending chain of ideals in $R[X]$. Consider the ideals $I_{i, d}$ defined as the ideal of elements of $R$ which occur as leading coefficients of degree $d$ polynomials in $J_i$. Clearly $I_{i, d} \subset I_{i', d'}$ whenever $i \leq i'$ and $d \leq d'$. By the ascending chain condition in $R$ there are at most finitely many distinct ideals among all of the $I_{i, d}$. (Hint: Any infinite set of elements of $\mathbf{N} \times \mathbf{N}$ contains an increasing infinite sequence.) Take $i_0$ so large that $I_{i, d} = I_{i_0, d}$ for all $i \geq i_0$ and all $d$. Suppose $f \in J_i$ for some $i \geq i_0$. By induction on the degree $d = \deg(f)$ we show that $f \in J_{i_0}$. Namely, there exists a $g\in J_{i_0}$ whose degree is $d$ and which has the same leading coefficient as $f$. By induction $f - g \in J_{i_0}$ and we win. $\square$

#### Lemma. Obtaining a separable extension
 Let $K/k$ be a finitely generated field extension. There exists a diagram $$\begin{gathered}\begin{matrix}K & K' \\ k & k'\end{matrix} \\[6pt] \begin{aligned}K & \longrightarrow K' \\ k & \longrightarrow K \\ k & \longrightarrow k' \\ k' & \longrightarrow K'\end{aligned}\end{gathered}$$ where $k'/k$, $K'/K$ are finite purely inseparable field extensions such that $K'/k'$ is a separable field extension. In this situation we can assume that $K' = k'K$ is the compositum, and also that $K' = (k' \otimes_k K)_{red}$.

**Proof.** By Lemma [Commutative algebra](#native-algebra-lemma-make-separably-generated) we can find such a diagram with $K'/k'$ separably generated. By Lemma [Field extensions](#native-algebra-lemma-separably-generated-separable) this implies that $K'$ is separable over $k'$. The compositum $k'K$ is a subextension of $K'/k'$ and hence $k' \subset k'K$ is separable by Lemma [Field extensions](#native-algebra-lemma-subextensions-are-separable). The ring $(k' \otimes_k K)_{red}$ is a domain as for some $n \gg 0$ the map $x \mapsto x^{p^n}$ maps it into $K$. Hence it is a field by Lemma [Integral extensions and field extensions](#native-algebra-lemma-integral-over-field). Thus $(k' \otimes_k K)_{red} \to K'$ maps it isomorphically onto $k'K$. $\square$

#### Lemma. Descent of regularity
 Let $R \to S$ be a ring map. Assume that

1.  $R \to S$ is faithfully flat, and

2.  $S$ is a regular ring.

Then $R$ is a regular ring.

**Proof.** We see that $R$ is Noetherian by Lemma [Descent of Noetherianity](#native-algebra-lemma-descent-noetherian). Let $\mathfrak p \subset R$ be a prime. Choose a prime $\mathfrak q \subset S$ lying over $\mathfrak p$. Then Lemma [Flatness and regular ring maps](#native-algebra-lemma-flat-under-regular) applies to $R_\mathfrak p \to S_\mathfrak q$ and we conclude that $R_\mathfrak p$ is regular. Since $\mathfrak p$ was arbitrary we see $R$ is regular. $\square$

#### Lemma. Radical ideals under a surjection of spectra
 Let $\varphi : R \to S$ be a ring map. The following are equivalent:

1.  The map $\operatorname{Spec}(S) \to \operatorname{Spec}(R)$ is surjective.

2.  For any ideal $I \subset R$ the inverse image of $\sqrt{IS}$ in $R$ is equal to $\sqrt{I}$.

3.  For any radical ideal $I \subset R$ the inverse image of $IS$ in $R$ is equal to $I$.

4.  For every prime $\mathfrak p$ of $R$ the inverse image of $\mathfrak p S$ in $R$ is $\mathfrak p$.

In this case the same is true after any base change: Given a ring map $R \to R'$ the ring map $R' \to R' \otimes_R S$ has the equivalent properties (1), (2), (3) as well.

**Proof.** If $J \subset S$ is an ideal, then $\sqrt{\varphi^{-1}(J)} = \varphi^{-1}(\sqrt{J})$. This shows that (2) and (3) are equivalent. The implication (3) $\Rightarrow$ (4) is immediate. If $I \subset R$ is a radical ideal, then Lemma [The Zariski topology on an affine spectrum](#native-algebra-lemma-zariski-topology) guarantees that $I = \bigcap_{I \subset \mathfrak p} \mathfrak p$. Hence (4) $\Rightarrow$ (2). By Lemma [A point in the image of a spectrum map](#native-algebra-lemma-in-image) we have $\mathfrak p = \varphi^{-1}(\mathfrak p S)$ if and only if $\mathfrak p$ is in the image. Hence (1) $\Leftrightarrow$ (4). Thus (1), (2), (3), and (4) are equivalent.

Assume (1) holds. Let $R \to R'$ be a ring map. Let $\mathfrak p' \subset R'$ be a prime ideal lying over the prime $\mathfrak p$ of $R$. To see that $\mathfrak p'$ is in the image of $\operatorname{Spec}(R' \otimes_R S) \to \operatorname{Spec}(R')$ we have to show that $(R' \otimes_R S) \otimes_{R'} \kappa(\mathfrak p')$ is not zero, see Lemma [A point in the image of a spectrum map](#native-algebra-lemma-in-image). But we have $$(R' \otimes_R S) \otimes_{R'} \kappa(\mathfrak p') =
S \otimes_R \kappa(\mathfrak p)
\otimes_{\kappa(\mathfrak p)} \kappa(\mathfrak p')$$ which is not zero as $S \otimes_R \kappa(\mathfrak p)$ is not zero by assumption and $\kappa(\mathfrak p) \to \kappa(\mathfrak p')$ is an extension of fields. $\square$

#### Lemma. A reformulation of the local algebraic condition
 Let $R$ be a ring. Let $I \subset R$ be an ideal. Let $M$ be an $R$-module. If $M/IM$ is flat over $R/I$ and $\text{Tor}_1^R(R/I, M) = 0$ then

1.  $M/I^nM$ is flat over $R/I^n$ for all $n \geq 1$, and

2.  for any module $N$ which is annihilated by $I^m$ for some $m \geq 0$ we have $\text{Tor}_1^R(N, M) = 0$.

In particular, if $I$ is nilpotent, then $M$ is flat over $R$.

**Proof.** Assume $M/IM$ is flat over $R/I$ and $\text{Tor}_1^R(R/I, M) = 0$. Let $N$ be an $R/I$-module. Choose a set $\Lambda$ and a short exact sequence $$0 \to K \to \bigoplus\nolimits_{\lambda \in \Lambda} R/I \to N \to 0$$ By the long exact sequence of $\text{Tor}$ and the vanishing of $\text{Tor}_1^R(R/I, M)$ we get $$0 \to \text{Tor}_1^R(N, M) \to K \otimes_R M \to
(\bigoplus\nolimits_{\lambda \in \Lambda} R/I) \otimes_R M \to N \otimes_R M \to 0$$ But since $K$, $\bigoplus_{\lambda \in \Lambda} R/I$, and $N$ are all annihilated by $I$ we see that $$\begin{aligned}
K \otimes_R M & = K \otimes_{R/I} M/IM, \\
(\bigoplus\nolimits_{\lambda \in \Lambda} R/I) \otimes_R M & =
(\bigoplus\nolimits_{\lambda \in \Lambda} R/I) \otimes_{R/I} M/IM, \\
N \otimes_R M & = N \otimes_{R/I} M/IM.
\end{aligned}$$ As $M/IM$ is flat over $R/I$ we conclude that $$0 \to K \otimes_{R/I} M/IM \to
(\bigoplus\nolimits_{\lambda \in \Lambda} R/I) \otimes_{R/I} M/IM \to
N \otimes_{R/I} M/IM \to 0$$ is exact. Combining this with the above we conclude that $\text{Tor}_1^R(N, M) = 0$ for any $R$-module $N$ annihilated by $I$.

Let us prove (2) by induction on $m$. The case $m = 1$ was done in the previous paragraph. For $N$ annihilated by $I^m$ for $m > 1$ we may choose an exact sequence $0 \to N' \to N \to N'' \to 0$ with $N'$ and $N''$ annihilated by $I^{m - 1}$. For example one can take $N' = IN$ and $N'' = N/IN$. Then the exact sequence $$\text{Tor}_1^R(N', M) \to
\text{Tor}_1^R(N, M) \to
\text{Tor}_1^R(N'', M)$$ and induction prove the vanishing we want.

Finally, we prove (1). Given $n \geq 1$ we have to show that $M/I^nM$ is flat over $R/I^n$. In other words, we have to show that the functor $N \mapsto N \otimes_{R/I^n} M/I^nM$ is exact on the category of $R$-modules $N$ annihilated by $I^n$. However, for such $N$ we have $N \otimes_{R/I^n} M/I^nM = N \otimes_R M$. By the vanishing of $\text{Tor}_1$ in (2) we see that the functor $N \mapsto N \otimes_R M$ is exact on the category of $N$ annihilated by some power of $I$ and we conclude. $\square$

#### Remark. Tor for a quotient by an ideal
 The proof of Lemma [Criteria for flatness](#native-algebra-lemma-characterize-flat) actually shows that $$\text{Tor}_1^R(M, R/I)
=
\operatorname{Ker}(I \otimes_R M \to M).$$

#### Lemma. Finite modules over a finite ring extension

Let $R \to S$ be a finite ring map. Let $M$ be an $S$-module. Then $M$ is finite as an $R$-module if and only if $M$ is finite as an $S$-module.

**Proof.** One of the implications follows from Lemma [Finite algebras](#native-algebra-lemma-finite-over-subring). To see the other assume that $M$ is finite as an $S$-module. Pick $x_1, \ldots, x_n \in S$ which generate $S$ as an $R$-module. Pick $y_1, \ldots, y_m \in M$ which generate $M$ as an $S$-module. Then $x_i y_j$ generate $M$ as an $R$-module. $\square$

#### Lemma. Finitely many maximal ideals in an Artinian ring
 If $R$ is Artinian then $R$ has only finitely many maximal ideals.

**Proof.** Suppose that $\mathfrak m_i$, $i = 1, 2, 3, \ldots$ are pairwise distinct maximal ideals. Then $\mathfrak m_1 \supset \mathfrak m_1\cap \mathfrak m_2
\supset \mathfrak m_1 \cap \mathfrak m_2 \cap \mathfrak m_3 \supset \ldots$ is an infinite descending sequence (because by the Chinese remainder theorem all the maps $R \to \oplus_{i = 1}^n R/\mathfrak m_i$ are surjective). $\square$

#### Lemma. Nilpotence of the radical of an Artinian ring

Let $R$ be Artinian. The Jacobson radical of $R$ is a nilpotent ideal.

**Proof.** Let $I \subset R$ be the Jacobson radical. Note that $I \supset I^2 \supset I^3 \supset \ldots$ is a descending sequence. Thus $I^n = I^{n + 1}$ for some $n$. Set $J = \{ x\in R \mid xI^n = 0\}$. We have to show $J = R$. If not, choose an ideal $J' \not = J$, $J \subset J'$ minimal (possible by the Artinian property). Then $J'/J$ is a simple $R$-module, hence isomorphic to $R/\mathfrak m$ for some maximal ideal $\mathfrak m$, see Lemma [Criteria for commutative algebra](#native-algebra-lemma-characterize-length-1). Then $\mathfrak m I^n$ kills $J'$. Since $I \subset \mathfrak m$ we conclude that $I^{n + 1} = I^n$ kills $J'$. Hence $J' = J$ which is a contradiction. $\square$

#### Lemma. Vector-space dimension and module length
 Let $R$ be a ring with maximal ideal $\mathfrak m$. Suppose that $M$ is an $R$-module with $\mathfrak m M  =  0$. Then the length of $M$ as an $R$-module agrees with the dimension of $M$ as a $R/\mathfrak m$ vector space. The length is finite if and only if $M$ is a finite $R$-module.

**Proof.** The first part is a special case of Lemma [Independence of a composition series](#native-algebra-lemma-length-independent). Thus the length is finite if and only if $M$ has a finite basis as a $R/\mathfrak m$-vector space if and only if $M$ has a finite set of generators as an $R$-module. $\square$

#### Lemma. Extending a morphism after finite denominators are cleared
 Let $R$ be a ring. Let $\alpha : R^{\oplus n} \to M$ and $\beta : N \to M$ be module maps. If $\operatorname{Im}(\alpha) \subset \operatorname{Im}(\beta)$, then there exists an $R$-module map $\gamma : R^{\oplus n} \to N$ such that $\alpha = \beta \circ \gamma$.

**Proof.** Let $e_i = (0, \ldots, 0, 1, 0, \ldots, 0)$ be the $i$th basis vector of $R^{\oplus n}$. Let $x_i \in N$ be an element with $\alpha(e_i) = \beta(x_i)$ which exists by assumption. Set $\gamma(a_1, \ldots, a_n) = \sum a_i x_i$. By construction $\alpha = \beta \circ \gamma$. $\square$

#### Lemma. Smoothness at a generic point

Let $R \to S$ be an injective finite type ring map with $R$ and $S$ domains. Then $R \to S$ is smooth at $\mathfrak q = (0)$ if and only if the induced extension $L/K$ of fraction fields is separable.

**Proof.** Assume $R \to S$ is smooth at $(0)$. We may replace $S$ by $S_g$ for some nonzero $g \in S$ and assume that $R \to S$ is smooth. Then $K \to S \otimes_R K$ is smooth (Lemma [Base change of smooth ring maps](#native-algebra-lemma-base-change-smooth)). Moreover, for any field extension $K'/K$ the ring map $K' \to S \otimes_R K'$ is smooth as well. Hence $S \otimes_R K'$ is a regular ring by Lemma Smooth algebras over a field and the Jacobian criterion, Theorems 5.1–6.1 and Sections 1–3, in particular reduced. It follows that $S \otimes_R K$ is geometrically reduced over $K$. Hence $L$ is geometrically reduced over $K$, see Lemma [Commutative algebra](#native-algebra-lemma-geometrically-reduced-permanence). Hence $L/K$ is separable by Lemma [Criteria for a separable field extension](#native-algebra-lemma-characterize-separable-field-extensions).

Conversely, assume that $L/K$ is separable. We may assume $R \to S$ is of finite presentation, see Lemma [Finite presentation and finite algebras](#native-algebra-lemma-generic-finite-presentation). It suffices to prove that $K \to S \otimes_R K$ is smooth at $(0)$, see Lemma [The smooth locus under flat base change](#native-algebra-lemma-flat-base-change-locus-smooth). This follows from Lemma [Smooth morphisms and field extensions](#native-algebra-lemma-separable-smooth), the fact that a field is a regular ring, and the assumption that $L/K$ is separable. $\square$

#### Lemma. The quasi-finite open in an integral closure

Let $R \to S$ be a finite type ring map. Suppose that $S$ is quasi-finite over $R$. Let $S' \subset S$ be the integral closure of $R$ in $S$. Then

1.  $\operatorname{Spec}(S) \to \operatorname{Spec}(S')$ is a homeomorphism onto an open subset,

2.  if $g \in S'$ and $D(g)$ is contained in the image of the map, then $S'_g \cong S_g$, and

3.  there exists a finite $R$-algebra $S'' \subset S'$ such that (1) and (2) hold for the ring map $S'' \to S$.

**Proof.** Because $S/R$ is quasi-finite we may apply Theorem [Zariski's main theorem in affine algebra](#native-algebra-theorem-main-theorem) to each point $\mathfrak q$ of $\operatorname{Spec}(S)$. Since $\operatorname{Spec}(S)$ is quasi-compact, see Lemma [Quasi-compactness of an affine spectrum](#native-algebra-lemma-quasi-compact), we may choose a finite number of $g_i \in S'$, $i = 1, \ldots, n$ such that $S'_{g_i} = S_{g_i}$, and such that $g_1, \ldots, g_n$ generate the unit ideal in $S$ (in other words the standard opens of $\operatorname{Spec}(S)$ associated to $g_1, \ldots, g_n$ cover all of $\operatorname{Spec}(S)$).

Suppose that $D(g) \subset \operatorname{Spec}(S')$ is contained in the image. Then $D(g) \subset \bigcup D(g_i)$. In other words, $g_1, \ldots, g_n$ generate the unit ideal of $S'_g$. Note that $S'_{gg_i} \cong S_{gg_i}$ by our choice of $g_i$. Hence $S'_g \cong S_g$ by Lemma [A finite cover by affine localizations](#native-algebra-lemma-cover).

We construct a finite algebra $S'' \subset S'$ as in (3). To do this note that each $S'_{g_i} \cong S_{g_i}$ is a finite type $R$-algebra. For each $i$ pick some elements $y_{ij} \in S'$ such that each $S'_{g_i}$ is generated as $R$-algebra by $1/g_i$ and the elements $y_{ij}$. Then set $S''$ equal to the sub $R$-algebra of $S'$ generated by all $g_i$ and all the $y_{ij}$. Details omitted. $\square$

#### Lemma. Finiteness after completion
 Let $R \to S$ be a local homomorphism of local rings $(R, \mathfrak m)$ and $(S, \mathfrak n)$. Let $R^\wedge$, resp. $S^\wedge$ be the completion of $R$, resp. $S$ with respect to $\mathfrak m$, resp. $\mathfrak n$. If $\mathfrak m$ and $\mathfrak n$ are finitely generated and $\dim_{\kappa(\mathfrak m)} S/\mathfrak mS < \infty$, then

1.  $S^\wedge$ is equal to the $\mathfrak m$-adic completion of $S$, and

2.  $S^\wedge$ is a finite $R^\wedge$-module.

**Proof.** We have $\mathfrak mS \subset \mathfrak n$ because $R \to S$ is a local ring map. The assumption $\dim_{\kappa(\mathfrak m)} S/\mathfrak mS < \infty$ implies that $S/\mathfrak mS$ is an Artinian ring, see Lemma [Dimension, codimension and finite algebras](#native-algebra-lemma-finite-dimensional-algebra). Hence it has dimension $0$, see Lemma [Dimension, codimension and Noetherian rings](#native-algebra-lemma-noetherian-dimension-0), hence $\mathfrak n = \sqrt{\mathfrak mS}$. This and the fact that $\mathfrak n$ is finitely generated implies that $\mathfrak n^t \subset \mathfrak mS$ for some $t \geq 1$. By Lemma [Changing the ideal of completion](#native-algebra-lemma-change-ideal-completion) we see that $S^\wedge$ can be identified with the $\mathfrak m$-adic completion of $S$. As $\mathfrak m$ is finitely generated we see from Lemma [Finite algebras](#native-algebra-lemma-hathat-finitely-generated) that $S^\wedge$ and $R^\wedge$ are $\mathfrak m$-adically complete. At this point we may apply Lemma [Finite algebras over a complete ring](#native-algebra-lemma-finite-over-complete-ring) to $S^\wedge$ as an $R^\wedge$-module to conclude. $\square$

#### Proposition. Rings of dimension zero
 Let $R$ be a ring. The following are equivalent:

1.  $R$ is Artinian,

2.  $R$ is Noetherian and $\dim(R) \leq 0$,

3.  $R$ has finite length as a module over itself,

4.  $R$ is a finite product of Artinian local rings,

5.  $R$ is Noetherian and $\operatorname{Spec}(R)$ is a finite discrete topological space,

6.  $R$ is a finite product of Noetherian local rings of dimension $0$,

7.  $R$ is a finite product of Noetherian local rings $R_i$ with $d(R_i) = 0$,

8.  $R$ is a finite product of Noetherian local rings $R_i$ whose maximal ideals are nilpotent,

9.  $R$ is Noetherian, has finitely many maximal ideals and its Jacobson radical ideal is nilpotent, and

10. $R$ is Noetherian and there are no strict inclusions among its primes.

**Proof.** This is a combination of Lemmas [Local factors of a product ring](#native-algebra-lemma-product-local), [Finite length over an Artinian ring](#native-algebra-lemma-artinian-finite-length), [Dimension, codimension and Noetherian rings](#native-algebra-lemma-noetherian-dimension-0), and [Dimension and codimension](#native-algebra-lemma-dimension-0-d-0). $\square$

#### Lemma. Flatness and regular ring maps
 Let $R \to S$ be a local homomorphism of local Noetherian rings. Assume that $R \to S$ is flat and that $S$ is regular. Then $R$ is regular.

**Proof.** Let $\mathfrak m \subset R$ be the maximal ideal and let $\kappa = R/\mathfrak m$ be the residue field. Let $d = \dim S$. Choose any resolution $F_\bullet \to \kappa$ with each $F_i$ a finite free $R$-module. Set $K_d = \operatorname{Ker}(F_{d - 1} \to F_{d - 2})$. By flatness of $R \to S$ the complex $0 \to K_d \otimes_R S \to F_{d - 1} \otimes_R S \to \ldots
\to F_0 \otimes_R S \to \kappa \otimes_R S \to 0$ is still exact. Because the global dimension of $S$ is $d$, see Proposition [Regular rings and dimension and codimension](#native-algebra-proposition-finite-gl-dim-regular), we see that $K_d \otimes_R S$ is a finite free $S$-module (see also Lemma [Independence of a projective resolution](#native-algebra-lemma-independent-resolution)). By Lemma [Projective, locally free modules and finite algebras](#native-algebra-lemma-finite-projective-descends) we see that $K_d$ is a finite free $R$-module. Hence $\kappa$ has finite projective dimension and $R$ is regular by Proposition [Regular rings and dimension and codimension](#native-algebra-proposition-finite-gl-dim-regular). $\square$

#### Lemma. Noether normalization over a domain

Let $R \to S$ be an injective finite type ring map. Assume $R$ is a domain. Then there exists an integer $d$ and a factorization $$R \to R[y_1, \ldots, y_d] \to S' \to S$$ by injective maps such that $S'$ is finite over $R[y_1, \ldots, y_d]$ and such that $S'_f \cong S_f$ for some nonzero $f \in R$.

**Proof.** Pick $x_1, \ldots, x_n \in S$ which generate $S$ over $R$. Let $K$ be the fraction field of $R$ and $S_K = S \otimes_R K$. By Lemma [Noether normalization](#native-algebra-lemma-noether-normalization) we can find $y_1, \ldots, y_d \in S$ such that $K[y_1, \ldots, y_d] \to S_K$ is a finite injective map. Note that $y_i \in S$ because we may pick the $y_j$ in the $\mathbf{Z}$-algebra generated by $x_1, \ldots, x_n$. As a finite ring map is integral (see Lemma [Integral extensions and finite algebras](#native-algebra-lemma-finite-is-integral)) we can find monic $P_i \in K[y_1, \ldots, y_d][T]$ such that $P_i(x_i) = 0$ in $S_K$. Let $f \in R$ be a nonzero element such that $fP_i \in R[y_1, \ldots, y_d][T]$ for all $i$. Then $fP_i(x_i)$ maps to zero in $S_K$. Hence after replacing $f$ by another nonzero element of $R$ we may also assume $fP_i(x_i)$ is zero in $S$. Set $x_i' = fx_i$ and let $S' \subset S$ be the $R$-subalgebra generated by $y_1, \ldots, y_d$ and $x'_1, \ldots, x'_n$. Note that $x'_i$ is integral over $R[y_1, \ldots, y_d]$ as we have $Q_i(x_i') = 0$ where $Q_i = f^{\deg_T(P_i)}P_i(T/f)$ which is a monic polynomial in $T$ with coefficients in $R[y_1, \ldots, y_d]$ by our choice of $f$. Hence $R[y_1, \ldots, y_d] \subset S'$ is finite by Lemma [Criteria for integral extensions and finite algebras](#native-algebra-lemma-characterize-finite-in-terms-of-integral). Since $S' \subset S$ we have $S'_f \subset S_f$ (localization is exact). On the other hand, the elements $x_i = x'_i/f$ in $S'_f$ generate $S_f$ over $R_f$ and hence $S'_f \to S_f$ is surjective. Whence $S'_f \cong S_f$ and we win. $\square$

#### Lemma. Changing the ideal of completion
 Let $R$ be a ring. Let $I$, $J$ be ideals of $R$. Assume there exist integers $c, d > 0$ such that $I^c \subset J$ and $J^d \subset I$. Then completion with respect to $I$ agrees with completion with respect to $J$ for any $R$-module. In particular an $R$-module $M$ is $I$-adically complete if and only if it is $J$-adically complete.

**Proof.** Consider the system of maps $M/I^nM \to M/J^{\lfloor n/c \rfloor}M$ and the system of maps $M/J^mM \to M/I^{\lfloor m/d \rfloor}M$ to get mutually inverse maps between the completions. $\square$

#### Lemma. Finite algebras over a complete ring

Let $R$ be a ring. Let $I \subset R$ be an ideal. Let $M$ be an $R$-module. Assume

1.  $R$ is $I$-adically complete,

2.  $\bigcap_{n \geq 1} I^nM = (0)$, and

3.  $M/IM$ is a finite $R/I$-module.

Then $M$ is a finite $R$-module.

**Proof.** Let $x_1, \ldots, x_n \in M$ be elements whose images in $M/IM$ generate $M/IM$ as an $R/I$-module. Denote by $M' \subset M$ the $R$-submodule generated by $x_1, \ldots, x_n$. By Lemma [Complete rings and formal power series](#native-algebra-lemma-completion-generalities) the map $(M')^\wedge \to M^\wedge$ is surjective. Since $\bigcap I^nM = 0$ we see in particular that $\bigcap I^nM' = (0)$. Hence by Lemma [Complete rings, formal power series and modules](#native-algebra-lemma-when-finite-module-complete-over-complete-ring) we see that $M'$ is complete, and we conclude that $M' \to M^\wedge$ is surjective. Finally, the kernel of $M \to M^\wedge$ is zero since it is equal to $\bigcap I^nM = (0)$. Hence we conclude that $M \cong M' \cong M^\wedge$ is finitely generated. $\square$

#### Lemma. Dimension under an integral extension

Suppose that $R \to S$ is a ring map such that $S$ is integral over $R$. Then $\dim (R) \geq \dim(S)$, and every closed point of $\operatorname{Spec}(S)$ maps to a closed point of $\operatorname{Spec}(R)$.

**Proof.** Immediate from Lemmas [Incomparability for an integral ring map](#native-algebra-lemma-integral-no-inclusion) and [Commutative algebra](#native-algebra-lemma-going-up-maximal-on-top) and the definitions. $\square$

#### Lemma. Localizations at minimal primes of a reduced ring
 Let $\mathfrak p$ be a minimal prime of a ring $R$. Every element of the maximal ideal of $R_{\mathfrak p}$ is nilpotent. If $R$ is reduced then $R_{\mathfrak p}$ is a field.

**Proof.** If some element $x$ of ${\mathfrak p}R_{\mathfrak p}$ is not nilpotent, then $D(x) \not = \emptyset$, see Lemma [The Zariski topology on an affine spectrum](#native-algebra-lemma-zariski-topology). This contradicts the minimality of $\mathfrak p$. If $R$ is reduced, then ${\mathfrak p}R_{\mathfrak p} = 0$ and hence $R_{\mathfrak p}$ is a field. $\square$

#### Lemma. Geometric regularity over a subfield

Let $k$ be a field. Let $A$ be an algebra over $k$. Let $k = \mathop{\operatorname{colim}} k_i$ be a directed colimit of subfields. If $A$ is geometrically regular over each $k_i$, then $A$ is geometrically regular over $k$.

**Proof.** Let $k'/k$ be a finite purely inseparable field extension. We can get $k'$ by adjoining finitely many variables to $k$ and imposing finitely many polynomial relations. Hence we see that there exists an $i$ and a finite purely inseparable field extension $k_i'/k_i$ such that $k' = k \otimes_{k_i} k_i'$. Thus $A \otimes_k k' = A \otimes_{k_i} k_i'$ and the lemma is clear. $\square$

#### Lemma. Ascent of geometric regularity
 Let $k$ be a field. Let $A \to B$ be a smooth ring map of $k$-algebras. If $A$ is geometrically regular over $k$, then $B$ is geometrically regular over $k$.

**Proof.** Let $k'/k$ be a finitely generated field extension. Then $A \otimes_k k' \to B \otimes_k k'$ is a smooth ring map (Lemma [Base change of smooth ring maps](#native-algebra-lemma-base-change-smooth)) and $A \otimes_k k'$ is regular. Hence $B \otimes_k k'$ is regular by Lemma [Regularity ascends along a regular ring map](#native-algebra-lemma-regular-goes-up). $\square$

#### Definition. Formally smooth ring maps
 Let $R \to S$ be a ring map. We say $S$ is *formally smooth over $R$* if for every commutative solid diagram $$\begin{gathered}\begin{matrix}S & A/I \\ R & A\end{matrix} \\[6pt] \begin{aligned}S & \longrightarrow A/I \\ S & \dashrightarrow A \\ R & \longrightarrow A \\ R & \longrightarrow S \\ A & \longrightarrow A/I\end{aligned}\end{gathered}$$ where $I \subset A$ is an ideal of square zero, a dotted arrow exists which makes the diagram commute.

#### Lemma. Finite algebras

*Source credit:* the original source citation Matlis (Theorem 15). The slick proof given here is from an email of Bjorn Poonen dated Nov 5, 2016.

Let $R$ be a ring. Let $I$ be a finitely generated ideal of $R$. Let $M$ be an $R$-module. Then

1.  the completion $M^\wedge$ is $I$-adically complete, and

2.  $I^nM^\wedge = \operatorname{Ker}(M^\wedge \to M/I^nM) = (I^nM)^\wedge$ for all $n \geq 1$.

In particular $R^\wedge$ is $I$-adically complete, $I^nR^\wedge = (I^n)^\wedge$, and $R^\wedge/I^nR^\wedge = R/I^n$.

**Proof.** Since $I$ is finitely generated, $I^n$ is finitely generated, say by $f_1, \ldots, f_r$. Applying Lemma [Complete rings and formal power series](#native-algebra-lemma-completion-generalities) part (2) to the surjection $(f_1, \ldots, f_r) : M^{\oplus r} \to I^n M$ yields a surjection $$(M^\wedge)^{\oplus r} \xrightarrow{(f_1, \ldots, f_r)} (I^n M)^\wedge =
\varprojlim_{m \geq n} I^n M/I^m M = \operatorname{Ker}(M^\wedge \to M/I^n M).$$ On the other hand, the image of $(f_1, \ldots, f_r) : (M^\wedge)^{\oplus r} \to M^\wedge$ is $I^n M^\wedge$. Thus $M^\wedge / I^n M^\wedge \simeq M/I^n M$. Taking inverse limits yields $(M^\wedge)^\wedge \simeq M^\wedge$; that is, $M^\wedge$ is $I$-adically complete. $\square$

#### Lemma. Commutative algebra
 Let $\varphi : R \to S$ be a ring map. Assume

1.  $R$ is Noetherian,

2.  $S$ is Noetherian,

3.  $\varphi$ is flat,

4.  the fibre rings $S \otimes_R \kappa(\mathfrak p)$ have property $(R_k)$, and

5.  $R$ has property $(R_k)$.

Then $S$ has property $(R_k)$.

**Proof.** Let \(\mathfrak q\) be a prime of \(S\) lying over a prime \(\mathfrak p\) of \(R\). Assume that \(\dim(S_{\mathfrak q}) \leq k\). Since \(\dim(S_{\mathfrak q}) = \dim(R_{\mathfrak p}) + \dim(S_{\mathfrak q}/\mathfrak pS_{\mathfrak q})\) by Lemma [Dimension of a flat family](#native-algebra-lemma-dimension-base-fibre-equals-total) we see that \(\dim(R_{\mathfrak p}) \leq k\) and \(\dim(S_{\mathfrak q}/\mathfrak pS_{\mathfrak q}) \leq k\). Hence \(R_{\mathfrak p}\) and \(S_{\mathfrak q}/\mathfrak pS_{\mathfrak q}\) are regular by assumption. It follows that \(S_{\mathfrak q}\) is regular by Lemma [Regularity over a regular base with regular fibre](#native-algebra-lemma-flat-over-regular-with-regular-fibre). \(\square\)

#### Lemma. Filtered limits and finite presentation and modules
 Let $R$ be a ring and let $M$ be an $R$-module. Then $M$ is the colimit of a directed system $(M_i, \mu_{ij})$ of $R$-modules with all $M_i$ finitely presented $R$-modules.

**Proof.** Consider any finite subset $S \subset M$ and any finite collection of relations $E$ among the elements of $S$. So each $s \in S$ corresponds to $x_s \in M$ and each $e \in E$ consists of a vector of elements $f_{e, s} \in R$ such that $\sum f_{e, s} x_s = 0$. Let $M_{S, E}$ be the cokernel of the map $$R^{\# E} \longrightarrow R^{\# S}, \quad
(g_e)_{e\in E} \longmapsto (\sum g_e f_{e, s})_{s\in S}.$$ There are canonical maps $M_{S, E} \to M$. If $S \subset S'$ and if the elements of $E$ correspond, via this map, to relations in $E'$, then there is an obvious map $M_{S, E} \to M_{S', E'}$ commuting with the maps to $M$. Let $I$ be the set of pairs $(S, E)$ with ordering by inclusion as above. It is clear that the colimit of this directed system is $M$. $\square$

#### Lemma. Commutative algebra
 Let $$0 \to A_i \xrightarrow{f_i} B_i \xrightarrow{g_i} C_i \to 0$$ be an exact sequence of directed inverse systems of abelian groups over $I$. Suppose $I$ is countable. If $(A_i)$ is Mittag-Leffler, then $$0 \to \varprojlim A_i \to \varprojlim B_i \to \varprojlim C_i\to 0$$ is exact.

**Proof.** Taking limits of directed inverse systems is left exact, hence we only need to prove surjectivity of $\varprojlim B_i \to \varprojlim C_i$. So let $(c_i) \in \varprojlim
C_i$. For each $i \in I$, let $E_i = g_i^{-1}(c_i)$, which is nonempty since $g_i: B_i \to C_i$ is surjective. The system of maps $\varphi_{ji}: B_j
\to B_i$ for $(B_i)$ restrict to maps $E_j \to E_i$ which make $(E_i)$ into an inverse system of nonempty sets. It is enough to show that $(E_i)$ is Mittag-Leffler. For then Lemma [Commutative algebra](#native-algebra-lemma-ml-limit-nonempty) would show $\varprojlim E_i$ is nonempty, and taking any element of $\varprojlim E_i$ would give an element of $\varprojlim B_i$ mapping to $(c_i)$.

By the injection $f_i: A_i \to B_i$ we will regard $A_i$ as a subset of $B_i$. Since $(A_i)$ is Mittag-Leffler, if $i \in I$ then there exists $j \geq
i$ such that $\varphi_{ki}(A_k) = \varphi_{ji}(A_j)$ for $k \geq j$. We claim that also $\varphi_{ki}(E_k) = \varphi_{ji}(E_j)$ for $k \geq j$. Always $\varphi_{ki}(E_k) \subset \varphi_{ji}(E_j)$ for $k \geq j$. For the reverse inclusion let $e_j \in E_j$, and we need to find $x_k \in E_k$ such that $\varphi_{ki}(x_k) = \varphi_{ji}(e_j)$. Let $e'_k \in E_k$ be any element, and set $e'_j = \varphi_{kj}(e'_k)$. Then $g_j(e_j - e'_j) = c_j - c_j = 0$, hence $e_j - e'_j = a_j \in A_j$. Since $\varphi_{ki}(A_k) =
\varphi_{ji}(A_j)$, there exists $a_k \in A_k$ such that $\varphi_{ki}(a_k) =
\varphi_{ji}(a_j)$. Hence $$\varphi_{ki}(e'_k + a_k) = \varphi_{ji}(e'_j) + \varphi_{ji}(a_j) =
\varphi_{ji}(e_j),$$ so we can take $x_k = e'_k + a_k$. $\square$

#### Lemma. Proper morphisms and modules
 Let $R$ be a ring. Let $S \subset R$ be a multiplicative subset. Let $M$, $N$ be $R$-modules. Assume all the elements of $S$ act as automorphisms on $N$. Then the canonical map $$\operatorname{Hom}_R(S^{-1}M, N) \longrightarrow \operatorname{Hom}_R(M, N)$$ induced by the localization map, is an isomorphism.

**Proof.** It is clear that the map is well-defined and $R$-linear. Injectivity: Let $\alpha \in \operatorname{Hom}_R(S^{-1}M, N)$ and take an arbitrary element $m/s \in S^{-1}M$. Then, since $s \cdot \alpha(m/s) = \alpha(m/1)$, we have $\alpha(m/s) =s^{-1}(\alpha (m/1))$, so $\alpha$ is completely determined by what it does on the image of $M$ in $S^{-1}M$. Surjectivity: Let $\beta : M \rightarrow N$ be a given $R$-linear map. We need to show that it can be \"extended\" to $S^{-1}M$. Define a map of sets $$M \times S \rightarrow N,\quad
(m,s) \mapsto s^{-1}\beta(m)$$ Clearly, this map respects the equivalence relation from above, so it descends to a well-defined map $\alpha : S^{-1}M \rightarrow N$. It remains to show that this map is $R$-linear, so take $r, r' \in R$ as well as $s, s' \in S$ and $m, m' \in M$. Then $$\begin{aligned}
\alpha(r \cdot m/s + r' \cdot m' /s')
& =
\alpha((r \cdot s' \cdot m + r' \cdot s \cdot m') /(ss')) \\
& =
(ss')^{-1}\beta(r \cdot s' \cdot m + r' \cdot s \cdot m') \\
& =
(ss')^{-1} (r \cdot s' \beta (m) + r' \cdot s \beta (m')) \\
& =
r \alpha (m/s) + r' \alpha (m' /s')
\end{aligned}$$ and we win. $\square$

#### Lemma. Tensor products and direct sums
 Let $R$ be a ring. Let $A_1 \to A_0$ and $B_1 \to B_0$ be two term complexes. Suppose that there exist morphisms of complexes $\varphi : A_\bullet \to B_\bullet$ and $\psi : B_\bullet \to A_\bullet$ such that $\varphi \circ \psi$ and $\psi \circ \varphi$ are homotopic to the identity maps. Then $A_1 \oplus B_0 \cong B_1 \oplus A_0$ as $R$-modules.

**Proof.** Choose a map $h : A_0 \to A_1$ such that $$\text{id}_{A_1} - \psi_1 \circ \varphi_1 = h \circ d_A
\text{ and }
\text{id}_{A_0} - \psi_0 \circ \varphi_0 = d_A \circ h.$$ Similarly, choose a map $h' : B_0 \to B_1$ such that $$\text{id}_{B_1} - \varphi_1 \circ \psi_1 = h' \circ d_B
\text{ and }
\text{id}_{B_0} - \varphi_0 \circ \psi_0 = d_B \circ h'.$$ A trivial computation shows that $$\left(
\begin{matrix}
\text{id}_{A_1} & -\psi_1 \circ h' + h \circ \psi_0 \\
0 & \text{id}_{B_0}
\end{matrix}
\right)
=
\left(
\begin{matrix}
\psi_1 & h \\
-d_B & \varphi_0
\end{matrix}
\right)
\left(
\begin{matrix}
\varphi_1 & - h' \\
d_A & \psi_0
\end{matrix}
\right).$$ The product in the reverse order is also upper triangular with identity diagonal entries. Thus both products are invertible, so both factors are invertible and the lemma follows. $\square$

#### Lemma. Koszul complexes, regular sequences and regular rings
 Suppose that $R \to S$ is a flat and local ring homomorphism of Noetherian local rings. Denote by $\mathfrak m$ the maximal ideal of $R$. Suppose $f_1, \ldots, f_c$ is a sequence of elements of $S$ such that the images $\overline{f}_1, \ldots, \overline{f}_c$ form a regular sequence in $S/{\mathfrak m}S$. Then $f_1, \ldots, f_c$ is a regular sequence in $S$ and each of the quotients $S/(f_1, \ldots, f_i)$ is flat over $R$.

**Proof.** Induction and Lemma [Commutative algebra (programme binding)](#uncovered-algebra-lemma-grothendieck). $\square$

#### Lemma. Complete rings, formal power series and Noetherian rings
 Let $R$ be a ring. Let $S = R[x_1, \ldots, x_n]/(f_1, \ldots, f_c)$ be a relative global complete intersection (Definition [Relative global complete intersections](#native-algebra-definition-relative-global-complete-intersection)). There exists a finite type $\mathbf{Z}$-subalgebra $R_0 \subset R$ such that $f_i \in R_0[x_1, \ldots, x_n]$ and such that $$S_0 = R_0[x_1, \ldots, x_n]/(f_1, \ldots, f_c)$$ is a relative global complete intersection.

**Proof.** Let $R_0 \subset R$ be the $\mathbf{Z}$-algebra of $R$ generated by all the coefficients of the polynomials $f_1, \ldots, f_c$. Let $S_0 = R_0[x_1, \ldots, x_n]/(f_1, \ldots, f_c)$. Clearly, $S = R \otimes_{R_0} S_0$. Pick a prime $\mathfrak q \subset S$ and denote by $\mathfrak p \subset R$, $\mathfrak q_0 \subset S_0$, and $\mathfrak p_0 \subset R_0$ the primes it lies over. Because $\dim (S \otimes_R \kappa(\mathfrak p) ) = n - c$ we also have $\dim (S_0 \otimes_{R_0} \kappa(\mathfrak p_0)) = n - c$, see Lemma [Dimension, codimension and field extensions](#native-algebra-lemma-dimension-preserved-field-extension). By Lemma [An open neighbourhood with bounded fibre dimension](#native-algebra-lemma-dimension-fibres-bounded-open-upstairs) there exists a $g \in S_0$, $g \not \in \mathfrak q_0$ such that all nonempty fibres of $R_0 \to (S_0)_g$ have dimension $\leq n - c$. As $\mathfrak q$ was arbitrary and $\operatorname{Spec}(S)$ quasi-compact, we can find finitely many $g_1, \ldots, g_m \in S_0$ such that (a) for $j = 1, \ldots, m$ the nonempty fibres of $R_0 \to (S_0)_{g_j}$ have dimension $\leq n - c$ and (b) the image of $\operatorname{Spec}(S) \to \operatorname{Spec}(S_0)$ is contained in $D(g_1) \cup \ldots \cup D(g_m)$. In other words, the images of $g_1, \ldots, g_m$ in $S = R \otimes_{R_0} S_0$ generate the unit ideal. After increasing $R_0$ we may assume that $g_1, \ldots, g_m$ generate the unit ideal in $S_0$. By (a) the nonempty fibres of $R_0 \to S_0$ all have dimension $\leq n - c$ and we conclude. $\square$

#### Lemma. Filtered limits and commutative algebra

Filtered colimits are exact. Directed colimits are exact.

Let $I$ be a directed set. Let $(L_i, \lambda_{ij})$, $(M_i, \mu_{ij})$, and $(N_i, \nu_{ij})$ be systems of $R$-modules over $I$. Let $\varphi_i : L_i \to M_i$ and $\psi_i : M_i \to N_i$ be morphisms of systems over $I$. Assume that for all $i \in I$ the sequence of $R$-modules $$\begin{gathered}\begin{matrix}L_i & M_i & N_i\end{matrix} \\[6pt] \begin{aligned}L_i & \xrightarrow{\varphi_i} M_i \\ M_i & \xrightarrow{\psi_i} N_i\end{aligned}\end{gathered}$$ is a complex with homology $H_i$. Then the $R$-modules $H_i$ form a system over $I$, the sequence of $R$-modules $$\begin{gathered}\begin{matrix}\mathop{\operatorname{colim}}_i L_i & \mathop{\operatorname{colim}}_i M_i & \mathop{\operatorname{colim}}_i N_i\end{matrix} \\[6pt] \begin{aligned}\mathop{\operatorname{colim}}_i L_i & \xrightarrow{\varphi} \mathop{\operatorname{colim}}_i M_i \\ \mathop{\operatorname{colim}}_i M_i & \xrightarrow{\psi} \mathop{\operatorname{colim}}_i N_i\end{aligned}\end{gathered}$$ is a complex as well, and denoting $H$ its homology we have $$H = \mathop{\operatorname{colim}}_i H_i.$$

**Proof.** It is clear that $\begin{gathered}\begin{matrix}\mathop{\operatorname{colim}}_i L_i & \mathop{\operatorname{colim}}_i M_i & \mathop{\operatorname{colim}}_i N_i\end{matrix} \\[6pt] \begin{aligned}\mathop{\operatorname{colim}}_i L_i & \xrightarrow{\varphi} \mathop{\operatorname{colim}}_i M_i \\ \mathop{\operatorname{colim}}_i M_i & \xrightarrow{\psi} \mathop{\operatorname{colim}}_i N_i\end{aligned}\end{gathered}$ is a complex. For each $i \in I$, there is a canonical $R$-module morphism $H_i \to H$ (sending each $[m] \in H_i = \operatorname{Ker}(\psi_i) / \operatorname{Im}(\varphi_i)$ to the residue class in $H = \operatorname{Ker}(\psi) / \operatorname{Im}(\varphi)$ of the image of $m$ in $\mathop{\operatorname{colim}}_i M_i$). These give rise to a morphism $\mathop{\operatorname{colim}}_i H_i \to H$. It remains to show that this morphism is surjective and injective.

We are going to repeatedly use the description of colimits over $I$ as in Lemma [Filtered limits and commutative algebra (uncovered prerequisite)](#uncovered-algebra-lemma-directed-colimit) without further mention. Let $h \in H$. Since $H = \operatorname{Ker}(\psi)/\operatorname{Im}(\varphi)$ we see that $h$ is the class mod $\operatorname{Im}(\varphi)$ of an element $[m]$ in $\operatorname{Ker}(\psi) \subset \mathop{\operatorname{colim}}_i M_i$. Choose an $i$ such that $[m]$ comes from an element $m \in M_i$. Choose a $j \geq i$ such that $\nu_{ij}(\psi_i(m)) = 0$ which is possible since $[m] \in \operatorname{Ker}(\psi)$. After replacing $i$ by $j$ and $m$ by $\mu_{ij}(m)$ we see that we may assume $m \in \operatorname{Ker}(\psi_i)$. This shows that the map $\mathop{\operatorname{colim}}_i H_i \to H$ is surjective.

Suppose that $h_i \in H_i$ has image zero in $H$. Since $H_i = \operatorname{Ker}(\psi_i)/\operatorname{Im}(\varphi_i)$ we may represent $h_i$ by an element $m \in \operatorname{Ker}(\psi_i) \subset M_i$. The assumption on the vanishing of $h_i$ in $H$ means that the class of $m$ in $\mathop{\operatorname{colim}}_i M_i$ lies in the image of $\varphi$. Hence there exists a $j \geq i$ and an $l \in L_j$ such that $\varphi_j(l) = \mu_{ij}(m)$. Clearly this shows that the image of $h_i$ in $H_j$ is zero. This proves the injectivity of $\mathop{\operatorname{colim}}_i H_i \to H$. $\square$

#### Lemma. Finite algebras
 Let $R \to S$ be a finite type ring map. Let $\mathfrak q \subset S$ be a prime. Let $\mathfrak p \subset R$ be the inverse image of $\mathfrak q$. Suppose that $\dim_{\mathfrak q}(S/R) = n$. There exists a $g \in S$, $g \not\in \mathfrak q$ such that $S_g$ is quasi-finite over a polynomial algebra $R[t_1, \ldots, t_n]$.

**Proof.** The ring $\overline{S} = S \otimes_R \kappa(\mathfrak p)$ is of finite type over $\kappa(\mathfrak p)$. Let $\overline{\mathfrak q}$ be the prime of $\overline{S}$ corresponding to $\mathfrak q$. By definition of the dimension of a topological space at a point there exists an open $U \subset \operatorname{Spec}(\overline{S})$ with $\overline{\mathfrak q} \in U$ and $\dim(U) = n$. Since the topology on $\operatorname{Spec}(\overline{S})$ is induced from the topology on $\operatorname{Spec}(S)$ (see Remark [Commutative algebra](#native-algebra-remark-fundamental-diagram)), we can find a $g \in S$, $g \not \in \mathfrak q$ with image $\overline{g} \in \overline{S}$ such that $D(\overline{g}) \subset U$. Thus after replacing $S$ by $S_g$ we see that $\dim(\overline{S}) = n$.

Next, choose generators $x_1, \ldots, x_N$ for $S$ as an $R$-algebra. By Lemma [Noether normalization](#native-algebra-lemma-noether-normalization) there exist elements $y_1, \ldots, y_n$ in the $\mathbf{Z}$-subalgebra of $S$ generated by $x_1, \ldots, x_N$ such that the map $R[t_1, \ldots, t_n] \to S$, $t_i \mapsto y_i$ has the property that $\kappa(\mathfrak p)[t_1, \ldots, t_n] \to \overline{S}$ is finite. In particular, $S$ is quasi-finite over $R[t_1, \ldots, t_n]$ at $\mathfrak q$. Hence, by Lemma [Finite algebras (programme binding)](#uncovered-algebra-lemma-quasi-finite-open) we may replace $S$ by $S_g$ for some $g\in S$, $g \not \in \mathfrak q$ such that $R[t_1, \ldots, t_n] \to S$ is quasi-finite. $\square$

#### Lemma. Dimension, codimension and finite algebras

A quasi-finite cover of affine n-space has dimension at most n.

Let $k$ be a field. Let $S$ be a finite type $k$-algebra. Suppose there is a quasi-finite $k$-algebra map $k[t_1, \ldots, t_n] \to S$. Then $\dim(S) \leq n$.

**Proof.** By Lemma [Dimension, codimension and affine neighbourhoods (uncovered prerequisite)](#uncovered-algebra-lemma-dim-affine-space) the dimension of any local ring of $k[t_1, \ldots, t_n]$ is at most $n$. Thus the result follows from Lemma [Dimension, codimension and finite algebras (programme binding)](#uncovered-algebra-lemma-dimension-inequality-quasi-finite). $\square$

#### Lemma. Dimension, codimension and field extensions

Let $k$ be a field. Let $S$ be a finite type $k$-algebra. Let $K/k$ be a field extension. Then $\dim(S) = \dim(K \otimes_k S)$.

**Proof.** By Lemma [Noether normalization](#native-algebra-lemma-noether-normalization) there exists a finite injective map $k[y_1, \ldots, y_d] \to S$ with $d = \dim(S)$. Since $K$ is flat over $k$ we also get a finite injective map $K[y_1, \ldots, y_d] \to K \otimes_k S$. The result follows from Lemma [Dimension, codimension and integral extensions](#native-algebra-lemma-integral-sub-dim-equal). $\square$

#### Lemma. Finite algebras
 Let $R$ be a ring. Let $\varphi : M \to N$ be a map of $R$-modules with $N$ a finite $R$-module. Then we have the equality $$\begin{aligned}
U & = \{\mathfrak p \subset R \mid
\varphi_{\mathfrak p} : M_{\mathfrak p} \to N_{\mathfrak p}
\text{ is surjective}\} \\
& = \{\mathfrak p \subset R \mid
\varphi \otimes \kappa(\mathfrak p) :
M \otimes \kappa(\mathfrak p) \to N \otimes \kappa(\mathfrak p)
\text{ is surjective}\}
\end{aligned}$$ and $U$ is an open subset of $\operatorname{Spec}(R)$. Moreover, for any $f \in R$ such that $D(f) \subset U$ the map $M_f \to N_f$ is surjective.

**Proof.** The equality in the displayed formula follows from Nakayama's lemma. Nakayama's lemma also implies that $U$ is open. See Lemma [Nakayama's lemma](#native-algebra-lemma-nak) especially part (3). If $D(f) \subset U$, then $M_f \to N_f$ is surjective on all localizations at primes of $R_f$, and hence it is surjective by Lemma [Detecting a zero module by localization](#native-algebra-lemma-characterize-zero-local). $\square$

#### Lemma. Locality of the complete-intersection condition
 Let $k$ be a field. Let $S$ be a local $k$-algebra essentially of finite type over $k$. The following are equivalent:

1.  $S$ is a complete intersection over $k$,

2.  for any surjection $R \to S$ with $R$ a regular local ring essentially of finite presentation over $k$ the ideal $\operatorname{Ker}(R \to S)$ can be generated by a regular sequence,

3.  for some surjection $R \to S$ with $R$ a regular local ring essentially of finite presentation over $k$ the ideal $\operatorname{Ker}(R \to S)$ can be generated by $\dim(R) - \dim(S)$ elements,

4.  there exists a global complete intersection $A$ over $k$ and a prime $\mathfrak a$ of $A$ such that $S \cong A_{\mathfrak a}$, and

5.  there exists a local complete intersection $A$ over $k$ and a prime $\mathfrak a$ of $A$ such that $S \cong A_{\mathfrak a}$.

**Proof.** It is clear that (2) implies (1) and (1) implies (3). It is also clear that (4) implies (5). Let us show that (3) implies (4). Thus we assume there exists a surjection $R \to S$ with $R$ a regular local ring essentially of finite presentation over $k$ such that the ideal $\operatorname{Ker}(R \to S)$ can be generated by $\dim(R) - \dim(S)$ elements. We may write $R = (k[x_1, \ldots, x_n]/J)_{\mathfrak q}$ for some $J \subset k[x_1, \ldots, x_n]$ and some prime $\mathfrak q \subset k[x_1, \ldots, x_n]$ with $J \subset \mathfrak q$. Let $I \subset k[x_1, \ldots, x_n]$ be the kernel of the map $k[x_1, \ldots, x_n] \to S$ so that $S \cong (k[x_1, \ldots, x_n]/I)_{\mathfrak q}$. By assumption $(I/J)_{\mathfrak q}$ is generated by $\dim(R) - \dim(S)$ elements. We conclude that $I_{\mathfrak q}$ can be generated by $\dim(k[x_1, \ldots, x_n]_{\mathfrak q}) - \dim(S)$ elements by Lemma [Commutative algebra (programme binding)](#uncovered-algebra-lemma-ci-well-defined). From Lemma [Local criteria for complete intersections](#native-algebra-lemma-lci) we see that for some $g \in k[x_1, \ldots, x_n]$, $g \not \in \mathfrak q$ the algebra $(k[x_1, \ldots, x_n]/I)_g$ is a global complete intersection and $S$ is isomorphic to a local ring of it.

To finish the proof of the lemma we have to show that (5) implies (2). Assume (5) and let $\pi : R \to S$ be a surjection with $R$ a regular local $k$-algebra essentially of finite type over $k$. By assumption we have $S = A_{\mathfrak a}$ for some local complete intersection $A$ over $k$. Choose a presentation $R = (k[y_1, \ldots, y_m]/J)_{\mathfrak q}$ with $J \subset \mathfrak q \subset k[y_1, \ldots, y_m]$. We may and do assume that $J$ is the kernel of the map $k[y_1, \ldots, y_m] \to R$. Let $I \subset k[y_1, \ldots, y_m]$ be the kernel of the map $k[y_1, \ldots, y_m] \to S = A_{\mathfrak a}$. Then $J \subset I$ and $(I/J)_{\mathfrak q}$ is the kernel of the surjection $\pi : R \to S$. So $S = (k[y_1, \ldots, y_m]/I)_{\mathfrak q}$.

By Lemma [Local algebra (uncovered prerequisite)](#uncovered-algebra-lemma-isomorphic-local-rings) we see that there exist $g \in A$, $g \not \in \mathfrak a$ and $g' \in k[y_1, \ldots, y_m]$, $g' \not \in \mathfrak q$ such that $A_g \cong (k[y_1, \ldots, y_m]/I)_{g'}$. After replacing $A$ by $A_g$ and $k[y_1, \ldots, y_m]$ by $k[y_1, \ldots, y_{m + 1}]$ we may assume that $A \cong k[y_1, \ldots, y_m]/I$. Consider the surjective maps of local rings $$k[y_1, \ldots, y_m]_{\mathfrak q} \to R \to S.$$ We have to show that the kernel of $R \to S$ is generated by a regular sequence. By Lemma [Local criteria for complete intersections](#native-algebra-lemma-lci) we know that $k[y_1, \ldots, y_m]_{\mathfrak q} \to A_{\mathfrak a} = S$ has this property (as $A$ is a local complete intersection over $k$). We win by Lemma [Commutative algebra (programme binding)](#uncovered-algebra-lemma-ci-well-defined). $\square$

#### Lemma. Dimension, codimension and field extensions
 Let $k$ be a field. Let $S$ be a finite type $k$-algebra. Let $X = \operatorname{Spec}(S)$. Let $\mathfrak p \subset S$ be a prime ideal, and let $x \in X$ be the corresponding point. Then we have $$\dim_x(X) = \dim(S_{\mathfrak p}) + \text{trdeg}_k\ \kappa(\mathfrak p).$$

**Proof.** By Lemma [Prime ideals and dimension in a polynomial ring](#native-algebra-lemma-dimension-prime-polynomial-ring) we know that $r = \text{trdeg}_k\ \kappa(\mathfrak p)$ is equal to the dimension of $V(\mathfrak p)$. Pick any maximal chain of primes $\mathfrak p \subset \mathfrak p_1 \subset \ldots \subset \mathfrak p_r$ starting with $\mathfrak p$ in $S$. This has length $r$ by Lemma [Dimension and codimension (programme binding)](#uncovered-algebra-lemma-dimension-spell-it-out). Let $\mathfrak q_j$, $j \in J$ be the minimal primes of $S$ which are contained in $\mathfrak p$. These correspond $1-1$ to minimal primes in $S_{\mathfrak p}$ via the rule $\mathfrak q_j \mapsto \mathfrak q_jS_{\mathfrak p}$. By Lemma [Dimension, codimension and field extensions (programme binding)](#uncovered-algebra-lemma-dimension-at-a-point-finite-type-over-field) we know that $\dim_x(X)$ is equal to the maximum of the dimensions of the rings $S/\mathfrak q_j$. For each $j$ pick a maximal chain of primes $\mathfrak q_j \subset \mathfrak p'_1 \subset \ldots \subset \mathfrak p'_{s(j)}
= \mathfrak p$. Then $\dim(S_{\mathfrak p}) = \max_{j \in J} s(j)$. Now, each chain $$\mathfrak q_j \subset \mathfrak p'_1 \subset \ldots \subset
\mathfrak p'_{s(j)} = \mathfrak p \subset
\mathfrak p_1 \subset \ldots \subset \mathfrak p_r$$ is a maximal chain in $S/\mathfrak q_j$, and by what was said before we have $\dim_x(X) = \max_{j \in J} r + s(j)$. The lemma follows. $\square$

#### Proposition. Dimension, codimension and finite algebras

*Source credit:* the original source citation FAC (Chapter III, §4, no. 68, Hilbert-syzygy vanishing of graded Ext, p. 261) the original source citation FAC (Chapter III, §5, no. 74, syzygy bound for the local rings of projective space, pp. 268--269)

The source uses Hilbert's syzygy theorem to conclude that for $S=K[t_0,\ldots,t_r]$ and finite $M$, its internal graded $\operatorname{Ext}^q_S(M,N)$ vanishes for $q>r+1$. The proposition below supplies the global-dimension statement; the internal-to-ordinary comparison is isolated in Lemma [Derived Hom, Ext and proper morphisms (uncovered prerequisite)](#uncovered-algebra-lemma-graded-ext-properties).

No. 74 applies the corresponding local bound on projective $r$-space: every finite module over a stalk has projective dimension at most $r$. Each standard chart is affine $r$-space, so this follows from the global dimension statement below and localization.

A polynomial algebra in $n$ variables over a field is a regular ring. It has global dimension $n$. All localizations at maximal ideals are regular local rings of dimension $n$.

**Proof.** By Lemma [Dimension, codimension and affine neighbourhoods (uncovered prerequisite)](#uncovered-algebra-lemma-dim-affine-space) all localizations $k[x_1, \ldots, x_n]_{\mathfrak m}$ at maximal ideals are regular local rings of dimension $n$. Hence we conclude by Lemma [Regular rings and dimension and codimension (programme binding)](#uncovered-algebra-lemma-finite-gl-dim-finite-dim-regular). $\square$

#### Lemma. Commutative algebra

Let $R$ be a Noetherian local ring. Let $M$ be a Cohen-Macaulay module over $R$. Suppose $g \in \mathfrak m$ is such that $\dim(\text{Supp}(M) \cap V(g))
= \dim(\text{Supp}(M)) - 1$. Then (a) $g$ is a nonzerodivisor on $M$, and (b) $M/gM$ is Cohen-Macaulay of depth one less.

**Proof.** Choose an $M$-regular sequence $f_1, \ldots, f_d$ with $d = \dim(\text{Supp}(M))$. If $g$ is good with respect to $(M, f_1, \ldots, f_d)$ we win by Lemma [Commutative algebra (programme binding)](#uncovered-algebra-lemma-good-element). In particular the lemma holds if $d = 1$. (The case $d = 0$ does not occur.) Assume $d > 1$. Choose an element $h \in R$ such that (i) $h$ is good with respect to $(M, f_1, \ldots, f_d)$, and (ii) $\dim(\text{Supp}(M) \cap V(h, g)) = d - 2$. To see $h$ exists, let $\{\mathfrak q_j\}$ be the (finite) set of minimal primes of the closed sets $\text{Supp}(M)$, $\text{Supp}(M)\cap V(f_1, \ldots, f_i)$, $i = 1, \ldots, d - 1$, and $\text{Supp}(M) \cap V(g)$. None of these $\mathfrak q_j$ is equal to $\mathfrak m$ and hence we may find $h \in \mathfrak m$, $h \not \in \mathfrak q_j$ by Lemma [An elementary algebraic comparison](#native-algebra-lemma-silly). It is clear that $h$ satisfies (i) and (ii). From Lemma [Commutative algebra (programme binding)](#uncovered-algebra-lemma-good-element) we conclude that $M/hM$ is Cohen-Macaulay. By (ii) we see that the pair $(M/hM, g)$ satisfies the induction hypothesis. Hence $M/(h, g)M$ is Cohen-Macaulay and $g : M/hM \to M/hM$ is injective. By Lemma [Commutative algebra (programme binding)](#uncovered-algebra-lemma-permute-xi) we see that $g : M \to M$ and $h : M/gM \to M/gM$ are injective. Combined with the fact that $M/(g, h)M$ is Cohen-Macaulay this finishes the proof. $\square$

#### Lemma. Commutative algebra

In a local Cohen-Macaulay ring, any maximal chain of prime ideals has length equal to the dimension.

Let $R$ be a Noetherian local ring. Assume there exists a Cohen-Macaulay module $M$ with $\operatorname{Spec}(R) = \text{Supp}(M)$. Then any maximal chain of prime ideals $\mathfrak p_0 \subset
\mathfrak p_1 \subset \ldots \subset \mathfrak p_n$ has length $n = \dim(R)$.

**Proof.** We will prove this by induction on $\dim(R)$. If $\dim(R) = 0$, then the statement is clear. Assume $\dim(R) > 0$. Then $n > 0$. Choose an element $x \in \mathfrak p_1$, with $x$ not in any of the minimal primes of $R$, and in particular $x \not \in \mathfrak p_0$. (See Lemma [An elementary algebraic comparison](#native-algebra-lemma-silly).) Then $\dim(R/xR) = \dim(R) - 1$ by Lemma [A single polynomial equation](#native-algebra-lemma-one-equation). The module $M/xM$ is Cohen-Macaulay over $R/xR$ by Proposition [Characterizations of Cohen–Macaulay modules](#native-algebra-proposition-cm-module) and Lemma [Commutative algebra (programme binding)](#uncovered-algebra-lemma-cm-over-quotient). The support of $M/xM$ is $\operatorname{Spec}(R/xR)$ by Lemma [Closed support (programme binding)](#uncovered-algebra-lemma-support-quotient). After replacing $x$ by $x^n$ for some $n$, we may assume that $\mathfrak p_1$ is an associated prime of $M/xM$, see Lemma [Prime spectra and associated points (uncovered prerequisite)](#uncovered-algebra-lemma-inherit-minimal-primes). By Lemma [Closed support (programme binding)](#uncovered-algebra-lemma-cm-ass-minimal-support) we conclude that $\mathfrak p_1/(x)$ is a minimal prime of $R/xR$. It follows that the chain $\mathfrak p_1/(x) \subset \ldots \subset \mathfrak p_n/(x)$ is a maximal chain of primes in $R/xR$. By induction we find that this chain has length $\dim(R/xR) = \dim(R) - 1$ as desired. $\square$

#### Lemma. Prime spectra, associated points and tensor products and direct sums
 Let $R$ be a ring, $I$ and $J$ two ideals and $\mathfrak p$ a prime ideal containing the product $IJ$. Then $\mathfrak{p}$ contains $I$ or $J$.

**Proof.** Assume the contrary and take $x \in I \setminus \mathfrak p$ and $y \in J \setminus \mathfrak p$. Their product is an element of $IJ \subset \mathfrak p$, which contradicts the assumption that $\mathfrak p$ was prime. $\square$

#### Lemma. Cotangent complexes and differentials

In diagram ([Commutative algebra](#context-algebra-equation-functorial-omega)), suppose that $S \to S'$ is surjective with kernel $I \subset S$, and assume that $R' = R$. Then there is a canonical exact sequence of $S'$-modules $$I/I^2
\longrightarrow
\Omega_{S/R} \otimes_S S'
\longrightarrow
\Omega_{S'/R}
\longrightarrow
0.$$ The leftmost map is characterized by the rule that $f \in I$ maps to $\text{d}f \otimes 1$.

**Proof.** The middle term is $\Omega_{S/R} \otimes_S S/I$. For $f \in I$ denote by $\overline{f}$ the image of $f$ in $I/I^2$. To show that the map $\overline{f} \mapsto \text{d}f \otimes 1$ is well defined we just have to check that $\text{d} f_1f_2 \otimes 1 = 0$ if $f_1, f_2 \in I$. And this is clear from the Leibniz rule $\text{d} f_1f_2 \otimes 1 = (f_1 \text{d}f_2 + f_2 \text{d} f_1 )\otimes 1 =
\text{d}f_2 \otimes f_1 + \text{d}f_1 \otimes f_2 = 0$. A similar computation shows this map is $S' = S/I$-linear.

The map $\Omega_{S/R} \otimes_S S' \to \Omega_{S'/R}$ is the canonical $S'$-linear map associated to the $S$-linear map $\Omega_{S/R} \to \Omega_{S'/R}$. It is surjective because $\Omega_{S/R} \to \Omega_{S'/R}$ is surjective by Lemma [Cotangent complexes and differentials (programme binding)](#uncovered-algebra-lemma-differential-surjective).

The composite of the two maps is zero because $\text{d}f$ maps to zero in $\Omega_{S'/R}$ for $f \in I$. Note that exactness just says that the kernel of $\Omega_{S/R} \to \Omega_{S'/R}$ is generated as an $S$-submodule by the submodule $I\Omega_{S/R}$ together with the elements $\text{d}f$, with $f \in I$. We know by Lemma [Cotangent complexes and differentials (programme binding)](#uncovered-algebra-lemma-differential-surjective) that this kernel is generated by the elements $\text{d}(a)$ where $\varphi(a) = \beta(r)$ for some $r \in R$. But then $a = \alpha(r) + a - \alpha(r)$, so $\text{d}(a) = \text{d}(a - \alpha(r))$. And $a - \alpha(r) \in I$ since $\varphi(a - \alpha(r)) =
\varphi(a) - \varphi(\alpha(r)) = \beta(r) - \beta(r) = 0$. We conclude the elements $\text{d}f$ with $f \in I$ already generate the kernel as an $S$-module, as desired. $\square$

#### Theorem. The Nullstellensatz (Hilbert Nullstellensatz)
 Let $k$ be a field.

1.   For any maximal ideal $\mathfrak m \subset k[x_1, \ldots, x_n]$ the field extension $\kappa(\mathfrak m)/k$ is finite.

2.   Any radical ideal $I \subset k[x_1, \ldots, x_n]$ is the intersection of maximal ideals containing it.

The same is true in any finite type $k$-algebra.

**Proof.** It is enough to prove part ([the indicated step](#native-algebra-item-finite-kappa)) of the theorem for the case of a polynomial algebra $k[x_1, \ldots, x_n]$, because any finitely generated $k$-algebra is a quotient of such a polynomial algebra. We prove this by induction on $n$. The case $n = 0$ is clear. Suppose that $\mathfrak m$ is a maximal ideal in $k[x_1, \ldots, x_n]$. Let $\mathfrak p \subset k[x_n]$ be the intersection of $\mathfrak m$ with $k[x_n]$.

If $\mathfrak p \not = (0)$, then $\mathfrak p$ is maximal and generated by an irreducible monic polynomial $P$ (because of the Euclidean algorithm in $k[x_n]$). Then $k' = k[x_n]/\mathfrak p$ is a finite field extension of $k$ and contained in $\kappa(\mathfrak m)$. In this case we get a surjection $$k'[x_1, \ldots, x_{n-1}]
\to
k'[x_1, \ldots, x_n] =
k' \otimes_k k[x_1, \ldots, x_n]
\longrightarrow
\kappa(\mathfrak m)$$ and hence we see that $\kappa(\mathfrak m)$ is a finite extension of $k'$ by induction hypothesis. Thus $\kappa(\mathfrak m)$ is finite over $k$ as well.

If $\mathfrak p = (0)$ we consider the ring extension $k[x_n] \subset k[x_1, \ldots, x_n]/\mathfrak m$. This is a finitely generated ring extension, hence of finite presentation by Lemmas [Noetherian rings (programme binding)](#uncovered-algebra-lemma-obvious-noetherian) and [Finite presentation and Noetherian rings (programme binding)](#uncovered-algebra-lemma-noetherian-finite-type-is-finite-presentation). Thus the image of $\operatorname{Spec}(k[x_1, \ldots, x_n]/\mathfrak m)$ in $\operatorname{Spec}(k[x_n])$ is constructible by Theorem [Chevalley's constructibility theorem](#native-algebra-theorem-chevalley). Since the image contains $(0)$ we conclude that it contains a standard open $D(f)$ for some $f\in k[x_n]$ nonzero. Since clearly $D(f)$ is infinite we get a contradiction with the assumption that $k[x_1, \ldots, x_n]/\mathfrak m$ is a field (and hence has a spectrum consisting of one point).

Proof of ([the indicated step](#native-algebra-item-polynomial-ring-jacobson)). Let $I \subset R$ be a radical ideal, with $R$ of finite type over $k$. Let $f \in R$, $f \not \in I$. We have to find a maximal ideal $\mathfrak m \subset R$ with $I \subset \mathfrak m$ and $f \not \in \mathfrak m$. The ring $(R/I)_f$ is nonzero, since $1 = 0$ in this ring would mean $f^n \in I$ and since $I$ is radical this would mean $f \in I$ contrary to our assumption on $f$. Thus we may choose a maximal ideal $\mathfrak m'$ in $(R/I)_f$, see Lemma [The Zariski topology on an affine spectrum](#native-algebra-lemma-zariski-topology). Let $\mathfrak m \subset R$ be the inverse image of $\mathfrak m'$ in $R$. We see that $I \subset \mathfrak m$ and $f \not \in \mathfrak m$. If we show that $\mathfrak m$ is a maximal ideal of $R$, then we are done. We clearly have $$k \subset R/\mathfrak m \subset \kappa(\mathfrak m').$$ By part ([the indicated step](#native-algebra-item-finite-kappa)) the field extension $\kappa(\mathfrak m')/k$ is finite. Hence $R/\mathfrak m$ is a field by Fields, Lemma [Field extensions (programme binding)](#uncovered-fields-lemma-subalgebra-algebraic-extension-field). Thus $\mathfrak m$ is maximal and the proof is complete. $\square$

#### Lemma. Flatness and local algebra
 Let $$\begin{gathered}\begin{matrix}S & S' \\ R & R'\end{matrix} \\[6pt] \begin{aligned}S & \longrightarrow S' \\ R & \longrightarrow R' \\ R & \longrightarrow S \\ R' & \longrightarrow S'\end{aligned}\end{gathered}$$ be a commutative diagram of local homomorphisms of local Noetherian rings. Let $I \subset R$ be a proper ideal. Let $M$ be a finite $S$-module. Denote by $I' = IR'$ and $M' = M \otimes_S S'$. Assume that

1.  $S'$ is a localization of the tensor product $S \otimes_R R'$,

2.  $M/IM$ is flat over $R/I$,

3.  $\text{Tor}_1^R(M, R/I) \to \text{Tor}_1^{R'}(M', R'/I')$ is zero.

Then $M'$ is flat over $R'$.

**Proof.** Since $S'$ is a localization of $S \otimes_R R'$ we see that $M'$ is a localization of $M \otimes_R R'$. Note that by Lemma [Base change of flat modules](#native-algebra-lemma-flat-base-change) the module $M/IM \otimes_{R/I} R'/I'
= M \otimes_R R' /I'(M \otimes_R R')$ is flat over $R'/I'$. Hence also $M'/I'M'$ is flat over $R'/I'$ as the localization of a flat module is flat. By Lemma [A variant of the local criterion for flatness](#native-algebra-lemma-variant-local-criterion-flatness) it suffices to show that $\text{Tor}_1^{R'}(M', R'/I')$ is zero. Since $M'$ is a localization of $M \otimes_R R'$, the last assumption implies that it suffices to show that $\text{Tor}_1^R(M, R/I) \otimes_R R'
\to
\text{Tor}_1^{R'}(M \otimes_R R', R'/I')$ is surjective.

By Lemma [Derived tensor products and Tor amplitude (programme binding)](#uncovered-algebra-lemma-surjective-on-tor-one-trivial) we see that $\text{Tor}_1^R(M, R'/I') \to \text{Tor}_1^{R'}(M \otimes_R R', R'/I')$ is surjective. So now it suffices to show that $\text{Tor}_1^R(M, R/I) \otimes_R R'
\to
\text{Tor}_1^R(M, R'/I')$ is surjective. This follows from Lemma [Derived tensor products and Tor amplitude (programme binding)](#uncovered-algebra-lemma-surjective-on-tor-one) by looking at the ring maps $R \to R/I \to R'/I'$ and the module $M$. $\square$

#### Lemma. Faithfully flat modules

A flat module is faithfully flat if and only if it has nonzero fibers.

Let $M$ be a flat $R$-module. The following are equivalent:

1.  $M$ is faithfully flat,

2.  for every nonzero $R$-module $N$, the tensor product $M \otimes_R N$ is nonzero,

3.  for all $\mathfrak p \in \operatorname{Spec}(R)$ the tensor product $M \otimes_R \kappa(\mathfrak p)$ is nonzero, and

4.  for all maximal ideals $\mathfrak m$ of $R$ the tensor product $M \otimes_R \kappa(\mathfrak m) = M/{\mathfrak m}M$ is nonzero.

**Proof.** Assume $M$ faithfully flat and $N \not = 0$. By Lemma [Commutative algebra (programme binding)](#uncovered-algebra-lemma-easy-ff) the nonzero map $1 : N \to N$ induces a nonzero map $M \otimes_R N \to M \otimes_R N$, so $M \otimes_R N \not = 0$. Thus (1) implies (2). The implications (2) $\Rightarrow$ (3) $\Rightarrow$ (4) are immediate.

Assume (4). Suppose that $N_1 \to N_2 \to N_3$ is a complex and suppose that $N_1 \otimes_R M \to N_2\otimes_R M \to
N_3\otimes_R M$ is exact. Let $H$ be the cohomology of the complex, so $H = \operatorname{Ker}(N_2 \to N_3)/\operatorname{Im}(N_1 \to N_2)$. To finish the proof we will show $H = 0$. By flatness we see that $H \otimes_R M = 0$. Take $x \in H$ and let $I = \{f \in R \mid fx = 0 \}$ be its annihilator. Since $R/I \subset H$ we get $M/IM \subset H \otimes_R M = 0$ by flatness of $M$. If $I \not =  R$ we may choose a maximal ideal $I \subset \mathfrak m \subset R$. This immediately gives a contradiction. $\square$

#### Remark. Commutative algebra
 A fundamental commutative diagram associated to a ring map $\varphi : R \to S$ and a prime $\mathfrak p \subset R$ is the following $$\begin{gathered}\begin{matrix}\kappa(\mathfrak p) \otimes_R S =
S_{\mathfrak p}/{\mathfrak p}S_{\mathfrak p} & S_{\mathfrak p} & S & S/\mathfrak pS & (R \setminus \mathfrak p)^{-1}S/\mathfrak pS \\ \kappa(\mathfrak p) =
R_{\mathfrak p}/{\mathfrak p}R_{\mathfrak p} & R_{\mathfrak p} & R & R/\mathfrak p & \kappa(\mathfrak p)\end{matrix} \\[6pt] \begin{aligned}S_{\mathfrak p} & \longrightarrow \kappa(\mathfrak p) \otimes_R S =
S_{\mathfrak p}/{\mathfrak p}S_{\mathfrak p} \\ S & \longrightarrow S/\mathfrak pS \\ S & \longrightarrow S_{\mathfrak p} \\ S/\mathfrak pS & \longrightarrow (R \setminus \mathfrak p)^{-1}S/\mathfrak pS \\ \kappa(\mathfrak p) =
R_{\mathfrak p}/{\mathfrak p}R_{\mathfrak p} & \longrightarrow \kappa(\mathfrak p) \otimes_R S =
S_{\mathfrak p}/{\mathfrak p}S_{\mathfrak p} \\ R_{\mathfrak p} & \longrightarrow S_{\mathfrak p} \\ R_{\mathfrak p} & \longrightarrow \kappa(\mathfrak p) =
R_{\mathfrak p}/{\mathfrak p}R_{\mathfrak p} \\ R & \longrightarrow S \\ R & \longrightarrow R/\mathfrak p \\ R & \longrightarrow R_{\mathfrak p} \\ R/\mathfrak p & \longrightarrow S/\mathfrak pS \\ R/\mathfrak p & \longrightarrow \kappa(\mathfrak p) \\ \kappa(\mathfrak p) & \longrightarrow (R \setminus \mathfrak p)^{-1}S/\mathfrak pS\end{aligned}\end{gathered}$$ In this diagram the outer left and outer right columns are identical. On spectra the horizontal maps induce homeomorphisms onto their images and the squares induce fibre squares of topological spaces (see Lemmas [The spectrum of a localization](#native-algebra-lemma-spec-localization) and [Closed subsets of an affine spectrum](#native-algebra-lemma-spec-closed)). This shows that $\mathfrak p$ is in the image of the map on Spec if and only if $S \otimes_R \kappa(\mathfrak p)$ is not the zero ring. If there does exist a prime $\mathfrak q \subset S$ lying over $\mathfrak p$, i.e., with $\mathfrak p = \varphi^{-1}(\mathfrak q)$ then we can extend the diagram to the following diagram $$\begin{gathered}\begin{matrix}\kappa(\mathfrak q) = S_{\mathfrak q}/{\mathfrak q}S_{\mathfrak q} & S_{\mathfrak q} & S & S/\mathfrak q & \kappa(\mathfrak q) \\ \kappa(\mathfrak p) \otimes_R S =
S_{\mathfrak p}/{\mathfrak p}S_{\mathfrak p} & S_{\mathfrak p} & S & S/\mathfrak pS & (R \setminus \mathfrak p)^{-1}S/\mathfrak pS \\ \kappa(\mathfrak p) =
R_{\mathfrak p}/{\mathfrak p}R_{\mathfrak p} & R_{\mathfrak p} & R & R/\mathfrak p & \kappa(\mathfrak p)\end{matrix} \\[6pt] \begin{aligned}S_{\mathfrak q} & \longrightarrow \kappa(\mathfrak q) = S_{\mathfrak q}/{\mathfrak q}S_{\mathfrak q} \\ S & \longrightarrow S/\mathfrak q \\ S & \longrightarrow S_{\mathfrak q} \\ S/\mathfrak q & \longrightarrow \kappa(\mathfrak q) \\ \kappa(\mathfrak p) \otimes_R S =
S_{\mathfrak p}/{\mathfrak p}S_{\mathfrak p} & \longrightarrow \kappa(\mathfrak q) = S_{\mathfrak q}/{\mathfrak q}S_{\mathfrak q} \\ S_{\mathfrak p} & \longrightarrow S_{\mathfrak q} \\ S_{\mathfrak p} & \longrightarrow \kappa(\mathfrak p) \otimes_R S =
S_{\mathfrak p}/{\mathfrak p}S_{\mathfrak p} \\ S & \longrightarrow S \\ S & \longrightarrow S/\mathfrak pS \\ S & \longrightarrow S_{\mathfrak p} \\ S/\mathfrak pS & \longrightarrow S/\mathfrak q \\ S/\mathfrak pS & \longrightarrow (R \setminus \mathfrak p)^{-1}S/\mathfrak pS \\ (R \setminus \mathfrak p)^{-1}S/\mathfrak pS & \longrightarrow \kappa(\mathfrak q) \\ \kappa(\mathfrak p) =
R_{\mathfrak p}/{\mathfrak p}R_{\mathfrak p} & \longrightarrow \kappa(\mathfrak p) \otimes_R S =
S_{\mathfrak p}/{\mathfrak p}S_{\mathfrak p} \\ R_{\mathfrak p} & \longrightarrow S_{\mathfrak p} \\ R_{\mathfrak p} & \longrightarrow \kappa(\mathfrak p) =
R_{\mathfrak p}/{\mathfrak p}R_{\mathfrak p} \\ R & \longrightarrow S \\ R & \longrightarrow R/\mathfrak p \\ R & \longrightarrow R_{\mathfrak p} \\ R/\mathfrak p & \longrightarrow S/\mathfrak pS \\ R/\mathfrak p & \longrightarrow \kappa(\mathfrak p) \\ \kappa(\mathfrak p) & \longrightarrow (R \setminus \mathfrak p)^{-1}S/\mathfrak pS\end{aligned}\end{gathered}$$ In this diagram it is still the case that the outer left and outer right columns are identical and that on spectra the horizontal maps induce homeomorphisms onto their image.

#### Lemma. An isolated point of an affine spectrum
 Let $k$ be a field. Let $S$ be a finite type $k$-algebra. Let $\mathfrak q$ be a prime of $S$. The following are equivalent:

1.  $\mathfrak q$ is an isolated point of $\operatorname{Spec}(S)$,

2.  $S_{\mathfrak q}$ is finite over $k$,

3.  there exists a $g \in S$, $g \not\in \mathfrak q$ such that $D(g) = \{ \mathfrak q \}$,

4.  $\dim_{\mathfrak q} \operatorname{Spec}(S) = 0$,

5.  $\mathfrak q$ is a closed point of $\operatorname{Spec}(S)$ and $\dim(S_{\mathfrak q}) = 0$, and

6.  the field extension $\kappa(\mathfrak q)/k$ is finite and $\dim(S_{\mathfrak q}) = 0$.

In this case $S = S_{\mathfrak q} \times S'$ for some finite type $k$-algebra $S'$. Also, the element $g$ as in (3) has the property $S_{\mathfrak q} = S_g$.

**Proof.** Suppose $\mathfrak q$ is an isolated point of $\operatorname{Spec}(S)$, i.e., $\{\mathfrak q\}$ is open in $\operatorname{Spec}(S)$. Because $\operatorname{Spec}(S)$ is a Jacobson space (see Lemmas [Field extensions and finite algebras (programme binding)](#uncovered-algebra-lemma-finite-type-field-jacobson) and [Commutative algebra (programme binding)](#uncovered-algebra-lemma-jacobson)) we see that $\mathfrak q$ is a closed point. Hence $\{\mathfrak q\}$ is open and closed in $\operatorname{Spec}(S)$. By Lemmas [Product decompositions from disjoint closed subsets](#native-algebra-lemma-disjoint-decomposition) and [A disjoint spectrum and a product of rings](#native-algebra-lemma-disjoint-implies-product) we may write $S = S_1 \times S_2$ with $\mathfrak q$ corresponding to the only point $\operatorname{Spec}(S_1)$. Hence $S_1 = S_{\mathfrak q}$ is a zero dimensional ring of finite type over $k$. Hence it is finite over $k$ for example by Lemma [Noether normalization](#native-algebra-lemma-noether-normalization). We have proved (1) implies (2).

Suppose $S_{\mathfrak q}$ is finite over $k$. Then $S_{\mathfrak q}$ is Artinian local, see Lemma [Dimension, codimension and finite algebras](#native-algebra-lemma-finite-dimensional-algebra). So $\operatorname{Spec}(S_{\mathfrak q}) = \{\mathfrak qS_{\mathfrak q}\}$ by Lemma [Finite length over an Artinian ring](#native-algebra-lemma-artinian-finite-length). Consider the exact sequence $0 \to K \to S \to S_{\mathfrak q}
\to Q \to 0$. It is clear that $K_{\mathfrak q} = Q_{\mathfrak q} = 0$. Also, $K$ is a finite $S$-module as $S$ is Noetherian and $Q$ is a finite $S$-module since $S_{\mathfrak q}$ is finite over $k$. Hence there exists $g \in S$, $g \not \in \mathfrak q$ such that $K_g = Q_g = 0$. Thus $S_{\mathfrak q} = S_g$ and $D(g) = \{ \mathfrak q \}$. We have proved that (2) implies (3).

Suppose $D(g) =  \{ \mathfrak q \}$. Since $D(g)$ is open by construction of the topology on $\operatorname{Spec}(S)$ we see that $\mathfrak q$ is an isolated point of $\operatorname{Spec}(S)$. We have proved that (3) implies (1). In other words (1), (2) and (3) are equivalent.

Assume $\dim_{\mathfrak q} \operatorname{Spec}(S) = 0$. This means that there is some open neighbourhood of $\mathfrak q$ in $\operatorname{Spec}(S)$ which has dimension zero. Then there is an open neighbourhood of the form $D(g)$ which has dimension zero. Since $S_g$ is Noetherian we conclude that $S_g$ is Artinian and $D(g) = \operatorname{Spec}(S_g)$ is a finite discrete set, see Proposition [Rings of dimension zero](#native-algebra-proposition-dimension-zero-ring). Thus $\mathfrak q$ is an isolated point of $D(g)$ and, by the equivalence of (1) and (2) above applied to $\mathfrak qS_g \subset S_g$, we see that $S_{\mathfrak q} = (S_g)_{\mathfrak qS_g}$ is finite over $k$. Hence (4) implies (2). It is clear that (1) implies (4). Thus (1) -- (4) are all equivalent.

Lemma [Dimension, codimension and field extensions (programme binding)](#uncovered-algebra-lemma-dimension-closed-point-finite-type-field) gives the implication (5) $\Rightarrow$ (4). The implication (4) $\Rightarrow$ (6) follows from Lemma [Dimension, codimension and field extensions](#native-algebra-lemma-dimension-at-a-point-finite-type-field). The implication (6) $\Rightarrow$ (5) follows from Lemma [Finite algebras (programme binding)](#uncovered-algebra-lemma-finite-residue-extension-closed). At this point we know (1) -- (6) are equivalent.

The two statements at the end of the lemma we saw during the course of the proof of the equivalence of (1), (2) and (3) above. $\square$

#### Lemma. Base change for finite algebras
 Let $R \to S$ be a ring map. Let $M$ be an $S$-module. Let $R \to R'$ be a ring map and let $S' = S \otimes_R R'$ and $M' = M \otimes_R R'$ be the base changes.

1.  If $M$ is a finite $S$-module, then the base change $M'$ is a finite $S'$-module.

2.  If $M$ is an $S$-module of finite presentation, then the base change $M'$ is an $S'$-module of finite presentation.

3.  If $R \to S$ is of finite type, then the base change $R' \to S'$ is of finite type.

4.  If $R \to S$ is of finite presentation, then the base change $R' \to S'$ is of finite presentation.

**Proof.** Proof of (1). Take a surjective, $S$-linear map $S^{\oplus n} \to M \to 0$. By Lemma [Tensor products and direct sums (uncovered prerequisite)](#uncovered-algebra-lemma-flip-tensor-product) and [Tensor products and direct sums](#native-algebra-lemma-tensor-product-exact) the result after tensoring with $R^\prime$ is a surjection ${S^\prime}^{\oplus n} \to M^\prime \rightarrow 0$, so $M^\prime$ is a finitely generated $S^\prime$-module. Proof of (2). Take a presentation $S^{\oplus m} \to S^{\oplus n} \to M \to 0$. By Lemma [Tensor products and direct sums (uncovered prerequisite)](#uncovered-algebra-lemma-flip-tensor-product) and [Tensor products and direct sums](#native-algebra-lemma-tensor-product-exact) the result after tensoring with $R^\prime$ gives a finite presentation ${S^\prime}^{\oplus m} \to {S^\prime}^{\oplus n} \to M^\prime \to 0$, of the $S^\prime$-module $M^\prime$. Proof of (3). This follows by the remark preceding the lemma as we can take $I$ to be finite by assumption. Proof of (4). This follows by the remark preceding the lemma as we can take $I$ and $J$ to be finite by assumption. $\square$

#### Lemma. Criteria for formal smoothness and smooth morphisms
 Let $R \to S$ be a ring map. Let $P \to S$ be a surjective $R$-algebra map from a polynomial ring $P$ onto $S$. Denote by $J \subset P$ the kernel. Then $R \to S$ is formally smooth if and only if there exists an $R$-algebra map $\sigma : S \to P/J^2$ which is a right inverse to the surjection $P/J^2 \to S$.

**Proof.** Assume $R \to S$ is formally smooth. Consider the commutative diagram $$\begin{gathered}\begin{matrix}S & P/J \\ R & P/J^2\end{matrix} \\[6pt] \begin{aligned}S & \longrightarrow P/J \\ S & \dashrightarrow P/J^2 \\ R & \longrightarrow P/J^2 \\ R & \longrightarrow S \\ P/J^2 & \longrightarrow P/J\end{aligned}\end{gathered}$$ By assumption the dotted arrow exists. This proves that $\sigma$ exists.

Conversely, suppose we have a $\sigma$ as in the lemma. Let a solid diagram $$\begin{gathered}\begin{matrix}S & A/I \\ R & A\end{matrix} \\[6pt] \begin{aligned}S & \longrightarrow A/I \\ S & \dashrightarrow A \\ R & \longrightarrow A \\ R & \longrightarrow S \\ A & \longrightarrow A/I\end{aligned}\end{gathered}$$ as in Definition [Formally smooth ring maps](#native-algebra-definition-formally-smooth) be given. Because $P$ is formally smooth by Lemma [Formal smoothness and smooth morphisms (programme binding)](#uncovered-algebra-lemma-polynomial-ring-formally-smooth), there exists an $R$-algebra homomorphism $\psi : P \to A$ which lifts the map $P \to S \to A/I$. Clearly $\psi(J) \subset I$ and since $I^2 = 0$ we conclude that $\psi(J^2) = 0$. Hence $\psi$ factors as $\overline{\psi} : P/J^2 \to A$. The desired dotted arrow is the composition $\overline{\psi} \circ \sigma : S \to A$. $\square$

#### Lemma. Criteria for formal smoothness and smooth morphisms
 Let $R \to S$ be a ring map. Let $P \to S$ be a surjective $R$-algebra map from a polynomial ring $P$ onto $S$. Denote by $J \subset P$ the kernel. Then $R \to S$ is formally smooth if and only if the sequence $$0 \to J/J^2 \to \Omega_{P/R} \otimes_P S \to \Omega_{S/R} \to 0$$ of Lemma [Cotangent complexes and differentials](#native-algebra-lemma-differential-seq) is a split exact sequence.

**Proof.** Assume $S$ is formally smooth over $R$. By Lemma [Criteria for formal smoothness and smooth morphisms](#native-algebra-lemma-characterize-formally-smooth) this means there exists an $R$-algebra map $S \to P/J^2$ which is a right inverse to the canonical map $P/J^2 \to S$. By Lemma [Cotangent complexes and differentials (programme binding)](#uncovered-algebra-lemma-differential-mod-power-ideal) we have $\Omega_{P/R} \otimes_P S = \Omega_{(P/J^2)/R} \otimes_{P/J^2} S$. By Lemma Kähler differentials, Theorems 3.1–3.3, Proposition 3.4 and Theorem 7.1 the sequence is split.

Assume the exact sequence of the lemma is split exact. Choose a splitting \(\sigma : \Omega_{S/R} \to \Omega_{P/R} \otimes_P S\). For each \(\lambda \in S\) choose \(x_\lambda \in P\) which maps to \(\lambda\). Next, for each \(\lambda \in S\) choose \(f_\lambda \in J\) such that 

\[
\text{d}f_\lambda = \text{d}x_\lambda - \sigma(\text{d}\lambda)
\]

 in the middle term of the exact sequence. We claim that \(s : \lambda \mapsto x_\lambda - f_\lambda \mod J^2\) is an \(R\)-algebra homomorphism \(s : S \to P/J^2\). To prove this we will repeatedly use that if \(h \in J\) and \(\text{d}h = 0\) in \(\Omega_{P/R} \otimes_P S\), then \(h \in J^2\). Let \(\lambda, \mu \in S\). Then \(\sigma(\text{d}\lambda + \text{d}\mu - \text{d}(\lambda + \mu)) = 0\). This implies 

\[
\text{d}(x_\lambda + x_\mu - x_{\lambda + \mu}
- f_\lambda - f_\mu + f_{\lambda + \mu}) = 0
\]

 which means that \(x_\lambda + x_\mu - x_{\lambda + \mu} - f_\lambda - f_\mu + f_{\lambda + \mu} \in J^2\), which in turn means that \(s(\lambda) + s(\mu) = s(\lambda + \mu)\). Similarly, we have \(\sigma(\lambda \text{d}\mu + \mu \text{d}\lambda - \text{d}(\lambda\mu)) = 0\) which implies that 

\[
\mu(\text{d}x_\lambda - \text{d}f_\lambda) +
\lambda(\text{d}x_\mu - \text{d}f_\mu) -
\text{d}x_{\lambda\mu} + \text{d}f_{\lambda\mu} = 0
\]

 in the middle term of the exact sequence. Moreover we have 

\[
\text{d}(x_\lambda x_\mu) =
x_\lambda \text{d}x_\mu + x_\mu \text{d}x_\lambda =
\lambda \text{d}x_\mu + \mu \text{d} x_\lambda
\]

 in the middle term again. Combined these equations mean that \(x_\lambda x_\mu - x_{\lambda\mu} - x_\mu f_\lambda - x_\lambda f_\mu + f_{\lambda\mu} \in J^2\), hence \((x_\lambda - f_\lambda)(x_\mu - f_\mu) - (x_{\lambda\mu} - f_{\lambda\mu}) \in J^2\) as \(f_\lambda f_\mu \in J^2\), which means that \(s(\lambda)s(\mu) = s(\lambda\mu)\). If \(\lambda \in R\), then \(\text{d}\lambda = 0\) and we see that \(\text{d}f_\lambda = \text{d}x_\lambda\), hence \(\lambda - x_\lambda + f_\lambda \in J^2\) and hence \(s(\lambda) = \lambda\) as desired. At this point we can apply Lemma [Criteria for formal smoothness and smooth morphisms](#native-algebra-lemma-characterize-formally-smooth) to conclude that \(S/R\) is formally smooth. \(\square\)

#### Lemma. Cotangent complexes and differentials

Let $A \to B$ be a surjective ring map with kernel $I$. Then $\mathrm{NL}_{B/A}$ is homotopy equivalent to the chain complex $(I/I^2 \to 0)$ with $I/I^2$ in degree $1$. In particular $H_1(L_{B/A}) = I/I^2$.

**Proof.** Follows from Lemma Kähler differentials, Theorems 3.1–3.3, Proposition 3.4 and Theorem 7.1 and the fact that $A \to B$ is a presentation of $B$ over $A$. $\square$

#### Lemma. Noetherian rings

Let $R$ be a Noetherian ring. Any finite $R$-module is of finite presentation. Any submodule of a finite $R$-module is finite. The ascending chain condition holds for $R$-submodules of a finite $R$-module.

**Proof.** We first show that any submodule $N$ of a finite $R$-module $M$ is finite. We do this by induction on the number of generators of $M$. If this number is $1$, then $N = J/I \subset
M = R/I$ for some ideals $I \subset J \subset R$. Thus the definition of Noetherian implies the result. If the number of generators of $M$ is greater than $1$, then we can find a short exact sequence $0 \to M' \to M \to M'' \to 0$ where $M'$ and $M''$ have fewer generators. Note that setting $N' = M' \cap N$ and $N'' = \operatorname{Im}(N \to
M'')$ gives a similar short exact sequence for $N$. Hence the result follows from the induction hypothesis since the number of generators of $N$ is at most the number of generators of $N'$ plus the number of generators of $N''$.

To show that $M$ is finitely presented just apply the previous result to the kernel of a presentation $R^n \to M$.

It is well known and easy to prove that the ascending chain condition for $R$-submodules of $M$ is equivalent to the condition that every submodule of $M$ is a finite $R$-module. We omit the proof. $\square$

#### Lemma. Prime spectra and associated points

*Source credit:* the original source citation EGA1 (Corollary 1.2.4)

Let $\varphi : R \to S$ be a ring map. Assume that every $g \in S$ can be written as $g = u\varphi(f)$ for some $f \in R$ and some unit $u \in S$. Then $$\operatorname{Spec}(S) \longrightarrow \operatorname{Spec}(R)$$ is a homeomorphism onto its image.

**Proof.** The map is continuous by Lemma [Functoriality of affine spectra (programme binding)](#uncovered-algebra-lemma-spec-functorial). If $\mathfrak q$ and $\mathfrak q'$ have the same inverse image in $R$, then the assumption shows that every $g \in S$ is in $\mathfrak q$ if and only if it is in $\mathfrak q'$. Thus the map is injective. Finally, if $g = u\varphi(f)$ as in the statement, then $$D(g) = \operatorname{Spec}(\varphi)^{-1}(D(f)).$$ Since the standard opens form a basis, the map is a homeomorphism onto its image. $\square$

#### Lemma. The spectrum of a product of rings

Let $R_1$ and $R_2$ be rings. Let $R = R_1 \times R_2$. The maps $R \to R_1$, $(x, y) \mapsto x$ and $R \to R_2$, $(x, y) \mapsto y$ induce continuous maps $\operatorname{Spec}(R_1) \to \operatorname{Spec}(R)$ and $\operatorname{Spec}(R_2) \to \operatorname{Spec}(R)$. The induced map $$\operatorname{Spec}(R_1) \amalg \operatorname{Spec}(R_2)
\longrightarrow
\operatorname{Spec}(R)$$ is a homeomorphism. In other words, the spectrum of $R = R_1\times R_2$ is the disjoint union of the spectrum of $R_1$ and the spectrum of $R_2$.

**Proof.** Write $1 = e_1 + e_2$ with $e_1 = (1, 0)$ and $e_2 = (0, 1)$. Note that $e_1$ and $e_2 = 1 - e_1$ are idempotents. We leave it to the reader to show that $R_1 = R_{e_1}$ is the localization of $R$ at $e_1$. Similarly for $e_2$. Thus the statement of the lemma follows from Lemma [Idempotents and open-and-closed subsets of a spectrum](#native-algebra-lemma-idempotent-spec) combined with Lemma [Principal open subsets of a spectrum](#native-algebra-lemma-standard-open). $\square$

#### Lemma. Standard affine covers of a spectrum
 Let $R$ be a ring, and let $f_1, f_2, \ldots, f_n \in R$ generate the unit ideal in $R$. Then the following sequence is exact: $$0 \longrightarrow
R \longrightarrow
\bigoplus\nolimits_i R_{f_i} \longrightarrow
\bigoplus\nolimits_{i, j}R_{f_if_j}$$ where the maps $\alpha : R \longrightarrow \bigoplus_i R_{f_i}$ and $\beta : \bigoplus_i R_{f_i} \longrightarrow \bigoplus_{i, j} R_{f_if_j}$ are defined as $$\alpha(x) = \left(\frac{x}{1}, \ldots, \frac{x}{1}\right)
\text{ and }
\beta\left(\frac{x_1}{f_1^{r_1}}, \ldots, \frac{x_n}{f_n^{r_n}}\right)
=
\left(\frac{x_i}{f_i^{r_i}}-\frac{x_j}{f_j^{r_j}}~\text{in}~R_{f_if_j}\right).$$

**Proof.** Special case of Lemma [Modules (programme binding)](#uncovered-algebra-lemma-cover-module). $\square$

#### Definition. Formally étale ring maps
 Let $R \to S$ be a ring map. We say $S$ is *formally étale over $R$* if for every commutative solid diagram $$\begin{gathered}\begin{matrix}S & A/I \\ R & A\end{matrix} \\[6pt] \begin{aligned}S & \longrightarrow A/I \\ S & \dashrightarrow A \\ R & \longrightarrow A \\ R & \longrightarrow S \\ A & \longrightarrow A/I\end{aligned}\end{gathered}$$ where $I \subset A$ is an ideal of square zero, there exists a unique dotted arrow making the diagram commute.

#### Lemma. Tensor products and direct sums
 Let $$\begin{aligned}
M_1\xrightarrow{f} M_2\xrightarrow{g} M_3 \to 0
\end{aligned}$$ be an exact sequence of $R$-modules and homomorphisms, and let $N$ be any $R$-module. Then the sequence 

$$M_1\otimes N\xrightarrow{f \otimes 1} M_2\otimes N \xrightarrow{g \otimes 1}
M_3\otimes N \to 0$$ is exact. In other words, the functor $- \otimes_R N$ is *right exact*, in the sense that tensoring each term in the original right exact sequence preserves the exactness.

**Proof.** For every $R$-module $P$ we apply the functor $\operatorname{Hom}(-, \operatorname{Hom}(N, P))$ to the first exact sequence. We obtain $$0 \to
\operatorname{Hom}(M_3, \operatorname{Hom}(N, P)) \to
\operatorname{Hom}(M_2, \operatorname{Hom}(N, P)) \to
\operatorname{Hom}(M_1, \operatorname{Hom}(N, P))$$ which is exact by Lemma [Exactness of Hom from a projective module](#native-algebra-lemma-hom-exact) (1). By Lemma [Derived Hom, Ext and tensor products and direct sums (uncovered prerequisite)](#uncovered-algebra-lemma-hom-from-tensor-product) this becomes the sequence $$0 \to \operatorname{Hom}(M_3 \otimes N, P) \to
\operatorname{Hom}(M_2 \otimes N, P) \to \operatorname{Hom}(M_1 \otimes N, P)$$ which is therefore also exact. Then using Lemma [Exactness of Hom from a projective module](#native-algebra-lemma-hom-exact) (1) again, we arrive at the desired exact sequence. $\square$

#### Lemma. Commutative algebra
 Let $(M_i, \mu_{ij})$ be a directed system. Let $M = \mathop{\operatorname{colim}} M_i$ with $\mu_i : M_i \to M$. Then, $\mu_i(x_i) = 0$ for $x_i \in M_i$ if and only if there exists $j \geq i$ such that $\mu_{ij}(x_i) = 0$.

**Proof.** This is clear from the description of the directed colimit in Lemma [Filtered limits and commutative algebra (uncovered prerequisite)](#uncovered-algebra-lemma-directed-colimit). $\square$

#### Lemma. Integral extensions and field extensions

Let $k$ be a field. Let $S$ be a $k$-algebra over $k$.

1.  If $S$ is a domain and finite dimensional over $k$, then $S$ is a field.

2.  If $S$ is integral over $k$ and a domain, then $S$ is a field.

3.  If $S$ is integral over $k$ then every prime of $S$ is a maximal ideal (see Lemma [Prime spectra and associated points (uncovered prerequisite)](#uncovered-algebra-lemma-ring-with-only-minimal-primes) for more consequences).

**Proof.** The statement on primes follows from the statement "integral $+$ domain $\Rightarrow$ field". Let $S$ be integral over $k$ and assume $S$ is a domain. Take a nonzero $s\in S$. By Lemma [Criteria for integral extensions](#native-algebra-lemma-characterize-integral) we may find a finite dimensional $k$-subalgebra $k \subset S' \subset S$ containing $s$. Hence $S$ is a field if we can prove the first statement. Assume $S$ finite dimensional over $k$ and a domain. Pick $s\in S$. Since $S$ is a domain the multiplication map $s : S \to S$ is surjective by dimension reasons. Hence there exists an element $s_1 \in S$ such that $ss_1 = 1$. So $S$ is a field. $\square$

#### Lemma. Flatness and local algebra

A flat local ring homomorphism of local rings is faithfully flat.

**Proof.** Immediate from Lemma [Faithfully flat ring maps](#native-algebra-lemma-ff-rings). $\square$

#### Lemma. Faithfully flat ring maps
 Let $R \to S$ be a flat ring map. The following are equivalent:

1.  $R \to S$ is faithfully flat,

2.  the induced map on $\operatorname{Spec}$ is surjective, and

3.  any closed point $x \in \operatorname{Spec}(R)$ is in the image of the map $\operatorname{Spec}(S) \to \operatorname{Spec}(R)$.

**Proof.** This follows quickly from Lemma [Faithfully flat modules](#native-algebra-lemma-ff), because we saw in Remark [Commutative algebra](#native-algebra-remark-fundamental-diagram) that $\mathfrak p$ is in the image if and only if the ring $S \otimes_R \kappa(\mathfrak p)$ is nonzero. $\square$

#### Lemma. Étale morphisms and prime spectra and associated points
 Let $R \to S$ be a ring map. Let $\mathfrak q \subset S$ be a prime lying over the prime $\mathfrak p \subset R$. Assume $R \to S$ is finite type and quasi-finite at $\mathfrak q$. Then there exists

1.  an étale ring map $R \to R'$,

2.  a prime $\mathfrak p' \subset R'$ lying over $\mathfrak p$,

3.  a product decomposition $$R' \otimes_R S = A \times B$$

with the following properties

1.  $\kappa(\mathfrak p) = \kappa(\mathfrak p')$,

2.  $R' \to A$ is finite,

3.  $A$ has exactly one prime $\mathfrak r$ lying over $\mathfrak p'$,

4.  $\mathfrak r$ lies over $\mathfrak q$, and

5.  $B$ does not have a prime lying over $\mathfrak q$ and $\mathfrak p'$.

**Proof.** Let $S' \subset S$ be the integral closure of $R$ in $S$. Let $\mathfrak q' = S' \cap \mathfrak q$. By Zariski's Main Theorem [Zariski's main theorem in affine algebra](#native-algebra-theorem-main-theorem) there exists a $g \in S'$, $g \not \in \mathfrak q'$ such that $S'_g \cong S_g$. Consider the fibre rings $F = S \otimes_R \kappa(\mathfrak p)$ and $F' = S' \otimes_R \kappa(\mathfrak p)$. Denote by $\overline{\mathfrak q}'$ the prime of $F'$ corresponding to $\mathfrak q'$. Since $F'$ is integral over $\kappa(\mathfrak p)$ we see that $\overline{\mathfrak q}'$ is a closed point of $\operatorname{Spec}(F')$, see Lemma [Integral extensions and field extensions](#native-algebra-lemma-integral-over-field). Note that $\mathfrak q$ defines an isolated closed point $\overline{\mathfrak q}$ of $\operatorname{Spec}(F)$ (see Definition [Finite algebras](#context-algebra-definition-quasi-finite)). Since $S'_g \cong S_g$ we have $F'_g \cong F_g$, so $\overline{\mathfrak q}$ and $\overline{\mathfrak q}'$ have isomorphic open neighbourhoods in $\operatorname{Spec}(F)$ and $\operatorname{Spec}(F')$. We conclude the set $\{\overline{\mathfrak q}'\} \subset \operatorname{Spec}(F')$ is open. Combined with $\overline{\mathfrak q}'$ being closed (shown above) we conclude that $\overline{\mathfrak q}'$ defines an isolated closed point of $\operatorname{Spec}(F')$ as well.

An additional small remark is that under the map $\operatorname{Spec}(F) \to \operatorname{Spec}(F')$ the point $\overline{\mathfrak q}$ is the only point mapping to $\overline{\mathfrak q}'$. This follows from the discussion above.

By Lemma [A disjoint spectrum and a product of rings](#native-algebra-lemma-disjoint-implies-product) we may write $F' = F'_1 \times F'_2$ with $\operatorname{Spec}(F'_1) = \{\overline{\mathfrak q}'\}$. Since $F' = S' \otimes_R \kappa(\mathfrak p)$, there exists an $s' \in S'$ which maps to the element $(r, 0) \in F'_1 \times F'_2 = F'$ for some $r \in R$, $r \not \in \mathfrak p$. In fact, what we will use about $s'$ is that it is an element of $S'$, not contained in $\mathfrak q'$, and contained in any other prime lying over $\mathfrak p$.

Let $f(x) \in R[x]$ be a monic polynomial such that $f(s') = 0$. Denote by $\overline{f} \in \kappa(\mathfrak p)[x]$ the image. We can factor it as $\overline{f} = x^e \overline{h}$ where $\overline{h}(0) \not = 0$. After replacing $f$ by $x f$ if necessary, we may assume $e \geq 1$. By Lemma [Étale morphisms and derived tensor products and Tor amplitude (uncovered prerequisite)](#uncovered-algebra-lemma-factor-mod-lift-etale) we can find an étale ring extension $R \to R'$, a prime $\mathfrak p'$ lying over $\mathfrak p$, and a factorization $f = h i$ in $R'[x]$ such that $\kappa(\mathfrak p) = \kappa(\mathfrak p')$, $\overline{h} = h \bmod \mathfrak p'$, $x^e = i \bmod \mathfrak p'$, and we can write $a h + b i = 1$ in $R'[x]$ (for suitable $a, b$).

Consider the elements $h(s'), i(s') \in R' \otimes_R S'$. By construction we have $h(s')i(s') = f(s') = 0$. On the other hand they generate the unit ideal since $a(s')h(s') + b(s')i(s') = 1$. Thus we see that $R' \otimes_R S'$ is the product of the localizations at these elements: $$R' \otimes_R S'
=
(R' \otimes_R S')_{i(s')}
\times
(R' \otimes_R S')_{h(s')}
=
S'_1 \times S'_2$$ Moreover this product decomposition is compatible with the product decomposition we found for the fibre ring $F'$; this comes from our choices of $s', i, h$ which guarantee that $\overline{\mathfrak q}'$ is the only prime of $F'$ which does not contain the image of $i(s')$ in $F'$. Here we use that the fibre ring of $R'\otimes_R S'$ over $R'$ at $\mathfrak p'$ is the same as $F'$ due to the fact that $\kappa(\mathfrak p) = \kappa(\mathfrak p')$. It follows that $S'_1$ has exactly one prime, say $\mathfrak r'$, lying over $\mathfrak p'$ and that this prime lies over $\mathfrak q'$. Hence the element $g \in S'$ maps to an element of $S'_1$ not contained in $\mathfrak r'$.

The base change $R'\otimes_R S$ inherits a similar product decomposition $$R' \otimes_R S
=
(R' \otimes_R S)_{i(s')}
\times
(R' \otimes_R S)_{h(s')}
=
S_1 \times S_2$$ It follows from the above that $S_1$ has exactly one prime, say $\mathfrak r$, lying over $\mathfrak p'$ (consider the fibre ring as above), and that this prime lies over $\mathfrak q$.

Now we may apply Lemma [Finite algebras (programme binding)](#uncovered-algebra-lemma-produce-finite) to the ring maps $R' \to S'_1 \to S_1$, the prime $\mathfrak p'$ and the element $g$ to see that after replacing $R'$ by a principal localization we can assume that $S_1$ is finite over $R'$ as desired. $\square$

#### Lemma. The general fibrewise injectivity criterion for module maps

Suppose that $R \to S$ is a local homomorphism of local rings. Denote by $\mathfrak m$ the maximal ideal of $R$. Let $u : M \to N$ be a map of $S$-modules. Assume

1.  $S$ is essentially of finite presentation over $R$,

2.  $M$, $N$ are finitely presented over $S$,

3.  $N$ is flat over $R$, and

4.  $\overline{u} : M/\mathfrak mM \to N/\mathfrak mN$ is injective.

Then $u$ is injective, and $N/u(M)$ is flat over $R$.

**Proof.** By Lemma [Essentially finitely presented module models](#native-algebra-lemma-limit-module-essentially-finite-presentation) and its proof we can find a system $R_\lambda \to S_\lambda$ of local ring maps together with maps of $S_\lambda$-modules $u_\lambda : M_\lambda \to N_\lambda$ satisfying the conclusions (1) -- (6) for both $N$ and $M$ of that lemma and such that the colimit of the maps $u_\lambda$ is $u$. By Lemma [Eventual flatness in a filtered colimit](#native-algebra-lemma-colimit-eventually-flat) we may assume that $N_\lambda$ is flat over $R_\lambda$ for all sufficiently large $\lambda$. Denote by $\mathfrak m_\lambda \subset R_\lambda$ the maximal ideal and $\kappa_\lambda = R_\lambda / \mathfrak m_\lambda$, resp. $\kappa = R/\mathfrak m$ the residue fields.

Consider the map $$\Psi_\lambda :
M_\lambda/\mathfrak m_\lambda M_\lambda \otimes_{\kappa_\lambda} \kappa
\longrightarrow
M/\mathfrak m M.$$ Since $S_\lambda/\mathfrak m_\lambda S_\lambda$ is essentially of finite type over the field $\kappa_\lambda$ we see that the tensor product $S_\lambda/\mathfrak m_\lambda S_\lambda \otimes_{\kappa_\lambda} \kappa$ is essentially of finite type over $\kappa$. Hence it is a Noetherian ring and we conclude the kernel of $\Psi_\lambda$ is finitely generated. Since $M/\mathfrak m M$ is the colimit of the system $M_\lambda/\mathfrak m_\lambda M_\lambda$ and $\kappa$ is the colimit of the fields $\kappa_\lambda$ there exists a $\lambda' \geq \lambda$ such that the kernel of $\Psi_\lambda$ is generated by the kernel of $$\Psi_{\lambda, \lambda'} :
M_\lambda/\mathfrak m_\lambda M_\lambda
\otimes_{\kappa_\lambda}
\kappa_{\lambda'}
\longrightarrow
M_{\lambda'}/\mathfrak m_{\lambda'} M_{\lambda'}.$$ By construction there exists a multiplicative subset $W \subset S_\lambda \otimes_{R_\lambda} R_{\lambda'}$ such that $S_{\lambda'} = W^{-1}(S_\lambda \otimes_{R_\lambda} R_{\lambda'})$ and $$W^{-1}(M_\lambda/\mathfrak m_\lambda M_\lambda
\otimes_{\kappa_\lambda}
\kappa_{\lambda'})
=
M_{\lambda'}/\mathfrak m_{\lambda'} M_{\lambda'}.$$ Now suppose that $x$ is an element of the kernel of $$\Psi_{\lambda'} :
M_{\lambda'}/\mathfrak m_{\lambda'} M_{\lambda'}
\otimes_{\kappa_{\lambda'}} \kappa
\longrightarrow
M/\mathfrak m M.$$ Write $x = y/w$ for some $w \in W$ and $y \in M_\lambda/\mathfrak m_\lambda M_\lambda \otimes_{\kappa_\lambda} \kappa$. Hence $y \in \operatorname{Ker}(\Psi_\lambda)$. Hence $y$ is a linear combination of elements in the kernel of $\Psi_{\lambda, \lambda'}$. Hence the image of $y$ is zero in $M_{\lambda'}/\mathfrak m_{\lambda'} M_{\lambda'}
\otimes_{\kappa_{\lambda'}} \kappa$, hence $x = 0$ because $w$ is invertible in $S_{\lambda'}$. We conclude that the kernel of $\Psi_{\lambda'}$ is zero for all sufficiently large $\lambda'$!

By the result of the preceding paragraph we may assume that the kernel of $\Psi_\lambda$ is zero for all $\lambda$ sufficiently large, which implies that the map $M_\lambda/\mathfrak m_\lambda M_\lambda \to M/\mathfrak m M$ is injective. Combined with $\overline{u}$ being injective this formally implies that also $\overline{u_\lambda} : M_\lambda/\mathfrak m_\lambda M_\lambda
\to N_\lambda/\mathfrak m_\lambda N_\lambda$ is injective. By Lemma [Injectivity from a fibrewise injectivity criterion](#native-algebra-lemma-mod-injective) we conclude that (for all sufficiently large $\lambda$) the map $u_\lambda$ is injective and that $N_\lambda/u_\lambda(M_\lambda)$ is flat over $R_\lambda$. The lemma follows. $\square$

#### Remark. Finite generation and finite presentation over a general ring
 It is not true that a finite $R$-module which is $R$-flat is automatically projective. A counterexample is where $R = \mathcal{C}^\infty(\mathbf{R})$ is the ring of infinitely differentiable functions on $\mathbf{R}$, and $M = R_{\mathfrak m} = R/I$ where $\mathfrak m = \{f \in R \mid f(0) = 0\}$ and $I = \{f \in R \mid \exists \epsilon, \epsilon > 0 :
f(x) = 0\ \forall x, |x| < \epsilon\}$.

#### Lemma. Complete rings, formal power series and flatness

Let $I$ be an ideal of a Noetherian ring $R$. Denote by ${}^\wedge$ completion with respect to $I$.

1.  The ring map $R \to R^\wedge$ is flat.

2.  The functor $M \mapsto M^\wedge$ is exact on the category of finitely generated $R$-modules.

**Proof.** Consider $J \otimes_R R^\wedge \to R \otimes_R R^\wedge = R^\wedge$ where $J$ is an arbitrary ideal of $R$. According to Lemma Completion, Theorems 3.1–3.3, 4.1 and 5.1 this is identified with $J^\wedge \to R^\wedge$ and $J^\wedge \to R^\wedge$ is injective. Part (1) follows from Lemma [Flatness](#native-algebra-lemma-flat). Part (2) is a reformulation of Lemma Completion, Theorems 3.1–3.3, 4.1 and 5.1 part (2). $\square$

#### Lemma. Composition and flatness

A composition of (faithfully) flat ring maps is (faithfully) flat. If $R \to R'$ is (faithfully) flat, and $M'$ is a (faithfully) flat $R'$-module, then $M'$ is a (faithfully) flat $R$-module.

**Proof.** The first statement of the lemma is a particular case of the second, so it is clearly enough to prove the latter. Let $R \to R'$ be a flat ring map, and $M'$ a flat $R'$-module. We need to prove that $M'$ is a flat $R$-module. Let $N_1 \to N_2 \to N_3$ be an exact complex of $R$-modules. Then, the complex $R' \otimes_R N_1 \to
R' \otimes_R N_2 \to R' \otimes_R N_3$ is exact (since $R'$ is flat as an $R$-module), and so the complex $M' \otimes_{R'} \left(R' \otimes_R N_1\right)
\to M' \otimes_{R'} \left(R' \otimes_R N_2\right)
\to M' \otimes_{R'} \left(R' \otimes_R N_3\right)$ is exact (since $M'$ is a flat $R'$-module). Since $M' \otimes_{R'} \left(R' \otimes_R N\right)
\cong \left(M' \otimes_{R'} R'\right) \otimes_R N
\cong M' \otimes_R N$ for any $R$-module $N$ functorially (by Lemmas [Modules and tensor products and direct sums (uncovered prerequisite)](#uncovered-algebra-lemma-tensor-with-bimodule) and [Tensor products and direct sums (uncovered prerequisite)](#uncovered-algebra-lemma-flip-tensor-product)), this complex is isomorphic to the complex $M' \otimes_R N_1 \to M' \otimes_R N_2 \to M' \otimes_R N_3$, which is therefore also exact. This shows that $M'$ is a flat $R$-module. Tracing this argument backwards, we can show that if $R \to R'$ is faithfully flat, and if $M'$ is faithfully flat as an $R'$-module, then $M'$ is faithfully flat as an $R$-module. $\square$

#### Lemma. Complete rings and formal power series
 Let $R$ be a Noetherian ring. Let $I$ be an ideal of $R$. Let $M$ be an $R$-module. Then the completion $M^\wedge$ of $M$ with respect to $I$ is $I$-adically complete, $I^n M^\wedge = (I^nM)^\wedge$, and $M^\wedge/I^nM^\wedge = M/I^nM$.

**Proof.** This is a special case of Lemma [Finite algebras](#native-algebra-lemma-hathat-finitely-generated) because $I$ is a finitely generated ideal. $\square$

#### Lemma. Flatness
 Let $0 \to M_1 \to M_2 \to M_3 \to 0$ be a universally exact sequence of $R$-modules, and suppose $M_2$ is flat. Then $M_1$ and $M_3$ are flat.

**Proof.** Let $0 \to N \to N' \to N'' \to 0$ be a short exact sequence of $R$-modules. Consider the commutative diagram $$\begin{gathered}\begin{matrix}M_1 \otimes_R N & M_2 \otimes_R N & M_3 \otimes_R N \\ M_1 \otimes_R N' & M_2 \otimes_R N' & M_3 \otimes_R N' \\ M_1 \otimes_R N'' & M_2 \otimes_R N'' & M_3 \otimes_R N''\end{matrix} \\[6pt] \begin{aligned}M_1 \otimes_R N & \longrightarrow M_2 \otimes_R N \\ M_1 \otimes_R N & \longrightarrow M_1 \otimes_R N' \\ M_2 \otimes_R N & \longrightarrow M_3 \otimes_R N \\ M_2 \otimes_R N & \longrightarrow M_2 \otimes_R N' \\ M_3 \otimes_R N & \longrightarrow M_3 \otimes_R N' \\ M_1 \otimes_R N' & \longrightarrow M_2 \otimes_R N' \\ M_1 \otimes_R N' & \longrightarrow M_1 \otimes_R N'' \\ M_2 \otimes_R N' & \longrightarrow M_3 \otimes_R N' \\ M_2 \otimes_R N' & \longrightarrow M_2 \otimes_R N'' \\ M_3 \otimes_R N' & \longrightarrow M_3 \otimes_R N'' \\ M_1 \otimes_R N'' & \longrightarrow M_2 \otimes_R N'' \\ M_2 \otimes_R N'' & \longrightarrow M_3 \otimes_R N''\end{aligned}\end{gathered}$$ (we have dropped the $0$'s on the boundary). By assumption the rows give short exact sequences and the arrow $M_2 \otimes N \to M_2 \otimes N'$ is injective. Clearly this implies that $M_1 \otimes N \to M_1 \otimes N'$ is injective and we see that $M_1$ is flat. In particular the left and middle columns give rise to short exact sequences. It follows from a diagram chase that the arrow $M_3 \otimes N \to M_3 \otimes N'$ is injective. Hence $M_3$ is flat. $\square$

#### Proposition. Criteria for coherent sheaves

*Source credit:* This is the original source citation Chase (Theorem 2.1).

Let $R$ be a ring. The following are equivalent

1.  $R$ is coherent,

2.  any product of flat $R$-modules is flat, and

3.  for every set $A$ the module $R^A$ is flat.

**Proof.** Assume $R$ coherent, and let $Q_\alpha$, $\alpha \in A$ be a set of flat $R$-modules. We have to show that $I \otimes_R \prod_\alpha Q_\alpha \to \prod Q_\alpha$ is injective for every finitely generated ideal $I$ of $R$, see Lemma [Flatness](#native-algebra-lemma-flat). Since $R$ is coherent $I$ is an $R$-module of finite presentation. Hence $I \otimes_R \prod_\alpha Q_\alpha = \prod I \otimes_R Q_\alpha$ by Proposition [Finite presentation and tensor products and direct sums (uncovered prerequisite)](#uncovered-algebra-proposition-fp-tensor). The desired injectivity follows as $I \otimes_R Q_\alpha \to Q_\alpha$ is injective by flatness of $Q_\alpha$.

The implication (2) $\Rightarrow$ (3) is trivial.

Assume that the $R$-module $R^A$ is flat for every set $A$. Let $I$ be a finitely generated ideal in $R$. Then $I \otimes_R R^A \to R^A$ is injective by assumption. By Proposition [Tensor products and direct sums (uncovered prerequisite)](#uncovered-algebra-proposition-fg-tensor) and the finiteness of $I$ the image is equal to $I^A$. Hence $I \otimes_R R^A = I^A$ for every set $A$ and we conclude that $I$ is finitely presented by Proposition [Finite presentation and tensor products and direct sums (uncovered prerequisite)](#uncovered-algebra-proposition-fp-tensor). $\square$

#### Lemma. Coherent sheaves and Noetherian rings
 A Noetherian ring is a coherent ring.

**Proof.** By Lemma [Finite presentation and Noetherian rings (programme binding)](#uncovered-algebra-lemma-noetherian-finite-type-is-finite-presentation) any finite $R$-module is finitely presented. In particular any ideal of $R$ is finitely presented. $\square$

#### Remark. Derived Hom and Ext

We can also construct $R^{sh}$ from $R^h$. Namely, for any finite separable subextension $\kappa^{sep}/\kappa'/\kappa$ there exists a unique (up to unique isomorphism) finite étale local ring extension $R^h \subset R^h(\kappa')$ whose residue field extension reproduces the given extension, see Lemma [Finite étale algebras over a henselian ring](#native-algebra-lemma-henselian-cat-finite-etale). Hence we can set $$R^{sh} =
\bigcup\nolimits_{\kappa \subset \kappa' \subset \kappa^{sep}}
R^h(\kappa')$$ The arrows in this system, compatible with the arrows on the level of residue fields, exist by Lemma [Finite étale algebras over a henselian ring](#native-algebra-lemma-henselian-cat-finite-etale). This will produce a henselian local ring by Lemma [Filtered limits and henselian rings (programme binding)](#uncovered-algebra-lemma-colimit-henselian) since each of the rings $R^h(\kappa')$ is henselian by Lemma [Henselian rings and finite algebras (programme binding)](#uncovered-algebra-lemma-finite-over-henselian). By construction the residue field extension induced by $R^h \to R^{sh}$ is the field extension $\kappa^{sep}/\kappa$. Hence $R^{sh}$ so constructed is strictly henselian. By Lemma [Composition and étale morphisms (uncovered prerequisite)](#uncovered-algebra-lemma-composition-colimit-etale) the $R$-algebra $R^{sh}$ is a colimit of étale $R$-algebras. Hence the uniqueness of Lemma [Henselian rings (uncovered prerequisite)](#uncovered-algebra-lemma-uniqueness-henselian) shows that $R^{sh}$ is the strict henselization.

#### Lemma. Filtered limits and henselian rings

Let $R \to S$ be a ring map with $S$ henselian local. Given

1.  an $R$-algebra $A$ which is a filtered colimit of étale $R$-algebras,

2.  a prime $\mathfrak q$ of $A$ lying over $\mathfrak p = R \cap \mathfrak m_S$,

3.  a $\kappa(\mathfrak p)$-algebra map $\tau : \kappa(\mathfrak q) \to S/\mathfrak m_S$,

then there exists a unique homomorphism of $R$-algebras $f : A \to S$ such that $\mathfrak q = f^{-1}(\mathfrak m_S)$ and $f$ induces $\tau$ on residue fields.

**Proof.** Write $A = \mathop{\operatorname{colim}} A_i$ as a filtered colimit of étale $R$-algebras. Set $\mathfrak q_i = A_i \cap \mathfrak q$. We obtain $f_i : A_i \to S$ by applying Lemma [Maps into a henselian local ring](#native-algebra-lemma-map-into-henselian). Set $f = \mathop{\operatorname{colim}} f_i$. $\square$

#### Proposition. Successive localizations
 Let $\overline{S}$ be the image of $S$ in $S'^{-1}A$, then $(SS')^{-1}A$ is isomorphic to $\overline{S}^{-1}(S'^{-1}A)$.

**Proof.** The map sending $x\in A$ to $x/1\in (SS')^{-1}A$ induces a map sending $x/s\in S'^{-1}A$ to $x/s \in (SS')^{-1}A$, by universal property. The image of the elements in $\overline{S}$ are invertible in $(SS')^{-1}A$. By the universal property we get a map $f : \overline{S}^{-1}(S'^{-1}A) \to (SS')^{-1}A$ which maps $(x/s')/(s/1)$ to $x/ss'$.

On the other hand, the map from $A$ to $\overline{S}^{-1}(S'^{-1}A)$ sending $x\in A$ to $(x/1)/(1/1)$ also induces a map $g : (SS')^{-1}A \to \overline{S}^{-1}(S'^{-1}A)$ which sends $x/ss'$ to $(x/s')/(s/1)$, by the universal property again. It is immediately checked that $f$ and $g$ are inverse to each other, hence they are both isomorphisms. $\square$

#### Proposition. Exactness of localization

*Source credit:* the original source citation FAC (Chapter II, §4, no. 48, Lemma 1, p. 241)

The cited proof constructs the localized module from fractions, identifies $S^{-1}A \otimes_A M$ with $S^{-1}M$, and checks exactness directly. It assumes $0 \notin S$; the formulation below also includes the zero-ring localization when $0 \in S$.

Localization is exact.

Let $L\xrightarrow{u} M\xrightarrow{v} N$ be an exact sequence of $A$-modules. Then $S^{-1}L \to S^{-1}M \to S^{-1}N$ is also exact.

**Proof.** First it is clear that $S^{-1}L \to S^{-1}M \to S^{-1}N$ is a complex since localization is a functor. Next suppose that $x/s$ maps to zero in $S^{-1}N$ for some $x/s \in S^{-1}M$. Then by definition there is a $t\in S$ such that $v(xt) = v(x)t = 0$ in $N$, which means $xt \in \operatorname{Ker}(v)$. By the exactness of $L \to M \to N$ we have $xt = u(y)$ for some $y$ in $L$. Then $x/s$ is the image of $y/st$. This proves the exactness. $\square$

#### Lemma. Projective, locally free modules and finite algebras

Let $R \to S$ be a flat local homomorphism of local rings. Let $M$ be a finite $R$-module. Then $M$ is finite projective over $R$ if and only if $M \otimes_R S$ is finite projective over $S$.

**Proof.** By Lemma [Characterizations of finite projective modules](#native-algebra-lemma-finite-projective) being finite projective over a local ring is the same thing as being finite free. Suppose that $M \otimes_R S$ is a finite free $S$-module. Pick $x_1, \ldots, x_r \in M$ whose images in $M/\mathfrak m_RM$ form a basis over $\kappa(\mathfrak m_R)$. Then we see that $x_1 \otimes 1, \ldots, x_r \otimes 1$ are a basis for $M \otimes_R S$. This implies that the map $R^{\oplus r} \to M, (a_i) \mapsto \sum a_i x_i$ becomes an isomorphism after tensoring with $S$. By faithful flatness of $R \to S$, see Lemma [Flatness and local algebra](#native-algebra-lemma-local-flat-ff) we see that it is an isomorphism. $\square$

#### Lemma. Finite presentation and flatness

Let $R$ be a ring. Let $R \to S$ be of finite presentation and flat. For any $d \geq 0$ the set $$\left\{
\begin{matrix}
\mathfrak q \in \operatorname{Spec}(S)
\text{ such that setting }\mathfrak p = R \cap \mathfrak q
\text{ the fibre ring}\\
S_{\mathfrak q}/\mathfrak pS_{\mathfrak q}
\text{ is Cohen-Macaulay}
\text{ and } \dim_{\mathfrak q}(S/R) = d
\end{matrix}
\right\}$$ is open in $\operatorname{Spec}(S)$.

**Proof.** Let $\mathfrak q$ be an element of the set indicated, with $\mathfrak p$ the corresponding prime of $R$. We have to find a $g \in S$, $g \not \in \mathfrak q$ such that all fibre rings of $R \to S_g$ are Cohen-Macaulay and $\dim_{\mathfrak r}(S_g/R) = d$ for every prime $\mathfrak r \subset S_g$. During the course of the proof we may (finitely many times) replace $S$ by $S_g$ for a $g \in S$, $g \not \in \mathfrak q$. Thus by Lemma [Finite algebras](#native-algebra-lemma-quasi-finite-over-polynomial-algebra) we may assume there is a quasi-finite ring map $R[t_1, \ldots, t_d] \to S$ with $d = \dim_{\mathfrak q}(S/R)$. Let $\mathfrak q' = R[t_1, \ldots, t_d] \cap \mathfrak q$. By Lemma [Commutative algebra (programme binding)](#uncovered-algebra-lemma-where-cm) we see that the ring map $$R[t_1, \ldots, t_d]_{\mathfrak q'} /
\mathfrak p R[t_1, \ldots, t_d]_{\mathfrak q'}
\longrightarrow
S_{\mathfrak q}/\mathfrak p S_{\mathfrak q}$$ is flat. Hence by the critère de platitude par fibres Lemma [The fibrewise criterion for flatness](#native-algebra-lemma-criterion-flatness-fibre) we see that $R[t_1, \ldots, t_d]_{\mathfrak q'} \to S_{\mathfrak q}$ is flat. Hence by Theorem [Openness of the flat locus (programme binding)](#uncovered-algebra-theorem-openness-flatness) we see that for some $g \in S$, $g \not \in \mathfrak q$, the ring map $R[t_1, \ldots, t_d] \to S_g$ is flat. Replacing $S$ by $S_g$ we see that for every prime $\mathfrak r \subset S$, setting $\mathfrak r' = R[t_1, \ldots, t_d] \cap \mathfrak r$ and $\mathfrak p' = R \cap \mathfrak r$ the local ring map $R[t_1, \ldots, t_d]_{\mathfrak r'} \to S_{\mathfrak r}$ is flat. Hence also the base change $$R[t_1, \ldots, t_d]_{\mathfrak r'} /
\mathfrak p' R[t_1, \ldots, t_d]_{\mathfrak r'}
\longrightarrow
S_{\mathfrak r}/\mathfrak p' S_{\mathfrak r}$$ is flat. Hence by Lemma [Commutative algebra (programme binding)](#uncovered-algebra-lemma-where-cm) applied with $k = \kappa(\mathfrak p')$ we see $\mathfrak r$ is in the set of the lemma as desired. $\square$

#### Lemma. Divisibility of polynomials
 Let $K$ be a field. Let $n, m \in \mathbf{N}$ and $a_0, \ldots, a_{n - 1}, b_0, \ldots, b_{m - 1} \in K$. If the polynomial $x^n + a_{n - 1}x^{n - 1} + \ldots + a_0$ divides the polynomial $x^m + b_{m - 1} x^{m - 1} + \ldots + b_0$ in $K[x]$ then

1.  $a_0, \ldots, a_{n - 1}$ are integral over any subring $R_0$ of $K$ containing the elements $b_0, \ldots, b_{m - 1}$, and

2.  each $a_i$ lies in $\sqrt{(b_0, \ldots, b_{m-1})R}$ for any subring $R \subset K$ containing the elements $a_0, \ldots, a_{n - 1}, b_0, \ldots, b_{m - 1}$.

**Proof.** Let $L/K$ be a field extension such that we can write $x^m + b_{m - 1} x^{m - 1} + \ldots + b_0 =
\prod_{i = 1}^m (x - \beta_i)$ with $\beta_i \in L$. See Fields, Section [The geometric construction](#context-fields-section-splitting-fieds). Each $\beta_i$ is integral over $R_0$. Since each $a_i$ is a homogeneous polynomial in $\beta_1, \ldots, \beta_m$ we deduce the same for the $a_i$ (use Lemma [Integral extensions](#native-algebra-lemma-integral-closure-is-ring)). This proves (1).

Let $R$ be as in (2). Choose $c_0, \ldots, c_{m - n - 1} \in K$ such that $$\begin{matrix}
x^m + b_{m - 1} x^{m - 1} + \ldots + b_0 =  \\
(x^n + a_{n - 1}x^{n - 1} + \ldots + a_0)
(x^{m - n} + c_{m - n - 1}x^{m - n - 1}+ \ldots + c_0).
\end{matrix}$$ This equation implies $$\begin{aligned}
c_{m - n - 1} & = b_{m - 1} - a_{n - 1}, \\
c_{m - n - 2} & = b_{m - 2} - a_{n - 2} - a_{n - 1}c_{m - n - 1}, \\
\ldots
\end{aligned}$$ Thus $c_j \in R$ for all $j$. Dividing out the radical $\sqrt{(b_0, \ldots, b_{m - 1})}$ we get a reduced ring $\overline{R}$. We have to show that the images $\overline{a}_i \in \overline{R}$ are zero. And in $\overline{R}[x]$ we have the relation $$\begin{matrix}
x^m = x^m + \overline{b}_{m - 1} x^{m - 1} + \ldots + \overline{b}_0 = \\
(x^n + \overline{a}_{n - 1}x^{n - 1} + \ldots + \overline{a}_0)
(x^{m - n} + \overline{c}_{m - n - 1}x^{m - n - 1}+ \ldots + \overline{c}_0).
\end{matrix}$$ It is easy to see that this implies $\overline{a}_i = 0$ for all $i$. Indeed by Lemma [Localizations at minimal primes of a reduced ring](#native-algebra-lemma-minimal-prime-reduced-ring) the localization of $\overline{R}$ at a minimal prime $\mathfrak{p}$ is a field and $\overline{R}_{\mathfrak p}[x]$ a UFD. Thus $f = x^n + \sum \overline{a}_i x^i$ is associated to $x^n$ and since $f$ is monic $f = x^n$ in $\overline{R}_{\mathfrak p}[x]$. Then there exists an $s \in \overline{R}$, $s \not\in \mathfrak p$ such that $s(f - x^n) = 0$. Therefore all $\overline{a}_i$ lie in $\mathfrak p$ and we conclude by Lemma [Field extensions and tensor products and direct sums (uncovered prerequisite)](#uncovered-algebra-lemma-reduced-ring-sub-product-fields). $\square$

#### Lemma. Criteria for integral extensions

Let $\varphi : R \to S$ be a ring map. Let $s_1, \ldots, s_n$ be a finite set of elements of $S$. In this case $s_i$ is integral over $R$ for all $i = 1, \ldots, n$ if and only if there exists an $R$-subalgebra $S' \subset S$ finite over $R$ containing all of the $s_i$.

**Proof.** If each $s_i$ is integral, then the subalgebra generated by $\varphi(R)$ and the $s_i$ is finite over $R$. Namely, if $s_i$ satisfies a monic equation of degree $d_i$ over $R$, then this subalgebra is generated as an $R$-module by the elements $s_1^{e_1} \ldots s_n^{e_n}$ with $0 \leq e_i \leq d_i - 1$. Conversely, suppose given a finite $R$-subalgebra $S'$ containing all the $s_i$. Then all of the $s_i$ are integral by Lemma [Integral extensions and finite algebras](#native-algebra-lemma-finite-is-integral). $\square$

#### Lemma. Idempotents and open-and-closed subsets of a spectrum

Let $R$ be a ring. Let $e \in R$ be an idempotent. In this case $$\operatorname{Spec}(R) = D(e) \amalg D(1-e).$$

**Proof.** Note that an idempotent $e$ of a domain is either $1$ or $0$. Hence we see that $$\begin{eqnarray*}
D(e)
& = &
\{ \mathfrak p \in \operatorname{Spec}(R)
\mid
e \not\in \mathfrak p \} \\
& = &
\{ \mathfrak p \in \operatorname{Spec}(R)
\mid
e \not = 0\text{ in }\kappa(\mathfrak p) \} \\
& = &
\{ \mathfrak p \in \operatorname{Spec}(R)
\mid
e = 1\text{ in }\kappa(\mathfrak p) \}
\end{eqnarray*}$$ Similarly we have $$\begin{eqnarray*}
D(1-e)
& = &
\{ \mathfrak p \in \operatorname{Spec}(R)
\mid
1 - e \not\in \mathfrak p \} \\
& = &
\{ \mathfrak p \in \operatorname{Spec}(R)
\mid
e \not = 1\text{ in }\kappa(\mathfrak p) \} \\
& = &
\{ \mathfrak p \in \operatorname{Spec}(R)
\mid
e = 0\text{ in }\kappa(\mathfrak p) \}
\end{eqnarray*}$$ Since the image of $e$ in any residue field is either $1$ or $0$ we deduce that $D(e)$ and $D(1-e)$ cover all of $\operatorname{Spec}(R)$. $\square$

#### Lemma. Principal open subsets of a spectrum

Let $R$ be a ring. Let $f \in R$. The map $R \to R_f$ induces via the functoriality of $\operatorname{Spec}$ a homeomorphism $$\operatorname{Spec}(R_f) \longrightarrow D(f) \subset \operatorname{Spec}(R).$$ The inverse is given by $\mathfrak p \mapsto \mathfrak p \cdot R_f$.

**Proof.** This is a special case of Lemma [The spectrum of a localization](#native-algebra-lemma-spec-localization). $\square$

#### Theorem. Chevalley's constructibility theorem (Chevalley's Theorem)

Suppose that $R \to S$ is of finite presentation. The image of a constructible subset of $\operatorname{Spec}(S)$ in $\operatorname{Spec}(R)$ is constructible.

**Proof.** Write $S = R[x_1, \ldots, x_n]/(f_1, \ldots, f_m)$. We may factor $R \to S$ as $R \to R[x_1] \to R[x_1, x_2]
\to \ldots \to R[x_1, \ldots, x_{n-1}] \to S$. Hence we may assume that $S = R[x]/(f_1, \ldots, f_m)$. In this case we factor the map as $R \to R[x] \to S$, and by Lemma [Finite presentation (uncovered prerequisite)](#uncovered-algebra-lemma-closed-fp) we reduce to the case $S = R[x]$. By Lemma [Commutative algebra (programme binding)](#uncovered-algebra-lemma-constructible) it suffices to show that if $T = (\bigcup_{i = 1\ldots n} D(f_i)) \cap V(g_1, \ldots, g_m)$ for $f_i , g_j \in R[x]$ then the image in $\operatorname{Spec}(R)$ is constructible. Since finite unions of constructible sets are constructible, it suffices to deal with the case $n = 1$, i.e., when $T = D(f) \cap V(g_1, \ldots, g_m)$.

Note that if $c \in R$, then we have $$\operatorname{Spec}(R) =
V(c) \amalg D(c) =
\operatorname{Spec}(R/(c)) \amalg \operatorname{Spec}(R_c),$$ and correspondingly $\operatorname{Spec}(R[x]) =
V(c) \amalg D(c) = \operatorname{Spec}(R/(c)[x]) \amalg
\operatorname{Spec}(R_c[x])$. The intersection of $T = D(f) \cap V(g_1, \ldots, g_m)$ with each part still has the same shape, with $f$, $g_i$ replaced by their images in $R/(c)[x]$, respectively $R_c[x]$. Note that the image of $T$ in $\operatorname{Spec}(R)$ is the union of the image of $T \cap V(c)$ and $T \cap D(c)$. Using Lemmas [Finite presentation (uncovered prerequisite)](#uncovered-algebra-lemma-open-fp) and [Finite presentation (uncovered prerequisite)](#uncovered-algebra-lemma-closed-fp) it suffices to prove the images of both parts are constructible in $\operatorname{Spec}(R/(c))$, respectively $\operatorname{Spec}(R_c)$.

Let us assume we have $T = D(f) \cap V(g_1, \ldots, g_m)$ as above, with $\deg(g_1) \leq \deg(g_2) \leq \ldots \leq \deg(g_m)$. We are going to use induction on $m$, and on the degrees of the $g_i$. Let $d_1 = \deg(g_1)$, i.e., $g_1 = c x^{d_1} + l.o.t$ with $c \in R$ not zero. Cutting $R$ up into the pieces $R/(c)$ and $R_c$ we either lower the degree of $g_1$ (and this is covered by induction) or we reduce to the case where $c$ is invertible. If $c$ is invertible, and $m > 1$, then write $g_2 = c' x^{d_2} + l.o.t$. In this case consider $g_2' = g_2 - (c'/c) x^{d_2 - d_1} g_1$. Since the ideals $(g_1, g_2, \ldots, g_m)$ and $(g_1, g_2', g_3, \ldots, g_m)$ are equal we see that $T = D(f) \cap V(g_1, g_2', g_3\ldots, g_m)$. But here the degree of $g_2'$ is strictly less than the degree of $g_2$ and hence this case is covered by induction.

The bases case for the induction above are the cases (a) $T = D(f) \cap V(g)$ where the leading coefficient of $g$ is invertible, and (b) $T = D(f)$. These two cases are dealt with in Lemmas [Affine neighbourhoods (uncovered prerequisite)](#uncovered-algebra-lemma-affineline-special) and [Affine neighbourhoods (uncovered prerequisite)](#uncovered-algebra-lemma-affineline-open). $\square$

#### Lemma. Commutative algebra
 Let $R$ be a ring. Let $E \subset \operatorname{Spec}(R)$ be a constructible subset.

1.  If $E$ is stable under specialization, then $E$ is closed.

2.  If $E$ is stable under generalization, then $E$ is open.

**Proof.** First proof. The first assertion follows from Lemma [Closed images stable under specialization](#native-algebra-lemma-image-stable-specialization-closed) combined with Lemma [Commutative algebra (programme binding)](#uncovered-algebra-lemma-constructible-is-image). The second follows because the complement of a constructible set is constructible (see Topology, Lemma [The geometric construction (programme binding)](#uncovered-topology-lemma-constructible)), the first part of the lemma and Topology, Lemma [The geometric construction (programme binding)](#uncovered-topology-lemma-open-closed-specialization).

Second proof. Since $\operatorname{Spec}(R)$ is a spectral space by Lemma [Prime spectra and associated points (uncovered prerequisite)](#uncovered-algebra-lemma-spec-spectral) this is a special case of Topology, Lemma [The geometric construction (programme binding)](#uncovered-topology-lemma-constructible-stable-specialization-closed). $\square$

#### Lemma. Integral extensions
 Let $R \to S$ be a ring homomorphism. The set $$S' = \{s \in S \mid s\text{ is integral over }R\}$$ is an $R$-subalgebra of $S$.

**Proof.** This is clear from Lemmas [Criteria for integral extensions](#native-algebra-lemma-characterize-integral) and [Integral extensions and finite algebras](#native-algebra-lemma-finite-is-integral). $\square$

#### Lemma. Criteria for integral extensions
 Let $\varphi : R \to S$ be a ring map. Let $I \subset R$ be an ideal. Let $A = \sum I^nt^n \subset R[t]$ be the subring of the polynomial ring generated by $R \oplus It \subset R[t]$. An element $s \in S$ is integral over $I$ if and only if the element $st \in S[t]$ is integral over $A$.

**Proof.** Suppose $st$ is integral over $A$. Let $P = x^d + \sum_{j < d} a_j x^j$ be a monic polynomial with coefficients in $A$ such that $P^\varphi(st) = 0$. Let $a_j' \in A$ be the degree $d-j$ part of $a_j$, in other words $a_j' = a_j'' t^{d-j}$ with $a_j'' \in I^{d-j}$. For degree reasons we still have $(st)^d + \sum_{j < d} \varphi(a_j'') t^{d-j} (st)^j = 0$. Hence $s^d + \sum_{j < d} \varphi(a_j'') s^j = 0$ and we see that $s$ is integral over $I$.

Suppose that $s$ is integral over $I$. Say $P = x^d + \sum_{j < d} a_j x^j$ with $a_j \in I^{d-j}$. Then we immediately find a polynomial $Q = x^d + \sum_{j < d} (a_j t^{d-j}) x^j$ with coefficients in $A$ which proves that $st$ is integral over $A$. $\square$

#### Lemma. A point in the image of a spectrum map

Let $\varphi : R \to S$ be a ring map. Let $\mathfrak p$ be a prime of $R$. The following are equivalent

1.  $\mathfrak p$ is in the image of $\operatorname{Spec}(S) \to \operatorname{Spec}(R)$,

2.  $S \otimes_R \kappa(\mathfrak p) \not = 0$,

3.  $S_{\mathfrak p}/\mathfrak p S_{\mathfrak p} \not = 0$,

4.  $(S/\mathfrak pS)_{\mathfrak p} \not = 0$, and

5.  $\mathfrak p = \varphi^{-1}(\mathfrak pS)$.

**Proof.** We have already seen the equivalence of the first two in Remark [Commutative algebra](#native-algebra-remark-fundamental-diagram). The others are just reformulations of this. $\square$

#### Lemma. Integral extensions and local algebra
 Integral closure commutes with localization: If $A \to B$ is a ring map, and $S \subset A$ is a multiplicative subset, then the integral closure of $S^{-1}A$ in $S^{-1}B$ is $S^{-1}B'$, where $B' \subset B$ is the integral closure of $A$ in $B$.

**Proof.** Since localization is exact we see that $S^{-1}B' \subset S^{-1}B$. Suppose $x \in B'$ and $f \in S$. Then $x^d + \sum_{i = 1, \ldots, d} a_i x^{d - i} = 0$ in $B$ for some $a_i \in A$. Hence also $$(x/f)^d + \sum\nolimits_{i = 1, \ldots, d} a_i/f^i (x/f)^{d - i} = 0$$ in $S^{-1}B$. In this way we see that $S^{-1}B'$ is contained in the integral closure of $S^{-1}A$ in $S^{-1}B$. Conversely, suppose that $x/f \in S^{-1}B$ is integral over $S^{-1}A$. Then we have $$(x/f)^d + \sum\nolimits_{i = 1, \ldots, d} (a_i/f_i) (x/f)^{d - i} = 0$$ in $S^{-1}B$ for some $a_i \in A$ and $f_i \in S$. This means that $$(f'f_1 \ldots f_d x)^d +
\sum\nolimits_{i = 1, \ldots, d}
f^i(f')^if_1^i \ldots f_i^{i - 1} \ldots f_d^i a_i
(f'f_1 \ldots f_dx)^{d - i} = 0$$ for a suitable $f' \in S$. Hence $f'f_1\ldots f_dx \in B'$ and thus $x/f \in S^{-1}B'$ as desired. $\square$

#### Lemma. Base change for integral extensions

Integrality and finiteness are preserved under base change.

Let $R \to S$ and $R \to R'$ be ring maps. Set $S' = R' \otimes_R S$.

1.  If $R \to S$ is integral so is $R' \to S'$.

2.  If $R \to S$ is finite so is $R' \to S'$.

**Proof.** We prove (1). Let $s_i \in S$ be generators for $S$ over $R$. Each of these satisfies a monic polynomial equation $P_i$ over $R$. Hence the elements $1 \otimes s_i \in S'$ generate $S'$ over $R'$ and satisfy the corresponding polynomial $P_i'$ over $R'$. Since these elements generate $S'$ over $R'$ we see that $S'$ is integral over $R'$. Proof of (2) omitted. $\square$

#### Lemma. Commutative algebra
 Let $R \to S$ be a ring map.

1.  $R \to S$ satisfies going down if and only if generalizations lift along the map $\operatorname{Spec}(S) \to \operatorname{Spec}(R)$, see Topology, Definition [Lifting the geometric construction](#context-topology-definition-lift-specializations).

2.  $R \to S$ satisfies going up if and only if specializations lift along the map $\operatorname{Spec}(S) \to \operatorname{Spec}(R)$, see Topology, Definition [Lifting the geometric construction](#context-topology-definition-lift-specializations).

**Proof.** Omitted. $\square$

#### Lemma. Injective resolutions and prime spectra and associated points
 Let $R \subset S$ be an injective ring map. Then $\operatorname{Spec}(S) \to \operatorname{Spec}(R)$ hits all the minimal primes.

**Proof.** Let $\mathfrak p \subset R$ be a minimal prime. In this case $R_{\mathfrak p}$ has a unique prime ideal. Hence it suffices to show that $S_{\mathfrak p}$ is not zero. And this follows from the fact that localization is exact, see Proposition [Exactness of localization](#native-algebra-proposition-localization-exact). $\square$

#### Lemma. Localization of modules and local algebra

Let $R$ be a ring. Let $S \subset R$ be a multiplicative subset. The category of $S^{-1}R$-modules is equivalent to the category of $R$-modules $N$ with the property that every $s \in S$ acts as an automorphism on $N$.

**Proof.** The functor which defines the equivalence associates to an $S^{-1}R$-module $M$ the same module but now viewed as an $R$-module via the localization map $R \to S^{-1}R$. Conversely, if $N$ is an $R$-module, such that every $s \in S$ acts via an automorphism $s_N$, then we can think of $N$ as an $S^{-1}R$-module by letting $x/s$ act via $x_N  \circ s_N^{-1}$. We omit the verification that these two functors are quasi-inverse to each other. $\square$

#### Lemma. Exactness of Hom from a projective module

Exactness and $\operatorname{Hom}_R$. Let $R$ be a ring. Let $M_1$, $M_2$, $M_3$ be $R$-modules. Let $M_1 \to M_2$ and $M_2 \to M_3$ be $R$-module maps.

1.  $M_1 \to M_2 \to M_3 \to 0$ is exact if and only if $0 \to \operatorname{Hom}_R(M_3, N) \to \operatorname{Hom}_R(M_2, N) \to \operatorname{Hom}_R(M_1, N)$ is exact for all $R$-modules $N$.

2.  $0 \to M_1 \to M_2 \to M_3$ is exact if and only if $0 \to \operatorname{Hom}_R(N, M_1) \to \operatorname{Hom}_R(N, M_2) \to \operatorname{Hom}_R(N, M_3)$ is exact for all $R$-modules $N$.

**Proof.** Omitted. $\square$

#### Lemma. Filtered limits and proper morphisms and modules

Let $A$ be a ring and let $M, N$ be $A$-modules. Suppose that $R = \mathop{\operatorname{colim}}_{i \in I} R_i$ is a directed colimit of $A$-algebras.

1.  If $M$ is a finite $A$-module, and $u, u' : M \to N$ are $A$-module maps such that $u \otimes 1 = u' \otimes 1 : M \otimes_A R \to N \otimes_A R$ then for some $i$ we have $u \otimes 1 = u' \otimes 1 : M \otimes_A R_i \to N \otimes_A R_i$.

2.  If $N$ is a finite $A$-module and $u : M \to N$ is an $A$-module map such that $u \otimes 1 : M \otimes_A R \to N \otimes_A R$ is surjective, then for some $i$ the map $u \otimes 1 : M \otimes_A R_i \to N \otimes_A R_i$ is surjective.

3.  If $N$ is a finitely presented $A$-module, and $v : N \otimes_A R \to M \otimes_A R$ is an $R$-module map, then there exists an $i$ and an $R_i$-module map $v_i : N \otimes_A R_i \to M \otimes_A R_i$ such that $v = v_i \otimes 1$.

4.  If $M$ is a finite $A$-module, $N$ is a finitely presented $A$-module, and $u : M \to N$ is an $A$-module map such that $u \otimes 1 : M \otimes_A R \to N \otimes_A R$ is an isomorphism, then for some $i$ the map $u \otimes 1 : M \otimes_A R_i \to N \otimes_A R_i$ is an isomorphism.

**Proof.** To prove (1) assume $u$ is as in (1) and let $x_1, \ldots, x_m \in M$ be generators. Since $N \otimes_A R = \mathop{\operatorname{colim}}_i N \otimes_A R_i$ we may pick an $i \in I$ such that $u(x_j) \otimes 1 = u'(x_j) \otimes 1$ in $N \otimes_A R_i$, $j = 1, \ldots, m$. For such an $i$ we have $u \otimes 1 = u' \otimes 1 : M \otimes_A R_i \to N \otimes_A R_i$.

To prove (2) assume $u \otimes 1$ surjective and let $y_1, \ldots, y_m \in N$ be generators. Since $N \otimes_A R = \mathop{\operatorname{colim}}_i N \otimes_A R_i$ we may pick an $i \in I$ and $z_j \in M \otimes_A R_i$, $j = 1, \ldots, m$ whose images in $N \otimes_A R$ equal $y_j \otimes 1$. For such an $i$ the map $u \otimes 1 : M \otimes_A R_i \to N \otimes_A R_i$ is surjective.

To prove (3) let $y_1, \ldots, y_m \in N$ be generators. Let $K = \operatorname{Ker}(A^{\oplus m} \to N)$ where the map is given by the rule $(a_1, \ldots, a_m) \mapsto \sum a_j y_j$. Let $k_1, \ldots, k_t$ be generators for $K$. Say $k_s = (k_{s1}, \ldots, k_{sm})$. Since $M \otimes_A R = \mathop{\operatorname{colim}}_i M \otimes_A R_i$ we may pick an $i \in I$ and $z_j \in M \otimes_A R_i$, $j = 1, \ldots, m$ whose images in $M \otimes_A R$ equal $v(y_j \otimes 1)$. We want to use the $z_j$ to define the map $v_i : N \otimes_A R_i \to M \otimes_A R_i$. Since $K \otimes_A R_i \to R_i^{\oplus m} \to N \otimes_A R_i \to 0$ is a presentation, it suffices to check that $\xi_s = \sum_j k_{sj}z_j$ is zero in $M \otimes_A R_i$ for each $s = 1, \ldots, t$. This may not be the case, but since the image of $\xi_s$ in $M \otimes_A R$ is zero we see that it will be the case after increasing $i$ a bit.

To prove (4) assume $u \otimes 1$ is an isomorphism, that $M$ is finite, and that $N$ is finitely presented. Let $v : N \otimes_A R \to M \otimes_A R$ be an inverse to $u \otimes 1$. Apply part (3) to get a map $v_i : N \otimes_A R_i \to M \otimes_A R_i$ for some $i$. Apply part (1) to see that, after increasing $i$ we have $v_i \circ (u \otimes 1) = \text{id}_{M \otimes_A R_i}$ and $(u \otimes 1) \circ v_i = \text{id}_{N \otimes_A R_i}$. $\square$

#### Lemma. Regular rings
 Let $R$ be a ring. Let $M$ be an $R$-module. Let $f_1, \ldots, f_c \in R$ be an $M$-quasi-regular sequence. For any $i$ the sequence $\overline{f}_{i + 1}, \ldots, \overline{f}_c$ of $\overline{R} = R/(f_1, \ldots, f_i)$ is an $\overline{M} = M/(f_1, \ldots, f_i)M$-quasi-regular sequence.

**Proof.** It suffices to prove this for $i = 1$. Set $\overline{J} = (\overline{f}_2, \ldots, \overline{f}_c) \subset \overline{R}$. Then $$\begin{aligned}
\overline{J}^n\overline{M}/\overline{J}^{n + 1}\overline{M}
& =
(J^nM + f_1M)/(J^{n + 1}M + f_1M) \\
& = J^nM / (J^{n + 1}M + J^nM \cap f_1M).
\end{aligned}$$ For $n=0$, the displayed quotient is $M/JM$, as required. For $n \geq 1$, it suffices to show that $J^{n + 1}M + J^nM \cap f_1M = J^{n + 1}M + f_1J^{n - 1}M$ because that will show that $\bigoplus_{n \geq 0}
\overline{J}^n\overline{M}/\overline{J}^{n + 1}\overline{M}$ is the quotient of $\bigoplus_{n \geq 0} J^nM/J^{n + 1}M \cong M/JM[X_1, \ldots, X_c]$ by $X_1$. Actually, for $n \geq 1$, we have $J^nM \cap f_1M = f_1J^{n - 1}M$. Namely, if $m \not \in J^{n - 1}M$, then $f_1m \not \in J^nM$ because $\bigoplus J^nM/J^{n + 1}M$ is the polynomial module $(M/JM) \otimes_{R/J} (R/J)[X_1, \ldots, X_c]$ by assumption. $\square$

#### Lemma. Dimension and codimension
 Suppose $R$ is a Noetherian local Cohen-Macaulay ring of dimension $d$. For any prime $\mathfrak p \subset R$ we have $$\dim(R) = \dim(R_{\mathfrak p}) + \dim(R/\mathfrak p).$$

**Proof.** Follows immediately from Lemma [Maximal prime chains in a Cohen–Macaulay ring](#native-algebra-lemma-maximal-chain-cm). (Also, this is a special case of Lemma [Dimension and codimension (programme binding)](#uncovered-algebra-lemma-dim-formula-maximal-cm).) $\square$

#### Lemma. The equational criterion for a single module relation

Let $k$ be a field. Let $S = k[x_1, \ldots, x_n]/I$ for some proper ideal $I$. If $I \not = 0$, then there exist $y_1, \ldots, y_{n-1} \in k[x_1, \ldots, x_n]$ such that $S$ is finite over $k[y_1, \ldots, y_{n-1}]$. Moreover we may choose $y_i$ to be in the $\mathbf{Z}$-subalgebra of $k[x_1, \ldots, x_n]$ generated by $x_1, \ldots, x_n$.

**Proof.** Pick $f \in I$, $f\not = 0$. It suffices to show the lemma for $k[x_1, \ldots, x_n]/(f)$ since $S$ is a quotient of that ring. We will take $y_i = x_i - x_n^{e_i}$, $i = 1, \ldots, n-1$ for suitable integers $e_i$. When does this work? It suffices to show that $\overline{x_n} \in k[x_1, \ldots, x_n]/(f)$ is integral over the ring $k[y_1, \ldots, y_{n-1}]$. The equation for $\overline{x_n}$ over this ring is $$f(y_1 + x_n^{e_1}, \ldots, y_{n-1} + x_n^{e_{n-1}}, x_n) = 0.$$ Hence we are done if we can show there exist integers $e_i$ such that the leading coefficient with respect to $x_n$ of the equation above is a nonzero element of $k$. This can be achieved for example by choosing $e_1 \gg e_2 \gg \ldots \gg e_{n-1}$, see Lemma [Commutative algebra (programme binding)](#uncovered-algebra-lemma-helper-polynomial). $\square$

#### Lemma. Dimension, codimension and integral extensions
 Suppose $R \subset S$ and $S$ integral over $R$. Then $\dim(R) = \dim(S)$.

**Proof.** This is a combination of Lemmas [Going up for integral ring maps](#native-algebra-lemma-integral-going-up), [Surjectivity on spectra of an integral overring](#native-algebra-lemma-integral-overring-surjective), [Dimension and codimension (programme binding)](#uncovered-algebra-lemma-dimension-going-up), and [Dimension under an integral extension](#native-algebra-lemma-integral-dim-up). $\square$

#### Lemma. Dimension and codimension
 Let $R$ be a local Noetherian ring. The following are equivalent:

1.   $\dim(R) = 1$,

2.   $d(R) = 1$,

3.   there exists an $x \in \mathfrak m$, $x$ not nilpotent such that $V(x) = \{\mathfrak m\}$,

4.   there exists an $x \in \mathfrak m$, $x$ not nilpotent such that $\mathfrak m = \sqrt{(x)}$, and

5.  

    there exists an ideal of definition generated by $1$ element, and no ideal of definition is generated by $0$ elements.

**Proof.** First, assume that $\dim(R) = 1$. Let $\mathfrak p_i$ be the minimal primes of $R$. Because the dimension is $1$ the only other prime of $R$ is $\mathfrak m$. According to Lemma [Irreducible components of a Noetherian spectrum](#native-algebra-lemma-noetherian-irreducible-components) there are finitely many. Hence we can find $x \in \mathfrak m$, $x \not \in \mathfrak p_i$, see Lemma [An elementary algebraic comparison](#native-algebra-lemma-silly). Thus the only prime containing $x$ is $\mathfrak m$ and hence ([the indicated step](#native-algebra-item-vx)).

If ([the indicated step](#native-algebra-item-vx)) then $\mathfrak m = \sqrt{(x)}$ by Lemma [The Zariski topology on an affine spectrum](#native-algebra-lemma-zariski-topology), and hence ([the indicated step](#native-algebra-item-x)). The converse is clear as well. The equivalence of ([the indicated step](#native-algebra-item-x)) and ([the indicated step](#native-algebra-item-ideal-1)) follows directly from the definitions.

Assume ([the indicated step](#native-algebra-item-ideal-1)). Let $I = (x)$ be an ideal of definition. Note that $I^n/I^{n + 1}$ is a quotient of $R/I$ via multiplication by $x^n$ and hence $\text{length}_R(I^n/I^{n + 1})$ is bounded. Thus $d(R) = 0$ or $d(R) = 1$, but $d(R) = 0$ is excluded by the assumption that $0$ is not an ideal of definition.

Assume ([the indicated step](#native-algebra-item-d-1)). To get a contradiction, assume there exist primes \(\mathfrak p \subset \mathfrak q \subset \mathfrak m\), with both inclusions strict. Pick some ideal of definition \(I \subset R\). We will repeatedly use Lemma [Commutative algebra](#native-algebra-lemma-hilbert-ses-chi). First of all it implies, via the exact sequence \(0 \to \mathfrak p \to R \to R/\mathfrak p \to 0\), that \(d(R/\mathfrak p) \leq 1\). But it clearly cannot be zero. Pick \(x\in \mathfrak q\), \(x\not \in \mathfrak p\). Consider the short exact sequence 

\[
0 \to R/\mathfrak p \xrightarrow{x} R/\mathfrak p \to R/(xR + \mathfrak p) \to 0.
\]

 This implies that \(\chi_{I, R/\mathfrak p} - \chi_{I, R/\mathfrak p} - \chi_{I, R/(xR + \mathfrak p)} = - \chi_{I, R/(xR + \mathfrak p)}\) has degree \(< 1\). In other words, \(d(R/(xR + \mathfrak p)) = 0\), and hence \(\dim(R/(xR + \mathfrak p)) = 0\), by Lemma [Dimension and codimension](#native-algebra-lemma-dimension-0-d-0). But \(R/(xR + \mathfrak p)\) has the distinct primes \(\mathfrak q/(xR + \mathfrak p)\) and \(\mathfrak m/(xR + \mathfrak p)\) which gives the desired contradiction. \(\square\)

#### Lemma. Dimension and codimension
 Let $R$ be a Noetherian local ring. Then $\dim(R) = 0 \Leftrightarrow d(R) = 0$.

**Proof.** This is because $d(R) = 0$ if and only if $R$ has finite length as an $R$-module. See Lemma [Finite length over an Artinian ring](#native-algebra-lemma-artinian-finite-length). $\square$

#### Lemma. Commutative algebra

Let $R$ be a Noetherian local ring. Let $I \subset R$ be an ideal of definition. Let $0 \to M' \to M \to M'' \to 0$ be a short exact sequence of finite $R$-modules. Then

1.  if $M'$ does not have finite length, then $\chi_{I, M} - \chi_{I, M''} - \chi_{I, M'}$ is a numerical polynomial of degree $<$ the degree of $\chi_{I, M'}$,

2.  $\max\{ \deg(\chi_{I, M'}), \deg(\chi_{I, M''}) \} = \deg(\chi_{I, M})$, and

3.  $\max\{d(M'), d(M'')\} = d(M)$,

**Proof.** We first prove (1). Let $N \subset M'$ be as in Lemma [Commutative algebra (programme binding)](#uncovered-algebra-lemma-hilbert-ses). By Lemma [Finite algebras (programme binding)](#uncovered-algebra-lemma-differ-finite-chi) the numerical polynomial $\chi_{I, M'} - \chi_{I, N}$ has degree $<$ the common degree of $\chi_{I, M'}$ and $\chi_{I, N}$. By Lemma [Commutative algebra (programme binding)](#uncovered-algebra-lemma-hilbert-ses) the difference $$\chi_{I, M}(n) - \chi_{I, M''}(n) - \chi_{I, N}(n - c)$$ is constant for $n \gg 0$. By elementary calculus the difference $\chi_{I, N}(n) - \chi_{I, N}(n - c)$ has degree $<$ the degree of $\chi_{I, N}$ which is bigger than zero (see above). Putting everything together we obtain (1).

Note that the leading coefficients of $\chi_{I, M'}$ and $\chi_{I, M''}$ are nonnegative. Thus the degree of $\chi_{I, M'} + \chi_{I, M''}$ is equal to the maximum of the degrees. Thus if $M'$ does not have finite length, then (2) follows from (1). If $M'$ does have finite length, then $I^nM \to I^nM''$ is an isomorphism for all $n \gg 0$ by Artin-Rees (Lemma [The Artin–Rees lemma](#native-algebra-lemma-artin-rees)). Thus $M/I^nM \to M''/I^nM''$ is a surjection with kernel $M'$ for $n \gg 0$ and we see that $\chi_{I, M}(n) - \chi_{I, M''}(n) = \text{length}(M')$ for all $n \gg 0$. Thus (2) holds in this case also.

Proof of (3). This follows from (2) except if one of $M$, $M'$, or $M''$ is zero. We omit the proof in these special cases. $\square$

#### Lemma. Field extensions
 Let $k$ be a field. Let $S$ be a reduced $k$-algebra. Let $K/k$ be either a separable field extension, or a separably generated field extension. Then $K \otimes_k S$ is reduced.

**Proof.** Assume $k \subset K$ is separable. By Lemma [Filtered limits and commutative algebra (uncovered prerequisite)](#uncovered-algebra-lemma-limit-argument) we may assume that $S$ is of finite type over $k$ and $K$ is finitely generated over $k$. Then $S$ embeds into a finite product of fields, namely its total ring of fractions (see Lemmas [Localizations at minimal primes of a reduced ring](#native-algebra-lemma-minimal-prime-reduced-ring) and [Total rings of fractions without embedded primes](#native-algebra-lemma-total-ring-fractions-no-embedded-points)). Hence we may actually assume that $S$ is a domain. We choose $x_1, \ldots, x_{r + 1} \in K$ as in Lemma [Field extensions and finite algebras](#native-algebra-lemma-generating-finitely-generated-separable-field-extensions). Let $P \in k(x_1, \ldots, x_r)[T]$ be the minimal polynomial of $x_{r + 1}$. It is a separable polynomial. It is easy to see that $k[x_1, \ldots, x_r] \otimes_k S = S[x_1, \ldots, x_r]$ is a domain. This implies $k(x_1, \ldots, x_r) \otimes_k S$ is a domain as it is a localization of $S[x_1, \ldots, x_r]$. The ring extension $k(x_1, \ldots, x_r) \otimes_k S \subset K \otimes_k S$ is generated by a single element $x_{r + 1}$ with a single equation, namely $P$. Hence $K \otimes_k S$ embeds into $F[T]/(P)$ where $F$ is the fraction field of $k(x_1, \ldots, x_r) \otimes_k S$. Since $P$ is separable this is a finite product of fields and we win.

At this point we do not yet know that a separably generated field extension is separable, so we have to prove the lemma in this case also. To do this suppose that $\{x_i\}_{i \in I}$ is a separating transcendence basis for $K$ over $k$. For any finite set of elements $\lambda_j \in K$ there exists a finite subset $T \subset I$ such that $k(\{x_i\}_{i\in T}) \subset k(\{x_i\}_{i \in T} \cup \{\lambda_j\})$ is finite separable. Hence we see that $K$ is a directed colimit of finitely generated and separably generated extensions of $k$. Thus the argument of the preceding paragraph applies to this case as well. $\square$

#### Lemma. An elementary separability criterion

Let $k$ be a field of characteristic $p > 1$. Let $K/k$ be a field extension generated by $x_1, \ldots, x_{n + 1} \in K$ such that

1.  $\{x_1, \ldots, x_n\}$ is a transcendence base of $K/k$,

2.  for every $k$-linearly independent subset $\{a_1, \ldots, a_m\}$ of $K$ the set $\{a^p_1, \ldots, a_m^p\}$ is $k$-linearly independent.

Then there is $1 \leq j \leq n+1$ such that $\{ x_1, \ldots, \widehat{x}_j, \ldots, x_{n+1}\}$ is a separating transcendence base for $K / k$.

**Proof.** By assumption $x_{n + 1}$ is algebraic over $k(x_1, \ldots, x_n)$ so there exists a non-zero polynomial $F \in k[X_1, \ldots, X_{n + 1}]$ such that $F(x_1, \ldots, x_{n+1}) = 0$. Choose $F$ of minimal total degree. Then $F$ is irreducible, because at least one irreducible factor must also have the same property.

We claim that, for some $i$, not all powers of $X_i$ appearing in $F$ are multiples of $p$. Suppose for a contradiction that all the exponents appearing in $F$ were multiples of $p$, then the set $$\{x_1^{\alpha_1} \ldots x^{\alpha_{n+1}}_{n+1} \mid \lambda_\alpha \neq 0\}
\subset
K$$ is $k$-linearly dependent where $\lambda_\alpha$ are the coefficients of $F$. By assumption (2) we conclude the set $$\{x_1^{\alpha_1 / p} \ldots x^{\alpha_{n+1} / p}_{n+1}
\mid \lambda_\alpha \neq 0 \}$$ is also $k$-linearly dependent, contradicting minimality of $\deg(F)$.

Choose $i$ for which a non-$p$th power of $X_i$ appears in $F$. Then we see that $x_i$ is algebraic over $L = k(x_1, \ldots, x_{i - 1}, x_{i + 1}, \ldots, x_{n+1})$. By Fields, Lemma [The geometric construction (programme binding)](#uncovered-fields-lemma-transcendence-degree) we see that $x_1, \ldots, x_{i - 1}, x_{i + 1}, \ldots, x_{n+1}$ is a transcendence base of $K/k$. Thus $L$ is the fraction field of the polynomial ring over $k$ in $x_1, \ldots, x_{i - 1}, x_{i + 1}, \ldots, x_{n + 1}$. By Gauss' Lemma we conclude that $$P(T) =
F(x_1, \ldots, x_{i - 1}, T, x_{i + 1}, \ldots, x_{n + 1}) \in L[T]$$ is irreducible. By construction $P(T)$ is not contained in $L[T^p]$. Hence $K/L$ is separable as required. $\square$

#### Lemma. Formal smoothness and smooth morphisms

Let $A \to B \to C$ be ring maps. Assume $B \to C$ is formally smooth. Then the sequence $$0 \to \Omega_{B/A} \otimes_B C \to \Omega_{C/A} \to \Omega_{C/B} \to 0$$ of Lemma Kähler differentials, Theorems 3.1–3.3, Proposition 3.4 and Theorem 7.1 is a split short exact sequence.

**Proof.** Follows from Proposition [Characterizations of formal smoothness](#native-algebra-proposition-characterize-formally-smooth) and Lemma [The transitivity sequence for the naive cotangent complex](#native-algebra-lemma-exact-sequence-nl). $\square$

#### Lemma. Filtered limits and cotangent complexes and differentials

Let $I$ be a directed set. Let $(R_i \to S_i, \varphi_{ii'})$ be a system of ring maps over $I$, see Categories, Section [The geometric construction](#context-categories-section-posets-limits). Then we have $$\Omega_{S/R} =
\mathop{\operatorname{colim}}_i \Omega_{S_i/R_i},$$ where $R \to S = \mathop{\operatorname{colim}} (R_i \to S_i)$.

**Proof.** This is clear from the defining presentation of $\Omega_{S/R}$ and the functoriality of this described above. $\square$

#### Lemma. Field extensions and finite algebras
 Let $K/k$ be a separably generated, and finitely generated field extension. Set $r = \text{trdeg}_k(K)$. Then there exist elements $x_1, \ldots, x_{r + 1}$ of $K$ such that

1.  $x_1, \ldots, x_r$ is a transcendence basis of $K$ over $k$,

2.  $K = k(x_1, \ldots, x_{r + 1})$, and

3.  $x_{r + 1}$ is separable over $k(x_1, \ldots, x_r)$.

**Proof.** Combine the definition with Fields, Lemma [The geometric construction (programme binding)](#uncovered-fields-lemma-primitive-element). $\square$

#### Lemma. Cotangent complexes, differentials and local algebra
 Let $\varphi : A \to B$ be a ring map.

1.  If $S \subset A$ is a multiplicative subset mapping to invertible elements of $B$, then $\Omega_{B/A} = \Omega_{B/S^{-1}A}$.

2.  If $S \subset B$ is a multiplicative subset then $S^{-1}\Omega_{B/A} = \Omega_{S^{-1}B/A}$.

**Proof.** To show the equality of (1) it is enough to show that any $A$-derivation $D : B \to M$ annihilates the elements $\varphi(s)^{-1}$. This is clear from the Leibniz rule applied to $1 = \varphi(s) \varphi(s)^{-1}$. To show (2), note that there is an obvious map $S^{-1}\Omega_{B/A} \to \Omega_{S^{-1}B/A}$. To show it is an isomorphism it is enough to show that there is an $A$-derivation $\text{d}'$ of $S^{-1}B$ into $S^{-1}\Omega_{B/A}$. To define it we simply set $\text{d}'(b/s) = (1/s)\text{d}b - (1/s^2)b\text{d}s$. Details omitted. $\square$

#### Definition. Perfect complexes
 Let $k$ be a field. We say $k$ is *perfect* if every field extension of $k$ is separable over $k$.

#### Lemma. Commutative algebra
 Let $K/k$ be a finitely generated field extension. There exists a diagram $$\begin{gathered}\begin{matrix}K & K' \\ k & k'\end{matrix} \\[6pt] \begin{aligned}K & \longrightarrow K' \\ k & \longrightarrow K \\ k & \longrightarrow k' \\ k' & \longrightarrow K'\end{aligned}\end{gathered}$$ where $k'/k$, $K'/K$ are finite purely inseparable field extensions such that $K'/k'$ is a separably generated field extension.

**Proof.** This lemma is only interesting when the characteristic of $k$ is $p > 0$. Choose $x_1, \ldots, x_r$ a transcendence basis of $K$ over $k$. As $K$ is finitely generated over $k$ the extension $k(x_1, \ldots, x_r) \subset K$ is finite. Let $K/K_{sep}/k(x_1, \ldots, x_r)$ be the subextension found in Fields, Lemma [Field extensions (programme binding)](#uncovered-fields-lemma-separable-first). If $K = K_{sep}$ then we are done. We will use induction on $d = [K : K_{sep}]$.

Assume that $d > 1$. Choose a $\beta \in K$ with $\alpha = \beta^p \in K_{sep}$ and $\beta \not \in K_{sep}$. Let $P = T^n + a_1T^{n - 1} + \ldots + a_n$ be the minimal polynomial of $\alpha$ over $k(x_1, \ldots, x_r)$. Let $k'/k$ be a finite purely inseparable extension obtained by adjoining $p$th roots such that each $a_i$ is a $p$th power in $k'(x_1^{1/p}, \ldots, x_r^{1/p})$. Such an extension exists; details omitted. Let $L$ be a field fitting into the diagram $$\begin{gathered}\begin{matrix}K & L \\ k(x_1, \ldots, x_r) & k'(x_1^{1/p}, \ldots, x_r^{1/p})\end{matrix} \\[6pt] \begin{aligned}K & \longrightarrow L \\ k(x_1, \ldots, x_r) & \longrightarrow K \\ k(x_1, \ldots, x_r) & \longrightarrow k'(x_1^{1/p}, \ldots, x_r^{1/p}) \\ k'(x_1^{1/p}, \ldots, x_r^{1/p}) & \longrightarrow L\end{aligned}\end{gathered}$$ We may and do assume $L$ is the compositum of $K$ and $k'(x_1^{1/p}, \ldots, x_r^{1/p})$. Let $L/L_{sep}/k'(x_1^{1/p}, \ldots, x_r^{1/p})$ be the subextension found in Fields, Lemma [Field extensions (programme binding)](#uncovered-fields-lemma-separable-first). Then $L_{sep}$ is the compositum of $K_{sep}$ and $k'(x_1^{1/p}, \ldots, x_r^{1/p})$. The element $\alpha \in L_{sep}$ is a zero of the polynomial $P$ all of whose coefficients are $p$th powers in $k'(x_1^{1/p}, \ldots, x_r^{1/p})$ and whose roots are pairwise distinct. By Fields, Lemma [Field extensions (programme binding)](#uncovered-fields-lemma-pth-root) we see that $\alpha = (\alpha')^p$ for some $\alpha' \in L_{sep}$. Clearly, this means that $\beta$ maps to $\alpha' \in L_{sep}$. In other words, we get the tower of fields $$\begin{gathered}\begin{matrix}K & L \\ K_{sep}(\beta) & L_{sep} \\ K_{sep} & L_{sep} \\ k(x_1, \ldots, x_r) & k'(x_1^{1/p}, \ldots, x_r^{1/p}) \\ k & k'\end{matrix} \\[6pt] \begin{aligned}K & \longrightarrow L \\ K_{sep}(\beta) & \longrightarrow L_{sep} \\ K_{sep}(\beta) & \longrightarrow K \\ L_{sep} & \longrightarrow L \\ K_{sep} & \longrightarrow L_{sep} \\ K_{sep} & \longrightarrow K_{sep}(\beta) \\ L_{sep} & \mathrel{=} L_{sep} \\ k(x_1, \ldots, x_r) & \longrightarrow K_{sep} \\ k(x_1, \ldots, x_r) & \longrightarrow k'(x_1^{1/p}, \ldots, x_r^{1/p}) \\ k'(x_1^{1/p}, \ldots, x_r^{1/p}) & \longrightarrow L_{sep} \\ k & \longrightarrow k' \\ k & \longrightarrow k(x_1, \ldots, x_r) \\ k' & \longrightarrow k'(x_1^{1/p}, \ldots, x_r^{1/p})\end{aligned}\end{gathered}$$ Thus this construction leads to a new situation with $[L : L_{sep}] < [K : K_{sep}]$. By induction we can find $k' \subset k''$ and $L \subset L'$ as in the lemma for the extension $L/k'$. Then the extensions $k''/k$ and $L'/K$ work for the extension $K/k$. This proves the lemma. $\square$

#### Lemma. Field extensions
 A separably generated field extension is separable.

**Proof.** Combine Lemma [Field extensions](#native-algebra-lemma-separable-extension-preserves-reducedness) with Lemma [Criteria for a separable field extension](#native-algebra-lemma-characterize-separable-field-extensions). $\square$

#### Lemma. Field extensions
 Let $K/k$ be a separable field extension. For any subextension $K/K'/k$ the field extension $K'/k$ is separable.

**Proof.** This is direct from the definition. $\square$

#### Lemma. Criteria for flatness

Let $R$ be a ring. Let $M$ be an $R$-module. The following are equivalent:

1.  The module $M$ is flat over $R$.

2.  For all $i > 0$ the functor $\text{Tor}_i^R(M, -)$ is zero.

3.  The functor $\text{Tor}_1^R(M, -)$ is zero.

4.  For all ideals $I \subset R$ we have $\text{Tor}_1^R(M, R/I) = 0$.

5.  For all finitely generated ideals $I \subset R$ we have $\text{Tor}_1^R(M, R/I) = 0$.

**Proof.** Suppose $M$ is flat. Let $N$ be an $R$-module. Let $F_\bullet$ be a free resolution of $N$. Then $F_\bullet \otimes_R M$ is a resolution of $N \otimes_R M$, by flatness of $M$. Hence all higher Tor groups vanish.

It now suffices to show that the last condition implies that $M$ is flat. Let $I \subset R$ be an ideal. Consider the short exact sequence $0 \to I \to R \to R/I \to 0$. Apply Lemma [Derived tensor products and Tor amplitude (programme binding)](#uncovered-algebra-lemma-long-exact-sequence-tor). We get an exact sequence $$\text{Tor}_1^R(M, R/I) \to
M \otimes_R I \to
M \otimes_R R \to
M \otimes_R R/I \to
0$$ Since obviously $M \otimes_R R = M$ we conclude that the last hypothesis implies that $M \otimes_R I \to M$ is injective for every finitely generated ideal $I$. Thus $M$ is flat by Lemma [Flatness](#native-algebra-lemma-flat). $\square$

#### Lemma. Finite algebras
 Let $R \to S$ be a ring map. Let $M$ be an $S$-module. If $M$ is finite as an $R$-module, then $M$ is finite as an $S$-module.

**Proof.** In fact, any $R$-generating set of $M$ is also an $S$-generating set of $M$, since the $R$-module structure is induced by the image of $R$ in $S$. $\square$

#### Lemma. Criteria for commutative algebra

Let $R$ be a ring. Let $M$ be an $R$-module. The following are equivalent:

1.  $M$ is simple,

2.  $\text{length}_R(M) = 1$, and

3.  $M \cong R/\mathfrak m$ for some maximal ideal $\mathfrak m \subset R$.

**Proof.** Let $\mathfrak m$ be a maximal ideal of $R$. By Lemma [Vector-space dimension and module length](#native-algebra-lemma-dimension-is-length) the module $R/\mathfrak m$ has length $1$. The equivalence of the first two assertions is tautological. Suppose that $M$ is simple. Choose $x \in M$, $x \not = 0$. As $M$ is simple we have $M = R \cdot x$. Let $I \subset R$ be the annihilator of $x$, i.e., $I = \{f \in R \mid fx = 0\}$. The map $R/I \to M$, $f \bmod I \mapsto fx$ is an isomorphism, hence $R/I$ is a simple $R$-module. Since $R/I \not = 0$ we see $I \not = R$. Let $\mathfrak m$ be a maximal ideal containing $I$. If $I \not = \mathfrak m$, then $\mathfrak m /I \subset R/I$ is a nontrivial submodule contradicting the simplicity of $R/I$. Hence we see $I = \mathfrak m$ as desired. $\square$

#### Lemma. Independence of a composition series
 Let $R \to S$ be a ring map. Let $M$ be an $S$-module. We always have $\text{length}_R(M) \geq \text{length}_S(M)$. If $R \to S$ is surjective then equality holds.

**Proof.** A filtration of $M$ by $S$-submodules gives rise a filtration of $M$ by $R$-submodules. This proves the inequality. And if $R \to S$ is surjective, then any $R$-submodule of $M$ is automatically an $S$-submodule. Hence equality in this case. $\square$

#### Lemma. Commutative algebra
 Let $k$ be a field. If $R$ is geometrically reduced over $k$, and $S \subset R$ is a multiplicative subset, then the localization $S^{-1}R$ is geometrically reduced over $k$. If $R$ is geometrically reduced over $k$, then $R[x]$ is geometrically reduced over $k$.

**Proof.** Omitted. Hints: A localization of a reduced ring is reduced, and localization commutes with tensor products. $\square$

#### Lemma. Finite presentation and finite algebras

Let $R \subset S$ be an inclusion of domains. Assume that $R \to S$ is of finite type. There exists a nonzero $f \in R$, and a nonzero $g \in S$ such that $R_f \to S_{fg}$ is of finite presentation.

**Proof.** By induction on the number of generators of $S$ over $R$. During the proof we may replace $R$ by $R_f$ and $S$ by $S_f$ for some nonzero $f \in R$.

Suppose that $S$ is generated by a single element over $R$. Then $S = R[x]/\mathfrak q$ for some prime ideal $\mathfrak q \subset R[x]$. If $\mathfrak q = (0)$ there is nothing to prove. If $\mathfrak q \not = (0)$, then let $h \in \mathfrak q$ be a nonzero element with minimal degree in $x$. Write $h = f x^d + a_{d - 1} x^{d - 1} + \ldots + a_0$ with $a_i \in R$ and $f \not = 0$. After inverting $f$ in $R$ and $S$ we may assume that $h$ is monic. We obtain a surjective $R$-algebra map $R[x]/(h) \to S$. We have $R[x]/(h) = R \oplus Rx \oplus \ldots \oplus Rx^{d - 1}$ as an $R$-module and by minimality of $d$ we see that $R[x]/(h)$ maps injectively into $S$. Thus $R[x]/(h) \cong S$ is finitely presented over $R$.

Suppose that $S$ is generated by $n > 1$ elements over $R$. Say $x_1, \ldots, x_n \in S$ generate $S$. Denote $S' \subset S$ the $R$-subalgebra generated by $x_1, \ldots, x_{n-1}$. By induction hypothesis we see that there exist $f\in R$ and $g \in S'$ nonzero such that $R_f \to S'_{fg}$ is of finite presentation. Next we apply the induction hypothesis to $S'_{fg} \to S_{fg}$ to see that there exist $f' \in S'_{fg}$ and $g' \in S_{fg}$ such that $S'_{fgf'} \to S_{fgf'g'}$ is of finite presentation. We leave it to the reader to conclude. $\square$

#### Lemma. Smooth morphisms and field extensions
 Let $k$ be a field. Let $S$ be a finite type $k$-algebra. Let $\mathfrak q \subset S$ be a prime. Assume $\kappa(\mathfrak q)$ is separable over $k$. The following are equivalent:

1.  The algebra $S$ is smooth at $\mathfrak q$ over $k$.

2.  The ring $S_{\mathfrak q}$ is regular.

**Proof.** Let \(R = S_{\mathfrak q}\) and denote its maximal ideal by \(\mathfrak m\) and its residue field by \(\kappa\). By Lemmas [Cotangent complexes and differentials (programme binding)](#uncovered-algebra-lemma-computation-differential) and [Cotangent complexes and differentials](#native-algebra-lemma-differential-seq) we see that there is a short exact sequence 

\[
0 \to \mathfrak m/\mathfrak m^2 \to
\Omega_{R/k} \otimes_R \kappa \to
\Omega_{\kappa/k} \to 0
\]

 Note that \(\Omega_{R/k} = \Omega_{S/k, \mathfrak q}\), see Lemma [Cotangent complexes, differentials and local algebra](#native-algebra-lemma-differentials-localize). Moreover, since \(\kappa\) is separable over \(k\) we have \(\dim_{\kappa} \Omega_{\kappa/k} = \text{trdeg}_k(\kappa)\). Hence we get 

\[
\dim_{\kappa} \Omega_{R/k} \otimes_R \kappa
=
\dim_\kappa \mathfrak m/\mathfrak m^2 + \text{trdeg}_k (\kappa)
\geq
\dim R + \text{trdeg}_k (\kappa)
=
\dim_{\mathfrak q} S
\]

 (see Lemma [Dimension, codimension and field extensions](#native-algebra-lemma-dimension-at-a-point-finite-type-field) for the last equality) with equality if and only if \(R\) is regular. Thus we win by applying Lemma Smooth algebras over a field and the Jacobian criterion, Theorems 5.1–6.1 and Sections 1–3. \(\square\)

#### Theorem. Zariski's main theorem in affine algebra
 Let $R$ be a ring. Let $S$ be a finite type $R$-algebra. Let $S' \subset S$ be the integral closure of $R$ in $S$. Let $\mathfrak q \subset S$ be a prime of $S$. If $R \to S$ is quasi-finite at $\mathfrak q$ then there exists a $g \in S'$, $g \not \in \mathfrak q$ such that $S'_g \cong S_g$.

**Proof.** There exist finitely many elements $x_1, \ldots, x_n \in S$ such that $S$ is finite over the $R$-subalgebra generated by $x_1, \ldots, x_n$. (For example, generators of $S$ over $R$.) We prove the theorem by induction on the minimal such number $n$.

The case $n = 0$ is trivial, because in this case $S' = S$, see Lemma [Integral extensions and finite algebras](#native-algebra-lemma-finite-is-integral).

The case $n = 1$. We may replace $R$ by its integral closure in $S$ (Lemma [Finite algebras (programme binding)](#uncovered-algebra-lemma-quasi-finite-permanence) guarantees that $R \to S$ is still quasi-finite at $\mathfrak q$). Thus we may assume $R \subset S$ is integrally closed in $S$, in other words $R = S'$. Consider the map $\varphi : R[x] \to S$, $x \mapsto x_1$. (We will see that $\varphi$ is not injective below.) By assumption $\varphi$ is finite. Hence we are in Situation [Commutative algebra](#context-algebra-situation-one-transcendental-element). Let $J \subset S$ be the "conductor ideal" defined in Situation [Commutative algebra](#context-algebra-situation-one-transcendental-element). Consider the diagram $$\begin{gathered}\begin{matrix}R[x] & S & S/\sqrt{J} & R/(R \cap \sqrt{J})[x] \\ \phantom{X} & R & R/(R \cap \sqrt{J}) & \phantom{X}\end{matrix} \\[6pt] \begin{aligned}R[x] & \longrightarrow S \\ S & \longrightarrow S/\sqrt{J} \\ R/(R \cap \sqrt{J})[x] & \longrightarrow S/\sqrt{J} \\ R & \longrightarrow R[x] \\ R & \longrightarrow R/(R \cap \sqrt{J}) \\ R & \longrightarrow S \\ R/(R \cap \sqrt{J}) & \longrightarrow S/\sqrt{J} \\ R/(R \cap \sqrt{J}) & \longrightarrow R/(R \cap \sqrt{J})[x]\end{aligned}\end{gathered}$$ According to Lemma [Commutative algebra (programme binding)](#uncovered-algebra-lemma-all-coefficients-in-j) the image of $x$ in the quotient $S/\sqrt{J}$ is strongly transcendental over $R/ (R \cap \sqrt{J})$. Hence by Lemma [Finite algebras (programme binding)](#uncovered-algebra-lemma-reduced-strongly-transcendental-not-quasi-finite) the ring map $R/ (R \cap \sqrt{J}) \to S/\sqrt{J}$ is not quasi-finite at any prime of $S/\sqrt{J}$. By Lemma [Commutative algebra (programme binding)](#uncovered-algebra-lemma-four-rings) we deduce that $\mathfrak q$ does not lie in $V(J) \subset \operatorname{Spec}(S)$. Thus there exists an element $s \in J$, $s \not\in \mathfrak q$. By definition of $J$ we may write $s = \varphi(f)$ for some polynomial $f \in R[x]$. Let $I = \operatorname{Ker}(\varphi : R[x] \to S)$. Since $\varphi(f) \in J$ we get $(R[x]/I)_f \cong S_{\varphi(f)}$. Also $s \not \in \mathfrak q$ means that $f \not \in \varphi^{-1}(\mathfrak q)$. Thus $\varphi^{-1}(\mathfrak q)/I$ is a prime of $R[x]/I$ at which $R \to R[x]/I$ is quasi-finite, see Lemma [Finite algebras and local algebra (programme binding)](#uncovered-algebra-lemma-quasi-finite-local). Note that $R$ is integrally closed in $R[x]/I$ since $R$ is integrally closed in $S$. By Lemma [Finite algebras (programme binding)](#uncovered-algebra-lemma-quasi-finite-monogenic) there exists an element $h \in R$, $h \not \in R \cap \mathfrak q$ such that $R_h \cong (R[x]/I)_h$. Thus $(R[x]/I)_{fh} = S_{\varphi(fh)}$ is isomorphic to a principal localization $R_{h'}$ of $R$ for some $h' \in R$, $h' \not \in \mathfrak q$.

The case $n > 1$. Consider the subring $R' \subset S$ which is the integral closure of $R[x_1, \ldots, x_{n-1}]$ in $S$. By Lemma [Finite algebras (programme binding)](#uncovered-algebra-lemma-quasi-finite-permanence) the extension $S/R'$ is quasi-finite at $\mathfrak q$. Also, note that $S$ is finite over $R'[x_n]$. By the case $n = 1$ above, there exists a $g' \in R'$, $g' \not \in \mathfrak q$ such that $(R')_{g'} \cong S_{g'}$. At this point we cannot apply induction to $R \to R'$ since $R'$ may not be finite type over $R$. Since $S$ is finitely generated over $R$ we deduce in particular that $(R')_{g'}$ is finitely generated over $R$. Say the elements $g'$, and $y_1/(g')^{n_1}, \ldots, y_N/(g')^{n_N}$ with $y_i \in R'$ generate $(R')_{g'}$ over $R$. Let $R''$ be the $R$-subalgebra of $R'$ generated by $x_1, \ldots, x_{n-1}, y_1, \ldots, y_N, g'$. This has the property $(R'')_{g'} \cong S_{g'}$. Surjectivity follows from the choice of the $y_i$; injectivity follows from $R'' \subset R'$ and the exactness of localization. Note that $R''$ is finite over $R[x_1, \ldots, x_{n-1}]$ because of our choice of $R'$, see Lemma [Criteria for integral extensions](#native-algebra-lemma-characterize-integral). Let $\mathfrak q'' = R'' \cap \mathfrak q$. Since $(R'')_{\mathfrak q''} = S_{\mathfrak q}$ we see that $R \to R''$ is quasi-finite at $\mathfrak q''$, see Lemma [An isolated point of a fibre](#native-algebra-lemma-isolated-point-fibre). We apply our induction hypothesis to $R \to R''$, $\mathfrak q''$ and $x_1, \ldots, x_{n-1} \in R''$ and we find a subring $R''' \subset R''$ which is integral over $R$ and an element $g'' \in R'''$, $g'' \not \in \mathfrak q''$ such that $(R''')_{g''} \cong (R'')_{g''}$. Write the image of $g'$ in $(R'')_{g''}$ as $g'''/(g'')^n$ for some $g''' \in  R'''$. Set $g = g''g''' \in R'''$. Then it is clear that $g \not\in
\mathfrak q$ and $(R''')_g \cong S_g$. Since by construction we have $R''' \subset S'$ we also have $S'_g \cong S_g$ as desired. $\square$

#### Lemma. Dimension, codimension and finite algebras
 Suppose $R$ is a finite dimensional algebra over a field. Then $R$ is Artinian.

**Proof.** The descending chain condition for ideals obviously holds. $\square$

#### Lemma. Dimension, codimension and Noetherian rings

A Noetherian ring of dimension $0$ is Artinian. Conversely, any Artinian ring is Noetherian of dimension at most zero.

**Proof.** Assume $R$ is a Noetherian ring of dimension $0$. By Lemma [The topology of a Noetherian spectrum](#native-algebra-lemma-noetherian-topology) the space $\operatorname{Spec}(R)$ is Noetherian. By Topology, Lemma [Noetherian topological spaces (programme binding)](#uncovered-topology-lemma-noetherian) we see that $\operatorname{Spec}(R)$ has finitely many irreducible components, say $\operatorname{Spec}(R) = Z_1 \cup \ldots \cup Z_r$. According to Lemma [Irreducibility of an affine spectrum](#native-algebra-lemma-irreducible) each $Z_i = V(\mathfrak p_i)$ with $\mathfrak p_i$ a minimal prime ideal. Since the dimension is $0$ these $\mathfrak p_i$ are also maximal. Thus $\operatorname{Spec}(R)$ is the discrete topological space with elements $\mathfrak p_i$. All elements $f$ of the Jacobson radical $\bigcap \mathfrak p_i$ are nilpotent since otherwise $R_f$ would not be the zero ring and we would have another prime. By Lemma [Local factors of a product ring](#native-algebra-lemma-product-local) $R$ is equal to $\prod R_{\mathfrak p_i}$. Since $R_{\mathfrak p_i}$ is also Noetherian and dimension $0$, the previous arguments show that its radical $\mathfrak p_iR_{\mathfrak p_i}$ is locally nilpotent. Lemma [Noetherian rings (programme binding)](#uncovered-algebra-lemma-noetherian-power) gives $\mathfrak p_i^nR_{\mathfrak p_i} = 0$ for some $n \geq 1$. By Lemma [Finite algebras (programme binding)](#uncovered-algebra-lemma-length-finite) we conclude that $R_{\mathfrak p_i}$ has finite length over $R$. Hence we conclude that $R$ is Artinian by Lemma [Finite length over an Artinian ring](#native-algebra-lemma-artinian-finite-length).

If $R$ is an Artinian ring then by Lemma [Finite length over an Artinian ring](#native-algebra-lemma-artinian-finite-length) it is Noetherian. All of its primes are maximal by a combination of Lemmas [Finitely many maximal ideals in an Artinian ring](#native-algebra-lemma-artinian-finite-nr-max), [Nilpotence of the radical of an Artinian ring](#native-algebra-lemma-artinian-radical-nilpotent) and [Local factors of a product ring](#native-algebra-lemma-product-local). $\square$

#### Proposition. Regular rings and dimension and codimension

Let $(R, \mathfrak m, \kappa)$ be a Noetherian local ring. The following are equivalent

1.  $\kappa$ has finite projective dimension as an $R$-module,

2.  $R$ has finite global dimension,

3.  $R$ is a regular local ring.

Moreover, in this case the global dimension of $R$ equals $\dim(R) = \dim_\kappa(\mathfrak m/\mathfrak m^2)$.

**Proof.** We have (3) $\Rightarrow$ (2) by Proposition [Regular rings and dimension and codimension (programme binding)](#uncovered-algebra-proposition-regular-finite-gl-dim). The implication (2) $\Rightarrow$ (1) is trivial. Assume (1). By Lemmas [Field extensions (programme binding)](#uncovered-algebra-lemma-length-resolution-residue-field) and [Dimension and codimension (programme binding)](#uncovered-algebra-lemma-dim-gl-dim) we see that $\dim(R) \geq \dim_\kappa(\mathfrak m /\mathfrak m^2)$. Thus $R$ is regular, see Definition [Regular local rings](#native-algebra-definition-regular-local) and the discussion preceding it. Assume the equivalent conditions (1) -- (3) hold. By Proposition [Regular rings and dimension and codimension (programme binding)](#uncovered-algebra-proposition-regular-finite-gl-dim) the global dimension of $R$ is at most $\dim(R)$ and by Lemma [Field extensions (programme binding)](#uncovered-algebra-lemma-length-resolution-residue-field) it is at least $\dim_\kappa(\mathfrak m/\mathfrak m^2)$. Thus the stated equality holds. $\square$

#### Lemma. Independence of a projective resolution

Let $R$ be a ring. Suppose that $M$ is an $R$-module of projective dimension $d$. Suppose that $F_e \to F_{e-1} \to \ldots \to F_0 \to M \to 0$ is exact with $F_i$ projective and $e \geq d - 1$. Then the kernel of $F_e \to F_{e-1}$ is projective (or the kernel of $F_0 \to M$ is projective in case $e = 0$).

**Proof.** We prove this by induction on $d$. If $d = 0$, then $M$ is projective. In this case there is a splitting $F_0 = \operatorname{Ker}(F_0 \to M) \oplus M$, and hence $\operatorname{Ker}(F_0 \to M)$ is projective. This finishes the proof if $e = 0$, and if $e > 0$, then replacing $M$ by $\operatorname{Ker}(F_0 \to M)$ we decrease $e$.

Next assume $d > 0$. Let $0 \to P_d \to P_{d-1} \to \ldots \to P_0 \to M \to 0$ be a minimal length finite resolution with $P_i$ projective. According to Schanuel's Lemma [Commutative algebra (programme binding)](#uncovered-algebra-lemma-schanuel) we have $P_0 \oplus \operatorname{Ker}(F_0 \to M) \cong F_0 \oplus \operatorname{Ker}(P_0 \to M)$. This proves the case $d = 1$, $e = 0$, because then the right hand side is $F_0 \oplus P_1$ which is projective. Hence now we may assume $e > 0$. The module $F_0 \oplus \operatorname{Ker}(P_0 \to M)$ has the finite projective resolution $$0 \to P_d \to P_{d-1} \to \ldots \to
P_2 \to P_1 \oplus F_0 \to \operatorname{Ker}(P_0 \to M) \oplus F_0 \to 0$$ of length $d - 1$. By induction applied to the exact sequence $$F_e \to F_{e-1} \to \ldots \to F_2 \to P_0 \oplus F_1 \to
P_0 \oplus \operatorname{Ker}(F_0 \to M) \to 0$$ of length $e - 1$ we conclude $\operatorname{Ker}(F_e \to F_{e - 1})$ is projective (if $e \geq 2$) or that $\operatorname{Ker}(F_1 \oplus P_0 \to F_0 \oplus P_0)$ is projective. This implies the lemma. $\square$

#### Lemma. Restriction of scalars for a finite module
 Let $A$ be a local ring with maximal ideal $\mathfrak m$. Let $B$ be a semi-local ring with maximal ideals $\mathfrak m_i$, $i = 1, \ldots, n$. Suppose that $A \to B$ is a homomorphism such that each $\mathfrak m_i$ lies over $\mathfrak m$ and such that $$[\kappa(\mathfrak m_i) : \kappa(\mathfrak m)] < \infty.$$ Let $M$ be a $B$-module of finite length. Then $$\text{length}_A(M) = \sum\nolimits_{i = 1, \ldots, n}
[\kappa(\mathfrak m_i) : \kappa(\mathfrak m)]
\text{length}_{B_{\mathfrak m_i}}(M_{\mathfrak m_i}),$$ in particular $\text{length}_A(M) < \infty$.

**Proof.** Choose a maximal chain $$0 = M_0
\subset M_1
\subset M_2
\subset \ldots
\subset M_m = M$$ by $B$-submodules as in Lemma [Commutative algebra (programme binding)](#uncovered-algebra-lemma-simple-pieces). Then each quotient $M_j/M_{j - 1}$ is isomorphic to $\kappa(\mathfrak m_{i(j)})$ for some $i(j) \in \{1, \ldots, n\}$. Moreover $\text{length}_A(\kappa(\mathfrak m_i)) =
[\kappa(\mathfrak m_i) : \kappa(\mathfrak m)]$ by Lemma [Vector-space dimension and module length](#native-algebra-lemma-dimension-is-length). The lemma follows by additivity of lengths (Lemma [Commutative algebra (programme binding)](#uncovered-algebra-lemma-length-additive)). $\square$

#### Lemma. Integral extensions and finite algebras

A finite ring map is integral.

**Proof.** Let $R \to S$ be finite. Let $y \in S$. Apply Lemma [Criteria for integral extensions (programme binding)](#uncovered-algebra-lemma-characterize-integral-element) to $M = S$ to see that $y$ is integral over $R$. $\square$

#### Lemma. Criteria for integral extensions and finite algebras

Let $R \to S$ be a ring map. The following are equivalent

1.  $R \to S$ is finite,

2.  $R \to S$ is integral and of finite type, and

3.  there exist $x_1, \ldots, x_n \in S$ which generate $S$ as an algebra over $R$ such that each $x_i$ is integral over $R$.

**Proof.** Clear from Lemma [Criteria for integral extensions](#native-algebra-lemma-characterize-integral). $\square$

#### Lemma. Complete rings and formal power series
 Let $R$ be a ring. Let $I \subset R$ be an ideal. Let $\varphi : M \to N$ be a map of $R$-modules.

1.  If $M/IM \to N/IN$ is surjective, then $M^\wedge \to N^\wedge$ is surjective.

2.  If $M \to N$ is surjective, then $M^\wedge \to N^\wedge$ is surjective.

3.  If $0 \to K \to M \to N \to 0$ is a short exact sequence of $R$-modules and $N$ is flat, then $0 \to K^\wedge \to M^\wedge \to N^\wedge \to 0$ is a short exact sequence.

4.  The map $M \otimes_R R^\wedge \to M^\wedge$ is surjective for any finite $R$-module $M$.

**Proof.** Assume $M/IM \to N/IN$ is surjective. Then the map $M/I^nM \to N/I^nN$ is surjective for each $n \geq 1$ by Nakayama's lemma. More precisely, apply Lemma [Nakayama's lemma](#native-algebra-lemma-nak) part (11) to the map $M/I^nM \to N/I^nN$ over the ring $R/I^n$ and the nilpotent ideal $I/I^n$ to see this. Set $K_n = \{x \in M \mid \varphi(x) \in I^nN\}$. Thus we get short exact sequences $$0 \to K_n/I^nM \to M/I^nM \to N/I^nN \to 0$$ We claim that the canonical map $K_{n + 1}/I^{n + 1}M \to K_n/I^nM$ is surjective. Namely, if $x \in K_n$ write $\varphi(x) = \sum z_j n_j$ with $z_j \in I^n$, $n_j \in N$. By assumption we can write $n_j = \varphi(m_j) + \sum z_{jk}n_{jk}$ with $m_j \in M$, $z_{jk} \in I$ and $n_{jk} \in N$. Hence $$\varphi(x - \sum z_j m_j) = \sum z_jz_{jk} n_{jk}.$$ This means that $x' = x - \sum z_j m_j \in K_{n + 1}$ maps to $x \bmod I^nM$ which proves the claim. Now we may apply Lemma [Commutative algebra (programme binding)](#uncovered-algebra-lemma-mittag-leffler) to the inverse system of short exact sequences above to see (1). Part (2) is a special case of (1). If the assumptions of (3) hold, then for each $n$ the sequence $$0 \to K/I^nK \to M/I^nM \to N/I^nN \to 0$$ is short exact by Lemma [Tor vanishing for a flat module](#native-algebra-lemma-flat-tor-zero). Hence we can directly apply Lemma [Commutative algebra (programme binding)](#uncovered-algebra-lemma-mittag-leffler) to conclude (3) is true. To see (4) choose generators $x_i \in M$, $i = 1, \ldots, n$. Then the map $R^{\oplus n} \to M$, $(a_1, \ldots, a_n) \mapsto \sum a_ix_i$ is surjective. Hence by (2) we see $(R^\wedge)^{\oplus n} \to M^\wedge$, $(a_1, \ldots, a_n) \mapsto \sum a_ix_i$ is surjective. Assertion (4) follows from this. $\square$

#### Lemma. Complete rings, formal power series and modules
 Let $R$ be a ring. Let $I$ be an ideal of $R$. Let $M$ be an $R$-module. If (a) $R$ is $I$-adically complete, (b) $M$ is a finite $R$-module, and (c) $\bigcap I^nM = (0)$, then $M$ is $I$-adically complete.

**Proof.** By Lemma [Complete rings and formal power series](#native-algebra-lemma-completion-generalities) the map $M = M \otimes_R R = M \otimes_R R^\wedge \to M^\wedge$ is surjective. The kernel of this map is $\bigcap I^nM$ hence zero by assumption. Hence $M \cong M^\wedge$ and $M$ is complete. $\square$

#### Lemma. Commutative algebra

Suppose that $R \to S$ is a ring map with the going up property, see Definition [Commutative algebra](#context-algebra-definition-going-up-down). If $\mathfrak q \subset S$ is a maximal ideal, then the inverse image of $\mathfrak q$ in $R$ is a maximal ideal too.

**Proof.** Trivial. $\square$

#### Lemma. Descent of commutative algebra
 Let $R \to S$ be a ring map. Assume that

1.  $R \to S$ is faithfully flat, and

2.  $S$ is reduced.

Then $R$ is reduced.

**Proof.** This is clear as $R \to S$ is injective, by Lemma [Universal injectivity of a faithfully flat ring map](#native-algebra-lemma-faithfully-flat-universally-injective). $\square$

#### Lemma. Commutative algebra
 Let $\varphi : R \to S$ be a ring map. Assume

1.  $\varphi$ is smooth,

2.  $R$ is reduced.

Then $S$ is reduced.

**Proof.** Observe that $R \to S$ is flat with regular fibres (see the list of results on smooth ring maps in Section [Smooth morphisms](#context-algebra-section-smooth-overview)). In particular, the fibres are reduced. Thus if $R$ is Noetherian, then $S$ is Noetherian and we get the result from Lemma [Noetherian rings (programme binding)](#uncovered-algebra-lemma-reduced-goes-up-noetherian).

In the general case we may find a finitely generated $\mathbf{Z}$-subalgebra $R_0 \subset R$ and a smooth ring map $R_0 \to S_0$ such that $S \cong R \otimes_{R_0} S_0$, see remark (10) in Section [Smooth morphisms](#context-algebra-section-smooth-overview). Now, if $x \in S$ is an element with $x^2 = 0$, then we can enlarge $R_0$ and assume that $x$ comes from an element $x_0 \in S_0$. After enlarging $R_0$ once more we may assume that $x_0^2 = 0$ in $S_0$. However, since the subring $R_0 \subset R$ is reduced, we see that $S_0$ is reduced and hence $x_0 = 0$ as desired. $\square$

#### Lemma. Regular rings

*Source credit:* the original source citation FAC (Chapter III, §5, no. 75, proof of Theorem 3, pp. 269--270)

For the local ring of projective space at a point of a nonsingular subvariety, the cited proof considers the kernel of the quotient onto the local ring of the subvariety. It uses that the kernel has exactly the codimension number of generators and records the successive colon equalities saying that those generators form a regular sequence.

The lemma below gives the intrinsic regular-local-ring mechanism used there. It chooses the generators as part of a minimal system of parameters; Lemma [Regular rings are Cohen–Macaulay](#native-algebra-lemma-regular-ring-cm) then makes every initial segment a regular sequence. Thus the colon equalities in the source are the nonzerodivisor conditions for this sequence.

Let $R$ be a regular local ring. Let $I \subset R$ be an ideal such that $R/I$ is a regular local ring as well. Then there exists a minimal set of generators $x_1, \ldots, x_d$ for the maximal ideal $\mathfrak m$ of $R$ such that $I = (x_1, \ldots, x_c)$ for some $0 \leq c \leq d$.

**Proof.** Say \(\dim(R) = d\) and \(\dim(R/I) = d - c\). Denote by \(\overline{\mathfrak m} = \mathfrak m/I\) the maximal ideal of \(R/I\). Let \(\kappa = R/\mathfrak m\). We have 

\[
\dim_\kappa((I + \mathfrak m^2)/\mathfrak m^2) =
\dim_\kappa(\mathfrak m/\mathfrak m^2)
- \dim_\kappa(\overline{\mathfrak m}/\overline{\mathfrak m}^2) = d - (d - c) = c
\]

 by the definition of a regular local ring. Hence we can choose \(x_1, \ldots, x_c \in I\) whose images in \(\mathfrak m/\mathfrak m^2\) are linearly independent and supplement with \(x_{c + 1}, \ldots, x_d\) to get a minimal system of generators of \(\mathfrak m\). The induced map \(R/(x_1, \ldots, x_c) \to R/I\) is a surjection between regular local rings of the same dimension (Lemma [Regular rings are Cohen–Macaulay](#native-algebra-lemma-regular-ring-cm)). It follows that the kernel is zero, i.e., \(I = (x_1, \ldots, x_c)\). Namely, if not then we would have \(\dim(R/I) < \dim(R/(x_1, \ldots, x_c))\) by Lemmas Regular local rings, Theorem 1.1 and [A single polynomial equation](#native-algebra-lemma-one-equation). \(\square\)

#### Lemma. Injectivity from a fibrewise injectivity criterion

Suppose that $R \to S$ is a local homomorphism of local rings with $S$ Noetherian. Denote by $\mathfrak m$ the maximal ideal of $R$. Let $M$ be a flat $R$-module and $N$ a finite $S$-module. Let $u : N \to M$ be a map of $R$-modules. If $\overline{u} : N/\mathfrak m N \to M/\mathfrak m M$ is injective then $u$ is injective. In this case $M/u(N)$ is flat over $R$.

**Proof.** First we claim that $u_n : N/{\mathfrak m}^nN \to M/{\mathfrak m}^nM$ is injective for all $n \geq 1$. We proceed by induction, the base case is that $\overline{u} = u_1$ is injective. By our assumption that $M$ is flat over $R$ we have a short exact sequence $0 \to M \otimes_R {\mathfrak m}^n/{\mathfrak m}^{n + 1}
\to M/{\mathfrak m}^{n + 1}M \to M/{\mathfrak m}^n M \to 0$. Also, $M \otimes_R {\mathfrak m}^n/{\mathfrak m}^{n + 1}
= M/{\mathfrak m}M \otimes_{R/{\mathfrak m}}
{\mathfrak m}^n/{\mathfrak m}^{n + 1}$. We have a similar exact sequence $N \otimes_R {\mathfrak m}^n/{\mathfrak m}^{n + 1}
\to N/{\mathfrak m}^{n + 1}N \to N/{\mathfrak m}^n N \to 0$ for $N$ except we do not have the zero on the left. We also have $N \otimes_R {\mathfrak m}^n/{\mathfrak m}^{n + 1}
= N/{\mathfrak m}N \otimes_{R/{\mathfrak m}}
{\mathfrak m}^n/{\mathfrak m}^{n + 1}$. Thus the map $u_{n + 1}$ is injective as both $u_n$ and the map $\overline{u} \otimes \text{id}_{{\mathfrak m}^n/{\mathfrak m}^{n + 1}}$ are.

By Krull's intersection theorem (Lemma [Krull's intersection theorem](#native-algebra-lemma-intersect-powers-ideal-module-zero)) applied to $N$ over the ring $S$ and the ideal $\mathfrak mS$ we have $\bigcap \mathfrak m^nN = 0$. Thus the injectivity of $u_n$ for all $n$ implies $u$ is injective.

To show that $M/u(N)$ is flat over $R$, it suffices to show that $\text{Tor}_1^R(M/u(N), R/I) = 0$ for every ideal $I \subset R$, see Lemma [Criteria for flatness](#native-algebra-lemma-characterize-flat). From the short exact sequence $$0 \to N \xrightarrow{u} M \to M/u(N) \to 0$$ and the flatness of $M$ we obtain an exact sequence of Tors $$0 \to \text{Tor}_1^R(M/u(N), R/I) \to N/IN \to M/IM$$ See Lemma [Derived tensor products and Tor amplitude (programme binding)](#uncovered-algebra-lemma-long-exact-sequence-tor). Thus it suffices to show that $N/IN$ injects into $M/IM$. Note that $R/I \to S/IS$ is a local homomorphism of local rings with $S/IS$ Noetherian, $N/IN \to M/IM$ is a map of $R/I$-modules, $N/IN$ is finite over $S/IS$, and $M/IM$ is flat over $R/I$ and $u \bmod I : N/IN \to M/IM$ is injective modulo $\mathfrak m$. Thus we may apply the first part of the proof to $u \bmod I$ and we conclude. $\square$

#### Lemma. The universal property of Kähler differentials

Maps out of the module of differentials are the same as derivations.

The module of differentials of $S$ over $R$ has the following universal property. The map $$\operatorname{Hom}_S(\Omega_{S/R}, M)
\longrightarrow
\text{Der}_R(S, M), \quad
\alpha
\longmapsto
\alpha \circ \text{d}$$ is an isomorphism of functors.

**Proof.** By definition an $R$-derivation is a rule which associates to each $a \in S$ an element $D(a) \in M$. Thus $D$ gives rise to a map $[D] : \bigoplus S[a] \to M$. However, the conditions of being an $R$-derivation exactly mean that $[D]$ annihilates the image of the map in the displayed presentation of $\Omega_{S/R}$ above. $\square$

#### Lemma. Complete rings, formal power series and Noetherian rings
 Let $I$ be an ideal of a ring $R$. Assume

1.  $R/I$ is a Noetherian ring,

2.  $I$ is finitely generated.

Then the completion $R^\wedge$ of $R$ with respect to $I$ is a Noetherian ring complete with respect to $IR^\wedge$.

**Proof.** By Lemma [Finite algebras](#native-algebra-lemma-hathat-finitely-generated) we see that $R^\wedge$ is $I$-adically complete. Hence it is also $IR^\wedge$-adically complete. Since $R^\wedge/IR^\wedge = R/I$ is Noetherian we see that after replacing $R$ by $R^\wedge$ we may in addition to assumptions (1) and (2) assume that also $R$ is $I$-adically complete.

Let $f_1, \ldots, f_t$ be generators of $I$. Then there is a surjection of rings $R/I[T_1, \ldots, T_t] \to \bigoplus I^n/I^{n + 1}$ mapping $T_i$ to the element $\overline{f}_i \in I/I^2$. Hence $\bigoplus I^n/I^{n + 1}$ is a Noetherian ring. Let $J \subset R$ be an ideal. Consider the ideal $$\bigoplus J \cap I^n/J \cap I^{n + 1} \subset \bigoplus I^n/I^{n + 1}.$$ Let $\overline{g}_1, \ldots, \overline{g}_m$ be generators of this ideal. We may choose $\overline{g}_j$ to be a homogeneous element of degree $d_j$ and we may pick $g_j \in J \cap I^{d_j}$ mapping to $\overline{g}_j \in J \cap I^{d_j}/J \cap I^{d_j + 1}$. We claim that $g_1, \ldots, g_m$ generate $J$.

Let $x \in J \cap I^n$. There exist $a_j \in I^{\max(0, n - d_j)}$ such that $x - \sum a_j g_j \in J \cap I^{n + 1}$. The reason is that $J \cap I^n/J \cap I^{n + 1}$ is equal to $\sum_{j:\,d_j \leq n} \overline{g}_j I^{n - d_j}/I^{n - d_j + 1}$ by our choice of $g_1, \ldots, g_m$. Hence starting with $x \in J$ we can find a sequence of vectors $(a_{1, n}, \ldots, a_{m, n})_{n \geq 0}$ with $a_{j, n} \in I^{\max(0, n - d_j)}$ such that $$x =
\sum\nolimits_{n = 0, \ldots, N}
\sum\nolimits_{j = 1, \ldots, m} a_{j, n} g_j \bmod I^{N + 1}$$ Setting $A_j = \sum_{n \geq 0} a_{j, n}$ we see that $x = \sum A_j g_j$ as $R$ is complete. Hence $J$ is finitely generated and we win. $\square$

#### Lemma. Flatness and modules
 Let $R \to S$ be a ring map. Let $I \subset R$ be an ideal. Let $M$ be an $S$-module. Assume

1.  $R$ is a Noetherian ring,

2.  $S$ is a Noetherian ring,

3.  $M$ is a finite $S$-module, and

4.  for each $n \geq 1$ the module $M/I^n M$ is flat over $R/I^n$.

Then for every $\mathfrak q \in V(IS)$ the localization $M_{\mathfrak q}$ is flat over $R$. In particular, if $S$ is local and $IS$ is contained in its maximal ideal, then $M$ is flat over $R$.

**Proof.** We are going to use Lemma [A variant of the local criterion for flatness](#native-algebra-lemma-variant-local-criterion-flatness). By assumption $M/IM$ is flat over $R/I$. Hence it suffices to check that $\text{Tor}_1^R(M, R/I)$ is zero on localization at $\mathfrak q$. By Remark [Tor for a quotient by an ideal](#native-algebra-remark-tor-ring-mod-ideal) this Tor group is equal to $K = \operatorname{Ker}(I \otimes_R M \to M)$. We know that the kernel of $I/I^n \otimes_{R/I^n} M/I^nM \to M/I^nM$ is zero for all $n \geq 1$. Hence an element of $K$ maps to zero in $I/I^n \otimes_{R/I^n} M/I^nM$. Since $$I/I^n \otimes_{R/I^n} M/I^nM = I/I^n \otimes_R M =
(I \otimes_R M)/I^{n - 1}(I \otimes_R M)$$ we conclude that $K \subset I^{n - 1}(I \otimes_R M)$ for all $n \geq 1$. By the Artin-Rees lemma, and more precisely Lemma [Modules (programme binding)](#uncovered-algebra-lemma-intersection-powers-ideal-module) we conclude that $K_{\mathfrak q} = 0$, as desired. $\square$

#### Lemma. Commutative algebra

Let $(A_i, \varphi_{ji})$ be a directed inverse system over $I$. Suppose $I$ is countable. If $(A_i, \varphi_{ji})$ is Mittag-Leffler and the $A_i$ are nonempty, then $\varprojlim A_i$ is nonempty.

**Proof.** Let $i_1, i_2, i_3, \ldots$ be an enumeration of the elements of $I$. Define inductively a sequence of elements $j_n \in I$ for $n = 1, 2, 3, \ldots$ by the conditions: $j_1 = i_1$, and $j_n \geq i_n$ and $j_n \geq j_m$ for $m < n$. Then the sequence $j_n$ is increasing and forms a cofinal subset of $I$. Hence we may assume $I =\{1, 2, 3, \ldots \}$. So by Example [Commutative algebra (programme binding)](#uncovered-algebra-example-ml-surjective-maps) we are reduced to showing that the limit of an inverse system of nonempty sets with surjective maps indexed by the positive integers is nonempty. This follows from the axiom of choice. $\square$

[^1]: To avoid set theoretical difficulties we consider only $A' \to A$ such that $A'$ is a quotient of $R[x_1, x_2, x_3, \ldots]$.

[^2]: Here is the argument in more detail: Assume that we know that the second and fourth arrows are injective. Lemma [Tensor products and direct sums](#native-algebra-lemma-tensor-product-exact) (applied to the exact sequence $K \to N_2 \to Q \to 0$) yields that the sequence $K \otimes_R M \to N_2 \otimes_R M \to
    Q \otimes_R M \to 0$ is exact. Hence, $\operatorname{Ker} \left(N_2 \otimes_R M \to Q \otimes_R M\right)
    = \operatorname{Im} \left(K \otimes_R M \to N_2 \otimes_R M\right)$. Since $\operatorname{Im} \left(K \otimes_R M \to N_2 \otimes_R M\right)
    = \operatorname{Im} \left(N_1 \otimes_R M \to N_2 \otimes_R M\right)$ (due to the surjectivity of $N_1 \otimes_R M \to
    K \otimes_R M$) and $\operatorname{Ker} \left(N_2 \otimes_R M \to Q \otimes_R M\right)
    = \operatorname{Ker} \left(N_2 \otimes_R M \to N_3 \otimes_R M\right)$ (due to the injectivity of $Q \otimes_R M \to
    N_3 \otimes_R M$), this becomes $\operatorname{Ker} \left(N_2 \otimes_R M \to N_3 \otimes_R M\right)
    = \operatorname{Im} \left(N_1 \otimes_R M \to N_2 \otimes_R M\right)$, which shows that the functor $- \otimes_R M$ is exact, whence $M$ is flat.

[^3]: This becomes obvious if we identify $L' \otimes_R M$ and $L \otimes_R M$ with submodules of $M^{\oplus n}$ (which is legitimate since the maps $L \otimes_R M \to M^{\oplus n}$ and $L' \otimes_R M \to M^{\oplus n}$ are injective and commute with the obvious map $L' \otimes_R M \to L \otimes_R M$).

[^4]: Special cases: (I) $I = 0$. The lemma says if $x_1, \ldots, x_r$ generate $S^{-1}M$, then $x_1, \ldots, x_r$ generate $M_f$ for some $f \in S$. (II) $I = \mathfrak p$ is a prime ideal and $S = R \setminus \mathfrak p$. The lemma says if $x_1, \ldots, x_r$ generate $M \otimes_R \kappa(\mathfrak p)$ then $x_1, \ldots, x_r$ generate $M_f$ for some $f \in R$, $f \not \in \mathfrak p$.

#### Infinitesimal lifting and complete rings

#### Definition. Local complete-intersection ring maps
 A ring map $A \to B$ is called a *local complete intersection* if it is of finite type and for some (equivalently any) presentation $B = A[x_1, \ldots, x_n]/I$ the ideal $I$ is Koszul-regular.

#### Lemma. Noetherianity of a henselization

*Source credit:* the original source citation EGA (IV, Theorem 18.6.6 and Proposition 18.8.8)

Let $R$ be a local ring. The following are equivalent

1.  $R$ is Noetherian,

2.  $R^h$ is Noetherian, and

3.  $R^{sh}$ is Noetherian.

In this case we have

1.  $(R^h)^\wedge$ and $(R^{sh})^\wedge$ are Noetherian complete local rings,

2.  $R^\wedge \to (R^h)^\wedge$ is an isomorphism,

3.  $R^h \to (R^h)^\wedge$ and $R^{sh} \to (R^{sh})^\wedge$ are flat,

4.  $R^\wedge \to (R^{sh})^\wedge$ is formally smooth in the $\mathfrak m_{(R^{sh})^\wedge}$-adic topology,

5.  $(R^\wedge)^{sh} = R^\wedge \otimes_{R^h} R^{sh}$, and

6.  $((R^\wedge)^{sh})^\wedge = (R^{sh})^\wedge$.

**Proof.** Since $R \to R^h \to R^{sh}$ are faithfully flat (Lemma Henselian local rings and henselization, Sections 4 and 6, Proposition 6.1), we see that $R^h$ or $R^{sh}$ being Noetherian implies that $R$ is Noetherian, see Algebra, Lemma [Descent of Noetherianity](#native-algebra-lemma-descent-noetherian). In the rest of the proof we assume $R$ is Noetherian.

As $\mathfrak m \subset R$ is finitely generated it follows that $\mathfrak m^h = \mathfrak m R^h$ and $\mathfrak m^{sh} = \mathfrak mR^{sh}$ are finitely generated, see Lemma Henselian local rings and henselization, Sections 4 and 6, Proposition 6.1. Hence $(R^h)^\wedge$ and $(R^{sh})^\wedge$ are Noetherian by Algebra, Lemma Coefficient rings and the Cohen structure theorem, Theorem 6.1 and its Noetherianity consequence. This proves (a).

Note that (b) is immediate from Lemma Henselian local rings and henselization, Sections 4 and 6, Proposition 6.1. In particular we see that $(R^h)^\wedge$ is flat over $R$, see Algebra, Lemma Completion, Theorems 3.1–3.3, 4.1 and 5.1.

Next, we show that $R^h \to (R^h)^\wedge$ is flat. Write $R^h = \mathop{\operatorname{colim}}_i R_i$ as a directed colimit of localizations of étale $R$-algebras. By Algebra, Lemma [Flatness in a filtered ring colimit](#native-algebra-lemma-colimit-rings-flat) if $(R^h)^\wedge$ is flat over each $R_i$, then $R^h \to (R^h)^\wedge$ is flat. Note that $R^h = R_i^h$ (by construction). Hence $R_i^\wedge = (R^h)^\wedge$ by part (b) is flat over $R_i$ as desired. To finish the proof of (c) we show that $R^{sh} \to (R^{sh})^\wedge$ is flat. To do this, by a limit argument as above, it suffices to show that $(R^{sh})^\wedge$ is flat over $R$. Note that it follows from Lemma Henselian local rings and henselization, Sections 4 and 6, Proposition 6.1 that $(R^{sh})^\wedge$ is the completion of a free $R$-module. By Lemma [Flatness of a completed direct sum](#native-more-algebra-lemma-completed-direct-sum-flat) we see this is flat over $R$ as desired. This finishes the proof of (c).

At this point we know (c) is true and that $(R^h)^\wedge$ and $(R^{sh})^\wedge$ are Noetherian. It follows from Algebra, Lemma [Descent of Noetherianity](#native-algebra-lemma-descent-noetherian) that $R^h$ and $R^{sh}$ are Noetherian.

Part (d) follows from Lemma [Formal smoothness of henselization](#native-more-algebra-lemma-henselization-formally-smooth) and Lemma [Formal smoothness and completion](#native-more-algebra-lemma-formally-smooth-completion).

Part (e) follows from Algebra, Lemma [A strict henselization map extending a henselization map](#native-algebra-lemma-sh-from-h-map) and the fact that $R^\wedge$ is henselian by Algebra, Lemma Completion, Theorems 3.1–3.3, 4.1 and 5.1.

Proof of (f). Using (e) there is a map $R^{sh} \to (R^\wedge)^{sh}$ which induces a map $(R^{sh})^\wedge \to ((R^\wedge)^{sh})^\wedge$ upon completion. Using (e) there is a map $R^\wedge \to (R^{sh})^\wedge$. Since $(R^{sh})^\wedge$ is strictly henselian (see above) this map induces a map $(R^\wedge)^{sh} \to (R^{sh})^\wedge$ by Algebra, Lemma [Functoriality of strict henselization](#native-algebra-lemma-strictly-henselian-functorial). Completing we obtain a map $((R^\wedge)^{sh})^\wedge \to (R^{sh})^\wedge$. We omit the verification that these two maps are mutually inverse. $\square$

#### Lemma. Lifting a unit
 Let $A$ be a ring, let $I \subset A$ be an ideal, let $\overline{u} \in A/I$ be an invertible element. There exists an étale ring map $A \to A'$ which induces an isomorphism $A/I \to A'/IA'$ and an invertible element $u' \in A'$ lifting $\overline{u}$.

**Proof.** Choose any lift $f \in A$ of $\overline{u}$ and set $A' = A_f$ and $u$ the image of $f$ in $A'$. $\square$

#### Lemma. First cotangent homology after a regular quotient
 Let $A$ be a ring. Let $I \subset A$ be an ideal. Let $g_1, \ldots, g_m$ be a sequence in $A$ whose image in $A/I$ is $H_1$-regular. Then $I \cap (g_1, \ldots, g_m) =
I(g_1, \ldots, g_m)$.

**Proof.** Consider the exact sequence of complexes $$0 \to I \otimes_A K_\bullet(A, g_1, \ldots, g_m)
\to K_\bullet(A, g_1, \ldots, g_m) \to
K_\bullet(A/I, g_1, \ldots, g_m) \to 0$$ Since the complex on the right has $H_1 = 0$ by assumption we see that $$\operatorname{Coker}(I^{\oplus m} \to I)
\longrightarrow
\operatorname{Coker}(A^{\oplus m} \to A)$$ is injective. This is equivalent to the assertion of the lemma. $\square$

#### Lemma. Locality of the complete-intersection condition
 Let $R \to S$ be a ring map. Let $g_1, \ldots, g_m \in S$ generate the unit ideal. If each $R \to S_{g_j}$ is a local complete intersection so is $R \to S$.

**Proof.** Let $S = R[x_1, \ldots, x_n]/I$ be a presentation. Pick $h_j \in R[x_1, \ldots, x_n]$ mapping to $g_j$ in $S$. Then $R[x_1, \ldots, x_n, x_{n + 1}]/(I, x_{n + 1}h_j - 1)$ is a presentation of $S_{g_j}$. Hence $I_j = (I, x_{n + 1}h_j - 1)$ is a Koszul-regular ideal in $R[x_1, \ldots, x_n, x_{n + 1}]$. Pick a prime $I \subset \mathfrak q \subset R[x_1, \ldots, x_n]$. Then $h_j \not \in \mathfrak q$ for some $j$ and $\mathfrak q_j = (\mathfrak q, x_{n + 1}h_j - 1)$ is a prime ideal of $V(I_j)$ lying over $\mathfrak q$. Pick $f_1, \ldots, f_r \in I$ which map to a basis of $I/I^2 \otimes \kappa(\mathfrak q)$. Then $x_{n + 1}h_j - 1, f_1, \ldots, f_r$ is a sequence of elements of $I_j$ which map to a basis of $I_j \otimes \kappa(\mathfrak q_j)$, see Algebra, Lemma [The cotangent complex of a principal localization](#native-algebra-lemma-principal-localization-nl). By Nakayama's lemma there exists an $h \in R[x_1, \ldots, x_n, x_{n + 1}]$ such that $(I_j)_h$ is generated by $x_{n + 1}h_j - 1, f_1, \ldots, f_r$. We may also assume that $(I_j)_h$ is generated by a Koszul regular sequence of some length $e$. Looking at the dimension of $I_j \otimes \kappa(\mathfrak q_j)$ we see that $e = r + 1$. Hence by Lemma [Independence of a chosen set of ideal generators](#native-more-algebra-lemma-independence-of-generators) we see that $x_{n + 1}h_j - 1, f_1, \ldots, f_r$ is a Koszul-regular sequence generating $(I_j)_h$ for some $h \in R[x_1, \ldots, x_n, x_{n + 1}]$, $h \not \in \mathfrak q_j$. By Lemma [Truncation of a Koszul-regular sequence](#native-more-algebra-lemma-truncate-koszul-regular) we see that $I_{h'}$ is generated by a Koszul-regular sequence for some $h' \in R[x_1, \ldots, x_n]$, $h' \not \in \mathfrak q$ as desired. $\square$

#### Lemma. Koszul complexes of global complete intersections
 Let $R$ be a ring. If $R[x_1, \ldots, x_n]/(f_1, \ldots, f_c)$ is a relative global complete intersection, then $f_1, \ldots, f_c$ is a Koszul regular sequence.

**Proof.** Recall that the homology groups $H_i(K_\bullet(f_\bullet))$ are annihilated by the ideal $(f_1, \ldots, f_c)$. Hence it suffices to show that $H_i(K_\bullet(f_\bullet))_\mathfrak q$ is zero for all primes $\mathfrak q \subset R[x_1, \ldots, x_n]$ containing $(f_1, \ldots, f_c)$. This follows from Algebra, Lemma [The conormal module of a global complete intersection](#native-algebra-lemma-relative-global-complete-intersection-conormal) and the fact that a regular sequence is Koszul regular (Lemma [Regular sequences are Koszul-regular](#native-more-algebra-lemma-regular-koszul-regular)). $\square$

#### Definition. Regular ideals
 Let $R$ be a ring and let $I \subset R$ be an ideal.

1.  We say $I$ is a *regular ideal* if for every $\mathfrak p \in V(I)$ there exists a $g \in R$, $g \not \in \mathfrak p$ and a regular sequence $f_1, \ldots, f_r \in R_g$ such that $I_g$ is generated by $f_1, \ldots, f_r$.

2.  We say $I$ is a *Koszul-regular ideal* if for every $\mathfrak p \in V(I)$ there exists a $g \in R$, $g \not \in \mathfrak p$ and a Koszul-regular sequence $f_1, \ldots, f_r \in R_g$ such that $I_g$ is generated by $f_1, \ldots, f_r$.

3.  We say $I$ is a *$H_1$-regular ideal* if for every $\mathfrak p \in V(I)$ there exists a $g \in R$, $g \not \in \mathfrak p$ and an $H_1$-regular sequence $f_1, \ldots, f_r \in R_g$ such that $I_g$ is generated by $f_1, \ldots, f_r$.

4.  We say $I$ is a *quasi-regular ideal* if for every $\mathfrak p \in V(I)$ there exists a $g \in R$, $g \not \in \mathfrak p$ and a quasi-regular sequence $f_1, \ldots, f_r \in R_g$ such that $I_g$ is generated by $f_1, \ldots, f_r$.

#### Lemma. Relative regular immersions in affine algebra
 Let $A \to B$ and $A \to A'$ be ring maps. Set $B' = B \otimes_A A'$. Let $f_1, \ldots, f_r \in B$. Assume $B/(f_1, \ldots, f_r)B$ is flat over $A$

1.  If $f_1, \ldots, f_r$ is a quasi-regular sequence, then the image in $B'$ is a quasi-regular sequence.

2.  If $f_1, \ldots, f_r$ is a $H_1$-regular sequence, then the image in $B'$ is a $H_1$-regular sequence.

**Proof.** Assume $f_1, \ldots, f_r$ is quasi-regular. Set $J = (f_1, \ldots, f_r)$. By assumption $J^n/J^{n + 1}$ is isomorphic to a direct sum of copies of $B/J$ hence flat over $A$. By induction and Algebra, Lemma [Flat modules in a short exact sequence](#native-algebra-lemma-flat-ses) we conclude that $B/J^n$ is flat over $A$. The ideal $(J')^n$ is equal to $J^n \otimes_A A'$, see Algebra, Lemma [Tor vanishing for a flat module](#native-algebra-lemma-flat-tor-zero). Hence $(J')^n/(J')^{n + 1} = J^n/J^{n + 1} \otimes_A A'$ which clearly implies that $f_1, \ldots, f_r$ is a quasi-regular sequence in $B'$.

Assume $f_1, \ldots, f_r$ is $H_1$-regular. By Lemma [Base change of first-homology regularity](#native-more-algebra-lemma-base-change-h1-regular) the vanishing of the Koszul homology group $H_1(K_\bullet(B, f_1, \ldots, f_r))$ implies the vanishing of $H_1(K_\bullet(B', f'_1, \ldots, f'_r))$ and we win. $\square$

#### Lemma. Regularity conditions for finite ideals in Noetherian rings

Let $(R, \mathfrak m)$ be a Noetherian local ring. Let $M$ be a nonzero finite $R$-module. Let $f_1, \ldots, f_r \in \mathfrak m$. The following are equivalent

1.  $f_1, \ldots, f_r$ is an $M$-regular sequence,

2.  $f_1, \ldots, f_r$ is a $M$-Koszul-regular sequence,

3.  $f_1, \ldots, f_r$ is an $M$-$H_1$-regular sequence,

4.  $f_1, \ldots, f_r$ is an $M$-quasi-regular sequence.

In particular the sequence $f_1, \ldots, f_r$ is a regular sequence in $R$ if and only if it is a Koszul regular sequence, if and only if it is a $H_1$-regular sequence, if and only if it is a quasi-regular sequence.

**Proof.** The implication (1) $\Rightarrow$ (2) is Lemma [Regular sequences are Koszul-regular](#native-more-algebra-lemma-regular-koszul-regular). The implication (2) $\Rightarrow$ (3) is Lemma [Koszul regularity implies first-homology regularity](#native-more-algebra-lemma-koszul-regular-h1-regular). The implication (3) $\Rightarrow$ (4) is Lemma [First-homology regularity implies quasi-regularity](#native-more-algebra-lemma-h1-regular-quasi-regular). The implication (4) $\Rightarrow$ (1) is Algebra, Lemma [Quasi-regular and regular ideals in a Noetherian ring](#native-algebra-lemma-quasi-regular-regular). $\square$

#### Lemma. Regularity and completion

Let $A$ be a Noetherian local ring. Then $A$ is regular if and only if $A^\wedge$ is so.

**Proof.** If $A^\wedge$ is regular, then $A$ is regular by Algebra, Lemma [Flatness and regular ring maps](#native-algebra-lemma-flat-under-regular). Assume $A$ is regular. Let $\mathfrak m$ be the maximal ideal of $A$. Then $\dim_{\kappa(\mathfrak m)} \mathfrak m/\mathfrak m^2 =
\dim(A) = \dim(A^\wedge)$ (Lemma [Dimension of a completion](#native-more-algebra-lemma-completion-dimension)). On the other hand, $\mathfrak mA^\wedge$ is the maximal ideal of $A^\wedge$ and hence $\mathfrak m_{A^\wedge}$ is generated by at most $\dim(A^\wedge)$ elements. Thus $A^\wedge$ is regular. (You can also use Algebra, Lemma [Regularity over a regular base with regular fibre](#native-algebra-lemma-flat-over-regular-with-regular-fibre).) $\square$

#### Lemma. Derivations of formal power series in positive characteristic
 Let $p$ be a prime number. Let $B$ be a domain with $p = 0$ in $B$. Let $f \in B$ be an element which is not a $p$th power in the fraction field of $B$. If $B$ is of finite type over a Noetherian complete local ring, then there exists a derivation $D : B \to B$ such that $D(f)$ is not zero.

**Proof.** Let $R$ be a Noetherian complete local ring such that there exists a finite type ring map $R \to B$. Of course we may replace $R$ by its image in $B$, hence we may assume $R$ is a domain of characteristic $p > 0$ (as well as Noetherian complete local). By Algebra, Lemma [A complete local domain finite over a regular ring](#native-algebra-lemma-complete-local-noetherian-domain-finite-over-regular) we can write $R$ as a finite extension of $k[[x_1, \ldots, x_n]]$ for some field $k$ and integer $n$. Hence we may replace $R$ by $k[[x_1, \ldots, x_n]]$. Next, we use Algebra, Lemma [Noether normalization over a domain](#native-algebra-lemma-noether-normalization-over-a-domain) to factor $R \to B$ as $$R \subset R[y_1, \ldots, y_d] \subset B' \subset B$$ with $B'$ finite over $R[y_1, \ldots, y_d]$ and $B'_g \cong B_g$ for some nonzero $g \in R$. Note that $f' = g^{pN} f \in B'$ for some large integer $N$. It is clear that $f'$ is not a $p$th power in the fraction field of $B'$. If we can find a derivation $D' : B' \to B'$ with $D'(f') \not = 0$, then Lemma [Extending a derivation](#native-more-algebra-lemma-derivation-extends) guarantees that $D = g^MD'$ extends to $B$ for some $M > 0$. Then $D(f) = g^MD'(f) = g^MD'(g^{-pN}f') = g^{M - pN}D'(f')$ is nonzero. Thus it suffices to prove the lemma in case $B$ is a finite extension of $A = k[[x_1, \ldots, x_n]][y_1, \ldots, y_m]$.

Assume $B$ is a finite extension of $A = k[[x_1, \ldots, x_n]][y_1, \ldots, y_m]$. Denote $L$ the fraction field of $B$. Note that $\text{d}f$ is not zero in $\Omega_{L/\mathbf{F}_p}$, see Algebra, Lemma [Polynomials with zero derivative in characteristic p](#native-algebra-lemma-derivative-zero-pth-power). We apply Lemma [Subfields of a formal power-series ring](#native-more-algebra-lemma-power-series-ring-subfields) to find a subfield $k' \subset k$ of finite index such that with $A' = k'[[x_1^p, \ldots, x_n^p]][y_1^p, \ldots, y_m^p]$ the element $\text{d}f$ does not map to zero in $\Omega_{L/K'}$ where $K'$ is the fraction field of $A'$. Thus we can choose a $K'$-derivation $D' : L \to L$ with $D'(f) \not = 0$. Since $A' \subset A$ and $A \subset B$ are finite by construction we see that $A' \subset B$ is finite. Choose $b_1, \ldots, b_t \in B$ which generate $B$ as an $A'$-module. Then $D'(b_i) = f_i/g_i$ for some $f_i, g_i \in B$ with $g_i \not = 0$. Setting $D = g_1 \ldots g_t D'$ we win. $\square$

#### Lemma. Extending a derivation
 Let $R$ be a ring. Let $D : R \to R$ be a derivation.

1.  For any ideal $I \subset R$ the derivation $D$ extends canonically to a derivation $D^\wedge : R^\wedge \to R^\wedge$ on the $I$-adic completion.

2.  For any multiplicative subset $S \subset R$ the derivation $D$ extends uniquely to the localization $S^{-1}R$ of $R$.

If $R \subset R'$ is a finite type extension of rings such that $R_g \cong R'_g$ for some $g \in R$ which is a nonzerodivisor in $R'$, then $g^ND$ extends to $R'$ for some $N \geq 0$.

**Proof.** Proof of (1). For $n \geq 2$ we have $D(I^n) \subset I^{n - 1}$ by the Leibniz rule. Hence $D$ induces maps $D_n : R/I^n \to R/I^{n - 1}$. Taking the limit we obtain $D^\wedge$. We omit the verification that $D^\wedge$ is a derivation.

Proof of (2). To extend $D$ to $S^{-1}R$ just set $D(r/s) = D(r)/s - rD(s)/s^2$ and check the axioms.

Proof of the final statement. Let $x_1, \ldots, x_n \in R'$ be generators of $R'$ over $R$. Choose an $N$ such that $g^Nx_i \in R$. Consider $g^{N + 1}D$. By (2) this extends to $R_g$. Moreover, by the Leibniz rule and our construction of the extension above we have $$g^{N + 1}D(x_i) = g^{N + 1}D(g^{-N} g^Nx_i) = -Ng^Nx_iD(g) +
gD(g^Nx_i)$$ and both terms are in $R$. This implies that $$g^{N + 1}D(x_1^{e_1} \ldots x_n^{e_n}) =
\sum e_i x_1^{e_1} \ldots x_i^{e_i - 1} \ldots x_n^{e_n} g^{N + 1}D(x_i)$$ is an element of $R'$. Hence every element of $R'$ (which can be written as a sum of monomials in the $x_i$ with coefficients in $R$) is mapped to an element of $R'$ by $g^{N + 1}D$ and we win. $\square$

#### Lemma. Regularity after an extension of degree p
 Let $R$ be a regular ring. Let $f \in R$. Assume there exists a derivation $D : R \to R$ such that $D(f)$ is a unit of $R$. Then $R[z]/(z^n - f)$ is regular for any integer $n \geq 1$. More generally, $R[z]/(p(z) - f)$ is regular for any $p \in \mathbf{Z}[z]$.

**Proof.** By Algebra, Lemma [Regularity ascends along a regular ring map](#native-algebra-lemma-regular-goes-up) we see that $R[z]$ is a regular ring. Apply Lemma [Regularity of a quotient](#native-more-algebra-lemma-quotient-regular) to the extension of $D$ to $R[z]$ which maps $z$ to zero. This works because $D$ annihilates any polynomial with integer coefficients and sends $f$ to a unit. $\square$

#### Lemma. Fibres of henselization maps

Let $R$ be a Noetherian local ring. Let $\mathfrak p \subset R$ be a prime. Then $$R^h \otimes_R \kappa(\mathfrak p) =
\prod\nolimits_{i = 1, \ldots, t} \kappa(\mathfrak q_i)
\quad\text{resp.}\quad
R^{sh} \otimes_R \kappa(\mathfrak p) =
\prod\nolimits_{i = 1, \ldots, s} \kappa(\mathfrak r_i)$$ where $\mathfrak q_1, \ldots, \mathfrak q_t$, resp. $\mathfrak r_1, \ldots, \mathfrak r_s$ are the prime of $R^h$, resp. $R^{sh}$ lying over $\mathfrak p$. Moreover, the field extensions $\kappa(\mathfrak q_i)/\kappa(\mathfrak p)$ resp. $\kappa(\mathfrak r_i)/\kappa(\mathfrak p)$ are separable algebraic.

**Proof.** This can be deduced from the more general Lemma [Noetherian fibres of a filtered colimit of étale maps](#native-more-algebra-lemma-filtered-colimit-etale-noetherian-fibres) using that the henselization and strict henselization are Noetherian (as we've seen above). But we also give a direct proof as follows.

We will use without further mention the results of Lemmas Henselian local rings and henselization, Sections 4 and 6, Proposition 6.1 and [Noetherianity of a henselization](#native-more-algebra-lemma-henselization-noetherian). Note that $R^h/\mathfrak pR^h$, resp. $R^{sh}/\mathfrak pR^{sh}$ is the henselization, resp. strict henselization of $R/\mathfrak p$, see Algebra, Lemma Henselian local rings and henselization, Sections 4 and 6, Proposition 6.1 resp. Algebra, Lemma Henselian local rings and henselization, Sections 4 and 6, Proposition 6.1. Hence we may replace $R$ by $R/\mathfrak p$ and assume that $R$ is a Noetherian local domain and that $\mathfrak p = (0)$. Since $R^h$, resp. $R^{sh}$ is Noetherian, it has finitely many minimal primes $\mathfrak q_1, \ldots, \mathfrak q_t$, resp. $\mathfrak r_1, \ldots, \mathfrak r_s$. Since $R \to R^h$, resp. $R \to R^{sh}$ is flat these are exactly the primes lying over $\mathfrak p = (0)$ (by going down). Finally, as $R$ is a domain, we see that $R^h$, resp. $R^{sh}$ is reduced, see Lemma [Reducedness of a henselization](#native-more-algebra-lemma-henselization-reduced). Thus we see that $R^h \otimes_R \kappa(\mathfrak p)$ resp. $R^{sh} \otimes_R \kappa(\mathfrak p)$ is a reduced Noetherian ring with finitely many primes, all of which are minimal (and hence maximal). Thus these rings are Artinian and are products of their localizations at maximal ideals, each necessarily a field (see Algebra, Proposition [Rings of dimension zero](#native-algebra-proposition-dimension-zero-ring) and Algebra, Lemma [Localizations at minimal primes of a reduced ring](#native-algebra-lemma-minimal-prime-reduced-ring)).

The final statement follows from the fact that $R \to R^h$, resp. $R \to R^{sh}$ is a colimit of étale ring maps and hence the induced residue field extensions are colimits of finite separable extensions, see Algebra, Lemma [Étaleness at a prime ideal](#native-algebra-lemma-etale-at-prime). $\square$

#### Proposition. Formal smoothness and regularity
 Let $A \to B$ be a local homomorphism of Noetherian complete local rings. Let $k$ be the residue field of $A$ and $\overline{B} = B \otimes_A k$ the special fibre. The following are equivalent

1.  $A \to B$ is regular,

2.  $A \to B$ is flat and $\overline{B}$ is geometrically regular over $k$,

3.  $A \to B$ is flat and $k \to \overline{B}$ is formally smooth in the $\mathfrak m_{\overline{B}}$-adic topology, and

4.  $A \to B$ is formally smooth in the $\mathfrak m_B$-adic topology.

**Proof.** We have seen the equivalence of (2), (3), and (4) in Proposition [Formal smoothness from flatness and formally smooth fibres](#native-more-algebra-proposition-fs-flat-fibre-fs). It is clear that (1) implies (2). Thus we assume the equivalent conditions (2), (3), and (4) hold and we prove (1).

Let $\mathfrak p$ be a prime of $A$. We will show that $B \otimes_A \kappa(\mathfrak p)$ is geometrically regular over $\kappa(\mathfrak p)$. By Lemma [Base change of formal smoothness](#native-more-algebra-lemma-base-change-fs) we may replace $A$ by $A/\mathfrak p$ and $B$ by $B/\mathfrak pB$. Thus we may assume that $A$ is a domain and that $\mathfrak p = (0)$.

Choose $A_0 \subset A$ as in Algebra, Lemma [A complete local domain finite over a regular ring](#native-algebra-lemma-complete-local-noetherian-domain-finite-over-regular). We will use all the properties stated in that lemma without further mention. As $A_0 \to A$ induces an isomorphism on residue fields, and as $B/\mathfrak m_A B$ is geometrically regular over $A/\mathfrak m_A$ we can find a diagram $$\begin{gathered}\begin{matrix}C & B \\ A_0 & A\end{matrix} \\[6pt] \begin{aligned}C & \longrightarrow B \\ A_0 & \longrightarrow A \\ A_0 & \longrightarrow C \\ A & \longrightarrow B\end{aligned}\end{gathered}$$ with $A_0 \to C$ formally smooth in the $\mathfrak m_C$-adic topology such that $B = C \otimes_{A_0} A$, see Remark [The finite-equation meaning of formal smoothness](#native-more-algebra-remark-what-does-it-mean). (Completion in the tensor product is not needed as $A_0 \to A$ is finite, see Algebra, Lemma Completion, Theorems 3.1–3.3, 4.1 and 5.1.) Hence it suffices to show that $C \otimes_{A_0} K_0$ is a geometrically regular algebra over the fraction field $K_0$ of $A_0$.

The upshot of the preceding paragraph is that we may assume that $A = k[[x_1, \ldots, x_n]]$ where $k$ is a field or $A = \Lambda[[x_1, \ldots, x_n]]$ where $\Lambda$ is a Cohen ring. In this case $B$ is a regular ring, see Algebra, Lemma [Regularity over a regular base with regular fibre](#native-algebra-lemma-flat-over-regular-with-regular-fibre). Hence $B \otimes_A K$ is a regular ring too (where $K$ is the fraction field of $A$) and we win if the characteristic of $K$ is zero.

Thus we are left with the case where $A = k[[x_1, \ldots, x_n]]$ and $k$ is a field of characteristic $p > 0$. Let $L/K$ be a finite purely inseparable field extension. We will show by induction on $[L : K]$ that $B \otimes_A L$ is regular. The base case is $L = K$ which we've seen above. Let $K \subset M \subset L$ be a subfield such that $L$ is a degree $p$ extension of $M$ obtained by adjoining a $p$th root of an element $f \in M$. Let $A'$ be a finite $A$-subalgebra of $M$ with fraction field $M$. Clearing denominators, we may and do assume $f \in A'$. Set $A'' = A'[z]/(z^p -f)$ and note that $A' \subset A''$ is finite and that the fraction field of $A''$ is $L$. By induction we know that $B \otimes_A M$ ring is regular. We have $$B \otimes_A L = B \otimes_A M[z]/(z^p - f)$$ By Lemma [Derivations of formal power series in positive characteristic](#native-more-algebra-lemma-find-d) we know there exists a derivation $D : A' \to A'$ such that $D(f) \not = 0$. As $A' \to B \otimes_A A'$ is formally smooth in the $\mathfrak m$-adic topology by Lemma [Descent of formal smoothness](#native-more-algebra-lemma-descent-fs) we can use Lemma [Lifting formal smoothness](#native-more-algebra-lemma-lift-derivation-through-fs) to extend $D$ to a derivation $D' : B \otimes_A A' \to B \otimes_A A'$. Note that $D'(f) = D(f)$ is a unit in $B \otimes_A M$ as $D(f)$ is not zero in $A' \subset M$. Hence $B \otimes_A L$ is regular by Lemma [Regularity after an extension of degree p](#native-more-algebra-lemma-degree-p-extension-regular) and we win. $\square$

#### Lemma. Formal smoothness and smooth morphisms
 Let $\varphi : R \to S$ be a ring map.

1.  If $R \to S$ is formally smooth in the sense of Algebra, Definition [Formally smooth ring maps](#native-algebra-definition-formally-smooth), then $R \to S$ is formally smooth for any linear topology on $R$ and any pre-adic topology on $S$ such that $R \to S$ is continuous.

2.  Let $\mathfrak n \subset S$ and $\mathfrak m \subset R$ ideals such that $\varphi$ is continuous for the $\mathfrak m$-adic topology on $R$ and the $\mathfrak n$-adic topology on $S$. Then the following are equivalent

    1.  $\varphi$ is formally smooth for the $\mathfrak m$-adic topology on $R$ and the $\mathfrak n$-adic topology on $S$, and

    2.  $\varphi$ is formally smooth for the discrete topology on $R$ and the $\mathfrak n$-adic topology on $S$.

**Proof.** Assume $R \to S$ is formally smooth in the sense of Algebra, Definition [Formally smooth ring maps](#native-algebra-definition-formally-smooth). If $S$ has a pre-adic topology, then there exists an ideal $\mathfrak n \subset S$ such that $S$ has the $\mathfrak n$-adic topology. Suppose given a solid commutative diagram as in Definition [Formally smooth ring maps](#native-more-algebra-definition-formally-smooth). Continuity of $S \to A/J$ means that $\mathfrak n^k$ maps to zero in $A/J$ for some $k \geq 1$, see Lemma [Derived commutative algebra](#native-more-algebra-lemma-continuous). We obtain a ring map $\psi : S \to A$ from the assumed formal smoothness of $S$ over $R$. Then $\psi(\mathfrak n^k) \subset J$ hence $\psi(\mathfrak n^{2k}) = 0$ as $J^2 = 0$. Hence $\psi$ is continuous by Lemma [Derived commutative algebra](#native-more-algebra-lemma-continuous). This proves (1).

The proof of (2)(b) $\Rightarrow$ (2)(a) is the same as the proof of (1). Assume (2)(a). Suppose given a solid commutative diagram as in Definition [Formally smooth ring maps](#native-more-algebra-definition-formally-smooth) where we use the discrete topology on $R$. Since $\varphi$ is continuous we see that $\varphi(\mathfrak m^n) \subset \mathfrak n$ for some $n \geq 1$. As $S \to A/J$ is continuous we see that $\mathfrak n^k$ maps to zero in $A/J$ for some $k \geq 1$. Hence $\mathfrak m^{nk}$ maps into $J$ under the map $R \to A$. Thus $\mathfrak m^{2nk}$ maps to zero in $A$ and we see that $R \to A$ is continuous in the $\mathfrak m$-adic topology. Thus (2)(a) gives a dotted arrow as desired. $\square$

#### Lemma. Formal smoothness and completion
 Let $(R, \mathfrak m)$ and $(S, \mathfrak n)$ be rings endowed with finitely generated ideals. Endow $R$ and $S$ with the $\mathfrak m$-adic and $\mathfrak n$-adic topologies. Let $R \to S$ be a homomorphism of topological rings. The following are equivalent

1.  $R \to S$ is formally smooth for the $\mathfrak n$-adic topology,

2.  $R \to S^\wedge$ is formally smooth for the $\mathfrak n^\wedge$-adic topology,

3.  $R^\wedge \to S^\wedge$ is formally smooth for the $\mathfrak n^\wedge$-adic topology.

Here $R^\wedge$ and $S^\wedge$ are the $\mathfrak m$-adic and $\mathfrak n$-adic completions of $R$ and $S$.

**Proof.** The assumption that $\mathfrak m$ is finitely generated implies that $R^\wedge$ is $\mathfrak mR^\wedge$-adically complete, that $\mathfrak mR^\wedge = \mathfrak m^\wedge$ and that $R^\wedge/\mathfrak m^nR^\wedge = R/\mathfrak m^n$, see Algebra, Lemma [Finite algebras](#native-algebra-lemma-hathat-finitely-generated) and its proof. Similarly for $(S, \mathfrak n)$. Thus it is clear that diagrams as in Definition [Formally smooth ring maps](#native-more-algebra-definition-formally-smooth) for the cases (1), (2), and (3) are in 1-to-1 correspondence. $\square$

#### Lemma. Regularity of a quotient

The Jacobian criterion for hypersurfaces, done right.

Let $R$ be a regular ring. Let $f \in R$. Assume there exists a derivation $D : R \to R$ such that $D(f)$ is a unit of $R/(f)$. Then $R/(f)$ is regular.

**Proof.** It suffices to prove this when $R$ is a local ring with maximal ideal $\mathfrak m$ and residue field $\kappa$. In this case it suffices to prove that $f \not \in \mathfrak m^2$, see Algebra, Lemma [Regular rings are Cohen–Macaulay](#native-algebra-lemma-regular-ring-cm). However, if $f \in \mathfrak m^2$ then $D(f) \in \mathfrak m$ by the Leibniz rule, a contradiction. $\square$

#### Lemma. Flatness of a completed direct sum
 Let $R$ be a ring. Let $I \subset R$ be an ideal. Let $A$ be a set. Assume $R$ is Noetherian. The completion $(\bigoplus\nolimits_{\alpha \in A} R)^\wedge$ is a flat $R$-module.

**Proof.** Denote \(R^\wedge\) the completion of \(R\) with respect to \(I\). As \(R \to R^\wedge\) is flat by Algebra, Lemma [Complete rings, formal power series and flatness](#native-algebra-lemma-completion-flat) it suffices to prove that \((\bigoplus\nolimits_{\alpha \in A} R)^\wedge\) is a flat \(R^\wedge\)-module (use Algebra, Lemma [Composition and flatness](#native-algebra-lemma-composition-flat)). Since 

\[
(\bigoplus\nolimits_{\alpha \in A} R)^\wedge
=
(\bigoplus\nolimits_{\alpha \in A} R^\wedge)^\wedge
\]

 we may replace \(R\) by \(R^\wedge\) and assume that \(R\) is complete with respect to \(I\) (see Algebra, Lemma [Complete rings and formal power series](#native-algebra-lemma-completion-complete)). In this case Lemma [Universal injectivity from a completed direct sum into a product](#native-more-algebra-lemma-ui-completion-direct-sum-into-product) tells us the map \((\bigoplus\nolimits_{\alpha \in A} R)^\wedge \to \prod_{\alpha \in A} R\) is universally injective. Thus, by Algebra, Lemma [Flatness](#native-algebra-lemma-ui-flat-domain) it suffices to show that \(\prod_{\alpha \in A} R\) is flat. By Algebra, Proposition [Criteria for coherent sheaves](#native-algebra-proposition-characterize-coherent) (and Algebra, Lemma [Coherent sheaves and Noetherian rings](#native-algebra-lemma-noetherian-coherent)) we see that \(\prod_{\alpha \in A} R\) is flat. \(\square\)

#### Lemma. Formal smoothness of henselization
 Let $(R, \mathfrak m, \kappa)$ be a local ring. Then

1.  $R \to R^h$, $R^h \to R^{sh}$, and $R \to R^{sh}$ are formally étale,

2.  $R \to R^h$, $R^h \to R^{sh}$, resp. $R \to R^{sh}$ are formally smooth in the $\mathfrak m^h$, $\mathfrak m^{sh}$, resp. $\mathfrak m^{sh}$-topology.

**Proof.** Part (1) follows from the fact that $R^h$ and $R^{sh}$ are directed colimits of étale algebras (by construction), that étale algebras are formally étale (Algebra, Lemma Formally smooth, unramified and étale ring maps, Theorem 3.1 and Sections 4–7), and that colimits of formally étale algebras are formally étale (Algebra, Lemma [Formal étaleness in a filtered colimit](#native-algebra-lemma-colimit-formally-etale)). Part (2) follows from the fact that a formally étale ring map is formally smooth and Lemma [Formal smoothness and smooth morphisms](#native-more-algebra-lemma-formally-smooth). $\square$

#### Lemma. Independence of a chosen set of ideal generators

Let $R$ be a ring. Let $I$ be an ideal generated by $f_1, \ldots, f_r \in R$.

1.  If $I$ can be generated by a quasi-regular sequence of length $r$, then $f_1, \ldots, f_r$ is a quasi-regular sequence.

2.  If $I$ can be generated by an $H_1$-regular sequence of length $r$, then $f_1, \ldots, f_r$ is an $H_1$-regular sequence.

3.  If $I$ can be generated by a Koszul-regular sequence of length $r$, then $f_1, \ldots, f_r$ is a Koszul-regular sequence.

**Proof.** If $I$ can be generated by a quasi-regular sequence of length $r$, then $I/I^2$ is free of rank $r$ over $R/I$. Since $f_1, \ldots, f_r$ generate by assumption we see that the images $\overline{f}_i$ form a basis of $I/I^2$ over $R/I$. It follows that $f_1, \ldots, f_r$ is a quasi-regular sequence as all this means, besides the freeness of $I/I^2$, is that the maps $\text{Sym}^n_{R/I}(I/I^2) \to I^n/I^{n + 1}$ are isomorphisms.

We continue to assume that $I$ can be generated by a quasi-regular sequence, say $g_1, \ldots, g_r$. Write $g_j = \sum a_{ij}f_i$. As $f_1, \ldots, f_r$ is quasi-regular according to the previous paragraph, we see that $\det(a_{ij})$ is invertible mod $I$. The matrix $a_{ij}$ gives a map $R^{\oplus r} \to R^{\oplus r}$ which induces a map of Koszul complexes $\alpha : K_\bullet(R, f_1, \ldots, f_r) \to K_\bullet(R, g_1, \ldots, g_r)$, see Lemma [Functoriality of the lifting construction](#native-more-algebra-lemma-functorial). This map becomes an isomorphism on inverting $\det(a_{ij})$. Since the cohomology modules of both $K_\bullet(R, f_1, \ldots, f_r)$ and $K_\bullet(R, g_1, \ldots, g_r)$ are annihilated by $I$, see Lemma [Koszul complexes and regular sequences](#native-more-algebra-lemma-homotopy-koszul), we see that $\alpha$ is a quasi-isomorphism.

Now assume that $g_1, \ldots, g_r$ is a $H_1$-regular sequence generating $I$. Then $g_1, \ldots, g_r$ is a quasi-regular sequence by Lemma [First-homology regularity implies quasi-regularity](#native-more-algebra-lemma-h1-regular-quasi-regular). By the previous paragraph we conclude that $f_1, \ldots, f_r$ is a $H_1$-regular sequence. Similarly for Koszul-regular sequences. $\square$

#### Lemma. Truncation of a Koszul-regular sequence
 Let $A$ be a ring. Let $f_1, \ldots, f_n, g_1, \ldots, g_m \in A$. If both $f_1, \ldots, f_n$ and $f_1, \ldots, f_n, g_1, \ldots, g_m$ are Koszul-regular sequences in $A$, then $\overline{g}_1, \ldots, \overline{g}_m$ in $A/(f_1, \ldots, f_n)$ form a Koszul-regular sequence.

**Proof.** Set $I = (f_1, \ldots, f_n)$. Our assumptions say that $K_\bullet(A, f_1, \ldots, f_n)$ is a finite free resolution of $A/I$ and $K_\bullet(A, f_1, \ldots, f_n, g_1, \ldots, g_m)$ is a finite free resolution of $A/(f_i, g_j)$ over $A$. Then $$\begin{aligned}
A/(f_i, g_j) & \cong K_\bullet(A, f_1, \ldots, f_n, g_1, \ldots, g_m) \\
& = \text{Tot}(K_\bullet(A, f_1, \ldots, f_n) \otimes_A
K_\bullet(A, g_1, \ldots, g_m)) \\
& \cong A/I \otimes_A K_\bullet(A, g_1, \ldots, g_m) \\
& = K_\bullet(A/I, \overline{g}_1, \ldots, \overline{g}_m)
\end{aligned}$$ The first quasi-isomorphism $\cong$ by assumption. The first equality by Lemma [Koszul complexes, regular sequences and derived categories](#native-more-algebra-lemma-join-sequences-koszul-complex). The second quasi-isomorphism by (the dual of) Homology, Lemma [Derived categories (uncovered prerequisite)](#uncovered-homology-lemma-double-complex-gives-resolution) as the $q$th row of the double complex $K_\bullet(A, f_1, \ldots, f_n) \otimes_A K_\bullet(A, g_1, \ldots, g_m)$ is a resolution of $A/I \otimes_A K_q(A, g_1, \ldots, g_m)$. The second equality is clear. Hence we win. $\square$

#### Lemma. Regular sequences are Koszul-regular

*Source credit:* the original source citation FAC (Chapter III, §3, no. 62, Proposition 1, pp. 254--255) the original source citation FAC (Chapter III, §4, no. 69, Lemma 1, p. 262) the original source citation FAC (Chapter III, §5, no. 75, proof of Theorem 3, pp. 269--270)

The hypothesis of the cited proposition is precisely the injectivity condition in the first sentence below, applied to $t_0^k, \ldots, t_r^k$. In particular, it does not include the nonvanishing condition sometimes imposed in the definition of a regular sequence. The source uses the resulting exactness of the positive cochain Koszul complex to identify degree-zero cocycles and to kill its intermediate cohomology.

No. 69 applies the ring case to the powers of all the variables in a polynomial ring. For $k\geq1$ these powers form a regular sequence; for $k=0$ the Koszul complex is contractible because its entries are units. Deleting the final ring term gives the graded free resolution of the ideal generated by the powers that is isolated in the next lemma.

No. 75 uses the same construction for a regular sequence generating the ideal of a nonsingular subvariety in projective space. Its free module in degree $q$ has the exterior basis indexed by increasing $q$-tuples, and its augmented Koszul complex resolves the local ring of the subvariety. In the printed general differential the sign is $(-1)^j$, but the immediately following degree-one formula is $d(e\langle i\rangle)=f_i$; substituting $q=1$ in the general formula would instead give $-f_i$. The corrected formula uses $(-1)^{j + 1}$, as in Definition [The Koszul complex](#native-more-algebra-definition-koszul), and therefore agrees with the displayed degree-one case. If the opposite sign is used uniformly in every positive degree, multiplying homological degree $q$ by $(-1)^q$ identifies the resulting complex with this one, so the exactness conclusion is unchanged.

Let $R$ be a ring, $M$ an $R$-module, and $f_1, \ldots, f_r \in R$ such that for $i = 1, \ldots, r$ multiplication by $f_i$ is injective on $M/(f_1, \ldots, f_{i - 1})M$. Then $f_1, \ldots, f_r$ is $M$-Koszul regular. In particular, an $M$-regular sequence is $M$-Koszul-regular and any regular sequence is Koszul-regular.

**Proof.** Let $R$, $M$, $f_1, \ldots, f_r$ be as in the first sentence of the lemma. If $r = 1$, it is immediate that $f_1$ is $M$-Koszul-regular. Assume $r > 1$. Since $f_1$ is a nonzerodivisor on $M$, we obtain a short exact sequence of complexes: $$0 \to K_\bullet(f_2, \ldots, f_r) \otimes M
\xrightarrow{f_1}
K_\bullet(f_2, \ldots, f_r) \otimes M \to
K_\bullet(\overline{f}_2, \ldots, \overline{f}_r) \otimes M/f_1M \to 0$$ Here $\overline{f}_i$ is the image of $f_i$ in $R/(f_1)$. By Lemma [Koszul complexes, regular sequences and derived categories](#native-more-algebra-lemma-cone-koszul) the complex $K_\bullet(f_1, \ldots, f_r)$ is isomorphic to the cone of multiplication by $f_1$ on $K_\bullet(f_2, \ldots, f_r)$. Thus $K_\bullet(R, f_1, \ldots, f_r) \otimes M$ is isomorphic to the cone on the first map. Hence $K_\bullet(\overline{f}_2, \ldots, \overline{f}_r) \otimes M/f_1M$ is quasi-isomorphic to $K_\bullet(f_1, \ldots, f_r) \otimes M$. As $R/(f_1)$, $M/f_1M$, $\overline{f}_2, \ldots, \overline{f}_r$ satisfy the conditions of the lemma, by induction we conclude this complex is acyclic in postive degrees. This finishes the proof of the first statement. The second statement immediately follows from the first. $\square$

#### Lemma. Base change of first-homology regularity
 Let $A \to B$ be a ring map. Let $f_1, \ldots, f_r$ be a sequence in $B$ such that $B/(f_1, \ldots, f_r)$ is $A$-flat. Let $A \to A'$ be a ring map. Then the canonical map $$H_1(K_\bullet(B, f_1, \ldots, f_r)) \otimes_A A'
\longrightarrow
H_1(K_\bullet(B', f'_1, \ldots, f'_r))$$ is surjective. Here $B' = B \otimes_A A'$ and $f_i' \in B'$ is the image of $f_i$.

**Proof.** The sequence $$\wedge^2(B^{\oplus r}) \to B^{\oplus r} \to B \to B/J \to 0$$ is a complex of $A$-modules with $B/J$ flat over $A$ and cohomology group $H_1 = H_1(K_\bullet(B, f_1, \ldots, f_r))$ in the spot $B^{\oplus r}$. If we tensor this with $A'$ we obtain a complex $$\wedge^2((B')^{\oplus r}) \to (B')^{\oplus r} \to B' \to B'/J' \to 0$$ which is exact at $B'$ and $B'/J'$. In order to compute its cohomology group $H'_1 = H_1(K_\bullet(B', f'_1, \ldots, f'_r))$ at $(B')^{\oplus r}$ we split the first sequence above into the exact sequences $0 \to J \to B \to B/J \to 0$, $0 \to K \to B^{\oplus r} \to J \to 0$, and $\wedge^2(B^{\oplus r}) \to K \to H_1 \to 0$. Tensoring over $A$ with $A'$ we obtain the exact sequences $$\begin{matrix}
0 \to J \otimes_A A' \to B \otimes_A A' \to (B/J) \otimes_A A' \to 0 \\
K \otimes_A A' \to B^{\oplus r} \otimes_A A' \to J \otimes_A A' \to 0 \\
\wedge^2(B^{\oplus r}) \otimes_A A' \to K \otimes_A A' \to H_1 \otimes_A A'
\to 0
\end{matrix}$$ where the first one is exact as $B/J$ is flat over $A$, see Algebra, Lemma [Tor vanishing for a flat module](#native-algebra-lemma-flat-tor-zero). We conclude that $J' = J \otimes_A A' \subset B'$ and that $K \otimes_A A' \to \operatorname{Ker}((B')^{\oplus r} \to B')$ is surjective. Thus $$\begin{aligned}
H_1 \otimes_A A'
& =
\operatorname{Coker}\left(\wedge^2(B^{\oplus r}) \otimes_A A' \to K \otimes_A A'\right) \\
& \to
\operatorname{Coker}\left(
\wedge^2((B')^{\oplus r})  \to \operatorname{Ker}((B')^{\oplus r} \to B')
\right) = H'_1
\end{aligned}$$ is surjective too. $\square$

#### Lemma. Koszul regularity implies first-homology regularity

A $M$-Koszul-regular sequence is $M$-$H_1$-regular. A Koszul-regular sequence is $H_1$-regular.

**Proof.** This is immediate from the definition. $\square$

#### Lemma. First-homology regularity implies quasi-regularity
 An $M$-$H_1$-regular sequence is $M$-quasi-regular.

**Proof.** Let $R$ be a ring and let $M$ be an $R$-module. Let $f_1, \ldots, f_r$ be an $M$-$H_1$-regular sequence. Denote $J = (f_1, \ldots, f_r)$. The assumption means that we have an exact sequence $$\wedge^2(R^r) \otimes M \to R^{\oplus r} \otimes M \to JM \to 0$$ where the first arrow is given by $e_i \wedge e_j \otimes m \mapsto (f_ie_j - f_je_i) \otimes m$. Tensoring the sequence with $R/J$ we see that $$JM/J^2M = (R/J)^{\oplus r} \otimes_R M = (M/JM)^{\oplus r}$$ is a finite free module. To finish the proof we have to prove for every $n \geq 2$ the following: if $$\xi = \sum\nolimits_{|I| = n, I = (i_1, \ldots, i_r)}
m_I f_1^{i_1} \ldots f_r^{i_r} \in J^{n + 1}M$$ then $m_I \in JM$ for all $I$. In the next paragraph, we prove $m_I \in JM$ for $I = (0, \ldots, 0, n)$ and in the last paragraph we deduce the general case from this special case.

Let \(I = (0, \ldots, 0, n)\). Let \(\xi\) be as above. We can write \(\xi = m_1 f_1 + \ldots + m_{r - 1}f_{r - 1} + m_I f_r^n\). As we have assumed \(\xi \in J^{n + 1}M\), we can also write \(\xi = \sum_{1 \leq i \leq j \leq r - 1} m_{ij}f_if_j + \sum_{1 \leq i \leq r - 1}m'_i f_if_r^n + m'' f_r^{n + 1}\). Then we see that 

\[
\begin{matrix}
(m_1 - m_{11}f_1 - m'_1f_r^n)f_1 + \\
(m_2 - m_{12}f_1 - m_{22}f_2 - m'_2f_r^n)f_2 + \\
\ldots + \\
(m_{r - 1} - m_{1 r - 1}f_1 - \ldots - m_{r - 1 r - 1}f_{r - 1}
- m'_{r - 1}f_r^n)f_{r - 1} + \\
(m_I - m'' f_r)f_r^n = 0
\end{matrix}
\]

 Since \(f_1, \ldots, f_{r - 1}, f_r^n\) is \(M\)-\(H_1\)-regular by Lemma [Koszul complexes, regular sequences and regular rings](#native-more-algebra-lemma-mult-koszul-regular) we see that \(m_I - m'' f_r\) is in the submodule \(f_1M + \ldots + f_{r - 1}M + f_r^nM\). Thus \(m_I \in f_1M + \ldots + f_rM\).

Let $S = R[x_1, x_2, \ldots, x_r, 1/x_r]$. The ring map $R \to S$ is faithfully flat, hence $f_1, \ldots, f_r$ is an $M$-$H_1$-regular sequence in $S$, see Lemma [Base change for Koszul complexes, regular sequences and flatness](#native-more-algebra-lemma-koszul-regular-flat-base-change). By Lemma [Changing a basis of a finite free complex](#native-more-algebra-lemma-change-basis) we see that $$g_1 = f_1 - \frac{x_1}{x_r} f_r,
\ \ldots,
\ g_{r - 1} = f_{r - 1} - \frac{x_{r - 1}}{x_r} f_r,
\ g_r = \frac{1}{x_r}f_r$$ is an $M$-$H_1$-regular sequence in $S$. Finally, note that our element $\xi$ can be rewritten $$\xi = \sum\nolimits_{|I| = n, I = (i_1, \ldots, i_r)}
m_I (g_1 + x_1 g_r)^{i_1} \ldots (g_{r - 1} + x_{r - 1} g_r)^{i_{r - 1}}
(x_rg_r)^{i_r}$$ and the coefficient of $g_r^n$ in this expression is $$\sum m_I x_1^{i_1} \ldots x_r^{i_r}$$ By the case discussed in the previous paragraph this sum is in $J(M \otimes_R S)$. Since the monomials $x_1^{i_1} \ldots x_r^{i_r}$ form part of an $R$-basis of $S$ over $R$ we conclude that $m_I \in J$ for all $I$ as desired. $\square$

#### Lemma. Dimension of a completion
 Let $A$ be a Noetherian local ring. Then $\dim(A) = \dim(A^\wedge)$.

**Proof.** By Algebra, Lemma [Complete rings and formal power series](#native-algebra-lemma-completion-complete) the map $A \to A^\wedge$ induces isomorphisms $A/\mathfrak m^n = A^\wedge/(\mathfrak m^\wedge)^n$ for $n \geq 1$. By Algebra, Lemma [Restriction of scalars for a finite module](#native-algebra-lemma-pushdown-module) this implies that $$\text{length}_A(A/\mathfrak m^n) =
\text{length}_{A^\wedge}(A^\wedge/(\mathfrak m^\wedge)^n)$$ for all $n \geq 1$. Thus $d(A) = d(A^\wedge)$ and we conclude by Algebra, Proposition [Dimension and codimension](#native-algebra-proposition-dimension). An alternative proof is to use Algebra, Lemma [Dimension of a flat family](#native-algebra-lemma-dimension-base-fibre-equals-total). $\square$

#### Lemma. Subfields of a formal power-series ring
 Let $k$ be a field of characteristic $p > 0$. Let $\{x_i\}_{i \in I}$ be a $p$-basis for $k$. Let $n, m \geq 0$. Let $K$ be the fraction field of $A = k[[x_1, \ldots, x_n]][y_1, \ldots, y_m]$. Let $J$ be a finite subset of $I$. Consider the subfield $k/k_J/k^p$ generated by $k^p$ and $x_i$ with $i \in I \setminus J$. The fraction fields $K_J$ of $$A_J = k_J[[x_1^p, \ldots, x_n^p]][y_1^p, \ldots, y_m^p]$$ form a family of subfields of $K$ as in Lemma [Intersections of subfields](#native-more-algebra-lemma-intersection-subfields). Moreover, each of the ring extensions $A_J \subset A$ is finite.

**Proof.** Since $k/k_J$ is finite, the ring extension $k_J[[x_1^p, \ldots, x_d^p]] \subset k[[x_1, \ldots, x_d]]$ is finite by Algebra, Lemma [Finiteness after completion](#native-algebra-lemma-finite-after-completion). This implies that $A_J \to A$ is finite.

Let us check properties (1), (2), (3) of Lemma [Intersections of subfields](#native-more-algebra-lemma-intersection-subfields). Proof of (1). For $a \in A$ we see that $a^p \in A_J$. Hence $K^p \subset K_J$. Proof of (2). Suppose that $f/g^p \in K$, $f, g \in A$, $g \not = 0$ is contained in $K_J$ for every choice of $J$. Fix $J$ for the moment. Since $f/g^p \in K_J$ we can write $f/g^p = a/b^p$ with $a \in A_J$ and $b \in A$ nonzero. Hence $b^p f \in A_J$. For any $A_J$-derivation $D : A \to A$ we see that $0 = D(b^pf) = b^p D(f)$ hence $D(f) = 0$ as $A$ is a domain. Taking $D = \partial_{x_i}$ and $D = \partial_{y_j}$ we conclude that $f \in k[[x_1^p, \ldots, x_n^p]][y_1^p, \ldots, y_m^p]$. Applying a $k_J$-derivation $\theta : k \to k$ we similarly conclude that all coefficients of $f$ are in $k_J$, i.e., $f \in A_J$. Since it is clear that $A^p = \bigcap\nolimits_J A_J$ where $J$ ranges over all subfields as in the lemma we conclude $f \in A^p$ as desired. Proof of (3). This is clear because $K_{J \cup J'} \subset K_J \cap K_{J'}$. $\square$

#### Lemma. Noetherian fibres of a filtered colimit of étale maps
 Let $A$ be a ring. Let $B$ be a filtered colimit of étale $A$-algebras. Let $\mathfrak p$ be a prime of $A$. If $B$ is Noetherian, then there are finitely many primes $\mathfrak q_1, \ldots, \mathfrak q_r$ lying over $\mathfrak p$, we have $B \otimes_A \kappa(\mathfrak p) = \prod \kappa(\mathfrak q_i)$, and each of the field extensions $\kappa(\mathfrak q_i)/\kappa(\mathfrak p)$ is separable algebraic.

**Proof.** Write $B$ as a filtered colimit $B = \mathop{\operatorname{colim}} B_i$ with $A \to B_i$ étale. Then on the one hand $B \otimes_A \kappa(\mathfrak p) = \mathop{\operatorname{colim}} B_i \otimes_A \kappa(\mathfrak p)$ is a filtered colimit of étale $\kappa(\mathfrak p)$-algebras, and on the other hand it is Noetherian. An étale $\kappa(\mathfrak p)$-algebra is a finite product of finite separable field extensions (Algebra, Lemma Formally smooth, unramified and étale ring maps, Theorem 3.1 and Sections 4–7). Hence there are no nontrivial specializations between the primes (which are all maximal and minimal primes) of the algebras $B_i \otimes_A \kappa(\mathfrak p)$ and hence there are no nontrivial specializations between the primes of $B \otimes_A \kappa(\mathfrak p)$. Thus $B \otimes_A \kappa(\mathfrak p)$ is reduced and has finitely many primes which all minimal. Thus it is a finite product of fields (use Algebra, Lemma [Total rings of fractions without embedded primes](#native-algebra-lemma-total-ring-fractions-no-embedded-points) or Algebra, Proposition [Rings of dimension zero](#native-algebra-proposition-dimension-zero-ring)). Each of these fields is a colimit of finite separable extensions and hence the final statement of the lemma follows. $\square$

#### Lemma. Reducedness of a henselization

Reducedness passes to the (strict) henselization.

Let $R$ be a local ring. The following are equivalent: $R$ is reduced, the henselization $R^h$ of $R$ is reduced, and the strict henselization $R^{sh}$ of $R$ is reduced.

**Proof.** The ring maps $R \to R^h \to R^{sh}$ are faithfully flat. Hence one direction of the implications follows from Algebra, Lemma [Descent of commutative algebra](#native-algebra-lemma-descent-reduced). Conversely, assume $R$ is reduced. Since $R^h$ and $R^{sh}$ are filtered colimits of étale, hence smooth $R$-algebras, the result follows from Algebra, Lemma [Commutative algebra](#native-algebra-lemma-reduced-goes-up). $\square$

#### Proposition. Formal smoothness from flatness and formally smooth fibres
 Let $A \to B$ be a local homomorphism of Noetherian local rings. Let $k$ be the residue field of $A$ and $\overline{B} = B \otimes_A k$ the special fibre. The following are equivalent

1.  $A \to B$ is flat and $\overline{B}$ is geometrically regular over $k$,

2.  $A \to B$ is flat and $k \to \overline{B}$ is formally smooth in the $\mathfrak m_{\overline{B}}$-adic topology, and

3.  $A \to B$ is formally smooth in the $\mathfrak m_B$-adic topology.

**Proof.** The equivalence of (1) and (2) follows from Theorem [Regular maps and formal smoothness](#native-more-algebra-theorem-regular-fs).

Assume (3). By Lemma [Formal smoothness and flatness](#native-more-algebra-lemma-formally-smooth-flat) we see that $A \to B$ is flat. By Lemma [Base change of formal smoothness](#native-more-algebra-lemma-base-change-fs) we see that $k \to \overline{B}$ is formally smooth in the $\mathfrak m_{\overline{B}}$-adic topology. Thus (2) holds.

Assume (2). Lemma [Formal smoothness and completion](#native-more-algebra-lemma-formally-smooth-completion) tells us formal smoothness is preserved under completion. The same is true for flatness by Algebra, Lemma Completion, Theorems 3.1–3.3, 4.1 and 5.1. Hence we may replace $A$ and $B$ by their respective completions and assume that $A$ and $B$ are Noetherian complete local rings. In this case choose a diagram $$\begin{gathered}\begin{matrix}S & B \\ R & A\end{matrix} \\[6pt] \begin{aligned}S & \longrightarrow B \\ R & \longrightarrow S \\ R & \longrightarrow A \\ A & \longrightarrow B\end{aligned}\end{gathered}$$ as in Lemma [Complete rings, formal power series and Noetherian rings](#native-more-algebra-lemma-embed-map-noetherian-complete-local-rings). We will use all of the properties of this diagram without further mention. Fix a regular system of parameters $t_1, \ldots, t_d$ of $R$ with $t_1 = p$ in case the characteristic of $k$ is $p > 0$. Set $\overline{S} = S \otimes_R k$. Consider the short exact sequence $$0 \to J \to S \to B \to 0$$ As $\overline{B}$ and $\overline{S}$ are regular, the kernel of $\overline{S} \to \overline{B}$ is generated by elements $\overline{x}_1, \ldots, \overline{x}_r$ which form part of a regular system of parameters of $\overline{S}$, see Algebra, Lemma [Regular rings](#native-algebra-lemma-regular-quotient-regular). Lift these elements to $x_1, \ldots, x_r \in J$. Then $t_1, \ldots, t_d, x_1, \ldots, x_r$ is part of a regular system of parameters for $S$. Hence $S/(x_1, \ldots, x_r)$ is a power series ring over a field (if the characteristic of $k$ is zero) or a power series ring over a Cohen ring (if the characteristic of $k$ is $p > 0$), see Lemma [Complete rings and formal power series](#native-more-algebra-lemma-quotient-power-series-ring-over-cohen). Moreover, it is still the case that $R \to S/(x_1, \ldots, x_r)$ maps $t_1, \ldots, t_d$ to a part of a regular system of parameters of $S/(x_1, \ldots, x_r)$. In other words, we may replace $S$ by $S/(x_1, \ldots, x_r)$ and assume we have a diagram $$\begin{gathered}\begin{matrix}S & B \\ R & A\end{matrix} \\[6pt] \begin{aligned}S & \longrightarrow B \\ R & \longrightarrow S \\ R & \longrightarrow A \\ A & \longrightarrow B\end{aligned}\end{gathered}$$ as in Lemma [Complete rings, formal power series and Noetherian rings](#native-more-algebra-lemma-embed-map-noetherian-complete-local-rings) with moreover $\overline{S} = \overline{B}$. In this case the map $$S \otimes_R A \longrightarrow B$$ is an isomorphism as it is surjective, an isomorphism on special fibres, and source and target are flat over $A$ (for example use Algebra, Lemma [Injectivity from a fibrewise injectivity criterion](#native-algebra-lemma-mod-injective) or use that tensoring the short exact sequence $0 \to I \to S \otimes_R A \to B \to 0$ over $A$ with $k$ we find $I \otimes_A k = 0$ hence $I = 0$ by Nakayama). Thus by Lemma [Base change of formal smoothness](#native-more-algebra-lemma-base-change-fs) it suffices to show that $R \to S$ is formally smooth in the $\mathfrak m_S$-adic topology. Of course, since $\overline{S} = \overline{B}$, we have that $\overline{S}$ is formally smooth over $k = R/\mathfrak m_R$.

Choose elements $y_1, \ldots, y_m \in S$ such that $t_1, \ldots, t_d, y_1, \ldots, y_m$ is a regular system of parameters for $S$. If the characteristic of $k$ is zero, choose a coefficient field $K \subset S$ and if the characteristic of $k$ is $p > 0$ choose a Cohen ring $\Lambda \subset S$ with residue field $K$. At this point the map $K[[t_1, \ldots, t_d, y_1, \ldots, y_m]] \to S$ (characteristic zero case) or $\Lambda[[t_2, \ldots, t_d, y_1, \ldots, y_m]] \to S$ (characteristic $p > 0$ case) is an isomorphism, see Lemma [Complete rings and formal power series](#native-more-algebra-lemma-quotient-power-series-ring-over-cohen). From now on we think of $S$ as the above power series ring.

The rest of the proof is analogous to the argument in the proof of Theorem [Regular maps and formal smoothness](#native-more-algebra-theorem-regular-fs). Choose a solid diagram $$\begin{gathered}\begin{matrix}S & N/J \\ R & N\end{matrix} \\[6pt] \begin{aligned}S & \xrightarrow{\bar\psi} N/J \\ S & \dashrightarrow N \\ R & \xrightarrow{i} S \\ R & \xrightarrow{\varphi} N \\ N & \xrightarrow{\pi} N/J\end{aligned}\end{gathered}$$ as in Definition [Formally smooth ring maps](#native-more-algebra-definition-formally-smooth). As $J^2 = 0$ we see that $J$ has a canonical $N/J$ module structure and via $\bar\psi$ a $S$-module structure. As $\bar\psi$ is continuous for the $\mathfrak m_S$-adic topology we see that $\mathfrak m_S^nJ = 0$ for some $n$. Hence we can filter $J$ by $N/J$-submodules $0 \subset J_1 \subset J_2 \subset \ldots \subset J_n = J$ such that each quotient $J_{t + 1}/J_t$ is annihilated by $\mathfrak m_S$. Considering the sequence of ring maps $N \to N/J_1 \to N/J_2 \to \ldots \to N/J$ we see that it suffices to prove the existence of the dotted arrow when $J$ is annihilated by $\mathfrak m_S$, i.e., when $J$ is a $K$-vector space.

Assume given a diagram as above such that $J$ is annihilated by $\mathfrak m_S$. As $\mathbf{Q} \to S$ (characteristic zero case) or $\mathbf{Z} \to S$ (characteristic $p > 0$ case) is formally smooth in the $\mathfrak m_S$-adic topology (see Lemma [Formal smoothness and complete rings and formal power series](#native-more-algebra-lemma-power-series-ring-over-cohen-fs)), we can find a ring map $\psi : S \to N$ such that $\pi \circ \psi = \bar \psi$. Since $S$ is a power series ring in $t_1, \ldots, t_d$ (characteristic zero) or $t_2, \ldots, t_d$ (characteristic $p > 0$) over a subring, it follows from the universal property of power series rings that we can change our choice of $\psi$ so that $\psi(t_i)$ equals $\varphi(t_i)$ (automatic for $t_1 = p$ in the characteristic $p$ case). Then $\psi \circ i$ and $\varphi : R \to N$ are two maps whose compositions with $\pi$ are equal and which agree on $t_1, \ldots, t_d$. Hence $D = \psi \circ i - \varphi : R \to J$ is a derivation which annihilates $t_1, \ldots, t_d$. By Algebra, Lemma [The universal property of Kähler differentials](#native-algebra-lemma-universal-omega) we can write $D = \xi \circ \text{d}$ for some $R$-linear map $\xi : \Omega_{R/\mathbf{Z}} \to J$ which annihilates $\text{d}t_1, \ldots, \text{d}t_d$ (by construction) and $\mathfrak m_R \Omega_{R/\mathbf{Z}}$ (as $J$ is annihilated by $\mathfrak m_R$). Hence $\xi$ factors as a composition $$\Omega_{R/\mathbf{Z}} \to \Omega_{k/\mathbf{Z}} \xrightarrow{\xi'} J$$ where $\xi'$ is $k$-linear. Using the $K$-vector space structure on $J$ we extend $\xi'$ to a $K$-linear map $$\xi'' : \Omega_{k/\mathbf{Z}} \otimes_k K \longrightarrow J.$$ Using that $\overline{S}/k$ is formally smooth we see that $$\Omega_{k/\mathbf{Z}} \otimes_k K \to
\Omega_{\overline{S}/\mathbf{Z}} \otimes_S K$$ is injective by Theorem [Regular maps and formal smoothness](#native-more-algebra-theorem-regular-fs) (this is true also in the characteristic zero case as it is even true that $\Omega_{k/\mathbf{Z}} \to \Omega_{K/\mathbf{Z}}$ is injective in characteristic zero, see Algebra, Proposition [Characterizations of separable field extensions](#native-algebra-proposition-characterize-separable-field-extensions)). Hence we can find a $K$-linear map $\xi''' : \Omega_{\overline{S}/\mathbf{Z}} \otimes_S K \to J$ whose restriction to $\Omega_{k/\mathbf{Z}} \otimes_k K$ is $\xi''$. Write $$D' : S \xrightarrow{\text{d}} \Omega_{S/\mathbf{Z}}
\to \Omega_{\overline{S}/\mathbf{Z}} \to
\Omega_{\overline{S}/\mathbf{Z}} \otimes_S K \xrightarrow{\xi'''} J.$$ Finally, set $\psi' = \psi - D' : S \to N$. The reader verifies that $\psi'$ is a ring map such that $\pi \circ \psi' = \bar \psi$ and such that $\psi' \circ i = \varphi$ as desired. $\square$

#### Lemma. Base change of formal smoothness

Let $R$, $S$ be rings. Let $\mathfrak n \subset S$ be an ideal. Let $R \to S$ be formally smooth for the $\mathfrak n$-adic topology. Let $R \to R'$ be any ring map. Then $R' \to S' = S \otimes_R R'$ is formally smooth in the $\mathfrak n' = \mathfrak nS'$-adic topology.

**Proof.** Let a solid diagram $$\begin{gathered}\begin{matrix}S & S' & A/J \\ R & R' & A\end{matrix} \\[6pt] \begin{aligned}S & \longrightarrow S' \\ S & \dashrightarrow A \\ S' & \longrightarrow A/J \\ S' & \dashrightarrow A \\ R & \longrightarrow S \\ R & \longrightarrow R' \\ R' & \longrightarrow A \\ R' & \longrightarrow S' \\ A & \longrightarrow A/J\end{aligned}\end{gathered}$$ as in Definition [Formally smooth ring maps](#native-more-algebra-definition-formally-smooth) be given. Then the composition $S \to S' \to A/J$ is continuous. By assumption the longer dotted arrow exists. By the universal property of tensor product we obtain the shorter dotted arrow. $\square$

#### Remark. The finite-equation meaning of formal smoothness

The assertion of Lemma [Lifting formal smoothness](#native-more-algebra-lemma-lift-fs) is quite strong. Namely, suppose that we have a diagram $$\begin{gathered}\begin{matrix}\phantom{X} & B \\ A & A'\end{matrix} \\[6pt] \begin{aligned}A & \longrightarrow A' \\ A' & \longrightarrow B\end{aligned}\end{gathered}$$ of local homomorphisms of Noetherian complete local rings where $A \to A'$ induces an isomorphism of residue fields $k = A/\mathfrak m_A = A'/\mathfrak m_{A'}$ and with $B \otimes_{A'} k$ formally smooth over $k$. Then we can extend this to a commutative diagram $$\begin{gathered}\begin{matrix}C & B \\ A & A'\end{matrix} \\[6pt] \begin{aligned}C & \longrightarrow B \\ A & \longrightarrow A' \\ A & \longrightarrow C \\ A' & \longrightarrow B\end{aligned}\end{gathered}$$ of local homomorphisms of Noetherian complete local rings where $A \to C$ is formally smooth in the $\mathfrak m_C$-adic topology and where $C \otimes_A k \cong B \otimes_{A'} k$. Namely, pick $A \to C$ as in Lemma [Lifting formal smoothness](#native-more-algebra-lemma-lift-fs) lifting $B \otimes_{A'} k$ over $k$. By formal smoothness we can find the arrow $C \to B$, see Lemma [Lifting derived commutative algebra](#native-more-algebra-lemma-lift-continuous). Denote $C \otimes_A^\wedge A'$ the completion of $C \otimes_A A'$ with respect to the ideal $C \otimes_A \mathfrak m_{A'}$. Note that $C \otimes_A^\wedge A'$ is a Noetherian complete local ring (see Algebra, Lemma [Complete rings, formal power series and Noetherian rings](#native-algebra-lemma-completion-noetherian)) which is flat over $A'$ (see Algebra, Lemma [Flatness and modules](#native-algebra-lemma-flat-module-powers)). We have moreover

1.  $C \otimes_A^\wedge A' \to B$ is surjective,

2.  if $A \to A'$ is surjective, then $C \to B$ is surjective,

3.  if $A \to A'$ is finite, then $C \to B$ is finite, and

4.  if $A' \to B$ is flat, then $C \otimes_A^\wedge A' \cong B$.

Namely, by Nakayama's lemma for nilpotent ideals (see Algebra, Lemma [Nakayama's lemma](#native-algebra-lemma-nak)) we see that $C \otimes_A k \cong B \otimes_{A'} k$ implies that $C \otimes_A A'/\mathfrak m_{A'}^n \to B/\mathfrak m_{A'}^nB$ is surjective for all $n$. This proves (1). Parts (2) and (3) follow from part (1). Part (4) follows from Algebra, Lemma [Injectivity from a fibrewise injectivity criterion](#native-algebra-lemma-mod-injective).

#### Lemma. Descent of formal smoothness

Let $R$, $S$ be rings. Let $\mathfrak n \subset S$ be an ideal. Let $R \to R'$ be a ring map. Set $S' = S \otimes_R R'$ and $\mathfrak n' = \mathfrak nS$. If

1.  the map $R \to R'$ embeds $R$ as a direct summand of $R'$ as an $R$-module, and

2.  $R' \to S'$ is formally smooth for the $\mathfrak n'$-adic topology,

then $R \to S$ is formally smooth in the $\mathfrak n$-adic topology.

**Proof.** Let a solid diagram $$\begin{gathered}\begin{matrix}S & A/J \\ R & A\end{matrix} \\[6pt] \begin{aligned}S & \longrightarrow A/J \\ R & \longrightarrow S \\ R & \longrightarrow A \\ A & \longrightarrow A/J\end{aligned}\end{gathered}$$ as in Definition [Formally smooth ring maps](#native-more-algebra-definition-formally-smooth) be given. Set $A' = A \otimes_R R'$ and $J' = \operatorname{Im}(J \otimes_R R' \to A')$. The base change of the diagram above is the diagram $$\begin{gathered}\begin{matrix}S' & A'/J' \\ R' & A'\end{matrix} \\[6pt] \begin{aligned}S' & \longrightarrow A'/J' \\ S' & \overset{\psi'}{\dashrightarrow} A' \\ R' & \longrightarrow S' \\ R' & \longrightarrow A' \\ A' & \longrightarrow A'/J'\end{aligned}\end{gathered}$$ with continuous arrows. By condition (2) we obtain the dotted arrow $\psi' : S' \to A'$. Using condition (1) choose a direct summand decomposition $R' = R \oplus C$ as $R$-modules. (Warning: $C$ isn't an ideal in $R'$.) Then $A' = A \oplus A \otimes_R C$. Set $$J'' = \operatorname{Im}(J \otimes_R C \to A \otimes_R C) \subset J' \subset A'.$$ Then $J' = J \oplus J''$ as $A$-modules. The image of the composition $\psi : S \to A'$ of $\psi'$ with $S \to S'$ is contained in $A + J' = A \oplus J''$. However, in the ring $A + J' = A \oplus J''$ the $A$-submodule $J''$ is an ideal! (Use that $J^2 = 0$.) Hence the composition $S \to A + J' \to (A + J')/J'' = A$ is the arrow we were looking for. $\square$

#### Lemma. Lifting formal smoothness
 Let $A \to B$ be a local homomorphism of Noetherian local rings. Let $D : A \to A$ be a derivation. Assume that $B$ is complete and $A \to B$ is formally smooth in the $\mathfrak m_B$-adic topology. Then there exists an extension $D' : B \to B$ of $D$.

**Proof.** Denote $B[\epsilon] = B[x]/(x^2)$ the ring of dual numbers over $B$. Consider the ring map $\psi : A \to B[\epsilon]$, $a \mapsto a + \epsilon D(a)$. Consider the commutative diagram $$\begin{gathered}\begin{matrix}B & B \\ A & B[\epsilon]\end{matrix} \\[6pt] \begin{aligned}B & \xrightarrow{1} B \\ A & \longrightarrow B \\ A & \xrightarrow{\psi} B[\epsilon] \\ B[\epsilon] & \longrightarrow B\end{aligned}\end{gathered}$$ By Lemma [Lifting derived commutative algebra](#native-more-algebra-lemma-lift-continuous) and the assumption of formal smoothness of $B/A$ we find a map $\varphi : B \to B[\epsilon]$ fitting into the diagram. Write $\varphi(b) = b + \epsilon D'(b)$. Then $D' : B \to B$ is the desired extension. $\square$

#### Definition. Formally smooth ring maps
 Let $R \to S$ be a homomorphism of topological rings with $R$ and $S$ linearly topologized. We say $S$ is *formally smooth over $R$* if for every commutative solid diagram $$\begin{gathered}\begin{matrix}S & A/J \\ R & A\end{matrix} \\[6pt] \begin{aligned}S & \longrightarrow A/J \\ S & \dashrightarrow A \\ R & \longrightarrow A \\ R & \longrightarrow S \\ A & \longrightarrow A/J\end{aligned}\end{gathered}$$ of homomorphisms of topological rings where $A$ is a discrete ring and $J \subset A$ is an ideal of square zero, a dotted arrow exists which makes the diagram commute.

#### Lemma. Derived commutative algebra

Let $\varphi : R \to S$ be a ring map. Let $I \subset R$ and $J \subset S$ be ideals and endow $R$ with the $I$-adic topology and $S$ with the $J$-adic topology. Then $\varphi$ is a homomorphism of topological rings if and only if $\varphi(I^n) \subset J$ for some $n \geq 1$.

**Proof.** Omitted. $\square$

#### Lemma. Universal injectivity from a completed direct sum into a product

Let $R$ be a ring. Let $I \subset R$ be an ideal. Let $A$ be a set. Assume $R$ is Noetherian and complete with respect to $I$. There is a canonical map $$\left(\bigoplus\nolimits_{\alpha \in A} R\right)^\wedge
\longrightarrow
\prod\nolimits_{\alpha \in A} R$$ from the $I$-adic completion of the direct sum into the product which is universally injective.

**Proof.** By definition an element $x$ of the left hand side is $x = (x_n)$ where $x_n = (x_{n, \alpha}) \in \bigoplus\nolimits_{\alpha \in A} R/I^n$ such that $x_{n, \alpha} = x_{n + 1, \alpha} \bmod I^n$. As $R = R^\wedge$ we see that for any $\alpha$ there exists a $y_\alpha \in R$ such that $x_{n, \alpha} = y_\alpha \bmod I^n$. Note that for each $n$ there are only finitely many $\alpha$ such that the elements $x_{n, \alpha}$ are nonzero. Conversely, given $(y_\alpha) \in \prod_\alpha R$ such that for each $n$ there are only finitely many $\alpha$ such that $y_{\alpha} \bmod I^n$ is nonzero, then this defines an element of the left hand side. Hence we can think of an element of the left hand side as infinite "convergent sums" $\sum_\alpha y_\alpha$ with $y_\alpha \in R$ such that for each $n$ there are only finitely many $y_\alpha$ which are nonzero modulo $I^n$. The displayed map maps this element to the element to $(y_\alpha)$ in the product. In particular the map is injective.

Let $Q$ be a finite $R$-module. We have to show that the map $$Q \otimes_R \left(\bigoplus\nolimits_{\alpha \in A} R\right)^\wedge
\longrightarrow
Q \otimes_R \left(\prod\nolimits_{\alpha \in A} R\right)$$ is injective, see Algebra, Theorem [Commutative algebra (programme binding)](#uncovered-algebra-theorem-universally-exact-criteria). Choose a presentation $R^{\oplus k} \to R^{\oplus m} \to Q \to 0$ and denote $q_1, \ldots, q_m \in Q$ the corresponding generators for $Q$. By Artin-Rees (Algebra, Lemma [The Artin–Rees lemma](#native-algebra-lemma-artin-rees)) there exists a constant $c$ such that $\operatorname{Im}(R^{\oplus k} \to R^{\oplus m}) \cap (I^N)^{\oplus m}
\subset \operatorname{Im}((I^{N - c})^{\oplus k} \to R^{\oplus m})$. Let us contemplate the diagram $$\begin{gathered}\begin{matrix}\bigoplus_{l = 1}^k \left(\bigoplus\nolimits_{\alpha \in A} R\right)^\wedge & \bigoplus_{j = 1}^m \left(\bigoplus\nolimits_{\alpha \in A} R\right)^\wedge & Q \otimes_R \left(\bigoplus\nolimits_{\alpha \in A} R\right)^\wedge & 0 \\ \bigoplus_{l = 1}^k \left(\prod\nolimits_{\alpha \in A} R\right) & \bigoplus_{j = 1}^m \left(\prod\nolimits_{\alpha \in A} R\right) & Q \otimes_R \left(\prod\nolimits_{\alpha \in A} R\right) & 0\end{matrix} \\[6pt] \begin{aligned}\bigoplus_{l = 1}^k \left(\bigoplus\nolimits_{\alpha \in A} R\right)^\wedge & \longrightarrow \bigoplus_{j = 1}^m \left(\bigoplus\nolimits_{\alpha \in A} R\right)^\wedge \\ \bigoplus_{l = 1}^k \left(\bigoplus\nolimits_{\alpha \in A} R\right)^\wedge & \longrightarrow \bigoplus_{l = 1}^k \left(\prod\nolimits_{\alpha \in A} R\right) \\ \bigoplus_{j = 1}^m \left(\bigoplus\nolimits_{\alpha \in A} R\right)^\wedge & \longrightarrow Q \otimes_R \left(\bigoplus\nolimits_{\alpha \in A} R\right)^\wedge \\ \bigoplus_{j = 1}^m \left(\bigoplus\nolimits_{\alpha \in A} R\right)^\wedge & \longrightarrow \bigoplus_{j = 1}^m \left(\prod\nolimits_{\alpha \in A} R\right) \\ Q \otimes_R \left(\bigoplus\nolimits_{\alpha \in A} R\right)^\wedge & \longrightarrow 0 \\ Q \otimes_R \left(\bigoplus\nolimits_{\alpha \in A} R\right)^\wedge & \longrightarrow Q \otimes_R \left(\prod\nolimits_{\alpha \in A} R\right) \\ \bigoplus_{l = 1}^k \left(\prod\nolimits_{\alpha \in A} R\right) & \longrightarrow \bigoplus_{j = 1}^m \left(\prod\nolimits_{\alpha \in A} R\right) \\ \bigoplus_{j = 1}^m \left(\prod\nolimits_{\alpha \in A} R\right) & \longrightarrow Q \otimes_R \left(\prod\nolimits_{\alpha \in A} R\right) \\ Q \otimes_R \left(\prod\nolimits_{\alpha \in A} R\right) & \longrightarrow 0\end{aligned}\end{gathered}$$ with exact rows. Pick an element $\sum_j \sum_\alpha y_{j, \alpha}$ of $\bigoplus_{j = 1, \ldots, m}
\left(\bigoplus\nolimits_{\alpha \in A} R\right)^\wedge$. If this element maps to zero in the module $Q \otimes_R \left(\prod\nolimits_{\alpha \in A} R\right)$, then we see in particular that $\sum_j q_j \otimes y_{j, \alpha} = 0$ in $Q$ for each $\alpha$. Thus we can find an element $(z_{1, \alpha}, \ldots, z_{k, \alpha}) \in \bigoplus_{l = 1, \ldots, k} R$ which maps to $(y_{1, \alpha}, \ldots, y_{m, \alpha}) \in \bigoplus_{j = 1, \ldots, m} R$. Moreover, if $y_{j, \alpha} \in I^{N_\alpha}$ for $j = 1, \ldots, m$, then we may assume that $z_{l, \alpha} \in I^{N_\alpha - c}$ for $l = 1, \ldots, k$. Hence the sum $\sum_l \sum_\alpha z_{l, \alpha}$ is "convergent" and defines an element of $\bigoplus_{l = 1, \ldots, k}
\left(\bigoplus\nolimits_{\alpha \in A} R\right)^\wedge$ which maps to the element $\sum_j \sum_\alpha y_{j, \alpha}$ we started out with. Thus the right vertical arrow is injective and we win. $\square$

#### Lemma. Functoriality of the lifting construction
 Let $\varphi : E \to R$ and $\varphi' : E' \to R$ be $R$-module maps. Let $\psi : E \to E'$ be an $R$-module map such that $\varphi' \circ \psi = \varphi$. Then $\psi$ induces a homomorphism of differential graded algebras $K_\bullet(\varphi) \to K_\bullet(\varphi')$.

**Proof.** This is immediate from the definitions. $\square$

#### Lemma. Koszul complexes and regular sequences

Let $R$ be a ring. Let $f_1, \ldots, f_r \in R$ be a sequence. Multiplication by $f_i$ on $K_\bullet(f_\bullet)$ is homotopic to zero, and in particular the cohomology modules $H_i(K_\bullet(f_\bullet))$ are annihilated by the ideal $(f_1, \ldots, f_r)$.

**Proof.** Special case of Lemma [Koszul complexes and regular sequences](#native-more-algebra-lemma-homotopy-koszul-abstract). $\square$

#### Lemma. Koszul complexes, regular sequences and derived categories

Let $R$ be a ring. Let $f_1, \ldots, f_r$, $g_1, \ldots, g_s$ be elements of $R$. Then there is an isomorphism of Koszul complexes $$K_\bullet(R, f_1, \ldots, f_r, g_1, \ldots, g_s) =
\text{Tot}(K_\bullet(R, f_1, \ldots, f_r) \otimes_R
K_\bullet(R, g_1, \ldots, g_s)).$$

**Proof.** Omitted. Hint: If $K_\bullet(R, f_1, \ldots, f_r)$ is generated as a differential graded algebra by $x_1, \ldots, x_r$ with $\text{d}(x_i) = f_i$ and $K_\bullet(R, g_1, \ldots, g_s)$ is generated as a differential graded algebra by $y_1, \ldots, y_s$ with $\text{d}(y_j) = g_j$, then we can think of $K_\bullet(R, f_1, \ldots, f_r, g_1, \ldots, g_s)$ as the differential graded algebra generated by the sequence of elements $x_1, \ldots, x_r, y_1, \ldots, y_s$ with $\text{d}(x_i) = f_i$ and $\text{d}(y_j) = g_j$. $\square$

#### Definition. The Koszul complex

Let $R$ be a ring. Let $\varphi : E \to R$ be an $R$-module map. The *Koszul complex* $K_\bullet(\varphi)$ associated to $\varphi$ is the commutative differential graded algebra defined as follows:

1.  the underlying graded algebra is the exterior algebra $K_\bullet(\varphi) = \wedge(E)$,

2.  the differential $d : K_\bullet(\varphi) \to K_\bullet(\varphi)$ is the unique derivation such that $d(e) = \varphi(e)$ for all $e \in E = K_1(\varphi)$.

#### Lemma. Koszul complexes, regular sequences and derived categories

Let $R$ be a ring. Let $f_1, \ldots, f_r$ be a sequence of elements of $R$. The complex $K_\bullet(f_1, \ldots, f_r)$ is isomorphic to the cone of the map of complexes $$f_r :
K_\bullet(f_1, \ldots, f_{r - 1})
\longrightarrow
K_\bullet(f_1, \ldots, f_{r - 1}).$$

**Proof.** Special case of Lemma [Koszul complexes, regular sequences and derived categories](#native-more-algebra-lemma-cone-koszul-abstract). $\square$

#### Lemma. Koszul complexes, regular sequences and regular rings

Let $f_1, \ldots, f_{r - 1} \in R$ be a sequence and $f, g \in R$. Let $M$ be an $R$-module.

1.  If $f_1, \ldots, f_{r - 1}, f$ and $f_1, \ldots, f_{r - 1}, g$ are $M$-$H_1$-regular then $f_1, \ldots, f_{r - 1}, fg$ is $M$-$H_1$-regular too.

2.  If $f_1, \ldots, f_{r - 1}, f$ and $f_1, \ldots, f_{r - 1}, g$ are $M$-Koszul-regular then $f_1, \ldots, f_{r - 1}, fg$ is $M$-Koszul-regular too.

**Proof.** By Lemma [Koszul complexes and regular sequences](#native-more-algebra-lemma-koszul-mult) we have exact sequences $$H_i(K_\bullet(f_1, \ldots, f_{r - 1}, f) \otimes M) \to
H_i(K_\bullet(f_1, \ldots, f_{r - 1}, fg) \otimes M) \to
H_i(K_\bullet(f_1, \ldots, f_{r - 1}, g) \otimes M)$$ for all $i$. $\square$

#### Lemma. Base change for Koszul complexes, regular sequences and flatness
 Let $\varphi : R \to S$ be a flat ring map. Let $f_1, \ldots, f_r \in R$. Let $M$ be an $R$-module and set $N = M \otimes_R S$.

1.  If $f_1, \ldots, f_r$ in $R$ is an $M$-$H_1$-regular sequence, then $\varphi(f_1), \ldots, \varphi(f_r)$ is an $N$-$H_1$-regular sequence in $S$.

2.  If $f_1, \ldots, f_r$ is an $M$-Koszul-regular sequence in $R$, then $\varphi(f_1), \ldots, \varphi(f_r)$ is an $N$-Koszul-regular sequence in $S$.

**Proof.** This is true because $K_\bullet(f_1, \ldots, f_r) \otimes_R S =
K_\bullet(\varphi(f_1), \ldots, \varphi(f_r))$ and therefore $(K_\bullet(f_1, \ldots, f_r) \otimes_R M) \otimes_R S =
K_\bullet(\varphi(f_1), \ldots, \varphi(f_r)) \otimes_S N$. $\square$

#### Lemma. Changing a basis of a finite free complex

Let $f_1, \ldots, f_r \in R$ be a sequence. Let $(x_{ij})$ be an invertible $r \times r$-matrix with coefficients in $R$. Then the complexes $K_\bullet(f_\bullet)$ and $$K_\bullet(\sum x_{1j}f_j, \sum x_{2j}f_j, \ldots, \sum x_{rj}f_j)$$ are isomorphic.

**Proof.** Set $g_i = \sum x_{ij}f_j$. The matrix $(x_{ji})$ gives an isomorphism $x : R^{\oplus r} \to R^{\oplus r}$ such that $(g_1, \ldots, g_r) = (f_1, \ldots, f_r) \circ x$. Hence this follows from the functoriality of the Koszul complex described in Lemma [Functoriality of the lifting construction](#native-more-algebra-lemma-functorial). $\square$

#### Lemma. Intersections of subfields

Let $K$ be a field of characteristic $p$. Let $\{K_\alpha\}_{\alpha \in A}$ be a collection of subfields of $K$ with the following properties

1.  $K^p \subset K_\alpha$ for all $\alpha \in A$,

2.  $K^p = \bigcap_{\alpha \in A} K_\alpha$,

3.  for $\alpha, \alpha' \in A$ there exists an $\alpha'' \in A$ such that $K_{\alpha''} \subset K_\alpha \cap K_{\alpha'}$.

Then

1.  the intersection of the kernels of the maps $\Omega_{K/\mathbf{F}_p} \to \Omega_{K/K_\alpha}$ is zero,

2.  for any finite extension $L/K$ we have $L^p = \bigcap_{\alpha \in A} L^pK_\alpha$.

**Proof.** Proof of (1). Choose a $p$-basis $\{x_i\}$ for $K$ over $\mathbf{F}_p$. Suppose that $\eta = \sum_{i \in I'} y_i \text{d}x_i$ maps to zero in $\Omega_{K/K_\alpha}$ for every $\alpha \in A$. Here the index set $I'$ is finite. By Lemma [A p-basis in positive characteristic](#native-more-algebra-lemma-p-basis) this means that for every $\alpha$ there exists a relation $$\sum\nolimits_E a_{E, \alpha} x^E = 0,\quad a_{E, \alpha} \in K_\alpha$$ where $E$ runs over multi-indices $E = (e_i)_{i \in I'}$ with $0 \leq e_i < p$. On the other hand, Lemma [A p-basis in positive characteristic](#native-more-algebra-lemma-p-basis) guarantees there is no such relation $\sum a_E x^E = 0$ with $a_E \in K^p$. This is a contradiction by Lemma [Field extensions](#native-more-algebra-lemma-intersection-subfields-subspace).

Proof of (2). Suppose that we have a tower $L/M/K$ of finite extensions of fields. Set $M_\alpha = M^p K_\alpha$ and $L_\alpha = L^p K_\alpha = L^p M_\alpha$. Then we can first prove that $M^p = \bigcap_{\alpha \in A} M_\alpha$, and after that prove that $L^p = \bigcap_{\alpha \in A} L_\alpha$. Hence it suffices to prove (2) for primitive field extensions having no nontrivial subfields. First, assume that $L = K(\theta)$ is separable over $K$. Then $L$ is generated by $\theta^p$ over $K$, hence we may assume that $\theta \in L^p$. In this case we see that $$L^p = K^p \oplus K^p\theta \oplus \ldots K^p\theta^{d - 1}
\quad\text{and}\quad
L^pK_\alpha =
K_\alpha \oplus K_\alpha \theta \oplus \ldots K_\alpha\theta^{d - 1}$$ where $d = [L : K]$. Thus the conclusion is clear in this case. The other case is where $L = K(\theta)$ with $\theta^p = t \in K$, $t \not \in K^p$. In this case we have $$L^p = K^p \oplus K^pt \oplus \ldots K^pt^{p - 1}
\quad\text{and}\quad
L^pK_\alpha =
K_\alpha \oplus K_\alpha t \oplus \ldots K_\alpha t^{p - 1}$$ Again the result is clear. $\square$

#### Theorem. Regular maps and formal smoothness
 Let $k$ be a field. Let $(A, \mathfrak m, K)$ be a Noetherian local $k$-algebra. If the characteristic of $k$ is zero then the following are equivalent

1.  $A$ is a regular local ring, and

2.  $k \to A$ is formally smooth in the $\mathfrak m$-adic topology.

If the characteristic of $k$ is $p > 0$ then the following are equivalent

1.  $A$ is geometrically regular over $k$,

2.  $k \to A$ is formally smooth in the $\mathfrak m$-adic topology.

3.  for all $k \subset k' \subset k^{1/p}$ finite over $k$ the ring $A \otimes_k k'$ is regular,

4.  $A$ is regular and the canonical map $H_1(L_{K/k}) \to \mathfrak m/\mathfrak m^2$ is injective, and

5.  $A$ is regular and the map $\Omega_{k/\mathbf{F}_p} \otimes_k K \to \Omega_{A/\mathbf{F}_p} \otimes_A K$ is injective.

**Proof.** If the characteristic of $k$ is zero, then the equivalence of (1) and (2) follows from Lemmas [Formal smoothness implies regularity](#native-more-algebra-lemma-fs-implies-regular) and [Regularity implies formal smoothness](#native-more-algebra-lemma-regular-implies-fs).

If the characteristic of $k$ is $p > 0$, then it follows from Proposition [Characterizations of geometric regularity](#native-more-algebra-proposition-characterization-geometrically-regular) that (1), (3), (4), and (5) are equivalent. Assume (2) holds. By Lemma [Base change of formal smoothness](#native-more-algebra-lemma-base-change-fs) we see that $k' \to A' = A \otimes_k k'$ is formally smooth for the $\mathfrak m' = \mathfrak mA'$-adic topology. Hence if $k \subset k'$ is finite purely inseparable, then $A'$ is a regular local ring by Lemma [Formal smoothness implies regularity](#native-more-algebra-lemma-fs-implies-regular). Thus we see that (1) holds.

Finally, we will prove that (5) implies (2). Choose a solid diagram $$\begin{gathered}\begin{matrix}A & B/J \\ k & B\end{matrix} \\[6pt] \begin{aligned}A & \xrightarrow{\bar\psi} B/J \\ A & \dashrightarrow B \\ k & \xrightarrow{i} A \\ k & \xrightarrow{\varphi} B \\ B & \xrightarrow{\pi} B/J\end{aligned}\end{gathered}$$ as in Definition [Formally smooth ring maps](#native-more-algebra-definition-formally-smooth). As $J^2 = 0$ we see that $J$ has a canonical $B/J$ module structure and via $\bar\psi$ an $A$-module structure. As $\bar\psi$ is continuous for the $\mathfrak m$-adic topology we see that $\mathfrak m^nJ = 0$ for some $n$. Hence we can filter $J$ by $B/J$-submodules $0 \subset J_1 \subset J_2 \subset \ldots \subset J_n = J$ such that each quotient $J_{t + 1}/J_t$ is annihilated by $\mathfrak m$. Considering the sequence of ring maps $B \to B/J_1 \to B/J_2 \to \ldots \to B/J$ we see that it suffices to prove the existence of the dotted arrow when $J$ is annihilated by $\mathfrak m$, i.e., when $J$ is a $K$-vector space.

Assume given a diagram as above such that $J$ is annihilated by $\mathfrak m$. By Lemma [Regularity implies formal smoothness](#native-more-algebra-lemma-regular-implies-fs) we see that $\mathbf{F}_p \to A$ is formally smooth in the $\mathfrak m$-adic topology. Hence we can find a ring map $\psi : A \to B$ such that $\pi \circ \psi = \bar \psi$. Then $\psi \circ i, \varphi : k \to B$ are two maps whose compositions with $\pi$ are equal. Hence $D = \psi \circ i - \varphi : k \to J$ is a derivation. By Algebra, Lemma [The universal property of Kähler differentials](#native-algebra-lemma-universal-omega) we can write $D = \xi \circ \text{d}$ for some $k$-linear map $\xi : \Omega_{k/\mathbf{F}_p} \to J$. Using the $K$-vector space structure on $J$ we extend $\xi$ to a $K$-linear map $\xi' : \Omega_{k/\mathbf{F}_p} \otimes_k K \to J$. Using (5) we can find a $K$-linear map $\xi'' : \Omega_{A/\mathbf{F}_p} \otimes_A K$ whose restriction to $\Omega_{k/\mathbf{F}_p} \otimes_k K$ is $\xi'$. Write $$D' : A \xrightarrow{\text{d}} \Omega_{A/\mathbf{F}_p}
\to \Omega_{A/\mathbf{F}_p} \otimes_A K \xrightarrow{\xi''} J.$$ Finally, set $\psi' = \psi - D' : A \to B$. The reader verifies that $\psi'$ is a ring map such that $\pi \circ \psi' = \bar \psi$ and such that $\psi' \circ i = \varphi$ as desired. $\square$

#### Lemma. Formal smoothness and flatness
 Let $A \to B$ be a local homomorphism of Noetherian local rings. Assume $A \to B$ is formally smooth in the $\mathfrak m_B$-adic topology. Then $A \to B$ is flat.

**Proof.** We may assume that $A$ and $B$ a Noetherian complete local rings by Lemma [Formal smoothness and completion](#native-more-algebra-lemma-formally-smooth-completion) and Algebra, Lemma [Complete rings, formal power series and Noetherian rings (programme binding)](#uncovered-algebra-lemma-completion-noetherian-noetherian) (this also uses Algebra, Lemma [Descent of flatness](#native-algebra-lemma-flatness-descends-more-general) and Completion, Theorems 3.1–3.3, 4.1 and 5.1 to see that flatness of the map on completions implies flatness of $A \to B$). Choose a commutative diagram $$\begin{gathered}\begin{matrix}S & B \\ R & A\end{matrix} \\[6pt] \begin{aligned}S & \longrightarrow B \\ R & \longrightarrow S \\ R & \longrightarrow A \\ A & \longrightarrow B\end{aligned}\end{gathered}$$ as in Lemma [Complete rings, formal power series and Noetherian rings](#native-more-algebra-lemma-embed-map-noetherian-complete-local-rings) with $R \to S$ flat. Let $I \subset R$ be the kernel of $R \to A$. Because $B$ is formally smooth over $A$ we see that the $A$-algebra map $$S/IS \longrightarrow B$$ has a section, see Lemma [Lifting derived commutative algebra](#native-more-algebra-lemma-lift-continuous). Hence $B$ is a direct summand of the flat $A$-module $S/IS$ (by base change of flatness, see Algebra, Lemma [Base change of flat modules](#native-algebra-lemma-flat-base-change)), whence flat. $\square$

#### Lemma. Complete rings, formal power series and Noetherian rings

Let $A \to B$ be a local homomorphism of Noetherian complete local rings. Then there exists a commutative diagram $$\begin{gathered}\begin{matrix}S & B \\ R & A\end{matrix} \\[6pt] \begin{aligned}S & \longrightarrow B \\ R & \longrightarrow S \\ R & \longrightarrow A \\ A & \longrightarrow B\end{aligned}\end{gathered}$$ with the following properties:

1.  the horizontal arrows are surjective,

2.  if the characteristic of $A/\mathfrak m_A$ is zero, then $S$ and $R$ are power series rings over fields,

3.  if the characteristic of $A/\mathfrak m_A$ is $p > 0$, then $S$ and $R$ are power series rings over Cohen rings, and

4.  $R \to S$ maps a regular system of parameters of $R$ to part of a regular system of parameters of $S$.

In particular $R \to S$ is flat (see Algebra, Lemma [Flatness over a regular local ring](#native-algebra-lemma-flat-over-regular)) with regular fibre $S/\mathfrak m_R S$ (see Algebra, Lemma [Regular rings are Cohen–Macaulay](#native-algebra-lemma-regular-ring-cm)).

**Proof.** Use the Cohen structure theorem (Algebra, Theorem [Commutative algebra (programme binding)](#uncovered-algebra-theorem-cohen-structure-theorem)) to choose a surjection $S \to B$ as in the statement of the lemma where we choose $S$ to be a power series over a Cohen ring if the residue characteristic is $p > 0$ and a power series over a field else. Let $J \subset S$ be the kernel of $S \to B$. Next, choose a surjection $R = \Lambda[[x_1, \ldots, x_n]] \to A$ where we choose $\Lambda$ to be a Cohen ring if the residue characteristic of $A$ is $p > 0$ and $\Lambda$ equal to the residue field of $A$ otherwise. We lift the composition $\Lambda[[x_1, \ldots, x_n]] \to A \to B$ to a map $\varphi : R \to S$. This is possible because $\Lambda[[x_1, \ldots, x_n]]$ is formally smooth over $\mathbf{Z}$ in the $\mathfrak m$-adic topology (see Lemma [Formal smoothness and complete rings and formal power series](#native-more-algebra-lemma-power-series-ring-over-cohen-fs)) by an application of Lemma [Lifting derived commutative algebra](#native-more-algebra-lemma-lift-continuous). Finally, we replace $\varphi$ by the map $\varphi' : R = \Lambda[[x_1, \ldots, x_n]] \to S' = S[[y_1, \ldots, y_n]]$ with $\varphi'|_\Lambda = \varphi|_\Lambda$ and $\varphi'(x_i) = \varphi(x_i) + y_i$. We also replace $S \to B$ by the map $S' \to B$ which maps $y_i$ to zero. After this replacement it is clear that a regular system of parameters of $R$ maps to part of a regular sequence in $S'$ and we win. $\square$

#### Lemma. Complete rings and formal power series

Let $K$ be a field and $A = K[[x_1, \ldots, x_n]]$. Let $\Lambda$ be a Cohen ring and let $B = \Lambda[[x_1, \ldots, x_n]]$.

1.  If $y_1, \ldots, y_n \in A$ is a regular system of parameters then $K[[y_1, \ldots, y_n]] \to A$ is an isomorphism.

2.  If $z_1, \ldots, z_r \in A$ form part of a regular system of parameters for $A$, then $r \leq n$ and $A/(z_1, \ldots, z_r) \cong K[[y_1, \ldots, y_{n - r}]]$.

3.  If $p, y_1, \ldots, y_n \in B$ is a regular system of parameters then $\Lambda[[y_1, \ldots, y_n]] \to B$ is an isomorphism.

4.  If $p, z_1, \ldots, z_r \in B$ form part of a regular system of parameters for $B$, then $r \leq n$ and $B/(z_1, \ldots, z_r) \cong \Lambda[[y_1, \ldots, y_{n - r}]]$.

**Proof.** Proof of (1). Set $A' = K[[y_1, \ldots, y_n]]$. It is clear that the map $A' \to A$ induces an isomorphism $A'/\mathfrak m_{A'}^n \to A/\mathfrak m_A^n$ for all $n \geq 1$. Since $A$ and $A'$ are both complete we deduce that $A' \to A$ is an isomorphism. Proof of (2). Extend $z_1, \ldots, z_r$ to a regular system of parameters $z_1, \ldots, z_r, y_1, \ldots, y_{n - r}$ of $A$. Consider the map $A' = K[[z_1, \ldots, z_r, y_1, \ldots, y_{n - r}]] \to A$. This is an isomorphism by (1). Hence (2) follows as it is clear that $A'/(z_1, \ldots, z_r) \cong K[[y_1, \ldots, y_{n - r}]]$. The proofs of (3) and (4) are exactly the same as the proofs of (1) and (2). $\square$

#### Lemma. Formal smoothness and complete rings and formal power series
 Let $K$ be a field of characteristic $0$ and $A = K[[x_1, \ldots, x_n]]$. Let $L$ be a field of characteristic $p > 0$ and $B = L[[x_1, \ldots, x_n]]$. Let $\Lambda$ be a Cohen ring. Let $C = \Lambda[[x_1, \ldots, x_n]]$.

1.  $\mathbf{Q} \to A$ is formally smooth in the $\mathfrak m_A$-adic topology.

2.  $\mathbf{F}_p \to B$ is formally smooth in the $\mathfrak m_B$-adic topology.

3.  $\mathbf{Z} \to C$ is formally smooth in the $\mathfrak m_C$-adic topology.

**Proof.** By the universal property of power series rings it suffices to prove:

1.  $\mathbf{Q} \to K$ is formally smooth.

2.  $\mathbf{F}_p \to L$ is formally smooth.

3.  $\mathbf{Z} \to \Lambda$ is formally smooth in the $\mathfrak m_\Lambda$-adic topology.

The first two are Algebra, Proposition [Characterizations of separable field extensions](#native-algebra-proposition-characterize-separable-field-extensions). The third follows from Algebra, Lemma [Formal smoothness and smooth morphisms (programme binding)](#uncovered-algebra-lemma-cohen-ring-formally-smooth) since for any test diagram as in Definition [Formally smooth ring maps](#native-more-algebra-definition-formally-smooth) some power of $p$ will be zero in $A/J$ and hence some power of $p$ will be zero in $A$. $\square$

#### Lemma. Lifting formal smoothness
 Let $A$ be a Noetherian complete local ring with residue field $k$. Let $B$ be a Noetherian complete local $k$-algebra. Assume $k \to B$ is formally smooth in the $\mathfrak m_B$-adic topology. Then there exists a Noetherian complete local ring $C$ and a local homomorphism $A \to C$ which is formally smooth in the $\mathfrak m_C$-adic topology such that $C \otimes_A k \cong B$.

**Proof.** Choose a diagram $$\begin{gathered}\begin{matrix}S & B \\ R & A\end{matrix} \\[6pt] \begin{aligned}S & \longrightarrow B \\ R & \longrightarrow S \\ R & \longrightarrow A \\ A & \longrightarrow B\end{aligned}\end{gathered}$$ as in Lemma [Complete rings, formal power series and Noetherian rings](#native-more-algebra-lemma-embed-map-noetherian-complete-local-rings). Let $t_1, \ldots, t_d$ be a regular system of parameters for $R$ with $t_1 = p$ in case the characteristic of $k$ is $p > 0$. As $B$ and $\overline{S} = S \otimes_R k$ are regular we see that $\operatorname{Ker}(\overline{S} \to B)$ is generated by elements $\overline{x}_1, \ldots, \overline{x}_r$ which form part of a regular system of parameters of $\overline{S}$, see Algebra, Lemma [Regular rings](#native-algebra-lemma-regular-quotient-regular). Lift these elements to $x_1, \ldots, x_r \in S$. Then $t_1, \ldots, t_d, x_1, \ldots, x_r$ is part of a regular system of parameters for $S$. Hence $S/(x_1, \ldots, x_r)$ is a power series ring over a field (if the characteristic of $k$ is zero) or a power series ring over a Cohen ring (if the characteristic of $k$ is $p > 0$), see Lemma [Complete rings and formal power series](#native-more-algebra-lemma-quotient-power-series-ring-over-cohen). Moreover, it is still the case that $R \to S/(x_1, \ldots, x_r)$ maps $t_1, \ldots, t_d$ to a part of a regular system of parameters of $S/(x_1, \ldots, x_r)$. In other words, we may replace $S$ by $S/(x_1, \ldots, x_r)$ and assume we have a diagram $$\begin{gathered}\begin{matrix}S & B \\ R & A\end{matrix} \\[6pt] \begin{aligned}S & \longrightarrow B \\ R & \longrightarrow S \\ R & \longrightarrow A \\ A & \longrightarrow B\end{aligned}\end{gathered}$$ as in Lemma [Complete rings, formal power series and Noetherian rings](#native-more-algebra-lemma-embed-map-noetherian-complete-local-rings) with moreover $\overline{S} = B$. In this case $R \to S$ is formally smooth in the $\mathfrak m_S$-adic topology by Proposition [Formal smoothness from flatness and formally smooth fibres](#native-more-algebra-proposition-fs-flat-fibre-fs). Hence the base change $C = S \otimes_R A$ is formally smooth over $A$ in the $\mathfrak m_C$-adic topology by Lemma [Base change of formal smoothness](#native-more-algebra-lemma-base-change-fs). $\square$

#### Lemma. Lifting derived commutative algebra

Let $R \to S$ be a ring map. Let $\mathfrak n$ be an ideal of $S$. Assume that $R \to S$ is formally smooth in the $\mathfrak n$-adic topology. Consider a solid commutative diagram $$\begin{gathered}\begin{matrix}S & A/J \\ R & A\end{matrix} \\[6pt] \begin{aligned}S & \xrightarrow{\psi} A/J \\ S & \dashrightarrow A \\ R & \longrightarrow A \\ R & \longrightarrow S \\ A & \longrightarrow A/J\end{aligned}\end{gathered}$$ of homomorphisms of topological rings where $A$ is adic and $A/J$ is the quotient (as topological ring) of $A$ by a closed ideal $J \subset A$ such that $J^t$ is contained in an ideal of definition of $A$ for some $t \geq 1$. Then there exists a dotted arrow in the category of topological rings which makes the diagram commute.

**Proof.** Let $I \subset A$ be an ideal of definition so that $I \supset J^t$ for some $t$. Then $A = \varprojlim A/I^n$ and $A/J = \varprojlim A/J + I^n$ because $J$ is assumed closed. Consider the following diagram of discrete $R$ algebras $A_{n, m} = A/J^n + I^m$: $$\begin{gathered}\begin{matrix}A/J^3 + I^3 & A/J^2 + I^3 & A/J + I^3 \\ A/J^3 + I^2 & A/J^2 + I^2 & A/J + I^2 \\ A/J^3 + I & A/J^2 + I & A/J + I\end{matrix} \\[6pt] \begin{aligned}A/J^3 + I^3 & \longrightarrow A/J^2 + I^3 \\ A/J^3 + I^3 & \longrightarrow A/J^3 + I^2 \\ A/J^2 + I^3 & \longrightarrow A/J + I^3 \\ A/J^2 + I^3 & \longrightarrow A/J^2 + I^2 \\ A/J + I^3 & \longrightarrow A/J + I^2 \\ A/J^3 + I^2 & \longrightarrow A/J^2 + I^2 \\ A/J^3 + I^2 & \longrightarrow A/J^3 + I \\ A/J^2 + I^2 & \longrightarrow A/J + I^2 \\ A/J^2 + I^2 & \longrightarrow A/J^2 + I \\ A/J + I^2 & \longrightarrow A/J + I \\ A/J^3 + I & \longrightarrow A/J^2 + I \\ A/J^2 + I & \longrightarrow A/J + I\end{aligned}\end{gathered}$$ Note that each of the commutative squares defines a surjection $$A_{n + 1, m + 1} \longrightarrow A_{n + 1, m} \times_{A_{n, m}} A_{n, m + 1}$$ of $R$-algebras whose kernel has square zero. We will inductively construct $R$-algebra maps $\varphi_{n, m} : S \to A_{n, m}$. Namely, we have the maps $\varphi_{1, m} = \psi \bmod J + I^m$. Note that each of these maps is continuous as $\psi$ is. We can inductively choose the maps $\varphi_{n, 1}$ by starting with our choice of $\varphi_{1, 1}$ and lifting up, using the formal smoothness of $S$ over $R$, along the bottom row of the diagram above. We construct the remaining maps $\varphi_{n, m}$ by induction on $n + m$. Namely, we choose $\varphi_{n + 1, m + 1}$ by lifting the pair $(\varphi_{n + 1, m}, \varphi_{n, m + 1})$ along the displayed surjection above (again using the formal smoothness of $S$ over $R$). In this way all of the maps $\varphi_{n, m}$ are compatible with the transition maps of the system. As $J^t \subset I$ we see that for example $\varphi_n = \varphi_{nt, n} \bmod I^n$ induces a map $S \to A/I^n$. Taking the limit $\varphi = \varprojlim \varphi_n$ we obtain a map $S \to A = \varprojlim A/I^n$. The composition into $A/J$ agrees with $\psi$ as we have seen that $A/J = \varprojlim A/J + I^n$. Finally we show that $\varphi$ is continuous. Namely, we know that $\psi(\mathfrak n^r) \subset J + I/J$ for some $r \geq 1$ by our assumption that $\psi$ is a morphism of topological rings, see Lemma [Derived commutative algebra](#native-more-algebra-lemma-continuous). Hence $\varphi(\mathfrak n^r) \subset J + I$ hence $\varphi(\mathfrak n^{rt}) \subset I$ as desired. $\square$

#### Lemma. Koszul complexes and regular sequences
 Let $R$ be a ring. Let $\varphi : E \to R$ be an $R$-module map. Let $e \in E$ with image $f = \varphi(e)$ in $R$. Then $$f = de + ed$$ as endomorphisms of $K_\bullet(\varphi)$.

**Proof.** This is true because $d(ea) = d(e)a - ed(a) = fa - ed(a)$. $\square$

#### Lemma. Koszul complexes, regular sequences and derived categories

Let $R$ be a ring. Let $\varphi : E \to R$ be an $R$-module map. Let $f \in R$. Set $E' = E \oplus R$ and define $\varphi' : E' \to R$ by $\varphi$ on $E$ and multiplication by $f$ on $R$. The complex $K_\bullet(\varphi')$ is isomorphic to the cone of the map of complexes $$f :
K_\bullet(\varphi)
\longrightarrow
K_\bullet(\varphi).$$

**Proof.** Denote $e_0 \in E'$ the element $1 \in R \subset R \oplus E$. By our definition of the cone above we see that $$C(f)_n = K_n(\varphi) \oplus K_{n - 1}(\varphi) =
\wedge^n(E) \oplus \wedge^{n - 1}(E) = \wedge^n(E')$$ where in the last $=$ we map $(0, e_1 \wedge \ldots \wedge e_{n - 1})$ to $e_0 \wedge e_1 \wedge \ldots \wedge e_{n - 1}$ in $\wedge^n(E')$. A computation shows that this isomorphism is compatible with differentials. Namely, this is clear for elements of the first summand as $\varphi'|_E = \varphi$ and $d_{C(f)}$ restricted to the first summand is just $d_{K_\bullet(\varphi)}$. On the other hand, if $e_1 \wedge \ldots \wedge e_{n - 1}$ is in the second summand, then $$d_{C(f)}(0, e_1 \wedge \ldots \wedge e_{n - 1}) =
fe_1 \wedge \ldots \wedge e_{n - 1}
- d_{K_\bullet(\varphi)}(e_1 \wedge \ldots \wedge e_{n - 1})$$ and on the other hand $$\begin{aligned}
& d_{K_\bullet(\varphi')}(0, e_0 \wedge e_1 \wedge \ldots \wedge e_{n - 1}) \\
& =
\sum\nolimits_{i = 0, \ldots, n - 1}
(-1)^i \varphi'(e_i)e_0 \wedge \ldots \wedge \widehat{e_i}
\wedge \ldots \wedge e_{n - 1} \\
& =
fe_1 \wedge \ldots \wedge e_{n - 1} +
\sum\nolimits_{i = 1, \ldots, n - 1}
(-1)^i \varphi(e_i)e_0 \wedge \ldots \wedge \widehat{e_i}
\wedge \ldots \wedge e_{n - 1} \\
& =
fe_1 \wedge \ldots \wedge e_{n - 1} -
e_0 \left(\sum\nolimits_{i = 1, \ldots, n - 1}
(-1)^{i + 1} \varphi(e_i)e_1 \wedge \ldots \wedge \widehat{e_i}
\wedge \ldots \wedge e_{n - 1}\right)
\end{aligned}$$ which is the image of the result of the previous computation. $\square$

#### Lemma. Koszul complexes and regular sequences

Let $R$ be a ring. Let $f_1, \ldots, f_{r - 1}$ be a sequence of elements of $R$. Let $f, g \in R$. The complex $K_\bullet(f_1, \ldots, f_{r - 1}, fg)$ is homotopy equivalent to the cone of a map of complexes $$K_\bullet(f_1, \ldots, f_{r - 1}, f)[1]
\longrightarrow
K_\bullet(f_1, \ldots, f_{r - 1}, g)$$

**Proof.** Special case of Lemma [Koszul complexes and regular sequences](#native-more-algebra-lemma-koszul-mult-abstract). $\square$

#### Lemma. A p-basis in positive characteristic

Let $K/k$ be a field extension. Assume $k$ has characteristic $p > 0$. Let $\{x_i\}$ be a subset of $K$. The following are equivalent

1.  the elements $\{x_i\}$ are $p$-independent over $k$, and

2.  the elements $\text{d}x_i$ are $K$-linearly independent in $\Omega_{K/k}$.

Any $p$-independent collection can be extended to a $p$-basis of $K$ over $k$. In particular, the field $K$ has a $p$-basis over $k$. Moreover, the following are equivalent:

1.  $\{x_i\}$ is a $p$-basis of $K$ over $k$, and

2.  $\text{d}x_i$ is a basis of the $K$-vector space $\Omega_{K/k}$.

**Proof.** Assume (2) and suppose that $\sum a_E x^E = 0$ is a linear relation with $a_E \in k K^p$. Let $\theta_i : K \to K$ be a $k$-derivation such that $\theta_i(x_j) = \delta_{ij}$ (Kronecker delta). Note that any $k$-derivation of $K$ annihilates $kK^p$. Applying $\theta_i$ to the given relation we obtain new relations $$\sum\nolimits_{E, e_i > 0}
e_i a_E x_1^{e_1}\ldots x_i^{e_i - 1} \ldots x_n^{e_n} = 0$$ Hence if we pick $\sum a_E x^E$ as the relation with minimal total degree $|E| = \sum e_i$ for some $a_E \not = 0$, then we get a contradiction. Hence (1) holds.

If $\{x_i\}$ is a $p$-basis for $K$ over $k$, then $K \cong kK^p[X_i]/(X_i^p - x_i^p)$. Hence we see that $\text{d}x_i$ forms a basis for $\Omega_{K/k}$ over $K$. Thus (a) implies (b).

Let $\{x_i\}$ be a $p$-independent subset of $K$ over $k$. An application of Zorn's lemma shows that we can enlarge this to a maximal $p$-independent subset of $K$ over $k$. We claim that any maximal $p$-independent subset $\{x_i\}$ of $K$ is a $p$-basis of $K$ over $k$. The claim will imply that (1) implies (2) and establish the existence of $p$-bases. To prove the claim let $L$ be the subfield of $K$ generated by $kK^p$ and the $x_i$. We have to show that $L = K$. If $x \in K$ but $x \not \in L$, then $x^p \in L$ and $L(x) \cong L[z]/(z^p - x^p)$. Hence $\{x_i\} \cup \{x\}$ is $p$-independent over $k$, a contradiction.

Finally, we have to show that (b) implies (a). By the equivalence of (1) and (2) we see that $\{x_i\}$ is a maximal $p$-independent subset of $K$ over $k$. Hence by the claim above it is a $p$-basis. $\square$

#### Lemma. Field extensions

Let $K/k$ be a field extension. Let $\{K_\alpha\}_{\alpha \in A}$ be a collection of subfields of $K$ with the following properties

1.  $k \subset K_\alpha$ for all $\alpha \in A$,

2.  $k = \bigcap_{\alpha \in A} K_\alpha$,

3.  for $\alpha, \alpha' \in A$ there exists an $\alpha'' \in A$ such that $K_{\alpha''} \subset K_\alpha \cap K_{\alpha'}$.

Then for $n \geq 1$ and $V \subset K^{\oplus n}$ a $K$-vector space we have $V \cap k^{\oplus n} \not = 0$ if and only if $V \cap K_\alpha^{\oplus n} \not = 0$ for all $\alpha \in A$.

**Proof.** By induction on $n$. The case $n = 1$ follows from the assumptions. Assume the result proven for subspaces of $K^{\oplus n - 1}$. Assume that $V \subset K^{\oplus n}$ has nonzero intersection with $K_\alpha^{\oplus n}$ for all $\alpha \in A$. If $V \cap 0 \oplus k^{\oplus n - 1}$ is nonzero then we win. Hence we may assume this is not the case. By induction hypothesis we can find an $\alpha$ such that $V \cap 0 \oplus K_\alpha^{\oplus n - 1}$ is zero. Let $v = (x_1, \ldots, x_n) \in V \cap K_\alpha^{\oplus n}$ be a nonzero element. By our choice of $\alpha$ we see that $x_1$ is not zero. Replace $v$ by $x_1^{-1}v$ so that $v = (1, x_2, \ldots, x_n)$. Note that if $v' = (x_1', \ldots, x'_n) \in V \cap K_\alpha^{\oplus n}$, then $v' - x_1'v = 0$ by our choice of $\alpha$. Hence we see that $V \cap K_\alpha^{\oplus n} = K_\alpha v$. If we choose some $\alpha'$ such that $K_{\alpha'} \subset K_\alpha$, then we see that necessarily $v \in V \cap K_{\alpha'}^{\oplus n}$ (by the same arguments applied to $\alpha'$). Hence $$x_2, \ldots, x_n \in
\bigcap\nolimits_{\alpha' \in A, K_{\alpha'} \subset K_\alpha} K_{\alpha'}$$ which equals $k$ by (2) and (3). $\square$

#### Lemma. Formal smoothness implies regularity
 Let $k$ be a field and let $(A, \mathfrak m, K)$ be a Noetherian local $k$-algebra. If $k \to A$ is formally smooth for the $\mathfrak m$-adic topology, then $A$ is a regular local ring.

**Proof.** Let $k_0 \subset k$ be the prime field. Then $k_0$ is perfect, hence $k / k_0$ is separable, hence formally smooth by Algebra, Lemma [Elementary formally smooth extensions](#native-algebra-lemma-formally-smooth-extensions-easy). By Lemmas [Formal smoothness and smooth morphisms](#native-more-algebra-lemma-formally-smooth) and [Composition of formally smooth maps](#native-algebra-lemma-compose-formally-smooth) we see that $k_0 \to A$ is formally smooth for the $\mathfrak m$-adic topology on $A$. Hence we may assume $k = \mathbf{Q}$ or $k = \mathbf{F}_p$.

By Algebra, Lemmas Completion, Theorems 3.1–3.3, 4.1 and 5.1 and [Flatness and regular ring maps](#native-algebra-lemma-flat-under-regular) it suffices to prove the completion $A^\wedge$ is regular. By Lemma [Formal smoothness and completion](#native-more-algebra-lemma-formally-smooth-completion) we may replace $A$ by $A^\wedge$. Thus we may assume that $A$ is a Noetherian complete local ring. By the Cohen structure theorem (Algebra, Theorem [Commutative algebra (programme binding)](#uncovered-algebra-theorem-cohen-structure-theorem)) there exist a map $K \to A$. As $k$ is the prime field we see that $K \to A$ is a $k$-algebra map.

Let $x_1, \ldots, x_n \in \mathfrak m$ be elements whose images form a basis of $\mathfrak m/\mathfrak m^2$. Set $T = K[[X_1, \ldots, X_n]]$. Note that $$A/\mathfrak m^2 \cong K[x_1, \ldots, x_n]/(x_ix_j)$$ and $$T/\mathfrak m_T^2 \cong K[X_1, \ldots, X_n]/(X_iX_j).$$ Let $A/\mathfrak m^2 \to T/m_T^2$ be the local $K$-algebra isomorphism given by mapping the class of $x_i$ to the class of $X_i$. Denote $f_1 : A \to T/\mathfrak m_T^2$ the composition of this isomorphism with the quotient map $A \to A/\mathfrak m^2$. The assumption that $k \to A$ is formally smooth in the $\mathfrak m$-adic topology means we can lift $f_1$ to a map $f_2 : A \to T/\mathfrak{m}_T^3$, then to a map $f_3 : A \to T/\mathfrak{m}_T^4$, and so on, for all $n \geq 1$. Warning: the maps $f_n$ are continuous $k$-algebra maps and may not be $K$-algebra maps. We get an induced map $f : A \to T = \varprojlim T/\mathfrak m_T^n$ of local $k$-algebras. By our choice of $f_1$, the map $f$ induces an isomorphism $\mathfrak m/\mathfrak m^2 \to \mathfrak m_T/\mathfrak m_T^2$ hence each $f_n$ is surjective and we conclude $f$ is surjective as $A$ is complete. This implies $\dim(A) \geq \dim(T) = n$. Hence $A$ is regular by definition. (It also follows that $f$ is an isomorphism.) $\square$

#### Lemma. Regularity implies formal smoothness
 Let $k$ be a field. Let $(A, \mathfrak m, K)$ be a regular local $k$-algebra such that $K/k$ is separable. Then $k \to A$ is formally smooth in the $\mathfrak m$-adic topology.

**Proof.** It suffices to prove that the completion of $A$ is formally smooth over $k$, see Lemma [Formal smoothness and completion](#native-more-algebra-lemma-formally-smooth-completion). Hence we may assume that $A$ is a complete local regular $k$-algebra with residue field $K$ separable over $k$. By Lemma [Complete rings, formal power series and field extensions](#native-more-algebra-lemma-power-series-over-residue-field) we see that $A = K[[x_1, \ldots, x_n]]$.

The power series ring $K[[x_1, \ldots, x_n]]$ is formally smooth over $k$. Namely, $K$ is formally smooth over $k$ and $K[x_1, \ldots, x_n]$ is formally smooth over $K$ as a polynomial algebra. Hence $K[x_1, \ldots, x_n]$ is formally smooth over $k$ by Algebra, Lemma [Composition of formally smooth maps](#native-algebra-lemma-compose-formally-smooth). It follows that $k \to K[x_1, \ldots, x_n]$ is formally smooth for the $(x_1, \ldots, x_n)$-adic topology by Lemma [Formal smoothness and smooth morphisms](#native-more-algebra-lemma-formally-smooth). Finally, it follows that $k \to K[[x_1, \ldots, x_n]]$ is formally smooth for the $(x_1, \ldots, x_n)$-adic topology by Lemma [Formal smoothness and completion](#native-more-algebra-lemma-formally-smooth-completion). $\square$

#### Lemma. Koszul complexes and regular sequences
 Let $R$ be a ring. Let $\varphi : E \to R$ be an $R$-module map. Let $f, g \in R$. Set $E' = E \oplus R$ and define $\varphi'_f, \varphi'_g, \varphi'_{fg} : E' \to R$ by $\varphi$ on $E$ and multiplication by $f, g, fg$ on $R$. The complex $K_\bullet(\varphi'_{fg})$ is homotopy equivalent to the cone of a map of complexes $$K_\bullet(\varphi'_f)[1]
\longrightarrow
K_\bullet(\varphi'_g).$$

**Proof.** By Lemma [Koszul complexes, regular sequences and derived categories](#native-more-algebra-lemma-cone-koszul-abstract) the complex $K_\bullet(\varphi'_f)$ is isomorphic to the cone of multiplication by $f$ on $K_\bullet(\varphi)$ and similarly for the other two cases. Hence the lemma follows from Lemma [Derived categories](#native-more-algebra-lemma-cone-squared). $\square$

#### Lemma. Complete rings, formal power series and field extensions

Let $k$ be a field. Let $(A, \mathfrak m, \kappa)$ be a complete local $k$-algebra. If $\kappa/k$ is separable and $A$ regular, then there exists an isomorphism of $A \cong \kappa[[t_1, \ldots, t_d]]$ as $k$-algebras.

**Proof.** Choose $\kappa \to A$ as in Lemma [Lifting field extensions](#native-more-algebra-lemma-lift-residue-field) and apply Algebra, Lemma [Complete rings, formal power series and regular rings (programme binding)](#uncovered-algebra-lemma-regular-complete-containing-coefficient-field). $\square$

#### Lemma. Derived categories

Let $R$ be a ring. Let $A_\bullet$ be a complex of $R$-modules. Let $f, g \in R$. Let $C(f)_\bullet$ be the cone of $f : A_\bullet \to A_\bullet$. Define similarly $C(g)_\bullet$ and $C(fg)_\bullet$. Then $C(fg)_\bullet$ is homotopy equivalent to the cone of a map $$C(f)_\bullet[1] \longrightarrow C(g)_\bullet$$

**Proof.** We first prove this if $A_\bullet$ is the complex consisting of $R$ placed in degree $0$. In this case the complex $C(f)_\bullet$ is the complex $$\ldots \to 0 \to R \xrightarrow{f} R \to 0 \to \ldots$$ with $R$ placed in (homological) degrees $1$ and $0$. The map of complexes we use is $$\begin{gathered}\begin{matrix}0 & 0 & R & R & 0 \\ 0 & R & R & 0 & 0\end{matrix} \\[6pt] \begin{aligned}0 & \longrightarrow 0 \\ 0 & \longrightarrow 0 \\ 0 & \longrightarrow R \\ 0 & \longrightarrow R \\ R & \xrightarrow{f} R \\ R & \xrightarrow{1} R \\ R & \longrightarrow 0 \\ R & \longrightarrow 0 \\ 0 & \longrightarrow 0 \\ 0 & \longrightarrow R \\ R & \xrightarrow{g} R \\ R & \longrightarrow 0 \\ 0 & \longrightarrow 0\end{aligned}\end{gathered}$$ The cone of this is the chain complex consisting of $R^{\oplus 2}$ placed in degrees $1$ and $0$ and differential ([Cotangent complexes, differentials and derived categories](#context-more-algebra-equation-differential-cone)) $$\left(
\begin{matrix}
g & 1 \\
0 & -f
\end{matrix}
\right) :
R^{\oplus 2} \longrightarrow R^{\oplus 2}$$ To see this chain complex is homotopic to $C(fg)_\bullet$, i.e., to $R \xrightarrow{fg} R$, consider the maps of complexes $$\begin{gathered}\begin{matrix}R & R \\ R^{\oplus 2} & R^{\oplus 2}\end{matrix} \\[6pt] \begin{aligned}R & \xrightarrow{(1, -g)} R^{\oplus 2} \\ R & \xrightarrow{fg} R \\ R & \xrightarrow{(0, 1)} R^{\oplus 2} \\ R^{\oplus 2} & \longrightarrow R^{\oplus 2}\end{aligned}\end{gathered}
\quad\quad
\begin{gathered}\begin{matrix}R^{\oplus 2} & R^{\oplus 2} \\ R & R\end{matrix} \\[6pt] \begin{aligned}R^{\oplus 2} & \xrightarrow{(1, 0)} R \\ R^{\oplus 2} & \longrightarrow R^{\oplus 2} \\ R^{\oplus 2} & \xrightarrow{(f, 1)} R \\ R & \xrightarrow{fg} R\end{aligned}\end{gathered}$$ with obvious notation. The composition of these two maps in one direction is the identity on $C(fg)_\bullet$, but in the other direction it isn't the identity. We omit writing out the required homotopy.

To see the result holds in general, we use that we have a functor $K_\bullet \mapsto \text{Tot}(A_\bullet \otimes_R K_\bullet)$ on the category of complexes which is compatible with homotopies and cones. Then we write $C(f)_\bullet$ and $C(g)_\bullet$ as the total complex of the double complexes $$(R \xrightarrow{f} R) \otimes_R A_\bullet
\quad\text{and}\quad
(R \xrightarrow{g} R) \otimes_R A_\bullet$$ and in this way we deduce the result from the special case discussed above. Some details omitted. $\square$

#### Lemma. Lifting field extensions
 Let $k$ be a field. Let $(A, \mathfrak m, \kappa)$ be a complete local $k$-algebra. If $\kappa/k$ is separable, then there exists a $k$-algebra map $\kappa \to A$ such that $\kappa \to A \to \kappa$ is $\text{id}_\kappa$.

**Proof.** By Algebra, Proposition [Characterizations of separable field extensions](#native-algebra-proposition-characterize-separable-field-extensions) the extension $\kappa/k$ is formally smooth. By Lemma [Formal smoothness and smooth morphisms](#native-more-algebra-lemma-formally-smooth) $k \to \kappa$ is formally smooth in the sense of Definition [Formally smooth ring maps](#native-more-algebra-definition-formally-smooth). Then we get $\kappa \to A$ from Lemma [Lifting derived commutative algebra](#native-more-algebra-lemma-lift-continuous). $\square$

#### Marked formal deformation groupoids

#### Lemma. Surjectivity on cotangent spaces
 Let $f: R \to S$ be a ring map in $\widehat{\mathcal{C}}_\Lambda$. The following are equivalent

1.  $f$ is surjective,

2.  the map $\mathfrak m_R/\mathfrak m_R^2 \to \mathfrak m_S/\mathfrak m_S^2$ is surjective, and

3.  the map $\mathfrak m_R/(\mathfrak m_\Lambda R + \mathfrak m_R^2) \to
    \mathfrak m_S/(\mathfrak m_\Lambda S + \mathfrak m_S^2)$ is surjective.

**Proof.** Note that for \(n \geq 2\) we have the equality of relative cotangent spaces 

\[
\mathfrak m_R/(\mathfrak m_\Lambda R + \mathfrak m_R^2)
=
\mathfrak m_{R_n}/(\mathfrak m_\Lambda R_n + \mathfrak m_{R_n}^2)
\]

 and similarly for \(S\). Hence by Lemma [Formal deformation groupoids](#native-formal-defos-lemma-surjective) we see that \(R_n \to S_n\) is surjective for all \(n\). Now let \(K_n\) be the kernel of \(R_n \to S_n\). Then the sequences 

\[
0 \to K_n \to R_n \to S_n \to 0
\]

 form an exact sequence of directed inverse systems. The system \((K_n)\) is Mittag-Leffler since each \(K_n\) is Artinian. Hence by Algebra, Lemma [Commutative algebra](#native-algebra-lemma-ml-exact-sequence) taking limits preserves exactness. So \(\varprojlim R_n \to \varprojlim S_n\) is surjective, i.e., \(f\) is surjective. \(\square\)

#### Lemma. Formal deformation groupoids
 Let $A \to B$ be a ring map in $\mathcal{C}_\Lambda$. The following are equivalent

1.  $f$ is surjective,

2.  $\mathfrak m_A/\mathfrak m_A^2 \to \mathfrak m_B/\mathfrak m_B^2$ is surjective, and

3.  $\mathfrak m_A/(\mathfrak m_\Lambda A + \mathfrak m_A^2)
    \to \mathfrak m_B/(\mathfrak m_\Lambda B + \mathfrak m_B^2)$ is surjective.

**Proof.** For any ring map $f : A \to B$ in $\mathcal{C}_\Lambda$ we have $f(\mathfrak m_A) \subset \mathfrak m_B$ for example because $\mathfrak m_A$, $\mathfrak m_B$ is the set of nilpotent elements of $A$, $B$. Suppose $f$ is surjective. Let $y \in \mathfrak m_B$. Choose $x \in A$ with $f(x) = y$. Since $f$ induces an isomorphism $A/\mathfrak m_A \to B/\mathfrak m_B$ we see that $x \in \mathfrak m_A$. Hence the induced map $\mathfrak m_A/\mathfrak m_A^2 \to \mathfrak m_B/\mathfrak m_B^2$ is surjective. In this way we see that (1) implies (2).

It is clear that (2) implies (3). The map $A \to B$ gives rise to a canonical commutative diagram $$\begin{gathered}\begin{matrix}\mathfrak m_\Lambda/\mathfrak m_\Lambda^2 \otimes_{k'} k & \mathfrak m_A/\mathfrak m_A^2 & \mathfrak m_A/(\mathfrak m_\Lambda A + \mathfrak m_A^2) & 0 \\ \mathfrak m_\Lambda/\mathfrak m_\Lambda^2 \otimes_{k'} k & \mathfrak m_B/\mathfrak m_B^2 & \mathfrak m_B/(\mathfrak m_\Lambda B + \mathfrak m_B^2) & 0\end{matrix} \\[6pt] \begin{aligned}\mathfrak m_\Lambda/\mathfrak m_\Lambda^2 \otimes_{k'} k & \longrightarrow \mathfrak m_A/\mathfrak m_A^2 \\ \mathfrak m_\Lambda/\mathfrak m_\Lambda^2 \otimes_{k'} k & \longrightarrow \mathfrak m_\Lambda/\mathfrak m_\Lambda^2 \otimes_{k'} k \\ \mathfrak m_A/\mathfrak m_A^2 & \longrightarrow \mathfrak m_A/(\mathfrak m_\Lambda A + \mathfrak m_A^2) \\ \mathfrak m_A/\mathfrak m_A^2 & \longrightarrow \mathfrak m_B/\mathfrak m_B^2 \\ \mathfrak m_A/(\mathfrak m_\Lambda A + \mathfrak m_A^2) & \longrightarrow 0 \\ \mathfrak m_A/(\mathfrak m_\Lambda A + \mathfrak m_A^2) & \longrightarrow \mathfrak m_B/(\mathfrak m_\Lambda B + \mathfrak m_B^2) \\ \mathfrak m_\Lambda/\mathfrak m_\Lambda^2 \otimes_{k'} k & \longrightarrow \mathfrak m_B/\mathfrak m_B^2 \\ \mathfrak m_B/\mathfrak m_B^2 & \longrightarrow \mathfrak m_B/(\mathfrak m_\Lambda B + \mathfrak m_B^2) \\ \mathfrak m_B/(\mathfrak m_\Lambda B + \mathfrak m_B^2) & \longrightarrow 0\end{aligned}\end{gathered}$$ with exact rows. Hence if (3) holds, then so does (2).

Assume (2). To show that $A \to B$ is surjective it suffices by Nakayama's lemma (Algebra, Lemma [Nakayama's lemma](#native-algebra-lemma-nak)) to show that $A/\mathfrak m_A \to B/\mathfrak m_AB$ is surjective. (Note that $\mathfrak m_A$ is a nilpotent ideal.) As $k = A/\mathfrak m_A = B/\mathfrak m_B$ it suffices to show that $\mathfrak m_AB \to \mathfrak m_B$ is surjective. Applying Nakayama's lemma once more we see that it suffices to see that $\mathfrak m_AB/\mathfrak m_A\mathfrak m_B \to \mathfrak m_B/\mathfrak m_B^2$ is surjective which is what we assumed. $\square$

### Uncovered prerequisites

The following supporting claims have no separately incorporated native proof. Their exact current programme bindings and deductions are stated individually below. Partial and unbound claims remain conditional at their recorded scope. The central desingularization and family-approximation constructions have been supplied; this record does not certify recursive closure of every lower prerequisite.

#### Noetherian topological spaces

**Written provider and explicit deduction.** Native locator: `topology.tex` / `lemma-Noetherian`.

A Noetherian space has Noetherian subspaces and finitely many irreducible components, each containing a nonempty open.

*Spectra of rings* (AG-CA), Theorem4.3 and proof, lines168-174: Arbitrary Noetherian topological spaces.

For a subspace, lift a descending closed chain to ambient closed sets and replace them by their finite successive intersections; ambient stabilization gives subspace stabilization. The written finite irredundant decomposition gives the components; subtracting the other finitely many components leaves a nonempty open contained in each component.

Bind this finite chain, and include the stated routine deduction if the reader requires an explicit bridge; do not claim that one narrower theorem alone states the full native claim.

#### Points of finite type

**Unbound lower prerequisite.** Native locator: `morphisms.tex` / `lemma-point-finite-type`.

No exact existing written or genuinely assigned programme provider was established in this bounded title/statement/plan reconciliation. A related topic is not asserted to own the entire native claim.

#### Commutative algebra

**Written subargument at the stated scope.** Native locator: `algebra.tex` / `example-ML-surjective-maps`.

Stable-image replacement of a Mittag-Leffler system gives surjective transition maps and the same inverse limit.

*Completion* (AG-CA), Lemma1.1 proof, lines25-27: The stable-image/surjectivity step uses directedness; countability is required only for the subsequent nonempty-limit conclusion.

Line25 chooses a common later index beyond two stabilization indices. The same finite-index argument is valid for an arbitrary directed system. Compatible coordinates already lie in every later image, giving the same limit.

#### Modules

**Written exact provider.** Native locator: `algebra.tex` / `lemma-intersection-powers-ideal-module`.

For a Noetherian ring and finite module, the intersection of ideal powers vanishes on a neighbourhood of every prime containing the ideal, and vanishes globally for a Jacobson-radical ideal.

*Noetherian and Artinian rings* (AG-CA), Theorem6.1, lines254-276: Noetherian R, finite M, arbitrary ideal I.

The theorem provides a single annihilator 1+a with a in I. For a prime containing I this annihilator avoids that prime; localizing kills the intersection. The Jacobson-radical case is stated expressly.

#### Derived tensor products and Tor amplitude

**Written exact provider.** Native locator: `algebra.tex` / `lemma-long-exact-sequence-tor`.

Tor has the natural long exact sequence for a short exact sequence in its second variable.

*Resolutions, Tor and Ext* (AG-CA), Section2 lines32-40; Theorem3.2 lines54-60: Arbitrary commutative ring and arbitrary modules.

The actual stated scope matches this exact native claim; its local written argument is present. Provider prerequisites retain their actual state.

#### Noetherian rings

**Written provider and explicit deduction.** Native locator: `algebra.tex` / `lemma-reduced-goes-up-noetherian`.

A flat map of Noetherian rings with reduced base and reduced fibres has reduced target.

*Spectra of rings* (AG-CA), Theorem1.2, lines34-53; minimal primes in Theorem4.1/Lemma4.2: Nilradical and minimal prime detection.

*Noetherian and Artinian rings* (AG-CA), Proposition2.2 and Theorem4.2, lines69-79,157-196: Finitely many minimal primes; Noetherian zero-dimensional rings are Artinian.

*Tor and flat modules* (AG-CA), Definition of flatness and Theorem2.1, lines9-24,80-109: Arbitrary ring and module.

The reduced Noetherian base embeds into the finite product of its localizations at minimal primes; those local rings are reduced zero-dimensional Noetherian local rings and hence fields. Flat tensoring preserves that injection and commutes with this finite product. The target therefore embeds into the product of its reduced minimal-prime fibres, so is reduced. This is a finite composition of the written predecessors, with the exact native assumptions retained.

Bind this finite chain, and include the stated routine deduction if the reader requires an explicit bridge; do not claim that one narrower theorem alone states the full native claim.

#### Commutative algebra

**Written exact provider.** Native locator: `algebra.tex` / `lemma-Mittag-Leffler`.

A short exact sequence of integer-indexed module systems remains exact under inverse limit when the kernel system is Mittag-Leffler.

*Completion* (AG-CA), Lemma1.1 and Theorem1.2, lines23-40: Countable directed inverse systems of abelian groups; applies to the stated integer-indexed module systems.

The actual stated scope matches this exact native claim; its local written argument is present. Provider prerequisites retain their actual state.

#### Criteria for integral extensions

**Written exact provider.** Native locator: `algebra.tex` / `lemma-characterize-integral-element`.

An element preserving a finite base submodule containing1 is integral.

*Integral extensions: lying over, going up and going down* (AG-CA), Theorem1.1, determinant proof lines29-41: Arbitrary base ring/algebra and finite faithful module for multiplication by the element.

A stable finite submodule containing1 is faithful over R[y]: an operator killing it kills1. Thus the exact determinant argument applies.

#### Commutative algebra

**Written exact provider.** Native locator: `algebra.tex` / `lemma-length-additive`.

Module length, allowing infinity, is additive in a short exact sequence.

*Noetherian and Artinian rings* (AG-CA), Theorem3.3, lines117-135: Arbitrary ring; finite-length iff statement and finite additivity.

Finite middle length is equivalent to both ends having finite length; the stated finite sum proves additivity there, and the iff treats the remaining infinite-length cases.

#### Commutative algebra

**Written exact provider.** Native locator: `algebra.tex` / `lemma-simple-pieces`.

Composition factors are residue fields, with maximal-ideal multiplicities measured by localized length.

*Noetherian and Artinian rings* (AG-CA), Section3; Theorems3.2-3.3 and Proposition3.4, lines83-139: Finite-length module over an arbitrary commutative ring.

The actual stated scope matches this exact native claim; its local written argument is present. Provider prerequisites retain their actual state.

#### Commutative algebra

**Written at this consumer scope.** Native locator: `algebra.tex` / `lemma-Schanuel`.

Stable isomorphism of two projective presentation kernels.

*Projective dimension and the Auslander–Buchsbaum formula* (AG-CA), Lemma1.1, lines21-27: Arbitrary ring, projective presentations of the same module.

The fibre-product proof identifies the common module with K plus Q and L plus P. The native lemma additionally displays a diagram; the matched consumer is the stable-kernel isomorphism. Retain that diagram as a display construction when consumed.

#### Field extensions

**Written exact provider.** Native locator: `algebra.tex` / `lemma-length-resolution-residue-field`.

Projective dimension of the residue field is at least embedding dimension.

*Regular local rings* (AG-CA), Lemma2.1, lines75-124: Noetherian local ring; arbitrary characteristic, finite or infinite projective dimension.

The actual stated scope matches this exact native claim; its local written argument is present. Provider prerequisites retain their actual state.

#### Regular rings and dimension and codimension

**Written exact provider.** Native locator: `algebra.tex` / `proposition-regular-finite-gl-dim`.

A nonzero finite module of depth e over a d-dimensional regular local ring has a finite free resolution of length d-e, and global dimension is at most d.

*Projective dimension and the Auslander–Buchsbaum formula* (AG-CA), Theorem2.2, Theorem2.3 and Corollary4.3, lines117-154,242-255: Noetherian regular local ring; global dimension includes arbitrary modules.

The actual stated scope matches this exact native claim; its local written argument is present. Provider prerequisites retain their actual state.

#### Dimension and codimension

**Written provider and explicit deduction.** Native locator: `algebra.tex` / `lemma-dim-gl-dim`.

Finite projective dimension n of the residue field is at most the Krull dimension.

*Projective dimension and the Auslander–Buchsbaum formula* (AG-CA), Theorem3.1, lines157-195: Noetherian local ring and finite module of finite projective dimension.

*Regular sequences, depth and Cohen–Macaulay modules* (AG-CA), Theorem3.1, lines151-192: Depth of a finite module is at most support dimension.

Apply Auslander-Buchsbaum to the residue field, whose depth is0: n=depth R<=dim R. Regularity is not an additional hypothesis.

Bind this finite chain, and include the stated routine deduction if the reader requires an explicit bridge; do not claim that one narrower theorem alone states the full native claim.

#### Finite algebras

**Partial written provider; the remaining claim is unbound.** Native locator: `algebra.tex` / `lemma-length-finite`.

Finite modules killed by a power of a finitely generated maximal ideal have finite length even over a non-Noetherian ring.

The written finite-layer explanation covers the Noetherian local use; the native assumption needs only a finitely generated maximal ideal and need not assume the ring Noetherian. Do not silently narrow its scope.

#### Noetherian rings

**Written exact provider.** Native locator: `algebra.tex` / `lemma-Noetherian-power`.

An ideal contained in the radical of another has a power contained in it.

*Noetherian and Artinian rings* (AG-CA), Proposition2.2 proof, lines69-79: Arbitrary ideals in a Noetherian ring.

The written proof gives (sqrt I)^N subset I; J subset sqrt I gives J^N subset I.

#### Finite algebras

**Written provider and explicit deduction.** Native locator: `algebra.tex` / `lemma-quasi-finite-permanence`.

A finite-type composite that is quasi-finite at a point stays quasi-finite over an intermediate base.

*Quasi-finite morphisms and Chevalley’s theorem* (AG-MO), Theorem1.1 and Proposition2.1, lines13-43: Finite-type algebra pointwise tests and base-change/immersion stability.

The intermediate algebra acts on the finite-dimensional isolated original fibre algebra. Localizing to the selected intermediate residue field keeps a finite-dimensional quotient after scalar extension. Alternatively the graph is a closed immersion into the base change; apply the same base-change/immersion pointwise test. No finite-presentation hypothesis on the intermediate algebra is added.

Bind this finite chain, and include the stated routine deduction if the reader requires an explicit bridge; do not claim that one narrower theorem alone states the full native claim.

#### Finite algebras

**Written exact provider.** Native locator: `algebra.tex` / `lemma-quasi-finite-monogenic`.

An isolated fibre point of a monogenic finite-type algebra has the stated integral-closure localization.

*Zariski's Main Theorem* (AG-MO), Theorem1.1 and Sections1-2: Arbitrary ring and finite-type algebra.

The actual theorem treats all finite-type algebras, hence the monogenic case. Its actual conductor and point-isolation lower prerequisites remain unclosed; this is a written owned provider, not recursive closure.

#### Finite algebras and local algebra

**Written provider and explicit deduction.** Native locator: `algebra.tex` / `lemma-quasi-finite-local`.

Quasi-finiteness at a point is unchanged by localizing source and base away from the corresponding primes.

*Quasi-finite morphisms and Chevalley’s theorem* (AG-MO), Theorem1.1, lines13-27: Locally finite-type scheme morphisms; fibre-local characterization.

The base localization preserves the same fibre and the source localization is an open containing the point. Isolation in that fibre is equivalent before and after either localization, exactly the pointwise test.

Bind this finite chain, and include the stated routine deduction if the reader requires an explicit bridge; do not claim that one narrower theorem alone states the full native claim.

#### Commutative algebra

**Written provider and explicit deduction.** Native locator: `algebra.tex` / `lemma-four-rings`.

A quotient of a base-changed finite-type algebra preserves quasi-finiteness at the corresponding point.

*Quasi-finite morphisms and Chevalley’s theorem* (AG-MO), Proposition2.1, lines37-43: Arbitrary bases; base change, composition and immersions.

The surjection S tensor_R R-prime -> S-prime gives a closed immersion into the base change. Base change preserves the pointwise property and the closed immersion is locally quasi-finite; composition proves the assertion.

Bind this finite chain, and include the stated routine deduction if the reader requires an explicit bridge; do not claim that one narrower theorem alone states the full native claim.

#### Finite algebras

**Unbound lower prerequisite.** Native locator: `algebra.tex` / `lemma-reduced-strongly-transcendental-not-quasi-finite`.

No exact ordinary predecessor provider was established for this strongly-transcendental non-quasi-finite lemma; a general quasi-finite stability theorem is not equivalent.

#### Commutative algebra

**Unbound lower prerequisite.** Native locator: `algebra.tex` / `lemma-all-coefficients-in-J`.

No ordinary programme provider was established for the strongly-transcendental radical-coefficient statement at this source-defined situation.

#### Cotangent complexes and differentials

**Written subargument at the stated scope.** Native locator: `algebra.tex` / `lemma-computation-differential`.

For a Noetherian local k-algebra with finitely generated separable residue extension, m/m^2 injects into Omega tensor the residue field.

*Smooth algebras over a field and the Jacobian criterion* (AG-CA), Theorem3.2 proof subargument, lines166-178: The injection subargument requires only a local k-algebra and finitely generated separable residue field; the surrounding smoothness equivalence additionally assumes finite type.

The proof lifts the residue field into A/m^2 by formal smoothness and invokes the split-conormal proposition; its product-rule identification gives the displayed injection. Only this expressly written subargument is bound, not an arbitrary-ring extension of the surrounding finite-type smoothness theorem.

#### Field extensions

**Unbound lower prerequisite.** Native locator: `fields.tex` / `lemma-pth-root`.

No exact existing field provider for this separable-extension pth-root descent claim was found. Prime-field formal smoothness in the coefficient lesson does not state it.

#### Field extensions

**Unbound lower prerequisite.** Native locator: `fields.tex` / `lemma-separable-first`.

No exact existing provider for unique separable-then-purely-inseparable factorization of every algebraic extension was found. Finite field differential criteria are narrower and cannot be substituted.

#### The geometric construction

**Unbound lower prerequisite.** Native locator: `fields.tex` / `lemma-primitive-element`.

No exact existing provider for the primitive-element iff finitely-many-intermediate-fields statement was found. A course citing the separable primitive-element result is not its written proof.

#### The geometric construction

**Written provider and explicit deduction.** Native locator: `fields.tex` / `lemma-transcendence-degree`.

Transcendence bases exist, extend an independent set within a generating set, and have well-defined cardinality.

*Krull dimension and Noether normalization* (AG-CA), Lemma1.3 and proof, lines45-53: Arbitrary field extensions, including infinite bases.

The Zorn proof extends a prescribed independent A by considering independent subsets of the generating G containing A; maximality forces every generator algebraic. The written cardinality/exchange proof handles arbitrary basis sizes. Record this specified choice in the short application rather than pretending the printed statement explicitly names A and G.

#### Filtered limits and commutative algebra

**Unbound lower prerequisite.** Native locator: `algebra.tex` / `lemma-limit-argument`.

No exact programme lemma for all three finite-subalgebra detection statements over a field was established; finite equation descent is a related input, not a recorded complete proof here.

#### Commutative algebra

**Unbound lower prerequisite.** Native locator: `algebra.tex` / `lemma-hilbert-ses`.

Degree additivity for Hilbert-Samuel polynomials is written, but this exact shifted finite-colength equality is stronger; no exact provider was established.

#### Finite algebras

**Unbound lower prerequisite.** Native locator: `algebra.tex` / `lemma-differ-finite-chi`.

No exact written provider was established for the strict degree drop of the difference polynomial for every finite-colength submodule of an infinite-length module.

#### Dimension and codimension

**Unbound lower prerequisite.** Native locator: `algebra.tex` / `lemma-dimension-going-up`.

The native source allows arbitrary rings and any surjective going-up or going-down map. Integral dimension and local Noetherian flat dimension formulas are narrower; no exact full provider was established.

#### Commutative algebra

**Partial written provider; the remaining claim is unbound.** Native locator: `algebra.tex` / `lemma-helper-polynomial`.

A triangular high-power substitution makes any nonconstant polynomial over an arbitrary ring have a single positive-degree top term.

The full source uses e1 much larger than e2 and so on with en=1, while the provider displays increasing base-e weights. Reindexing gives the same triangular substitution, and the calculation works over an arbitrary ring without dividing by coefficients. Bind only after recording this specific elementary change; do not label the complete field normalization lemma as an arbitrary-ring normalization theorem.

#### Dimension and codimension

**Partial written provider; the remaining claim is unbound.** Native locator: `algebra.tex` / `lemma-dim-formula-maximal-CM`.

A Noetherian local ring carrying a CM module with full support satisfies the dimension formula at every prime.

The explicitly stated dimension formula assumes the ring is CM, which is stronger than existence of a full-support CM module. The native full-support-module version is not silently bound to Lemma5.4; a separate exact module argument is needed.

#### The geometric construction

**Written exact provider.** Native locator: `topology.tex` / `lemma-constructible-stable-specialization-closed`.

For a spectral space a patch-closed subset has every closure point as a specialization from it; specialization-stable patch-closed subsets are closed, with the complementary open assertion.

*Spectral spaces and affine realization* (AG-CA), Lemma1.2 and proof, lines38-40: Every spectral space and patch-closed subset.

The compactness proof supplies the closure specialization. Its closed/stable equivalence gives part2; applying it to the complementary patch-closed set gives part3.

#### Prime spectra and associated points

**Partial written provider; the remaining claim is unbound.** Native locator: `algebra.tex` / `lemma-spec-spectral`.

Every affine spectrum is a spectral space.

The required affine-spectrum axioms are ordinary written predecessors, but the exact aggregate statement was not established as an explicit theorem in the bounded body pass. Do not use Hochster realization in the reverse direction as a proof of this claim.

#### The geometric construction

**Unbound lower prerequisite.** Native locator: `topology.tex` / `lemma-open-closed-specialization`.

No exact existing written or genuinely assigned programme provider was established in this bounded title/statement/plan reconciliation. A related topic is not asserted to own the entire native claim.

#### The geometric construction

**Unbound lower prerequisite.** Native locator: `topology.tex` / `lemma-constructible`.

No exact existing written or genuinely assigned programme provider was established in this bounded title/statement/plan reconciliation. A related topic is not asserted to own the entire native claim.

#### Commutative algebra

**Unbound lower prerequisite.** Native locator: `algebra.tex` / `lemma-constructible-is-image`.

No exact existing written or genuinely assigned programme provider was established in this bounded title/statement/plan reconciliation. A related topic is not asserted to own the entire native claim.

#### Affine neighbourhoods

**Unbound lower prerequisite.** Native locator: `algebra.tex` / `lemma-affineline-open`.

No exact existing written or genuinely assigned programme provider was established in this bounded title/statement/plan reconciliation. A related topic is not asserted to own the entire native claim.

#### Affine neighbourhoods

**Unbound lower prerequisite.** Native locator: `algebra.tex` / `lemma-affineline-special`.

No exact existing written or genuinely assigned programme provider was established in this bounded title/statement/plan reconciliation. A related topic is not asserted to own the entire native claim.

#### Finite presentation

**Unbound lower prerequisite.** Native locator: `algebra.tex` / `lemma-closed-fp`.

No exact existing written or genuinely assigned programme provider was established in this bounded title/statement/plan reconciliation. A related topic is not asserted to own the entire native claim.

#### Finite presentation

**Unbound lower prerequisite.** Native locator: `algebra.tex` / `lemma-open-fp`.

No exact existing written or genuinely assigned programme provider was established in this bounded title/statement/plan reconciliation. A related topic is not asserted to own the entire native claim.

#### Commutative algebra

**Unbound lower prerequisite.** Native locator: `algebra.tex` / `lemma-constructible`.

No exact existing written or genuinely assigned programme provider was established in this bounded title/statement/plan reconciliation. A related topic is not asserted to own the entire native claim.

#### Field extensions and tensor products and direct sums

**Unbound lower prerequisite.** Native locator: `algebra.tex` / `lemma-reduced-ring-sub-product-fields`.

The reduced ring embedding into residue fields follows from the nilradical theorem, but the full minimal-prime localization and union-of-minimal-primes zero-divisor statement is broader; no exact full programme provider was established.

#### Commutative algebra

**Written provider and explicit deduction.** Native locator: `algebra.tex` / `lemma-where-CM`.

For a quasi-finite map from a finite-type field algebra to affine d-space, flatness at a point is equivalent to Cohen-Macaulayness and pointwise field dimension d.

*Flatness criteria, dimension and the flat locus* (AG-FSE), Theorem3.1, Theorem4.1 and Corollary7.1, lines64-84,107-153,307-311: Noetherian local dimension, miracle flatness and quasi-finite local equal-dimension criterion.

*Regular sequences, depth and Cohen–Macaulay modules* (AG-CA), Proposition1.1 and Theorem6.1, lines20-26,281-315: Flat transport of regular sequences and regular local parameters.

*Regular local rings* (AG-CA), Proposition3.3 and consequence, lines185-197: Polynomial regularity over every field.

*Krull dimension and Noether normalization* (AG-CA), Theorem6.1, lines205-228: Pointwise dimension = local dimension plus residue transcendence degree.

*Quasi-finite morphisms and Chevalley’s theorem* (AG-MO), Theorem1.1, lines13-27: Quasi-finite points have finite residue extension and zero-dimensional local fibre.

Write p for the point in affine d-space. Finite residue extension identifies the two residue transcendence degrees. Thus source pointwise dimension d is equivalent to equality of source and target local dimensions. CM plus that equality gives flatness by Corollary7.1. Conversely flatness gives the same local dimension by the zero-dimensional-fibre formula; a regular parameter sequence of the target stays regular in the source by flatness, so depth reaches the source dimension and the source is CM. The dimension identity then gives pointwise dimension d. This deduction treats all geometric characteristics and nonreduced fibres.

Bind this finite chain, and include the stated routine deduction if the reader requires an explicit bridge; do not claim that one narrower theorem alone states the full native claim.

#### Openness of the flat locus

**Written exact provider.** Native locator: `algebra.tex` / `theorem-openness-flatness`.

The flat locus of a finitely presented module over a finitely presented base algebra is open.

*Flatness criteria, dimension and the flat locus* (AG-FSE), Theorem6.4, lines289-295: Arbitrary base ring, finitely presented algebra and module.

The exact arbitrary-base theorem has its actual written finite-model proof; the Noetherian Theorem5.2 alone is not the provider.

#### Henselian rings

**Partial written provider; the remaining claim is unbound.** Native locator: `algebra.tex` / `lemma-uniqueness-henselian`.

Two henselian local ind-etale R-algebras identified with the same residue field are uniquely isomorphic compatibly.

The same-residue henselization case is written, but the exact native statement allows arbitrary R and a common residue field extension K. No single exact general ind-etale uniqueness provider was established; do not substitute only the henselization universal property without the needed lifting/colimit deduction.

#### Composition and étale morphisms

**Unbound lower prerequisite.** Native locator: `algebra.tex` / `lemma-composition-colimit-etale`.

Composition stability for individual etale maps is written, but the exact filtered-colimit composition theorem needs a finite-presentation descent argument not identified as a matching printed provider.

#### Henselian rings and finite algebras

**Written provider and explicit deduction.** Native locator: `algebra.tex` / `lemma-finite-over-henselian`.

Finite algebras over a henselian local base split into henselian local factors; every quasi-finite point over the closed point has a finite henselian localization.

*Henselian local rings and henselization* (AG-CA), Proposition3.1, lines97-101: Arbitrary henselian local base and finite algebras.

*Étale neighbourhoods, henselization and quasi-finite morphisms* (AG-FSE), Lemma4.1, lines120-139: Arbitrary henselian local base and finite-type algebra.

The finite-part lemma gives exactly a finite local factor for each isolated closed-fibre point. Its local ring at that point is that factor, so Proposition3.1 makes it finite henselian. This covers all four native parts; preserve its actual algebraic Zariski Main dependency.

Bind this finite chain, and include the stated routine deduction if the reader requires an explicit bridge; do not claim that one narrower theorem alone states the full native claim.

#### Filtered limits and henselian rings

**Written exact provider.** Native locator: `algebra.tex` / `lemma-colimit-henselian`.

Filtered colimits along local maps preserve henselianity and strict henselianity.

*Henselian local rings and henselization* (AG-CA), Proposition3.2, lines103-107: Arbitrary local rings and filtered local maps.

The actual stated scope matches this exact native claim; its local written argument is present. Provider prerequisites retain their actual state.

#### Finite presentation and Noetherian rings

**Written provider and explicit deduction.** Native locator: `algebra.tex` / `lemma-Noetherian-finite-type-is-finite-presentation`.

Finite modules are finitely presented, their submodules are finite, and finite-type algebras are finitely presented over a Noetherian ring.

*Noetherian and Artinian rings* (AG-CA), Theorem1.1, Proposition1.2 and Theorem2.1, lines15-59; also differential lesson line166: Noetherian base; finite modules and finite-type algebras.

Finite free presentation kernels are finite by Proposition1.2; polynomial presentation kernels are finite by Hilbert basis. Line166 of Kahler differentials states the algebra consequence expressly.

#### Finite presentation and tensor products and direct sums

**Unbound lower prerequisite.** Native locator: `algebra.tex` / `proposition-fp-tensor`.

No exact written or genuinely assigned provider for the full tensor/product characterization of finite presentation was established.

#### Tensor products and direct sums

**Unbound lower prerequisite.** Native locator: `algebra.tex` / `proposition-fg-tensor`.

No exact written or genuinely assigned provider for the full tensor/product characterization of finite generation was established.

#### Tensor products and direct sums

**Unbound lower prerequisite.** Native locator: `algebra.tex` / `lemma-flip-tensor-product`.

No exact programme provider for the complete symmetry/distribution/unit triple was established in the bounded search.

#### Modules and tensor products and direct sums

**Unbound lower prerequisite.** Native locator: `algebra.tex` / `lemma-tensor-with-bimodule`.

No exact programme provider for the full bimodule associativity statement was established.

#### Finite algebras

**Unbound lower prerequisite.** Native locator: `algebra.tex` / `lemma-produce-finite`.

No exact matching finite-neighbourhood production claim with the stated integral intermediate algebra and invertible fibre element was established.

#### Étale morphisms and derived tensor products and Tor amplitude

**Unbound lower prerequisite.** Native locator: `algebra.tex` / `lemma-factor-mod-lift-etale`.

Henselian factor lifting is written, but the native statement constructs a same-residue etale base neighbourhood from an arbitrary base; no exact construction provider was established in this pass.

#### Prime spectra and associated points

**Unbound lower prerequisite.** Native locator: `algebra.tex` / `lemma-ring-with-only-minimal-primes`.

Artinian decomposition is not the arbitrary-ring eight-way equivalence for zero-dimensional affine spectra. No exact matching ordinary programme provider was found.

#### Filtered limits and commutative algebra

**Unbound lower prerequisite.** Native locator: `algebra.tex` / `lemma-directed-colimit`.

The henselization lesson explains the explicit filtered-colimit element construction at lines132 and156, but no complete standalone arbitrary-preordered-module-system provider was established.

#### Derived Hom, Ext and tensor products and direct sums

**Unbound lower prerequisite.** Native locator: `algebra.tex` / `lemma-hom-from-tensor-product`.

No exact current programme theorem/file for the full tensor-Hom adjunction was established in the bounded search; a label in a prerequisite list is not sufficient.

#### Modules

**Unbound lower prerequisite.** Native locator: `algebra.tex` / `lemma-cover-module`.

Affine module sheaf-gluing is a related existing geometric construction, but no exact predecessor theorem for this arbitrary-module finite standard-open equalizer was established.

#### Functoriality of affine spectra

**Written exact provider.** Native locator: `algebra.tex` / `lemma-spec-functorial`.

Contraction of primes defines a continuous contravariant spectrum functor.

*Spectra of rings* (AG-CA), Section3, lines96-103: Arbitrary ring map.

The actual stated scope matches this exact native claim; its local written argument is present. Provider prerequisites retain their actual state.

#### Cotangent complexes and differentials

**Written provider and explicit deduction.** Native locator: `algebra.tex` / `lemma-differential-mod-power-ideal`.

Modding out by I^(n+1) does not change differentials after tensoring with S/I^n.

*Kähler differentials* (AG-CA), Theorem3.3 and proof, lines99-108: Arbitrary ring map and arbitrary ideal.

The conormal kernel is generated by d(I^(n+1)). Leibniz expresses each such differential with coefficients in I^n, so its image after tensoring with S/I^n is zero. Right exactness gives the exact native isomorphism for every n>=1.

Bind this finite chain, and include the stated routine deduction if the reader requires an explicit bridge; do not claim that one narrower theorem alone states the full native claim.

#### Formal smoothness and smooth morphisms

**Written exact provider.** Native locator: `algebra.tex` / `lemma-polynomial-ring-formally-smooth`.

Polynomial rings are formally smooth.

*Formally smooth, unramified and étale ring maps* (AG-CA), Theorem1.2, lines23-31: Arbitrary base and any set of polynomial variables.

The actual stated scope matches this exact native claim; its local written argument is present. Provider prerequisites retain their actual state.

#### Finite algebras

**Written provider and explicit deduction.** Native locator: `algebra.tex` / `lemma-finite-residue-extension-closed`.

A prime over a maximal base ideal with algebraic residue extension is maximal.

*Integral extensions: lying over, going up and going down* (AG-CA), Lemma3.1, lines122-124: Integral inclusions of domains.

The domain S/q contains the base field R/m and is algebraic over it, hence integral over it. The written integral-domain/field equivalence makes S/q a field. No finite-type hypothesis is added.

Bind this finite chain, and include the stated routine deduction if the reader requires an explicit bridge; do not claim that one narrower theorem alone states the full native claim.

#### Dimension, codimension and field extensions

**Written exact provider.** Native locator: `algebra.tex` / `lemma-dimension-closed-point-finite-type-field`.

At a closed point of a finite-type field scheme, pointwise dimension equals local-ring dimension.

*Krull dimension and Noether normalization* (AG-CA), Theorem6.1 and closed-point consequence, lines205-228: Any finite-type algebra over any field, including reducible and nonreduced.

The actual stated scope matches this exact native claim; its local written argument is present. Provider prerequisites retain their actual state.

#### Commutative algebra

**Written exact provider.** Native locator: `algebra.tex` / `lemma-jacobson`.

The algebraic Jacobson-ring condition equals the topological Jacobson-spectrum condition.

*The Nullstellensatz and Jacobson rings* (AG-CA), Proposition3.1, lines98-108: Arbitrary commutative ring.

The actual stated scope matches this exact native claim; its local written argument is present. Provider prerequisites retain their actual state.

#### Field extensions and finite algebras

**Written exact provider.** Native locator: `algebra.tex` / `lemma-finite-type-field-Jacobson`.

Every finite-type algebra over a field is Jacobson.

*The Nullstellensatz and Jacobson rings* (AG-CA), Theorem2.2, lines58-96; alternatively Theorem4.2, lines128-147: Arbitrary field and finite-type algebra.

The actual stated scope matches this exact native claim; its local written argument is present. Provider prerequisites retain their actual state.

#### Commutative algebra

**Written exact provider.** Native locator: `algebra.tex` / `lemma-easy-ff`.

Faithfully flat tensoring detects zero module maps.

*Faithful flatness and the local criterion for flatness* (AG-CA), Theorem1.1 and consequence, lines20-33: Arbitrary ring and flat module.

Line33 identifies the tensor image with the image tensored and proves zero-map reflection. Conversely testing identities gives faithful nonzero-module detection from Theorem1.1.

#### Derived tensor products and Tor amplitude

**Unbound lower prerequisite.** Native locator: `algebra.tex` / `lemma-surjective-on-tor-one`.

Long exact Tor and balanced Tor are written, but the exact change-of-rings surjection with flat pulled-back M was not identified as a complete programme proof.

#### Derived tensor products and Tor amplitude

**Unbound lower prerequisite.** Native locator: `algebra.tex` / `lemma-surjective-on-tor-one-trivial`.

The exact quotient change-of-rings Tor1 surjection was not identified in a written programme theorem; Tor balance alone is insufficient.

#### Field extensions

**Written provider and explicit deduction.** Native locator: `fields.tex` / `lemma-subalgebra-algebraic-extension-field`.

Every intermediate subring of an algebraic field extension is a field.

*Integral extensions: lying over, going up and going down* (AG-CA), Lemma3.1, lines122-124: Integral inclusions of domains.

If F subset R subset E and E/F is algebraic, E is integral over R using its monic equations over F. Apply the direction B field implies A field to R subset E. This covers infinite algebraic extensions.

Bind this finite chain, and include the stated routine deduction if the reader requires an explicit bridge; do not claim that one narrower theorem alone states the full native claim.

#### Noetherian rings

**Written exact provider.** Native locator: `algebra.tex` / `lemma-obvious-Noetherian`.

Finite-type algebras over a field or the integers are Noetherian.

*Noetherian and Artinian rings* (AG-CA), Theorem2.1, lines45-59: Noetherian base ring.

The actual stated scope matches this exact native claim; its local written argument is present. Provider prerequisites retain their actual state.

#### Cotangent complexes and differentials

**Written provider and explicit deduction.** Native locator: `algebra.tex` / `lemma-differential-surjective`.

A quotient in a commuting ring-map square gives a surjection on differentials, with kernel generated by derivatives of elements whose image lies in the new base.

*Kähler differentials* (AG-CA), Theorems3.1 and3.3, lines83-108: Arbitrary composable ring maps and quotient ideals.

First quotient the target algebra over the old base using the conormal sequence, then enlarge the base using the first fundamental sequence. A generator from the new base which is in the quotient target lifts to an old target element, giving exactly the stated kernel. Elements of the quotient ideal are included.

Bind this finite chain, and include the stated routine deduction if the reader requires an explicit bridge; do not claim that one narrower theorem alone states the full native claim.

#### Closed support

**Written exact provider.** Native locator: `algebra.tex` / `lemma-CM-ass-minimal-support`.

A finite CM module has only minimal associated support primes and all such components have its support dimension.

*Regular sequences, depth and Cohen–Macaulay modules* (AG-CA), Theorem4.1, lines194-203: Finite CM module over a Noetherian local ring.

The actual stated scope matches this exact native claim; its local written argument is present. Provider prerequisites retain their actual state.

#### Prime spectra and associated points

**Unbound lower prerequisite.** Native locator: `algebra.tex` / `lemma-inherit-minimal-primes`.

No exact existing proof or assignment was found for membership in Ass(M/x^n M) for some n of a prime minimal over p+(x). Associated-prime localization alone does not cover it.

#### Closed support

**Written provider and explicit deduction.** Native locator: `algebra.tex` / `lemma-support-quotient`.

Support of a finite module modulo I is its support intersected with V(I); submodules, quotients and exact sequences have the stated support calculus.

*Localization, local properties and support* (AG-CA), Proposition6.1, lines213-227; Theorem4.2 Nakayama, lines181-193: Arbitrary ring; finite M for the I-quotient formula.

Localize. If I avoids the prime the quotient is zero; otherwise I is in the local maximal ideal, and Nakayama makes M_p/I M_p nonzero exactly when M_p is nonzero. Exactness gives the other three assertions.

Bind this finite chain, and include the stated routine deduction if the reader requires an explicit bridge; do not claim that one narrower theorem alone states the full native claim.

#### Commutative algebra

**Written provider and explicit deduction.** Native locator: `algebra.tex` / `lemma-CM-over-quotient`.

A finite module over a quotient of Noetherian local rings is CM over either ring simultaneously.

*Regular sequences, depth and Cohen–Macaulay modules* (AG-CA), Definition of regular sequences and Theorem2.3, lines11-18,96-125: Noetherian local ring and finite module.

*Localization, local properties and support* (AG-CA), Theorem3.1, lines119-144; Proposition6.1, lines213-227: Quotient prime correspondence and finite support.

Regular sequences act through the quotient and lift along the surjection, so depths agree. Prime/support correspondence preserves chains, so support dimensions agree. The depth-equals-support-dimension definition therefore agrees.

Bind this finite chain, and include the stated routine deduction if the reader requires an explicit bridge; do not claim that one narrower theorem alone states the full native claim.

#### Commutative algebra

**Written exact provider.** Native locator: `algebra.tex` / `lemma-permute-xi`.

Regular sequences on finite modules over Noetherian local rings can be permuted.

*Regular sequences, depth and Cohen–Macaulay modules* (AG-CA), Proposition1.2, lines28-34: Nonzero finite module over a Noetherian local ring.

The actual stated scope matches this exact native claim; its local written argument is present. Provider prerequisites retain their actual state.

#### Commutative algebra

**Unbound lower prerequisite.** Native locator: `algebra.tex` / `lemma-good-element`.

No exact provider for this source-defined good-element construction was established; the actual definitions and maximal regular sequence conditions cannot be inferred from the label.

#### Regular rings and dimension and codimension

**Partial written provider; the remaining claim is unbound.** Native locator: `algebra.tex` / `lemma-finite-gl-dim-finite-dim-regular`.

For a nonzero Noetherian ring, finite global dimension equals finite regular Krull dimension and the corresponding bounds on all localizations.

The source is a global arbitrary-module theorem. The local statements alone do not cover it. A uniform local bound plus finite-syzygy projectivity/localization deduction is needed; no exact written global theorem was identified in the inspected bodies.

#### Dimension, codimension and affine neighbourhoods

**Partial written provider; the remaining claim is unbound.** Native locator: `algebra.tex` / `lemma-dim-affine-space`.

A maximal ideal in k[x1,...,xn] is generated by n elements and has an n-dimensional regular local ring.

The regular-local conclusion is explicitly written, including inseparable residue fields. Its minimal local parameter count does not itself prove that the maximal ideal is globally generated by n polynomial elements; the full native global-generator assertion remains unbound.

#### Derived Hom, Ext and proper morphisms

**Unbound lower prerequisite.** Native locator: `algebra.tex` / `lemma-graded-ext-properties`.

Ordinary Tor/Ext and some projective-space graded calculations are written, but the entire exact six-part graded Ext statement, including forgetful comparison and polynomial global-dimension range, was not bound.

#### Dimension, codimension and field extensions

**Partial written provider; the remaining claim is unbound.** Native locator: `algebra.tex` / `lemma-dimension-at-a-point-finite-type-over-field`.

Pointwise dimension equals the maximum component dimension through the point and the minimum local dimension over containing maximal ideals.

The maximum-component equality and closed-point formula are explicitly written. The minimum over maximal ideals containing p requires choosing a closed specialization avoiding the larger unwanted components; that complete third equality was not established as a written locus in the bounded provider pass.

#### Dimension and codimension

**Written exact provider.** Native locator: `algebra.tex` / `lemma-dimension-spell-it-out`.

Every maximal localization of a finite-type field domain has its full dimension.

*Krull dimension and Noether normalization* (AG-CA), Corollary4.4, lines166-173; Theorem5.1, lines175-203: Finite-type domain over any field.

The actual stated scope matches this exact native claim; its local written argument is present. Provider prerequisites retain their actual state.

#### Commutative algebra

**Unbound lower prerequisite.** Native locator: `algebra.tex` / `lemma-ci-well-defined`.

Regular quotients and expected-dimension regular-sequence criteria are written, but no exact real provider for independence of the regular local presentation of a complete intersection was established.

#### Local algebra

**Unbound lower prerequisite.** Native locator: `algebra.tex` / `lemma-isomorphic-local-rings`.

No exact matching existing provider for spreading an isomorphism of two finitely presented local algebras to principal neighbourhoods was found.

#### Dimension, codimension and finite algebras

**Written provider and explicit deduction.** Native locator: `algebra.tex` / `lemma-dimension-inequality-quasi-finite`.

For an arbitrary finite-type ring map quasi-finite at q over p, the local source dimension is at most the local base dimension.

*Zariski's Main Theorem* (AG-MO), Theorem1.1 and Sections1-2: Arbitrary finite-type algebra isolated-point integral-closure localization.

*Étale neighbourhoods, henselization and quasi-finite morphisms* (AG-FSE), Lemma4.1 proof substep, line131: The finite integral subalgebra construction itself uses only the localization supplied by algebraic Zariski Main; henselianity enters afterwards.

*Integral extensions: lying over, going up and going down* (AG-CA), Theorem3.3, lines140-149: Incomparability for arbitrary integral ring maps.

Choose the integral-closure element g avoiding q with S_g = S-prime_g. The finite numerator construction at line131 gives a finite integral base algebra C with C_g = S_g, using one point and no henselian hypothesis. The local ring S_q is C at the corresponding prime. Every strict prime chain below that prime contracts to a strict chain below p by integral incomparability, proving the dimension inequality even for arbitrary non-Noetherian bases. Keep the actual algebraic Zariski Main lower dependency state.

Bind this finite chain, and include the stated routine deduction if the reader requires an explicit bridge; do not claim that one narrower theorem alone states the full native claim.

#### Finite algebras

**Unbound lower prerequisite.** Native locator: `algebra.tex` / `lemma-quasi-finite-open`.

No exact existing written or genuinely assigned programme provider was established in this bounded title/statement/plan reconciliation. A related topic is not asserted to own the entire native claim.

#### Commutative algebra

**Written exact provider.** Native locator: `algebra.tex` / `lemma-grothendieck`.

A nonzerodivisor in the closed fibre of a flat local Noetherian map lifts to a nonzerodivisor, and its quotient is flat.

*Faithful flatness and the local criterion for flatness* (AG-CA), Theorem5.2, lines237-239: Flat local Noetherian ring map.

If f is a unit the source assertion is immediate; otherwise the local hypotheses put f in the source maximal ideal and the written theorem applies.

#### Finite algebras

**Written provider and explicit deduction.** Native locator: `fields.tex` / `lemma-algebraic-finitely-generated`.

An algebraic field extension generated by finitely many elements is finite.

*Integral extensions: lying over, going up and going down* (AG-CA), Theorems1.1-1.2 and Lemma3.1, lines20-59,122-124: Finite-type integral algebras and domains over fields.

The algebra generated by the algebraic elements is finite over the base field by integral finite-type finiteness. It is a finite-dimensional domain and hence a field by Lemma3.1, so is the stated generated field.

Bind this finite chain, and include the stated routine deduction if the reader requires an explicit bridge; do not claim that one narrower theorem alone states the full native claim.

#### Lifting the geometric construction

**Unbound lower prerequisite.** Native locator: `topology.tex` / `lemma-lift-specialization-composition`.

No exact existing written or genuinely assigned programme provider was established in this bounded title/statement/plan reconciliation. A related topic is not asserted to own the entire native claim.

#### Lifting the geometric construction

**Unbound lower prerequisite.** Native locator: `topology.tex` / `lemma-lift-specializations-images`.

No exact existing written or genuinely assigned programme provider was established in this bounded title/statement/plan reconciliation. A related topic is not asserted to own the entire native claim.

#### The geometric construction

**Unbound lower prerequisite.** Native locator: `categories.tex` / `lemma-directed-category-system`.

No exact genuinely assigned or written ordinary programme provider for the source category-to-directed-system replacement lemma was established.

#### The geometric construction

**Unbound lower prerequisite.** Native locator: `topology.tex` / `lemma-closed-open-map-specialization`.

No exact existing written or genuinely assigned programme provider was established in this bounded title/statement/plan reconciliation. A related topic is not asserted to own the entire native claim.

#### Cofinality and colimits

**Unbound lower prerequisite.** Native locator: `categories.tex` / `lemma-cofinal`.

No exact genuinely assigned or written ordinary programme provider for this native cofinality lemma was established.

#### Cofinal subcategories of filtered categories

**Unbound lower prerequisite.** Native locator: `categories.tex` / `lemma-cofinal-in-filtered`.

No exact genuinely assigned or written ordinary programme provider for this filtered-category cofinality lemma was established.

#### Complete rings, formal power series and regular rings

**Written exact provider.** Native locator: `algebra.tex` / `lemma-regular-complete-containing-coefficient-field`.

A complete Noetherian regular local ring in equal characteristic is a power-series ring over its residue field, respecting a specified coefficient field.

*Coefficient rings and the Cohen structure theorem* (AG-CA), Corollary6.2 and proof, lines163-165; power-series map in Theorem6.1 lines149-159: Complete regular local ring, equal characteristic, arbitrary residue field.

For a prescribed coefficient field use that given map in the written construction of Phi; its dimension argument proves injectivity. No perfectness restriction is introduced.

#### Commutative algebra

**Written exact provider.** Native locator: `algebra.tex` / `theorem-cohen-structure-theorem`.

A complete local ring has a coefficient ring, and a finite maximal ideal gives a quotient of a finite-variable power-series ring over a field or Cohen ring.

*Coefficient rings and the Cohen structure theorem* (AG-CA), Theorems5.1 and6.1, lines121-161: Every complete local ring; finite maximal ideal only for the power-series presentation.

The actual stated scope matches this exact native claim; its local written argument is present. Provider prerequisites retain their actual state.

#### Formal smoothness and smooth morphisms

**Written subargument at the stated scope.** Native locator: `algebra.tex` / `lemma-cohen-ring-formally-smooth`.

For every Cohen ring and n>=1 its quotient modulo p^n is formally smooth over Z/p^n.

*Coefficient rings and the Cohen structure theorem* (AG-CA), Theorem4.1 and proof, lines82-106: Any Cohen ring, any residue field, every n>=1.

The formal-smoothness proof after construction uses only the DVR Cohen-ring properties, its arbitrary residue field, Lemma1.1 and flatness. It is not restricted to a perfect residue field or to the displayed construction.

#### Complete rings, formal power series and Noetherian rings

**Written exact provider.** Native locator: `algebra.tex` / `lemma-completion-Noetherian-Noetherian`.

The completion of a Noetherian ring along any ideal is Noetherian.

*Completion* (AG-CA), Theorem3.3, lines137-158: Noetherian ring and arbitrary ideal.

The actual stated scope matches this exact native claim; its local written argument is present. Provider prerequisites retain their actual state.

#### Commutative algebra

**Unbound lower prerequisite.** Native locator: `algebra.tex` / `theorem-universally-exact-criteria`.

The exact six-equivalence purity theorem is not the short-exact-sequence-with-flat-quotient theorem. No exact current programme proof or genuinely assigned target covering all six conditions was established.

#### Derived categories

**Partial written provider; the remaining claim is unbound.** Native locator: `homology.tex` / `lemma-double-complex-gives-resolution`.

A vertically resolving locally finite double complex over an arbitrary abelian category totalizes to a quasi-isomorphism, with the symmetric variant.

The native statement permits every abelian category and arbitrary horizontal indices with finite diagonals. The module/first-quadrant total-complex comparison is a genuine written special case, not the whole native theorem.

| Mathematical foundation | Still uncovered exact claims |
| --- | ---: |
| Categories, topology and deformation groupoids | 10 |
| Schemes, limits and descent | 1 |
| Commutative algebra and field extensions | 91 |
| Derived modules, homological algebra and ringed sites | 1 |

The accompanying conversion manifest lists every exact source label and its consumers. The full central constructions printed above are not reassigned to future work. A transitive proof-closure claim must wait for the listed lower obligations to be proved or bound to their exact existing programme providers.

### Notation and numbered calculations

References to surrounding source sections, notation and numbered calculations retain stable anchors here. Their exact namespaces and correspondence appear in the accompanying manifest. Notation not reproduced in the reader retains its prerequisite status.

### Sources and programme proofs

The human Stacks Project proofs and the AI Integrated Stacks edition are credited in the source notice. Stable invisible anchors retain every included statement, step and equation. Exact source correspondence and conversion checks accompany the reusable converter in the control record.

Existing programme proofs are cited only for the matched claims stated in their provider entries. A written provider retains its actual scope and its own dependencies; this conversion does not certify recursive closure.

- Completion, Theorems 3.1–3.3, 4.1 and 5.1, SHA-256 9f7f25fbff8633dc0ca506a3c2a4992bcb711f2518b8f32a704f8207b7ae7f3e.
- Coefficient rings and the Cohen structure theorem, Theorem 6.1 and its Noetherianity consequence, SHA-256 98155272b26f565ff6c0e0732a740aec5ff70e94d29fa98f127d9e5ca86cc765.
- Henselian local rings and henselization, Sections 4 and 6, Proposition 6.1, SHA-256 b2c6ff73da96c68eb54b3268a98af98f613967255ed6b87778c9133ea8b6a4b3.
- Formally smooth, unramified and étale ring maps, Theorem 3.1 and Sections 4–7, SHA-256 0c84318365e0d1f616a5e28c2a198e787997f83c95a3a6d892c17b3170596564.
- Smooth algebras over a field and the Jacobian criterion, Theorems 5.1–6.1 and Sections 1–3, SHA-256 f904cb9dabe15b90dba190a855f3b27229c8178dffadef82180188a81662ae49.
- Regular sequences, depth and Cohen–Macaulay modules, Propositions 1.1–1.3 and Theorem 6.1, SHA-256 2b5e3bf9f723af5187a07ca9fdc1877d1e1c3d22ccd940dfc47fad0ac8e4417b.
- Regular local rings, Theorem 1.1, SHA-256 5ff9e6d477b256fe256719cf51a334f2eb8d47220d035473f51039daed2eabce.
- Kähler differentials, Theorems 3.1–3.3, Proposition 3.4 and Theorem 7.1, SHA-256 87ad4d3d4984ab9d655490856dabdd1e4eda406f929c3b125857c5e745b530fe.
- Faithful flatness and the local criterion for flatness, Theorems 2.1–3.1, 4.2, 5.2 and 5.4, SHA-256 e101e670904bea5f8310d5fe4e6b5ace3cb68cd8d4942ca680ba808d8c58319e.
- [Lesson 7, Appendix A, Lemma A.3](artin-axioms.md#appendix-a-artin-rees-perturbation-and-graded-quotients), SHA-256 89e51708bd3e115a02841fa9b13782186f4411456a8ed545ab82af72f59ed5aa.

The [complete GNU Free Documentation License 1.2](../licenses/GFDL-1.2.txt) accompanies this modified chapter. The incorporated human-source component is licensed under version 1.2 or any later version, with no Invariant Sections, Front-Cover Texts or Back-Cover Texts.

## History

**Source edition.** *The Stacks Project*, by the Stacks Project authors, with its human-source copyright notice above; distributed in the *AI Integrated Stacks Project*, 2026 edition at revision `565b10e987aba5969b21145a0833f42d69f96790` (30 September 2026). The source publisher is the Stacks Project; the fork distribution and its separately credited AI changes are identified by the pinned repository and its [retained source provenance](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/PROVENANCE.md). The [source application notice](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/introduction.tex) supplies the licence grant, and [the pinned transparent source](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/tree/565b10e987aba5969b21145a0833f42d69f96790) preserves the incorporated source files and their prior network locations.

**Modified course edition.** *Algebraic spaces and stacks — Artin's axioms*, October 2026, published by the Open Math Courses project, `KokunoYumeto/open-math-courses`. Adapted and integrated by GPT-6.1 Sol (OpenAI), Codex, Ultra, 5–6 October 2026. The course integrates the full general Néron desingularization, G-ring permanence and marked-family approximation treatments; independently expressed Artin–Rees perturbation supplies the exact graded comparison. The reader conversion repairs display delimiters and equivalent text controls while preserving formulas and proofs. Source authorship is retained; no AI copyright holder or human endorsement is asserted. The detailed source loci, exact edition and concrete corrections remain in this chapter. Original eligible expression is additionally dedicated to CC0; the complete inseparable modified chapter retains GFDL 1.2-or-later for component export.

**Independent sections and mathematical corrections, 8 October 2026.** The component record delimits the independently written singularity-ideal, presentation, lifting, desingularization, approximation and supporting algebra passages, with their writing credits and CC0 1.0 dedication. The new replacements and corrections are by GPT-6 Astra (OpenAI), Codex, Ultra; the retained full family-approximation proof keeps its earlier writing credit. The symmetric-algebra section proves the correct general relation-module formula and exhibits a counterexample to the unrestricted conormal identification; its projective specialization retains the smooth-presentation applications. The denominator inference in part (6) of the comparison lemma is explicitly identified as unproved. Other incorporated source expression and its notices remain under GFDL 1.2-or-later.
