# Lefschetz theorems for finite étale covers

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by GPT-6.1 Sol, the AI that wrote it. Public domain (CC0).*

A finite étale cover has an underlying vector bundle, together with multiplication and a unit. This lets formal comparison for vector bundles control maps of covers. Existence is subtler: an algebraized bundle must acquire its algebra structure, and the resulting finite map must be étale. Finally, a cover constructed near an ample zero scheme may still have to be extended over finitely many omitted points.

We use Formal geometry along a closed subscheme, especially its section comparison, full-faithfulness tests and vector-bundle existence theorem, and the depth and completion results in Local cohomology. We assume faithfully flat descent, the elementary properties of finite étale morphisms, and Galois categories. The identification of finite étale covers with finite continuous fundamental-group sets is [Stacks, [Tag 0BNB](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-lemma-finite-etale-connected-galois-category), [Tag 0BND](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-theorem-fundamental-group)]. We specify the two algebraic gluing inputs in Section 3.

Write \(\operatorname{FEt}(X)\) for the category of schemes finite étale over \(X\), allowing disconnected covers and the empty cover. When \(X\) is connected and \(\bar x\) is a geometric point, its fundamental group is the group of automorphisms of the geometric-fibre functor, with its profinite topology. For a geometric point \(\bar y\) of \(Y\subset X\), the comparison homomorphism always means
\[
\pi_1(Y,\bar y)\longrightarrow\pi_1(X,\bar y).
\tag{0.1}
\]
We will first formulate categorical assertions without connectedness assumptions.

## 1. Faithfulness and the group interpretation

**Proposition 1.1.** Let \(Y\subset X\) be a closed subscheme of any scheme. If every connected component of \(X\) meets \(Y\), restriction
\(\operatorname{FEt}(X)\to\operatorname{FEt}(Y)\) is faithful.

**Proof.** For two maps \(a,b:T\to T'\) of finite étale \(X\)-schemes, their equalizer \(E\subset T\) is open and closed: the diagonal of the finite étale separated scheme \(T'\) is open and closed. If the maps agree over \(Y\), the complement \(D=T\setminus E\) has no point over \(Y\). But \(D\to X\) is finite étale. Its image is closed by finiteness and open by flatness and finite presentation. If this image were nonempty, it would contain a connected component of \(X\), which meets \(Y\). That contradicts the defining property of \(D\). Thus \(D\) is empty and \(a=b\). This argument does not require the connected components themselves to be open. ∎

This is [Stacks, [Tag 0EJX](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-lemma-restriction-faithful)]. In the local situation
\[
X=\operatorname{Spec}A,\quad X_0=\operatorname{Spec}(A/fA),\quad
U=X\setminus\{\mathfrak m\},\quad U_0=X_0\setminus\{\mathfrak m\},
\tag{1.1}
\]
where \(A\) is Noetherian local and \(f\in\mathfrak m\), a sufficient condition for faithfulness is
\[
\dim(A/\mathfrak p)\ge2
\quad\text{for every minimal prime }\mathfrak p\text{ not containing }f.
\tag{1.2}
\]
Indeed a component contained in \(V(f)\) already meets \(U_0\) if it occurs in \(U\). On any other component, a prime minimal over its nonzero principal ideal \((f)\) has height at most one. In a local domain of dimension at least two this prime is not the closed point. Thus every irreducible component of \(U\), and hence every connected component, meets \(U_0\). Proposition 1.1 proves [Stacks, [Tag 0BLG](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-lemma-faithful)].

**Lemma 1.2.** Suppose \(X\) is connected, \(Y\subset X\) is Noetherian, and restriction of finite étale covers is fully faithful. Then \(Y\) is nonempty and connected, and (0.1) is surjective. If restriction is an equivalence, (0.1) is an isomorphism.

**Proof.** Maps \(X\to X\amalg X\) over \(X\) correspond to open-and-closed decompositions of \(X\); there are exactly two. Full faithfulness says the same about \(Y\). An empty \(Y\) would give one map, and a disconnected \(Y\) at least four. Hence \(Y\) is nonempty and connected.

Use the Galois-category descriptions, and put \(H=\pi_1(Y,\bar y)\), \(G=\pi_1(X,\bar y)\). Restriction of covers becomes restriction of finite \(G\)-sets along \(H\to G\). If the image in a finite quotient \(Q\) of \(G\) were a proper subgroup, the regular \(Q\)-set would have more than one orbit under that image. An indicator function of one such orbit would be an \(H\)-equivariant map \(Q\to\{0,1\}\), with trivial action on the target, but would not be \(G\)-equivariant. This contradicts fullness. Thus the image fills every finite quotient of \(G\). It is dense, and it is closed because \(H\) is compact, so it is all of \(G\).

If restriction is also essentially surjective, an element of the kernel acts trivially on every finite \(H\)-set, since every such set comes from \(G\). Finite quotients separate elements of a profinite group, so the kernel is trivial. The continuous bijection between compact Hausdorff groups is an isomorphism. ∎

Full faithfulness, rather than faithfulness alone, is the condition used to obtain surjectivity. This is why comparing all maps between covers matters.

## 2. Passing through the formal completion

Let \(X\) be Noetherian, \(Y=V(\mathcal I)\), and \(Y_n=V(\mathcal I^n)\), with \(n\ge1\). A finite étale cover of \(Y\) has a unique compatible lift, up to unique isomorphism, to finite étale covers of all \(Y_n\). More precisely, restriction across a nilpotent thickening is an equivalence, including on morphisms [Stacks, [Tag 0BQB](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-lemma-thickening)]. This is the usual infinitesimal invariance of étale morphisms. Standard étale presentations lift across nilpotent ideals because their invertible Jacobian remains invertible; uniqueness of lifts of maps gives gluing. Finiteness persists across these thickenings. We use this basic étale fact throughout.

**Proposition 2.1 (formal comparison of covers).** If completion is fully faithful on vector bundles on \(X\), then
\[
\operatorname{FEt}(X)\longrightarrow\operatorname{FEt}(Y)
\tag{2.1}
\]
is fully faithful. If completion is an equivalence on vector bundles, (2.1) is an equivalence. Both statements hold for germs of neighbourhoods of \(Y\), with the corresponding hypotheses on vector bundles on neighbourhoods.

**Proof.** Let \(T,T'\) be finite étale over \(X\), with finite locally free algebras \(B,B'\). A map over \(Y\) gives, by infinitesimal invariance, compatible algebra maps
\[
B'/\mathcal I^nB'\longrightarrow B/\mathcal I^nB.
\]
Full faithfulness for bundles gives a unique ordinary module map \(B'\to B\). It is an algebra map: the two maps \(B'\otimes B'\to B\) expressing compatibility with multiplication agree after completion, and faithfulness detects their equality. The unit equation is checked on the map \(\mathcal O_X\to B\) in the same way. This proves full faithfulness for covers.

Now start with a finite étale cover \(T_1\to Y\) and its lifts \(T_n\to Y_n\). Their algebras \(B_n\) form a finite locally free formal module. Algebraize it to a vector bundle \(B\). Fullness lifts the multiplication \(B^\wedge\otimes B^\wedge\to B^\wedge\) and unit \(\mathcal O_X^\wedge\to B^\wedge\). Faithfulness detects the associativity, commutativity and unit equations, so \(B\) is a finite locally free algebra.

We must check étaleness. For such an algebra the trace pairing gives a bundle map
\[
q:B\longrightarrow B^\vee,\qquad
b\longmapsto\bigl(c\mapsto\operatorname{Tr}(bc)\bigr).
\tag{2.2}
\]
It is an isomorphism exactly when \(\operatorname{Spec}_XB\to X\) is étale [Stacks, [Tag 0BJF](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/discriminant.html#discriminant-lemma-discriminant)]. Each completed level is étale, so \(q^\wedge\) has an inverse. Fullness lifts that inverse to \(B^\vee\to B\), and faithfulness makes its two composites the identity. Hence \(q\) is an isomorphism on all of \(X\).

For neighbourhood germs, lift the maps after shrinking to one common neighbourhood. Each of the finitely many algebra equations holds after further shrinking, by faithfulness in the germ category. The trace pairing is already invertible on \(Y\); its noninvertibility locus is closed in the neighbourhood and disjoint from \(Y\). Remove that locus. This produces a finite étale cover on an ordinary neighbourhood. Uniqueness of maps is likewise uniqueness after shrinking. ∎

These arguments prove [Stacks, [Tag 0EL8](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-lemma-restriction-fully-faithful), [Tag 0EL9](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-lemma-restriction-equivalence), [Tag 0ELA](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-lemma-restriction-fully-faithful-general), [Tag 0EK1](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-lemma-restriction-equivalence-general)]. No principal ideal was assumed: the formal algebra at level \(n\) is locally \((\mathcal O_X/\mathcal I^n)^r\).

The previous lesson's section tests therefore give the following useful criteria. Full faithfulness follows if \(X\) is quasi-affine and
\(\Gamma(X,\mathcal O_X)\to\varprojlim\Gamma(Y_n,\mathcal O_{Y_n})\) is an isomorphism; or if \(X\) has an ample \(L\) and the corresponding comparison holds for every sufficiently high \(L^m\); or if it holds for every vector bundle. The same tests with colimits of neighbourhood sections prove full faithfulness for neighbourhood covers. The two locally split presentations in that lesson reduce general bundles to ample powers, so the tests require no cohomology vanishing for every bundle separately. This gives [Stacks, [Tag 0EJZ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-lemma-restriction-fully-faithful-special), [Tag 0EK0](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-lemma-restriction-fully-faithful-general-special)].

We will also use the finite étale **internal Hom**. For covers \(T,T'\) of \(X\), there is a finite étale \(X\)-scheme \(\underline{\operatorname{Hom}}_X(T,T')\) whose sections after any base change are maps from \(T\) to \(T'\). Étale locally the covers are constant finite sets \(S,S'\), and this Hom is the constant set of functions \(S\to S'\). The descriptions glue by faithfully flat descent, including their representing property. Thus lifting arbitrary maps of covers reduces to lifting sections of one cover [Stacks, [Tag 04HN](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale.html#etale-lemma-finite-etale-etale-local), [Tag 0BL7](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-lemma-internal-hom-finite-etale)].

## 3. The local Lefschetz theorem

We use (1.1). Here \(f\) is arbitrary; it need not be a nonzerodivisor. A henselian pair \((A,(f))\) has the idempotent-lifting property: for every finite \(A\)-algebra \(B\), idempotents of \(B/fB\) lift uniquely to \(B\). A henselian local ring has this property for every ideal in its maximal ideal.

Two gluing inputs will be used with their exact scopes.

- **Finite formal gluing.** For a Noetherian local \(A\), put \(\widehat A=\varprojlim A/\mathfrak m^n\), \(\widehat X=\operatorname{Spec}\widehat A\), and \(\widehat U=U\times_X\widehat X\). A finite algebra on \(U\) and a finite \(\widehat A\)-algebra, identified on \(\widehat U\), glue to a finite \(A\)-algebra with those restrictions. Indeed the flat-map gluing equivalence [Stacks, [Tag 05ER](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-algebra.html#more-algebra-proposition-equivalence)] applies to generators \(g_i\) of \(\mathfrak m\), since \(A/\mathfrak m=\widehat A/\mathfrak m\widehat A\). Its data are the module over \(\widehat A\), the modules over \(A_{g_i}\), and their overlap identifications. The equivalence respects tensor products, so multiplication and unit descend. Finiteness is detected after the faithfully flat base change to \(\widehat A\). This proves the finite-algebra assertion of [Stacks, [Tag 0BLH](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-lemma-fill-in-missing)].
- **Finite extension across the missing point.** A finite cover of \(\widehat U\) admits a finite extension to \(\widehat X\), without a claim that this extension is étale at the closed point. Its composite to the affine Noetherian \(\widehat X\) is quasi-finite and separated. Zariski's main theorem factors it as an open immersion into a finite scheme [Stacks, [Tag 05K0](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-morphisms.html#more-morphisms-lemma-quasi-finite-separated-pass-through-finite)]. Replace that finite scheme by the scheme-theoretic closure of the given open. Over \(\widehat U\) the original open is also closed, because it is finite there; density of the closure therefore makes its restriction exactly the given cover.

**Lemma 3.1 (henselian descent from completion).** Suppose \((A,(f))\) is henselian. If
\[
\operatorname{FEt}(\widehat U)\longrightarrow
\operatorname{FEt}(\widehat U_0)
\tag{3.1}
\]
is fully faithful, then \(\operatorname{FEt}(U)\to\operatorname{FEt}(U_0)\) is fully faithful.

**Proof.** Faithfulness follows from (3.1) and faithful flatness of \(\widehat A/A\). By the internal Hom it remains to extend a section \(s_0:U_0\to T_0\), where \(T\to U\) is finite étale. Fullness over the completion gives \(s':\widehat U\to\widehat T\). A section of a finite étale cover is open and closed, so
\[
\widehat T=s'(\widehat U)\amalg W'.
\]
Choose a finite extension \(Z'\) of \(W'\) to \(\widehat X\), by the second input, and set \(Y'=\widehat X\amalg Z'\). The first input glues \(T\) and \(Y'\) to \(Y=\operatorname{Spec}B\), finite over \(X\).

We must descend the idempotent \(e'\) selecting the \(\widehat X\) summand. If \(U_0\) is empty, (3.1) forces \(\widehat U\) to be empty: otherwise the two constant sections of \(\widehat U\amalg\widehat U\) would have the same empty restriction. Then \(U\) is empty and there is nothing to prove. Assume \(U_0\ne\varnothing\).

In \(Y_0=\operatorname{Spec}(B/fB)\), take the scheme-theoretic closure of the image \(s_0(U_0)\). Flat base change to \(\widehat A\) commutes with this closure, since the immersion is quasi-compact. Its underlying subset after base change is exactly the \(\widehat X_0\) summand: the nonempty punctured spectrum of the local ring \(\widehat A/f\widehat A\) is topologically dense in its spectrum. In particular this subset is open and closed. A faithfully flat quasi-compact map is a quotient map for topology, so the underlying closure in \(Y_0\) is open and closed too. Let \(e_0\in B/fB\) be its idempotent. Only this open-and-closed subset is needed; no assertion that a schematic closure preserves every embedded closed-point structure is required.

Lift \(e_0\) to \(e\in B\) by henselianity. Its image in \(B\otimes_A\widehat A\) is \(e'\), by uniqueness of idempotent lifting modulo \(f\). Here a finite algebra over the complete local ring \(\widehat A\) is henselian, and \(f\) lies in its Jacobson radical. The summand \(Y_1\subset Y\) selected by \(e\) becomes \(\widehat X\) after completion. Faithful flatness detects that \(Y_1\to X\) is an isomorphism. Its restriction gives the desired section \(U\to T\); agreement with \(s_0\) is detected after the same faithfully flat base change. This proves fullness and the lemma. ∎

This supplies the descent in [Stacks, [Tag 0BLI](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-lemma-fully-faithful-henselian-completion)]. Completion in this lemma is \(\mathfrak m\)-adic, not merely \(f\)-adic.

**Theorem 3.2 (local Lefschetz).** In (1.1), if \(\operatorname{depth}A\ge3\) and \((A,(f))\) is henselian, then
\[
\operatorname{FEt}(U)\longrightarrow\operatorname{FEt}(U_0)
\tag{3.2}
\]
is fully faithful.

More generally, the same conclusion holds if \(H^1_{\mathfrak m}(A)\) and \(H^2_{\mathfrak m}(A)\) are each killed by a power of \(f\), with the same henselian hypothesis.

**Proof.** Depth at least three kills both displayed local cohomology groups, by the depth criterion proved in Local cohomology. Thus it suffices to prove the more general assertion. Flat completion carries these two annihilators to the corresponding groups over \(\widehat A\), by the finite Čech complex. Lemma 3.1 reduces to \(\widehat A\).

A Noetherian complete local ring is \(f\)-adically complete for \(f\in\mathfrak m\). To see this, an \(f\)-adic Cauchy sequence is \(\mathfrak m\)-adically Cauchy; its limit lies in every required \(f^n\)-coset since each finite ideal \(f^n\widehat A\) is \(\mathfrak m\)-adically closed. Separation follows from Krull intersection. Apply Lemma 3.2 of Formal geometry with \(\sigma=1\), \(M=\widehat A\), and support at its maximal ideal. It gives
\[
\Gamma(\widehat U,\mathcal O_{\widehat U})
\simeq
\varprojlim_n\Gamma(\widehat U,
\mathcal O_{\widehat U}/f^n\mathcal O_{\widehat U}).
\tag{3.3}
\]
The proof of that lemma used a two-term complex and bounded coherent \(f\)-torsion; it did not assume \(f\) regular. Since \(\widehat U\) is quasi-affine, the section test in Section 2 gives full faithfulness for covers restricted to \(\widehat U_0\). Lemma 3.1 descends it. ∎

The first assertion is [Stacks, [Tag 0BLJ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-lemma-fully-faithful)], and the annihilator version is [Stacks, [Tag 0BM6](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-lemma-fully-faithful-minimal)]. Full faithfulness does not assert that every cover of the punctured hypersurface comes from all of \(U\).

## 4. Local existence on neighbourhoods

We now impose that \(f\) is a nonzerodivisor and that \(A\) is \(f\)-adically complete. These are additional hypotheses, unlike those of Theorem 3.2.

**Lemma 4.1 (sections after shrinking).** If \(H^1_{\mathfrak m}(A/fA)\) is finite, then
\[
\operatorname*{colim}_{U_0\subset V\subset U}
\Gamma(V,\mathcal O_V)
\simeq
\varprojlim_n\Gamma(U,\mathcal O_U/f^n\mathcal O_U).
\tag{4.1}
\]

**Proof.** Set \(E_n=\mathcal O_U/f^n\mathcal O_U\) and \(N=\varprojlim\Gamma(U,E_n)\). The support sequence makes \(\Gamma(U,E_1)\) finite: it is an extension of a quotient of \(A/fA\) by \(H^1_{\mathfrak m}(A/fA)\).

The exact regular-system sequences \(0\to E_c\xrightarrow{f^n}E_{n+c}\to E_n\to0\) show
\(\ker(N\to\Gamma(U,E_n))=f^nN\), by left exactness of limits. Hence \(N\) is separated and complete for \(f\), and \(N/fN\) is a submodule of the finite \(\Gamma(U,E_1)\). Lift generators of that submodule and approximate successively in the complete ring \(A\). Topological Nakayama gives a finite presentation \(A^r\to N\). Also \(f\) is injective on \(N\): if a compatible section is killed by \(f\), its component at level \(n+1\) lies in \(f^nE_{n+1}\), so its component at level \(n\) is zero.

The natural map \(A\to N\) is an isomorphism near every point of \(U_0\). For \(g\in\mathfrak m\), localize
\[
A/fA\longrightarrow N/fN\longrightarrow\Gamma(U,E_1).
\]
The last module restricted to \(D(g)\) is \((A/fA)_g\), by quasi-coherent affine pushforward and localization. The second arrow is injective and the composite is an isomorphism, so the first arrow becomes an isomorphism on \(D(g)\). At a prime of \(U_0\), Nakayama first kills the cokernel of \(A\to N\). Its kernel modulo \(f\) is then zero because \(f\) is regular on both modules; Nakayama kills that kernel too. The finite kernel and cokernel therefore vanish on an open neighbourhood \(V\) of \(U_0\).

Every element of \(N\) consequently gives a section on some such \(V\), with its prescribed formal restrictions. Conversely a section with zero formal restrictions has zero stalk at every point of \(U_0\), by Krull intersection in the finite stalk. Its coherent support can be removed by shrinking \(V\), so its germ is zero. This proves (4.1). ∎

This is the principal local section argument of [Stacks, [Tag 0EIH](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebraization.html#algebraization-lemma-alternative-colim-H0), [Tag 0EKV](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebraization.html#algebraization-lemma-fully-faithful-general-alternative)]. In the localization step the open is \(D(g)\), where \(g\in\mathfrak m\); a quotient killed by \(f\) would have zero restriction to \(D(f)\).

**Theorem 4.2.** Under the completeness and regularity hypotheses of this section, restriction of neighbourhood covers
\[
\operatorname*{colim}_{U_0\subset V\subset U}\operatorname{FEt}(V)
\longrightarrow\operatorname{FEt}(U_0)
\tag{4.2}
\]
is fully faithful if \(H^1_{\mathfrak m}(A/fA)\) is finite. It is an equivalence if both \(H^1_{\mathfrak m}(A/fA)\) and \(H^2_{\mathfrak m}(A/fA)\) are finite.

**Proof.** Lemma 4.1, the quasi-affine neighbourhood test in Formal geometry, and Proposition 2.1 give full faithfulness. With both groups finite, lift a cover of \(U_0\) to its finite locally free formal algebra. The local algebraization statement (8.3) in Formal geometry, with \(\mathfrak a=\mathfrak m\), algebraizes its underlying formal bundle as a coherent module on \(U\) that is free on a neighbourhood of \(U_0\). Full faithfulness for bundles, obtained from Lemma 4.1, lifts its multiplication and unit after shrinking. The finitely many algebra equations hold on a smaller neighbourhood, and the trace pairing becomes invertible after another shrinking. Proposition 2.1's construction therefore produces the desired cover. ∎

These are [Stacks, [Tag 0BLP](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-lemma-fully-faithful-general), [Tag 0BLV](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-lemma-essentially-surjective-general)]. The formal-module input is precisely the openly licensed full proof at [Stacks, [Tag 0DXW](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebraization.html#algebraization-lemma-algebraization-principal-variant)], whose full hypotheses were recorded in the previous lesson.

**Proposition 4.3 (extending beyond the neighbourhood).** If both groups in Theorem 4.2 are finite, and purity holds for every local ring \((A_f)_{\mathfrak p}\) at a maximal ideal of \(A_f\), then \(\operatorname{FEt}(U)\to\operatorname{FEt}(U_0)\) is essentially surjective.

Here **purity holds for a Noetherian local ring** \((R,\mathfrak n)\) means that
\[
\operatorname{FEt}(\operatorname{Spec}R)\longrightarrow
\operatorname{FEt}(\operatorname{Spec}R\setminus\{\mathfrak n\})
\tag{4.3}
\]
is essentially surjective. This is a hypothesis about objects, as in [Stacks, [Tag 0BM7](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-section-local-purity)]; we have not yet proved it for regular rings.

**Proof.** Theorem 4.2 supplies a cover on some \(V\subset U\) containing \(U_0\). Its complement \(T\) is a finite set of closed points of \(U\), each maximal in \(\operatorname{Spec}A_f\). Indeed the closure in \(X\) of each irreducible component of \(T\) meets \(V(f)\) only at \(\mathfrak m\). If its generic prime is \(\mathfrak p\), then \(f\notin\mathfrak p\) and \(f\) generates an ideal with maximal radical in the local domain \(A/\mathfrak p\). The principal ideal theorem gives \(\dim(A/\mathfrak p)=1\). Its puncture is a single point; there are finitely many such components by Noetherianity.

At each omitted point apply (4.3) to extend the restricted cover over its local spectrum. These extensions glue to the cover on \(V\). For clarity, the gluing fact is elementary finite-presentation descent: an algebra over \(\mathcal O_{U,t}\) spreads to an affine neighbourhood of \(t\); its prescribed isomorphism on the puncture spreads after shrinking because that puncture is quasi-compact. Multiplication, inverse isomorphisms and all relations involve finitely many elements and equations, so one common shrinking suffices. Finiteness and étaleness hold after shrinking as well. Ordinary gluing on that neighbourhood and its overlap with \(V\) adds \(t\). Repeating for the finite set gives a cover of \(U\). This is the point-gluing assertion of [Stacks, [Tag 0BPA](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/limits.html#limits-lemma-glueing-near-closed-point)], and proves [Stacks, [Tag 0EKA](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-lemma-equivalence)]. ∎

The following variants are useful when the two cohomology modules are not explicitly known to be finite. Each has its full linked open proof at the tag following the statement. These arguments combine the general formal-section and formal-bundle criteria with the dualizing depth bounds; the last also extends across the omitted local points by purity. We retain their full source generality. Throughout use (1.1).

1. If \(A\) has a dualizing complex, is \(f\)-adically complete, and every irreducible component of \(X\) not contained in \(X_0\) has dimension at least three, (4.2) is fully faithful [Stacks, [Tag 0DXX](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-lemma-fully-faithful-general-better)].
2. If \(A\) has a dualizing complex and is \(f\)-adically complete, (4.2) is an equivalence under either of these conditions: \(A_f\) is \((S_2)\) and every component of \(X\) not contained in \(X_0\) has dimension at least four; or
   \[
   \operatorname{depth}A_{\mathfrak p}+\dim(A/\mathfrak p)>3
   \]
   whenever \(f\notin\mathfrak p\) and
   \(V(\mathfrak p)\cap V(f)\ne\{\mathfrak m\}\) [Stacks, [Tag 0DXY](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-lemma-essentially-surjective-general-better)].
3. If \(A\) has a dualizing complex and \((A,(f))\) is henselian, restriction on all of \(U\) is fully faithful under either of these conditions: \(A_f\) is \((S_2)\) and every component not contained in \(X_0\) has dimension at least three; or
   \[
   \operatorname{depth}A_{\mathfrak p}+\dim(A/\mathfrak p)>2
   \quad\text{for every }\mathfrak p\notin V(f)
   \]
   [Stacks, [Tag 0EK5](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-lemma-fully-faithful-simple)].
4. Add purity at every maximal localization of \(A_f\) to the hypotheses of item 2. Then restriction on all of \(U\) is essentially surjective [Stacks, [Tag 0EK9](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-lemma-equivalence-better)]. This assertion alone is not an equivalence unless full faithfulness is also known.

The closure-intersection exclusion in item 2, the different thresholds three and four, and the distinction between a henselian pair and a complete ring are part of these statements.

## 5. Global Lefschetz and purity

Let \(X\) be proper over a field \(k\), let \(L\) be ample, and let \(Y=Z(s)\) for \(s\in\Gamma(X,L)\). The section may be a zero divisor.

**Theorem 5.1 (global full faithfulness).** If
\[
\operatorname{depth}\mathcal O_{X,x}
+\dim\overline{\{x\}}>1
\quad(x\notin Y),
\tag{5.1}
\]
then \(\operatorname{FEt}(V)\to\operatorname{FEt}(Y)\) is fully faithful for every open \(V\supset Y\), including \(V=X\). If \(X\) is connected, \(Y\) is connected and (0.1) is surjective.

**Proof.** Apply Theorem 4.1 and Corollary 4.2 of Formal geometry with \(\sigma=1\) to every \(L^m\). Its stalk depth is that of its ring. These results give
\[
\Gamma(V,L^m)\simeq
\varprojlim_n\Gamma(Y_n,L^m|_{Y_n})
\]
for every \(m\), on each \(V\supset Y\). The ample-power comparison test gives full faithfulness of completion for vector bundles on \(V\). Proposition 2.1 gives the assertion for covers. Lemma 1.2 gives the connectedness and group statements. ∎

This proves [Stacks, [Tag 0ELC](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-proposition-lefschetz-fully-faithful)]. The depth condition is imposed outside \(Y\), with closure dimension in \(X\), not depth on \(Y\).

**Theorem 5.2 (global neighbourhood equivalence).** If
\[
\operatorname{depth}\mathcal O_{X,x}
+\dim\overline{\{x\}}>2
\quad(x\notin Y),
\tag{5.2}
\]
then
\[
\operatorname*{colim}_{Y\subset V\subset X}\operatorname{FEt}(V)
\longrightarrow\operatorname{FEt}(Y)
\tag{5.3}
\]
is an equivalence.

**Proof.** The vector-bundle neighbourhood equivalence, Theorem 6.4 of Formal geometry, applies exactly under (5.2), including arbitrary sections. Proposition 2.1 transports it to finite étale covers, lifting all algebra maps and equations on a common neighbourhood and removing the closed trace-degeneracy locus. ∎

This is [Stacks, [Tag 0ELD](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-proposition-lefschetz-equivalence-general)].

**Theorem 5.3 (global isomorphism under purity).** In addition to (5.2), suppose purity holds for \(\mathcal O_{X,x}\) at every closed point \(x\notin Y\). Then
\[
\operatorname{FEt}(X)\longrightarrow\operatorname{FEt}(Y)
\tag{5.4}
\]
is an equivalence. Consequently \(X\) and \(Y\) have the same connected components; if either is connected, (0.1) is an isomorphism.

**Proof.** Full faithfulness is Theorem 5.1. Theorem 5.2 algebraizes a cover of \(Y\) over an open \(V\supset Y\). The complement \(T=X\setminus V\), with its reduced closed structure, is proper over \(k\) and is closed in the affine scheme \(X\setminus Y\). The latter is affine because \(Y\) is the zero scheme of an ample section. Thus \(T\) is both proper and affine over \(k\), hence finite over \(k\). It is a finite set of closed points outside \(Y\).

At each of these points, the restriction of the cover to the punctured local spectrum extends by the assumed purity. The point-gluing argument of Proposition 4.3, now on \(X\), spreads the finite étale local algebra and its overlap identification to a neighbourhood and glues it to the existing cover. Add the finitely many points successively. This gives a finite étale cover of \(X\) whose restriction is the prescribed cover of \(Y\), proving essential surjectivity.

An equivalence preserves open-and-closed summands of the terminal object. For Noetherian schemes the connected components are open and closed and finite in number, so the component sets agree. The connected group assertion follows from Lemma 1.2. ∎

This proves [Stacks, [Tag 0ELE](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-proposition-lefschetz-equivalence)] with purity as a hypothesis. The regular-ring purity theorem of the later lesson is not used in this proof.

## 6. Examples and projective applications

**Example 6.1 (a curve on an abelian surface).** Let \(X\) be an abelian surface and let \(Y\) be a smooth curve cut out by an ample section. At a point of codimension \(h\), the smooth local ring has depth \(h\), while its closure has dimension \(2-h\). Their sum is two. Thus (5.1) holds and
\[
\pi_1(Y,\bar y)\twoheadrightarrow\pi_1(X,\bar y).
\]
Theorem 5.1 also proves that \(Y\) is connected. If \(k\) is algebraically closed and \(\ell\ne\operatorname{char}k\), multiplication by \(\ell\) on the abelian surface gives finite étale covers of degree \(\ell^4\) [Stacks, [Tag 0BFG](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/groupoids.html#groupoids-lemma-degree-multiplication-by-d), [Tag 0BFH](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/groupoids.html#groupoids-lemma-abelian-variety-multiplication-by-d-etale)]. Their pullbacks to \(Y\) remain connected: the corresponding transitive finite quotient action stays transitive under a surjective group homomorphism. So the comparison has a concrete consequence for covers, beyond its formal group statement.

**Example 6.2 (projective space without using purity).** Over an algebraically closed field, a connected finite étale cover \(C\to\mathbb P^1\) is a smooth projective curve. The unramified Riemann–Hurwitz formula [Stacks, [Tag 0C1B](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/curves.html#curves-section-riemann-hurewitz)] gives
\[
2g(C)-2=\deg(C/\mathbb P^1)(-2).
\]
Since the genus is nonnegative, the degree is one. Thus \(\pi_1(\mathbb P^1)=1\). For \(n\ge2\), restrict to a hyperplane. The depth-plus-closure sum on \(\mathbb P^n\) is \(n>1\), so Theorem 5.1 gives
\(\pi_1(\mathbb P^{n-1})\twoheadrightarrow\pi_1(\mathbb P^n)\).
Induction gives \(\pi_1(\mathbb P^n)=1\) in all characteristics. This calculation uses global surjectivity, not regular-ring purity.

**Example 6.3 (the plane cubic obstruction).** Let \(k\) be algebraically closed with \(\operatorname{char}k\ne2\), and let \(E\subset\mathbb P^2_k\) be a smooth cubic. Choose a point of \(E(k)\) as its origin. It is an elliptic curve. Multiplication by two,
\[
[2]:E\longrightarrow E,
\]
is a connected finite étale cover of degree four. Its differential is multiplication by two on the tangent line, hence invertible everywhere by translations; its degree is \(2^2\), the elementary elliptic-curve multiplication formula. The translations by \(E[2]\simeq(\mathbb Z/2)^2\) make it a Galois cover. Therefore \(\pi_1(E)\) has a nontrivial quotient, whereas Example 6.2 gives \(\pi_1(\mathbb P^2)=1\).

The comparison is surjective but not an isomorphism. Its failure occurs exactly at the stronger depth bound: on the smooth ambient surface the sum is two, which satisfies (5.1) and fails (5.2). In characteristic two use multiplication by three, of degree nine, for the same phenomenon. The elliptic multiplication facts in arbitrary characteristic are recorded in The ℓ-adic Tate module of an elliptic curve, Section 1.

**Example 6.4 (hypersurfaces and complete intersections).** A pure Cohen–Macaulay proper scheme of dimension \(n\) has depth-plus-closure sum \(n\). Hence an ample zero scheme in such a scheme has the surjectivity conclusion if \(n\ge2\), and the neighbourhood-equivalence conclusion if \(n\ge3\).

In particular, a smooth hypersurface \(Y\subset\mathbb P^n\) with \(n\ge3\) has the isomorphism conclusion once purity at the closed points of \(\mathbb P^n\setminus Y\) is supplied. With that purity hypothesis, Example 6.2 gives \(\pi_1(Y)=1\) over an algebraically closed field. The regular-ring purity theorem in the later lesson will supply it.

For a flag of projective complete intersections ending in dimension at least two, every preceding ambient member has dimension at least three and is Cohen–Macaulay. Apply Theorem 5.3 at each step, provided purity holds at the closed points of those ambient members off the next zero scheme. This gives the same fundamental group as projective space. Without those purity hypotheses the conclusions proved here are the successive surjections and the equivalences on neighbourhood germs. A singular intermediate complete intersection requires its own purity input; smoothness of the final member alone does not justify asserting it. The complete-intersection purity statement and resulting applications are addressed with purity later.

## 7. Exercises and solutions

**Exercise 7.1 (faithfulness; elementary).** Show that restriction of finite étale covers is faithful when every connected component of \(X\) meets \(Y\).

**Solution.** The equality locus of two maps of covers is open and closed in the source. Its complement is finite étale over \(X\), with open-and-closed image. If the maps agree over \(Y\), that image avoids \(Y\). A nonempty open-and-closed subset contains a connected component, contradicting the hypothesis. Thus the equality locus is the whole source. This also explains why connected components need not themselves be open.

**Exercise 7.2 (abelian surface; intermediate).** Show that a smooth ample curve on an abelian surface induces a surjection on fundamental groups.

**Solution.** The abelian surface is smooth and pure of dimension two. At its generic point the sum is \(0+2\); at a codimension-one point it is \(1+1\); at a closed point it is \(2+0\). Every sum is two, including at all points outside the curve. Theorem 5.1 therefore applies. It gives connectedness of the curve and the surjection for any chosen geometric point on it. No purity assumption is required for this conclusion.

**Exercise 7.3 (cubic; intermediate).** Exhibit a connected finite étale cover of a smooth plane cubic and locate the failed isomorphism hypothesis.

**Solution.** Over an algebraically closed field of characteristic different from two, choose an origin and use \([2]:E\to E\). Its source is connected, its degree is four and its derivative is invertible, so it is a nontrivial finite étale cover. Therefore \(\pi_1(E)\ne1\). On \(\mathbb P^2\), the depth-plus-closure sum equals two, not a number greater than two. Thus the stronger bound of Theorem 5.3 fails, although Theorem 5.1 still gives a surjection onto the trivial group. In characteristic two \([3]\) supplies the nontrivial cover instead. Over a non-algebraically-closed field one should compare geometric fundamental groups for the assertion that projective space has trivial group.

**Exercise 7.4 (normal surface; intermediate).** Let \(X\) be a connected normal projective surface, pure of dimension two, and let \(Y\) be the zero scheme of an ample section. Check (5.1) at all types of point and conclude surjectivity.

**Solution.** At a generic point the local ring is a field, so the sum is \(0+2=2\). At a codimension-one point normality gives a discrete valuation ring, of depth one; its closure has dimension one, giving \(1+1=2\). At a closed point normality gives \((S_2)\), hence depth at least two in its two-dimensional local ring; its closure dimension is zero. Thus every sum is at least two. Theorem 5.1 proves \(Y\) connected and \(\pi_1(Y,\bar y)\twoheadrightarrow\pi_1(X,\bar y)\). Normality was used both in codimension one and in the depth-two closed-point condition.

**Exercise 7.5 (a power-series local ring; advanced).** Let \(A=k[[x_1,\ldots,x_n]]\), \(n\ge3\), and \(f=x_n\). Prove full faithfulness and describe what essential surjectivity would require.

**Solution.** The variables form a regular sequence, so \(A\) has depth \(n\ge3\). It is \(f\)-adically complete: its elements can be expanded as formal power series in \(x_n\) with coefficients in \(k[[x_1,\ldots,x_{n-1}]]\). A complete ideal pair is henselian. Theorem 3.2 gives full faithfulness on all of \(U\).

The quotient \(A/fA\) is regular local of dimension \(n-1\). Its local cohomology below degree \(n-1\) vanishes. If \(n\ge4\), both degrees one and two vanish, so Theorem 4.2 gives algebraization of every cover of \(U_0\) on some neighbourhood \(V\subset U\). To get a cover on all of \(U\) by Proposition 4.3, one must additionally supply purity at the maximal localizations of \(A_f\).

If \(n=3\), the degree-two quotient cohomology is its nonzero top local cohomology and is not finite. One can see this in the inverse monomials \(x_1^{-a}x_2^{-b}\), \(a,b>0\), of the Čech quotient for \(k[[x_1,x_2]]\): multiplication by \(x_1\) is surjective on this nonzero module. If it were finite, Nakayama would make it zero. Thus the sufficient neighbourhood-existence hypothesis just used fails; full faithfulness alone proves no essential-surjectivity assertion. The later regular-ring purity theorem nevertheless supplies a different route in every \(n\ge3\): a cover of the punctured regular \(A/fA\) extends over \(\operatorname{Spec}(A/fA)\), and henselian equivalence of finite étale algebras [Stacks, [Tag 09ZS](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-lemma-gabber)] lifts that cover over \(\operatorname{Spec}A\), which restricts to \(U\). This last route is conditional here on that later purity input.

## Proof inputs

We use nilpotent invariance of finite étale covers, faithfully flat descent, the flat-map formal-gluing theorem, Zariski's main theorem and the Galois-category reconstruction as verified prerequisites. The local formal-module algebraization used in Theorem 4.2 has the exact open proof at Tag 0DXW, explained with its full hypotheses in Formal geometry, Section 8. The four dualizing-complex variants in Section 4 have the exact linked open proofs at Tags 0DXX, 0DXY, 0EK5 and 0EK9. The unramified Riemann–Hurwitz formula has its exact open proof at [Stacks, Tag 0C1B](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/curves.html#curves-section-riemann-hurewitz). The multiplication degree and étaleness theorem is also proved in the written programme lesson Abelian varieties, Theorem 6.1: multiplication by an integer n has degree n to the power twice the dimension, and is étale when n is invertible in the field.

Purity for regular local rings and complete intersections is not invoked as a proved result here. It is an explicit hypothesis in the global isomorphism and extension theorems, and the smooth and complete-intersection applications requiring it are correspondingly conditional. This order preserves the local Lefschetz theorem as an input to the later proof of purity.

## References

Linked Stacks proofs retain their [GNU Free Documentation License](https://github.com/stacks/stacks-project/blob/master/COPYING). The CC0 dedication covers the independently written exposition here.

- [Stacks] The Stacks Project authors, *The Stacks Project*, [official project](https://stacks.math.columbia.edu/). Tag links use AI Integrated Stacks Project, an edition with AI-proposed corrections and AI-written additions, not reviewed by the Stacks Project's maintainers. Its [English reader](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/) retains upstream tags. Relevant sections are Fundamental Groups of Schemes, “Local Lefschetz for the fundamental group,” “Finite étale covers of punctured spectra,” and “Lefschetz theorems”; Algebraic and Formal Geometry, “Completion functors”; and More on Algebra, “Formal glueing.”
- [Grothendieck–Laszlo] A. Grothendieck, *Cohomologie locale des faisceaux cohérents et théorèmes de Lefschetz locaux et globaux (SGA 2)*, revised edition edited by Y. Laszlo, [arXiv:math/0511279](https://arxiv.org/abs/math/0511279), Exposés X and XII, for local and global Lefschetz theorems.
