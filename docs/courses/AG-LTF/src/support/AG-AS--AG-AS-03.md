# Properties and morphisms of algebraic spaces

*Algebraic spaces and stacks, Lesson 3 of 12.*

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

An algebraic space has an étale chart by a scheme, but that chart need not have a Zariski-local inverse. We therefore need two kinds of locality. Its underlying topological space describes open subspaces and specializations. Its small étale site carries the structure sheaf and modules. These constructions also let us formulate properness without assuming that a neighbourhood of each point is a scheme.

We use the quotient theorem from *Algebraic spaces* and the bootstrap and scheme-recognition results from *The bootstrap theorem*. Scheme theory, including faithfully flat descent of quasi-coherent modules and the elementary scheme properties of étale morphisms, is prerequisite material. The scheme inputs used below are listed precisely at the end. Algebraic spaces and all their fibre products are considered over a fixed base scheme \(S\).

## 1. Points and open subspaces

### 1.1. Field-valued points

A field-valued point of \(X\) is a morphism \(a:\operatorname{Spec}K\to X\). Two such points \(a:\operatorname{Spec}K\to X\) and \(b:\operatorname{Spec}L\to X\) are equivalent if there is a field \(\Omega\), embeddings \(K\to\Omega\) and \(L\to\Omega\), and equality of the resulting morphisms \(\operatorname{Spec}\Omega\to X\). Write \(|X|\) for the set of equivalence classes. Equality here includes the morphisms of fields; it does not mean merely that a symmetry fixes an ordinary point of a chart.

**Proposition 1.1 (points and topology).** The construction \(|X|\) is a well-defined set and is functorial in \(X\). For a scheme it gives its usual points. There is a topology on \(|X|\), independent of the chosen presentation, for which every étale surjection \(U\to X\) from a scheme induces an open, continuous surjection

\[
|U|\longrightarrow |X|.
\tag{1.1}
\]

Every morphism of algebraic spaces induces a continuous map of these spaces. Every étale morphism induces an open map.

**Proof.** Reflexivity and symmetry of the field-point relation are immediate. For transitivity, suppose that the equivalence of \(a\) and \(b\) is witnessed over \(\Omega_1\), and that of \(b\) and \(c\) over \(\Omega_2\). The tensor product \(\Omega_1\otimes_L\Omega_2\) is nonzero because extensions of fields are faithfully flat. Choose a prime of this tensor product and then the fraction field of the resulting domain. Both \(\Omega_i\) embed into this field, and the three morphisms become equal there. Thus the relation is transitive. Composition with a morphism \(X\to Y\) preserves the relation, giving functoriality.

For a scheme \(T\), a field-valued morphism factors through the spectrum of the residue field of its image point. Two morphisms are equivalent precisely when their image points agree: the reverse implication follows by taking a common field extension of the two residue-field extensions. Hence this definition agrees with the usual set \(|T|\).

Choose an étale surjection \(q:U\to X\), and put \(R=U\times_XU\). If \(a:\operatorname{Spec}K\to X\), then \(U\times_X\operatorname{Spec}K\) is a nonempty étale scheme over \(K\). A point of it has residue field finite separable over \(K\), so \(a\) is equivalent to the image of a point of \(U\). Consequently \(|U|\to|X|\) is surjective. Two points of \(U\) have the same image exactly when they are the two images of a point of \(R\): equality after a field extension provides a point of the fibre product, and a point of the fibre product supplies that equality. Therefore \(|X|\) is the quotient of the set \(|U|\) by this relation. This also proves that it is a set, rather than a proper class of field-valued morphisms.

Give \(|X|\) the quotient topology: a subset \(W\) is open when \(q^{-1}(W)\) is open in \(U\). If \(A\subset |U|\) is open, its saturation is

\[
q^{-1}(q(A))=t(s^{-1}(A)),
\tag{1.2}
\]

where \(s,t\colon R\rightrightarrows U\) are the two projections. Both are étale and hence open as morphisms of schemes. The right side is open, so \(q(A)\) is open. This proves the openness in (1.1).

Suppose \(V\to X\) is another étale scheme atlas. The scheme \(U\times_XV\) maps étale and surjectively to both atlases. An open surjection of topological spaces is a quotient map. Pulling the proposed open set back to this common refinement shows that the two quotient topologies agree. The same argument, without requiring \(V\to X\) to be surjective, shows that every étale scheme chart maps openly and continuously to \(|X|\).

For \(f:X\to Y\), choose a scheme atlas \(V\to Y\), then a scheme atlas \(U\to X\times_YV\). The composite \(U\to X\) is an étale surjection. The map \(U\to V\) is a morphism of schemes, so the inverse image in \(U\) of an open of \(|Y|\) is open. Since \(|U|\to|X|\) is a quotient map, \(|f|\) is continuous. If \(f\) is étale, \(U\to V\) is étale: \(X\times_YV\to V\) is étale and \(U\) is an étale chart. For an open \(A\subset |X|\), its pullback to \(U\) is open, and its image in \(|Y|\) is the composite image through \(V\). Both maps in that composite are open. The surjectivity of \(U\to X\) identifies the image with \(f(A)\). Thus \(f\) is open. \(\square\)

There is a useful fibre-product consequence. For \(X\to Z\leftarrow Y\), the natural map

\[
|X\times_ZY|\longrightarrow |X|\times_{|Z|}|Y|
\tag{1.3}
\]

is surjective: representatives whose images in \(Z\) agree can be put over a common field, and then define a point of the fibre product. It need not be injective. For example, \(\operatorname{Spec}\mathbf C\times_{\operatorname{Spec}\mathbf R}\operatorname{Spec}\mathbf C\) has two points, while both factors have one point. This distinction matters when using topological fibres.

**Proposition 1.2 (opens).** Open subsets of \(|X|\) correspond bijectively to open subspaces of \(X\), meaning subfunctors represented after every scheme base change by open subschemes.

**Proof.** For an open \(W\subset|X|\), let \(U_W\subset U\) be its inverse image in an atlas. It is saturated by (1.2). The restricted relation has both endpoints in \(U_W\), and its quotient \(X_W\) exists by the quotient theorem of *Algebraic spaces*. Its map to \(X=U/R\) pulls back along \(U\to X\) to \(U_W\to U\): saturation says that every arrow whose one endpoint is in \(U_W\) has its other endpoint there. The descent argument for opens in that theorem then makes \(X_W\to X\) an open immersion. Its underlying image is exactly \(W\).

Conversely, an open subspace pulls back to an open of every atlas. Its point set is therefore open by Proposition 1.1. Two such subspaces with the same point set have the same open subscheme in an atlas, and equality descends, proving uniqueness. \(\square\)

We shall use *quasi-compact* for a morphism \(X\to Y\) whose inverse image over every affine scheme \(T\to Y\) is a quasi-compact algebraic space. For a space, quasi-compactness can equally be read from \(|X|\). Here is the small verification needed later. The images of affine opens in a scheme atlas are open and quasi-compact, by continuity and openness. If \(|X|\) is quasi-compact, finitely many such images cover it, and the corresponding finite disjoint union of affine schemes is an affine étale surjection onto \(X\). Conversely an affine étale surjection has quasi-compact image \(|X|\).

It suffices to test the morphism condition on the affine pieces \(V_i\) of one étale atlas of \(Y\). Suppose \(X\times_YV_i\) is quasi-compact for each \(i\), and choose an affine atlas of each of these spaces. For an arbitrary affine \(T\to Y\), finitely many affine opens \(W_j\) of the schemes \(T\times_YV_i\) have images covering \(T\), because these images form an open cover of the quasi-compact space \(T\). Each \(X\times_YW_j\) is quasi-compact: base change its chosen affine atlas along the morphism of affine schemes \(W_j\to V_i\), obtaining an affine atlas. These finitely many spaces cover \(X\times_YT\) étale and surjectively, so their quasi-compact point spaces have quasi-compact union image. This proves the condition for every \(T\). It also proves chart independence and base-change stability. Compatibility with schemes is their ordinary affine-local quasi-compactness criterion.

*References:* [Stacks, Tags 03BT and 03BU], and the surrounding section on points in [AI Integrated Stacks Project, Properties of Algebraic Spaces](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/spaces-properties.html).

### 1.2. Decency and residue fields

We use the following form of the definition in [Stacks, Tag 03I8]. An algebraic space \(X\) is **decent** if every point \(x\in|X|\) is represented by a **quasi-compact monomorphism** \(\operatorname{Spec}\kappa(x)\to X\) from a field. Quasi-compactness is part of this definition. A general field-valued representative is not required to be a monomorphism, and a monomorphism without the finiteness requirement is not the definition of decency.

Whenever a point is represented by a field-spectrum monomorphism, its field and that monomorphism are unique up to unique isomorphism. We verify this directly. First, a nonempty scheme \(P\) with a monomorphism \(P\to\operatorname{Spec}K\) is \(\operatorname{Spec}K\). On a nonempty affine open \(\operatorname{Spec}B\subset P\), the map \(K\to B\) is faithfully flat and

\[
B\otimes_KB\xrightarrow{\sim}B
\]

because the morphism is a monomorphism. Faithfully flat descent of this isomorphism gives \(K\xrightarrow{\sim}B\). Every other nonempty affine open satisfies the same conclusion; they meet the first one, since two disjoint opens would give two different \(K\)-points after a common field extension. Thus there is just this one open, and \(P=\operatorname{Spec}K\).

Now, if \(\operatorname{Spec}K\to X\) and \(\operatorname{Spec}L\to X\) are monomorphisms representing the same point, their fibre product is a nonempty scheme and is a monomorphism over each field. It is therefore the spectrum of each field, giving the required unique isomorphism. More generally, any field-valued representative of their point factors uniquely through this monomorphism: its fibre product with the monomorphism is a nonempty monomorphism over its own field, hence is that field's spectrum. For decent spaces this justifies the notation \(\kappa(x)\), without imposing it on all algebraic spaces.

For an explicit failure, let

\[
X=\mathbf A^1_{\mathbf Q}/\mathbf Z,
\qquad n\cdot x=x+n.
\tag{1.4}
\]

Its étale relation is the disjoint union of the translation graphs. The proof in *Algebraic spaces*, Lemma 5.1 and Section 5.3, shows that the image of the generic point cannot factor through a field-spectrum monomorphism. To recall the mechanism, a component of a \(\mathbf Z\)-torsor over a field is a finite separable field extension; its stabilizer is its finite Galois group. A hypothetical monomorphism representing this generic point would, after pullback to the affine line, force the chosen component field to be \(\mathbf Q(x)\). Its finite stabilizer in the torsion-free group \(\mathbf Z\) is trivial, forcing the representative field also to be \(\mathbf Q(x)\). But

\[
\operatorname{Spec}\mathbf Q(x)\times_X
\operatorname{Spec}\mathbf Q(x)
\simeq\coprod_{n\in\mathbf Z}\operatorname{Spec}\mathbf Q(x)
\]

is not the diagonal. Thus the map is not a monomorphism. The factorization property just proved makes this an obstruction to *any* field-spectrum monomorphism representing that point. In particular \(X\) is not decent [Stacks, Tag 03ID].

## 2. The small étale site and modules

### 2.1. The site and a presentation of a sheaf

The **small étale site** \(X_{\mathrm{\acute et}}\) has schemes \(T\) with an étale morphism \(T\to X\) as objects. Its arrows are morphisms over \(X\), and its coverings are jointly surjective families of étale morphisms. Fibre products of objects are schemes, because the diagonal of \(X\) is representable by schemes, and are again étale over \(X\).

In fact every arrow \(T_1\to T_2\) of this site is étale. Its graph is a section of the étale projection \(T_1\times_XT_2\to T_1\), so it is an open immersion; the other projection to \(T_2\) is étale. This also verifies stability of coverings under pullback. Notice that \(X\) itself is an object of this scheme-valued site only when it is a scheme.

One can instead allow algebraic spaces étale over \(X\) as objects. This site has \(X\) as a final object and has the same sheaves as the scheme-valued site. Here is an explicit comparison. For a sheaf \(F\) on the latter and an étale algebraic space \(Z\to X\), choose a scheme atlas \(V\to Z\) and set

\[
F(Z)=\operatorname{Eq}\bigl(F(V)\rightrightarrows F(V\times_ZV)\bigr).
\tag{2.1}
\]

Both terms are values on objects of the scheme-valued site. If a second atlas is used, pull both atlases back to their common refinement. The sheaf condition for its two surjections shows that compatible sections on one atlas are precisely compatible sections on the common refinement, and hence on the other atlas. This gives canonical, mutually inverse identifications in (2.1). A morphism \(Z'\to Z\) induces a restriction map by pulling the atlas back and then using a scheme atlas of that pullback. The same comparison makes this map independent of the choices and compatible with composition. Finally, a covering by algebraic spaces can be refined by scheme atlases; the ordinary sheaf condition on that refinement gives the sheaf condition on the larger site. Conversely every sheaf on the larger site has (2.1) as its value, since \(V\to Z\) is a covering. This proves the comparison.

In particular, arbitrary morphisms \(f:X\to Y\) can be treated functorially on étale sites: base change of an étale algebraic space over \(Y\) is an étale algebraic space over \(X\), and covers and fibre products are preserved. The comparison then returns to the scheme-valued sites. It avoids the mistaken assumption that \(X\times_YT\) must be a scheme for every scheme \(T\to Y\).

Fix a presentation \(q:U\to X\), with \(R=U\times_XU\). Write \(s,t\colon R\rightrightarrows U\), with an arrow oriented from \(s\) to \(t\). A sheaf on \(X_{\mathrm{\acute et}}\) restricts to a sheaf \(F_U\) on \(U_{\mathrm{\acute et}}\), together with an isomorphism

\[
\alpha:s^*F_U\xrightarrow{\sim}t^*F_U
\tag{2.2}
\]

on \(R\). It is the identity along the unit and is compatible with composition: transporting along two composable arrows equals transporting along their composite. Equivalently its three pullbacks to \(U\times_XU\times_XU\) satisfy the usual cocycle equation.

Conversely these data determine a sheaf on \(X\). For an object \(T\to X\), the scheme \(T_U=T\times_XU\) is an object of \(U_{\mathrm{\acute et}}\). Define its sections to be those sections of \(F_U(T_U)\) whose two restrictions to \(T\times_XR\) agree after applying \(\alpha\). The unit and cocycle give a well-defined descent condition. For a covering \(\{T_i\to T\}\), the pulled-back family covers \(T_U\). The sheaf condition for \(F_U\) uniquely glues compatible sections, and their descent condition can be checked on this covering of \(T\times_XR\). Thus the constructed functor is a sheaf. When \(T\to X\) factors through \(U\), its induced cover \(T_U\to T\) has a section, and the descent condition identifies these sections with \(F_U(T)\). This proves that the reconstruction returns \(F_U\) and its isomorphism. The sheaf condition for \(T_U\to T\) proves that restriction followed by reconstruction returns the original sheaf on \(X\). Morphisms are reconstructed by the same equalizers, so this is an equivalence of categories.

The **structure sheaf** is

\[
\mathcal O_X(T)=\Gamma(T,\mathcal O_T).
\tag{2.3}
\]

It is a sheaf of rings by scheme descent of regular functions. An \(\mathcal O_X\)-module is a sheaf of modules over this sheaf of rings. Formula (2.2) applies to such modules, with the module structures included.

*Reference:* [Stacks, Tag 03EB], the section on the small étale site.

### 2.2. Quasi-coherent modules and effective descent

A module \(\mathcal F\) on this site is **quasi-coherent** if its restriction to every scheme chart \(T\to X\) is the étale sheaf associated to a quasi-coherent \(\mathcal O_T\)-module. These restrictions are cartesian: for an arrow \(a:T'\to T\), their transition is the canonical isomorphism \(a^*\mathcal F_T\simeq\mathcal F_{T'}\). Equivalently, it locally has a presentation by free \(\mathcal O_X\)-modules, with arbitrary sets of generators and relations. On a scheme these descriptions agree with the usual Zariski notion, by scheme quasi-coherent descent.

**Theorem 2.1 (quasi-coherent descent and the abelian category).** For every scheme atlas \(U\to X\), restriction is an equivalence

\[
\operatorname{QCoh}(X)\simeq
\left\{(M,\alpha):M\in\operatorname{QCoh}(U),\quad
\alpha:s^*M\xrightarrow{\sim}t^*M\text{ satisfies the cocycle}\right\}.
\tag{2.4}
\]

The category \(\operatorname{QCoh}(X)\) is abelian. Kernels and cokernels are those computed in the category of all \(\mathcal O_X\)-modules.

**Proof.** Restriction of a quasi-coherent module gives \(M\) and the canonical isomorphism \(\alpha\). The equality \(q\circ s=q\circ t\) gives the isomorphism; functoriality of pullback gives its cocycle and unit conditions.

For the converse, take \(M\) and \(\alpha\). For every scheme \(T\to X\) étale, pull \(M\) to \(T_U=T\times_XU\). The double overlap is \(T\times_XR\), so \(\alpha\) gives a descent datum for the surjective étale morphism \(T_U\to T\). Scheme faithfully flat descent of quasi-coherent modules [Stacks, Tag 023T] gives a quasi-coherent module \(M_T\) on \(T\), with a specified isomorphism of its pullback with this datum. This use requires no quasi-compactness of the entire atlas: over each affine open in \(T\), finitely many affine opens of \(T_U\) cover it, and give a faithfully flat finite-presentation affine cover. Descent on these covers, and unique gluing on their overlaps, is exactly the scheme theorem.

For \(a:T'\to T\), the pullback of the descent datum on \(T_U\) is the datum already constructed on \(T'_U\). The fully faithful part of scheme descent therefore gives a unique isomorphism

\[
c_a:a^*M_T\xrightarrow{\sim}M_{T'}.
\tag{2.5}
\]

For two successive arrows, the two proposed composite isomorphisms have the same pullback to their atlas. Faithfulness forces them to be equal. The identity arrow is handled in the same way. Thus these modules and isomorphisms form a cartesian system, rather than a collection of unrelated descended modules.

Set \(\mathcal F(T)=\Gamma(T,M_T)\), using (2.5) for restriction. For a covering of \(T\), the module systems pull back from \(M_T\); scheme descent of sections gives the sheaf condition. Its restriction to each chart is the étale sheaf of \(M_T\), so it is quasi-coherent. If \(T\to X\) factors through \(U\), the pulled-back datum is the canonical datum of the pullback of \(M\). Full faithfulness of scheme descent identifies \(M_T\) with that module, and the identifications recover \(\alpha\). Starting instead with \(\mathcal F\), scheme descent identifies its chart restrictions with the \(M_T\) just constructed. Their transition maps agree by faithfulness, so the resulting sheaf is \(\mathcal F\). A morphism \(M\to N\) commuting with \(\alpha\) descends on every \(T\); uniqueness gives compatibility with (2.5). This verifies both inverse functors and the assertion on morphisms.

It remains to check that this category is abelian. On \(U\), let \(u:M\to N\) commute with the descent isomorphisms. Its kernel \(K\) and cokernel \(C\) are quasi-coherent scheme modules. Since \(s,t\) are étale and hence flat, their pullback functors are exact. The isomorphisms on \(M,N\) therefore induce isomorphisms on \(K,C\); their unit and cocycle equations follow by functoriality of kernel and cokernel. Thus \(K,C\) descend by (2.4). Restriction to a chart is exact and detects zero sheaves: a section which vanishes on the atlas cover vanishes by the sheaf axiom. Consequently the descended objects are the kernel and cokernel in all module sheaves. Finite direct sums also descend. Finally the canonical coimage-to-image map becomes an isomorphism on \(U\), where quasi-coherent modules form an abelian category, and hence is an isomorphism on \(X\). This proves the assertion. \(\square\)

The proof shows independence of the presentation: two atlases have a common refinement, and their categories in (2.4) identify with the same category of sheaves on \(X\). It also describes pullback under an arbitrary \(f:X\to Y\): on charts use the ordinary tensor-product pullback of quasi-coherent modules, and descend its canonical overlap identifications. Pullback need not be exact for an arbitrary \(f\); the exactness above came from the flat maps \(s,t\).

**Example 2.2 (a free finite quotient).** If a finite constant group \(G\) acts freely on \(U\), then \(R=G\times U\). An isomorphism \(\alpha\) on \(R\) is a collection of transports along the action maps, with the multiplication equation imposed by the cocycle. Thus quasi-coherent modules on \(U/G\) are exactly \(G\)-equivariant quasi-coherent modules on \(U\). There is no division by \(|G|\) in this statement, even when the characteristic divides that order.

*References:* [Stacks, Tags 03G5 and 03M3].

## 3. Properties seen through charts

### 3.1. Properties of spaces

Let \(\mathcal P\) be a property of schemes that is preserved by étale morphisms and descends under surjective étale coverings. Say that \(X\) has \(\mathcal P\) when a scheme atlas has \(\mathcal P\). This does not depend on the atlas. Indeed, for atlases \(U,V\to X\), the scheme \(U\times_XV\) inherits the property from \(U\) and covers \(V\) étale, so \(V\) inherits it by descent. The same argument works for every étale scheme chart, even one that is not surjective. If \(X\) is a scheme, the definition agrees with the original one.

In particular this defines the following properties, with their usual scheme meanings:

| Property of \(X\) | Test on an étale scheme atlas \(U\) |
| --- | --- |
| Locally Noetherian | Every point of \(U\) has a Noetherian affine neighbourhood. |
| Reduced | The local rings of \(U\) have no nonzero nilpotents. |
| Normal | Every local ring of \(U\) is an integrally closed domain. |
| Regular | Every local ring of \(U\) is a Noetherian regular local ring. |

Here normality does not include an implicit Noetherian hypothesis. The ascending scheme facts we use are that a smooth algebra over a reduced ring is reduced, and a smooth algebra over a normal ring is normal [Stacks, Tags 033B and 033C]. They apply, in particular, to étale maps at arbitrary generality. Their descent parts can be checked directly. A faithfully flat local map \(A\to B\) is injective. If \(B\) is reduced, this proves that \(A\) is reduced. If \(B\) is a normal domain, \(A\) is a domain. For \(z=a/b\in\operatorname{Frac}A\) integral over \(A\), its image is integral over \(B\), hence belongs to \(B\). Thus \(a\in bB\cap A=bA\), where the last equality is faithfully flat descent of the quotient \(A/bA\to B/bB\). It follows that \(z\in A\). Applying this to local rings at points above a given point proves normality descends. Together with the stated ascending facts, this proves that reducedness and normality are étale local.

Locally Noetherian schemes are preserved by finite-presentation morphisms, so by étale maps. For descent, a faithfully flat local map to a Noetherian local ring makes every ideal in the source finitely generated: extend the ideal, choose finitely many of its original elements generating the extension, and contract the equality using faithful flatness. Affine neighbourhoods can instead use a finite affine étale cover and the same argument for its product algebra. This proves the locality of the locally Noetherian property [Stacks, Tag 034C].

For regularity, at an étale local map of Noetherian local rings \((A,\mathfrak m)\to(B,\mathfrak n)\), the fibre is a finite separable field extension and \(\mathfrak n=\mathfrak mB\). Flatness gives

\[
(\mathfrak m/\mathfrak m^2)\otimes_{\kappa(A)}\kappa(B)
\simeq\mathfrak n/\mathfrak n^2,
\qquad \dim A=\dim B.
\tag{3.1}
\]

The cotangent-space formula follows by tensoring \(\mathfrak m/\mathfrak m^2\) with the flat algebra and then with the residue field; the dimension equality is the scheme dimension theorem for flat local maps with zero-dimensional fibre. Thus embedding dimension equals Krull dimension for one ring precisely when it does for the other. Coupled with the Noetherian locality just proved, this proves regularity is étale local; compare [Stacks, Tag 036D].

### 3.2. Properties of morphisms

For \(f:X\to Y\), choose a scheme atlas \(V\to Y\) and a scheme atlas \(U\to X\times_YV\). We obtain a scheme morphism

\[
U\longrightarrow V.
\tag{3.2}
\]

For scheme morphism properties that are étale local on both source and target, define the property of \(f\) by (3.2). This applies to flat, locally of finite type, locally of finite presentation, smooth, étale, and unramified. The needed scheme locality statements, including the distinction between source and target, are among [Stacks, Tags 02KX, 02KY, 02L2, 02VL, 02VM, 02VN, 036K, 036N, 036O, 036U, 036W and 03YV].

To verify independence, first fix \(V\). Two atlases of \(X\times_YV\) have an étale common refinement, so scheme source-locality compares their maps to \(V\). For two target atlases \(V,V'\), use \(V\times_YV'\), a scheme étale over both, and a scheme atlas of its base change with \(X\). Scheme base-change stability and target descent compare the two choices. This argument also proves arbitrary base-change stability of the resulting properties of algebraic-space morphisms: refine a chart of the new target with the pullback of \(V\), then apply the scheme assertion. It agrees with the usual definition when \(f\) is representable by schemes, since in that case \(X\times_YV\) is itself a scheme.

A morphism is **of finite type** if it is locally of finite type and quasi-compact. Do not remove the quasi-compactness condition by testing only the local map (3.2). Likewise **of finite presentation** includes quasi-compactness and quasi-separatedness in addition to local finite presentation.

Separatedness and properness require a different test. They cannot be inferred merely by checking that \(U\to V\) is separated or proper for an arbitrary source atlas. They will be defined intrinsically in the next section. The sign-identification space in Section 6 has a separated affine scheme atlas over the base field, yet its own diagonal is not even an immersion.

## 4. The diagonal and properness

For a morphism \(f:X\to Y\), its relative diagonal

\[
\Delta_f:X\longrightarrow X\times_YX
\tag{4.1}
\]

is representable by schemes: equality of two \(X\)-sections of a scheme is represented by the diagonal of \(X\), and equality automatically respects their fixed \(Y\)-section. It is a monomorphism. We call \(f\) **separated** if \(\Delta_f\) is a closed immersion, **locally separated** if it is an immersion, and **quasi-separated** if it is quasi-compact. These definitions agree with those for schemes. The conditions are invariant under arbitrary base change because the new diagonal is a base change of (4.1).

**Lemma 4.1 (the diagonal has small fibres).** For every morphism of algebraic spaces, \(\Delta_f\) is separated, locally of finite type, and locally quasi-finite.

**Proof.** Choose a scheme atlas \(U\to X\). The pullback of \(\Delta_f\) by the étale surjection \(U\times_YU\to X\times_YX\) is

\[
U\times_XU\longrightarrow U\times_YU,
\tag{4.2}
\]

a morphism of schemes. Over the second copy of \(U\), its composite to \(U\) is étale, hence locally of finite type. The elementary permanence rule for finite type [Stacks, Tag 01T8] then makes (4.2) locally of finite type. It is a monomorphism and so has at most one geometric point in every geometric fibre. A locally finite-type scheme morphism with such fibres is locally quasi-finite. A monomorphism is separated, since its own diagonal is an isomorphism. Each of these properties descends under the étale target cover, proving the lemma. \(\square\)

A map \(f\) is **universally closed** if every base change has a closed map on underlying topological spaces. It suffices to test scheme base changes: for an algebraic-space base change, pull back to a scheme atlas of its target. Closed subsets are detected on that atlas by the quotient topology. Formula (1.3) shows that the image of the pulled-back closed subset is exactly the inverse image of the original image, so closedness descends. An arbitrary scheme base change can then be tested on affine opens.

By definition, \(f\) is **proper** if it is separated, of finite type, and universally closed. This agrees with scheme properness and its representable extension. In particular proper morphisms are quasi-separated, since a closed immersion is quasi-compact.

**Proposition 4.2 (testing separation on a presentation).** For atlases \(V\to Y\), \(U\to X\times_YV\), put \(R=U\times_{X\times_YV}U\). The morphism \(f\) is separated, locally separated, or quasi-separated exactly when the scheme map \(R\to U\times_VU\) is respectively a closed immersion, an immersion, or quasi-compact.

**Proof.** This is the pullback of the relative diagonal by the scheme étale cover \(U\times_VU\to X\times_YX\) after base change to \(V\). The respective scheme properties are local under these covers: closed immersions and quasi-compactness are fpqc local on the target, and immersions are fppf local [Stacks, Tags 02L6, 02KQ and 02YM]. Base-change stability gives one implication and target descent gives the other. \(\square\)

Thus an endpoint map on a relation detects separation. It is not enough that the projections \(R\to U\) are étale.

## 5. The valuative criterion

This section proves the criterion at finite type and quasi-separated generality. The essential arguments concern arbitrary valuation rings, with no Noetherian, rank-one, or discreteness restriction.

### 5.1. The two kinds of lift

Let \(A\) be a valuation ring and \(K=\operatorname{Frac}A\). A valuative square for \(f\) consists of maps

\[
a:\operatorname{Spec}K\to X,\qquad
b:\operatorname{Spec}A\to Y,\qquad f a=b|_{\operatorname{Spec}K}.
\tag{5.1}
\]

The **ordinary uniqueness condition** says that there is at most one morphism \(\operatorname{Spec}A\to X\) extending \(a\) over \(b\). The **extended existence condition** says that there are a field extension \(K'/K\), a valuation ring \(A'\subset K'\) with fraction field \(K'\) which dominates \(A\), and a lift \(\operatorname{Spec}A'\to X\) of the square after extension. To dominate means

\[
A\subset A',\qquad \mathfrak m_{A'}\cap A=\mathfrak m_A.
\tag{5.2}
\]

In this situation \(A'\cap K=A\): an element \(c\in K\setminus A\) has inverse in \(\mathfrak m_A\), so cannot belong to \(A'\). The **extended valuative criterion** combines extended existence with ordinary uniqueness. The **ordinary criterion** asks for a unique lift over \(A\) itself. These are the conventions of [Stacks, Tag 0CKZ].

All these conditions are preserved by base change. Indeed a generic lift and a map from the valuation ring to a new target can be composed to a square for \(f\). Its solution, together with the fixed map to the new target, defines the solution in the fibre product. The same observation handles uniqueness.

**Lemma 5.1 (uniqueness from separation).** A separated morphism satisfies ordinary uniqueness. More generally, two maps from the spectrum of a domain to \(X\), over the same map to \(Y\), which agree on its fraction field are equal.

**Proof.** Their equality functor is the pullback of \(\Delta_f\), hence is a closed subscheme of the domain's spectrum. It contains the generic point as a scheme: its defining ideal becomes zero in the fraction field. An ideal in a domain which becomes zero there is already zero. The equality subscheme is consequently the whole spectrum. \(\square\)

### 5.2. Extended existence and closed images

**Lemma 5.2.** If \(f:X\to Y\) is quasi-compact and satisfies extended existence, then it is universally closed.

**Proof.** Existence and quasi-compactness persist after base change. We may therefore replace the target by an arbitrary affine scheme \(\operatorname{Spec}D\). Let \(C\subset |X|\) be closed. Choose an affine scheme atlas \(U=\operatorname{Spec}B\to X\), which exists by the quasi-compactness discussion following Proposition 1.2. Its inverse image of \(C\) is the point set of a closed subscheme \(Z\subset U\). In particular \(Z\) is affine. The image of \(C\) in \(\operatorname{Spec}D\) is the image of \(Z\).

We first show that this image is stable under specialization. Let \(y'\) belong to it and let \(y\) be a specialization of \(y'\). Choose \(x'\in C\) above \(y'\) and a field-valued representative with field \(L\). Write \(\mathfrak p'\subset\mathfrak p\) for the two primes of \(D\). The local domain

\[
E=(D/\mathfrak p')_{\mathfrak p}
\]

embeds into \(\kappa(y')\), hence into \(L\). There is a valuation ring \(A\subset L\) with fraction field \(L\) dominating \(E\) [Stacks, Tag 00IA]. The resulting map \(\operatorname{Spec}A\to\operatorname{Spec}D\) sends the generic point to \(y'\) and the closed point to \(y\). Apply extended existence to the generic representative of \(x'\). A lift over a valuation ring \(A'\) dominating \(A\) sends its generic point to \(x'\) as a point of \(X\), and its closed point to a specialization \(x\) of \(x'\) above \(y\). Because \(C\) is closed, \(x\in C\). This proves specialization stability.

For completeness the affine image argument that now gives closedness has a short algebraic proof. For a ring map \(D\to H\), let \(T\) be its image on spectra. If \(\mathfrak p\) is in the closure of \(T\), then \(H_d\ne0\) for every \(d\notin\mathfrak p\), because the open \(D(d)\) meets the image. It follows that \(H_{\mathfrak p}\ne0\): an equality \(1=0\) in this localization would already hold after inverting one such \(d\). A prime of \(H_{\mathfrak p}\) maps to a prime \(\mathfrak q\subset\mathfrak p\) in \(T\). If \(T\) is stable under specialization, \(\mathfrak p\in T\). Thus \(T\) is closed. Apply this to the affine scheme \(Z\) above. It proves the image of every \(C\) is closed, and proves universal closedness after all the base changes already allowed. \(\square\)

This is the affine image lemma [Stacks, Tag 00HY]; the proof makes clear why quasi-compactness was used. Specialization stability alone would not prove closedness for an arbitrary, non-quasi-compact image.

**Lemma 5.3.** If \(f:X\to Y\) is quasi-separated and universally closed, then it satisfies extended existence. The field extension needed in the following construction can be chosen finite separable.

**Proof.** Base change (5.1) to \(\operatorname{Spec}A\), and retain the notation \(X\) for this base change. The morphism

\[
a:\operatorname{Spec}K\longrightarrow X
\]

is quasi-compact. To see this, take an affine scheme chart \(U\to X\). There is a cartesian diagram expressing

\[
U\times_X\operatorname{Spec}K
\longrightarrow U\times_A\operatorname{Spec}K
\]

as a base change of \(\Delta_{X/A}\). That diagonal is quasi-compact by quasi-separatedness, and the scheme on the right is affine. Thus the fibre product on the left is quasi-compact. This is precisely the quasi-compactness test for \(a\).

Let \(x\) be the image of the generic point and \(\overline{\{x\}}\) its closure in \(|X|\). Universal closedness says that the image of this closed subset in \(\operatorname{Spec}A\) is closed. It contains the generic point, so it is the whole spectrum. Choose \(x_0\in\overline{\{x\}}\) above the closed point of \(A\), and an affine étale chart \(U=\operatorname{Spec}B\to X\) with a point \(u_0\) above \(x_0\).

An open continuous map \(q\) satisfies

\[
q^{-1}\bigl(\overline{\{x\}}\bigr)
=\overline{q^{-1}(\{x\})}.
\tag{5.3}
\]

For if \(u\) lies on the left, every neighbourhood of \(u\) has an open image containing \(q(u)\), and hence meeting \(x\). That neighbourhood therefore meets \(q^{-1}(\{x\})\). The reverse inclusion follows by continuity. We can apply this to the étale chart by Proposition 1.1.

The scheme

\[
P=U\times_X\operatorname{Spec}K
\]

is both quasi-compact, as shown above, and étale over \(K\). An étale scheme over a field is a disjoint union of spectra of finite separable field extensions; quasi-compactness makes this a finite disjoint union. Write its component fields as \(L_1,\ldots,L_n\), and let \(\eta_i\) be their image points in \(U\). Formula (1.3) shows that \(q^{-1}(\{x\})=\{\eta_1,\ldots,\eta_n\}\). By (5.3), \(u_0\) is in the union of their closures, hence specializes some \(\eta_i\).

Let \(\mathfrak p_i\subset\mathfrak q_0\) be the corresponding primes of \(B\). The map \(B\to L_i\) has kernel \(\mathfrak p_i\), and gives an embedding

\[
D=(B/\mathfrak p_i)_{\mathfrak q_0}\ \subset L_i.
\]

The original map \(A\to B\) embeds \(A\) into \(D\), since its composite into \(L_i\) is the given inclusion \(A\subset K\subset L_i\). Moreover its inverse image of the maximal ideal of \(D\) is \(\mathfrak m_A\), because \(u_0\) maps to the closed point of \(A\). Choose a valuation ring \(A'\subset L_i\) with fraction field \(L_i\) dominating \(D\), using the same domination theorem. It also dominates \(A\).

The maps \(B\to D\to A'\) now give \(\operatorname{Spec}A'\to U\to X\). On fraction fields this is the chosen point of \(P\), so its map to \(X\) is the original \(a\) after the extension \(L_i/K\). It is over \(\operatorname{Spec}A\), and supplies extended existence. \(\square\)

The finiteness in this argument is a consequence of quasi-separatedness applied to the particular field-valued map. We did not assume the target space had residue fields at all points, or that it was locally Noetherian.

### 5.3. Recovering separatedness from uniqueness

**Lemma 5.4.** A quasi-separated morphism \(f\) is separated if and only if it satisfies ordinary uniqueness.

**Proof.** One implication is Lemma 5.1. For the other, consider the diagonal \(d=\Delta_f\). It is quasi-compact by hypothesis. In a valuative square for \(d\), the lower map to \(X\times_YX\) consists of two maps \(\operatorname{Spec}A\to X\) over \(Y\). The generic map to the diagonal says that these maps agree on \(\operatorname{Spec}K\). Ordinary uniqueness for \(f\) makes them equal on \(\operatorname{Spec}A\), which gives an ordinary lift for \(d\). Thus \(d\) satisfies extended existence as well.

Lemma 5.2 makes \(d\) universally closed. By Lemma 4.1, it is representable by schemes, separated, locally of finite type, and has finite geometric fibres. For every scheme base change, these conditions imply that the resulting scheme morphism is finite [Stacks, Tag 02LS]. It is also a monomorphism; a finite monomorphism of schemes is a closed immersion [Stacks, Tag 03BB]. Therefore \(d\) is a closed immersion, as required. \(\square\)

Here the diagonal's local finite type was proved in Lemma 4.1; it was not inferred merely from the word “monomorphism.”

### 5.4. Descending an extended lift

We prove the step that replaces an extended lift by a lift over the original valuation ring. It uses quasi-coherent descent from Theorem 2.1 to construct a closed image, rather than presupposing a scheme neighbourhood of the image.

**Lemma 5.5 (closed image in the case we need).** Let \(A\) be a ring, let \(W\) be a quasi-compact algebraic space separated over \(\operatorname{Spec}A\), and let \(g:\operatorname{Spec}H\to W\) be an \(A\)-morphism. There is a smallest closed subspace \(Z\subset W\) through which \(g\) factors. For every affine étale chart \(V=\operatorname{Spec}B\to W\), the fibre product \(V\times_W\operatorname{Spec}H=\operatorname{Spec}C\) is affine and

\[
Z\times_WV=\operatorname{Spec}\bigl(B/\ker(B\to C)\bigr).
\tag{5.4}
\]

This construction commutes with flat base change on \(\operatorname{Spec}A\), and with étale change of chart.

**Proof.** The fibre product is closed in the affine scheme \(V\times_A\operatorname{Spec}H\), because it is a pullback of the closed diagonal of \(W/A\). Thus it is affine. If \(V'=\operatorname{Spec}B'\to V\) is a flat morphism of affine charts, its fibre algebra is \(C\otimes_BB'\). Flatness gives

\[
\ker(B'\to C\otimes_BB')
=\ker(B\to C)\,B'.
\tag{5.5}
\]

Choose an affine atlas \(V\to W\). On an affine open of \(V\times_WV\), either of the projections is étale, hence flat, and the two fibre products with \(\operatorname{Spec}H\) coincide. Equation (5.5) identifies the two pulled-back ideals. These identifications satisfy the cocycle because both are the kernel of the same map on a triple overlap. Theorem 2.1 therefore descends the ideals, with their inclusions into \(\mathcal O_V\), to a quasi-coherent ideal \(\mathcal I\subset\mathcal O_W\).

One can construct its closed subspace explicitly. The closed subscheme \(V_Z\subset V\) cut out by the ideal is preserved by the relation, because its two pulled-back ideals agree. The restriction of \(V\times_WV\) to \(V_Z\) is still an étale equivalence relation. Its quotient \(Z\) exists by the quotient theorem and maps to \(W\). Pulling that map back to \(V\) gives \(V_Z\to V\); étale descent of closed immersions [Stacks, Tag 02L6] makes \(Z\to W\) a closed immersion. This establishes (5.4).

The map \(g\) factors through \(Z\) because the kernel ideal vanishes after its pullback; this can be checked on the surjective étale cover \(V\times_W\operatorname{Spec}H\) of \(\operatorname{Spec}H\). If \(g\) factors through another closed subspace with ideal \(\mathcal J\), that ideal pulls back on \(V\) to an ideal vanishing in \(C\), hence is contained in \(\ker(B\to C)\). Thus \(\mathcal J\subset\mathcal I\), or \(Z\) is contained in that closed subspace. This proves minimality.

For a flat base change \(A\to A_1\), the atlas and its fibre product remain affine and their algebras become \(B\otimes_AA_1\) and \(C\otimes_AA_1\). Flatness again commutes with the kernel, proving the last assertion by (5.4). Étale change of chart was already handled by (5.5). \(\square\)

This is the scheme-theoretic image, constructed here only in the separated affine-source case used in the next proof.

**Lemma 5.6 (push down the lift).** Let \(f:X\to Y\) be separated. Given an extended lift for (5.1) over a valuation ring \(A'\subset K'\) dominating \(A\), there is a lift over \(A\) itself.

**Proof.** Replace \(X\to Y\) by its base change over \(\operatorname{Spec}A\). The result is separated over \(A\). The image of \(\operatorname{Spec}A'\) in \(|X|\) is quasi-compact. Choose a finite collection of images of affine chart opens covering it; their union is a quasi-compact open subspace of \(X\) by Proposition 1.2. Restrict to this open, through which the given map factors. We may therefore assume \(X\) quasi-compact and separated over \(A\).

Let \(Z\subset X\) be the closed image of \(\operatorname{Spec}A'\to X\) given by Lemma 5.5. We first prove

\[
Z_K=\operatorname{Spec}K,
\tag{5.6}
\]

with its map to \(X_K\) equal to the original generic section. Write \(A'_K=(A\setminus\{0\})^{-1}A'\), a nonzero domain in \(K'\). Its spectrum is the base change of \(\operatorname{Spec}A'\) to \(K\). On its fraction field the given map to \(X_K\) agrees with the composite through the original section \(a:\operatorname{Spec}K\to X_K\). Since \(X_K\) is separated over \(K\), the domain version of Lemma 5.1 makes these maps equal on all of \(\operatorname{Spec}A'_K\). The section \(a\) is a closed immersion: it is the base change of the diagonal of \(X_K/K\) along the map \(z\mapsto (z,a)\). The map \(K\to A'_K\) is faithfully flat, being a nonzero algebra over a field. Consequently the closed image of \(\operatorname{Spec}A'_K\to X_K\) is exactly that section. Flat base-change compatibility in Lemma 5.5 proves (5.6).

This argument deliberately uses \(A'_K\), not an identification of it with \(K'\). Such an identification need not hold for arbitrary extensions of valuation rings. For instance, \(A=K\) can itself be a field and \(A'=K[t]_{(t)}\subset K(t)\) a valuation ring dominating it; then \(A'_K=A'\ne K(t)\). Separatedness supplied the factorization needed above.

Choose an affine étale surjection \(U\to X\), and restrict it to \(Z\), obtaining the affine étale surjection \(V=U\times_XZ=\operatorname{Spec}B\to Z\). Its base change with \(\operatorname{Spec}A'\) is affine, say \(\operatorname{Spec}C\), since \(Z\) is separated over \(A\). Formula (5.4) identifies \(B\) with the original chart ring modulo the kernel of its map to \(C\), so \(B\to C\) is injective. The map \(A'\to C\) is étale, being the base change of \(V\to Z\). The ring \(A'\) is torsion-free as an \(A\)-module, and \(C\) is flat over \(A'\). Thus \(C\), and its submodule \(B\), are torsion-free over \(A\).

Over a valuation ring, a module is flat precisely when it is torsion-free [Stacks, Tag 0539]. The relevant algebra can also be seen from the flatness criterion: in a finite relation \(\sum a_i m_i=0\), choose a nonzero \(a_j\) dividing all the coefficients, possible because divisibility in a valuation ring is totally ordered. Torsion-freeness cancels \(a_j\), expressing \(m_j\) in terms of the other \(m_i\), and trivializes the relation as required by the equational criterion for flatness. In particular \(B\) is flat over \(A\).

The scheme \(V\times_ZV\) is closed in \(V\times_AV\), so write it as \(\operatorname{Spec}D\), with a surjection

\[
\theta:B\otimes_AB\twoheadrightarrow D.
\tag{5.7}
\]

By (5.6), this map becomes an isomorphism after tensoring with \(K\). Both copies of \(B\) are flat over \(A\); their tensor product is flat and hence torsion-free. Every element of \(\ker\theta\) is killed by a nonzero element of \(A\), because it is zero after localization to \(K\). Therefore \(\ker\theta=0\). We have proved

\[
V\times_ZV=V\times_AV.
\tag{5.8}
\]

The map \(A\to A'\) is faithfully flat. Indeed torsion-freeness makes it flat, and domination makes it a local map; a flat local map is faithfully flat [Stacks, Tag 00HR]. Hence \(\operatorname{Spec}A'\to\operatorname{Spec}A\) is surjective. Its factorization through \(Z\), together with the surjectivity of \(V\to Z\), shows that \(V\to\operatorname{Spec}A\) is surjective. Since \(B\) is already flat over \(A\), \(A\to B\) is faithfully flat.

One of the projections in (5.8) is étale, being a base change of \(V\to Z\). It is also the base change of \(V\to\operatorname{Spec}A\) by the faithfully flat map \(V\to\operatorname{Spec}A\). Étaleness descends under that base change [Stacks, Tag 02VN]. Thus \(V\to\operatorname{Spec}A\) is étale and surjective, as is \(V\to Z\). They have the same fibre relation by (5.8). The quotient theorem identifies both targets with the sheaf quotient of this relation; hence

\[
Z\xrightarrow{\sim}\operatorname{Spec}A.
\]

Its inverse followed by \(Z\to X\) is the required lift. Equation (5.6) verifies that its generic restriction is the prescribed \(a\). \(\square\)

*Reference:* the push-down statement is [Stacks, Tag 0ARH]. The proof above supplies the closed-image construction and treats arbitrary fraction-field extensions.

### 5.5. The properness theorem

**Theorem 5.7 (valuative criterion, finite type and quasi-separated).** Let \(f:X\to Y\) be a morphism of algebraic spaces of finite type and quasi-separated. The following are equivalent:

1. \(f\) is proper.
2. \(f\) satisfies extended existence and ordinary uniqueness.
3. Every square (5.1), for every valuation ring \(A\) with fraction field \(K\), has a unique lift \(\operatorname{Spec}A\to X\).

**Proof.** Suppose \(f\) is proper. It is separated, so uniqueness holds by Lemma 5.1. It is quasi-separated and universally closed, so Lemma 5.3 supplies extended existence. This proves \(1\Rightarrow2\). Separation then allows each extended lift to descend by Lemma 5.6, proving \(1\Rightarrow3\).

Suppose condition 2 holds. Since \(f\) is of finite type it is quasi-compact, and Lemma 5.2 makes it universally closed. Since it is quasi-separated, Lemma 5.4 makes it separated. Together with the assumed finite type these are exactly properness, so \(2\Rightarrow1\). Finally \(3\Rightarrow2\) follows by taking the trivial extension \(K'=K\), \(A'=A\). \(\square\)

This proves the stated generality of [Stacks, Tag 0A40]. The proof also shows that for quasi-compact and quasi-separated \(f\), without a finite-type assumption, the same criteria characterize “separated and universally closed.” Finite type is what then makes this properness. For an arbitrary separated \(f\), extended existence and ordinary existence are equivalent by Lemma 5.6; uniqueness already holds.

### 5.6. Chow's lemma

We state the permitted approximation result precisely, without using it in the proof of Theorem 5.7.

**Theorem 5.8 (Chow's lemma; stated).** Let \(Y\) be a quasi-compact and quasi-separated algebraic space, and let \(f:X\to Y\) be separated and of finite type. There are algebraic spaces \(X'\) and \(\overline X'\), and compatible morphisms over \(Y\),

\[
X\ \longleftarrow X'\ \hookrightarrow\ \overline X',
\]

such that \(X'\to X\) is proper and surjective, \(X'\to\overline X'\) is an open immersion, and \(\overline X'\to Y\) is proper and representable by schemes [Stacks, Tag 089L].

Representability here means that \(\overline X'\times_YT\) is a scheme for every scheme \(T\to Y\). In particular, when \(Y\) is a scheme, \(\overline X'\) and its open \(X'\) are schemes. The statement does not assert that \(X'\) is an absolute scheme for every algebraic-space target, and it does not replace the hypotheses on \(Y\) or on \(f\).

## 6. A space with one nonschematic point

Let \(k\) have characteristic different from \(2\), and consider the relation on \(U=\mathbf A^1_k\)

\[
R=\mathbf A^1_k\amalg\mathbf G_{m,k},\qquad
x\longmapsto(x,x)\text{ on the first component},\quad
x\longmapsto(x,-x)\text{ on the second}.
\tag{6.1}
\]

Its projections are étale, and it is an equivalence relation: sign changes are allowed off the origin and square to the identity. The quotient \(X=U/R\) is an algebraic space by *Algebraic spaces*. Write \(o\) for the image of the origin.

**Proposition 6.1.** The map \(x\mapsto x^2\) descends to \(h:X\to\mathbf A^1_k\) and induces a homeomorphism

\[
|X|\xrightarrow{\sim}|\mathbf A^1_k|.
\tag{6.2}
\]

The open complement \(X\setminus\{o\}\) is \(\mathbf G_{m,k}\), with quotient coordinate \(z=x^2\). No open neighbourhood of \(o\) in \(X\) is a scheme.

**Proof.** Squaring is equal on the endpoints of (6.1), so it descends to the quotient sheaf. On points its fibres are exactly the classes of the relation. One way to check this over a general \(k\) is to pass to a common algebraically closed residue-field extension for two points with the same square. Two roots of the same square differ by sign, and at zero there is just one root. Thus Proposition 1.1 makes \(|h|\) bijective.

The scheme map \(\mathbf A^1_x\to\mathbf A^1_z\) given by \(z=x^2\) is finite and surjective: \(k[x]\) is free of rank two over \(k[z]\), with basis \(1,x\). It is a closed continuous surjection and hence a quotient map on point spaces. The atlas map \(|U|\to|X|\) is also a quotient map. For a subset of \(|\mathbf A^1_z|\), its inverse image under the bijection (6.2) is open exactly when its inverse image in \(U\) is open, which is exactly when the subset itself is open. This proves the homeomorphism.

The inverse image of \(X\setminus\{o\}\) in \(U\) is \(\mathbf G_m\), so Proposition 1.2 identifies it with the quotient of the restricted relation. The ring map

\[
k[z,z^{-1}]\longrightarrow k[x,x^{-1}],\qquad z\longmapsto x^2
\]

is finite faithfully flat, and is étale since \(2x\) is invertible. Its fibre relation is the disjoint union of the identity and sign graphs: the equation \(y^2=x^2\) splits into the comaximal factors \(y-x\) and \(y+x\) on \(\mathbf G_m^2\). Its quotient is therefore \(\mathbf G_{m,z}\).

For the last assertion, let \(W\subset X\) be an open containing \(o\), and let \(U_W\subset U\) be its saturated inverse image. The pullback of the diagonal of \(W/k\) is the endpoint map

\[
R_W\longrightarrow U_W\times_kU_W.
\tag{6.3}
\]

The diagonal component of \(R_W\) is open and closed in \(R_W\). Its image is the diagonal line restricted to \(U_W^2\). The other component maps to the punctured antidiagonal. On the antidiagonal, the open \(U_W^2\) contains the origin and therefore also the generic point of that line; that generic point belongs to the second component's image. The image of the diagonal component is consequently not open near the origin in the image of (6.3) with its subspace topology. An immersion induces the subspace topology, so (6.3) is not an immersion.

Every scheme over \(k\) is locally separated: restrict its diagonal to products of affine neighbourhoods, where the local diagonal is closed; these products cover the diagonal's image and give immersions locally. Thus if \(W\) were a scheme its diagonal and (6.3) would be immersions, a contradiction. \(\square\)

Topologically this space looks exactly like an affine line, but its diagonal remembers the failure of a scheme neighbourhood at \(o\). Every other point has the scheme open \(\mathbf G_m\) around it. This is the sense in which \(o\) is its only nonschematic point; it does not mean that a topological invariant singles it out.

*Reference:* [Stacks, Tag 02Z1].

## 7. Exercises and complete solutions

**Exercise 7.1 (first steps: the quotient topology).** Describe \(|X|\) for the space (6.1), including its closed points and topology over a field which is not algebraically closed.

**Solution.** Two ordinary points of \(\mathbf A^1_x\) are identified if one is the image of the other under \(x\mapsto-x\). At the origin the second graph contributes no arrow, but the resulting point class is still a singleton. Equivalently, by Proposition 6.1 the classes are indexed by all prime ideals of \(k[z]\). The generic point corresponds to the zero ideal. Closed points correspond to monic irreducible polynomials \(p(z)\); their inverse images are the primes occurring in \(p(x^2)\). Any two distinct such primes belong to the same sign orbit, as can be seen by choosing roots in a common algebraic closure. If there is only one prime it is fixed as an ordinary point by sign, possibly with a nontrivial automorphism of its residue field. All these identifications follow from the relation after allowing the field extensions in the definition of a point.

The topology is the Zariski topology on \(\operatorname{Spec}k[z]\): nonempty proper closed sets are finite unions of these closed points, and the entire space is irreducible with its one generic point. Squaring is finite surjective, hence a quotient map, while the atlas is a quotient map by Proposition 1.1. This proves the topological assertion for arbitrary \(k\) of characteristic different from \(2\), not just for its rational points. Over an algebraically closed field the closed-point classes can be written \(\{a,-a\}\), with \(\{0\}\) at the origin.

**Exercise 7.2 (scheme locality: reduced and normal).** Show that reducedness and normality are étale local properties of schemes, and define the corresponding properties of an algebraic space. Keep the non-Noetherian case of normality.

**Solution.** Étale morphisms are smooth. The ascending commutative-algebra statements [Stacks, Tags 033B and 033C] say that a smooth algebra over a reduced, respectively normal, ring remains reduced, respectively normal, with no Noetherian assumption. Localizing these statements proves preservation on scheme charts.

For descent, let \(V\to T\) be an étale surjection, fix \(t\in T\), and choose \(v\) above it. The map \(A=\mathcal O_{T,t}\to B=\mathcal O_{V,v}\) is flat and local, hence faithfully flat. If \(B\) is reduced, a nilpotent of \(A\) maps to zero, and the injectivity of \(A\to B\) makes it zero. If \(B\) is a normal domain, \(A\) is a domain. For \(a/b\in\operatorname{Frac}A\) integral over \(A\), its image belongs to the integrally closed domain \(B\). Hence \(a\in bB\cap A\). Faithful flatness gives \(bB\cap A=bA\), by the injectivity of \(A/bA\to B/bB\). It follows that \(a/b\in A\). Thus every local ring of \(T\) is reduced, respectively an integrally closed domain.

These properties are also local in the Zariski topology, since they are properties of all local rings. They are therefore étale local. Define \(X\) reduced, respectively normal, by requiring one étale scheme atlas to be reduced, respectively normal. Given another atlas, its common refinement with the first inherits the property and covers the second étale. The property consequently holds on every atlas and every étale scheme chart, and agrees with the usual property for schemes. The two ascending scheme theorems are the precise prerequisite imports in this solution; the descent and atlas-independence arguments are proved here.

**Exercise 7.3 (separation: uniqueness).** Prove the uniqueness part of the valuative criterion for a separated morphism \(f:X\to Y\) of algebraic spaces.

**Solution.** If \(a_1,a_2:\operatorname{Spec}A\to X\) are two lifts of the same square, form their equality scheme by pulling back the closed immersion \(\Delta_f\) along \((a_1,a_2)\). It is a closed subscheme \(\operatorname{Spec}(A/I)\) of \(\operatorname{Spec}A\). Equality of the generic maps gives \(I\otimes_AK=0\). Since \(A\) is a domain, \(I=0\), so the equality scheme is all of \(\operatorname{Spec}A\). Thus \(a_1=a_2\). Neither the rank nor Noetherianity of the valuation ring enters this argument.

**Exercise 7.4 (a nonschematic point).** For (6.1), prove that the complement of the image of the origin is a scheme isomorphic to \(\mathbf G_m\) through \(x\mapsto x^2\), and that no open neighbourhood of that image is a scheme.

**Solution.** Pull the complement back to the atlas; it is \(\mathbf G_{m,x}\). The restricted relation has both complete sign graphs, and

\[
\mathbf G_{m,x}\times_{\mathbf G_{m,z}}\mathbf G_{m,x}
\simeq\mathbf G_{m,x}\amalg\mathbf G_{m,x}.
\]

The two components are cut out by \(y=x\) and \(y=-x\). They are disjoint because \(2x\) is a unit. The square map is finite étale and surjective, so its target \(\mathbf G_{m,z}\) is its sheaf quotient, identifying the complement.

For an open neighbourhood of the origin's class, its inverse image in the affine line is an invariant open containing zero. The endpoint map of its relation has one full diagonal component and one punctured antidiagonal component. The diagonal component is open in the source; its image is not open in the image of that endpoint map near \((0,0)\), since every neighbourhood there contains a point of the punctured antidiagonal. The endpoint map is therefore not an immersion. A scheme has an immersion as its relative diagonal over \(k\), and this property would remain an immersion on the atlas pullback. This contradiction excludes every such scheme neighbourhood, including non-affine ones.

## What this lesson does not prove

The following are precise scheme prerequisites, rather than additional unproved algebraic-space versions of the results proved here.

- Faithfully flat effective descent of quasi-coherent scheme modules [Stacks, Tag 023T], and the equivalence between Zariski and étale quasi-coherent modules on a scheme [Stacks, Tags 03DX and 03LC]. The lesson proves their extension to an algebraic-space presentation, including the transition-map and inverse-functor verifications.
- The ascending commutative-algebra theorems that smooth algebras over reduced or normal rings remain reduced or normal [Stacks, Tags 033B and 033C]. Normality includes arbitrary normal rings. Their descent and the passage to spaces are proved here.
- The Noetherian scheme finite-type theorem and the dimension formula for a flat local map of Noetherian rings with zero-dimensional fibre [Stacks, Tags 01T6 and 00ON]. These enter the étale-local Noetherian and regular-ring arguments. We also use the usual fibre description and cotangent properties of étale scheme maps.
- Scheme locality of the chart-morphism properties in Section 3.2: the target descent statements [Stacks, Tags 02KX, 02KY, 02L2, 02VL, 02VM and 02VN] and the source locality statements [Stacks, Tags 036K, 036N, 036O, 036U, 036W and 03YV]. Their extension and presentation-independence are proved here.
- Scheme descent of quasi-compactness, immersions and closed immersions [Stacks, Tags 02KQ, 02YM and 02L6]; the finite-type permanence rule [Stacks, Tag 01T8]; and the fact that a locally finite-type scheme morphism with finite fibres is locally quasi-finite.
- Existence of a valuation ring in a prescribed field dominating a local subring [Stacks, Tag 00IA]; the torsion-free flatness theorem for modules over valuation rings [Stacks, Tag 0539]; and faithful flatness of a flat local map [Stacks, Tag 00HR]. The lesson recalls the flatness mechanism but does not reprove the general equational flatness criterion.
- The scheme theorem that a universally closed, separated, locally finite-type morphism with finite fibres is finite [Stacks, Tag 02LS], and that a finite monomorphism is a closed immersion [Stacks, Tag 03BB]. They are applied to scheme base changes of the diagonal.

Chow's lemma, Theorem 5.8 [Stacks, Tag 089L], is stated without proof as permitted. The valuative criterion itself, its extended existence and push-down arguments, the point-space construction, and quasi-coherent descent on an algebraic space have been proved in the lesson.

## References

- **[Stacks]** The Stacks project, *Properties of Algebraic Spaces*, *Morphisms of Algebraic Spaces*, *Decent Algebraic Spaces*, and *More on Morphisms of Spaces*, especially Tags 03BT, 03EB, 03G5, 03M3, 03I8, 03ID, 03ZL, 0CKZ, 0ARH, 0A40 and 089L. The corresponding chapters are available in [AI Integrated Stacks Project](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/), an edition containing AI-proposed corrections and additions which have not been reviewed by the Stacks project's maintainers. The [official Stacks project](https://stacks.math.columbia.edu/) retains its own publication and tags.
