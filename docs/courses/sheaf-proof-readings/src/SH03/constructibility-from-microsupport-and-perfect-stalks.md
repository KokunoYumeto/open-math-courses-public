# Constructibility from microsupport and perfect stalks

Constructibility combines geometric control with a coefficient condition. The geometric part says that cohomology sheaves are locally constant on suitable subanalytic pieces; equivalently, their directional support is contained in a subanalytic isotropic cotangent set. The coefficient part asks that the stalk complexes be perfect. We prove the geometric equivalence, keeping the μ-condition that controls approaches between strata, and then explain the resulting categories.

Let \(k\) be a commutative ring of finite global dimension. Let \(X\) be a finite-dimensional real analytic manifold, Hausdorff and countable at infinity. We work with \(F\in D^b(k_X)\). Bounded means a finite global cohomological degree interval. Local finiteness and subanalyticity are in the ambient manifold. No finite-generation assumption is made for the weak constructibility results. Noetherian hypotheses will be stated where used.

Use Microlocal stratifications by removing bad loci, Unshared conormal directions and dimension filtrations, and Involutive subsets of subanalytic isotropic sets. The full tensor estimate, missing-submanifold boundary estimate, and involutivity of the entire microsupport have exact programme proofs with their stated coefficient scopes. The closed-embedding formula and zero-section local-constancy criterion, including bounded derived local descent, now have explicit programme proofs in the companion lesson. We state the application contracts below. Their transitive foundational audits remain open. For eligible human-source context, Hohl and Schapira’s [*Unusual functorialities for weakly constructible sheaves*](https://arxiv.org/abs/2303.11189v2), §4, recalls the isotropic and Lagrangian descriptions and the perfect-stalk definition. It does not supply their proofs. We prove the equivalences here through restriction to a stratum and extension from its complement, using the exact programme estimates below. Schapira’s [*A short review on microlocal sheaf theory*](https://webusers.imj-prg.fr/~pierre.schapira/LectNotes/MuShv.pdf), §2.2–2.3, supplies further context for local support tests, the zero-section criterion and the closed-embedding formula. The distinction between those statements and complete programme proofs is retained.

*Programme text begun by GPT-6.1 Sol (OpenAI), Ultra, September 2026; developed by GPT-6 Astra (OpenAI), Ultra, October 2026. Independently written programme expression is public domain (CC0).*

<span id="the-exact-sheaf-estimates-used-here"></span>

## The exact sheaf estimates used here {#constructibility-inputs}

For bounded sheaf complexes, the full tensor estimate is

\[
\operatorname{SS}(F\otimes^L G)
\subset\operatorname{SS}(F)\widehat{+}\operatorname{SS}(G).
\tag{1}
\]

It requires neither constructibility nor a noncharacteristic condition. The \(\widehat{+}\) operation retains unbounded cancelling covectors and the position-covector product established in Limiting cotangent sums and characteristic inverse images.

If \(i:S\hookrightarrow U\) is a closed smooth embedding and \(H\in D^b(k_S)\), the exact cotangent formula is

\[
\operatorname{SS}(i_*H)=i_\pi i_d^{-1}\operatorname{SS}(H).
\tag{2}
\]

Here \(i_d:T^*U|_S\to T^*S\) restricts a covector to the tangent of \(S\), and \(i_\pi\) includes that covector in \(T^*U\). Restriction is surjective, and its kernel is \(T_S^*U\). Consequently (2) gives

\[
\operatorname{SS}(i_*H)\subset T_S^*U
\quad\Longleftrightarrow\quad
\operatorname{SS}(H)\subset T_S^*S.
\tag{3}
\]

The proved zero-section criterion identifies the right side with every \(H^j(H)\) being locally constant. It also retains the bounded derived local-descent statement: on a sufficiently small contractible chart, \(H\) is a constant bounded coefficient complex. It does not discard extension data between cohomology degrees.

For a closed smooth \(S\subset U\), its open complement \(j:U\setminus S\hookrightarrow U\), and \(K\in D^b(k_{U\setminus S})\), the boundary estimate we use is

\[
\operatorname{SS}(j_!K)\cap T^*U|_S
\subset\operatorname{SS}(K)\widehat{+}T_S^*U.
\tag{4}
\]

The first microsupport on the right is regarded in \(T^*U|_{U\setminus S}\) and need not be ambient closed. There is no properness hypothesis on the open embedding. The exact missing-submanifold estimate applies to both ordinary and zero extensions, but the localization triangle below uses \(j_!\). Finally, microsupport is local, obeys the triangle inequality, and is a closed conic involutive set for every bounded \(F\), including its singular points and zero covectors.

The uniform compact-cap proof and extension-continuity calculations supply preliminary steps for the limiting estimates. The directional projector and cap-test converse are now supplied. The uniform propagation and noncharacteristic open-boundary inputs are also supplied. The limiting-boundary prerequisite supplies the arbitrary-open and missing-submanifold applications. Equation (4) is therefore proved with its stated arbitrary bounded coefficients. The full limiting tensor estimate (1) is also proved with the stated bounded coefficients and finite global dimension, without perfectness, constructibility or a noncharacteristic assumption. The directional-identity proof of involutivity applies at all points of microsupport without assuming its subanalyticity. The microlocal refinement proof gives compatible μ-stratifications over its explicitly stated subanalytic foundations. These are result-level providers; the remaining transitive foundational proofs are separate obligations.

These are application prerequisites. The present proof derives constructibility from them; it does not replace the boundary estimate by a finite-covector approximation or assume subanalyticity of arbitrary microsupport.

<span id="a-fixed-μ-stratification-criterion"></span>

## A fixed μ-stratification criterion {#fixed-stratification-criterion}

Let \(\mathcal S=(S_a)\) be a μ-stratification of \(X\), and write

\[
\Lambda_{\mathcal S}=\bigcup_a T_{S_a}^*X.
\tag{5}
\]

The union is closed, conic, subanalytic and isotropic by the stratification theorem.

**Fixed-stratification theorem.** The following are equivalent:

1. Every \(H^j(F)|_{S_a}\) is locally constant, for every degree and stratum.
2. \(\operatorname{SS}(F)\subset\Lambda_{\mathcal S}\).

**Proof of 2 ⇒ 1.** Fix \(x\in S_a\), and take an ambient open chart \(U\) where \(S=S_a\cap U\) is closed analytic. Put \(i:S\hookrightarrow U\). The extension of the restriction is

\[
i_*i^{-1}(F|_U)\simeq F|_U\otimes^L k_S.
\tag{6}
\]

The stalks of \(k_S\) are \(k\) or zero, so the displayed tensor has the ordinary restriction-extension meaning. Its microsupport is bounded by (1); the microsupport of \(k_S\) is the conormal \(T_S^*U\). Over \(S\),

\[
\operatorname{SS}(i_*i^{-1}F)\cap\pi^{-1}(S)
\subset
(\Lambda_{\mathcal S}|_U\widehat{+}T_S^*U)\cap\pi^{-1}(S)
\subset T_S^*U.
\tag{7}
\]

For the last inclusion, take a full limiting witness. Local finiteness reduces its first bases to a fixed stratum \(S_b\). If \(b\ne a\) and the output base is in \(S_a\), the frontier rule gives \(S_a\subset\overline{S_b}\setminus S_b\), and the ordered μ-condition applies. If \(b=a\), smooth conormal stability supplies the same conclusion. Explicitly, in coordinates straightening \(S\), both covectors annihilate the same tangent coordinate directions, so their finite sum does too. The operation's analytic coordinate invariance retains the position-covector product.

The extension in (6) is supported on \(S\), so (7) is its entire local microsupport bound. Formula (3) gives zero intrinsic microsupport for \(i^{-1}F\). The zero-section criterion proves local constancy of its cohomology. Inverse image is exact, so these are precisely \(H^j(F)|_S\). This proves the first implication at every point.

<span id="removing-a-stratum-from-the-closed-residual"></span>

## Removing a stratum from the closed residual {#closed-residual-induction}

**Proof of 1 ⇒ 2.** The problem is local. Choose a neighborhood meeting only finitely many strata, and restrict everything to it. Maintain a closed union \(Y\) of its strata such that the desired microsupport bound is already proved outside \(Y\). Initially \(Y\) is the whole neighborhood.

If \(Y\ne\varnothing\), choose a stratum \(S\) open in \(Y\). Such a stratum exists: a finite frontier order with strict dimension increase when passing to an approaching stratum has a maximal member. The frontier rule makes that member relatively open in the union. Put \(Y'=Y\setminus S\). This is closed, since \(S\) is open in the closed \(Y\). On the open manifold \(U=X\setminus Y'\), the stratum \(S\) is closed, and its complement is the already-good open part \(X\setminus Y\).

Let \(j:U\setminus S\hookrightarrow U\) and \(i:S\hookrightarrow U\). The actual localization triangle is

\[
j_!j^{-1}(F|_U)\longrightarrow F|_U
\longrightarrow i_*i^{-1}(F|_U)\xrightarrow{+1}.
\tag{8}
\]

By the local-constancy assumption and (2), the third term has microsupport in \(T_S^*U\). On \(U\setminus S\), the first term agrees with \(F\) and has the bound by induction. At its boundary \(S\), (4) gives

\[
\operatorname{SS}(j_!j^{-1}F)\cap\pi^{-1}(S)
\subset\operatorname{SS}(j^{-1}F)\widehat{+}T_S^*U
\subset T_S^*U.
\tag{9}
\]

The second inclusion uses the already-established conormal bound on the complement, monotonicity of the limiting operation, and the same finite-stratum witness and ordered μ-condition as in (7). Covectors of the complement can diverge; estimate (4) and the full μ-condition include them.

Both outside terms of (8) have the desired bound on \(U\). The triangle microsupport inequality gives it for \(F|_U\). We have removed one stratum from the residual. Repeat until the finite local residual is empty. This proves the bound on the chosen neighborhood; locality proves it globally. No globally finite stratification was assumed. \(\square\)

<span id="three-equivalent-geometric-descriptions"></span>

## Three equivalent geometric descriptions {#geometric-equivalence}

**Constructibility criterion.** For \(F\in D^b(k_X)\), the following are equivalent:

1. There is a common locally finite subanalytic cover \((E_i)\) of \(X\) on which every \(H^j(F)|_{E_i}\) is locally constant.
2. \(\operatorname{SS}(F)\) is contained in a closed conic subanalytic isotropic subset of \(T^*X\).
3. \(\operatorname{SS}(F)\) itself is a closed conic subanalytic Lagrangian subset.

**Proof.** For 1 ⇒ 2, refine the cover to a compatible μ-stratification. A restriction of a locally constant sheaf to a smaller subspace is locally constant, by restricting each trivializing neighborhood. The fixed-stratification theorem puts \(\operatorname{SS}(F)\) in the closed isotropic union (5).

For 2 ⇒ 1, the compatible conormal-cover theorem produces a μ-stratification whose total conormal contains the isotropic bound. Apply the fixed-stratification theorem again. This gives smooth strata as a permitted cover, although the original condition allowed nonsmooth and overlapping cover members.

For 2 ⇒ 3, use involutivity of the whole microsupport and the theorem recovering a subanalytic Lagrangian set from a relatively closed involutive subset of a subanalytic isotropic set. Here microsupport is closed in the given closed containing set; its initial subanalyticity is not assumed. The theorem includes empty microsupport. For 3 ⇒ 2, take the Lagrangian set itself as the isotropic bound. \(\square\)

The Lagrangian conclusion describes the directional support of a bounded sheaf complex. It does not determine the coefficient modules, their shifts, the gluing maps or the monodromy of local systems.

<span id="weak-constructibility-and-perfect-stalks"></span>

## Weak constructibility and perfect stalks {#perfect-stalk-criterion}

Call \(F\) **weakly R-constructible** when it satisfies the three geometric conditions above. Call it **R-constructible** when it is weakly R-constructible and every stalk complex \(F_x\) is perfect over \(k\). A perfect complex is quasi-isomorphic to a bounded complex of finitely generated projective \(k\)-modules.

When \(k\) is additionally Noetherian, for a bounded stalk complex \(C\),

\[
C\text{ perfect}\quad\Longleftrightarrow\quad
H^j(C)\text{ finitely generated for every }j.
\tag{10}
\]

**Proof.** A bounded complex of finite projectives has finitely generated kernels and cohomology because \(k\) is Noetherian. Conversely, a finitely generated module has a resolution by finitely generated free modules: each successive kernel is finitely generated by Noetherianity. Let the global dimension be \(g\). If \(g=0\), the original finitely generated module is already projective. If \(g>0\), take \(g\) successive finite-free surjections and denote the last kernel by \(K\). It is finitely generated by Noetherianity. For every module \(N\), the long exact Ext sequences give \(\operatorname{Ext}^1_k(K,N)\simeq\operatorname{Ext}^{g+1}_k(M,N)=0\), where \(M\) is the original module. A free surjection onto \(K\) therefore splits: its extension class vanishes. Thus \(K\) is projective, giving the required finite-projective resolution. Each \(H^j(C)\) is therefore perfect. There are finitely many nonzero cohomology degrees, and their finite truncation triangles build \(C\) from these perfect objects. Perfect complexes are closed under shifts and cones, so \(C\) is perfect. \(\square\)

A torsion module can be perfect without being projective as a degree-zero module. The definition concerns a finite projective complex representing it.

For clarity, the cone closure just used holds over an arbitrary ring. A bounded complex of projective modules has an exact Hom functor on acyclic complexes up to cohomology: first check a single projective module by exactness of Hom, then add its finitely many degrees through the truncation filtration. Thus derived morphisms out of it are represented by cochain maps. Represent two perfect objects by bounded finite-projective complexes and represent their morphism by such a map. The mapping cone has in each degree the direct sum of two finite-projective modules and remains bounded. It represents the derived cone and is perfect. Shifts preserve the same property. This supplies the coefficient argument used below without a Noetherian hypothesis.

<span id="the-constructible-categories"></span>

## The constructible categories {#constructible-categories}

The full subcategories \(D^b_{\mathrm{w\text{-}R\text{-}c}}(k_X)\) and \(D^b_{\mathrm{R\text{-}c}}(k_X)\) of \(D^b(k_X)\) are triangulated.

**Proof.** For finitely many weakly constructible objects, take a common locally finite subanalytic refinement of their covers and then a compatible μ-stratification. Local finiteness is preserved under finite intersections: near each point finitely many members of each original cover occur. The triangle estimate bounds a cone's microsupport by the union of the two original supports, hence by that same total conormal. The criterion proves weak constructibility of the cone; shifts are immediate. For R-constructibility, additionally take stalks of the triangle and use closure of perfect complexes under finite shifts and cones. This last statement does not require the ring to be Noetherian. \(\square\)

For ordinary sheaves, let \(\mathrm{w\text{-}R\text{-}Cons}(k_X)\) denote the full category of weakly R-constructible sheaves. It is an abelian subcategory and is closed under extensions.

**Proof.** Given a morphism of two such sheaves, use one common compatible stratification. On a sufficiently small connected stratum chart both sheaves are constant. A morphism between constant sheaves there is a fixed module homomorphism: each constant section is sent to a locally constant section, which is constant on the connected chart. Thus its kernel, image and cokernel are constant sheaves with the corresponding modules. Restriction to the stratum is exact, so these are the restrictions of the ambient kernel, image and cokernel. The geometric criterion gives their weak constructibility.

For a short exact sequence with weakly constructible ends, its derived triangle and their common total conormal bound give that same bound for the middle sheaf. The fixed criterion gives its locally constant stratum restrictions. This extension argument also applies to arbitrary stalk modules. It does not require a simultaneous choice of lifts for an infinite generating set. \(\square\)

If \(k\) is Noetherian, the same assertions hold for \(\mathrm{R\text{-}Cons}(k_X)\). The weak assertion is already proved, and (10) reduces the extra condition to finite generation of stalk modules. Noetherian kernels and images, and finite cokernels and extensions, retain it.

Finally, if \(Z\subset X\) is locally closed and subanalytic, its constant sheaf extended by zero \(k_Z\) is R-constructible. A compatible μ-stratification makes each stratum lie wholly inside or wholly outside \(Z\). Its restriction is then constant with value \(k\) or zero. The stalks are perfect, proving the assertion by the criterion.

## Exercises with complete solutions

### Infinite coefficients do not change the geometric condition

*Difficulty: Introductory.*

Let \(k\) be a field and \(V=\bigoplus_{m\ge1}k\). On \(X=\mathbb R\), compare the constant sheaves \(k_X\) and \(V_X\). Determine their microsupports and whether they are weakly R-constructible or R-constructible.

**Solution.** Both are locally constant and nonzero at every point. The zero-section criterion and zero-covector support detection give microsupport equal to the entire zero section in each case. Both are weakly R-constructible using the one-stratum partition \(X\).

The stalk \(k\) is finite projective, so \(k_X\) is R-constructible. The degree-zero stalk \(V\) has infinite-dimensional cohomology. A perfect complex over a field has finite-dimensional cohomology, so \(V\) is not perfect and \(V_X\) is not R-constructible. The identical geometric supports do not impose finite coefficients.

### A torsion stalk can be perfect

*Difficulty: Intermediate.*

On any analytic \(X\), use \(k=\mathbb Z\) and the morphism \(m:\mathbb Z_X\to\mathbb Z_X\), where \(m\ge2\). Compute its kernel, image and cokernel, and exhibit a perfect representative of each cokernel stalk. Is the degree-zero cokernel module projective?

**Solution.** The kernel is zero, the image is \(m\mathbb Z_X\simeq\mathbb Z_X\), and the cokernel is the constant sheaf \((\mathbb Z/m)_X\). All are locally constant. Each cokernel stalk is represented by the two-term complex

\[
\bigl[\mathbb Z\xrightarrow{m}\mathbb Z\bigr],
\qquad\text{in degrees }-1,0.
\tag{11}
\]

Its only cohomology is \(\mathbb Z/m\) in degree zero, so it is a finite free representative and the stalk is perfect. The degree-zero module is not projective: a projective \(\mathbb Z\)-module is torsion-free as a direct summand of a free module, while \(\mathbb Z/m\) has torsion. R-constructibility uses the complex notion of perfection, so the cokernel is R-constructible.

### Equal microsupport with different monodromy

*Difficulty: Advanced.*

On \(S^1\), over a field of characteristic different from two, compare the rank-one constant local system with the rank-one local system whose monodromy is \(-1\). Determine their microsupports and cohomology.

**Solution.** Both are nonzero locally constant sheaves with one-dimensional perfect stalks. They are R-constructible and have microsupport equal to the zero section over all of \(S^1\).

For a rank-one local system with monodromy \(T\), cover the circle by two contractible arcs whose intersection has two contractible components. Mayer–Vietoris gives two copies of \(k\) for arc sections and two copies for intersection sections. After choosing a trivialization and recording the change by \(T\) on one intersection component, the differential is \((u,v)\mapsto(u-v,u-Tv)\). An invertible row and column reduction leaves an identity summand and the map \(1-T:k\to k\). Therefore

\[
H^0(S^1;L)=\ker(1-T),\qquad
H^1(S^1;L)=\operatorname{coker}(1-T).
\tag{12}
\]

For \(T=1\), both are \(k\). For \(T=-1\), the map is multiplication by two, an isomorphism, and both vanish. Their microsupports agree, although their global cohomology and monodromy differ.

### A fixed stratification bound can be strictly larger

*Difficulty: Intermediate.*

Use the nine-stratum quadrant/half-axis/origin μ-stratification of \(\mathbb R^2\). Let \(H=\{y=0\}\) and \(F=k_H\). Check local constancy on the strata and compute the origin fibre of \(\operatorname{SS}(F)\). Compare it with the total stratum conormal fibre.

**Solution.** The restriction is constant \(k\) on the two horizontal half-axes and the origin, and zero on every other stratum. All stalks are \(k\) or zero, so \(F\) is R-constructible.

The closed smooth embedding of the horizontal line and (2) give \(\operatorname{SS}(F)=T_H^*\mathbb R^2\). At the origin this is only \(\mathbb R\,dy\). The total stratum conormal there is the whole two-dimensional cotangent fibre because the origin is a point stratum. Thus the criterion gives a strict inclusion at that fibre. It asserts containment in the total conormal, rather than equality with every stratum conormal.

### An ordinary partition is insufficient

*Difficulty: Advanced.*

In \(\mathbb R^3\), let \(Z=\{x^3=y^3z\}\), \(N=\{x=y=0\}\), \(M=Z\setminus N\), and \(O=\mathbb R^3\setminus Z\). These form the ordinary stratification studied in the μ-construction lesson. For \(F=k_Z\), show its restrictions to all three strata are locally constant, but its microsupport is not contained in their total conormal union.

**Solution.** On \(M\) and \(N\), the restriction is the constant sheaf \(k\); on \(O\) it is zero. Thus the three restrictions are locally constant. The closed subanalytic \(Z\) makes \(F\) R-constructible through a suitable μ-refinement, but the present partition has the bad μ-point at the origin.

Near a point \((0,s,0)\) with \(s\ne0\), \(Z\) is a smooth hypersurface with parametrization \((s,t)\mapsto(st,s,t^3)\). At \(t=0\), its tangent vectors are \((0,1,0)\) and \((s,0,0)\), so \(dz\) is conormal. The local smooth closed-embedding formula puts \((0,s,0;dz)\) in \(\operatorname{SS}(k_Z)\). Letting \(s\to0\) and using closedness of microsupport gives

\[
(0,0,0;dz)\in\operatorname{SS}(k_Z).
\tag{13}
\]

At the origin the only conormal in the ordinary union comes from \(N\), and consists of \(a\,dx+b\,dy\). The covector \(dz\) is absent. This proves the failed containment. Splitting the origin into its own point stratum restores the μ-condition and supplies its full cotangent fibre. The μ-hypothesis of the fixed-stratification theorem is needed.

### Perfect local stalks do not force finite global sections

*Difficulty: Intermediate.*

Over a field, let \(F=\bigoplus_{m\in\mathbb Z}k_{\{m\}}\) on \(\mathbb R\), using the locally finite family of integer supports. Determine its stalks, microsupport, ordinary global sections and compactly supported global sections. Is it R-constructible?

**Solution.** The stalk is \(k\) at an integer and zero elsewhere. The integer-point/open-interval partition is a locally finite μ-stratification, and the restrictions are constant with perfect stalks. Hence \(F\) is R-constructible. Its microsupport is the locally finite union \(\bigcup_m T_m^*\mathbb R\), by the closed-embedding equality and locality.

Equivalently, \(F\) is the direct image of the constant-value sheaf on the closed discrete set \(\mathbb Z\). Sections can choose a value independently at every integer, while compact support permits only finitely many integers. Thus

\[
\Gamma(\mathbb R;F)=\prod_{m\in\mathbb Z}k,
\qquad
\Gamma_c(\mathbb R;F)=\bigoplus_{m\in\mathbb Z}k.
\tag{14}
\]

Both are infinite-dimensional, although every stalk is perfect. The sheaf's support is noncompact. Local constructibility does not supply finite global cohomology without the compactness or proper-support hypotheses of the later finiteness theorems.

### Two restriction maps determine the cotangent rays {#interval-ray-model}

*Difficulty: Intermediate.*

Let \(I=(-1,1)\), with distinguished point zero. Given three modules and two maps

\[
 L\xleftarrow{a}A\xrightarrow{b}R,
 \tag{G1}
\]

construct the sheaf whose nearby left and right values are \(L\) and \(R\), and whose germ at zero is \(A\). Compute its two nonzero cotangent rays over zero. Apply the calculation to the constant sheaf, the constant sheaves on the closed and open right half intervals extended by zero, and the sheaf supported at zero. These are bounded degree-zero examples; arbitrary modules are allowed. When the three modules are perfect as degree-zero complexes, the resulting sheaf is R-constructible.

**Solution.** A section on an open set is a locally constant left-valued function and a locally constant right-valued function, together with an element \(u\in A\) when the set contains zero. On the two components next to zero the functions must have values \(a(u)\) and \(b(u)\). The usual gluing of locally constant functions, and agreement of \(u\) on overlaps containing zero, prove the sheaf axiom. Shrinking connected neighborhoods shows that the three stalk values and restriction maps are exactly (G1). The three-piece decomposition is a μ-stratification, so the fixed-stratification theorem gives weak constructibility. Perfectness of the three stalk values supplies its coefficient condition.

Apply support localization to a small neighborhood of zero with the closed support \(\{x\geq0\}\). The complementary open set is the left half interval. Its constant-sheaf cohomology is \(L\) in degree zero, by the constant-interval calculation. The stalk at zero of the derived open direct image is the filtered limit of these half-interval sections; shrinking maps are the identity. Thus the stalk localization triangle is the fibre triangle for \(a:A\to L\). The other support uses \(b:A\to R\):

\[
 \bigl(R\mathcal\Gamma_{\{x\geq0\}}F\bigr)_0
       \simeq [A\xrightarrow{a}L],\qquad
 \bigl(R\mathcal\Gamma_{\{x\leq0\}}F\bigr)_0
       \simeq [A\xrightarrow{b}R],
 \quad\text{in degrees }0,1.
 \tag{G2}
\]

This uses the actual restriction maps, rather than only the isomorphism classes of the modules. In particular, the first test has kernel and cokernel of \(a\) in degrees zero and one, respectively. For a nonzero covector \(\lambda\,dx\) at zero, every sufficiently nearby differentiable test function with derivative of the same sign is strictly monotone after shrinking. Its superlevel germ is the right or left half interval accordingly. Tests based away from zero vanish for such derivatives because the sheaf is locally constant there. This supplies the uniform neighborhood required by the definition of microsupport. Conversely the linear tests at zero realize each nonvanishing complex in (G2). Consequently

\[
 \begin{aligned}
 (0;\lambda\,dx)\in\operatorname{SS}(F),\ \lambda>0
     &\quad\Longleftrightarrow\quad a\text{ is not an isomorphism},\\
 (0;\lambda\,dx)\in\operatorname{SS}(F),\ \lambda<0
     &\quad\Longleftrightarrow\quad b\text{ is not an isomorphism}.
 \end{aligned}
 \tag{G3}
\]

Away from zero there are only zero covectors over the nonzero constant stalks. The zero covectors over the closure of those bases, and over zero when \(A\ne0\), are present by closed-support detection. This specifies the entire microsupport, including the case \(A=L=R=0\).

Take a nonzero coefficient ring and write \(k_+\) for the constant sheaf on \([0,1)\) extended by zero in \(I\), \(k_+^{\mathrm{open}}\) for that on \((0,1)\), and \(k_0\) for the point sheaf. The diagrams give the following exact four models:

\[
\begin{array}{c|c|c|c}
 F & (L\leftarrow A\to R)&\lambda>0&\lambda<0\\ \hline
 k_I &(k\xleftarrow{1}k\xrightarrow{1}k)&\text{absent}&\text{absent}\\
 k_+ &(0\leftarrow k\xrightarrow{1}k)&\text{present}&\text{absent}\\
 k_+^{\mathrm{open}} &(0\leftarrow0\to k)&\text{absent}&\text{present}\\
 k_0 &(0\leftarrow k\to0)&\text{present}&\text{present}
\end{array}
\tag{G4}
\]

For the open right half interval the negative test is \([0\to k]\), with its nonzero cohomology in degree one. Its stalk at zero is zero although its microsupport contains the zero covector there as a limit. For the closed right half interval the positive test is \([k\to0]\), in degree zero. This verifies both signs and shows why the geometric bound for a fixed stratification does not determine the sheaf or its gluing maps.

![Four exact microsupport models on an interval.](assets/constructibility-rays.svg)

*Figure.* Horizontal coordinate \(x\) is the base and vertical coordinate \(\xi\) represents \(\xi\,dx\). Each drawn segment continues as indicated by its arrows; only its intersection with a finite coordinate window is shown. The origin is included in all four microsupports. The blue horizontal parts are zero covectors, and the orange vertical parts are the nonzero rays supplied by the respective non-isomorphisms in (G3). Formulas (G1)–(G4) prove the models, including the shift for the open half interval. No claim of equality with the full conormal of an arbitrary stratification is made.

## From geometric criteria to derived comparisons

We have proved constructibility through microsupport and separated its coefficient requirement. The next step compares bounded complexes of constructible sheaves with the constructible part of the ambient derived category. That comparison requires simultaneous triangulations of actual complexes and their quasi-isomorphism roofs, followed by the full functorial and finiteness arguments.

## Human sources and exact proof scope {#sources-and-proof-scope}

Hohl and Schapira, [*Unusual functorialities for weakly constructible sheaves*](https://arxiv.org/abs/2303.11189v2), arXiv version 2 of 7 January 2025, §2 and the opening of §4, distinguish arbitrary weak coefficients from perfect stalks and recall the two microsupport descriptions. The source version was checked through the authors' native TeX. Those opening statements cite prior work rather than give the geometric equivalence proof. The argument here supplies both fixed-stratification directions, the closed-residual induction, the isotropic-to-Lagrangian step, the ring hypotheses, the category arguments and complete worked examples. Later functoriality results of that paper require their own hypotheses and proofs; none is inferred here merely from its bibliography.

Schapira, [*A short review on microlocal sheaf theory*](https://webusers.imj-prg.fr/~pierre.schapira/LectNotes/MuShv.pdf), 19 January 2016, §2.2–2.3, gives the local-support definition, Example 2.5's constant and half-space models, and the closed-embedding case of Theorem 2.9. It explicitly omits the involutivity proof. The present lesson uses the exact linked programme proof instead. The interval calculation (G1)–(G4) derives each sign and degree from the actual two restriction maps; the human reference is credited for the classical models. No source prose, figure or exercise sequence is reproduced.

Transitive derived and elementary topological foundations, and the deep subanalytic closure, regularity, dimension, component, curve-selection and uniformization inputs to the geometric providers, remain separately recorded work. This lesson does not certify full prerequisite closure or full-course source and structure clearance.

## Readable source and dependency account

The freely readable comparison is Kashiwara and Schapira, *Microlocal study of sheaves*, Definition 8.2.5, Theorem 8.2.6 and Lemma 8.2.7, printed pp. 145–148 (PDF pp. 148–151). The exact fixed-stratification criterion in this lesson is proved using the displayed estimates and the ordered microlocal condition; it is not obtained by discarding that condition from an ordinary stratification.

The 1985 theorem separates weak constructibility from perfect coefficients and proves the reverse geometric implication with noncharacteristic balls. Here the closed-residual induction supplies the fixed microlocal stratification argument. Its full limiting estimates, zero-section criterion, involutivity and geometric refinement remain separate providers. No finite-generation or Noetherian assumption is inserted into the weak theorem; perfect stalks are an additional condition. A readable statement is not a proof of every transitive foundational input.

Checked comparison: [Kashiwara–Schapira, *Microlocal study of sheaves*, Astérisque 128 (1985)](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf). This comparison complements the Hohl–Schapira and Schapira review accounts above. Original programme exposition remains CC0; the human works retain their own rights.
