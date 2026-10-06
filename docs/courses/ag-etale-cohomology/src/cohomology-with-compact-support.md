# Cohomology with compact support

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI, GPT-6.1 Sol (OpenAI). Links and citations revised by Claude Opus 5.5 (Anthropic), October 2026. Original text released under CC0. The constructibility reduction and finiteness proof in Section 12 are by GPT-6 Astra (OpenAI), October 2026.*

A section on an open curve can remain nonzero arbitrarily close to a missing point. Compact support imposes a different condition: its nonzero locus must be proper over the base. To retain that condition in higher cohomology, extend the coefficient complex by zero into a compactification and then use proper direct image. The main work is showing that every compactification produces the same functor and the same comparison maps.

We use [The proper base change theorem](the-proper-base-change-theorem.md), [Torsion sheaves on curves](torsion-sheaves-on-curves.md), and [Constructible sheaves and extension by zero](constructible-sheaves-and-extension-by-zero.md). Proper and projective morphisms provide the geometric vocabulary. Sections 4–5 supply the dimension and unbounded-complex arguments needed in this lesson; they are not deferred to a later cohomological-dimension theorem.

## 1. Coefficients and the statements

All sites are small étale sites. A coefficient ring \(\Lambda\) is commutative with identity. Write \(D(X,\Lambda)\) for the derived category of sheaves of \(\Lambda\)-modules on \(X\). The subcategory \(D^+_{\mathrm{tors}}(X,\Lambda)\) consists of bounded-below complexes whose cohomology sheaves are torsion as abelian sheaves. Different sections can have different annihilators. A *torsion ring* satisfies \(n\Lambda=0\) for some positive integer \(n\): the additive order of its identity supplies such an integer.

For a separated morphism of finite type \(f:X\to Y\) between quasi-compact, quasi-separated schemes, we construct

\[
Rf_!:D^+_{\mathrm{tors}}(X,\Lambda)
\longrightarrow D^+_{\mathrm{tors}}(Y,\Lambda).
\tag{1.1}
\]

When \(\Lambda\) is torsion, the construction works on the entire, possibly unbounded, category \(D(X,\Lambda)\). Every subsequent assertion about \(Rf_!\) uses one of these two domains. Exact inverse image is denoted \(f^{-1}\), and tensors in the derived category are derived tensors.

**Theorem 1.1.** The functor \(Rf_!\) is canonically independent of compactification. There are canonical, associative isomorphisms

\[
Rg_!Rf_!\simeq R(gf)_!,
\qquad g^{-1}Rf_!\simeq Rf'_!a^{-1}
\tag{1.2}
\]

for composable separated finite-type morphisms and for a cartesian square

\[
\begin{matrix}
X'=X\times_Y Y'&\xrightarrow{a}&X\\
f'\downarrow&&\downarrow f\\
Y'&\xrightarrow{g}&Y.
\end{matrix}
\tag{1.3}
\]

Base change is arbitrary; it need not be flat. For a torsion ring and arbitrary complexes \(E\in D(X,\Lambda)\), \(M\in D(Y,\Lambda)\),

\[
Rf_!E\otimes^L_\Lambda M
\simeq Rf_!(E\otimes^L_\Lambda f^{-1}M).
\tag{1.4}
\]

For an open immersion with quasi-compact domain \(j:U\to X\) and its closed complement \(i:Z\to X\), these functors give the excision triangle. If every geometric fibre of \(f\) has dimension at most \(d\), then

\[
R^qf_!\mathcal F=0\quad(q>2d)
\tag{1.5}
\]

for every torsion sheaf \(\mathcal F\). No constructibility assumption enters this bound. Sections 6–12 prove these assertions and the curve finiteness theorem.

## 2. Properly supported sections

Let \(f:X\to Y\) be separated and locally of finite type. For an étale \(V\to Y\), write \(X_V=X\times_YV\). A section \(s\in\mathcal F(X_V)\) has a closed support: its complement is the union of open loci where its germ is zero. Properness of this closed subset over \(V\) means that its reduced induced closed subscheme is proper over \(V\). Define

\[
f_!\mathcal F(V)=
\{s\in\mathcal F(X_V):\operatorname{Supp}(s)\to V
\text{ is proper}\}.
\tag{2.1}
\]

**Lemma 2.1.** Formula (2.1) defines an additive subsheaf of \(f_*\mathcal F\). If \(f\) is proper, \(f_!=f_*\). If \(j:X\hookrightarrow\overline X\) is an open immersion over \(Y\), and \(p:\overline X\to Y\) is proper, then

\[
f_!\mathcal F=p_*j_!\mathcal F.
\tag{2.2}
\]

**Proof.** The support of a sum is contained in the union of the two supports. Finite unions and closed subsets of properly supported closed subsets are properly supported. Pulling back a section pulls back its support, and properness survives base change. To check gluing, first glue the sections in \(f_*\mathcal F\). Their supports on an étale covering are the pullbacks of the support of the glued section. Properness descends through that covering: finite type, separatedness and universal closedness can each be checked faithfully flat locally on the target. Thus the glued section satisfies (2.1).

When \(f\) is proper every closed support is proper. For (2.2), a section of \(j_!\mathcal F\) on \(\overline X_V\) has closed support contained in \(X_V\), because the boundary stalks are zero. That closed support is proper over \(V\). Conversely a support proper over \(V\) is closed in \(\overline X_V\): its map there is proper, using separatedness of \(\overline X_V/V\). Glue the given section on \(X_V\) to zero off its support. This produces a section of \(j_!\mathcal F\), uniquely, and the two operations are inverse. □

**Lemma 2.2.** Suppose \(f\) is separated and locally quasi-finite. For a geometric point \(\bar y\),

\[
(f_!\mathcal F)_{\bar y}
=\bigoplus_{\bar x\in X_{\bar y}}\mathcal F_{\bar x}.
\tag{2.3}
\]

Consequently \(f_!\) is exact and commutes with direct sums and arbitrary base change. For separated étale \(f\), this is the exact extension-by-zero functor of lesson 11.

**Proof.** First suppose \(X/Y\) is finite type and \(Y\) affine. Compactify it. Equation (2.2), degree-zero proper base change, and the base change of open extension by zero identify the left side with

\[
H^0(\overline X_{\bar y},j_{\bar y,!}\mathcal F|_{X_{\bar y}})
=H^0_c(X_{\bar y},\mathcal F|_{X_{\bar y}}).
\tag{2.4}
\]

The locally quasi-finite geometric fibre is a disjoint union of zero-dimensional local schemes. Their étale topoi are point topoi: nilpotents do not change that topos, and the residue fields are algebraically closed. A proper closed support in this discrete fibre consists of finitely many points. Formula (2.4) is therefore the sum in (2.3).

For a general locally quasi-finite \(f\), work near \(\bar y\) in an affine base. A properly supported section has quasi-compact support, hence is contained in a quasi-compact open of \(X\). Such an open is separated and finite type over the affine base. Extension by zero from these opens identifies \(f_!\) with their filtered union: supports proper over the base stay closed in the larger separated scheme. The fibre sum is the corresponding union of finite sums. This proves (2.3) without a global quasi-compactness hypothesis on \(X\).

Exactness and sums now follow from exactness of stalks and of direct sums of modules. For base change, pull back a section with its support. This defines the canonical map \(g^{-1}f_!\mathcal F\to f'_!a^{-1}\mathcal F\). At \(\bar y'\) both sums are indexed by the identical fibre \(X_{\bar y'}\), and each summand is identified by inverse image of germs. The map is the identity on these sums, so it is an isomorphism. For étale \(f\), lesson 11's extension by zero has the same canonical summand maps: a section on a local branch extends by zero to that branch. Étale locally the finite support lies in finitely many such branches, which proves the identification with (2.1). □

A finite formal-support description sometimes extends this construction to nonseparated locally quasi-finite maps. One sheafifies sums \((T,s)\), with \(T\) locally closed and finite over the target and \(s\) supported on \(T\), subject to addition and enlargement-of-support relations. For separated maps each such \(T\) is closed in \(X_V\), so this gives exactly (2.1). Our finite-type derived construction throughout this lesson requires separatedness.

## 3. Compactifications and refinements

**Nagata compactification, stated.** A separated finite-type morphism to a quasi-compact, quasi-separated scheme factors

\[
X\xrightarrow{j}\overline X\xrightarrow{p}Y,
\qquad j\text{ open},\quad p\text{ proper}.
\tag{3.1}
\]

This is Nagata's compactification theorem. Its complete proof in this generality is [AI Integrated Stacks Project, Tag 0F41](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/flat.html#flat-theorem-nagata): it reduces to a Noetherian base by limits, compactifies the members of a finite affine cover inside projective spaces, and glues these compactifications with Lemma 0F40 and the preceding results of the same section. Finite presentation of \(f\) is not required. Taking the schematic closure of \(X\) in \(\overline X\) gives a compactification with \(X\) dense and schematically dense; call such a compactification dense. The open is quasi-compact, so its schematic closure exists and restricts to \(X\) on that open.

A morphism of compactifications is a \(Y\)-map \(h:\overline X_1\to\overline X_2\) restricting to the identity on \(X\). It is proper: its graph is closed in \(\overline X_1\times_Y\overline X_2\), and projection from that product to \(\overline X_2\) is proper.

**Lemma 3.1.** The category of compactifications is cofiltered. Dense compactifications suffice to refine any finite collection of choices. For a refinement with dense source,

\[
h^{-1}(X)=X.
\tag{3.2}
\]

**Proof.** Nonemptiness is Nagata. For two compactifications take the schematic closure of the diagonal copy of \(X\) in \(\overline X_1\times_Y\overline X_2\). It is proper over \(Y\). Above the open \(X\) in the first factor, that copy is the graph of \(X\to\overline X_2\), which is closed because \(\overline X_2/Y\) is separated. The closure thus restricts to that graph, and the copy of \(X\) is open in the closure. Both projections give refinements.

Two parallel morphisms are equalized by their closed equalizer in the source; the equalizer is proper and contains the same open \(X\). Taking its schematic closure if needed makes a dense refining object. These are exactly the three cofilteredness requirements.

For (3.2), inside \(h^{-1}(X)\) the given copy of \(X\) is an open section of a proper morphism to \(X\). That section is also closed. Its complement is therefore open in \(h^{-1}(X)\), hence open in \(\overline X_1\), and disjoint from the dense \(X\). It is empty. An open subscheme is determined by its underlying open subset, which gives (3.2). Finally two maps out of a schematically dense compactification that agree on \(X\) agree everywhere: their closed equalizer has ideal restricting to zero on \(X\), and schematic density makes that ideal zero. □

Nagata's theorem is used only for existence. The refinement and equalizer arguments, which provide the canonical nature of our cohomological construction, have been proved here.

## 4. The proper dimension bound

We need a bound before passing to unbounded complexes. The geometric foundations used in this section are these: normalization of a reduced finite-type scheme over a field is finite; an integral normal scheme is regular at codimension-one points; a rational map from such a scheme to a proper curve extends at those points; and a dominant morphism from an integral \(n\)-dimensional scheme to a curve has fibres of dimension at most \(n-1\). In the last assertion, on an affine piece the special fibre is cut out by a nonzero parameter, while the generic fibre has dimension \(n-1\). These are geometric facts about finite-type schemes, without a cohomological premise.

**Theorem 4.1.** If \(p:T\to S\) is proper and every geometric fibre has dimension at most \(d\), then

\[
R^qp_*\mathcal F=0\quad(q>2d)
\tag{4.1}
\]

for every torsion abelian sheaf \(\mathcal F\).

**Proof.** Induct on \(d\), proving the assertion for all proper morphisms at once. If \(d=0\), the morphism is proper and quasi-finite, hence finite; lesson 7 proves exactness of its direct image. For \(d=1\), proper base change reduces the assertion to the proper curve theorem of lesson 12 over an algebraically closed field.

For the induction step, proper base change again reduces to \(H^q(T,\mathcal F)=0\) for \(T\) proper over an algebraically closed field, \(\dim T\leq d\). Replace \(T\) by its reduction using topological invariance. Let \(\nu:T^\nu\to T\) be its finite normalization, a disjoint union of normal integral components. The adjunction map

\[
0\longrightarrow\mathcal F\longrightarrow
\nu_*\nu^{-1}\mathcal F\longrightarrow i_*\mathcal G
\longrightarrow0
\tag{4.2}
\]

is injective since every geometric point has a lift to the surjective \(\nu\). It is an isomorphism on a dense open containing the generic points, so the cokernel is supported on a proper closed subscheme \(Z\) of dimension at most \(d-1\). Closed pushforward identifies it with \(i_*\mathcal G\). By induction \(H^q(Z,\mathcal G)=0\) for \(q>2d-2\). Since finite pushforward is exact, the long exact sequence reduces the desired vanishing to the normal integral components of \(T^\nu\). Components of dimension below \(d\) are already covered by induction.

Now let \(T\) be normal integral of dimension \(d>1\). Choose a nonconstant rational function. Its graph closure supplies

\[
T\xleftarrow{b}T'\xrightarrow{r}\mathbf P^1.
\tag{4.3}
\]

Both arrows are proper. The first is an isomorphism where the rational map is defined. The complementary closed subset \(Z\subset T\) has codimension at least two: at a codimension-one point, the local ring is a discrete valuation ring and the rational map extends to the proper \(\mathbf P^1\) by its valuative criterion. Every fibre of \(b\) is a closed subscheme of \(\mathbf P^1\), hence has dimension at most one. Thus \(Rb_*b^{-1}\mathcal F\) has cohomology only in degrees \(0,1,2\). For the triangle

\[
\mathcal F\longrightarrow Rb_*b^{-1}\mathcal F
\longrightarrow Q\longrightarrow\mathcal F[1],
\tag{4.4}
\]

surjectivity of \(b\) makes the degree-zero adjunction injective. Therefore \(Q\) has cohomology only in degrees \(0,1,2\), supported on \(Z\); those sheaves are torsion. The induction hypothesis and the finite hypercohomology spectral sequence give

\[
H^m(T,Q)=0\quad(m>2\dim Z+2),
\qquad 2\dim Z+2\leq2d-2.
\tag{4.5}
\]

Consequently it suffices to bound \(H^q(T',b^{-1}\mathcal F)\). The graph closure is integral and \(r\) is dominant, so its fibres have dimension at most \(d-1\). Induction gives \(R^jr_*b^{-1}\mathcal F=0\) for \(j>2d-2\). Each of the remaining sheaves is torsion, and the proper curve theorem gives zero cohomology on \(\mathbf P^1\) above degree two. The Leray spectral sequence

\[
H^i(\mathbf P^1,R^jr_*b^{-1}\mathcal F)
\Longrightarrow H^{i+j}(T',b^{-1}\mathcal F)
\tag{4.6}
\]

has no entries above total degree \(2d\). This proves the absolute vanishing, and hence the relative vanishing by the geometric-stalk formula. □

For a proper finite-type morphism over a quasi-compact base a finite fibre-dimension bound exists. On each of finitely many affine charts of source and target, a finite list of algebra generators bounds the dimension of every fibre by the length of that list. This gives a uniform integer, even when the base is not Noetherian.

## 5. Finite amplitude and unbounded proper base change

We use the foundational existence of K-injective resolutions in a Grothendieck category of sheaves: a complex admits a quasi-isomorphism into a K-injective complex whose terms are injective. Derived direct image is computed on such a resolution. The following argument explains why bounded cohomological dimension allows *any* termwise acyclic resolution, including unbounded ones.

**Lemma 5.1.** Let \(F\) be left exact, with enough injectives and \(R^qF=0\) for \(q>N\). A complex of \(F\)-acyclic objects computes \(RF\). Moreover

\[
RF(D^{\geq a})\subset D^{\geq a},
\qquad RF(D^{\leq b})\subset D^{\leq b+N}.
\tag{5.1}
\]

Thus \(H^i(RFE)\) is determined by the finite cohomology window \([i-N,i]\) of \(E\).

**Proof.** Consider an exact complex \(L^\bullet\) of acyclic objects and put \(Z^t=\ker d^t\). From

\[
0\to Z^t\to L^t\to Z^{t+1}\to0
\tag{5.2}
\]

we obtain \(R^qF(Z^{t+1})=R^{q+1}F(Z^t)\) for \(q\geq1\). Iterating to the left \(N+1\) times makes every positive derived functor of each cycle zero. Applying \(F\) to (5.2) is consequently exact, so \(F(L^\bullet)\) is exact. The cone of a quasi-isomorphism between complexes of acyclic objects has acyclic terms and is exact. Applying \(F\) to that cone proves that the quasi-isomorphism remains one. Comparing with a termwise injective K-injective resolution proves the computation claim.

The lower bound in (5.1) follows by choosing a bounded-below injective resolution for an object of \(D^{\geq a}\). For the upper bound, use a termwise injective resolution \(I^\bullet\) of \(E\in D^{\leq b}\). It is exact in degrees above \(b\). For \(i>b+N\), the cohomology of \(F(I^\bullet)\) in degree \(i\) is

\[
\operatorname{coker}(F(I^{i-1})\to F(Z^i))
=R^1F(Z^{i-1})
=R^{N+1}F(Z^{i-N-1})=0.
\tag{5.3}
\]

The short exact cycle sequences used here are valid because their right-hand cycle degrees exceed \(b\); the final sequence uses \(I^b\to Z^{b+1}\) only when \(i=b+N+1\). If \(N=0\), \(F\) is exact and the same conclusion is immediate. Apply (5.1) to the cones of \(\tau_{\leq i}E\to E\) and \(E\to\tau_{\geq i-N}E\). They contribute no cohomology that can change \(H^i\), giving the finite-window assertion. □

**Proposition 5.2.** For a proper morphism, proper base change holds on unbounded complexes over a torsion ring. On a quasi-compact base \(Rp_*\) has finite amplitude, and commutes with arbitrary direct sums.

**Proof.** Work locally on the base to bound fibre dimensions by \(d\). Theorem 4.1 bounds sheaf cohomological dimension by \(N=2d\). Sheaf-of-module cohomology agrees with the underlying abelian-sheaf cohomology, as proved in lesson 12; hence the same bound applies to \(\Lambda\)-modules. Choose a K-injective, termwise injective complex \(I^\bullet\) representing \(E\).

In the base change square, the bounded-below theorem applied to each single sheaf \(I^t\) gives

\[
R^qp'_*a^{-1}I^t=0\quad(q>0),
\qquad g^{-1}p_*I^t=p'_*a^{-1}I^t.
\tag{5.4}
\]

Lemma 5.1 lets the termwise \(p'_*\)-acyclic complex \(a^{-1}I^\bullet\) compute \(Rp'_*a^{-1}E\). Equation (5.4) identifies its image with \(g^{-1}p_*I^\bullet\), proving unbounded base change with the usual canonical map. This argument uses the common annihilator supplied by the torsion ring.

For sums choose such \(I_\alpha^\bullet\) for each input. Quasi-compact, quasi-separated higher direct images commute with filtered colimits of sheaves, by lesson 7. They therefore commute with sums, a sum being the filtered colimit of its finite subsums. Every \(\bigoplus_\alpha I_\alpha^t\) is \(p_*\)-acyclic. Lemma 5.1 computes the image termwise, and \(p_*\bigoplus I_\alpha^\bullet=\bigoplus p_*I_\alpha^\bullet\). This proves the direct-sum assertion. Finite amplitude is (5.1). □

Over an arbitrary ring, bounded-below complexes with torsion cohomology remain covered by lesson 13. Their direct images have torsion cohomology: on a geometric proper fibre, write a torsion sheaf as the filtered union of its annihilator subsheaves; each cohomology group is then a filtered colimit of torsion groups. A bounded-below hypercohomology filtration has finitely many contributing terms in each total degree. The same argument covers bounded-below families with a common lower bound. We do not infer an unbounded arbitrary-ring statement from that filtration.

## 6. The proper–open exchange and its coherence

**Lemma 6.1.** Suppose

\[
\begin{matrix}
U&\xrightarrow{j}&T\\
p'\downarrow&&\downarrow p\\
V&\xrightarrow{i}&S
\end{matrix}
\tag{6.1}
\]

commutes, with horizontal arrows open and vertical arrows proper. The square need not be cartesian. There is a canonical isomorphism

\[
\epsilon:i_!Rp'_*E\xrightarrow{\sim}Rp_*j_!E.
\tag{6.2}
\]

It is compatible with stacking squares vertically or horizontally and with arbitrary base change.

**Proof.** Put \(T_V=T\times_SV\). The induced map \(k:U\to T_V\) is open and proper: its graph argument uses properness of \(U/V\) and separatedness of \(T_V/V\). Thus \(k\) is an open-and-closed immersion, for which \(k_!=k_*\) is exact. Restricting the right side of (6.2) to \(V\) identifies it with

\[
R(p|_{T_V})_*k_!E=Rp'_*E.
\tag{6.3}
\]

The inverse of this identification defines (6.2) by the derived adjunction \(i_!\dashv i^{-1}\). That adjunction holds since both functors are exact; \(i^{-1}\) also takes K-injective complexes to K-injectives because its exact left adjoint is \(i_!\).

On \(V\), the map is the isomorphism (6.3). On the closed complement of \(V\), proper base change says that \(Rp_*j_!E\) is the proper direct image of the zero complex: the support open \(U\) has no points there. The left side is also zero. Geometric stalks on these two loci detect a quasi-isomorphism, proving (6.2) on both coefficient domains.

Here are the map compatibilities. In a vertically stacked diagram, proper direct image composition identifies the restriction of both the composed exchanges and the outer exchange with the same proper direct image of the same clopen-supported complex. Both identifications are formed from the composition of direct-image adjunction units. The identity
\(\eta_{pq}=p_*\eta_q\circ\eta_p\), with the indicated inverse images inserted, gives equality. Since the source is extension by zero from the bottom open, its adjunction determines the whole map from this restriction. Horizontally stacking opens uses \((ii')_!=i_!i'_!\). Restrict to the smallest open: the two maps again give the identical clopen pushforward identification (6.3). The same adjunction proves equality globally. Exchanges on disjoint positions of a diagram commute by naturality of transformations, so these two pasting rules also apply to a grid of squares.

After base change, open extension by zero, proper direct image comparison, and the clopen identification (6.3) are all natural. Restrict the two candidate maps to the pulled-back open. There they are the composition-compatible proper base change maps of lesson 13 or Proposition 5.2. Their equality, followed by the open adjunction, proves base-change compatibility. Thus the isomorphism and all its pasting properties concern actual canonical maps. □

## 7. Definition and independence of compactification

Choose (3.1) and define

\[
Rf_!E=Rp_*j_!E.
\tag{7.1}
\]

The exact functor \(j_!\) acts termwise on complexes and preserves torsion cohomology. Proper direct image preserves the domains specified in Section 1. For a sheaf, its degree-zero image is (2.2); this justifies the notation \(f_!\). The symbol \(Rf_!\) in (7.1) denotes the compactification construction. It is not a claim that taking a right derived functor of the ordinary properly supported-section functor produces (7.1).

**Theorem 7.1.** Definition (7.1) is independent of compactification up to a canonical isomorphism. These isomorphisms satisfy the identity and cocycle conditions.

**Proof.** A refinement \(h:\overline X_1\to\overline X_2\) gives a square of the form (6.1), with top open \(j_1:X\to\overline X_1\), bottom open \(j_2:X\to\overline X_2\), and left proper map \(\mathrm{id}_X\). Lemma 6.1 gives

\[
j_{2,!}\xrightarrow{\sim}Rh_*j_{1,!}.
\tag{7.2}
\]

Applying \(Rp_{2,*}\), and using proper composition, gives a comparison from the functor for compactification 2 to the functor for compactification 1. For two successive refinements, vertical pasting in Lemma 6.1 says precisely that the composite comparison equals the comparison for their composite; for an identity it is the identity.

For arbitrary choices choose a common refinement \(C\) and compare both functors to the functor for \(C\). If another common refinement is chosen, cofilteredness gives a further refinement of both. Composition compatibility shows that both comparisons become equal there, hence were equal already, since refinement comparisons are isomorphisms. Parallel refining maps are equalized by a further refinement; their functor maps likewise become equal and hence agree. This proves independence of all choices. Taking a common refinement of three choices proves the cocycle condition by cancellation of their maps to that common object. □

If \(f\) is proper, choose \(j=\mathrm{id}_X\); thus \(Rf_!=Rf_*\). If \(f\) is quasi-finite, separated and finite type, Zariski's main theorem gives \(X\hookrightarrow\overline X\) with \(\overline X/Y\) finite. Then

\[
Rf_!=\overline f_*j_!=f_!
\tag{7.3}
\]

as exact functors. In particular \(Rj_!=j_!\) for a quasi-compact open immersion, and the same agreement holds for separated finite-type étale morphisms.

## 8. Composition, including associativity

**Theorem 8.1.** For \(X\xrightarrow{f}Y\xrightarrow{g}Z\) separated and finite type between quasi-compact, quasi-separated schemes,

\[
c_{g,f}:Rg_!Rf_!\xrightarrow{\sim}R(gf)_!
\tag{8.1}
\]

is canonical and associative.

**Proof.** Compactify \(g\) as \(Y\xrightarrow{i}D\xrightarrow{q}Z\). Compactify the separated finite-type composite \(if\) as \(X\hookrightarrow C\xrightarrow{p}D\). Put \(U=p^{-1}(Y)\), write \(j:X\hookrightarrow U\), \(k:U\hookrightarrow C\), and \(h:U\to Y\). The map \(h\) is proper. These choices compute

\[
Rf_!=Rh_*j_!,\quad Rg_!=Rq_*i_!,
\quad R(gf)_!=R(qp)_*k_!j_!.
\tag{8.2}
\]

The cartesian proper–open square \((U,C;Y,D)\) supplies

\[
Rq_*i_!Rh_*j_!
\xrightarrow{Rq_*\epsilon j_!}
Rq_*Rp_*k_!j_!
=R(qp)_*k_!j_!,
\tag{8.3}
\]

which is (8.1) for this system.

We verify choice independence. Given two systems \((C_t,D_t)\), choose a dense common refinement \(D_3\to D_1,D_2\). In
\(C_1\times_ZC_2\times_ZD_3\), impose the closed equations equating the two maps to each \(D_t\). They are closed because \(D_t/Z\) is separated. The resulting scheme is proper over \(D_3\), contains the diagonal copy of \(X\), and its schematic closure of that copy gives \(C_3\). The copy is open: over \(X\subset C_1\) it is the graph of the other two maps, closed by separatedness. Thus \((C_3,D_3)\) refines both systems, compatibly at every vertex. The opens \(U_t\) also pull back to \(U_3\), because a dense refinement has inverse image \(Y\) equal to \(Y\), by (3.2).

Compare (8.3) under one such refinement. There are exchanges for refinement of \(C\), for refinement of \(D\), and for the middle proper–open square. Expanding each comparison into these exchanges yields two routes through the same grid. Vertical pasting identifies the exchanges along a composite proper map, horizontal pasting identifies those along composite opens, and the exchanges in separate positions commute by naturality. Both routes are therefore the exchange for the outer rectangle followed by the same proper composition. This proves the comparison square commutes. The common refinement now gives choice independence by Theorem 7.1.

For three maps \(f,g,h\), compactify successively the last target, the preceding source over that compactification, and then the first source over the next compactification. Taking inverse images of the successive opens gives one compatible triangular array of opens and proper maps. Both parenthesizations of \(Rh_!Rg_!Rf_!\) move the same two middle opens past the same proper maps. A pasting across adjacent squares combines to the outer exchange by Lemma 6.1; exchanges in separated positions commute by naturality. Hence both routes give the same map to \(R(hgf)_!\). Independence of the chosen array has just been proved. Identity maps use identity compactifications and identity exchanges. This proves the associative, unital composition law. □

## 9. Arbitrary base change and the fibre formula

**Theorem 9.1.** In (1.3), the canonical comparison

\[
\beta_{g,f}:g^{-1}Rf_!E\xrightarrow{\sim}Rf'_!a^{-1}E
\tag{9.1}
\]

is an isomorphism on both domains of Section 1. It is independent of compactification, compatible with composition of morphisms, and compatible with successive changes of base.

**Proof.** Compactify \(f\) as \(pj\), and base change that factorization. Let \(\bar a:\overline X'=\overline X\times_YY'\to\overline X\) be the projection. The pulled-back \(p'\) is proper and \(j':X'\hookrightarrow\overline X'\) is open. Define (9.1) by

\[
\begin{aligned}
g^{-1}Rp_*j_!E
&\xrightarrow{\mathrm{proper\ BC}}
Rp'_*\bar a^{-1}j_!E\\
&\xrightarrow{\mathrm{open\ BC}}
Rp'_*j'_!a^{-1}E.
\end{aligned}
\tag{9.2}
\]

The first map is an isomorphism by lesson 13 for bounded-below torsion complexes, or by Proposition 5.2 for unbounded complexes over a torsion ring. The second is the exact open base change isomorphism, which acts termwise on any complex.

For a refinement \(t:\overline X_1\to\overline X_2\), the comparisons between its two definitions use the exchange \(j_{2,!}\to Rt_*j_{1,!}\). Base-change compatibility of that exchange, proved in Lemma 6.1, and composition compatibility of proper base change show that the refinement comparison square for (9.2) commutes. A common refinement handles arbitrary choices. Thus the map is independent of compactification, rather than only an abstract isomorphism between the two functors.

For a composite \(gf\), use the system (8.2). Expanding the two routes through (9.2) leaves proper base change maps for \(p,q,h\), open base change maps for \(i,j,k\), and the middle exchange \(i_!Rh_*\to Rp_*k_!\). The proper maps compose compatibly, the open maps compose compatibly, and Lemma 6.1 makes the middle square commute. This is precisely the square comparing (9.1) with (8.1). For two successive base changes of a single \(f\), the expansion is just two successive proper comparisons followed by two successive open comparisons. Their pasting equals the comparison for the composite base change; hence so does (9.1). □

For a separated finite-type scheme \(X\) over a field \(k\), with structure map \(s\), define

\[
R\Gamma_c(X,E)=R\Gamma(\operatorname{Spec}k,Rs_!E),
\qquad H^q_c(X,E)=H^q(R\Gamma_c(X,E)).
\tag{9.3}
\]

The field need not be algebraically closed. If \(j:X\hookrightarrow\overline X\) is a proper compactification over \(k\), derived direct image composition gives

\[
R\Gamma_c(X,E)=R\Gamma(\overline X,j_!E).
\tag{9.4}
\]

These equalities include the canonical comparison isomorphisms of Section 7.

**Corollary 9.2.** For any geometric point \(\bar y:\operatorname{Spec}\Omega\to Y\),

\[
(Rf_!E)_{\bar y}
\simeq R\Gamma_c(X_{\bar y},E|_{X_{\bar y}}).
\tag{9.5}
\]

In particular \((R^qf_!\mathcal F)_{\bar y}=H^q_c(X_{\bar y},\mathcal F|_{X_{\bar y}})\).

**Proof.** Apply (9.1) to \(g=\bar y\). Inverse image at this point is the exact geometric-stalk functor. The small étale topos of the algebraically closed \(\Omega\) is a point topos, whose global sections are exact. Thus its derived global sections do not introduce further cohomology, and (9.3) gives (9.5). □

For an extension \(K/k\) of algebraically closed fields, the same theorem gives the canonical isomorphism on compactly supported cohomology after scalar extension, even though ordinary cohomology of a nonproper scheme can fail such invariance. Over general fields the theorem compares the complexes \(Rs_!E\) on their field topoi; applying global sections additionally involves their Galois cohomology. One must not identify the latter groups without an argument about the fields.

## 10. Projection formula for arbitrary complexes

There is a standard adjunction map

\[
Rp_*E\otimes^L M
\longrightarrow Rp_*(E\otimes^Lp^{-1}M)
\tag{10.1}
\]

for a morphism \(p\): its adjoint is the tensor of the counit \(p^{-1}Rp_*E\to E\) with \(p^{-1}M\). Here and below tensors are over \(\Lambda\). We prove that this map is an isomorphism for proper \(p\) and torsion \(\Lambda\).

**Lemma 10.1.** Suppose \(T\) is quasi-compact, quasi-separated and has finite étale cohomological dimension for \(\Lambda\)-modules. If \(E\in D(T,\Lambda)\), \(M\in D(\Lambda)\), then

\[
R\Gamma(T,E)\otimes^L M
\xrightarrow{\sim}
R\Gamma(T,E\otimes^L\underline M).
\tag{10.2}
\]

**Proof.** Fix \(E\). Both sides are exact functors of \(M\) and commute with arbitrary sums. For the right side this uses the direct-sum argument of Proposition 5.2, now with the global-sections functor and its assumed finite cohomological dimension. The left side commutes with sums by tensor adjunction. The comparison is visibly the identity for \(M=\Lambda[t]\).

We explain why this tests every complex. A module has a free resolution in nonpositive degrees. A bounded portion of that resolution is constructed from sums of shifts of \(\Lambda\) by finitely many cones. Its entire resolution is the homotopy colimit of its successively longer brutal truncations. A homotopy colimit of a sequence is the cone of \(1-\mathrm{shift}\) on the sum of its terms. Since the functors preserve sums and cones, an isomorphism for all terms implies one for that colimit. Hence (10.2) holds for every module. For a bounded-above complex, use its increasingly long brutal truncations, each a bounded complex assembled by cones from modules, and the same homotopy-colimit argument. Finally any complex \(M\) is the homotopy colimit of its good upper truncations \(\tau_{\leq b}M\) as \(b\to\infty\): filtered colimits of modules are exact, and in every fixed cohomological degree these truncations stabilize. Each upper truncation is bounded above. This proves the assertion for arbitrary \(M\), without a finite Tor-dimension assumption. □

**Proposition 10.2.** For proper \(p\), (10.1) is an isomorphism for all \(E,M\) over a torsion ring.

**Proof.** Check geometric stalks at \(\bar y\). Inverse image commutes with derived tensor: choose K-flat resolutions, whose tensor products remain valid after exact inverse image; flatness is detected on module stalks. Unbounded proper base change identifies (10.1) there with

\[
\begin{aligned}
R\Gamma(T_{\bar y},E|_{T_{\bar y}})\otimes^L M_{\bar y}
\longrightarrow
R\Gamma\bigl(T_{\bar y},
E|_{T_{\bar y}}\otimes^L\underline{M_{\bar y}}\bigr).
\end{aligned}
\tag{10.3}
\]

The proper geometric fibre has finite dimension, so Theorem 4.1 gives the finite cohomological dimension required by Lemma 10.1. Thus every stalk comparison is an isomorphism, proving the proposition. □

**Theorem 10.3.** For separated finite-type \(f\), over a torsion ring and with arbitrary complexes,

\[
Rf_!E\otimes^L M
\xrightarrow{\sim}Rf_!(E\otimes^Lf^{-1}M).
\tag{10.4}
\]

**Proof.** Write \(f=pj\). Exact open extension by zero satisfies

\[
j_!E\otimes^Lp^{-1}M
\simeq j_!(E\otimes^Lj^{-1}p^{-1}M).
\tag{10.5}
\]

To verify this, extend a K-flat representative of \(E\) by zero. It remains K-flat: tensoring it with any acyclic complex restricts on the open to an acyclic tensor product and is zero outside; exactness is tested on stalks. Formula (10.5) is the usual tensor identification on the open and zero on the complement. Combine it with Proposition 10.2:

\[
\begin{aligned}
Rp_*j_!E\otimes^LM
&\simeq Rp_*(j_!E\otimes^Lp^{-1}M)\\
&\simeq Rp_*j_!(E\otimes^Lf^{-1}M).
\end{aligned}
\tag{10.6}
\]

The map is canonical. Under a refinement, the open tensor identification is natural, and the proper projection maps are defined from the same direct-image counits. Restricting to the support open makes their compatibility with the refinement exchange immediate; the open adjunction of Lemma 6.1 extends this equality globally. Thus (10.6) is independent of compactification under the comparisons of Section 7. □

No assumption says that a derived tensor of bounded-below \(\Lambda\)-complexes is bounded below. Over a ring of infinite global dimension it need not be. The unbounded torsion-ring domain proved in Section 5 is what makes (10.4) valid in that situation.

## 11. Excision, compact sections and Mayer–Vietoris

Let \(X\) be separated finite type over a field, \(j:U\hookrightarrow X\) an open, and \(i:Z\hookrightarrow X\) the closed complement. These schemes are Noetherian, so the open is quasi-compact and the morphisms are within our finite-type category.

**Theorem 11.1.** For a complex \(E\) on \(X\) in one of the two domains of Section 1,

\[
\begin{aligned}
R\Gamma_c(U,j^{-1}E)&\longrightarrow R\Gamma_c(X,E)
\longrightarrow R\Gamma_c(Z,i^{-1}E)\\
&\longrightarrow R\Gamma_c(U,j^{-1}E)[1]
\end{aligned}
\tag{11.1}
\]

is a distinguished triangle, natural in \(E\). Its relative version for \(f:X\to Y\) holds whenever \(U\) is quasi-compact.

**Proof.** Lesson 11 gives the termwise exact sequence

\[
0\to j_!j^{-1}E^t\to E^t\to i_*i^{-1}E^t\to0.
\tag{11.2}
\]

The maps are restriction and extension by zero; on each geometric point the sequence is either \(0\to E^t\to E^t\to0\) or \(0\to0\to E^t\to E^t\to0\). This termwise exact sequence of complexes gives a distinguished triangle. Apply the exact triangulated functor \(Rf_!\). Composition, \(Rj_!=j_!\), and \(Ri_!=Ri_*=i_*\) identify the three terms with \(R(fj)_!j^{-1}E\), \(Rf_!E\), and \(R(fi)_!i^{-1}E\). This proves the relative triangle. For the structural morphism apply \(R\Gamma(\operatorname{Spec}k,-)\) to obtain (11.1). All maps are the termwise canonical maps of (11.2), so the triangle is natural. □

For a sheaf \(\mathcal F\), equations (9.4) and (2.2) identify

\[
H^0_c(X,\mathcal F)=
\{s\in H^0(X,\mathcal F):\operatorname{Supp}(s)
\text{ is proper over }k\}.
\tag{11.3}
\]

Indeed \(j_!\mathcal F\) is a sheaf in degree zero, so its degree-zero derived global sections are ordinary sections; the support argument in Lemma 2.1 applies over the field. For proper \(X\), all of its ordinary cohomology agrees with compactly supported cohomology.

**Proposition 11.2.** If \(X=U\cup V\) with quasi-compact opens and \(W=U\cap V\), there is a relative distinguished triangle

\[
\begin{aligned}
R(f|_W)_!E|_W&\longrightarrow
R(f|_U)_!E|_U\oplus R(f|_V)_!E|_V\\
&\longrightarrow Rf_!E\longrightarrow R(f|_W)_!E|_W[1].
\end{aligned}
\tag{11.4}
\]

**Proof.** In each term of a representative complex, the sequence of extensions by zero from \(W,U,V\) to \(X\) is exact, with first arrow \((1,-1)\) and second arrow addition. At a point in both opens this is the usual sequence \(0\to A\to A\oplus A\to A\to0\); at a point in only one it is the identity sequence. Apply \(Rf_!\) and composition as in Theorem 11.1. □

Compact support also has pullback for proper maps. If \(u:X\to Y\) is proper over a field, the adjunction unit \(E\to Ru_*u^{-1}E=Ru_!u^{-1}E\), followed by composition, gives

\[
R\Gamma_c(Y,E)\longrightarrow R\Gamma_c(X,u^{-1}E).
\tag{11.5}
\]

Its composition law is the composition law for these units and Theorem 8.1. For opens, extension by zero instead gives the first arrow of excision, from the open's compact cohomology into that of the ambient scheme.

## 12. Bounds, curve finiteness and the stated general theorems

**Theorem 12.1.** If \(X\) is separated finite type of dimension \(d\) over an algebraically closed field, then for every torsion sheaf

\[
H^q_c(X,\mathcal F)=0\quad(q>2d).
\tag{12.1}
\]

If the fibres of \(f:X\to Y\) have dimension at most \(d\), then \(R^qf_!\mathcal F=0\) for \(q>2d\). On both coefficient domains,

\[
H^i(E)=0\ (i\notin[a,b])
\quad\Longrightarrow\quad
H^i(Rf_!E)=0\ (i\notin[a,b+2d]).
\tag{12.2}
\]

**Proof.** Choose a dense compactification over the field. It has the same dimension as \(X\), since every irreducible component meets the dense open and its dimension is unchanged on a nonempty open. By (9.4) and Theorem 4.1,
\(H^q_c(X,\mathcal F)=H^q(\overline X,j_!\mathcal F)=0\) above \(2d\). This proves (12.1). Formula (9.5) applies this absolute bound to every actual geometric fibre of \(f\), and geometric stalks detect zero; this proves the relative sheaf bound. The fibres of a chosen compactification might be larger, but the bound here uses a dense compactification of each fibre itself, so it remains the stated \(2d\).

For bounded-below complexes, the hypercohomology spectral sequence

\[
R^pf_!H^q(E)\Longrightarrow H^{p+q}(Rf_!E)
\tag{12.3}
\]

has \(0\leq p\leq2d\), proving (12.2). This spectral sequence can be obtained by applying the exact triangulated \(Rf_!\) to successive good truncation triangles; at a fixed total degree its filtration is finite. For unbounded complexes over a torsion ring, the chosen proper compactification first supplies a uniform finite amplitude \(N\) by Section 5. The finite-window argument reduces a fixed output degree to a bounded complex, where (12.3) is valid. Its sheaf bound \(2d\) now sharpens the original \(N\) and proves (12.2) for all complexes. The same reasoning shows that the window \([i-2d,i]\) suffices to compute \(H^i(Rf_!E)\). □

**Theorem 12.2, curve finiteness.** Let \(\dim X\leq1\), with \(X\) separated finite type over an algebraically closed field. If \(\Lambda\) is Noetherian and \(\mathcal F\) is a constructible \(\Lambda\)-module sheaf that is torsion as an abelian sheaf, then each \(H^q_c(X,\mathcal F)\) is a finitely generated \(\Lambda\)-module and is zero for \(q>2\). For a constructible finite abelian sheaf, the groups have finite cardinality.

**Proof.** A dense proper compactification \(\overline X\) has dimension at most one. Its open immersion \(j\) is quasi-compact. Lesson 11 proves that \(j_!\mathcal F\) is constructible; on the boundary stratum it is zero. The proper coefficient-ring curve theorem of lesson 12 applies to \(\overline X\) and \(j_!\mathcal F\). Equation (9.4) identifies its groups with the compact-support groups and gives finite generation. The bound follows either from that theorem or from Theorem 12.1. If \(\mathcal F\) is finite abelian, quasi-compactness and its finite constructible strata supply a common annihilator \(n\). Regard it as a constructible \(\mathbf Z/n\)-module sheaf. A finitely generated module over this finite ring is a finite group. □

The word “finite” for a module over a general Noetherian ring means finitely generated. It need not mean a finite underlying set, even when the ring has positive characteristic.

The next two results use the affine-line constructibility proof in AI Integrated Stacks, with the reduction to general morphisms and the finiteness deduction written out below. Let \(D_c\) mean that every cohomology sheaf is constructible; it does not impose boundedness. Let \(D^+_{\mathrm{tors},c}\) impose constructibility, torsion and a lower bound.

**Theorem 12.3 (general constructibility).** If \(f\) is separated of finite presentation between quasi-compact, quasi-separated schemes and \(\Lambda\) is Noetherian, then \(Rf_!\) takes \(D^+_{\mathrm{tors},c}(X,\Lambda)\) into \(D^+_{\mathrm{tors},c}(Y,\Lambda)\). If \(\Lambda\) is torsion, it also takes \(D_c(X,\Lambda)\) into \(D_c(Y,\Lambda)\). This is [Tag 0GL0](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-etale.html#more-etale-theorem-constructible-shriek). Finite presentation, rather than just finite type, is part of this assertion over a non-Noetherian base.

### Proof of general constructibility

**Proof of Theorem 12.3.** We use one geometric input from the [AI Integrated Stacks proof for the affine-line projection](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-etale.html#more-etale-lemma-constructible-shriek-rel-dim-1): if \(T\) is affine and \(p:\mathbf A^1_T\to T\), then \(R^qp_!\mathcal F\) is constructible for every \(q\) and every constructible torsion sheaf of modules over the Noetherian coefficient ring \(\Lambda\). There is no Noetherian hypothesis on \(T\), and no requirement that the torsion order be invertible on \(T\).

The input's proof descends the finitely presented coefficient data to a finitely generated \(\mathbf Z\)-subalgebra of the base ring and uses compact base change. Its geometric ingredients are the [constant-coefficient curve argument](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-etale.html#more-etale-lemma-constant-shriek-rel-dim-1) and the [locally constant coefficient argument](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-etale.html#more-etale-lemma-loc-constant-shriek-rel-dim-1). The former uses [proper smooth curve constructibility](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-etale.html#more-etale-lemma-proper-smooth-family-curves-modules), whose [prime-coefficient proof](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-etale.html#more-etale-lemma-proper-smooth-family-curves) treats the residue-characteristic case by Artin–Schreier, not by assuming invertibility. These are specific prerequisite proofs, not consequences of Poincaré duality in the later lesson.

First explain passage from sheaves to complexes. Let \(g:Z\to T\) be one of the separated finite-presentation morphisms under consideration, and suppose \(R^ag_!\mathcal G\) is constructible for every constructible torsion sheaf \(\mathcal G\) and every \(a\). The finite cohomological-amplitude result of this lesson supplies \(N\geq0\) such that \(Rg_!\) sends degrees \([u,v]\) into \([u,v+N]\). For a fixed integer \(n\), put

\[
B_n=\tau_{\geq n-N}\tau_{\leq n}E.
\]

The truncation triangles give isomorphisms

\[
H^n(Rg_!E)\ \xleftarrow{\ \sim\ }
H^n(Rg_!\tau_{\leq n}E)
\ \xrightarrow{\ \sim\ }\ H^n(Rg_!B_n).
\]

Indeed, \(Rg_!\tau_{\geq n+1}E\) has no cohomology below \(n+1\), while \(Rg_!\tau_{\leq n-N-1}E\) has no cohomology above \(n-1\). These two vanishings give the displayed isomorphisms by the long exact sequences. The bounded complex \(B_n\) is built by finitely many truncation triangles from the sheaves \(H^q(E)[-q]\), for \(n-N\leq q\leq n\). The constructible sheaves form a Serre subcategory by Lesson 11, so the long exact sequences show that \(H^n(Rg_!B_n)\) is constructible. This reasoning is degreewise: it does not assume that an object of \(D_c\) is bounded. For a general \(\Lambda\) we use it only in the stated bounded-below torsion category; for a torsion ring the unbounded functor and its amplitude were constructed earlier in this lesson. Bounded-below objects remain bounded below, and the torsion property is preserved by the construction of \(Rg_!\).

Apply this observation first to \(p:\mathbf A^1_T\to T\), using the geometric input. Repeated composition then proves preservation of constructible cohomology for \(\mathbf A^m_T\to T\) for every \(m\geq0\): each projection forgets one coordinate, its base is affine, and composition of the compact-support functors is the canonical composition proved in Section 8. For \(m=0\) the morphism and its functor are identities.

Now suppose \(X\) and \(Y\) are affine. Finite presentation provides a factorization

\[
X\xrightarrow{i}\mathbf A^m_Y\xrightarrow{p}Y
\]

in which \(i\) is a closed immersion defined by a finitely generated ideal. Thus \(i\) has finite presentation. Extension by zero along \(i\) is exact and preserves constructible sheaves: this is the finite-presentation closed-immersion case of Lesson 11, also proved in the [locally quasi-finite finite-presentation lemma](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-etale.html#more-etale-lemma-qf-f-shriek-constructible). Exactness gives \(H^q(i_*E)=i_*H^q(E)\), so it preserves the relevant category of complexes too. Since \(Rf_!\simeq Rp_!i_*\), the affine case follows. This is where finite presentation, rather than finite type alone, matters over a non-Noetherian base.

For general \(X,Y\), first restrict to an affine open of \(Y\), using compact base change. Over this open, \(X\) is quasi-compact and separated, and has a finite affine open cover. Intersections of its affine opens are affine because \(X\) is separated over the affine base. All these restricted morphisms retain finite presentation. Glue the affine cases with the compact-support Mayer–Vietoris triangle. For quasi-compact opens \(U,V\) with \(X=U\cup V\), and restrictions \(a:U\to Y\), \(b:V\to Y\), \(c:U\cap V\to Y\), it is

\[
Rc_!(E|_{U\cap V})\longrightarrow
Ra_!(E|_U)\oplus Rb_!(E|_V)\longrightarrow
Rf_!E\longrightarrow Rc_!(E|_{U\cap V})[1].
\]

To construct the triangle, use the exact extension-by-zero sequence for the two-open cover; its maps are the two restrictions with opposite signs and then their sum. The sequence is exact on every geometric stalk. Apply the derived functor and the composition identifications. Equivalently this is the [relative Mayer–Vietoris proof](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-etale.html#more-etale-lemma-relative-mayer-vietoris). Induction on the number of affine opens applies also to the intersections with the last open, which have smaller affine covers. The long exact sequence and the Serre property preserve constructibility at each step. Finally, constructibility is local on the base; its affine-local conclusions combine on a finite affine cover of the quasi-compact scheme \(Y\). This proves both asserted coefficient cases. \(\square\)

### General finiteness over an algebraically closed field

**Corollary 12.4 (general finiteness).** For separated finite-type \(X\) over an algebraically closed field and Noetherian \(\Lambda\), each \(H^i_c(X,E)\) is a finitely generated \(\Lambda\)-module for \(E\in D^+_{\mathrm{tors},c}(X,\Lambda)\), or \(E\in D_c(X,\Lambda)\) when \(\Lambda\) is torsion. This is [Tag 0GLH](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-etale.html#more-etale-lemma-finiteness-compactly-supported). For finite coefficients it gives finite groups. For a bounded constructible complex, (12.2) additionally bounds the possible degrees; an unbounded complex need not have only finitely many nonzero groups.

**Proof of Corollary 12.4.** Write \(s:X\to\operatorname{Spec}k\) for the structure morphism. Since \(k\) is a field, the finite-type morphism \(s\) has finite presentation. Theorem 12.3 therefore applies to \(Rs_!E\). The étale topos of an algebraically closed field is the topos of sets: its finite-presentation étale objects are finite disjoint unions of that point. Consequently global sections on its module sheaves is exact, and a constructible module sheaf is exactly a finitely generated \(\Lambda\)-module. From the definition

\[
R\Gamma_c(X,E)=R\Gamma(\operatorname{Spec}k,Rs_!E)
\]

we obtain \(H^i_c(X,E)=H^i(Rs_!E)\), hence the asserted finite generation. When \(\Lambda\) is finite, a finitely generated module is a quotient of a finite Cartesian power of \(\Lambda\), so its underlying set is finite. Finite generation alone does not assert finite cardinality for a general Noetherian coefficient ring. \(\square\)

The next lesson proves the relevant smooth base change theorem. Its proper smooth consequence concerns locally constant finite coefficients whose orders are invertible on the base: the sheaves \(R^qf_*\mathcal F\) are locally constant. Removing invertibility would incorrectly include characteristic-\(p\) variation of \(p\)-torsion cohomology. The general compact-support constructibility statement above, however, allows torsion of every order.

## 13. Three calculations and the role of the coefficients

Assume first that \(k\) is algebraically closed, \(n\geq2\), and \(n\) is invertible in \(k\). Put \(A=\mathbf Z/n\). Our earlier curve calculations give

\[
H^q(\mathbf P^1,A)=
\begin{cases}A&q=0,\\ A(-1)&q=2,\\0&\text{otherwise}.\end{cases}
\tag{13.1}
\]

The twist is retained: \(A(1)=\mu_n\) and \(A(-1)=\operatorname{Hom}_A(\mu_n,A)\). Although \(\mu_n\) is constant over \(k\), identifying its generator with \(1\in A\) requires a choice. More intrinsically, \(H^2(\mathbf P^1,\mu_n)=A\) is normalized by degree one, and (13.1) follows by tensoring with the constant free rank-one \(A(-1)\) and the projection formula.

**Example 13.1, the affine line.** Compactify \(\mathbf A^1\) by the single point \(\infty\) in \(\mathbf P^1\). Excision gives

\[
0\to H^0_c(\mathbf A^1,A)\to A
\xrightarrow{1}A\to H^1_c(\mathbf A^1,A)\to0,
\tag{13.2}
\]

and \(H^2_c(\mathbf A^1,A)=H^2(\mathbf P^1,A)\). A point has zero positive cohomology, and Theorem 12.1 bounds the rest. Therefore

\[
H^q_c(\mathbf A^1,A)=
\begin{cases}A(-1)&q=2,\\0& q\ne2.\end{cases}
\tag{13.3}
\]

The identity in (13.2) is actual restriction of a constant section to the boundary. □

**Example 13.2, the multiplicative group.** Its compactification in \(\mathbf P^1\) has boundary \(\{0,\infty\}\). Restriction is the diagonal \(A\to A^2\), so

\[
H^0_c(\mathbf G_m,A)=0,\quad
H^1_c(\mathbf G_m,A)=A^2/\Delta A,\quad
H^2_c(\mathbf G_m,A)=A(-1).
\tag{13.4}
\]

The difference map \((a_0,a_\infty)\mapsto a_\infty-a_0\) identifies \(A^2/\Delta A\) with \(A\); the ordering of the two boundary points fixes this sign. All other degrees vanish. □

**Example 13.3, extension by zero and ordinary direct image.** For \(j:\mathbf A^1\hookrightarrow\mathbf P^1\), \(Rj_!=j_!\). Its stalk at \(\infty\) is zero. The stalk of \(j_*A\) there is \(A\): the punctured strict local neighbourhood is connected, so its constant sections are \(A\). In fact its \(R^1j_*A\) stalk is \(A(-1)\), by the valuation/Kummer computation on that punctured neighbourhood. Thus the canonical map \(j_!A\to Rj_*A\) is not an isomorphism. Globally,

\[
R\Gamma(\mathbf P^1,j_!A)=R\Gamma_c(\mathbf A^1,A),
\qquad
R\Gamma(\mathbf P^1,Rj_*A)=R\Gamma(\mathbf A^1,A).
\tag{13.5}
\]

For example the first has zero degree-zero group, whereas the second has \(A\) in degree zero. □

The assumption that \(n\) is invertible cannot be suppressed in (13.1)–(13.4). To see the difference, let \(\operatorname{char}k=p>0\). Artin–Schreier and \(H^1(\mathbf P^1,\mathcal O)=0\) give

\[
H^q(\mathbf P^1,\mathbf F_p)=0\quad(q>0),
\qquad H^0(\mathbf P^1,\mathbf F_p)=\mathbf F_p.
\tag{13.6}
\]

Here \(x\mapsto x^p-x\) is surjective on the algebraically closed \(k\), and the coherent cohomology above degree one is zero; the full Artin–Schreier long exact sequence proves (13.6). The same boundary restrictions now give

\[
H^q_c(\mathbf A^1,\mathbf F_p)=0\ \text{for every }q,
\qquad
H^q_c(\mathbf G_m,\mathbf F_p)=
\begin{cases}\mathbf F_p&q=1,\\0&q\ne1.\end{cases}
\tag{13.7}
\]

This contrasts with the large ordinary \(H^1(\mathbf A^1,\mathbf F_p)\) computed in lesson 12. Compact-support finiteness allows characteristic torsion; its groups simply differ from the prime-to-characteristic groups. Successive exact sequences of constant \(p\)-power sheaves give the corresponding compact groups for \(\mathbf Z/p^a\): the affine-line groups remain zero, while the multiplicative group has \(\mathbf Z/p^a\) in degree one and zero elsewhere. One can also see the latter directly as the cokernel of the diagonal boundary restriction on \(\mathbf P^1\).

## 14. Exercises

Throughout Exercises 1–2, \(k\) is algebraically closed and \(n\geq2\) is invertible in \(k\). Write \(A=\mathbf Z/n\).

1. **Easy.** Compute all \(H^q_c(\mathbf A^1,A)\) using \(\mathbf A^1\subset\mathbf P^1\). Identify the boundary restriction map, rather than only the ranks.
2. **Medium.** For \(r\) distinct points of \(\mathbf P^1\), compute the compact cohomology of their complement. Include \(r=0\). Compute the Euler characteristic, using \(A\)-ranks of the resulting free modules; when \(n\) is prime this is the usual vector-space Euler characteristic.
3. **Medium.** Prove that \(Rf_!=Rf_*\) for a proper morphism. For a separated finite-type étale morphism, prove that \(Rf_!\) agrees with the exact properly supported-section functor of Section 2. Explain the local extension to a separated étale morphism without a global finite-type assumption.
4. **Medium.** Let \(X\) be separated finite type over an algebraically closed field and \(\mathcal F\) any torsion sheaf. Prove \(H^q_c(X,\mathcal F)=0\) for \(q>2\dim X\), without assuming constructibility. Retain separatedness, which is part of this lesson's definition of compact support.
5. **Hard.** Construct arbitrary base change for \(Rf_!\) from proper base change and open extension by zero. Prove that its map is independent of compactification and compatible with composition. Treat the unbounded torsion-ring case as well as bounded-below torsion complexes.

## 15. Complete solutions

**Solution 1.** Let \(j:\mathbf A^1\hookrightarrow\mathbf P^1\) and \(i:\{\infty\}\hookrightarrow\mathbf P^1\). The exact sequence \(0\to j_!A\to A\to i_*A\to0\) gives the excision long exact sequence. Constant sections on the connected projective line and on the boundary point are both \(A\); their restriction is \(a\mapsto a\), an isomorphism. Since \(H^1(\mathbf P^1,A)=0\), exactness gives \(H^0_c=H^1_c=0\). The point has no positive cohomology, so the segment surrounding degree two identifies \(H^2_c(\mathbf A^1,A)\) with \(H^2(\mathbf P^1,A)=A(-1)\). Higher groups vanish by (12.1), and negative groups vanish because a sheaf and its compact cohomology have no negative degrees. Thus (13.3) lists every group. The map to degree-two projective cohomology is the extension-by-zero map; with \(\mu_n\) coefficients its target has the degree-one normalization from lesson 10. □

**Solution 2.** Put \(D=\{x_1,\ldots,x_r\}\) and \(U=\mathbf P^1\setminus D\). If \(r=0\), the scheme is proper, so its groups are \(A\) in degree zero, \(A(-1)\) in degree two, and zero otherwise; its Euler characteristic is two.

If \(r\geq1\), \(H^0(D,A)=A^r\), and the restriction from \(H^0(\mathbf P^1,A)\) is the injective diagonal \(a\mapsto(a,\ldots,a)\). The boundary has no positive cohomology. The complete nontrivial segments of excision consequently give

\[
H^0_c(U,A)=0,\quad
H^1_c(U,A)=A^r/\Delta A,\quad
H^2_c(U,A)=A(-1).
\tag{15.1}
\]

All other groups are zero as in Solution 1. The map
\((a_1,\ldots,a_r)\mapsto(a_2-a_1,\ldots,a_r-a_1)\) is surjective onto \(A^{r-1}\), with kernel \(\Delta A\), so the middle group is free of rank \(r-1\), even for composite \(n\). The Euler characteristic is \(-(r-1)+1=2-r\). Its definition by ranks is meaningful here because every displayed module is free. The quotient \(A^r/\Delta A\) is canonical and carries boundary permutations; the chosen difference coordinates depend on the distinguished point \(x_1\). □

**Solution 3.** For proper \(f\), the factorization \(X\xrightarrow{\mathrm{id}}X\xrightarrow fY\) is a compactification. Formula (7.1) gives \(Rf_!=Rf_*\). Theorem 7.1 identifies this with any other choice, including its canonical maps.

For separated finite-type étale \(f\), quasi-finiteness and Zariski's main theorem give \(X\xrightarrow j\overline X\xrightarrow pY\), with \(p\) finite. Lesson 7 gives \(Rp_*=p_*\) and its exactness. Open \(j_!\) is exact. Therefore \(Rf_!=p_*j_!\) is exact and, by Lemma 2.1, equals \(f_!\) of (2.1) on sheaves, hence termwise on all complexes of the two domains of Section 1. Lemma 2.2 identifies it with the étale extension-by-zero functor, whose stalk is the sum over geometric lifts.

For separated étale \(f\) without global finite type, the ordinary functor is still given by (2.1). A properly supported section near an affine target has support contained in some quasi-compact open of the source. Such opens are finite type over that target and exhaust the section functor by extension of supports, as in Lemma 2.2. Its stalks remain the same direct sums, and so it is exact. This local statement does not require extending the global finite-type definition (7.1) to other morphisms. □

**Solution 4.** The empty scheme has zero groups, so suppose \(X\ne\varnothing\) and put \(d=\dim X\). Nagata supplies \(j:X\hookrightarrow\overline X\) proper over the field. Replace \(\overline X\) by the schematic closure of \(X\). Then every irreducible component meets \(X\) in a dense open, and \(\dim\overline X=d\). The sheaf \(j_!\mathcal F\) is torsion on \(\overline X\) because its stalks are either those of \(\mathcal F\) or zero. Theorem 4.1, proved using proper base change, the curve theorem, normalization and the rational-function graph induction, gives

\[
H^q(\overline X,j_!\mathcal F)=0\quad(q>2d).
\tag{15.2}
\]

By definition and proper direct image composition the left side is \(H^q_c(X,\mathcal F)\). No finiteness of stalks, common annihilator, or finite stratification was used. Torsion of every order is included. The argument applies to the separated finite-type schemes for which our compactification construction is defined. □

**Solution 5.** Choose \(X\xrightarrow j\overline X\xrightarrow pY\), and pull the factorization back along \(g:Y'\to Y\). Properness and openness survive arbitrary base change, so it computes both compact direct images. With \(\bar a:\overline X'\to\overline X\), the required map is exactly

\[
\begin{aligned}
g^{-1}Rp_*j_!E
&\longrightarrow Rp'_*\bar a^{-1}j_!E\\
&\longrightarrow Rp'_*j'_!a^{-1}E.
\end{aligned}
\tag{15.3}
\]

The first arrow is proper base change. The second is open base change, the identity on the pulled-back support open and zero elsewhere. For a bounded-below torsion complex both are isomorphisms by lesson 13 and exactness of \(j_!\). For an unbounded complex over a torsion ring, take a termwise injective K-injective resolution of \(j_!E\). Proper base change for its individual terms makes their inverse images \(p'_*\)-acyclic. The finite-dimensional proper fibres and Theorem 4.1 provide a uniform finite cohomological bound locally on the base; Lemma 5.1 allows that entire unbounded complex to compute \(Rp'_*\). Hence the first arrow of (15.3) is again an isomorphism. No boundedness or finite Tor dimension of \(E\) is substituted for this argument.

For independence, let \(t:\overline X_1\to\overline X_2\) refine a compactification. Its comparison is \(j_{2,!}E\to Rt_*j_{1,!}E\), followed by \(Rp_{2,*}\). Pulling back that exchange produces the same exchange in the pulled-back square, by Lemma 6.1. Proper comparison along \(p_2t\) is the composite of those along \(t\) and \(p_2\). Expanding (15.3) with these identifications therefore gives the same map for both choices. Cofilteredness supplies a common refinement for any two choices, and the cocycle comparisons of Theorem 7.1 finish independence.

For a composite of separated finite-type maps use (8.2). Its composition map (8.3) exchanges \(i_!\) with the middle proper image \(Rh_*\). Pulling back the exchange commutes with it by Lemma 6.1. The remaining proper and open comparisons compose by their adjunction and extension-by-zero laws. Thus the composite base-change map agrees with the one for the composite morphism. For successive changes of base the same expansion contains only consecutive proper comparisons and consecutive open comparisons, each of which pastes to the outer comparison. These arguments also prove the naturality and the asserted compatibility of the canonical maps. □

## 16. Sources and the boundary of the proof

The corresponding sections of the AI-integrated Stacks project are [Sections with compact support](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-etale.html#more-etale-section-compact-support), [Sections with finite support](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-etale.html#more-etale-section-finite-support), [Derived lower shriek via compactifications](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-etale.html#more-etale-section-derived-lower-shriek-compactification), [Properties of derived lower shriek](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-etale.html#more-etale-section-derived-lower-shriek-properties), and [Compactly supported cohomology](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-etale.html#more-etale-section-compactly-supported-cohomology). The relevant targets are 0F4V–0F52, 0F6E/0F6R, 0F7A/0F7H–0F7L, 0G28/0G2A/0GKN/0GKP/0GL5, and 0GJY/0GJZ/0GK1/0GKR. The proper dimension argument is 095U in 0A5I; its proof is developed in Section 4. Unbounded acyclic-complex computation and the direct-sum/free-resolution argument have been supplied rather than replaced by a bounded-below tensor claim.

The historical reference is P. Deligne's [SGA 4](https://www.normalesup.org/~forgogozo/SGA4/), Exposé XVII: §3.2–3.3 for compactification refinement and gluing; §5.1.5–5.1.16 for exchange, construction, composition and localization; and §5.2.3–5.2.9 for canonical base change, the fibre bound and projection. The present text uses constant commutative coefficient rings and states its two derived domains explicitly.

For the Nagata historical passage, Deligne, *Le théorème de plongement de Nagata*, Kyoto Journal of Mathematics 50 (2010), 661–670 ([free in the IAS collected works](https://publications.ias.edu/node/2562)), Theorem 1.6 on page 668, states the embedding in a proper scheme under the paper's global Noetherian convention. Taking the closure of the locally closed image makes the embedding open in a proper scheme. The quasi-compact, quasi-separated generality used here is the modern statement 0F41; it is not attributed to the broader scope of that historical paper. The proof used here is the one linked in Section 3.

Theorem 12.3 gives the general-morphism reduction from the exact affine-line constructibility provider; Corollary 12.4 proves finiteness over an algebraically closed field. The corresponding statements are 0GL0 and 0GLH. Their Noetherian-coefficient, finite-presentation and derived-category hypotheses are retained in Section 12; the curve-provider links identify the geometric prerequisites used there. Curve finiteness, the vanishing bounds, compactification independence, coherent composition, arbitrary base change, the projection formula, excision, and every exercise solution have been proved in the lesson using the indicated earlier course results. The examples and smooth-base-change preview retain their invertibility hypotheses; characteristic torsion is included in the general compact-support construction and bounds.
