# Proper pushforwards of nearby and vanishing cycles

A map need not be proper on its entire source for its pushforward to commute with nearby and vanishing cycles. Properness on the sheaf's support suffices. The proof must keep this support after passing to the covering or to coefficient Hom; otherwise a later base-change step can silently lose its hypothesis.

We prove the two comparisons with their actual natural maps, monodromy, and both canonical/variation triangles. We then apply them to the graph of an arbitrary holomorphic function. The proper-map comparison is stated in David B. Massey’s freely accessible [*Notes on Perverse Sheaves and Vanishing Cycles*, version 13, §3](https://arxiv.org/html/math/9908107v13#p370). Massey states the comparison for proper maps with his constructible coefficients. The stronger proper-on-closed-support assertion below is established relative to the stated ordinary adjunction and proper-support base-change theorems. Its proof follows the support carrier through each operation, identifies the comparison map, and checks its compatibility with the two coefficient triangles. Those additional steps and the broader coefficient scope are not supplied by the cited statement.

*Written by GPT-6.1 Sol (OpenAI), Ultra, October 2026. New original text is public domain (CC0).*

## Maps and zero fibres

Let \(g:Z\to X\) be holomorphic between finite-dimensional complex manifolds, and let \(h:X\to\mathbb C\) be holomorphic. Set

\[
Y_X=h^{-1}(0),\quad Y_Z=(h\circ g)^{-1}(0),
\quad i_X:Y_X\hookrightarrow X,\quad i_Z:Y_Z\hookrightarrow Z.
\]

The induced map \(g_0:Y_Z\to Y_X\) gives the cartesian square

\[
\begin{array}{ccc}
Y_Z&\xrightarrow{g_0}&Y_X\\
\scriptstyle i_Z\downarrow&&\downarrow\scriptstyle i_X\\
Z&\xrightarrow{g}&X.
\end{array}
\tag{1}
\]

Neither zero fibre is required to be smooth. All inverse images and direct images on them are sheaf operations on their underlying locally compact spaces.

Let \(F\in D^b(k_Z)\), with the same finite-global-dimension commutative ring as before. Assume \(g\) is proper on a closed support carrier \(S\) of \(F\). Thus \(F|_{Z\setminus S}=0\), and \(g|_S:S\to X\) is proper. This is the hypothesis used at every base-change step below; it permits arbitrary behaviour of \(g\) away from the support. The formal comparisons below require no constructibility of \(F\). In particular they apply to its stated weakly complex-constructible inputs, including infinite coefficient modules.

Use the coefficient sheaf \(L\), complex \(K\), deck action \(T\), and maps \(\beta,\gamma\) constructed in Nearby cycles and the two monodromy triangles. On \(X\) the coefficients are \(h^{-1}L,h^{-1}K\), and on \(Z\) they are \((h\circ g)^{-1}L,(h\circ g)^{-1}K\). Their inverse-image identification is exact.

## Internal Hom preserves the support carrier

For an ambient coefficient complex \(A\), put

\[
H_A(F)=R\mathcal Hom_Z(g^{-1}A,F).
\tag{2}
\]

Its restriction to \(Z\setminus S\) is zero: restriction of derived internal Hom to an open set is internal Hom of the restrictions, and the second restriction is zero. Thus \(S\) is a support carrier for \(H_A(F)\), even if \(A\) has infinite-rank stalks or is supported everywhere. This uses the support of the second Hom argument, not a claim that its first argument is perfect.

There is a canonical ordinary inverse/direct internal adjunction

\[
Rg_*H_A(F)\simeq R\mathcal Hom_X(A,Rg_*F).
\tag{3}
\]

Here is its application proof, using the existing derived ordinary adjunction. Test the left object against a variable \(E\) in the ordinary derived category:

\[
\begin{split}
\operatorname{Hom}(E,Rg_*R\mathcal Hom(g^{-1}A,F))
&\simeq\operatorname{Hom}(g^{-1}E,R\mathcal Hom(g^{-1}A,F))\\
&\simeq\operatorname{Hom}(g^{-1}E\otimes^L g^{-1}A,F)\\
&\simeq\operatorname{Hom}(g^{-1}(E\otimes^L A),F)\\
&\simeq\operatorname{Hom}(E\otimes^L A,Rg_*F)\\
&\simeq\operatorname{Hom}(E,R\mathcal Hom(A,Rg_*F)).
\end{split}
\tag{4}
\]

Exact inverse image for constant coefficients commutes with derived tensor: its stalks pull back the same flat resolutions. Yoneda gives (3). The isomorphism is natural in \(A,F\); applying the same argument on open subsets gives the internal-Hom and restriction compatibilities. For the bounded objects used here, ordinary derived adjunction has the following direct construction. The inverse-image presheaf and sheafification give the usual sheaf adjunction. Inverse image is exact because its stalk at a source point is the original stalk at its image. Its right adjoint therefore preserves injective sheaves: applying the Hom test for injectivity reduces to this exact inverse image. Resolve the second argument by a bounded-below complex of injectives and apply the sheaf adjunction degree by degree. The resulting isomorphism of Hom complexes computes the derived morphisms, since a bounded-below injective complex is homotopically injective. It is compatible with restriction and with the unit and counit inherited from sheaves. This is the ordinary part (A8) of Duality maps for constructible inverse and direct images. The existence of injective resolutions, their computation of derived morphisms, and the tensor–Hom adjunction used in (4) remain explicit algebraic prerequisites; the finite-dimensional bound below puts the resulting objects in the bounded category.

For the particular \(A=h^{-1}L\), formula (7) of the preceding lesson identifies \(H_A(F)\) with the ordinary direct image from the pulled-back covering. Its boundedness follows from finite manifold cohomological dimension. For \(A=h^{-1}K\), its coefficient triangle then gives boundedness from this covering object and \(F\). The constant and zero-fibre coefficient terms are bounded for the same reason. Thus every proper-support operation used below is on a bounded input. No unfinished unbounded proper-direct-image extension is used.

## Ordinary base change is invertible on these supports

For every bounded object \(B\) supported on \(S\), forgetting support gives an isomorphism

\[
Rg_!B\xrightarrow{\sim}Rg_*B.
\tag{5}
\]

Indeed the closed-embedding factorization \(B\simeq (a_S)_*(B|_S)\) reduces the map to proper direct image along \(g|_S\). The finite-dimensional proper-support and proper-map comparisons supply this assertion. After the base change (1), \(g_0\) is proper on \(S_0=S\cap Y_Z\), so the same assertion applies to \(i_Z^{-1}B\).

Combine (5) with the existing arbitrary proper-support base-change bridge:

\[
\begin{split}
i_X^{-1}Rg_*B
&\simeq i_X^{-1}Rg_!B\\
&\simeq R(g_0)_!i_Z^{-1}B\\
&\simeq R(g_0)_*i_Z^{-1}B.
\end{split}
\tag{6}
\]

The natural transformation is the ordinary base-change map. The support-forgetting compatibility for proper-support base change states that pulling back a properly supported section and forgetting its support agrees with first forgetting support and then applying ordinary base change. Consequently (6) establishes invertibility of the actual ordinary comparison, not merely the existence of an isomorphism with its target. The underlying soft, fibre, composition and topology primitives remain open imported proofs.

Formula (2) showed why the same properness applies after coefficient Hom. Applying (6) to \(H_A(F)\) and then (3) gives

\[
i_X^{-1}R\mathcal Hom_X(A,Rg_*F)
\simeq R(g_0)_*\,i_Z^{-1}R\mathcal Hom_Z(g^{-1}A,F).
\tag{7}
\]

Everything is natural in the coefficient argument \(A\).

## Both cycle comparisons and both triangles

Take \(A=h^{-1}L\) in (7) and use the coefficient description of nearby cycles. Take \(A=h^{-1}K\) for vanishing cycles. We obtain

\[
\psi_h(Rg_*F)\simeq R(g_0)_*\psi_{h\circ g}(F),
\qquad
\phi_h(Rg_*F)\simeq R(g_0)_*\phi_{h\circ g}(F).
\tag{8}
\]

The spaces of both sides are \(Y_X\). No extra dimension shift or orientation line appears: these are ordinary direct images and ordinary restrictions of the same coefficient Hom functors. In particular the source-normalized \([-1]\) in the two monodromy triangles stays unchanged.

For \(A=k_X\), formula (7) gives the ordinary restriction comparison

\[
i_X^{-1}Rg_*F\simeq R(g_0)_*i_Z^{-1}F.
\tag{9}
\]

For \(A=k_{Y_X}\), its inverse image is \(k_{Y_Z}\); the supported-Hom formula gives

\[
i_X^!Rg_*F\simeq R(g_0)_*i_Z^!F.
\tag{10}
\]

This proves the exceptional comparison directly from the same supported coefficient argument. It does not identify exceptional and ordinary restrictions.

The two coefficient triangles involve precisely \(k_X,h^{-1}K,h^{-1}L[1]\) and \(h^{-1}L[1],h^{-1}K,k_{Y_X}\). Since (7) is natural for every map among these coefficients, it commutes with their actual \(\beta,\gamma\) and quotient maps. Thus applying \(R(g_0)_*\) to either source monodromy triangle gives the corresponding target triangle under (8)–(10), including its canonical and variation maps. Naturality for \(T\) identifies the two monodromies. Both \(1-M\) composition identities are preserved. We did not choose an arbitrary isomorphism between two cone objects to conclude this compatibility.

## The covering proof has the same support condition

The nearby comparison can also be followed through its original covering definition. Form the cartesian map

\[
\widetilde g:\widetilde U_Z\longrightarrow\widetilde U_X,
\qquad q_X\widetilde g=gq_Z.
\]

The map \(\widetilde g\) is proper on \(q_Z^{-1}S\), the base change of the carrier. The ordinary base-change map

\[
q_X^{-1}Rg_*F\longrightarrow R\widetilde g_*q_Z^{-1}F
\tag{11}
\]

is invertible by the same proper-support/ordinary compatibility as (6). Composition of ordinary direct images gives

\[
Rq_{X*}q_X^{-1}Rg_*F
\simeq Rg_*Rq_{Z*}q_Z^{-1}F.
\tag{12}
\]

The last covering direct image is still supported on \(S\): an open set outside the closed carrier pulls back to a set where the sheaf vanishes. Therefore ordinary base change to the zero fibre is again legitimate. Restricting (12) recovers the first comparison in (8). This explains both appearances of support properness in a covering proof. Merely asserting that the covering map is proper would be incorrect; it has infinitely many sheets and no fibre at zero.

## The graph construction has a zero-extension term

For an arbitrary holomorphic \(f:Z\to\mathbb C\), let

\[
\Gamma_f:Z\longrightarrow\mathbb C\times Z,
\quad z\longmapsto(f(z),z),
\qquad t:\mathbb C\times Z\to\mathbb C.
\]

The graph is a closed embedding and hence proper. The ambient zero fibre is \(\{0\}\times Z\simeq Z\), while the original zero fibre is \(Y=f^{-1}(0)\). The induced zero-fibre graph map is the closed inclusion \(a:Y\hookrightarrow Z\). Formula (8) reads, as sheaves on that ambient \(Z\),

\[
\psi_t((\Gamma_f)_*F)\simeq a_*\psi_f(F),
\qquad
\phi_t((\Gamma_f)_*F)\simeq a_*\phi_f(F).
\tag{13}
\]

All these closed direct images are exact. Restriction to \(Y\) recovers the original cycle objects. The explicit \(a_*\) records their support and types; the two zero fibres are not silently the same space. This permits a comparison for arbitrary \(f\) to use the regular projection \(t\) in a graph ambient space, without pretending that \(df\) was nonzero on its original zero fibre. The normal-specialization and microlocalization identifications for that projection remain separate proofs.

## Exercises

### 1. Proper only on a section
*Difficulty: Intermediate.*

Let \(g:\mathbb C^2\to\mathbb C\) be \(g(x,y)=x\), let \(S=\{y=0\}\), and let \(F=k_S\). Put \(h(x)=x^2\). Verify the support hypothesis, compute \(Rg_*F\), and compute both sides of (8) at zero.

**Solution.** The whole projection is not proper, since its fibres are complex lines. Its restriction to the closed section \(S\) is an isomorphism, hence proper. The closed-supported constant sheaf therefore has \(Rg_*F=k_{\mathbb C}\) with no higher cohomology. On the source support the function is also \(x^2\). Its pulled-back punctured section has two contractible lifted components, giving nearby cycles \(k^2\), supported at the single source point \((0,0)\). Its vanishing object is \((k^2/k(1,1))[-1]\).

The map \(g_0\) sends the whole source zero fibre \(\{x=0\}\) to a point, but it is proper on the support of either cycle object, the one point \((0,0)\). Its pushforward leaves the displayed modules unchanged. The target constant sheaf with \(h=x^2\) has exactly those nearby and vanishing objects by the ramification calculation. This checks (8) for a genuinely nonproper whole-source map while retaining properness at every relevant supported stage.

### 2. A finite ramified pushforward
*Difficulty: Intermediate.*

Let \(m\) be a positive integer. Take \(g(z)=z^m\) on \(\mathbb C\), \(h(x)=x\), and \(F=k_{\mathbb C}\). Describe \(Rg_*F\) at and away from zero. Compute its cycles for \(h\), and identify the maps with the cycles for \(h\circ g\).

**Solution.** The finite map is proper. Away from zero it is an \(m\)-sheet covering, so the pushforward is a local system with fibre \(k^m\); looping permutes its sheets. At zero, the inverse image of a small disc is a disc, with constant cohomology \(k\) in degree zero and no higher terms. Thus \(Rg_*F\) is an ordinary sheaf with central stalk \(k\), generic module \(k^m\), and diagonal restriction map. There are no positive-degree direct-image cohomology sheaves, by the same local calculation everywhere.

Its nearby object for \(h\) is \(k^m\) and its vanishing object is \((k^m/k(1,\ldots,1))[-1]\). These are precisely the cycles of \(z^m\) on the source constant sheaf. The zero-fibre map is the identity of a point. Under the common sheet convention, monodromy is the same cyclic action, canonical is the quotient, and variation is the map induced by \(1-M\). This works over every allowed ring, including when its characteristic divides \(m\).

### 3. Remove support properness
*Difficulty: Advanced.*

Let \(g:\mathbb C^*\hookrightarrow\mathbb C\) be the open inclusion, \(h(x)=x\), and \(F=k_{\mathbb C^*}\). Calculate both sides of each comparison in (8). Does weak complex constructibility rescue the comparisons?

**Solution.** The source function \(h\circ g\) has empty zero fibre. Both source cycle objects are therefore zero, and the right sides of (8) are zero. On the target, \(Rg_*F=Rj_*k\). Its restriction to the punctured disc is constant, so its nearby cycles are \(k\), in degree zero. Its costalk at zero is zero by localization, while its central derived restriction has \(k\) in degrees zero and one. The second monodromy triangle therefore gives vanishing cycles \(k[-1]\). Both left sides are nonzero for a nonzero coefficient ring.

The sheaf on the source is perfect complex constructible, and the target direct image has finite complex-constructible cohomology on the punctured-disc/centre partition. Thus even this stronger coefficient property does not rescue either comparison. The inclusion is not proper on the support: sequences approaching zero escape the source over a compact neighborhood of zero. This is exactly the hypothesis missing from the theorem.

### 4. Type the graph comparison
*Difficulty: Introductory.*

For a possibly singular zero fibre \(Y=f^{-1}(0)\), identify the spaces carrying each term in (13). Prove that restriction gives the original cycles, and explain why the ambient regular projection does not force \(df\neq0\).

**Solution.** The function \(t\) is defined on \(\mathbb C\times Z\), with zero fibre \(\{0\}\times Z\), identified with \(Z\). Thus its two cycle objects on the left of (13) live on \(Z\). The function \(f\) is defined on \(Z\), so its cycles on the right before applying \(a_*\) live on \(Y\). The zero-fibre graph map is \(a:Y\hookrightarrow Z\); its exact closed pushforward puts those cycles on \(Z\), supported on \(Y\). Closed restriction satisfies \(a^{-1}a_*\simeq\mathrm{id}\), giving the original objects on \(Y\).

The derivative of \(t\) in the ambient first coordinate is nonzero everywhere. The derivative of its restriction to the graph is \(df\), which can vanish. A regular ambient projection and a ramified or critical restricted function are compatible. For \(f(z)=z^2\) the graph proof applies even though \(df(0)=0\), and its nonzero vanishing cycles are extended from the one-point original zero fibre into the ambient zero fibre.

### 5. Check the exceptional triangle at a branch point
*Difficulty: Advanced.*

For the finite map in Exercise 2, prove that the costalk of \(Rg_*k_{\mathbb C}\) at zero is \(k[-2]\). Check this directly from its variation triangle, without dividing by \(m\).

**Solution.** Formula (10) gives the pushforward of the source constant-sheaf point costalk. On the complex line the real orientation is canonical and the point has real codimension two, so that costalk is \(k[-2]\). The zero-fibre map is the identity, giving the asserted object.

For the direct check, put \(V=k^m\), \(D=k(1,\ldots,1)\) and \(Q=V/D\). Variation is \(r:Q\to V\), \(r(\overline v)=(1-M)v\), in degree one. The kernel of \(1-M\) on \(V\) is exactly \(D\), by equality of every cyclic coordinate. Thus \(r\) is injective. Its image is the kernel of the summation \(V\to k\): one inclusion follows by telescoping, and the reverse inclusion is solved by successive cyclic differences, whose consistency is exactly the zero-sum condition. Summation is surjective by one coordinate, so its cokernel is \(k\). The fibre of \(Q[-1]\xrightarrow{r}V[-1]\) has only degree-two cohomology \(k\), namely \(k[-2]\), as required. This proof includes characteristic dividing \(m\); in characteristic two at \(m=2\), the variation image is the diagonal but remains an injective image of \(Q\).

### 6. Infinite coefficients do not require a perfect Hom factor
*Difficulty: Intermediate.*

Over a field let \(V=\bigoplus_{r\geq1}k\), and replace the source constant sheaf in Exercise 2 by \(V_{\mathbb C}\). Calculate the cycle objects and explain which part of the comparison proof permits these nonperfect coefficients.

**Solution.** Each small lifted component is contractible, with constant cohomology \(V\) in degree zero. The nearby object is \(V^m\), and the central restriction is the diagonal \(V\to V^m\). Vanishing cycles are \((V^m/\operatorname{diag}V)[-1]\), and monodromy permutes the finitely many components. Canonical and variation are again the quotient and the induced \(1-M\). The diagonal splits by any coordinate projection, so the quotient is isomorphic to \(V^{m-1}\), without a finite-dimensional assumption.

The sheaf is weakly complex constructible and is not perfect, because its stalks are infinite-dimensional. Formula (4) uses ordinary adjunction and derived tensor–Hom adjunction, neither of which demands a perfect first Hom argument. Formula (2) keeps the support carrier using the second argument, regardless of its rank. Properness belongs to the finite map and its carrier. These are exactly the ingredients permitting the weak example; no finite-dimensional dual-tensor identification or perfect projection-formula assertion is substituted.

## What has been established

Both proper-on-support cycle comparisons, both monodromy-triangle comparisons, and the typed graph construction are proved for bounded inputs, with singular zero fibres and arbitrary weak coefficients allowed. The finite-dimensional proper-support, ordinary adjunction and topology primitives remain the exact imported foundations. Normal-specialization/microlocal comparisons, cycle constructibility in full generality, the holomorphic microsupport test criterion and the quadratic model remain separate results. This lesson uses the sheaf-operation and topology prerequisites specified above; it does not prove their full foundational theory.
