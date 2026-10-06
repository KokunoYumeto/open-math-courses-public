# Fundamental groups of proper schemes and the homotopy exact sequence

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI, GPT-6.1 Sol (OpenAI). Public domain (CC0).*

Finite étale covers ignore nilpotent structure and purely inseparable identifications. Properness gives a second rigidity: a cover of a special fibre over a henselian local base extends uniquely, and extending an algebraically closed ground field adds no covers of a proper scheme. We import finite-cover invariance under thickenings, prove its extension to universal homeomorphisms and the properness statements at their full stated generality, then use the finite étale part of Stein factorization to prove the homotopy exact sequence.

Connected schemes and connected fibres are nonempty throughout. Fibre functors, continuous group maps and their conjugacy conventions are those of *The étale fundamental group*. The sequence for a proper family will be exact in the middle and surjective on the right; it will not assert injectivity of its left arrow.

## 1. Topological invariance

A **thickening** is a closed immersion \(i:Z\hookrightarrow X\) inducing a homeomorphism on underlying spaces. On affines its defining ideal is contained in the nilradical. It need not have a globally bounded nilpotence exponent.

We import finite étale invariance, including finiteness of every lift and all morphisms, from [*Infinitesimal lifting and invariance under thickenings*, Theorem 6.2](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-FSE/infinitesimal-lifting-and-invariance-under-thickenings.html#6-keeping-the-lift-finite). Its proof applies to every thickening defined by a nil ideal, without a uniform nilpotence bound. We record the equivalence and derive its fundamental-group consequence here.

**Proposition 1.1.** Restriction gives
\[
\operatorname{F\acute Et}(X)\simeq\operatorname{F\acute Et}(Z).
\tag{1.1}
\]
In particular \(\pi_1(X_{\mathrm{red}})\to\pi_1(X)\) is an isomorphism whenever \(X\) is connected. [Stacks, Tag 0BQB](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-lemma-thickening)

*Proof of the fundamental-group consequence.* The categorical equivalence (1.1) is the exact prerequisite import just cited. The geometric fibres are unchanged by a thickening. Their canonical identification makes an equivalence of these categories identify their automorphism groups as topological groups, by *Galois categories*, Theorem 4.1. The reduction immersion is a thickening even in the non-Noetherian case, which gives the final assertion. \(\square\)

A **universal homeomorphism** is a morphism that becomes a homeomorphism after every base change. Equivalently it is integral, surjective and universally injective [Stacks, Tag 04DF](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-universal-homeomorphism). Universal injectivity is also called being radicial; it includes purely inseparable extensions of residue fields.

**Theorem 1.2.** For every universal homeomorphism \(f:X\to S\), base change gives an equivalence
\[
\operatorname{F\acute Et}(S)\simeq\operatorname{F\acute Et}(X).
\tag{1.2}
\]
For connected schemes it induces an isomorphism of fundamental groups. No finite-type, separation or quasi-compactness hypothesis on \(S\) is imposed. [Stacks, Tag 0BQN](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-proposition-universal-homeomorphism)

*Proof.* Because \(f\) is integral, it is separated. Its diagonal
\(\Delta:X\to X\times_SX\) is a closed immersion, and universal injectivity makes it surjective [Stacks, Tag 01S4](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-universally-injective). It is a thickening. The analogous diagonal \(X\to X\times_SX\times_SX\) is a thickening too.

Let \(U\to X\) be finite étale. Its two pullbacks to \(X\times_SX\) restrict along \(\Delta\) to the same object \(U\). Proposition 1.1 therefore gives a unique isomorphism between these pullbacks whose restriction is the identity. On the triple product its two compositions and its third pullback agree on the triple diagonal. Full faithfulness in Proposition 1.1 makes them equal everywhere. Thus this isomorphism is a descent datum.

Effective integral descent in [*Descending properties of schemes and morphisms*](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-DFG/AG-DFG-03.html), Theorem 6.4, applies to the integral surjection \(X\to S\). The object \(U\to X\) is quasi-compact and separated étale, so the datum gives a quasi-compact separated étale \(V\to S\), with \(U\simeq X\times_SV\). We check finiteness rather than presume that arbitrary integral descent preserves it.

The composite \(U\to S\) is integral, as a composite of the finite map \(U\to X\) and integral \(X\to S\). The map \(U\to V\) is the base change of \(X\to S\), so is integral and universally surjective. For any \(T\to S\) and closed subset \(C\subset V_T\), its inverse image in \(U_T\) is closed, and its image in \(T\) is closed because \(U_T\to T\) is integral. Surjectivity makes this image exactly the image of \(C\). Hence \(V\to S\) is universally closed. Since it is quasi-compact, separated and étale, it is proper quasi-finite, and therefore finite. This proves essential surjectivity.

For full faithfulness take a map between two pulled-back covers over \(X\). On the double product its two compatibility expressions agree on the diagonal. Proposition 1.1 makes them agree on the whole product. Integral full faithfulness from the same descent lesson gives a unique map over \(S\). Finally the homeomorphism preserves connectedness, and a geometric fibre identifies the fibre functors in (1.2). Their automorphism groups therefore agree topologically. \(\square\)

For example, if \(k'/k\) is any algebraic purely inseparable extension, then \(X_{k'}\to X\) is a universal homeomorphism. Integrality comes from the scalar extension, and each geometric fibre has a single underlying point with purely inseparable residue extension; these properties persist after base change. Thus (1.2) proves purely inseparable invariance, including infinite extensions. The direct perfection proof in the preceding lesson is a special case.

**Proposition 1.3.** Suppose \(f:X\to S\) is a morphism inducing an equivalence of finite étale categories. It preserves connectedness. If both schemes are quasi-compact and quasi-separated, it also gives a homeomorphism \(\pi_0(X)\to\pi_0(S)\) of their spaces of connected components. [Stacks, Tag 0BQA](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-lemma-what-equivalence-gives)

*Proof.* Open-and-closed subsets are precisely the finite étale subobjects of the terminal object. An equivalence carries the terminal object and its subobjects bijectively. Hence inverse image is an isomorphism of the Boolean algebras of open-and-closed subsets, proving the connectedness assertion.

For the assertion about components, use the standard spectral-space facts: a quasi-compact quasi-separated scheme is spectral, its components are intersections of their open-and-closed neighbourhoods, and its component space with the quotient topology is compact Hausdorff and totally disconnected [Stacks, Tags [094L](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/properties.html#properties-lemma-quasi-compact-quasi-separated-spectral), [005F](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/topology.html#topology-lemma-connected-component-intersection), [0900](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/topology.html#topology-lemma-pi0-profinite)]. Every ultrafilter of open-and-closed subsets is realized by a point: its members are closed and have the finite-intersection property, so quasi-compactness makes their intersection nonempty. The intersection is one component, by the stated intersection description. Thus the Boolean-algebra isomorphism identifies the component sets. The map is continuous for their quotient topologies, and is a bijection between compact Hausdorff spaces. It is a homeomorphism. \(\square\)

The argument about subobjects uses their preservation as categorical subobjects, not a presumption that \(f\) is surjective.

## 2. Covers over a complete local base

Let \((A,\mathfrak m)\) be a complete Noetherian local ring, and let \(X\) be proper over \(A\). Set
\[
X_n=X\times_A\operatorname{Spec}(A/\mathfrak m^{n+1}),
\qquad n\ge0.
\]

We use Grothendieck's existence theorem from the formal-cohomology prerequisite in its coherent form: completion is an equivalence from coherent modules on a proper \(A\)-scheme to compatible systems of coherent modules on the \(X_n\) [Stacks, Tag 088E](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/coherent.html#coherent-theorem-grothendieck-existence). This includes full faithfulness for maps. Completion commutes with tensor products of coherent modules. We will algebraize finite algebra structures with this theorem, rather than assert that a formal étale cover is automatically an algebraic one.

A useful properness observation is that every nonempty closed subset of a proper \(A\)-scheme meets its closed fibre. Its image in \(\operatorname{Spec}A\) is nonempty and closed, so contains the closed point. In particular an open subset containing the entire closed fibre contains the entire scheme if its complement is closed.

**Theorem 2.1 (complete case).** Restriction gives an equivalence
\[
\operatorname{F\acute Et}(X)\simeq
\operatorname{F\acute Et}(X_0).
\tag{2.1}
\]
It identifies connected components, and for connected \(X\) identifies its fundamental group with that of \(X_0\). [Stacks, Tag 0A48, complete case](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-lemma-finite-etale-on-proper-over-henselian)

*Proof: essential surjectivity.* Start with \(Y_0\to X_0\) finite étale. Proposition 1.1 lifts it successively to finite étale \(Y_n\to X_n\). Choose the transition identifications lifting the given ones. Full faithfulness makes their further compatibilities unique. Let
\[
\mathcal B_n=(Y_n\to X_n)_*\mathcal O_{Y_n}.
\]
These are compatible coherent finite locally free algebras. Existence gives a coherent module \(\mathcal B\) restricting to each \(\mathcal B_n\). Full faithfulness algebraizes the compatible multiplication and unit maps. Associativity, commutativity and the unit identities hold because their two sides have equal completions and completion is faithful. Thus \(\mathcal B\) is a coherent algebra, and \(Y=\underline{\operatorname{Spec}}_X\mathcal B\) is finite over \(X\), with all the required restrictions.

We verify that \(\mathcal B\) is locally free. At \(x\in X_0\), write \(R=\mathcal O_{X,x}\), \(J=\mathfrak mR\), and \(M=\mathcal B_x\). The ring \(R\) is Noetherian local. Each \(M/J^{n+1}M\) is free of the same finite rank \(r\) over \(R/J^{n+1}\). Lift a basis modulo \(J\) to \(r\) elements of \(M\). Nakayama makes \(R^r\to M\) surjective, and modulo each \(J^{n+1}\) the lifted basis is again a basis by Nakayama. Its kernel is therefore contained in
\(\bigcap_n J^{n+1}R^r=0\), by Noetherian Krull intersection [Stacks, Tag 00IQ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-intersection-powers-ideal-module). So \(M\) is free. The local-freeness locus of a coherent module on the Noetherian scheme \(X\) is open. Its closed complement misses \(X_0\), so is empty by properness. This proves local freeness everywhere.

The finite algebra's module of relative differentials is coherent. Its restriction to \(X_0\) vanishes, because \(Y_0\to X_0\) is étale. Nakayama makes it vanish at points of the closed fibre; its closed support then misses that fibre and is empty by the same properness observation, applied to \(Y\). Hence \(Y\to X\) is finite locally free and unramified, therefore finite étale by the finite étale algebra criterion from the [étale-morphism prerequisite](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-FSE/etale-morphisms-and-their-local-structure.html#1-a-definition-and-its-geometric-tests). This proves essential surjectivity.

*Proof: full faithfulness by graphs.* Let \(U,V\) be finite étale over \(X\), and let \(\alpha_0:U_0\to V_0\) be an \(X_0\)-map. Its graph is an open-and-closed immersion
\[
U_0\longrightarrow U_0\times_{X_0}V_0,
\]
since both covers are étale and separated. The scheme \(P=U\times_XV\) is proper over \(A\). Essential surjectivity just proved, now applied to \(P\), lifts the graph to a finite étale \(W\to P\). The projection \(W\to U\) is finite étale: it is a map between finite étale \(X\)-schemes, as proved in the preceding lesson. Its restriction over \(U_0\) is an isomorphism.

The locus on \(U\) where its locally free degree differs from one is open and closed, and misses \(U_0\). It is closed and proper over \(A\), so empty. A finite locally free algebra of rank one is its base algebra, by the unit and Nakayama argument in the preceding lesson. Thus \(W\to U\) is an isomorphism. Composing its inverse with \(W\to V\) gives a lift of \(\alpha_0\).

For uniqueness, the equalizer of two \(X\)-maps \(U\to V\) is open and closed in \(U\), by the finite étale diagonal. If they agree on \(U_0\), the complementary closed subset misses \(U_0\). Properness makes it empty. Thus the lift is unique, proving full faithfulness.

The component assertion follows from Proposition 1.3, since proper schemes over Noetherian affine bases are quasi-compact and quasi-separated. For connected \(X\), the equivalence and the geometric fibre at a point of \(X_0\) give the topological group isomorphism. \(\square\)

The two uses of properness are substantive: they let the coherent existence theorem apply and ensure that bad loci cannot escape the closed fibre.

### 2.2. The precisely stated henselian inputs

A henselian pair \((A,I)\) has \(I\) in the Jacobson radical and has the coprime monic factorization-lifting property. A henselian local ring is the case \(I=\mathfrak m\). We use these three results as named inputs, allowed by the course programme:

- For a henselian pair, finite étale \(A\)-algebras and finite étale \(A/I\)-algebras form equivalent categories [Stacks, Tag 09ZS](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-lemma-gabber).
- For any henselian local ring \(A\) and any proper \(X/A\), restriction to the closed fibre is an equivalence of finite étale categories [Stacks, Tag 0A48](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-lemma-finite-etale-on-proper-over-henselian).
- For any henselian pair \((A,I)\) and any proper \(X/A\), restriction to \(X\times_A\operatorname{Spec}(A/I)\) is such an equivalence [Stacks, Tag 0GS2](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-lemma-finite-etale-on-proper-over-henselian-pair).

No Noetherian or completeness assumption is imposed in these statements. Theorem 2.1 proves the complete Noetherian local case directly. Passing from that case to general henselian bases requires algebraization and approximation; it is not justified merely by completing the ring.

One consequence used below is that every open-and-closed decomposition of the special fibre of a proper scheme over a henselian local ring lifts uniquely to an open-and-closed decomposition of the whole scheme. This follows from the subobject argument of Proposition 1.3, which did not require quasi-compactness for its Boolean-algebra assertion.

## 3. Algebraically closed extensions and properness

**Theorem 3.1.** If \(k'/k\) is an extension of algebraically closed fields and \(X\) is proper over \(k\), then base change gives
\[
\operatorname{F\acute Et}(X)\simeq
\operatorname{F\acute Et}(X_{k'}).
\tag{3.1}
\]
For connected \(X\) the induced fundamental-group map is an isomorphism. [Stacks, Tag 0A49](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-lemma-finite-etale-invariant-over-proper)

*Proof.* Write \(k'\) as the filtered union of its finitely generated \(k\)-subalgebras \(R\). These are domains. A finite étale \(Y'\to X_{k'}\) descends to a finite étale \(Y_R\to X_R\) for some such \(R\), by finite-presentation approximation from the preceding lesson, including eventual finiteness and étaleness. The nonzero finite-type algebra \(R\) has a \(k\)-valued closed point \(t\), by the Nullstellensatz. Set \(Y=(Y_R)_t\), a finite étale cover of \(X\).

Let \(B=R_{\mathfrak m_t}^h\), the henselization of the local ring at \(t\). Both \((Y_R)_B\) and \(Y_B\) restrict to \(Y\) over the closed fibre \(X\). The henselian proper input in Section 2.2 gives an isomorphism
\[
(Y_R)_B\simeq Y_B
\quad\text{over }X_B.
\tag{3.2}
\]

We explain why there is a ring map \(B\to k'\) extending \(R\subset k'\), rather than regard the chosen closed point as an embedding into the generic field. Localizing \(R\) first gives an embedding of \(R_{\mathfrak m_t}\) into its fraction field \(F=\operatorname{Frac}R\subset k'\). Henselization is faithfully flat and is a filtered colimit of étale neighbourhood algebras. Its generic fibre \(B\otimes_R F\) is nonzero; choose a prime of it. The residue field at that prime is algebraic separable over \(F\): the neighbourhood algebras become finite étale algebras over \(F\), and their residue fields at the compatible primes are finite separable extensions. Since \(k'\) is algebraically closed, this residue field embeds into \(k'\) extending the given \(F\)-embedding. The composite
\(B\to B\otimes_RF\to\kappa(\mathfrak p)\to k'\)
is the desired map. Pulling (3.2) back along it identifies \(Y'\) with \(Y_{k'}\). This proves essential surjectivity.

For fullness let \(U,V\) be finite étale over \(X\) and let
\(\alpha':U_{k'}\to V_{k'}\) be an \(X_{k'}\)-map. Approximation descends it to a map between \(U_R,V_R\) for some \(R\). Choose \(t,B\) as above. Its fibre \(\alpha_t:U\to V\) is an \(X\)-map. Full faithfulness of the henselian proper equivalence makes the descended map over \(B\) equal to the base change of \(\alpha_t\), because these two maps have the same closed fibre. A map \(B\to k'\) then proves \(\alpha'=(\alpha_t)_{k'}\). For faithfulness, equality after a faithfully flat field extension detects equality of morphisms, by *Faithfully flat descent*. Thus (3.1) is an equivalence with all maps.

Connectedness is preserved here; alternatively it follows from the standard geometric connectedness criterion over a separably closed field [Stacks, Tag 0363](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/varieties.html#varieties-lemma-separably-closed-field-connected-components). The canonical geometric-fibre identification and (3.1) now identify the fundamental groups. \(\square\)

There is a useful distinction. For a connected scheme over an algebraically closed field, a field extension preserves connectedness of every connected finite étale cover, by the same geometric connectedness criterion. The surjectivity criterion in *Galois categories* therefore makes the base-change functor fully faithful. Properness in Theorem 3.1 supplies essential surjectivity. The next example shows exactly how new objects can appear without it.

## 4. New covers of the affine line in characteristic \(p\)

Let \(k\subsetneq k'\) be algebraically closed fields of characteristic \(p>0\), and choose \(a\in k'\setminus k\). Consider
\[
W_a=\operatorname{Spec}
 k'[x,y]/(y^p-y-a x)\longrightarrow\mathbf A^1_{k'}.
\tag{4.1}
\]
It is finite étale of degree \(p\), and is connected: eliminating \(x\), since \(a\ne0\), identifies its source with \(\operatorname{Spec}k'[y]\). Translations by \(\mathbf F_p\) make it a Galois cover.

**Proposition 4.1.** The underlying cover \(W_a\) is not isomorphic to the base change of any finite étale cover of \(\mathbf A^1_k\). Thus the functor in (3.1) can fail to be essentially surjective without properness. [Stacks, Tag 0A47, for the Artin–Schreier cohomology calculation](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale-cohomology.html#etale-cohomology-remark-invariance)

We prove the assertion about underlying covers, including why forgetting the chosen translations cannot make descent possible.

First, every \(\mathbf Z/p\mathbf Z\)-torsor over \(\operatorname{Spec}R\), with \(R=k[x]\), has an equation
\[
z^p-z=h(x),\qquad h\in k[x].
\tag{4.2}
\]
Here is an algebraic proof. Let its finite étale algebra be \(B\), and let \(\sigma\) be the generator acting on \(B\). The trace \(B\to R\) is surjective: on an étale covering splitting the torsor it is the sum map \(R^p\to R\), which is surjective, and faithful flatness detects surjectivity. Choose \(b\in B\) with trace one, and put
\[
z=-\sum_{i=0}^{p-1}i\,\sigma^i(b).
\tag{4.3}
\]
Reindexing the sum gives \(\sigma(z)-z=1\). Hence \(z^p-z\) is invariant and belongs to \(R\). The invariants are \(R\) by faithfully flat affine descent: the torsor relation identifies its double fibre product with the disjoint union indexed by the group. On a geometric fibre, the \(p\) values of \(z\) differ by all elements of \(\mathbf F_p\). The algebra map from the rank-\(p\) finite locally free algebra in (4.2) to \(B\) is therefore an isomorphism on every geometric fibre. Locally a map between free modules of the same rank with invertible determinant on residue fibres is an isomorphism. This proves (4.2), with its translation action.

Two equations of the form (4.2), with their specified translation actions, define isomorphic torsors precisely when their right sides differ by \(v^p-v\) for some \(v\in k[x]\). Indeed an equivariant isomorphism makes the two coordinates differ by an invariant element \(v\), and substitution gives that condition; a coordinate translation supplies its converse.

Every polynomial has, modulo these differences, a unique representative of the form
\[
\sum_{n\ge1,\ p\nmid n}\lambda_n x^n.
\tag{4.4}
\]
To see existence, remove the constant using surjectivity of \(c\mapsto c^p-c\) on algebraically closed \(k\). A term \(d x^{pm}\) can be replaced by \(d^{1/p}x^m\), subtracting
\((d^{1/p}x^m)^p-d^{1/p}x^m\). Repeating lowers the relevant exponents and terminates. All coefficients stay in \(k\). For uniqueness, a nonconstant difference \(v^p-v\) has highest exponent \(p\deg v\), divisible by \(p\), whereas a nonzero polynomial of the form (4.4) does not. A constant difference cannot change (4.4).

Now suppose \(W_a\simeq V_{k'}\) for a cover \(V\) over \(\mathbf A^1_k\). The cover \(V\) is connected of degree \(p\). Base change on finite étale categories is fully faithful here, by the observation at the end of Section 3: every connected finite étale \(k\)-cover remains connected over \(k'\) [Stacks, Tag 0363](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/varieties.html#varieties-lemma-separably-closed-field-connected-components), so the Galois-category surjectivity criterion applies. Thus every deck transformation of \(W_a\) descends to a deck transformation of \(V\), once the proposed isomorphism is chosen.

There are exactly \(p\) deck transformations of \(W_a\). The \(p\) translations already exist, and connected-object one-point uniqueness bounds their number by the fibre degree \(p\). In particular the chosen generator \(y\mapsto y+1\) descends to a generator on \(V\). Its action on each geometric fibre is free by the same one-point uniqueness and hence transitive, so \(V\) is a \(\mathbf Z/p\mathbf Z\)-torsor for this descended action. Apply (4.2): it has an equation with \(h\in k[x]\). The proposed isomorphism, with this choice of descended generator, is equivariant. Thus over \(k'\) we would have
\[
a x-h=v^p-v,\qquad v\in k'[x].
\tag{4.5}
\]
Reduce \(h\) using (4.4) over \(k\). Its reduced coefficients lie in \(k\), and the same reduction remains valid over \(k'\). The reduced representative of \(a x\) is \(a x\). Uniqueness of (4.4) over \(k'\) forces the coefficient of \(x\) in the reduced \(h\) to be \(a\), contradicting \(a\notin k\). This proves Proposition 4.1.

The source's Artin–Schreier sequence computes the same phenomenon as
\(H^1_{\mathrm{\acute et}}(\mathbf A^1_k,\mathbf Z/p\mathbf Z)\);
the trace construction above supplies the torsor equations directly. There is no conflict with purely inseparable invariance: these algebraically closed field extensions add new transcendental coefficients.

## 5. The finite étale part of Stein factorization

For a proper \(f:X\to S\), the candidate Stein space is
\[
S'=\underline{\operatorname{Spec}}_S(f_*\mathcal O_X),
\tag{5.1}
\]
with its evaluation map \(X\to S'\). Under the hypotheses below, we prove directly that this algebra is finite étale and that the evaluation map has geometrically connected fibres.

We need one precise cohomology input. If \(f\) is proper, flat and of finite presentation, then
\[
E=Rf_*\mathcal O_X
\]
is perfect and its formation commutes with arbitrary base change [Stacks, Tag 0B91](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/perfect.html#perfect-lemma-flat-proper-perfect-direct-image-general). Locally a perfect complex is represented by a bounded complex of finite projective modules. In particular flat base change computes \(H^0\) by tensoring, and at any residue field its degree-zero cohomology is the global functions of the fibre. This is a cohomology-and-base-change prerequisite, not the Stein conclusion we are about to prove.

We will also use the elementary description of global functions on a proper geometrically reduced scheme \(Z\) over a field \(F\):
\[
H^0(Z,\mathcal O_Z)
\text{ is a finite product of finite separable extensions of }F.
\tag{5.2}
\]
For completeness, coherent proper finiteness makes this algebra finite-dimensional [Stacks, Tag 02O6](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/coherent.html#coherent-lemma-proper-over-affine-cohomology-finite). Reducedness makes it a reduced Artinian algebra, hence a product of fields. Flat base change for global functions, proved in [*Descending properties of schemes and morphisms*](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-DFG/AG-DFG-03.html), makes its tensor product with an algebraic closure reduced when \(Z\) is geometrically reduced. A finite field extension with that property is separable. Idempotents correspond exactly to open-and-closed decompositions of \(Z\), so the field factors correspond to its connected components. Over a separably closed field, (5.2) is a product of copies of that field. In particular a geometrically connected geometrically reduced proper scheme has only its ground field as global functions [Stacks, Tag 0BUG](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/varieties.html#varieties-lemma-proper-geometrically-reduced-global-sections).

### 5.1. A finite-complex calculation

Let \(R\) be local with residue field \(F\), and let \(C^\bullet\) be a bounded finite-free complex with no negative-degree cohomology after tensoring with \(F\). Cancelling split contractible summands in its negative degrees gives a representative starting in degree zero. Here is why: in the lowest negative degree the differential is injective modulo the maximal ideal. Some full-rank minor is a unit, so that differential is a split inclusion. Cancel its source and image, and repeat in the next negative degree.

Suppose also that
\[
H^0(C^\bullet)\longrightarrow H^0(C^\bullet\otimes_R F)
\tag{5.3}
\]
is surjective, and let the dimension of the latter be \(r\). Choose actual cycles \(c_1,\ldots,c_r\) lifting a basis. Their reductions are independent in \(C^0\otimes F\), so they extend to a basis of \(C^0\). Write \(C^0=R^r\oplus Q\), with the first summand spanned by these cycles. The differential is zero on \(R^r\), and is injective on \(Q\) modulo the maximal ideal: the entire kernel modulo that ideal is spanned by the \(c_i\). A unit minor again makes \(Q\to C^1\) a split inclusion. Its image has zero further differential. Cancelling this contractible pair leaves
\[
C^\bullet\simeq R^r[0]\oplus P^\bullet,
\qquad P^\bullet \text{ finite free and starting in degree }1.
\tag{5.4}
\]
Thus \(H^0(C^\bullet)=R^r\), and its formation commutes with every base change. At a stalk of a scheme these finitely many cycles, bases and unit minors spread to an open neighbourhood, so the same conclusions hold locally there. This proves the degree-zero case of the splitting calculation [Stacks, Tag 0A1U](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-algebra.html#more-algebra-lemma-better-cut-complex-in-two), including the algebra needed below.

### 5.2. Lifting the fibre basis and proving finiteness

**Theorem 5.1.** Let \(f:X\to S\) be proper, flat and of finite presentation, with geometrically reduced fibres. Then \(f_*\mathcal O_X\) is a finite locally free algebra, commutes with arbitrary base change, and is finite étale. Consequently (5.1) gives a factorization
\[
X\xrightarrow{q}S'\xrightarrow{h}S
\tag{5.5}
\]
with \(h\) finite étale and \(q\) proper with geometrically connected fibres. [Stacks, Tag 0BUN](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-lemma-stein-factorization-etale)

*Proof.* Work at \(s\in S\), with \(R=\mathcal O_{S,s}\) and \(F=\kappa(s)\). Choose a strictly henselian local extension \(R^{sh}\), with separable-closure residue field \(F^s\). Its faithful flatness is part of the [henselization prerequisite](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-FSE/etale-neighbourhoods-henselization-and-quasi-finite-morphisms.html#3-the-two-colimits-of-local-choices). By (5.2), the global functions of the proper geometrically reduced fibre over \(F^s\) are \((F^s)^r\) for some \(r\ge0\).

Each coordinate idempotent in this algebra specifies an open-and-closed component of that fibre. The proper henselian equivalence from Section 2.2 lifts the decomposition to \(X_{R^{sh}}\). Its characteristic functions are global idempotents lifting those coordinate idempotents. Multiplying them by lifts of elements of \(F^s\) in \(R^{sh}\) shows that
\[
H^0(X_{R^{sh}},\mathcal O)\longrightarrow
H^0(X_{F^s},\mathcal O)
\]
is surjective. Flat base change identifies the left side with
\(H^0(X_R,\mathcal O)\otimes_RR^{sh}\), and identifies the target with
\(H^0(X_F,\mathcal O)\otimes_FF^s\).
Faithful flatness of the field extension \(F^s/F\) therefore makes
\[
H^0(X_R,\mathcal O)\longrightarrow H^0(X_F,\mathcal O)
\tag{5.6}
\]
surjective.

Apply the perfect-complex input to \(E\) at \(s\). Its residue-field complex computes coherent cohomology of the fibre, so has no negative-degree cohomology. The preceding calculation removes negative terms. Surjectivity (5.6) is exactly (5.3), so (5.4) proves that \(H^0(E)\) is locally free of finite rank near \(s\), and that its formation commutes with arbitrary base change there. This argument works at every \(s\), including the case of an empty fibre, where \(r=0\). It proves the asserted finiteness, local freeness and base-change statement on all of \(S\).

By (5.2) every residue-field algebra is finite étale. A finite locally free algebra is of finite presentation; its module of relative differentials is finitely generated. Tensoring that module with each residue field gives zero, so Nakayama at every point of its spectrum makes the module zero. The finite flat unramified criterion makes the algebra finite étale. This proves the assertion about \(h\).

The evaluation map \(q\) exists by the relative-spectrum adjunction. It is proper: its graph in \(X\times_SS'\) is closed because \(S'\to S\) is separated, and projection from that product to \(S'\) is a base change of the proper map \(f\). For a geometric point \(\bar s=\operatorname{Spec}\Omega\to S\), base change gives
\[
S'_{\bar s}=\operatorname{Spec}H^0(X_{\bar s},\mathcal O)
=\operatorname{Spec}\Omega^r.
\]
The primitive idempotents on the right select exactly the connected components of the reduced proper scheme \(X_{\bar s}\). The fibre of \(q\) at one of these points is that component. It is nonempty and connected; after an algebraically closed extension it remains connected by [Stacks, Tag 0363](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/varieties.html#varieties-lemma-separably-closed-field-connected-components). Thus the fibres of \(q\) are geometrically connected. This proves (5.5). \(\square\)

If the geometric fibres of \(f\) are also connected, the algebra has rank one at every point. Its unit is an isomorphism, as for finite rank-one algebras in the preceding lesson. Therefore
\[
f_*\mathcal O_X=\mathcal O_S,
\tag{5.7}
\]
and this remains true after every base change. The evaluation factorization is then \(X\to S\to S\).

For any finite étale \(Y\to X\), the composite \(Y\to S\) still satisfies the hypotheses of Theorem 5.1: flatness and finite presentation compose, properness composes, and a finite étale cover of a geometrically reduced fibre is geometrically reduced. Its Stein space
\[
T_Y=\underline{\operatorname{Spec}}_S((Y\to S)_*\mathcal O_Y)
\tag{5.8}
\]
is consequently finite étale over \(S\). Its geometric fibre is the finite set of connected components of \(Y_{\bar s}\). These are precisely the components needed in the homotopy argument.

## 6. The homotopy exact sequence

**Theorem 6.1.** Let \(f:X\to S\) be proper, flat and of finite presentation, with geometrically connected and geometrically reduced fibres. Suppose \(S\) is connected. For a geometric point \(\bar s\) of \(S\) and a geometric point \(\bar x\) of \(X_{\bar s}\), there is an exact sequence
\[
\pi_1(X_{\bar s},\bar x)\xrightarrow{b}
\pi_1(X,\bar x)\xrightarrow{a}
\pi_1(S,\bar s)\longrightarrow1.
\tag{6.1}
\]
Exactness means \(\operatorname{im}b=\ker a\) and that \(a\) is surjective. [Stacks, Tag 0C0J](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-proposition-first-homotopy-sequence)

*Proof.* First \(X\) is connected. More generally a proper surjection with nonempty connected fibres over a connected base has connected source. If its source decomposed into two open-and-closed pieces, their images would be closed by properness. A connected fibre could meet only one piece, so these images would give a disjoint closed partition of the base. Connectedness makes one piece empty. The same argument after base change shows that \(X_U=U\times_SX\) is connected for every connected finite étale \(U\to S\).

The exact functors underlying the two group arrows are
\[
\operatorname{F\acute Et}(S)\xrightarrow{f^*}
\operatorname{F\acute Et}(X)\xrightarrow{i^*}
\operatorname{F\acute Et}(X_{\bar s}).
\tag{6.2}
\]
We verify all categorical tests from *Galois categories*, Section 4.

**Surjectivity on the right and full faithfulness.** The preceding connectedness argument shows that \(f^*\) preserves connected objects, so \(a\) is surjective. There is also a useful explicit proof of full faithfulness. For finite étale \(Y\to X\), let \(T_Y\) be (5.8). For finite étale \(U\to S\), relative-spectrum adjunction gives
\[
\operatorname{Hom}_X(Y,U\times_SX)
=\operatorname{Hom}_S(Y,U)
=\operatorname{Hom}_S(T_Y,U).
\tag{6.3}
\]
The last equality includes all maps, since \(U\) is affine over \(S\) and \(T_Y\) is the relative spectrum of the pushforward algebra. This makes \(Y\mapsto T_Y\) left adjoint to \(f^*\). Equation (5.7), after base change to \(U\), gives \(T_{U\times_SX}=U\), compatibly with morphisms. In (6.3) set \(Y=V\times_SX\) to obtain
\(\operatorname{Hom}_X(V\times_SX,U\times_SX)=\operatorname{Hom}_S(V,U)\).
This proves full faithfulness directly.

**Trivial composite.** The restriction of \(f^*U\) to \(X_{\bar s}\) is a finite disjoint union of copies of \(X_{\bar s}\), since \(U_{\bar s}\) is a finite set of geometric points. Thus \(ab=1\), where \(1\) denotes the trivial homomorphism.

**Normality of the fibre image.** Let \(Y\to X\) be a connected finite étale cover whose restriction to \(X_{\bar s}\) has a section. The section image is an open-and-closed connected component \(Z\) isomorphic to \(X_{\bar s}\). In (5.8), \(T_Y\) is connected, because the surjective evaluation map \(Y\to T_Y\) has connected source. Hence \(T_Y\times_SX\) is connected by the initial argument.

There is a map of finite étale \(X\)-schemes
\[
\lambda:Y\longrightarrow T_Y\times_SX.
\tag{6.4}
\]
It is finite étale by the map-between-covers observation in the preceding lesson. The component \(Z\) corresponds to one point \(\bar t\in(T_Y)_{\bar s}\), by Theorem 5.1. Choose a closed point of \(X_{\bar s}\); it is rational over the algebraically closed residue field of \(\bar s\), because the fibre is nonempty of finite type. The fibre of \(\lambda\) over that point together with \(\bar t\) is the fibre of \(Z\to X_{\bar s}\), so has degree one. The degree of \(\lambda\) is locally constant on its connected target. It is consequently one everywhere, and the rank-one algebra argument makes \(\lambda\) an isomorphism.

Thus a connected \(Y\) with one section on the chosen fibre becomes completely trivial on that fibre. The normality criterion of *Galois categories*, Theorem 4.5, says exactly that \(\operatorname{im}b\) is normal in \(\pi_1(X)\).

**The whole kernel.** Suppose now \(Y\to X\), not necessarily connected, becomes trivial on \(X_{\bar s}\). Decompose it into its finitely many connected covers \(Y_j\), as in the preceding lesson. Each nonempty \(Y_j\) surjects onto connected \(X\), so its fibre is nonempty. Since that fibre is trivial, it contains a section. The argument for (6.4) gives
\[
Y_j\simeq T_{Y_j}\times_SX.
\]
Taking the disjoint union proves \(Y\simeq f^*T\) for the finite étale
\(T=\coprod_jT_{Y_j}\) over \(S\); the empty case uses the empty \(T\).

Consequently \(f^*\) is fully faithful, its composite with \(i^*\) trivializes objects, and every object trivialized by \(i^*\) lies in its essential image, in particular is an epic image of an object in that image. The closed-normal-kernel criterion of *Galois categories*, Theorem 4.4, identifies \(\ker a\) with the closed normal subgroup generated by \(\operatorname{im}b\). This image is already normal, and is closed because the source is profinite and the target Hausdorff. Therefore \(\ker a=\operatorname{im}b\). This completes every exactness condition in (6.1). \(\square\)

Flatness, finite presentation and geometric reducedness entered Theorem 5.1. Properness controlled both the global-functions algebra and the connectedness argument. Geometric connectedness made (5.7) hold and gave surjectivity on the right. These uses do not establish a converse saying that failure of any single hypothesis forces nonexactness in every example.

## 7. Examples and complete solutions

We first record the cover-subgroup calculation used in the disconnected-fibre example.

**Lemma 7.1.** If \(S\) is connected and \(U\to S\) is connected finite étale of degree \(n\), and \(\bar u\) is a point over \(\bar s\), then
\(\pi_1(U,\bar u)\to\pi_1(S,\bar s)\) is injective with open image of index \(n\), equal to the stabilizer of \(\bar u\) in the fibre action.

*Proof.* Composition gives an equivalence
\[
\operatorname{F\acute Et}(U)\simeq
\operatorname{F\acute Et}(S)/U.
\]
A map to \(U\) from a finite étale \(S\)-scheme is finite étale over \(U\), and composition preserves finiteness and étaleness, so this includes all objects and all maps. Put \(\Pi=\pi_1(S,\bar s)\). The reconstruction theorem identifies \(U\)'s fibre with \(\Pi/H\), for the open stabilizer \(H\) at \(\bar u\). Finite \(\Pi\)-sets over \(\Pi/H\) are equivalent to finite continuous \(H\)-sets: take the fibre over \(H\), with inverse the induced set \(\Pi\times_HE\). The latter is finite because \(H\) has finite index; its action is continuous because the kernel of a finite \(H\)-action contains an open subgroup whose core in \(\Pi\) is open. The fibre functor at \(\bar u\) is the underlying-set functor on this \(H\)-category. Its automorphism group is \(H\), by *Galois categories*, Lemma 1.1. The functorial map is its inclusion in \(\Pi\), and \([\Pi:H]=n\). \(\square\)

### 7.1. The projective line over a connected base

For any connected scheme \(S\), the projection \(\mathbf P^1_S\to S\) is proper, smooth and of finite presentation, with geometrically connected reduced fibres. The fibre group is trivial by the preceding lesson's all-characteristic projective-line computation. Theorem 6.1 therefore gives
\[
\pi_1(\mathbf P^1_S)\simeq\pi_1(S).
\tag{7.1}
\]
The section \([1:0]\) supplies the inverse group map after compatible base points are chosen. A section alone makes the projection map surjective and the section map injective; injectivity of the projection in (7.1) comes from the trivial fibre group and exactness.

### 7.2. A connected double cover with disconnected fibres

Let \(k\) be any field of characteristic different from two. The scheme
\[
U=\operatorname{Spec}k[x,t,t^{-1}]/(x^2-t)
\longrightarrow\mathbf G_{m,k}
\tag{7.2}
\]
is \(\mathbf G_{m,k}\) itself in coordinate \(x\), since \(x\) is invertible and \(t=x^2\). It is connected and finite étale of degree two: the algebra is free with basis \(1,x\), and derivative \(2x\) is invertible. Its deck involution is \(x\mapsto-x\), so it is Galois.

Lemma 7.1 identifies the image of its group map as an open subgroup of index two, the kernel of the quotient
\[
\pi_1(\mathbf G_{m,k})\twoheadrightarrow\mathbf Z/2\mathbf Z
\]
defined by this cover. It is not surjective. All geometric fibres have two points. Thus (7.2) satisfies properness, flatness, finite presentation and geometric reducedness, but fails geometric connectedness. This is the needed counterexample to omitting that hypothesis. When \(k\) is algebraically closed of characteristic zero, compatible roots identify the group with \(\widehat{\mathbf Z}\), and the subgroup is \(2\widehat{\mathbf Z}\).

**Exercise 7.1 (easy).** Show that reduction preserves the fundamental group.

*Solution.* The immersion \(X_{\mathrm{red}}\hookrightarrow X\) is defined on every affine by its nilradical and is a thickening. Proposition 1.1 gives an equivalence of finite étale categories, including every map. Restriction preserves the geometric fibre at a chosen geometric point of \(X_{\mathrm{red}}\). It therefore preserves the natural automorphism group of that fibre functor and its topology of agreement on finite fibres. For connected \(X\) this proves
\(\pi_1(X_{\mathrm{red}})\simeq\pi_1(X)\). No global nilpotence bound is needed.

**Exercise 7.2 (medium).** Prove purely inseparable invariance for an arbitrary algebraic purely inseparable extension \(k'/k\).

*Solution.* The projection \(X_{k'}\to X\) is integral, since the scalars in \(k'\) satisfy monic equations over \(k\). After any base change it is surjective, and each point has a unique lift with purely inseparable residue extension. This is checked for finite subextensions by the equations \(T^{p^r}-c\), whose geometric zero sets have one point, and then for their filtered union by compatible unique extensions of primes. Thus it is a universal homeomorphism [Stacks, Tag 04DF](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-universal-homeomorphism). Theorem 1.2 gives the finite étale category equivalence with geometric fibres identified, and hence the asserted fundamental-group isomorphism for connected schemes. The same proof includes infinite extensions; no finite-presentation condition is used.

**Exercise 7.3 (medium).** Compute the image of the group map in (7.2), and identify the failed homotopy hypothesis.

*Solution.* The ring identifies the source with \(k[x,x^{-1}]\), so it is connected. The finite étale degree is two, and the nontrivial deck involution exchanges the two points of each geometric fibre. The fibre is the transitive regular two-element set for the quotient \(\mathbf Z/2\mathbf Z\) of the target fundamental group. The stabilizer of a chosen point is its quotient kernel. Lemma 7.1 proves that the source group maps injectively onto this stabilizer, of index two. The map is therefore not surjective. Its fibres are reduced but disconnected; the other hypotheses hold because the morphism is finite étale. This isolates the geometric-connectedness failure without imposing a characteristic-zero assumption.

**Exercise 7.4 (medium).** Compute \(\pi_1(\mathbf P^1_S)\) for connected \(S\), and explain the role of a section.

*Solution.* The projection is proper flat and of finite presentation, and every geometric fibre is \(\mathbf P^1\) over an algebraically closed field. These fibres are geometrically connected and reduced, and have trivial fundamental group by the differential-degree proof in the preceding lesson. The homotopy sequence becomes
\[
1\longrightarrow\pi_1(\mathbf P^1_S)\xrightarrow{f_*}
\pi_1(S)\longrightarrow1,
\]
where the first \(1\) denotes the trivial fibre image, not an additional claim about injectivity of a general homotopy arrow. Exactness proves both trivial kernel and surjectivity of \(f_*\). The section \(s=[1:0]\), with compatible geometric base point, satisfies \(f_*s_*=\mathrm{id}\). Since \(f_*\) is already injective, it follows that \(s_*f_*=\mathrm{id}\) too. Hence the section supplies the inverse in (7.1). It is exactness and fibre triviality that prove injectivity of \(f_*\), not merely the existence of the section.

**Exercise 7.5 (hard).** For algebraically closed \(k\subsetneq k'\) of characteristic \(p\), prove that (4.1), with \(a\notin k\), cannot descend even as a cover with its group action forgotten.

*Solution.* If it descended to \(V\), that \(V\) would be connected of degree \(p\), because base change is faithfully flat. Every connected finite étale cover over algebraically closed \(k\) stays connected over \(k'\), by [Stacks, Tag 0363](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/varieties.html#varieties-lemma-separably-closed-field-connected-components). Thus the Galois-category test makes this base-change functor fully faithful. Its bijection on endomorphisms makes the translation \(y\mapsto y+1\) descend to an automorphism \(\sigma\) of \(V\). Its order is \(p\), and it acts freely on geometric fibres by connected-object one-point uniqueness. Since those fibres have \(p\) points, it gives a torsor action.

For its algebra \(B/k[x]\), choose \(b\) of trace one; trace is surjective after a split étale covering, hence before it. The sum (4.3) gives \(z\) with \(\sigma z-z=1\). Thus \(B=k[x,z]/(z^p-z-h)\) for \(h\in k[x]\), by the fibre-isomorphism argument of Section 4. Under the proposed isomorphism to \(W_a\), the coordinates differ by an invariant polynomial in \(k'[x]\), so \(a x-h\) is an Artin–Schreier difference.

Remove constants and reduce all \(p\)-divisible exponents of \(h\) by taking \(p\)th roots of their coefficients in \(k\), as in (4.4). This leaves a polynomial with coefficients in \(k\) and only positive exponents prime to \(p\). Its difference from \(a x\) has the same form. A nonconstant Artin–Schreier difference has highest exponent divisible by \(p\), so that reduced difference must be zero. Its coefficient of \(x\) then gives \(a\in k\), a contradiction. This proves failure of essential surjectivity, even for the underlying cover, and therefore failure of proper-field invariance without properness.

## 8. What this lesson does not prove

We have proved finite étale topological invariance, the complete Noetherian local equivalence, proper algebraically closed field invariance, the finite étale Stein factorization, the homotopy exact sequence, both counterexamples, and all five solutions. We used these precise inputs:

- Finite étale invariance under arbitrary thickenings, including every morphism and finiteness of the lift, is imported from [*Infinitesimal lifting and invariance under thickenings*, Theorem 6.2](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-FSE/infinitesimal-lifting-and-invariance-under-thickenings.html#6-keeping-the-lift-finite). Proposition 1.1 derives the geometric-fibre and fundamental-group consequences. The integral-surjection descent theorem and full faithfulness were proved in [*Descending properties of schemes and morphisms*](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-DFG/AG-DFG-03.html) at their full quasi-compact separated étale generality.
- The characterization of universal homeomorphisms and the surjective-diagonal criterion for universal injectivity [Stacks, Tags [04DF](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-universal-homeomorphism), [01S4](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-universally-injective)]. Proper quasi-finite finiteness is the stated Zariski Main consequence from the [quasi-finite-morphism prerequisite](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-FSE/etale-neighbourhoods-henselization-and-quasi-finite-morphisms.html#4-extracting-the-finite-branches).
- Coherent Grothendieck existence for a proper scheme over a complete Noetherian local ring, with full faithfulness and tensor compatibility [Stacks, Tag 088E](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/coherent.html#coherent-theorem-grothendieck-existence), from the formal-cohomology prerequisite. Noetherian Krull intersection [Stacks, Tag 00IQ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-intersection-powers-ideal-module), Nakayama, and openness of the local-freeness locus for coherent modules are the accompanying commutative-algebra facts.
- The three full henselian statements in Section 2.2 [Stacks, Tags [09ZS](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-lemma-gabber), [0A48](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-lemma-finite-etale-on-proper-over-henselian), [0GS2](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-lemma-finite-etale-on-proper-over-henselian-pair)]. Their general approximation proofs are permitted inputs. Flatness and the étale-neighbourhood description of henselization and strict henselization belong to the [henselization prerequisite](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-FSE/etale-neighbourhoods-henselization-and-quasi-finite-morphisms.html#3-the-two-colimits-of-local-choices).
- Finite-presentation approximation of objects, maps and equality [Stacks, Tags [01ZM](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/limits.html#limits-lemma-descend-finite-presentation), [01ZO](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/limits.html#limits-lemma-descend-finite-finite-presentation), [07RP](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/limits.html#limits-lemma-descend-etale)], already stated precisely in the preceding lesson. The Nullstellensatz supplies the specialization point in Section 3.
- Perfect direct image and arbitrary derived base change for \(\mathcal O_X\) under proper flat finite-presentation morphisms [Stacks, Tag 0B91](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/perfect.html#perfect-lemma-flat-proper-perfect-direct-image-general), and coherent proper finiteness [Stacks, Tag 02O6](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/coherent.html#coherent-lemma-proper-over-affine-cohomology-finite), from cohomology and base change. Sections 5.1–5.2 proved the needed degree-zero splitting and every further step producing the finite étale algebra; the Stein assertion itself was not assumed.
- The connected-component invariance over a separably closed field [Stacks, Tag 0363](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/varieties.html#varieties-lemma-separably-closed-field-connected-components), valid for arbitrary schemes and field extensions; the spectral-space component facts [Stacks, Tags [094L](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/properties.html#properties-lemma-quasi-compact-quasi-separated-spectral), [005F](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/topology.html#topology-lemma-connected-component-intersection), [0900](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/topology.html#topology-lemma-pi0-profinite)], used only with the explicit quasi-compact quasi-separated hypotheses in Proposition 1.3.
- The finite étale algebra criterion, geometric reducedness under étale maps, and basic smoothness and properness of projective space, from the étale and scheme prerequisites. All Galois-category tests used here were proved in *Galois categories*.

The next lesson uses the henselian proper equivalence to compare generic and special fibres. It will keep the hypotheses of specialization and of tame ramification separate: an exact homotopy sequence alone does not identify all the fundamental groups in a family.
