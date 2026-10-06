# Normal toric orbits and derived realization

This reading proves derived realization for the orbit stratification of every complex normal separated toric variety of finite type. It supplies invariant affine neighborhoods, saturated monoid and lattice calculations, compatible weighted cone charts, contractible universal covers and the actual link maps. Singular and nonsimplicial cones are included. Three exercises have complete solutions.

*Original teaching text and solutions by GPT-6.1 Sol (OpenAI), Ultra, October 2026. CC0.*

## Setting and earlier comparisons

The variety is complex; the coefficient ring for bounded-below unrestricted realization is any associative unital ring. The derived finite-stalk heart is treated over every field. The statement preserves normality, separatedness, finite type and the classical topology.

The fixed-stratification reading proves the universal-cover theorem (25), full realization criterion (27)–(30), and normal-link test (31)–(34). The finite-coefficient reading proves the finite prime filtration, finite-heart theorem and abelian-monodromy comparison (48). The separately licensed Artin–Rees component linked below supplies the actual commutative-algebra proof. These earlier proofs are prerequisites, with their hypotheses retained.

Equations 50–77 retain their locators in the existing derived-constructibility lesson. The local toric proof below supplies its geometric and divisor arguments; it does not assume a global fan-classification theorem.

## Normal toric orbit stratifications in full generality

The projective line was one example. We now prove the realization theorem for every complex normal separated toric variety of finite type, with its orbit stratification and classical topology. Singular and nonsimplicial cones are included. Global projectivity and smoothness are unnecessary.

The references are Lunts and Schnürer's [Proposition 6.11 and Corollary 7.15](https://arxiv.org/html/2601.05477v1#S6.Thmtheorem11), Simon Telen's [*Introduction to Toric Geometry*](https://arxiv.org/html/2203.01690v1), and Hideyasu Sumihiro's [*Equivariant completion*](https://projecteuclid.org/download/pdf_1/euclid.kjm/1250523277), Theorem 1, Lemma 8 and Corollary 2 on. Their mathematical credit is retained. The proof below expands the toric specialization directly, including the affine-complement step left unstated in Sumihiro's Lemma 7.

Write *N* for the cocharacter lattice of the dense torus and *M* for its dual character lattice. A monomial character carries its character-lattice exponent; a real subscript means tensoring the lattice with the real numbers.

The geometry is local. First prove invariant affine neighborhoods, then classify their normal coordinate monoids and construct actual compatible cone neighborhoods. This supplies the theorem without importing a global fan-classification theorem as an unproved prerequisite. The product belongs to the orbit star; the entire variety need not be a product with that orbit.

Let $X$ be an irreducible normal separated complex algebraic variety of finite type, with a dense open torus $T=(\mathbb C^*)^n$ whose multiplication extends to an algebraic action on $X$. We prove that every point has a $T$-invariant affine open neighborhood. This is the missing local input for the full toric orbit-stratification argument; a global reconstruction of the fan is unnecessary.

### Normality and poles, with the needed algebra supplied

We use the already written Hilbert basis and Artin–Rees proofs in the separately licensed analytic-finiteness component, and the finite prime cyclic filtration proved in the finite-heart argument above. Both preserve their exact Noetherian hypotheses.

Here are the additional normal-domain facts. If $R$ is a Noetherian local domain and $a$ belongs to its maximal ideal, then

$$
\bigcap_{r\geq 0}a^rR=0.
\tag{50}
$$

Indeed the intersection $Q$ is a finitely generated ideal. Artin–Rees for $Q\subset R$ gives $Q=aQ$. On finitely many generators, that equality gives a matrix relation with matrix $I-aB$; its determinant is a unit and its adjugate kills the generators. Hence $Q=0$. This is also the finite-module Nakayama argument, with the determinant made explicit.

Consequently, if a nonzero maximal ideal of a Noetherian local domain is principal, say $(c)$, then every nonzero element is $c^r u$ for a finite $r$ and a unit $u$. Repeated division stops by (50). Every nonzero prime then contains $c$ and equals the maximal ideal. Such a local domain has dimension one.

We shall use one other determinant argument. If $z$ belongs to the fraction field of a domain and $zI\subset I$ for a nonzero finitely generated ideal $I$, express multiplication by $z$ on finitely many generators of $I$ by a matrix over the ring. Its characteristic polynomial kills those generators. A nonzero generator is faithful in a domain, so the monic polynomial vanishes at $z$. Thus $z$ is integral.

Let $A$ be a Noetherian integrally closed domain with fraction field $K$. Its localizations are integrally closed: clearing the finitely many coefficient denominators of a monic integral equation shows that a suitable denominator times its root is integral over $A$, hence lies in $A$. We claim

$$
A=\bigcap_{\operatorname{ht}\mathfrak p=1}A_{\mathfrak p}
\quad\text{inside }K.
\tag{51}
$$

To prove this, write $z=b/a\notin A$, with $a\ne0$. In the cyclic submodule generated by the nonzero class of $b$ in $A/aA$, choose a nonzero element whose annihilator is maximal among these annihilators. Noetherianity permits the choice. Its annihilator $\mathfrak p$ is prime: if $uv$ kills the element but $v$ does not, the nonzero element multiplied by $v$ has annihilator containing the original one and $u$, so maximality forces $u$ into it. The chosen element is the class of $db$, for some $d\in A$.

Set $y=db/a$. Its denominator ideal is exactly $\mathfrak p$; in particular $a\in\mathfrak p$ and $y\notin A_{\mathfrak p}$. In $R=A_{\mathfrak p}$, with maximal ideal $\mathfrak m$, we have $y\mathfrak m\subset R$. If $y\mathfrak m\subset\mathfrak m$, the determinant argument would make $y$ integral and hence an element of the normal ring $R$, a contradiction. Therefore some $c\in\mathfrak m$ has $yc$ a unit. For every $d'\in\mathfrak m$,

$$
d'=c\,\frac{yd'}{yc}.
$$

Thus $\mathfrak m=(c)$, and the preceding principal-maximal-ideal argument gives $\dim R=1$. We have found a height-one $\mathfrak p$ at which $y$, and hence $z$, is not regular. This proves (51).

A one-dimensional Noetherian normal local domain is a discrete valuation ring. To see the remaining point directly, take $0\ne a\in\mathfrak m$. All primes in the support of $R/aR$ are the maximal ideal, so the finite prime cyclic filtration makes this quotient finite length. It has a nonzero element with annihilator $\mathfrak m$. Choose its representative $b\notin aR$, and put $y=b/a$. Again $y\mathfrak m\subset R$, and normality and the determinant argument force an element $c\in\mathfrak m$ with $yc$ a unit. Thus $\mathfrak m=(c)$. Formula (50) supplies a finite exponent for every nonzero element, so its exponent of $c$ is the discrete valuation.

These proofs justify the pole criterion: on a normal variety, a rational function is regular precisely when it has no negative valuation at any prime divisor of each affine chart. They also justify extension across a closed subset of codimension at least two. On any affine chart, every height-one point is outside that subset; apply (51). Uniqueness follows from the dense open set.

For a Cartier divisor $D$, the same argument identifies the sections of $\mathcal O_X(D)$ with the rational functions $f$ satisfying $\operatorname{div}(f)+D\geq0$. Trivialize $D$ locally and apply (51); inequalities alone would be insufficient without normality.

### The boundary of an affine open is divisorial

Let $U_0\subset X$ be a nonempty affine open. Its complement has only codimension-one irreducible components. Suppose a component $C$ had codimension at least two. Remove all the other components of the complement to obtain an open neighborhood $V$ of the generic point of $C$; here $V\setminus U_0$ has codimension at least two.

Each of the finitely many coordinate generators of $\mathbb C[U_0]$ extends from $V\cap U_0$ to $V$ by the preceding pole criterion. Their equations continue to hold, since they hold on a dense open set. They define a morphism $V\to U_0$. Its composite with $U_0\hookrightarrow X$ equals the inclusion on $V\cap U_0$. Since $X$ is separated, equality holds everywhere: the inverse image of its closed diagonal contains a dense open set. Its image would therefore put all of $V$ in $U_0$, a contradiction.

Give the finitely many boundary prime divisors positive multiplicities. We obtain an effective Weil divisor $D$ with

$$
X\setminus\operatorname{Supp}D=U_0.
\tag{52}
$$

If $U_0=X$, use $D=0$. No assumption that $D$ is already Cartier is made.

### The torus fixes divisor classes

The Laurent polynomial ring $\mathbb C[t_1^{\pm1},\ldots,t_n^{\pm1}]$ is a unique factorization domain. For completeness, the polynomial-ring assertion follows inductively from Gauss's lemma: reducing coefficients modulo a prime factor proves that the product of primitive polynomials is primitive; factorization over the fraction field can then be cleared of content, giving existence and uniqueness over a factorial coefficient ring. Begin with the field, where the one-variable Euclidean algorithm supplies factorization. Inverting the variables preserves the remaining prime factorizations.

Thus the restriction to $T$ of any Weil divisor on $X$ is principal. Subtract that principal divisor on $X$. The resulting divisor is supported on the finitely many codimension-one components of $X\setminus T$. Each such component is $T$-invariant: the connected torus cannot permute a finite collection nontrivially. One can see this without a discreteness assumption on the permutation map: the image of the irreducible space $T\times E$, for a boundary component $E$, has irreducible closure in the finite union of those components and contains $E$, so it remains in $E$; translation is invertible.

Every divisor class therefore has a representative fixed by $T$. In particular,

$$
tD\sim D\qquad(t\in T),
\tag{53}
$$

where $\sim$ denotes linear equivalence, not merely algebraic or rational equivalence of arbitrary-dimensional cycles.

### Affine-complement divisors produce a projective embedding

We need the full elementary statement used as Lemma 7 in Sumihiro.

**Lemma.** Let $V$ be a normal separated variety. Suppose finitely many effective Weil divisors $D_i$, linearly equivalent to $D$, have affine complements $V_i=V\setminus\operatorname{Supp}D_i$ covering $V$. Then $V$ is quasi-projective.

**Proof.** At a point in $V_i$, the divisor $D_i$ is zero locally. Linear equivalence makes $D$ principal there. On overlaps the two local equations have quotient with divisor zero; the pole criterion applies to that quotient and its inverse, so their quotient is a regular unit. Hence $D$ and all $D_i$ are Cartier everywhere. Let $s_i$ be the corresponding sections of $\mathcal O_V(D)$, so $V_i=\{s_i\ne0\}$.

Choose finitely many coordinate generators $g_{ij}$ of each affine $V_i$. As rational functions on $V$, they can have poles only on the finitely many prime components of $D_i$. The pole criterion therefore supplies an integer $N\geq1$, common to all $i,j$, such that

$$
s_i^N,\qquad g_{ij}s_i^N,\qquad s_k s_i^{N-1}
\tag{54}
$$

are global sections of $\mathcal O_V(ND)$. For the middle sections, increase $N$ beyond every negative valuation divided by its positive multiplicity in $D_i$; for the others they are products of global sections. There are finitely many choices.

These sections have no common zero, because the $V_i$ cover. They give a morphism to a finite-dimensional projective space. The inverse image of the standard affine chart for coordinate $s_i^N$ is exactly $V_i$. The coordinate ratios on this chart include every $g_{ij}$; all the other ratios are regular functions on $V_i$. Consequently this chart map is a closed immersion: its coordinate-ring map is surjective because it contains the chosen algebra generators. On the union of those projective affine charts the morphism is a closed immersion, since being a closed immersion is local on the target and these charts cover the image. This union is open in projective space. We have a locally closed projective immersion, proving the lemma. $\square$

Apply the lemma to the toric variety as follows. Fix $x\in U_0$ and put

$$
U=\bigcup_{t\in T}tU_0.
\tag{55}
$$

This is an invariant open neighborhood of the entire orbit of $x$. It contains $T$, since $U_0$ meets that dense orbit. A Noetherian open is quasi-compact, so finitely many translates $t_iU_0$ cover $U$. The divisors $t_iD|_U$ have these affine complements and are linearly equivalent by (53). The lemma makes $U$ quasi-projective. This proves the toric specialization of Sumihiro's Lemma 8 with its formerly unstated affine-complement step supplied.

### Monomial sections make the embedding equivariant

Let $U$ now be this normal quasi-projective invariant neighborhood, still with dense torus $T$. Choose a projective locally closed embedding and a very ample Cartier divisor $H$ on $U$, with finitely many sections that realize that embedding. Since the Laurent ring is factorial, choose $f\in\mathbb C(T)^*$ with

$$
H_0=H-\operatorname{div}(f)
\quad\text{supported on }U\setminus T.
\tag{56}
$$

The divisor $H_0$ is Cartier and $T$-invariant. Multiplication by $f$ identifies the sections for $H$ with those for $H_0$. Every section for $H_0$, represented as a rational function, is regular on $T$; it is a finite Laurent polynomial there.

The space of such sections is preserved by torus translation, because $H_0$ is invariant and translations preserve its divisor inequalities. If a section has finitely many monomial weights, each individual monomial is itself a section. Indeed distinct Laurent characters are linearly independent. Choose sufficiently many torus elements so that their character evaluation matrix has full rank; otherwise a nonzero linear combination of the characters would vanish everywhere on $T$, contradicting this independence. Linear combinations of those translates isolate each weight component. They remain sections.

For all the finitely many original embedding sections, take all their monomial components. Their span $W$ is finite-dimensional, $T$-stable, and contains the original sections. It still has no base point and still gives a locally closed immersion

$$
U\hookrightarrow\mathbb P(W^*).
\tag{57}
$$

To check the last assertion, choose a basis of $W$ beginning with a basis of the old section space. On a chart where one of those old sections is nonzero, projection to the old coordinate ratios is defined. Those ratios already realize the old locally closed immersion; the additional ratios are regular functions on its image and give their graph. A graph into an affine space is closed over that image. The old nonvanishing charts cover $U$, so the added sections preserve the immersion.

Use the pullback action $(t\cdot s)(y)=s(t^{-1}y)$ on sections and its dual action on $W^*$. A monomial section $\chi^m$ has section weight $\chi^m(t)^{-1}$, and its evaluation coordinate has weight $\chi^m(t)$. The action is therefore diagonal and (57) is equivariant; equality on the dense torus extends to $U$. We have proved the needed toric specialization of Sumihiro's Theorem 1 without the general-group invertible-function or cocycle primitives.

### A semi-invariant equation gives the invariant affine open

Let $Y$ be the projective closure of the image of $U$ in (57), and let $B=Y\setminus U$, a closed invariant subset. If $B\ne\varnothing$, take a homogeneous polynomial vanishing on $B$ but not at the given point $x$. Such a polynomial exists by the definition of a projective closed subset and $x\notin B$. Its finite-dimensional homogeneous degree space decomposes into torus weights. Since the homogeneous ideal of $B$ is invariant, the same translate-and-project argument puts each weight component in that ideal. At least one component $F$ is nonzero at $x$.

If $B$ is empty, instead take any projective coordinate nonzero at $x$ and then choose a nonzero weight component; the vanishing-on-boundary condition is vacuous. In either case $F$ is homogeneous of positive degree and semi-invariant. Therefore

$$
V_x=Y\cap\{F\ne0\}\subset U
\tag{58}
$$

is invariant and contains $x$. It is affine. Under the Veronese embedding of degree $\deg F$, $F$ becomes a linear homogeneous coordinate; its nonvanishing locus is a standard affine projective chart, and $Y$ intersects it in a closed affine subvariety. If $U$ is a point the assertion is immediate, so no positive-dimensional coordinate exception is needed.

Thus every point of the original normal separated toric variety has an invariant affine open neighborhood. The proof uses normality for the pole extension and divisor-to-section steps, separatedness for the boundary lemma, finite type for Noetherianity, and the dense torus for factorial Laurent functions and finite weight spaces. None of these hypotheses has been dropped.


### From an invariant affine chart to its rational cone

Let $U \subset  X$ be a nonempty invariant affine open supplied by the preceding affine-neighborhood theorem. It contains the dense torus: it meets the torus, and invariance makes the intersection the entire transitive torus orbit. Restriction to the dense torus embeds the coordinate algebra $A=\mathbb C[U]$ in the Laurent algebra $\mathbb C[M]$; both have the same fraction field because the torus is dense open. $A$ is a finitely generated normal domain.

The regular torus action has a coordinate coaction $A\to \mathbb C[M]\otimes A$. If the restriction of $f\in A$ to the torus is the Laurent sum $\sum c_m \chi^m$, the coefficient of $\chi^m$ in this coaction restricts to $c_m \chi^m$ on the dense torus. Linear independence of Laurent characters and injectivity of restriction show that every such component lies in $A$. Hence $A$ is a direct sum of one-dimensional monomial weight spaces. Define $S={m\in M:\chi^m\in A}$. Multiplication gives closure under addition and $0\in S$, and

$$
A=\mathbb C[S].
\tag{59}
$$

Choose finitely many algebra generators of $A$ and collect the finitely many monomials occurring in their Laurent expansions. All these monomials lie in $A$, so they generate it as an algebra; linear independence shows their exponents generate $S$ as a monoid. This proves finite monoid generation without assuming an affine toric classification.

Moreover $\mathbb Z S=M$. For any $m\in M$, express $\chi^m=f/g$ in the common fraction field with nonzero $f,g\in \mathbb C[S]$. Choosing a monomial exponent $n$ with nonzero coefficient in $g$, the equality $\chi^m g=f$ implies $n+m\in S$. Hence $m=(n+m)-n$ belongs to $\mathbb Z S$. If $a m\in S$ for a positive integer $a$, then $\chi^m$ is in the fraction field and satisfies the monic equation $Y^a-\chi^{am}=0$ over $A$. Normality gives $\chi^m\in A$, so $m\in S$. Thus $S$ is saturated in the full torus character lattice $M$.

Let $C=\operatorname{cone}_{\mathbb R}(S)$. It is rational polyhedral by finite generation, and spans $M_{\mathbb R}$ because $\mathbb Z S=M$. For any $m\in C\cap M$, an expression as a nonnegative real combination of the integral generators can be chosen rational: discard a linear dependence while preserving nonnegativity until the used vectors are linearly independent, then solve their rational linear system. After clearing denominators, $a m\in S$ for some positive integer $a$; saturation gives $m\in S$. Consequently

$$
S=C\cap M=\sigma^\vee\cap M,
\qquad \sigma=C^\vee\subset N_\mathbb R.
\tag{60}
$$

Polyhedral duality makes $\sigma$ rational, and the fact that $C$ spans $M_{\mathbb R}$ makes $\sigma$ strongly convex. This proves $U\cong U_\sigma$, including its torus action. It imposes no full-dimensionality, simpliciality, or smoothness on $\sigma$. A point $x\in U_\sigma$ belongs to a unique orbit $O(\tau)$ by the orbit-face calculation below. Localizing as in (75) replaces the chart by $U_\tau$, where $O(\tau)$ is the unique closed orbit. Rename that cone $\sigma$ for the ensuing product and link calculation. This supplies precisely the affine model used there.

The elementary polyhedral calculations just used can also be proved directly. A finitely generated cone is closed: eliminate a linear dependence among a nonnegative expression by subtracting a suitable multiple of that dependence until one coefficient is zero. Repeating leaves linearly independent generators. Hence the cone is a finite union of cones on independent subsets, each closed in its linear span. If $x$ is outside a closed cone $C$, let $q\in C$ minimize its Euclidean distance to $x$. Convexity gives $\langle q-x,c-q\rangle \ge 0$ for every $c\in C$; using $c=0,2q$ gives $\langle q-x,q\rangle =0$. Thus the functional $q-x$ is nonnegative on $C$ and strictly negative on $x$. This proves $C^{\vee\vee}=C$.

To see finite rational generation of a dual, start with $\mathbb R^n=\operatorname{cone}(\pm e_i)$ and impose the finite rational inequalities one at a time. Suppose a current cone is generated by $v_i$, and impose $l\ge 0$. Retain generators with $l(v_i)\ge 0$ and add, for every positive/negative pair, the zero-level vector

$$
l(v_i)v_j-l(v_j)v_i\qquad(l(v_i)>0>l(v_j)).
$$

These generate the intersection. In a nonnegative expression satisfying $l\ge 0$, distribute the positive $l$-mass to cancel the negative $l$-mass in pairs; the canceled pairs give exactly these vectors and the remainder uses the retained nonnegative generators. All generators stay rational, and denominators may be cleared. This proves rational polyhedral duality without a Minkowski–Weyl theorem as a hidden import.

For the face calculations below, take a relative interior point $u$ of a cone defined by finitely many generator inequalities. Its face is cut out by those inequalities that vanish at $u$: a small displacement in their common kernel still satisfies every other, strict, inequality. Therefore that kernel is the span of the face, and the active generators span its annihilator. This proves the dual-face description and its dimension. Exposing functionals for rational faces may be chosen rational by solving the vanishing rational linear equations and approximating while preserving the finitely many strict inequalities; multiplication clears denominators. Finally, the sum of a set of nonzero integral cone generators spanning the cone lies in its relative interior, which supplies the integral interior points used later.

### The saturated lattice product at an orbit

Put

$$
N_\sigma=N\cap\operatorname{span}_{\mathbb R}\sigma,
\qquad k=\dim\sigma.
$$

This lattice is saturated in $N$: if $a n \in  N_\sigma$ for a nonzero integer $a$, then $n$ belongs to the same real span. Thus $N/N_\sigma$ is torsion free. A saturated subgroup of a finite free lattice splits. To prove this, divide any nonzero vector in the subgroup by the gcd of its coordinates; saturation keeps that primitive vector in the subgroup. Euclidean integer row operations send it to the first basis vector, so it extends to a basis of the ambient lattice. Subtracting its coordinate splits off this rank-one subgroup. The intersection with the complementary lattice remains saturated. Repeat by induction on the subgroup rank. Thus there is a complement $N^c$ and a decomposition

$$
N=N_\sigma\oplus N^c.
\tag{61}
$$

This is a split of lattices, not a choice of a basis among ray generators. In a singular cone those rays need not generate the saturated lattice, and using their lattice instead would insert an unnecessary finite quotient.

Let $M_\sigma = \operatorname{Hom}(N_\sigma,\mathbb Z)$ and $M^c = \operatorname{Hom}(N^c,\mathbb Z)$, extended to $N$ by zero on the other factor. Since $\sigma$ lies in $(N_\sigma)_{\mathbb R}$,

$$
\sigma^\vee\cap M
=\bigl(\sigma^\vee_{N_\sigma}\cap M_\sigma\bigr)\oplus M^c.
$$

Writing $S' = \sigma^\vee_{N_\sigma} \cap  M_\sigma$ gives the actual algebra and variety maps

$$
\mathbb C[\sigma^\vee\cap M]
\cong \mathbb C[S']\otimes_\mathbb C\mathbb C[M^c],
\qquad
\chi^{m'+m^c}\longmapsto\chi^{m'}\otimes\chi^{m^c},
$$

$$
U_\sigma\cong X'\times T_{N^c},
\qquad X'=\operatorname{Spec}\mathbb C[S'].
\tag{62}
$$

The cone $\sigma$ is full dimensional in $(N_\sigma)_{\mathbb R}$. Its dual there is pointed, so the monoid map $S'\to\mathbb C$, equal to one at zero and zero at every other monoid element, defines a point $p \in  X'$. It is the unique fixed point of $T_{N_\sigma}$. Under (62),

$$
O(\sigma)=\{p\}\times T_{N^c}.
$$

For every face $\tau \preceq  \sigma$, the same splitting identifies the orbit

$$
O(\tau)=S'_\tau\times T_{N^c},
\qquad
S'_\tau\cong T_{N_\sigma/N_\tau},
\qquad N_\tau=N\cap\operatorname{span}_{\mathbb R}\tau.
\tag{63}
$$

The quotient lattices in (63) are free, because the span lattices are saturated. For a proper face, $d = k - \dim \tau > 0$, so $S'_\tau \cong  (\mathbb C^*)^d$. For $\tau=\sigma$, this transverse orbit is just $p$ and is handled as the cone vertex.

### A contracting action with positive weights

The monoid $S'$ has finitely many generators. Here is the elementary finite-generation argument if Gordan’s lemma is not already available. Express the rational cone $\sigma^\vee_{N_\sigma}$ as the positive span of finitely many integral vectors $u_i$. For a lattice point $m=\sum a_i u_i$, with $a_i \ge  0$, subtract $\sum \lfloor a_i\rfloor u_i$. The remainder is a lattice point in the bounded set $\sum [0,1]u_i$ and still lies in the cone. There are only finitely many such lattice remainders. They and the $u_i$ generate $S'$.

Choose nonzero generators $m_1,\ldots,m_r$ (zero adds no coordinate). They give a closed monomial embedding

$$
X'\hookrightarrow\mathbb C^r,
\qquad z_i=\chi^{m_i},\qquad p=0.
\tag{64}
$$

For $k>0$, choose an integral point $v \in  \operatorname{relint}(\sigma)$; rational polyhedrality lets one multiply a rational interior point by a common denominator. Every nonzero $m_i$ in the dual cone has

$$
a_i=\langle m_i,v\rangle\in\mathbb Z_{>0}.
$$

Indeed a dual functional vanishing at an interior point must vanish on the whole full-dimensional cone and hence be zero. The cocharacter $v$ acts in (64) as

$$
\lambda(t)(z_1,\ldots,z_r)
=(t^{a_1}z_1,\ldots,t^{a_r}z_r),
\qquad t\in\mathbb C^*.
\tag{65}
$$

The monomial relations are preserved by (65), since equal sums of $m_i$ have equal total weight. Formula (65) extends to $t=0$ by the constant point $p$. Thus it gives a continuous contraction of $X'$ to $p$. For positive real $t$, it preserves every $T_{N_\sigma}$-orbit. No ordinary scalar-invariance of $X'$ is asserted or needed.

### From contraction to a compatible cone

Fix $\varepsilon>0$ and use the Euclidean norm in (64). Set

$$
L_\varepsilon=X'\cap\{\|z\|=\varepsilon\},
\qquad W_\varepsilon=X'\cap\{\|z\|<\varepsilon\}.
$$

The total link $L_\varepsilon$ is compact because $X'$ is closed and the sphere is compact. It need not be a manifold or an aspherical space. Only its individual orbit pieces will have those properties.

For $z\ne 0$, the function

$$
F_z(t)=\|\lambda(t)z\|^2
=\sum_i t^{2a_i}|z_i|^2,\qquad t>0,
$$

is strictly increasing, with limits zero and infinity. Its derivative is positive because some $z_i$ is nonzero. There is exactly one $s(z)>0$ with $F_z(s(z))=\varepsilon^2$. The solution depends continuously on $z\ne 0$, by the implicit function theorem (or strict monotonicity and the two endpoint limits). Put

$$
y(z)=\lambda(s(z))z\in L_\varepsilon,
\qquad t(z)=s(z)^{-1}.
$$

These maps are inverse to the explicit homeomorphism

$$
\Phi:L_\varepsilon\times(0,\infty)
\xrightarrow{\sim}X'\setminus\{p\},
\qquad \Phi(y,t)=\lambda(t)y.
\tag{66}
$$

For $0<t<1$, the image has norm less than $\varepsilon$. Adding the vertex gives

$$
\overline\Phi:\operatorname{Cone}(L_\varepsilon)
\xrightarrow{\sim}W_\varepsilon,
\tag{67}
$$

where the open cone has radial coordinate in $[0,1)$. The continuity at the collapsed end, including that of the inverse, follows from the explicit estimates for $y\in L_\varepsilon$ and $0<t\le 1$:

$$
\varepsilon t^{a_{\max}}
\le\|\lambda(t)y\|
\le\varepsilon t^{a_{\min}}.
\tag{68}
$$

In particular $t\to 0$ makes all directions converge uniformly to $p$, and $z\to p$ forces $t(z)\to 0$. Compactness of the link means the quotient cone neighborhoods at the vertex contain a uniform short radial interval, so these estimates verify the quotient topology as well. This is the step that a mere contraction does not supply by itself.

For a proper face $\tau\prec \sigma$, set

$$
L_\tau=L_\varepsilon\cap S'_\tau.
$$

Because positive cocharacter scaling preserves orbits, (66) restricts to

$$
L_\tau\times(0,\infty)\cong S'_\tau,
\qquad
L_\tau\times(0,1)\cong W_\varepsilon\cap S'_\tau.
\tag{69}
$$

Each $L_\tau$ is nonempty: a point of the nonzero orbit can be scaled uniquely to the sphere. It is a smooth real manifold of dimension $2d-1$. Indeed the derivative of $\|z\|^2$ along the positive-scaling vector field on the smooth torus orbit is $\sum 2a_i|z_i|^2>0$, so the sphere is a regular level on that orbit. It is connected, since (69) identifies its product with a connected torus. There are finitely many pieces, one for each proper face. Their frontier relation is exactly the restriction of the affine orbit relation: if points in one orbit approach a point on the sphere, apply the continuous normalization $y(z)$ to obtain approaching points in the corresponding link piece. The converse follows by inclusion in the orbit closure. Thus these pieces are a stratification of the total link.

### Normal charts at every point of the orbit

Let $x\in O(\sigma)$, and identify that orbit with $T_{N^c}$ in (62). Choose a small real coordinate ball $B_x$ in this torus. Then

$$
V_x=W_\varepsilon\times B_x
\cong\operatorname{Cone}(L_\varepsilon)\times B_x
\tag{70}
$$

is open in the ambient variety and contains $x$. Its intersection with the closed orbit is ${p}\times B_x$, and for every incident orbit $S=O(\tau)$, $\tau\prec \sigma$,

$$
S\cap V_x\cong L_\tau\times(0,1)\times B_x.
\tag{71}
$$

The base orbit corresponds to the cone vertex, not a punctured link piece. All non-base orbits meeting this affine chart are incident by the orbit-cone relation. No nonincident orbit meets it. Decreasing the radius at $p$ and the ball at $x$ gives a basis of neighborhoods. Alternatively, keep $L_\varepsilon$ fixed and restrict the weighted radial coordinate to $[0,\eta)$; (68) proves that these neighborhoods are cofinal with ordinary small Euclidean neighborhoods. The chart respects the stratification for every such decrease.

When $k=0$, the chart is just a small ball in the open torus orbit. There is no transverse nonzero orbit or incident link piece; set $\operatorname{Cone}(\varnothing)={p}$. Finite type gives finitely many orbit strata: use a finite invariant affine cover and the finite number of faces in each cone chart. Thus (70)–(71) supply precisely the finite normal structure needed in the course criterion.

### Universal covers and the actual link map

The inclusion $i_\tau:L_\tau\to S'_\tau$ at radial coordinate one in (69) is a strong deformation retract. In the product coordinates, the homotopy is $(y,t)\mapsto (y,(1-u)t+u)$, $0\le u\le 1$; transporting it through (66) gives a homotopy entirely inside the same orbit. Therefore

$$
\pi_1(L_\tau)\xrightarrow{\sim}\pi_1(S'_\tau)
=N_\sigma/N_\tau.
\tag{72}
$$

The torus $S'_\tau\cong (\mathbb C^*)^d$ has universal cover $\mathbb C^d$, by coordinatewise exponentiation, with deck lattice $2\pi i \mathbb Z^d$. Its universal cover is contractible. The connected smooth manifold $L_\tau$ has a universal cover $\widetilde L_\tau$. By (69), $\widetilde L_\tau\times (0,\infty)$ is a universal covering of $S'_\tau$, hence is isomorphic as a covering to $\mathbb C^d$. It is contractible, and the projection to the slice at one shows $\widetilde L_\tau$ itself is contractible. Consequently every incident link piece is a $K(\pi ,1)$ manifold. Contractibility also implies its universal cover is acyclic for every unital coefficient ring. Every ambient orbit $O(\tau)\cong T_{N/N_\tau}$ has the same property.

Choose the link slice by holding the base torus coordinate fixed at $x$. Its map into the ambient stratum in (63) is

$$
L_\tau\longrightarrow S'_\tau\times T_{N^c},
\qquad y\longmapsto(y,x).
$$

It is a homotopy equivalence onto the first factor followed by a factor inclusion. On the intrinsic cocharacter lattices the actual homomorphism is

$$
N_\sigma/N_\tau\longrightarrow N/N_\tau,
\qquad [n]\longmapsto[n].
\tag{73}
$$

Its kernel is zero: a representative in $N_\sigma$ maps to zero exactly when it belongs to $N_\tau$. After choosing (61), its cokernel is $N^c$. Basepoint changes only conjugate fundamental-group homomorphisms; here the orbit groups are abelian, so the injection is independent of that change. This identifies the map required by Theorem 6.10(2)(a), not an unrelated abstract embedding of groups.

Combining (70)–(73) with tags (31)–(34) of the existing lesson yields unrestricted bounded-below realization for the orbit stratification using the affine-neighborhood theorem already proved. All stratum groups are free abelian of finite rank. Over a field, the existing finite-heart theorem (48) therefore gives the bounded finite-stalk realization as well. No classification of indecomposable injectives is part of this geometric proof.

### The orbit-face and star-localization calculation

This section expands the elementary cone-chart input used above. The invariant affine-neighborhood theorem above has already supplied the connection to an abstract normal toric variety.

For a point of $U_\sigma$, evaluation gives a multiplicative monoid map $\gamma:S=\sigma^\vee\cap M\to\mathbb C$ with $\gamma(0)=1$. Conversely evaluation of monoid generators satisfying the monomial relations defines a point. The torus action is $(t·\gamma)(m)=\chi^m(t)\gamma(m)$.

The nonzero support $F={m:\gamma(m)\ne 0}$ is a monoid face: $a+b\in F$ if and only if both $a,b\in F$. Choose finitely many monoid generators $s_i$ and let $I$ index those in $F$. Then $F$ is exactly the monoid generated by these $s_i$. Its cone is an exposed face of $C=\sigma^\vee$. One elementary verification is to project the excluded generators modulo $\operatorname{span}_{\mathbb R}{ s_i:i\in I }$. Zero cannot lie in their convex hull: a rational positive relation to this span, with denominators cleared and the inside terms moved to opposite sides, would give a monoid equality whose one side evaluates to zero and other side to nonzero. A real feasible relation can be chosen rational by row reduction over $\mathbb Q$ and approximation in its affine solution space. Separating zero from that compact convex hull gives a functional zero on the inside span and strictly positive on every excluded generator. It can be chosen rational and scaled integral. If there are no excluded generators, use the zero functional.

Thus for a unique face $\tau\preceq \sigma$,

$$
F=\sigma^\vee\cap\tau^\perp\cap M.
$$

The elementary dual-face relation identifies $\tau$ as the common zero face in $\sigma$ of the inside generators. The separating functional is in its relative interior because all remaining generator inequalities are strict. Dual-face uniqueness follows from the same defining zero inequalities.

The group generated by $F$ is exactly $M\cap \tau^\perp$. To see this, choose an integral relative interior point $w$ of its cone. For any lattice $m$ in its span, $aw+m$ and $aw$ belong to that cone for sufficiently large integer $a$, so $m$ is a difference of two elements of $F$. (If the cone is its whole span, take $w=0$.) Restriction of $\gamma$ to $F$ consequently extends to a character of $M\cap \tau^\perp$. Conversely any such character, extended by zero outside $F$, is a monoid point. The lattice $M\cap \tau^\perp$ is saturated in $M$; split it off to extend a character to $M$. The torus therefore acts transitively on points of each support, proving

$$
O(\tau)\cong\operatorname{Hom}(M\cap\tau^\perp,\mathbb C^*)
\cong T_{N/N_\tau}.
\tag{74}
$$

For faces $\tau\preceq \eta\preceq \sigma$, positive cocharacter limits with an integral $u\in \operatorname{relint}(\eta)$ carry the distinguished point of $O(\tau)$ to that of $O(\eta)$: evaluate $t^{\langle m,u\rangle }\gamma_\tau(m)$ and let $t\to 0$. This proves $O(\eta)\subset \overline{O(\tau)}$ in the classical topology. Conversely monomials vanishing on $O(\tau)$ vanish on its closure. The support of a point in $O(\eta)$ must then be contained in the dual face of $\tau$; dual-face inclusion reverses the original face inclusion, giving $\tau\preceq \eta$. This proves the incidence relation used in (63) and (71).

Finally, if $\tau\preceq \sigma$, choose integral $h\in \sigma^\vee$ with $\sigma\cap h^\perp=\tau$. For $m\in \tau^\vee\cap M$, the finitely many ray inequalities for $\sigma$ show $m+a h\in \sigma^\vee$ for all sufficiently large integers $a$: on rays in $\tau$ the inequality already holds; on the other rays $h$ is positive. Hence

$$
\tau^\vee\cap M
=(\sigma^\vee\cap M)+\mathbb Z(-h),
\qquad
U_\tau=D(\chi^h)\subset U_\sigma.
\tag{75}
$$

This affine invariant open has $O(\tau)$ as its unique closed orbit. In a global toric variety, an invariant open containing an orbit also contains every orbit whose closure meets that orbit: the open intersects the latter orbit, hence contains it by invariance and transitivity. Applied to (75), and combined with its affine orbit description, this proves that the chosen affine open is exactly the union of global orbits incident to the chosen closed orbit. It is the open orbit star meant in Proposition 6.11. This last argument uses no global fan classification.


### The general realization theorem

**Theorem.** Let $X$ be a complex normal separated toric variety of finite type, in its classical topology, and let $\mathcal S$ be its torus-orbit stratification. For every associative unital coefficient ring $R$,

$$
D^+(\operatorname{Cons}_R(X,\mathcal S))
\xrightarrow{\sim}D^+_{\mathcal S}(X;R).
\tag{76}
$$

The bounded restriction is an equivalence as well. Over every field $k$, the derived finite-stalk heart also realizes all bounded complexes with finite-stalk orbit-constructible cohomology:

$$
D^b(\operatorname{Cons}_{ft,k}(X,\mathcal S))
\xrightarrow{\sim}D^b_{\mathcal S,ft}(X;k).
\tag{77}
$$

**Proof.** Every orbit has an invariant affine star by the neighborhood, monoid and face-localization arguments. The saturated product and weighted-sphere construction give the normal charts, with one connected manifold link piece for each incident orbit. The number of orbits is finite. Each stratum and each incident link piece has a contractible universal cover, and its actual link-to-stratum fundamental-group map is the injection (73).

The universal-cover theorem (25) therefore gives realization on every stratum over $R$. The normal-link argument (31)–(34) gives the internal-to-ambient direct-image comparison: restriction along an injective group homomorphism preserves injective modules because induction is exact. The full fixed-stratification criterion (27)–(30), with its actual finite gluing, now proves (76). Restrict to bounded cohomology for its bounded version. No finite-kernel averaging or characteristic condition is needed here.

For (77), every stratum group is the finite free lattice $N/N_\tau$. The cone charts have finitely many incident link components. Thus the finite-heart theorem (48), whose required injectives were actually constructed by Artin–Rees and Baer, applies. Compose it with the bounded finite-cohomology restriction of (76). This proves (77), rather than merely an objectwise finite-cohomology assertion. $\square$

## Exercises on singular toric links and weighted charts

### A redundant monomial coordinate changes the radial weights

*Difficulty: Intermediate.*

Embed $\mathbb A^2$ in $\mathbb C^3$ by $(x,y)\mapsto(x,y,x^2)$. Explain why ordinary scalar multiplication does not give the required cone coordinates in this embedding. Construct the weighted action and prove that every nonzero point has exactly one positive scaling to a sphere of radius $\varepsilon>0$.

**Solution.** The image is $z=x^2$. Ordinary scalar multiplication would require $tz=(tx)^2=t^2x^2$, which fails for $x\ne0$ and $t\notin\{0,1\}$. The cocharacter action is $(x,y,z)\mapsto(tx,ty,t^2z)$, with weights $1,1,2$; it preserves the equation. For a nonzero point put $A=|x|^2+|y|^2>0$ and $B=|z|^2\geq0$. The squared norm is $At^2+Bt^4$, strictly increasing from zero to infinity for $t>0$. If $B=0$, the unique value is $t=\varepsilon/\sqrt A$. Otherwise its square is $(\sqrt{A^2+4B\varepsilon^2}-A)/(2B)>0$. This solves the sphere equation and proves uniqueness. The positive action preserves each torus orbit, so the resulting radial coordinates respect the orbit strata.

### Ray generators are not always the saturated span lattice

*Difficulty: Intermediate.*

In $N=\mathbb Z^2$, let $\sigma$ be generated by $u=(1,0)$ and $v=(1,2)$. Compare the lattice they generate with $N_\sigma$. For the face $\tau=\mathbb R_{\geq0}u$, compute the genuine link-group map at the closed orbit.

**Solution.** The ray lattice is $\mathbb Zu+\mathbb Zv=\{(a,b):b\text{ is even}\}$, of index two in $N$. The real span of $\sigma$ is all of $N_\mathbb R$, so $N_\sigma=N$, not this index-two subgroup. Also $N_\tau=\mathbb Z(1,0)$, so both $N_\sigma/N_\tau$ and $N/N_\tau$ are $\mathbb Z$, generated by the class of $(0,1)$. The actual link map (73) is their identity. Using only the ray lattice would instead produce the subgroup $2\mathbb Z$ in this coordinate. That artificial index comes from a finite covering of the affine torus, not from the geometric link. Saturation is necessary even though both rays themselves are primitive.

### The dense-orbit link differs from the total singular link

*Difficulty: Advanced.*

For the same cone, show that its affine toric surface is $XZ=Y^2$. Describe the link piece of the dense orbit, and exhibit a loop that is nonzero in that piece but becomes contractible in the total link. Explain which group the realization test uses.

**Solution.** The dual inequalities are $a\geq0$ and $a+2b\geq0$. Its lattice monoid is generated by $(0,1),(1,0),(2,-1)$: for $b\geq0$ use the first two; for $b<0$ subtract $(-b)(2,-1)$, leaving $(a+2b,0)$. Their single relation is $(0,1)+(2,-1)=2(1,0)$. Consequently the monoid algebra is $\mathbb C[X,Y,Z]/(XZ-Y^2)$. To verify that no additional relations occur, reduce every monomial using $XZ=Y^2$ until either its $X$- or its $Z$-exponent is zero. The two resulting families have distinct character exponents except for their common powers of $Y$.

The map $(u,v)\mapsto(u^2,uv,v^2)$ identifies the surface with the quotient of $\mathbb C^2$ by simultaneous sign. It is surjective by choosing a square root of $X$ when $X\ne0$, and of $Z$ otherwise; its fibers are precisely those sign pairs. It is proper, since bounded $X,Z$ bound $u,v$; the induced continuous bijection from the quotient is therefore a homeomorphism. The positive cocharacter $(1,1)$ gives weight one to $X,Y,Z$. Radial normalization identifies the total sphere link with $S^3/\{\pm1\}$.

On the dense orbit $u,v\ne0$, write a unit-sphere point as
$(r e^{i\alpha},\sqrt{1-r^2}e^{i\beta})$, $0<r<1$. The sign quotient identifies $(\alpha,\beta)$ with $(\alpha+\pi,\beta+\pi)$. Thus the dense-orbit link is the product of an open interval and a two-torus, with period lattice
$\mathbb Z^2+\mathbb Z(\tfrac12,\tfrac12)$ when angles are divided by $2\pi$. The positive-radius product gives the same period lattice for the dense orbit itself, so its link map is an isomorphism, as (72)–(73) predict.

Keep $v=b\ne0$ and let $u=a e^{i\theta}$, with $|a|^2+|b|^2=1$. Its image is a nonzero period in that dense link; in the original cocharacter lattice it is $(1,2)$, since $X,Y,Z$ wind by $2,1,0$. In the full $S^3$, it bounds the explicit disk
$(r a e^{i\theta},\sqrt{1-r^2|a|^2}\,b/|b|)$, $0\leq r\leq1$. At $r=0$ the angular coordinate collapses to a point with $u=0$. Project the disk to the sign quotient and normalize to the surface sphere. It contracts this loop in the total link, passing through a boundary orbit. The realization test uses the link piece within each incident stratum, with its map to that stratum; it does not replace that piece by the entire singular link.

## Sources and reuse

Lunts and Schnürer's Categories of constructible sheaves supplies the modern toric realization statements. Simon Telen's Introduction to Toric Geometry and Hideyasu Sumihiro's Equivariant completion supply the credited geometric source questions and arguments at the exact locators linked in the proof. Guillaume Valette's Artin–Rees component retains CC BY4.0 at its linked provider. The earlier derived-category foundations retain the Stacks project authors' credit and their component terms. No source expression is imported or relicensed here. Original teaching, three complete solutions and reader code are CC0.

Self-checked by the writing AI.

[Reading index](README.md) · [Reuse terms](LICENSE.txt) · Provenance
