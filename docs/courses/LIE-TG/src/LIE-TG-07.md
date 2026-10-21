# The adjoint group, composition and isomorphism

*GPT-6.1 Sol (OpenAI). Original exposition and English translations: CC0 1.0; quoted German originals are public domain.*

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

## Historical reading: the adjoint group

Sophus Lie and Friedrich Engel, *Theorie der Transformationsgruppen*, Volume I (1888), Chapter 16 introduction and §§76–77, printed pp. 270–278. [German original](https://archive.org/details/theotransformation01liesrich).

The German original is in the public domain. The transcription and independently written English translation are dedicated to CC0.

### German text: Chapter 16 introduction and §§76–77

**Kapitel 16. Die adjungirte Gruppe.**

Es sei $x_i'=f_i(x_1\cdots x_n,a_1\cdots a_r)$ eine $r$-gliedrige Gruppe mit den $r$ unabhängigen infinitesimalen Transformationen:

$$
X_kf=\sum_1^n{}^{i}\xi_{ki}(x)\frac{\partial f}{\partial x_i}
\qquad(k=1\cdots r).
$$

Führt man in den Ausdruck $\sum e_kX_kf$ die $x_i'$ als neue Veränderliche ein, so ergiebt sich, wie schon in Kap. 4, Satz 4, S. 81 gezeigt worden ist, für alle Werthe der $e_k$ eine Gleichung von der Form:

$$
\sum_1^r{}^{k} e_k\cdot X_kf=\sum_1^r{}^{k} e_k'\cdot X_k'f.
$$

Dabei sind die $e_k'$ gewisse lineare, homogene Functionen der $e_k$ mit Coefficienten, welche von $a_1\cdots a_r$ abhängen:

$$
e_k'=\sum_1^r{}^{j}\varrho_{kj}(a_1\cdots a_r)\cdot e_j.\tag{1}
$$

Führt man weiter in $\sum e_k'X_k'f$ die neuen Veränderlichen $x_i''=f_i(x',b)$ ein, so bekommt man:

$$
\sum_1^r{}^{k} e_k'\cdot X_k'f=\sum_1^r{}^{k} e_k''\cdot X_k''f,
$$

wo:

$$
e_k''=\sum_1^r{}^{j}\varrho_{kj}(b_1\cdots b_r)\cdot e_j'.\tag{1'}
$$

Nun stellen aber die Gleichungen $x_i'=f_i(x,a)$ eine Gruppe dar, also sind die $x''$ mit den $x$ durch Relationen von der Form $x_i''=f_i(x,c)$ verknüpft, in denen die $c$ nur von den $a$ und $b$ abhängen:

$$
c_k=\varphi_k(a_1\cdots a_r,b_1\cdots b_r).
$$

Geht man daher unmittelbar von den $x$ zu den $x''$ über, so findet man:

$$
\sum_1^r{}^{k} e_k\cdot X_kf=\sum_1^r{}^{k} e_k''\cdot X_k''f,
$$

und zwar ist:

$$
\begin{gathered}
e_k''=\sum_1^r{}^{j}\varrho_{kj}(c_1\cdots c_r)\cdot e_j\\
=\sum_1^r{}^{j}
\varrho_{kj}\bigl(\varphi_1(a,b)\\
\cdots\varphi_r(a,b)\bigr)\cdot e_j.
\end{gathered}\tag{1''}
$$

Hieraus lässt sich schliessen, dass der Inbegriff aller Transformationen $e_k'=\sum\varrho_{kj}(a)\cdot e_j$ eine Gruppe bildet. Es ergiebt sich nämlich durch Verbindung der Gleichungen (1) und (1'):

$$
e_k''=\sum_{j,\nu}^{1\cdots r}
\varrho_{kj}(b_1\cdots b_r)\cdot\varrho_{j\nu}(a_1\cdots a_r)\cdot e_\nu,
$$

was natürlich mit den Gleichungen (1'') übereinstimmen muss und zwar für alle Werthe der $e$, der $a$ und der $b$. Es bestehen daher die $r^2$ Identitäten:

$$
\begin{gathered}
\varrho_{k\nu}\bigl(\varphi_1(a,b)\cdots\varphi_r(a,b)\bigr)\\
=\sum_1^r{}^{j}
\varrho_{j\nu}(a_1\cdots a_r)\cdot\varrho_{kj}(b_1\cdots b_r),
\end{gathered}
$$

aus denen hervorgeht, dass die Schaar der Transformationen $e_k'=\sum\varrho_{kj}(a)\cdot e_j$ wirklich eine Gruppe bildet.

Zu jeder $r$-gliedrigen Gruppe $x_i'=f_i(x,a)$ gehört demnach eine ganz bestimmte lineare homogene Gruppe:

$$
\begin{gathered}
e_k'=\sum_1^r{}^{j}\varrho_{kj}(a_1\cdots a_r)\cdot e_j
\\
(k=1\cdots r),
\end{gathered}\tag{1}
$$

welche wir als die *adjungirte Gruppe*\*) der Gruppe $x_i'=f_i(x,a)$ bezeichnen wollen.

Betrachten wir zum Beispiel die zweigliedrige Gruppe $x'=ax+b$ mit den beiden unabhängigen infinitesimalen Transformationen: $\frac{df}{dx}$, $x\frac{df}{dx}$. Wir finden:

$$
\begin{gathered}
e_1\frac{df}{dx}+e_2x\frac{df}{dx}\\
=e_1a\frac{df}{dx'}+e_2(x'-b)\frac{df}{dx'}\\
=e_1'\frac{df}{dx'}+e_2'x'\frac{df}{dx'},
\end{gathered}
$$

also erhalten wir für die adjungirte Gruppe der Gruppe $x'=ax+b$ die folgenden Gleichungen:

$$
e_1'=ae_1-be_2,\qquad e_2'=e_2,
$$

welche augenscheinlich wirklich eine Gruppe darstellen.

Die adjungirte Gruppe der Gruppe $x_i'=f_i(x,a)$ enthält in der Form, in welcher wir sie oben gefunden haben, gerade $r$ willkürliche Parameter: $a_1\cdots a_r$. Es bedarf aber bei jeder einzelnen Gruppe $x_i'=f_i(x,a)$ einer besonderen Untersuchung, ob die Parameter $a_1\cdots a_r$ in der adjungirten Gruppe alle wesentlich sind. Wirklich werden wir bald sehen, dass es $r$-gliedrige Gruppen giebt, deren adjungirte Gruppen nicht $r$ wesentliche Parameter enthalten.

Eine Transformation kommt übrigens in der adjungirten Gruppe der Gruppe $x_i'=f_i(x,a)$ unter allen Umständen vor, nämlich die identische Transformation; denn setzt man in den Gleichungen (1) für $a_1\cdots a_r$ diejenigen Zahlenwerthe, welche in der Gruppe $x_i'=f_i(x,a)$ die identische Transformation $x_i'=x_i$ liefern, so erhält man die Transformation: $e_1'=e_1,\cdots,e_r'=e_r$, welche daher immer in der adjungirten Gruppe vorhanden ist. Allerdings kann es, wie wir sehen werden, geschehen, dass die adjungirte Gruppe blos aus der identischen Transformation: $e_1'=e_1,\cdots,e_r'=e_r$ besteht.

**§76.** Um die adjungirte Gruppe der Untersuchung zugänglich zu machen, müssen wir vor allen Dingen ihre infinitesimalen Transformationen bestimmen. Hierzu gelangen wir leicht durch Anwendung des Theorems 43, Kap. 15, S. 252; doch müssen wir dabei die Gleichungen $x_i'=f_i(x,a)$ unserer Gruppe durch die äquivalenten *kanonischen* Gleichungen

$$
\begin{gathered}
x_i'=x_i\\
+\frac{t}{1}\sum_1^r{}^{k}\lambda_k\cdot X_kx_i+\cdots
\\
(i=1\cdots n)
\end{gathered}\tag{2}
$$

ersetzen, welche die $\infty^{r-1}$ eingliedrigen Untergruppen der Gruppe $x_i'=f_i(x,a)$ darstellen. Nach Kap. 4, S. 69 sind hier die $a_k$ als Functionen von $t$ und $\lambda_1\cdots\lambda_r$ durch das simultane System

$$
\begin{gathered}
\frac{da_k}{dt}=\sum_1^r{}^{j}\lambda_j\cdot\alpha_{jk}(a_1\cdots a_r)
\\
(k=1\cdots r)
\end{gathered}\tag{3}
$$

definirt.

Vermittelst der Gleichungen (2) haben wir also die neuen Veränderlichen $x_i'$ in $\sum e_kX_kf$ einzuführen und müssen dabei eine Relation von der Form

$$
\sum_1^r{}^{k} e_k\cdot X_kf=\sum_1^r{}^{k} e_k'\cdot X_k'f
$$

erhalten. Die in Theorem 43, S. 252 mit $Yf$ bezeichnete infinitesimale Transformation lautet jetzt: $\lambda_1X_1f+\cdots+\lambda_rX_rf$; wir bekommen daher in unserem Falle:

$$
\begin{gathered}
Y(X_k(f))-X_k(Y(f))
\\
=\sum_1^r{}^{\nu}\lambda_\nu(X_\nu X_k)\\
=\sum_1^r{}^{s}\left\{\sum_1^r{}^{\nu}
\lambda_\nu c_{\nu ks}\right\}X_sf.
\end{gathered}
$$

Für $e_1'\cdots e_r'$ ergeben sich demnach folgende Differentialgleichungen:

$$
\begin{gathered}
\frac{de_s'}{dt}
+\sum_1^r{}^{\nu}\lambda_\nu\sum_1^r{}^{k} c_{\nu ks}e_k'=0
\\
(s=1\cdots r).
\end{gathered}\tag{4}
$$

Die Integration dieser Differentialgleichungen betrachten wir als eine ausführbare Operation, da sie bekanntlich nur die Auflösung einer algebraischen Gleichung $r$-ten Grades erfordert. Führen wir die Integration aus unter Zugrundelegung der Anfangsbedingung: $e_k'=e_k$ für $t=0$, so erhalten wir $r$ Gleichungen von der Form:

$$
\begin{gathered}
e_k'=\sum_1^r{}^{j}\psi_{kj}(\lambda_1t,\cdots,\lambda_rt)\cdot e_j
\\
(k=1\cdots r),
\end{gathered}\tag{5}
$$

welche mit den Gleichungen (1) äquivalent sind, sobald in diesen letzteren die $a_k$ als Functionen von $\lambda_1t,\cdots,\lambda_rt$ ausgedrückt werden. Hieraus geht hervor, dass auch die Gleichungen (5) die adjungirte Gruppe darstellen. Nun aber haben wir die Gleichungen (5) genau in derselben Weise hergeleitet, als hätten wir alle endlichen Transformationen bestimmen wollen, welche von den infinitesimalen Transformationen

$$
\sum_1^r{}^{\nu}\lambda_\nu\sum_{ks}^{1\cdots r}
c_{k\nu s}e_k\frac{\partial f}{\partial e_s}
=\sum_1^r{}^{\nu}\lambda_\nu\cdot E_\nu f
$$

erzeugt werden (vgl. S. 51, oben). *Also schliessen wir, dass die adjungirte Gruppe (1) aus dem Inbegriffe aller eingliedrigen Gruppen von der Form $\lambda_1E_1f+\cdots+\lambda_rE_rf$ besteht.*

Giebt es unter der Schaar aller infinitesimalen Transformationen $\lambda_1E_1f+\cdots+\lambda_rE_rf$ gerade $\varrho$ und nicht mehr unabhängige, etwa $E_1f\cdots E_\varrho f$, so sind alle endlichen Transformationen der eingliedrigen Gruppen $\lambda_1E_1f+\cdots+\lambda_rE_rf$ schon in dem Inbegriffe aller endlichen Transformationen der $\infty^{\varrho-1}$ eingliedrigen Gruppen $\lambda_1E_1f+\cdots+\lambda_\varrho E_\varrho f$ enthalten. Der Inbegriff dieser $\infty^\varrho$ endlichen Transformationen bildet die adjungirte Gruppe: $e_k'=\sum\varrho_{kj}(a)\cdot e_j$, welche somit nur $\varrho$ wesentliche Parameter enthält (Kap. 3, Theorem 8, S. 65).

Nach dem Vorangehenden ist es vorauszusehen, dass $E_1f\cdots E_\varrho f$ durch Relationen von der Form

$$
(E_\mu E_\nu)=\sum_1^\varrho{}^{s} g_{\mu\nu s}\cdot E_sf
$$

verknüpft sind; wir können das auch durch Rechnung bestätigen. Bei direkter Ausrechnung kommt:

$$
\begin{gathered}
E_\mu(E_\nu(f))-E_\nu(E_\mu(f))\\
=\sum_{\sigma k\pi}^{1\cdots r}
(c_{\pi\mu k}c_{k\nu\sigma}-c_{\pi\nu k}c_{k\mu\sigma})
e_\pi\frac{\partial f}{\partial e_\sigma}.
\end{gathered}
$$

Aber zwischen den $c_{iks}$ bestehen die $\frac{r(r-1)}{1\cdot2}$ Relationen

$$
\sum_1^r{}^{k}
(c_{\pi\mu k}c_{k\nu\sigma}
+c_{\mu\nu k}c_{k\pi\sigma}
+c_{\nu\pi k}c_{k\mu\sigma})=0,
$$

welche wir seinerzeit (vgl. Kap. 9, Theorem 27, S. 170) aus der Jacobischen Identität abgeleitet haben. Nehmen wir hierzu noch, dass $c_{\nu\pi k}=-c_{\pi\nu k}$ ist und $c_{k\pi\sigma}=-c_{\pi k\sigma}$, so können wir die rechte Seite unserer Gleichung für $(E_\mu E_\nu)$ auf die Form bringen:

$$
\sum_1^r{}^{k} c_{\mu\nu k}
\sum_{\sigma\pi}^{1\cdots r}
c_{\pi k\sigma}e_\pi\frac{\partial f}{\partial e_\sigma},
$$

also wird:

$$
(E_\mu E_\nu)=\sum_1^r{}^{k} c_{\mu\nu k}\cdot E_kf.
$$

Hier lässt sich endlich unter den oben gemachten Voraussetzungen die rechte Seite durch $E_1f\cdots E_\varrho f$ allein ausdrücken, so dass wirklich Relationen von der Form

$$
(E_\mu E_\nu)=\sum_1^\varrho{}^{s} g_{\mu\nu s}E_sf
$$

bestehen, in welchen die $g_{\mu\nu s}$ Constanten bezeichnen.

Bevor wir weitergehen, wollen wir erst noch die bisherigen Ergebnisse des Kapitels im Zusammenhange wiederholen:

**Theorem 48.** *Führt man in die allgemeine infinitesimale Transformation $e_1X_1f+\cdots+e_rX_rf$ der $r$-gliedrigen Gruppe $x_i'=f_i(x,a)$ an Stelle der $x$ die neuen Veränderlichen $x'$ ein, so erhält man einen Ausdruck von der Form:*

$$
e_1'\cdot X_1'f+\cdots+e_r'\cdot X_r'f;
$$

*dabei sind die $e'$ mit den $e$ durch Gleichungen von der Gestalt*

$$
e_k'=\sum_1^r{}^{j}\varrho_{kj}(a_1\cdots a_r)\cdot e_j
\qquad(k=1\cdots r)
$$

*verknüpft, welche eine Gruppe in den Veränderlichen $e$ darstellen, die sogenannte adjungirte Gruppe der Gruppe $x_i'=f_i(x,a)$. Diese adjungirte Gruppe enthält die identische Transformation und wird von gewissen infinitesimalen Transformationen erzeugt; bestehen zwischen $X_1f\cdots X_rf$ die Relationen*

$$
(X_iX_k)=\sum_1^r{}^{s} c_{iks}\cdot X_sf
\qquad(i,k=1\cdots r),
$$

*und setzt man:*

$$
E_\mu f=\sum_{kj}^{1\cdots r} c_{j\mu k}e_j
\frac{\partial f}{\partial e_k}
\qquad(\mu=1\cdots r),
$$

*so ist $\lambda_1E_1f+\cdots+\lambda_rE_rf$ die allgemeine infinitesimale Transformation der adjungirten Gruppe und zwischen $E_1f\cdots E_rf$ bestehen dabei die Relationen:*

$$
(E_iE_k)=\sum_1^r{}^{s} c_{iks}\cdot E_sf
\qquad(i,k=1\cdots r).
$$

Sind zwei $r$-gliedrige Gruppen $X_1f\cdots X_rf$ und $Y_1f\cdots Y_rf$ so beschaffen, dass zu gleicher Zeit gilt:

$$
\begin{gathered}
(X_iX_k)=\sum_1^r{}^{s} c_{iks}\cdot X_sf,\\
(Y_iY_k)=\sum_1^r{}^{s} c_{iks}\cdot Y_sf,
\end{gathered}
$$

beide Male mit denselben Constanten $c_{iks}$, so haben beide Gruppen offenbar dieselbe adjungirte Gruppe. Später werden wir sehen, dass unter Umständen auch solche Gruppen, welche nicht gleiche Gliederzahl besitzen, doch dieselbe adjungirte Gruppe haben.

**§77.** Woran lässt sich nun erkennen, wie viele unabhängige es unter den infinitesimalen Transformationen $E_1f\cdots E_rf$ giebt?

Sind $E_1f\cdots E_rf$ nicht alle von einander unabhängig, so giebt es wenigstens eine infinitesimale Transformation $\sum g_\mu E_\mu f$, welche identisch verschwindet. Aus der Identität

$$
\sum_1^r{}^{\mu} g_\mu
\sum_{kj}^{1\cdots r} c_{j\mu k}e_j\frac{\partial f}{\partial e_k}=0
$$

ergiebt sich:

$$
\sum_1^r{}^{\mu} g_\mu c_{j\mu k}=0
$$

für alle Werthe von $j$ und $k$, folglich verschwindet auch der Ausdruck

$$
\begin{gathered}
\left(X_jf,\sum_1^r{}^{\mu} g_\mu\cdot X_\mu f\right)\\
=\sum_1^r{}^{k}\left\{\sum_1^r{}^{\mu}
g_\mu c_{j\mu k}\right\}X_kf,
\end{gathered}
$$

das heisst, die infinitesimale Transformation $\sum g_\mu X_\mu f$ ist mit allen $r$ infinitesimalen Transformationen $X_kf$ vertauschbar. Enthält umgekehrt die Gruppe $X_1f\cdots X_rf$ eine infinitesimale Transformation $\sum g_\mu X_\mu f$, welche mit allen $X_kf$ vertauschbar ist, so folgt daraus in derselben Weise, dass die infinitesimale Transformation $\sum g_\mu E_\mu f$ identisch verschwindet.

Um diese Beziehungen möglichst kurz ausdrücken zu können, führen wir die folgende Benennung ein:

*Eine infinitesimale Transformation $\sum g_\mu X_\mu f$ der $r$-gliedrigen Gruppe $X_1f\cdots X_rf$ heisse eine ausgezeichnete infinitesimale Transformation dieser Gruppe, wenn sie mit allen $X_kf$ vertauschbar ist.*

Die ausgezeichneten infinitesimalen Transformationen der Gruppe $X_1f\cdots X_rf$ sind, nebenbei bemerkt, auch dadurch charakterisirt, dass sie bei Einführung der neuen Veränderlichen: $x_i'=f_i(x,a)$ ihre Form behalten, welche Werthe auch die Parameter $a_1\cdots a_r$ haben mögen. Ist nämlich die infinitesimale Transformation $\sum g_\mu X_\mu f$ ausgezeichnet, so besteht nach Kap. 15, S. 259 eine Relation von der Form:

$$
\sum g_\mu\cdot X_\mu f=\sum g_\mu\cdot X_\mu'f.
$$

Ueberdies zeigen die citirten Entwickelungen, dass jede endliche Transformation der eingliedrigen Gruppe $\sum g_\mu X_\mu f$ mit jeder endlichen Transformation der Gruppe $X_1f\cdots X_rf$ vertauschbar ist.

Nach dem oben Gesagten entspricht jeder ausgezeichneten infinitesimalen Transformation der Gruppe $X_1f\cdots X_rf$ eine lineare Relation zwischen $E_1f\cdots E_rf$. Ist $\sum g_\mu X_\mu f$ eine ausgezeichnete infinitesimale Transformation, so besteht zwischen den $E_\mu f$ einfach die Relation: $\sum g_\mu E_\mu f=0$. Folglich bestehen zwischen $E_1f\cdots E_rf$ gerade so viele unabhängige Relationen dieser Art, als es in der Gruppe $X_1f\cdots X_rf$ unabhängige ausgezeichnete infinitesimale Transformationen giebt.

Giebt es also solcher Transformationen gerade $m$ und nicht mehr unabhängige, so giebt es unter den infinitesimalen Transformationen $E_1f\cdots E_rf$ gerade $r-m$ und nicht mehr unabhängige, und ebenso viele wesentliche Parameter enthält die adjungirte Gruppe.

Wir haben somit das

**Theorem 49.** *Die adjungirte Gruppe $e_k'=\sum\varrho_{kj}(a)\cdot e_j$ einer $r$-gliedrigen Gruppe $X_1f\cdots X_rf$ enthält dann und nur dann $r$ wesentliche Parameter, wenn keine von den $\infty^{r-1}$ infinitesimalen Transformationen $\sum g_\mu X_\mu f$ innerhalb der Gruppe $X_1f\cdots X_rf$ ausgezeichnet ist; die adjungirte Gruppe hat dagegen weniger als $r$, nämlich gerade $r-m$ wesentliche Parameter, wenn die Gruppe $X_1f\cdots X_rf$ gerade $m$ und nicht mehr unabhängige ausgezeichnete infinitesimale Transformationen enthält.*\*)

Nehmen wir zum Beispiel die Gruppe

$$
\frac{\partial f}{\partial x_1}\cdots
\frac{\partial f}{\partial x_r}\qquad(r\leq n).
$$

Deren infinitesimale Transformationen sind alle ausgezeichnet, denn alle $c_{iks}$ sind gleich Null. Es verschwinden also alle $r$ Ausdrücke $E_1f\cdots E_rf$ identisch, und die adjungirte Gruppe schrumpft zur identischen Transformation zusammen.

Nehmen wir andererseits die viergliedrige Gruppe:

$$
x\frac{\partial f}{\partial x},\quad
y\frac{\partial f}{\partial x},\quad
x\frac{\partial f}{\partial y},\quad
y\frac{\partial f}{\partial y}.
$$

Dieselbe enthält eine einzige ausgezeichnete infinitesimale Transformation, nämlich:

$$
x\frac{\partial f}{\partial x}+y\frac{\partial f}{\partial y};
$$

ihre adjungirte Gruppe ist daher blos dreigliedrig.

Enthält die Gruppe $X_1f\cdots X_rf$ die ausgezeichnete infinitesimale Transformation $\sum g_\mu X_\mu f$, so ist $\sum g_\mu X_\mu f=0$ eine lineare partielle Differentialgleichung, welche bei der Gruppe invariant bleibt; die Gruppe ist in Folge dessen imprimitiv (vgl. S. 221). Wir schliessen hieraus, dass der folgende Satz gilt:

**Satz 1.** *Ist die Gruppe $X_1f\cdots X_rf$ in den Veränderlichen $x_1\cdots x_n$ primitiv, so enthält sie keine ausgezeichnete infinitesimale Transformation.*

Verbinden wir diesen Satz mit dem letzten Theoreme, so erhalten wir noch den

**Satz 2.** *Die adjungirte Gruppe einer $r$-gliedrigen primitiven Gruppe enthält $r$ wesentliche Parameter.*

An einer späteren Stelle werden wir den beiden letzten Sätzen eine etwas allgemeinere Fassung geben (vgl. das Kapitel 24, über systatische Gruppen).

Nach dem Vorangehenden sind die infinitesimalen Transformationen einer $r$-gliedrigen Gruppe $X_1f\cdots X_rf$ und diejenigen der adjungirten Gruppe $E_1f\cdots E_rf$ einander derart zugeordnet, dass jeder nicht ausgezeichneten infinitesimalen Transformation $\sum e_kX_kf$ eine nicht verschwindende infinitesimale Transformation $\sum e_kE_kf$ entspricht, während jeder ausgezeichneten infinitesimalen Transformation $\sum e_kX_kf$ in der adjungirten Gruppe die identische Transformation zugeordnet ist. Berücksichtigt man überdies, dass die beiden Gleichungensysteme

$$
\begin{gathered}
(X_iX_k)=\sum_1^r{}^{s} c_{iks}\cdot X_sf,\\
(E_iE_k)=\sum_1^r{}^{s} c_{iks}\cdot E_sf
\end{gathered}
$$

genau dieselbe Form haben, so könnte man auf die Vermuthung kommen, dass die adjungirte Gruppe keine ausgezeichnete infinitesimale Transformation enthalten kann. Diese Vermuthung wäre indess falsch; das zeigt uns die Gruppe $\frac{\partial f}{\partial x_2}$, $x_1\frac{\partial f}{\partial x_2}$, $\frac{\partial f}{\partial x_1}$, deren adjungirte Gruppe aus zwei vertauschbaren infinitesimalen Transformationen besteht und somit zwei unabhängige ausgezeichnete infinitesimale Transformationen enthält.

### German original footnotes

**F1 · p. 272, at the name “adjungirte Gruppe”.** [Lie, Archiv for Math., Bd. 1, Christiania 1876.](https://archive.org/details/archivformathema11876oslo)

**F2 · p. 277, after Theorem 49.** [Lie, Math. Ann. Bd. XXV, S. 94.](https://gdz.sub.uni-goettingen.de/download/pdf/PPN235181684_0025/PPN235181684_0025.pdf)

### English translation: Chapter 16 introduction and §§76–77

**Chapter 16. The adjoint group.**

Let $x_i'=f_i(x_1\cdots x_n,a_1\cdots a_r)$ be an $r$-parameter group with the $r$ independent infinitesimal transformations

$$
X_kf=\sum_1^n{}^{i}\xi_{ki}(x)\frac{\partial f}{\partial x_i}
\qquad(k=1\cdots r).
$$

If the $x_i'$ are introduced as new variables in $\sum e_kX_kf$, then, as already shown in Chapter 4, Proposition 4, p. 81, an equation of the following form holds for every choice of the $e_k$:

$$
\sum_1^r{}^{k} e_k\cdot X_kf=\sum_1^r{}^{k} e_k'\cdot X_k'f.
$$

The $e_k'$ are linear homogeneous functions of the $e_k$, with coefficients depending on $a_1\cdots a_r$:

$$
e_k'=\sum_1^r{}^{j}\varrho_{kj}(a_1\cdots a_r)\cdot e_j.\tag{1}
$$

Next introduce the new variables $x_i''=f_i(x',b)$ in $\sum e_k'X_k'f$. This gives

$$
\sum_1^r{}^{k} e_k'\cdot X_k'f=\sum_1^r{}^{k} e_k''\cdot X_k''f,
$$

where

$$
e_k''=\sum_1^r{}^{j}\varrho_{kj}(b_1\cdots b_r)\cdot e_j'.\tag{1'}
$$

But the equations $x_i'=f_i(x,a)$ constitute a group. Thus $x''$ and $x$ satisfy relations of the form $x_i''=f_i(x,c)$, in which the $c$ depend only on the $a$ and $b$:

$$
c_k=\varphi_k(a_1\cdots a_r,b_1\cdots b_r).
$$

Going directly from the $x$ to the $x''$ therefore gives

$$
\sum_1^r{}^{k} e_k\cdot X_kf=\sum_1^r{}^{k} e_k''\cdot X_k''f,
$$

with

$$
\begin{gathered}
e_k''=\sum_1^r{}^{j}\varrho_{kj}(c_1\cdots c_r)\cdot e_j\\
=\sum_1^r{}^{j}
\varrho_{kj}\bigl(\varphi_1(a,b)\\
\cdots\varphi_r(a,b)\bigr)\cdot e_j.
\end{gathered}\tag{1''}
$$

This shows that all the transformations $e_k'=\sum\varrho_{kj}(a)\cdot e_j$ together form a group. Combining equations (1) and (1') yields

$$
e_k''=\sum_{j,\nu}^{1\cdots r}
\varrho_{kj}(b_1\cdots b_r)\cdot\varrho_{j\nu}(a_1\cdots a_r)\cdot e_\nu,
$$

This must agree with equations (1'') for every choice of the $e$, $a$ and $b$. Hence we have the $r^2$ identities

$$
\begin{gathered}
\varrho_{k\nu}\bigl(\varphi_1(a,b)\cdots\varphi_r(a,b)\bigr)\\
=\sum_1^r{}^{j}
\varrho_{j\nu}(a_1\cdots a_r)\cdot\varrho_{kj}(b_1\cdots b_r),
\end{gathered}
$$

They prove that the family of transformations $e_k'=\sum\varrho_{kj}(a)\cdot e_j$ does indeed form a group.

Every $r$-parameter group $x_i'=f_i(x,a)$ therefore has a uniquely determined linear homogeneous group

$$
\begin{gathered}
e_k'=\sum_1^r{}^{j}\varrho_{kj}(a_1\cdots a_r)\cdot e_j
\\
(k=1\cdots r),
\end{gathered}\tag{1}
$$

which we shall call the *adjoint group*\*) of the group $x_i'=f_i(x,a)$.

For example, consider the two-parameter group $x'=ax+b$, with its two independent infinitesimal transformations $\frac{df}{dx}$ and $x\frac{df}{dx}$. We find

$$
\begin{gathered}
e_1\frac{df}{dx}+e_2x\frac{df}{dx}\\
=e_1a\frac{df}{dx'}+e_2(x'-b)\frac{df}{dx'}\\
=e_1'\frac{df}{dx'}+e_2'x'\frac{df}{dx'},
\end{gathered}
$$

The adjoint group of $x'=ax+b$ is consequently given by

$$
e_1'=ae_1-be_2,\qquad e_2'=e_2,
$$

These equations plainly define a group.

In the form just obtained, the adjoint group of $x_i'=f_i(x,a)$ contains exactly $r$ arbitrary parameters, $a_1\cdots a_r$. For each particular group $x_i'=f_i(x,a)$, however, a separate investigation is needed to determine whether all the parameters $a_1\cdots a_r$ are essential in its adjoint group. We shall shortly see that some $r$-parameter groups have adjoint groups with fewer than $r$ essential parameters.

One transformation is always present in the adjoint group of $x_i'=f_i(x,a)$: the identity. Indeed, substitute in equations (1) the values of $a_1\cdots a_r$ that give the identity $x_i'=x_i$ in the original group $x_i'=f_i(x,a)$. The result is $e_1'=e_1,\cdots,e_r'=e_r$, so this transformation always belongs to the adjoint group. As we shall see, it is even possible for the adjoint group to consist solely of the identity $e_1'=e_1,\cdots,e_r'=e_r$.

**§76.** To make the adjoint group accessible to investigation, we must first determine its infinitesimal transformations. Theorem 43 in Chapter 15, p. 252, readily provides them. For that purpose, we replace the equations $x_i'=f_i(x,a)$ of our group by the equivalent *canonical* equations

$$
\begin{gathered}
x_i'=x_i\\
+\frac{t}{1}\sum_1^r{}^{k}\lambda_k\cdot X_kx_i+\cdots
\\
(i=1\cdots n)
\end{gathered}\tag{2}
$$

representing the $\infty^{r-1}$ one-parameter subgroups of $x_i'=f_i(x,a)$. According to Chapter 4, p. 69, the $a_k$, as functions of $t$ and $\lambda_1\cdots\lambda_r$, are defined here by the simultaneous system

$$
\begin{gathered}
\frac{da_k}{dt}=\sum_1^r{}^{j}\lambda_j\cdot\alpha_{jk}(a_1\cdots a_r)
\\
(k=1\cdots r)
\end{gathered}\tag{3}
$$

We must therefore use equations (2) to introduce the new variables $x_i'$ in $\sum e_kX_kf$, obtaining a relation of the form

$$
\sum_1^r{}^{k} e_k\cdot X_kf=\sum_1^r{}^{k} e_k'\cdot X_k'f
$$

The infinitesimal transformation denoted by $Yf$ in Theorem 43, p. 252, is now $\lambda_1X_1f+\cdots+\lambda_rX_rf$. In our case we therefore obtain

$$
\begin{gathered}
Y(X_k(f))-X_k(Y(f))
\\
=\sum_1^r{}^{\nu}\lambda_\nu(X_\nu X_k)\\
=\sum_1^r{}^{s}\left\{\sum_1^r{}^{\nu}
\lambda_\nu c_{\nu ks}\right\}X_sf.
\end{gathered}
$$

The resulting differential equations for $e_1'\cdots e_r'$ are

$$
\begin{gathered}
\frac{de_s'}{dt}
+\sum_1^r{}^{\nu}\lambda_\nu\sum_1^r{}^{k} c_{\nu ks}e_k'=0
\\
(s=1\cdots r).
\end{gathered}\tag{4}
$$

We regard their integration as an operation that can be performed, since, as is known, it requires only the solution of an algebraic equation of degree $r$. Integrating with the initial condition $e_k'=e_k$ at $t=0$ gives $r$ equations of the form

$$
\begin{gathered}
e_k'=\sum_1^r{}^{j}\psi_{kj}(\lambda_1t,\cdots,\lambda_rt)\cdot e_j
\\
(k=1\cdots r),
\end{gathered}\tag{5}
$$

These are equivalent to equations (1) once the $a_k$ in those equations have been expressed as functions of $\lambda_1t,\cdots,\lambda_rt$. It follows that equations (5) also represent the adjoint group. But we derived equations (5) in precisely the same way as if we had wanted to determine all finite transformations generated by the infinitesimal transformations

$$
\sum_1^r{}^{\nu}\lambda_\nu\sum_{ks}^{1\cdots r}
c_{k\nu s}e_k\frac{\partial f}{\partial e_s}
=\sum_1^r{}^{\nu}\lambda_\nu\cdot E_\nu f
$$

(compare the top of p. 51). *We therefore conclude that the adjoint group (1) consists of all the one-parameter groups of the form $\lambda_1E_1f+\cdots+\lambda_rE_rf$.*

Suppose that the family of all infinitesimal transformations $\lambda_1E_1f+\cdots+\lambda_rE_rf$ contains exactly $\varrho$ independent ones, say $E_1f\cdots E_\varrho f$. Every finite transformation of the one-parameter groups $\lambda_1E_1f+\cdots+\lambda_rE_rf$ is then already among the finite transformations of the $\infty^{\varrho-1}$ one-parameter groups $\lambda_1E_1f+\cdots+\lambda_\varrho E_\varrho f$. These $\infty^\varrho$ finite transformations make up the adjoint group $e_k'=\sum\varrho_{kj}(a)\cdot e_j$, which consequently has only $\varrho$ essential parameters (Chapter 3, Theorem 8, p. 65).

The preceding argument suggests that $E_1f\cdots E_\varrho f$ satisfy relations of the form

$$
(E_\mu E_\nu)=\sum_1^\varrho{}^{s} g_{\mu\nu s}\cdot E_sf
$$

We can also verify this by calculation. Direct computation gives

$$
\begin{gathered}
E_\mu(E_\nu(f))-E_\nu(E_\mu(f))\\
=\sum_{\sigma k\pi}^{1\cdots r}
(c_{\pi\mu k}c_{k\nu\sigma}-c_{\pi\nu k}c_{k\mu\sigma})
e_\pi\frac{\partial f}{\partial e_\sigma}.
\end{gathered}
$$

The $c_{iks}$ satisfy the $\frac{r(r-1)}{1\cdot2}$ relations

$$
\sum_1^r{}^{k}
(c_{\pi\mu k}c_{k\nu\sigma}
+c_{\mu\nu k}c_{k\pi\sigma}
+c_{\nu\pi k}c_{k\mu\sigma})=0,
$$

which we previously derived from the Jacobi identity (Chapter 9, Theorem 27, p. 170). Using also $c_{\nu\pi k}=-c_{\pi\nu k}$ and $c_{k\pi\sigma}=-c_{\pi k\sigma}$, we can write the right side of our equation for $(E_\mu E_\nu)$ as

$$
\sum_1^r{}^{k} c_{\mu\nu k}
\sum_{\sigma\pi}^{1\cdots r}
c_{\pi k\sigma}e_\pi\frac{\partial f}{\partial e_\sigma},
$$

Thus

$$
(E_\mu E_\nu)=\sum_1^r{}^{k} c_{\mu\nu k}\cdot E_kf.
$$

Under the assumptions already made, the right side can finally be expressed using $E_1f\cdots E_\varrho f$ alone. Hence relations of the form

$$
(E_\mu E_\nu)=\sum_1^\varrho{}^{s} g_{\mu\nu s}E_sf
$$

do hold, with constant $g_{\mu\nu s}$.

Before proceeding, let us collect the results obtained in this chapter:

**Theorem 48.** *Introduce the new variables $x'$ in place of the $x$ in the general infinitesimal transformation $e_1X_1f+\cdots+e_rX_rf$ of the $r$-parameter group $x_i'=f_i(x,a)$. The resulting expression has the form*

$$
e_1'\cdot X_1'f+\cdots+e_r'\cdot X_r'f;
$$

*The $e'$ and $e$ are related by equations of the form*

$$
e_k'=\sum_1^r{}^{j}\varrho_{kj}(a_1\cdots a_r)\cdot e_j
\qquad(k=1\cdots r)
$$

*These define a group in the variables $e$, called the adjoint group of $x_i'=f_i(x,a)$. This adjoint group contains the identity and is generated by certain infinitesimal transformations. If $X_1f\cdots X_rf$ satisfy*

$$
(X_iX_k)=\sum_1^r{}^{s} c_{iks}\cdot X_sf
\qquad(i,k=1\cdots r),
$$

*and we put*

$$
E_\mu f=\sum_{kj}^{1\cdots r} c_{j\mu k}e_j
\frac{\partial f}{\partial e_k}
\qquad(\mu=1\cdots r),
$$

*then $\lambda_1E_1f+\cdots+\lambda_rE_rf$ is the general infinitesimal transformation of the adjoint group, and $E_1f\cdots E_rf$ satisfy the relations*

$$
(E_iE_k)=\sum_1^r{}^{s} c_{iks}\cdot E_sf
\qquad(i,k=1\cdots r).
$$

If two $r$-parameter groups $X_1f\cdots X_rf$ and $Y_1f\cdots Y_rf$ satisfy

$$
\begin{gathered}
(X_iX_k)=\sum_1^r{}^{s} c_{iks}\cdot X_sf,\\
(Y_iY_k)=\sum_1^r{}^{s} c_{iks}\cdot Y_sf,
\end{gathered}
$$

with the same constants $c_{iks}$ in both systems, they plainly have the same adjoint group. We shall later see that, in some circumstances, groups with different numbers of parameters can also have the same adjoint group.

**§77.** How can we determine the number of independent infinitesimal transformations among $E_1f\cdots E_rf$?

If $E_1f\cdots E_rf$ are not all independent, then at least one infinitesimal transformation $\sum g_\mu E_\mu f$ vanishes identically. From the identity

$$
\sum_1^r{}^{\mu} g_\mu
\sum_{kj}^{1\cdots r} c_{j\mu k}e_j\frac{\partial f}{\partial e_k}=0
$$

we obtain

$$
\sum_1^r{}^{\mu} g_\mu c_{j\mu k}=0
$$

for every $j$ and $k$. Consequently the expression

$$
\begin{gathered}
\left(X_jf,\sum_1^r{}^{\mu} g_\mu\cdot X_\mu f\right)\\
=\sum_1^r{}^{k}\left\{\sum_1^r{}^{\mu}
g_\mu c_{j\mu k}\right\}X_kf,
\end{gathered}
$$

also vanishes. In other words, the infinitesimal transformation $\sum g_\mu X_\mu f$ commutes with all $r$ infinitesimal transformations $X_kf$. Conversely, suppose that the group $X_1f\cdots X_rf$ contains an infinitesimal transformation $\sum g_\mu X_\mu f$ commuting with every $X_kf$. The same reasoning shows that $\sum g_\mu E_\mu f$ vanishes identically.

To express these relations concisely, we introduce the following term:

*An infinitesimal transformation $\sum g_\mu X_\mu f$ of the $r$-parameter group $X_1f\cdots X_rf$ will be called a distinguished infinitesimal transformation of this group if it commutes with every $X_kf$.*

The distinguished infinitesimal transformations of $X_1f\cdots X_rf$ can also be characterized by their retaining their form when the new variables $x_i'=f_i(x,a)$ are introduced, whatever the values of the parameters $a_1\cdots a_r$. Indeed, if $\sum g_\mu X_\mu f$ is distinguished, Chapter 15, p. 259, gives a relation of the form

$$
\sum g_\mu\cdot X_\mu f=\sum g_\mu\cdot X_\mu'f.
$$

The cited discussion further shows that every finite transformation of the one-parameter group $\sum g_\mu X_\mu f$ commutes with every finite transformation of $X_1f\cdots X_rf$.

Each distinguished infinitesimal transformation of $X_1f\cdots X_rf$ therefore corresponds to a linear relation among $E_1f\cdots E_rf$. If $\sum g_\mu X_\mu f$ is distinguished, the relation among the $E_\mu f$ is simply $\sum g_\mu E_\mu f=0$. Thus the number of independent relations of this kind among $E_1f\cdots E_rf$ is exactly the number of independent distinguished infinitesimal transformations in $X_1f\cdots X_rf$.

If there are exactly $m$ independent distinguished transformations, there are exactly $r-m$ independent transformations among $E_1f\cdots E_rf$. The adjoint group has that same number of essential parameters.

We have therefore obtained

**Theorem 49.** *The adjoint group $e_k'=\sum\varrho_{kj}(a)\cdot e_j$ of an $r$-parameter group $X_1f\cdots X_rf$ has $r$ essential parameters if and only if none of the $\infty^{r-1}$ infinitesimal transformations $\sum g_\mu X_\mu f$ is distinguished within $X_1f\cdots X_rf$. It has fewer than $r$ essential parameters—exactly $r-m$—if the group $X_1f\cdots X_rf$ contains exactly $m$ independent distinguished infinitesimal transformations.*\*)

For example, take the group

$$
\frac{\partial f}{\partial x_1}\cdots
\frac{\partial f}{\partial x_r}\qquad(r\leq n).
$$

All its infinitesimal transformations are distinguished, since every $c_{iks}$ is zero. Thus all $r$ expressions $E_1f\cdots E_rf$ vanish identically, and the adjoint group reduces to the identity.

Now take the four-parameter group

$$
x\frac{\partial f}{\partial x},\quad
y\frac{\partial f}{\partial x},\quad
x\frac{\partial f}{\partial y},\quad
y\frac{\partial f}{\partial y}.
$$

It has just one distinguished infinitesimal transformation,

$$
x\frac{\partial f}{\partial x}+y\frac{\partial f}{\partial y};
$$

Its adjoint group therefore has only three parameters.

If $X_1f\cdots X_rf$ contains a distinguished infinitesimal transformation $\sum g_\mu X_\mu f$, then $\sum g_\mu X_\mu f=0$ is a linear partial differential equation invariant under the group. The group is consequently imprimitive (compare p. 221). We conclude that the following proposition holds:

**Proposition 1.** *If $X_1f\cdots X_rf$ is primitive in the variables $x_1\cdots x_n$, it contains no distinguished infinitesimal transformation.*

Combining this proposition with the last theorem gives

**Proposition 2.** *The adjoint group of an $r$-parameter primitive group has $r$ essential parameters.*

Later we shall give these last two propositions a slightly more general formulation (see Chapter 24 on systatic groups).

The infinitesimal transformations of an $r$-parameter group $X_1f\cdots X_rf$ and those of its adjoint group $E_1f\cdots E_rf$ are therefore related as follows. Every infinitesimal transformation $\sum e_kX_kf$ that is not distinguished corresponds to a nonzero infinitesimal transformation $\sum e_kE_kf$. Every distinguished infinitesimal transformation $\sum e_kX_kf$ corresponds to the identity in the adjoint group. Moreover, the two systems

$$
\begin{gathered}
(X_iX_k)=\sum_1^r{}^{s} c_{iks}\cdot X_sf,\\
(E_iE_k)=\sum_1^r{}^{s} c_{iks}\cdot E_sf
\end{gathered}
$$

have exactly the same form. One might therefore conjecture that the adjoint group cannot contain a distinguished infinitesimal transformation. That conjecture would be false. The group $\frac{\partial f}{\partial x_2}$, $x_1\frac{\partial f}{\partial x_2}$, $\frac{\partial f}{\partial x_1}$ provides a counterexample: its adjoint group consists of two commuting infinitesimal transformations and hence contains two independent distinguished infinitesimal transformations.

### English translation of the original footnotes

**F1 · p. 272, at the name “adjoint group”.** [Lie, *Archiv for Math.*, vol. 1, Christiania, 1876.](https://archive.org/details/archivformathema11876oslo)

**F2 · p. 277, after Theorem 49.** [Lie, *Math. Ann.*, vol. XXV, p. 94.](https://gdz.sub.uni-goettingen.de/download/pdf/PPN235181684_0025/PPN235181684_0025.pdf)

## Historical reading: invariant subgroups

Sophus Lie and Friedrich Engel, *Theorie der Transformationsgruppen*, Volume I (1888), complete §74, printed pp. 260–265. [German original](https://archive.org/details/theotransformation01liesrich).

The German original is in the public domain. The transcription and independently written English translation are dedicated to CC0.

### German text: §74

**§74.**

Aus den allgemeinen Entwickelungen der §§69 und 70 werden wir jetzt noch einige weitere Folgerungen ziehen, die von Wichtigkeit sind.

Wir setzen wieder voraus, dass die $r$ unabhängigen infinitesimalen Transformationen $X_1f\cdots X_rf$ in den Beziehungen

$$
(X_iX_k)=\sum_1^r{}^{s} c_{iks}X_sf
$$

stehen, dass also nach Theorem 24 des Kap. 9, S. 158 die $\infty^r$ endlichen Transformationen $\sum e_kX_kf$ eine $r$-gliedrige Gruppe bilden. Bleibt nun die Schaar der Transformationen $\sum e_kX_kf$ bei allen Transformationen einer eingliedrigen Gruppe $Yf$ invariant, welche der $r$-gliedrigen Gruppe nicht angehört, so bestehen nach Theorem 43, S. 252 $r$ Gleichungen von der Form

$$
(YX_k)=\sum_1^r{}^{s} g_{ks}X_sf.\tag{4}
$$

Diese Gleichungen zeigen, dass die $r+1$ infinitesimalen Transformationen $X_1f\cdots X_rf$, $Yf$ eine $(r+1)$-gliedrige Gruppe erzeugen, welcher $X_1f\cdots X_rf$ als $r$-gliedrige Untergruppe angehört.

Ausserdem ist klar, dass die Relationen (4) ihre Form nicht wesentlich ändern, wenn für $Yf$ eine ganz beliebige infinitesimale Transformation der $(r+1)$-gliedrigen Gruppe eingesetzt wird.

Sind daher $x_i'=\psi_i(x_1\cdots x_n;a_1\cdots a_{r+1})$ die endlichen Gleichungen der $(r+1)$-gliedrigen Gruppe, so bleibt die Schaar der endlichen Transformationen $\sum e_kX_kf$ invariant, wenn man in dieselbe an Stelle der $x$ die neuen Veränderlichen $x'$ einführt, d. h. in dem analytischen Ausdrucke der $r$-gliedrigen Gruppe ändern sich nur die Parameter.

Aehnliches würde gelten, wenn man statt der einen Transformation $Yf$ mehrere etwa $m$ solche hätte, welche sämmtlich Relationen von der Form (4) befriedigen; ausserdem wollen wir noch die Voraussetzung hinzufügen, dass diese $m$ infinitesimalen Transformationen $Y_1f\cdots Y_mf$ mit $X_1f\cdots X_rf$ zusammen eine $(r+m)$-gliedrige Gruppe erzeugen. Führen wir alsdann in der Gruppe $X_1f\cdots X_rf$ vermöge einer beliebigen Transformation der $(r+m)$-gliedrigen Gruppe neue Veränderliche ein, so bleibt die Schaar der endlichen Transformationen unserer $r$-gliedrigen Gruppe invariant, während sich allerdings in ihrer analytischen Darstellung die Parameter ändern werden.

Wir wollen diese Beziehung zwischen den beiden Gruppen kurz dadurch ausdrücken, dass wir sagen: *die $r$-gliedrige Gruppe $X_1f\cdots X_rf$ bleibt invariant bei allen Transformationen der $(r+m)$-gliedrigen, sie ist eine invariante Untergruppe derselben.*

Uebertragen wir die in der Substitutionentheorie gebräuchliche Ausdrucksweise, so können wir die Definition der invarianten Untergruppen auch folgendermassen fassen:

Ist $T$ Symbol einer beliebigen Transformation der $(r+m)$-gliedrigen Gruppe $G$, und ist $S$ eine beliebige Transformation einer Untergruppe von $G$, so ist diese Untergruppe in $G$ invariant, wenn stets auch die Transformation $T^{-1}ST$ der betreffenden Untergruppe angehört.

Die analytischen Bedingungen für die Invarianz einer Untergruppe sind in dem oben Gesagten vollständig angegeben; wir brauchen sie daher nur noch einmal zusammenzufassen:

**Theorem 47.** *Ist die $r$-gliedrige Gruppe $X_1f\cdots X_rf$ in einer $(r+m)$-gliedrigen Gruppe $X_1f\cdots X_rf$, $Y_1f\cdots Y_mf$ enthalten, so ist sie eine invariante Untergruppe derselben, wenn jedes $(Y_iX_k)$ sich linear mit constanten Coefficienten durch $X_1f\cdots X_rf$ allein ausdrückt.*

Man kann dem Theorem 47 die folgende allgemeinere, allerdings nur formell allgemeinere Fassung geben:

**Satz 5.** *Bildet der Inbegriff aller infinitesimalen Transformationen $e_1X_1f+\cdots+e_mX_mf$ eine in der $r$-gliedrigen Gruppe $X_1f\cdots X_mf\cdots X_rf$ invariante Schaar, so erzeugen $X_1f\cdots X_mf$ eine $m$-gliedrige invariante Untergruppe der $r$-gliedrigen Gruppe.*

Da nämlich alle $(X_iX_k)$, in denen $i\leq m$ ist, sich aus $X_1f\cdots X_mf$ allein linear ableiten lassen, so gilt das insbesondere von allen $(X_iX_k)$, in denen $i$ und $k$ beide $\leq m$. Demnach erzeugen $X_1f\cdots X_mf$ eine $m$-gliedrige Untergruppe, auf welche sich sofort das Theorem 47 anwenden lässt.

Zunächst einige Beispiele von invarianten Untergruppen.

**Satz 6\*).** *Erzeugen die $r$ unabhängigen infinitesimalen Transformationen $X_1f\cdots X_rf$ eine $r$-gliedrige Gruppe, so erzeugt auch der Inbegriff aller infinitesimalen Transformationen $(X_iX_k)$ eine Gruppe; enthält diese letztere $r$ Parameter, so ist sie mit der Gruppe $X_1f\cdots X_rf$ identisch; enthält sie weniger als $r$ Parameter, so ist sie eine invariante Untergruppe der Gruppe $X_1f\cdots X_rf$; fügt man zu den $(X_iX_k)$ beliebig viele von einander und von den $(X_iX_k)$ unabhängige infinitesimale Transformationen $e_1X_1f+\cdots+e_rX_rf$ hinzu, so erhält man stets wieder eine invariante Untergruppe der Gruppe $X_1f\cdots X_rf$.*

Dass die $(X_iX_k)$ höchstens eine $r$-gliedrige Gruppe erzeugen können, ist klar, da sie alle der Gruppe $X_1f\cdots X_rf$ angehören; dass sie wirklich eine Gruppe erzeugen, ergiebt sich aus den Relationen

$$
(X_iX_k)=\sum_1^r{}^{s} c_{iks}X_sf
$$

sofort, es wird ja:

$$
\bigl((X_iX_k)(X_jX_l)\bigr)
=\sum_{s\sigma}^{1\cdots r} c_{iks}c_{jl\sigma}(X_sX_\sigma).
$$

Dass die von den $(X_iX_k)$ erzeugte Gruppe in der Gruppe $X_1f\cdots X_rf$ invariant ist, erhellt aus den Gleichungen:

$$
\bigl(X_j(X_iX_k)\bigr)
=\sum_1^r{}^{s} c_{iks}(X_jX_s).
$$

Der letzte Theil des Satzes bedarf einer näheren Begründung nicht. Bemerkenswerth ist die folgende Verallgemeinerung des eben bewiesenen Satzes:

**Satz 7.** *Erzeugen $m$ unabhängige infinitesimale Transformationen $Z_1f\cdots Z_mf$ der $r$-gliedrigen Gruppe $X_1f\cdots X_rf$ eine $m$-gliedrige Untergruppe dieser Gruppe, und ist die betreffende Untergruppe in der $r$-gliedrigen invariant, so ist auch die Untergruppe, welche von den sämmtlichen infinitesimalen Transformationen $(Z_\mu Z_\nu)$ erzeugt wird, in der $r$-gliedrigen Gruppe invariant.*

Der Beweis hierfür ist sehr einfach. Unter den Voraussetzungen des Satzes bestehen Relationen von der Gestalt:

$$
\begin{gathered}
(X_kZ_\mu)=\sum_1^m{}^{\lambda} h_{k\mu\lambda}Z_\lambda f
\\
(k=1\cdots r;\ \mu=1\cdots m),
\end{gathered}
$$

wo die $h_{k\mu\lambda}$ Constanten sind. Bilden wir nun die Jacobische Identität (vgl. Kap. 5, S. 94):

$$
\begin{gathered}
\bigl(X_k(Z_\mu Z_\nu)\bigr)\\
+\bigl(Z_\mu(Z_\nu X_k)\bigr)\\
+\bigl(Z_\nu(X_kZ_\mu)\bigr)=0
\end{gathered}
$$

und setzen in derselben für $(Z_\mu X_k)$ und $(Z_\nu X_k)$ die vorhin geschriebenen Ausdrücke, so erhalten wir die Gleichungen:

$$
\begin{gathered}
\bigl(X_k(Z_\mu Z_\nu)\bigr)\\
=\sum_1^m{}^{\lambda}
\bigl\{h_{k\nu\lambda}(Z_\mu Z_\lambda)\\
-h_{k\mu\lambda}(Z_\nu Z_\lambda)\bigr\},
\end{gathered}
$$

aus denen hervorgeht, dass die von den $(Z_\mu Z_\nu)$ erzeugte Untergruppe der Gruppe $X_1f\cdots X_rf$ in dieser letzteren invariant ist. Das aber war zu beweisen. —

Die $r$-gliedrige Gruppe $X_1f\cdots X_rf$ oder kurz $G_r$ enthalte eine $(r-1)$-gliedrige invariante Untergruppe und es seien $r$ unabhängige infinitesimale Transformationen $Y_1f\cdots Y_rf$ der $G_r$ so ausgewählt, dass $Y_1f\cdots Y_{r-1}f$ diese invariante Untergruppe ist. Dann bestehen Relationen von der Form:

$$
\begin{gathered}
(Y_iY_k)=c_{ik1}Y_1f+\cdots+c_{ik,r-1}Y_{r-1}f
\\
(i,k=1\cdots r),
\end{gathered}
$$

es lassen sich also alle $(Y_iY_k)$ und natürlich auch alle $(X_iX_k)$ aus $Y_1f\cdots Y_{r-1}f$ allein linear ableiten. Wir schliessen hieraus, dass jede $(r-1)$-gliedrige invariante Untergruppe der $G_r$ die sämmtlichen infinitesimalen Transformationen $(X_iX_k)$ enthält und erkennen so, dass der folgende Satz gilt:

**Satz 8.** *In der $r$-gliedrigen Gruppe $X_1f\cdots X_rf$ giebt es dann und nur dann eine $(r-1)$-gliedrige Untergruppe, wenn die infinitesimalen Transformationen $(X_iX_k)$ eine Gruppe mit weniger als $r$ Parametern erzeugen; sind unter den $(X_iX_k)$ gerade $r_1<r$ von einander unabhängige infinitesimale Transformationen vorhanden, so erhält man alle $(r-1)$-gliedrigen invarianten Untergruppen der Gruppe $X_1f\cdots X_rf$, wenn man zu den $(X_iX_k)$ in allgemeinster Weise $r-r_1-1$ von einander und von den $(X_iX_k)$ unabhängige infinitesimale Transformationen $e_1X_1f+\cdots+e_rX_rf$ hinzufügt.*

Der Satz 1 in Kap. 12, Seite 205 liefert uns andere Beispiele von invarianten Untergruppen.

Enthielt nämlich eine Gruppe in der Umgebung eines Punktes $x_1^0\cdots x_n^0$ infinitesimale Transformationen von erster und von höherer Ordnung in den $x_i-x_i^0$, so erzeugten jedesmal alle infinitesimalen Transformationen von $k$-ter $(k>0)$ und höherer Ordnung eine Untergruppe. Nun liefern zwei infinitesimale Transformationen $Xf$ und $Yf$ von bezüglich $k$-ter und $(k+v)$-ter Ordnung durch Klammeroperation eine Transformation $(XY)$ von der Ordnung $2k+v-1$. Wegen $k>0$ ist $2k+v-1\geq k+v$, folglich muss sich $(XY)$ aus den infinitesimalen Transformationen von $(k+v)$-ter und höherer Ordnung linear ableiten lassen. Mit andern Worten: die sämmtlichen infinitesimalen Transformationen von $(k+v)$-ter und höherer Ordnung erzeugen eine Gruppe, welche in der von den infinitesimalen Transformationen $k$-ter und höherer Ordnung erzeugten Gruppe invariant ist. Alles das gilt aber wie gesagt nur unter der Voraussetzung, dass die Zahl $k$ grösser ist als Null.

Lassen sich insbesondere die Zahlen $k$ und $k+v$ so wählen, dass die Gruppe in der Umgebung von $x_1^0\cdots x_n^0$ keine infinitesimalen Transformationen von $(2k+v-1)$-ter und höherer Ordnung enthält, so muss der Ausdruck $(XY)$ identisch verschwinden. Es gilt daher der

**Satz 9.** *Enthält eine Gruppe in der Umgebung eines Punktes $x_1^0\cdots x_n^0$ keine infinitesimalen Transformationen von $(s+1)$-ter oder höherer Ordnung, enthält sie dagegen Transformationen von $k$-ter Ordnung, wo $k$ die Bedingung $2k-1>s$ erfüllt, so erzeugen alle infinitesimalen Transformationen der Gruppe, welche von $k$-ter und höherer Ordnung sind, eine Gruppe mit paarweise vertauschbaren Transformationen.*

Der Punkt $x_1^0\cdots x_n^0$ braucht hier keineswegs so beschaffen zu sein, dass sich für denselben die Coefficienten der aufgelösten Definitionsgleichungen der Gruppe (vgl. Kap. 11, S. 189 ff.) regulär verhalten. —

Consequenterweise muss man sagen, dass jede endliche continuirliche Gruppe zwei invariante Untergruppen enthält, nämlich erstens sich selbst und zweitens die identische Transformation. Man erkennt das, wenn man in dem Theorem 47 einmal $m$, das andere Mal $r$ gleich Null setzt; in beiden Fällen ist die Bedingung für die Invarianz der Untergruppe $X_1f\cdots X_rf$ von selbst erfüllt, sobald nur $X_1f\cdots X_rf$, $Y_1f\cdots Y_mf$ eine $(r+m)$-gliedrige Gruppe ist.

Von besonderer Wichtigkeit sind die Gruppen, welche, abgesehen von den beiden immer vorhandenen, gar keine invariante Untergruppe enthalten. Diese Gruppen sollen deshalb auch einen besonderen Namen haben, sie sollen *einfache Gruppen* heissen. Im Gegensatze dazu heisst eine Gruppe *zusammengesetzt*, wenn sie ausser den oben angegebenen zwei noch andere invariante Untergruppen enthält.

Zum Schlusse noch zwei Sätze über invariante Untergruppen:

**Satz 10.** *Die gemeinsamen Transformationen zweier invarianten Untergruppen einer Gruppe $G$ bilden ebenfalls eine in $G$ invariante Untergruppe.*

Eine Untergruppe von $G$ bilden die betreffenden Transformationen sicher (vgl. Kap. 9, Satz 2, S. 159); diese Untergruppe muss in $G$ invariant sein, da sie bei allen Transformationen von $G$ in eine Gruppe übergeht, welche den beiden invarianten Untergruppen angehört, d. h. in sich selbst.

**Satz 11.** *Haben zwei invariante Untergruppen $Y_1f\cdots Y_mf$ und $Z_1f\cdots Z_pf$ einer Gruppe $G$ keine infinitesimale Transformation gemein, so verschwinden alle Ausdrücke $(Y_iZ_k)$ identisch, das heisst es ist jede Transformation der einen Untergruppe mit jeder Transformation der andern Untergruppe vertauschbar.*

Jeder Ausdruck $(Y_iZ_k)$ muss sich nämlich unter den gemachten Voraussetzungen sowohl durch $Y_1f\cdots Y_mf$ als durch $Z_1f\cdots Z_pf$ linear mit constanten Coefficienten ausdrücken; da aber beide Untergruppen keine infinitesimale Transformation gemein haben, so geht das nicht anders, als indem alle Ausdrücke $(Y_iZ_k)$ identisch verschwinden. Das Uebrige folgt aus dem Satze 4, S. 259.

### German original footnote for §74

**F1 · p. 261, at Satz 6.** Im [Archiv for Mathematik og Naturvidenskab Bd. 8, S. 390, Christiania 1883](https://archive.org/details/archivformathema81883oslo) bemerkte Lie, dass die $(X_iX_k)$ eine invariante Untergruppe bilden. Davon unabhängig hat Killing dies im Jahre 1886 erkannt.

### English translation: §74

**§74.**

We shall now draw some further consequences from the general developments of §§69 and 70, which are important.

We again suppose that the $r$ independent infinitesimal transformations $X_1f\cdots X_rf$ satisfy

$$
(X_iX_k)=\sum_1^r{}^{s} c_{iks}X_sf
$$

and hence, by Theorem 24 of Chapter 9, p. 158, the $\infty^r$ finite transformations $\sum e_kX_kf$ form an $r$-parameter group. Now, if the family of transformations $\sum e_kX_kf$ is invariant under every transformation of a one-parameter group $Yf$ that does not belong to the $r$-parameter group, then Theorem 43, p. 252, gives $r$ equations of the form

$$
(YX_k)=\sum_1^r{}^{s} g_{ks}X_sf.\tag{4}
$$

These equations show that the $r+1$ infinitesimal transformations $X_1f\cdots X_rf$, $Yf$ generate an $(r+1)$-parameter group containing $X_1f\cdots X_rf$ as an $r$-parameter subgroup.

It is also clear that relations (4) do not change their form substantially if $Yf$ is replaced by any infinitesimal transformation of the $(r+1)$-parameter group.

Thus, if $x_i'=\psi_i(x_1\cdots x_n;a_1\cdots a_{r+1})$ are the finite equations of the $(r+1)$-parameter group, the family of finite transformations $\sum e_kX_kf$ remains invariant when the new variables $x'$ are substituted for the $x$ in it. In other words, only the parameters change in the analytic expression of the $r$-parameter group.

The same would hold if, instead of the single transformation $Yf$, we had several, say $m$, transformations, all satisfying relations of the form (4). Moreover, we shall add the assumption that these $m$ infinitesimal transformations $Y_1f\cdots Y_mf$, together with $X_1f\cdots X_rf$, generate an $(r+m)$-parameter group. If we then introduce new variables into the group $X_1f\cdots X_rf$ by any transformation of the $(r+m)$-parameter group, the family of finite transformations of our $r$-parameter group remains invariant, although its parameters change in the analytic representation.

We shall express this relation between the two groups briefly by saying: *the $r$-parameter group $X_1f\cdots X_rf$ is invariant under every transformation of the $(r+m)$-parameter group; it is an invariant subgroup of that group.*

Using the terminology customary in substitution theory, we can also define invariant subgroups as follows.

Let $T$ denote any transformation of the $(r+m)$-parameter group $G$, and let $S$ be any transformation of a subgroup of $G$. That subgroup is invariant in $G$ if the transformation $T^{-1}ST$ always belongs to the subgroup as well.

The analytic conditions for invariance of a subgroup have been fully stated above; we therefore need only summarize them once more.

**Theorem 47.** *If the $r$-parameter group $X_1f\cdots X_rf$ is contained in an $(r+m)$-parameter group $X_1f\cdots X_rf$, $Y_1f\cdots Y_mf$, it is an invariant subgroup of that group when every $(Y_iX_k)$ can be expressed linearly through $X_1f\cdots X_rf$ alone with constant coefficients.*

Theorem 47 can be given the following more general formulation, although the greater generality is only formal.

**Proposition 5.** *If the collection of all infinitesimal transformations $e_1X_1f+\cdots+e_mX_mf$ is an invariant family in the $r$-parameter group $X_1f\cdots X_mf\cdots X_rf$, then $X_1f\cdots X_mf$ generates an $m$-parameter invariant subgroup of the $r$-parameter group.*

Indeed, every $(X_iX_k)$ with $i\leq m$ can be obtained as a linear combination of $X_1f\cdots X_mf$ alone. This holds, in particular, for all $(X_iX_k)$ for which $i$ and $k$ are both $\leq m$. Consequently, $X_1f\cdots X_mf$ generates an $m$-parameter subgroup, to which Theorem 47 applies immediately.

We first give some examples of invariant subgroups.

**Proposition 6\*).** *If the $r$ independent infinitesimal transformations $X_1f\cdots X_rf$ generate an $r$-parameter group, then the collection of all infinitesimal transformations $(X_iX_k)$ also generates a group. If the latter has $r$ parameters, it is identical with $X_1f\cdots X_rf$; if it has fewer than $r$ parameters, it is an invariant subgroup of $X_1f\cdots X_rf$. Adding to the $(X_iX_k)$ any number of infinitesimal transformations $e_1X_1f+\cdots+e_rX_rf$ that are independent of one another and of the $(X_iX_k)$ always gives another invariant subgroup of $X_1f\cdots X_rf$.*

It is clear that the $(X_iX_k)$ can generate a group with at most $r$ parameters, since they all belong to $X_1f\cdots X_rf$. The relations

$$
(X_iX_k)=\sum_1^r{}^{s} c_{iks}X_sf
$$

show at once that they do generate a group, for

$$
\bigl((X_iX_k)(X_jX_l)\bigr)
=\sum_{s\sigma}^{1\cdots r} c_{iks}c_{jl\sigma}(X_sX_\sigma).
$$

The equations

$$
\bigl(X_j(X_iX_k)\bigr)
=\sum_1^r{}^{s} c_{iks}(X_jX_s).
$$

show that the group generated by the $(X_iX_k)$ is invariant in $X_1f\cdots X_rf$.

The last part of the proposition needs no further justification. The following generalization of the proposition just proved deserves attention.

**Proposition 7.** *If $m$ independent infinitesimal transformations $Z_1f\cdots Z_mf$ of the $r$-parameter group $X_1f\cdots X_rf$ generate an $m$-parameter subgroup of this group, and if that subgroup is invariant in the $r$-parameter group, then the subgroup generated by all the infinitesimal transformations $(Z_\mu Z_\nu)$ is also invariant in the $r$-parameter group.*

The proof is very simple. Under the assumptions of the proposition, there are relations of the form

$$
\begin{gathered}
(X_kZ_\mu)=\sum_1^m{}^{\lambda} h_{k\mu\lambda}Z_\lambda f
\\
(k=1\cdots r;\ \mu=1\cdots m),
\end{gathered}
$$

where the $h_{k\mu\lambda}$ are constants. Form the Jacobi identity (compare Chapter 5, p. 94)

$$
\begin{gathered}
\bigl(X_k(Z_\mu Z_\nu)\bigr)\\
+\bigl(Z_\mu(Z_\nu X_k)\bigr)\\
+\bigl(Z_\nu(X_kZ_\mu)\bigr)=0
\end{gathered}
$$

and substitute the expressions given above for $(Z_\mu X_k)$ and $(Z_\nu X_k)$. We obtain

$$
\begin{gathered}
\bigl(X_k(Z_\mu Z_\nu)\bigr)\\
=\sum_1^m{}^{\lambda}
\bigl\{h_{k\nu\lambda}(Z_\mu Z_\lambda)\\
-h_{k\mu\lambda}(Z_\nu Z_\lambda)\bigr\},
\end{gathered}
$$

These equations show that the subgroup generated by the $(Z_\mu Z_\nu)$ is invariant in $X_1f\cdots X_rf$, as required. —

Suppose that the $r$-parameter group $X_1f\cdots X_rf$, or briefly $G_r$, contains an $(r-1)$-parameter invariant subgroup. Choose $r$ independent infinitesimal transformations $Y_1f\cdots Y_rf$ of $G_r$ so that $Y_1f\cdots Y_{r-1}f$ is this invariant subgroup. Then there are relations of the form

$$
\begin{gathered}
(Y_iY_k)=c_{ik1}Y_1f+\cdots+c_{ik,r-1}Y_{r-1}f
\\
(i,k=1\cdots r),
\end{gathered}
$$

Thus all the $(Y_iY_k)$, and of course all the $(X_iX_k)$, can be expressed as linear combinations of $Y_1f\cdots Y_{r-1}f$ alone. We conclude that every $(r-1)$-parameter invariant subgroup of $G_r$ contains all the infinitesimal transformations $(X_iX_k)$, and obtain the following proposition.

**Proposition 8.** *The $r$-parameter group $X_1f\cdots X_rf$ has an $(r-1)$-parameter subgroup if and only if its infinitesimal transformations $(X_iX_k)$ generate a group with fewer than $r$ parameters. If exactly $r_1<r$ independent infinitesimal transformations occur among the $(X_iX_k)$, all $(r-1)$-parameter invariant subgroups of $X_1f\cdots X_rf$ are obtained by adding to the $(X_iX_k)$, in the most general way, $r-r_1-1$ infinitesimal transformations $e_1X_1f+\cdots+e_rX_rf$ independent of one another and of the $(X_iX_k)$.*

Proposition 1 in Chapter 12, p. 205, supplies further examples of invariant subgroups.

If a group has infinitesimal transformations of first and higher order in the $x_i-x_i^0$ near a point $x_1^0\cdots x_n^0$, then all its infinitesimal transformations of order $k$ $(k>0)$ and higher generate a subgroup. Now take infinitesimal transformations $Xf$ and $Yf$ of orders $k$ and $(k+v)$, respectively, and form their bracket $(XY)$, of order $2k+v-1$. Since $k>0$, we have $2k+v-1\geq k+v$. Hence $(XY)$ must be a linear combination of the infinitesimal transformations of order $(k+v)$ and higher. In other words, all the infinitesimal transformations of order $(k+v)$ and higher generate a group invariant in the group generated by the infinitesimal transformations of order $k$ and higher. As stated, all this holds only under the assumption that $k$ is greater than zero.

In particular, if $k$ and $k+v$ can be chosen so that the group has no infinitesimal transformations of order $(2k+v-1)$ and higher near $x_1^0\cdots x_n^0$, then $(XY)$ must vanish identically. We therefore have

**Proposition 9.** *Suppose a group has no infinitesimal transformations of order $(s+1)$ or higher near a point $x_1^0\cdots x_n^0$, but has transformations of order $k$, where $k$ satisfies $2k-1>s$. Then all its infinitesimal transformations of order $k$ and higher generate a group whose transformations commute pairwise.*

The point $x_1^0\cdots x_n^0$ need not be one where the coefficients of the group's solved defining equations (compare Chapter 11, p. 189 ff.) behave regularly. —

For consistency, we must say that every finite continuous group contains two invariant subgroups: itself and the identity transformation. This follows by putting first $m$, then $r$, equal to zero in Theorem 47. In either case, the condition for invariance of the subgroup $X_1f\cdots X_rf$ is automatically satisfied, provided that $X_1f\cdots X_rf$, $Y_1f\cdots Y_mf$ forms an $(r+m)$-parameter group.

Groups which contain no invariant subgroup at all, apart from the two that are always present, are especially important. These groups should therefore also have a special name: they shall be called *simple groups*. In contrast, a group is called *composite* if it has invariant subgroups besides the two just described.

We finish with two further propositions about invariant subgroups.

**Proposition 10.** *The transformations common to two invariant subgroups of a group $G$ also form an invariant subgroup in $G$.*

These transformations certainly form a subgroup of $G$ (compare Chapter 9, Proposition 2, p. 159). That subgroup must be invariant in $G$, since every transformation of $G$ carries it to a group belonging to both invariant subgroups, hence to itself.

**Proposition 11.** *If two invariant subgroups $Y_1f\cdots Y_mf$ and $Z_1f\cdots Z_pf$ of a group $G$ have no infinitesimal transformation in common, all expressions $(Y_iZ_k)$ vanish identically. That is, every transformation of one subgroup commutes with every transformation of the other.*

Under the stated assumptions, each $(Y_iZ_k)$ must be expressible both through $Y_1f\cdots Y_mf$ and through $Z_1f\cdots Z_pf$ as a linear combination with constant coefficients. Since the two subgroups have no infinitesimal transformation in common, this is possible only if all $(Y_iZ_k)$ vanish identically. The remainder follows from Proposition 4, p. 259.

### English translation of the original footnote for §74

**F1 · p. 261, at Proposition 6.** In [*Archiv for Mathematik og Naturvidenskab*, vol. 8, p. 390, Christiania, 1883](https://archive.org/details/archivformathema81883oslo), Lie observed that the $(X_iX_k)$ form an invariant subgroup. Killing independently recognized this in 1886.

## Historical reading: reciprocal groups

Sophus Lie and Friedrich Engel, *Theorie der Transformationsgruppen*, Volume I (1888), Chapter 20 introduction and complete §§95–97, printed pp. 367–390. [German original](https://archive.org/details/theotransformation01liesrich).

The German original is in the public domain. The transcription and independently written English translation are dedicated to CC0.

### German text: commuting transformations and reciprocal groups

**Kapitel 20. Gruppen, deren Transformationen mit allen Transformationen einer vorgelegten Gruppe vertauschbar sind.**

Durch die Entwickelungen der §§89, 90, 91, S. 330 bis 355 sind wir in den Stand gesetzt, alle Transformationen zu bestimmen, welche eine vorgelegte $r$-gliedrige Gruppe:

$$
X_kf=\sum_1^s{}^{i}\xi_{ki}(x_1\cdots x_s)\frac{\partial f}{\partial x_i}
\qquad(k=1\cdots r)
$$

invariant lassen. Wir wollen nun unter allen Transformationen von dieser Beschaffenheit diejenigen herausgreifen, welche ausserdem noch die Eigenschaft besitzen, *jede einzelne Transformation der Gruppe $X_1f\cdots X_rf$ invariant zu lassen* und wollen uns mit diesen Transformationen etwas näher beschäftigen.

Wenn eine Transformation $T$ jede einzelne Transformation $S$ der Gruppe $X_1f\cdots X_rf$ invariant lässt, so steht sie nach S. 258 zu $S$ in Beziehung:

$$
T^{-1}ST=S
$$

oder, was dasselbe ist, in der Beziehung:

$$
ST=TS,
$$

sie ist also mit $T$ vertauschbar. Demnach können wir die eben definirten Transformationen auch folgendermassen charakterisiren: *es sind diejenigen Transformationen, welche mit sämmtlichen Transformationen der Gruppe $X_1f\cdots X_rf$ vertauschbar sind.*

**§95.**

Nach Kap. 15, S. 255 kann der Ausdruck $e_1X_1f+\cdots+e_rX_rf$ als das allgemeine Symbol einer Transformation der Gruppe $X_1f\cdots X_rf$ angesehen werden. Folglich wird eine Transformation $x_i'=\Phi_i(x_1\cdots x_s)$ stets dann aber auch nur dann jede einzelne Transformation der Gruppe $X_1f\cdots X_rf$ invariant lassen, wenn sie den Ausdruck $e_1X_1f+\cdots+e_rX_rf$ bei beliebiger Wahl der $e$ invariant lässt, wenn also der Ausdruck $e_1X_1f+\cdots+e_rX_rf$ bei Einführung der neuen Veränderlichen $x_i'=\Phi_i(x)$ die Form: $e_1X_1'f+\cdots+e_rX_r'f$ annimmt, wo:

$$
X_k'f=\sum_1^s{}^{i}\xi_{ki}(x_1'\cdots x_s')\frac{\partial f}{\partial x_i'}
$$

ist. Nothwendige und hinreichende Bedingung hierfür ist, dass die $r$ infinitesimalen Transformationen: $X_1f\cdots X_rf$ bei Einführung der neuen Veränderlichen $x_i'$ bezüglich die Formen $X_1'f\cdots X_r'f$ erhalten.

Dass es Transformationen $x_i'=\Phi_i(x)$ von der verlangten Beschaffenheit giebt, ist klar; die identische Transformation $x_i'=x_i$ ist ja eine solche; überdies geht es aus dem Satze 2 des vorigen Kapitels (S. 354) hervor; denn dieser Satz zeigt, dass es Transformationen giebt, welche $X_1f\cdots X_rf$ in bezüglich $X_1'f\cdots X_r'f$ überführen. Aus den damaligen Entwickelungen folgt überdies, dass die allgemeinste Transformation von der verlangten Beschaffenheit dargestellt wird durch das allgemeinste nach $x_1\cdots x_s$ auflösbare Gleichungensystem:

$$
\begin{gathered}
x_1'=\Phi_1(x_1\cdots x_s),\\
\cdots,\\

x_s'=\Phi_s(x_1\cdots x_s),
\end{gathered}
$$

welches die $r$-gliedrige Gruppe: $X_1f+X_1'f$, $\cdots$, $X_rf+X_r'f$ in den $2s$ Veränderlichen $x_1\cdots x_s$, $x_1'\cdots x_s'$ gestattet.

Führt man nach einander zwei Transformationen aus, welche jede einzelne Transformation der Gruppe: $X_1f\cdots X_rf$ invariant lassen, so erhält man offenbar stets eine Transformation, welche dasselbe thut; also bildet der Inbegriff aller Transformationen von dieser Beschaffenheit eine Gruppe $G$. Diese Gruppe kann discontinuirlich sein, ja sogar auf die identische Transformation zusammenschrumpfen; sie kann aus mehreren discreten Schaaren bestehen, von denen jede nur eine endliche Anzahl willkürlicher Parameter enthält, sie kann unendlich sein: immer aber ordnen sich ihre Transformationen paarweise als inverse zusammen, denn lässt eine Transformation alle Transformationen der Gruppe: $X_1f\cdots X_rf$ invariant, so besitzt die zugehörige inverse Transformation natürlich dieselbe Eigenschaft.

Enthält die eben definirte Gruppe $G$ nur eine endliche Anzahl von willkürlichen Parametern, so gehört sie in die Kategorie von Gruppen, welche in Kapitel 18 besprochen ist, und umfasst nach Theorem 56, S. 315 sicher eine von infinitesimalen Transformationen erzeugte, endliche continuirliche Untergruppe. Ist andererseits die Gruppe $G$ unendlich, so lässt sich durch ähnliche Betrachtungen wie in Kapitel 18 nachweisen, dass sie eingliedrige Gruppen umfasst, und zwar unendlich viele, die von unendlich vielen unabhängigen infinitesimalen Transformationen erzeugt sind.

Wir stellen uns jetzt direkt die Aufgabe, alle eingliedrigen Gruppen zu bestimmen, die etwa in der Gruppe $G$ enthalten sind.

Nach Kap. 15, S. 258 und 259 bleiben die $r$ Ausdrücke $X_1f\cdots X_rf$ dann und nur dann bei allen Transformationen der eingliedrigen Gruppe $Zf$ invariant, wenn die $r$ Relationen:

$$
\begin{gathered}
(X_kZ)=X_k(Z(f))-Z(X_k(f))=0
\\
(k=1\cdots r)
\end{gathered}
$$

identisch erfüllt sind, wenn also die infinitesimale Transformation $Zf$ mit allen Transformationen der Gruppe $X_1f\cdots X_rf$ vertauschbar ist.

Demnach kommt die Bestimmung aller eingliedrigen Gruppen von der vorhin definirten Beschaffenheit hinaus auf die Bestimmung der allgemeinsten infinitesimalen Transformation $Zf$, welche mit allen $X_kf$ vertauschbar ist.

Hat man zwei infinitesimale Transformationen $Z_1f$ und $Z_2f$, welche mit allen $X_kf$ vertauschbar sind, so verschwinden alle Ausdrücke $(Z_1X_k)$ und $(Z_2X_k)$ identisch, also reducirt sich die Jacobische Identität:

$$
\bigl((Z_1Z_2)X_k\bigr)+\bigl((Z_2X_k)Z_1\bigr)
+\bigl((X_kZ_1)Z_2\bigr)=0
$$

auf:

$$
\bigl((Z_1Z_2)X_k\bigr)\equiv0.
$$

Es gilt demnach der

**Satz 1.** *Sind die beiden infinitesimalen Transformationen $Z_1f$ und $Z_2f$ mit allen infinitesimalen Transformationen der $r$-gliedrigen Gruppe $X_1f\cdots X_rf$ vertauschbar, so ist es auch die Transformation $(Z_1Z_2)$.*

Auf der andern Seite ist zugleich jede infinitesimale Transformation $aZ_1f+bZ_2f$ mit $X_1f\cdots X_rf$ vertauschbar, welche Werthe auch die Constanten $a$ und $b$ haben mögen. Giebt es daher zufällig nur eine endliche Anzahl, etwa nur $q$ unabhängige infinitesimale Transformationen $Z_1f\cdots Z_qf$, welche mit $X_1f\cdots X_rf$ vertauschbar sind, so hat die allgemeinste infinitesimale Transformation von derselben Beschaffenheit die Form: $\lambda_1Z_1f+\cdots+\lambda_qZ_qf$, unter $\lambda_1\cdots\lambda_q$ willkürliche Parameter verstanden. Es müssen dann wegen Satz 1 Relationen von der Form:

$$
(Z_iZ_k)=\sum_1^q{}^{\sigma} c'_{ik\sigma}Z_\sigma f
$$

bestehen, so dass also *$Z_1f\cdots Z_qf$ eine $q$-gliedrige Gruppe erzeugen.*

Versuchen wir jetzt direkt die allgemeinste infinitesimale Transformation:

$$
Zf=\sum_1^s{}^{i}\xi_i(x_1\cdots x_s)\frac{\partial f}{\partial x_i}
$$

zu bestimmen, welche mit allen infinitesimalen Transformationen der Gruppe $X_1f\cdots X_rf$ vertauschbar ist.

Die $r$ Bedingungsgleichungen:

$$
(X_1Z)=0,\quad\cdots,\quad(X_rZ)=0
$$

zerfallen sofort in die $rs$ folgenden:

$$
X_k\xi_i=Z\xi_{ki}\qquad(k=1\cdots r;\ i=1\cdots s),
$$

oder ausführlich geschrieben:

$$
\begin{gathered}
\sum_1^s{}^{\nu}\xi_{k\nu}(x)\frac{\partial\xi_i}{\partial x_\nu}\\
=\sum_1^s{}^{\nu}\frac{\partial\xi_{ki}}{\partial x_\nu}\xi_\nu
\\
(k=1\cdots r;\ i=1\cdots s).
\end{gathered}\tag{1}
$$

Es handelt sich also darum, die allgemeinsten Lösungen dieser Differentialgleichungen für $\xi_1\cdots\xi_s$ zu bestimmen.

Ist

$$
\xi_i=\omega_i(x_1\cdots x_s)\qquad(i=1\cdots s)\tag{2}
$$

irgend ein Lösungensystem von (1), so verschwinden die Ausdrücke:

$$
X_k\omega_i-\sum_1^s{}^{\nu}\frac{\partial\xi_{ki}}{\partial x_\nu}\xi_\nu
$$

bei der Substitution: $\xi_1=\omega_1(x)$, $\cdots$, $\xi_s=\omega_s(x)$ sämmtlich identisch, mit anderen Worten: das Gleichungensystem (2) in den $2s$ Veränderlichen $x_1\cdots x_s$, $\xi_1\cdots\xi_s$ gestattet die $r$ infinitesimalen Transformationen:

$$
\begin{gathered}
W_kf=X_kf+\sum_1^s{}^{i}
\bigl\{\sum_1^s{}^{\nu}\frac{\partial\xi_{ki}}{\partial x_\nu}\xi_\nu\bigr\}
\frac{\partial f}{\partial\xi_i}
\\
(k=1\cdots r).
\end{gathered}
$$

Gestattet umgekehrt ein Gleichungensystem von der Form (2) die infinitesimalen Transformationen $W_1f\cdots W_rf$, so sind $\omega_1(x)\cdots\omega_s(x)$ offenbar Lösungen der Differentialgleichungen (1). Folglich ist die Integration der Differentialgleichungen (1) äquivalent mit der Bestimmung des allgemeinsten Gleichungensystems (2), welches die infinitesimalen Transformationen $W_1f\cdots W_rf$ gestattet.

Jedes Gleichungensystem, welches $W_1f\cdots W_rf$ gestattet, lässt auch die infinitesimale Transformation $W_k(W_j(f))-W_j(W_k(f))=(W_kW_j)$ zu; berechnen wir dieselbe.

Es wird:

$$
\begin{gathered}
(W_kW_j)={}(X_kX_j)\\
+\sum_{i\mu\nu}^{1\cdots s}
\bigl\{\xi_{k\nu}\frac{\partial^2\xi_{ji}}{\partial x_\mu\partial x_\nu}\\
-\xi_{j\nu}\frac{\partial^2\xi_{ki}}{\partial x_\mu\partial x_\nu}\bigr\}\\
\xi_\mu\frac{\partial f}{\partial\xi_i}\\
+\sum_{i\mu\nu}^{1\cdots s}
\bigl\{\frac{\partial\xi_{k\nu}}{\partial x_\mu}
\frac{\partial\xi_{ji}}{\partial x_\nu}\\
-\frac{\partial\xi_{j\nu}}{\partial x_\mu}
\frac{\partial\xi_{ki}}{\partial x_\nu}\bigr\}\\
\xi_\mu\frac{\partial f}{\partial\xi_i},
\end{gathered}
$$

und hier lässt sich die rechte Seite schreiben:

$$
\begin{gathered}
(X_kX_j)+\sum_{i\mu}^{1\cdots s}\frac{\partial}{\partial x_\mu}
\sum_1^s{}^{\nu}
\bigl\{\xi_{k\nu}\frac{\partial\xi_{ji}}{\partial x_\nu}\\
-\xi_{j\nu}\frac{\partial\xi_{ki}}{\partial x_\nu}\bigr\}\\
\xi_\mu\frac{\partial f}{\partial\xi_i}.
\end{gathered}
$$

Nun aber bestehen Relationen von der Form:

$$
(X_kX_j)=\sum_1^r{}^{\sigma} c_{kj\sigma}X_\sigma f,
$$

aus denen folgt:

$$
\sum_1^s{}^{\nu}
\left\{\xi_{k\nu}\frac{\partial\xi_{ji}}{\partial x_\nu}
-\xi_{j\nu}\frac{\partial\xi_{ki}}{\partial x_\nu}\right\}
=\sum_1^r{}^{\sigma} c_{kj\sigma}\xi_{\sigma i},
$$

mithin ergiebt sich einfach:

$$
(W_kW_j)=\sum_1^r{}^{\sigma} c_{kj\sigma}W_\sigma f.
$$

Wir ersehen hieraus, dass $W_1f\cdots W_rf$ eine $r$-gliedrige Gruppe in den $2s$ Veränderlichen $x_1\cdots x_s$, $\xi_1\cdots\xi_s$ erzeugen; das zu vermuthen lag allerdings nahe.

Es mögen unter den infinitesimalen Transformationen $X_1f\cdots X_rf$ irgend $n$, etwa $X_1f\cdots X_nf$ durch keine lineare Relation von der Form:

$$
\begin{gathered}
\chi_1(x_1\cdots x_s)\cdot X_1f\\
+\cdots+
\chi_n(x_1\cdots x_s)\cdot X_nf=0
\end{gathered}
$$

verknüpft sein, während $X_{n+1}f\cdots X_rf$ sich folgendermassen ausdrücken lassen:

$$
\begin{gathered}
X_{n+k}f=\sum_1^n{}^{\rho}\varphi_{k\rho}(x_1\cdots x_s)\cdot X_\rho f
\\
(k=1\cdots r-n).
\end{gathered}\tag{3}
$$

Unter diesen Voraussetzungen lassen sich die Differentialgleichungen (1) auch schreiben:

$$
X_\rho\xi_i-Z\xi_{\rho i}=0
\qquad(\rho=1\cdots n;\ i=1\cdots s)
$$

$$
\begin{gathered}
\sum_1^n{}^{\rho}\varphi_{k\rho}(x)\cdot X_\rho\xi_i-Z\xi_{n+k,i}=0
\\
(k=1\cdots r-n;\ i=1\cdots s).
\end{gathered}
$$

Werden daher die Ausdrücke $X_1\xi_i\cdots X_n\xi_i$ weggeschafft, so ergeben sich zwischen $\xi_1\cdots\xi_s$ die endlichen Gleichungen:

$$
\begin{gathered}
\sum_1^s{}^{\pi}
\bigl\{\frac{\partial\xi_{n+k,i}}{\partial x_\pi}\\
-\sum_1^n{}^{\rho}\varphi_{k\rho}\frac{\partial\xi_{\rho i}}{\partial x_\pi}\bigr\}
\xi_\pi=0
\\
(k=1\cdots r-n;\ i=1\cdots s).
\end{gathered}\tag{4}
$$

Es leuchtet ein, dass jedes Gleichungensystem von der Form (2), welches die Gruppe $W_1f\cdots W_rf$ gestattet, die Gleichungen (4) umfassen muss.

Die Gleichungen (4) sind linear und homogen in $\xi_1\cdots\xi_s$; finden sich daher unter ihnen gerade $s$ von einander unabhängige, so ist $\xi_1=0$, $\cdots$, $\xi_s=0$ das einzige Lösungensystem, welches sie alle befriedigt. In diesem Falle giebt es nur ein Gleichungensystem von der Form (2), welches die Gruppe $W_1f\cdots W_rf$ gestattet, nämlich das Gleichungensystem: $\xi_1=0$, $\cdots$, $\xi_s=0$, es giebt also keine infinitesimale Transformation $Zf$, welche mit allen $X_kf$ vertauschbar ist.

Anders, wenn sich die Gleichungen (4) auf weniger als $s$, etwa auf $m<s$ unabhängige Gleichungen reduciren. Wir werden sehen, dass es in diesem Falle ausser dem unbrauchbaren Systeme $\xi_1=0$, $\cdots$, $\xi_s=0$ auch noch andere Systeme von der Form (2) giebt, welche die Gruppe $W_1f\cdots W_rf$ gestatten.

Vor allen Dingen bemerken wir, dass das Gleichungensystem (4) die Gruppe $W_1f\cdots W_rf$ gestattet.

Um das zu beweisen, schreiben wir uns die Matrix auf, welche zu den infinitesimalen Transformationen $W_1f\cdots W_rf$ gehört:

$$
\begin{gathered}
\left|
\begin{array}{cccccc}
\xi_{11}&\cdot&\xi_{1s}&
\displaystyle\sum_1^s{}^{\nu}\frac{\partial\xi_{11}}{\partial x_\nu}\xi_\nu&
\cdot&\displaystyle\sum_1^s{}^{\nu}\frac{\partial\xi_{1s}}{\partial x_\nu}\xi_\nu\\
\cdot&\cdot&\cdot&\cdot&\cdot&\cdot\\
\xi_{r1}&\cdot&\xi_{rs}&
\displaystyle\sum_1^s{}^{\nu}\frac{\partial\xi_{r1}}{\partial x_\nu}\xi_\nu&
\cdot&\displaystyle\sum_1^s{}^{\nu}\frac{\partial\xi_{rs}}{\partial x_\nu}\xi_\nu
\end{array}
\right|.\\
\text{(5)}
\end{gathered}
$$

Wir werden zeigen, dass (4) zu den Gleichungensystemen gehört, welche man durch Nullsetzen aller $(n+1)$-reihigen Determinanten dieser Matrix erhält. Damit ist dann nach Kap. 14, S. 228 bewiesen, dass (4) die Gruppe $W_1f\cdots W_rf$ gestattet.

Unter den $(n+1)$-reihigen Determinanten der Matrix (5) giebt es solche von der Form:

$$
D=\left|
\begin{array}{cccc}
\xi_{1\kappa_1}&\cdot&\xi_{1\kappa_n}&
\displaystyle\sum_1^s{}^{\nu}\frac{\partial\xi_{1\sigma}}{\partial x_\nu}\xi_\nu\\
\cdot&\cdot&\cdot&\cdot\\
\xi_{n\kappa_1}&\cdot&\xi_{n\kappa_n}&
\displaystyle\sum_1^s{}^{\nu}\frac{\partial\xi_{n\sigma}}{\partial x_\nu}\xi_\nu\\
\xi_{n+j,\kappa_1}&\cdot&\xi_{n+j,\kappa_n}&
\displaystyle\sum_1^s{}^{\nu}\frac{\partial\xi_{n+j,\sigma}}{\partial x_\nu}\xi_\nu
\end{array}\right|.
$$

Benutzen wir die aus (3) folgenden Identitäten:

$$
\begin{gathered}
\xi_{n+j,\pi}=\sum_1^n{}^{\nu}\varphi_{j\nu}(x)\cdot\xi_{\nu\pi}
\\
(\pi=1\cdots s;\ j=1\cdots r-n),
\end{gathered}
$$

so können wir $D$ offenbar schreiben:

$$
\begin{gathered}
D=\sum_1^n\pm\xi_{1\kappa_1}\cdots\xi_{n\kappa_n}\cdot\\
\sum_1^s{}^{\nu}
\bigl\{\frac{\partial\xi_{n+j,\sigma}}{\partial x_\nu}\\
-\sum_1^n{}^{\tau}\varphi_{j\tau}\frac{\partial\xi_{\tau\sigma}}{\partial x_\nu}\bigr\}
\xi_\nu.
\end{gathered}
$$

Nun verschwinden unter den gemachten Voraussetzungen nicht alle Determinanten von der Form:

$$
\sum\pm\xi_{1\kappa_1}\cdots\xi_{n\kappa_n}
$$

identisch; setzen wir daher alle Determinanten von der Form $D$ gleich Null, so erhalten wir entweder Relationen zwischen $x_1\cdots x_s$ allein, oder wir erhalten das Gleichungensystem (4). Dieses Gleichungensystem bringt aber, wie leicht zu sehen, überhaupt alle $(n+1)$-reihigen Determinanten der Matrix (5) zum Verschwinden, also gestattet es die Gruppe $W_1f\cdots W_rf$.

Die Bestimmung des allgemeinsten Gleichungensystems (2), welches die Gruppe $W_1f\cdots W_rf$ gestattet und die Gleichungen (4) umfasst, lässt sich nun auf Grund von Kap. 14, S. 236 bis 238 durchführen.

Das Gleichungensystem (4) bringt alle $(n+1)$-reihigen, nicht aber alle $n$-reihigen Determinanten der Matrix (5) zum Verschwinden; ebenso wenig kann ein Gleichungensystem von der Form (2) alle $n$-reihigen Determinanten der Matrix (5) gleich Null machen. Also verfahren wir folgendermassen: Wir lösen die Gleichungen (4) nach $m$ von den Grössen $\xi_1\cdots\xi_s$ auf, etwa nach $\xi_1\cdots\xi_m$, sodann bilden wir in den $2s-m$ Veränderlichen $x_1\cdots x_s$, $\xi_{m+1}\cdots\xi_s$ nach Anleitung der citirten Entwickelungen die verkürzten infinitesimalen Transformationen $\overline W_1f\cdots\overline W_rf$, endlich bestimmen wir irgend $2s-m-n$ unabhängige Lösungen des $n$-gliedrigen vollständigen Systems, welches von den $n$ Gleichungen: $\overline W_1f=0$, $\cdots$, $\overline W_nf=0$ gebildet wird.

Die $n$ Gleichungen: $\overline W_1f=0$, $\cdots$, $\overline W_nf=0$ sind nach $n$ von den Differentialquotienten $\frac{\partial f}{\partial x_1}\cdots\frac{\partial f}{\partial x_s}$ auflösbar, also sind ihre $2s-m-n$ unabhängigen Lösungen in Bezug auf $s-n$ von den $x$ und die Veränderlichen $\xi_{m+1}\cdots\xi_s$ von einander unabhängig (vgl. Kap. 5, Theor. 12, S. 91). Nun giebt es unter den Lösungen des vollständigen Systems $W_kf=0$ gerade $s-n$ unabhängige, welche zugleich das $n$-gliedrige vollständige System: $X_1f=0$, $\cdots$, $X_nf=0$ befriedigen und also nur von den $x$ abhängen, sie mögen:

$$
u_1(x_1\cdots x_s)\cdots u_{s-n}(x_1\cdots x_s)
$$

heissen. Sind daher

$$
\begin{gathered}
\mathfrak B_1(\xi_{m+1}\cdots\xi_s,x_1\cdots x_s),\\
\cdots,\\

\mathfrak B_{s-m}(\xi_{m+1}\cdots\xi_s,x_1\cdots x_s)
\end{gathered}
$$

irgend $s-m$ von einander und von den $u$ unabhängige Lösungen des vollständigen Systems $\overline W_kf=0$, so sind dieselben nothwendig in Bezug auf $\xi_{m+1}\cdots\xi_s$ von einander unabhängig.

Das allgemeinste Gleichungensystem (2), welches die Gruppe $W_1f\cdots W_rf$ gestattet, erhalten wir jetzt, wenn wir zu den Gleichungen (4) in allgemeinster Weise $s-m$ von einander unabhängige, nach $\xi_{m+1}\cdots\xi_s$ auflösbare Relationen zwischen $u_1\cdots u_{s-n}$, $\mathfrak B_1\cdots\mathfrak B_{s-m}$ hinzufügen. Es ist klar, dass diese Relationen nach $\mathfrak B_1\cdots\mathfrak B_{s-m}$ auflösbar sein müssen, dass sie also auf die Form:

$$
\begin{gathered}
\mathfrak B_\mu(\xi_{m+1}\cdots\xi_s,x_1\cdots x_s)\\
=\Omega_\mu\bigl(u_1(x)\cdots u_{s-n}(x)\bigr)
\\
(\mu=1\cdots s-m)
\end{gathered}\tag{6}
$$

gebracht werden können. Hier sind die $\Omega_\mu$ keinerlei Beschränkung unterworfen, sondern vollkommen willkürliche Functionen ihrer Argumente.

Fügen wir demnach die Gleichungen (6) zu (4) hinzu und lösen wir, was immer möglich ist, alles nach $\xi_1\cdots\xi_s$ auf, so erhalten wir das allgemeinste Gleichungensystem (2), welches die Gruppe $W_1f\cdots W_rf$ gestattet und damit auch das allgemeinste Lösungensystem der Differentialgleichungen (1). Dieses allgemeinste Lösungensystem enthält augenscheinlich $s-m$ willkürliche Functionen von $u_1\cdots u_{s-n}$.

Nun aber sind die Differentialgleichungen (1) linear und homogen in den Unbekannten $\xi_1\cdots\xi_s$; also lässt sich schliessen, dass ihr allgemeinstes Lösungensystem $\xi_1\cdots\xi_s$ aus $s-m$ particulären Lösungensystemen:

$$
\xi_{\mu1}(x)\cdots\xi_{\mu s}(x)\qquad(\mu=1\cdots s-m)
$$

in der folgenden Weise abgeleitet werden kann:

$$
\begin{gathered}
\xi_i=\chi_1(u_1\cdots u_{s-n})\cdot\xi_{1i}\\
+\cdots+\chi_{s-m}(u_1\cdots u_{s-n})\cdot\xi_{s-m,i}
\\
(i=1\cdots s),
\end{gathered}
$$

wobei die $\chi$ vollständig willkürliche Functionen der $u$ sind; natürlich müssen die betreffenden particulären Lösungensysteme so beschaffen sein, dass es keine $s-m$ Functionen $\psi_1(u_1\cdots u_{s-n})\cdots\psi_{s-m}(u_1\cdots u_{s-n})$ giebt, welche die $s$ Gleichungen:

$$
\begin{gathered}
\psi_1(u)\cdot\xi_{1i}+\cdots+\psi_{s-m}(u)\cdot\xi_{s-m,i}=0
\\
(i=1\cdots s)
\end{gathered}
$$

identisch befriedigen.

Es lässt sich sogar zeigen, dass es überhaupt keine $s-m$ Functionen $\Psi_1(x_1\cdots x_s)\cdots\Psi_{s-m}(x_1\cdots x_s)$ giebt, welche die $s-m$ Gleichungen:

$$
\begin{gathered}
\Psi_1(x)\cdot\xi_{1i}+\cdots+
\Psi_{s-m}(x)\cdot\xi_{s-m,i}=0
\\
(i=1\cdots s)
\end{gathered}
$$

identisch befriedigen. Nämlich die $s-m$ Gleichungen:

$$
\begin{gathered}
\xi_{m+\sigma}=\sum_1^{s-m}{}^{\mu}\chi_\mu(u)\cdot\xi_{\mu,m+\sigma}
\\
(\sigma=1\cdots s-m)
\end{gathered}
$$

sind offenbar mit den Gleichungen (6) äquivalent, also müssen sie nach $\chi_1\cdots\chi_{s-m}$ auflösbar sein und die Determinante:

$$
\sum\pm\xi_{1,m+1}\cdots\xi_{s-m,m+s-m}
$$

darf nicht identisch verschwinden.

Nach diesen Vorbereitungen können wir endlich die Form angeben, welche die allgemeinste mit $X_1f\cdots X_rf$ vertauschbare infinitesimale Transformation $Zf$ besitzt. Die betreffende Transformation lautet:

$$
Zf=\sum_1^{s-m}{}^{\mu}\chi_\mu(u_1\cdots u_{s-m})\cdot Z_\mu f,
$$

wo die $s-m$ infinitesimalen Transformationen:

$$
\begin{gathered}
Z_\mu f=\sum_1^s{}^{i}\xi_{\mu i}(x_1\cdots x_s)\frac{\partial f}{\partial x_i}
\\
(\mu=1\cdots s-m)
\end{gathered}
$$

durch keine lineare Relation von der Form:

$$
\begin{gathered}
\Psi_1(x_1\cdots x_s)\cdot Z_1f\\
+\cdots+
\Psi_{s-m}(x_1\cdots x_s)\cdot Z_{s-m}f=0
\end{gathered}
$$

verknüpft sind.

Da überdies nach Satz 1, S. 369 auch jede infinitesimale Transformation $(Z_\mu Z_\nu)$ mit $X_1f\cdots X_rf$ vertauschbar ist, so bestehen Relationen von der besonderen Form:

$$
\begin{gathered}
(Z_\mu Z_\nu)=\sum_1^{s-m}{}^{\pi}
\omega_{\mu\nu\pi}(u_1\cdots u_{s-m})\cdot Z_\pi f
\\
(\mu,\nu=1\cdots s-m).
\end{gathered}
$$

Wir sehen also: Es giebt stets dann, aber auch nur dann eine infinitesimale Transformation, welche mit $X_1f\cdots X_rf$ vertauschbar ist, wenn die auf S. 372 definirte Zahl $m$ kleiner ist als die Zahl $s$ der Veränderlichen $x$. Ist $m<s$ und zugleich $n<s$, ist also die Gruppe $X_1f\cdots X_rf$ intransitiv, so hängt die allgemeinste mit $X_1f\cdots X_rf$ vertauschbare infinitesimale Transformation $Zf$ von willkürlichen Functionen ab. Ist dagegen $n=s$, ist also die Gruppe $X_1f\cdots X_rf$ transitiv, so lässt sich die allgemeinste mit $X_1f\cdots X_rf$ vertauschbare infinitesimale Transformation $Zf$ aus $s-m$ unabhängigen infinitesimalen Transformationen: $Z_1f\cdots Z_{s-m}f$ linear ableiten; nach einer früheren Bemerkung (S. 369) erzeugen dann die betreffenden infinitesimalen Transformationen eine $(s-m)$-gliedrige Gruppe. —

Wir wissen, dass eine mit $X_1f\cdots X_rf$ vertauschbare infinitesimale Transformation nur dann existirt, wenn die Gleichungen (4) sich auf weniger als $s$ unabhängige reduciren. Dieser Bedingung können wir eine etwas übersichtlichere Fassung geben, wenn wir uns der Identitäten (3) oder der äquivalenten:

$$
\begin{gathered}
\xi_{n+k,i}-\sum_1^n{}^{\rho}\varphi_{k\rho}(x)\cdot\xi_{\rho i}=0
\\
(k=1\cdots r-n;\ i=1\cdots s)
\end{gathered}
$$

erinnern, welche die Functionen $\varphi_{k\rho}$ definiren. Differentiiren wir nämlich die eben geschriebenen Identitäten nach $x_j$, so erhalten wir die folgenden Identitäten:

$$
\begin{gathered}
\frac{\partial\xi_{n+k,i}}{\partial x_j}\\
-\sum_1^n{}^{\rho}
\bigl\{\varphi_{k\rho}\frac{\partial\xi_{\rho i}}{\partial x_j}\\
+\xi_{\rho i}\frac{\partial\varphi_{k\rho}}{\partial x_j}\bigr\}=0
\\
(k=1\cdots r-n;\ i,j=1\cdots s),
\end{gathered}
$$

vermöge deren sich die Gleichungen (4) durch die äquivalenten Gleichungen:

$$
\begin{gathered}
\sum_1^n{}^{\rho}\xi_{\rho i}\sum_1^s{}^{j}
\xi_j\frac{\partial\varphi_{k\rho}}{\partial x_j}=0
\\
(i=1\cdots s;\ k=1\cdots r-n)
\end{gathered}
$$

ersetzen lassen. Da aber nicht alle Determinanten von der Form $\sum\pm\xi_{\kappa_1}\cdots\xi_{\kappa_n}$ identisch verschwinden, so sind die letzten Gleichungen ihrerseits äquivalent mit:

$$
\begin{gathered}
\sum_1^s{}^{j}\xi_j\frac{\partial\varphi_{k\rho}}{\partial x_j}=0
\\
(k=1\cdots r-n;\ \rho=1\cdots n).
\end{gathered}\tag{4'}
$$

Es giebt demnach eine mit $X_1f\cdots X_rf$ vertauschbare infinitesimale Transformation $Zf$ nur dann, wenn die in den $\xi_i$ linearen Gleichungen (4') sich auf weniger als $s$ unabhängige reduciren.

Die Gleichungen (4') sind übersichtlicher als die Gleichungen (4), sie haben überdies einen einfachen Sinn, sie sagen nämlich aus, dass jede der $n(r-n)$ Functionen $\varphi_{k\rho}(x_1\cdots x_s)$ die sämmtlichen infinitesimalen Transformationen $Zf$ gestattet.

Giebt es unter den Gleichungen (4) gerade $m$ von einander unabhängige, so giebt es natürlich auch unter den Gleichungen (4') gerade $m$ von einander unabhängige, also ist $m$ offenbar nichts anderes als die Zahl der unabhängigen unter den $n(r-n)$ Functionen $\varphi_{k\rho}(x)$.

Fassen wir die gewonnenen Ergebnisse zusammen:

**Theorem 67.** *Sind von den $r$ unabhängigen infinitesimalen Transformationen:*

$$
X_kf=\sum_1^s{}^{i}\xi_{ki}(x_1\cdots x_s)\frac{\partial f}{\partial x_i}
\qquad(k=1\cdots r)
$$

*einer $r$-gliedrigen Gruppe etwa $X_1f\cdots X_nf$ durch keine lineare Relation verknüpft, während $X_{n+1}f\cdots X_rf$ sich linear durch $X_1f\cdots X_nf$ ausdrücken lassen:*

$$
\begin{gathered}
X_{n+j}f=\sum_1^n{}^{\rho}\varphi_{j\rho}(x_1\cdots x_s)\cdot X_\rho f
\\
(j=1\cdots r-n),
\end{gathered}
$$

*und sind unter den $n(r-n)$ Functionen $\varphi_{k\rho}$ gerade $s$ von einander unabhängige vorhanden, so giebt es keine infinitesimale Transformation, welche mit allen $X_kf$ vertauschbar ist; sind dagegen unter den Functionen $\varphi_{k\rho}$ weniger als $s$, etwa blos $m$ unabhängige vorhanden, so giebt es infinitesimale Transformationen, welche mit $X_1f\cdots X_rf$ vertauschbar sind, und zwar besitzt die allgemeinste infinitesimale Transformation $Zf$ von dieser Beschaffenheit die Form:*

$$
\begin{gathered}
Zf=\psi_1(u_1\cdots u_{s-n})\cdot Z_1f\\
+\cdots+
\psi_{s-m}(u_1\cdots u_{s-n})\cdot Z_{s-m}f,
\end{gathered}
$$

*wo $u_1\cdots u_{s-n}$ unabhängige Lösungen des $n$-gliedrigen vollständigen Systems: $X_1f=0$, $\cdots$, $X_nf=0$ bezeichnen, wo ferner $\psi_1\cdots\psi_{s-m}$ willkürliche Functionen ihrer Argumente bedeuten und wo endlich die mit $X_1f\cdots X_rf$ vertauschbaren, durch keine lineare Relation verknüpften infinitesimalen Transformationen:*

$$
\begin{gathered}
Z_\mu f=\sum_1^s{}^{i}\xi_{\mu i}(x_1\cdots x_s)\frac{\partial f}{\partial x_i}
\\
(\mu=1\cdots s-m)
\end{gathered}
$$

*paarweise in Beziehungen von der Form:*

$$
(Z_\mu Z_\nu)=\sum_1^{s-m}{}^{\pi}
\omega_{\mu\nu\pi}(u_1\cdots u_{s-m})\cdot Z_\pi f
$$

*stehen.*\*)

Ein Theil der in diesem Satze ausgesprochenen Ergebnisse folgt übrigens unmittelbar aus den Entwickelungen des vorigen Kapitels. Ist nämlich die Anzahl der unabhängigen unter den Functionen $\varphi_{k\rho}(x_1\cdots x_s)$ gerade gleich $s$, so stellen nach S. 344 die Gleichungen:

$$
\begin{gathered}
\varphi_{k\rho}(x_1'\cdots x_s')=\varphi_{k\rho}(x_1\cdots x_s)
\\
(k=1\cdots r-n;\ \rho=1\cdots n)
\end{gathered}
$$

die allgemeinste Transformation dar, welche $X_1f\cdots X_rf$ bezüglich in: $X_1'f\cdots X_r'f$ überführt. Giebt es dagegen unter den $\varphi_{k\rho}$ weniger als $s$ von einander unabhängige Functionen, so giebt es nach Theor. 65, S. 353 eine continuirliche Menge von Transformationen, welche jedes $X_kf$ invariant lassen; wir bemerkten schon auf S. 368, dass der Inbegriff aller derartigen Transformationen eine Gruppe bildet, von welcher sich direkt einsehen lässt, dass sie eingliedrige Gruppen umfasst.

Es scheint angemessen, noch den folgenden Satz ausdrücklich auszusprechen:

**Satz 2.** *Giebt es überhaupt eine infinitesimale Transformation, welche mit allen infinitesimalen Transformationen $X_1f\cdots X_rf$ einer $r$-gliedrigen Gruppe des Raumes $x_1\cdots x_s$ vertauschbar ist, so enthält die allgemeinste mit $X_1f\cdots X_rf$ vertauschbare infinitesimale Transformation willkürliche Functionen, sobald die Gruppe $X_1f\cdots X_rf$ intransitiv ist, dagegen nur willkürliche Parameter, sobald die Gruppe transitiv ist.*

**§96.**

Von hervorragender Bedeutung ist der Fall, dass die Gruppe $X_kf$ einfach transitiv ist, also der Fall $s=r=n$.

Wünscht man in diesem Falle die allgemeinste Transformation $x_i'=\Phi_i(x_1\cdots x_n)$ zu kennen, vermöge deren jedes $X_kf$ die Form $X_k'f$ annimmt, so hat man nur $n$ unabhängige Lösungen $\Omega_1\cdots\Omega_n$ des $n$-gliedrigen vollständigen Systems:

$$
X_kf+X_k'f=0\qquad(k=1\cdots n)
$$

aufzusuchen und dieselben gleich willkürlichen Constanten $a_1\cdots a_n$ zu setzen. Die Gleichungen:

$$
\Omega_k(x_1\cdots x_n,x_1'\cdots x_n')=a_k
\qquad(k=1\cdots n)
$$

sind dann sowohl nach $x$ als nach $x'$ auflösbar und stellen die verlangte Transformation dar.

Wir wissen von vornherein, dass der Inbegriff aller Transformationen $\Omega_k=a_k$ eine Gruppe bildet. Wir sehen jetzt, dass diese Gruppe $n$-gliedrig und einfach transitiv ist; das geht sofort aus der Form hervor, in welcher die Gruppe vorliegt, aufgelöst nach ihren $n$ Parametern.

Die Gruppe:

$$
\Omega_1(x,x')=a_1,\quad\cdots,\quad\Omega_n(x,x')=a_n
$$

enthält die identische Transformation und $n$ unabhängige infinitesimale Transformationen:

$$
Z_kf=\sum_1^n{}^{i}\xi_{ki}(x_1\cdots x_n)\frac{\partial f}{\partial x_i}
\qquad(k=1\cdots n),
$$

das geht aus den Entwickelungen des vorigen Paragraphen hervor; es ist aber auch an sich klar, da sich die Transformationen der Gruppe paarweise als inverse zusammen ordnen und also das Theorem 56 im Kap. 18, S. 315 Anwendung findet. Aus der Transitivität der Gruppe $Z_1f\cdots Z_nf$ folgt überdies, dass $Z_1f\cdots Z_nf$ durch keine lineare Relation von der Form $\sum\chi_i(x_1\cdots x_s)Z_if=0$ verknüpft sind.

Zwischen den beiden *einfach transitiven* Gruppen $X_kf$ und $Z_if$ besteht ein völliges Reciprocitätsverhältniss. Sind die $X_kf$ gegeben, so ist die allgemeine infinitesimale Transformation $Zf=\sum e_iZ_if$ durch die $n$ Gleichungen:

$$
X_k(Z(f))-Z(X_k(f))=0\qquad(k=1\cdots n)
$$

vollständig definirt; sind andererseits die $Z_if$ gegeben, so bestimmen die $n$ Gleichungen:

$$
X(Z_i(f))-Z_i(X(f))=0\qquad(i=1\cdots n)
$$

in gleicher Weise die allgemeine infinitesimale Transformation

$$
Xf=\sum e_kX_kf.
$$

Damit ist aber die eigenartige Beziehung, in welcher die beiden Gruppen stehen, noch nicht in erschöpfender Weise beschrieben. Die beiden Gruppen sind nämlich, wie wir jetzt zeigen werden, auch noch gleichzusammengesetzt; da beide einfach transitiv sind, folgt daraus sofort, dass sie auch mit einander ähnlich sind (vgl. Kap. 19, Theorem 64, S. 340).

Wir denken uns in den infinitesimalen Transformationen $X_kf$ und $Z_if$ die $\xi_{k\nu}$ und $\xi_{i\nu}$ nach Potenzen von $x_1\cdots x_n$ entwickelt, indem wir voraussetzen, dass $x_1=0$, $\cdots$, $x_n=0$ ein Punkt von allgemeinster Lage ist. Nach Kap. 13, S. 217 enthält die Gruppe $X_kf$, weil sie einfach transitiv ist, gerade $n$ infinitesimale Transformationen von nullter Ordnung in $x_1\cdots x_n$, aus denen sich keine infinitesimale Transformation von erster oder höherer Ordnung linear ableiten lässt.

Wir können daher $X_1f\cdots X_nf$ durch $n$ andere unabhängige infinitesimale Transformationen $\mathfrak X_1f\cdots\mathfrak X_nf$ ersetzt denken, welche bei Weglassung der Glieder zweiter und höherer Ordnung die Form:

$$
\begin{gathered}
\mathfrak X_kf=\frac{\partial f}{\partial x_k}\\
+\sum_{\mu\nu}^{1\cdots n} h_{k\mu\nu}x_\mu\frac{\partial f}{\partial x_\nu}\\
+\cdots\\
(k=1\cdots n)
\end{gathered}
$$

haben. In derselben Weise können wir $Z_1f\cdots Z_nf$ durch $n$ unabhängige infinitesimale Transformationen von der Form:

$$
\begin{gathered}
\mathfrak Z_if=-\frac{\partial f}{\partial x_i}\\
+\sum_{\mu\nu}^{1\cdots n} l_{i\mu\nu}x_\mu\frac{\partial f}{\partial x_\nu}\\
+\cdots\\
(i=1\cdots n)
\end{gathered}
$$

ersetzen.

Nach diesen Vorbereitungen bilden wir die Gleichung $(\mathfrak X_k\mathfrak Z_i)=0$; dieselbe nimmt die Form an:

$$
\sum_1^n{}^{\nu}(l_{ik\nu}+h_{ki\nu})\frac{\partial f}{\partial x_\nu}
+\cdots=0,
$$

woraus folgt:

$$
l_{ik\nu}=-h_{ki\nu}.
$$

Rechnungen derselben Art ergeben:

$$
(\mathfrak X_k\mathfrak X_j)
=\sum_1^n{}^{\nu}(h_{jk\nu}-h_{kj\nu})\frac{\partial f}{\partial x_\nu}
+\cdots
$$

$$
\begin{gathered}
(\mathfrak Z_k\mathfrak Z_j)\\
=\sum_1^n{}^{\nu}(-l_{jk\nu}+l_{kj\nu})\frac{\partial f}{\partial x_\nu}\\
+\cdots\\
=\sum_1^n{}^{\nu}(h_{kj\nu}-h_{jk\nu})\frac{\partial f}{\partial x_\nu}\\
+\cdots.
\end{gathered}
$$

Andererseits ist:

$$
\begin{gathered}
(\mathfrak X_k\mathfrak X_j)=\sum_1^n{}^{\nu} c_{kj\nu}\mathfrak X_\nu f,
\\

(\mathfrak Z_k\mathfrak Z_j)=\sum_1^n{}^{\nu} c'_{kj\nu}\mathfrak Z_\nu f;
\end{gathered}
$$

hier setzen wir die eben gefundenen Ausdrücke für: $\mathfrak X_\nu f$, $\mathfrak Z_\nu f$, $(\mathfrak X_k\mathfrak X_j)$, $(\mathfrak Z_k\mathfrak Z_j)$ ein und machen dann die Substitution: $x_1=0$, $\cdots$, $x_n=0$; da kommt:

$$
c_{kj\nu}=h_{jk\nu}-h_{kj\nu}=c'_{kj\nu}.
$$

Also sind unsere beiden Gruppen wirklich gleichzusammengesetzt und in Folge dessen, wie schon oben bemerkt, mit einander ähnlich. Somit gilt das

**Theorem 68.** *Sind $X_1f\cdots X_nf$ unabhängige infinitesimale Transformationen einer einfach transitiven Gruppe in den Veränderlichen $x_1\cdots x_n$, so definiren die $n$ Gleichungen $(X_kZ)=0$ die allgemeine infinitesimale Transformation $Zf$ einer zweiten einfach transitiven Gruppe $Z_1f\cdots Z_nf$, welche mit der Gruppe $X_1f\cdots X_nf$ gleichzusammengesetzt und derselben zugleich ähnlich ist. Die Beziehung zwischen diesen beiden einfach transitiven Gruppen ist eine gegenseitige: jede der beiden Gruppen besteht aus dem Inbegriff aller eingliedrigen Gruppen, deren Transformationen mit jeder Transformation der andern Gruppe vertauschbar sind.*\*)

Es ist bequem, die Gruppen $X_kf$ und $Z_if$ als *reciproke* Transformationsgruppen zu bezeichnen, oder immer die eine als die reciproke Gruppe der andern.

Erinnern wir uns aus Kap. 16, S. 276, dass die ausgezeichneten infinitesimalen Transformationen $e_1X_1f+\cdots+e_nX_nf=Yf$ der Gruppe $X_1f\cdots X_nf$ durch die Gleichungen $(X_kY)=0$ definirt sind, so können wir noch den folgenden Satz aussprechen:

**Satz 3.** *Die gemeinsamen infinitesimalen Transformationen zweier reciproker einfach transitiver Gruppen sind zugleich die ausgezeichneten infinitesimalen Transformationen beider Gruppen.*

Die beiden $n$-gliedrigen Gruppen $X_1f\cdots X_nf$ und $Z_1f\cdots Z_nf$ in den $n$ Veränderlichen $x_1\cdots x_n$ seien einfach transitiv und zu einander reciprok. Gehen dann bei Einführung neuer Veränderlicher $x_1'\cdots x_n'$ die $X_kf$ über in $X_k'f$, die $Z_kf$ über in $Z_k'f$, so sind auch die beiden einfach transitiven Gruppen $X_1'f\cdots X_n'f$ und $Z_1'f\cdots Z_n'f$ zu einander reciprok; das folgt unmittelbar aus der Relation: $(X_k'Z_j')=(X_kZ_j)\equiv0$.

Hieraus ergiebt sich insbesondere der

**Satz 4.** *Bleibt eine $n$-gliedrige einfach transitive Gruppe in $n$ Veränderlichen bei einer Transformation invariant, so bleibt gleichzeitig ihre reciproke einfach transitive Gruppe invariant.*

Aus diesem Satz folgt endlich der nachstehende:

**Satz 5.** *Die grösste Gruppe des Raumes $x_1\cdots x_n$, in welcher eine $n$-gliedrige einfach transitive Gruppe dieses Raumes als invariante Untergruppe enthalten ist, fällt zusammen mit der grössten Gruppe, in welcher die reciproke Gruppe dieser einfach transitiven Gruppe als invariante Untergruppe enthalten ist.*

Wir wollen zu den vorstehenden allgemeinen Entwickelungen über einfach transitive Gruppen ein paar einfache Beispiele geben.

Die Gruppe

$$
\frac{\partial f}{\partial x},\quad
x\frac{\partial f}{\partial x}+y\frac{\partial f}{\partial y}
$$

der Ebene $x$, $y$ ist einfach transitiv. Die endlichen Gleichungen der reciproken Gruppe ergeben sich durch Integration des vollständigen Systems

$$
\begin{gathered}
\frac{\partial f}{\partial x}+\frac{\partial f}{\partial x'}=0,\\

x\frac{\partial f}{\partial x}+y\frac{\partial f}{\partial y}\\
+x'\frac{\partial f}{\partial x'}+y'\frac{\partial f}{\partial y'}=0
\end{gathered}
$$

in folgender Form:

$$
\frac{x'-x}{y}=a,\qquad\frac{y'}y=b,
$$

also nach $x'$ und $y'$ aufgelöst:

$$
x'=x+ay,\qquad y'=by.
$$

Die infinitesimalen Transformationen der reciproken Gruppe werden demnach:

$$
y\frac{\partial f}{\partial x},\qquad y\frac{\partial f}{\partial y}.
$$

Ein interessantes Beispiel bietet die sechsgliedrige projective Gruppe einer nicht ausgearteten Fläche zweiter Ordnung im gewöhnlichen Raume. Diese Gruppe enthält nämlich zwei dreigliedrige einfach transitive zu einander reciproke Gruppen, von denen die eine alle Erzeugenden der einen Schaar stehen lässt, die andere alle Erzeugenden der andern Schaar.

Ist $z-xy=0$ die Gleichung der Fläche, so ist

$$
X_1f=\frac{\partial f}{\partial x}+y\frac{\partial f}{\partial z},
\qquad
X_2f=x\frac{\partial f}{\partial x}+z\frac{\partial f}{\partial z},
$$

$$
X_3f=x^2\frac{\partial f}{\partial x}+(xy-z)\frac{\partial f}{\partial y}
+xz\frac{\partial f}{\partial z}
$$

die eine der beiden einfach transitiven Gruppen und

$$
Z_1f=\frac{\partial f}{\partial y}+x\frac{\partial f}{\partial z},
\qquad
Z_2f=y\frac{\partial f}{\partial y}+z\frac{\partial f}{\partial z},
$$

$$
Z_3f=(xy-z)\frac{\partial f}{\partial x}+y^2\frac{\partial f}{\partial y}
+yz\frac{\partial f}{\partial z}
$$

die andere.

Die beiden reciproken Gruppen sind natürlich mit einander ähnlich; zu bemerken ist aber, dass sie durch eine *projective* Transformation mit einander ähnlich sind, nämlich durch jede projective Transformation, welche die beiden Schaaren von Erzeugenden der Fläche mit einander vertauscht.

**§97.**

Wir fahren fort in den allgemeinen Untersuchungen über reciproke einfach transitive Gruppen.

Es seien $X_1f\cdots X_nf$ und $Z_1f\cdots Z_nf$ zwei einfach transitive und zu einander reciproke Gruppen in den Veränderlichen $x_1\cdots x_n$.

Wäre $n$ gleich 1, so wären beide Gruppen mit einander identisch, wie man sich leicht überzeugt; wir wollen daher voraussetzen, dass $n$ grösser als 1 ist. Dann enthält die Gruppe $Z_1f\cdots Z_nf$ sicher Untergruppen. Ist $Z_1f\cdots Z_mf$ $(m<n)$ eine solche, so bilden die Gleichungen:

$$
Z_1f=0,\quad\cdots,\quad Z_mf=0
$$

ein $m$-gliedriges vollständiges System, welches, wie aus den Identitäten:

$$
\begin{gathered}
(X_iZ_1)\equiv0,\\
\cdots,\\
(X_iZ_m)\equiv0
\\
(i=1\cdots n)
\end{gathered}
$$

hervorgeht, die Gruppe $X_1f\cdots X_nf$ gestattet (vgl. Kap. 8, Theorem 20, S. 140). Folglich ist die Gruppe $X_1f\cdots X_nf$ *imprimitiv*.

Sind $u_1\cdots u_{n-m}$ unabhängige Lösungen des vollständigen Systems $Z_1f=0$, $\cdots$, $Z_mf=0$, so bestehen nach Kap. 8, Satz 1, S. 139 Relationen von der Form:

$$
\begin{gathered}
X_iu_\nu=\omega_{i\nu}(u_1\cdots u_{n-m})
\\
(i=1\cdots n;\ \nu=1\cdots n-m)
\end{gathered}
$$

und es werden daher (vgl. S. 143) die $\infty^{n-m}$ $m$-fach ausgedehnten Mannigfaltigkeiten:

$$
u_1=\mathrm{const.},\quad\cdots,\quad u_{n-m}=\mathrm{const.}
$$

von der Gruppe $X_1f\cdots X_nf$ unter einander vertauscht.

Wir haben also den

**Satz 6.** *Jede einfach transitive Gruppe: $X_1f\cdots X_nf$ in $n>1$ Veränderlichen: $x_1\cdots x_n$ ist imprimitiv; ist $Z_1f\cdots Z_nf$ die zugehörige reciproke Gruppe und $Z_1f\cdots Z_mf$ eine beliebige Untergruppe derselben mit den Invarianten $u_1\cdots u_{n-m}$, so gestattet das $m$-gliedrige vollständige System $Z_1f=0$, $\cdots$, $Z_mf=0$ die Gruppe $X_1f\cdots X_nf$ und die $\infty^{n-m}$ $m$-fach ausgedehnten Mannigfaltigkeiten: $u_1=\mathrm{const.}$, $\cdots$, $u_{n-m}=\mathrm{const.}$ werden von dieser Gruppe unter einander vertauscht.*

Der vorstehende Satz zeigt, dass jede $m$-gliedrige Untergruppe der Gruppe $Z_1f\cdots Z_nf$ eine ganz bestimmte bei der Gruppe $X_1f\cdots X_nf$ invariante Zerlegung des Raumes $x_1\cdots x_n$ in $\infty^{n-m}$ $m$-fach ausgedehnte Mannigfaltigkeiten liefert. Denken wir uns daher alle Untergruppen der Gruppe $Z_1f\cdots Z_nf$ bestimmt und zu jeder die zugehörigen Invarianten berechnet, so erhalten wir unendlich viele bei der Gruppe $X_1f\cdots X_nf$ invariante Zerlegungen des Raumes. Es lässt sich nachweisen, dass auf diese Weise alle vorhandenen invarianten Zerlegungen gefunden werden, dass also der Satz 6 sich umkehren lässt.

Es sei: $Y_1f=0$, $\cdots$, $Y_mf=0$ irgend ein $m$-gliedriges vollständiges System, welches die Gruppe $X_1f\cdots X_nf$ gestattet, $u_1\cdots u_{n-m}$ seien unabhängige Lösungen dieses vollständigen Systems, so dass also die Schaar der $\infty^{n-m}$ $m$-fach ausgedehnten Mannigfaltigkeiten:

$$
u_1=\mathrm{const.},\quad\cdots,\quad u_{n-m}=\mathrm{const.}
$$

eine bei der Gruppe $X_1f\cdots X_nf$ invariante Zerlegung des Raumes $x_1\cdots x_n$ darstellt. Wir behaupten, dass die Gruppe $Z_1f\cdots Z_nf$ eine ganz bestimmte $m$-gliedrige Untergruppe enthält, welche jede einzelne dieser $\infty^{n-m}$ Mannigfaltigkeiten stehen lässt; das ist eben die Umkehrung des Satzes 6.

Wir führen zunächst in unseren reciproken Gruppen die Functionen $u_1\cdots u_{n-m}$ und irgend $m$ von denselben und von einander unabhängige Functionen: $v_1\cdots v_m$ der $x$ als Veränderliche ein, dann wird:

$$
\begin{gathered}
X_kf=\sum_1^{n-m}{}^{\nu}\omega_{k\nu}(u_1\cdots u_{n-m})
\frac{\partial f}{\partial u_\nu}\\
+\sum_1^m{}^{\mu} X_kv_\mu\frac{\partial f}{\partial v_\mu}
\\
(k=1\cdots n)
\end{gathered}
$$

und:

$$
\begin{gathered}
Z_kf=\sum_1^{n-m}{}^{\nu}Z_ku_\nu\frac{\partial f}{\partial u_\nu}\\
+\sum_1^m{}^{\mu} Z_kv_\mu\frac{\partial f}{\partial v_\mu}
\\
(k=1\cdots n),
\end{gathered}
$$

wo die $X_kv_\mu$, $Z_ku_\nu$ und $Z_kv_\mu$ gewisse Functionen der $u$ und $v$ sind. Unsere Behauptung kommt nun offenbar darauf hinaus, dass sich aus $Z_1f\cdots Z_nf$ gerade $m$ unabhängige infinitesimale Transformationen linear ableiten lassen sollen, welche $u_1\cdots u_{n-m}$ gar nicht transformiren, in denen also die Coefficienten von $\frac{\partial f}{\partial u_1}\cdots\frac{\partial f}{\partial u_{n-m}}$ sämmtlich null sind.

Um das beweisen zu können, müssen wir die Coefficienten von $\frac{\partial f}{\partial u_1}\cdots\frac{\partial f}{\partial u_{n-m}}$ in der allgemeinen infinitesimalen Transformation $Zf=e_1Z_1f+\cdots+e_nZ_nf$ der Gruppe $Z_1f\cdots Z_nf$ berechnen.

Die infinitesimale Transformation $Zf$ ist durch die Relationen:

$$
\begin{gathered}
X_1(Z(f))-Z(X_1(f))=0,\\
\cdots,\\

X_n(Z(f))-Z(X_n(f))=0
\end{gathered}
$$

vollständig definirt. Ersetzen wir in denselben $f$ durch $u_\nu$, so erhalten wir die Relationen:

$$
\begin{gathered}
X_1(Zu_\nu)-Z\omega_{1\nu}=0,\\
\cdots,\\

X_n(Zu_\nu)-Z\omega_{n\nu}=0
\\
(\nu=1\cdots n-m).
\end{gathered}
$$

Folglich sind die Functionen $Zu_1\cdots Zu_{n-m}$ Lösungen der Differentialgleichungen:

$$
\begin{gathered}
X_k\rho_\nu-\sum_1^{n-m}{}^{\mu}
\frac{\partial\omega_{k\nu}}{\partial u_\mu}\rho_\mu=0
\\
(k=1\cdots n;\ \nu=1\cdots n-m),
\end{gathered}\tag{7}
$$

in welchen $\rho_1\cdots\rho_{n-m}$ als die unbekannten Functionen anzusehen sind.

Wenn

$$
\begin{gathered}
\rho_1=\psi_1(u_1\cdots u_{n-m},v_1\cdots v_m),\\
\cdots,\\

\rho_{n-m}=\psi_{n-m}(u_1\cdots u_{n-m},v_1\cdots v_m)
\end{gathered}\tag{8}
$$

irgend ein Lösungensystem der Differentialgleichungen (7) ist, so verschwinden die $n(n-m)$ Ausdrücke:

$$
X_k\psi_\nu-\sum_1^{n-m}{}^{\mu}
\frac{\partial\omega_{k\nu}}{\partial u_\mu}\rho_\mu
$$

bei der Substitution: $\rho_1=\psi_1$, $\cdots$, $\rho_{n-m}=\psi_{n-m}$ sämmtlich identisch. Fassen wir daher die Gleichungen (8) auf als ein Gleichungensystem in den $n+n-m$ Veränderlichen: $u_1\cdots u_{n-m}$, $v_1\cdots v_m$, $\rho_1\cdots\rho_{n-m}$, so erkennen wir sofort, dass dieses Gleichungensystem die $n$ infinitesimalen Transformationen:

$$
\begin{gathered}
U_kf=X_kf\\
+\sum_1^{n-m}{}^{\nu}
\bigl\{\sum_1^{n-m}{}^{\mu}
\frac{\partial\omega_{k\nu}}{\partial u_\mu}\rho_\mu\bigr\}
\frac{\partial f}{\partial\rho_\nu}
\\
(k=1\cdots n)
\end{gathered}\tag{9}
$$

gestattet. Umgekehrt ist auch klar: kennt man irgend ein Gleichungensystem von der Form (8), welches die infinitesimalen Transformationen $U_1f\cdots U_nf$ gestattet, so kennt man auch ein System Lösungen der Differentialgleichungen (7), denn die Functionen $\psi_1\cdots\psi_{n-m}$ sind ein solches System.

Hieraus geht hervor, dass die Bestimmung des allgemeinsten Lösungensystems der Differentialgleichungen (7) darauf hinauskommt, in den $2n-m$ Veränderlichen $u$, $v$, $\rho$ das allgemeinste Gleichungensystem (8) zu bestimmen, welches die infinitesimalen Transformationen $U_1f\cdots U_nf$ gestattet.

Jedes Gleichungensystem, welches $U_1f\cdots U_nf$ gestattet, lässt auch die sämmtlichen infinitesimalen Transformationen $(U_iU_k)$ zu. Durch Ausrechnung finden wir:

$$
\begin{gathered}
(U_iU_k)={}(X_iX_k)\\
+\sum_{\mu\nu\pi}^{1\cdots n-m}
\bigl(\omega_{i\pi}\frac{\partial^2\omega_{k\nu}}{\partial u_\mu\partial u_\pi}\\
-\omega_{k\pi}\frac{\partial^2\omega_{i\nu}}{\partial u_\mu\partial u_\pi}\bigr)\\
\rho_\mu\frac{\partial f}{\partial\rho_\nu}\\
+\sum_{\mu\nu\pi}^{1\cdots n-m}
\bigl(\frac{\partial\omega_{i\nu}}{\partial u_\mu}
\frac{\partial\omega_{k\pi}}{\partial u_\nu}\\
-\frac{\partial\omega_{k\nu}}{\partial u_\mu}
\frac{\partial\omega_{i\pi}}{\partial u_\nu}\bigr)\\
\rho_\mu\frac{\partial f}{\partial\rho_\pi},
\end{gathered}
$$

oder anders geschrieben:

$$
\begin{gathered}
(U_iU_k)=(X_iX_k)\\
+\sum_{\mu\nu}^{1\cdots n-m}
\frac{\partial}{\partial u_\mu}(X_i\omega_{k\nu}-X_k\omega_{i\nu})
\cdot\rho_\mu\frac{\partial f}{\partial\rho_\nu}.
\end{gathered}
$$

Da nun $X_1f\cdots X_nf$ eine Gruppe erzeugen, so bestehen Relationen von der Form:

$$
\begin{gathered}
(X_iX_k)=X_i(X_k(f))-X_k(X_i(f))\\
=\sum_1^n{}^{\sigma} c_{ik\sigma}X_\sigma f,
\end{gathered}
$$

es ist also insbesondere:

$$
\begin{gathered}
X_i(X_ku_\nu)-X_k(X_iu_\nu)\\
=X_i\omega_{k\nu}-X_k\omega_{i\nu}\\
=\sum_1^n{}^{\sigma} c_{ik\sigma}\omega_{\sigma\nu}
\end{gathered}
$$

und es wird:

$$
(U_iU_k)=\sum_1^n{}^{\sigma} c_{ik\sigma}U_\sigma f.
$$

Folglich erzeugen die infinitesimalen Transformationen $U_1f\cdots U_nf$ eine $n$-gliedrige Gruppe in den $2n-m$ Veränderlichen $u_1\cdots u_{n-m}$, $v_1\cdots v_m$, $\rho_1\cdots\rho_{n-m}$.

Es handelt sich also jetzt darum, das allgemeinste Gleichungensystem von der Form (8) zu bestimmen, welches die Gruppe $U_1f\cdots U_nf$ gestattet. Da $X_1f\cdots X_nf$ durch keine lineare Relation verknüpft sind, so verschwinden in der Matrix, welche zu $U_1f\cdots U_nf$ gehört, nicht alle $n$-reihigen Determinanten identisch und ebensowenig können alle diese Determinanten vermöge eines Gleichungensystems von der Form (8) verschwinden. Aus Kap. 14, Theorem 42, S. 237 ergiebt sich daher, dass jedes Gleichungensystem von der Form (8), welches die Gruppe $U_1f\cdots U_nf$ gestattet, durch Relationen zwischen den Lösungen des $n$-gliedrigen vollständigen Systems $U_1f=0$, $\cdots$, $U_nf=0$ dargestellt wird.

Nun besitzt dieses vollständige System gerade $n-m$ unabhängige Lösungen, etwa:

$$
\begin{gathered}
\Psi_\mu(u_1\cdots u_{n-m},v_1\cdots v_m,\rho_1\cdots\rho_{n-m})
\\
(k=1\cdots n-m)
\end{gathered}
$$

und zwar sind $\Psi_1\cdots\Psi_{n-m}$ in Bezug auf $\rho_1\cdots\rho_{n-m}$ von einander unabhängig, weil das vollständige System nach den Differentialquotienten $\frac{\partial f}{\partial u_1}\cdots\frac{\partial f}{\partial u_{n-m}}$, $\frac{\partial f}{\partial v_1}\cdots\frac{\partial f}{\partial v_m}$ auflösbar ist (vgl. Kap. 5, Theorem 12, S. 91). Wir schliessen daraus, dass das allgemeinste Gleichungensystem (8), welches die Gruppe $U_1f\cdots U_nf$ gestattet, die Form:

$$
\Psi_1=C_1,\quad\cdots,\quad\Psi_{n-m}=C_{n-m}
$$

erhalten kann, wo $C_1\cdots C_{n-m}$ willkürliche Constanten bezeichnen.

Lösen wir das eben gefundene Gleichungensystem nach $\rho_1\cdots\rho_{n-m}$ auf, was sicher möglich ist, so erhalten wir das allgemeinste Lösungensystem der Differentialgleichungen (7), wir sehen also, dass dieses allgemeinste Lösungensystem gerade $n-m$ wesentliche willkürliche Constanten enthält. Da nun die Differentialgleichungen (7) in den Unbekannten $\rho_1\cdots\rho_{n-m}$ linear und homogen sind, so muss das bewusste allgemeinste Lösungensystem die Form erhalten können:

$$
\begin{gathered}
\rho_\mu=C'_1\psi_\mu^{(1)}+C'_2\psi_\mu^{(2)}\\
+\cdots+C'_{n-m}\psi_\mu^{(n-m)}
\\
(\mu=1\cdots n-m),
\end{gathered}\tag{10}
$$

wo die $n-m$ Functionensysteme:

$$
\begin{gathered}
\psi_1^{(\nu)},\\
\psi_2^{(\nu)},\\
\cdots,\\
\psi_{n-m}^{(\nu)}
\\
(\nu=1\cdots n-m)
\end{gathered}
$$

ebensoviel linear unabhängige, von willkürlichen Constanten freie Lösungensysteme der Differentialgleichungen (7) darstellen und wo die $C'$ willkürliche Constanten sind. Selbstverständlich verschwindet hier die Determinante der $\psi$ nicht, da sich die Gleichungen (10) nach $C'_1\cdots C'_{n-m}$ auflösen lassen müssen.

Die Functionen: $Zu_1\cdots Zu_{n-m}$ sind nach S. 384 Lösungen der Differentialgleichungen (7), sie haben daher die Form:

$$
\begin{gathered}
Zu_\mu=\overline C_1\psi_\mu^{(1)}+\cdots+
\overline C_{n-m}\psi_\mu^{(n-m)}
\\
(\mu=1\cdots n-m).
\end{gathered}
$$

Hierbei sind die $\overline C_\nu$ Constanten, über die wir vorläufig noch nichts genaueres wissen; es wäre ja noch denkbar, dass sie durch lineare Relationen verknüpft wären.

Aus den Werthen der $Zu_\mu$ ergiebt sich für die allgemeine infinitesimale Transformation $Zf$ der Gruppe: $Z_1f\cdots Z_nf$ die folgende Darstellung:

$$
Zf=\sum_{\mu\nu}^{1\cdots n-m}\overline C_\mu\psi_\nu^{(\mu)}
\frac{\partial f}{\partial u_\nu}
+\sum_1^m{}^{\mu} Zv_\mu\frac{\partial f}{\partial v_\mu}.
$$

Da nun die $n-m$ Ausdrücke:

$$
\sum_1^{n-m}{}^{\nu}\psi_\nu^{(\mu)}\frac{\partial f}{\partial u_\nu}
\qquad(\mu=1\cdots n-m)
$$

unabhängige infinitesimale Transformationen darstellen, so lassen sich offenbar aus $Z_1f\cdots Z_nf$ mindestens $m$, also etwa gerade $m+\varepsilon$ unabhängige infinitesimale Transformationen linear ableiten, in denen die Coefficienten von $\frac{\partial f}{\partial u_1}\cdots\frac{\partial f}{\partial u_{n-m}}$ gleich Null sind. Diese $m+\varepsilon$ infinitesimalen Transformationen erzeugen natürlich eine $(m+\varepsilon)$-gliedrige Untergruppe der Gruppe: $Z_1f\cdots Z_nf$ und zwar eine Untergruppe, welche jede der $\infty^{n-m}$ $m$-fach ausgedehnten Mannigfaltigkeiten: $u_1=\mathrm{const.}$, $\cdots$, $u_{n-m}=\mathrm{const.}$ stehen lässt. Das ist aber nur möglich, wenn die ganze Zahl $\varepsilon$ gleich Null ist, denn wäre $\varepsilon>0$, so könnte die Gruppe $Z_1f\cdots Z_nf$ nicht einfach transitiv sein.

Damit ist die auf S. 383 aufgestellte Behauptung bewiesen; wir können also den folgenden Satz aussprechen:

**Satz 7.** *Sind $X_1f\cdots X_nf$ und $Z_1f\cdots Z_nf$ zwei reciproke einfach transitive Gruppen in den $n$ Veränderlichen $x_1\cdots x_n$, und ist*

$$
\begin{gathered}
u_1(x_1\cdots x_n)=\mathrm{const.},\\
\cdots,\\

u_{n-m}(x_1\cdots x_n)=\mathrm{const.}
\end{gathered}
$$

*irgend eine bei der Gruppe $X_1f\cdots X_nf$ invariante Zerlegung des Raumes $x_1\cdots x_n$ in $\infty^{n-m}$ $m$-fach ausgedehnte Mannigfaltigkeiten, so enthält die Gruppe $Z_1f\cdots Z_nf$ stets eine $m$-gliedrige Untergruppe, welche jede einzelne dieser $\infty^{n-m}$ Mannigfaltigkeiten stehen lässt.*

Durch Verbindung dieses Satzes mit dem Satze 6, S. 383 erhalten wir das

**Theorem 69.** *Ist die $n$-gliedrige Gruppe $X_1f\cdots X_nf$ in $n$ Veränderlichen $x_1\cdots x_n$ einfach transitiv, so findet man alle $m$-gliedrigen vollständigen Systeme, welche diese Gruppe gestatten, oder was dasselbe ist, alle invarianten Zerlegungen des Raumes $x_1\cdots x_n$ in $\infty^{n-m}$ $m$-fach ausgedehnte Mannigfaltigkeiten folgendermassen: Man bestimme zunächst die zu dieser Gruppe $X_1f\cdots X_nf$ gehörige reciproke einfach transitive Gruppe: $Z_1f\cdots Z_nf$ und stelle alle $m$-gliedrigen Untergruppen dieser letzteren auf; ist etwa:*

$$
\begin{gathered}
Z_\mu f=g_{\mu1}Z_1f+\cdots+g_{\mu n}Z_nf
\\
(\mu=1\cdots m)
\end{gathered}
$$

*eine der gefundenen Untergruppen, so stellen die Gleichungen: $Z_1f=0$, $\cdots$, $Z_mf=0$ eines der gesuchten vollständigen Systeme dar und bestimmen eine bei der Gruppe $X_1f\cdots X_nf$ invariante Zerlegung des Raumes $x_1\cdots x_n$ in $\infty^{n-m}$ $m$-fach ausgedehnte Mannigfaltigkeiten; bildet man für jede der gefundenen Untergruppen das $m$-gliedrige vollständige System, welches sie liefert, so erhält man alle $m$-gliedrigen vollständigen Systeme, welche die Gruppe $X_1f\cdots X_nf$ gestatten. Führt man die angedeutete Untersuchung für jede der Zahlen $m=1,2\cdots n-1$ durch, so erhält man überhaupt alle vollständigen Systeme, welche die Gruppe $X_1f\cdots X_nf$ gestatten und damit zugleich alle bei dieser Gruppe invarianten Zerlegungen des Raumes $x_1\cdots x_n$.*

Das vorstehende Theorem enthält die Lösung der Aufgabe, alle möglichen Weisen zu bestimmen, in denen eine vorgelegte *einfach transitive* Gruppe imprimitiv ist.

Es mögen jetzt die Gleichungen:

$$
u_1=\mathrm{const.},\quad\cdots,\quad u_{n-m}=\mathrm{const.}
$$

wieder irgend eine bei der Gruppe $X_1f\cdots X_nf$ invariante Zerlegung des Raumes $x_1\cdots x_n$ in $\infty^{n-m}$ $m$-fach ausgedehnte Mannigfaltigkeiten darstellen, so dass also, wenn $u_1\cdots u_{n-m}$ nebst $m$ geeigneten Functionen $v_1\cdots v_m$ als neue Veränderliche eingeführt werden, $X_1f\cdots X_nf$ die Form erhalten:

$$
\begin{gathered}
X_kf=\sum_1^{n-m}{}^{\nu}\omega_{k\nu}(u_1\cdots u_{n-m})
\frac{\partial f}{\partial v_\nu}\\
+\sum_1^m{}^{\mu}\overline\xi_{k\mu}(u_1\cdots u_{n-m},v_1\cdots v_m)
\frac{\partial f}{\partial v_\mu}.
\end{gathered}
$$

Hier können nicht alle $(n-m)$-reihigen Determinanten der Matrix:

$$
\left|\begin{array}{ccc}
\omega_{11}&\cdot&\omega_{1,n-m}\\
\cdot&\cdot&\cdot\\
\cdot&\cdot&\cdot\\
\omega_{n1}&\cdot&\omega_{n,n-m}
\end{array}\right|
$$

identisch verschwinden, sonst müssten $X_1f\cdots X_nf$ durch eine lineare Relation verknüpft sein, was gegen die Voraussetzung wäre. Verstehen wir daher unter $u_1^0\cdots u_{n-m}^0$ ein allgemeines Werthsystem, so enthält die Gruppe $X_1f\cdots X_nf$ nach Kap. 13, S. 222 gerade $\infty^{m-1}$ verschiedene infinitesimale Transformationen, welche das Gleichungensystem:

$$
u_1=u_1^0,\quad\cdots,\quad u_{n-m}=u_{n-m}^0
$$

invariant lassen; diese infinitesimalen Transformationen erzeugen dann natürlich eine $m$-gliedrige Untergruppe, die allgemeinste Untergruppe der Gruppe $X_1f\cdots X_nf$, welche die $m$-fach ausgedehnte Mannigfaltigkeit: $u_1=u_1^0$, $\cdots$, $u_{n-m}=u_{n-m}^0$ oder kurz $M$ stehen lässt.

Die eben besprochene $m$-fach ausgedehnte Mannigfaltigkeit $M$ gestattet nun auf der andern Seite auch $m$ unabhängige infinitesimale Transformationen der reciproken Gruppe $Z_1f\cdots Z_nf$, denn diese Gruppe enthält ja nach Satz 7, S. 387 eine $m$-gliedrige Untergruppe, welche jede einzelne der $\infty^{n-m}$ Mannigfaltigkeiten:

$$
u_1=\mathrm{const.},\quad\cdots,\quad u_{n-m}=\mathrm{const.}
$$

stehen lässt. Es ist überdies klar, dass $M$ keine grössere Untergruppe der Gruppe $Z_1f\cdots Z_nf$ gestatten kann, da ja $u_1^0\cdots u_{n-m}^0$ ein allgemeines Werthsystem sein soll.

Wir ersehen hieraus, dass $M$ von jeder der beiden reciproken Gruppen: $X_1f\cdots X_nf$ und: $Z_1f\cdots Z_nf$ gerade $m$ unabhängige infinitesimale Transformationen zulässt, also von jeder eine ganz bestimmte $m$-gliedrige Untergruppe.

Wir können diese beiden $m$-gliedrigen Untergruppen sichtbar machen, wenn wir irgend ein Werthsystem: $v_1^0\cdots v_m^0$ von allgemeiner Lage auswählen und die infinitesimalen Transformationen unserer beiden reciproken Gruppen nach Potenzen von: $u_1-u_1^0$, $\cdots$, $u_{n-m}-u_{n-m}^0$, $v_1-v_1^0$, $\cdots$, $v_m-v_m^0$ entwickeln. Sehen wir nämlich von den Gliedern erster und höherer Ordnung ab, so können wir ähnlich wie auf S. 379 die infinitesimalen Transformationen: $X_1f\cdots X_nf$ durch $n$ unabhängige von der Form:

$$
\begin{gathered}
\mathfrak X_1f=\frac{\partial f}{\partial u_1}+\cdots,\\
\cdots,\\

\mathfrak X_{n-m}f=\frac{\partial f}{\partial u_{n-m}}+\cdots,
\end{gathered}
$$

$$
\begin{gathered}
\mathfrak X_{n-m+1}f=\frac{\partial f}{\partial v_1}+\cdots,\\
\cdots,\\

\mathfrak X_nf=\frac{\partial f}{\partial v_m}+\cdots
\end{gathered}
$$

ersetzen und $Z_1f\cdots Z_nf$ durch $n$ von der Form:

$$
\begin{gathered}
\mathfrak Z_1f=-\frac{\partial f}{\partial u_1}+\cdots,\\
\cdots,\\

\mathfrak Z_{n-m}f=-\frac{\partial f}{\partial u_{n-m}}+\cdots,
\end{gathered}
$$

$$
\begin{gathered}
\mathfrak Z_{n-m+1}f=-\frac{\partial f}{\partial v_1}+\cdots,\\
\cdots,\\

\mathfrak Z_nf=-\frac{\partial f}{\partial v_m}+\cdots.
\end{gathered}
$$

Hier sind offenbar $\mathfrak X_{n-m+1}f\cdots\mathfrak X_nf$ unabhängige infinitesimale Transformationen, welche die Mannigfaltigkeit: $u_1=u_1^0$, $\cdots$, $u_{n-m}=u_{n-m}^0$ invariant lassen, und $\mathfrak Z_{n-m+1}f\cdots\mathfrak Z_nf$ sind unabhängige infinitesimale Transformationen, welche dasselbe thun; es sind also: $\mathfrak X_{n-m+1}f\cdots\mathfrak X_nf$ und $\mathfrak Z_{n-m+1}f\cdots\mathfrak Z_nf$ die beiden $m$-gliedrigen Untergruppen, von denen wir soeben gesprochen haben.

Aus dieser Darstellung der beiden Untergruppen lassen sich einige bemerkenswerthe Schlüsse ziehen.

Zwischen $\mathfrak X_1f\cdots\mathfrak X_nf$ bestehen Relationen von der Form:

$$
(\mathfrak X_i\mathfrak X_k)=\sum_1^n{}^{\nu} c_{ik\nu}\mathfrak X_\nu f
$$

und nach S. 379 f. bestehen zwischen $\mathfrak Z_1f\cdots\mathfrak Z_nf$ dieselben Relationen:

$$
(\mathfrak Z_i\mathfrak Z_k)=\sum_1^n{}^{\nu} c_{ik\nu}\mathfrak Z_\nu f
$$

mit denselben Constanten $c_{ik\nu}$. Hieraus ergiebt sich, dass die beiden Untergruppen: $\mathfrak X_{n-m+1}f\cdots\mathfrak X_nf$ und $\mathfrak Z_{n-m+1}f\cdots\mathfrak Z_nf$ mit einander gleichzusammengesetzt sind. Es ergiebt sich aber noch mehr. Da nämlich die beiden Gruppen: $X_1f\cdots X_nf$ und: $Z_1f\cdots Z_nf$ holoedrisch isomorph auf einander bezogen sind, wenn jeder infinitesimalen Transformation: $e_1\mathfrak X_1f+\cdots+e_r\mathfrak X_rf$ die infinitesimale Transformation: $e_1\mathfrak Z_1f+\cdots+e_r\mathfrak Z_rf$ zugeordnet wird, und da bei dieser Zuordnung offenbar der Untergruppe: $\mathfrak X_{n-m+1}f\cdots\mathfrak X_rf$ die Untergruppe: $\mathfrak Z_{n-m+1}f\cdots\mathfrak Z_rf$ entspricht, so erhellt, dass die beiden reciproken Gruppen derart holoedrisch isomorph auf einander bezogen werden können, dass die beiden $m$-gliedrigen Untergruppen, welche $M$ invariant lassen, einander entsprechen.

Fassen wir die Ergebnisse der SS. 388 ff. zusammen, so haben wir den

**Satz 8.** *Gestattet eine $m$-fach ausgedehnte Mannigfaltigkeit des Raumes $x_1\cdots x_n$ gerade $m$ unabhängige infinitesimale Transformationen und also eine $m$-gliedrige Untergruppe einer einfach transitiven Gruppe $X_1f\cdots X_nf$ dieses Raumes, so gestattet sie zugleich gerade $m$ unabhängige infinitesimale Transformationen und also eine $m$-gliedrige Untergruppe der zu $X_1f\cdots X_nf$ reciproken einfach transitiven Gruppe: $Z_1f\cdots Z_nf$. Die beiden so definirten $m$-gliedrigen Untergruppen sind gleichzusammengesetzt, und es ist möglich, die beiden reciproken einfach transitiven Gruppen derart holoedrisch isomorph auf einander zu beziehen, dass diese $m$-gliedrigen Untergruppen einander entsprechen.*

### German original footnotes for §§95–97

**F1 · p. 377, after Theorem 67.** Dieses allgemeine Theorem deutete Lie in den [Math. Ann. Bd. XXV](https://gdz.sub.uni-goettingen.de/download/pdf/PPN235181684_0025/PPN235181684_0025.pdf) an.

**F2 · p. 380, after Theorem 68.** Das Theorem 68 theilte Lie der Gesellschaft der Wissenschaften zu Christiania im Nov. 1882 und Mai 1883 mit; vgl. auch die [Math. Annalen Bd. XXV](https://gdz.sub.uni-goettingen.de/download/pdf/PPN235181684_0025/PPN235181684_0025.pdf), S. 107 ff.

### English translation: commuting transformations and reciprocal groups

**Chapter 20. Groups whose transformations commute with every transformation of a given group.**

The developments of §§89, 90 and 91, pp. 330–355, enable us to determine all transformations that leave a given $r$-parameter group

$$
X_kf=\sum_1^s{}^{i}\xi_{ki}(x_1\cdots x_s)\frac{\partial f}{\partial x_i}
\qquad(k=1\cdots r)
$$

invariant. Among these transformations, we now wish to single out those that also *leave every individual transformation of the group $X_1f\cdots X_rf$ invariant*, and study them more closely.

If a transformation $T$ leaves every individual transformation $S$ of the group $X_1f\cdots X_rf$ invariant, then, by p. 258, its relation to $S$ is

$$
T^{-1}ST=S
$$

or, equivalently,

$$
ST=TS,
$$

so it commutes with $T$. We can therefore also characterize the transformations just defined as follows: *they are the transformations that commute with every transformation of the group $X_1f\cdots X_rf$.*

**§95.**

By Chapter 15, p. 255, the expression $e_1X_1f+\cdots+e_rX_rf$ can be regarded as the general symbol of a transformation of $X_1f\cdots X_rf$. Consequently, a transformation $x_i'=\Phi_i(x_1\cdots x_s)$ leaves every individual transformation of $X_1f\cdots X_rf$ invariant if and only if it leaves $e_1X_1f+\cdots+e_rX_rf$ invariant for arbitrary choices of the $e$. That is, introducing the new variables $x_i'=\Phi_i(x)$ must turn $e_1X_1f+\cdots+e_rX_rf$ into $e_1X_1'f+\cdots+e_rX_r'f$, where

$$
X_k'f=\sum_1^s{}^{i}\xi_{ki}(x_1'\cdots x_s')\frac{\partial f}{\partial x_i'}
$$

The necessary and sufficient condition is that introducing the new variables $x_i'$ turns the $r$ infinitesimal transformations $X_1f\cdots X_rf$ into $X_1'f\cdots X_r'f$, respectively.

It is clear that transformations $x_i'=\Phi_i(x)$ of the required kind exist: the identity transformation $x_i'=x_i$ is one. Their existence also follows from Proposition 2 of the preceding chapter, p. 354, which shows that there are transformations carrying $X_1f\cdots X_rf$ to $X_1'f\cdots X_r'f$, respectively. The developments at that time further show that the most general transformation of the required kind is represented by the most general system of equations

$$
\begin{gathered}
x_1'=\Phi_1(x_1\cdots x_s),\\
\cdots,\\

x_s'=\Phi_s(x_1\cdots x_s),
\end{gathered}
$$

solvable for $x_1\cdots x_s$ and admitting the $r$-parameter group $X_1f+X_1'f$, $\cdots$, $X_rf+X_r'f$ in the $2s$ variables $x_1\cdots x_s$, $x_1'\cdots x_s'$.

Performing two transformations in succession, each leaving every individual transformation of $X_1f\cdots X_rf$ invariant, plainly gives another transformation with the same property. Hence all transformations of this kind form a group $G$. This group may be discontinuous, or may even reduce to the identity transformation. It may consist of several discrete families, each with only finitely many arbitrary parameters, or it may be infinite. Its transformations can nevertheless always be paired as inverses: if a transformation leaves every transformation of $X_1f\cdots X_rf$ invariant, its inverse naturally has the same property.

If the group $G$ just defined has only finitely many arbitrary parameters, it belongs to the category discussed in Chapter 18 and, by Theorem 56, p. 315, certainly contains a finite continuous subgroup generated by infinitesimal transformations. If $G$ is infinite, arguments similar to those of Chapter 18 show that it contains infinitely many one-parameter groups generated by infinitely many independent infinitesimal transformations.

We now set ourselves the direct task of determining all one-parameter groups that may be contained in $G$.

By Chapter 15, pp. 258–259, the $r$ expressions $X_1f\cdots X_rf$ are invariant under every transformation of the one-parameter group $Zf$ if and only if the $r$ relations

$$
\begin{gathered}
(X_kZ)=X_k(Z(f))-Z(X_k(f))=0
\\
(k=1\cdots r)
\end{gathered}
$$

hold identically; in other words, if the infinitesimal transformation $Zf$ commutes with every transformation of $X_1f\cdots X_rf$.

Thus determining all one-parameter groups of the kind defined above amounts to determining the most general infinitesimal transformation $Zf$ that commutes with every $X_kf$.

If infinitesimal transformations $Z_1f$ and $Z_2f$ commute with every $X_kf$, then all expressions $(Z_1X_k)$ and $(Z_2X_k)$ vanish identically. The Jacobi identity

$$
\bigl((Z_1Z_2)X_k\bigr)+\bigl((Z_2X_k)Z_1\bigr)
+\bigl((X_kZ_1)Z_2\bigr)=0
$$

therefore reduces to

$$
\bigl((Z_1Z_2)X_k\bigr)\equiv0.
$$

This gives

**Proposition 1.** *If infinitesimal transformations $Z_1f$ and $Z_2f$ commute with every infinitesimal transformation of the $r$-parameter group $X_1f\cdots X_rf$, then $(Z_1Z_2)$ does so as well.*

On the other hand, every infinitesimal transformation $aZ_1f+bZ_2f$ also commutes with $X_1f\cdots X_rf$, whatever values the constants $a$ and $b$ have. Thus, if there happen to be only finitely many independent infinitesimal transformations, say $q$ of them, $Z_1f\cdots Z_qf$, commuting with $X_1f\cdots X_rf$, the most general infinitesimal transformation of the same kind has the form $\lambda_1Z_1f+\cdots+\lambda_qZ_qf$, where $\lambda_1\cdots\lambda_q$ are arbitrary parameters. Proposition 1 then requires relations of the form

$$
(Z_iZ_k)=\sum_1^q{}^{\sigma} c'_{ik\sigma}Z_\sigma f
$$

so *$Z_1f\cdots Z_qf$ generates a $q$-parameter group.*

We now try to determine directly the most general infinitesimal transformation

$$
Zf=\sum_1^s{}^{i}\xi_i(x_1\cdots x_s)\frac{\partial f}{\partial x_i}
$$

that commutes with all infinitesimal transformations of $X_1f\cdots X_rf$.

The $r$ conditions

$$
(X_1Z)=0,\quad\cdots,\quad(X_rZ)=0
$$

immediately separate into the following $rs$ equations:

$$
X_k\xi_i=Z\xi_{ki}\qquad(k=1\cdots r;\ i=1\cdots s),
$$

or, written out,

$$
\begin{gathered}
\sum_1^s{}^{\nu}\xi_{k\nu}(x)\frac{\partial\xi_i}{\partial x_\nu}\\
=\sum_1^s{}^{\nu}\frac{\partial\xi_{ki}}{\partial x_\nu}\xi_\nu
\\
(k=1\cdots r;\ i=1\cdots s).
\end{gathered}\tag{1}
$$

We must therefore determine their most general solutions for $\xi_1\cdots\xi_s$.

If

$$
\xi_i=\omega_i(x_1\cdots x_s)\qquad(i=1\cdots s)\tag{2}
$$

is any solution system of (1), the expressions

$$
X_k\omega_i-\sum_1^s{}^{\nu}\frac{\partial\xi_{ki}}{\partial x_\nu}\xi_\nu
$$

vanish identically after the substitution $\xi_1=\omega_1(x)$, $\cdots$, $\xi_s=\omega_s(x)$. In other words, the system (2) in the $2s$ variables $x_1\cdots x_s$, $\xi_1\cdots\xi_s$ admits the $r$ infinitesimal transformations

$$
\begin{gathered}
W_kf=X_kf+\sum_1^s{}^{i}
\bigl\{\sum_1^s{}^{\nu}\frac{\partial\xi_{ki}}{\partial x_\nu}\xi_\nu\bigr\}
\frac{\partial f}{\partial\xi_i}
\\
(k=1\cdots r).
\end{gathered}
$$

Conversely, if a system of the form (2) admits $W_1f\cdots W_rf$, then $\omega_1(x)\cdots\omega_s(x)$ are plainly solutions of (1). Integrating (1) is therefore equivalent to finding the most general system (2) admitting $W_1f\cdots W_rf$.

Every system admitting $W_1f\cdots W_rf$ also admits the infinitesimal transformation $W_k(W_j(f))-W_j(W_k(f))=(W_kW_j)$. Let us calculate it.

We obtain

$$
\begin{gathered}
(W_kW_j)={}(X_kX_j)\\
+\sum_{i\mu\nu}^{1\cdots s}
\bigl\{\xi_{k\nu}\frac{\partial^2\xi_{ji}}{\partial x_\mu\partial x_\nu}\\
-\xi_{j\nu}\frac{\partial^2\xi_{ki}}{\partial x_\mu\partial x_\nu}\bigr\}\\
\xi_\mu\frac{\partial f}{\partial\xi_i}\\
+\sum_{i\mu\nu}^{1\cdots s}
\bigl\{\frac{\partial\xi_{k\nu}}{\partial x_\mu}
\frac{\partial\xi_{ji}}{\partial x_\nu}\\
-\frac{\partial\xi_{j\nu}}{\partial x_\mu}
\frac{\partial\xi_{ki}}{\partial x_\nu}\bigr\}\\
\xi_\mu\frac{\partial f}{\partial\xi_i},
\end{gathered}
$$

The right-hand side can be written as

$$
\begin{gathered}
(X_kX_j)+\sum_{i\mu}^{1\cdots s}\frac{\partial}{\partial x_\mu}
\sum_1^s{}^{\nu}
\bigl\{\xi_{k\nu}\frac{\partial\xi_{ji}}{\partial x_\nu}\\
-\xi_{j\nu}\frac{\partial\xi_{ki}}{\partial x_\nu}\bigr\}\\
\xi_\mu\frac{\partial f}{\partial\xi_i}.
\end{gathered}
$$

But there are relations of the form

$$
(X_kX_j)=\sum_1^r{}^{\sigma} c_{kj\sigma}X_\sigma f,
$$

which imply

$$
\sum_1^s{}^{\nu}
\left\{\xi_{k\nu}\frac{\partial\xi_{ji}}{\partial x_\nu}
-\xi_{j\nu}\frac{\partial\xi_{ki}}{\partial x_\nu}\right\}
=\sum_1^r{}^{\sigma} c_{kj\sigma}\xi_{\sigma i},
$$

Hence we simply have

$$
(W_kW_j)=\sum_1^r{}^{\sigma} c_{kj\sigma}W_\sigma f.
$$

Thus $W_1f\cdots W_rf$ generates an $r$-parameter group in the $2s$ variables $x_1\cdots x_s$, $\xi_1\cdots\xi_s$, as one might have expected.

Suppose that some $n$ of the infinitesimal transformations $X_1f\cdots X_rf$, say $X_1f\cdots X_nf$, satisfy no linear relation of the form

$$
\begin{gathered}
\chi_1(x_1\cdots x_s)\cdot X_1f\\
+\cdots+
\chi_n(x_1\cdots x_s)\cdot X_nf=0
\end{gathered}
$$

while $X_{n+1}f\cdots X_rf$ can be expressed as

$$
\begin{gathered}
X_{n+k}f=\sum_1^n{}^{\rho}\varphi_{k\rho}(x_1\cdots x_s)\cdot X_\rho f
\\
(k=1\cdots r-n).
\end{gathered}\tag{3}
$$

Under these assumptions, equations (1) can also be written

$$
X_\rho\xi_i-Z\xi_{\rho i}=0
\qquad(\rho=1\cdots n;\ i=1\cdots s)
$$

$$
\begin{gathered}
\sum_1^n{}^{\rho}\varphi_{k\rho}(x)\cdot X_\rho\xi_i-Z\xi_{n+k,i}=0
\\
(k=1\cdots r-n;\ i=1\cdots s).
\end{gathered}
$$

Eliminating $X_1\xi_i\cdots X_n\xi_i$ therefore gives the following finite equations among $\xi_1\cdots\xi_s$:

$$
\begin{gathered}
\sum_1^s{}^{\pi}
\bigl\{\frac{\partial\xi_{n+k,i}}{\partial x_\pi}\\
-\sum_1^n{}^{\rho}\varphi_{k\rho}\frac{\partial\xi_{\rho i}}{\partial x_\pi}\bigr\}
\xi_\pi=0
\\
(k=1\cdots r-n;\ i=1\cdots s).
\end{gathered}\tag{4}
$$

Every system of the form (2) admitting $W_1f\cdots W_rf$ must plainly include equations (4).

Equations (4) are linear and homogeneous in $\xi_1\cdots\xi_s$. If exactly $s$ of them are independent, $\xi_1=0$, $\cdots$, $\xi_s=0$ is the only solution system satisfying them all. In that case, there is only one system of the form (2) admitting $W_1f\cdots W_rf$, namely $\xi_1=0$, $\cdots$, $\xi_s=0$. There is consequently no infinitesimal transformation $Zf$ commuting with every $X_kf$.

The situation is different if equations (4) reduce to fewer than $s$, say $m<s$, independent equations. We shall see that, besides the unusable system $\xi_1=0$, $\cdots$, $\xi_s=0$, there are then other systems of the form (2) admitting $W_1f\cdots W_rf$.

First, we observe that system (4) admits $W_1f\cdots W_rf$.

To prove this, write the matrix belonging to the infinitesimal transformations $W_1f\cdots W_rf$:

$$
\begin{gathered}
\left|
\begin{array}{cccccc}
\xi_{11}&\cdot&\xi_{1s}&
\displaystyle\sum_1^s{}^{\nu}\frac{\partial\xi_{11}}{\partial x_\nu}\xi_\nu&
\cdot&\displaystyle\sum_1^s{}^{\nu}\frac{\partial\xi_{1s}}{\partial x_\nu}\xi_\nu\\
\cdot&\cdot&\cdot&\cdot&\cdot&\cdot\\
\xi_{r1}&\cdot&\xi_{rs}&
\displaystyle\sum_1^s{}^{\nu}\frac{\partial\xi_{r1}}{\partial x_\nu}\xi_\nu&
\cdot&\displaystyle\sum_1^s{}^{\nu}\frac{\partial\xi_{rs}}{\partial x_\nu}\xi_\nu
\end{array}
\right|.\\
\text{(5)}
\end{gathered}
$$

We shall show that (4) is one of the systems obtained by setting every $(n+1)$-rowed determinant of this matrix equal to zero. Chapter 14, p. 228, will then show that (4) admits $W_1f\cdots W_rf$.

Among the $(n+1)$-rowed determinants of matrix (5), there are ones of the form

$$
D=\left|
\begin{array}{cccc}
\xi_{1\kappa_1}&\cdot&\xi_{1\kappa_n}&
\displaystyle\sum_1^s{}^{\nu}\frac{\partial\xi_{1\sigma}}{\partial x_\nu}\xi_\nu\\
\cdot&\cdot&\cdot&\cdot\\
\xi_{n\kappa_1}&\cdot&\xi_{n\kappa_n}&
\displaystyle\sum_1^s{}^{\nu}\frac{\partial\xi_{n\sigma}}{\partial x_\nu}\xi_\nu\\
\xi_{n+j,\kappa_1}&\cdot&\xi_{n+j,\kappa_n}&
\displaystyle\sum_1^s{}^{\nu}\frac{\partial\xi_{n+j,\sigma}}{\partial x_\nu}\xi_\nu
\end{array}\right|.
$$

Using the identities following from (3),

$$
\begin{gathered}
\xi_{n+j,\pi}=\sum_1^n{}^{\nu}\varphi_{j\nu}(x)\cdot\xi_{\nu\pi}
\\
(\pi=1\cdots s;\ j=1\cdots r-n),
\end{gathered}
$$

we can plainly write $D$ as

$$
\begin{gathered}
D=\sum_1^n\pm\xi_{1\kappa_1}\cdots\xi_{n\kappa_n}\cdot\\
\sum_1^s{}^{\nu}
\bigl\{\frac{\partial\xi_{n+j,\sigma}}{\partial x_\nu}\\
-\sum_1^n{}^{\tau}\varphi_{j\tau}\frac{\partial\xi_{\tau\sigma}}{\partial x_\nu}\bigr\}
\xi_\nu.
\end{gathered}
$$

Under the stated assumptions, not all determinants of the form

$$
\sum\pm\xi_{1\kappa_1}\cdots\xi_{n\kappa_n}
$$

vanish identically. Setting every determinant of the form $D$ equal to zero therefore gives either relations involving $x_1\cdots x_s$ alone, or system (4). As is readily seen, this system makes all $(n+1)$-rowed determinants of matrix (5) vanish, so it admits $W_1f\cdots W_rf$.

Chapter 14, pp. 236–238, now provides the means to determine the most general system (2) admitting $W_1f\cdots W_rf$ and including equations (4).

System (4) makes every $(n+1)$-rowed determinant of matrix (5) vanish, but does not make every $n$-rowed determinant vanish. Nor can a system of the form (2) make every $n$-rowed determinant of matrix (5) zero. We therefore proceed as follows. Solve (4) for $m$ of the quantities $\xi_1\cdots\xi_s$, say $\xi_1\cdots\xi_m$. Following the cited developments, form the reduced infinitesimal transformations $\overline W_1f\cdots\overline W_rf$ in the $2s-m$ variables $x_1\cdots x_s$, $\xi_{m+1}\cdots\xi_s$. Finally, find any $2s-m-n$ independent solutions of the $n$-term complete system formed by the $n$ equations $\overline W_1f=0$, $\cdots$, $\overline W_nf=0$.

The $n$ equations $\overline W_1f=0$, $\cdots$, $\overline W_nf=0$ can be solved for $n$ of the derivatives $\frac{\partial f}{\partial x_1}\cdots\frac{\partial f}{\partial x_s}$. Their $2s-m-n$ independent solutions are therefore independent with respect to $s-n$ of the $x$ and the variables $\xi_{m+1}\cdots\xi_s$ (compare Chapter 5, Theorem 12, p. 91). Among the solutions of $W_kf=0$ there are exactly $s-n$ independent ones also satisfying the $n$-term complete system $X_1f=0$, $\cdots$, $X_nf=0$, and hence depending only on the $x$. Call them

$$
u_1(x_1\cdots x_s)\cdots u_{s-n}(x_1\cdots x_s)
$$

If, therefore,

$$
\begin{gathered}
\mathfrak B_1(\xi_{m+1}\cdots\xi_s,x_1\cdots x_s),\\
\cdots,\\

\mathfrak B_{s-m}(\xi_{m+1}\cdots\xi_s,x_1\cdots x_s)
\end{gathered}
$$

are any $s-m$ solutions of $\overline W_kf=0$ independent of one another and of the $u$, they are necessarily independent with respect to $\xi_{m+1}\cdots\xi_s$.

The most general system (2) admitting $W_1f\cdots W_rf$ is now obtained by adjoining to (4), in the most general way, $s-m$ independent relations among $u_1\cdots u_{s-n}$, $\mathfrak B_1\cdots\mathfrak B_{s-m}$, solvable for $\xi_{m+1}\cdots\xi_s$. These relations must plainly also be solvable for $\mathfrak B_1\cdots\mathfrak B_{s-m}$, so they can take the form

$$
\begin{gathered}
\mathfrak B_\mu(\xi_{m+1}\cdots\xi_s,x_1\cdots x_s)\\
=\Omega_\mu\bigl(u_1(x)\cdots u_{s-n}(x)\bigr)
\\
(\mu=1\cdots s-m)
\end{gathered}\tag{6}
$$

The $\Omega_\mu$ have no restrictions: they are completely arbitrary functions of their arguments.

Adjoin equations (6) to (4) and solve all of them for $\xi_1\cdots\xi_s$, which is always possible. This gives the most general system (2) admitting $W_1f\cdots W_rf$, and hence the most general solution system of (1). It plainly contains $s-m$ arbitrary functions of $u_1\cdots u_{s-n}$.

But equations (1) are linear and homogeneous in the unknowns $\xi_1\cdots\xi_s$. We can therefore conclude that their most general solution system $\xi_1\cdots\xi_s$ is obtained from $s-m$ particular solution systems

$$
\xi_{\mu1}(x)\cdots\xi_{\mu s}(x)\qquad(\mu=1\cdots s-m)
$$

as follows:

$$
\begin{gathered}
\xi_i=\chi_1(u_1\cdots u_{s-n})\cdot\xi_{1i}\\
+\cdots+\chi_{s-m}(u_1\cdots u_{s-n})\cdot\xi_{s-m,i}
\\
(i=1\cdots s),
\end{gathered}
$$

Here the $\chi$ are completely arbitrary functions of the $u$. The particular solution systems must naturally be such that there are no $s-m$ functions $\psi_1(u_1\cdots u_{s-n})\cdots\psi_{s-m}(u_1\cdots u_{s-n})$ satisfying the $s$ equations

$$
\begin{gathered}
\psi_1(u)\cdot\xi_{1i}+\cdots+\psi_{s-m}(u)\cdot\xi_{s-m,i}=0
\\
(i=1\cdots s)
\end{gathered}
$$

identically.

One can even show that there are no $s-m$ functions $\Psi_1(x_1\cdots x_s)\cdots\Psi_{s-m}(x_1\cdots x_s)$ satisfying the $s-m$ equations

$$
\begin{gathered}
\Psi_1(x)\cdot\xi_{1i}+\cdots+
\Psi_{s-m}(x)\cdot\xi_{s-m,i}=0
\\
(i=1\cdots s)
\end{gathered}
$$

identically. Indeed, the $s-m$ equations

$$
\begin{gathered}
\xi_{m+\sigma}=\sum_1^{s-m}{}^{\mu}\chi_\mu(u)\cdot\xi_{\mu,m+\sigma}
\\
(\sigma=1\cdots s-m)
\end{gathered}
$$

are plainly equivalent to (6). They must therefore be solvable for $\chi_1\cdots\chi_{s-m}$, and the determinant

$$
\sum\pm\xi_{1,m+1}\cdots\xi_{s-m,m+s-m}
$$

cannot vanish identically.

With these preparations, we can finally give the form of the most general infinitesimal transformation $Zf$ commuting with $X_1f\cdots X_rf$. It is

$$
Zf=\sum_1^{s-m}{}^{\mu}\chi_\mu(u_1\cdots u_{s-m})\cdot Z_\mu f,
$$

where the $s-m$ infinitesimal transformations

$$
\begin{gathered}
Z_\mu f=\sum_1^s{}^{i}\xi_{\mu i}(x_1\cdots x_s)\frac{\partial f}{\partial x_i}
\\
(\mu=1\cdots s-m)
\end{gathered}
$$

satisfy no linear relation of the form

$$
\begin{gathered}
\Psi_1(x_1\cdots x_s)\cdot Z_1f\\
+\cdots+
\Psi_{s-m}(x_1\cdots x_s)\cdot Z_{s-m}f=0
\end{gathered}
$$

Moreover, by Proposition 1, p. 369, every infinitesimal transformation $(Z_\mu Z_\nu)$ also commutes with $X_1f\cdots X_rf$. There are therefore relations of the special form

$$
\begin{gathered}
(Z_\mu Z_\nu)=\sum_1^{s-m}{}^{\pi}
\omega_{\mu\nu\pi}(u_1\cdots u_{s-m})\cdot Z_\pi f
\\
(\mu,\nu=1\cdots s-m).
\end{gathered}
$$

We see that an infinitesimal transformation commuting with $X_1f\cdots X_rf$ exists if and only if the number $m$ defined on p. 372 is smaller than the number $s$ of variables $x$. If $m<s$ and also $n<s$, so the group $X_1f\cdots X_rf$ is intransitive, the most general infinitesimal transformation $Zf$ commuting with $X_1f\cdots X_rf$ depends on arbitrary functions. If $n=s$, so $X_1f\cdots X_rf$ is transitive, the most general infinitesimal transformation $Zf$ commuting with $X_1f\cdots X_rf$ is a linear combination of $s-m$ independent infinitesimal transformations $Z_1f\cdots Z_{s-m}f$. By the earlier observation on p. 369, these generate an $(s-m)$-parameter group. —

We know that an infinitesimal transformation commuting with $X_1f\cdots X_rf$ exists only if equations (4) reduce to fewer than $s$ independent equations. We can make this condition clearer by recalling identities (3), or their equivalent form

$$
\begin{gathered}
\xi_{n+k,i}-\sum_1^n{}^{\rho}\varphi_{k\rho}(x)\cdot\xi_{\rho i}=0
\\
(k=1\cdots r-n;\ i=1\cdots s)
\end{gathered}
$$

which defines the functions $\varphi_{k\rho}$. Differentiating these identities with respect to $x_j$ gives

$$
\begin{gathered}
\frac{\partial\xi_{n+k,i}}{\partial x_j}\\
-\sum_1^n{}^{\rho}
\bigl\{\varphi_{k\rho}\frac{\partial\xi_{\rho i}}{\partial x_j}\\
+\xi_{\rho i}\frac{\partial\varphi_{k\rho}}{\partial x_j}\bigr\}=0
\\
(k=1\cdots r-n;\ i,j=1\cdots s),
\end{gathered}
$$

By these identities, equations (4) can be replaced by the equivalent equations

$$
\begin{gathered}
\sum_1^n{}^{\rho}\xi_{\rho i}\sum_1^s{}^{j}
\xi_j\frac{\partial\varphi_{k\rho}}{\partial x_j}=0
\\
(i=1\cdots s;\ k=1\cdots r-n)
\end{gathered}
$$

Since not all determinants of the form $\sum\pm\xi_{\kappa_1}\cdots\xi_{\kappa_n}$ vanish identically, these last equations are in turn equivalent to

$$
\begin{gathered}
\sum_1^s{}^{j}\xi_j\frac{\partial\varphi_{k\rho}}{\partial x_j}=0
\\
(k=1\cdots r-n;\ \rho=1\cdots n).
\end{gathered}\tag{4'}
$$

Thus an infinitesimal transformation $Zf$ commuting with $X_1f\cdots X_rf$ exists only if equations (4'), linear in the $\xi_i$, reduce to fewer than $s$ independent equations.

Equations (4') are clearer than (4) and have a simple meaning: each of the $n(r-n)$ functions $\varphi_{k\rho}(x_1\cdots x_s)$ admits all the infinitesimal transformations $Zf$.

If exactly $m$ equations in (4) are independent, exactly $m$ equations in (4') are independent as well. Hence $m$ is simply the number of independent functions among the $n(r-n)$ functions $\varphi_{k\rho}(x)$.

We summarize the results as follows.

**Theorem 67.** *Suppose that, among the $r$ independent infinitesimal transformations*

$$
X_kf=\sum_1^s{}^{i}\xi_{ki}(x_1\cdots x_s)\frac{\partial f}{\partial x_i}
\qquad(k=1\cdots r)
$$

*of an $r$-parameter group, some, say $X_1f\cdots X_nf$, satisfy no linear relation, while $X_{n+1}f\cdots X_rf$ can be expressed linearly through $X_1f\cdots X_nf$:*

$$
\begin{gathered}
X_{n+j}f=\sum_1^n{}^{\rho}\varphi_{j\rho}(x_1\cdots x_s)\cdot X_\rho f
\\
(j=1\cdots r-n),
\end{gathered}
$$

*If exactly $s$ independent functions occur among the $n(r-n)$ functions $\varphi_{k\rho}$, no infinitesimal transformation commutes with every $X_kf$. If fewer than $s$, say only $m$, independent functions occur among the $\varphi_{k\rho}$, there are infinitesimal transformations commuting with $X_1f\cdots X_rf$. The most general such infinitesimal transformation $Zf$ has the form*

$$
\begin{gathered}
Zf=\psi_1(u_1\cdots u_{s-n})\cdot Z_1f\\
+\cdots+
\psi_{s-m}(u_1\cdots u_{s-n})\cdot Z_{s-m}f,
\end{gathered}
$$

*Here $u_1\cdots u_{s-n}$ are independent solutions of the $n$-term complete system $X_1f=0$, $\cdots$, $X_nf=0$; $\psi_1\cdots\psi_{s-m}$ are arbitrary functions of their arguments; and the infinitesimal transformations*

$$
\begin{gathered}
Z_\mu f=\sum_1^s{}^{i}\xi_{\mu i}(x_1\cdots x_s)\frac{\partial f}{\partial x_i}
\\
(\mu=1\cdots s-m)
\end{gathered}
$$

*commute with $X_1f\cdots X_rf$, satisfy no linear relation and obey pairwise relations of the form*

$$
(Z_\mu Z_\nu)=\sum_1^{s-m}{}^{\pi}
\omega_{\mu\nu\pi}(u_1\cdots u_{s-m})\cdot Z_\pi f
$$

\*)

Some results stated in this theorem also follow directly from the preceding chapter. If exactly $s$ of the functions $\varphi_{k\rho}(x_1\cdots x_s)$ are independent, then, by p. 344, the equations

$$
\begin{gathered}
\varphi_{k\rho}(x_1'\cdots x_s')=\varphi_{k\rho}(x_1\cdots x_s)
\\
(k=1\cdots r-n;\ \rho=1\cdots n)
\end{gathered}
$$

represent the most general transformation carrying $X_1f\cdots X_rf$ to $X_1'f\cdots X_r'f$, respectively. If fewer than $s$ of the $\varphi_{k\rho}$ are independent functions, Theorem 65, p. 353, gives a continuous family of transformations leaving each $X_kf$ invariant. We already observed on p. 368 that all such transformations form a group, which can directly be seen to contain one-parameter groups.

It seems appropriate to state the following proposition explicitly.

**Proposition 2.** *If there is any infinitesimal transformation commuting with all infinitesimal transformations $X_1f\cdots X_rf$ of an $r$-parameter group on $x_1\cdots x_s$, the most general infinitesimal transformation commuting with $X_1f\cdots X_rf$ contains arbitrary functions when the group $X_1f\cdots X_rf$ is intransitive, and only arbitrary parameters when the group is transitive.*

**§96.**

The case where $X_kf$ is simply transitive, that is, $s=r=n$, is especially important.

To find the most general transformation $x_i'=\Phi_i(x_1\cdots x_n)$ carrying each $X_kf$ to $X_k'f$ in this case, we need only find $n$ independent solutions $\Omega_1\cdots\Omega_n$ of the $n$-term complete system

$$
X_kf+X_k'f=0\qquad(k=1\cdots n)
$$

and set them equal to arbitrary constants $a_1\cdots a_n$. The equations

$$
\Omega_k(x_1\cdots x_n,x_1'\cdots x_n')=a_k
\qquad(k=1\cdots n)
$$

are then solvable both for $x$ and for $x'$, and represent the required transformation.

We know in advance that all transformations $\Omega_k=a_k$ form a group. We now see that this group has $n$ parameters and is simply transitive. This follows immediately from the form in which the group is given, solved for its $n$ parameters.

The group

$$
\Omega_1(x,x')=a_1,\quad\cdots,\quad\Omega_n(x,x')=a_n
$$

contains the identity transformation and $n$ independent infinitesimal transformations

$$
Z_kf=\sum_1^n{}^{i}\xi_{ki}(x_1\cdots x_n)\frac{\partial f}{\partial x_i}
\qquad(k=1\cdots n),
$$

This follows from the preceding section, but is also clear in itself, since the group's transformations can be paired as inverses, so Theorem 56 of Chapter 18, p. 315, applies. Transitivity of $Z_1f\cdots Z_nf$ also implies that $Z_1f\cdots Z_nf$ satisfies no linear relation of the form $\sum\chi_i(x_1\cdots x_s)Z_if=0$.

There is a complete reciprocal relation between the two *simply transitive* groups $X_kf$ and $Z_if$. If the $X_kf$ are given, the general infinitesimal transformation $Zf=\sum e_iZ_if$ is fully defined by the $n$ equations

$$
X_k(Z(f))-Z(X_k(f))=0\qquad(k=1\cdots n)
$$

If, conversely, the $Z_if$ are given, the $n$ equations

$$
X(Z_i(f))-Z_i(X(f))=0\qquad(i=1\cdots n)
$$

similarly determine the general infinitesimal transformation

$$
Xf=\sum e_kX_kf.
$$

This does not yet exhaust the special relation between the groups. As we shall now show, they also have the same composition. Since both are simply transitive, it follows at once that they are similar to one another (compare Chapter 19, Theorem 64, p. 340).

Imagine the coefficients $\xi_{k\nu}$ and $\xi_{i\nu}$ in the infinitesimal transformations $X_kf$ and $Z_if$ expanded in powers of $x_1\cdots x_n$. We assume that $x_1=0$, $\cdots$, $x_n=0$ is a point in the most general position. By Chapter 13, p. 217, the simply transitive group $X_kf$ contains exactly $n$ infinitesimal transformations of order zero in $x_1\cdots x_n$, from which no infinitesimal transformation of first or higher order can be formed as a linear combination.

We can therefore replace $X_1f\cdots X_nf$ by $n$ other independent infinitesimal transformations $\mathfrak X_1f\cdots\mathfrak X_nf$, which, omitting terms of second and higher order, have the form

$$
\begin{gathered}
\mathfrak X_kf=\frac{\partial f}{\partial x_k}\\
+\sum_{\mu\nu}^{1\cdots n} h_{k\mu\nu}x_\mu\frac{\partial f}{\partial x_\nu}\\
+\cdots\\
(k=1\cdots n)
\end{gathered}
$$

We can similarly replace $Z_1f\cdots Z_nf$ by $n$ independent infinitesimal transformations of the form

$$
\begin{gathered}
\mathfrak Z_if=-\frac{\partial f}{\partial x_i}\\
+\sum_{\mu\nu}^{1\cdots n} l_{i\mu\nu}x_\mu\frac{\partial f}{\partial x_\nu}\\
+\cdots\\
(i=1\cdots n)
\end{gathered}
$$

With these preparations, form the equation $(\mathfrak X_k\mathfrak Z_i)=0$. It takes the form

$$
\sum_1^n{}^{\nu}(l_{ik\nu}+h_{ki\nu})\frac{\partial f}{\partial x_\nu}
+\cdots=0,
$$

and hence

$$
l_{ik\nu}=-h_{ki\nu}.
$$

Calculations of the same kind give

$$
(\mathfrak X_k\mathfrak X_j)
=\sum_1^n{}^{\nu}(h_{jk\nu}-h_{kj\nu})\frac{\partial f}{\partial x_\nu}
+\cdots
$$

$$
\begin{gathered}
(\mathfrak Z_k\mathfrak Z_j)\\
=\sum_1^n{}^{\nu}(-l_{jk\nu}+l_{kj\nu})\frac{\partial f}{\partial x_\nu}\\
+\cdots\\
=\sum_1^n{}^{\nu}(h_{kj\nu}-h_{jk\nu})\frac{\partial f}{\partial x_\nu}\\
+\cdots.
\end{gathered}
$$

On the other hand,

$$
\begin{gathered}
(\mathfrak X_k\mathfrak X_j)=\sum_1^n{}^{\nu} c_{kj\nu}\mathfrak X_\nu f,
\\

(\mathfrak Z_k\mathfrak Z_j)=\sum_1^n{}^{\nu} c'_{kj\nu}\mathfrak Z_\nu f;
\end{gathered}
$$

Substitute the expressions just found for $\mathfrak X_\nu f$, $\mathfrak Z_\nu f$, $(\mathfrak X_k\mathfrak X_j)$ and $(\mathfrak Z_k\mathfrak Z_j)$, and then set $x_1=0$, $\cdots$, $x_n=0$. The result is

$$
c_{kj\nu}=h_{jk\nu}-h_{kj\nu}=c'_{kj\nu}.
$$

Thus the two groups do have the same composition and, as observed above, are consequently similar. We obtain

**Theorem 68.** *If $X_1f\cdots X_nf$ are independent infinitesimal transformations of a simply transitive group in the variables $x_1\cdots x_n$, then the $n$ equations $(X_kZ)=0$ define the general infinitesimal transformation $Zf$ of a second simply transitive group $Z_1f\cdots Z_nf$ having the same composition as $X_1f\cdots X_nf$ and also similar to it. The relation between these simply transitive groups is mutual: each consists of all the one-parameter groups whose transformations commute with every transformation of the other group.*\*)

It is convenient to call $X_kf$ and $Z_if$ *reciprocal* transformation groups, or to call either the reciprocal group of the other.

Recall from Chapter 16, p. 276, that the distinguished infinitesimal transformations $e_1X_1f+\cdots+e_nX_nf=Yf$ of $X_1f\cdots X_nf$ are defined by $(X_kY)=0$. We can therefore state

**Proposition 3.** *The infinitesimal transformations common to two reciprocal simply transitive groups are precisely the distinguished infinitesimal transformations of both groups.*

Let the $n$-parameter groups $X_1f\cdots X_nf$ and $Z_1f\cdots Z_nf$ in the $n$ variables $x_1\cdots x_n$ be simply transitive and reciprocal. If introducing new variables $x_1'\cdots x_n'$ turns the $X_kf$ into $X_k'f$ and the $Z_kf$ into $Z_k'f$, the simply transitive groups $X_1'f\cdots X_n'f$ and $Z_1'f\cdots Z_n'f$ are also reciprocal. This follows directly from $(X_k'Z_j')=(X_kZ_j)\equiv0$.

In particular, this gives

**Proposition 4.** *If a transformation leaves an $n$-parameter simply transitive group in $n$ variables invariant, it also leaves its reciprocal simply transitive group invariant.*

Finally, this implies

**Proposition 5.** *The largest group on $x_1\cdots x_n$ containing an $n$-parameter simply transitive group as an invariant subgroup is the same as the largest group containing its reciprocal group as an invariant subgroup.*

We give a few simple examples of the preceding general developments on simply transitive groups.

The group

$$
\frac{\partial f}{\partial x},\quad
x\frac{\partial f}{\partial x}+y\frac{\partial f}{\partial y}
$$

on the plane $x$, $y$ is simply transitive. The finite equations of its reciprocal group are obtained by integrating the complete system

$$
\begin{gathered}
\frac{\partial f}{\partial x}+\frac{\partial f}{\partial x'}=0,\\

x\frac{\partial f}{\partial x}+y\frac{\partial f}{\partial y}\\
+x'\frac{\partial f}{\partial x'}+y'\frac{\partial f}{\partial y'}=0
\end{gathered}
$$

in the form

$$
\frac{x'-x}{y}=a,\qquad\frac{y'}y=b,
$$

Solving for $x'$ and $y'$ gives

$$
x'=x+ay,\qquad y'=by.
$$

The infinitesimal transformations of the reciprocal group are therefore

$$
y\frac{\partial f}{\partial x},\qquad y\frac{\partial f}{\partial y}.
$$

An interesting example is supplied by the six-parameter projective group of a nondegenerate quadric surface in ordinary space. It contains two reciprocal three-parameter simply transitive groups: one leaves every generator in one ruling fixed, while the other leaves every generator in the other ruling fixed.

If $z-xy=0$ is the equation of the surface, one of the two simply transitive groups is

$$
X_1f=\frac{\partial f}{\partial x}+y\frac{\partial f}{\partial z},
\qquad
X_2f=x\frac{\partial f}{\partial x}+z\frac{\partial f}{\partial z},
$$

$$
X_3f=x^2\frac{\partial f}{\partial x}+(xy-z)\frac{\partial f}{\partial y}
+xz\frac{\partial f}{\partial z}
$$

and the other is

$$
Z_1f=\frac{\partial f}{\partial y}+x\frac{\partial f}{\partial z},
\qquad
Z_2f=y\frac{\partial f}{\partial y}+z\frac{\partial f}{\partial z},
$$

$$
Z_3f=(xy-z)\frac{\partial f}{\partial x}+y^2\frac{\partial f}{\partial y}
+yz\frac{\partial f}{\partial z}
$$

The reciprocal groups are naturally similar. Here, however, the similarity is given by a *projective* transformation: any projective transformation interchanging the two rulings of the surface.

**§97.**

We continue the general study of reciprocal simply transitive groups.

Let $X_1f\cdots X_nf$ and $Z_1f\cdots Z_nf$ be reciprocal simply transitive groups in the variables $x_1\cdots x_n$.

If $n$ were equal to 1, the groups would be identical, as is easily checked. We therefore suppose that $n$ is greater than 1. Then $Z_1f\cdots Z_nf$ certainly contains subgroups. If $Z_1f\cdots Z_mf$ $(m<n)$ is one, the equations

$$
Z_1f=0,\quad\cdots,\quad Z_mf=0
$$

form an $m$-term complete system which, by the identities

$$
\begin{gathered}
(X_iZ_1)\equiv0,\\
\cdots,\\
(X_iZ_m)\equiv0
\\
(i=1\cdots n)
\end{gathered}
$$

admits $X_1f\cdots X_nf$ (compare Chapter 8, Theorem 20, p. 140). Thus $X_1f\cdots X_nf$ is *imprimitive*.

If $u_1\cdots u_{n-m}$ are independent solutions of $Z_1f=0$, $\cdots$, $Z_mf=0$, Chapter 8, Proposition 1, p. 139, gives relations of the form

$$
\begin{gathered}
X_iu_\nu=\omega_{i\nu}(u_1\cdots u_{n-m})
\\
(i=1\cdots n;\ \nu=1\cdots n-m)
\end{gathered}
$$

Consequently (compare p. 143), $X_1f\cdots X_nf$ permutes the $\infty^{n-m}$ $m$-dimensional manifolds

$$
u_1=\mathrm{const.},\quad\cdots,\quad u_{n-m}=\mathrm{const.}
$$

We have obtained

**Proposition 6.** *Every simply transitive group $X_1f\cdots X_nf$ in $n>1$ variables $x_1\cdots x_n$ is imprimitive. If $Z_1f\cdots Z_nf$ is its reciprocal group and $Z_1f\cdots Z_mf$ is any subgroup with invariants $u_1\cdots u_{n-m}$, the $m$-term complete system $Z_1f=0$, $\cdots$, $Z_mf=0$ admits $X_1f\cdots X_nf$, which permutes the $\infty^{n-m}$ $m$-dimensional manifolds $u_1=\mathrm{const.}$, $\cdots$, $u_{n-m}=\mathrm{const.}$.*

This proposition shows that every $m$-parameter subgroup of $Z_1f\cdots Z_nf$ gives a definite decomposition of $x_1\cdots x_n$ into $\infty^{n-m}$ $m$-dimensional manifolds invariant under $X_1f\cdots X_nf$. Determining all subgroups of $Z_1f\cdots Z_nf$ and calculating their invariants therefore gives infinitely many invariant decompositions for $X_1f\cdots X_nf$. One can show that this finds all invariant decompositions, so Proposition 6 has a converse.

Let $Y_1f=0$, $\cdots$, $Y_mf=0$ be any $m$-term complete system admitting $X_1f\cdots X_nf$, and let $u_1\cdots u_{n-m}$ be independent solutions. The family of $\infty^{n-m}$ $m$-dimensional manifolds

$$
u_1=\mathrm{const.},\quad\cdots,\quad u_{n-m}=\mathrm{const.}
$$

then gives an invariant decomposition of $x_1\cdots x_n$ under $X_1f\cdots X_nf$. We claim that $Z_1f\cdots Z_nf$ contains a definite $m$-parameter subgroup leaving each of these $\infty^{n-m}$ manifolds fixed. This is the converse of Proposition 6.

First introduce into the reciprocal groups the functions $u_1\cdots u_{n-m}$, together with any $m$ functions $v_1\cdots v_m$ of the $x$ independent of one another and of the former, as variables. Then

$$
\begin{gathered}
X_kf=\sum_1^{n-m}{}^{\nu}\omega_{k\nu}(u_1\cdots u_{n-m})
\frac{\partial f}{\partial u_\nu}\\
+\sum_1^m{}^{\mu} X_kv_\mu\frac{\partial f}{\partial v_\mu}
\\
(k=1\cdots n)
\end{gathered}
$$

and

$$
\begin{gathered}
Z_kf=\sum_1^{n-m}{}^{\nu}Z_ku_\nu\frac{\partial f}{\partial u_\nu}\\
+\sum_1^m{}^{\mu} Z_kv_\mu\frac{\partial f}{\partial v_\mu}
\\
(k=1\cdots n),
\end{gathered}
$$

Here $X_kv_\mu$, $Z_ku_\nu$ and $Z_kv_\mu$ are functions of $u$ and $v$. Our claim plainly amounts to saying that exactly $m$ independent infinitesimal transformations can be obtained as linear combinations of $Z_1f\cdots Z_nf$ without transforming $u_1\cdots u_{n-m}$ at all; that is, all coefficients of $\frac{\partial f}{\partial u_1}\cdots\frac{\partial f}{\partial u_{n-m}}$ vanish.

To prove this, we must calculate the coefficients of $\frac{\partial f}{\partial u_1}\cdots\frac{\partial f}{\partial u_{n-m}}$ in the general infinitesimal transformation $Zf=e_1Z_1f+\cdots+e_nZ_nf$ of $Z_1f\cdots Z_nf$.

The transformation $Zf$ is fully defined by

$$
\begin{gathered}
X_1(Z(f))-Z(X_1(f))=0,\\
\cdots,\\

X_n(Z(f))-Z(X_n(f))=0
\end{gathered}
$$

Replacing $f$ by $u_\nu$ gives

$$
\begin{gathered}
X_1(Zu_\nu)-Z\omega_{1\nu}=0,\\
\cdots,\\

X_n(Zu_\nu)-Z\omega_{n\nu}=0
\\
(\nu=1\cdots n-m).
\end{gathered}
$$

Hence $Zu_1\cdots Zu_{n-m}$ are solutions of

$$
\begin{gathered}
X_k\rho_\nu-\sum_1^{n-m}{}^{\mu}
\frac{\partial\omega_{k\nu}}{\partial u_\mu}\rho_\mu=0
\\
(k=1\cdots n;\ \nu=1\cdots n-m),
\end{gathered}\tag{7}
$$

where $\rho_1\cdots\rho_{n-m}$ are the unknown functions.

If

$$
\begin{gathered}
\rho_1=\psi_1(u_1\cdots u_{n-m},v_1\cdots v_m),\\
\cdots,\\

\rho_{n-m}=\psi_{n-m}(u_1\cdots u_{n-m},v_1\cdots v_m)
\end{gathered}\tag{8}
$$

is any solution system of (7), the $n(n-m)$ expressions

$$
X_k\psi_\nu-\sum_1^{n-m}{}^{\mu}
\frac{\partial\omega_{k\nu}}{\partial u_\mu}\rho_\mu
$$

vanish identically after the substitution $\rho_1=\psi_1$, $\cdots$, $\rho_{n-m}=\psi_{n-m}$. Regard (8) as a system in the $n+n-m$ variables $u_1\cdots u_{n-m}$, $v_1\cdots v_m$, $\rho_1\cdots\rho_{n-m}$. It immediately follows that this system admits the $n$ infinitesimal transformations

$$
\begin{gathered}
U_kf=X_kf\\
+\sum_1^{n-m}{}^{\nu}
\bigl\{\sum_1^{n-m}{}^{\mu}
\frac{\partial\omega_{k\nu}}{\partial u_\mu}\rho_\mu\bigr\}
\frac{\partial f}{\partial\rho_\nu}
\\
(k=1\cdots n)
\end{gathered}\tag{9}
$$

Conversely, a system of the form (8) admitting $U_1f\cdots U_nf$ gives a solution system of (7): its functions $\psi_1\cdots\psi_{n-m}$ form such a system.

Thus determining the most general solution system of (7) amounts to determining the most general system (8), in the $2n-m$ variables $u$, $v$, $\rho$, that admits $U_1f\cdots U_nf$.

Every system admitting $U_1f\cdots U_nf$ also admits all infinitesimal transformations $(U_iU_k)$. Calculation gives

$$
\begin{gathered}
(U_iU_k)={}(X_iX_k)\\
+\sum_{\mu\nu\pi}^{1\cdots n-m}
\bigl(\omega_{i\pi}\frac{\partial^2\omega_{k\nu}}{\partial u_\mu\partial u_\pi}\\
-\omega_{k\pi}\frac{\partial^2\omega_{i\nu}}{\partial u_\mu\partial u_\pi}\bigr)\\
\rho_\mu\frac{\partial f}{\partial\rho_\nu}\\
+\sum_{\mu\nu\pi}^{1\cdots n-m}
\bigl(\frac{\partial\omega_{i\nu}}{\partial u_\mu}
\frac{\partial\omega_{k\pi}}{\partial u_\nu}\\
-\frac{\partial\omega_{k\nu}}{\partial u_\mu}
\frac{\partial\omega_{i\pi}}{\partial u_\nu}\bigr)\\
\rho_\mu\frac{\partial f}{\partial\rho_\pi},
\end{gathered}
$$

or, equivalently,

$$
\begin{gathered}
(U_iU_k)=(X_iX_k)\\
+\sum_{\mu\nu}^{1\cdots n-m}
\frac{\partial}{\partial u_\mu}(X_i\omega_{k\nu}-X_k\omega_{i\nu})
\cdot\rho_\mu\frac{\partial f}{\partial\rho_\nu}.
\end{gathered}
$$

Since $X_1f\cdots X_nf$ generates a group, there are relations of the form

$$
\begin{gathered}
(X_iX_k)=X_i(X_k(f))-X_k(X_i(f))\\
=\sum_1^n{}^{\sigma} c_{ik\sigma}X_\sigma f,
\end{gathered}
$$

In particular,

$$
\begin{gathered}
X_i(X_ku_\nu)-X_k(X_iu_\nu)\\
=X_i\omega_{k\nu}-X_k\omega_{i\nu}\\
=\sum_1^n{}^{\sigma} c_{ik\sigma}\omega_{\sigma\nu}
\end{gathered}
$$

so

$$
(U_iU_k)=\sum_1^n{}^{\sigma} c_{ik\sigma}U_\sigma f.
$$

Consequently, $U_1f\cdots U_nf$ generates an $n$-parameter group in the $2n-m$ variables $u_1\cdots u_{n-m}$, $v_1\cdots v_m$, $\rho_1\cdots\rho_{n-m}$.

We must now determine the most general system of the form (8) admitting $U_1f\cdots U_nf$. Since $X_1f\cdots X_nf$ satisfies no linear relation, not all $n$-rowed determinants of the matrix belonging to $U_1f\cdots U_nf$ vanish identically; nor can a system of the form (8) make them all vanish. Chapter 14, Theorem 42, p. 237, therefore shows that every system (8) admitting $U_1f\cdots U_nf$ is represented by relations among solutions of the $n$-term complete system $U_1f=0$, $\cdots$, $U_nf=0$.

This complete system has exactly $n-m$ independent solutions, say

$$
\begin{gathered}
\Psi_\mu(u_1\cdots u_{n-m},v_1\cdots v_m,\rho_1\cdots\rho_{n-m})
\\
(k=1\cdots n-m)
\end{gathered}
$$

The functions $\Psi_1\cdots\Psi_{n-m}$ are independent with respect to $\rho_1\cdots\rho_{n-m}$, because the complete system can be solved for the derivatives $\frac{\partial f}{\partial u_1}\cdots\frac{\partial f}{\partial u_{n-m}}$, $\frac{\partial f}{\partial v_1}\cdots\frac{\partial f}{\partial v_m}$ (compare Chapter 5, Theorem 12, p. 91). We conclude that the most general system (8) admitting $U_1f\cdots U_nf$ can take the form

$$
\Psi_1=C_1,\quad\cdots,\quad\Psi_{n-m}=C_{n-m}
$$

where $C_1\cdots C_{n-m}$ are arbitrary constants.

Solving the system just found for $\rho_1\cdots\rho_{n-m}$, which is certainly possible, gives the most general solution system of (7). It therefore contains exactly $n-m$ essential arbitrary constants. Since (7) is linear and homogeneous in the unknowns $\rho_1\cdots\rho_{n-m}$, its most general solution system must be expressible as

$$
\begin{gathered}
\rho_\mu=C'_1\psi_\mu^{(1)}+C'_2\psi_\mu^{(2)}\\
+\cdots+C'_{n-m}\psi_\mu^{(n-m)}
\\
(\mu=1\cdots n-m),
\end{gathered}\tag{10}
$$

where the $n-m$ function systems

$$
\begin{gathered}
\psi_1^{(\nu)},\\
\psi_2^{(\nu)},\\
\cdots,\\
\psi_{n-m}^{(\nu)}
\\
(\nu=1\cdots n-m)
\end{gathered}
$$

are linearly independent solution systems of (7), free of arbitrary constants, and the $C'$ are arbitrary constants. The determinant of the $\psi$ naturally does not vanish, since equations (10) must be solvable for $C'_1\cdots C'_{n-m}$.

By p. 384, the functions $Zu_1\cdots Zu_{n-m}$ solve equations (7), so they have the form

$$
\begin{gathered}
Zu_\mu=\overline C_1\psi_\mu^{(1)}+\cdots+
\overline C_{n-m}\psi_\mu^{(n-m)}
\\
(\mu=1\cdots n-m).
\end{gathered}
$$

Here the $\overline C_\nu$ are constants about which we know nothing further for the moment; it is still conceivable that they satisfy linear relations.

The values of $Zu_\mu$ give the following representation of the general infinitesimal transformation $Zf$ of $Z_1f\cdots Z_nf$:

$$
Zf=\sum_{\mu\nu}^{1\cdots n-m}\overline C_\mu\psi_\nu^{(\mu)}
\frac{\partial f}{\partial u_\nu}
+\sum_1^m{}^{\mu} Zv_\mu\frac{\partial f}{\partial v_\mu}.
$$

Since the $n-m$ expressions

$$
\sum_1^{n-m}{}^{\nu}\psi_\nu^{(\mu)}\frac{\partial f}{\partial u_\nu}
\qquad(\mu=1\cdots n-m)
$$

are independent infinitesimal transformations, at least $m$, say exactly $m+\varepsilon$, independent infinitesimal transformations can plainly be obtained as linear combinations of $Z_1f\cdots Z_nf$ in which the coefficients of $\frac{\partial f}{\partial u_1}\cdots\frac{\partial f}{\partial u_{n-m}}$ are zero. These $m+\varepsilon$ transformations naturally generate an $(m+\varepsilon)$-parameter subgroup of $Z_1f\cdots Z_nf$ leaving each of the $\infty^{n-m}$ $m$-dimensional manifolds $u_1=\mathrm{const.}$, $\cdots$, $u_{n-m}=\mathrm{const.}$ fixed. This is possible only if the integer $\varepsilon$ is zero: if $\varepsilon>0$, the group $Z_1f\cdots Z_nf$ could not be simply transitive.

The claim made on p. 383 is now proved, and we can state

**Proposition 7.** *Let $X_1f\cdots X_nf$ and $Z_1f\cdots Z_nf$ be reciprocal simply transitive groups in the $n$ variables $x_1\cdots x_n$. If*

$$
\begin{gathered}
u_1(x_1\cdots x_n)=\mathrm{const.},\\
\cdots,\\

u_{n-m}(x_1\cdots x_n)=\mathrm{const.}
\end{gathered}
$$

*is any decomposition of $x_1\cdots x_n$ into $\infty^{n-m}$ $m$-dimensional manifolds invariant under $X_1f\cdots X_nf$, then $Z_1f\cdots Z_nf$ always contains an $m$-parameter subgroup leaving each of these $\infty^{n-m}$ manifolds fixed.*

Combining this with Proposition 6, p. 383, gives

**Theorem 69.** *If the $n$-parameter group $X_1f\cdots X_nf$ in $n$ variables $x_1\cdots x_n$ is simply transitive, all $m$-term complete systems admitting it, or equivalently all invariant decompositions of $x_1\cdots x_n$ into $\infty^{n-m}$ $m$-dimensional manifolds, are obtained as follows. First determine the reciprocal simply transitive group $Z_1f\cdots Z_nf$ of $X_1f\cdots X_nf$, and find all its $m$-parameter subgroups. If*

$$
\begin{gathered}
Z_\mu f=g_{\mu1}Z_1f+\cdots+g_{\mu n}Z_nf
\\
(\mu=1\cdots m)
\end{gathered}
$$

*is one of them, then $Z_1f=0$, $\cdots$, $Z_mf=0$ is one of the required complete systems and determines an invariant decomposition of $x_1\cdots x_n$ under $X_1f\cdots X_nf$ into $\infty^{n-m}$ $m$-dimensional manifolds. Forming the $m$-term complete system supplied by each subgroup gives all $m$-term complete systems admitting $X_1f\cdots X_nf$. Carrying out this investigation for every $m=1,2\cdots n-1$ gives all complete systems admitting $X_1f\cdots X_nf$, and hence all its invariant decompositions of $x_1\cdots x_n$.*

This theorem solves the problem of finding every way in which a given *simply transitive* group is imprimitive.

Suppose again that the equations

$$
u_1=\mathrm{const.},\quad\cdots,\quad u_{n-m}=\mathrm{const.}
$$

give any invariant decomposition of $x_1\cdots x_n$ under $X_1f\cdots X_nf$ into $\infty^{n-m}$ $m$-dimensional manifolds. Introducing $u_1\cdots u_{n-m}$ together with $m$ suitable functions $v_1\cdots v_m$ as new variables gives $X_1f\cdots X_nf$ the form

$$
\begin{gathered}
X_kf=\sum_1^{n-m}{}^{\nu}\omega_{k\nu}(u_1\cdots u_{n-m})
\frac{\partial f}{\partial v_\nu}\\
+\sum_1^m{}^{\mu}\overline\xi_{k\mu}(u_1\cdots u_{n-m},v_1\cdots v_m)
\frac{\partial f}{\partial v_\mu}.
\end{gathered}
$$

Not all $(n-m)$-rowed determinants of the matrix

$$
\left|\begin{array}{ccc}
\omega_{11}&\cdot&\omega_{1,n-m}\\
\cdot&\cdot&\cdot\\
\cdot&\cdot&\cdot\\
\omega_{n1}&\cdot&\omega_{n,n-m}
\end{array}\right|
$$

can vanish identically; otherwise $X_1f\cdots X_nf$ would satisfy a linear relation, contrary to the assumption. Thus, if $u_1^0\cdots u_{n-m}^0$ is a general system of values, Chapter 13, p. 222, shows that $X_1f\cdots X_nf$ contains exactly $\infty^{m-1}$ distinct infinitesimal transformations leaving

$$
u_1=u_1^0,\quad\cdots,\quad u_{n-m}=u_{n-m}^0
$$

invariant. They naturally generate an $m$-parameter subgroup, the most general subgroup of $X_1f\cdots X_nf$ leaving the $m$-dimensional manifold $u_1=u_1^0$, $\cdots$, $u_{n-m}=u_{n-m}^0$, or briefly $M$, fixed.

The $m$-dimensional manifold $M$ also admits $m$ independent infinitesimal transformations of the reciprocal group $Z_1f\cdots Z_nf$. By Proposition 7, p. 387, that group contains an $m$-parameter subgroup leaving each of the $\infty^{n-m}$ manifolds

$$
u_1=\mathrm{const.},\quad\cdots,\quad u_{n-m}=\mathrm{const.}
$$

fixed. It is also clear that $M$ cannot admit a larger subgroup of $Z_1f\cdots Z_nf$, since $u_1^0\cdots u_{n-m}^0$ is assumed to be a general system of values.

Thus $M$ admits exactly $m$ independent infinitesimal transformations from each reciprocal group, $X_1f\cdots X_nf$ and $Z_1f\cdots Z_nf$, and hence a definite $m$-parameter subgroup of each.

We can make these two $m$-parameter subgroups explicit by choosing any system of values $v_1^0\cdots v_m^0$ in general position and expanding the infinitesimal transformations of the reciprocal groups in powers of $u_1-u_1^0$, $\cdots$, $u_{n-m}-u_{n-m}^0$, $v_1-v_1^0$, $\cdots$, $v_m-v_m^0$. Omitting terms of first and higher order, we can, as on p. 379, replace $X_1f\cdots X_nf$ by $n$ independent transformations of the form

$$
\begin{gathered}
\mathfrak X_1f=\frac{\partial f}{\partial u_1}+\cdots,\\
\cdots,\\

\mathfrak X_{n-m}f=\frac{\partial f}{\partial u_{n-m}}+\cdots,
\end{gathered}
$$

$$
\begin{gathered}
\mathfrak X_{n-m+1}f=\frac{\partial f}{\partial v_1}+\cdots,\\
\cdots,\\

\mathfrak X_nf=\frac{\partial f}{\partial v_m}+\cdots
\end{gathered}
$$

and $Z_1f\cdots Z_nf$ by $n$ of the form

$$
\begin{gathered}
\mathfrak Z_1f=-\frac{\partial f}{\partial u_1}+\cdots,\\
\cdots,\\

\mathfrak Z_{n-m}f=-\frac{\partial f}{\partial u_{n-m}}+\cdots,
\end{gathered}
$$

$$
\begin{gathered}
\mathfrak Z_{n-m+1}f=-\frac{\partial f}{\partial v_1}+\cdots,\\
\cdots,\\

\mathfrak Z_nf=-\frac{\partial f}{\partial v_m}+\cdots.
\end{gathered}
$$

The independent transformations $\mathfrak X_{n-m+1}f\cdots\mathfrak X_nf$ plainly preserve the manifold $u_1=u_1^0$, $\cdots$, $u_{n-m}=u_{n-m}^0$, and the independent transformations $\mathfrak Z_{n-m+1}f\cdots\mathfrak Z_nf$ do the same. Thus $\mathfrak X_{n-m+1}f\cdots\mathfrak X_nf$ and $\mathfrak Z_{n-m+1}f\cdots\mathfrak Z_nf$ are the two $m$-parameter subgroups just discussed.

This representation of the subgroups gives some noteworthy conclusions.

There are relations of the form

$$
(\mathfrak X_i\mathfrak X_k)=\sum_1^n{}^{\nu} c_{ik\nu}\mathfrak X_\nu f
$$

among $\mathfrak X_1f\cdots\mathfrak X_nf$. By pp. 379 ff., the same relations

$$
(\mathfrak Z_i\mathfrak Z_k)=\sum_1^n{}^{\nu} c_{ik\nu}\mathfrak Z_\nu f
$$

hold among $\mathfrak Z_1f\cdots\mathfrak Z_nf$, with the same constants $c_{ik\nu}$. Hence the subgroups $\mathfrak X_{n-m+1}f\cdots\mathfrak X_nf$ and $\mathfrak Z_{n-m+1}f\cdots\mathfrak Z_nf$ have the same composition. More follows. The groups $X_1f\cdots X_nf$ and $Z_1f\cdots Z_nf$ are in holoedric isomorphism when each infinitesimal transformation $e_1\mathfrak X_1f+\cdots+e_r\mathfrak X_rf$ is assigned $e_1\mathfrak Z_1f+\cdots+e_r\mathfrak Z_rf$. This assignment plainly sends $\mathfrak X_{n-m+1}f\cdots\mathfrak X_rf$ to $\mathfrak Z_{n-m+1}f\cdots\mathfrak Z_rf$. Thus the reciprocal groups can be placed in holoedric isomorphism so that their $m$-parameter subgroups preserving $M$ correspond.

Summarizing pp. 388 ff. gives

**Proposition 8.** *If an $m$-dimensional manifold in $x_1\cdots x_n$ admits exactly $m$ independent infinitesimal transformations, and hence an $m$-parameter subgroup, of a simply transitive group $X_1f\cdots X_nf$, it also admits exactly $m$ independent infinitesimal transformations, and hence an $m$-parameter subgroup, of the simply transitive group $Z_1f\cdots Z_nf$ reciprocal to $X_1f\cdots X_nf$. The two $m$-parameter subgroups so defined have the same composition. The reciprocal simply transitive groups can be placed in holoedric isomorphism so that these $m$-parameter subgroups correspond.*

### English translation of the original footnotes for §§95–97

**F1 · p. 377, after Theorem 67.** Lie indicated this general theorem in [*Math. Ann.*, vol. XXV](https://gdz.sub.uni-goettingen.de/download/pdf/PPN235181684_0025/PPN235181684_0025.pdf).

**F2 · p. 380, after Theorem 68.** Lie communicated Theorem 68 to the Society of Sciences in Christiania in November 1882 and May 1883; see also [*Math. Annalen*, vol. XXV](https://gdz.sub.uni-goettingen.de/download/pdf/PPN235181684_0025/PPN235181684_0025.pdf), pp. 107 ff.
