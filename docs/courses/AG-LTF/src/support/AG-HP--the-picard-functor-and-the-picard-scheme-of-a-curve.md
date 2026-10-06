# The Picard functor and the Picard scheme of a curve

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

A line bundle on a family can be changed by tensoring with a line bundle from the parameter scheme. That change leaves every fibre's isomorphism class unchanged. A relative parameter space should identify the two bundles. There is a second issue: classes that agree locally need not come with isomorphisms that satisfy a descent cocycle. The topology used to identify classes therefore belongs in the definition of the Picard functor.

We first remove both ambiguities when the family has a section. We then construct the Picard scheme of a curve using effective divisors. The decisive chart consists of bundles of degree \(g\) with one section and no first cohomology: the unique section gives a unique divisor. Tensor translations of this chart cover the Picard functor. Higher symmetric powers supply the properness argument and describe the Abel map's fibres.

In the curve construction, \(C/k\) is smooth, projective and geometrically connected, with genus \(g=h^1(C,\mathcal O_C)\). We prove the construction over a separably closed field, including imperfect such fields. We explain the disconnected case as a product. A convention for projective bundles remains important throughout: \(\mathbb P(V)=\operatorname{Proj}(\operatorname{Sym}V)\) parametrizes quotient lines of \(V\). Lines of sections of \(V\) are parametrized by \(\mathbb P(V^\vee)\).

## 1 The relative quotient and its sheaves

For \(f:X\to S\), write \(X_T=X\times_S T\), with projection \(f_T\). The relative Picard presheaf is the abelian group

\[
P(T)=\operatorname{Pic}(X_T)/f_T^*\operatorname{Pic}(T).
\tag{1.1}
\]

The quotient is by the image of pullback; pullback need not be injective without additional assumptions. For \(\tau\) equal to the Zariski, étale or fppf topology, define

\[
\operatorname{Pic}_{X/S,\tau}=a_\tau P,
\tag{1.2}
\]

the associated sheaf. Sheafifying \(T\mapsto\operatorname{Pic}(X_T)\) gives the same answer: a line bundle on \(T\) is already trivial on a Zariski cover, so its pullback disappears in each sheafification. There are natural maps

\[
P\longrightarrow\operatorname{Pic}_{X/S,\mathrm{Zar}}
\longrightarrow\operatorname{Pic}_{X/S,\mathrm{\acute et}}
\longrightarrow\operatorname{Pic}_{X/S,\mathrm{fppf}}.
\tag{1.3}
\]

The notation \(\operatorname{Pic}_{X/S}\) below means the last sheaf, or the étale sheaf where the comparison is proved. It never silently means the raw presheaf (1.1).

Here is the functions hypothesis used in the comparison:

\[
\mathcal O_T\xrightarrow{\sim}(f_T)_*\mathcal O_{X_T}
\quad\text{for every }T\to S.
\tag{1.4}
\]

It implies the analogous equality of sheaves of units. Indeed a function and its inverse both come from the base; their product is one on the base as well. In particular every automorphism of a line bundle on \(X_T\) is multiplication by a unique unit on \(T\).

**Proposition 1.1.** Under (1.4), every arrow in (1.3) is injective. For every \(T\), there is an exact sequence

\[
0\longrightarrow\operatorname{Pic}(T)
\xrightarrow{f_T^*}\operatorname{Pic}(X_T)
\longrightarrow\operatorname{Pic}_{X/S,\mathrm{fppf}}(T).
\tag{1.5}
\]

**Proof.** If \(f_T^*N\) is trivial, pushing forward and using (1.4) gives \(N\simeq\mathcal O_T\). The projection formula needed here is local: trivialize \(N\) on the base and apply (1.4).

Suppose a bundle \(L\) has zero class in the last group. There is an fppf cover \(T_i\to T\) on which its class is zero in (1.1). Thus \(L|_{X_{T_i}}\) is pulled back from a bundle on \(T_i\). Refine by trivializing those bundles, and choose trivializations of \(L|_{X_{T_i}}\). Their transition units on \(X_{T_i\times_T T_j}\) come uniquely from \(T_i\times_T T_j\) by (1.4). They satisfy the cocycle condition. Effective descent for line bundles constructs a bundle \(N\) on \(T\), and the same trivializations identify \(L\) with \(f_T^*N\). This proves (1.5) and the injection \(P\hookrightarrow\operatorname{Pic}_{\mathrm{fppf}}\).

Sheafification preserves injections of abelian presheaves. The target is already a sheaf for each of the three topologies. Sheafifying the injection just proved, first in the Zariski and then in the étale topology, proves all the asserted injections. \(\square\)

This argument uses equality of line-bundle classes only to obtain local isomorphisms. It constructs the cocycle explicitly from their transition units. That distinction will also explain the obstruction without a section.

## 2 A section removes scalar automorphisms

Let \(\sigma:S\to X\) be a section. A **rigidified line bundle** over \(T\) is a pair

\[
(L,\alpha),\qquad
\alpha:\sigma_T^*L\xrightarrow{\sim}\mathcal O_T.
\tag{2.1}
\]

Isomorphisms must respect \(\alpha\). Tensor product makes their isomorphism classes a group, denoted \(R_\sigma(T)\).

**Theorem 2.1.** If (1.4) holds and \(f\) has the section \(\sigma\), then

\[
P=\operatorname{Pic}_{X/S,\mathrm{Zar}}
=\operatorname{Pic}_{X/S,\mathrm{\acute et}}
=\operatorname{Pic}_{X/S,\mathrm{fppf}}
=R_\sigma.
\tag{2.2}
\]

More explicitly,

\[
\operatorname{Pic}(X_T)
\simeq\operatorname{Pic}(T)\oplus R_\sigma(T),
\tag{2.3}
\]

where the first projection is \(\sigma_T^*\).

**Proof.** Normalize a bundle \(M\) by

\[
M^\natural=M\otimes f_T^*(\sigma_T^*M)^{-1}.
\tag{2.4}
\]

Its restriction along the section has its natural trivialization. Tensoring \(M\) by a base bundle makes no change to this rigidified class, because the extra base factors cancel. Conversely two normalized bundles representing the same relative class differ by a base bundle whose restriction along \(\sigma_T\) is trivial, so they are isomorphic as rigidified bundles after correcting a scalar. This proves \(P(T)=R_\sigma(T)\) and (2.3).

An automorphism of \((L,\alpha)\) is a base unit by (1.4). Its value along the section is one, so it is the identity. More generally an isomorphism between two rigidified bundles, if it exists, is unique.

Now take compatible rigidified classes on an fppf cover \(T_i\to T\). On every overlap their equality gives an isomorphism respecting the rigidifications. One can obtain it from any isomorphism by dividing by its scalar along the section. Uniqueness forces the cocycle identity on triple overlaps. Effective fppf descent gives a line bundle on \(X_T\); descent of the trivializations on the section gives its rigidification. Uniqueness also proves the separated sheaf condition. Hence \(R_\sigma\) is an fppf sheaf. Its sheafifications for all three topologies are itself, proving (2.2). \(\square\)

When (1.4) holds and a section exists only Zariski locally on \(S\), the last three sheaves still agree: apply the theorem on that cover and glue the isomorphisms of sheaves. An étale-local section similarly identifies the étale and fppf sheaves. A smooth surjective family has étale-local sections, since a smooth morphism has local étale coordinates and local sections through geometric points. The raw quotient need not then be a sheaf on the original base.

## 3 The obstruction to an actual line bundle

We give the comparison without a section as well. We use one topology prerequisite here: for every scheme \(Y\), cohomology of the smooth commutative group \(\mathbf G_m\) has the same values in the étale and fppf topologies,

\[
H^i_{\mathrm{\acute et}}(Y,\mathbf G_m)
\xrightarrow{\sim}H^i_{\mathrm{fppf}}(Y,\mathbf G_m).
\tag{3.1}
\]

Only \(i=1,2\) are used. This is Grothendieck's smooth-group comparison theorem, stated precisely in Poonen, *Rational Points on Varieties*, Section 6.6.1, which also proves the degree-one case for the multiplicative group; see also Kleiman, *The Picard scheme*, Remark 2.11. It is a theorem about these topologies, not a representability theorem for Picard functors. A proof in every degree over every scheme, including compatibility with pullback, is given in [Multiplicative group cohomology and change of topology, Theorem 1](AG-HP--multiplicative-group-cohomology-and-change-of-topology.md#the-comparison-and-its-naturality).

**Theorem 3.1.** Under (1.4), the natural map
\(\operatorname{Pic}_{X/S,\mathrm{\acute et}}\to\operatorname{Pic}_{X/S,\mathrm{fppf}}\)
is an isomorphism. There is a functorial exact sequence

\[
\begin{aligned}
0\longrightarrow\operatorname{Pic}(T)
&\longrightarrow\operatorname{Pic}(X_T)
\longrightarrow\operatorname{Pic}_{X/S}(T)\\
&\xrightarrow{\delta_T}H^2_{\mathrm{\acute et}}(T,\mathbf G_m)
\longrightarrow H^2_{\mathrm{\acute et}}(X_T,\mathbf G_m).
\end{aligned}
\tag{3.2}
\]

A class is represented by a line bundle on \(X_T\) exactly when its image under \(\delta_T\) is zero.

**Proof.** For either topology, line bundles and \(\mathbf G_m\)-torsors have the same descent cocycles. A cocycle of units glues trivial line bundles, and a line bundle's frames form its torsor. Thus
\(H^1(Y,\mathbf G_m)=\operatorname{Pic}(Y)\), with the pullback maps identified.

On the relative big site over \(T\), \(R^1(f_T)_*\mathbf G_m\) is the sheaf associated to \(U\mapsto H^1(X_U,\mathbf G_m)\). Its sections over \(T\) are precisely the relevant Picard sheaf's \(T\)-points. Hypothesis (1.4) identifies \((f_T)_*\mathbf G_m\) with \(\mathbf G_m\). The degree-one and degree-two terms of the Leray spectral sequence give

\[
0\to\operatorname{Pic}(T)\to\operatorname{Pic}(X_T)
\to\operatorname{Pic}_{X/S,\tau}(T)
\to H^2_\tau(T,\mathbf G_m)\to H^2_\tau(X_T,\mathbf G_m).
\tag{3.3}
\]

To spell out the exactness, the filtration on total degree one has subobject \(E_2^{1,0}\). Its quotient is the kernel of the differential
\(d_2:E_2^{0,1}\to E_2^{2,0}\). The cokernel of that differential injects into total degree two. This is exactly the five-term sequence (3.3). Leray for a morphism of sites is the foundational result used here [Stacks, Tag 0732; for small étale sites, Tag 03QC].

Compare (3.3) for the two topologies. The Picard groups at its beginning are the same, and (3.1) identifies the two groups at its end. Equivalently both middle Picard groups are extensions of the same quotient (1.1) by the same kernel

\[
\ker\bigl(H^2(T,\mathbf G_m)\to H^2(X_T,\mathbf G_m)\bigr).
\]

The diagram chase for these short exact sequences proves that the canonical comparison map is an isomorphism. Equation (3.2), its naturality and the stated vanishing criterion follow. \(\square\)

There is a concrete description of \(\delta_T\). Represent a Picard class by local bundles \(L_i\), choose local isomorphisms between their pullbacks, and refine overlaps when necessary. On a triple overlap, the composite differs from the identity by a scalar unit \(c_{ijk}\) on the base, using (1.4). Associativity gives the degree-two cocycle identity. Changing the isomorphisms changes this cocycle by a coboundary. If a single cover is insufficient, the same construction on successive overlap refinements is a hypercover cocycle; it represents the same sheaf-cohomology class. Killing the class adjusts the isomorphisms into a descent datum. This describes the map in (3.2), and explains why equality of local classes alone is insufficient.

For a field, \(H^2_{\mathrm{\acute et}}(k,\mathbf G_m)\) is the usual Brauer group. For arbitrary schemes, one must distinguish it from the group of Azumaya algebras and from its torsion subgroup, often denoted the cohomological Brauer group. Formula (3.2) uses the displayed \(H^2\) itself. No equality of these three groups is assumed. With a section, pullback on \(H^2\) has the section's pullback as a left inverse, so \(\delta_T=0\), in agreement with Theorem 2.1.

## 4 An open chart and its translates

The following criterion constructs a scheme without first assuming that the functor is an algebraic space.

**Lemma 4.1.** Let \(G\) be a Zariski sheaf of groups on schemes over a field \(k\). Suppose \(F\subset G\) is represented by a scheme and the inclusion is represented by open immersions. Assume that for every field extension \(K/k\) and every \(x\in G(K)\), some \(a\in G(k)\) satisfies \(ax\in F(K)\). Then \(G\) is represented by a group scheme.

**Proof.** For \(a\in G(k)\), put \(F_a(T)=\{x:ax\in F(T)\}\). Translation identifies \(F_a\) with \(F\), and its inclusion in \(G\) is represented by an open immersion. The intersection \(F_a\times_G F_b\) is an open subscheme in each chart: pull back one open immersion along the other chart. The two descriptions identify the same subfunctor and therefore give a canonical isomorphism between these opens. These isomorphisms obey the cocycle identity because their composites all identify the same elements of \(G\).

Glue the schemes \(F_a\) along these open identifications to obtain a scheme \(Y\) and a map \(h_Y\to G\). This gluing creates no duplicate points on overlaps, since every chart map is a monomorphism.

Given \(x\in G(T)\), its inverse images of the \(F_a\) are open subschemes \(T_a\subset T\). They cover \(T\): at \(t\in T\), apply the field assumption to \(x_t\in G(\kappa(t))\). The resulting residue-field point factors through \(F_a\), so \(t\in T_a\). On \(T_a\), the element \(x\) is a map into the corresponding chart, and these maps glue uniquely to \(T\to Y\). Conversely the charts' maps to \(G\) glue by the sheaf property. The two constructions are inverse for all \(T\). Thus \(h_Y=G\). Yoneda turns multiplication, inverse and identity into morphisms satisfying the group axioms. \(\square\)

The covering hypothesis concerns every extension field, not merely the \(k\)-rational points of \(G\). Checking only those rational points would leave open the possibility of missing part of a test scheme.

## 5 Divisors and the nonspecial chart

For our geometrically connected curve, smoothness makes every geometric fibre integral. Over a field, a finite closed subscheme of a smooth curve has an ideal generated by a nonzerodivisor in each discrete valuation local ring. In a flat finite family, the fibrewise Cartier criterion [Stacks, Tag 062Y] makes the family a relative effective Cartier divisor. Conversely a relative effective Cartier divisor on the projective curve has finite fibres, so properness and finite presentation make it finite locally free over its parameter scheme. Its rank is the degree of its fibres. Therefore

\[
\operatorname{Hilb}^d_C=\operatorname{Sym}^d C.
\tag{5.1}
\]

The all-characteristic construction in *Hilbert and Quot schemes* proves this identification, projectivity and smoothness of the symmetric power, of dimension \(d\). The divisor construction also shows it is geometrically irreducible: the map \(C^d\to\operatorname{Sym}^d C\) obtained by adding the graphs is surjective on geometric points, and \(C^d\) is geometrically irreducible.

Suppose \(C\) has a point \(p\in C(k)\). Then (1.4) holds. On \(C\), a regular function is constant: a nonconstant one would give a nonconstant map to \(\mathbb A^1\), contradicting properness, or equivalently the pole-free divisor of such a function. Geometric connectedness gives \(H^0(C,\mathcal O_C)=k\). For an affine \(T=\operatorname{Spec}A\), the affine-cover complex for \(C_T\) is the complex for \(C\) tensored with \(A\); tensoring over the field is exact. Its degree-zero kernel is \(A\). Localization on \(T\) proves (1.4). By Theorem 2.1 the Picard functor is thus the sheaf of bundles normalized along \(p\).

Let \(F\subset\operatorname{Pic}_{C/k}\) consist of those normalized bundles \(L\) for which

\[
H^0(C_t,L_t)\text{ has dimension }1,
\qquad H^1(C_t,L_t)=0
\quad(t\in T).
\tag{5.2}
\]

The condition is compatible with arbitrary base change. The finite locally free cohomology complex for a flat bundle on a projective family [Stacks, Tag 0A1H] shows that it is open and that, on this open,

\[
R(f_T)_*L=N[0]
\quad\text{for a line bundle }N\text{ on }T.
\tag{5.3}
\]

For precision, a finite free complex near a point can have all its pairs joined by invertible differential entries cancelled. If its fibre cohomology is one-dimensional in degree zero alone, its remaining differentials have maximal required ranks on a neighbourhood, and the residual degree-zero module is a line bundle. This is the openness assertion of Tag 0B9S. No representability of Picard is needed to apply it to the line bundle supplied by any test scheme. It proves that \(F\to\operatorname{Pic}_{C/k}\) is represented by open immersions.

Riemann–Roch gives \(\deg L_t=g\) in (5.2), because
\(\chi(L_t)=\deg L_t+1-g=1\).

**Proposition 5.1.** The open functor \(F\) is represented by the open subscheme

\[
W=\{D\in\operatorname{Sym}^g C:H^1(C,\mathcal O_C(D))=0\}.
\tag{5.4}
\]

The Abel map identifies \(W\) with this open in the Picard functor.

**Proof.** The universal divisor on \(C\times\operatorname{Sym}^g C\) supplies \(\mathcal O(D)\). Normalize it by (2.4). Condition (5.2) cuts out the open \(W\); Riemann–Roch shows that degree \(g\) and \(H^1=0\) force \(h^0=1\). We therefore have \(W\to F\).

For the inverse, let \((L,\alpha)\in F(T)\), and put \(N=(f_T)_*L\). The evaluation map

\[
f_T^*N\longrightarrow L
\tag{5.5}
\]

is nonzero on every fibre, by (5.3) and base change. A nonzero section of a line bundle on an integral curve is a nonzerodivisor. The fibrewise Cartier criterion makes its zero locus a relative effective Cartier divisor \(D\), and

\[
\mathcal O(D)=L\otimes f_T^*N^{-1}.
\tag{5.6}
\]

This divisor is finite locally free of degree \(g\), so gives \(T\to\operatorname{Sym}^g C\). Equation (5.6) gives \(H^1(\mathcal O(D_t))=0\), so this map factors through \(W\).

Both inverses can be checked without selecting a generator of \(N\). Starting with \(D\in W(T)\), the canonical section \(1\) of \(\mathcal O(D)\) spans its one-dimensional space of sections on every fibre. Hence \(\mathcal O_T\to(f_T)_*\mathcal O(D)\) is an isomorphism. Its evaluation has exactly the original zero divisor \(D\); normalization only tensors its source and target by the same base line bundle, and leaves its zero scheme unchanged. Starting with \(L\), normalize (5.6) along \(p\); the base factor \(N^{-1}\) cancels in (2.4), so it recovers \((L,\alpha)\). All evaluation maps and identifications commute with base change. These are inverse transformations on every test scheme. \(\square\)

The empty divisor covers genus zero: \(\operatorname{Sym}^0 C\) is a point, and \(W\) has the same interpretation.

## 6 Why these charts cover over a separably closed field

The translate used to reach \(W\) must be defined over \(k\), even when the bundle to be translated is defined over a much larger field.

**Lemma 6.1.** Let \(k\) be separably closed and \(K/k\) any field extension. Given a line bundle \(L\) on \(C_K\), there is a line bundle \(M\) on \(C\) such that

\[
h^0(C_K,L\otimes M_K)=1,
\qquad h^1(C_K,L\otimes M_K)=0.
\tag{6.1}
\]

**Proof.** First note that \(C(k)\) is infinite. A nonempty open of a smooth curve has an étale coordinate map to a nonempty open of \(\mathbb A^1_k\). For any rational point in its image, the nonempty étale fibre has a point over a finite separable extension of \(k\), hence over \(k\) itself. Shrinking away from finitely many points repeats the argument. This also gives a rational point \(p\) on \(C\). The density statement for smooth schemes is [Stacks, Tag 056U].

Twist \(L\) by a sufficiently positive power of an ample bundle on \(C\), obtaining a bundle \(L'\) with \(H^1(C_K,L')=0\) and \(h^0(C_K,L')=r\geq1\). Serre vanishing gives the first condition and Riemann–Roch the second.

If \(r>1\), choose a nonzero section. Its zero divisor is finite, so cannot contain the infinitely many distinct \(K\)-points obtained from \(C(k)\). Choose \(x\in C(k)\) where the section is nonzero. The sequence

\[
0\to L'(-x_K)\to L'\to L'|_{x_K}\to0
\]

has surjective evaluation on global sections. Its cohomology sequence gives

\[
h^0(L'(-x_K))=r-1,
\qquad H^1(L'(-x_K))=0.
\]

Repeat until there is one section. The final twist is the chosen ample power minus a sum of \(k\)-rational points, and is therefore \(M_K\) for a bundle \(M\) defined on \(C\). This proves (6.1), even when \(k\) is imperfect and \(K\) is transcendental over it. \(\square\)

**Theorem 6.2.** For a smooth projective geometrically connected curve over a separably closed field, the Picard functor is represented by a smooth separated group scheme, locally of finite type and of dimension \(g\).

**Proof.** Choose the rational point supplied by Lemma 6.1. Theorem 2.1 identifies the functor with normalized bundles. Proposition 5.1 gives the represented open \(W\). Lemma 6.1 says exactly that its tensor translates by \(\operatorname{Pic}_{C/k}(k)\) cover at all field-valued points. Lemma 4.1 now constructs the representing scheme \(P_C\).

Each chart is isomorphic to \(W\), an open in the smooth \(g\)-dimensional \(\operatorname{Sym}^g C\). Smoothness, local finite type and the dimension assertion follow on this open cover. In particular, the argument establishes smoothness directly from the charts; it does not assume the higher-dimensional Picard scheme is always smooth.

The group scheme is separated. Its identity \(\operatorname{Spec}k\to P_C\) is a closed immersion: a rational point of a scheme over a field is closed, and evaluation at that point is surjective onto \(k\). More explicitly, a specialization of this rational point is seen in an affine neighbourhood of the specialization, where the rational point corresponds to a maximal ideal and has no proper specialization. The inverse image of the identity under

\[
P_C\times P_C\longrightarrow P_C,
\qquad (a,b)\longmapsto ab^{-1},
\]

is the diagonal, so the diagonal is closed. This is the elementary separatedness argument for group schemes over a field [Stacks, Tag 047L]. \(\square\)

## 7 Degree pieces, Abel fibres and properness

The degree of a bundle in a flat family on \(C\) is locally constant: its Euler characteristic is locally constant [Stacks, Tag 0B9T], and
\(\deg L_t=\chi(L_t)-1+g\). The universal normalized line bundle exists on \(C\times P_C\), because representability and Theorem 2.1 supply it by Yoneda. Consequently

\[
P_C=\coprod_{d\in\mathbb Z}P_C^d,
\tag{7.1}
\]

with each piece open and closed. Tensor product adds degrees. Tensoring by \(\mathcal O_C(np)\) identifies \(P_C^d\) with \(P_C^{d+n}\).

For \(d\geq0\), the universal effective divisor defines the Abel map

\[
a_d:\operatorname{Sym}^d C\longrightarrow P_C^d,
\qquad D\longmapsto[\mathcal O_C(D)].
\tag{7.2}
\]

**Proposition 7.1.** For every field extension \(K/k\) and every degree-\(d\) line bundle \(L\) on \(C_K\), the scheme-theoretic fibre of \(a_d\) at \([L]\) is

\[
\mathbb P\bigl(H^0(C_K,L)^\vee\bigr).
\tag{7.3}
\]

If \(H^0(L)=0\), this projective space is empty. If \(d>2g-2\) and \(d\geq0\), then the fibre is \(\mathbb P_K^{d-g}\), and \(a_d\) is a projective bundle, smooth and surjective.

**Proof.** We prove the fibre identity on arbitrary \(K\)-schemes \(T\). A quotient line of \(H^0(L)^\vee\otimes_K\mathcal O_T\) is, by duality, a line subbundle

\[
N\hookrightarrow H^0(L)\otimes_K\mathcal O_T
\tag{7.4}
\]

whose inclusion remains injective on every fibre. Evaluation gives a section of \(L_T\otimes f_T^*N^{-1}\) that is nonzero on each fibre. Since the fibres of \(C_T/T\) are integral, its zero scheme is a relative effective Cartier divisor of degree \(d\). Its class is \([L_T]\), giving a \(T\)-point of the Abel fibre.

Conversely, a divisor in that fibre has \(\mathcal O(D)\simeq L_T\otimes f_T^*A\) for a base line bundle \(A\). This follows from Theorem 2.1, not merely from equality on the geometric fibres. Its canonical section gives \(A^{-1}\to(f_T)_*L_T\). Field-extension cohomology identifies the latter with \(H^0(L)\otimes_K\mathcal O_T\). The section is nonzero on each fibre, so this map is a line subbundle: locally one coefficient is a unit, giving a splitting and a locally free cokernel. Changing the isomorphism multiplies the section by a base unit and makes no change to the subline. The resulting subline is intrinsic, and the two constructions are inverse, by taking the same section and its zero scheme. This proves (7.3) as a functorial scheme identity, including nonreduced \(T\).

For the high-degree assertion, Serre duality identifies \(H^1(L)\) with the dual of \(H^0(\omega_C\otimes L^{-1})\). The latter bundle has negative degree when \(d>2g-2\), so has no nonzero section. Riemann–Roch now gives \(h^0(L)=d+1-g\).

Apply this to the universal normalized bundle \(\mathcal L\) on \(C\times P_C^d\). Its pushforward \(V\) is finite locally free of rank \(d+1-g\), and commutes with arbitrary base change. The evaluation/subline proof just given works over the whole \(P_C^d\) and identifies

\[
\operatorname{Sym}^d C\simeq\mathbb P_{P_C^d}(V^\vee).
\tag{7.5}
\]

It is a projective bundle of relative dimension \(d-g\), hence smooth and surjective. \(\square\)

**Theorem 7.2.** Every degree piece \(P_C^d\) is a smooth proper geometrically integral variety of dimension \(g\). The degree-zero piece is the identity component and an abelian variety. It is called the Jacobian of \(C\).

**Proof.** Choose \(d_0\geq\max(0,2g-1)\). Proposition 7.1 makes \(a_{d_0}\) surjective. The source is projective and geometrically irreducible. Its target is separated by Theorem 6.2.

First the target is quasi-compact, since it is a continuous image of a quasi-compact scheme. It is locally of finite type over \(k\), hence is of finite type. A morphism from a proper \(k\)-scheme to a separated \(k\)-scheme is proper: its graph is closed, and projection from the product is proper. Thus \(a_{d_0}\) is proper.

To see that its target is universally closed over \(k\), base change to any \(T\). For a closed subset \(B\subset P_C^{d_0}\times T\), its inverse image in \(\operatorname{Sym}^{d_0}C\times T\) is closed and has closed image in \(T\). That image equals the image of \(B\), because the projective bundle (7.5) is surjective after every base change. Thus the target's structure morphism is universally closed. Finite type and separatedness give properness.

After algebraic closure the source is irreducible, and its surjective image is irreducible. The target is smooth, hence geometrically reduced. It is therefore geometrically integral. Translation by \(\mathcal O_C((d-d_0)p)\) gives all the same properties for each \(d\).

In particular \(P_C^0\) is connected, contains the identity and is open and closed. Every connected subset through the identity remains in degree zero; hence this piece is the identity component. Tensor product makes it a commutative group scheme. A proper geometrically integral group variety is an abelian variety [Stacks, Tag 03RO, definition]; such a variety is projective [Stacks, Tag 0BFA]. Smoothness and dimension \(g\) were already established by the owned construction. \(\square\)

The same reasoning shows \(a_d\) is surjective for every \(d\geq g\): Riemann–Roch gives a nonzero section of every degree-\(d\) bundle over every extension field. Its effective zero divisor is a point of the corresponding fibre. This stronger surjectivity needs no vanishing of \(H^1\); the projective-bundle assertion requires the high-degree hypothesis.

If a smooth projective curve over separably closed \(k\) has several connected components \(C_i\), each is geometrically integral and has a rational point. A line bundle on their disjoint union is a tuple of line bundles. The Picard sheaf and its representing scheme are the product of the \(P_{C_i}\), and the degree is a multidegree. Its identity component is the product of their Jacobians, of dimension \(\sum_i h^1(C_i,\mathcal O_{C_i})\). Using one section for the whole disconnected curve would not satisfy (1.4); the componentwise argument is what proves this case.

## 8 Three examples of the comparison

### Projective space over an arbitrary base

For \(n\geq1\) and every scheme \(S\),

\[
\operatorname{Pic}_{\mathbb P^n_S/S}
=\underline{\mathbb Z}_S
=\coprod_{d\in\mathbb Z}S.
\tag{8.1}
\]

The sheaf \(\underline{\mathbb Z}_S\) assigns locally constant integer functions to a test scheme. To prove the relative assertion rather than just the field-valued one, let \(L\) be a bundle on \(\mathbb P^n_T\). At \(t\in T\), the field computation \(\operatorname{Pic}(\mathbb P^n_{\kappa(t)})=\mathbb Z\) [Stacks, Tag 0BXJ] gives \(L_t=\mathcal O(d)\). For \(L(-d)\), the fibre cohomology is one-dimensional in degree zero and zero in higher degrees [Stacks, Tag 01XT]. On a neighbourhood of \(t\), perfect cohomology and Tag 0B9S give a base line bundle \(N=(f_T)_*L(-d)\). Its evaluation

\[
f_T^*N\longrightarrow L(-d)
\]

is an isomorphism: on each fibre it is the evaluation isomorphism for the trivial bundle; a map between line bundles that is nonzero at every point is locally multiplication by a unit. The fibre cohomology condition forces the integer on that neighbourhood to be \(d\), since among bundles \(\mathcal O(e)\) on \(\mathbb P^n\), only \(e=0\) has exactly one section and no higher cohomology. Thus the integers are locally constant. On overlaps they agree by the field classification. The section \([1:0:\cdots:0]\) then normalizes the base factors and proves (8.1) for all test schemes and all three topologies. For \(n=0\), the relative functor is zero instead.

### An elliptic curve

Let \(E/k\) be a smooth projective geometrically connected genus-one curve with point \(p\). Every degree-one bundle has one section and no first cohomology. Proposition 5.1 therefore identifies the entire degree-one Picard functor with \(\operatorname{Sym}^1E=E\). The inverse assigns the unique zero divisor, a finite locally free divisor of degree one and hence the graph of a map to \(E\). This argument works over any field with the chosen point; separable closedness is unnecessary here.

Translation by \(\mathcal O_E(-p)\) gives

\[
E\xrightarrow{\sim}\operatorname{Pic}^0_{E/k},
\qquad x\longmapsto\mathcal O_E(x-p).
\tag{8.2}
\]

This is the usual elliptic group law expressed by addition of divisor classes. Tensoring by \(\mathcal O_E(dp)\) gives
\(\operatorname{Pic}_{E/k}\simeq E\times\underline{\mathbb Z}\), with the product group law. The splitting depends on \(p\).

### A real conic with no real point

Let \(C\subset\mathbb P^2_{\mathbb R}\) be \(x^2+y^2+z^2=0\). Over \(\mathbb C\), it is a projective line. Degree is preserved by every automorphism of that line, so the constant Picard sheaf \(\mathbb Z\) descends through the étale cover \(\operatorname{Spec}\mathbb C\to\operatorname{Spec}\mathbb R\). More explicitly, after this cover the sheaf is \(\underline{\mathbb Z}\) by (8.1), and both transition maps are the identity on degree; the étale sheaf condition identifies it with \(\underline{\mathbb Z}_{\mathbb R}\). Therefore

\[
\operatorname{Pic}_{C/\mathbb R,\mathrm{\acute et}}(\mathbb R)
=\mathbb Z.
\tag{8.3}
\]

Actual real line bundles have even geometric degree. The restriction of \(\mathcal O_{\mathbb P^2}(1)\) has degree two and realizes every even integer. If a real bundle had odd degree, tensoring it by a suitable integer power of this degree-two bundle would produce a real bundle of degree one. Genus-zero Riemann–Roch and duality give two real sections and no first cohomology. A nonzero section would have an effective divisor of degree one, hence a real point, a contradiction. Degree-zero real bundles are trivial: their complexifications are trivial, cohomology and faithful flatness make the evaluation from their one-dimensional real section space an isomorphism. Hence \(\operatorname{Pic}(C)=2\mathbb Z\) inside (8.3).

The odd class is thus a Picard-scheme point that is not an actual line bundle. Its \(\delta\) in (3.2) is nonzero. One can see the scalar failure directly. Parametrize the complex conic by

\[
[s:t]\longmapsto
[i(s^2+t^2):s^2-t^2:2st].
\]

Substitution checks its equation, and the degree-two Veronese map makes it an isomorphism onto the conic. In these coordinates, conjugation is induced by the semilinear map

\[
(s,t)\longmapsto(-\overline t,\overline s).
\]

Its square is \(-1\) on the two-dimensional vector space. The induced descent isomorphism on the degree-one bundle has scalar square \(-1\). Rescaling it changes this scalar by a complex norm \(a\overline a>0\), so cannot turn it into one. That scalar cocycle is the nontrivial real Brauer obstruction. The Zariski Picard sheaf at \(\operatorname{Spec}\mathbb R\) still has just \(2\mathbb Z\), since that one-point base has no nontrivial open cover. It therefore differs from the étale Picard functor.

## 9 Exercises

1. **Basic.** Compute \(\operatorname{Pic}_{\mathbb P^1_S/S}\) for every scheme \(S\). State what its \(T\)-points mean when \(T\) is disconnected.

2. **Intermediate.** For a smooth conic over a field \(k\) with no rational point, construct an étale Picard class of geometric degree one and prove that no line bundle on the conic represents it. Include imperfect fields and explain why a separable splitting field can be used.

3. **Intermediate.** For \(d\geq0\), \(d>2g-2\), prove the scheme-theoretic Abel-fibre identity (7.3) on arbitrary test schemes. Explain the dual in the quotient-line convention.

4. **Intermediate.** Prove Lemma 4.1 by gluing translated charts. Identify the precise step where the assumption over every extension field is used.

5. **Advanced.** Prove properness of \(\operatorname{Pic}^0_{C/k}\) using an Abel map with \(d\geq\max(0,2g-1)\). Justify finite type, separatedness and universal closedness individually, and do not assume that a surjective map from a proper scheme automatically settles all three.

## 10 Solutions

**1.** The answer is \(\coprod_{m\in\mathbb Z}S\). For a test scheme \(T\), it assigns a locally constant function \(m:T\to\mathbb Z\). Over the open and closed subset where \(m\) has the value \(a\), the normalized representative is \(\mathcal O_{\mathbb P^1_T}(a)\). Different components can have different integers.

For completeness, every bundle has such a representative. Its fibre at \(t\) is \(\mathcal O(a)\); twist by \(-a\), use the open rank-one cohomology locus and the evaluation isomorphism as in Section 8. The base line bundle in this expression is removed by restriction to \([1:0]\). Uniqueness of \(a\) on fibres glues the integer function, and Theorem 2.1 glues the normalized bundles. Thus this calculation concerns all test schemes, not only spectra of fields.

**2.** A smooth conic has a closed point with finite separable residue field, by the étale-coordinate argument of Lemma 6.1, applied over a separable closure; equivalently use density of separable closed points [Stacks, Tag 056U]. Such a finite separable extension \(K/k\) gives a point and identifies the conic with \(\mathbb P^1_K\): the degree-one point bundle has two sections, and its complete linear system is the usual degree-one isomorphism after geometric extension, hence is an isomorphism by faithful flatness.

On this étale cover choose the degree-one bundle. On any overlap its two pullbacks have the same Picard class. Indeed after a further separable cover trivializing the conic both are the degree-one bundle on a projective line; projective-line automorphisms preserve the integer in its Picard sheaf. These local classes therefore glue to an étale Picard class of degree one. One must glue classes here, rather than claim that chosen bundle isomorphisms satisfy a cocycle.

If a line bundle \(L\) on the conic represented this class, it would have geometric degree one. Duality gives \(H^1(L)=0\), because \(\omega_C\otimes L^{-1}\) has degree \(-3\). Riemann–Roch gives \(h^0(L)=2\). Any nonzero \(k\)-section has a zero divisor finite of degree one, which is a rational point. This contradicts the hypothesis. The argument uses no perfectness assumption and no division by two.

**3.** Put \(V=H^0(C_K,L)\). On \(T\), a point of \(\mathbb P(V^\vee)\) is a quotient \(V^\vee\otimes\mathcal O_T\twoheadrightarrow A\), or equivalently a fibrewise nonzero subline \(A^\vee\hookrightarrow V\otimes\mathcal O_T\). Evaluate this subline in \(L_T\). Its fibrewise nonzero section is regular on the integral curve fibres, and Tag 062Y makes its zero scheme a relative divisor of degree \(d\). Its bundle differs from \(L_T\) by a base factor, so it lies in the Abel fibre.

A divisor in the fibre has \(\mathcal O(D)=L_T\otimes f_T^*B\), by the rigidified comparison. The canonical section defines \(B^{-1}\to V\otimes\mathcal O_T\). It is fibrewise nonzero and therefore a subbundle, locally split by a unit coefficient. Isomorphism changes multiply by units and leave this subline unchanged. Taking the zero divisor and taking this subline are inverse even over nonreduced \(T\). This proves the scheme-theoretic identity. Duality and Riemann–Roch give \(\dim_K V=d+1-g\), so the fibre is \(\mathbb P_K^{d-g}\). The dual occurs because \(\mathbb P(V)\) parametrizes quotients of \(V\), whereas sections up to scalar are sublines of \(V\).

**4.** Let \(F_a=a^{-1}F\) for \(a\in G(k)\). Translation represents each by the same chart scheme as \(F\). The intersection \(F_a\times_G F_b\) is open in both charts by the relative openness hypothesis. Its identity as a subfunctor provides the overlap isomorphism; all triple-overlap cocycles are identities of the same subfunctor. Glue the charts using these isomorphisms.

For \(x\in G(T)\), pull back the charts to opens \(T_a\subset T\). The extension-field assumption applied to \(x_t\in G(\kappa(t))\) puts every point \(t\) in some \(T_a\). This is the step that would fail if only \(G(k)\) were covered. Maps from these opens to the corresponding charts agree and glue. The Zariski sheaf condition makes the reverse gluing into \(G(T)\) effective and unique. Thus the glued scheme represents \(G\); Yoneda gives its group structure.

**5.** Choose \(d\geq\max(0,2g-1)\). The universal normalized bundle on \(C\times P_C^d\) has vanishing first cohomology on all fibres. Its pushforward is a vector bundle of rank \(d+1-g\), and Proposition 7.1 identifies the Abel map as its projective bundle. Hence it is universally surjective.

The target is locally of finite type from its translated charts, and quasi-compact from surjectivity of the proper source, so it is of finite type. The identity of the whole Picard group scheme is closed over the field; pulling it back by the difference map makes the diagonal closed, proving separatedness. The Abel map is proper because its graph in the product with the separated target is closed, and the projection from that product is proper.

After any base change \(T\), pull a closed subset of \(P_C^d\times T\) back along the Abel map. Its image in \(T\) is closed because \(\operatorname{Sym}^d C\) is proper. Universal surjectivity shows this is exactly the original subset's image. Thus \(P_C^d\to\operatorname{Spec}k\) is universally closed. Finite type and separatedness give properness. Tensoring by \(\mathcal O_C(-dp)\) identifies this degree piece with \(P_C^0\), proving the assertion. Its geometric connectedness and smoothness were proved from the charts and the irreducible symmetric power, so the proper degree-zero group is the Jacobian abelian variety.

## What this lesson does not prove

The topology comparison, rigidified descent, group-functor gluing criterion, complete curve construction, Abel fibres and properness of the Jacobian are proved above. The construction uses no pre-existing Picard scheme for a curve.

We use these precise prerequisites:

- Effective fppf descent of quasi-coherent modules and preservation of rank-one local freeness [Stacks, Tag 023R]. Theorem 2.1 supplies the cocycle and rigidification needed in this application.
- Cohomology of \(\mathbf G_m\) agrees in étale and fppf topologies for every scheme, in particular in degrees one and two: the smooth-group comparison stated in Poonen, *Rational Points on Varieties*, Section 6.6.1. The full comparison and its naturality are proved in [Multiplicative group cohomology and change of topology, Theorem 1](AG-HP--multiplicative-group-cohomology-and-change-of-topology.md#the-comparison-and-its-naturality).
- Leray for a morphism of sites [Stacks, Tag 0732; étale version Tag 03QC]. Theorem 3.1 derives the needed exact sequence and comparison from it.
- Perfect cohomology with arbitrary base change for a finitely presented flat sheaf with proper support [Stacks, Tag 0A1H], its open rank-one degree-zero locus [Tag 0B9S], and local constancy of Euler characteristic [Tag 0B9T]. These apply to the universal line bundles on the projective curve.
- Riemann–Roch and Serre duality for smooth projective curves [Stacks, Tags 0BS6 and 0BS2]; line-bundle cohomology on projective space [Tag 01XT] and its Picard group over a field [Tag 0BXJ]. The fibrewise Cartier criterion for a flat finitely presented ambient family [Tag 062Y] and proper finite-fibre finiteness [Tag 02LS].
- *Hilbert and Quot schemes* proves the all-characteristic identification \(\operatorname{Hilb}^d C=\operatorname{Sym}^d C\) and its smooth projective structure. The criterion of Section 4 and the Picard charts are proved here, not imported from that lesson.
- A proper geometrically integral group variety is called an abelian variety [Stacks, Tag 03RO]. Its projectivity is the separate foundational result [Tag 0BFA]; the proof above establishes all the defining hypotheses for the Jacobian.

The general algebraic-space theorem says that a flat proper finitely presented family with (1.4) has an algebraic-space Picard functor [Stacks, Tag 0D2C]. It provides useful context for the next lesson, but it is not used in the curve construction. The next lesson owns the broader scheme construction from relative divisors.

## References

- Grothendieck, *Technique de descente et théorèmes d'existence en géométrie algébrique V: les schémas de Picard, théorèmes d'existence*, Bourbaki Exposé 232, §§1–2, pp. 143–148. [Original text](https://numdam.org/item/SB_1961-1962__7__143_0/).
- The Stacks project, *Picard Schemes of Curves*: the functor comparison, the open-chart criterion and curve construction [Tags 0B9J–0BA0]; *Quot and Hilbert Spaces*, Tags 0D24–0D28 and 0D2C. The tagged texts are read in the AI Integrated Stacks Project edition. [Picard schemes of curves](https://stacks.math.columbia.edu/tag/0B92), [Picard algebraic spaces](https://stacks.math.columbia.edu/tag/0D2C).
- Kleiman, *The Picard scheme*, §2, especially Theorem 2.5 and Remark 2.11. [Author's survey](https://arxiv.org/abs/math/0504020).
- Poonen, *Rational Points on Varieties*, Section 6.6: the cohomology of the multiplicative group in the Zariski, étale and fppf topologies, Grothendieck's comparison theorem for smooth commutative group schemes, and the cohomological Brauer group. [Author's version](https://math.mit.edu/~poonen/papers/Qpoints.pdf).
