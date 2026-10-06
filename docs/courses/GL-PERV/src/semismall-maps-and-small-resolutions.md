# Semismall maps and small resolutions

*Reconstructed by GPT-6 Astra (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the AI that wrote it. Public domain (CC0).*

An exceptional curve in a surface and an exceptional curve in a threefold behave differently under direct image. In the surface it can supply a perverse summand at a point. In the threefold it can belong to the stalk of the intersection complex itself. We begin with explicit resolutions exhibiting this difference, derive the dimension test that explains it, and then identify the map that decides whether the additional summand splits. The two-point Hilbert scheme gives a family version of the surface calculation.

Use the normalization
\[
\operatorname{IC}_X(L)=j_{!*}L[\dim X],\qquad
IH^a(X,L)=H^{a-\dim X}(X,\operatorname{IC}_X(L)).
\]
Closed-support ICs are understood to be pushed into the ambient variety. Our default coefficients \(\Lambda\) are a characteristic-zero field in the classical topology, or \(\overline{\mathbb Q}_\ell\) in the étale topology with \(\ell\) invertible on the variety. Arithmetic formulas keep Tate twists; decompositions obtained from finite-field weights are asserted geometrically. Section 4 separately allows any coefficient field \(k\) on complex varieties. Characteristic two for \(k\) there does not mean that the variety has characteristic two.

The earlier inputs are proper base change, localization and oriented duality from Constructible complexes on algebraic varieties, the strict boundary characterization in [Intermediate extensions and intersection complexes](intermediate-extensions-and-intersection-complexes.md), and, for general characteristic-zero splitting, [The decomposition theorem](the-decomposition-theorem.md). We will distinguish the arguments needing that last theorem from the ones proved by dimensions and adjunction alone.

## 1. Two exceptional curves and one small resolution

For the blow-up of the plane, write the source as an incidence variety:
\[
B=\{((x,y),[u:v]):xv=yu\}\subset\mathbb A^2\times\mathbb P^1.
\tag{1.1}
\]
Projection \(b:B\to\mathbb A^2\) is projective because incidence is closed. In the chart \(u\ne0\), put \(a=v/u\); then \(y=ax\), so \((a,x)\) are smooth coordinates. In the other chart put \(b'=u/v\); the coordinates are \((b',y)\). On the overlap, \(b'=a^{-1}\) and \(y=ax\). These are precisely the transition maps of the tautological line over \(\mathbb P^1\). Thus \(B=\operatorname{Tot}\mathcal O(-1)\). Away from zero the direction is forced to be \([x:y]\). Over zero it is arbitrary, giving the zero section \(E=\mathbb P^1\).

The surface singularity
\[
X_1=\{(x,z,y):xy=z^2\}
\]
has the resolution
\[
\pi_1:Y_1=\{((x,z,y),[u:v]):xv=zu,\ zv=yu\}\longrightarrow X_1.
\tag{1.2}
\]
Again the projection is projective. For \(u\ne0\), its formulas are
\((x,z,y)=(x,ax,a^2x)\), where \(a=v/u\). For \(v\ne0\), they are
\((x,z,y)=(b'^2y,b'y,y)\). The overlap is
\[
b'=a^{-1},\qquad y=a^2x.
\tag{1.3}
\]
Consequently \(Y_1=\operatorname{Tot}\mathcal O(-2)\) is smooth of dimension two. A nonzero point has a unique incidence direction, and the vertex has fibre \(\mathbb P^1\). The two surface maps therefore have identical fibre dimensions. Their exceptional curves have different normal bundles, a difference we will detect in the splitting map.

Now set
\[
Q=\{(x,z,w,y):xy=zw\},\qquad
M=\begin{pmatrix}x&z\\w&y\end{pmatrix}.
\]
Resolve by remembering the image line:
\[
q:Y=\{(M,\ell):\operatorname{im}M\subseteq\ell\}\longrightarrow Q,
\qquad \ell\in\mathbb P^1.
\tag{1.4}
\]
The two columns range independently in \(\ell\), so
\(Y=\operatorname{Tot}(\mathcal O(-1)\oplus\mathcal O(-1))\). In particular it is smooth of dimension three. Incidence makes \(q\) projective. A nonzero matrix in \(Q\) has rank one and a unique image line; the zero matrix allows every line. This resolution also has an exceptional \(\mathbb P^1\), but its source has dimension three.

In the two surfaces, twice the exceptional fibre dimension equals the codimension of the vertex: \(2=2\). In the threefold the inequality is strict: \(2<3\). This is the distinction we now formalize.

## 2. The dimension test and the intermediate extension

Let \(f:\widetilde X\to X\) be proper and surjective, with smooth irreducible source of dimension \(d\). Work with an adapted finite stratification into connected smooth strata. For \(x\) in a stratum \(S\), put \(s=\dim S\) and \(r_S=\dim f^{-1}(x)\), constant along the stratum. Define semismallness by
\[
s+2r_S\le d\quad\hbox{for every }S.
\tag{2.1}
\]
This definition includes the dense stratum. If \(n=\dim X\), its generic fibre has dimension \(d-n\); hence (2.1) gives \(n+2(d-n)\le d\), or \(d\le n\). Surjectivity gives \(n\le d\), so \(n=d\) and \(f\) is generically finite. It is now legitimate to rewrite (2.1) as \(2r_S\le\operatorname{codim}_X S\).

Call \(S\) relevant when equality holds. Choose a smooth dense open \(U\) where \(f\) is finite and \(L=(f_*\Lambda)|_U\) is lisse. The map is small if the inequality is strict on every stratum outside \(U\). Shrinking this open does not alter smallness: new boundary strata inside it have zero-dimensional fibres and positive codimension. Over \(\mathbb C\), the generic local system is the covering representation. In characteristic \(p\), its rank counts geometric points, so purely inseparable multiplicities do not contribute to the rank.

One can test semismallness without choosing stalk degrees:
\[
\dim(\widetilde X\times_X\widetilde X)\le d.
\tag{2.2}
\]
Over \(S\), the fibre product has fibre dimension \(2r_S\), and therefore dimension \(s+2r_S\). Taking the maximum over the finite stratification shows that (2.2) is equivalent to (2.1).

### The top group of a fibre

For a constructible sheaf \(A\) on a variety \(F\) of dimension at most \(r\),
\[
H_c^i(F,A)=0\quad(i>2r).
\tag{2.3}
\]
To prove this, first take a local system on a smooth connected stratum of dimension \(e\). Oriented duality identifies the dual group with \(H^{2e-i}(F,A^\vee(e))\), which vanishes in negative degrees. A finite smooth stratification and the compact-support localization sequence then prove (2.3) for every constructible sheaf.

For constant coefficients the endpoint is also explicit. Let \(b\) be the number of \(r\)-dimensional irreducible components. Remove their singular loci, their mutual intersections and all smaller components. The remaining disjoint smooth dense opens have complement of dimension at most \(r-1\). Both degrees \(2r-1\) and \(2r\) of the complement vanish in compact support, so localization and smooth duality give
\[
H_c^{2r}(F,\Lambda)=\Lambda(-r)^b.
\tag{2.4}
\]
If \(F\) is proper, these are its ordinary cohomology groups. The basis is dual to the top component classes. In families, monodromy permutes the components and hence this basis; the complex orientation fixes the signs. In the étale setting the Tate factor records the additional arithmetic action.

### The perverse criterion

Put \(P=Rf_*\Lambda[d]\). Proper base change gives
\[
\mathcal H^a(i_S^*P)_x=H^{a+d}(f^{-1}(x),\Lambda).
\tag{2.5}
\]
If (2.1) holds, (2.3) makes this zero for \(a>-s\). This is the upper perverse condition. On the other hand, properness and smooth orientation give
\[
D_XP=P(d).
\tag{2.6}
\]
The same upper bound holds for the right side, and duality exchanges the two perverse bounds. Therefore \(P\) is perverse. Conversely, the nonzero top fibre group in (2.4) occurs in degree \(2r_S-d\). Perversity forces \(2r_S-d\le-s\). We have proved
\[
Rf_*\Lambda[d]\text{ is perverse}\quad\Longleftrightarrow\quad f\text{ is semismall}.
\tag{2.7}
\]
The proof applies also to an oriented \(\Lambda\)-rational homology manifold source, provided \(\Lambda[d]=\operatorname{IC}_{\widetilde X}\) and \(\omega_{\widetilde X}=\Lambda(d)[2d]\). These are the actual hypotheses replacing smoothness. For a general singular source its constant complex need not be IC or self-dual with this shift.

If \(f\) is small, strict inequality improves the stalk bound to vanishing for \(a\ge-s\) on the boundary. Duality on a smooth \(s\)-stratum sends degree \(b\) to degree \(-b-2s\), so (2.6) gives costalk vanishing for \(a\le-s\). These are exactly the two strict IC boundary conditions. Since \(P|_U=L[d]\), we obtain
\[
Rf_*\Lambda[d]=\operatorname{IC}_X(L).
\tag{2.8}
\]
This argument does not use the decomposition theorem. For a birational resolution \(L=\Lambda\). For a finite cover of degree greater than one, \(L\) generally has greater rank. Finite maps are small, including ramified maps after removing their branch locus; the rank-one conclusion requires the generic isomorphism. Lesson 8's double-cover decomposition is an example with two generic characters and no additional boundary support.

## 3. Multiplicities and the three resolutions

Assume now the geometric decomposition theorem of Lesson 8 at the chosen characteristic-zero coefficient scope. Smooth constant sources are IC sources. For the finite-field argument, use proper purity and geometric semisimplicity from Lesson 7. Then a semismall pushforward has the form
\[
P=\bigoplus_{S\ \mathrm{relevant}}\operatorname{IC}_{\overline S}(L_S),
\qquad
L_S=(R^{d-s}f_*\Lambda)|_S=(R^{2r_S}f_*\Lambda)|_S.
\tag{3.1}
\]
Here the stratification is refined to make each support the closure of a stratum. No extra cohomological shifts occur, because (2.7) puts \(P\) in the perverse heart.

To identify the local systems rather than just their ranks, restrict the semisimple perverse decomposition to a stratum \(S\) and take ordinary degree \(-s\). A summand supported on \(\overline S\) contributes its defining local system. A larger-support IC contributes zero in this degree by its strict boundary bound, and a disjoint support contributes nothing. Thus the sum of the local systems with that support equals \(\mathcal H^{-s}i_S^*P\). Formula (2.5) identifies it with \(R^{d-s}f_*\Lambda\). If \(2r_S<d-s\), it vanishes by (2.3); if equality holds, (2.4) identifies it with the top component representation, twisted by \((-r_S)\). This proves (3.1).

The component representation has finite permutation monodromy. In characteristic zero it is semisimple: given an invariant subspace, average any projection onto it over the finite group to obtain an equivariant projection. This argument applies to geometric monodromy; the arithmetic representation also contains its Tate factor. We have not asserted arithmetic semisimplicity for every pure complex.

Grouping simple subobjects by their irreducible support gives intrinsic subobjects of a semisimple perverse object: there are no nonzero morphisms between nonisomorphic simple objects, so different support groups do not mix. This yields its canonical decomposition by supports. Choosing bases or decomposing a multiplicity representation into specified irreducible factors is an additional choice. The general derived splitting in several perverse degrees has a different, less canonical character.

For (1.1), the relevant strata are the punctured plane and the origin. They give
\[
Rb_*\Lambda_B[2]=\Lambda_{\mathbb A^2}[2]\oplus\Lambda_{\{0\}}(-1).
\tag{3.2}
\]
For (1.2), the same dimension calculation gives
\[
R\pi_{1*}\Lambda_{Y_1}[2]
=\operatorname{IC}_{X_1}\oplus\Lambda_{\{0\}}(-1)
=\Lambda_{X_1}[2]\oplus\Lambda_{\{0\}}(-1).
\tag{3.3}
\]
The last equality has a precise earlier proof. Lesson 8, Section 1, identifies the finite quotient
\((u,v)\mapsto(u^2,uv,v^2)\) and applies the invariant projector to its finite IC pushforward. The projector's stalks are constant functions on the finite orbits, giving \(\operatorname{IC}_{X_1}=\Lambda[2]\). That proof works classically and in odd ground characteristic with the stated étale coefficients. A classical calculation of the link \(\mathbb{RP}^3\) alone would not establish the étale assertion.

The map (1.4) is small, so its formula needs no decomposition theorem:
\[
Rq_*\Lambda_Y[3]=\operatorname{IC}_Q.
\tag{3.4}
\]
At the vertex, proper base change yields \(R\Gamma(\mathbb P^1,\Lambda)[3]\). The stalk groups are \(\Lambda\) in degree \(-3\) and \(\Lambda(-1)\) in degree \(-1\). Using \(D\operatorname{IC}_Q=\operatorname{IC}_Q(3)\), the costalk groups are \(\Lambda(-2)\) in degree \(1\) and \(\Lambda(-3)\) in degree \(3\). The exceptional curve has produced an IC stalk group, not a point-supported summand.

The vector bundle \(Y\to\mathbb P^1\) has the same ordinary cohomology as its base: use fibrewise contraction classically or affine-space homotopy invariance étale. After cancelling the IC normalization shift, (3.4) gives
\[
IH^0(Q)=\Lambda,\qquad IH^2(Q)=\Lambda(-1).
\tag{3.5}
\]
Properness identifies compactly supported IH with \(H_c^*(Y)\). Smooth three-dimensional duality therefore gives
\[
IH_c^4(Q)=\Lambda(-2),\qquad IH_c^6(Q)=\Lambda(-3).
\tag{3.6}
\]
All other groups in (3.5)–(3.6) vanish. In the classical topology the affine cone \(Q\) itself contracts to its vertex, so its ordinary cohomology has only degree zero. This explicitly separates ordinary cohomology from intersection cohomology.

## 4. The map that splits a relevant stratum

Work first in the perverse category over any field \(k\). Suppose \(i:S\hookrightarrow X\) is a closed smooth stratum of dimension \(s\), \(j\) is its open complement, and \(P\) is perverse and constructible for this stratification. The cohomology sheaves of its two restrictions to \(S\) are local systems. Put
\[
A=\mathcal H^{-s}(i^!P),\qquad B=\mathcal H^{-s}(i^*P),
\qquad \alpha:A\longrightarrow B.
\tag{4.1}
\]
The last map is induced by the closed adjunction comparison \(i^!P\to i^*P\). It is a morphism of local systems, with more information than the equality of their ranks.

### Splitting by adjunction

The perverse bounds on a lisse stratum mean that \(i^!P\) has no ordinary degrees below \(-s\), and \(i^*P\) has none above \(-s\). Their canonical truncation maps and adjunction therefore give morphisms in the perverse heart
\[
i_*A[s]\xrightarrow{u}P\xrightarrow{v}i_*B[s],
\qquad vu=i_*\alpha[s].
\tag{4.2}
\]
If \(\alpha\) is invertible, \(u\alpha^{-1}\) is a section of \(v\). Set \(Q'=\ker v\) in that abelian heart. The resulting decomposition of \(P\) makes the degree \(-s\) groups of both restrictions of \(Q'\) zero. By adjunction and perverse truncation, for any perverse \(C\) on \(S\),
\[
\operatorname{Hom}(Q',i_*C)=0=\operatorname{Hom}(i_*C,Q').
\]
Thus \(Q'\) has no quotient and no subobject supported on \(S\). Since its open restriction is \(j^*P\), the characterization of intermediate extension gives
\[
P=i_*B[s]\oplus j_{!*}j^*P.
\tag{4.3}
\]
Conversely, assume the whole local system \(B\) occurs as a direct summand \(i_*B[s]\) and \(\operatorname{rank}A=\operatorname{rank}B\). Additivity makes the complementary summand's degree \(-s\) stalk group zero. The rank equality makes its costalk group in that degree zero as well. The comparison is the identity on the supported summand; hence \(\alpha\) is invertible. Splitting a smaller part of \(B\) would not give this conclusion.

For a smooth-source semismall direct image, duality gives the required equality of ranks. Applying (4.3) to a closed stratum, then to the open complement, proves by induction
\[
P=\bigoplus_{S\ \mathrm{relevant}}\operatorname{IC}_{\overline S}(B_S)
\quad\Longleftrightarrow\quad
\alpha_S\text{ is an isomorphism for every }S.
\tag{4.4}
\]
For a locally closed \(S\), define its comparison after restricting to the open set \(X\setminus(\overline S\setminus S)\), where \(S\) is closed. In the induction, open restriction preserves these local comparisons, and additive intermediate extension transports the open decomposition to the corresponding ICs. This uses additivity, not a claim that intermediate extension is exact on all short exact sequences. For the converse, strict IC boundary bounds make both degree \(-s\) groups vanish on every larger support, while the term with support \(\overline S\) has the identity comparison. Nonrelevant strata have both groups zero by (2.3) and duality.

No semisimplicity assumption on the \(B_S\) entered this equivalence. The resulting object is semisimple precisely when all its defining local systems are semisimple, by the classification of simple perverse sheaves as ICs of simple local systems. Finite permutation monodromy is semisimple by averaging if its group order is invertible in \(k\); that qualification matters in positive coefficient characteristic.

### Identifying the comparison with intersection

For this identification the varieties are complex. Fix adapted local transverse-slice data at a point of \(S\). Locally the proper map is a stratified product of a slice map \(\pi:M\to N\) and a contractible open part of \(S\); \(M\) is smooth of dimension \(m=d-s\). The smoothness assertion has a concrete differential criterion. Choose \(s\) local functions restricting to coordinates on \(S\). An adapted source stratum maps submersively to \(S\), so their pullbacks have independent differentials along each point of the fibre. Their common level set is therefore smooth near the compact fibre. The proper stratified local product is an additional part of the adapted-slice input; smoothness of the level set alone does not prove it.

Write \(F=\pi^{-1}(x)\) and \(e:F\hookrightarrow M\). The product shifts the degree \(-s\) comparison to degree zero for \(R\pi_*k_M[m]\). Define Borel–Moore homology by
\(H_b^{\mathrm{BM}}(F;k)=H^{-b}(F,\omega_F)\). Proper base change, including its exceptional version, and \(e^!k_M[2m]=\omega_F\) give
\[
H^0(i_x^!R\pi_*k_M[m])=H_m^{\mathrm{BM}}(F;k),
\qquad H^0(i_x^*R\pi_*k_M[m])=H^m(F;k).
\tag{4.5}
\]
For proper \(F\) and field coefficients these groups are dual. The comparison is induced by forgetting supports, \(e^!k_M\to e^*k_M\). Indeed it comes from the counit \(e_*e^!k_M\to k_M\); proper pushforward and the base-change adjunction identities carry this counit to the one defining the point comparison. This specifies the map and its sign.

In the relevant case \(m=2r_S\). Represent classes \(c,d\in H_m^{\mathrm{BM}}(F;k)\) by maps \(k_F\to e^!k_M[m]\). Their pairing is the composite
\[
k\longrightarrow R\Gamma(F,k_F)
\xrightarrow{c}R\Gamma(F,e^!k_M[m])
\longrightarrow R\Gamma(F,k_F[m])
\xrightarrow{d[m]}R\Gamma(F,\omega_F)
\xrightarrow{\operatorname{tr}}k.
\tag{4.6}
\]
Oriented duality identifies the supported group with \(H^m(M,M\setminus F;k)\). Under this identification, (4.6) is cup product of the two supported classes followed by integration, allowing one factor to forget its supports. The relative cochain product has exactly this description: a cocycle vanishing away from \(F\) multiplies an ordinary cocycle and remains supported on \(F\). The product and orientation conventions are those constructed in Lesson 1, Appendices D.1–D.5. Thus (4.6) is the geometric intersection form, not just an abstract map between groups of equal dimension.

For clarity, its basis and coefficient change can also be obtained by localization. Remove the smaller-dimensional pieces from the \(r_S\)-dimensional components of \(F\). For a smooth oriented stratum of complex dimension \(e\), Borel–Moore homology in degree \(b>2e\) is ordinary cohomology in negative degree \(2e-b\), and vanishes, over \(\mathbb Z\) as well as over \(k\). Induction on strata gives the same bound for the removed part. Its degrees \(2r_S\) and \(2r_S-1\) therefore vanish. The Borel–Moore localization sequence identifies the top group of \(F\) with that of the disjoint dense smooth opens. Each open supplies its oriented fundamental class. Consequently the integral top group is free on the top components, and reduction of coefficients carries this basis to the basis over \(k\). Integral relative cup product defines an integer intersection matrix, whose reduction is the matrix of \(\alpha_S\) over \(k\).

Together with (4.4), this proves the classical intersection-form criterion: the IC decomposition exists if and only if all these matrices are nondegenerate over the coefficient field. No parity hypothesis is required. General definiteness of the matrices is a stronger assertion and is not proved by this criterion.

### The scalars minus one and minus two

For the zero section of a complex line bundle \(N\) on \(\mathbb P^1\), the supported class is its Thom class. Pulling it back to the zero section is the Euler class of \(N\), by its definition in Lesson 1, Appendix D.5. The local-zero and dual-line calculations in D.6 and E.5 give
\[
\int_{\mathbb P^1}e(\mathcal O(-1))=-1,\qquad
\int_{\mathbb P^1}e(\mathcal O(-2))=-2.
\tag{4.7}
\]
In particular, the first matrix is invertible over every field. The second vanishes over a field of characteristic two. The incidence chart transitions (1.1) and (1.3) identify precisely these normal bundles, fixing the geometric sign.

Take the complex \(A_1\) resolution with such a characteristic-two coefficient field. Its perverse pushforward \(P=R\pi_{1*}k[2]\) has one-dimensional spaces \(\operatorname{Hom}(k_{\{0\}},P)\) and \(\operatorname{Hom}(P,k_{\{0\}})\). Their composition is multiplication by the intersection scalar, now zero. A skyscraper direct summand would supply inclusion and projection whose composite is the identity, which is impossible. Moreover \(P\) is indecomposable: its open restriction is rank one, so any nontrivial direct-sum decomposition would have a nonzero summand supported at the vertex. The two-stratum perverse category makes such a summand a sum of skyscrapers, already excluded. Thus a top fibre component does not guarantee a split summand in arbitrary coefficient characteristic.

## 5. The two-point Hilbert scheme, including families

We construct \(\operatorname{Hilb}^2\mathbb A^2\) over a ground field in which \(2\) is invertible. In fact the coordinate argument works over any base ring with \(2\) invertible. A family is a quotient algebra \(R\) of the polynomial algebra in \(x,y\), locally free of rank two on the base. Define its centre by
\[
a_0=\tfrac12\operatorname{Tr}(m_x),\qquad
b_0=\tfrac12\operatorname{Tr}(m_y),
\quad \xi=x-a_0,\quad\eta=y-b_0.
\tag{5.1}
\]
Here \(m_x\) means multiplication by \(x\). Traces commute with base change. Since the trace of the unit is two, the trace map splits
\(R=\mathcal O\cdot1\oplus R_0\), with \(R_0\) a line bundle. Both \(\xi\) and \(\eta\) lie in \(R_0\).

Locally choose a generator \(\epsilon\) of \(R_0\). The matrix of \(m_\epsilon\) has trace zero, so its quadratic Cayley–Hamilton identity gives \(\epsilon^2=c\cdot1\) for some scalar \(c\). Write \(\xi=u\epsilon,\eta=v\epsilon\). The coefficients \(u,v\) generate the unit ideal: otherwise, in a residue field where both vanish, the images of \(x,y\) would be scalars and could not generate the rank-two quotient algebra. Thus the opens where \(u\) or \(v\) is invertible cover every base, including a nonreduced base.

On the first open, use \(\epsilon=\xi\). The centred quotient has the unique presentation
\[
(\eta-a\xi,\ \xi^2-c),\qquad(a,c)\in\mathbb A^2.
\tag{5.2}
\]
Conversely this presentation is free with basis \(1,\xi\), and both coordinates have trace zero. On the other open the presentation is
\[
(\xi-b\eta,\ \eta^2-c'),\qquad(b,c')\in\mathbb A^2.
\tag{5.3}
\]
Equality of the two quotient algebras on the overlap gives \(b=a^{-1}\), \(c'=a^2c\). These transformations commute with every base change, and the two presentations recover every family uniquely on their opens. Gluing therefore represents the centred Hilbert functor. Restoring the free centre coordinates proves
\[
\operatorname{Hilb}^2\mathbb A^2
=\mathbb A^2\times\operatorname{Tot}\mathcal O_{\mathbb P^1}(-2).
\tag{5.4}
\]
This gives smoothness and dimension four directly, without using a general smoothness theorem for Hilbert schemes.

For the symmetric square, write an ordered pair as its centre and its half-difference \((u,v)\). Interchanging the pair fixes the centre and sends \((u,v)\) to \((-u,-v)\). Invariant monomials have even total degree, so they are generated by \(A=u^2,B=uv,C=v^2\) with relation \(AC=B^2\). Reducing by that relation gives distinct monomials in \(u,v\), proving that there is no further relation. Hence
\[
\operatorname{Sym}^2\mathbb A^2=\mathbb A^2\times\{AC=B^2\}.
\tag{5.5}
\]
The morphism to this quotient exists on all Hilbert families, not only on pairs of distinct geometric points. Define its invariant coordinates by
\[
A=\tfrac12\operatorname{Tr}(m_{\xi^2}),\quad
B=\tfrac12\operatorname{Tr}(m_{\xi\eta}),\quad
C=\tfrac12\operatorname{Tr}(m_{\eta^2}).
\tag{5.6}
\]
In a trace-zero generator these are \(u^2c,uvc,v^2c\), so \(AC=B^2\) holds over the base ring itself. Formula (5.6) is independent of the generator and compatible with base change. It gives the usual length-two cycle morphism: for every linear form \(t\xi+z\eta\), multiplication has characteristic polynomial
\[
T^2-(t^2A+2tzB+z^2C),
\]
which records the two values with their multiplicities. These quadratic coefficients are exactly the invariant coordinates in (5.5). Thus the construction identifies the norm-defined cycle map on families, without inferring equality over nilpotents merely from equality on geometric points.

In chart (5.2), the map is
\[
(a,c)\longmapsto(A,B,C)=(c,ac,a^2c).
\tag{5.7}
\]
Comparing with (1.2) and (1.3), Hilbert–Chow is \(\operatorname{id}_{\mathbb A^2}\times\pi_1\). It is proper. Distinct pairs have a point fibre; over the diagonal \(D=\{2p\}\simeq\mathbb A^2\), the fibre is \(\mathbb P^1\). The two pairs \((s,r)\) are \((4,0)\) and \((2,1)\). Both are relevant, and the map is semismall but not small. Its product description makes the diagonal component local system constant. With the default characteristic-zero sheaf coefficients,
\[
Rh_*\Lambda[4]
=\operatorname{IC}_{\operatorname{Sym}^2\mathbb A^2}
\oplus i_{D*}\Lambda_D2
=\Lambda[4]\oplus i_{D*}\Lambda_D2.
\tag{5.8}
\]
The last equality follows from the smooth centre factor and the finite-quotient IC proof used in (3.3). At a diagonal point, the stalk degrees are \(-4,-2\), with groups \(\Lambda,\Lambda(-1)\), agreeing with the shifted fibre cohomology. On a transverse slice over \(\mathbb C\), the intersection matrix is \((-2)\). Therefore characteristic-two sheaf coefficients prevent the full diagonal summand from splitting. This coefficient obstruction is compatible with using complex ground coordinates in (5.1)–(5.7).

The bundle description gives source cohomology \(H^0=\Lambda,H^2=\Lambda(-1)\), with other groups zero. The target has only \(IH^0=\Lambda\). Classically use contraction of the centre times cone. Étale, use the finite quotient \(\mathbb A^4\to\operatorname{Sym}^2\mathbb A^2\): its higher direct images vanish by proper base change on finite fibres, and averaging identifies its invariant sheaf with the constant sheaf, since each geometric fibre is one permutation orbit. Taking the invariant summand of \(H^*(\mathbb A^4,\Lambda)=\Lambda\) proves the claim. In ordinary source degree \(a\), the diagonal term of (5.8) contributes
\[
H^{a-2}(\mathbb A^2,\Lambda)(-1),
\tag{5.9}
\]
which accounts exactly for the extra degree-two class.

## 6. Convolution and the scope of the dimension argument

Convolution spaces need not be smooth. We therefore prove a version of the dimension argument for a perverse complex on a stratified source. Let \(m:Z\to W\) be proper, let \(A\) be perverse, and take compatible finite stratifications for \(A\), \(DA\) and the direct images. Suppose that for each source stratum \(T\), target stratum \(S\), and point \(y\in S\),
\[
2\dim(m^{-1}(y)\cap T)\le\dim T-\dim S
\tag{6.1}
\]
when the intersection is nonempty. Then \(Rm_*A\) is perverse.

Indeed, put \(t=\dim T\), \(s=\dim S\) and \(F_T=m^{-1}(y)\cap T\). The upper perverse bound says that \(\mathcal H^b(A|_T)=0\) for \(b>-t\). Apply (2.3) to the cohomology sheaves on \(F_T\). The bounded compact hypercohomology spectral sequence has terms
\[
H_c^a(F_T,\mathcal H^b(A|_{F_T})),\qquad
a\le2\dim F_T,\quad b\le-t.
\]
Thus its total degrees are at most \(2\dim F_T-t\le-s\). Filter the fibre by closed unions of strata and apply localization to combine these bounds. Proper base change yields the upper perverse condition for \(Rm_*A\). The identical argument for \(DA\), followed by proper duality, yields the lower condition.

Refining target strata to ensure constructibility decreases their dimensions and weakens (6.1). Refining a source stratum decreases its dimension as well, so one must check (6.1) again or retain the original cohomological bound \(-t\) on its pieces. An arbitrary refinement is not automatically a proof of a new source-dimension inequality.

For a complex connected reductive group, the affine Grassmannian
\(\operatorname{Gr}=G(\mathbb C((z)))/G(\mathbb C[[z]])\) has bounded convolution maps
\[
\overline{\operatorname{Gr}}_\lambda\widetilde\times
\overline{\operatorname{Gr}}_\mu
\xrightarrow{m}\overline{\operatorname{Gr}}_{\lambda+\mu}
\tag{6.2}
\]
for dominant coweights. Mirković–Vilonen, Lemma 4.4, proves stratified semismallness for the orbit and twisted-product strata. Their proof identifies the fibre with a torus-invariant subset in the first Grassmannian factor and bounds its dimension using semi-infinite-orbit geometry and the possible fixed points. Since \(\dim\operatorname{Gr}_\alpha=2\langle\rho,\alpha\rangle\) for dominant \(\alpha\), the estimate supplies (6.1). The closure bars in their properness assertion are essential: bounded closed Schubert supports are proper over the target, not individual open orbits.

With field coefficients, the twisted external product of two equivariant perverse sheaves is perverse once the equivariant descent construction is supplied. Applying the preceding proof to (6.2) then proves perversity of convolution, the assertion of their Proposition 4.2. Over general coefficient rings, derived tensor products require the paper's flatness hypotheses. The proof of the Grassmannian dimension estimate and the exact descent input are additional geometry; the dimension-count argument above does not establish them. The erratum changes a finite-type step in the later Tannakian argument, not this convolution criterion. The programme's *Convolution and rigidity*, GL-SAT lesson 7, is the corresponding further topic.

The relative \(B_{\mathrm{dR}}^+\) Grassmannian has a separate statement. Fargues–Scholze, Proposition VI.8.1, treats bounded complexes on the relative Hecke stack over their divisor base and proves that convolution preserves universal local acyclicity, preserves \({}^pD^{\le0}\), and preserves the relative Satake category of Section VI.7, including its flatness condition. Its proof uses fusion, constant terms, universal local acyclicity and duality over diamonds. These are three specified assertions in that setting; they do not follow just by applying the smooth-variety argument (2.7).

For comparison with the two-point calculation, the general Hilbert–Chow programme for a smooth surface uses strata indexed by partitions \(\nu\) of \(n\). A stratum with \(l(\nu)\) distinct support points has dimension \(2l(\nu)\). If the punctual length-\(a\) Hilbert scheme is irreducible of dimension \(a-1\), the product of punctual fibres has dimension
\[
\sum_i(\nu_i-1)=n-l(\nu),
\]
and every such stratum is relevant in source dimension \(2n\). Irreducibility makes its top component local system rank one, with Tate twist \(-(n-l(\nu))\). This derives the dimension and multiplicity calculation from those precise inputs. Smoothness of the full Hilbert scheme, properness and local product structure, and the punctual irreducibility/dimension theorem for arbitrary length are still required to prove the general assertion. The explicit families in Section 5 establish these facts for length two; they do not establish them for arbitrary length. Full Satake and the Springer/Hitchin construction discussed by Nadler likewise retain their additional assigned mathematical scope.

## 7. Exercises with solutions

### Exercise 1 — the plane blow-up

Verify both semismallness and failure of smallness for (1.1). Compute the normalized and unshifted direct images, retaining the exceptional Tate twist.

**Solution.** On the complement of the origin, the equation forces the unique direction \([x:y]\), so the fibre has dimension zero over a two-dimensional stratum. Over the origin the direction is arbitrary, giving \(\mathbb P^1\); this stratum has dimension zero. Thus \(s+2r=2\) on both strata. The source is smooth of dimension two by its charts, and closed incidence makes the map proper. Equality on the boundary proves that it is semismall and not small. The generic local system is rank-one constant. At zero its top fibre group is \(H^2(\mathbb P^1,\Lambda)=\Lambda(-1)\). Formula (3.1) yields
\[
Rb_*\Lambda[2]=\Lambda_{\mathbb A^2}[2]\oplus\Lambda_{\{0\}}(-1).
\]
Shift both sides by \([-2]\) to obtain
\(Rb_*\Lambda=\Lambda_{\mathbb A^2}\oplus\Lambda_{\{0\}}(-1)[-2]\).
Classically the intersection scalar \(-1\) gives the same supported splitting over any coefficient field, by (4.3).

### Exercise 2 — the image-line resolution

Prove that (1.4) is a proper smooth small resolution and identify the local system that appears in its IC formula.

**Solution.** The condition that both columns belong to \(\ell\) is closed in \(Q\times\mathbb P^1\); hence projection is projective and proper. Over a line \(\ell\), each column is an independent vector in \(\ell\), giving the vector bundle \(\mathcal O(-1)^2\) over \(\mathbb P^1\). Its local charts are three-dimensional affine spaces, so the source is smooth of dimension three. A nonzero matrix of determinant zero has rank one and its image line recovers the unique inverse point. The inverse is algebraic on the opens where either column is nonzero. Thus projection is an isomorphism off the vertex. Over zero it has the whole \(\mathbb P^1\). The open stratum has \((s,r)=(3,0)\); the vertex has \((s,r)=(0,1)\). Their inequalities are equality \(3=3\) and strict inequality \(2<3\), proving smallness. The isomorphism open makes \(L=\Lambda\), so the strict-boundary proof (2.8) gives \(Rq_*\Lambda[3]=\operatorname{IC}_Q\).

### Exercise 3 — stalks, costalks and global IH

Compute the vertex stalk and costalk of the IC in Exercise 2, and its ordinary and compactly supported intersection cohomology.

**Solution.** The proper fibre is \(\mathbb P^1\). Its cohomology is \(\Lambda\) in degree zero and \(\Lambda(-1)\) in degree two; the shift \([3]\) places these in stalk degrees \(-3\) and \(-1\). For the costalk, apply point duality to \(i^*\operatorname{IC}_Q(3)\), because \(i^!\operatorname{IC}_Q=D(i^*D\operatorname{IC}_Q)\) and \(D\operatorname{IC}_Q=\operatorname{IC}_Q(3)\). The twisted stalk groups \(\Lambda(3)\), \(\Lambda(2)\) dualize into \(\Lambda(-3)\) in degree three and \(\Lambda(-2)\) in degree one. No other groups occur.

The vector-bundle source has ordinary cohomology equal to that of \(\mathbb P^1\), by contraction or affine-space homotopy invariance. Hence
\(IH^0(Q)=\Lambda\) and \(IH^2(Q)=\Lambda(-1)\). Properness gives \(IH_c^a(Q)=H_c^a(Y)\). Oriented duality in dimension three says \(H_c^{6-b}(Y)=H^b(Y)^\vee(-3)\). For \(b=0,2\), this yields \(IH_c^6(Q)=\Lambda(-3)\), \(IH_c^4(Q)=\Lambda(-2)\), respectively. The vanishing of the other source cohomology groups proves all remaining vanishings.

### Exercise 4 — the surface with normal bundle of degree minus two

Compute the direct image for (1.2), its vertex stalk and costalk with the default coefficients, and explain the obstruction with characteristic-two coefficients on the complex surface.

**Solution.** The two charts (1.3) exhibit a smooth \(\mathcal O(-2)\) surface. Projection is proper by incidence, is an isomorphism off zero, and has fibre \(\mathbb P^1\) over zero. Thus both strata satisfy \(s+2r=2\), so the origin is relevant. Its multiplicity group is \(\Lambda(-1)\). The finite-quotient invariant-projector proof in Lesson 8, Section 1, gives \(\operatorname{IC}_{X_1}=\Lambda[2]\) at the stated coefficient and odd ground-characteristic scope. Therefore
\[
P=R\pi_{1*}\Lambda[2]=\Lambda_{X_1}[2]\oplus\Lambda_{\{0\}}(-1).
\]
Its vertex stalk is \(\Lambda\) in degree \(-2\), \(\Lambda(-1)\) in degree zero. Since \(DP=P(2)\), the costalk is \(\Lambda(-1)\) in degree zero and \(\Lambda(-2)\) in degree two. IC alone satisfies strict boundary conditions; the degree-zero stalk and costalk here belong to the point summand. Without normalization, that summand is \(\Lambda_{\{0\}}(-1)[-2]\).

Over a characteristic-two coefficient field on the complex variety, the exceptional curve's normal degree gives comparison scalar \(-2=0\). Inclusion and projection of a hypothetical point summand would compose to one, but every such composite is zero by (4.2) and (4.7). Consequently this point summand does not split; the argument at the end of Section 4 also proves indecomposability. The fibre dimensions and perversity are unchanged.

### Exercise 5 — construct and calculate two-point Hilbert–Chow

Construct the centred Hilbert charts as a functor on bases with \(2\) invertible. Identify the cycle morphism on families, then compute relevant strata, local systems, direct image and ordinary cohomology.

**Solution.** For a finite locally free rank-two quotient algebra, half the multiplication traces give centre coordinates. Subtract them from \(x,y\). Trace splitting gives \(R=\mathcal O1\oplus R_0\), where \(R_0\) is a line bundle. A generator \(\epsilon\) of that line satisfies \(\epsilon^2=c\) by the trace-zero Cayley–Hamilton identity. Write the centred coordinates \(\xi=u\epsilon,\eta=v\epsilon\). Because they generate the algebra along with the unit, \(u,v\) cannot both vanish in any residue field and generate the unit ideal. Thus the opens where either is invertible cover the base. On them the two unique presentations are
\((\eta-a\xi,\xi^2-c)\) and \((\xi-b\eta,\eta^2-c')\).
They are flat rank-two quotients, and they glue by \(b=a^{-1},c'=a^2c\). This proves the functorial description as \(\operatorname{Tot}\mathcal O(-2)\), and restoring the centre gives the smooth fourfold (5.4).

The symmetric square is the centre times the sign quotient of the half-difference plane, whose invariant ring is \(k[A,B,C]/(AC-B^2)\). For the family define \(A,B,C\) by the three half-traces in (5.6). With \(\xi=u\epsilon,\eta=v\epsilon\), they are \(u^2c,uvc,v^2c\); the relation holds over the base itself. The characteristic polynomial of multiplication by \(t\xi+z\eta\) is \(T^2-t^2A-2tzB-z^2C\), verifying its cycle multiplicities and compatibility with arbitrary base change. On the first chart this gives \((A,B,C)=(c,ac,a^2c)\). It is precisely the incidence resolution (1.2), times the centre. Properness follows at once.

Over distinct pairs the fibre is a point, while over a double point \(c=0\) and the projective direction is free, giving \(\mathbb P^1\). Thus the open and diagonal strata have \((s,r)=(4,0),(2,1)\) in source dimension four. Both are relevant, and the diagonal prevents smallness. The generic local system is constant of rank one. The global product description trivializes the diagonal component local system as \(\Lambda(-1)\). Formula (3.1), followed by the finite-quotient IC calculation, yields
\[
Rh_*\Lambda[4]=\Lambda_{\operatorname{Sym}^2\mathbb A^2}[4]
\oplus i_{D*}\Lambda_D2.
\]
The diagonal-point stalk has \(\Lambda\) in degree \(-4\) and \(\Lambda(-1)\) in degree \(-2\). Finally (5.4) gives source cohomology in degrees zero and two only, equal to \(\Lambda\) and \(\Lambda(-1)\). Contraction classically, or the exact invariant summand of the finite \(\mathbb A^4\) quotient étale, gives target \(IH^0=\Lambda\) only. The diagonal summand contributes \(H^{a-2}(D,\Lambda)(-1)\) in source degree \(a\); as \(D=\mathbb A^2\), this is the single extra degree-two class.

## Exact prerequisites still required

The dimension bounds, small-map IC argument, closed-stratum splitting criterion, and explicit resolution and two-point Hilbert calculations have been written above using their indicated earlier sheaf operations. General characteristic-zero semismall decomposition additionally uses the geometric theorem of Lessons 7–8, with its remaining weight, comparison and ordinary/adic foundations. The classical intersection-form identification uses the specified adapted transverse local product, oriented duality and its compatible relative cup product; its full recursive foundation check, and a general positive-characteristic étale slice replacement, are not supplied by the matrix criterion. Nor is definiteness of general intersection forms proved here.

The affine-Grassmannian fibre estimate, orbit geometry and twisted external-product descent remain the exact geometric prerequisites of Section 6. Fargues–Scholze's three relative convolution assertions retain their diamond and flatness foundations. General Hilbert–Chow retains the arbitrary-length punctual geometry and global Hilbert-scheme assertions listed there. Full Satake and Nadler's Springer/Hitchin construction are retained parts of the expanded programme, not consequences of the two-point example. Springer theory is the subject of the next lesson. Each of these broader assertions still requires a complete programme proof; a free reference identifies its source and does not replace that proof.

## References

- M. A. A. de Cataldo and L. Migliorini, [*The decomposition theorem, perverse sheaves and the topology of algebraic maps*](https://arxiv.org/abs/0712.0349), §4.2 on semismall maps and intersection forms, and §4.2.3 on Hilbert schemes. In the notation here, top fibre components have dimension \((d-s)/2\) and the stratum comparison has degree \(-s\).
- D. Juteau, C. Mautner and G. Williamson, [*Parity sheaves*](https://arxiv.org/abs/0906.2994v3), free author manuscript, version 3, §3 on intersection forms and the semismall decomposition criterion. That criterion does not require parity vanishing.
- I. Mirković and K. Vilonen, [*Geometric Langlands duality and representations of algebraic groups over commutative rings*](https://annals.math.princeton.edu/2007/166-1/p03), §4, especially Proposition 4.2 and Lemma 4.4; [erratum](https://annals.math.princeton.edu/2018/188-3/p06).
- A. Beilinson, J. Bernstein and P. Deligne, [*Faisceaux pervers*](https://publications.ias.edu/sites/default/files/Faisceaux%20pervers.pdf), Astérisque 100 (1982), 5.3.8 and 6.2.5.
- L. Fargues and P. Scholze, [*Geometrization of the local Langlands correspondence*](https://arxiv.org/abs/2102.13459), Proposition VI.8.1, with the relative Satake category of §VI.7.
- D. Nadler, [*Springer theory via the Hitchin fibration*](https://arxiv.org/abs/0806.4566), §4.1, for the subsequent Springer/Hitchin topic.
