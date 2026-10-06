# Transport along a scaling action

Its proofs are
relative to the explicit sheaf-theoretic imports below; it does not close those
imports or the Microlocal Sheaves course. The consulted antecedents are
Kashiwara and Schapira, [*Microlocal Study of Sheaves*, Astérisque 128 (1985)](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf),
§2.1.1, printed p. 39, and Pierre Schapira,
[*An Introduction to Sheaves on Grothendieck Topologies*](https://webusers.imj-prg.fr/~pierre.schapira/LectNotes/SHV.pdf),
version dated 1 August 2026, Definition 5.4.4 and Exercise 5.13, pp. 114 and 120.
Their conic objects use positive rays in a real vector bundle. This unit also
treats arbitrary continuous positive-real actions, so it proves the required
transport and topology statements below instead of importing them from that
vector-bundle setting. The final section compares the actual source hypotheses
and proof mechanisms. No constructibility or finite-generation condition is
imposed.

## SH02-CON-CONTRACT — Objects, degree conventions, and imports

Fix a commutative ring $A$ of finite global dimension $d$. All spaces called
locally compact are Hausdorff. Write $D^+(X)$ for complexes of sheaves of
$A$-modules with cohomology bounded below. Bounds need not be zero and stalk
modules need not be finitely generated. A shift satisfies
$H^q(K[r])=H^{q+r}(K)$. In particular a module in cohomological degree one is
written $M[-1]$. Tensor products and internal Hom below are derived over the
constant sheaf of rings, unless specified otherwise.

The action group is $G=(0,\infty)$ under multiplication. Its orientation is
the increasing coordinate $\log t$. An action is a continuous map
$a:X\times G\to X$ with $a(a(x,s),t)=a(x,st)$ and $a(x,1)=x$. The action is
not required to be free, proper, effective, or a vector-space action. Set

$$
p:X\times G\longrightarrow X,\qquad e:X\longrightarrow X\times G,
\qquad p(x,t)=x,\quad e(x)=(x,1).
$$

Here are the exact prerequisite results used. Their proof routes are
identified below; the exceptional-operation and orientation contracts retain
their separately stated scopes.

### SH02-IMPORT-INTERVAL — Interval cohomology (SH-01 import contract)

A locally constant sheaf on an interval is
   constant; its ordinary cohomology in positive degrees vanishes. Evaluation
   at any point identifies its sections with its stalk. These statements hold
   for arbitrary $A$-modules. They also give the analogous evaluation statement
   for a bounded-below complex with locally constant cohomology, by the
   hypercohomology spectral sequence. The interval-constancy and evaluation proof establishes all these statements for arbitrary module coefficients, including open, closed, half-open and unbounded intervals. Its complex comparison is the actual section-to-germ map, using the bounded-below hypercohomology proof and its canonical edge, not an unspecified isomorphism.

### SH02-IMPORT-CONTINUITY — Closed-exhaustion continuity (SH-01 import contract)

Stalks and filtered colimits of $A$-modules are
   exact. For a closed exhaustion $T_n\subset\operatorname{Int}(T_{n+1})$
   of a space $T$, the usual sheaf-cohomology continuity theorem and its
   Mittag-Leffler criterion apply. In particular, if the restriction maps
   $H^q(T_m;K)\to H^q(T_n;K)$ are isomorphisms for every $q$ and $m\ge n$,
   then $H^q(T;K)\to H^q(T_n;K)$ is an isomorphism. The same assertion is
   available after restriction to an open subset of a parameter space.
   The geometric derived-limit comparison and its degree-specific Milnor
   obstruction are proved in the closed-exhaustion comparison and its tower, Milnor and Mittag–Leffler proofs,
   specifically SH02-EXH-COMPARISON, SH02-EXH-MILNOR and SH02-EXH-STRIPS.
   That proof includes the noncompact strips used below.

### SH02-IMPORT-DERIVED-SHEAVES — Derived sheaf operations (SH-01 import contract)

Exact inverse image, derived direct image,
   adjunction, derived sections, localization triangles, stalk detection of
   quasi-isomorphisms, and the bounded-below hypercohomology spectral sequence.
   Proper base change for $Rf_!$ is part of this import; ordinary $Rf_*$ base
   change is used below only when the relevant map is proper or when a separate
   proof is supplied. For the proper closed-strip projections in SH02-CON-CYLINDER, the proper-fibre and section-restriction proof supplies the exact ordinary direct-image comparison on locally compact Hausdorff spaces, for arbitrary module coefficients and bounded-below complexes. This does not assert ordinary base change for a general nonproper map.

### SH02-IMPORT-SIX-FUNCTORS — Exceptional operations contract

If $f_!$ has finite cohomological dimension,
   $Rf_!\dashv f^!$ on $D^+$, with its units and counits, composition,
   projection formula, and

   $$
   Rf_*R\mathcal Hom(K,f^!L)
     \simeq R\mathcal Hom(Rf_!K,L),\qquad
   f^!R\mathcal Hom(B,C)
     \simeq R\mathcal Hom(f^{-1}B,f^!C).
   $$

   In these formulas the first internal-Hom argument is bounded above and the
   second is bounded below. All instances below meet these bounds. For an
   oriented topological submersion of relative dimension $r$,
   $f^!L\simeq f^{-1}L[r]$. An oriented open interval has
   $R\Gamma_c(I;A)\simeq A[-1]$, and integration identifies
   $R\Gamma_c(I;A[1])\to A$ with the identity in this identification. These
   assertions include the trace's compatibility with proper base change.

The submersion comparison, SH02-MD-SUBMERSION, proves the oriented-submersion assertion for every bounded-below input on locally compact Hausdorff bases. Its product-chart argument checks the actual tensor comparison, not only the underlying objects. The compact-support generator, SH02-MD-EUCLIDEAN, and normalized trace and submersion base change, SH02-MD-TRACE, prove the interval calculation and its sign. They use the cylinder theorem above only at SH02-CON-CYLINDER, whose proof uses neither orientation nor exceptional inverse image.

For internal duality with a bounded first input and a bounded-below second input, SH02-EX-INTERNAL supplies the proof; that scope suffices for SH02-CON-INTERVAL-FIBRES. The opposite-bounded-range proof, (EXA.1)–(EXA.9), supplies the full bounded-above first-input contract displayed above under the same uniform proper-support dimension hypothesis. It uses the finite relative-soft model, the exact unbounded acyclic-model theorem and an explicit coefficient exchange, rather than assuming that a bounded-above/bounded-below tensor is bounded below.

### SH02-IMPORT-PROPER-SUPPORTS — Proper-support sections contract

For a map $f:Y\to B$ of locally compact
   spaces, the stalks of $R^qf_!K$ can be computed by the filtered system of
   $H^q_C(f^{-1}V;K)$, where $V$ runs through neighbourhoods of the base point
   and $C\subset f^{-1}V$ is closed and proper over $V$. For a closed embedding
   $i:S\hookrightarrow Y$, $i_*i^!K\simeq R\Gamma_S K$, compatibly with
   inclusions of closed supports.

These are hypotheses on the available sheaf formalism, not additional
geometric assumptions such as compactness of $X$ or constructibility of $K$.
Finite global dimension is a fixed convention of this unit; no noetherian
assumption is added. Results about actual manifolds use finite
dimension and countability at infinity, but the action and vector-bundle
results below require only the stated locally compact spaces.

## SH02-CON-CYLINDER — Descent across a contractible parameter

**Lemma.** Let $B$ be locally compact and let $q:B\times\mathbb R\to B$.
For $K\in D^+(B\times\mathbb R)$, assume every $H^j(K)$ restricts to a
locally constant sheaf on every fibre of $q$. With $s_0(b)=(b,0)$, the
evaluation and counit morphisms

$$
Rq_*K\longrightarrow s_0^{-1}K,
\qquad q^{-1}Rq_*K\longrightarrow K
$$

are isomorphisms. Consequently $q^{-1}:D^+(B)\to D^+(B\times\mathbb R)$
is fully faithful; its essential image consists exactly of those $K$ with
fibrewise locally constant cohomology. Restriction by $s_0$ is an inverse on
that image.

**Proof.** Put $I_n=[-n,n]$, restrict $K$ to $B\times I_n$, and denote the
proper projection by $q_n$. It is proper because the inverse image of a compact $C\subset B$ is $C\times I_n$, which is compact; the spaces are Hausdorff. The proper-fibre comparison with its actual restriction map identifies the stalk at $b$ of
$Rq_{n*}(K|_{B\times I_n})$ with $R\Gamma(I_n;K|_{\{b\}\times I_n})$.
In the spectral sequence for these sections the terms in positive sheaf
cohomology degree vanish by SH02-IMPORT-INTERVAL. The remaining terms are the
stalks at $(b,0)$ of $H^j(K)$. The spectral sequence is convergent because
$K$ is bounded below, by HC1a–HC2. The interval evaluation theorem identifies this calculation with evaluation and proves that

$$
Rq_{n*}(K|_{B\times I_n})\longrightarrow s_0^{-1}K
$$

is a quasi-isomorphism. For $m\ge n$ the restriction morphism between these
direct images commutes with evaluation, so it too is an isomorphism.

For every open $V\subset B$, this gives compatible isomorphisms

$$
H^j(V\times I_n;K)\simeq H^j(V;s_0^{-1}K).
$$

The closed strips $V\times I_n$ exhaust $V\times\mathbb R$, each lying in
the interior of the next. The transition maps on cohomology are isomorphisms,
so SH02-IMPORT-CONTINUITY shows that evaluation
$H^j(V\times\mathbb R;K)\to H^j(V;s_0^{-1}K)$ is an isomorphism for every
$j$. This is the asserted isomorphism $Rq_*K\to s_0^{-1}K$.

For the counit, fix $(b,t)$ and choose $n>|t|$. Its restriction to the strip
fits into the adjunction diagram with the counit for $q_n$. On the stalk at
$(b,t)$, the latter is evaluation from
$R\Gamma(I_n;K|_{\{b\}\times I_n})$ to $K_{(b,t)}$. The same spectral
sequence calculation, now evaluated at $t$, makes this an isomorphism. The
map $Rq_*K\to Rq_{n*}(K|_{B\times I_n})$ was already shown to be an
isomorphism. Thus the counit is an isomorphism on every stalk.

For $K=q^{-1}L$ its cohomology is constant along fibres, and the unit
$L\to Rq_*q^{-1}L$ is inverse to evaluation: the composite is the identity
by the adjunction identity. Hence this unit is an isomorphism. Adjunction now
gives

$$
\operatorname{Hom}(q^{-1}L,q^{-1}M)
 \simeq\operatorname{Hom}(L,Rq_*q^{-1}M)
 \simeq\operatorname{Hom}(L,M).
$$

This proves full faithfulness and the remaining assertions. The same proof
works after replacing $\mathbb R$ by $G$ through $\log$. Iterating it gives
full faithfulness for $B\times G^r\to B$ for every finite $r$. No
finite-generation or upper-boundedness assertion was used. $\square$

## SH02-CON-DEFINITION — Which orbit topology is meant?

For a subset $Z\subset X$, restriction in this unit means
$F|_Z=i_Z^{-1}F$, where the subset has its induced topology. For a general
action this must be distinguished from pullback along an orbit parameter.
The distinction is invisible for an ordinary nonzero vector-bundle ray,
whose induced and homogeneous-space topologies agree. Thus the raywise
definitions in Astérisque 128, §2.1.1, and Schapira's Definition 5.4.4 do not
decide which definition to use for a dense orbit of a general action.
We specify both and compare them directly.

For $x\in X$, let $b_x$ be its orbit with the topology induced from $X$,
and write $i_x:b_x\to X$ and $o_x:G\to X$, $o_x(t)=a(x,t)$, for the
inclusion and the orbit map. The induced-orbit sheaf category is the full subcategory

$$
\operatorname{Mod}_{\mathrm{ind}}(A_X)
=\{L\in\operatorname{Mod}(A_X):
       i_x^{-1}L\text{ is locally constant on }b_x\text{ for every }x\}.
$$

Write $D_{\mathrm{ind}}^+(X)$ for the full subcategory of $D^+(X)$ whose
cohomology sheaves belong to this category. These are definitions; they do
not identify induced-orbit conicity with parameter conicity, or require
$b_x$ to be locally compact.

In this unit, **conic** means **parameter-conic**: $F\in D^+(X)$ is conic
if $o_x^{-1}H^j(F)$ is locally constant on $G$ for every $x$ and $j$.
Write $D_G^+(X)$ for this full subcategory. For an ordinary sheaf $L$, the
corresponding condition is local constancy of every $o_x^{-1}L$.

Equivalently, one can restrict to each orbit with its homogeneous-space
topology. Here is the topology check, including nonembedded orbits. The
stabilizer $G_x$ is closed because $X$ is Hausdorff. Under $\log$, a closed
subgroup of $\mathbb R$ is either $0$, $c\mathbb Z$ for some $c>0$, or
$\mathbb R$. Indeed, if positive subgroup elements have infimum zero their
integer multiples approximate every real number and closedness gives the
whole line. Otherwise the positive infimum belongs to the closed subgroup,
and division with remainder shows that it generates the subgroup. The
remaining subgroup has no nonzero elements.

Thus $G/G_x$ is a line, a circle, or a point. Except for the point case the
quotient map has local sections and is a local homeomorphism. A sheaf on the
homogeneous orbit is locally constant if and only if its pullback to $G$ is:
one direction is functorial pullback, and the other follows by pulling back
along a local section and using a neighbourhood on which the pulled-back
sheaf is constant. In the point case both statements hold for every module.
Inverse image is exact, so this applies separately to every cohomology sheaf.

Here pullback from a homogeneous orbit means pullback along the continuous
map $G/G_x\to X$ induced by $o_x$, with $G/G_x$ given its quotient topology.
That map need not be an embedding, so its quotient topology cannot be
silently replaced by the induced topology. The next example proves that
$D_{\mathrm{ind}}^+(X)\subseteq D_G^+(X)$ can be strict, while the
homogeneous and parameter conditions are equivalent as just proved.

## SH02-CON-EXAMPLE-DENSE-ORBIT — A topology distinction detected by supports

Take $A=\mathbb Z$, choose an irrational real number $\lambda$, and put

$$
X=S^1\times S^1,\qquad
j:\mathbb R\longrightarrow X,\qquad
j(u)=(e^{iu},e^{i\lambda u}).
$$

Use the continuous action

$$
a((z_1,z_2),t)=(e^{i\log t}z_1,e^{i\lambda\log t}z_2).
$$

The map $j$ is injective: $j(u)=j(v)$ would give $u-v=2\pi m$ and
$\lambda m\in\mathbb Z$, forcing $m=0$. Its image $b$ is one orbit.
It is dense. To see this, the closure of the subgroup
$\mathbb Z+\lambda\mathbb Z\subset\mathbb R$ contains $1$ and
$\lambda$. By the closed-subgroup classification above, a proper such
closure would be $c\mathbb Z$, making $\lambda$ a ratio of integers.
Thus this subgroup is dense, so the fractional parts of $m\lambda$ are
dense in the circle. At each fixed first coordinate, adding $2\pi m$ to
the parameter therefore gives a dense set of second coordinates. This
proves density in $X$. The nonconstancy argument below only needs the
recurrence that we will also prove explicitly.

Let

$$
F=j_!\mathbb Z_{\mathbb R}.
$$

Here $j_!$ is the direct image with proper supports for a continuous map
between locally compact Hausdorff spaces. It does not require $j$ to be a
locally closed embedding. Concretely, $F(U)$ consists of locally constant
integer-valued sections on $j^{-1}U$ whose closed support is proper over $U$.
Proper base change identifies the stalk of $Rj_!\mathbb Z_{\mathbb R}$ at
$y$ with compactly supported cohomology of $j^{-1}(y)$. That fibre is one
point for $y\in b$ and empty otherwise. Thus $Rj_!\mathbb Z_{\mathbb R}$
is concentrated in degree zero, equals $F$, and has stalk $\mathbb Z$ on
$b$ and zero off $b$. The same fibre calculation for arbitrary sheaves on
$\mathbb R$ shows that $j_!$ has cohomological dimension zero.

For $y\in X$ use the additive orbit parameter
$r_y(s)=a(y,e^s)$. If $y=j(u_0)$, the fibre product of $r_y$ and $j$ is
the graph $\{(s,u_0+s):s\in\mathbb R\}$, with its usual graph topology.
Projection to $s$ is a homeomorphism. If $y\notin b$, the fibre product is
empty. Proper base change for these squares gives the sheaf isomorphisms

$$
r_y^{-1}F\simeq
\begin{cases}
\mathbb Z_{\mathbb R},&y\in b,\\
0,&y\notin b.
\end{cases}
$$

These are isomorphisms of sheaves, not merely identifications of stalk
groups. Hence $F$ is conic according to SH02-CON-DEFINITION.

We now show that $F|_b$ is not locally constant when $b$ carries its topology
as a subset of $X$. Fix $x=j(u_0)$ and a section $s\in F(U)$ over an
ambient open neighbourhood $U$ of $x$. Choose a compact neighbourhood
$K\subset U$ of $x$. If $C\subset j^{-1}U$ is the closed support of the
section defining $s$, properness makes $C\cap j^{-1}K$ compact in
$\mathbb R$, hence bounded. Consequently there is $R$ such that the germ
of $s$ at every $j(u)\in K$ with $|u|>R$ is zero.

There are positive integers $m_k\to\infty$ such that the distance of
$m_k\lambda$ to $\mathbb Z$ tends to zero. Indeed, subdividing $0,1)$
into $N$ equal intervals and comparing the $N+1$ fractional parts of
$0,\lambda,\ldots,N\lambda$ gives an integer $1\le m\le N$ with
distance at most $1/N$. Such integers cannot stay in a finite set as the
distance tends to zero, since $\lambda$ is irrational. Passing to an
unbounded subsequence proves the assertion. Therefore

$$
u_k=u_0+2\pi m_k\longrightarrow+\infty,\qquad j(u_k)\longrightarrow x.
$$

For all sufficiently large $k$, these points lie in the interior of $K$
and their germs of $s$ vanish. Every ambient section with nonzero germ at
$x$ consequently has zero germs at points of $b$ arbitrarily near $x$.

If $F|_b$ were locally constant near $x$, a local trivialization and the
nonzero element $1\in F_x=\mathbb Z$ would provide a section with nonzero
germ everywhere on some relative neighbourhood of $x$. By the definition
of inverse image to a subspace, that section is represented, after a
further relative shrink around $x$, by an ambient section of $F$. The
recurrent zero germs just proved give a contradiction.

Thus conicity along parameter maps, equivalently along homogeneous-space
orbits, does not imply local constancy on an orbit with its induced
subspace topology. Local constancy for the induced topology does imply the
parameter condition, since the parameter map to that subspace is
continuous and inverse image preserves locally constant sheaves. The
implication is therefore strict. In particular, an equivalence formulated
using parameter pullbacks cannot simply replace that condition by local
constancy on induced-subspace orbits. This independently proved topology
obstruction is distinct from the periodic-action failure in
SH02-CON-RESTRICTION. $\square$

**The topology distinction in pictures.** Specialize the example to
$\lambda=\sqrt2$. The first figure shows the orbit on a standard embedded
torus; the second separates long parameter travel from small return
distance and shows why proper supports obstruct an induced-orbit
trivialization.

![A finite irrational orbit segment on a torus, with its initial point and a later return marked

The blue curve samples $j(u)$ for $0\le u\le20\pi$ at 6,001 parameter
values. It is shown through the embedding
$E(\theta,\phi)=((1.8+0.6\cos\phi)\cos\theta,
(1.8+0.6\cos\phi)\sin\theta,0.6\sin\phi)$, with
$\theta=u$ and $\phi=\sqrt2u$. The red point is $j(0)$ and the gold point
is $j(10\pi)$; the latter has second-circle angle
$2\pi/(5\sqrt2+7)$ modulo $2\pi$. The gray grid describes the ambient
torus and is not sheaf support. Curve thickness is only a drawing aid.

![Exact return samples and the proper-support mechanism in the dense-orbit counterexample](../assets/conic-orbit-topology.png)

For the displayed pairs $(m,n)=(5,7),(12,17),(29,41),(70,99),(169,239)$,
put $u=2\pi m$ and
$\epsilon=m\sqrt2-n=(2m^2-n^2)/(m\sqrt2+n)$. The first circle
coordinate of $j(u)$ is exactly $1$. The right panel magnifies the second
circle; its labelled distance is the Euclidean chord
$|e^{2\pi i\epsilon}-1|=2|\sin(\pi\epsilon)|$, not an intrinsic metric
on the orbit. The lower panel depicts the proof above: properness of a
section's support over a compact neighbourhood bounds the parameters of
its nonzero germs, while recurrence supplies arbitrarily large parameters
whose images return near the basepoint. Those returning germs must vanish.
No numerical bound for an arbitrary section is asserted.

These are finite illustrations of SH02-CON-EXAMPLE-DENSE-ORBIT. The full
density, recurrence and sheaf arguments remain above. The proper-support
definition used in that proof is compared with Schapira's Definition 4.2.2
and Remark 4.2.5, pp. 85–86: compactness over each compact subset of the
target bounds the returning parameters of any one section's support.
The dense-orbit example and its drawings are independently authored course
material illustrating the mathematical distinction proved here. A
vector copy of the return and support panels
preserves the exact labels.

## SH02-CON-COMPARISON — Canonical transport and its normalization

For any $F\in D^+(X)$ let $K=a^{-1}F$. Define

$$
u_F:Rp_*K\longrightarrow F
$$

by applying $Rp_*$ to the unit $K\to Re_*e^{-1}K$ and using
$p\circ e=a\circ e=\operatorname{id}_X$. There are two specified maps

$$
\alpha_F:p^{-1}Rp_*a^{-1}F\longrightarrow a^{-1}F,
\qquad
\beta_F=p^{-1}u_F:p^{-1}Rp_*a^{-1}F\longrightarrow p^{-1}F,
$$

where $\alpha_F$ is the counit for $p^{-1}\dashv Rp_*$. These definitions
specify the maps, not just their source and target objects.

**Theorem.** The following conditions on $F$ are equivalent:

1. $F$ is conic.
2. Every $H^j(a^{-1}F)$ is locally constant on every fibre of $p$.
3. Both $\alpha_F$ and $\beta_F$ are isomorphisms.
4. There exists an isomorphism $p^{-1}F\simeq a^{-1}F$ in $D^+(X\times G)$.
5. There exists an isomorphism $p^!F\simeq a^!F$.

When these conditions hold, there is a canonical transport isomorphism

$$
\theta_F=\alpha_F\circ\beta_F^{-1}:
p^{-1}F\longrightarrow a^{-1}F. \tag{SH02-CON-THETA}
$$

It is natural in $F$ and its restriction along $e$ is the identity.

**Proof.** Since inverse image is exact, restriction of
$H^j(a^{-1}F)=a^{-1}H^j(F)$ to $\{x\}\times G$ is exactly
$o_x^{-1}H^j(F)$. This proves the equivalence of the first two conditions.
Under the second condition SH02-CON-CYLINDER applies to $K=a^{-1}F$:
its evaluation is $u_F$ and its counit is $\alpha_F$. Both are
isomorphisms, hence so is $\beta_F$. The third condition gives the fourth
by the displayed definition of $\theta_F$. Conversely, any isomorphism in
the fourth condition identifies the cohomology of $a^{-1}F$, on each
$p$-fibre, with the constant cohomology of $p^{-1}F$, giving condition two.

For condition five, the homeomorphism

$$
h:X\times G\longrightarrow X\times G,\qquad h(x,t)=(a(x,t),t)
$$

has inverse $(y,t)\mapsto(a(y,t^{-1}),t)$, and $a=p\circ h$. Thus both
$p$ and $a$ are topological submersions of relative dimension one. Orient
their fibres by the coordinate $\log t$; $h$ preserves that coordinate.
The submersion identity gives $p^!F\simeq p^{-1}F[1]$ and
$a^!F\simeq a^{-1}F[1]$. Shifting by $[-1]$ proves the equivalence with
condition four, without an orientation sign change.

Finally, restriction of the counit $\alpha_F$ by $e^{-1}$ is precisely
$u_F$. The same is true of $e^{-1}\beta_F$, by $e^{-1}p^{-1}=\mathrm{id}$.
Their quotient is the identity. Every construction used a unit, counit,
or its inverse naturally, proving naturality. $\square$

**The precise reach of the transport tests.** Let $I(F)$ mean induced-orbit
conicity, $P(F)$ parameter conicity, and $H(F)$ homogeneous-orbit conicity.
The existing topology comparison and the theorem give, under exactly the
hypotheses of SH02-CON-CONTRACT,

$$
I(F)\Longrightarrow P(F)\Longleftrightarrow H(F)
\Longleftrightarrow (2)\Longleftrightarrow (3)
\Longleftrightarrow (4)\Longleftrightarrow (5).
$$

To make the logical issue explicit, consider a proposed three-condition
criterion labelled (i) induced-orbit conicity, (ii) invertibility of the
comparison maps, and (iii) fibrewise local constancy. Conditions (ii) and
(iii) are conditions three and two above. With condition (i) read as $I(F)$,
none of the four transport tests implies $I(F)$ in the stated generality.
The same sheaf in SH02-CON-EXAMPLE-DENSE-ORBIT satisfies all four tests and
fails $I(F)$.

The fibre-pullback identity in the first sentence of our proof is valid for
every $F$ and proves $(2)\Longleftrightarrow P(F)$. Together with $I(F)
\Rightarrow P(F)$ it proves the forward implication (i)$\Rightarrow$(iii)
in that proposed criterion, but not the false converse (iii)$\Rightarrow$(i).
Thus the theorem supplies the full parameter/homogeneous equivalence and
all valid induced-orbit implications, without adding an embedded-orbit
hypothesis. These are independently proved implications between the
definitions in this unit; they make no claim about the wording or intended
meaning of an unconsulted source.

**Corollary.** $D_G^+(X)$ is closed under shifts, cones of morphisms between
its objects, and cohomological truncations.

**Proof.** Truncations and shifts preserve the defining orbital-pullback
condition. For cones, use the natural transformations $\alpha$ and $\beta$:
their source and target functors are triangulated. In the comparison of the
two distinguished triangles, isomorphisms at the first two vertices force an
isomorphism at the third. SH02-CON-COMPARISON applies to the cone. $\square$

## SH02-CON-COCYCLE — What the canonical transport actually proves

**Proposition.** $\theta_F$ is the unique isomorphism
$p^{-1}F\to a^{-1}F$ whose restriction at $t=1$ is the identity. On
$X\times G\times G$ it satisfies

$$
\theta_F(x,st)=\theta_F(a(x,s),t)\circ\theta_F(x,s). \tag{SH02-CON-COCYCLE-EQ}
$$

Here the formula denotes equality of the corresponding pullback morphisms
in the derived category, not a formula between chosen complexes of stalks.

**Proof.** For any other normalized isomorphism $\phi$, the composite
$\theta_F^{-1}\phi$ is an automorphism of $p^{-1}F$. Full faithfulness in
SH02-CON-CYLINDER says it is the pullback of one automorphism of $F$; applying
$e^{-1}$ identifies that automorphism with the identity. This proves
uniqueness.

For the second assertion, the two sides are maps from $q^{-1}F$ to
$c^{-1}a^{-1}F$, where $q(x,s,t)=x$ and $c(x,s,t)=(x,st)$. The left side is
an isomorphism, and both sides restrict to the identity at $(s,t)=(1,1)$.
Compose the right side with the inverse of the left side. The result is an
endomorphism of $q^{-1}F$. Full faithfulness for $X\times G^2\to X$ and
restriction at $(1,1)$ make it the identity. This is the required equality.
$\square$

This proves normalized action data and its cocycle equality in the ordinary
derived category. It makes no claim about a chosen dg or infinity-categorical
equivariant enhancement or about higher coherences. Those are different
constructions and have not been imported by the mere existence of an
isomorphism in condition four.

## SH02-CON-INTERVAL-FIBRES — An open-submersion calculation

**Lemma.** Let $B$ be locally compact Hausdorff, let $W$ be an open subset
of $B\times\mathbb R$, and let
$r:W\to B$ be the projection. Suppose each fibre $W_b$ is a nonempty
interval. For every $L\in D^+(B)$ the unit
$L\to Rr_*r^{-1}L$ is an isomorphism.

**Proof.** The map $r$ is an oriented topological submersion of relative
dimension one and has finite cohomological dimension for proper direct
image. Its relative dualizing object is
$\omega_r=r^!A_B\simeq A_W[1]$. Consider the trace

$$
\operatorname{tr}:Rr_!\omega_r\longrightarrow A_B.
$$

By proper base change its stalk at $b$ is the integration morphism
$R\Gamma_c(W_b;A[1])\to A$. A nonempty open interval, bounded or unbounded,
is orientation-preservingly homeomorphic to $\mathbb R$, so this is an
isomorphism by the positive-interval trace normalization and submersion base-change identity. Stalk detection proves that the
trace is an isomorphism.

The submersion formula and the bounded-first-input internal duality proof identify

$$
\begin{aligned}
Rr_*r^{-1}L
&\simeq Rr_*R\mathcal Hom(\omega_r,r^!L)\\
&\simeq R\mathcal Hom(Rr_!\omega_r,L)\\
&\simeq R\mathcal Hom(A_B,L)\simeq L.
\end{aligned}
$$

The first identity cancels the common shift $[1]$ in the two internal-Hom
arguments; $A_W$ is the tensor unit, so it needs no stalk-finiteness
assumption. Under the second identity, precomposition with the trace is the
unit $L\to Rr_*r^{-1}L$: this is the tensor-Hom adjunction identity for
the counit $Rr_!r^!A_B\to A_B$. Thus the displayed isomorphism proves the
assertion for the specified unit.

Here is the map check with its tensor order explicit. Write $\epsilon_r(L):Rr_!r^!L\to L$ for the counit, and let $\theta:\omega_r\otimes r^{-1}L\to r^!L$ be the submersion tensor isomorphism, with the relative dualizing factor first. Its defining trace identity, (EX.24), identifies the composite

$$
Rr_!\omega_r\otimes L
\xrightarrow{\pi}Rr_!(\omega_r\otimes r^{-1}L)
\xrightarrow{Rr_!\theta}Rr_!r^!L
\xrightarrow{\epsilon_r(L)}L
$$

with $\epsilon_r(A_B)\otimes1_L$, followed by $A_B\otimes L\simeq L$.

To see the unit explicitly, put $H=R\mathcal Hom(\omega_r,r^!L)$ and let $\lambda:r^{-1}L\to H$ be the curry of $\theta$. The submersion formula makes $\lambda$ an isomorphism. Write $\eta_L:L\to Rr_*r^{-1}L$ and $\delta_H:r^{-1}Rr_*H\to H$ for the ordinary unit and counit. The map in question, after internal duality, is

$$
L\xrightarrow{\eta_L}Rr_*r^{-1}L
\xrightarrow{Rr_*\lambda}Rr_*H
\longrightarrow R\mathcal Hom(Rr_!\omega_r,L).
$$

Uncurry using the evaluated construction (EX.22). Naturality of the ordinary counit and its triangle identity give

$$
\delta_H\circ r^{-1}Rr_*\lambda\circ r^{-1}\eta_L
=\lambda\circ\delta_{r^{-1}L}\circ r^{-1}\eta_L
=\lambda.
$$

Evaluation of $\omega_r\otimes\lambda$ is $\theta$, so this uncurry is precisely the displayed projection–tensor–trace composite. Currying the equal composite $\epsilon_r(A_B)\otimes1_L$ is exactly precomposition with the trace. Thus the identity concerns the original unit, with the signs fixed by the same tensor order. Here $\omega_r\simeq A_W[1]$ is bounded, so the bounded-first-input internal-Hom proof, (EX.20)–(EX.22), applies with the arbitrary bounded-below second input $L$; no unbounded internal-Hom extension is used.

This proof uses proper base change for
$Rr_!$; it never invokes unrestricted nonproper base change for $Rr_*$.
$\square$

## SH02-CON-RESTRICTION — Restricting sections without losing a winding

For an open $U\subset X$ and $x\in X$ define the open subset of the parameter
group

$$
T_x(U)=\{t>0:a(x,t^{-1})\in U\}.
$$

**Theorem.** Suppose $T_x(U)$ is a nonempty interval in the coordinate
$\log t$ for every $x$. For conic $F\in D_G^+(X)$ the restriction map

$$
R\Gamma(X;F)\longrightarrow R\Gamma(U;F|_U)
$$

is an isomorphism.

**Proof.** Let $b:U\times G\to X$ be the restricted action. The change of
coordinates $h$ used above identifies this map with the projection from

$$
W=\{(x,t)\in X\times G:a(x,t^{-1})\in U\}
$$

to $X$. This is open because $U$ is open and the inverse action is
continuous. Its fibre at $x$ is $T_x(U)$. SH02-CON-INTERVAL-FIBRES therefore
makes the unit $F\to Rb_*b^{-1}F$ an isomorphism.

Restrict $\theta_F$ to $U\times G$. It identifies $b^{-1}F$ with
$p_U^{-1}(F|_U)$, where $p_U:U\times G\to U$. The cylinder lemma and
composition of direct images give isomorphisms

$$
R\Gamma(X;F)
 \longrightarrow R\Gamma(U\times G;b^{-1}F)
 \simeq R\Gamma(U\times G;p_U^{-1}(F|_U))
 \longrightarrow R\Gamma(U;F|_U).
$$

The first map is pullback along $b$ and the last is evaluation along
$u\mapsto(u,1)$. Since $\theta_F$ is the identity along that section, the
composite is exactly pullback along $U\hookrightarrow X$, that is,
restriction. Hence it is the required isomorphism. $\square$

**Why the parameter fibre matters.** A contractible intersection of an open
set with the image of an orbit does not suffice for a general action. Take
$A=\mathbb Z$, $X=S^1$, and

$$
a(z,t)=e^{i\log t}z,\qquad U=S^1\setminus\{1\},\qquad F=\mathbb Z_X.
$$

There is one orbit, its intersection with $U$ is a nonempty contractible open
arc, and $F$ is conic. Nevertheless

$$
H^1(X;F)=\mathbb Z,\qquad H^1(U;F|_U)=0.
$$

For completeness, cover the circle by two contractible arcs whose intersection
has two contractible components. Their constant-sheaf Cech complex has
$\mathbb Z^2$ in degrees zero and one, with differential, after compatible
trivializations, $(a,b)\mapsto(b-a,b-a)$. Its kernel and cokernel are both
$\mathbb Z$; interval acyclicity makes this Cech computation valid. The
arc $U$ is acyclic by SH02-IMPORT-INTERVAL. Thus the restriction in degree
one is the zero map from a nonzero group.

In this example $\log T_x(U)$ is a disjoint union of infinitely many open
intervals, rather than one interval. The same computation works with any
nonzero allowed coefficient ring. An orbit-image version of the criterion
is therefore false as a statement for arbitrary positive-real actions.
SH02-CON-RESTRICTION states and proves a sufficient condition on the actual
parameter fibres. The counterexample is retained with its complete
cohomology calculation; no correspondence with an unconsulted source or
errata entry is needed for the conclusion. For vector-bundle scaling the
parameter fibres required below really are intervals.

## SH02-CON-RADIAL-STAR — Ordinary contraction to the zero section

Let $\tau:E\to Z$ be a real vector bundle of finite rank $n$ over a locally
compact space. Give $E$ the action $(v,t)\mapsto tv$, and let
$i:Z\hookrightarrow E$ be its zero section. No orientation of $E$ or $Z$
is chosen. For $F\in D_G^+(E)$ define

$$
\rho_F:R\tau_*F\longrightarrow i^{-1}F
$$

by restricting the counit $\tau^{-1}R\tau_*F\to F$ to $i$.

**Theorem.** $\rho_F$ is an isomorphism.

**Proof.** This can be checked on stalks at $z\in Z$. Trivialize the bundle
over an open neighbourhood of $z$ and use a Euclidean norm on that
trivialization. For an open $V$ in the trivializing neighbourhood and
$\varepsilon>0$, set
$U_{V,\varepsilon}=V\times B_\varepsilon\subset V\times\mathbb R^n$.
For $(v,w)$ with $w\ne0$, the parameter fibre in the restriction theorem is

$$
\{t>0:|w|/t<\varepsilon\}=(|w|/\varepsilon,\infty).
$$

For $w=0$ it is all of $G$. Thus SH02-CON-RESTRICTION gives

$$
R\Gamma(\tau^{-1}V;F)\longrightarrow
R\Gamma(U_{V,\varepsilon};F)
$$

as an isomorphism. These are actual restrictions, so the isomorphisms are
compatible as $V$ and $\varepsilon$ shrink. The sets
$U_{V,\varepsilon}$ form a neighbourhood basis of $i(z)$: in a product
topology, every neighbourhood of $(z,0)$ contains such a product.

For each degree $q$, taking filtered colimits yields

$$
\begin{aligned}
H^q(R\tau_*F)_z
 &=\varinjlim_{V\ni z}H^q(\tau^{-1}V;F)\\
 &\simeq\varinjlim_{V\ni z,\,\varepsilon>0}
       H^q(U_{V,\varepsilon};F)
 =H^q(F)_{i(z)}.
\end{aligned}
$$

Exactness of filtered colimits justifies passage to cohomology. The map in
this display is induced by restriction to germs, hence is $H^q(\rho_F)_z$.
It is an isomorphism for every $q$ and $z$. $\square$

The proof is local on the base and therefore needs neither a global bundle
metric nor a paracompactness assumption on $Z$. It also explains why a
nonproper map $\tau$ is allowed: no properness of $\tau$ was invoked.

## SH02-CON-RADIAL-SUPPORT — Proper-support contraction

Define a natural morphism in the other direction by the closed-embedding
counit:

$$
\sigma_F:i^!F\simeq R\tau_!i_*i^!F\longrightarrow R\tau_!F.
$$

Here $i$ is proper and $\tau\circ i=\operatorname{id}_Z$. The rank of
$\tau$ is finite, so $\tau_!$ has finite cohomological dimension and all
displayed functors are defined on $D^+$.

**Theorem.** For every $F\in D_G^+(E)$, $\sigma_F$ is an isomorphism.

**Proof.** First assume $n>0$ and work in a local trivialization over $V$.
Write

$$
Y_V=V\times\mathbb R^n,\quad S_V=V\times\{0\},\quad
C_{V,R}=V\times\overline B_R\qquad(R>0).
$$

On the invariant open space $Y_V\setminus S_V$, take the open subset
$Y_V\setminus C_{V,R}$. Every point $(v,w)$ of the former has $w\ne0$,
and its parameter fibre for the latter is $(0,|w|/R)$. It is a nonempty
interval. SH02-CON-RESTRICTION therefore shows that

$$
R\Gamma(Y_V\setminus S_V;F)\longrightarrow
R\Gamma(Y_V\setminus C_{V,R};F)
$$

is an isomorphism. Compare the two localization triangles

$$
\begin{aligned}
R\Gamma_{S_V}(Y_V;F)&\longrightarrow R\Gamma(Y_V;F)
                    \longrightarrow R\Gamma(Y_V\setminus S_V;F)
                    \longrightarrow,\\
R\Gamma_{C_{V,R}}(Y_V;F)&\longrightarrow R\Gamma(Y_V;F)
                    \longrightarrow R\Gamma(Y_V\setminus C_{V,R};F)
                    \longrightarrow.
\end{aligned}
$$

The vertical maps are inclusion of supports, the identity, and restriction.
The last two are isomorphisms, hence so is

$$
R\Gamma_{S_V}(Y_V;F)\longrightarrow
R\Gamma_{C_{V,R}}(Y_V;F). \tag{SH02-CON-DISK-SUPPORT}
$$

It remains to check the support limit, since fibre compactness alone is not
global properness. Each $C_{V,R}\to V$ is proper. Conversely, take a closed
support $C\subset Y_V$ proper over $V$, and fix $z\in V$. Choose a smaller
neighbourhood $V'$ of $z$ whose closure is compact and contained in $V$;
local compactness and the Hausdorff condition provide it. Properness makes
$C\cap\tau^{-1}(\overline{V'})$ compact. The norm in the trivialization is
bounded on this compact set, so after choosing $R$ we have
$C\cap\tau^{-1}V'\subset C_{V',R}$. Thus closed disk supports are cofinal
in the system of proper supports after passage to the stalk at $z$.

By SH02-IMPORT-PROPER-SUPPORTS and this cofinality,

$$
\begin{aligned}
H^q(i^!F)_z
 &=\varinjlim_{V\ni z}H^q_{S_V}(Y_V;F),\\
H^q(R\tau_!F)_z
 &=\varinjlim_{V\ni z,\,R>0}H^q_{C_{V,R}}(Y_V;F).
\end{aligned}
$$

The first equality also uses $i_*i^!F=R\Gamma_{i(Z)}F$. The compatible
isomorphisms (SH02-CON-DISK-SUPPORT) identify these two colimits. Their map is
inclusion of zero-section support into proper support, hence is exactly
$H^q(\sigma_F)_z$. This proves the theorem.

If $n=0$, then $E=Z$ and $i=\tau=\mathrm{id}$. Both $\rho_F$ and
$\sigma_F$ are the identity. This also avoids inserting a fictitious sphere
or punctured fibre into the argument. If $Z=\varnothing$, all objects and
maps are zero and both assertions hold. $\square$

There is no orientation twist or shift in either contraction comparison.
Orientation and shifts enter only when the resulting stalk or costalk is
subsequently computed. The proof of proper-support contraction did not use
Verdier double-dual reflexivity, which would require unjustified finiteness
hypotheses for the objects allowed here.

## SH02-CON-FUNCTORS — Transport through sheaf operations

Let $f:Y\to X$ be a continuous equivariant map of locally compact
$G$-spaces. In this section assume $f_!$ has finite cohomological dimension,
so that $f^!$ is available in the
stated formalism. Set $\widetilde f=f\times\mathrm{id}_G$. Its proper
direct image has the same finite cohomological-dimension bound, by proper
base change on the identical fibres.

**Theorem.** If $F\in D_G^+(X)$ and $K\in D_G^+(Y)$, then

$$
f^{-1}F,\ f^!F\in D_G^+(Y),\qquad
Rf_*K,\ Rf_!K\in D_G^+(X).
$$

If $F_1,F_2\in D_G^+(X)$, their derived tensor product is conic. If in
addition $F_1\in D^-(X)$, then $R\mathcal Hom(F_1,F_2)$ is conic and
belongs to $D^+(X)$. Since $F_1$ was already bounded below, this last
hypothesis makes $F_1$ bounded; it does not say that it is perfect or has
finite-rank stalks.

**Proof.** We check each comparison and its required base change.

For inverse image, equivariance and $p_X\widetilde f=fp_Y$ give

$$
a_Y^{-1}f^{-1}F
\simeq\widetilde f^{-1}a_X^{-1}F
\simeq\widetilde f^{-1}p_X^{-1}F
\simeq p_Y^{-1}f^{-1}F.
$$

The middle map is transport for $F$, with its direction inverted as needed.
SH02-CON-COMPARISON proves conicity.

For extraordinary inverse image, functoriality of $!$ for the two commuting
composites gives

$$
a_Y^!f^!F\simeq\widetilde f^!a_X^!F
\simeq\widetilde f^!p_X^!F\simeq p_Y^!f^!F.
$$

The middle isomorphism is the shift of transport by $[1]$. The orientations
used for $a_Y,p_Y,a_X,p_X$ all use $\log t$, preserved by
$\widetilde f$. Hence their relative shifts agree and no minus sign is
introduced. The extraordinary version of SH02-CON-COMPARISON applies.

For proper direct image, both squares with horizontal maps $p_Y,p_X$ and
with horizontal maps $a_Y,a_X$ are Cartesian. For the action square this
deserves verification: given $(x,t)$ and $y$ with $a_X(x,t)=f(y)$, the
unique preimage is $(a_Y(y,t^{-1}),t)$, because equivariance gives
$f(a_Y(y,t^{-1}))=x$. Proper base change therefore supplies

$$
a_X^{-1}Rf_!K\simeq R\widetilde f_!a_Y^{-1}K
\simeq R\widetilde f_!p_Y^{-1}K
\simeq p_X^{-1}Rf_!K.
$$

Here $f$ need not be proper: base change is for $Rf_!$, whose supports
are already proper over the target.

For ordinary direct image we justify the product base-change map instead
of applying nonproper base change indiscriminately. The canonical map

$$
p_X^{-1}Rf_*K\longrightarrow R\widetilde f_*p_Y^{-1}K
$$

is an isomorphism on stalks. Indeed, rectangles $V\times I$ with $I$ an
open interval form a neighbourhood basis at $(x,t)$. The right-hand stalk
is the filtered colimit of
$H^j(f^{-1}V\times I;p_Y^{-1}K)$, which the cylinder lemma identifies
naturally with $H^j(f^{-1}V;K)$, with the canonical pullback map providing
that identification. Their colimit is $H^j(Rf_*K)_x$, the left-hand stalk.
The same holds for the action square by applying the homeomorphisms
$h_X,h_Y$; equivariance gives
$h_X\widetilde f=\widetilde f h_Y$. Thus

$$
a_X^{-1}Rf_*K\simeq R\widetilde f_*a_Y^{-1}K
\simeq R\widetilde f_*p_Y^{-1}K
\simeq p_X^{-1}Rf_*K,
$$

and conicity follows. The rectangle argument is valid for bounded-below
complexes because inverse image and stalk formation are exact and the
cylinder lemma was proved in $D^+$.

For tensor products, exact inverse image commutes with derived tensor, and
therefore

$$
a_X^{-1}(F_1\otimes^L F_2)
\simeq a_X^{-1}F_1\otimes^L a_X^{-1}F_2
\simeq p_X^{-1}F_1\otimes^L p_X^{-1}F_2
\simeq p_X^{-1}(F_1\otimes^L F_2).
$$

If the two lower cohomological bounds are $b_1,b_2$, finite global dimension
$d$ gives lower bound $b_1+b_2-d$ for their derived tensor product. Thus it
really is an object of $D^+$, as required by the conicity criterion.

For internal Hom, put $H=R\mathcal Hom(F_1,F_2)$. If $F_1$ has upper
bound $c$ and $F_2$ lower bound $b$, derived Hom has lower bound $b-c$.
The extraordinary inverse-image/internal-Hom comparison, (EXA.2), gives

$$
\begin{aligned}
a_X^!H
&\simeq R\mathcal Hom(a_X^{-1}F_1,a_X^!F_2)\\
&\simeq R\mathcal Hom(p_X^{-1}F_1,p_X^!F_2)
\simeq p_X^!H.
\end{aligned}
$$

This proves conicity by the extraordinary comparison criterion. It does
not assume that arbitrary inverse image commutes with internal Hom, an
identity which would require additional justification. $\square$

All comparisons in this proof are composites of specified units, counits,
base-change maps, functor-composition maps, and $\theta$. Their restrictions
at $t=1$ are identities by the adjunction and base-change identities. Hence
they give the canonical transport on the resulting conic object by
SH02-CON-COCYCLE. In particular this compatibility statement is independent
of a chosen isomorphism witnessing condition four.

**External products.** If $F\in D_G^+(X)$ and $K\in D_G^+(Y)$, put
$F\boxtimes^L K=\mathrm{pr}_X^{-1}F\otimes^L\mathrm{pr}_Y^{-1}K$.
It is invariant under the two scaling parameters independently: pullback
by $(x,y,s,t)\mapsto(a_X(x,s),a_Y(y,t))$ is identified with pullback by
the projection using the two transport isomorphisms and tensor. Thus its
cohomology is locally constant along each parametrized $G^2$-orbit. This
is what **biconic** means here. Pulling this isomorphism back along $s=t$
proves conicity for the diagonal action. Finite global dimension gives the
same lower bound as for tensor, so the external product remains in $D^+$.

## SH02-CON-EXAMPLE — A large angular family with zero ordinary sections

Let $E=Z\times\mathbb R^2$ and let
$j:Z\times(\mathbb R^2\setminus\{0\})\hookrightarrow E$ be the open
embedding. Define

$$
q:Z\times(\mathbb R^2\setminus\{0\})\longrightarrow Z\times S^1,
\qquad q(z,v)=(z,v/|v|),
$$

and let $s:Z\times S^1\to Z$. For an arbitrary
$L\in D^+(Z\times S^1)$ set $F=j_!q^{-1}L$. The angular data $L$ need
not be locally constant, constructible, or of finite rank.

The action on $Z\times S^1$ is trivial. Every object there is conic,
because each parametrized orbit is a constant map. Both $q$ and $j$ are
equivariant; the fibres of $q$ are one-dimensional and $j_!$ is exact, so
the functor theorem proves that $F$ is conic. Since extension by zero has
zero stalks along the complement of its open domain, $i^{-1}F=0$.
Ordinary contraction therefore gives

$$
R\tau_*F=0.
$$

Polar coordinates identify $q$ with projection from
$(Z\times S^1)\times(0,\infty)$, with radial orientation $dr$.
The projection formula and interval integration give
$Rq_!q^{-1}L\simeq L[-1]$. Composition of proper direct images, and
properness of $s$, now give

$$
R\tau_!F\simeq Rs_*L[-1],\qquad i^!F\simeq Rs_*L[-1].
$$

This displays a conic sheaf whose ordinary direct image vanishes while its
proper direct image can be large. It also tests the direction of both
contraction maps: the ordinary one reads a stalk, while the proper one reads
a costalk.

For a concrete non-finite module, take $Z$ to be a point, $A=\mathbb Z$,
and $L=M_{S^1}$ with
$M=\mathbb Q\oplus\bigoplus_{m\ge1}\mathbb Z/2\mathbb Z$.
The two-arc Cech complex used above is now
$[M^2\xrightarrow{(a,b)\mapsto(b-a,b-a)}M^2]$.
Splitting its source into diagonal and difference coordinates and its target
into diagonal and a complementary coordinate gives one copy of $M$ in
degree zero, one in degree one, and a contractible identity summand.
Consequently

$$
R\Gamma(S^1;M_{S^1})\simeq M\oplus M[-1],\qquad
R\Gamma_c(E;F)\simeq M[-1]\oplus M[-2].
$$

Every use of interval acyclicity in this calculation applies to this
arbitrary module. No finite-rank substitute was made.

## SH02-CON-EXERCISE-MONODROMY — Transport after one period

**Exercise.** Give $S^1$ the action $a(z,t)=e^{i\log t}z$. Let $N$ be any
$A$-module and let $T:N\to N$ be an automorphism. Let $L_T$ be the locally
constant sheaf whose positive monodromy is $T$. Compute its cohomology and
the restriction to $U=S^1\setminus\{1\}$. Determine the canonical action
transport at $t=e^{2\pi}$ after identifying the fibre at one chosen point
with $N$.

**Solution.** Trivialize on two arcs as in the circle calculation, using one
intersection component to identify the trivializations and the other to
record $T$. The Cech differential is, with one choice of ordering,

$$
N\oplus N\longrightarrow N\oplus N,
\qquad (u,v)\longmapsto(v-u,v-Tu).
$$

Subtract the first target coordinate from the second, and write the source
in coordinates $(u,w=v-u)$. The differential becomes
$(u,w)\mapsto(w,(1-T)u)$. The identity map on the $w$ coordinate is a
contractible summand, leaving the two-term complex
$[N\xrightarrow{1-T}N]$ in degrees zero and one. All intersections are
acyclic for a locally constant sheaf by the interval import, so this complex
computes derived sections. Hence

$$
H^0(S^1;L_T)=\ker(T-1),\quad
H^1(S^1;L_T)=\operatorname{coker}(T-1),\quad H^j=0\ (j\ne0,1).
$$

The restriction to $U$ is constant with fibre $N$. In degree zero the map
is evaluation of invariant sections, namely $\ker(T-1)\hookrightarrow N$;
in degree one it maps $\operatorname{coker}(T-1)$ to zero. Thus this
restriction need not be an isomorphism even though $U$ meets the orbit in
a contractible arc.

On the parametrized orbit $\mathbb R\to S^1$, increasing $\log t$ traces
the positive path. Local-system transport along that path defines a map
$p^{-1}L_T\to a^{-1}L_T$ restricting to the identity at $t=1$. By
SH02-CON-COCYCLE it equals $\theta_{L_T}$. After one period its value is
therefore $T$, although the underlying homeomorphism of $S^1$ at that
parameter is the identity. A periodic point is not a reason to force the
action transport to be the identity. $\square$

## SH02-CON-EXERCISE-BOUNDARY — Zero rank and a trivial action

**Exercise.** Check the comparison maps for a trivial action and for a
rank-zero bundle. Explain why a radial shift $[n]$ must not be inserted into
either contraction theorem.

**Solution.** For a trivial action $a=p$, and $a^{-1}F=p^{-1}F$ for every
$F\in D^+(X)$. The unit $F\to Rp_*p^{-1}F$ and evaluation are inverse by
the cylinder lemma. The counit and evaluation in the definition of
$\theta_F$ consequently give the identity of $p^{-1}F$; this also follows
from uniqueness of normalized transport. No condition on the cohomology of
$F$ in the $X$ direction appears. The restriction criterion in this case
requires $U=X$: if $x\notin U$, then $T_x(U)$ is empty.

For rank zero, $E=Z$ and both maps $i$ and $\tau$ are identities.
Their units and counits are identities, so $\rho_F$ and $\sigma_F$ are
identities. In positive rank the two theorems identify direct images with
the actual inverse and extraordinary inverse images along the zero section;
any codimension shift is already contained in a separate computation of
$i^!F$. For example, the costalk in SH02-CON-EXAMPLE has degrees one and
two although its ordinary stalk is zero. Inserting another radial shift
would contradict that computed proper cohomology. $\square$

## SH02-CON-BOUNDARY — Scope and remaining proof dependencies

**What the consulted sources establish.** The comparisons here use the
1985 Astérisque 128 edition, §2.1.1, printed pp. 39–41 (PDF pp. 42–44),
and Schapira's *An Introduction to Sheaves on Grothendieck Topologies*,
1 August 2026 version. They concern the actual passages listed below,
not the other works cited within those passages. No statement about an
excluded book's definitions, theorem numbering or errata is needed for
the results of this unit.

| Step in this unit | Consulted passage and its scope | Argument supplied here |
| --- | --- | --- |
| Positive-ray conicity | Astérisque 128, §2.1.1, p. 39, uses bounded-below complexes on a real vector bundle over a locally compact base, with locally constant cohomology on half-lines. Schapira, Definition 5.4.4, p. 114, uses bounded complexes on a finite-dimensional vector bundle over a real manifold. | SH02-CON-DEFINITION specifies parameter pullbacks for general continuous actions. The stabilizer classification proves equivalence with homogeneous-orbit pullback. The proper-support dense-orbit example proves that the induced-subspace condition can be strictly stronger. |
| Cylinder descent and its maps | Schapira, Proposition 3.5.3 and Lemma 3.6.4, pp. 73–75, prove interval constancy and the compact-interval product unit. Exercise 3.18, pp. 78–79, proposes a proper contractible exhaustion argument for bounded complexes. | SH02-CON-CYLINDER first applies proper base change to closed strips, then uses the separate closed-exhaustion bridge for their noncompact open-base restrictions. It checks the evaluation, counit and unit individually. The degreewise spectral sequence is bounded below; a uniform upper bound is unnecessary. |
| Open interval fibres and restriction | Schapira, Theorem 4.5.3 and equation (4.5.4), p. 93, give proper-direct-image base change and its compact-support fibre formula. Proposition 4.6.6, pp. 95–96, identifies internal duality by the counit; Proposition 5.1.9, pp. 107–108, identifies the submersion dualizing object for bounded-below input. | SH02-CON-INTERVAL-FIBRES applies base change to the trace, then internal duality to identify the specified ordinary unit. SH02-CON-RESTRICTION computes the action map's actual fibres and checks that the composite is restriction. The periodic circle and monodromy solution detect why an orbit-image test loses winding. |
| The two radial contractions | Schapira, Exercise 5.13, p. 120, states both contractions for bounded conic objects over a locally compact base of finite soft dimension. It is an exercise, not a proof of the larger scope used here. | SH02-CON-RADIAL-STAR uses a local product-ball basis and compatible restrictions. SH02-CON-RADIAL-SUPPORT compares localization triangles, then proves disk supports cofinal after shrinking at a base point. Both identify the actual maps. Neither uses a global metric, a finite-soft-dimension base, double-dual reflexivity, finite generation, or an extra radial shift. |
| Equivariant operations | Schapira, §§4.4–4.6, pp. 90–98, supplies projection, base-change and adjunction machinery; Proposition 4.6.5 prints the exceptional internal-Hom identity for bounded inputs. Astérisque 128, Propositions 2.1.5–2.1.6, p. 41, concerns vector-bundle Fourier functoriality. | SH02-CON-FUNCTORS proves each action comparison separately, including the Cartesian action square and ordinary product base change by rectangles. Its internal-Hom conclusion uses the explicit exceptional-operation contract at the stated bounds, not an unsupported inverse-image/internal-Hom interchange or a wholesale import of vector-bundle Fourier functoriality. |

The proper-support calculation deserves a further distinction. Schapira's
Definition 4.2.2 and Remark 4.2.5, pp. 85–86, identify sections of proper
direct image by closed supports proper over the target open set. They do
not permit replacing properness by compactness of each individual fibre.
That is why the dense-orbit proof bounds a section's support over a compact
target neighbourhood, and the radial proof shrinks the base before choosing
a disk radius. The support-to-stalk comparison and its derived version are
still named imports in SH02-CON-CONTRACT; the new geometric cofinality
argument is supplied in full here.

The contraction statements themselves are established antecedents, and no
priority claim is made for them or for a restriction criterion. The general
action formulation, normalized maps, topology comparison and counterexamples
are justified by the complete arguments in this reader, under the explicit
definitions and hypotheses stated here.
The independently authored course prose, proofs and figures remain under
the edition's CC0 dedication. The linked human works retain their own terms;
in particular Astérisque 128 carries the Société mathématique de France
1985 copyright notice. Access for consultation does not relicense those works.

This unit proves the parametrized-orbit criterion, its canonical comparisons
and ordinary derived-category cocycle, the actual-parameter restriction theorem
with a counterexample to the overly broad orbit-image assertion, all listed
equivariant operations with their stated boundedness, and both vector-bundle
contractions. Fixed points, periodic actions, nonembedded orbits under the
declared topology, zero rank, empty base, nonproper bundle projections, and
arbitrary coefficient modules are accounted for.

The five prerequisite families in SH02-CON-CONTRACT remain explicit.
The interval evaluation theorem, the closed-exhaustion comparison with its
limit proofs, and the proper-fibre and hypercohomology proofs supply the
cylinder inputs at the stated bounded-below scope. The closed-exhaustion
argument includes noncompact strips; a bounded-complex exercise alone would
not establish that scope. SH02-MD-SUBMERSION and SH02-MD-TRACE supply the
orientation/trace package, its normalization and submersion base-change
compatibility. Other parts of the derived sheaf formalism and the
derived proper-support stalk formula retain their explicitly stated contracts. 
The exceptional internal-Hom contract with bounded-above first input and
bounded-below second input is supplied by SH02-EX-BOUNDED-ABOVE at exactly
that scope. Its finite resolution proof does not impose an upper bound on
the second input. The separate unbounded supported-evaluation proof
supplies the support-forgetting comparison without narrowing its first input;
it is not needed to replace the interval argument above. Other declared
prerequisites retain their own proof obligations.
SH02-CON-EXAMPLE-DENSE-ORBIT proves that an induced-subspace interpretation
of nonembedded orbits can give a strictly smaller category. This unit
supplies no Fourier-Sato
equivalence, specialization, microlocalization, microsupport estimate, or
involutivity proof; these are subsequent course obligations. The source comparisons above do not
by themselves admit the course or discharge its remaining proof dependencies.
