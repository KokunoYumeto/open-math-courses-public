# The cotangent complex

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

The naive cotangent complex records generators and first relations. It classifies square-zero extensions, but it can discard relations among relations. The full cotangent complex retains those additional degrees. Its fundamental triangle then turns a lifting problem into a connecting class in an Ext group.

We construct it from polynomial simplicial resolutions, prove independence and functoriality, prove the fundamental triangle and its basic consequences, and derive the extension and obstruction theorems. A computation for the map from the dual numbers to their residue field exhibits a genuine degree $-2$ term. For quotient rings we also construct Quillen's augmentation filtration, prove its connectivity bounds in every characteristic and prove convergence to the self-intersection Tor groups. The global extension and obstruction classifications are proved on ringed sites, with scheme thickenings for quasi-coherent kernels.

## 1. Simplicial algebra and the standard resolution

A simplicial module $E_\bullet$ has face maps $d_i:E_n\to E_{n-1}$ and degeneracy maps $s_i:E_n\to E_{n+1}$ satisfying the simplicial identities. Its unnormalized chain complex has differential

$$
\partial_n=\sum_{i=0}^n(-1)^i d_i.
\tag{1.1}
$$

The degenerate subcomplex is generated in degree $n$ by the images of $s_0,\ldots,s_{n-1}$. The normalized complex is the quotient by this subcomplex. It is also a direct summand of the unnormalized complex, with the same homology. For a bisimplicial module, the complex of the diagonal is naturally quasi-isomorphic to the total complex of its two normalized directions. Theorems 1.1–1.3 below prove the normalization, Dold–Kan and Eilenberg–Zilber statements over arbitrary coefficient rings [compare Stacks, Tags 019D and 019G]. We do not identify simplicial rings with ordinary differential graded rings; that replacement needs additional care in positive characteristic.

### Normalization and the inverse construction

We give the algebraic foundations over an arbitrary coefficient ring \(R\). For a simplicial \(R\)-module \(V\), use the Moore model

\[
N_nV=\bigcap_{i=1}^n\ker d_i,\qquad d_N=d_0.
\]

Its differential squares to zero, since \(d_0d_0=d_0d_1\). Write \(D_nV=\sum_{j=0}^{n-1}s_jV_{n-1}\) for the degenerate terms.

**Theorem 1.1 (exact normalization).** The unnormalized complex is the direct sum of the Moore complex and its degenerate subcomplex. The latter is acyclic. Thus the quotient model, Moore model and unnormalized model have the same homology. Normalization is exact and commutes with change of coefficient ring.

**Proof.** Starting with \(v\in V_n\), for \(i=n,n-1,\ldots,1\) replace it by \(v-s_{i-1}d_iv\). The step kills its \(i\)-th face. It preserves every already zero higher face: for \(j>i\),
\(d_js_{i-1}d_i=s_{i-1}d_{j-1}d_i=s_{i-1}d_id_j\).
The resulting natural projection is

\[
\pi_n=(1-s_0d_1)(1-s_1d_2)\cdots(1-s_{n-1}d_n).
\]

It fixes \(N_nV\), and \(v-\pi_nv\) is degenerate. It kills each \(s_j\). Indeed for \(i>j+1\) the \(i\)-th factor moves past \(s_j\) as
\((1-s_{i-1}d_i)s_j=s_j(1-s_{i-2}d_{i-1})\); the next factor is \(1-s_jd_{j+1}\), which kills \(s_j\). Hence \(V_n=N_nV\oplus D_nV\). In the alternating boundary of \(s_jv\), the two identity terms cancel, and every other term is a degeneracy. Thus \(D\) is a subcomplex; on its complement the differential is \(d_0\). This proves the chain decomposition and the quotient identification.

For acyclicity, filter \(D\) increasingly by the subcomplexes
\(D^{(r)}_n=\sum_{j\leq r}s_jV_{n-1}\), with nonexistent degeneracies omitted. On \(D^{(r)}/D^{(r-1)}\), the operator \((-1)^rs_r\) is a contracting homotopy. To verify it, expand the alternating boundary:

\[
\partial s_r+s_r\partial
=\sum_{i<r}(-1)^i s_{r-1}d_i
 +\sum_{i\leq r}(-1)^i s_rd_i.
\]

The first sum is an earlier degeneracy. On \(s_rv\), the terms of the second sum with \(i<r\) are earlier degeneracies too, using \(s_rs_{r-1}=s_{r-1}s_{r-1}\); its \(i=r\) term is \((-1)^rs_rv\). The operator respects the earlier-degeneracy submodule, so gives the asserted contraction. Every finite filtration stage is therefore acyclic by its long exact sequence. Their exact filtered union is \(D\), proving acyclicity.

Exactness of normalization follows from the natural projection: to lift a normalized element across a surjection, lift it in \(V_n\) and apply \(\pi_n\). Kernels are computed in the same way. The displayed idempotents are split and use only integer linear combinations of faces and degeneracies. Their images therefore commute with arbitrary tensor change of the coefficient ring. \(\square\)

**Theorem 1.2 (Dold–Kan).** Normalization is an equivalence from simplicial \(R\)-modules to nonnegative chain complexes. Its inverse has terms

\[
\Gamma(C)_n=
\bigoplus_{\eta:[n]\twoheadrightarrow[k]}C_k.
\]

The sum is over order-preserving surjections. No projectivity or finiteness hypothesis on the modules is required.

**Proof.** Define degeneracies on a summand by composing its surjection with the corresponding degeneracy surjection. For a face, delete that vertex of the domain and inspect the image of the resulting map into \([k]\). If it is still surjective, carry the element unchanged to that summand. If the deletion removes the unique occurrence of \(0\), apply \(d_C:C_k\to C_{k-1}\) and relabel the remaining image in order. If it removes a positive value, send the element to zero. These rules define all operators.

They satisfy the simplicial identities. Compositions of degeneracies are just compositions of surjections. In a mixed face–degeneracy identity, deleting one of the two copies of a duplicated vertex gives the identity; all other cases give the same relabelled map. For two faces, the two orders of deletion have the same image. If no image value disappears, both carry the element unchanged. If just the initial value disappears, both apply \(d_C\); disappearance of a positive value makes both zero. The remaining case deletes the initial two values: one order gives \(d_C^2\), while the order which first removes a positive value gives zero. They agree because \(d_C^2=0\). This checks every generator relation.

The identity-surjection summand \(C_n\) has all its positive faces zero and first face \(d_C\). Every other summand is degenerate. The projection of Theorem 1.1 therefore identifies \(N\Gamma C=C\), with exactly its differential.

For a simplicial module \(V\), the natural comparison is

\[
\bigoplus_{\eta:[n]\twoheadrightarrow[k]}N_kV
\longrightarrow V_n,\qquad
(v_\eta)\longmapsto\sum_\eta\eta^*v_\eta.
\]

It is onto by the normalization projection and induction on \(n\): subtract the normalized part, express the remainder by degeneracies, and decompose their lower-dimensional arguments. We check uniqueness over arbitrary rings. For a surjection \(\eta\), let \(e_j\) be the last index in its \(j\)-th fibre and let \(\delta_\eta:[k]\to[n]\) choose these indices. Apply \(\pi_k\delta_\eta^*\) to the comparison. A term from a dimension \(l<k\) is killed because its resulting map factors through a proper degeneracy in dimension \(k\). For terms of dimension \(k\), its coefficient is the identity precisely when \(\eta'\delta_\eta=1\), and is zero otherwise: a nonsurjective self-map factors through a proper degeneracy, which \(\pi_k\) kills. The identity condition forces the fibre-end indices of \(\eta'\) to be at least the corresponding \(e_j\). The diagonal condition \(\eta'=\eta\) always holds. Thus, ordering the finite set of end-index vectors lexicographically, this block is unit triangular. First subtract the higher-dimensional components; then solve these triangular blocks in decreasing dimension. This gives unique components, without dividing by a coefficient.

The comparison is therefore an isomorphism. Its compatibility with faces is exactly the rule above: a positive face kills a normalized component, and the initial face is its differential. Compatibility with degeneracies is composition. It is a simplicial isomorphism \(\Gamma NV\simeq V\). Together with \(N\Gamma C=C\), it proves the equivalence and its naturality. \(\square\)

### Alexander–Whitney and shuffle maps

**Theorem 1.3 (Eilenberg–Zilber).** For simplicial modules \(V,W\), there are natural chain homotopy equivalences

\[
N(V\otimes_R W)\simeq
\operatorname{Tot}(NV\otimes_R NW).
\]

More generally, normalization of the diagonal of a bisimplicial module is naturally chain homotopy equivalent to the total complex of its two normalizations. All these constructions work over every ring.

**Proof.** For a tensor in degree \(n\), the Alexander–Whitney map is

\[
\begin{gathered}
\operatorname{AW}_n(v\otimes w)\\
=\sum_{p+q=n}
(d_{p+1}\cdots d_nv)\otimes(d_0^p w).
\end{gathered}
\]

It takes the front \(p\)-face of the first factor and the back \(q\)-face of the second. The inverse comparison is the shuffle map. Partition \(\{0,\ldots,p+q-1\}\) into increasing lists \(\mu\) of length \(p\) and \(\nu\) of length \(q\). With \(\epsilon\) the sign of this shuffle, put

\[
\begin{gathered}
\operatorname{sh}(v\otimes w)=\\
\sum_{(\mu,\nu)}(-1)^\epsilon
\bigl(s_{\nu_q}\cdots s_{\nu_1}v\bigr)
\otimes\bigl(s_{\mu_p}\cdots s_{\mu_1}w\bigr).
\end{gathered}
\]

Empty strings of operators are identities. Both formulas descend through degenerate terms. In Alexander–Whitney, a diagonal degeneracy appears in at least one of the two faces at each cut. In a shuffle, a degeneracy already present in an input can be moved to the common diagonal after pairing the shuffles which cross that repetition; their signs cancel when necessary.

Here are the boundary checks. In Alexander–Whitney, deleting a vertex inside a front or back face gives the corresponding differential of that factor. The terms deleting the shared cut vertex occur at consecutive cuts with opposite signs and cancel. The differential on the back factor has sign \((-1)^p\), which is exactly the tensor differential. For a shuffle, a deleted repeated vertex either removes a degeneracy and gives a term of the input differential, or lies at a crossing of the two lists. Crossing terms pair by exchanging their two neighbouring entries, which reverses the shuffle sign. The unpaired terms have respectively the first-factor sign and \((-1)^p\) times the second-factor sign. Thus both formulas are chain maps, including over rings in which two is zero.

We supply the homotopies as well. A useful elementary construction is the following. Suppose a nonnegative complex of additive functors has each degree a retract of a direct sum of evaluation functors on free simplicial models. Suppose a target complex on those models is augmented to \(R\) and has a contraction in positive degrees. Two natural chain maps agreeing on the augmentation are naturally homotopic. To construct the homotopy in degree \(n\), after degrees below \(n\) have been constructed, form the residual map

\[
r_n=f_n-g_n-h_{n-1}d.
\]

The chain-map equations and the previous homotopy equation give \(d r_n=0\). In degree zero its augmentation is zero. Evaluate on each free model and apply its contraction to obtain a preimage under \(d\). Extend by the universal evaluation map and then restrict to the degree's retract. This defines \(h_n\) naturally and gives \(d h_n=r_n\). Induction proves \(f-g=dh+hd\). This is an explicit recursive construction, not an assumption about arbitrary complexes of functors.

For the tensor comparison, the free models are pairs \((R[\Delta[a]],R[\Delta[b]])\). An element of a simplicial module in degree \(a\) is exactly a module map from \(R[\Delta[a]]\), so a tensor in two evaluation degrees has the required universal bilinear evaluation property. Normalized terms are retracts of these evaluation terms by Theorem 1.1. On a model the diagonal is \(R[\Delta[a]\times\Delta[b]]\). Its normalized complex is contracted to its initial vertex: prepend \((0,0)\) to a simplex. The extra-face identities give \(dh+hd=1-\iota\varepsilon\). This operation takes degenerate simplices to degenerate simplices and thus works on normalization. The total complex on that model is the tensor of the two simplex chain complexes; their vertex contractions, with the tensor differential signs, contract it to \(R\) too. Both comparison composites induce the identity on that augmentation. The recursive construction therefore makes them homotopic to the identity.

For a general bisimplicial module, use free rectangular models \(R[\Delta[a]]\boxtimes R[\Delta[b]]\). In Alexander–Whitney use the front horizontal face and back vertical face; in the shuffle use the horizontal and vertical degeneracies in the displayed orders. The same boundary cancellations apply because the two directions commute. Evaluation in a bidegree is represented by a rectangular model, and normalized or total-normalized terms are its finite direct-sum retracts. On each rectangular model the diagonal and total contractions are exactly the ones just given. The same induction produces both homotopies. Each total degree has only finitely many bidegrees, so no infinite-totalization assertion enters this proof. \(\square\)

This also proves the homotopy assertion used with Dold–Kan. If \(f-g=dh+hd\) for chain maps \(C\to D\), define a chain map on \(C\otimes N(R[\Delta[1]])\) by using \(g,f\) on the two vertices and \((-1)^n h\) on a degree-\(n\) element tensored with the edge. The boundary of the edge is \([1]-[0]\), so the chain-map equation is precisely \(f-g=dh+hd\). Precompose with Alexander–Whitney and apply the Dold–Kan equivalence. This gives a simplicial linear homotopy \(\Gamma C\otimes R[\Delta[1]]\to\Gamma D\), with endpoints \(\Gamma g,\Gamma f\). In particular the cone of an identity has a simplicial linear contraction.

For a simplicial algebra, compose the shuffle map with multiplication to obtain its normalized product. Shuffling three ordered lists identifies the two associative products term by term; moving a list of length \(p\) past one of length \(q\) supplies the sign \((-1)^{pq}\). The boundary calculation above is the Leibniz rule. These identities justify the normalized products and signs in the cotangent and Quillen constructions.

All normalization, inverse-construction and comparison identities use universal finite sums, signs, faces and degeneracies. They therefore also give exact normalization, Dold–Kan and the Alexander–Whitney/shuffle comparisons for sheaves of modules on any ringed site, without a hypothesis that the site has enough points.

### Horn filling for additive resolutions

**Proposition 1.4 (simplicial groups and normalized homotopy).** Every simplicial group is Kan. For a simplicial abelian group, its homotopy groups at zero are the homology groups of its Moore normalization, including degree zero.

**Proof.** First write the group law multiplicatively. A horn prescribes faces \(a_i\), \(i\ne k\), satisfying \(d_i a_j=d_{j-1}a_i\) for \(i<j\). Begin with the identity element \(x\) in degree \(n\). For \(i=0,\ldots,k-1\), replace

\[
x\longmapsto s_i\bigl(a_i(d_ix)^{-1}\bigr)x.
\]

This fixes its \(i\)-th face and preserves all already fixed lower faces: the corresponding faces of the correction are the identity by the compatibility equations. Next, for \(i=n,n-1,\ldots,k+1\), replace

\[
x\longmapsto s_{i-1}\bigl(a_i(d_ix)^{-1}\bigr)x.
\]

It fixes its \(i\)-th face and preserves the already fixed higher faces. It also preserves every face below \(k\), since their correction faces are the identity by the same compatibility equation. The final element fills the horn. This uses the order of multiplication displayed, so proves the assertion for nonabelian groups too.

Now write the abelian law additively. An \(n\)-cycle in the face definition of \(\pi_n\) is a simplex \(z\) with all faces zero. It is exactly a cycle of \(NV\). An equivalent adjacent-face presentation of based homotopy uses an \((n+1)\)-simplex \(u\) with \(d_0u=z\), \(d_1u=z'\) and all higher faces zero: the prism comparison in Simplicial sets, nerves and Kan complexes, Lemma 5.3b moves this adjacent pair to the defining final pair. Subtract \(s_0z'\). The result is in \(N_{n+1}V\) and its first face is \(z-z'\). Conversely a normalized element with that first face, plus \(s_0z'\), supplies exactly this homotopy. Hence the equivalence relation is quotient by normalized boundaries. The simplex \(s_{n-1}z'+s_nz\) has final three faces \(z',z'+z,z\) and all earlier faces zero, so the defining horn product is addition. In degree zero, components are the quotient by \(d_0-d_1\), which is the degree-zero Moore homology. This proves the claimed identifications.

In particular an augmentation to a constant abelian group, surjective in degree zero and an isomorphism on normalized homology, has nonempty acyclic Kan fibres. Each fibre is a translate of the kernel, whose normalization is acyclic by exactness. The boundary-filling result Simplicial sets, nerves and Kan complexes, Lemma 5.3c then shows that it lifts every boundary over that constant target. This is the trivial Kan fibration criterion used for polynomial resolutions. \(\square\)


Let $A\to B$ be a ring map. All rings in this lesson are commutative. Let $F$ send a set $E$ to the polynomial $A$-algebra $A[E]$, and let $U$ forget an $A$-algebra to its set. The composite $G=FU$ is a comonad. Its counit evaluates a variable at the element labelling it, and its comultiplication replaces a label by the variable with that label. Define

$$
\begin{gathered}
P_n=G^{n+1}B,
\\
 P_0=A[B],\quad P_1=A[A[B]],\quad\ldots.
\end{gathered}
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
\begin{gathered}
\Omega_{(P_n\otimes_A A')/A'}\otimes_{P_n\otimes_A A'}B'
\\
=\Omega_{P_n/A}\otimes_{P_n}B'.
\end{gathered}
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

For a quasi-isomorphism \(R_\bullet\to R'_\bullet\) of simplicial rings and a degreewise flat simplicial \(R_\bullet\)-module \(M_\bullet\), homological change of rings is the assertion that

$$
M_\bullet\longrightarrow
M_\bullet\otimes_{R_\bullet}R'_\bullet
\tag{4.1}
$$

induces a quasi-isomorphism on associated additive complexes. We prove this assertion and its arbitrary-complex derived version before using them to construct the cotangent triangle.

### Change of simplicial rings

For a simplicial ring \(R_\bullet\) and a simplicial set \(T\), write
\[
R[T]_n=\bigoplus_{t\in T_n}R_n.
\]
The structure maps act on the coefficient and its label together. This is the free simplicial \(R\)-module on \(T\). All the complexes in the following first argument have nonnegative homological degrees.

**Lemma 4.A (flat simplicial change of rings).** If \(R\to R'\) is a quasi-isomorphism on normalized additive complexes, then (4.1) is a quasi-isomorphism for every simplicial \(R\)-module \(M\) with each \(M_n\) flat over \(R_n\). No flatness of \(R'_n/R_n\), or of either ring over \(\mathbb Z\), is required.

**Proof.** First take \(M=R[T]\). As a simplicial abelian group it is the diagonal tensor \(R\otimes_{\mathbb Z}\mathbb Z[T]\). Theorem 1.3 identifies its normalization, up to natural chain homotopy, with
\[
\operatorname{Tot}\bigl(NR\otimes_{\mathbb Z}N\mathbb Z[T]\bigr).
\]
Every term of \(N\mathbb Z[T]\) is a direct summand of a free abelian group and hence projective. Tensoring with this nonnegative complex preserves quasi-isomorphisms: filter its direct-sum total complex by chain degree; each graded piece is a shift of tensoring with one flat module. Finite stages preserve acyclicity, and their increasing union does too because filtered colimits of modules are exact. Apply this to the cone of \(NR\to NR'\). Thus \(R[T]\to R'[T]\) is a quasi-isomorphism.

Resolve \(M\), in the category of simplicial \(R\)-modules, by successive free modules on underlying simplicial sets. More explicitly, put \(F_0=R[UM]\), with evaluation \(F_0\twoheadrightarrow M\). Put \(K_0=M\), \(K_{q+1}=\ker(F_q\to K_q)\), and \(F_{q+1}=R[UK_{q+1}]\). These maps form an exact augmented complex
\[
\cdots\longrightarrow F_2\longrightarrow F_1
\longrightarrow F_0\longrightarrow M\longrightarrow0
\]
of simplicial modules; in every simplicial degree it is a free resolution. Its kernels are flat in that degree. Indeed, in \(0\to K\to F\to V\to0\) with \(F,V\) flat, tensoring with any module remains exact and \(K\) is flat: a free resolution of that module gives \(\operatorname{Tor}_1(-,V)=\operatorname{Tor}_2(-,V)=0\), and the long exact sequence gives both assertions. Induction starts from the assumed flatness of \(M_n\). Consequently tensoring this whole augmented resolution with \(R'_n\) is exact.

Normalize in the simplicial direction and totalize with the free-resolution direction. Exactness of normalization and the first-quadrant filtration show that the first total complex maps quasi-isomorphically to \(NM\), and its base-changed total complex to \(N(M\otimes_RR')\). For clarity, the filtration argument has only finitely many summands in each total degree: its successive homology first computes the exact augmented free resolution, leaving precisely the claimed augmentation. Each column map \(NF_q\to N(F_q\otimes_RR')\) is a quasi-isomorphism by the free case. The other first-quadrant filtration therefore makes their total map a quasi-isomorphism. These three comparisons prove (4.1). Every construction used all element labels and is natural. \(\square\)

The arbitrary-complex version has a precise interpretation in the derived category of module diagrams. We give that version as well, including the category-homology formulation of [Stacks, Tag 08RX](https://stacks.math.columbia.edu/tag/08RX).

Let \(\mathcal C\) be a small category, and let \(\mathcal R:\mathcal C\to\mathrm{CRing}\) be a covariant ring diagram. An \(\mathcal R\)-module diagram \(E\) has an \(\mathcal R(V)\)-module \(E(V)\) at each object, with compatible semilinear transition maps. Kernels, cokernels, direct sums and filtered colimits are computed objectwise. Denote by \(\mathbb H_{\mathcal C}(K)\) the derived colimit of the underlying abelian-group complex of a module-diagram complex \(K\). Total complexes here and below use direct sums, including for unbounded \(K\).

**Theorem 4.B (derived diagram change of rings).** Suppose there is a simplicial object \(U_\bullet\) of \(\mathcal C\) such that, for every \(V\), the augmented normalized integral chain complex of
\[
T_V=\operatorname{Hom}_{\mathcal C}(V,U_\bullet)
\]
resolves \(\mathbb Z\). In particular this holds if each \(T_V\) is contractible. Let \(\mathcal R\to\mathcal R'\) be a map of ring diagrams such that
\[
N\mathcal R(U_\bullet)\longrightarrow
N\mathcal R'(U_\bullet)
\]
is a quasi-isomorphism. For every complex \(K\) of \(\mathcal R\)-module diagrams, without boundedness assumptions, the natural map gives an isomorphism
\[
\mathbb H_{\mathcal C}(K)\ \xrightarrow{\ \sim\ }
\mathbb H_{\mathcal C}
 \bigl(K\otimes_{\mathcal R}^{\mathbf L}\mathcal R'\bigr).
\tag{4.1a}
\]
These functors and the map are defined on derived categories. In particular they do not depend on a chosen free resolution.

**Proof.** We first describe derived colimit in a form valid for unbounded complexes. A right integral \(\mathcal C\)-module is a contravariant abelian-group diagram. Its tensor with a covariant diagram \(E\) is the quotient of \(\bigoplus_V H(V)\otimes_{\mathbb Z}E(V)\) by the transition relations
\[
\begin{gathered}
H(\alpha)(h)\otimes e=h\otimes E(\alpha)(e),\\
\alpha:V\to W,\quad h\in H(W).
\end{gathered}
\]
Tensor with the constant right module \(\mathbb Z\) is exactly colimit. The right modules \(\mathbb Z[\operatorname{Hom}(-,W)]\) are projective by the Yoneda lemma, since maps from one into a right module evaluate that module at \(W\). Tensoring with one evaluates \(E\) at \(W\). The simplicial right module
\[
V\longmapsto\mathbb Z[T_V]
\]
has such a representable in each degree. Its normalized complex \(H_\bullet\) has projective terms, by the split normalization projection, and by hypothesis resolves the constant right module \(\mathbb Z\).

A nonnegative complex of flat right modules is tensor-flat as a complex: the finite-stage and exact-union argument in Lemma 4.A proves that tensoring it with any acyclic covariant complex gives an acyclic total complex. Thus this resolution computes the derived tensor with \(\mathbb Z\), even for unbounded \(E\). The tensor-evaluation identity and the split normalization give the concrete formula
\[
\begin{gathered}
\mathbb H_{\mathcal C}(E)
=H_\bullet\otimes_{\mathcal C}E\\
=\operatorname{Tot}N\bigl(E(U_\bullet)\bigr).
\end{gathered}
\tag{4.1b}
\]
For a complex \(E\), the last expression has both its internal and its simplicial degree. The formula proves exactness as a derived functor and preservation of direct sums. It also shows directly that it sends an objectwise quasi-isomorphism of complexes to a quasi-isomorphism. This proves the needed unbounded interpretation of the diagram comparison; no unbounded spectral sequence is being asserted to converge.

The free evaluation generators in \(\mathcal R\)-module diagrams are
\[
G_V(W)=\bigoplus_{\alpha:V\to W}\mathcal R(W).
\]
A module-diagram map from \(G_V\) to \(E\) is specified uniquely by the image of the identity-labelled generator, an arbitrary element of \(E(V)\). Hence \(G_V\) is projective, these objects generate, and each is objectwise free and therefore tensor-flat. Base change sends it to the corresponding \(G'_V\).

By (4.1b), \(\mathbb H_{\mathcal C}(G_V)\) is the normalization of \(\mathcal R(U_\bullet)[T_V]\). Theorem 1.3 compares this with the total tensor of \(N\mathcal R(U_\bullet)\) and \(N\mathbb Z[T_V]\). The latter augmented complex is a projective resolution of \(\mathbb Z\) over \(\mathbb Z\), so its augmentation is a chain homotopy equivalence. To check this last assertion, split its degree-zero surjection onto \(\mathbb Z\); its kernel is projective. Then split the surjection in the next degree onto that kernel, and continue. These splittings contract the augmented kernel. They remain contractions after tensoring with any complex. It follows that
\[
\mathbb H_{\mathcal C}(G_V)\simeq N\mathcal R(U_\bullet),
\qquad
\mathbb H_{\mathcal C}(G'_V)\simeq N\mathcal R'(U_\bullet).
\]
The augmentations and the shuffle comparison commute with the ring map. Our hypothesis therefore proves (4.1a) for every free generator and every shift or direct sum of such generators.

Here are the resolution and passage to an arbitrary unbounded \(K\). Starting with \(Q_0=0\to K\), construct \(Q_{j+1}\) from \(Q_j\) by adjoining shifted copies of \(G_V\), one for every cycle in the mapping cone at every object and every integer degree. If such a cycle is \((k,q)\in K^n(V)\oplus Q_j^{n+1}(V)\), the conditions are \(d q=0\) and \(d k+f(q)=0\). Adjoin a degree-\(n\) generator \(e\) with \(de=q\) and \(f(e)=-k\); extend these prescriptions by the evaluation property. The cycle is then a boundary in the new cone, up to the harmless overall sign dictated by this cone convention. This gives a complex and a compatible map because \(d^2e=0\) and \(df(e)=f(de)\). In each chain degree the inclusion \(Q_j\subset Q_{j+1}\) splits as a module diagram, and its quotient is a direct sum of shifts of the \(G_V\), with zero differential.

Put \(Q=\operatorname{colim}_jQ_j\). Every cone cycle appears at a finite stage and is killed at the next one. Filtered colimits are exact objectwise, so \(Q\to K\) is a quasi-isomorphism. The filtration also proves that \(Q\) is tensor-flat as a complex: for any acyclic module-diagram complex, tensor the degreewise split filtration, use flatness of its shifted free quotients, and take the exact union. Thus \(Q\otimes_{\mathcal R}\mathcal R'\) computes the derived tensor in (4.1a).

Apply the two sides of (4.1a) to this filtration. At stage zero their comparison is an isomorphism. Its quotient comparison at each next stage is a direct sum of shifts of the free-generator comparisons already proved, so the exact triangle for that stage proves the next comparison. Finally both functors commute with the direct-sum telescope of the \(Q_j\). The telescope computes their union: the sequence with map \(1-\mathrm{shift}\) from \(\bigoplus_jQ_j\) to itself is degreewise injective and has cokernel \(Q\). Hence its cone maps quasi-isomorphically to \(Q\). Taking the telescope of the stagewise isomorphisms proves (4.1a) for \(K\). This also proves independence and naturality of the resolution calculation. \(\square\)

Take \(\mathcal C=\Delta^{\mathrm{op}}\) and \(U_\bullet\) the identity simplicial object. Then \(T_{[m]}=\Delta[m]\); contraction to its initial vertex makes it contractible. Formula (4.1b) is normalized realization. Theorem 4.B consequently gives precisely the derived change-of-simplicial-rings statement for arbitrary complexes of simplicial modules. For an ordinary simplicial module which is degreewise flat, derived extension is ordinary degreewise tensor, recovering Lemma 4.A and (4.1). For the polynomial-algebra category in Section 2, the contractible map sets in (2.2) provide the same category-homology hypothesis. These are module-theoretic statements, obtained before and independently of the cotangent triangle.


**Theorem 4.1.** For ring maps $A\to B\to C$, there is a canonical distinguished triangle

$$
\begin{gathered}
L_{B/A}\otimes_B^{\mathbf L}C
\longrightarrow L_{C/A}
\longrightarrow L_{C/B}
\\
\longrightarrow
\bigl(L_{B/A}\otimes_B^{\mathbf L}C\bigr)[1].
\end{gathered}
\tag{4.2}
$$

**Proof.** We first prove a special case and a product statement to avoid using localization consequences circularly.

If $B$ is polynomial over $A$, choose a polynomial resolution $Q_\bullet\to C$ over $B$. Every $Q_n$ is polynomial over $A$ too. The polynomial differential sequence is split exact in each degree:

$$
\begin{gathered}
0\to\Omega_{B/A}\otimes_B C
\to\Omega_{Q_n/A}\otimes_{Q_n}C
\\
\to\Omega_{Q_n/B}\otimes_{Q_n}C\to0.
\end{gathered}
\tag{4.3}
$$

The first term is a constant simplicial module. Normalization is exact, and Lemma 2.1 identifies the other two complexes with $L_{C/A}$ and $L_{C/B}$. The first is $L_{B/A}\otimes_B^{\mathbf L}C$ by (2.5). This proves (4.2) when its middle ring is polynomial.

Next, for two $A$-algebras $C_1,C_2$, there is a canonical isomorphism

$$
\begin{gathered}
L_{(C_1\times C_2)/A}\\
\simeq L_{C_1/A}\oplus L_{C_2/A}
\\
\text{in }D(C_1\times C_2).
\end{gathered}
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
\begin{gathered}
0\to\Omega_{P_n/A}\otimes_{P_n}C
\to\Omega_{Q_n/A}\otimes_{Q_n}C
\\
\to\Omega_{\overline Q_n/B}\otimes_{\overline Q_n}C\to0.
\end{gathered}
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
\begin{gathered}
L_{D/A}\simeq
\bigl(L_{B/A}\otimes_B^{\mathbf L}D\bigr)
\\
\oplus
\bigl(L_{C/A}\otimes_C^{\mathbf L}D\bigr).
\end{gathered}
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
\begin{gathered}
P_1=P[x_f\mid f\in I],\\
 d_0x_f=f,
\quad d_1x_f=0,
\end{gathered}
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

We use finite local complete intersections: locally on the target a finite-presentation map admits a presentation by a localized polynomial algebra whose kernel is generated by a finite Koszul-regular sequence. A regular sequence is sufficient. No flatness of the map itself is assumed. The following argument proves independence of the polynomial presentation and the Koszul and conormal facts used in the computations.

### Koszul equations and a change of presentation

The elementary Koszul facts needed here hold over every ring. For a regular sequence, its Koszul complex resolves the quotient: adjoining the last equation is the mapping cone of its multiplication on the preceding complex. By induction the latter has only degree-zero homology, and injectivity of the last equation on that quotient gives the assertion.

Suppose more generally that the Koszul complex on \(f_1,\ldots,f_r\) has no positive homology, and put \(I=(f_1,\ldots,f_r)\), \(B=R/I\). The natural surjection
\[
B^r\longrightarrow I/I^2,\qquad e_i\longmapsto f_i
\]
is an isomorphism. Indeed, if \(\sum c_if_i\in I^2\), subtract from the vector \((c_i)\) a vector with entries in \(I\) having the same product with \((f_i)\). The remaining vector is a degree-one Koszul cycle. It is a Koszul boundary, whose entries are all in \(I\). Thus every original \(c_i\) is in \(I\), proving injectivity.

We also justify the presentation independence used in the definition. It is a local assertion at a point of \(\operatorname{Spec}B\). Consider two localized polynomial presentations \(P\to B\) and \(Q\to B\) over \(A\), with variables \(x_1,\ldots,x_m\) and \(y_1,\ldots,y_n\), and kernels \(I,J\). Suppose \(I\) is generated by a finite Koszul-regular sequence \(f_1,\ldots,f_r\). Localize at the chosen point and its inverse images. Lift the images of the \(y_j\) to \(g_j(x)\in P\), and the images of the \(x_i\) to \(h_i(y)\in Q\). Take the common local polynomial ring
\[
R=A[x_1,\ldots,x_m,y_1,\ldots,y_n]_{\mathfrak p},
\]
where \(\mathfrak p\) is the inverse image of the chosen prime of \(B\); the presentation denominators are inverted in this local ring. Evaluation of \(y\) at \(g(x)\) gives \(R\to P\), and evaluation of \(x\) at \(h(y)\) gives \(R\to Q\). These maps are well defined: an element outside \(\mathfrak p\) has image outside the corresponding local prime, as detected in \(B\).

Let \(K=\ker(R\to B)\). It is generated by
\[
f_1(x),\ldots,f_r(x),\quad
y_1-g_1(x),\ldots,y_n-g_n(x).
\]
This sequence is Koszul regular. Polynomial extension and localization preserve the exact Koszul resolution on the \(f_i\); on its quotient the remaining equations eliminate independent polynomial variables one at a time, and are a regular sequence. The mapping-cone argument proves the combined exactness. Consequently \(K/K^2\) is free over the local ring \(B\), of rank \(r+n\), by the conormal calculation just given.

Put \(q_i=x_i-h_i(y)\). Then \(R/(q_1,\ldots,q_m)=Q\), and \(K=JR+(q_1,\ldots,q_m)\). Relative differentiation over \(Q\) gives a split surjection
\[
K/K^2\longrightarrow
\Omega_{R/Q}\otimes_RB=B^m,\qquad
[q_i]\longmapsto dx_i.
\]
The kernel is generated by the classes of elements of \(J\). To check this directly, express an element of \(K\) as a sum of a member of \(JR\) and \(\sum a_iq_i\). Its derivative is \(\sum\bar a_i dx_i\). If that derivative is zero, all \(a_i\) are in \(K\), and the latter sum is zero in \(K/K^2\).

The kernel of this split map is a finite projective module over the local ring \(B\), hence free. Choose \(b_1,\ldots,b_s\in J\) whose classes form its basis. Then \(q_1,\ldots,q_m,b_1,\ldots,b_s\) form a basis of \(K/K^2\), and \(m+s=r+n\). They generate \(K\) itself by Nakayama: \(K\) is finitely generated, \(K\) lies in the maximal ideal of \(R\), and generation modulo \(K^2\) suffices. The matrix expressing these generators in the preceding generators of \(K\) is invertible modulo \(K\), and hence invertible in \(R\). An invertible change of generators induces an isomorphism on their Koszul complexes, through the induced exterior-power maps. Thus the Koszul complex on \(q,b\) is exact in positive degrees.

Finally \(q_1,\ldots,q_m\) is a regular sequence in \(R\), eliminating the \(x\)-variables, and its Koszul complex resolves \(Q\). Tensor this resolution with the bounded free Koszul complex on the \(b_j\). It gives a quasi-isomorphism
\[
K_R(q,b)\longrightarrow K_Q(b).
\]
It follows that \(b_1,\ldots,b_s\) is Koszul regular in \(Q\). Projecting \(K=(q,b)\) to \(Q\) also gives \(J=(b_1,\ldots,b_s)\). All chosen generators, identities and invertible matrices involve only finitely many elements and localization denominators, so this local argument holds on neighbourhoods of the chosen point. Exchanging the two presentations proves independence. No Noetherian or flatness hypothesis on \(A\to B\) was used.

**Lemma 7.1.** If $R\to B=R/(f_1,\ldots,f_r)$ and the sequence is Koszul regular, then

$$
\begin{gathered}
L_{B/R}\simeq (I/I^2)[1],\\
 I=(f_1,\ldots,f_r).
\end{gathered}
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

### Quillen's filtration and its convergence

For a quotient ring, the cotangent complex controls an entire filtration of the derived self-intersection. Symmetric powers appear in its associated graded. These are symmetric powers of simplicial modules, so their homology retains the characteristic-dependent relations that an ordinary graded symmetric algebra can miss.

We use homological degrees for normalized simplicial modules in this subsection. Thus \(H_i(L_{B/A})\) here means the earlier \(H^{-i}(L_{B/A})\). A complex is **\(a\)-connective** if its homology is zero below degree \(a\).

**Lemma 7.3 (symmetric-power connectivity).** Let \(F\) be a simplicial module over any commutative ring \(B\). Suppose every \(F_n\) is projective and \(H_0(NF)=0\). Then, for every \(p\geq1\),

\[
H_i(N\operatorname{Sym}_B^p F)=0\qquad(i<p).
\tag{7.8}
\]

**Proof.** Normalization splits off the degenerate terms, so \(NF\) is a nonnegative complex of projectives. Its differential \((NF)_1\to(NF)_0\) is surjective. Split this surjection. The image of the preceding differential from degree two lies in its kernel. Thus the complex is the direct sum of a positive complex of projectives \(C\), with \(C_0=0\), and a two-term contractible complex. Under Dold–Kan this gives a simplicial linear homotopy equivalence \(F\simeq\Gamma C\). Applying any functor to the maps and operators of a simplicial homotopy preserves their identities, since those identities use composition. In particular symmetric powers preserve this homotopy equivalence. We may replace \(F\) by \(\Gamma C\).

Put \(D_i=C_{i+1}\), with differential \(d_D=-d_C\), so \(D[1]=C\) in the homological shift convention. The exact sequence

\[
0\longrightarrow D\longrightarrow\operatorname{Cone}(1_D)
\longrightarrow D[1]\longrightarrow0
\]

is split in each degree. Apply the additive Dold–Kan functor, and write its terms as

\[
0\longrightarrow M\longrightarrow CM\longrightarrow BM
\longrightarrow0.
\tag{7.9}
\]

Here \(BM=\Gamma C\), every term is projective, and \(CM\) has a simplicial linear contraction induced by the cone contraction. For each degree, the homogeneous part of weight \(p\) in the Koszul complex on \(M\subset CM\) is exact:

\[
\begin{gathered}
0\longrightarrow\bigwedge^p M
\\
\longrightarrow\bigwedge^{p-1}M\otimes CM\longrightarrow\cdots\\
\longrightarrow M\otimes\operatorname{Sym}^{p-1}CM\\
\longrightarrow\operatorname{Sym}^p CM\\
\longrightarrow\operatorname{Sym}^p BM\longrightarrow0.
\end{gathered}
\tag{7.10}
\]

To check exactness without a characteristic assumption, split \(CM=M\oplus BM\) in that degree. For a free \(M\), its variables form a regular sequence in \(\operatorname{Sym}M\); the Koszul complex resolves the quotient by those variables. The finite-variable calculation extends to an arbitrary basis by exact filtered colimits. For a projective \(M\), add a projective complement making it free. Its own Koszul complex is a retract of that free-variable complex, by including and then augmenting the complement's Koszul factor. Hence it too has no positive homology and has degree-zero quotient \(B\). Tensor with \(\operatorname{Sym}BM\), which is projective in each weight: a symmetric power of a projective module is a direct summand of the corresponding symmetric power of a free module. Taking weight \(p\) proves (7.10). The differential uses the inclusion \(M\to CM\), so these exact complexes are compatible with faces and degeneracies.

Every middle term in (7.10) is a contractible simplicial module. Indeed positive symmetric powers preserve the simplicial contraction of \(CM\). Tensoring such a contraction with the degeneracy operators in the other factor gives a contraction of their tensor product. More explicitly, if \(h_i\) are its homotopy operators, use \(s_i\otimes h_i\); the face and degeneracy identities follow separately in both factors. Exact normalization and successive long exact homology sequences therefore give

\[
\begin{gathered}
H_i(N\operatorname{Sym}^p BM)
\\
\simeq H_{i-p}(N\bigwedge^p M).
\end{gathered}
\tag{7.11}
\]

The complex on the right is nonnegative, so it vanishes when \(i<p\). No factorial was inverted, and the proof includes characteristic two. \(\square\)

**Lemma 7.4 (positive polynomial cells and powers of their ideal).** If \(A\to B\) is surjective, it has a polynomial resolution \(P_\bullet\to B\) with \(P_0=A\), constructed by attaching free cells only in positive dimensions. For

\[
\begin{gathered}
Q_\bullet=B\otimes_A P_\bullet,\\

I_\bullet=\ker(Q_\bullet\to B),
\end{gathered}
\tag{7.12}
\]

every power satisfies

\[
H_i(NI^p)=0\qquad(i<p).
\tag{7.13}
\]

**Proof.** Begin with the constant algebra \(A\). For each \(r\in\ker(A\to B)\), attach a free one-simplex with faces \(r,0\). Algebraically a free \(n\)-cell attachment is the pushout obtained by adjoining a simplex and identifying its boundary with the prescribed boundary in the old algebra. In simplicial degree \(m\), the boundary variables are eliminated by that prescription. The remaining independent variables are indexed by surjections \([m]\twoheadrightarrow[n]\), one for each degeneracy of the new cell. Thus every term is still polynomial, and terms in dimensions below \(n\) do not change.

The one-cells make \(\pi_0\) exactly \(B\): their boundaries generate the kernel ideal, and the augmentation prevents any further relation on \(B\). For each normalized \(n\)-cycle, \(n\geq1\), attach an \((n+1)\)-cell whose first face is that cycle and whose other faces are zero. The cycle identities are exactly the boundary compatibility identities. This kills every class in \(\pi_n\) and changes no lower normalized term or boundary. Proceed by dimension. The resulting augmentation induces an isomorphism on \(\pi_0\) and has zero positive homotopy groups. Its additive underlying simplicial group is Kan; a map to a constant simplicial group is a Kan fibration, since every horn filler remains in the component specified by its vertex. The boundary-lifting criterion therefore makes this a polynomial resolution as defined in Section 1. Taking all kernel elements and all cycles as labels makes the construction functorial, without choosing generators.

After tensoring with \(B\), all new cell variables augment to zero. We prove (7.13) by induction through these cell attachments. It holds for the initial algebra \(Q=B\), whose augmentation ideal is zero. Consider an attachment in dimension \(n\geq1\), and write \(Q'\), \(I'\) for the enlarged algebra and ideal. Degreewise it is a polynomial extension \(Q_m[z_\sigma]\), and
\(I'_m=I_m+(z_\sigma)\). Filter \((I')^p\) **increasingly** by polynomial degree at most \(j\) in these new variables. Boundary substitutions belong to the old ideal \(I\); they lower the number of new variables and preserve this filtration. The weight-\(j\) quotient is the simplicial module

\[
I^{\max(p-j,0)}\otimes_B\operatorname{Sym}_B^j V,
\tag{7.14}
\]

where \(I^0=Q\) and \(V\) is the direct sum of copies of \(\Gamma(B[n])\) for the attached cells. To see the coefficient ideal in (7.14), a monomial of new degree \(j\) belongs to \((I')^p\) precisely when its coefficient has old ideal order at least \(\max(p-j,0)\). In the associated graded, a boundary substitution disappears, so the remaining action on new variables is exactly the simplicial sphere module \(V\).

For \(j=0\), this quotient is the old \(I^p\), already \(p\)-connective. For \(j>0\), Lemma 7.3 makes \(\operatorname{Sym}^jV\) \(j\)-connective. If \(j<p\), the other factor is \((p-j)\)-connective by induction; if \(j\geq p\), it is the nonnegative complex of \(Q\). The tensor product is therefore at least \(p\)-connective. Here tensor products can be computed by normalized projective complexes, Theorem 1.3, and The derived tensor product and Tor sheaves, Theorem 2.2: degreewise the ideal powers have monomial bases over \(B\), and all the symmetric sphere terms are projective. The derived tensor of a complex supported homologically from degree \(a\) and one supported from degree \(b\) is supported from \(a+b\); replace their connective truncations by projective resolutions in those same ranges to check this directly.

The long exact sequences for the successive increasing filtration steps now prove the same bound for each finite step. Their union is all of \((I')^p\): each polynomial has finite new degree. Exact filtered colimits of modules commute with normalization and homology, so the bound holds for the whole attachment. At a limit of cell stages, ideal powers and their normalized homology again commute with the filtered union. This completes the induction and proves (7.13) for every \(p\). \(\square\)

**Theorem 7.5 (Quillen's spectral sequence).** For every surjection of commutative rings \(A\to B\), let \(E\) be the polynomial differential diagram (2.3). There is a strongly convergent spectral sequence

$$
\begin{gathered}
E_1^{p,q}\\
=H_{-p-q}\bigl(\mathcal D_{B/A},\operatorname{Sym}^p E\bigr)
\\
\Longrightarrow\operatorname{Tor}^A_{-p-q}(B,B),
\\
d_r:(p,q)\mapsto(p+r,q-r+1),
\end{gathered}
\tag{13.1}
$$

Here \(p\geq0\), and a term can be nonzero only when \(-p-q\geq p\). In particular

\[
\begin{gathered}
H_i(\mathcal D_{B/A},\operatorname{Sym}^p E)=0
\\
(i<p).
\end{gathered}
\tag{7.15}
\]

The filtration on \(\operatorname{Tor}_n^A(B,B)\) is finite, with its \((n+1)\)-st step zero. The construction is natural in commutative squares of surjective ring maps and is compatible with the products on derived self-intersections.

**Proof.** Choose the functorial cell resolution of Lemma 7.4. The split normalization decomposition commutes with tensoring. Hence \(NQ=(NP)\otimes_A B\), and \(NP\) is a nonnegative projective \(A\)-resolution of \(B\). Consequently

\[
H_n(NQ)=\operatorname{Tor}_n^A(B,B).
\tag{7.16}
\]

In each degree, \(Q_m\) is a polynomial \(B\)-algebra augmented by sending its variables to zero. Its ideal powers have the canonical associated graded

\[
\begin{gathered}
I/I^2\xrightarrow{d}\Omega_{P_\bullet/A}\otimes_{P_\bullet}B,\\
I^p/I^{p+1}\simeq\operatorname{Sym}_B^p(I/I^2).
\end{gathered}
\tag{7.17}
\]

The first arrow is an isomorphism: in polynomial coordinates both sides have the basis of the variables, mapped to their differentials. These identifications commute with every polynomial face map, including nonlinear ones, because the induced map modulo the square of the ideal is its linear differential at the augmentation.

Define an actual filtered complex by

\[
\begin{gathered}
C=NQ,\\
 F^pC=N(I^p)\ (p\geq0),
\\
 F^pC=C\ (p<0).
\end{gathered}
\tag{7.18}
\]

Normalization is exact, so its graded quotient is \(N\operatorname{Sym}^p(I/I^2)\). The page construction and its naturality are Filtered complexes and Cartan–Eilenberg resolutions, Theorem 1.1. Apply it with cohomological indexing \(p+q=-n\). Its first page is the homology of this graded quotient, and its differential increases \(p\) by \(r\) and total cohomological degree by one. This gives exactly the displayed bidegree in (13.1). Lemma 2.1, applied to the diagram \(\operatorname{Sym}^pE\), identifies that first page with the stated diagram homology.

The simplicial module \(I/I^2\) is degreewise free. Its degree-zero homology is \(\Omega_{B/A}=0\): the polynomial differential coequalizer is the module of derivations of \(B\), and every \(A\)-derivation of a quotient of \(A\) is zero. Lemma 7.3 proves (7.15). In total homological degree \(n\), the first page therefore has only the finitely many weights \(0\leq p\leq n\).

This finite first-page region does not by itself justify convergence of an infinite decreasing filtration. We use the stronger estimate of Lemma 7.4. From
\(0\to N(I^p)\to NQ\to N(Q/I^p)\to0\), it gives

\[
\begin{gathered}
H_n(NQ)\\
\xrightarrow{\sim}H_n(N(Q/I^p))
\\
(p>n).
\end{gathered}
\tag{7.19}
\]

Both the degree-\(n\) and degree-\((n-1)\) homology of the kernel vanish. The complexes on the right have finite filtrations, so the same lesson, Theorem 2.1 proves their convergence. Choose \(p>n+1\) to stabilize the abutments in degree \(n\) and the adjacent incoming degree. Increasing it further introduces no new first-page term in those degrees, by (7.15), and the finite exact-couple construction identifies the stabilized graded pieces. This proves strong convergence to the actual Tor groups. Their induced filtration is
\(F^p\operatorname{Tor}_n=\operatorname{im}(H_n(NI^p)\to H_n(NQ))\); it is zero for \(p>n\). No completion or exchange of homology with an inverse limit is needed.

Finally the labelled cell construction and all the ideal-power maps are functorial. Ideal multiplication sends \(I^p\otimes I^{p'}\) into \(I^{p+p'}\). The normalized shuffle product is a chain map preserving this filtration; the shuffle identities give its associativity and Leibniz rule. The resulting products pass through the exact couples to the products on \(H_*(B\otimes_A^{\mathbf L}B)\), which are the derived self-intersection products. This proves the naturality and product assertions. \(\square\)

For a quotient by a regular sequence, the spectral sequence has a particularly simple form. Lemma 7.1 gives \(L_{B/A}=(I/I^2)[1]\), with \(I/I^2\) projective. Formula (7.11), now with a constant simplicial module \(M=I/I^2\), places the homology of its \(p\)-th symmetric power entirely in degree \(p\), where it is \(\bigwedge^p(I/I^2)\). All differentials vanish, and the result is the usual exterior Tor algebra of the Koszul resolution. This includes regular quotients in characteristic two; an exterior square is still required to kill each repeated generator.


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
\begin{gathered}
\operatorname{Exal}_A(B,M)\\
\simeq\operatorname{Ext}^1_B(L_{B/A},M),
\\

\operatorname{Aut}(E/B,M)\simeq
\\
\operatorname{Ext}^0_B(L_{B/A},M)=\operatorname{Der}_A(B,M).
\end{gathered}
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
\begin{gathered}
H^0(L_{A/A'})=0,\\
 H^{-1}(L_{A/A'})=J.
\end{gathered}
\tag{9.2}
$$

Its canonical truncation map $L_{A/A'}\to J[1]$, followed by $c[1]$, defines an element of $\operatorname{Ext}^1_A(L_{A/A'},M)$. Derived tensor–Hom adjunction identifies this group with

$$
\begin{gathered}
\operatorname{Ext}^1_B(L_{A/A'}\otimes_A^{\mathbf L}B,M)
\\
=\operatorname{Hom}_A(J,M).
\end{gathered}
\tag{9.3}
$$

For the equality, the source of the Ext group has no degree-zero cohomology and has $H^{-1}=J\otimes_A B$; its terms below $-1$ contribute nothing to Ext in degree one. Thus the element in (9.3) is exactly the specified map $c$.

Apply $\mathbf R\operatorname{Hom}_B(-,M)$ to the fundamental triangle for $A'\to A\to B$. Its long exact sequence includes

$$
\begin{gathered}
0\to\operatorname{Ext}^1_B(L_{B/A},M)
\\
\to\operatorname{Ext}^1_B(L_{B/A'},M)
\\
\xrightarrow{r}\operatorname{Hom}_A(J,M)
\\
\xrightarrow{\partial}\operatorname{Ext}^2_B(L_{B/A},M).
\end{gathered}
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
\begin{gathered}
\mathbf Lf^*L_{Y/S}\to L_{X/S}\to L_{X/Y}
\\
\to(\mathbf Lf^*L_{Y/S})[1].
\end{gathered}
\tag{10.3}
$$

Smooth, étale, and lci computations have the same local forms as for rings.

**Proof.** Stalks commute with free polynomial constructions, differentials, tensor products, and normalization. At $x\in U$ corresponding to $\mathfrak p\subset B$, with image $\mathfrak q\subset A$, the sheaf model has stalk $L_{B_{\mathfrak p}/A_{\mathfrak q}}$. Localization (5.1) identifies it with $L_{B/A}\otimes_B B_{\mathfrak p}$, the stalk of the right side of (10.2). The natural comparison map is therefore a quasi-isomorphism on every stalk, proving (10.2) and quasi-coherence of cohomology.

The polynomial construction, differential sequences, and their comparison maps in Section 4 apply to sheaves of rings. They give (10.3); equivalently its affine restrictions are the already proved triangles and the globally defined maps identify their cones on every stalk. The smooth, étale, and lci claims follow by checking the respective affine opens. ∎

For a smooth $X/k$, the result is $L_{X/k}=\Omega_{X/k}[0]$, so for a quasi-coherent module $M$,

$$
\begin{gathered}
\operatorname{Ext}^i_X(L_{X/k},M)
\\
=H^i(X,\mathcal H\!om(\Omega_{X/k},M)).
\end{gathered}
\tag{10.4}
$$

Here finite local freeness of $\Omega$ removes the local higher Ext terms. Thus the familiar $H^0$ automorphisms, $H^1$ first-order deformations and $H^2$ obstructions from the earlier smooth-scheme lesson are the global groups associated with the cotangent complex.

The global ringed-space theorem [Stacks, Tag 08UZ](https://stacks.math.columbia.edu/tag/08UZ) has the following form. Given a square-zero thickening $S\hookrightarrow S'$ with kernel $\mathcal J$, a morphism $f:X\to S$, an $\mathcal O_X$-module $M$, and an $f^{-1}\mathcal O_S$-linear map $f^{-1}\mathcal J\to M$, there is a canonical obstruction in $\operatorname{Ext}^2_X(L_{X/S},M)$ to a thickening $X\hookrightarrow X'$ with identified kernel $M$ and compatible morphism $X'\to S'$ inducing that map. Its vanishing is necessary and sufficient; if it vanishes, isomorphism classes of solutions form a torsor under $\operatorname{Ext}^1_X(L_{X/S},M)$, and automorphisms are $\operatorname{Ext}^0_X(L_{X/S},M)$. The following sheaf-extension argument proves this statement, including its ringed-topos form.

### Extensions of sheaves of algebras

We now work on an arbitrary small site, or equivalently in its sheaf topos \(\mathscr T\), with a homomorphism \(\mathcal A\to\mathcal B\) of commutative ring sheaves. No enough-points assumption is made. An extension has identified kernel and quotient:
\[
0\longrightarrow M\longrightarrow\mathcal E
\longrightarrow\mathcal B\longrightarrow0,
\qquad M^2=0,
\]
where \(\mathcal E\) is an \(\mathcal A\)-algebra and its induced \(\mathcal B\)-module structure on \(M\) is the specified one. Denote its isomorphism class by \(\operatorname{Exal}_{\mathcal A}(\mathcal B,M)\). Fibre product over \(\mathcal B\), followed by addition of the two kernels, gives Baer addition; the split algebra \(\mathcal B\oplus M\) is its zero.

We will use two sheaf foundations explicitly. Module sheaves have colimits formed by sheafifying presheaf colimits. Their filtered colimits are exact: a finite relation or a lift in a kernel is witnessed locally by finitely many sections and therefore at a common filtered stage. The sum of the free modules \(\mathcal B[h_U^{\#}]\), over the site objects \(U\), is a generator; maps from its \(U\)-summand are sections over \(U\), so they detect a nonzero morphism. Here \(h_U^{\#}\) is the sheafification of the representable presheaf; the site need not be subcanonical. Thus the module category is a locally small Grothendieck abelian category. The complete generator-extension and transfinite argument in K-injective resolutions, Section 2, Theorem 2.4 supplies an embedding of every module into an injective. Only this module embedding theorem is needed here, not the unbounded resolution theorem.

The polynomial sheaf construction, the cotangent triangle, and Theorem 6.1 also apply on this site. Here is a way to verify that assertion without points or projective module sheaves. On each site object form the standard polynomial resolution for its section rings, with the natural restriction maps, and sheafify. Free polynomial sheaves are the sheafifications of these polynomial presheaves: every polynomial uses finitely many local labels and coefficients, and equality of two polynomials is a finite local condition. Iteration gives the standard sheaf resolution. Differentials, their tensor products and the split normalization commute with this sheafification. Its augmented additive complex is exact, either by the extra-degeneracy contraction or by exact sheafification of the sectionwise resolution. Free module sheaves indexed by a sheaf of labels are flat: a tensor element is locally a finite sum of labelled coefficients, and lifting finitely many coefficients proves preservation of an exact sequence. Normalized differential modules are retracts of such flat modules. Hence their bounded-above complexes compute the required derived tensors. The natural polynomial differential and cone models of Section 4 sheafify to the cotangent triangle. The face formula (6.5) and the finite relation-and-filler calculation (6.6)–(6.7) sheafify to
\[
\tau_{\geq-1}L_{\mathcal B/\mathcal A}
\simeq[\mathcal N\longrightarrow\mathcal F],
\qquad
\mathcal N=\mathcal K/\mathcal K^2,
\]
where \(\mathcal P=\mathcal A[U\mathcal B]\twoheadrightarrow\mathcal B\), \(\mathcal K\) is its kernel and \(\mathcal F=\Omega_{\mathcal P/\mathcal A}\otimes_{\mathcal P}\mathcal B\). Thus \(H^0L=\Omega_{\mathcal B/\mathcal A}\). For a surjection of ring sheaves its first truncation is the conormal module in degree \(-1\). All these exactness assertions concern sheaves; surjectivity on every object’s sections is neither assumed nor needed.

**Lemma 10.2 (injective coefficients lift polynomial generators).** Let \(I\) be an injective \(\mathcal B\)-module. In an extension by \(I\), any prescribed map from a free polynomial sheaf into \(\mathcal B\) lifts to an \(\mathcal A\)-algebra map into \(\mathcal E\).

**Proof.** Let \(S\) be its sheaf of generators, with prescribed label map \(S\to U\mathcal B\), and let \(p:\mathscr T/S\to\mathscr T\) be the slice projection. The fibre sheaf of lifts of these labels is a torsor under \(p^*I\): the difference of two lifts lies uniquely in \(I\), and a lift exists locally because \(\mathcal E\to\mathcal B\) is an epimorphism.

The pullback \(p^*I\) is injective as a \(p^*\mathcal B\)-module. Indeed \(p^*\) has the exact left adjoint \(p_!\) on modules, the direct sum indexed by \(S\). Its construction uses local finite-support sums of elements in the fibres over labels. Its exactness follows by locally lifting the finitely many entries of such a sum; kernels are checked entry by entry. The adjunction then makes \(\operatorname{Hom}(-,p^*I)=\operatorname{Hom}(p_!(-),I)\) exact.

An additive torsor \(C\) under an injective module \(J\) over a ring sheaf \(D\) has a section. To see this directly, linearize it: take \(J\oplus D[C]\) and impose
\[
[c+j]-[c]=j.
\]
Send \([c]\) to \(1\) and \(J\) to zero. Locally a choice of \(c\) identifies the result with \(J\oplus D\), so it is an extension \(0\to J\to W\to D\to0\), whose fibre over \(1\) is exactly \(C\). Injectivity of \(J\) gives a retraction onto \(J\), hence a splitting of the extension and a section of that fibre. Apply this in \(\mathscr T/S\) to \(p^*I\). A section is a sheaf map of generator lifts \(S\to U\mathcal E\). The polynomial universal property extends it uniquely to the required algebra map. \(\square\)

**Theorem 10.3 (global extension classification).** For every \(\mathcal B\)-module \(M\) there are natural identifications
\[
\begin{gathered}
\operatorname{Exal}_{\mathcal A}(\mathcal B,M)
\simeq\operatorname{Ext}^1_{\mathcal B}
 (L_{\mathcal B/\mathcal A},M),\\
\operatorname{Aut}(\mathcal E/\mathcal B,M)
\simeq\operatorname{Ext}^0_{\mathcal B}
 (L_{\mathcal B/\mathcal A},M).
\end{gathered}
\tag{10.5}
\]
The first is an isomorphism of Baer groups. The Ext groups are global derived Hom in the category of module sheaves.

**Proof.** First construct the comparison for every \(M\). The cotangent triangle for \(\mathcal A\to\mathcal E\to\mathcal B\) and the conormal truncation for its square-zero quotient give
\[
L_{\mathcal B/\mathcal A}
\longrightarrow L_{\mathcal B/\mathcal E}
\longrightarrow M[1].
\tag{10.6}
\]
Call this class \(\kappa_M(\mathcal E)\). It is natural for maps of extensions and of coefficients. In a polynomial presentation admitting a lift into \(\mathcal E\), its relation map is exactly \(k\mapsto\widetilde k\in M\): use the lifted evaluation from the polynomial algebra over \(\mathcal E\) to \(\mathcal E\) to compare its conormal presentation with the presentation having no variables for \(\mathcal E\twoheadrightarrow\mathcal B\). This checks the sign and the asserted relation map. The split extension has zero class, because its section splits the first arrow of the cotangent triangle. For a fibre-product extension by \(M\oplus M\), the two coefficient projections give the pair of classes. Pushing out along addition therefore proves that \(\kappa_M\) respects Baer addition.

If \(M=I\) is injective, Lemma 10.2 gives a global lift from \(\mathcal P\). The usual presentation argument now takes place with sheaf maps, not objectwise choices. A lift sends relations to a \(\mathcal B\)-linear map \(u:\mathcal N\to I\); changing it changes \(u\) by a map \(\mathcal F\to I\). Conversely push out the square-zero algebra \(\mathcal P/\mathcal K^2\) along \(u\). Explicitly quotient its semidirect sum with \(I\) by the pairs \((k,-u(k))\). This yields the extension, and the lifted presentation identifies every extension in this way. Thus
\[
\operatorname{Exal}_{\mathcal A}(\mathcal B,I)
=\operatorname{coker}\bigl(
 \operatorname{Hom}(\mathcal F,I)
 \to\operatorname{Hom}(\mathcal N,I)\bigr).
\]
Exactness of \(\operatorname{Hom}(-,I)\) identifies this cokernel with \(\operatorname{Hom}(H^{-1}L,I)\): a map on \(\ker(\mathcal N\to\mathcal F)\) extends to \(\mathcal N\), and a map vanishing on that kernel extends from the image to \(\mathcal F\). The same exactness computes \(\operatorname{Ext}^1(L,I)=\operatorname{Hom}(H^{-1}L,I)\). The relation calculation for (10.6) identifies these maps. Hence \(\kappa_I\) is an isomorphism.

Choose an exact coefficient sequence \(0\to M\to I\to Q\to0\), with \(I\) injective. There is an exact sequence of Baer groups
\[
\begin{gathered}
0\to\operatorname{Der}(\mathcal B,M)
\to\operatorname{Der}(\mathcal B,I)\\
\to\operatorname{Der}(\mathcal B,Q)
\xrightarrow{\delta}\operatorname{Exal}(\mathcal B,M)\\
\to\operatorname{Exal}(\mathcal B,I)
\to\operatorname{Exal}(\mathcal B,Q),
\end{gathered}
\tag{10.7}
\]
where all derivations and extensions are relative to \(\mathcal A\). Here is a direct exactness check. For a derivation \(D:\mathcal B\to Q\), pull back \(\mathcal B\oplus I\to\mathcal B\oplus Q\) along its graph \(b\mapsto(b,D b)\). This is \(\delta D\). It splits exactly when \(D\) lifts to a derivation into \(I\). If pushing an extension by \(M\) out to \(I\) makes it split, the difference between that splitting and the canonical zero splitting of its quotient by \(M\) is such a derivation into \(Q\); its graph pullback recovers the extension. Finally an extension by \(I\) comes from one by \(M\) exactly when its quotient extension by \(Q\) splits: pull back the chosen section to obtain the extension by \(M\). This proves exactness at every displayed term.

Under \(\kappa\), the graph boundary is the derived connecting map. One can check it without choosing global polynomial lifts: represent \(D\) by \(\Omega_{\mathcal B/\mathcal A}\to Q\), pull back \(I\to Q\) to a module extension of \(\Omega\), and compose its Yoneda class with \(L\to\Omega\). Its pullback along the universal derivation has elements \((b,i)\) with \(\bar i=D b\), and multiplication \((b,i)(b',i')=(bb',bi'+b'i)\). This is the graph algebra above. The relation description of (10.6) gives precisely that Yoneda class. Thus (10.7) maps to the derived Hom exact sequence, with its first three terms identified by \(\operatorname{Der}(\mathcal B,-)=\operatorname{Hom}(\Omega,-)=\operatorname{Ext}^0(L,-)\).

We can now prove bijectivity for arbitrary coefficients. If \(\kappa_M(e)=0\), its image with coefficients \(I\) is zero, because \(\kappa_I\) is injective. By (10.7), \(e=\delta D\). The derived exact sequence makes \(D\) the image of a derivation into \(I\), so \(e=0\). This proves injectivity for every module, including \(Q\). Given \(x\in\operatorname{Ext}^1(L,M)\), its image with coefficients \(I\) corresponds to an extension \(e_I\). The image of \(e_I\) with coefficients \(Q\) has zero class; injectivity just proved for \(Q\) makes it split. Exactness lifts \(e_I\) to an extension by \(M\). Its class differs from \(x\) by a boundary from a derivation into \(Q\); correcting by the corresponding graph extension gives exactly \(x\). This proves surjectivity.

An automorphism fixing kernel and quotient is \(e\mapsto e+D(\bar e)\), for a unique \(\mathcal A\)-derivation \(D:\mathcal B\to M\); its inverse uses \(-D\). This is a sheaf formula, so it gives the global automorphism group. The identity \(H^0L=\Omega\) proves the degree-zero statement of (10.5). \(\square\)

### Global lifting over a thickened base

**Theorem 10.4 (global obstruction and choices).** Let \(\mathcal A'\twoheadrightarrow\mathcal A\) be a square-zero quotient on \(\mathscr T\), with kernel \(J\). Fix \(\mathcal A\to\mathcal B\), a \(\mathcal B\)-module \(M\), and an \(\mathcal A\)-linear map \(c:J\to M\). There is a canonical class
\[
\operatorname{ob}(c)\in
\operatorname{Ext}^2_{\mathcal B}
 (L_{\mathcal B/\mathcal A},M)
\tag{10.8}
\]
whose vanishing is equivalent to existence of a square-zero \(\mathcal A'\)-algebra extension of \(\mathcal B\) with identified kernel \(M\) and prescribed action \(c\) on \(J\). If it vanishes, its isomorphism classes form a torsor under \(\operatorname{Ext}^1_{\mathcal B}(L_{\mathcal B/\mathcal A},M)\); its automorphisms are \(\operatorname{Ext}^0_{\mathcal B}(L_{\mathcal B/\mathcal A},M)\).

**Proof.** Put \(D=\mathcal B\otimes_{\mathcal A}^{\mathbf L}L_{\mathcal A/\mathcal A'}\). The conormal truncation gives \(D\in D^{\leq-1}\) and \(H^{-1}D=\mathcal B\otimes_{\mathcal A}J\). The canonical map \(D\to(\mathcal B\otimes_{\mathcal A}J)[1]\), followed by \(c\), identifies
\[
\begin{gathered}
\operatorname{Ext}^1_{\mathcal B}(D,M)
=\operatorname{Hom}_{\mathcal A}(J,M),\\
\operatorname{Hom}_{\mathcal B}(D,M)=0.
\end{gathered}
\]
The sheaf cotangent triangle for \(\mathcal A'\to\mathcal A\to\mathcal B\) therefore gives
\[
\begin{gathered}
0\to\operatorname{Ext}^1(L_{\mathcal B/\mathcal A},M)\\
\to\operatorname{Ext}^1(L_{\mathcal B/\mathcal A'},M)\\
\xrightarrow{r}\operatorname{Hom}_{\mathcal A}(J,M)\\
\xrightarrow{\partial}
\operatorname{Ext}^2(L_{\mathcal B/\mathcal A},M).
\end{gathered}
\tag{10.9}
\]
By Theorem 10.3, the middle group classifies the actual global extensions. Its map \(r\) is the structural map on \(J\). To check this equality, embed \(M\) into an injective \(I\) and push the extension out. Lemma 10.2 gives a polynomial lift there, where (10.6) sends a constant relation \(j\) to its structural image. Equality with coefficients \(I\) implies equality with coefficients \(M\), since \(\operatorname{Hom}_{\mathcal A}(J,M)\to\operatorname{Hom}_{\mathcal A}(J,I)\) is injective. Thus the requested objects are exactly the fibre \(r^{-1}(c)\). Define \(\operatorname{ob}(c)=\partial c\). Exactness proves the criterion and the torsor statement. An \(\mathcal A'\)-derivation of \(\mathcal B\) is the same as an \(\mathcal A\)-derivation, since the action on \(\mathcal B\) factors through the epimorphism \(\mathcal A'\to\mathcal A\). Theorem 10.3 gives the automorphisms. \(\square\)

For the ringed-space problem stated above, take
\[
\mathcal A'=f^{-1}\mathcal O_{S'},\quad
\mathcal A=f^{-1}\mathcal O_S,\quad
\mathcal B=\mathcal O_X.
\]
Inverse image is exact and preserves the polynomial constructions; its kernel is \(f^{-1}\mathcal J\). An extension is a sheaf of rings on the unchanged underlying space of \(X\), with its structure map from \(S'\), so it is exactly the desired ringed-space thickening. Formula (10.8) lies in \(\operatorname{Ext}^2_X(L_{X/S},M)\) and proves the full criterion stated there. For a morphism of ringed topoi use its exact inverse-image functor in the same construction; a thickening retains the underlying topoi. This proves the ringed-topos assertion as well, without relying on points or on a Čech cover assumed to compute arbitrary sheaf cohomology.

If \(X,S\) are schemes and \(M\) is quasi-coherent on \(X\), the resulting ringed-space thickening is a scheme. On an affine \(U\subset X\), affine vanishing gives \(H^1(U,M)=0\), so the section sequence surjects onto \(\mathcal O_X(U)\). Let \(E=\mathcal O_{X'}(U)\). Its kernel is \(M(U)\). For a principal open \(D(g)\subset U\) choose a lift of \(g\) in \(E\); it is invertible exactly where its reduction is invertible. Localization and quasi-coherence identify the kernel on \(D(g)\) with \(M(U)_g\), and affine vanishing again identifies the quotient with \(\mathcal O_X(U)_g\). The natural map \(E_g\to\mathcal O_{X'}(D(g))\) is therefore an isomorphism. These principal opens identify \((U,\mathcal O_{X'}|_U)\) with \(\operatorname{Spec}E\), since a square-zero quotient induces a homeomorphism of spectra. These identifications give scheme charts. The lifted morphism is locally ringed because invertibility is detected modulo a nilpotent ideal.

When \(X/S\) is flat and \(M=\mathcal J\otimes_{\mathcal O_S}\mathcal O_X\), with \(c(j)=j\otimes1\), the square-zero flatness criterion on these affine charts makes the lift flat. Conversely every flat lift has this kernel and this structural map. Thus the theorem includes flat scheme deformations while retaining the more general ringed-space and ringed-site classification.


## 11. Exercises

**Exercise 1.** Compute $L_{A[x_1,\ldots,x_n]/A}$ and its Ext groups with an arbitrary module $M$.

**Exercise 2.** Compute $L_{k[x]/(x^2)/k}$ in every characteristic. Verify perfection and Tor amplitude, and compute its Ext groups with coefficients in $B=k[x]/(x^2)$.

**Exercise 3.** Deduce from the fundamental triangle that $L_{C/A}=L_{C/B}$ when $A\to B$ is étale. Explain why $B\to C$ need not be smooth or flat.

**Exercise 4.** Prove flat base change (3.4), identifying exactly where flatness is used. Give an ordinary base-change example in which the formula fails when flatness and Tor independence are absent.

**Exercise 5.** Prove $\operatorname{Exal}_A(B,M)=\operatorname{Ext}^1_B(L_{B/A},M)$ from the naive-complex classification and comparison. Show why the same truncation argument does not identify Ext in degree two. Compute that failure for $B=k[x]/(x^2)\to k$.

**Exercise 6.** Let \(F=\Gamma(B[1])\) over any ring \(B\), with generator \(x\) in degree one and \(e=s_0x\), \(f=s_1x\) in degree two. Using the Moore direct-summand model \(N_n=\bigcap_{i>0}\ker d_i\), compute the entire normalized complex of \(\operatorname{Sym}^2F\). Check the result in characteristic two. More generally use (7.11) to compute \(\operatorname{Sym}^p\Gamma(B^r[1])\) in homology and deduce the collapse of (13.1) for a quotient by a regular sequence.

**Exercise 7.** Over a field \(k\), give the two-term homological complex \(C=[k[t]\xrightarrow{1-t}k[t]]\), in degrees one and zero, the filtration \(F^pC=t^pC\), \(p\geq0\). Compute its associated graded complexes, every quotient \(C/F^pC\), and its actual homology. Show that the filtration is separated in each chain degree, but its first spectral-sequence page cannot converge to that homology. Identify the convergence hypothesis from Theorem 7.5 which fails.

**Exercise 8.** Let \(A\ne0\) be any ring, let \(C=[A\xrightarrow{1}A]\) in homological degrees one and zero, and put \(V=\Gamma C\). The inclusion of the degree-zero subcomplex gives a constant simplicial submodule \(J=\Gamma(A[0])\subset V\). Form the square-zero simplicial ring \(R=A\oplus V\), its augmentation \(R\to A\), and the simplicial \(R\)-module \(M=R/J\). Prove that \(R\to A\) is a quasi-isomorphism but \(M\to M\otimes_RA\) is not. Locate the failure of the flatness hypothesis in Lemma 4.A, and explain why Theorem 4.B still applies with derived tensor.

**Exercise 9.** Let \(X=\mathbb P^1_k\) over any field and \(M=\mathcal O_X(-4)\). Classify square-zero ringed-space extensions of \(X/k\) with identified kernel \(M\). Show that each is locally split, but its global classes form \(k\). Give transition maps on the standard two-affine cover, and calculate the automorphisms and the degree-two obstruction group.

## 12. Complete solutions

**Solution 1.** Use the constant polynomial resolution. Its differential module is $\bigoplus_{i=1}^nB\,dx_i$, concentrated in degree zero, by (2.5). It is finite free, so

$$
\begin{gathered}
\operatorname{Ext}^0_B(L_{B/A},M)=M^n,
\\
 \operatorname{Ext}^i_B(L_{B/A},M)=0\quad(i>0).
\end{gathered}
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
\begin{gathered}
\operatorname{Ext}^2_k(L_{k/B},k)=k,
\\
 \operatorname{Ext}^2_k(\operatorname{NL}_{k/B},k)=0.
\end{gathered}
\tag{12.3}
$$

For example $\operatorname{Hom}(k[2],k[2])=k$ supplies the missing class on the left, while the category of vector spaces has no positive Ext of two degree-zero vector spaces. Thus degree-one extension classification survives truncation, but degree-two obstruction theory requires the full complex.

**Solution 6.** Both faces of \(x\) vanish. The simplicial identities give
\[
\begin{array}{c|ccc}
&d_0&d_1&d_2\\
e&x&x&0\\
f&0&x&x
\end{array}
\]
The degree-one term of the symmetric square is \(B x^2\). In degree two write an element as \(a e^2+b ef+c f^2\). The equation \(d_2=0\) forces \(c=0\); then \(d_1=0\) forces \(a+b=0\). Hence its Moore-normalized term is \(B(e^2-ef)\), and \(d_0(e^2-ef)=x^2\). Every monomial in simplicial degree \(n>2\) uses at most two of the \(n\) degree-one degeneracy coordinates. Choose an unused coordinate; that monomial is in the image of the degeneracy omitting that coordinate. Thus the degenerate quotient, and equivalently its Moore direct summand, is zero in all higher degrees. The whole normalized complex is therefore
\[
B\xrightarrow{1}B\qquad\text{in degrees }2,1,
\]
and is acyclic over every \(B\). In characteristic two the same computation uses \(e^2+ef\); its differential is still \(x^2\). No division by two is involved.

For \(B^r[1]\), use (7.11) with the constant simplicial module \(M=B^r\). The only homology is \(\bigwedge^pB^r\), in degree \(p\). If \(B=A/(f_1,\ldots,f_r)\) is a regular quotient, Lemma 7.1 gives this model with \(B^r=I/I^2\). The first page of (13.1) is supported on \((p,q)=(p,-2p)\). Its differential cannot reach another such position: a putative target would require \(r+1=0\) for a page number \(r\geq1\). Incoming differentials have the same obstruction. The filtration on each Tor group has just its weight equal to its homological degree. Thus
\[
\operatorname{Tor}_*^A(B,B)\simeq\bigwedge_B^*(I/I^2),
\]
with its usual exterior product, also computed directly by the regular-sequence Koszul resolution.

**Solution 7.** Each graded quotient has the identity as its differential, because \(1-t\) reduces to \(1\) modulo \(t\). Thus every associated graded complex is acyclic and the first page is zero. On \(C/F^pC\), multiplication by \(1-t\) has inverse \(1+t+\cdots+t^{p-1}\) for \(p\geq1\), so these quotient complexes are acyclic too. But multiplication by \(1-t\) is injective on \(k[t]\) and has cokernel \(k[t]/(1-t)=k\). Therefore \(H_1(C)=0\) and \(H_0(C)=k\).

Each chain term satisfies \(\bigcap_p t^pk[t]=0\), so the filtration is degreewise separated. Nevertheless every \(F^pC\) has the same nonzero degree-zero homology, and its map to \(H_0(C)\) is an isomorphism: evaluation at \(t=1\) sends \(t^p\) to \(1\). The induced filtration on homology is constant, not separated. In particular the connectivity estimate (7.13) fails in degree zero for every positive \(p\). Consequently (7.19) fails as well; the finite quotients all have zero homology instead of stabilizing to \(H_0(C)\). This is why the proof of Theorem 7.5 establishes the bound on the actual ideal powers, in addition to the bound on their associated graded.

**Solution 8.** The multiplication in \(R\) is \((a,v)(b,w)=(ab,aw+bv)\); the ideal \(V\) has square zero. Since \(J\) is a simplicial \(A\)-submodule, it is an ideal in \(R\). Exact normalization and Dold–Kan give
\[
NR=A[0]\oplus C,\qquad
NM=A[0]\oplus A[1].
\]
The first augmentation is a quasi-isomorphism, because \(C\) is contractible. Ordinary base change kills the image of \(V\), so \(M\otimes_RA=A\). Its comparison map kills \(H_1(NM)=A\ne0\).

In degree zero, \(R_0=A[\varepsilon]/(\varepsilon^2)\) and \(M_0=A\), with \(\varepsilon\) acting by zero. This module is not flat: tensor the inclusion \((\varepsilon)\hookrightarrow R_0\) with \(A\). Its source is \(A\), whereas its map into \(R_0\otimes_{R_0}A=A\) is zero. Thus precisely the flatness needed to keep the free resolution exact under ordinary tensor has failed. Theorem 4.B nevertheless identifies the normalized derived realization of \(M\otimes_R^{\mathbf L}A\) with \(NM\), including its degree-one copy of \(A\). The pointwise higher derived tensor terms supply what ordinary tensor discarded.

**Solution 9.** Since \(X/k\) is smooth, \(L_{X/k}=\Omega_{X/k}=\mathcal O_X(-2)\) in degree zero. Hence
\[
\begin{gathered}
\operatorname{Ext}^i_X(L_{X/k},M)\\
=H^i(X,\mathcal O_X(-2)).
\end{gathered}
\]
On \(U=\operatorname{Spec}k[x]\) and \(V=\operatorname{Spec}k[y]\), \(y=x^{-1}\), choose frames \(m_U,m_V\) for \(M\) with \(m_V=x^{-4}m_U\). The frame \(\partial_y\otimes m_V\) is \(-x^{-2}(\partial_x\otimes m_U)\). Affine vanishing and the two-member Čech complex therefore give
\[
\begin{gathered}
H^0(X,\mathcal O_X(-2))=0,\\
H^1(X,\mathcal O_X(-2))
=\frac{k[x,x^{-1}]}{k[x]+x^{-2}k[x^{-1}]}
=k\,[x^{-1}],\\
H^i(X,\mathcal O_X(-2))=0\quad(i\geq2).
\end{gathered}
\]
For \(\lambda\in k\) define on the overlap the derivation
\[
D_\lambda(f)=\lambda x^{-1}f'(x)m_U.
\]
Glue the split algebras \(\mathcal O_U\oplus M|_U\) and \(\mathcal O_V\oplus M|_V\), after the usual coordinate and module identifications, by \((f,m)\mapsto(f,m+D_\lambda(f))\). Its inverse uses \(-D_\lambda\), and the derivation rule makes it an algebra isomorphism. There are no triple-cover conditions beyond inverse compatibility on this two-open cover. Changing the local splitting adds a coboundary, precisely a term in \(k[x]+x^{-2}k[x^{-1}]\). Thus these are all classes and different \(\lambda\) give different identified extensions. Theorem 10.3 makes their Baer addition addition in \(k\). Their automorphism groups fixing quotient and kernel are trivial, and the degree-two obstruction group is zero. Quasi-coherence of \(M\) makes these actual scheme thickenings by the argument after Theorem 10.4. This calculation works in every characteristic, including two.

## 13. Foundations and scope

- **Kan boundary lifting.** The general boundary-filling result for a nonempty acyclic Kan complex is Simplicial sets, nerves and Kan complexes, Lemma 5.3c. Proposition 1.4 proves its precise application to polynomial resolutions. Theorems 1.1–1.3 supply exact normalization, its Dold–Kan inverse, the diagonal–total comparison and the homotopies used here. The standard polynomial resolution and diagram-homology comparison are constructed in Sections 1–2.
- **Homological change of rings.** Lemma 4.A proves (4.1) for degreewise flat simplicial modules. Theorem 4.B proves the general category-homology statement corresponding to [Stacks, Tag 08RX], including arbitrary unbounded module-diagram complexes, explicit derived colimit, tensor-flat free resolutions and direct-sum telescopes. Its simplicial specialization proves that (4.5) remains a resolution. The cotangent fundamental triangle is then constructed from this module theorem and polynomial differential sequences in Section 4.
- **Derived-category algebra.** The free diagram resolutions and their derived colimits are constructed in Theorem 4.B. Complexes, cones and localization, Sections 1–5 proves the cone and localized triangle constructions. Flat modules and K-flat resolutions, Sections 1–2 proves that a bounded-above complex of flat modules is K-flat; The derived tensor product and Tor sheaves, Sections 1–2 proves invariance and associativity. Internal derived Hom and Ext sheaves, Sections 1–3 and Theorem 3.1 proves tensor–Hom adjunction. The two spectral sequences and the finite-filtration convergence used here are constructed in Filtered complexes and Cartan–Eilenberg resolutions, Sections 1–3. For the standard orthogonality \(\operatorname{Hom}(D^{\leq a},D^{\geq a+1})=0\), represent the first object by its upper good truncation and the second by an injective resolution starting in degree \(a+1\). Maps into that bounded-below injective complex compute derived maps, and every degree-zero chain map from the first complex is zero. The required injective resolutions are Injective modules and bounded-below derived functors, Sections 2–4.
- **Commutative algebra.** Section 7 proves Koszul exactness for a regular sequence, the conormal basis for a Koszul-regular sequence and independence of a finite local complete-intersection presentation, all over arbitrary rings. Étale morphisms and their local structure, Sections 1–2 proves the diagonal and standard étale facts: the open diagonal gives a flat epimorphism on affine coordinate rings. Smooth morphisms, Theorem 4.1 gives local étale coordinates. The arbitrary-module square-zero flatness criterion is Formal moduli and Schlessinger's theorem, Lemma 4.3: reduction flatness and injectivity of \(J\otimes_A B\to B'\) imply flatness of the lift.
- **Extensions and sheaf deformation theory.** The presentation classification for rings, including Baer addition and automorphisms, is Deformations of rings and schemes and the naive cotangent complex, Section 3. Theorem 10.3 proves global extension classification on any ringed site by injective-coefficient lifting and the exact coefficient sequence; Theorem 10.4 proves the full global obstruction and torsor theorem corresponding to [Stacks, Tag 08UZ]. The slice-torsor argument, derived class, descent through coefficients and passage to scheme thickenings are included. Injective embeddings use the complete general Grothendieck-category theorem linked in Section 10.
## 14. Sources and the end of the course

The cotangent-complex chapter provides the construction [Stacks, Tags 08PL–08PN], resolution comparison [Stacks, Tag 08PQ], functoriality and Tor-independent base change [Stacks, Tags 08QL and 08QQ], the fundamental triangle [Stacks, Tag 08QX], étale and smooth computations [Stacks, Tags 08R2 and 08R5], naive comparison [Stacks, Tag 08RB], complete intersections [Stacks, Tag 08SL], tensor products [Stacks, Tag 09D8], and the ring obstruction theorem [Stacks, Tag 08SP]. Quillen's spectral sequence [Stacks, Tag 08RF] is proved here using symmetric-power connectivity, positive polynomial cells and the actual augmentation filtration. For schemes and ringed spaces the definitions and local comparisons are [Stacks, Tags 08UQ, 08UT, 08T1 and 08T4]. Our proofs use polynomial and simplicial models throughout, including in small positive characteristics.

The cotangent complex goes back to Illusie, who developed its construction, transitivity, infinitesimal extensions and local calculations, and later diagram cohomology and a more extensive equivariant deformation theory. Those larger theories are not prerequisites of the computations of this lesson. The precise results used here are the Stacks project tags cited above.

The course began with functors of points and representability. Grassmannians and boundedness made Hilbert and Quot functors representable; flattening kept their fibre conditions functorial. Formal deformation theory then described their completed local behaviour. Picard schemes added the distinction between a bundle and its sheaf class, and between discrete components and infinitesimal structure. The cotangent complex supplies the common derived mechanism: extensions in degree one, lifting obstructions in degree two, and a fundamental triangle that preserves the relations a two-term presentation can forget.
