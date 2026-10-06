# Artin's axioms

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

An algebraic stack has smooth coordinates, whereas a moduli problem usually arrives as a rule assigning a groupoid to each scheme. Artin's criterion constructs coordinates from that rule. The construction has three stages: obtain a versal deformation over a complete local ring, approximate it by a family of finite type, and enlarge its versal locus to an open set. A second argument explains why a flat presentation, even one with inseparable fibres, can be replaced by a smooth presentation.

Read Algebraic stacks first. We use the quotient and bootstrap theorems of The bootstrap theorem, Schlessinger's existence theorem for versal formal objects, the deformation theory of square-zero extensions and the naive cotangent complex, and the commutative algebra of completion and henselization. Precise imported statements appear at the end. All fibre products of groupoids below are 2-fibre products.

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

A Noetherian ring is a **G-ring** if every localization has geometrically regular formal fibres. We use the following approximation theorem without proving its desingularization input.

**Artin approximation.** A regular map of Noetherian rings is a filtered colimit of smooth algebras (Popescu's theorem). If \(B\) is a henselian Noetherian local G-ring, a finite polynomial system over \(B\) with a solution in \(\widehat B\) has, for every \(N\), a solution in \(B\) congruent to it modulo \(\mathfrak m^N\). For a local G-ring which is not henselian, the solution lies in an étale neighbourhood inducing the same residue field. These are [Stacks, Tags 07GC, 07QY and 07QZ].

The object version needed here also preserves associated graded rings.

**Lemma 2.3 (approximating a family).** Let \(\mathcal X\) be limit preserving on objects. Let \(x_R\in\mathcal X(R)\), where \(R\) is as in (2.2), and let \(s\) be the image of its closed point in \(S\). If \(\mathcal O_{S,s}\) is a G-ring, then, for every \(N\), there are a finite type \(S\)-algebra \(A\), a maximal ideal \(\mathfrak n\), and \(x_A\in\mathcal X(A)\), together with

\[
A/\mathfrak n^N\simeq R/\mathfrak m^N,\qquad
x_A|_{A/\mathfrak n^N}\simeq x_R|_{R/\mathfrak m^N},\qquad
\operatorname{gr}_{\mathfrak n}A\simeq
\operatorname{gr}_{\mathfrak m}R.
\tag{2.3}
\]

**Proof.** Work over \(\operatorname{Spec}\Lambda\subset S\). Limit preservation descends \(x_R\) to a finitely generated \(\Lambda\)-algebra \(C\) with a map \(C\to R\). Lift generators of the finite residue extension and generators of \(\mathfrak m/\mathfrak m^2\) to \(R\). They give a surjection \(P\twoheadrightarrow R\), where \(P\) is the completion of a localization of a polynomial \(\Lambda\)-algebra at a maximal ideal. Write its kernel as \((b_1,\ldots,b_r)\), and choose a matrix \(K\) of generators of the relations among the \(b_i\).

Choose lifts \(a_i\in P\) of the images of generators of \(C\). If \(C=\Lambda[y_1,\ldots,y_u]/(f_j)\), choose coefficients \(c_{ji}\) with

\[
f_j(a)=\sum_i c_{ji}b_i,\qquad
K(b_1,\ldots,b_r)^{\mathsf t}=0.
\tag{2.4}
\]

These are finitely many polynomial equations. The local polynomial ring underlying \(P\) is a G-ring, by permanence under essentially finite type extensions. Choose the approximation order larger than both the required \(N\) and Artin–Rees constants for
\(P^{\oplus t}\to P^{\oplus r}\to P\).
Approximation gives \(a_i',b_i',c_{ji}',K'\) in an étale neighbourhood \(B\), with the same equations and the prescribed congruences in \(P=\widehat{B_{\mathfrak n}}\). Set \(A_1=B/(b_i')\). Equations (2.4) give \(C\to A_1\), hence the object.

The congruences give equality modulo order \(N\). The finite-complex Artin–Rees perturbation lemma [Stacks, Tags 07VE and 07VF] says that the images of the two perturbed relation maps have identical initial submodules. Applying it to the displayed presentation identifies the associated graded quotient rings. This explains why one approximates the relations as well as the generators of the ideal.

The construction is initially essentially of finite type. Express \(A_1\) as a filtered localization of finite type algebras and descend its object to one stage. That stage has the same local ring at the selected point, so retains all three conclusions of (2.3). \(\square\)

*Reference:* [Stacks, Tag 07XB]. The cited finite-complex lemma is an input from commutative algebra, not an algebraicity criterion.

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

*Reference:* [Stacks, Tags 06FG and 06FI]. This completes the flat-groupoid theorem used as a stated forward reference in Quotient stacks and Deligne–Mumford stacks, including examples such as \(B\mu_p\).

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

## What this lesson does not prove

All four acceptance results—Artin's space and stack criteria, openness from naive obstruction theories, and algebraicity of flat groupoid quotients—have been proved above. The product-compatible obstruction criterion and the stronger-effectiveness criterion have also been proved. The imported inputs are:

- Schlessinger's existence theorem for a versal formal object in a predeformation category satisfying (S1), (S2), and finite-dimensional tangent space [Stacks, Tag 06IW], and its field-change, linearity and small-extension tests. These are the assigned formal-deformation prerequisites. The cotangent obstruction to lifting a ring map, the regular-immersion conormal calculation and square-zero flatness criterion are the assigned deformation prerequisites; the space versions are obtained on étale charts [Stacks, Tags 06CB, 06CC and 06BH].
- Popescu's desingularization and Artin approximation as stated in Section 2.3 [Stacks, Tags 07GC, 07QY and 07QZ]. We also import permanence of G-rings under essentially finite type extensions [Stacks, Tag 07PV], and the exact finite-complex Artin–Rees perturbation statements [Stacks, Tags 07VE and 07VF].
- The ordinary-scheme Artinian smoothness test [Stacks, Tag 02HX], étale lifting over henselian local rings, finite presentation descent along affine limits, scheme Zariski main and idempotent lifting from the earlier lessons. The openness criteria for unramified and lci families with flat finitely presented source and target, and the Cohen–Macaulay slicing inputs, have their precise space or scheme formulations in [Stacks, Tags 05X8, 06CE, 045U and 0570].
- The Noetherian topological statements in Section 5.1 [Stacks, Tags 0G2F and 0G2R]; coherent cohomology finiteness and the dimension bound; perfect direct image with arbitrary base change [Stacks, Tag 0B91]; and Grothendieck existence for proper schemes [Stacks, Tag 088C; the proper-support extension is Tag 088E]. Existence is used with all its morphisms. Its conversion from coherent sheaves to invertible sheaves was proved in Section 7.

The general pushout theorem for algebraic stacks along arbitrary affine thickenings [Stacks, Tag 07WM] is mentioned as a stronger statement. The Artinian assertion needed here was proved in Lemma 1.2. The general theorem's flat-space patching input is not developed in this lesson.

## References

- **[Stacks]** The Stacks project, *Artin's Axioms*: Tags 07T0, 07T2, 07WM, 06L9, 07WT, 07WW, 07WY, 07X3, 07XA, 07XK, 07XD, 07XP, 07XJ, 07XZ, 07Y0, 07Y1, 07Y3, 07Y4, 07Y5, 0CXN, 0CXR, 07Y6, 07YF, 07YG, 0CYF, 07YJ, 07YP, 07YT and 07YU. Read the chapter in [AI Integrated Stacks Project, Artin's Axioms](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/artin.html).
- **[Stacks]** *Criteria for Representability*: Tags 05XF, 05XH, 06CT, 06CZ, 06D4, 05XX, 06DB, 06DC, 06FG and 06FI, and the finite Hilbert and restriction-of-scalars constructions used in Section 6. See [AI Integrated Stacks Project, Criteria for Representability](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/criteria.html).
- **[Stacks]** *Smoothing Ring Maps*, Tags 07GC, 07QY and 07QZ; *More on Algebra*, Tags 07PV, 07VE and 07VF; *Formal Deformation Theory*, Tag 06IW; and the scheme-theory inputs listed above. See [AI Integrated Stacks Project, Smoothing Ring Maps](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/smoothing.html). AI Integrated Stacks Project retains the upstream tags; its additions and corrections are not reviewed by the Stacks project's maintainers.
- **[EGA]** A. Grothendieck, with J. Dieudonné, *Éléments de géométrie algébrique III*, Theorem 5.1.5, for the existence theorem invoked through its proper-scheme form in [Stacks, Tag 088C].
