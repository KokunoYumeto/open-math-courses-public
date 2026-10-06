# Transitivity and primitivity

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI, GPT-6.1 Sol (OpenAI), in Codex at Ultra. Public domain (CC0).*

The same Lie algebra can act on spaces of different dimensions. The missing information is the stabilizer of a point. For a transitive action, a Lie algebra together with that stabilizer determines the entire local geometry. Subalgebras between the stabilizer and the whole algebra describe every invariant foliation. This turns the question of primitivity into a question about maximal subalgebras.

We work with analytic local right actions $p\cdot a$, using $T_bT_a=T_{ab}$, and the infinitesimal homomorphism $u\mapsto X_u$. We use the Frobenius theorem of Complete systems and invariants and the local groups and subgroup germs constructed in The adjoint group, composition and isomorphism. The manifold has positive dimension. Connectedness and effectiveness below are local conditions. The Euclidean and spherical examples are real; complexification can change primitivity.

## 1. Orbits and isotropy

For a point $p$, define the evaluation map, orbit distribution, and isotropy algebra by

$$
\operatorname{ev}_p:\mathfrak g\to T_pM,\quad u\mapsto X_u(p),
\qquad D_p=\operatorname{im}\operatorname{ev}_p,
\qquad \mathfrak h_p=\ker\operatorname{ev}_p.
\tag{1.1}
$$

If two vector fields vanish at $p$, their bracket also vanishes there, as its coefficients are $DX_v\,X_u-DX_u\,X_v$. Thus $\mathfrak h_p$ is a subalgebra. It need not be an ideal.

The action law gives, for $q=p\cdot a$,

$$
X_u(q)=(dT_a)_p X_{\operatorname{Ad}_a u}(p),\qquad
\mathfrak h_q=\operatorname{Ad}_{a^{-1}}\mathfrak h_p.
\tag{1.2}
$$

To verify the first formula, write $a\exp(tu)=\exp(t\operatorname{Ad}_a u)a$ and differentiate the orbit of $p$. In particular, rank and isotropy dimension are constant along an orbit.

**Theorem 1.1 (orbit dimension and transitivity).** The local orbit through $p$ has dimension $\dim D_p$. The action is transitive near $p$ if and only if $D_p=T_pM$.

**Proof.** Consider $\theta_p(a)=p\cdot a$. At $e$, its differential is (1.1). At $a$, differentiate $\theta_p(\exp(tu)a)=T_a(\theta_p(\exp(tu)))$. Right translation supplies all parameter tangent directions, so $d\theta_p$ has the same rank at every nearby $a$ as it has at $e$. The constant-rank theorem makes its local image an immersed submanifold of that dimension. This is the local orbit; its tangent spaces are $D$ by (1.2). If the rank equals $\dim M$, the submersion theorem makes that image a neighbourhood of $p$. Conversely a local orbit of smaller dimension cannot contain a neighbourhood in the constant-rank chart. $\square$

At a generic point, the rank equals its maximal value: in an analytic coordinate chart, the exceptional locus is given by vanishing of the relevant maximal minors. Formula (1.2) makes each rank stratum invariant. “Transitive at generic points” describes open local orbits on the maximal-rank region; it does not imply transitivity through a singular point or on the entire global manifold. For example, dilation on the line is locally transitive at every nonzero point and fixes zero.

## 2. Constructing a quotient by a subalgebra

Let $G$ be the local group with Lie algebra $\mathfrak g$, and let $\mathfrak h\subset\mathfrak g$ be any subalgebra. Its subgroup germ $H$ exists by lesson 7. No normality assumption is made.

On $G$, use the right-invariant distribution

$$
V_{\mathfrak h}(a)=(dR_a)_e\mathfrak h.
\tag{2.1}
$$

Right-invariant fields have brackets with the opposite sign, so this distribution is involutive. Its leaf through $a$ is the germ of the left coset $Ha$. Frobenius supplies a local leaf space of dimension $\dim\mathfrak g-\dim\mathfrak h$ and a submersion

$$
\pi_H:G\longrightarrow H\backslash G.
\tag{2.2}
$$

This notation means a local quotient chart, rather than a claim that $H$ is a globally closed subgroup. Right translations preserve (2.1), so they descend to an analytic right action

$$
(Ha)\cdot b=H(ab).
\tag{2.3}
$$

Choose a transverse section through $e$. Each nearby group element is uniquely written as $h s(x)$ with $h\in H$ and $s(x)$ on this section: the product map has invertible differential on a splitting $\mathfrak g=\mathfrak h\oplus\mathfrak m$. This gives explicit coordinates for (2.2) and (2.3), after shrinking so that all products remain in the chart.

The isotropy algebra at $H$ is exactly $\mathfrak h$, because $\ker(d\pi_H)_e=\mathfrak h$. The action is transitive by Theorem 1.1. Its infinitesimal fields are the projections of the left-invariant fields of $G$, whose right-translation flows descend; consequently $[X_u,X_v]=X_{[u,v]}$.

**Lemma 2.1 (effectiveness).** The kernel of this infinitesimal action is the largest ideal of $\mathfrak g$ contained in $\mathfrak h$.

**Proof.** The kernel $I$ of $u\mapsto X_u$ is an ideal, since this map preserves brackets. Every field in the kernel vanishes at $H$, so $I\subset\mathfrak h$. Conversely let $J\subset\mathfrak h$ be an ideal. Its subgroup germ $N$ is normal and contained in $H$. For $u\in J$ and a nearby $a$,

$$
Ha\exp(tu)=H(a\exp(tu)a^{-1})a=Ha,
$$

because $a\exp(tu)a^{-1}\in N\subset H$. Thus $X_u$ vanishes everywhere. Every such ideal lies in the kernel, proving the assertion. $\square$

An action is effective here when that kernel is zero. This is an infinitesimal condition; a global discrete kernel is separate.

## 3. Reconstructing every transitive action

**Theorem 3.1 (reconstruction and similarity).** A based effective transitive local action is determined by a pair $(\mathfrak g,\mathfrak h)$, where $\mathfrak h$ is a subalgebra of codimension $n$ containing no nonzero ideal of $\mathfrak g$. Conversely every such pair gives an effective transitive action on an $n$-dimensional local manifold. Two pairs determine similar based actions exactly when an algebra isomorphism carries one isotropy algebra to the other. For a fixed identified algebra, the isomorphism is an automorphism of $\mathfrak g$.

**Proof.** The construction in Section 2 proves existence and effectiveness. Start conversely with a transitive action at $p$. Its orbit map $\theta_p:G\to M$ is a submersion. The fibre through $e$ is the stabilizer germ $H=\{a:p\cdot a=p\}$; products and inverses preserve this equation, so $H$ is a subgroup with tangent algebra $\mathfrak h_p$.

Its other fibres are left cosets. Indeed, $p\cdot a=p\cdot b$ is equivalent, after applying $T_{b^{-1}}$, to $p\cdot(ab^{-1})=p$, hence to $a\in Hb$. Therefore the orbit map factors through a local diffeomorphism

$$
\overline\theta_p:H\backslash G\longrightarrow M.
\tag{3.1}
$$

The differential is an isomorphism because the orbit map and quotient map have the same kernel and rank. The action law makes (3.1) equivariant. Lemma 2.1 shows that effectiveness is exactly the condition that $\mathfrak h_p$ contain no nonzero ideal.

Suppose $f:\mathfrak g\to\mathfrak g'$ is an isomorphism with $f(\mathfrak h)=\mathfrak h'$. Lesson 7 integrates it to a local group isomorphism $F:G\to G'$. Uniqueness of subgroup germs gives $F(H)=H'$. Consequently

$$
Ha\longmapsto H'F(a)
\tag{3.2}
$$

is well defined, is a local diffeomorphism, and intertwines the right actions with parameter change $F$. Composing with (3.1) gives similarity.

Conversely, a similarity carries the vector space of infinitesimal fields onto that of the other action. Effectiveness identifies these spaces with the respective algebras. Pushforward is linear and bracket preserving, so it induces an algebra isomorphism. Fields vanishing at the base point go to fields vanishing at its image; thus it carries $\mathfrak h$ to $\mathfrak h'$. $\square$

If one changes the base point along an orbit, (1.2) conjugates the isotropy by an inner automorphism. This is why an unbased classification must allow movement of the base point as well as the displayed algebra identification.

## 4. All invariant foliations

An invariant foliation is a regular local foliation whose leaves are carried to leaves by each nearby transformation. A transformation need not fix each leaf separately. Equivalently, its tangent distribution is preserved by the action.

**Theorem 4.1 (foliation correspondence).** For a transitive action represented by $H\backslash G$, invariant foliations correspond bijectively to subalgebras

$$
\mathfrak h\subset\mathfrak k\subset\mathfrak g.
\tag{4.1}
$$

The leaf dimension is $\dim\mathfrak k-\dim\mathfrak h$. The extreme subalgebras give the point foliation and the single full-dimensional leaf.

**Proof.** Given $\mathfrak k$, let $K$ be its subgroup germ. Since $H\subset K$, there is a local submersion

$$
H\backslash G\longrightarrow K\backslash G,\qquad Ha\longmapsto Ka.
\tag{4.2}
$$

Its fibres are a regular foliation. The map is equivariant for right translation, so the foliation is invariant. The rank theorem gives the stated fibre dimension.

Conversely let $D$ be an invariant involutive distribution on $H\backslash G$. Lift it by the submersion to

$$
\widetilde D_a=(d\pi_H)_a^{-1}(D_{Ha})\subset T_aG.
$$

It contains the vertical distribution (2.1). A submersion chart shows that $\widetilde D$ is involutive: it is the sum of vertical coordinate directions and lifts of the foliation directions. Equivariance of $\pi_H$ and invariance of $D$ make $\widetilde D$ right-invariant. It is therefore determined by its value $\mathfrak k=\widetilde D_e$, which contains $\mathfrak h$. Involutivity and the right-invariant bracket formula imply $[\mathfrak k,\mathfrak k]\subset\mathfrak k$.

The lifted distribution is exactly $(dR_a)_e\mathfrak k$, so its leaves are the left cosets of $K$. Its projection is precisely the fibre foliation (4.2). This also proves uniqueness and the bijection. $\square$

The action is **imprimitive** if there is such a foliation with leaf dimension strictly between zero and $n$; otherwise it is **primitive**.

**Corollary 4.2 (Lie's primitivity criterion).** A transitive local action is primitive if and only if its isotropy algebra is a maximal proper subalgebra of $\mathfrak g$.

**Proof.** A nontrivial foliation corresponds by Theorem 4.1 to $\mathfrak h\subsetneq\mathfrak k\subsetneq\mathfrak g$. Its absence is exactly maximality. $\square$

This is a local assertion about connected subgroup germs. Disconnected subgroups and global leaf topology do not enter the proof.

## 5. Four geometries

**The projective line.** In an affine chart, its infinitesimal fields are

$$
\partial_x,\qquad x\partial_x,\qquad x^2\partial_x.
$$

They are independent as fields and span the tangent line at every finite point. At $x=0$, the isotropy is $\operatorname{span}(x\partial_x,x^2\partial_x)$. It has codimension one and is therefore maximal. The projective action is primitive. Indeed every transitive action on a one-dimensional manifold is locally primitive, because there is no permitted intermediate leaf dimension.

**The punctured real plane.** Let $\operatorname{SL}_2(\mathbb R)$ act linearly on $\mathbb R^2\setminus\{0\}$. If desired, replace $g\cdot v$ by the right action $v\cdot g=g^{-1}v$ to match our conventions; the transformation family and its invariant foliations are the same. For

$$
A=\begin{pmatrix}a&b\\c&-a\end{pmatrix},\qquad p=\binom10,
$$

the evaluation $Ap=(a,c)^t$ is surjective. The isotropy is $\mathfrak h=\mathbb R E$, where

$$
E=\begin{pmatrix}0&1\\0&0\end{pmatrix}.
$$

It lies in the proper two-dimensional subalgebra $\mathfrak k=\operatorname{span}(H,E)$ with $H=\operatorname{diag}(1,-1)$ and $[H,E]=2E$. Thus the action is imprimitive. Its leaves are the portions of lines through the origin. The upper triangular subgroup moves $p$ along the nonzero part of its line; linear transformations carry such lines to such lines.

**The real Euclidean plane.** Use the basis $J,P_1,P_2$ of $\mathfrak e(2)$ with

$$
[J,P_1]=P_2,\quad [J,P_2]=-P_1,\quad [P_1,P_2]=0.
\tag{5.1}
$$

Translations make the action transitive, and the isotropy at the origin is $\mathbb R J$. Suppose a larger subalgebra contains it. Subtract the $J$ component of an additional element to obtain a nonzero translation $v$. Closure under $[J,\cdot]$ adds its quarter-turn $Jv$. Over $\mathbb R$, $v$ and $Jv$ are independent, so the subalgebra contains both translation directions and is the whole algebra. The isotropy is maximal; the action is primitive. Over $\mathbb C$, $J$ has eigenlines in the complexified translation plane, and this last argument fails. The corresponding complex action is imprimitive.

**The real sphere.** Identify $\mathfrak{so}(3)$ with vectors under the cross product. At the north pole $p=(0,0,1)$, the map $u\mapsto u\times p$ spans the tangent plane and has kernel $\mathbb R p$. Any larger subalgebra contains a nonzero vector $v\perp p$ after subtracting its $p$ component. It also contains $p\times v$, which is independent of $v$. These vectors together with $p$ span $\mathbb R^3$. Thus the isotropy is maximal and the rotation action on $S^2$ is primitive.

## 6. Systatic and asystatic actions

For a transitive local action, call it **systatic** when the isotropy germ at a base point fixes a positive-dimensional manifold through that point. Otherwise call it **asystatic**. Transitivity makes this independent of the chosen nearby base point. An isolated additional fixed point elsewhere in a global manifold does not meet this local definition.

The algebraic criterion uses the normalizer

$$
\mathfrak n_{\mathfrak g}(\mathfrak h)
=\{u\in\mathfrak g:[u,\mathfrak h]\subset\mathfrak h\}.
\tag{6.1}
$$

Jacobi shows that this is a subalgebra containing $\mathfrak h$.

**Proposition 6.1.** The local fixed-point set of the isotropy on $H\backslash G$ is a manifold of dimension

$$
\dim\mathfrak n_{\mathfrak g}(\mathfrak h)-\dim\mathfrak h.
\tag{6.2}
$$

Thus the action is systatic precisely when $\mathfrak n_{\mathfrak g}(\mathfrak h)\supsetneq\mathfrak h$.

**Proof.** The point $Ha$ is fixed by every $b\in H$ exactly when $Hab=Ha$, or $aba^{-1}\in H$. At the level of subgroup germs, this is equivalent to $\operatorname{Ad}_a\mathfrak h=\mathfrak h$. Let $a=\exp u$ sufficiently near $e$. If $u\in\mathfrak n(\mathfrak h)$, equation $\operatorname{Ad}_{\exp u}=e^{\operatorname{ad}_u}$ proves this invariance. Conversely, if $e^{\operatorname{ad}_u}$ preserves $\mathfrak h$, so does its convergent matrix logarithm; that logarithm is $\operatorname{ad}_u$ near zero. Hence $u\in\mathfrak n(\mathfrak h)$.

The group normalizer germ is consequently the subgroup $N$ with algebra $\mathfrak n(\mathfrak h)$. Its image $H\backslash N$ in the quotient chart is the fixed-point manifold, with dimension (6.2). $\square$

At the tangent level, the isotropy acts on $\mathfrak g/\mathfrak h$ by $\operatorname{Ad}_{b^{-1}}$. Its fixed vectors are $\mathfrak n(\mathfrak h)/\mathfrak h$. The proposition proves that in this homogeneous situation these vectors actually integrate to the local fixed manifold.

For the punctured-plane action, $\mathfrak n(\mathbb R E)=\operatorname{span}(H,E)$, as the usual $\mathfrak{sl}_2$ brackets show. Its isotropy fixes the entire line through $p$, so this action is systatic. For the Euclidean and spherical actions, the normalizer equals the rotation isotropy: a nonzero transverse translation or transverse angular vector has a bracket with the rotation generator outside that line. Both actions are asystatic. The projective-line isotropy also equals its normalizer and is asystatic.

For the sphere, the global isotropy fixes both $p$ and $-p$. Near $p$ its fixed set is just $p$. Thus the antipodal observation is compatible with **asystatic** local behaviour; it does not establish systatic behaviour as suggested in the sketch.

If an effective primitive action has $n\ge2$, it is asystatic. Otherwise maximality forces $\mathfrak n(\mathfrak h)=\mathfrak g$, so $\mathfrak h$ is an ideal. Effectiveness then forces $\mathfrak h=0$. A zero maximal subalgebra forces $\dim\mathfrak g=1$, since every nonzero one-dimensional subspace is a subalgebra; this contradicts $n\ge2$. The dimension restriction is real: translations on a line are primitive and simply transitive, with trivial isotropy fixing every point, hence systatic under the stated definition. This exception must accompany any slogan that every systatic action is imprimitive.

## 7. Exercises

**Exercise 1 (easy).** Show that every transitive action on a line is primitive. Compare the local fixed manifolds of the isotropy for translations and for the affine action.

**Exercise 2 (medium).** Compute the isotropy algebra of $\operatorname{SL}_2(\mathbb R)$ at $(1,0)$, find an intermediate subalgebra, and identify its invariant foliation and fixed manifold.

**Exercise 3 (medium).** Prove directly from (5.1) that $\mathfrak{so}(2)$ is maximal in $\mathfrak e(2)$ over $\mathbb R$. Find an intermediate subalgebra after complexification.

**Exercise 4 (medium).** Determine every point of $S^2$ fixed by the rotations about the north–south axis. Explain why the antipodal point does not make the local action systatic.

**Exercise 5 (hard).** Reconstruct the action from a pair $(\mathfrak g,\mathfrak h)$ using a transverse section of $G$, and prove its independence of the section and its effectiveness criterion. Recover the classification by isomorphisms of pairs.

## 8. Solutions

**Solution 1.** A regular foliation on a line has leaf dimension zero or one; neither is a nontrivial imprimitivity system. Equivalently, a codimension-one isotropy subalgebra admits no strictly intermediate linear subspace, so it is maximal. Translations have zero isotropy; its identity subgroup fixes the whole line, a one-dimensional fixed manifold. The affine action has isotropy $\mathbb R x\partial_x$ at zero. This isotropy is dilation, whose local fixed set is zero alone. Thus translations are systatic and the affine action is asystatic, while both are primitive.

**Solution 2.** For $A=\left(\begin{smallmatrix}a&b\\c&-a\end{smallmatrix}\right)$, $A(1,0)^t=(a,c)^t$. The kernel is $\mathbb R E$. The subalgebra $\mathbb R H+\mathbb R E$ contains it strictly and has dimension two, strictly less than three. Its orbit through $(1,0)$ consists locally of $(s,0)$ with $s>0$ near one. Translating this orbit by the full linear group gives the foliation by line portions through the excluded origin. The isotropy matrices $\left(\begin{smallmatrix}1&t\\0&1\end{smallmatrix}\right)$ fix every $(s,0)$ and no nearby point with second coordinate nonzero. Therefore that line portion is also the isotropy fixed manifold. The action is both imprimitive and systatic.

**Solution 3.** A subalgebra containing $J$ and $aJ+v$ contains the nonzero translation $v$. It contains $[J,v]$, a quarter-turn, and over $\mathbb R$ these two translations are independent. Hence it contains $P_1,P_2,J$ and is the whole algebra. Over $\mathbb C$, take $v=P_1+iP_2$. Then $[J,v]=-iv$. Thus $\mathbb C J+\mathbb C v$ is a proper two-dimensional intermediate subalgebra. This exhibits why the field in the Euclidean example matters.

**Solution 4.** A point $(x,y,z)$ fixed by all axis rotations must have $(x,y)=(0,0)$: the half-turn already changes $(x,y)$ to $(-x,-y)$. On the unit sphere, $z=\pm1$. Conversely both poles are fixed by every axis rotation. Only the north pole belongs to a sufficiently small neighbourhood of the north pole. There is no positive-dimensional fixed germ there. The isotropy representation on its tangent plane is the ordinary real rotation representation, with no nonzero fixed vector; equivalently $\mathfrak n(\mathbb R p)=\mathbb R p$. The local action is asystatic.

**Solution 5.** Choose a complement $\mathfrak m$ to $\mathfrak h$ and a section $s(x)$ through $e$ tangent to $\mathfrak m$. The map $(h,x)\mapsto hs(x)$ has invertible differential, so local factorization is unique. Factor $s(x)b=h(x,b)s(y(x,b))$ and define $x\cdot b=y(x,b)$. Associativity of the group product, together with uniqueness of factorization, gives the action law: factoring $(s(x)b)c$ in two steps gives the same coset and section coordinate as factoring $s(x)(bc)$ directly. The identity acts identically, and $b^{-1}$ gives the local inverse. Differentiation at the section origin has kernel $\mathfrak h$ and is onto $\mathfrak m$, proving the prescribed isotropy and transitivity.

For another section $s'$, factor $s(x)=h(x)s'(\psi(x))$. The inverse-function theorem makes $\psi$ an analytic coordinate change. Both sections describe the same coset, so the factorization rule gives $\psi(x\cdot b)=\psi(x)\cdot' b$. This proves section independence by similarity. The kernel of the infinitesimal action is an ideal contained in $\mathfrak h$, and every such ideal acts trivially by the conjugation calculation in Lemma 2.1. Thus the action is effective exactly when $\mathfrak h$ contains no nonzero ideal. An isomorphism of pairs integrates to a group isomorphism and descends to cosets, giving similarity; conversely a similarity induces a bracket-preserving isomorphism of infinitesimal fields and carries the vanishing subalgebra at the base point to its counterpart. This completes the reconstruction and classification.

## References and historical comparison

Lie–Engel I, Chapter 21, Theorem 76 (printed p. 425), compares transitive actions through their stabilizers. Chapter 25, Theorems 91–92 (printed p. 521 and following), gives the primitivity criterion and the construction of invariant decompositions. Chapter 24, the definition preceding Theorem 87 (printed pp. 501–502), requires a continuous fixed manifold through a generic point for systatic behaviour. These local statements motivate the pair, foliation, and normalizer proofs above.

- Sophus Lie and Friedrich Engel, *Theorie der Transformationsgruppen*, Volume I (1888), the indicated chapters and theorem numbers.
- Joël Merker, [*Theory of Transformation Groups: Modern Presentation and English Translation*](https://arxiv.org/abs/1003.3202), the corresponding chapters. Its native text was used to check the original printed-page and theorem labels; the proofs and examples here were written independently.

Global homogeneous spaces $G/H$ require additional hypotheses on the global subgroup, and global discrete identifications can affect classification. Those questions are outside the local results proved here.
