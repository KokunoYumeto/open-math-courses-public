# Grothendieck's existence theorem

*Written by GPT-6.1 Sol (OpenAI), in Codex, at Ultra effort, October 2026. Self-checked by the writing AI, GPT-6.1 Sol, at Ultra effort. Public domain (CC0).*

Formal functions recovers completed cohomology from infinitesimal neighborhoods. Grothendieck's existence theorem recovers the sheaves themselves. Over a complete Noetherian base, a compatible coherent sheaf on every thickening of a proper scheme comes from one coherent sheaf, and compatible morphisms come from unique algebraic morphisms.

We use [formal functions](the-theorem-on-formal-functions.md), [Serre generation and vanishing](serres-theorems-on-projective-schemes.md), and [proper coherence](proper-morphisms-and-coherent-direct-images.md). The existing earlier *Completion*, Theorems 3.1–3.3 proves Noetherianness, flatness and exactness of completion, and completeness of finite modules. The proper-coherence lesson gives Chow's construction in Lemma 4.0 and links the full Noetherian variant to the earlier programme's *Projective morphisms and Chow's lemma*, Theorem 4.1. Internal derived Hom and its identification with global Ext are proved in the earlier *Internal derived Hom and Ext sheaves*, Theorem 3.1 and equations (3.2)–(3.3). We prove the formal comparison and proper reduction below.

## 1. Compatible coherent systems

For a Noetherian scheme \(X\) and a coherent ideal \(J\subset\mathcal O_X\), a **coherent formal module** is a system \(\mathfrak F=(F_n)_{n\geq1}\) of coherent sheaves, with
\[
J^nF_n=0,\qquad F_{n+1}/J^nF_{n+1}\xrightarrow{\sim}F_n.
\tag{1}
\]
Morphisms are compatible sheaf maps at every level. Equivalently, \(F_n\) is a coherent sheaf on \(X_n=V(J^n)\). Iterating (1) gives \(F_m/J^nF_m=F_n\) for \(m\geq n\). Write \(\operatorname{Coh}(X,J)\) for this category.

**Lemma 1.1 (the affine description).** If \(X=\operatorname{Spec}R\) and \(J=I\mathcal O_X\), this category is equivalent to finite modules over \(\widehat R=\varprojlim R/I^n\). The correspondence is
\[
(M_n)\longmapsto M=\varprojlim M_n,
\qquad M\longmapsto(M/I^nM).
\]

**Proof.** The transition maps are onto, so a compatible sequence lifting any chosen element of \(M_1\) can be constructed recursively. Lift finitely many generators of \(M_1\) to \(M\). They define maps \((R/I^n)^r\to M_n\), which are onto by Nakayama for the nilpotent ideal \(I/I^n\).

Let \(K_n\) be their kernels. These kernels also have surjective transitions. To lift \(v\in K_n\), lift it to \(w\in(R/I^{n+1})^r\). Its image in \(M_{n+1}\) lies in \(I^nM_{n+1}\), since it vanishes in \(M_n\). Surjectivity of the free-module map lets us subtract an element of \(I^n(R/I^{n+1})^r\) with that same image. The corrected lift belongs to \(K_{n+1}\).

Taking limits gives
\[
0\to\varprojlim K_n\to\widehat R^{\,r}\to M\to0.
\]
Surjectivity on the right follows by adjusting consecutive lifts using the surjective kernel transitions. Thus \(M\) is finite. Since \(\varprojlim K_n\to K_n\) is onto, reducing this presentation modulo \(I^n\) gives \(M/I^nM=M_n\). Conversely finite modules over the Noetherian complete ring \(\widehat R\) are complete, so are recovered from their quotients. Compatible maps pass uniquely to and from limits, proving the equivalence. \(\square\)

An affine open in a scheme over a complete ring need not have a complete coordinate ring. For instance the \(t\)-adic completion of \(k[[t]][x]\) is the ring
\[
k[[t]]\langle x\rangle=\varprojlim_n(k[t]/t^n)[x]
\]
of restricted power series: in \(\sum a_jx^j\), the coefficients \(a_j\) tend to zero \(t\)-adically. This contains series of unbounded degree in \(x\), unlike the polynomial ring.

## 2. Exactness and the actual formal kernel

**Theorem 2.1.** The category \(\operatorname{Coh}(X,J)\) is abelian, exactness is local on \(X\), and the completion functor
\[
\operatorname{Coh}(X)\longrightarrow\operatorname{Coh}(X,J),
\qquad F\longmapsto\widehat F=(F/J^nF)
\]
is exact.

**Proof.** On an affine, Lemma 1.1 identifies the category with finite modules over a Noetherian ring, an abelian category. We explain why its kernels glue, since taking the kernels separately at each level is generally wrong.

For a morphism \(\alpha:(F_n)\to(G_n)\), take the images
\[
K'_{l,m}=\operatorname{im}(\ker\alpha_l\to F_m),\qquad l\geq m.
\]
On an affine let \(u:M\to N\) be the corresponding completed-module map, with kernel \(K\) and image \(H\). Artin–Rees for \(H\subset N\) gives a constant \(c\) such that
\[
u^{-1}(I^lN)\subset K+I^{l-c}M\quad(l\geq c).
\]
Indeed \(H\cap I^lN\subset I^{l-c}H\), and elements of this last module lift from \(I^{l-c}M\). Hence for \(l\geq m+c\), the image \(K'_{l,m}\) is precisely
\(K/(K\cap I^mM)\). It stabilizes. Artin–Rees for \(K\subset M\) then shows that, for fixed \(n\) and sufficiently large \(m\),
\[
K'_m/I^nK'_m
=K/(K\cap I^mM+I^nK)=K/I^nK.
\tag{2}
\]
All these images and quotients are constructions with coherent sheaves and commute with restriction. A finite affine cover gives uniform stabilization bounds, so they define coherent sheaves globally. The resulting system is the formal kernel: a map of systems killed by \(\alpha\) factors at every level through the stabilized images, then through (2); the factorization is unique. Cokernels are the levelwise cokernels, since quotient formation preserves (1). On affines these constructions give the ordinary module kernel and cokernel, so image equals coimage. They also show that restriction is exact and that exactness can be checked on an open cover.

On an affine the completion functor is \(M\mapsto M\otimes_R\widehat R\) on finite modules. Flatness of Noetherian completion makes it exact. The local characterization just established proves exactness globally. \(\square\)

For example multiplication by \(t\) on \(k[[t]]\) has zero kernel, but multiplication by \(t\) on \(k[t]/t^n\) has kernel \(k\,t^{n-1}\). These nonzero kernels map to zero at the preceding level. Their stabilized formal kernel is zero. An exact sequence in the formal category therefore need not give a left-exact sequence at each fixed quotient level.

A map of formal modules is onto exactly when its first-level map is onto. In the affine description, its cokernel is a finite completed module \(C\); if \(C/IC=0\), Nakayama gives \(C=0\). Here \(I\widehat R\) lies in the Jacobson radical: \(1-a\) is invertible for \(a\in I\widehat R\), by its convergent geometric series. This also proves the assertion locally on \(X\).

## 3. Full faithfulness from formal functions

Now let \(A\) be Noetherian and complete for an ideal \(I\), let \(X\) be proper over \(A\), and set \(J=I\mathcal O_X\).

**Lemma 3.1 (completed Hom).** For coherent \(F,G\), with \(H=\mathcal Hom(F,G)\),
\[
\operatorname{Hom}_{\operatorname{Coh}(X,J)}(\widehat F,\widehat G)
\cong\varprojlim_n\Gamma(X,H/J^nH).
\tag{3}
\]

**Proof.** Affine locally, \(F\) has a finite presentation. Applying \(\operatorname{Hom}(-,G)\) describes Hom as the kernel of a map between two finite direct sums of \(G\). Tensoring this kernel with the flat completed ring preserves the kernel and gives
\[
\operatorname{Hom}_R(M,N)\otimes_R\widehat R
=\operatorname{Hom}_{\widehat R}(\widehat M,\widehat N).
\]
Lemma 1.1 identifies the right side with compatible maps on the quotients. These natural affine identifications identify the sheaves of completed Hom sections with the sheaves of compatible formal maps. They glue on overlaps. Taking global sections, which commutes with inverse limits of sheaves, gives (3). Notice that no equality of the separate finite-level Hom modules was asserted. \(\square\)

**Theorem 3.2 (full faithfulness).** Completion on coherent sheaves on \(X\) is fully faithful.

**Proof.** The sheaf \(H\) is coherent, so its global section module is finite over \(A\). Formal functions identifies the right side of (3) with \(\widehat{\Gamma(X,H)}\). A finite module over the complete Noetherian ring \(A\) is already complete. Thus (3) identifies formal maps with \(\Gamma(X,H)=\operatorname{Hom}_X(F,G)\), and the identification is the completion map on morphisms. \(\square\)

In particular, an algebraization, when it exists, is unique up to the unique isomorphism inducing a specified formal identification. Formal isomorphisms algebraize because both directions algebraize and faithfulness makes their composites identities.

**Proposition 3.3 (extension comparison, also with proper supports).** If \(F,G\) are coherent on a separated finite-type \(X/A\), and have proper support, then completion induces isomorphisms
\[
\operatorname{Ext}^r_X(F,G)
\xrightarrow{\sim}
\operatorname{Ext}^r_{\operatorname{Coh}(X,J)}(\widehat F,\widehat G)
\qquad(r=0,1).
\]
The group in degree one means short exact sequences in the formal category with their specified ends. Thus every such formal extension is algebraizable.

**Proof.** On an affine chart, resolve the finite module of \(F\) by finite free modules, successively resolving its finite syzygies. Noetherianness permits any finite prefix. Applying Hom into \(G\) computes module Ext as a kernel modulo an image; these finite modules sheafify, and localization commutes with the computation. Hence the sheaves \(E^q=\mathcal Ext^q_X(F,G)\) are coherent and supported on the proper intersection of the two supports. Flatness of completion preserves every kernel and image in the finite prefix, giving the formal local identity
\[
\mathcal Ext^q(\widehat F,\widehat G)=\widehat{E^q}.
\]
The identifications are compatible with restriction to principal opens (where restriction is followed by completion), so glue.

We spell out the cohomological step in this formal identity. On a formal affine, coherent modules are finite completed modules by Lemma 1.1. Their Čech complex for a finite principal cover is the inverse limit of the corresponding module complexes modulo \(I^n\), each exact in positive degrees by affine acyclicity. The complexes have surjective transitions in every term and in the augmented section term. The elementary inverse-limit argument therefore preserves this exactness: lift a preimage at one level and correct its next lift by a cocycle at the preceding level. Equivalently the difference map \(\prod C_n\to\prod C_n\), \((c_n)\mapsto(c_n-u_{n+1}c_{n+1})\), is onto termwise, and its kernel is \(\varprojlim C_n\). The basis criterion in the Čech lesson proves acyclicity for coherent formal modules on these affine opens. Use a finite affine cover of \(X\), whose intersections are affine by separatedness. For a coherent \(E\), the formal section complex is \(\varprojlim C_n(E/I^nE)\). Formal functions proves Mittag–Leffler stabilization of all its cohomology systems. The same product-difference sequence now gives
\[
H^p(X,\widehat E)=\varprojlim H^p(X,E/I^nE)
=\widehat{H^p(X,E)}.
\]
Here the possible cokernel of the product-difference map on \(H^{p-1}\) is zero: stabilized images admit recursive lifts, which proves this assertion directly for a Mittag–Leffler system. For proper support, formal functions is applied to its proper scheme-theoretic support. The finite \(A\)-modules \(H^p(X,E)\) are already complete.

For completeness the local-to-global Ext spectral sequence follows from exactly the first-quadrant filtered-complex construction of the Čech lesson. Resolve \(G\) by injectives as module sheaves on the ringed space, take internal Hom from \(F\), and apply the cohomology-sheaf filtration and a flasque resolution. Internal Hom into an injective is flasque: a map on an open extends using the injection from extension by zero of \(F\) into \(F\). Thus the total global Hom complex computes Ext and the second page is \(H^p(X,E^q)\). The formal ringed space is constructed by the completed affine rings and their completed restrictions, as in Lemma 1.1; the same injective construction applies to its module sheaves. Its coherent modules are exactly our systems. Extensions of coherent modules are coherent locally over the Noetherian completed rings, so its degree-one Ext agrees with Yoneda Ext in our formal category. Its second page is \(H^p(X,\widehat{E^q})\). The preceding cohomology comparison identifies these second pages. Each total degree has finitely many \(p,q\ge0\), so the finite-filtration comparison gives the asserted isomorphisms in degrees zero and one.

Finally degree-one derived Ext classifies extensions: embed \(G\) in an injective \(Q\), pull back \(Q\to Q/G\) along maps from \(F\), and identify two pullbacks when their difference lifts to \(Q\). Conversely injectivity extends \(G\to Q\) over any extension's middle module and recovers such a map. This identifies Yoneda classes with the same Hom cokernel, and commutes with completion. An algebraic extension of coherent modules is coherent and has support in the union of the proper supports. \(\square\)

## 4. One twist for every thickening

Suppose \(X\) is projective over \(A\), and choose a relatively ample invertible sheaf \(L\). For a formal module \(\mathfrak F=(F_n)\), put \(F_0=0\) and
\[
D_n=\ker(F_{n+1}\to F_n),\qquad n\geq0.
\]

**Lemma 4.1 (uniform vanishing).** There exists \(d_0\) such that
\[
H^1(X,D_n\otimes L^d)=0\quad\text{for every }n\geq0,
\quad d\geq d_0.
\]

**Proof.** Let \(B=\bigoplus_{n\geq0}I^n/I^{n+1}\), a Noetherian graded algebra generated in degree one over \(A/I\). The sheaf \(D=\bigoplus D_n\) is a graded module over \(\mathcal O_X\otimes_A B\). On an affine, Lemma 1.1 identifies it with the associated graded module \(\bigoplus J^nM/J^{n+1}M\) of a finite completed module. It is generated over the associated graded ring in degree zero. The map from the pulled-back \(B\) to that associated graded ring is surjective, because \(J\) is generated by the image of \(I\). Consequently \(D\) is of finite type over \(\mathcal O_X\otimes_A B\). Surjectivity is sufficient; no flatness is needed to identify associated graded rings.

On \(X_B=X\times_A\operatorname{Spec}B\), with affine projection \(p\), the affine sheaf correspondence realizes \(D=p_*E\) for a coherent \(E\). The morphism \(X_B\to\operatorname{Spec}B\) is projective and \(p^*L\) is relatively ample. Serre vanishing gives one bound for the positive cohomology of \(E\otimes p^*L^d\). Affine pushforward, its projection formula, and cohomology commuting with direct sums of quasi-coherent sheaves on this separated quasi-compact scheme identify that cohomology with
\(\bigoplus_n H^1(X,D_n\otimes L^d)\). Every summand is zero for the same bound. \(\square\)

The bound is uniform in the infinitesimal index. Applying Serre vanishing independently to each \(F_n\) would give bounds depending on \(n\), insufficient for a single finite presentation.

## 5. Existence on a projective scheme

**Theorem 5.1 (projective existence).** For projective \(X\) over \(A\), completion gives an equivalence
\[
\operatorname{Coh}(X)\simeq\operatorname{Coh}(X,I\mathcal O_X).
\]

**Proof.** Full faithfulness is Theorem 3.2. Let \(\mathfrak F\) be a formal module. Choose \(d\) large enough both for Lemma 4.1 and for finitely many sections of \(F_1\otimes L^d\) to generate it. The exact sequences with kernel \(D_n\otimes L^d\) make
\[
\Gamma(X,F_{n+1}\otimes L^d)\to\Gamma(X,F_n\otimes L^d)
\]
surjective. Lift the chosen finite collection recursively to compatible sections at every level. They give a formal morphism
\[
\widehat P\twoheadrightarrow\mathfrak F,
\qquad P=(L^{-d})^r.
\]
It is onto because it is onto at the first level. Its kernel \(\mathfrak K\) is a coherent formal module by Theorem 2.1. Apply the same construction to \(\mathfrak K\) to obtain \(\widehat Q\twoheadrightarrow\mathfrak K\), with \(Q=(L^{-e})^s\) for some \(e,s\). Thus
\[
\widehat Q\longrightarrow\widehat P\longrightarrow\mathfrak F\to0
\]
is a presentation in the formal category. Full faithfulness algebraizes its first map to \(Q\to P\). Take its coherent cokernel \(F\). Exactness of completion identifies \(\widehat F\) with \(\mathfrak F\), proving essential surjectivity. \(\square\)

The two presentations use different twists if necessary. There is no assertion that their kernel is a vector bundle, or that every coherent sheaf has a finite resolution by line bundles.

## 6. Proper schemes and proper supports

**Theorem 6.1 (Grothendieck existence).** Let \(A\) be Noetherian and \(I\)-adically complete, and let \(X\) be separated and of finite type over \(A\). Completion gives an equivalence between coherent sheaves on \(X\) with support proper over \(A\) and coherent formal modules whose first-level support is proper over \(A\). In particular, when \(X\) is proper, all coherent sheaves and all coherent formal modules participate.

**Proof.** Full faithfulness for proper supports is Proposition 3.3 in degree zero. We prove existence by Noetherian induction on closed subschemes of \(X\). If there were a counterexample, the ascending chain condition on coherent ideals would give a maximal defining ideal of a closed subscheme on which existence fails. Replace \(X\) by that subscheme. We may therefore assume existence for every \(V(K)\) with \(K\ne0\). This is ideal induction and requires no finite dimension bound on the Noetherian base.

Use the schematic, possibly nonreduced Noetherian Chow theorem proved in the earlier *Projective morphisms and Chow's lemma*, Theorem 4.1. Its hypotheses are satisfied: \(A\) is Noetherian and \(X/A\) is separated and of finite type. Its affine cover is chosen with every member containing all generic points; their intersection \(U\) contains these points. Schematic closure preserves the structure over \(U\). The resulting projective proper surjection \(p:Y\to X\) is an isomorphism over \(U\), with \(Y\) quasi-projective over \(A\). This assertion uses the full schematic theorem, and does not replace \(X\) by its reduction. If \(X\) is proper, \(Y\) is projective over \(A\), by the graph argument.

Pull the formal module \(\mathfrak F\) to \(Y\). For proper \(X\), Theorem 5.1 algebraizes it to \(E\). In the proper-support case, immerse \(Y\) as an open of its projective closure \(\overline Y\). The first-level pulled-back support is proper, since \(p\) is proper and the original first-level support is proper. At higher levels its underlying closed set is unchanged and its scheme structure is a nilpotent thickening; Lemma 5.4 of the formal-functions lesson makes these supports proper as well. Each is consequently closed in \(\overline Y\). Extension by zero is coherent: near a point of its closed support we are inside \(Y\), and outside that support the sheaf is zero. These extensions and their quotient transitions give a coherent formal module on \(\overline Y\). Theorem 5.1 algebraizes it to \(\overline E\).

The boundary intersection of the algebraic support of \(\overline E\) is closed in the projective scheme and has closed image in \(\operatorname{Spec}A\). It misses \(V(I)\), by the specified first-level support. The ideal \(I\) lies in the Jacobson radical: the geometric series inverts \(1-a\) for every \(a\in I\). Every nonempty closed subset of \(\operatorname{Spec}A\) therefore meets \(V(I)\). The boundary intersection is empty. Restriction gives \(E\) on \(Y\) with proper support. In both cases \(H=p_*E\) is coherent by proper coherence and has proper support. For the support assertion, its reduced support is contained in the proper image of the support of \(E\); its scheme-theoretic support is a finite nilpotent thickening of a closed subset of that image, hence proper by Lemma 5.4.

The adjunction maps at all finite levels, followed by inverse limit, define
\[
\alpha:\mathfrak F\longrightarrow\widehat H.
\]
Formal functions in degree zero for \(p\), checked on affine opens of \(X\), identifies the completed direct image with this inverse limit. Thus \(\alpha\) is a morphism of coherent formal modules, an isomorphism over \(U\). We must prove a fixed power annihilating both defects.

Fix an affine \(V=\operatorname{Spec}R\subset X\), and let \(\widehat R\) be its \(I\)-adic completion. Lemma 1.1 represents \(\mathfrak F|_V\) by a finite \(\widehat R\)-module \(M\). The scheme \(Y_{\widehat R}\) is projective over the complete Noetherian ring \(\widehat R\). The pullbacks of \(E\) and \(p^*\widetilde M\) there have the same specified formal completion, by their construction and quotient identities. Theorem 3.2 on this projective scheme makes them isomorphic algebraically. Flat base change along \(R\to\widehat R\), proved in the base-change lesson, identifies \(H\otimes_R\widehat R\) with \(p_*p^*\widetilde M\). Under these identifications \(\alpha\) is the actual adjunction
\[
M\longrightarrow\Gamma(Y_{\widehat R},p^*\widetilde M).
\]
It is an isomorphism outside \(V(K\widehat R)\), where \(K\) is the coherent ideal of \(X\setminus U\). Its kernel and cokernel are finite modules over the Noetherian ring \(\widehat R\). The support-power proof in the proper-coherence lesson annihilates them by a power of \(K\widehat R\). A finite affine cover gives a common maximum exponent \(c\), so both formal defects are annihilated by \(K^c\).

Write these defects as \(\mathfrak C,\mathfrak D\). Their first-level supports are proper: the formal kernel has support inside the first-level support of \(\mathfrak F\), since the affine Nakayama test makes the formal module zero wherever its first member is zero; the cokernel has support inside that of \(\widehat H\). They are now formal modules on \(V(K^c)\). The ideal \(K^c\) is nonzero, since \(K\) is the unit ideal at every generic point contained in \(U\). Induction algebraizes the defects to coherent proper-support \(C,D\) on \(X\), annihilated by \(K^c\). Full faithfulness algebraizes the formal quotient \(\widehat H\to\mathfrak D=\widehat D\) to \(H\to D\). This is onto: its coherent proper-support cokernel has zero completion, and full faithfulness detects zero. Put \(Q=\ker(H\to D)\). Exact completion identifies \(\widehat Q\) with the image of \(\alpha\). We obtain the formal sequence
\[
0\to\widehat C\to\mathfrak F\to\widehat Q\to0.
\]
Proposition 3.3 lifts its extension class to \(0\to C\to F\to Q\to0\). The middle sheaf is coherent with proper support; equality of extension classes gives the specified \(\widehat F\cong\mathfrak F\). This contradicts the counterexample and completes the induction for both proper schemes and proper supports. \(\square\)

## 7. Examples: what can fail on an affine line

On \(\mathbf P^1_{k[[t]]}\), the systems \(\mathcal O_{X_n}(d)\) algebraize to \(\mathcal O_X(d)\). The extension system
\[
0\to\mathcal O_{X_n}(-2)\to E_n\to\mathcal O_{X_n}\to0
\]
with compatible class \(a_n\in k[t]/t^n\) algebraizes to the extension with class \(a=\varprojlim a_n\in k[[t]]\), because \(H^1(\mathcal O_X(-2))=k[[t]]\). Choosing \(a=t\) recovers our cohomology-jump example.

For \(X=\mathbf A^1_{k[[t]]}\), completion is not fully faithful. The restricted series
\[
h(x)=\sum_{j\geq0}t^jx^j
\]
defines a compatible multiplication map on the systems \(\mathcal O_{X_n}\), but is not a polynomial in \(x\). It therefore does not come from an endomorphism of \(\mathcal O_X\). Faithfulness also fails: the nonzero coherent module \(k[[t]][x]/(tx-1)\) has zero completion, since \(tx-1\) is a unit modulo every power of \(t\).

These are failures of morphism recovery and uniqueness, not examples of nonalgebraizable objects. In fact this particular affine line has a stronger existence property.

**Proposition 7.1.** Every coherent formal module on \(\mathbf A^1_{k[[t]]}\) is algebraizable.

**Proof.** Let \(R=k[[t]][x]\), \(B=\widehat R\), and let the system correspond to a finite \(B\)-module \(M\). The ring \(B\) is a Noetherian domain, and \(B/tB=k[x]\). Thus \((t)\) is prime, and \(B_{(t)}\) is a discrete valuation ring: its maximal ideal is generated by the nonzero element \(t\). The structure theorem over this ring gives
\[
M_{(t)}\cong B_{(t)}^{\,r}\oplus\bigoplus_{i=1}^s B_{(t)}/(t^{a_i}).
\]
Finite presentations let this isomorphism and its inverse be defined after inverting finitely many elements of \(B\setminus(t)\). The identities defining inverse maps also hold after finitely many such inversions. Let \(h\in k[x]\setminus\{0\}\) be the product of their nonzero reductions modulo \(t\). In the \(t\)-adic completion of \(R[1/h]\), each denominator is a unit, since its reduction modulo \(t\) is a unit. Hence the formal system on \(D(h)\) is isomorphic to the completion of the displayed free-plus-\(t\)-power-torsion module.

The zero set of \(h\) in \(\mathbf P^1_k\) is finite and lies in the affine line: the homogenization has nonzero value at infinity. Let \(V\subset\mathbf P^1_{k[[t]]}\) be the complement of that homogenized zero set. It contains infinity and meets the affine chart in \(D(h)\). On \(V\), take the formal completion of the same free-plus-torsion module. Glue it to the given system on the affine chart using the formal isomorphism on \(D(h)\). This gives compatible coherent sheaves on all projective-line thickenings. Theorem 5.1 algebraizes them on \(\mathbf P^1_{k[[t]]}\). Restricting that sheaf to the affine chart algebraizes the original system. \(\square\)

Thus a claim that an arbitrary formal multiplication series automatically gives a nonalgebraizable coherent module on this affine line would be false. The theorem's equivalence, including morphisms and unique recovery, genuinely needs its support hypotheses; essential surjectivity alone can hold in a special nonproper situation.

## 8. Exercises with solutions

**Exercise 8.1 (easy: exactness).** Explain the sense in which completion of a coherent short exact sequence is exact, and exhibit the failure of left exactness at a fixed quotient level.

**Solution.** On an affine, finite-module completion is tensoring with the flat Noetherian completed ring, so is exact; Theorem 2.1 glues this statement in the formal category. For multiplication by \(t\) on \(k[[t]]\), the original map is injective but its reduction modulo \(t^n\) has kernel \(k t^{n-1}\). These kernels are transient and have stabilized formal kernel zero. Thus finite-level injectivity is not the meaning of exact completion.

**Exercise 8.2 (medium: projective-line maps).** Compute the compatible morphisms from \((\mathcal O_{X_n}(a))\) to \((\mathcal O_{X_n}(b))\) on \(\mathbf P^1_{k[[t]]}\).

**Solution.** They are the limit of sections of \(\mathcal O_{X_n}(b-a)\). If \(b-a<0\), each group is zero. Otherwise its monomial basis gives \((k[t]/t^n)^{b-a+1}\), whose limit is \(k[[t]]^{b-a+1}\). This is exactly the algebraic Hom group from projective-space cohomology, with its coefficientwise restriction map. It proves full faithfulness for these line bundles directly.

**Exercise 8.3 (medium: nonproper failure).** Give both a compatible endomorphism on the affine-line formal structure sheaf that does not algebraize as an endomorphism of \(\mathcal O_X\), and a nonzero coherent sheaf with zero completion.

**Solution.** Multiplication by \(\sum_{j\geq0}t^jx^j\) is defined modulo every \(t^n\), but a polynomial cannot have its unbounded nonzero \(x\)-coefficients, so it does not algebraize as the specified endomorphism. The sheaf associated to \(R/(tx-1)\) is nonzero: its ring is \(k((t))\), with \(x=t^{-1}\). Its reduction modulo \(t^n\) is zero because \(t\) is invertible there. Proposition 7.1 explains why neither example should be misdescribed as a nonalgebraizable formal object.

**Exercise 8.4 (medium: algebraizing a presentation).** Recover projective existence from uniform vanishing, full faithfulness and exactness.

**Solution.** Use a uniform twist to lift a finite generating collection for \(F_1\), giving \(\widehat P\twoheadrightarrow\mathfrak F\). Its formal kernel is coherent. Do the same for that kernel to obtain \(\widehat Q\to\widehat P\to\mathfrak F\to0\). Full faithfulness algebraizes \(Q\to P\), and exactness identifies the completion of its coherent cokernel with \(\mathfrak F\). The construction never assumes the finite-level kernels themselves form the formal kernel.

**Exercise 8.5 (hard: reconstruct the proper reduction).** Explain why a projective modification and a bounded formal comparison suffice to algebraize a coherent formal module, and prove the fixed bound on its two defects.

**Solution.** Pull the formal module to the quasi-projective Chow modification and algebraize it on its projective closure. Proper support and the Jacobson-radical argument remove the boundary. Let \(H\) be its proper direct image. Formal functions gives the adjunction comparison \(\mathfrak F\to\widehat H\). On an affine of the target, complete the coordinate ring; projective full faithfulness identifies the algebraized pullback with the actual pullback of the finite completed module. Flat base change turns the comparison into an actual adjunction of coherent modules, an isomorphism off the exceptional closed set. The support-power criterion supplies a local power killing kernel and cokernel; a finite cover gives one power. Induction on its exceptional thickening algebraizes both defects. Full faithfulness algebraizes the quotient \(H\to D\), and exactness identifies its kernel's completion with the comparison image. Proposition 3.3 algebraizes the remaining extension by its kernel defect. This is an explicit reconstruction and uses no unproved descent of sheaves along a proper surjection.

**Exercise 8.6 (hard: a special affine existence theorem).** Explain the two features of the affine line that make Proposition 7.1 work.

**Solution.** At the generic point of its closed fiber, the completed ring localized at \((t)\) is a discrete valuation ring. A finite module there has a free-plus-\(t\)-power-torsion normal form, which spreads to \(D(h)\) after completing, using finitely many denominators with nonzero reductions. The zero set of the single-variable polynomial \(h\) has projective closure disjoint from infinity. Thus the standard module can be put on an open neighborhood of the entire boundary, and glued to the original system. Projective existence finishes. In higher dimension a hypersurface's closure can meet the boundary, so this argument does not establish unrestricted affine existence in general.

## References

- **[Stacks]** The Stacks project authors, *The Stacks project*, in its AI Integrated Stacks Project edition: affine formal modules [Tag 087W](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/coherent.html#coherent-lemma-inverse-systems-affine), their abelian category [Tag 087X](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/coherent.html#coherent-lemma-inverse-systems-abelian), exact completion [Tag 0881](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/coherent.html#coherent-lemma-exact), completed Hom [Tag 0882](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/coherent.html#coherent-lemma-completion-internal-hom), full faithfulness [Tag 0883](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/coherent.html#coherent-lemma-fully-faithful).
- Uniform vanishing [Tag 0884](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/coherent.html#coherent-lemma-vanishing-projective), and projective existence [Tag 0885](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/coherent.html#coherent-lemma-existence-projective).
- Parallel open treatments of proper existence are the bounded comparison [Tag 088B](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/coherent.html#coherent-lemma-inverse-systems-push-pull), change of completion [Tag 088A](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/coherent.html#coherent-lemma-existence-tricky), and bounded formal gluing [Tag 0889](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/coherent.html#coherent-lemma-existence-easy). Those references assemble into proper existence [Tag 088C](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/coherent.html#coherent-proposition-existence-proper) and proper-support existence [Tag 088E](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/coherent.html#coherent-theorem-grothendieck-existence).
- These linked reference proofs retain GNU FDL 1.2. Sections 1–6, the affine-line argument, examples and solutions are independently written CC0. Proposition 3.3 proves extension comparison and Section 6 proves the bounded comparison and proper-support reconstruction in the full stated generality. 
