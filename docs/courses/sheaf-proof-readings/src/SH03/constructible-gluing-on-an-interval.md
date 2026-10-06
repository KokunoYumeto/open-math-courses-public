# Constructible gluing on an interval

A constructible sheaf can change at a small set of points while remaining locally constant elsewhere. The change is not described by a list of stalks alone. We must also know how a section near a singular point restricts to each neighboring region. On an interval with one distinguished point, this produces a diagram of three modules. We will construct the sheaf from that diagram, calculate its cohomology and costalk, and extend the calculation to bounded complexes.

We assume the definition of a sheaf, exactness detected at stalks, the localization triangle for an open subset and its closed complement, and derived adjunction for extension by zero. We also use the elementary sheaf-cohomology calculation for a constant sheaf on a contractible interval. A prerequisite is [Sheaves of modules and their derived categories](https://kokunoyumeto.github.io/open-math-courses-public/courses/derived-categories-and-sheaf-operations/sheaves-of-modules-and-their-derived-categories.html); extension-by-zero adjunction is also required. The source account below identifies the classical operations and the exact scope of their use.

*Written by GPT-6.1 Sol (OpenAI), Ultra, September 2026. Author self-check recorded; not independently reviewed. New original text is public domain (CC0).*

The licensed pointwise universal-object proof supplies the abelian diagram category. Below we construct its interval sheaves and compare ambient derived cohomology; these are additional sheaf-theoretic obligations, not consequences of evaluation alone.

## Restriction data at one point

Let \(I=(-1,1)\), \(I_-=(-1,0)\), and \(I_+=(0,1)\). A sheaf of \(k\)-modules is weakly constructible for this decomposition if its restrictions to \(I_-\) and \(I_+\) are locally constant. They are constant because each interval is simply connected. This statement uses no finiteness condition on the modules and no global-dimension condition on the ring \(k\).

Choose trivializations of the two restrictions. Denote their values by \(L\) and \(R\), and put \(V=F_0\). A germ at zero has a representative on a sufficiently small interval. Its restrictions to the two half intervals give homomorphisms

\[
L\xleftarrow{r_-}V\xrightarrow{r_+}R.
\tag{1}
\]

The arrows point away from the singular point. This is the direction in which a germ at zero determines nearby values. They need not be injective or surjective.

**Theorem 1.** Weakly constructible sheaves on \(I\) are equivalent to diagrams (1). Morphisms are triples of module homomorphisms commuting with both arrows. Kernels, cokernels and exact sequences are calculated at the three modules.

**Proof.** We first construct a sheaf \(E\) from a diagram. On an open subset \(U\subset I\), a section consists of a locally constant \(L\)-valued function on \(U\cap I_-\), a locally constant \(R\)-valued function on \(U\cap I_+\), and, if \(0\in U\), an element \(v\in V\). Near zero the two functions must have the constant values \(r_-(v)\) and \(r_+(v)\). There is no condition on connected components of \(U\) away from zero.

Restriction forgets parts of the two functions and, when necessary, the value at zero. Compatible local functions glue uniquely. If an open covering contains zero, at least one member contains a neighborhood of it; the values \(v\) agree on overlaps containing zero. The near-zero condition therefore glues too. This proves the sheaf axiom.

At a point of \(I_-\) or \(I_+\), the stalk is \(L\) or \(R\). At zero, a section on a sufficiently small connected interval is uniquely determined by \(v\), because each half interval is connected and its value is prescribed. Thus \(E_0=V\), and its two restriction maps are the chosen arrows.

Conversely, construct (1) from a sheaf \(F\). Independence of the representative of a germ follows by shrinking its neighborhood; a locally constant function on the connected half interval has one value. A section of \(F\) determines the two locally constant functions and its germ at zero. This gives a natural sheaf morphism from \(F\) to the constructed \(E\). It is an isomorphism on each of the three types of stalk, hence an isomorphism of sheaves. The two constructions also identify morphisms. Finally, sheaf exactness is stalkwise, so exactness is componentwise in (1). \(\square\)

For example, \(L=R=k\) and \(V=0\) gives a sheaf with nonzero values on both sides but no germ at zero. Taking \(V=k\) and both arrows the identity gives the constant sheaf on all of \(I\). These sheaves have the same values away from zero and different gluing.

## Cohomology of the whole interval

For a diagram (1), every section on \(I\) is determined by its value in \(V\), so \(\Gamma(I;F)=V\). The corresponding derived assertion needs a proof in the category of all sheaves, rather than only exactness within the diagram category.

Let \(j_\pm:I_\pm\hookrightarrow I\) and \(i:\{0\}\hookrightarrow I\). The exact sequence separating the closed point from the two open pieces is

\[
0\longrightarrow j_{-!}L_{I_-}\oplus j_{+!}R_{I_+}
\longrightarrow F\longrightarrow i_*V\longrightarrow0.
\tag{2}
\]

Exactness follows from stalks: the first map is the identity away from zero and has zero stalk at zero; the last map is the identity at zero and zero elsewhere.

**Proposition 2.** For every module diagram (1),

\[
R\Gamma(I;F)\simeq V
\tag{3}
\]

with \(V\) in degree zero.

**Proof.** The constant sheaf with value \(L\) on the closed half interval \((-1,0]\), pushed into \(I\), fits into

\[
0\longrightarrow j_{-!}L_{I_-}
\longrightarrow L_{(-1,0]}
\longrightarrow i_*L\longrightarrow0.
\tag{4}
\]

The closed half interval is contractible, and its constant-sheaf cohomology is \(L\) in degree zero. The point has the same cohomology. The map on degree-zero cohomology in (4) is the identity of \(L\). The long exact cohomology sequence gives
\(R\Gamma(I;j_{-!}L_{I_-})=0\).
The right half interval gives the same statement for \(j_{+!}R_{I_+}\). Apply derived global sections to (2). Both open-piece terms vanish, and \(R\Gamma(I;i_*V)=V\), proving (3). \(\square\)

The constant-sheaf interval calculation used here holds for arbitrary coefficient modules. The programme proof is compact-interval acyclicity and its constant-module argument, followed by homotopy invariance through a proper interval. Each open, closed or half-open interval used here contracts inside itself to a point. Evaluation at that point and the constant-section map have one composite equal to the identity by definition; homotopy invariance identifies the other composite with the identity induced by the interval contraction. This gives the ordinary cohomology identification, naturally in the module. Finite truncation triangles give the same assertion for a bounded coefficient complex. No compact-support cohomology of an open half interval has been substituted for ordinary cohomology on \(I\).

## Bounded complexes of diagrams

We now assume that \(k\) is a commutative ring of finite global dimension \(g\). Let \(\mathcal A\) be the abelian category of diagrams (1). Let \(D^b_{\mathcal S}(k_I)\) denote bounded complexes of sheaves whose cohomology sheaves are weakly constructible for the three pieces.

**Theorem 3.** The exact sheaf construction in Theorem 1 induces an equivalence

\[
D^b(\mathcal A)\xrightarrow{\sim}D^b_{\mathcal S}(k_I).
\tag{5}
\]

Under this equivalence a bounded complex can be represented by three complexes and two cochain maps

\[
L^\bullet\xleftarrow{r_-}V^\bullet\xrightarrow{r_+}R^\bullet.
\tag{6}
\]

**Proof.** We give the homological-algebra argument because passing from sheaves to complexes must preserve extension data.

For a module \(M\), form the following diagrams:

\[
\begin{aligned}
P_0(M)&=(M\xleftarrow{\mathrm{id}}M\xrightarrow{\mathrm{id}}M),\\
P_-(M)&=(M\leftarrow0\to0),\\
P_+(M)&=(0\leftarrow0\to M).
\end{aligned}
\]

Here the notation always lists left value, middle value, right value. A map from \(P_0(M)\) to (1) is determined by a map \(M\to V\); maps from \(P_-(M)\) and \(P_+(M)\) are determined by maps to \(L\) and \(R\). Consequently these diagrams are projective when \(M\) is projective, and \(\mathcal A\) has enough projectives.

For \(E=(L\leftarrow V\to R)\) there is a functorial exact sequence

\[
0\to P_-(V)\oplus P_+(V)
\to P_0(V)\oplus P_-(L)\oplus P_+(R)
\to E\to0.
\tag{7}
\]

The last map is the identity at the middle module. On the left and right it sends \((v,l)\) to \(r_-(v)+l\), and \((v,r)\) to \(r_+(v)+r\). The first map on the left sends \(v\) to \((v,-r_-(v))\), and on the right sends \(v\) to \((v,-r_+(v))\). These formulas prove exactness at every module.

Each of \(V,L,R\) has a projective resolution of length at most \(g\). The functors \(P_0,P_-,P_+\) are exact and carry projective modules to projective diagrams. Resolving the terms of (7), and taking the mapping cone of a lifted resolution map, gives a projective diagram resolution of \(E\) of length at most \(g+1\).

Next, these projective diagrams have no higher sheaf Ext into a weakly constructible sheaf \(G\). The sheaf associated to \(P_0(M)\) is the constant sheaf \(M_I\). Derived adjunction identifies its derived Hom into \(G\) with

\[
R\operatorname{Hom}_k(M,R\Gamma(I;G)).
\]

By Proposition 2, the second argument is \(G_0\) in degree zero. If \(M\) is projective, this has no higher cohomology. The sheaves associated to \(P_-(M)\) and \(P_+(M)\) are \(j_{-!}M_{I_-}\) and \(j_{+!}M_{I_+}\). Extension-by-zero adjunction gives instead
\(R\operatorname{Hom}_k(M,R\Gamma(I_\pm;G|_{I_\pm}))\).
The restriction is constant on a contractible interval, so these complexes too have no higher cohomology for projective \(M\).

A finite projective diagram resolution can therefore calculate both diagram Ext and sheaf Ext into \(G\). In degree zero the Hom groups agree by Theorem 1; the resolution maps agree as well. Dimension shifting yields equality of Ext groups in every degree. The induced functor on bounded derived categories is fully faithful: apply these Ext comparisons successively to the truncation triangles of the two bounded complexes.

For essential surjectivity, take a bounded sheaf complex with constructible cohomology. If it has one nonzero cohomology sheaf, it is a shift of a sheaf in Theorem 1. Induct on the number of possibly nonzero cohomology degrees. A truncation triangle expresses the complex as an extension of its lower truncation by its highest cohomology sheaf with a shift. By the induction hypothesis these two objects come from \(D^b(\mathcal A)\); by full faithfulness the connecting morphism comes from that category too. Its cone produces a preimage of the original complex. This proves (5). Finally, a bounded complex in the diagram category is exactly the data (6). \(\square\)

This proof concerns the one-point interval decomposition. It does not assert the corresponding theorem for an arbitrary stratification or triangulation.

For a cochain map \(u:A^\bullet\to B^\bullet\), our cone has
\(\operatorname{Cone}(u)^n=B^n\oplus A^{n+1}\) and differential
\(d(b,a)=(d_Bb+u(a),-d_Aa)\). We use the connecting-arrow convention of **Sheaves of modules and their derived categories**. The fibre objects calculated below are cones shifted by \([-1]\); their cohomology degrees are independent of negating a triangle's connecting arrow.

## Stalks and costalks

For the complex (6), the stalk at zero is \(V^\bullet\). The costalk \(Ri^!F\) measures cohomology supported at zero. It is sensitive to the restriction maps.

Put \(j:I\setminus\{0\}\hookrightarrow I\). The localization triangle is

\[
i_*Ri^!F\longrightarrow F\longrightarrow Rj_*j^{-1}F\longrightarrow i_*Ri^!F[1].
\tag{8}
\]

At zero the third term is the cohomology of two small punctured half intervals. Each is contractible, and the restrictions in (6) are constant complexes there. Hence its stalk is \(L^\bullet\oplus R^\bullet\), and the middle map in (8) is \((r_-,r_+)\).

**Proposition 4.** There is a natural isomorphism

\[
Ri^!F\simeq
\operatorname{Cone}\bigl(V^\bullet\xrightarrow{(r_-,r_+)}L^\bullet\oplus R^\bullet\bigr)[-1].
\tag{9}
\]

For a sheaf in degree zero this gives

\[
\begin{aligned}
H^0(Ri^!F)&=\ker(V\to L\oplus R),\\
H^1(Ri^!F)&=\operatorname{coker}(V\to L\oplus R),
\end{aligned}
\tag{10}
\]

and all other cohomology groups vanish.

**Proof.** Taking a stalk is exact and takes (8) to a distinguished triangle
\(Ri^!F\to V^\bullet\to L^\bullet\oplus R^\bullet\to Ri^!F[1]\).
The fibre of the middle map is its cone shifted by \(-1\), giving (9). For degree-zero modules, the long exact sequence gives (10). \(\square\)

In particular, the constant sheaf has diagonal restriction \(k\to k\oplus k\). Its costalk has \(k\) in degree one, or \(k[-1]\). This agrees with the one-dimensional local orientation calculation after choosing an orientation of the interval. The skyscraper \(i_*k\) has zero neighboring modules and costalk \(k\) in degree zero. A stalk and a costalk can therefore occupy different degrees.

## Perfect values and finite coefficients

A complex of \(k\)-modules is perfect if it is quasi-isomorphic to a bounded complex of finitely generated projective modules. In this lesson a bounded weakly constructible complex is constructible if each stalk is perfect. For (6), this means precisely that \(V^\bullet,L^\bullet,R^\bullet\) are perfect.

This definition is valid without assuming that \(k\) is Noetherian. Perfect complexes are closed under finite direct sums, shifts and cones. To see the cone statement, represent two perfect complexes by bounded complexes of finitely generated projectives. A derived morphism between them is represented by a cochain map because its source is a bounded projective complex. Its ordinary mapping cone is another bounded complex of finitely generated projectives. Formula (9) therefore shows that a constructible complex in this model also has perfect costalk at zero.

If \(k\) is Noetherian as well as of finite global dimension, a bounded complex is perfect exactly when its cohomology modules are finitely generated. One direction follows because kernels and cokernels of maps between finitely generated modules are finitely generated. For the other, resolve a finitely generated cohomology module by finite free modules; Noetherianity keeps the successive kernels finitely generated, and finite global dimension makes a sufficiently high kernel projective. This gives a finite resolution by finitely generated projectives. Use the finitely many truncation triangles and closure under cones for a bounded complex.

Over a field, perfect simply means bounded with finite-dimensional cohomology. The diagram with \(V=\bigoplus_{n\geq0}k\), \(L=R=0\) is weakly constructible but not constructible: its stalk at zero is infinite dimensional. The geometry of the decomposition alone supplies no finiteness of coefficients.

## One diagram from sections to a closed-layer correction

Use this example throughout the diagram-to-heart route. Over \(\mathbb Z\), take

\[
 L=\mathbb Z,\qquad V=\mathbb Z^2,\qquad R=\mathbb Z,\qquad
 r_-(a,b)=2a+4b,\qquad r_+(a,b)=a+2b.
 \tag{B1}
\]

Write \(q(a,b)=a+2b\), \(u=(-2,1)\), and let \(E\) be its sheaf. All three modules are finite free, but neither their ranks nor their perfection determines its local tests. The combined attachment is \(\rho=(2q,q):V\to L\oplus R\).

Proposition 2 gives \(R\Gamma(I;E)=\mathbb Z^2\) in degree zero. Under this identification the maps restricting a global section to either half interval are exactly \(2q\) and \(q\). At zero, ordinary restriction also gives \(V\). The costalk, by Proposition 4, has the model

\[
 K=[\,\mathbb Z^2\xrightarrow{\ (2q,q)\ }\mathbb Z^2\,]
       \quad\text{in degrees }0,1.
 \tag{B2}
\]

Here and in the two directional models we identify the shifted cone with the displayed positive differential by negating its degree-one target. We make the same change for all three cones, so their projection maps commute. Its degree-zero cohomology is \(\mathbb Zu\). The functional
\(\ell(x,y)=x-2y\) induces an isomorphism
\(\operatorname{coker}\rho\to\mathbb Z\): it kills \((2,1)\), is onto, and its kernel is precisely \(\mathbb Z(2,1)\). Thus \(H^1K=\mathbb Z\).

The directional tests are

\[
 J_+=[\,V\xrightarrow{\,2q\,}\mathbb Z\,],\qquad
 J_-=[\,V\xrightarrow{\,q\,}\mathbb Z\,].
 \tag{B3}
\]

Both have \(H^0=\mathbb Zu\); their \(H^1\) are respectively \(\mathbb Z/2\) and zero. In particular both nonzero covector directions occur, even though the right attachment is onto. Absence requires a quasi-isomorphism, so its nonzero kernel matters too.

These models give more than three independent cohomology calculations. Projection to the left coordinate induces \(K\to J_+\), with identity in degree zero and \((x,y)\mapsto x\) in degree one. On \(H^0\) it is the identity of \(\mathbb Zu\). On \(H^1\) it is reduction modulo two, because \(x\equiv\ell(x,y)\pmod2\). Its kernel complex is \(R[-1]\), included by \(y\mapsto(0,y)\). Consequently the cohomology sequence contains the actual maps

\[
 \mathbb Z=R\xrightarrow{\ -2\ }\mathbb Z=H^1K
        \xrightarrow{\ \bmod2\ }\mathbb Z/2=H^1J_+\longrightarrow0.
 \tag{B4}
\]

The sign comes from \(\ell(0,y)=-2y\). Projection to the right coordinate gives \(K\to J_-\), again the identity on \(H^0\), and zero on \(H^1\). Keeping the attachment maps accounts for both the torsion and this comparison.

The ordinary smart lower cut of (B2) at zero is the subgroup \(\mathbb Zu\) in degree zero, with its inclusion into \(V\). Its upper cut starts with \(\operatorname{coker}\rho=\mathbb Z\) in degree one. Deleting the target would leave all of \(V\), rather than its kernel.

## The interval dictionary in the perverse construction

After learning the abstract heart and the perverse stratum criterion, return to the same diagram. For the real perversity \(p(s)=-s\), the open-layer cutoff is \(-1\). Since \(E\) is in ordinary degree zero there, its lower open cut is zero. The full closed-layer calculation therefore takes \(G=E\), \(C=\tau^{\le0}i^!G=\mathbb Zu\), and uses the exceptional counit
\(i_*\mathbb Zu\to E\), whose point map is \(z\mapsto(-2z,z)\).
Its ordinary quotient is the sheaf \(B\) with diagram
\(\mathbb Z\xleftarrow{\,2\,}\mathbb Z\xrightarrow{\,1\,}\mathbb Z\).
The quotient at zero is \(q\), and it is the identity on both open pieces. Its point costalk has no degree-zero cohomology and has \(\mathbb Z\) in degree one. Thus the triangle is \(i_*\mathbb Zu\to E\to B\), with the exact stratum bounds required of the two perverse cuts. The general theorem retains arbitrary coefficients and geometry; this single diagram supplies its map-level example.

## Evaluation does not supply a natural splitting

The separately licensed pointwise abelian and natural-splitting treatment explains the distinction between evaluating a diagram and splitting it naturally. Its human source is Tom Leinster, *Basic Category Theory*, arXiv version 2, 26 August 2025; that component and its AI additions retain CC BY-NC-SA 4.0. This lesson applies its universal objects to the interval; it does not reproduce that adapted exposition or change its licence.

For a direct interval example, the usual sheaf sequence
\[
 0\longrightarrow j_!\mathbb Z_{I\setminus\{0\}}
   \longrightarrow\mathbb Z_I\longrightarrow i_*\mathbb Z
   \longrightarrow0
 \tag{B5}
\]
is split after evaluating at every stratum. At zero its quotient is the identity of \(\mathbb Z\); on an open half the quotient is zero. A section as a diagram would have to be the identity at zero and zero on both halves. Naturality along either attachment would say \(1=0\), because the middle constant sheaf has identity attachments. No such section exists. Stalkwise exactness and stalkwise splitness have different conclusions.

The [hidden-differential exercise](#a-hidden-differential) is a second check: the complex \([k\xrightarrow{1}k]\) is zero in the derived category even though its two terms are nonzero. Neither a termwise dimension list nor a family of unrelated splittings removes the need to retain all maps.

## Exercises with solutions

### Three boundary conditions

*Difficulty: Introductory.*

Let \(k\neq0\). Give the diagrams and costalks for the constant sheaf \(k_I\), the extension by zero \(j_{+!}k_{I_+}\), and the ordinary direct image \(j_{+*}k_{I_+}\).

**Solution.** The constant sheaf has \(V=L=R=k\) and both arrows the identity. Its costalk is the fibre of the diagonal map, hence \(k[-1]\). Extension by zero has \(V=L=0\) and \(R=k\); its costalk is \(k[-1]\) by (9), even though its stalk at zero vanishes. Ordinary direct image has \(L=0\), \(V=R=k\), and \(r_+=\mathrm{id}\); its costalk is zero. On a small interval, sections of the latter sheaf are determined by the constant value on its positive half, which explains its nonzero stalk at zero. The higher direct-image stalks vanish because the punctured positive half interval is contractible.

### Torsion from gluing

*Difficulty: Intermediate.*

Take \(k=\mathbb Z\), \(V=L=R=\mathbb Z\), and maps \(r_-(v)=2v\), \(r_+(v)=6v\). Calculate the stalk, global cohomology and costalk of the resulting sheaf.

**Solution.** The stalk at zero and the global cohomology are \(\mathbb Z\) in degree zero, by construction and Proposition 2. The map to the two neighboring values is \(v\mapsto(2v,6v)\), which is injective. Its cokernel is \(\mathbb Z\oplus\mathbb Z/2\): replace the second coordinate by the second minus three times the first, so the map becomes \(v\mapsto(2v,0)\). Thus \(H^0(Ri^!F)=0\) and \(H^1(Ri^!F)=\mathbb Z\oplus\mathbb Z/2\). Every stalk module is finite free, while the costalk detects torsion created by the restriction maps.

### A hidden differential

*Difficulty: Intermediate.*

Work over a field. Let \(L^\bullet=R^\bullet=0\), and let \(V^\bullet=[k\xrightarrow{\mathrm{id}}k]\) in degrees zero and one. Compare this complex with the skyscraper complex having \(V=k\) in degree zero.

**Solution.** The first \(V^\bullet\) is acyclic, so all stalks of its associated sheaf complex are acyclic. That sheaf complex is zero in the derived category, as is its costalk. The second has nonzero degree-zero stalk and costalk. The list of term dimensions is not a substitute for cohomology or for the differentials in a derived diagram.

### Euler characteristic at the singular point

*Difficulty: Intermediate.*

Let \(k\) be a field and assume the three complexes in (6) are perfect. Define \(\chi(C)=\sum_j(-1)^j\dim_kH^j(C)\). Prove

\[
\chi(Ri^!F)=\chi(V^\bullet)-\chi(L^\bullet)-\chi(R^\bullet).
\]

Evaluate it for the constant sheaf and the skyscraper.

**Solution.** A distinguished triangle of bounded finite-dimensional complexes has additive Euler characteristic, by its finite long exact cohomology sequence. Apply this to the stalk triangle of (8). It gives the stated difference. For the constant sheaf the result is \(1-1-1=-1\), agreeing with \(k[-1]\). For the skyscraper it is \(1-0-0=1\), agreeing with a degree-zero costalk. This identity describes the costalk in this decomposition; it has not defined a characteristic-cycle sign convention.

## References

**Classical sheaf operations.** Pierre Schapira, [*An Introduction to Sheaves on Grothendieck Topologies*, 1 August 2026](https://webusers.imj-prg.fr/~pierre.schapira/LectNotes/SHV.pdf), §3.2, pp. 66–68, gives open extension, closed restriction and their exact sequences, then derives the supported-cohomology triangles by internal Hom. The exact sequences in (2), (4) and (8) are instances of these classical constructions; they are checked here on stalks and used with the displayed attachment maps. The nonsplitting of the constant-sheaf quotient in (B5) is the familiar phenomenon in Exercise 3.3 of those notes. Its pointwise splitting does not give a natural section. The separate Leinster-based diagram component retains the CC BY-NC-SA 4.0 terms stated above.

**Intervals and coefficient scope.** Schapira's Lemmas 3.5.1–2 and Proposition 3.5.3, pp. 72–73, prove interval cohomology bounds and constancy by continuation along overlapping intervals. Theorem 3.6.3 and Corollary 3.6.7, pp. 74–76, obtain constant-coefficient acyclicity by homotopy. Those notes have a standing finite-global-dimension convention. Our sheaf classification and ordinary interval calculation allow arbitrary coefficient modules over the stated ring: the classification is constructed directly, while the arbitrary-module cohomology calculation is bound above to the programme's compact-interval and homotopy proofs. Finite global dimension is imposed only when the lesson passes to finite projective diagram resolutions and bounded derived realization. Finite generation is a different condition and enters only in the perfect-stalk discussion.

**Derived algebra and the local realization proof.** The Stacks Project, [*Cohomology of Sheaves*, Internal hom in the derived category, Tag 08DJ](https://stacks.math.columbia.edu/tag/08DJ), constructs internal Hom with a K-injective target, proves its tensor adjunction, and identifies derived Hom by sections. The checked native source is revision `a04446e5`. This is background for the derived Hom formalism, not a theorem identifying every constructible derived category with a diagram category. Theorem 3 supplies the interval-specific argument: the two-arrow resolution (7), higher-Ext vanishing for its projective terms, dimension shifting, and lifting the truncation extension by full faithfulness. Each step is needed; componentwise exactness alone does not prove (5).

**Teaching route and remaining prerequisites.** This lesson follows one attachment diagram from sections through the costalk and directional tests to an explicit closed-layer correction. Its integral example keeps the quotient coordinate, torsion and actual comparison signs; the exercises test these maps and the hidden differential. These are independently written calculations using classical sheaf operations. The complete construction of derived categories, their adjunctions and the separately linked perverse truncation theorem remain programme prerequisites with their own proof obligations. The source comparisons here do not certify all of those foundations or the course as a whole.
