# Semismall maps and small resolutions

*AI-generated exposition by GPT-6 Astra (OpenAI), October 2026. Public domain (CC0).*

An exceptional curve in a surface and an exceptional curve in a threefold behave differently under direct image. In the surface it can supply a perverse summand at a point. In the threefold it can belong to the stalk of the intersection complex itself. We begin with explicit resolutions exhibiting this difference, derive the dimension test that explains it, and then identify the map that decides whether the additional summand splits. The two-point Hilbert scheme gives a family version of the surface calculation.

Use the normalization
\[
\operatorname{IC}_X(L)=j_{!*}L[\dim X],\qquad
IH^a(X,L)=H^{a-\dim X}(X,\operatorname{IC}_X(L)).
\]
Closed-support ICs are understood to be pushed into the ambient variety. Our default coefficients \(\Lambda\) are a characteristic-zero field in the classical topology, or \(\overline{\mathbb Q}_\ell\) in the étale topology with \(\ell\) invertible on the variety. Arithmetic formulas keep Tate twists; decompositions obtained from finite-field weights are asserted geometrically. Section 4 separately allows any coefficient field \(k\) on complex varieties. Characteristic two for \(k\) there does not mean that the variety has characteristic two.

The earlier inputs are proper base change, localization and oriented duality from [Constructible complexes on algebraic varieties](constructible-complexes-on-algebraic-varieties.md), the strict boundary characterization in [Intermediate extensions and intersection complexes](intermediate-extensions-and-intersection-complexes.md), and, for general characteristic-zero splitting, [The decomposition theorem](the-decomposition-theorem.md). We will distinguish the arguments needing that last theorem from the ones proved by dimensions and adjunction alone.

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

For this identification the varieties are complex. Fix a point of \(S\). Proposition 4.1 below constructs a slice map \(\pi:M\to N\) and a product of its source pair with a contractible open part of \(S\); \(M\) is smooth of dimension \(m=d-s\). The smoothness assertion has a concrete differential criterion. Choose \(s\) local functions restricting to coordinates on \(S\). An adapted source stratum maps submersively to \(S\), so their pullbacks have independent differentials along each point of the fibre. Their common level set is therefore smooth near the compact fibre. Proposition 4.1 constructs the pair product by proper controlled flows; Proposition 4.2 identifies its actual support comparison.

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

### 4.1. Constructing the transverse source pair

We give the local geometry needed in (4.5), including its support comparison. All spaces in this subsection have their classical topology. Let \(f:Y\to X\) be a proper morphism of complex varieties, with \(Y\) smooth of complex dimension \(d\). The properness used below is compactness of inverse images of compact sets in this topology. Choose finite compatible Whitney stratifications for which every source stratum maps submersively onto a target stratum. Such stratifications, including prescribed algebraic markings, are constructed in [Lesson 1, K.6–K.7](constructible-complexes-on-algebraic-varieties.md#k-7-compatible-stratifications-of-an-algebraic-map). Fix \(x\) in a target stratum \(S\), of dimension \(s\).

**Proposition 4.1.** There are an open neighborhood \(V\) of \(x\) in \(X\), a coordinate box \(B\subset S\) centered at \(x\), and a holomorphic coordinate projection \(p\) with \(p|_S=1\), for which the following holds. Put
\[
\begin{gathered}
N=V\cap p^{-1}(x),\qquad M=f^{-1}(N),\qquad F=f^{-1}(x),\\
Z=f^{-1}(V),\qquad W=f^{-1}(B),\qquad g=p\circ f.
\end{gathered}
\tag{4.8}
\]
Then \(M\) is smooth of complex dimension \(m=d-s\), \(\pi=f|_M:M\to N\) is proper, and there is a homeomorphism of pairs over \(B\)
\[
h:(B\times M,\ B\times F)\xrightarrow{\sim}(Z,W).
\tag{4.9}
\]
It preserves the induced strata and is the identity on the fiber over \(x\). On \(W\), the morphism \(f\) is the projection to \(B\) under (4.9).

**Proof.** Work in a local embedding of \(X\) in a complex manifold. Holomorphic submanifold coordinates flatten \(S\); write them as \((y,z)\), with \(S=\{z=0\}\), and set
\[
p(y,z)=y,\qquad \rho(y,z)=|z|^2.
\tag{4.10}
\]
Translate \(y(x)\) to zero. Remove the closures of the finitely many target strata not incident to \(S\). On a sufficiently small neighborhood, every remaining stratum is either \(S\) or has \(S\) in its frontier.

Whitney regularity makes \((p,\rho)\) submersive on every such upper stratum at all sufficiently small positive normal radii, uniformly over a compact smaller box in \(S\). Here is the rank test. If a sequence of rank defects tends to \(y_0\in S\), normalize a linear relation among the rows of \(dp\) and \(d|z|\). In the limit it is a vector \(a+bv\), of norm one, perpendicular to a limiting upper tangent plane \(E\), where \(a\) is horizontal and \(v\) is a unit normal secant. Whitney (a) gives the horizontal space in \(E\), and Whitney (b), applied to the secants from \((y,z)\) to \((y,0)\), gives \(v\in E\). Thus \(a+bv\) lies both in \(E\) and its orthogonal complement, a contradiction. The complex tangent planes are regarded here as real tangent planes. Squaring the radius does not change the rank at positive radius. This is the local calculation of [Lesson 1, I.2](constructible-complexes-on-algebraic-varieties.md#i-2-whitney-regularity-and-the-tubular-submersion).

At every point of \(F\), the differential of \(g=p f\) is surjective: it is already surjective on the tangent space of the source stratum mapping to \(S\). The critical set of \(g\) in the smooth source is closed. Its image under the proper map \(f\) is closed relative to the coordinate neighborhood and misses \(x\). Shrink that neighborhood to avoid this image. Consequently \(g\) is a holomorphic submersion throughout the part of \(Y\) now under consideration. Its level \(M\) is smooth of dimension \(d-s\).

Choose a sufficiently small fixed \(r>0\) and a box \(B\) with compact closure in the coordinate chart. The closed normal cap and its inverse image are
\[
C=X\cap\{y\in B,\ \rho\le r^2\},\qquad
\overline Z=f^{-1}(C).
\tag{4.11}
\]
Choose the closure of the cap inside the previously chosen neighborhood. For a compact \(K\subset B\), the set \(C\cap p^{-1}(K)\) is closed in the compact product of \(K\) with the closed normal ball. Its inverse image under \(f\) is compact. Hence \(g:\overline Z\to B\) is proper.

Stratify \(\overline Z\) by intersecting the source strata with the interior and boundary of this cap. On each source stratum above a target stratum different from \(S\), the map \((g,\rho f)\) is submersive: \(f\) is submersive onto that target stratum, and the preceding rank test applies there. Above \(S\), the map \(g\) is submersive and the radius is zero. Therefore \(g\) is submersive on every interior stratum and on every boundary stratum \(\rho f=r^2\).

The cap partition is Whitney. For a pair of boundary strata, tangent spaces are intersections of the original tangent spaces with \(\ker d(\rho f)\). The differential is nonzero on the lower tangent space. Whitney (a) therefore makes the intersections of a converging family of upper tangent planes converge to the intersection of its limit with that kernel; a right inverse for a surjective row is its transpose divided by its squared norm. A secant within the level has limit in the kernel by the first-order expansion of \(\rho f\), so original Whitney (b) gives the boundary Whitney condition. For an interior upper stratum and a boundary lower stratum, the upper tangent plane is unchanged and the lower tangent is smaller, so original (a) and (b) suffice. When both pieces come from the same original stratum, smooth half-space coordinates give the conditions directly. The frontier rule is preserved by these transverse cuts.

Apply the [controlled-flow construction and proper isotopy argument of Lesson 1, I.3–I.6](constructible-complexes-on-algebraic-varieties.md#i-6-proper-stratified-submersions-and-normal-cones) to \(g:\overline Z\to B\). Concretely, lift the real coordinate vector fields of \(B\) by fields tangent to all these strata. The compatible tube equations keep each lift projected to the prescribed coordinate field and keep its controlled normal radii fixed. Its flow is continuous across strata and leaves every compact set at a finite maximal endpoint. A lifted coordinate segment stays in the compact inverse image of that segment, so it exists for its entire length. Composing the flows in a fixed order gives
\[
B\times g^{-1}(x)\longrightarrow\overline Z.
\tag{4.12}
\]
The inverse composes the opposite-time flows in reverse order. This proves bijectivity and continuity in both directions; commutation of the lifts is unnecessary. At the center all flow times are zero.

Both the outer boundary and \(W\) are unions of these strata. The homeomorphism preserves them. Removing the outer boundary gives (4.9), with
\(V=X\cap\{y\in B,\rho<r^2\}\). This is open in \(X\); \(M=g^{-1}(x)\cap Z\) is the smooth level already established, and \(N=V\cap p^{-1}(x)\). The map \(\pi\) is the base change of the proper map \(f\). On \(W\), its target is \(S=\{z=0\}\), so \(f|_W=g|_W\), proving the projection assertion. If \(s=0\), the box is a point and the construction is the identity. \(\square\)

The homeomorphism (4.9) specifies the source pair needed for local intersection. It does not assert an analytic product, or an intertwining of the entire morphism \(f\) with a product morphism away from \(W\).

### 4.2. The actual comparison on the slice

**Proposition 4.2.** Let \(k\) be any coefficient field, let \(P=Rf_*k_Y[d]\), and let \(i:B\hookrightarrow V\) be the closed stratum in Proposition 4.1. With \(e:F\hookrightarrow M\), there are identifications carrying the degree \(-s\) comparison of (4.1) to
\[
H^m(F,e^!k_M)\longrightarrow H^m(F,k_F),
\qquad m=d-s,
\tag{4.13}
\]
induced by forgetting support. Thus, for a semismall \(f\), the comparison is exactly the transverse intersection map used in (4.5)–(4.6).

**Proof.** Denote the inclusion \(W\hookrightarrow Z\) by \(a\) and its proper projection to \(B\) by \(b\). Closed-support base change and proper base change give
\[
i^!P=Rb_*a^!k_Z[d],
\qquad
i^*P=Rb_*k_W[d].
\tag{4.14}
\]
The arrow between them is the image of \(a^!k_Z\to a^*k_Z\). To check the first identity and this assertion at the map level, take the localization triangle for \(a\) and apply \(Rf_*\). The open complement is the inverse image of \(V\setminus B\), and direct-image composition identifies its open direct image with the open direct image of \(j^*Rf_*k_Z\). The resulting triangle is the closed-support localization triangle for \(i\). Its first map is the image of the original support counit. Composing with restriction to \(B\) gives exactly the comparison in (4.14). The constructions of these triangles and their counits are in [Lesson 1, B.2](constructible-complexes-on-algebraic-varieties.md#b-2-the-actual-open-closed-recollement); [H.2](constructible-complexes-on-algebraic-varieties.md#h-2-derived-fibers-bounds-and-arbitrary-proper-support-base-change) proves the actual proper-base-change evaluation.

Under the pair homeomorphism, restriction to the central slice gives an isomorphism
\[
(a^!k_Z)|_F\xrightarrow{\sim}e^!k_M.
\tag{4.15}
\]
We verify it without a noncharacteristic base-change assumption. In \(B\times M\), take a product neighborhood \(B'\times O\), where \(B'\) is convex. The closed support is \(B'\times(F\cap O)\). The supported section complex is the fiber of restriction to its complement, hence is computed by relative singular cochains
\[
C^\bullet\bigl(B'\times O,\ B'\times(O\setminus F);k\bigr).
\tag{4.16}
\]
The natural sheaf comparison and its compatibility with restrictions are proved in [Lesson 1, C.1–C.2](constructible-complexes-on-algebraic-varieties.md#c-2-the-actual-sheaf-singular-comparison). Both \(O\) and \(O\setminus F\) are open subsets of a manifold; no smoothness of \(F\) is needed. Projection to \(O\) and inclusion of any slice are inverse homotopy equivalences of these pairs: contract the convex coordinate \(B'\), leaving \(O\setminus F\) invariant. The prism operator is a relative chain homotopy, so pullback to the slice gives an isomorphism from (4.16) to
\(C^\bullet(O,O\setminus F;k)\). Passing to neighborhood germs gives (4.15). The square with the maps from relative to ordinary cochains commutes before taking cohomology, proving compatibility with the support-forgetting map. These same relative chain identities hold with integer coefficients, by [Lesson 1, D.1–D.2](constructible-complexes-on-algebraic-varieties.md#d-1-integral-small-chains-pairs-and-covers).

Now take the stalk at \(x\) of (4.14), using properness of \(b\). Its two complexes are
\[
R\Gamma(F,e^!k_M)[d],
\qquad R\Gamma(F,k_F)[d],
\tag{4.17}
\]
and the arrow is induced by the same support-forgetting map. Degree \(-s\) of these complexes is degree \(d-s=m\) before shifting, which gives (4.13).

Finally the complex orientation of the smooth slice gives
\[
e^!k_M[2m]=\omega_F,\qquad
H^m(F,e^!k_M)=H^{-m}(F,\omega_F)
 =H_m^{\mathrm{BM}}(F;k).
\tag{4.18}
\]
The dimension in this orientation is that of \(M\), not that of \(Y\). The slice is the level of the holomorphic submersion \(g\), so its orientation is the complex orientation used in the relative cup-product calculation. The comparison in (4.13) has already been identified before invoking orientation; the identification (4.18) therefore turns it into the supported intersection pairing, with the counit and trace of (4.6). Relative cochain restriction also commutes with coefficient change. In the top-component bases constructed above, the integral matrix consequently reduces to the matrix over \(k\). \(\square\)

This proves the classical transverse geometry required by the intersection-form criterion. The sheaf-theoretic splitting equivalence (4.4) and this local calculation hold in every coefficient characteristic. Nondegeneracy, or definiteness, of a particular geometric intersection matrix is a further mathematical assertion.

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
\oplus i_{D*}\Lambda_D[2](-1)
=\Lambda[4]\oplus i_{D*}\Lambda_D[2](-1).
\tag{5.8}
\]
The last equality follows from the smooth centre factor and the finite-quotient IC proof used in (3.3). At a diagonal point, the stalk degrees are \(-4,-2\), with groups \(\Lambda,\Lambda(-1)\), agreeing with the shifted fibre cohomology. On a transverse slice over \(\mathbb C\), the intersection matrix is \((-2)\). Therefore characteristic-two sheaf coefficients prevent the full diagonal summand from splitting. This coefficient obstruction is compatible with using complex ground coordinates in (5.1)–(5.7).

The bundle description gives source cohomology \(H^0=\Lambda,H^2=\Lambda(-1)\), with other groups zero. The target has only \(IH^0=\Lambda\). Classically use contraction of the centre times cone. Étale, use the finite quotient \(\mathbb A^4\to\operatorname{Sym}^2\mathbb A^2\): its higher direct images vanish by proper base change on finite fibres, and averaging identifies its invariant sheaf with the constant sheaf, since each geometric fibre is one permutation orbit. Taking the invariant summand of \(H^*(\mathbb A^4,\Lambda)=\Lambda\) proves the claim. In ordinary source degree \(a\), the diagonal term of (5.8) contributes
\[
H^{a-2}(\mathbb A^2,\Lambda)(-1),
\tag{5.9}
\]
which accounts exactly for the extra degree-two class.

### Arbitrary length and separated supports

Let \(X\) be a smooth irreducible quasi-projective surface over an algebraically closed field \(k\). For every \(n\ge0\),
\[
\operatorname{Hilb}^n(X)\text{ is smooth and irreducible of dimension }2n.
\tag{5.10}
\]
The case \(n=0\) is a point. The complete proof of (5.10), in every characteristic, is in [Tangent spaces and obstructions for Hilbert and Quot schemes, Theorem 7.4](course:AG-HP/tangent-spaces-and-obstructions-for-hilbert-and-quot-schemes#smoothness-and-irreducibility-on-a-surface). Its inputs are the tangent identification in Proposition 1.1, the finite-resolution calculation \(\dim_k\operatorname{Hom}(I,k[x,y]/I)=2n\) in Lemma 7.1, the explicit staircase smoothing in Lemma 7.2, and the finite flat monomial degeneration in Lemma 7.3. The tangent calculation and those families together prove regularity and membership in the component of distinct configurations. The theorem then constructs étale plane-coordinate charts on the Hilbert scheme of a surface. This argument does not require the finite subscheme to be a complete intersection, and does not invert \(n!\).

We next prove a product statement that applies to families, including families over nonreduced bases. Write a length-\(n\) subscheme as
\[
Z=Z_1\amalg\cdots\amalg Z_r,\qquad
\operatorname{Supp}(Z_i)=\{x_i\},\qquad
\operatorname{length}(Z_i)=n_i.
\tag{5.11}
\]
Here the \(x_i\) are distinct and \(\sum_i n_i=n\). The decomposition follows by applying the Chinese remainder theorem to the local Artin factors of the finite coordinate algebra. Choose affine open neighbourhoods \(V_i\subset X\) of \(x_i\). The opens \(V_i\) may intersect.

**Proposition 5.1.** In \(\prod_i\operatorname{Hilb}^{n_i}(V_i)\), let \(D\) be the locus of tuples whose members have pairwise disjoint images in \(X\). Then \(D\) is open and disjoint union defines an étale morphism
\[
u:D\longrightarrow\operatorname{Hilb}^n(X).
\tag{5.12}
\]
It sends \((Z_1,\ldots,Z_r)\) to \(Z\). The construction commutes with arbitrary base change.

**Proof.** The representing schemes and their locally finite presentation follow from the explicit finite-algebra charts in [Hilbert and Quot schemes, Proposition 5.1](course:AG-HP/hilbert-and-quot-schemes#5-finite-points-on-affine-schemes). On the product parameter scheme, consider two universal finite families. Their fibre product over the parameter scheme is finite over that scheme. Inside it, equality of the two images in \(X\) is a closed condition because the diagonal of \(X\) is closed. Its image in the parameter scheme is therefore closed. Removing these images for all pairs gives the claimed open locus \(D\).

Each family in \(V_i\) is also a closed subscheme of \(X\) over the parameter scheme: its map to \(X\) is an immersion, and is proper by its closed graph and finiteness over the base. On \(D\) their ideals are pairwise comaximal. Their intersection consequently defines a closed subscheme with coordinate algebra the product of their finite locally free algebras. Its rank is \(\sum_i n_i=n\). This constructs \(u\), and the product decomposition proves compatibility with every base change.

For formal étaleness, take a surjection \(A'\to A\) with nilpotent kernel \(J\), a family \(Z'\subset X_{A'}\) finite locally free of rank \(n\), and a specified decomposition of its reduction corresponding to a point of \(D(A)\). Write \(B'=\Gamma(Z',\mathcal O_{Z'})\). The given decomposition of \(B'/JB'\) is a set of orthogonal idempotents summing to one. They lift uniquely to \(B'\).

Here is the ring calculation for that assertion. If \(N^2=0\) and \(x\) lifts an idempotent modulo \(N\), put \(q=x^2-x\in N\) and
\[
e=x-(2x-1)q.
\tag{5.13}
\]
Expansion gives \(e^2-e=q^2(4q-3)=0\). If two lifts differ by \(\delta\in N\), their idempotent equations give \((2e-1)\delta=0\); since \((2e-1)^2=1\), they agree. Applying this argument successively to \(N^j/N^{j+1}\) proves existence and uniqueness for any nilpotent ideal. The products of the lifted idempotents lift zero and hence are zero. Their sum is an idempotent lifting one and hence is one. Thus
\[
B'=\prod_i e_iB'.
\tag{5.14}
\]
Each factor is a direct summand of the finite locally free \(A'\)-module \(B'\), so is finite locally free. It has rank \(n_i\), since a nilpotent thickening leaves the underlying topological space unchanged. The associated closed subscheme \(Z_i'\subset Z'\) remains inside \(V_i\) for the same reason. The \(Z_i'\) are pairwise disjoint, give a lift to \(D(A')\), and are uniquely determined. This proves the formal étale lifting property, without a characteristic restriction.

All the schemes concerned are locally of finite type over \(k\), so \(u\) is locally of finite presentation. The infinitesimal criterion in [Infinitesimal lifting and the invariance of étale morphisms under thickenings, Theorem 4.1](course:AG-FSE/infinitesimal-lifting-and-invariance-under-thickenings#section-4) now proves that \(u\) is étale. \(\square\)

In particular, for any local Artin \(k\)-algebra with residue field \(k\), embedded deformations of \(Z\) correspond uniquely to tuples of embedded deformations of the \(Z_i\) inside the \(V_i\). Proposition 5.1 is stronger than a tangent-space decomposition: it identifies the lifting problem at every nilpotent order.

There is also an elementary compatibility with norm coordinates. For a finite locally free algebra \(B=\prod_i B_i\) over a ring \(A\), and an element \(a=(a_i)\), multiplication is block diagonal. Hence, as polynomials over \(A\),
\[
\det(T-m_a\mid B)=\prod_i\det(T-m_{a_i}\mid B_i).
\tag{5.15}
\]
This can be checked on opens where the summands are free, where it is the determinant formula for a block diagonal matrix; those identities agree on overlaps. It therefore holds over nonreduced bases as well. It is the compatibility required of norm descriptions under disjoint union. Properness of the cycle morphism is proved below. Lemma 5.3 gives the punctual dimension \(a-1\), and Theorem 5.5 proves irreducibility of the entire punctual length-\(a\) fibre. Irreducibility of the full smooth Hilbert scheme in (5.10) does not imply irreducibility of those fibres.

### The cycle morphism and its properness

Keep \(X,k,n\) as in (5.10). There is a proper morphism
\[
h_n:\operatorname{Hilb}^n(X)\longrightarrow\operatorname{Sym}^n(X),
\qquad
Z\longmapsto\sum_x\operatorname{length}(\mathcal O_{Z,x})[x].
\tag{5.16}
\]
We construct the morphism, including its action on nonreduced parameter schemes, and prove properness. For \(n=0\) it is the identity of a point; assume \(n>0\).

**The symmetric target.** For an affine open \(U=\operatorname{Spec}A\), put
\[
T_n(A)=\bigl(A^{\otimes_k n}\bigr)^{\mathfrak S_n},
\qquad
Q_U=\operatorname{Spec}T_n(A).
\tag{5.17}
\]
The tensor product is the coordinate ring of \(U^n\). For a finite group acting on a finitely generated algebra \(C\), every \(c\in C\) satisfies the monic polynomial \(\prod_g(T-gc)\) with invariant coefficients. Thus \(C\) is finite over \(C^G\): finitely many algebra generators are integral, and their bounded powers span a finite module. The finite-extension algebra lemma in [Hilbert and Quot schemes, Section 9](course:AG-HP/hilbert-and-quot-schemes#a-finite-extension-algebra-lemma) proves that \(C^G\) is finitely generated over \(k\). Integral lying-over makes \(\operatorname{Spec}C\to\operatorname{Spec}C^G\) surjective.

Its geometric fibres are exactly the orbits. To see this, extend the field to an algebraically closed field. Invariants commute with that extension: they are the kernel of the finite list of linear maps \(c\mapsto gc-c\), and field extension is flat. For two different finite orbits of closed points, the Chinese remainder theorem gives a function zero on the first and one on the second. The product of its translates is invariant and has the same two values, so distinguishes those orbits.

An invariant open subset has open image, since its invariant complement has closed image under the finite quotient. The restricted quotient has the expected functions. Indeed, near any closed orbit in that open, choose a function vanishing on the complement and nonzero throughout the orbit, and multiply its translates. The resulting invariant function \(g\) gives an invariant principal neighbourhood inside the open. Such neighbourhoods cover: a nonempty complement in a scheme of finite type over \(k\) would have a closed point. On them,
\[
(C_g)^G=(C^G)_g,
\tag{5.18}
\]
because localization is exact and preserves the kernel defining invariants.

Every finite subset of a quasi-projective variety lies in an affine open; the hypersurface-complement proof is given in Theorem 7.4 linked at (5.10). Therefore the opens \(U^n\) cover \(X^n\). Intersections of affine opens of \(X\) are affine, since \(X\) is separated. Formula (5.18) identifies the quotient of \((U\cap V)^n\) with the corresponding opens of both \(Q_U\) and \(Q_V\). They glue to a finite-type scheme \(Q=\operatorname{Sym}^n(X)\) and a finite surjection \(q:X^n\to Q\).

The target \(Q\) is separated. The inverse image of the underlying diagonal under the finite surjection \(q\times q\) is the union of the permutation graphs in \(X^n\times X^n\). Those graphs are closed because \(X^n\) is separated. Their image is closed. Near each point of this image, use an affine open \(Q_U\) containing its common coordinate; on \(Q_U\times Q_U\) the diagonal is a closed immersion. Together with the open complement of the image, these neighbourhoods show that the whole diagonal is a closed immersion.

**Determinants give the affine morphism.** A family on \(U\) over \(\operatorname{Spec}R\) is a quotient \(A\otimes_kR\twoheadrightarrow B\) with \(B\) locally free of rank \(n\) over \(R\). For \(a\in A\), let \(m_a\) be multiplication by its image in \(B\). There is a canonical algebra homomorphism
\[
\Phi_B:T_n(A)\longrightarrow R
\quad\text{with}\quad
\Phi_B\bigl((\textstyle\sum_i t_i a_i)^{\otimes n}\bigr)
=\det\bigl(\textstyle\sum_i t_i m_{a_i}\mid B\bigr).
\tag{5.19}
\]
The equality is an identity of polynomials in any finite list of indeterminates \(t_i\); \(\Phi_B\) is applied to their coefficients.

Here is a construction without division by \(n!\). Choose a \(k\)-basis \((b_\lambda)\) of \(A\). Tensor words in this basis are permuted by \(\mathfrak S_n\). For a finite multiplicity vector \(\alpha\) of total size \(n\), let \(O_\alpha\) be the sum of the distinct words with those multiplicities, each word occurring once. The \(O_\alpha\) form a basis of \(T_n(A)\), in every characteristic. Define \(\Phi_B(O_\alpha)\) to be the coefficient of \(t^\alpha\) in \(\det(\sum_\lambda t_\lambda m_{b_\lambda})\). Only finitely many variables occur in each calculation. Determinants of locally free modules are defined by taking the top exterior power, or equivalently by determinants in local bases; change of basis conjugates the matrix, so these coefficients glue.

Expanding any finite list \(a_i\) in the chosen basis and substituting into this polynomial proves (5.19). It also proves independence of the basis. To check multiplication, use two lists and write \(v=\sum_i t_i a_i\), \(w=\sum_j s_j c_j\). In the tensor algebra,
\[
(vw)^{\otimes n}=v^{\otimes n}w^{\otimes n},
\qquad
\det(m_{vw})=\det(m_v)\det(m_w).
\tag{5.20}
\]
Apply (5.19) to the finite list of products \(a_ic_j\). Comparing coefficients of \(t^\alpha s^\beta\) in (5.20), with the two lists chosen from a basis, gives
\(\Phi_B(O_\alpha O_\beta)=\Phi_B(O_\alpha)\Phi_B(O_\beta)\).
The value on the tensor unit is \(\det(1_B)=1\). Thus \(\Phi_B\) is an algebra homomorphism. All formulas commute with arbitrary changes of the parameter ring \(R\), including nonflat ones. They define
\[
h_U:\operatorname{Hilb}^n(U)\longrightarrow Q_U.
\tag{5.21}
\]

At a geometric point, the finite algebra is a product of local Artin algebras \(B_x\). A composition series for \(B_x\) has \(\dim B_x\) one-dimensional residue-field factors. Multiplication by \(a\) acts on each factor as the scalar \(a(x)\). Consequently
\[
\det(m_a\mid B)=\prod_x a(x)^{\dim B_x}.
\tag{5.22}
\]
Apply the same calculation to a linear combination with indeterminates. Its coefficients show that (5.21) has exactly the value in (5.16).

These local morphisms glue on the smooth Hilbert scheme from (5.10). On an overlap they have identical values at every geometric point by (5.22). Their equalizer is closed because \(Q\) is separated, and is the whole overlap as a closed subscheme: on each affine open its defining ideal vanishes at all closed points, and hence is zero by the Nullstellensatz and reducedness of the smooth source. This gives \(h_n\). Moreover,
\[
h_n^{-1}(Q_U)=\operatorname{Hilb}^n(U).
\tag{5.23}
\]
Both sides are open, and equality is detected on geometric points by their support. Thus the gluing retains the affine construction on every such open. Since the local formulas describe a morphism of representing schemes, they give its functorial action on arbitrary parameter schemes.

**Limits over valuation rings.** It suffices to prove that (5.21) is proper. Its source has a finite cover by the multiplication-matrix charts of Proposition 5.1 of *Hilbert and Quot schemes*: there are only finitely many choices of \(n\) basis monomials of degree at most \(n-1\). It is therefore of finite type over \(k\), and Noetherian. The target is affine of finite type, so \(h_U\) is of finite type and quasi-separated.

Let \(R\) be any valuation ring containing \(k\), with fraction field \(K\). Consider a valuation diagram for \(h_U\). The generic family gives an \(n\)-dimensional quotient algebra \(B_K\) of \(A\otimes_kK\), and the extending cycle gives a homomorphism \(\psi:T_n(A)\to R\) whose extension to \(K\) is \(\Phi_{B_K}\). For \(a\in A\), let \(a^{(j)}\) denote \(a\) in the \(j\)-th tensor factor. The invariant polynomial
\[
P_a(T)=\prod_{j=1}^n(T-a^{(j)})\in T_n(A)[T]
\quad\text{satisfies}\quad
\psi(P_a(T))=\det(T-m_a\mid B_K)\in R[T].
\tag{5.24}
\]
This follows from (5.19), applied to \(T\cdot1-a\). Cayley–Hamilton therefore gives a monic equation over \(R\) for the image of every \(a\) in \(B_K\). The identity follows directly by expanding
\((TI-M)\operatorname{adj}(TI-M)=\det(TI-M)I\): the coefficient recursions give \(\det(TI-M)|_{T=M}=0\).

Choose algebra generators \(a_1,\ldots,a_s\) of \(A\), and form the image algebra
\[
B_R=R[\overline a_1,\ldots,\overline a_s]\subset B_K.
\tag{5.25}
\]
The monic equations of degree \(n\) show that the monomials \(\prod_i\overline a_i^{e_i}\), \(0\le e_i<n\), span it over \(R\). It is finite and torsion-free, and \(B_R\otimes_RK=B_K\).

For clarity, every finite torsion-free module \(M\) over a valuation ring is free. Choose a finite generating list minimal under deletion. If it were linearly dependent over \(K\), clear denominators in a relation. Among its nonzero coefficients choose one whose principal ideal contains all the others, using comparability of principal ideals in a valuation ring. Divide the relation by that coefficient in \(M\otimes_RK\). Torsion-freeness identifies \(M\) with its image there, so the resulting relation, with one coefficient equal to one and all others in \(R\), expresses one generator through the others. This contradicts minimality. The list is therefore a basis.

Apply this to \(B_R\). Its rank is \(n\), so the quotient \(A\otimes_kR\twoheadrightarrow B_R\) defines a finite flat family on \(U_R\). Its norm map equals \(\psi\): both maps to the domain \(R\) agree after its injection into \(K\). This is an extension of the diagram. Any other finite flat quotient extending the generic family injects into \(B_K\), since it is torsion-free, and its image is necessarily the image algebra (5.25). Thus the extension is unique.

The general valuative criterion in [Proper morphisms and the valuative criterion of properness, Theorem 3.1](course:AG-MO/proper-morphisms-and-valuative-criteria#3-the-general-valuative-criterion) proves properness of \(h_U\). Its Theorem 2.1 and (5.23) prove properness of \(h_n\). This completes the proof of (5.16), without a restriction on the characteristic or on the rank of the valuation ring.

The determinant construction is the norm description of Hilbert–Chow; Rydh's freely available [*Hilbert and Chow schemes of points, symmetric products and divided powers*, Section 4.3](https://people.kth.se/~dary/thesis/thesis-paperIII.pdf) describes its relation to the general divided-power construction. Equations (5.19)–(5.25) give the construction and the properness argument needed here directly. Proposition 5.2 identifies each fibre with its punctual factors, Lemma 5.3 computes their dimension, and Theorem 5.5 proves their irreducibility.

### Punctual factors and their dimensions

For a closed point \(x\in X\), denote the scheme-theoretic fibre of \(h_a\) over \(a[x]\) by \(F_a(X,x)\). No reduced structure is implicit in this notation.

**Proposition 5.2.** If \(\xi=\sum_{i=1}^r n_i[x_i]\), where the \(x_i\) are distinct and \(\sum_i n_i=n\), disjoint union gives an isomorphism of schemes
\[
\prod_{i=1}^r F_{n_i}(X,x_i)\ \xrightarrow{\ \sim\ }\ h_n^{-1}(\xi).
\tag{5.26}
\]

**Proof.** Put the finite set of support points in one affine open \(U=\operatorname{Spec}A\). Every family in either side lies in \(U\): on every geometric fibre its support lies there, so the inverse image of \(X\setminus U\) is empty. Work over an arbitrary affine parameter scheme \(\operatorname{Spec}R\). Choose \(f\in A\) with pairwise distinct values \(\lambda_i=f(x_i)\), using the Chinese remainder theorem. Define
\[
P(T)=\prod_i(T-\lambda_i)^{n_i}.
\tag{5.27}
\]
For the finite locally free algebra \(B\) of a family with cycle \(\xi\), (5.24) gives \(P(f)=0\) in \(B\). The factors of \(P\) are pairwise coprime over \(k\). Choose polynomials \(E_i(T)\) which are one modulo the \(i\)-th factor and zero modulo the others. Their classes are orthogonal idempotents summing to one in \(k[T]/P\). Hence
\[
e_i=E_i(f),\qquad B=\prod_i B_i,\qquad B_i=e_iB.
\tag{5.28}
\]
Each factor is finite locally free. At every geometric parameter point it selects exactly the local Artin algebra at \(x_i\), so has rank \(n_i\).

It remains to verify the cycle of each factor over \(R\), including its nilpotents. For any finite symbolic linear combination \(a=\sum_j t_j a_j\) of elements of \(A\), apply the norm identity of the given family to \(E_i(f)a+1-E_i(f)\). Multiplication by this element is multiplication by \(a\) on \(B_i\) and the identity on all other factors. At the support points its values are \(a(x_i)\) and \(1\). Consequently
\[
\det(m_a\mid B_i)=a(x_i)^{n_i}.
\tag{5.29}
\]
Coefficient comparison in (5.19) says precisely that \(B_i\) has the constant cycle \(n_i[x_i]\) as an \(R\)-point of the symmetric scheme. This is stronger than equality on geometric parameter points.

Conversely, families with those punctual cycles have disjoint supports and hence disjoint scheme-theoretic images. Their union is finite flat and its determinant is the product of their determinants, giving cycle \(\xi\). On its \(i\)-th factor, \((f-\lambda_i)^{n_i}=0\) by Cayley–Hamilton, so \(E_i(f)\) acts as the identity there and as zero on the other factors. Thus the two constructions are inverse. They commute with every base change, and the decomposition is consequently independent of the separating function. Gluing on the parameter scheme and the representing property prove (5.26). \(\square\)

**Plane coordinates for a punctual fibre.** Choose affine étale coordinates \((u,v):V\to\mathbb A^2\) near \(x\), with \(x\) mapping to zero, and shrink so that the fibre over zero is just \(x\). Write \(V=\operatorname{Spec}A\); then its point ideal is \(\mathfrak m_x=(u,v)\). The formal étale lifting property, with the identical residue field \(k\), gives compatible isomorphisms
\[
k[u,v]/(u,v)^N\ \simeq\ A/\mathfrak m_x^N
\quad(N\ge1).
\tag{5.30}
\]
Indeed the section at the closed point lifts uniquely through each nilpotent thickening of the origin. Its composites with the coordinate map are identities by the same uniqueness, proving the displayed inverse maps. This is the infinitesimal criterion used in the earlier surface proof at (5.10).

For a family in \(F_a(X,x)\), the characteristic polynomials of \(u\) and \(v\) are both \(T^a\). Thus \(u^a=v^a=0\) in its finite algebra and \(\mathfrak m_x^{2a-1}\) acts as zero. The same holds on the plane. Formula (5.30) at \(N=2a-1\) therefore identifies their quotient algebras. Every function on \(V\), modulo that power, is a polynomial in \(u,v\); the polynomial norm identities (5.19) show that the fixed-cycle condition on all functions is preserved in both directions. This proves an isomorphism
\[
F_a(X,x)\simeq F_a(\mathbb A^2,0)
\tag{5.31}
\]
on all parameter schemes, depending on the chosen coordinates.

**Lemma 5.3.** For every \(a\ge1\), the punctual fibre \(F_a(\mathbb A^2,0)\) has dimension \(a-1\) and exactly one irreducible component of that dimension, in every characteristic.

**Proof.** We compute dimensions on reduced varieties; this does not assert that the scheme-theoretic punctual fibre is reduced. Put \(V=k^a\). A framed length-\(a\) quotient of \(k[u,v]\) is the same as commuting matrices \(N,M\in\operatorname{End}(V)\) and a vector \(z\) cyclic for them: the map \(p\mapsto p(N,M)z\) is surjective, and its kernel is an ideal because \(N,M\) commute. Conversely multiplication and the unit of a quotient give these data. On the opens where selected monomials applied to \(z\) form a basis, these constructions are polynomial changes of coordinates, as in the matrix charts used for (5.21). The frame space is locally the product of the Hilbert scheme with \(\operatorname{GL}_a\).

Over an algebraically closed field, a quotient has support at the origin exactly when both commuting matrices are nilpotent. One direction is immediate from its local Artin algebra. For the converse, \(N^a=M^a=0\) implies that \((u,v)^{2a-1}\) kills the quotient, so its support is the origin. Thus the reduced frame space of the punctual fibre is the variety of such nilpotent cyclic triples. This equality on reduced varieties follows from equality of their closed points in the same affine matrix charts; it makes no assertion that the nilpotency equations alone define the full fibre over a nonreduced base.

We supply the linear algebra for its stratification. Every nilpotent operator has a basis of Jordan chains. To construct it, take a chain \(z,Nz,\ldots,N^{d-1}z\) of maximal length \(d\), and a linear functional \(\ell\) equal to one on \(N^{d-1}z\) and zero on the earlier chain vectors. The formula
\[
p(w)=\sum_{j=0}^{d-1}\ell(N^{d-1-j}w)N^jz
\tag{5.32}
\]
defines a projection onto the chain span commuting with \(N\), since \(N^d=0\). Its kernel is invariant; induction gives the other chains.

Let \(\lambda=(\lambda_1,\ldots,\lambda_b)\) be the partition of \(a\) recording the lengths, and let \(m_d\) count its parts equal to \(d\). Fix the corresponding matrix \(N_\lambda\). Its centralizer algebra is
\[
E=\operatorname{End}_{k[t]}
 \left(\bigoplus_{i=1}^b k[t]/t^{\lambda_i}\right),
\qquad
c_\lambda:=\dim E=\sum_{i,j}\min(\lambda_i,\lambda_j).
\tag{5.33}
\]
The dimension formula follows because a homomorphism from a block of length \(d\) to one of length \(e\) sends its generator to a multiple of \(t^{\max(e-d,0)}\) modulo \(t^e\), giving \(\min(d,e)\) free coefficients.

Taking the constant terms between blocks of equal length gives a surjective algebra homomorphism
\[
E\longrightarrow\prod_d\operatorname{Mat}_{m_d}(k).
\tag{5.34}
\]
A composition through a different block length contributes a positive power of \(t\) on returning to the original length, so these constant terms respect multiplication. Constant matrices among equal-length blocks give a section.

Its kernel \(J\) is a nilpotent ideal. A block entry of an element of \(J\) has positive \(t\)-order when the target length is at least the source length: this follows from (5.33) for a strict increase, and from the zero constant term for equal lengths. In any path of \(a\) block transitions, the lengths cannot decrease strictly at every step, because they are integers between one and \(a\). Thus that part of the path contributes at least one power of \(t\). A product of \(a^2\) elements of \(J\) contributes at least \(a\) powers along every path and hence is zero in every target block. Therefore \(J^{a^2}=0\).

An element of \(E\) is nilpotent exactly when all its images in (5.34) are nilpotent. The reverse implication holds because a power then lies in the nilpotent ideal \(J\). The nilpotent cone in \(\operatorname{Mat}_m(k)\) is irreducible of dimension \(m^2-m\): the regular single-chain orbit has centralizer dimension \(m\), and every Jordan matrix is its limit by replacing the zero links between successive chains with a parameter \(s\). For \(s\ne0\) there is one chain; at zero there are the specified blocks. This puts every nilpotent matrix in the closure of that irreducible orbit. A linear splitting of (5.34) consequently identifies the nilpotent locus of \(E\), as a variety, with the product of \(J\) and these nilpotent cones. It is irreducible of dimension
\[
c_\lambda-\sum_d m_d=c_\lambda-b.
\tag{5.35}
\]

The pairs \((N,M)\) with \(N\) of type \(\lambda\) and \(M\) nilpotent commuting with it are the image of
\(\operatorname{GL}_a\times E_{\mathrm{nil}}\)
under simultaneous conjugation. Every fibre is a coset of \(E^\times\), which is open in the \(c_\lambda\)-dimensional vector space \(E\). The dimension-of-fibres formula gives an irreducible pair stratum of dimension \(a^2-b\). Adjoining a cyclic vector is a nonempty open condition in its product with \(V\). Nonemptiness follows directly from the monomial quotient with basis
\[
\{u^iv^j:0\le j<b,\ 0\le i<\lambda_{j+1}\},
\tag{5.36}
\]
where the parts are in decreasing order: multiplication by \(u\) has precisely those chain lengths, multiplication by \(v\) is nilpotent, and \(1\) is cyclic.

Let \(S_\lambda\) be the locus in the reduced punctual fibre where multiplication by \(u\) has type \(\lambda\). The ranks of its powers define a locally closed stratum. The preceding triple space is its frame bundle, with fibres \(\operatorname{GL}_a\). Hence \(S_\lambda\) is irreducible and
\[
\dim S_\lambda=(a^2-b+a)-a^2=a-b.
\tag{5.37}
\]
These are finitely many strata. Only \(\lambda=(a)\) has \(b=1\). In that stratum the powers \(1,u,\ldots,u^{a-1}\) form a basis, and the ideals are
\[
\left(u^a,\ v-\sum_{j=1}^{a-1}c_j u^j\right),
\qquad (c_1,\ldots,c_{a-1})\in\mathbb A^{a-1}.
\tag{5.38}
\]
The constant coefficient of \(v\) is zero at every closed point and hence on the reduced stratum. Thus this stratum is an affine space of dimension \(a-1\). Every other stratum has dimension at most \(a-2\). Its closure supplies the unique component of maximum dimension, proving the lemma. The argument also includes \(a=1\), when the fibre is a point. \(\square\)

The centralizer calculation can be compared with Bulois–Evain, [*Nested punctual Hilbert schemes and commuting varieties of parabolic subalgebras*, Proposition 4.5](https://arxiv.org/abs/1306.4838v2). The proof here uses block homomorphisms and a nilpotent kernel to obtain the precise stratum dimension. The dimension calculation alone does not exclude components of smaller dimension. The socle and incidence argument in Theorem 5.5 proves that the whole punctual fibre is the closure of (5.38).

**Corollary 5.4.** The morphism \(h_n\) is semismall. For a partition \(\nu\) of \(n\), let \(r=l(\nu)\) be its number of parts, and let \(S_\nu\) be the locus of cycles with those multiplicities at distinct support points. Then
\[
\dim S_\nu=2r,\qquad
\dim h_n^{-1}(\xi)=n-r,\qquad
\dim S_\nu+2\dim h_n^{-1}(\xi)=2n
\quad(\xi\in S_\nu).
\tag{5.39}
\]
Each fibre has a unique component of dimension \(n-r\).

Indeed the ordered distinct-point locus in \(X^r\) has dimension \(2r\). Sending a tuple to its weighted cycle has finite geometric fibres, consisting of permutations of equal multiplicities, so its image \(S_\nu\) has the same dimension. This argument allows an inseparable map in positive characteristic. Equations (5.26), (5.31) and (5.37) give the fibre dimension and its unique top component. The examples (5.38) make every fibre nonempty, so \(h_n\) is surjective. Its source is smooth of dimension \(2n\) by (5.10), and it is proper by (5.16). Equation (5.39) proves the semismall inequality. Refining the partition loci for constructibility preserves that inequality; a piece of smaller dimension has a strict inequality.

At the sheaf-operation and coefficient scope of Section 2, it follows that \(Rh_{n*}\Lambda[2n]\) is perverse. Its generic top-component representation on \(S_\nu\) has one basis vector, with twist \(-(n-r)\), by (2.4). Under the geometric decomposition theorem used in Section 3, this gives
\[
Rh_{n*}\Lambda[2n]
=\bigoplus_{\nu\vdash n}
 \operatorname{IC}_{\overline{S_\nu}}(\Lambda)\bigl(-(n-l(\nu))\bigr).
\tag{5.40}
\]
Here the constant coefficient denotes the generic rank-one component local system on each partition locus. Additional smaller pieces in an adapted stratification are not relevant and give no new summands. Formula (5.40) retains the exact characteristic-zero coefficient and geometric decomposition hypotheses of (3.1); it is not a decomposition assertion for arbitrary coefficient rings.

### Socles and irreducibility of punctual fibres

**Theorem 5.5.** Let \(k\) be algebraically closed, in any characteristic, and let \(X\) be a smooth surface over \(k\). Every punctual fibre \(F_a(X,x)\), for \(a\ge1\), is irreducible of dimension \(a-1\). Consequently every fibre of the Hilbert–Chow morphism (5.16) is irreducible.

Irreducibility here is a statement about the underlying space. It does not assert that the scheme-theoretic fibre is reduced. By (5.31) it suffices to work at the origin of the plane. Put
\[
R=k[u,v],\qquad \mathfrak m=(u,v),\qquad
Q_a=F_a(\mathbb A^2,0)_{\mathrm{red}}.
\tag{5.41}
\]
For a point \(B=R/I\) of \(Q_a\), its socle is
\(\operatorname{Soc}(B)=\{b:ub=vb=0\}\). Write \(Q_{a,s}\) for the locus where its dimension is \(s\), with reduced structure. It is locally closed: on a finite-algebra chart it is the constant-rank locus of \(B\to B\oplus B,\ b\mapsto(ub,vb)\). On this locus the socles form a vector bundle, as Gaussian elimination on a nonzero rank minor shows.

We use the height bound for equations from [Dimension theory of Noetherian local rings, Theorem 3.1](course:AG-CA/dimension-theory-of-noetherian-local-rings#3-how-much-can-one-equation-cut), together with the dimension and height formulas in [Krull dimension and Noether normalization, Theorems 4.2–4.3](course:AG-CA/krull-dimension-and-noether-normalization#4-parameters-measure-dimension-and-height). Thus \(r\) equations on an integral variety of dimension \(d\) have all their components of dimension at least \(d-r\). We also use the following direct consequence of dimension as transcendence degree. For a finite-type morphism, stratify its source and target into integral locally closed pieces and apply the tower rule to their function fields. If its fibres have dimension at most \(e\), its source has dimension at most the dimension of its target plus \(e\). For a projective bundle of relative dimension \(e\), equality holds, even when its base has several components.

**One-point extensions.** The Koszul resolution of \(k\) for \(u,v\), tensored with \(B\), has terms of dimensions \(a,2a,a\). Its degree-zero homology is \(k\), and its degree-two homology is the socle. The alternating sum of dimensions therefore gives
\[
\dim_k\operatorname{Tor}_1^R(k,B)=s+1,\qquad
\dim_k I/\mathfrak m I=s+1.
\tag{5.42}
\]
For the second equality use \(0\to I\to R\to B\to0\): the map \(I/\mathfrak m I\to k\) is zero and \(\operatorname{Tor}_1^R(k,R)=0\). The Koszul resolution is exact because multiplication by \(u\) on \(R\), and then by \(v\) on \(R/(u)\), is injective.

A nonzero functional \(\lambda:I/\mathfrak m I\to k\) gives \(I'=\ker(\lambda:I\to k)\) and
\[
0\longrightarrow k\longrightarrow B'=R/I'
 \longrightarrow B\longrightarrow0.
\tag{5.43}
\]
Changing \(\lambda\) by a scalar leaves the nested pair unchanged. Conversely, every nested pair of colengths \(a,a+1\) supported at the origin arises this way. For a fixed \(B'\), its possible quotients \(B\) are obtained by dividing by a line in \(\operatorname{Soc}(B')\). Thus the reduced incidence variety \(Z_a\), with projections \(\alpha,\beta\) to \(Q_a,Q_{a+1}\), has fibres
\[
\alpha^{-1}(B)=\mathbb P^s,\qquad
\beta^{-1}(B')=\mathbb P^{t-1}
\quad\text{if }\dim\operatorname{Soc}(B')=t.
\tag{5.44}
\]
These are algebraic incidence constructions: choose a common truncated polynomial algebra and impose the ideal and containment conditions in Grassmannians. Such a truncation exists since \(\mathfrak m^a B=0\). Indeed the descending powers of \(\mathfrak m B\) must decrease in length until zero; equality of consecutive nonzero powers would contradict Nakayama. Over the reduced parameter spaces the same power vanishes identically, by its vanishing at all closed points. Equivalently, \(\alpha\) is the reduced projectivization of the universal \(I/\mathfrak m I\); over \(Q_{a,s}\) it is a projective bundle. The same assertion for \(\beta\) follows from the socle bundle on \(Q_{a+1,t}\). These descriptions concern reduced incidence varieties and do not identify the full punctual fibre functor with a reduced parameter space.

The connecting map on socles in (5.43) can be written without extension notation. If \(b\in\operatorname{Soc}(B)\) has lift \(f\in R\), set
\[
\delta_\lambda(b)=\bigl(\lambda(uf),\lambda(vf)\bigr)\in k^2.
\qquad
t=s+1-\operatorname{rank}(\delta_\lambda).
\tag{5.45}
\]
The value is independent of the lift because \(\lambda(\mathfrak m I)=0\). A socle element of \(B\) lifts to the socle of \(B'\) precisely when both entries vanish; the kernel of the map from the latter socle to the former is the copy of \(k\) in (5.43). This proves the formula, including \(|s-t|\le1\).

There is a useful exceptional locus \(D_{a,s}\subset Q_{a,s}\): it consists of the quotients for which \(\delta_\lambda=0\) for every functional \(\lambda\). This is a closed condition on the constant-rank stratum, since (5.45) is a bilinear map between its vector bundles. For a point of this locus and any nonzero \(b\in\operatorname{Soc}(B)\), its lift satisfies \(uf,vf\in\mathfrak m I\). If \(J=I+(f)\), then
\[
\mathfrak m J=\mathfrak m I,\qquad
\dim_k J/\mathfrak m J=s+2,\qquad
\dim_k\operatorname{Soc}(R/J)=s+1.
\tag{5.46}
\]
Here \(J/I=kb\), and (5.42) gives the last equality. When \(a=1\), the exceptional locus is empty: \(I=\mathfrak m\), and the lift \(f=1\) has \(u f=u\notin\mathfrak m I\).

**A dimension estimate for every socle stratum.** We prove simultaneously for all \(s\ge1\), by induction on \(a\), that
\[
\dim Q_{a,s}\le a+1-2s.
\tag{5.47}
\]
Empty strata have dimension \(-\infty\). For \(a=1\) the only stratum is a point with \(s=1\).

Suppose the assertion holds through length \(a\). First, for \(a\ge2\), take all socle lines in the quotients belonging to \(D_{a,s}\). This incidence space has dimension \(\dim D_{a,s}+s-1\). By (5.46) its other projection lands in \(Q_{a-1,s+1}\), and its fibres there have dimension at most \(s+1\) by (5.44). The induction hypothesis gives
\[
\dim D_{a,s}+s-1
 \le \bigl(a-2s-2\bigr)+(s+1),\qquad
\dim D_{a,s}\le a-2s.
\tag{5.48}
\]
This is one dimension less than the bound for all of \(Q_{a,s}\).

Fix a target socle dimension \(t\) at length \(a+1\), and split \(\beta^{-1}(Q_{a+1,t})\) according to the source socle dimension \(s\). Only \(s=t-1,t,t+1\) can occur. For \(s=t\) or \(t+1\), (5.44) and (5.47) bound the dimension of the corresponding part by \(a+1-s\), hence by \(a+1-t\). For \(s=t-1\), equation (5.45) requires \(\delta_\lambda=0\). Outside \(D_{a,s}\) this cuts out a proper projective linear subspace of the extension space \(\mathbb P^s\), of dimension at most \(s-1\). Above \(D_{a,s}\) its dimension is at most \(s\), but (5.48) improves the base bound by one. Both contributions therefore have dimension at most
\[
(a+1-2s)+(s-1)=a-s=a+1-t.
\]
For \(a=1\) the exceptional part is empty, so the same reasoning applies. Since the full inverse image under \(\beta\) is a projective bundle of relative dimension \(t-1\), we obtain
\[
\dim Q_{a+1,t}+(t-1)\le a+1-t.
\tag{5.49}
\]
This proves (5.47) at length \(a+1\).

**A presentation over the parameter space.** We next need a bound from below on every incidence component, not just on the largest one. Let \(A\) be an affine parameter ring and let \(B\) be a finite free rank-\(a\) quotient of \(A[u,v]\). With \(U,V\) its commuting multiplication matrices and \(P=A[u,v]\), there is an exact resolution
\[
0\longrightarrow P^a
 \xrightarrow{\,(-v+V,\ u-U)\,}P^{2a}
 \xrightarrow{\,(u-U,\ v-V)\,}P^a
 \longrightarrow B\longrightarrow0.
\tag{5.50}
\]
To check it over arbitrary \(A\), first divide vector polynomials by the monic operator \(u-U\). The quotient is \(A[v]^a\), and \(u-U\) is injective by its highest \(u\)-coefficient. On that quotient \(v-V\) is likewise injective, with cokernel \(B\). For a relation \((u-U)c+(v-V)d=0\), reduction modulo \(u-U\) gives \(d=(u-U)e\); injectivity then gives \(c=-(v-V)e\). This proves exactness in the middle and also injectivity of the left map.

Locally on \(\operatorname{Spec}A\), include \(1\in B\) in an \(A\)-basis. This is possible because its value in every residue algebra is nonzero. Let \(K\) be the kernel of \(P^a\to B\), and separate the summand \(P\cdot1\) from the other \(a-1\) basis vectors. Projection gives a surjection \(K\to P^{a-1}\), since \(P\cdot1\to B\) is already surjective. Its kernel is the universal ideal \(I=\ker(P\to B)\). The composite \(P^{2a}\to K\to P^{a-1}\) is surjective and splits; let \(E\) be its kernel, a locally free \(P\)-module of rank \(a+1\). Restricting (5.50) gives
\[
0\longrightarrow P^a\longrightarrow E\longrightarrow I
 \longrightarrow0,\qquad \operatorname{rank}E=a+1.
\tag{5.51}
\]
In particular \(\mathbb P(I)\) is locally cut out by \(a\) linear equations in \(\mathbb P(E)\). This construction proves the needed presentation even when the parameter space is singular.

**Excluding all additional components.** Induct on \(a\) that \(Q_a\) is irreducible. The case \(a=1\) is a point. Suppose it is known for \(a\); its dimension is \(a-1\) by Lemma 5.3. On the integral variety
\[
W=Q_a\times\mathbb A^2
\]
take the universal ideal \(I\) and put \(H=\mathbb P_W(I)_{\mathrm{red}}\). The variety \(W\) has dimension \(a+1\). Presentation (5.51) and the height bound show that every component of \(H\) has dimension at least \(a+1\). Away from \(Q_a\times\{0\}\) the ideal is the whole structure sheaf, so \(H\to W\) is an isomorphism there. Above \(Q_{a,s}\times\{0\}\), its fibre is \(\mathbb P^s\), and (5.47) bounds that part by
\[
\dim Q_{a,s}+s\le a+1-s\le a.
\tag{5.52}
\]
Thus no component is contained over the origin. The inverse image of its complement is irreducible and dense, so \(H\) is integral.

The inverse image of the universal finite subscheme is a Cartier divisor on \(H\). Here is the required local verification. If \(I\) is generated by \(f_0,\ldots,f_q\), write \(T_i\) for their images in its symmetric algebra. The relations
\[
f_iT_j=f_jT_i
\]
hold because both sides represent \(f_if_j\in I\) in degree one. On the projective chart \(T_0\ne0\) they give \(f_i=f_0(T_i/T_0)\), so the extended ideal is generated by \(f_0\). Every nonempty such chart meets the dense open where \(I\) is the unit ideal. Therefore \(f_0\) is nonzero in its integral coordinate ring, hence a nonzerodivisor. This proves the Cartier assertion. The support of this divisor is precisely the inverse image of \(Q_a\times\{0\}\); call its reduction \(E_a\). Every component of \(E_a\) has dimension \(a\), by the principal ideal theorem and the height formula.

For \(s\ge2\), (5.52) bounds the corresponding part of \(E_a\) by \(a-1\). In contrast, \(Q_{a,1}\) is a nonempty open subset of the irreducible \(Q_a\): socle dimension is at least one, is upper semicontinuous, and equals one at \(k[u]/(u^a)\). Above it \(E_a\) is a \(\mathbb P^1\)-bundle. That irreducible open has to be dense in every component, since the remaining finitely many strata are too small to contain a component. Hence \(E_a\) is irreducible.

The universal one-dimensional quotient of \(I\) on \(E_a\) constructs (5.43) in families and therefore a morphism \(E_a\to Q_{a+1}\). The resulting quotient is finite flat: it is an extension of the rank-\(a\) family by a line bundle supported at the origin. Every closed point of \(Q_{a+1}\) lies in its image, since its nonzero socle contains a line. The closure of the image is thus all of \(Q_{a+1}\), which is irreducible. This completes the induction.

Finally (5.26) expresses every Hilbert–Chow fibre as a product of the punctual fibres. Products of irreducible varieties over an algebraically closed field are irreducible. One can check this directly on affine charts: write a nonzero element of \(A\otimes_k C\), with \(A,C\) finite-type domains, using a \(k\)-linearly independent list of coefficients in \(C\). Outside a proper closed subset of \(\operatorname{Spec}A\), its specialization is a nonzero function on \(\operatorname{Spec}C\). For two such elements choose a common \(k\)-point of those open subsets, then a \(k\)-point where both specialized functions are nonzero. Their product cannot vanish. Thus \(A\otimes_k C\) is a domain. Nilpotents do not affect the underlying spaces. Theorem 5.5 follows. \(\square\)

The elementary-modification method is developed in Ellingsrud–Lehn, [*Irreducibility of the Punctual Quotient Scheme of a Surface*, Section 1 and Lemma 7](https://arxiv.org/abs/alg-geom/9704016v1), and Ellingsrud–Strømme, [*An intersection number for the punctual Hilbert scheme of a surface*, Section 3](https://arxiv.org/abs/alg-geom/9603015v1). Equations (5.42)–(5.52) give the socle estimate, relative presentation and component argument used here.

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
for dominant coweights. Proposition 6.1 proves stratified semismallness for the orbit and twisted-product strata, using the exact earlier programme geometry. Mirković–Vilonen, Lemma 4.4, gives a free primary account of this estimate. The proof below identifies the fibre with a torus-invariant subset in the first Grassmannian factor and bounds its dimension by contraction and semi-infinite intersections. Since \(\dim\operatorname{Gr}_\alpha=2\langle\rho,\alpha\rangle\) for dominant \(\alpha\), the estimate supplies (6.1). The closure bars in their properness assertion are essential: bounded closed Schubert supports are proper over the target, not individual open orbits.

With field coefficients, Proposition 6.2 constructs the twisted external product of two equivariant perverse sheaves and proves that it is perverse. Applying the preceding proof to (6.2) then proves perversity of convolution, the assertion of their Proposition 4.2. For commutative Noetherian coefficient rings of finite global dimension, Proposition 6.4 takes perverse degree zero before descent. Flatness conditions govern when this truncation can be omitted. Propositions 6.1–6.2 give the bounded endpoint construction, fibre estimate and field-coefficient descent; Propositions 6.3–6.5 give the classical coefficient-ring and flat-cohomology arguments. Proposition 6.6 proves the rational étale version over an algebraically closed field with the coefficient prime invertible. The erratum changes a finite-type step in the later Tannakian argument, not this convolution criterion. The programme's *Convolution and rigidity*, GL-SAT lesson 7, is the corresponding further topic.

The relative \(B_{\mathrm{dR}}^+\) Grassmannian belongs to a divisor-base setting with different geometric hypotheses. Let \(F\) be a nonarchimedean local field of residue characteristic \(p\), let \(G/F\) be reductive, and let the commutative coefficient ring \(\Lambda\) be killed by an integer prime to \(p\). Fargues–Scholze, Proposition VI.8.1, treats bounded complexes on the relative Hecke stack over any small v-stack \(S\to\operatorname{Div}^{d}_{Y}\). It asserts that convolution preserves universal local acyclicity, preserves \({}^pD^{\le0}\), and preserves the relative Satake category, whose objects are universally locally acyclic and remain perverse after derived tensor with every coefficient module. The proof uses fusion, conservative constant-term functors and relative duality over diamonds. Lemma 6.7 and Proposition 6.8 below prove the coefficient-amplitude and dense-locus degree arguments used in that setting; the geometric assertions require their own diamond, local-acyclicity and hyperbolic-localization foundations.

For comparison with the two-point calculation, the general Hilbert–Chow programme for a smooth surface uses strata indexed by partitions \(\nu\) of \(n\). A stratum with \(l(\nu)\) distinct support points has dimension \(2l(\nu)\). Proposition 5.2 and Lemma 5.3 give punctual dimension \(a-1\) at length \(a\), so the product of punctual fibres has dimension
\[
\sum_i(\nu_i-1)=n-l(\nu),
\]
and every such stratum is relevant in source dimension \(2n\). Uniqueness of the top-dimensional component makes its generic top-component local system rank one, with Tate twist \(-(n-l(\nu))\). This derives the dimension and multiplicity calculation from those precise inputs. For a smooth irreducible quasi-projective surface, (5.10) supplies the smooth source of dimension twice the length, and Proposition 5.1 supplies étale product charts at separated supports. The map (5.16) is proper. Corollary 5.4 proves semismallness and the rank-one top-component multiplicity in every length. Theorem 5.5 proves irreducibility of every fibre, including the exclusion of smaller components. Full Satake and the Springer/Hitchin construction discussed by Nadler likewise require their additional geometric results.

### Proposition 6.1. Bounded endpoints and the fibre inequality

Put \(O=\mathbb C[[t]]\), \(F=\mathbb C((t))\), \(K=G(O)\), and write \(O_\alpha\) for the orbit of a dominant coweight and \(Z_\alpha=\overline{O_\alpha}_{\mathrm{red}}\). Fix a maximal torus and positive roots, and let \(\rho\) be their half-sum. The following earlier programme proofs provide the geometric inputs:

- [Loop groups and the affine Grassmannian, Lemma 4.1](course:GL-SAT/GL-SAT-02#4-why-the-sheaf-quotient-gives-the-same-space), constructs formal frames étale locally; its [§7.6](course:GL-SAT/GL-SAT-02#76-closed-finite-stages-with-their-nilpotents-intact) constructs projective bounded stages on the full parameter functor.
- [Orbits and Schubert varieties, Theorem 2.3](course:GL-SAT/GL-SAT-04#2-the-stabilizer-and-the-finite-orbit-directions), computes the smooth finite-jet stabilizer and proves \(d_\alpha:=\dim O_\alpha=2\langle\rho,\alpha\rangle\). Its [Theorem 3.5](course:GL-SAT/GL-SAT-04#3-the-closure-order-for-lattices) proves the closure order, and [§5](course:GL-SAT/GL-SAT-04#5-components-and-small-groups) constructs the additive component invariant \(\kappa:G(F)\to X_*(T)/\mathbb Z\Phi^\vee\).
- For the unipotent radical \(N\), put \(S_\eta=N(F)t^\eta K/K\). [Semi-infinite orbits and weight functors, §7](course:GL-SAT/GL-SAT-05#7-finite-orbit-indices-attraction-and-hyperplane-dimension), proves finite intersection indices and dominant-cocharacter contraction. Its [§8](course:GL-SAT/GL-SAT-05#8-the-downward-dimension-chain) proves the following upper bound:

\[
\dim(S_\eta\cap Z_\alpha)\le\langle\rho,\alpha+\eta\rangle
\tag{6.3}
\]
whenever the intersection is nonempty. This is the upper bound obtained by successive hyperplane sections of a component closure; the stronger equidimensionality theorem is unnecessary here.

Choose a faithful closed representation \(G\hookrightarrow\operatorname{GL}(V)\). For \(X_1=Z_\lambda\) and \(X_2=Z_\mu\), choose lattice bounds \(t^{N_i}V_O\subset L_i\subset t^{-N_i}V_O\). A chain is locally represented by \([g,y]\), with \(gK\in X_1\), \(y\in X_2\), and relation
\[
(g,y)\sim(gh^{-1},hy)\quad(h\in K).
\]
Its endpoints are \(p([g,y])=gK\) and \(m([g,y])=gy\). The second lattice has bound \(M=N_1+N_2\), because
\[
t^{N_2}L_1\subset gL_2\subset t^{-N_2}L_1.
\tag{6.4}
\]
These are inclusions over the parameter ring itself.

Let \(X_M\) be a projective stage containing that bound. On a formal-frame chart \(U\to X_1\), the condition on the second endpoint \(z\) is \(g_U^{-1}z\in X_2\). The inverse frame sends \(X_M\) into a common finite bound \(M+N_1\); hence this is a closed condition on \(U\times X_M\). Two frames differ by an integral loop, which preserves \(X_2\) as a closed subscheme. Their ideals therefore agree on overlaps. [Faithfully flat descent, Theorem 2.5](course:AG-DFG/faithfully-flat-descent#2-recovering-a-module-from-a-cocycle), constructs the ideal as the invariant-module equalizer and proves that its pullback is the prescribed ideal. Its inclusion and multiplication descend by the same theorem on morphisms; faithful flatness preserves injectivity. Applying this on affine charts and gluing the unique ideals constructs
\[
Y=X_1\widetilde\times X_2\ \lhook\joinrel\longrightarrow\
X_1\times X_M.
\tag{6.5}
\]
The endpoint functor is its inverse description: a frame of the first endpoint recovers the relative second endpoint, and a different frame gives exactly the displayed equivalence. Thus (6.5) identifies schemes, including their families over nonreduced rings. In particular \(Y\) is projective and \(m\) is proper.

For completeness, its endpoint image is \(Z_{\lambda+\mu}\). The representations in the proof of the closure order have highest weights \(\chi_i=c_i\omega_i\), \(c_i>0\), and give the lattice bounds
\[
\rho_i(g^{-1})V_{i,O}\subset
t^{-\langle\chi_i,\lambda\rangle}V_{i,O}.
\]
Multiplying two inverse frames adds these bounds. An endpoint of dominant type \(\delta\) therefore has \(\langle\chi_i,\delta\rangle\le\langle\chi_i,\lambda+\mu\rangle\). Additivity of \(\kappa\) puts \(\lambda+\mu-\delta\) in the coroot lattice. Its simple-coroot coefficients are consequently nonnegative, so \(\delta\le\lambda+\mu\). The chain of torus points has endpoint \(t^{\lambda+\mu}\); equivariance and properness put its entire orbit closure in the image. This proves equality of the closed reduced images. The map factors through that reduced target: étale frame charts of \(Y\) are products of reduced complex varieties, so \(Y\) is reduced, and a function vanishing at all its closed points is zero.

The same construction for \(Z_\alpha,Z_\beta\) gives the closure \(Y_{\alpha,\beta}\) of the smooth stratum
\[
T_{\alpha,\beta}=O_\alpha\widetilde\times O_\beta,
\qquad \dim T_{\alpha,\beta}=d_\alpha+d_\beta.
\]
Frame charts prove the dimension formula, density and the closure relation: the boundary consists of pairs with smaller orbit indices. There are only finitely many such pairs in \(Y\), and they admit a filtration by closed unions.

Choose an antidominant coweight \(\nu\) representing a target orbit \(O_{\nu^+}\). Its dimension is \(d_{\nu^+}=-2\langle\rho,\nu\rangle\). By (6.5), the reduced fibre
\[
F_\nu=m^{-1}(t^\nu)\cap Y_{\alpha,\beta}
\]
is a closed \(T\)-stable subset of \(Z_\alpha\). Partition it by the finitely many \(S_\phi\) meeting \(Z_\alpha\). If \(F_\nu\cap S_\phi\ne\varnothing\), contraction by a strictly dominant cocharacter stays in this closed fibre and has limit \(t^\phi\). The second relative endpoint at that fixed point is \(t^{\nu-\phi}\in Z_\beta\). Applying (6.3) to this nonempty intersection gives
\[
0\le\langle\rho,\beta+\nu-\phi\rangle.
\]
Applying it to the first factor gives
\[
\dim(F_\nu\cap S_\phi)
\le\langle\rho,\alpha+\phi\rangle
\le\langle\rho,\alpha+\beta+\nu\rangle.
\tag{6.6}
\]
The maximum over the finite partition is \(\dim F_\nu\). Thus
\[
2\dim F_\nu\le d_\alpha+d_\beta-d_{\nu^+}.
\tag{6.7}
\]
The open source-stratum fibre is a locally closed subset of \(F_\nu\), so satisfies the same bound. Equivariance transports it to every point of the target orbit: the smooth finite-jet orbit map has étale local sections, and acting by a section identifies the inverse image with the product of that chart and its fibre, preserving each source stratum. This proves (6.1) for every orbit pair, including boundary source strata. Only the dimensions of reduced spaces enter (6.6)–(6.7).

### Proposition 6.2. Descent of the twisted product and perversity

Let \(\Lambda\) be a coefficient field and let \(P,Q\) be perverse sheaves on \(X_1,X_2\), with finite-dimensional constructible cohomology and normalized finite-jet equivariance. All sheaf operations in this proposition are on the classical complex spaces.

Choose \(n\ge\max(1,2N_2)\) large enough for the specified equivariance of \(Q\), and put \(J_nG=G(O/t^n)\). Its congruence kernel acts trivially on \(X_2\). Indeed, if \(h\equiv1\bmod t^n\), then
\[
(h-1)L_2\subset t^{n-N_2}V_O\subset t^{N_2}V_O\subset L_2;
\tag{6.8}
\]
apply the same calculation to \(h^{-1}\) to get equality of lattices. The faithful closed representation detects equality in the Grassmannian. Let \(E_n\to X_1\) be the torsor of frames modulo \(t^n\). Its group is smooth of dimension \(e=n\dim G\): successive truncation kernels are the additive spaces \(t^a\mathfrak g/t^{a+1}\mathfrak g\), and the first quotient is \(G\). Formal lifting on affine charts and (6.8) give
\[
Y=E_n\times^{J_nG}X_2,\qquad
q:E_n\times X_2\longrightarrow Y,\qquad
\pi:E_n\times X_2\longrightarrow X_1\times X_2.
\tag{6.9}
\]
Both \(q\) and \(\pi\) are smooth of relative dimension \(e\); the former is the contraction torsor.

We first justify the sheaf input. Over a field, the stalk Künneth formula gives
\[
\mathcal H^k(P\boxtimes Q)=
\bigoplus_{a+b=k}\mathcal H^a(P)\boxtimes\mathcal H^b(Q).
\tag{6.10}
\]
Each summand has support dimension at most \(-a-b=-k\). For the lower bound, integrate first over one projection and then over the other. The base-change and projection maps of [Lesson 1, H.2–H.4](course:GL-PERV/constructible-complexes-on-algebraic-varieties#h-2-derived-fibers-bounds-and-arbitrary-proper-support-base-change) give
\[
R\Gamma_c(U\times V,P\boxtimes Q)
\simeq R\Gamma_c(U,P)\otimes_\Lambda R\Gamma_c(V,Q).
\tag{6.11}
\]
Take the conical neighbourhoods of [Lesson 1, J.4](course:GL-PERV/constructible-complexes-on-algebraic-varieties#j-4-the-general-normal-attaching-and-support-complexes), with their smooth-stratum ball factors. Their compact cohomology is a bounded finite-dimensional complex, and extension between smaller such neighbourhoods identifies the same local support complex. The dualizing complex constructed in Lesson 1, Appendix F, computes sections of \(D\) by the linear dual of compact sections. Dualizing (6.11) and using
\((A\otimes B)^\vee=A^\vee\otimes B^\vee\) for these perfect complexes therefore gives, on a cofinal product-neighbourhood basis,
\[
D(P\boxtimes Q)\simeq DP\boxtimes DQ.
\tag{6.12}
\]
The maps agree under restriction because (6.11) uses the actual proper-support maps and their evaluation pairings. The upper support bound applied to \(DP,DQ\) proves the lower bound for \(P\boxtimes Q\); hence it is perverse.

Smooth normalized pullback, proved in [Lesson 5, Proposition 3.1](course:GL-PERV/affine-morphisms-artin-vanishing-and-perverse-cohomology#3-transport-a-perverse-sheaf-through-a-smooth-map), makes \(F=\pi^*(P\boxtimes Q)[e]\) perverse. Equivariance of \(Q\) gives the contraction descent datum on \(F\): changing the first frame by \(h^{-1}\) changes the second point by \(h\), and its action isomorphism identifies the two pullbacks. The action unit and multiplication law are exactly the identity and cocycle conditions on the torsor relation.

Here is effective descent, including the normalization. Choose local sections \(s_i:U_i\to E_n\times X_2\) of \(q\), after an étale cover of \(Y\), and set \(A_i=s_i^*F[-e]\). The torsor descent isomorphism identifies \(q_i^*A_i[e]\) with \(F|_{q^{-1}U_i}\). Smooth surjective normalized pullback reflects the perverse cuts: it is \(t\)-exact, commutes with perverse cohomology, and is conservative on stalks. Consequently \(A_i\) is perverse. This argument does not assume that pullback by a section is \(t\)-exact. Pulling the descent datum back along \((s_i,s_j)\) gives the transition maps of the \(A_i\), with their triple-overlap cocycle. [Lesson 3, Proposition 4.1](course:GL-PERV/the-perverse-t-structure#4-constructing-objects-from-local-data), constructs the resulting object and its morphisms by the effective perverse-heart equalizer. We obtain a unique perverse sheaf \(A=P\widetilde\boxtimes Q\), with its specified descent identification,
\[
q^*A[e]\simeq\pi^*(P\boxtimes Q)[e].
\tag{6.13}
\]
The shifts on the two sides cancel. In a formal-frame chart \(U\to X_1\), \(A\) is \(P|_U\boxtimes Q\), without an extra shift. Increasing \(n\) gives the identical local objects and frame-transition maps, so effective descent identifies the results, compatibly through any further increase. Smooth duality applied to the two normalized pullbacks in (6.13), together with (6.12), gives
\[
D(P\widetilde\boxtimes Q)\simeq DP\widetilde\boxtimes DQ.
\tag{6.14}
\]

Equivariance makes the cohomology of \(P,Q\) locally constant along their orbits: pull the action isomorphism back by local sections of the smooth orbit map. Their upper perverse bounds and (6.10) therefore put the cohomology of \(A|_{T_{\alpha,\beta}}\) in degrees \(b\le-d_\alpha-d_\beta\). For \(x\in O_\delta\), (6.7) and compact-support dimension give
\[
H_c^j\bigl(m^{-1}(x)\cap T_{\alpha,\beta},
                   A|_{m^{-1}(x)\cap T_{\alpha,\beta}}\bigr)=0
\quad\text{if }j>-d_\delta.
\tag{6.15}
\]
Intersect the finite closed source filtration with the fibre and use compact-support localization. Each step preserves (6.15). The whole fibre is proper, so its compact cohomology equals its ordinary cohomology; proper base change gives the upper perverse bound for \(Rm_*A\). The same proof for \(DP,DQ\), followed by (6.14) and proper duality, gives the lower bound. Therefore
\[
P*Q:=Rm_*(P\widetilde\boxtimes Q)
\quad\text{is perverse.}
\tag{6.16}
\]
This proof uses no semisimplicity or decomposition theorem. It uses the original orbit cohomological bounds throughout; any auxiliary refinement for the sheaf operations retains those bounds as described after (6.1). The field hypothesis in (6.10)–(6.12) is substantive. Propositions 6.3–6.4 give the coefficient-ring version with perverse truncation and an intrinsic flatness criterion. The relative-diamond assertions retain their separately stated tensor-flatness, duality and geometric hypotheses.

### Proposition 6.3. The semismall degree test over a coefficient ring

Let \(R\) be a commutative Noetherian ring of finite global dimension. Use the classical constructible category with finitely generated stalk cohomology. Its middle perverse cuts are defined by
\[
i_T^*A\in D^{\le-\dim_{\mathbb C}T},\qquad
i_T^!A\in D^{\ge-\dim_{\mathbb C}T}
\tag{6.17}
\]
on the smooth strata. These are the cuts obtained by the abstract recollement construction of [Lesson 2, Theorem 2.1](course:GL-PERV/gluing-t-structures#2-construct-a-truncation-from-the-two-pieces), applied successively with the ordinary structure shifted by the complex dimension on each stratum. That construction is independent of self-duality of the coefficient ring.

For a proper map with compatible constructible stratifications as in (6.1), the same inequality implies that \(Rm_*A\) is perverse over \(R\). We give the lower-bound argument without assuming that \(R\)-linear Verdier duality preserves the heart.

The sheaf operations used here are the arbitrary-module constructions in *Duality maps for constructible inverse and direct images*: the [finite exceptional adjoint](course:constructible-duality-and-infinite-twists/duality-maps-for-constructible-inverse-and-direct-images#exceptional-adjoint-complex), [projection formula](course:constructible-duality-and-infinite-twists/duality-maps-for-constructible-inverse-and-direct-images#projection-arbitrary-coefficients) and [pairing transport](course:constructible-duality-and-infinite-twists/duality-maps-for-constructible-inverse-and-direct-images#transport). They apply to bounded complexes, including infinite coefficient modules. Locally closed complex varieties are treated in ambient analytic manifold charts by extension by zero; support localization and exceptional composition identify the intrinsic operations on overlaps. The [local support comparisons](course:sheaf-proof-readings/SH03-constructible-costalks-and-verdier-duality#the-two-local-measurements) identify sufficiently small compact-support neighbourhood complexes with the actual costalks. The [compact-set calculation](course:sheaf-proof-readings/SH03-perfect-coefficients-on-compact-fibres#finite-descent-on-a-compact-triangulation) gives perfect cohomology on compact constructible supports.

The constructible recollement also retains this coefficient scope. The [perfect-operation theorem](course:sheaf-proof-readings/SH03-perfect-operations-and-finite-microlocal-coefficients#perfect-inverse-images-tensors-and-internal-hom) proves closure under tensor and internal Hom. For a subanalytic open inclusion \(j:U\hookrightarrow X\), extend a constructible complex \(C\) by zero. This retains its perfect stalks, and the actual open adjunction gives \(Rj_*C=R\mathcal Hom(R_U,j_!C)\). Thus ordinary open image remains bounded constructible as well. Closed support is computed by \(R\mathcal Hom(R_Z,-)\). These formulas and the two localization triangles supply the functors needed in the finite gluing argument for (6.17).

Set
\[
I=\operatorname{Hom}_{\mathbb Z}(R,\mathbb Q/\mathbb Z),
\qquad
\mathbb D_I B=R\mathcal Hom_R(B,a_X^!I).
\tag{6.18}
\]
The action on \(I\) is \((r\chi)(s)=\chi(rs)\). Evaluation at \(1\), with inverse \(\phi\mapsto[b\mapsto(r\mapsto\phi(rb))]\), identifies
\[
\operatorname{Hom}_R(M,I)
=\operatorname{Hom}_{\mathbb Z}(M,\mathbb Q/\mathbb Z).
\tag{6.19}
\]
This functor is exact and detects nonzero modules. To see both facts, divisibility of \(\mathbb Q/\mathbb Z\) extends a character across one additional group generator: prescribe a value whose required integer multiple is the already prescribed value, or choose any value when there is no such relation. A maximal extension consequently has the whole group as domain. Every nonzero cyclic subgroup has a character nonzero on its generator, and the extension argument extends that character. Thus \(I\) is an injective cogenerator. In particular, for a bounded complex \(C\),
\[
H^qR\operatorname{Hom}_R(C,I)
=\operatorname{Hom}_R(H^{-q}C,I).
\tag{6.20}
\]

The proper-support adjunction with target \(I\) gives, on each open \(U\),
\[
R\Gamma(U,\mathbb D_I B)
\simeq R\operatorname{Hom}_R(R\Gamma_c(U,B),I).
\]
The local support comparisons and exact filtered stalk colimits therefore identify
\[
(\mathbb D_I B)_x
\simeq R\operatorname{Hom}_R(i_x^!B,I).
\tag{6.21}
\]
This calculation applies to constructible \(B\); no biduality with \(I\) is asserted. The exceptional-adjoint bound makes \(a_X^!I\), and hence the local duals in use, bounded. More directly, (6.21) and the finite range of constructible costalks give a uniform bound for their cohomology.

If \(x\in T\) and \(t=\dim_{\mathbb C}T\), the local system \(i_T^!B\) satisfies
\[
i_x^!B\simeq(i_T^!B)_x[-2t].
\]
The shift is the compact-support degree of an oriented real \(2t\)-ball. Combining this with (6.20)–(6.21) gives
\[
H^q(\mathbb D_I B)_x
=\operatorname{Hom}_R\!\left(H^{-q-2t}(i_T^!B)_x,I\right).
\tag{6.22}
\]
Consequently the lower inequality in (6.17) is equivalent to the upper stalk bound \(H^q(\mathbb D_I B)|_T=0\) for \(q>-t\). This dual may have infinite stalk modules, which is why its operation bounds must allow them.

Those modules cause no change in the compact-support estimate. The [uniform manifold bound](course:constructible-duality-and-infinite-twists/duality-maps-for-constructible-inverse-and-direct-images#uniform-manifold-dimension) proves \(H_c^a(V,L)=0\) for \(a>\dim_{\mathbb R}V\) for every sheaf of \(R\)-modules on a manifold. Stratify a complex algebraic set of dimension at most \(r\) into finitely many smooth pieces and use compact-support localization. It gives the bound \(a\le2r\) for every coefficient sheaf on that set, without finite generation.

Apply the compact-support argument preceding (6.2) first to \(A\), using its upper inequalities, and then to \(\mathbb D_I A\), using (6.22). On a source-stratum fibre the latter has cohomology only in degrees \(b\le-t\), so (6.1) bounds the total degrees by \(-s\), where \(s\) is the target-stratum dimension. The finite closed filtration and proper base change give the upper bound for both \(Rm_*A\) and \(Rm_*\mathbb D_I A\).

Finally, the pairing-transport proof applies with \(a_W^!I\) as its dualizing target. Indeed, for a bounded test object \(C\) on \(W\), its successive adjunctions are
\[
\begin{aligned}
\operatorname{Hom}(C,Rm_*\mathbb D_I A)
&=\operatorname{Hom}(m^*C\otimes^L A,a_Z^!I)\\
&=\operatorname{Hom}(Rm_!(m^*C\otimes^L A),a_W^!I)\\
&=\operatorname{Hom}(C\otimes^L Rm_!A,a_W^!I).
\end{aligned}
\]
Projection and exceptional composition identify the indicated maps. Currying and Yoneda prove
\[
Rm_*\mathbb D_I A\simeq\mathbb D_I Rm_!A
=\mathbb D_I Rm_*A,
\tag{6.23}
\]
the last equality using properness. Formula (6.22) for the constructible output now turns its dual upper bound into the lower inequality in (6.17). Together with its already proved upper bound, this proves the assertion.

### Proposition 6.4. Convolution in the perverse heart over \(R\)

For finite-support equivariant \(R\)-perverse sheaves \(P,Q\), form
\[
B={}^{p}H^0(P\boxtimes_R^L Q).
\tag{6.24}
\]
Descend \(B\) along the bounded finite-frame correspondence (6.9), with the two equal smooth normalizations, and denote the descended perverse sheaf by \(\widetilde B\). Then
\[
P*_R Q:=Rm_*\widetilde B
\quad\text{is perverse.}
\tag{6.25}
\]

Here are the coefficient and descent details. Noetherianness and finite global dimension make a bounded complex with finitely generated cohomology a perfect coefficient complex: resolve each cohomology module by finitely generated free modules and stop at the global-dimension bound, where the final syzygy is projective; its finite Postnikov filtration assembles these resolutions. Thus the stalk tensor complexes are bounded with finitely generated cohomology. Product charts preserve constructibility, so (6.24) belongs to the constructible category on the product.

Smooth pullback shifted by its complex relative dimension is \(t\)-exact over \(R\). The upper support calculation is the one in Proposition 3.1 of Lesson 5. For the lower calculation use local product coordinates: an oriented real \(2e\)-ball has compact coefficient complex \(R[-2e]\), a free rank-one complex. The normalized pullback therefore increases point-costalk degrees and stratum dimensions by the same \(e\), preserving the lower test (6.17). Surjectivity makes normalized pullback conservative, so it also reflects both cuts. This argument uses the ball orientation, not self-duality of the \(R\)-perverse heart.

The normalized action pullbacks consequently commute with perverse cohomology. The action on \(P\boxtimes_R^L Q\) induces the action datum on \(B\), preserving its unit and cocycle. On sections of \(q\), pull back \(\pi^*B[e]\) and shift back by \([-e]\). Conservativity proves perversity of those local objects exactly as in (6.13). Their descent is effective over \(R\): for two open sets \(U,V\), with overlap isomorphism \(\alpha\), take the cone of
\[
j_{U\cap V,!}B_U|_{U\cap V}
\xrightarrow{(u,-v\alpha)}
j_{U!}B_U\oplus j_{V!}B_V.
\tag{6.26}
\]
On either open, the overlap summand cancels by a triangular automorphism, leaving its prescribed object; on the intersection the two resulting markings differ by precisely \(\alpha\). Degree-zero morphisms in the perverse heart glue uniquely, so successive two-open constructions realize the cocycle on a finite cover. This is the explicit finite descent proof in [Perverse descent and fibre dimension bounds](course:sheaf-proof-readings/SH03-perverse-descent-and-fibre-dimension-bounds#glue-two-objects-by-an-actual-overlap-map). Compactness of \(Y\) gives a finite cover by local sections. The descended objects are constructible for the one finite twisted-orbit stratification, which supplies their global constructibility. Increasing the frame level retains the same objects and transitions.

The smooth orbit maps and their local sections make the direct image locally constant along each target orbit. Its stalk is the cohomology of the compact fibre with constructible coefficients; the compact-set calculation cited above makes that complex perfect. Thus it is a bounded constructible complex. Proposition 6.1 gives (6.1) for all boundary strata, and Proposition 6.3 proves (6.25).

The truncation in (6.24) matters even on a point. With \(R=\mathbb Z\) and \(P=Q=\mathbb Z/n\), \(n>1\), the free resolution \([\mathbb Z\xrightarrow{n}\mathbb Z]\), in degrees \(-1,0\), gives
\[
P\otimes_{\mathbb Z}^L Q
\simeq[\mathbb Z/n\xrightarrow{0}\mathbb Z/n].
\tag{6.27}
\]
Both degrees \(-1\) and \(0\) have nonzero cohomology; only the degree-zero part lies in the point heart. This is also the convolution at the identity of any group. Tensoring \(0\to\mathbb Z\xrightarrow{n}\mathbb Z\to\mathbb Z/n\to0\) with that point object shows that the heart operation need not be exact in a variable.

There is an intrinsic sufficient condition for omitting the truncation. Say that \(Q\) is *perversely flat over \(R\)* if \(Q\otimes_R^L M\) is perverse for every finitely generated \(R\)-module \(M\) in degree zero. Then \(P\boxtimes_R^L Q\) is perverse for every \(P\) in the heart.

To prove this, put \(C_x(P)=i_x^!P\). The compact-support projection and product maps, on the stabilized small neighbourhoods, give the actual comparisons
\[
\begin{aligned}
C_y(Q\otimes_R^L M)&\simeq C_y(Q)\otimes_R^L M,\\
C_{(x,y)}(P\boxtimes_R^L Q)&\simeq
C_x(P)\otimes_R^L C_y(Q).
\end{aligned}
\tag{6.28}
\]
If \(y\) lies on a stratum of complex dimension \(s\), perverse flatness makes the first line lie in \(D^{\ge s}\). If \(x\) lies on a stratum of dimension \(r\), \(C_x(P)\in D^{\ge r}\), with finitely generated cohomology. Apply its finite Postnikov filtration: the term \(H^a(C_x(P))[-a]\), \(a\ge r\), tensored with \(C_y(Q)\) lies in \(D^{\ge s+a}\). Extensions preserve that bound. The second line is therefore in \(D^{\ge r+s}\), the lower perverse test on the product. The upper test holds without flatness: derived tensor of bounded-above complexes has no cohomology above the sum of their upper degrees. This proves the sufficient condition. The same proof applies when \(P\) is perversely flat.

Over a field this condition is automatic and recovers Proposition 6.2. Proposition 6.5 proves that flat total cohomology implies perverse flatness, using the ring-valued semi-infinite weight functors. The assertions over relative diamonds retain the universal-local-acyclicity and flatness conditions specified above.

### 6.5. Weight detection and flat total cohomology

Retain the classical complex Grassmannian and the commutative Noetherian ring \(R\) of finite global dimension from Proposition 6.4. All objects have bounded, finitely generated constructible cohomology and finite Schubert support. Put
\[
h_\nu=\langle2\rho,\nu\rangle,\qquad
W_\nu(A)=R\Gamma_c(S_\nu,A)[h_\nu],\qquad
F_\nu(P)=H^0W_\nu(P).
\tag{6.29}
\]
Here \(S_\nu\) and \(T_\nu\) are the attracting and repelling semi-infinite orbits for the dominant cocharacter used in [Semi-infinite orbits, Sections 7–11](course:GL-SAT/GL-SAT-05#7-finite-orbit-indices-attraction-and-hyperplane-dimension). On each finite stage these are locally closed subsets, and only finitely many meet the stage. The notation \(R\Gamma_{T_\nu}(Y,A)\) below means \(R\Gamma(T_\nu\cap Y,p^{-!}A)\) for its locally closed inclusion \(p^-\).

**Proposition 6.5.** On the spherical perverse heart, each \(W_\nu\) is concentrated in degree zero and \(F_\nu\) is exact. The \(F_\nu\) jointly detect zero objects, and there is a natural graded decomposition
\[
H^*(Y,P)=\bigoplus_\nu F_\nu(P),
\qquad F_\nu(P)\text{ in degree }h_\nu .
\tag{6.30}
\]
For a bounded spherical complex \(A\),
\[
A\text{ is perverse}\quad\Longleftrightarrow\quad
H^jW_\nu(A)=0\quad\text{for all }\nu\text{ and }j\ne0.
\tag{6.31}
\]
If \(H^*(Y,Q)\) is flat over \(R\), then \(Q\) is perversely flat in the sense of (6.27). In particular, if either factor has flat total cohomology, its derived external product with the other factor is perverse, and (6.25) can be formed without taking perverse degree zero.

**Hyperbolic restriction with these coefficients.** We first establish the coefficient scope of the comparison used in the proof:
\[
R\Gamma_{T_\nu}(Y,A)\ \xrightarrow{\ \sim\ }\
R\Gamma_c(S_\nu\cap Y,A).
\tag{6.32}
\]
The finite projective embedding and the attractor coordinate descriptions are those of [Semi-infinite orbits, Sections 11–16](course:GL-SAT/GL-SAT-05#11-classical-sheaf-operations-and-finite-stage-attractors). The sheaf argument there is stated for a field. The following proof gives the ring-valued version for the naively equivariant objects needed here.

The operations in Proposition 6.3 apply over \(R\). In addition, the actual evaluation isomorphism \(A\simeq D_RD_RA\) and the two dual exchanges hold for these constructible complexes: finite global dimension makes their finitely generated stalks perfect; the [perfect-costalk and evaluation proofs](course:sheaf-proof-readings/SH03-constructible-costalks-and-verdier-duality#the-evaluation-map-is-biduality) and [perfect-operation comparisons](course:sheaf-proof-readings/SH03-perfect-operations-and-finite-microlocal-coefficients#perfect-inverse-images-tensors-and-internal-hom) give the stated maps. A singular variety is treated as a closed subset of a smooth local ambient variety, using closed proper image and its supported exceptional inverse. This use of \(D_R\) makes no assertion that it preserves the perverse heart.

We need ordinary product comparison only for a contractible manifold \(D\). Projection \(\pi:D\times X\to X\) satisfies \(R\pi_*\pi^*B=B\) for every bounded complex of sheaves of \(R\)-modules. Here is the module argument. Sections of \(\pi^*M\) on \(V\times U\), with \(V\) connected, are sections of \(M\) on \(U\): restrict to a fixed slice; fibrewise constancy proves equality on every stalk. This also shows that \(\pi^*\) preserves products, by a basis of such product opens. Embed \(M\) in its germ sheaf \(T(M)=\prod_x(i_x)_*M_x\). On \(D\times X\) its pullback has the product of the flabby constant-cochain resolutions on the closed fibres. On coordinate balls these are resolutions by the ordinary prism contraction; products of exact sequences of modules are exact, since coordinatewise surjections are surjective. On the whole fibre their cohomology is \(M_x\) in degree zero and zero above. Thus \(R^i\pi_*\pi^*T(M)=0\) for \(i>0\). The sequence \(0\to M\to T(M)\to T(M)/M\to0\), the degree-zero section identity, and dimension shifting prove the same vanishing for every \(M\). Finite ordinary truncation towers give the bounded-complex assertion. Applying it on product opens gives the actual ordinary comparison for \(1_D\times f\), for every map \(f\) occurring here.

For \(q:\mathbb C\times X\to X\), \(j:\mathbb C^*\times X\hookrightarrow\mathbb C\times X\) and the zero section \(z\), the two-slit cover of \(\mathbb C^*\) gives the complex \([B\xrightarrow{0}B]\) in degrees zero and one, both on the whole punctured line and on a punctured disc. Restriction is its identity. The boundary triangle therefore proves
\[
Rq_*j_!q^*B=0,\qquad
Rq_*K\xrightarrow{\sim}z^*K
\quad\text{if }j^*K\simeq j^*q^*B.
\tag{6.33}
\]
In the first term \(q^*B\) is restricted to the open domain of \(j\). The calculation uses the contractible slit products just proved. Consequently an endomorphism of \(q^*B\) that is zero at zero and invertible at one forces \(B=0\): its direct image, identified with \(B\) by restriction at either section, is simultaneously zero and invertible.

For clarity, the contraction argument can now be carried out with the ring unchanged. Let \(E,H\) be weight bundles over a fixed base \(X\), all weights of \(E\) greater than those of \(H\). Set
\[
V=\mathbb P(E\oplus H)\setminus\mathbb P(E),\qquad
Z=\mathbb P(H),\qquad f:V\to X.
\]
For equivariant \(K\), write \(K_U=\sigma_!\sigma^*K\), where \(U=V\setminus Z\). Close the action graph in \(\mathbb C\times V\times\mathbb P(E\oplus H)\). Its projections \(r_1,r_2\) to \(\mathbb C\times V\) satisfy \(fr_1=fr_2\); \(r_1\) is proper. In weight coordinates, \(y_jz_i=t^{a_i-b_j}y_i z_j\), with \(a_i>b_j\), forces the second point at \(t=0\) into \(Z\). Thus the graph lies in \(\mathbb C\times V\times V\), and \(r_2^{-1}(\mathbb C\times U)=\mathbb C^*\times U\).

Put \(C=Rf_*K_U\), \(Q=1_{\mathbb C}\times f\) and \(p:\mathbb C\times V\to V\). Proper-support base change for \(r_1\), equivariance on the punctured graph and composition give
\[
D=RQ_*Rr_{2*}r_2^*p^*K_U
\simeq RQ_*j_!p^*K_U .
\tag{6.34}
\]
On \(\mathbb C^*\times X\) this is \(q^*C\). Pushing (6.34) to \(X\) and using (6.33) over \(V\) gives \(Rq_*D=0\); the second assertion of (6.33) gives \(z^*D=0\). The unit for \(r_2^*\dashv Rr_{2*}\), followed by the extension-by-zero map, is therefore
\[
q^*C\longrightarrow D=j_!j^*q^*C\longrightarrow q^*C.
\]
It is invertible at one and zero at zero. Hence \(C=0\). Localization and then constructible duality prove the two natural contraction maps
\[
Rf_*K\xrightarrow{\sim}R(f|_Z)_*i^*K,\qquad
R(f|_Z)_!i^!K\xrightarrow{\sim}Rf_!K .
\tag{6.35}
\]
Equivariance is preserved by duality: the action and projection are smooth of the same complex relative dimension one, so their common orientation shift cancels. It is preserved by ordinary image through the product comparison, and by proper-support image through base change. These observations justify every equivariant complex in this argument.

Here is how contraction gives the specified hyperbolic map. For fixed, attracting and repelling spaces, use \(i^\pm:X^0\to X^\pm\), \(p^\pm:X^\pm\to X\), \(q^\pm:X^\pm\to X^0\). The unit into \(Rp^+_*p^{+*}\), extraordinary/ordinary base-change exchange on \(X^+\times_X X^-\), and projection onto its open-and-closed diagonal fixed summand give
\[
i^{-*}p^{-!}A\longrightarrow i^{+!}p^{+*}A.
\tag{6.36}
\]
The restriction \(Rq^-_*\to i^{-*}\) and counit \(i^{+!}\to Rq^+_!\) complete the map \(L^-\to L^+\). For a weight vector space \(E_+\oplus E_-\oplus E_0\), regard \(E_0\) as base. Formula (6.35) identifies both outside maps with isomorphisms. The cone of (6.36) is controlled by \(A_0=j_!j^*A\), where \(j\) is the complement of \(E_+\oplus E_0\). Embed the vector space into
\(\mathbb P(E_+\oplus E_-\oplus\mathcal O)\setminus\mathbb P(E_-)\), and extend \(A_0\) by zero from the chart of the last coordinate. Apply the localization triangle for the closed repeller. Its middle term has zero ordinary image by (6.35) for the inverse action, contracting to \(\mathbb P(E_+\oplus\mathcal O)\), where the restriction is zero. Its open-complement term has zero image by the same formula, now contracting to \(\mathbb P(E_+)\), outside that chart. Its first term is \(L^-A_0\), so this too vanishes. If a positive or negative summand is zero, (6.35) alone gives the comparison.

For an equivariant closed affine embedding into a weight vector space, homogeneous coordinate ideals identify the attracting, repelling and fixed schemes by closed base change. That base change carries (6.36), including its unit and counit, to the vector-space map. Closed direct image is conservative. Finally, eigen-coordinate affine charts of a projective weight embedding cover the fixed locus. An orbit with limit in an invariant open lies wholly in that open: otherwise its orbit closure lies in the invariant closed complement. Thus the attracting and repelling spaces over that fixed open are exactly those of the open chart. Ordinary image restricts to target opens, and proper-support and exceptional operations have their local comparison maps. The affine isomorphisms therefore prove the projective one. On the finite Grassmannian stage its fixed component is the point \(t^\nu\), which gives (6.32).

**The two degree bounds.** Let \(O_\lambda\) have complex dimension \(d_\lambda=\langle2\rho,\lambda\rangle\). Equivariance makes both \(i_{O_\lambda}^*P\) and \(i_{O_\lambda}^!P\) locally constant complexes on the orbit, by local sections of its smooth finite-jet orbit map. The perverse inequalities are
\[
i_{O_\lambda}^*P\in D^{\le-d_\lambda},\qquad
i_{O_\lambda}^!P\in D^{\ge-d_\lambda}.
\tag{6.37}
\]
The semi-infinite dimension bounds and the arbitrary-module compact dimension bound in Proposition 6.3 give
\[
H^a_c(S_\nu\cap O_\lambda,i_{O_\lambda}^*P)=0
\quad(a>h_\nu).
\tag{6.38}
\]
Indeed each ordinary cohomology term of degree \(b\le-d_\lambda\) contributes at most \(2\dim(S_\nu\cap O_\lambda)+b\le h_\nu\). A finite orbit filtration gives the upper bound on \(S_\nu\cap Y\).

For the lower bound, refine each \(T_\nu\cap O_\lambda\) into smooth locally closed pieces \(B\) of dimension \(e\le(d_\lambda-h_\nu)/2\), with a finite closed-open filtration. If \(u:B\to O_\lambda\), normal complex coordinates give, for a locally constant coefficient complex \(L\),
\[
u^!L\simeq u^*L[-2(d_\lambda-e)].
\tag{6.39}
\]
Locally this is the relative cochain complex of a normal ball and its puncture. The prism contraction and the sphere cell calculation leave one free \(R\)-generator in degree \(2(d_\lambda-e)\); complex orientation glues that generator. The same free relative complex works for every module, and finite ordinary truncation towers give (6.39) for \(L\). No flatness of its cohomology is needed. Applying (6.39) to the second complex in (6.37) yields
\[
(i_B)^!P\in D^{\ge d_\lambda-2e}\subset D^{\ge h_\nu}.
\tag{6.40}
\]
Ordinary derived sections preserve a lower degree bound. In the closed-open localization triangle for \(p^{-!}P\), the closed term is exceptional restriction and the open term is ordinary restriction, which equals exceptional restriction for that open immersion. Induction over the chosen finite filtration therefore puts \(R\Gamma_{T_\nu}(Y,P)\) in \(D^{\ge h_\nu}\). Formula (6.32) and (6.38) prove concentration. Compact constructible finiteness gives finitely generated weight modules, and the adjacent vanishing groups in the long exact sequence prove exactness of \(F_\nu\).

**Splitting and detection.** Work in one component class. All its heights have the same parity, since the height of a simple coroot is two. Let \(Y_{\le h}\) be the union of attracting slices of height at most \(h\). The semi-infinite closure order makes this a closed subset; different slices of height \(h\) are open and closed in their union \(Y_h\). Put \(U_{\ge h}=Y\setminus Y_{<h}\). Concentration and finite closed-open induction show that \(U_{>h}\) has no compact cohomology in degrees \(h,h+1\), and \(Y_{<h}\) has none in degrees \(h-1,h\). The actual localization maps thus give
\[
\bigoplus_{h_\nu=h}F_\nu(P)
=H_c^h(Y_h,P)
\ \xleftarrow{\ \sim\ }\ H_c^h(U_{\ge h},P)
\ \xrightarrow{\ \sim\ }\ H^h(Y,P).
\tag{6.41}
\]
The right arrow is extension by zero, using properness of \(Y\). This constructs (6.30) naturally, over \(R\), rather than inferring a splitting from ranks.

If \(P\ne0\), choose a dominant index \(\lambda\) maximal among the orbits in its support. The support is a union of their closures. The opposite-orbit geometry says \(T_\lambda\cap O_\mu\ne\varnothing\) only if \(\lambda\le\mu\); hence its intersection with this support is the single point \(t^\lambda\) in the open orbit \(O_\lambda\). One can also see the last assertion from the zero-dimensional slice bound and contraction: a finite reduced set contracted to a point has only that point. Locally \(P=L[d_\lambda]\) on this orbit, with \(L\ne0\). Its point costalk is \(L_{t^\lambda}[-d_\lambda]\), so (6.32) gives \(F_\lambda(P)=L_{t^\lambda}\ne0\). This proves joint detection.

Perverse truncations remain spherical: smooth normalized action pullback and projection pullback are t-exact, so their equivariance isomorphism and its cocycle pass to the truncations. The perverse t-structure is bounded on this finite stage. Its finite truncation triangles, together with concentration on every heart object, give the natural identities
\[
H^jW_\nu(A)=F_\nu({}^pH^jA).
\tag{6.42}
\]
To justify that no differential is being suppressed, apply \(W_\nu\) to the bounded perverse Postnikov tower: a term \({}^pH^jA[-j]\) has image in degree \(j\) only. The triangle at each truncation identifies the cohomology in that degree, and the lower truncation has no cohomology above \(j-1\). This proves (6.42) by induction. Joint detection now proves (6.31).

**Flat coefficients and the tensor product.** If \(H^*(Y,Q)\) is flat, (6.30) makes every \(F_\nu(Q)\) a flat direct summand. For any finitely generated \(R\)-module \(M\), the actual compact-support projection formula gives
\[
W_\nu(Q\otimes_R^L M)
\simeq W_\nu(Q)\otimes_R^L M
\simeq F_\nu(Q)\otimes_R M[0].
\tag{6.43}
\]
Here \(M[0]\) is the degree-zero constant coefficient complex; finite global dimension ensures boundedness. Criterion (6.31) makes \(Q\otimes_R^L M\) perverse. This is precisely (6.27), so Proposition 6.4 proves the assertion about convolution. Equivalently, apply the same weight criterion to \(G\times G\). Compact Künneth identifies the weight complex of \(P\boxtimes_R^LQ\) with \(F_\nu(P)\otimes_R^L F_\eta(Q)\) in normalized degree zero; one flat factor removes the negative Tor degrees. The example (6.26) shows why a flatness hypothesis cannot simply be dropped. All constructions above concern the classical complex Grassmannian with the stated coefficient ring.

### 6.6. Rational étale convolution over an algebraically closed field

Let \(k\) be algebraically closed, let \(G/k\) be connected reductive, and let \(\ell\ne\operatorname{char}k\). Fix a finite extension \(E/\mathbb Q_\ell\), with valuation ring \(O\) and uniformizer \(\varpi\). Here \(D_c^b(X,E)\) is the actual rational constructible category obtained from derived-complete \(O\)-coefficients and coefficient localization. All supports are finite unions of closed Schubert varieties in the equal-characteristic Grassmannian \(G(k((t)))/G(k[[t]])\). A spherical object carries a genuine action through a finite jet quotient: its action isomorphism has an identity and a multiplication cocycle. The [rational Satake heart, Theorem B.2.3.1](course:GL-SAT/GL-SAT-06#b23-the-finite-support-category-and-its-composition-series), proves that these objects form an abelian category, with stage-independent morphisms.

**Proposition 6.6.** For spherical perverse \(P,Q\) supported on \(X_1,X_2\), the finite frame correspondence gives a unique twisted perverse object \(A=P\widetilde\boxtimes Q\), characterized by
\[
q^*A[h_n]\simeq\pi^*(P\boxtimes_E^LQ)[h_n],
\qquad h_n=\dim J_nG,\qquad
P*Q=Rm_*A.
\tag{6.44}
\]
Convolution is spherical, perverse and exact in each variable. The construction is independent of the finite frame level and closed support stage. With structural duality and its actual evaluation maps, it has natural isomorphisms
\[
D(P*Q)\simeq DP*DQ,\qquad
E_{\{1\}}*P\simeq P\simeq P*E_{\{1\}},\qquad
(P*Q)*R\simeq P*(Q*R).
\tag{6.45}
\]
The associator satisfies the pentagon and the unit triangles. The raw intersection complex of the largest orbit occurs with multiplicity one as a composition factor of
\(IC_\alpha^{\mathrm{raw}}*IC_\beta^{\mathrm{raw}}\), at index \(\alpha+\beta\). This last assertion concerns composition factors.

**Coefficient operations.** We use the actual maps proved in [Semi-infinite orbits, O.4](course:GL-SAT/GL-SAT-05#o4-actual-proper-comparison-proper-support-and-projection) for proper base change, proper support and projection, and [P.3](course:GL-SAT/GL-SAT-05#p3-structural-duality-with-the-actual-evaluation) for biduality and the dual exchanges. Their coefficient construction is as follows. Ordinary image and scalar pullback have specified finite reductions. The cone of the proper comparison is complete; its first reduction is the finite proper base-change map and is zero. Derived completeness then kills this cone. Proper support is proper image after open extension on a compactification, with common-refinement comparisons. Projection is the transpose of the image counit tensored with the coefficient factor. It is an isomorphism first for locally perfect factors, then for their locally closed extensions, and then by the finite constructibility filtration. Actual rationalization preserves these specified maps and their composition diagrams.

Likewise \(D_XK=R\mathcal Hom(K,a_X^!E)\). Integral double evaluation reduces to finite-field structural double evaluation. Its complete cone vanishes, and rational localization gives the actual rational evaluation isomorphism. The proper dual exchanges are obtained by transposing evaluation through proper-support projection and exceptional adjunction; their composites use the composed counit. These facts permit duality on singular Schubert supports. They do not require an equivariant integral lattice for every rational action object: the action maps below are constructed and descended in the rational category.

The external-duality map is the one proved in [Convolution and rigidity, Theorem A.3.2.1](course:GL-SAT/GL-SAT-07#a32-generic-induction-proves-the-external-evaluation-isomorphism):
\[
D_XP\boxtimes D_YQ\xrightarrow{\sim}D_{X\times Y}(P\boxtimes Q).
\tag{6.46}
\]
Its evaluation first moves the second dual factor past the first original factor, contributing \((-1)^{|\psi||v|}\), then evaluates each pair. The product structural trace is the transpose of the two traces under compact Künneth. The cited proof establishes invertibility by coordinate-generic dimension induction, retaining the even orientation line \(E(1)[2]\). On proper factors the cone is forced onto finitely many closed points; only then does proper cohomology detect it, through finite-dimensional coefficient duality. Open compactification gives the general case with the same evaluation map. Thus the map in (6.46) is specified, including its sign and trace.

We also need the compact dimension bound for these coefficients. Refine the finite constructibility stratification so that on each smooth piece \(Z\) the rational sheaf has a lisse lattice \(M\). Its actual compact complex is
\[
R\Gamma_c(Z,M)=R\varprojlim_aR\Gamma_c(Z,M/\varpi^a).
\tag{6.47}
\]
The finite-level groups are finite and vanish above \(2\dim Z\). Their inverse systems are Mittag–Leffler, because the images in each finite group stabilize. In the product/cone model of (6.47) this kills the \(\varprojlim^1\) term, so the same upper bound holds integrally and after localization. Finite closed-open and ordinary cohomology filtrations yield
\[
K\in D^{\le b}_c(Z,E)
\quad\Longrightarrow\quad
R\Gamma_c(Z,K)\in D^{\le 2\dim Z+b}.
\tag{6.48}
\]
The lattice, transition and compactification details are proved in [Semi-infinite orbits, Lemma Q.4.1.1](course:GL-SAT/GL-SAT-05#q41-the-compact-dimension-bound-after-rationalization). This includes arbitrary rational constructible cohomology sheaves, not only constant coefficients.

**External product and normalized descent.** Actual rational pullback is ordinarily t-exact on constructible complexes. To see the coefficient issue, a lisse rational sheaf is locally free over the completed rational coefficient sheaf. Pullback of a locally closed extension of such a sheaf is its corresponding extension on the inverse image. A finite constructibility filtration then proves ordinary t-exactness for every constructible sheaf. The same argument, with supported tensor, shows that the derived tensor of two rational constructible sheaves has no nonzero Tor degree. Consequently the ordinary cohomology of \(P\boxtimes Q\) is the finite direct sum of products of their cohomology sheaves. Product supports have additive dimensions. The upper perverse bounds for \(P,Q\) therefore give the upper bound for their external product; (6.46) and the same calculation for \(DP,DQ\) give its lower bound. Its exactness in either heart variable follows from the heart long exact sequence. This is the coefficient calculation of [Theorem A.4.1.1](course:GL-SAT/GL-SAT-07#a41-field-tensor-and-external-perversity).

For a smooth surjective torsor \(q:T\to Y\) of relative dimension \(h\), normalized pullback \(q^*[h]\) is t-exact and conservative. The upper assertion follows from ordinary t-exactness and addition of \(h\) to support dimensions; smooth duality gives the lower assertion, with orientation \(E(h)[2h]\). Conservativity follows by lifting geometric stalks. A genuine equivariant perverse object \(B\) on \(T\) therefore descends on an étale section chart \(\sigma_i:U_i\to T\) to
\[
A_i=\sigma_i^*B[-h],\qquad B|_{T_{U_i}}\simeq q_i^*A_i[h].
\tag{6.49}
\]
The second identity and conservativity prove that \(A_i\) is perverse. For sections related by \(\sigma_j=\sigma_i g_{ij}\), the action provides the overlap map; its cocycle gives the triple-overlap identity. These heart objects and morphisms descend by the perverse étale equalizer. The complete proof, including the section inverse on morphisms, is [Theorem A.1.2.1](course:GL-SAT/GL-SAT-07#a12-a-smooth-connected-torsor-descends-perverse-action-objects). Its connected-parameter Hom argument first treats proper support using negative perverse Hom vanishing, then uses intermediate extension for a nonproper base; it does not require vanishing of higher cohomology of the acting group.

Apply this to the finite frame space \(E_n\times X_2\), with right action
\((e,y)h=(eh,h^{-1}y)\). The two maps \(q,\pi\) have the same smooth relative dimension \(h_n\). The genuine action of \(Q\) supplies the right-action cocycle on \(\pi^*(P\boxtimes Q)[h_n]\). Formula (6.49) proves (6.44). On a frame chart the two shifts cancel, giving \(P|_U\boxtimes Q\). Raising \(n\) truncates the same frame transitions to the original action, so the descended objects and maps agree uniquely. Closed support enlargement gives their closed extensions by proper closed base change.

Duality retains that cancellation:
\[
\begin{aligned}
D(q^*A[h_n])&=q^*D_YA(h_n)[h_n],\\
D(\pi^*(P\boxtimes Q)[h_n])
&=\pi^*D(P\boxtimes Q)(h_n)[h_n].
\end{aligned}
\tag{6.50}
\]
Cancel the common Tate line and use (6.46). Normalized torsor descent gives
\(D_YA=DP\widetilde\boxtimes DQ\), with its evaluation comparison. In particular there is no residual group-dimension shift or Tate twist in the twisted product.

**The proper image.** The bounded endpoint immersion is defined over every parameter algebra, using the closed relative-position ideals on formal frame charts and faithfully flat ideal descent. Its projective target makes \(m\) proper. The all-field geometry of [Lemma A.5.1.1](course:GL-SAT/GL-SAT-07#a51-endpoint-image-and-the-bound-on-every-source-stratum) gives, on every twisted orbit stratum \(T_{\alpha,\beta}\) and target orbit \(O_\delta\),
\[
\dim T_{\alpha,\beta}=d_\alpha+d_\beta,\qquad
2\dim\bigl(m^{-1}(x)\cap T_{\alpha,\beta}\bigr)
\le d_\alpha+d_\beta-d_\delta.
\tag{6.51}
\]
This is the algebraic contraction argument of Proposition 6.1: at antidominant endpoint \(\nu=w_0\delta\), the fibre is a closed torus-stable subset of \(Z_\alpha\). If its slice of index \(\phi\) is nonempty, contraction places \(t^\phi\) in that fibre, so \(t^{\nu-\phi}\in Z_\beta\). The semi-infinite dimension bounds give
\(\dim(F_\nu\cap S_\phi)\le\langle\rho,\alpha+\phi\rangle\le\langle\rho,\alpha+\beta+\nu\rangle\).
The finite partition proves (6.51), including all boundary strata, in every characteristic of \(k\).

On \(T_{\alpha,\beta}\), the cohomology of \(A\) is lisse and vanishes in degrees above \(-d_\alpha-d_\beta\), by the normalized frame description. For a geometric \(x\in O_\delta\), (6.48) and (6.51) imply
\[
R\Gamma_c(m^{-1}(x)\cap T_{\alpha,\beta},A)
\in D^{\le-d_\delta}.
\tag{6.52}
\]
Compact localization combines the finite closed source filtration. The whole fibre is proper, so its compact cohomology is its ordinary cohomology; proper base change identifies this with \((Rm_*A)_x\).

The output has a genuine finite-jet action. For first-support bound \(N_1\), conjugation by a first frame loses at most \(2N_1\) congruence orders. A left jet level at least \(\max(n+2N_1,2(N_1+N_2))\), enlarged to include the action level of \(P\), acts on the entire bounded correspondence. Its left frame action commutes with the right action used for descent. The two coefficient transports consequently commute as well. Descend their unit and cocycle on the group and its square, then apply proper base change for \(m\). The resulting equivariance makes each target-orbit cohomology sheaf lisse; thus (6.52) proves the upper perverse bound globally.

Repeat this bound for \(DP,DQ\). Actual proper dual exchange and (6.50) identify that proper image with \(D(P*Q)\). Its upper bound proves the lower bound for \(P*Q\), giving the first comparison in (6.45). Twisted tensor and proper image preserve triangles, and their outputs on heart inputs are now in the heart. Their long exact sequences prove exactness in each variable.

**Associativity and the largest constituent.** With three inputs, the finite scheme of three successive modifications is closed in the product of the three bounded endpoint stages. Both intermediate-forgetting maps are proper. On common finite frames descend the ordered external tensor \(P\boxtimes Q\boxtimes R\) to a complex \(C\). Proper base change and projection identify
\[
Ra_*C=(P*Q)\widetilde\boxtimes R,\qquad
Rb_*C=P\widetilde\boxtimes(Q*R),\qquad
m_La=m_Rb=c .
\tag{6.53}
\]
Thus both parenthesizations have the specified comparison to \(Rc_*C\). For four inputs the same ordered four-chain tensor and composed proper counits give both pentagon paths. Tensor associativity and proper composition make them equal on the common frames, and normalized torsor full faithfulness gives equality downstairs. Fixing one modification at the base point gives the identity correspondence and the unit triangles. These maps are constructed in [Theorem A.6.2.1](course:GL-SAT/GL-SAT-07#a62-unit-and-associativity-from-the-actual-chain-correspondence).

Finally the image of \(Z_\alpha\widetilde\times Z_\beta\) is \(Z_{\alpha+\beta}\). The fibre over its largest orbit is zero dimensional. At \(\nu=w_0(\alpha+\beta)\), a point of that finite torus-stable fibre has first endpoint \(t^\phi\). The two nonnegative numbers
\[
\langle\rho,\alpha+\phi\rangle,\qquad
\langle\rho,\beta+\nu-\phi\rangle
\tag{6.54}
\]
sum to zero. The minimum of \(\rho\) on a Weyl orbit is its antidominant value. Together with the Schubert closure order, this forces \(\phi=w_0\alpha\) and second relative endpoint \(w_0\beta\). The endpoint immersion makes the geometric fibre a single point in the open source stratum. Its possible nilpotents do not change étale sheaves. Proper base change therefore gives
\[
(IC_\alpha^{\mathrm{raw}}*IC_\beta^{\mathrm{raw}})
|_{O_{\alpha+\beta}}
=E[d_{\alpha+\beta}].
\tag{6.55}
\]
The genuine orbit system is constant, by its connected smooth stabilizer and the identity action there. Finite length and the simple-object description in Theorem B.2.3.1 now prove multiplicity one: open restriction is exact, all smaller-support simples vanish there, and the remaining rank is one. The raw convention is \(IC_\lambda^{\mathrm{raw}}|_{O_\lambda}=E[d_\lambda]\); its dual is \(IC_\lambda^{\mathrm{raw}}(d_\lambda)\). No choice of a square root of the Tate line enters the argument.

This proposition concerns the equal-characteristic Grassmannian over the specified algebraically closed field. The relative \(B_{\mathrm{dR}}^+\) convolution assertions above concern a different base and coefficient geometry.

For a primary account of the rational convolution theorem and its geometric setting, see X. Zhu, [*An introduction to affine Grassmannians and the geometric Satake equivalence*, Section 5.1](https://arxiv.org/abs/1603.05593v2).

### 6.7. Perfect coefficients and degree bounds across a dense locus

Let \(\Lambda\) be any commutative ring. A perfect complex is represented by a bounded complex of finitely generated projective \(\Lambda\)-modules. Write \(C^\vee=R\operatorname{Hom}_\Lambda(C,\Lambda)\), with the usual cochain Hom differential. For integers \(a\le b\), say that \(C\) has Tor-amplitude in \([a,b]\) if
\[
H^j(C\otimes_\Lambda^L M)=0
\quad(j\notin[a,b])
\quad\text{for every }\Lambda\text{-module }M.
\tag{6.56}
\]
There is no Noetherian or finite-global-dimension assumption in this subsection.

**Lemma 6.7 (the two-sided perfect-complex test).** For perfect \(C\), the following conditions are equivalent:
\[
\begin{aligned}
&C\text{ has a finite projective representative in degrees }[a,b];\\
&C\text{ has Tor-amplitude in }[a,b];\\
&C\in D^{\le b}(\Lambda)
\quad\text{and}\quad C^\vee\in D^{\le-a}(\Lambda).
\end{aligned}
\tag{6.57}
\]
In particular,
\[
C,\ C^\vee\in D^{\le0}(\Lambda)
\quad\Longleftrightarrow\quad
C\simeq P[0]\text{ for a finitely generated projective }P.
\tag{6.58}
\]

**Proof.** The first condition implies the second because projective terms are flat. A bounded complex of flat modules computes derived tensor: filter it by its finitely many terms; tensoring an acyclic complex with each flat term is acyclic, and finite cones retain acyclicity. The first condition also implies the third by dualizing its finite projective terms.

Conversely, start with a bounded projective representative \(Q\). If its highest nonzero term is \(Q^n\), \(n>b\), then \(H^n(Q)=0\) makes \(Q^{n-1}\to Q^n\) surjective. Projectivity of \(Q^n\) supplies a section. Thus
\[
Q^{n-1}=\ker d^{n-1}\oplus Q^n,
\tag{6.59}
\]
and the second summand maps identically to \(Q^n\). The preceding differential lands in the kernel because \(d^2=0\). We have split off the contractible two-term identity complex; the remaining kernel is a finitely generated projective direct summand. Repeating gives a representative in degrees at most \(b\). If \(C^\vee\in D^{\le-a}\), apply the same procedure to its termwise dual, removing the terms above \(-a\). Dualizing these splittings removes only the terms below \(a\) in the original representative, without creating terms above \(b\). Termwise double evaluation, with its cochain signs, identifies the resulting double dual with the original finite projective complex. This proves the third condition implies the first.

It remains to recover finite projective terms from the Tor-amplitude condition. Taking \(M=\Lambda\) first gives the upper bound, so use (6.59) to assume \(Q^j=0\) for \(j>b\). Put
\[
N=\operatorname{coker}(Q^{a-1}\longrightarrow Q^a).
\]
The truncated augmented complex
\(\cdots\to Q^{a-1}\to Q^a\to N\to0\)
is a finite projective resolution, because \(H^j(Q)=0\) for \(j<a\). Its first Tor group with any \(M\) is \(H^{a-1}(Q\otimes M)\), which vanishes by (6.56). The [Tor criterion for flatness](course:AG-CA/tor-and-flat-modules#2-the-ideal-and-tor-criteria) therefore makes \(N\) flat. That criterion uses the natural long exact sequence from the [resolution and total-complex proof](course:AG-CA/resolutions-tor-and-ext#3-balance-and-symmetry-of-tor), with arbitrary module ranks.

We give the finite-presentation step explicitly. Since \(Q^{a-1}\) and \(Q^a\) are finitely generated projective, \(N\) has a finite presentation. Indeed choose a finite projective complement of \(Q^a\) in \(\Lambda^r\); the kernel of \(\Lambda^r\to N\) is the sum of that complement and the image of \(Q^{a-1}\), hence finitely generated. Write this kernel as \(K\), generated by vectors
\[
v_j=\sum_{i=1}^r a_{ij}e_i\in K,\qquad 1\le j\le s.
\]
Flatness of \(N\) and the Tor exact sequence imply that \(K\otimes L\to\Lambda^r\otimes L\) is injective for every module \(L\). Take
\[
L=\operatorname{coker}
\left(\Lambda^r\xrightarrow{(a_{ij})^{\mathsf t}}\Lambda^s\right).
\]
The class of \((v_1,\ldots,v_s)\) in \(K\otimes L\) maps to zero in \(\Lambda^r\otimes L\): the vector \((e_1,\ldots,e_r)\) is a preimage there. Hence that class was zero already. Right exactness of tensor supplies \(x_1,\ldots,x_r\in K\) such that
\[
\sum_i a_{ij}x_i=v_j\quad\text{for every }j.
\tag{6.60}
\]
The map \(\Lambda^r\to K\), \(e_i\mapsto x_i\), fixes the generators \(v_j\), so it retracts \(K\hookrightarrow\Lambda^r\). Thus \(N\) is a direct summand of \(\Lambda^r\), and is finitely generated projective. Replacing the part of \(Q\) below degree \(a\) by \(N\) in degree \(a\), with its induced next differential, gives a quasi-isomorphic finite projective complex in \([a,b]\). This proves the remaining implication and (6.58).

Every cancellation above is a genuine homotopy equivalence, so tensoring it with any coefficient module or ring preserves it. The resulting representatives and the amplitude bounds are therefore valid after arbitrary change of coefficients. No particular splitting is asserted to be canonical. \(\square\)

**Proposition 6.8 (transport from a dense locus).** Let \(S\) be a space with a sheaf theory having enough points and exact stalks. Suppose its local trivializing charts map openly to \(|S|\). This includes the ordinary topology, and applies to an étale sheaf theory when its charts have these properties. Let \(j:U\hookrightarrow S\) be a dense open immersion, and let \(K\) be a locally constant perfect complex of \(\Lambda\)-modules: on a covering by such charts it is the constant complex associated to a perfect coefficient complex. Then
\[
j^*K\in D^{\le b}
\quad\Longleftrightarrow\quad K\in D^{\le b}.
\tag{6.61}
\]
The analogous lower bound holds. Tor-amplitude in any fixed interval \([a,b]\) is likewise detected on \(U\), and in particular
\[
j^*K\text{ locally finite projective in degree }0
\quad\Longleftrightarrow\quad
K\text{ locally finite projective in degree }0.
\tag{6.62}
\]

**Proof.** On a nonempty trivializing chart \(V\), write \(K|_V=\underline C_V\). The open image of \(V\) meets the dense subset \(U\); choose a point \(v\) above that intersection. The stalk at \(v\) is the coefficient complex \(C\). Exact stalks identify its cohomology with the stalks of the cohomology sheaves. The upper bound on \(U\) therefore gives \(H^r(C)=0\) for \(r>b\), so the same bound holds on all of \(V\). These charts cover \(S\), and enough points detect vanishing. This proves (6.61); the lower bound is identical.

For any module \(M\), the finite projective model of \(C\) computes the stalk of \(K\otimes_\Lambda^L M\) as \(C\otimes_\Lambda M\). If the restriction to \(U\) has Tor-amplitude \([a,b]\), the same point \(v\) consequently gives the bound for \(C\otimes M\), for every \(M\). Lemma 6.7 supplies a finite projective representative of \(C\) in that interval. It works on the entire chart and after every coefficient change. This proves the assertion about Tor-amplitude and (6.62). Restriction proves the reverse implications.

Alternatively, degree zero can be tested by the two upper bounds
\[
K\in D^{\le0},\qquad K^\vee\in D^{\le0},
\tag{6.63}
\]
where the dual is the locally constant coefficient dual. Both are detected on the dense locus by (6.61), and (6.58) gives exactly the locally finite projective conclusion. The dual here is the coefficient dual, with no structural orientation shift. \(\square\)

The local-constancy hypothesis is necessary. On \(\mathbb A^1\), with \(i:\{0\}\hookrightarrow\mathbb A^1\), the constructible complex \(i_*\Lambda[-1]\) restricts to zero on the dense complement but has nonzero degree-one stalk at zero if \(\Lambda\ne0\). All its stalks are perfect. Thus perfect stalks alone do not allow (6.61).

The distinction between degree zero and Tor-amplitude zero is also necessary for the relative Satake category. For example, let \(\Lambda=\mathbb F_\ell[t]\) and \(C=\Lambda/(t)\) in degree zero. This ring is killed by \(\ell\). The resolution
\[
C\simeq[\,\Lambda\xrightarrow{t}\Lambda\,]
\quad\text{in degrees }-1,0
\tag{6.64}
\]
makes \(C\) perfect, but \(H^1(C^\vee)=\Lambda/(t)\ne0\). Tensoring (6.64) with \(\Lambda/(t)\) gives a zero differential and nonzero cohomology in both degrees \(-1,0\). Thus neither ordinary degree zero nor perfection alone gives the flatness required in (6.62).

**The degree calculation in fusion.** In the relative Hecke setting, write
\[
B=(\operatorname{Div}^{1}_{Y})^2,\qquad
U=B\setminus\Delta,\qquad
K=R\pi_{T*}\bigl(\operatorname{CT}_{B_0}(\mathcal F)[\deg]\bigr),
\tag{6.65}
\]
where \(B_0\) is a chosen Borel, \(\mathcal F\) is the two-modification direct image, and \(\deg\) is the componentwise \(2\rho\)-shift on the torus Grassmannian. Here the bracket shift is applied before the torus direct image. If this geometric construction makes \(K\) étale locally constant with perfect coefficient fibres, and the off-diagonal restriction is in \(D^{\le0}\), (6.61) gives that same upper bound on the diagonal. For a flatness conclusion one uses Tor-amplitude, or the pair of bounds (6.63), and obtains locally finite projective degree-zero coefficients.

The application needs the geometric local-constancy statement, density on the divisor base, the finite torus-support comparison, and the conservative perverse test supplied by the constant-term functor. These are hypotheses of this application, separate from the coefficient and dense-locus propositions just proved. Fargues–Scholze's [Propositions VI.7.4, VI.7.7 and VI.8.1](https://arxiv.org/abs/2102.13459v4) use precisely these ingredients, together with preservation of universal local acyclicity under the relevant proper images and compositions.

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
\oplus i_{D*}\Lambda_D[2](-1).
\]
The diagonal-point stalk has \(\Lambda\) in degree \(-4\) and \(\Lambda(-1)\) in degree \(-2\). Finally (5.4) gives source cohomology in degrees zero and two only, equal to \(\Lambda\) and \(\Lambda(-1)\). Contraction classically, or the exact invariant summand of the finite \(\mathbb A^4\) quotient étale, gives target \(IH^0=\Lambda\) only. The diagonal summand contributes \(H^{a-2}(D,\Lambda)(-1)\) in source degree \(a\); as \(D=\mathbb A^2\), this is the single extra degree-two class.

## Geometric and coefficient hypotheses

The dimension bounds, small-map IC argument, closed-stratum splitting criterion, and explicit resolution and two-point Hilbert calculations use their indicated earlier sheaf operations. General characteristic-zero semismall decomposition additionally uses the geometric theorem of Lessons 7–8, with its weight, comparison and ordinary/adic hypotheses. Propositions 4.1–4.2 construct the classical transverse source pair and identify the actual support comparison, using the earlier Whitney, controlled-flow and relative-cochain proofs. The intersection-form identification uses oriented duality and its compatible relative cup product. A general positive-characteristic étale slice comparison requires its own geometric argument. Nor is definiteness of general intersection forms proved here.

Propositions 6.1–6.5 prove the bounded classical convolution statement for commutative Noetherian coefficient rings of finite global dimension, using perverse degree zero before descent. They prove weight concentration and detection over that ring, and show that flat total cohomology is sufficient to omit the truncation. Proposition 6.6 gives rational étale convolution over an algebraically closed ground field with the coefficient prime invertible, including exactness, actual duality, coherent associativity and the largest composition factor. Lemma 6.7 and Proposition 6.8 prove the arbitrary-ring perfect-amplitude criterion and transport of degree bounds for locally constant perfect complexes across a dense locus. Fargues–Scholze's three relative convolution assertions additionally require their diamond geometry, universal local acyclicity and conservative constant-term foundations. For general Hilbert–Chow, (5.10) and Proposition 5.1 give global smoothness and irreducibility and étale separated-support charts. Section 5 proves properness, the scheme-theoretic fibre products, the sharp fibre dimension and irreducibility of every fibre. Full Satake and Nadler's Springer/Hitchin construction are broader than the two-point example. Springer theory is the subject of the next lesson. The general proofs of these broader assertions are not contained in this lesson.

## References

- M. A. A. de Cataldo and L. Migliorini, [*The decomposition theorem, perverse sheaves and the topology of algebraic maps*](https://arxiv.org/abs/0712.0349), §4.2 on semismall maps and intersection forms, and §4.2.3 on Hilbert schemes. In the notation here, top fibre components have dimension \((d-s)/2\) and the stratum comparison has degree \(-s\).
- D. Juteau, C. Mautner and G. Williamson, [*Parity sheaves*](https://arxiv.org/abs/0906.2994v3), free author manuscript, version 3, §3 on intersection forms and the semismall decomposition criterion. That criterion does not require parity vanishing.
- I. Mirković and K. Vilonen, [*Geometric Langlands duality and representations of algebraic groups over commutative rings*](https://arxiv.org/abs/math/0401222v5), free author manuscript, version 5, §§3–4, especially Theorems 3.5–3.6, Lemmas 3.9 and 4.1, Proposition 4.2 and Lemma 4.4; [erratum](https://annals.math.princeton.edu/2018/188-3/p06).
- A. Beilinson, J. Bernstein and P. Deligne, [*Faisceaux pervers*](https://publications.ias.edu/sites/default/files/Faisceaux%20pervers.pdf), Astérisque 100 (1982), 5.3.8 and 6.2.5.
- L. Fargues and P. Scholze, [*Geometrization of the local Langlands correspondence*](https://arxiv.org/abs/2102.13459v4), version 4, Proposition VI.8.1, with the relative Satake category of §VI.7 and the local-acyclicity constructions of §IV.2.
- D. Nadler, [*Springer theory via the Hitchin fibration*](https://arxiv.org/abs/0806.4566), §4.1, for the subsequent Springer/Hitchin topic.
