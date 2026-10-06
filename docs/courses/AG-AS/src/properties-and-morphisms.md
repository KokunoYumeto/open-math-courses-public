# Properties and morphisms of algebraic spaces

*Algebraic spaces and stacks, Lesson 3 of 12.*

*Written and self-checked by the writing AI, GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Public domain (CC0).*

An algebraic space has an étale chart by a scheme, but that chart need not have a Zariski-local inverse. We therefore need two kinds of locality. Its underlying topological space describes open subspaces and specializations. Its small étale site carries the structure sheaf and modules. These constructions also let us formulate properness without assuming that a neighbourhood of each point is a scheme.

We use the quotient theorem from *Algebraic spaces* and the bootstrap and scheme-recognition results from *The bootstrap theorem*. For Chow's lemma we also use the genuinely assigned scheme approximation and Zariski Main foundations, with their current states stated in §5.6. Scheme theory, including faithfully flat descent of quasi-coherent modules and the elementary scheme properties of étale morphisms, is prerequisite material. The scheme inputs used below are listed precisely at the end. Algebraic spaces and all their fibre products are considered over a fixed base scheme \(S\).

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

An algebraic space separated over a base need not be a scheme. Chow's lemma replaces it, by a proper surjection, with an open subspace of a proper space which is a scheme after every scheme base change of the target.

**Theorem 5.8 (Chow's lemma).** Let \(Y\) be a quasi-compact and quasi-separated algebraic space, and let \(f:X\to Y\) be separated and of finite type. There are algebraic spaces \(X'\) and \(\overline X'\), and compatible morphisms over \(Y\),
\[
X\ \longleftarrow X'\ \hookrightarrow\ \overline X',
\]
such that \(X'\to X\) is proper and surjective, \(X'\to\overline X'\) is an open immersion, and \(\overline X'\to Y\) is proper and representable by schemes.

Representability means that \(\overline X'\times_YT\) is a scheme for every scheme \(T\to Y\). Consequently \(X'\times_YT\) is also a scheme. For an algebraic-space target the theorem asserts relative representability; it does not assert that \(X'\) is an absolute scheme.

We first construct the modification over a Noetherian algebraic space. We then use two approximation operations to recover every separated finite-type morphism over a quasi-compact, quasi-separated target. The flattening result needed for the first part has this precise form:

The proof has three foundations: approximation through étale presentations, finite hulls for charts, and flattening of strict transforms. The next subsections prove their space extensions and local algebra. The final construction uses admissible blowups to put two modifications in one separated space, then returns from the Noetherian case to the original finite-type morphism. Lettered lemma names refer to the local support proofs in these subsections.

#### 5.6.1. Approximation by étale presentations

The exact scheme foundations are finite-presentation descent and relative approximation with prescribed quasi-compact open models in *Limits of schemes and Noetherian approximation* (AG-MO-03), Theorems 4.1 and 5.2. The current finite-presentation comparison is written; the complete prescribed-open construction remains a genuine planned repair in that lesson. We retain that actual prerequisite state. Here we prove its extension to spaces using an étale presentation.

**Finite-presentation descent for spaces.** Suppose \(B=\varprojlim B_i\), with quasi-compact, quasi-separated spaces and affine transitions. Choose an affine étale presentation \(E_0\to B_0\), and set \(E_i=E_0\times_{B_0}B_i\), \(R_i=E_i\times_{B_i}E_i\). Each \(E_i\) is affine, and each \(R_i\) is a quasi-compact separated scheme. Their limits present \(B\).

For a finite-presentation \(Z\to B\), choose a finite affine étale cover \(W\to Z\times_BE\). Then \(W\to E\) is of finite presentation. The relation \(P=W\times_ZW\) is of finite presentation over \(R\): pull back the finite-presentation diagonal of \(Z\to B\) along the two finite-presentation copies of \(W\to E\). It is quasi-compact and separated.

Scheme descent along limits gives \(W_i\to E_i\), \(P_i\to R_i\) and the source and target maps at a stage. Identity, inverse and composition descend after increasing that stage, since they are maps between finite-presentation schemes with finitely many equality requirements. Étaleness descends. The assertion that \(P_i\to W_i\times W_i\) is a monomorphism descends by descending the inverse to its diagonal isomorphism at the limit; every comparison involved is of finite presentation. Thus \(P_i\rightrightarrows W_i\) is an étale equivalence relation. Lesson 1's presentation theorem gives \(Z_i=W_i/P_i\), of finite presentation over \(B_i\), and its base change is \(Z\).

Maps between two such objects descend by descending their maps on finite affine étale presentations and requiring equality on the relation. Equality of two maps has a finite-stage witness for the same reason. This proves the fully faithful comparison needed for descended groupoid diagrams.

Separatedness descends by applying scheme eventual closedness to the pulled-back diagonal on the presentation; a finite-presentation closed-immersion assertion descends to a stage, and closed immersions descend from the target étale cover. Quasi-compact opens descend by descending their finitely many chart opens and the equality of their two pullbacks on the relation. A quasi-compact space with empty limit is empty at a stage, by the same assertion on its finite scheme chart.

**Finite étale splitting filtration.** A quasi-compact, quasi-separated space \(T\) has quasi-compact opens
\[
\varnothing=U_{n+1}\subset U_n\subset\cdots\subset U_1=T
\]
and quasi-compact separated scheme covers \(V_p\to U_p\), étale and isomorphisms over the reduced closed stratum \(U_p\setminus U_{p+1}\).

Choose an affine étale surjection \(E\to T\). Its geometric fibre cardinalities have a common finite bound \(n\): pull back to a finite affine target cover, and use scheme Zariski's Main Theorem for the resulting quasi-finite separated quasi-compact maps. Their finite hulls have fibre cardinalities bounded by finitely many module generators. For each \(p\), delete all diagonals from \(E^p_T\), obtaining \(W_p\). The diagonals are open and closed because \(E\to T\) is separated and étale. Thus \(W_p\) is a quasi-compact separated scheme. Its map to affine \(E^p_{\mathbf Z}\) is quasi-finite and separated, hence quasi-affine by scheme Zariski's Main Theorem. Every finite set of its points has an affine neighbourhood, by choosing a principal open in an affine envelope.

The symmetric group \(S_p\) acts freely on \(W_p\). The finite-orbit affine quotient construction of Lesson 1 gives a separated scheme \(V_p=W_p/S_p\). The map \(V_p\to T\) is étale by descent from \(W_p\). Let \(U_p\) be its image, a quasi-compact open. A geometric point belongs to \(U_p\) exactly when its \(E\)-fibre has at least \(p\) points. On the stratum with exactly \(p\) points, the \(V_p\)-fibre is the single unordered set of all those points. The restricted étale map is universally injective and surjective, hence an isomorphism. The bound \(n\) makes the filtration finite.

**Approximation by induction on the filtration.** At the bottom, \(V_n\to U_n\) is an isomorphism: its restriction over the reduction is one, so all its geometric fibres are singletons; an étale universally injective surjection is an isomorphism. Approximate this scheme by the genuinely planned scheme theorem.

At an induction step, let \(U\subset T\) already have \(U=\varprojlim U_i\), and let \(V\to T\) be the separated scheme chart from the filtration. Put \(W=V\times_TU\), a quasi-compact open scheme in \(V\), étale of finite presentation over \(U\). Descend it to \(W_i\to U_i\). After increasing the stage the \(W_i\) are schemes; an eventual-scheme proof is recorded below.

Apply the exact **relative prescribed-open approximation** assigned to AG-MO-03, Theorem 5.2's extension route: for the prescribed system \(W=\varprojlim W_i\) and the quasi-compact open \(W\subset V\), refine the directed index so that \(V=\varprojlim V_i\), with \(V_i\) finite-type schemes over \(\mathbf Z\), affine transitions, and \(W_i\subset V_i\) compatible open immersions whose inverse images at later stages are the later \(W_j\). This preserves the already chosen \(W_i\)'s; unrelated absolute approximations would not do so.

For each \(i\), glue
\[
R_i=V_i\amalg_{W_i}(W_i\times_{U_i}W_i)
\]
along the open diagonal of the second term. Extend its two projections by the identity on \(V_i\). They are étale and form an equivalence relation: on \(W_i\) the relation is that of \(W_i\to U_i\); outside \(W_i\) there are only identity arrows and no arrows cross the two parts. Put \(T_i=V_i/R_i\). The presentation is finite type over \(\mathbf Z\) with quasi-compact relation, so \(T_i\) is quasi-separated and finite type.

The squares of \(R_i\to V_i\) with earlier-stage counterparts are cartesian: on the relation open use \(W_i=W_{i'}\times_{U_{i'}}U_i\), and on its other open use the identity relation and the inverse-image condition on \(W_i\subset V_i\). Presentation descent then gives
\[
V_i=T_i\times_{T_{i'}}V_{i'}.
\]
Affineness of \(V_i\to V_{i'}\) descends from this target étale cover, so \(T_i\to T_{i'}\) is affine. The limit relation is \(V\amalg_W(W\times_UW)\). It equals \(V\times_TV\): over the complementary closed stratum the cover has just one geometric point in every fibre, so its arrows lie in its open diagonal; all other arrows lie over \(U\). The two relation opens therefore cover, intersecting along \(W\). Their identification respects projections, hence \(T=V/R=\varprojlim T_i\). Induction gives the space approximation assertion with precisely the planned scheme prerequisites just identified.

The eventual-scheme assertion used here follows from eventual affineness and open descent. Cover the scheme limit by finitely many affine opens and descend them. For an affine space limit, take an affine étale chart, write its finitely presented étale algebra over that affine limit, and descend its finitely many algebra coefficients and étale presentation. The chart's comparison to the descended étale algebra becomes an isomorphism at a stage by finite-presentation scheme descent. The resulting cartesian presentation identifies that stage with an affine scheme by faithfully flat affine descent. Thus the descended opens are eventually affine. Their quasi-compact complement has empty limit and is eventually empty. They then cover a scheme stage. This is the finite-presentation scheme limit and affine-descent argument applied to the space presentation, not an inference that an arbitrary finite-stage space is a scheme.

#### 5.6.2. Quasi-coherent completeness and ideal extension

**G.1.** On a qcqs algebraic space \(B\), every quasi-coherent module is a filtered colimit of finitely presented quasi-coherent modules and a union of finite-type quasi-coherent submodules. Every finite-type module is a quotient of a finitely presented module. Finite-type quasi-coherent submodules, including ideals, extend from a quasi-compact open. A quasi-coherent algebra is a filtered colimit of finitely presented quasi-coherent algebras. An integral quasi-coherent algebra is a union of finite quasi-coherent subalgebras.

We first prove the essential Noetherian space assertion, rather than assume that a coherent subsheaf on an atlas descends. Choose an affine étale surjection \(E\to B\); let \(R=E\times_BE\) be its Noetherian qcqs scheme relation, with flat projections \(s,t:R\to E\). A quasi-coherent module on \(B\) is a quasi-coherent module \(M\) on \(E\) with transport isomorphisms along arrows of \(R\rightrightarrows E\), satisfying the identity and composition laws. This is the quasi-coherent descent theorem proved in Lesson 3.

For any module \(L\) on \(E\), its coinduced module is \(\mathcal C(L)=s_*t^*L\). On an arrow with source \(e\), its sections have values in \(L\) at the target; composition identifies arrows out of two objects related by an arrow and gives the transport on \(\mathcal C(L)\). The inverse arrow makes this an isomorphism, and associativity gives the cocycle. Formally, the two pullbacks of \(s_*t^*L\) identify by flat base change with pushforwards on the composable-arrow fibre products; the composition-and-inverse isomorphism of these products gives precisely this transport. Flat base change here can be checked by a finite affine covering of the qcqs source: degree-zero sections are the kernel of its finite Čech difference map, and flat tensor commutes with that kernel. The same calculation shows that \(s_*\) preserves filtered colimits. No properness or coherent pushforward assertion is being used.

There is an equivariant map \(M\to\mathcal C(M)\), sending a vector at the source to its transported vector along each arrow. Evaluation at the identity arrow gives a left inverse, so this map is injective. Express the underlying module on the affine Noetherian \(E\) as a filtered union of coherent submodules \(L_i\subset M\). Flatness of \(t\) and left exactness of \(s_*\) make \(\mathcal C(L_i)\subset\mathcal C(M)\). The equivariant preimages
\[
 M_i=M\times_{\mathcal C(M)}\mathcal C(L_i)
\]
are quasi-coherent submodules with transport, hence descend to submodules on \(B\). They are coherent on \(E\): evaluation at the identity shows \(M_i\subset L_i\), and a quasi-coherent submodule of a coherent module on a Noetherian scheme is coherent. As \(\varinjlim\mathcal C(L_i)=\mathcal C(M)\), the preimages exhaust \(M\). Coherence is étale local, so their descents are coherent on \(B\). This proves that every quasi-coherent module on a Noetherian algebraic space is a union of coherent modules. It also gives the completeness assertion there, since coherent modules on a Noetherian space are finitely presented.

For a general qcqs \(B\), use its absolute Noetherian approximation proved in §5.6.1: \(B=\varprojlim B_i\), with affine transition maps and Noetherian finite-type spaces \(B_i\). This is the space presentation-and-prescribed-open extension argument there, with its exact AG-MO-03 prerequisite still honestly planned; it is not imported from a scheme-only theorem without that argument. Fix a stage and let \(q:B\to B_i\), affine. For a quasi-coherent \(M\) on \(B\), \(q_*M\) is quasi-coherent and is a union of coherent \(L_j\) by the Noetherian result. The evaluation
\[
 \varinjlim q^*L_j=q^*q_*M\longrightarrow M
\]
is surjective. On an affine target chart this is the multiplication map \(A\otimes_RM\to M\), \(a\otimes m\mapsto am\), with \(1\otimes m\) as a preimage. Each \(q^*L_j\) is finitely presented.

To pass from a quotient of such a colimit to a colimit of finitely presented modules, apply the same argument to the kernel. A finitely presented module is compact in this quasi-coherent category: cover \(B\) by finitely many affine étale charts and their qcqs relation by finitely many affine charts; a homomorphism involves finitely many images of generators and finitely many equations on these charts. These equations and the descent equalities hold at a finite stage of a filtered colimit. Thus maps from finitely presented modules commute with filtered colimits. If \(P=\varinjlim P_i\twoheadrightarrow M\), with \(P_i\) finitely presented, and \(K=\varinjlim K_j\twoheadrightarrow\ker(P\to M)\), maps from each \(K_j\) into \(P\) factor through a stage. Form all cokernels
\[
 \operatorname{coker}\left(\bigoplus_{j\in J_0}K_j\longrightarrow P_i\right)
\]
where \(J_0\) is finite and the maps lift the indicated kernel maps. These cokernels are finitely presented. The finite choices form a filtered system: take common upper stages, combine the finite kernel lists, and increase the upper stage until the finitely many equalities of lifts hold. Its colimit kills exactly \(K\) and is \(M\). This proves the asserted filtered-colimit description.

The images in \(M\) of these finitely presented modules are finite type and exhaust \(M\), giving the union assertion. If \(M\) is finite type, lift a finite family of generators on a finite affine étale cover to one stage; its image is all of \(M\). Hence \(M\) is a quotient of a finitely presented module.

For extension let \(j:V\hookrightarrow B\) be a quasi-compact open, \(N\subset M|_V\) a finite-type quasi-coherent submodule. Since \(B\) is qcqs, \(j\) is qcqs and its pushforward is quasi-coherent. Put
\[
 K=\ker\bigl(M\to j_*(M|_V/N)\bigr).
\]
It is quasi-coherent and \(K|_V=N\). Exhaust \(K\) by finite-type submodules. Quasi-compactness of \(V\) and finite generation of \(N\) select one submodule \(K_0\) with \(K_0|_V=N\). This is the required extension. If \(M=\mathcal O_B\), it is an ideal, giving exactly the centre extensions used in A and F.

The algebra version uses these module statements, not a new approximation axiom. For a finite-type quasi-coherent algebra \(A\), choose a finitely presented module \(P\to A\) whose image generates it as an algebra (choose a finite generating family on an atlas and a common module stage). The symmetric algebra \(\operatorname{Sym}P\twoheadrightarrow A\) is finitely presented as a quasi-coherent algebra. Its kernel is the union of finite-type quasi-coherent modules; adjoining their finitely many relations gives finitely presented algebra quotients whose filtered colimit is \(A\). For arbitrary \(A\), first take its finite-type subalgebras generated by these finite-type module images, then the same construction. Tensor products combine any two choices, and a finite list of relation differences equalizes any pair of maps, so the indexing system is filtered. If \(A\) is integral, each finite-type subalgebra is finite as an \(\mathcal O_B\)-module: on affine charts finitely many integral generators have monic equations, and the monomials with bounded exponents generate their algebra. Finiteness is étale local. This proves all of G.1.

In particular, a closed subspace of an affine space over \(B\) has its quasi-coherent ideal as a union of finite-type ideals. The ambient ideal belongs to the ambient space, not to \(B\). A quasi-affine map can be placed as an open in an affine space, its affine algebra approximated by the algebra statement above, and its quasi-compact open descended. These are exactly the completeness steps in the finite-presentation-envelope proof in §5.6.1.

#### 5.6.3. Separated finite-presentation envelopes

**Separated finite-presentation envelopes.** With absolute space approximation available, the finite-type envelope follows through quasi-affineness and quasi-coherent completeness. Write \(X=\varprojlim X_i\) in absolute models. The graph
\[
X\longrightarrow X\times_{\mathbf Z}Y
\]
is a finite-type monomorphism. A finite-type morphism into an affine-transition system which is a monomorphism at the limit is a monomorphism at a stage: pull back to scheme presentations and use the finite-presentation diagonal to descend its isomorphism onto the fibre-square. The scheme proof also gives eventual closed immersions for finite-type maps with closed-immersion limit.

Hence \(X\to X_i\times_{\mathbf Z}Y\) is eventually a finite-type monomorphism, and is representable by schemes by Lesson 2's separated locally quasi-finite recognition. Scheme Zariski's Main Theorem makes it quasi-affine. Put the quasi-affine map as a quasi-compact open in a relative affine space, express its quasi-coherent algebra by finitely presented algebras, descend the open, and apply eventual closedness to the original finite-type map. This produces \(X\hookrightarrow Z\) closed, with \(Z\to Y\) of finite presentation.

G.1 above supplies quasi-coherent completeness, ideal extension and algebra presentations on the full qcqs space.

Using G.1, let \(\mathcal J\) be the ideal of \(X\hookrightarrow Z\), **on \(Z\)**. Write it as a directed union \(\bigcup_a\mathcal J_a\) of finite-type quasi-coherent ideals. Then \(Z_a=V(\mathcal J_a)\) is of finite presentation over \(Y\), with closed transition maps and limit \(X\). Eventual separatedness, checked on scheme presentations and diagonals, supplies some separated \(Z_a\to Y\). Set \(X_1=Z_a\). This is the closed separated finite-presentation envelope used in the final finite-type reduction.

#### 5.6.4. Finite hulls for separated étale charts

**H.1.** Let \(B\) be a qcqs algebraic space and \(w:W\to B\) a qc separated étale morphism with \(W\) a scheme. There is a factorization
\[
 W\xrightarrow{j}P\xrightarrow{\pi}B
\]
with \(j\) a quasi-compact open immersion and \(\pi\) finite and finitely presented. Thus the Noetherian instance required for the Chow construction, and the arbitrary-base centre descent in F, are both covered.

We begin with Noetherian \(B\). The algebra \(\mathcal H=w_*\mathcal O_W\) is quasi-coherent; this is checked on affine étale base charts by the finite affine-cover equalizer calculation in G. Let \(\mathcal A\subset\mathcal H\) be the integral closure of \(\mathcal O_B\). We justify its étale compatibility, which is essential for this construction to glue.

For rings \(R\to H\) and an étale \(R\)-algebra \(R_1\), let \(A\subset H\) be the integral closure of \(R\). Then
\[
 R_1\otimes_RA
 =\text{integral closure of }R_1\text{ in }R_1\otimes_RH.
\]
Injection follows from flatness. Localize \(R_1\) to a standard étale presentation \((R[x]/(F))_g\), with \(F\) monic and \(F'\) invertible. Integral closure commutes with localization: after multiplying an integral element by a sufficiently large power of the denominator, its monic relation has coefficients in the original ring. It is therefore enough to consider \(h\in H[x]/(F)\) integral over \(R[x]/(F)\), hence integral over \(R\). In a finite free splitting algebra, write the roots as \(\alpha_1,\ldots,\alpha_n\). The universal polynomial identity
\[
 F'h=\sum_{i=1}^n h(\alpha_i)
 \prod_{j\ne i}(x-\alpha_j)\pmod F
\]
holds even with repeated roots: prove it over the universal polynomial ring by inverting the discriminant, then use injectivity into that localization to obtain the polynomial identity before specializing. Each \(\alpha_i\) and \(h(\alpha_i)\) is integral over \(R\). The coefficients of \(F'h\) are consequently integral over \(R\). They are also in \(H\), because \(1,x,\ldots,x^{n-1}\) is a basis before and after the faithful free splitting extension. Thus those coefficients lie in \(A\). Inverting \(F'\) puts \(h\) in \(R_1\otimes_RA\), proving the claim.

The algebras \(\mathcal A\) on étale charts therefore agree on overlaps and are quasi-coherent. Put \(B'=\underline{\operatorname{Spec}}_B\mathcal A\), integral over \(B\), with its canonical evaluation map \(W\to B'\). This map is a quasi-compact open immersion. To check it, take an affine étale \(V\to B\). The scheme \(W_V\to V\) is qc, separated and quasi-finite. Scheme Zariski Main (AG-MO-12) factors it as a qc open in a finite \(V\)-scheme \(P_V\). Replace \(P_V\) by the schematic closure of that open; its structure algebra injects into \(w_*\mathcal O_{W_V}\) and is integral over \(\mathcal O_V\). The integral closure of \(\mathcal O_V\) in that algebra of functions is also its integral closure over \(\mathcal O_{P_V}\), by transitivity of integrality. Above the open \(W_V\subset P_V\), this closure is just \(\mathcal O_{W_V}\). Hence \(W_V\to\operatorname{Spec}_V(\mathcal A|_V)\) is an open immersion. The compatible canonical evaluations descend the assertion to \(B\). This uses the **scheme** Zariski Main theorem and the étale integral-closure comparison just proved; it has not assumed the desired space factorization.

By G.1, write \(\mathcal A=\varinjlim\mathcal A_i\) as a union of finite quasi-coherent subalgebras. Put \(P_i=\underline{\operatorname{Spec}}_B\mathcal A_i\). They are finite over \(B\), hence Noetherian and finitely presented, and \(B'=\varprojlim P_i\) with affine transitions. Descend the qc open \(W\subset B'\) to a qc open \(V_i\subset P_i\), using the space open-descent argument in §5.6.1 (proved by descending chart opens and their two equal pullbacks). Then \(W=\varprojlim V_i\).

The finite-type eventual-closed-immersion comparison gives a stage with \(W\to V_i\) closed. Here is a direct proof of the space extension in this application. The maps \(V_j\to V_i\) are affine and \(W=\varprojlim V_j\). Choose an affine étale cover \(V\to B\), and a finite affine étale cover \(E_i\to V_i\times_BV\). Let \(E_j=E_i\times_{V_i}V_j\) and \(E=E_i\times_{V_i}W\). All these are affine schemes, since the projections to \(E_i\) are affine; \(E=\varprojlim E_j\). Moreover \(E\to V\) is finite type: \(E\to W\times_BV\) is a quasi-compact étale map and \(W\to B\) is finite type. In rings the finite-type \(R=\mathcal O(V)\)-algebra \(\mathcal O(E)\) is the filtered colimit of \(\mathcal O(E_j)\). Its finitely many \(R\)-algebra generators all occur at one stage, so \(\mathcal O(E_j)\to\mathcal O(E)\) is surjective at that stage. Thus \(E\to E_j\) is closed. Closed immersions descend from the surjective étale cover \(E_j\to V_j\), giving \(W\to V_j\) closed. If several affine pieces were chosen, one common stage works for all of them. This argument uses the original compatible limit \(W=\varprojlim V_j\); it does not replace it by the generally different fibre product \(W\times_{V_i}W\).

Consequently \(W\to P_i\) is an immersion. Let \(P\subset P_i\) be its schematic closure. It is finite over \(B\), and its intersection with the open \(V_i\) is exactly the closed subscheme \(W\subset V_i\). Thus \(W\subset P\) is open. Since \(B\) and \(P_i\) are Noetherian, its ideal is coherent and \(P\to B\) is finitely presented. This proves H.1 for Noetherian \(B\).

For arbitrary qcqs \(B\), use the absolute Noetherian space approximation in §5.6.1. The finitely presented object \(W\to B\) descends to \(W_i\to B_i\); its étale and separated properties hold at a stage by the presentation-and-diagonal descent proved there. The scheme limit \(W\) is a scheme at a stage by the eventual-scheme argument there: descend a finite affine open cover, use eventual affineness on its affine limits through an étale affine presentation and faithfully flat affine descent, and remove its eventually empty complement. We therefore have a qc separated étale **scheme** \(W_i\to B_i\). Apply the Noetherian case, and base change its finite finitely presented hull to \(B\). The resulting open is canonically \(W\), by the descended object isomorphism. This proves H.1 at its full qcqs scope. Its transitive scheme approximation prerequisite remains the exact planned AG-MO-03 assignment, as recorded below.

Together, F.1, G.1 and H.1 provide flattening, centre descent, completeness and finite hulls for the construction in §5.6.13.

#### 5.6.5. Strict transforms and compositions of blowups

Let \(S\) be a scheme, \(U\subset S\) a quasi-compact open, and \(b:S'\to S\) the blowup of a finite-type quasi-coherent ideal \(J\) with \(J|_U=\mathcal O_U\). The exceptional ideal \(J\mathcal O_{S'}\) is invertible and locally has a regular generator \(a\in\mathcal O_{S'}\). For a quasi-coherent module \(N\) on \(T\to S\), its strict transform is
\[
 N^{\mathrm{str}}=(N\otimes_{\mathcal O_S}\mathcal O_{S'})/
 \{n:a^kn=0\text{ for some }k\geq0\}.
\]
This definition glues: replacing \(a\) by a unit multiple does not change its power torsion. It retains the restriction over \(U\). It commutes with flat pullback and with pushforward along an affine morphism, since both assertions reduce to the same module and the same submodule of power torsion on affine charts. Thus finite pushforward detects base flatness and respects the strict transform.

We will use three elementary facts about successive modifications. Their scheme blowup foundations are AG-MO-16; the comparisons are worth making explicit.

* A quasi-compact open complement is the vanishing set of a finite-type ideal. Blowing up such an ideal makes the complement an effective Cartier divisor. Its local equation is regular on the blowup, so \(U\) is then schematically dense, including in nonreduced cases. If \(U=\varnothing\), this initial blowup is empty and all the assertions about strict transforms hold on the empty scheme.
* A local centre on a quasi-compact open \(V\subset S\), equal to the unit ideal on \(U\cap V\), extends to a finite-type ideal on \(S\), equal to the unit ideal on \(U\). Glue it with \(\mathcal O_U\) on \(U\cup V\), then extend a finite-type quasi-coherent submodule from that open. This last extension is proved in G.1, for schemes as a special case. The resulting blowup restricts to the given one on \(V\).
* The blowup of \(J_1\cdots J_n\) dominates the blowup of each \(J_i\). On a chart where the product ideal is the regular principal ideal \((a)\), each factor is invertible: for two factors, \(I K=(a)\), so \(a^{-1}K\) is an inverse fractional ideal to \(I\); a finite expression for \(a\) as a sum of products supplies a dual basis. The universal property gives the maps. Successive blowups in finite-type ideals are themselves a blowup, by A.2 below. The basic scheme charts and universal property are AG-MO-16; we supply the additional composition argument at arbitrary qcqs scope rather than assign it to the Noetherian-only Serre theorem of AG-QC-05. The algebraic-space chart and gluing extension is already proved in the blowup charts in §5.6.13.

Flat strict transforms stay flat under further admissible blowups. If \(N'\) is flat over \(S'\), its pullback to \(S''\) is flat over \(S''\). A regular local equation of the new exceptional divisor acts injectively on a base-flat module, so the next strict transform is this pullback itself. Hence finitely many local flattenings can be combined without undoing those already achieved.

We also need an exactness statement stronger than injectivity at a generic point.

**A.1. Pure strict-transform exactness.** Suppose
\[
0\longrightarrow N_1\longrightarrow N_2\longrightarrow N_3\longrightarrow0
\]
remains exact after every base change of \(S\). Their strict transforms form a short exact sequence. After a blowup chart the sequence is still pure over its base ring \(R'\). The only issue is exactness in the middle. If the class of \(x\in N_2\) maps to power torsion in \(N_3\), then \(a^nx=y\in N_1\). Purity modulo \(a^n\) gives \(y=a^nz\) for \(z\in N_1\); thus \(a^n(x-z)=0\), and the class of \(x\) is the image of the class of \(z\). The outside injectivity and surjectivity follow directly from power-torsion quotients. The element mapping to the class of \(x\) is \(z\).

**A.2. Composition at arbitrary qcqs scope.** Let \(b:S_1=\operatorname{Bl}_I S\to S\), where \(S\) is qcqs and \(I\) is finite type. Let \(J_1\subset\mathcal O_{S_1}\) be finite type. There exist \(d>0\) and a finite-type ideal \(J\subset I^d\) such that
\[
 J\mathcal O_{S_1}=(I\mathcal O_{S_1})^dJ_1.
\]
Here is the required twist argument without a Noetherian hypothesis. On an affine base write the Rees algebra as a degree-one generated algebra, with finitely many generators \(u_i\). The standard opens \(D_+(u_i)\) are affine. Choose finitely many generators of \(J_1\) on each. Clear each homogeneous denominator to obtain a homogeneous numerator. A power of \(u_i\) makes that numerator lie in \(J_1\) globally: its class in the quasi-coherent quotient restricts to zero on \(D_+(u_i)\); on each of the finitely many standard charts the localization equality criterion kills that class by a power of \(u_i\), and a common power works. Increase the degrees to a common \(d\), multiplying the \(i\)-th numerators by powers of \(u_i\). Their degree-\(d\) images generate \(J_1(d)\) on the \(i\)-th chart and lie in it on every chart. They form a finite submodule of \(I^d\) with the displayed pullback property.

For a finite affine cover of \(S\), first make these degrees common by multiplying by the appropriate powers of \(I\). The local submodules lie in the quasi-coherent kernel
\[
 K=\ker\left(I^d\longrightarrow b_*(\mathcal O_{S_1}(d)/J_1(d))\right).
\]
The pushforward is quasi-coherent because \(b\) is qcqs. G.1 supplies finite-type submodules of \(K\) containing these local generators, extended from the respective base opens. Their finite sum is the desired global \(J\). Its pullback is contained in the right-hand side by the kernel definition and equals it on every chosen open. If \(I|_U=\mathcal O_U\) and \(J_1|_{b^{-1}U}=\mathcal O\), the equality over the isomorphism \(b^{-1}U\cong U\) also gives \(J|_U=\mathcal O_U\).

Multiplying a centre by an invertible ideal leaves its blowup unchanged: locally an invertible regular generator multiplies degree \(n\) by its \(n\)-th power, so the degree-zero localized charts are identical; these identifications glue under changes of generator. Thus \(\operatorname{Bl}_{J_1}S_1=\operatorname{Bl}_{J\mathcal O_{S_1}}S_1\). Blowing up \(I\), then the pullback of \(J\), equals \(\operatorname{Bl}_{IJ}S\). Indeed the two effective Cartier exceptional ideals on the composite make \(IJ\) invertible, hence give a map to the product blowup. Conversely the factor-invertibility calculation above gives successive maps from that product blowup to the two blowups. The composites are identities by uniqueness in their universal properties. This proves the composition assertion and its \(U\)-admissibility. It uses G's completeness support, whose independent space approximation route has no flattening input, so there is no circular flattening argument.

#### 5.6.6. Projectivity and purity of the base module

The important projectivity assertion concerns an infinite module over the base, not finite local freeness of an affine morphism:

**B.1.** If \(R\to A\) is flat and finitely presented and every fibre \(A\otimes_R\kappa(\mathfrak p)\) is geometrically integral, then \(A\) is a projective \(R\)-module.

We give the algebraic support rather than conceal it inside a coefficient argument. A map is **pure** if it remains injective after tensoring with every module over the stated base ring.

**B.2. Local purity test.** For a local ring \((R,\mathfrak m)\), a projective module \(P\), a flat module \(N\), and an \(R\)-linear map \(u:P\to N\), injectivity modulo \(\mathfrak m\) implies purity. Choose \(C\) with \(P\oplus C\) free, and apply the free case to \(u\oplus1_C:P\oplus C\to N\oplus C\). In the free case it is enough to consider a finite set of basis vectors. By Lazard's theorem their map factors through a finite free module in a filtered presentation of the flat target. Its reduction modulo \(\mathfrak m\) is injective and stays injective at every later stage. A matrix of full column rank over the residue field has a unit maximal minor; its map is a split injection over the local ring. Tensoring with any \(R\)-module preserves that injection, and filtered colimits preserve it. The reduction to the finite set of basis vectors proves the whole free case. This proof uses no finite-rank hypothesis on \(P\).

Here is the completion argument for B.1. We include the particular module criterion it uses. For a flat module \(M\), call the finite-coefficient condition the assertion that for every finite free \(F\) and \(x\in F\otimes_RM\), there is a smallest submodule \(F_x\subset F\) with \(x\in F_x\otimes_RM\). This is the flat Mittag–Leffler condition. The following proof explains the needed consequences.

Write \(M=\varinjlim F_i\) with finite free \(F_i\), using Lazard. For \(j\geq i\), let
\[
 Q_{ij}=\operatorname{im}(F_j^*\to F_i^*).
\]
These submodules decrease. The map \(F_i\to M\), regarded as a tensor in \(F_i^*\otimes M\), has a smallest coefficient submodule \(Q_i\). It lies in every \(Q_{ij}\). Express this tensor by finitely many elements of \(Q_i\), lift their coefficients to a common stage, and increase the stage so that the equality holds there. The transition \(F_i\to F_j\) then has all its rows in \(Q_i\), so \(Q_{ij}\subset Q_i\). Therefore the \(Q_{ij}\) stabilize. Conversely stable \(Q_{ij}\) give the same minimal-coefficient condition by lifting a tensor from a finite free stage. Equality of these dual images says that the map \(F_i\to F_j\) factors through every sufficiently late \(F_i\to F_k\): each row of its matrix is a linear combination of the rows of the latter matrix. This also proves that, for every \(L\), the images of \(\operatorname{Hom}(F_j,L)\to\operatorname{Hom}(F_i,L)\) eventually stabilize.

If \(M\) is countably generated, choose stages containing its generators and repeatedly add the stabilization stages just described, together with common upper bounds. The resulting countable directed subsystem has colimit \(M\): it is surjective because it contains the generators, and every relation killed in the original system is killed by one of the selected stabilization maps. Choose a cofinal sequence in this subsystem. Applying \(\operatorname{Hom}(F_i,-)\) to a short exact sequence and then taking inverse limits is exact, because the inverse system of kernels has stabilizing images. Explicitly, replace the kernels by their eventual images; their transition maps are surjective, so successive lifts of a compatible right-hand element can be corrected at the next stage to form a compatible sequence. Hence \(\operatorname{Hom}(M,-)\) is exact: a countably generated flat module with this condition is projective.

The condition descends faithfully flatly. In a finite-free Lazard system, flat extension \(R\to R_1\) takes \(Q_{ij}\) to \(Q_{ij}\otimes_RR_1\). If the latter stabilize, faithful flatness reflects equality of the former. Thus projectivity descends for countably generated modules: flatness descends, the condition descends, and the preceding paragraph applies. Countable generation itself descends by expressing a countable generating family over \(R_1\) as finite sums of tensors and taking their countably many \(R\)-components.

For a Noetherian ring \(R\), any product \(R^{\Lambda}\) is flat: tensor a finitely generated ideal into the product, using its finite presentation, to reduce injectivity to each coordinate. It has the finite-coefficient condition. A tensor in \(F\otimes_RR^{\Lambda}=F^{\Lambda}\) is a family \(x_\lambda\in F\); the submodule generated by these vectors is finite and finitely presented, and is exactly its smallest coefficient submodule. Pure submodules inherit the condition: if a tensor in \(F\otimes M\subset F\otimes N\) lies in \(F'\otimes N\), its image in \((F/F')\otimes N\) vanishes; purity makes its image in \((F/F')\otimes M\) vanish as well. Flatness then identifies the kernel with \(F'\otimes M\).

Suppose now that \(R\) is Noetherian and \(I\)-adically complete. The completion \(\widehat{\bigoplus_\Lambda R}\) consists of families tending to zero \(I\)-adically and embeds purely in \(\prod_\Lambda R\). For the tensor test take a finite \(R\)-module \(L\), a finite presentation of \(L\), and a matrix presenting its relations. If a family tending to zero represents zero after tensoring into the product, each coordinate lies in the image of that matrix. Artin–Rees gives a uniform constant \(c\): a relation vector in \(I^nR^m\) lifts to coefficients in \(I^{n-c}R^k\). Choose these lifts coordinate by coordinate; they also tend to zero. Thus the tensor kernel already vanishes in the completed sum. Every module is a filtered colimit of finite modules over a Noetherian ring, so this proves purity for all tensors. The completed sum is therefore flat and has the finite-coefficient condition.

If \(M\) is flat and \(M/IM\) projective, choose a free surjection \(P\to M\) with kernel \(K\). The sequences
\[
0\to K/I^nK\to P/I^nP\to M/I^nM\to0
\]
are exact. The right-hand terms are projective over \(R/I^n\): projectives lift through a nilpotent ideal by lifting an idempotent on a free module; the polynomial correction \(e\mapsto e+(1-2e)(e^2-e)\) squares its error, so finitely many corrections suffice. A lifted projective mapping to a flat module with the same reduction is an isomorphism by the finite \(I\)-adic filtration. Choose compatible sections of the displayed sequences. Given a section modulo \(I^n\), choose any section modulo \(I^{n+1}\) and lift their difference, a map into \(K/I^nK\), to \(K/I^{n+1}K\); projectivity of \(M/I^{n+1}M\) permits this correction. The limits split, so \(\widehat M\) is a direct summand of \(\widehat P\), and is flat with the finite-coefficient condition.

We apply this with \(M=A\), where \(R\) is complete and every fibre of \(A\) is geometrically integral. For every prime \(\mathfrak p\subset R\), \(A/\mathfrak pA\) is a domain: it is flat over the domain \(R/\mathfrak p\), embeds in its generic fibre, and that generic fibre is a domain. A prime filtration of a finite \(R\)-module \(L\), tensored with flat \(A\), shows that every associated prime of \(L\otimes_RA\) belongs to the finite list of primes \(\mathfrak pA\) coming from that filtration. Because \(I\subset\operatorname{Jac}(R)\), each \(\mathfrak p+I\) is proper. The map \(R\to A\) is faithfully flat, since its integral fibres are nonempty, so \(\mathfrak pA+IA\) is proper as well.

Consequently \(A\to\widehat A\) is pure over \(R\). Indeed, for each finite \(L\), an associated prime \(\mathfrak q\) of \(L\otimes A\) is contained in a prime containing \(IA\). In that local ring Krull intersection makes the kernel of \(L\otimes A\to\widehat{L\otimes A}\) zero. Localization at its associated primes therefore makes the kernel zero everywhere. The canonical map from \(L\otimes\widehat A\) to that completion shows that \(L\otimes A\to L\otimes\widehat A\) is injective. Filtered colimits give all \(L\). If \(A/IA\) is projective, the preceding completion argument and purity imply that \(A\) is flat with the finite-coefficient condition. It is countably generated over \(R\), since it is a finite-type \(R\)-algebra. It is therefore projective.

To prove B.1 when \(R\) is Noetherian, assume otherwise and take a maximal ideal \(J\subset R\) such that \(A/JA\) is not projective over \(R/J\). If \(J\ne\sqrt J\), projectivity modulo \(\sqrt J/J\) and the nilpotent lifting argument contradict this choice. Replace \(R,A\) by their quotients by \(J,JA\). We have reduced to \(R\) reduced and \(A/IA\) projective for every nonzero ideal \(I\subset R\). Choose \(0\ne f\in R\) such that \(A_f\) is free, by Noetherian generic freeness; to do this, choose an element outside one minimal prime and inside every other minimal prime, using prime avoidance. Its localization is a domain because \(R\) is reduced; then generic freeness supplies a further nonzero localization. Their product is the required nonzero \(f\). The primes outside this open are covered by the completion factor, so no component is discarded. The map
\[
 R\longrightarrow R_f\times\widehat R_{(f)}
\]
is faithfully flat. Completion is flat, it covers the primes containing \(f\), and \(R_f\) covers the other primes. The base change of \(A\) to the completion is projective by the previous paragraph, since its reduction modulo \(f\) is projective. The base change to \(R_f\) is free. Countable projectivity descends, a contradiction.

For arbitrary \(R\), the finite-presentation data descend to a Noetherian model with flat, geometrically integral fibres by C. The Noetherian result makes the model algebra projective over its base; base change makes \(A\) projective over \(R\). This completes B.1 in its stated generality.

#### 5.6.7. Flat and geometrically integral finite models

We require two finite-stage assertions beyond merely writing down the coefficients of an algebra. Both are proved here; we use AG-MO-03 for finite-presentation objects, maps, relations and quasi-compact opens in a filtered limit.

**C.1. Flat module models.** If \(A\) is a finitely presented \(R\)-algebra and \(M\) a finitely presented \(A\)-module flat over \(R\), they descend to a finite-type \(\mathbf Z\)-algebra \(R_0\), a finitely presented \(R_0\)-algebra \(A_0\), and a finite \(A_0\)-module \(M_0\) flat over \(R_0\). More generally flatness is eventually true in any compatible filtered finite-presentation model system.

First consider a point, and localize the base and source at its images. Present the local algebra by finitely many equations followed by localization at the chosen prime, and present the module by a finite matrix. Their local models \(R_i\to A_i,M_i\) are Noetherian; transitions in \(A_i\) are localizations of base change. At a fixed stage the finite \(A_i\)-module
\[
 T_i=\operatorname{Tor}_1^{R_i}(M_i,R_i/\mathfrak m_i)
 =\ker(\mathfrak m_i\otimes_{R_i}M_i\to M_i)
\]
has finitely many generators. In the limit they vanish, by flatness of \(M\). At a later stage \(j\) their images vanish in
\(
\operatorname{Tor}_1^{R_j}(M_j,R_j/\mathfrak m_iR_j).
\)
Since \(M_i/\mathfrak m_iM_i\) is a vector space, it is flat over \(R_i/\mathfrak m_i\). The ideal form of the Noetherian local criterion therefore makes \(M_j\) flat over \(R_j\). Here is the needed change-of-base detail: for local Noetherian maps and \(I\subset R_i\), the map
\[
\operatorname{Tor}_1^{R_i}(M_i,R_i/I)\otimes_{R_i}R_j
\longrightarrow\operatorname{Tor}_1^{R_j}(M_j,R_j/IR_j)
\]
is surjective when \(M_i/IM_i\) is \(R_i/I\)-flat. The change-of-rings Tor sequence for \(R_i\to R_i/I\to R_j/IR_j\) gives surjectivity onto \(\operatorname{Tor}_1^{R_i}(M_i,R_j/IR_j)\); the change-of-rings sequence for \(R_i\to R_j\) then gives surjectivity onto the last Tor group. Localization of the source algebra preserves this surjectivity. Vanishing of the indicated image thus annihilates that group, exactly as the local criterion requires.

For global affine models, the flat locus of \(M_i\) in \(\operatorname{Spec}A_i\) is open by the Noetherian theorem in AG-FSE-02. The local argument covers \(\operatorname{Spec}A\) by inverse images of these loci. Quasi-compactness gives one stage where their union covers it. At that stage the complement is \(V(J)\) with \(JA=A\); finitely many coefficients witnessing \(1\in JA\) descend to a later stage. At that later stage the whole module is flat. This proves existence of a flat Noetherian model. To prove eventual flatness in a prescribed compatible system, descend the isomorphism with this flat model and its inverse: their composites become identity at a finite stage because all data are finitely presented. All later compatible models are its base changes and are flat.

**C.2. Geometrically integral algebra models.** In a Noetherian finite-type family, the locus of geometrically integral fibres is constructible. We supply the finite-type geometric reasoning needed for that assertion.

Over an integral affine base with field of fractions \(K\), a geometrically reduced generic fibre has a dense smooth open: at its generic points the function fields are separably generated over \(K\), so a separating transcendence basis and a separable minimal polynomial exhibit a smooth neighbourhood. Let \(V\) be the smooth locus in the family. Its generic fibre is schematically dense. On an affine chart \(\operatorname{Spec}B\), choose finitely many \(g_i\) with \(D(g_i)\subset V\) covering that generic open. The generic map \(B_K\to\bigoplus B_K\), \(b\mapsto(g_i b)_i\), is injective (the \(g_i\) avoid the associated primes collectively). Generic freeness makes its cokernel and \(B\) base-flat after shrinking. The map is then injective before taking fibres, and remains injective after every field extension. Thus \(V\) is schematically dense in every geometric fibre there. A schematically dense reduced open forces the whole fibre reduced: any nilpotent restricts to zero and schematic density kills it.

If the generic fibre is not geometrically reduced, it has a nonzero nilpotent after a finite extension \(K'/K\). Spread that finite field extension to a finite free domain algebra over a shrunk base (adjoin successively roots of monic polynomials and clear the finitely many relations). Spread the nilpotent \(h\), with \(h^n=0\). Generic freeness of the ideal \((h)\) and its quotient makes the ideal inject into every fibre and nonzero in every fibre: its generic free rank is positive. Each such fibre is nonreduced. The finite flat base change is surjective after shrinking, so all fibres of the original family there fail geometric reducedness.

A geometrically integral generic fibre spreads to geometrically integral fibres. Use its separably generated function field to find a birational hypersurface presentation over \(K\): a separating transcendence basis \(t_1,\ldots,t_d\), followed by one separable algebraic generator, gives an absolutely irreducible polynomial \(P(t_1,\ldots,t_d,z)\). Clear denominators, and shrink until the family and this hypersurface have isomorphic nonempty opens, dense in every geometric fibre. The required density is the schematic-density argument just proved, applied to the reduced generic fibres. Absolute irreducibility of \(P\) persists after shrinking: make \(P\) monic in one variable by a triangular power substitution and invert its leading coefficient. For each split of its monic degree into **two positive degrees**, the possible coefficients of monic factors satisfy finitely many polynomial equations, with bounded degrees in the remaining variables. Their finite-type coefficient algebra has zero generic fibre, because no factorization exists over \(\overline K\). Some nonzero base element makes that algebra zero. The product of the finitely many such elements excludes every nontrivial factorization in every residue field extension. Degree-zero monic factors are \(1\), so are excluded, not counted as an obstruction. The common open is integral in every geometric fibre; being dense forces the original fibre irreducible, and the preceding reducedness result makes it integral.

If a geometrically reduced generic fibre is geometrically reducible, a finite separable extension splits its finitely many geometric irreducible components. This follows by taking their finitely generated defining ideals over a separable closure and descending their finitely many coefficients. Spread the field extension to a finite étale cover of a shrunk integral base. Close the distinct components in the family. Their union covers the family after shrinking, since the complement has empty generic fibre. The opens obtained by removing the other component closures are nonempty in the generic fibre; generic freeness and openness make all these opens nonempty in every fibre after shrinking. At least two are disjoint nonempty opens in each fibre, so each fibre is reducible. Surjectivity of the finite étale base change gives the same failure of geometric irreducibility downstairs. An empty generic fibre similarly gives empty fibres after shrinking, by descending the equation \(1=0\) on affine charts.

These arguments decide geometric integrality on a dense open of every irreducible closed base subspace. Noetherian induction supplies a finite constructible partition, proving the asserted constructibility. The small field facts used here follow from the separating-basis criterion for geometric reducedness, finite-coefficient descent over a separable closure, and ordinary field theory; they do not require the general geometric-component theorem as an extra provider.

Now descend \(A/R\) to a flat Noetherian finite-presentation model, using C.1 with \(M=A\). Let \(E\) be its constructible good locus. The image of \(\operatorname{Spec}R\) lies in \(E\), because geometric integrality is preserved and reflected by field extension. A limit lying in a constructible subset lies there at a finite stage: decompose the complement into finitely many locally closed affine pieces and use eventual emptiness of each piece, which is a finite equation \(1=0\) after the prescribed localizations and quotients. This is the constructible-containment limit comparison assigned in AG-MO-03. At that stage every fibre is geometrically integral. The finite-type model base is still Noetherian. This proves the model assertion used in B.1.

#### 5.6.8. Elementary local dévissage

**D.1 (F1).** Let \(T\to S\) be a locally finite-type morphism of schemes, \(N\) a finite-type quasi-coherent module, and \(t\in\operatorname{Supp}(N_s)\), where \(s\) is its image. Put \(d=\dim_t\operatorname{Supp}(N_s)\). There are affine elementary étale neighbourhoods \((T_0,t_0)\to(T,t)\), \((S_0,s_0)\to(S,s)\), a closed immersion \(i:Z_0\to T_0\) of finite presentation, a finite morphism \(\pi:Z_0\to P_0\), and a smooth surjective morphism \(P_0\to S_0\) of relative dimension \(d\), with geometrically integral fibres, such that
\[
 i_*G=N|_{T_0},\quad
 \pi^{-1}(p_0)=\{t_0\},\quad
 \kappa(p_0)/\kappa(s_0)\text{ is purely transcendental}.
\]
An elementary neighbourhood includes the specified equality of residue fields at the selected point. If \(t\notin\operatorname{Supp}(N_s)\), Nakayama makes \(N\) zero near \(t\), and that neighbourhood needs no dévissage.

Work first on affine neighbourhoods, \(S=\operatorname{Spec}R,T=\operatorname{Spec}A\). Write \(I=\operatorname{Ann}_A N\). On the fibre, \(\operatorname{Supp}(N_s)=V(I\,A\otimes_R\kappa(s))\): at each fibre prime this follows from Nakayama applied to the finite local module. The fibre algebra is Noetherian. Choose finitely many elements of \(I\) whose extended ideal generates \(I\,A\otimes_R\kappa(s)\). They cut out a closed finitely presented \(Z\subset T\) on which \(N=i_*G\), and \(Z_s\) has exactly the support above. Thus we may apply the geometric construction to \(Z\to S\) of fibre dimension \(d\) at \(t\).

Noether normalization on a sufficiently small fibre neighbourhood gives a quasi-finite map to \(\mathbf A^d_S\) after lifting the chosen polynomial coordinates. The purely transcendental residue field can also be arranged, rather than assumed. For a prime \(\mathfrak q\subset k[x_1,\ldots,x_d]\), with \(r=\operatorname{trdeg}_k\kappa(\mathfrak q)\), a finite polynomial coordinate map can send its inverse image to \((y_{r+1},\ldots,y_d)\). Here is the refinement of ordinary normalization. Induct on \(d\). If \(r=d\), the prime is zero. Otherwise choose a nonzero polynomial in it, make that polynomial monic in \(x_d\) by a triangular power substitution, and use it as the last coordinate. The remaining contracted prime is in \(k[x_1,\ldots,x_{d-1}]\); apply the induction hypothesis there. Each coordinate step is finite because it gives a monic equation for \(x_d\), and the contracted prime has the required form. Lift these finitely many polynomial coefficients from \(\kappa(s)\) after shrinking the base. The composite is quasi-finite at the selected point; restrict to its open quasi-finite locus. Its image point \(p\in\mathbf A^d_s\) now has residue field \(\kappa(s)(y_1,\ldots,y_r)\).

Apply the elementary étale finite-part theorem of AG-FSE-07 to this quasi-finite map at the selected point. It gives an elementary étale neighbourhood \(P\to\mathbf A^d_S\) and an open in the pulled-back \(Z\) which is finite over \(P\), with exactly one point over the selected \(p\). The morphism \(P\to S\) is smooth of relative dimension \(d\), and the residue field at \(p\) remains purely transcendental. Replace \(P\) by an affine neighbourhood and its finite inverse image by the corresponding affine neighbourhood.

We next arrange geometrically integral fibres of \(P\), while preserving an **elementary** base neighbourhood. Let \(C\subset P_s\) be the connected component containing \(p\). It is open and closed and is geometrically connected: over a separable closure, the finite geometric connected components form a Galois set. A point with purely transcendental residue field has geometrically connected inverse image, so lies in a Galois-fixed component. Connectedness over the original field forces the action on the components to be transitive, hence there is only one. Purely inseparable extensions do not change connectedness. Smooth geometric fibres are regular; a connected Noetherian regular scheme is integral because its irreducible components are disjoint. Thus \(C\) is geometrically integral.

We use the following smooth-family component construction. For a smooth finite-presentation morphism \(Y\to B\) with section \(z\), the union \(Y^0\) of the fibre connected components meeting \(z\) is open and its formation commutes with base change. Base-change compatibility follows from the preceding rational-point argument. Over a Noetherian base it is constructible: on an integral closed base stratum, separate the generic connected component from its complement by their closures; their intersection and the uncovered locus have empty generic fibre and disappear after shrinking. The component containing the section has geometrically integral generic fibre. C.2 makes its fibres geometrically integral after shrinking. This supplies an open-and-closed component description on a dense open of each stratum, so Noetherian induction proves constructibility.

It is stable under generization. For a generization \(y'\leadsto y\in Y^0\), realize the specialization by a morphism from a discrete valuation ring into \(Y\). In the resulting smooth family over that ring, remove the other components of the special fibre. The section and the specializing point now lie in the same connected component of the total space. A scheme smooth over a discrete valuation ring is regular; its connected components are integral. Their generic fibres are integral, so the two generic points lie in the same fibre connected component. Thus \(y'\in Y^0\). Constructibility and generization stability make \(Y^0\) open. Over an arbitrary base, descend the smooth family and section to a Noetherian finite-presentation model; standard smooth equations and the Jacobian unit minor descend at a finite stage. Pull back its component open. Base-change compatibility proves the assertion for the original family.

For completeness, the discrete valuation ring in this argument needs no excellence assumption. Given a nontrivial specialization in a Noetherian scheme, quotient its local ring at the special point by the generic-point prime, obtaining a nonfield Noetherian local domain \(D\). A valuation ring of its fraction field dominating \(D\) exists by maximality among dominating local subrings. Choose a maximal-ideal generator of minimum valuation and adjoin the ratios of the other generators to it. Its ideal is now principal and proper; localize at a minimal prime over it. The principal ideal theorem gives a one-dimensional Noetherian local domain dominating \(D\). Its normalization is Noetherian by the following elementary Krull–Akizuki argument. For a one-dimensional local domain \(E\), fraction field \(K\), and any submodule \(L\subset K^n\),
\[
\operatorname{length}_E(L/xL)\leq n\operatorname{length}_E(E/xE),\quad0\ne x\in E.
\]
For a finite full-rank submodule, sandwich it between \(x^cE^n\) and \(E^n\), compare the lengths modulo \(x^m\), and divide the resulting bounds by \(m\to\infty\). For arbitrary \(L\), any finite strict chain modulo \(xL\) lifts to a finite submodule, giving the same bound. A nonzero ideal of an intermediate ring \(E\subset E'\subset K\) meets \(E\); therefore it contains \(xE'\), and its quotient by \(xE'\) has finite length over \(E\). The ideal is finitely generated, proving \(E'\) Noetherian. Apply this to the normalization and localize at a maximal ideal above that of \(E\). The resulting one-dimensional normal local ring is a DVR by *Discrete valuation rings, normal rings and Serre’s criterion*, Theorem 1.2. Its local map realizes the required specialization. A trivial specialization can use \(\kappa(y)[t]_{(t)}\).

To use the component construction without changing the selected base residue field, first choose a closed separable point \(c\in C\). Such a point exists in a nonempty smooth variety: an étale chart has an open image in affine space, which has a point over a finite separable extension, and a point of an étale fibre has separable residue field. At \(c\), choose parameters vanishing there whose differentials form a basis. They give an étale map near \(c\) from \(P\) to \(\mathbf A^d_S\). Its inverse image of the zero section is étale and quasi-finite over \(S\). AG-FSE-07, applied on the base, gives an **elementary** neighbourhood \((S_0,s_0)\to(S,s)\) in which the selected finite part \(D\to S_0\) is finite étale, nonempty, and has a map \(D\to P_{S_0}\). Shrink \(S_0\) to make \(D\to S_0\) surjective.

On \(P_D\to D\), the multisection becomes a section. Take its component open \(P_D^0\). On \(D\times_{S_0}D\), the two component opens agree over the selected fibre, because that fibre component is geometrically connected. Membership of either section in the other component open is an open condition. Since \(D\times_{S_0}D\to S_0\) is finite, remove the image of the closed disagreement locus. The two opens then agree everywhere. Faithfully flat descent of open subsets descends \(P_D^0\) to an open \(P_0\subset P_{S_0}\), with selected fibre \(C\), and all fibres geometrically integral. Shrink to affine neighbourhoods as follows: choose an affine \(V\subset P_0\) containing \(p\), then an affine base neighbourhood inside its open image. Its inverse image in \(V\) is affine and surjective; its fibres are nonempty opens of integral fibres. Finite inverse images remain affine.

Finally lift the elementary étale neighbourhood of \(Z\) to one of \(T\). Over the chosen base neighbourhood work with the closed immersion \(Z_{S_0}\subset T_{S_0}\). Near the selected point an étale algebra over its quotient ring has a standard étale presentation. Lift its monic polynomial, the localization element and the invertible derivative to the ambient ring. This defines an étale neighbourhood \(T_0\to T_{S_0}\) whose closed pullback is the prescribed neighbourhood of \(Z\); shrink both to the selected standard étale open. If this restricts the finite source, remove from \(P_0\) the image of its closed complement: finiteness makes that image closed, and it avoids the selected point because the selected finite fibre has just one point. The remaining finite inverse image lies entirely in the chosen open. The residue field is unchanged. Its closed ideal is the pullback of the finite-type ideal defining \(Z\), so \(i:Z_0\to T_0\) is finitely presented. Pullback of \(i_*G=N\) along this flat map gives the asserted identity. This proves all the data of F1, including the return to the original module.

#### 5.6.9. Generic bases and Fitting ideals

**E.1 (F2, affine constant-rank form).** Let \(R\to A\) be flat and finitely presented with geometrically integral fibres. Let \(f\in R\), let \(N\) be a finite \(A\)-module with \(N_f\) finitely presented, and suppose \(N_{\mathfrak pA}\) is free of rank \(r\) for every \(\mathfrak p\notin V(f)\). There is a finite ideal \(I\subset R\), \(V(I)=V(f)\), such that on every blowup chart \(R'=R[I/a]\), the strict transform \(N'\) is free of rank \(r\) on an open of \(\operatorname{Spec}A'\), \(A'=A\otimes_RR'\), meeting the generic point of every fibre over \(R'\).

Choose a finitely presented \(A\)-module \(N_0\twoheadrightarrow N\) inducing an isomorphism after inverting \(f\): choose generators of \(N\), then finitely many relations generating their kernel after localization. A blowup chart has \(R'_a=R_a\). Since \(a\in fI_0\), this is a localization of \(R_f\), so the strict transforms \(N_0'\to N'\) agree after inverting \(a\). Their kernel is power torsion, and \(N_0'\) has none; the map is also surjective. Thus it is enough to prove E.1 for finitely presented \(N\). We do not identify the whole chart localization with \(R_f\).

Let \(J=\operatorname{Fitt}_r(N)\subset A\), a finite ideal. B.1 supplies a splitting \(A\oplus C=\bigoplus_\lambda R\). Let \(I_0\subset R\) be the ideal of coefficients of elements of \(J\) in this free module. It is finite: take finitely many generators of \(J\); multiplication by any element of \(A\) is \(R\)-linear and extends through the projection onto the \(A\)-summand, so the coefficients of all their multiples lie in the coefficient ideal already generated by this finite list. Set \(I=fI_0\). At \(\mathfrak p\notin V(f)\), generic-fibre freeness makes \(J\) nonzero in the fibre algebra. Some coefficient is nonzero there, so \(I_0\not\subset\mathfrak p\). Hence \(V(I)=V(f)\).

On \(R'=R[I/a]\), write \(a=fb\) with \(b\in I_0\). Then \(I_0R'=(b)\), and both \(a\) and \(b\) are regular. Every generator \(h\in J\) has coefficients divisible by \(b\). Dividing its coefficient vector by \(b\) gives a vector in the \(A'\)-summand: apply its projector and use regularity of \(b\) to check this. Thus \(h=b\widetilde h\) in \(A'\). The coefficients of the finitely many \(\widetilde h\) together generate the unit ideal of \(R'\), because the coefficients of the \(h\) generate \(I_0R'=(b)\).

Fix \(\mathfrak p'\subset R'\). A normalized coefficient is a unit on a base neighbourhood of \(\mathfrak p'\); therefore its corresponding \(\widetilde h\) is nonzero in \(A'\otimes_{R'}\kappa(\mathfrak p')\). This fibre is a domain, so \(\widetilde h\) is a unit in its fraction-field localization. Consequently
\[
 J A'_{\mathfrak p'A'}=(b).
\]
No assertion that \(\widetilde h\) is a unit in the whole polynomial or source algebra is used.

We recall the principal-Fitting calculation. If a finite module \(L\) over a local ring has \(\operatorname{Fitt}_r(L)=(b)\), then \(L/\ker(b:L\to L)\) is generated by \(r\) elements. In a presentation with \(n\) generators, a finite list of relations contains an \((n-r)\)-minor generating \((b)\), by Nakayama. Multiply the selected relation block by its adjugate. Every coefficient on one of the remaining \(r\) generators is a same-size minor, hence belongs to \((b)\). Write those coefficients as multiples of \(b\). The resulting relations say that \(b\) times each of the first \(n-r\) generators is \(b\) times a combination of the remaining generators. Their differences lie in \(\ker(b:L\to L)\). Thus the remaining \(r\) classes generate the quotient; no cancellation of a possibly zerodivisor \(b\) is assumed. This proves the calculation, also when the relation module itself is not finite. Apply it at \(\mathfrak p'A'\). Since \(b\)-torsion is \(a\)-power torsion, \(N'\) is generated by \(r\) elements on a neighbourhood \(D(g)\) of that generic fibre point.

Those generators have no relations. Their relation-coordinate ideal is \(\operatorname{Fitt}_{r-1}(N')\) on \(D(g)\). After inverting \(a\), it vanishes at each generic fibre point by the rank assumption. The algebra \(A'_a\) injects into the product of these generic-fibre localizations: localize at each base prime; an element outside its fibre prime acts injectively, by B.2 applied to its multiplication on the projective base module in B.1, and localization preserves that injection. Thus the relation ideal becomes zero in \(A'_a\). Regularity of \(a\) on the flat algebra \(A'\) kills any ideal vanishing after inverting \(a\). All relation coordinates are zero, so \(N'|_{D(g)}\cong(A'|_{D(g)})^r\). For \(r=0\), the principal-Fitting calculation already gives the zero module. Taking the union of these neighbourhoods proves E.1.

**E.2 (F2, global form).** Let \(S\) be a qcqs scheme and \(T\to S\) an affine, flat, finitely presented morphism of schemes with geometrically integral fibres. Let \(N\) be finite, \(N|_{T_U}\) finitely presented, and \(N\) base-flat at the generic points of all fibres over a quasi-compact open \(U\subset S\). There is a \(U\)-admissible blowup and an open \(V\subset T_{S'}\) surjecting onto \(S'\) on which the strict transform is finite locally free.

The generic rank on \(U\) is locally constant. Indeed a finitely presented module which is base-flat and free on the selected fibre at a point is locally free near that point. To see that criterion in this generality, use C.1 to obtain a base-flat Noetherian module model. Fibre flatness at the selected point descends along the faithfully flat local field-extension map; the Noetherian fibrewise criterion in AG-FSE-02 gives flatness over the source algebra there, hence local freeness for a finite module. Pull back that open. The image of the open is open, since \(T\to S\) is flat and finitely presented. Geometric integrality makes it meet the unique generic point of every fibre in that image, with the same rank. This proves local constancy. There are finitely many ranks because \(U\) is quasi-compact.

Separate its finitely many clopen rank pieces by admissible blowups. For disjoint quasi-compact opens \(U_1,U_2\), choose finite ideals with vanishing sets their complements. Their product is nilpotent; a common power of both makes their product zero. Blow up their sum. Charts whose denominator lies in the first ideal annihilate the second, and conversely; charts of opposite kinds have empty intersection, since their product denominator is zero and regular. Thus the blowup splits into two disjoint opens containing the respective \(U_i\). Repetition separates all rank pieces. Make \(S\setminus U\) Cartier, take finitely many affine charts with local equation \(f\), and apply E.1. Extend and combine their centres as in A. Flat strict transforms on the constructed open stay locally free after pullback, and flatness of \(T\to S\) ensures all base changes still have nonempty geometrically integral fibres. The combined open therefore still surjects onto the modified base. This proves F2 at arbitrary qcqs scope.

**E.3 (F3).** Let \((R,\mathfrak m)\) be local, \(A/R\) flat and finitely presented with geometrically integral fibres, \(\mathfrak p=\mathfrak mA\), \(\mathfrak q\supset\mathfrak p\) a prime over \(\mathfrak m\), and \(N\) finite over \(A\). Choose an \(A\)-linear map \(\alpha:A^r\to N\) inducing a basis isomorphism over \(\kappa(\mathfrak p)\). Then the following are equivalent:

1. \(N_{\mathfrak q}\) is \(R\)-flat.
2. \(\alpha\) is pure over \(R\), and \((\operatorname{coker}\alpha)_{\mathfrak q}\) is \(R\)-flat.
3. \(\alpha\) is injective, and that cokernel localization is \(R\)-flat.
4. \(\alpha_{\mathfrak p}\) is an isomorphism, and that cokernel localization is \(R\)-flat.
5. \(\alpha_{\mathfrak q}\) is injective, and that cokernel localization is \(R\)-flat.

Such \(\alpha\) exists by taking a basis from the images of finitely many generators of \(N\). If (1) holds, \(N_{\mathfrak p}\) is \(R\)-flat. The reduction of \(A^r\to N_{\mathfrak p}\) modulo \(\mathfrak m\) is injective, since \(A/\mathfrak mA\) is a domain and the map becomes the chosen basis isomorphism over its fraction field. B.1 and B.2 make that map pure. Its factorization through \(N\) makes \(\alpha\) pure as well. Localize at \(\mathfrak q\); the Tor sequence and flatness of \(N_{\mathfrak q}\) make its cokernel flat. Thus (1) implies (2), and (2) implies (3).

If (3) holds, Nakayama at the local ring \(A_{\mathfrak p}\) makes \(\alpha_{\mathfrak p}\) surjective; it is already injective, giving (4). Every element of \(A\setminus\mathfrak p\) acts purely, hence injectively, on \(A\): apply B.2 to multiplication, whose reduction is nonzero multiplication on the integral fibre. Therefore \(A_{\mathfrak q}\to A_{\mathfrak p}\) is injective. An isomorphism at \(\mathfrak p\) consequently makes \(\alpha_{\mathfrak q}\) injective, proving (4) implies (5). Finally (5) gives \(N_{\mathfrak q}\) as an extension of two \(R\)-flat modules, hence flat. This proves F3, including the original non-Noetherian local base.

#### 5.6.10. Flattening by admissible blowups

**F.1.** Let \(S\) be a qcqs scheme, \(T\to S\) a locally finitely presented morphism of schemes with \(T\) quasi-compact, \(N\) a finite-type quasi-coherent module on \(T\), and \(U\subset S\) a quasi-compact open. Suppose \(N|_{T_U}\) is finitely presented and \(U\)-flat. There is a \(U\)-admissible blowup \(b:S'\to S\) for which \(N^{\mathrm{str}}\) is finitely presented on \(T\times_SS'\) and flat over \(S'\).

We first prove this over a Noetherian base. The assertion is étale local on source and base in the precise sense explained after the induction. Take affine neighbourhoods. The integer
\[
 d=\max_{s\in S}\dim\operatorname{Supp}(N_s)
\]
is finite, bounded by the number of generators of an affine finite-type presentation of \(T\). Induct on \(d\), using \(d=-1\) for the zero module. At a point of support fibre dimension \(d\), apply F1. Strict transform commutes with the closed affine pushforward \(i_*\) and finite pushforward \(\pi_*\); finite pushforward detects base flatness. Thus for that local problem replace \(N\) by \(\pi_*G\) on the smooth affine family \(P_0\to S_0\), whose fibres are geometrically integral of dimension \(d\). The identity \(i_*G=N|_{T_0}\) specifies how to return to the original module.

Apply F2. There is now an open on which the transformed module is locally free, surjecting onto the base. Fix a base point \(s\), choose a generic-fibre basis \(\alpha:A^r\to N\) there, and shrink around that generic point until it is an isomorphism. Its open image in the base contains \(s\); shrink the base to that image. On every fibre the isomorphism open is nonempty, hence contains its generic point. F3 at every base prime now shows that \(\alpha\) is pure over the base. Put \(H=\operatorname{coker}\alpha\). Its fibre support misses each generic point of the \(d\)-dimensional integral fibre, so its maximum support dimension is less than \(d\). It is finite; over \(U\) it is flat and finitely presented, by the pure exact sequence and the original flatness. Apply the induction hypothesis to \(H\). A.1 yields on the further blowup
\[
0\to\mathcal O_{P_{S'}}^r\to N^{\mathrm{str}}\to H^{\mathrm{str}}\to0.
\]
Both outside terms are base-flat, so the middle term is base-flat. Over a Noetherian base the source after these blowups is Noetherian locally of finite type; a finite module there is finitely presented. Points with smaller support dimension are handled directly by the same induction. The vanishing locus is handled by zero modules. Finite étale covers and finite affine covers suffice by quasi-compactness, and their centres can be combined as below. This proves the Noetherian case.

Here is the actual étale-centre descent, for schemes and for the algebraic spaces needed in Chow. Let \(W\to B\) be a qc separated étale chart, \(U\subset B\) qc open, and \(J\subset\mathcal O_W\) finite type with \(J|_{W_U}=\mathcal O\). H.1 constructs a finite hull \(W\subset P\to B\) with \(P\to B\) finite and finitely presented. Extend \(J\), glued with the unit ideal on \(P_U\), to a finite-type ideal \(J_2\subset\mathcal O_P\), using G. Let \(D=V(J_2)\subset P\), \(\tau:D\to B\), and
\[
 K=\operatorname{Fitt}_0(\tau_*\mathcal O_D)\subset\mathcal O_B.
\]
The pushforward is finitely presented: on affine charts, a finite finitely presented algebra is finitely presented as a base module (reduce monomials using its finitely many integral equations and relations). Fitting ideals commute with base change and give finite-type ideals. \(K|_U=\mathcal O_U\).

The section \(W\to W\times_BP\) defined by \(W\subset P\) is open and closed: it lies in the open \(W\times_BW\), where it is the diagonal of the separated étale map, and its graph is closed in the finite separated morphism \(W\times_BP\to W\). Therefore
\[
 W\times_BD=V(J)\amalg D_1.
\]
Finite flat base change and the product formula for the zeroth Fitting ideal of a direct sum give
\[
 K\mathcal O_W=J\cdot\operatorname{Fitt}_0((D_1\to W)_*\mathcal O_{D_1})=J J_1.
\]
The base is \(B\), not \(P\), in this fibre product. Blowing up \(K\) consequently dominates the prescribed blowup of \(J\). For finitely many charts, blow up the product of their \(K\). Its pullbacks dominate all local flattenings. Their flat strict transforms stay flat under the resulting further blowups by A. Faithfully flat local descent on the étale source cover makes the global strict transform flat. In the Noetherian case finite presentation follows as above. For the general scheme proof this centre argument may use scheme AG-MO-12 for the finite hull; H supplies the algebraic-space extension without taking it as a prerequisite of scheme Zariski Main.

We now return to arbitrary qcqs \(S\) and finite \(N\); this return also proves finite presentation without appealing to an unproved general theorem that finite base-flat modules are locally finitely presented. The assertion is local on the base and on a finite affine source cover. Make \(S\setminus U\) Cartier and work on an affine chart \(S=\operatorname{Spec}R\), \(U=D(f)\), with \(f\) regular. For \(T=\operatorname{Spec}A\), choose a finitely presented \(A\)-module \(N_0\twoheadrightarrow N\) which is an isomorphism over \(D(f)\). The finite algebra and module presentations, the element \(f\), and the flatness of \((N_0)_f\) descend to a Noetherian model
\[
(R_0,A_0,M_0,f_0),\quad
 A=A_0\otimes_{R_0}R,\quad N_0=M_0\otimes_{R_0}R,
\]
with \((M_0)_{f_0}\) flat over \((R_0)_{f_0}\), by C.1. Apply the Noetherian result over \(R_0\). Multiplying its centre \(I_0\) by \(f_0\) if necessary makes its vanishing set exactly \(V(f_0)\), and the new blowup dominates the old one, so its flat strict transform remains flat. Denote that finitely presented flat transform by \(M_0^{\mathrm{str}}\).

Blow up \(I_0R\subset R\). This **need not be the base change of the model blowup**. Nevertheless its invertible exceptional ideal gives a canonical morphism from this actual blowup to the model blowup, by the universal property; each factor of the product centre is invertible as in A. Pull back \(M_0^{\mathrm{str}}\). It is finitely presented over the pulled-back source algebra and flat over the actual modified base. The pullback of \(N_0\) surjects onto it, and its kernel vanishes after inverting the exceptional chart equation \(a\). The pullback of the flat transform has no \(a\)-torsion, because \(a\) is regular on the actual base. Thus it is exactly the strict transform of \(N_0\): every kernel element is killed by a power of \(a\), and every \(a\)-torsion element maps to zero. The strict transforms of \(N_0\to N\) also agree. Their map is surjective and becomes an isomorphism on \(R'_a=R_a\), a localization of \(R_f\), since the chosen centre is a multiple of \(f\). The source has no \(a\)-torsion, so its kernel is zero.

We have therefore obtained the **actual** strict transform of \(N\), not just a flat comparison object, and it is finitely presented and base-flat. Extend and combine the finitely many local centres using A. Under further blowups this module pulls back unchanged, so both finite presentation and flatness remain true. The étale-source version of the same descent argument covers a quasi-compact \(T\) without a quasi-separatedness assumption on \(T\): take a finite affine open cover and descend the local assertions on their union. This proves F.1 with all the original hypotheses.

#### 5.6.11. Descending flattening to spaces

Let \(b:B'\to B\) be a blowup, with exceptional invertible ideal \(\mathcal L=\mathcal I\mathcal O_{B'}\). For \(\mathcal F\) on \(T\), set \(M=b_T^*\mathcal F\) on \(T\times_BB'\), and define its exceptional-power-torsion submodule by
\[
M[\mathcal L^\infty]=
\bigcup_{n\geq1}\{m:\mathcal L^nm=0\}.
\]
The strict transform is \(M/M[\mathcal L^\infty]\). With a local generator \(a\) of \(\mathcal L\), this is the quotient by the elements killed by some power of \(a\). The definition commutes with flat base change, because flat tensor product commutes with each annihilator kernel and with their filtered union. It also commutes with affine pushforward, by the same module calculation.

Successive strict transforms agree with the strict transform for a composite blowup. On a chart, removing \(a\)-power torsion and then \(c\)-power torsion removes exactly the \((ac)\)-power torsion: if \(c^nm\) is \(a\)-torsion then \(a^kc^nm=0\), and a large power of \(ac\) kills \(m\). Conversely an \((ac)\)-torsion element becomes \(c\)-torsion after removing \(a\)-torsion. Pullback of the first removed submodule is itself \(a\)-torsion, so the same calculation applies after tensoring to the second chart. The exceptional ideal of the composite differs by positive invertible powers, which have the same power-torsion submodule.

If \(\mathcal F\) is flat over \(B\), its pullback has no exceptional-ideal torsion, since multiplication by a regular element of the base is injective on a flat module. Its strict transform is therefore its ordinary pullback and remains flat. For \(\mathcal F=\mathcal O_T\), the Rees charts show that the strict transform is the blowup of \(T\) in the pulled-back centre ideal and is closed in \(T\times_BB'\).

The exact scheme foundation used is:

**F (module flattening by blowup).** Let \(S\) be a quasi-compact, quasi-separated scheme, let \(T\to S\) be quasi-compact and locally of finite presentation, let \(\mathcal F\) be a finite-type quasi-coherent module on \(T\), and let \(V\subset S\) be a quasi-compact open where \(\mathcal F\) is finitely presented and flat over \(V\). There exists a \(V\)-admissible blowup \(S'\to S\) such that the strict transform of \(\mathcal F\) is finitely presented and flat over \(S'\).

For Chow's construction its Noetherian instance suffices. We prove that the space version follows from this instance and the finite hull of H.1.

Let \(B\) be Noetherian, \(T\to B\) quasi-compact locally of finite presentation, and \(\mathcal F\) finite type, flat over \(V\). Choose finitely many affine étale charts of \(T\). Each chart over \(B\) is representable, since an algebraic space has representable diagonal. Flatness and finite presentation descend along this source étale cover. It is therefore enough to flatten the module on each chart and find a single base blowup dominating all their local centre ideals.

Choose an affine étale cover \(W\to B\). Scheme theorem F supplies coherent centre ideals on the finitely many relevant affine scheme charts over \(W\). For a centre \(J\subset\mathcal O_W\), equal to the unit ideal over \(V\), we require a coherent ideal \(I\subset\mathcal O_B\), also the unit ideal on \(V\), such that
\[
I\mathcal O_W=J J'
\]
for another coherent ideal \(J'\). This equality makes the pullback of the \(I\)-blowup dominate the prescribed \(J\)-blowup.

Factor \(W\to B\) as a quasi-compact open \(W\subset P\) followed by a finite morphism \(P\to B\). This is the **representable finite-hull support**: for a quasi-compact separated étale scheme chart over a Noetherian space there is such a finite algebraic-space hull. The general scheme factorization theorem does not by itself establish this space assertion; its full space proof is H.1 above.

Extend \(J\) to a coherent ideal \(J_P\) on \(P\), equal to the unit ideal above \(V\), by the Noetherian open-ideal extension used in the main proof. Put \(D=V(J_P)\), let \(\pi:D\to B\) be finite, and define
\[
I=\operatorname{Fitt}_0(\pi_*\mathcal O_D).
\]
This is a coherent ideal, the unit ideal on \(V\). In \(W\times_BP\), the section defined by \(W\subset P\) is open and closed. It is open because inside the open \(W\times_BW\) it is the étale diagonal, and it is closed because it is the graph into the separated space \(P\to B\). Consequently
\[
W\times_BD=V(J)\amalg D'
\]
for finite \(D'\to W\). Finite pushforward commutes with this base change, and the zeroth Fitting ideal of a direct sum is the product of the zeroth Fitting ideals. Since \(\operatorname{Fitt}_0(\mathcal O_W/J)=J\), the desired equality follows with \(J'=\operatorname{Fitt}_0(\pi'_*\mathcal O_{D'})\). The fibre product is over \(B\), not over \(P\).

Take the product of the finitely many resulting \(I\)'s and blow it up on \(B\). Over each chart it is the blowup of a product with its prescribed \(J\) as a factor. The product-ideal calculation makes the domination a further blowup. Strict transforms compose, and an already flat transform pulls back through that further blowup. Thus all selected charts have flat strict transforms, and étale descent proves flatness on \(T\). The Noetherian transformed source makes its finite module finitely presented.

Finally apply this space module assertion to \(\mathcal O_T\). Over a Noetherian \(B\), a finite-type source is Noetherian and is locally of finite presentation over \(B\). Its transformed structural sheaf is that of its closed strict transform, so the preceding result gives exactly the flattening support used in the reading section.

#### 5.6.12. Dense affine opens

A Noetherian quasi-separated algebraic space \(T\) has a scheme open containing all its generic points. Choose an affine étale surjection \(E\to T\), which is quasi-compact and separated, and put \(R=E\times_TE\). The projections \(s,t:R\to E\) are quasi-finite and separated. Scheme Zariski's Main Theorem makes \(s\) finite on a neighbourhood of each generic point of \(E\): factor it locally into an open in a finite scheme and remove the closed image of the missing part, which avoids those generic points.

Let \(E_0\subset E\) be the largest open over which \(s\) is finite. It is invariant under \(R\). In fact, pulling the source map back along the two endpoint maps gives isomorphic morphisms of schemes, by composition and inversion in the relation. Finiteness descends along an étale target cover, so these two pullbacks have the same finite locus. Thus \(T_0=E_0/R_0\) is an open in \(T\), contains its generic points, and has the finite étale cover \(E_0\to T_0\).

Fix a generic point \(\eta\) of \(T_0\). Its fibre in \(E_0\) consists of finitely many generic points. They have a common affine neighbourhood \(W\). To construct it, remove the other irreducible components near each selected generic point, choose an affine neighbourhood in its now-disjoint component open, and take the finite disjoint union. Remove from \(T_0\) the closed image of \(E_0\setminus W\). Over the resulting neighbourhood \(N\) of \(\eta\), the cover \(E_N\) lies in \(W\).

Choose \(a\in\Gamma(W,\mathcal O_W)\) with \(D(a)\subset E_N\), nonzero at every point of the selected finite fibre. Finite prime avoidance applied to the ideal of \(W\setminus E_N\) gives such an element. On \(E_N\) form
\[
q=\operatorname{Norm}_{t}(s^*a),
\]
the determinant of multiplication by \(s^*a\) on the finite locally free module \(t_*\mathcal O_{R_{E_N}}\). Composing with an arrow identifies the finite fibres of arrows into its two endpoints and preserves their source functions, so the two pullbacks of \(q\) agree. The open \(D(q)\) is invariant and contains the selected fibre. It lies in \(D(a)\), because the identity arrow is one of the factors of the fibre norm; invertibility of the determinant requires \(a\) to be invertible there. Restricted to affine \(D(a)\), \(q\) is a regular function, and its principal open \(D(q)\) is affine.

The restricted relation is finite étale between affine schemes. The finite flat affine-equivalence-relation theorem of Lesson 2, Appendix A, makes \(D(q)/R_{D(q)}\) an affine scheme. It is an open neighbourhood of \(\eta\) in \(T\). The union over the finitely many generic points is a scheme open, since schemes glue on open intersections, and it is dense. This proves the claim.

Now let \(X\to Y\) be separated finite type, with \(Y\) Noetherian. The claim gives a scheme open in \(X\) containing every generic point. Removing the other components near each generic point lets us work with finitely many disjoint irreducible scheme opens; all nilpotents in those opens are retained.

For one such open, let \(\eta\) be its generic point and \(\xi=f(\eta)\). Let \(T\subset Y\) be the reduced closure of \(\xi\), with coherent ideal \(\mathcal I\). Its image in the Artinian ring \(\mathcal O_{X,\eta}\) lies in the maximal ideal and is therefore nilpotent. Thus \(\mathcal I^m\mathcal O_{X,\eta}=0\) for some \(m\). Coherence lets us shrink the open around \(\eta\) until \(\mathcal I^m\mathcal O_X=0\) there. This factors that open through the closed thickening \(Y_T=V(\mathcal I^m)\), including its nilpotent structure.

The irreducible Noetherian space \(Y_T\) has an affine scheme open \(A\) containing its generic point \(\xi\). Choose an affine neighbourhood \(V\) of \(\eta\) in \(f^{-1}(A)\). The finite-type map between the affine schemes \(V,A\) is a closed immersion into \(\mathbf A^n_A\) after choosing finitely many algebra generators. Composing with the open \(\mathbf A^n_A\subset\mathbf A^n_{Y_T}\) and the closed \(\mathbf A^n_{Y_T}\subset\mathbf A^n_Y\) gives an immersion \(V\to\mathbf A^n_Y\).

Do this at each generic point of \(X\). Pad the affine coordinates with zeros to a common length \(n\), and append the standard basis vector \(e_l\in\mathbf A^r_Y\) on the \(l\)-th of the \(r\) disjoint opens. The resulting closed coordinate slices in \(\mathbf A^{n+r}_Y\) are pairwise disjoint: one coordinate takes values \(1\) and \(0\), whose difference is a unit over every base. Hence their disjoint union is an immersion. Distinct integer labels would fail in some residue characteristics. The finite union is the required quasi-compact dense open in \(X\).

#### 5.6.13. Constructing the Chow diagram

**Blowups and a flat comparison.** For a coherent ideal \(\mathcal I\subset\mathcal O_B\), form the Rees algebra \(\bigoplus_{n\geq0}\mathcal I^n\). On an étale scheme chart of \(B\), its relative Proj is the ordinary scheme blowup. Flat base change identifies the Rees algebras on intersections of charts. Their Proj identifications satisfy the cocycle condition, so they glue to an algebraic space \(\operatorname{Bl}_{\mathcal I}B\) over \(B\).

This morphism is proper, as checked after a target étale cover. It is representable by schemes for a more precise reason: for every scheme \(S\to B\), its base change is the scheme
\[
\operatorname{Proj}_S\left(\bigoplus_{n\geq0}
\mathcal I^n\otimes_{\mathcal O_B}\mathcal O_S\right).
\]
This relative Proj exists on \(S\); its canonical identifications with the pulled-back charts descend to the claimed isomorphism. Arbitrary base change need not identify that graded algebra with the Rees algebra of the pulled-back ideal, but it does identify its Proj with the base-changed blowup. Thus representability is proved for every scheme base change, rather than inferred just from an étale cover. The blowup is an isomorphism where \(\mathcal I=\mathcal O_B\). Its pulled-back ideal is invertible. Its local generator is a nonzerodivisor on every nonempty blowup chart, since the chart for \(a\in I\) has ring
\[
A[I/a]\subset A_a,
\]
where multiplication by \(a\) is injective. Thus blowing up an ideal defining \(B\setminus V\) makes \(V\) schematically dense, even when \(B\) is nonreduced. A blowup whose centre misses \(V\) is called \(V\)-admissible.

We shall use a flat comparison which avoids a fibre-dimension reduction. Suppose \(h:T\to B\) is separated, flat and of finite presentation, \(V\subset B\) is a quasi-compact schematically dense open, and \(T\times_BV\to V\) is an isomorphism. Then \(h\) is an open immersion. Indeed, \(T\times_BT\) is flat over \(B\), so its inverse image of \(V\) is schematically dense. On an affine chart \(\operatorname{Spec}A\to B\), cover the pullback of \(V\) by finitely many principal opens \(D(a_i)\). Schematic density gives
\[
0\longrightarrow A\longrightarrow\prod_i A_{a_i}.
\]
Tensoring with a flat \(A\)-algebra preserves injectivity. This proves the assertion on affine charts of the flat source, and hence on the space.

The ideal of the closed diagonal \(\Delta_h:T\to T\times_BT\) vanishes over \(V\). Schematic density makes it zero, so the diagonal is an isomorphism and \(h\) is a monomorphism. A flat morphism of finite presentation with isomorphic diagonal is étale, by the scheme flat, unramified, finite-presentation criterion checked on charts and descended. An étale monomorphism is an open immersion, since on an étale target neighbourhood it is the inclusion of its open image. This proves the comparison.

Suppose now that \(B,T\) are Noetherian, \(h:T\to B\) is separated and finite type, and \(h^{-1}(V)\to V\) is an isomorphism. First blow up the ideal of \(B\setminus V\), so that \(V\) becomes schematically dense. Apply strict-transform flattening to the transformed morphism. The preceding flat comparison shows that its new strict transform is open in the new base. The pullback of \(V\) is still schematically dense after the second blowup: on a blowup chart the previously regular boundary equation remains a nonzerodivisor, since that chart embeds into a localization of the previous base ring. Thus a composition of \(V\)-admissible blowups makes this strict transform an open immersion.

**Putting two modifications in one separated space.** Let \(Y\) be Noetherian. Suppose \(U\) is an open subspace of \(X_1\) and \(X_2\), where \(U,X_1,X_2\) are separated and of finite type over \(Y\). Let
\[
C\subset X_1\times_YX_2
\]
be the schematic closure of the diagonal copy of \(U\). Its projections \(p_i:C\to X_i\) are separated and of finite type. The inverse image \(p_i^{-1}(U)\) is exactly \(U\), including its scheme structure: inside \(U\times_YX_2\), the graph of \(U\to X_2\) is closed because \(X_2\to Y\) is separated, and the schematic closure restricts to that graph. The other projection is treated the same way.

Apply the comparison after blowing up to each \(p_i\). It gives admissible modifications \(X_i^{(i)}\to X_i\) and strict transforms \(C_i\) open in \(X_i^{(i)}\). A.2 expresses the composition as one blowup. If its centre ideal is \(\mathcal I_i\), then \(C_i\) is the blowup of \(C\) in \(p_i^*\mathcal I_i\); this follows on scheme charts from the Rees algebra description, and the identifications descend.

Blow up \(C\) in the product \((p_1^*\mathcal I_1)(p_2^*\mathcal I_2)\), and call the result \(C'\). Blowing up a product factors as blowing up either factor and then the pulled-back other factor. On the product blowup, an equality \(IJ=(a)\) with \(a\) a nonzerodivisor makes \(I,J\) invertible fractional ideals, inverse to \(a^{-1}J,a^{-1}I\). The universal property therefore gives the maps to the successive blowups. Conversely the successive blowups make \(IJ\) invertible, so map to the product blowup. Uniqueness in the universal property makes the composites identities. Thus \(C'\to C_i\) is an admissible blowup.

Extend its coherent centre ideal from \(C_i\subset X_i^{(i)}\) to a coherent ideal on \(X_i^{(i)}\) equal to the unit ideal on \(U\). To do so, glue the ideal with \(\mathcal O_U\) on the open \(C_i\cup U\), and take the kernel of
\[
\mathcal O_{X_i^{(i)}}\longrightarrow
j_*(\mathcal O_{C_i\cup U}/\mathcal J)
\]
for its quasi-compact open immersion \(j\). The pushforward is quasi-coherent, as checked on finite affine covers after an étale chart; its kernel is a quasi-coherent ideal, hence coherent in the Noetherian setting. Blow up this extension. We obtain \(X_i'\to X_i^{(i)}\), with \(C'\) open in \(X_i'\).

The morphism
\[
C'\longrightarrow X_1'\times_YX_2'
\tag{5.8.1}
\]
is an immersion: its first component is open and the remaining component gives a graph into the separated space \(X_2'\to Y\). It is also proper. The map \(C'\to C\) is proper, \(C\to X_1\times_YX_2\) is closed, and \(X_1'\times_YX_2'\to X_1\times_YX_2\) is separated. A map from a proper space over a base to a separated space over that base is proper: factor it as its closed graph followed by the base change of the proper structural map. This makes (5.8.1) a proper immersion and therefore a closed immersion.

Glue \(X_1'\) and \(X_2'\) along the identified open \(C'\), obtaining \(M\). It is finite type over \(Y\), because it is covered by those two finite-type opens. It is separated: on the four opens \(X_i'\times_YX_j'\) of \(M\times_YM\), its diagonal is the diagonal of \(X_i'\) if \(i=j\), and (5.8.1), or its switched version, if \(i\ne j\). Each is closed. Both modified spaces are therefore open in one separated finite-type \(Y\)-space.

For completeness, a composition of coherent blowups on a Noetherian space is one blowup. Let \(b:\operatorname{Bl}_I B\to B\), and let \(J'\) be a coherent ideal on the blowup. For sufficiently large \(d\), the usual scheme Proj generation argument gives a coherent subideal \(J\subset I^d\) with
\[
J\mathcal O_{\operatorname{Bl}_I B}
=I^d\mathcal O_{\operatorname{Bl}_I B}\cdot J'.
\]
One obtains \(J\) by pushing forward the ideal twisted by \(\mathcal O(d)\); relative generation holds for large \(d\) on each of finitely many scheme charts and hence on their common refinement. The construction glues since it is pushforward followed by evaluation. The invertible factor \(I^d\) does not change a blowup. The product-ideal argument thus identifies the composition with \(\operatorname{Bl}_{IJ}B\). If both original centres miss \(U\), \(IJ\) is the unit ideal on \(U\).

**A projective open and the containment argument.** Suppose a quasi-compact open \(U\subset X\) has an immersion into \(\mathbf P^n_Y\), with \(X\to Y\) separated finite type and \(Y\) Noetherian. Let \(Z\) be its schematic closure in \(\mathbf P^n_Y\). Then \(U\) is open and schematically dense in \(Z\), and \(Z\to Y\) is proper and representable by schemes.

If \(U\) is only topologically dense in \(X\), first blow up the ideal of \(X\setminus U\). The modification is proper, is an isomorphism on \(U\), is surjective because its closed image contains the dense \(U\), and makes \(U\) schematically dense by the chart calculation. We now use this modification as the \(X\) side of the common construction. Subsequent admissible blowups preserve schematic density: each chart is a subring of a localization of the previous ring, and its restriction to the dense open is injective. This step retains the nilpotent and embedded-component cases.

The common construction gives \(X'\to X\), \(Z'\to Z\) and open immersions of \(X'\), \(Z'\) into a separated finite-type \(Y\)-space \(M\). The map \(Z'\to Y\) is proper and representable. Since \(M\to Y\) is separated, \(Z'\to M\) is proper; being also open, it is a closed immersion.

Let \(\mathcal K\) be its closed-immersion ideal on \(M\). The restriction \(\mathcal K|_{X'}\) vanishes on \(U\). Schematic density gives an injection
\[
\mathcal O_{X'}\longrightarrow j_*\mathcal O_U,
\]
so \(\mathcal K|_{X'}=0\). Thus \(X'\to M\) factors **scheme-theoretically** through \(Z'\). The factor is an open immersion: it is the base change to \(Z'\) of \(X'\subset M\), whose fibre product is \(X'\) because of the factorization. Taking \(\overline X'=Z'\) gives the desired open compactification. Topological density alone would not justify this containment.

**The Noetherian case.** The dense-open proof above gives a quasi-compact dense open \(U\subset X\) with an immersion into \(\mathbf A^n_Y\), hence into \(\mathbf P^n_Y\). It includes nilpotents and does not assume that \(Y\) is absolutely separated. If \(X\) is empty, take both modifications empty. Otherwise apply the projective-open construction. The map \(X'\to X\) is proper and an isomorphism over \(U\); its closed image contains the dense \(U\), hence is all of \(X\). This proves the Noetherian case, using the strict-transform flattening proved above.

**Recovering finite presentation and the original target.** The approximation and envelope proofs above supply these statements for algebraic spaces:

1. Every quasi-compact, quasi-separated \(Y\) is a limit \(Y=\varprojlim Y_i\) of quasi-separated finite-type algebraic spaces over \(\mathbf Z\), with affine transitions. Finite-presentation spaces and morphisms over \(Y\) descend to a stage, and separatedness descends after increasing that stage.
2. For \(X\to Y\) separated finite type, there is a closed immersion \(X\hookrightarrow X_1\) with \(X_1\to Y\) separated and of finite presentation.

First suppose that \(f\) is of finite presentation. Descend it in (1) to a separated finite-presentation morphism \(f_i:X_i\to Y_i\). The term \(X_i\) is an **algebraic space**, rather than automatically a scheme. The space \(Y_i\) is Noetherian, so the preceding construction gives
\[
X_i\longleftarrow X_i'\hookrightarrow\overline X_i'.
\]
Base change along \(Y\to Y_i\). Properness, surjectivity, open immersion and representability by schemes are preserved by base change; the leftmost term is the original \(X\). This proves the finite-presentation case over the full target \(Y\).

For arbitrary finite-type \(f\), apply this case to the envelope in (2):
\[
X_1\longleftarrow X_1'\hookrightarrow\overline X_1'.
\]
Set \(X'=X\times_{X_1}X_1'\). It is closed in \(X_1'\), and \(X'\to X\) is proper and surjective by base change. Let \(\overline X'\) be its schematic closure in \(\overline X_1'\). It is closed in a proper space representable by schemes over \(Y\), so has both properties.

The intersection \(\overline X'\cap X_1'\) is exactly \(X'\), including its scheme structure: restricting the kernel defining schematic closure to an open commutes with that kernel, and \(X'\) was already closed on this open. Hence \(X'\) is open in \(\overline X'\). This is the required diagram for the original finite-type morphism. It imposes no finite-presentation hypothesis on that morphism. \(\square\)

The construction follows the Stacks project authors, *More on Morphisms of Spaces*, “Chow's lemma,” as read in the [AI Integrated Stacks Project](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/), together with *Limits of Algebraic Spaces*, *Divisors on Algebraic Spaces*, and *More on Flatness*. The [official Stacks project statement](https://stacks.math.columbia.edu/tag/089L) is the corresponding public reference.

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

## Prerequisites and sources

The following are precise scheme prerequisites, rather than additional unproved algebraic-space versions of the assigned results.

- Faithfully flat effective descent of quasi-coherent scheme modules [Stacks, Tag 023T], and the equivalence between Zariski and étale quasi-coherent modules on a scheme [Stacks, Tags 03DX and 03LC]. The lesson proves their extension to an algebraic-space presentation, including the transition-map and inverse-functor verifications.
- The ascending commutative-algebra theorems that smooth algebras over reduced or normal rings remain reduced or normal [Stacks, Tags 033B and 033C]. Normality includes arbitrary normal rings. Their descent and the passage to spaces are proved here.
- The Noetherian scheme finite-type theorem and the dimension formula for a flat local map of Noetherian rings with zero-dimensional fibre [Stacks, Tags 01T6 and 00ON]. These enter the étale-local Noetherian and regular-ring arguments. We also use the usual fibre description and cotangent properties of étale scheme maps.
- Scheme locality of the chart-morphism properties in Section 3.2: the target descent statements [Stacks, Tags 02KX, 02KY, 02L2, 02VL, 02VM and 02VN] and the source locality statements [Stacks, Tags 036K, 036N, 036O, 036U, 036W and 03YV]. Their extension and presentation-independence are proved here.
- Scheme descent of quasi-compactness, immersions and closed immersions [Stacks, Tags 02KQ, 02YM and 02L6]; the finite-type permanence rule [Stacks, Tag 01T8]; and the fact that a locally finite-type scheme morphism with finite fibres is locally quasi-finite.
- Existence of a valuation ring in a prescribed field dominating a local subring [Stacks, Tag 00IA]; the torsion-free flatness theorem for modules over valuation rings [Stacks, Tag 0539]; and faithful flatness of a flat local map [Stacks, Tag 00HR]. The lesson recalls the flatness mechanism but does not reprove the general equational flatness criterion.
- The scheme theorem that a universally closed, separated, locally finite-type morphism with finite fibres is finite [Stacks, Tag 02LS], and that a finite monomorphism is a closed immersion [Stacks, Tag 03BB]. They are applied to scheme base changes of the diagonal.

Theorem 5.8 proves Chow's lemma [Stacks, Tag 089L] at its full qcqs target and separated finite-type scope, relative to the genuinely assigned scheme foundations. It includes the space approximation, finite hull, ideal-completeness, local dévissage, projectivity/purity, Fitting-ideal and strict-transform-flattening arguments in §5.6. The relative prescribed-open approximation construction of AG-MO-03, Theorem 5.2, and the conductor/nonaffine finite-completion foundations of AG-MO-12 remain existing planned prerequisite repairs; neither is claimed written here. The valuative criterion itself, its extended existence and push-down arguments, the point-space construction, and quasi-coherent descent on an algebraic space have been proved in the lesson.

The flattening proofs use the written Artin–Rees and Krull-intersection theorems of *Noetherian and Artinian rings*, Theorems 5.1 and 6.1, prime filtrations in *Associated primes and primary decomposition*, and Lazard's theorem in *Tor and flat modules*, Theorem 6.4. These are named lessons of *Commutative algebra for geometry*. Faithful flatness and the local criterion are supplied by *Faithful flatness and the local criterion for flatness*; normalization and dimension by *Krull dimension and Noether normalization* and *Dimension theory of Noetherian local rings*; the normal one-dimensional local-ring criterion by *Discrete valuation rings, normal rings and Serre’s criterion*, Theorem 1.2; and Noetherian completion by *Completion*. The actual infinite projectivity, purity and Mittag–Leffler arguments needed here are supplied in §5.6.6. Generic freeness and the flat locus have their scheme homes in AG-FSE-01/02; standard étale, smooth-local and elementary finite-part statements are AG-FSE-04/05/07. The additional connected-fibre construction is proved here. Scheme blowups are AG-MO-16; arbitrary-base composition and the space extensions are proved above. These exact contracts do not certify closure of every transitive prerequisite.

The Chow construction and its local support follow the Stacks Project authors, as read in the AI Integrated Stacks Project at revision `565b10e987aba5969b21145a0833f42d69f96790`, especially *More on Morphisms of Spaces*, *Limits of Algebraic Spaces*, *More on Flatness*, *Groupoids* and the scheme and space divisor chapters. This treatment is independently expressed eligible AI writing under CC0. The source documents retain their GFDL terms and human attribution. The writing AI checked its constructions, reduction-return maps and edits.

## References

- **[Stacks]** The Stacks project, *Properties of Algebraic Spaces*, *Morphisms of Algebraic Spaces*, *Decent Algebraic Spaces*, and *More on Morphisms of Spaces*, especially Tags 03BT, 03EB, 03G5, 03M3, 03I8, 03ID, 03ZL, 0CKZ, 0ARH, 0A40 and 089L. The corresponding chapters are available in [AI Integrated Stacks Project](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/), an edition containing AI-proposed corrections and additions which have not been reviewed by the Stacks project's maintainers. The [official Stacks project](https://stacks.math.columbia.edu/) retains its own publication and tags.
