# The Riemann-Helmholtz space problem

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI, GPT-6.1 Sol (OpenAI), in Codex at Ultra. Public domain (CC0).*

How much geometry can be recovered from the permitted motions? A distance function immediately supplies invariants of motions. The converse question is harder: which assumptions about motions force a metric, and which force its curvature to be constant? We prove a local answer, with the compactness hypothesis stated explicitly, and distinguish it from the historical formulations.

Our actions are effective real-analytic local actions on real manifolds. A field means a germ when discussing a local algebra. The convention is $[X,Y]=XY-YX$. We use the action, orbit and isotropy constructions proved in Transitivity and primitivity. Basic differential geometry is available from [Differential Geometry](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D50). We give the curvature and normal-coordinate arguments needed for the space theorem, including its local uniqueness step.

## 1. What the historical problem asks

Riemann starts with an infinitesimal length given by a positive quadratic form, now written $ds^2=g_{ij}(x)dx^i dx^j$. Helmholtz instead asks what can be inferred from the movement of rigid configurations. Lie examines the transformations themselves. The opening of the fifth division of *Theorie der Transformationsgruppen* III, pp. 393–398, and Chapter 20, §85, pp. 399–410, set out this change of viewpoint.

Helmholtz's four assumptions, quoted by Lie in Chapter 21, §91, pp. 438–440 (following the chapter introduction on pp. 437–438), have the following roles. The first gives an $n$-dimensional differentiable coordinate description and differentiable motions. The second describes rigidity through a relation between each pair of points, preserved by motions; it does not initially posit a Riemannian metric. The third requires free movement of rigid configurations subject to their pair relations. The fourth, usually called monodromy, asks that the one-parameter motion remaining after fixing $n-1$ suitable points return to its initial configuration without reversing the motion. Precise regularity, independence and neighbourhood qualifications are part of the mathematical problem, rather than consequences of these informal words.

Lie objects in particular to replacing a finite motion group by its first-order truncation and treating the resulting infinitesimal group as if it retained the original invariant and mobility properties. First-order terms need not retain that information. The critique in Chapter 21, §§91–96, and Merker's discussion in *Sophus Lie, Friedrich Engel et le problème de Riemann–Helmholtz*, §§2.4–2.6, concern that passage, not a denial that valid infinitesimal methods exist. Lessons 2–6 supply the hypotheses and integration arguments under which such methods work.

The historical word “essential” needs care. Chapter 20 defines an invariant of a configuration as *essential* when it cannot be expressed through invariants of configurations with fewer points (p. 399). Thus “no essential invariant” for more than two points means generation by the pair invariants, not the absence of nonconstant or functionally independent invariants. This differs from the ordinary functional-independence usage in a compressed modern formulation. The complete introduction translated below states the pairwise-generation condition explicitly (pp. 397–398). Even three Euclidean points have three independent pair distances near a noncollinear configuration. To see independence, move the first point to zero, the second to $(a,0,0)$, and the third to $(b,c,0)$, where $a,c>0$. The squared distances are

$$
a^2,\qquad b^2+c^2,\qquad (b-a)^2+c^2.
\tag{1.1}
$$

Their Jacobian with respect to $(a,b,c)$ has determinant $8a^2c\ne0$. Thus they are local independent invariants. For $m\ge3$ points in general position in three-dimensional Euclidean space, a motion fixing the configuration has zero infinitesimal stabilizer: fixing three noncollinear points fixes their spanning plane pointwise, and a skew matrix vanishing on that plane is zero. The six-dimensional motion orbit therefore has codimension $3m-6$. Pair distances generate these local invariants: their values give the Gram matrix of the displacement vectors by

$$
\langle v_i,v_j\rangle
=\tfrac12\bigl(|v_i|^2+|v_j|^2-|v_i-v_j|^2\bigr).
$$

A Gram matrix determines such a configuration up to an orthogonal motion. When restricting to orientation-preserving motions, the possible orientation sign is discrete; it is fixed on a sufficiently small regular neighbourhood and supplies no additional essential continuous invariant.

Lie's first solution begins with the Chapter 22 introduction on pp. 471–472; §97, the plane case, occupies pp. 472–477; the three-dimensional conclusion is Theorem 40 in §98, pp. 477–479. His second solution occupies Chapter 23, pp. 498–523. The modern theorem below uses a precise compact isotropy condition and derives a metric. We do not identify that condition with every historical version of free mobility.

## 2. Recovering an invariant metric

Fix a base point $p$ of a transitive local action. Derivatives at $p$ of transformations fixing $p$ act linearly on $T_pM$. For a local group, make the compactness assumption precise as follows: these local derivatives are contained in a compact subgroup $K\subset\mathrm{GL}(T_pM)$. Equivalently, the subgroup they generate has compact closure. Compactness of just a small bounded parameter neighbourhood would say nothing useful.

The only measure-theoretic input is Haar existence and uniqueness: every locally compact Hausdorff group has a nonzero left-invariant Radon measure, unique up to positive scalar. These are Theorems 8.3 and 9.2 of Haar measure on locally compact groups. On a compact group its total mass is positive and finite, so normalize it to one. Right translation of this probability measure is again a left-invariant probability measure, and uniqueness makes it unchanged. Thus normalized compact Haar measure is both left and right invariant.

**Theorem 2.1 (invariant metric).** A transitive analytic local action satisfying this compact derivative-isotropy condition preserves a positive-definite analytic Riemannian metric near $p$.

**Proof.** Choose any positive inner product $b_0$ on $T_pM$ and set

$$
b(v,w)=\int_K b_0(kv,kw)\,d\mu(k).
\tag{2.1}
$$

It is a bilinear positive inner product: the integrand for $v=w\ne0$ is everywhere positive, and is continuous on the compact group. Right invariance gives $b(k_0v,k_0w)=b(v,w)$. Hence every local isotropy derivative preserves $b$.

Write $T_a(x)=x\cdot a$ for the right action. Then $T_b\circ T_a=T_{ab}$. The transitive orbit map has a local analytic section $q\mapsto a(q)$ with $p\cdot a(q)=q$, by the orbit-chart argument in lesson 8. Define

$$
g_q(DT_a|_p v,DT_a|_p w)=b(v,w),\qquad p\cdot a=q.
\tag{2.2}
$$

If $b'$ is another sufficiently small parameter sending $p$ to $q$, the transformation $T_{b'}^{-1}\circ T_a=T_{a(b')^{-1}}$ fixes $p$. Its derivative preserves $b$, proving independence of the choice in (2.2). The section and the derivatives of the action are analytic, so $g$ is analytic and positive definite. Finally, composing $T_a$ with $T_c$ represents transport to $q\cdot c$ by $ac$; formula (2.2) proves $T_c^*g=g$ wherever the local action and its compositions are defined. Shrink the neighbourhood once to ensure these assertions have common domains. $\square$

The construction does not assume in advance that isotropy is determined by its derivative. That conclusion follows from the metric, as we now prove. This avoids the first-order faithfulness problem encountered for projective isotropy in lesson 11.

## 3. Isometries and their first derivatives

We recall explicitly the local geometry used here. A positive metric has a unique torsion-free metric connection. In coordinates its coefficients are

$$
\Gamma^k_{ij}=\tfrac12g^{k\ell}
(\partial_i g_{j\ell}+\partial_j g_{i\ell}-\partial_\ell g_{ij}).
\tag{3.1}
$$

The displayed symmetry gives zero torsion, and substitution gives $\nabla g=0$. Conversely, writing metric compatibility for three permutations of $i,j,\ell$, and using zero torsion, solves for (3.1); this proves uniqueness. Geodesics solve $\ddot x^k+\Gamma^k_{ij}\dot x^i\dot x^j=0$. Local ODE existence and uniqueness give the exponential map $\exp_p(v)$ at time one, whose derivative at $v=0$ is the identity because the linear variation from the constant geodesic is $tv$. The inverse theorem supplies a normal-coordinate neighbourhood. All these constructions are analytic for an analytic metric; the smooth versions also suffice below.

An isometry preserves the connection, by its uniqueness, and therefore preserves geodesics with their parameters. Consequently an isometry $f$ satisfies

$$
f(\exp_p v)=\exp_{f(p)}(Df_pv)
\tag{3.2}
$$

on a small normal neighbourhood. In particular, its germ is determined by $f(p)$ and $Df_p$. An isometry fixing $p$ with derivative the identity is the identity germ.

A Killing field is a field $X$ with $\mathcal L_Xg=0$. Its local flow consists of isometries, since
$\frac d{dt}(\Phi_X^t)^*g=(\Phi_X^t)^*\mathcal L_Xg=0$; the converse follows by differentiating at zero. Metric compatibility and zero torsion give

$$
(\mathcal L_Xg)(u,v)=g(\nabla_uX,v)+g(u,\nabla_vX).
\tag{3.3}
$$

For example, expand the Lie derivative as $Xg(u,v)-g([X,u],v)-g(u,[X,v])$ and use $[X,u]=\nabla_Xu-\nabla_uX$ to obtain (3.3). Thus $(\nabla X)_p$ is skew with respect to $g_p$ for a Killing field. Killing fields form a Lie algebra because $\mathcal L_{[X,Y]}=[\mathcal L_X,\mathcal L_Y]$.

**Theorem 3.1 (first-jet determination and dimension).** For a connected $n$-dimensional Riemannian manifold, the map

$$
X\longmapsto\bigl(X(p),(\nabla X)_p\bigr)
\quad\text{from Killing fields to }T_pM\oplus\mathfrak{so}(T_pM,g_p)
\tag{3.4}
$$

is injective. Hence

$$
\dim\operatorname{Kill}(M,g)\le n+\frac{n(n-1)}2
=\frac{n(n+1)}2.
\tag{3.5}
$$

The same injection and bound hold for local Killing-field germs.

**Proof.** Suppose the jet in (3.4) is zero. Since $X(p)=0$, its flow fixes $p$. In coordinates $(\nabla X)_p=DX_p$ at a zero of $X$, and the derivative of the flow there is $e^{tDX_p}=I$. Equation (3.2) makes the flow the identity on a normal neighbourhood for small $t$. Differentiation gives $X=0$ there. This proves the germ assertion.

For a global field, the set of points where its first jet is zero is closed by continuity. The preceding local argument makes it open: every such point has a neighbourhood on which $X$ is identically zero. It is nonempty and the manifold is connected, so it is the whole manifold. This proves injection. The finite-dimensional target has the dimension in (3.5), proving the bound even without assuming finite-dimensionality of the space of Killing fields beforehand. $\square$

In particular, an effective metric-preserving local action has faithful derivative isotropy. If an infinitesimal isotropy field has zero derivative, Theorem 3.1 makes it the zero germ, and effectiveness excludes it from the acting algebra.

## 4. From isotropy to constant curvature

Our curvature convention is

$$
R(U,V)W=\nabla_U\nabla_VW-\nabla_V\nabla_UW-\nabla_{[U,V]}W,
\qquad
K(\langle u,v\rangle)=
\frac{g(R(u,v)v,u)}{g(u,u)g(v,v)-g(u,v)^2}.
\tag{4.1}
$$

Isometries preserve $R$ because they preserve the connection. Therefore isotropy acts on the function assigning sectional curvature to a two-plane at $p$.

**Theorem 4.1 (constant curvature).** In dimension $n\ge2$, if the action in Theorem 2.1 has isotropy transitive on the unoriented two-planes of $T_pM$, then its invariant metric has constant sectional curvature near $p$.

**Proof.** Isotropy invariance and plane transitivity give a single value $K$ at $p$. Transitivity of the action carries each nearby point to $p$ by an isometry and carries its tangent two-planes bijectively to those at $p$. Thus their curvature is the same value $K$. For $n=2$ there is just one tangent two-plane at each point, so the plane condition is automatic; transitivity still makes its Gaussian curvature constant. $\square$

This homogeneous argument does not need Schur's lemma. Schur's lemma concerns a metric with plane-independent curvature at each point without assuming any transitive motions; it is proved in Solution 2.

For later use, constant sectional curvature is equivalent to the full tensor identity

$$
R(U,V)W=K\bigl(g(V,W)U-g(U,W)V\bigr).
\tag{4.2}
$$

Here is the polarization step, including the algebraic identities it uses. At a normal-coordinate origin, put $R_{abcd}=g(R(\partial_a,\partial_b)\partial_c,\partial_d)$ and use a comma for ordinary coordinate derivatives. Substitution in (3.1) gives

$$
R_{abcd}=\tfrac12
(g_{bd,ac}+g_{ac,bd}-g_{bc,ad}-g_{ad,bc}).
$$

Symmetry of the metric and commutation of its second derivatives give antisymmetry in the first two and last two indices, pair interchange, and the cyclic first Bianchi identity, with each metric derivative cancelling its opposite. These are tensor identities and hence hold everywhere. Subtract the right side of (4.2) from $R$ and let $T(x,y,z,w)$ be its inner product with $w$. Zero sectional curvature says $T(x,y,y,x)=0$. Polarizing the outer $x$ and using pair interchange gives $T(x,y,y,z)=0$. Polarizing the repeated $y$ then gives $T(x,y,w,z)+T(x,w,y,z)=0$. Along with the two original antisymmetries this makes $T$ alternating in all four arguments. The cyclic first Bianchi identity is therefore $3T=0$. Thus $T=0$, proving (4.2).

## 5. A full local uniqueness argument

We next show that constant $K$ determines the local metric, rather than importing a global space-form classification. Put

$$
S_K(r)=
\begin{cases}
\sin(\sqrt K r)/\sqrt K,&K>0,\\
r,&K=0,\\
\sinh(\sqrt{-K}r)/\sqrt{-K},&K<0.
\end{cases}
\tag{5.1}
$$

**Theorem 5.1 (local space-form uniqueness).** Two Riemannian manifolds of the same dimension and the same constant sectional curvature $K$ are locally isometric near any chosen points. Every linear isometry between their tangent spaces extends to such a local isometry.

**Proof.** Work in a small normal ball about $p$. For a unit vector $v$, the radial geodesic is $\gamma(r)=\exp_p(rv)$. Vary $v$ through unit vectors with derivative $w\perp v$. The variation field $J$ has $J(0)=0$ and $D_rJ(0)=w$. Commuting the two covariant derivatives of the geodesic variation, and using zero torsion to interchange its velocity derivatives, gives

$$
D_r^2J+R(J,\dot\gamma)\dot\gamma=0.
\tag{5.2}
$$

For clarity, if $T=\partial_r\gamma$ and $J=\partial_s\gamma$, then $[T,J]=0$, $\nabla_JT=\nabla_TJ$, and $\nabla_TT=0$. Thus $R(J,T)T=-\nabla_T\nabla_JT=-D_r^2J$, which is (5.2).

Parallel transport is an isometry by $\nabla g=0$. Formula (4.2) and the initial conditions show that the unique solution is

$$
J(r)=S_K(r)P_rw,
\tag{5.3}
$$

where $P_r$ is parallel transport along $\gamma$. Indeed, this field stays perpendicular to $\dot\gamma$, and (5.2) becomes the scalar equation $S_K''+KS_K=0$, $S_K(0)=0$, $S_K'(0)=1$. Uniqueness of the linear ODE gives (5.3).

The radial direction has unit length and is orthogonal to these angular variations, by (5.3). Consequently the metric in polar normal coordinates is exactly

$$
g=dr^2+S_K(r)^2g_{\mathrm{round}},
\tag{5.4}
$$

where $g_{\mathrm{round}}$ is the unit-sphere metric in $T_pM$. Choose the normal ball small enough that $S_K(r)>0$ for $r>0$. Given a linear tangent isometry $L:T_pM\to T_{p'}M'$, the map $\exp_{p'}\circ L\circ\exp_p^{-1}$ has the same radial and angular metric by (5.4), and is an isometry off the centre. It is smooth across the centre by its normal-coordinate definition, so the metric equality extends there by continuity. This proves both assertions. $\square$

No completeness, simple connectivity or global covering assertion enters this proof. The word *local* in the space theorem is essential.

## 6. The three models and their motion algebras

For $K=0$ the model is $\mathbb R^n$ with its Euclidean metric. Its motions $q\mapsto Aq+b$, $A\in\mathrm{SO}(n)$, have infinitesimal fields

$$
X_{a,B}(q)=a+Bq,\qquad B^T=-B.
\tag{6.1}
$$

There are $n+n(n-1)/2$ independent fields. Their flows preserve the metric. The abstract motion algebra is $\mathfrak e(n)=\mathfrak{so}(n)\ltimes\mathbb R^n$.

For $K>0$, put $R=1/\sqrt K$ and use the sphere

$$
S_R^n=\{q\in\mathbb R^{n+1}:|q|^2=R^2\}
\tag{6.2}
$$

with its induced metric. The group $\mathrm{SO}(n+1)$ acts transitively by isometries. The stabilizer of a point acts on its tangent space as $\mathrm{SO}(n)$: extend an oriented orthonormal tangent frame by the radial unit normal to see both assertions.

For $K<0$, put $R=1/\sqrt{-K}$ and write the ambient bilinear form as $\langle(u,t),(u',t')\rangle=u\cdot u'-tt'$. The model is

$$
H_R^n=\{(u,t):|u|^2-t^2=-R^2,\ t>0\}
\tag{6.3}
$$

with the induced positive metric. To check positivity, a tangent vector $(v,s)$ satisfies $u\cdot v=ts$. Hence
$|v|^2-s^2\ge(1-|u|^2/t^2)|v|^2>0$ unless the vector is zero. The identity component $\mathrm{SO}^+(n,1)$ preserves this sheet and its metric. It acts transitively, with tangent isotropy $\mathrm{SO}(n)$: choose an orthonormal tangent basis and the future unit timelike normal, then map one such ambient orthonormal basis to another. Choices of orientation give the identity-component motion taking the prescribed nearby points and frames to each other; this suffices for the local action, and continuation along paths gives transitivity of the whole sheet.

Here is a direct curvature calculation for both nonzero models. Let the ambient normal be $N=q/R$ and let $\varepsilon=\langle N,N\rangle$, equal to $1$ for the sphere and $-1$ for the hyperboloid. Ambient differentiation gives $D_UN=U/R$ and

$$
h(U,V):=\langle D_UV,N\rangle=-g(U,V)/R,
\qquad D_UV=\nabla_UV+\varepsilon h(U,V)N.
$$

The tangential part defines the metric torsion-free connection. Taking the tangential part of the zero ambient curvature gives

$$
0=R(U,V)W+
\frac{\varepsilon}{R}\bigl(h(V,W)U-h(U,W)V\bigr).
$$

Consequently $R(U,V)W=(\varepsilon/R^2)(g(V,W)U-g(U,W)V)$, exactly (4.2). The curvatures are $1/R^2$ and $-1/R^2$ with our sign convention.

On these models the infinitesimal fields are $X_A(q)=Aq$, where $A$ is skew for the ambient bilinear form. Each is tangent and Killing, and their number is $n(n+1)/2$. They are independent as germs: if $Aq=0$ on an open patch, it annihilates the base point and the whole tangent space by differentiation, which together span the ambient space. Thus $A=0$. Theorem 3.1 shows that these are **all** the local Killing fields.

Matrix and field brackets have opposite signs:

$$
X_A,X_B=(BA-AB)q=-X_{[A,B]}(q).
\tag{6.4}
$$

The map $A\mapsto-X_A$ is therefore the Lie algebra isomorphism. The same minus sign identifies the affine matrix algebra with (6.1), using homogeneous coordinates. This agrees with the convention in lessons 6 and 9.

For dimension three the three algebras are

$$
\mathfrak e(3),\qquad\mathfrak{so}(4),\qquad\mathfrak{so}(3,1),
\tag{6.5}
$$

all of dimension six, with three-dimensional rotational isotropy. For dimension two they are

$$
\mathfrak e(2),\qquad\mathfrak{so}(3),\qquad\mathfrak{so}(2,1),
\tag{6.6}
$$

all of dimension three, with one-dimensional rotational isotropy. The last algebra is isomorphic to $\mathfrak{sl}_2(\mathbb R)$. An explicit verification uses

$$
J=\begin{pmatrix}0&-1&0\\1&0&0\\0&0&0\end{pmatrix},\quad
B_1=\begin{pmatrix}0&0&1\\0&0&0\\1&0&0\end{pmatrix},\quad
B_2=\begin{pmatrix}0&0&0\\0&0&1\\0&1&0\end{pmatrix}.
$$

For the form $\operatorname{diag}(1,1,-1)$ these have brackets
$[J,B_1]=B_2$, $[J,B_2]=-B_1$, $[B_1,B_2]=-J$.
Taking $H=2B_1$, $E=B_2-J$, $F=B_2+J$ gives $[H,E]=2E$, $[H,F]=-2F$, $[E,F]=H$, the real Chevalley relations. Thus (6.6) is also the familiar Euclidean, compact and split surface list. The real spherical action is primitive, although its complexification is outside the primitive complex-plane list in lesson 11: complexification admits invariant complex directions in the isotropy representation.

## 7. The modern space theorem and maximal mobility

**Theorem 7.1 (local space theorem).** Let an effective finite-dimensional analytic local action be transitive near $p$ on a real three-manifold. Suppose its derivative isotropy Lie algebra, after a linear change of tangent coordinates, is exactly $\mathfrak{so}(3)$. Then it preserves an analytic Riemannian metric of constant sectional curvature. In local isometric coordinates its algebra is the full motion algebra of one of the three models in (6.5).

In dimension two the analogous assumption is derivative isotropy $\mathfrak{so}(2)$, and the conclusions are the three models and algebras in (6.6).

**Proof.** Restrict to transformations in the identity neighbourhood of the local group. The derivative isotropy is locally generated by exponentials of the indicated matrix Lie algebra, so it is contained in $\mathrm{SO}(3)$, or $\mathrm{SO}(2)$ in the surface case. This is the compact condition of Theorem 2.1. Its averaged metric is invariant. Relative to that metric the derivative isotropy is the full orthogonal Lie algebra: it preserves the metric, has the same dimension as that orthogonal algebra, and is contained in it. In dimension three the resulting rotations act transitively on two-planes; in dimension two there is only one such plane. Theorem 4.1 gives constant $K$.

Theorem 3.1 makes derivative isotropy faithful. Thus the acting algebra has dimension $3+3=6$, or $2+1=3$, by the orbit–isotropy exact sequence. Theorem 5.1 identifies the metric locally with the corresponding model in Section 6. Pushforward carries the acting algebra into the model's Killing algebra. Their equal dimensions and the model calculation show that the inclusion is equality, proving the asserted equivalence of actions and the algebra isomorphisms. $\square$

The same proof works in dimension $n\ge2$ with full derivative isotropy $\mathfrak{so}(n)$. A hypothesis merely saying that some noncompact linear group moves tangent directions transitively does not give its first step. For example, $\mathrm{GL}^+(3)$ moves directions and two-planes transitively but contains every positive dilation. An invariant inner product at a fixed point would have to satisfy $b(\lambda v,\lambda v)=b(v,v)$, impossible for $\lambda\ne1$. Section 2 uses compactness, not just direction transitivity.

**Theorem 7.2 (equality in the Killing bound).** If a connected Riemannian $n$-manifold, $n\ge2$, has $n(n+1)/2$ independent global Killing fields, it has constant sectional curvature. At the level of germs, constant-curvature metrics attain this bound. In particular, a connected three-manifold has at most six global Killing fields, and equality forces constant curvature.

**Proof.** Equality makes the injective map (3.4) surjective at every point. Evaluation is therefore onto, and the Killing fields vanishing at the point realize every skew derivative there. Choose $n$ fields whose values form a basis; their successive local flows give an open orbit by the inverse theorem. The local Killing action is transitive. Its isotropy realizes all infinitesimal rotations, and their flows act as the rotation group on tangent planes. The argument of Theorem 4.1 makes curvature constant in a neighbourhood of each point. These neighbourhood values agree on overlaps, and connectedness makes the value constant on the whole manifold. Conversely, Theorem 5.1 and the independent model fields in Section 6 supply $n(n+1)/2$ Killing germs for every constant-curvature metric. $\square$

This last converse is deliberately about germs. A constant-curvature quotient can have fewer global Killing fields, because a model field need not descend through its identifications. Nor does the local positive-curvature model decide whether a global geometry is spherical or elliptic. Completeness, topology and covering spaces are additional questions.

## 8. What the three geometries share and what differs

All three models have the same local freedom to choose a point and an orthonormal frame. Their curvature signs distinguish the geometries: in (5.4), nearby radial angular distances scale as $S_K(r)=r-Kr^3/6+O(r^5)$. Compared with the flat model, positive curvature makes this scale smaller and negative curvature makes it larger. This follows directly by expanding (5.1), and describes an actual local measurement rather than just three abstract algebra names.

Lie's work puts the finite transformation group and its isotropy at the centre of the classification. The tensor and frame language used above leads to the later metric and connection formulations associated with Weyl and Cartan. Merker's historical and mathematical account separates Riemann's metric assumption, Helmholtz's mobility assumptions, and Lie's classifications. The distinction remains useful: specifying which objects are invariant is part of a theorem's hypotheses. It cannot be replaced by a count of informal degrees of freedom.

## 9. Exercises

**Exercise 1 (introductory).** Show that $\mathrm{SO}(3)$ acts transitively on the unoriented two-planes of $\mathbb R^3$. Explain how this is used in the curvature argument.

**Exercise 2 (intermediate).** Prove Schur's lemma: in a connected Riemannian manifold of dimension $n\ge3$, if sectional curvature at each point is independent of the two-plane, its value is constant. Explain the failure in dimension two.

**Exercise 3 (intermediate).** Compute all Killing fields of the round unit sphere $S^2$. Give their spherical-coordinate formulas, their brackets, and the dimension.

**Exercise 4 (intermediate).** Explain why the affine group acting on $\mathbb R^3$ cannot preserve a positive Riemannian metric, although its isotropy moves directions and two-planes transitively.

**Exercise 5 (advanced).** Prove $\dim\operatorname{Kill}(M,g)\le n(n+1)/2$ for every connected Riemannian $n$-manifold, without assuming beforehand that its Killing fields form a finite-dimensional space. State the distinction between the local and global equality conclusions.

## 10. Solutions

**Solution 1.** A two-plane is the orthogonal complement of a unit normal, with the two choices of normal defining the same plane. Given planes with normals $u,v$, complete $u$ and $v$ to positively oriented orthonormal bases. The unique orthogonal map between these bases has determinant one and sends $u^\perp$ to $v^\perp$. Hence the action is transitive. Because isometries preserve the curvature tensor, isotropy transitivity makes all sectional curvatures at the fixed point equal; transitive motions then give the same value at nearby points.

**Solution 2.** Denote the plane-independent value by $K(p)$. It is smooth, since it can be evaluated on any local orthonormal pair. The polarization argument in Section 4 gives (4.2), so

$$
\operatorname{Ric}=(n-1)Kg,\qquad \operatorname{scal}=n(n-1)K.
\tag{10.1}
$$

We need the contracted differential Bianchi identity

$$
\nabla^i\operatorname{Ric}_{ij}=\tfrac12\partial_j\operatorname{scal}.
\tag{10.2}
$$

Here is its derivation. In normal coordinates at an arbitrary point, $\Gamma=0$ and the curvature components are the alternating first derivatives of $\Gamma$, with the usual quadratic $\Gamma\Gamma$ terms. In the cyclic sum

$$
(\nabla_a R)(b,c)d+(\nabla_b R)(c,a)d+(\nabla_c R)(a,b)d
$$

the quadratic terms and their first derivatives vanish at the point, while each second partial derivative of a connection coefficient occurs twice with opposite signs. Commutation of ordinary partial derivatives makes the sum zero. This proves the differential Bianchi identity there, and hence tensorially everywhere. To see the contraction signs explicitly, use $R_{abcd}=g(R(e_a,e_b)e_c,e_d)$ in an orthonormal frame at the point. The differential identity is

$$
\nabla_aR_{bcde}+\nabla_bR_{cade}+\nabla_cR_{abde}=0.
$$

Contract $a=d$ and use $\operatorname{Ric}_{ce}=\sum_a R_{acea}$ to obtain

$$
\sum_a\nabla_aR_{bcae}+\nabla_b\operatorname{Ric}_{ce}
-\nabla_c\operatorname{Ric}_{be}=0.
$$

Now contract $b=e$. The first two terms are both $\nabla^a\operatorname{Ric}_{ca}$, and the last is $-\partial_c\operatorname{scal}$. This gives (10.2).

Substituting (10.1) in (10.2) gives

$$
(n-1)dK=\tfrac12n(n-1)dK,
\qquad (n-1)(n-2)dK=0.
$$

For $n\ge3$ this says $dK=0$. Connectedness gives constancy. In dimension two every point has only one tangent two-plane, so the assumption imposes no condition. For an explicit counterexample use $g=dx^2+f(x)^2dy^2$ with $f=e^{x^2}$. Formula (3.1) gives $\Gamma^x_{yy}=-ff'$ and $\Gamma^y_{xy}=\Gamma^y_{yx}=f'/f$, with the other coefficients zero. Then $R(\partial_x,\partial_y)\partial_y=-ff''\partial_x$, so $K=-f''/f=-(2+4x^2)$, which varies.

**Solution 3.** Let $q=(\sin\theta\cos\phi,\sin\theta\sin\phi,\cos\theta)$. Rotation about an axis $a$ has field $X_a(q)=a\times q$. For the three standard axes these are

$$
X_1=-\sin\phi\,\partial_\theta-\cot\theta\cos\phi\,\partial_\phi,
\qquad
X_2=\cos\phi\,\partial_\theta-\cot\theta\sin\phi\,\partial_\phi,
\qquad X_3=\partial_\phi.
\tag{10.3}
$$

These coordinate formulas hold away from the poles; the ambient formulas define smooth global fields. For instance, take the dot products of $e_1\times q$ with $\partial_\theta q$ and $\partial_\phi q$, dividing the latter by $\sin^2\theta$, to obtain the first formula. The other axes give the remaining two. The fields are Killing because rotations preserve the induced metric. A constant relation among them would say $a\times q=0$ for every $q$ on a patch, forcing $a=0$, so they are independent. The bound in Theorem 3.1 is three for a surface, proving that their span is the full global and local Killing algebra of the round sphere. Formula (6.4) gives $[X_a,X_b]=-X_{a\times b}$, in particular $[X_1,X_2]=-X_3$ and its cyclic counterparts. The map $a\mapsto-X_a$ identifies it with $\mathfrak{so}(3)$.

**Solution 4.** At the origin the affine stabilizer contains $q\mapsto\lambda q$ for every $\lambda>0$. If it were an isometry of some positive metric, its derivative would satisfy $\lambda^2g_0(v,v)=g_0(v,v)$ for every tangent vector. Choose $v\ne0$ and $\lambda\ne1$ to get a contradiction. Meanwhile any positively oriented basis can be sent to another by $\mathrm{GL}^+(3)$, so that isotropy is transitive on directions and on two-planes. Those transitivity assertions therefore cannot replace compactness in Theorem 2.1.

**Solution 5.** For a Killing field, (3.3) makes $(\nabla X)_p$ a skew endomorphism. If its value and covariant derivative both vanish at $p$, the flow fixes $p$ and has derivative $e^{tDX_p}=I$. By geodesic uniqueness it fixes every $\exp_pv$ in a normal ball, so $X$ vanishes there. The set of points with zero first jet is both closed and open; connectedness propagates that vanishing to all of $M$. Thus (3.4) is an injective linear map into a space of dimension $n+n(n-1)/2$. Any independent family of fields maps to an independent family of vectors there, giving the bound without a preliminary finite-dimensionality theorem.

For $n\ge2$, global equality forces constant curvature by Theorem 7.2; constant curvature gives local equality by its model identification. It need not give global equality on an arbitrary quotient. In dimension one the bound is one, and every metric is locally a Euclidean length coordinate, obtained by integrating its positive length density; there is no sectional-curvature assertion to make.

## What this lesson does not prove

Haar existence and uniqueness are imported in their exact measure-theoretic form from *Haar measure on locally compact groups*, Theorems 8.3 and 9.2. We prove the compact normalization and averaging consequences used here. We assume the local action and orbit theory of lessons 5–8 and the local ODE and inverse-function results located in lessons 3 and 1. The basic tensor operations of D50 are used, with the connection, first-jet, curvature-polarization, Jacobi, local-uniqueness and Killing-dimension arguments supplied above.

We do not prove that every historical formulation of Helmholtz's axioms implies the precise compact derivative-isotropy hypothesis of Theorem 7.1. Lie's different historical classification arguments are cited in Chapters 20–24 of Volume III. The modern theorem explicitly states the hypothesis it uses. Global space-form classification, completeness, covering-space descriptions, and the full subsequent theories of Weyl and Cartan are outside this lesson.

## References

- Sophus Lie, with Friedrich Engel, *Theorie der Transformationsgruppen*, Volume III (1893), fifth division, introduction, pp. 393–398; Chapter 20, §§85–90, pp. 399–436, with complete §85 on pp. 399–410; Chapter 21, §§91–96, pp. 437–470; Chapter 22, first solution, introduction pp. 471–472 and §97 pp. 472–477, especially §98, Theorem 40, pp. 477–479; Chapter 23, second solution, pp. 498–523; Chapter 24, pp. 524–534, and concluding remarks from p. 535. Printed chapter titles and pages govern these references.
- Joël Merker, *Sophus Lie, Friedrich Engel et le problème de Riemann–Helmholtz*, [arXiv:0910.0801](https://arxiv.org/abs/0910.0801), especially §§2.4–2.6 for Helmholtz's hypotheses and Lie's critique. The present proofs and English prose are independently written.
- *Haar measure on locally compact groups*, course lesson, Theorems 8.3 and 9.2, for Haar existence and uniqueness.
- [Differential Geometry, D50](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D50), for the prerequisite differential-geometric language.

