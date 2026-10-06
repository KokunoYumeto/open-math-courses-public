# Compact Morse models and full cotangent projections

A compactly supported sheaf with nonzero ordinary cohomology has a microsupport point over every covector direction. A single isolated linear test can certify that its cohomology is nonzero: when its localized coefficient is an unshifted rank-\(m\) skyscraper, the whole global cohomology complex is \(k^m\). This proves the assigned cotangent-projection theorem over every field.

*Written by GPT-6.1 Sol (OpenAI), Ultra, 2 October 2026. Author self-check recorded; not independently reviewed. New original text is public domain (CC0).*

Learn first Pure and simple sheaves from directional tests for the closed support test and its compatibility with localized representatives. Pure test degrees and strong Morse inequalities states and proves the exact arbitrary-field filtration used here, separately from its characteristic-cycle formulas. Its written SH-02 provider is Local jumps and finite Morse data and A finite filtration by local tests. Their proper-support, endpoint, localization and connecting-map proofs retain their exact earlier foundational obligations. The argument below supplies the localized-model and projection steps in full.

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

The integer \(m\) initially denotes the dimension of a finite coefficient space, so \(m\ge0\). The equality of sets in (1) says that \(p\) actually belongs to \(\operatorname{SS}(F)\).

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

If \(p\notin\operatorname{SS}(G)\), the defining microsupport vanishing test with
\(d\ell_{x_0}=\xi_0\) makes (3) zero. Hence this exact functor kills
\(\mathcal N_p\), inverts every denominator whose cone belongs to that kernel, and factors through (2). Applying it to the given localized isomorphism computes

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

The second property follows from compact closed support, even though the linear function on \(V\) is usually nonproper. Its restriction to the coefficient support is proper. The only local test required by the finite Morse theorem is (4), which is bounded and finite-dimensional.

Recall the actual arbitrary-field filtration. If a smooth function has finitely many microsupport graph intersections, the closed sublevel support condition and finite local tests give triangles

\[
 B_0=0,\qquad B_r\simeq R\Gamma(V;F),\qquad
 L_\nu\longrightarrow B_\nu\longrightarrow B_{\nu-1}
       \xrightarrow{+1},\qquad
 L_\nu\simeq\bigoplus_{\ell(x_i)=c_\nu}M_{p_i}(F).
 \qquad\text{(6)}
\]

The maps from an upper sublevel to a lower one are ordinary restrictions. Proper direct image to the real line and its supported localization identify \(L_\nu\) with the indicated closed local tests. On the critical fibre those tests vanish away from the finitely many microsupport intersections; proper base change then gives their actual finite direct sum. The one-sided finite-band comparisons identify levels between jumps and retain the endpoints. These are the exact maps of the preceding written filtration.

In our case there is one critical value \(c\) and one summand. Formula (6) is the triangle \(M_p(F)\to B_1\to0\xrightarrow{+1}\). It yields

\[
 \boxed{R\Gamma(V;F)\simeq k^m.}
 \qquad\text{(7)}
\]

For completeness, a level below the minimum of \(\ell\) on the compact support has zero sublevel complex. A level above its maximum contains all coefficient support and has global complex \(R\Gamma(V;F)\). The finite-band theorem transports these endpoints to the one-jump triangle. No escape of support at infinity or limiting extra term is present.

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

Every closed support sublevel is compact. The zero-intersection case of the same finite-band theorem therefore identifies all sublevel section complexes. A level below the compact support starts at zero; a level above it is the global complex. Hence

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

The local test is finite and bounded because \(P\) is perfect, so (6) applies. Its one triangle gives the middle isomorphism, and the missing-direction lemma gives the last conclusion. A nonzero \(P\) can have Euler number zero; the argument keeps its whole complex.

If \(V\) has dimension zero, its dual is one point. The hypotheses give a nonzero coefficient at that point, and (7)–(12) have the same interpretation. If \(\xi_0=0\) in positive dimension, (1) forces the entire closed support to be \(\{x_0\}\); point-support adjunction gives the same global complex directly.

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

**Solution.** The global complex is \(P=k\oplus k[1]\), with one-dimensional cohomology in degrees zero and minus one. Its Euler number is \(1-1=0\), but \(P\ne0\). Its microsupport is the cotangent fibre over zero, so every directional intersection is unique. Formula (12), or directly the missing-direction lemma, gives full projection. This coefficient is not an unshifted rank-\(m\) model; it illustrates the stronger complex statement without changing (1). In characteristic zero its characteristic cycle cancels by the proved triangle and shift additivity, although its microsupport is nonempty.

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

The full cotangent projection of a compactly supported real constructible sheaf over a field is a classical consequence of the index theory of M. Kashiwara, [*Index theorem for constructible sheaves*](https://www.numdam.org/item/AST_1985__130__193_0/), Astérisque 130 (1985). The proof here uses the arbitrary-field finite Morse filtration and retains the whole local coefficient complex. It also explains the forced positive multiplicity, the zero-covector case, support properness and the distinction between integer rank and scalar trace. Its graded extension and counterexamples are proved explicitly.
