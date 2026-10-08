# Inverse limits and unbounded resolutions

*Written by GPT-6.1 Sol (OpenAI), in Codex at Ultra, October 2026, following Dolors Herbera, Wolfgang Pitsch, Manuel Saorín and Simone Virili, [A poisonous example to explicit resolutions of unbounded complexes, v3](https://arxiv.org/abs/2407.09741v3), §§2, 4 and 8.7. Self-checked by the writing AI. Original text: public domain (CC0). The lesson adds direct lifting and K-injectivity proofs, an explicit truncation calculation, totalization details and worked exercises. See the [course notice](../LICENCE.md).*

The [Grothendieck-category lesson](k-injective-resolutions-in-grothendieck-categories.md) constructs K-injective resolutions by exact filtered unions. Another method resolves successive lower truncations and takes their inverse limit. The second method needs a different exactness argument. Resolving each finite stage correctly does not by itself prove that its limit resolves the original complex.

The prerequisites are the common reading's cone and short-exact-sequence triangles; bounded-below injective resolutions and the Hom test for K-injectivity from [Injective modules and bounded-below derived functors](injective-modules-and-bounded-below-derived-functors.md), Sections 2–4; and the product argument of Proposition 5.4 in the [Grothendieck-category lesson](k-injective-resolutions-in-grothendieck-categories.md). That product argument applies in any abelian category with the required products, because its Hom complexes are complexes of abelian groups.

Throughout, \(\mathcal A\) is a complete, locally small abelian category with enough injectives. A DG-injective complex is termwise injective and K-injective. Write \(T_n=\tau^{\geq-n}X\) for the good lower truncation: its degree \(-n\) term is \(X^{-n}/B^{-n}X\), lower terms are zero, and higher terms agree with \(X\). The natural maps \(T_{n+1}\to T_n\) are chain maps. Each fixed degree eventually agrees with \(X\), so \(X=\lim_nT_n\) in complexes.

## 1. Building a compatible tower

**Lemma 1.1 (strict extension).** If \(A\hookrightarrow B\) is a monic quasi-isomorphism and \(I\) is DG-injective, every chain map \(A\to I\) extends to a chain map \(B\to I\).

**Proof.** Termwise injectivity gives a graded extension \(g\). Its defect \(Dg=d_Ig-gd_B\) vanishes on \(A\), hence factors through the acyclic quotient \(C=B/A\). In the Hom complex this factor is a degree-one cycle, since \(D^2g=0\). K-injectivity makes \(\operatorname{Hom}^{\bullet}(C,I)\) acyclic, so it is \(Dh\) for a degree-zero graded map \(h:C\to I\). Subtracting \(h\pi\) from \(g\), where \(\pi:B\to C\), kills the defect and retains the prescribed restriction to \(A\). \(\square\)

**Proposition 1.2 (resolution towers).** There are monic quasi-isomorphisms \(\lambda_n:T_n\to E_n\) with \(E_n\) bounded below and termwise injective, and chain maps \(t_n:E_{n+1}\to E_n\), such that
\[
t_n\lambda_{n+1}=\lambda_n(T_{n+1}\to T_n).
\]

Each \(t_n\) can be chosen degreewise split epic with bounded-below, termwise-injective kernel.

**Proof.** Choose a monic bounded-below injective resolution of \(T_0\). Given \(E_n\), choose one of \(T_{n+1}\), say \(T_{n+1}\hookrightarrow J\). Lemma 1.1 extends the displayed map into \(E_n\) to a chain map \(r:J\to E_n\). Bounded-below complexes of injectives are K-injective by the preceding lesson.

Put \(D=\operatorname{Cone}(1_{E_n})[-1]\), using the common reading's cone differential. Explicitly,
\[
D^q=E_n^{q-1}\oplus E_n^q,\qquad
d_D(a,b)=(-d a-b,d b).
\]

The chain projection \(p:D\to E_n\), \(p(a,b)=b\), is degreewise split epic; \(D\) is contractible. Replace \(J\) by \(E_{n+1}=J\oplus D\), its resolution map by \((\lambda,0)\), and its map to \(E_n\) by \((r,p)\). A graded section is \(b\mapsto(0,(0,b))\). Boundedness below and termwise injectivity persist. Each kernel term is a direct summand of an injective term and hence injective; its complex is bounded below. Adding the contractible summand preserves the monic quasi-isomorphism and the compatibility square. Induction constructs the tower. \(\square\)

## 2. What the limit always gives

**Lemma 2.1 (split towers).** For a degreewise split-epic tower \(K_{n+1}\xrightarrow{t_n}K_n\), there is a degreewise split exact sequence
\[
0\longrightarrow\lim_nK_n\longrightarrow\prod_nK_n
\xrightarrow{\,1-t\,}\prod_nK_n\longrightarrow0,
\qquad
(1-t)(b)_n=b_n-t_nb_{n+1}.
\]

**Proof.** The kernel is the limit by its universal property. Choose graded sections \(s_n\) of \(t_n\). For a coordinate family \(a\), define \(b_0=0\) and \(b_{n+1}=s_n(b_n-a_n)\). Each \(b_n\) uses only finitely many coordinates of \(a\), so these formulas define morphisms from the categorical product, without a notion of infinite summation. They give \(b_n-t_nb_{n+1}=a_n\), proving that \(1-t\) has a graded right inverse. These sections need not be chain maps. \(\square\)

**Proposition 2.2.** The limit \(E=\lim_nE_n\) of a resolution tower from Proposition 1.2 is DG-injective, without any exact-products hypothesis.

**Proof.** A product of K-injectives is K-injective: its Hom complex from an acyclic object is the product of acyclic complexes of abelian groups, and products in abelian groups are exact. K-injectives are closed under shifts and cones by that same Hom test. A degreewise split short exact sequence identifies its kernel in the homotopy category with the shifted cone of its epimorphism, as proved in the common reading. Apply this to Lemma 2.1 to prove K-injectivity of \(E\).

Products of injective objects are injective: maps into the product are families of maps into its factors, and a map from a subobject extends coordinate by coordinate. Lemma 2.1 also makes every \(E^q\) a direct summand of a product of injectives. Hence every term of \(E\) is injective. \(\square\)

This proves a property of the *target*. It has not proved that the natural map \(X\to E\) is a quasi-isomorphism. Cohomology of products in \(\mathcal A\) need not be the product of the cohomology objects.

## 3. Finite higher-product dimension

For a set \(J\), the category \(\mathcal A^J\) has componentwise injective resolutions. Define \(R^q\prod_J\) using these bounded-below resolutions. The condition **\(\mathrm{AB4}^{*}\!-\!k\)**, for an integer \(k\geq0\), means
\[
R^q\prod_J(A_j)=0\quad(q>k)
\]
for every set \(J\) and every family of objects. When \(k=0\), this says products are exact. This condition was introduced by Jan-Erik Roos; here we use the finite-dimensional form developed in the cited paper.

**Lemma 3.1 (product bound).** Suppose \(\mathcal A\) is \(\mathrm{AB4}^{*}\!-\!k\). Let \(K_n\) be bounded-below complexes of injectives with \(H^q(K_n)=0\) for every \(q\geq a\), uniformly in \(n\). Then
\[
H^q\!\left(\prod_nK_n\right)=0\quad(q>a+k+1).
\]

**Proof.** Let \(L_n\) be the brutal lower truncation of \(K_n\) in degree \(a+1\): it has \(K_n^q\) for \(q\geq a+1\) and zero below. Its terms are injective. Its degree-\((a+1)\) cohomology is \(Z^{a+1}K_n\), and its higher cohomology is zero. Thus it is an injective resolution of \(Z^{a+1}K_n\), placed in degree \(a+1\). The finite-product-dimension hypothesis gives
\[
H^q\!\left(\prod_nL_n\right)=0\quad(q>a+1+k).
\]

The inclusions \(L_n\to K_n\) are chain maps and are isomorphisms in all degrees at least \(a+1\). Their product is therefore an isomorphism in those degrees. Cohomology in degree \(q\) uses terms \(q-1,q,q+1\), so it induces a cohomology isomorphism for \(q>a+1\). This gives the asserted bound, including \(k=0\). The brutal truncation is important: the boundary term of a good lower truncation need not be injective. \(\square\)

**Corollary 3.2 (limit bound).** If the \(K_n\) in Lemma 3.1 also form a degreewise split-epic tower, then
\[
H^q(\lim_nK_n)=0\quad(q>a+k+2).
\]

**Proof.** The long exact sequence of Lemma 2.1 has \(H^{q-1}(\prod K_n)\) and \(H^q(\prod K_n)\) on either side of \(H^q(\lim K_n)\). Both vanish in the stated range by Lemma 3.1. \(\square\)

**Theorem 3.3 (the resolution theorem with its hypothesis).** In a complete abelian category with enough injectives satisfying \(\mathrm{AB4}^{*}\!-\!k\) for some finite \(k\), the map \(X\to\lim_nE_n\) from Proposition 1.2 is a DG-injective resolution of every unbounded complex \(X\). Neither exact filtered colimits nor a generator is required for this theorem.

**Proof.** Fix a stage \(h\). For \(n>h\), the composite \(E_n\to E_h\) is degreewise split epic. Let its kernel be \(K_n\). Its terms are injective and it is bounded below. The induced maps on cohomology are isomorphisms in degrees \(q\geq-h\), since the same is true for \(T_n\to T_h\), and \(H^{-h-1}(E_h)=0\). The exact sequence
\[
H^{q-1}(E_n)\to H^{q-1}(E_h)\to H^q(K_n)
\to H^q(E_n)\to H^q(E_h)
\]
then gives \(H^q(K_n)=0\) for \(q\geq-h\). At \(q=-h\), the needed preceding surjection has zero target \(H^{-h-1}(E_h)\); this verifies the endpoint separately. The maps of kernels remain degreewise split epic: a graded section of \(E_{n+1}\to E_n\) sends \(\ker(E_n\to E_h)\) into \(\ker(E_{n+1}\to E_h)\).

In each degree a graded section of \(E\to E_h\) can be constructed recursively, starting with an element at stage \(h\) and lifting it by the sections of the transitions. The coordinates are finite composites of morphisms from \(E_h\). Thus there is a degreewise split exact sequence
\[
0\to\lim_{n>h}K_n\to E\to E_h\to0.
\]

Corollary 3.2, with \(a=-h\), implies that the kernel has zero cohomology for \(q>-h+k+2\). Its long exact sequence therefore gives
\[
H^q(E)\xrightarrow{\sim}H^q(E_h)
\quad(q\geq-h+k+3).
\]

For any fixed \(q\), choose \(h\geq\max(0,k+3-q)\). The commuting resolution square identifies the composite \(H^q(X)\to H^q(E)\to H^q(E_h)\) with the isomorphism furnished by \(\lambda_h:T_h\to E_h\); also \(q\geq-h\). Hence \(H^q(X)\to H^q(E)\) is an isomorphism. Proposition 2.2 gives DG-injectivity. \(\square\)

The bounds used in this proof are sufficient bounds, not optimality claims.

| Object | Uniform cohomology vanishing used |
|---|---|
| \(K_n\) | \(q\geq a\) |
| \(\prod_nK_n\) | \(q>a+k+1\) |
| \(\lim_nK_n\) | \(q>a+k+2\) |
| \(E\to E_h\) | isomorphism for \(q\geq-h+k+3\) |

## 4. Products and Cartan–Eilenberg totalization

A Cartan–Eilenberg injective resolution of \(F\) is a bicomplex \(C^{p,q}\), \(p\geq0\), with an augmentation \(F^q\to C^{0,q}\). Its vertical columns resolve the terms of \(F\), and the vertical complexes of horizontal boundaries, cycles and cohomology resolve respectively \(B^qF,Z^qF,H^qF\). These resolutions have injective terms. We use anticommuting horizontal and vertical differentials and the product totalization
\[
\operatorname{Tot}^{\,n}C=\prod_{p+q=n,\ p\geq0}C^{p,q},
\qquad d_{\operatorname{Tot}}=d_h+d_v.
\]
Each output coordinate of the differential uses two input coordinates, so the formula defines a map of products.

Such a resolution exists. Here are the construction details needed for the totalization argument. For \(0\to A\to B\to D\to0\), given injective resolutions of \(A,D\), extend \(A\to I_A^0\) to \(B\to I_A^0\), and combine it with \(B\to D\to I_D^0\). The resulting \(B\to I_A^0\oplus I_D^0\) is monic: its kernel lies in \(A\), where the first map is monic. The cokernels form a short exact sequence \(0\to A_1\to B_1\to D_1\to0\), by the kernel–cokernel argument. Repeat on that sequence. Composing each quotient map with the next embedding defines the differentials. This proves the injective horseshoe construction with split columns.

Choose resolutions of \(B^qF\) and \(H^qF\). Apply the horseshoe first to \(0\to B^qF\to Z^qF\to H^qF\to0\), then to \(0\to Z^qF\to F^q\to B^{q+1}F\to0\). The terms \(C^{p,q}\) have graded decompositions
\[
C^{p,q}=I_{B^q}^{p}\oplus I_{H^q}^{p}\oplus I_{B^{q+1}}^{p}.
\]
The horizontal differential projects to the last summand and includes it as the first summand in column \(q+1\). Its square is zero; its boundary, cycle and cohomology objects are respectively the indicated \(B\), \(B\oplus H\), and \(H\) summands, hence injective. The horseshoe differentials commute with those inclusions and projections. Multiplying the vertical differential in column \(q\) by \((-1)^q\) makes the two differentials anticommute. This verifies all resolution conditions.

**Theorem 4.1 (valid product totalization).** Under \(\mathrm{AB4}^{*}\!-\!k\) for finite \(k\), the augmentation \(F\to\operatorname{Tot}C\) of any Cartan–Eilenberg injective resolution is a DG-injective resolution, even if \(F\) is unbounded.

**Proof.** For a lower bound \(b\), replace the horizontal complex in each row by its good lower truncation at \(b\): put zero in columns \(q<b\), put \(C^{p,b}/B^b(C^{p,\bullet})\) at \(q=b\), and leave \(q>b\) unchanged. Call the resulting bicomplex \(C_{\geq b}\). Because the boundary, cycle and cohomology terms are injective, their row sequences split; the quotient terms at \(b\) are injective. The vertical quotient column resolves \(F^b/B^bF\), by the short exact sequences of vertical resolutions. The other columns retain their resolutions. This is a Cartan–Eilenberg resolution of \(\tau^{\geq b}F\).

In the region \(p\geq0,q\geq b\), every total degree has finitely many terms. Exactness of its augmentation follows by finite elimination in the augmented columns. Specifically include \(F^q\) in vertical degree \(p=-1\). For a total cycle, its component in the least occupied \(q\) is a vertical cycle. Column exactness supplies a vertical preimage, whose total boundary removes that component and can only add a component in column \(q+1\). Repeating terminates: in a fixed total degree, \(p\geq-1\) bounds \(q\) above. Thus the augmented total complex is acyclic, proving the quasi-isomorphism. Its unaugmented total complex is bounded below with injective terms, so is DG-injective.

The maps \(\operatorname{Tot}C_{\geq-n-1}\to\operatorname{Tot}C_{\geq-n}\) are degreewise split epic. They discard the lowest column and quotient the new boundary column by its injective boundary summand; both operations have graded sections. The augmentations form a resolution tower of \(\tau^{\geq-n}F\). In each degree its inverse limit is the full product totalization: every fixed \(C^{p,q}\) is retained unchanged once the cut is below \(q\), and compatible finite-coordinate tuples are precisely tuples in the product. Theorem 3.3 now proves the claim. \(\square\)

The finite elimination just used cannot be applied directly to an unbounded horizontal complex: a correction could continue into infinitely many columns. The inverse-limit theorem supplies the missing justification under its stated hypothesis.

## 5. How an obstruction survives

Here is a conditional test for failure of a diagonal augmentation.

**Proposition 5.1 (diagonal obstruction criterion).** Let \(\mathcal G\) be an abelian category embedded fully in \(R\)-modules, with exact quotient functor \(Q:\operatorname{Mod}(R)\to\mathcal G\), left adjoint to the embedding, and kernel a torsion class \(\mathcal T\). Suppose products in \(\mathcal G\) are \(Q\) of module products. Let \(M\hookrightarrow I^\bullet\) be an injective resolution in \(\mathcal G\) with \(I^q=0\) for \(q<0\), viewed in modules, with
\[
M\xrightarrow{\sim}H_R^0(I),\qquad H_R^j(I)=T_j\in\mathcal T\quad(j>0),
\]
If \(\prod_{j>0}T_j\notin\mathcal T\), then the diagonal map from the complex having \(M\) in every integer degree and zero differential to
\(\prod_{i\in\mathbb Z}I[-i]\), computed in \(\mathcal G\), is not a quasi-isomorphism. Nevertheless its target is K-injective, and it is the limit of valid bounded-below partial resolutions with split-epic transitions.

**Proof.** Module products are exact, so their cohomology is computed coordinatewise. In degree \(n\), the module product \(J=\prod_{i\in\mathbb Z}I[-i]\) has
\[
H_R^n(J)=M\times\prod_{j>0}T_j.
\]
The diagonal map induces inclusion of the \(M\) coordinate. Its module cone therefore has cohomology \(\prod_{j>0}T_j\) in every degree. Exactness of \(Q\) preserves kernels, cokernels and the cone, so its cone in \(\mathcal G\) has cohomology \(Q(\prod_{j>0}T_j)\ne0\). Thus it is not a quasi-isomorphism.

The partial product \(\prod_{i\geq-h}I[-i]\) is locally finite in each degree, since \(I\) starts in degree zero. It is a bounded-below injective resolution of the corresponding lower truncation of the zero-differential complex. The transitions are projections, with kernel the additional shifted copy of \(I\). Their inverse limit is the full product. The product Hom argument proves its K-injectivity. \(\square\)

Proposition 5.1 identifies a sufficient obstruction under its explicit hypotheses. The lesson has not constructed a category and resolution satisfying all those hypotheses. Sections 1–4 prove that a split resolution tower has a DG-injective limit target and that its augmentation is a quasi-isomorphism under the stated finite higher-product-dimension hypothesis. The exact-filtered-union proof in the earlier Grothendieck-category lesson establishes existence independently of that hypothesis.

For further study of examples, see Herbera–Pitsch–Saorín–Virili, [§3](https://arxiv.org/html/2407.09741v3#S3), and Chachólski, Neeman, Pitsch and Scherer, [*Relative homological algebra via truncations*, §8](https://arxiv.org/abs/1702.05357). These are optional reading routes; their example calculations are not used as proved results here.

## 6. Finite coresolutions as a source of the hypothesis

Read Proposition 6.1 now. Before Theorem 6.2, continue with Sections 1–2 of [Quasi-coherent sheaves and concentrated scheme maps](quasi-coherent-sheaves-and-concentrated-maps.md#1-affine-sheaves-and-localization), which prove its scheme prerequisites, then return here. The tower construction needed later in that lesson is already proved in Sections 1–2 above.

### Finite coresolutions

**Proposition 6.1.** Suppose there is an objectwise exact sequence of endofunctors
\[
0\to1_{\mathcal A}\to F_1\to\cdots\to F_{n+1}\to0
\]
and every family \((F_iA_j)_j\) is product-acyclic, meaning its higher derived products vanish. Then \(\mathcal A\) satisfies \(\mathrm{AB4}^{*}\!-\!n\).

**Proof.** Put \(K_1=1_{\mathcal A}\) and \(K_{n+1}=F_{n+1}\); the intermediate kernels give \(0\to K_i\to F_i\to K_{i+1}\to0\). Apply the long exact derived-product sequence to each family. For \(q\geq2\), acyclicity of \(F_i\) identifies
\[
R^q\prod_J K_i(A_j)=R^{q-1}\prod_J K_{i+1}(A_j).
\]
If \(q>n\), repeat this \(n\) times to obtain \(R^{q-n}\prod_J F_{n+1}(A_j)=0\). For \(n=0\), the given sequence identifies the identity with \(F_1\), so acyclicity itself gives exact products. \(\square\)

For the following geometric application use [Quasi-coherent sheaves and concentrated scheme maps, Theorem 1.2 and Proposition 1.3](quasi-coherent-sheaves-and-concentrated-maps.md#1-affine-sheaves-and-localization) for the exact affine module equivalence, localization and restriction formulas. Its [Theorem 2.1 and Lemma 2.2](quasi-coherent-sheaves-and-concentrated-maps.md#2-small-submodules-and-enough-injectives) prove Gabber's small-submodule construction, the Grothendieck-category consequence and the existence of quasi-coherent limits. These full scheme prerequisites are needed for Theorem 6.2; Sections 1–5 and Proposition 6.1 require none of them.

### Finite affine-cover bound

**Theorem 6.2 (finite affine-cover bound).** Let \(X\) be a quasi-compact semi-separated scheme with an affine open cover \(V_1,\ldots,V_{n+1}\), where \(n\geq0\). Then \(\operatorname{QCoh}(X)\) satisfies \(\mathrm{AB4}^{*}\!-\!n\). Thus the tower and Cartan–Eilenberg resolution theorems apply to all unbounded complexes in this category.

**Proof.** The cited Theorem 2.1 and Lemma 2.2 make this category Grothendieck and supply all limits and enough injectives. Semi-separatedness says intersections of affine opens are affine. For any such intersection \(V\), let \(j_V:V\hookrightarrow X\). Restriction \(j_V^*\) is exact and is left adjoint to \(j_{V*}\) on quasi-coherent sheaves. The latter preserves quasi-coherence and is exact in this category: on an affine open \(W\subset X\), its sections are sections of the original quasi-coherent sheaf on the affine \(W\cap V\). On \(D(f)\subset W\) these sections are the localization at \(f\), verifying quasi-coherence, and the affine equivalence verifies exactness. This argument applies to every affine \(W\).

Being a right adjoint to exact restriction, \(j_{V*}\) preserves products and injectives. For a family \(A_\lambda\) on \(V\), resolve each by injectives in \(\operatorname{QCoh}(V)\). Pushing those resolutions forward still gives injective resolutions. Product preservation and exactness give
\[
R^q\prod_{\operatorname{QCoh}(X)}(j_{V*}A_\lambda)
=j_{V*}R^q\prod_{\operatorname{QCoh}(V)}(A_\lambda)=0\quad(q>0),
\]
since the affine equivalence identifies the latter products with exact module products.

The ordered Čech sequence for the finite cover is
\[
0\to F\to
\bigoplus_i j_{V_i*}F|_{V_i}\to
\bigoplus_{i<j}j_{V_i\cap V_j*}F|_{V_i\cap V_j}
\to\cdots\to j_{V_1\cap\cdots\cap V_{n+1}*}F|_{V_1\cap\cdots\cap V_{n+1}}\to0.
\]
The differentials are alternating restrictions. It is exact as a sequence of sheaves: restrict to a cover member \(V_i\), and insertion of that index into a strictly ordered tuple, with the sign of its position, contracts the augmented Čech complex. Intersections with \(V_i\) identify the relevant restricted direct-image terms, so this contraction is a sheaf-map identity on that open. Exactness is local, hence holds globally. Empty intersections contribute zero. Every term is quasi-coherent.

Let the \(n+1\) Čech endofunctors be \(F_1,\ldots,F_{n+1}\). Every family of their values is product-acyclic by the preceding calculation and finite additivity of derived products: there are only finitely many intersections in each term. Proposition 6.1 gives \(\mathrm{AB4}^{*}\!-\!n\), with the same value of \(n\) as the cover bound. Apply Theorems 3.3 and 4.1. \(\square\)

This is the bound proved by Herbera–Pitsch–Saorín–Virili in [§8.7](https://arxiv.org/html/2407.09741v3#S8.SS7). It concerns products and direct images *within* the quasi-coherent category. The same open direct image on all module sheaves need not be exact.

## 7. Exercises with complete solutions

**Exercise 1.** In Theorem 3.3, give a sufficient stage for computing \(H^{-10}(X)\) when \(k=2\). Why is stage \(10\) not justified by the displayed estimate?

**Solution.** The estimate is \(q\geq-h+k+3\). With \(q=-10,k=2\), it gives \(h\geq15\). Stage \(10\) identifies the cohomology of its truncation with that of \(X\), but the estimate comparing that stage with the inverse limit only starts in degree \(-5\). The distinction is between correct finite truncation and justified passage to the limit.

**Exercise 2.** Why does Lemma 2.1 not prove that inverse limits are exact in \(\mathcal A\)?

**Solution.** It describes one tower whose transitions have graded sections. In a short exact sequence of arbitrary towers, the products entering the three sequences need not preserve epimorphisms, and the corresponding map of kernels need not be epic. Neither the splitting of \(1-t\) for these particular complexes nor its generally non-chain sections establishes exactness of the inverse-limit functor.

**Exercise 3.** Let \(R\) be any associative unital ring. Which existence proof applies to all unbounded complexes of left \(R\)-modules?

**Solution.** Module products are exact by coordinatewise lifting, so \(\mathrm{AB4}^{*}\!-\!0\) holds; modules have enough injectives and all limits. Theorem 3.3 therefore gives the tower proof. Module categories are also Grothendieck, so the earlier filtered-union proof applies independently. The two proofs use different hypotheses, both satisfied here.

**Exercise 4.** Does the obstruction criterion imply that a product of K-injectives fails to be K-injective?

**Solution.** No. Its target is K-injective by Proposition 2.2 and the product Hom argument. The cone calculation proves that the chosen map into that target fails to be a quasi-isomorphism. A resolution requires both the target property and the quasi-isomorphism.
