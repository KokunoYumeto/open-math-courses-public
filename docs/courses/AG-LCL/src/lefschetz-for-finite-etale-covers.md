# Lefschetz theorems for finite étale covers

*Mathematical exposition by GPT-6.1 Sol (OpenAI). Original exposition: CC0 1.0.*

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

Let \(X\) be Noetherian, \(Y=V(\mathcal I)\), and \(Y_n=V(\mathcal I^n)\), with \(n\ge1\). A finite étale cover of \(Y\) has a unique compatible lift, up to unique isomorphism, to finite étale covers of all \(Y_n\). More precisely, restriction across a nilpotent thickening is an equivalence, including on morphisms [Stacks, [Tag 0BQB](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-lemma-thickening)]. The full construction, including finiteness of every lift, is Infinitesimal lifting and invariance under thickenings, Theorem 6.2. Its square-Jacobian presentation gives the finite algebra lift, and its morphism-lifting theorem gives unique overlap maps and their cocycles.

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
It is an isomorphism exactly when \(\operatorname{Spec}_XB\to X\) is étale [Stacks, [Tag 0BJF](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/discriminant.html#discriminant-lemma-discriminant)].

To verify this criterion, pass to a geometric fibre. A nilpotent element \(a\) of a finite-dimensional commutative algebra pairs to zero with every \(b\), because multiplication by \(ab\) is nilpotent and has trace zero. A perfect trace form therefore forces the algebra to be reduced; over an algebraically closed field it is a product of copies of that field. Conversely this product has the perfect coordinatewise pairing. The finite flat fibre criterion in the earlier Étale morphisms lesson now gives étaleness. Invertibility of \(q\) is detected on these fibres by its determinant. Thus the trace criterion holds over the original base.

Each completed level is étale, so \(q^\wedge\) has an inverse. Fullness lifts that inverse to \(B^\vee\to B\), and faithfulness makes its two composites the identity. Hence \(q\) is an isomorphism on all of \(X\).

For neighbourhood germs, lift the maps after shrinking to one common neighbourhood. Each of the finitely many algebra equations holds after further shrinking, by faithfulness in the germ category. The trace pairing is already invertible on \(Y\); its noninvertibility locus is closed in the neighbourhood and disjoint from \(Y\). Remove that locus. This produces a finite étale cover on an ordinary neighbourhood. Uniqueness of maps is likewise uniqueness after shrinking. ∎

These arguments prove [Stacks, [Tag 0EL8](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-lemma-restriction-fully-faithful), [Tag 0EL9](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-lemma-restriction-equivalence), [Tag 0ELA](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-lemma-restriction-fully-faithful-general), [Tag 0EK1](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-lemma-restriction-equivalence-general)]. No principal ideal was assumed: the formal algebra at level \(n\) is locally \((\mathcal O_X/\mathcal I^n)^r\).

The previous lesson's section tests therefore give the following useful criteria. Full faithfulness follows if \(X\) is quasi-affine and
\(\Gamma(X,\mathcal O_X)\to\varprojlim\Gamma(Y_n,\mathcal O_{Y_n})\) is an isomorphism; or if \(X\) has an ample \(L\) and the corresponding comparison holds for every sufficiently high \(L^m\); or if it holds for every vector bundle. The same tests with colimits of neighbourhood sections prove full faithfulness for neighbourhood covers. The two locally split presentations in that lesson reduce general bundles to ample powers, so the tests require no cohomology vanishing for every bundle separately. This gives [Stacks, [Tag 0EJZ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-lemma-restriction-fully-faithful-special), [Tag 0EK0](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-lemma-restriction-fully-faithful-general-special)].

We will also use the finite étale **internal Hom**. For covers \(T,T'\) of \(X\), there is a finite étale \(X\)-scheme \(\underline{\operatorname{Hom}}_X(T,T')\) whose sections after any base change are maps from \(T\) to \(T'\). Étale locally the covers are constant finite sets \(S,S'\), and this Hom is the constant set of functions \(S\to S'\). The descriptions glue by faithfully flat descent, including their representing property. Thus lifting arbitrary maps of covers reduces to lifting sections of one cover [Stacks, [Tag 04HN](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale.html#etale-lemma-finite-etale-etale-local), [Tag 0BL7](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-lemma-internal-hom-finite-etale)].

## 3. The local Lefschetz theorem

We use (1.1). Here \(f\) is arbitrary; it need not be a nonzerodivisor. A henselian pair \((A,(f))\) has the idempotent-lifting property: for every finite \(A\)-algebra \(B\), idempotents of \(B/fB\) lift uniquely to \(B\). A henselian local ring has this property for every ideal in its maximal ideal. The idempotent statement for finite algebras over a henselian pair is proved in Étale neighbourhoods, henselization and quasi-finite morphisms, Lemma 5.3; its Theorem 5.6 proves the corresponding finite étale equivalence.

**Finite formal gluing.** Let \((A,\mathfrak m)\) be Noetherian local, let \(S=\widehat A\) be its maximal-ideal completion, and put \(U=\operatorname{Spec}A\setminus\{\mathfrak m\}\). A coherent module on \(U\) and a finite \(S\)-module, identified on \(U_S\), are the restrictions of a finite \(A\)-module. Maps with compatible restrictions glue uniquely. This also holds for finite algebras.

**Proof.** We first construct the module. Write \(F\) for the coherent module on \(U\), and \(C\) for the finite \(S\)-module. The coherent-extension construction in Formal geometry, Section 8, chooses a finite submodule
\(M_0\subset\Gamma(U,F)\) whose restriction is \(F\). A finite distinguished affine cover and flatness give
\[
\Gamma(U,F)\otimes_A S=\Gamma(U_S,F_S).
\]
Thus \((M_0)_S\) is a finite submodule of the group on the right.

The kernel \(T\) of \(C\to\Gamma(U_S,\widetilde C)\) is its maximal-ideal torsion. It is finite and is killed by some power of \(\mathfrak m\), hence has finite length. Put \(C_1=C/T\), regarded as another finite submodule of \(\Gamma(U_S,F_S)\). Its intersection with \((M_0)_S\) is finite. The two quotients by that intersection are supported at the closed point, since the modules agree on \(U_S\). They therefore have finite length. Consequently, for some \(a\),
\[
(\mathfrak m^aM_0)_S\subset C_1,
\qquad Q=C_1/(\mathfrak m^aM_0)_S
\quad\text{has finite length}.
\]
Set \(L=\mathfrak m^aM_0\). Both \(Q\) and \(T\) are ordinary finite-length \(A\)-modules: the actions factor through \(S/\mathfrak m^bS=A/\mathfrak m^b\).

The extension \(0\to L_S\to C_1\to Q\to0\) descends to \(A\). Indeed a resolution by free modules of finite rank, flat base change and the fact that a power of \(\mathfrak m\) kills \(Q\) give
\[
\operatorname{Ext}^1_S(Q,L_S)
=\operatorname{Ext}^1_A(Q,L)\otimes_A S
=\operatorname{Ext}^1_A(Q,L).
\]
The last equality holds because this finite Ext module is killed by the same power of \(\mathfrak m\). Choose its extension \(0\to L\to M_1\to Q\to0\). Its completion is the prescribed extension, and on \(U\) its first map identifies \(M_1\) with \(F\), compatibly with the given identification after completion. The remaining extension \(0\to T\to C\to(M_1)_S\to0\) descends too, since
\[
\operatorname{Ext}^1_S((M_1)_S,T)
=\operatorname{Ext}^1_A(M_1,T).
\]
It produces a finite module \(M\) with the required restrictions and their specified overlap identification.

Here is the assertion about maps. For finite \(A\)-modules \(M,N\), suppose a map \(\phi_U\) on \(U\) and a map \(\phi_S:M_S\to N_S\) agree on \(U_S\). The support sequence
\[
0\to T_N\to N\to\Gamma(U,\widetilde N)
\to H^1_{\mathfrak m}(N)\to0
\]
has \(T_N\) finite length and its last term maximal-ideal torsion. Tensor product with \(S\) is the identity on any maximal-ideal torsion module: this follows first for a module killed by \(\mathfrak m^b\), and then by its filtered union. Flat base change identifies the third term after tensoring with the sections on \(U_S\). Hence the obstruction for the map \(M\to\Gamma(U,\widetilde N)\) to take values in \(N/T_N\) is zero, since \(\phi_S\) lifts it after completion.

Pulling back \(0\to T_N\to N\to N/T_N\to0\) gives an extension of \(M\) by \(T_N\). Its class is zero after completion. The equality of the two Ext groups just used makes it zero over \(A\), so choose a lift \(M\to N\). Its completed difference from \(\phi_S\) has image in \(T_N\). The analogous equality for Hom descends this difference, and subtracting it gives a lift with exactly the prescribed completion. Such a lift is unique by faithful flatness of \(S/A\).

Finally apply this map assertion to multiplication and the unit. Tensor products of the constructed finite modules have the corresponding tensor-product restrictions. The algebra operations therefore descend, and their associativity, commutativity and unit identities hold because completion detects equality of maps. This proves the algebra statement, including [Stacks, Tag 0BLH](https://stacks.math.columbia.edu/tag/0BLH). ∎

**Finite extension across the missing point.** A finite cover of \(\widehat U\) admits a finite extension to \(\widehat X\), without a claim that this extension is étale at the closed point. Its composite to the affine Noetherian \(\widehat X\) is quasi-finite and separated. Zariski's Main Theorem, Theorem 4.2, factors it as an open immersion into a finite scheme [Stacks, [Tag 05K0](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-morphisms.html#more-morphisms-lemma-quasi-finite-separated-pass-through-finite)]. Replace that finite scheme by the scheme-theoretic closure of the given open. Over \(\widehat U\) the original open is also closed, because it is finite there; density of the closure therefore makes its restriction exactly the given cover.

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

These are [Stacks, [Tag 0BLP](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-lemma-fully-faithful-general), [Tag 0BLV](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-lemma-essentially-surjective-general)]. The formal-module input is the principal formal-bundle theorem in Formal geometry, equation (8.3) and its proof.

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

### Dualizing depth bounds on a punctured spectrum

In the rest of this section \(f\) may be a zero divisor. We continue to use (1.1). A point outside \(V(f)\) will be called relevant if its closure meets \(U_0\); equivalently
\(V(\mathfrak p)\cap V(f)\ne\{\mathfrak m\}\).

**Lemma 4.4 (the component bounds).** Suppose \(A\) has a dualizing complex, \(A_f\) is \((S_2)\), and every component not contained in \(V(f)\) has dimension at least \(a\). For \(a=3\),
\[
\operatorname{depth}A_{\mathfrak p}+\dim(A/\mathfrak p)>2
\qquad(f\notin\mathfrak p).
\tag{4.4}
\]
For \(a=4\), the sum is greater than three at every relevant prime outside \(V(f)\).

**Proof.** The ring is catenary by Local duality and finiteness, Lemma 6.16. Write \(e=\dim A_{\mathfrak p}\), \(b=\dim A/\mathfrak p\), and choose a minimal prime \(q\subset\mathfrak p\). It does not contain \(f\). The chain formula gives
\[
e+b\ge\operatorname{ht}(\mathfrak p/q)+b
=\dim A/q\ge a.
\]
The \((S_2)\) condition gives depth at least \(\min(2,e)\). If \(e\le1\), the desired sum is at least \(a\). If \(e\ge2\), its sum is at least \(2+b\). Here \(b\ge1\), since \(\mathfrak p\ne\mathfrak m\), proving (4.4). For a relevant prime, there is \(\mathfrak p\subsetneq q'\subsetneq\mathfrak m\) with \(f\in q'\), so \(b\ge2\). This gives the second assertion. ∎

We next prove the principal formal-bundle existence assertion needed with these bounds. The proof keeps track of the obstruction to lifting sections; individual cohomology groups on the puncture need not be finite.

**Lemma 4.5 (finite dual obstruction modules).** Let \(A\) be \(f\)-adically complete with a dualizing complex, and assume
\[
\operatorname{depth}A_{\mathfrak p}+\dim A/\mathfrak p>3
\quad\text{at every relevant }\mathfrak p\notin V(f).
\tag{4.5}
\]
Let \((E_n)\) be a coherent formal system on \(U\), regular for \(f\), whose completed modules are finite locally free outside \(V(f)\). Choose finite modules \(M_n\), killed by \(f^n\), with \(\widetilde M_n|_U=E_n\), compatible transitions and \(H^0_{\mathfrak m}(M_n)=0\). For \(i=1,2\), there are a finite module \(P_i\), killed by a power of \(f\), and compatible maps, for all sufficiently large \(n\),
\[
H^i_{\mathfrak m}(M_n)\longrightarrow
D(P_i),\qquad D(-)=\operatorname{Hom}_A(-,E_A(k)),
\tag{4.6}
\]
such that the kernel systems have finite-length transition images sufficiently far apart. The maps in (4.6) factor through one fixed finite level of the cohomology system.

**Proof.** Such \(M_n\) can always be chosen. Extend each \(E_n\) by a finite submodule of its sections, as in Formal geometry, Section 8. Choose these submodules inductively: replace a proposed \(M_{n+1}\) by the inverse image of \(M_n\) under its section map to \(E_n\). This is finite and still restricts to \(E_{n+1}\). Being a submodule of sections on \(U\), it has no maximal-ideal torsion.

Normalize the dualizing complex \(\omega\) so that its dimension function is \(\delta(\mathfrak p)=\dim A/\mathfrak p\), and put
\(L_n^i=\operatorname{Ext}^{-i}_A(M_n,\omega)\).
These are finite modules with forward transitions. We show that, on \(U\), their forward systems are constant up to systems whose sufficiently long transitions vanish.

Choose generators \(g_j\) of \(\mathfrak m\). On \(D(g_j)\), put \(B=\widehat{A_{g_j}}^{\,(f)}\) and let \(N\) be the finite completed module of the formal system. Then \((M_n)_{g_j}=N/f^nN\). Flat Hom base change identifies
\[
(L_n^i)_{g_j}
=\operatorname{Ext}^{-i}_B(N/f^nN,\omega\otimes_A B).
\tag{4.7}
\]
Indeed the modules on the left are killed by \(f^n\), and \(B/f^nB=A_{g_j}/f^nA_{g_j}\).

At a prime \(Q\supset fB\), its contraction \(q\) is in \(U_0\). Proposition 6.18 of Local duality and finiteness and the residue-field normalization at \(Q\) give, for \(P\subset Q\) and \(p=P\cap A\),
\[
\operatorname{depth}B_P+\delta_B(P)
=\operatorname{depth}A_p+\delta(p).
\tag{4.8}
\]
Here \(\delta_B(Q)=\delta(q)\), and the interval from \(P\) to \(Q\) supplies the remaining difference of dimension functions. Every maximal ideal of \(B\) contains \(f\), so every prime is below such a \(Q\). If \(f\notin P\), then \(p\) is relevant. The module \(N_P\) is free, or zero, and (4.5) therefore makes its depth plus \(\delta_B(P)\) greater than three.

Apply the depth formula for coherent dual Ext from Local duality and finiteness, Lemma 6.10.1, to
\(L=R\operatorname{Hom}_B(N,\omega\otimes_A B)\).
The three finite modules \(H^{-1}(L),H^{-2}(L),H^{-3}(L)\) vanish outside \(V(f)\). One power \(f^c\) kills all three. Since \(f\) is regular on \(N\), the multiplication triangle gives exact sequences
\[
0\to H^{-i-1}(L)/f^nH^{-i-1}(L)
\to \operatorname{Ext}^{-i}_B(N/f^nN,\omega\otimes B)
\to H^{-i}(L)[f^n]\to0.
\tag{4.9}
\]
Their forward transitions multiply the left term by \(f\) and include the right term. For \(n\ge c\), the right term is the fixed module \(H^{-i}(L)\); a transition of length at least \(c\) kills the left term. Its image is consequently a copy of that fixed module. Later cokernel systems have zero transitions after a further length \(c\).

There are finitely many charts. Choose common indices \(n_0<n_1\), far enough apart, and set
\[
P_i=\operatorname{im}(L_{n_0}^i\to L_{n_1}^i).
\]
On every chart this is the constant image just described. Thus, for \(n\ge n_1\), the maps \(P_i\to L_n^i\) have kernels supported at \(\mathfrak m\), and the forward cokernel systems have transition images supported there sufficiently far apart. All modules involved are finite, so those kernels and transition images have finite length. Also \(f^{n_0}P_i=0\).

Local duality identifies \(H^i_{\mathfrak m}(M_n)\) naturally with \(D(L_n^i)\). This identity holds without maximal-adic completeness of \(A\): the completed finite Ext module has the same Hom into \(E_A(k)\), and Matlis biduality recovers the Artinian local-cohomology module. Exactness of \(D\) now turns the preceding maps into (4.6), with the asserted finite-length transition images in their kernels. Since \(P_i\) is a submodule of \(L_{n_1}^i\), the maps factor through \(H^i_{\mathfrak m}(M_{n_1})\). ∎

**Proposition 4.6 (principal formal bundles on a puncture).** Under (4.5), every finite locally free formal system along \(f\) on \(U\) is the completion of a coherent module on \(U\), locally free on a neighbourhood of \(U_0\).

**Proof.** First consider a regular system \((E_n)\) as in Lemma 4.5. Set
\[
M=\varprojlim H^0(U,E_n),\qquad
O=\varprojlim H^1(U,E_n).
\]
The multiplication-sequence argument proving (5.2) in Formal geometry, Lemma 5.1, applies before any finiteness assertion. It says that the two limit topologies are their \(f\)-adic topologies. They are separated and complete. Multiplication by \(f\) is injective on \(M\): a compatible section killed by \(f\) is zero at each level after comparison with the next level.

By the support sequence, \(H^1(U,E_n)=H^2_{\mathfrak m}(M_n)\). Lemma 4.5 gives a map \(O\to D(P_2)\), factoring through one level. Let \(K\) be its kernel. It is the limit of the kernel system in (4.6). Its limit topology is also \(f\)-adic: if \(f^cP_2=0\), then
\(f^cO\subset K\subset O\), and
\[
f^nK\subset K\cap f^nO\subset f^{n-c}K
\qquad(n\ge c).
\]
It is closed in \(O\), since its defining map factors through one discrete level. Hence \(K\) is separated and complete. At any fixed sufficiently late level, its image lies in a finite-length transition image from a later kernel. For an index whose projection kernel is contained in \(fK\), this makes \(K/fK\) finite. Topological Nakayama, proved by successive approximation in Formal geometry, Lemma 5.1, makes \(K\) a finite \(A\)-module.

The same control in degree one makes \(M\) finite. The exact sequences are
\[
0\to M_n\to H^0(U,E_n)\to H^1_{\mathfrak m}(M_n)\to0.
\]
Choose \(c\) with \(f^cP_1=0\). A compatible section, multiplied by \(f^c\), has its boundary in the kernel at every level. Its boundary at level \(n\) therefore lies in the image of a sufficiently late kernel, a finite-length module by Lemma 4.5. Its part in \(M_n\) is finite too. Consequently the image of \(f^cM\) in \(H^0(U,E_n)\) is finite. Since the projection kernel on \(M\) is \(f^nM\), regularity of \(f\) identifies this image, for \(n\ge c\), with \(M/f^{n-c}M\). In particular \(M/fM\) is finite, and successive approximation makes \(M\) finite.

We must still prove uniform lifting of sections. Let
\(\partial_n:H^0(U,E_n)\to O\)
be the compatible boundary for
\(0\to E_a\xrightarrow{f^n}E_{a+n}\to E_n\to0\), taking the limit over \(a\). A zero boundary means that the section lifts to every finite higher level. Naturality gives
\(\partial_{n+1}(fs)=\partial_n(s)\).
Choose \(b\) such that the map \(O\to D(P_2)\) factors through \(H^1(U,E_b)\), and put
\[
S_n=\operatorname{im}\bigl(H^0(U,E_{n+b})\to H^0(U,E_n)\bigr).
\]
For \(s\in S_n\), its boundary at level \(b\) is zero, so \(\partial_n(s)\in K\). Thus
\[
\bigoplus_{n\ge1}\operatorname{im}(S_n\xrightarrow{\partial_n}K)
\]
is a graded submodule of \(K[T]\), where \(T\) acts as the identity on coefficients while raising the degree. It is finite over \(A[T]\), since \(K\) is finite and \(A[T]\) Noetherian. Choose homogeneous generators represented by \(s_j\in S_{n_j}\), and set \(a=\max n_j\). If \(n\ge a\) and \(s\in S_n\), subtract a linear combination of \(f^{n-n_j}s_j\) with the same boundary. The remainder lifts to every higher level, and the subtracted terms vanish at level \(n-a\). To obtain a lift in \(S_{n'}\), lift it first to level \(n'+b\) and then reduce to level \(n'\). Hence the image of \(S_n\) at level \(n-a\) is the image of every later \(S_{n'}\). This is the Mittag–Leffler property. The systems \((S_n)\) and \((H^0(U,E_n))\) are pro-isomorphic, by their definition, so both have it.

The limit consequently surjects onto each stable image. Together with the projection kernel \(f^nM\), this identifies the section system with \((M/f^nM)\) as pro-systems. Sheafifying on the quasi-affine open \(U\) recovers \((E_n)\); Formal geometry, Proposition 1.3, turns this pro-isomorphism into an isomorphism of coherent formal objects. This algebraizes every regular system in the lemma.

For the original finite locally free formal system, its completed modules on a finite affine cover are finite. Their \(f\)-power torsion is killed by one common power. Quotienting it out gives a regular system, unchanged outside \(V(f)\), so the preceding proof applies. Restore the bounded torsion kernel by Formal geometry, Lemma 6.2. Its Ext comparison applies on \(U\) as well: a finite distinguished affine cover computes the global Ext groups, and on each chart the finite-free Hom complexes with a target killed by \(f^c\) are unchanged by completion. Therefore the required extension class is an ordinary coherent extension. No regularity of \(f\) on \(A\) is used.

We obtain a coherent \(F\) on \(U\) with the original completion. At \(y\in U_0\), its completed stalk is free: lift a basis at the first formal level and use Nakayama at every subsequent level. The local \(f\)-adic completion is faithfully flat, so a finite presentation descends that freeness to \(F_y\). The open free locus of \(F\) contains \(U_0\). Restriction to it gives the desired bundle. ∎

**Theorem 4.7 (four dualizing-complex variants).** Use (1.1), allowing arbitrary \(f\in\mathfrak m\).

1. If \(A\) has a dualizing complex, is \(f\)-adically complete, and every irreducible component of \(X\) not contained in \(X_0\) has dimension at least three, (4.2) is fully faithful [Stacks, Tag 0DXX](https://stacks.math.columbia.edu/tag/0DXX).
2. If \(A\) has a dualizing complex and is \(f\)-adically complete, (4.2) is an equivalence under either of these conditions: \(A_f\) is \((S_2)\) and every component not contained in \(X_0\) has dimension at least four; or (4.5) holds at every relevant prime outside \(V(f)\) [Stacks, Tag 0DXY](https://stacks.math.columbia.edu/tag/0DXY).
3. If \(A\) has a dualizing complex and \((A,(f))\) is henselian, restriction \(\operatorname{FEt}(U)\to\operatorname{FEt}(U_0)\) is fully faithful under either of these conditions: \(A_f\) is \((S_2)\) and every component not contained in \(X_0\) has dimension at least three; or (4.4) holds at every prime outside \(V(f)\) [Stacks, Tag 0EK5](https://stacks.math.columbia.edu/tag/0EK5).
4. Add purity at every maximal localization of \(A_f\) to the hypotheses of item 2. Then restriction on all of \(U\) is essentially surjective [Stacks, Tag 0EK9](https://stacks.math.columbia.edu/tag/0EK9). This assertion alone gives no full-faithfulness conclusion.

**Proof of item 1.** Replace \(A\) by \(A_{\mathrm{red}}\). Its nilradical is nilpotent, and finite étale invariance under thickenings, including every morphism, is proved in Infinitesimal lifting and invariance under thickenings, Theorem 6.2. The two spectra have the same open neighbourhoods, so this replacement respects the colimit category as well as \(\operatorname{FEt}(U_0)\). The quotient is \(f\)-adically complete by exactness of completion on finite modules and has a dualizing complex by quotient duality. Its component dimensions are unchanged.

In a reduced Noetherian ring the associated primes are minimal: zero is the intersection of its finitely many minimal primes, giving an embedding into the direct sum of the corresponding domain quotients; associated primes of a submodule are among those of the ambient module. A vector bundle has the same associated points as the structure sheaf wherever its rank is nonzero. Thus every relevant associated point \(p\) of such a bundle outside \(V(f)\) has \(\dim A/p\ge3\). The principal Čech complex gives \(\operatorname{cd}(A,(f))\le1\). The coherent Hom criterion of Formal geometry, Theorem 8.5, with \(I=(f)\) and \(\mathfrak a=\mathfrak m\), therefore applies: its required bound is \(\dim A/p>\operatorname{cd}(A,(f))+1\), at most two. It proves full faithfulness for neighbourhood bundles. Proposition 2.1 transfers this to finite étale covers, proving item 1.

**Proof of item 2.** Lemma 4.4 reduces its first alternative to (4.5). For an associated point \(p\) of a vector bundle, depth is zero; hence (4.5) implies \(\dim A/p>3\) at every relevant associated point outside \(V(f)\). Theorem 8.5 of Formal geometry again gives full faithfulness for neighbourhood bundles. Proposition 4.6 gives essential surjectivity for these bundles, retaining the relevant-prime qualification and allowing zero divisors in \(f\).

Lift a prescribed finite étale cover of \(U_0\) through its nilpotent thickenings by the preceding finite étale invariance theorem. Proposition 4.6 algebraizes the resulting formal bundle on some neighbourhood. Its multiplication and unit lift by full faithfulness; their finitely many equations hold after a common shrinking. The trace-pairing argument in Proposition 2.1 makes the algebra étale after another shrinking. This proves essential surjectivity for covers; the same proposition gives full faithfulness, so (4.2) is an equivalence.

**Proof of item 3.** Lemma 4.4 reduces the component alternative to (4.4), imposed here at every prime outside \(V(f)\), not only the relevant ones. Let \(S=\widehat A^{\,\mathfrak m}\). Lemma 6.16 of Local duality and finiteness carries a dualizing complex to \(S\). Its Proposition 6.18, with completion ideal \(\mathfrak m\) and upper prime \(\mathfrak mS\), gives
\[
\operatorname{depth}S_P+\dim S/P
=\operatorname{depth}A_p+\dim A/p>2
\qquad(f\notin P,\ p=P\cap A).
\tag{4.10}
\]
Apply the annihilator theorem, Theorem 6.1 of that lesson, with support \(\{\mathfrak mS\}\), allowed annihilator locus \(V(f)\), and degrees through two. Condition (4.10) is exactly its prime-pair test. Its annihilator ideal has zero set inside \(V(f)\), so it contains a power of \(f\). This power kills \(H^1_{\mathfrak mS}(S)\) and \(H^2_{\mathfrak mS}(S)\).

The complete local ring \(S\) is also \(f\)-adically complete, as proved in Theorem 3.2. Formal geometry, Lemma 3.2, consequently identifies ordinary sections of \(\mathcal O_{U_S}\) with their formal sections. The quasi-affine bundle test and Proposition 2.1 give full faithfulness for covers of \(U_S\). Lemma 3.1 descends this conclusion to \(U\), using precisely the henselian-pair hypothesis. This proves item 3 without requiring \(A\) to be complete or \(f\) to be regular.

**Proof of item 4.** Item 2 gives the cover on some neighbourhood \(V\) of \(U_0\). Its omitted closed set in \(U\) is a finite set of points maximal in \(\operatorname{Spec}A_f\), by the dimension-one argument in Proposition 4.3; that argument uses only that \(V\) contains \(U_0\). At each point, purity extends the restricted cover from the punctured local spectrum to the whole local spectrum. The finite-presentation gluing argument in Proposition 4.3 spreads the local finite étale algebra and its overlap isomorphism to a neighbourhood and attaches that point. Repeating finitely many times gives a cover of all of \(U\) with the prescribed restriction. This proves essential surjectivity, as asserted. ∎

The thresholds three and four enter different steps. In item 1, reduction makes associated primes minimal and only their dimensions matter. Existence in item 2 instead requires control of both dual obstruction modules in Lemma 4.5. Item 3 imposes its depth inequality even at the nonrelevant primes because it controls sections on all of \(U\). Item 4 uses purity to fill the finitely many points left by neighbourhood algebraization.

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

**Lemma (Euler characteristics of an unramified cover).** Let \(h:C\to D\) be a finite étale morphism of degree \(r\) between smooth projective connected curves over an algebraically closed field. In every characteristic,
\[
1-g(C)=r(1-g(D)),
\qquad 2g(C)-2=r(2g(D)-2).
\tag{6.1}
\]
Here \(g(B)=\dim_kH^1(B,\mathcal O_B)\). This is the unramified case of Riemann–Hurwitz.

**Proof.** We recall the required degree and Euler-characteristic calculation. A line bundle on a smooth integral curve has a nonzero rational section. Its zeros and poles form a finite divisor. For a closed point \(p\), the quotient of \(L(p)\) by \(L\) has length one, so its Euler characteristic differs by one. Iterating through the positive and negative parts of a divisor gives
\[
\chi(L)=\chi(\mathcal O_D)+\deg L.
\]
In particular a principal divisor has degree zero, since its line bundle is trivial. This also proves that degree is additive for tensor products and changes sign on duals.

For a rank-\(r\) vector bundle \(E\), choose a rational basis and an effective divisor \(B\) clearing all its poles. It gives an injective map \(\mathcal O_D(-B)^r\to E\) with torsion cokernel of finite length \(l\). At each point a matrix over the discrete valuation ring has determinant valuation equal to its cokernel length, by diagonalizing the matrix with elementary row and column operations. Thus
\(\deg(\det E)=l-r\deg B\), and the cohomology sequence gives
\[
\chi(E)=r\chi(\mathcal O_D)+\deg(\det E).
\tag{6.2}
\]
All these cohomology groups are finite by Proper morphisms and coherent direct images, Corollary 5.1. There is no cohomology above degree one: two affine complements of disjoint hyperplane sections cover the curve, and their affine intersection gives a Čech complex of length one. Such sections exist because the algebraically closed field is infinite. The same statements hold for a torsion sheaf, whose Euler characteristic is its length.

Apply (6.2) to \(E=h_*\mathcal O_C\). It is finite locally free. Its trace pairing identifies \(E\) with \(E^\vee\): after an étale splitting it is the pairing \((a,b)\mapsto\sum a_ib_i\) on \(\mathcal O_D^r\). Therefore \(2\deg(\det E)=0\), so this integer is zero. A finite morphism is affine, and the affine Čech calculation identifies \(H^i(D,E)\) with \(H^i(C,\mathcal O_C)\). Hence \(\chi(\mathcal O_C)=r\chi(\mathcal O_D)\).

Finally a connected smooth projective curve is integral: its regular irreducible components are disjoint, so connectedness leaves one. Its global function ring is a finite-dimensional domain over \(k\), by proper coherence, and therefore equals \(k\). Thus \(\chi(\mathcal O_C)=1-g(C)\), and likewise for \(D\). This proves both equalities. ∎

**Example 6.2 (projective space without using purity).** Over an algebraically closed field, a connected finite étale cover \(C\to\mathbb P^1\) is a smooth projective curve. The unramified Riemann–Hurwitz formula (6.1) gives
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

Finite étale invariance across every nil thickening, including finiteness and every map, is proved in Infinitesimal lifting and invariance under thickenings, Theorem 6.2. Étale-local splitting is Étale neighbourhoods, henselization and quasi-finite morphisms, Theorem 5.1. The finite flat fibre criterion for étaleness is proved in Étale morphisms and their local structure, Proposition 1.1 and Lemma 1.2. The étale fundamental-group lesson, Propositions 1.1–1.2, Theorem 1.3 and (2.2), proves the cover-category, internal Hom and fibre-functor identifications, using the module and affine descent proofs in Faithfully flat descent.

Section 3 proves finite completion gluing for the exact module and algebra data used in henselian descent. The finite factorization used to extend across the missing point is proved in the earlier Zariski's Main Theorem, Theorem 4.2. The local formal-module theorem in Theorem 4.2 is Formal geometry, Section 8, equation (8.3). For the four dualizing variants, Lemmas 4.4–4.5 and Proposition 4.6 prove the depth reduction, dual obstruction bounds and principal formal-bundle existence, including zero divisors. Theorem 4.7 then proves each of the four cover assertions. Local duality and finiteness supplies the actual annihilator theorem, local duality, dimension function and completion/depth comparison; Formal geometry supplies coherent Hom comparison, supported corrections and the regular-system limit argument.

The unramified Riemann–Hurwitz formula in every characteristic is proved in (6.1)–(6.2), by the divisor Euler-characteristic calculation and trace pairing. Proper coherent cohomology finiteness is Proper morphisms and coherent direct images, Corollary 5.1. The multiplication degree and étaleness theorem is Abelian varieties, Theorem 6.1: multiplication by an integer n has degree n to the power twice the dimension, and is étale when n is invertible in the field.

Purity for regular local rings and complete intersections is not invoked as a proved result here. It is an explicit hypothesis in the global isomorphism and extension theorems, and the smooth and complete-intersection applications requiring it are correspondingly conditional. This order preserves the local Lefschetz theorem as an input to the later proof of purity.

## References

- [Stacks] The Stacks Project authors, *The Stacks Project*, [official project](https://stacks.math.columbia.edu/). The tag links refer to the AI Integrated Stacks Project edition. Its [English reader](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/) retains upstream tags. Relevant sections are Fundamental Groups of Schemes, “Local Lefschetz for the fundamental group,” “Finite étale covers of punctured spectra,” and “Lefschetz theorems”; Algebraic and Formal Geometry, “Completion functors”; and More on Algebra, “Formal glueing.”
- [Grothendieck–Laszlo] A. Grothendieck, *Cohomologie locale des faisceaux cohérents et théorèmes de Lefschetz locaux et globaux (SGA 2)*, revised edition edited by Y. Laszlo, [arXiv:math/0511279](https://arxiv.org/abs/math/0511279), Exposés X and XII, for local and global Lefschetz theorems.
