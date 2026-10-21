# Transitivity and primitivity

*GPT-6.1 Sol (OpenAI). Original exposition and English translations: CC0 1.0; quoted German originals are public domain.*

The same Lie algebra can act on spaces of different dimensions. The missing information is the stabilizer of a point. For a transitive action, a Lie algebra together with that stabilizer determines the entire local geometry. Subalgebras between the stabilizer and the whole algebra describe every invariant foliation. This turns the question of primitivity into a question about maximal subalgebras.

We work with analytic local right actions $p\cdot a$, using $T_bT_a=T_{ab}$, and the infinitesimal homomorphism $u\mapsto X_u$. We use the Frobenius theorem of Complete systems and invariants and the local groups and subgroup germs constructed in The adjoint group, composition and isomorphism. The manifold has positive dimension. Connectedness and effectiveness below are local conditions. The Euclidean and spherical examples are real; complexification can change primitivity.

The analytic inverse and constant-rank theorems are proved in Transformation groups and their parameters, Theorems A–B. The matrix logarithm used in Section 6 is supplied by the matrix exponential and logarithm lemma in The adjoint group, composition and isomorphism.

## 1. Orbits and isotropy

For a point $p$, define the evaluation map, orbit distribution, and isotropy algebra by

$$
\begin{gathered}
\operatorname{ev}_p:\mathfrak g\to T_pM,\\
 u\mapsto X_u(p),
\\
 D_p=\operatorname{im}\operatorname{ev}_p,
\\
 \mathfrak h_p=\ker\operatorname{ev}_p.

\end{gathered}\tag{1.1}
$$

If two vector fields vanish at $p$, their bracket also vanishes there, as its coefficients are $DX_v\,X_u-DX_u\,X_v$. Thus $\mathfrak h_p$ is a subalgebra. It need not be an ideal.

The action law gives, for $q=p\cdot a$,

$$
\begin{gathered}
X_u(q)=(dT_a)_p X_{\operatorname{Ad}_a u}(p),\\

\mathfrak h_q=\operatorname{Ad}_{a^{-1}}\mathfrak h_p.

\end{gathered}\tag{1.2}
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

Suppose $f:\mathfrak g\to\mathfrak g'$ is an isomorphism with $f(\mathfrak h)=\mathfrak h'$. Lesson 7, Theorem 2.2 integrates it to a local group isomorphism $F:G\to G'$. Uniqueness of subgroup germs gives $F(H)=H'$. Consequently

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
\begin{gathered}
H\backslash G\longrightarrow K\backslash G,\\
 Ha\longmapsto Ka.

\end{gathered}\tag{4.2}
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
\begin{gathered}
{}[J,P_1]=P_2,\\
 {}[J,P_2]=-P_1,\\
 {}[P_1,P_2]=0.

\end{gathered}\tag{5.1}
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

For the sphere, the global isotropy fixes both $p$ and $-p$. Near $p$ its fixed set is just $p$. Thus the antipodal observation is compatible with **asystatic** local behaviour; it does not establish systatic behaviour.

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

Lie–Engel I, Chapter 21, Theorem 76 (printed p. 425), compares transitive actions through their stabilizers. Chapter 24, Theorems 91–92 (printed p. 521 and following), gives the primitivity criterion and the construction of invariant decompositions. Chapter 24, the definition preceding Theorem 87 (printed pp. 501–502), requires a continuous fixed manifold through a generic point for systatic behaviour. These local statements motivate the pair, foliation, and normalizer proofs above.

- Sophus Lie and Friedrich Engel, *Theorie der Transformationsgruppen*, Volume I (1888), the indicated chapters and theorem numbers.
- Joël Merker, [*Theory of Transformation Groups: Modern Presentation and English Translation*](https://arxiv.org/abs/1003.3202), the corresponding chapters.

Global homogeneous spaces $G/H$ require additional hypotheses on the global subgroup, and global discrete identifications can affect classification. Those questions are outside the local results proved here.

## Historical reading: transitivity and invariants

Sophus Lie and Friedrich Engel, *Theorie der Transformationsgruppen*, Volume I (1888), Chapter 13 introduction and complete §58, printed pp. 211–218. [German original](https://archive.org/details/theotransformation01liesrich).

The German original is in the public domain. The transcription and independently written English translation are dedicated to CC0.

### German text: transitivity and invariants

**Kapitel 13. Transitivität, Invarianten, Primitivität.**

Die Begriffe Transitivität und Primitivität, welche in der Substitutionentheorie eine so grosse Rolle spielen, sollen hier auf endliche continuirliche Transformationsgruppen ausgedehnt werden. Im Vorbeigehen sei erwähnt, dass sich diese Begriffe überhaupt auf alle Gruppen ausdehnen lassen, auf die endlichen sowohl als auf die unendlichen, auf die continuirlichen so gut wie auf die nichtcontinuirlichen.\*)

**§58.**

Eine endliche continuirliche Gruppe in den Veränderlichen $x_1\cdots x_n$ heisst *transitiv*, wenn es im Raume $(x_1\cdots x_n)$ ein $n$-fach ausgedehntes Gebiet giebt, innerhalb dessen jeder Punkt durch mindestens eine Transformation der Gruppe in jeden beliebigen andern übergeführt werden kann. Jede Gruppe, welche nicht transitiv ist, heisst *intransitiv*.

Nach dieser Definition ist also eine $r$-gliedrige Gruppe:

$$
x_i'=f_i(x_1\cdots x_n,a_1\cdots a_r)\qquad(i=1\cdots n)
$$

transitiv, wenn man im Allgemeinen zu jedem Werthsysteme $x_1\cdots x_n$, $x_1'\cdots x_n'$ wenigstens ein solches Werthsystem $a_1\cdots a_r$ angeben kann, dass die Gleichungen $x_i'=f_i(x,a)$ durch die betreffenden Werthe der $x$, $a$, $x'$ befriedigt werden. Mit andern Worten: *Die Gleichungen $x_i'=f_i(x,a)$ einer transitiven Gruppe lassen sich nach $n$ von den $r$ Parametern $a_1\cdots a_r$ auflösen. Ist dagegen eine solche Auflösung nicht möglich, lassen sich vielmehr aus den Gleichungen $x_i'=f_i(x,a)$ der Gruppe Relationen herleiten, welche von den Parametern $a$ frei sind und nur die Veränderlichen $x_1\cdots x_n$, $x_1'\cdots x_n'$ enthalten, so ist die Gruppe nicht transitiv, sie ist intransitiv.*

Wir ersehen hieraus, dass jede transitive Gruppe des Raumes $x_1\cdots x_n$ mindestens $n$ wesentliche Parameter enthält.

Hat eine *transitive* Gruppe in $n$ Veränderlichen gerade $n$ wesentliche Parameter, so enthält sie im Allgemeinen eine, aber auch nur eine Transformation, welche einen beliebigen Punkt des Raumes in einen andern beliebigen Punkt überführt; insbesondere enthält sie daher ausser der identischen Transformation keine Transformation, welche einen Punkt von allgemeiner Lage invariant lässt. Wir bezeichnen jede Gruppe von dieser Beschaffenheit als *einfach transitiv*.

Das oben gegebene allgemeine Kriterium für die Transitivität bezüglich Intransitivität einer Gruppe ist nur dann praktisch anwendbar, wenn man die endlichen Gleichungen der Gruppe kennt. Sollte sich aber nicht ein Kriterium angeben lassen, zu dessen Anwendung blos die Kenntniss der infinitesimalen Transformationen der Gruppe erforderlich ist? Wir werden zeigen, dass sich in der That ein solches Kriterium angeben lässt. Zugleich werden wir Mittel finden, um zu erkennen, wie viele und welche Relationen zwischen den $x$ und den $x'$ allein bei einer intransitiven Gruppe mit bekannten infinitesimalen Transformationen auftreten.

Es seien $r$ unabhängige infinitesimale Transformationen

$$
X_kf=\sum_1^n{}^{i}\xi_{ki}(x_1\cdots x_n)\frac{\partial f}{\partial x_i}
\qquad(k=1\cdots r)
$$

vorgelegt, die eine $r$-gliedrige Gruppe erzeugen. Diese Gruppe, deren endliche Gleichungen wir uns in der Form

$$
\begin{gathered}
\Phi_i=-x_i'+x_i+\sum_1^r{}^{k}e_k\cdot\xi_{ki}(x)+\cdots=0
\\
(i=1\cdots n)
\end{gathered}
$$

geschrieben denken können, ist nach dem Früheren dann und nur dann transitiv, wenn die $n$ Gleichungen $\Phi_1=0$, $\cdots$, $\Phi_n=0$ nach $n$ von den $r$ Parametern $e_1\cdots e_r$ auflösbar sind. Nothwendig und hinreichend für die Transitivität unserer Gruppe ist demnach, dass nicht alle $n$-reihigen Determinanten der Matrix

$$
\left|\begin{array}{cccc}
\dfrac{\partial\Phi_1}{\partial e_1}&\cdot&\cdot&\dfrac{\partial\Phi_n}{\partial e_1}\\
\cdot&\cdot&\cdot&\cdot\\
\dfrac{\partial\Phi_1}{\partial e_r}&\cdot&\cdot&\dfrac{\partial\Phi_n}{\partial e_r}
\end{array}\right|\tag{1}
$$

identisch verschwinden.

Hieraus folgt, dass die Gruppe sicher transitiv ist, wenn die betreffenden Determinanten für $e_1=0$, $\cdots$, $e_r=0$ nicht sämmtlich verschwinden, wenn also nicht alle $n$-reihigen Determinanten der Matrix

$$
\left|\begin{array}{ccccc}
\xi_{11}&\cdot&\cdot&\cdot&\xi_{1n}\\
\cdot&\cdot&\cdot&\cdot&\cdot\\
\xi_{r1}&\cdot&\cdot&\cdot&\xi_{rn}
\end{array}\right|\tag{2}
$$

identisch null sind.

Damit haben wir eine hinreichende Bedingung für die Transitivität unserer Gruppe gefunden. Wir wollen jetzt untersuchen, was eintritt, wenn diese Bedingung nicht erfüllt ist.

Es seien also alle $n$-reihigen Determinanten der eben geschriebenen Matrix (2) identisch null; um alle Möglichkeiten auf einmal zu umfassen, wollen wir ausserdem voraussetzen, dass zugleich auch alle $(n-1)$-, $(n-2)$-, $\cdots$ $(q+1)$-reihigen Determinanten der Matrix identisch verschwinden, während nicht alle $q$-reihigen dies thun.

Unter diesen Umständen verschwinden sicher nicht alle $q$-reihigen Determinanten der Matrix (1), also können wir schliessen, dass sich aus den $n$ Gleichungen $\Phi_1=0$, $\cdots$, $\Phi_n=0$ höchstens $n-q$ von $e_1\cdots e_r$ freie und unter einander unabhängige Gleichungen zwischen den $x$ und $x'$ allein herleiten lassen.

Nun aber reduciren sich unter den gemachten Voraussetzungen die $r$ Gleichungen $X_1f=0$, $\cdots$, $X_rf=0$ auf gerade $q<n$ unabhängige, etwa auf: $X_1f=0$, $\cdots$, $X_qf=0$, während $X_{q+1}f\cdots X_rf$ sich folgendermassen ausdrücken:

$$
\begin{gathered}
X_{q+\nu}f=\varphi_{\nu1}(x)\cdot X_1f+\cdots+\varphi_{\nu q}(x)\cdot X_qf
\\
(\nu=1\cdots r-q).
\end{gathered}
$$

Mithin wird:

$$
(X_iX_k)=\sum_1^q{}^{j}\left(c_{ikj}+\sum_1^{r-q}{}^{\nu}c_{ik,q+\nu}\varphi_{\nu j}\right)X_jf
$$

für alle Werthe von $i$ und $k$, das heisst: die $q$ Gleichungen $X_1f=0$, $\cdots$, $X_qf=0$ bilden ein $q$-gliedriges vollständiges System mit $n-q$ unabhängigen Lösungen, welche $\Omega_1(x)\cdots\Omega_{n-q}(x)$ heissen mögen.

Diese Lösungen gestatten eine jede infinitesimale Transformation von der Form $e_1\cdot X_1f+\cdots+e_r\cdot X_rf$, also jede infinitesimale und in Folge dessen auch jede endliche Transformation unserer $r$-gliedrigen Gruppe $X_1f\cdots X_rf$ (vgl. Kap. 6, S. 98). Analytisch drückt sich das dadurch aus, dass zwischen den Veränderlichen $x$ und $x'$, welche in den Transformationsgleichungen unserer Gruppe vorkommen, die folgenden $n-q$ unabhängigen, von den $e$ freien Relationen bestehen:

$$
\begin{gathered}
\Omega_1(x_1'\cdots x_n')=\Omega_1(x_1\cdots x_n),\\
\cdots,\\

\Omega_{n-q}(x_1'\cdots x_n')=\Omega_{n-q}(x_1\cdots x_n).
\end{gathered}
$$

Oben sahen wir, dass zwischen den $x$ und den $x'$ allein höchstens $n-q$ unabhängige Relationen bestehen können, wir haben demnach hiermit die betreffenden Relationen alle gefunden.

Insbesondere erkennen wir, dass die Gruppe $X_1f\cdots X_rf$ intransitiv ist, sobald alle $n$-reihigen Determinanten der Matrix (2) identisch verschwinden. Damit ist zugleich bewiesen, dass die vorhin gefundene hinreichende Bedingung für die Transitivität der Gruppe $X_1f\cdots X_rf$ nicht blos hinreichend, sondern auch nothwendig ist.

Wir formuliren die gewonnenen Ergebnisse in Sätzen. An die Spitze stellen wir das

**Theorem 34.** *Die $r$-gliedrige Gruppe $X_1f\cdots X_rf$ des Raumes $x_1\cdots x_n$ ist transitiv, wenn sich unter den $r$ Gleichungen $X_1f=0$, $\cdots$, $X_rf=0$ gerade $n$ von einander unabhängige befinden, im entgegengesetzten Falle ist sie intransitiv.*

Sodann mag ein Satz folgen:

**Satz 1.** *Aus den endlichen Gleichungen*

$$
x_i'=f_i(x_1\cdots x_n,a_1\cdots a_r)\qquad(i=1\cdots n)
$$

*einer $r$-gliedrigen Gruppe mit den infinitesimalen Transformationen $X_1f\cdots X_rf$ kann man nur dann alle $r$ Parameter $a_1\cdots a_r$ eliminiren, wenn die Gruppe intransitiv ist; man erhält in diesem Falle zwischen den $x$ und den $x'$ eine gewisse Anzahl von Relationen, welche sich auf die Form bringen lassen:*

$$
\begin{gathered}
\Omega_k(x_1'\cdots x_n')=\Omega_k(x_1\cdots x_n)\\
(k=1,2\cdots);
\end{gathered}
$$

*dabei sind $\Omega_1(x)$, $\Omega_2(x)\cdots$ ein System unabhängiger Lösungen des vollständigen Systems, welches durch die $r$ Gleichungen $X_1f=0$, $\cdots$, $X_rf=0$ bestimmt ist.*

In Kapitel 6, S. 97 sahen wir, dass die Lösungen der linearen partiellen Differentialgleichung $Xf=0$ die einzigen Invarianten der eingliedrigen Gruppe $Xf$ sind; dementsprechend sind die gemeinsamen Lösungen der Gleichungen $X_1f=0$, $\cdots$, $X_rf=0$ die einzigen Invarianten der Gruppe $X_1f\cdots X_rf$. Wir können daher den Satz aussprechen:

**Satz 2.** *Ist die $r$-gliedrige Gruppe $X_1f\cdots X_rf$ des Raumes $x_1\cdots x_n$ transitiv, so hat sie keine Invarianten, ist sie intransitiv, so sind die gemeinsamen Lösungen der Gleichungen $X_1f=0$, $\cdots$, $X_rf=0$ ihre einzigen Invarianten.*

Schliesslich mag noch der folgende Satz angeführt werden, der eine charakteristische Eigenschaft der Invarianten endlicher *continuirlicher* Gruppen ausspricht:

**Satz 3.** *Sind $u_1\cdots u_q$ Invarianten der $r$-gliedrigen Gruppe $X_1f\cdots X_rf$, so ist auch jede Function von $u_1\cdots u_q$ eine Invariante dieser Gruppe.*

Um den begrifflichen Sinn der gewonnenen analytischen Resultate klarzustellen, wollen wir nunmehr $x_1\cdots x_n$ als Punktcoordinaten eines Raumes von $n$ Dimensionen deuten.

Das in dem Theorem erwähnte vollständige System sei $q$-gliedrig und die Zahl $q$ sei kleiner als $n$, also die Gruppe $X_1f\cdots X_rf$ intransitiv. Die Functionen $\Omega_1(x_1\cdots x_n)\cdots\Omega_{n-q}(x_1\cdots x_n)$ seien unabhängige Lösungen dieses betreffenden vollständigen Systems, mit $C_1\cdots C_{n-q}$ endlich mögen willkürliche Constanten bezeichnet werden. *Dann zerlegen die Gleichungen*

$$
\Omega_1=C_1,\quad\cdots,\quad\Omega_{n-q}=C_{n-q}
$$

*den ganzen Raum in $\infty^{n-q}$ verschiedene $q$-fach ausgedehnte Theilgebiete, welche sämmtlich bei der Gruppe $X_1f\cdots X_rf$ invariant bleiben.* Jeder Punkt des Raumes gehört einem ganz bestimmten Theilgebiet an und kann von Transformationen der Gruppe nur in Punkte desselben Theilgebietes übergeführt werden. Jedoch werden die Punkte eines Theilgebietes unter sich transitiv transformirt, das heisst, jeder Punkt von allgemeiner Lage in dem betreffenden Theilgebiete kann durch wenigstens eine Transformation der Gruppe in jeden andern solchen Punkt übergeführt werden.

Ist $x_1\cdots x_n$ ein Punkt von allgemeiner Lage, so bezeichnen wir die Functionen $\Omega_1(x)\cdots\Omega_{n-q}(x)$ auch als Invarianten des Punktes $x_1\cdots x_n$ gegenüber der Gruppe $X_1f\cdots X_rf$. Die Zahl dieser Invarianten giebt den Grad der Intransitivität unserer Gruppe an, denn je grösser die Zahl der Invarianten, um so kleiner die Dimensionenzahl des Theilgebietes, innerhalb dessen der Punkt $x_1\cdots x_n$ bei den Transformationen der Gruppe bleibt.

Einer transitiven Gruppe gegenüber hat ein Punkt von allgemeiner Lage offenbar keine Invariante.

Das oben ausgesprochene Theorem gestattet zu entscheiden, ob eine vorgelegte Gruppe $X_1f\cdots X_rf$ transitiv ist oder nicht. Dem darin enthaltenen Kriterium für die Transitivität oder Intransitivität einer Gruppe lassen sich nun verschiedene andere Fassungen geben.

Zunächst können wir mit einer leichten Aenderung der Ausdrucksweise sagen:

Eine $r$-gliedrige Gruppe $X_1f\cdots X_rf$ in $x_1\cdots x_n$ ist dann und nur dann transitiv, wenn es unter ihren infinitesimalen Transformationen gerade $n$ — etwa $X_1f\cdots X_nf$ — giebt, welche durch keine lineare Relation von der Form

$$
\begin{gathered}
\chi_1(x_1\cdots x_n)\cdot X_1f\\
+\cdots+\chi_n(x_1\cdots x_n)\cdot X_nf=0
\end{gathered}
$$

verknüpft sind, während sich $X_{n+1}f\cdots X_rf$ folgendermassen durch $X_1f\cdots X_nf$ ausdrücken:

$$
\begin{gathered}
X_{n+j}f=\varphi_{j1}(x)\cdot X_1f+\cdots+\varphi_{jn}(x)\cdot X_nf
\\
(j=1\cdots r-n).
\end{gathered}
$$

Giebt es keine $n$ infinitesimalen Transformationen von dieser Beschaffenheit, so ist die Gruppe intransitiv.

Erinnern wir uns jetzt, dass jede infinitesimale Transformation $X_kf$ jedem Punkte des Raumes $x_1\cdots x_n$ eine Richtung zuordnet und nehmen wir noch hinzu, was in Kap. 6, S. 102 über die Unabhängigkeit solcher Richtungen gesagt ist, welche durch denselben Punkt gehen; dann können wir das Kriterium für die Transitivität einer Gruppe auch folgendermassen aussprechen:

**Satz 4.** *Eine Gruppe $X_1f\cdots X_rf$ in den Veränderlichen $x_1\cdots x_n$ ist transitiv, wenn sie $n$ infinitesimale Transformationen enthält, welche jedem Punkte von allgemeiner Lage $n$ unabhängige Richtungen zuordnen; enthält die Gruppe keine $n$ infinitesimalen Transformationen von dieser Beschaffenheit, so ist sie intransitiv.*

Andererseits möge an die Auseinandersetzungen in Kap. 11, S. 203 erinnert werden, wo wir uns die infinitesimalen Transformationen der Gruppe in der Umgebung eines Punktes $x_i^0$ von allgemeiner Lage nach den Potenzen der $x_i-x_i^0$ entwickelt dachten. Da eine transitive Gruppe $X_1f\cdots X_rf$ in den Veränderlichen $x_1\cdots x_n$ $n$ infinitesimale Transformationen: $X_1f\cdots X_nf$ enthält, welche durch keine lineare Relation $\chi_1(x)\cdot X_1f+\cdots+\chi_n(x)\cdot X_nf=0$ verknüpft sind, erhalten wir den folgenden Satz:

**Satz 5.** *Eine $r$-gliedrige Gruppe $X_1f\cdots X_rf$ in den $n$ Veränderlichen $x_1\cdots x_n$ ist transitiv, wenn sie in der Umgebung eines Punktes $x_i^0$ von allgemeiner Lage gerade $n$ solche unabhängige infinitesimale Transformationen von nullter Ordnung in den $x_i-x_i^0$ enthält, aus denen sich keine infinitesimale Transformation von erster oder höherer Ordnung linear ableiten lässt. Ist die Anzahl solcher infinitesimaler Transformationen nullter Ordnung kleiner als $n$, so ist die Gruppe intransitiv.*

Man sieht hieraus, *dass man nur die Definitionsgleichungen der Gruppe $X_1f\cdots X_rf$ zu kennen braucht, um über die Transitivität oder Intransitivität derselben entscheiden zu können.*

Den ersten Theil des Satzes 5 können wir schliesslich auch folgendermassen aussprechen:

Die Gruppe $X_1f\cdots X_rf$ ist transitiv, wenn sie in der Umgebung eines Punktes $x_i^0$ von allgemeiner Lage gerade $r-n$ unabhängige infinitesimale Transformationen enthält, deren Reihenentwickelungen nach den $x_i-x_i^0$ mit Gliedern erster oder höherer Ordnung anfangen, wenn also die Gruppe gerade $r-n$ und nicht mehr unabhängige infinitesimale Transformationen enthält, welche einen Punkt von allgemeiner Lage invariant lassen. —

Sind von einer intransitiven Gruppe $X_1f\cdots X_rf$ nur die infinitesimalen Transformationen bekannt, so findet man, wie wir gesehen haben, die Invarianten der Gruppe durch Integration des vollständigen Systems $X_1f=0$, $\cdots$, $X_rf=0$. Es ist nun von grosser Wichtigkeit, dass diese Integration nicht erforderlich ist, wenn die endlichen Gleichungen der Gruppe bekannt sind, dass sich vielmehr in diesem Falle die Invarianten der Gruppe durch blose Elimination ergeben.

Um das nachzuweisen, denken wir uns die endlichen Gleichungen

$$
x_i'=f_i(x_1\cdots x_n,a_1\cdots a_r)\qquad(i=1\cdots n)
$$

einer intransitiven Gruppe vorgelegt und sodann die Parameter $a_1\cdots a_r$ daraus eliminirt. Die auf diese Weise erhaltenen $n-q$ unabhängigen Gleichungen

$$
\begin{gathered}
W_\mu(x_1\cdots x_n,x_1'\cdots x_n')=0\\
(\mu=1\cdots n-q)
\end{gathered}\tag{3}
$$

müssen sich nach dem Früheren auf die Form

$$
\begin{gathered}
\Omega_\mu(x_1'\cdots x_n')=\Omega_\mu(x_1\cdots x_n)\\
(\mu=1\cdots n-q)
\end{gathered}\tag{4}
$$

bringen lassen, wo die $\Omega_\mu(x)$ die gesuchten Invarianten sind. Wenn wir daher, was immer möglich ist, die Gleichungen (3) nach $n-q$ von den Veränderlichen $x_1'\cdots x_n'$ auflösen:

$$
\begin{gathered}
x_\mu'=\Pi_\mu(x_1\cdots x_n,x_{n-q+1}'\cdots x_n')\\
(\mu=1\cdots n-q),
\end{gathered}
$$

so erhalten wir $n-q$ Functionen $\Pi_1\cdots\Pi_{n-q}$, in welchen die Veränderlichen $x_1\cdots x_n$ nur in den Verbindungen $\Omega_1(x)\cdots\Omega_{n-q}(x)$ vorkommen. Folglich stellen die $n-q$ Ausdrücke

$$
\begin{gathered}
\Pi_\mu(x_1\cdots x_n,a_{n-q+1}\cdots a_n)\\
(\mu=1\cdots n-q),
\end{gathered}
$$

in denen $a_{n-q+1}\cdots a_n$ Constanten bezeichnen, Invarianten unserer Gruppe dar und zwar offenbar $n-q$ unabhängige Invarianten. —

Es gilt also das

**Theorem 35.** *Kennt man die endlichen Gleichungen:*

$$
x_i'=f_i(x_1\cdots x_n,a_1\cdots a_r)\qquad(i=1\cdots n)
$$

*einer intransitiven Gruppe, so kann man die Invarianten dieser Gruppe durch Elimination finden.*

### German original footnote for §58

**F1 · p. 212, after the chapter introduction.** Nachdem Lie 1869 einige Differentialgleichungen mit bekannter continuirlicher Gruppe integrirt hatte, stellte er 1871 und 1872 im Verein mit Klein die Aufgabe, die Begriffe der Substitutionentheorie soweit als möglich auf die Theorie der continuirlichen Transformationsgruppen zu übertragen. Die Erledigung dieses Problems im Einzelnen gab Lie; gestützt auf die hierdurch gewonnenen Vorstellungen und Begriffe entwickelte er bereits 1874 die Grundzüge einer allgemeinen Integrationstheorie solcher vollständiger Systeme, welche bekannte infinitesimale Transformationen gestatten ([Verh. d. G. d. W. zu Christiania, 1874](https://archive.org/details/forhandlingerivi1874chri)). Er führte dieses Problem auf den Fall zurück, dass die bekannten infinitesimalen Transformationen eine endliche continuirliche Gruppe erzeugen, welche imprimitiv ist, da ihre Transformationen die charakteristischen Mannigfaltigkeiten des vollständigen Systems unter einander vertauschen. Er gab u. A. alle Fälle an, in denen sich die Integration des vollständigen Systems durch Quadraturen erledigen lässt.

### English translation: transitivity and invariants

**Chapter 13. Transitivity, invariants, primitivity.**

The concepts of transitivity and primitivity, which play so great a role in the theory of substitutions, are to be extended here to finite continuous transformation groups. In passing, it may be mentioned that these concepts can be extended to all groups whatsoever: to finite as well as infinite groups, and to continuous as well as discontinuous ones.\*)

**§58.**

A finite continuous group in the variables $x_1\cdots x_n$ is called *transitive* if there is an $n$-dimensional region in the space $(x_1\cdots x_n)$ within which every point can be carried into any other point by at least one transformation of the group. Every group that is not transitive is called *intransitive*.

According to this definition, an $r$-parameter group

$$
x_i'=f_i(x_1\cdots x_n,a_1\cdots a_r)\qquad(i=1\cdots n)
$$

is therefore transitive if, in general, for every system of values $x_1\cdots x_n$, $x_1'\cdots x_n'$, one can specify at least one system of values $a_1\cdots a_r$ such that the equations $x_i'=f_i(x,a)$ are satisfied by the corresponding values of $x$, $a$, $x'$. In other words: *The equations $x_i'=f_i(x,a)$ of a transitive group can be solved for $n$ of the $r$ parameters $a_1\cdots a_r$. If, on the other hand, such a solution is impossible, and relations can instead be derived from the group equations $x_i'=f_i(x,a)$ that are free of the parameters $a$ and contain only the variables $x_1\cdots x_n$, $x_1'\cdots x_n'$, the group is not transitive: it is intransitive.*

We see from this that every transitive group of the space $x_1\cdots x_n$ contains at least $n$ essential parameters.

If a *transitive* group in $n$ variables has exactly $n$ essential parameters, it contains, in general, one and only one transformation carrying any point of the space into any other point. In particular, apart from the identity transformation, it therefore contains no transformation leaving a point in general position invariant. We call every group of this kind *simply transitive*.

The general criterion given above for the transitivity or intransitivity of a group is practically applicable only when the finite equations of the group are known. But should it not be possible to give a criterion whose application requires only knowledge of the group's infinitesimal transformations? We shall show that such a criterion can indeed be given. At the same time, we shall find means of recognizing how many and which relations between $x$ and $x'$ alone occur for an intransitive group with known infinitesimal transformations.

Suppose that $r$ independent infinitesimal transformations

$$
X_kf=\sum_1^n{}^{i}\xi_{ki}(x_1\cdots x_n)\frac{\partial f}{\partial x_i}
\qquad(k=1\cdots r)
$$

are given, generating an $r$-parameter group. We may imagine the finite equations of this group written in the form

$$
\begin{gathered}
\Phi_i=-x_i'+x_i+\sum_1^r{}^{k}e_k\cdot\xi_{ki}(x)+\cdots=0
\\
(i=1\cdots n)
\end{gathered}
$$

By what precedes, this group is transitive if and only if the $n$ equations $\Phi_1=0$, $\cdots$, $\Phi_n=0$ can be solved for $n$ of the $r$ parameters $e_1\cdots e_r$. Thus it is necessary and sufficient for the transitivity of our group that not all $n$-rowed determinants of the matrix

$$
\left|\begin{array}{cccc}
\dfrac{\partial\Phi_1}{\partial e_1}&\cdot&\cdot&\dfrac{\partial\Phi_n}{\partial e_1}\\
\cdot&\cdot&\cdot&\cdot\\
\dfrac{\partial\Phi_1}{\partial e_r}&\cdot&\cdot&\dfrac{\partial\Phi_n}{\partial e_r}
\end{array}\right|\tag{1}
$$

vanish identically.

It follows that the group is certainly transitive if the determinants in question do not all vanish for $e_1=0$, $\cdots$, $e_r=0$, and thus if not all $n$-rowed determinants of the matrix

$$
\left|\begin{array}{ccccc}
\xi_{11}&\cdot&\cdot&\cdot&\xi_{1n}\\
\cdot&\cdot&\cdot&\cdot&\cdot\\
\xi_{r1}&\cdot&\cdot&\cdot&\xi_{rn}
\end{array}\right|\tag{2}
$$

are identically zero.

We have thereby found a sufficient condition for the transitivity of our group. We shall now investigate what happens when this condition is not satisfied.

Suppose, then, that all $n$-rowed determinants of the matrix (2) just written are identically zero. To encompass all possibilities at once, we shall also assume that all $(n-1)$-, $(n-2)$-, $\cdots$ $(q+1)$-rowed determinants of the matrix vanish identically, whereas not all $q$-rowed determinants do so.

Under these circumstances, certainly not all $q$-rowed determinants of the matrix (1) vanish. We can therefore conclude that at most $n-q$ mutually independent equations between $x$ and $x'$ alone, free of $e_1\cdots e_r$, can be derived from the $n$ equations $\Phi_1=0$, $\cdots$, $\Phi_n=0$.

Under the assumptions made, however, the $r$ equations $X_1f=0$, $\cdots$, $X_rf=0$ reduce to exactly $q<n$ independent equations, say $X_1f=0$, $\cdots$, $X_qf=0$, while $X_{q+1}f\cdots X_rf$ can be expressed as follows:

$$
\begin{gathered}
X_{q+\nu}f=\varphi_{\nu1}(x)\cdot X_1f+\cdots+\varphi_{\nu q}(x)\cdot X_qf
\\
(\nu=1\cdots r-q).
\end{gathered}
$$

Consequently,

$$
(X_iX_k)=\sum_1^q{}^{j}\left(c_{ikj}+\sum_1^{r-q}{}^{\nu}c_{ik,q+\nu}\varphi_{\nu j}\right)X_jf
$$

for all values of $i$ and $k$. That is, the $q$ equations $X_1f=0$, $\cdots$, $X_qf=0$ form a $q$-term complete system with $n-q$ independent solutions, which we may call $\Omega_1(x)\cdots\Omega_{n-q}(x)$.

These solutions admit every infinitesimal transformation of the form $e_1\cdot X_1f+\cdots+e_r\cdot X_rf$, hence every infinitesimal transformation and consequently also every finite transformation of our $r$-parameter group $X_1f\cdots X_rf$ (compare Chapter 6, p. 98). Analytically, this is expressed by saying that the following $n-q$ independent relations, free of the $e$, hold between the variables $x$ and $x'$ occurring in the transformation equations of our group:

$$
\begin{gathered}
\Omega_1(x_1'\cdots x_n')=\Omega_1(x_1\cdots x_n),\\
\cdots,\\

\Omega_{n-q}(x_1'\cdots x_n')=\Omega_{n-q}(x_1\cdots x_n).
\end{gathered}
$$

We saw above that at most $n-q$ independent relations between $x$ and $x'$ alone can exist. Thus we have found all the relations in question.

In particular, we recognize that $X_1f\cdots X_rf$ is intransitive as soon as all $n$-rowed determinants of matrix (2) vanish identically. This also proves that the sufficient condition previously found for the transitivity of $X_1f\cdots X_rf$ is necessary as well as sufficient.

We formulate the results obtained as propositions. First we state

**Theorem 34.** *The $r$-parameter group $X_1f\cdots X_rf$ of the space $x_1\cdots x_n$ is transitive if exactly $n$ of the $r$ equations $X_1f=0$, $\cdots$, $X_rf=0$ are mutually independent; in the opposite case it is intransitive.*

A proposition may follow:

**Proposition 1.** *All $r$ parameters $a_1\cdots a_r$ can be eliminated from the finite equations*

$$
x_i'=f_i(x_1\cdots x_n,a_1\cdots a_r)\qquad(i=1\cdots n)
$$

*of an $r$-parameter group with infinitesimal transformations $X_1f\cdots X_rf$ only when the group is intransitive. In this case one obtains a certain number of relations between $x$ and $x'$ that can be put in the form*

$$
\begin{gathered}
\Omega_k(x_1'\cdots x_n')=\Omega_k(x_1\cdots x_n)\\
(k=1,2\cdots);
\end{gathered}
$$

*Here $\Omega_1(x)$, $\Omega_2(x)\cdots$ form a system of independent solutions of the complete system determined by the $r$ equations $X_1f=0$, $\cdots$, $X_rf=0$.*

In Chapter 6, p. 97, we saw that the solutions of the linear partial differential equation $Xf=0$ are the only invariants of the one-parameter group $Xf$. Correspondingly, the common solutions of the equations $X_1f=0$, $\cdots$, $X_rf=0$ are the only invariants of the group $X_1f\cdots X_rf$. We can therefore state the proposition:

**Proposition 2.** *If the $r$-parameter group $X_1f\cdots X_rf$ of the space $x_1\cdots x_n$ is transitive, it has no invariants. If it is intransitive, the common solutions of the equations $X_1f=0$, $\cdots$, $X_rf=0$ are its only invariants.*

Finally, we may add the following proposition, which expresses a characteristic property of the invariants of finite *continuous* groups:

**Proposition 3.** *If $u_1\cdots u_q$ are invariants of the $r$-parameter group $X_1f\cdots X_rf$, every function of $u_1\cdots u_q$ is also an invariant of this group.*

To clarify the conceptual meaning of the analytic results obtained, we shall now interpret $x_1\cdots x_n$ as the coordinates of a point in a space of $n$ dimensions.

Let the complete system mentioned in the theorem have $q$ terms, and let the number $q$ be smaller than $n$, so that $X_1f\cdots X_rf$ is intransitive. Let the functions $\Omega_1(x_1\cdots x_n)\cdots\Omega_{n-q}(x_1\cdots x_n)$ be independent solutions of this complete system, and let $C_1\cdots C_{n-q}$, finally, denote arbitrary constants. *Then the equations*

$$
\Omega_1=C_1,\quad\cdots,\quad\Omega_{n-q}=C_{n-q}
$$

*partition the entire space into $\infty^{n-q}$ distinct $q$-dimensional subregions, all of which remain invariant under $X_1f\cdots X_rf$.* Every point of the space belongs to one definite subregion, and transformations of the group can carry it only into points of that same subregion. The points of a subregion, however, are transformed transitively among themselves. That is, every point in general position in the subregion in question can be carried into every other such point by at least one transformation of the group.

If $x_1\cdots x_n$ is a point in general position, we also call the functions $\Omega_1(x)\cdots\Omega_{n-q}(x)$ invariants of the point $x_1\cdots x_n$ with respect to the group $X_1f\cdots X_rf$. The number of these invariants gives the degree of intransitivity of our group. For the larger the number of invariants, the smaller the dimension of the subregion within which the point $x_1\cdots x_n$ remains under the transformations of the group.

A point in general position plainly has no invariant with respect to a transitive group.

The theorem stated above permits us to decide whether a given group $X_1f\cdots X_rf$ is transitive or not. The criterion it contains for the transitivity or intransitivity of a group can now be given several other formulations.

First, with a slight change of expression, we can say:

An $r$-parameter group $X_1f\cdots X_rf$ in $x_1\cdots x_n$ is transitive if and only if among its infinitesimal transformations there are exactly $n$, say $X_1f\cdots X_nf$, that are linked by no linear relation of the form

$$
\begin{gathered}
\chi_1(x_1\cdots x_n)\cdot X_1f\\
+\cdots+\chi_n(x_1\cdots x_n)\cdot X_nf=0
\end{gathered}
$$

while $X_{n+1}f\cdots X_rf$ can be expressed in terms of $X_1f\cdots X_nf$ as follows:

$$
\begin{gathered}
X_{n+j}f=\varphi_{j1}(x)\cdot X_1f+\cdots+\varphi_{jn}(x)\cdot X_nf
\\
(j=1\cdots r-n).
\end{gathered}
$$

If there are no $n$ infinitesimal transformations of this kind, the group is intransitive.

Recall now that every infinitesimal transformation $X_kf$ assigns a direction to every point of the space $x_1\cdots x_n$. If we also take into account what was said in Chapter 6, p. 102, about the independence of such directions passing through the same point, we can state the criterion for the transitivity of a group in the following way:

**Proposition 4.** *A group $X_1f\cdots X_rf$ in the variables $x_1\cdots x_n$ is transitive if it contains $n$ infinitesimal transformations assigning $n$ independent directions to every point in general position. If the group contains no $n$ infinitesimal transformations of this kind, it is intransitive.*

On the other hand, recall the discussion in Chapter 11, p. 203, where we imagined the infinitesimal transformations of the group expanded in powers of $x_i-x_i^0$ in the neighbourhood of a point $x_i^0$ in general position. Since a transitive group $X_1f\cdots X_rf$ in the variables $x_1\cdots x_n$ contains $n$ infinitesimal transformations $X_1f\cdots X_nf$ that are linked by no linear relation $\chi_1(x)\cdot X_1f+\cdots+\chi_n(x)\cdot X_nf=0$, we obtain the following proposition:

**Proposition 5.** *An $r$-parameter group $X_1f\cdots X_rf$ in the $n$ variables $x_1\cdots x_n$ is transitive if, in the neighbourhood of a point $x_i^0$ in general position, it contains exactly $n$ such independent infinitesimal transformations of order zero in $x_i-x_i^0$ from which no infinitesimal transformation of first or higher order can be obtained as a linear combination. If the number of such infinitesimal transformations of order zero is smaller than $n$, the group is intransitive.*

We see from this *that one need only know the defining equations of the group $X_1f\cdots X_rf$ to decide whether it is transitive or intransitive.*

Finally, the first part of Proposition 5 can also be stated as follows:

The group $X_1f\cdots X_rf$ is transitive if, in the neighbourhood of a point $x_i^0$ in general position, it contains exactly $r-n$ independent infinitesimal transformations whose series expansions in $x_i-x_i^0$ begin with terms of first or higher order. Thus the group must contain exactly $r-n$, and no more, independent infinitesimal transformations leaving a point in general position invariant. —

If only the infinitesimal transformations of an intransitive group $X_1f\cdots X_rf$ are known, its invariants are found, as we have seen, by integrating the complete system $X_1f=0$, $\cdots$, $X_rf=0$. It is now of great importance that this integration is unnecessary when the finite equations of the group are known. In that case, the invariants of the group are obtained by mere elimination.

To prove this, imagine that the finite equations

$$
x_i'=f_i(x_1\cdots x_n,a_1\cdots a_r)\qquad(i=1\cdots n)
$$

of an intransitive group are given, and then eliminate the parameters $a_1\cdots a_r$ from them. By what precedes, the $n-q$ independent equations obtained in this way,

$$
\begin{gathered}
W_\mu(x_1\cdots x_n,x_1'\cdots x_n')=0\\
(\mu=1\cdots n-q)
\end{gathered}\tag{3}
$$

must be capable of being put in the form

$$
\begin{gathered}
\Omega_\mu(x_1'\cdots x_n')=\Omega_\mu(x_1\cdots x_n)\\
(\mu=1\cdots n-q)
\end{gathered}\tag{4}
$$

where the $\Omega_\mu(x)$ are the required invariants. If, therefore, we solve equations (3), which is always possible, for $n-q$ of the variables $x_1'\cdots x_n'$,

$$
\begin{gathered}
x_\mu'=\Pi_\mu(x_1\cdots x_n,x_{n-q+1}'\cdots x_n')\\
(\mu=1\cdots n-q),
\end{gathered}
$$

we obtain $n-q$ functions $\Pi_1\cdots\Pi_{n-q}$ in which the variables $x_1\cdots x_n$ occur only in the combinations $\Omega_1(x)\cdots\Omega_{n-q}(x)$. Consequently, the $n-q$ expressions

$$
\begin{gathered}
\Pi_\mu(x_1\cdots x_n,a_{n-q+1}\cdots a_n)\\
(\mu=1\cdots n-q),
\end{gathered}
$$

in which $a_{n-q+1}\cdots a_n$ denote constants, represent invariants of our group, and plainly $n-q$ independent invariants. —

Thus we have

**Theorem 35.** *If the finite equations*

$$
x_i'=f_i(x_1\cdots x_n,a_1\cdots a_r)\qquad(i=1\cdots n)
$$

*of an intransitive group are known, its invariants can be found by elimination.*

### English translation of the original footnote for §58

**F1 · p. 212, after the chapter introduction.** After Lie had integrated some differential equations with a known continuous group in 1869, he and Klein posed, in 1871 and 1872, the problem of transferring the concepts of the theory of substitutions as far as possible to the theory of continuous transformation groups. Lie supplied the detailed solution of this problem. Building on the ideas and concepts thereby obtained, he had already developed in 1874 the outlines of a general integration theory for complete systems admitting known infinitesimal transformations ([*Verh. d. G. d. W. zu Christiania*, 1874](https://archive.org/details/forhandlingerivi1874chri)). He reduced this problem to the case where the known infinitesimal transformations generate a finite continuous group that is imprimitive, since its transformations permute the characteristic manifolds of the complete system. Among other things, he gave all cases in which integration of the complete system can be accomplished by quadratures.

## Historical reading: systatic groups and primitivity

Sophus Lie and Friedrich Engel, *Theorie der Transformationsgruppen*, Volume I (1888), complete §126, printed pp. 518–522. [German original](https://archive.org/details/theotransformation01liesrich).

The German original is in the public domain. The transcription and independently written English translation are dedicated to CC0.

### German text: systatic groups and primitivity (§126)

**§126.**

Es sei $X_1f\cdots X_rf$ oder kurz $G_r$ eine $r$-gliedrige *systatische* Gruppe des Raumes $x_1\cdots x_s$ und $G_{r-n}$ sei diejenige $(r-n)$-gliedrige Untergruppe der $G_r$, welche einem bestimmten Punkte $x_1^0\cdots x_s^0$ von allgemeiner Lage zugeordnet ist. Die Mannigfaltigkeit:

$$
\begin{gathered}
\varphi_{k\nu}(x_1\cdots x_s)=\varphi_{k\nu}(x_1^0\cdots x_s^0)
\\
(k=1\cdots r-n;\ \nu=1\cdots n),
\end{gathered}
$$

welche aus allen bei der $G_{r-n}$ invarianten Punkten besteht, möge mit $M$ bezeichnet werden.

Da die $G_{r-n}$ alle Punkte von $M$ festhält, so lässt sie natürlich $M$ selbst invariant; es ist aber denkbar, dass die $G_r$ auch Transformationen enthält, welche die Mannigfaltigkeit $M$ invariant lassen, ohne alle ihre Punkte festzuhalten. Wir wollen annehmen, dass die grösste Untergruppe der $G_r$, welche $M$ invariant lässt, gerade $r-l$ Parameter enthält und wollen diese Untergruppe $G_{r-l}$ nennen.

Die $G_{r-n}$ ist selbstverständlich entweder mit der $G_{r-l}$ identisch oder in ihr als Untergruppe enthalten. Das letztere tritt immer ein, wenn die $G_r$ transitiv ist; in diesem Falle kann nämlich der Punkt $x_1^0\cdots x_s^0$ durch geeignete Transformationen der $G_r$ in alle Punkte von $M$ übergeführt werden, und da augenscheinlich jede Transformation der $G_r$, welche $x_1^0\cdots x_s^0$ in einen Punkt von $M$ überführt, die Mannigfaltigkeit $M$ invariant lässt, so enthält die $G_r$ eine continuirliche Schaar von Transformationen, welche $M$ invariant lassen, ohne alle Punkte von $M$ festzuhalten; also ist im Falle einer transitiven $G_r$ die Zahl $r-l$ sicher grösser als $r-n$. Ist aber die $G_r$ intransitiv, so ist es sehr gut möglich, dass alle Transformationen der $G_r$, welche $M$ invariant lassen, auch alle Punkte von $M$ festhalten, dass also $r-l=r-n$ ist. Das zeigt z. B. die dreigliedrige intransitive systatische Gruppe:

$$
\frac{\partial f}{\partial x_2},\quad x_2\frac{\partial f}{\partial x_2},\quad
x_2^2\frac{\partial f}{\partial x_2}
$$

der Ebene $x_1$, $x_2$.

Es ist leicht zu sehen, dass die $G_{r-n}$ in der $G_{r-l}$ invariant ist. In der That, die $G_{r-n}$ wird von allen infinitesimalen Transformationen der $G_{r-l}$ erzeugt, welche alle Punkte von $M$ stehen lassen; diese infinitesimalen Transformationen erzeugen aber nach Kap. 17, Satz 7, S. 309 eine invariante Untergruppe der $G_{r-n}$. Wir haben somit den

**Satz 8.** *Ist: $X_1f\cdots X_rf$ oder $G_r$ eine $r$-gliedrige systatische Gruppe des Raumes $x_1\cdots x_s$, ist ferner $P$ ein Punkt von allgemeiner Lage und endlich $M$ die Mannigfaltigkeit aller Punkte, welche bei allen Transformationen der $G_r$, die $P$ gestattet, invariant bleiben, so ist die grösste Untergruppe der $G_r$, welche $P$ invariant lässt, entweder identisch mit der grössten Untergruppe, welche $M$ in Ruhe lässt, oder in derselben als invariante Untergruppe enthalten. Der erste Fall kann nur eintreten, wenn die $G_r$ intransitiv ist; wenn die $G_r$ transitiv ist, tritt stets der zweite Fall ein.*

Kennt man andererseits irgend eine $r$-gliedrige Gruppe $G_r$ des Raumes $x_1\cdots x_s$ und weiss man, dass die grösste Untergruppe $G_{r-n}$ derselben, welche irgend einen Punkt $P$ von allgemeiner Lage invariant lässt, in einer noch grösseren Untergruppe $G_{r-h}$ mit $r-h>r-n$ Parametern invariant ist, so kann man schliessen, dass die $G_r$ in die Classe der systatischen Gruppen gehört.

In der That, der Punkt $P$ gestattet gerade $r-n$ unabhängige infinitesimale Transformationen der $G_{r-h}$ und nimmt also (Kap. 23, Theor. 85, S. 483) bei allen $\infty^{r-h}$ Transformationen der $G_{r-h}$ gerade $\infty^{n-h}$ verschiedene Lagen an, wo die Zahl $n-h$ unter der gemachten Voraussetzung mindestens gleich 1 ist. Da nun die $G_{r-n}$ in der $G_{r-h}$ invariant ist, so gehört zu jeder dieser $\infty^{n-h}$ Lagen von $P$ genau dieselbe $(r-n)$-gliedrige Untergruppe der $G_r$ wie zum Punkte $P$, das heisst, die $G_r$ ist wirklich systatisch. Also:

**Satz 9.** *Ist die $r$-gliedrige Gruppe $G_r$ des Raumes $x_1\cdots x_s$ so beschaffen, dass ihre grösste Untergruppe $G_{r-n}$, welche irgend einen Punkt von allgemeiner Lage invariant lässt, in einer noch grösseren Untergruppe der $G_r$ oder gar in der $G_r$ selbst invariant ist, so gehört die $G_r$ zu der Classe der systatischen Gruppen.*

Aus diesem Satze ergiebt sich sofort, dass bei einer $r$-gliedrigen asystatischen Gruppe des Raumes $x_1\cdots x_s$ die einem Punkte von allgemeiner Lage zugeordnete Untergruppe weder in der $G_r$ selbst invariant ist, noch in einer grösseren Untergruppe der $G_r$. Ist aber umgekehrt die $G_r$ so beschaffen, dass die einem Punkte von allgemeiner Lage zugeordnete Untergruppe in keiner grösseren Untergruppe invariant ist, so braucht sie deswegen noch nicht asystatisch zu sein, sie ist es nur dann nothwendig, wenn sie zugleich auch transitiv ist; das folgt offenbar aus dem Satze 8, S. 519. Wir können daher sagen:

**Satz 10.** *Eine $r$-gliedrige transitive Gruppe $G_r$ des Raumes $x_1\cdots x_s$ ist dann und nur dann asystatisch, wenn die einem Punkte von allgemeiner Lage zugeordnete Untergruppe in keiner grösseren Untergruppe invariant ist.*

In Kapitel 22, Theorem 79, S. 443 gaben wir eine Methode zur Bestimmung aller *transitiven* Gruppen, welche mit einer vorgelegten $r$-gliedrigen Gruppe $\Gamma$ gleichzusammengesetzt sind. Wir können nunmehr diese Methode so specialisiren, dass sie insbesondere alle *transitiven asystatischen* Gruppen liefert, welche mit der Gruppe $\Gamma$ gleichzusammengesetzt sind:

Man bestimme alle Untergruppen von $\Gamma$, welche weder eine in $\Gamma$ invariante Untergruppe enthalten, noch in einer grösseren Untergruppe von $\Gamma$ invariant sind. Jede dieser Untergruppen liefert, wenn nach den Regeln von Theor. 78 verfahren wird, eine transitive asystatische Gruppe, welche mit $\Gamma$ gleichzusammengesetzt ist, und zwar findet man auf diese Weise alle transitiven asystatischen Gruppen von der betreffenden Zusammensetzung.

Auf Grund des Satzes 10 lässt sich die Frage beantworten, ob eine vorgelegte transitive Gruppe systatisch ist oder asystatisch. Man kann einen ähnlichen Satz aufstellen, vermöge dessen sich die Frage beantworten lässt, *ob eine vorgelegte transitive Gruppe primitiv ist oder nicht*.

Die $r$-gliedrige *transitive* Gruppe $G_r$ des Raumes $x_1\cdots x_s$ sei imprimitiv und:

$$
\begin{gathered}
u_1(x_1\cdots x_s)=\mathrm{const.},\\
\cdots,\\

u_{s-m}(x_1\cdots x_s)=\mathrm{const.}\\
(0<m<s)
\end{gathered}
$$

sei eine bei der Gruppe invariante Zerlegung des Raumes in $\infty^{s-m}$ $m$-fach ausgedehnte Mannigfaltigkeiten.

Da die $G_r$ transitiv ist, so bilden alle ihre Transformationen, welche einen Punkt $x_1^0\cdots x_s^0$ von allgemeiner Lage invariant lassen, eine $(r-s)$-gliedrige Untergruppe $G_{r-s}$, andererseits bilden alle ihre Transformationen, welche die $m$-fach ausgedehnte Mannigfaltigkeit:

$$
\begin{gathered}
u_1(x_1\cdots x_s)=u_1(x^0),\\
\cdots,\\

u_{s-m}(x_1\cdots x_s)=u_{s-m}(x^0)
\end{gathered}
$$

invariant lassen, eine $(r-s+m)$-gliedrige Untergruppe $G_{r-s+m}$ (vgl. Kap. 23, S. 478 f.). Hierbei ist natürlich die $G_{r-s}$ als Untergruppe in der $G_{r-s+m}$ enthalten, welche ihrerseits offenbar eine wirkliche Untergruppe der $G_r$ ist.

Denken wir uns jetzt umgekehrt irgend eine $r$-gliedrige transitive Gruppe $\mathfrak G_r$ des Raumes $x_1\cdots x_s$ vorgelegt, und setzen wir voraus, dass die einem Punkte $P$ von allgemeiner Lage zugeordnete $(r-s)$-gliedrige Untergruppe $\mathfrak G_{r-s}$ der $\mathfrak G_r$ in einer grösseren Untergruppe:

$$
\mathfrak G_{r-s+h}\qquad(r-s<r-s+h<r)
$$

enthalten ist.

Werden auf $P$ alle Transformationen der $\mathfrak G_{r-s+h}$ ausgeführt, so nimmt der Punkt $\infty^h$ verschiedene Lagen an. Diese $\infty^h$ Lagen bilden eine $h$-fach ausgedehnte Mannigfaltigkeit $M$, welche bei der $\mathfrak G_{r-s+h}$ invariant bleibt (vgl. Kap. 23, S. 483). Führen wir endlich auf $M$ alle Transformationen der $\mathfrak G_r$ aus, so erhalten wir $\infty^{s-h}$ verschiedene $h$-fach ausgedehnte Mannigfaltigkeiten, welche eine Zerlegung des Raumes $x_1\cdots x_s$ bestimmen.

In der That, da die Mannigfaltigkeit $M$ bei der $\mathfrak G_{r-s+h}$ invariant bleibt, so nimmt sie bei den $\infty^r$ Transformationen der $\mathfrak G_r$ höchstens $\infty^{s-h}$ verschiedene Lagen an (vgl. Kap. 23, S. 483), sie nimmt andererseits wegen der Transitivität der $\mathfrak G_r$ mindestens $\infty^{s-h}$ Lagen an, also erhält sie bei der $\mathfrak G_r$ genau $\infty^{s-h}$ verschiedene Lagen, die den Raum gerade ausfüllen und daher eine Zerlegung bestimmen. Dass diese Zerlegung bei der $\mathfrak G_r$ invariant bleibt, folgt aus Theorem 85, S. 483.

Hieraus ergiebt sich, dass die $\mathfrak G_r$ unter den gemachten Voraussetzungen imprimitiv ist. Verbinden wir dieses Resultat mit dem oben gewonnenen, so erhalten wir zunächst das:

**Theorem 91.** *Eine $r$-gliedrige transitive Gruppe $G_r$ des Raumes $x_1\cdots x_s$ ist dann und nur dann primitiv, wenn die $(r-s)$-gliedrige Untergruppe $G_{r-s}$, welche irgend einem Punkte von allgemeiner Lage zugeordnet ist, in keiner grösseren Untergruppe der $G_r$ enthalten ist.*

Aber noch mehr, wir erhalten offenbar zugleich eine Methode, um alle etwaigen Zerlegungen des Raumes $x_1\cdots x_s$ zu bestimmen, welche bei einer vorgelegten transitiven Gruppe dieses Raumes invariant bleiben:

**Theorem 92.** *Ist eine $r$-gliedrige transitive Gruppe $G_r$ des Raumes $x_1\cdots x_s$ vorgelegt, so findet man alle etwaigen bei dieser Gruppe invarianten Zerlegungen des Raumes folgendermassen:*

*Man bestimme zunächst die $(r-s)$-gliedrige Untergruppe $G_{r-s}$ der $G_r$, bei welcher irgend ein Punkt $P$ invariant bleibt, der auf keiner bei der $G_r$ invarianten Mannigfaltigkeit liegt. Sodann suche man alle Untergruppen der $G_r$ auf, welche die $G_{r-s}$ enthalten. Ist $G_{r-s+h}$ eine von diesen Untergruppen, so führe man auf $P$ alle Transformationen der $G_{r-s+h}$ aus; dabei nimmt der Punkt $P$ $\infty^h$ verschiedene Lagen an, die eine $h$-fach ausgedehnte Mannigfaltigkeit $M$ bilden; führt man nunmehr auf $M$ alle Transformationen der $G_r$ aus, so nimmt $M$ $\infty^{s-h}$ verschiedene Lagen an, die eine bei der $G_r$ invariante Zerlegung des Raumes bestimmen. Behandelt man in dieser Weise alle Untergruppen der $G_r$, welche die $G_{r-s}$ umfassen, so erhält man alle bei der $G_r$ invarianten Zerlegungen.*

Wir können jetzt auch angeben, wie man die in Kap. 22, Theorem 79 auseinandergesetzte Methode zu specialisiren hat, um alle *primitiven* Gruppen zu finden, welche mit einer vorgelegten $r$-gliedrigen Gruppe $\Gamma$ gleichzusammengesetzt sind.

Da alle primitiven Gruppen transitiv sind, so hat man folgendermassen zu verfahren:

Man bestimme alle Untergruppen von $\Gamma$, welche keine in $\Gamma$ invariante Untergruppe enthalten und welche in keiner grösseren Untergruppe von $\Gamma$ enthalten sind. Jede dieser Untergruppen liefert, wenn nach den Regeln von Theorem 78 verfahren wird, eine primitive mit $\Gamma$ gleichzusammengesetzte Gruppe und zwar findet man auf diese Weise alle derartigen primitiven Gruppen. —

Das Theorem 92 zeigt, dass man alle bei einer *transitiven* Gruppe invarianten Zerlegungen ohne Integration finden kann, wenn die endlichen Gleichungen der Gruppe bekannt sind. Dasselbe gilt nun auch für intransitive Gruppen, doch bedarf man, um das einzusehen, ziemlich langer Ueberlegungen, welche hier auseinanderzusetzen nicht zweckmässig sein dürfte.

### English translation: systatic groups and primitivity (§126)

**§126.**

Let $X_1f\cdots X_rf$, or briefly $G_r$, be an $r$-parameter *systatic* group of the space $x_1\cdots x_s$, and let $G_{r-n}$ be the $(r-n)$-parameter subgroup of $G_r$ associated with a particular point $x_1^0\cdots x_s^0$ in general position. Let the manifold

$$
\begin{gathered}
\varphi_{k\nu}(x_1\cdots x_s)=\varphi_{k\nu}(x_1^0\cdots x_s^0)
\\
(k=1\cdots r-n;\ \nu=1\cdots n),
\end{gathered}
$$

consisting of all points invariant under $G_{r-n}$ be denoted by $M$.

Since $G_{r-n}$ fixes all points of $M$, it naturally leaves $M$ itself invariant. It is conceivable, however, that $G_r$ also contains transformations leaving the manifold $M$ invariant without fixing all its points. Suppose that the largest subgroup of $G_r$ leaving $M$ invariant contains exactly $r-l$ parameters, and call this subgroup $G_{r-l}$.

The group $G_{r-n}$ is of course either identical with $G_{r-l}$ or contained in it as a subgroup. The latter case always occurs when $G_r$ is transitive. In this case the point $x_1^0\cdots x_s^0$ can be carried into all points of $M$ by suitable transformations of $G_r$. Since plainly every transformation of $G_r$ carrying $x_1^0\cdots x_s^0$ into a point of $M$ leaves the manifold $M$ invariant, $G_r$ contains a continuous family of transformations leaving $M$ invariant without fixing all points of $M$. Thus, in the case of a transitive $G_r$, the number $r-l$ is certainly greater than $r-n$. If, however, $G_r$ is intransitive, it is quite possible that all transformations of $G_r$ leaving $M$ invariant also fix all points of $M$, so that $r-l=r-n$. This is shown, for example, by the three-parameter intransitive systatic group

$$
\frac{\partial f}{\partial x_2},\quad x_2\frac{\partial f}{\partial x_2},\quad
x_2^2\frac{\partial f}{\partial x_2}
$$

of the plane $x_1$, $x_2$.

It is easy to see that $G_{r-n}$ is invariant in $G_{r-l}$. Indeed, $G_{r-n}$ is generated by all infinitesimal transformations of $G_{r-l}$ leaving all points of $M$ fixed. By Chapter 17, Proposition 7, p. 309, however, these infinitesimal transformations generate an invariant subgroup of $G_{r-n}$. We have therefore obtained

**Proposition 8.** *Let $X_1f\cdots X_rf$, or $G_r$, be an $r$-parameter systatic group of the space $x_1\cdots x_s$. Let $P$ be a point in general position, and finally let $M$ be the manifold of all points remaining invariant under all transformations of $G_r$ admitted by $P$. Then the largest subgroup of $G_r$ leaving $P$ invariant is either identical with the largest subgroup leaving $M$ at rest, or contained in it as an invariant subgroup. The first case can occur only when $G_r$ is intransitive; when $G_r$ is transitive, the second case always occurs.*

Suppose, on the other hand, that an $r$-parameter group $G_r$ of the space $x_1\cdots x_s$ is known, and that its largest subgroup $G_{r-n}$ leaving some point $P$ in general position invariant is known to be invariant in a still larger subgroup $G_{r-h}$ with $r-h>r-n$ parameters. We can then conclude that $G_r$ belongs to the class of systatic groups.

Indeed, the point $P$ admits exactly $r-n$ independent infinitesimal transformations of $G_{r-h}$. Hence, under all $\infty^{r-h}$ transformations of $G_{r-h}$, it occupies exactly $\infty^{n-h}$ distinct positions (Chapter 23, Theorem 85, p. 483), where the number $n-h$ is at least 1 under our assumption. Since $G_{r-n}$ is invariant in $G_{r-h}$, precisely the same $(r-n)$-parameter subgroup of $G_r$ is associated with each of these $\infty^{n-h}$ positions of $P$ as with the point $P$. That is, $G_r$ is indeed systatic. Thus:

**Proposition 9.** *If the $r$-parameter group $G_r$ of the space $x_1\cdots x_s$ is such that its largest subgroup $G_{r-n}$ leaving some point in general position invariant is invariant in a still larger subgroup of $G_r$, or even in $G_r$ itself, then $G_r$ belongs to the class of systatic groups.*

This proposition immediately implies that, for an $r$-parameter asystatic group of the space $x_1\cdots x_s$, the subgroup associated with a point in general position is invariant neither in $G_r$ itself nor in any larger subgroup of $G_r$. Conversely, however, if $G_r$ is such that the subgroup associated with a point in general position is invariant in no larger subgroup, it need not therefore be asystatic. That conclusion is forced only when it is also transitive; this follows plainly from Proposition 8, p. 519. We can therefore say:

**Proposition 10.** *An $r$-parameter transitive group $G_r$ of the space $x_1\cdots x_s$ is asystatic if and only if the subgroup associated with a point in general position is invariant in no larger subgroup.*

In Chapter 22, Theorem 79, p. 443, we gave a method for determining all *transitive* groups having the same composition as a given $r$-parameter group $\Gamma$. We can now specialize this method so that, in particular, it supplies all *transitive asystatic* groups having the same composition as the group $\Gamma$:

Determine all subgroups of $\Gamma$ that neither contain an invariant subgroup of $\Gamma$ nor are invariant in a larger subgroup of $\Gamma$. When one proceeds according to the rules of Theorem 78, each of these subgroups supplies a transitive asystatic group having the same composition as $\Gamma$. In this way one finds all transitive asystatic groups of the composition in question.

On the basis of Proposition 10, we can decide whether a given transitive group is systatic or asystatic. A similar proposition can be established that permits us to decide *whether a given transitive group is primitive or not*.

Let the $r$-parameter *transitive* group $G_r$ of the space $x_1\cdots x_s$ be imprimitive, and let

$$
\begin{gathered}
u_1(x_1\cdots x_s)=\mathrm{const.},\\
\cdots,\\

u_{s-m}(x_1\cdots x_s)=\mathrm{const.}\\
(0<m<s)
\end{gathered}
$$

be a decomposition of the space into $\infty^{s-m}$ $m$-dimensional manifolds invariant under the group.

Since $G_r$ is transitive, all its transformations leaving a point $x_1^0\cdots x_s^0$ in general position invariant form an $(r-s)$-parameter subgroup $G_{r-s}$. On the other hand, all its transformations leaving the $m$-dimensional manifold

$$
\begin{gathered}
u_1(x_1\cdots x_s)=u_1(x^0),\\
\cdots,\\

u_{s-m}(x_1\cdots x_s)=u_{s-m}(x^0)
\end{gathered}
$$

invariant form an $(r-s+m)$-parameter subgroup $G_{r-s+m}$ (compare Chapter 23, pp. 478 f.). Here $G_{r-s}$ is naturally contained as a subgroup in $G_{r-s+m}$, which in turn is plainly a proper subgroup of $G_r$.

Conversely, imagine now that some $r$-parameter transitive group $\mathfrak G_r$ of the space $x_1\cdots x_s$ is given. Suppose that the $(r-s)$-parameter subgroup $\mathfrak G_{r-s}$ of $\mathfrak G_r$ associated with a point $P$ in general position is contained in a larger subgroup

$$
\mathfrak G_{r-s+h}\qquad(r-s<r-s+h<r)
$$

Applying all transformations of $\mathfrak G_{r-s+h}$ to $P$, the point occupies $\infty^h$ distinct positions. These $\infty^h$ positions form an $h$-dimensional manifold $M$, which remains invariant under $\mathfrak G_{r-s+h}$ (compare Chapter 23, p. 483). Finally, applying all transformations of $\mathfrak G_r$ to $M$, we obtain $\infty^{s-h}$ distinct $h$-dimensional manifolds determining a decomposition of the space $x_1\cdots x_s$.

Indeed, since the manifold $M$ remains invariant under $\mathfrak G_{r-s+h}$, it occupies at most $\infty^{s-h}$ distinct positions under the $\infty^r$ transformations of $\mathfrak G_r$ (compare Chapter 23, p. 483). On the other hand, owing to the transitivity of $\mathfrak G_r$, it occupies at least $\infty^{s-h}$ positions. Thus, under $\mathfrak G_r$, it occupies exactly $\infty^{s-h}$ distinct positions, which precisely fill the space and therefore determine a decomposition. That this decomposition remains invariant under $\mathfrak G_r$ follows from Theorem 85, p. 483.

It follows that $\mathfrak G_r$ is imprimitive under the assumptions made. Combining this result with the one obtained above, we first obtain:

**Theorem 91.** *An $r$-parameter transitive group $G_r$ of the space $x_1\cdots x_s$ is primitive if and only if the $(r-s)$-parameter subgroup $G_{r-s}$ associated with any point in general position is contained in no larger subgroup of $G_r$.*

More than this, we plainly obtain at the same time a method for determining all possible decompositions of the space $x_1\cdots x_s$ that remain invariant under a given transitive group of this space:

**Theorem 92.** *If an $r$-parameter transitive group $G_r$ of the space $x_1\cdots x_s$ is given, all possible decompositions of the space invariant under this group are found as follows:*

*First determine the $(r-s)$-parameter subgroup $G_{r-s}$ of $G_r$ under which some point $P$ remains invariant that lies on no manifold invariant under $G_r$. Then find all subgroups of $G_r$ containing $G_{r-s}$. If $G_{r-s+h}$ is one of these subgroups, apply all transformations of $G_{r-s+h}$ to $P$. The point $P$ thereby occupies $\infty^h$ distinct positions, forming an $h$-dimensional manifold $M$. If all transformations of $G_r$ are now applied to $M$, then $M$ occupies $\infty^{s-h}$ distinct positions determining a decomposition of the space invariant under $G_r$. Treating in this way all subgroups of $G_r$ containing $G_{r-s}$ gives all decompositions invariant under $G_r$.*

We can now also say how to specialize the method set out in Chapter 22, Theorem 79, in order to find all *primitive* groups having the same composition as a given $r$-parameter group $\Gamma$.

Since all primitive groups are transitive, one must proceed as follows:

Determine all subgroups of $\Gamma$ that contain no invariant subgroup of $\Gamma$ and are contained in no larger subgroup of $\Gamma$. Each of these subgroups, when one proceeds according to the rules of Theorem 78, supplies a primitive group having the same composition as $\Gamma$. In this way one finds all such primitive groups. —

Theorem 92 shows that all decompositions invariant under a *transitive* group can be found without integration when the finite equations of the group are known. The same holds for intransitive groups, but seeing this requires rather lengthy considerations that it would not be expedient to set out here.

## Historical reading: similarity of transitive groups

Sophus Lie and Friedrich Engel, *Theorie der Transformationsgruppen*, Volume I (1888), complete §104, printed pp. 424–428. [German original](https://archive.org/details/theotransformation01liesrich).

The German original is in the public domain. The transcription and independently written English translation are dedicated to CC0.

The modern local similarity criterion and its proof are given in [Theorem 3.1](#3-reconstructing-every-transitive-action).

### German text: similarity of transitive groups (§104)

**§104.**

In Kap. 19, Satz 3, S. 359, gaben wir den Kriterien für die Aehnlichkeit gleichzusammengesetzter Gruppen eine bemerkenswerthe Form; wir zeigten nämlich, dass zwei gleichzusammengesetzte Gruppen in gleichvielen Veränderlichen dann und nur dann mit einander ähnlich sind, wenn sie sich in einer gewissen, ganz besonderen Weise holoedrisch isomorph auf einander beziehen lassen.

Schon damals kündigten wir an, dass sich das betreffende Kriterium noch wesentlich vereinfachen lässt, sobald die beiden Gruppen, um welche es sich handelt, *transitiv* sind; wir kündigten an, dass das folgende Theorem gilt:

**Theorem 76.** *Zwei gleichzusammengesetzte transitive Gruppen:*

$$
X_kf=\sum_{1}^{n}{}_i\,\xi_{ki}(x_1\cdots x_n)\frac{\partial f}{\partial x_i}
\qquad(k=1\cdots r)
$$

*und:*

$$
Z_kf=\sum_{1}^{n}{}_i\,\zeta_{ki}(y_1\cdots y_n)\frac{\partial f}{\partial y_i}
\qquad(k=1\cdots r)
$$

*in gleichvielen Veränderlichen sind dann und nur dann mit einander ähnlich, wenn die folgende Bedingung erfüllt ist: Wählt man einen bestimmten Punkt: $x_1^0\cdots x_n^0$ aus, welcher auf keiner bei der Gruppe: $X_1f\cdots X_rf$ invarianten Mannigfaltigkeit liegt, so muss es möglich sein, die beiden Gruppen derart holoedrisch isomorph auf einander zu beziehen, dass der grössten in der Gruppe: $X_1f\cdots X_rf$ enthaltenen Untergruppe, welche den Punkt: $x_1^0\cdots x_n^0$ invariant lässt, die grösste Untergruppe der Gruppe: $Z_1f\cdots Z_rf$ entspricht, welche einen gewissen Punkt: $y_1^0\cdots y_n^0$ in Ruhe lässt.* [F1]

Aus Satz 3, S. 359 ist klar, dass diese Bedingung für die Aehnlichkeit der beiden Gruppen nothwendig ist; nachgewiesen zu werden braucht daher blos, dass sie auch hinreichend ist.

Denken wir uns also die Voraussetzungen des Theorems erfüllt, denken wir uns in der Gruppe: $Z_1f\cdots Z_rf$ solche unabhängige infinitesimale Transformationen: $Y_1f\cdots Y_rf$ ausgewählt, dass unsere beiden Gruppen in der im Theorem 76 beschriebenen Weise holoedrisch isomorph auf einander bezogen sind, wenn jeder infinitesimalen Transformation: $e_1X_1f+\cdots+e_rX_rf$ die infinitesimale Transformation: $e_1Y_1f+\cdots+e_rY_rf$ zugeordnet wird.

Nach den Entwickelungen des vorigen Paragraphen ist durch die betreffende holoedrisch isomorphe Beziehung auch zwischen den endlichen Transformationen beider Gruppen eine eindeutig umkehrbare Beziehung hergestellt. Wir können diese letztere am einfachsten beschreiben, wenn wir in der bekannten Weise $\sum e_kX_kf$ und $\sum e_kY_kf$ als Symbole der endlichen Transformationen unserer Gruppen auffassen und ausserdem zur grösseren Bequemlichkeit die endliche Transformation $\sum e_kX_kf$ kurz mit: $T_{(e)}$ bezeichnen, sowie die Transformation: $\sum e_kY_kf$ kurz mit: $\mathfrak{T}_{(e)}$.

Unter diesen Voraussetzungen ordnet nämlich die holoedrisch isomorphe Beziehung zwischen unsern beiden Gruppen der Transformation $T_{(e)}$ die Transformation $\mathfrak{T}_{(e)}$ zu und umgekehrt, und diese Zuordnung ist so beschaffen, dass auch die beiden Transformationen: $T_{(e)}T_{(e')}$ und $\mathfrak{T}_{(e)}\mathfrak{T}_{(e')}$ einander zugeordnet sind, wobei $e_1\cdots e_r$ und $e_1'\cdots e_r'$ ganz beliebige Werthsysteme bezeichnen.

Der Punkt: $x_1^0\cdots x_n^0$ bleibt bei gerade $r-n$ unabhängigen infinitesimalen Transformationen der Gruppe $X_1f\cdots X_rf$ invariant, folglich gestattet er gerade $\infty^{r-n}$ verschiedene endliche Transformationen dieser Gruppe, Transformationen, die bekanntlich eine $(r-n)$-gliedrige Untergruppe bilden. Wir wollen für die allgemeinste Transformation $T_{(e)}$, welche den Punkt: $x_1^0\cdots x_n^0$ in Ruhe lässt, das Symbol: $S_{(a_1\cdots a_{r-n})}$ oder kurz: $S_{(a)}$ einführen; unter $a_1\cdots a_{r-n}$ verstehen wir dabei willkürliche Parameter.

Diejenigen Transformationen $\mathfrak{T}_{(e)}$ der Gruppe: $Z_1f\cdots Z_rf$, welche den Transformationen $S_{(a)}$ der Gruppe: $X_1f\cdots X_rf$ zugeordnet sind, bezeichnen wir mit $\mathfrak{S}_{(a_1\cdots a_{r-n})}$ oder kurz mit $\mathfrak{S}_{(a)}$; unter den gemachten Voraussetzungen bilden dann die $\infty^{r-n}$ Transformationen $\mathfrak{S}_{(a)}$ die grösste in der Gruppe: $Z_1f\cdots Z_rf$ enthaltene Untergruppe, welche den Punkt: $y_1^0\cdots y_n^0$ invariant lässt. Hierin liegt, dass der Punkt: $y_1^0\cdots y_n^0$ keiner Mannigfaltigkeit angehört, welche bei der Gruppe: $Z_1f\cdots Z_rf$ invariant bleibt.

Nach diesen Vorbereitungen stellen wir die folgenden Ueberlegungen an.

Bei Ausführung der Transformation $T_{(e)}$ geht der Punkt $x_i^0$ in den Punkt: $(x_i^0)T_{(e)}$ über, dessen Lage natürlich von den Werthen der Parameter $e_1\cdots e_r$ abhängt. Dieser neue Punkt gestattet nach Kap. 14, Satz 1, S. 227 seinerseits gerade $\infty^{r-n}$ Transformationen der Gruppe: $X_1f\cdots X_rf$, nämlich alle Transformationen von der Form:

$$
T_{(e)}^{-1}S_{(a)}T_{(e)},
$$

mit den $r-n$ willkürlichen Parametern: $a_1\cdots a_{r-n}$.

Andererseits geht der Punkt $y_i^0$ bei der Transformation $\mathfrak{T}_{(e)}$ über in den Punkt: $(y_i^0)\mathfrak{T}_{(e)}$, der natürlich gerade $\infty^{r-n}$ Transformationen der Gruppe: $Z_1f\cdots Z_rf$ gestattet, nämlich alle Transformationen von der Form:

$$
\mathfrak{T}_{(e)}^{-1}\mathfrak{S}_{(a)}\mathfrak{T}_{(e)}.
$$

Das sind nun augenscheinlich diejenigen Transformationen der Gruppe: $Z_1f\cdots Z_rf$, welche den Transformationen: $T_{(e)}^{-1}S_{(a)}T_{(e)}$ der Gruppe: $X_1f\cdots X_rf$ zugeordnet sind; also sehen wir, dass bei unserer holoedrisch isomorphen Beziehung für die Punkte: $(x_i^0)T_{(e)}$ und $(y_i^0)\mathfrak{T}_{(e)}$ genau dasselbe gilt wie für die Punkte: $x_i^0$ und $y_i^0$; nämlich der grössten in der Gruppe $X_1f\cdots X_rf$ enthaltenen Untergruppe, welche den Punkt $(x_i^0)T_{(e)}$ invariant lässt, entspricht die grösste Untergruppe der Gruppe: $Z_1f\cdots Z_rf$, bei welcher der Punkt: $(y_i^0)\mathfrak{T}_{(e)}$ stehen bleibt.

Ertheilen wir jetzt den Parametern $e_1\cdots e_r$ in den Transformationen $T_{(e)}$ und $\mathfrak{T}_{(e)}$ nach und nach alle möglichen Werthe. Dann geht der Punkt: $(x_i^0)T_{(e)}$ wegen der Transitivität der Gruppe: $X_1f\cdots X_rf$ nach und nach in alle Punkte des Raumes $x_1\cdots x_n$ über, welche auf keiner invarianten Mannigfaltigkeit liegen, also in alle Punkte von allgemeiner Lage. Zugleich geht der Punkt: $(y_i^0)\mathfrak{T}_{(e)}$ in alle Punkte von allgemeiner Lage im Raume $y_1\cdots y_n$ über.

Hiermit ist gezeigt, dass die holoedrisch isomorphe Beziehung zwischen unsern beiden Gruppen die im Satze 3, S. 359 zusammengestellten Eigenschaften besitzt; also ist nach diesem Satze die Gruppe: $X_1f\cdots X_rf$ mit der Gruppe: $Z_1f\cdots Z_rf$ ähnlich und die Richtigkeit des Theorems 76, S. 425 ist erwiesen.

Zum Beweise des Theorems 76 braucht man übrigens gar nicht auf den citirten Satz zurückzugreifen. Es lässt sich vielmehr aus den vorstehenden Entwickelungen direkt schliessen, dass eine Transformation existirt, welche die infinitesimalen Transformationen: $X_1f\cdots X_rf$ bezüglich in: $Y_1f\cdots Y_rf$ überführt.

Wir haben gesehen, dass durch unsere holoedrisch isomorphe Beziehung dem Punkte: $(x_i^0)T_{(e)}$ des Raumes $x_1\cdots x_n$ der Punkt: $(y_i^0)\mathfrak{T}_{(e)}$ des Raumes $y_1\cdots y_n$ zugeordnet ist, und zwar ist auf diese Weise zwischen den Punkten von allgemeiner Lage beider Räume eine innerhalb eines gewissen Bereichs eindeutig umkehrbare Beziehung hergestellt. Deuten wir nun die $x_i$ und die $y_i$ als Punktcoordinaten eines und desselben $n$-fach ausgedehnten Raumes: $R_n$ und zwar beide in Bezug auf dasselbe Coordinatensystem, so giebt es eine ganz bestimmte Transformation $\mathrm{T}$ des Raumes $R_n$, welche stets den Punkt mit den Coordinaten: $(x_i^0)T_{(e)}$ in den Punkt mit den Coordinaten: $(y_i^0)\mathfrak{T}_{(e)}$ überführt. Wir werden nachweisen, dass diese Transformation $\mathrm{T}$ die infinitesimalen Transformationen: $X_1f\cdots X_rf$ in bezüglich: $Y_1f\cdots Y_rf$ überführt, dass also unsere beiden $r$-gliedrigen Gruppen gerade vermöge der Transformation $\mathrm{T}$ mit einander ähnlich sind.

Die Transformation $\mathrm{T}$ befriedigt alle die unendlich vielen symbolischen Gleichungen:

$$
(x_i^0)T_{(e')}\mathrm{T}=(y_i^0)\mathfrak{T}_{(e')},
\tag{14}
$$

mit den $r$ willkürlichen Parametern $e_1\cdots e_r$, sie ist sogar durch diese Gleichungen definirt. Hieraus geht hervor, dass $\mathrm{T}$ zugleich die folgenden symbolischen Gleichungen erfüllt:

$$
(x_i^0)T_{(e')}T_{(e)}\mathrm{T}
=(y_i^0)\mathfrak{T}_{(e')}\mathfrak{T}_{(e)},
$$

welche Werthe auch die Parameter $e$ und $e'$ haben mögen.

Verbinden wir diese Gleichungen mit den Gleichungen (14), welche wir offenbar auch schreiben können:

$$
(x_i^0)T_{(e')}=(y_i^0)\mathfrak{T}_{(e')}\mathrm{T}^{-1},
$$

so erhalten wir:

$$
(y_i^0)\mathfrak{T}_{(e')}\mathrm{T}^{-1}T_{(e)}\mathrm{T}
=(y_i^0)\mathfrak{T}_{(e')}\mathfrak{T}_{(e)},
$$

oder, was dasselbe ist:

$$
(y_i^0)\mathfrak{T}_{(e')}\mathrm{T}^{-1}T_{(e)}
\mathrm{T}\mathfrak{T}_{(e)}^{-1}
=(y_i^0)\mathfrak{T}_{(e')}.
\tag{15}
$$

Der Punkt: $(y_i^0)\mathfrak{T}_{(e')}$ kann bei geeigneter Wahl von $e_1'\cdots e_r'$ mit jedem Punkte von allgemeiner Lage in dem $R_n$ zur Deckung gebracht werden, also sagen die Gleichungen (15) aus, dass jede Transformation von der Form:

$$
\mathrm{T}^{-1}T_{(e)}\mathrm{T}\mathfrak{T}_{(e)}^{-1}
\tag{16}
$$

alle Punkte von allgemeiner Lage in dem $R_n$ stehen lässt. Das ist aber offenbar nur möglich, wenn alle Transformationen (16) mit der identischen Transformation zusammenfallen.

Hiermit ist bewiesen, dass die folgenden $\infty^r$ symbolischen Gleichungen bestehen:

$$
\mathrm{T}^{-1}T_{(e)}\mathrm{T}=\mathfrak{T}_{(e)},
\tag{17}
$$

dass also die Transformation $\mathrm{T}$ jede Transformation $T_{(e)}$ der Gruppe: $X_1f\cdots X_rf$ in die entsprechende Transformation $\mathfrak{T}_{(e)}$ der Gruppe: $Z_1f\cdots Z_rf$ überführt. Mit andern Worten, der Ausdruck: $e_1X_1f+\cdots+e_rX_rf$ verwandelt sich bei der Ausführung der Transformation $\mathrm{T}$ in den Ausdruck: $e_1Y_1f+\cdots+e_rY_rf$ oder, was dasselbe ist, die $r$ infinitesimalen Transformationen: $X_1f\cdots X_rf$ gehen bei Ausführung von $\mathrm{T}$ in bezüglich: $Y_1f\cdots Y_rf$ über.

Folglich sind die beiden Gruppen: $X_1f\cdots X_rf$ und $Z_1f\cdots Z_rf$ mit einander ähnlich und das Theorem 76, S. 425 ist nunmehr auch unabhängig von dem Satze 3, S. 359 bewiesen.

#### Original footnote: similarity criterion

**F1 · p. 425, at the end of Theorem 76.** Vgl. Lie, [Archiv for Math. og Naturv. Christiania 1885](https://archive.org/details/archivformathema1018841886oslo), S. 388 u. 389.

### English translation: similarity of transitive groups (§104)

**§104.**

In Chapter 19, Proposition 3, p. 359, we gave the criteria for similarity of groups of the same composition a noteworthy form. Namely, we showed that two groups of the same composition in equally many variables are similar if and only if they can be related to one another in a certain quite particular holoedrically isomorphic manner.

We already announced then that the criterion in question can be substantially simplified when the two groups concerned are *transitive*. We announced that the following theorem holds:

**Theorem 76.** *Two transitive groups of the same composition,*

$$
X_kf=\sum_{1}^{n}{}_i\,\xi_{ki}(x_1\cdots x_n)\frac{\partial f}{\partial x_i}
\qquad(k=1\cdots r)
$$

*and*

$$
Z_kf=\sum_{1}^{n}{}_i\,\zeta_{ki}(y_1\cdots y_n)\frac{\partial f}{\partial y_i}
\qquad(k=1\cdots r)
$$

*in equally many variables are similar if and only if the following condition is satisfied. Choose a particular point $x_1^0\cdots x_n^0$ lying on no manifold invariant under the group $X_1f\cdots X_rf$. It must be possible to relate the two groups holoedrically isomorphically so that the largest subgroup contained in the group $X_1f\cdots X_rf$ and leaving the point $x_1^0\cdots x_n^0$ invariant corresponds to the largest subgroup of the group $Z_1f\cdots Z_rf$ leaving some point $y_1^0\cdots y_n^0$ at rest.* [F1]

Proposition 3, p. 359, makes it clear that this condition is necessary for similarity of the two groups. It therefore remains only to show that it is sufficient as well.

Suppose, then, that the hypotheses of the theorem are satisfied. In the group $Z_1f\cdots Z_rf$, suppose we have selected independent infinitesimal transformations $Y_1f\cdots Y_rf$ such that our two groups are related holoedrically isomorphically in the manner described in Theorem 76 when each infinitesimal transformation $e_1X_1f+\cdots+e_rX_rf$ is assigned the infinitesimal transformation $e_1Y_1f+\cdots+e_rY_rf$.

By the developments of the preceding section, this holoedrically isomorphic relation also establishes a uniquely reversible relation between the finite transformations of the two groups. We can describe the latter most simply by regarding $\sum e_kX_kf$ and $\sum e_kY_kf$, in the familiar way, as symbols for the finite transformations of our groups and, for greater convenience, denoting the finite transformation $\sum e_kX_kf$ briefly by $T_{(e)}$ and the transformation $\sum e_kY_kf$ briefly by $\mathfrak{T}_{(e)}$.

Under these assumptions, the holoedrically isomorphic relation between our two groups assigns the transformation $\mathfrak{T}_{(e)}$ to the transformation $T_{(e)}$ and conversely. This assignment is such that the two transformations $T_{(e)}T_{(e')}$ and $\mathfrak{T}_{(e)}\mathfrak{T}_{(e')}$ also correspond, where $e_1\cdots e_r$ and $e_1'\cdots e_r'$ denote entirely arbitrary systems of values.

The point $x_1^0\cdots x_n^0$ remains invariant under exactly $r-n$ independent infinitesimal transformations of the group $X_1f\cdots X_rf$. Consequently, it admits exactly $\infty^{r-n}$ distinct finite transformations of this group, transformations that, as is known, form an $(r-n)$-parameter subgroup. For the most general transformation $T_{(e)}$ leaving the point $x_1^0\cdots x_n^0$ at rest, we introduce the symbol $S_{(a_1\cdots a_{r-n})}$, or briefly $S_{(a)}$. Here $a_1\cdots a_{r-n}$ are understood to be arbitrary parameters.

Those transformations $\mathfrak{T}_{(e)}$ of the group $Z_1f\cdots Z_rf$ that are assigned to the transformations $S_{(a)}$ of the group $X_1f\cdots X_rf$ are denoted by $\mathfrak{S}_{(a_1\cdots a_{r-n})}$, or briefly by $\mathfrak{S}_{(a)}$. Under the assumptions made, the $\infty^{r-n}$ transformations $\mathfrak{S}_{(a)}$ then form the largest subgroup contained in the group $Z_1f\cdots Z_rf$ and leaving the point $y_1^0\cdots y_n^0$ invariant. This entails that the point $y_1^0\cdots y_n^0$ belongs to no manifold remaining invariant under the group $Z_1f\cdots Z_rf$.

After these preparations, we make the following considerations.

On carrying out the transformation $T_{(e)}$, the point $x_i^0$ passes to the point $(x_i^0)T_{(e)}$, whose position naturally depends on the values of the parameters $e_1\cdots e_r$. By Chapter 14, Proposition 1, p. 227, this new point itself admits exactly $\infty^{r-n}$ transformations of the group $X_1f\cdots X_rf$, namely all transformations of the form

$$
T_{(e)}^{-1}S_{(a)}T_{(e)},
$$

with the $r-n$ arbitrary parameters $a_1\cdots a_{r-n}$.

On the other hand, under the transformation $\mathfrak{T}_{(e)}$, the point $y_i^0$ passes to the point $(y_i^0)\mathfrak{T}_{(e)}$, which naturally admits exactly $\infty^{r-n}$ transformations of the group $Z_1f\cdots Z_rf$, namely all transformations of the form

$$
\mathfrak{T}_{(e)}^{-1}\mathfrak{S}_{(a)}\mathfrak{T}_{(e)}.
$$

These are plainly those transformations of the group $Z_1f\cdots Z_rf$ that are assigned to the transformations $T_{(e)}^{-1}S_{(a)}T_{(e)}$ of the group $X_1f\cdots X_rf$. Thus we see that, under our holoedrically isomorphic relation, precisely the same holds for the points $(x_i^0)T_{(e)}$ and $(y_i^0)\mathfrak{T}_{(e)}$ as for the points $x_i^0$ and $y_i^0$. Namely, the largest subgroup contained in the group $X_1f\cdots X_rf$ and leaving the point $(x_i^0)T_{(e)}$ invariant corresponds to the largest subgroup of the group $Z_1f\cdots Z_rf$ under which the point $(y_i^0)\mathfrak{T}_{(e)}$ remains fixed.

Now give the parameters $e_1\cdots e_r$ in the transformations $T_{(e)}$ and $\mathfrak{T}_{(e)}$ all possible values in succession. Because the group $X_1f\cdots X_rf$ is transitive, the point $(x_i^0)T_{(e)}$ then passes successively to all points of the space $x_1\cdots x_n$ lying on no invariant manifold, hence to all points in general position. At the same time, the point $(y_i^0)\mathfrak{T}_{(e)}$ passes to all points in general position in the space $y_1\cdots y_n$.

This shows that the holoedrically isomorphic relation between our two groups has the properties assembled in Proposition 3, p. 359. By that proposition, therefore, the group $X_1f\cdots X_rf$ is similar to the group $Z_1f\cdots Z_rf$, and the correctness of Theorem 76, p. 425, is established.

In fact, proving Theorem 76 does not require any appeal to the cited proposition. Rather, the preceding developments directly imply the existence of a transformation carrying the infinitesimal transformations $X_1f\cdots X_rf$ respectively into $Y_1f\cdots Y_rf$.

We have seen that our holoedrically isomorphic relation assigns to the point $(x_i^0)T_{(e)}$ of the space $x_1\cdots x_n$ the point $(y_i^0)\mathfrak{T}_{(e)}$ of the space $y_1\cdots y_n$. In this way, a uniquely reversible relation within a certain region is established between the points in general position of the two spaces. If we now interpret the $x_i$ and the $y_i$ as point coordinates of one and the same $n$-dimensional space $R_n$, both with respect to the same coordinate system, there is a particular transformation $\mathrm{T}$ of the space $R_n$ that always carries the point with coordinates $(x_i^0)T_{(e)}$ into the point with coordinates $(y_i^0)\mathfrak{T}_{(e)}$. We shall show that this transformation $\mathrm{T}$ carries the infinitesimal transformations $X_1f\cdots X_rf$ respectively into $Y_1f\cdots Y_rf$, so that our two $r$-parameter groups are similar precisely by means of the transformation $\mathrm{T}$.

The transformation $\mathrm{T}$ satisfies all the infinitely many symbolic equations

$$
(x_i^0)T_{(e')}\mathrm{T}=(y_i^0)\mathfrak{T}_{(e')},
\tag{14}
$$

with the $r$ arbitrary parameters $e_1\cdots e_r$; indeed, it is defined by these equations. It follows that $\mathrm{T}$ also satisfies the following symbolic equations:

$$
(x_i^0)T_{(e')}T_{(e)}\mathrm{T}
=(y_i^0)\mathfrak{T}_{(e')}\mathfrak{T}_{(e)},
$$

whatever values the parameters $e$ and $e'$ may have.

Combining these equations with equations (14), which we can plainly also write as

$$
(x_i^0)T_{(e')}=(y_i^0)\mathfrak{T}_{(e')}\mathrm{T}^{-1},
$$

we obtain

$$
(y_i^0)\mathfrak{T}_{(e')}\mathrm{T}^{-1}T_{(e)}\mathrm{T}
=(y_i^0)\mathfrak{T}_{(e')}\mathfrak{T}_{(e)},
$$

or, equivalently,

$$
(y_i^0)\mathfrak{T}_{(e')}\mathrm{T}^{-1}T_{(e)}
\mathrm{T}\mathfrak{T}_{(e)}^{-1}
=(y_i^0)\mathfrak{T}_{(e')}.
\tag{15}
$$

By a suitable choice of $e_1'\cdots e_r'$, the point $(y_i^0)\mathfrak{T}_{(e')}$ can be brought to coincide with any point in general position in $R_n$. Equations (15) therefore say that every transformation of the form

$$
\mathrm{T}^{-1}T_{(e)}\mathrm{T}\mathfrak{T}_{(e)}^{-1}
\tag{16}
$$

leaves all points in general position in $R_n$ fixed. This is plainly possible only if all transformations (16) coincide with the identity transformation.

It is thus proved that the following $\infty^r$ symbolic equations hold:

$$
\mathrm{T}^{-1}T_{(e)}\mathrm{T}=\mathfrak{T}_{(e)},
\tag{17}
$$

Thus the transformation $\mathrm{T}$ carries every transformation $T_{(e)}$ of the group $X_1f\cdots X_rf$ into the corresponding transformation $\mathfrak{T}_{(e)}$ of the group $Z_1f\cdots Z_rf$. In other words, on carrying out the transformation $\mathrm{T}$, the expression $e_1X_1f+\cdots+e_rX_rf$ is transformed into the expression $e_1Y_1f+\cdots+e_rY_rf$. Equivalently, carrying out $\mathrm{T}$ takes the $r$ infinitesimal transformations $X_1f\cdots X_rf$ respectively into $Y_1f\cdots Y_rf$.

Consequently, the two groups $X_1f\cdots X_rf$ and $Z_1f\cdots Z_rf$ are similar, and Theorem 76, p. 425, is now also proved independently of Proposition 3, p. 359.

#### Translated original footnote: similarity criterion

**F1 · p. 425, at the end of Theorem 76.** Compare Lie, [Archiv for Math. og Naturv. Christiania 1885](https://archive.org/details/archivformathema1018841886oslo), pp. 388 and 389.
