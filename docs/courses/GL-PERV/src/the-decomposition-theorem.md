# The decomposition theorem

*Written by GPT-6 Astra (OpenAI) in Codex, Ultra setting, October 2026. Public domain (CC0).*

The stalk of a proper direct image is the cohomology of a fibre. The decomposition problem asks how those stalks assemble: which local systems occur, on which closed supports, and in which perverse degrees? There are two distinct assertions to establish. The complex must split into its shifted perverse cohomology objects, and those objects must themselves be sums of simple perverse sheaves. We begin with a finite map where the splitting can be constructed by projectors. We then separate the categorical splitting argument from the weight and hyperplane arguments that supply the general theorem.

Our conventions and prerequisites are [Gluing t-structures](gluing-t-structures.md), [The perverse t-structure](the-perverse-t-structure.md), [Intermediate extensions and intersection complexes](intermediate-extensions-and-intersection-complexes.md), [Affine morphisms, Artin vanishing and perverse cohomology](affine-morphisms-artin-vanishing-and-perverse-cohomology.md), and [Weights, purity and semisimplicity over finite fields](weights-purity-and-semisimplicity-over-finite-fields.md). Local monodromy calculations use Nearby and vanishing cycles. The ordinary operations and the elementary curve topology used below are developed in Constructible complexes on algebraic varieties.

All varieties are separated and of finite type over the indicated field. In the classical setting the maps are algebraic maps of complex varieties. Write \(\operatorname{IC}_Z(L)=j_{!*}(L[s])\), where \(Z\) is irreducible of dimension \(s\) and \(L\) is an irreducible local system on a dense smooth open \(j:U\hookrightarrow Z\). A closed inclusion into the ambient space is understood. A semisimple complex means a finite sum of shifted simple perverse sheaves; being perverse is not part of that definition. Our shifts satisfy \(\mathcal H^i(K[a])=\mathcal H^{i+a}(K)\).

Over finite fields we use \(\overline{\mathbb Q}_\ell\), with \(\ell\) invertible on the variety, and retain Tate twists. Subscript \(0\) denotes arithmetic descent; removing it denotes pullback to an algebraic closure. The complex geometric-origin theorem is stated with complex coefficients. The rational constant-IC form used in the resolution examples is also retained, with its coefficient comparison identified in the closing prerequisite paragraph.

## 1. A finite map determines its own summands

Let \(f:X\to Y\) be finite, surjective and generically étale, with \(X\) smooth and irreducible of dimension \(d\). Choose a dense smooth open \(V\subset Y\) such that its inverse image \(V'\) is dense and \(f|_{V'}\) is étale. Put \(M=(f|_{V'})_*\Lambda\). We claim
\[
Rf_*\Lambda_X[d]=j_{!*}(M[d]),\qquad j:V\hookrightarrow Y.
\tag{1.1}
\]
The claim applies classically, and in the geometric étale setting with characteristic-zero coefficients.

Here is the boundary argument. Finite direct image is perverse exact by the dimension bounds of lesson 5, so \(P=Rf_*\Lambda_X[d]\) is perverse. If \(i:Y\setminus V\hookrightarrow Y\) and \(i':X\setminus V'\hookrightarrow X\), proper base change and its dual identify \(i^*P\) and \(i^!P\) with the finite images of \(i'^*\Lambda_X[d]\) and \(i'^!\Lambda_X[d]\). The smooth constant sheaf is the intermediate extension of its restriction to \(V'\). Consequently these two boundary complexes have zero perverse cohomology in degree zero. Exactness of finite image preserves that vanishing. Lesson 4's uniqueness characterization now identifies \(P\) with (1.1).

The local system \(M\) has finite monodromy. A representation of a finite group over a characteristic-zero field is semisimple: average any linear retraction to a subrepresentation over the group, dividing by its order, to obtain an equivariant retraction. Iterating on dimension gives a sum of irreducibles. Intermediate extension commutes with finite direct sums, since its defining image does. Thus (1.1) decomposes into the intersection complexes of the irreducible constituents of \(M\). No general decomposition theorem was needed for this calculation.

For \(f:\mathbb P^1\to\mathbb P^1\), \(z\mapsto z^2\), let \(\sigma\) be the deck involution. The idempotents \((1+\sigma)/2\) and \((1-\sigma)/2\) give the two constituents over \(\mathbb G_m\). The first is constant and the second, denoted \(L_-\), has monodromy \(-1\) around both omitted points. At either puncture the two-term boundary complex has differential \(T-1=-2\); hence it is acyclic. The sign summand has zero boundary stalk and costalk. The branched fibre consists of a single fixed point, contributing only the constant summand. Therefore
\[
f_*\Lambda[1]=\Lambda_{\mathbb P^1}[1]\oplus j_{!*}(L_-[1]).
\tag{1.2}
\]
There are no point summands. Over a finite field the characteristic must be odd for this description of the cover.

### The quotient surface in both coefficient settings

The same method gives the IC calculation needed later for \(X=\{xy=z^2\}\). In characteristic different from two the finite map
\[
p:\mathbb A^2\longrightarrow X,\qquad (u,v)\longmapsto(u^2,v^2,uv)
\tag{1.3}
\]
is the quotient by \((u,v)\mapsto(-u,-v)\). Indeed the invariant monomials are generated by \(u^2,uv,v^2\), whose sole relation is \(xy=z^2\): reduce a polynomial using that relation to monomials with at most one factor \(z\), whose images are distinct monomials in \(u,v\). The coordinates \(u,v\) are integral over the invariant ring, so the map is finite. Away from the vertex it is an étale double cover. On \(u\ne0\), for example, its coordinate description is adjoining the invertible square root \(u\) of \(x\); the other chart is analogous.

Take the invariant projector on \(p_*\Lambda[2]\). The resulting summand is \(\Lambda_X[2]\). To check this assertion as a sheaf statement, use the unit \(\Lambda_X\to p_*\Lambda\): on each geometric fibre the invariant functions are precisely the constants, whether the fibre has two points or one. Finite proper base change gives no higher fibre cohomology, so this stalk check proves the assertion for the complex as well. Formula (1.1) and the two projectors then show
\[
\operatorname{IC}_X=\Lambda_X[2].
\tag{1.4}
\]
This is a proof for the odd-characteristic étale quotient as well as the classical quotient. It uses the exact finite-image and base-change foundations just stated; it does not infer an étale calculation from the classical link \(\mathbb {RP}^3\).

## 2. Removing the extreme cohomology groups

Before treating proper maps, we isolate a categorical statement. Let \(\mathcal D\) have a bounded t-structure, with cohomology functors \(H^i\), and an exact t-exact autoequivalence \((1)\). Suppose
\[
e:M\longrightarrow M(1)[2],\qquad
H^{-r}(e^r):H^{-r}M\xrightarrow{\sim}H^rM(r)
\quad(r\ge0).
\tag{2.1}
\]
Then
\[
M\simeq\bigoplus_iH^iM[-i].
\tag{2.2}
\]
This is Deligne's Lefschetz splitting criterion. We prove it by removing the two outermost cohomology degrees, so no primitive decomposition is needed.

First, a retraction \(r:M\to A\) of \(a:A\to M\) produces a complement inside a triangulated category. Complete \(a\) to \(A\to M\xrightarrow{v}N\xrightarrow{\delta}A[1]\). Applying \(\operatorname{Hom}(-,A)\) shows \(\delta=0\), since \(\operatorname{id}_A=ra\) lifts. Hence \(v\) has a section \(t\). Replace \(t\) by \(t-art\), so \(rt=0\). Now \((r,v)(a,t)=1\). Conversely \(d=1-ar-tv\) satisfies \(vd=0\), and therefore \(d=ah\) by the triangle's exact Hom sequence. Since \(rd=0\), also \(h=0\). Thus \((a,t)\) is an isomorphism \(A\oplus N\to M\). This uses the triangle axioms, without a separate idempotent-completeness assumption.

Choose \(n\) with all cohomology of \(M\) in \([-n,n]\). For \(n=0\) the assertion is truncation. Otherwise set
\[
A=H^{-n}M[n],\quad B=H^nM[-n],\quad
\lambda=H^{-n}(e^n):H^{-n}M\xrightarrow{\sim}H^nM(n).
\]
The extreme truncations give maps \(a:A\to M\) and \(p:M\to B\). Define
\[
\begin{aligned}
r&=\lambda^{-1}[n]\circ p(n)[2n]\circ e^n:M\to A,\\
s&=e^n(-n)[-2n]\circ a(-n)[-2n]
       \circ\bigl(\lambda(-n)^{-1}\bigr)[-n]:B\to M.
\end{aligned}
\tag{2.3}
\]
The middle target in the first formula is \(H^nM(n)[n]\). In the second, the rightmost map lands in \(H^{-n}M(-n)[-n]\), after which \(a(-n)[-2n]\) lands in \(M(-n)[-2n]\). These observations verify all the displayed types.

Taking extreme cohomology gives \(ra=1_A\) and \(ps=1_B\); endomorphisms of a shifted heart object are determined by that cohomology. Orthogonality gives \(pa=0\), because \(A\in\mathcal D^{\le-n}\) and \(B\in\mathcal D^{\ge n}\). There is no reason for \(rs\) to vanish. Correct it by setting \(s'=s-ars\). Then
\[
(r,p)(a,s')=1_{A\oplus B}.
\]
The preceding split-triangle argument yields \(M=A\oplus B\oplus N\), where \(N\) has cohomology only in \([-n+1,n-1]\). Write \(t:N\to M\) and \(v:M\to N\) for inclusion and projection, and put \(e_N=v(1)[2]et\).

For each \(r<n\), the successive degrees \(-r,-r+2,\ldots,r\) lie entirely in the remaining interval. In those degrees \(t\) and \(v\) identify the cohomology of \(N\) with that of \(M\). Thus \(H^{-r}(e_N^r)\) is the original isomorphism. For \(r\ge n\) both ends vanish. Induction proves (2.2).

For any cohomological functor \(F\), define \(F^a(K)=F(K[a])\). Apply the functorial truncation tower to a chosen isomorphism (2.2). It becomes the finite direct sum of the towers for the individual shifted heart objects. Each has a single cohomology row, so every differential after the cohomology page is zero. Additivity of the exact couples gives degeneration for their sum:
\[
E_2^{a,b}=F^a(H^bM)\Longrightarrow F^{a+b}(M).
\tag{2.4}
\]
Boundedness makes the filtration finite. Neither this argument nor (2.2) asserts semisimplicity of the objects \(H^iM\). It also does not select a unique splitting. Deligne's 1994 construction of normalized primitive lifts supplies additional choices attached to the specified class \(e\); that is extra structure beyond the existence argument here.

## 3. Weights supply the geometric decomposition

### Finite fields

Suppose \(f:X_0\to Y_0\) is proper and \(K_0\) is pure of weight \(w\). The results proved conditionally in lesson 7 give proper purity, the perverse weight criterion, geometric semisimplicity of pure perverse sheaves, and splitting of a geometric pure complex. In that order they imply
\[
Rf_*K_0\text{ pure of weight }w,\qquad
{}^pH^n(Rf_*K_0)\text{ pure of weight }w+n,
\]
and then
\[
Rf_*K\simeq\bigoplus_n{}^pH^n(Rf_*K)[-n],
\qquad {}^pH^n(Rf_*K)\text{ geometrically semisimple}.
\tag{3.1}
\]
The last line is over the algebraic closure. The preceding weight statements concern the arithmetic objects. Those statements do not make arithmetic Frobenius diagonalizable or furnish a Frobenius-equivariant splitting of (3.1). The remaining ordinary weight and adic foundations of lesson 7 remain prerequisites here.

### The finite construction defining geometric origin

For complex varieties, start with the constant rank-one sheaf on a point. From previously obtained simple perverse sheaves, permit the following operations: take any simple constituent of any perverse cohomology of \(Rf_*A,Rf_!A,f^*A,f^!A\), or, for objects on the same space, of \(A\otimes^LB\) and \(R\mathcal Hom(A,B)\). The smallest collection closed under these rules is the collection of simple perverse sheaves of geometric origin. A semisimple complex of geometric origin is a finite direct sum of shifts of members of this collection. This is the hypothesis of BBD, 6.2.4–6.2.5.

Every such object has a finite construction. Indeed the union of the successive finite stages of these rules is already closed under them, since every rule has finitely many inputs. On a smooth variety, the constant local system comes from pullback from a point. For an irreducible variety, choose a dense smooth open and take its shifted constant sheaf. Its intermediate extension is a simple constituent of the degree-zero perverse cohomology of the open extension by zero, by the image description in lesson 2. Thus the permitted operations also generate the constant IC on that variety. A finite-monodromy irreducible local system is a constituent of the finite-cover regular representation: averaging proves semisimplicity, and a nonzero vector gives a surjection from the regular representation onto any irreducible representation. Consequently these local systems and their IC extensions are also of geometric origin.

We use the following specific comparison construction. Descend a finite diagram of varieties, sheaves, morphisms, strata and operations to a finitely generated ring. After restricting its spectrum, classical/étale comparison and specialization give equivalences for the constructible categories with the specified allowed local-system constituents. These equivalences are fully faithful and perverse t-exact, and preserve the six operations, tensor products and internal Hom appearing in that diagram. Their hearts are closed under subquotients. Include proper maps, and when required a projective map, its ample line bundle and its Chern-class morphisms, before making the comparison. The integral models and stable-lattice qualifications in BBD, 6.1.2 are part of this input. No equivalence of unrestricted constructible categories on arbitrary fibres is being asserted. A complete construction of these comparisons is still required for P514.

We prove the further pure-model step. Let \(G_0\) be mixed perverse over a finite field, and let \(S\) be a simple constituent after geometric pullback. Its weight filtration has a pure graded piece \(Q_0\) whose geometric pullback contains \(S\). By geometric semisimplicity, \(Q\) is a sum of isotypic pieces. A finite residue-field extension makes the class of \(S\) fixed under Frobenius, so its full isotypic piece becomes stable. Write it \(S\otimes M\).

Here \(\operatorname{End}(S)=\overline{\mathbb Q}_\ell\): restriction to the dense local-system stratum embeds the endomorphism ring in a finite-dimensional matrix algebra, and every endomorphism of an irreducible object over an algebraically closed field has an eigenvalue; its corresponding nonzero kernel forces it to be scalar. Choose an isomorphism \(\operatorname{Fr}^*S\simeq S\). The Frobenius action on \(S\otimes M\) is then that isomorphism tensored with an invertible linear operator on \(M\). An eigenline of that operator selects a stable copy of \(S\). It inherits continuous arithmetic descent as a subobject of \(Q_0\) over the extended field. Pure perverse subobjects are pure, by the weight bounds of lesson 7. Thus \(S\) has a pure arithmetic model after a finite extension. The continuity conclusion comes from this embedding in an existing arithmetic object, not from assigning an arbitrary Frobenius matrix.

Apply this argument inductively to a geometric-origin construction. The starting constant point sheaf has its weight-zero model. At a later step take pure models of the inputs over a common finite extension of the closed fibre's residue field. Their required operation is mixed by the mixed-operation theorem, and each of its perverse cohomologies is mixed. Comparison identifies the selected geometric constituent with a constituent of that mixed object. The argument of the preceding paragraph gives it a pure model, after another finite extension. This proves the claim for every construction step, including tensor product and internal Hom. Enlarging the finite diagram handles finitely many desired objects simultaneously. Purity of every generating operation is unnecessary; mixedness and constituent selection suffice.

**The complex geometric-origin theorem.** If \(f:X\to Y\) is proper and \(K\) is a semisimple complex of geometric origin, then \(Rf_*K\) is again a semisimple complex of geometric origin. In particular it has an expression
\[
Rf_*K\simeq\bigoplus_{n,a}\operatorname{IC}_{Z_{n,a}}(L_{n,a})[-n].
\tag{3.2}
\]

To prove it from the specified comparisons, first take a simple perverse source \(P\). Include \(f,P,Rf_*P\), the needed perverse cohomologies and their finite constructions in the diagram. The preceding induction produces a pure arithmetic model on an allowed closed geometric fibre. Properness descends, so (3.1) applies there. Full faithfulness of the inverse comparison lifts a splitting and its inverse to actual morphisms; t-exactness identifies their terms with the perverse cohomologies on the characteristic-zero fibre. The equivalence preserves and reflects simple objects, hence semisimplicity. Classical comparison gives the claimed complex-algebraic splitting. Its simple constituents are of geometric origin by the defining direct-image rule. Finally take finite sums and shifts of the argument for simple sources. This proves (3.2), relative to the comparison and weight foundations. The support classification is lesson 4's simple-object theorem.

The perverse cohomology objects are canonical. Their simple isomorphism classes and multiplicities are determined. An isomorphism (3.2), including the individual inclusions and projections, generally requires choices.

### The larger semisimple-source statement

Geometric origin is the scope of the arithmetic reduction just proved, not the limit of the known complex-algebraic theorem. For a proper map of complex varieties and a semisimple perverse sheaf with rational or complex coefficients, the direct image is semisimple as a complex. For a projective map its relatively ample class also satisfies relative hard Lefschetz. No quasi-projectivity or smoothness assumption on the two varieties is required in this formulation. The exact statements are de Cataldo, *Decomposition theorem for semi-simples*, Theorems 2.1.1–2.1.2 and Corollary 2.2.1. Its proof extends the smooth quasi-projective theorem of Mochizuki and Sabbah using resolution, Chow envelopes and coefficient descent. This broader statement is retained here as a proof obligation; neither its analytic starting theorem nor the full reduction is proved by the finite-field argument above. None of the calculations below uses that extension. Saito's mixed Hodge modules and the Hodge-theoretic proof of de Cataldo–Migliorini are further approaches, discussed in the freely available survey, §3.

## 4. Hyperplane restriction becomes a Lefschetz isomorphism

### The arithmetic Lefschetz argument

Let \(f:X_0\to Y_0\) be projective, let \(F_0\) be pure perverse, and let \(\eta=c_1(\mathcal L)\) for an \(f\)-ample line bundle. We prove
\[
\eta^r:{}^pH^{-r}(Rf_*F_0)\xrightarrow{\sim}
{}^pH^r(Rf_*F_0)(r),\qquad r\ge0.
\tag{4.1}
\]
This argument uses the ordinary operations, affine bounds and conditional purity/semisimplicity results of the earlier lessons. Those weight results are obtained before this argument and do not assume (4.1).

Work geometrically while retaining all arithmetic models. Locally on \(Y\), a positive power of \(\mathcal L\) gives a closed embedding into \(\mathbb P^d\times Y\), with \(d\ge1\). Multiplication of \(\eta\) by the positive integer does not change the isomorphism question over a characteristic-zero coefficient field. We may use the hyperplane class of this embedding.

Set \(T=(\mathbb P^d)^\vee\), \(Y'=T\times Y\), \(X'=T\times X\), and let \(v:H\hookrightarrow X'\) be the universal incidence divisor. Write \(u:Y'\to Y\), \(q:X'\to X\), \(f':X'\to Y'\) and \(h=f'v\). The maps \(q\) and \(qv\) are smooth projective bundles of dimensions \(d\) and \(d-1\). In particular
\[
\begin{aligned}
F'&=q^*F[d],& F_H&=(qv)^*F[d-1],\\
M&=Rf_*F,& A&=Rf'_*F'=u^*M[d],& L&=Rh_*F_H.
\end{aligned}
\tag{4.2}
\]
have \(F'\) and \(F_H\) perverse. If \(F_0\) has weight \(w\), then \(F_H\) has weight \(w+d-1\). Proper purity and the perverse weight criterion make \(S={}^pH^0L\) pure of that weight, hence geometrically semisimple.

We need the projective-bundle calculation with its maps. For \(b:E\to Z\) a projective bundle of dimension \(e\), unit followed by powers of \(\beta=c_1(\mathcal O_E(1))\) defines
\[
\bigoplus_{a=0}^e K[-2a](-a)\xrightarrow{\sim}Rb_*b^*K.
\tag{4.3}
\]
Proper base change reduces the assertion to a geometric fibre. Filter \(\mathbb P^e\) by its standard hyperplane and affine complement. Localization, and the single compact cohomology group of \(\mathbb A^e\), give one group in each even degree \(0,2,\ldots,2e\) and none in odd degree. Hyperplane Gysin identifies the successive generators with \(1,\beta,\ldots,\beta^e\). Smooth trace normalizes the class of the transverse intersection of \(e\) hyperplanes to \(+1\). This proves that the displayed map is a fibrewise isomorphism, with its stated twists, using the earlier smooth trace and purity foundations.

Consider the heart functor \(U(P)=u^*P[d]\). It is exact. Formula (4.3) and adjunction show full faithfulness and also
\[
\operatorname{Hom}(UP,UQ[1])
=\bigoplus_{a=0}^d\operatorname{Hom}(P,Q(-a)[1-2a])
=\operatorname{Hom}(P,Q[1]).
\tag{4.4}
\]
All summands with \(a>0\) vanish by negative-degree orthogonality. Its essential image is a Serre subcategory of the perverse heart. For completeness, smooth base change and t-exactness show that \(U\) commutes with intermediate extension. It preserves a simple IC: the product projection induces a surjection of fundamental groups, since it has a section, so pullback preserves irreducibility of the defining local system. Degree-one derived Hom classifies heart extensions, so (4.4) lifts every extension between image objects. Finite length now shows that any subobject or quotient of an image object, assembled from the same simple constituents, is in the image too.

The right adjoint to \(U\) on hearts is
\[
R(S)={}^pH^{-d}(Ru_*S).
\tag{4.5}
\]
The lower fibre bound places \(Ru_*S[-d]\) in \({}^pD^{\ge0}\), so truncation and adjunction give (4.5). Formula (4.3) identifies \(RU\) with the identity through its unit. The counit \(UR(S)\to S\) is a monomorphism: its kernel lies in the image Serre subcategory, and applying the left-exact right adjoint annihilates that kernel because the counit becomes the identity on \(R(S)\). An image object killed by \(R\) is zero. By adjunction, every map from an image object to \(S\) factors through this counit. Thus it is the largest subobject of \(S\) belonging to the image.

The complement of the incidence divisor is affine over \(Y'\): it is closed in the universal affine hyperplane complement. Apply localization to \(F'\) and use the compact-support affine bound on that complement. Perverse cohomology gives restriction maps
\[
a_j:U({}^pH^jM)\longrightarrow{}^pH^{j+1}L,
\tag{4.6}
\]
which are isomorphisms for \(j<-1\) and injective for \(j=-1\). In particular \(C=U({}^pH^{-1}M)\) injects into \(S\). We show it is precisely the largest image subobject just described.

Put \(B=L[1]\), so (4.6) comes from \(A\to B\) and identifies their truncations in degrees at most \(-2\). Apply (4.3), using the hyperplane class of \(T\) for both bundles. It gives
\[
Ru_*A=\bigoplus_{a=0}^d M[d-2a](-a),\qquad
Ru_*B=\bigoplus_{a=0}^{d-1} M[d-2a](-a).
\tag{4.7}
\]
Restriction is the identity on the first \(d\) columns. Subtracting the possibly nonzero components of the last column identifies its fibre with \(M[-d](-d)\). The bound \(M\in{}^pD^{\ge-d}\) puts this fibre in \({}^pD^{\ge0}\). Therefore the two total images agree in every degree below zero.

Compare the two truncation triangles at degrees \(-2,-1\) after applying \(Ru_*\). Their lower terms agree; their total terms agree in degrees \(-d-1\) and \(-d\), both below zero. The five terms of the two long exact sequences around the upper-tail group in degree \(-d-1\) imply that these tail groups agree. The lower amplitude bound of \(Ru_*\) identifies them as
\[
{}^pH^{-d}Ru_*({}^pH^{-1}A)=R(C),\qquad
{}^pH^{-d}Ru_*({}^pH^{-1}B)=R(S).
\]
Thus \(R(C)\to R(S)\) is an isomorphism. Adjunction identifies \(C\to S\) with its maximal image subobject. Apply the same proof to \(DF\) and dualize. Smooth duality preserves the image of \(U\), and the dual restriction, namely Gysin, identifies \(U({}^pH^1M)(1)\) as the maximal quotient of \(S\) in that image.

In a semisimple finite-length object, the sum of the simple factors belonging to a Serre subcategory is both its largest subobject and its largest quotient in that subcategory. The composite between those two objects is an isomorphism: the other factors have no maps to or from them. Apply this to \(S\). Restriction followed by Gysin gives an isomorphism from \(U({}^pH^{-1}M)\) to \(U({}^pH^1M)(1)\).

We must identify that map, including its class. The incidence is a regular Cartier divisor; on a chart where one coordinate of \(x\) is nonzero its equation solves for a hyperplane coefficient. Smooth duality for \(q\) and \(qv\), with transitivity of exceptional pullback, gives
\(v^!F'=F_H[-1](-1)\).
The restriction and counit therefore supply the restriction–Gysin composite. By the divisor class construction it is cup product with
\[
c_1(\mathcal O_{X'}(H))=q^*\eta+f'^*\beta.
\tag{4.8}
\]
The plus sign comes from the tensor product of the two hyperplane line bundles and the positive divisor orientation. With the localization convention of lesson 6, Appendix E, the Kummer localization boundary of a parameter is the *negative* of its supported divisor class; it must not be silently substituted with the opposite sign. The oriented Gysin map in (4.8) uses the positive class.

A base class acts by zero between distinct perverse cohomology degrees. Indeed cup product by \(\beta\) is a natural transformation \(K\to K(1)[2]\). Compare it with \({}^p\tau^{\le j}K\to K\). The latter is an isomorphism on \({}^pH^j\), whereas the degree-\(j\) group of \(({}^p\tau^{\le j}K)(1)[2]\) is zero. Naturality kills the map to \({}^pH^{j+2}K(1)\). Thus the preceding isomorphism is exactly \(U(\eta)\), and faithfulness gives (4.1) for \(r=1\).

Induct on \(r\), simultaneously for all projective maps and pure perverse sources. For \(r>1\), (4.6) and its dual give the outer isomorphisms in
\[
U({}^pH^{-r}M)\longrightarrow{}^pH^{1-r}L
\xrightarrow{\eta_H^{r-1}}{}^pH^{r-1}L(r-1)
\longrightarrow U({}^pH^rM)(r),
\tag{4.9}
\]
where \(\eta_H=(qv)^*\eta\) is relatively ample for \(h\). The middle arrow is an isomorphism by induction applied to \(F_H\). Projection formula identifies the composite with the action of \((q^*\eta+f'^*\beta)(q^*\eta)^{r-1}\). The term containing \(\beta\) vanishes on the relevant perverse cohomology by the same naturality argument. We obtain \(U(\eta^r)\), hence (4.1). The case \(r=0\) is the identity. Since the maps descend and geometric pullback is conservative, the arithmetic maps are isomorphisms as well. This completes the universal-hyperplane argument of BBD, 5.4.10–5.4.15, relative to the identified ordinary foundations.

### Transport to complex varieties

If \(P\) is semisimple perverse of geometric origin and \(f\) is projective over \(\mathbb C\), include \(\mathcal L\), its Chern map and all nonzero perverse degrees in the finite diagram of §3. A simple constituent of \(P\) has a pure model on an allowed closed fibre. Formula (4.1) makes the descended Lefschetz maps isomorphisms. Comparison carries their actual morphisms to the corresponding complex-fibre morphisms. Their cones vanish on one side of an equivalence and hence on the other. Finite sums prove
\[
\eta^r:{}^pH^{-r}(Rf_*P)\xrightarrow{\sim}{}^pH^r(Rf_*P)(r).
\tag{4.10}
\]
Geometric Tate coefficients may be trivialized. The comparison of the Chern maps, not just of the objects, is essential to this proof. The categorical result of §2 then supplies a derived splitting. Proper decomposition in §3 also applies when a relatively ample class has not been supplied.

## 5. The natural consequences of a chosen decomposition

### Intersection cohomology inside a resolution

For a proper resolution \(f:\widetilde X\to X\) of an irreducible \(d\)-dimensional variety, with \(\widetilde X\) smooth, the unique full-support summand of \(Rf_*\Lambda[d]\) is \(\operatorname{IC}_X\), with multiplicity one and shift zero. To see this, restrict a decomposition to a dense smooth open where \(f\) is an isomorphism and which avoids all the other proper supports. The restriction is \(\Lambda[d]\). It has exactly one rank-one perverse constituent in degree zero. Consequently there is exactly one full-support term, and its intermediate extension is \(\operatorname{IC}_X\). All other terms have smaller support. In global degree \(r-d\) this yields
\[
IH^r(X,\Lambda)\text{ is a direct summand of }H^r(\widetilde X,\Lambda).
\tag{5.1}
\]
The definition is \(IH^r(X)=H^{r-d}(X,\operatorname{IC}_X)\), so both sides have the displayed degree. A chosen derived splitting induces the inclusion and retraction. The theorem proves existence of these maps, not their canonicity. In particular, whenever the groups are finite-dimensional, their dimensions satisfy the corresponding inequality in every degree.

### Global invariant cycles

Let \(A=Rf_*K\), with \(f\) proper and \(K\) semisimple of geometric origin. Suppose \(V\subset Y\) is Zariski open and \(\mathcal H^iA|_V\) is locally constant. Then the natural edge and restriction map
\[
H^i(X,K)\longrightarrow H^0(V,\mathcal H^iA|_V)
\tag{5.2}
\]
is surjective.

We first compute the bottom ordinary degree of a simple IC. If \(s=\dim Z\) and \(j:U\hookrightarrow Z\) is its defining dense smooth open, the successive ordinary truncations in lesson 4 never cut below degree \(-s\). At every step the derived open image has no lower cohomology, and its degree \(-s\) sheaf is the ordinary direct image of the preceding bottom sheaf. Thus
\[
\mathcal H^b\operatorname{IC}_Z(L)=0\ (b<-s),\quad
\mathcal H^{-s}\operatorname{IC}_Z(L)=j_*L,\quad
H^{-s}(Z,\operatorname{IC}_Z(L))=H^0(U,L).
\tag{5.3}
\]
For the last equality the lowest-degree hypercohomology spectral sequence has only its degree-zero sheaf-cohomology term; the possible outgoing targets have ordinary degree below \(-s\).

Choose (3.2). Each \(\mathcal H^i\) of a summand, restricted to \(V\), is a direct summand of the local system \(\mathcal H^iA|_V\), so is itself locally constant. For a term \(\operatorname{IC}_Z(L)[-n]\), its generic value is zero unless \(i-n=-s\). A locally constant sheaf that vanishes on a dense open of its possible support cannot acquire a nonzero rank just on its boundary. Terms whose supports miss \(V\) also contribute nothing. For a contributing term, choose its dense smooth defining open \(U\) inside \(V\cap Z\); shrinking does not change IC, as proved in lesson 4. Formula (5.3) identifies its source and target in (5.2) with the same \(H^0(U,L)\). The induced map is the identity. Summing proves surjectivity. Composition of derived sections identifies \(H^i(Y,A)\) with \(H^i(X,K)\).

If \(V\) is connected and \(y\in V\), a section of a local system is determined by its value at \(y\), and that value must be fixed by every loop. Conversely an invariant value extends by transport along paths, independently of the path. Proper base change therefore identifies the target of (5.2) with
\[
H^i(X_y,K|_{X_y})^{\pi_1(V,y)}.
\tag{5.4}
\]
The choice of decomposition proves surjectivity of a map defined without that choice.

### Local invariant cycles

Fix \(y\in Y\). For a sufficiently small ball \(B\) about \(y\) in a local embedding, intersected with \(Y\), the local version is
\[
H^i(X_y,K|_{X_y})\longrightarrow
H^0(B\cap V,\mathcal H^iA|_{B\cap V})
\quad\text{surjective}.
\tag{5.5}
\]
The neighborhood input is simultaneous stabilization, on sufficiently small such balls, of the finitely many constructible section groups involved. One must also identify cohomology on the small ball with the stalk before inverting that comparison to define the displayed map. These are the constructible-neighborhood statements in BBD, 6.2.9; lesson 1's normal-neighborhood arguments address their geometry, but their exact small-ball scope and recursive prerequisites still need verification here.

Given this input, apply the preceding IC argument on \(B\). A contributing bottom sheaf is \(j_*L\). Its stalk at \(y\) is the colimit of \(H^0(B'\cap U,L)\) over shrinking neighborhoods. Stabilization identifies that stalk with the corresponding sections on the chosen \(B\). Since \(U\subset V\), the direct-image identity identifies those sections with the target for this summand in (5.5). All remaining summands have zero target. Their sum gives the surjection, and proper base change supplies its source. On a punctured disc the target is \(\ker(T-1)\); it need not be the entire nearby fibre group.

### The perverse Leray filtration

Use §2's single-row argument on (3.2). It proves degeneration of
\[
E_2^{a,b}=H^a(Y,{}^pH^b(Rf_*K))\Longrightarrow H^{a+b}(X,K).
\tag{5.6}
\]
The truncation filtration is canonical, whereas a splitting of it inherits the choice of a derived decomposition. This is the perverse Leray sequence. For a smooth proper family over a smooth base of dimension \(b\), the ordinary direct-image sheaves are local systems; shifting those sheaves by \([b]\) makes them perverse. The two index systems then translate into one another and give ordinary Leray degeneration. With singular fibres, replacing the perverse terms in (5.6) by ordinary cohomology sheaves is not justified by this argument.

## 6. Exceptional fibres and a vanishing loop

### A single exceptional projective line

The blow-up of the origin in \(\mathbb A^2\) is the incidence surface \(xv=yu\) in \(\mathbb A^2\times\mathbb P^1\). On \(u\ne0\) its coordinates are \((x,v/u)\), with \(y=xv/u\); the other chart is symmetric. The surface is smooth, its projection \(f\) is projective, and it is an isomorphism away from the origin with exceptional fibre \(\mathbb P^1\).

Put \(P=Rf_*\Lambda[2]\). At the origin its stalk has \(\Lambda\) in degree \(-2\) and \(\Lambda(-1)\) in degree zero. Smooth duality and properness give \(DP=P(2)\), so its costalk has degrees zero and two. Off the origin it is \(\Lambda[2]\). The support and cosupport tests therefore make \(P\) perverse. The decomposition theorem supplies semisimplicity. Generic restriction fixes its full-support summand as \(\Lambda_{\mathbb A^2}[2]\); the unused degree-zero stalk is one point coefficient. Hence
\[
Rf_*\Lambda_{\widetilde{\mathbb A^2}}[2]
\simeq\Lambda_{\mathbb A^2}[2]\oplus i_*\Lambda(-1).
\tag{6.1}
\]
Classically the Tate factor is omitted. This calculation shows explicitly why the resolution summand can be a proper summand of the direct image.

### The monodromy of a nodal cubic family

Consider the projective family
\[
y^2z=x^3+x^2z+t z^3
\tag{6.2}
\]
over the complex line with \(-4/27\) removed. In the affine chart \(z=1\), differentiation with respect to \(t\) proves smoothness of the total space. At infinity its only point is \([0:1:0]\), where differentiation with respect to \(z\) is nonzero. The cubic polynomial in \(x\) has discriminant \(-t(4+27t)\); equivalently a repeated root must solve \(3x^2+2x=0\), giving exactly those two parameter values. Near zero the noncentral fibres are smooth plane cubics and have Betti numbers \(1,2,1\), by lesson 1, Appendix E. The central fibre is the nodal cubic with normalization \(\mathbb P^1\) and two points above the node, calculated in Appendix L; its Betti numbers are \(1,1,1\).

We spell out why the local monodromy has a single nontrivial unipotent block. Near the node the convergent branch of \(\sqrt{1+x}\) defines
\[
a=y-x\sqrt{1+x},\qquad b=y+x\sqrt{1+x},\qquad ab=t.
\tag{6.3}
\]
The coordinate Jacobian at the origin is nonzero. For fixed small nonzero \(t\), the region \(|a|,|b|\le\varepsilon\) is an annulus in the \(a\)-coordinate, with radii \(|t|/\varepsilon\) and \(\varepsilon\). The outer boundary is parametrized by \(a\), and the inner boundary by \(b=t/a\). When \(t\) runs through \(t_0e^{i\theta}\), keeping \(a\) fixed on the outer boundary and \(b\) fixed on the inner boundary changes the argument of \(a\) by zero at the outer edge and by \(\theta\) at the inner edge.

Choose a radial cutoff \(\chi\) equal to zero near the outer edge and one near the inner edge. The maps \(a\mapsto a e^{i\theta\chi(|a|)}\), with \(b=t_0e^{i\theta}/a\), realize that transport. At \(\theta=2\pi\) it is one annular twist fixing both boundary circles. Outside the node region the family is a compact smooth submersion with boundary over the whole small disc. The relative vector-field construction in lesson 1, Appendix I.1, supplies a trivialization there: prescribe the displayed boundary lifts on collars, extend a horizontal lift by a partition of unity, and integrate along radial paths in the disc. Compactness gives the required complete flows. The collar prescription makes this trivialization agree with the chosen boundary parameters. Thus the annular twist is the whole monodromy up to isotopy.

The exterior of the central node is the normalization sphere with two discs removed, an annulus; the same is true of the exterior in the smooth fibres by that trivialization. Gluing it to the smoothing annulus gives a torus. A core circle \(\alpha\) of the smoothing annulus and a curve \(\gamma\) crossing that annulus once form a homology basis: cutting along both leaves a disc, with the usual four-edge boundary and one two-cell whose cellular boundary is zero. The twist fixes \(\alpha\). The crossing curve winds one additional time around the annulus, so, choosing its orientation accordingly, it sends \(\gamma\) to \(\gamma+\alpha\). Therefore the cohomological inverse transpose has one size-two unipotent Jordan block and
\[
\dim\ker(T-1)=1.
\tag{6.4}
\]
This argument uses the actual plumbing coordinates and the stated smooth-flow and sheaf/topology comparisons, rather than taking a Picard–Lefschetz formula as an unexplained input.

Let \(B\) be a small disc, \(j:B^*\hookrightarrow B\), and \(L=R^1f_*\Lambda|_{B^*}\). Restrict the algebraic decomposition to this disc. The open fibre cohomology fixes the full-support terms as
\[
Rf_*\Lambda[2]|_B
\simeq\Lambda_B[2]\oplus j_{!*}(L[1])\oplus\Lambda_B.
\tag{6.5}
\]
To check completeness of the list, lesson 6's disc calculation puts \(\ker(T-1)\) in stalk degree \(-1\) of \(j_{!*}(L[1])\), and gives zero in degree zero. The other two terms have stalk degrees \(-2\) and zero. They already account for all three dimensions of the central fibre. Any extra shifted point sheaf would add dimension in some degree, so none occurs. Formula (5.5) identifies the one-dimensional central \(H^1\) isomorphically with the invariant subspace of the two-dimensional nearby \(H^1\). It does not identify it with all nearby cohomology.

## 7. Exercises with complete solutions

### Exercise 1 — the exceptional coefficient

Compute both shifts of the direct image of the blow-up of \(\mathbb A^2\) at zero, including the arithmetic coefficient.

**Solution.** The smooth open fixes the full-support perverse constituent \(\Lambda_{\mathbb A^2}[2]\). The exceptional \(\mathbb P^1\) contributes stalk groups in degrees \(-2\) and zero after shifting by two, with coefficients \(\Lambda\) and \(\Lambda(-1)\). Duality gives the costalk bounds required for perversity. The full-support term uses the first stalk group, so semisimplicity leaves exactly \(i_*\Lambda(-1)\) as the second perverse term. Undoing the shift in (6.1) gives \(Rf_*\Lambda=\Lambda_{\mathbb A^2}\oplus i_*\Lambda(-1)[-2]\). Over \(\mathbb F_q\) the exceptional coefficient has geometric Frobenius eigenvalue \(q\), and both shifted summands are pure of weight two. There is no arithmetic twist in the classical formula.

### Exercise 2 — characters at a branch point

Decompose the unshifted direct image for \(z\mapsto z^2\) on \(\mathbb P^1\), and compute its branch-point stalks.

**Solution.** On a two-point fibre the involution exchanges the two coordinates of \(\Lambda^2\). Its invariant vector spans the trivial representation and its anti-invariant vector spans the sign representation. The two averaging projectors act on the global direct-image sheaf. At a branch point the fibre has one point and the involution acts trivially, so only the invariant summand has a stalk there. For the sign local system on \(\mathbb G_m\), the puncture complex has invertible differential \(-2\), proving zero boundary stalk and costalk for its IC extension. Thus \(f_*\Lambda=\Lambda\oplus(j_{!*}(L_-[1]))[-1]\). Formula (1.2) is its shift by one, with no skyscraper term. The projectors explicitly construct the splitting.

### Exercise 3 — the natural invariant-cycle map

Deduce global invariant cycles from (3.2), keeping track of which map is surjective.

**Solution.** Apply ordinary degree \(i\) to each IC summand and restrict to \(V\). The result is locally constant because it is a direct summand of \(\mathcal H^i(Rf_*K)|_V\). A support of dimension \(s\) contributes only for shift \(n=i+s\): in any other degree its generic stalk is zero, forcing the locally constant summand to vanish. Shrink its defining smooth open to \(U\subset V\cap Z\). The lowest-degree calculation (5.3) identifies both its degree-\(i\) global cohomology and its restricted section group with \(H^0(U,L)\). The edge and restriction map becomes the identity on that group. Sum these maps and identify \(R\Gamma(Y,Rf_*K)=R\Gamma(X,K)\); this gives precisely (5.2), not a newly chosen map. On a connected \(V\), parallel transport identifies its target with the invariant vectors in a fibre, and proper base change gives (5.4).

### Exercise 4 — the unique full-support resolution term

Determine the multiplicity and shift of IC in a resolution pushforward, and the resulting cohomological summand.

**Solution.** Choose a dense smooth open on which the resolution is an isomorphism, avoiding every smaller support in a decomposition. Its direct image there is the single rank-one perverse sheaf \(\Lambda[d]\). Exactly one full-support simple term can therefore occur, with shift zero and constant rank-one local system. Uniqueness of intermediate extension identifies that term with \(\operatorname{IC}_X\). Applying global cohomology in degree \(r-d\) gives (5.1). Multiplicity and the abstract constituent are intrinsic; the derived inclusion and projection come from the chosen splitting. Exceptional-fibre summands are not removed by the argument.

### Exercise 5 — the minimal resolution of \(xy=z^2\)

Construct the minimal resolution of this surface, over \(\mathbb C\) or over a finite field of odd characteristic with characteristic-zero étale coefficients. Determine the complete shifted direct image.

**Solution.** Let the tautological line \(\lambda\subset k^2\) vary over \(\mathbb P^1\), and map its square \(\lambda^{\otimes2}\) into \(\operatorname{Sym}^2k^2\). The total space is \(Y=\mathcal O_{\mathbb P^1}(-2)\), and the map sends a fibre coordinate to \((x,y,z)=(t u^2,t v^2,tuv)\). Rescaling \((u,v)\) rescales \(t\) inversely by its square, so the formula is well-defined. Its incidence equations are \(xv=zu\), \(zv=yu\) in \(X\times\mathbb P^1\).

On \(u\ne0\), put \(a=v/u\). The equations give \(z=ax\), \(y=a^2x\); hence \((x,a)\) are smooth coordinates. The other chart has coordinates \((y,u/v)\). Projection \(\pi:Y\to X\) is projective, is an isomorphism off the vertex, and has exceptional fibre \(\mathbb P^1\). Its normal bundle is \(\mathcal O(-2)\), so the sole exceptional curve has self-intersection \(-2\). It cannot be contracted to a smooth point. Indeed the coordinate transition \(y=a^2x\), \(b=1/a\) gives \(dy\wedge db=-dx\wedge da\), so the canonical line of \(Y\) restricts trivially to the exceptional curve \(E\). If a contraction \(g\) to a smooth surface existed, its Jacobian would identify \(K_Y\otimes g^*K_Z^{-1}\) with \(\mathcal O(aE)\) for a positive integer \(a\): it is invertible off \(E\) and vanishes on \(E\), where the differential kills its tangent direction. Restricting to \(E\), the left side has degree zero, since \(g(E)\) is a point. The right side has degree \(-2a\), a contradiction. Thus there is no further contraction to a smooth resolution, which gives minimality.

The vertex stalk of \(P=R\pi_*\Lambda[2]\) has \(\Lambda\) in degree \(-2\) and \(\Lambda(-1)\) in degree zero. Proper smooth-source duality says \(DP=P(2)\), giving costalk degrees zero and two. These bounds and the smooth open show perversity, and the decomposition theorem gives semisimplicity. The resolution argument supplies one full-support IC term. Formula (1.4), proved by finite quotient and projectors in both settings, identifies it with \(\Lambda_X[2]\). Its stalk consumes exactly the degree-\(-2\) coefficient. The only remaining term is therefore
\[
R\pi_*\Lambda_Y[2]\simeq\operatorname{IC}_X\oplus i_*\Lambda(-1).
\tag{7.1}
\]
Every other possible point term would add a stalk dimension. Unshifted, the terms are \(\Lambda_X\) and \(i_*\Lambda(-1)[-2]\). Over \(\mathbb F_q\), geometric Frobenius on the exceptional term is \(q\). The coefficient and the intersection number \(-2\) agree with the intersection-form calculation developed in the next lesson.

## Exact prerequisites still required

The finite-data classical/étale and specialization comparisons, including their stable lattices and compatibility with Chern maps, remain unproved inputs in §3. The rational IC-source version used in the resolution calculations is the version stated in de Cataldo–Migliorini, Theorem 1.6.1; its full coefficient passage must also be supplied. Lesson 7's ordinary weight, mixed-operation, curve-conductor and generic-local-acyclicity foundations, together with the exact normalized adic operations, remain prerequisites of §§3–4. The divisor class identity, smooth trace, finite and proper base change, and their coefficient comparisons must be checked at the precise versions used. The abstract splitting proof does not remove any of these obligations.

The small-ball comparisons specified before (5.5) require their exact earlier proof and recursive prerequisite check. The plumbing calculation in §6 refers to lesson 1's written smooth-flow, plane-curve, normalization and sheaf–singular arguments; their entire prerequisite closure is not established by this reference. Finally, the broader semisimple-source theorem stated in §3 remains an assigned proof obligation at its full stated generality. A free reference identifies the statement and supplies material for its eventual proof; it does not discharge any of these obligations.

## References

- A. Beilinson, J. Bernstein and P. Deligne, with results of O. Gabber, *Faisceaux pervers*, Astérisque **100** (1982): 5.3.8, 5.4.4–5.4.5, 5.4.10–5.4.15, 6.1 and 6.2.4–6.2.10. [Free original volume](https://www.numdam.org/item/AST_1982__100__1_0/).
- P. Deligne, *Théorème de Lefschetz et critères de dégénérescence de suites spectrales*, Publications Mathématiques de l'IHÉS **35** (1968), 107–126: Proposition 1.2, Theorem 1.5 and Remark 1.8. [Free original article](https://www.numdam.org/item/PMIHES_1968__35__107_0/).
- M. A. de Cataldo and L. Migliorini, *The decomposition theorem, perverse sheaves and the topology of algebraic maps*: Theorem 1.6.1, Remark 1.6.2 and §3. [Free author preprint](https://arxiv.org/abs/0712.0349).
- P. Deligne, [*Décompositions dans la catégorie dérivée*](https://publications.ias.edu/sites/default/files/68_Decompositionsdans.pdf), 1994: §1 and 2.4–2.5. Free author-hosted text.
- M. A. de Cataldo, *Decomposition theorem for semi-simples*, 2017 preprint: Theorems 2.1.1–2.1.2, Corollary 2.2.1 and §2.3. [Free author preprint, version 1](https://arxiv.org/abs/1702.06775v1).
