# Affine morphisms, Artin vanishing and perverse cohomology

*Reconstructed by GPT-6 Astra (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

A direct image can acquire cohomology in two different ways: its fibres can have positive dimension, and sections near a missing boundary can carry higher cohomology. We will calculate both effects before asking what affineness removes. This makes the direction of each perverse inequality visible. The final application cuts a projective variety by a hyperplane: the error in restriction is compactly supported cohomology of the affine complement.

We use the categories of Constructible complexes on algebraic varieties, the truncation construction in [Gluing t-structures](gluing-t-structures.md), and the support tests of [The perverse t-structure](the-perverse-t-structure.md). Coefficients are the classical field coefficients of those lessons, or rational adic coefficients with the qualifications in Section 4. All maps are separated and of finite type. Dimensions are complex or algebraic dimensions; the dimension of an empty support is minus infinity. Our shift convention is \(\mathcal H^q(K[r])=\mathcal H^{q+r}K\). In the étale case, global cohomology is geometric cohomology over an algebraic closure; relative functors retain descent data and Tate twists.

The free author-hosted edition of Beilinson–Bernstein–Deligne, Sections 4.1–4.2, supplies the affine and smooth statements against which we check the hypotheses. The free de Cataldo–Migliorini survey, Section 5.3, supplies a second comparison of operation directions. The proofs below use the earlier programme constructions at the places specified, with unresolved inputs recorded as such.

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
The second summand is the dimension of the generic fibre of \(W\to Z\), at most \(d\). Taking maxima proves (2.1). The dimension formula itself is one of the algebraic prerequisites still to be checked recursively.

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
The orthogonal characterization of the lower half therefore gives the last inclusion. Over our field coefficients, Verdier duality reverses the two perverse halves and exchanges star with shriek. Dualizing the two proved inclusions gives the other two. These last deductions require the precise operation and duality prerequisites, which remain part of the course audit. \(\square\)

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

**Proposition 3.1.** If \(f:X\to Y\) is smooth of pure relative dimension \(r\), then \(f^*[r]\) is t-exact. If all its geometric fibres are connected and nonempty, its restriction to perverse hearts is fully faithful.

**Proof of t-exactness.** Apply (2.1) to each ordinary cohomology sheaf of \(K\in{}^pD^{\le0}(Y)\). The degree \(q\) sheaf of \(f^*K[r]\) has support dimension at most
\(-(q+r)+r=-q\).
Thus the upper test holds. Smooth duality, with the orientation supplied by the complex or étale theory, reads

\[
D_X(f^*K[r])\simeq f^*(D_YK)r.
\tag{3.1}
\]

Again omit the twist classically. Apply the already proved upper bound to \(D_YK\); since twisting does not change support or degrees, duality gives the lower bound. This proves both halves. \(\square\)

**Proof of full faithfulness.** For \(P,Q\in\mathcal P(Y)\), let
\(H=\mathcal H^0R\mathcal Hom_Y(P,Q)\).
On each open or étale neighbourhood, negative derived Hom between heart objects vanishes by t-structure orthogonality. Sheafification shows that the internal Hom complex has no negative ordinary cohomology sheaves. Its degree-zero global cohomology is consequently \(\Gamma(Y,H)\), either by ordinary truncation or by the degree-zero edge of its hypercohomology sequence. Thus

\[
\operatorname{Hom}(P,Q)=\Gamma(Y,H).
\tag{3.2}
\]

The identity \(R\mathcal Hom(P,Q)=D(P\otimes DQ)\) and smooth duality show that pullback commutes with this internal Hom: the relative shifts and twists appear once on each side of the inner dual and cancel. Exactness of ordinary pullback then identifies the morphism sheaf for \(f^*P[r],f^*Q[r]\) with \(f^*H\).

It remains to prove \(H\simeq f_*^{\mathrm{ord}}f^*H\). A smooth surjection has local sections, in the analytic or étale topology. Pull a section of \(f^*H\) back along one such section. On every geometric fibre, \(f^*H\) is the constant sheaf with the value of the corresponding stalk of \(H\); connectedness means its sections have a single value. The pullback along the local section therefore recovers the value on that entire fibre. The same stalk comparison proves that the reconstructed section pulls back to the original one. Nonempty fibres make this reconstruction unique, so the local sections agree on overlaps and glue. Taking global sections in (3.2) proves full faithfulness. The local-section and smooth-duality inputs are required at the coefficient version in use. \(\square\)

Both qualifications on fibres are necessary. A non-surjective open immersion is smooth with nonempty fibres connected wherever they exist, but kills a nonzero perverse sheaf supported in its complement. Pullback from a point to two points sends \(V\) to \((V,V)\); the target allows two independent endomorphisms, whereas pullback supplies only diagonal pairs.

## 4. Why affineness removes the positive degrees

The ordinary support estimate needed here is

\[
\dim\operatorname{Supp}R^af_*F\le
\dim\operatorname{Supp}F-a\qquad(a\ge0)
\tag{4.1}
\]

for affine \(f\) and an ordinary constructible sheaf \(F\). We first deduce the perverse consequence from this precise estimate, then examine its coefficients and proof obligations.

**Theorem 4.1 (affine bounds).** With (4.1) available at the coefficient version in question,

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

For torsion coefficients with torsion prime to the characteristic, the earlier lesson [Cohomological dimension and the Künneth formula](course:ag-etale-cohomology/cohomological-dimension-and-the-kunneth-formula#6-affine-direct-images-lower-support-dimension), Theorem 6.2, writes the relative Artin proof. Its bound applies to every torsion sheaf, using the transcendence degrees of points with nonzero stalks. The proof uses strict-local finite models and affine cohomological-dimension induction; it does not replace a nonproper direct-image stalk by the cohomology of the geometric fibre. On constructible supports the transcendence-degree bound is (4.1). Its own prerequisites remain subject to recursive verification.

For rational adic coefficients we need a separate argument. Let \(E/\mathbb Q_\ell\) be finite, \(\mathcal O\) its valuation ring, \(\pi\) a uniformizer, and \(k=\mathcal O/(\pi)\). We require a bounded normalized constructible integral category with recollement; its operations must preserve the required constructibility and finiteness, and flat rationalization must commute with ordinary and exceptional restriction. The latter exceptional comparison and nonproper image finiteness are still unresolved prerequisites here. Under these hypotheses, the necessary integral truncation can be constructed now, without referring to a later lesson.

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
They give \(j^*A=U_0\), \(i^*A=F_0\), while \(j^*B\) and \(i^!B\) have the positive bounds on their respective pieces. Hence \(A\) is upper and \(B\) is lower of degree at least one for the glued pair. Orthogonality follows from the open ordinary orthogonality and the closed inductive orthogonality by applying Hom to \(j_!j^*A\to A\to i_*i^*A\to\). This is precisely the truncation construction proved in the earlier gluing lesson. Its upper condition is the stalk-support condition; the lower condition uses exceptional restriction. No self-duality of an integral heart is asserted. The finite number of strata and the stated operation hypotheses ensure boundedness and constructibility. Refinement uses the corresponding smooth-stratum restriction and purity comparisons, included among those integral prerequisites.

Choose an integral model \(L_0\) of \(K\), using the rational-model construction in [ℓ-adic sheaves and their cohomology](course:AG-LTF/l-adic-sheaves-and-their-cohomology#4-changing-the-coefficient-field). Flat rationalization commutes with both restriction tests, by the specified comparison hypotheses. It therefore carries a glued truncation triangle to the rational truncation triangle. Uniqueness gives
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

At any point of transcendence degree greater than \(-n\), the right stalk vanishes by the upper test. If the stalk of \(M_n\) is finite over \(\mathcal O\), it must then be zero. To spell out this use of Nakayama, choose generators \(m_1,\ldots,m_t\). The equality \(M=\pi M\) expresses their column as \(\pi C\) times itself. The determinant of \(I-\pi C\) is a unit; its adjugate therefore forces every generator to vanish. This proves the support bound on \(M_n\). Rationalizing, with the required image comparison, proves (4.2) over \(E\). Descent to a finite coefficient field and exact faithful scalar extension give the \(\overline{\mathbb Q}_\ell\) statement. Applying that statement to \(F[s]\), where \(s=\dim\operatorname{Supp}F\), recovers (4.1) for rational adic ordinary sheaves.

The normalized reduction and rational-model arguments are developed in the cited adic-sheaf lesson and [The pro-étale site and ℓ-adic complexes](course:AG-LTF/the-pro-etale-site-and-l-adic-complexes#4-completion-remembers-a-complex). They do not, by themselves, prove finiteness of a nonproper image or the exceptional rationalization comparison. The argument (4.4)–(4.6) is conditional on those exact geometric inputs; taking inverse limits of torsion vanishing is not a substitute for them.

### The classical input still to be completed

The classical form of (4.1) remains a proof obligation for every allowed algebraically constructible field-valued sheaf, not only for sheaves already obtained from an étale coefficient system. The free BBD edition, Remark 4.1.9, states the complex analogue and points to comparison theorems. That remark does not write the comparison proof we need here. In particular, identifying the constant-coefficient cohomology of an algebraic variety with its analytic cohomology would not yet establish the required comparison for arbitrary constructible complexes and relative direct images. Descent of coefficients, constructibility, compatibility of the direct image and preservation of support dimensions must all be supplied at the stated generality before that route proves (4.1).

Another possible route passes through ordinary perverse cohomology on Stein spaces. The analytic programme has written [Morse exhaustion geometry](course:SH-03/holomorphic-morse-exhaustions-on-stein-manifolds) and a [microlocal Stein argument](course:SH-03/microlocal-types-and-stein-cohomology), but its [ordinary/microlocal comparison and transverse restriction](course:SH-03/microlocal-types-and-stein-cohomology#sources-and-the-next-comparison) remain planned. Those texts therefore cannot currently serve as a completed provider for (4.1). We retain the full classical theorem as an assigned result to be proved. Its applications in this lesson are the explicit deductions from (4.1); neither this source pointer nor the proposed analytic route completes that premise.

## 5. Extensions and the remaining degree intervals

Combining the dimension bounds in Section 2 with the affine bounds in Section 4 gives the following precise ranges for a perverse input \(P\).

| Map \(f\) | Possible perverse degrees of \(Rf_*P\) | Possible perverse degrees of \(Rf_!P\) |
|---|---|---|
| Fibres of dimension at most \(d\) | At least \(-d\) | At most \(d\) |
| Affine, with the same fibre bound | \([-d,0]\) | \([0,d]\) |
| Proper, with the same fibre bound | \([-d,d]\) | \([-d,d]\) |
| Finite | \(0\) | \(0\) |

The affine row has exactly the coefficient and prerequisite qualifications of Section 4. For an affine quasi-finite map, \(d=0\), so both images are t-exact. In particular an affine open immersion \(j:U\hookrightarrow X\) gives exact functors
\(j_!,Rj_*:\mathcal P(U)\to\mathcal P(X)\).
To see exactness on hearts, regard a short exact sequence as its distinguished triangle; the perverse cohomology sequence of its image has only degree zero, and is again short exact.

For a local calculation independent of the unfinished general classical Artin input, take \(j:\mathbb C^*\hookrightarrow\mathbb C\), \(A=\Lambda[1]\), and \(i:\{0\}\hookrightarrow\mathbb C\). A circle has cellular cochains \(\Lambda\) in degrees zero and one with zero differential. The earlier boundary triangle and recollement therefore give

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

For a smooth hyperplane section this is ordinary weak Lefschetz. Its proof here inherits the exact classical or adic input still identified in Section 4; the short localization deduction does not close that gap.

## 7. Exercises and solutions

**Exercise 1 (easy).** For \(j:\mathbb C^*\hookrightarrow\mathbb C\), verify the perversity of \(Rj_*\Lambda[1]\) from the point tests, and identify its quotient by \(\Lambda_{\mathbb C}[1]\).

**Solution.** Write the cellular cochains of the punctured disc as the two-term complex \([\Lambda\xrightarrow{0}\Lambda]\) in degrees zero and one. After shifting by one, the stalk degrees are \(-1,0\), meeting the upper point bound. The costalk is zero because \(i^!Rj_*=0\), meeting the lower point bound. On the open stratum the object is the required shifted local system, so both tests hold everywhere. The map from the constant shifted sheaf identifies the degree-minus-one stalk and is an isomorphism off zero. Its cone has only \(\Lambda\) in degree zero at the origin; thus it is \(i_*\Lambda\). Since the three terms lie in the perverse heart, this cone is the asserted quotient. This calculation does not invoke the general affine theorem.

**Exercise 2 (easy).** Compute the perverse cohomology of \(Ra_*\Lambda_{\mathbb P^1}[1]\) for \(a:\mathbb P^1\to\mathrm{pt}\), and decide whether \(Ra_*\) is right t-exact.

**Solution.** The classical cell structure has a degree-zero and a degree-two generator, with no adjacent cell for a differential. The geometric étale computation gives the same degrees and a Tate twist on the upper generator. Shifting by one yields precisely \({}^pH^{-1}=\Lambda\) and \({}^pH^1=\Lambda(-1)\), with the twist omitted classically; all other groups are zero. On a point these are ordinary cohomology groups. The smooth-curve sheaf \(\Lambda[1]\) is in the perverse heart, but its image has a positive group. Right t-exactness therefore fails, despite properness.

**Exercise 3 (medium).** Convert the perverse restriction degrees into ordinary weak Lefschetz for a smooth projective \(d\)-fold and a smooth hyperplane section. Determine what happens at the boundary degree.

**Solution.** The shifted constant sheaf on the \(d\)-fold is perverse. Its degree-\(n\) cohomology on either side of restriction is degree \(n+d\) cohomology with unshifted coefficients. The two compact-support groups adjoining restriction in (6.2) have perverse indices \(n\) and \(n+1\). Both vanish for \(n<-1\); just the first is forced to vanish for \(n=-1\). Translating gives an isomorphism for ordinary degree \(m<d-1\) and injectivity for \(m=d-1\). For a curve this boundary is degree zero: constants on a connected curve map diagonally to constants at its hyperplane points, an injective map which need not be onto. The deduction is conditional on the same affine input as Theorem 6.1.

**Exercise 4 (medium).** Prove that finite direct image is perverse t-exact, allowing singular source and target.

**Solution.** A finite map has zero-dimensional fibres. Pullback of any ordinary cohomology support therefore has no larger dimension; the upper test gives \(f^*({}^pD^{\le0})\subset{}^pD^{\le0}\). For lower \(B\), adjunction makes every map from an upper object of degree at most \(-1\) to \(Rf_*B\) zero. Hence \(Rf_*\) preserves the lower part. Field duality gives preservation of the upper part by \(Rf_!\). Properness of a finite map identifies these two direct images, supplying both halves for one functor. The perverse cohomology sequence then proves exactness on hearts, and uniqueness of truncation gives commutation with (1.1). This uses the dimension, operation and duality prerequisites, without an Artin-vanishing step.

**Exercise 5 (hard).** Derive positive-degree affine vanishing for every \(K\in{}^pD^{\le0}(U)\) directly from ordinary Artin vanishing. Explain the compact-support consequence and the absence of a degree-zero concentration claim.

**Solution.** Ordinary Artin vanishing bounds cohomology of an ordinary sheaf by the dimension of its support. For \(F=\mathcal H^bK\), that dimension is at most \(-b\), so
\(H^a(U,\mathcal H^bK)=0\) whenever \(a>-b\).
In the ordinary hypercohomology spectral sequence, every term of total degree \(n>0\) satisfies this inequality and vanishes on its second page. Every later subquotient in that total degree is zero. Boundedness supplies a finite filtration of the abutment; an iterated extension of zero groups is zero. Thus \(H^n(U,K)=0\) for \(n>0\).

For a perverse \(P\), its field dual is again perverse. The identity
\(H_c^n(U,P)^\vee=H^{-n}(U,D_UP)\)
then gives compact-support vanishing for \(n<0\). On \(\mathbb A^r\), however, the perverse sheaf \(\Lambda[r]\) has an ordinary global group \(\Lambda\) in degree \(-r\) and a compact-support group \(\Lambda(-r)\) in degree \(r\). Classically these follow by contraction and the one-point compactification \(S^{2r}\); the geometric étale versions use affine-space cohomology and smooth duality. They exhibit the two permitted sides of the bounds. Neither functor is asserted to concentrate in degree zero. As in Section 4, the ordinary Artin premise at the exact coefficient version must be supplied, not inferred from a citation.

## Remaining proof obligations and free references

This reconstruction retains the following dependencies explicitly. The torsion support theorem is written in the earlier étale companion, but its strict-local models, continuity, curve results and dimension induction still require recursive verification at exact versions. The integral truncation used here now has its construction in (4.4); its ambient normalized operations, nonproper finiteness, refinement/purity and rationalization comparisons remain required. The classical ordinary perverse Stein theorem is unfinished because the ordinary/microlocal comparison and transverse restriction have not been supplied. Smooth duality, local smooth sections, constructibility, finite-type dimension, oriented ball/sphere comparisons and the geometric étale curve and affine-space calculations must all have their earlier proofs verified. Thus neither the displayed deductions nor a successful render grants whole-lesson P514 clearance.

The sources used for the affine and smooth comparison are the freely accessible versions below. The Bhatt–Blickle–Lyubeznik–Singh–Zhang reference concerns a different characteristic-\(p\) coefficient theory; its subsection 5.1 is a further reading direction and supplies no proof input to the prime-to-characteristic arguments here.

- A. Beilinson, J. Bernstein and P. Deligne, with contributions by O. Gabber, [*Faisceaux pervers*](https://publications.ias.edu/sites/default/files/Faisceaux%20pervers.pdf), freely readable IAS edition; Sections 4.1.1–4.1.5, Remark 4.1.9 and Sections 4.2.3–4.2.5.
- M. A. A. de Cataldo and L. Migliorini, [*The Decomposition Theorem and the topology of algebraic maps*](https://arxiv.org/abs/0712.0349v2), arXiv:0712.0349v2; Section 5.3.
- M. Artin, A. Grothendieck and J.-L. Verdier, [*Théorie des topos et cohomologie étale des schémas*](https://www.normalesup.org/~forgogozo/SGA4/tomes/SGA4.pdf), free Laszlo–Orgogozo transcription of SGA 4; Exposé XIV supplies the torsion affine theorem discussed in the earlier companion.
- B. Bhatt, M. Blickle, G. Lyubeznik, A. K. Singh and W. Zhang, [*Applications of perverse sheaves in commutative algebra*](https://arxiv.org/abs/2308.03155), free arXiv version; subsection 5.1 for the separate characteristic-\(p\) setting.
