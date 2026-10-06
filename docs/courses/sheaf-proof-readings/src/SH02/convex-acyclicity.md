# SH02-CA — Extending sections on convex sets

Original programme text: CC0 1.0 Universal. This reading develops interval, compact-convex and locally closed convex extension arguments, including their canonical restriction maps.

Convexity controls how test sets fit together. It does not make an arbitrary sheaf acyclic. This unit proves an extension criterion that the directional-topology construction needs: if sections on every compact convex test set extend to the whole space, then ordinary higher cohomology vanishes. The distinction between extension on points and extension on convex sets becomes essential in dimension two.

Throughout this unit, $k$ is a commutative ring with identity, $V$ is a finite-dimensional real vector space, and sheaves are sheaves of arbitrary $k$-modules. The argument does not use finite global dimension; it therefore applies, in particular, to the full coefficient convention of the advanced course. No field, flatness, finite rank, constructibility, bounded support, or compact-ambient-space assumption is introduced. For a subset $B$ of the space carrying $F$, the notation $H^q(B;F)$ means $H^q(B;F|_B)$ with the ordinary subspace topology. It does not mean cohomology with support in $B$.

Use the [sheaf-operation hypotheses](open-prerequisites.md) for exact inverse image, enough injectives and derived sections. The proper-fibre proof supplies the compact-fibre comparison below, and the bounded-below hypercohomology proof supplies the constant-complex calculation. An injective sheaf is flabby, and flabby sheaves are acyclic for direct image; these facts apply to modules on every ringed space. See [Stacks, Tag 09SX](https://stacks.math.columbia.edu/tag/09SX) and [Tag 09T0](https://stacks.math.columbia.edu/tag/09T0). We prove the closed-cover, compact-neighborhood and exhaustion arguments actually needed below. Thus none of those three arguments is left as an unnamed SH-01 import.

## The finite gluing obstruction

### SH02-CA-CLOSED-MV — Closed-cover cohomology

**Lemma.** Suppose a topological space $Y$ is the union of two closed subsets $A$ and $B$. For every sheaf $F$ on $Y$, there is a natural long exact sequence

\[
\cdots\longrightarrow H^{q-1}(A\cap B;F)
\longrightarrow H^q(Y;F)
\longrightarrow H^q(A;F)\oplus H^q(B;F)
\longrightarrow H^q(A\cap B;F)\longrightarrow\cdots.
\tag{C1}
\]

The map on the right is the difference of the two restrictions.

*Proof.* Write $i_A,i_B,i_{A\cap B}$ for the closed inclusions. The sequence of sheaves on $Y$

\[
0\longrightarrow F\longrightarrow
i_{A*}(F|_A)\oplus i_{B*}(F|_B)
\longrightarrow i_{A\cap B,*}(F|_{A\cap B})\longrightarrow0
\tag{C2}
\]

has diagonal first map and difference second map. At a point in $A\cap B$, its stalk sequence is $0\to F_y\to F_y\oplus F_y\to F_y\to0$. At a point in just one of $A,B$, it is the identity on $F_y$, followed by zero. These are exact. Closedness is used to make the other stalk zero outside its closed set. Thus (C2) is exact.

The pushforward along a closed inclusion is exact, as its stalks have precisely this description. It also preserves injectives, being right adjoint to exact inverse image. Its derived global sections are therefore the derived sections on the closed subset. Apply derived global sections to (C2) to obtain (C1). No statement about an infinite closed cover is being used. $\square$

### SH02-CA-INTERVAL — Interval criterion

**Interval criterion.** Let $I$ be a compact interval and $F$ any sheaf on $I$. Then $H^q(I;F)=0$ for $q>1$. If, in addition, every evaluation

\[
\Gamma(I;F)\longrightarrow F_t,\qquad t\in I,
\tag{C3}
\]

is surjective, then $H^q(I;F)=0$ for every $q>0$.

*Proof.* A one-point interval has an exact sections functor, so assume $I=[a,b]$ with $a<b$. Fix $u\in H^q(I;F)$, where $q>0$. A positive-degree cohomology class is locally zero: choose an injective resolution and a global cocycle representing $u$. Exactness of the resolution as a sheaf complex gives a primitive on a neighborhood of each point. Restriction to an open set preserves injectives, because extension by zero for an open inclusion is exact. The primitive therefore makes the restricted cohomology class zero on that neighborhood.

Choose a finite such open cover of $I$. A sufficiently fine partition

\[
a=t_0<t_1<\cdots<t_m=b
\]

has every closed piece $J_r=[t_{r-1},t_r]$ contained in one member of the cover. For example, use a Lebesgue number for the finite cover and take all piece lengths smaller than it. Consequently $u|_{J_r}=0$ for every $r$.

We now join the pieces successively. Put $L_r=[a,t_r]$. The closed cover $L_{r+1}=L_r\cup J_{r+1}$ has intersection the single point $t_r$. If $q>1$, the group $H^{q-1}(\{t_r\};F)$ vanishes, so (C1) makes

\[
H^q(L_{r+1};F)\longrightarrow
H^q(L_r;F)\oplus H^q(J_{r+1};F)
\]

injective. For $q=1$ under (C3), the same injectivity follows because the preceding difference map

\[
\Gamma(L_r;F)\oplus\Gamma(J_{r+1};F)\longrightarrow F_{t_r}
\]

is surjective: a prescribed germ is the germ of a section on $I$, which can be restricted to $L_r$ and paired with zero. Notice that the original global hypothesis supplies the needed surjectivity at every intermediate join; no new hypothesis on $F|_{L_r}$ is imposed.

Induction on $r$ now gives $u|_{L_r}=0$ and finally $u=0$. This proves both assertions. The empty interval has zero sections and cohomology and is harmless. $\square$

### SH02-CA-LOCAL-SYSTEM — Locally constant coefficients and evaluation

**Theorem.** Let $I$ be a nonempty interval in $\mathbb R$, with its subspace topology, and fix $x\in I$. An interval here may be open, closed, half-open, unbounded or a singleton. For any locally constant sheaf $F$ of $k$-modules, evaluation is an isomorphism

\[
\operatorname{ev}_x:\Gamma(I;F)\xrightarrow{\sim}F_x,
\qquad H^p(I;F)=0\quad(p>0).
\tag{LC1}
\]

The unique sections with prescribed germ at $x$ identify $F$ with the constant sheaf $(F_x)_I$. More generally, if $K\in D^+(I)$ has locally constant cohomology sheaves, the canonical evaluation morphism

\[
\operatorname{ev}_x:R\Gamma(I;K)\longrightarrow K_x
\tag{LC2}
\]

is an isomorphism. It is natural in $K$, and restriction to a subinterval containing $x$ commutes with it. Neither finite generation of stalks nor an upper cohomological bound is required. The ring need not have finite global dimension.

*Proof of constancy and sections.* First observe uniqueness. For two sections of a locally constant sheaf on a connected interval, the locus where their germs agree and its complement are open. Indeed, in a local constant-sheaf trivialization both sections are locally constant functions, and equality or inequality persists on a small connected neighbourhood. If they agree at one point, connectedness makes them agree everywhere. This applies equally to a restricted sheaf on a subinterval.

On a compact interval $J=[a,b]$, a finite cover by trivializing relative-open intervals and a sufficiently fine partition give a chain of trivializing open intervals $W_1,\ldots,W_m$ covering $J$. Each $W_r$ contains the corresponding closed partition piece; consecutive overlaps contain the partition point. Such intervals are obtained by slightly enlarging those pieces inside their chosen trivializing sets. Each union $W_1\cup\cdots\cup W_r$ is an interval, and its nonempty intersection with $W_{r+1}$ is an interval. A prescribed germ at $a$ gives a constant section on $W_1$. At the next join its germ determines the unique constant section on $W_2$; these sections agree on their connected overlap by uniqueness. Continue and glue. This gives a unique section on $J$ for each germ at $a$.

Within each trivialization, passage from the germ at one point to the germ at another is an isomorphism of $k$-modules. The construction is a finite composite of these isomorphisms. Hence evaluation at every $x\in J$, not only at $a$, is an isomorphism. Uniqueness shows that the resulting section is independent of the cover, partition and trivializations. For a singleton the assertion is immediate.

For a nondegenerate arbitrary interval $I$, choose compact subintervals $J_n$ containing $x$ such that

\[
J_n\subset\operatorname{Int}_I(J_{n+1}),\qquad
\bigcup_{n\geq0}J_n=I.
\tag{LC3}
\]

To obtain them, move the two endpoints monotonically towards the endpoints of $I$, allowing them to tend to infinity. An endpoint belonging to $I$ can be included and then kept fixed; at an endpoint not belonging to $I$, keep the approximating endpoints strictly inside. Choose the initial interval so that $x$ is in its relative interior. The interiors in (LC3) are relative to $I$, so this also works when $x$ is an included endpoint of $I$.

For $m\in F_x$, the compact case supplies a section on each $J_n$. Their restrictions agree by uniqueness. Their restrictions to $\operatorname{Int}_I(J_n)$ therefore glue to a section on $I$ with germ $m$. Uniqueness on $I$ proves (LC1)'s assertion about sections. The construction respects addition and scalar multiplication by uniqueness. The map from the constant sheaf $(F_x)_I$ to $F$ sends a locally constant $F_x$-valued function to these sections on the open sets on which that function is constant. At a point $y$ its stalk map is the continuation from $x$ to $y$, an isomorphism by the compact case on a subinterval containing both. Thus this is a sheaf isomorphism.

*Proof of higher acyclicity.* On compact $J$, the just-proved surjectivity of every evaluation is exactly the hypothesis of [SH02-CA-INTERVAL](#SH02-CA-INTERVAL). It gives $H^p(J;F)=0$ for $p>0$. For arbitrary $I$, use (LC3) and the closed-exhaustion comparison and its Milnor sequence, with the tower and Mittag–Leffler proofs. The inverse system $H^0(J_n;F)$ is identified by evaluation at $x$ with the constant system $F_x$, with identity transitions. In every positive degree it is zero. Thus in each degree the inverse system is Mittag–Leffler and its first derived limit vanishes. The Milnor sequence gives the asserted vanishing on $I$ and identifies the degree-zero comparison with evaluation. This use of the closed-exhaustion theorem is not circular: its proof concerns general sheaves and tower resolutions and does not use interval acyclicity.

*Proof for bounded-below complexes and the actual map.* Resolve $K$ by a bounded-below complex of injective sheaves $E^\bullet$. The morphism (LC2) is represented by the section-to-germ chain map $\Gamma(I;E^\bullet)\to E^\bullet_x$. Exactness of stalks ensures that the target represents $K_x$. The bounded-below hypercohomology proof, HC1a–HC2, gives

\[
E_2^{p,q}=H^p(I;H^qK)\Longrightarrow H^{p+q}R\Gamma(I;K).
\tag{LC4}
\]

If $H^qK=0$ for $q<c$, the filtration in total degree $n$ is finite because $p\geq0$ and $q\geq c$. By the sheaf case all columns except $p=0$ vanish. Consequently the canonical truncation edge is an isomorphism, and HC2 identifies its composite with the section-to-germ map as the cohomology map of (LC2):

\[
H^nR\Gamma(I;K)\xrightarrow{\sim}\Gamma(I;H^nK)
\xrightarrow{\sim}(H^nK)_x=H^n(K_x).
\tag{LC5}
\]

This proves (LC2) in every degree without an upper bound. The section-to-germ maps commute with sheaf morphisms, resolution comparisons and restriction to a subinterval containing $x$. These identities descend to the derived category and prove the asserted naturality and restriction compatibility. For the empty interval sections and cohomology are zero; no point-evaluation assertion is made. $\square$

## Compact convex test sets

### SH02-OR-CONVEX-COMPACT — Compact convex criterion

**Compact convex criterion.** Let $K\subset V$ be compact and convex and let $F$ be a sheaf on $K$. Assume that for every compact convex $L\subset K$, restriction

\[
\Gamma(K;F)\longrightarrow\Gamma(L;F)
\tag{C4}
\]

is surjective. Then $H^q(K;F)=0$ for $q>0$.

*Proof.* The assertion is immediate for $K=\varnothing$. We induct on the dimension $d$ of the affine hull of nonempty $K$. At $d=0$ the set is one point and sections are exact. If $d>0$, choose an affine linear function that is nonconstant on $K$. It defines a map

\[
p:K\longrightarrow I=p(K),
\]

where $I$ is a nondegenerate compact interval. The map is proper: $K$ is compact and the target is Hausdorff, so inverse images of compact sets are closed subsets of $K$ and hence compact.

For $t\in I$, the fiber $K_t=K\cap p^{-1}(t)$ is a nonempty compact convex set of affine dimension at most $d-1$. Its restricted sheaf inherits (C4). Indeed, for compact convex $L\subset K_t$, an extension of any section on $L$ to $K$ can be restricted to $K_t$. The induction hypothesis gives $H^q(K_t;F)=0$ for $q>0$.

The proper-fibre formula and its section-restriction identification apply to the compact Hausdorff spaces $K$ and $I$, with arbitrary $k$-module coefficients. They identify

\[
(R^q p_*F)_t\simeq H^q(K_t;F),
\qquad
(p_*F)_t\simeq\Gamma(K_t;F).
\tag{C5}
\]

Thus $Rp_*F$ is the sheaf $p_*F$ in degree zero. The evaluation of a global section of $p_*F$ at $t$ corresponds in (C5) to the restriction $\Gamma(K;F)\to\Gamma(K_t;F)$, which is surjective by (C4). The interval criterion applies to $p_*F$.

Finally, direct-image composition gives

\[
R\Gamma(K;F)\simeq R\Gamma(I;Rp_*F)
\simeq R\Gamma(I;p_*F).
\tag{C6}
\]

For clarity, this composition can be computed with one injective resolution: $p_*$ preserves injectives because its left adjoint $p^{-1}$ is exact. The last complex in (C6) has no positive cohomology by the interval criterion. This completes the induction, including compact convex sets with empty ambient interior. $\square$

The only fiberwise cohomology identification in this proof is for a proper map. Merely observing that the fibers of a nonproper map are convex would not justify (C5). The canonical maps in (C5) are the proper-base-change maps; the map tested for surjectivity is the actual restriction, not an abstract isomorphism chosen between modules. [Stacks, Tag 09V6](https://stacks.math.columbia.edu/tag/09V6)

## Two compactness tools

### SH02-CA-COMPACT-NEIGHBORHOOD — Compact-neighborhood extension

**Extending a compact-set section to a neighborhood.** If $Y$ is locally compact Hausdorff, $L\subset Y$ is compact, and $E$ is a sheaf on $Y$, then

\[
\mathop{\mathrm{colim}}_{W\supset L\text{ open}}
\Gamma(W;E)\longrightarrow\Gamma(L;E|_L)
\tag{C7}
\]

is an isomorphism. In particular, if $E$ is flabby, every section on $L$ extends to $Y$.

*Proof.* Let $s$ be a section on $L$. By the construction of inverse image, it has local representatives $s_i\in\Gamma(U_i;E)$, whose restrictions represent $s$ on $L\cap U_i$. Local compactness and the Hausdorff property allow a finite family of open sets $V_i$ covering $L$ such that $\overline V_i$ is compact and contained in the corresponding $U_i$. To obtain them, first choose at each point a relatively compact neighborhood with closure in a representing open neighborhood, and then take a finite subcover of $L$.

For each pair $i,j$, the set

\[
B_{ij}=\{y\in\overline V_i\cap\overline V_j:
(s_i)_y\ne(s_j)_y\}
\]

is closed in the compact set $\overline V_i\cap\overline V_j$, since equality of germs is open on $U_i\cap U_j$. It is compact, hence closed in $Y$, and disjoint from $L$. Remove the finite union of these bad sets from $\bigcup_iV_i$. The result is an open neighborhood of $L$, and the $s_i$ agree on all its overlaps. They glue to a representative of $s$ on that neighborhood.

If two neighborhood sections induce the same section on $L$, their germs agree at every point of $L$. Their equality locus in the common domain is an open neighborhood of $L$, so they represent the same colimit element. This proves injectivity and surjectivity of (C7). For flabby $E$, the neighborhood representative extends to $Y$ by flabbiness. $\square$

### SH02-CA-CONVEX-EXHAUSTION-GEOMETRY — Compact convex exhaustion

**A compact convex exhaustion.** Every nonempty locally closed convex subset $C\subset V$ has compact convex subsets $K_n$ such that

\[
K_n\subset\operatorname{int}_C K_{n+1},
\qquad C=\bigcup_{n\ge1}\operatorname{int}_C K_n.
\tag{C8}
\]

Here $\operatorname{int}_C$ is topological interior in $C$. It is not the relative interior taken in an affine hull.

*Proof.* Fix a Euclidean norm. Because $C$ is locally closed, it is open in its closure $\overline C$. Hence $D=\overline C\setminus C$ is closed in $V$. Set

\[
A_m=\{x\in\overline C:|x|\le m,
\operatorname{dist}(x,D)\ge 1/m\},
\qquad m\ge1.
\tag{C9}
\]

If $D=\varnothing$, omit the distance condition. Each $A_m$ is compact and contained in $C$, the sequence is increasing, and its interiors in $C$ cover $C$. In fact, for $x\in C$, choose $m$ with $|x|<m$ and, when needed, $\operatorname{dist}(x,D)>1/m$. Both strict inequalities hold on a neighborhood of $x$ in $C$, contained in $A_m$.

Put $B_m=\operatorname{conv}(A_m)$, taking the hull of the empty set to be empty. Convexity of $C$ gives $B_m\subset C$. These hulls are compact in finite dimension. Here is the needed finite-dimensional argument. If a convex combination in $V$ uses more than $N+1$ points, where $N=\dim V$, their augmented vectors $(x_i,1)$ are linearly dependent. Varying the coefficients in that dependence keeps their sum and barycenter fixed. One may vary until a coefficient first becomes zero, keeping all coefficients nonnegative. Repeating leaves at most $N+1$ points. Thus the convex hull of a nonempty compact set is the image of the compact space $A_m^{N+1}\times\Delta^N$ under its continuous barycenter map, and is compact.

The $B_m$ are increasing, and $\operatorname{int}_C A_m\subset\operatorname{int}_C B_m$, so their interiors cover $C$. After discarding initial empty terms, construct increasing indices $m_n$ recursively. Given $m_n$, compactness of $B_{m_n}$ and the increasing open cover by the $\operatorname{int}_C B_m$ allow an index $m_{n+1}>m_n$ with $B_{m_n}\subset\operatorname{int}_C B_{m_{n+1}}$. The indices tend to infinity. Taking $K_n=B_{m_n}$ gives (C8). This argument includes sets of lower affine dimension and sets with some boundary faces retained and others excluded. $\square$

## Passing to a locally closed convex set

### SH02-OR-CONVEX-EXHAUSTION — Locally closed convex criterion

**Locally closed convex criterion.** Let $C\subset V$ be locally closed and convex, and let $F$ be a sheaf on $C$. Suppose

\[
\Gamma(C;F)\longrightarrow\Gamma(L;F)
\quad\text{is surjective for every compact convex }L\subset C.
\tag{C10}
\]

Then $H^q(C;F)=0$ for every $q>0$.

*Proof.* Assume $C$ is nonempty; otherwise the statement is immediate. It is locally compact Hausdorff. The restriction $F|_L$ to any compact convex $L\subset C$ satisfies the compact criterion: for compact convex $T\subset L$, an extension from $T$ to $C$ restricts to an extension to $L$. Therefore

\[
H^q(L;F)=0\qquad(q>0).
\tag{C11}
\]

Choose a monomorphism into an injective sheaf and let $Q$ be its cokernel:

\[
0\longrightarrow F\longrightarrow J\longrightarrow Q\longrightarrow0.
\tag{C12}
\]

First we prove that $\Gamma(C;J)\to\Gamma(C;Q)$ is onto. Take $s\in\Gamma(C;Q)$ and an exhaustion (C8). Exact restriction of (C12) to $K_n$, followed by (C11) in degree one, permits a lift $u_n\in\Gamma(K_n;J)$ of $s|_{K_n}$. We choose these lifts compatibly. If $u_n$ is already chosen and $v$ is any lift on $K_{n+1}$, the difference $v|_{K_n}-u_n$ is a section $a$ of $F$ on $K_n$. Hypothesis (C10) extends $a$ to $C$ and hence to a section $\widetilde a$ on $K_{n+1}$. Replace $v$ by $v-\widetilde a$, using the inclusion $F\hookrightarrow J$. The new lift restricts to $u_n$.

The compatible $u_n$ glue to a section $u$ of $J$ on $C$. To justify gluing despite the sets $K_n$ being closed, restrict them to the open cover $\operatorname{int}_C K_n$. Compatibility makes the restricted sections agree, so the sheaf axiom glues them. The resulting section has the specified germ on every $K_n$, because any point of $K_n$ belongs to the interior of some later $K_m$ and $u_m|_{K_n}=u_n$. Its image is $s$. The long exact sequence of (C12) now gives $H^1(C;F)=0$.

Next we show that $Q$ again satisfies (C10). Let $L\subset C$ be compact convex and take $t\in\Gamma(L;Q)$. Equation (C11) lifts $t$ to a section of $J$ on $L$. The sheaf $J$ is flabby, so (C7) extends that section to $C$. Its image in $Q$ extends $t$. This proves the claim.

The first-degree argument consequently applies to every successive cokernel in an injective resolution. Since positive cohomology of an injective sheaf is zero, the long exact sequence gives, for $q\ge2$,

\[
H^q(C;F)\simeq H^{q-1}(C;Q).
\]

Repeat until reaching the already proved first-degree vanishing. This proves all positive-degree vanishing. No interchange of a derived functor with an unverified inverse limit is used; the compatible-lift construction supplies precisely the extension that such an argument would have to establish. $\square$

### SH02-CA-OPEN-AMBIENT — Open ambient sets

**Extension criterion in an open ambient set.** Let $X\subset V$ be open, with no convexity assumption on $X$, and let $F$ be a sheaf on $X$. Assume that $\Gamma(X;F)\to\Gamma(K;F)$ is onto for every compact convex subset $K\subset X$. Then

\[
H^q(U;F)=0\qquad(q>0)
\tag{C13}
\]

for every convex open subset $U\subset X$. More generally the same conclusion holds for every locally closed convex subset $C\subset X$.

*Proof.* Restricting a global extension on $X$ to $C$ proves (C10) for $F|_C$, so apply the locally closed criterion. A convex open $U$ is a permitted $C$. In particular, passing from $X$ to $U$ does not assume $X$ was convex and does not replace the original global extension hypothesis by an unverified local one. $\square$

This last assertion contains the full open-ambient theorem used in the manifold theory. The stronger locally closed conclusion is what allows the same proof to handle $K+\gamma$ when that set is closed and unbounded in the [directional-topology unit](cone-topology.md).

## Coefficients, a counterexample, and practice

### SH02-CA-CONSTANT — Constant coefficients

**Constant coefficients.** For nonempty locally closed convex $C$ and any $k$-module $M$, the canonical map $M\to R\Gamma(C;M_C)$ is an isomorphism. Convex sets are connected and locally connected, so sections of a constant sheaf on a nonempty convex set are exactly the constant functions with values in $M$. Restrictions between such sets are the identity on $M$; thus (C10) holds and gives higher vanishing. The identification in degree zero is the stated constant-section map.

More generally this canonical map is an isomorphism for a coefficient complex $M\in D^+(k)$. The bounded-below hypercohomology construction, including its finite filtration and natural edge, proves the convergent spectral sequence

\[
E_2^{p,q}=H^p(C;H^q(N))\Longrightarrow H^{p+q}R\Gamma(C;N),
\qquad N\in D^+(k_C).
\]

Apply it to $N=M_C$. The constant-sheaf functor is exact, so its cohomology sheaves are $H^q(M)_C$, all acyclic by the preceding result. Boundedness below gives convergence in each degree, and the spectral sequence makes the edge map

\[
H^qR\Gamma(C;M_C)\longrightarrow\Gamma(C;H^q(M)_C)
\]

an isomorphism. Naturality makes its composite with $H^q(M)\to H^qR\Gamma(C;M_C)$ the constant-section isomorphism. Here is the actual map identification: the edge is induced by the canonical truncation map, as proved in the natural-edge calculation. Truncation commutes with the exact constant-sheaf functor, and in the single degree $q$ the composite is the ordinary constant-section map $H^q(M)\to\Gamma(C;H^q(M)_C)$. That map is an isomorphism because $C$ is nonempty and connected. Hence the canonical coefficient-to-derived-sections map is an isomorphism. No assumption on the size, projectivity or flatness of the modules is used.

### SH02-CA-COUNTEREXAMPLE-POINTS — Pointwise extension misses a loop

**Pointwise extension misses a loop.** Let $M$ be any nonzero $k$-module, take $K=[-2,2]\times[-1,1]$, and let

\[
S=\{(x,y):(x/2)^2+y^2=1\}\subset K.
\]

For the closed inclusion $i:S\hookrightarrow K$, put $F=i_*M_S$. The map $\Gamma(K;F)\to F_z$ is onto at every point $z$: on $S$ it is the identity $M\to M$, and outside $S$ its target is zero. Nevertheless,

\[
H^1(K;F)\simeq M\ne0.
\tag{C14}
\]

Here is a calculation using only this unit. Cover $S$ by its closed upper and lower half-ellipses. Each is homeomorphic to a compact interval, with constant coefficient cohomology $M$ in degree zero. Their intersection consists of two points. The difference map in (C1) is

\[
M\oplus M\longrightarrow M\oplus M,
\qquad(a,b)\longmapsto(a-b,a-b).
\]

Its cokernel is $M$, identified by subtracting the two coordinates. This proves $H^1(S;M_S)=M$, with all higher cohomology zero. Exact closed pushforward identifies this with (C14).

The missing compact-convex test is visible: for the vertical segment $L=\{0\}\times[-1,1]$, the restriction $F|_L$ is supported at its two endpoints, so $\Gamma(L;F)=M\oplus M$. Restriction from $\Gamma(K;F)=M$ is diagonal and is not surjective. Thus the compact convex criterion cannot in dimension two be weakened to its singleton tests. This counterexample involves torsion or infinite modules just as well as vector spaces.

### SH02-CA-EXERCISES — Exercises with solutions

**Exercises with solutions.**

1. Let $C=\{(x,y):0<x\le1,\ 0\le y\le x\}$. Give a compact convex exhaustion satisfying (C8). Explain why affine relative interiors would give the wrong covering condition.

   *Solution.* Take $K_n=C\cap\{x\ge1/(n+1)\}$. These are compact convex quadrilaterals or triangles, increase to $C$, and $K_n\subset\operatorname{int}_C K_{n+1}$ because $1/(n+1)>1/(n+2)$. The interiors in $C$ cover points on the edges $y=0$, $y=x$ and $x=1$ as well. Affine relative interiors of these full-dimensional polygons exclude all those edge points, so their union would omit valid points of $C$.

2. For nonzero $M$, show that $M_{\mathbb R^2}$ satisfies (C10) but is not flabby.

   *Solution.* Every nonempty compact convex subset is connected, so every section there is a single value in $M$ and extends constantly to $\mathbb R^2$. On the union of two disjoint nonempty open disks, sections are $M\oplus M$. Restriction from the whole plane is diagonal and fails to be surjective. Thus convex-set extension is strictly weaker than extension over every open subset.

3. Let $I=[0,3]$, let $j:(1,2)\hookrightarrow I$, and take $E=j_!M_{(1,2)}$. Compute $R\Gamma(I;E)$ and identify the failed hypothesis of the interval criterion.

   *Solution.* Let $J=[1,2]$. On $I$ there is an exact sequence

   \[
   0\longrightarrow E\longrightarrow M_J
   \longrightarrow M_{\{1\}}\oplus M_{\{2\}}\longrightarrow0,
   \]

   where closed subsets mean exact closed pushforward. Exactness follows on stalks. The interval constant-sheaf calculation makes the map on degree-zero cohomology the diagonal $M\to M\oplus M$, whose kernel is zero and cokernel is $M$. Hence $H^0(I;E)=0$, $H^1(I;E)=M$, and all higher groups vanish: in cohomological notation, $R\Gamma(I;E)\simeq M[-1]$. If $M\ne0$, the global-to-stalk map at any point of $(1,2)$ is $0\to M$ and is not surjective. Contractibility of $I$ has not supplied the missing extension property.

4. Where does finite dimension enter the locally closed criterion, and where does local closedness enter?

   *Solution.* Finite dimension makes the compact convex induction terminate, supplies a scalar affine projection, and makes the convex hull of a compact set compact through the $N+1$-point barycenter argument. Local closedness makes $C$ locally compact Hausdorff and makes $\overline C\setminus C$ closed, so the distance cores in (C9) exhaust $C$ by compact subsets. Those properties are used both to construct (C8) and to extend sections of the injective sheaf from a compact subset to a neighborhood. The proof establishes no corresponding theorem after deleting either hypothesis.

## Antecedents and closure boundary

Compare the official Stacks Project at [revision a04446e57ec1](https://github.com/stacks/stacks-project/tree/a04446e57ec1fbc252a871afcec7752fb2807b14). [Tag 09SX](https://stacks.math.columbia.edu/tag/09SX), with the open-extension argument in [Tag 01EA](https://stacks.math.columbia.edu/tag/01EA), proves that injective modules on a ringed space are flabby. [Tag 09T0](https://stacks.math.columbia.edu/tag/09T0) gives their direct-image acyclicity. These apply to the constant sheaf of the coefficient ring; they impose no field or finite-global-dimension hypothesis.

[Tag 09V3](https://stacks.math.columbia.edu/tag/09V3) compares cohomology on a compact Hausdorff subset with the filtered system of its open neighborhoods. Its degree-zero proof extends finitely many local representatives after shrinking their overlaps. The compact-neighborhood lemma in this reading supplies the finite-dimensional neighborhood argument used here. [Tag 09V6](https://stacks.math.columbia.edu/tag/09V6) proves proper base change by reducing the canonical map to the two fibre calculations. In (C5) the scalar projection has compact domain and Hausdorff target, so it is proper; forgetting the coefficient action identifies the underlying sheaf calculation, and the natural restriction maps preserve that action.

The interval subdivision, induction on affine dimension and compatible-lift exhaustion in this reading give the convex extension criterion itself. None is replaced by the assertion that a space is contractible or that its fibres are convex. The final constant-complex calculation uses bounded-below hypercohomology, also treated in [Tag 0BKM](https://stacks.math.columbia.edu/tag/0BKM). The programme proof linked above constructs its finite filtration and identifies the edge using truncation; its composite with the coefficient map is the stated constant-section map. The comparison verifies these specific Stacks foundations, not an exact Stacks import of the whole convex theorem.

The linked Stacks text retains its own GFDL terms. The interval subdivision, affine-dimension induction and compatible-lift exhaustion give the convex theorem here. The linked programme lessons supply the proper-fibre and bounded-below hypercohomology arguments, with the actual restriction and constant-section maps used in these proofs. Further sheaf-operation hypotheses are stated in the prerequisite contracts.
