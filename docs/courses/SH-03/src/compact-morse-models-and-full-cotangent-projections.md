# Compact Morse models and full cotangent projections

A compactly supported sheaf with nonzero ordinary cohomology has a microsupport point over every covector direction. A single isolated linear test can certify that its cohomology is nonzero: when its localized coefficient is an unshifted rank-\(m\) skyscraper, the whole global cohomology complex is \(k^m\). This proves the assigned cotangent-projection theorem over every field.

*Original programme exposition, examples and solutions are dedicated to the public domain under CC0.*

The [neighborhood-uniform support test](../../sheaf-proof-readings/src/SH02/microsupport-tests.md#sh02-mst-test--the-local-experiment) and thick point localization specify the local category and its denominators. The [closed-test discussion](../../microlocal-composition-and-pure-sheaves/src/pure-and-simple-sheaves-from-directional-tests.md#the-test-function-includes-a-covector-and-a-transversality-condition) gives the same direct cone-vanishing argument for localized representatives. We use that argument below; it requires neither a smooth Lagrangian model nor transverse intersection.

[Pure test degrees and strong Morse inequalities](pure-test-degrees-and-strong-morse-inequalities.md#the-morse-filtration-retains-the-attaching-maps) supplies the arbitrary-field filtration, separately from its characteristic-zero cycle formulas. Its current SH-02 providers are [Local jumps and finite Morse data](../../sheaf-proof-readings/src/SH02/microsupport-operations.md#sh02-mo-field-boundary--local-jumps-and-finite-morse-data) and [A finite filtration by local tests](../../sheaf-proof-readings/src/SH02/microsupport-operations.md#sh02-mo-morse-inequalities--a-finite-filtration-by-local-tests). We spell out the restriction maps, their supported fibres and both endpoints. The sublevel deformation proof applies to arbitrary bounded sheaves; compact-neighborhood continuity and the open-union comparison provide its endpoint maps. Thus the projection argument retains whole complexes over every field.

## The source hypotheses include a present microsupport point

Let \(V\) be a finite-dimensional real vector space, \(k\) any field, and
\(F\in D^b_{\mathbb R\text{-c}}(k_V)\) have compact closed support. Let
\(q:T^*V=V\times V^*\to V^*\) be the second projection. Assume

\[
 p=(x_0;\xi_0),\qquad
 q^{-1}(\xi_0)\cap\operatorname{SS}(F)=\{p\},
 \qquad
 F\simeq k_{\{x_0\}}^{\,m}\text{ in }D^b(V;p).
 \qquad\text{(1)}
\]

Here support always means the closed support, including a boundary point at which the stalk itself can be zero. The integer \(m\) initially denotes the dimension of a finite coefficient space, so \(m\ge0\). The equality of sets in (1) says that \(p\) actually belongs to \(\operatorname{SS}(F)\).

Recall the localization:

\[
 \mathcal N_p=\{G\in D^b(k_V):p\notin\operatorname{SS}(G)\},
 \qquad
 D^b(V;p)=D^b(k_V)/\mathcal N_p.
 \qquad\text{(2)}
\]

The kernel \(\mathcal N_p\) is thick. Shifts preserve microsupport; the microsupport triangle inclusion preserves avoidance of \(p\); and direct summands preserve the defining local-test vanishing. The neighborhoods witnessing avoidance can be intersected for a finite triangle.

An object becomes zero in this quotient exactly when it belongs to \(\mathcal N_p\). Here is the kernel check in its fraction description. If its localized identity is zero, choose a denominator \(u:H\to G\), with \(\operatorname{Cone}(u)\in\mathcal N_p\), on which that identity becomes zero. Then \(u=0\), and its cone is \(G\oplus H[1]\). Thickness puts \(G\) itself in \(\mathcal N_p\). The converse follows by the quotient definition.

Consequently \(m=0\) in (1) would force \(p\notin\operatorname{SS}(F)\). This contradicts the same equation's singleton intersection. Thus \(m>0\). A zero sheaf has an empty intersection in (1), and supplies no counterexample to these hypotheses.

## A linear closed test descends to the localized category

Put \(\ell(x)=\langle x,\xi_0\rangle\) and \(c=\ell(x_0)\). The exact local test functor is

\[
 M_p(G)=\bigl(R\Gamma_{\{\ell\ge c\}}G\bigr)_{x_0}.
 \qquad\text{(3)}
\]

For \(j:\{\ell<c\}\hookrightarrow V\), the actual localization triangle at \(x_0\) is \(M_p(G)\to G_{x_0}\to(Rj_*j^{-1}G)_{x_0}\xrightarrow{+1}\); its second arrow is restriction toward lower height. This specifies (3) as a triangulated functor, including its maps. Finite cohomological dimension on \(V\) keeps the values bounded. If \(p\notin\operatorname{SS}(G)\), the defining neighborhood-uniform vanishing criterion applies in particular to \(\ell\), whose differential at \(x_0\) is \(\xi_0\). Hence \(M_p(G)=0\). Applying this functor to the cone triangle of any denominator makes that denominator invertible, so the universal property of (2) gives a functor on the whole quotient, including fraction representatives. Applying it to the specified localized isomorphism computes

\[
 M_p(F)\simeq M_p(k_{\{x_0\}}^{\,m})\simeq k^m.
 \qquad\text{(4)}
\]

The last comparison has no shift. The skyscraper is already supported in the closed set \(\{\ell\ge c\}\), since its supporting point lies on its boundary. Sections with that support leave the skyscraper unchanged, and its stalk is \(k^m\).

For \(\xi_0=0\), \(\ell\) is constant and (3) is the ordinary stalk functor. An object in \(\mathcal N_{(x_0,0)}\) vanishes in a neighborhood of \(x_0\), by the zero-section support identity. The same factorization and calculation still apply.

## One jump determines the entire global complex

The graph of \(d\ell\) is the constant-covector section \(V\times\{\xi_0\}\). Thus (1) gives

\[
 \{(x;d\ell_x)\}\cap\operatorname{SS}(F)=\{p\},
 \qquad
 \operatorname{supp}(F)\cap\{\ell\le t\}\text{ is compact for all }t.
 \qquad\text{(5)}
\]

Write \(D=\operatorname{supp}(F)\). The second property follows from compact closed support, even though the linear function on \(V\) is usually nonproper. For any compact interval \(I\), \(D\cap\ell^{-1}(I)\) is closed in compact \(D\), so \(\ell|_D\) is proper. Proper-on-support direct image, rather than properness of the ambient linear map, is therefore available. The local test (4) is bounded and finite-dimensional.

Recall the actual arbitrary-field filtration. More generally, for a smooth height \(\varphi\) and an arbitrary \(F\in D^b(k_V)\), assume that each closed support sublevel is compact, that the graph of \(d\varphi\) meets \(\operatorname{SS}(F)\) at finitely many points \(p_i=(x_i;d\varphi_{x_i})\), and that the corresponding local tests \(M_{p_i}(F)=(R\Gamma_{\{\varphi\geq\varphi(x_i)\}}F)_{x_i}\) have bounded finite-dimensional cohomology. These hypotheses require no constructibility or transversality. Write \(c_1<\cdots<c_r\) for the distinct critical values. In the notation \(\varphi=\ell\) of our application, the filtration gives triangles

\[
 B_0=0,\qquad B_r\simeq R\Gamma(V;F),\qquad
 L_\nu\longrightarrow B_\nu\longrightarrow B_{\nu-1}
       \xrightarrow{+1},\qquad
 L_\nu\simeq\bigoplus_{\ell(x_i)=c_\nu}M_{p_i}(F).
 \qquad\text{(6)}
\]

Here is a construction that retains the arrows. Suppose first that \(r>0\), and put \(E_t=R\Gamma(\{\varphi<t\};F)\). The support is bounded below: choose one nonempty compact sublevel, take its minimum, and observe that every point of the support outside that sublevel has larger height. Choose \(t_0\) below this minimum, \(t_\nu\in(c_\nu,c_{\nu+1})\) for \(0<\nu<r\), and \(t_r>c_r\). Set \(B_\nu=E_{t_\nu}\). The maps \(B_\nu\to B_{\nu-1}\) are ordinary restrictions. Their fibres are initially the supported section complexes in the closed part \(\{t_{\nu-1}\leq\varphi<t_\nu\}\) of the open set \(\{\varphi<t_\nu\}\).

On an interval of heights containing no graph intersection, the defining microsupport tests vanish on every level. To check the sublevel deformation hypotheses directly, take \(U_t=\{\varphi<t\}\). The closure of \(U_t\setminus U_s\), intersected with the support, is a closed subset of the compact band \(\{s\leq\varphi\leq t\}\cap D\). The limiting front \(\bigcap_{t>s}\overline{U_t\setminus U_s}\) lies in \(\{\varphi=s\}\). For a later time it lies inside \(U_t\), where the supported test vanishes automatically; at the equal time \(t=s\), vanishing is precisely the positive closed test. The deformation theorem on an open parameter interval consequently gives the actual restriction isomorphisms between the \(E_t\), including the limit toward the upper open endpoint. No negative-covector condition or duality of the coefficient complex is being substituted.

At a critical value \(c=c_\nu\), put \(Y=\{\varphi\leq c\}\), \(U=\{\varphi<c\}\), and \(A_c=R\Gamma(Y;F|_Y)\). The compact set \(K=D\cap Y\) has the relative neighborhoods \(D\cap\{\varphi<c+\epsilon\}\) as a cofinal system when \(\epsilon\downarrow0\). Indeed all these sets lie in one fixed compact support sublevel; points outside a prescribed neighborhood with heights decreasing to \(c\) would have a limit in \(K\), a contradiction. Compact-neighborhood continuity therefore identifies the cohomology of \(A_c\) with the filtered colimit of the upper open-sublevel cohomologies. The restriction maps in that system are isomorphisms, because no further critical value intervenes. The natural restriction \(B_\nu\to A_c\) is thus a quasi-isomorphism. The open-sublevel deformation comparison also identifies \(R\Gamma(U;F)\to B_{\nu-1}\) by its actual restriction map.

Now restrict the support-localization triangle for \(\{\varphi\geq c\}\) to \(Y\). If \(j:U\hookrightarrow V\) and \(j':U\hookrightarrow Y\), the natural comparison \((Rj_*F|_U)|_Y\to Rj'_*F|_U\) is an isomorphism: a neighborhood in \(Y\) is the intersection of a neighborhood in \(V\) with \(Y\), and both intersect \(U\) in the same open set. The derived direct-image stalk calculations therefore agree. Taking sections on \(Y\) gives the triangle
\(R\Gamma(Y;(R\Gamma_{\{\varphi\geq c\}}F)|_Y)\to A_c\to R\Gamma(U;F)\xrightarrow{+1}\).
The sheaf complex \((R\Gamma_{\{\varphi\geq c\}}F)|_Y\) has zero stalk below \(c\), and on the fibre at \(c\) its stalk vanishes except at the finitely many points \(x_i\) with \(\varphi(x_i)=c\). For the closed inclusion \(i:S=\{x_i:\varphi(x_i)=c\}\hookrightarrow Y\), its restriction unit to \(i_*i^{-1}\) of it is an isomorphism on every stalk. Sections on the finite discrete set \(S\) are an exact finite direct sum. This identifies the first term with \(L_\nu=\bigoplus_{\varphi(x_i)=c}M_{p_i}(F)\), and gives (6) with its connecting map.

The proper-image description is the same construction. For \(H=R\varphi_*F\), localization identifies \(R\Gamma_{[c,\infty)}H\) with \(R\varphi_*R\Gamma_{\{\varphi\geq c\}}F\). The latter coefficient is still supported inside \(D\), on which \(\varphi\) is proper. Proper base change at \(c\) gives sections of its restriction to the critical fibre, and the finite-support argument just given yields the same \(L_\nu\). This explains the local direct sum without assuming that a nonproper ordinary image can be evaluated on a closed fibre.

Finally, \(B_0=0\). Above \(c_r\), all open-sublevel restrictions are isomorphisms. An increasing sequence of such levels exhausts \(V\). Its inverse cohomology system is constant in every degree, and its first derived limit vanishes: the difference map on products is surjective by recursive lifting along the isomorphisms. The open-union comparison identifies \(R\Gamma(V;F)\to B_r\) as a quasi-isomorphism. When there are no intersections, start below the support and the same argument gives zero at every stage and globally. For finitely many finite local tests, induction in the displayed triangles makes every \(B_\nu\) perfect. This proves the full proper-below filtration and retains every attaching map.

In our case there is one critical value \(c\) and one summand. Formula (6) is the triangle \(M_p(F)\to B_1\to0\xrightarrow{+1}\). It yields

\[
 \boxed{R\Gamma(V;F)\simeq k^m.}
 \qquad\text{(7)}
\]

In the present compact-support application there is an even shorter endpoint check. A level below the minimum of \(\ell|_D\) has zero sublevel complex, and a level above its maximum contains all of \(D\). The latter has the same global complex as \(V\), by the closed-support adjunction \(F\simeq i_*i^{-1}F\) for \(i:D\hookrightarrow V\). Thus the endpoints can be chosen outside the entire support, and the single supported-localization triangle already proves (7). The exhaustion argument above is only needed for the more general proper-below filtration. No contribution arrives from infinity.

In particular

\[
 H^j(V;F)=0\ (j\ne0),\qquad
 \dim_k H^0(V;F)=m>0,\qquad \chi(V;F)=m\in\mathbb Z.
 \qquad\text{(8)}
\]

The isomorphism uses the specified localized model and filtration comparisons. The proof does not require a globally defined isomorphism \(F\simeq k_{\{x_0\}}^{\,m}\).

## A missing direction forces global cohomology to vanish

We now prove a useful statement independent of (1).

**Lemma.** If \(G\in D^b(k_V)\) has compact closed support and a covector
\(\eta\in V^*\) does not belong to \(q(\operatorname{SS}(G))\), then
\(R\Gamma(V;G)=0\).

**Proof.** Take \(h(x)=\langle x,\eta\rangle\). Its positive graph has no microsupport intersection:

\[
 \{(x;dh_x)\}\cap\operatorname{SS}(G)
       =q^{-1}(\eta)\cap\operatorname{SS}(G)=\varnothing.
 \qquad\text{(9)}
\]

Let \(D_G\) be the compact closed support. If it is nonempty, choose \(a<\min h(D_G)\) and \(b>\max h(D_G)\). The missing direction in (9) makes every positive local support test for \(h\) vanish. For \(U_t=\{h<t\}\), the supported closures of increments lie in the compact \(D_G\); the limiting front lies on \(h=s\), so the equal-time test is exactly the one that vanishes, and all later-time tests vanish inside \(U_t\). The sublevel deformation theorem therefore identifies the actual restriction from \(\{h<b\}\) to \(\{h<a\}\). The source computes \(R\Gamma(V;G)\) because it contains the closed support, and the target is zero. This argument uses bounded complexes of arbitrary sheaves: it makes no constructibility, finite-stalk, finite-local-test or characteristic-zero assumption. Hence

\[
 R\Gamma(V;G)=0.
 \qquad\text{(10)}
\]

This also holds for empty support. For \(\eta=0\), the missing zero-section intersection itself forces empty support, by
\(\operatorname{SS}(G)\cap0_V=0_{\operatorname{supp}(G)}\). Thus all directions are included in the lemma. \(\square\)

**Projection theorem.** Under (1),

\[
 \boxed{q(\operatorname{SS}(F))=V^*.}
 \qquad\text{(11)}
\]

**Proof.** Formula (7) is a nonzero complex because \(m>0\). If a direction were missing from the projected microsupport, the lemma would make that same complex zero. This contradiction proves (11). \(\square\)

More generally the lemma proves that any compactly supported bounded sheaf complex with nonzero ordinary cohomology has full cotangent projection. The particular single-test hypothesis in the exercise is a way to prove that nonvanishing.

## The coefficient complex can be retained in full

The same proof permits a nonzero perfect coefficient complex \(P\) in place of the unshifted \(k^m\). If the unique graph intersection is \(p\) and the localized model is \(k_{\{x_0\}}\otimes_kP\), then

\[
 M_p(F)\simeq P,\qquad R\Gamma(V;F)\simeq P,\qquad
 q(\operatorname{SS}(F))=V^*\quad(P\ne0).
 \qquad\text{(12)}
\]

The point-extension functor and the support test commute with tensoring by a perfect coefficient complex: represent \(P\) by a bounded finite complex of finite-dimensional vector spaces and apply the functors term by term. The skyscraper test is therefore \(P\) with its entire differential. Alternatively it follows directly because this point-supported complex is already supported in the closed test set. The localized isomorphism is carried to that same \(P\) by the exact quotient functor. Its local cohomology is bounded and finite-dimensional, so the one triangle of (6) gives the middle isomorphism in (12), and the missing-direction lemma gives the last conclusion. A nonzero \(P\) can have Euler number zero; no Euler-number nonvanishing is used.

If \(V\) has dimension zero, its dual is one point. The hypotheses give a nonzero coefficient at that point, and (7)–(12) have the same interpretation. If \(\xi_0=0\) in positive dimension, the zero-section support identity forces the entire closed support to be \(\{x_0\}\). For its inclusion \(i\), the ordinary restriction unit \(F\to i_*i^{-1}F=i_*F_{x_0}\) is an isomorphism on every stalk. It gives \(R\Gamma(V;F)\simeq F_{x_0}\). The constant closed test identifies this stalk with the specified coefficient complex, giving the same conclusion directly.

## Exercises with complete solutions

### Rank equal to the characteristic
*Difficulty: Introductory.*

Let \(k\) have characteristic \(p>0\), and take the skyscraper \(F=k_{\{0\}}^{\,p}\) on \(V\). Compare its integer Euler number with the scalar trace of its identity. Determine its cotangent projection.

**Solution.** Ordinary cohomology is \(k^p\) in degree zero. Its integer Euler number is \(p>0\), while its scalar identity trace is \(p\,1_k=0\). The skyscraper microsupport is the full cotangent fibre over zero, so its projection is all of \(V^*\). Every fibre over a direction contains exactly that base point and the localized rank is \(p\). Thus it meets (1). The scalar zero does not make the coefficient complex vanish; (7) and the missing-direction lemma work directly over \(k\).

### A shifted point model
*Difficulty: Intermediate.*

Retain compact support and the unique intersection, but replace the local model by \(k_{\{x_0\}}^{\,m}[s]\), with \(m>0\). Determine global cohomology, Euler number and cotangent projection.

**Solution.** Exactness makes the local closed test \(k^m[s]\). The one-jump triangle gives global complex \(k^m[s]\). Its only nonzero cohomology is in degree \(-s\), of dimension \(m\), and its integer Euler number is \((-1)^s m\). That complex is nonzero for every integer \(s\), so the projection is still full. This is the shifted extension (12); the assigned exercise's unshifted model is \(s=0\).

### A zero Euler number with a full projection
*Difficulty: Intermediate.*

Take \(F=k_{\{0\}}\oplus k_{\{0\}}[1]\) on \(V\). Compute global cohomology and its Euler number. Explain which projection theorem applies.

**Solution.** The global complex is \(P=k\oplus k[1]\), with one-dimensional cohomology in degrees zero and minus one. Its Euler number is \(1-1=0\), but \(P\ne0\). Its microsupport is the cotangent fibre over zero, so every directional intersection is unique. Formula (12), or directly the missing-direction lemma, gives full projection. This coefficient is not an unshifted rank-\(m\) model; it illustrates the stronger complex statement without changing (1). In characteristic zero its characteristic cycle cancels by the proved [triangle and shift additivity](constructible-functions-and-integral-lagrangian-cycles.md#the-three-groups-and-their-coefficients), although its microsupport is nonempty.

### A noncompact ray satisfies the local model but misses directions
*Difficulty: Advanced.*

On \(V=\mathbb R\), let \(F=k_{[0,\infty)}\). Check the localized model at \(p=(0;1)\) and the unique intersection over \(1\). Compute its projected microsupport and identify the failed hypothesis.

**Solution.** At an interior positive point the sheaf is locally constant; at a negative point it vanishes. At zero a positive closed test has supported stalk \(k\). For a negative derivative the local closed test is the endpoint-supported relative complex of a half-interval. Restriction \(k\to k\) from the half-interval to its puncture is the identity, so that test vanishes. Monotonicity gives these same local tests for all nearby functions with the respective derivative sign. Thus
\(\operatorname{SS}(F)=0_{[0,\infty)}\cup\{(0;\xi):\xi\ge0\}\), and its projection is \([0,\infty)\).

The triangle \(k_{(0,\infty)}\to k_{[0,\infty)}\to k_{\{0\}}\xrightarrow{+1}\) identifies \(F\) with the skyscraper at \(p\): the open ray has only the opposite, negative nonzero covectors at zero, so the cone avoids \(p\). Over \(1\) the intersection is exactly \(\{p\}\). However the closed support is noncompact. Its negative-height sublevels are noncompact, and its projection omits all negative directions. This gives a counterexample when compactness is removed.

### Two compact jumps can cancel
*Difficulty: Advanced.*

On \(\mathbb R\) take \(F=k_{[0,1)}\) and use the height \(h(x)=x\). Find its positive critical tests and compute their attaching map. Explain why it does not satisfy the singleton hypothesis.

**Solution.** At zero the local model is the closed positive ray and its test is \(J_0=k\). At one the local model is the open negative ray. Its supported test is the fibre of \(0\to k\), namely \(J_1=k[-1]\). There are no nonzero microsupport covectors at interior points. The positive direction consequently has two microsupport points, one at each endpoint.

Between the endpoints the ordinary sublevel complex is \(B_1=k\). The full ordinary complex is zero: the localization triangle
\(k_{[0,1)}\to k_{[0,1]}\to k_{\{1\}}\xrightarrow{+1}\) gives the identity map \(k\to k\) on global sections. The second Morse triangle is therefore
\(k[-1]\to0\to k\xrightarrow{\delta}k\). Exactness makes \(\delta\) an isomorphism. With the identification of \(J_1\) induced by its local boundary map, \(\delta\) is the identity: the sublevel constant section restricts to the same constant section on the left punctured neighborhood. The two local degrees cancel through this actual attaching map. The support is compact and the model at the first point has rank one, but the intersection over the positive direction is not a singleton. It violates that precise hypothesis in (1).

### The zero covector and dimension zero
*Difficulty: Intermediate.*

Assume (1) with \(\xi_0=0\). Determine the support of \(F\), and verify the projection conclusion also when \(\dim V=0\).

**Solution.** The zero-section identity identifies \(q^{-1}(0)\cap\operatorname{SS}(F)\) with the zero covectors over its closed support. The singleton condition forces that support to be \(\{x_0\}\). Closed point-support adjunction gives \(F=i_*F_{x_0}\). The constant closed test is the stalk, so the localized model identifies it with \(k^m\), where \(m>0\). Therefore \(F\simeq k_{\{x_0\}}^{\,m}\) globally, and its microsupport projects to the entire dual space. When \(V\) is a point, its cotangent fibre and dual are both a point, and the same nonzero coefficient proves the conclusion. No nonzero-covector exclusion is needed.

### Changing the affine coordinates
*Difficulty: Introductory.*

In \(V=\mathbb R^2\), let \(x_0=(2,-1)\), \(\xi_0=(3,4)\), and set
\(w=A(x-x_0)\) with \(A=\begin{pmatrix}1&1\\0&2\end{pmatrix}\).
Compute the transformed covector and explain why the theorem is unchanged.

**Solution.** Covectors transform by \(A^{-t}\), so
\(\eta=A^{-t}\xi_0=(3,\tfrac12)\). The calibrated height is
\(\langle x-x_0,\xi_0\rangle=\langle w,\eta\rangle\).
The coordinate change preserves compact support, takes the skyscraper to the skyscraper at zero, and carries the specified directional microsupport fibre to the corresponding fibre over \(\eta\). It preserves the closed support test and its exact cohomology complex. The dual linear map is invertible, so it takes a full projected microsupport to a full one. This argument uses the local coefficient complex and no coordinate-orientation scalar.

### An actual global cone gives a second proof
*Difficulty: Advanced.*

Suppose, in addition to (1), that a global triangle
\(G\to F\to k_{\{x_0\}}^{\,m}\xrightarrow{+1}\) has
\(p\notin\operatorname{SS}(G)\). Prove \(R\Gamma(V;F)\simeq k^m\) directly from the missing-direction lemma.

**Solution.** The support triangle puts the closed support of \(G\) inside the union of the compact support of \(F\) and \(\{x_0\}\), so it is compact. The microsupport triangle inclusion gives
\(\operatorname{SS}(G)\subset\operatorname{SS}(F)\cup T^*_{\{x_0\}}V\).
Intersecting with \(q^{-1}(\xi_0)\) leaves at most \(p\); the extra assumption removes that point too. The missing-direction lemma now gives \(R\Gamma(V;G)=0\). Global sections of the displayed triangle identify \(R\Gamma(V;F)\) with the skyscraper coefficient \(k^m\). This proof uses the additional actual global triangle. The general localized isomorphism in (1) can involve fraction representatives; the local-test factorization in (3)–(4) handles those as well.

## References

M. Kashiwara, [Index theorem for constructible sheaves](https://www.numdam.org/item/AST_1985__130__193_0/), Astérisque 130 (1985), Theorem 4.2, p. 199, relates the sheaf Euler characteristic to an intersection with a differential graph when the closed sublevels on the coefficient support and the graph–microsupport intersection are compact. Its introduction, p. 194, explains the change of sublevel cohomology through local Morse tests. The proof above uses the linked arbitrary-field Morse filtration to retain the entire local coefficient complex, rather than only its Euler characteristic. This is what also handles positive characteristic and a nonzero coefficient complex of Euler number zero.
