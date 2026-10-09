# Constructible duality and infinite twists

Learn how the actual Verdier-duality maps reverse inverse and direct images, why a nonproper image needs a second constructibility input, and how an infinite locally constant twist can preserve the comparison when the untwisted object has finite boundary control. Eight exercises have complete solutions.

- [Duality maps for constructible inverse and direct images](duality-maps-for-constructible-inverse-and-direct-images.html) · [editable source](src/duality-maps-for-constructible-inverse-and-direct-images.md)
- [Natural comparisons with infinite locally constant coefficients](providers/weak-operation-comparisons.html) · [editable proof selection](providers/src/comparisons-selection.md)

The lesson uses a commutative ring of finite global dimension, bounded complexes and the stated finite-dimensional analytic-manifold conventions. The nonproper twisted direct-image theorem uses b-analytic pairs, a subanalytic ambient graph and an untwisted zero extension with perfect stalks. The twist itself may be infinite and need not extend across the ambient boundary. Orientations, shifts and canonical evaluation order are retained.

Download the lesson, proofs, sources and build code · [Reuse terms](LICENSE.txt) · Provenance


# Duality maps for constructible inverse and direct images

Dualizing a sheaf twice comes with a map from the original sheaf. Whether that map is invertible determines which duality comparisons can be reversed. We will construct the comparison maps, factor the reversed maps through evaluation, and then identify the geometric hypotheses that make those evaluations invertible. An infinite locally constant coefficient requires a different argument: move it through an internal Hom, rather than evaluate it twice.

The first part develops proper support, adjunction, orientation and evaluation. The constructible applications use the geometric results listed in [Prerequisites and reading](#prerequisites-and-reading-prerequisites).

*Original programme exposition and exercises: CC0. The infinite-coefficient results of Andreas Hohl and Pierre Schapira are credited where they enter the argument.*

## Coefficients, pairings and the operation contracts {#pairings}

Let \(k\) be a commutative ring of finite global dimension. Spaces in this lesson are finite-dimensional real analytic manifolds, Hausdorff and countable at infinity, with a uniform dimension bound. Complexes are globally bounded. All tensors and internal Homs are derived. We use

\[
\omega_X=a_X^!k,\qquad D_XE=R\mathcal Hom_X(E,\omega_X),
\qquad H^j(E[s])=H^{j+s}(E).
\tag{1}
\]

For a \(d\)-manifold, \(\omega_X=\mathrm{or}_X[d]\). Keep the orientation line in this formula unless an orientation has been chosen.

We first work formally with a map \(f:Y\to X\). The required operation contracts are ordinary adjunction \(f^{-1}\dashv Rf_*\), proper-support adjunction \(Rf_!\dashv f^!\), tensor–Hom adjunction, the projection isomorphism

\[
Rf_!(B\otimes f^{-1}A)\simeq Rf_!B\otimes A,
\tag{2}
\]

and composition \(f^!\omega_X\simeq\omega_Y\), with its compatible trace \(Rf_!\omega_Y\to\omega_X\). These contracts include their units, counits, naturality and boundedness. The sections below prove compact-support extension and lifting, the proper-image fibre formulas, base change and composition, the uniform manifold dimension bound, and arbitrary-coefficient projection. The adjunction section then constructs both adjunctions on bounded-below categories and fixes their trace-compatible exceptional composition. The following bounds section proves globally bounded preservation for ordinary direct image, exceptional inverse image and duality. The tensor–Hom section then constructs the remaining algebraic contract, including the actual evaluation map and its signs. The orientation section proves the constant local-support and orientation inputs. Constructible and weakly constructible geometric inputs remain prerequisites. In particular, (2) permits arbitrary bounded \(A\); it is not a projection theorem restricted to perfect coefficients. The formal arguments also apply outside the analytic setting whenever these same bounded operation contracts hold.

Evaluation is the pairing \(\operatorname{ev}_E:D_XE\otimes E\to\omega_X\). By symmetry and currying it gives

\[
\eta_E:E\longrightarrow D_XD_XE.
\tag{3}
\]

We call \(E\) **reflexive for this duality** when this particular map is invertible. An abstract isomorphism between \(E\) and \(D_XD_XE\) would not be sufficient.

All maps below use the usual symmetry on complexes. On homogeneous tensors that symmetry is \(v\otimes w\mapsto(-1)^{|v||w|}w\otimes v\). Currying and evaluation use the same convention, so reversing a pairing introduces no unrecorded sign.

<span id="two-general-identities-before-biduality"></span>

## Compact support: extension, lifting and acyclicity {#compact-support-proof}

The projection proof needs precise control of support when a section is extended or lifted. We supply that part of its foundation here. Throughout this section, spaces are locally compact Hausdorff and coefficients are arbitrary modules over the fixed commutative ring \(k\). Finite global dimension is unnecessary for these support arguments. For a compact subset \(K\subset X\), \(\Gamma(K;F)\) means sections of the inverse-image sheaf on \(K\), not sections on \(X\) whose support lies in \(K\).

The human source for these results is Pierre Schapira's freely accessible [*An Introduction to Sheaves on Grothendieck Topologies*, 1 August 2026, §4.3](https://webusers.imj-prg.fr/~pierre.schapira/LectNotes/SHV.pdf). His word “soft” in that section means what we call **c-soft**: every section on every compact subset extends to a global section. We organise the proof around two concrete operations—extending with prescribed support and lifting through a quotient—and include the compact-neighbourhood details they require. The following sections supply the proper-image fibre formula and the uniform manifold dimension bound.

### Compact subsets remember neighbourhood germs {#compact-germ-gluing}

We first justify the comparison

\[
\mathop{\mathrm{colim}}_{K\subset V\text{ open}}\Gamma(V;F)
\xrightarrow{\sim}\Gamma(K;F).
\tag{C1}
\]

The elementary topological facts needed below follow from compactness and Hausdorff separation. Disjoint compact sets have disjoint open neighbourhoods: separate each pair of points, take a finite intersection on the neighbourhood of a fixed point and a finite union on the opposite compact set, then repeat over a finite cover of the first compact set. Thus a compact Hausdorff space is normal. Inside a compact neighbourhood, this separation shrinks a neighbourhood of a point so that its closure is compact and lies in any specified open neighbourhood. Applying these pointwise shrinkings and then taking a finite subcover gives compact sets subordinate to any finite open cover of a compact set.

Surjectivity of (C1) is not merely the definition of inverse image, since that definition also sheafifies. A section on \(K\) has local representatives \(s_i\) on ambient open sets \(N_i\). Choose finitely many compact sets \(K_i\subset K\cap N_i\) covering \(K\), and relatively compact open neighbourhoods \(O_i\) of \(K_i\) with \(\overline{O_i}\subset N_i\). For each pair \(i,j\), let \(E_{ij}\) be the open subset of \(N_i\cap N_j\) where the germs of \(s_i,s_j\) agree. It contains \(K_i\cap K_j\). The compact set
\(D_{ij}=(\overline{O_i}\cap\overline{O_j})\setminus E_{ij}\)
therefore meets \(K_i\) and \(K_j\) in disjoint closed subsets. Separate those two subsets by disjoint relatively open subsets of \(D_{ij}\). Their complements in \(D_{ij}\) are compact, so taking their complements in \(X\) gives open neighbourhoods of \(K_i,K_j\) whose intersection misses \(D_{ij}\). Intersect these neighbourhoods over the finitely many pairs, also intersecting with \(O_i\). The resulting opens \(W_i\) still contain \(K_i\), and the representatives agree on every \(W_i\cap W_j\). The sheaf axiom glues them to a section on \(\bigcup_iW_i\), a neighbourhood of \(K\). This proves surjectivity.

For injectivity, two representatives with equal restriction to \(K\) have equal germs at every point of \(K\). Their equality locus is open and contains \(K\). They are therefore equal after shrinking their common neighbourhood, exactly the equivalence relation in the colimit.

We also use gluing over a finite closed cover of a compact space. If sections on closed sets \(K_1,\ldots,K_m\) agree on their intersections, their germs give a section on their union. To check this locally at a point, discard the finitely many closed sets not containing that point. Representatives from the remaining sets have the same germ there, so they agree on a common smaller neighbourhood. This supplies a local representative of the proposed glued section; these representatives agree wherever both are defined. Hence the sheaf axiom proves existence and uniqueness of the glued section. This argument concerns sections of restricted sheaves, so equality on an intersection includes equality of the corresponding ambient germs.

### Extending a section while controlling its support {#compact-support-extension}

**Support extension lemma.** Suppose \(F\) is c-soft, \(K\subset X\) is compact, and \(s\in\Gamma(K;F)\). If the support of \(s\) in \(K\) lies in an open set \(V\subset X\), there is \(t\in\Gamma_c(X;F)\) such that

\[
t|_K=s,\qquad \operatorname{supp}(t)\subset V.
\tag{C2}
\]

**Proof.** The support of a section is closed in its domain because its zero-germ locus is open. Thus \(A=\operatorname{supp}(s)\) is compact. Choose a compact neighbourhood \(L\) of \(A\) contained in \(V\); if \(A\) is empty, take \(t=0\). On the compact set \((K\cap L)\cup\partial L\), prescribe \(s\) on \(K\cap L\) and zero on \(\partial L\). These prescriptions agree on the intersection because \(A\subset\operatorname{int}L\). Finite closed gluing supplies a section there. By c-softness it extends to a global section \(u\) of \(F\).

The germs of \(u\) vanish on \(\partial L\), so \(u\) vanishes on an open neighbourhood of that boundary. Glue \(u\) on \(\operatorname{int}L\) to zero on the union of that neighbourhood with \(X\setminus L\). These opens cover \(X\), and the prescribed sections agree on the overlap. The resulting \(t\) has support in \(L\subset V\). On \(K\cap L\) it agrees with \(s\); on \(K\setminus L\) both vanish. This proves (C2). \(\square\)

Several stability properties now have direct proofs.

* Restriction preserves c-softness whenever the subspace in question is locally compact Hausdorff. A compact subset of that subspace is compact in \(X\), and iterated inverse image identifies its restricted sections with \(\Gamma(K;F)\). Extend in \(X\) and then restrict.
* If \(j:U\hookrightarrow X\) is open and \(G\) is c-soft on \(U\), then \(j_!G\) is c-soft on \(X\). Given a section on a compact \(K\subset X\), its support \(A\) is a compact subset of \(K\cap U\), since the stalks off \(U\) are zero. Choose \(A\subset\operatorname{int}L\subset L\subset U\) with \(L\) compact. The same prescription on \((K\cap L)\cup\partial L\), now made entirely inside \(U\), extends using c-softness of \(G\). Cut it off at \(\partial L\) as in the lemma and extend by zero to \(X\). It has the prescribed restriction to \(K\).
* An arbitrary coproduct of c-soft sheaves is c-soft. A section of that coproduct on a compact set locally involves finitely many summands, by the sheafification definition of a coproduct. A finite cover of the compact set shows that a single finite set of indices suffices. The section factors through that finite subsum on the compact set, as one can check on stalks. Extend its finitely many components globally and then include the finite subsum in the full coproduct. No assertion about unrestricted sections commuting with infinite coproducts is used.

Finally, injective sheaves are c-soft. For opens \(U\subset V\), the map \(k_U\to k_V\) is a monomorphism, as its stalks show. The identification \(\operatorname{Hom}(k_U,I)=\Gamma(U;I)\) and injectivity of \(I\) make every restriction \(\Gamma(V;I)\to\Gamma(U;I)\) surjective. Thus \(I\) is flabby. A section on a compact set is represented on a neighbourhood by (C1), and flabbiness extends that representative to \(X\). The same argument proves directly that every flabby sheaf is c-soft.

### Lifting compactly supported sections {#compact-support-lifting}

**Lifting lemma.** If \(0\to F'\to F\to F^{\prime\prime}\to0\) is exact and \(F'\) is c-soft, then

\[
0\longrightarrow\Gamma_c(X;F')\longrightarrow\Gamma_c(X;F)
\longrightarrow\Gamma_c(X;F^{\prime\prime})\longrightarrow0
\tag{C3}
\]

is exact.

**Proof.** Left exactness follows from kernels and the definition of support. We prove surjectivity first when \(X\) is compact. A section \(s^{\prime\prime}\) has lifts on an open cover because the sheaf map \(F\to F^{\prime\prime}\) is surjective on stalks. Choose a finite compact closed cover \(K_i\) subordinate to that cover, and use the corresponding local lifts on \(K_i\).

Suppose lifts have already been glued on \(K_1\cup\cdots\cup K_{i-1}\). On its intersection with \(K_i\), the difference between the existing lift and the new lift is a section of \(F'\): restriction is exact and sections preserve kernels. The intersection is compact, so c-softness extends that difference to a global section of \(F'\). Add this extension to the new lift. The adjusted lifts agree on the intersection, and finite closed gluing combines them. Finite induction gives a lift on all of \(X\).

For general \(X\), let \(s^{\prime\prime}\) have compact support \(A\), and choose a relatively compact open \(U\) containing \(A\). Write \(F_U=j_!(F|_U)\), and similarly for the other two sheaves. Open extension by zero is exact by its stalk formula, so these sheaves give a short exact sequence. Its first term is c-soft by the restriction and extension properties just proved. Each term has zero stalks outside the compact set \(\overline U\).

A sheaf supported on a closed set is the direct image of its restriction to that set: the natural map to that direct image is an isomorphism on every stalk. Restrict our sequence to \(\overline U\), apply the compact case there, and push the resulting section back to \(X\). All its support is compact. The section \(s^{\prime\prime}\) belongs to \(\Gamma_c(X;F^{\prime\prime}_U)\), since it vanishes near every point outside its compact support \(A\subset U\). The compact-case lift is therefore a compactly supported lift of the original \(s^{\prime\prime}\). This proves (C3). \(\square\)

**Quotient consequence.** In a short exact sequence, if \(F'\) and \(F\) are c-soft, then so is \(F^{\prime\prime}\). Given a section of \(F^{\prime\prime}\) on a compact \(K\), restrict the sequence to \(K\). Its first term is c-soft there, so the compact case of (C3) lifts that section to \(\Gamma(K;F)\). C-softness of \(F\) extends the lift globally. Its image is the desired extension of the original section.

### The compact-cohomology criterion {#compact-cohomology-criterion}

We now prove, rather than assume, the equivalence

\[
F\text{ is c-soft}\quad\Longleftrightarrow\quad
H_c^q(U;F|_U)=0
\quad\text{for every open }U\subset X\text{ and }q>0.
\tag{C4}
\]

Use the usual injective definition of the right derived functor of \(\Gamma_c\). If \(F\) is c-soft, embed it into an injective and continue to an injective resolution. Every successive cokernel is c-soft by the quotient consequence. The lifting lemma makes each of the resulting short exact sequences exact after \(\Gamma_c\). Hence the complex of compactly supported sections of the injective resolution is exact in positive degrees. This proves \(\Gamma_c\)-acyclicity. Apply the same argument to the c-soft restriction on each open \(U\) to obtain the forward implication in (C4).

We will also use the following derived extension identity, including for a sheaf \(G\) which is not c-soft:

\[
H_c^q(X;j_!G)=H_c^q(U;G),\qquad j:U\hookrightarrow X.
\tag{C5}
\]

Take an injective resolution of \(G\) on \(U\). Its terms are c-soft, so their open extensions are c-soft on \(X\) and therefore \(\Gamma_c\)-acyclic by the preceding paragraph. Exactness of \(j_!\) makes this an acyclic resolution of \(j_!G\). Termwise, compactly supported sections on \(U\) and on \(X\) are identical under extension by zero: a compact support in \(U\) is compact in \(X\), and a compact support of a section of \(j_!G\) lies inside \(U\). The acyclic-resolution comparison, applied to these degreewise identical complexes, proves (C5).

Here is the comparison needed in that last step. For an acyclic resolution \(0\to M\to A^0\to A^1\to\cdots\), put \(Z^1=A^0/M\). The first derived-functor exact sequence identifies \(R^1T(M)\) with \(\operatorname{coker}(T(A^0)\to T(Z^1))\), which is \(H^1(T(A^\bullet))\) because \(T\) preserves kernels. For \(q\geq2\), the same exact sequence gives \(R^qT(M)=R^{q-1}T(Z^1)\). Repeat using the tail resolution of \(Z^1\); after finitely many repetitions this is the same degree-one calculation. Degree zero is left exactness. The connecting maps come from the given short exact sequences, so the identifications are natural. Apply this with \(T=\Gamma_c\).

For the reverse implication in (C4), fix a compact \(K\subset X\), put \(U=X\setminus K\), and let \(i:K\hookrightarrow X\), \(j:U\hookrightarrow X\). Stalks give an exact sequence

\[
0\longrightarrow j_!(F|_U)\longrightarrow F
\longrightarrow i_*(F|_K)\longrightarrow0.
\tag{C6}
\]

The long exact sequence for compactly supported cohomology and (C5) show that \(\Gamma_c(X;F)\to\Gamma_c(X;i_*(F|_K))\) is surjective, because its obstruction lies in \(H_c^1(U;F|_U)=0\). The group on the right is \(\Gamma(K;F)\), since \(K\) is compact. Every section on \(K\) thus has a compactly supported global extension, proving c-softness. This completes (C4).

### What this proves for proper direct image {#soft-proper-image-boundary}

The support arguments above also supply proper-image acyclicity from the **underived proper-image fibre formula**, proved in the next section:

\[
(f_!Q)_x\simeq\Gamma_c(f^{-1}(x);Q|_{f^{-1}(x)}).
\tag{C7}
\]

Indeed, restrict an injective resolution of a c-soft \(Q\) to the closed fibre. Restriction is exact, all its terms are c-soft there, and all the successive cokernels are c-soft. The lifting lemma makes its compact-section complex exact in positive degrees. Applying (C7) termwise identifies that complex with the stalk of \(f_!I^\bullet\). Thus \(R^qf_!Q=0\) for \(q>0\). This proves the acyclicity implication without assuming the derived fibre formula as an extra theorem.

The next section proves (C7) and the coproduct and open-extension compatibilities of \(f_!\), thereby establishing the acyclicity conclusion. The following composition and dimension section proves the uniform compact-cohomology bound. The subsequent bounded c-soft construction shows exactly how it supplies finite cohomological dimension and arbitrary-coefficient projection.


## Proper support and the fibre calculation {#proper-image-proof}

We now supply the proper-image facts used in (C7) and in the projection argument. Let \(f:Y\to X\) be continuous between locally compact Hausdorff spaces. The results in this section hold over an arbitrary fixed commutative coefficient ring \(k\); finite generation and finite global dimension are unnecessary. The source for the construction is Pierre Schapira's freely accessible [*An Introduction to Sheaves on Grothendieck Topologies*, 1 August 2026, §§4.1–4.2](https://webusers.imj-prg.fr/~pierre.schapira/LectNotes/SHV.pdf). We use compactly supported pieces to make the stalk calculation explicit, including its agreement with the ordinary proper-support definition.

### A proper map shrinks neighbourhoods of its fibre {#proper-fibre-neighbourhoods}

Suppose first that \(p:Z\to X\) is proper, meaning that inverse images of compact subsets are compact. Such a map is closed. Indeed, if \(A\subset Z\) is closed and \(x\notin p(A)\), choose a compact neighbourhood \(N\) of \(x\). The set \(A\cap p^{-1}N\) is compact, so its image is compact and hence closed in \(X\). Removing that image from \(\operatorname{int}N\) gives a neighbourhood of \(x\) disjoint from \(p(A)\).

Let \(W\) be any open neighbourhood of the compact fibre \(Z_x=p^{-1}(x)\). Closedness of \(p\) shows that \(V=X\setminus p(Z\setminus W)\) is an open neighbourhood of \(x\), and \(p^{-1}V\subset W\). Consequently the sets \(p^{-1}V\), for \(V\) ranging over neighbourhoods of \(x\), are cofinal among neighbourhoods of \(Z_x\). The compact-germ comparison (C1) gives

\[
(p_*H)_x
=\mathop{\mathrm{colim}}_{x\in V}\Gamma(p^{-1}V;H)
\simeq\Gamma(Z_x;H|_{Z_x}).
\tag{F1}
\]

This is the restriction map on germs, and is natural in \(H\). If the fibre is empty, the same closedness argument supplies a neighbourhood with empty inverse image, so both sides are zero. No surjectivity or local triviality of \(p\) was assumed.

The same formula applies when \(p\) is proper only on a closed set supporting \(H\): write \(H\) as the direct image of its restriction to that closed set and apply the proper case there. In particular it applies to every sheaf supported on a fixed compact set.

### Constructing the proper-support subsheaf {#proper-support-construction}

For an open \(U\subset Y\), let \(Q_U\) denote the restriction of \(Q\) to \(U\), extended by zero. Each \(Q_U\to Q\) is monic on stalks. Relatively compact open subsets of \(Y\) form a directed family under finite unions. Define the sheaf

\[
f_!Q=\mathop{\mathrm{colim}}_{U\Subset Y}f_*(Q_U),
\qquad U\Subset Y\text{ means }\overline U\text{ is compact}.
\tag{F2}
\]

The colimit here is a **sheaf** colimit. The inclusions into \(f_*Q\) identify it with a subsheaf: taking stalks gives a directed union of submodules. Thus a section of \(f_!Q\) over an open \(V\subset X\) is locally represented by sections of \(Q_U\) for relatively compact \(U\). We prove that this is exactly the familiar condition that its support be proper over \(V\).

Take such a section, viewed as \(s\in\Gamma(f^{-1}V;Q)\), and write \(S=\operatorname{supp}(s)\), a closed subset of \(f^{-1}V\). Locally on \(V\), the representative through \(Q_U\) implies \(S\subset\overline U\). Over a compact subset \(C\) of that local neighbourhood, the set \(S\cap f^{-1}C\) is closed in \(Y\) and contained in the compact set \(\overline U\); it is therefore compact. For a general compact \(C\subset V\), choose finitely many compact subsets covering \(C\), each subordinate to one of those local neighbourhoods. This finite shrinking is available by the compact Hausdorff argument preceding (C1). Their inverse images in \(S\) are compact and cover the inverse image of \(C\). Thus \(S\to V\) is proper.

Conversely, suppose \(S\to V\) is proper. For \(x\in V\), choose a compact neighbourhood \(N\subset V\) of \(x\). Then \(S\cap f^{-1}N\) is compact, so it lies in some relatively compact open \(U\subset Y\). On \(f^{-1}(\operatorname{int}N)\), the section has zero germs outside \(U\). The stalk description of the subsheaf \(Q_U\subset Q\) shows that it factors through that subsheaf there. Hence \(s\) locally belongs to a term in (F2), so it is a section of \(f_!Q\). This proves the claimed identification with proper support.

In particular, when \(f\) itself is proper, every section of \(f_*Q\) satisfies this condition: a closed support over an open of the target remains proper over that open. The natural inclusion is then an isomorphism \(f_!Q=f_*Q\).

### The underived fibre formula {#proper-image-fibre}

Fix \(x\in X\) and put \(Y_x=f^{-1}(x)\). For every relatively compact open \(U\subset Y\), the sheaf \(Q_U\) is supported on the compact set \(\overline U\). Applying (F1) to that support gives

\[
(f_!Q)_x
\simeq\mathop{\mathrm{colim}}_{U\Subset Y}
\Gamma(Y_x;(Q_U)|_{Y_x})
\simeq\Gamma_c(Y_x;Q|_{Y_x}).
\tag{F3}
\]

Here are the details of the last isomorphism. By the stalk formula for open extension, \((Q_U)|_{Y_x}\) is \(Q|_{Y_x}\) restricted to \(U\cap Y_x\) and extended by zero within the fibre. A global section of this sheaf has support closed in \(Y_x\) and contained in \(\overline U\cap Y_x\), a compact set. It therefore gives a compactly supported section of \(Q|_{Y_x}\). All transition maps are the inclusions of these sections into the same section module.

Conversely, if \(t\) has compact support in \(Y_x\), that support is compact in \(Y\). Choose a relatively compact open \(U\) containing it. The section has zero germs outside \(U\cap Y_x\), so it belongs to \(\Gamma(Y_x;(Q_U)|_{Y_x})\). The directed union therefore contains exactly all compactly supported sections. This proves (F3), including injectivity, and proves the previously stated formula (C7). No commutation of unrestricted sections with a colimit was used.

Restriction to the fibre is exact, and compactly supported sections preserve kernels: a section in a kernel has the same support whether regarded in the kernel sheaf or in the containing sheaf. Testing on stalks in (F3) consequently proves that \(f_!\) is left exact. It also confirms that, for the map to a point, (F2) is exactly \(\Gamma_c\).

### Coproducts and open extensions {#proper-image-support-compatibilities}

Compactly supported sections commute with arbitrary coproducts. A section with compact support \(K\) locally uses only finitely many summands; a finite cover of \(K\) gives one finite set of indices which suffices everywhere on \(K\). Outside \(K\) all its germs are zero. Stalkwise factorization therefore puts the whole section in that finite subsum, and its finitely many components have compact support. Conversely a finite family of compactly supported sections gives such a section of the coproduct. These inverse constructions prove the claim. Inverse image to a fibre preserves coproducts, so (F3) shows that the canonical map

\[
\bigoplus_\lambda f_!Q_\lambda
\xrightarrow{\sim}f_!\left(\bigoplus_\lambda Q_\lambda\right)
\tag{F4}
\]

is an isomorphism on every stalk. This does not assert that arbitrary sections commute with coproducts.

Let \(V\subset X\) be open, \(U=f^{-1}V\), and \(f_V:U\to V\) the restricted map. The proper-support description of sections immediately gives
\((f_!Q)|_V=(f_V)_!(Q|_U)\): over every open subset of \(V\), the section modules and proper-support conditions are identical.

There is also the extension comparison

\[
(f_!Q)_V\xrightarrow{\sim}f_!(Q_U),
\qquad U=f^{-1}V.
\tag{F5}
\]

Both sides are subsheaves of \(f_!Q\). The right side is a subsheaf by left exactness. On a stalk inside \(V\), formula (F3) identifies each inclusion with the identity of \(\Gamma_c(Y_x;Q|_{Y_x})\). On a stalk outside \(V\), the fibre misses \(U\), so both sides are zero. Their images in \(f_!Q\) are thus the same subsheaf, proving (F5) canonically.

The stalk identifications \(Q\otimes k_U=Q_U\) and \(f_!Q\otimes k_V=(f_!Q)_V\) turn (F5) into the open-generator projection map (P7). It is the map which multiplies a properly supported section by the pulled-back coefficient section. Hence the isomorphism just proved is the specific map used in the projection proof, not merely an unspecified isomorphism of its endpoints.

### The derived fibre formula and c-soft acyclicity {#derived-proper-image-fibre}

Combining (F3) with the compact-support proofs gives, for \(B\in D^+(k_Y)\), the natural identity

\[
(Rf_!B)_x\simeq R\Gamma_c(Y_x;B|_{Y_x}).
\tag{F6}
\]

To prove it, choose a bounded-below injective representative \(I\) of \(B\). Stalks are exact, so \((Rf_!B)_x\) is represented by \((f_!I)_x\), which (F3) identifies termwise with \(\Gamma_c(Y_x;I|_{Y_x})\). Restriction is exact, hence \(I|_{Y_x}\) represents \(B|_{Y_x}\). Its terms are c-soft, by injective c-softness and restriction stability, and thus are \(\Gamma_c\)-acyclic.

For clarity, a bounded-below complex of acyclic terms computes a right derived functor. In any fixed degree \(q\), cut the complex off brutally above degree \(q+1\). The kernel starts in degree \(q+2\); applying the termwise functor or its right derived functor gives no cohomology below that degree. For the derived statement, use a bounded-below injective replacement starting in the same degree, which exists by the usual degreewise resolution construction. The cutoff therefore changes neither computation in degree \(q\). The cutoff complex is bounded, and the finite acyclic-complex argument proved after (P4) applies to it. These natural comparisons prove the assertion in each degree. This argument does not use an unbounded totalization or a uniform cohomological-dimension bound.

Apply that comparison to \(I|_{Y_x}\) to prove (F6). The maps arise from restriction and resolution comparisons, so the identity is natural in \(B\). For an ordinary sheaf \(Q\) whose restriction to every fibre is c-soft, (C4) and (F6) imply \(R^qf_!Q=0\) for \(q>0\). In particular every c-soft sheaf on \(Y\) is \(f_!\)-acyclic. Thus the conditional acyclicity argument after (C7) is now established without an imported fibre theorem.

No bounded-output assertion follows merely from (F6). The next section supplies a uniform compact-cohomology bound and a finite c-soft resolution on the standing manifolds, thereby keeping \(Rf_!\) in a globally bounded range. The later adjunction section constructs the bounded-below exceptional adjoint. The subsequent bounds section proves its globally bounded output estimate. The geometric duality inputs remain separate obligations.


## Composition and the uniform dimension bound {#composition-and-dimension}

The fibre calculation alone does not bound cohomology. We now prove the missing bound, using proper-image composition to reduce Euclidean space one coordinate at a time to the interval. We then turn the local bounds into finite c-soft resolutions on manifolds. These arguments work for arbitrary sheaves over the fixed commutative ring \(k\); neither finite generation nor finite global dimension is needed in this section.

The human source is Schapira's free [*An Introduction to Sheaves on Grothendieck Topologies*, 1 August 2026](https://webusers.imj-prg.fr/~pierre.schapira/LectNotes/SHV.pdf): §4.2 for proper-support composition, §§4.3 and 4.5 for c-soft images and base change, Lemma 3.5.1 for the interval, and Lemma 5.1.1 and Proposition 5.1.2 for the dimension bound. We supply the compact-neighbourhood continuity, closed-interval gluing and dimension-shifting details used in the proof. The dimension argument does not use the projection formula it is about to justify.

### Pulling back a proper support {#proper-support-base-change}

Consider a Cartesian square with \(f:Y\to X\), \(g:X'\to X\), \(Y'=Y\times_X X'\), and projections \(f':Y'\to X'\), \(g':Y'\to Y\). These spaces are locally compact Hausdorff: the fibre product is closed in \(Y\times X'\), since the diagonal of \(X\) is closed. Pulling back sections defines

\[
g^{-1}f_!Q\xrightarrow{\sim}f'_!g'^{-1}Q.
\tag{D1}
\]

We verify both the map and its invertibility. A section of \(f_!Q\) over an open \(V\subset X\) is a section of \(Q\) on \(f^{-1}V\) with a support \(S\) proper over \(V\). Its pullback has support \(g'^{-1}S\). For a compact \(C\subset g^{-1}V\), the part of that support over \(C\) is a closed subset of
\((S\cap f^{-1}g(C))\times C\).
Both factors are compact, and the equality \(f(y)=g(x')\) is closed. Thus the pulled-back support is proper. Pullback of local sections, followed by sheafification of the inverse-image presheaf, therefore gives the displayed map.

At a point \(x'\in X'\), (F3) identifies its two stalks with compactly supported sections on \(Y_{g(x')}\) and on \(Y'_{x'}\). The projection \(g'\) identifies these fibres homeomorphically, with the same restricted sheaf, and the map is the resulting pullback of sections. It is an isomorphism. Stalkwise detection proves (D1). This proof also shows that the comparison respects restriction and consecutive changes of base: in each case it pulls back the same section.

### Composing proper images and preserving c-softness {#proper-image-composition}

Let \(f:Y\to X\) and \(g:X\to Z\). Then there is a natural identification

\[
g_!f_!Q\simeq(gf)_!Q.
\tag{D2}
\]

To check it on an open \(V\subset Z\), compare both sides as subsheaves of \((gf)_*Q\). For a section \(s\) of \(Q\) on \((gf)^{-1}V\), put \(S=\operatorname{supp}(s)\). If \(S\to V\) is proper, then \(S\to g^{-1}V\) through \(f\) is proper: the inverse image of a compact \(C\subset g^{-1}V\) is closed in the compact set \(S\cap(gf)^{-1}g(C)\). The corresponding section \(t\) of \(f_!Q\) has support exactly \(T=f(S)\). Indeed, (F3) says that its stalk at \(x\) is the restricted section on the fibre, which is nonzero exactly when that fibre meets \(S\). The set \(T\) is closed in \(g^{-1}V\), since \(f|_S\) is proper and hence closed. Its inverse image under \(g\) of a compact \(C\subset V\) is the compact image \(f(S\cap(gf)^{-1}C)\). Thus \(t\) has proper support over \(V\).

Conversely, if \(s\) represents a section of \(g_!f_!Q\), then \(S\to T\) and \(T\to V\) are proper by the same support description. The inverse image in \(S\) of a compact subset of \(V\) is compact by two successive properness applications. Hence \(S\to V\) is proper. Both sheaves therefore consist of the same sections with the same restriction maps. This proves (D2), and also proves its identity and threefold-associativity compatibilities: every comparison retains the underlying section of \(Q\).

In particular, taking the last map to a point gives \(\Gamma_c(X;f_!Q)=\Gamma_c(Y;Q)\). We use this to prove that \(f_!\) preserves c-soft sheaves.

First, a c-soft sheaf \(Q\) has surjective restriction \(\Gamma_c(Y;Q)\to\Gamma_c(A;Q|_A)\) for every closed \(A\subset Y\). Given a compactly supported section on \(A\), choose a compact neighbourhood \(L\) of its support. Prescribe that section on \(A\cap L\) and zero on \(\partial L\). The prescriptions agree, since the support lies in \(\operatorname{int}L\). Both sets are compact. The compact extension and cutoff argument proving (C2) gives a global compactly supported section with the required restriction to all of \(A\); off \(L\), both restrictions vanish.

Now let \(K\subset X\) be compact. Base change (D1) for the closed inclusion of \(K\), followed by (D2) for the map from \(K\) to a point, identifies
\(\Gamma(K;f_!Q)\) with \(\Gamma_c(f^{-1}K;Q|_{f^{-1}K})\).
The restriction map from \(\Gamma_c(X;f_!Q)=\Gamma_c(Y;Q)\) becomes restriction to the closed set \(f^{-1}K\), which is surjective by the preceding paragraph. This proves c-softness of \(f_!Q\).

Choose a bounded-below injective representative \(I\) of \(B\in D^+(k_Y)\). Its terms are c-soft, so \(f_!I\) has c-soft terms and computes \(Rf_!B\). Those terms are also \(g_!\)-acyclic by (F6). The bounded-below acyclic-complex comparison proved there therefore gives

\[
Rg_!Rf_!B\simeq R(gf)_!B,
\qquad R\Gamma_c(X;Rf_!B)\simeq R\Gamma_c(Y;B).
\tag{D3}
\]

The termwise maps are (D2), so they are the natural composition maps and retain identity and threefold-associativity compatibility. This proof does not need a cohomological-dimension bound.

The same method derives (D1). Each term of \(g'^{-1}I\) is c-soft on every fibre of \(f'\): the fibre is identified with a fibre of \(f\), on which the original injective term restricts to a c-soft sheaf. Formula (F6) makes these terms \(f'_!\)-acyclic. Since inverse image is exact, applying the bounded-below comparison and (D1) termwise proves

\[
g^{-1}Rf_!B\simeq Rf'_!g'^{-1}B.
\tag{D4}
\]

The maps still pull back the original local sections before passing to resolutions; their base-change compatibilities follow from that construction. No properness of \(f\), beyond the proper supports defining \(f_!\), is required.

### Cohomology near a compact set and the interval bound {#interval-cohomology-bound}

Let \(K\) be a compact subset of a locally compact Hausdorff space. There is a natural continuity isomorphism

\[
\mathop{\mathrm{colim}}_{K\subset V\text{ open}}H^q(V;Q|_V)
\simeq H^q(K;Q|_K).
\tag{D5}
\]

To prove it, take an injective resolution \(I\) of \(Q\) on the ambient space. Restriction to an open preserves injectives: its left adjoint is the exact extension by zero, so its Hom test for injectivity remains exact. Thus \(\Gamma(V;I)\) computes the left-hand groups. The restricted complex \(I|_K\) is exact over \(Q|_K\), and its terms are c-soft on the compact space \(K\). There \(\Gamma=\Gamma_c\), so the same terms are acyclic and \(\Gamma(K;I)\) computes the right-hand groups. Comparison (C1) identifies these complexes after taking the filtered colimit. Filtered colimits of modules are exact: each equality and each witness for a preimage is witnessed at some common later index. Consequently they commute with kernels modulo images, hence with cohomology. This proves (D5).

The same proof works with compact neighbourhoods instead of open neighbourhoods. Every neighbourhood of a compact set contains a compact neighbourhood, and every compact neighbourhood contains an open one. These interleavings give the same colimit termwise. Restrictions of \(I\) to the compact neighbourhoods remain c-soft and acyclic. In particular, closed intervals shrinking down to a closed interval or to an endpoint have this cohomology continuity.

We claim that \(H^q([0,1];Q)=0\) for every \(q>1\) and every sheaf \(Q\). For \(0<t<a\leq1\), write \([0,a]=[0,t]\cup[t,a]\). Restrict an injective resolution on \([0,a]\) to these compact sets. Finite closed gluing gives the kernel in the sequence of section complexes, and c-softness gives surjectivity onto the section complex at \(\{t\}\): every germ there extends globally. The difference of restrictions therefore gives a termwise short exact sequence. Its long exact cohomology sequence, and exactness of sections on a point, give

\[
H^q([0,a];Q)\simeq
H^q([0,t];Q)\oplus H^q([t,a];Q)
\quad(q>1).
\tag{D6}
\]

Take \(s\in H^q([0,1];Q)\), \(q>1\), and let \(J\) be the set of \(a\) for which \(s|_{[0,a]}=0\). It is downward closed. The restriction to \(\{0\}\) is zero; continuity at that compact set makes the restriction zero on a nontrivial initial interval. Hence \(\tau=\sup J\) is positive. Continuity at \(\{\tau\}\), considered inside \([0,\tau]\), makes the restriction zero on some terminal interval \([t,\tau]\) with \(t<\tau\). The initial interval \([0,t]\) also has zero restriction, by the definition of the supremum and downward closure. Formula (D6) shows that the restriction to \([0,\tau]\) is zero. If \(\tau<1\), continuity around the compact set \([0,\tau]\) makes it zero on a strictly larger initial interval, a contradiction. Thus \(\tau=1\), and \(s=0\). This proves the claim without a constructibility hypothesis.

An open interval is homeomorphic to \(\mathbb R\). Extend a sheaf on \((0,1)\) by zero to \([0,1]\). Formula (C5), and compactness of the closed interval, identify its compactly supported cohomology with the ordinary cohomology of that extension. The proved interval bound therefore gives \(H_c^q(\mathbb R;Q)=0\) for \(q>1\).

### Euclidean dimension by one-dimensional fibres {#euclidean-cohomology-bound}

We prove by induction that

\[
H_c^q(\mathbb R^n;Q)=0\qquad(q>n)
\tag{D7}
\]

for every sheaf \(Q\). For \(n=0\), sections on a point are exact. The case \(n=1\) was just proved. For \(n>1\), use the projection \(p:\mathbb R^n\to\mathbb R^{n-1}\). Its fibres are lines. Formula (F6) and the interval result give \(R^jp_!Q=0\) for \(j\notin\{0,1\}\). The cohomology truncation triangle is therefore
\(R^0p_!Q\to Rp_!Q\to(R^1p_!Q)[-1]\to(R^0p_!Q)[1]\).
Applying \(R\Gamma_c(\mathbb R^{n-1};-)\), the induction hypothesis kills its first term in cohomological degrees greater than \(n-1\) and its third term in degrees greater than \(n\). The long exact sequence kills the middle term in degrees greater than \(n\). Composition (D3) identifies that middle term with \(R\Gamma_c(\mathbb R^n;Q)\), proving (D7).

If \(V\subset\mathbb R^n\) is open and \(G\) is any sheaf on \(V\), (C5) identifies \(H_c^q(V;G)\) with \(H_c^q(\mathbb R^n;j_!G)\). The same bound therefore holds on every open subset, with the same integer \(n\).

### C-softness is local {#c-softness-is-local}

Suppose a sheaf \(Q\) is c-soft on each member \(U_i\) of an open cover of a locally compact Hausdorff space. Given a section \(s\) on a compact set \(K\), choose finitely many compact subsets \(K_1,\ldots,K_m\) of \(K\) covering \(K\), each contained in a member of the cover. Such a closed refinement follows by choosing, at each point of \(K\), an open neighbourhood whose closure lies in a cover member, and then taking a finite subcover and intersecting those closures with \(K\). We extend \(s\) by successive corrections, keeping the already corrected pieces fixed.

Suppose a compactly supported global section already agrees with \(s\) on \(A=K_1\cup\cdots\cup K_{r-1}\). Its residual section on \(K\) has zero germs on \(A\), and therefore factors through \(Q_{X\setminus A}|_K\), by the stalk formula for extension by zero. On the cover member containing \(K_r\), the sheaf \(Q_{X\setminus A}\) is c-soft: it is an open extension of a restriction of the locally c-soft sheaf \(Q\). Apply (C2) there to extend the residual on \(K_r\) to a compactly supported section of that sheaf. Extend the correction by zero to the whole space and add it. It changes no germs on \(A\), and corrects \(K_r\).

Start with zero and repeat finitely many times. The resulting compactly supported section agrees with \(s\) on all of \(K\), proving c-softness of \(Q\). Only a finite cover of the given compact set was used; no locally finite global partition was assumed.

### The uniform manifold bound and finite c-soft resolutions {#uniform-manifold-dimension}

Let \(Y\) be a manifold of the standing kind, with a fixed finite upper bound \(N\) on all its local dimensions. Then, for every open \(U\subset Y\) and every sheaf \(Q\) on \(U\),

\[
H_c^q(U;Q)=0\qquad(q>N).
\tag{D8}
\]

Here is the finite resolution that proves this globally. For a sheaf \(Q\) on \(Y\), choose an injective resolution \(I\) in nonnegative degrees and put \(Z^r=\ker(d:I^r\to I^{r+1})\), with \(Z^0=Q\). The sequences \(0\to Z^r\to I^r\to Z^{r+1}\to0\) are exact. On an open subset \(V\) of a coordinate chart, the terms \(I^r|_V\) are c-soft and compact-section acyclic. Their long exact sequences give, for \(q>0\),

\[
H_c^q(V;Z^N|_V)\simeq H_c^{q+N}(V;Q|_V)=0.
\tag{D9}
\]

The last equality is the Euclidean open-set bound, since the chart dimension is at most \(N\). If \(N=0\), it is that bound directly, with no dimension-shifting steps. Criterion (C4) makes \(Z^N\) c-soft on each chart. Locality, just proved, makes it c-soft on \(Y\). We thus have the exact finite c-soft resolution

\[
0\longrightarrow Q\longrightarrow I^0\longrightarrow\cdots
\longrightarrow I^{N-1}\longrightarrow Z^N\longrightarrow0.
\tag{D10}
\]

For \(N=0\), this means that \(Q\) itself is c-soft; there are no injective middle terms. Every term is \(\Gamma_c\)-acyclic, so this resolution gives zero compact cohomology above degree \(N\). Applying the same argument to the open manifold \(U\), whose local dimensions have the same bound, proves (D8).

Every term of (D10) is also \(f_!\)-acyclic for any continuous map from \(Y\) to a locally compact Hausdorff space, by (F6). Thus the same bound gives \(R^qf_!Q=0\) for \(q>N\). This proves both dimension inputs used by the bounded c-soft and left-tail constructions below. The bound is uniform because the standing manifold dimensions are uniformly bounded; no claim of a finite global bound is made for an unbounded union of dimensions.

The compact-support, fibre, composition and dimension arguments needed for projection have now been supplied. The later adjunction section supplies the bounded-below exceptional construction and its trace. The later bounds section supplies globally bounded operation estimates. Geometric duality and constructibility remain separate obligations.


## Why projection permits arbitrary bounded coefficients {#projection-proof}

The projection isomorphism (2) is essential to both transport arguments. We prove it here for the standing manifold setting, without assuming finite generation of the coefficient complex. The resolution method is developed from Pierre Schapira's freely accessible [*An Introduction to Sheaves on Grothendieck Topologies*, 1 August 2026, §4.4](https://webusers.imj-prg.fr/~pierre.schapira/LectNotes/SHV.pdf). We give the resolution and truncation arguments explicitly; they are needed when a flat resolution has infinitely many terms to the left.

The [compact-support section](#compact-support-extension-lifting-and-acyclicity-compact-support-proof) proves injective c-softness, restriction/open-extension/coproduct stability, and the compact-cohomology criterion. The [proper-image section](#proper-support-and-the-fibre-calculation-proper-image-proof) proves the fibre formula, c-soft acyclicity for proper direct image and its required underived support compatibilities. The [composition and dimension section](#composition-and-the-uniform-dimension-bound-composition-and-dimension) proves the uniform integer bound \(H_c^j(U;Q)=0\) for \(j>n\), every open \(U\subset Y\) and every sheaf \(Q\), where \(n\) bounds the standing manifold dimensions. It also proves \(R^jf_!Q=0\) for \(j>n\). These are the topological inputs used below.

### Resolving coefficients by sums of open constant sheaves {#open-generator-resolution}

For an open subset \(U\subset X\), write \(k_U\) for its constant sheaf extended by zero to \(X\). A sum \(\bigoplus_\lambda k_{U_\lambda}\) is flat: its stalk at a point is a direct sum of copies of \(k\), and tensor exactness is detected on stalks. Such sums surject onto every sheaf \(Q\). Indeed, a section \(s\in Q(U)\) gives a map \(k_U\to Q\); take the sum over all open sets and sections. Each germ of \(Q\) lies in the image of one summand, proving stalkwise surjectivity.

The same generators give a bounded-above flat replacement of every bounded-above complex \(G^\bullet\). We include the construction because the generators need not be projective as sheaves. Suppose \(P^i\), its differential and a chain map \(u^i:P^i\to G^i\) have been constructed for \(i>q\). Form the sheaf

\[
C^q=\{(x,p)\in G^q\oplus P^{q+1}:
d_Gx=u^{q+1}p,\ d_Pp=0\}.
\tag{P1}
\]

Choose a sum of open constant sheaves \(P^q\) surjecting onto \(C^q\). Compose that epimorphism with the two projections to define \(u^q\) and \(d_P^q\). Equation (P1) gives \(d_P^2=0\) and \(d_Gu=ud_P\). Start above the upper bound of \(G\) with zero terms and repeat in descending degrees.

To verify that \(u:P\to G\) is a quasi-isomorphism, use the convention

\[
\operatorname{Cone}(u)^q=G^q\oplus P^{q+1},\qquad
d(x,p)=(d_Gx+u(p),-d_Pp).
\tag{P2}
\]

A cycle \((x,p)\) determines \((x,-p)\in C^q\). Locally it lifts to some \(z\in P^q\), by the epimorphism just chosen. Then \(d(0,z)=(x,p)\). The cone is therefore exact on stalks, which proves the claim. No lifting through a globally projective open-generator sheaf was assumed.

A bounded-above complex of flat sheaves is K-flat for the direct-sum tensor totalization used here. For completeness, its brutal truncations obtained by discarding all terms below a fixed degree are bounded subcomplexes. A bounded flat complex tensored with an exact complex is exact: filter it by its finitely many terms and use flatness and the long exact cohomology sequences of the resulting short exact sequences of complexes. The whole bounded-above flat complex is the directed union of these subcomplexes. Tensor products commute with that union, and directed colimits of sheaves of modules are exact because this can be checked on stalks. Tensoring the union with an exact complex is thus exact. This proves K-flatness and justifies using \(P\) to compute a derived tensor product.

### Removing an exact left tail before deriving {#acyclic-left-tail}

**Finite-dimension lemma.** Let \(T\) be a left exact additive functor between abelian categories with enough injectives, and assume \(R^jT=0\) for \(j>r\). Let \(C^\bullet\) be bounded above, with \(T\)-acyclic terms and bounded cohomology. Then the termwise complex \(T(C^\bullet)\) computes \(RT(C^\bullet)\).

**Proof.** Choose \(a\) such that \(H^i(C)=0\) for \(i<a\), and write \(Z^i=\ker d_C^i\). For \(i<a\), the exact left tail gives short exact sequences

\[
0\longrightarrow Z^{i-1}\longrightarrow C^{i-1}
\longrightarrow Z^i\longrightarrow0.
\tag{P3}
\]

Since the middle terms are \(T\)-acyclic, the long exact derived-functor sequences give, for \(j>0\),

\[
R^jT(Z^i)\simeq R^{j+r}T(Z^{i-r})=0.
\tag{P4}
\]

For \(r=0\), vanishing is immediate from the hypothesis; no connecting maps are required. Thus every \(Z^i\) with \(i<a\) is \(T\)-acyclic. Let \(B^a=\operatorname{im}d_C^{a-1}\). The sequence
\(0\to Z^{a-1}\to C^{a-1}\to B^a\to0\)
also makes \(B^a\) acyclic for \(T\).

Replace the entire left tail by \(B^a\) in degree \(a-1\), with its inclusion into \(C^a\). Call the resulting bounded complex \(C'\). The map \(C\to C'\), given by the quotient in degree \(a-1\) and the identity above it, is a quasi-isomorphism. Applying \(T\) preserves that quasi-isomorphism: (P3) and the last short exact sequence remain exact after applying \(T\), since their left terms are acyclic. The bounded complex \(C'\) has acyclic terms, so the usual bounded acyclic-resolution argument computes \(RT(C')\) by \(T(C')\). Hence \(T(C)\) represents the same derived object. All comparisons are induced by the specified truncation maps, so the result identifies the natural computation map. \(\square\)

The bounded acyclic-resolution argument used in the last sentence follows by filtering \(C'\) by its finitely many brutal truncations. For a single acyclic term it is the definition of acyclicity. At each additional term the short exact sequence of complexes and its derived triangle identify the two computations by the long exact cohomology sequence. Induction over the finite number of terms proves the assertion.

### A bounded c-soft model for the source input {#bounded-soft-model}

Let \(B\in D^b(k_Y)\), with cohomology in degrees \([a,b]\). Choose a bounded-below injective representative \(I^\bullet\) starting in degree \(a\). Its terms are c-soft. Put \(Z^i=\ker d_I^i\). Since the cohomology above \(b\) is zero, for every \(i\geq b\) there is an exact sequence

\[
0\longrightarrow Z^i\longrightarrow I^i\longrightarrow Z^{i+1}\longrightarrow0.
\tag{P5}
\]

Restriction to an open \(U\subset Y\) preserves these exact sequences and c-softness. Dimension shifting gives, for \(j>0\),

\[
H_c^j(U;Z^{b+n}|_U)
\simeq H_c^{j+n}(U;Z^b|_U)=0.
\tag{P6}
\]

For \(n=0\), the vanishing follows directly from the uniform compact-cohomology bound. The c-soft criterion therefore makes \(Z^{b+n}\) c-soft. Replace \(I^{b+n}\) by this kernel and discard higher degrees. This upper truncation \(A^\bullet\) is quasi-isomorphic to \(B\), has finitely many nonzero terms, and every term is c-soft. Consequently its terms are \(f_!\)-acyclic and \(f_!A\) computes \(Rf_!B\).

For an ordinary sheaf \(B\) in degree zero, this construction produces \(A\) in degrees \(0,\ldots,n\). Its terms are \(f_!\)-acyclic by the proved fibre and c-soft results. Hence \(R^jf_!B=0\) for \(j>n\). Thus the same uniform compact-cohomology bound implies finite cohomological dimension of \(f_!\); no additional dimension hypothesis on the map is needed for the left-tail lemma.

### The projection proof {#projection-arbitrary-coefficients}

Choose the bounded c-soft model \(A\) of \(B\), and an open-generator replacement \(P\to E\) for \(E\in D^b(k_X)\). Inverse image is exact and sends \(k_U\) to \(k_{f^{-1}U}\), so \(f^{-1}P\) is again a bounded-above K-flat complex. It follows that
\(A\otimes f^{-1}P\) represents \(B\otimes^Lf^{-1}E\).

Each term of that tensor total complex is a finite sum, over the degrees of \(A\), of coproducts of open extensions of c-soft sheaves. It is c-soft and hence \(f_!\)-acyclic. The complex is bounded above. Its cohomology is bounded below as well: stalkwise, the two inputs are bounded complexes of \(k\)-modules and finite global dimension bounds all Tor degrees. The finite-dimension lemma therefore proves that applying \(f_!\) termwise calculates the desired derived image even though \(P\) may have an infinite left tail.

For an individual open generator the underived projection map is

\[
f_!A^p\otimes k_U\xrightarrow{\sim}
f_!(A^p\otimes k_{f^{-1}U}).
\tag{P7}
\]

It is the compatibility of proper-support image with open restriction and extension by zero. Since \(f_!\) commutes with coproducts, (P7) holds with any \(P^q\) in place of \(k_U\). Totalization uses only finitely many terms in each degree, because \(A\) is bounded. Thus the termwise maps assemble to an isomorphism of complexes

\[
(f_!A)\otimes P\xrightarrow{\sim}f_!(A\otimes f^{-1}P).
\tag{P8}
\]

The left side represents \(Rf_!B\otimes^LE\), since \(P\) is K-flat. The right side represents \(Rf_!(B\otimes^Lf^{-1}E)\), by the preceding paragraph. This proves (2) for arbitrary bounded coefficients.

Finally, these are the canonical projection maps. Before deriving, (P7) multiplies a properly supported section by a pulled-back coefficient section. Multiplying by two coefficients consecutively is the same as multiplying by their tensor product; multiplication by the unit coefficient is the identity. Swapping homogeneous coefficients gives exactly the Koszul sign. These equalities hold termwise in (P8), commute with differentials and pass to the derived category. Hence this proof supplies the unit, associativity and symmetry compatibilities needed by the pairings (5)–(11).


## Constructing the adjunction and fixing its trace {#adjunction-construction}

We now construct the adjunction used in (1). For this construction let \(f:Y\to X\), with \(Y\) a manifold whose local dimensions are at most \(N\), and \(X\) locally compact Hausdorff. The coefficients may be any fixed commutative ring \(k\). The construction gives \(Rf_!\dashv f^!\) on \(D^+\) and a lower cohomological bound. The next section proves the additional upper bound needed to keep its output globally bounded in the standing manifold setting.

A human source for the finite-resolution method is Akhil Mathew's freely accessible [*Verdier duality*, 29 July 2011, Corollary 3.6, Lemma 3.7 and §§4.1–4.3](https://www.math.uchicago.edu/~amathew/verd.pdf). That treatment assumes Noetherian coefficients. Here we work first over \(\mathbb Z\), prove the needed tensor and generator statements, and then carry the arbitrary \(k\)-action through the construction. In particular, we do not assume that products of flat modules over an arbitrary ring are flat. The compact-support and dimension inputs are the proofs already given in this lesson.

### A finite resolution that works with every coefficient sheaf {#universal-integral-resolution}

The bound (D8), with integral coefficients, has the following consequence. Suppose an abelian sheaf \(E\) admits an exact sequence
\(0\to A\to S_{N-1}\to\cdots\to S_0\to E\to0\),
where the \(N\) middle terms are c-soft. Restrict to any open \(V\subset Y\). Repeated connecting morphisms identify \(H_c^q(V;E)\) with \(H_c^{q+N}(V;A)\) for \(q>0\). The latter vanishes. Criterion (C4) makes \(E\) c-soft. If \(N=0\), every abelian sheaf is c-soft directly by the same bound and criterion.

Consequently, if \(L\) is a flat c-soft abelian sheaf, then \(M\otimes_{\mathbb Z}L\) is c-soft for every abelian sheaf \(M\). Indeed, resolve \(M\) to the left by coproducts of open generators \(\mathbb Z_U\), choosing generators for local sections and repeating on the kernel. Flatness preserves exactness after tensoring. The resulting terms are coproducts of \(L_U\), hence c-soft by the proved support stability. Use the last \(N\) terms and the preceding dimension shift. This proof applies to the underlying abelian sheaf of a \(k\)-module, without assuming that \(k\) is flat over \(\mathbb Z\).

We construct a finite resolution of the constant integral sheaf. For an abelian sheaf \(E\), put \(C(E)(V)=\prod_{y\in V}E_y\), with restrictions deleting coordinates. This is a sheaf and is flabby, because arbitrary coordinate families extend by zero. The germ map \(E\to C(E)\) is injective. On the stalk at \(y\), evaluating the \(y\)-coordinate is a retraction: an element of \(C(E)_y\) is represented on a neighbourhood containing \(y\), so that coordinate is well defined and sends the germ of a genuine section back to itself.

If the stalks of \(E\) are torsion-free, so are the products defining \(C(E)\), their filtered stalk colimits, and the direct summands \((C(E)/E)_y\). Torsion-free abelian groups are flat: each is the filtered union of its finitely generated subgroups, which are free by integer row reduction, and filtered colimits of tensor functors preserve exactness. Thus \(C(E)\) and \(C(E)/E\) are flat whenever \(E\) is flat over \(\mathbb Z\).

Starting from \(E^0=\mathbb Z_Y\), form \(L^p=C(E^p)\) and \(E^{p+1}=L^p/E^p\) for \(0\le p<N\), and put \(L^N=E^N\). The preceding dimension shift makes the final term c-soft; the other terms are flabby. We obtain

\[
0\longrightarrow\mathbb Z_Y\longrightarrow L^0\longrightarrow\cdots
\longrightarrow L^N\longrightarrow0,
\qquad L^p\text{ flat and c-soft}.
\tag{A1}
\]

For \(N=0\), take \(L^0=\mathbb Z_Y\). Each constituent short exact sequence of (A1) splits on stalks by the coordinate retraction, so tensoring it with any sheaf preserves exactness. Hence \(M\to M\otimes_{\mathbb Z}L^\bullet\) is a quasi-isomorphism for every sheaf \(M\). It remains so for a bounded-below complex: the augmented double complex has exact finite rows in the \(L\)-direction, and in each total degree only finitely many entries occur. Successive elimination along these rows proves its total complex acyclic. Every term of the unaugmented total complex is c-soft by the tensor result. Formula (F6) and its acyclic-complex argument therefore give

\[
Rf_!G\simeq f_!\operatorname{Tot}(G\otimes_{\mathbb Z}L^\bullet)
\qquad(G\in D^+(k_Y)).
\tag{A2}
\]

### Representing the supported pairing on open sets {#supported-pairing-sheaf}

For a flat c-soft abelian sheaf \(L\), write \(T_L(M)=f_!(M\otimes_{\mathbb Z}L)\) for \(k\)-module sheaves \(M\). This functor is exact. Tensoring a short exact sequence is exact, and its c-soft terms are \(f_!\)-acyclic, so the proper-image long exact sequence proves the assertion. It also preserves coproducts, by (F4) and distributivity of tensor.

For an injective \(k_X\)-module sheaf \(I\), define

\[
J_L(I)(U)=\operatorname{Hom}_{k_X}\bigl(T_L(k_U),I\bigr)
\qquad(U\subset Y\text{ open}).
\tag{A3}
\]

The inclusion \(k_V\to k_U\) for \(V\subset U\) defines restriction. This presheaf is a sheaf: if \(U=\bigcup_iU_i\), the sequence
\(\bigoplus_{i,j}k_{U_i\cap U_j}\to\bigoplus_i k_{U_i}\to k_U\to0\)
is right exact, with the first map the difference of the two inclusions. On a stalk in \(U\), this is the presentation of one copy of \(k\) by generators indexed by cover members containing the point and relations identifying any two; outside \(U\) all terms vanish. Applying the exact coproduct-preserving \(T_L\), then \(\operatorname{Hom}(-,I)\), gives precisely the sheaf equalizer for (A3). The presentation uses coproducts of sheaves; the resulting equalizer uses products of section modules.

There is a natural bijection

\[
\operatorname{Hom}_{k_X}(T_L(M),I)
\simeq\operatorname{Hom}_{k_Y}(M,J_L(I)).
\tag{A4}
\]

Given a morphism on the left, precompose with \(T_L(k_U)\to T_L(M)\) for each local section of \(M\). The resulting compatible linear maps on sections define the morphism on the right. For \(M=k_U\) this is the identity in (A3), since \(\operatorname{Hom}(k_U,J_L(I))=J_L(I)(U)\). It is therefore a bijection for coproducts of open generators. Every \(M\) has a presentation \(P_1\to P_0\to M\to0\) by such coproducts: use all local sections to construct the first surjection and repeat for its kernel. Both sides of (A4) send that presentation to the kernel of the corresponding map from the value on \(P_0\) to the value on \(P_1\). The bijections on the two generators identify the kernels. This proves (A4) and its naturality. No projectivity of \(k_U\), or colimit formula omitting additive relations, has been used.

The left side of (A4) is exact as a contravariant functor of \(M\). Thus \(J_L(I)\) is injective. This construction is covariant in \(I\) and contravariant in \(L\), as is already visible in (A3).

### The complex and the adjunction {#exceptional-adjoint-complex}

Represent \(F\in D^+(k_X)\) by a bounded-below injective complex \(I\), and use the fixed finite resolution (A1). Define a complex \(J(I)\) by

\[
J(I)^n=\bigoplus_{p=0}^{N}J_{L^p}(I^{n+p}),
\qquad (dh)_p=d_Ih_p-(-1)^n h_{p+1}d_L^p.
\tag{A5}
\]

The last term is zero when \(p=N\). The notation means postcomposition in \(I\) and precomposition in \(L\). The two mixed terms cancel when this differential is squared, while \(d_I^2=d_L^2=0\). Every term is a finite sum of injectives, hence injective. If \(I\) starts in degree \(a\), then \(J(I)\) starts in degree \(a-N\).

Apply (A4) in each bidegree of (A2). Reindexing the Hom products is legitimate because there are only \(N+1\) possible \(p\)'s. It gives an isomorphism of Hom complexes

\[
\operatorname{Hom}^{\bullet}\!\left(
 f_!\operatorname{Tot}(G\otimes_{\mathbb Z}L),I\right)
\simeq\operatorname{Hom}^{\bullet}(G,J(I)).
\tag{A6}
\]

Here is the sign check. A degree-\(n\) map has components \(\phi_{i,p}:f_!(G^i\otimes L^p)\to I^{i+p+n}\). Its Hom differential has three terms: postcomposition by \(d_I\), minus \((-1)^n\) times precomposition by \(d_G\), and minus \((-1)^{n+i}\) times precomposition by \(d_L\). After currying, \(\phi_i\) takes values in \(J(I)^{i+n}\). Formula (A5), followed by the Hom differential for \(G\), gives these same three signs. Thus (A6) is a chain isomorphism, not only a graded bijection.

Both target complexes in (A6) are bounded-below injective complexes. Their Hom-complex degree-zero cohomology computes morphisms in \(D^+\). Together with (A2), this proves

\[
\operatorname{Hom}_{D^+(k_X)}(Rf_!G,F)
\simeq\operatorname{Hom}_{D^+(k_Y)}(G,f^!F),
\qquad f^!F=J(I),
\quad f^!D^{\ge a}\subset D^{\ge a-N}.
\tag{A7}
\]

Maps and homotopies of injective complexes induce maps and homotopies of (A5). Bounded-below injective replacements therefore make this a functor on \(D^+\); the Hom differential also gives its shift and cone compatibility. The Hom complexes themselves need not be bounded below when both inputs extend arbitrarily far to the right. The argument only uses their degree-zero cohomology and makes no such extra bound claim.

For completeness, ordinary adjunction comes from the sheaf inverse-image construction. The inverse-image presheaf is the colimit of sections over open sets containing the image, and sheafification does not change maps into a sheaf. This identifies maps \(f^{-1}A\to B\) with maps \(A\to f_*B\). Inverse image is exact, since its stalk at \(y\) is the stalk at \(f(y)\). Therefore \(f_*\) takes injectives to injectives, by its Hom test. Applying the same degreewise adjunction to a bounded-below injective replacement gives

\[
\operatorname{Hom}_{D^+(k_Y)}(f^{-1}A,B)
\simeq\operatorname{Hom}_{D^+(k_X)}(A,Rf_*B).
\tag{A8}
\]

### Units, traces and exceptional composition {#trace-and-exceptional-composition}

Let \(\eta_G:G\to f^!Rf_!G\) correspond to \(1_{Rf_!G}\) under (A7), and let \(\epsilon_F:Rf_!f^!F\to F\) correspond to \(1_{f^!F}\). The latter is the trace. Naturality of the bijection says that the transpose of \(u:Rf_!G\to F\) is \(f^!u\circ\eta_G\), and the inverse transpose of \(v:G\to f^!F\) is \(\epsilon_F\circ Rf_!v\). Apply these two inverse operations to the identity morphisms. They give

\[
\epsilon_{Rf_!G}\circ Rf_!\eta_G=1_{Rf_!G},
\qquad f^!\epsilon_F\circ\eta_{f^!F}=1_{f^!F}.
\tag{A9}
\]

If another choice of (A1) or injective representative produces a second adjoint, its counit transposes to a unique comparison with this one. Exchanging the choices produces the inverse, by (A9). The comparison preserves the trace, is natural, and satisfies the cocycle identity for three choices, since its transpose is fixed. The chain isomorphism (A6) makes this normalization compatible with shifts; there is no free choice of a sign for the shifted trace.

For \(Z\xrightarrow{g}Y\xrightarrow{f}X\), successive adjunctions and (D3) identify maps from \(G\) to \(g^!f^!F\) with maps from \(R(fg)_!G\) to \(F\). Consequently there is a unique adjoint comparison

\[
(fg)^!F\simeq g^!f^!F,
\qquad
\epsilon_{fg,F}=\epsilon_{f,F}\circ Rf_!(\epsilon_{g,f^!F}),
\tag{A10}
\]

where the source of the trace is identified by (D3) and this comparison. Indeed, the composite on the right is the inverse transpose of the identity under the successive adjunctions, which characterizes the counit on the left. With three maps, either parenthesization has this same ordered composite of traces; associativity of (D3) and uniqueness of a trace-preserving adjoint comparison make the two identifications equal. For the identity map, proper image is the identity and its adjunction has identity trace, proving the unit compatibility. The same argument with the last map \(a_X:X\to\{*\}\) gives \(f^!\omega_X\simeq\omega_Y\) for \(\omega_X=a_X^!k\), with exactly the composite trace required in the opening contracts.

These constructions supply both adjunctions and trace-compatible exceptional composition on \(D^+\). The finite model gives the lower bound in (A7); the next section proves the remaining globally bounded estimates. The tensor–Hom section below supplies explicit resolutions, currying and evaluation. The later orientation section supplies orientation identification and constant relative-ball calculations. Constructible biduality and weak-constructibility results remain explicit proof obligations. They are not inferred from existence of the adjoint.


## Why the operations remain globally bounded {#globally-bounded-operations}

Write \(N\) and \(M\) for finite upper bounds on the local dimensions of \(Y\) and \(X\), respectively. We now prove the bounds needed in the opening contracts for a continuous map \(f:Y\to X\) between the standing manifolds. Besides the lower bound in (A7), the missing ingredients are ordinary cohomology and an upper bound for exceptional inverse image.

The freely accessible human reference is Schapira's [*An Introduction to Sheaves on Grothendieck Topologies*, 1 August 2026, Proposition 5.1.2 and Proposition 5.1.9](https://webusers.imj-prg.fr/~pierre.schapira/LectNotes/SHV.pdf). We supply the ordinary-section lifting argument, the constant-interval computation and the graph factorization explicitly. For the projection bound we use supported rectangular opens and the adjunction just constructed; an orientation identification is not needed for this bound.

### From compact extension to ordinary cohomology {#ordinary-cohomology-bound}

Every standing manifold has a compact exhaustion \(K_1\subset\operatorname{int}K_2\subset\cdots\) with union the whole manifold. To construct one, start with its countable compact cover. At each stage cover the preceding compact set and the next member of that cover by finitely many relatively compact open neighbourhoods, and take the union of their compact closures. Each compact subset of a manifold is covered by finitely many coordinate charts, so the countable compact cover also gives a countable union of countable chart bases. Thus the manifold is second countable. Every open subset inherits a countable base and has a countable cover by relatively compact neighbourhoods; the same exhaustion construction applies there.

Consider a short exact sequence of sheaves \(0\to S\to E\to Q\to0\), where \(S\) is c-soft, and let \(s\in\Gamma(Y;Q)\). On every compact \(K_n\), the compact lifting result (C3), applied to the restricted sequence, lifts \(s|_{K_n}\) to a section of \(E|_{K_n}\). Make these lifts compatible inductively. If a lift \(e_n\) is already chosen, take any lift \(e'_{n+1}\) on \(K_{n+1}\). The difference \(e_n-e'_{n+1}|_{K_n}\) lies in \(S|_{K_n}\). C-softness extends that difference to a global section of \(S\); add its restriction to \(e'_{n+1}\). The corrected lift agrees with \(e_n\). The resulting sections agree on the nested interiors and glue to a global lift of \(s\). Hence

\[
\Gamma(Y;E)\longrightarrow\Gamma(Y;Q)\longrightarrow0
\quad\text{is exact when the kernel sheaf is c-soft}.
\tag{B1}
\]

A c-soft sheaf is therefore acyclic for ordinary sections on these spaces. Indeed, embed it into an injective sheaf. The quotient is c-soft by the quotient result preceding (C4); repeat. Formula (B1) makes the resulting injective resolution exact after taking ordinary sections in positive degrees. Apply this to the finite c-soft resolution (D10), and then to any open subset. For every sheaf \(Q\) on every open \(U\subset Y\), we obtain

\[
H^q(U;Q)=0\qquad(q>N).
\tag{B2}
\]

This argument concerns ordinary sections and uses the countable exhaustion. Compact-section acyclicity alone was not silently substituted for it.

For an injective resolution \(I\) of a sheaf \(Q\) on \(Y\), the stalk at \(x\) of the cohomology of \(f_*I\) is
\(\mathop{\mathrm{colim}}_{x\in V}H^q(f^{-1}V;Q)\).
Open restriction preserves injectives, and filtered colimits of modules are exact, so this is the stalk of \(R^qf_*Q\). Formula (B2) makes it zero for \(q>N\). The proper-image bound was proved in (D10). Applying the finite cohomology truncation triangles of a bounded complex now yields

\[
Rf_*D^{[a,b]}(k_Y)\subset D^{[a,b+N]}(k_X),
\qquad Rf_!D^{[a,b]}(k_Y)\subset D^{[a,b+N]}(k_X).
\tag{B3}
\]

Here each successive triangle attaches a single cohomology sheaf in its original degree; the two sheaf bounds and the long exact sequence give exactly the displayed interval. Inverse image remains exact and preserves \([a,b]\).

### Closed support and its bound {#closed-support-bound}

Let \(i:Z\hookrightarrow W\) be closed, and let \(j:W\setminus Z\hookrightarrow W\) be its open complement. The sheaf \(\Gamma_Z E\) is the kernel of \(E\to j_*j^{-1}E\). A map from \(i_*A\) to \(E\) has zero stalks off \(Z\), so lands in \(\Gamma_ZE\), and is uniquely determined by its restriction to \(Z\). Thus \(i^{-1}\Gamma_Z\) is the sheaf right adjoint to the exact functor \(i_*\). It preserves injectives. For an injective \(I\), flabbiness makes \(I(V)\to I(V\setminus Z)\) surjective for each open \(V\). Therefore
\(0\to\Gamma_ZI\to I\to j_*j^{-1}I\to0\)
is exact.

For a bounded-below injective representative of \(F\), open restriction is injective and computes the derived open image. The preceding short exact sequence of complexes gives the localization triangle

\[
i_*i^!F\longrightarrow F\longrightarrow Rj_*j^{-1}F
\longrightarrow(i_*i^!F)[1].
\tag{B4}
\]

The left term uses the derived sheaf adjunction just proved. When the exceptional adjoint (A7) applies to \(i\), uniqueness of the adjoint identifies the two constructions and their counits, since \(i_!=i_*\). This also fixes the first arrow as the support-inclusion map.

If \(W\) is a standing manifold of local dimension at most \(D\), (B3) applies to \(j\). The long exact sequence of (B4) and left exactness of the sheaf support functor give

\[
i^!D^{[a,b]}(k_W)\subset D^{[a,b+D+1]}(k_Z).
\tag{B5}
\]

Indeed, the two middle terms in (B4) vanish above \(b+D\), so the first vanishes above \(b+D+1\); its lower bound is \(a\). Exact closed direct image and restriction detect these same bounds on \(Z\). This estimate is sufficient here; it is not asserted optimal.

We also need the open restriction of an exceptional image. For an open inclusion \(u:U\hookrightarrow Y\), exact extension by zero has exact right adjoint \(u^{-1}\): the bijection follows by restricting a map out of a section extended by zero, and extending it back. It gives \(u^!=u^{-1}\). Composition (A10) consequently identifies \((fu)^!F\) with \(u^{-1}f^!F\), compatibly with the trace. The boundedness question is therefore local on the source.

### Compact cohomology of constant coefficients on boxes {#constant-box-compact-cohomology}

First, a constant sheaf on a closed interval has no positive cohomology. The case \(q>1\) was proved in (D6). For \(q=1\), its same closed-interval Mayer–Vietoris sequence has preceding map
\(k\oplus k\to k\), the difference of the values on the two intervals at their common endpoint. This map is surjective. Thus (D6) is also an isomorphism in degree one for constant coefficients. The proof following (D6) now works unchanged: a class vanishes on a small initial interval by compact-set continuity, the supremum of the zero initial intervals belongs to that set by two-interval gluing, and continuity extends beyond it unless it is the right endpoint. Hence the class is zero. Degree-zero sections are \(k\), since an interval is connected. We have proved

\[
R\Gamma([0,1];k)\simeq k.
\tag{B6}
\]

Let \(v:(0,1)\hookrightarrow[0,1]\) and let \(e:\{0,1\}\hookrightarrow[0,1]\). The sequence
\(0\to v_!k\to k_{[0,1]}\to e_*k_{\{0,1\}}\to0\)
is exact by its stalks. Compact sections on the closed interval are ordinary sections. Applying cohomology, using (B6) and the two-point calculation, gives

\[
R\Gamma_c((0,1);k)\simeq k[-1],
\qquad
0\longrightarrow k\xrightarrow{t\mapsto(t,t)}k^2
\xrightarrow{(s,t)\mapsto t-s}k\longrightarrow0.
\tag{B7}
\]

The displayed cokernel identifies the degree-one group; the other degrees vanish. Equivalently, the compact-support complex is the shifted cone of the diagonal map, with this cokernel identification. Every open interval has the same conclusion by a homeomorphism.

For finite-dimensional manifolds \(A,B\), proper base change identifies the proper image under \(A\times B\to B\) of the inverse image of \(E\in D^b(k_A)\) with the constant complex on \(B\) associated to \(R\Gamma_c(A;E)\). Apply the projection formula with \(F\in D^b(k_B)\), then compose with the map from \(B\) to a point. A second projection formula gives

\[
R\Gamma_c(A\times B;E\boxtimes^L F)
\simeq R\Gamma_c(A;E)\otimes_k^L R\Gamma_c(B;F).
\tag{B8}
\]

All operations here are the already constructed ones; (D3), (D4) and (P8) supply these maps. The standing finite global dimension keeps the tensor products bounded. For constant coefficients on a product of \(n\) open intervals, induction using (B7) gives

\[
R\Gamma_c(U;k)\simeq k[-n]
\qquad\text{for an open coordinate box }U\subset\mathbb R^n.
\tag{B9}
\]

For \(n=0\), the box is a point. For higher \(n\), tensoring the free rank-one complexes introduces no Tor groups. Only the existence of these identifications is needed for the bound below. The later orientation section identifies their transition maps, including the determinant signs.

### Projection bounds from the actual adjunction {#exceptional-projection-bound}

Let \(p:T\times X\to X\), where \(T\) is a manifold of constant dimension \(n\). For a coordinate box \(U\subset T\) and an open \(V\subset X\), proper-image composition for the open inclusions, base change and (B9) give

\[
Rp_!k_{U\times V}\simeq k_V[-n].
\tag{B10}
\]

For fixed \(U\), choose its identification in (B9) once. The resulting comparison (B10) is then natural as \(V\) shrinks; it is extension of the same constant compact-cohomology complex from \(V\).

Let \(F\in D^{[a,b]}(k_X)\). Derived sections on \(U\times V\), the adjunction (A7) and (B10) give

\[
H^q(U\times V;p^!F)
\simeq\operatorname{Hom}(Rp_!k_{U\times V},F[q])
\simeq H^{q+n}(V;F).
\tag{B11}
\]

These equalities are natural in \(V\) for fixed \(U\). To pass to a stalk at \((t,x)\), represent a class on a rectangle \(U\times V\). For any bounded-below complex \(C\), exactness of filtered colimits and the definition of a stalk give
\(\mathop{\mathrm{colim}}_{x\in V}H^j(V;C)=\mathcal H^j(C)_x\): use a bounded-below injective representative and commute the colimit with cohomology. If \(q+n\notin[a,b]\), the class corresponding under (B11) therefore becomes zero after shrinking \(V\). Naturality makes the original class zero on that smaller rectangle. Rectangles form a neighbourhood basis, so every such stalk class vanishes. This proves the sharp degree interval

\[
p^!D^{[a,b]}(k_X)\subset D^{[a-n,b-n]}(k_{T\times X}).
\tag{B12}
\]

No compatibility between orientation choices on different boxes was required for this vanishing argument. The later orientation section proves that compatibility and the global orientation-sheaf identification.

### A closed graph gives a bound for every continuous map {#exceptional-graph-bound}

Restrict \(f:Y\to X\) to a coordinate neighbourhood \(U\subset Y\) of dimension \(n\). Factor it as the graph embedding \(i:U\to U\times X\) followed by the projection \(p\). The graph is closed because \(X\) is Hausdorff: two unequal points of \(X\) have disjoint neighbourhoods, so the complement of the graph is open. The ambient manifold has local dimension at most \(n+M\).

For \(F\in D^{[a,b]}(k_X)\), (B12) places \(p^!F\) in degrees \([a-n,b-n]\). Apply (B5) to the closed graph, and use exceptional composition and open restriction. On \(U\), the resulting \(f^!F\) has cohomology only in degrees \([a-n,b+M+1]\). All chart dimensions satisfy \(n\le N\). Hence globally

\[
f^!D^{[a,b]}(k_X)\subset D^{[a-N,b+M+1]}(k_Y).
\tag{B13}
\]

The upper estimate is a uniform sufficient bound, not a proposed optimal amplitude for every map. It proves the globally bounded preservation required by the opening contracts, with no constructibility or properness restriction. Together with (B3), it closes the previously missing ordinary and exceptional operation bounds.

### A bounded injective model for the dualizing object {#bounded-dualizing-model}

Let \(d\) be the finite global dimension of \(k\). The module \(k\) has an injective resolution in degrees \(0,\ldots,d\). To see the bound, take any injective resolution and let \(Z^d\) be its \(d\)-th kernel. Dimension shifting gives \(\operatorname{Ext}^1_k(M,Z^d)=\operatorname{Ext}^{d+1}_k(M,k)=0\) for every module \(M\), the last vanishing following from a projective resolution of length at most \(d\). Thus \(Z^d\) is injective: vanishing of these extension groups makes every extension with kernel \(Z^d\) split, which, by pushing out along a map from a submodule, is exactly the extension property for injectivity. For \(d=0\), the same argument applies to \(k\) itself.

Apply the explicit construction (A5) to \(a_Y:Y\to\{*\}\) and this finite injective module resolution. It supplies a representative \(W_Y\) of \(\omega_Y\) with

\[
W_Y^q=0\quad(q\notin[-N,d]),
\qquad W_Y^q\text{ injective as a }k_Y\text{-module sheaf}.
\tag{B14}
\]

For \(F\in D^{[a,b]}(k_Y)\), choose its good-truncated representative in degrees \([a,b]\). The internal Hom complex \(\mathcal Hom^\bullet(F,W_Y)\) computes \(D_YF\). In detail, restriction of an injective sheaf to any open remains injective, so \(\mathcal Hom(-,W_Y^q)\) is exact as a contravariant sheaf functor. On each open its sections are the usual Hom into that injective restriction. The finite Hom totalization consequently sends bounded acyclic source complexes to acyclic complexes and computes the derived internal Hom into the chosen injective target. Its term in degree \(r\) is a finite product of \(\mathcal Hom(F^i,W_Y^{i+r})\); all such terms vanish outside the interval

\[
D_YD^{[a,b]}(k_Y)\subset D^{[-N-b,d-a]}(k_Y).
\tag{B15}
\]

This proves boundedness of duality for arbitrary bounded sheaves, without assuming biduality, finite rank or constructibility. Identifying \(\omega_Y\) with the shifted orientation sheaf, and proving when evaluation is an isomorphism, remain separate matters. The next section proves the tensor–Hom and evaluation statements on explicit models. The following orientation section proves the orientation and constant relative-ball statements. Biduality and constructibility retain their separate proof obligations.


## Tensor–Hom adjunction and the actual evaluation map {#tensor-hom-foundations}

We now supply the complex models behind the remaining algebraic operation contract. Put \(d=\operatorname{gldim}k\). This section uses bounded complexes for the lesson's inputs and bounded-below injective resolutions for their targets. No perfectness or finite generation is imposed. Schapira's freely accessible [*An Introduction to Sheaves on Grothendieck Topologies*, §§2.1–2.3, pp. 43–45 and 49–53](https://webusers.imj-prg.fr/~pierre.schapira/LectNotes/SHV.pdf) supplies the tensor and internal-Hom statements used for comparison. The constructions below include the injective replacement, the finite flat truncation and the evaluation signs needed here.

### Constructing enough injectives {#explicit-injective-models}

We first justify the injective resolutions used above. The abelian group \(\mathbb Q/\mathbb Z\) is divisible and injective. Here is the extension argument. For a homomorphism defined on a subgroup \(A\subset B\), choose a maximal extension by the union-of-chains form of Zorn's lemma. If its domain omits \(b\in B\), the set of integers \(n\) with \(nb\) in that domain is an ideal \(m\mathbb Z\). If \(m=0\), assign any value to \(b\). If \(m>0\), divisibility supplies a value whose \(m\)-fold multiple is the prescribed value on \(mb\). In either case the rule extends consistently to the subgroup generated by the domain and \(b\), a contradiction. This proves injectivity. It is also a cogenerator: a nonzero element generates a finite or infinite cyclic subgroup admitting a character into \(\mathbb Q/\mathbb Z\) nonzero on that element, and injectivity extends the character to the whole group.

Give \(E=\operatorname{Hom}_{\mathbb Z}(k,\mathbb Q/\mathbb Z)\) its \(k\)-action \((s\varphi)(r)=\varphi(sr)\). The mutually inverse operations of evaluation at \(1\) and \(\chi\mapsto[m\mapsto(r\mapsto\chi(rm))]\) give

\[
\operatorname{Hom}_k(M,E)
\simeq\operatorname{Hom}_{\mathbb Z}(M,\mathbb Q/\mathbb Z),
\qquad
M\hookrightarrow
E^{\operatorname{Hom}_{\mathbb Z}(M,\mathbb Q/\mathbb Z)}.
\tag{H1}
\]

The first functor is exact, so \(E\) is injective. The second map has component \(m\mapsto(r\mapsto\chi(rm))\); the cogenerator property makes it injective. Products of injectives are injective, since a map into a product extends component by component. Thus (H1) constructs an injective module \(J(M)\) containing each \(M\).

For a point inclusion \(i_x:\{x\}\to X\), the skyscraper \(i_{x*}J\) is injective when \(J\) is: maps into it are maps from the exact stalk functor into \(J\). Consequently every sheaf \(F\) has a monomorphism

\[
F\longrightarrow\prod_{x\in X}i_{x*}J(F_x).
\tag{H2}
\]

The component at \(x\), followed by taking its stalk at \(x\), is the chosen injection of \(F_x\). This proves monicity without assuming that stalks commute with infinite products. The product on the right is injective by the same componentwise extension argument. Repeating on cokernels gives an injective resolution of a sheaf. This construction also supplies the injective modules invoked in (B14).

There is an explicit replacement for a bounded-below complex \(C\), say \(C^n=0\) for \(n<a\). Set \(I^n=0\) below \(a\) and embed \(C^a\) into an injective \(I^a\), defining \(f^a\). Suppose \(f\) and \(d_I\) have been defined through degree \(n\). Form the quotient sheaf

\[
Q^{n+1}=
\frac{I^n\oplus C^{n+1}}
{\operatorname{im}\bigl[(u,c)\mapsto
(d_Iu+f^nc,-d_Cc)\bigr]},
\quad (u,c)\in I^{n-1}\oplus C^n.
\tag{H3}
\]

Embed \(Q^{n+1}\) in an injective \(I^{n+1}\). The classes of \((u,0)\) and \((0,c)\) define \(d_I^nu\) and \(f^{n+1}c\). The relations in (H3) give \(d_I^2=0\) and \(d_If=fd_C\). To prove that \(f:C\to I\) is a quasi-isomorphism, use the cone with differential \((u,c)\mapsto(d_Iu+fc,-d_Cc)\). In degree \(n\), its first output component is the composite of the quotient to \(Q^{n+1}\) and an injection. A cone cycle therefore lies in the preceding image; conversely that image consists of cycles because the differential squares to zero. At degree \(a-1\) exactness is the initial injection. This proves exactness of the whole cone on stalks and hence the claim.

We also need the homotopy property, not just existence. Every chain map \(t:A\to I\) from an acyclic complex to a bounded-below complex of injectives is null-homotopic. Construct \(h^n:A^n\to I^{n-1}\) in ascending degrees. Below the lower bound of \(I\) take zero. Once the previous step is fixed, the residual \(t^n-d_Ih^n\) vanishes on \(\ker d_A^n=\operatorname{im}d_A^{n-1}\), by the chain-map equation and the preceding homotopy equation. It therefore defines a map from \(\operatorname{im}d_A^n\) into \(I^n\). Injectivity extends it to \(A^{n+1}\); take that extension as \(h^{n+1}\). Induction gives

\[
t=d_Ih+hd_A.
\tag{H4}
\]

Applying this to shifts shows that the global Hom complex \(\operatorname{Hom}^\bullet(A,I)\) is acyclic. Thus precomposition with a quasi-isomorphism induces an isomorphism on homotopy classes of maps into \(I\): its cone is acyclic, and the Hom cone has zero cohomology. A roof in the derived category with target \(I\) consequently has a unique representing homotopy class from its left endpoint. This proves that maps into \(I\) in the homotopy and derived categories agree. In particular, two such resolutions of the same object have comparison maps inverse up to homotopy, with their classes uniquely determined by the resolution maps.

### Flat models of finite length {#finite-flat-models}

For sheaves \(F,G\), define \(F\otimes G\) by sheafifying the presheaf tensor product. Define \(\mathcal Hom(F,G)(U)=\operatorname{Hom}(F|_U,G|_U)\). Compatible local maps glue uniquely, so this is a sheaf. A map out of a tensor is a locally bilinear map; currying that map and gluing gives

\[
\operatorname{Hom}(A\otimes B,C)
\simeq\operatorname{Hom}(A,\mathcal Hom(B,C)).
\tag{H5}
\]

The same argument on every open gives the internal version. Tensor exactness is stalkwise exactness. In particular, the open-generator resolutions (P1)–(P2) have flat terms with free stalks and are K-flat by the proof there.

Let \(B\) have cohomology in \([a,b]\). The elementary good truncations give a representative zero outside that interval: at the lower edge quotient by incoming boundaries, and at the upper edge take outgoing cycles. Resolve it by (P1), obtaining \(P\to B\) with \(P^i=0\) for \(i>b\). Write \(C^i=\operatorname{coker}(P^{i-1}\to P^i)\). Exactness below \(a\) gives \(0\to C^i\to P^{i+1}\to C^{i+1}\to0\) for \(i<a\). The stalk \(C^{a-d}_x\) is therefore a \(d\)-th syzygy of \(C^a_x\) through projective modules. It is projective, because every \(k\)-module has projective dimension at most \(d\).

For clarity, the last assertion does not require these sheaves themselves to be projective. Given two projective presentations of a module, the fibre product of their epimorphisms projects onto each projective term. Splitting these two projections identifies it both with \(K\oplus P'\) and with \(K'\oplus P\), where \(K,K'\) are the two kernels. Repeat this comparison through \(d\) stages against a projective resolution of length \(d\). It identifies the proposed \(d\)-th syzygy, after adding projective summands, with a projective module; hence that syzygy is a direct summand of a projective module and is projective. For \(d=0\), all modules are already projective.

Thus \(C^{a-d}\) is a flat sheaf. Quotient the left end of \(P\) to obtain

\[
P_{\mathrm{fin}}=
[\,C^{a-d}\longrightarrow P^{a-d+1}\longrightarrow\cdots
\longrightarrow P^b\,],
\qquad P\longrightarrow P_{\mathrm{fin}}\simeq B.
\tag{H6}
\]

The displayed quotient map is a quasi-isomorphism, since the removed degrees are exact and its boundary quotient preserves the remaining cohomology. The final identification in (H6) is in the derived category; a chain map from the quotient to the originally chosen representative is not being presumed. All terms are flat. This gives finite flat models for every bounded coefficient complex, including arbitrary infinite coefficients. In particular, tensoring inputs in \([a,b]\) and \([c,e]\) produces cohomology in \([a+c-d,b+e]\), by using (H6) for the first and a bounded representative for the second.

### Currying on complexes and passage to the derived category {#derived-currying-proof}

Use the cochain conventions

\[
\begin{aligned}
d(a\otimes b)&=d_Aa\otimes b+(-1)^{|a|}a\otimes d_Bb,\\
\mathcal Hom^n(A,C)&=\prod_p\mathcal Hom(A^p,C^{p+n}),\\
(dh)(a)&=d_Ch(a)-(-1)^{|h|}h(d_Aa).
\end{aligned}
\tag{H7}
\]

For bounded-above inputs and a bounded-below target all products contributing to any one degree here are finite. The curried map \(\alpha:A\to\mathcal Hom(B,C)\) and its uncurried map are related by \(\widetilde\alpha(a\otimes b)=\alpha(a)(b)\), with no sign for this order of factors. For \(|\alpha|=n\) and \(|a|=p\), both differentials evaluate to

\[
d_C\alpha(a)(b)-(-1)^n\alpha(d_Aa)(b)
-(-1)^{n+p}\alpha(a)(d_Bb).
\tag{H8}
\]

This proves the isomorphism of Hom complexes, including its signs, and the identical calculation on each open proves the internal isomorphism. The tensor associator and unit act by their ordinary formulas. The symmetry is \(a\otimes b\mapsto(-1)^{|a||b|}b\otimes a\); substituting (H7) checks that it commutes with the differential. The associativity and symmetry coherence identities follow on a pure tensor: regrouping preserves the order, and swapping a homogeneous entry past two others has exponent \(p(q+r)=pq+pr\). These identities hold on local sections and hence on sheaves.

Two elementary injectivity observations allow these formulas to compute derived functors. An injective sheaf remains injective on an open subset: extension by zero is its exact left adjoint, as is seen on stalks. Thus \(\mathcal Hom(-,I)\) is exact when \(I\) is injective, by applying injectivity on every open. Also \(\mathcal Hom(F,I)\) is injective for a flat \(F\), since (H5) expresses maps into it as the composite of exact tensoring with \(F\) and exact contravariant Hom into \(I\).

It follows that \(\mathcal Hom(P,I)\), for bounded-above flat \(P\) and bounded-below injective \(I\), is a bounded-below complex of injective sheaves. In each degree only finitely many terms occur. For any acyclic \(A\), (H4) applied on every open shows that \(\mathcal Hom(A,I)\) is acyclic: restriction preserves acyclicity of \(A\) and the bounded-below complex of injectives \(I\). Consequently \(\mathcal Hom(B,I)\) computes \(R\mathcal Hom(B,C)\) when \(I\) resolves \(C\), and replacing a bounded-above \(B\) by \(P\) gives a quasi-isomorphic injective model.

These constructions are independent of the choices. For injective targets this follows from the unique homotopy classes proved after (H4). For tensor, resolve roofs by (P1) and use K-flatness: tensoring a quasi-isomorphism with a K-flat complex preserves its acyclic cone. Resolving the middle object of a roof gives a roof between flat models, so the localization on flat models computes the same derived category of bounded-above objects. All tensor comparison maps and their composites are therefore the ordinary ones on these roofs. Finite models (H6) can be substituted through their explicit quasi-isomorphisms.

Take bounded-above flat models \(P_A,P_B\) and a bounded-below injective \(I_C\). Currying (H8) identifies the two Hom complexes; its inner Hom is a bounded-below injective model. Passing to homotopy classes and then using (H4) proves

\[
\begin{aligned}
\operatorname{Hom}_{D(X)}(A\otimes^L B,C)
&\simeq\operatorname{Hom}_{D(X)}(A,R\mathcal Hom(B,C)),\\
R\mathcal Hom(A\otimes^L B,C)
&\simeq R\mathcal Hom(A,R\mathcal Hom(B,C)).
\end{aligned}
\tag{H9}
\]

The first line is computed by global sections of the corresponding Hom complexes; the second uses their equality as sheaf complexes. In the lesson all inputs are bounded, and (H6) supplies bounded tensor products. The target of an internal Hom in (H9) is allowed to be bounded below; no assertion that arbitrary internal Hom preserves boundedness is needed. For duality its stronger boundedness was proved using the special model (B14).

The same injective Hom model proves \(R\operatorname{Hom}(A,C)=R\Gamma(X;R\mathcal Hom(A,C))\): global sections of \(\mathcal Hom(P_A,I_C)\) compute both sides. Here \(R\operatorname{Hom}\) means the complex of global derived morphisms. Naturality in all the variables follows already from evaluation on local sections, so the isomorphisms identify actual adjunction maps. Inverse image is exact and sends the stalk of a tensor to the tensor of the stalks. The resulting natural monoidal isomorphism preserves flat models and the symmetry, associator and unit just checked. Thus pullbacks use these same conventions.

### Evaluation, units and the double-dual identity {#evaluation-sign-proof}

For the order \(\mathcal Hom(B,C)\otimes B\), evaluation is \(h\otimes b\mapsto h(b)\). Formula (H7) verifies that it is a chain map. For the adjunction \(-\otimes B\dashv\mathcal Hom(B,-)\), its unit sends \(a\) to the map \(b\mapsto a\otimes b\). Evaluating this unit returns \(a\otimes b\); applying the unit to a Hom and then postcomposing with evaluation returns \(h\). These are the two triangle identities on complexes. Replacing the inputs as above proves them for the derived adjunction as well. Likewise composition of homogeneous maps is \((g,h)\mapsto g\circ h\), with differential \(d(gh)=(dg)h+(-1)^{|g|}g(dh)\). Evaluation of its transpose is \(g(h(a))\), so it is associative and natural, with the identity maps as units.

Fix the bounded injective model \(W\) for \(\omega_X\) from (B14). If \(A\) is a bounded representative, write \(D_WA=\mathcal Hom(A,W)\). This complex is bounded and represents \(D_XA\). It can therefore be used again as the input of the same Hom model. The map (3) is represented by

\[
\eta_A(a)(h)=(-1)^{|a||h|}h(a),
\qquad
\eta_A:A\longrightarrow D_WD_WA.
\tag{H10}
\]

The sign comes from moving \(a\) past \(h\) before evaluation. Explicitly, for \(|a|=p\), \(|h|=q\), the differential of this double-Hom expression is

\[
\begin{aligned}
(d\eta_A(a))(h)
&=(-1)^{pq}d_Wh(a)
-(-1)^p(-1)^{p(q+1)}(dh)(a)\\
&=(-1)^{(p+1)q}h(d_Aa)
=\eta_A(d_Aa)(h).
\end{aligned}
\tag{H11}
\]

Thus (H10) is a chain map. Although the ordinary tensor product with \(A\) need not compute a derived tensor product, its evaluation gives the derived evaluation after flat replacement. Currying that pairing gives exactly (H10), by naturality of the replacement and (H8). No flatness of \(A\) or of \(D_WA\) is required here.

For a degree-zero chain map \(u:A\to A'\), evaluation on \(a,h\) gives \(D_WD_W(u)\eta_A=\eta_{A'}u\). Since \(D_W\) sends quasi-isomorphisms between bounded complexes to quasi-isomorphisms, this equality descends to all derived morphisms represented by roofs. Finally, for homogeneous \(h\in D_WA\), precomposition with \(\eta_A\) gives

\[
\bigl(D_W\eta_A\circ\eta_{D_WA}\bigr)(h)(a)
=(-1)^{|h||a|}\eta_A(a)(h)
=h(a).
\qquad D_X\eta_A\circ\eta_{D_XA}=1_{D_XA}.
\tag{H12}
\]

Both signs have the same exponent and cancel. This is the double-evaluation identity used below. It holds without assuming that either evaluation map is an isomorphism. The comparison and evaluation-obstruction arguments therefore have the tensor–Hom adjunction, naturality and triangle identities they require. The next section identifies orientation transition maps and proves the constant relative-ball comparisons. Constructible biduality and weak-constructibility statements retain their separate prerequisite chains.

## From local compact classes to orientation and duality {#orientation-and-local-support}

We identify the orientation object and its actual transition maps before using constructible biduality. The free reference is Schapira's [*An Introduction to Sheaves on Grothendieck Topologies*, Lemma 5.1.3 and Proposition 5.1.5, pp. 106–107](https://webusers.imj-prg.fr/~pierre.schapira/LectNotes/SHV.pdf). That treatment states the orientation identification and refers elsewhere for the differentiable-coordinate comparison. Here we prove the local-support comparison, the signs of coordinate changes and the normalization by trace. These arguments use the compact-support and algebraic constructions already supplied above.

### Homotopy invariance from a proper interval {#proper-interval-homotopy}

Let \(T\) be a locally compact Hausdorff space occurring below, and put \(q:T\times[0,1]\to T\). The map \(q\) is proper. For a bounded complex of coefficient modules \(M\), the actual unit is an isomorphism

\[
M_T\longrightarrow Rq_*M_{T\times[0,1]}.
\tag{O1}
\]

Here the auxiliary spaces include closed balls and closed interval cylinders. The compact-neighbourhood and fibre arguments (C1), (F1)–(F3) and (D5) apply to these spaces: their proofs require local compactness and the Hausdorff property, not the absence of boundary. One can check (O1) directly without an additional manifold theorem. Represent the sheaf input by injectives. The stalk of its direct-image complex is the filtered colimit of sections on inverse images of neighbourhoods of \(t\). Properness makes these neighbourhoods cofinal among neighbourhoods of the compact fibre. Compact-germ continuity identifies that complex with sections of the restricted injective resolution on the fibre. Injectives are flabby and c-soft, their restrictions to the compact fibre are c-soft, and hence these restricted terms are acyclic for its sections, by (C3). Thus the stalk computes the fibre cohomology. For \(M\) a module, (B6), whose proof applies to any constant module, identifies the stalk of the unit with \(M\to R\Gamma([0,1];M)\), an isomorphism. Finite truncation triangles give (O1) for bounded \(M\).

The two endpoint restrictions are inverses to (O1), because their composites with the unit are the identity. A continuous map \(g:S\to T\) gives the usual pullback of constant-coefficient cohomology by the unit for \(g^{-1}\dashv Rg_*\); these maps compose by ordinary adjunction. Applying this to a homotopy \(g:S\times[0,1]\to T\) proves

\[
g_0^*=g_1^*:R\Gamma(T;M_T)\longrightarrow R\Gamma(S;M_S).
\tag{O2}
\]

If \(g\) is proper, the same equality holds for compactly supported cohomology: proper pullback preserves compact support, \(q_*=q_!\), and applying \(R\Gamma_c\) to (O1) and proper-image composition makes both endpoint maps inverse to the same isomorphism. For a homotopy of pairs \((S,A)\to(T,B)\), apply the ordinary argument simultaneously to the two restriction maps and take their fibres. It proves homotopy invariance of relative sheaf cohomology as well. We use this for open complements of a point; no properness of a contraction is needed for the ordinary or relative statement.

### The actual point-to-compact comparison {#point-to-compact-comparison}

Let \(V=\mathbb R^n\), let \(x\in V\), and let \(M\in D^b(k)\). Contraction of \(V\) to \(x\), using (O2), proves that the constant-section map and evaluation at \(x\) are inverse isomorphisms. The compact calculation (B7)–(B9), with the coefficient projection formula, gives the other end of

\[
R\Gamma(V;M_V)\simeq M,
\qquad
R\Gamma_{\{x\}}(V;M_V)
\longrightarrow R\Gamma_c(V;M_V).
\tag{O3}
\]

We prove that the displayed support-forgetting map is an isomorphism. Translate \(x\) to zero. For a closed ball \(K_r\) of radius \(r>0\), inclusion \(V\setminus K_r\to V\setminus\{0\}\) is a homotopy equivalence: choose a radius \(R>r\), and deform both spaces radially onto the sphere of radius \(R\). The formula sends \(v\ne0\) at time \(t\) to \(((1-t)+tR/\lVert v\rVert)v\); if \(\lVert v\rVert>r\), its radius stays greater than \(r\). These retractions and inclusions supply inverse homotopy classes. Equation (O2) therefore makes restriction between the two complement cohomologies an isomorphism.

The closed-support localization triangles have the same middle term \(R\Gamma(V;M_V)\). The complement isomorphism just proved gives

\[
R\Gamma_{\{0\}}(V;M_V)
\xrightarrow{\sim} R\Gamma_{K_r}(V;M_V)
\longrightarrow R\Gamma_c(V;M_V).
\tag{O4}
\]

Closed balls are cofinal among compact subsets of \(V\). Compact sections of an injective resolution are the filtered union of its sections with compact closed support. Filtered colimits are exact, so passage to that union proves that the second map in (O3) is an isomorphism too. This establishes the actual map, naturally in \(M\), rather than choosing an abstract identification of the groups. For \(n=0\), all spaces are a point and the assertion is immediate.

Excision for point supports follows directly by restriction and extension by zero: a section supported at a point inside an open neighbourhood is zero near its boundary, so these operations are inverse; the same calculation on injective restrictions proves the derived assertion. Consequently (O3) holds on every open coordinate ball, for any point in it. If two such balls satisfy \(U'\subset U\) and contain \(x\), the maps from the common point-supported complex to their compact-section complexes commute with extension from \(U'\) to \(U\). All three comparisons are isomorphisms. In particular, extension between the compact-cohomology groups of nested coordinate balls is an isomorphism with a specified geometric normalization.

### The integral sign line {#integral-orientation-line}

Work first on a component of dimension \(n\). Define \(o_X^{\mathbb Z}\) as the sheafification of the presheaf

\[
U\longmapsto
\operatorname{Hom}_{\mathbb Z}(H_c^n(U;\mathbb Z),\mathbb Z),
\tag{O5}
\]

whose restrictions are dual to extension of compact supports. On a coordinate ball the compact group is free of rank one, by (B9) over \(\mathbb Z\). The preceding point-support comparison makes all restrictions to smaller coordinate balls isomorphisms. A chart itself can be taken to be a ball; its chosen generator therefore trivializes (O5) on a basis inside that chart. Hence the sheaf is locally constant of rank one. On a connected overlap, any two integral bases differ by \(+1\) or \(-1\), since these are the units of \(\mathbb Z\); on a disconnected overlap this assertion holds locally.

Set \(o_X=k_X\otimes_{\mathbb Z}o_X^{\mathbb Z}\). The interval boundary calculation is natural in its coefficient module: changing \(\mathbb Z\) to \(k\) sends the endpoint difference generator to its \(k\)-valued counterpart. Iteration in ordered coordinates gives the same assertion on boxes. Excision and (O3) then give it on coordinate balls with their restriction maps. Thus sheafifying \(U\mapsto\operatorname{Hom}_k(H_c^n(U;k),k)\) gives precisely \(o_X\), including rings of positive characteristic. No claim that dualization commutes with arbitrary change of coefficients is used; the local groups in this comparison are free of rank one.

There is a canonical square pairing on the integral line: for either generator \(e\), send \(e\otimes e\) to \(1\). Changing both signs preserves that rule, so it glues. After change of coefficients it gives

\[
o_X\otimes_k o_X\simeq k_X,
\qquad o_X^\vee:=\mathcal Hom_k(o_X,k_X)\simeq o_X.
\tag{O6}
\]

These tensors and Homs are already exact locally because the line is free. The self-duality uses the integral sign structure; it is not asserted for every rank-one \(k\)-local system. The dual line \((o_X)_x^\vee\) identifies canonically with \(H^n_{\{x\}}(X;k)\), by (O3) and the evaluation pairing of that free local group with its dual.

### Coordinate changes and their signs {#orientation-coordinate-signs}

The ordered coordinate generator of \(H_c^n(\mathbb R^n;\mathbb Z)\) is the external product of the increasing-interval classes from (B7). In one dimension a positive rescaling preserves the endpoint order, so it preserves the generator. Reflection exchanges the endpoints and sends their difference to its negative. A swap of two coordinates exchanges two degree-one factors in (B8); the tensor symmetry (H7) therefore contributes \(-1\). These assertions concern the actual pullback maps and the same ordered product generator.

An elementary shear \(x_i\mapsto x_i+t x_j\), \(i\ne j\), is properly homotopic to the identity as \(t\) varies over a compact interval. Indeed its inverse is \(x_i\mapsto x_i-tx_j\), which sends a bounded set into a uniformly bounded set; the inverse image of a compact set is also closed and is therefore compact in \(\mathbb R^n\times[0,1]\). Proper homotopy invariance from (O2) makes its action the identity. Gaussian elimination expresses an invertible real matrix using these shears, swaps and nonzero rescalings: choose a nonzero pivot in each remaining column, swap it into place, rescale it and clear its column, then continue on the remaining square block. Multiplying the actions of these elementary operations proves

\[
A^*=\operatorname{sgn}(\det A)
\quad\text{on }H_c^n(\mathbb R^n;\mathbb Z),
\qquad A\in\operatorname{GL}_n(\mathbb R).
\tag{O7}
\]

Point-support comparison gives the same formula on local cohomology at zero.

Now let \(h\) be a \(C^1\) change of coordinates fixing zero, with \(A=Dh(0)\) invertible. Shrink a ball about zero so that differentiability gives \(\lVert A^{-1}h(v)-v\rVert<\tfrac12\lVert v\rVert\) for \(v\ne0\) in it. For

\[
h_t(v)=(1-t)Av+t h(v),
\qquad
\lVert A^{-1}h_t(v)\rVert>\tfrac12\lVert v\rVert
\quad(v\ne0),
\tag{O8}
\]

we have a homotopy of maps of pairs into \((\mathbb R^n,\mathbb R^n\setminus\{0\})\). Intermediate maps need only avoid zero away from zero; their invertibility is unnecessary. Relative homotopy invariance and excision identify the local-cohomology actions of \(h\) and \(A\). Thus the transition in (O5), and its dual, is multiplication by \(\operatorname{sgn}\det Dh(0)\). Repeat at every point of an overlap. The determinant is continuous and never zero, so its sign is locally constant. This proves that the sign line just constructed is the usual orientation sheaf for the real analytic manifolds of this lesson.

### Identifying the dualizing object and its trace {#orientation-dualizing-trace}

The projection estimate (B12), applied locally to the map to a point, shows that \(\omega_X\) has only degree \(-n\) on an \(n\)-dimensional component. Put \(L=\mathcal H^{-n}(\omega_X)\). Good truncation gives the canonical isomorphism \(\omega_X\simeq L[n]\). On any coordinate ball \(U\), adjunction and (B9) identify

\[
\begin{aligned}
\Gamma(U;L)
&=H^{-n}(U;\omega_X)\\
&=\operatorname{Hom}_{D(k)}(R\Gamma_c(U;k),k[-n])\\
&=\operatorname{Hom}_k(H_c^n(U;k),k).
\end{aligned}
\qquad \omega_X\simeq o_X[n].
\tag{O9}
\]

The maps as \(U\) shrinks are dual to compact-support extension, because the adjunction was constructed from that extension on open generators. Thus (O9) identifies the actual sheaf \(L\) with (O5) after change of coefficients, not merely their stalk ranks. It also identifies the actual maps on overlaps with the signs proved in (O8). On manifolds with components of different dimensions the formula is read componentwise, with the standing uniform bound.

The adjunction specifies the trace. Let \(c_U\) be an integral compact generator, extended to \(k\), and let \(e_U\) be its dual local orientation section. In the order with the dualizing section first, the pairing obtained from compact-support projection and the trace is

\[
R\Gamma(U;\omega_U)\otimes_k^L R\Gamma_c(U;k)
\longrightarrow k,
\qquad e_U\otimes c_U\longmapsto1.
\tag{O10}
\]

Indeed (O9) is the adjunction map taking that section to its functional on compact cohomology. Its inverse reconstructs exactly the same pairing by the counit. This proves the normalization, including compatibility with smaller balls and extension of compact supports. Both generators change sign when the orientation changes, so the pairing is unchanged. Their cohomological degrees are \(-n\) and \(n\); reversing their order uses the Koszul sign \((-1)^n\). Formula (O10) fixes the order and avoids concealing that sign in an unnamed identification of shifted lines.

### Constant coefficients on relative balls {#constant-relative-balls}

Let \(i_x:\{x\}\to X\), and suppose a bounded coefficient complex is constant, \(M_U\), on a coordinate ball around \(x\). Closed-support adjunction (B4), excision and (O3) give the natural identification

\[
i_x^!M_U
\simeq R\Gamma_{\{x\}}(U;M_U)
\xrightarrow{\sim} R\Gamma_c(U;M_U)
\simeq M\otimes_k (o_X)_x^\vee[-n].
\tag{O11}
\]

The final expression puts the coefficient first. It uses the projection formula and the symmetry fixed in (H7); moving a degree-\(p\) coefficient past the degree-\(n\) compact class has sign \((-1)^{np}\). The line is free, so no Tor correction or finite-rank assumption on \(M\) is needed. All maps are natural in \(M\) and in shrinking balls, by the actual support maps in (O3)–(O4).

There is also a closed-ball description with its boundary map retained. For a closed coordinate ball \(\overline B\) about \(x\), let \(B\) be its interior and \(S\) its boundary. Write relative sheaf cohomology as the fibre of restriction. The exact sequence of constant sheaves and their extensions gives

\[
\begin{aligned}
R\Gamma(\overline B,S;M)
&:=\operatorname{Cone}\bigl(R\Gamma(\overline B;M)
\longrightarrow R\Gamma(S;M)\bigr)[-1]\\
&\simeq R\Gamma_c(B;M)
\simeq M\otimes_k(o_X)_x^\vee[-n].
\end{aligned}
\tag{O12}
\]

To verify the first isomorphism, apply sections on the compact \(\overline B\) to \(0\to j_!M_B\to M_{\overline B}\to i_*M_S\to0\), degree by degree and then to its bounded total complex. Stalks prove this sequence exact. Open proper-image composition identifies its first derived-section term with \(R\Gamma_c(B;M)\). Thus the displayed relative map is the localization boundary with the cone convention already fixed in (P2). For \(n=1\) it is the endpoint difference \((s,t)\mapsto t-s\) of (B7). For \(n=0\) the boundary is empty and the result is \(M\) in degree zero. Formula (O12) is a statement about relative sheaf cohomology; it does not silently import a comparison with a chosen singular or cellular cochain model.

The orientation and constant local-support calculations apply to arbitrary bounded constant coefficients and retain the transition signs and trace normalization. [Small balls, central fibres and supported cohomology](../sheaf-proof-readings/src/SH03/small-balls-central-fibres-and-supported-cohomology.md#scalar-endpoint-proof) uses these foundations in its scalar endpoint, closed-support and compact-support comparisons. Its geometric input comes from [proper cotangent transport](../sheaf-proof-readings/src/SH03/isotropic-cotangent-transport-and-discrete-critical-values.md#proper-direct-transport). The constructible applications below also use perfect compact cohomology, local dual pairings and constructible biduality, as listed in the prerequisites.


## Transporting a pairing through a map {#transport}

There are two comparisons which require no constructibility:

\[
u_E:f^!D_XE\xrightarrow{\sim}D_Yf^{-1}E,
\qquad
b_B:Rf_*D_YB\xrightarrow{\sim}D_XRf_!B.
\tag{4}
\]

Here is a proof of both from the operation contracts. It also specifies the actual maps.

For a bounded test object \(T\) on \(Y\), compute

\[
\begin{aligned}
\operatorname{Hom}_Y(T,f^!D_XE)
&\simeq\operatorname{Hom}_X(Rf_!T,D_XE)\\
&\simeq\operatorname{Hom}_X(Rf_!T\otimes E,\omega_X)\\
&\simeq\operatorname{Hom}_X(Rf_!(T\otimes f^{-1}E),\omega_X)\\
&\simeq\operatorname{Hom}_Y(T\otimes f^{-1}E,\omega_Y)\\
&\simeq\operatorname{Hom}_Y(T,D_Yf^{-1}E).
\end{aligned}
\tag{5}
\]

Every step is natural in \(T\) and \(E\). The first and fourth use proper-support adjunction, the middle step uses (2), and the remaining steps curry a pairing. Yoneda therefore gives the first isomorphism in (4). Its uncurried pairing is

\[
f^!D_XE\otimes f^{-1}E
\longrightarrow f^!(D_XE\otimes E)
\longrightarrow f^!\omega_X=\omega_Y.
\tag{6}
\]

The first arrow in (6) is obtained by taking the right-adjunction mate of projection followed by the counit \(Rf_!f^!D_XE\to D_XE\). This describes it without assuming an internal exceptional-Hom theorem. Tracing the identity map through (5) yields precisely (6), so (5) proves invertibility of the designated comparison.

For a bounded test object \(A\) on \(X\), a second computation gives

\[
\begin{aligned}
\operatorname{Hom}_X(A,Rf_*D_YB)
&\simeq\operatorname{Hom}_Y(f^{-1}A,D_YB)\\
&\simeq\operatorname{Hom}_Y(f^{-1}A\otimes B,\omega_Y)\\
&\simeq\operatorname{Hom}_X(Rf_!(f^{-1}A\otimes B),\omega_X)\\
&\simeq\operatorname{Hom}_X(A\otimes Rf_!B,\omega_X)\\
&\simeq\operatorname{Hom}_X(A,D_XRf_!B).
\end{aligned}
\tag{7}
\]

Ordinary adjunction enters in the first step; proper-support adjunction enters in the third. Naturality and Yoneda again give an isomorphism. In this case its pairing is

\[
\begin{aligned}
Rf_*D_YB\otimes Rf_!B
&\simeq Rf_!(f^{-1}Rf_*D_YB\otimes B)\\
&\longrightarrow Rf_!(D_YB\otimes B)
\longrightarrow Rf_!\omega_Y\longrightarrow\omega_X.
\end{aligned}
\tag{8}
\]

The first counit in (8) is for ordinary inverse/direct image; the last arrow is the proper-support trace. This checks that the isomorphism is \(b_B\), with those counits and that trace. Finite global dimension keeps the tensors bounded, and the standing operation bounds keep the remaining objects in the bounded categories. Neither proof uses perfection or properness of \(f\).

<span id="the-role-of-the-extra-hypothesis"></span>

## Where a reversed comparison can fail {#evaluation-obstruction}

We now define the two reversed maps for arbitrary bounded inputs. Let

\[
\begin{aligned}
A_E&=f^{-1}D_XE,&
\delta_E&=u_{D_XE}\circ f^!\eta_E:f^!E\longrightarrow D_YA_E,\\
H_B&=Rf_!D_YB,&
\gamma_B&=b_{D_YB}\circ Rf_*\eta_B:Rf_*B\longrightarrow D_XH_B.
\end{aligned}
\tag{9}
\]

These are defined even when evaluation is not invertible. Dualization reverses their directions. Thus the composites

\[
\begin{aligned}
c_E&:A_E\xrightarrow{\eta_{A_E}}D_YD_YA_E
       \xrightarrow{D_Y\delta_E}D_Yf^!E,\\
e_B&:H_B\xrightarrow{\eta_{H_B}}D_XD_XH_B
       \xrightarrow{D_X\gamma_B}D_XRf_*B
\end{aligned}
\tag{10}
\]

have the advertised inverse- and direct-image types. We use (10) as the explicit definition of these dual comparisons. Equivalently, uncurry them to the evaluation pairings

\[
\begin{aligned}
f^{-1}D_XE\otimes f^!E&\longrightarrow
f^!(D_XE\otimes E)\longrightarrow\omega_Y,\\
Rf_!D_YB\otimes Rf_*B&\longrightarrow
Rf_!(D_YB\otimes f^{-1}Rf_*B)
\longrightarrow Rf_!\omega_Y\longrightarrow\omega_X.
\end{aligned}
\tag{11}
\]

To check this equivalence, expand \(\delta_E\) using (6), or \(\gamma_B\) using (8). The composite of double evaluation with evaluation is evaluation again: explicitly,
\(D\eta_Q\circ\eta_{DQ}=1_{DQ}\).
The chain calculation (H12) proves this identity with its two cancelling Koszul signs; the tensor–Hom unit and counit were checked immediately before (H10). In the second line of (11), ordinary adjunction additionally cancels \(f^{-1}\dashv Rf_*\)'s unit–counit pair. In the first line, the mate defining (6) cancels the corresponding \(Rf_!\dashv f^!\) pair. The remaining pairings are exactly (11). Thus the definitions retain the canonical evaluation and trace, not just the isomorphism classes of their endpoints.

**Evaluation criterion.** If \(\eta_E\) is invertible, then \(c_E\) is invertible if and only if \(\eta_{A_E}\) is invertible. If \(\eta_B\) is invertible, then \(e_B\) is invertible if and only if \(\eta_{H_B}\) is invertible.

**Proof.** Under the first assumption, both factors defining \(\delta_E\) in (9) are isomorphisms. Therefore \(D_Y\delta_E\) is an isomorphism, and the first factorization in (10) proves the first assertion. Under the second assumption \(\gamma_B\), hence \(D_X\gamma_B\), is an isomorphism. The second factorization proves the other assertion. No conservativity of dualization is used. \(\square\)

This criterion isolates the obstruction at a specific object: the pulled-back dual for inverse image, and the proper-support image of the dual for direct image. It does not attempt to dualize a noninvertible map and infer invertibility of that map.

<span id="reversing-inverse-image-duality"></span>

## Applying the criterion to constructible coefficients {#constructible-case}

An \(\mathbb R\)-constructible complex here is weakly subanalytic constructible with perfect stalk complexes. A perfect complex has a bounded representative by finitely generated projective \(k\)-modules. We retain the full ring \(k\); no Noetherian hypothesis is added.

The geometric inputs are constructible biduality and dual stability, analytic inverse-image stability, and proper direct-image stability on the closed coefficient support. Their current in-course arguments are identified in the prerequisite ledger below. They are precisely the inputs needed to apply the formal criterion.

If \(f\) is analytic and \(E\) is constructible, then \(D_XE\) and \(A_E=f^{-1}D_XE\) are constructible. Constructible biduality makes both \(\eta_E\) and \(\eta_{A_E}\) invertible. Consequently

\[
f^{-1}D_XE\xrightarrow{c_E,\ \sim}D_Yf^!E.
\tag{12}
\]

<span id="the-second-constructibility-input-for-a-nonproper-image"></span>

For direct image, assume explicitly that

\[
B\in D^b_{\mathbb R\text{-}c}(k_Y),\qquad
H_B=Rf_!D_YB\in D^b_{\mathbb R\text{-}c}(k_X).
\tag{13}
\]

Evaluation of \(B\) makes \(\gamma_B:Rf_*B\to D_XH_B\) invertible. Since \(H_B\) is constructible, its dual is constructible. This proves constructibility of \(Rf_*B\) before invoking any biduality for that image. Evaluation of \(H_B\) now gives

\[
Rf_!D_YB\xrightarrow{e_B,\ \sim}D_XRf_*B,
\qquad Rf_*B\in D^b_{\mathbb R\text{-}c}(k_X).
\tag{14}
\]

Properness on the closed support of \(B\) is one sufficient condition for (13). The closed supports of a constructible object and its dual agree: each vanishes on an open set if and only if its dual does, by local duality and biduality. Thus proper direct-image stability applies to \(D_YB\). A nonproper map can also satisfy (13); the actual condition concerns its coefficient image.

<span id="duality-after-an-infinite-locally-constant-twist"></span>

## Infinite twists: applying Hom instead of biduality {#infinite-twists}

Let \(M\in D^b(k_X)\) be locally constant. Its stalks may be arbitrary modules. Locally, the whole derived object is isomorphic to \(L_U\) for some bounded coefficient complex \(L\). Do not replace this assumption by global constancy or by a chosen extension to an ambient boundary.

The free paper by Andreas Hohl and Pierre Schapira, [*Unusual functorialities for weakly constructible sheaves*, version 2](https://arxiv.org/html/2303.11189v2), proves the comparisons used here in Theorems 4.3 and 4.8 and the resulting duality statements in Corollaries 4.10 and 4.11. The following arguments use those results through their current [in-course comparison proofs](../sheaf-proof-readings/src/SH03/weak-constructibility-under-sheaf-operations.md#natural-comparisons-with-infinite-locally-constant-coefficients).

Write \(\mathcal H_M(Q)=R\mathcal Hom(M,Q)\). Tensor–Hom currying gives a natural identity

\[
D_X(Q\otimes M)=\mathcal H_M(D_XQ).
\tag{15}
\]

This is valid for arbitrary bounded \(M\). It does not identify \(\mathcal H_M\) with tensoring by \(D M\).

<span id="inverse-duality-uses-perfection-before-the-twist"></span>

**Inverse-image twist.** Let \(f:Y\to X\) be analytic. For constructible \(E\), the canonical comparison is invertible:

\[
f^{-1}D_X(E\otimes M)\xrightarrow{\sim}D_Yf^!(E\otimes M).
\tag{16}
\]

**Proof.** Start with \(f^{-1}\mathcal H_M(D_XE)\). The inverse-Hom comparison for a locally constant first argument and a weakly constructible second argument identifies it with
\(\mathcal H_{f^{-1}M}(f^{-1}D_XE)\).
Apply this Hom functor to (12); its value is
\(\mathcal H_{f^{-1}M}(D_Yf^!E)=D_Y(f^!E\otimes f^{-1}M)\).
Finally the exceptional-tensor comparison
\[
f^!E\otimes f^{-1}M\xrightarrow{\sim}f^!(E\otimes M)
\tag{17}
\]
identifies this with the right side of (16), after dualizing (17) and using its inverse. All three steps are isomorphisms. The inverse-Hom step applies because \(D_XE\) is constructible; (17) applies because \(E\) is weakly constructible and \(M\) is locally constant. Currying (11) and then evaluating \(M\) identifies their composite with the canonical comparison. The only finite biduality used was (12) for \(E\), before adding \(M\). \(\square\)

<span id="direct-duality-needs-finite-boundary-control-on-the-untwisted-object"></span>

**Direct-image twist.** Let \(Y_\infty=(Y,\widehat Y)\) and \(X_\infty=(X,\widehat X)\) be b-analytic pairs: their open subsets are relatively compact and subanalytic in the ambient analytic manifolds. Let \(f:Y\to X\) be analytic with graph subanalytic in \(\widehat Y\times\widehat X\), so that it is a morphism of these b-analytic pairs. Suppose the zero extension \(j_{Y!}B\) is constructible with perfect stalks. Then

\[
Rf_!D_Y(B\otimes f^{-1}M)
\xrightarrow{\sim}D_X(Rf_*B\otimes M).
\tag{18}
\]

**Proof.** First check the untwisted input to (14). Put \(\widehat B=j_{Y!}B\). Open restriction of duality gives
\(D_YB=j_Y^{-1}D_{\widehat Y}\widehat B\).
Its zero extension is therefore
\(k_Y\otimes D_{\widehat Y}\widehat B\),
where \(k_Y\) is the ambient zero extension of the constant sheaf. Dual stability and the perfect cutoff make this constructible with perfect stalks. Thus \(D_YB\) is constructible up to infinity as well.

The b-analytic graph argument for image stability now makes \(H_B=Rf_!D_YB\) constructible with perfect stalks. Compactness here concerns the closed supports of the ambient graph coefficients: they lie in the compact closure of the graph. Projection is proper on those actual supports. It does not assert that \(f\) is proper on \(Y\). We have verified both conditions in (13), so (14) is available for the untwisted \(B\).

Use (15) on the source. The compact-graph Hom comparison then gives
\[
\begin{aligned}
Rf_!D_Y(B\otimes f^{-1}M)
&=Rf_!\mathcal H_{f^{-1}M}(D_YB)\\
&\xrightarrow{\sim}\mathcal H_M(H_B)
\xrightarrow{\mathcal H_M(e_B),\ \sim}\mathcal H_M(D_XRf_*B)\\
&=D_X(Rf_*B\otimes M).
\end{aligned}
\tag{19}
\]

The Hom comparison requires weak constructibility up to infinity of \(D_YB\), already checked. It is local on \(X\), so local constant models for \(M\) suffice; no ambient extension of \(M\) is imposed. Its map is defined by evaluation and the proper-support trace, and composing it with the pairing defining \(e_B\) gives (18). Neither \(B\otimes f^{-1}M\) nor \(Rf_*B\otimes M\) was assumed reflexive. \(\square\)

<span id="exercises-with-complete-solutions"></span>

## Eight calculations and tests {#exercises}

<span id="evaluation-order-prevents-circular-image-biduality"></span>

### 1. Finite pairings and the object to evaluate

*Difficulty: Intermediate.* Let \(Y\) be a finite discrete space with coefficients \(P_y\) that are perfect complexes, and map it to a point. Describe \(b_B\), \(e_B\), and the evaluations that justify them. Include the empty space.

**Solution.** Both images are the finite direct sum of the \(P_y\). The source dual has coefficient \(P_y^\vee\). A finite direct sum commutes with coefficient duality, so the pairing is \(\sum_y\operatorname{ev}_{P_y}\), with no cross term between different points. The map \(b_B\) already follows from (7). For \(e_B\), evaluate \(B\), obtaining \(\gamma_B\), and then evaluate \(H_B=\bigoplus_yP_y^\vee\). Finite projective evaluation makes both isomorphisms. Formula (10) gives the displayed sum pairing. For the empty space every object is zero and all comparison maps are the unique isomorphism of zero objects. This also shows why evaluating an ordinary image before proving its finiteness is unnecessary.

<span id="a-locally-finite-source-with-infinite-target-coefficients"></span>

<span id="infinite-discrete-support-invalidates-the-second-input"></span>

### 2. A discrete source whose ordinary image is too large

*Difficulty: Advanced.* Work over a field. Embed \(S=\{3n:n\in\mathbb Z\}\) as a closed subset of the real line, let \(B=i_*k_S\), and map the line to a point. Decide which maps in (4) and (10) remain invertible.

**Solution.** The points of \(S\) and the intervening open intervals give a locally finite subanalytic stratification; the restrictions have coefficients \(k\) or zero. Thus \(B\) has perfect stalks and is constructible. Closed-embedding duality gives \(D_{\mathbb R}B=i_*k_S\), because the intrinsic dualizing object of each isolated point is \(k\) in degree zero. Ordinary sections on \(S\) form a product and compact sections a direct sum. Both are exact functors on a discrete space, so
\[
Rf_*B=k^{\mathbb Z},\qquad H_B=k^{(\mathbb Z)}=:V.
\tag{20}
\]
Here \(\gamma_B\) identifies the product with \(V^*\), while \(e_B\) becomes the canonical evaluation \(V\to V^{**}\). This map is injective because coordinate functionals separate finite families. It is not surjective: the constant sequence \(1\) gives a nonzero class in \(k^{\mathbb Z}/k^{(\mathbb Z)}\). Extend that class to a basis and choose a linear functional nonzero on it. Composing with the quotient gives a nonzero functional on the product vanishing on every finite family. A finite coordinate functional with that vanishing property must be zero, so this functional is not an evaluation at an element of \(V\). The general map \(b_B\) remains an isomorphism; both its sides are \(k^{\mathbb Z}\). The failed evaluation is exactly \(\eta_{H_B}\). Neither vector space in (20) is finite dimensional.

<span id="a-closed-point-keeps-orientation-and-codimension"></span>

### 3. The orientation line at a point

*Difficulty: Intermediate.* For \(i:\{p\}\hookrightarrow X^d\), let \(P_X\) be a constant perfect complex and write \(L=\mathrm{or}_{X,p}\). Calculate (12) without choosing an orientation.

**Solution.** Finite projective duality gives
\(i^{-1}D_XP_X=P^\vee\otimes L[d]\).
The relative-ball calculation (O11)–(O12) gives
\(i^!P_X=P\otimes L^\vee[-d]\): the relative constant-coefficient cohomology has its generator in degree \(d\), and change of orientation acts by the dual orientation line. Dualizing on the point yields \(P^\vee\otimes L[d]\), the same object. Its pairing with \(P\otimes L^\vee[-d]\) is finite-projective evaluation times \(L\otimes L^\vee\to k\), with the complex symmetry convention of (1)–(3). For \(P=k\), both sides of (12) have their nonzero cohomology in degree \(-d\). Replacing \(i^!\) by ordinary restriction would lose the codimension shift.

<span id="integral-torsion-retains-its-dual-degree"></span>

### 4. Torsion tests the derived degree

*Difficulty: Intermediate.* In the preceding calculation take \(k=\mathbb Z\), \(P=\mathbb Z/m\) with \(m>1\), and trivialize the local orientation. Determine the nonzero degree of (12).

**Solution.** A representative of \(P\) is \([\mathbb Z\xrightarrow{m}\mathbb Z]\) in degrees \(-1,0\). Its dual has cokernel \(\mathbb Z/m\) in degree \(1\), hence \(P^\vee=P[-1]\). Both sides of (12) are \(P[d-1]\), with nonzero cohomology in degree \(1-d\). Indeed, \(i^!P_X=P[-d]\), so its point dual is \(P^\vee[d]\). Ordinary degree-zero Hom would give \(\operatorname{Hom}_{\mathbb Z}(\mathbb Z/m,\mathbb Z)=0\) and lose the actual dual object. The finite free resolution verifies perfection and retains its Ext degree.

<span id="nonproper-integration-on-an-oriented-line"></span>

### 5. Nonproper integration and its shift

*Difficulty: Introductory.* Give \(\mathbb R\) its increasing orientation and let \(a:\mathbb R\to\{\mathrm{pt}\}\). For a perfect constant complex \(P_{\mathbb R}\), calculate the two direct-image comparisons.

**Solution.** Contractibility, with the homotopy comparison (O1)–(O3), gives \(Ra_*P_{\mathbb R}=P\). The endpoint-difference calculation (B7), followed by coefficient projection, gives \(Ra_!P_{\mathbb R}=P[-1]\) for every bounded \(P\). Since \(D_{\mathbb R}P_{\mathbb R}=(P^\vee)_{\mathbb R}[1]\), the two maps have endpoints
\[
Ra_*D_{\mathbb R}P_{\mathbb R}=P^\vee[1]=D_{\mathrm{pt}}Ra_!P_{\mathbb R},
\quad
Ra_!D_{\mathbb R}P_{\mathbb R}=P^\vee=D_{\mathrm{pt}}Ra_*P_{\mathbb R}.
\tag{21}
\]
The oriented trace sends the compact fundamental cohomology generator to \(1\); the remaining pairing is evaluation on \(P\). The two constructibility inputs of (13) hold, although \(a\) is nonproper.

<span id="open-interval-endpoints-distinguish-the-images"></span>

### 6. Endpoints distinguish the two images

*Difficulty: Intermediate.* For \(j:U=(-2,2)\hookrightarrow\mathbb R\), compare ordinary and proper-support images of \(k_U\), and calculate their duality maps at an endpoint.

**Solution.** On a small neighborhood of an endpoint, intersection with \(U\) is a contractible half-interval. Thus \(Rj_*k_U=k_{[-2,2]}\) with endpoint stalk \(k\), while \(j_!k_U=k_{(-2,2)}\) has endpoint stalk zero. On the oriented source, \(D_Uk_U=k_U[1]\). Formula (4) gives
\(D_{\mathbb R}k_{(-2,2)}=k_{[-2,2]}[1]\),
and (14) gives
\(D_{\mathbb R}k_{[-2,2]}=k_{(-2,2)}[1]\).
The first comparison has endpoint stalk \(k[1]\); the reversed comparison has zero endpoint stalk. The inputs in (13) are constructible in both cases. The difference concerns boundary stalks, not invertibility of either comparison.

<span id="further-exercises-on-infinite-twists"></span>

<span id="a-constant-infinite-twist-keeps-the-point-codimension"></span>

### 7. A twist can preserve a comparison without becoming reflexive

*Difficulty: Intermediate.* Let \(k\) be a field and \(V\) any vector space. Take \(E=k_X\), \(M=V_X\), and the inclusion of a point in an oriented \(d\)-manifold. Calculate (16). Test biduality when \(V=k^{(\mathbb N)}\).

**Solution.** Constant-sheaf Hom on a sufficiently small ball gives \(D_XV_X=(V^*)_X[d]\). Formula (O11) applies to arbitrary bounded constant coefficients and gives \(i^!V_X=V[-d]\), including infinite \(V\). Both sides of (16) are consequently \(V^*[d]\), and their map is the evaluation comparison from these identifications. For \(V=k^{(\mathbb N)}\), the quotient-functional argument in calculation 2 gives a functional on \(k^{\mathbb N}\) which is not a finite coordinate functional. Thus \(V\to V^{**}\) is not surjective. The comparison used finite biduality of \(k_X\), not biduality of the twist.

<span id="an-open-interval-permits-a-nonproper-infinite-twist"></span>

### 8. A controlled boundary permits an infinite twist

*Difficulty: Intermediate.* Regard \(j:(-2,2)\hookrightarrow(-3,3)\) as a morphism of pairs \(((-2,2),\mathbb R)\to((-3,3),\mathbb R)\). Use \(B=k_U\) and \(M=V_{(-3,3)}\), with arbitrary \(V\) over a field. Check (18) including both endpoints.

**Solution.** The ambient zero extension of \(B\) is constructible with perfect stalks. The ambient graph is subanalytic with compact closure. All boundary hypotheses are therefore satisfied. The left side of (18) is \((V^*)_{(-2,2)}[1]\), with zero endpoint stalks. The ordinary untwisted image is \(k_{[-2,2]}\); after tensoring it becomes \(V_{[-2,2]}\). At an endpoint its costalk is the fibre of the identity \(V\to V\), hence zero. In the interior its costalk is \(V[-1]\). Stalk–costalk duality identifies its dual with \((V^*)_{(-2,2)}[1]\). The oriented trace matches the interior evaluation, and the endpoint maps are the unique maps of zero objects. This verifies (18) without requiring finite dimension of \(V\) or an ambient extension as part of the theorem's hypotheses.

## Prerequisites and reading {#prerequisites}

The compact-support arguments (C1)–(C6) prove the extension, lifting, stability and c-soft criterion needed by the projection proof (P1)–(P8). The proper-image arguments (F1)–(F6) supply the fibre and support-operation inputs. The composition and dimension arguments (D1)–(D10) supply base change, proper-image composition and the uniform bound. Projection therefore supplies contract (2) with its compact-support foundations proved here. The construction (A1)–(A10) supplies ordinary and exceptional adjunction and trace-compatible exceptional composition on bounded-below categories. The bounds (B1)–(B15) establish ordinary and exceptional boundedness, closed localization and a finite injective dualizing model. The constructions (H1)–(H12) supply enough injectives, finite flat models, tensor–Hom adjunction, natural evaluation and the double-dual triangle identity. These provide the algebraic operation contracts used by (5), (7), (9)–(10) and the evaluation criterion. The local arguments (O1)–(O12) prove homotopy invariance through a proper interval, point-to-compact comparison, orientation signs, the dualizing identification with its trace and the constant relative-ball formulas. The formal background is [Complexes, cones and localization, Sections 4–5](../derived-categories-and-sheaf-operations/src/complexes-cones-and-localization.md#4-fractions-at-quasi-isomorphisms), which constructs roofs, distinguished triangles and good truncations. The geometric applications additionally use the results in the table.

| Input | Current in-course argument | Use here |
|---|---|---|
| Actual evaluation is constructible biduality over the stated ring | [Constructible costalks and Verdier duality, “The evaluation map is biduality”](../sheaf-proof-readings/src/SH03/constructible-costalks-and-verdier-duality.md#the-evaluation-map-is-biduality) | Evaluations in (12)–(14) |
| Perfect constructible inverse and proper-support image stability | [Perfect operations and finite microlocal coefficients](../sheaf-proof-readings/src/SH03/perfect-operations-and-finite-microlocal-coefficients.md), and [Perfect coefficients on compact fibres, “Proper direct image with perfect stalks”](../sheaf-proof-readings/src/SH03/perfect-coefficients-on-compact-fibres.md#proper-direct-image-with-perfect-stalks) | Verifying constructibility, including the untwisted image in (18) |
| Stabilized stalk and costalk comparisons | [Small balls, central fibres and supported cohomology](../sheaf-proof-readings/src/SH03/small-balls-central-fibres-and-supported-cohomology.md) | Local duality and arbitrary coefficients |
| Inverse-Hom and exceptional-tensor comparisons | [Weak constructibility under sheaf operations, “Analytic inverse images commute with these coefficients”](../sheaf-proof-readings/src/SH03/weak-constructibility-under-sheaf-operations.md#analytic-inverse-images-commute-with-these-coefficients) | (16)–(17) |
| Compact graph image and Hom comparisons | [Weak constructibility under sheaf operations, “Nonproper maps with controlled behavior at infinity”](../sheaf-proof-readings/src/SH03/weak-constructibility-under-sheaf-operations.md#nonproper-maps-with-controlled-behavior-at-infinity) | (18)–(19) |
| General weakly constructible small-ball stabilization and local duality | The [scalar small-ball argument](../sheaf-proof-readings/src/SH03/small-balls-central-fibres-and-supported-cohomology.md#scalar-profile) gives the ordinary, compact-support and closed-support comparisons using proper-image weak constructibility and its stated cotangent and local-duality inputs. | Calculations 2–8 and local duality |

The general duality discussion in David B. Massey's [*Notes on Perverse Sheaves and Vanishing Cycles*, version 13](https://arxiv.org/html/math/9908107v13) provides further reading. Its stated coefficient assumptions are different from ours; it is not used to supply the full-ring biduality proof here. Andreas Hohl and Pierre Schapira's [*Unusual functorialities for weakly constructible sheaves*, version 2](https://arxiv.org/html/2303.11189v2#S4.SSx4) supplies the infinite-twist results treated above.
