# Affine morphisms, Artin vanishing and perverse cohomology

*AI-generated exposition by GPT-6 Astra (OpenAI), October 2026. Public domain (CC0).*

A direct image can acquire cohomology in two different ways: its fibres can have positive dimension, and sections near a missing boundary can carry higher cohomology. We will calculate both effects before asking what affineness removes. This makes the direction of each perverse inequality visible. The final application cuts a projective variety by a hyperplane: the error in restriction is compactly supported cohomology of the affine complement.

We use the categories of [Constructible complexes on algebraic varieties](constructible-complexes-on-algebraic-varieties.md), the truncation construction in [Gluing t-structures](gluing-t-structures.md), and the support tests of [The perverse t-structure](the-perverse-t-structure.md). Coefficients are the classical field coefficients of those lessons, or rational adic coefficients with the qualifications in Section 4. All maps are separated and of finite type. Dimensions are complex or algebraic dimensions; the dimension of an empty support is minus infinity. Our shift convention is \(\mathcal H^q(K[r])=\mathcal H^{q+r}K\). In the étale case, global cohomology is geometric cohomology over an algebraic closure; relative functors retain descent data and Tate twists.

For the affine and smooth statements and their hypotheses, see Beilinson–Bernstein–Deligne, Sections 4.1–4.2, and de Cataldo–Migliorini, Section 5.3. The deductions below use the earlier programme constructions with the coefficient and geometric hypotheses specified at each step.

## 1. Read degrees from a perverse tower

Write \(\mathcal P(X)\) for the perverse heart. For a bounded constructible complex \(M\), its successive perverse layers are

\[
{}^pH^b(M)=({}^p\tau^{\ge b}{}^p\tau^{\le b}M)[b]\in\mathcal P(X).
\tag{1.1}
\]

The truncation axioms proved in the gluing lesson give triangles

\[
{}^p\tau^{\le b-1}M\longrightarrow{}^p\tau^{\le b}M
\longrightarrow{}^pH^b(M)[-b]\longrightarrow.
\tag{1.2}
\]

Boundedness makes this a finite construction of \(M\) from its layers. It does not provide a direct-sum decomposition. An exact triangulated functor which preserves both halves of the t-structure carries the truncation triangle to a truncation triangle; uniqueness of that triangle gives

\[
F({}^pH^bM)\simeq{}^pH^b(FM).
\tag{1.3}
\]

Here **right t-exact** means preservation of \({}^pD^{\le0}\), and **left t-exact** means preservation of \({}^pD^{\ge0}\). We will state the inequalities as well as the terminology.

For \(M=Rf_*K\), apply \(H^*(Y,-)\) to (1.2). To see the indexing rather than guess it, put

\[
D^{a,b}=H^{a+b}(Y,{}^p\tau^{\le b}M),\qquad
E^{a,b}=H^a(Y,{}^pH^bM).
\tag{1.4}
\]

The long exact sequences give an exact couple with arrows
\(D^{a+1,b-1}\to D^{a,b}\to E^{a,b}\to D^{a+2,b-1}\).
The composite through the next \(D\)-term has bidegree \((2,-1)\). Taking its kernels modulo its images, and replacing \(D\) by the image of its first arrow, gives the derived couple. Repeating this construction increases the first component of the differential by one and decreases the second by one. Thus the resulting spectral sequence has

\[
E_2^{a,b}=H^a(Y,{}^pH^b(Rf_*K)),\qquad
d_r:E_r^{a,b}\to E_r^{a+r,b-r+1},
\quad E_2\Longrightarrow H^{a+b}(X,K).
\tag{1.5}
\]

The finite tower ensures convergence: below its first layer the truncation is zero, and above its last it is \(M\); consequently the surviving quotients are exactly those of the finite filtration

\[
P_bH^n(X,K)=\operatorname{im}\bigl(
H^n(Y,{}^p\tau^{\le b}Rf_*K)\to H^n(X,K)\bigr).
\tag{1.6}
\]

This is the perverse Leray spectral sequence. Negative indices are allowed. No degeneration assertion has entered its construction.

Two calculations now test any proposed degree bound. For the proper map \(a:\mathbb P^1\to\mathrm{pt}\), the perverse input \(\Lambda[1]\) has image with cohomology in degrees \(-1\) and \(1\): these come from the degree-zero and degree-two cohomology of the projective line. For the open map
\(v:\mathbb C^2\setminus\{0\}\to\mathbb C^2\), the degree-one stalk of \(Rv_*\Lambda[2]\) is also nonzero: a punctured ball retracts onto \(S^3\), and shifting its top cohomology by two puts it in degree one. The first map has one-dimensional fibres; the second has zero-dimensional fibres. Thus positive degree in a nonproper direct image cannot be bounded by fibre dimension alone. We will justify and use both calculations below.

## 2. Obtain the inequalities supplied by dimension

Suppose every fibre of \(f:X\to Y\) has dimension at most \(d\). For a constructible subset \(T\subset Y\),

\[
\dim f^{-1}T\le\dim T+d.
\tag{2.1}
\]

Indeed, partition \(T\) into locally closed pieces and take an irreducible component \(W\) of their inverse images. If \(Z\) is its image closure, the dimension formula for finite-type integral varieties gives
\(\dim W=\dim Z+\operatorname{trdeg}_{k(Z)}k(W)\).
The second summand is the dimension of the generic fibre of \(W\to Z\), at most \(d\). Taking maxima proves (2.1). This argument requires the algebraic dimension formula stated above.

**Proposition 2.1.** Under this fibre hypothesis the following four bounds hold:

\[
\begin{aligned}
f^*({}^pD^{\le0}(Y))&\subset{}^pD^{\le d}(X),&
Rf_!({}^pD^{\le0}(X))&\subset{}^pD^{\le d}(Y),\\
f^!({}^pD^{\ge0}(Y))&\subset{}^pD^{\ge-d}(X),&
Rf_*({}^pD^{\ge0}(X))&\subset{}^pD^{\ge-d}(Y).
\end{aligned}
\tag{2.2}
\]

**Proof.** The upper support test says that \(A\in{}^pD^{\le0}(Y)\) has
\(\dim\operatorname{Supp}\mathcal H^qA\le-q\).
Ordinary pullback is exact, so (2.1) bounds the support of \(\mathcal H^qf^*A\) by \(-q+d\). This proves the first inclusion.

Next take \(B\in{}^pD^{\ge0}(X)\). For every \(A\in{}^pD^{\le-d-1}(Y)\), the first inclusion puts \(f^*A\) in \({}^pD^{\le-1}(X)\). Adjunction and orthogonality give
\(\operatorname{Hom}(A,Rf_*B)=\operatorname{Hom}(f^*A,B)=0\).
The orthogonal characterization of the lower half therefore gives the last inclusion. Over our field coefficients, Verdier duality reverses the two perverse halves and exchanges star with shriek. Dualizing the two proved inclusions gives the other two. These last deductions require the precise operation and duality prerequisites, not all of which are proved in these lessons. \(\square\)

For proper \(f\), identify \(Rf_!=Rf_*\). A perverse input then has image only in perverse degrees \([-d,d]\). For finite \(f\), use \(d=0\): **finite direct image is t-exact**. Smoothness is unnecessary. For quasi-finite \(f\), properness is unnecessary for the individual conclusions

\[
Rf_*({}^pD^{\ge0})\subset{}^pD^{\ge0},\qquad
Rf_!({}^pD^{\le0})\subset{}^pD^{\le0}.
\tag{2.3}
\]

Return to the open immersion \(v\) of Section 1. On its smooth source \(\Lambda[2]\) is perverse. The sphere calculation gives

\[
\mathcal H^q(i^*Rv_*\Lambda[2])=
\begin{cases}\Lambda&q=-2,1,\\0&\text{otherwise},\end{cases}
\quad i:\{0\}\hookrightarrow\mathbb C^2.
\tag{2.4}
\]

The sphere has one cell in dimensions zero and three, with zero cellular differential, so these are precisely its two groups after the shift. Its degree-one group violates the upper perverse stalk test at a point. Thus \(d=0\) in (2.2) cannot be used to add an upper bound on \(Rf_*\). The map \(v\) is not affine. To verify this algebraically, cover the punctured plane by \(D(x)\) and \(D(y)\). A regular function belongs to
\(\mathbb C[x,y]_x\cap\mathbb C[x,y]_y\)
inside \(\mathbb C(x,y)\). Coprimality of \(x\) and \(y\) forces all denominators to cancel, so the intersection is \(\mathbb C[x,y]\). If the punctured plane were affine, its canonical map to the spectrum of its global functions would be an isomorphism; that map is the inclusion missing the origin, a contradiction.

The projective-line calculation is different. The classical sphere model for \(\mathbb P^1\) has one cell in dimensions zero and two. The earlier étale curve calculation gives the corresponding geometric groups with the orientation twist. Hence

\[
{}^pH^b(Ra_*\Lambda[1])=
\begin{cases}\Lambda&b=-1,\\\Lambda(-1)&b=1,\\0&\text{otherwise},\end{cases}
\tag{2.5}
\]

where the twist is omitted classically. The target is a point, so ordinary and perverse degrees agree. This attains both ends of the proper interval \([-1,1]\) and disproves right t-exactness for a general proper map.

## 3. Transport a perverse sheaf through a smooth map

### The relative smooth orientation

We need the smooth formula with arbitrary constructible coefficients on the base, including a singular base. The classical argument uses the compact-support operations of the first lesson, H.2–H.5. All coefficient vector spaces are over the fixed field \(\Lambda\).

**Lemma 3.0.** Suppose \(f:X\to Y\) is locally a projection in smooth relative charts with real \(m\)-dimensional manifold fibres, and the spaces have the locally compact, finite-dimensional hypotheses of H. Let \(\mathrm{or}_f\) be the relative orientation sheaf. For every bounded coefficient complex \(G\), the canonical coefficient map gives
\[
 f^*G\otimes\mathrm{or}_f[m]\xrightarrow{\ \sim\ }f^!G.
 \tag{3.O1}
\]
For a smooth complex algebraic map of pure relative dimension \(r\), the relative orientation is canonically trivial and \(m=2r\). No smoothness of \(Y\) is required.

**Proof.** Start with the projection \(p:Y\times B_0\to Y\), where \(B_0\) is an oriented open \(m\)-ball. For an open \(V\subset Y\) and an oriented ball \(B\subset B_0\), write \(W=V\times B\), and use \(\Lambda_W\) and \(\Lambda_V\) for extension by zero of the constant sheaves on those opens. Proper-support base change (H.6), composition with open extension, and the ball calculation C.5 give
\[
 Rp_!\Lambda_W\simeq
 \Lambda_V\otimes R\Gamma_c(B,\Lambda)
 \simeq\Lambda_V[-m].
 \tag{3.O2}
\]
These are the proper-support base-change maps. Extension by zero from a smaller oriented ball preserves the generator: the compact support can be placed in a still smaller closed ball, where support excision identifies both generators. This compatibility is proved in F.5.

The exceptional adjunction (H.14) now computes the actual local sections:
\[
 \begin{aligned}
 R\Gamma(W,p^!G)
 &\simeq R\operatorname{Hom}_{Y\times B_0}(\Lambda_W,p^!G)\\
 &\simeq R\operatorname{Hom}_Y(Rp_!\Lambda_W,G)\\
 &\simeq R\Gamma(V,G)[m].
 \end{aligned}
 \tag{3.O3}
\]
Shrinking \(V\) induces ordinary restriction on the last line; shrinking \(B\) preserves its oriented generator. Product rectangles form a neighbourhood basis at \(x=(y,b)\). Taking the filtered colimit of the degree-\(q\) groups in (3.O3) therefore gives
\[
 \mathcal H^q(p^!G)_x\simeq\mathcal H^{q+m}(G)_y.
 \tag{3.O4}
\]
To justify this passage for complexes, take an injective resolution. The filtered colimit of its sections on neighbourhoods is its stalk complex, and exact filtered colimits of vector spaces commute with cohomology. Thus no ordinary-image fibre formula or ordinary product-cohomology assertion is needed here.

In particular \(\omega_p=p^!\Lambda_Y\) has its only cohomology in degree \(-m\), with its positive generator specified by (3.O3). Truncation gives \(\omega_p\simeq\Lambda[m]\). On overlaps of relative coordinate charts, the generator changes by the orientation sign: C.4 proves the determinant rule by deforming a coordinate change to its derivative on a small punctured ball. Consequently the same local calculation for \(f\) gives
\[
 \omega_f=f^!\Lambda_Y\simeq\mathrm{or}_f[m].
 \tag{3.O5}
\]
Restriction of the exceptional image to a source open is the exceptional image of the restricted map, by H.5 and composition with extension by zero. Thus these local calculations concern the one global object \(\omega_f\).

There is also a single global coefficient map. Transpose the following composite through \(Rf_!\dashv f^!\):
\[
 Rf_!(f^*G\otimes\omega_f)
 \simeq G\otimes Rf_!\omega_f
 \xrightarrow{\,1\otimes\varepsilon_\Lambda\,}G.
 \tag{3.O6}
\]
Here the first map is H.4's projection isomorphism and the second uses the actual adjunction counit. Call its transpose \(\theta_{f,G}:f^*G\otimes\omega_f\to f^!G\). It restricts to the corresponding map in every product chart. Under (3.O3), its map on a cohomology germ of \(G\) is that germ multiplied by the positive ball trace, hence is the identity in (3.O4). More explicitly, represent the germ by a local derived section, or a map \(\Lambda_V[-q-m]\to G\), and use naturality of \(\theta\). For the coefficient unit the transpose in (3.O6) is the identity of \(\omega_f\), by the adjunction identity; shrinking the representing neighbourhood gives the asserted stalk map. Thus \(\theta_{f,G}\) induces an isomorphism on every cohomology stalk, proving (3.O1).

A smooth complex algebraic morphism has these local projection charts even when the base is singular. The étale coordinates of Smooth morphisms, Theorem 4.1 give relative equations with invertible Jacobian. The parameter inverse-function argument I.1, applied in an ambient parameter neighbourhood and then restricted to the base, solves them analytically. Vertical holomorphic coordinate changes have positive real determinant \(|\det_{\mathbb C}|^2\), by C.4. Their orientation signs are therefore \(+1\), and (3.O5) becomes \(\omega_f=\Lambda_X[2r]\). This proves the complex assertion. \(\square\)

The identifications preserve the counits and the comparisons used below. For composition, H.5 composes the actual exceptional adjunctions, and H.3 composes proper support. On successive product charts the compact orientation generator is the product generator: the successive relative connecting maps of C.4–C.5 give that generator in the concatenated coordinates. Both integration maps send it to \(1\). Complex orientation shifts are even, so exchanging the two blocks introduces no sign. The relative dualizing objects have cohomology in a single degree, so equality of their oriented maps is equality of sheaf maps after that shift. For general \(G\), associativity of projection and composition of the counits in (3.O6) give the same transpose; this proves the composed coefficient comparison. For base change, H.2 pulls back the same supported sections and (3.O2) the same ball generator. This identifies the comparison on the relative dualizing object. The natural projection and counit maps then give its coefficient comparison, whose transpose is the canonical exceptional base-change map. These statements identify the maps, not just the stalk dimensions.

For the arithmetic coefficient categories, the corresponding input is
\[
 f^!G\simeq f^*G(r)[2r].
 \tag{3.O7}
\]
The finite-coefficient proof is BJ.4–BJ.6: the coordinate traces agree by the relative-curve calculation; the proper-support top-degree bound defines their unique derived trace; projection and adjunction produce the smooth coefficient map. Its coordinate restrictions are the affine-line adjunction isomorphisms. BJ.6 proves compatibility with composition and base change using those same traces. BV.2–BV.4 carry this map through finite coefficient change and the single category of complete coefficient diagrams. BW.7–BX.7 identify its rationalization with the actual rational operation. Thus (3.O7) uses the complete and rational categories at their stated field-level scope.

Finally the dual exchange \(D_Xf^*G=f^!D_YG\) is (H.17) classically and (BV.20) with its rational comparison arithmetically. Substituting (3.O1) or (3.O7) and using \(D(K[r])=(DK)[-r]\) gives (3.1), including its twist. This is the smooth-duality input to the following perverse argument.

**Proposition 3.1.** If \(f:X\to Y\) is smooth of pure relative dimension \(r\), then \(f^*[r]\) is t-exact. If all its geometric fibres are connected and nonempty, its restriction to perverse hearts is fully faithful.

**Proof of t-exactness.** Apply (2.1) to each ordinary cohomology sheaf of \(K\in{}^pD^{\le0}(Y)\). The degree \(q\) sheaf of \(f^*K[r]\) has support dimension at most
\(-(q+r)+r=-q\).
Thus the upper test holds. Smooth duality, with the orientation supplied by the complex or étale theory, reads

\[
D_X(f^*K[r])\simeq f^*(D_YK)[r](r).
\tag{3.1}
\]

Again omit the twist classically. Apply the already proved upper bound to \(D_YK\); since twisting does not change support or degrees, duality gives the lower bound. This proves both halves. \(\square\)

**Proof of full faithfulness.** We first compute the degree-zero adjunction unit for ordinary coefficient sheaves, then apply that calculation to exceptional restrictions of a perverse sheaf.

**Local sections and ordinary sheaves.** In the classical topology a smooth map has local sections: in a smooth coordinate chart it is a projection, and fixing the fibre coordinate gives a section. For an algebraic smooth map this chart follows from étale coordinates, Theorem 4.1; over the complex numbers the invertible Jacobian makes its analytic coordinate map a local isomorphism, by the parameter inverse-function construction in I.1. The construction works over a singular base as well: solve the relative equations in an ambient parameter neighbourhood and restrict the resulting section to the base.

In the étale topology use Smooth morphisms, Theorem 5.2. Here is the construction relevant to the sheaf argument. A nonempty smooth fibre has a point over a finite separable extension of the residue field: an étale chart has open image in affine space, and that image has a point over the separable closure. Its finitely many coordinates and equations descend to a finite separable extension. A separable polynomial and its invertible derivative realize this extension on an étale neighbourhood of the base point. After this change the chosen fibre point is rational. Lift its coordinates to local functions on the base and pull the étale chart back along their graph. This gives a further étale neighbourhood mapping into \(X\), hence a section of the pulled-back \(f\). The proof of Theorem 5.2 includes the denominator clearing and the nonemptiness of this graph pullback.

Let \(H\) be an ordinary sheaf, classically, or a finite-coefficient étale sheaf. The map
\[
 H\longrightarrow f_*^{\mathrm{ord}}f^*H
 \tag{3.3}
\]
is an isomorphism when the fibres are connected and nonempty. This is local on the target. On a neighbourhood with section \(s\), pull a section \(t\) of \(f^*H\) back along \(s\), obtaining \(u\) in \(H\). On each geometric fibre, the pullback of \(H\) is constant with the corresponding stalk as value. A section of a constant sheaf on a connected space has a single value: the inverse images of its values are disjoint open and closed subsets. The étale assertion follows by the same description of the constant sheaf as the disjoint union of copies of the scheme. Thus \(t\) and \(f^*u\) agree at every point of that fibre. Geometric stalks detect equality, so they agree everywhere. Nonempty fibres make \(u\) unique. These sections therefore glue on overlaps, proving (3.3) for the actual adjunction map.

For complete integral coefficients, let \(H_n\) be the strict finite quotient system of a standard-heart object \(H\). BP.2–BP.4 identify \(H\) with \(R\!\varprojlim\nu^*H_n\); BQ.5 identifies the pulled-back heart object with the system \(f^*H_n\). The actual ordinary image is a right adjoint and commutes with these derived limits. Its finite-coefficient comparison is BK.5. Each \(Rf_*\nu^*f^*H_n\) has no negative cohomology, so the product-cone formula gives
\[
 \mathcal H^0Rf_*f^*H
 =\varprojlim_n\nu^*(f_*^{\mathrm{ord}}f^*H_n)
 =\varprojlim_n\nu^*H_n=H.
 \tag{3.4}
\]
There is no degree-minus-one term contributing to this degree-zero limit. The maps in (3.4) are induced by the finite-level units, so their composite is the degree-zero unit. This uses ordinary strict quotients to reconstruct a heart object; it does not identify a derived reduction with its ordinary quotient.

Every rational standard-heart object has an integral heart model by BW.7. Exact rationalization and the actual image comparison BX.22 carry (3.4) to rational coefficients. Exact faithful extension of a finite coefficient field gives the same conclusion over \(\overline{\mathbb Q}_\ell\). Thus (3.3), interpreted as the degree-zero derived unit, holds in every coefficient category used in Proposition 3.1.

**The unit on bounded complexes.** Put
\[
 T_f(A)=\operatorname{Cone}\bigl(A\xrightarrow{\eta_A}Rf_*f^*A\bigr).
 \tag{3.5}
\]
For an ordinary sheaf \(H\), exact pullback and the left exactness of ordinary direct image put \(Rf_*f^*H\) in ordinary degrees at least zero. Its degree-zero unit is (3.3)–(3.4), hence \(T_f(H)\in D^{\ge1}\). For a bounded \(A\in D^{\ge n}\), its finite ordinary truncation tower has layers \(\mathcal H^j(A)[-j]\), with \(j\ge n\). Naturality of the unit gives maps between these towers. Their cone triangles, formed on complexes, have layers \(T_f(\mathcal H^jA)[-j]\in D^{\ge j+1}\). Extension closure yields
\[
 A\in D^{\ge n}\quad\Longrightarrow\quad T_f(A)\in D^{\ge n+1}.
 \tag{3.6}
\]
This argument also accounts for the adjacent cohomology degree in a cone; an isomorphism on the lowest cohomology group alone would not suffice.

**The perverse lower bound.** Let \(a:S\hookrightarrow Y\) be a smooth locally closed stratum of dimension \(s\), and form \(a_X:X_S\hookrightarrow X\) and \(f_S:X_S\to S\). Closed-image base change \(f^*a_*=a_{X,*}f_S^*\), transposed through its adjunctions, gives \(a^!Rf_*=Rf_{S,*}a_X^!\) when \(a\) is closed. For an open immersion this is restriction of the ordinary image to an open slice. Factoring a locally closed immersion into these two cases proves the same identity for \(a\).

Transitivity of exceptional inverse images and the smooth orientations for \(f\) and \(f_S\), of the same relative dimension \(r\), give
\[
 a_X^!f^*A\simeq f_S^*a^!A.
 \tag{3.7}
\]
Indeed apply \(a_X^!f^!\simeq f_S^!a^!\) and cancel the common invertible twist and shift \((r)[2r]\). The classical transitivity is H.5; the complete-coefficient version and its smooth orientation are BV.4, transported to rational coefficients by BW.7–BX.7. The comparisons use the same adjunction counits. Transposing the closed-image base-change map and the orientation square therefore takes \(a^!\eta_A\) to the unit for \(f_S\), and gives
\[
 a^!T_f(A)\simeq T_{f_S}(a^!A).
 \tag{3.8}
\]
In particular these are comparisons of the specified maps, not merely of their source and target objects.

Take \(A=Q\in\mathcal P(Y)\). The lower perverse test is \(a^!Q\in D^{\ge-s}\). Every base change \(f_S\) remains smooth with connected nonempty geometric fibres, so (3.6) and (3.8) give \(a^!T_f(Q)\in D^{\ge1-s}\). Choose a finite smooth partition adapted to this constructible cone as well as to \(Q\). The exceptional-restriction test then says
\[
 T_f(Q)\in{}^pD^{\ge1}(Y).
 \tag{3.9}
\]
For \(P\in\mathcal P(Y)\), orthogonality kills both \(\operatorname{Hom}(P,T_f(Q))\) and \(\operatorname{Hom}(P,T_f(Q)[-1])\). The unit triangle and ordinary adjunction consequently identify
\[
 \operatorname{Hom}_Y(P,Q)
 \xrightarrow{\ \sim\ }
 \operatorname{Hom}_X(f^*P[r],f^*Q[r]).
 \tag{3.10}
\]
The map is precisely pullback of morphisms. Together with the already proved t-exactness, this proves full faithfulness on the perverse hearts. \(\square\)

For classical sheaves there is also a useful morphism-sheaf description. Set \(H=\mathcal H^0R\mathcal Hom_Y(P,Q)\). On each open subset, negative derived Hom between the restricted heart objects vanishes by orthogonality. The definition of the cohomology sheaves of internal Hom therefore makes its negative cohomology sheaves zero. Ordinary truncation gives
\[
\operatorname{Hom}(P,Q)=\Gamma(Y,H).
\tag{3.2}
\]
The identity \(R\mathcal Hom(P,Q)=D(P\otimes DQ)\), smooth duality and biduality identify the pullback internal Hom with \(R\mathcal Hom(f^*P,f^*Q)\): the inner smooth dual contributes \((r)[2r]\), and the outer dual contributes its inverse. Transposing evaluation fixes the resulting comparison. Exact pullback thus identifies the morphism sheaf upstairs with \(f^*H\); (3.3) recovers (3.10). The unit-and-costalk proof above supplies the rational-adic argument through its finite quotients and specified coefficient maps.

Both qualifications on fibres are necessary. A non-surjective open immersion is smooth with nonempty fibres connected wherever they exist, but kills a nonzero perverse sheaf supported in its complement. Pullback from a point to two points sends \(V\) to \((V,V)\); the target allows two independent endomorphisms, whereas pullback supplies only diagonal pairs.

## 4. Why affineness removes the positive degrees

The ordinary support estimate needed here is

\[
\dim\operatorname{Supp}R^af_*F\le
\dim\operatorname{Supp}F-a\qquad(a\ge0)
\tag{4.1}
\]

for affine \(f\) and an ordinary constructible sheaf \(F\). We first deduce the perverse consequence from this precise estimate, then examine its coefficients and geometric hypotheses.

**Theorem 4.1 (affine bounds).** For affine \(f\) in the classical algebraic and rational adic settings fixed above,

\[
Rf_*({}^pD^{\le0})\subset{}^pD^{\le0},\qquad
Rf_!({}^pD^{\ge0})\subset{}^pD^{\ge0}.
\tag{4.2}
\]

**Proof.** For an upper object \(K\), use its finite *ordinary* truncation tower. A layer is \(\mathcal H^bK[-b]\), and its direct image has degree \(n=a+b\) sheaf \(R^af_*\mathcal H^bK\). Equation (4.1) bounds that support by
\(-b-a=-n\).
Thus every image layer lies in the upper perverse part. This part is extension closed: the cohomology sequence of a triangle bounds each middle support by the union of the two outer supports. The finite tower therefore puts \(Rf_*K\) in the upper part. For a lower object \(L\), apply this to \(D_XL\) and use \(D_YRf_!L=Rf_*D_XL\). Field duality reverses the inequality and proves the second assertion. \(\square\)

For a perverse sheaf \(P\) on an affine variety \(U\), the structural map has a point as target; (4.2) gives

\[
H^n(U,P)=0\ (n>0),\qquad H_c^n(U,P)=0\ (n<0).
\tag{4.3}
\]

These conclusions concern geometric cohomology in the arithmetic setting. Including the Galois cohomology of a non-algebraically-closed base would be a different operation.

### Torsion support and the integral cut

For torsion coefficients with torsion prime to the characteristic, the earlier lesson [Cohomological dimension and the Künneth formula](course:ag-etale-cohomology/cohomological-dimension-and-the-kunneth-formula#6-affine-direct-images-lower-support-dimension), Theorem 6.2, writes the relative Artin proof. Its bound applies to every torsion sheaf, using the transcendence degrees of points with nonzero stalks. The proof uses strict-local finite models and affine cohomological-dimension induction; it does not replace a nonproper direct-image stalk by the cohomology of the geometric fibre. On constructible supports the transcendence-degree bound is (4.1). [Appendix C](#appendix-c-affine-images-at-a-strict-local-base) gives the strict-local support calculation with its exact finite-model, continuity and absolute affine-vanishing inputs, including the passage from those models to the actual higher-image stalk.

For rational adic coefficients we need a separate argument. Let \(E/\mathbb Q_\ell\) be finite, \(\mathcal O\) its valuation ring, \(\pi\) a uniformizer, and \(k=\mathcal O/(\pi)\). Use the bounded complete constructible category of the first lesson, identified with its completed-ring presentation in BW. The operation inputs below are supplied for separated finite-type schemes and morphisms over a field, with \(\ell\) invertible in that field. The base field is distinct from the coefficient residue field \(k\).

| Input used in the integral argument | Exact earlier proof and scope |
|---|---|
| A bounded integral category and ordinary truncations | BM.6 gives boundedness; BQ.3–BQ.4 recover its cohomology and truncations. |
| Nonproper direct image and coefficient reduction | BV.1, using M.4 and BK.5, proves bounded constructibility and the actual reduction comparison (BV.3). No properness hypothesis or nonproper fibre formula is inserted. |
| Finite integral coefficient fibres | BP.1–BP.2 identify strict systems on a common finite partition with finite \(\mathcal O\)-modules; BQ.3 applies this to the cohomology of an image. |
| Recollement and exceptional restriction | BV.4 gives the exceptional adjoint, closed-support triangle and smooth orientation. BX.2 supplies the ordinary open–closed triangle. The categorical cut is Gluing t-structures, Theorem 2.1. |
| Integral models and rational operations | BX.6–BX.7 give constructible integral models and the equivalence (BX.20). Equations (BX.21)–(BX.22) identify ordinary restriction and image after rationalization; the exceptional adjunction and its closed-support comparison identify exceptional restriction as well. |

These are the specified maps, not just equalities of cohomology dimensions. Nonproper image finiteness and exceptional rationalization are therefore supplied inputs at this field-level scope, rather than unwritten premises. [Appendix B](#appendix-b-integral-dimension-cuts-and-change-of-coefficients) proves the smooth-stratum exceptional comparison, refinement independence and integral perverse truncation over the finite or algebraically closed ground fields fixed in the first lesson. The field-level constructibility theorem requires its stated algebraic and cohomological prerequisites; it does not extend to an arbitrary trait or strict-local limit.

**Lemma 4.2 (integral upper model).** Under these integral hypotheses, every rational \(K\in{}^pD^{\le0}(X,E)\) has a model \(L\in{}^pD^{\le0}(X,\mathcal O)\) whose derived reduction \(L\otimes^L_{\mathcal O}k\) is also upper perverse.

**Proof.** Construct the integral t-structure by induction on a finite stratification. On a smooth stratum of dimension \(s\), use the ordinary t-structure shifted so that its upper part is \(D^{\le-s}\). For an object \(L_0\), choose such a dense open union \(j:U\hookrightarrow X\) on which its cohomology is locally constant; let \(i:Z\hookrightarrow X\) be the smaller-dimensional complement. Cut the open restriction at the indicated ordinary degree, obtaining \(U_0\). Form

\[
j_!U_0\longrightarrow L_0\longrightarrow L_1\longrightarrow,
\qquad F_0={}^p\tau_Z^{\le0}i^!L_1,
\qquad i_*F_0\longrightarrow L_1\longrightarrow B\longrightarrow.
\tag{4.4}
\]

The closed truncation exists by induction. The octahedron produces triangles
\(A\to L_0\to B\to\) and \(j_!U_0\to A\to i_*F_0\to\).
They give \(j^*A=U_0\), \(i^*A=F_0\), while \(j^*B\) and \(i^!B\) have the positive bounds on their respective pieces. Hence \(A\) is upper and \(B\) is lower of degree at least one for the glued pair. Orthogonality follows from the open ordinary orthogonality and the closed inductive orthogonality by applying Hom to \(j_!j^*A\to A\to i_*i^*A\to\). This is precisely the truncation construction proved in the earlier gluing lesson. Its upper condition is the stalk-support condition; the lower condition uses exceptional restriction. No self-duality of an integral heart is asserted. The finite number of strata and the stated operation hypotheses ensure boundedness and constructibility. The smooth-stratum restriction comparison and refinement independence are proved in B.1–B.2; Theorem B.1 supplies the bounded integral cut without assuming self-duality of its heart.

Choose an integral model \(L_0\) of \(K\), using BX.6–BX.7: stratum lattices and extension-class lifting give constructible integral models, and finite truncation towers give models of bounded complexes. A global lisse lattice on a singular scheme is not assumed. Flat rationalization commutes with both restriction tests by BW.7 and BX.7, including exceptional restriction, at the stated field-level scope. B.4 applies these maps to the integral perverse cut. It therefore carries a glued truncation triangle to the rational truncation triangle. Uniqueness gives
\(({}^p\tau^{\le0}L_0)\otimes E\simeq{}^p\tau^{\le0}K=K\).
Take \(L={}^p\tau^{\le0}L_0\).

Derived reduction is the cone in

\[
L\xrightarrow{\pi}L\longrightarrow L\otimes^L_{\mathcal O}k
\longrightarrow L[1].
\tag{4.5}
\]

The upper part contains both \(L\) and \(L[1]\), and is extension closed, so it contains the cone. This uses derived reduction, including its adjacent-degree torsion term. The stalk-support upper test is the same whether that cone is viewed over \(\mathcal O\) or over \(k\). \(\square\)

Apply the torsion case of Theorem 4.1 to this reduction. Exactness and \(\mathcal O\)-linearity of \(Rf_*\) carry (4.5) to its coefficient cone. With \(M_n=\mathcal H^n(Rf_*L)\), its long exact sequence gives

\[
M_n/\pi M_n\hookrightarrow
\mathcal H^n\bigl(Rf_*(L\otimes^Lk)\bigr).
\tag{4.6}
\]

At any point of transcendence degree greater than \(-n\), the right stalk vanishes by the upper test. Here the normalized coefficient fibre of \(M_n\) is finite over \(\mathcal O\): BV.1 puts \(Rf_*L\) in the complete constructible category, BQ.3 identifies its cohomology with a strict system, and BP.1 supplies the finite module on each stratum. The quotient in (4.6) has that module modulo \(\pi\) as its fibre. Hence a zero quotient fibre forces the integral fibre to be zero. To spell out this use of Nakayama, choose generators \(m_1,\ldots,m_t\). The equality \(M=\pi M\) expresses their column as \(\pi C\) times itself. The determinant of \(I-\pi C\) is a unit; its adjugate therefore forces every generator to vanish. This proves the support bound on \(M_n\). Rationalizing, with the required image comparison, proves (4.2) over \(E\). Descent to a finite coefficient field and exact faithful scalar extension give the \(\overline{\mathbb Q}_\ell\) statement. Applying that statement to \(F[s]\), where \(s=\dim\operatorname{Supp}F\), recovers (4.1) for rational adic ordinary sheaves.

The [adic-sheaf lesson](course:AG-LTF/l-adic-sheaves-and-their-cohomology#4-changing-the-coefficient-field) and [pro-étale lesson](course:AG-LTF/the-pro-etale-site-and-l-adic-complexes#4-completion-remembers-a-complex) remain complementary coefficient references. The geometric inputs are the first lesson's BV.1, BV.4, BW.7 and BX.7, with the exact maps specified above. In particular (BX.22) identifies rationalization of the actual ordinary image, and its exceptional adjunction supplies the other restriction test. A bare inverse limit of torsion vanishing is still not the argument: (4.6) uses the finite normalized coefficient fibres before rationalization. This field-level route does not assert those finiteness and comparison hypotheses for the strict-local generic limits in nearby cycles, Lemma B.1.

### The classical affine support estimate

For separated finite-type complex varieties and bounded algebraically constructible complexes of finite-dimensional vector spaces over any field, [Theorem A.3](#a-5-the-relative-affine-bound) proves the relative affine bound directly. Its support consequence (A.16) is (4.1), including coefficient systems not obtained from étale sheaves. The argument uses the original normal Morse pairs, an explicit strictly plurisubharmonic exhaustion, and the transverse ordinary-image comparison (A.11).

The unrestricted analytic Stein setting has a separate scope. A deduction there uses Morse exhaustion geometry and the microlocal Stein argument, together with the ordinary/microlocal comparison and transverse restriction. Those general analytic comparisons remain additional hypotheses. Appendix A proves the classical algebraic affine conclusions without them.

## 5. Extensions and the remaining degree intervals

Combining the dimension bounds in Section 2 with the affine bounds in Section 4 gives the following precise ranges for a perverse input \(P\).

| Map \(f\) | Possible perverse degrees of \(Rf_*P\) | Possible perverse degrees of \(Rf_!P\) |
|---|---|---|
| Fibres of dimension at most \(d\) | At least \(-d\) | At most \(d\) |
| Affine, with the same fibre bound | \([-d,0]\) | \([0,d]\) |
| Proper, with the same fibre bound | \([-d,d]\) | \([-d,d]\) |
| Finite | \(0\) | \(0\) |

The affine row holds in the classical algebraic and rational adic settings of Section 4; Appendices A–C supply its affine and coefficient arguments. For an affine quasi-finite map, \(d=0\), so both images are t-exact. In particular an affine open immersion \(j:U\hookrightarrow X\) gives exact functors
\(j_!,Rj_*:\mathcal P(U)\to\mathcal P(X)\).
To see exactness on hearts, regard a short exact sequence as its distinguished triangle; the perverse cohomology sequence of its image has only degree zero, and is again short exact.

For a local calculation that does not require the general classical Artin theorem, take \(j:\mathbb C^*\hookrightarrow\mathbb C\), \(A=\Lambda[1]\), and \(i:\{0\}\hookrightarrow\mathbb C\). A circle has cellular cochains \(\Lambda\) in degrees zero and one with zero differential. The earlier boundary triangle and recollement therefore give

| Object | Degrees and values of its stalk at zero | Degrees and values of its costalk at zero |
|---|---|---|
| \(Rj_*A\) | \(\Lambda\) in \(-1,0\) | Zero |
| \(j_!A\) | Zero | \(\Lambda\) in \(0,1\) |
| \(\Lambda_{\mathbb C}[1]\) | \(\Lambda\) in \(-1\) | \(\Lambda\) in \(1\) |

For the middle row use \(i^!j_!A\simeq i^*Rj_*A[-1]\); for the last use the oriented real two-dimensional ball. All three objects restrict to \(A\) on the open stratum. The upper stalk and lower costalk tests show directly that each is perverse. The adjunction map from the constant shifted sheaf to \(Rj_*A\) is an isomorphism in degree \(-1\); its only remaining cone group is \(i_*\Lambda\) in degree zero. It gives

\[
0\to\Lambda_{\mathbb C}[1]\to Rj_*A\to i_*\Lambda\to0.
\tag{5.1}
\]

Dualizing in this classical field setting gives

\[
0\to i_*\Lambda\to j_!A\to\Lambda_{\mathbb C}[1]\to0.
\tag{5.2}
\]

The first sequence cannot split: a direct summand \(i_*\Lambda\) would give a nonzero costalk in degree zero to an object with zero costalk. The second cannot split because such a summand would give a nonzero stalk to \(j_!A\). The image of \(j_!A\to Rj_*A\) is \(\Lambda_{\mathbb C}[1]\), so this is the intermediate extension. The boundary contribution has moved from a quotient to a subobject.

Affineness can also be measured by a finite cover. Suppose the inverse image of every affine open of \(Y\) admits a cover by \(c+1\) affine opens. Their intersections are affine because \(X\) is separated. The augmented alternating Čech complex is exact stalkwise: choose an open containing the point and insert its index to contract the augmented complex. After deriving sections, this gives a finite tower for \(Rf_*K\), whose degree-\(q\) layers are images from intersections shifted by \([-q]\), for \(0\le q\le c\). The maps from those intersections to the affine target are affine. For upper \(K\), Theorem 4.1 puts their unshifted images in \({}^pD^{\le0}\); the shifts put every layer in \({}^pD^{\le c}\). Extension closure and then duality give

\[
Rf_*({}^pD^{\le0})\subset{}^pD^{\le c},\qquad
Rf_!({}^pD^{\ge0})\subset{}^pD^{\ge-c}.
\tag{5.3}
\]

These are cover bounds, with the same Artin qualifications. They explain how an arbitrary open immersion can have an upper amplitude larger than its zero fibre dimension.

## 6. Remove a hyperplane and compute the error

Let \(X\) be proper, \(i:Y\hookrightarrow X\) closed, and \(j:U\hookrightarrow X\) its affine complement. A projective variety with a hyperplane section is the main example. For a perverse \(K\), the error in restricting cohomology to \(Y\) is measured by the localization triangle

\[
j_!j^*K\longrightarrow K\longrightarrow i_*i^*K\longrightarrow.
\tag{6.1}
\]

Since \(X\) is proper, cohomology of the first term is compactly supported cohomology on \(U\). The exact sequence around restriction is

\[
H_c^n(U,j^*K)\longrightarrow H^n(X,K)
\longrightarrow H^n(Y,i^*K)\longrightarrow H_c^{n+1}(U,j^*K).
\tag{6.2}
\]

**Theorem 6.1 (weak Lefschetz).** Under the affine compact-support vanishing established subject to the inputs in Section 4, the middle map in (6.2) is an isomorphism for \(n<-1\), and injective for \(n=-1\).

**Proof.** Open restriction is t-exact, so \(j^*K\) is perverse. Equation (4.3) kills the two outside terms when \(n\) and \(n+1\) are negative. At \(n=-1\), it still kills the first term, which proves injectivity. \(\square\)

No perversity of the unshifted closed restriction \(i^*K\) was required. If \(X\) is smooth projective of dimension \(d\), substitute \(K=\Lambda_X[d]\) and write \(m=n+d\). The conclusion becomes

\[
H^m(X,\Lambda)\longrightarrow H^m(Y,\Lambda)
\quad\text{is an isomorphism for }m<d-1,
\quad\text{and injective for }m=d-1.
\tag{6.3}
\]

For a smooth hyperplane section this is ordinary weak Lefschetz. At the classical field-coefficient scope, Theorem A.3 supplies its affine premise. The adic conclusion retains the exact coefficient and geometric hypotheses of Section 4.

## 7. Exercises and solutions

**Exercise 1 (easy).** For \(j:\mathbb C^*\hookrightarrow\mathbb C\), verify the perversity of \(Rj_*\Lambda[1]\) from the point tests, and identify its quotient by \(\Lambda_{\mathbb C}[1]\).

**Solution.** Write the cellular cochains of the punctured disc as the two-term complex \([\Lambda\xrightarrow{0}\Lambda]\) in degrees zero and one. After shifting by one, the stalk degrees are \(-1,0\), meeting the upper point bound. The costalk is zero because \(i^!Rj_*=0\), meeting the lower point bound. On the open stratum the object is the required shifted local system, so both tests hold everywhere. The map from the constant shifted sheaf identifies the degree-minus-one stalk and is an isomorphism off zero. Its cone has only \(\Lambda\) in degree zero at the origin; thus it is \(i_*\Lambda\). Since the three terms lie in the perverse heart, this cone is the asserted quotient. This calculation does not invoke the general affine theorem.

**Exercise 2 (easy).** Compute the perverse cohomology of \(Ra_*\Lambda_{\mathbb P^1}[1]\) for \(a:\mathbb P^1\to\mathrm{pt}\), and decide whether \(Ra_*\) is right t-exact.

**Solution.** The classical cell structure has a degree-zero and a degree-two generator, with no adjacent cell for a differential. The geometric étale computation gives the same degrees and a Tate twist on the upper generator. Shifting by one yields precisely \({}^pH^{-1}=\Lambda\) and \({}^pH^1=\Lambda(-1)\), with the twist omitted classically; all other groups are zero. On a point these are ordinary cohomology groups. The smooth-curve sheaf \(\Lambda[1]\) is in the perverse heart, but its image has a positive group. Right t-exactness therefore fails, despite properness.

**Exercise 3 (medium).** Convert the perverse restriction degrees into ordinary weak Lefschetz for a smooth projective \(d\)-fold and a smooth hyperplane section. Determine what happens at the boundary degree.

**Solution.** The shifted constant sheaf on the \(d\)-fold is perverse. Its degree-\(n\) cohomology on either side of restriction is degree \(n+d\) cohomology with unshifted coefficients. The two compact-support groups adjoining restriction in (6.2) have perverse indices \(n\) and \(n+1\). Both vanish for \(n<-1\); just the first is forced to vanish for \(n=-1\). Translating gives an isomorphism for ordinary degree \(m<d-1\) and injectivity for \(m=d-1\). For a curve this boundary is degree zero: constants on a connected curve map diagonally to constants at its hyperplane points, an injective map which need not be onto. The deduction uses the same affine input as Theorem 6.1, supplied classically by Theorem A.3 and with the adic qualifications of Section 4.

**Exercise 4 (medium).** Prove that finite direct image is perverse t-exact, allowing singular source and target.

**Solution.** A finite map has zero-dimensional fibres. Pullback of any ordinary cohomology support therefore has no larger dimension; the upper test gives \(f^*({}^pD^{\le0})\subset{}^pD^{\le0}\). For lower \(B\), adjunction makes every map from an upper object of degree at most \(-1\) to \(Rf_*B\) zero. Hence \(Rf_*\) preserves the lower part. Field duality gives preservation of the upper part by \(Rf_!\). Properness of a finite map identifies these two direct images, supplying both halves for one functor. The perverse cohomology sequence then proves exactness on hearts, and uniqueness of truncation gives commutation with (1.1). This uses the dimension, operation and duality prerequisites, without an Artin-vanishing step.

**Exercise 5 (hard).** Derive positive-degree affine vanishing for every \(K\in{}^pD^{\le0}(U)\) directly from ordinary Artin vanishing. Explain the compact-support consequence and the absence of a degree-zero concentration claim.

**Solution.** Ordinary Artin vanishing bounds cohomology of an ordinary sheaf by the dimension of its support. For \(F=\mathcal H^bK\), that dimension is at most \(-b\), so
\(H^a(U,\mathcal H^bK)=0\) whenever \(a>-b\).
In the ordinary hypercohomology spectral sequence, every term of total degree \(n>0\) satisfies this inequality and vanishes on its second page. Every later subquotient in that total degree is zero. Boundedness supplies a finite filtration of the abutment; an iterated extension of zero groups is zero. Thus \(H^n(U,K)=0\) for \(n>0\).

For a perverse \(P\), its field dual is again perverse. The identity
\(H_c^n(U,P)^\vee=H^{-n}(U,D_UP)\)
then gives compact-support vanishing for \(n<0\). On \(\mathbb A^r\), however, the perverse sheaf \(\Lambda[r]\) has an ordinary global group \(\Lambda\) in degree \(-r\) and a compact-support group \(\Lambda(-r)\) in degree \(r\). Classically these follow by contraction and the one-point compactification \(S^{2r}\); the geometric étale versions use affine-space cohomology and smooth duality. They exhibit the two permitted sides of the bounds. Neither functor is asserted to concentrate in degree zero. The classical ordinary Artin premise is (A.16); the étale and adic premises have the precise coefficient scopes stated in Section 4.

## Appendix A. Stratified Morse bounds and the classical affine theorem

Let \(k\) be any field. All varieties in this appendix are separated and of finite type over \(\mathbb C\); coefficients are bounded complexes with finite-dimensional algebraically constructible cohomology. Stratum dimensions are complex dimensions. In particular, the upper perverse condition on a stratum \(S\) is

\[
 F_x\in D^{\leq-\dim S}(k)\qquad(x\in S).
 \tag{A.1}
\]

The same local degree arguments apply to bounded weak coefficients whenever the indicated finite algebraic stratification and coefficient-transport hypotheses hold. Only the finite-dimensional category is needed for the duality and relative conclusions below.

### A.1. The original normal pairs give the upper degree bound

We use the actual normal-pair constructions in Normal Morse coefficients, TMC and E07, NC and HNC, HB, and CLF1–CLF9. The controlled tubes, lifts and flows used there are also proved in Constructible complexes, Appendix I; their coefficient comparison is J.1. Here are the precise maps and degree consequences of those constructions.

At \(x\in S\), with \(d=\dim S\), choose a complex normal slice, a sufficiently small closed distance ball \(B\) in it, and a holomorphic function \(g\) with generic normal differential and \(g(x)=0\). Generic means that the differential annihilates \(T_xS\) but does not annihilate a limiting tangent plane of an incident larger stratum. For a small nonzero value \(w\), put \(L=B\cap\{g=w\}\). The normal object is

\[
 N_{S,g}(F)=\operatorname{Fib}\bigl(F_x\longrightarrow R\Gamma(L;F)\bigr).
 \tag{A.2}
\]

The arrow is restriction from \(B\), using the actual central restriction isomorphism \(R\Gamma(B;F)\simeq F_x\). HB5 and HB10–HB14 prove that assertion and identify the same fibre with the real normal-band object. HNC compares the prescribed slice, distance ball and value by proper pair maps and their coefficient endpoint arrows. Transport may have monodromy; no path-independent identification is required for a degree bound.

For these algebraic strata, the geometric exceptional-set hypothesis of CLF1 has an elementary algebraic verification. Work in an affine ambient space \(M\) of dimension \(n\), and split the finitely many strata into their irreducible components. For a smooth stratum \(R\), its conormal bundle is algebraic of dimension \(n\): in a smooth chart its equations say that the covector annihilates the tangent rows, and it has rank \(n-\dim R\) over \(R\). Its closure \(C_R\subset T^*M\) is irreducible of the same dimension. The part over \(\overline R\setminus R\) is a proper closed subset, so has dimension at most \(n-1\). The finite union of these parts has a finite decomposition into smooth algebraic pieces of real dimension at most \(2n-2\), by K.1 and K.6. This is the exceptional set needed in CLF3's joint choice of slice value and Morse perturbation. In particular, no microsupport-detection or involutivity theorem is needed here.

The resulting CLF17–CLF18 filtration computes the ordinary cohomology of the *prescribed* complex link \(L\). For an incident original stratum \(R\) of dimension \(r\), its quotients have the form

\[
 N_{R,g_R}(F)[-\tau_R],\qquad 0\leq\tau_R\leq r-d-1.
 \tag{A.3}
\]

Indeed, the induced stratum in the complex link has dimension \(r-d-1\). A strictly plurisubharmonic Morse function has negative index at most that dimension: a larger negative real subspace would meet its image under multiplication by \(i\), contradicting the positivity of the Levi sum. E07 compares its original radial sublevel pair with the normal-band pair times the negative tangential disk. TMC7 computes the relative cohomology of that product as the normal complex shifted by minus the negative index. NC, HB and HNC identify this with the original \(R\)-normal object. All these are maps of the restriction diagrams; they do not replace a relative arrow by an abstract vector-space isomorphism. The collar and finite closed-cover argument in CLF5 and CLF8 gives the filtration itself, with zero initial term and the actual restriction maps.

**Lemma A.1.** Condition (A.1) implies

\[
 N_{S,g}(F)\in D^{\leq-d}(k)
 \tag{A.4}
\]

for every original stratum and every allowed generic normal pair.

**Proof.** Work in a chart meeting finitely many strata and induct downwards in their dimensions. When no larger stratum is incident, the link is empty and the normal object is \(F_x\). Otherwise assume the assertion for the incident larger strata. Every quotient in (A.3) lies in

\[
 D^{\leq-r+\tau_R}\subset D^{\leq-d-1}(k).
\]

Finite extensions give \(R\Gamma(L;F)\in D^{\leq-d-1}\). The fibre triangle (A.2) and \(F_x\in D^{\leq-d}\) imply (A.4), since the shifted link \(R\Gamma(L;F)[-1]\) also lies in \(D^{\leq-d}\). The finite local induction applies at every point. It proves an upper degree assertion for the actual normal objects, independently of the existence of perverse truncation functors. \(\square\)

### A.2. Exhaustions on affine spaces and ball products

Consider either \(M=\mathbb C^n\), or

\[
 M=B_\epsilon^a\times\mathbb C^b,
 \qquad B_\epsilon^a=\{z\in\mathbb C^a:|z|<\epsilon\}.
\]

Let \(Z\) be a closed algebraic subset of the corresponding full affine space, restricted to \(M\). Give it a finite algebraic Whitney stratification, restricted to this open set. The coefficient complex is the restriction of an algebraically constructible complex and satisfies (A.1) there. When \(a=0\), use the affine-space case. For positive \(a\), set

\[
 \rho(z,w)=\frac1{\epsilon^2-|z|^2}+|w|^2.
 \tag{A.5}
\]

This is strictly plurisubharmonic: the first summand is an increasing convex function of \(|z|^2\), with positive first derivative, and the second has positive definite Levi form in the \(w\)-directions. Its sublevels are compact in \(M\). In the affine case use \(\rho=|z|^2\).

There is a real linear form \(\alpha\), as small as desired, such that \(\varphi=\rho+\alpha+C\) is nonnegative, proper and strictly plurisubharmonic, and all its stratum-critical points are Morse with generic original normal covectors. Properness holds for every fixed \(\alpha\): the ball variables are bounded, and completing the square in the affine variables bounds their linear contribution below by \(-\frac12|w|^2-C_\alpha\). The additive constant makes the function nonnegative. A linear form does not change the Levi form.

We prove the genericity assertion. Let \(N=\dim_{\mathbb C}M\). The exceptional conormal set described in A.1 has real smooth pieces of dimension at most \(2N-2\). The map

\[
 (x,\lambda)\longmapsto\operatorname{Re}\lambda-d\rho_x
 \tag{A.6}
\]

from those pieces to the \(2N\)-dimensional space of linear forms has measure-zero image. On each compact smooth chart it is Lipschitz; a mesh of size \(\delta\) gives \(O(\delta^{-q})\) image balls of radius \(O(\delta)\) for \(q<2N\), so their total outer \(2N\)-volume tends to zero. Countably many compact charts cover the set.

For a stratum \(S\), the critical incidence

\[
 E_S=\{(x,\alpha):d(\rho+\alpha)_x|_{T_xS}=0\}
\]

is smooth of real dimension \(2N\), because differentiation in \(\alpha\) gives every covector on \(T_xS\). A critical point of \(\varphi|_S\) is nondegenerate exactly when the projection \(E_S\to\mathbb R^{2N}\) has invertible differential: the kernel of that differential is the kernel of the tangential Hessian. The equal-dimensional critical-value argument in CLF3 applies directly. Explicitly, on a compact cube, uniform continuity of the derivative places the image of each small cube meeting the critical set in a box with \(2N-1\) sides \(O(\delta)\) and one side \(o(\delta)\). Summing over \(O(\delta^{-2N})\) cubes proves measure zero. Countably many charts and finitely many strata leave a null exceptional set. Choose \(\alpha\) outside this set and the images (A.6).

The chosen covector at every critical point is generic against all incident upper tangent limits. Otherwise orthogonal projection of that covector onto the conormal planes of an approaching upper stratum would put it in that upper stratum's boundary conormal set, contrary to (A.6). The critical set is finite in every compact sublevel. An accumulating sequence on one stratum would either converge to a nondegenerate critical point on that stratum, contradicting its isolation, or converge to a lower stratum and give exactly such a boundary conormal. The derivatives of \(\varphi\) are bounded near any limit in \(M\), so the limiting covector exists. Thus the critical values are locally finite.

### A.3. Ordinary cohomology and the degree-one limit

**Lemma A.2.** In the setting of A.2,

\[
 H^q(Z;F)=0\qquad(q>0).
 \tag{A.7}
\]

**Proof.** Choose increasing regular levels \(t_i\to\infty\), with \(t_0<0\), crossing at most one critical value at each step, and put \(W_i=Z\cap\{\varphi<t_i\}\), \(A_i=R\Gamma(W_i;F)\). All points at a repeated critical value are treated together. The original-pair comparison and the finite closed-cover excision in CLF5 identify the fibre of the actual restriction \(A_i\to A_{i-1}\) with a finite sum of

\[
 N_{S,g}(F)[-\tau],\qquad \tau\leq\dim S.
 \tag{A.8}
\]

This application only uses a compact sublevel band. Outside disjoint small critical balls a controlled lift of \(-d/dt\) retracts the band to its lower end, including the sphere interfaces; the relative complexes of the exterior and those interfaces vanish. Inside each ball E07, NC and HB give (A.8). The strictly plurisubharmonic index bound is the same negative-subspace argument as in A.1. A collar at a regular endpoint identifies the closed-sublevel calculation with \(W_i\) by actual coefficient transport. It fixes the entire lower part, so critical points below the band cause no additional requirement on the lift.

By Lemma A.1 each object in (A.8) lies in \(D^{\leq0}\). Starting with \(A_0=0\), the fibre triangles therefore give

\[
 H^q(A_i)=0\ (q>0),\qquad
 H^0(A_i)\twoheadrightarrow H^0(A_{i-1}).
 \tag{A.9}
\]

The surjectivity is essential. To pass to \(Z=\bigcup_iW_i\), take a bounded-below injective resolution \(I\) of \(F\), and set \(E_i=\Gamma(W_i;I)\). Restrictions of injectives to opens remain injective, since extension by zero is exact. Injective sheaves are flasque, so the restriction maps of these complexes are degreewise surjective. Consequently

\[
 0\longrightarrow\Gamma(Z;I)\longrightarrow\prod_iE_i
 \xrightarrow{\Delta}\prod_iE_i\longrightarrow0,
 \qquad \Delta(a)_i=a_i-r_i(a_{i+1})
 \tag{A.10}
\]

is exact. Its kernel is the complex of compatible sections, which glue on the open union. For surjectivity, solve \(a_i-r_i(a_{i+1})=b_i\) successively using the surjective restrictions. Products of vector spaces are exact, so the cohomology sequence has kernel term \(\ker(\Delta:\prod H^q(A_i)\to\prod H^q(A_i))\) and cokernel term \(\operatorname{coker}(\Delta:\prod H^{q-1}(A_i)\to\prod H^{q-1}(A_i))\). For \(q>1\) both vanish by (A.9); for \(q=1\) the cokernel vanishes by the same recursive solution using the surjectivity in degree zero. This proves (A.7). It is the actual restriction-limit argument, also proved in Microlocal types and Stein cohomology, the ordinary-section limit; here the local bounds came directly from ordinary perverse stalk conditions. \(\square\)

In particular, for an affine complex variety \(Z\), ordinary upper-perverse coefficients have no positive cohomology. For finite-dimensional coefficients Verdier duality gives the complementary compact-support assertion: the dual of \(R\Gamma_c(Z;F)\) is \(R\Gamma(Z;D_ZF)\), and duality interchanges the perverse halves. Over a field the linear dual detects vanishing, so \(F\in{}^pD^{\geq0}\) implies \(H_c^q(Z;F)=0\) for \(q<0\). These duality maps and constructibility are Constructible complexes, H.6 and K.8.

### A.4. The transverse ordinary-image comparison

Let \(f:X\to Y\) be affine. Locally on the target, \(Y\) is affine and \(X\) is a closed subvariety of \(Y\times\mathbb A^m\): finitely many generators of its coordinate algebra give this embedding. Let \(\overline X\) be its closure in \(Y\times\mathbb P^m\), with open inclusion \(j:X\hookrightarrow\overline X\) and proper projection \(\overline f:\overline X\to Y\). Properness in the usual topology follows from compactness of projective space. Choose the compatible finite algebraic Whitney stratifications of K.7, respecting the boundary and the cohomology strata of \(F\). Every source stratum maps submersively onto a target stratum.

Fix \(y\) in a target stratum \(T\) of dimension \(d\). In an affine ambient embedding of \(Y\), choose \(d\) complex linear coordinates \(h\), translated to vanish at \(y\), whose differential is invertible on \(T_yT\). On every source stratum over \(y\), \(h\overline f\) is submersive. This remains true on every stratum over a sufficiently small neighborhood of \(y\). Indeed, Whitney \(a\) includes the tangent space of a limiting lower stratum in every upper tangent limit; a sequence of rank failures converging to a point over \(y\) would contradict surjectivity on that lower tangent space. Cover the compact fibre by finitely many such neighborhoods. Properness then permits one target neighborhood whose whole inverse image lies in their union. The same argument makes \(h\) submersive on all target strata near \(y\).

Write \(Y_0=Y\cap\{h=0\}\), \(\overline X_0=\overline X\times_Y Y_0\), \(X_0=X\times_Y Y_0\), and \(F_0=F|_{X_0}\). All statements here may be restricted to that target neighborhood. There is a canonical isomorphism

\[
 (Rf_*F)|_{Y_0}\xrightarrow{\sim}R(f_0)_*F_0.
 \tag{A.11}
\]

Here is its ordinary open-image step. A stratified submersion \(h\overline f\) has a local product with its zero fibre, preserving the original strata and the boundary. Use compatible controlled lifts of its real coordinate fields, compose their small flows in a fixed order, and reverse them in the opposite order. The common open flow domain contains a product of a neighborhood in the zero fibre and a sufficiently small coordinate ball: continuity and a smaller compact time box give a common existence interval for this finite list of forward and reverse flows. These maps are inverse because each flow changes precisely its own base coordinate. Their product image is a neighborhood, and the construction can be made inside any prescribed neighborhood of the point. The base coordinates are the actual \(h\overline f\), so its central slice is the specified \(\overline X_0\). The construction uses I.4–I.5, not properness of the open immersion.

On this product, \(X\) is the product of its central open part with the base ball. The coefficient transport of J.1, or NMG5, identifies \(F\) with pullback of its central restriction, naturally on smaller such neighborhoods. The contraction of the base ball is stratum-preserving. Its proper compact-interval evaluation diagram identifies the actual restriction of ordinary sections to the central slice with an isomorphism. Taking the neighborhood colimit therefore proves

\[
 (Rj_*F)|_{\overline X_0}\xrightarrow{\sim}R(j_0)_*F_0.
 \tag{A.12}
\]

The map is the ordinary base-change map: both its adjunction and the product comparison restrict sections to the same central open subset. This stalk check determines the isomorphism and retains its naturality. Applying proper base change to \(\overline f\), then (A.12) and composition of derived direct images, proves (A.11). Proper base change is H.2. In particular, (A.11) does not identify a nonproper ordinary-image stalk with the cohomology of its geometric fibre.

The source slice cuts an original stratum \(S\) of dimension \(r\) transversely in dimension \(r-d\). Tangent-kernel continuity and the Taylor secant argument, as in NMG1 and NMG6, give the induced Whitney strata. If \(F\) satisfies (A.1), then

\[
 F_0[-d]\in{}^pD^{\leq0}(X_0)
 \tag{A.13}
\]

on this neighborhood: its stalk upper bound is \(-r+d=-(r-d)\). Further algebraic Whitney refinement preserves this upper bound because stratum dimensions can only decrease. Thus a global refinement adapted to the algebraically constructible restriction \(F_0\) is permitted, even if the transverse description was only needed near this fibre. This proves the required upper restriction assertion directly from stalks; no exceptional noncharacteristic-restriction theorem is used in (A.13).

### A.5. The relative affine bound

**Theorem A.3.** For every affine morphism of complex varieties and every field \(k\),

\[
 Rf_*({}^pD^{\leq0}_c(X;k))\subset{}^pD^{\leq0}_c(Y;k),
 \qquad
 Rf_!({}^pD^{\geq0}_c(X;k))\subset{}^pD^{\geq0}_c(Y;k).
 \tag{A.14}
\]

**Proof.** The images are bounded algebraically constructible by K.8. Fix \(y,T,d,h\) as in A.4. Intersect the affine normal plane \(\{h=0\}\) with successively smaller Euclidean balls about \(y\). The inverse image under \(f_0\) is a closed algebraic set restricted to a ball times an affine space, using the closed embedding \(X\subset Y\times\mathbb A^m\). Its coefficients \(F_0[-d]\) satisfy (A.1) by (A.13). Lemma A.2 gives

\[
 H^q\bigl(f_0^{-1}(B\cap Y_0);F_0\bigr)=0
 \qquad(q>-d).
 \tag{A.15}
\]

The inverse images in this formula are whole inverse images of neighborhoods, not single fibres. The injective stalk formula and exact filtered colimits turn (A.15) into the same bound for \((R(f_0)_*F_0)_y\). By (A.11) it is the bound for \((Rf_*F)_y\). Since \(y\) was arbitrary, the upper stalk characterization on every target stratum proves the first inclusion. The second follows from \(D_YRf_!\simeq Rf_*D_X\), biduality and interchange of the two perverse halves. \(\square\)

For an ordinary constructible sheaf \(A\) with support of dimension \(e\), the complex \(A[e]\) satisfies the upper perverse stalk bound: every stratum on which it is nonzero has dimension at most \(e\). Apply Theorem A.3 to \(A[e]\). The support characterization of the upper perverse half gives

\[
 \dim\operatorname{Supp}R^qf_*A\leq e-q.
 \tag{A.16}
\]

This is exactly (4.1), for all the classical field coefficients specified there. Taking the target to be a point gives ordinary Artin vanishing and its compact-support dual. Combining (A.14) with Section 2 gives the full affine row of Section 5, including both exact extension functors for an affine open immersion. No comparison with étale coefficients is required for these classical conclusions.

## Appendix B. Integral dimension cuts and change of coefficients

Let \(k_0\) be a finite field or an algebraically closed field, as in the arithmetic setting of the first lesson. Let \(X\) be separated and of finite type over \(k_0\). Retain the complete discrete valuation ring \(\mathcal O\), uniformizer \(\pi\), finite residue field \(\kappa\), and fraction field \(E\), with the residue characteristic invertible in \(k_0\). Write \(\mathscr C_X\) for the bounded complete constructible category of Constructible complexes, BV. We use its standard truncations, completed inverse image, exceptional inverse image and structural duality. All the operations below are restricted to this category.

The object called lisse on a smooth piece will have a pro-étale local model given by a bounded complex of finite free \(\mathcal O\)-modules. BO.1–BO.6 prove this local description when the first reduction has locally constant cohomology. Its cohomology may have \(\pi\)-torsion. In the completed-ring presentation of BW the unit is \(R_S\), and these are ordinary perfect complexes locally over \(R_S\).

### B.1. Exceptional restriction between smooth pieces

Let \(b:T\hookrightarrow S\) be a locally closed immersion of smooth pure-dimensional schemes, with

\[
 s=\dim S,\qquad t=\dim T,\qquad c=s-t.
 \tag{B.1}
\]

For a lisse complex \(L\) on \(S\), there is a natural comparison

\[
 b_c^!L\simeq b_c^*L(-c)[-2c].
 \tag{B.2}
\]

Here is its proof, including the coefficient calculation. Smooth orientation in BV.4 identifies the two structural dualizing objects with

\[
 \Omega_S=\mathbf1_S(s)[2s],\qquad
 \Omega_T=\mathbf1_T(t)[2t].
 \tag{B.3}
\]

For a local finite free model \(P\), let \(P^\vee=\operatorname{Hom}_{\mathcal O}^{\bullet}(P,\mathcal O)\), with the usual Hom differential. Its evaluation and the signed double-evaluation map identify \(P^{\vee\vee}\) with \(P\) term by term. Finite sums make these identifications commute with coefficient pullback. Thus, writing \(L^\vee=R\mathcal Hom(L,\mathbf1_S)\), the natural evaluation comparisons give

\[
 b_c^*(L^\vee)\simeq(b_c^*L)^\vee,\qquad
 (L^\vee)^\vee\simeq L.
 \tag{B.4}
\]

The comparisons are defined before choosing a free model, so their local isomorphisms glue. They also commute with the invertible Tate objects. BV.7 gives the actual dual exchange \(b_c^!=\mathbb D_Tb_c^*\mathbb D_S\). Substituting (B.3)–(B.4) gives

\[
 \begin{aligned}
 b_c^!L
 &\simeq \mathbb D_T\bigl(b_c^*(L^\vee)(s)[2s]\bigr)\\
 &\simeq (b_c^*L)^{\vee\vee}(t-s)[2t-2s]\\
 &\simeq b_c^*L(-c)[-2c],
 \end{aligned}
 \tag{B.5}
\]

which proves (B.2). These are the evaluation and adjunction maps of BV.6–BV.7, transported by BW.4. The statement concerns smooth pieces over the fixed field. It does not assert absolute purity for arbitrary regular schemes.

Integral torsion illustrates why this argument uses complexes. On a geometric point,
\(R\operatorname{Hom}_{\mathcal O}(\mathcal O/\pi,\mathcal O)\)
is \((\mathcal O/\pi)[-1]\). Indeed the free resolution
\([\mathcal O\xrightarrow{\pi}\mathcal O]\) in degrees \(-1,0\)
has dual in degrees \(0,1\), with only degree-one cohomology.
Integral duality therefore does not preserve the ordinary heart even on a
point. Formula (B.5) uses double evaluation, not such a preservation claim.

### B.2. Refinement of the stratum tests

A finite collection of objects of \(\mathscr C_X\) admits a finite smooth partition on which both its restrictions and exceptional restrictions are lisse. To construct it, include each object's structural dual in the collection. BV.5–BV.6 make these duals bounded constructible. Their first reductions and those of the original objects have finitely many constructible cohomology sheaves. A common finite refinement makes those sheaves locally constant. Since \(k_0\) is perfect, the dense smooth-open construction of M.1 permits smooth pieces: take dense smooth opens in the reduced irreducible components, remove their intersections and the non-lisse loci, and repeat on the closed complement. At each step the dimension drops on each remaining component. Noetherian finite dimension makes the process finite. Nilpotent thickenings do not change the coefficient topoi, by BX.2.

For a resulting piece \(a:S\hookrightarrow X\), BO supplies the local finite free models of \(a_c^*K\) and \(a_c^*\mathbb D_XK\). The identity

\[
 a_c^!K=\mathbb D_Sa_c^*\mathbb D_XK
 \tag{B.6}
\]

and (B.3)–(B.4) give such a model of \(a_c^!K\) too. Thus the finite partition has the required two properties. Intersections of two finite partitions have a further finite smooth refinement by the same construction.

On such a partition define the two tests

\[
 \begin{aligned}
 K\in\mathscr U_X
 &\Longleftrightarrow a_c^*K\in D^{\leq-\dim S}
                 \quad\hbox{for every }S,\\
 K\in\mathscr V_X
 &\Longleftrightarrow a_c^!K\in D^{\geq-\dim S}
                 \quad\hbox{for every }S.
 \end{aligned}
 \tag{B.7}
\]

They are independent of the chosen adapted partition. First refine one smooth piece \(S\) by smooth pieces \(T\) of codimension \(c\). Ordinary pullback is standard t-exact by BQ.5, so its upper bound changes as

\[
 a_c^*K\in D^{\leq-s}
 \ \Longrightarrow\
 (ab)_c^*K\in D^{\leq-s}\subset D^{\leq-t}.
 \tag{B.8}
\]

Exceptional transitivity and (B.2), applied to the lisse complex \(a_c^!K\), give

\[
 \begin{aligned}
 (ab)_c^!K&\simeq b_c^*(a_c^!K)(-c)[-2c],\\
 a_c^!K\in D^{\geq-s}
 &\ \Longrightarrow\
 (ab)_c^!K\in D^{\geq-s+2c}\subset D^{\geq-t}.
 \end{aligned}
 \tag{B.9}
\]

Both inequalities use \(c\geq0\). Conversely, each connected component of \(S\) has a nonempty open part among its full-dimensional refinement pieces. Their \(c=0\) tests recover the old bounds on that open. The cohomology of the old two restrictions is lisse with a constant coefficient-module type on a connected component, by BO.2 and BO.6. Vanishing on this nonempty open therefore gives vanishing throughout that component. This proves the converse. Passing through a common refinement proves independence for any two adapted partitions.

For the upper condition, the maximum of the dimensions of the strata on which a cohomology sheaf is nonzero is its support dimension. Hence

\[
 \mathscr U_X
 =\{K:\dim\operatorname{Supp}\mathcal H^qK\leq-q
                    \text{ for every }q\}.
 \tag{B.10}
\]

In particular this upper condition uses the normalized cohomology sheaves of BQ, rather than the underived cohomology of a chosen coefficient tower.

### B.3. The integral perverse t-structure

**Theorem B.1.** The pair \((\mathscr U_X,\mathscr V_X)\) is a bounded t-structure on \(\mathscr C_X\).

**Proof.** The required shift inclusions follow directly from (B.7). We prove orthogonality and existence of truncations by dimension induction, using actual open–closed adjunctions from BV.4 and BX.2.

For orthogonality take \(A\in\mathscr U_X\) and \(B\in\mathscr V_X[-1]\), so \(B\) has lower perverse degree at least one. Choose a common adapted partition and a dense open union \(j:U\hookrightarrow X\) of its smooth pieces, with closed complement \(i:Z\hookrightarrow X\) of smaller dimension. On each pure-dimensional component of \(U\), the ordinary upper degree of \(j^*A\) is at most minus its dimension and the ordinary lower degree of \(j^*B\) is at least one minus its dimension. Ordinary truncation orthogonality makes their Hom group zero. On \(Z\), exceptional transitivity and the ordinary restriction tests put \(i^*A\) in \(\mathscr U_Z\) and \(i^!B\) in \(\mathscr V_Z[-1]\). Their Hom group vanishes by induction. Applying \(\operatorname{Hom}(-,B)\) to

\[
 j_!j^*A\longrightarrow A\longrightarrow i_*i^*A\longrightarrow
 \tag{B.11}
\]

and using the two adjunctions proves \(\operatorname{Hom}(A,B)=0\).

To cut an arbitrary \(K\), choose \(U\) adapted to \(K\). On a component of dimension \(s\), put \(U_0=\tau^{\leq-s}j^*K\). Standard truncations of its finite free local model have finite lisse cohomology and remain in \(\mathscr C_U\), by BQ.4. Form

\[
 j_!U_0\longrightarrow K\longrightarrow K_1\longrightarrow,
 \qquad F_0={}^p\tau_Z^{\leq0}i^!K_1,
 \qquad i_*F_0\longrightarrow K_1\longrightarrow B\longrightarrow.
 \tag{B.12}
\]

The closed truncation exists by induction. The octahedron gives

\[
 A\longrightarrow K\longrightarrow B\longrightarrow,
 \qquad j_!U_0\longrightarrow A\longrightarrow i_*F_0\longrightarrow.
 \tag{B.13}
\]

The recollement identities give \(j^*A=U_0\), \(i^*A=F_0\),
\(j^*B=\tau^{\geq1-s}j^*K\) on the component of dimension \(s\), and
\(i^!B={}^p\tau_Z^{\geq1}i^!K_1\).
Refine the closed part to make its finitely many objects adapted. Equations
(B.8)–(B.9) preserve all tests under that refinement. Consequently
\(A\in\mathscr U_X\) and \(B\in\mathscr V_X[-1]\). This is the required
truncation triangle. Its uniqueness and functoriality follow from the
orthogonality just proved, as in Gluing t-structures, A.2.

Finally, on a finite adapted partition every ordinary and exceptional restriction has cohomology in a finite interval. Taking the largest upper endpoint plus the stratum dimension gives an upper perverse bound. Taking the smallest lower endpoint plus that dimension gives a lower perverse bound. Thus every object has finite perverse amplitude. The argument constructs the t-structure on the full complete constructible category and does not require its identification with the bounded derived category of its heart. \(\square\)

### B.4. Rationalization and the upper integral model

Under BX.7, rationalization is standard t-exact, commutes with ordinary restriction and identifies exceptional restriction through its adjunction and closed-support comparison. Thus it carries both tests (B.7) to the corresponding rational tests. It is perverse t-exact. Applying it to a truncation triangle and using uniqueness yields

\[
 ({}^p\tau^{\leq0}L_0)[1/\pi]
 \simeq{}^p\tau^{\leq0}(L_0[1/\pi]).
 \tag{B.14}
\]

For a rational upper-perverse \(K\), BX.6–BX.7 give an integral model \(L_0\). Put \(L={}^p\tau^{\leq0}L_0\). Formula (B.14) gives \(L[1/\pi]\simeq K\). The coefficient triangle

\[
 L\xrightarrow{\pi}L\longrightarrow
 L\otimes_{\mathcal O}^{L}\kappa\longrightarrow L[1]
 \tag{B.15}
\]

places its third object in the upper perverse half: the rotated triangle has outer terms \(L,L[1]\), and that half is extension closed. Its upper support test is unchanged when the \(\kappa\)-complex is regarded as an \(\mathcal O\)-complex. This proves the integral-model and residue-upper assertions of Lemma 4.2.

Only this upper assertion about reduction is used. For example, the same free resolution of \(\mathcal O/\pi\) gives

\[
 (\mathcal O/\pi)\otimes_{\mathcal O}^{L}\kappa
 \simeq\kappa\oplus\kappa[1].
 \tag{B.16}
\]

On a point its two groups lie in degrees \(0,-1\). The integral perverse heart is the ordinary heart there, so derived reduction does not preserve both halves. The coefficient-cone injection (4.6) retains precisely this adjacent-degree term before the finite-module Nakayama argument.

## Appendix C. Affine images at a strict local base

The support estimate can be proved before the higher images are known to be constructible. This distinction matters in passing from ordinary torsion coefficients to the complete integral category of Section 4.

**Theorem C.1.** Let \(f:X\to Y\) be an affine morphism of finite-type schemes over a field \(k_0\), and let \(F\) be a constructible sheaf of finite-dimensional vector spaces over a finite field \(\kappa\) of characteristic invertible in \(k_0\). Put \(e=\dim\overline{\operatorname{Supp}F}\). For every geometric point \(\bar y\) above \(y\in Y\) and every \(q\ge0\),
\[
 (R^qf_*F)_{\bar y}=0
 \quad\text{if}\quad
 q+\operatorname{trdeg}_{k_0}\kappa(y)>e.
 \tag{C.1}
\]
Consequently \(\dim\operatorname{Supp}R^qf_*F\le e-q\). Empty support gives the zero sheaf.

### C.1. The cohomology group that computes the stalk

Restrict to an affine neighbourhood \(Y_0=\operatorname{Spec}B\) of \(y\). Its inverse image is affine. Write
\[
 b=\operatorname{trdeg}_{k_0}\kappa(y),\qquad
 R=\mathcal O^{\mathrm{sh}}_{Y,\bar y}.
 \tag{C.2}
\]
The strict-local formula BA.9 identifies the actual stalk as
\[
 (R^qf_*F)_{\bar y}
 =H^q(X_R,F_R),\qquad
 X_R=X\times_Y\operatorname{Spec}R.
 \tag{C.3}
\]
Here the notation on the right means pullback to the entire strict-local base. BA.5 proves continuity for arbitrary compatible sheaves on qcqs affine-transition limits; the injective slice calculation gives the canonical higher-image map in (C.3).

Let \(i:Z\hookrightarrow X_{Y_0}\) be the reduced closure of the support of the restricted sheaf. It is affine and \(\dim Z\le e\). The unit \(F\to i_*i^*F\) is an isomorphism on every geometric stalk: on \(Z\) it is the identity, and off \(Z\) both sides vanish. Exact closed pushforward, including after base change, therefore gives
\[
 H^q(X_R,F_R)=H^q(Z_R,G),\qquad G=i_R^*F_R.
 \tag{C.4}
\]
This uses only the closed-support sheaf identity, not a constructibility assertion about \(R^qf_*F\).

### C.2. Support models over a separably closed field

Use normalization adapted to an ideal, Corollary 3.2, for \(B\) and the prime of \(y\). It gives a polynomial subalgebra with a distinguished subring
\[
 P_0=k_0[t_1,\ldots,t_b]\longrightarrow B
 \quad\text{such that }y\text{ maps to the generic point of }\operatorname{Spec}P_0.
 \tag{C.5}
\]
In particular every nonzero element of \(P_0\) becomes a unit in \(R\). The chosen geometric point and strict henselization, Theorem 5.1, give a compatible embedding
\[
 L=k_0(t_1,\ldots,t_b)^{\mathrm{sep}}\hookrightarrow R.
 \tag{C.6}
\]

The compatible finite models are those of the cohomological-dimension lesson, Lemma 3.2. Write \(L=\operatorname{colim}_i A_i\) using pointed affine étale neighbourhoods of the generic point of \(\operatorname{Spec}P_0\), and \(R=\operatorname{colim}_j B_j\) using pointed affine étale neighbourhoods of \(y\). Keep the integral component of each \(A_i\) selected by the marking. This is a cofinal choice: the étale \(P_0\)-scheme is smooth over \(k_0\), so its regular local rings are domains and its finitely many components are disjoint open and closed subsets. Thus \(A_i\) injects into \(L\), has dimension \(b\), and its fraction field is finite separable over \(\operatorname{Frac}P_0\).

Index by triples \((i,j,\phi)\), where \(\phi:A_i\to B_j\) induces the prescribed map into \(R\). A finite presentation of \(A_i\) makes every such map factor through a sufficiently late \(B_j\). A common refinement of two \(A_i\)'s, followed by this factorization and the finitely many equations equating the old maps, gives a common receiving triple. The same finite-equation argument equalizes parallel maps. Hence the triple category is filtered, and
\[
 R=\operatorname{colim}_{(i,j,\phi)}
       (B_j\otimes_{A_i}L).
 \tag{C.7}
\]
Surjectivity follows by representing an element in some \(B_j\). For injectivity, represent the finitely many \(L\)-coefficients of a tensor expression at a later \(A_i\), move them across the tensor sign using \(\phi\), and kill the resulting zero element at a later \(B_j\). These refinements also preserve any previously specified finite set of equations.

Set
\[
 Z_{ij}=(Z\times_{Y_0}\operatorname{Spec}B_j)
                  \times_{\operatorname{Spec}A_i}\operatorname{Spec}L.
 \tag{C.8}
\]
These are affine finite-type \(L\)-schemes and \(Z_R=\varprojlim Z_{ij}\), by (C.7). Before the second base change, the scheme is étale over \(Z\), so each of its components \(W\) has dimension at most \(e\). A component not dominating the integral scheme \(\operatorname{Spec}A_i\) disappears upon inverting its nonzero elements. On a dominating component, the finite-type field dimension formula gives
\[
 \dim W_{\operatorname{Frac}A_i}
 =\operatorname{trdeg}_{k_0}k_0(W)-b\le e-b.
 \tag{C.9}
\]
The dimension formula is Theorem 4.2 of the normalization lesson, applied after this localization. Extending the field from \(\operatorname{Frac}A_i\) to \(L\) preserves dimension: a finite normalization map to affine space stays finite and surjective after field extension, and the polynomial dimension is unchanged. Consequently
\[
 \dim Z_{ij}\le e-b.
 \tag{C.10}
\]
If \(e<b\), every component disappears, so every one of these support models is empty. The argument includes singular targets and nonclosed points \(y\); no smoothness of \(Y\) has been assumed.

### C.3. Continuity and the affine bound

Artin vanishing, Theorem 5.1 of the cohomological-dimension lesson, states that an affine finite-type scheme \(V\) over a field \(K\) has torsion cohomological dimension at most \(\dim V+\operatorname{cd}_{\mathrm{tors}}K\). The separably closed field \(L\) has cohomological dimension zero: its étale topos is the topos of sets and its abelian section functor is exact. Thus (C.10) gives
\[
 H^q(Z_{ij},M)=0\qquad(q>e-b)
 \tag{C.11}
\]
for every torsion sheaf \(M\) on \(Z_{ij}\).

For the projections \(p_{ij}:Z_R\to Z_{ij}\), put \(G_{ij}=(p_{ij})_*G\). These are \(\kappa\)-sheaves, although they need not be constructible. A germ and an equality of germs are represented on finite-presentation étale neighbourhoods, which descend to a finite stage. This proves \(G=\operatorname{colim}p_{ij}^{-1}G_{ij}\). Applying BA.5 to that compatible system yields
\[
 H^q(Z_R,G)=\operatorname{colim}_{(i,j,\phi)}
                 H^q(Z_{ij},G_{ij})=0\qquad(q>e-b).
 \tag{C.12}
\]
Together with (C.3)–(C.4), this proves (C.1), including degree zero when \(e<b\). The ordinary direct-image finiteness theorem M.4 makes the higher images constructible at these finite coefficients. On a constructible subset the dimension is the maximum transcendence degree of its generic points. Therefore (C.1) is precisely (4.1). \(\square\)

The absolute Artin input in this proof has no relative-finiteness premise. Its proof in Sections 2–5 of the earlier lesson starts with affine curves and cohomology continuity, proves the proper dimension bound from proper curves and proper base change, and then inducts on affine dimension simultaneously over all fields. At a smooth boundary, the strict local ring contains \(L(f)\) after the local equation \(f\) is inverted; the denominator calculation is explicit in M.1. This lowers the geometric dimension before invoking induction. Compactifying the last affine coordinate puts all positive boundary images on the section at infinity. The two Leray sequences then give the affine bound, including the separate degree-two generic-stalk argument. Thus the order of the proof is curve bounds, absolute affine vanishing, relative support drop, and finally ordinary direct-image constructibility.

The ordinary foundations used in that order have the following earlier proofs: finite pushforward in AX.5, curve cohomology in AK.5, proper base change in BE, and arbitrary compatible-sheaf continuity in BA.5. The first lesson's normality and strict-local algebra arguments and the linked normalization and henselization proofs supply their stated algebraic inputs.

For a basic distinction between (C.3) and a fibre formula, take \(j:\mathbf G_m\hookrightarrow\mathbf A^1\) over an algebraically closed field and the constant sheaf \(\kappa\). The fibre over zero is empty. Nevertheless the strict local ring at zero is a discrete valuation ring, and its punctured spectrum is the spectrum of its fraction field, hence connected. Thus \((j_*\kappa)_{\bar0}=\kappa\), whereas the cohomology of the empty geometric fibre is zero.

The finite-coefficient support estimate and the finite ordinary tower prove the torsion upper bound in (4.2). The integral perverse model of Appendix B, the actual image/reduction comparison and the finite-module calculation (4.6) give its rational-adic version. Appendix A supplies the classical algebraic version. Duality gives the corresponding lower shriek bound in the field-valued perverse categories used here. These arguments concern affine morphisms over the course ground fields; they assert no arbitrary-trait comparison or unrestricted analytic Stein theorem.

## Geometric hypotheses and references

Theorem C.1 proves the finite-coefficient support estimate using strict-local support models, the absolute affine theorem and continuity, with the curve and dimension prerequisites identified there. Integral truncation is constructed in (4.4); the bounded normalized operations, nonproper finiteness, finite-coefficient fibres and rationalization comparisons over fields are those of BV–BX and BP–BQ, as specified in Section 4. Appendix B constructs the compatible integral dimension cuts and proves the smooth-stratum exceptional comparison and refinement independence over the course ground fields. Its proof uses the actual complete-coefficient evaluation, duality and localization maps of BO, BQ and BV–BX. The field-level finiteness theorem does not apply to an arbitrary trait or its strict-local generic limits. Appendix A proves the classical algebraic affine theorem over any field by normal Morse bounds, an exhaustion limit and transverse ordinary-image comparison. The unrestricted analytic Stein deduction retains its separate ordinary/microlocal and restriction hypotheses. The relative orientation and smooth duality used in Section 3 are proved in Lemma 3.0 with its stated arithmetic comparisons; local sections and the coefficient-unit passage are proved in the full-faithfulness argument. Constructibility, finite-type dimension, oriented ball and sphere comparisons, and geometric étale curve and affine-space cohomology are further inputs, with the earlier proof locations specified in Sections 2–4 and Appendices A–C. Their general foundations are not all proved in this lesson.

The sources used for the affine and smooth comparison are the freely accessible versions below. The Bhatt–Blickle–Lyubeznik–Singh–Zhang reference concerns a different characteristic-\(p\) coefficient theory; its subsection 5.1 is a further reading direction and supplies no proof input to the prime-to-characteristic arguments here.

- A. Beilinson, J. Bernstein and P. Deligne, with contributions by O. Gabber, [*Faisceaux pervers*](https://publications.ias.edu/sites/default/files/Faisceaux%20pervers.pdf), freely readable IAS edition; Sections 4.1.1–4.1.5, Remark 4.1.9 and Sections 4.2.3–4.2.5.
- M. A. A. de Cataldo and L. Migliorini, [*The Decomposition Theorem and the topology of algebraic maps*](https://arxiv.org/abs/0712.0349v2), arXiv:0712.0349v2; Section 5.3.
- L. G. Maxim and J. Schürmann, [*Constructible sheaf complexes in complex geometry and applications*](https://people.math.wisc.edu/~lmaxim/handbook.pdf), author-hosted draft of 2 June 2021; Corollary 3.25 and Section 3.5 for normal Morse degree bounds and Artin-type vanishing.
- M. Artin, A. Grothendieck and J.-L. Verdier, [*Théorie des topos et cohomologie étale des schémas*](https://www.normalesup.org/~forgogozo/SGA4/tomes/SGA4.pdf), free Laszlo–Orgogozo transcription of SGA 4; Exposé XIV supplies the torsion affine theorem discussed in the earlier companion.
- The Stacks Project Authors, [Cohomological dimension, §59.95](https://stacks.math.columbia.edu/tag/0F0P), especially Lemma 59.95.5, Proposition 59.95.6 and Lemma 59.95.8 for strict-local models, affine vanishing and relative support.
- The Stacks Project Authors, [Étale local sections of smooth morphisms, Lemma 37.38.6](https://stacks.math.columbia.edu/tag/055U).
- A. Mathew, [*Verdier duality*](https://math.uchicago.edu/~amathew/verd.pdf), free author notes of 29 July 2011; Theorem 4.1 and Corollary 5.5 for the exceptional adjunction and the orientation calculation.
- B. Bhatt, M. Blickle, G. Lyubeznik, A. K. Singh and W. Zhang, [*Applications of perverse sheaves in commutative algebra*](https://arxiv.org/abs/2308.03155), free arXiv version; subsection 5.1 for the separate characteristic-\(p\) setting.
