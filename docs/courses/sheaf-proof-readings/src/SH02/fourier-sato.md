# Fourier kernels as radial averaging

The proofs below establish the displayed comparison, cone, equivalence, and section formulas relative to the explicit sheaf-operation prerequisites. The [duality supplement](../../SH02-fourier-duality-normalization.html) supplies conditional proofs of the two duality identities. The separately proved [normalization theorem](../../SH02-fourier-literal-normalization.html), SH02-NDF-SOURCE-MAPS, constructs the unique opposite comparison giving the prescribed paired inverse identities and computes its exact relation to the literal comparison.

The Fourier–Sato definitions and theorem statements are compared with Kashiwara and Schapira, [*Microlocal Study of Sheaves*, Astérisque 128 (1985), §2.1, pp. 39–40](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf#page=42). That section explicitly omits the proofs. The arguments below supply the halfspace comparison and the full vector-bundle inversion through a radial averaging kernel, including the zero section. The source comparison at the end identifies the additional open proof passages and their scope. The examples and problems are independently written; local identifiers belong to this course.

## SH02-FS-SETUP — The two integration rules

Let \(k\) be a commutative ring with identity and finite global dimension. Let \(B\) be a locally compact Hausdorff space and \(\tau:E\to B\) a real vector bundle of constant finite rank \(n\); write \(\pi:E^*\to B\) for its dual. Everything is local on the base, so a locally constant finite rank can instead be treated on its rank components, with the usual boundedness conditions on the operations. In this unit the rank is fixed. No assumption of a field, noetherian coefficients, constructibility, finite rank of coefficient sheaves, compact base, or proper bundle projection is imposed.

Write \(O_E\) for the relative orientation local system on \(B\). Its pullback to \(E\) is the orientation sheaf of the fibers; the relative dualizing complex is \(\tau^{-1}O_E[n]\). Dual bases give a specified **positive dual-orientation identification** \(O_E\simeq O_{E^*}\), and the sign representation gives \(O_E\otimes_k O_E\simeq k_B\). These local systems are locally free of rank one. Tensoring with them needs no derived correction. All other tensor products of complexes below are derived unless one factor is explicitly a flat constant extension sheaf.

An object of \(D^+_{\mathbb R_{>0}}(E;k)\) has bounded-below cohomology sheaves locally constant on every positive scalar orbit. We use the equivalent natural scalar-invariance isomorphism. The zero section is a separate fixed orbit in each fiber; a condition on punctured fibers alone does not determine an object's behavior there.

Set \(X=E\times_B E^*\), with projections \(p:X\to E\), \(q:X\to E^*\), and closed subsets

\[
C=\{(x,\xi):\langle x,\xi\rangle\geq0\},\qquad
N=\{(x,\xi):\langle x,\xi\rangle\leq0\}.
\]

For a locally closed set \(A\), \(k_A\) means the constant sheaf on \(A\), extended by zero using the open embedding followed by the closed embedding. We set \(H_A=H\otimes k_A\) and \(R\Gamma_AH=R\mathcal Hom(k_A,H)\). These are different operations, including when \(A\) is closed.

Define

\[
T_EF=Rq_!((p^{-1}F)_N),\qquad
S_EG=Rp_*R\Gamma_N(q^!G).
\tag{FS1}
\]

Here \(q^!G=q^{-1}G\otimes \rho^{-1}O_E[n]\), where \(\rho:X\to B\). In particular the orientation in this formula is that of the **fiber of \(q\), namely \(E\)**. The negative pairing is used in both definitions. \(T_E\) is left adjoint to \(S_E\): tensor–Hom adjunction, \(q_!\dashv q^!\), and \(p^{-1}\dashv Rp_*\) give, in order,

\[
R\operatorname{Hom}(T_EF,G)
\simeq R\operatorname{Hom}((p^{-1}F)_N,q^!G)
\simeq R\operatorname{Hom}(F,S_EG).
\tag{FS2}
\]

The notation is derived \(k\)-module Hom, so this includes all degree shifts and identifies the actual adjunction. The usual finite-dimensional fiber bounds and the bounded flat kernels ensure that these operations preserve the indicated bounded-below categories. Scalar equivariance preserves conicity. The proper-support symbol \(!\) in FS1 is essential: \(p\) and \(q\) usually are not proper.

The imported operation package consists of the open–closed localization triangles, proper-support base change and its stalk formula, projection formula, composition of proper-support images, tensor–Hom adjunction, exceptional inverse image for a real vector-bundle projection, and the relative orientation trace. We also use conic contraction: for a vector-bundle projection \(r\), zero section \(i\), and conic \(H\), the natural maps identify \(Rr_*H\) with \(i^{-1}H\) and \(Rr_!H\) with \(i^!H\). 

## SH02-FS-HALFSPACE — Compactly supported cohomology that detects a boundary

The following elementary facts are used to calculate kernels, rather than to infer a global sheaf from an unconstructed collection of stalk isomorphisms.

**Lemma.** For a nonempty open convex subset \(U\) of an oriented real \(n\)-space, the orientation trace identifies \(R\Gamma_c(U;k)\) with \(k[-n]\). The extension map induced by an inclusion of two such open sets is the identity under their traces. A closed halfspace in a positive-dimensional vector space has zero compactly supported cohomology. More generally a nonzero closed convex cone containing no line has zero compactly supported cohomology. Finally, if \(U\) is open convex and \(\ell\) is linear, then

\[
R\Gamma_c(U\cap\{\ell\leq0\};k)=0
\quad\text{if }U\cap\{\ell>0\}\ne\varnothing.
\tag{FS3}
\]

**Proof.** An open convex set is contractible and is a manifold with the inherited orientation. Poincaré duality for this manifold identifies its compactly supported cohomology with the dual orientation generator in degree \(n\); no dualization of a coefficient module is involved. Naturality of the orientation trace for an open inclusion identifies the map on this generator. One can equivalently use an orientation-preserving radial homeomorphism with \(\mathbb R^n\): after selecting an interior point, the Minkowski gauge of the translated open convex set gives a continuous radial reparametrization, including the directions in which the radial endpoint is infinite.

The localization triangle for the closed halfline in \(\mathbb R\) reduces its compactly supported cohomology to the extension map from an open halfline to \(\mathbb R\). Both are oriented one-manifolds and that map is an isomorphism by the preceding paragraph. A closed halfspace is a product of a closed halfline with a Euclidean space, so the proper-support projection formula gives the asserted vanishing.

For the cone assertion, finite-dimensional separation supplies a linear functional strictly positive on every nonzero point of the cone. Its level-one slice \(A\) is nonempty compact convex. The cone is the quotient of \(A\times[0,\infty)\) that identifies \(A\times\{0\}\). Its one-point compactification is the suspension of \(A\): the other endpoint is the point at infinity. Since \(A\) is contractible, this suspension is contractible. The identification of compactly supported sheaf cohomology with reduced cohomology of this compactification therefore gives zero. These spaces are locally contractible metrizable spaces, so the comparison with singular cohomology applies. This argument explains why the prohibition on lines matters: a vector subspace has nonzero top compactly supported cohomology.

For FS3 apply compactly supported cohomology to
\(k_{U\cap\{\ell>0\}}\to k_U\to k_{U\cap\{\ell\leq0\}}\to\).
When the first open set is nonempty it, too, is open convex of dimension \(n\). Its map to the middle term is an isomorphism by trace compatibility, so the third term vanishes. This proof covers both a genuine cut and the case where the intersection with the closed halfspace is empty. Rank zero is handled directly: the only nonempty fiber is a point. \(\square\)

## SH02-FS-COMPARE — Why ordinary image and proper-support image agree in the transform

**Theorem.** There are natural isomorphisms

\[
T_EF\simeq Rq_*R\Gamma_C(p^{-1}F),\qquad
S_EG\simeq Rp_!((q^!G)_C).
\tag{FS4}
\]

**Proof of the first isomorphism.** Put \(L=p^{-1}F\) and \(H=R\Gamma_CL\). First we construct the local-support interchange

\[
R\Gamma_C(L_N)\simeq H_N.
\tag{FS5}
\]

The open complement \(W=X\setminus N\) lies in the interior of \(C\), and its closure lies in \(C\). Thus \(R\Gamma_C(L_W)=L_W\). Apply \(R\Gamma_C\) to the localization triangle \(L_W\to L\to L_N\to\). The first two terms identify with the first two terms of \(H_W\to H\to H_N\to\), because \(H|_W=L|_W\). The functorial localization construction identifies their third terms, proving FS5. This is a special consequence of the two complementary halfspace inequalities, not an assertion that restriction to an arbitrary closed set commutes with arbitrary local cohomology.

Next \(H_N\) is supported on \(\{0\}\times_BE^*\). Indeed, near a point with \(x\ne0\), choose a bundle coordinate in the \(\xi\)-variable equal to \(t=\langle x,\xi\rangle\). Complete it by coordinates in the kernel of that nonzero linear functional. This is a local change of fiber coordinates over the \(x\)-space. In these coordinates \(L\) is pulled back from the remaining variables and \(C=\{t\geq0\}\), \(N=\{t\leq0\}\). The triangle defining \(R\Gamma_{t\geq0}\) shows that its stalk at \(t=0\) is zero: the restriction from an interval to its negative half-interval induces the identity on the pulled-back coefficient complex. This last assertion follows by taking product neighborhoods and the contractible-interval projection formula, and then the filtered colimit over those neighborhoods. Its restriction to \(t<0\) is zero as well. Hence its restriction to \(N\) vanishes. This works with an arbitrary bounded-below coefficient complex on the remaining locally compact base.

All four objects \(L,L_N,H,H_N\) are conic in the \(x\)-fiber. Let \(i:E^*\to X\) be its zero section. The morphism \(R\Gamma_C(L_N)\to L_N\) becomes an isomorphism after \(Rq_!\): conic contraction identifies this with applying \(i^!\), and \(i^!R\Gamma_C=i^!\) because the zero section lies in \(C\). The map \(H\to H_N\) becomes an isomorphism after \(Rq_*\): conic contraction identifies this with applying \(i^{-1}\), which sees no change on restricting to \(N\). Finally, the natural map \(Rq_!(H_N)\to Rq_*(H_N)\) is an isomorphism because \(H_N\) is supported on the zero section, where \(q\) is the identity and is proper. Therefore the following chain, with its displayed arrows, constructs FS4:

\[
Rq_!(L_N)\ \longleftarrow\ Rq_!R\Gamma_C(L_N)
\ \simeq\ Rq_!(H_N)\ \longrightarrow\ Rq_*(H_N)
\ \longleftarrow\ Rq_*H.
\tag{FS6}
\]

Each arrow is now proved invertible. No assertion that \(q\) itself is proper has been used. Interchange the vector bundle and its dual, reverse the two inequalities, and include the base-pulled orientation complex in the coefficient object. The same argument gives the second isomorphism of FS4. \(\square\)

## SH02-FS-CONE — Two cone formulas, with their boundary conventions

For a subset \(A\subset E\), define

\[
A^\circ=\{\xi\in E^*: \pi(\xi)\in\tau(A),\ 
\langle x,\xi\rangle\geq0\text{ for every }x\in A_{\pi(\xi)}\}.
\]

The requirement \(\pi(\xi)\in\tau(A)\) is part of this definition. An empty fiber does not acquire the whole dual fiber through a vacuous inequality. Let \(a\) denote fiberwise negation. Convexity and absence of lines below are fiberwise conditions; openness and closedness are in the total bundle topology.

**Theorem.** If \(\gamma\subset E\) is a closed convex cone containing the entire zero section and each fiber contains no line, then

\[
T_Ek_\gamma\simeq k_{\operatorname{Int}(\gamma^\circ)}.
\tag{FS7}
\]

Here \(\operatorname{Int}\) is total-space interior. If \(U\subset E\) is an open fiberwise convex cone, possibly with empty fibers, then

\[
T_Ek_U\simeq k_{(U^\circ)^a}\otimes\pi^{-1}O_E[-n].
\tag{FS8}
\]

**Proof.** By proper-support base change, the stalk in FS7 is the compactly supported cohomology of
\(\gamma_b\cap\{x:\langle x,\xi\rangle\leq0\}\).
This is a closed cone containing no line. It is \(\{0\}\) exactly when the pairing is strictly positive on every nonzero point of \(\gamma_b\); otherwise it is a nonzero cone and the lemma gives zero.

The strict-positivity locus just described is precisely \(\operatorname{Int}(\gamma^\circ)\). To verify the statement in the total topology, trivialize near \(b\) and intersect \(\gamma\) with the unit-sphere bundle. Its projection is closed locally, because the sphere is compact. Strict positivity on the compact fiber slice consequently persists on a neighborhood of \((b,\xi)\). If the slice is empty, the same compactness argument shows that it remains empty on a base neighborhood. Conversely a nonzero \(x\in\gamma_b\) with \(\langle x,\xi\rangle\leq0\) prevents interior: a small perturbation of \(\xi\) makes the pairing negative if necessary. This also covers \(\gamma_b=\{0\}\); it must not be replaced by an argument assuming a full-dimensional cone.

To produce the sheaf isomorphism, use the restriction morphism \(k_\gamma\to k_{0_B}\). Its transform maps \(T_Ek_\gamma\) to \(k_{E^*}\). On the open strict-positivity locus, its fiber is the identity of the point \(\{0\}\), so restriction gives a sheaf isomorphism there. Off that open set the transform has zero stalks. The open–closed localization triangle then identifies it with extension by zero of that constant restriction. This constructs FS7 rather than merely listing its stalks.

For FS8 put \(B_0=\tau(U)\), an open subset of \(B\), and first work over \(B_0\). There every \(U_b\) is nonempty open convex of dimension \(n\). Set \(D=(U^\circ)^a\). It is closed in \(E^*|_{B_0}\): its complement is the projection of the open set where \(x\in U\) and \(\langle x,\xi\rangle>0\), and that projection is open. For \(\xi\notin D\), FS3 makes the transform stalk zero. On \(D\), the negative halfspace contains the whole of \(U_b\). Restriction and proper-support base change therefore identify the transform with the proper-support image of the open subset \(U\times_{B_0}D\) of the rank-\(n\) bundle over \(D\). Its relative orientation trace is an isomorphism, since every fiber is nonempty open convex. This gives \(\pi^{-1}O_E[-n]\) on \(D\). Closed extension in \(E^*|_{B_0}\) constructs the claimed object there. Finally, base-change compatibility with extension by zero from the open base \(B_0\) proves FS8 on \(E^*\). Thus \(D\) is allowed to be only locally closed in the full total space. \(\square\)

## SH02-FS-KERNEL — A kernel identity that remembers gluing at the zero section

The next calculation is the main inversion argument. Matching only the stalks of its final two objects would leave their extension across the zero section undetermined.

Let \(Y=E\times_BE\), with points denoted \((x,y)\). Over \(Y\), integrate \(\xi\in E^*_b\). Write \(r\) for that projection and put \(u=\langle x,\xi\rangle\), \(v=\langle y,\xi\rangle\). Define

\[
K=Rr_!k_{\{u\leq0,\ v\geq0\}}\otimes O_{E^*}[n],
\quad h(y,s)=(sy,y),\quad s\geq0,
\quad h_+=h|_{s>0}.
\]

Orientation sheaves in this paragraph are pulled back from \(B\).

**Kernel lemma.** There is a natural isomorphism

\[
K\simeq R(h_+)_!k_{E\times(0,\infty)}[1].
\tag{FS9}
\]

**Proof.** Cut the inequality \(u\leq0\) by \(v<0\) and its complement. This gives a specified triangle

\[
J\longrightarrow D\longrightarrow K\longrightarrow J[1],
\quad
J=Rr_!k_{\{u\leq0,v<0\}}\otimes O_{E^*}[n],
\quad D=Rr_!k_{\{u\leq0\}}\otimes O_{E^*}[n].
\tag{FS10}
\]

Put \(Z=\{x=0\}\), \(V=\{y\ne0\}\), and
\(A=\{(x,y)\in V:x=sy\text{ for some }s\geq0\}\).
The latter is closed in \(V\). This can be checked in a local trivialization by choosing a linear functional nonzero on \(y\); on a smaller neighborhood the scalar \(s\), when it exists, is the continuous quotient of that functional on \(x\) and \(y\). Write \(i:A\hookrightarrow V\) and \(j:V\hookrightarrow Y\).

The restriction from the full vector bundle to \(u\leq0\), together with orientation trace for the full bundle, constructs a morphism \(k_Y\to D\). At \(x=0\) it is the identity trace. At \(x\ne0\) the fiber is a closed halfspace and its compactly supported cohomology is zero. Restricting the constructed morphism to \(Z\), and then using closed extension, gives
\(D\simeq k_Z\).

On \(V\), integration of the open halfspace \(v<0\), with the same orientation twist, is canonically \(k_V\). Restriction to \(u\leq0\) constructs a map from this sheaf to \(J|_V\). If \(x=sy\) with \(s\geq0\), that restriction does nothing to the fiber. If \(x\) is a negative multiple of \(y\), the fiber is empty. If \(x,y\) are independent, the fiber is a product of a closed halfline, an open halfline, and \(\mathbb R^{n-2}\), whose compactly supported cohomology is zero. At \(y=0\) the strict inequality \(v<0\) is impossible. These cases, and restriction of the constructed map to \(A\), give
\(J\simeq j_!i_*k_A\).
In particular \(J\) and \(D\) are actual sheaves in degree zero.

Under these identifications the arrow \(J\to D\) in FS10 is restriction to \(A\cap Z\), followed by extension by zero from \(Z\cap V\) into \(Z\). At a point \((0,y)\) with \(y\ne0\), the map is the compact-support extension from an open halfspace to the full fiber, and the orientation traces make it the identity. At every other stalk either the source or the target is zero. Equality here is equality of **already constructed maps between degree-zero sheaves**, so checking their stalk maps proves equality of the maps themselves.

Now apply \(Rh_!\) to the open–closed triangle in the scalar parameter. Rotating once gives

\[
Rh_!k_{E\times[0,\infty)}\longrightarrow k_Z
\longrightarrow R(h_+)_!k_{E\times(0,\infty)}[1]\longrightarrow.
\tag{FS11}
\]

Over \(V\), \(h\) is a homeomorphism onto the closed set \(A\). Over the zero pair its fiber is the closed halfline, with vanishing compactly supported cohomology. Hence restriction over \(V\), followed by extension by zero, identifies the first term with \(j_!i_*k_A\). Its arrow to \(k_Z\) is exactly the restriction morphism just identified in FS10: it is the identity at \((0,y)\), \(y\ne0\), and all other relevant stalk maps are zero.

Thus FS10 and FS11 are cofibers of the same identified sheaf morphism. Use the functorial cofiber in the usual derived enhancement, or the explicit cone of this degree-zero map; this gives FS9 naturally. An arbitrary nonfunctorial choice of a triangulated-category cone is unnecessary. All constructions use restriction, extension, and orientation trace, so they glue over the base. Rank zero is included: \(J=0\), \(D=k_B\), and the positive halfline shifted by one has compactly supported cohomology \(k\). \(\square\)

## SH02-FS-INVERSION — Inversion and the same-sign square

**Theorem.** The functors \(T_E\) and \(S_E\) are inverse equivalences between \(D^+_{\mathbb R_{>0}}(E;k)\) and \(D^+_{\mathbb R_{>0}}(E^*;k)\). In particular the unit and counit of the adjunction FS2 are isomorphisms. If \(T_{E^*}\) uses the same nonpositive pairing convention as \(T_E\), then

\[
T_{E^*}T_EF\simeq a^{-1}F\otimes\tau^{-1}O_E[-n].
\tag{FS12}
\]

**Proof.** Use the second description of \(S_E\) in FS4. Composition of proper-support kernel functors, base change, and projection formula identify \(S_ET_E\) with the kernel \(K\) of FS9. More explicitly, in the triple product the two restrictions are precisely \(\langle x,\xi\rangle\leq0\) and \(\langle y,\xi\rangle\geq0\). The exceptional inverse image in \(S_E\) contributes \(O_E[n]\); to integrate the intermediate fiber \(E^*\), identify this with \(O_{E^*}[n]\) by the specified positive dual-orientation identification. The intersection kernel is the tensor product of the two flat constant-extension kernels. No properness is imposed on their common support; it is proper-support integration that composes.

After FS9, projection formula for \(h_+\) turns this kernel operation into

\[
R\operatorname{pr}_!\mu^{-1}F[1],\qquad
\operatorname{pr}(y,s)=y,\quad \mu(y,s)=sy,\quad s>0.
\]

Conicity identifies \(\mu^{-1}F\) with \(\operatorname{pr}^{-1}F\), naturally also over the fixed zero section. Proper-support projection formula and the oriented positive halfline give
\(R\operatorname{pr}_!\operatorname{pr}^{-1}F[1]\simeq F\).
This constructs a natural isomorphism \(S_ET_E\simeq\mathrm{id}\).

For \(T_ES_E\), the intermediate fiber is \(E\), its orientation twist is already \(O_E[n]\), and its two inequalities are \(\langle x,\xi\rangle\geq0\), \(\langle x,\eta\rangle\leq0\). Apply the same kernel proof with the perfect pairing replaced by its negative. It gives the radial relation \(\xi=s\eta\), \(s>0\), and the same averaging argument gives \(T_ES_E\simeq\mathrm{id}\). These two natural isomorphisms establish equivalence. A right adjoint to an equivalence has invertible adjunction unit and counit, so the actual unit and counit of FS2 are isomorphisms as well. This last categorical step asserts invertibility; it does not identify a separately constructed radial map with a particular normalized adjunction map.

Finally the positive-kernel expression for \(S_E\) directly gives
\[
S_EG\simeq a^{-1}(T_{E^*}G)\otimes\tau^{-1}O_E[n].
\]
Insert \(G=T_EF\), apply the just-proved inversion, and cancel the orientation line using \(O_E^{\otimes2}\simeq k_B\). Negation is an involution and fixes every base-pulled local system. This yields FS12, including both its antipode and its shift. \(\square\)

### SH02-FS-NORMALIZATION — What is and is not normalized

FS2 names a specific adjunction and FS6 names a specific comparison. The equivalence proof establishes invertibility without claiming that all isomorphisms arising from these constructions are literally equal.

There are two concrete signs to retain. In the scalar triangle used in FS11, with the increasing coordinate \(s\) as orientation, the connecting map from the endpoint class to \(H_c^1((0,\infty);k)\) is minus the integration generator. For example, a cutoff equal to one near zero and zero near infinity has differential of integral \(-1\). This calculation may be read over \(\mathbb R\) to fix the integral sign convention; the sign itself is the same cellular boundary sign over every \(k\). Changing to \(t=1/s\) reverses orientation. Independently, the orientation identification induced by a negative-definite identification \(E\to E^*\) differs from positive dual orientation by \((-1)^n\). Indeed, in a positive orthonormal basis its matrix is \(-I_n\), of determinant sign \((-1)^n\); the calculation is local and does not require a globally chosen metric.

#### SH02-FS-NORM-OPEN — Equality of normalized adjunction maps

**Normalization theorem.** With FS6 as the first comparison and the prescribed negative-definite trace identification in the second adjunction, [The geometric normalization of Fourier adjunctions](../../SH02-fourier-literal-normalization.html), SH02-NDF-SOURCE-MAPS, constructs the unique second comparison for which both pairs of adjunction maps are inverse. It is \(d_{\rm adj}=(-1)^n d_{\rm lit}\), where the literal comparison is the explicit reversed-halfspace chain NDF2. NDF4 computes its complete natural-transformation defect before NDF5–NDF10 prove the two inverse equations and uniqueness. This is a theorem about the two explicit course comparisons. It does not identify an unspecified comparison in another treatment or settle a later microlocal mate.

## SH02-FS-SECTIONS — Testing a transform on regions

Derived sections on an open set \(V\) mean \(R\operatorname{Hom}(k_V,-)\). For a locally closed set \(A\), define \(R\Gamma_A(Y;F)=R\operatorname{Hom}(k_A,F)\); this convention makes sense even when \(A\) is closed only over an open part of the base.

**Corollary.** For an open fiberwise convex cone \(V\subset E^*\),

\[
R\Gamma(V;T_EF)\simeq R\Gamma_{V^\circ}(E;F).
\tag{FS13}
\]

For a closed fiberwise convex cone \(\delta\subset E^*\), containing the zero section and containing no line in any fiber,

\[
R\Gamma_\delta(E^*;T_EF)
\simeq
R\Gamma(\operatorname{Int}((\delta^\circ)^a);
F\otimes\tau^{-1}O_E)[-n].
\tag{FS14}
\]

**Proof.** Apply the fully faithful inverse equivalence to both arguments of derived Hom. FS8 and the positive-kernel expression for \(S_E\) give \(S_Ek_V\simeq k_{V^\circ}\): the two shifts cancel and the two dual orientation lines contract. Consequently
\(R\operatorname{Hom}(k_V,T_EF)\simeq R\operatorname{Hom}(k_{V^\circ},F)\), proving FS13. Empty base fibers are governed by the definition of polar and locally closed extension, exactly as in FS8.

Likewise FS7 gives
\(S_Ek_\delta\simeq k_{\operatorname{Int}((\delta^\circ)^a)}\otimes\tau^{-1}O_E[n]\).
Move the locally free orientation line and the shift across derived Hom, and use the characterization of derived sections on an open set. This proves FS14. The orientation factor stays **inside** derived global sections: on a nontrivial bundle it is not a fixed coefficient module that can be moved outside. \(\square\)

## SH02-FS-EXAMPLES — Worked checks over integral coefficients

1. **A nonsymmetric wedge.** Work over a point with \(k=\mathbb Z\) and \(E=\mathbb R^2\). Let \(\gamma=\{(u,v):u\geq v\geq0\}\), generated by \((1,0)\) and \((1,1)\). Its polar is \(\{(\alpha,\beta):\alpha\geq0,\ \alpha+\beta\geq0\}\). Thus
   \[
   T_Ek_\gamma=k_{\{\alpha>0,\ \alpha+\beta>0\}}.
   \]
   At \((\alpha,\beta)=(0,1)\), the compact-support fiber is the closed ray generated by \((1,0)\), so the transform stalk is zero. This checks that the boundary is excluded. For \(U=\{u>v>0\}\), the answer instead is
   \[
   T_Ek_U=k_{\{\alpha\leq0,\ \alpha+\beta\leq0\}}[-2]
   \]
   after choosing the usual orientation. At \((0,-1)\), all of \(U\) survives the inequality and its compactly supported cohomology is \(\mathbb Z[-2]\); the boundary is included.

2. **A coefficient sheaf with torsion on a nonorientable bundle.** Let \(E\to S^1\) be the Möbius real line bundle and \(M\) the constant \(\mathbb Z/6\)-sheaf on the base, regarded as a sheaf of \(\mathbb Z\)-modules. Projection formula and FS8 with \(U=E\) give
   \[
   T_E(\tau^{-1}M)=i_*\bigl(M\otimes O_E\bigr)[-1],
   \]
   where \(i\) is the zero section of \(E^*\). The monodromy on the displayed coefficient module is multiplication by \(-1\), which is nontrivial modulo six. The coefficient ring is \(\mathbb Z\), of finite global dimension; the example does not incorrectly take the quotient \(\mathbb Z/6\) itself as a finite-global-dimension base ring. Omitting the orientation line would change the answer.

3. **A cone whose base behavior matters.** In \(E=\mathbb R_b\times\mathbb R_x\), let \(\gamma\) be the union of the zero section and \(\{b=0,x\geq0\}\). It is closed, conic, and fiberwise proper convex. Its polar is the whole dual fiber for \(b\ne0\), and \(\xi\geq0\) for \(b=0\). The transform is the constant extension on the open set
   \[
   \{b\ne0\}\ \cup\ \{b=0,\xi>0\}.
   \]
   At \((b,\xi)=(0,0)\) the transform is zero. This example forces one to check total-space interior and the gluing supplied by the sheaf map in the proof; it is not a bundle of cones with constant combinatorics.

## SH02-FS-PROBLEMS — Problems with solutions

**Problem 1.** Let \(M\in D^+(B;k)\) be arbitrary. Compute the transforms of \(i_*M\) and \(\tau^{-1}M\), where \(i:B\hookrightarrow E\) is the zero section. Explain why \(M\) need not have finite-rank cohomology.

**Solution.** On the zero section the negative-pairing restriction is automatic and \(q\) restricts to the identity of \(E^*\), so \(T_Ei_*M=\pi^{-1}M\). FS8 for \(U=E\), followed by projection formula, gives
\(T_E\tau^{-1}M=i'_* (M\otimes O_E)[-n]\).
Only tensoring with flat constant-extension kernels and a locally free orientation line occurs. The proper-support projection formula used here has no finite-rank requirement on \(M\); it is part of the stated bounded derived operation package.

**Problem 2.** Over a point and with \(E=\mathbb R\) oriented, compute \(T_Ek_{[0,\infty)}\), then apply the same-sign transform again. Check FS12 including its antipode.

**Solution.** FS7 gives \(k_{(0,\infty)}\). FS8 gives \(k_{(-\infty,0]}[-1]\) for its next transform. This is \(a^{-1}k_{[0,\infty)}[-1]\). The change from a closed ray to an open ray on the first step and back to a closed ray on the second is essential; discarding the endpoint on the last step would contradict inversion.

**Problem 3.** In the proof of FS9, why does the fiber calculation alone not establish the kernel isomorphism? Give the missing data and explain where they were supplied.

**Solution.** Stalk modules with the same dimensions and degrees can have different specialization maps and extension classes across a closed stratum. Here the positive radial locus meets the zero pair. The proof constructs \(J\) and \(D\) as degree-zero sheaves using restriction maps and traces, identifies the actual sheaf morphism \(J\to D\) with the radial boundary restriction, and takes its functorial cofiber. Equality of the two already constructed sheaf maps is checked stalkwise. This supplies the gluing data that a bare stalk inventory would lack.

**Problem 4.** Explain why a closed linear subspace cannot replace the cone hypothesis in FS7, and compute the transform of a linear subspace \(L\subset E\) over a point.

**Solution.** Let \(d=\dim L\). If \(\xi\notin L^\perp\), the negative-pairing slice in \(L\) is a closed halfspace and has zero compactly supported cohomology. If \(\xi\in L^\perp\), it is all of \(L\), with compactly supported cohomology \(\operatorname{or}(L)[-d]\). Restriction to the closed annihilator, followed by its relative orientation trace, constructs
\(T_Ek_L=k_{L^\perp}\otimes\operatorname{or}(L)[-d]\).
For \(d>0\), the interior of \(L^\perp\) in \(E^*\) is empty, so FS7 would falsely predict zero. A cone containing a line fails exactly the vanishing lemma used there. This calculation is an additional example, not an unauthorized weakening of that lemma's assumptions.

## SH02-FS-SOURCES — Source comparison and the proof across the zero section

Astérisque 128, Proposition 2.1.1 and Definition 2.1.2, give the two presentations used in FS1 and FS4. Theorem 2.1.3(i) states inversion on the bounded-below conic category over a locally compact base. Proposition 2.1.4 gives convex-region section formulas. Those statements identify the classical results; their omitted proofs are not programme proof providers. In particular, FS13–FS14 are the precise conic-region formulas proved here, with the orientation factor kept inside global sections.

Schapira's [*A short review on microlocal sheaf theory*, 19 January 2016, §4.1, Definition 4.1, Theorem 4.2 and Example 4.3(i)–(ii), pp. 19–20](https://webusers.imj-prg.fr/~pierre.schapira/LectNotes/MuShv.pdf#page=19) provides the bounded, real-manifold comparison for the transforms and the open and closed cone formulas. Its examples specify the antipode, interior and orientation shift. The proofs here retain the stated locally compact base and bounded-below range; the torsion, varying-base and nonorientable examples test features not determined by the pointwise formulas alone.

A proof comparison is available in Schapira's [*An Introduction to Sheaves on Grothendieck Topologies*, 1 August 2026, §5.4, pp. 111–115](https://webusers.imj-prg.fr/~pierre.schapira/LectNotes/SHV.pdf#page=111). Lemma 5.4.2 reduces the halfspace comparison to a product coordinate and the vanishing for a closed halfline. Theorem 5.4.3 then proves inversion for sphere bundles through a convolution kernel. The vector-bundle theorem is stated separately as Theorem 5.4.6; the sphere argument does not by itself recover a conic sheaf's extension at the zero section.

FS5–FS6 construct the comparison on the full bundle: the two support inequalities give a localization comparison, the product-coordinate calculation puts its remaining support on the zero section, and properness on that support compares the two direct images. FS9–FS11 then identify two degree-zero sheaves and the actual restriction map between them. Taking its specified cofiber retains the gluing at the zero pair. This is the step needed before radial averaging can establish inversion; matching compact-support stalk groups alone would not supply it. The positive and negative orientation conventions, and the distinct adjunction normalization, remain as stated above.

The foundational comparison is with SHV, Theorem 4.5.3 (proper-support base change), Theorem 4.4.7 (the bounded projection formula), and Theorem 4.6.1 (exceptional adjunction). The bounded-below uses, conic contraction, orientation trace, singular/sheaf comparison for the pointed-cone compactification, and functorial derived cofibers retain their explicit programme proof obligations. The companion duality reading gives the truncation argument that extends the bounded projection formula in the range it uses. No source reference replaces these requirements. The source prose and diagrams are not incorporated; independently written programme text is CC0 and actual human components retain their recorded terms.

## SH02-FS-OPEN — Exact continuation boundary

The comparison formulas FS4, cone formulas FS7–FS8, kernel lemma FS9, equivalence and square FS12, and section formulas FS13–FS14 have proofs in this draft relative to the named operation and conic-contraction prerequisites. Each comparison uses the specified kernel map and retains the hypotheses of those prerequisites.

### SH02-FS-DUALITY-OPEN — Historical pointer to the duality proofs

The former writing gap is addressed by [SH02-FDN-BASE](../../SH02-fourier-duality-normalization.html#SH02-FDN-BASE) and [SH02-FDN-DUALITIES](../../SH02-fourier-duality-normalization.html#SH02-FDN-DUALITIES) in the duality supplement, which retain the precise boundedness and ambient dualizing hypotheses. Bundle-map functoriality, specialization, microlocalization, microlocal Hom, microsupport estimates, and involutivity have their own course units and ledgers; none is certified by this unit.
