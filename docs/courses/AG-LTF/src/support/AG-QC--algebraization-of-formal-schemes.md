# Algebraization of formal schemes

*Written by GPT-6.1 Sol (OpenAI), in Codex, at Ultra effort, October 2026. Self-checked by the writing AI. Public domain (CC0).*

A compatible family of infinitesimal schemes need not arrive inside one ambient algebraic scheme. A compatible ample line bundle supplies that ambient space: sufficiently positive sections lift at every order and embed the entire system in a fixed projective space. Grothendieck existence then algebraizes its quotient structure sheaf.

We use Grothendieck existence, formal functions, and projective-space cohomology. Ampleness, its embedding criterion, and the equivalence between ampleness of an invertible sheaf and a positive tensor power belong to the planned *Ample invertible sheaves* lesson in *Morphisms of schemes*. We use the precise open nilpotent-thickening results [Stacks, Tags 09ZW and 0896]: finite type, properness and closed immersions can be checked on the reduced-base member of a cartesian finite-order thickening.

Throughout, \(A\) is Noetherian and complete for an ideal \(I\), \(S=\operatorname{Spec}A\), and \(S_n=\operatorname{Spec}(A/I^n)\). Such an ideal lies in the Jacobson radical. Indeed \(1-a\) has inverse \(\sum_{j\geq0}a^j\) for \(a\in I\), so no maximal ideal can omit \(I\).

## 1. Algebraizing closed subschemes

Let \(X\) be proper over \(S\), and write \(X_n=X\times_S S_n\). Suppose \(Z_n\hookrightarrow X_n\) are closed subschemes with compatible cartesian squares, meaning
\[
Z_n=Z_{n+1}\times_{X_{n+1}}X_n.
\]
Their quotient structure sheaves form a coherent formal module \(F_n=\mathcal O_{Z_n}\) on \(X\), with compatible quotient maps \(\mathcal O_{X_n}\twoheadrightarrow F_n\).

**Theorem 1.1.** There is a unique closed subscheme \(Z\hookrightarrow X\) whose base changes are the specified \(Z_n\), compatibly as subschemes of \(X_n\).

**Proof.** Grothendieck existence gives a coherent \(F\) with \(\widehat F=(F_n)\). Full faithfulness algebraizes the formal quotient map to \(q:\mathcal O_X\to F\). Its coherent cokernel has zero completion, by exactness. Faithfulness of completion makes that cokernel zero: its identity has zero image, hence is zero. Thus \(q\) is surjective, and its kernel \(K\) is a coherent ideal. Set \(Z=V(K)\); reducing the quotient modulo \(I^n\) gives exactly the prescribed quotient algebra on \(X_n\).

For uniqueness, the quotient modules of two algebraizations have a specified formal isomorphism respecting the quotient maps. Full faithfulness gives a unique algebraic isomorphism respecting those maps, because their difference has zero completion. Their kernels are therefore the same ideal. This proves uniqueness as an embedded closed subscheme. \(\square\)

The kernels of the separate quotients \(\mathcal O_{X_n}\to F_n\) need not themselves satisfy the quotient compatibility for a coherent formal module. The argument uses the quotient systems and the actual formal-category kernel, avoiding that mistake.

We also need the proper-support version. If \(W\) is separated of finite type over \(S\), the same conclusion holds for closed \(Z_n\subset W_n\) whose first member is proper over \(S_1\), and the resulting \(Z\) is proper over \(S\). This is [Stacks, Tag 0899]. Here is why the quotient construction still works. Existence with proper support algebraizes \(F_n\) to a coherent \(F\) with proper scheme-theoretic support. The formal units are compatible sections of \(F_n\). Formal functions on that proper support identifies them with a unique section of \(F\), giving \(\mathcal O_W\to F\). Its cokernel has proper support and zero completion, so vanishes. Uniqueness is proved on the proper closed union of two candidate supports, using full faithfulness there. The quotient defines the required proper closed subscheme.

## 2. Finite schemes and morphisms

**Proposition 2.1.** Suppose \(X\) is proper over \(S\), and \(Y_n\to X_n\) are compatible finite morphisms with cartesian squares. They algebraize to a finite morphism \(Y\to X\), with \(Y\) proper over \(S\).

**Proof.** The finite algebras \(B_n=(Y_n\to X_n)_*\mathcal O_{Y_n}\) are a coherent formal module: affine base change identifies their quotient transitions. Algebraize its underlying module to \(B\). The formal multiplications algebraize to \(B\otimes B\to B\), since completion commutes with tensor products of finite modules. The unit algebraizes to \(\mathcal O_X\to B\). Associativity, commutativity and the unit equations are equalities of coherent-module maps; full faithfulness lifts them from every formal level. Thus \(B\) is a coherent algebra. Take \(Y=\underline{\operatorname{Spec}}_X B\). It is finite over \(X\), hence proper over \(S\), and its base changes recover the finite algebras \(B_n\) and the schemes \(Y_n\). \(\square\)

The same argument works when \(X\) is only separated of finite type and \(Y_1\) is proper over \(S_1\), using proper-support existence. The algebraized algebra is supported on a proper closed subscheme, and its finite relative Spec is proper. This is the exact generality of [Stacks, Tag 09ZT].

**Theorem 2.2 (algebraization of morphisms).** If \(X\) is proper and \(Y\) is separated of finite type over \(S\), any compatible system \(g_n:X_n\to Y_n\) comes from a unique \(S\)-morphism \(g:X\to Y\).

**Proof.** Separatedness makes the graphs \(\Gamma_n\subset X_n\times_{S_n}Y_n\) closed. They form a cartesian system with proper first member. The proper-support closed-subscheme result gives a proper \(Z\subset X\times_S Y\) algebraizing these graphs. Its projection \(p:Z\to X\) is proper, by the closed-graph factorization, and is an isomorphism modulo every \(I^n\).

The fibers of \(p\) over \(X_1\) have one point. A proper morphism over a Noetherian scheme is finite on a neighborhood of any finite fiber [Stacks, Tag 02OH]; its proof uses the open quasi-finite locus and the finiteness theorem from formal functions. Thus \(p\) is finite over an open neighborhood \(U\) of \(X_1\). The closed complement \(X\setminus U\) has closed image in \(S\), because \(X\) is proper. This image misses \(V(I)\). Every nonempty closed subset of \(S\) meets \(V(I)\), since \(I\) lies in the Jacobson radical. The complement is therefore empty, so \(p\) is finite everywhere.

Finite pushforward commutes with all base changes, by the affine algebra description. Hence the unit \(\mathcal O_X\to p_*\mathcal O_Z\) is an isomorphism on every formal level. Full faithfulness for proper \(X\) makes it an isomorphism algebraically. A finite map is recovered from its algebra, so \(p\) is an isomorphism. Its inverse followed by the other projection defines \(g\). Any other algebraization has a proper closed graph with the same formal graph system; uniqueness of the proper-support closed-subscheme result identifies the graphs and the morphisms. \(\square\)

This proves morphism recovery with the target hypotheses of [Stacks, Tag 0A42]; the target need not be proper.

## 3. An abstract polarized system

Now suppose schemes \(T_n\to S_n\) and transition morphisms are given with cartesian squares, so
\[
T_n=T_{n+1}\times_{S_{n+1}}S_n.
\]
They share one underlying topological space, since \(I\) is nilpotent on each finite level. Assume that \(T_1\to S_1\) is proper and that there are invertible sheaves \(L_n\) with specified compatible isomorphisms
\[
L_{n+1}|_{T_n}\cong L_n,
\qquad L_1\text{ ample on }T_1.
\]
The nilpotent-thickening criterion makes all \(T_n\) proper and of finite type over their Noetherian bases. No flatness is assumed in this section.

**Lemma 3.1 (uniform section lifting).** There is an integer \(d_0\) such that, for \(d\geq d_0\),
\[
\Gamma(T_{n+1},L_{n+1}^d)\longrightarrow\Gamma(T_n,L_n^d)
\]
is onto for every \(n\geq1\).

**Proof.** On the common space set \(D_0=\mathcal O_{T_1}\) and
\[
D_n=\ker(\mathcal O_{T_{n+1}}\to\mathcal O_{T_n})
=I^n\mathcal O_{T_{n+1}}\quad(n\geq1).
\]
Each is annihilated by \(I\), so is coherent on \(T_1\). Computing at a level larger than the indices defines products \(D_a\otimes D_b\to D_{a+b}\). They are independent of that level, by the cartesian quotient identities. With \(B=\bigoplus I^n/I^{n+1}\), multiplication gives a graded surjection
\[
\mathcal O_{T_1}\otimes_{A/I}B\twoheadrightarrow D=\bigoplus D_n.
\]
The ring \(B\) is Noetherian and finitely generated. On the proper scheme \(T_1\times_{A/I}\operatorname{Spec}B\), the graded module \(D\) corresponds under affine pushforward to a coherent sheaf \(E\). Pullback of \(L_1\) is relatively ample. Serre vanishing for \(E\), followed by affine pushforward and direct-sum cohomology, supplies one bound for
\(H^1(T_1,D_n\otimes L_1^d)=0\), simultaneously in \(n\). The exact sequences
\[
0\to D_n\otimes L_1^d\to L_{n+1}^d\to L_n^d\to0
\]
then give the asserted surjectivity. \(\square\)

The argument uses only a surjection of graded algebras, so survives nonflatness. It is the same uniform-vanishing mechanism that algebraized formal modules in the preceding lesson.

## 4. Grothendieck's algebraization theorem

**Theorem 4.1.** The polarized system of Section 3 comes from a projective scheme \(T\to S\) and an ample invertible \(L\), with compatible identifications
\[
T_n\cong T\times_S S_n,
\qquad L_n\cong L|_{T_n}.
\]

**Proof.** Choose \(d\) large enough for Lemma 3.1 and for a finite set of sections of \(L_1^d\) to give a closed immersion
\(T_1\hookrightarrow\mathbf P^N_{A/I}\). The ample embedding criterion gives an immersion for a sufficiently large power, and properness makes it closed. Lift those sections recursively using Lemma 3.1. At each level they generate \(L_n^d\), because their cokernel reduces to zero modulo the nilpotent ideal \(I\), and Nakayama applies. They define compatible maps
\[
\psi_n:T_n\longrightarrow\mathbf P^N_{A/I^n}.
\]
Their reductions are \(\psi_1\), a closed immersion. The nilpotent closed-immersion criterion [Stacks, Tag 0896] makes every \(\psi_n\) a closed immersion. The squares are cartesian because the original systems and the projective spaces both have the specified base changes.

Apply Theorem 1.1 in \(\mathbf P^N_A\). It gives a closed subscheme \(T\), hence a projective scheme, with precisely the desired reductions. The coherent formal module \((L_n)\) on \(T\) algebraizes by Grothendieck existence to a coherent \(L\). The inverse line bundles \((L_n^{-1})\) also algebraize to \(G\). Their formal evaluation isomorphism algebraizes, with its inverse, to
\(L\otimes G\cong\mathcal O_T\). This makes \(L\) invertible. Locally its tensor inverse forces both finite modules to have one generator modulo the maximal ideal; writing them as quotients of the local ring shows their defining ideals must both be zero.

The embedding constructed from the lifted sections identifies \(L_n^d\) with \(\mathcal O_T(1)|_{T_n}\). Full faithfulness identifies \(L^d\) with \(\mathcal O_T(1)\). This is ample; ampleness of a positive power implies ampleness of \(L\). Thus the theorem recovers the given polarization itself, not just its embedding power. \(\square\)

This is the full form of [Stacks, Tag 089A]. Its projective conclusion follows here from an actual closed immersion into a fixed finite projective space. Different compatible choices of sections produce the same algebraized system up to a unique isomorphism inducing the prescribed identifications: Theorem 2.2 algebraizes the compatible isomorphisms and their inverses. Full faithfulness also identifies the polarizations.

## 5. Lifting line bundles and the role of flatness

For a square-zero thickening \(T\hookrightarrow T'\) with ideal \(J\), there is an exact sequence of abelian sheaves on their common space
\[
0\to J\xrightarrow{a\mapsto1+a}\mathcal O_{T'}^*
\to\mathcal O_T^*\to1.
\tag{2}
\]
The first map is additive because \(J^2=0\). A unit modulo \(J\) lifts locally to a unit: lift it and an inverse, whose product is \(1+a\), and multiply by \(1-a\). Hence the sequence is exact as a sequence of sheaves. Since \(\operatorname{Pic}(T)=H^1(T,\mathcal O_T^*)\), its long exact sequence gives
\[
H^1(T,J)\to\operatorname{Pic}(T')\to\operatorname{Pic}(T)
\xrightarrow{\partial}H^2(T,J).
\tag{3}
\]
Thus \(\partial(L)\) is the exact obstruction to lifting \(L\). When it vanishes, lift classes form a torsor under the quotient of \(H^1(T,J)\) by the image of the preceding unit boundary. This proves the square-zero lifting statement directly, including its correct obstruction group.

**Theorem 5.1 (the flat \(H^2\) criterion).** Let \((A,\mathfrak m,k)\) be complete Noetherian local. Suppose the cartesian system \(T_n\to\operatorname{Spec}(A/\mathfrak m^n)\) is flat at every level, \(T_1\) is projective over \(k\), and
\(H^2(T_1,\mathcal O_{T_1})=0\). Then it algebraizes to a projective flat scheme over \(A\).

**Proof.** The ideal of \(T_n\) in \(T_{n+1}\) is square-zero, since \(2n\geq n+1\). Flatness makes its ideal layer
\[
J_n\cong\mathcal O_{T_1}\otimes_k
(\mathfrak m^n/\mathfrak m^{n+1}).
\]
This follows by tensoring the defining ideal sequence of the base with the flat structure sheaf; the vector space on the right is finite-dimensional. Consequently \(H^2(T_n,J_n)=0\). Starting with an ample \(L_1\), sequence (3) constructs \(L_{n+1}\) with a chosen identification on \(T_n\), recursively. Theorem 4.1 algebraizes the resulting polarized system to projective \(T\).

At a point of the closed fiber, its Noetherian local algebra is flat over \(A\): all quotients modulo \(\mathfrak m^n\) are flat over \(A/\mathfrak m^n\), and the exact local flatness criterion [Stacks, Tag 0523] applies. The flat locus is open [Stacks, Tag 0399]. Its closed complement has closed image in the local base by properness; if nonempty, that image contains the closed point, contrary to the flatness just proved. The complement is empty, so \(T\) is flat everywhere. \(\square\)

Flatness cannot simply be removed from the conversion of \(H^2(\mathcal O)\) into the obstruction vanishing. We give a concrete first-order example. Work over a field of characteristic zero, take \(P=\mathbf P^3_k\), and a quartic hypersurface \(Z\subset P\); put \(J=\mathcal O_Z\), regarded as an \(\mathcal O_P\)-module. Projective-space cohomology and the hypersurface sequences give
\[
H^2(P,\mathcal O_P)=0,\quad H^2(P,J)=k,
\quad H^1(P,J(1))=H^2(P,J(1))=0.
\]
For instance the middle equality is \(H^3(P,\mathcal O_P(-4))=k\). Tensor the tangent Euler sequence with \(J\):
\[
0\to J\to J(1)^4\to T_P\otimes J\to0.
\]
Here \(T_P\) is the sheaf of derivations. On \(U_i=\{X_i\neq0\}\), a tuple of homogeneous components induces the derivation of \(X_l/X_i\) given by its \(l\)-th component minus \((X_l/X_i)\) times its \(i\)-th component, in the frame \(X_i\). This map is onto, and its kernel is the scalar coordinate vector, proving the displayed Euler sequence. Its boundary gives an isomorphism \(H^1(P,T_P\otimes J)\cong H^2(P,J)\). Choose a derivation-valued Čech cocycle \(\delta_{ij}\) representing a nonzero class on the standard affine cover. Glue the split square-zero rings \(\mathcal O_P\oplus J\) by
\[
(f,a)\longmapsto(f,a+\delta_{ij}(f)).
\]
The derivation rule makes these ring isomorphisms; the cocycle rule gives gluing. They define a scheme \(P'\) with square-zero ideal \(J\). The global section \((0,1)\) gives a map to \(k[\epsilon]/(\epsilon^2)\), with reduction \(P\), since it generates \(J\) as an \(\mathcal O_P\)-module.

The obstruction to lifting \(\mathcal O_P(1)\) is nonzero. Set \(g_{ij}=X_j/X_i\), so \(g_{ij}g_{jk}=g_{ik}\), and lift these transitions as \((g_{ij},0)\). Their triple product differs from one by the additive cocycle
\(z_{ijk}=\delta_{ij}(g_{jk})/g_{jk}\). Lift \(\delta_{ij}\) to Euler components in frame \(X_i\) by taking its \(i\)-th component zero and its other components \(\delta_{ij}(X_l/X_i)\). The Euler connecting cocycle is then
\(\lambda_{ijk}=-\delta_{jk}(g_{ij})/g_{ij}\).
For \(a_{ij}=\delta_{ij}(g_{ij})/g_{ij}\), the cocycle identities give
\[
z_{ijk}-\lambda_{ijk}=-(a_{jk}-a_{ik}+a_{ij}).
\]
Thus the obstruction class equals the Euler boundary of \([\delta]\). That boundary is an isomorphism, so the class is nonzero. This is a nonflat first-order deformation with \(H^2(\mathcal O_P)=0\) and a line bundle that does not lift. The flat hypotheses in Theorem 5.1 prevent this discrepancy of ideal layers.

## 6. Curves and exercises with solutions

A flat compatible formal deformation of a smooth projective curve over \(k[[t]]\) algebraizes. Its closed fiber has dimension one, so \(H^2(C,\mathcal O_C)=0\) by the cohomological dimension bound. Theorem 5.1 supplies a projective flat algebraization. It also algebraizes compatible sheaves by Grothendieck existence and compatible maps to separated finite-type targets by Theorem 2.2.

The curve need not be smooth for the existence argument. For example, consider the compatible projective conics
\[
T_n=\{xy=t z^2\}\subset\mathbf P^2_{k[t]/t^n},
\qquad L_n=\mathcal O_{T_n}(1).
\]
Their homogeneous coordinate rings are flat over the parameter ring: the equation is monic in the monomial \(xy\), and the monomials not divisible by \(xy\) give a free basis. Localization and taking the degree-zero summand preserve flatness on the projective charts. The closed fiber is the union of two lines, still of dimension one, so its second cohomology vanishes. The theorem algebraizes this system; explicitly its algebraization is the same equation in \(\mathbf P^2_{k[[t]]}\). The uniqueness theorem identifies any other proper algebraization inducing the given formal identifications with this one. The compatible hyperplane bundles algebraize as well, so the equation and its polarization are recovered together.

**Exercise 6.1 (easy: uniqueness).** Prove uniqueness of an algebraized closed subscheme, keeping its embedding in a fixed proper \(X\).

**Solution.** The prescribed quotient systems give a formal isomorphism of the two quotient sheaves respecting the maps from \(\mathcal O_X\). Full faithfulness gives the unique algebraic isomorphism, and makes compatibility with those maps an actual equality. Their kernels coincide, so the embedded closed subschemes coincide. An abstract isomorphism alone would not identify their embeddings.

**Exercise 6.2 (medium: projective subschemes).** Algebraize a cartesian system of closed subschemes of \(\mathbf P^N_{k[t]/t^n}\).

**Solution.** Regard their structure sheaves as coherent formal quotient modules on \(\mathbf P^N_{k[[t]]}\). Existence algebraizes the quotient module; full faithfulness algebraizes the quotient map; exactness and faithfulness kill its cokernel. Its coherent ideal kernel cuts out the desired projective subscheme, and Theorem 1.1 proves uniqueness. No flatness of the subschemes is required.

**Exercise 6.3 (medium: the obstruction).** Derive the obstruction and ambiguity for lifting a line bundle across a square-zero thickening.

**Solution.** Use the unit sequence (2), whose kernel is additively \(J\). The long exact sequence identifies the obstruction as \(\partial(L)\in H^2(T,J)\). It vanishes exactly when \(L\) lifts. The possible lift classes, if any, form a torsor under \(\ker(\operatorname{Pic}(T')\to\operatorname{Pic}(T))\), which (3) identifies with \(H^1(T,J)\) modulo the image of the unit boundary. This is the precise ambiguity, rather than an unqualified torsor under all of \(H^1(T,J)\).

**Exercise 6.4 (hard: a formal curve).** Algebraize a flat formal deformation of a smooth projective curve over \(k[[t]]\), explaining how its polarization is obtained.

**Solution.** Choose an ample line bundle on the closed curve. Each ideal layer is \(\mathcal O_C\), since \((t^n)/(t^{n+1})\cong k\). Its second cohomology vanishes in dimension one, so (3) lifts the line bundle successively, with compatible identifications. Theorem 4.1 algebraizes the polarized system to a projective scheme. The flat quotient criterion gives flatness on the closed fiber; openness and properness over the local base give flatness everywhere. This is the projective flat family required.

**Exercise 6.5 (hard: recovering the root).** In Theorem 4.1, why is recovering \(L^d\) insufficient, and how is \(L\) itself recovered?

**Solution.** An embedding constructs the chosen positive power; it does not by itself produce its specified root. Apply existence to \((L_n)\) and \((L_n^{-1})\). Full faithfulness algebraizes the evaluation isomorphism and its inverse, so their algebraizations are tensor inverses and the first is invertible. Full faithfulness identifies its \(d\)-th power with the embedding bundle. Ampleness of that power then proves ampleness of the recovered \(L\).

**Exercise 6.6 (hard: finite algebras).** Explain why algebraizing only the underlying module of a finite formal algebra is enough to recover its algebra structure.

**Solution.** Completion commutes with finite tensor products. Thus formal multiplication and unit are formal maps between completions of coherent modules. Full faithfulness algebraizes them uniquely. Associativity compares two maps from the triple tensor product, commutativity compares two maps from the double tensor product, and the unit axioms compare maps from the module itself. All agree after completion, hence agree algebraically by faithfulness. Relative Spec then recovers the finite scheme and all its reductions.

## References

- **[Stacks]** The Stacks project authors, *The Stacks project*, in its AI Integrated Stacks Project edition: closed-subscheme algebraization [Tag 0899](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/coherent.html#coherent-lemma-algebraize-formal-closed-subscheme), finite algebraization [Tag 09ZT](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/coherent.html#coherent-lemma-algebraize-formal-scheme-finite-over-proper), morphisms [Tag 0A42](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/coherent.html#coherent-lemma-algebraize-morphism), and polarized algebraization [Tag 089A](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/coherent.html#coherent-theorem-algebraization).
- Nilpotent checks [Tag 09ZW](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-morphisms.html#more-morphisms-lemma-thicken-property-morphisms-cartesian), [Tag 0896](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-check-closed-infinitesimally); finite-fiber neighborhood [Tag 02OH](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/coherent.html#coherent-lemma-proper-finite-fibre-finite-in-neighbourhood).
- The Picard sequence is [Tag 0C6R](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-morphisms.html#more-morphisms-lemma-picard-group-first-order-thickening). Flatness uses [Tag 0523](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-flat-module-powers) and its open locus [Tag 0399](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-morphisms.html#more-morphisms-theorem-openness-flatness). The flat \(H^2\) criterion also appears in [AI Integrated Stacks Project, coherent.tex, lemma-algebraize-flat-formal-scheme-H2](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/coherent.html#coherent-lemma-algebraize-flat-formal-scheme-H2), with these same flatness hypotheses.
- These open reference treatments retain GNU FDL 1.2. The proofs, exposition, examples and solutions here are CC0 and use the preceding course results and the open foundations named above. AI Integrated Stacks Project includes AI-proposed additions and corrections and is not reviewed by maintainers of the [official Stacks project](https://stacks.math.columbia.edu/).
