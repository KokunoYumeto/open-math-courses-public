# The adjoint group, composition and isomorphism

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI, GPT-6.1 Sol (OpenAI), in Codex at Ultra. Public domain (CC0).*

A transformation group has two kinds of structure. It moves points of a manifold, and it moves its own infinitesimal directions by conjugation. The second action is linear. It detects the centre, makes normal subgroups visible as invariant subspaces, and connects transformation groups with triangular matrices.

We use finite-dimensional analytic local groups over $\mathbb K=\mathbb R$ or $\mathbb C$. Their Lie algebra is the space of left-invariant vector fields, evaluated at the identity. The existence and uniqueness results of The third fundamental theorem are available. All subgroup and quotient statements concern connected germs at the identity. The linear algebra theorem of Lie requires $\mathbb K=\mathbb C$; Engel's theorem works over either field.

## 1. Conjugation and the adjoint representation

For a group element $a$ near the identity, set

$$
C_a(b)=aba^{-1},\qquad
\operatorname{Ad}_a=(dC_a)_e:\mathfrak g\longrightarrow\mathfrak g.
\tag{1.1}
$$

Locality means that these formulas are used on a smaller common neighbourhood where the indicated products exist. Since $C_aC_b=C_{ab}$, differentiation gives

$$
\operatorname{Ad}_{ab}=\operatorname{Ad}_a\operatorname{Ad}_b.
\tag{1.2}
$$

Every group automorphism carries a left-invariant field to the left-invariant field with the transformed value at $e$. Diffeomorphisms preserve brackets. Therefore $\operatorname{Ad}_a$ is a Lie algebra automorphism.

**Lemma (matrix exponential and logarithm).** In a neighbourhood of zero in the space of real or complex square matrices, the absolutely convergent series

$$
\exp A=\sum_{j=0}^{\infty}\frac{A^j}{j!},\qquad
\log(I+B)=\sum_{j=1}^{\infty}\frac{(-1)^{j+1}}{j}B^j
$$

are inverse analytic maps. If $I+B$ preserves a linear subspace and $\|B\|<1$ in a submultiplicative norm, its logarithm preserves that subspace too.

**Proof.** The exponential converges absolutely for every $A$; the logarithm does so for $\|B\|<1$, locally uniformly with derivatives. For scalars, put
$\ell(z)=\sum_{j\ge1}(-1)^{j+1}z^j/j$. Termwise differentiation gives $\ell'(z)=1/(1+z)$. Thus $\exp(\ell(z))/(1+z)$ has derivative zero and value one at zero, proving $\exp(\ell(z))=1+z$. Also $\ell(\exp z-1)$ has derivative one and value zero near zero, proving $\ell(\exp z-1)=z$.

These are identities of convergent power series. Substitute a single matrix in each identity. All its powers commute, and absolute convergence justifies regrouping their products. On a sufficiently small matrix ball the scalar majorants also bound each composition, giving $\exp(\log(I+B))=I+B$ and $\log(\exp A)=A$. No commutativity of different matrices is required.

If $I+B$ preserves a subspace, so does $B=(I+B)-I$, hence every power of $B$ and every partial sum of its logarithm. A finite-dimensional subspace is closed, so the limit preserves it. $\square$

**Theorem 1.1.** The differential of $\operatorname{Ad}$ is

$$
\operatorname{ad}_u(v)=[u,v].
\tag{1.3}
$$

Moreover, the kernel of $\operatorname{Ad}$ near $e$ is the central subgroup germ $\exp Z(\mathfrak g)$. Its image has $\dim\mathfrak g-\dim Z(\mathfrak g)$ essential parameters. In particular, the adjoint representation is locally faithful exactly when $Z(\mathfrak g)=0$.

**Proof.** Let $U$ be the left-invariant field with value $u$. Its flow on the parameter group is $b\mapsto b\exp(tu)$. For any field $V$, the flow identity

$$
\left.\frac d{dt}\right|_{0}(\Phi_U^{-t})_*V=[U,V]
\tag{1.4}
$$

follows by differentiating $D\Phi_U^{-t}\,V\circ\Phi_U^t$ in coordinates. If $V$ is left-invariant, evaluate the right-hand side at $e$. The left-hand side there is the derivative of $\operatorname{Ad}_{\exp(tu)}v$: right translation by $\exp(-tu)$ carries the value of $V$ at $\exp(tu)$ to the derivative of conjugation. This proves (1.3). The one-parameter homomorphism (1.2) now solves a constant linear ODE, so

$$
\operatorname{Ad}_{\exp(tu)}=e^{t\operatorname{ad}_u}.
\tag{1.5}
$$

The group exponential is a local coordinate map at zero, by the canonical-coordinate construction in lesson 3. For $u$ sufficiently small, $e^{\operatorname{ad}_u}=I$ implies $\operatorname{ad}_u=0$ by the matrix logarithm lemma. Thus the kernel is exactly $\exp Z(\mathfrak g)$ near $e$.

If $\operatorname{Ad}_a=I$, conjugation fixes every $\exp(tu)$ by uniqueness of its one-parameter group. These exponentials fill a neighbourhood of $e$, so $a$ commutes with all nearby elements. The converse follows immediately from (1.1). Finally the differential of $\operatorname{Ad}$ has kernel $Z(\mathfrak g)$. Translations and (1.2) make its rank constant. The constant-rank theorem proved in lesson 1, Theorem B, gives the stated image dimension and essential parameter count. $\square$

The word **locally** matters. A connected global group can have a discrete nontrivial centre even when its Lie algebra has zero centre; $\operatorname{SL}_2(\mathbb R)$ has the central elements $I$ and $-I$. A local chart about $I$ excludes $-I$. Also, in the right-action convention used in earlier lessons, the pushforward of a fundamental field by a point transformation $T_a$ corresponds to $\operatorname{Ad}_{a^{-1}}$, not $\operatorname{Ad}_a$. Definition (1.1) fixes the convention independently of that choice.

**Example 1.2: rotations.** Identify $\mathfrak{so}(3)$ with $\mathbb R^3$ by $v\mapsto A_v$, where $A_vw=v\times w$. Then

$$
RA_vR^{-1}=A_{Rv},\qquad [A_u,A_v]=A_{u\times v}.
$$

The first identity follows because rotations preserve the cross product. If $u\times v=0$ for every $v$, then $u=0$. The adjoint group is therefore the usual faithful rotation group on $\mathbb R^3$.

**Example 1.3: the Heisenberg group.** In the exponential coordinates of lesson 6,

$$
(x,y,z)(u,v,w)=(x+u,y+v,z+w+\tfrac12(xv-yu)).
$$

Its algebra has $[e_x,e_y]=e_z$ and all other basis brackets zero. Hence

$$
\operatorname{Ad}_{(x,y,z)}e_x=e_x-ye_z,\qquad
\operatorname{Ad}_{(x,y,z)}e_y=e_y+xe_z,\qquad
\operatorname{Ad}_{(x,y,z)}e_z=e_z.
$$

The parameter $z$ disappears. The kernel is the central line, and the adjoint image is a two-dimensional abelian group. An adjoint group can itself have a centre.

## 2. Subgroups, ideals, and quotient groups

A linear subspace $\mathfrak h\subset\mathfrak g$ is a **subalgebra** when $[\mathfrak h,\mathfrak h]\subset\mathfrak h$. It is an **ideal** when $[\mathfrak g,\mathfrak h]\subset\mathfrak h$. A subgroup is **normal**, or invariant in Lie's terminology, when nearby conjugations preserve its germ.

**Theorem 2.1.** Subalgebras correspond bijectively to connected local subgroup germs. Under this correspondence, ideals correspond exactly to normal subgroup germs.

**Proof.** Translate $\mathfrak h$ to the distribution $D_a=(dL_a)_e\mathfrak h$ on the parameter group. The left-invariant fields belonging to a basis of $\mathfrak h$ span $D$. Their brackets remain in $D$, so Frobenius gives a unique leaf germ $H$ through $e$.

Left translations preserve $D$. For $a\in H$, the leaf through $a$ is $H$, hence $L_a$ carries the germ of $H$ into that leaf. This proves closure under sufficiently small products. The ordered flows of a basis of $\mathfrak h$ give coordinates on $H$; they are products of exponentials $\exp(tu)$ with $u\in\mathfrak h$. Their inverses are reversed products of $\exp(-tu)$, which also lie in $H$. Thus $H$ is a subgroup germ with tangent algebra $\mathfrak h$.

Conversely, the left-invariant fields tangent to a subgroup are closed under brackets because brackets of tangent fields are tangent. A connected subgroup germ with tangent algebra $\mathfrak h$ is an integral leaf of $D$, so uniqueness of that leaf proves the bijection.

If $\mathfrak h$ is an ideal, every $\operatorname{ad}_u$ preserves it. Equation (1.5) shows that conjugation by $\exp(tu)$ preserves its tangent algebra, and consequently its unique subgroup germ. Products of small exponentials fill the parameter group; hence $H$ is normal. Conversely, normality gives $\operatorname{Ad}_a\mathfrak h=\mathfrak h$. Differentiate along $a=\exp(tu)$ to obtain $[u,\mathfrak h]\subset\mathfrak h$. $\square$

For an ideal $\mathfrak i$, define the quotient bracket by

$$
[u+\mathfrak i,v+\mathfrak i]=[u,v]+\mathfrak i.
\tag{2.1}
$$

Changing either representative changes the bracket by an element of $\mathfrak i$, so this is well defined. Skew symmetry and Jacobi pass to the quotient.

**Theorem 2.2.** Every Lie algebra homomorphism $f:\mathfrak g\to\mathfrak q$ integrates uniquely to a local group homomorphism $F:G\to Q$. If $f$ is surjective, $F$ is a submersion and its kernel is the subgroup germ with algebra $\ker f$. In particular, $G/I$ is a local group with algebra $\mathfrak g/\mathfrak i$ when $I$ corresponds to an ideal $\mathfrak i$.

**Proof.** On $G\times Q$, take the distribution spanned by

$$
(U_u,U_{f(u)}),\qquad u\in\mathfrak g,
$$

where both fields are left-invariant. The homomorphism identity makes this distribution involutive. Projection onto $G$ is an isomorphism on each of its tangent spaces. Its Frobenius leaf through $(e,e)$ is therefore the graph of an analytic map $F$, and

$$
dF(U_u)=U_{f(u)}\circ F,\qquad F(e)=e.
\tag{2.2}
$$

These equations determine $F$ uniquely along successive basis flows, and those flows give local coordinates. Fix $a\in G$. The maps $b\mapsto F(ab)$ and $b\mapsto F(a)F(b)$ have the same value at $e$ and satisfy the same equations (2.2) in $b$, because left translations preserve left-invariant fields. The same uniqueness proves $F(ab)=F(a)F(b)$.

The rank of $dF$ equals the rank of $f$ everywhere by (2.2). Surjectivity gives a submersion. Its identity fibre is a subgroup germ with tangent algebra $\ker f$, hence is the subgroup already constructed in Theorem 2.1. Apply this to the projection $\mathfrak g\to\mathfrak g/\mathfrak i$, using the local existence theorem to construct $Q$. The fibres of $F$ are precisely local cosets of $I$: $F(a)=F(b)$ is equivalent to $a^{-1}b\in I$. Thus $Q$ realizes the local quotient. $\square$

The first isomorphism theorem is now transparent: $\mathfrak g/\ker f\simeq\operatorname{im}f$, by $u+\ker f\mapsto f(u)$. The map is well defined, bijective, and bracket preserving. Historically, an isomorphism was called *holoedric*, while a quotient relationship was called *meroedric*. These terms do not assert that distinct actions with the same algebra are conjugate: isotropy must also be considered.

## 3. Solvability and nilpotence

Define the derived series and the lower central series by

$$
\mathfrak g^{(0)}=\mathfrak g,\quad
\mathfrak g^{(j+1)}=[\mathfrak g^{(j)},\mathfrak g^{(j)}],
\qquad
\gamma_1\mathfrak g=\mathfrak g,\quad
\gamma_{j+1}\mathfrak g=[\mathfrak g,\gamma_j\mathfrak g].
\tag{3.1}
$$

Brackets of subspaces mean their linear spans. Jacobi shows that all these spaces are ideals: if $I$ is an ideal, then $[a,[u,v]]=[[a,u],v]+[u,[a,v]]$ belongs to $[I,I]$ when $u,v\in I$. The same calculation applies to $[\mathfrak g,I]$.

The algebra is **solvable** if its derived series reaches zero, and **nilpotent** if its lower central series reaches zero. Nilpotence implies solvability, since repeated derived terms lie in successively deeper lower central terms. Lie's historical “integrable” groups refer here to solvable groups, not to every group admitting a local integral action.

For $[h,e]=e$, the affine algebra has derived algebra $\mathbb K e$, whose own bracket is zero. It is solvable. Its lower central series stays $\mathbb K e$ after the first step, so it is not nilpotent. The Heisenberg algebra has $\gamma_2=\mathbb K e_z$ and $\gamma_3=0$.

Upper triangular matrices are solvable. A commutator has zero diagonal, so the first derived algebra is strictly upper triangular. A product of $n$ strictly upper triangular $n\times n$ matrices is zero: every nonzero entry of a product requires a strictly increasing chain of $n+1$ indices. Iterated brackets are sums of such products. This also proves that a subalgebra of strictly upper triangular matrices is nilpotent.

## 4. Engel's theorem

**Theorem 4.1 (Engel).** If a Lie algebra $L\subset\operatorname{End}(V)$ consists entirely of nilpotent operators, there is a basis $v_1,\ldots,v_n$ such that

$$
L v_j\subset\operatorname{span}(v_1,\ldots,v_{j-1}).
\tag{4.1}
$$

Thus all its matrices are strictly upper triangular. A finite-dimensional abstract Lie algebra is nilpotent if and only if every $\operatorname{ad}_u$ is nilpotent.

**Proof.** First prove that $L$ annihilates a common nonzero vector whenever $V\ne0$. Induct on $\dim L$, allowing an arbitrary representation with nilpotent image by replacing the algebra with its image. Dimension zero is immediate.

For a nilpotent operator $a$ with $a^d=0$, the operator $\operatorname{ad}_a$ on $\operatorname{End}(V)$ is nilpotent. Indeed,

$$
(\operatorname{ad}_a)^m T=
\sum_{j=0}^m(-1)^j\binom mj a^{m-j}Ta^j,
$$

which vanishes when $m\ge2d-1$. Let $H$ be a proper subalgebra of $L$. The adjoint action of $H$ on $L/H$ is well defined and consists of nilpotent operators. Its image has dimension at most $\dim H<\dim L$, so the induction hypothesis gives a nonzero class $b+H$ killed by $H$. In other words, $b\notin H$ and $[H,b]\subset H$. Consequently the normalizer of every proper subalgebra strictly contains it.

Choose $H$ maximal among proper subalgebras. Its normalizer must be $L$, so $H$ is an ideal. Also $L/H$ has dimension one: otherwise the inverse image of any nonzero one-dimensional subalgebra of $L/H$ would lie strictly between $H$ and $L$. Write $L=H+\mathbb K b$.

By induction, $W=\{v:Hv=0\}$ is nonzero. For $a\in H$ and $w\in W$,

$$
a(bw)=b(aw)+[a,b]w=0.
$$

Thus $bW\subset W$. The nilpotent operator $b|_W$ has a nonzero kernel; a vector in this kernel is annihilated by all of $L$. This completes the induction.

Take that vector as $v_1$ and apply the result to $V/\mathbb K v_1$. Every induced operator remains nilpotent. Repeating constructs the full flag (4.1).

For an abstract algebra with nilpotent adjoint operators, apply (4.1) to its adjoint representation on $\mathfrak g$. A product of $\dim\mathfrak g$ adjoint operators is zero, so every nested bracket of that depth vanishes and the lower central series terminates. Conversely, if $\gamma_{s+1}\mathfrak g=0$, each application of $\operatorname{ad}_u$ moves a vector one step deeper in the lower central series; hence $(\operatorname{ad}_u)^s=0$. $\square$

Nilpotence of a basis of $L$ would not suffice: the hypothesis applies to **every** element. For instance $E_{12}$ and $E_{21}$ are individually nilpotent, but their sum is invertible on $\mathbb K^2$ and their bracket is diagonal.

## 5. Lie's theorem

**Theorem 5.1 (Lie).** Every representation of a solvable complex Lie algebra on a nonzero finite-dimensional complex vector space has a common eigenvector. It has an invariant full flag, and therefore all its matrices are upper triangular in a single basis.

**Proof.** Prove the common-eigenvector assertion by induction on the dimension of the algebra $L$. Dimension zero is trivial. For $L\ne0$, solvability gives $[L,L]\ne L$. Choose a codimension-one subspace containing $[L,L]$; it is an ideal $H$. Write $L=H\oplus\mathbb C b$. The restriction to $H$ has a common eigenvector $v\ne0$ by induction. Thus there is a linear functional $\lambda:H\to\mathbb C$ with $av=\lambda(a)v$.

We claim that $\lambda([a,b])=0$ for all $a\in H$. Let

$$
W_j=\operatorname{span}(v,bv,\ldots,b^jv),\qquad
W=\operatorname{span}(v,bv,b^2v,\ldots).
$$

The space $W$ is finite dimensional and $b$-invariant. Simultaneously for every $a\in H$, induction on $j$ gives

$$
a b^jv-\lambda(a)b^jv\in W_{j-1}.
\tag{5.1}
$$

For $j=0$ this is the eigenvector equation. For the next step use $ab=ba+[a,b]$; both $a$ and $[a,b]$ belong to $H$, so the induction hypothesis controls their action on $b^jv$. Until the first linear dependence, $v,bv,\ldots,b^{m-1}v$ is a basis of $W$, where $m=\dim W$. Equation (5.1) shows that $H$ preserves $W$ and every $a|_W$ has the constant diagonal $\lambda(a)$. In particular,

$$
m\lambda([a,b])=\operatorname{tr}([a,b]|_W)
=\operatorname{tr}(a|_Wb|_W-b|_Wa|_W)=0.
$$

Characteristic zero gives the claim.

Now let $V_\lambda=\{w:aw=\lambda(a)w\text{ for every }a\in H\}$. It contains $v$. For $w\in V_\lambda$,

$$
a(bw)=b(aw)+[a,b]w=\lambda(a)bw.
$$

Therefore $b$ preserves $V_\lambda$. Over $\mathbb C$, $b|_{V_\lambda}$ has an eigenvector; that vector is a common eigenvector of $H$ and $b$, hence of $L$.

Its line is invariant. Apply the same assertion to the quotient by that line and repeat, obtaining an invariant full flag. Choosing a basis adapted to the flag makes every operator upper triangular. $\square$

The trace step explains the characteristic-zero hypothesis. Algebraic closure is used to find the final eigenvector. Over $\mathbb R$, the one-dimensional abelian algebra generated by

$$
\begin{pmatrix}0&-1\\1&0\end{pmatrix}
$$

is solvable but has no real invariant line. There is no real triangularization in that example.

## 6. Similarity and reciprocal groups

Two local transformation actions are **similar** when an analytic change of point coordinates conjugates one to the other, allowing a corresponding change of group parameters. An action is **simply transitive** near $p$ when its orbit map $a\mapsto p\cdot a$ is a local diffeomorphism. Equivalently, its generators form a pointwise basis near $p$ and the group and manifold have the same dimension.

**Theorem 6.1.** Simply transitive local actions with isomorphic Lie algebras are similar. The local transformations commuting with a simply transitive action form a reciprocal simply transitive group.

**Proof.** Let $F:G\to Q$ be the local group isomorphism integrating an algebra isomorphism, by Theorem 2.2 and the inverse-function theorem. Choose points $p\in M$, $q\in N$. Their orbit maps $\theta_M$ and $\theta_N$ are local diffeomorphisms. Set

$$
\Psi=\theta_N\circ F\circ\theta_M^{-1}.
$$

For $x=\theta_M(a)$, the right-action law gives

$$
\Psi(x\cdot b)=\theta_N(F(ab))
=\theta_N(F(a)F(b))=\Psi(x)\cdot F(b).
$$

This is the required conjugacy.

Use $\theta_M$ to identify $M$ with the parameter group, so the action consists of right translations $R_b(a)=ab$. A local map $S$ commuting with every sufficiently small $R_b$ must satisfy

$$
S(b)=S(R_b(e))=R_b(S(e))=S(e)b.
$$

Thus $S=L_c$ with $c=S(e)$. Conversely, every left translation commutes with every right translation, by associativity. The left translations are parametrized by $c$, and their orbit map at $e$ is $c\mapsto c$, so they are simply transitive. $\square$

As parameterized families of diffeomorphisms, $L_c\circ L_d=L_{cd}$ while $R_c\circ R_d=R_{dc}$. The reciprocal families therefore have opposite parameter multiplication if their parameters are labeled identically. Relabeling a right translation by $c^{-1}$ makes its multiplication the same as that of the left translations. This is the precise sense of “the same composition” in the reciprocal-group statement. Their infinitesimal left- and right-invariant frames commute with each other and have opposite bracket signs, as computed in lesson 5.

### Regular centralizers

The **centralizer** fixes every transformation under conjugation; the **normalizer** preserves the whole group as a set. The infinitesimal centralizer of fields $X_1,\ldots,X_r$ consists of analytic fields $Z$ with $[X_a,Z]=0$ for every $a$. It can be infinite-dimensional even when the given group is finite-dimensional.

**Theorem 6.2 (the regular centralizer).** Let $X_1,\ldots,X_r$ be independent over constants, satisfy constant bracket relations, and have constant pointwise rank $n$ on an $s$-dimensional analytic neighborhood. Choose $X_1,\ldots,X_n$ pointwise independent and write

$$
X_{n+k}=\sum_{\rho=1}^{n}\varphi_{k\rho}(x)X_\rho,
\qquad 1\le k\le r-n.
\tag{6.1}
$$

Suppose the full array of functions $\varphi_{k\rho}$ has constant functional rank $m$. After shrinking the neighborhood, there are $q=s-m$ pointwise independent fields $Z_1,\ldots,Z_q$, each centralizing all the $X_a$. Every field in the infinitesimal centralizer has a unique expression

$$
Z=\sum_{\alpha=1}^{q}h_\alpha(u_1,\ldots,u_{s-n})Z_\alpha,
\tag{6.2}
$$

where $u_1,\ldots,u_{s-n}$ are local independent orbit invariants and the $h_\alpha$ are arbitrary analytic functions. In particular, the centralizer is zero when $m=s$, and has dimension $s-m$ over constants when the action is transitive. When $r=n$, the coefficient array is empty and $m=0$.

**Proof.** For a tangent vector $z$ at $x$, lift each field to the tangent bundle by

$$
W_a(x,z)=\bigl(\xi_a(x),D\xi_a(x)z\bigr),
\qquad X_a(x)=\xi_a(x).
\tag{6.3}
$$

Differentiating both components gives $[W_a,W_b]=W_{[X_a,X_b]}$. The second component is the derivative of the first bracket in the direction $z$: differentiating $\xi_a^j\partial_j\xi_b^i-\xi_b^j\partial_j\xi_a^i$ supplies exactly its Hessian and product terms. Thus the lifts have the same constant structure relations. The graph of a field $Z(x)=\zeta(x)$ is invariant under $W_a$ exactly when

$$
D\zeta(x)\xi_a(x)=D\xi_a(x)\zeta(x),
\tag{6.4}
$$

which is $[X_a,Z]=0$.

Define the analytic kernel bundle

$$
K_x=\bigcap_{k,\rho}\ker d\varphi_{k\rho}(x).
\tag{6.5}
$$

The constant-rank hypothesis makes its rank $q=s-m$; a nonzero minor supplies an analytic frame by solving the corresponding linear equations. From (6.1),

$$
[X_{n+k},Z]
=\sum_\rho\varphi_{k\rho}[X_\rho,Z]
-\sum_\rho Z(\varphi_{k\rho})X_\rho.
\tag{6.6}
$$

Consequently $Z$ commutes with every generator if and only if it commutes with the first $n$ and takes values in $K$.

We must show that these algebraic conditions permit every initial value in $K$. Let $\mathfrak a$ be the constant coefficient space of the generators, and let $\mathfrak a_x$ be the kernel of evaluation $\mathfrak a\to T_xM$. A basis of that kernel is

$$
B_k(x)=e_{n+k}-\sum_\rho\varphi_{k\rho}(x)e_\rho.
\tag{6.7}
$$

The flow $\Phi_t$ of any $X_b$ transports the generator space by a constant invertible linear map. Indeed, the flow identity (1.4), applied to this finite-dimensional span, gives a constant linear ODE for the coefficients of $(\Phi_t)_*X_a$. It follows that $\mathfrak a_{\Phi_t(x)}$ is obtained from $\mathfrak a_x$ by that fixed linear map. In the kernel chart (6.7), the new coefficient array is therefore an analytic function of the old array alone; solving for it uses an invertible minor. Its derivative in any direction $z\in K_x$ is zero. Hence

$$
D\Phi_t(x)K_x=K_{\Phi_t(x)}.
\tag{6.8}
$$

This proves that the tangent lifts preserve $K$. On this bundle,

$$
W_{n+k}-\sum_\rho\varphi_{k\rho}W_\rho
=\left(0,\sum_\rho(d\varphi_{k\rho}z)\xi_\rho\right)=0.
\tag{6.9}
$$

The lifted distribution on $K$ is therefore involutive of rank $n$, and its projection is an isomorphism onto the rank-$n$ orbit distribution. The analytic Frobenius theorem proved in Complete systems and invariants, §2 gives local lifted leaves.

Choose an $(s-n)$-dimensional transversal $T$ to the orbit plaques. A lifted leaf through a vector of $K|_T$ projects locally diffeomorphically to the associated plaque. Uniqueness of the Frobenius leaf makes its lift unambiguous. Equivalently, use the orbit coordinates supplied by Frobenius and compose the corresponding horizontal coordinate flows. This transports the vector to each point of the plaque. The transport is linear and invertible, since its fiber equation is a homogeneous linear ODE and the reverse path gives its inverse.

Choose an analytic basis of $K|_T$ and transport it. This gives pointwise independent fields $Z_1,\ldots,Z_q$ whose graphs are invariant under the lifts, so they commute with all generators by (6.4) and (6.6). Every commuting field is determined by its arbitrary analytic initial section on $T$. The first-integral coordinates $u$ label the plaques, by Complete systems and invariants, Theorem 3.2. Expanding its initial section in that basis proves (6.2), including uniqueness. Conversely, $X_a h_\alpha(u)=0$, so every expression (6.2) commutes with the generators.

When $n=s$, the transversal is a point and the coefficients are constants. When $q=0$, the initial fiber is zero. These prove the remaining conclusions. $\square$

If the given algebra is zero, every analytic field centralizes it; (6.2) then holds with $n=m=0$, all $s$ coordinates as invariants, and the coordinate frame as the $Z_\alpha$. In general, Jacobi implies that $[Z_\alpha,Z_\beta]$ again centralizes the given algebra. Its coefficients in the frame are first integrals, so they can vary with $u$ when the action is intransitive; the centralizing frame itself can have nonzero brackets.

**Example 6.3.** On the plane, $X_1=\partial_x$ and $X_2=y\partial_x$ have $r=2$, $n=1$ and $\varphi=y$, so $m=1$ and $q=1$. A field commuting with $\partial_x$ has the form $f(y)\partial_x+g(y)\partial_y$. Its bracket with $y\partial_x$ is $-g(y)\partial_x$, forcing $g=0$. The full centralizer is therefore $f(y)\partial_x$: one arbitrary function of one invariant. Adding $X_3=\partial_y$ makes the action transitive and forces $f$ to be constant. Adding both translations and the Euler field instead gives a transitive action with zero centralizer.

### Invariant foliations and reciprocal subgroups

**Theorem 6.4.** For a simply transitive local action of dimension $n$, its invariant regular foliations of dimension $m$ correspond bijectively to the connected $m$-dimensional local subgroups of its reciprocal action. If $0<m<n$, these are precisely its regular systems of imprimitivity. Every such action with $n>1$ is imprimitive.

In the group coordinates of Theorem 6.1, where the given action consists of right translations, let $H$ be the subgroup corresponding to a foliation. Its leaves are the right cosets $Hp$. The subgroup of the given action preserving the fixed leaf $Hp$ has parameters $p^{-1}Hp$; the reciprocal subgroup preserving that leaf, and every leaf of the family, has parameters $H$. The two transformation subgroups correspond under an isomorphism of the full reciprocal transformation groups.

**Proof.** Let $D$ be the foliation's regular tangent distribution. Right-translation invariance gives

$$
D_p=(dR_p)_eD_e.
\tag{6.10}
$$

Set $\mathfrak h=D_e$. Its right-invariant fields are sections of $D$. Their brackets are right-invariant fields with the negative algebra bracket, as in Solution 4. Involutivity of $D$ therefore says that $\mathfrak h$ is a subalgebra. Theorem 2.1 integrates it to a connected local subgroup $H$. The distribution tangent to its right cosets $Hp$ is exactly (6.10), so its leaves agree with the given foliation, by uniqueness of integral leaves.

Conversely, every subalgebra supplies this right-invariant involutive distribution. Its right cosets form a regular local foliation, right translation permutes the cosets, and left translation by $H$ preserves each of them. The distribution at the identity recovers the subalgebra, proving uniqueness and the correspondence. Normality is not required. For $n>1$, any nonzero one-dimensional subalgebra is proper and gives a system of imprimitivity.

For a fixed leaf, cancellation of sufficiently small local products gives

$$
Hpa=Hp\ \Longleftrightarrow\ pa p^{-1}\in H,\qquad
bHp=Hp\ \Longleftrightarrow\ b\in H.
\tag{6.11}
$$

Thus the two stabilizers have dimension $m$. As transformation families, $R_a\circ R_b=R_{ba}$ and $L_a\circ L_b=L_{ab}$. The map

$$
R_a\longmapsto L_{p a^{-1}p^{-1}}
\tag{6.12}
$$

is therefore an isomorphism: the inverse and conjugation turn $ba$ into $(pa^{-1}p^{-1})(pb^{-1}p^{-1})$. It sends the first stabilizer exactly to the second. Infinitesimally it sends the left-invariant field of $u$ to the negative right-invariant field of $\operatorname{Ad}_p u$, reconciling the opposite bracket signs. All these equalities concern local germs on common domains. $\square$

More generally, if an $m$-dimensional regular manifold admits an $m$-dimensional subgroup of a simply transitive action, that subgroup's orbit through $p$ is an open piece of the manifold, by the inverse-function theorem. Write it as $pH_0=(pH_0p^{-1})p$ and apply the fixed-leaf argument with $H=pH_0p^{-1}$. This proves the reciprocal stabilizer assertion without first assuming an invariant foliation.

**Corollary 6.5.** The infinitesimal transformations common to reciprocal simply transitive groups are their central fields, and the two groups have the same local normalizer.

**Proof.** Membership in the reciprocal algebra means commuting with every field of the first algebra. Their intersection is consequently the centre of the first algebra, and mutual reciprocity makes it the centre of the second as well. A local diffeomorphism carries a centralizer to the centralizer of the transported algebra, because it preserves brackets. Normalizing either algebra therefore normalizes the other; reversing the argument proves equality of the normalizers. The connected local groups are generated by their flows, so the same conclusion holds for those group germs. $\square$

**Example 6.6.** In the Heisenberg coordinates of Example 1.3, take $H$ generated by $e_x$. Its right cosets are

$$
y=y_0,\qquad z-\tfrac12y_0x=\text{constant}.
\tag{6.13}
$$

Their tangent field is $V_x=\partial_x+\tfrac12y\partial_z$. The given right-translation action is generated by the left-invariant fields $U_x,U_y,U_z$ of Solution 4, and all commute with $V_x$. The subgroup is not normal because $[e_y,e_x]=-e_z$. At $p=(0,c,0)$ the subgroup preserving the fixed leaf in the given action has algebra $\mathbb K(e_x+ce_z)$, while the reciprocal subgroup preserving every leaf has algebra $\mathbb K e_x$. Conjugation gives

$$
p^{-1}(t,0,0)p=(t,0,ct).
\tag{6.14}
$$

This also shows why single-leaf stabilizers need not have the same basis direction at a nonidentity base point. For $n=1$, no dimension satisfies $0<m<n$, so the imprimitivity conclusion has no one-dimensional version.

## 7. Exercises

**Exercise 1 (easy).** For $[h,e]=e$, compute the matrices of $\operatorname{ad}_h$ and $\operatorname{ad}_e$ in the ordered basis $(h,e)$, and determine the centre.

**Exercise 2 (medium).** Compute the derived and lower central series of the affine algebra, and identify its connected normal subgroup in the action $x\mapsto\alpha x+\beta$ with $\alpha>0$.

**Exercise 3 (medium).** Prove the abstract conclusion of Engel's theorem directly for $\dim\mathfrak g\le3$, using the nonzero centre established by the common-zero-vector part of its proof. Identify the possible nonabelian nilpotent algebra in dimension three.

**Exercise 4 (medium).** On the Heisenberg group, compute the left- and right-invariant fields associated to $e_x,e_y,e_z$. Verify that the two triples commute with each other and have opposite internal brackets. Explain the composition convention of the reciprocal groups.

**Exercise 5 (hard).** In the proof of Lie's theorem, justify (5.1) explicitly for every $j$, then complete the argument for a representation that is not faithful. Deduce that the derived algebra of any solvable complex matrix algebra consists of nilpotent matrices.

**Exercise 6 (medium).** Determine the full local analytic infinitesimal centralizer of each plane action below. Give the orbit rank $n$, coefficient rank $m$, centralizing-frame rank $q$, and the number of free functions or constants:

$$
\begin{aligned}
&\text{(a)}\quad \partial_x;\\
&\text{(b)}\quad \partial_x,\ y\partial_x;\\
&\text{(c)}\quad \partial_x,\ y\partial_x,\ \partial_y;\\
&\text{(d)}\quad \partial_x,\ \partial_y,\ x\partial_x+y\partial_y.
\end{aligned}
$$

**Exercise 7 (hard).** Consider the two triples of vector-field coefficients on three-dimensional space

$$
\begin{aligned}
X_1&=(1,0,y),&X_2&=(x,0,z),&X_3&=(x^2,xy-z,xz),\\
Z_1&=(0,1,x),&Z_2&=(0,y,z),&Z_3&=(xy-z,y^2,yz).
\end{aligned}
$$

Find their determinants and internal brackets, and verify all mixed brackets. Identify where they are reciprocal simply transitive actions. Describe their ranks and orbits on $z=xy$, and exhibit a projective transformation interchanging the triples.

**Exercise 8 (hard).** For the Heisenberg group of Example 1.3, let $H$ be generated by $e_x$. Find the foliation by right cosets of $H$, prove that the given right-translation action preserves it, and decide whether $H$ is normal. For $p=(0,c,0)$, find both subgroups preserving the fixed leaf $Hp$ and write an isomorphism of the full reciprocal transformation groups carrying one stabilizer to the other.

## 8. Solutions

**Solution 1.** Columns are images of the ordered basis vectors, so

$$
\operatorname{ad}_h=\begin{pmatrix}0&0\\0&1\end{pmatrix},\qquad
\operatorname{ad}_e=\begin{pmatrix}0&0\\-1&0\end{pmatrix}.
$$

If $ah+be$ is central, its bracket with $e$ gives $ae=0$ and its bracket with $h$ gives $-be=0$. Hence $a=b=0$. Its adjoint representation is locally faithful, although $\operatorname{ad}_e$ alone is nilpotent.

**Solution 2.** The derived series is $\mathfrak g,\mathbb K e,0$. The lower central series is $\mathfrak g,\mathbb K e,\mathbb K e,\ldots$. In the affine action, $e=\partial_x$ generates translations. They form a normal subgroup because conjugating a translation by $x\mapsto\alpha x+\beta$ gives a translation by the old amount multiplied by $\alpha$ (or its reciprocal for the opposite conjugation). The quotient is the one-dimensional dilation group. The distinction between the two series proves solvability and failure of nilpotence.

**Solution 3.** If the algebra is nonzero and every adjoint is nilpotent, the common-zero-vector argument applied to the adjoint representation gives $Z(\mathfrak g)\ne0$. The same hypothesis passes to quotients. In dimension two, quotienting by any central line leaves dimension one, so all brackets of the original algebra lie in that central line. Choose a central basis element $z$ and a complement $u$; the only possible basis bracket is $[u,z]=0$, so the algebra is abelian. Dimensions zero and one are already abelian.

In dimension three, the quotient by the whole centre has dimension at most two, and the preceding argument makes it abelian. Thus $[\mathfrak g,\mathfrak g]\subset Z(\mathfrak g)$ and $\gamma_3=0$. If the centre has dimension at least two, choose a complement of dimension at most one; every bracket then vanishes. If the algebra is nonabelian, its centre has dimension one. For a central element $z$ and a complementary basis $u,v$, write $[u,v]=cz$ with $c\ne0$; rescale $z$ to make $[u,v]=z$. This is exactly the Heisenberg algebra.

**Solution 4.** Differentiate right multiplication by $(t,0,0)$, $(0,t,0)$, and $(0,0,t)$ to obtain the left-invariant fields

$$
U_x=\partial_x-\tfrac y2\partial_z,\quad
U_y=\partial_y+\tfrac x2\partial_z,\quad U_z=\partial_z.
$$

Differentiating left multiplication gives the right-invariant fields

$$
V_x=\partial_x+\tfrac y2\partial_z,\quad
V_y=\partial_y-\tfrac x2\partial_z,\quad V_z=\partial_z.
$$

Direct differentiation gives $[U_x,U_y]=U_z$, $[V_x,V_y]=-V_z$, and all other internal basis brackets zero. For the mixed pair $U_x,V_y$, the two derivatives of the $\partial_z$ coefficient are $-1/2$ and $-1/2$, so their difference is zero; for $U_y,V_x$ they are both $1/2$. The remaining mixed pairs vanish because no coefficient depends on $z$ and a field does not differentiate its own transverse coordinate. Thus $[U_i,V_j]=0$ for all $i,j$. Left translations compose in the written order and right translations in the reverse order. Inverting the right-translation parameter identifies their composition laws.

**Solution 5.** Suppose (5.1) holds at level $j$ simultaneously for every $a\in H$. Then

$$
a b^{j+1}v=b(a b^jv)+[a,b]b^jv.
$$

The first term differs from $\lambda(a)b^{j+1}v$ by an element of $bW_{j-1}\subset W_j$. The second belongs to $W_j$ by the induction hypothesis for $[a,b]\in H$. This proves the next level. The initial level is the defining eigenvector equation. Once the cyclic span stops growing, $bW\subset W$, so the trace calculation is valid on a finite-dimensional invariant space. It proves $\lambda([H,b])=0$, hence invariance of the common eigenspace. An eigenvector of $b$ on that space is common to the whole algebra. Quotienting by its line repeats the proof and gives the full flag.

For a nonfaithful representation, one may either run the same proof on the abstract algebra using its operators, or pass to its image. The image is solvable because the homomorphism carries each derived term onto the corresponding derived term. Triangularization therefore still holds. In an upper triangular basis, every commutator has diagonal entries zero, so the derived algebra consists of strictly upper triangular, hence nilpotent, matrices. This statement concerns the represented derived algebra; it does not say that every represented element of a solvable algebra is nilpotent.

**Solution 6.** Write $Z=A(x,y)\partial_x+B(x,y)\partial_y$. Commutation with $\partial_x$ forces $A=f(y)$ and $B=g(y)$.

In (a), both functions are arbitrary. There are no dependency coefficients, so $n=1$, $m=0$, $q=2$; the first integral is $y$. In (b), the additional bracket is

$$
[y\partial_x,Z]=-g(y)\partial_x,
$$

so $g=0$. The dependency coefficient is $\varphi=y$, giving $n=1$, $m=1$, $q=1$, with one arbitrary function $f(y)$. In (c), commutation with $\partial_y$ also gives $f'=0$. Choose $\partial_x,\partial_y$ as the orbit frame; the dependency coefficient of $y\partial_x$ is still $y$, hence $n=2$, $m=1$, $q=1$. There is one arbitrary constant.

In (d), both translations force $A,B$ to be constants, say $a,b$. Their bracket with the Euler field is

$$
[x\partial_x+y\partial_y,a\partial_x+b\partial_y]
=-a\partial_x-b\partial_y,
$$

so both vanish. Relative to the two translations, the coefficient array is $(x,y)$ of rank $m=2$; therefore $n=2$ and $q=0$. All four results agree with Theorem 6.2, including the difference between orbit rank and centralizer rank.

**Solution 7.** Put $q=z-xy$ and use $[A,B]=DB\,A-DA\,B$ for coefficient columns. Direct expansion gives

$$
\det(X_1,X_2,X_3)=q^2,\qquad
\det(Z_1,Z_2,Z_3)=-q^2.
$$

For either triple $F=X$ or $F=Z$,

$$
[F_1,F_2]=F_1,\qquad
[F_1,F_3]=2F_2,\qquad
[F_2,F_3]=F_3.
$$

The mixed brackets all vanish. For example,

$$
\begin{aligned}
DZ_3\,X_3
&=DX_3\,Z_3\\
&=\bigl(2x(xy-z),\,2y(xy-z),\,2xyz-z^2\bigr);
\end{aligned}
$$

the remaining eight pairs give the same cancellation component by component. On $q\ne0$, each triple is a frame and hence a simply transitive local action. Commutation and Theorem 6.1 show that they are reciprocal.

The surface $q=0$ is preserved because

$$
(X_1q,X_2q,X_3q)=(0,q,2xq),\qquad
(Z_1q,Z_2q,Z_3q)=(0,q,2yq).
$$

On that surface $X_2=xX_1$, $X_3=x^2X_1$, while $Z_2=yZ_1$, $Z_3=y^2Z_1$. Both ranks are exactly one, since the leading $x$ or $y$ component of the first field is one. The first triple's orbits are the lines $y=\mathrm{constant}$, $z=xy$; the second's are the lines $x=\mathrm{constant}$, $z=xy$. The projective affine coordinate interchange $(x,y,z)\mapsto(y,x,z)$ preserves the surface and sends each $X_i$ to $Z_i$.

Thus preservation of a quadric and simple transitivity on its ambient regular region are distinct assertions. At $(0,0,1)$, a reciprocal frame normalized to have the negative initial values of the $X_i$ is $(Z_3,-Z_2,Z_1)$; it has the same structure constants as the $X$ frame, in agreement with the sign convention.

**Solution 8.** Left multiplication by $(t,0,0)$ gives

$$
(t,0,0)(x,y,z)=(x+t,y,z+\tfrac12ty).
$$

The right cosets have invariants $y$ and $z-yx/2$, and tangent field $V_x=\partial_x+(y/2)\partial_z$. Solution 4 gives $[U_i,V_x]=0$, so the right-translation action generated by the $U_i$ preserves the foliation. The algebra $\mathbb K e_x$ is not an ideal, since $[e_y,e_x]=-e_z$; hence $H$ is not normal.

Conjugation at $p=(0,c,0)$ gives

$$
p^{-1}(t,0,0)p=(t,0,ct).
$$

The fixed-leaf stabilizer inside the given right translations is therefore the subgroup with algebra $\mathbb K(e_x+ce_z)$. Inside the reciprocal left translations it is $H$, with algebra $\mathbb K e_x$, and this latter subgroup preserves every leaf. The full-family isomorphism is $R_a\mapsto L_{pa^{-1}p^{-1}}$, by (6.12). For $a=p^{-1}(t,0,0)p$ its image is $L_{(-t,0,0)}$, so it carries the stabilizers onto one another, including their opposite raw parameter convention.

## Historical terminology and references

Lie–Engel I, Chapter 15, Theorem 47, treats invariant subgroups; Chapter 16, Theorems 48–49, treats the adjoint group and its essential parameters. Chapter 17, Theorem 54, concerns equal structure constants, while Chapters 19–20, Theorems 64 and 68, treat simply transitive and reciprocal groups. Chapter 20, Theorems 67 and 69, gives the general centralizer and the invariant-foliation correspondence proved above. “Excellent” infinitesimal transformations are central directions. The historical conclusions here are interpreted as local statements; no claim about global discrete kernels is inferred from their infinitesimal parameter counts.

- Sophus Lie and Friedrich Engel, *Theorie der Transformationsgruppen*, Volume I (1888), the chapters and theorem numbers above; contextual access through [Merker's presentation](https://arxiv.org/abs/1003.3202).
- J. S. Milne, [*Lie Algebras, Algebraic Groups, and Lie Groups*](https://www.jmilne.org/math/CourseNotes/LAG.pdf), Chapter I, §§2–3, especially Theorems 2.8 and 3.7, for the linear algebra statements of Engel and Lie. The arguments in this lesson include the normalizer induction and the cyclic-space trace step explicitly.

The historical location of Lie's triangularization theorem in the original Lie–Engel volumes has not been established here. Its attribution is by theorem name; the modern numbered reference supplies a verifiable statement and proof. Semisimple structure theory, including Cartan's criteria and root classification, lies beyond this lesson.
