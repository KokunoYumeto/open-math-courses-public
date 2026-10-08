# Holonomic D-modules and duality

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

A holonomic module can contain both a connection on an open set and a contribution supported on its boundary. Duality reverses how those pieces are attached. On the affine line, the Laurent-polynomial module contains the polynomial connection and has a point module as quotient. Its dual has the point module as submodule and the polynomial connection as quotient. Computing this reversal requires a derived Hom, a dimension shift, and a change from right modules to left modules.

Let $k$ be a field of characteristic zero, and let $X$ be a smooth separated variety of finite type, of pure dimension $d$. Write $\mathcal D_X$ for differential operators, $\omega_X=\bigwedge^d\Omega_X^1$, and $\pi:T^*X\to X$. Modules are left modules and are quasi-coherent over $\mathcal O_X$. The Weyl-algebra calculations below hold over any characteristic-zero field. Analytic comparisons use $k=\mathbb C$.

Prerequisites are [characteristic varieties and cycles](good-filtrations-and-the-characteristic-variety.md), [Bernstein growth and finite length](the-bernstein-filtration-and-holonomic-modules.md), and [holonomic localization](bernstein-sato-polynomials.md). We use cohomological complexes: $K[d]^i=K^{i+d}$, so an Ext group originally in degree $d$ moves to degree zero after $[d]$.

## 1. The holonomic category on a variety

A coherent $\mathcal D_X$-module $M$ is **holonomic** if

\[
\dim\operatorname{Ch}(M)\leq d.
\tag{1.1}
\]

The zero module is included. For nonzero $M$, the independently proved whole-dimension inequality, Theorem 7.2, gives $\dim\operatorname{Ch}(M)\geq d$, so a nonzero holonomic module has characteristic dimension exactly $d$. The proved Gabber theorem and Corollary 7.1 give the stronger componentwise assertion: every component is coisotropic and has dimension at least $d$. Under (1.1) every component therefore has dimension $d$ and is Lagrangian at its smooth points, so the characteristic support is pure of dimension $d$. The finite-length and duality proofs below use the independent whole-dimension bound. No regular-singularity condition is part of holonomicity.

For a short exact sequence of coherent modules,

\[
0\longrightarrow M'\longrightarrow M\longrightarrow M''\longrightarrow0,
\]

the earlier exact-filtration argument gives

\[
\operatorname{Ch}(M)=\operatorname{Ch}(M')\cup\operatorname{Ch}(M'').
\tag{1.2}
\]

Consequently holonomic modules form a Serre subcategory $\operatorname{Hol}(\mathcal D_X)$: submodules, quotients, and extensions remain holonomic. Coherence of submodules is local Noetherianity of $\mathcal D_X$.

Define

\[
D_h^b(\mathcal D_X)=
\{K\in D^b(\mathcal D_X\text{-}\mathrm{Mod}_{\mathrm{qc}}):
H^i(K)\text{ is holonomic for every }i\}.
\tag{1.3}
\]

Here the ambient category consists of quasi-coherent left modules. The Serre property shows that cones, shifts, and standard truncations preserve (1.3). Its standard heart is $\operatorname{Hol}(\mathcal D_X)$. The definition does not require an additional assertion identifying (1.3) with the abstract bounded derived category of that heart.

On $X=\mathbb A^n$, a coherent module corresponds to a finite $A_n(k)$-module. The order–Bernstein comparison proved in the preceding chapters identifies $\dim\operatorname{Ch}(M)$ with its Bernstein growth dimension. Definition (1.1) therefore agrees with the Weyl-algebra definition.

## 2. A connection on a dense open set

### Theorem 2.1. Generic connection structure

For every holonomic $M$, there is a dense open subset $U\subseteq X$ such that $M|_U$ is locally free of finite rank over $\mathcal O_U$, with its integrable connection. The rank can be zero on a component of $U$.

**Proof.** Put $C=\operatorname{Ch}(M)$. For $d>0$, form the projectivization of its nonzero covectors,

\[
\mathbf P C=(C\setminus X)/\mathbb G_m
\subseteq \mathbf P(T^*X).
\tag{2.1}
\]

The copy of $X$ removed here is the zero section. In a cotangent trivialization, $C$ is defined by homogeneous equations in the fiber coordinates, and those equations define the closed subset $\mathbf P C$ of the projective bundle. Each nonempty projectivized component has dimension one less than its corresponding conic component: on a projective coordinate chart, normalizing one nonzero fiber coordinate identifies the inverse image with that chart times $\mathbb G_m$. Hence

\[
\dim\mathbf P C\leq d-1.
\tag{2.2}
\]

The projective-bundle map to $X$ is proper, so

\[
Z=\pi_{\mathbf P}(\mathbf P C)
\tag{2.3}
\]

is closed and has dimension at most $d-1$. Properness here is the usual scheme-theoretic fact that a locally projective morphism is proper; see [Stacks, Tag 01WC](https://stacks.math.columbia.edu/tag/01WC). Since $X$ is pure of dimension $d$, $U=X\setminus Z$ meets every irreducible component densely. On $U$, there are no nonzero characteristic covectors.

We recall why this last assertion gives $\mathcal O_U$-coherence, without replacing the graded module by its reduced support. Work on an affine cotangent trivialization. Its symbol ring is $S=\mathcal O(U)[\xi_1,\ldots,\xi_d]$. A finite graded module $G=\operatorname{gr}M$ supported in the zero section is killed by a power of $J=(\xi_1,\ldots,\xi_d)$: every $\xi_i$ lies in the radical of its annihilator, and finitely many powers give a common bound. Therefore $G$ is finite over $S/J^N$, which is finite over $\mathcal O(U)$. Choose finitely many homogeneous $\mathcal O(U)$-generators of $G$ and lift them to $M$. Subtraction lowers the filtration degree; its lower bound makes this induction terminate. The lifts generate $M$ over $\mathcal O(U)$.

Thus $M|_U$ is $\mathcal O_U$-coherent. Its $\mathcal D_U$-action supplies an integrable connection, and the local-freeness theorem proved in the connection chapter applies in characteristic zero. If $d=0$, $\mathcal D_X=\mathcal O_X$ and the result holds on all of $X$. $\square$

A point module can be zero on this dense open set. For instance $\delta_0$ on the affine line has characteristic fiber over zero, so the construction gives $U=\mathbb G_m$ and $M|_U=0$. The theorem says nothing about extending the connection across the exceptional set.

### Theorem 2.2. Finite length

Every holonomic $\mathcal D_X$-module has finite length.

**Proof.** In (2.4) and (2.5), $\operatorname{CC}$ denotes the dimension-$d$ part of the characteristic cycle: sum only the components of dimension $d$, using their generic local lengths. Write

\[
\operatorname{CC}(M)=\sum_{\Lambda}m_\Lambda[\Lambda],
\qquad
\mu(M)=\sum_\Lambda m_\Lambda.
\tag{2.4}
\]

There are finitely many components, since $X$ is a variety of finite type and the characteristic support is closed and Noetherian. For nonzero holonomic $M$, the independent whole-dimension inequality ensures there is a dimension-$d$ component. Its generic length, and every other $m_\Lambda$ in this sum, is a positive integer. Hence $\mu(M)>0$.

In a short exact sequence of holonomic modules, all characteristic supports have dimension at most $d$, and every nonzero term has whole dimension $d$. The exact-filtration and top-dimensional generic-length theorem therefore gives

\[
\operatorname{CC}(M)=\operatorname{CC}(M')+\operatorname{CC}(M''),
\qquad
\mu(M)=\mu(M')+\mu(M'').
\tag{2.5}
\]

Every nonzero strict subquotient consumes at least one unit of $\mu$. An ascending or descending strict chain in $M$ has at most $\mu(M)$ nonzero successive quotients.

For completeness, a composition series follows by induction on $\mu(M)$. If $M$ is simple, use its one-step series. Otherwise choose a nonzero proper coherent submodule $N$. Both $N$ and $M/N$ are holonomic, and (2.5) makes both multiplicities smaller. By induction each has a finite composition series. Insert the series of $N$ into the inverse images of the series of $M/N$. This gives a series of $M$, with at most $\mu(M)$ simple factors. $\square$

This is a global cycle argument. It requires neither a global map from $X$ to affine space nor an assertion that every étale chart is itself affine space.

## 3. Constructing the dual

For a left module $M$, the sheaf $\mathcal Hom_{\mathcal D_X}(M,\mathcal D_X)$ is naturally a **right** module: multiply the output on the right. Higher derived Hom has the same right action. Let

\[
\operatorname{SC}(N)=N\otimes_{\mathcal O_X}\omega_X^{-1}
\tag{3.1}
\]

denote the inverse of the side-changing equivalence from the connection chapter. This is a left module when $N$ is a right module.

Locally choose a nowhere-zero volume form $\eta$. The corresponding formal transpose is

\[
t_\eta(a)=a\quad(a\in\mathcal O_X),\qquad
t_\eta(\xi)=-\xi-\operatorname{div}_\eta(\xi),
\quad
t_\eta(PQ)=t_\eta(Q)t_\eta(P).
\tag{3.2}
\]

The left action in (3.1), in this trivialization, is $P\cdot(n\otimes\eta^{-1})=(n\,t_\eta(P))\otimes\eta^{-1}$. Changing $\eta$ gives the same intrinsic action; the inverse canonical bundle is precisely what accounts for the change of volume.

Define

\[
\mathbb D_X(M)=
\operatorname{SC}\!\left(
R\mathcal Hom_{\mathcal D_X}(M,\mathcal D_X)
\right)[d].
\tag{3.3}
\]

The tensor with the line bundle is exact. The Hom in (3.3) is internal sheaf Hom, not a derived global-sections vector space.

### Finite local operator resolutions

The finite local resolutions needed for (3.3) can be constructed with a uniform bound. The exact commutative prerequisites are Projective dimension and the Auslander–Buchsbaum formula, Theorem 1.3 and Corollary 4.3, and Regular local rings, Theorem 2.2 and Proposition 3.3. The former proves the Ext criterion for any chosen terminal syzygy. The latter proves the regular-local finite free-resolution bound and polynomial regularity. Their Koszul input is Regular sequences, depth and Cohen–Macaulay modules, Theorem 6.1. The passage from those commutative results to filtered operator modules is proved here. The graded coefficient modules below are finite projective $\mathcal O_X$-modules locally on the base.

**Lemma 3.0 (finite local operator resolutions).** On a smooth variety of dimension $d$, each coherent left or right $\mathcal D_X$-module locally has a finite free operator resolution of length at most $2d$. Its dual (3.3) is bounded coherent in degrees $[-d,d]$. The bound is independent of the module; no global finite free resolution is asserted.

**Proof.** Work on a smooth affine coordinate neighbourhood with tangent basis and write $A=\mathcal O_X(U)$, $D=\mathcal D_X(U)$. The coordinate and good-filtration results of the first lessons give
$\operatorname{gr}D=S=A[\zeta_1,\ldots,\zeta_d]$ and a finite graded symbol module for a coherent input. The local rings of $A$ are regular of dimension at most $d$. One may see this in the same étale coordinate presentation: the local map from a polynomial local ring is flat with zero-dimensional separable fibre; its maximal ideal is generated by the images of the base regular parameters and has the same dimension, so the regular-local criterion applies. The polynomial-local regularity and flat local dimension calculation are the ones proved in the cited commutative lessons. Iterating Proposition 3.3 makes every local ring of $S$ regular of dimension at most $2d$.

Let $N$ be a finite $S$-module. Take $2d$ successive finite free surjections and kernels. Noetherianity keeps the kernels finite and finitely presented. At each prime, the regular-local bound and the syzygy criterion make the final kernel $P$ projective over that local ring. Thus $P$ is finite locally free and is finite projective over $S$. Here is the last implication without a global freeness assumption. Choose a finite principal cover on which $P$ has dual bases. By finite presentation, clear the denominators in each factorization of its identity through a finite free module; a further power of the covering function makes this equality global. The resulting powers still generate the unit ideal. A linear combination of those factorizations factors $\operatorname{id}_P$ through a finite free module, proving that $P$ is a direct summand. Hence every finite $S$-module has projective dimension at most $2d$.

We also need a graded refinement. If a finite, bounded-below graded $S$-module $P$ is projective as an ungraded module, take a finite graded free surjection $G\to P$. Its ungraded splitting has a degree-zero part, which is a graded $S$-linear splitting: on a homogeneous element retain the output of that same degree. Multiplication by a homogeneous element respects this operation. Thus $P$ is graded projective. Put $S_+=(\zeta_1,\ldots,\zeta_d)$ and $E=P/S_+P$. The splitting makes $E$ a finite graded projective $A$-module, nonzero in finitely many degrees. Lift each $E_j$ to $P_j$ by $A$-projectivity. This gives
\[
S\otimes_AE\longrightarrow P.
\tag{3.3a}
\]
It is an isomorphism modulo $S_+$. Graded Nakayama proves surjectivity: a nonzero bounded-below graded cokernel cannot equal $S_+$ times itself, since its least nonzero degree would have to come from smaller degrees. The surjection splits gradedly by projectivity of $P$. Its kernel therefore has zero quotient modulo $S_+$ and vanishes by the same argument. Thus (3.3a) is an isomorphism. After shrinking the affine base near a specified point, the finitely many projective $A$-modules $E_j$ are free. Consequently $P$ has a finite homogeneous free basis on that neighbourhood.

Now choose a good bounded-below filtration on the coherent $D$-module $M$. Lift homogeneous symbol generators to obtain a finite filtered free surjection $L_0\to M$. It is strict: lift the symbol of a section in filtration degree $m$, subtract its lifted image, and repeat in lower degrees; boundedness below terminates the reduction. Give the kernel its induced filtration. Strictness identifies its symbol module with the kernel of the symbol surjection, and that kernel is finite over the Noetherian ring $S$. Repeat this procedure $2d$ times. Taking associated graded gives an actual finite graded free resolution through its terminal syzygy. The preceding projective-dimension bound makes that syzygy projective. By (3.3a), after shrinking the base it has a homogeneous free basis. Lift the basis to the filtered terminal kernel. The resulting finite filtered free map is an isomorphism: leading-symbol reduction proves surjectivity, and a nonzero kernel element would have a nonzero symbol in the kernel of the symbol isomorphism. We have obtained a local resolution of length at most $2d$.

The proof works for right modules too, since the symbol ring is commutative and strict leading-order reduction works on either side. Applying Hom into $D$ to the finite free resolution proves sheaf Ext vanishing above $2d$. Every term of that Hom complex is finite free on the opposite side; Noetherianity makes its cohomology coherent. The shift $[d]$ and the density side change in (3.3) put the dual in $[-d,d]$. Bounded truncation triangles extend local perfection and the corresponding bounds to every bounded coherent complex. $\square$

For analytic differential operators, Theorem 3.0c below proves the stronger local finite free length bound $d$, Ext vanishing above $d$, and stalk global dimension $d$. Its proof includes the analytic coherence and symbol support arguments. The algebraic argument here uses Lemma 3.0.

On finite projectives, evaluation is an isomorphism to the double module dual. Applying it term by term to a bounded projective resolution proves derived biduality. The evaluation has the usual complex signs and is natural in maps of complexes. Side change converts the two right/left Hom constructions into (3.3); the two shifts cancel because Hom reverses shifts. Thus

\[
\mathbb D_X\mathbb D_X(K)\simeq K
\tag{3.4}
\]

for coherent bounded complexes. These local evaluation maps glue because their construction is intrinsic.

### Commutative Ext bounds

The exact commutative prerequisites are the associated-prime and finite-avoidance proofs in Associated primes and primary decomposition, Theorems 1.2 and 2.2 and Solution 8.5, the height formula in Krull dimension and Noether normalization, Theorem 4.3, and the depth-drop and regular-local Cohen–Macaulay proofs in Regular sequences, depth and Cohen–Macaulay modules, Theorems 2.3 and 6.1. The regular-local finite free-resolution bound is the one already used in Lemma 3.0. We prove the additional change-of-rings step rather than assume a grade theorem for the symbol module.

**Lemma 3.0a.** Let $S$ be a regular Noetherian algebra of finite type over a field, pure of dimension $n$, and $N$ a finite $S$-module. Put $c=n-\dim\operatorname{Supp}N$ when $N\ne0$. Then
\[
\operatorname{Supp}\operatorname{Ext}_S^i(N,S)
\subseteq\operatorname{Supp}N\cap
\{\mathfrak p:\operatorname{ht}\mathfrak p\geq i\},
\qquad
\dim\operatorname{Supp}\operatorname{Ext}_S^i(N,S)\leq n-i,
\tag{3.4a}
\]
and $\operatorname{Ext}_S^i(N,S)=0$ for $i<c$. For $N=0$ all these Ext groups vanish. No Cohen–Macaulay hypothesis on $N$ is required.

**Proof.** A resolution by finite free modules exists by repeatedly taking a finite generating set and its finite kernel. Its Hom complex shows that Ext is finite and commutes with localization. At a prime $\mathfrak p$, it computes
\[
\operatorname{Ext}_S^i(N,S)_{\mathfrak p}
=\operatorname{Ext}_{S_{\mathfrak p}}^i
(N_{\mathfrak p},S_{\mathfrak p}).
\tag{3.4b}
\]
This is zero if $N_{\mathfrak p}=0$. Otherwise the regular local ring $S_{\mathfrak p}$ has dimension $\operatorname{ht}\mathfrak p$ and the earlier finite free-resolution bound makes it zero for $i>\operatorname{ht}\mathfrak p$. This proves the support inclusion.

We first supply the regular-sequence input for the lower vanishing. Let $R$ be regular local and $I\subsetneq R$ an ideal all of whose containing primes have height at least $r$. It contains an $R$-regular sequence of length $r$. Indeed, suppose $a_1,\ldots,a_j\in I$ have been chosen, with $j<r$, and set $Q_j=R/(a_1,\ldots,a_j)$. If $\mathfrak q$ is associated to $Q_j$, an element with annihilator $\mathfrak q$ remains nonzero on localization at $\mathfrak q$. It is killed there by the maximal ideal, so $(Q_j)_{\mathfrak q}$ has depth zero. The sequence remains regular in $R_{\mathfrak q}$ and its final quotient is nonzero. The regular-local Cohen–Macaulay theorem and the exact depth drop give
\[
0=\operatorname{depth}_{R_{\mathfrak q}}(Q_j)_{\mathfrak q}
=\operatorname{ht}_R\mathfrak q-j.
\tag{3.4c}
\]
Thus every associated prime of $Q_j$ has height $j$ and none contains $I$. Finite prime avoidance chooses $a_{j+1}\in I$ outside their union. The zero-divisor theorem makes this element injective on $Q_j$, and Nakayama keeps the quotient nonzero because $a_{j+1}$ lies in the maximal ideal. Induction proves the claim; the intermediate quotient rings need not be regular.

Next let $a\in R$ be a nonzerodivisor, put $B=R/(a)$, and assume $aL=0$. We prove
\[
\operatorname{Hom}_R(L,R)=0,
\qquad
\operatorname{Ext}_R^i(L,R)
\simeq\operatorname{Ext}_B^{i-1}(L,B)\quad(i\geq1).
\tag{3.4d}
\]
Hom vanishes since its image would be killed by $a$ in $R$. Here is the full change-of-rings argument for the higher groups. All the rings here are algebras over the original field $k$. For any $k$-vector space $V$, the $R$-module $\operatorname{Hom}_k(R,V)$, with $(r\phi)(s)=\phi(rs)$, is injective: evaluation at $1$ identifies Hom into it with the exact functor $\operatorname{Hom}_k(-,V)$. Every $R$-module $E$ embeds in one by $e\mapsto(s\mapsto se)$, taking $V=E$. Embedding successive cokernels constructs an injective resolution $J^\bullet$ of $R$ in nonnegative degrees.

These injectives compute the same Ext as free resolutions. To check this, use $\operatorname{Hom}_R(F_p,J^q)$ for a free resolution $F_\bullet\to L$. Exactness in either direction leaves, respectively, the complexes $\operatorname{Hom}_R(F_\bullet,R)$ and $\operatorname{Hom}_R(L,J^\bullet)$. Each total degree has finitely many entries. Filtering the total complex by rows or columns and successively removing these exact entries gives the same cohomology, with no infinite-totalization issue.

Set $H^\bullet=\operatorname{Hom}_R(B,J^\bullet)$. Each $H^q$ is injective over $B$, since Hom into it is $\operatorname{Hom}_R(-,J^q)$ on $B$-modules. The free resolution $0\to R\xrightarrow{a}R\to B\to0$ and its dual $R\xrightarrow{a}R$ show
\[
H^q(H^\bullet)=0\quad(q\ne1),\qquad H^1(H^\bullet)=B.
\tag{3.4e}
\]
Consequently $H^0\to H^1$ is injective and splits because $H^0$ is injective over $B$. Remove this contractible two-term direct summand. The remaining degree-one term is still injective, its kernel is $B$, and the higher terms form an injective resolution of $B$, starting in degree one. Finally
$\operatorname{Hom}_R(L,J^\bullet)=\operatorname{Hom}_B(L,H^\bullet)$.
Removing the same contractible summand proves (3.4d), with the claimed shift.

Iterating (3.4d) along an $R$-regular sequence $a_1,\ldots,a_r$ annihilating $L$ makes $\operatorname{Ext}_R^i(L,R)=0$ for $i<r$: each step removes one degree, and negative Ext degrees are zero.

Apply this at $R=S_{\mathfrak p}$ with $N_{\mathfrak p}\ne0$ and $I=\operatorname{ann}_R N_{\mathfrak p}$. Finiteness gives $\operatorname{Supp}N=V(\operatorname{ann}_S N)$ and $I=(\operatorname{ann}_S N)_{\mathfrak p}$. Both statements follow by taking a product of denominators killing a finite generating set. Every prime containing $I$ corresponds to a support prime $\mathfrak q\subseteq\mathfrak p$. Its height in $S_{\mathfrak p}$ equals its height in $S$, since all prime chains below $\mathfrak q$ are already contained in $\mathfrak p$.

For a regular finite-type ring the irreducible components are disjoint: two minimal primes below one prime would contradict the fact that its regular local ring is a domain. The finitely many components are therefore open and closed. On each dimension-$n$ domain component, the earlier height formula gives $\dim(S/\mathfrak q)=n-\operatorname{ht}\mathfrak q$. Hence every support prime has height at least $c$, and $c$ is the minimum of those heights. The regular-sequence construction supplies a length-$c$ sequence in $I$. The preceding Ext shift makes (3.4b) vanish below $c$ at every prime, proving the lower vanishing. The same height formula applied to the support inclusion proves the dimension bound in (3.4a). $\square$

### Filtered Ext comparison

**Lemma 3.0b (filtered Ext comparison).** Let \(X\) be a smooth variety of pure dimension \(d\), and let \(M\) be a coherent left \(\mathcal D_X\)-module. On each sufficiently small affine coordinate neighbourhood \(U\), choose a good filtration of \(M|_U\). Put
\[
\begin{aligned}
A&=\mathcal O_X(U),\qquad D=\mathcal D_X(U),\\
S&=\operatorname{gr}D=A[\zeta_1,\ldots,\zeta_d],\\
N&=\operatorname{gr}M(U).
\end{aligned}
\]
There is a good filtration of the right \(D\)-module
\(\operatorname{Ext}_D^i(M(U),D)\) such that its associated graded module is a graded \(S\)-subquotient of \(\operatorname{Ext}_S^i(N,S)\). More precisely, the filtered Hom complex constructed in the proof has pages
\[
\begin{aligned}
E_1^{p,i}&=\operatorname{Ext}_S^i(N,S)_p,\\
d_r&:E_r^{p,i}\longrightarrow E_r^{p-r,i+1},
\end{aligned}
\tag{3.4f}
\]
and there is a single finite page, independent of \(p\) and \(i\), at which
\[
E_r^{p,i}\ \simeq\
\operatorname{gr}_p\operatorname{Ext}_D^i(M(U),D).
\tag{3.4g}
\]
These identifications describe an exhaustive, bounded-below filtration of the actual Ext module. The assertion holds with left and right exchanged.

Consequently, on \(X\),
\[
\operatorname{Ch}
 \bigl(\mathcal Ext_{\mathcal D_X}^{\,i}(M,\mathcal D_X)\bigr)
 \ \subseteq\ \operatorname{Ch}(M),
\tag{3.4h}
\]
and, writing \(t=\dim\operatorname{Ch}(M)\) for nonzero \(M\),
\[
\begin{split}
\mathcal Ext_{\mathcal D_X}^{\,i}(M,\mathcal D_X)&=0
       &&(i<2d-t),\\
\dim\operatorname{Ch}
 \bigl(\mathcal Ext_{\mathcal D_X}^{\,i}(M,\mathcal D_X)\bigr)
 &\leq \min\{t,\,2d-i\}.
\end{split}
\tag{3.4i}
\]
The characteristic variety of a right module uses its right good filtration. Formula (3.4i) also includes Ext vanishing above \(2d\); the dimension of the empty support is taken to be \(-\infty\). All assertions are componentwise when the components of \(X\) have different dimensions.

**Proof.** We first prove the filtered assertion, without using any commutative grade or support estimate.

Shrink \(U\) as in Lemma 3.0. We have a finite resolution
\[
0\longrightarrow L_n\longrightarrow\cdots\longrightarrow
L_0\longrightarrow M(U)\longrightarrow0,
\qquad n\leq 2d,
\tag{3.4j}
\]
by finite filtered free left \(D\)-modules. Its maps are strict, and
\(\operatorname{gr}L_\bullet\) is a finite graded free resolution of \(N\).
All filtrations are increasing, exhaustive and zero in sufficiently negative degrees. Their pieces are finite \(A\)-modules. Affine sections compute the sheaf construction: the terms, kernels and images of these complexes are quasi-coherent as \(\mathcal O_U\)-modules, and sections of quasi-coherent modules on \(U\) are exact.

Let
\[
C^i=\operatorname{Hom}_D(L_i,D),\qquad
\partial^i:C^i\longrightarrow C^{i+1}
\]
be the finite dual cochain complex. It is a complex of right \(D\)-modules; the differential is precomposition with the resolution differential. Define
\[
F_pC^i=\{\phi: \phi(F_qL_i)\subseteq F_{p+q}D
                       \text{ for every }q\}.
\tag{3.4k}
\]
If a free basis vector \(e_j\) of \(L_i\) has filtration degree \(a_j\), then (3.4k) says
\(\phi(e_j)\in F_{p+a_j}D\). Thus \(C^i\) is a finite filtered free right module, with dual basis degrees \(-a_j\). In particular its filtration is good and bounded below. The differential preserves filtration, and evaluation on the basis gives
\[
\operatorname{gr}C^\bullet
 =\operatorname{Hom}_S(\operatorname{gr}L_\bullet,S),
\qquad
H^i(\operatorname{gr}C^\bullet)
 =\operatorname{Ext}_S^i(N,S).
\tag{3.4l}
\]
The Hom on the right includes all homogeneous internal degrees. Every \(S\)-linear map from a finite graded free module is a finite sum of homogeneous maps, so this also computes ordinary Ext with its internal grading.

We need a bound on the filtration lost when lifting a boundary. For each \(i\), put
\(B^i=\operatorname{im}\partial^{i-1}\subseteq C^i\), and give it two filtrations:
\[
G_pB^i=B^i\cap F_pC^i,\qquad
Q_pB^i=\partial^{i-1}(F_pC^{i-1}).
\tag{3.4m}
\]
Always \(Q_pB^i\subseteq G_pB^i\). Both filtrations are good. Indeed,
\(\operatorname{gr}_GB^i\) embeds in the finite \(S\)-module
\(\operatorname{gr}C^i\); it is finite because \(S\) is Noetherian.
The associated graded map from \(C^{i-1}\) onto the image with filtration \(Q\) is surjective, so \(\operatorname{gr}_QB^i\) is finite as well.
The filtration pieces in both cases are finite \(A\)-modules: for \(G\) they are submodules of \(F_pC^i\), and for \(Q\) they are images of \(F_pC^{i-1}\). Both filtrations are exhaustive and bounded below.

Here finiteness of the associated graded really gives finite weighted generators. Lift finitely many homogeneous symbol generators to elements \(b_j\) of degrees \(a_j\). For an element of filtration degree \(p\), express its symbol using those generators, lift the coefficients, and subtract. The remainder has degree at most \(p-1\). Since the filtration is bounded below, repetition terminates and expresses the original element using coefficients of orders at most \(p-a_j\). Apply this to filtration \(G\). Exhaustiveness of \(Q\) puts each resulting \(b_j\) in some \(Q_{a_j+c_i}B^i\), with a common integer \(c_i\geq0\). Compatibility with the operator filtration then gives
\[
G_pB^i\subseteq Q_{p+c_i}B^i
                         \qquad\text{for every }p.
\]
There are only finitely many terms. Choose \(c\geq0\) dominating all their \(c_i\), taking \(c_i=0\) for zero images. We have proved the uniform lifting statement
\[
b\in B^i\cap F_pC^i
 \quad\Longrightarrow\quad
b=\partial a\text{ for some }a\in F_{p+c}C^{i-1}.
\tag{3.4n}
\]
This bound depends on the chosen finite filtered complex, not on \(p\) or \(i\).
No assertion about proper direct images or holonomic duality entered its proof.

We now construct the pages and their transitions explicitly. Extend \(C^\bullet\) by zero outside its finite range and, for \(r\geq0\), set
\[
Z_r^{p,i}
 =\{x\in F_pC^i: \partial x\in F_{p-r}C^{i+1}\}.
\]
In particular \(Z_0^{p,i}=F_pC^i\). For \(r\geq1\), define
\[
E_r^{p,i}
 =\frac{Z_r^{p,i}}
 {\,Z_{r-1}^{p-1,i}
       +\partial Z_{r-1}^{p+r-1,i-1}\,}.
\tag{3.4o}
\]
Both denominator terms lie in the numerator. Applying \(\partial\) gives a well-defined map \(d_r\) as in (3.4f): changing a representative by an element of the first denominator term changes its differential by a denominator boundary in the target; changing it by a boundary changes its differential by zero. Also \(d_r^2=0\).
For \(r=1\), (3.4o) is exactly the cycle and boundary quotient of
\(\operatorname{gr}_pC^\bullet\), proving the first equality in (3.4f).

For completeness, the passage from page \(r\) to page \(r+1\) is a quotient calculation. If \(d_r[x]=0\), then
\[
\partial x=u+\partial v,\qquad
u\in Z_{r-1}^{p-r-1,i+1},\quad
v\in Z_{r-1}^{p-1,i}.
\]
Replacing \(x\) by \(x-v\) keeps its class on page \(r\) and puts it in
\(Z_{r+1}^{p,i}\). This proves that the latter group maps onto the kernel of \(d_r\).
An incoming \(d_r\)-boundary has the form \(\partial a\), with
\(a\in Z_r^{p+r,i-1}\). To identify the remaining quotient, suppose
\(x\in Z_{r+1}^{p,i}\) represents such an incoming boundary. Then
\[
x=\partial a+v+\partial b,\qquad
v\in Z_{r-1}^{p-1,i},\quad
b\in Z_{r-1}^{p+r-1,i-1}.
\]
Since \(\partial v=\partial x\in F_{p-r-1}C^{i+1}\), actually
\(v\in Z_r^{p-1,i}\). Moreover
\(a+b\in Z_r^{p+r,i-1}\).
Thus precisely the denominator
\(Z_r^{p-1,i}+\partial Z_r^{p+r,i-1}\) is removed. Conversely each of its terms maps to zero or to an incoming boundary on page \(r\). This proves
\[
E_{r+1}^{p,i}\simeq H^{p,i}(E_r,d_r)
\tag{3.4p}
\]
with exactly the indices in (3.4o).

These are pages of graded \(S\)-modules. For a homogeneous symbol
\(a\in S_k\), lift \(a\) to \(P\in F_kD\) and put
\([x]a=[xP]\in E_r^{p+k,i}\).
Right \(D\)-linearity of \(\partial\) preserves all the defining groups.
Replacing \(P\) by another lift changes \(xP\) by an element of
\(Z_{r-1}^{p+k-1,i}\), which is in the denominator. The same argument makes multiplication and addition independent of lifts, and the commutativity of \(S=\operatorname{gr}D\) gives the graded \(S\)-module structure.
The maps \(d_r\) are \(S\)-linear of internal degree \(-r\).
Therefore
\(\bigoplus_pE_{r+1}^{p,i}\) is an \(S\)-subquotient of
\(\bigoplus_pE_r^{p,i}\). Each is finite, starting with (3.4l).

There is uniform stabilization, even though the filtration has no upper bound.
Take \(r\geq c+1\) and \(x\in Z_r^{p,i}\).
Its differential is a boundary in \(F_{p-r}C^{i+1}\).
By (3.4n), choose
\[
y\in F_{p-r+c}C^i,\qquad \partial y=\partial x.
\]
Since \(p-r+c\leq p-1\), this \(y\) lies in
\(Z_{r-1}^{p-1,i}\). Hence \(x-y\) is a genuine cycle in \(F_pC^i\)
and represents the same class on page \(r\).
Every class on every page \(r\geq c+1\) thus has a genuine cycle representative; all further \(d_r\) vanish.

This also identifies the stable page with the actual cohomology filtration.
Write \(Z^i=\ker\partial^i\) and define
\[
F_pH^i(C^\bullet)
 =\operatorname{im}(Z^i\cap F_pC^i\longrightarrow Z^i/B^i).
\tag{3.4q}
\]
For \(r\geq c+1\), a genuine cycle in \(F_pC^i\) defines a map
\[
\operatorname{gr}_pH^i(C^\bullet)\longrightarrow E_r^{p,i}.
\tag{3.4r}
\]
It is well defined. A lower-filtration cycle belongs to
\(Z_{r-1}^{p-1,i}\). If \(b\in B^i\cap F_pC^i\), (3.4n) writes
\(b=\partial a\) with
\(a\in F_{p+c}C^{i-1}\subseteq F_{p+r-1}C^{i-1}\).
Since \(\partial a\in F_pC^i\), this \(a\) belongs to
\(Z_{r-1}^{p+r-1,i-1}\), and \(b\) is also zero on page \(r\).
Surjectivity of (3.4r) is the preceding genuine-cycle correction.
For injectivity, a genuine cycle that is zero on page \(r\) has the form
\[
z=u+\partial v,\qquad u\in Z_{r-1}^{p-1,i}.
\]
Then \(\partial u=\partial z=0\), so \(u\) is a genuine lower-filtration cycle. Its cohomology class is zero in the associated graded of (3.4q), as is that of \(z\).
This proves (3.4g), compatibly with all later pages and with the \(S\)-actions.

The filtration (3.4q) is exhaustive and bounded below. Each of its pieces is the finite \(A\)-module
\[
(Z^i\cap F_pC^i)/(B^i\cap F_pC^i).
\]
Its associated graded is a finite \(S\)-module, by (3.4p) and (3.4r).
It is therefore a good filtration. Repeated use of (3.4p), ending at the single page \(c+1\), proves that this associated graded is an \(S\)-subquotient of \(\operatorname{Ext}_S^i(N,S)\).
In particular, if the latter Ext module is zero, the former is zero. Exhaustiveness and boundedness below then force \(H^i(C^\bullet)=0\): a nonzero class has a least filtration degree and a nonzero symbol there. Formulas (3.4n)–(3.4r) thus prove convergence to actual cohomology in every filtration degree at the same finite page.

We finish with the geometric consequences. Lemma 3.0a applies to the regular ring \(S\) of dimension \(2d\). If \(V=\operatorname{Supp}_S N\) and
\(g=\operatorname{codim}V=2d-\dim V\), it gives
\[
\begin{aligned}
\operatorname{Ext}_S^i(N,S)&=0\quad(i<g),\\
\operatorname{Supp}_S\operatorname{Ext}_S^i(N,S)&\subseteq V,\\
\dim\operatorname{Supp}_S\operatorname{Ext}_S^i(N,S)&\leq2d-i.
\end{aligned}
\tag{3.4s}
\]
The zero module is handled separately. Subquotients have contained support, so the filtered comparison gives
\[
\operatorname{Supp}_S\operatorname{gr}\operatorname{Ext}_D^i(M(U),D)
\subseteq\operatorname{Supp}_S\operatorname{Ext}_S^i(N,S)
\subseteq V.
\]
It gives vanishing below \(g\), and dimension at most
\(\min\{\dim V,2d-i\}\), on every such affine \(U\).
For a global nonzero \(M\), \(\dim V\leq t\), so the local lower bound
\(g=2d-\dim V\) is at least \(2d-t\).
The filtrations just constructed need not be the same on overlapping neighbourhoods. Theorem 2.1 of the good-filtrations lesson proves that the reduced symbol support is independent of the good filtration and transforms intrinsically under coordinate changes. Thus these local inclusions and dimension estimates give (3.4h)–(3.4i) for the sheaf Ext on \(X\).
The construction for right input modules uses a finite filtered free right resolution and its left Hom complex; every formula and every bound is unchanged. \(\square\)

### Analytic local operator resolutions

**Theorem 3.0c.** On a complex manifold $X$ of dimension $d$, the analytic operator sheaf $\mathcal D_X$ is left and right coherent. Every coherent left or right operator module has, near each point, a finite free resolution of length at most $d$. In particular

\[
\mathcal Ext^i_{\mathcal D_X}(M,\mathcal D_X)=0\qquad(i>d).
\tag{3.4t}
\]

For every point, on both sides,

\[
\operatorname{gl.dim}\mathcal D_{X,x}=d.
\tag{3.4u}
\]

The last statement includes arbitrary stalk modules: they have projective resolutions of length at most $d$. The finite free assertion concerns coherent modules on a neighborhood.

The exact analytic prerequisites are the preparation/division proof, Noetherianity in Lemma 2.1, and the coherent-module arguments in Proposition 1.1 of AG-QC, Complex analytic spaces and analytification; the dimension and regularity proof in The local ring of holomorphic germs, Proposition 1.1; and the uniform Oka coherence theorem, Theorem 2.1. The commutative inputs are AG-CA 03, Theorem 2.1, AG-CA 11, Theorem 3.1, AG-CA 14, Theorem 2.2 and Theorem 3.2, and AG-CA 19, Theorems 3.1–3.2. The regular-system-of-parameters property is proved in AG-CA 12, Theorem 6.1; the needed Koszul exactness is proved below. We use Gabber involutivity, Theorem 7.0 in its full Noetherian rational-symbol scope.

For the analytic characteristic germ we use the proved local parametrization, analytic Nullstellensatz and dense smooth-locus theorems, Theorems 4.1, 5.1 and 5.4, and Cartan coherence, Theorem 1.1. The finite-field input used by the parametrization proof is supplied immediately below. The remaining operator, completion and homological steps are proved here. Kashiwara's freely accessible [thesis translation, Section 3.1](https://www.numdam.org/article/MSMF_1995_2_63__R1_0.pdf), Theorem 3.1.5 and Remark 6, is further reading for the same Ext and global-dimension statements.

**Proof.**

#### The finite-field input for analytic parametrization

**Field lemma.** Every finite field extension in characteristic zero has a primitive element and has as many embeddings in an algebraic closure as its degree.

**Proof.** Let E/F be a finite extension in characteristic zero and fix an algebraic closure containing E. An irreducible polynomial p has no repeated roots: p' is nonzero of smaller degree, so a common divisor of p and p' would contradict irreducibility. If E is obtained by adjoining finitely many algebraic generators, every embedding of the preceding field extends to exactly as many embeddings of the next field as the degree of that adjunction: choose one of the distinct roots of the transported minimal polynomial and use evaluation on the simple extension. Multiplying these counts along the tower shows that E has exactly [E:F] distinct F-embeddings in the algebraic closure.

If E=F(α,β), two distinct such embeddings cannot agree on both α and β. For each pair of embeddings, equality on α+cβ excludes at most one c∈F: when their β-images differ it is a single linear equation in c, and when those images agree their α-images differ and there is no solution. There are finitely many pairs. The field F is infinite, since it contains Q, so choose c outside this finite exceptional set. The element θ=α+cβ then has [E:F] distinct images. Its minimal polynomial has at least that many distinct roots, hence degree at least [E:F]; the reverse inequality follows from F(θ)⊂E. Equality of finite vector-space dimensions gives F(θ)=E. Iterating the two-generator argument proves the assertion for any finite list. A finite extension has such a list because a finite basis generates it as a field. This proves the primitive-element and embedding counts used in the local analytic parametrization argument.

The countable hyperplane avoidance used by the analytic parametrization proof also has an elementary proof. Start in any open ball in a finite-dimensional complex vector space. Choose a closed ball inside it disjoint from the first proper linear hyperplane. Recursively choose a closed ball inside the preceding ball’s interior, disjoint from the next hyperplane, and of radius at most $2^{-n}$. This is possible because a proper hyperplane has empty interior and is closed. The centers are Cauchy, and completeness gives a point in every one of the nested closed balls. That point avoids every listed hyperplane. Since the starting open ball was arbitrary, the complement of their union is dense.

#### Koszul exactness for the resolution argument

Let $a_1,\ldots,a_r$ be a regular sequence in a commutative ring $T$. The tensor product of the two-term complexes $[T\xrightarrow{a_j}T]$ has homology only in degree zero, where it is $T/(a_1,\ldots,a_r)$. For one element this is the injectivity of multiplication by $a_1$ and its displayed cokernel. Inductively, the new tensor product is the mapping cone of multiplication by $a_r$ on the previous complex. Its homology exact sequence leaves only the kernel and cokernel of multiplication by $a_r$ on $T/(a_1,\ldots,a_{r-1})$: the kernel is zero by regularity and the cokernel is the new quotient. This exact sequence can be obtained directly by writing the cone as the direct sum of the previous complex and its shifted copy: projection onto the shifted copy and inclusion of the first copy are exact in every degree, and lifting a cycle computes the connecting map as multiplication by $a_r$. Thus the induction proves the Koszul assertion, including the empty sequence. In the polynomial symbol ring the successive quotients by the $\zeta_j$ are polynomial rings with fewer variables, so these variables form a regular sequence.

#### Analytic local algebra and relative completion

At a coordinate point put
\[
H=\mathbb C\{x_1,\ldots,x_d\},\quad
S=H[\zeta_1,\ldots,\zeta_d],\quad
P=(x,\zeta),\quad R=S_P,\quad
B=\mathbb C\{x,\zeta\},\quad Q=(\zeta).
\tag{3.4v}
\]
The preparation/division proof and Lemma 2.1 in the earlier AG-QC analytic lesson make \(H\) and \(B\) Noetherian. For clarity, the induction is as follows. In a nonzero ideal choose a germ whose first nonzero homogeneous part is nonzero on a chosen last coordinate axis. Preparation gives a monic polynomial in that variable in the ideal. Division makes its quotient ring finite free over the convergent ring in one fewer variable. An ideal in that quotient is finite by induction, and its lifts together with the monic polynomial generate the original ideal.

The maximal ideal of \(\mathbb C\{u_1,\ldots,u_n\}\) is generated by the coordinates: subtract the constant term and factor every positive-degree monomial by one coordinate, preserving convergence on a smaller polydisc. Their classes are independent modulo its square by first Taylor coefficients. The chain of coordinate prime ideals has length \(n\); the height bound for an ideal generated by \(n\) elements gives the reverse dimension inequality. Thus this is a regular local ring of dimension \(n\). In particular \(H\) has dimension \(d\), \(B\) dimension \(2d\), and their prime localizations are regular by AG-CA 14, Theorem 3.2.

For completeness, polynomial Noetherianity follows from the elementary leading-coefficient argument. If \(A\) is Noetherian and \(I\subset A[t]\), the leading coefficients of its polynomials, together with zero, form an ideal: multiply lower-degree polynomials by powers of \(t\) to compare degrees. Choose finitely many generating leading coefficients, realized by polynomials \(f_j\in I\), and let \(N\) exceed their degrees. Every element of \(I\) of degree at least \(N\) can have its leading term removed by a combination of \(t\)-multiples of the \(f_j\). The remaining elements of \(I\) of degree below \(N\) form an \(A\)-submodule of the finite free coefficient module \(A^N\), and are finitely generated. These generators and the \(f_j\) generate \(I\), by finite descending-degree reduction. Iterate in the \(d\) variables to make \(S\) Noetherian.

The local ring \(R=S_P\) is directly regular of dimension \(2d\): its maximal ideal has the \(2d\) coordinate generators, and successively setting \(x_1,\ldots,x_d,\zeta_1,\ldots,\zeta_d\) to zero gives a prime chain of length \(2d\). Each quotient before localization is a convergent domain with polynomial variables, so these prime ideals remain proper after localization. No global polynomial-dimension equality is needed.

**Lemma 3.0c.1 (relative analytification at zero).** The map \(R\to B\) is faithfully flat. Both rings have \(Q\)-adic completion
\[
C=H[[\zeta_1,\ldots,\zeta_d]].
\tag{3.4w}
\]

**Proof.** Taylor truncation in \(\zeta\) gives
\[
B/Q^r=H[\zeta]/(\zeta)^r.
\]
Every finite list of coefficient germs has a common coordinate neighbourhood, so every truncated polynomial occurs. Conversely all remaining Taylor terms belong to \(Q^r\); this can be checked by collecting monomials divisible by a monomial of total \(\zeta\)-degree \(r\), with convergence after shrinking. In \(R\), every inverted polynomial has a unit constant \(\zeta\)-coefficient in \(H\). Its inverse in the truncated polynomial ring is a finite geometric series. Consequently localization does not change this same quotient. Taking inverse limits proves (3.4w).

The exact earlier completion theorem applies to the two Noetherian local rings and the ideal \(Q\) in their maximal ideals. It makes \(C\) faithfully flat over both \(R\) and \(B\). For an \(R\)-module injection, the kernel of its base change to \(B\), tensored further with \(C\), vanishes because \(C\) is flat over \(R\). Faithfulness over \(B\) kills that kernel. Thus \(B\) is flat over \(R\). If an \(R\)-module becomes zero over \(B\), it becomes zero over \(C\), and faithfulness over \(R\) kills it. This proves full faithful flatness, including arbitrary modules. \(\square\)

**Lemma 3.0c.2 (homogeneous radicals and detection).** If \(J\subset S\) is a homogeneous radical ideal, \(JB\) is radical. A nonzero finite graded \(S\)-module remains nonzero over \(B\).

**Proof.** Exact completion of the finite module \(S/J\) gives
\[
C/JC=\prod_{r\ge0}(S/J)_r.
\tag{3.4x}
\]
Indeed, modulo \((\zeta)^r\), a homogeneous quotient has exactly the direct sum of its degree pieces below \(r\). The inverse limit is their product, with finite convolution in each degree. A nonzero series has a first nonzero homogeneous coefficient \(a_k\). Its \(n\)-th power has first coefficient \(a_k^n\ne0\), since \(S/J\) is reduced. Therefore (3.4x) is reduced. Faithfully flat completion of \(B/JB\) embeds it into \(C/JC\), so \(B/JB\) is reduced as well.

The annihilator of a graded module is homogeneous: apply an annihilator to homogeneous elements and compare distinct output degrees. If a finite graded \(V\) vanished after localization at \(P\), one denominator \(f\notin P\) would kill a finite generating set. Every homogeneous component of \(f\) would be an annihilator. Its degree-zero component is a unit of \(H\), a contradiction. Thus \(V_P\ne0\); Lemma 3.0c.1 gives \(V\otimes_S B\ne0\). This applies to shifted or bounded-below graded modules too.

The radical of a homogeneous ideal is homogeneous. One proof is to apply scaling \(\zeta\mapsto t\zeta\) for finitely many distinct nonzero complex \(t\), and invert the coefficient Vandermonde matrix. The nilradical of the graded quotient is invariant under these automorphisms, and its ideal property puts each homogeneous component in that nilradical. \(\square\)

The homogeneity hypothesis supplies the lowest-degree argument, and faithful relative completion detects the resulting reducedness after analytic extension.

#### Uniform symbol relations and operator coherence

Finite polynomial relations below give generators on one neighbourhood for every symbol degree.

**Lemma 3.0c.3 (one neighbourhood for all symbol degrees).** The kernel of a homogeneous matrix between finite graded free sheaves over \(\mathcal O_U[\zeta]\) has, near each base point, finitely many homogeneous polynomial generators, on a single neighbourhood for every degree.

**Proof.** At the base point \(x\), its stalk kernel \(L_x\) is finite over the Noetherian ring \(S_x\). Choose homogeneous generators \(\lambda_1,\ldots,\lambda_s\), and represent all their polynomial coefficient germs and the identities they satisfy on one base neighbourhood. Analytify the matrix on a product neighbourhood of \((x,0)\) in \(U\times\mathbb C^d\). Lemma 3.0c.1 and localization identify its analytic kernel stalk with \(L_x\otimes_{S_x}B_{(x,0)}\). The \(\lambda_a\) generate this stalk.

The finite shifts in source and target are kept: a homogeneous map has degree zero between those shifted free modules, and every \(\lambda_a\) is chosen homogeneous in its source shift. Forgetting the shifts for analytic extension gives the same finite matrix.

Oka's theorem makes the analytic kernel and its quotient by the analytic span of these finitely many \(\lambda_a\) coherent. The quotient has zero stalk at \((x,0)\), hence is zero on a neighbourhood: a finite generating list consists of germs zero at that point, so all its sections vanish on one smaller neighbourhood. Choose a product \(U'\times V\) in it. At every \((y,0)\) with \(y\in U'\), faithful-flat base change gives the analogous analytic kernel \(L_y\otimes B_{(y,0)}\). Write \(Q_y\) for the cokernel of the polynomial \(\lambda_a\) in \(L_y\), a finite graded module over the coefficient-germ polynomial ring \(S_y\). First localize this polynomial ring at \(P_y=(\mathfrak m_y,\zeta)\); then extend to the analytic stalk \(B_{(y,0)}\). Analytic vanishing and Lemma 3.0c.1 kill \((Q_y)_{P_y}\). Graded zero-section detection in Lemma 3.0c.2 then kills \(Q_y\) itself. These are distinct steps, and neither treats \(S_y\) as already localized at \(P_y\). Therefore the same list generates \(L_y\) in every degree, for all \(y\in U'\). There is no degree-dependent shrinking. \(\square\)

In coordinates, analytic operators have the finite PBW expressions
\[
D=\mathcal D_{X,x}
=\left\{\sum_{\alpha}a_\alpha(x)\partial_x^\alpha:
 a_\alpha\in H,\ \text{finitely many }\alpha\right\}.
\tag{3.4y}
\]
The relations are \([\partial_i,a]=\partial_i(a)\), \([\partial_i,\partial_j]=0\); the order symbol is \(S\). Uniqueness can be checked by applying an alleged zero operator to \(e^{\langle t,x\rangle}\) for all constant \(t\): the polynomial \(\sum_\alpha a_\alpha(x)t^\alpha\) is zero. The ordinary order-reduction proof makes \(D\) Noetherian on both sides: the symbols of an ideal or a submodule of a finite free module form a finite \(S\)-module; lift finite homogeneous generators, and subtract matching leading symbols until bounded-below order terminates. The same proof gives good filtrations of finite stalk modules and their induced submodules. Each order piece is finite free over \(H\).

**Lemma 3.0c.4 (uniform operator images and relations).** The kernel and image of a finite operator matrix are locally finitely generated. The image, as a submodule of a filtered finite free module, has a locally good induced filtration.

**Proof.** Write the matrix as \(\phi:F\to F'\) between finite free operator sheaves, with fixed finite shifts of their order filtrations. At \(x\), the induced symbol of \(I_x=\operatorname{im}\phi_x\) is a submodule of \(\operatorname{gr}F'_x\), hence finite. Choose \(g_j\in I_x\) whose leading symbols generate it and let \(G\) be the shifted free module with basis \(e_j\) of those orders. The map \(\psi:G\to F'\), \(e_j\mapsto g_j\), is strict onto \(I_x\) by descending-order reduction.

Choose \(v:G\to F\) with \(\phi v=\psi\), and \(u:F\to G\) with \(\psi u=\phi\) at \(x\). Such \(v\) exists by the choice of \(g_j\); such \(u\) exists because strict reduction expresses the original finitely many matrix columns in the \(g_j\). These are finitely many operator identities, so they hold on one neighbourhood after representing the coefficients. In particular \(\operatorname{im}\phi=\operatorname{im}\psi\) there.

Let \(\lambda_a\) be homogeneous generators of
\(\ker(\operatorname{gr}\psi_x)\), and lift them to filtered elements \(\widetilde\lambda_a\in G_x\) of their degrees \(k_a\). Their images under \(\psi\) have order below \(k_a\). Strict reduction at \(x\) supplies \(w_a\in G_{k_a-1,x}\) with
\(\psi(w_a)=\psi(\widetilde\lambda_a)\). Thus
\[
r_a=\widetilde\lambda_a-w_a,\qquad
\psi(r_a)=0,\qquad \sigma(r_a)=\lambda_a.
\tag{3.4z}
\]
Represent these finitely many exact identities and order bounds nearby. Lemma 3.0c.3 makes the \(\lambda_a\) generate \(\ker\operatorname{gr}\psi_y\) on one neighbourhood.

For \(z\in\ker\psi_y\), its leading symbol is a combination of the \(\lambda_a\); retain homogeneous coefficients of the required degrees, lift them to operators, subtract the corresponding combination of \(r_a\), and lower the order. Boundedness below terminates. Hence the \(r_a\) generate \(\ker\psi_y\) and its induced symbols. If \(\psi(z)\) has order smaller than the order of \(z\), the same subtraction uses an exact relation and lowers the order of \(z\) without changing \(\psi(z)\). Repetition proves strictness of \(\psi_y\) onto its induced image. Its associated graded image and kernel are therefore finite, with finite-degree pieces coherent over \(\mathcal O\), by Oka's theorem.

Finally, if \(z\in\ker\phi_y\), then \(u(z)\in\ker\psi_y\) and
\[
z=v\,u(z)+(1-vu)z.
\]
Thus \(\ker\phi_y\) is generated by the finite list \(v(r_a)\) and \((1-vu)(e_i)\), where \(e_i\) are the original basis elements of \(F\). Both lists lie in the kernel, since \(\phi v=\psi\) and \(\psi u=\phi\). This proves the uniform kernel statement. \(\square\)

Lemma 3.0c.4 proves coherence of \(\mathcal D_X\). The elementary presentation argument then proves that its finite-presentation modules form an abelian category. Explicitly, present each module by finite free terms; lifts between presentations and the finite kernels just established present the kernel of a module map, and a block presentation gives the cokernel and image. For a presentation \(F_1\to F_0\to M\to0\), Lemma 3.0c.4 gives the image in \(F_0\) a good induced filtration; the quotient filtration on \(M\) is good. Its pieces are coherent \(\mathcal O\)-modules as quotients of finite coherent pieces. A finitely generated submodule of a finite free filtered module is an image of a finite free matrix, so Lemma 3.0c.4 makes its induced filtration good as well.

Lift homogeneous generators of \(\operatorname{gr}M\) to a shifted finite free surjection. Descending-order reduction makes it strict. Its kernel is coherent, and its induced filtration is good by the preceding image argument. Repeat to obtain as many strict finite filtered free terms as desired, on a successively smaller neighbourhood. Only finitely many steps will be used. Formal adjunction \(a^t=a,\ \partial_i^t=-\partial_i\), which respects the displayed relations, exchanges left and right modules and proves all these assertions on the right as well.

#### A finite free starting resolution

We now prove the analytic counterpart of Lemma 3.0, using the analytic coherence and regularity just established.

Take \(2d\) successive strict finite filtered free surjections and kernels from the operator coherence construction above. Their symbols give an exact sequence of finite graded \(S\)-modules through its \(2d\)-th syzygy \(K\). Localize at \(P\). The regular-local finite free-resolution bound of the \(2d\)-dimensional ring \(R=S_P\), and dimension shifting, make \(K_P\) finite projective over \(R\). It is free over that local ring. The elementary local freeness proof is to lift a basis of its residue quotient to a finite free surjection, split it by projectivity, and apply Nakayama to the finite kernel.

Choose a homogeneous \(\mathbb C\)-basis of \(K/PK\) and lift it to \(K\). With the corresponding finite shifts, this gives a graded map
\[
L=\bigoplus_jS(-a_j)\longrightarrow K.
\tag{3.4aa}
\]
At \(P\), the map is an isomorphism: these are minimal generators of the free \(R\)-module \(K_P\); their number is its rank, and their coefficient matrix in a local free basis has invertible determinant modulo the maximal ideal. Its kernel and cokernel over \(S\) are finite graded. They vanish after localization at \(P\), so Lemma 3.0c.2's graded detection kills them globally over the coefficient-germ polynomial ring. Thus (3.4aa) is an isomorphism and \(K\) has a finite homogeneous free basis.

Lift this basis into the operator syzygy. The resulting filtered free map is an isomorphism at \(x\): symbol reduction proves surjectivity, and a nonzero kernel element would have a nonzero leading symbol in a zero symbol kernel. Coherence of its kernel and cokernel makes this an isomorphism on a smaller neighbourhood. Hence every coherent analytic operator module has an actual length-\(2d\) finite free resolution locally, on either side. This also proves the starting bound for every finite stalk module by the same finite-generator construction at a single stalk.

#### Actual Ext support and the analytic dimension bound

Let \(L_\bullet\to M\) be this finite strict filtered free resolution. Give
\[
C^\bullet=\operatorname{Hom}_D(L_\bullet,D)
\]
its usual shifted order filtrations. Then
\[
\operatorname{gr}C^\bullet
=\operatorname{Hom}_S(\operatorname{gr}L_\bullet,S),
\quad
H^i(\operatorname{gr}C^\bullet)
=\operatorname{Ext}_S^i(\operatorname{gr}M,S).
\tag{3.4ab}
\]
Each \(C^i\) is finite free on the opposite side. Set
\(Z^i=\ker(C^i\to C^{i+1})\) and
\(B^i=\operatorname{im}(C^{i-1}\to C^i)\), using induced filtrations, and give \(E^i=Z^i/B^i\) the quotient filtration. Lemma 3.0c.4 and coherence show these are good filtrations with finite symbols. In particular \(E^i\) is a coherent right operator module.

The induced filtrations all come from the same term $C^i$, so they give the complete inclusion chain
\[
\operatorname{im}(\operatorname{gr}d^{i-1})
\subset\operatorname{gr}B^i
\subset\operatorname{gr}Z^i
\subset\ker(\operatorname{gr}d^i),
\qquad
\operatorname{gr}E^i=\operatorname{gr}Z^i/\operatorname{gr}B^i.
\]
prove
\[
\operatorname{Supp}_S\operatorname{gr}E^i
\subset
\operatorname{Supp}_S\operatorname{Ext}_S^i(\operatorname{gr}M,S).
\tag{3.4ac}
\]
Indeed, where the middle cohomology of the graded complex is zero,
\(\operatorname{gr}Z^i\) is contained in the graded boundary module, so its quotient is zero. This finite-complex argument supplies the actual Ext filtration and its support containment.

Extend (3.4ab) to \(B\) using Lemma 3.0c.1, after localization at \(P\). The finite free resolution base changes exactly, and
\[
\operatorname{Ext}_S^i(\operatorname{gr}M,S)\otimes_SB
=\operatorname{Ext}_B^i(\operatorname{gr}M\otimes_SB,B).
\tag{3.4ad}
\]
At a prime \(\mathfrak q\subset B\) of height less than \(i\), the regular local ring \(B_{\mathfrak q}\) has finite free-resolution bound \(\operatorname{ht}\mathfrak q\). Ext in degree \(i\) is zero there. Thus every support prime of (3.4ad) has height at least \(i\). Concatenating a chain below \(\mathfrak q\) with a chain above it gives
\[
\operatorname{ht}\mathfrak q+\dim(B/\mathfrak q)\leq2d.
\]
This proves, without a finite-type height equality or a catenarity assertion,
\[
\dim\operatorname{Supp}_B(\operatorname{gr}E^i\otimes_SB)
\leq2d-i.
\tag{3.4ae}
\]
Finite presentation and flatness preserve the support containment in (3.4ac): localization outside the right-hand support kills the left-hand module before and after base change.

Suppose \(E^i\ne0\). Apply **Gabber to the actual right \(D\)-module \(E^i\)**. One must not apply it to the commutative symbol Ext in (3.4ab), which need not be a characteristic module. On the right the commutator bracket changes sign; radical bracket closure is unaffected. Therefore
\[
J=\sqrt{\operatorname{ann}_S\operatorname{gr}E^i}
\]
is homogeneous and involutive for
\[
\{f,g\}=\sum_{j=1}^d
(\partial_{\zeta_j}f\,\partial_{x_j}g
-\partial_{x_j}f\,\partial_{\zeta_j}g).
\tag{3.4af}
\]
Lemma 3.0c.2 makes \(JB\) radical and makes
\(\operatorname{gr}E^i\otimes_SB\ne0\).
Its support is exactly \(V(JB)\): a finite module and its annihilator have the same support, and for flat base change annihilators commute here. To check the last point, choose finitely many module generators; the annihilator is the kernel of the simultaneous multiplication map \(S\to V^r\). Flatness preserves that kernel. Also, a power of \(J\) lies in the original annihilator: raise each of its finitely many generators to an annihilating power and use the monomial pigeonhole argument. Extending this inclusion to \(B\) shows that the radical of the extended annihilator is the radical of \(JB\), which Lemma 3.0c.2 identifies with \(JB\).

Choose finitely many homogeneous generators \(f_a\) of \(J\). The finite relations
\(\{f_a,f_b\}\in J\) and the analytic Leibniz rule show directly
\[
\{JB,JB\}\subset JB.
\tag{3.4ag}
\]
No approximation argument is needed.

By the exact earlier analytic Nullstellensatz, \(JB\) is the vanishing ideal of its analytic germ. Cartan's theorem makes the vanishing ideal sheaf coherent. Its quotient by the sheaf generated by the \(f_a\) has zero stalk at \((x,0)\), and is zero on a smaller neighbourhood. Thus the same defining ideal is radical throughout that neighbourhood. Equations (3.4ag), represented by their finitely many coefficient identities, hold there.

The earlier finite-projection/discriminant proof supplies dense regular points of each irreducible analytic component, with the component's local-ring dimension. Avoid the other finitely many components as well; their proper intersections have smaller dimension by that same proof. At such a regular point the conormal differentials span the annihilator of the component's tangent space. This follows from a graph chart: its ideal is generated by normal coordinates minus holomorphic functions of tangent coordinates. For completeness, the holomorphic implicit-function construction used for that chart comes from a contraction after inverting the normal derivative matrix. Shrink until the derivative of the resulting iteration in the normal variable has norm less than \(1/2\). Iteration converges uniformly on a smaller polydisc; the iterates are holomorphic in the parameters, so their limit is holomorphic by Cauchy's formula. Uniqueness gives the graph, and differences of a holomorphic function from its restriction to the graph are sums of those normal defining functions times holomorphic coefficients, by integrating its normal derivatives along the segment.

With the symplectic form \(\sum_j dx_j\wedge d\zeta_j\), equations (3.4af)–(3.4ag) say that this conormal space is isotropic for the inverse symplectic form. An isotropic subspace \(W\) of a nondegenerate alternating \(2d\)-space satisfies \(W\subset W^\perp\), and
\(\dim W+\dim W^\perp=2d\); hence \(\dim W\leq d\). Its codimension is the dimension of this conormal space. Every component of \(V(JB)\) therefore has dimension at least \(d\).

Combining this with (3.4ae) gives \(d\leq2d-i\). For \(i>d\) that is impossible. Hence
\[
\operatorname{Ext}_D^i(M,D)=0\quad(i>d).
\tag{3.4ah}
\]
The local finite free resolutions identify these stalk Ext groups with the stalks of the internal sheaf Ext. Consequently (3.4ah) proves (3.4t) on all of \(X\). The argument applies identically with the sides reversed.

#### Shortening while retaining free terms

Retain the actual finite free resolution
\[
0\to F_r\to\cdots\to F_0\to M\to0,\qquad r\leq2d.
\tag{3.4ai}
\]
If \(r>d\), its final injection \(j:P_r\to P_{r-1}\) initially has finite free terms. Vanishing of its top Ext says
\[
j^*:\operatorname{Hom}_D(P_{r-1},D)
\twoheadrightarrow\operatorname{Hom}_D(P_r,D).
\]
The dual of a finite projective is projective on the opposite side, as follows by dualizing its split inclusion in a finite free module. Thus \(j^*\) splits. Dualize the splitting and use finite-projective evaluation \(P\cong P^{**}\); this is an isomorphism first for a free module and then for its direct summands. We obtain a retraction of \(j\). Its cokernel is finite projective, and the split two-term end can be replaced by that cokernel. Repeat until the projective resolution has length \(d\).

The \(d\)-th syzygy \(K_d\) in the original free resolution is finite projective. For example, dimension shift gives \(\operatorname{Ext}^1_D(K_d,N)=0\) against every \(N\), using the shortened projective resolution; the kernel extension of a free surjection onto \(K_d\) splits. The original finite free tail ending in \(K_d\) now splits successively and yields
\[
K_d\oplus F_{d+1}\oplus F_{d+3}\oplus\cdots
\cong F_d\oplus F_{d+2}\oplus F_{d+4}\oplus\cdots,
\tag{3.4aj}
\]
with both sums stopping at \(r\). Let \(T\) be the finite free sum on the left. For \(d\geq1\), add the contractible pair \(T\xrightarrow{1}T\) in degrees \(d,d-1\) to the truncated projective resolution. The new last two terms are \(K_d\oplus T\) and \(F_{d-1}\oplus T\), both finite free, and all remaining terms were already free. Its exactness and length \(d\) are unchanged. When \(d=0\), the operator stalk is \(\mathbb C\), so a finite-dimensional basis gives the required length-zero free resolution separately.

This proof uses stable freeness of this particular syzygy, established by (3.4ai), rather than freeness of every finite projective \(D\)-module. The free resolution and all finite matrices and identities can be represented near \(x\). Coherence of the finitely many kernels and cokernels makes exactness at the stalk persist on a smaller common neighbourhood. This proves the finite free assertion in Theorem 3.0c.

#### Global dimension for arbitrary stalk modules

Every finite left \(D\)-module now has projective dimension at most \(d\). In particular every cyclic quotient \(D/I\), for every left ideal \(I\), has that bound. Here is the all-module extension explicitly, by the following ideal-extension argument.

For a \(\mathbb Q\)-vector space \(V\), the coinduced module
\(\operatorname{Hom}_{\mathbb Q}(D,V)\), with
\((a\phi)(b)=\phi(ba)\), is injective. Its adjunction with restriction of scalars identifies homomorphism extension with extension of linear maps between vector spaces, which is accomplished by extending a basis. Every module \(N\) embeds in the coinduced module for its underlying vector space by \(n\mapsto(a\mapsto an)\).

Iterate these embeddings \(d\) times. The terminal cokernel \(C_N\) has
\[
\operatorname{Ext}^1_D(D/I,C_N)
=\operatorname{Ext}^{d+1}_D(D/I,N)=0
\]
for every left ideal. Thus every map \(I\to C_N\) extends to \(D\). This makes \(C_N\) injective: take a maximal extension of a map from a submodule to \(C_N\), using unions of chains. If its domain omits \(v\), the left ideal \(I=\{a\in D\mid av\text{ is in the domain}\}\) maps by \(a\mapsto f(av)\). Extend this map to \(D\), with value \(c\) at \(1\); then \(f(l+av)=f(l)+ac\) extends to the larger domain. Its well-definedness is precisely compatibility on \(I\), contradicting maximality. Consequently every target module has injective dimension at most \(d\).

Therefore \(\operatorname{Ext}^{d+1}_D(V,N)=0\) for arbitrary \(V,N\). A free resolution of an arbitrary \(V\) has a \(d\)-th syzygy with \(\operatorname{Ext}^1\) zero against every module; applying this to its free-surjection kernel extension proves it projective. Hence every module has projective dimension at most \(d\). For \(d=0\), the same argument applies without iteration. The opposite-side proof is identical.

To prove the reverse inequality, take the left \(D\)-module \(H\) with its natural derivative action. Its coordinate Spencer complex is the Koszul complex
\[
0\to D\otimes\bigwedge^d\mathbb C^d\to\cdots
\to D\otimes\mathbb C^d\to D\to H\to0,
\tag{3.4ak}
\]
where the differential is the alternating sum of right multiplication by the commuting \(\partial_i\). Its symbol is the Koszul complex of \(\zeta_1,\ldots,\zeta_d\) over \(H[\zeta]\); those variables are a regular sequence, and the Koszul induction proved above gives exactness. Leading-order reduction lifts that exactness to (3.4ak).

Applying \(\operatorname{Hom}_D(-,D)\) shows
\[
\operatorname{Ext}^d_D(H,D)
=D/\sum_i\partial_iD\ne0.
\tag{3.4al}
\]
Indeed formal adjunction sends this quotient to
\(D/\sum_iD\partial_i\), which PBW identifies with \(H\): an operator acts on \(1\) by its constant derivative coefficient, and precisely the terms with positive derivative order lie in the displayed left ideal. Thus \(H\) has projective dimension \(d\). Formal adjunction gives the right-hand lower bound too. For \(d=0\), both dimensions are zero. This proves (3.4u) with its full all-module scope.

### Theorem 3.1. Holonomic Ext concentration

For holonomic $M$,

\[
\mathcal Ext_{\mathcal D_X}^{\,i}(M,\mathcal D_X)=0
\quad(i\ne d),
\tag{3.5}
\]

and the right module $\mathcal Ext^d(M,\mathcal D_X)$ is holonomic. Hence $\mathbb D_X(M)$ is a holonomic module in degree zero.

**Proof.** The zero module is immediate. For nonzero holonomic $M$, the independently proved whole-dimension Bernstein inequality, Theorem 7.2, together with (1.1), gives $\dim\operatorname{Ch}(M)=d$. Lemma 3.0b then makes every sheaf Ext below $d$ vanish.

For $i>d$, the same lemma puts the characteristic dimension of the coherent right module $E^i=\mathcal Ext_{\mathcal D_X}^{\,i}(M,\mathcal D_X)$ at most $2d-i<d$. If it were nonzero, Bernstein's inequality applied on a nonempty coordinate open, after canonical-bundle side change, would give dimension at least $d$, a contradiction. Here side change preserves characteristic dimension and support: in a volume trivialization its transpose fixes functions and sends the symbol of a vector field to its negative. The coefficient from changing the volume has order zero. The induced cotangent map is $(x,\xi)\mapsto(x,-\xi)$, which preserves every conic characteristic support; tensoring with a line bundle changes no support. Thus the same dimension inequality applies on the right. All $E^i$ above $d$ vanish as well.

For $i=d$, Lemma 3.0b gives $\operatorname{Ch}(E^d)\subseteq\operatorname{Ch}(M)$ and characteristic dimension at most $d$. Therefore $E^d$ is holonomic on the right, and its side change is holonomic on the left. The shift $[d]$ puts this sole Ext group in degree zero, proving all assertions. The proof uses the commutative bounds, the proved filtered comparison and the independent whole-dimension inequality. It does not use the general Gabber theorem, whose complete proof is supplied in the earlier characteristic-variety lesson. $\square$

For freely accessible further reading, C. Schnell, [*D-modules*, Lecture 8](https://www.math.stonybrook.edu/~cschnell/pdf/notes/d-modules.pdf), Corollary 8.4 and Lemma 8.5, discusses the Ext characterization and holonomicity of the dual; Ginzburg, [*Lectures on D-modules*](https://math.berkeley.edu/~nadler/ginzburg.dmodules.pdf), Section 4.3, Corollary 4.3.4, discusses the sheaf version. The proof above supplies the filtered estimates and concentration within the programme.

Section 4 retains a complete explicit calculation of the one-variable cyclic case.

### Corollary 3.2. Exact contravariant equivalence

Duality gives an exact anti-equivalence of $\operatorname{Hol}(\mathcal D_X)$, preserves simple modules, and preserves length. It also preserves $D_h^b(\mathcal D_X)$.

**Proof.** Apply the long exact Ext sequence to a short exact sequence of holonomic modules. By (3.5), its only surviving part is

\[
0\longrightarrow\mathcal Ext^d(M'',\mathcal D_X)
\longrightarrow\mathcal Ext^d(M,\mathcal D_X)
\longrightarrow\mathcal Ext^d(M',\mathcal D_X)
\longrightarrow0.
\tag{3.6}
\]

Side change is exact, so this is the dual short exact sequence. Biduality (3.4) supplies the inverse functor.

If the dual of a simple nonzero module had a nonzero proper submodule, dualizing the resulting short exact sequence would give a nonzero proper quotient of the original simple module. This is impossible. Reversing and dualizing a composition series therefore gives a composition series of the same length.

Finally a bounded complex is assembled from its cohomology modules by finitely many standard truncation triangles. Duality reverses triangles, and the duals of its holonomic cohomology modules are holonomic. The Serre property then keeps every intermediate cohomology holonomic. This proves preservation of (1.3). $\square$

## 4. Cyclic modules on the line: a complete Ext calculation

Put $A=A_1(k)$ and use the volume form $dx$. Its transpose is the anti-involution

\[
x^*=x,\qquad \partial^*=-\partial,\qquad
(PQ)^*=Q^*P^*.
\tag{4.1}
\]

It respects the Weyl relation, since $(\partial x-x\partial)^*=(-x\partial)-(-\partial x)=1$. It squares to the identity.

### Proposition 4.1. Dual of a cyclic equation

For $0\ne P\in A$ and $M_P=A/AP$,

\[
\operatorname{Ext}_A^i(M_P,A)=0\quad(i\ne1),
\qquad
\operatorname{Ext}_A^1(M_P,A)=A/PA
\tag{4.2}
\]

as a right module, and

\[
\mathbb D_{\mathbb A^1}(M_P)\simeq A/AP^*.
\tag{4.3}
\]

For a nonzero scalar $P$, both sides are zero.

**Proof.** The Weyl algebra is a domain by its PBW symbol filtration. Consequently right multiplication by $P$ is injective and gives the left-module resolution

\[
0\longrightarrow A
\xrightarrow{\;\cdot P\;}A
\longrightarrow M_P\longrightarrow0.
\tag{4.4}
\]

A left-linear map $A\to A$ has the form $a\mapsto aq$, where $q$ is its value at $1$. Precomposing with the arrow in (4.4) sends $q$ to $Pq$. Thus derived Hom is the complex of right modules

\[
A\xrightarrow{\;P\cdot\;}A
\quad\text{in degrees }0,1.
\tag{4.5}
\]

Its kernel is zero by the domain property, and its cokernel is $A/PA$. There are no higher terms. This proves (4.2), without using Theorem 3.1.

The shift $[1]$ places the cokernel in degree zero. Side change sends the right module $A/PA$ to the left module $A/AP^*$ by

\[
[q]\longmapsto[q^*].
\tag{4.6}
\]

Indeed $(Pq)^*=q^*P^*$, so the right ideal becomes the indicated left ideal. For the changed left action, $a\cdot[q]=[qa^*]$, and $(qa^*)^*=a q^*$, so (4.6) is left-linear. It is bijective because transpose is an involution. This proves (4.3). $\square$

For example, $\mathcal O_{\mathbb A^1}=A/A\partial$ is self-dual. The point module $\delta_0=A/Ax$ is also self-dual. For the Euler module $Q_\lambda=A/A(x\partial-\lambda)$, the parameter transforms as

\[
(x\partial-\lambda)^*=-(x\partial+\lambda+1),
\qquad
\mathbb D(Q_\lambda)=Q_{-\lambda-1}.
\tag{4.7}
\]

The additional $1$ comes from moving $\partial$ past $x$.

## 5. Connections and opposite extensions

### Proposition 5.1. Dual of a finite connection

If $E$ is a finite locally free module with integrable connection, then

\[
\mathbb D_X(E)\simeq E^\vee
\tag{5.1}
\]

with the dual connection characterized by

\[
\xi\langle\phi,e\rangle
=\langle\nabla^\vee_\xi\phi,e\rangle
+\langle\phi,\nabla_\xi e\rangle.
\tag{5.2}
\]

**Proof.** Work in commuting étale coordinate fields $\partial_1,\ldots,\partial_d$. The Spencer resolution has terms

\[
S_p=\mathcal D_X\otimes_{\mathcal O_X}
(\textstyle\bigwedge^p T_X\otimes_{\mathcal O_X}E),
\quad 0\leq p\leq d,
\tag{5.3}
\]

placed in degree $-p$. For a wedge of coordinate fields its differential is the alternating sum of

\[
P\otimes(\partial_{i_1}\wedge\cdots\wedge\partial_{i_p})\otimes e
\longmapsto
(-1)^{a-1}
\bigl(P\partial_{i_a}\otimes\widehat{\partial_{i_a}}\otimes e
-P\otimes\widehat{\partial_{i_a}}\otimes\nabla_{i_a}e\bigr).
\tag{5.4}
\]

The hat denotes the remaining wedge in its original order. Flatness and commutation of the coordinate fields make the differential square to zero; pairs of two-derivative terms cancel, with the remaining connection terms giving the curvature. The augmentation is $P\otimes e\mapsto Pe$.

For arbitrary vector fields $\xi_1,\ldots,\xi_p$, the intrinsic formula also contains

\[
\sum_{a<b}(-1)^{a+b}P\otimes
\bigl([\xi_a,\xi_b]\wedge
\xi_1\wedge\cdots\widehat{\xi_a}\cdots
\widehat{\xi_b}\cdots\wedge\xi_p\bigr)\otimes e.
\]

The product rule and the connection's Leibniz rule make this formula compatible with moving functions across the tensor products. Thus it is independent of the coordinate frame; its bracket term vanishes in the commuting frame used in (5.4).

Give $S_p$ the order filtration shifted by $p$. Its associated graded complex is the Koszul complex of $\xi_1,\ldots,\xi_d$ on $S\otimes E$, resolving $E$ on the zero section. These variables form a regular sequence, so it is exact except at the augmentation. Lifting a graded preimage and subtracting lowers order; the bounded lower limit proves exactness of (5.3) itself.

Apply $\mathcal Hom_{\mathcal D_X}(-,\mathcal D_X)$. The associated graded dual Koszul complex is exact below degree $d$, with top quotient $\omega_X\otimes E^\vee$. The same lowering argument proves vanishing of the lower cohomology of the filtered dual complex. In the top quotient, the relations supplied by (5.4) move a derivative from an output operator onto the dual coefficient, with a minus sign. They reduce every normal-form operator to its coefficient of order zero. The action on that coefficient is

\[
(\eta\otimes\phi)\xi
=-\mathcal L_\xi\eta\otimes\phi
-\eta\otimes\nabla^\vee_\xi\phi.
\tag{5.5}
\]

The pairing identity (5.2) verifies the relation for each coordinate derivative and for multiplication by functions. It also shows that the zero-order representative is unique: the candidate module $\omega_X\otimes E^\vee$ with action (5.5) satisfies all the relations and receives the identity map on those representatives. Thus $\mathcal Ext^d(E,\mathcal D_X)$ is that right module. The intrinsic Spencer construction and pairing make the local identifications compatible with changes of coordinates and frame. Side change and $[d]$ give (5.1). $\square$

In particular $\mathbb D_X(\mathcal O_X)=\mathcal O_X$. For the exponential connection $\mathcal O_Xe^f$, defined by $\partial_i e^f=(\partial_i f)e^f$, equation (5.2) gives $\mathcal O_Xe^{-f}$. On $\mathbb G_m$, the connection $\mathcal O x^\lambda$ has dual $\mathcal O x^{-\lambda}$.

This agrees with (4.7). After restricting $Q_{-\lambda-1}$ to $\mathbb G_m$, if $w$ is its cyclic generator, then $xw$ satisfies

\[
x\partial(xw)=-\lambda(xw).
\tag{5.6}
\]

The invertible change of generator removes the extra integer in the affine-line presentation.

### Laurent polynomials: the *-extension

Let $j:\mathbb G_m\hookrightarrow\mathbb A^1$. The module denoted here by $j_*\mathcal O_{\mathbb G_m}$ is

\[
L=k[x,x^{-1}]\simeq A/A(\partial x).
\tag{5.7}
\]

To verify the presentation, send its cyclic generator $v$ to $x^{-1}$. The relation $\partial x\,v=0$ holds, and differentiation and coordinate multiplication generate all Laurent monomials. The quotient is spanned by

\[
x^a v\ (a\geq0),\qquad \partial^b v\ (b\geq1),
\tag{5.8}
\]

since $x\partial^b v=-b\partial^{b-1}v$ reduces every mixed monomial. Their images are $x^{a-1}$ and $(-1)^b b!x^{-b-1}$, respectively. They have distinct Laurent exponents and nonzero coefficients, so they are independent. This proves (5.7).

There is an exact sequence

\[
0\longrightarrow\mathcal O_{\mathbb A^1}
\longrightarrow L\longrightarrow\delta_0\longrightarrow0.
\tag{5.9}
\]

For a direct check of the quotient, the class of $x^{-1}$ is killed by $x$, and its successive derivatives give a basis of the negative powers modulo polynomials, exactly the basis of $\delta_0$. The extension cannot split: a map $\delta_0\to L$ would send its generator to a Laurent polynomial killed by $x$, and no nonzero such element exists. Both end modules are simple, so $L$ has length two.

### The !-extension and its simple submodule

Define $j_!\mathcal O_{\mathbb G_m}$ by duality of (5.7). Since $(\partial x)^*=-x\partial$, Proposition 4.1 gives

\[
J:=j_!\mathcal O_{\mathbb G_m}\simeq A/A(x\partial).
\tag{5.10}
\]

Dualizing (5.9), or calculating directly, gives the opposite nonsplit extension

\[
0\longrightarrow\delta_0
\longrightarrow J\longrightarrow\mathcal O_{\mathbb A^1}
\longrightarrow0.
\tag{5.11}
\]

Here the point submodule is generated by $w=\partial v$: $xw=0$. To verify it completely, the quotient has basis $x^a v$, $a\geq0$, and $\partial^b v$, $b\geq1$. Spanning follows from $x\partial^b v=-(b-1)\partial^{b-1}v$. For independence, take a vector space with basis $u_a$ for $a\geq0$ and $w_b$ for $b\geq1$, and define

\[
\begin{aligned}
xu_a&=u_{a+1},&
\partial u_0&=w_1,\\
\partial u_a&=a u_{a-1}\quad(a\geq1),\\
\partial w_b&=w_{b+1},&
xw_b&=-(b-1)w_{b-1}\quad(b\geq1),
\end{aligned}
\tag{5.12}
\]

where the last expression is zero for $b=1$. These actions satisfy $[\partial,x]=1$, including at $u_0$ and $w_1$. The module is generated by $u_0$ with $x\partial u_0=0$, and the map $v\mapsto u_0$ sends the proposed spanning vectors to its distinct basis vectors. This proves independence. Its derivative branch is $\delta_0$, and quotienting by that branch leaves the polynomial connection, proving (5.11).

A section of the last map would lift $1$ to $v+u$, where $u$ is a finite linear combination of $\partial^b v$ for $b\geq1$, and would require $\partial(v+u)=0$. In that derivative, the coefficient of $\partial v$ is one; the derivative of $u$ has only higher powers. Thus no section exists.

Finally $\delta_0$ is the unique simple submodule of $J$. Any simple submodule other than this one would have zero intersection with it and would map isomorphically onto the simple quotient $\mathcal O$, splitting (5.11). This is impossible. Both $L$ and $J$ restrict to the same connection on $\mathbb G_m$; their boundary attachments distinguish them.

## 6. Exercises with complete solutions

### Exercise 6.1 — easy: the point dual

Compute the dual of $\delta_0$ on the affine line, including its Ext degree and side.

**Solution.** Use (4.4) with $P=x$. The right-module Hom complex is $A\xrightarrow{x\cdot}A$ in degrees zero and one. Its kernel is zero and its cokernel is the right module $A/xA$. After $[1]$, only degree zero remains. Since $x^*=x$, side change identifies that module with $A/Ax=\delta_0$.

### Exercise 6.2 — easy: an adjoint with a variable coefficient

Compute $(x^2\partial-1)^*$ and the dual of $A/A(x^2\partial-1)$. Identify its connection on $\mathbb G_m$.

**Solution.** Reverse the product and commute:

\[
(x^2\partial-1)^*=-\partial x^2-1
=-x^2\partial-2x-1.
\]

Thus the dual is $A/A(x^2\partial+2x+1)$, since multiplying an operator by $-1$ does not change its left ideal. On $\mathbb G_m$, its generator $w$ satisfies $\partial w=-(2/x+1/x^2)w$. Set $z=x^2w$. Then

\[
\partial z=2xw+x^2\partial w=-w=-x^{-2}z.
\]

The original localized module is the exponential connection $e^{-1/x}$, whose logarithmic derivative is $x^{-2}$. The new generator exhibits its dual as $e^{1/x}$. The extra $2x$ in the adjoint is accounted for by this invertible generator change.

### Exercise 6.3 — medium: length and a nonsplit extension

Prove that $L=k[x,x^{-1}]$ has length two and that (5.9) does not split.

**Solution.** The polynomials are a nonzero submodule. Their quotient is generated by $[x^{-1}]$, killed by $x$, and $\partial^r[x^{-1}]=(-1)^r r![x^{-r-1}]$ gives its independent basis. Hence the quotient is $\delta_0$. The polynomial connection is simple: differentiating a nonzero polynomial enough times produces a nonzero constant, and multiplication then produces every polynomial. The point module is simple: for a nonzero polynomial in $\partial$ applied to its generator, enough applications of $x$ lower its degree to a nonzero constant multiple of the generator. Thus the sequence is a composition series with two factors.

If a splitting existed, the image of the point generator would be a nonzero element $u\in L$ with $xu=0$. Multiplication by $x$ is invertible in $L$, so this is impossible.

### Exercise 6.4 — medium: Euler Ext and the parameter

Compute $\operatorname{Ext}^1_A(Q_\lambda,A)$ as a right module and its associated left module. Reconcile the result with duality of a rank-one connection on $\mathbb G_m$.

**Solution.** Resolution (4.4) gives the right module

\[
\operatorname{Ext}^1_A(Q_\lambda,A)
=A/(x\partial-\lambda)A.
\]

There is no degree-zero or higher Ext. Transpose gives the left module $A/A(x\partial+\lambda+1)=Q_{-\lambda-1}$. On $\mathbb G_m$, its generator $w$ has Euler eigenvalue $-\lambda-1$. The generator $z=xw$ has eigenvalue $-\lambda$, since $x\partial(xw)=xw+x(x\partial w)$. Therefore the localized connection is the dual $\mathcal O x^{-\lambda}$.

### Exercise 6.5 — hard: the unique simple submodule of the !-extension

Prove the presentation (5.10), describe its unique simple submodule, and show why it is not an $\mathcal O$-module extension by zero.

**Solution.** The complete cyclic Ext calculation applied to $P=\partial x$ gives $J=A/A(x\partial)$, because $(\partial x)^*=-x\partial$. Its vector $w=\partial v$ is killed by $x$, and the independent derivative branch in (5.12) identifies $Aw$ with $\delta_0$. Quotienting by this branch gives $A/A\partial=\mathcal O$. The coefficient of $\partial v$ prevents any horizontal lift of $1$, proving nonsplitting exactly as in Section 5.

If another simple submodule existed, its intersection with $Aw$ would be zero by simplicity, and its nonzero image in the simple quotient $\mathcal O$ would be an isomorphism. That would yield a section and contradict nonsplitting. So $Aw$ is unique. It is nonzero and supported at the omitted point. The underlying sheaf and derivative action in (5.12) have a point contribution and a nontrivial boundary extension; the construction is the holonomic dual of $j_*\mathcal O$, not the operation of assigning zero stalks outside the open subset.

### Exercise 6.6 — hard: the exceptional set and the dimension hypothesis

Compute the generic-connection open set for $M=\mathcal O_{\mathbb A^1}\oplus\delta_0$, and explain why the same argument does not produce a dense connection open set for the regular module $A_1$.

**Solution.** The first module has characteristic variety equal to the zero section together with the cotangent fiber over zero. Projectivizing removes the zero-section component and turns the nonzero fiber into a single point mapping to zero. Thus $Z=\{0\}$ and $U=\mathbb G_m$; the point summand disappears and the remaining connection has rank one.

For the regular module, the characteristic variety is all of $T^*\mathbb A^1$, of dimension two. Its projectivization is $\mathbb A^1\times\mathbf P^0$, whose image is all of $\mathbb A^1$. Inequality (2.2) fails: the projectivized characteristic set has dimension one, not at most zero. Accordingly there is no dense open set supplied by this argument. In fact the regular module has infinitely many independent derivative directions over the coordinate ring on every nonempty open set, so it cannot be a finite connection there.

## References and proof boundary

Generic connection structure and finite length are proved in Section 2 from the characteristic-support and cycle results of the earlier lessons. The duality construction, bidual evaluation, exactness consequences, cyclic Ext calculation, connection dual, the two opposite boundary extensions and all six exercises are worked out here. Lemmas 3.0a and 3.0b prove the commutative and filtered Ext-support estimates, including finite-page stabilization of the actual Ext filtration. Theorem 3.1 proves general holonomic Ext concentration from those estimates and the independent whole-dimension Bernstein inequality in the earlier characteristic-variety lesson. Section 4 also proves the cyclic case explicitly. The full Gabber theorem is proved in the earlier characteristic-variety lesson. Theorem 3.0c also proves the sharper analytic finite free resolution bound and the full stalk global-dimension statement, using uniform analytic operator coherence, relative completion, actual Ext support and the earlier Gabber theorem. The algebraic concentration proof remains independent of that analytic bound.

V. Ginzburg, [*Lectures on D-modules*](https://math.berkeley.edu/~nadler/ginzburg.dmodules.pdf), Section 4.3, especially Definition 4.3.1 and Corollary 4.3.4, discusses algebraic holonomic duality. The shift and right/left sides are fixed explicitly in (3.3)–(4.6).

E. Frenkel, [*Lectures on the Langlands program and conformal field theory*](https://arxiv.org/abs/hep-th/0512172), Section 3.6, explains the relation with regular holonomic modules and the operations on their analytic solutions. Bhatt, Blickle, Lyubeznik, Singh and Zhang, [*Applications of perverse sheaves in commutative algebra*](https://arxiv.org/abs/2308.03155), Section 2, theorem on the Riemann–Hilbert correspondence, part (1), records compatibility with duality for **regular** holonomic modules. That analytic correspondence is outside this chapter's proofs and does not restrict the algebraic duality used here to regular modules.

- M. Kashiwara, [*Algebraic study of systems of partial differential equations*](https://www.kurims.kyoto-u.ac.jp/~kenkyubu/kashiwara/master_thesis.pdf), freely accessible translation of the 1970 thesis, §3.1, Lemma 3.1.1, Theorem 3.1.5 and Remark 6: analytic resolution and homological-dimension bounds.
