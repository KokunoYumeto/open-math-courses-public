# The third fundamental theorem

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI, GPT-6.1 Sol (OpenAI), in Codex at Ultra. Public domain (CC0).*

The first two theorems begin with transformations or vector fields. The third begins with an abstract vector space and a bracket. Antisymmetry and Jacobi are the only algebraic conditions needed for a local analytic group. We first explain why changing a basis changes the constants but preserves the algebra. The adjoint representation proves existence when the centre is zero, and two linear constructions show what a centre can change. A construction with differential forms then handles every centre.

We use the constant-frame construction and uniqueness theorem in The second fundamental theorem and the group of parameters, and the analytic inverse theorem proved in Transformation groups and their parameters, Theorem A. Section 3 prepares the differentiation of forms before giving the full radial Maurer–Cartan calculation. Section 6 develops Lie's function-group route separately, using straightening in One-parameter groups, Theorem 3.1, and the complete-system theorem in Complete systems and differential invariants, Theorem 2.1. Basic historical references are [Lie–Engel I–III] and [Merker].

## 1. The algebraic conditions

A finite-dimensional Lie algebra over $\mathbb K$ is a vector space $\mathfrak g$ with a bilinear bracket satisfying

$$
[u,v]=-[v,u],\qquad
[[u,v],w]+[[v,w],u]+[[w,u],v]=0.
\tag{1.1}
$$

In a basis $e_1,\ldots,e_r$, write $[e_i,e_j]=\sum_kc_{ij}^ke_k$.

**Proposition 1.1.** The structure constants of an effective local transformation group satisfy

$$
c_{ij}^k=-c_{ji}^k,\qquad
\sum_m(c_{ij}^mc_{mk}^s+c_{jk}^mc_{mi}^s+c_{ki}^mc_{mj}^s)=0.
\tag{1.2}
$$

**Proof.** Vector-field commutators are antisymmetric. Their Jacobi identity follows by expanding the six triple compositions of differential operators; each occurs once with each sign. Insert the constant bracket relations into these identities and use independence of the generators over constants to equate coefficients. $\square$

Jacobi also says that $\operatorname{ad}_u(v)=[u,v]$ is a derivation and that

$$
[\operatorname{ad}_u,\operatorname{ad}_v]=\operatorname{ad}_{[u,v]}.
\tag{1.3}
$$

The centre is $Z(\mathfrak g)=\{u:[u,v]=0\text{ for all }v\}$, exactly the kernel of $\operatorname{ad}$.

### Changing the basis and classifying composition

Lie calls the bracket structure, up to an invertible constant change of generators, the group's *composition*. This description permits actions on spaces of different dimensions. It concerns their Lie algebras, and therefore their local parameter groups by the preceding lesson's uniqueness theorem.

Let $H=(h_{ij})$ be invertible and put $f_i=\sum_jh_{ij}e_j$. Write $c'{}_{ik}^{\rho}$ for the constants in this new basis. Expanding the bracket in the old basis gives

$$
\sum_{\rho=1}^r c'{}_{ik}^{\rho}h_{\rho s}
=\sum_{j,\pi=1}^rh_{ij}h_{k\pi}c_{j\pi}^{s}.
\tag{1.4}
$$

Consequently,

$$
c'{}_{ik}^{\rho}
=\sum_{j,\pi,s=1}^r
h_{ij}h_{k\pi}c_{j\pi}^{s}(H^{-1})_{s\rho}.
\tag{1.5}
$$

The last inverse index is essential. If $D=\det H$, it is
$(H^{-1})_{s\rho}=D^{-1}\partial D/\partial h_{\rho s}$.

**Proposition 1.2 (basis changes).** Formula (1.5) acts on every bilinear coefficient array, preserves antisymmetry and Jacobi, and has the composition rule

$$
T_K(T_H(c))=T_{KH}(c).
\tag{1.6}
$$

Two Lie algebra structures on an $r$-dimensional vector space are isomorphic exactly when their arrays belong to the same orbit of these changes.

**Proof.** For an arbitrary bilinear operation $\mu$ on the fixed space $V$, define the invertible linear map $A_H$ by $A_H(e_i)=\sum_jh_{ij}e_j$. The transformed operation is

$$
\mu_H(u,v)=A_H^{-1}\mu(A_Hu,A_Hv).
$$

Its coefficients are (1.5). Antisymmetry is preserved by this formula. For the Jacobi expression
$J_\mu(u,v,w)=\mu(\mu(u,v),w)+\mu(\mu(v,w),u)+\mu(\mu(w,u),v)$,
direct substitution gives

$$
J_{\mu_H}(u,v,w)
=A_H^{-1}J_\mu(A_Hu,A_Hv,A_Hw).
$$

Thus Jacobi is preserved, without assuming that $\mu$ has already been realized by transformations. Applying a second basis change $K$ replaces the basis by
$g_i=\sum_jk_{ij}f_j=\sum_s(KH)_{is}e_s$. This proves (1.6), and the identity and inverse changes follow by taking $I$ and $H^{-1}$. Finally, $\mu_H=\nu$ means that $A_H$ is a bracket-preserving isomorphism from $(V,\nu)$ to $(V,\mu)$. Conversely, the matrix of any such isomorphism gives this identity and hence the change (1.5). $\square$

The skew and Jacobi equations define an algebraic subset $\mathcal J_r$ of the space $\mathbb K^{r^3}$ of all arrays. It can have singularities; calling it a variety does not make it a regular manifold. Its basis-change orbits are the isomorphism classes. For two given arrays $c,d$, the precise algebraic orbit question asks whether

$$
\sum_\rho d_{ik}^{\rho}h_{\rho s}
=\sum_{j,\pi}h_{ij}h_{k\pi}c_{j\pi}^{s},
\qquad t\det H=1
\tag{1.7}
$$

has a solution over $\mathbb K$. The extra scalar $t$ enforces invertibility. This formulation is an algebraic criterion; it does not produce a finite list of all classes in every dimension or a regular quotient manifold.

## 2. A realization when the centre is zero

For $u\in\mathfrak g$, define a linear vector field on the underlying vector space by

$$
E_u(a)=-[u,a].
\tag{2.1}
$$

The minus sign is needed with our vector-field bracket. For matrix fields $X_A(a)=Aa$, the coefficient formula gives $X_A,X_B=(BA-AB)a$, so the passage from matrices to these fields reverses the commutator.

**Proposition 2.1.** The map $u\mapsto E_u$ preserves brackets and has kernel $Z(\mathfrak g)$. If the centre is zero, these fields give a faithful realization and generate an $r$-parameter local group.

**Proof.** Using (1.3) and the matrix-field calculation,

$$
[E_u,E_v]=X_{-[\operatorname{ad}_u,\operatorname{ad}_v]}
=X_{-\operatorname{ad}_{[u,v]}}=E_{[u,v]}.
$$

The field $E_u$ is identically zero precisely when $\operatorname{ad}_u=0$, proving the kernel statement. If the centre is zero, a constant relation among basis fields would give an element in this kernel, so they are independent over constants. The converse second theorem then constructs the group. $\square$

Every field in (2.1) vanishes at $a=0$. Their independence is independence as fields, not pointwise independence there. If the centre is nonzero, this construction realizes only $\mathfrak g/Z(\mathfrak g)$ and cannot prove the general theorem.

**Example 2.2.** For $[h,e]=e$, write $a=sh+te$. Formula (2.1) gives $E_h=-t\partial_t$ and $E_e=s\partial_t$, with $[E_h,E_e]=E_e$. They are independent over constants even though they are pointwise collinear. For $\mathfrak{sl}_2$ with basis $h,e,f$ and brackets $[h,e]=2e$, $[h,f]=-2f$, $[e,f]=h$, a central element $ah+be+cf$ must have $b=c=0$ from its bracket with $h$, and then $a=0$ from its bracket with $e$. Thus (2.1) realizes all three dimensions.

### A centre that splits off as a direct summand

**Proposition 2.3 (the split-centre construction).** Suppose
$\mathfrak g=\mathfrak h\oplus Z(\mathfrak g)$ as vector spaces and $\mathfrak h$ is a subalgebra. Then $\mathfrak g$ has a faithful realization by linear vector fields.

**Proof.** Both summands are ideals: the central one by definition, and $\mathfrak h$ because $[\mathfrak g,\mathfrak h]=[\mathfrak h,\mathfrak h]\subset\mathfrak h$. An element central in $\mathfrak h$ commutes with both summands, so it lies in $\mathfrak h\cap Z(\mathfrak g)=0$. Thus $\mathfrak h$ is centreless.

Choose a basis $z_1,\ldots,z_q$ of the central summand and use coordinates $(a,b_1,\ldots,b_q)$ on $\mathfrak h\times\mathbb K^q$. For $u\in\mathfrak h$ and $z=\sum_\alpha\lambda_\alpha z_\alpha$, set

$$
\rho(u+z)=-[u,a]\cdot\partial_a
+\sum_{\alpha=1}^q\lambda_\alpha b_\alpha\partial_{b_\alpha}.
\tag{2.2}
$$

The first fields preserve brackets by Proposition 2.1. The central dilations commute with one another and with those fields, since they act on separate coordinates. This proves bracket preservation for $\rho$. If $\rho(u+z)$ is identically zero, its $\partial_{b_\alpha}$ coefficients force every $\lambda_\alpha=0$. Its remaining coefficient says that $u$ is central in $\mathfrak h$, hence zero. The realization is faithful. Its independent generators integrate by the converse second theorem. $\square$

A vector-space complement to the centre is not enough: it must be a subalgebra. In a basis whose last $q$ elements span the centre, this condition says that brackets of the other basis elements have no central component. The Heisenberg algebra fails this condition, but still admits a faithful linear realization.

**Example 2.4 (Lie's linear Heisenberg realization).** On $\mathbb K^3$ with coordinates $a_1,a_2,a_3$, put

$$
L_1=a_3\partial_{a_1},\qquad
L_2=a_1\partial_{a_2},\qquad
L_3=a_3\partial_{a_2}.
\tag{2.3}
$$

The coefficient formula for a bracket gives
$[L_1,L_2]=L_3$ and $[L_1,L_3]=[L_2,L_3]=0$. In a constant relation
$\lambda_1L_1+\lambda_2L_2+\lambda_3L_3=0$, the $\partial_{a_1}$ coefficient is $\lambda_1a_3$, and the $\partial_{a_2}$ coefficient is $\lambda_2a_1+\lambda_3a_3$. Varying $a_1,a_3$ forces all three constants to vanish. Thus the map from the Heisenberg basis to these fields is faithful, although all three fields vanish at the origin.

The flows are the linear shears

$$
\begin{aligned}
\Phi_1^\tau(a)&=(a_1+\tau a_3,a_2,a_3),\\
\Phi_2^\tau(a)&=(a_1,a_2+\tau a_1,a_3),\\
\Phi_3^\tau(a)&=(a_1,a_2+\tau a_3,a_3).
\end{aligned}
$$

This example retains the central generator that the adjoint representation loses. Neither this example nor Proposition 2.3 proves a faithful finite-dimensional linear realization for every Lie algebra. The general local existence proof below constructs a coframe directly.

## 3. A form defined by an entire power series

### Differentiating forms

An exterior form is an alternating covariant tensor, written in coordinates as a sum of $f_I\,dx^{i_1}\wedge\cdots\wedge dx^{i_p}$. The exterior derivative is
$d(f_I\,dx^I)=df_I\wedge dx^I$. Its graded product rule, $d^2=0$, and commutation with pullback are proved in the programme's [*Smooth Manifolds and Differential Geometry*, complete English reader, 1 September 2026](https://github.com/KokunoYumeto/brenner-differentialgeometrie-en/releases/download/v2026.09.01-complete/smooth-manifolds-differential-geometry-complete-en.pdf), Definitions 14.1 and 14.6 and Theorem 20.4, PDF pp. 193–199 and 272–276. That reader, based on Holger Brenner's course, is published under CC BY-SA 4.0. We use those definitions and independently prove the flow identities needed here.

For a field $X$, contraction means
$(\iota_X\alpha)(v_1,\ldots,v_{p-1})=\alpha(X,v_1,\ldots,v_{p-1})$.
Alternation gives
$\iota_X(\alpha\wedge\beta)=(\iota_X\alpha)\wedge\beta+(-1)^p\alpha\wedge\iota_X\beta$ when $\alpha$ has degree $p$.
Define $\mathcal L_X\alpha=\left.\frac{d}{dt}\right|_0(\Phi_X^t)^*\alpha$ using the analytic flow of lesson 3.

**Lemma (Cartan differentiation).** For every exterior form,

$$
\mathcal L_X=d\iota_X+\iota_Xd,\qquad
\mathcal L_Xd=d\mathcal L_X,\qquad
[\mathcal L_X,\mathcal L_Y]=\mathcal L_{[X,Y]}.
$$

For a one-form $\eta$ and fields $U,V$, moreover,

$$
d\eta(U,V)=U(\eta(V))-V(\eta(U))-\eta([U,V]).
$$

**Proof.** Differentiating the pullback of a product shows that $\mathcal L_X$ is a derivation of degree zero. On functions it is $Xf$. On the coordinate one-forms it is
$\mathcal L_Xdx^j=dX^j$, since pullback commutes with $d$ and the derivative of the flow's $j$th component at zero is $X^j$. The graded product rules for $d$ and $\iota_X$ show, by cancellation of the two middle terms, that $d\iota_X+\iota_Xd$ is also a derivation of degree zero. It takes the same values $Xf$ and $dX^j$ on functions and coordinate one-forms. Every form is generated by these, which proves the first formula.

The equality $d^2=0$ now gives commutation with $d$. A commutator of degree-zero derivations is a derivation. On functions, $[\mathcal L_X,\mathcal L_Y]f=[X,Y]f$; on $dx^j$, commutation with $d$ gives $d([X,Y]x^j)$. Thus this commutator agrees with $\mathcal L_{[X,Y]}$ on the same generators and hence on every form.

Finally write $\eta=\sum_j a_j\,dx^j$. Expanding the right-hand side of the last formula cancels the terms differentiating the components of $U,V$ and leaves
$\sum_{i,j}(\partial_i a_j)(U^iV^j-V^iU^j)$, which is exactly $d\eta(U,V)$. All these arguments apply componentwise to vector-valued forms. $\square$

For $\mathfrak g$-valued forms $\alpha=\sum_a e_a\alpha^a$ and $\beta=\sum_b e_b\beta^b$, use the exterior bracket

$$
[\alpha,\beta]=\sum_{a,b}[e_a,e_b]\,\alpha^a\wedge\beta^b.
$$

If their degrees are $p,q$, alternation gives
$[\beta,\alpha]=-(-1)^{pq}[\alpha,\beta]$, and the exterior product rule gives
$d[\alpha,\beta]=[d\alpha,\beta]+(-1)^p[\alpha,d\beta]$.
In particular $\omega,\omega=2[\omega(u),\omega(v)]$ for a one-form $\omega$. These conventions fix the signs in the following calculation.

### The analytic coframe

Identify $T_a\mathfrak g$ with $\mathfrak g$. Define

$$
\omega_a(v)=\int_0^1e^{-t\operatorname{ad}_a}v\,dt
=\sum_{k=0}^\infty\frac{(-1)^k}{(k+1)!}(\operatorname{ad}_a)^kv.
\tag{3.1}
$$

This is the meaning of $((1-e^{-\operatorname{ad}_a})/\operatorname{ad}_a)\,da$. No inverse of $\operatorname{ad}_a$ is taken. In particular, the expression remains meaningful when the centre is nonzero or the adjoint map is nilpotent.

Choose a norm on $\mathfrak g$. Bilinearity gives $\|\operatorname{ad}_a\|\le C\|a\|$. The series in (3.1) converges absolutely and locally uniformly, with all derivatives, by the exponential majorant. Hence $\omega$ is analytic. Since $\omega_0=I$, it is an invertible coframe near zero.

For a $\mathfrak g$-valued one-form, our convention is

$$
\omega,\omega=2[\omega(u),\omega(v)].
$$

**Theorem 3.1 (Maurer–Cartan equation).** The form (3.1) satisfies

$$
d\omega+\tfrac12[\omega,\omega]=0.
\tag{3.2}
$$

**Proof.** Write $R_a=a$ for the radial vector field and $K=d\omega+\frac12[\omega,\omega]$. Since $\operatorname{ad}_a(a)=0$, we have $\omega(R)=a$. Also, for a constant vector $v$,

$$
t\omega_{ta}(v)=\int_0^t e^{-s\operatorname{ad}_a}v\,ds.
$$

Differentiating at $t=1$ shows

$$
(\mathcal L_R\omega)_a(v)=e^{-\operatorname{ad}_a}v.
$$

Cartan's formula $\mathcal L_R\omega=\iota_Rd\omega+d(\omega(R))$ therefore gives

$$
(\iota_Rd\omega)_a(v)=(e^{-\operatorname{ad}_a}-I)v.
$$

On the other hand,

$$
\left(\iota_R\tfrac12[\omega,\omega]\right)_a(v)
=[a,\omega_a(v)]=(I-e^{-\operatorname{ad}_a})v.
$$

Adding gives $\iota_RK=0$.

For clarity, define the three-form $[\omega,K]$ by

$$
\omega,K=[\omega(u),K(v,w)]+[\omega(v),K(w,u)]+[\omega(w),K(u,v)].
$$

The exterior derivative product rule and Jacobi give the Bianchi identity

$$
dK+[\omega,K]=0.
\tag{3.3}
$$

Indeed, $d(\frac12[\omega,\omega])=-[\omega,d\omega]$, while $[\omega,\frac12[\omega,\omega]]=0$ is Jacobi evaluated on three vectors. These two equalities prove (3.3) without assuming a group exists.

Contract (3.3) with $R$. Since $\iota_RK=0$, Cartan's formula gives

$$
\mathcal L_RK=-[a,K].
$$

For constant vectors $u,v$, the coordinate expression for this equality along the ray $ta$ is

$$
t\frac{d}{dt}K_{ta}(u,v)+2K_{ta}(u,v)
=-t[a,K_{ta}(u,v)].
$$

Thus $Q(t)=t^2K_{ta}(u,v)$ solves $Q'(t)=-\operatorname{ad}_aQ(t)$ for $t>0$. Analyticity makes $Q(0)=0$ and extends this equation continuously to zero. Uniqueness of this linear equation gives $Q=0$. At $t=1$, $K_a(u,v)=0$. This proves (3.2). $\square$

## 4. Turning the coframe into a group

Let $E_i$ be the dual frame, defined by $\omega(E_i)=e_i$. Its fields are analytic because the coframe is invertible.

**Theorem 4.1 (local third theorem).** Every finite-dimensional real or complex Lie algebra is the Lie algebra of an analytic local Lie group, unique up to local isomorphism with a prescribed Lie-algebra identification.

**Proof.** Evaluate (3.2) on $E_i,E_j$. Since $\omega(E_i)$ and $\omega(E_j)$ are constant,

$$
d\omega(E_i,E_j)=-\omega([E_i,E_j]).
$$

Equation (3.2) gives $\omega([E_i,E_j])=[e_i,e_j]$. Therefore $[E_i,E_j]=\sum_kc_{ij}^kE_k$. The constant-frame construction in the preceding lesson gives a local group with identity zero and this left-invariant frame. Its tangent algebra is the original $\mathfrak g$. The uniqueness theorem there gives uniqueness of the local group. $\square$

This is a local result. It neither asserts that these coordinates contain every element of a global group nor derives global topology from the bracket.

### Canonical parameters and the two reciprocal frames

Volume III, Chapters 26–27, derives two parameter frames from the first variation of a flow. Our construction gives those frames without choosing eigenvalues of the adjoint matrix.

**Proposition 4.2 (exponential coordinates).** In the local group of Theorem 4.1, the coordinate $a\in\mathfrak g$ is its own exponential parameter:
$\exp(tu)=tu$ whenever this segment stays in the chosen neighbourhood. Put

$$
J_-(a)=\int_0^1e^{-s\operatorname{ad}_a}\,ds,
\qquad
J_+(a)=\int_0^1e^{s\operatorname{ad}_a}\,ds.
\tag{4.1}
$$

The left- and right-invariant fields with identity value $u$ are, respectively,

$$
E_u(a)=J_-(a)^{-1}u,\qquad
C_u(a)=J_+(a)^{-1}u.
\tag{4.2}
$$

They satisfy

$$
[E_u,E_v]=E_{[u,v]},\qquad
[C_u,C_v]=-C_{[u,v]},\qquad
[E_u,C_v]=0.
\tag{4.3}
$$

Both inverses in (4.2) exist near zero; neither is an inverse of $\operatorname{ad}_a$.

**Proof.** Since $\operatorname{ad}_{tu}u=0$, (3.1) gives
$\omega_{tu}(u)=u$. Thus $E_u(tu)=u$, and the path $t\mapsto tu$ solves the left-invariant flow equation from the identity. Uniqueness of that equation identifies it with the one-parameter subgroup. In particular, inversion is $a\mapsto-a$.

The first formula in (4.2) is the definition of the dual frame. In the preceding lesson, Section 3, right-invariant fields were constructed from right translations. Inversion carries $E_u$ to $-C_u$. In the coordinates here, its derivative is $-I$, so
$C_u(a)=E_u(-a)=J_+(a)^{-1}u$. Pushing the bracket of two $E$ fields through inversion gives the second bracket in (4.3). The flows of $E_u$ are right translations by $\exp(tu)$, whereas those of $C_v$ are left translations by $\exp(sv)$. Associativity makes these flows commute; differentiating their two-parameter identity gives the last bracket. The first bracket was proved in Theorem 4.1. Finally, $J_-(0)=J_+(0)=I$, and their determinants stay nonzero near zero. $\square$

The signs in (4.3) matter when comparing Lie's two parameter groups. His inverse-coordinate change exchanges the two frames. A constant change of basis changes both together, as in Proposition 1.2.

### Recovering central parameters by quadratures

There is also a precise local meaning to the central quadratures in Chapter 26. Here a *quadrature* means finding a primitive of an explicitly determined closed one-form by a line integral. The adjoint exponential is an entire matrix function; calling its calculation algebraic in the historical sense does not make its entries algebraic functions.

**Proposition 4.3 (central integration).** Suppose an analytic local group is already given in regular coordinates, and its Lie algebra has dimension $r$ and centre dimension $q$. The equations of its exponential map can be recovered locally from the adjoint exponential, coordinate inversion, and $q$ primitives of closed one-forms. For $q=0$, the local adjoint map alone determines the exponential coordinates.

**Proof.** Write
$\operatorname{Ad}(g)=d(h\mapsto ghg^{-1})_e$. Composition of conjugations proves that $\operatorname{Ad}$ is a local homomorphism. Its infinitesimal map is $\operatorname{ad}$. To check the sign, conjugation by $\exp(tu)$ has infinitesimal field $C_u-E_u$. For any field $V$, differentiation of its pushforward by the flow of a field $Z$ gives $-[Z,V]$: this follows by differentiating $d\Phi_t\,V(\Phi_{-t}(x))$ in coordinates. Apply it to $V=E_v$ and use (4.3), which holds in every local group by the reciprocal-frame calculation in the preceding lesson. The derivative is $E_{[u,v]}$. At the identity this is $[u,v]$. The homomorphism law now gives the constant matrix differential equation and initial value

$$
\frac{d}{dt}\operatorname{Ad}(\exp(tu))
=\operatorname{Ad}(\exp(tu))\operatorname{ad}_u,\qquad
\operatorname{Ad}(e)=I.
$$

Hence $\operatorname{Ad}(\exp(tu))=e^{t\operatorname{ad}_u}$.

At $e$, the differential of $\operatorname{Ad}$ has kernel the centre, so its rank is $m=r-q$. At $g$, differentiation along $E_v$ gives
$\operatorname{Ad}(g)\operatorname{ad}_v$; multiplication by the invertible matrix $\operatorname{Ad}(g)$ preserves this rank. The analytic constant-rank theorem therefore applies. Select $m$ matrix entries with independent differentials and call their collection $F(g)$. On a smaller chart they are transverse coordinates for the adjoint fibres. Every other adjoint entry is a function of $F$ there: its derivative vanishes on $\ker dF=\ker d\operatorname{Ad}$, so in the constant-rank coordinates it is independent of the fibre coordinates. This includes $m=0$, when the adjoint map is locally constant.

Fix a sufficiently small $u$. In the space of $(t,g)$ impose the $m$ equations

$$
F(g)=\text{the selected entries of }e^{t\operatorname{ad}_u}.
\tag{4.4}
$$

They define an analytic $(q+1)$-manifold $S$ near $(0,e)$. The full adjoint matrix on $S$ is $e^{t\operatorname{ad}_u}$: all its entries are functions of the selected ones, and the existing curve $\exp(tu)$ supplies the same branch. This curve is used to justify membership in the local adjoint image, rather than to supply its unknown coordinates.

Choose a basis $z_1,\ldots,z_q$ of the centre. On $S$ the fields

$$
Z=\partial_t+E_u,\qquad E_{z_1},\ldots,E_{z_q}
\tag{4.5}
$$

are tangent and form a frame. Tangency follows by differentiating (4.4), using the adjoint derivative just computed. The central fields span each adjoint fibre, and $Z$ has $t$ component one, proving independence. All fields in (4.5) commute, since $[u,z_j]=[z_i,z_j]=0$.

Define a one-form $\alpha_j$ on $S$ by
$\alpha_j(Z)=0$ and $\alpha_j(E_{z_i})=\delta_{ji}$. Its coefficients are obtained by inverting the frame matrix. The formula for an exterior derivative evaluated on a pair of fields shows that $d\alpha_j=0$: their brackets vanish and these evaluations are constant.

Each $\alpha_j$ has a local primitive $\sigma_j$. For completeness, take coordinates $y$ centred at $(0,e)$ on a star-shaped neighbourhood of $S$, and set

$$
\sigma_j(y)=\int_0^1(\alpha_j)_{sy}(y)\,ds.
\tag{4.6}
$$

Writing $\alpha_j=\sum_k a_k(y)\,dy_k$, closedness is
$\partial_\ell a_k=\partial_k a_\ell$. Differentiation of the integral gives

$$
\partial_\ell\sigma_j
=\int_0^1\left(a_\ell(sy)
+s\sum_k y_k\partial_k a_\ell(sy)\right)\,ds
=a_\ell(y).
$$

Thus (4.6) is the required primitive, normalized to zero at the initial point. Its construction is one quadrature for each $j$.

On a fibre at fixed $t$, the differentials $d\sigma_j$ are independent because their matrix on the $E_{z_i}$ is the identity. The equations
$\sigma_1=\cdots=\sigma_q=0$ therefore specify a unique local section of $S\to\{t\}$. Its tangent is $Z$, since $Z\sigma_j=0$ and $Zt=1$. It starts at $e$, so uniqueness of the original flow equation identifies this section with $(t,\exp(tu))$. Solving these $q$ equations together with (4.4) recovers the exponential coordinates. When $q=0$, there are no one-forms to integrate; the adjoint map is locally invertible onto its image. All constructions are local, and the same argument works with holomorphic coordinates over $\mathbb C$. $\square$

This result assumes that the group's finite equations are known. It is an integration reduction for that group, whereas Theorem 4.1 constructs a group from the bracket alone.

## 5. Examples with a centre

For an abelian algebra, $\operatorname{ad}_a=0$ and (3.1) is $\omega=da$. Its dual fields are constant and the resulting group is addition. The adjoint realization of Section 2 would have been zero; the coframe construction retains every dimension.

For the Heisenberg algebra, use $[e_x,e_y]=e_z$ with $e_z$ central and put $a=xe_x+ye_y+ze_z$. Since $\operatorname{ad}_a^2=0$,

$$
\omega^x=dx,\qquad \omega^y=dy,\qquad
\omega^z=dz-\tfrac12(x\,dy-y\,dx).
$$

Thus

$$
E_x=\partial_x-\tfrac y2\partial_z,\qquad
E_y=\partial_y+\tfrac x2\partial_z,\qquad E_z=\partial_z.
$$

Their bracket is $[E_x,E_y]=E_z$. The multiplication is

$$
(x,y,z)(u,v,w)=(x+u,y+v,z+w+\tfrac12(xv-yu)).
\tag{5.1}
$$

Associativity follows by expanding the bilinear cross term; identity is zero and inverse is $(-x,-y,-z)$. Differentiating (5.1) in the second factor gives the displayed left-invariant fields, so uniqueness identifies this explicit group with the coframe construction. The coordinate change $z_{\mathrm{matrix}}=z+xy/2$ gives the upper-unitriangular matrix coordinates of the preceding lesson.

For the two-dimensional nonabelian algebra $[h,e]=e$, put $a=sh+te$ and $f(s)=(1-e^{-s})/s$, with $f(0)=1$. Computing the integral in (3.1) gives

$$
\omega^h=ds,\qquad
\omega^e=f(s)\,dt+\frac{t(1-f(s))}{s}\,ds.
$$

The quotient $(1-f(s))/s$ has the analytic value $1/2$ at zero. This example illustrates again why division symbols in (3.1) denote analytic power series, rather than inverses of singular matrices.

## 6. Lie's function-group proof

In Volume II, Chapter 17, Lie realizes the constants first as brackets of independent functions on a canonical phase space. Their Hamiltonian fields then give a simply transitive group on a regular integral manifold. The earlier realization theorem he uses is proved in Volume II, Chapter 13. We supply its needed mathematics here, including the regularity condition that the canonical-coordinate construction requires. This route uses no group supplied by Theorem 4.1.

### A Jacobi bracket before any transformations exist

On an open set in $\mathbb K^r$ with coordinates $z_1,\ldots,z_r$, let analytic functions $w_{ij}(z)$ satisfy

$$
w_{ij}=-w_{ji},\qquad
\sum_\ell\left(
w_{\ell k}\partial_\ell w_{ij}
+w_{\ell i}\partial_\ell w_{jk}
+w_{\ell j}\partial_\ell w_{ki}\right)=0.
\tag{6.1}
$$

Define a bracket of analytic functions by

$$
\{F,G\}_w=\sum_{i,j}w_{ij}(z)\partial_iF\,\partial_jG,
\qquad X_F(G)=\{F,G\}_w.
\tag{6.2}
$$

Such a bracket is called a *Poisson bracket*: it is bilinear, antisymmetric, satisfies the product rule in each argument, and satisfies Jacobi. We use Lie's canonical sign, for which $\{p_i,x_j\}=\delta_{ij}$.

**Lemma 6.1.** Conditions (6.1) make (6.2) a Poisson bracket, and
$[X_F,X_G]=X_{\{F,G\}_w}$.

**Proof.** Bilinearity, antisymmetry and the product rules follow directly from (6.2). Expand
$\{\{F,G\}_w,H\}_w+\{\{G,H\}_w,F\}_w+\{\{H,F\}_w,G\}_w$.
The terms involving second derivatives of $F$ have coefficient

$$
\sum_{i,\ell,j,k}
(\partial_i\partial_\ell F)(\partial_jG)(\partial_kH)
\big(w_{\ell k}w_{ij}-w_{\ell j}w_{ik}\big).
$$

The expression in parentheses changes sign when $i,\ell$ are exchanged, while $\partial_i\partial_\ell F$ does not. Their sum is zero. The terms containing second derivatives of $G$ or $H$ cancel in the same way. The remaining expression is

$$
\sum_{i,j,k}(\partial_iF)(\partial_jG)(\partial_kH)
\sum_\ell\big(
w_{\ell k}\partial_\ell w_{ij}
+w_{\ell i}\partial_\ell w_{jk}
+w_{\ell j}\partial_\ell w_{ki}\big),
$$

which vanishes by (6.1). Finally, Jacobi gives
$\{F,\{G,H\}\}-\{G,\{F,H\}\}=\{\{F,G\},H\}$ for every $H$, proving the vector-field identity. $\square$

### Constructing one canonical pair at a time

**Lemma 6.2 (regular canonical coordinates).** Suppose $w$ has constant rank $2s$ near a point of an $r$-dimensional analytic Poisson space. There are analytic coordinates

$$
P_1,Q_1,\ldots,P_s,Q_s,C_1,\ldots,C_k,\qquad k=r-2s,
$$

in which
$\{P_i,Q_j\}=\delta_{ij}$ and all remaining coordinate brackets are determined by antisymmetry or vanish. In particular, every $C_\alpha$ commutes with all functions.

**Proof.** If the rank is zero, every $w_{ij}$ vanishes on this neighbourhood, and any coordinates serve as the $C_\alpha$.

If the rank is positive, some Hamiltonian coordinate field is nonzero at the chosen point. Rename that coordinate $P$. By the analytic straightening theorem, choose an analytic function $Q$ with $X_PQ=1$, so $\{P,Q\}=1$. Lemma 6.1 gives
$[X_P,X_Q]=X_1=0$. These two fields are pointwise independent: applying a relation between them to $P$ and $Q$ gives both coefficients zero. The complete-system theorem gives $r-2$ independent common first integrals $\zeta_1,\ldots,\zeta_{r-2}$.

The functions $(P,Q,\zeta)$ are a coordinate system. Indeed, in a relation between their differentials, evaluation on $X_P$ eliminates the coefficient of $dQ$, and evaluation on $X_Q$ eliminates that of $dP$. Independence of the $d\zeta$ eliminates the rest. Thus

$$
\{P,Q\}=1,\qquad
\{P,\zeta_a\}=\{Q,\zeta_a\}=0.
$$

Jacobi now implies
$X_P\{\zeta_a,\zeta_b\}=X_Q\{\zeta_a,\zeta_b\}=0$.
Every common first integral is a function of $\zeta$, by the same complete-system theorem. Hence the remaining bracket coefficients depend only on $\zeta$. In the new coordinates the coefficient matrix is a canonical rank-two block plus this residual Poisson matrix. Its rank is therefore $2s-2$, constant on a smaller neighbourhood. Its Jacobi identity follows by applying Lemma 6.1 to functions of $\zeta$ alone.

Apply the same construction to that residual bracket. Each step removes a rank-two block, so after $s$ steps the residual matrix is zero. Its $k$ remaining coordinates are the $C_\alpha$. This proves the statement by induction. All steps are analytic straightening, complete-system integration and an inverse-function coordinate change. $\square$

### Independent functions realizing the prescribed brackets

**Theorem 6.3 (canonical function realization).** Let $w$ satisfy (6.1) on a regular neighbourhood of rank $2s$ in dimension $r$. There are $r$ functionally independent analytic functions $\varphi_i(x,p)$ on a canonical phase space of dimension $2n$, with $n=r-s$, such that

$$
\{\varphi_i,\varphi_j\}_{xp}
=w_{ij}(\varphi_1,\ldots,\varphi_r),\qquad
\{F,G\}_{xp}
=\sum_{\mu=1}^n(F_{p_\mu}G_{x_\mu}-F_{x_\mu}G_{p_\mu}).
\tag{6.3}
$$

This phase-space dimension is the smallest possible for a realization whose differentials are independent and whose target bracket has this rank.

**Proof.** Take the coordinates of Lemma 6.2 and express the original coordinates as
$z_i=F_i(P,Q,C)$. On canonical phase space set

$$
\varphi_i(x,p)
=F_i(p_1,x_1,\ldots,p_s,x_s,p_{s+1},\ldots,p_{s+k}),
\qquad n=s+k=r-s.
$$

The functions do not depend on the unused partners $x_{s+1},\ldots,x_{s+k}$. The coordinate brackets of the arguments on the right are precisely those in Lemma 6.2. Applying the chain rule to both brackets proves (6.3). The inverse coordinate map $F$ has invertible derivative, and the selected $r$ phase-space coordinates are independent; hence the $d\varphi_i$ are independent. This also covers $s=0$: take independent momenta as the $\varphi_i$.

For minimality, suppose a realization exists on a $2N$-dimensional canonical phase space. Nondegeneracy of the canonical skew form
$\sigma=\sum_\mu dp_\mu\wedge dx_\mu$ identifies the independent $d\varphi_i$ with independent Hamiltonian fields $X_{\varphi_i}$, since $\iota_{X_\varphi}\sigma=-d\varphi$. Let $D$ be their $r$-dimensional span at the point. The restriction of $\sigma$ to $D$ has matrix $\{\varphi_i,\varphi_j\}$ and rank $2s$. Its kernel has dimension $r-2s$ and equals $D\cap D^\perp$. Nondegeneracy of $\sigma$ gives $\dim D^\perp=2N-r$, so
$r-2s\le2N-r$, or $2N\ge2(r-s)$. The constructed realization attains this bound. $\square$

### From a function group to a simply transitive group

**Proposition 6.4 (Lie's existence construction).** Every skew constant array satisfying Jacobi admits the independent canonical realization
$\{\varphi_i,\varphi_j\}=\sum_\ell c_{ij}^{\ell}\varphi_\ell$.
Its Hamiltonian fields restrict to a full constant-bracket frame on an $r$-dimensional integral manifold, and hence produce an analytic local group with the prescribed Lie algebra.

**Proof.** Set $w_{ij}(z)=\sum_\ell c_{ij}^{\ell}z_\ell$. The skew equations for $w$ are immediate. Its Jacobi expression in (6.1) is

$$
\sum_m z_m\sum_\ell
\big(c_{ij}^{\ell}c_{\ell k}^{m}
+c_{jk}^{\ell}c_{\ell i}^{m}
+c_{ki}^{\ell}c_{\ell j}^{m}\big)=0.
$$

Choose a point where this analytic matrix has maximal rank. A nonzero maximal minor remains nonzero in a neighbourhood; maximality prevents any greater rank there. Thus a regular neighbourhood exists, including when the matrix is identically zero. Theorem 6.3 supplies independent $\varphi_i$ with the required brackets.

The fields $A_i=X_{\varphi_i}$ have pointwise rank $r$ by canonical nondegeneracy. Lemma 6.1 gives
$[A_i,A_j]=\sum_\ell c_{ij}^{\ell}A_\ell$. The complete-system theorem therefore supplies $2n-r$ independent common first integrals $\psi_\alpha$. Complete them to coordinates $(u_1,\ldots,u_r,\psi)$. Every $A_i$ has only $u$ components, whose coefficient matrix is invertible. On a fibre $\psi=C$ within this chart, these fields retain their full rank and their bracket relations. The constant-frame construction in the preceding lesson makes this fibre, locally, the desired group. Its transformations act simply transitively near the chosen identity. $\square$

Lie calls the functions commuting with all $\varphi_i$ their *polar function group*. Here they are precisely common first integrals of the Hamiltonian distribution. The construction begins at a regular point of the coefficient space; it does not assert a regular canonical normal form at every singular point, such as the origin of a nonzero linear Poisson bracket. The resulting local group has an identity of its own on the chosen integral manifold, so no identity at that singular coefficient-space origin is required.

**Example 6.5 (the central generator survives).** On a four-dimensional phase space $(x,y,p_x,p_y)$ take
$\varphi_1=p_x$, $\varphi_2=x p_y$ and $\varphi_3=p_y$. Their only nonzero independent bracket is $\{\varphi_1,\varphi_2\}=\varphi_3$. On $p_y\ne0$ their differentials are independent, and

$$
A_1=\partial_x,\qquad
A_2=x\partial_y-p_y\partial_{p_x},\qquad
A_3=\partial_y.
$$

The polar coordinate is $p_y$. Fixing $p_y=C\ne0$ gives a full frame on $(x,y,p_x)$ with $[A_1,A_2]=A_3$. Although $\varphi_3$ is central among these functions, it is not constant on the phase space; its Hamiltonian field is nonzero. At $C=0$ this particular frame loses rank, explaining why fibre values must stay inside the regular chart.

### Homogeneous contact realizations

**Proposition 6.6 (homogenization).** A function realization of a linear Lie bracket can be made homogeneous of degree one in the momenta after adding one canonical pair. Its independent Hamiltonian fields preserve the canonical one-form and realize the same algebra.

**Proof.** Add coordinates $(t,\tau)$ and work on $\tau\ne0$. Define

$$
h_i(x,p,t,\tau)=\tau\varphi_i(x,p/\tau).
\tag{6.4}
$$

These functions are independent of $t$. Their derivatives in an old canonical pair are
$(h_i)_{p_\mu}=(\varphi_i)_{p_\mu}(x,p/\tau)$ and
$(h_i)_{x_\mu}=\tau(\varphi_i)_{x_\mu}(x,p/\tau)$.
The new pair contributes zero to mutual brackets because $(h_i)_t=0$. Hence

$$
\{h_i,h_j\}=\tau\{\varphi_i,\varphi_j\}(x,p/\tau)
=\sum_\ell c_{ij}^{\ell}h_\ell.
$$

For fixed nonzero $\tau$, the old variables still give rank $r$ of the differentials. The Hamiltonian fields are consequently independent, and Lemma 6.1 gives their required brackets.

Each $h_i$ satisfies Euler's identity
$\sum_\mu p_\mu(h_i)_{p_\mu}+\tau(h_i)_\tau=h_i$.
Put $\theta=\sum_\mu p_\mu\,dx_\mu+\tau\,dt$. The coordinate Hamiltonian formula gives
$\iota_{X_h}d\theta=-dh$ and $\theta(X_h)=h$. Thus

$$
\mathcal L_{X_h}\theta
=\iota_{X_h}d\theta+d(\theta(X_h))
=-dh+dh=0.
$$

The same Euler identity shows that $X_h$ commutes with momentum dilation: its spatial coefficients have degree zero and its momentum coefficients have degree one. Its local flow therefore preserves $\theta$ and respects dilation. These are the homogeneous contact transformations used in the historical reading. Passing to a chart of momentum ratios gives the usual contact distribution. Linear combinations of the $h_i$ still have degree one, so every infinitesimal transformation in the generated algebra has this property. $\square$

This added-pair construction supplies the homogeneous realization needed in the final part of Lie's Chapter 17. Lie's Chapter 13 instead constructs homogeneous canonical coordinates directly. Both arguments require regular local domains; neither asserts a global homogeneous chart.

<a id="6-exercises"></a>

## 7. Exercises

**Exercise 1 (introductory).** Verify Jacobi for the algebra with $[e_i,e_j]=\sum_k\varepsilon_{ijk}e_k$.

**Exercise 2 (intermediate).** Verify the two-dimensional centreless realization in Example 2.2 and compute the two flows.

**Exercise 3 (intermediate).** Prove that the adjoint realization always has image isomorphic to $\mathfrak g/Z(\mathfrak g)$. Apply this to an abelian algebra and to the Heisenberg algebra.

**Exercise 4 (intermediate).** Compute $d\omega^z$ in the Heisenberg example and check the Maurer–Cartan equation and multiplication law.

**Exercise 5 (advanced).** Reconstruct the radial proof of (3.2), including the Bianchi identity and the initial value at $t=0$. Explain why merely checking $\iota_RK=0$ would be insufficient.

**Exercise 6 (intermediate).** In the Heisenberg algebra $[e_1,e_2]=e_3$, change basis to $f_1=e_1+e_2$, $f_2=e_2+e_3$, $f_3=e_3$. Compute every independent bracket in this basis and check (1.5). Then scale all three $f_i$ by a nonzero scalar $\lambda$. How do the constants change?

**Exercise 7 (intermediate).** Prove that the Heisenberg centre has no complementary subalgebra. Compare this obstruction with the faithful linear realization (2.3).

**Exercise 8 (intermediate).** Verify the independence and Hamiltonian brackets in Example 6.5, and compute the frame determinant after fixing $p_y=C$. Explain why four is the smallest canonical phase-space dimension for this independent function realization, although the resulting local group has dimension three. What is the corresponding minimum for $r$ independent commuting Hamiltonians?

**Exercise 9 (intermediate).** Compute both reciprocal frames in the Heisenberg exponential coordinates of Section 5. Check the opposite right-frame bracket and the commutation of the two frames. Does a central element make either $J_-$ or $J_+$ singular?

**Exercise 10 (advanced).** Use the Heisenberg group in matrix coordinates, with law
$(A,B,C)(A',B',C')=(A+A',B+B',C+C'+AB')$. For $u=xe_x+ye_y+ze_z$, determine its adjoint matrix, the manifold $S$ in Proposition 4.3, and the one closed form needed to recover its exponential. Compute $\exp(u)$.

<a id="7-solutions"></a>

## 8. Solutions

**Solution 1.** Identify this bracket with the cross product in $\mathbb R^3$ and extend scalars if desired. The vector identity $u\times(v\times w)=v(u\cdot w)-w(u\cdot v)$ makes the cyclic sum zero. This identity follows componentwise from $\sum_k\varepsilon_{ijk}\varepsilon_{k\ell m}=\delta_{i\ell}\delta_{jm}-\delta_{im}\delta_{j\ell}$, which can be checked by distinguishing repeated and distinct indices. Thus Jacobi holds for all vectors by bilinearity.

**Solution 2.** The fields are $E_h=-t\partial_t$ and $E_e=s\partial_t$. Their bracket coefficient is $(-t)\partial_t(s)-s\partial_t(-t)=s$, so $[E_h,E_e]=E_e$. Their time-$\tau$ flows are $(s,t)\mapsto(s,e^{-\tau}t)$ and $(s,t)\mapsto(s,t+\tau s)$. A constant combination vanishes for all $s,t$ only if both constants vanish.

**Solution 3.** Proposition 2.1 gives a bracket-preserving linear map with kernel exactly the centre. The linear first-isomorphism theorem, together with bracket preservation, identifies its image with the quotient algebra. For an abelian algebra the quotient and image are zero. For Heisenberg, the quotient has basis represented by $e_x,e_y$ and is abelian; the nonzero central direction is lost. This is why the adjoint construction alone cannot realize Heisenberg faithfully.

**Solution 4.** Differentiating gives $d\omega^z=-dx\wedge dy$, while the $e_z$ component of $\frac12[\omega,\omega]$ is $dx\wedge dy$. The other components vanish. For (5.1), the central cross term in a triple product is the sum of the cross terms of the first pair, the first and third elements, and the second and third elements, independent of parenthesization. Identity and inverse follow immediately; differentiating in $(u,v,w)$ at zero gives $E_x,E_y,E_z$.

**Solution 5.** First use $\omega(R)=a$ and the derivative of $t\omega_{ta}$ to obtain $\iota_RK=0$. Next expand $K=d\omega+\frac12[\omega,\omega]$ and apply the exterior derivative product rule; Jacobi removes the cubic bracket term and yields $dK+[\omega,K]=0$. Contracting this equation gives $\mathcal L_RK=-[a,K]$. On a ray this becomes $Q'=-\operatorname{ad}_aQ$ for $Q=t^2K_{ta}(u,v)$. Continuity of $K$ at zero gives $Q(0)=0$, so uniqueness forces $Q=0$. A two-form can have zero radial contraction while being nonzero in transverse directions; the Bianchi equation and zero initial value supply the missing implication.

**Solution 6.** Bilinearity and centrality give $[f_1,f_2]=e_3=f_3$ and $[f_1,f_3]=[f_2,f_3]=0$. Here

$$
H=\begin{pmatrix}1&1&0\\0&1&1\\0&0&1\end{pmatrix},
\qquad
H^{-1}=\begin{pmatrix}1&-1&1\\0&1&-1\\0&0&1\end{pmatrix}.
$$

The only old nonzero constants are $c_{12}^{3}=1$ and $c_{21}^{3}=-1$. Formula (1.5) therefore reduces to
$c'{}_{ik}^{\rho}=(h_{i1}h_{k2}-h_{i2}h_{k1})(H^{-1})_{3\rho}$.
The last row of $H^{-1}$ is $(0,0,1)$, which gives exactly the brackets above. If $g_i=\lambda f_i$, then $[g_i,g_k]=\lambda^2[f_i,f_k]=\sum_\rho\lambda c'{}_{ik}^{\rho}g_\rho$. Thus every constant is multiplied by $\lambda$, in agreement with (1.5) for $H=\lambda I$.

**Solution 7.** The centre is $\mathbb K e_3$. If a two-dimensional subspace $\mathfrak h$ complements it, projection to $\mathfrak g/\mathbb K e_3$ maps a basis $u,v$ of $\mathfrak h$ to a basis. Write their $e_1,e_2$ coefficients as $(a,b)$ and $(c,d)$. Then $ad-bc\ne0$ and $[u,v]=(ad-bc)e_3$ is a nonzero central element. If $\mathfrak h$ were a subalgebra, this element would belong to $\mathfrak h\cap\mathbb K e_3=0$, a contradiction. Proposition 2.3 consequently does not apply. Example 2.4 nevertheless realizes all three generators faithfully, so the failed split-centre hypothesis is a limitation of that construction, not an obstruction to every linear realization.

**Solution 8.** The Jacobian of $(p_x,xp_y,p_y)$ with respect to $(p_x,x,p_y)$ has determinant $p_y$, so it has rank three on $p_y\ne0$. The canonical formula gives $\{\varphi_1,\varphi_2\}=p_y=\varphi_3$ and the other two independent brackets zero. Its Hamiltonian fields are the displayed $A_1,A_2,A_3$; direct differentiation gives $[A_1,A_2]=A_3$ and the other brackets zero. On $p_y=C$, their coefficient columns in $(x,y,p_x)$ are $(1,0,0)$, $(0,x,-C)$ and $(0,1,0)$, whose determinant is $C$. The target bracket has rank two there, so Theorem 6.3 gives the minimum $2(3-1)=4$. This bounds the phase space of independent Hamiltonian functions, not the dimension of an ordinary group: restricting to the three-dimensional integral manifold gives the group. For $r$ independent commuting Hamiltonians the target rank is zero, and the same bound is $2r$, attained by the $r$ canonical momenta.

**Solution 9.** Here $\operatorname{ad}_a^2=0$, so $J_-=I-\frac12\operatorname{ad}_a$ and $J_+=I+\frac12\operatorname{ad}_a$. Their inverses have the opposite signs. Besides the left frame displayed in Section 5, this gives

$$
C_x=\partial_x+\tfrac y2\partial_z,\qquad
C_y=\partial_y-\tfrac x2\partial_z,\qquad C_z=\partial_z.
$$

The $z$ coefficient of $[C_x,C_y]$ is $-\frac12-\frac12=-1$, hence $[C_x,C_y]=-C_z$. Each mixed bracket vanishes: for example, the two derivative terms in the $z$ coefficient of $[E_x,C_y]$ are $-\frac12$ and $-\frac12$ before subtraction. The other mixed pairs give zero in the same coordinate formula. If $a$ is central, $\operatorname{ad}_a=0$ and both matrices are the identity. Centrality therefore causes no singularity.

**Solution 10.** In these coordinates the left frame is
$E_x=\partial_A$, $E_y=\partial_B+A\partial_C$, $E_z=\partial_C$. The inverse of $(A,B,C)$ is $(-A,-B,-C+AB)$. Computing its conjugation on each of the three coordinate one-parameter subgroups gives

$$
\operatorname{Ad}(A,B,C)e_x=e_x-Be_z,\qquad
\operatorname{Ad}(A,B,C)e_y=e_y+Ae_z,\qquad
\operatorname{Ad}(A,B,C)e_z=e_z.
$$

Thus the selected adjoint coordinates can be $(A,B)$ and (4.4) imposes
$A=tx$, $B=ty$. The remaining coordinate is $C$, so $S$ has coordinates $(t,C)$ and the commuting frame is

$$
Z=\partial_t+(z+txy)\partial_C,\qquad E_z=\partial_C.
$$

Its required closed form is
$\alpha=dC-(z+txy)\,dt$. A normalized primitive is
$\sigma=C-zt-\frac12xyt^2$. The equation $\sigma=0$ gives
$\exp(tu)=(tx,ty,tz+\frac12t^2xy)$ and hence
$\exp(u)=(x,y,z+\frac12xy)$. This is exactly the coordinate change from the exponential coordinates in Section 5 to the matrix coordinates.

## Historical and global perspective

Lie's first-volume adjoint construction addresses the centreless case. His function-group proof uses the canonical realization theorem of Volume II, Chapter 13, and the Hamiltonian construction of Chapter 17; Section 6 develops these steps explicitly. Volume III revisits the existence and structure theory. The coframe proof and the function-group proof above are two independent local routes, with the same constant-frame integration as their final step.

Chapter 25 of Volume III states both directions of the first two fundamental theorems and distinguishes a regular identity family from a coset of a group. It gives the full converse integration argument, rather than relying on the preliminary commutator heuristic. Its §115 returns to general existence: the linear coadjoint fields can lose central directions, and adjoining the missing conjugate variables restores independence. This is the canonical realization developed in Section 6.

Chapter 26 recovers exponential parameters from known group equations; Proposition 4.3 explains its centreless and central cases. Chapter 27 constructs the two reciprocal parameter frames from the structure constants; Proposition 4.2 gives them by entire power series. The final step in §129 takes invariants of a subalgebra of one frame and projects the commuting frame to those invariant variables. The complete-system theorem supplies the local invariants, and commutation makes the projected coefficients functions of those variables. The projected generators must still be independent over constants for an effective $r$-parameter action. The later lesson Transitive actions, isotropy, and invariant foliations carries out this stabilizer construction and its kernel condition.

The global theorem asserts existence of a connected simply connected Lie group for every finite-dimensional real Lie algebra, unique up to Lie-group isomorphism; the complex analogue requires holomorphic group structure. This global theorem is not proved here. Ado's theorem, which gives faithful finite-dimensional linear representations in characteristic zero, is also not proved here and was not needed for our local argument.

## References

- Sophus Lie, with Friedrich Engel, *Theorie der Transformationsgruppen*, Volume I, 1888, Chapter 17, pp. 289–310; Volume II, 1890, Chapter 13, §§62–63, especially Theorems 37–38, pp. 241–249, and complete Chapter 17, §75, pp. 294–298; Volume III, 1893, complete Chapters 25–27, §§107–129, pp. 545–665. Section 6 gives independently written proofs of the needed canonical-realization and Hamiltonian steps, following the original canonical-pair construction for regular brackets. The historical readings below reproduce complete selected passages from the original German and give an independent English translation.
- Joël Merker, *Theory of Transformation Groups, by S. Lie and F. Engel (Vol. I, 1888): Modern Presentation and English Translation*, 2010, chapter on composition and isomorphism. [Author's preprint](https://arxiv.org/abs/1003.3202).
- Michael Kunzinger, *Lie Transformation Groups: An Introduction to Symmetry Group Analysis of Differential Equations*, 2015, corrected December 2024. [Author's text](https://www.mat.univie.ac.at/~mike/teaching/ss15/ltg.pdf).

## Historical reading: composition, isomorphism and existence

**Source and complete scope.** Sophus Lie and Friedrich Engel, *Theorie der Transformationsgruppen*, Volume I (1888), complete Chapter 17 introduction and complete §§80–81, printed pp. 289–300. The reading starts at the Chapter 17 heading below the Chapter 16 conclusion on p. 289 and stops after Theorem 53, before §82 on p. 300. The initially assigned pp. 296–300 omit most of §80; the full sections are included here. Both original footnotes, on pp. 293 and 296, are retained. The original is public domain; this transcription, independently written English translation and editorial notes are dedicated to CC0.

**Editorial method.** Historical spelling, paragraph order, section divisions, theorem numbers and equation numbers are retained. Words divided across lines are joined; spacing and summation typography are normalized; running heads are omitted. Fraktur letters distinguish the changed generator bases. Repeated equation numbers are retained as printed. The bracket $(XY)$ means the differential-operator commutator $XY-YX$, applied to $f$. Historical “isomorphism” has the broader meaning defined in the reading; it includes quotient homomorphisms. Mathematical qualifications appear separately in the reading notes. Lie's explicit deferral of the general existence proof is translated without alteration.

### German transcription: Chapter 17 introduction and complete §§80–81

**D01 · p. 289**

**Kapitel 17. Zusammensetzung und Isomorphismus.**

Viele Aufgaben, die man über eine $r$-gliedrige Gruppe $X_1f\cdots X_rf$ stellen kann, erfordern zu ihrer Lösung nur die Kenntniss der Constanten $c_{iks}$ in den Relationen:

$$
(X_iX_k)=\sum_{s=1}^r c_{iks}\,X_sf.
$$

So haben wir zum Beispiel gesehen, dass die Bestimmung aller Untergruppen der Gruppe $X_1f\cdots X_rf$ nur von den Constanten $c_{iks}$ abhängt und genau dasselbe gilt auch von der Bestimmung aller Typen von Untergruppen (vgl. Theorem 33, S. 210 und Kapitel 16, S. 280 und 281).

**D02 · p. 289**

Es erhellt hieraus, dass die Constanten $c_{iks}$ an und für sich schon gewisse Eigenschaften der Gruppe $X_1f\cdots X_rf$ abspiegeln. Für den Inbegriff dieser Eigenschaften führen wir eine besondere Bezeichnung ein, wir nennen ihn die *Zusammensetzung* der Gruppe und sagen daher, *dass die Constanten $c_{iks}$ in den Relationen*

$$
(X_iX_k)=\sum_{s=1}^r c_{iks}\,X_sf.\tag{1}
$$

*die Zusammensetzung der $r$-gliedrigen Gruppe $X_1f\cdots X_rf$ bestimmen*.

**D03 · pp. 289–290**

**§80.** Das System der $c_{iks}$, welches die Zusammensetzung der $r$-gliedrigen Gruppe $X_1f\cdots X_rf$ bestimmt, ist seinerseits nicht vollständig bestimmt. Die einzelnen $c_{iks}$ erhalten nämlich im Allgemeinen andere Zahlenwerthe, wenn man an Stelle von $X_1f\cdots X_rf$ irgend $r$ andere unabhängige infinitesimale Transformationen $e_1X_1f+\cdots+e_rX_rf$ derselben Gruppe auswählt.

Hieraus folgt, dass zwei verschiedene Systeme von $c_{iks}$ unter Umständen die Zusammensetzung einer und derselben Gruppe darstellen können. Wie aber erkennen, ob sie das thun?

**D04 · p. 290**

Wir gehen aus von den Relationen:

$$
(X_iX_k)=\sum_{s=1}^r c_{iks}\,X_sf\qquad(i,k=1\cdots r),\tag{1}
$$

welche zwischen $r$ bestimmten unabhängigen infinitesimalen Transformationen $X_1f\cdots X_rf$ unsrer Gruppe bestehen. Wir suchen die allgemeine Form der Relationen, durch welche $r$ beliebige unabhängige infinitesimale Transformationen $\mathfrak{X}_1f\cdots\mathfrak{X}_rf$ der Gruppe $X_1f\cdots X_rf$ verknüpft sind.

Haben die betreffenden Relationen die Form:

$$
(\mathfrak{X}_i\mathfrak{X}_k)=\sum_{s=1}^r c'_{iks}\,\mathfrak{X}_sf.\tag{2}
$$

so ist das System der Constanten $c'_{iks}$ das allgemeinste, welches die Zusammensetzung der Gruppe $X_1f\cdots X_rf$ darstellt. Es handelt sich daher nur um die Berechnung der $c'_{iks}$.

**D05 · p. 290**

Da $\mathfrak{X}_1f\cdots\mathfrak{X}_rf$ beliebige unabhängige infinitesimale Transformationen der Gruppe $X_1f\cdots X_rf$ sein sollen, so ist:

$$
\mathfrak{X}_kf=\sum_{j=1}^r h_{kj}\,X_jf\qquad(k=1\cdots r),
$$

wo die Constanten $h_{kj}$ alle möglichen Werthe annehmen können, welche die Determinante

$$
D=\sum\pm h_{11}\cdots h_{rr}
$$

nicht zum Verschwinden bringen.

**D06 · p. 290**

Durch Ausrechnung ergiebt sich:

$$
(\mathfrak{X}_i\mathfrak{X}_k)=\sum_{j,\pi=1}^r h_{ij}h_{k\pi}(X_jX_\pi)=\sum_{j,\pi,s=1}^r h_{ij}h_{k\pi}c_{j\pi s}\,X_sf;
$$

andererseits folgt aus (2):

$$
(\mathfrak{X}_i\mathfrak{X}_k)=\sum_{\pi,s=1}^r h_{\pi s}c'_{ik\pi}\,X_sf.
$$

Vergleichen wir diese beiden Ausdrücke für $(\mathfrak{X}_i\mathfrak{X}_k)$ mit einander und berücksichtigen, dass $X_1f\cdots X_rf$ unabhängige infinitesimale Transformationen sind, so erhalten wir die Relationen:

$$
\sum_{\pi=1}^r h_{\pi s}c'_{ik\pi}=\sum_{j,\pi=1}^r h_{ij}h_{k\pi}c_{j\pi s}\qquad(s=1\cdots r).\tag{3}
$$

**D07 · p. 291**

Unter den gemachten Voraussetzungen lassen sich diese Gleichungen nach den $c'_{ik\pi}$ auflösen, also wird:

$$
c'_{ik\rho}=\frac1D\sum_{s=1}^r\left\{\frac{\partial D}{\partial h_{\rho s}}\sum_{j,\pi=1}^r h_{ij}h_{k\pi}\right\}c_{j\pi s}\qquad(i,k,\rho=1\cdots r).\tag{4}
$$

Hiermit ist nach dem Obigen die allgemeine Form aller Constantensysteme gefunden, welche die Zusammensetzung der Gruppe $X_1f\cdots X_rf$ bestimmen. Zugleich haben wir wenigstens theoretisch die Möglichkeit, zu entscheiden, ob ein vorgelegtes System von Constanten $\bar c_{iks}$ die Zusammensetzung der Gruppe $X_1f\cdots X_rf$ bestimmt; es besitzt nämlich diese Eigenschaft offenbar dann, aber auch nur dann, wenn man in (4) die Parameter $h_{kj}$ so wählen kann, dass $c'_{iks}=\bar c_{iks}$ wird. —

**D08 · p. 291**

Sind *zwei* $r$-gliedrige Gruppen vorgelegt, so können wir die Zusammensetzungen derselben mit einander vergleichen. Offenbar sind wir durch die obigen Entwickelungen in den Stand gesetzt, zu entscheiden, ob die beiden Gruppen ein und dieselbe oder ob sie verschiedene Zusammensetzung haben. Auf die Zahl der Veränderlichen, welche in den beiden Gruppen auftreten, brauchen wir dabei offenbar keine Rücksicht zu nehmen.

*Zwei $r$-gliedrige Gruppen, welche ein und dieselbe Zusammensetzung haben, bezeichnen wir als gleichzusammengesetzt.*

**D09 · p. 291**

Sind

$$
X_kf=\sum_{i=1}^n \xi_{ki}(x_1\cdots x_n)\frac{\partial f}{\partial x_i}\qquad(k=1\cdots r)
$$

unabhängige infinitesimale Transformationen einer $r$-gliedrigen Gruppe und

$$
Y_kf=\sum_{\mu=1}^m\eta_{k\mu}(y_1\cdots y_m)\frac{\partial f}{\partial y_\mu}\qquad(k=1\cdots r)
$$

unabhängige infinitesimale Transformationen einer zweiten, bestehen ausserdem die Relationen

$$
(X_iX_k)=\sum_{s=1}^r c_{iks}\,X_sf,
$$

*so sind diese beiden Gruppen offenbar dann, aber auch nur dann gleichzusammengesetzt, wenn sich unter den infinitesimalen Transformationen $e_1Y_1f+\cdots+e_rY_rf$ der zweiten $r$ solche von einander unabhängige $\mathfrak{Y}_1f\cdots\mathfrak{Y}_rf$ angeben lassen, dass die Relationen*

$$
(\mathfrak{Y}_i\mathfrak{Y}_k)=\sum_{s=1}^r c_{iks}\,\mathfrak{Y}_sf
$$

*identisch stattfinden.*

**D10 · p. 292**

Haben die zwischen $Y_1f\cdots Y_rf$ stattfindenden Relationen die Form

$$
(Y_iY_k)=\sum_{s=1}^r\bar c_{iks}\,Y_sf,
$$

so können wir sagen: die beiden Gruppen sind dann und nur dann gleichzusammengesetzt, wenn es möglich ist, in den Gleichungen (4) die Parameter $h_{kj}$ so zu wählen, dass jedes $c'_{iks}$ dem entsprechenden $\bar c_{iks}$ gleich wird.

Man kann auch die Zusammensetzung solcher Gruppen vergleichen, die nicht beide dieselbe Anzahl von Parametern haben. Ermöglicht wird das durch die Einführung des allgemeinen Begriffes: *Isomorphismus*.

**D11 · p. 292**

*Die $r$-gliedrige Gruppe $X_1f\cdots X_rf$:*

$$
(X_iX_k)=\sum_{s=1}^r c_{iks}\,X_sf
$$

*nennen wir isomorph mit der $(r-q)$-gliedrigen: $Y_1f\cdots Y_{r-q}f$, wenn es möglich ist, in der $(r-q)$-gliedrigen $r$ infinitesimale Transformationen*

$$
\mathfrak{Y}_kf=h_{k1}\,Y_1f+\cdots+h_{k,r-q}\,Y_{r-q}f\qquad(k=1\cdots r)
$$

*so auszuwählen, dass nicht alle $(r-q)$-reihigen Determinanten der Matrix*

$$
\left|\begin{matrix}h_{11}&\cdots&h_{1,r-q}\\ \vdots&&\vdots\\ h_{r1}&\cdots&h_{r,r-q}\end{matrix}\right|
$$

*verschwinden, und dass zugleich die Relationen*

$$
(\mathfrak{Y}_i\mathfrak{Y}_k)=\sum_{s=1}^r c_{iks}\,\mathfrak{Y}_sf
$$

*identisch bestehen.*

**D12 · pp. 292–293**

Es finde Isomorphismus in diesem Sinne statt, und es seien $\mathfrak{Y}_1f\cdots\mathfrak{Y}_rf$ bereits in der angegebenen Weise gewählt. Ordnen wir dann der infinitesimalen Transformation $e_1X_1f+\cdots+e_rX_rf$ der $r$-gliedrigen Gruppe stets die infinitesimale Transformation

$$
e_1\,\mathfrak{Y}_1f+\cdots+e_r\,\mathfrak{Y}_rf
$$

der $(r-q)$-gliedrigen zu, welche Werthe auch die Constanten $e_1\cdots e_r$ haben mögen, so findet offenbar Folgendes statt: wenn $\Upsilon_1f$ diejenige Transformation der $(r-q)$-gliedrigen Gruppe ist, welche der Transformation $\Xi_1f$ der anderen Gruppe zugeordnet ist, und wenn in entsprechender Weise $\Upsilon_2f$ der Transformation $\Xi_2f$ zugeordnet ist, so entspricht stets der Transformation $(\Upsilon_1\Upsilon_2)$ die Transformation $(\Xi_1\Xi_2)$. Wir drücken das kürzer so aus: durch die angegebene Zuordnung der infinitesimalen Transformationen beider Gruppen zu einander sind die Gruppen *isomorph auf einander bezogen*. Augenscheinlich ist diese isomorphe Beziehung vollständig bestimmt, wenn man weiss, dass $X_1f\cdots X_rf$ bezüglich den Transformationen $\mathfrak{Y}_1f\cdots\mathfrak{Y}_rf$ zugeordnet sind.

**D13 · p. 293**

Man unterscheidet zwischen *holoedrischem* und *meroedrischem Isomorphismus*. Der holoedrische tritt ein, wenn die Zahl $q$, welche in der Definition des Isomorphismus vorkommt, den Werth Null hat; der meroedrische, wenn $q$ grösser ist als Null. Dementsprechend sagt man, dass die beiden Gruppen holoedrisch oder meroedrisch isomorph auf einander bezogen sind, jenachdem.

Augenscheinlich ist die Eigenschaft des Gleichzusammengesetztseins zweier Gruppen ein besonderer Fall des Isomorphismus; zwei gleichzusammengesetzte Gruppen sind nämlich stets holoedrisch isomorph, und umgekehrt.

**D14 · p. 293**

Zwei meroedrisch isomorphe Gruppen sind zum Beispiel die beiden:

$$
\frac{\partial f}{\partial x_1},\quad x_1\frac{\partial f}{\partial x_1},\quad x_1^2\frac{\partial f}{\partial x_1},\quad\frac{\partial f}{\partial x_2}
$$

und:

$$
\frac{\partial f}{\partial y_1},\quad y_1\frac{\partial f}{\partial y_1},\quad y_1^2\frac{\partial f}{\partial y_1},
$$

mit bezüglich vier und drei Parametern. Wir erhalten diese Gruppen meroedrisch isomorph auf einander bezogen, wenn wir den vier infinitesimalen Transformationen:

$$
\begin{aligned}X_1f&=\frac{\partial f}{\partial x_1},&X_2f&=x_1\frac{\partial f}{\partial x_1},\\X_3f&=x_1^2\frac{\partial f}{\partial x_1},&X_4f&=\frac{\partial f}{\partial x_1}+\frac{\partial f}{\partial x_2}\end{aligned}
$$

der einen etwa die folgenden vier:

$$
\begin{aligned}\mathfrak{Y}_1f&=\frac{\partial f}{\partial y_1},&\mathfrak{Y}_2f&=y_1\frac{\partial f}{\partial y_1},\\\mathfrak{Y}_3f&=y_1^2\frac{\partial f}{\partial y_1},&\mathfrak{Y}_4f&=\frac{\partial f}{\partial y_1}\end{aligned}
$$

der andern zuordnen.

**D15 · p. 293**

Auch in der Substitutionentheorie redet man von isomorphen Gruppen, doch definirt man da den Isomorphismus anscheinend anders als hier geschehen. [F1] Wir werden uns später (vgl. Kap. 21, die Parametergruppe) überzeugen, dass nichtsdestoweniger der aus unserer Definition folgende Begriff des Isomorphismus sich vollkommen mit demjenigen deckt, welchen man erhält, sobald man die Definition der Substitutionentheorie direkt auf die Theorie der endlichen continuirlichen Gruppen überträgt.

**D16 · p. 294**

Jetzt werden wir zunächst einige einfache Folgerungen aus unsrer Definition des Isomorphismus ziehen.

Im vorigen Kapitel haben wir gesehen, dass zu jeder $r$-gliedrigen Gruppe $X_1f\cdots X_rf$ eine gewisse lineare homogene Gruppe gehört, die adjungirte Gruppe, wie wir sie genannt haben. Aus den Relationen, welche zwischen den infinitesimalen Transformationen der adjungirten Gruppe bestehen (vgl. Kap. 16, S. 275), erhellt unmittelbar, dass die Gruppe $X_1f\cdots X_rf$ mit ihrer Adjungirten isomorph ist; holoedrisch isomorph sind allerdings beide Gruppen nur dann, wenn die Gruppe $X_1f\cdots X_rf$ keine ausgezeichnete infinitesimale Transformation enthält, denn nur in diesem Falle ist die adjungirte Gruppe $r$-gliedrig, während sie sonst stets weniger als $r$ Parameter enthält. Also:

**D17 · p. 294**

**Theorem 51.** *Zu jeder $r$-gliedrigen Gruppe $X_1f\cdots X_rf$ giebt es eine isomorphe lineare homogene Gruppe, nämlich die zugehörige adjungirte Gruppe; holoedrisch isomorph ist dieselbe mit der Gruppe $X_1f\cdots X_rf$ nur dann, wenn diese letztere keine ausgezeichnete infinitesimale Transformation enthält.*

Wir gehen hier nicht auf die Frage ein, ob auch zu jeder solchen $r$-gliedrigen Gruppe, welche ausgezeichnete infinitesimale Transformationen enthält, eine holoedrisch isomorphe lineare homogene Gruppe angegeben werden kann. Doch wollen wir an Beispielen zeigen, dass dies jedenfalls in vielen Fällen möglich ist, auch wenn die gegebene $r$-gliedrige Gruppe ausgezeichnete infinitesimale Transformationen enthält.

**D18 · p. 294**

Die $r$-gliedrige Gruppe $X_1f\cdots X_rf$ enthalte gerade $r-m$ unabhängige ausgezeichnete infinitesimale Transformationen, und es seien $X_1f\cdots X_rf$ so gewählt, dass $X_{m+1}f\cdots X_rf$ ausgezeichnete Transformationen sind; dann bestehen zwischen $X_1f\cdots X_rf$ Relationen von der Form:

$$
\begin{gathered}(X_\mu X_\nu)=c_{\mu\nu1}\,X_1f+\cdots+c_{\mu\nu r}\,X_rf,\\ (X_\mu X_{m+k})=(X_{m+k}X_{m+j})=0\\(\mu,\nu=1\cdots m;\ k,j=1\cdots r-m).\end{gathered}
$$

In der zugehörigen adjungirten Gruppe $E_1f\cdots E_rf$ giebt es nur $m$ unabhängige infinitesimale Transformationen: $E_1f\cdots E_mf$, während $E_{m+1}f\cdots E_rf$ identisch verschwinden, es sind daher $E_1f\cdots E_mf$ durch die Relationen verknüpft:

$$
(E_\mu E_\nu)=c_{\mu\nu1}\,E_1f+\cdots+c_{\mu\nu m}\,E_mf.
$$

**D19 · pp. 294–295**

Verschwinden nun insbesondere alle $c_{\mu,\nu,m+1}\cdots c_{\mu\nu r}$, so lässt sich stets eine $r$-gliedrige lineare homogene Gruppe angeben, welche mit der Gruppe $X_1f\cdots X_rf$ holoedrisch isomorph ist. In diesem Falle erzeugen nämlich $X_1f\cdots X_mf$ an und für sich eine $m$-gliedrige Gruppe, zu welcher die Gruppe $E_1f\cdots E_mf$ holoedrisch isomorph ist. Setzen wir daher

$$
E_{m+1}f=e_{r+1}\frac{\partial f}{\partial e_{r+1}},\quad\cdots,\quad E_rf=e_{2r-m}\frac{\partial f}{\partial e_{2r-m}},
$$

so erzeugen offenbar die $r$ unabhängigen infinitesimalen Transformationen:

$$
E_1f\cdots E_mf,\quad E_{m+1}f\cdots E_rf
$$

eine lineare homogene zu der Gruppe $X_1f\cdots X_rf$ holoedrisch isomorphe Gruppe.

**D20 · p. 295**

Aber auch in solchen Fällen, wo nicht alle $c_{\mu,\nu,m+1}\cdots c_{\mu\nu r}$ verschwinden, kann man oft leicht eine holoedrisch isomorphe lineare homogene Gruppe angeben. Als Beispiel diene die dreigliedrige Gruppe $X_1f,X_2f,X_3f$:

$$
(X_1X_2)=X_3f,\qquad(X_1X_3)=(X_2X_3)=0,
$$

welche eine ausgezeichnete infinitesimale Transformation enthält, nämlich $X_3f$; sie ist holoedrisch isomorph mit der linearen homogenen Gruppe:

$$
E_1f=a_3\frac{\partial f}{\partial a_1},\qquad E_2f=a_1\frac{\partial f}{\partial a_2},\qquad E_3f=a_3\frac{\partial f}{\partial a_2}.
$$

**D21 · p. 295**

Die Constanten $c_{iks}$ in den Gleichungen:

$$
(X_iX_k)=\sum_{s=1}^r c_{iks}\,X_sf\tag{1}
$$

befriedigen, wie wir in Kap. 9, S. 170 gesehen haben, die Relationen:

$$
\begin{cases}c_{iks}+c_{kis}=0,\\ \displaystyle\sum_{v=1}^r\{c_{ikv}c_{vjs}+c_{kjv}c_{vis}+c_{jiv}c_{vks}\}=0\end{cases}\qquad(i,k,j,s=1\cdots r).\tag{5}
$$

**D22 · p. 295**

Mit Hülfe dieser Relationen gelang es uns in Kap. 16, S. 274 zu beweisen, dass die $r$ infinitesimalen Transformationen

$$
E_\mu f=\sum_{k,j=1}^r c_{j\mu k}e_j\frac{\partial f}{\partial e_k}\qquad(\mu=1\cdots r)\tag{6}
$$

der zur Gruppe $X_1f\cdots X_rf$ adjungirten Gruppe paarweise in den Beziehungen

$$
(E_\mu E_\nu)=\sum_{s=1}^r c_{\mu\nu s}\,E_sf\tag{7}
$$

stehen.

**D23 · p. 295**

Bei diesem Beweise der Relationen (7) haben wir aber weiter nichts benutzt als den Umstand, dass die $c_{iks}$ den Gleichungen (5) genügten, namentlich haben wir davon keinen Gebrauch gemacht, dass wir die Existenz von $r$ unabhängigen infinitesimalen Transformationen $X_1f\cdots X_rf$ kannten, welche durch die Relationen (1) verknüpft waren. Durch die citirten Entwickelungen ist daher bewiesen, dass die $r$ infinitesimalen Transformationen (6) stets dann in den Beziehungen (7) stehen, wenn die $c_{iks}$ den Gleichungen (5) genügen.

**D24 · p. 296**

Kennen wir demnach ein System von $c_{iks}$, welches die Relationen (5) befriedigt, so können wir sofort $r$ lineare homogene infinitesimale Transformationen $E_1f\cdots E_rf$ angeben, die Transformationen (6) nämlich, welche paarweise in den Beziehungen:

$$
(E_iE_k)=\sum_{s=1}^r c_{iks}\,E_sf
$$

stehen.

**D25 · p. 296**

Selbstverständlich erzeugen die so erhaltenen infinitesimalen Transformationen $E_1f\cdots E_rf$ eine Gruppe und zwar eine mit $r$ oder weniger Parametern; eine mit gerade $r$ Parametern erzeugen sie offenbar nur dann, wenn sie von einander unabhängig sind, wenn es also unmöglich ist, die Gleichungen:

$$
g_1\,E_1f+\cdots+g_r\,E_rf=0
$$

oder die $r^2$ damit äquivalenten Gleichungen:

$$
g_1c_{j1k}+g_2c_{j2k}+\cdots+g_rc_{jrk}=0\qquad(j,k=1\cdots r)
$$

durch $r$ nicht sämmtlich verschwindende Grössen $g_1\cdots g_r$ zu befriedigen.

Damit haben wir das

**D26 · pp. 296–297**

**Theorem 52.** [F2] *Wenn die Constanten $c_{iks}$ $(i,k,s=1\cdots r)$ solche Werthe besitzen, dass alle Relationen von der Form:*

$$
\begin{cases}c_{iks}+c_{kis}=0,\\ \displaystyle\sum_{v=1}^r\{c_{ikv}c_{vjs}+c_{kjv}c_{vis}+c_{jiv}c_{vks}\}=0\end{cases}\qquad(i,k,j,s=1\cdots r)\tag{5}
$$

*befriedigt sind, so stehen die $r$ linearen homogenen infinitesimalen Transformationen:*

$$
E_\mu f=\sum_{k,j=1}^r c_{j\mu k}e_j\frac{\partial f}{\partial e_k}\qquad(\mu=1\cdots r),
$$

*paarweise in den Beziehungen:*

$$
(E_iE_k)=\sum_{s=1}^r c_{iks}\,E_sf\qquad(i,k=1\cdots r)
$$

*und erzeugen daher eine lineare homogene Gruppe. Sind die $c_{iks}$ insbesondere so beschaffen, dass nicht alle $r$-reihigen Determinanten verschwinden, deren Horizontalreihen die Form haben:*

$$
\left|c_{j1k}\quad c_{j2k}\quad\cdots\quad c_{jrk}\right|\qquad(j,k=1\cdots r),
$$

*so sind $E_1f\cdots E_rf$ unabhängige infinitesimale Transformationen und erzeugen eine $r$-gliedrige Gruppe, deren Zusammensetzung durch das System der $c_{iks}$ bestimmt wird, und welche keine ausgezeichnete infinitesimale Transformation enthält. In allen andern Fällen hat die von $E_1f\cdots E_rf$ erzeugte Gruppe weniger als $r$ Parameter.*

**D27 · p. 297**

**§81.** Die Ergebnisse des vorigen Paragraphen legen die Vermuthung nahe, dass überhaupt jedes System von $c_{iks}$, welches die Relationen (5) befriedigt, die Zusammensetzung gewisser $r$-gliedriger Gruppen darstellt. Diese Vermuthung entspricht der Wahrheit, es gilt wirklich der folgende

**D28 · p. 297**

**Satz 1.** *Besitzen die Constanten $c_{iks}$ $(i,k,s=1\cdots r)$ solche Werthe, dass die Relationen:*

$$
\begin{cases}c_{iks}+c_{kis}=0,\\ \displaystyle\sum_{v=1}^r\{c_{ikv}c_{vjs}+c_{kjv}c_{vis}+c_{jiv}c_{vks}\}=0\end{cases}\qquad(i,k,j,s=1\cdots r)\tag{5}
$$

*erfüllt sind, so giebt es stets in einem Raume von geeigneter Dimensionenzahl $r$ unabhängige infinitesimale Transformationen $X_1f\cdots X_rf$, welche paarweise in den Beziehungen*

$$
(X_iX_k)=\sum_{s=1}^r c_{iks}\,X_sf
$$

*stehen und daher eine $r$-gliedrige Gruppe von der Zusammensetzung $c_{iks}$ erzeugen.*

**D29 · p. 297**

Wir unterdrücken den Beweis für diesen wichtigen Satz einstweilen, um nicht zu weit abschweifen zu müssen, und werden diesen Beweis erst im nächsten Abschnitte bringen. Doch werden wir natürlich bis dahin von dem Satze so wenig als möglich Gebrauch machen.

Aus dem Satze 1 geht hervor, dass der Inbegriff aller möglichen Zusammensetzungen von $r$-gliedrigen Gruppen durch den Inbegriff aller Systeme von $c_{iks}$, welche die Gleichungen (5) befriedigen, dargestellt wird. Kennt man alle solchen Systeme von $c_{iks}$, so kennt man damit zugleich alle Zusammensetzungen von $r$-gliedrigen Gruppen.

**D30 · pp. 297–298**

Nun aber giebt es, wie wir auf S. 291 gesehen haben, im Allgemeinen unendlich viele Systeme von $c_{iks}$, welche ein und dieselbe Zusammensetzung darstellen; ist ein System von $c_{iks}$ gegeben, das eine Zusammensetzung darstellt, so findet man alle Systeme $c'_{iks}$, welche dieselbe Zusammensetzung darstellen, vermittelst der Gleichungen (4), unter den $h_{kj}$ willkürliche Parameter verstanden. Wenn man daher alle Systeme von $c_{iks}$ kennt, welche den Gleichungen (5) genügen, so bedarf es noch einer besonderen Untersuchung, um festzustellen, welche von diesen Systemen verschiedene Zusammensetzungen darstellen. Um diese Untersuchung durchführen zu können, müssen wir zunächst die Gleichungen (4) etwas näher betrachten.

**D31 · p. 298**

Sehen wir für den Augenblick davon ab, dass die $c_{iks}$ durch Relationen verknüpft sind; betrachten wir vielmehr die $c_{iks}$ und ebenso die $c'_{iks}$ als von einander unabhängige Veränderliche. Es wird sich zeigen, dass bei Zugrundelegung dieser Auffassung die Gleichungen (4) eine continuirliche Transformationsgruppe in den Veränderlichen $c_{iks}$ und mit den Parametern $h_{kj}$ darstellen.

Um die eben behauptete Eigenschaft der Gleichungen (4) zu beweisen, werden wir direkt zwei Transformationen (4) oder, was dasselbe ist, zwei Transformationen:

$$
\sum_{\pi=1}^r h_{\pi s}c'_{ik\pi}=\sum_{j,\pi=1}^r h_{ij}h_{k\pi}c_{j\pi s}\qquad(i,k,s=1\cdots r)\tag{3}
$$

nach einander ausführen.

**D32 · p. 298**

Zuerst gehen wir also vermöge der Transformation (3) von den $c_{iks}$ zu den $c'_{iks}$ über und sodann von den $c'_{iks}$ zu den $c''_{iks}$ vermöge der Transformation:

$$
\sum_{\pi=1}^r h'_{\pi s}c''_{ik\pi}=\sum_{j,\pi=1}^r h'_{ij}h'_{k\pi}c'_{j\pi s}.\tag{3'}
$$

Auf diese Weise erhalten wir eine neue Transformation, deren Gleichungen sich ergeben, wenn die $c'_{iks}$ aus (3) und (3') weggeschafft werden. Zu beweisen ist, dass diese neue Transformation die Form hat:

$$
\sum_{\pi=1}^r h''_{\pi s}c''_{ik\pi}=\sum_{j,\pi=1}^r h''_{ij}h''_{k\pi}c'_{j\pi s},\tag{3''}
$$

wo die $h''$ Functionen der $h$ und der $h'$ allein sind.

**D33 · pp. 298–299**

Wir multipliciren (3') mit $h_{s\sigma}$ und summiren nach $s$; dann bekommen wir:

$$
\sum_{\pi,s=1}^r h'_{\pi s}h_{s\sigma}c''_{ik\pi}=\sum_{j,\pi,s=1}^r h'_{ij}h'_{k\pi}h_{s\sigma}c'_{j\pi s},
$$

oder wegen (3):

$$
\sum_{\pi,s=1}^r h'_{\pi s}h_{s\sigma}c''_{ik\pi}=\sum_{j,\pi,\tau,\rho=1}^r h'_{ij}h'_{k\pi}h_{j\tau}h_{\pi\rho}c_{\tau\rho\sigma}.
$$

Das ist die besprochene neue Transformation; sie verwandelt sich in (3''), wenn gesetzt wird:

$$
h''_{\pi\sigma}=\sum_{s=1}^r h'_{\pi s}h_{s\sigma}.
$$

Damit ist bewiesen, dass die Transformationen (4) wirklich eine Gruppe bilden.

**D34 · p. 299**

Wir behaupten nun, dass die Transformationen dieser Gruppe das Gleichungensystem (5) invariant lassen.

Es seien die $c_{iks}$ ein System von Constanten, welches die Relationen (5) befriedigt, welches also nach Satz 1 die Zusammensetzung einer gewissen $r$-gliedrigen Gruppe darstellt. Dann stellt, wie wir wissen, das System der $c'_{iks}$, welches durch die Gleichungen (4) bestimmt wird, ebenfalls eine Zusammensetzung dar, nämlich dieselbe Zusammensetzung wie jenes System der $c_{iks}$; folglich genügen auch die $c'_{iks}$ Relationen von der Form (5). Die Transformationen (4) führen demnach jedes Werthsystem $c_{iks}$, welches (5) erfüllt, in ein Werthsystem $c'_{iks}$ von derselben Beschaffenheit über, das heisst, sie lassen das System der Gleichungen (5) invariant, was eben unsere Behauptung war.

**D35 · p. 299**

Deuten wir nunmehr die $r^3$ Veränderlichen $c_{iks}$ als Punktcoordinaten in einem Raume von $r^3$ Dimensionen.

In diesem Raume wird durch die Gleichungen (5) eine gewisse Mannigfaltigkeit $M$ ausgeschieden, welche bei den Transformationen der Gruppe (4) invariant bleibt. Jeder Punkt von $M$ — so können wir sagen — stellt eine Zusammensetzung $r$-gliedriger Gruppen dar, und umgekehrt wird jede mögliche Zusammensetzung $r$-gliedriger Gruppen durch gewisse Punkte von $M$ dargestellt. Zwei verschiedene Punkte von $M$ stellen ein und dieselbe Zusammensetzung dar, wenn es in der Gruppe (4) eine Transformation giebt, welche den einen Punkt in den andern überführt.

**D36 · p. 299**

Ist daher $P$ irgend ein Punkt von $M$, so fällt der Inbegriff aller Lagen, welche $P$ bei den Transformationen der Gruppe (4) annimmt, zusammen mit dem Inbegriff aller Punkte, welche dieselbe Zusammensetzung darstellen wie $P$. Wir wissen von früher her (Kap. 14, S. 225), dass dieser Inbegriff von Punkten eine bei der Gruppe (4) invariante Mannigfaltigkeit bildet und zwar eine sogenannte kleinste invariante Mannigfaltigkeit.

Hieraus ergiebt sich, dass man folgendes Verfahren einzuschlagen hat, um alle verschiedenen Zusammensetzungen $r$-gliedriger Gruppen zu finden:

**D37 · pp. 299–300**

Man bestimme alle auf $M$ gelegenen kleinsten Mannigfaltigkeiten, welche bei der Gruppe (4) invariant bleiben; auf jeder solchen Mannigfaltigkeit wähle man irgend einen Punkt $c_{iks}$: die Werthsysteme $c_{iks}$, welche zu den gewählten Punkten gehören, stellen dann alle verschiedenen Zusammensetzungen $r$-gliedriger Gruppen dar.

Da die endlichen Gleichungen der Gruppe (4) vorliegen, so ist die Bestimmung der kleinsten invarianten Mannigfaltigkeiten als eine ausführbare Operation zu betrachten; sie erfordert blos die Auflösung algebraischer Gleichungen.

Wir haben hiermit das

**D38 · p. 300**

**Theorem 53.** *Die Bestimmung aller wesentlich verschiedenen Zusammensetzungen von $r$-gliedrigen Gruppen erfordert blos algebraische Operationen.*

### Original footnotes

**F1 · p. 293, after the comparison with substitution theory.** Camille Jordan, Traité des substitutions, Paris 1870.

**F2 · p. 296, at Theorem 52.** Lie, Archiv for Math. og Nat. Bd. 1, S. 192, Christiania 1876.

### Independent English translation: Chapter 17 introduction and complete §§80–81

**E01 · p. 289**

**Chapter 17. Composition and isomorphism.**

Many questions about an $r$-parameter group $X_1f\cdots X_rf$ can be answered using only the constants $c_{iks}$ in the relations

$$
(X_iX_k)=\sum_{s=1}^r c_{iks}\,X_sf.
$$

For example, we have seen that determining all subgroups of $X_1f\cdots X_rf$ depends only on the constants $c_{iks}$. The same holds for determining all types of subgroups (see Theorem 33, p. 210, and Chapter 16, pp. 280 and 281).

**E02 · p. 289**

It follows that the constants $c_{iks}$ themselves already reflect certain properties of $X_1f\cdots X_rf$. We give the collection of these properties a special name: the group's *composition*. Thus we say that *the constants $c_{iks}$ in the relations*

$$
(X_iX_k)=\sum_{s=1}^r c_{iks}\,X_sf.\tag{1}
$$

*determine the composition of the $r$-parameter group $X_1f\cdots X_rf$*.

**E03 · pp. 289–290**

**§80.** The system of constants $c_{iks}$ determining the composition of the $r$-parameter group $X_1f\cdots X_rf$ is itself not uniquely determined. In general, the individual $c_{iks}$ take different numerical values when $X_1f\cdots X_rf$ are replaced by any other $r$ independent infinitesimal transformations $e_1X_1f+\cdots+e_rX_rf$ of the same group.

Consequently, two different systems of constants $c_{iks}$ may represent the composition of the same group. How can we recognize when they do?

**E04 · p. 290**

We begin with the relations

$$
(X_iX_k)=\sum_{s=1}^r c_{iks}\,X_sf\qquad(i,k=1\cdots r),\tag{1}
$$

among $r$ specified independent infinitesimal transformations $X_1f\cdots X_rf$ of our group. We seek the general form of the relations joining any $r$ independent infinitesimal transformations $\mathfrak{X}_1f\cdots\mathfrak{X}_rf$ of $X_1f\cdots X_rf$.

If those relations have the form

$$
(\mathfrak{X}_i\mathfrak{X}_k)=\sum_{s=1}^r c'_{iks}\,\mathfrak{X}_sf.\tag{2}
$$

then $c'_{iks}$ is the most general system of constants representing the composition of $X_1f\cdots X_rf$. We therefore need only calculate $c'_{iks}$.

**E05 · p. 290**

Since $\mathfrak{X}_1f\cdots\mathfrak{X}_rf$ may be any independent infinitesimal transformations of $X_1f\cdots X_rf$, we have

$$
\mathfrak{X}_kf=\sum_{j=1}^r h_{kj}\,X_jf\qquad(k=1\cdots r),
$$

where the constants $h_{kj}$ may take any values for which the determinant

$$
D=\sum\pm h_{11}\cdots h_{rr}
$$

does not vanish.

**E06 · p. 290**

Direct calculation gives

$$
(\mathfrak{X}_i\mathfrak{X}_k)=\sum_{j,\pi=1}^r h_{ij}h_{k\pi}(X_jX_\pi)=\sum_{j,\pi,s=1}^r h_{ij}h_{k\pi}c_{j\pi s}\,X_sf;
$$

while (2) gives

$$
(\mathfrak{X}_i\mathfrak{X}_k)=\sum_{\pi,s=1}^r h_{\pi s}c'_{ik\pi}\,X_sf.
$$

Comparing these two expressions for $(\mathfrak{X}_i\mathfrak{X}_k)$ and using independence of $X_1f\cdots X_rf$, we obtain

$$
\sum_{\pi=1}^r h_{\pi s}c'_{ik\pi}=\sum_{j,\pi=1}^r h_{ij}h_{k\pi}c_{j\pi s}\qquad(s=1\cdots r).\tag{3}
$$

**E07 · p. 291**

Under our assumptions these equations can be solved for $c'_{ik\pi}$, giving

$$
c'_{ik\rho}=\frac1D\sum_{s=1}^r\left\{\frac{\partial D}{\partial h_{\rho s}}\sum_{j,\pi=1}^r h_{ij}h_{k\pi}\right\}c_{j\pi s}\qquad(i,k,\rho=1\cdots r).\tag{4}
$$

This finds the general form of all systems of constants determining the composition of $X_1f\cdots X_rf$. It also gives, at least theoretically, a way to decide whether a proposed system $\bar c_{iks}$ determines the composition of $X_1f\cdots X_rf$: it does so exactly when the parameters $h_{kj}$ in (4) can be chosen so that $c'_{iks}=\bar c_{iks}$.

**E08 · p. 291**

Given *two* $r$-parameter groups, we can compare their compositions. The preceding calculations let us decide whether their compositions are the same or different. The numbers of variables on which the two groups act need not enter this comparison.

*We call two $r$-parameter groups with the same composition equally composed.*

**E09 · p. 291**

Suppose

$$
X_kf=\sum_{i=1}^n \xi_{ki}(x_1\cdots x_n)\frac{\partial f}{\partial x_i}\qquad(k=1\cdots r)
$$

are independent infinitesimal transformations of one $r$-parameter group, and

$$
Y_kf=\sum_{\mu=1}^m\eta_{k\mu}(y_1\cdots y_m)\frac{\partial f}{\partial y_\mu}\qquad(k=1\cdots r)
$$

are independent infinitesimal transformations of a second, and suppose also that

$$
(X_iX_k)=\sum_{s=1}^r c_{iks}\,X_sf,
$$

*Then the two groups are equally composed exactly when, among the infinitesimal transformations $e_1Y_1f+\cdots+e_rY_rf$ of the second group, one can choose $r$ independent transformations $\mathfrak{Y}_1f\cdots\mathfrak{Y}_rf$ such that*

$$
(\mathfrak{Y}_i\mathfrak{Y}_k)=\sum_{s=1}^r c_{iks}\,\mathfrak{Y}_sf
$$

*hold identically.*

**E10 · p. 292**

If the relations among $Y_1f\cdots Y_rf$ have the form

$$
(Y_iY_k)=\sum_{s=1}^r\bar c_{iks}\,Y_sf,
$$

we can say that the groups are equally composed exactly when the parameters $h_{kj}$ in (4) can be chosen so that each $c'_{iks}$ equals the corresponding $\bar c_{iks}$.

We can also compare the compositions of groups having different numbers of parameters. The general notion of *isomorphism* makes this possible.

**E11 · p. 292**

*We call the $r$-parameter group $X_1f\cdots X_rf$, with*

$$
(X_iX_k)=\sum_{s=1}^r c_{iks}\,X_sf
$$

*isomorphic to the $(r-q)$-parameter group $Y_1f\cdots Y_{r-q}f$ if one can select $r$ infinitesimal transformations in that $(r-q)$-parameter group,*

$$
\mathfrak{Y}_kf=h_{k1}\,Y_1f+\cdots+h_{k,r-q}\,Y_{r-q}f\qquad(k=1\cdots r)
$$

*such that not all minors of order $(r-q)$ of the matrix*

$$
\left|\begin{matrix}h_{11}&\cdots&h_{1,r-q}\\ \vdots&&\vdots\\ h_{r1}&\cdots&h_{r,r-q}\end{matrix}\right|
$$

*vanish, and such that the relations*

$$
(\mathfrak{Y}_i\mathfrak{Y}_k)=\sum_{s=1}^r c_{iks}\,\mathfrak{Y}_sf
$$

*hold identically.*

**E12 · pp. 292–293**

Suppose isomorphism in this sense holds and $\mathfrak{Y}_1f\cdots\mathfrak{Y}_rf$ have already been chosen as described. Assign to every infinitesimal transformation $e_1X_1f+\cdots+e_rX_rf$ of the $r$-parameter group the transformation

$$
e_1\,\mathfrak{Y}_1f+\cdots+e_r\,\mathfrak{Y}_rf
$$

of the $(r-q)$-parameter group, whatever the values of $e_1\cdots e_r$. Then the following holds: if $\Upsilon_1f$ in the $(r-q)$-parameter group corresponds to $\Xi_1f$ in the other group, and $\Upsilon_2f$ similarly corresponds to $\Xi_2f$, the transformation $(\Upsilon_1\Upsilon_2)$ always corresponds to $(\Xi_1\Xi_2)$. We express this more briefly by saying that the assignment of infinitesimal transformations *relates the groups isomorphically to one another*. The relation is completely determined once we know that $X_1f\cdots X_rf$ correspond, respectively, to $\mathfrak{Y}_1f\cdots\mathfrak{Y}_rf$.

**E13 · p. 293**

We distinguish *holoedric* and *meroedric isomorphism*. The former occurs when the number $q$ in the definition of isomorphism is zero; the latter occurs when $q$ is positive. Accordingly, we say that the two groups are related holoedrically or meroedrically isomorphically, as appropriate.

Equal composition is a special case of isomorphism: two equally composed groups are always holoedrically isomorphic, and conversely.

**E14 · p. 293**

For example, the following two groups are meroedrically isomorphic:

$$
\frac{\partial f}{\partial x_1},\quad x_1\frac{\partial f}{\partial x_1},\quad x_1^2\frac{\partial f}{\partial x_1},\quad\frac{\partial f}{\partial x_2}
$$

and

$$
\frac{\partial f}{\partial y_1},\quad y_1\frac{\partial f}{\partial y_1},\quad y_1^2\frac{\partial f}{\partial y_1},
$$

with four and three parameters, respectively. One such relation assigns to the four infinitesimal transformations of the first,

$$
\begin{aligned}X_1f&=\frac{\partial f}{\partial x_1},&X_2f&=x_1\frac{\partial f}{\partial x_1},\\X_3f&=x_1^2\frac{\partial f}{\partial x_1},&X_4f&=\frac{\partial f}{\partial x_1}+\frac{\partial f}{\partial x_2}\end{aligned}
$$

the following four transformations of the second:

$$
\begin{aligned}\mathfrak{Y}_1f&=\frac{\partial f}{\partial y_1},&\mathfrak{Y}_2f&=y_1\frac{\partial f}{\partial y_1},\\\mathfrak{Y}_3f&=y_1^2\frac{\partial f}{\partial y_1},&\mathfrak{Y}_4f&=\frac{\partial f}{\partial y_1}\end{aligned}
$$

**E15 · p. 293**

Substitution theory also speaks of isomorphic groups, although its definition appears to differ from the one given here. [F1] Later, in Chapter 21 on the parameter group, we shall see that our definition nevertheless yields exactly the notion obtained by transferring the definition from substitution theory directly to the theory of finite continuous groups.

**E16 · p. 294**

We first draw some simple consequences from our definition of isomorphism.

The preceding chapter associated a certain linear homogeneous group with every $r$-parameter group $X_1f\cdots X_rf$: its adjoint group, as we called it. The relations among the adjoint group's infinitesimal transformations (Chapter 16, p. 275) immediately show that $X_1f\cdots X_rf$ is isomorphic to its adjoint group. The isomorphism is holoedric only when $X_1f\cdots X_rf$ contains no distinguished infinitesimal transformation. Only then does the adjoint group have $r$ parameters; otherwise it always has fewer than $r$. Thus:

**E17 · p. 294**

**Theorem 51.** *Every $r$-parameter group $X_1f\cdots X_rf$ has an isomorphic linear homogeneous group, namely its adjoint group. The latter is holoedrically isomorphic to $X_1f\cdots X_rf$ only when the original group contains no distinguished infinitesimal transformation.*

We do not consider here whether every $r$-parameter group containing distinguished infinitesimal transformations also has a holoedrically isomorphic linear homogeneous group. Examples will show, however, that this is possible in many cases even when the given $r$-parameter group contains distinguished infinitesimal transformations.

**E18 · p. 294**

Suppose the $r$-parameter group $X_1f\cdots X_rf$ contains exactly $r-m$ independent distinguished infinitesimal transformations. Choose $X_1f\cdots X_rf$ so that $X_{m+1}f\cdots X_rf$ are distinguished. The relations among $X_1f\cdots X_rf$ then have the form

$$
\begin{gathered}(X_\mu X_\nu)=c_{\mu\nu1}\,X_1f+\cdots+c_{\mu\nu r}\,X_rf,\\ (X_\mu X_{m+k})=(X_{m+k}X_{m+j})=0\\(\mu,\nu=1\cdots m;\ k,j=1\cdots r-m).\end{gathered}
$$

The associated adjoint group $E_1f\cdots E_rf$ has only $m$ independent infinitesimal transformations, $E_1f\cdots E_mf$, while $E_{m+1}f\cdots E_rf$ vanish identically. Consequently $E_1f\cdots E_mf$ satisfy

$$
(E_\mu E_\nu)=c_{\mu\nu1}\,E_1f+\cdots+c_{\mu\nu m}\,E_mf.
$$

**E19 · pp. 294–295**

If, in particular, all $c_{\mu,\nu,m+1}\cdots c_{\mu\nu r}$ vanish, one can always give an $r$-parameter linear homogeneous group holoedrically isomorphic to $X_1f\cdots X_rf$. In this case $X_1f\cdots X_mf$ themselves generate an $m$-parameter group holoedrically isomorphic to $E_1f\cdots E_mf$. Hence, setting

$$
E_{m+1}f=e_{r+1}\frac{\partial f}{\partial e_{r+1}},\quad\cdots,\quad E_rf=e_{2r-m}\frac{\partial f}{\partial e_{2r-m}},
$$

the $r$ independent infinitesimal transformations

$$
E_1f\cdots E_mf,\quad E_{m+1}f\cdots E_rf
$$

generate a linear homogeneous group holoedrically isomorphic to $X_1f\cdots X_rf$.

**E20 · p. 295**

Even when some $c_{\mu,\nu,m+1}\cdots c_{\mu\nu r}$ do not vanish, it is often easy to give a holoedrically isomorphic linear homogeneous group. Consider, for example, the three-parameter group $X_1f,X_2f,X_3f$ with

$$
(X_1X_2)=X_3f,\qquad(X_1X_3)=(X_2X_3)=0,
$$

It has one distinguished infinitesimal transformation, $X_3f$, and is holoedrically isomorphic to the linear homogeneous group

$$
E_1f=a_3\frac{\partial f}{\partial a_1},\qquad E_2f=a_1\frac{\partial f}{\partial a_2},\qquad E_3f=a_3\frac{\partial f}{\partial a_2}.
$$

**E21 · p. 295**

As we saw in Chapter 9, p. 170, the constants $c_{iks}$ in the equations

$$
(X_iX_k)=\sum_{s=1}^r c_{iks}\,X_sf\tag{1}
$$

satisfy

$$
\begin{cases}c_{iks}+c_{kis}=0,\\ \displaystyle\sum_{v=1}^r\{c_{ikv}c_{vjs}+c_{kjv}c_{vis}+c_{jiv}c_{vks}\}=0\end{cases}\qquad(i,k,j,s=1\cdots r).\tag{5}
$$

**E22 · p. 295**

Using these relations, we proved in Chapter 16, p. 274, that the $r$ infinitesimal transformations

$$
E_\mu f=\sum_{k,j=1}^r c_{j\mu k}e_j\frac{\partial f}{\partial e_k}\qquad(\mu=1\cdots r)\tag{6}
$$

of the group adjoint to $X_1f\cdots X_rf$ satisfy pairwise

$$
(E_\mu E_\nu)=\sum_{s=1}^r c_{\mu\nu s}\,E_sf\tag{7}
$$

**E23 · p. 295**

The proof of (7) used only the fact that $c_{iks}$ satisfy (5). In particular, it did not use the known existence of $r$ independent infinitesimal transformations $X_1f\cdots X_rf$ related by (1). Those calculations therefore prove that the $r$ infinitesimal transformations (6) satisfy (7) whenever $c_{iks}$ satisfy (5).

**E24 · p. 296**

Thus, given any system $c_{iks}$ satisfying (5), we can immediately give $r$ linear homogeneous infinitesimal transformations $E_1f\cdots E_rf$, namely (6), satisfying pairwise

$$
(E_iE_k)=\sum_{s=1}^r c_{iks}\,E_sf
$$

**E25 · p. 296**

The resulting transformations $E_1f\cdots E_rf$ generate a group with at most $r$ parameters. They generate one with exactly $r$ parameters only when they are independent: that is, when the equation

$$
g_1\,E_1f+\cdots+g_r\,E_rf=0
$$

or, equivalently, the following $r^2$ equations,

$$
g_1c_{j1k}+g_2c_{j2k}+\cdots+g_rc_{jrk}=0\qquad(j,k=1\cdots r)
$$

cannot be satisfied by $r$ quantities $g_1\cdots g_r$ that are not all zero.

We have therefore obtained

**E26 · pp. 296–297**

**Theorem 52.** [F2] *Suppose the constants $c_{iks}$, $(i,k,s=1\cdots r)$, have values satisfying all relations of the form*

$$
\begin{cases}c_{iks}+c_{kis}=0,\\ \displaystyle\sum_{v=1}^r\{c_{ikv}c_{vjs}+c_{kjv}c_{vis}+c_{jiv}c_{vks}\}=0\end{cases}\qquad(i,k,j,s=1\cdots r)\tag{5}
$$

*Then the $r$ linear homogeneous infinitesimal transformations*

$$
E_\mu f=\sum_{k,j=1}^r c_{j\mu k}e_j\frac{\partial f}{\partial e_k}\qquad(\mu=1\cdots r),
$$

*satisfy pairwise*

$$
(E_iE_k)=\sum_{s=1}^r c_{iks}\,E_sf\qquad(i,k=1\cdots r)
$$

*and hence generate a linear homogeneous group. If, in particular, $c_{iks}$ are such that not all determinants of order $r$ vanish whose rows have the form*

$$
\left|c_{j1k}\quad c_{j2k}\quad\cdots\quad c_{jrk}\right|\qquad(j,k=1\cdots r),
$$

*then $E_1f\cdots E_rf$ are independent and generate an $r$-parameter group whose composition is determined by $c_{iks}$ and which contains no distinguished infinitesimal transformation. In every other case, the group generated by $E_1f\cdots E_rf$ has fewer than $r$ parameters.*

**E27 · p. 297**

**§81.** The preceding section suggests that every system $c_{iks}$ satisfying (5) represents the composition of some $r$-parameter groups. This conjecture is correct: the following proposition holds.

**E28 · p. 297**

**Proposition 1.** *If the constants $c_{iks}$, $(i,k,s=1\cdots r)$, satisfy*

$$
\begin{cases}c_{iks}+c_{kis}=0,\\ \displaystyle\sum_{v=1}^r\{c_{ikv}c_{vjs}+c_{kjv}c_{vis}+c_{jiv}c_{vks}\}=0\end{cases}\qquad(i,k,j,s=1\cdots r)\tag{5}
$$

*then, in a space of suitable dimension, there always exist $r$ independent infinitesimal transformations $X_1f\cdots X_rf$ satisfying pairwise*

$$
(X_iX_k)=\sum_{s=1}^r c_{iks}\,X_sf
$$

*and hence generating an $r$-parameter group with composition $c_{iks}$.*

**E29 · p. 297**

For now we omit the proof of this important proposition to avoid too lengthy a digression; we shall give it only in the next part. Until then we shall, of course, use the proposition as little as possible.

Proposition 1 shows that all possible compositions of $r$-parameter groups are represented by all systems $c_{iks}$ satisfying (5). Knowing every such system $c_{iks}$ therefore means knowing all compositions of $r$-parameter groups.

**E30 · pp. 297–298**

As we saw on p. 291, however, infinitely many systems $c_{iks}$ generally represent the same composition. Given one such system $c_{iks}$, all systems $c'_{iks}$ representing the same composition are obtained from (4), treating $h_{kj}$ as arbitrary parameters. Thus, even if we know all systems $c_{iks}$ satisfying (5), a further investigation is required to determine which represent different compositions. To carry this out, we must examine (4) more closely.

**E31 · p. 298**

For the moment, disregard the relations among $c_{iks}$ and treat $c_{iks}$, and likewise $c'_{iks}$, as independent variables. We shall show that, with this interpretation, (4) describes a continuous transformation group in the variables $c_{iks}$ with parameters $h_{kj}$.

To prove this property of (4), we directly perform two transformations of that form successively, or equivalently two transformations

$$
\sum_{\pi=1}^r h_{\pi s}c'_{ik\pi}=\sum_{j,\pi=1}^r h_{ij}h_{k\pi}c_{j\pi s}\qquad(i,k,s=1\cdots r)\tag{3}
$$

**E32 · p. 298**

First (3) takes $c_{iks}$ to $c'_{iks}$; then the transformation

$$
\sum_{\pi=1}^r h'_{\pi s}c''_{ik\pi}=\sum_{j,\pi=1}^r h'_{ij}h'_{k\pi}c'_{j\pi s}.\tag{3'}
$$

takes $c'_{iks}$ to $c''_{iks}$. Eliminating $c'_{iks}$ from (3) and (3') gives the equations of the resulting transformation. We must prove that it has the form

$$
\sum_{\pi=1}^r h''_{\pi s}c''_{ik\pi}=\sum_{j,\pi=1}^r h''_{ij}h''_{k\pi}c'_{j\pi s},\tag{3''}
$$

where $h''$ depend only on $h$ and $h'$.

**E33 · pp. 298–299**

Multiply (3') by $h_{s\sigma}$ and sum over $s$. This gives

$$
\sum_{\pi,s=1}^r h'_{\pi s}h_{s\sigma}c''_{ik\pi}=\sum_{j,\pi,s=1}^r h'_{ij}h'_{k\pi}h_{s\sigma}c'_{j\pi s},
$$

or, using (3),

$$
\sum_{\pi,s=1}^r h'_{\pi s}h_{s\sigma}c''_{ik\pi}=\sum_{j,\pi,\tau,\rho=1}^r h'_{ij}h'_{k\pi}h_{j\tau}h_{\pi\rho}c_{\tau\rho\sigma}.
$$

This is the resulting transformation discussed above. It becomes (3'') on setting

$$
h''_{\pi\sigma}=\sum_{s=1}^r h'_{\pi s}h_{s\sigma}.
$$

Thus the transformations (4) do indeed form a group.

**E34 · p. 299**

We now claim that this group's transformations leave the system (5) invariant.

Let $c_{iks}$ satisfy (5). By Proposition 1, this system represents the composition of some $r$-parameter group. As we know, the system $c'_{iks}$ determined by (4) also represents a composition, indeed the same composition as $c_{iks}$. Hence $c'_{iks}$ likewise satisfies relations of the form (5). The transformations (4) therefore send every system $c_{iks}$ satisfying (5) to a system $c'_{iks}$ with the same property. In other words, they leave (5) invariant, as claimed.

**E35 · p. 299**

Now interpret the $r^3$ variables $c_{iks}$ as point coordinates in a space of dimension $r^3$.

Equations (5) select a certain manifold $M$ in this space, invariant under the transformations (4). We may say that each point of $M$ represents a composition of $r$-parameter groups; conversely, every possible composition of $r$-parameter groups is represented by certain points of $M$. Two different points of $M$ represent the same composition when a transformation in (4) carries one point to the other.

**E36 · p. 299**

For any point $P$ of $M$, the set of positions reached from $P$ under (4) is therefore exactly the set of points representing the same composition as $P$. We know from Chapter 14, p. 225, that this set of points forms an invariant manifold for (4), a so-called smallest invariant manifold.

Consequently, to find all different compositions of $r$-parameter groups, one should proceed as follows.

**E37 · pp. 299–300**

Determine all smallest manifolds contained in $M$ that remain invariant under (4), and choose a point $c_{iks}$ on each. The systems $c_{iks}$ belonging to these chosen points then represent all different compositions of $r$-parameter groups.

Since the finite equations of (4) are available, finding these smallest invariant manifolds is to be regarded as a feasible operation; it requires only the solution of algebraic equations.

We have thus obtained

**E38 · p. 300**

**Theorem 53.** *Determining all essentially different compositions of $r$-parameter groups requires only algebraic operations.*

### Translated original footnotes

**F1 · p. 293, after the comparison with substitution theory.** Camille Jordan, *Traité des substitutions*, Paris, 1870.

**F2 · p. 296, at Theorem 52.** Lie, *Archiv for Math. og Nat.*, Volume 1, p. 192, Christiania, 1876.

### Reading notes

1. **Composition and constant basis changes (D01–D10).** “Composition” describes the Lie algebra up to an invertible constant change of basis. It does not mean composition of two individual transformations. If $\mathfrak{X}_i=\sum_j h_{ij}X_j$ and $D=\det H\ne0$, expansion of the commutator gives (3). Multiplication by $H^{-1}$ in the output index gives (4), since $(H^{-1})_{s\rho}=D^{-1}\partial D/\partial h_{\rho s}$. The printed formula places $c_{j\pi s}$ after the closing brace, although $j,\pi$ are summed inside it. This placement is retained in both languages. The unambiguous intended formula is

   $$
   c'_{ik\rho}=\frac1D\sum_{s,j,\pi=1}^r
   \frac{\partial D}{\partial h_{\rho s}}h_{ij}h_{k\pi}c_{j\pi s}.
   $$

   Both $\mathfrak{X}$ and $\mathfrak{Y}$ are changed bases, and the two actions may have different numbers of spatial variables. Equal composition determines their local parameter group up to isomorphism; it does not provide a coordinate transformation conjugating the two spatial actions. Theorem 5.1 in the modern preceding lesson proves the precise analytic local group statement.

2. **Historical isomorphism includes a kernel (D11–D15).** The full-rank rectangular matrix in D11 defines a surjective linear map from the $r$-dimensional source algebra to the $(r-q)$-dimensional target algebra. Its printed vertical bars delimit the rectangular array; the rank condition concerns its square minors, rather than a determinant of the whole rectangular matrix. The displayed bracket relations say exactly that this map preserves brackets. Its constant kernel has dimension $q$ and is an ideal: if $\rho(u)=0$, then $\rho([v,u])=[\rho(v),0]=0$. Holoedric means $q=0$, hence a Lie algebra isomorphism in today's terminology. Meroedric means $q>0$, hence a quotient homomorphism; it has no connection with meromorphic functions. For the projective example in D14, put $P=\partial_{x_1}$, $D=x_1\partial_{x_1}$, $Q=x_1^2\partial_{x_1}$ and $Z=\partial_{x_2}$. The listed fourth basis field is $P+Z$. The map forgets $Z$ and sends $P,D,Q$ to the corresponding fields in $y_1$. Its kernel is the central line spanned by $X_4-X_1=Z$. This directly verifies the relations, including those involving the fourth field. Theorem 5.2 of the preceding lesson supplies the local group quotient. The original bracket on p. 292 correctly prints $Y_s$ on its right-hand side, as the enlarged scan confirms.

3. **Distinguished transformations and the adjoint sign (D16–D18, D22–D26).** An “ausgezeichnete infinitesimale Transformation” here commutes with every generator, so its algebra element belongs to the centre. Formula (6) has coefficient $c_{j\mu k}$, with the generator index in the middle. By antisymmetry it is the linear vector field $E_{e_\mu}(a)=-[e_\mu,a]$. For linear fields $X_A(a)=Aa$, the vector-field bracket is $X_{BA-AB}$, which reverses the matrix commutator. The minus sign therefore makes $[E_u,E_v]=E_{[u,v]}$, using Jacobi. The kernel is precisely the centre. All these fields vanish at the origin, even when they are independent over constants; no full pointwise rank at the origin is asserted. Proposition 2.1 of the modern lesson proves this calculation without assuming a group already exists.

4. **The special central extension must split (D19).** The vanishing of every central-output coefficient $c_{\mu,\nu,m+1},\ldots,c_{\mu\nu r}$ says that the chosen span of $X_1,\ldots,X_m$ is a subalgebra. With the full centre as the complementary span, the algebra is a direct sum $\mathfrak h\oplus Z(\mathfrak g)$. The subalgebra $\mathfrak h$ has zero centre: an element central in $\mathfrak h$ also commutes with the complementary central summand, so it would lie in $\mathfrak h\cap Z(\mathfrak g)=0$. Its adjoint fields are consequently independent. The additional central dilations are independent fields on new coordinates and commute with those adjoint fields and with one another. This proves the special faithful linear realization. The printed added variables are $e_{r+1},\ldots,e_{2r-m}$; their indices are retained. A mere vector-space complement to the centre need not be a subalgebra, and then this construction is not available.

5. **A nonsplit linear example (D20).** For the displayed three fields,

   $$
   [a_3\partial_{a_1},a_1\partial_{a_2}]=a_3\partial_{a_2},\qquad
   [a_3\partial_{a_1},a_3\partial_{a_2}]
   =[a_1\partial_{a_2},a_3\partial_{a_2}]=0.
   $$

   A constant relation has $\partial_{a_1}$ coefficient $\lambda_1a_3$, forcing $\lambda_1=0$, and $\partial_{a_2}$ coefficient $\lambda_2a_1+\lambda_3a_3$, forcing the other two constants to vanish. Thus the realization is faithful although every field vanishes at the origin. It realizes the Heisenberg centre nontrivially; the adjoint realization would lose it. This single example does not establish faithful finite-dimensional linear realizability for every Lie algebra. The general local existence proof in this lesson does not require that stronger statement.

6. **The rank criterion is a coefficient rank (D25–D26).** Form the constant matrix with $r^2$ rows, indexed by $(j,k)$, and $r$ columns, indexed by $\mu$, whose entries are $c_{j\mu k}$. A vector $g$ is in its kernel exactly when $\sum_\mu g_\mu E_\mu=0$ as a field. Thus a nonzero minor of order $r$ means that the centre is zero. Theorem 52 then applies the converse second theorem to these fields; the finite-evaluation argument in the preceding lesson handles their possible pointwise dependence. If the matrix has rank less than $r$, its kernel is the centre, and the adjoint group has that smaller effective dimension. The theorem's phrase “no distinguished infinitesimal transformation” follows from the zero centre of the realized algebra in the full-rank case.

7. **The general theorem is stated and deferred (D27–D29).** Satz 1 allows every antisymmetric set of constants satisfying Jacobi, including every possible centre. It asks for fields independent over constants in a space of suitable dimension; it does not prescribe a faithful linear model. The following paragraph explicitly postpones the proof to the next part of the treatise. “Abschnitt” is accordingly translated as “part,” without attributing the proof to the immediately following chapter. The independent modern proof in this lesson supplies an analytic coframe by an entire power series, proves the Maurer–Cartan equation by the radial and Bianchi identities, and integrates its dual constant-bracket frame. Thus the historical proof deferral does not leave the lesson's local third theorem unproved. The later function-group proof belongs to the separately assigned Volume II reading.

8. **Basis-change orbits and the Jacobi locus (D30–D38).** For an arbitrary coefficient array $c$, define a bilinear operation on a fixed vector space by those coefficients. Formula (4) simply expresses this operation in another basis, whether or not it satisfies Jacobi. Applying $H$ and then $H'$ gives $H''=H'H$, exactly the order in D33; the identity matrix and inverse matrix give the identity and inverse transformations. The original (3″) in D32 prints $c'_{j\pi s}$ on the right, and both languages retain that prime. Eliminating the intermediate array instead gives $c_{j\pi s}$ there, as the following expanded calculation in D33 confirms; this is the intended composition formula. A change of basis carries the antisymmetry and Jacobi expressions to the corresponding expressions in the new basis, so their simultaneous vanishing is preserved. This proves invariance algebraically without needing the deferred existence theorem that the historical argument invokes. The set $M$ is the algebraic set cut out by the skew and quadratic Jacobi equations. It may be singular; the word “Mannigfaltigkeit” in this passage should not be read as a proof that all of $M$ is a regular manifold. Its change-of-basis orbits are precisely the isomorphism classes of Lie algebra structures. Theorem 53 is retained as written. A precise algebraic test for two arrays to belong to the same orbit asks for the polynomial equations (3) and $t\det H=1$ to have a solution. The orbit description does not by itself provide a finite list of types, a finite effective classification procedure in every dimension, or a globally regular quotient space.

## Historical reading: existence through function groups

**Source and complete scope.** Sophus Lie and Friedrich Engel, *Theorie der Transformationsgruppen*, Volume II (1890), complete Chapter 17 introduction and §75, printed pp. 294–298. The reading ends after Proposition 3, before Chapter 18 on p. 298. The original footnote on p. 297 is retained. The preceding Division IV introduction on pp. 292–293 has been read for context. The original is public domain; this transcription, independently written English translation and editorial notes are dedicated to CC0.

**Editorial method.** Historical spelling, paragraph order, original theorem and proposition numbers, and repeated equation tags are retained. Line divisions are joined, display spacing and summation layout are normalized, and running heads are omitted. The Greek generator index is written $\kappa$. “Independent functions” means functional independence on a regular local chart. “Independent transformations” means independence over constants unless the passage explicitly discusses independent linear PDE. Lie's earlier proof dependencies remain visible.

### German transcription: complete Chapter 17 and §75

**D01 · p. 294 · Chapter 17 introduction**

**Kapitel 17. Beweis der Existenz von Gruppen mit gegebener Zusammensetzung.**

Wir denken uns eine Zusammensetzung gegeben, also $r^3$ Constanten $c_{i\kappa s}$, welche die Gleichungen:
$$
\left\{\begin{aligned}
c_{i\kappa s}+c_{\kappa is}&=0,\\
\sum_{\nu=1}^r\{c_{i\kappa\nu}c_{\nu js}+c_{\kappa j\nu}c_{\nu is}+c_{ji\nu}c_{\nu\kappa s}\}&=0
\end{aligned}\right.
\qquad(i,\kappa,j,s=1\cdots r).\tag{1}
$$
erfüllen.

**D02 · p. 294 · Chapter 17 introduction**

Wir behaupten, dass es in einer geeigneten Zahl $m$ von Veränderlichen $y_1\cdots y_m$ $r$ unabhängige infinitesimale Punkttransformationen:
$$
Y_\kappa(f)=\sum_{\mu=1}^m\eta_{\kappa\mu}(y_1\cdots y_m)\frac{\partial f}{\partial y_\mu}\qquad(\kappa=1\cdots r)
$$
giebt, welche in den Beziehungen:
$$
Y_i(Y_\kappa(f))-Y_\kappa(Y_i(f))=\sum_{s=1}^r c_{i\kappa s}Y_s(f)\qquad(i,\kappa=1\cdots r).\tag{2}
$$
stehen und somit eine $r$-gliedrige Gruppe von der Zusammensetzung $c_{i\kappa s}$ erzeugen.

**D03 · p. 294 · §75**

**§75.**

Zunächst werden wir nachweisen, dass es bei geeigneter Wahl von $n$ stets $r$ unabhängige Functionen: $\varphi_1(x,p)\cdots\varphi_r(x,p)$ der $2n$ Veränderlichen $x_1\cdots x_n$, $p_1\cdots p_n$ giebt, welche in den Beziehungen:
$$
(\varphi_i\varphi_\kappa)_{xp}=\sum_{s=1}^r c_{i\kappa s}\varphi_s=w_{i\kappa}(\varphi_1\cdots\varphi_r)\qquad(i,\kappa=1\cdots r).\tag{3}
$$
stehen.

**D04 · pp. 294–295 · §75**

Nach Theorem 37, S. 241 ist zur Existenz von $r$ derartigen Functionen: $\varphi_1(x,p)\cdots\varphi_r(x,p)$ nothwendig und hinreichend, dass die $w_{i\kappa}(\varphi_1\cdots\varphi_r)$ die Relationen:
$$
\left\{\begin{aligned}
w_{i\kappa}+w_{\kappa i}&=0,\\
\sum_{\nu=1}^r\left\{
w_{\nu j}\frac{\partial w_{i\kappa}}{\partial\varphi_\nu}
+w_{\nu i}\frac{\partial w_{\kappa j}}{\partial\varphi_\nu}
+w_{\nu\kappa}\frac{\partial w_{ji}}{\partial\varphi_\nu}\right\}&=0
\end{aligned}\right.
\qquad(i,\kappa,j=1\cdots r).\tag{4}
$$
identisch erfüllen. Von diesen Relationen sind nun aber die in der ersten Reihe wegen: $c_{i\kappa s}+c_{\kappa is}=0$ augenscheinlich erfüllt und die in der zweiten Reihe nehmen bei wirklicher Ausrechnung die Form an:

**D05 · p. 295 · §75**

$$
\sum_{s=1}^r\varphi_s\cdot\sum_{\nu=1}^r\{c_{i\kappa\nu}c_{\nu js}+c_{\kappa j\nu}c_{\nu is}+c_{ji\nu}c_{\nu\kappa s}\}=0,
$$
werden also vermöge (1) ebenfalls zu Identitäten. Folglich giebt es sicher $r$ unabhängige Functionen: $\varphi_1(x,p)\cdots\varphi_r(x,p)$ von der angegebenen Beschaffenheit und wir haben den

**D06 · p. 295 · §75**

**Satz 1.** *Sind $r^3$ Constanten $c_{i\kappa s}$ vorgelegt, welche die Gleichungen:*
$$
\left\{\begin{aligned}
c_{i\kappa s}+c_{\kappa is}&=0,\\
\sum_{\nu=1}^r\{c_{i\kappa\nu}c_{\nu js}+c_{\kappa j\nu}c_{\nu is}+c_{ji\nu}c_{\nu\kappa s}\}&=0
\end{aligned}\right.
\qquad(i,\kappa,j,s=1\cdots r).\tag{1}
$$
*erfüllen, so ist es nach geeigneter Wahl von $n$ stets möglich solche unabhängige Functionen: $\varphi_1(x,p)\cdots\varphi_r(x,p)$ der $2n$ Veränderlichen $x_1\cdots x_n$, $p_1\cdots p_n$ zu finden, welche in den Beziehungen:*
$$
(\varphi_i\varphi_\kappa)_{xp}=\sum_{s=1}^r c_{i\kappa s}\varphi_s\qquad(i,\kappa=1\cdots r).\tag{3}
$$
*stehen und zwar ist zur Bestimmung von derartigen Functionen: $\varphi_1\cdots\varphi_r$ höchstens die Integration gewöhnlicher Differentialgleichungen erforderlich.*

**D07 · p. 295 · §75**

Jetzt seien: $\varphi_1(x,p)\cdots\varphi_r(x,p)$ unabhängige Functionen, welche in den Beziehungen (3) stehen.

Wir betrachten die $r$ infinitesimalen Transformationen:
$$
(\varphi_1f)_{xp}\cdots(\varphi_rf)_{xp}
$$
in den Veränderlichen $x_1\cdots x_n$, $p_1\cdots p_n$. Diese Transformationen sind nach S. 260, Satz 7 von einander unabhängig, denn $\varphi_1\cdots\varphi_r$ sind unabhängige Functionen der $x,p$ und durch keine lineare Relation:
$$
c_1\varphi_1+\cdots+c_r\varphi_r+c=0
$$
mit constanten Coefficienten verknüpft.

**D08 · pp. 295–296 · §75**

Setzen wir nun für den Augenblick:
$$
(\varphi_\kappa f)_{xp}=A_\kappa(f)\qquad(\kappa=1\cdots r),
$$
so kommt:
$$
\begin{aligned}
A_i(A_\kappa(f))-A_\kappa(A_i(f))
&=(\varphi_i(\varphi_\kappa f))-(\varphi_\kappa(\varphi_i f))\\
&=((\varphi_i\varphi_\kappa)f)
=\sum_{s=1}^r c_{i\kappa s}(\varphi_sf).
\end{aligned}
$$
oder:

**D09 · p. 296 · §75**

$$
A_i(A_\kappa(f))-A_\kappa(A_i(f))=\sum_{s=1}^r c_{i\kappa s}A_s(f)\qquad(i,\kappa=1\cdots r).
$$
Demnach sind $A_1(f)\cdots A_r(f)$ $r$ unabhängige infinitesimale Transformationen in den Veränderlichen $x_1\cdots x_n$, $p_1\cdots p_n$, welche eine $r$-gliedrige Gruppe von der Zusammensetzung $c_{i\kappa s}$ erzeugen.

Damit ist die im Eingang des Kapitels aufgestellte Behauptung bewiesen; denn wählen wir die dort genannte Zahl $m=2n$ und schreiben wir: $x_1\cdots x_n$, $p_1\cdots p_n$ an Stelle von $y_1\cdots y_m$, so brauchen wir blos zu setzen: $Y_\kappa f=A_\kappa f$.

**D10 · p. 296 · §75**

Die $r$-gliedrige Functionengruppe: $\varphi_1(x,p)\cdots\varphi_r(x,p)$ besitzt eine $(2n-r)$-gliedrige Polargruppe: $\psi_1(x,p)\cdots\psi_{2n-r}(x,p)$. Wir führen die $2n-r$ unabhängigen Functionen: $\psi_1\cdots\psi_{2n-r}$ dieser Polargruppe nebst $r$ geeigneten Grössen $z_1\cdots z_r$ als neue unabhängige Veränderliche ein, dann erhalten die $r$ infinitesimalen Transformationen:
$$
A_\kappa(f)=(\varphi_\kappa f)_{xp}\qquad(\kappa=1\cdots r)
$$
augenscheinlich die Form:
$$
A_\kappa(f)=\sum_{j=1}^r\xi_{\kappa j}(z_1\cdots z_r,\psi_1\cdots\psi_{2n-r})\frac{\partial f}{\partial z_j}\qquad(\kappa=1\cdots r).
$$

**D11 · p. 296 · §75**

Nun sind die $r$ linearen partiellen Differentialgleichungen:
$$
(\varphi_1f)_{xp}=0,\quad\ldots,\quad(\varphi_rf)_{xp}=0
$$
von einander unabhängig, da $\varphi_1\cdots\varphi_r$ unabhängige Functionen der $x,p$ sind, folglich müssen auch die $r$ linearen partiellen Differentialgleichungen:
$$
\sum_{j=1}^r\xi_{\kappa j}(z_1\cdots z_r,\psi_1\cdots\psi_{2n-r})\frac{\partial f}{\partial z_j}=0\qquad(\kappa=1\cdots r)
$$
von einander unabhängig sein und sie müssen es auch bleiben, wenn man in ihnen die Grössen $\psi_1\cdots\psi_{2n-r}$ nicht mehr als Veränderliche, sondern als willkürliche Constanten ansieht. Hieraus ergiebt sich, dass die $r$ infinitesimalen Transformationen:
$$
\mathfrak A_\kappa(f)=\sum_{j=1}^r\xi_{\kappa j}(z_1\cdots z_r,C_1\cdots C_{2n-r})\frac{\partial f}{\partial z_j}\qquad(\kappa=1\cdots r)
$$
in den Veränderlichen $z_1\cdots z_r$ von einander unabhängig sind, zugleich ist klar, dass diese infinitesimalen Transformationen eine $r$-gliedrige Gruppe in $z_1\cdots z_r$ erzeugen und zwar nothwendig eine einfach transitive Gruppe. Also:

**D12 · p. 297 · §75**

**Theorem 48.** *Sind $r^3$ Constanten:*
$$
c_{i\kappa s}\qquad(i,\kappa,s=1\cdots r),
$$
*vorgelegt, welche die Relationen:*
$$
\left\{\begin{aligned}
c_{i\kappa s}+c_{\kappa is}&=0,\\
\sum_{\nu=1}^r\{c_{i\kappa\nu}c_{\nu js}+c_{\kappa j\nu}c_{\nu is}+c_{ji\nu}c_{\nu\kappa s}\}&=0
\end{aligned}\right.
\qquad(i,\kappa,j,s=1\cdots r).\tag{1}
$$
*erfüllen, so ist es immer möglich durch Integration von gewöhnlichen Differentialgleichungen eine $r$-gliedrige einfach transitive Gruppe von Punkttransformationen aufzustellen, welche die Zusammensetzung $c_{i\kappa s}$ besitzt.* [F1]

**D13 · p. 297 · §75**

Ist eine einfach transitive Gruppe von Punkttransformationen bestimmt, welche die Zusammensetzung $c_{i\kappa s}$ hat, so findet man nach Abschn. I, Kap. 22 alle anderen Gruppen von Punkttransformationen mit dieser Zusammensetzung ebenfalls durch Integration gewöhnlicher Differentialgleichungen. Mithin gilt der

**D14 · p. 297 · §75**

**Satz 2.** *Hat man $r^3$ Constanten:*
$$
c_{i\kappa s}\qquad(i,\kappa,s=1\cdots r),
$$
*welche die Relationen:*
$$
\left\{\begin{aligned}
c_{i\kappa s}+c_{\kappa is}&=0,\\
\sum_{\nu=1}^r\{c_{i\kappa\nu}c_{\nu js}+c_{\kappa j\nu}c_{\nu is}+c_{ji\nu}c_{\nu\kappa s}\}&=0
\end{aligned}\right.
\qquad(i,\kappa,j,s=1\cdots r).\tag{1}
$$
*erfüllen, so giebt es unbegrenzt viele Gruppen von Punkttransformationen, welche die Zusammensetzung $c_{i\kappa s}$ haben. Alle diese Gruppen können jedenfalls durch Integration gewöhnlicher Differentialgleichungen gefunden werden.*

**D15 · pp. 297–298 · §75**

Da in den Relationen (3) die $w_{i\kappa}$ homogene Functionen erster Ordnung von $\varphi_1\cdots\varphi_r$ sind, so giebt es dem Theoreme 38, S. 248 zufolge insbesondere auch $r$ unabhängige Functionen: $h_1(x,p)\cdots h_r(x,p)$, die in den $p$ homogen von erster Ordnung sind und in den Beziehungen:
$$
(h_i h_\kappa)_{xp}=\sum_{s=1}^r c_{i\kappa s}h_s\qquad(i,\kappa=1\cdots r)
$$
stehen. Dann sind:
$$
(h_1f)_{xp}\cdots(h_rf)_{xp}
$$

**D16 · p. 298 · §75**

offenbar infinitesimale *homogene* Berührungstransformationen und erzeugen eine $r$-gliedrige Gruppe mit der Zusammensetzung $c_{i\kappa s}$. Also:

**D17 · p. 298 · §75 conclusion**

**Satz 3.** *Hat man $r^3$ Constanten:*
$$
c_{i\kappa s}\qquad(i,\kappa,s=1\cdots r),
$$
*welche die Relationen:*
$$
\left\{\begin{aligned}
c_{i\kappa s}+c_{\kappa is}&=0,\\
\sum_{\nu=1}^r\{c_{i\kappa\nu}c_{\nu js}+c_{\kappa j\nu}c_{\nu is}+c_{ji\nu}c_{\nu\kappa s}\}&=0
\end{aligned}\right.
\qquad(i,\kappa,j,s=1\cdots r).\tag{1}
$$
*erfüllen, so kann man stets und zwar jedenfalls durch Integration gewöhnlicher Differentialgleichungen $r$ unabhängige infinitesimale homogene Berührungstransformationen:*
$$
B_\kappa(f)=(h_\kappa f)_{xp}\qquad(\kappa=1\cdots r)
$$
*finden, welche in den Beziehungen:*
$$
B_i(B_\kappa(f))-B_\kappa(B_i(f))=\sum_{s=1}^r c_{i\kappa s}B_s(f)\qquad(i,\kappa=1\cdots r)
$$
*stehen und somit eine $r$-gliedrige Gruppe von der Zusammensetzung $c_{i\kappa s}$ erzeugen; die infinitesimalen Transformationen:*
$$
\sum_{\kappa=1}^r e_\kappa(h_\kappa f)=\left(\sum_{\kappa=1}^r e_\kappa h_\kappa,f\right)
$$
*dieser Gruppe sind sämmtlich infinitesimale homogene Berührungstransformationen.*

### Original footnote

**F1 · p. 297, at Theorem 48.** Lie, Verhandlungen der Ges. d. W. zu Christiania 1888; vgl. auch Archiv for Mathematik, Bd. 1, Christiania 1876; Math. Ann., Bd. XVI und Berichte der Kgl. Sächs. Ges. d. W. 1888.

### Independent English translation: complete Chapter 17 and §75

**E01 · p. 294 · Chapter 17 introduction**

**Chapter 17. Proof of the existence of groups with a given composition.**

Suppose a composition is given, that is, $r^3$ constants $c_{i\kappa s}$ satisfying
$$
\left\{\begin{aligned}
c_{i\kappa s}+c_{\kappa is}&=0,\\
\sum_{\nu=1}^r\{c_{i\kappa\nu}c_{\nu js}+c_{\kappa j\nu}c_{\nu is}+c_{ji\nu}c_{\nu\kappa s}\}&=0
\end{aligned}\right.
\qquad(i,\kappa,j,s=1\cdots r).\tag{1}
$$

**E02 · p. 294 · Chapter 17 introduction**

We claim that, in a suitable number $m$ of variables $y_1\cdots y_m$, there are $r$ independent infinitesimal point transformations
$$
Y_\kappa(f)=\sum_{\mu=1}^m\eta_{\kappa\mu}(y_1\cdots y_m)\frac{\partial f}{\partial y_\mu}\qquad(\kappa=1\cdots r)
$$
satisfying
$$
Y_i(Y_\kappa(f))-Y_\kappa(Y_i(f))=\sum_{s=1}^r c_{i\kappa s}Y_s(f)\qquad(i,\kappa=1\cdots r).\tag{2}
$$
and hence generating an $r$-parameter group with composition $c_{i\kappa s}$.

**E03 · p. 294 · §75**

**§75.**

First we shall show that, for a suitable choice of $n$, there are always $r$ independent functions $\varphi_1(x,p)\cdots\varphi_r(x,p)$ of the $2n$ variables $x_1\cdots x_n$, $p_1\cdots p_n$, satisfying
$$
(\varphi_i\varphi_\kappa)_{xp}=\sum_{s=1}^r c_{i\kappa s}\varphi_s=w_{i\kappa}(\varphi_1\cdots\varphi_r)\qquad(i,\kappa=1\cdots r).\tag{3}
$$

**E04 · pp. 294–295 · §75**

By Theorem 37, p. 241, the existence of $r$ such functions $\varphi_1(x,p)\cdots\varphi_r(x,p)$ requires, and is guaranteed by, the identities
$$
\left\{\begin{aligned}
w_{i\kappa}+w_{\kappa i}&=0,\\
\sum_{\nu=1}^r\left\{
w_{\nu j}\frac{\partial w_{i\kappa}}{\partial\varphi_\nu}
+w_{\nu i}\frac{\partial w_{\kappa j}}{\partial\varphi_\nu}
+w_{\nu\kappa}\frac{\partial w_{ji}}{\partial\varphi_\nu}\right\}&=0
\end{aligned}\right.
\qquad(i,\kappa,j=1\cdots r).\tag{4}
$$
for $w_{i\kappa}(\varphi_1\cdots\varphi_r)$. The first row plainly holds because $c_{i\kappa s}+c_{\kappa is}=0$. On expansion, the second row becomes

**E05 · p. 295 · §75**

$$
\sum_{s=1}^r\varphi_s\cdot\sum_{\nu=1}^r\{c_{i\kappa\nu}c_{\nu js}+c_{\kappa j\nu}c_{\nu is}+c_{ji\nu}c_{\nu\kappa s}\}=0,
$$
These too are identities by (1). Thus $r$ independent functions $\varphi_1(x,p)\cdots\varphi_r(x,p)$ of the required kind certainly exist, and we have obtained the following proposition.

**E06 · p. 295 · §75**

**Proposition 1.** *Given $r^3$ constants $c_{i\kappa s}$ satisfying*
$$
\left\{\begin{aligned}
c_{i\kappa s}+c_{\kappa is}&=0,\\
\sum_{\nu=1}^r\{c_{i\kappa\nu}c_{\nu js}+c_{\kappa j\nu}c_{\nu is}+c_{ji\nu}c_{\nu\kappa s}\}&=0
\end{aligned}\right.
\qquad(i,\kappa,j,s=1\cdots r).\tag{1}
$$
*one can, by a suitable choice of $n$, always find independent functions $\varphi_1(x,p)\cdots\varphi_r(x,p)$ of the $2n$ variables $x_1\cdots x_n$, $p_1\cdots p_n$, satisfying*
$$
(\varphi_i\varphi_\kappa)_{xp}=\sum_{s=1}^r c_{i\kappa s}\varphi_s\qquad(i,\kappa=1\cdots r).\tag{3}
$$
*Determining such functions $\varphi_1\cdots\varphi_r$ requires at most the integration of ordinary differential equations.*

**E07 · p. 295 · §75**

Now let $\varphi_1(x,p)\cdots\varphi_r(x,p)$ be independent functions satisfying (3).

Consider the $r$ infinitesimal transformations
$$
(\varphi_1f)_{xp}\cdots(\varphi_rf)_{xp}
$$
in the variables $x_1\cdots x_n$, $p_1\cdots p_n$. By p. 260, Proposition 7, these transformations are independent: $\varphi_1\cdots\varphi_r$ are independent functions of $x,p$ and satisfy no linear relation
$$
c_1\varphi_1+\cdots+c_r\varphi_r+c=0
$$
with constant coefficients.

**E08 · pp. 295–296 · §75**

For the moment put
$$
(\varphi_\kappa f)_{xp}=A_\kappa(f)\qquad(\kappa=1\cdots r),
$$
Then
$$
\begin{aligned}
A_i(A_\kappa(f))-A_\kappa(A_i(f))
&=(\varphi_i(\varphi_\kappa f))-(\varphi_\kappa(\varphi_i f))\\
&=((\varphi_i\varphi_\kappa)f)
=\sum_{s=1}^r c_{i\kappa s}(\varphi_sf).
\end{aligned}
$$
or, equivalently,

**E09 · p. 296 · §75**

$$
A_i(A_\kappa(f))-A_\kappa(A_i(f))=\sum_{s=1}^r c_{i\kappa s}A_s(f)\qquad(i,\kappa=1\cdots r).
$$
Thus $A_1(f)\cdots A_r(f)$ are $r$ independent infinitesimal transformations in the variables $x_1\cdots x_n$, $p_1\cdots p_n$, generating an $r$-parameter group with composition $c_{i\kappa s}$.

This proves the claim at the start of the chapter: choose the number there as $m=2n$, write $x_1\cdots x_n$, $p_1\cdots p_n$ in place of $y_1\cdots y_m$, and simply set $Y_\kappa f=A_\kappa f$.

**E10 · p. 296 · §75**

The $r$-function group $\varphi_1(x,p)\cdots\varphi_r(x,p)$ has a $(2n-r)$-function polar group $\psi_1(x,p)\cdots\psi_{2n-r}(x,p)$. Introduce its $2n-r$ independent functions $\psi_1\cdots\psi_{2n-r}$, together with $r$ suitable quantities $z_1\cdots z_r$, as new independent variables. The $r$ infinitesimal transformations
$$
A_\kappa(f)=(\varphi_\kappa f)_{xp}\qquad(\kappa=1\cdots r)
$$
then plainly take the form
$$
A_\kappa(f)=\sum_{j=1}^r\xi_{\kappa j}(z_1\cdots z_r,\psi_1\cdots\psi_{2n-r})\frac{\partial f}{\partial z_j}\qquad(\kappa=1\cdots r).
$$

**E11 · p. 296 · §75**

The $r$ linear partial differential equations
$$
(\varphi_1f)_{xp}=0,\quad\ldots,\quad(\varphi_rf)_{xp}=0
$$
are independent, since $\varphi_1\cdots\varphi_r$ are independent functions of $x,p$. Hence the $r$ linear partial differential equations
$$
\sum_{j=1}^r\xi_{\kappa j}(z_1\cdots z_r,\psi_1\cdots\psi_{2n-r})\frac{\partial f}{\partial z_j}=0\qquad(\kappa=1\cdots r)
$$
must also be independent, and must remain so when the quantities $\psi_1\cdots\psi_{2n-r}$ in them are treated as arbitrary constants instead of variables. It follows that the $r$ infinitesimal transformations
$$
\mathfrak A_\kappa(f)=\sum_{j=1}^r\xi_{\kappa j}(z_1\cdots z_r,C_1\cdots C_{2n-r})\frac{\partial f}{\partial z_j}\qquad(\kappa=1\cdots r)
$$
in the variables $z_1\cdots z_r$ are independent. These infinitesimal transformations plainly generate an $r$-parameter group in $z_1\cdots z_r$, necessarily a simply transitive group. Thus:

**E12 · p. 297 · §75**

**Theorem 48.** *Given $r^3$ constants*
$$
c_{i\kappa s}\qquad(i,\kappa,s=1\cdots r),
$$
*satisfying*
$$
\left\{\begin{aligned}
c_{i\kappa s}+c_{\kappa is}&=0,\\
\sum_{\nu=1}^r\{c_{i\kappa\nu}c_{\nu js}+c_{\kappa j\nu}c_{\nu is}+c_{ji\nu}c_{\nu\kappa s}\}&=0
\end{aligned}\right.
\qquad(i,\kappa,j,s=1\cdots r).\tag{1}
$$
*one can always construct, by integrating ordinary differential equations, an $r$-parameter simply transitive group of point transformations with composition $c_{i\kappa s}$.* [F1]

**E13 · p. 297 · §75**

Once a simply transitive group of point transformations with composition $c_{i\kappa s}$ has been determined, all other groups of point transformations with this composition can also be found by integrating ordinary differential equations, according to Part I, Chapter 22. Hence the following holds.

**E14 · p. 297 · §75**

**Proposition 2.** *Given $r^3$ constants*
$$
c_{i\kappa s}\qquad(i,\kappa,s=1\cdots r),
$$
*satisfying*
$$
\left\{\begin{aligned}
c_{i\kappa s}+c_{\kappa is}&=0,\\
\sum_{\nu=1}^r\{c_{i\kappa\nu}c_{\nu js}+c_{\kappa j\nu}c_{\nu is}+c_{ji\nu}c_{\nu\kappa s}\}&=0
\end{aligned}\right.
\qquad(i,\kappa,j,s=1\cdots r).\tag{1}
$$
*there are indefinitely many groups of point transformations with composition $c_{i\kappa s}$. All these groups can in any case be found by integrating ordinary differential equations.*

**E15 · pp. 297–298 · §75**

Since the $w_{i\kappa}$ in (3) are homogeneous functions of first degree in $\varphi_1\cdots\varphi_r$, Theorem 38, p. 248, also gives $r$ independent functions $h_1(x,p)\cdots h_r(x,p)$, homogeneous of first degree in the $p$, satisfying
$$
(h_i h_\kappa)_{xp}=\sum_{s=1}^r c_{i\kappa s}h_s\qquad(i,\kappa=1\cdots r)
$$
Then
$$
(h_1f)_{xp}\cdots(h_rf)_{xp}
$$

**E16 · p. 298 · §75**

are plainly infinitesimal *homogeneous* contact transformations, and generate an $r$-parameter group with composition $c_{i\kappa s}$. Thus:

**E17 · p. 298 · §75 conclusion**

**Proposition 3.** *Given $r^3$ constants*
$$
c_{i\kappa s}\qquad(i,\kappa,s=1\cdots r),
$$
*satisfying*
$$
\left\{\begin{aligned}
c_{i\kappa s}+c_{\kappa is}&=0,\\
\sum_{\nu=1}^r\{c_{i\kappa\nu}c_{\nu js}+c_{\kappa j\nu}c_{\nu is}+c_{ji\nu}c_{\nu\kappa s}\}&=0
\end{aligned}\right.
\qquad(i,\kappa,j,s=1\cdots r).\tag{1}
$$
*one can always find, in any case by integrating ordinary differential equations, $r$ independent infinitesimal homogeneous contact transformations*
$$
B_\kappa(f)=(h_\kappa f)_{xp}\qquad(\kappa=1\cdots r)
$$
*satisfying*
$$
B_i(B_\kappa(f))-B_\kappa(B_i(f))=\sum_{s=1}^r c_{i\kappa s}B_s(f)\qquad(i,\kappa=1\cdots r)
$$
*and hence generating an $r$-parameter group with composition $c_{i\kappa s}$. All infinitesimal transformations*
$$
\sum_{\kappa=1}^r e_\kappa(h_\kappa f)=\left(\sum_{\kappa=1}^r e_\kappa h_\kappa,f\right)
$$
*of this group are infinitesimal homogeneous contact transformations.*

### Translated original footnote

**F1 · p. 297, at Theorem 48.** Lie, *Verhandlungen der Ges. d. W. zu Christiania*, 1888; compare also *Archiv for Mathematik*, Volume 1, Christiania, 1876; *Mathematische Annalen*, Volume XVI; and *Berichte der Kgl. Sächs. Ges. d. W.*, 1888.

### Reading notes

1. **The actual realization step (D03–D06).** Theorem 37 is an earlier canonical-function realization theorem. Setting $w_{i\kappa}(\varphi)=\sum_sc_{i\kappa s}\varphi_s$ reduces its skew and Jacobi conditions to the given constant identities. This algebraic reduction is complete in the passage, but the existence of independent functions does rely on that earlier theorem's proof. The modern lesson's Lemmas 6.1–6.2 and Theorem 6.3 supply the needed regular Poisson realization argument, and Proposition 6.4 applies it to these constants. The regular point may be chosen where this linear bracket matrix has maximal rank. It need not be the zero of the coefficient space.

2. **The canonical bracket and its sign (D07–D09).** With Lie's convention,

   $$
   (\varphi f)_{xp}
   =\sum_{\mu=1}^n\left(
   \frac{\partial\varphi}{\partial p_\mu}\frac{\partial f}{\partial x_\mu}
   -\frac{\partial\varphi}{\partial x_\mu}\frac{\partial f}{\partial p_\mu}\right).
   $$

   Thus $(p_\mu f)_{xp}=\partial_{x_\mu}f$ and $(x_\mu f)_{xp}=-\partial_{p_\mu}f$. For $H_\varphi=(\varphi\,\cdot)_{xp}$, canonical Jacobi gives $[H_\varphi,H_\psi]=H_{(\varphi\psi)_{xp}}$. No extra adjoint minus sign is introduced here. Nondegeneracy of the canonical bracket identifies the covector $d\varphi$ with $H_\varphi$. Hence functional independence of the $r$ functions gives pointwise rank $r$ of their Hamiltonian fields, a stronger conclusion than constant independence. A constant function has zero Hamiltonian field, which explains the affine constant $c$ in D07.

3. **The polar group is a system of first integrals (D10–D11).** A polar function satisfies $(\varphi_\kappa\psi)_{xp}=0$ for every $\kappa$. Since the Hamiltonian fields have constant rank $r$ and their brackets close, the complete-system theorem supplies $2n-r$ independent common first integrals. Complete them by $z_1,\ldots,z_r$ to a coordinate system. In these coordinates the fields have no $\partial_\psi$ component, and their $r$-by-$r$ coefficient matrix in the $z$ directions is invertible. Fixing $\psi=C$ retains that invertibility wherever the chosen chart is regular, and retains the bracket relations because the fields never differentiate $C$. This proves the full-rank frame assertion. “Arbitrary constants” means values inside this regular coordinate neighbourhood; no singular or global fibre statement follows. The constant-frame theorem then supplies the simply transitive local group.

4. **What Proposition 2 says (D12–D14).** Theorem 48 concerns a simply transitive realization. The following statement concerns the other spatial actions with that composition, using the previously developed construction in Volume I Chapter 22. It does not claim that different actions are conjugate or that classifying all Lie algebras is a finite algebraic task. Adding passive spatial coordinates already gives indefinitely many realizations if the ambient dimension is allowed to vary. An ordinary differential equation construction here is local and requires regular initial data; it is not an elementary closed formula.

5. **Homogeneity is an additional construction (D15–D17).** Theorem 38 provides realizing Hamiltonians homogeneous of first degree in all momenta. Its proof is an additional step, rather than a consequence of simply naming a function group. The modern lesson's Proposition 6.6 proves the required homogeneous realization directly. From independent $\varphi_i(x,p)$ add a canonical pair $(t,\tau)$ and, on $\tau\ne0$, put $h_i(x,p,t,\tau)=\tau\varphi_i(x,p/\tau)$. Then $(h_i h_j)=\tau(\varphi_i\varphi_j)(x,p/\tau)=\sum_sc_{ijs}h_s$. Fixing $\tau$ shows independence. Each $h_i$ has degree one in $(p,\tau)$, and its Hamiltonian flow preserves the canonical one-form $\sum_\mu p_\mu\,dx_\mu+\tau\,dt$: Cartan's formula and Euler's homogeneous identity give zero Lie derivative. This explains Lie's homogeneous-contact realization and preserves his final Proposition 3 in full.

## Historical reading: the three fundamental theorems and infinitesimal increments

**Source and complete scope.** Sophus Lie and Friedrich Engel, *Theorie der Transformationsgruppen*, Volume III (1893), complete Chapter 25 introduction and §§107–108, printed pp. 545–557. Section 107 begins on p. 546 and ends on p. 549; §108 begins there and ends on p. 557, immediately before §109 on p. 558. The complete original domain footnote on p. 552 is retained. The Division VI introduction on pp. 544–545 has been read for context. The original is public domain; this transcription, independent English translation and editorial notes are CC0.

**Editorial method.** Historical spelling, paragraph sequence and all original equation numbers, including repetitions, are retained. Broken lines are joined; running heads, signatures and ornamental dividers are omitted. The old indexed summation symbols are written as ordinary sums with explicit lower indices. The Fraktur argument is written $\mathfrak x$, the dummy index in (12'') is $\tau$, and the inverse-equation coefficients are $\vartheta$. The distinction between $X_jf$ and $X_j'f$ is retained.

### German transcription: Chapter 25 introduction and §§107–108

**D01 · p. 545 · Chapter 25 introduction**

**Kapitel 25. Die Fundamentalsätze der Gruppentheorie.**

Wünscht man einen Ueberblick über die Sätze zu haben, auf denen die ganze Theorie der endlichen continuirlichen Gruppen aufgebaut ist, so unterscheidet man am Besten drei Sätze, die füglich als die drei Fundamentalsätze der Gruppentheorie bezeichnet werden können.

Jeder dieser drei Fundamentalsätze ist ein Doppelsatz, das heisst er besteht eigentlich aus zwei Sätzen, von denen aber jedesmal der eine die Umkehrung des andern ist.

**D02 · pp. 545–546 · Chapter 25 introduction**

Der erste Fundamentalsatz sagt aus, dass jede $r$-gliedrige Gruppe gewissen Differentialgleichungen von ganz besonderer Beschaffenheit, nämlich den sogenannten grundlegenden Differentialgleichungen genügt und dass umgekehrt jede Schaar von $\infty^r$ Transformationen, die derartige Differentialgleichungen erfüllt und ausserdem noch die identische Transformation enthält, eine $r$-gliedrige Gruppe bildet.

**D03 · p. 546 · Chapter 25 introduction**

Der zweite Fundamentalsatz sagt aus, dass jede $r$-gliedrige Gruppe mit paarweise inversen Transformationen von $r$ unabhängigen infinitesimalen Transformationen: $X_1f\ldots X_rf$ erzeugt ist, die paarweise in Beziehungen von der Form:
$$
(X_iX_k)=\sum_{s=1}^r c_{iks}X_sf\qquad(i,k=1\ldots r).\tag{A}
$$
stehen, und dass umgekehrt $r$ unabhängige infinitesimale Transformationen, die in diesen Beziehungen stehen, stets eine $r$-gliedrige Gruppe mit paarweise inversen Transformationen erzeugen.

**D04 · p. 546 · Chapter 25 introduction**

Der dritte Fundamentalsatz endlich sagt aus, dass die $r^3$ Constanten $c_{iks}$, die in den Gleichungen (A) auftreten, gewisse Relationen erfüllen und dass umgekehrt zu jedem gegebenen System von $r^3$ Constanten $c_{iks}$, das die betreffenden Relationen erfüllt, $r$ unabhängige infinitesimale Transformationen: $X_1f\ldots X_rf$ gefunden werden können, die gerade in den Beziehungen (A) stehen.

**D05 · p. 546 · Chapter 25 introduction**

Keiner dieser drei Fundamentalsätze ist entbehrlich, wenn man ein vollständiges Gebäude der Gruppentheorie errichten will; fragt man dagegen, welcher unter ihnen am häufigsten benutzt wird, so muss man sagen, dass der zweite Fundamentalsatz bei allen gruppentheoretischen Untersuchungen ohne Vergleich die häufigste Anwendung findet. Wir bezeichnen deshalb diesen zweiten Satz wohl auch als den Hauptsatz der ganzen Gruppentheorie.

**D06 · p. 546 · Chapter 25 introduction**

Wir wollen jetzt die drei Fundamentalsätze der Reihe nach etwas eingehender besprechen; es kommt uns dabei hauptsächlich darauf an, den begrifflichen Inhalt dieser Sätze und der früher für sie gelieferten Beweise möglichst durchsichtig zu machen. Wir bemerken jedoch gleich hier, dass wir dabei alle Fragen über die Bereiche, innerhalb deren die auftretenden Functionen definirt sind, bei Seite lassen und betreffs dieser Fragen auf die Entwicklungen des Abschnitts I verweisen.

**D07 · pp. 546–547 · §107**

**§107.** Die Gleichungen:
$$
x_i'=f_i(x_1\ldots x_n;\ a_1\ldots a_r)\qquad(i=1\ldots n).\tag{1}
$$
mit den $r$ wesentlichen Parametern: $a_1\ldots a_r$ mögen eine beliebige Schaar von $\infty^r$ verschiedenen Transformationen darstellen, also vorläufig noch nicht gerade eine $r$-gliedrige Gruppe; die Transformation (1) dieser Schaar möge der Kürze wegen mit $S_{(a)}$ bezeichnet werden.

**D08 · p. 547 · §107**

Ist nun $S_{(a+\delta a)}$ eine beliebige, in der Schaar (1) enthaltene Transformation, die der Transformation $S_{(a)}$ unendlich benachbart ist, so kann man $S_{(a+\delta a)}$ auf zwei verschiedene Weisen aus der Transformation $S_{(a)}$ und aus einer infinitesimalen Transformation zusammensetzen, nämlich entweder, indem man zuerst die Transformation $S_{(a)}$ ausführt und dann die infinitesimale Transformation: $S_{(a)}^{-1}S_{(a+\delta a)}$ oder indem man zuerst die infinitesimale Transformation: $S_{(a+\delta a)}S_{(a)}^{-1}$ und dann die Transformation $S_{(a)}$ ausführt.

**D09 · p. 547 · §107**

Durch die beiden unendlich benachbarten Transformationen: $S_{(a)}$ und $S_{(a+\delta a)}$ der Schaar (1) sind demnach zwei infinitesimale Transformationen: $S_{(a)}^{-1}S_{(a+\delta a)}$ und: $S_{(a+\delta a)}S_{(a)}^{-1}$ definirt. Die Identität:
$$
S_{(a)}^{-1}\cdot S_{(a+\delta a)}S_{(a)}^{-1}\cdot S_{(a)}=S_{(a)}^{-1}S_{(a+\delta a)}.
$$
zeigt jedoch, dass diese beiden infinitesimalen Transformationen in einer sehr einfachen Beziehung zu einander stehen: die Transformation: $S_{(a)}^{-1}S_{(a+\delta a)}$ wird nämlich erhalten, wenn man in die Transformation: $S_{(a+\delta a)}S_{(a)}^{-1}$ vermöge der Transformation $S_{(a)}$ neue Veränderliche einführt.

**D10 · p. 547 · §107**

Setzt man voraus, dass sich durch Auflösung der Gleichungen (1) nach $x_1\ldots x_n$ ergiebt:
$$
x_i=F_i(x_1'\ldots x_n';\ a_1\ldots a_r)\qquad(i=1\ldots n),\tag{1'}
$$
so kann man die besprochenen infinitesimalen Transformationen wirklich hinschreiben. Man findet für die infinitesimale Transformation: $S_{(a)}^{-1}S_{(a+\delta a)}$ die Gleichungen:
$$
x_i'=f_i(F_1(x,a)\ldots F_n(x,a);\ a_1+\delta a_1,\ldots,a_r+\delta a_r),
$$
die wegen der Identitäten:
$$
f_i(F_1(x,a)\ldots F_n(x,a);\ a_1\ldots a_r)\equiv x_i
$$
die Gestalt:
$$
x_i'=x_i+\sum_{k=1}^r\delta a_k\left[\frac{\partial f_i(\mathfrak x,a)}{\partial a_k}\right]_{\mathfrak x=F(x,a)}\qquad(i=1\ldots n).\tag{2}
$$
annehmen.

**D11 · pp. 547–548 · §107**

Für die infinitesimale Transformation: $S_{(a+\delta a)}S_{(a)}^{-1}$ findet man ebenso die Gleichungen:
$$
x_i'=F_i(f_1(x,a+\delta a)\ldots f_n(x,a+\delta a);\ a_1\ldots a_r),
$$
aus denen durch Entwicklung nach den unendlich kleinen Grössen: $\delta a_1\ldots\delta a_r$ die Gleichungen:
$$
x_i'=x_i+\sum_{k=1}^r\delta a_k\sum_{\nu=1}^n\frac{\partial f_\nu(x,a)}{\partial a_k}\left[\frac{\partial F_i(\mathfrak x,a)}{\partial\mathfrak x_\nu}\right]_{\mathfrak x=f(x,a)}\qquad(i=1\ldots n)
$$
hervorgehen. Diese Gleichungen kann man aber sehr wesentlich vereinfachen. Aus der Identität:
$$
F_i(f_1(x,a)\ldots f_n(x,a);\ a_1\ldots a_r)\equiv x_i
$$
ergiebt sich nämlich durch Differentiation nach $a_k$:
$$
\sum_{\nu=1}^n\left[\frac{\partial F_i(\mathfrak x,a)}{\partial\mathfrak x_\nu}\right]_{\mathfrak x=f(x,a)}\frac{\partial f_\nu(x,a)}{\partial a_k}+\left[\frac{\partial F_i(\mathfrak x,a)}{\partial a_k}\right]_{\mathfrak x=f(x,a)}=0,
$$
also bekommt die infinitesimale Transformation: $S_{(a+\delta a)}S_{(a)}^{-1}$ die einfache Form:
$$
x_i'=x_i-\sum_{k=1}^r\delta a_k\left[\frac{\partial F_i(\mathfrak x,a)}{\partial a_k}\right]_{\mathfrak x=f(x,a)}\qquad(i=1\ldots n).\tag{3}
$$

**D12 · p. 548 · §107**

Noch schneller hätte man zu dieser Form gelangen können, wenn man beachtet hätte, dass
$$
S_{(a+\delta a)}S_{(a)}^{-1}=\left((S_{(a)}^{-1})^{-1}S_{(a+\delta a)}^{-1}\right)^{-1},
$$
eine Gleichung, die in Formeln gekleidet unmittelbar zu den Gleichungen (3) führt.

**D13 · p. 548 · §107**

Ertheilt man den $a$ bestimmte Werthe, lässt aber die $\delta a$ willkürlich, so stellen die Gleichungen (2) und (3) zwei Schaaren von infinitesimalen Transformationen dar, die der Transformation: $x_i'=f_i(x,a)$ durch die Gleichungen (1) zugeordnet sind. Es ist leicht zu sehen, dass beide Schaaren im Allgemeinen aus je $\infty^{r-1}$ verschiedenen infinitesimalen Transformationen bestehen.

In der That, die infinitesimalen Transformationen (2) sind sämmtlich aus den $r$ infinitesimalen Transformationen:
$$
Z_kf=\sum_{i=1}^n\left[\frac{\partial f_i(\mathfrak x,a)}{\partial a_k}\right]_{\mathfrak x=F(x,a)}\frac{\partial f}{\partial x_i}\qquad(k=1\ldots r)
$$
linear abgeleitet.

**D14 · pp. 548–549 · §107**

Nun aber sind unter den gemachten Voraussetzungen die $r$ Parameter $a_1\ldots a_r$ in den Gleichungen (1) wesentlich, was nach Abschn. I, S. 13 dann und nur dann eintritt, wenn es nicht möglich ist, $r$ solche nicht sämmtlich verschwindende Functionen: $\chi_1\ldots\chi_r$ von den $a$ allein anzugeben, dass die $n$ Gleichungen:
$$
\sum_{k=1}^r\chi_k(a_1\ldots a_r)\frac{\partial f_i(x,a)}{\partial a_k}=0\qquad(i=1\ldots n)
$$
identisch bestehen. Demnach können auch die infinitesimalen Transformationen: $Z_1f\ldots Z_rf$ keine Relation von der Form:
$$
\sum_{k=1}^r\chi_k(a_1\ldots a_r)Z_kf\equiv0
$$
befriedigen, ohne dass $\chi_1\ldots\chi_r$ alle verschwinden. Hierin liegt, dass die $r$ infinitesimalen Transformationen: $Z_1f\ldots Z_rf$ für allgemeine Werthe der $a$ von einander unabhängig sind, und das kommt wieder darauf hinaus, dass die Schaar (2) für jedes Werthsystem: $a_1\ldots a_r$ von allgemeiner Lage aus $\infty^{r-1}$ verschiedenen infinitesimalen Transformationen besteht. Für die Schaar (3) gilt natürlich dasselbe, denn aus ihr wird ja die Schaar (2) erhalten, wenn man vermöge der Transformation $S_{(a)}$ neue Veränderliche einführt.

**D15 · p. 549 · §107**

Wir sehen also, dass die Schaar der $\infty^r$ Transformationen (1) jeder ihrer Transformationen $S_{(a)}$ zwei Schaaren (2) und (3) von je $\infty^{r-1}$ infinitesimalen Transformationen zuordnet. Diese beiden Schaaren sind so beschaffen, dass man jede der Transformation $S_{(a)}$ unendlich benachbarte Transformation $S_{(a+\delta a)}$ der Schaar (1) erhält, indem man entweder zuerst $S_{(a)}$ und dann eine geeignete infinitesimale Transformation der Schaar (2) ausführte oder indem man zuerst eine geeignete infinitesimale Transformation der Schaar (3) und dann die Transformation $S_{(a)}$ ausführt.

Besonders erwähnt sei noch ein Umstand, der aus den soeben angestellten Betrachtungen folgt: es ergiebt sich nämlich, dass umgekehrt, wenn die Schaar (2) für allgemeine Werthe der $a$ $r$ unabhängige infinitesimale Transformationen enthält und also aus $\infty^{r-1}$ verschiedenen infinitesimalen Transformationen besteht, zugleich die Schaar (1) aus $\infty^r$ verschiedenen endlichen Transformationen besteht. Demnach deckt sich die Forderung, dass die Schaar (2) für allgemeine Werthe von $a_1\ldots a_r$ gerade $r$ unabhängige infinitesimale Transformationen enthalte, mit der Forderung, dass die $r$ Parameter $a_1\ldots a_r$ in den Gleichungen (1) wesentlich seien.

**D16 · pp. 549–550 · §108**

**§108.** Nunmehr wollen wir insbesondere voraussetzen, dass die $\infty^r$ Transformationen (1) eine $r$-gliedrige Gruppe bilden, dass also die Gleichungen, die sich aus (1) und:
$$
x_i''=f_i(x_1'\ldots x_n';\ b_1\ldots b_r)\qquad(i=1\ldots n),\tag{4}
$$
durch Fortschaffung der $x'$ ergeben, nämlich die Gleichungen:
$$
x_i''=f_i(f_1(x,a)\ldots f_n(x,a);\ b_1\ldots b_r)\qquad(i=1\ldots n),\tag{5}
$$
die Form:
$$
x_i''=f_i(x_1\ldots x_n;\ c_1\ldots c_r)\qquad(i=1\ldots n),\tag{5'}
$$
erhalten können, wo die $c$ gewisse Functionen:
$$
c_k=\varphi_k(a_1\ldots a_r;\ b_1\ldots b_r)\qquad(k=1\ldots r)\tag{6}
$$
der $a$ und $b$ allein sind. Diese Voraussetzung kann offenbar kürzer durch die symbolische Gleichung:
$$
S_{(a)}S_{(b)}=S_{(c)}.\tag{7}
$$
ausgedrückt werden.

**D17 · p. 550 · §108**

Ertheilen wir den $b$ feste Werthe, während wir die $a$ willkürlich lassen, so bestimmt die linke Seite der Gleichung (7) augenscheinlich eine Schaar von $\infty^r$ Transformationen; von der rechten Seite muss dasselbe gelten, folglich sind die $c_k$ unabhängige Functionen von $a_1\ldots a_r$. Genau so ergiebt sich, dass die $c_k$ auch unabhängige Functionen von $b_1\ldots b_r$ sind: kurz, die Gleichungen (6) sind sowohl nach den $a$ als nach den $b$ auflösbar, ein Ergebniss, das wir in Abschnitt I (auf S. 17 f.) rein analytisch, aber deshalb auch auf ziemlich umständliche Weise abgeleitet haben.

**D18 · p. 550 · §108**

Aus der Gleichung (7) folgt ohne Weiteres die nachstehende:
$$
S_{(a+\delta a)}S_{(b+\delta b)}=S_{(c+\delta c)},
$$
wo die $\delta c$ aus den Gleichungen (6) durch Differentiation gefunden werden. Da die Gleichungen (6) sowohl nach $a_1\ldots a_r$ als nach $b_1\ldots b_r$ auflösbar sind, so können wir die $\delta a$ und die $\delta b$ stets so bestimmen, dass die $\delta c$ alle verschwinden; die betreffenden Werthe der $\delta a$ und $\delta b$ sind dann durch die Gleichungen:
$$
\sum_{j=1}^r\frac{\partial\varphi_k(a,b)}{\partial a_j}\delta a_j+\sum_{j=1}^r\frac{\partial\varphi_k(a,b)}{\partial b_j}\delta b_j=0\qquad(k=1\ldots r)\tag{8}
$$
definirt, und wir haben, sobald diese Gleichungen erfüllt sind:
$$
S_{(a+\delta a)}S_{(b+\delta b)}=S_{(c)}=S_{(a)}S_{(b)}.\tag{9}
$$

**D19 · pp. 550–551 · §108**

Nun aber können wir nach §107 die Transformation $S_{(a+\delta a)}$ erhalten, indem wir zuerst die Transformation $S_{(a)}$ und dann die der Schaar (2) angehörige infinitesimale Transformation: $S_{(a)}^{-1}S_{(a+\delta a)}$ ausführen, und ebenso können wir $S_{(b+\delta b)}$ erhalten, wenn wir zuerst die infinitesimale Transformation: $S_{(b+\delta b)}S_{(b)}^{-1}$ und dann die Transformation: $S_{(b)}$ ausführen. Demnach können wir die Gleichung (9) auch schreiben:
$$
S_{(a)}\cdot(S_{(a)}^{-1}S_{(a+\delta a)}\cdot S_{(b+\delta b)}S_{(b)}^{-1})\cdot S_{(b)}=S_{(a)}S_{(b)},
$$
und hieraus ergiebt sich:
$$
S_{(a)}^{-1}S_{(a+\delta a)}\cdot S_{(b+\delta b)}S_{(b)}^{-1}=1,
$$
das heisst gleich der identischen Transformation. Die beiden infinitesimalen Transformationen: $S_{(a)}^{-1}S_{(a+\delta a)}$ und $S_{(b+\delta b)}S_{(b)}^{-1}$ sind also unter den gemachten Voraussetzungen zu einander invers; da überdies die zu $S_{(b+\delta b)}S_{(b)}^{-1}$ inverse Transformation offenbar die Form hat: $S_{(b-\delta b)}S_{(b)}^{-1}$, so bekommen wir schliesslich:
$$
S_{(a)}^{-1}S_{(a+\delta a)}=S_{(b-\delta b)}S_{(b)}^{-1}.\tag{10}
$$

**D20 · p. 551 · §108**

Die Gleichung (10) ist eine Folge der Gleichung (7), sie enthält aber die Grössen: $c_1\ldots c_r$ nicht mehr. Da nun die $a$ und $b$ an und für sich durch gar keine Relation verknüpft sind, so muss die Gleichung (10) bei beliebiger Wahl von $a_1\ldots a_r$ und $b_1\ldots b_r$ gültig sein für alle Werthe der $\delta a_k$ und $\delta b_k$, die den Gleichungen (8) genügen. Die Gleichungen (8) lassen sich aber sowohl nach den $\delta a_k$ als nach den $\delta b_k$ auflösen und daher entweder in der Form:
$$
\delta b_j=\sum_{k=1}^r\Psi_{jk}(a_1\ldots a_r;\ b_1\ldots b_r)\delta a_k\qquad(j=1\ldots r),\tag{8'}
$$
oder in der Form:
$$
\delta a_j=\sum_{k=1}^r A_{kj}(a_1\ldots a_r;\ b_1\ldots b_r)\delta b_k\qquad(j=1\ldots r).\tag{8''}
$$
schreiben (vgl. Abschn. I, S. 29 und 30); aus ihnen ergiebt sich mithin weder zwischen $\delta b_1\ldots\delta b_r$ allein eine Relation, noch eine zwischen $\delta a_1\ldots\delta a_r$ allein.

**D21 · p. 551 · §108**

Denken wir uns daher für $a_1\ldots a_r$ und $b_1\ldots b_r$ zwei beliebig aber fest gewählte Werthsysteme von allgemeiner Lage eingesetzt und die $\delta a$ und $\delta b$ den Gleichungen (8) unterworfen, sonst jedoch ganz willkürlich, so stellt die linke Seite von (10) die erste der beiden Schaaren von je $\infty^{r-1}$ infinitesimalen Transformationen dar, die nach §107 der Transformation $S_{(a)}$ zugeordnet sind; die rechte Seite von (10) dagegen stellt die zweite der beiden Schaaren von je $\infty^{r-1}$ infinitesimalen Transformationen dar, die der Transformation $S_{(b)}$ zugeordnet sind, denn es liegt auf der Hand, dass die Schaar der $\infty^{r-1}$ infinitesimalen Transformationen $S_{(b-\delta b)}S_{(b)}^{-1}$ mit der Schaar: $S_{(b+\delta b)}S_{(b)}^{-1}$ identisch ist. Demnach sagt die Gleichung (10) aus, dass die erste der zwei $S_{(a)}$ zugeordneten Schaaren von $\infty^{r-1}$ infinitesimalen Transformationen mit der zweiten der zwei $S_{(b)}$ zugeordneten Schaaren zusammenfällt.

**D22 · pp. 551–552 · §108**

Halten wir jetzt blos $b_1\ldots b_r$ fest, während wir $a_1\ldots a_r$ sich ändern lassen, so ergiebt sich aus (10), dass die Schaar der $\infty^{r-1}$ infinitesimalen Transformationen: $S_{(a)}^{-1}S_{(a+\delta a)}$ stets dieselbe bleibt, wie sich auch $a_1\ldots a_r$ ändern mögen. Genau in entsprechender Weise erkennt man, dass auch die Schaar der $\infty^{r-1}$ infinitesimalen Transformationen: $S_{(b-\delta b)}S_{(b)}^{-1}$ sich nicht mit $b_1\ldots b_r$ ändert. Da nun wegen der Gleichung (10) die beiden Schaaren: $S_{(a)}^{-1}S_{(a+\delta a)}$ und $S_{(b-\delta b)}S_{(b)}^{-1}$ zusammenfallen, so liegt hierin zugleich, dass die beiden Schaaren von $\infty^{r-1}$ infinitesimalen Transformationen, die durch die beiden Ausdrücke: $S_{(a)}^{-1}S_{(a+\delta a)}$ und $S_{(a+\delta a)}S_{(a)}^{-1}$ dargestellt werden, mit einander identisch sind und sich beide nicht mit $a_1\ldots a_r$ ändern.[F1]

**D23 · p. 552 · §108**

Wir sehen hieraus, dass alle die Schaaren von $\infty^{r-1}$ infinitesimalen Transformationen, die die Schaar (1) jeder ihrer $\infty^r$ angehörigen Transformationen zuordnet, mit einander identisch sind, sobald die Schaar (1) eine $r$-gliedrige Gruppe bildet. Mit andern Worten:

Zu jeder $r$-gliedrigen Gruppe (1) von $\infty^r$ Punkttransformationen gehört eine ganz bestimmte Schaar von $\infty^{r-1}$ infinitesimalen Transformationen. Diese Schaar besteht aus allen infinitesimalen Transformationen, die aus $r$ gewissen, von einander unabhängigen infinitesimalen Transformationen linear ableitbar sind, und sie ist so beschaffen, dass man aus jeder Transformation $S_{(a)}$ der Gruppe (1) jede unendlich benachbarte Transformation $S_{(a+\delta a)}$ der Gruppe erhalten kann, indem man entweder zuerst die Transformation $S_{(a)}$ ausführt und dann eine geeignete infinitesimale Transformation der bewussten Schaar, oder indem man zuerst eine geeignete infinitesimale Transformation dieser Schaar ausführt und dann die Transformation $S_{(a)}$.

**D24 · pp. 552–553 · §108**

Wir wollen jetzt zusehen, was für analytische Ergebnisse aus den vorhin angestellten begrifflichen Ueberlegungen folgen.

Die infinitesimale Transformation: $S_{(a)}^{-1}S_{(a+\delta a)}$ wird nach S. 547 durch die Gleichungen:
$$
x_i'=x_i+\sum_{k=1}^r\delta a_k\left[\frac{\partial f_i(\mathfrak x,a)}{\partial a_k}\right]_{\mathfrak x=F(x,a)}\qquad(i=1\ldots n),\tag{2}
$$
dargestellt und die infinitesimale Transformation: $S_{(b-\delta b)}S_{(b)}^{-1}$ nach S. 548 durch die Gleichungen:
$$
x_i'=x_i+\sum_{k=1}^r\delta b_k\left[\frac{\partial F_i(\mathfrak x,b)}{\partial b_k}\right]_{\mathfrak x=f(x,b)}\qquad(i=1\ldots n).\tag{3'}
$$
Unterwirft man insbesondere die $\delta a$ und $\delta b$ den Gleichungen (8), so gilt die Gleichung (10), vermöge (8) wird also:
$$
\sum_{k=1}^r\delta a_k\left[\frac{\partial f_i(\mathfrak x,a)}{\partial a_k}\right]_{\mathfrak x=F(x,a)}=\sum_{k=1}^r\delta b_k\left[\frac{\partial F_i(\mathfrak x,b)}{\partial b_k}\right]_{\mathfrak x=f(x,b)}
$$
für alle Werthe der $x$, $a$ und $b$.

**D25 · p. 553 · §108**

Drücken wir daher mit Hülfe der Gleichungen (8'), die ja mit (8) äquivalent sind, die $\delta b$ durch die $\delta a$ aus und berücksichtigen wir, dass zwischen $\delta a_1\ldots\delta a_r$ allein keine Relation besteht, so ergiebt sich:
$$
\left[\frac{\partial f_i(\mathfrak x,a)}{\partial a_k}\right]_{\mathfrak x=F(x,a)}=\sum_{j=1}^r\Psi_{jk}(a,b)\left[\frac{\partial F_i(\mathfrak x,b)}{\partial b_j}\right]_{\mathfrak x=f(x,b)}\qquad(i=1\ldots n;\ k=1\ldots r).\tag{11}
$$

**D26 · p. 553 · §108**

In derselben Weise ergeben sich durch Benutzung der Gleichungen (8'') die mit (11) äquivalenten Identitäten:
$$
\left[\frac{\partial F_i(\mathfrak x,b)}{\partial b_k}\right]_{\mathfrak x=f(x,b)}=\sum_{j=1}^r A_{kj}(a,b)\left[\frac{\partial f_i(\mathfrak x,a)}{\partial a_j}\right]_{\mathfrak x=F(x,a)}\qquad(i=1\ldots n;\ k=1\ldots r),\tag{12}
$$
Hier haben, wie schon oben angedeutet, die $\Psi$ und die $A$ dieselbe Bedeutung wie auf S. 29 f. von Abschnitt I. Andererseits ist nach der auf S. 28 daselbst angewandten Bezeichnung:
$$
\left[\frac{\partial F_i(\mathfrak x,b)}{\partial b_k}\right]_{\mathfrak x=f(x,b)}=\Phi_{ki}(x_1\ldots x_n;\ b_1\ldots b_r).\tag{13}
$$
allerdings wurden damals die $\Phi$ auf andre Weise gebildet, man überzeugt sich aber leicht, dass die linke Seite von (13) mit der damals gebildeten Function: $\Phi_{ki}(x,b)$ übereinstimmt.

**D27 · pp. 553–554 · §108**

Da die Identitäten (11) und (12) für alle Werthe der $x$, der $a$ und der $b$ gültig sind, so bleiben sie auch dann noch erfüllt, wenn man für $b_1\ldots b_r$ irgend ein festes Werthsystem: $\omega_1\ldots\omega_r$ von allgemeiner Lage einsetzt. Thut man das und wendet man dieselben Abkürzungen an wie auf S. 31 von Abschnitt I, so erhält man aus (11) und (12) die folgenden neuen Identitäten:
$$
\left[\frac{\partial f_i(\mathfrak x,a)}{\partial a_k}\right]_{\mathfrak x=F(x,a)}=\sum_{j=1}^r\psi_{jk}(a)\xi_{ji}(x),\tag{11'}
$$
$$
\xi_{ki}(x)=\sum_{j=1}^r\alpha_{kj}(a)\left[\frac{\partial f_i(\mathfrak x,a)}{\partial a_j}\right]_{\mathfrak x=F(x,a)},\tag{12'}
$$
die natürlich auch mit einander äquivalent sind. Aus (11') und (12) ergiebt sich schliesslich noch die Identität:
$$
\left[\frac{\partial F_i(\mathfrak x,b)}{\partial b_k}\right]_{\mathfrak x=f(x,b)}=\sum_{\tau=1}^r\left\{\sum_{j=1}^r A_{kj}(a,b)\psi_{\tau j}(a)\right\}\xi_{\tau i}(x).\tag{12''}
$$

**D28 · p. 554 · §108**

Hiermit ist das Ergebniss, zu dem wir vorhin durch begriffliche Ueberlegungen gelangt sind, analytisch ausgedrückt. Da nämlich unter den gemachten Voraussetzungen die Determinante der $\psi_{jk}(a)$ einen endlichen von Null verschiedenen Werth hat, so zeigen die Identitäten (11') unmittelbar, dass die $\infty^{r-1}$ infinitesimalen Transformationen: $S_{(a)}^{-1}S_{(a+\delta a)}$, die durch die Gleichungen (2) auf S. 552 dargestellt werden, aus den $r$ infinitesimalen Transformationen:
$$
X_kf=\sum_{i=1}^n\xi_{ki}(x_1\ldots x_n)\frac{\partial f}{\partial x_i}\qquad(k=1\ldots r),
$$
linear abgeleitet sind. Ebenso zeigen die Identitäten (12''), dass von den $\infty^{r-1}$ infinitesimalen Transformationen: $S_{(b+\delta b)}S_{(b)}^{-1}$ dasselbe gilt. Hierin aber liegt, dass die $r$ infinitesimalen Transformationen: $X_1f\ldots X_rf$ von einander unabhängig sind und dass die Schaar von $\infty^{r-1}$ infinitesimalen Transformationen, die durch den Ausdruck:
$$
\sum_{k=1}^r\lambda_kX_kf\tag{14}
$$
mit den $r$ Parametern $\lambda_1\ldots\lambda_r$ dargestellt wird, eben die Schaar von $\infty^{r-1}$ infinitesimalen Transformationen ist, die im Sinne von S. 552 zu der Gruppe (1) gehört.

**D29 · pp. 554–555 · §108**

Macht man in den Identitäten (11') und (12') die Substitution: $\mathfrak x=f(x,a)$ und schreibt man dann $x'$ für $x$ und $x$ für $\mathfrak x$, so erhält man neue Identitäten, die aussagen, dass die beiden mit einander äquivalenten Systeme von Differentialgleichungen:
$$
\frac{\partial x_i'}{\partial a_k}=\sum_{j=1}^r\psi_{jk}(a)\xi_{ji}(x')\qquad(i=1\ldots n;\ k=1\ldots r),\tag{15}
$$
und:
$$
\xi_{ki}(x')=\sum_{j=1}^r\alpha_{kj}(a)\frac{\partial x_i'}{\partial a_j}\qquad(i=1\ldots n;\ k=1\ldots r),\tag{16}
$$
bei der Substitution: $x_i'=f_i(x,a)$ identisch erfüllt werden. Damit sind wir wieder zu den grundlegenden Differentialgleichungen des Theorems 3 auf S. 33 von Abschnitt I gelangt. Aber diese Differentialgleichungen erscheinen uns jetzt in einem andern Lichte. Da sie nämlich mit den Identitäten (11') gleichbedeutend sind, so sagen sie einfach aus, dass man aus einer beliebig gewählten Transformation $S_{(a)}$ der Gruppe (1) jede unendlich benachbarte Transformation $S_{(a+\delta a)}$ der Gruppe erhalten kann, indem man zuerst $S_{(a)}$ und dann eine geeignete infinitesimale Transformation der Schaar (14) ausführt. Die betreffende infinitesimale Transformation ist übrigens auch leicht angebbar, sie wird ja durch den Ausdruck: $S_{(a)}^{-1}S_{(a+\delta a)}$ dargestellt und besitzt daher die Form:
$$
x_i'=x_i+\sum_{k=1}^r\delta a_k\sum_{j=1}^r\psi_{jk}(a)\xi_{ji}(x)\qquad(i=1\ldots n).\tag{17}
$$

**D30 · p. 555 · §108**

Man beachte übrigens, dass die eben ausgesprochene Deutung der grundlegenden Differentialgleichungen nicht davon abhängig ist, dass die Schaar (1), die unsre Differentialgleichungen erfüllt, eine Gruppe bildet. Hat man nämlich irgend eine Schaar (1) von $\infty^r$ Transformationen, die den Differentialgleichungen (15) oder den äquivalenten (16) genügt, so bestehen für diese Schaar die Identitäten (11') und es lässt sich demnach jede Transformation $S_{(a+\delta a)}$ der Schaar dadurch herstellen, dass man zuerst die Transformation $S_{(a)}$ und sodann eine geeignete infinitesimale Transformation der Schaar (14) ausführt.

Wir kommen im nächsten Paragraphen hierauf zurück.

**D31 · p. 555 · §108**

Aus den Identitäten (12'') ergiebt sich ein System von Differentialgleichungen, das ein Seitenstück zu dem Systeme (15) bildet. Die Ableitung dieses Systems ist fast genau so wie auf S. 40 f. von Abschnitt I. Wie dort beweist man, dass der Ausdruck:
$$
\sum_{j=1}^r A_{kj}(a,b)\psi_{\tau j}(a)
$$
von $a_1\ldots a_r$ frei ist und durch eine Function: $\vartheta_{\tau k}(b)$ von den $b$ allein ersetzt werden kann. Sodann findet man leicht, dass die Differentialgleichungen:
$$
\frac{\partial x_i}{\partial a_k}=\sum_{j=1}^r\vartheta_{jk}(a)\xi_{ji}(x)\qquad(i=1\ldots n;\ k=1\ldots r)\tag{18}
$$
bei der Substitution: $x_i=F_i(x',a)$ identisch erfüllt werden, dass also $x_1\ldots x_n$, wenn man sie sich aus den Gleichungen: $x_i'=f_i(x,a)$ als Functionen der $x'$ und der $a$ bestimmt denkt, den Differentialgleichungen (18) genügen.

**D32 · pp. 555–556 · §108**

Da die Differentialgleichungen (18) mit den Identitäten (12'') gleichbedeutend sind, so sagen sie offenbar aus, dass jede Transformation $S_{(a+\delta a)}$ der Gruppe (1) dadurch erhalten werden kann, dass man zuerst eine geeignete infinitesimale Transformation der Schaar (14) und dann die Transformation $S_{(a)}$ ausführt. Die betreffende infinitesimale Transformation wird durch den Ausdruck: $S_{(a+\delta a)}S_{(a)}^{-1}$ dargestellt und lautet daher:
$$
x_i'=x_i-\sum_{k=1}^r\delta a_k\sum_{j=1}^r\vartheta_{jk}(a)\xi_{ji}(x)\qquad(i=1\ldots n).\tag{19}
$$
(vgl. S. 548 und S. 554 Gl. (12'')).

Auch hier ist zu bemerken, dass diese Deutung der Differentialgleichungen (18) nicht daran hängt, dass die Schaar (1) eine Gruppe bildet; denn wenn für irgend eine Schaar (1) von $\infty^r$ Transformationen die Differentialgleichungen (18) erfüllt sind, so hat das immer den Sinn, dass die Transformation $S_{(a+\delta a)}$ der Schaar (1) in der eben beschriebenen Weise erhalten werden kann, mag nun die Schaar (1) eine Gruppe bilden oder nicht.

**D33 · p. 556 · §108**

Wir sahen auf S. 547, dass die beiden infinitesimalen Transformationen: $S_{(a)}^{-1}S_{(a+\delta a)}$ und $S_{(a+\delta a)}S_{(a)}^{-1}$ in der einfachen Beziehung stehen:
$$
S_{(a)}^{-1}\cdot S_{(a+\delta a)}S_{(a)}^{-1}\cdot S_{(a)}=S_{(a)}^{-1}S_{(a+\delta a)},
$$
dass also die erste erhalten wird, wenn man in die zweite vermöge der Transformation $S_{(a)}$ neue Veränderliche einführt. Ertheilen wir den $a$ feste Werthe, während wir die $\delta a$ willkürlich lassen, so stellen die beiden Ausdrücke: $S_{(a)}^{-1}S_{(a+\delta a)}$ und $S_{(a+\delta a)}S_{(a)}^{-1}$ zwei Schaaren von je $\infty^{r-1}$ infinitesimalen Transformationen dar und diese beiden Schaaren sind unter den Voraussetzungen des gegenwärtigen Paragraphen mit einander und mit der Schaar (14) identisch (s. S. 551 f. und S. 554). Demnach ergiebt sich, dass die Schaar der $\infty^{r-1}$ infinitesimalen Transformationen (14) bei jeder Transformation $S_{(a)}$ unsrer Gruppe invariant bleibt.

**D34 · pp. 556–557 · §108**

Um dieses Ergebniss analytisch auszudrücken, erinnern wir daran, dass die infinitesimale Transformation $S_{(a)}^{-1}S_{(a+\delta a)}$ durch die Gleichungen (17) und die infinitesimale Transformation $S_{(a+\delta a)}S_{(a)}^{-1}$ durch die Gleichungen (19) dargestellt wird. Setzen wir daher: $\delta a_k=u_k\delta t$, wo $u_1\ldots u_r$ endliche Grössen sind, so wird das Symbol der infinitesimalen Transformation: $S_{(a)}^{-1}S_{(a+\delta a)}$ sein:
$$
\sum_{k=1}^r u_k\sum_{j=1}^r\psi_{jk}(a)X_jf\tag{20}
$$
und das Symbol von $S_{(a+\delta a)}S_{(a)}^{-1}$:
$$
-\sum_{k=1}^r u_k\sum_{j=1}^r\vartheta_{jk}(a)X_jf.\tag{21}
$$

**D35 · p. 557 · §108**

Wegen der oben geschilderten Beziehung zwischen beiden infinitesimalen Transformationen muss nun der Ausdruck (21) bei der Transformation $S_{(a)}$ die Form (20) erhalten und zwar muss das bei beliebigen Werthen von $u_1\ldots u_r$ gelten. Führen wir demnach die Abkürzung ein:
$$
\sum_{i=1}^n\xi_{ki}(x_1'\ldots x_n')\frac{\partial f}{\partial x_i'}=X_k'f,
$$
so ergiebt sich, dass vermöge der Gleichungen:
$$
x_i'=f_i(x_1\ldots x_n;\ a_1\ldots a_r)\qquad(i=1\ldots n)\tag{1}
$$
unsrer Gruppe die Relationen:
$$
\sum_{j=1}^r\vartheta_{jk}(a)X_jf+\sum_{j=1}^r\psi_{jk}(a)X_j'f=0\qquad(k=1\ldots r)\tag{22}
$$
bestehen, unter $f$ eine beliebige Function von $x_1'\ldots x_n'$ verstanden. Es sind das dieselben Gleichungen, die wir in Abschnitt I auf S. 44 abgeleitet haben.

**D36 · p. 557 · §108 conclusion**

Das Bestehen der Gleichungen (22) ist eine Folge der Differentialgleichungen (15) und (18) und ausserdem der Identität:
$$
S_{(a)}^{-1}\cdot S_{(a+\delta a)}S_{(a)}^{-1}\cdot S_{(a)}=S_{(a)}^{-1}S_{(a+\delta a)},
$$
die für jede Schaar (1) von $\infty^r$ Transformationen gültig ist. Demnach ist das Bestehen der Gleichungen (22) nicht daran geknüpft, dass die Schaar (1) eine Gruppe bildet, sondern nur daran, dass für diese Schaar die Differentialgleichungen (15) und (18) erfüllt sind. Das gleichzeitige Erfülltsein der Differentialgleichungen (15) und (18) sagt eben aus, dass die Schaar der $\infty^{r-1}$ infinitesimalen Transformationen (14) bei jeder Transformation der Schaar (1) invariant bleibt, mag nun die Schaar (1) eine Gruppe bilden oder nicht.

Durch das Vorstehende sind alle Ergebnisse des 2. Kapitels von Abschnitt I wieder gewonnen, soweit sie sich nicht auf die Gültigkeitsbereiche der auftretenden Functionen beziehen. Dass unsre jetzige Ableitung dieser Ergebnisse grössere Durchsichtigkeit besitzt, liegt auf der Hand; aber dieser Vorzug ist nur erreicht durch die Benutzung einer Reihe von gruppentheoretischen Begriffen, die wir damals nicht als bekannt voraussetzen konnten.

### Original footnote

**F1 · p. 552, §108.** Wenn wir uns auch hier auf die Untersuchungen der Bereiche, innerhalb deren die auftretenden Functionen definirt sind, nicht einlassen, so können wir doch eine Bemerkung nicht unterdrücken. Aus den vorstehenden Betrachtungen ergiebt sich nämlich, dass die in Abschn. I auf S. 15 f. gemachten Voraussetzungen durch allgemeinere ersetzt werden können. Man braucht nicht zu verlangen, dass es innerhalb der dort definirten Bereiche $(x)$ und $(a)$ zwei kleinere Bereiche $((x))$ und $((a))$ gebe, die so beschaffen sind, dass jedesmal, wenn die $x$ in $((x))$ und die $a$ und $b$ innerhalb $((a))$ liegen, zugleich die $x'$ in den Bereich $(x)$ und die $c$ in den Bereich $(a)$ fallen; es genügt vielmehr, anzunehmen, dass es in dem Bereiche $(x)$ einen kleineren Bereich $((x))$ und in dem Bereiche $(a)$ zwei kleinere Bereiche $((a))$ und $((b))$ gebe, die so beschaffen sind, dass jedesmal, wenn die $x$ in $((x))$, die $a$ in $((a))$ und die $b$ in $((b))$ liegen, die $x'$ dem Bereiche $(x)$ und die $c$ dem Bereiche $(a)$ angehören.

### Independent English translation: Chapter 25 introduction and §§107–108

**E01 · p. 545 · Chapter 25 introduction**

**Chapter 25. The fundamental theorems of group theory.**

For an overview of the theorems supporting the whole theory of finite continuous groups, it is best to distinguish three theorems that may appropriately be called the three fundamental theorems of group theory.

Each of them is a paired theorem: it really consists of two assertions, one being the converse of the other.

**E02 · pp. 545–546 · Chapter 25 introduction**

The first fundamental theorem says that every $r$-parameter group satisfies differential equations of a very particular kind, the so-called fundamental differential equations. Conversely, any family of $\infty^r$ transformations satisfying such differential equations and also containing the identity transformation forms an $r$-parameter group.

**E03 · p. 546 · Chapter 25 introduction**

The second fundamental theorem says that every $r$-parameter group with pairwise inverse transformations is generated by $r$ independent infinitesimal transformations $X_1f\ldots X_rf$ whose pairwise relations have the form
$$
(X_iX_k)=\sum_{s=1}^r c_{iks}X_sf\qquad(i,k=1\ldots r).\tag{A}
$$
Conversely, $r$ independent infinitesimal transformations with these relations always generate an $r$-parameter group with pairwise inverse transformations.

**E04 · p. 546 · Chapter 25 introduction**

Finally, the third fundamental theorem says that the $r^3$ constants $c_{iks}$ in (A) satisfy certain relations. Conversely, for any given system of $r^3$ constants satisfying those relations, one can find $r$ independent infinitesimal transformations $X_1f\ldots X_rf$ with precisely the relations (A).

**E05 · p. 546 · Chapter 25 introduction**

None of these three fundamental theorems can be dispensed with in building a complete group theory. If instead one asks which is used most often, the second is by far the most frequently applied in group-theoretic investigations. We therefore also call it the principal theorem of the whole theory.

**E06 · p. 546 · Chapter 25 introduction**

We shall now discuss the three fundamental theorems in order and in greater detail. Our chief aim is to make the conceptual content of the theorems and their earlier proofs as clear as possible. We should say at once, however, that questions about the domains on which the functions are defined will be set aside here; for those questions we refer to the developments in Volume I.

**E07 · pp. 546–547 · §107**

**§107.** Let the equations
$$
x_i'=f_i(x_1\ldots x_n;\ a_1\ldots a_r)\qquad(i=1\ldots n).\tag{1}
$$
with $r$ essential parameters $a_1\ldots a_r$ describe an arbitrary family of $\infty^r$ distinct transformations, without yet assuming an $r$-parameter group. Write $S_{(a)}$ for the transformation (1).

**E08 · p. 547 · §107**

Take any transformation $S_{(a+\delta a)}$ in (1) infinitely close to $S_{(a)}$. It can be composed from $S_{(a)}$ and an infinitesimal transformation in two ways. One may first perform $S_{(a)}$, followed by $S_{(a)}^{-1}S_{(a+\delta a)}$; or first perform $S_{(a+\delta a)}S_{(a)}^{-1}$, followed by $S_{(a)}$.

**E09 · p. 547 · §107**

The two infinitely close transformations $S_{(a)}$ and $S_{(a+\delta a)}$ in (1) therefore define the two infinitesimal transformations $S_{(a)}^{-1}S_{(a+\delta a)}$ and $S_{(a+\delta a)}S_{(a)}^{-1}$. The identity
$$
S_{(a)}^{-1}\cdot S_{(a+\delta a)}S_{(a)}^{-1}\cdot S_{(a)}=S_{(a)}^{-1}S_{(a+\delta a)}.
$$
shows their simple relation: the first is obtained from the second by introducing new variables through $S_{(a)}$.

**E10 · p. 547 · §107**

Suppose solving (1) for $x_1\ldots x_n$ gives
$$
x_i=F_i(x_1'\ldots x_n';\ a_1\ldots a_r)\qquad(i=1\ldots n),\tag{1'}
$$
Then the infinitesimal transformations can be written explicitly. For $S_{(a)}^{-1}S_{(a+\delta a)}$ one finds
$$
x_i'=f_i(F_1(x,a)\ldots F_n(x,a);\ a_1+\delta a_1,\ldots,a_r+\delta a_r),
$$
The identities
$$
f_i(F_1(x,a)\ldots F_n(x,a);\ a_1\ldots a_r)\equiv x_i
$$
reduce them to
$$
x_i'=x_i+\sum_{k=1}^r\delta a_k\left[\frac{\partial f_i(\mathfrak x,a)}{\partial a_k}\right]_{\mathfrak x=F(x,a)}\qquad(i=1\ldots n).\tag{2}
$$

**E11 · pp. 547–548 · §107**

For $S_{(a+\delta a)}S_{(a)}^{-1}$ one similarly obtains
$$
x_i'=F_i(f_1(x,a+\delta a)\ldots f_n(x,a+\delta a);\ a_1\ldots a_r),
$$
Expanding in the infinitesimal quantities $\delta a_1\ldots\delta a_r$ gives
$$
x_i'=x_i+\sum_{k=1}^r\delta a_k\sum_{\nu=1}^n\frac{\partial f_\nu(x,a)}{\partial a_k}\left[\frac{\partial F_i(\mathfrak x,a)}{\partial\mathfrak x_\nu}\right]_{\mathfrak x=f(x,a)}\qquad(i=1\ldots n)
$$
These equations simplify substantially. Differentiating the identity
$$
F_i(f_1(x,a)\ldots f_n(x,a);\ a_1\ldots a_r)\equiv x_i
$$
with respect to $a_k$ yields
$$
\sum_{\nu=1}^n\left[\frac{\partial F_i(\mathfrak x,a)}{\partial\mathfrak x_\nu}\right]_{\mathfrak x=f(x,a)}\frac{\partial f_\nu(x,a)}{\partial a_k}+\left[\frac{\partial F_i(\mathfrak x,a)}{\partial a_k}\right]_{\mathfrak x=f(x,a)}=0,
$$
Hence $S_{(a+\delta a)}S_{(a)}^{-1}$ has the simple form
$$
x_i'=x_i-\sum_{k=1}^r\delta a_k\left[\frac{\partial F_i(\mathfrak x,a)}{\partial a_k}\right]_{\mathfrak x=f(x,a)}\qquad(i=1\ldots n).\tag{3}
$$

**E12 · p. 548 · §107**

The same form could have been obtained more quickly by noticing that
$$
S_{(a+\delta a)}S_{(a)}^{-1}=\left((S_{(a)}^{-1})^{-1}S_{(a+\delta a)}^{-1}\right)^{-1},
$$
Writing this identity in coordinates leads directly to (3).

**E13 · p. 548 · §107**

Fix values of $a$ while leaving $\delta a$ arbitrary. Equations (2) and (3) describe two families of infinitesimal transformations attached by (1) to $x_i'=f_i(x,a)$. It is easy to see that each family generally consists of $\infty^{r-1}$ distinct infinitesimal transformations.

Indeed, all the infinitesimal transformations (2) are linear combinations of the $r$ transformations
$$
Z_kf=\sum_{i=1}^n\left[\frac{\partial f_i(\mathfrak x,a)}{\partial a_k}\right]_{\mathfrak x=F(x,a)}\frac{\partial f}{\partial x_i}\qquad(k=1\ldots r)
$$

**E14 · pp. 548–549 · §107**

By hypothesis the $r$ parameters $a_1\ldots a_r$ in (1) are essential. According to Volume I, p. 13, this holds exactly when there are no functions $\chi_1\ldots\chi_r$ of $a$ alone, not all zero, for which the $n$ equations
$$
\sum_{k=1}^r\chi_k(a_1\ldots a_r)\frac{\partial f_i(x,a)}{\partial a_k}=0\qquad(i=1\ldots n)
$$
hold identically. The infinitesimal transformations $Z_1f\ldots Z_rf$ therefore cannot satisfy a relation
$$
\sum_{k=1}^r\chi_k(a_1\ldots a_r)Z_kf\equiv0
$$
unless every $\chi_k$ vanishes. Thus $Z_1f\ldots Z_rf$ are independent for general values of $a$. Equivalently, for each general parameter system $a_1\ldots a_r$, the family (2) consists of $\infty^{r-1}$ distinct infinitesimal transformations. The same is true of (3), since introducing new variables through $S_{(a)}$ carries it to (2).

**E15 · p. 549 · §107**

Thus the family (1) of $\infty^r$ transformations associates to each $S_{(a)}$ two families, (2) and (3), each of $\infty^{r-1}$ infinitesimal transformations. Each transformation $S_{(a+\delta a)}$ in (1) infinitely close to $S_{(a)}$ is obtained either by performing $S_{(a)}$ and then a suitable transformation from (2), or by performing a suitable transformation from (3) and then $S_{(a)}$.

There is also a converse worth recording. If, for general $a$, the family (2) contains $r$ independent infinitesimal transformations, and hence $\infty^{r-1}$ distinct ones, then (1) consists of $\infty^r$ distinct finite transformations. Requiring (2) to contain precisely $r$ independent infinitesimal transformations for general $a_1\ldots a_r$ is therefore equivalent to requiring that the $r$ parameters in (1) be essential.

**E16 · pp. 549–550 · §108**

**§108.** Now assume that the $\infty^r$ transformations (1) form an $r$-parameter group. Eliminating $x'$ between (1) and
$$
x_i''=f_i(x_1'\ldots x_n';\ b_1\ldots b_r)\qquad(i=1\ldots n),\tag{4}
$$
gives
$$
x_i''=f_i(f_1(x,a)\ldots f_n(x,a);\ b_1\ldots b_r)\qquad(i=1\ldots n),\tag{5}
$$
which can be put in the form
$$
x_i''=f_i(x_1\ldots x_n;\ c_1\ldots c_r)\qquad(i=1\ldots n),\tag{5'}
$$
where
$$
c_k=\varphi_k(a_1\ldots a_r;\ b_1\ldots b_r)\qquad(k=1\ldots r)\tag{6}
$$
depends only on $a$ and $b$. The assumption is expressed more briefly by
$$
S_{(a)}S_{(b)}=S_{(c)}.\tag{7}
$$

**E17 · p. 550 · §108**

Fix $b$ and let $a$ vary freely. The left side of (7) plainly describes $\infty^r$ transformations, so the right side must do likewise. The $c_k$ are consequently independent functions of $a_1\ldots a_r$. The same argument gives independence as functions of $b_1\ldots b_r$. In short, (6) can be solved either for $a$ or for $b$, a result derived purely analytically, and therefore rather laboriously, in Volume I, pp. 17 ff.

**E18 · p. 550 · §108**

Equation (7) immediately gives
$$
S_{(a+\delta a)}S_{(b+\delta b)}=S_{(c+\delta c)},
$$
where differentiating (6) determines $\delta c$. Since (6) can be solved for either parameter system, we can always choose $\delta a,\delta b$ so that every $\delta c$ vanishes. Those choices are defined by
$$
\sum_{j=1}^r\frac{\partial\varphi_k(a,b)}{\partial a_j}\delta a_j+\sum_{j=1}^r\frac{\partial\varphi_k(a,b)}{\partial b_j}\delta b_j=0\qquad(k=1\ldots r)\tag{8}
$$
Whenever these equations hold,
$$
S_{(a+\delta a)}S_{(b+\delta b)}=S_{(c)}=S_{(a)}S_{(b)}.\tag{9}
$$

**E19 · pp. 550–551 · §108**

By §107, $S_{(a+\delta a)}$ is obtained by first performing $S_{(a)}$ and then the infinitesimal transformation $S_{(a)}^{-1}S_{(a+\delta a)}$ from (2). Likewise, $S_{(b+\delta b)}$ is obtained by first performing $S_{(b+\delta b)}S_{(b)}^{-1}$ and then $S_{(b)}$. We can therefore rewrite (9) as
$$
S_{(a)}\cdot(S_{(a)}^{-1}S_{(a+\delta a)}\cdot S_{(b+\delta b)}S_{(b)}^{-1})\cdot S_{(b)}=S_{(a)}S_{(b)},
$$
It follows that
$$
S_{(a)}^{-1}S_{(a+\delta a)}\cdot S_{(b+\delta b)}S_{(b)}^{-1}=1,
$$
equals the identity transformation. Under these assumptions the two infinitesimal transformations are inverse to one another. The inverse of $S_{(b+\delta b)}S_{(b)}^{-1}$ has the form $S_{(b-\delta b)}S_{(b)}^{-1}$, so finally
$$
S_{(a)}^{-1}S_{(a+\delta a)}=S_{(b-\delta b)}S_{(b)}^{-1}.\tag{10}
$$

**E20 · p. 551 · §108**

Equation (10) follows from (7), but no longer contains $c_1\ldots c_r$. Since $a$ and $b$ themselves are unrelated, (10) holds for arbitrary choices of their values and every $\delta a_k,\delta b_k$ satisfying (8). Solving (8) for either set of increments gives
$$
\delta b_j=\sum_{k=1}^r\Psi_{jk}(a_1\ldots a_r;\ b_1\ldots b_r)\delta a_k\qquad(j=1\ldots r),\tag{8'}
$$
or
$$
\delta a_j=\sum_{k=1}^r A_{kj}(a_1\ldots a_r;\ b_1\ldots b_r)\delta b_k\qquad(j=1\ldots r).\tag{8''}
$$
Compare Volume I, pp. 29–30. Thus these equations impose no relation among $\delta b_1\ldots\delta b_r$ alone, or among $\delta a_1\ldots\delta a_r$ alone.

**E21 · p. 551 · §108**

Choose and fix any two general parameter systems $a_1\ldots a_r$ and $b_1\ldots b_r$. Subject $\delta a,\delta b$ to (8), but otherwise leave them free. The left side of (10) then describes the first of the two families of $\infty^{r-1}$ infinitesimal transformations attached to $S_{(a)}$ in §107. The right side describes the second such family attached to $S_{(b)}$, since changing $\delta b$ to $-\delta b$ does not change the family $S_{(b+\delta b)}S_{(b)}^{-1}$. Equation (10) therefore says that the first family attached to $S_{(a)}$ coincides with the second attached to $S_{(b)}$.

**E22 · pp. 551–552 · §108**

Keep only $b_1\ldots b_r$ fixed and vary $a_1\ldots a_r$. Equation (10) shows that the family $S_{(a)}^{-1}S_{(a+\delta a)}$ of $\infty^{r-1}$ infinitesimal transformations remains the same however $a$ varies. The corresponding argument shows that $S_{(b-\delta b)}S_{(b)}^{-1}$ does not vary with $b$. Since (10) identifies these two families, the families represented by $S_{(a)}^{-1}S_{(a+\delta a)}$ and $S_{(a+\delta a)}S_{(a)}^{-1}$ are identical and both independent of $a_1\ldots a_r$.[F1]

**E23 · p. 552 · §108**

Consequently, when (1) forms an $r$-parameter group, all the infinitesimal families attached to its $\infty^r$ transformations coincide. In other words:

Every $r$-parameter group (1) of $\infty^r$ point transformations has a definite family of $\infty^{r-1}$ infinitesimal transformations. It consists of all linear combinations of $r$ particular independent infinitesimal transformations. From any group transformation $S_{(a)}$, every infinitely close transformation $S_{(a+\delta a)}$ is obtained either by first performing $S_{(a)}$ and then a suitable infinitesimal transformation in that family, or by performing a suitable infinitesimal transformation in the family and then $S_{(a)}$.

**E24 · pp. 552–553 · §108**

Let us now obtain the analytic consequences of those conceptual considerations.

According to p. 547, $S_{(a)}^{-1}S_{(a+\delta a)}$ is represented by
$$
x_i'=x_i+\sum_{k=1}^r\delta a_k\left[\frac{\partial f_i(\mathfrak x,a)}{\partial a_k}\right]_{\mathfrak x=F(x,a)}\qquad(i=1\ldots n),\tag{2}
$$
According to p. 548, $S_{(b-\delta b)}S_{(b)}^{-1}$ is represented by
$$
x_i'=x_i+\sum_{k=1}^r\delta b_k\left[\frac{\partial F_i(\mathfrak x,b)}{\partial b_k}\right]_{\mathfrak x=f(x,b)}\qquad(i=1\ldots n).\tag{3'}
$$
If the increments satisfy (8), equation (10) holds. Thus (8) gives
$$
\sum_{k=1}^r\delta a_k\left[\frac{\partial f_i(\mathfrak x,a)}{\partial a_k}\right]_{\mathfrak x=F(x,a)}=\sum_{k=1}^r\delta b_k\left[\frac{\partial F_i(\mathfrak x,b)}{\partial b_k}\right]_{\mathfrak x=f(x,b)}
$$
for all $x,a,b$.

**E25 · p. 553 · §108**

Express $\delta b$ in terms of $\delta a$ using (8'), which is equivalent to (8). Since the $\delta a_1\ldots\delta a_r$ alone satisfy no relation, we obtain
$$
\left[\frac{\partial f_i(\mathfrak x,a)}{\partial a_k}\right]_{\mathfrak x=F(x,a)}=\sum_{j=1}^r\Psi_{jk}(a,b)\left[\frac{\partial F_i(\mathfrak x,b)}{\partial b_j}\right]_{\mathfrak x=f(x,b)}\qquad(i=1\ldots n;\ k=1\ldots r).\tag{11}
$$

**E26 · p. 553 · §108**

Using (8'') in the same way gives the equivalent identities
$$
\left[\frac{\partial F_i(\mathfrak x,b)}{\partial b_k}\right]_{\mathfrak x=f(x,b)}=\sum_{j=1}^r A_{kj}(a,b)\left[\frac{\partial f_i(\mathfrak x,a)}{\partial a_j}\right]_{\mathfrak x=F(x,a)}\qquad(i=1\ldots n;\ k=1\ldots r),\tag{12}
$$
As indicated above, $\Psi$ and $A$ have the meanings used in Volume I, pp. 29 ff. The notation of p. 28 there gives
$$
\left[\frac{\partial F_i(\mathfrak x,b)}{\partial b_k}\right]_{\mathfrak x=f(x,b)}=\Phi_{ki}(x_1\ldots x_n;\ b_1\ldots b_r).\tag{13}
$$
The $\Phi$ were formed differently there, but the left side of (13) is readily seen to agree with the function $\Phi_{ki}(x,b)$ formed at that earlier point.

**E27 · pp. 553–554 · §108**

Since (11) and (12) hold for every $x,a,b$, they remain valid when $b_1\ldots b_r$ is replaced by any fixed general parameter system $\omega_1\ldots\omega_r$. Doing this, with the abbreviations used in Volume I, p. 31, gives
$$
\left[\frac{\partial f_i(\mathfrak x,a)}{\partial a_k}\right]_{\mathfrak x=F(x,a)}=\sum_{j=1}^r\psi_{jk}(a)\xi_{ji}(x),\tag{11'}
$$
$$
\xi_{ki}(x)=\sum_{j=1}^r\alpha_{kj}(a)\left[\frac{\partial f_i(\mathfrak x,a)}{\partial a_j}\right]_{\mathfrak x=F(x,a)},\tag{12'}
$$
which are again equivalent. Finally, (11') and (12) give
$$
\left[\frac{\partial F_i(\mathfrak x,b)}{\partial b_k}\right]_{\mathfrak x=f(x,b)}=\sum_{\tau=1}^r\left\{\sum_{j=1}^r A_{kj}(a,b)\psi_{\tau j}(a)\right\}\xi_{\tau i}(x).\tag{12''}
$$

**E28 · p. 554 · §108**

This expresses analytically the result previously reached through conceptual reasoning. Under our assumptions the determinant of $\psi_{jk}(a)$ is finite and nonzero. Identities (11') therefore show directly that the infinitesimal transformations $S_{(a)}^{-1}S_{(a+\delta a)}$, represented by (2) on p. 552, are linear combinations of
$$
X_kf=\sum_{i=1}^n\xi_{ki}(x_1\ldots x_n)\frac{\partial f}{\partial x_i}\qquad(k=1\ldots r),
$$
Identities (12'') give the same conclusion for $S_{(b+\delta b)}S_{(b)}^{-1}$. Thus $X_1f\ldots X_rf$ are independent, and the family represented with $r$ parameters $\lambda_1\ldots\lambda_r$ by
$$
\sum_{k=1}^r\lambda_kX_kf\tag{14}
$$
is exactly the family of $\infty^{r-1}$ infinitesimal transformations belonging to (1) in the sense of p. 552.

**E29 · pp. 554–555 · §108**

In (11') and (12') substitute $\mathfrak x=f(x,a)$, then write $x'$ for $x$ and $x$ for $\mathfrak x$. The resulting identities say that the two equivalent systems
$$
\frac{\partial x_i'}{\partial a_k}=\sum_{j=1}^r\psi_{jk}(a)\xi_{ji}(x')\qquad(i=1\ldots n;\ k=1\ldots r),\tag{15}
$$
and
$$
\xi_{ki}(x')=\sum_{j=1}^r\alpha_{kj}(a)\frac{\partial x_i'}{\partial a_j}\qquad(i=1\ldots n;\ k=1\ldots r),\tag{16}
$$
are identically satisfied on substituting $x_i'=f_i(x,a)$. We have returned to the fundamental differential equations of Theorem 3 in Volume I, p. 33, but now see them differently. Their equivalence with (11') means simply that every transformation infinitely close to an arbitrary $S_{(a)}$ in the group is obtained by first performing $S_{(a)}$ and then a suitable infinitesimal transformation from (14). That infinitesimal transformation, represented by $S_{(a)}^{-1}S_{(a+\delta a)}$, has the form
$$
x_i'=x_i+\sum_{k=1}^r\delta a_k\sum_{j=1}^r\psi_{jk}(a)\xi_{ji}(x)\qquad(i=1\ldots n).\tag{17}
$$

**E30 · p. 555 · §108**

This interpretation of the fundamental differential equations does not require the family satisfying them to form a group. Any family (1) of $\infty^r$ transformations satisfying (15), or equivalently (16), also satisfies (11'). Each $S_{(a+\delta a)}$ in that family can therefore be obtained by performing $S_{(a)}$ and then a suitable infinitesimal transformation from (14).

We return to this in the next section.

**E31 · p. 555 · §108**

Identities (12'') yield a counterpart to (15). Its derivation is almost the same as in Volume I, pp. 40 ff. As there, one proves that
$$
\sum_{j=1}^r A_{kj}(a,b)\psi_{\tau j}(a)
$$
is independent of $a_1\ldots a_r$ and can be replaced by a function $\vartheta_{\tau k}(b)$ of $b$ alone. One then finds that
$$
\frac{\partial x_i}{\partial a_k}=\sum_{j=1}^r\vartheta_{jk}(a)\xi_{ji}(x)\qquad(i=1\ldots n;\ k=1\ldots r)\tag{18}
$$
holds identically on substituting $x_i=F_i(x',a)$. Thus the inverse coordinates $x_1\ldots x_n$, viewed as functions of $x'$ and $a$ through $x_i'=f_i(x,a)$, satisfy (18).

**E32 · pp. 555–556 · §108**

Because (18) and (12'') are equivalent, they say that $S_{(a+\delta a)}$ can be obtained by first performing a suitable infinitesimal transformation from (14), and then $S_{(a)}$. The former is $S_{(a+\delta a)}S_{(a)}^{-1}$ and has the form
$$
x_i'=x_i-\sum_{k=1}^r\delta a_k\sum_{j=1}^r\vartheta_{jk}(a)\xi_{ji}(x)\qquad(i=1\ldots n).\tag{19}
$$
Compare p. 548 and (12'') on p. 554.

Again this interpretation of (18) does not depend on (1) being a group. For any family of $\infty^r$ transformations satisfying (18), the transformation $S_{(a+\delta a)}$ is obtained in the stated way, whether or not the family forms a group.

**E33 · p. 556 · §108**

We saw on p. 547 that the two infinitesimal transformations satisfy
$$
S_{(a)}^{-1}\cdot S_{(a+\delta a)}S_{(a)}^{-1}\cdot S_{(a)}=S_{(a)}^{-1}S_{(a+\delta a)},
$$
The first is thus obtained from the second by introducing variables through $S_{(a)}$. Fix $a$ and let $\delta a$ vary. The two expressions give families of $\infty^{r-1}$ infinitesimal transformations which, under this section's assumptions, coincide with each other and with (14); see pp. 551 ff. and 554. Consequently the infinitesimal family (14) remains invariant under every transformation $S_{(a)}$ in the group.

**E34 · pp. 556–557 · §108**

For an analytic expression of this result, recall that (17) represents $S_{(a)}^{-1}S_{(a+\delta a)}$ and (19) represents $S_{(a+\delta a)}S_{(a)}^{-1}$. Set $\delta a_k=u_k\delta t$, where $u_1\ldots u_r$ are finite quantities. The symbol of the first infinitesimal transformation is
$$
\sum_{k=1}^r u_k\sum_{j=1}^r\psi_{jk}(a)X_jf\tag{20}
$$
and that of the second is
$$
-\sum_{k=1}^r u_k\sum_{j=1}^r\vartheta_{jk}(a)X_jf.\tag{21}
$$

**E35 · p. 557 · §108**

By the relation between the two infinitesimal transformations, (21) must become (20) under $S_{(a)}$, for every choice of $u_1\ldots u_r$. Define
$$
\sum_{i=1}^n\xi_{ki}(x_1'\ldots x_n')\frac{\partial f}{\partial x_i'}=X_k'f,
$$
Then the group equations
$$
x_i'=f_i(x_1\ldots x_n;\ a_1\ldots a_r)\qquad(i=1\ldots n)\tag{1}
$$
give the relations
$$
\sum_{j=1}^r\vartheta_{jk}(a)X_jf+\sum_{j=1}^r\psi_{jk}(a)X_j'f=0\qquad(k=1\ldots r)\tag{22}
$$
where $f$ is any function of $x_1'\ldots x_n'$. These are the equations derived in Volume I, p. 44.

**E36 · p. 557 · §108 conclusion**

Equations (22) follow from (15), (18), and the identity
$$
S_{(a)}^{-1}\cdot S_{(a+\delta a)}S_{(a)}^{-1}\cdot S_{(a)}=S_{(a)}^{-1}S_{(a+\delta a)},
$$
valid for every family (1) of $\infty^r$ transformations. Hence (22) does not require (1) to be a group; it requires only that the family satisfy (15) and (18). Their simultaneous satisfaction says precisely that (14) remains invariant under every transformation of (1), whether or not (1) forms a group.

The preceding argument recovers all the results of Volume I, Chapter 2, apart from those concerning the functions' domains of validity. This derivation is plainly more transparent, but that advantage comes from using several group-theoretic concepts that could not then be assumed known.

### Translated original footnote

**F1 · p. 552, §108.** Although we do not investigate here the domains on which the functions are defined, one remark should still be made. The preceding considerations show that the assumptions in Volume I, pp. 15 ff., can be replaced by more general ones. It is unnecessary to require smaller domains $((x))$ and $((a))$ inside the domains $(x)$ and $(a)$ defined there, such that whenever $x$ lies in $((x))$ and both $a$ and $b$ lie in $((a))$, the resulting $x'$ lies in $(x)$ and $c$ in $(a)$. It suffices to assume a smaller domain $((x))$ inside $(x)$ and two smaller domains $((a))$ and $((b))$ inside $(a)$, such that whenever $x$ lies in $((x))$, $a$ in $((a))$, and $b$ in $((b))$, the resulting $x'$ belongs to $(x)$ and $c$ to $(a)$.

### Reading notes

1. **Paired theorems and the identity.** The introduction distinguishes each fundamental theorem from its converse. In particular, the first converse explicitly requires an identity transformation. The later differential interpretation of a transformation family does not by itself supply identity or closure. Lesson 1's semigroup counterexample explains why that distinction matters. Lessons 2 and 5 give the forward differential equations and their integration under precise local hypotheses; the local third theorem in lesson 6 supplies every finite-dimensional bracket algebra.

2. **The order of products.** In the original products $S_{(a)}S_{(b)}$, the transformation written first is performed first. This is visible in (5): the resulting point is $f(f(x,a),b)$. The transcription and translation preserve that order. In ordinary operator notation it is $S_{(b)}\circ S_{(a)}$. Consequently $S_{(a)}^{-1}S_{(a+\delta a)}$ is the increment performed after $S_{(a)}$, and $S_{(a+\delta a)}S_{(a)}^{-1}$ the increment performed before it. Their conjugacy identities and the negative sign of the inverse-map derivative in (3), (19) and (21) follow from that convention.

3. **What infinitesimal equality means.** Equations involving $\delta a,\delta b$ express first-order variations. For instance, the inverse increment is obtained by reversing its tangent vector. The finite maps at parameters $b-\delta b$ and the exact inverse of an increment at $b+\delta b$ need not agree beyond first order. No higher-order equality is used in deriving (10)–(12).

4. **Independence and the exponent $r-1$.** The $Z_k$ and $X_k$ are independent over constants as vector fields; this need not mean pointwise independence at each spatial point. Essential parameters are measured on a regular parameter neighbourhood, as proved in lesson 1. Lie's count $\infty^{r-1}$ treats nonzero infinitesimal directions up to multiplication by a nonzero scalar, which merely rescales their one-parameter motion. Their linear space still has dimension $r$, and (14) uses $r$ coefficients. The passage does not remove a generator.

5. **The two coefficient matrices.** From (8'), $\Psi$ maps $\delta a$ to $\delta b$. Formula (8'') writes the inverse map using coefficients $A_{kj}$, with the first index attached to $\delta b_k$. Thus the displayed matrices $(\Psi_{jk})$ and $(A_{kj})$ are related by a transpose when both are viewed in the same row-column convention. Free parameter increments give (11) and (12). Fixing a regular $\omega$ yields the constant basis $\xi_{ki}(x)$. The identity (12'') follows by substituting (11') in (12); its inner sum is $A_{kj}\psi_{\tau j}$, precisely as printed. The coefficient of each independent field is unique, so the left-hand side of (12''), which has no $a$ dependence, forces that coefficient to depend only on $b$. This supplies the coefficient argument recalled rather briefly before (18).

6. **Domains remain mathematical hypotheses.** The original explicitly postpones domain questions but retains a long footnote permitting separate small parameter domains for the two factors. The present course uses local group germs and explicitly shrinks common domains before composing or differentiating. A count of transformations or the absence of an algebraic relation is interpreted on a regular analytic chart; it does not by itself exclude critical parameter values or give global inverses.

7. **Primed fields in (22).** Here $X_j'f$ is the field with coefficient functions $\xi_{ji}$ evaluated in the target coordinates and differentiating those coordinates. The unprimed $X_jf$ acts on a target function through the coordinate transformation. Therefore (22) is a relation between the transformed field and the target-coordinate basis, not a cancellation of two unrelated copies of a field. Together (15) and (18) express invariance of the whole infinitesimal linear space. That invariance can hold for a transformation family even before one has proved that the family is a group.
