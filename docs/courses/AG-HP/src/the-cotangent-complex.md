# The cotangent complex

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

The naive cotangent complex records generators and first relations. It classifies square-zero extensions, but it can discard relations among relations. The full cotangent complex retains those additional degrees. Its fundamental triangle then turns a lifting problem into a connecting class in an Ext group.

We construct it from polynomial simplicial resolutions, prove independence and functoriality, prove the fundamental triangle and its basic consequences, and derive the extension and obstruction theorems. A computation for the map from the dual numbers to their residue field will exhibit a genuine degree $-2$ term.

## 1. Simplicial algebra and the standard resolution

A simplicial module $E_\bullet$ has face maps $d_i:E_n\to E_{n-1}$ and degeneracy maps $s_i:E_n\to E_{n+1}$ satisfying the simplicial identities. Its unnormalized chain complex has differential

$$
\partial_n=\sum_{i=0}^n(-1)^i d_i.
\tag{1.1}
$$

The degenerate subcomplex is generated in degree $n$ by the images of $s_0,\ldots,s_{n-1}$. The normalized complex is the quotient by this subcomplex. It is also a direct summand of the unnormalized complex, with the same homology. For a bisimplicial module, the complex of the diagonal is naturally quasi-isomorphic to the total complex of its two normalized directions. These are the normalization and Eilenberg–Zilber facts we use. Dold–Kan identifies simplicial modules with nonnegative chain complexes [Stacks, Tags 019D and 019G]. We do not identify simplicial rings with ordinary differential graded rings; that replacement needs additional care in positive characteristic.

Let $A\to B$ be a ring map. All rings in this lesson are commutative. Let $F$ send a set $E$ to the polynomial $A$-algebra $A[E]$, and let $U$ forget an $A$-algebra to its set. The composite $G=FU$ is a comonad. Its counit evaluates a variable at the element labelling it, and its comultiplication replaces a label by the variable with that label. Define

$$
P_n=G^{n+1}B,
\qquad P_0=A[B],\quad P_1=A[A[B]],\quad\ldots.
\tag{1.2}
$$

The faces evaluate one layer and the degeneracies insert one layer:

$$
d_i=G^i\varepsilon G^{n-i},
\qquad s_i=G^i\delta G^{n-i}.
\tag{1.3}
$$

The comonad identities give the simplicial identities. Evaluation gives an augmentation $P_\bullet\to B$.

This augmentation is a resolution on underlying simplicial sets. To see the contraction, send an element $b\in B$ to its variable $[b]\in A[B]$, and in every higher degree send an element $z$ to the variable $[z]$ in the next outer polynomial layer. These extra degeneracies satisfy $d_0h=\mathrm{id}$ and $d_i h=h d_{i-1}$ for $i>0$, with the corresponding degeneracy identities. They contract each augmentation fibre. The contraction is a statement about sets; these extra maps need not be ring homomorphisms. Since the underlying additive simplicial groups are Kan, the augmentation is a trivial Kan fibration. In particular its normalized additive complex is a resolution of $B$. Each $P_n$ is a free $A$-module, so it is also a free module resolution when we forget multiplication.

We call any augmentation $R_\bullet\to B$ a polynomial resolution if every $R_n$ is polynomial over $A$ and its underlying simplicial sets map by a trivial Kan fibration to the constant set $B$. The standard resolution always provides one [Stacks, Tags 08PM and 08ND]. A polynomial ring $B$ can also be resolved by the constant resolution $R_\bullet=B$.

One can choose the initial polynomial presentation. If $R_0\to B$ is a polynomial surjection, construct a free simplicial resolution inductively by adding variables for compatible boundaries. Degenerate variables are indexed by the degeneracies of earlier nondegenerate variables. Faces of these variables are already prescribed by the simplicial identities. In degree $n$, add a new nondegenerate variable for every tuple of $n+1$ elements in degree $n-1$ whose faces match on their intersections and whose augmentations match in $B$; give that variable the specified faces. This preserves the identities and fills every boundary. Continuing in all degrees gives a trivial Kan fibration to $B$, with polynomial terms. The construction permits extra variables and prescribed fillers; we use that freedom for the degree-two calculation in Section 6.

## 2. Independence of the resolution

Put $\mathcal D_{B/A}$ for the category of polynomial $A$-algebras equipped with a map to $B$. Its morphisms are algebra homomorphisms over $B$. A covariant diagram of $B$-modules on this category has a derived colimit. Concretely, resolve the diagram by sums of diagrams

$$
R\longmapsto B[\operatorname{Hom}_{\mathcal D}(Q,R)],
\tag{2.1}
$$

where brackets mean a free module on the indicated set. These diagrams are projective by the Yoneda lemma and exactness of evaluation. Every diagram is a quotient of a sum of them. Applying colimit to such a projective resolution defines $\mathbf L\operatorname{colim}_{\mathcal D}$.

**Lemma 2.1.** If $R_\bullet\to B$ is a polynomial resolution and $E$ is a covariant $B$-module diagram on $\mathcal D_{B/A}$, then its associated simplicial module $E(R_\bullet)$ computes $\mathbf L\operatorname{colim}_{\mathcal D}E$.

**Proof.** For $Q=A[S]\to B$, the simplicial set of maps over $B$ is

$$
\operatorname{Hom}_{\mathcal D}(Q,R_\bullet)
=\prod_{s\in S}(R_\bullet)_{\beta(s)},
\tag{2.2}
$$

where $\beta(s)$ is the image of the variable $s$ in $B$, and the factor on the right is the corresponding augmentation fibre. Each fibre is contractible because the augmentation is a trivial Kan fibration. The product is contractible too: boundary lifting is performed in each coordinate, so the product map to a point remains a trivial Kan fibration.

Consequently evaluating (2.1) on $R_\bullet$ gives a free simplicial module quasi-isomorphic to $B$ in degree zero. Its colimit is also $B$, because the category of maps from $Q$ has the initial object $\mathrm{id}_Q$. Thus the evaluation claim holds for the projective generating diagrams.

For general $E$, take a projective resolution $E^\bullet\to E$ by sums of these diagrams and evaluate on $R_\bullet$. This is a double complex. Evaluation is exact, so taking homology first in the resolution direction leaves $E(R_\bullet)$. Taking homology first in the simplicial direction leaves the colimit complex $\operatorname{colim}E^\bullet$. Both compute the homology of the total complex. The construction is natural in $E$, giving the required derived identification. ∎

This is the explicit diagram-homology comparison behind [Stacks, Tag 08Q9]. It also proves that changing a polynomial resolution does not change the derived object. A map between resolutions over $B$ induces the corresponding identification, rather than an unrelated isomorphism.

Define the diagram

$$
E(P\to B)=\Omega_{P/A}\otimes_P B.
\tag{2.3}
$$

**Definition.** The cotangent complex $L_{B/A}$ is the normalized complex of the simplicial module $\Omega_{P_\bullet/A}\otimes_{P_\bullet}B$, with chain degree $n$ placed in cohomological degree $-n$.

In particular $L_{B/A}\in D^{\leq0}(B)$ and

$$
L_{B/A}\simeq\mathbf L\operatorname{colim}_{\mathcal D_{B/A}}E.
\tag{2.4}
$$

**Theorem 2.2.** The cotangent complex is well defined in $D(B)$ independently of the polynomial resolution. It is functorial in a commutative square of ring maps. For a polynomial algebra $B=A[x_s]_{s\in S}$,

$$
L_{B/A}\simeq\Omega_{B/A}[0]
=\left(\bigoplus_{s\in S}B\,dx_s\right)[0].
\tag{2.5}
$$

**Proof.** Lemma 2.1 applied to (2.3) proves independence. For a square $(A\to B)\to(A'\to B')$, the standard resolutions have canonical maps: in degree zero a variable labelled by $b$ goes to the variable labelled by its image in $B'$, and coefficients map through $A\to A'$. Iterate that rule in each degree. It respects evaluations and insertions, hence the faces and degeneracies. Taking differentials and then tensoring with the augmentations produces a canonical map

$$
L_{B/A}\otimes_B^{\mathbf L}B'\longrightarrow L_{B'/A'}.
\tag{2.6}
$$

The normalized terms of the source model are direct summands of free $B$-modules, hence projective; the complex is bounded above. Thus ordinary termwise tensor computes the derived tensor in (2.6). The construction respects composition and identities already on standard resolutions. Independence identifies these same maps in other resolution models. Finally the constant polynomial resolution of a polynomial $B$ computes its complex by Lemma 2.1, proving (2.5). ∎

## 3. Tor-independent base change

Suppose $B'=B\otimes_A A'$ and

$$
\operatorname{Tor}^A_i(B,A')=0\quad(i>0).
\tag{3.1}
$$

**Proposition 3.1.** The functoriality map is an isomorphism

$$
L_{B/A}\otimes_B^{\mathbf L}B'
\simeq L_{B'/A'}.
\tag{3.2}
$$

**Proof.** The additive normalized complex of a polynomial resolution $P_\bullet\to B$ is a projective $A$-module resolution. Tensoring it with $A'$ computes $B\otimes_A^{\mathbf L}A'$. Condition (3.1) therefore says that $P_\bullet\otimes_A A'\to B'$ remains a resolution. Its terms are polynomial $A'$-algebras; its additive augmentation is surjective in degree zero and a quasi-isomorphism, hence a trivial Kan fibration of underlying simplicial sets.

Polynomial differentials commute with base change:

$$
\Omega_{(P_n\otimes_A A')/A'}\otimes_{P_n\otimes_A A'}B'
=\Omega_{P_n/A}\otimes_{P_n}B'.
\tag{3.3}
$$

Normalizing this identity, and using the projective terms of the cotangent model, proves (3.2). ∎

In particular (3.2) holds when $A'$, or $B$, is flat over $A$. The flat-base-change exercise asks for the case $A'$ flat, where it can be written

$$
L_{(B\otimes_A A')/A'}\simeq L_{B/A}\otimes_A A'.
\tag{3.4}
$$

Tor independence is essential for ordinary tensor-product rings. For example take $A=\mathbb Z$, $B=A'=\mathbb F_p$. The ordinary tensor product is $\mathbb F_p$, whose cotangent complex over $\mathbb F_p$ is zero. But $L_{\mathbb F_p/\mathbb Z}\otimes_{\mathbb F_p}\mathbb F_p=\mathbb F_p[1]$, as Section 7 computes. The nonzero $\operatorname{Tor}^{\mathbb Z}_1(\mathbb F_p,\mathbb F_p)$ explains the failure.

A useful immediate consequence is that a flat ring epimorphism $A\to B$ has $L_{B/A}=0$. Its multiplication map identifies $B\otimes_A B$ with $B$, and flatness removes higher Tor. Apply (3.2) with $A'=B$. The left side is $L_{B/A}$ and the right side is $L_{B/B}=0$. In particular a localization has zero relative cotangent complex. This conclusion precedes the fundamental triangle.

## 4. The fundamental triangle

We use one additional homological foundation. If a quasi-isomorphism $R_\bullet\to R'_\bullet$ of simplicial rings is given, then for a degreewise flat simplicial $R_\bullet$-module $M_\bullet$, the base-change map

$$
M_\bullet\longrightarrow
M_\bullet\otimes_{R_\bullet}R'_\bullet
\tag{4.1}
$$

induces a quasi-isomorphism of associated additive complexes. The derived form replaces the tensor by its derived tensor and applies to arbitrary module complexes. This is the homological change-of-rings theorem [Stacks, Tag 08RX], specialized to simplicial objects, with normalization and Eilenberg–Zilber. It is a theorem about simplicial modules and weakly equivalent rings, independent of the cotangent complex. We list it explicitly among the foundations at the end.

**Theorem 4.1.** For ring maps $A\to B\to C$, there is a canonical distinguished triangle

$$
L_{B/A}\otimes_B^{\mathbf L}C
\longrightarrow L_{C/A}
\longrightarrow L_{C/B}
\longrightarrow
\bigl(L_{B/A}\otimes_B^{\mathbf L}C\bigr)[1].
\tag{4.2}
$$

**Proof.** We first prove a special case and a product statement to avoid using localization consequences circularly.

If $B$ is polynomial over $A$, choose a polynomial resolution $Q_\bullet\to C$ over $B$. Every $Q_n$ is polynomial over $A$ too. The polynomial differential sequence is split exact in each degree:

$$
0\to\Omega_{B/A}\otimes_B C
\to\Omega_{Q_n/A}\otimes_{Q_n}C
\to\Omega_{Q_n/B}\otimes_{Q_n}C\to0.
\tag{4.3}
$$

The first term is a constant simplicial module. Normalization is exact, and Lemma 2.1 identifies the other two complexes with $L_{C/A}$ and $L_{C/B}$. The first is $L_{B/A}\otimes_B^{\mathbf L}C$ by (2.5). This proves (4.2) when its middle ring is polynomial.

Next, for two $A$-algebras $C_1,C_2$, there is a canonical isomorphism

$$
L_{(C_1\times C_2)/A}\simeq L_{C_1/A}\oplus L_{C_2/A}
\quad\text{in }D(C_1\times C_2).
\tag{4.4}
$$

Factor through $A[t]$ by mapping $t$ to $(1,0)$. The special case just proved gives triangles for $C_1\times C_2$, $C_1$, and $C_2$ over $A[t]$. It suffices to prove (4.4) relative to $A[t]$. After inverting $t$, the second factor disappears; after inverting $t-1$, the first factor disappears. Proposition 3.1 identifies the cotangent complexes in each of these base changes. Since the two opens cover, the map is an isomorphism relative to $A[t]$. The three special-case triangles then prove (4.4) over $A$ as well.

Now suppose $B\to C$ is injective. Let $P_\bullet$ be the standard resolution of $B$ over $A$, and $Q_\bullet$ the standard resolution of $C$ over $A$. The injection makes every $Q_n$ a polynomial algebra over $P_n$: at degree zero its additional variables are the labels in $C\setminus B$, and iterating the polynomial construction preserves injections of the label sets. Form

$$
\overline Q_\bullet=Q_\bullet\otimes_{P_\bullet}B.
\tag{4.5}
$$

Its terms are polynomial over $B$. Since $P_\bullet\to B$ is a quasi-isomorphism and $Q_n$ is flat over $P_n$, the homological change-of-rings theorem (4.1) shows $Q_\bullet\to\overline Q_\bullet$ is a quasi-isomorphism on additive complexes. Thus $\overline Q_\bullet\to C$ is a polynomial resolution over $B$.

The degreewise polynomial differential sequences, tensored with $C$, are

$$
0\to\Omega_{P_n/A}\otimes_{P_n}C
\to\Omega_{Q_n/A}\otimes_{Q_n}C
\to\Omega_{\overline Q_n/B}\otimes_{\overline Q_n}C\to0.
\tag{4.6}
$$

Normalization gives a short exact sequence of complexes. Its first term computes $L_{B/A}\otimes_B^{\mathbf L}C$, because the normalized terms before tensoring are projective $B$-modules. Its second computes $L_{C/A}$ and its third computes $L_{C/B}$, by independence. The associated cone triangle is (4.2).

For arbitrary $B\to C$, use the injective graph map $B\to B\times C$, $b\mapsto(b,\bar b)$. The preceding case gives a triangle for $A\to B\to B\times C$. Tensor it with the flat projection $B\times C\to C$. Equation (4.4), once over $A$ and once over $B$, identifies the other terms with those of (4.2).

The first two arrows are the functoriality arrows. In the injective construction their chain maps are literally the maps of differentials in (4.6); Lemma 2.1 identifies the third term with its canonical derived-colimit model. The graph construction and product projections are natural. Thus the construction gives the canonical triangle, compatible with maps of the original ring diagrams, rather than just a triangle with the same objects. ∎

The tensor in the first term must be derived. Replacing it by tensoring the cohomology modules can lose both Tor terms and extension data.

## 5. Localization, étale maps, smooth maps, and tensor products

**Proposition 5.1.** For an étale map $A\to B$, $L_{B/A}=0$. For a smooth map, $L_{B/A}\simeq\Omega_{B/A}[0]$. If multiplicative sets $S\subset A$ and $T\subset B$ satisfy $S\mapsto T$, then

$$
L_{T^{-1}B/S^{-1}A}\simeq L_{B/A}\otimes_B T^{-1}B.
\tag{5.1}
$$

**Proof.** For étale $A\to B$, put $D=B\otimes_A B$. Both $A\to B$ and the diagonal ring map $D\to B$ are flat; the latter is a ring epimorphism. Thus $L_{B/D}=0$ by Section 3. Base change gives $L_{D/B}\simeq L_{B/A}\otimes_B^{\mathbf L}D$, where the base-ring $B$ is the other tensor factor. Apply the triangle to $B\to D\to B$. Its middle term is $L_{B/B}=0$ and its third term is zero. Therefore $L_{D/B}\otimes_D^{\mathbf L}B=0$, which by associativity of derived tensor is $L_{B/A}=0$.

For localization on the target, $L_{T^{-1}B/B}=0$ by Section 3. The triangle for $A\to B\to T^{-1}B$ proves $L_{T^{-1}B/A}=L_{B/A}\otimes_B T^{-1}B$. Base change from $A$ to $S^{-1}A$ gives the same object, since the target already inverts $S$; this proves (5.1).

A smooth algebra is locally étale over a polynomial algebra in relative coordinates. On each such target open, use the triangle, étale vanishing, and (2.5) to obtain $L_{B/A}=\Omega_{B/A}[0]$. Localization shows that these identifications cover the target and agree. ∎

Étale vanishing also shows, for $A\to B\to C$ with $A\to B$ étale,

$$
L_{C/A}\simeq L_{C/B}. \tag{5.2}
$$

For tensor products, suppose $B$ and $C$ are Tor-independent $A$-algebras, and put $D=B\otimes_A C$. Resolving both algebras by polynomial resolutions gives a bisimplicial polynomial algebra $P_\bullet\otimes_A Q_\bullet$. Its diagonal resolves $D$: Eilenberg–Zilber identifies its additive homology with the derived tensor product, whose positive homology vanishes by Tor independence. The polynomial differential identity then gives

$$
L_{D/A}\simeq
\bigl(L_{B/A}\otimes_B^{\mathbf L}D\bigr)
\oplus
\bigl(L_{C/A}\otimes_C^{\mathbf L}D\bigr).
\tag{5.3}
$$

Indeed the two summands come from differentiating the two tensor factors. Normalization and the two spectral sequences identify their complexes with the displayed derived tensors. Without Tor independence, the diagonal resolves the derived tensor product rather than the ordinary ring $D$, and (5.3) is not an unconditional formula for that ordinary ring.

## 6. The naive complex is the first truncation

Choose a polynomial surjection $P\to B$ with kernel $I$. The naive complex is

$$
\operatorname{NL}_{B/A}=
\left[I/I^2\xrightarrow{f\mapsto df}
\Omega_{P/A}\otimes_P B\right],
\tag{6.1}
$$

in degrees $-1,0$. Its independence was proved in Deformations of rings and schemes and the naive cotangent complex. We now identify exactly which part of $L$ it retains.

**Theorem 6.1.** There is a canonical isomorphism

$$
\tau_{\geq-1}L_{B/A}\simeq\operatorname{NL}_{B/A}.
\tag{6.2}
$$

In particular $H^0(L_{B/A})=\Omega_{B/A}$, and for a surjection $A\to B$ with kernel $I$, $H^{-1}(L_{B/A})=I/I^2$ and $H^0(L_{B/A})=0$.

**Proof.** We make the degree-two relations explicit. Start a free simplicial resolution with $P_0=P$ and

$$
P_1=P[x_f\mid f\in I],\qquad d_0x_f=f,
\quad d_1x_f=0,
\tag{6.3}
$$

with the degeneracy $P_0\to P_1$ the coefficient inclusion. This fills every compatible degree-one boundary: if $a,b\in P$ have the same image in $B$, then $b+x_{a-b}$ has faces $a,b$. Extend this beginning to a polynomial resolution by the boundary-filling construction of Section 1.

After tensoring differentials with $B$, the normalized degree-zero term is $\Omega_{P/A}\otimes_P B$, and the normalized degree-one term is the free module

$$
F=\bigoplus_{f\in I}B e_f,\qquad \partial e_f=df.
\tag{6.4}
$$

Define $\rho:F\to I/I^2$ by $e_f\mapsto\bar f$. We will show that its kernel is precisely the image of the normalized degree-two differential.

First every such boundary maps to zero under $\rho$. More generally, for any simplicial polynomial resolution with $P_0=P$, the degree-one map can be written on differentials as

$$
dg\otimes b\longmapsto
\bigl(d_0g-d_1g\bigr)b\pmod{I^2}.
\tag{6.5}
$$

The difference lies in $I$. The product rule is valid modulo $I^2$: the two faces have the same image in $B$, so the difference of a product is the sum of the differences multiplied by their common images. Thus (6.5) is a well-defined map on differentials. It vanishes on degeneracies. On a degree-two differential it gives the alternating sum of the differences of its faces, which is zero by $d_i d_j=d_{j-1}d_i$ for $i<j$. Hence degree-two boundaries lie in $\ker\rho$.

Conversely take a finite sum $\sum\bar a_f e_f\in\ker\rho$ and choose lifts $a_f\in P$. Then

$$
\sum a_f f=\sum_{j=1}^m u_jv_j,
\qquad u_j,v_j\in I.
\tag{6.6}
$$

In $P_1$ the polynomial

$$
z=\sum a_f x_f-\sum_{j=1}^m x_{u_j}x_{v_j}
\tag{6.7}
$$

has both faces zero. The compatible degree-two boundary $(z,0,0)$ therefore has a chosen polynomial filler $w$ with $d_0w=z$, $d_1w=d_2w=0$. The boundary of $dw$ in the normalized differential module is the image of $dz$. Under the augmentation, all $x_f$ vanish. Differentiating the products $x_{u_j}x_{v_j}$ therefore gives zero after tensoring with $B$, while differentiating $\sum a_f x_f$ gives exactly $\sum\bar a_f e_f$. Thus every element of $\ker\rho$ is a degree-two boundary.

It follows that the degree $-1$ term of the canonical truncation, namely $F/\operatorname{im}\partial_2$, is $I/I^2$. Its differential to degree zero is $f\mapsto df$, by (6.4). This proves (6.2). Formula (6.5), defined by faces rather than by choices of fillers, gives the comparison on any resolution and is compatible with ring maps. Independence in Theorem 2.2 and independence of (6.1) identify these comparison maps, proving canonicity.

The cokernel of the differential in (6.1) is $\Omega_{B/A}$ by the conormal sequence. For a surjection $A\to B$, one can use the polynomial presentation with no variables, namely $P=A$, obtaining $[I/I^2\to0]$ in the first truncation. ∎

This calculation explains why merely writing two presentation terms does not compute the full complex. The higher fillers ensure the augmentation is a resolution; their differentials impose the relations in degree $-1$, and still higher degrees can have their own cohomology.

## 7. Complete intersections and computations

We use finite local complete intersections: locally on the target a finite-presentation map admits a presentation by a localized polynomial algebra whose kernel is generated by a finite Koszul-regular sequence. A regular sequence is sufficient. No flatness of the map itself is assumed. The condition is invariant under changing polynomial presentation. Koszul exactness and the freeness of the conormal module are commutative-algebra foundations.

**Lemma 7.1.** If $R\to B=R/(f_1,\ldots,f_r)$ and the sequence is Koszul regular, then

$$
L_{B/R}\simeq (I/I^2)[1],\qquad I=(f_1,\ldots,f_r).
\tag{7.1}
$$

**Proof.** First take $U=\mathbb Z[t_1,\ldots,t_r]$ and $U\to\mathbb Z$ with $t_i\mapsto0$. The triangle for $\mathbb Z\to U\to\mathbb Z$ has middle term zero and first term $\bigoplus\mathbb Z\,dt_i$ in degree zero. Hence

$$
L_{\mathbb Z/U}\simeq\mathbb Z^r[1].
\tag{7.2}
$$

Map $U\to R$ by $t_i\mapsto f_i$. The Koszul resolution of $\mathbb Z$ over $U$, tensored with $R$, is the Koszul complex on the $f_i$. Exactness means exactly that $R$ and $\mathbb Z$ are Tor independent over $U$ and their derived tensor is the ordinary ring $B$. Proposition 3.1 and (7.2) yield $L_{B/R}=B^r[1]$. Koszul regularity identifies the basis vectors with the classes of $f_i$ in $I/I^2$, proving (7.1). ∎

**Theorem 7.2.** For a local complete intersection map $A\to B$, the cotangent complex is perfect of Tor amplitude in $[-1,0]$. In a local presentation $B=P/(f_1,\ldots,f_r)$ with $P$ a localized polynomial algebra,

$$
L_{B/A}\simeq
\left[I/I^2\xrightarrow{df}
\Omega_{P/A}\otimes_P B\right].
\tag{7.3}
$$

**Proof.** Polynomial and localization computations give $L_{P/A}=\Omega_{P/A}[0]$. Lemma 7.1 gives $L_{B/P}=(I/I^2)[1]$. The fundamental triangle for $A\to P\to B$ then shows that $L_{B/A}$ has no cohomology outside $[-1,0]$. Theorem 6.1 identifies it with (7.3). Both terms are finite locally free: the conormal module has the regular-sequence basis and the polynomial differential module has its coordinate basis. Such a two-term complex is perfect and, when tensored with any module, remains concentrated in the same two degrees. This proves the Tor-amplitude assertion locally and hence globally on the target. ∎

Concentration of cohomology and Tor amplitude are different assertions. The freeness of the two displayed modules is what gives the latter. The proof does not require the map $I/I^2\to\Omega_{P/A}\otimes B$ to be injective.

### Dual numbers over a field

For $B=k[x]/(x^2)$, the element $x^2$ is regular in $k[x]$ in every characteristic. Thus

$$
L_{B/k}=\left[B e\xrightarrow{e\mapsto 2x\,dx}B\,dx\right].
\tag{7.4}
$$

If $\operatorname{char}k\ne2$, then $H^{-1}(L)=(x)e$ and $H^0(L)=(B/(x))dx$. Both are one-dimensional over $k$. If $\operatorname{char}k=2$, the differential is zero and both groups are free rank one over $B$, hence two-dimensional over $k$. In either case the complex is perfect with the stated amplitude.

### Reduction modulo a prime

The integer $p$ is regular in $\mathbb Z$. Therefore

$$
L_{\mathbb F_p/\mathbb Z}\simeq\mathbb F_p[1].
\tag{7.5}
$$

The shift $[1]$ means that the module is in cohomological degree $-1$. It does not mean degree $+1$.

### A non-complete-intersection map with a degree $-2$ term

Let $B=k[x]/(x^2)$ and let $B\to k$ send $x$ to zero. Apply the triangle to $k\to B\to k$. Its middle term is $L_{k/k}=0$, so

$$
L_{k/B}\simeq\bigl(L_{B/k}\otimes_B^{\mathbf L}k\bigr)[1]
\simeq k[1]\oplus k[2].
\tag{7.6}
$$

The derived tensor in (7.6) is computed directly from the two free terms in (7.4); its differential becomes zero in every characteristic because $x$ maps to zero. Consequently

$$
H^{-1}(L_{k/B})=k,
\qquad H^{-2}(L_{k/B})=k.
\tag{7.7}
$$

This is a fully computed non-lci map, rather than an example whose lower cohomology is only asserted. Its ideal $(x)\subset B$ is generated by a zero divisor, and its cotangent complex contradicts the amplitude required of an lci map. The naive complex sees only $k[1]$ and loses $k[2]$. It therefore cannot satisfy the full fundamental triangle for these three maps; the earlier lesson's warning now has an exact derived explanation.

## 8. Square-zero extensions and Ext

Let $M$ be a $B$-module. Write $\operatorname{Exal}_A(B,M)$ for isomorphism classes of square-zero $A$-algebra extensions

$$
0\to M\to E\to B\to0,
\tag{8.1}
$$

with the given identification of the kernel. The extension lesson proved, including its Baer addition and derivation automorphisms,

$$
\operatorname{Exal}_A(B,M)
\simeq\operatorname{Ext}^1_B(\operatorname{NL}_{B/A},M).
\tag{8.2}
$$

**Theorem 8.1.** There are canonical identifications

$$
\operatorname{Exal}_A(B,M)\simeq\operatorname{Ext}^1_B(L_{B/A},M),
\qquad
\operatorname{Aut}(E/B,M)\simeq
\operatorname{Ext}^0_B(L_{B/A},M)=\operatorname{Der}_A(B,M).
\tag{8.3}
$$

**Proof.** Put $K=\tau_{\leq-2}L_{B/A}$. The truncation triangle is

$$
K\to L_{B/A}\to\operatorname{NL}_{B/A}\to K[1].
\tag{8.4}
$$

By the standard derived-category degree orthogonality, $\operatorname{Hom}(K,M)=0$ and $\operatorname{Hom}(K,M[1])=0$: the source is in degrees at most $-2$, whereas the targets begin in degree zero or $-1$. Applying $\operatorname{Hom}(-,M[1])$ to (8.4) therefore identifies $\operatorname{Ext}^1(\operatorname{NL},M)$ with $\operatorname{Ext}^1(L,M)$. Combining with (8.2) proves the first assertion, including the group law. The same truncation argument in degree zero gives $\operatorname{Ext}^0(L,M)=\operatorname{Hom}(\Omega_{B/A},M)$, which is the derivation group.

For an automorphism explicitly, add $D(\bar e)$ to each $e\in E$, where $D:B\to M$ is an $A$-derivation. The derivation rule and $M^2=0$ make this a ring automorphism fixing the kernel and quotient; its inverse uses $-D$. Conversely any such automorphism differs from the identity by exactly such a derivation. ∎

The truncation argument does not identify Ext in degree two. That is precisely where the lower part of $L$ can matter.

## 9. A canonical obstruction in degree two

Let $A'\to A$ be surjective with square-zero kernel $J$. Fix $A\to B$, a $B$-module $M$, and an $A$-linear map $c:J\to M$. We seek an $A'$-algebra extension (8.1) whose structural map from $A'$ sends $J$ into its kernel by $c$.

**Theorem 9.1.** There is a canonical class

$$
\operatorname{ob}(c)\in\operatorname{Ext}^2_B(L_{B/A},M)
\tag{9.1}
$$

whose vanishing is necessary and sufficient for such an extension to exist. When it exists, its isomorphism classes form a torsor under $\operatorname{Ext}^1_B(L_{B/A},M)$, and its automorphisms are $\operatorname{Ext}^0_B(L_{B/A},M)$.

**Proof.** Theorem 6.1 for the surjection $A'\to A$ gives

$$
H^0(L_{A/A'})=0,\qquad H^{-1}(L_{A/A'})=J.
\tag{9.2}
$$

Its canonical truncation map $L_{A/A'}\to J[1]$, followed by $c[1]$, defines an element of $\operatorname{Ext}^1_A(L_{A/A'},M)$. Derived tensor–Hom adjunction identifies this group with

$$
\operatorname{Ext}^1_B(L_{A/A'}\otimes_A^{\mathbf L}B,M)
=\operatorname{Hom}_A(J,M).
\tag{9.3}
$$

For the equality, the source of the Ext group has no degree-zero cohomology and has $H^{-1}=J\otimes_A B$; its terms below $-1$ contribute nothing to Ext in degree one. Thus the element in (9.3) is exactly the specified map $c$.

Apply $\mathbf R\operatorname{Hom}_B(-,M)$ to the fundamental triangle for $A'\to A\to B$. Its long exact sequence includes

$$
0\to\operatorname{Ext}^1_B(L_{B/A},M)
\to\operatorname{Ext}^1_B(L_{B/A'},M)
\xrightarrow{r}\operatorname{Hom}_A(J,M)
\xrightarrow{\partial}\operatorname{Ext}^2_B(L_{B/A},M).
\tag{9.4}
$$

The initial zero follows because $L_{A/A'}\otimes_A^{\mathbf L}B$ lies in degrees at most $-1$ and hence has no maps to $M$ in degree zero. Define $\operatorname{ob}(c)=\partial(c)$.

By Theorem 8.1, the middle Ext group classifies square-zero $A'$-algebra extensions of $B$ by $M$. Its map $r$ sends such an extension to its structural action on $J$. This can be checked in a polynomial presentation: restrict the lifted polynomial map along $A'$, and a relation $j\in J$ is sent to its image in the extension kernel. Equivalently, pull back the extension along $A\to B$; as an $A'$-algebra extension of $A$ its conormal map is precisely $j\mapsto c(j)$, by the presentation classification of the preceding lesson. Thus the desired extensions are exactly the fibre $r^{-1}(c)$.

Exactness of (9.4) proves the obstruction criterion. If the fibre is nonempty, it is a torsor under the injective kernel group $\operatorname{Ext}^1_B(L_{B/A},M)$. Automorphisms of a solution are $A'$-derivations $B\to M$; because $A'$ acts on $B$ through its surjective image $A$, these are precisely $A$-derivations. Theorem 8.1 identifies them with the stated degree-zero Ext group. ∎

This is a general ring-extension theorem, with no flatness or smallness assumption beyond $J^2=0$. Its class is natural in $c$ and in maps of the ring diagrams.

For flat deformation theory, assume in addition that $B$ is flat over $A$, put

$$
M=J\otimes_A B,\qquad c(j)=j\otimes1.
\tag{9.5}
$$

A solution is then exactly a flat lift $B'$ over $A'$ with $B'\otimes_{A'}A=B$ and identified reduction. Indeed the images of $J$ generate its whole kernel by (9.5), so $JB'=M$. The multiplication map $J\otimes_A B\to M$ is the prescribed identity and is injective. Together with flatness of $B/A$, the square-zero flatness criterion proves $B'/A'$ flat. Conversely a flat lift has kernel $J\otimes_A B$ and supplies such a solution. This is the precise scope in which (9.1) is the obstruction to extending a flat deformation.

For an affine lci algebra, Theorem 7.2 makes the derived Hom complex a two-term complex of degrees zero and one, so $\operatorname{Ext}^2_B(L_{B/A},M)=0$. These affine lifting problems are unobstructed. For a nonaffine lci scheme, global cohomology can still produce degree-two Ext; affine unobstructedness must not be asserted as a global theorem without a gluing argument.

## 10. Morphisms of schemes

For $f:X\to S$, work on the Zariski site of $X$ and apply the standard polynomial construction to the homomorphism of sheaves of rings

$$
f^{-1}\mathcal O_S\longrightarrow\mathcal O_X.
\tag{10.1}
$$

Free polynomial sheaves are obtained by sheafifying free polynomial presheaves. Their standard resolution defines $L_{X/S}\in D(\mathcal O_X)$ just as above. This is a single global construction, so no choice of unrelated derived-category identifications on overlaps is needed.

**Proposition 10.1.** If $U=\operatorname{Spec}B\subset X$ maps into $V=\operatorname{Spec}A\subset S$, then

$$
L_{X/S}|_U\simeq\widetilde{L_{B/A}}.
\tag{10.2}
$$

Its cohomology sheaves are quasi-coherent. For $X\xrightarrow{f}Y\to S$ there is a canonical triangle

$$
\mathbf Lf^*L_{Y/S}\to L_{X/S}\to L_{X/Y}
\to(\mathbf Lf^*L_{Y/S})[1].
\tag{10.3}
$$

Smooth, étale, and lci computations have the same local forms as for rings.

**Proof.** Stalks commute with free polynomial constructions, differentials, tensor products, and normalization. At $x\in U$ corresponding to $\mathfrak p\subset B$, with image $\mathfrak q\subset A$, the sheaf model has stalk $L_{B_{\mathfrak p}/A_{\mathfrak q}}$. Localization (5.1) identifies it with $L_{B/A}\otimes_B B_{\mathfrak p}$, the stalk of the right side of (10.2). The natural comparison map is therefore a quasi-isomorphism on every stalk, proving (10.2) and quasi-coherence of cohomology.

The polynomial construction, differential sequences, and their comparison maps in Section 4 apply to sheaves of rings. They give (10.3); equivalently its affine restrictions are the already proved triangles and the globally defined maps identify their cones on every stalk. The smooth, étale, and lci claims follow by checking the respective affine opens. ∎

For a smooth $X/k$, the result is $L_{X/k}=\Omega_{X/k}[0]$, so for a quasi-coherent module $M$,

$$
\operatorname{Ext}^i_X(L_{X/k},M)
=H^i(X,\mathcal H\!om(\Omega_{X/k},M)).
\tag{10.4}
$$

Here finite local freeness of $\Omega$ removes the local higher Ext terms. Thus the familiar $H^0$ automorphisms, $H^1$ first-order deformations and $H^2$ obstructions from the earlier smooth-scheme lesson are the global groups associated with the cotangent complex.

The exact global input is the ringed-space theorem [Stacks, Tag 08UZ]. Given a square-zero thickening $S\hookrightarrow S'$ with kernel $\mathcal J$, a morphism $f:X\to S$, an $\mathcal O_X$-module $M$, and an $f^{-1}\mathcal O_S$-linear map $f^{-1}\mathcal J\to M$, there is a canonical obstruction in $\operatorname{Ext}^2_X(L_{X/S},M)$ to a thickening $X\hookrightarrow X'$ with identified kernel $M$ and compatible morphism $X'\to S'$ inducing that map. Its vanishing is necessary and sufficient; if it vanishes, isomorphism classes of solutions form a torsor under $\operatorname{Ext}^1_X(L_{X/S},M)$, and automorphisms are $\operatorname{Ext}^0_X(L_{X/S},M)$. We state this sheaf deformation theorem as an input. The ring proof in Sections 8–9 proves its affine algebra counterpart; the full global ringed-space and ringed-topos classifications require sheaf extension theory.

## 11. Exercises

**Exercise 1.** Compute $L_{A[x_1,\ldots,x_n]/A}$ and its Ext groups with an arbitrary module $M$.

**Exercise 2.** Compute $L_{k[x]/(x^2)/k}$ in every characteristic. Verify perfection and Tor amplitude, and compute its Ext groups with coefficients in $B=k[x]/(x^2)$.

**Exercise 3.** Deduce from the fundamental triangle that $L_{C/A}=L_{C/B}$ when $A\to B$ is étale. Explain why $B\to C$ need not be smooth or flat.

**Exercise 4.** Prove flat base change (3.4), identifying exactly where flatness is used. Give an ordinary base-change example in which the formula fails when flatness and Tor independence are absent.

**Exercise 5.** Prove $\operatorname{Exal}_A(B,M)=\operatorname{Ext}^1_B(L_{B/A},M)$ from the naive-complex classification and comparison. Show why the same truncation argument does not identify Ext in degree two. Compute that failure for $B=k[x]/(x^2)\to k$.

## 12. Complete solutions

**Solution 1.** Use the constant polynomial resolution. Its differential module is $\bigoplus_{i=1}^nB\,dx_i$, concentrated in degree zero, by (2.5). It is finite free, so

$$
\operatorname{Ext}^0_B(L_{B/A},M)=M^n,
\qquad \operatorname{Ext}^i_B(L_{B/A},M)=0\quad(i>0).
\tag{12.1}
$$

The degree-zero identification sends a derivation to the values it assigns to the coordinates. When $n=0$, the complex and all these groups are zero.

**Solution 2.** The polynomial presentation has regular relation $x^2$. Its conormal generator maps to $d(x^2)=2x\,dx$, so (7.4) is the full cotangent complex. Both terms are free rank one over $B$, which proves perfection. Tensoring with any $B$-module gives a two-term complex in degrees $-1,0$, proving Tor amplitude directly.

Applying $\operatorname{Hom}_B(-,B)$ gives the cochain complex

$$
B\xrightarrow{2x}B
\tag{12.2}
$$

in degrees zero and one. If $\operatorname{char}k\ne2$, its kernel is $(x)$ and its cokernel is $B/(x)$. Thus both $\operatorname{Ext}^0$ and $\operatorname{Ext}^1$ have dimension one over $k$. If $\operatorname{char}k=2$, the differential vanishes and both are $B$, of dimension two over $k$. All Ext groups in degree at least two vanish. These computations allow $H^{-1}(L)$ to be nonzero while the amplitude is still exactly within the lci range.

**Solution 3.** Proposition 5.1 gives $L_{B/A}=0$ for the étale map. In (4.2) both the first term and its shift are zero, so its middle arrow $L_{C/A}\to L_{C/B}$ is an isomorphism. This uses no condition on $B\to C$: derived tensor of a zero object remains zero for every $C$.

**Solution 4.** Resolve $B$ by polynomial $A$-algebras $P_\bullet$. Its additive normalized complex is a projective resolution. Flatness of $A'/A$ makes tensoring preserve its homology, so $P_\bullet\otimes_A A'$ resolves $B\otimes_A A'$. Polynomial differentials commute with this base change in each degree, as (3.3) shows. Normalization commutes with tensoring here because its degenerate decomposition is split. Thus the complexes computing the two sides of (3.4) agree. For the failure, use $A=\mathbb Z$ and $B=A'=\mathbb F_p$. The left side is zero, while the purported right side is $\mathbb F_p[1]$ by (7.5). Higher Tor does not vanish, so tensoring the polynomial resolution no longer resolves the ordinary tensor-product ring.

**Solution 5.** Let $K=\tau_{\leq-2}L$. The truncation triangle is (8.4). Both $\operatorname{Hom}(K,M)$ and $\operatorname{Hom}(K,M[1])$ vanish by degree orthogonality. In the long exact Hom sequence these are the groups on either side of the map $\operatorname{Ext}^1(\operatorname{NL},M)\to\operatorname{Ext}^1(L,M)$, so that map is an isomorphism. The previous lesson's extension classification then proves the desired statement, including Baer addition and identified kernels.

In degree two, $M[2]$ lies in degree $-2$, and maps from $K$ need not vanish. For the explicit example (7.6), with coefficient module $k$, the full complex is $k[1]\oplus k[2]$ whereas its naive truncation is $k[1]$. Therefore

$$
\operatorname{Ext}^2_k(L_{k/B},k)=k,
\qquad \operatorname{Ext}^2_k(\operatorname{NL}_{k/B},k)=0.
\tag{12.3}
$$

For example $\operatorname{Hom}(k[2],k[2])=k$ supplies the missing class on the left, while the category of vector spaces has no positive Ext of two degree-zero vector spaces. Thus degree-one extension classification survives truncation, but degree-two obstruction theory requires the full complex.

## 13. What this lesson does not prove

- **Simplicial foundations.** Normalization, the acyclic degenerate summand, Dold–Kan [Stacks, Tags 019D and 019G], the Kan property of simplicial groups, the boundary-lifting characterization of trivial Kan fibrations, and Eilenberg–Zilber are imported homotopical foundations. The standard polynomial resolution and the diagram-homology comparison are constructed and proved in Sections 1–2.
- **Homological change of rings.** The theorem (4.1), including its derived form for modules over weakly equivalent simplicial rings, is [Stacks, Tag 08RX]. Its normalization and derived-total-complex interpretation is the foundation used to prove that (4.5) remains a resolution. We do not import the cotangent fundamental triangle as a theorem; Section 4 proves it from this module theorem and polynomial differential sequences.
- **Derived-category algebra.** Existence of projective diagram resolutions, the two spectral sequences of a bounded-direction double complex, derived tensor–Hom adjunction, associativity of derived tensor, the cone triangle of a short exact sequence, and standard truncation orthogonality are prerequisites. A bounded-above complex of projectives computes derived tensor. These facts explain every derived tensor used here.
- **Commutative algebra.** Koszul exactness for a regular sequence, the basis of its conormal module, finite-presentation lci presentations, the étale diagonal's flat epimorphism, and local étale coordinates for a smooth morphism are imported algebraic foundations. The square-zero flatness criterion is the one used in the earlier deformation lesson: reduction flatness and injectivity of $J\otimes_A B\to B'$ imply flatness of the lift.
- **Naive extensions and sheaf deformation theory.** The complete naive-complex extension classification (8.2), with its maps and group law, was proved earlier in this course. The comparison with $L$, the general ring obstruction criterion and torsor are proved here. The more general global ringed-space extension classification is the exact statement of [Stacks, Tag 08UZ] given in Section 10; it is not deduced solely from affine calculations.
- **Quillen's spectral sequence.** As an outlook, for a surjection $A\to B$ there is a convergent spectral sequence

  $$
  E_1^{p,q}=H_{-p-q}\bigl(\mathcal D_{B/A},\operatorname{Sym}^p E\bigr)
  \Longrightarrow\operatorname{Tor}^A_{-p-q}(B,B),
  \qquad d_r:(p,q)\mapsto(p+r,q-r+1),
  \tag{13.1}
  $$

  where diagram homology means derived colimit and $E$ is (2.3); moreover $H_i(\operatorname{Sym}^p E)=0$ for $i<p$. This is [Stacks, Tag 08RF]. We state it without proof and do not use it to replace the explicit computations or lifting proofs above.

## 14. Sources and the end of the course

The cotangent-complex chapter provides the construction [Stacks, Tags 08PL–08PN], resolution comparison [Stacks, Tag 08PQ], functoriality and Tor-independent base change [Stacks, Tags 08QL and 08QQ], the fundamental triangle [Stacks, Tag 08QX], étale and smooth computations [Stacks, Tags 08R2 and 08R5], naive comparison [Stacks, Tag 08RB], complete intersections [Stacks, Tag 08SL], tensor products [Stacks, Tag 09D8], and the ring obstruction theorem [Stacks, Tag 08SP]. For schemes and ringed spaces the definitions and local comparisons are [Stacks, Tags 08UQ, 08UT, 08T1 and 08T4]. Our proofs use polynomial and simplicial models throughout, including in small positive characteristics.

The cotangent complex goes back to Illusie, who developed its construction, transitivity, infinitesimal extensions and local calculations, and later diagram cohomology and a more extensive equivariant deformation theory. Those larger theories are not prerequisites of the computations of this lesson. The precise results used here are the Stacks project tags cited above.

The course began with functors of points and representability. Grassmannians and boundedness made Hilbert and Quot functors representable; flattening kept their fibre conditions functorial. Formal deformation theory then described their completed local behaviour. Picard schemes added the distinction between a bundle and its sheaf class, and between discrete components and infinitesimal structure. The cotangent complex supplies the common derived mechanism: extensions in degree one, lifting obstructions in degree two, and a fundamental triangle that preserves the relations a two-term presentation can forget.
