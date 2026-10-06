# Proper-support composition through a change of base

Course SH-02, unit SH02-SXP. The result below supplies the mixed pasting clause in SH02-FF-IMP-COMPOSE-LCH relative to the stated prerequisites. It does not admit those prerequisites or the course.

## SH02-SXP-DOMAINS — The diagram and the maps

Let $k$ be any commutative unital ring. All sheaves are sheaves of arbitrary $k$-modules. Let $X,Y,Z,Z'$ be locally compact Hausdorff spaces and let

\[
X\xrightarrow{g}Y\xrightarrow{f}Z,
\qquad a:Z'\longrightarrow Z
\tag{SXP.1}
\]

be continuous maps. Set $Y'=Y\times_Z Z'$ and $X'=X\times_Z Z'$, with maps $b:Y'\to Y$, $c:X'\to X$, $g':X'\to Y'$ and $f':Y'\to Z'$. The two squares and their outer rectangle are cartesian. The fibre products are locally compact Hausdorff: each is a closed subspace of the relevant product, since the space over which the product is taken is Hausdorff. We identify $X'$ with $X\times_Y Y'$ by its canonical homeomorphism.

Work throughout in the classical categories $D^+(k_W)$ with a global lower bound for each object. Write

\[
m_{f,g}:f_!g_!\xrightarrow{\sim}(fg)_!,
\qquad C_{f,g}:Rf_!Rg_!\xrightarrow{\sim}R(fg)_!
\tag{SXP.2}
\]

for the section identification and its normalized derived comparison. Write

\[
\beta_{f,a}:a^{-1}f_!\longrightarrow f'_!b^{-1},
\qquad B_{f,a}:a^{-1}Rf_!\xrightarrow{\sim}Rf'_!b^{-1}
\tag{SXP.3}
\]

for pullback of properly supported sections and the derived base-change map. The symbols with $(g,b)$ or $(fg,a)$ have the corresponding meaning.

The inputs from Proper supports and the bounded classical comparison are SH02-SIX-COMPACTIFICATION, SH02-SIX-COMPOSE and SH02-SIX-BASECHANGE. In particular, $g_!I$ is $f_!$-acyclic for every injective sheaf $I$, and the same assertion holds for the primed pair. This acyclicity is an established input here. We do not deduce it from the pasting theorem that we are about to prove.

No finite dimension, countability, manifold, constructibility, field or perfection hypothesis is imposed. No exceptional inverse image or tensor product occurs in the theorem. Thus neither finite integral cohomological dimension nor finite global dimension of $k$ is needed for it. The finite integral bounds required when exceptional adjoints are taken are retained separately below.

## SH02-SXP-SUPPORTS — The equation before deriving

For an open $V\subset Y$, a section of $g_!E$ is a section of $E$ on $g^{-1}V$ whose closed support is proper over $V$. These are the actual sections defining $g_!$.

We first spell out $m_{f,g}$. If a section of $g_!E$ over $f^{-1}W$ has support $T$ proper over $W$, let $s$ be its corresponding section on $(fg)^{-1}W$, with support $S$. The map $S\to f^{-1}W$ induced by $g$ is proper, and $T=g(S)$. Indeed, properness makes $g(S)$ closed. A germ of the pushed section is nonzero at $y$ exactly when some nonzero germ of $s$ lies over $y$: one implication follows by restriction, and the other follows because a neighborhood missing $g(S)$ carries the zero section. Thus $S\to T\to W$ is proper.

Conversely, suppose $S\to W$ under $fg$ is proper. For a compact $L\subset f^{-1}W$, the closed set $S\cap g^{-1}L$ lies in the compact set $S\cap(fg)^{-1}f(L)$, and hence is compact. Thus $g|_S$ is proper. Its image $T=g(S)$ is closed, and, for compact $K\subset W$, the set $T\cap f^{-1}K$ is the image of the compact set $S\cap(fg)^{-1}K$. Therefore $f|_T$ is proper as well. Here we use the equivalence between properness and compact inverse images for continuous maps between locally compact Hausdorff spaces. These two procedures give the same section and commute with open restriction. This proves the underived identification in (SXP.2).

The map $\beta_{f,a}$ pulls a locally represented section back to the cartesian product. Its support pulls back with it: the stalk of the inverse-image section at a point is the original stalk at its image. The pulled-back support is proper over the new target because properness is stable under base change. The construction is compatible with refinements of representatives, so it defines a sheaf morphism.

These definitions give the following equality of natural transformations on sheaves:

\[
\beta_{fg,a}\,a^{-1}m_{f,g}
=m_{f',g'}\,(f'_!\beta_{g,b})\,
 (\beta_{f,a}\,g_!).
\tag{SXP.4}
\]

Both sides send a represented section $s$ to its inverse-image section on $X'$. The support calculations above ensure that every intermediate section belongs to the indicated proper direct image. Equality holds on every represented germ and hence as a sheaf morphism. Applying these additive functors degree by degree proves (SXP.4) on every bounded-below complex, including its differential. This last assertion will be needed: equality on degree-zero cohomology alone would not suffice.

## SH02-SXP-RESOLUTIONS — A comparison principle for actual morphisms

Let $\mathcal A$ be an abelian category with enough injectives, let $F:\mathcal A\to\mathcal B$ be left exact, and let $u:\mathcal B\to\mathcal E$ be exact. Write $Q$ for passage from bounded-below complexes to the derived category. Applying a bounded-below injective resolution $K\to I$ gives

\[
\eta_F(K):F K\longrightarrow RF(QK),
\qquad RF(QK)=F I.
\tag{SXP.5}
\]

The equality here means the canonical resolution model in the derived category. Resolutions and their maps are taken in the homotopy category; comparison maps exist and are unique up to homotopy. The exact functor $u$ preserves quasi-isomorphisms. Consequently $uRF$ is the right derived functor of $uF$, with comparison $u\eta_F$.

We shall use the following elementary uniqueness principle. If $H:D^+(\mathcal A)\to D^+(\mathcal E)$ is a functor and two natural transformations

\[
\tau_1,\tau_2:uRF\longrightarrow H
\]

satisfy $\tau_1(QK)u\eta_F(K)=\tau_2(QK)u\eta_F(K)$ for every bounded-below complex $K$, then $\tau_1=\tau_2$.

To prove it, first take $K=I$ to be a bounded-below complex of injectives. The map $\eta_F(I)$ is an isomorphism, because such a complex computes $RF$. Thus $\tau_1(QI)=\tau_2(QI)$ as actual morphisms in the derived category. Every object is isomorphic to some $QI$, and naturality gives equality on all objects. This argument does not use detection of morphisms by their cohomology groups.

The resolution facts just used are the content of [Stacks, Section 20.3](https://stacks.math.columbia.edu/tag/0716) and [Section 13.25](https://stacks.math.columbia.edu/tag/05TM), together with the existence and homotopy uniqueness of lifts into bounded-below injective complexes. They are also part of SH02-IMP-DERIVE. The proof of the uniqueness principle above is included to specify exactly how those facts are used.

For any continuous map $h$, abbreviate its comparison (SXP.5) to $\eta_h$. The normalized composition map obeys, for every bounded-below complex $K$,

\[
\begin{aligned}
C_{f,g}(QK)\;Rf_!(\eta_g(K))\;\eta_f(g_!K)
=\eta_{fg}(K)\;m_{f,g}(K).
\end{aligned}
\tag{SXP.6}
\]

To check this normalization, resolve $K\to I$. The canonical comparison in the opposite direction, from $R(fg)_!$ to $Rf_!Rg_!$, is represented by

\[
f_!g_!I\longrightarrow Rf_!(g_!I).
\]

Its terms $g_!I^q$ are $f_!$-acyclic by the stated composition input, so this arrow is an isomorphism. Its inverse is $C_{f,g}$ after the identification $m_{f,g}$. Naturality of the resolution comparisons for $K\to I$ gives (SXP.6). This is the usual construction of the composition comparison in [Stacks, Lemma 13.22.1](https://stacks.math.columbia.edu/tag/015M); the acyclicity needed for invertibility has been explicitly retained. The construction is the comparison fixed in SH02-SIX-COMPOSE.

## SH02-SXP-BASECHANGE-NORMALIZATION — The compactification map is the derived section map

We need a corresponding equation for the particular map $B$ in (SXP.3). For any of our cartesian squares it is

\[
B_{f,a}(QK)\;a^{-1}\eta_f(K)
=\eta_{f'}(b^{-1}K)\;\beta_{f,a}(K)
\tag{SXP.7}
\]

as maps from $a^{-1}f_!K$ to $Rf'_!b^{-1}QK$. The input is an arbitrary bounded-below complex. In particular $b^{-1}K$ need not consist of injectives or of $f'_!$-acyclic sheaves.

Here is a check against the compactification construction. Factor $f=pj$ with $j:Y\hookrightarrow\overline Y$ open and $p:\overline Y\to Z$ proper, and pull this factorization back along $a:Z'\to Z$. Thus $j':Y'\hookrightarrow\overline Y'$ and $p':\overline Y'\to Z'$, with $\overline a:\overline Y'\to\overline Y$. Set

\[
e:\overline a^{-1}j_!\xrightarrow{\sim}j'_!b^{-1}.
\]

The morphism $e$ is the identity on the surviving inverse-image stalks and zero on the other stalks. It is already a natural isomorphism of exact functors on complexes. Under $f_!=p_*j_!$ and $f'_!=p'_*j'_!$, the underived map $\beta_{f,a}$ is the composite of ordinary proper base change and $p'_*e$; both pull back the same supported section.

For ordinary direct images the derived base-change morphism $B^*_{p,a}$ satisfies

\[
B^*_{p,a}(QL)\;a^{-1}\eta_{p_*}(L)
=\eta_{p'_*}(\overline a^{-1}L)\;
 \beta^*_{p,a}(L)
\tag{SXP.8}
\]

for every bounded-below complex $L$. This is an equation of actual morphisms, and it can be seen directly in the construction of [Stacks, Tag 02N7](https://stacks.math.columbia.edu/tag/02N7). Choose injective resolutions $L\to I$ and $\overline a^{-1}L\to J$. Because inverse image of constant-ring module sheaves is exact, $\overline a_*J$ is a complex of injectives. Lift the adjunction map from $L$ to $\overline a_*J$ across $L\to I$. The lift is unique up to homotopy. Its composite with $L\to I$ is the original map to $\overline a_*J$ up to homotopy. Push forward along $p$ and apply the inverse-image/direct-image adjunction for $a$. This is (SXP.8). The construction uses no preservation of injectives by $\overline a^{-1}$.

Apply (SXP.8) to $L=j_!K$. The compactification identification

\[
\rho_f:Rf_!\xrightarrow{\sim}Rp_*j_!
\]

satisfies $\rho_f\eta_f=\eta_{p_*}j_!$. Indeed, on an injective resolution $K\to I$, the sheaves $j_!I^q$ are $p_*$-acyclic by SH02-SIX-COMPACTIFICATION, and the equality is its defining acyclic-resolution comparison. The same statement holds for $f'$. Now compose (SXP.8) with $Rp'_*e$ and use naturality of $\eta_{p'_*}$ with respect to the complex isomorphism $e$. The result is exactly (SXP.7) for

\[
\rho_{f'}^{-1}\;Rp'_*e\;B^*_{p,a}\;a^{-1}\rho_f.
\tag{SXP.9}
\]

This is the map (SB.10) in SH02-SIX-BASECHANGE. Thus (SXP.7) normalizes the existing map, including its chosen compactification and its resolution comparisons. It also shows directly why a further injective resolution of a pulled-back complex introduces no ambiguity in the equation.

By the uniqueness principle of SH02-SXP-RESOLUTIONS, at most one natural transformation $a^{-1}Rf_!\to Rf'_!b^{-1}$ can satisfy (SXP.7). Consequently the comparison is independent of compactification: every allowed compactification gives (SXP.9) with the same equation (SXP.7).

## SH02-SXP-PASTING — Composition and base change commute

**Theorem.** For the diagram (SXP.1) and every $K\in D^+(k_X)$, the following two natural maps from $a^{-1}Rf_!Rg_!K$ to $R(f'g')_!c^{-1}K$ are equal:

\[
\begin{aligned}
P_K&=B_{fg,a}(K)\;a^{-1}C_{f,g}(K),\\
Q_K&=C_{f',g'}(c^{-1}K)\;
Rf'_!\bigl(B_{g,b}(K)\bigr)\;
B_{f,a}(Rg_!K).
\end{aligned}
\tag{SXP.10}
\]

Products of arrows in these formulas are read from right to left. Every arrow is the normalized comparison defined above; the theorem includes its signs and support conventions.

**Proof.** We will precompose both paths with the resolution comparison

\[
\zeta(K)=a^{-1}\!\left(
 Rf_!(\eta_g(K))\;\eta_f(g_!K)
\right)
\tag{SXP.11}
\]

from $a^{-1}f_!g_!K$, where temporarily $K$ is a bounded-below complex. By (SXP.6) and (SXP.7),

\[
P_{QK}\zeta(K)
=\eta_{f'g'}(c^{-1}K)\;
\beta_{fg,a}(K)\;a^{-1}m_{f,g}(K).
\tag{SXP.12}
\]

For the other path first use naturality of $B_{f,a}$ with respect to the morphism $\eta_g(K):g_!K\to Rg_!QK$. Then apply (SXP.7) for $(f,a)$ to the complex $g_!K$. This gives

\[
\begin{aligned}
Q_{QK}\zeta(K)
={}&C_{f',g'}\;Rf'_!(B_{g,b})\;
Rf'_!(b^{-1}\eta_g)\;\eta_{f'}(b^{-1}g_!K)\;
\beta_{f,a}(g_!K).
\end{aligned}
\tag{SXP.13}
\]

The suppressed arguments are $QK$ or $c^{-1}QK$ as forced by the domains. Equation (SXP.7) for $(g,b)$ replaces $B_{g,b}\,b^{-1}\eta_g$ by $\eta_{g'}(c^{-1}K)\,\beta_{g,b}(K)$. Naturality of $\eta_{f'}$ with respect to the complex map $\beta_{g,b}(K)$ then changes the right side of (SXP.13) to

\[
\begin{aligned}
C_{f',g'}\;Rf'_!(\eta_{g'}(c^{-1}K))\;
\eta_{f'}(g'_!c^{-1}K)\;
f'_!\beta_{g,b}(K)\;\beta_{f,a}(g_!K).
\end{aligned}
\tag{SXP.14}
\]

Apply (SXP.6) for the primed pair. We obtain

\[
\begin{aligned}
Q_{QK}\zeta(K)
={}&\eta_{f'g'}(c^{-1}K)\;
m_{f',g'}(c^{-1}K)\;
f'_!\beta_{g,b}(K)\;\beta_{f,a}(g_!K).
\end{aligned}
\tag{SXP.15}
\]

The right sides of (SXP.12) and (SXP.15) agree by the degreewise equation (SXP.4).

Finally take $K=I$ to be a bounded-below complex of injectives. The map $\eta_g(I)$ is an isomorphism. Each $g_!I^q$ is $f_!$-acyclic, so $\eta_f(g_!I)$ is also an isomorphism. Exactness of $a^{-1}$ makes $\zeta(I)$ an isomorphism. Cancelling it gives $P_{QI}=Q_{QI}$ as morphisms in $D^+(k_{Z'})$. Every bounded-below derived object has such a representative. Naturality therefore proves (SXP.10) for all $K$. $\square$

The proof never asserts that $c^{-1}I$ is injective or acyclic. Its image on the right is always derived, and the factors $\eta_{g'}$ and $\eta_{f'g'}$ are retained until the comparison equations are used. This is what permits an arbitrary continuous change of base.

## SH02-SXP-ITERATION — Longer diagrams and exceptional mates

Together with the identity and associativity of $C$ in SH02-SIX-COMPOSE and the repeated-base-change equality in SH02-SIX-BASECHANGE, (SXP.10) handles any finite rectangular array of these maps. To justify this statement, first associate each vertical composite from the right. Move a change of base through the last two pushforwards by (SXP.10), shortening that composite by one. Induction moves it through the entire string. For two successive changes of base, the fixed-map pasting equality identifies their composite with the outer base change. Associativity identifies different parenthesizations of a pushforward string. Repeating these operations proves equality for either order of reducing a finite rectangle; each step is one of the displayed equations. No infinite limit or uniform bound over an infinite family of maps is involved.

When a later application takes right mates under $Rh_!\dashv h^!$, it must separately impose the course's finite cohomological-dimension condition on $h_!$ for **all abelian sheaves**. If two maps have integral bounds $r,s$, their composite has bound $r+s$ by SH02-SIX-COMPOSE and the finite hypercohomology filtration. Thus its exceptional adjoint has the lower bound $a-r-s$ on an input with lower bound $a$, as proved in SH02-EX-ADJOINT and SH02-EX-COMPOSITION. Base-changed maps require their own such bounds; if the required integral fibre bound is available, the proper-support fibre formula supplies it. No bound is asserted for arbitrary continuous maps merely from their local compactness.

Under those hypotheses, an equality of transformations such as (SXP.10) gives an equality of its corresponding mates: a mate is obtained by composing with the fixed units and counits, so substituting equal arrows gives equal composites. The units, counits and composite trace remain those of SH02-EX-ADJOINT and SH02-EX-COMPOSITION. This formal observation adds neither a new exceptional existence theorem nor a tensor formula, and introduces no orientation identification.

## SH02-SXP-CHECKS — Two useful tests

**Exercise 1.** Take $a$ to be the identity of $Z$. Verify the theorem without choosing a resolution.

**Solution.** The three inverse-image maps are identities under the canonical fibre-product identifications. Each section pullback $\beta$ is the identity. Equation (SXP.7), evaluated on injective complexes, makes each $B$ the identity as well. Both sides of (SXP.10) are therefore $C_{f,g}$. This test checks identity normalization; it does not replace the argument for a general change of base.

**Exercise 2.** Explain the error in trying to prove (SXP.10) by resolving $K$ to $I$ and then replacing $Rg'_!c^{-1}I$ by $g'_!c^{-1}I$.

**Solution.** Inverse image is exact, but exactness alone does not preserve injective objects or proper-image acyclic objects. Such a replacement would need an additional theorem for the particular map and resolution. Equations (SXP.13)–(SXP.15) keep $Rg'_!$ derived and use the natural comparison $\eta_{g'}$. The only cancellations occur on the original side, where injectivity of $I$ and the known acyclicity of $g_!I$ justify them.

## SH02-SXP-STATUS — Exact scope of this proof

The theorem supplies the previously separate compatibility of composition of two proper direct images with the two corresponding cartesian base-change squares. It applies to all continuous maps of locally compact Hausdorff spaces and all classical bounded-below complexes over an arbitrary commutative ring. It matches the mixed clause of SH02-FF-IMP-COMPOSE-LCH together with the previously established composition and fixed-map base-change results.

The proof of this compatibility is the classical argument above. Its use of SH02-SIX-COMPOSE retains that lesson's explicit Volpe/Lurie reference imports, including the bounded comparison and the composition construction. Their proofs are not given here. The classical compactification and proper-base-change inputs retain their exact Stacks dependencies. The mathematical argument and its exposition are original course text; the cited Stacks results are mathematical references, and no source text or PDF is included.
