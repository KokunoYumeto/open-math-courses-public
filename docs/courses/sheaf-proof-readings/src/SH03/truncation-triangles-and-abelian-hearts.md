# Truncation triangles and abelian hearts

A triangulated category supplies cones and connecting maps. A t-structure specifies which part of an object lies below a degree and which part lies above it. Its degree-zero objects form an abelian category: the kernel and cokernel of a map are the two cohomology objects of its cone. The octahedral axiom identifies their image and coimage. We prove these statements, including the exactness of the resulting cohomology sequence, before using them to construct perverse sheaves.

*AI-generated exposition: GPT-6.1 Sol and GPT-6 Astra (OpenAI), Ultra. Edition: 5 October 2026. Independently written lesson text: CC0. Human mathematical sources are credited below.*

We use the axioms of a triangulated category: shifts, distinguished triangles, completion of a commuting square to a triangle map, the exact Hom sequences, and the octahedral axiom for composable arrows. These are the ambient categorical structure assumed in the theorem. All t-structure arguments are proved below. For the constructible example alone, Constructible costalks and Verdier duality supplies the already written bounded constructible duality equivalence, with its exact sheaf and geometric prerequisites.

## The cone that the heart must recover

Start with the module map \(f:\mathbb Z^2\to\mathbb Z\), \(f(a,b)=2a+4b\). Its cone is
\[
 C=[\,\mathbb Z^2\xrightarrow{(2,4)}\mathbb Z\,]
        \quad\text{in degrees }-1,0.
 \tag{T1}
\]
The kernel is \(\mathbb Z(-2,1)\); the cokernel is \(\mathbb Z/2\). A lower cut at \(-1\) must keep that kernel, with its actual inclusion into \(\mathbb Z^2\). An upper cut at zero must keep the quotient map \(\mathbb Z\to\mathbb Z/2\). Simply deleting a term gives the wrong object. The fixed interval diagram uses this same row as one of its attachments, so these kernel maps will return in its directional test.

Maps matter even when the objects are familiar. The sequence
\[
 0\longrightarrow\mathbb Z\xrightarrow{6}\mathbb Z
   \longrightarrow\mathbb Z/6\longrightarrow0
 \tag{T2}
\]
has connecting class \(1\in
\operatorname{Hom}_{D^b(\mathbb Z)}(\mathbb Z/6,\mathbb Z[1])
=\mathbb Z/6\). Represent the quotient by its two-term free resolution; the boundary is identity on the negative term, and homotopy changes that integer by a multiple of six. Thus this class is nonzero. No lift of the quotient generator to a six-torsion element in \(\mathbb Z\) exists. A heart must recover the nonsplit sequence and its connecting arrow, rather than only its three terms. Both calculations remain complete exercises below.

We now extract from this cone problem the axioms and constructions valid in any triangulated category. The abstract proof uses its triangulated axioms and exact Hom sequences. The optional constructible-duality branch comes after the abstract theorem and its exercises.

## The degree convention and the three axioms

Let \(\mathcal D\) be a triangulated category. Full subcategories below are closed under isomorphisms. Given \(\mathcal D^{\le0},\mathcal D^{\ge0}\), put

\[
 \mathcal D^{\le n}=\mathcal D^{\le0}[-n],\qquad
 \mathcal D^{\ge n}=\mathcal D^{\ge0}[-n],\qquad
 \mathcal A=\mathcal D^{\le0}\cap\mathcal D^{\ge0}.
 \tag{1}
\]

Thus \([1]\) lowers a cohomological degree. A **t-structure** satisfies

\[
\begin{gathered}
 \mathcal D^{\le-1}\subset\mathcal D^{\le0},\qquad
 \mathcal D^{\ge1}\subset\mathcal D^{\ge0},\\
 \operatorname{Hom}(U,V)=0
       \quad(U\in\mathcal D^{\le0},\ V\in\mathcal D^{\ge1}),\\
 U\longrightarrow X\longrightarrow V\longrightarrow U[1]
       \quad(U\in\mathcal D^{\le0},\ V\in\mathcal D^{\ge1})
       \quad\text{for every }X.
\end{gathered}
\tag{2}
\]

The last line asserts existence of a distinguished triangle. The subcategory \(\mathcal A\) is its **heart**. Shifting (2) gives the same assertions at every integer cut.

In the opposite triangulated category the shift is the original \([-1]\). Reversing a triangle and its Hom sequence makes
\(( (\mathcal D^{\ge0})^{\mathrm{op}},(\mathcal D^{\le0})^{\mathrm{op}} )\)
a t-structure. Replacing both halves by \(\mathcal D^{\le s},\mathcal D^{\ge s}\) also satisfies the axioms, by shifting (2). Its heart is \(\mathcal A[-s]\).

## The standard and dual constructible examples

For any abelian category \(\mathcal B\), the standard halves of \(D(\mathcal B)\) are the complexes whose cohomology vanishes in positive degrees or in negative degrees. Smart truncation puts \(\ker d^0\) at the top of the lower complex and \(\operatorname{coker}d^0\) at the bottom of the upper complex. The quotient of the original complex by its lower truncation maps quasi-isomorphically to the upper one: its extra two-term part is \(\operatorname{im}d^0\xrightarrow{1}\operatorname{im}d^0\), which is acyclic. This gives (2)'s triangle.

Orthogonality can be checked on roofs. Replace the source of a roof for a lower object by its lower smart truncation, still a quasi-isomorphism; replace the upper target by its upper smart truncation. A chain map from a complex in degrees at most zero to one in degrees at least one is zero. Thus the represented derived map is zero. Nesting is immediate from cohomological degrees. The heart is \(\mathcal B\): a complex with only degree-zero cohomology truncates to that object in degree zero. For two such objects, the same roof calculation identifies derived degree-zero Hom with their ordinary Hom, by factoring the degree-zero component through its cohomology.

## A truncation is characterized by its adjunction

Choose a triangle at cut \(n\), with first term \(U_X\in\mathcal D^{\le n}\) and third term \(V_X\in\mathcal D^{\ge n+1}\). If \(W\in\mathcal D^{\le n}\), both \(\operatorname{Hom}(W,V_X)\) and \(\operatorname{Hom}(W,V_X[-1])\) vanish: the second target lies in \(\mathcal D^{\ge n+2}\). The Hom sequence therefore gives

\[
 \operatorname{Hom}(W,U_X)\xrightarrow{\sim}\operatorname{Hom}(W,X).
 \tag{3}
\]

Dually, for \(W\in\mathcal D^{\ge n+1}\), the groups
\(\operatorname{Hom}(U_X,W)\) and \(\operatorname{Hom}(U_X[1],W)\)
vanish. Hence \(\operatorname{Hom}(V_X,W)\simeq\operatorname{Hom}(X,W)\).

Representing these two Hom functors defines the truncations
\(\tau^{\le n}X=U_X\) and \(\tau^{\ge n+1}X=V_X\), uniquely up to the unique isomorphism preserving their maps to and from \(X\). For \(f:X\to Y\), (3) gives the unique first arrow commuting with \(f\), and the dual statement gives the unique third arrow. Uniqueness proves identity and composition compatibility. Thus these are functors: the right adjoint and left adjoint, respectively, to the indicated inclusions.

Their connecting arrow is also canonical. More generally, suppose two distinguished triangles have the same first two arrows \(U\to X\to V\). Complete their identity square to a triangle map with third component \(a:V\to V\). Since \(a\) fixes the arrow \(X\to V\), exactness of Hom makes \(1-a\) factor through \(U[1]\to V\). If \(\operatorname{Hom}(U[1],V)=0\), then \(a=1\) and the two connecting arrows agree. In a truncation triangle this vanishing follows from \(U[1]\in\mathcal D^{\le n-1}\), \(V\in\mathcal D^{\ge n+1}\).

Completing the square for an arbitrary \(f\) now gives a triangle map whose first and third arrows are exactly the adjoint-defined ones. Its last square proves naturality of the connecting arrow. We have a natural distinguished triangle

\[
 \tau^{\le n}X\longrightarrow X\longrightarrow\tau^{\ge n+1}X
       \longrightarrow(\tau^{\le n}X)[1].
 \tag{4}
\]

This conclusion does not assert that cones of all maps in \(\mathcal D\) are functorial.

For (T1), the lower comparison at \(-1\) is \(z\mapsto(-2z,z)\) into the negative term, and the upper comparison is reduction modulo two on the degree-zero term. A chain map from a complex in degrees at most \(-1\) has top image in \(\ker(2,4)\), so its top component factors through that inclusion; the adjunction proves the corresponding statement for all derived maps. Choosing another generator, such as \((2,-1)\), changes its coordinates but not the comparison into \(C\): the unique isomorphism preserving that map changes sign. This is a concrete use of the uniqueness just proved. The nonzero boundary in (T2) likewise cannot be changed while fixing its triangle maps.

## Orthogonality recognizes the two halves

An object already in a half is unchanged by that half's truncation, because it represents its own restricted Hom functor. Triangle (4) then gives

\[
\begin{aligned}
 X\in\mathcal D^{\le n}&\ \Longleftrightarrow\ \tau^{\ge n+1}X=0,\\
 X\in\mathcal D^{\ge n}&\ \Longleftrightarrow\ \tau^{\le n-1}X=0,\\
 \mathcal D^{\le n}&={}^{\perp}\mathcal D^{\ge n+1},\qquad
 \mathcal D^{\ge n}=(\mathcal D^{\le n-1})^{\perp}.
\end{aligned}
\tag{5}
\]

Here a left or right orthogonal means vanishing of every Hom to or from objects in the other subcategory. To check the converse in the right-orthogonal identity, let \(U=\tau^{\le n-1}X\). The hypothesis kills \(\operatorname{Hom}(U,X)\); adjunction identifies this with \(\operatorname{Hom}(U,U)\), so its identity is zero and \(U=0\). The left-orthogonal converse uses \(V=\tau^{\ge n+1}X\) and \(\operatorname{Hom}(V,V)\simeq\operatorname{Hom}(X,V)\). The first two equivalences then finish both arguments.

Each half is extension closed. For example, if \(X'\to X\to X''\to X'[1]\) is distinguished and both outside objects lie in \(\mathcal D^{\ge n}\), the Hom sequence kills \(\operatorname{Hom}(W,X)\) for every \(W\in\mathcal D^{\le n-1}\). Formula (5) puts \(X\) in the same half. The other half follows by the dual Hom sequence. In particular the heart is extension closed. It contains zero and finite biproducts, using the split triangle \(A\to A\oplus B\to B\); it is an additive category.

## Cuts commute and finite intervals have a canonical object

The adjunctions give the shift and nested-cut formulas

\[
\begin{aligned}
 \tau^{\le n}(X[m])&\simeq(\tau^{\le n+m}X)[m],&
 \tau^{\ge n}(X[m])&\simeq(\tau^{\ge n+m}X)[m],\\
 \tau^{\le a}\tau^{\le b}&\simeq\tau^{\le\min(a,b)},&
 \tau^{\ge a}\tau^{\ge b}&\simeq\tau^{\ge\max(a,b)}.
\end{aligned}
\tag{6}
\]

For the first row, shift the representing Hom problem. For nested lower cuts with \(a\le b\), the composite \(\tau^{\le a}\tau^{\le b}X\) has the same Hom functor on \(\mathcal D^{\le a}\) as \(X\), so it is \(\tau^{\le a}X\). In the other order \(\tau^{\le b}\) fixes the object already in \(\mathcal D^{\le a}\). The upper-cut identities use the dual adjunction. Each comparison is the unique one preserving the units or counits, hence is natural.

The mixed cuts satisfy

\[
 \tau^{\ge b}\tau^{\le a}X
      \simeq\tau^{\le a}\tau^{\ge b}X
      =:\tau^{[b,a]}X,\qquad
 \tau^{[b,a]}X=0\quad(b>a).
 \tag{7}
\]

If \(b>a\), the first composite is zero by (5). The second is zero by the dual assertion.

If \(b\le a\), set \(P=\tau^{\le b-1}X\), \(Q=\tau^{\le a}X\),
\(R=\tau^{\ge b}X\), \(N=\tau^{\ge a+1}X\). Adjunction gives the map \(P\to Q\) compatible with their maps to \(X\). The octahedron for \(P\to Q\to X\) supplies one object \(M\) and triangles

\[
 P\longrightarrow Q\longrightarrow M\longrightarrow P[1],
 \qquad
 M\longrightarrow R\longrightarrow N\longrightarrow M[1].
 \tag{8}
\]

The first puts \(M\) in \(\mathcal D^{\le a}\), by extension closure applied to \(Q\to M\to P[1]\). The second puts \(M\) in \(\mathcal D^{\ge b}\), applied to \(N[-1]\to M\to R\). The triangles are consequently the truncation triangles of \(Q\) at \(b-1\) and of \(R\) at \(a\). Their adjunctions identify \(M\) with both sides of (7), compatibly with the maps \(Q\to M\to R\). This specifies the mixed comparison independently of choices and makes it natural.

On the same cone, both orders of the interval cut \([0,0]\) give \(\mathbb Z/2\), with the target quotient; both orders of \([-1,-1]\) give \(\mathbb Z[1]\), with the kernel inclusion. The interval comparison in (7) identifies these maps, rather than merely identifying abstract isomorphism classes.

## Cohomology and the boundedness needed for detection

Define heart-valued functors

\[
 H_t^j(X)=H_t^0(X[j]),\qquad
 H_t^0(X)=\tau^{[0,0]}X,\qquad
 H_t^j(X)\simeq(\tau^{[j,j]}X)[j]\in\mathcal A.
 \tag{9}
\]

These are additive because the adjunctions preserve the relevant finite Hom sums. The octahedron comparing successive lower cuts gives

\[
 \tau^{\le j-1}X\longrightarrow\tau^{\le j}X
      \longrightarrow H_t^j(X)[-j]\longrightarrow(\tau^{\le j-1}X)[1].
 \tag{10}
\]

Indeed its third object is \(\tau^{[j,j]}X\), by (8).

If \(X\in\mathcal D^{\ge a}\cap\mathcal D^{\le b}\), (10) is a finite filtration from zero at \(j=a-1\) to \(X\) at \(j=b\). Each successive quotient is \(H_t^j(X)[-j]\). It retains its connecting maps; the existence of these triangles supplies no splitting.

If \(X\) is bounded below for this t-structure, then

\[
 X\in\mathcal D^{\ge0}
   \quad\Longleftrightarrow\quad H_t^j(X)=0\quad(j<0).
 \tag{11}
\]

For the reverse implication take \(X\in\mathcal D^{\ge a}\). If \(a<0\), the triangle
\(H_t^a(X)[-a]\to\tau^{\ge a}X\to\tau^{\ge a+1}X\)
identifies \(X\) with the next upper cut because its first term is zero. Repeat finitely until the lower bound is zero. If \(a\ge0\) there is nothing to do. The forward implication follows from (7). Dually, for \(X\) bounded above,
\(X\in\mathcal D^{\le0}\) exactly when all \(H_t^j(X)\) with \(j>0\) vanish. In a finite interval, vanishing of every \(H_t^j\) makes every step of (10) an isomorphism from zero, so \(X=0\).

These bounds cannot be omitted from an arbitrary t-structure. A different sufficient hypothesis, nondegeneracy of the whole t-structure, will give detection even for unbounded objects below.

Check the bound at this point. For the degenerate t-structure \((\mathcal D,0)\), every lower cut is identity, every upper cut is zero, and all heart cohomology vanishes. A nonzero object belongs to no \(\mathcal D^{\ge a}\). Thus the finite induction proving (11) cannot even start. The complete degenerate example below tests exactly this absent hypothesis.

## Two cohomology objects of a cone give the kernel and cokernel

Let \(f:A\to B\) be a map in \(\mathcal A\), and choose a distinguished triangle \(A\to B\to C\to A[1]\). Extension closure puts \(C\) in \(\mathcal D^{\ge-1}\cap\mathcal D^{\le0}\). Thus

\[
 K=H_t^{-1}(C)=\tau^{\le0}(C[-1]),\qquad
 Q=H_t^0(C)=\tau^{\ge0}C
 \quad\text{belong to }\mathcal A.
 \tag{12}
\]

The canonical arrows are \(K\to C[-1]\to A\) and \(B\to C\to Q\).
For every \(W\in\mathcal A\), the Hom sequence gives
\(\operatorname{Hom}(W,C[-1])\simeq\ker(\operatorname{Hom}(W,A)\to\operatorname{Hom}(W,B))\),
because \(\operatorname{Hom}(W,B[-1])=0\).
Adjunction replaces its left side by \(\operatorname{Hom}(W,K)\). This is precisely the universal property of a kernel.

Dually, \(\operatorname{Hom}(C,W)\) is the kernel of
\(\operatorname{Hom}(B,W)\to\operatorname{Hom}(A,W)\), since
\(\operatorname{Hom}(A[1],W)=0\). Adjunction replaces it by
\(\operatorname{Hom}(Q,W)\). Hence \(Q\) is the cokernel. These universal properties remove any dependence on the chosen cone.

## The octahedron makes image and coimage identical

Complete the arrow \(B\to Q\) to a triangle \(I\to B\to Q\to I[1]\).
The triangle \(Q[-1]\to I\to B\) puts \(I\) in \(\mathcal D^{\ge0}\).
Apply the octahedron to \(B\to C\to Q\), using the truncation triangle
\(K[1]\to C\to Q\to K[2]\). It gives

\[
 K\longrightarrow A\longrightarrow I\longrightarrow K[1],
 \qquad
 I\longrightarrow B\longrightarrow Q\longrightarrow I[1],
 \quad
 f=(A\longrightarrow I\longrightarrow B).
 \tag{13}
\]

The first triangle puts \(I\) in \(\mathcal D^{\le0}\), since \(A\) and \(K[1]\) lie there. Consequently \(I\in\mathcal A\). Apply the just-proved kernel/cokernel calculation to the two triangles in (13): the cokernel of \(K\to A\) is \(I\), and the kernel of \(B\to Q\) is \(I\). The factorization is the one induced by \(f\), so its canonical map from coimage to image is this isomorphism.

An additive category with kernels and cokernels in which every coimage-to-image map is an isomorphism is abelian. We have proved all three properties. Thus **the heart is abelian**.

Moreover a short exact sequence \(0\to A\to B\to Q\to0\) in the heart comes from a distinguished triangle \(A\to B\to Q\to A[1]\). Complete \(A\to B\) to a cone. Formula (12) makes its negative cohomology zero and identifies its degree-zero object with the specified cokernel \(Q\). Since the cone lies in \([-1,0]\), its truncation triangle identifies it with \(Q\), compatibly with \(B\to Q\). The connecting arrow is unique by the earlier lemma, since \(\operatorname{Hom}(A[1],Q)=0\).

Conversely a triangle with all three terms in the heart is a short exact sequence. The Hom sequence into \(A,B,Q\) identifies \(A\) as the kernel of \(B\to Q\), and the dual sequence identifies \(Q\) as the cokernel of \(A\to B\); their preceding Hom terms vanish by (2).

For (T1), (12) recovers the actual kernel \(\mathbb Z(-2,1)\to\mathbb Z^2\) and quotient \(\mathbb Z\to\mathbb Z/2\). In (13), the common image is \(2\mathbb Z\subset\mathbb Z\), and the coimage comparison sends the class of \((a,b)\) to \(2a+4b\). It is onto \(2\mathbb Z\) and has precisely the identified kernel, so is an isomorphism. Shift this map into the heart with cutoff two: its two heart defects are the same modules placed in ordinary degree two, namely \(\mathbb Z[-2]\) and \((\mathbb Z/2)[-2]\). The cone itself has standard cohomology in degrees one and two. This tests the shifted-heart convention without altering the abstract proof.

## Every triangle gives an exact cohomology sequence

We now prove exactness rather than assuming it in the abelian-heart argument.
For a triangle \(X\to Y\to Z\to X[1]\), first suppose all three terms lie in \(\mathcal D^{\ge0}\). For \(W\in\mathcal A\), adjunction gives
\(\operatorname{Hom}(W,H_t^0X)=\operatorname{Hom}(W,X)\), and similarly for \(Y,Z\).
The term \(\operatorname{Hom}(W,Z[-1])\) vanishes. The resulting Hom sequence proves
\(0\to H_t^0X\to H_t^0Y\to H_t^0Z\) exact, by the kernel universal property in the now abelian heart.

Suppose only \(Z\in\mathcal D^{\ge0}\). For every \(W\in\mathcal D^{\le-1}\),
both \(\operatorname{Hom}(W,Z)\) and \(\operatorname{Hom}(W,Z[-1])\) vanish.
Thus \(\tau^{\le-1}X\to\tau^{\le-1}Y\) is an isomorphism by adjunction.
The octahedron cancelling this common lower cut gives a triangle
\(\tau^{\ge0}X\to\tau^{\ge0}Y\to Z\to\).
The preceding case applies, and (7) identifies its degree-zero terms with those of \(X,Y,Z\). Hence the same exact sequence starting with zero holds under this single hypothesis. By opposite-category duality, if \(X\in\mathcal D^{\le0}\), then
\(H_t^0X\to H_t^0Y\to H_t^0Z\to0\) is exact.

In the general case set \(U=\tau^{\le0}X\), \(V=\tau^{\ge1}X\).
The octahedron for \(U\to X\to Y\) gives

\[
 U\longrightarrow Y\longrightarrow W\longrightarrow U[1],
 \qquad
 V\longrightarrow W\longrightarrow Z\longrightarrow V[1].
 \tag{14}
\]

The first triangle, with \(U\le0\), makes
\(H_t^0X=H_t^0U\to H_t^0Y\to H_t^0W\to0\) exact.
Rotate the second to \(W\to Z\to V[1]\to\). Since \(V[1]\ge0\), the single-hypothesis case makes \(H_t^0W\to H_t^0Z\) a monomorphism. The composite \(Y\to W\to Z\) is the original triangle arrow. Therefore its kernel on degree-zero cohomology equals the kernel of \(H_t^0Y\to H_t^0W\), proving exactness at \(H_t^0Y\).

Apply this argument to every shift and rotation of the triangle. With the canonical connecting arrows from (4) and (9), it yields the full long exact sequence

\[
 \cdots\longrightarrow H_t^jX\longrightarrow H_t^jY
 \longrightarrow H_t^jZ\longrightarrow H_t^{j+1}X
 \longrightarrow H_t^{j+1}Y\longrightarrow\cdots.
 \tag{15}
\]

## Nondegenerate cohomology detects every object

The t-structure is **nondegenerate** when its two infinitely distant tails contain only zero:

\[
 \bigcap_{n\in\mathbb Z}\mathcal D^{\le n}=\{0\},\qquad
 \bigcap_{n\in\mathbb Z}\mathcal D^{\ge n}=\{0\}.
 \tag{17}
\]

**Theorem.** Under (17), an object is zero if and only if every \(H_t^j\) vanishes. For every integer \(m\),

\[
\begin{aligned}
 X\in\mathcal D^{\le m}&\quad\Longleftrightarrow\quad
       H_t^j(X)=0\quad(j>m),\\
 X\in\mathcal D^{\ge m}&\quad\Longleftrightarrow\quad
       H_t^j(X)=0\quad(j<m).
\end{aligned}
\tag{18}
\]

A morphism is an isomorphism if and only if all its cohomology morphisms are isomorphisms. No boundedness, completeness, or convergence of an infinite tower is assumed.

**Proof.** First suppose all cohomology of \(X\) vanishes. Fix an integer \(n\). The successive lower-cut triangles (10) identify \(\tau^{\le n}X\) with \(\tau^{\le r}X\) for every \(r<n\), by a finite sequence of isomorphisms for each such \(r\). Thus \(\tau^{\le n}X\) belongs to every lower half: for \(r\ge n\) use nesting, and for \(r<n\) use the isomorphism just obtained. The first intersection in (17) makes it zero. Triangle (4) now identifies \(X\) with \(\tau^{\ge n+1}X\). This holds for every \(n\), so the second intersection in (17) makes \(X=0\). The converse is immediate.

If \(H_t^j(X)=0\) for \(j>m\), let \(V=\tau^{\ge m+1}X\). The commuting-cut identities (6)–(7) show that \(H_t^j(V)=0\) for \(j\le m\) and that \(H_t^j(V)\simeq H_t^j(X)\) for \(j>m\). Thus all its cohomology vanishes, so \(V=0\). Formula (5) gives \(X\le m\). Conversely an object in that half has the stated vanishing by (7). The other equivalence follows in the same way with \(U=\tau^{\le m-1}X\).

Finally, for a morphism \(u:X\to Y\), choose a cone triangle. If all \(H_t^j(u)\) are isomorphisms, exactness of (15) makes every cohomology object of the cone zero. The first assertion makes the cone zero, so \(u\) is an isomorphism. A functor takes isomorphisms to isomorphisms, proving the converse. \(\square\)

The standard t-structure on \(D(\mathcal B)\) is nondegenerate: belonging to every lower half, or every upper half, forces ordinary complex cohomology to vanish in every degree. Such a complex is isomorphic to zero in the derived category by its definition through quasi-isomorphisms. Thus (18) applies to unbounded complexes as well. A bounded t-structure also satisfies (17): an object in every lower half has a lower bound and is therefore zero by orthogonality; the other tail is dual. The degenerate example below fails (17), so it remains a genuine limitation of cohomological detection.

## Exercises with complete solutions

### A shift changes the degree cut
*Difficulty: Introductory.*

Let \(A\ne0\) lie in the heart, and put \(X=A[-2]\). Compute its heart cohomology, \(\tau^{\le1}X\), \(\tau^{\ge2}X\), and \(\tau^{\le0}(X[2])\).

**Solution.** The sole cohomology is \(H_t^2X=A\). Formula (7) gives \(\tau^{\le1}X=0\) and \(\tau^{\ge2}X=X\). Since \(X[2]=A\), its lower zero cut is \(A\). Formula (6) gives the same result as \((\tau^{\le2}X)[2]\). The sign is \(n+m\) in the shifted cut.

### A smart cutoff keeps a kernel
*Difficulty: Intermediate.*

In \(D^b(\mathbb Z)\), let \(C\) be \(\mathbb Z^2\xrightarrow{(2,4)}\mathbb Z\) in degrees minus one and zero. Find its cohomology and its two cuts at \(-1\) and \(0\). Compare with deleting the degree-zero term.

**Solution.** The kernel is the free subgroup generated by \((-2,1)\), and the cokernel is \(\mathbb Z/2\). Thus \(H^{-1}C=\mathbb Z\), \(H^0C=\mathbb Z/2\),
\(\tau^{\le-1}C=\mathbb Z[1]\) and \(\tau^{\ge0}C=(\mathbb Z/2)[0]\).
The lower comparison includes the kernel subgroup into \(\mathbb Z^2\); the upper comparison is the quotient of the target. Deleting the degree-zero term instead produces \(\mathbb Z^2[1]\), with the wrong negative cohomology. A smart cutoff must change its boundary term.

### An epimorphism has a shifted kernel as its cone
*Difficulty: Intermediate.*

Take the quotient \(f:\mathbb Z\to\mathbb Z/6\) in the standard heart. Compute the heart kernel and cokernel from its cone, and determine whether that cone lies in the heart.

**Solution.** The cone is represented by \(\mathbb Z\to\mathbb Z/6\) in degrees minus one and zero. Its negative cohomology is \(6\mathbb Z\simeq\mathbb Z\); its degree-zero cohomology is zero. Formula (12) gives kernel \(6\mathbb Z\) with its actual inclusion and cokernel zero. Therefore \(f\) is epic and not monic. The cone is \(6\mathbb Z[1]\), so it is outside the nonzero standard heart. An abelian heart does not require cones of its maps to stay in that heart.

### A nonzero connecting map remembers a nonsplit extension
*Difficulty: Advanced.*

Find the connecting class of \(0\to\mathbb Z\xrightarrow{6}\mathbb Z\to\mathbb Z/6\to0\) in \(D^b(\mathbb Z)\). Explain why the triangle does not split.

**Solution.** Represent \(\mathbb Z/6\) by the free complex
\(\mathbb Z\xrightarrow{6}\mathbb Z\) in degrees minus one and zero. A chain map from it to \(\mathbb Z[1]\) is multiplication by an integer on the negative-degree term. Chain homotopies identify two such integers exactly when their difference is divisible by six. The boundary map of the cone triangle is the identity on that term, so its class is \(1\in\mathbb Z/6\), which is nonzero. The free complex is a bounded projective resolution, so this calculation computes the derived maps. A split triangle has zero boundary. Equivalently a splitting would lift \(1\in\mathbb Z/6\) to a six-torsion element of \(\mathbb Z\), which cannot occur. The connecting arrow retains information lost by listing the three terms.

### Mono and epi tests use different cone degrees
*Difficulty: Intermediate.*

For an arbitrary heart map \(f:A\to B\), show that it is monic exactly when \(H_t^{-1}(\operatorname{Cone}f)=0\), and epic exactly when \(H_t^0(\operatorname{Cone}f)=0\). What if both vanish?

**Solution.** Formula (12) identifies those objects with the kernel and cokernel. In an abelian category a map is monic exactly when its kernel is zero, and epic exactly when its cokernel is zero: this follows from their universal properties and the image/coimage factorization. If both vanish, the cone lies in \([-1,0]\) with no cohomology; its one truncation triangle makes it zero. The original triangle therefore makes \(f\) an isomorphism. This also follows from (13), whose two outer defects are zero.

### A finite filtration and its interval cut
*Difficulty: Intermediate.*

In \(D^b(k)\) for a field, take \(X=k[1]\oplus k[-2]\). Compute its nonzero cohomology, \(\tau^{\le0}X\), \(\tau^{\ge1}X\), and both mixed cuts for the interval \([-1,0]\). State what the general filtration would retain for a nonsplit object.

**Solution.** We have \(H^{-1}X=k\), \(H^2X=k\), and no other cohomology. The lower zero cut is \(k[1]\), and the upper one cut is \(k[-2]\). Both
\(\tau^{\ge-1}\tau^{\le0}X\) and
\(\tau^{\le0}\tau^{\ge-1}X\) are \(k[1]\), as (7) predicts.
The finite filtration has its two nonzero quotients in degrees \(-1\) and \(2\); the intervening zero quotients give isomorphisms. This particular direct sum splits. For a general object, (10) retains the actual boundary maps between successive stages; its cohomology objects alone do not specify or split those extensions.

### An invisible object in a degenerate t-structure
*Difficulty: Advanced.*

On a nonzero triangulated category, check the t-structure
\((\mathcal D^{\le0},\mathcal D^{\ge0})=(\mathcal D,0)\).
What are its heart, truncations and cohomology? Identify the absent bound that prevents (11) from forcing every object to be zero.

**Solution.** Nesting and orthogonality hold, and the required triangle is \(X\xrightarrow{1}X\to0\to X[1]\). Every lower cut is the identity and every upper cut is zero. The heart and all heart cohomology are zero. Nevertheless nonzero objects remain in \(\mathcal D\). Such an object belongs to no \(\mathcal D^{\ge a}\), since every upper half is zero. It is not bounded below. Formula (11) explicitly requires that bound, while finite-interval detection requires both bounds. The opposite degenerate t-structure exchanges this missing condition with boundedness above.

### Kernels in a shifted heart
*Difficulty: Intermediate.*

Shift the standard t-structure on \(D^b(\mathbb Z)\) to the cut \(s=2\). For multiplication by six on \(\mathbb Z[-2]\), compute the kernel and cokernel in the new heart and compare with standard cohomological degrees.

**Solution.** The shifted heart consists of abelian groups placed in degree two, namely \(\mathcal A[-2]\). Shifting the cone calculation for multiplication by six gives a cone with standard \(H^1=0\), \(H^2=\mathbb Z/6\), and no other cohomology. In the shifted structure,
\(H_{t_s}^j(X)=H_t^{j+2}(X)[-2]\), by (6) and (9).
Thus its negative heart cohomology is zero and its degree-zero heart cohomology is \((\mathbb Z/6)[-2]\). Formula (12) gives kernel zero and that cokernel. The object remains in degree two as an object of the original derived category; the heart's zero label is relative to its shifted cut.

## Optional constructible duality application

Let \(A\) now be Noetherian, commutative, of finite global dimension, and let \(X\) be a finite-dimensional real analytic manifold with the standing bounded constructible conventions. Standard truncation preserves \(D^b_{\mathbb R\text{-c}}(A_X)\). In a common local stratification, kernels and cokernels of maps of finite locally constant modules are locally constant and finitely generated; Noetherianity retains finiteness. Finite global dimension makes the bounded finite coefficient cohomology perfect. Truncation preserves the global degree bounds. Thus restriction of the standard t-structure is valid.

The written constructible duality equivalence \(D_X\), with \(D_X(F[1])=(D_XF)[-1]\) and its actual biduality map, transports the opposite t-structure back to this same category. It gives

\[
 {}^d\mathcal D^{\le0}=D_X(\mathcal D^{\ge0}),\qquad
 {}^d\mathcal D^{\ge0}=D_X(\mathcal D^{\le0}).
 \tag{16}
\]

Reversal of triangles, Hom directions and shifts verifies every axiom by (2). Its heart is \(D_X\) of the ordinary constructible heart, with arrows reversed. This proves the claimed t-structure using the exact existing duality theorem; it does not identify it with a middle perverse t-structure.

## References

A. A. Beilinson, J. Bernstein and P. Deligne, [*Faisceaux pervers*](https://publications.ias.edu/sites/default/files/Faisceaux%20pervers.pdf), Astérisque 100 (1982), develops t-structures, their abelian hearts, truncation and cohomology functors, and nondegenerate detection. The arguments and examples above give the proofs needed here in the stated conventions. The optional constructible application uses the internal Verdier-duality theorem linked in its prerequisite paragraph; that geometric theorem is separate from the abstract heart construction.
