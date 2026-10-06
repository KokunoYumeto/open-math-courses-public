# Holonomic D-modules and duality

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

A holonomic module can contain both a connection on an open set and a contribution supported on its boundary. Duality reverses how those pieces are attached. On the affine line, the Laurent-polynomial module contains the polynomial connection and has a point module as quotient. Its dual has the point module as submodule and the polynomial connection as quotient. Computing this reversal requires a derived Hom, a dimension shift, and a change from right modules to left modules.

Let $k$ be an algebraically closed field of characteristic zero, and let $X$ be a smooth separated variety of finite type, of pure dimension $d$. Write $\mathcal D_X$ for differential operators, $\omega_X=\bigwedge^d\Omega_X^1$, and $\pi:T^*X\to X$. Modules are left modules and are quasi-coherent over $\mathcal O_X$. The Weyl-algebra calculations below hold over any characteristic-zero field. Analytic comparisons use $k=\mathbb C$.

Prerequisites are [characteristic varieties and cycles](good-filtrations-and-the-characteristic-variety.md), [Bernstein growth and finite length](the-bernstein-filtration-and-holonomic-modules.md), and [holonomic localization](bernstein-sato-polynomials.md). We use cohomological complexes: $K[d]^i=K^{i+d}$, so an Ext group originally in degree $d$ moves to degree zero after $[d]$.

## 1. The holonomic category on a variety

A coherent $\mathcal D_X$-module $M$ is **holonomic** if

\[
\dim\operatorname{Ch}(M)\leq d.
\tag{1.1}
\]

The zero module is included. For nonzero $M$, the dimension bound from involutivity proved in the characteristic-variety chapter says that every irreducible component of $\operatorname{Ch}(M)$ has dimension at least $d$. Thus a nonzero holonomic module has pure characteristic dimension $d$. At a smooth point of a component, involutivity says that its tangent space is coisotropic in the $2d$-dimensional symplectic tangent space. Its dimension is $d$, so it is also isotropic: the component is Lagrangian. These are conic algebraic Lagrangians; no regular-singularity condition is part of holonomicity.

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

**Proof.** Write the characteristic cycle using generic local lengths,

\[
\operatorname{CC}(M)=\sum_{\Lambda}m_\Lambda[\Lambda],
\qquad
\mu(M)=\sum_\Lambda m_\Lambda.
\tag{2.4}
\]

There are finitely many components, since $X$ is a variety of finite type and the characteristic support is closed and Noetherian. For nonzero holonomic $M$, every $m_\Lambda$ is a positive integer, so $\mu(M)>0$.

In a short exact sequence of holonomic modules, all nonzero characteristic components have the common dimension $d$. The exact-filtration and generic-length theorem therefore gives

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

Coherent differential-operator modules locally admit finite resolutions by finite projective modules. One standard construction starts with a good filtration: the symbol algebra on a smooth chart is a regular ring of dimension $2d$, so its finite graded module has a finite projective resolution. Locally in the base, graded projective terms become free: reduce modulo the positive-degree ideal, choose homogeneous bases of the resulting finite projective $\mathcal O_X$-modules, and lift them by graded Nakayama. Lift the generators and relations to the filtered module successively; strictness follows by the same lower-degree induction used for good filtrations. A final free graded syzygy lifts to a free syzygy. This supplies the finite local resolutions needed to compute (3.3). In the analytic setting Kashiwara–Schapira, Proposition 11.2.6, gives the stronger local length bound $d$; that proposition is not itself a statement of holonomic duality.

On finite projectives, evaluation is an isomorphism to the double module dual. Applying it term by term to a bounded projective resolution proves derived biduality. The evaluation has the usual complex signs and is natural in maps of complexes. Side change converts the two right/left Hom constructions into (3.3); the two shifts cancel because Hom reverses shifts. Thus

\[
\mathbb D_X\mathbb D_X(K)\simeq K
\tag{3.4}
\]

for coherent bounded complexes. These local evaluation maps glue because their construction is intrinsic.

### Theorem 3.1. Holonomic Ext concentration — stated

For holonomic $M$,

\[
\mathcal Ext_{\mathcal D_X}^{\,i}(M,\mathcal D_X)=0
\quad(i\ne d),
\tag{3.5}
\]

and the right module $\mathcal Ext^d(M,\mathcal D_X)$ is holonomic. Hence $\mathbb D_X(M)$ is a holonomic module in degree zero. The filtered Ext-support estimates needed for (3.5) are not proved here. An algebraic reference is C. Schnell, [*D-modules*, Lecture 8](https://www.math.stonybrook.edu/~cschnell/pdf/notes/d-modules.pdf), Corollary 8.4 and Lemma 8.5, with the sheaf formulation on smooth algebraic varieties in Lecture 12, page 59. Ginzburg, Section 4.3, Corollary 4.3.4, states the same result.

The one-variable cyclic case will be proved completely in Section 4.

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

Generic connection structure and finite length are proved in Section 2 from the characteristic-support and cycle results of the earlier lessons. The duality construction, bidual evaluation, exactness consequences, cyclic Ext calculation, connection dual, the two opposite boundary extensions and all six exercises are worked out here. The general holonomic Ext-concentration theorem and its filtered support estimates are stated external inputs; Section 4 proves the assigned cyclic case independently.

V. Ginzburg, [*Lectures on D-modules*](https://math.berkeley.edu/~nadler/ginzburg.dmodules.pdf), Section 4.3, especially Definition 4.3.1 and Corollary 4.3.4, discusses algebraic holonomic duality. The shift and right/left sides are fixed explicitly in (3.3)–(4.6).

E. Frenkel, [*Lectures on the Langlands program and conformal field theory*](https://arxiv.org/abs/hep-th/0512172), Section 3.6, explains the relation with regular holonomic modules and the operations on their analytic solutions. Bhatt, Blickle, Lyubeznik, Singh and Zhang, [*Applications of perverse sheaves in commutative algebra*](https://arxiv.org/abs/2308.03155), Section 2, theorem on the Riemann–Hilbert correspondence, part (1), records compatibility with duality for **regular** holonomic modules. That analytic correspondence is outside this chapter's proofs and does not restrict the algebraic duality used here to regular modules.
