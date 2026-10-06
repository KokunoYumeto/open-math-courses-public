# Roots and reductive groups of rank one

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI, GPT-6.1 Sol (OpenAI). Original exposition is public domain (CC0). The collected lesson, including the explicitly attributed Stacks passage, is also distributed under the GNU Free Documentation License 1.2.*

The diagonal entries of a matrix act on its off-diagonal entries through ratios. Those ratios are the roots of a general linear group. For an arbitrary reductive group, roots are still characters of a maximal torus, but their one-dimensional spaces need not be globally trivial over the base. This lesson constructs the corresponding groups without using a power-series exponential, and shows why every root carries a copy of the rank-one geometry of $\operatorname{SL}_2$.

We use torus conjugacy, torus deformation, and the centralizer theorem from the preceding two lessons. A reductive $S$-group is smooth affine of finite presentation with connected reductive geometric fibres. A semisimple $S$-group has semisimple geometric fibres. Statements about line bundles and subgroup schemes are made over arbitrary schemes, including nonreduced ones.

## 1. The centre and the two ranks

Let $T$ be a split maximal torus of $G$, and, on an open set where the ranks are constant, write

$$
\mathfrak g=\mathfrak t\oplus\bigoplus_{\alpha\in\Phi}\mathfrak g_\alpha.
$$

For now $\Phi$ means the nonzero weights; we will prove that they form a reduced root system. Put

$$
Z=\bigcap_{\alpha\in\Phi}\ker(\alpha:T\to\mathbf G_m).
$$

The group $Z$ is of multiplicative type. It is precisely the scheme-theoretic centre of $G$. Indeed, its conjugation action on $\mathfrak g$ is trivial. Exactness of invariants for a multiplicative-type group makes $C_G(Z)$ smooth with Lie algebra $\mathfrak g$. Its geometric fibres are therefore all of $G$; the smooth fibrewise isomorphism argument of the preceding lesson gives $C_G(Z)=G$. Conversely any central point belongs to $C_G(T)=T$ and acts trivially on every weight summand, hence lies in $Z$. These constructions agree on overlaps and descend when $T$ is only étale locally split.

The centre need not be smooth: $Z(\operatorname{SL}_n)=\mu_n$, including when the characteristic divides $n$. Its largest subtorus is called the **radical**, denoted $\operatorname{Rad}(G)$. For a group of multiplicative type with character sheaf $M$, this subtorus has character sheaf $M/M_{\mathrm{tors}}$. Thus its rank is locally constant and its formation commutes with base change. The **rank** of $G$ is the dimension of a maximal torus; its **semisimple rank** is

$$
\operatorname{rank}(G)-\dim\operatorname{Rad}(G).
$$

Over an algebraically closed field, the radical also equals the largest smooth connected solvable normal subgroup. Its unipotent radical is normal in $G$ and is trivial by reductivity, so it is a torus; rigidity of torus automorphisms makes it central. Conversely a central torus is connected solvable normal. The quotient by this torus is semisimple: the inverse image of a connected solvable normal subgroup of the quotient would enlarge the radical.

The derived group will be constructed for arbitrary bases after the pinned existence theorem in [Pinnings and the classification of split reductive groups](AG-RG-05.md#the-derived-group). It is semisimple and the multiplication map

$$
\operatorname{Rad}(G)\times G_{\mathrm{der}}\longrightarrow G
$$

is a central isogeny. Its construction uses the root groups established here. We do not assume a relative derived group in constructing these groups. Central quotients, which we do need now, are constructed by graded invariant algebras in Section 7 of the next lesson; that construction does not use coroots. In rank one we will construct the simply connected cover explicitly below.

## 2. Why rank one has only two moving directions

We first prove the geometric rank-one statement, rather than assuming a root classification. Work over an algebraically closed field $k$.

**Lemma 2.1.** If a torus acts linearly on an irreducible projective variety $X$, it has at least $\dim X+1$ fixed points.

**Proof.** Choose a cocharacter separating the finitely many weights of an equivariant projective embedding. Induct on $\dim X$. Choose a lowest-weight basis vector and the complementary coordinate hyperplane. If $X$ lies in that hyperplane, remove the basis vector and repeat. Otherwise the hyperplane section has dimension $\dim X-1$ and has at least $\dim X$ fixed points by induction on an irreducible component. The affine complementary chart has nonnegative cocharacter weights. Sending its cocharacter parameter to zero produces another fixed point, outside the hyperplane. Separation of the torus weights makes it torus-fixed, not merely cocharacter-fixed. The base case is a point. $\square$

**Lemma 2.2 (the curve argument).** Over an algebraically closed field, a smooth projective curve dominated by $\mathbf P^1$ is isomorphic to $\mathbf P^1$.

**Proof.** We use Serre duality for a smooth projective curve, the precise internal prerequisite taught in *Dualizing sheaves and Serre duality for projective schemes* in the coherent-cohomology course: $H^1(C,L)$ is dual to $H^0(C,\omega_C\otimes L^{-1})$. Its provider and current publication state are identified in the prerequisite guide. Local Koszul resolutions in a projective embedding identify $\omega_C$ with $\Omega_{C/k}$: taking the top exterior powers in the conormal sequence gives the same determinant as the top Ext in that resolution.

Here are the remaining curve calculations. For any divisor $D$, adding one point in the divisor exact sequence changes the Euler characteristic of $\mathcal O_C(D)$ by one. Thus, with $g=h^1(\mathcal O_C)$,

$$
\chi(L)=\deg L+1-g.
$$

Every line bundle on a smooth curve has a rational section and is of this form. Duality gives $h^0(\omega_C)=g$ and $h^1(\omega_C)=1$, so $\deg\omega_C=2g-2$. A nonzero section of a line bundle has an effective zero divisor; hence a negative-degree line bundle has no nonzero section.

For a nonconstant separable morphism $f:\mathbf P^1\to C$ of degree $n$, the map $f^*\Omega_C\to\Omega_{\mathbf P^1}$ is a nonzero map of line bundles. Its zero divisor $R$ is effective, and taking degrees gives

$$
-2=n(2g-2)+\deg R.
$$

Pullback multiplies degree by $n$: for a point divisor this is the sum of the lengths of the finite flat fibres over the discrete valuation ring, and the general assertion follows by addition. The displayed equality forces $g=0$.

The inseparable case reduces to this one without any genus assertion about inseparable maps. In characteristic $p$, view $k(C)$ inside $k(t)$, and choose the largest $e$ such that $k(C)\subset k(t^{p^e})$. It exists, since any fixed nonconstant element has finite rational-function degree, divisible by $p^e$ if it lies in that subfield. Put $z=t^{p^e}$. Some element $f(z)$ of $k(C)$ has nonzero derivative: the kernel of the derivative on $k(z)$ is $k(z^p)$, as follows by writing $k(z)$ in the basis $1,z,\ldots,z^{p-1}$ over $k(z^p)$. The extension $k(z)/k(f)$ is separable, by differentiating its rational-function equation, so $k(z)/k(C)$ is separable. It gives a nonconstant separable morphism from the smooth projective curve with field $k(z)$, namely $\mathbf P^1$, to $C$. We have again proved $g=0$.

Choose $q\in C(k)$. The line bundle $L=\mathcal O_C(q)$ has degree one. Duality and $\deg\omega_C=-2$ give $h^1(L)=0$ and $h^0(L)=2$. For any point $x$, the same calculation for $L(-x)$ gives $h^0(L(-x))=1$. Thus $L$ is generated by its two sections. They define a nonconstant map $C\to\mathbf P^1$ whose pullback of $\mathcal O(1)$ has degree one. Its degree is one, so it is a finite birational morphism between smooth curves and hence an isomorphism, by their integrally closed local rings. $\square$

**Proposition 2.3.** A semisimple group of rank one has exactly two Borel subgroups containing a maximal torus, its Borel quotient is $\mathbf P^1$, and the action on that quotient has image $\operatorname{PGL}_2$ and kernel its centre.

**Proof.** The normalizer quotient acts faithfully on the rank-one torus, whose automorphism group is $\{1,-1\}$. It acts simply transitively on the torus-fixed points of the homogeneous projective quotient $G/B$, as proved in the preceding lesson without assuming the full Borel-normalizer theorem. There are at most two such points. There cannot be one: Lemma 2.1 would then make this quotient zero-dimensional, so the connected group would be solvable, contradicting nontrivial semisimplicity. There are therefore two, and Lemma 2.1 makes the quotient a smooth projective curve.

The kernel of the action is the intersection of the conjugates of a Borel. Its reduced identity component is solvable and normal, so is trivial by semisimplicity. Thus the action kernel is finite. In particular a positive-dimensional Borel acts nontrivially on the curve. A connected solvable group over $k$ is a rational variety: its torus times its split unipotent radical has an open affine parametrization, as in the solvable-group discussion in the first lesson. A nonconstant orbit map therefore restricts to a nonconstant rational map from an affine line, by fixing all but one of these coordinates. Since $k$ is infinite, the fixed coordinates can be chosen outside the finitely many vanishing conditions in its rational functions. Properness extends this map to $\mathbf P^1$. Lemma 2.2 identifies the curve with $\mathbf P^1$.

The natural map $\operatorname{PGL}_2\to\operatorname{Aut}(\mathbf P^1)$ is an isomorphism. To verify it over a ring, an automorphism carries the three pairwise fibrewise disjoint sections $0,1,\infty$ to another such triple. Locally, a $2\times2$ change of basis carries $0,\infty$ to the first and third members; diagonal scaling then carries $1$ to the second. The resulting projective matrix glues uniquely. An automorphism fixing $0$ and $\infty$ preserves their Cartier divisors; the ratio of its pullback of the coordinate to that coordinate is a global unit on $\mathbf P^1$, hence a unit of the base ring. Fixing $1$ makes that unit one. This proves uniqueness, including over rings with nilpotents.

The smooth connected image contains a one-dimensional torus, since the action kernel is finite. Conjugate this torus to the diagonal torus of $\operatorname{PGL}_2$. If the image were proper, its dimension would be at most two. Its Lie algebra then contains the diagonal line and at most one of the two distinct torus root lines. Choose the diagonal cocharacter with nonnegative weights on this Lie algebra. The general limit-subgroup lemma in Section 3 gives $P_H(\lambda)=H$ for this image $H$: it is a smooth connected closed subgroup with the same dimension. But $P_H(\lambda)=H\cap P_{\operatorname{PGL}_2}(\lambda)$, and the latter ambient subgroup is triangular. Thus $H$ would be solvable. The finite action kernel has central $k$-points, since conjugation by a connected group on a finite reduced set is constant. Solvability of $H$ would make $G(k)$ solvable as a central extension, and density of $G(k)$ in the smooth group would make $G$ solvable. This contradicts semisimplicity. The image is consequently all of $\operatorname{PGL}_2$.

Let $B_+$ and $B_-$ be the two Borels containing $T$. Their unipotent radicals are one-dimensional, since their images in the point stabilizers of $\operatorname{PGL}_2$ have finite kernel. A smooth connected one-dimensional unipotent group over $k$ is $\mathbf G_a$. The action of $T$ on these radicals has nonzero characters $\alpha_+$ and $\alpha_-$. An element of the normalizer interchanging the Borels induces inversion on $T$, so $\alpha_-=-\alpha_+$.

The Lie algebra of the action kernel lies in both $\mathfrak b_+$ and $\mathfrak b_-$, whose moving lines have the opposite nonzero characters just found. Thus it has no vector in either unipotent root line. Its intersection with either unipotent radical is finite and torus-stable. A finite subgroup of $\mathbf G_a$ stable under all scalar multiplications is defined by $x^{p^a}=0$ in characteristic $p$, or is trivial in characteristic zero: a homogeneous Hopf ideal has this form by the binomial formula. Every nontrivial such subgroup has nonzero tangent space. Our intersections therefore are trivial, so each unipotent radical maps isomorphically to the corresponding unipotent subgroup of $\operatorname{PGL}_2$. If a point of $B_+\cap B_-$ is written $tu_+$, its image lies in the diagonal intersection of the two point stabilizers in $\operatorname{PGL}_2$. Hence the image of $u_+$ is trivial, and $u_+=1$. This works on all test algebras and proves $B_+\cap B_-=T$. The action kernel is consequently contained in $T$. A normal multiplicative-type subgroup of a connected smooth group is central, by rigidity of its character sheaf. The converse inclusion follows because the image has trivial centre. $\square$

For a reductive group of semisimple rank one, quotienting by its radical gives this situation. Its centre is the kernel of the resulting action on the same projective line. The two Borel unipotent radicals are still additive lines with opposite characters.

Now let $\alpha$ be any nonzero weight of a maximal torus of an arbitrary reductive $k$-group. Define the codimension-one torus

$$
T_\alpha=(\ker\alpha)^0_{\mathrm{red}}.
$$

The centralizer $G_\alpha=C_G(T_\alpha)$ is reductive by the preceding lesson. Its weights are precisely the weights of $G$ that are rational multiples of $\alpha$, since these and only these vanish on $T_\alpha$. Its maximal central torus has codimension one in $T$: the nonzero characters on $T/T_\alpha$ span a rank-one lattice. Thus its semisimple rank is one. Proposition 2.3 proves

$$
\Phi\cap\mathbf Q\alpha=\{\alpha,-\alpha\},\qquad
\dim\mathfrak g_\alpha=1.
$$

This proves both the reducedness along each root line and the one-dimensional root-space assertion without appealing to a general root-system classification.

## 3. Subgroups obtained by taking a limit

Over a ring $R$, let $\lambda:\mathbf G_m\to H$ be a cocharacter of a smooth affine group. Define

$$
\begin{aligned}
P_H(\lambda)(A)&=\{h:\lambda(t)h\lambda(t)^{-1}\text{ extends to }t=0\},\\
U_H(\lambda)(A)&=\{h:\text{that extension has value }1\},\\
L_H(\lambda)&=C_H(\lambda(\mathbf G_m)).
\end{aligned}
$$

The extension is a morphism from $\mathbf A^1_A$, not a numerical limit. All definitions commute with base change.

**Lemma 3.1.** These are smooth closed subgroups of finite presentation. The limit map identifies

$$
P_H(\lambda)=L_H(\lambda)\ltimes U_H(\lambda),
$$

and multiplication gives an open immersion

$$
U_H(-\lambda)\times P_H(\lambda)\longrightarrow H.
$$

If $\mathfrak h=\bigoplus\mathfrak h_n$ is the cocharacter-weight decomposition, their Lie algebras are respectively $\bigoplus_{n\ge0}\mathfrak h_n$, $\bigoplus_{n>0}\mathfrak h_n$ and $\mathfrak h_0$. The fibres of $U_H(\lambda)$ are connected unipotent.

**Proof.** Give $R[H]$ its conjugation grading, with $f(t.h)=t^n f(h)$ for a homogeneous function of degree $n$. Existence of the limit is equivalent to vanishing of all negative-degree functions at $h$. They generate an ideal defining $P_H(\lambda)$. Killing all nonzero-degree functions gives $L_H(\lambda)$; additionally setting degree-zero functions equal to their values at $1$ gives $U_H(\lambda)$. Finite presentation follows after descending the finitely presented group and action to a Noetherian ring, where these ideals are finitely generated. The actual equations show that formation commutes with arbitrary base change.

Evaluation at zero is a homomorphism $P\to L$ and is the identity on $L$. The mutually inverse maps $(l,u)\mapsto lu$ and $p\mapsto(\lim t.p,(\lim t.p)^{-1}p)$ prove the semidirect product assertion.

Here is the smoothness check. At the identity, choose homogeneous lifts of a basis of the conormal module into the augmentation ideal; the splitting is possible because torus invariants are exact. Smoothness of $H$ identifies its formal completion there with the power-series algebra in these parameters. The three ideals just described kill exactly the parameters of negative weights, of nonpositive weights, or of nonzero weights, respectively. Their formal completions are power-series algebras in the remaining parameters. The formal smoothness criterion gives smoothness near the identity over the base. The group $L$ is smooth everywhere by the centralizer argument of the first lesson. For $U$, the smooth locus is open and invariant under the acting $\mathbf G_m$. The extended orbit of any geometric point has value the identity at zero; consequently some nonzero parameter carries it into this smooth locus, and invariance puts the original point in the locus too. Thus $U$ is smooth everywhere, and $P=L\ltimes U$ is smooth as well. The same coordinate calculation gives the claimed Lie algebras.

The intersection $U_H(-\lambda)\cap P_H(\lambda)$ is trivial: both positive and negative degrees must vanish, and the limit is the identity. The multiplication map is a monomorphism. Its differential is an isomorphism at the identity; at $(u,p)$, translations reduce it to the decomposition of $\mathfrak h$ by $\mathfrak u_-\oplus\mathfrak p$, followed by $\operatorname{Ad}(p^{-1})$, which induces an automorphism modulo $\mathfrak p$. It is therefore étale everywhere and hence an open immersion.

Every point of $U$ is connected to the identity by its extended orbit map $\mathbf A^1\to U$, so the geometric fibres are connected. Over a field, embed $H\rtimes\mathbf G_m$ faithfully in a general linear group and choose a weight basis for the acting torus. The condition that the limit be the identity makes $U$ strictly triangular relative to that weight ordering. It is therefore unipotent. $\square$

For $\operatorname{SL}_2$ and $\lambda(t)=\operatorname{diag}(t,t^{-1})$, conjugation sends $\begin{pmatrix}a&b\\c&d\end{pmatrix}$ to $\begin{pmatrix}a&t^2b\\t^{-2}c&d\end{pmatrix}$. Thus $P(\lambda)$ is upper triangular, $U(\lambda)$ is upper unipotent, and $L(\lambda)$ is diagonal. This calculation works in characteristic two because the group character $t^2$ remains nontrivial.

## 4. Root groups over the base

Let $T=D_S(M)$ be a split maximal torus. Locally the nonzero weights are a fixed finite set $\Phi\subset M$, and each $\mathfrak g_\alpha$ is a line bundle by Proposition 2.2 on geometric fibres. Define $T_\alpha$ by the torsion-free quotient of $M/\mathbf Z\alpha$. Then

$$
G_\alpha=C_G(T_\alpha),\qquad
\operatorname{Lie}(G_\alpha)=\mathfrak t\oplus\mathfrak g_\alpha\oplus\mathfrak g_{-\alpha}.
$$

Choose a cocharacter $\lambda$ of $T$ with $n=\langle\alpha,\lambda\rangle>0$, and set $U_\alpha=U_{G_\alpha}(\lambda)$. It is a smooth connected one-dimensional unipotent group, with Lie algebra $\mathfrak g_\alpha$.

For a line bundle $L$, write $\mathbf V(L)=\operatorname{Spec}_S\operatorname{Sym}(L^*)$ for its additive group.

**Theorem 4.1.** There is a unique $T$-equivariant homomorphism

$$
\exp_\alpha:\mathbf V(\mathfrak g_\alpha)\longrightarrow G
$$

whose differential is the inclusion of the root line. It is a closed immersion, with image $U_\alpha$, and commutes with every base change. Moreover

$$
U_{-\alpha}\times T\times U_\alpha\longrightarrow G_\alpha
$$

is an open immersion.

**Proof.** On $U_\alpha$, $\mathbf G_m$ acts through $t^n$ on each geometric fibre. Its subgroup $\mu_n$ acts trivially: the fixed subgroup is smooth by exactness of multiplicative-type invariants, and equals $U_\alpha$ on every geometric fibre, so equals it over $S$.

Étale locally choose a section $\sigma$ of $U_\alpha$ disjoint from its identity. The orbit map $t\mapsto t.\sigma$ extends to $q:\mathbf A^1\to U_\alpha$ with $q(0)=1$. Since $\mu_n$ acts trivially on the target, the map factors through the invariant ring $R[x]^{\mu_n}=R[x^n]$ on an affine chart. Its factor $\bar q:\mathbf A^1\to U_\alpha$ is an isomorphism on geometric fibres: there the original map is a nonzero scalar times $t^n$. The smooth fibrewise isomorphism criterion makes $\bar q$ an isomorphism over the base.

The quotient acting torus $\mathbf G_m/\mu_n$ gives ordinary scalar multiplication on the source. The transported group law is a polynomial $m(x,y)$ with

$$
m(tx,ty)=tm(x,y),\quad m(x,0)=x,\quad m(0,y)=y.
$$

Homogeneity forces $m=ax+by$, and the identities force $a=b=1$. Thus $U_\alpha$ is an additive line. Normalize the isomorphism by its differential to obtain $\exp_\alpha$. A scalar-equivariant polynomial map of an additive line is linear; if its differential is the identity it is the identity. This proves uniqueness and allows descent of the local construction.

An equivariant homomorphism with the required differential must factor through $G_\alpha$, since $T_\alpha$ acts trivially on its source, and through $U_{G_\alpha}(\lambda)$, since its orbit limits to the identity. The same uniqueness therefore holds as a map into $G$. The open immersion follows from Lemma 3.1, with $L_{G_\alpha}(\lambda)=T$. $\square$

The notation $\exp_\alpha$ denotes this algebraic map, not the analytic exponential series. No division by factorials occurs. A root-group parameterization $x_\alpha:\mathbf G_a\simeq U_\alpha$ is exactly a trivializing section of the root line.

**Example 4.2.** In $\operatorname{GL}_n$, conjugation by $\operatorname{diag}(t_i)$ sends $E_{ij}$ to $(t_i/t_j)E_{ij}$. Thus

$$
\alpha_{ij}=e_i-e_j,\quad
\mathfrak g_{\alpha_{ij}}=\mathcal O_SE_{ij},\quad
x_{ij}(u)=I+uE_{ij}.
$$

**Example 4.3.** For a line bundle $L$ on $S$, consider $G=\operatorname{SL}(\mathcal O_S\oplus L)$. It has the split torus acting by $(t,t^{-1})$ on the two summands. Its two root lines are $L^{-1}$ and $L$. If $L$ is nontrivial, its root groups are $\mathbf V(L^{-1})$ and $\mathbf V(L)$ and need not be globally isomorphic to $\mathbf G_a$. Having a split maximal torus is thus weaker than having globally parameterized root groups. The distinction disappears over a field.

## 5. A projective quotient and its rank-one form

We need one general algebraic-space tool before constructing this quotient. The following statement and its whole proof are adapted from the Stacks project authors, as read in AI Integrated Stacks Project, [Stacks, Tag 0ABS](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/spaces-morphisms.html#lemma-quasi-finite-separated-quasi-affine). This passage retains the GNU Free Documentation License 1.2.

**Quasi-finite normalization lemma.** Let $S$ be a scheme and let $f:X\to Y$ be a quasi-finite separated morphism of algebraic spaces over $S$. Let $Y'$ be the normalization of $Y$ in $X$. Then the factorization $X\xrightarrow{f'}Y'\xrightarrow{\nu}Y$ has $f'$ a quasi-compact open immersion and $\nu$ integral. In particular $f$ is quasi-affine.

**Proof from Stacks.** The representability theorem for locally quasi-finite separated morphisms of algebraic spaces makes $f$ representable. The finite-type separated normalization theorem then supplies an open subspace $U'\subset Y'$ with $(f')^{-1}(U')=X$ and $X\to U'$ an isomorphism. Thus $f'$ is an open immersion. It is quasi-compact because $f$ is quasi-compact and $\nu$ is separated. For every affine scheme $Z$ mapping to $Y$, the fibre product $Z\times_YX$ is therefore a quasi-compact open subscheme of the affine scheme $Z\times_YY'$. This is exactly the definition of a quasi-affine morphism. $\square$

The two general normalization and representability results used in this imported proof are the preceding results in its source chapter. The theorem on Zariski's Main Theorem in the programme supplies the scheme normalization statement; the imported algebraic-space proof and its source links retain the additional representability step.

The following construction will also be used for flag varieties. It makes explicit why a fibrewise projective quotient is a scheme, even before we have classified the group over the base.

**A flat-source fibre criterion.** A finitely presented closed immersion $Y\hookrightarrow Z$ over $S$, with $Y$ flat over $S$, is an isomorphism if it is so on every geometric fibre. Locally write its ideal as $I\subset C$. Flatness of $C/I$ makes $I\otimes k(s)\to C\otimes k(s)$ injective. Fibre equality makes this module zero. Since $I$ is finitely generated as an ideal, Nakayama at every prime of $C$ gives $I=0$. No flatness assumption on $Z$ is needed.

**Lemma 5.1.** Let $H$ be a smooth closed subgroup with connected fibres of a smooth affine $S$-group $K$ with connected fibres. Suppose $N_K(H)=H$, and suppose every geometric quotient $K_{\bar s}/H_{\bar s}$ is projective. Then the fppf quotient $X=K/H$ is a smooth projective $S$-scheme, locally on $S$. Its universal conjugate subgroup $\mathcal H\subset K_X$ supplies a canonical relatively ample line bundle $\det(\operatorname{Lie}\mathcal H)^*$.

**Proof.** Approximation reduces the construction on affine opens to a Noetherian base: all group laws, subgroup equations and smoothness conditions use finitely many coefficients. The free right $H$-action on $K$ defines a smooth equivalence relation. The bootstrap theorem, the precise internal prerequisite identified below, makes its quotient an algebraic space; $K\to X$ is an $H$-torsor, so $X$ is smooth and formation commutes with base change.

Let $K_n,H_n$ be the $n$th infinitesimal neighbourhoods of the identities. They are finite locally free; their coordinate modules have graded pieces $\operatorname{Sym}^i(\mathfrak k^*)$ and $\operatorname{Sym}^i(\mathfrak h^*)$ for $0\le i\le n$. Normalizing every $H_n$ is equivalent to normalizing $H$. To check this equivalence, formal agreement at the identity gives agreement of the defining ideals by Krull intersection, and connectedness and translations extend that agreement over the group. The descending closed intersections $N_K(H_n)$ therefore stabilize over the Noetherian base. For some $n$, $N_K(H_n)=H$.

Conjugation acts on the Grassmannian of quotients of the locally free coordinate module of $K_n$ of rank equal to that of $H_n$. Its section corresponding to $H_n$ has stabilizer exactly $H$. Thus the orbit map gives a finite-type monomorphism $X\to\operatorname{Gr}$. A finite-type monomorphism is quasi-finite and separated; the normalization lemma just imported makes it quasi-affine. In particular $X$ is a scheme and is quasi-projective locally on the base.

We verify properness. For a local Noetherian base, pass faithfully flatly to its completion $A$. Place $X$ as an open subscheme of a projective closure $\bar X$ over $A$. Its proper special fibre $X_0$ is open and closed in $\bar X_0$, and is therefore cut out by an idempotent. Idempotents lift uniquely across nilpotent ideals. The internal theorem on formal functions gives $\Gamma(\bar X,\mathcal O_{\bar X})\simeq\varprojlim_n\Gamma(\bar X_n,\mathcal O_{\bar X_n})$, since $A$ is complete and $\bar X$ is proper. It therefore turns this compatible formal idempotent into an actual idempotent. It defines an open and closed proper component $Z\subset\bar X$ with $Z_0=X_0$. The closed subset $Z\setminus X$ has empty special fibre; properness makes it empty. Hence $Z\subset X$.

The image of $Z\to\operatorname{Spec}A$ is both open and closed: it is proper, and it is the restriction of the smooth map $X\to S$. It contains the closed point, so is all of the local base. In each geometric fibre, $Z$ is a nonempty open and closed part of the connected fibre of $X$. It is the entire fibre. Thus $Z=X$, proving properness. This descends from the completion and from local bases.

The Grassmannian map is now a proper monomorphism and hence a closed immersion. Its Plücker bundle pulls back to $\det\mathcal O_{\mathcal H_n}$. The augmentation filtration identifies this determinant with

$$
\bigotimes_{i=0}^n\det(\operatorname{Sym}^i(\operatorname{Lie}\mathcal H)^*)
=\bigl(\det(\operatorname{Lie}\mathcal H)^*\bigr)^c
$$

for a positive integer $c$ when $\dim H>0$. Positivity follows already from the $i=1$ term; the determinant exponent for $\operatorname{Sym}^i$ on a rank-$d$ bundle is $\binom{i+d-1}{d}$. Thus the stated canonical bundle is relatively ample. The zero-dimensional connected smooth case is trivial. All the constructions descend to the original arbitrary base and commute with base change. $\square$

The bootstrap theorem and formal-functions theorem are exact internal dependencies, with their published or planned state recorded in the prerequisite guide. The algebraic-space normalization lemma has its complete open-licensed proof in this section. The group-specific argument is original exposition.

**Proposition 5.2.** If $G$ has trivial centre and geometric semisimple rank one, and has a split maximal torus $T$, then Zariski locally $(G,T)$ is isomorphic to $(\operatorname{PGL}_2,D)$.

**Proof.** Its geometric fibres are $\operatorname{PGL}_2$ by Proposition 2.3: the action on the projective line has trivial kernel. Choose a root $\alpha$ locally. It is an isomorphism $T\to\mathbf G_m$, as this is true on the character lattices of the geometric fibres. Put $B=P_G(\alpha^{-1})$. It is smooth and on each geometric fibre is an upper triangular Borel subgroup of $\operatorname{PGL}_2$.

Its scheme-theoretic normalizer equals $B$. The normalizer is closed of finite presentation: normalizing all identity jets is a family of closed conditions on finite locally free coordinate modules; over a Noetherian model their ideals stabilize, and their universal base-change interpretation descends the finite equations. Formal equality detects equality of these connected smooth subgroup schemes, as in Lemma 5.1. On geometric fibres the point stabilizer in $\mathbf P^1$ is self-normalizing. Infinitesimally, the bracket of a diagonal matrix class with the lower off-diagonal class is a nonzero lower off-diagonal class in every characteristic, so the normalizer has exactly the tangent space of $B$. It is therefore smooth and equals $B$ on those fibres. The flat-source criterion above, applied with source $B$, proves the equality over the base without assuming the normalizer flat.

Lemma 5.1 makes $G/B$ a smooth projective genus-zero curve with the section $1B$. The line bundle of this section has degree one on each fibre; its direct image is locally free of rank two and its evaluation map gives $G/B\simeq\mathbf P(E)$, where $E$ is that rank-two bundle. This is the elementary cohomology-and-base-change step: $H^1(\mathbf P^1,\mathcal O(1))=0$ and $H^0$ has dimension two; Nakayama's lemma on the evaluation cokernel and the finite free cohomology complex give the assertion. Locally trivializing $E$ gives $G/B\simeq\mathbf P^1_S$.

The action now gives $G\to\operatorname{PGL}_2$, an isomorphism on every geometric fibre, hence an isomorphism over $S$. It carries $B$ to the point stabilizer. Within that stabilizer the transporter taking its torus $T$ to the diagonal torus is a $\mathbf G_m$-torsor: the stabilizer of the diagonal torus inside the upper triangular group is the diagonal torus. Such a torsor is the frame bundle of a line bundle and is Zariski locally trivial. This finishes the pairwise assertion. $\square$

## 6. Splitting a central extension of the rank-one cover

We need an integral result, including characteristic two. The following splitting argument is due to Gabber; we give the argument for a separated commutative group scheme $Z$, which includes the multiplicative-type centres used here.

**Theorem 6.1.** Every fppf central extension

$$
1\longrightarrow Z\longrightarrow E\longrightarrow\operatorname{SL}_{2,S}\longrightarrow1
$$

has a unique homomorphic section.

**Proof.** In $\operatorname{SL}_2$ use

$$
x(u)=\begin{pmatrix}1&u\\0&1\end{pmatrix},\quad
y(v)=\begin{pmatrix}1&0\\v&1\end{pmatrix},\quad
h(t)=\operatorname{diag}(t,t^{-1}).
$$

Let $D',U',V'$ be their inverse images in $E$. A central extension of a commutative group has a commutator pairing on its quotient: changing a lift by an element of the central kernel does not change the commutator, and the identities for commutators make this pairing additive in each variable.

For $D'$, the pairing $\mathbf G_m\times\mathbf G_m\to Z$ is trivial. Restrict the first argument to $\mu_n$. The resulting pairing is killed by $n$ in that argument, and the $n$th-power map is an fppf epimorphism in the second argument, so this restriction is trivial. The schemes $\mu_n$ are universally schematically dense in $\mathbf G_m$: distinct Laurent exponents remain distinct modulo sufficiently large $n$. Separatedness of $Z$ makes the whole pairing trivial. Thus $D'$ is commutative.

The conjugation action on $E$ factors through $\operatorname{SL}_2$, since $Z$ is central. The commutator pairing on $U'$ is invariant under simultaneous multiplication of its arguments by $t^2$. The square map is fppf surjective, so it is invariant under simultaneous multiplication by every unit. For given $u,v$, the morphism $a\mapsto c(au,av)$ from $\mathbf A^1$ to $Z$ is constant on $\mathbf G_m$. Separatedness extends the equality to zero, where it is the identity. Hence $c(u,v)=1$. Thus $U'$ is commutative; the same argument proves it for $V'$.

We construct a unique $D$-equivariant section of $U'\to U$. Fppf locally choose a unit $t$ with $t^2-1$ invertible and a lift $\tilde h$ of $h(t)$. Such choices exist: the open locus $t(t^2-1)\ne0$ in an affine line is smooth surjective, and the extension is an fppf epimorphism. In the commutative group $U'$, the endomorphism

$$
\varphi(a)=\tilde h a\tilde h^{-1}a^{-1}
$$

kills $Z$ and induces multiplication by $t^2-1$ on $U=\mathbf G_a$. It therefore factors through a homomorphism $U\to U'$, which after division by $t^2-1$ is the required section. It is $D$-equivariant because $D'$ is commutative. Uniqueness holds since any difference is a $D$-invariant homomorphism $U\to Z$: scalar invariance and the specialization from nonzero scalars to zero force it to vanish. Uniqueness descends these local sections. Obtain $x':\mathbf G_a\to E$ and similarly $y'$.

Set

$$
w'(t)=y'(-t^{-1})x'(t)y'(-t^{-1}),\qquad
h'(t)=w'(t)w'(1)^{-1}.
$$

Their images are $\begin{pmatrix}0&t\\-t^{-1}&0\end{pmatrix}$ and $h(t)$. Thus $h'(t)\in D'$. Equivariance gives

$$
h'(s)w'(t)h'(s)^{-1}=w'(s^2t).
$$

Divide by the instance $t=1$. Since $D'$ is commutative, this gives $h'(t)=h'(s^2t)h'(s^2)^{-1}$. The square map being fppf surjective, $h'$ is a homomorphism. Its definition then gives $h'(s)w'(t)=w'(st)$.

Substitute the expression for $w'$ into this last equality and move the $y'$ terms using $h'(s)y'(v)h'(s)^{-1}=y'(s^{-2}v)$. With $u=st$ and $v=(s-1)/(st)$, the result is

$$
x'(u)y'(v)=y'\left(\frac{v}{1+uv}\right)
h'(1+uv)x'\left(\frac{u}{1+uv}\right)
\tag{1}
$$

when $u$ and $1+uv$ are units. The restriction that $u$ be a unit can be removed. Fppf locally write $u=a+b$ with $a,b,1+bv$ units; the open conditions on a choice of $b$ omit only finitely many points of each geometric affine-line fibre. Apply (1) first to $x'(b)y'(v)$, then to $x'(a)y'(v/(1+bv))$. The second denominator is $(1+uv)/(1+bv)$. Moving the two resulting $h'$ factors together leaves the $y'$ parameter $v/(1+uv)$ and the $x'$ parameter

$$
\frac{a}{(1+bv)(1+uv)}+\frac{b}{1+bv}
=\frac{u}{1+uv}.
$$

This proves (1) in its full domain.

These identities, the additivity of $x',y'$, the multiplicativity of $h'$, and its two conjugation identities are exactly the multiplication rules on the open cell $\Omega=U_-DU_+$ of $\operatorname{SL}_2$. Define a section there by

$$
y(v)h(t)x(u)\longmapsto y'(v)h'(t)x'(u).
$$

It is multiplicative whenever both factors and their product are in $\Omega$: reorder their factors with (1). To extend it to the whole group, any finite collection of partial products can fppf locally be translated into $\Omega$ by one point $\omega\in\Omega$. Indeed, the intersection of these finitely many translates of $\Omega$ is fibrewise nonempty, since each geometric fibre of the connected smooth group is irreducible. This intersection is smooth surjective over the base and hence an fppf cover.

If two words in points of $\Omega$ give the same point of $\operatorname{SL}_2$, choose such an $\omega$ for all partial products of both words. Repeated cell multiplicativity identifies each lifted word, after multiplying on the left by the lift of $\omega$, with the lift of the same translated endpoint. Cancellation shows that the two lifts agree. Points of $\Omega$ generate the group fppf locally by the same translation argument. Thus the cell section extends to a homomorphic section on all of $\operatorname{SL}_2$.

Finally any homomorphism $\operatorname{SL}_2\to Z$ kills $x(u)$, since

$$
[h(t),x(u)]=x((t^2-1)u),
$$

and one may choose $t^2-1$ invertible fppf locally. It kills $y(v)$ similarly, and then $h(t)=w(t)w(1)^{-1}$. It kills the open cell, hence the group. The difference between two central sections is such a homomorphism, proving uniqueness. $\square$

## 7. Coroots from multiplication

**Theorem 7.1.** For every root $\alpha$ there is a canonical coroot $\alpha^\vee:\mathbf G_m\to T$, with $\langle\alpha,\alpha^\vee\rangle=2$. There is a canonical perfect pairing $\mathfrak g_\alpha\otimes\mathfrak g_{-\alpha}\to\mathcal O_S$ such that, writing its value as $XY$,

$$
\exp_\alpha(X)\exp_{-\alpha}(Y)
=\exp_{-\alpha}\left(\frac{Y}{1+XY}\right)
\alpha^\vee(1+XY)
\exp_\alpha\left(\frac{X}{1+XY}\right)
\tag{2}
$$

whenever $1+XY$ is a unit. This unit condition is precisely membership in the open cell $U_{-\alpha}TU_\alpha$.

**Proof.** Work in $G_\alpha$, whose centre is $Z=\ker\alpha$. The central quotient $G_\alpha/Z$ is reductive with trivial centre, and its torus is $T/Z$. The quotient construction for central multiplicative-type groups is given in the next lesson; it uses only the centre calculation and affine invariant rings, not coroots. Proposition 5.2 identifies this quotient, Zariski locally, with $\operatorname{PGL}_2$ and $T/Z$ with its diagonal torus. Choose the identification so $\alpha(\operatorname{diag}(t,1))=t$.

Pull back $G_\alpha\to\operatorname{PGL}_2$ by $\operatorname{SL}_2\to\operatorname{PGL}_2$. Theorem 6.1 splits the resulting central extension by $Z$. The homomorphism $\operatorname{SL}_2\to G_\alpha$ obtained from the splitting identifies its upper and lower unipotent groups with $U_\alpha,U_{-\alpha}$: the maps are equivariant, and their differentials on the root lines are isomorphisms, so Theorem 4.1 gives the assertion. The diagonal cocharacter therefore defines $\alpha^\vee$.

Direct multiplication gives

$$
\begin{pmatrix}1&x\\0&1\end{pmatrix}
\begin{pmatrix}1&0\\y&1\end{pmatrix}
=
\begin{pmatrix}1&0\\y/(1+xy)&1\end{pmatrix}
\begin{pmatrix}1+xy&0\\0&(1+xy)^{-1}\end{pmatrix}
\begin{pmatrix}1&x/(1+xy)\\0&1\end{pmatrix}.
$$

The upper-left entry is a unit exactly when the product is in this open cell. It supplies (2), a perfect pairing of the two root lines, and $\alpha\circ\alpha^\vee(t)=t^2$.

The pairing and coroot are unique. In the adjoint quotient, comparing the upper-root parameter in (2) forces any alternative scalar in the pairing to be one; equality of open-cell coordinates then fixes the coroot on every unit $1+xy$, which ranges over all units by setting $y=1$. An alternative coroot in $T$ with the same adjoint image could differ by a cocharacter into $Z$, but (2) fixes its actual torus component and eliminates that difference. Hence the constructions on different local identifications agree and descend. The same characterization proves base-change compatibility. $\square$

For $\operatorname{SL}_2$, use $T\simeq\mathbf G_m$ via $\operatorname{diag}(t,t^{-1})$. Its root is $\alpha(t)=t^2$, and $\alpha^\vee(t)=\operatorname{diag}(t,t^{-1})$. For $\operatorname{PGL}_2$, parameterize its diagonal torus by the class of $\operatorname{diag}(t,1)$. Its root is $t\mapsto t$, and its coroot is the class of $\operatorname{diag}(t^2,1)$. In both cases the pairing is two, but the root and coroot occupy different sublattices.

For $\operatorname{GL}_2$, the roots are $e_1-e_2$ and its negative, and the positive coroot is $t\mapsto\operatorname{diag}(t,t^{-1})$. These explicit formulas remain valid over $\mathbb Z$.

## 8. The three rank-one groups

**Theorem 8.1.** A split reductive group over a field, of rank $r+1$ and semisimple rank one, is isomorphic to exactly one of

$$
\mathbf G_m^r\times\operatorname{SL}_2,\qquad
\mathbf G_m^r\times\operatorname{PGL}_2,\qquad
\mathbf G_m^{r-1}\times\operatorname{GL}_2\quad(r\ge1).
$$

For a reductive group over a scheme with split maximal torus and semisimple rank one, this list holds Zariski locally on loci with fixed type. Global identifications require trivializations of the root lines; a globally pinned group of constant type is the corresponding base change from $\mathbb Z$.

**Proof.** The adjoint quotient is $\operatorname{PGL}_2$, over a field globally and over a scheme locally by Proposition 5.2. Its central extension by $Z(G)=D(A)$ pulls back to a split extension of $\operatorname{SL}_2$ by Theorem 6.1. Consequently

$$
G\simeq(\operatorname{SL}_2\times D(A))/\mu_2,
$$

where the kernel is the graph of a homomorphism $\mu_2\to D(A)$, with inverse in the second coordinate. On characters this is a map $f:A\to\mathbb Z/2$. The centre has rank $r$, and $\ker f$ is torsion-free: it is the character lattice of the torus quotient of the centre by the image of $\mu_2$, equivalently the central torus in the adjoint fibre description.

There are exactly three elementary possibilities. If $A$ has torsion, its torsion injects into $\mathbb Z/2$ and is therefore $\mathbb Z/2$. Split it off by the structure theorem for finitely generated abelian groups. Subtract its generator from each free generator on which $f$ is nonzero. Then $A\simeq\mathbb Z^r\oplus\mathbb Z/2$ with $f$ projection on the last summand. The quotient above cancels this $\mu_2$ factor and is $\mathbf G_m^r\times\operatorname{SL}_2$.

If $A$ is torsion-free and $f=0$, the quotient is $\mathbf G_m^r\times\operatorname{PGL}_2$. If $A$ is torsion-free and $f\ne0$, a primitive integral change of basis makes $f$ reduction modulo two on one basis coordinate and zero on the others. For example, make one odd coordinate the first and eliminate the other odd coordinates by subtracting it; the Euclidean algorithm provides a unimodular basis. The quotient is then $\mathbf G_m^{r-1}\times(\operatorname{SL}_2\times\mathbf G_m)/\mu_2$, and the final factor is $\operatorname{GL}_2$ via $(g,t)\mapsto tg$. This is a surjective homomorphism of fppf sheaves, with kernel $\{(a^{-1}I,a):a^2=1\}$.

These groups are distinct. The first has centre $\mathbf G_m^r\times\mu_2$, a non-torus multiplicative-type group. The other two have torus centre. Their derived groups are respectively $\operatorname{PGL}_2$ and $\operatorname{SL}_2$, distinguished by their centres. This also proves uniqueness in every characteristic. Over a scheme the character sheaf is locally constant and the root lines can be trivialized Zariski locally, giving the local assertion; the pinned global statement follows in the isomorphism lesson. $\square$

The kernel condition in this proof can be checked directly on the maximal torus: the character group of $(D_2\times D(A))/\mu_2$ is $\{(m,a)\in\mathbb Z\oplus A:m\equiv f(a)\pmod2\}$. It is free precisely when $\ker f$ is free. This also avoids confusing the centre, which may be non-smooth, with its radical.

## 9. Exercises and solutions

**Exercise 9.1 (first steps).** Compute all roots and root spaces of $\operatorname{GL}_n$ with respect to its diagonal torus. Determine the zero-weight space and the positive coroot for $e_i-e_j$.

**Solution.** The diagonal matrix units have weight zero and form $\mathfrak t$. For $i\ne j$, $E_{ij}$ has weight $e_i-e_j$, each once. The corresponding root group is $I+uE_{ij}$. Its coroot has diagonal entries $t$ in position $i$, $t^{-1}$ in position $j$, and $1$ elsewhere. Evaluating $e_i-e_j$ gives $t^2$, so the root–coroot pairing is two.

**Exercise 9.2 (rank-one multiplication).** Compute $U_{\pm\alpha}$ and $\alpha^\vee$ for $\operatorname{SL}_2$. Verify the factorization (2), and explain why the character differential in characteristic two does not change this factorization.

**Solution.** The two groups are the upper and lower unipotent matrices. Their parameters are $x,y$ in the displayed matrix identity, and $\alpha^\vee(t)=\operatorname{diag}(t,t^{-1})$. Multiplication of the three factors gives $\begin{pmatrix}1+xy&x\\y&1\end{pmatrix}$, equal to $x_\alpha(x)x_{-\alpha}(y)$. The character on the upper group is $t^2$, so its pairing with this coroot is two. Although its differential is zero in characteristic two, the Laurent character and all polynomial matrix identities remain valid; no division by two was used.

**Exercise 9.3 (infinitesimal information).** In characteristic different from two, show that $\mathfrak{sl}_2\simeq\mathfrak{pgl}_2$ as Lie algebras, while the groups are not isomorphic. What happens to the differential of $\operatorname{SL}_2\to\operatorname{PGL}_2$ in characteristic two?

**Solution.** The inclusion of trace-zero matrices followed by quotienting by scalar matrices has zero kernel when two is invertible: a trace-zero scalar is zero. Both Lie algebras have dimension three, so this bracket-preserving map is an isomorphism. The groups have different centres, $\mu_2$ and $1$. In characteristic two the scalar identity has trace zero and lies in the kernel of the differential, which therefore has one-dimensional kernel. It cannot be an isomorphism. The group map remains a central fppf isogeny with kernel $\mu_2$.

**Exercise 9.4 (classification).** List the rank-two split reductive groups of semisimple rank one. Distinguish them by their centres and derived groups, including characteristic two.

**Solution.** Put $r=1$ in Theorem 8.1. The list is $\mathbf G_m\times\operatorname{SL}_2$, $\mathbf G_m\times\operatorname{PGL}_2$, and $\operatorname{GL}_2$. Their centres are respectively $\mathbf G_m\times\mu_2$, $\mathbf G_m$, and $\mathbf G_m$. The first centre is not a torus: in characteristic two it is non-smooth, and otherwise it has two geometric components. The last two are distinguished by derived groups $\operatorname{PGL}_2$ and $\operatorname{SL}_2$. The first and third both have derived group $\operatorname{SL}_2$, but their centres differ. All distinctions are scheme-theoretic and persist in characteristic two.

**Exercise 9.5 (families).** For $G=\operatorname{SL}(\mathcal O\oplus L)$, identify the two root groups and their pairing. Give a condition on $L$ necessary for a pinning of this pair with its displayed torus.

**Solution.** An upper off-diagonal entry is a map $L\to\mathcal O$, so its line is $L^{-1}$; a lower entry is a map $\mathcal O\to L$, so its line is $L$. Composition gives $L^{-1}\otimes L\to\mathcal O$, the perfect pairing in Theorem 7.1. A pinning chooses a nowhere-vanishing section in the simple root line. It therefore requires $L^{-1}$, equivalently $L$, to be trivial. This illustrates the global hypothesis absent from the field case.

The [course prerequisite guide](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-RG/prerequisites.html) records the exact supporting statements and which lessons are published or still planned.

## References and prerequisite proofs

- Brian Conrad, [*Reductive group schemes*](https://math.stanford.edu/~conrad/papers/luminysga3.pdf), §§2.3 and 4.1–4.3, for the dynamic approach and Gabber's central-extension splitting argument. The proofs above are written out independently.
- J. S. Milne, *Algebraic Groups: The Theory of Group Schemes of Finite Type over a Field*, 2017, Chapters 19–20, especially Theorem 20.33, for the field rank-one classification.
- SGA 3, [*Schémas en groupes*](https://webusers.imj-prg.fr/~patrick.polo/SGA3/), Exposés XIX–XX, for roots and the relative rank-one theorem.
- The [official Stacks project](https://stacks.math.columbia.edu/) and AI Integrated Stacks Project, an edition with AI-proposed corrections and AI-written additions, not reviewed by the Stacks project's maintainers. The normalization lemma and its whole proof in Section 5 are adapted from the Stacks project authors through this edition.

The following are assigned internal prerequisite lessons. Their published or planned state is recorded in the course prerequisite guide; their use does not claim that the entire programme is proof-complete:

- The bootstrap theorem, in *Algebraic spaces and stacks*: a free action by a flat locally finitely presented group algebraic space has an algebraic-space fppf quotient, and the map to that quotient is an fppf torsor. We apply it to the smooth subgroup $H$ acting on $K$.
- *The theorem on formal functions*, in *Coherent cohomology*: for $A$ Noetherian, $X$ proper over $A$, and $F$ coherent, $H^i(X,F)^\wedge\simeq\varprojlim H^i(X,F/I^nF)$. The degree-zero case over a complete local ring is used in Section 5.
- *Dualizing sheaves and Serre duality for projective schemes*, in *Coherent cohomology*: the full duality theorem for projective Cohen–Macaulay schemes, used for the smooth curve calculation in Lemma 2.2.
- *Semicontinuity and Grauert’s theorem*, in *Coherent cohomology*: a proper flat finite-presentation family with higher cohomology zero has locally free direct image commuting with base change. This is used for the degree-one bundle on the genus-zero family, including nonreduced bases.
- *Flatness criteria, dimension and the flat locus*, *Étale morphisms and their local structure*, and *Smooth morphisms and their local structure*, in *Flat, smooth and étale morphisms*: the fibre criteria used to pass from geometric isomorphisms to relative ones.

Central multiplicative-type quotients are proved by invariant algebras in Section 7 of the next lesson, without using the coroot conclusion of this lesson. The arbitrary-base derived group is constructed after the existence theorem in the following lesson.

## History

This lesson's new exposition, constructions, calculations, examples and solutions were written by GPT-6.1 Sol (OpenAI), Ultra setting, in October 2026, and are dedicated to the public domain under CC0.

The normalization lemma and its whole proof are adapted from the Stacks authors, *The Stacks Project*, *Morphisms of Algebraic Spaces*, Tag 0ABS, through the AI Integrated Stacks Project English source edition read on 1 October 2026. The Stacks authors retain copyright in that material. The source is the [versioned transparent source](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/spaces-morphisms.tex). AI Integrated Stacks Project contains AI-proposed corrections and AI-written additions and has not been reviewed by the Stacks project's maintainers.

This collected lesson, *Roots and reductive groups of rank one* (2026), is published by Open Mathematics Courses. The Stacks authors are the authors of its imported proof; GPT-6.1 Sol (OpenAI) is responsible for the new contributions and adaptation. Permission is granted to copy, distribute and modify this collected lesson under the GNU Free Documentation License, Version 1.2, with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts. An unaltered copy of the licence is supplied as [GNU Free Documentation License 1.2](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-RG/assets/GFDL-1.2.txt). This additional licence for the collected lesson does not withdraw the CC0 dedication of its original contributions.
