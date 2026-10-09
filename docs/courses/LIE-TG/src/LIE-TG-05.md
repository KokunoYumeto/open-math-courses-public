# The second fundamental theorem and the group of parameters

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI, GPT-6.1 Sol (OpenAI), in Codex at Ultra. Public domain (CC0).*

The generators of a transformation group close under brackets with constant coefficients. Conversely, a finite-dimensional bracket-closed space of analytic vector fields determines a local transformation group. The converse includes fields that are dependent at every individual point. To handle them, we first evaluate the fields at finitely many points, then construct multiplication from a frame with constant brackets.

We use The fundamental differential equations, One-parameter groups, and the complete-system theorem in Complete systems and invariants. Basic references are [Lie–Engel I], [Merker], and [Kunzinger]. We keep the right-action convention $T_b\circ T_a=T_{m(a,b)}$ and the bracket $XY-YX$.

## 1. Constant brackets on the parameter group

Let $B_i(a)=d(L_a)_e(e_i)$, where $L_a(b)=m(a,b)$ and $e_i$ is a tangent basis at the identity. Associativity gives $(L_a)_*B_i=B_i$. Thus $B_i$ are left-invariant fields.

**Theorem 1.1 (second fundamental theorem).** The generators of an effective $r$-dimensional local action satisfy

$$
[X_i,X_j]=\sum_{k=1}^r c_{ij}^kX_k
\tag{1.1}
$$

with constants $c_{ij}^k\in\mathbb K$.

**Proof.** Pushforward by a diffeomorphism preserves brackets, so $[B_i,B_j]$ is left-invariant. Write its value at the identity as $\sum_kc_{ij}^ke_k$. Left-invariance gives $[B_i,B_j]=\sum_kc_{ij}^kB_k$ everywhere near the identity.

For each fixed $x$, the orbit map $F_x(a)=T_a(x)$ relates $B_i$ to $X_i$: $dF_x(B_i)=X_i\circ F_x$, by the fundamental equations. Related fields have related brackets, since applying both sides to a function and pulling it back gives the same commutator of differential operators. Hence

$$
dF_x([B_i,B_j])=[X_i,X_j]\circ F_x.
$$

At the identity this is (1.1). Effectiveness makes the constants unique, because the $X_k$ are independent over constants. $\square$

The same argument would give constant bracket relations for an ineffective action, but its displayed generator list could have linear dependencies and nonunique constants. We henceforth identify an effective generator space with its finite-dimensional Lie algebra.

**Proposition 1.2 (necessary identities for the constants).** For the independent generators in Theorem 1.1,

$$
c_{ij}^k=-c_{ji}^k,\qquad
\sum_s\left(c_{ij}^sc_{sk}^{\ell}
+c_{jk}^sc_{si}^{\ell}
+c_{ki}^sc_{sj}^{\ell}\right)=0.
\tag{1.2}
$$

**Proof.** Antisymmetry of the operator commutator gives the first identity. Expanding
$[[X_i,X_j],X_k]+[[X_j,X_k],X_i]+[[X_k,X_i],X_j]$
as a sum of compositions of three differential operators cancels every term. Substitution of (1.1) gives a constant linear combination of the $X_\ell$ with the second coefficients in (1.2). Independence over constants makes each coefficient zero. With dependent generators, this calculation instead says that the resulting combination lies in their constant kernel. It does not force every chosen coefficient to vanish. $\square$

**Proposition 1.3 (common infinitesimal transformations).** Suppose two analytic local groups act on the same connected spatial neighbourhood, with finite-dimensional generator algebras $\mathfrak g$ and $\mathfrak k$. Their common infinitesimal transformations form the constant vector-space intersection

$$
\mathfrak h=\mathfrak g\cap\mathfrak k.
\tag{1.3}
$$

This space is bracket-closed and generates a local subgroup contained in both actions.

**Proof.** If $U,V\in\mathfrak h$, their bracket belongs to both $\mathfrak g$ and $\mathfrak k$, hence to $\mathfrak h$. Choose a basis of this finite-dimensional space. It is independent over constants and has constant bracket coefficients, so Theorem 3.1 below constructs its local group. Each of its canonical transformations is the small time-one flow of a field in $\mathfrak h$. Such a flow belongs to each original group, by uniqueness of the generator's flow there. Thus the generated group is common to both. If $\mathfrak h=0$, its local group is the identity alone. $\square$

This is an intersection of vector fields with constant coefficients, rather than an intersection of their pointwise spans. For example, $\mathfrak g=\mathbb K\partial_x$ and $\mathfrak k=\mathbb K x\partial_x$ have zero constant intersection. Away from $x=0$, their pointwise distributions are nevertheless the same one-dimensional tangent space.

## 2. A frame determines local multiplication

The following construction is useful both for the converse theorem and for uniqueness.

**Lemma 2.1 (constant-frame construction).** Let $E_1,\ldots,E_r$ be an analytic frame on an $r$-manifold $P$, with $[E_i,E_j]=\sum_kc_{ij}^kE_k$ and constant coefficients. Choose $o\in P$. There is a local group with identity $o$ whose left-invariant frame is $E_i$. A local map preserving the frame is uniquely determined by its value at one point.

**Proof.** On $P\times P$, consider the rank-$r$ fields $(E_i,E_i)$. Their brackets have the same constant relations, so they form a complete system. Its integral leaf through $(o,a)$ projects locally diffeomorphically to the first factor, because the projection maps its tangent frame to the frame $E_i$. The leaf is therefore the graph of an analytic map $H_a$ with $H_a(o)=a$ and $(H_a)_*E_i=E_i$.

The complete-system coordinates and the inverse-function theorem show that $H_a(p)$ depends analytically on both $a$ and $p$. More explicitly, choose a Frobenius chart for the distribution near $(o,o)$; its leaf labels depend analytically on $(o,a)$, and solving the projection equations in the leaf gives the graph by an analytic inverse. Thus the graph construction can be made on one product neighbourhood.

For uniqueness, ordered flow products of $E_1,\ldots,E_r$ give coordinates near any point, because their derivative at zero is a frame. A frame-preserving map intertwines each such flow by uniqueness of ordinary differential equations. Once its value at the initial point is specified, its value at every point in these product coordinates is forced.

Define $m(a,b)=H_a(b)$. The identity map preserves the frame and fixes $o$, so $H_o=\mathrm{id}$. Also $H_a(o)=a$, giving both identity equations. The composite $H_a\circ H_b$ preserves the frame and sends $o$ to $H_a(b)$. Uniqueness gives

$$
H_a\circ H_b=H_{m(a,b)}.
$$

This proves associativity wherever the maps are defined. Because $H_a$ is locally invertible, the inverse-function theorem solves $m(a,b)=o$ analytically for $b=\iota(a)$ near $o$. Associativity and injectivity of $H_a$ give

$$
m(a,m(\iota(a),a))=m(m(a,\iota(a)),a)=a=m(a,o),
$$

so $m(\iota(a),a)=o$ as well. Finally, $L_a=H_a$ preserves the frame, which is exactly left-invariance. $\square$

**Proposition 2.2 (reconstructing the parameter law).** In local coordinates on $P$, form the complete system

$$
\left(E_i(a')+E_i(b)\right)H_j(a',b)=0,\qquad
H_j(a',o)=a_j',
\quad 1\le i,j\le r.
\tag{2.1}
$$

The local multiplication is obtained by solving $a_j=H_j(a',b)$ for $a'$.

**Proof.** The diagonal fields have rank $r$ and constant brackets. Projection to the $b$ factor is an isomorphism on their tangent spaces, so the slice $b=o$ is transverse. The analytic complete-system theorem gives the normalized first integrals in (2.1). Their $a'$ Jacobian is the identity when $b=o$, hence solving for $a'$ is legitimate near $(o,o)$.

For fixed $a$, the graph $b\mapsto(m(a,b),b)$ is tangent to the diagonal distribution: $L_a$ preserves every $E_i$. It passes through $(a,o)$, where the first integrals take the values $a_j$. Therefore $H_j(m(a,b),b)=a_j$. The unique solution of these equations is exactly the law from Lemma 2.1. This gives the principal-solution algorithm of Lie's Theorem 73 without leaving its normalization implicit. $\square$

## 3. Constructing the action from its generators

**Theorem 3.1 (converse second theorem).** Let $X_1,\ldots,X_r$ be analytic vector fields on a connected neighbourhood in $M$, independent over constants, satisfying (1.1). They generate an effective analytic $r$-parameter local transformation group. Its transformations near the identity are the canonical flows from the one-parameter lesson.

**Proof.** First choose finitely many points $p_1,\ldots,p_N$ for which the evaluation map

$$
\mathfrak g\longrightarrow\bigoplus_{\ell=1}^NT_{p_\ell}M,
\qquad X\longmapsto(X(p_1),\ldots,X(p_N))
\tag{3.1}
$$

is injective. To see that such points exist, start with the whole finite-dimensional space $\mathfrak g$. If the kernel of the chosen evaluations is nonzero, select a nonzero field in it. It is nonzero somewhere, so evaluation at that point strictly reduces the kernel. At most $r$ reductions give an injective map.

On $M^N$ let $\widehat X_i$ be the diagonal field with $X_i$ in each factor. At the tuple $p=(p_1,\ldots,p_N)$ these are pointwise independent by (3.1); they stay independent near $p$. They satisfy the same constant brackets. The complete-system theorem supplies an $r$-dimensional integral leaf $P$ through $p$, and their restrictions form a frame $E_i$ on $P$. Lemma 2.1 gives a local parameter group on $P$, with identity $o=p$.

To produce an action on the original $M$, use the distribution on $P\times M$ spanned by

$$
(E_i,X_i),\qquad 1\le i\le r.
$$

Its rank is $r$, its brackets close with constants, and projection to $P$ is an isomorphism on its tangent spaces. The leaf through $(o,x)$ is the graph $a\mapsto f(x,a)$ of an analytic map, depending analytically on $x$. It satisfies $f(x,o)=x$ and

$$
d_a f(E_i)=X_i(f(x,a)).
\tag{3.2}
$$

Here $x$ may range over a neighbourhood of any specified point of $M$; the evaluation tuple used to construct $P$ need not lie in that neighbourhood. Since $D_xf$ is the identity at $a=o$, it remains invertible after shrinking.

It remains to prove the action law. For fixed $a$, left multiplication $H_a$ preserves $E_i$. Transporting a horizontal graph from $o$ to $b$ by $H_a$ gives the horizontal graph from $a$ to $m(a,b)$. Start this graph with value $f(x,a)$ at $a$. Equation (3.2) and uniqueness of integral graphs give endpoint $f(f(x,a),b)$. The original horizontal graph through $(o,x)$ gives endpoint $f(x,m(a,b))$. Both are the same integral leaf continued through $(a,f(x,a))$, so

$$
f(f(x,a),b)=f(x,m(a,b)).
$$

The inverse law makes $f(\cdot,\iota(a))$ the inverse transformation. Its generator along $E_i(o)$ is $X_i$ by (3.2). Independence over constants gives essentiality by the first fundamental theorem's independence test. Canonical coordinates from the one-parameter lesson now give the last assertion. $\square$

This proof does not assume an abstract existence theorem for an arbitrary Lie algebra. It begins with a Lie algebra already realized by analytic fields. Constructing such fields for an arbitrary abstract algebra is the third theorem.

## 4. Left and right translations

Let $R_a(b)=m(b,a)$ and define right-invariant fields $C_i(a)=d(R_a)_o(e_i)$. Their flows are left multiplication by one-parameter subgroup elements; the flows of $E_i$ are right multiplication by those elements. Associativity makes the two sets of flows commute, hence

$$
[E_i,C_j]=0.
$$

Inversion reverses multiplication. Differentiating it gives $\iota_*E_i=-C_i$. Since pushforward preserves brackets,

$$
[C_i,C_j]=-\sum_kc_{ij}^kC_k.
\tag{4.1}
$$

The parameter group's action on itself by right translations is locally simply transitive: $m(o,a)=a$, and solving $m(p,a)=q$ gives a unique $a$ near the identity. Left translations give the reciprocal action. Both have $r$ parameters; their bracket signs reflect which invariant frame is used.

**Example 4.1 (affine parameters).** With $(\alpha,\beta)\cdot(\gamma,\delta)=(\gamma\alpha,\gamma\beta+\delta)$,

$$
E_1=\alpha\partial_\alpha+\beta\partial_\beta,\quad E_2=\partial_\beta,
\qquad
C_1=\alpha\partial_\alpha,\quad C_2=\alpha\partial_\beta.
$$

Direct computation gives $[E_1,E_2]=-E_2$, $[C_1,C_2]=C_2$, and all cross brackets zero. The sign agrees with the physical fields $x\partial_x,\partial_x$.

**Example 4.2 (rotation brackets).** The physical rotation fields $X_1=y\partial_z-z\partial_y$, $X_2=z\partial_x-x\partial_z$, $X_3=x\partial_y-y\partial_x$ satisfy $[X_1,X_2]=-X_3$ and the cyclic analogues. Indeed, their coefficient matrices are $A_i v=e_i\times v$, with $[A_i,A_j]=\sum_k\varepsilon_{ijk}A_k$, whereas linear vector-field brackets reverse the matrix commutator. Replacing the basis by $J_i=-X_i$ gives $[J_i,J_j]=\sum_k\varepsilon_{ijk}J_k$. Either basis describes the same algebra; specifying the basis fixes the sign.

## 5. Equal structure constants mean local isomorphism

**Theorem 5.1.** Two analytic local groups whose tangent bases have the same structure constants are locally isomorphic by a unique local homomorphism with the specified tangent-basis identification.

**Proof.** Let $E_i$ and $F_i$ be their left-invariant frames. The distribution spanned by $(E_i,F_i)$ on the product of the groups is involutive with constant brackets. Its leaf through the pair of identities projects isomorphically to each factor, giving a local diffeomorphism $K$ that carries $E_i$ to $F_i$ and fixes the identity.

For fixed $a$, the maps $b\mapsto K(m_G(a,b))$ and $b\mapsto m_H(K(a),K(b))$ carry the $E$ frame to the $F$ frame and agree at the identity, where their value is $K(a)$. The uniqueness part of Lemma 2.1 makes them equal. Thus $K$ is a local homomorphism. That same uniqueness proves uniqueness of $K$. $\square$

Different actions of this same local group on different manifolds need not be equivalent. Structure constants determine the parameter group, whereas isotropy data are also needed to classify transitive actions.

The homomorphism here is analytic and local. Its inverse is a local homomorphism as well, since the construction is symmetric. No global group identification follows: the additive real line and the circle have the same one-dimensional abelian Lie algebra. Nor can an arbitrary product-preserving set bijection be differentiated; discontinuous additive automorphisms of the real line show why the analytic regularity matters in the converse direction of the historical correspondence argument.

**Theorem 5.2 (constructing a local quotient).** Let $G$ be an analytic local group of dimension $r$, and let $\mathfrak h$ be an ideal of its tangent Lie algebra, of dimension $q$. There is an analytic local group $Q$ of dimension $s=r-q$ and a local homomorphism $\pi:G\to Q$ whose differential has kernel $\mathfrak h$. Its local identity fibre is the connected subgroup germ generated by $\mathfrak h$.

**Proof.** Choose the tangent basis so that $e_{s+1},\ldots,e_r$ span $\mathfrak h$, and let $E_i$ be the corresponding left-invariant frame. The fields $E_{s+1},\ldots,E_r$ span an involutive rank-$q$ distribution. Choose $s$ independent first integrals $u_1,\ldots,u_s$ and complete them by coordinates $v_1,\ldots,v_q$, taking the identity as the coordinate origin.

Ideal invariance says that $[E_\alpha,E_i]$ is vertical whenever $\alpha>s$. Because $E_\alpha u_j=0$,

$$
E_\alpha(E_i u_j)
=[E_\alpha,E_i]u_j+E_i(E_\alpha u_j)=0.
$$

The kernel fields span the vertical tangent spaces, so $E_i u_j$ is independent of $v$. Thus, for $i\le s$, the projected fields
$\bar E_i=\sum_j(E_i u_j)\partial_{u_j}$
are well-defined. The full frame has an invertible block-triangular coefficient matrix in $(u,v)$; therefore the projected fields are an $s$-frame. Projecting brackets gives their constant relations, with the kernel terms removed. Lemma 2.1 constructs their local group $Q$, with identity $u=0$.

Set $\pi(u,v)=u$. To prove its multiplication law, fix $a\in G$ and compare the maps

$$
b\longmapsto\pi(m_G(a,b)),\qquad
b\longmapsto m_Q(\pi(a),\pi(b)).
$$

Both carry $E_i$ to $\bar E_i$ for $i\le s$ and to zero for $i>s$. They agree at $b=o_G$, with value $\pi(a)$. Ordered flow products of the full frame give coordinates near $o_G$; uniqueness of the corresponding flows in $Q$ forces the two maps to agree throughout those coordinates. Hence

$$
\pi(m_G(a,b))=m_Q(\pi(a),\pi(b)).
\tag{5.1}
$$

This also sends inverse parameters to inverse parameters. The identity fibre is $u=0$, the local integral leaf of the kernel distribution through $o_G$. Flow products of its frame generate precisely this connected subgroup germ. It is normal wherever the local products are defined, since (5.1) sends each conjugate of a kernel element to the identity in $Q$. Finally $d\pi_{o_G}$ kills precisely the chosen kernel basis. The cases $q=0$ and $s=0$ mean, respectively, a locally invertible projection and a quotient consisting of one point. $\square$

In these coordinates, the first $s$ output coordinates of the law on $G$ depend only on the two input $u$ tuples. The remaining coordinates may depend on both $u$ and $v$. This is the triangular parameter-law description in the end of historical §103. A global quotient requires global subgroup and domain hypotheses.

**Proposition 5.3 (allowing dependent generators).** Start with a regular constant-bracket frame $E_1,\ldots,E_r$ as in Lemma 2.1. Let analytic spatial fields $X_1,\ldots,X_r$, possibly dependent over constants, satisfy the same bracket relations. They determine an analytic local action of the frame's group $G$. If

$$
\rho(e_i)=X_i,\qquad
\mathfrak h=\ker\rho,
\tag{5.2}
$$

then the action factors through the quotient in Theorem 5.2 and has $\dim(\operatorname{im}\rho)$ essential parameters.

**Proof.** The bracket relations make $\rho$ a Lie algebra homomorphism. Its constant kernel is consequently an ideal. The distribution $(E_i,X_i)$ on $G\times M$ still has rank $r$, because its first components form a frame, and its brackets close with the given constants. The horizontal-graph construction and uniqueness argument of Theorem 3.1 therefore give an analytic action even though the spatial list is dependent.

Each field in $\mathfrak h$ acts as zero. The flow products generating the identity fibre of $\pi$ hence act as the identity transformation. If $\pi(a)=\pi(b)$ near the identity, then $h=m_G(\iota(a),b)$ is in that fibre, and $b=m_G(a,h)$. The action law gives $T_b=T_h\circ T_a=T_a$, so the action descends to $Q$. Its infinitesimal algebra is identified with $\operatorname{im}\rho$. A basis of that image is independent over constants; the essentiality test of the first fundamental theorem, or the finite-evaluation construction of Theorem 3.1, gives exactly its dimension as the number of essential parameters. After shrinking a faithful evaluation chart, the local identity kernel is precisely the fibre of $\pi$. $\square$

The regular auxiliary frame is a hypothesis here. It forces Jacobi for the specified constants. Constant bracket expressions for a dependent spatial list alone do not force this: set $X_1=X_2=X_3=0$ and prescribe abstract brackets $[e_1,e_2]=e_2$, $[e_2,e_3]=e_3$, $[e_3,e_1]=0$, with reverse brackets defined by antisymmetry. All the spatial identities hold, but the abstract Jacobi sum is $e_3$. Such constants cannot be the constants of a frame. Choosing an independent basis of the actual image algebra avoids this ambiguity.

**Example 5.1 (kernel and stabilizer).** For the additive parameter group $\mathbb K^2$, take $X_1=X_2=\partial_x$. Its action is $T_{(a,b)}(x)=x+a+b$. The constant kernel is $\mathbb K(e_1-e_2)$, and $u=a+b$ gives its one-dimensional effective quotient. By contrast, the affine fields $D=x\partial_x$ and $P=\partial_x$ have zero constant kernel, although $D-x_0P$ vanishes at the point $x_0$. That latter relation is in a point stabilizer; its field is nonzero away from $x_0$.

## 6. What fundamental equations imply without an identity

Suppose an analytic family of local diffeomorphisms satisfies

$$
\partial_{a_k}f(x,a)=\sum_j\psi_{kj}(a)X_j(f(x,a)),
\tag{6.1}
$$

where $\psi$ is invertible and the $X_j$ are independent over constants. Choose a regular parameter $a_0$. The **relative family**

$$
F(y,a)=f(f(\cdot,a_0)^{-1}(y),a)
\tag{6.2}
$$

has identity at $a_0$ and satisfies the same fundamental equations.

**Proposition 6.1.** The relative family (6.2) is a local transformation group after restricting and choosing regular parameter coordinates. The original family need not itself contain an identity.

**Proof.** Define a frame $B_j$ on the parameter domain by $\sum_kB_j^k\psi_{k\ell}=\delta_{j\ell}$. Then $d_aF(B_j)=X_j\circ F$. Write $[B_i,B_j]=\sum_kc_{ij}^k(a)B_k$. Related brackets give

$$
[X_i,X_j](F(y,a))=\sum_kc_{ij}^k(a)X_k(F(y,a)).
$$

For each $a$ the map $F(\cdot,a)$ has an open image. Analytic continuation gives this identity between fields on the connected neighbourhood. Independence over constants forces the coefficients $c_{ij}^k(a)$ to equal their values at $a_0$. Thus $B_j$ is a constant-bracket frame. Lemma 2.1 supplies its local group, and the horizontal-graph argument of Theorem 3.1 applies directly to $F$, yielding the action law. The contracting multipliers in the first two lessons show why the original family need not contain an identity. $\square$

Normalization is a mathematical operation, not a continuation of the original parameter domain. It preserves the topic of Lie's differential-equation approach without asserting the false conclusion that every closure-only family already has inverses.

**Proposition 6.2 (a redundant fundamental family).** In (6.1), keep $\psi$ invertible but allow the $X_j$ to be dependent over constants. Their span is a finite-dimensional Lie algebra of analytic fields. If its dimension is $s$, the normalized family (6.2) reduces locally to an effective $s$-parameter group.

**Proof.** Define the parameter frame $B_j$ exactly as in Proposition 6.1. Its bracket coefficients may now depend on $a$. Evaluating the related-bracket identity at $a=a_0$, where $F(y,a_0)=y$, gives constant expressions for every $[X_i,X_j]$ in their span. Thus that span is bracket-closed. Choosing an independent basis $Z_1,\ldots,Z_s$ gives its genuine structure constants and Jacobi, irrespective of any nonunique constants attached to the redundant list.

Write $X_j=\sum_\ell C_{j\ell}Z_\ell$ with a constant rank-$s$ matrix $C$. The fundamental equations become

$$
\partial_{a_k}F(y,a)
=\sum_{\ell=1}^s\eta_{k\ell}(a)Z_\ell(F(y,a)),
\qquad \eta=\psi C.
\tag{6.3}
$$

The matrix $\eta$ has rank $s$. Choose finitely many evaluation points $p_\nu$ at which combined evaluation of the $Z_\ell$ is injective. It remains injective at the tuple $F(p_\nu,a)$ when $a$ is sufficiently near $a_0$. Therefore the finite evaluation map $a\mapsto(F(p_\nu,a))_\nu$ has rank exactly $s$: its differential factors through $\eta$ and this injective evaluation map.

Choose $s$ scalar components $u(a)$ of that evaluation map with independent differentials. Complete them by $r-s$ original parameter coordinates $v$ so that $(u,v)$ is an analytic coordinate chart, using the inverse-function theorem. The kernel of $du$ equals the kernel of the full evaluation differential, since both have rank $s$ and the former components were selected from the latter. In particular, differentiating at fixed $u$ in a $v$ direction makes every evaluated component zero. Equation (6.3) and injectivity at the transformed tuple then force the coefficients of all the $Z_\ell$ in that derivative to vanish. The derivative of $F(y,a)$ in that direction is consequently zero for every $y$. On a smaller coordinate box, $F$ depends only on $u$.

Fixing $v=v_0$ leaves fundamental equations for this reduced family with an invertible $s$-by-$s$ coefficient matrix: its evaluated differential still has rank $s$, and the same injective evaluation factor detects the coefficient rank. It contains the identity at $u=u(a_0)$. Proposition 6.1 applies with the independent generators $Z_\ell$, giving the claimed effective local group. If $s=0$, (6.3) says directly that $F$ is the identity throughout the connected parameter box. $\square$

The original unnormalized family may be a translate of this effective group. The reduction does not turn arbitrary lifted constants for a dependent list into an abstract Lie algebra; it uses the bracket algebra of the actual fields.

**Example 6.1 (variable coefficients in a redundant frame).** Take
$F(x,a,b)=x+a+b+ab$ near $(a,b)=(0,0)$, with $X_1=X_2=\partial_x$ and $\psi=\operatorname{diag}(1+b,1+a)$. The fundamental equations hold, and $\psi$ is invertible. Its related parameter frame is

$$
B_1=\frac{1}{1+b}\partial_a,\qquad
B_2=\frac{1}{1+a}\partial_b,\qquad
[B_1,B_2]=\frac{B_1-B_2}{(1+a)(1+b)}.
\tag{6.4}
$$

The bracket coefficients of this frame vary with the parameters; their spatial image is zero because the two generators agree. The coordinates $u=a+b+ab$, $v=b$ have Jacobian determinant $1+b$. They reduce the family to $F(x,u)=x+u$, the effective translation group. This exhibits precisely why constant independence was needed to force the parameter coefficients themselves to be constant in Proposition 6.1.

## 7. Exercises

**Exercise 1 (introductory).** Compute all brackets in the basis $P=\partial_x$, $D=x\partial_x$, $K=x^2\partial_x$ of the projective line algebra.

**Exercise 2 (intermediate).** Construct the transformations generated by $P,D$, using both first-kind and ordered-product canonical coordinates.

**Exercise 3 (intermediate).** Verify all cross brackets in Example 4.1. Identify which flows multiply on which side.

**Exercise 4 (intermediate).** For upper unitriangular $3\times3$ matrices, derive the group law and invariant frame and show that it realizes the Heisenberg algebra.

**Exercise 5 (advanced).** In the proof of Theorem 3.1, justify the finite evaluation tuple and prove the action law from uniqueness of integral graphs, without assuming the abstract third theorem.

## 8. Solutions

**Solution 1.** The formula $[f\partial_x,g\partial_x]=(fg'-gf')\partial_x$ gives $[P,D]=P$, $[P,K]=2D$, and $[D,K]=K$. Reverse-order brackets are their negatives, and self brackets are zero.

**Solution 2.** Ordered flows give $\Phi_D^s\circ\Phi_P^t(x)=e^s(x+t)$. Thus every affine map near the identity has this form, with slope $e^s$ and intercept $e^st$. First-kind coordinates use $(a+bx)\partial_x$, whose time-one flow is $e^b x+a(e^b-1)/b$, with value $x+a$ at $b=0$ by analytic continuation of $(e^b-1)/b$. Its derivative in $(a,b)$ at zero is $1,x$, so the parameters are essential.

**Solution 3.** $[E_1,C_1]=0$ and $[E_2,C_1]=0$ follow by differentiating coefficients. For $C_2=\alpha\partial_\beta$, the two contributions to $[E_1,C_2]$ are $\alpha\partial_\beta$ from differentiating $\alpha$ and $-\alpha\partial_\beta$ from differentiating $\beta$, so they cancel. Also $[E_2,C_2]=0$. The $E$ fields are left-invariant and flow by right multiplication; the $C$ fields are right-invariant and flow by left multiplication, as follows by differentiating the products in each variable.

**Solution 4.** Write the matrix as $U(x,y,z)=\bigl(\begin{smallmatrix}1&x&z\\0&1&y\\0&0&1\end{smallmatrix}\bigr)$. Matrix multiplication gives

$$
(x,y,z)(u,v,w)=(x+u,y+v,z+w+xv).
$$

Differentiating in the second factor at zero gives the left-invariant fields $E_x=\partial_x$, $E_y=\partial_y+x\partial_z$, $E_z=\partial_z$. Their only nonzero basis bracket is $[E_x,E_y]=E_z$. The inverse is $(-x,-y,-z+xy)$ by substitution. Right translations of this group supply the right action with these generators.

**Solution 5.** Each added evaluation strictly reduces the kernel, because a nonzero analytic field in that kernel is nonzero at some point. Dimension therefore forces termination. On the resulting integral leaf, the diagonal fields are an actual frame. The product distribution $(E_i,X_i)$ has constant brackets and projects isomorphically to the parameter leaf, giving unique integral graphs. A graph through $(o,x)$ reaches $(a,F_a(x))$. Because left translation preserves $E_i$, the graph from $o$ to $b$ with initial value $F_a(x)$ translates to the graph from $a$ to $m(a,b)$. It is the same leaf as the original graph, so $F_b(F_a(x))=F_{m(a,b)}(x)$. This construction uses only the complete-system theorem and analytic inverse-function theorem, both already available.

## What this lesson does not prove

An abstract finite-dimensional Lie algebra need not initially be given as analytic vector fields. Its realization, including algebras with nonzero centre, is proved in *The third fundamental theorem*. Global groups and global integration of homomorphisms require additional hypotheses and are not consequences of the local graph arguments here.

## References

- Michael Kunzinger, *Lie Transformation Groups: An Introduction to Symmetry Group Analysis of Differential Equations*, 2015, corrected December 2024, Section 3.1. [Author's text](https://www.mat.univie.ac.at/~mike/teaching/ss15/ltg.pdf).
- Sophus Lie, with Friedrich Engel, *Theorie der Transformationsgruppen*, Volume I, 1888, Chapters 9 and 21.
- Joël Merker, *Theory of Transformation Groups, by S. Lie and F. Engel (Vol. I, 1888): Modern Presentation and English Translation*, 2010, chapters on characteristic relationships and the group of parameters. [Author's preprint](https://arxiv.org/abs/1003.3202).

