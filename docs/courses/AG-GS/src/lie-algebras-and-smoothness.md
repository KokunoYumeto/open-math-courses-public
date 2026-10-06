# Lie algebras and smoothness of group schemes

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

The identity of a group scheme is a place where infinitesimal geometry becomes algebra. First-order multiplication adds tangent vectors. Conjugation supplies an action on them, and its first-order variation supplies a bracket. Translation then transports the geometry at the identity to every point. This lesson uses that transport twice: to recognize smoothness from one tangent space, and to prove why characteristic zero rules out infinitesimal algebraic groups.

Throughout the field arguments, \(k\) is a field. A **locally algebraic** group scheme means a group scheme locally of finite type over \(k\); it need not be affine or quasi-compact. The first section also applies without the finite-type condition. Sections 1.4 and 2.3 explicitly pass to an arbitrary base ring \(R\), keeping the distinction between the tangent functor and its module of base-valued vectors. We use the Hopf and differential constructions from *Group schemes, actions and Hopf algebras*. The scheme-theoretic prerequisites are tangent spaces, regular local rings, smoothness over fields, and descent of smoothness under field extension. Exact imported statements are collected at the end.

## 1. The tangent functor at the identity

For a \(k\)-algebra \(A\), write \(A[\epsilon]=A[T]/(T^2)\), where \(\epsilon\) is the class of \(T\), and put

\[
\mathfrak g(A)=
\ker\bigl(G(A[\epsilon])\longrightarrow G(A)\bigr).
\]

The arrow sets \(\epsilon\) to zero. Its kernel is a group, and its elements reduce to the identity section, rather than to an arbitrary point of \(G(A)\). At \(A=k\) this is the tangent space at the identity. Denote it by \(\operatorname{Lie}(G)\), or \(\mathfrak g\).

**Proposition 1.1.** There is a natural identification

\[
\operatorname{Lie}(G)=T_eG
\simeq\operatorname{Hom}_k(e^*\Omega_{G/k},k).
\]

Under it, multiplication in the kernel is vector addition, inversion is negation, and the substitution \(\epsilon\mapsto c\epsilon\) is multiplication by \(c\in k\). The construction is functorial in \(G\) and preserves kernels and fibre products.

**Proof.** A map from the dual numbers reducing to \(e\) factors through any affine neighbourhood of \(e\). If that neighbourhood has ring \(B\), with evaluation \(q:B\to k\), the map has the form

\[
b\longmapsto q(b)+\epsilon v(b).
\]

It is an algebra map exactly when \(v\) is \(k\)-linear and

\[
v(bb')=q(b)v(b')+q(b')v(b).
\]

By the defining property of Kähler differentials, these derivations are the linear functionals on \(\Omega_{B/k}\otimes_{B,q}k=e^*\Omega_{G/k}\). The description is unaffected by shrinking the neighbourhood, so it is intrinsic.

The differential of multiplication is addition, as proved in the preceding lesson: its restrictions to the two tangent summands are identities. Its inverse therefore gives negation. The scalar substitution gives \(cv\) in the displayed formula. A group homomorphism differentiates by composition with pullback of functions, hence gives a linear map.

Finally, a point of the schematic kernel of \(f:G\to H\) is exactly a point of \(G\) sent to the identity of \(H\). Applying this both to \(k[\epsilon]\) and to \(k\) gives

\[
\operatorname{Lie}(\ker f)
=\ker\bigl(\operatorname{Lie}(G)\to\operatorname{Lie}(H)\bigr).
\]

The same pointwise argument for a fibre product gives

\[
\operatorname{Lie}(G_1\times_HG_2)
=\operatorname{Lie}(G_1)\times_{\operatorname{Lie}(H)}
\operatorname{Lie}(G_2).
\]

These equalities use the schematic kernels and products, including their nilpotents. \(\square\)

For an affine group with Hopf algebra \(B\) and augmentation ideal \(I\), this becomes

\[
\mathfrak g=\operatorname{Hom}_k(I/I^2,k).
\]

Indeed, \(B=k\oplus I\) as a vector space; the derivation vanishes on \(k\) and on \(I^2\), and every functional on \(I/I^2\) satisfies the required Leibniz rule.

If \(G\) is locally algebraic, \(\omega=e^*\Omega_{G/k}\) is finite-dimensional. The same derivation argument over every \(A\) gives

\[
\mathfrak g(A)=\operatorname{Hom}_A(\omega\otimes_kA,A)
=\mathfrak g\otimes_kA.
\tag{1}
\]

Thus its tangent functor is represented by the vector group associated to \(\mathfrak g\). Finite-dimensionality justifies commuting the dual with scalar extension here.

**Example 1.2. Matrix groups.** For \(\mathrm{GL}_r\), every first-order point at the identity is uniquely \(1+\epsilon X\), with \(X\in M_r(k)\); its inverse is \(1-\epsilon X\). Thus

\[
\operatorname{Lie}(\mathrm{GL}_r)=M_r(k).
\]

Expansion of the determinant gives

\[
\det(1+\epsilon X)=1+\epsilon\operatorname{tr}(X).
\]

One way to check the coefficient is to expand the permutation formula. Only the identity permutation can contribute a term containing just one \(\epsilon\), and its contributions are the diagonal entries. Consequently

\[
\operatorname{Lie}(\mathrm{SL}_r)
=\{X:\operatorname{tr}(X)=0\}.
\]

The formula holds even when the characteristic divides \(r\). Scalar matrices then belong to this trace-zero space, but the trace map remains surjective because \(\operatorname{tr}(E_{11})=1\).

**Example 1.3. One-dimensional and infinitesimal groups.** The first-order points of \(\mathbf G_a\) are \(c\epsilon\); those of \(\mathbf G_m\) are \(1+c\epsilon\). Both Lie spaces are \(k\). For \(\mu_n\),

\[
(1+c\epsilon)^n=1+nc\epsilon,
\qquad
\operatorname{Lie}(\mu_n)=\{c\in k:nc=0\}.
\]

It is zero if \(n\) is invertible in \(k\), and is one-dimensional if \(\operatorname{char}(k)=p\) divides \(n\). For \(\alpha_p\), \((c\epsilon)^p=0\), so \(\operatorname{Lie}(\alpha_p)=k\). The last two groups have dimension zero despite having a tangent direction.

Left exactness has no automatic surjectivity clause. In characteristic \(p\), the homomorphism \(F:\mathbf G_a\to\mathbf G_a\), \(x\mapsto x^p\), has zero differential although it is faithfully flat: \(k[x]\) is free over \(k[x^p]\), with basis \(1,x,\ldots,x^{p-1}\).

### 1.4. Tangent vectors over a ring

The field hypothesis hides a dualization issue. To see it, let \(R\) be any commutative ring and let \(G/R\) be a group scheme, without an affineness or finiteness assumption. Put \(\omega_G=e^*\Omega_{G/R}\), viewed as an \(R\)-module. The same definition with dual numbers gives a functor on \(R\)-algebras.

**Proposition 1.4. The relative tangent functor.** There are natural identifications

\[
\begin{gathered}
\ker(G(A[\epsilon])\to G(A))\\
 \simeq\operatorname{Hom}_R(\omega_G,A)\\
 \simeq\operatorname{Hom}_A(\omega_G\otimes_R A,A).
\end{gathered}
\]

Its group law is addition. It is represented by \(\operatorname{Spec}_R\operatorname{Sym}_R\omega_G\). If \(\omega_G\) is finite projective, then

\[
\operatorname{Lie}(G_A/A)
 \simeq\operatorname{Lie}(G/R)\otimes_R A
\]

for every \(R\)-algebra \(A\). This hypothesis holds when \(G/R\) is smooth and locally of finite presentation.

**Proof.** On an affine neighbourhood of a portion of the identity section, a lift to dual numbers is the identity evaluation plus \(\epsilon\) times a derivation. The derivation is exactly a map from the pullback of relative differentials to \(A\). These descriptions agree on intersections and glue along the identity section; hence they also apply when the whole section has no single affine neighbourhood. The two identities for multiplication with the identity show that its first differential is the sum of the two directions. Terms involving two directions vanish because \(\epsilon^2=0\). This gives the additive law without any assumption on \(R\).

An algebra map \(\operatorname{Sym}_R\omega_G\to A\) is exactly an \(R\)-linear map \(\omega_G\to A\), proving representability. Relative differentials commute with arbitrary base change, so the cotangent module after extension is \(\omega_G\otimes_R A\). For a finite projective module, dualization commutes with arbitrary scalar extension: prove this for a finite free module using its dual basis, then pass to a direct summand. This proves the displayed module formula. Smoothness makes the cotangent sheaf finite locally free near each point of the identity section; its pullback is finite locally free on the base. Over an affine base this is a finite projective module. \(\square\)

**Example 1.5. Failure of the module formula.** Let \(R\) be a discrete valuation ring with uniformizer \(\pi\), and give

\[
G=\operatorname{Spec}R[t]/(\pi t)
\]

the additive Hopf structure \(\Delta(t)=t\otimes1+1\otimes t\). The relation \(\pi t\) is preserved by multiplication, the identity and inversion, so this is a group scheme. Its identity cotangent module is \(R/\pi R\). Consequently

\[
\operatorname{Lie}(G/R)=\operatorname{Hom}_R(R/\pi R,R)=0,
\qquad
\operatorname{Lie}(G_{R/\pi R}/(R/\pi R))=R/\pi R.
\]

Thus the tangent **functor** commutes with base change, while the module of its \(R\)-valued vectors need not do so. The representing scheme in Proposition 1.4 is still valid; it is not generally a vector bundle.

**Proposition 1.6. Square-zero lifting for groups.** Let \(C\) be an \(R\)-algebra and \(J\subset C\) an ideal with \(J^2=0\). Then

\[
\ker(G(C)\to G(C/J))\simeq\operatorname{Hom}_R(\omega_G,J)
\]

as additive groups. Every nonempty fibre of this map is a principal homogeneous set under this kernel. If \(G/R\) is smooth, the map is surjective, including for nonaffine \(G\). The same surjectivity holds for every nilpotent ideal \(J\).

**Proof.** There is a distinguished lift of the identity, namely \(e_C\). Any other lift differs from its coordinate evaluations by a derivation into \(J\); the Leibniz rule has no quadratic correction since \(J^2=0\). The calculation in Proposition 1.4 therefore gives exactly the stated Hom module. The first differential of multiplication gives its addition. If \(g\) and \(h\) have the same reduction, then \(hg^{-1}\) belongs to the kernel, and is the unique kernel element carrying \(g\) to \(h\) by left multiplication. This proves the fibre assertion.

For a smooth scheme, choose a finite principal-open cover of \(\operatorname{Spec}C\) whose reductions map into smooth affine charts of \(G\). The smooth algebra lifting criterion gives local lifts. Their differences form a Čech one-cocycle in the quasi-coherent sheaf \(\operatorname{Hom}(\bar g^*\Omega_{G/R},\widetilde J)\), since smoothness makes the pulled-back cotangent module finite locally free. Affine quasi-coherent cohomology makes this cocycle a coboundary. Adjust the lifts by those derivations and glue them. This is precisely the complete gluing argument in [*Infinitesimal lifting and the invariance of étale morphisms under thickenings*, Theorem 4.1](../../AG-FSE/src/infinitesimal-lifting-and-invariance-under-thickenings.md). For a nilpotent ideal, use the finite sequence \(C/J^{i+1}\to C/J^i\); each kernel \(J^i/J^{i+1}\), for \(i\geq1\), is square-zero. Successive lifts give the required point of \(G(C)\). \(\square\)

These formulas also specify the base-change convention for a square-zero ideal: it is the actual ideal in the new algebra. For a flat extension \(C\to C'\), that ideal is \(J\otimes_C C'\subset C'\). Without flatness, this tensor product need not inject into \(C'\), so it cannot silently be substituted for the ideal.

**Proposition 1.7. Tangents to mapping functors.** Let \(f:X\to Y\) be a morphism of schemes over \(R\), and \(E\) an \(R\)-module. Morphisms over the split square-zero ring \(R\oplus E\), from \(X_{R\oplus E}\) to \(Y_{R\oplus E}\) with reduction \(f\), form the additive torsor

\[
\operatorname{Hom}_{\mathcal O_X}
\bigl(f^*\Omega_{Y/R},\mathcal O_X\otimes_RE\bigr),
\]

with origin the constant extension of \(f\). For \(Y=X\), \(f=1\), every such endomorphism is an automorphism. In particular

\[
\begin{gathered}
\operatorname{Lie}(\operatorname{Aut}_R(X))(A)\\
=\operatorname{Der}_A(\mathcal O_{X_A},\mathcal O_{X_A}).
\end{gathered}
\]

for every \(R\)-algebra \(A\), whether or not the automorphism functor is represented by a scheme. This is the module identification given by pullback. Its negative is the identification that preserves Lie brackets.

**Proof.** On compatible affine charts, two lifts have algebra maps differing by a derivation from the target algebra into the square-zero module of the source. The Leibniz rule follows by subtracting the two multiplicativity identities; their common reduction gives the module structure. Conversely adding such a derivation to the constant lift respects multiplication, since the square of the coefficient ideal is zero. The universal property of relative differentials identifies the derivations with the displayed Hom. All differences agree on chart overlaps, and local maps with the same reduction have the same underlying topological map, so this correspondence glues over arbitrary \(X,Y\).

For an identity lift, extend its derivation \(\delta\) to the square-zero thickening by making it zero on its coefficient ideal. Then \(\delta^2=0\), and \((1+\delta)(1-\delta)=1\). These inverses glue. With \(E=R\), composition adds the derivations, and replacing \(R\) by \(A\) gives the last formula. Composition of scheme automorphisms reverses the order of pullbacks. In two square-zero variables their group commutator therefore has pullback coefficient \(D_2D_1-D_1D_2\). Sending the pullback derivation \(D\) to \(-D\) gives the bracket-compatible identification with relative vector fields. This proves the mapping-functor and automorphism statements, including the sign convention, without a representability or flatness hypothesis on \(X\). \(\square\)

## 2. Conjugation and the bracket

Assume now that \(G\) is locally algebraic. For \(g\in G(A)\), conjugation by its constant lift to \(G(A[\epsilon])\) acts on the kernel in (1). It is \(A\)-linear, since it differentiates a morphism of \(A\)-schemes. It commutes with change of \(A\), is invertible, and respects products of \(g\)'s. Thus it defines a representation

\[
\operatorname{Ad}:G\longrightarrow\mathrm{GL}(\mathfrak g).
\]

Differentiating it at the identity gives

\[
\operatorname{ad}:\mathfrak g\longrightarrow
\operatorname{End}_k(\mathfrak g).
\]

Define

\[
[v,w]=\operatorname{ad}(v)(w).
\tag{2}
\]

Bilinearity is immediate. Alternation and Jacobi require proof, particularly in characteristic two, where skew-symmetry alone would not imply \([v,v]=0\).

We prove them through invariant vector fields, in a form that also works on a non-affine group. A vector field here is a \(k\)-derivation of the sheaf \(\mathcal O_G\) into itself.

**Lemma 2.1.** Evaluation at \(e\) identifies left-invariant vector fields on \(G\) with \(\mathfrak g\). For \(v\in\mathfrak g\), write \(L_v\) for its corresponding field. The commutator of two left-invariant fields is left-invariant.

**Proof.** The differential of left multiplication sends \(v\) at \(e\) to its translate at \(g\). Algebraically this is the dual of the invariant-differential isomorphism

\[
\Omega_{G/k}\simeq\mathcal O_G\otimes_k\omega
\]

proved in the preceding lesson. Since \(\omega\) is finite-dimensional, its dual identifies the tangent sheaf with \(\mathcal O_G\otimes_k\mathfrak g\). The constant section \(v\) in this trivialization gives \(L_v\). Associativity of multiplication makes it left-invariant after every base change. Conversely, invariance determines a field at every universal point from its value at \(e\), so evaluation and this construction are inverse.

There is a useful direct description. Let \(x_s\in G(k[s]/(s^2))\) represent \(v\). Right translation by \(x_s\) is an automorphism of the first-order thickening of \(G\), reducing to the identity. Its pullback on functions is

\[
r_{x_s}^*=1+sL_v.
\tag{3}
\]

At \(g\) its tangent direction is \(d(L_g)_e(v)\), exactly the field just constructed. Right translation commutes with left translation, which also proves invariance.

For derivations \(D,E\), expanding the Leibniz rule shows that \(DE-ED\) is a derivation: the mixed terms cancel. If both commute with pullback under left translations, their commutator does too. These computations apply on every open set and commute with restriction, so they prove the assertion for sheaf derivations. \(\square\)

**Theorem 2.2.** The bracket (2) corresponds to the commutator of invariant fields:

\[
L_{[v,w]}=L_vL_w-L_wL_v.
\tag{4}
\]

It makes \(\mathfrak g\) a Lie algebra in every characteristic. Differentials of group homomorphisms preserve this bracket.

**Proof.** Work over

\[
R=k[s,t]/(s^2,t^2).
\]

The coefficient \(st\) remains nonzero in this ring. Let \(x_s,y_t\in G(R)\) be the first-order points corresponding to \(v,w\), respectively. Differentiating \(\operatorname{Ad}\) means precisely that

\[
\operatorname{Ad}(x_s)(w)=w+s\operatorname{ad}(v)(w).
\]

Regarding \(R\) first as a dual-number algebra in \(t\) over \(k[s]/(s^2)\), first-order multiplication adds directions. Therefore the commutator

\[
c=x_sy_tx_s^{-1}y_t^{-1}
\]

is the point at the identity whose sole nonconstant term is the \(st\)-direction \(\operatorname{ad}(v)(w)\). In notation for such square-zero directions,

\[
c=e_{st}[v,w].
\tag{5}
\]

On the other hand, for right translations \(r_{ab}^*=r_a^*r_b^*\). Applying (3) and multiplying operators yields

\[
\begin{aligned}
r_c^*
&=(1+sL_v)(1+tL_w)(1-sL_v)(1-tL_w)\\
&=1+st(L_vL_w-L_wL_v).
\end{aligned}
\]

Equation (5), followed by (3) for the square-zero parameter \(st\), gives instead \(r_c^*=1+stL_{[v,w]}\). Comparing coefficients proves (4).

Commutators in any associative algebra are alternating and satisfy Jacobi. In detail, \([D,D]=DD-DD=0\), and the expansion of

\[
[D,[E,F]]+[E,[F,D]]+[F,[D,E]]
\]

contains each of \(DEF,DFE,EDF,EFD,FDE,FED\) twice with opposite signs. It is zero in every characteristic. Lemma 2.1 and (4) transfer these identities to \(\mathfrak g\). Bilinearity and alternation also give \([v,w]=-[w,v]\).

For a homomorphism \(f:G\to H\), the identity

\[
f(gug^{-1})=f(g)f(u)f(g)^{-1}
\]

first differentiates in \(u\) to give equivariance of \(df\) for the two adjoint actions. Differentiating again in \(g\) gives

\[
df([v,w])=[df(v),df(w)].
\]

This proves functoriality without requiring either group to be affine. \(\square\)

Every conjugation automorphism consequently acts by Lie algebra automorphisms. Jacobi also says that \(\operatorname{ad}(v)\) is a derivation of the bracket and that \(\operatorname{ad}\) is a Lie algebra homomorphism.

**Example 2.3. Matrices and signs.** For \(\mathrm{GL}_r\),

\[
\operatorname{Ad}(g)(X)=gXg^{-1}.
\]

Putting \(g=1+sY\) gives \(X+s(YX-XY)\). Hence

\[
[X,Y]=XY-YX.
\]

For a closed subgroup of \(\mathrm{GL}_r\), Proposition 1.1 injects its Lie algebra into \(M_r(k)\), and Theorem 2.2 identifies its bracket with this restriction. In particular the trace-zero matrices are closed under the bracket, since \(\operatorname{tr}(XY)=\operatorname{tr}(YX)\).

For \(\mathrm{SL}_2\), choose

\[
u=E_{12},\qquad v=E_{21},\qquad
h=\begin{pmatrix}1&0\\0&-1\end{pmatrix}.
\]

These remain a basis in characteristic two: then \(h\) is the identity matrix, and it still spans the one-dimensional diagonal trace-zero subspace. Direct multiplication gives

\[
[u,v]=h,\qquad[h,u]=2u,\qquad[h,v]=-2v.
\]

In characteristic two the last two brackets vanish; replacing this calculation by the familiar characteristic-zero classification would give the wrong answer.

For a commutative group scheme, conjugation is the identity on every test scheme. Its adjoint action is trivial and its bracket is zero. This applies to \(\mathbf G_a,\mathbf G_m,\mu_n,\alpha_p\), including the non-smooth examples.

### 2.3. The bracket over an arbitrary base

**Proposition 2.3. Relative invariant fields.** For every group scheme \(G/R\), evaluation at the identity identifies left-invariant relative derivations of \(\mathcal O_G\) with \(\operatorname{Hom}_R(\omega_G,R)\). Their commutator defines an alternating \(R\)-bilinear Lie bracket. Differentials of group homomorphisms preserve it. The canonical scalar-extension map on Lie modules preserves brackets, whether or not it is an isomorphism.

**Proof.** For \(v:\omega_G\to R\), Proposition 1.4 supplies the point \(x_s\in G(R[s]/s^2)\) reducing to the identity. Right translation by it acts on the sheaf of functions as \(1+sD_v\). Extracting the coefficient of \(s\) gives a relative derivation. It commutes with every left translation, since right and left translations commute. Its value at the identity is \(v\). Conversely, at a universal point \(g\), left invariance forces the field to be the image of its value at the identity under \(dL_g\). This proves uniqueness, and gives inverse constructions on every open chart without requiring the cotangent module to be projective.

Commutators of such derivations are derivations and are left invariant. Evaluation therefore gives a unique vector \([v,w]\). The operator computation

\[
(1+sD_v)(1+tD_w)(1-sD_v)(1-tD_w)
 =1+st(D_vD_w-D_wD_v)
\]

in \(R[s,t]/(s^2,t^2)\) shows that this is also the mixed infinitesimal group commutator. The coefficient \(st\) is a free \(R\)-summand, so its extraction is valid over every ring, including rings with nilpotents. The alternating and Jacobi identities follow from the same six-term cancellation proved in Theorem 2.2, now in the associative algebra of relative sheaf endomorphisms. Evaluation is injective on invariant fields, so the identities hold on the Lie module.

A group homomorphism sends the displayed group commutator to the commutator of its images. Extracting \(st\) proves compatibility with its differential. All the constructions commute with extension of coefficients, proving the final assertion. When \(\omega_G\) is finite projective, Proposition 1.4 makes that map an isomorphism of Lie algebras. \(\square\)

### 2.4. Tangent groups and infinitesimal homomorphisms

**Proposition 2.4. The tangent group is a semidirect product.** For every group scheme \(G/R\) and every \(R\)-algebra \(A\), put \(K_A=\operatorname{Lie}(G_A)(A)\). The split sequence

\[
1\longrightarrow K_A\longrightarrow G(A[\epsilon])
\longrightarrow G(A)\longrightarrow1
\]

identifies its middle group with \(\operatorname{Lie}(G_A)(A)\rtimes G(A)\), with multiplication

\[
(x,g)(y,h)=(x+\operatorname{Ad}(g)y,gh).
\]

Here \(\operatorname{Ad}(g)\) is the differential of conjugation by \(g\). This is an action on the entire relative Lie functor, even when the dual Lie module does not commute with base change. Differentiating \(\operatorname{Ad}\) gives the bracket of Proposition 2.3. At the identity, the derivatives of multiplication, inversion and the power map \(g\mapsto g^n\) are respectively addition, negation and multiplication by \(n\); the power map need not be a group homomorphism.

**Proof.** The projection is split by constant points, and Proposition 1.6 identifies its kernel with the additive tangent module. Every element has a unique expression \(xg\), with \(x\) in this kernel. Multiplication gives

\[
xg\,yh=x(gyg^{-1})gh,
\]

which is precisely the asserted formula. Conjugation respects the kernel's scalar multiplication because its differential is linear on derivations. Naturality in every test algebra gives the action on the relative functor. In two square-zero variables the coefficient of \(st\) in the commutator of \(x_s\) and \(y_t\) is the bracket, by Proposition 2.3. Equivalently conjugating \(y_t\) by \(x_s\) has tangent term \(y+s[x,y]\), proving the assertion about the derivative of \(\operatorname{Ad}\). Finally multiplication and inversion restricted to the additive kernel are addition and negation. Raising a kernel point to the \(n\)-th power adds it \(n\) times, for positive, zero and negative \(n\). This proves the three derivative assertions without any commutativity assumption on \(G\). \(\square\)

**Theorem 2.5. Deforming a homomorphism.** Let \(u:G\to H\) be a homomorphism of group schemes over \(R\). Its homomorphism deformations over \(R[\epsilon]/(\epsilon^2)\), with reduction \(u\), are in bijection with regular cocycles

\[
\begin{gathered}
c:G\longrightarrow\operatorname{Lie}(H/R),\\
c(gg')=c(g)+\operatorname{Ad}(u(g))c(g').
\end{gathered}
\]

Regular means a morphism of the represented tangent functors, rather than a function on one group of rational points. The identity is required on every test algebra. Conjugation by an infinitesimal point \(v\in\operatorname{Lie}(H/R)(R)\) changes \(c\) into

\[
c(g)+v-\operatorname{Ad}(u(g))v.
\]

If \(u\) is an isomorphism, every such deformation is an isomorphism. In particular the tangent spaces to the Hom and Isom functors agree **at an isomorphism**. No representability of these Hom or Isom functors is assumed.

**Proof.** Define the tangent functor of \(H\) by \(T_H(B)=H(B[\epsilon])\). It is represented by \(\operatorname{Spec}_H\operatorname{Sym}\Omega_{H/R}\), by the same local derivation calculation as Proposition 1.4. Currying a morphism \(G_{R[\epsilon]}\to H_{R[\epsilon]}\) identifies it with a morphism \(G\to T_H\): on every test scheme this is the defining adjunction for the functor of maps from the dual-number scheme. Reduction gives its projection to \(H\). Proposition 2.4 therefore writes a lift of \(u\) uniquely as \(g\mapsto(c(g),u(g))\). Its semidirect-product multiplication says exactly that this map is a homomorphism when \(c\) satisfies the displayed cocycle equation. The equation at \((e,e)\) forces \(c(e)=0\). This proves both directions, including all test algebras and gluing on nonaffine schemes.

Conjugate \((c(g),u(g))\) by \((v,1)\). The multiplication formula gives \((c(g)+v-\operatorname{Ad}(u(g))v,u(g))\), as stated.

For the last assertion we give the needed scheme argument. An endomorphism of \(X_{R[\epsilon]}\) reducing to the identity of any \(R\)-scheme \(X\) has pullback

\[
f+\epsilon a\longmapsto f+\epsilon\bigl(a+D(f)\bigr)
\]

on \(\mathcal O_X[\epsilon]\), for one relative derivation \(D\) of \(\mathcal O_X\). Its inverse replaces \(D\) by \(-D\). These local inverses agree on overlaps and define the inverse scheme morphism. Composing a deformation of an isomorphism \(u\) with its constant inverse reduces it to this case. Its inverse also respects the group law because it is the inverse of a group homomorphism. The Hom and Isom tangent functors at \(u\) consequently have the same points over every scalar extension, proving their equality there. \(\square\)

**Corollary 2.6. Nilpotent conjugacy for a diagonalizable source.** Let \(H/R\) be smooth, \(J\subset R\) nilpotent, and \(f_0,f_1:D_R(M)\to H\) two homomorphisms with equal reductions modulo \(J\). Here \(M\) is arbitrary. There is an element

\[
h\in\ker\bigl(H(R)\longrightarrow H(R/J)\bigr)
\]

such that \(f_1=\operatorname{Int}(h)\circ f_0\). The two original homomorphisms need not be equal.

**Proof.** First suppose \(J^2=0\). Since \(H\) is smooth, \(\omega_H\) is finite projective and its dual \(L\) gives its relative Lie bundle. Evaluate both maps on the universal point of \(D_R(M)\) over \(R[M]\). Their ratio \(f_1(g)f_0(g)^{-1}\) lies in the square-zero kernel of \(H(R[M])\to H((R/J)[M])\). Proposition 1.6, finite projectivity and freeness of \(R[M]\) identify this kernel with

\[
(L\otimes_RJ)\otimes_R R[M].
\]

Thus the ratio defines a regular cocycle \(c\) for the representation \(\operatorname{Ad}\circ f_0\) on \(E=L\otimes_RJ\). The cocycle identity is checked over the other free algebra \(R[M\oplus M]\), by multiplying the two homomorphisms and using the additive kernel. Only these free base extensions are used; an arbitrary scalar extension need not preserve the inclusion of \(J\) as an ideal.

For clarity, write the cocycle as \(c\in E\otimes_R R[M]\). Taking the coefficient of weight zero in the last factor of its cocycle identity gives \(v\otimes1=c+\rho(v)\), where \(v\) is the weight-zero coefficient of \(c\). This is exactly the contraction in [Diagonalizable groups](diagonalizable-groups.md), **Lemma 3.3**, and gives \(v\in E\) with \(c(g)=v-gv\). Proposition 1.6 identifies \(v\) with an element \(h\) of the displayed kernel. Conjugation of \(f_0\) by \(h\) has precisely this ratio, so equals \(f_1\). Equality on the universal point is equality of the two scheme morphisms.

For a general nilpotent ideal use induction on its nilpotence exponent. Reduce first modulo its last nonzero power \(I=J^{r-1}\), where \(J^r=0\). By induction the two reduced maps are conjugate by an element reducing to the identity modulo \(J\). Proposition 1.6 lifts that element to \(H(R)\), since \(I^2=0\) and \(H\) is smooth. After this conjugation the two maps agree modulo \(I\). The square-zero case conjugates them by an element in the kernel modulo \(I\), which also reduces to the identity modulo \(J\). Compose the conjugating elements. This completes the induction. \(\square\)

The smooth target is a substantive hypothesis. The conclusion gives conjugacy of homomorphisms, consistent with the unequal conjugate matrix actions in *Diagonalizable groups*, Section 7.3. It also proves the valid assertion about isomorphism classes of projective representations, by applying it to \(H=\mathrm{GL}(E)\) for a finite projective module \(E\).

### 2.7. Cotangent trivialization and subgroup calculations

**Proposition 2.7. All relative differentials are translated identity differentials.** For \(p:G\to\operatorname{Spec}R\), every group scheme has a canonical isomorphism

\[
\Omega_{G/R}\simeq p^*\omega_G.
\]

In particular a finite projective identity cotangent module makes the relative differential sheaf locally free. For a diagonalizable group,

\[
\begin{gathered}
\omega_{D_R(M)}\simeq R\otimes_{\mathbf Z}M,\\
\operatorname{Lie}(D_R(M))(A)
\simeq\operatorname{Hom}_{\mathbf Z}(M,A).
\end{gathered}
\]

The additive group law on \(A\) is used on the right, and its Lie bracket is zero. These formulas hold for arbitrary \(M\).

**Proof.** Over the first factor of \(G\times_RG\), the map \((g,x)\mapsto(g,gx)\) is an automorphism, with inverse \((g,y)\mapsto(g,g^{-1}y)\). It carries the section \((g,e)\) to the diagonal section \((g,g)\). Pull back the relative differential sheaf of the second factor along these sections and this automorphism. Along the first section it is \(p^*e^*\Omega_{G/R}=p^*\omega_G\); along the diagonal it is \(\Omega_{G/R}\). The automorphism induces the asserted isomorphism, using the general base-change identity for relative differentials. No flatness assumption on \(G\) is used.

For the last calculation an identity-based point of \(D_R(M)\) over \(A[\epsilon]\) assigns \(e^m\) the unit \(1+\epsilon\lambda(m)\). Multiplicativity is exactly additivity of \(\lambda:M\to A\). More generally an identity derivation from \(R[M]\) into an arbitrary \(R\)-module \(E\) is determined by the same additive rule \(M\to E\), by the Leibniz rule and the exponent basis. Thus the module representing these derivations is \(R\otimes_{\mathbf Z}M\), proving the cotangent formula by its universal property. Commutativity of \(D_R(M)\) makes conjugation trivial and hence its bracket zero. \(\square\)

**Proposition 2.8. A subgroup injects its tangent functor.** For a monomorphism \(G\to H\) of group schemes over \(R\), the induced map of represented Lie functors is a closed immersion, and \(\omega_H\to\omega_G\) is surjective. If \(\omega_G\) is finite projective, the map of dual Lie modules is a split injection.

**Proof.** A monomorphism remains injective on points over every dual-number algebra, hence on the identity kernels. The kernel of the induced linear tangent map is represented by \(\operatorname{Spec}_R\operatorname{Sym}Q\), with \(Q=\operatorname{coker}(\omega_H\to\omega_G)\): it parameterizes linear forms on \(\omega_G\) annihilating the image of \(\omega_H\). Injectivity says that this functor consists just of its zero section. Yoneda then makes its symmetric algebra \(R\); its degree-one summand is \(Q\), so \(Q=0\). The surjection of cotangent modules induces a surjection of symmetric algebras and hence the closed immersion of their spectra. If \(\omega_G\) is finite projective, the cotangent surjection splits over \(R\). Dualizing that splitting proves the last assertion. \(\square\)

**Theorem 2.9. Lie functors of centralizers and normalizers.** Let \(H\hookrightarrow G\) be a closed subgroup over \(R\), and let \(C,N\) denote its centralizer and normalizer functors. Their Lie functors mean the identity kernels on dual-number algebras; no representability assumption on \(C,N\) is needed for the formulas below. If \(G\) is separated and \(H\) is essentially free as defined in [Diagonalizable groups](diagonalizable-groups.md), Section 4.10, these functors are closed subgroup schemes by that lesson's Corollary 4.11. For every \(R\)-algebra \(A\),

\[
\begin{gathered}
\operatorname{Lie}(C)(A)=\operatorname{Lie}(G)(A)^{H_A},\\
\operatorname{Lie}(N)(A)=
\{v\in\operatorname{Lie}(G)(A):\\
\qquad\operatorname{Ad}(h)v_B-v_B\in\operatorname{Lie}(H)(B)\\
\qquad\text{for all }A\to B,\ h\in H(B)\}.
\end{gathered}
\]

Equivalently, using the pointwise quotient of tangent functors,

\[
\begin{gathered}
\operatorname{Lie}(N)/\operatorname{Lie}(H)\\
=\bigl(\operatorname{Lie}(G)/\operatorname{Lie}(H)\bigr)^H.
\end{gathered}
\]

In particular a normal subgroup has a Lie ideal. All these assertions concern the full group action, and cannot generally be replaced by invariance under \(\operatorname{Lie}(H)\) alone.

**Proof.** Write a tangent point of \(G\) as \(v_\epsilon\in G(A[\epsilon])\). Over \(B[\epsilon]\), every point of \(H\) has a unique form \(w_\epsilon h\), with \(w\in\operatorname{Lie}(H)(B)\) and \(h\in H(B)\), by Proposition 2.4. The two infinitesimal factors \(v_\epsilon,w_\epsilon\) commute because the square-zero kernel is additive. Thus the commutator of \(v_\epsilon\) with \(w_\epsilon h\) has tangent coefficient

\[
v_B-\operatorname{Ad}(h)v_B.
\]

It is the identity precisely when that coefficient is zero, and it belongs to \(H(B[\epsilon])\) precisely when the coefficient lies in \(\operatorname{Lie}(H)(B)\). This proves the necessary centralizer and normalizer conditions. For normalizing a subgroup both the element and its inverse must carry it into itself; their tangent coefficients are opposites, so the same condition proves both inclusions.

These tests over \(B[\epsilon]\) are also sufficient for all test algebras over \(A[\epsilon]\). Indeed for such an algebra \(D\), with image \(a\in D\) of \(\epsilon\), apply the preceding test with the underlying \(A\)-algebra \(B=D\), then evaluate its new formal variable at \(a\), where \(a^2=0\). Every chosen \(H(D)\)-point lifts as a constant point before that evaluation. This gives the universal centralizer or normalizer condition over \(D\). The two formulas follow.

For the quotient assertion a class \(v\bmod\operatorname{Lie}(H)(A)\) is invariant under \(H\) exactly when its difference under every \(h\) lies in the indicated subgroup. This is precisely the second formula. If \(H\) is normal, its adjoint action through \(G\) preserves \(\operatorname{Lie}(H)\). Differentiate this invariance in a second square-zero variable to obtain \([\operatorname{Lie}(G),\operatorname{Lie}(H)]\subset\operatorname{Lie}(H)\), proving the Lie-ideal assertion. \(\square\)

**Example 2.10. The group acts more faithfully than its Lie algebra.** Over a field of characteristic different from two, take \(G=\mathrm{GL}_2\) and \(H=\{1,\operatorname{diag}(-1,1)\}\). This finite étale subgroup has zero Lie algebra. Its centralizer is the diagonal torus: commuting with \(\operatorname{diag}(-1,1)\) forces both off-diagonal entries to vanish, since \(2\) is invertible in every test algebra. Thus \(\operatorname{Lie}(C_G(H))\) consists only of diagonal matrices, whereas the centralizer of \(\operatorname{Lie}(H)=0\) in \(\mathfrak{gl}_2\) is all of \(\mathfrak{gl}_2\). The comparison inclusion can be strict even for smooth groups and étale subgroups.

**Proposition 2.11. Differentiating a linear representation and its stabilizers.** Let \(V\) be a finite projective \(R\)-module. Then

\[
\operatorname{Lie}(\mathrm{GL}(V))(A)
=\operatorname{End}_A(V_A),\qquad [X,Y]=XY-YX.
\]

A representation \(\rho:G\to\mathrm{GL}(V)\) differentiates to a bracket-preserving map into these endomorphisms. If \(E\subset V\) is a finite projective direct summand, its stabilizer \(N_G(E)\) and its pointwise fixer \(C_G(E)\) are closed subgroup schemes of \(G\), and

\[
\begin{gathered}
\operatorname{Lie}(N_G(E))(A)
=\{x:d\rho(x)E_A\subset E_A\},\\
\operatorname{Lie}(C_G(E))(A)
=\{x:d\rho(x)E_A=0\}.
\end{gathered}
\]

Both right sides are Lie subalgebras. For the adjoint representation these are respectively the normalizer and centralizer of the specified Lie submodule, when that Lie bundle is finite projective and the submodule is a direct summand.

There is a useful functor version. Let \(\mathcal E\) be a subfunctor of the points of \(V\), whose values are modules and whose restriction maps are linear over the scalar maps, and suppose that for every \(R\)-algebra \(A\) its square-zero extension has \(\mathcal E(A[\epsilon])=\mathcal E(A)\oplus\epsilon\mathcal E(A)\) inside \(V_A[\epsilon]\). Then the normalizer tangent functor is given by \(d\rho(x_B)\mathcal E(B)\subset\mathcal E(B)\) for **every** \(A\to B\). The pointwise-fixer tangent functor is given by \(d\rho(x_B)\mathcal E(B)=0\) for every such \(B\), even without this square-zero hypothesis. These are assertions about functors; closed representability was proved above for the direct-summand case.

**Proof.** An automorphism of \(V_A\otimes_A A[\epsilon]\) reducing to the identity is uniquely \(1+\epsilon X\); its inverse is \(1-\epsilon X\). Matrix multiplication in two square-zero variables gives commutator coefficient \(XY-YX\). Local bases prove the formula for every finite projective \(V\); the formulas agree on overlaps. Differentiating \(\rho\) takes the coefficient of \(\epsilon\), and preserves brackets by Proposition 2.3.

Locally split \(V=E\oplus F\). A matrix preserving \(E\) has lower-left block zero. Its invertibility makes both diagonal blocks invertible: the determinant is their product, a unit, so each factor is a unit in the commutative test algebra. Its inverse consequently also preserves \(E\). The vanishing block equations define the stabilizer as a closed subscheme of \(\mathrm{GL}(V)\). The pointwise fixer further has upper-left block equal to the identity. These conditions glue intrinsically as the equations that the map \(E\to V/E\) vanish, or that \(E\to V\) equal its inclusion. Pull back those closed subschemes along \(\rho\) to obtain the two closed subgroups of \(G\).

Substitute \(1+\epsilon d\rho(x)\) into these equations. Their degree-one coefficients are exactly the two displayed conditions, with no extra restriction from invertibility. Operators preserving \(E\), or annihilating it, retain that property under their commutator, proving the Lie-subalgebra assertions. The adjoint case follows from \(d\operatorname{Ad}(x)y=[x,y]\) in Proposition 2.4. For the functor version, the normalizer sends \(e_0+\epsilon e_1\) to \(e_0+\epsilon(e_1+d\rho(x_B)e_0)\), proving the stated condition from the direct-sum hypothesis; the inverse has the opposite coefficient. For a pointwise fixer, the coefficient depends only on the reduction \(e_0\), so no hypothesis on its other coefficient is needed. To test every algebra over \(A[\epsilon]\), first test its underlying \(A\)-algebra with a new formal variable, then evaluate that variable at the image of \(\epsilon\), exactly as in Theorem 2.9. This proves sufficiency on all test algebras. \(\square\)

## 3. One local ring controls smoothness

Recall two different dimensions. The Krull dimension of a local ring counts chains of primes. Its embedding dimension is \(\dim_{\kappa(x)}\mathfrak m_x/\mathfrak m_x^2\), the tangent dimension when \(x\) is rational. A Noetherian local ring has Krull dimension at most embedding dimension; equality defines regularity. Group translation lets us compare these numbers at the identity and use the result everywhere.

<a id="gs02-point-dimension-after-field-extension"></a>

**Lemma 3.0a. Point dimension after field extension.** Let \(X\) be a scheme locally of finite type over a field \(k\). Let \(K/k\) be any field extension, let \(y\in X_K=X\times_k\operatorname{Spec}K\), and let \(x\in X\) be its image. With point dimension defined by

\[
\dim_xX=\inf_{x\in U,\ U\text{ open}}\dim U,
\]

one has

\[
\dim_yX_K=\dim_xX.
\]

No algebraicity, separability or perfectness hypothesis is imposed on the field extension.

**Proof.** Choose an affine finite-type neighborhood \(U=\operatorname{Spec}A\) of \(x\), and restrict to \(U_K=\operatorname{Spec}A_K\), where \(A_K=K\otimes_kA\). Computing point dimension in an open neighborhood does not change it: intersecting a neighborhood with that open gives a smaller neighborhood, whereas neighborhoods contained in the open are also neighborhoods in the whole scheme. We may therefore work with \(A\) and \(A_K\).

First take \(A\) to be a domain. [*Krull dimension and Noether normalization*, Corollary 3.2 and Theorem 4.2](../../AG-CA/src/krull-dimension-and-noether-normalization.md#3-normalization-that-respects-ideals) supply a finite inclusion

\[
P=k[t_1,\ldots,t_d]\hookrightarrow A,
\qquad d=\dim A.
\]

Put \(F=\operatorname{Frac}P\). Since the domain \(A\) is torsion-free as a \(P\)-module, \(A\to A\otimes_PF\) is injective. The latter is a finite-dimensional \(F\)-vector space, say of dimension \(r\). Choose an \(F\)-linear isomorphism \(A\otimes_PF\simeq F^r\), used only as a module comparison. Tensoring this injection over \(k\) gives a \(P_K=K[t_1,\ldots,t_d]\)-linear injection

\[
A_K\hookrightarrow (K\otimes_kF)^r.
\]

The ring \(K\otimes_kF\) is the localization of the domain \(P_K\) by the images of the nonzero elements of \(P\). Thus multiplication by every nonzero element of \(P_K\) is injective on the displayed target and on \(A_K\). Also \(A_K\) is finite over \(P_K\), by tensoring a finite generating list for \(A\) over \(P\).

Let \(\mathfrak q\) be a minimal prime of the Noetherian ring \(A_K\). Minimal primes are associated, and elements of associated primes are zero divisors: these are [*Associated primes and primary decomposition*, Theorems 3.2 and 1.2](../../AG-CA/src/associated-primes-and-primary-decomposition.md#3-localizing-the-associated-points). Consequently \(\mathfrak q\cap P_K=(0)\); otherwise a nonzero element of that contraction would both kill a nonzero element of \(A_K\) and act injectively. The induced ring map

\[
P_K\hookrightarrow A_K/\mathfrak q
\]

is an integral inclusion. [*Integral extensions, lying over, going up and going down*, Theorem 5.1](../../AG-CA/src/integral-extensions-lying-over-going-up-and-going-down.md#5-chains-and-dimension) therefore gives \(\dim(A_K/\mathfrak q)=d\). In particular every component of the scalar extension of a finite-type domain has the original domain's dimension.

Now allow arbitrary \(A\), including nilpotents and components of different dimensions. We use [*Tor and flat modules*, Theorem 6.3](../../AG-CA/src/tor-and-flat-modules.md#6-exact-sequences-and-prime-lifting): flat maps satisfy going down. Its actual argument is that \(A_{\mathfrak p}\to B_{\mathfrak q}\) is a flat local map, hence faithfully flat; its tensor product with the residue field at any smaller source prime is nonzero, and a prime of that fibre contracts to the required smaller prime. The fibre-prime correspondence is [*Localization, local properties and support*, Theorem 3.2](../../AG-CA/src/localization-local-properties-and-support.md#3-points-left-after-division-and-fibres).

The map \(A\to A_K\) is faithfully flat. Going down shows that every minimal prime \(\mathfrak q\) of \(A_K\) contracts to a minimal prime \(\mathfrak p\) of \(A\): a smaller prime downstairs would lift below \(\mathfrak q\), contradicting its minimality. Moreover \(\mathfrak q/\mathfrak pA_K\) is a minimal prime of

\[
A_K/\mathfrak pA_K\simeq K\otimes_k(A/\mathfrak p).
\]

The domain case therefore shows

\[
\dim(A_K/\mathfrak q)=\dim(A/\mathfrak p).
\tag{D1}
\]

Let \(\mathfrak q_y\) and \(\mathfrak p_x\) denote the primes of \(y\) and \(x\). For every minimal prime \(\mathfrak p\subseteq\mathfrak p_x\), going down lifts \(\mathfrak p\) to a prime \(\mathfrak r\subseteq\mathfrak q_y\). Choose a minimal prime \(\mathfrak q\subseteq\mathfrak r\). Its contraction is a minimal prime contained in \(\mathfrak p\), and must equal \(\mathfrak p\). Thus every downstairs component through \(x\) is matched by an upstairs component through \(y\); the converse follows by contraction. Equation (D1) preserves the dimensions of all the matched components. [*Krull dimension and Noether normalization*, Theorem 6.1](../../AG-CA/src/krull-dimension-and-noether-normalization.md#6-dimension-at-a-point) proves that point dimension is the maximum of the dimensions of the components through the point. Taking the two maxima proves the equality. \(\square\)

This statement concerns point dimension. It does not assert equality of the two local-ring dimensions at arbitrary points: residue transcendence degrees may change.

<a id="gs02-smoothness-descends-under-field-extension"></a>

**Lemma 3.0b. Smoothness descends under field extension.** Let \(X/k\) be locally of finite type and let \(K/k\) be any field extension. For any \(y\in X_K\) above \(x\in X\), \(X\) is smooth over \(k\) at \(x\) if and only if \(X_K\) is smooth over \(K\) at \(y\). In particular, \(X_K/K\) smooth implies \(X/k\) smooth.

**Proof by the dimension criterion.** On a finite-type affine neighborhood, put

\[
a_x=\dim_{\kappa(x)}(\Omega_{X/k}\otimes\kappa(x)),
\qquad
a_y=\dim_{\kappa(y)}(\Omega_{X_K/K}\otimes\kappa(y)).
\]

The natural differential base-change map is an isomorphism

\[
(\Omega_{X/k}\otimes\kappa(x))
\otimes_{\kappa(x)}\kappa(y)
\xrightarrow{\sim}
\Omega_{X_K/K}\otimes\kappa(y).
\tag{D2}
\]

It sends \(da\otimes c\) to \(c\,d(1\otimes a)\). A polynomial presentation verifies both its source, target and inverse: the generators \(dX_i\) and the defining differential relations extend by tensoring with \(K\), then with \(\kappa(y)\). This is also [*Kähler differentials*, Theorems 3.3 and 5.1](../../AG-CA/src/kahler-differentials.md). Hence \(a_y=a_x\). Lemma 3.0a gives \(\dim_yX_K=\dim_xX\). The fully proved [*Smooth algebras over a field and the Jacobian criterion*, Theorem 2.1](../../AG-CA/src/smooth-algebras-over-a-field-and-the-jacobian-criterion.md#2-the-criterion-and-its-open-locus) identifies smoothness with equality of these differential and point dimensions. Applying it on the two sides proves the claimed equivalence at the specified pair of points. Every \(x\) has a lift \(y\), since \(\kappa(x)\otimes_kK\) is a nonzero ring and therefore has a prime. This proves the global descent assertion. \(\square\)

**Alternative infinitesimal proof of global descent.** Take an affine chart \(X=\operatorname{Spec}S\), with \(S=P/I\) and \(P=k[X_1,\ldots,X_n]\). Hilbert's basis theorem makes the ideal \(I\) finitely generated. The conormal sequence is

\[
I/I^2\xrightarrow{\delta}S^n\longrightarrow\Omega_{S/k}\longrightarrow0,
\qquad \delta(\bar f)=df.
\tag{D3}
\]

The quotient modules and this map commute with flat scalar extension to \(K\). Smoothness upstairs makes (D3) locally split exact upstairs, by [*Formally smooth, unramified and étale ring maps*, Theorem 3.1](../../AG-CA/src/formally-smooth-unramified-and-etale-ring-maps.md#3-existence-is-measured-by-the-conormal-sequence). Thus its first map is injective, and the finite differential module is locally free. It is finite projective on this affine chart: local freeness gives flatness by the local flatness test, and finite presentation plus flatness gives finite projectivity by [*Tor and flat modules*, Theorem 5.3](../../AG-CA/src/tor-and-flat-modules.md). Faithful scalar extension detects the kernel of \(\delta\), and [*Faithful flatness and the local criterion for flatness*, Corollary 3.2](../../AG-CA/src/faithful-flatness-and-the-local-criterion-for-flatness.md#3-descending-finiteness-and-flatness) descends finite projectivity of \(\Omega_{S/k}\). Therefore (D3) downstairs is injective at its left and splits, since its last module is projective. Choose an \(S\)-linear left inverse \(\rho:S^n\to I/I^2\) to \(\delta\).

To see the actual lifting, let \(C\) be any \(k\)-algebra, let \(J\subset C\) have \(J^2=0\), and let \(\bar u:S\to C/J\) be a \(k\)-algebra map. Give \(J\) its \(S\)-module structure through \(\bar u\), and choose arbitrary lifts in \(C\) of the images of the \(X_i\). They define a \(k\)-algebra map \(q:P\to C\). It sends \(I\) into \(J\) and \(I^2\) to zero, so it induces an \(S\)-linear map \(\lambda:I/I^2\to J\). Compose

\[
D:P\xrightarrow{d}\Omega_{P/k}\otimes_PS\simeq S^n
\xrightarrow{\rho}I/I^2\xrightarrow{\lambda}J.
\]

This is a \(k\)-derivation with respect to the \(P\)-action on \(J\) through \(\bar u\); for \(i\in I\) it satisfies \(D(i)=q(i)\). Because \(J^2=0\), the map \(q-D:P\to C\) is a \(k\)-algebra map: expanding its product and using the derivation identity gives multiplicativity. It kills \(I\), hence factors through a lift \(u:S\to C\) of \(\bar u\). This proves formal smoothness, and the finite presentation of \(S/k\) gives smoothness. Apply this on each affine chart. No averaging or perfectness hypothesis is involved. \(\square\)

**Lemma 3.1. Homogeneous dimension.** A locally algebraic group scheme \(G/k\) is equidimensional. Its local dimension \(\dim_xG\), defined as the infimum of the dimensions of open neighbourhoods of \(x\), is constant and equals \(\dim G\). At every closed point \(x\),

\[
\dim\mathcal O_{G,x}=\dim G.
\]

**Proof.** For any two points \(x,y\), choose a common extension field of their residue fields and choose lifts of the points that are rational over that field. Point dimension is unchanged by this scalar extension, by [Lemma3.0a](#gs02-point-dimension-after-field-extension). Translation by \(yx^{-1}\) now carries the first lift to the second, so their local dimensions are equal. Thus \(\dim_xG\) is constant, with finite value \(d=\dim_eG\).

The dimension formula for a point of a locally finite-type \(k\)-scheme is

\[
\dim_xG=\dim\mathcal O_{G,x}
+\operatorname{trdeg}_k\kappa(x).
\tag{6}
\]

It gives \(\dim\mathcal O_{G,x}\leq d\) everywhere, and equality at closed points, whose residue fields are finite over \(k\). The dimension of a scheme is the supremum of its local-ring dimensions, so \(\dim G=d\).

At the generic point of an irreducible component, take an affine neighbourhood. Only finitely many components meet that neighbourhood, and deleting the other components leaves an open part of the chosen component. Its dimension is the transcendence degree of its function field, and equals the local dimension at that generic point. This is \(d\), so every component has dimension \(d\). Nothing here requires finitely many components globally. \(\square\)

*References for the point-dimension inputs:* [Stacks, Tags 02FX–02FY]. The group-scheme conclusion is [Stacks, Tag 045X].

**Theorem 3.2. Smoothness criterion.** For every locally algebraic group scheme over a field,

\[
\dim G\leq\dim_k\operatorname{Lie}(G),
\]

and equality holds if and only if \(G/k\) is smooth.

**Proof.** At the rational identity, the two numbers are respectively the dimension and embedding dimension of the Noetherian local ring \(\mathcal O_{G,e}\), by Lemma 3.1 and Proposition 1.1. The local-ring inequality proves the asserted inequality.

For the equality criterion, extend scalars to an algebraic closure \(\overline k\). [Lemma3.0a](#gs02-point-dimension-after-field-extension) preserves point dimension, and (1) shows that Lie dimension is unchanged. At the identity of \(G_{\overline k}\), equality therefore says that the local ring is regular. Over an algebraically closed field, a point of a scheme locally of finite type is smooth precisely when its local ring is regular. Thus the identity is smooth.

Every closed point of \(G_{\overline k}\) is rational, and translation carries the identity to it. Every such point is therefore smooth. The smooth locus is open. If its complement were nonempty, intersecting it with a finite-type affine neighbourhood would give a nonempty closed subset containing a closed point, by the Nullstellensatz. This contradicts the preceding conclusion. Thus all of \(G_{\overline k}\) is smooth. [Lemma3.0b](#gs02-smoothness-descends-under-field-extension) descends smoothness under this field extension, so \(G\) is smooth.

Conversely, if \(G\) is smooth, its local ring at the identity is regular. Its dimension equals its embedding dimension, which gives equality. \(\square\)

This proof explains the need for a geometric field extension. Regularity at a rational point alone over an imperfect field is not the general smoothness criterion for arbitrary varieties. It also explains why no affineness condition belongs in the theorem.

## 4. Why characteristic zero forces smoothness

The preceding lesson proved that \(\Omega_{G/k}\) is free for every group scheme over a field. In characteristic \(p\), a relation such as \(x^p=0\) disappears on differentiation. In characteristic zero, derivations prevent that disappearance. The following local argument makes the mechanism explicit.

**Lemma 4.1. A derivation detects a regular parameter.** Let \(R\) be a Noetherian local algebra over a characteristic-zero field. Suppose \(f\) is in its maximal ideal and a derivation \(\delta:R\to R\) satisfies \(\delta(f)=1\). Then \(f\) is a nonzerodivisor.

**Proof.** Suppose \(fa=0\). Since \(\delta^2(f)=0\), repeated differentiation gives

\[
0=\delta^n(fa)=f\delta^n(a)+n\delta^{n-1}(a)
\qquad(n\geq1).
\]

Starting with \(a=-f\delta(a)\), induction yields

\[
a=\frac{(-1)^n f^n\delta^n(a)}{n!}.
\]

All the factorials are invertible. Thus \(a\in f^nR\) for every \(n\). Krull's intersection theorem for the proper ideal \((f)\) in a Noetherian local ring gives \(\bigcap_n f^nR=0\), so \(a=0\). \(\square\)

**Lemma 4.2.** Let \(k\) be algebraically closed of characteristic zero. If \(R\) is a localization at a closed point of a finite-type \(k\)-algebra and \(\Omega_{R/k}\) is free, then \(R\) is regular.

**Proof.** Its residue field is \(k\). The natural map

\[
\mathfrak m/\mathfrak m^2
\longrightarrow\Omega_{R/k}\otimes_Rk
\]

is an isomorphism: the derivations on either side are the tangent vectors described in Proposition 1.1. Write their dimension as \(r\); it is also the rank of the free module \(\Omega_{R/k}\).

Induct on \(r\). If \(r=0\), Nakayama's lemma gives \(\mathfrak m=0\), and \(R\) is a field. For \(r>0\), choose \(f\in\mathfrak m\) with nonzero class in \(\mathfrak m/\mathfrak m^2\). Its differential has a nonzero residue in the free module, so \(df\) extends to a basis of that module: one coefficient of \(df\) is a unit, and elementary changes of basis make it the first basis vector. The linear functional taking \(df\) to \(1\) defines a derivation \(\delta\) with \(\delta(f)=1\). Lemma 4.1 makes \(f\) a nonzerodivisor.

The conormal sequence for the quotient is

\[
(f)/(f^2)\longrightarrow
\Omega_{R/k}\otimes_RR/(f)
\longrightarrow\Omega_{(R/(f))/k}\longrightarrow0.
\]

The first arrow sends the class of \(f\) to \(df\). Its image is the free direct summand generated by that basis vector. Therefore \(\Omega_{(R/(f))/k}\) is free of rank \(r-1\). The quotient is again a local ring of the required kind, so induction makes it regular. [Regular local rings, Proposition1.3](../../AG-CA/src/regular-local-rings.md#1-coordinates-graded-rings-and-regular-quotients) lifts regularity across this nonzerodivisor. Its one-equation dimension input is [Dimension theory of Noetherian local rings, Theorem3.2](../../AG-CA/src/dimension-theory-of-noetherian-local-rings.md#3-how-much-can-one-equation-cut). This proves the lemma. \(\square\)

**Theorem 4.3. Cartier's theorem.** Every group scheme locally of finite type over a field of characteristic zero is smooth.

**Proof.** Extend the field to an algebraic closure. The group-scheme differential isomorphism makes \(\Omega_{G/k}\) finite free, of rank \(\dim\omega\). At every closed point, its localization is the free differential module of the local ring. Lemma 4.2 makes that ring regular. Over the algebraically closed field, regularity at those points gives smoothness there. The open smooth locus contains every closed point and hence the whole scheme, by the same affine-neighbourhood argument as in Theorem 3.2. Finally descend smoothness to the original field by [Lemma3.0b](#gs02-smoothness-descends-under-field-extension). \(\square\)

In particular these group schemes are geometrically reduced, and a finite group scheme in characteristic zero is étale: its smooth morphism has relative dimension zero.

*References:* [Stacks, Tags 047I, 047N and 04QN]. Lemmas 4.1–4.2 supply the differential criterion used here rather than leaving it as a black box.

**Theorem 4.4. Reducedness in full generality.** Every group scheme over a characteristic-zero field is geometrically reduced, with no affine, quasi-compact, Noetherian or finite-type hypothesis.

**Proof.** The full argument is given in Appendix A.1–A.5, ending with Theorem A.11. It constructs a normal affine subgroup with finitely many equations, proves the integral generic quotient and its regular realization, and passes through a finitely generated nilpotent thickening before applying the finite-type theorem. Only the final identity-component reduction removes quasi-compactness. \(\square\)

This is the extension attributed to Perrin in [Stacks, Remark 047O]. Reducedness here does not remove the local finite-presentation requirement in the smoothness theorem.

## 5. Perfect fields and a failure over an imperfect field

**Theorem 5.1.** A reduced group scheme locally of finite type over a perfect field is smooth.

**Proof.** Characteristic zero is covered by Theorem 4.3. In any characteristic, let \(d=\dim G\), and write

\[
\Omega_{G/k}\simeq\mathcal O_G^{\oplus r}.
\]

Here \(r=\dim_k\mathfrak g\), by duality at the identity. Choose a generic point \(\eta\) of any irreducible component. A reduced locally Noetherian scheme has local ring \(\kappa(\eta)\) at such a point. Localizing differentials therefore gives

\[
\Omega_{G/k,\eta}
=\Omega_{\kappa(\eta)/k}.
\]

The field \(\kappa(\eta)\) is finitely generated over \(k\). Since \(k\) is perfect, it has a separating transcendence basis \(z_1,\ldots,z_d\): it is finite separable over \(k(z_1,\ldots,z_d)\). The differentials \(dz_i\) form a basis of \(\Omega_{\kappa(\eta)/k}\). To see this, a derivation on the rational function field extends uniquely across a separable algebraic element, by differentiating its minimal polynomial and dividing by its nonzero derivative. Thus the differential dimension is its transcendence degree, which is \(d\) by Lemma 3.1.

The free sheaf has rank \(r\) at \(\eta\), so \(r=d\). Theorem 3.2 now gives smoothness. \(\square\)

*References:* [Stacks, Tags 047P and 04QP].

Perfectness is essential. The next calculation identifies exactly the tangent direction that survives a purely inseparable relation.

**Example 5.2. A reduced group that becomes a thick line.** Let \(k=\mathbf F_p(a)\), where \(a\) is an indeterminate, and let

\[
H=\operatorname{Spec}k[x,y]/(x^p+ay^p).
\]

It is a closed subgroup of \(\mathbf G_a^2\). Indeed its equation is primitive under the additive coproduct:

\[
\Delta(x^p+ay^p)
=(x^p+ay^p)\otimes1+1\otimes(x^p+ay^p).
\]

Its value at the identity is zero and negation preserves its vanishing, so the Hopf maps descend.

To prove irreducibility, view the equation as a monic polynomial in \(x\) over \(k(y)=\mathbf F_p(y)(a)\). The element \(-ay^p\) is not a \(p\)-th power there: its valuation at the prime \(a\) is \(1\), whereas a \(p\)-th power has valuation divisible by \(p\). In characteristic \(p\), \(X^p-b\) for a non-\(p\)-th-power \(b\) is irreducible; adjoining its root is a purely inseparable extension of degree \(p\). Gauss's lemma then makes \(x^p+ay^p\) irreducible in \(k[x,y]\). The quotient is a domain, so \(H\) is reduced and irreducible.

The inclusion \(k[y]\hookrightarrow k[H]\) is integral and finite, with basis \(1,x,\ldots,x^{p-1}\). It gives \(\dim H=1\). At the identity, both partial derivatives of the equation are zero. Hence there is no linear tangent relation:

\[
\operatorname{Lie}(H)=k^2.
\]

Theorem 3.2 shows that \(H\) is not smooth. After adjoining \(b\) with \(b^p=a\), its equation is

\[
(x+by)^p=0.
\]

With \(u=x+by\), the coordinate ring becomes \(k(b)[u,y]/(u^p)\), a nonreduced thickening of a line. Reducedness over the original field therefore did not give geometric reducedness. Its bracket is zero because it is a commutative subgroup of the additive group. This is the example in [Stacks, Remark 047Q], with all claims checked directly.

## 6. Frobenius and the extra characteristic-\(p\) operation

Suppose \(\operatorname{char}(k)=p\). The relative Frobenius of a \(k\)-scheme \(X\) is a \(k\)-morphism \(F_{X/k}:X\to X^{(p)}\), where \(X^{(p)}\) is its base change along the Frobenius of \(k\). On rings the formula is

\[
B\otimes_{k,F_k}k\longrightarrow B,\qquad b\otimes c\longmapsto cb^p.
\]

The twist is needed to make this a \(k\)-algebra map. For a group scheme the construction respects multiplication, and its differential is zero: differentiating \(b^p\) gives zero.

The kernel \(G[F]\) is called the first Frobenius kernel. For a finite-type affine group with augmentation ideal \(I\), its algebra is

\[
k[G[F]]=k[G]/(b^p:b\in I).
\tag{7}
\]

Choose finitely many augmented algebra generators. In this quotient their \(p\)-th powers vanish, so their monomials with each exponent below \(p\) span a finite-dimensional algebra. Its augmentation ideal is nilpotent, so its spectrum has only the identity as a point. Thus this is a finite infinitesimal group whose relative Frobenius is the identity-valued morphism. A group with that property is said to have **height at most one**.

For \(\mathbf G_a\), (7) gives \(\alpha_p\). For \(\mathbf G_m\), it gives \(\mu_p\), since \(t^p-1=(t-1)^p\). For \(\mathrm{GL}_r\), its equations are

\[
x_{ij}^p=\delta_{ij}.
\]

The determinant is automatically invertible since its \(p\)-th power is \(1\).

There is also a natural \(p\)-operation on the Lie algebra. If \(D\) is a derivation, iterating Leibniz gives

\[
D^p(fg)=\sum_{i=0}^p\binom piD^i(f)D^{p-i}(g)
=D^p(f)g+fD^p(g).
\]

Thus \(D^p\) is again a derivation. If \(D\) is left-invariant, so is \(D^p\). Lemma 2.1 defines \(v^{[p]}\) by

\[
L_{v^{[p]}}=L_v^p.
\]

For \(\mathbf G_a\) and \(\alpha_p\), the basic field is \(d/dx\), whose \(p\)-th iterate is zero: on a monomial the coefficient is a product of \(p\) successive integers. For \(\mathbf G_m\) and \(\mu_p\), it is \(t\,d/dt\), whose \(p\)-th iterate equals itself, since \(m^p=m\) for every integer \(m\) viewed in \(k\). Consequently, if \(v\) is the standard basis vector,

\[
\begin{array}{c|cc}
&[v,v]&v^{[p]}\\ \hline
\alpha_p&0&0\\
\mu_p&0&v.
\end{array}
\]

This additional operation distinguishes their one-dimensional Lie algebras with \(p\)-structure, although their ordinary brackets agree. The classification of finite height-one groups by restricted Lie algebras goes further; this lesson only needs the operation and these calculations.

## 7. Exercises

1. **Easy — determinants in every characteristic.** Compute the differential of \(\det:\mathrm{GL}_r\to\mathbf G_m\), the Lie algebra of its kernel, and the Lie algebra of \(\mu_{10}\) in characteristics \(0,2,5\). Explain why the answer for \(\mathrm{SL}_r\) still has dimension \(r^2-1\) when the characteristic divides \(r\).
2. **Medium — an adjoint calculation.** Compute all brackets in the basis \(E_{12},E_{21},\operatorname{diag}(1,-1)\) for \(\operatorname{Lie}(\mathrm{SL}_2)\) by differentiating conjugation. Determine its centre in characteristic two.
3. **Medium — dimensions of thick points.** Prove that \(\mu_p\) and \(\alpha_p\) are not smooth over a field of characteristic \(p\). Compute the Lie map induced by the inclusion \(\mu_p\subset\mathbf G_m\), and explain why its being an isomorphism of Lie spaces does not make the inclusion an isomorphism.
4. **Medium — Cartier in an affine neighbourhood.** Let \(B\) be a finite-type commutative Hopf algebra over a characteristic-zero field. Give a proof that \(\operatorname{Spec}B\) is smooth which does not begin by assuming \(B\) is reduced. Identify the exact step that fails in characteristic \(p\).
5. **Hard — one inseparable coefficient.** Over \(k=\mathbf F_p(a)\), prove that the additive hypersurface \(x^p+ay^p=0\) is an integral group of dimension one and has Lie dimension two. Describe its base change to \(k(a^{1/p})\).
6. **Medium — a failure of right exactness.** Compute the Lie sequence of \(0\to\alpha_p\to\mathbf G_a\xrightarrow{F}\mathbf G_a\to0\), where the last map is surjective as an fppf sheaf. Prove the asserted sheaf surjectivity and show where exactness of the Lie sequence stops.
7. **Hard — ordinary Lie algebras miss a distinction.** Use the invariant fields on \(\alpha_p\) and \(\mu_p\) to prove that these group schemes are not isomorphic, even though their ordinary Lie algebras are isomorphic. Explain why invariance and the \(p\)-th iterate suffice, without a classification theorem.

8. **Medium — dualization over a ring.** Compute the Lie modules of \(\mathrm{GL}_{r,R}\), \(\mathrm{SL}_{r,R}\) and \(\mu_{n,R}\) over an arbitrary ring. Use \(\mu_{p,\mathbf Z}\) to show that flatness of a group scheme alone does not ensure the module base-change formula.
9. **Medium — lifting an infinitesimal matrix.** Let \(J^2=0\) in \(C\). Identify the kernel of \(\mathrm{GL}_r(C)\to\mathrm{GL}_r(C/J)\), prove that its multiplication is addition of matrices, and prove that the reduction map is surjective.

**Exercise 10.** Compute the infinitesimal automorphisms of \(\mathbf P^1_k\) reducing to the identity, in any characteristic. Give their vector fields on an affine coordinate chart and compute their bracket.

**Exercise 11.** Show that every infinitesimal deformation of a group homomorphism \(\mathbf G_m\to\mathbf G_m\) is unchanged, while every infinitesimal deformation of \(\mathbf G_m\to\mathrm{GL}_r\) is conjugate to its constant extension. Explain the difference between equality and conjugacy.

**Exercise 12.** Over \(\mathbf Q\), exhibit matrices for which \((gh)^2\ne g^2h^2\). Nevertheless compute the derivative of the squaring map at the identity of \(\mathrm{GL}_2\), and explain why no contradiction occurs.

## 8. Solutions

**1.** The first-order determinant formula gives \(X\mapsto\operatorname{tr}(X)\). Its kernel is the trace-zero space, by left exactness. The trace functional is nonzero and surjective because \(E_{11}\) has trace one; hence its kernel has dimension \(r^2-1\) in every characteristic. If the characteristic divides \(r\), scalar matrices are simply additional visible members of this same kernel, not an additional dimension. For \(\mu_{10}\), the condition on the direction \(c\) is \(10c=0\). It gives zero Lie space in characteristic zero, and all of \(k\) in characteristics two and five. Each conclusion uses the integer as an element of the actual base field.

**2.** Conjugation by \(1+sX\) sends \(Y\) to \(Y+s(XY-YX)\), so its differential is the matrix commutator. With \(u=E_{12},v=E_{21},h=\operatorname{diag}(1,-1)\), multiplication gives \(uv=E_{11}\), \(vu=E_{22}\), \(hu=u\), \(uh=-u\), \(hv=-v\), \(vh=v\). Thus \([u,v]=h\), \([h,u]=2u\), \([h,v]=-2v\); reversing entries negates the result, and the self-brackets vanish. In characteristic two, \(h\) is central. If \(z=\lambda u+\mu v+\nu h\), then \([z,u]=\mu h\) and \([z,v]=\lambda h\), since minus equals plus. Centrality forces \(\lambda=\mu=0\). The centre is exactly \(kh\).

**3.** The algebras \(k[\alpha_p]=k[x]/(x^p)\) and \(k[\mu_p]=k[u]/(u^p)\), with \(u=t-1\), are finite-dimensional local algebras. Their spectra have dimension zero. A dual-number point at the identity of either group has a freely chosen coefficient in \(k\), so its Lie dimension is one. Theorem 3.2 makes both non-smooth. The inclusion into \(\mathbf G_m\) sends \(1+c\epsilon\) to the same element, so its Lie map is the identity on \(k\). The source is finite of dimension zero, whereas the target has dimension one, so they are not isomorphic. An isomorphism on first-order directions does not recover higher-order equations.

**4.** Extend the field to an algebraic closure; smoothness will descend. The invariant-differential isomorphism makes \(\Omega_{B/k}\) free. For a maximal ideal, localize to \(R=B_{\mathfrak m}\). Its residue field is \(k\), so the free differential rank equals \(\dim\mathfrak mR/(\mathfrak mR)^2\). If that number is zero, Nakayama makes \(R\) a field. Otherwise choose a nonzero tangent parameter \(f\). Its differential extends to a basis, giving a derivation \(\delta\) with \(\delta f=1\). If \(fa=0\), repeated Leibniz gives \(a=(-1)^nf^n\delta^n(a)/n!\); Krull intersection forces \(a=0\). The conormal sequence then makes the differential module of \(R/(f)\) free of rank one less. Induction makes the quotient regular and the nonzerodivisor criterion makes \(R\) regular. Thus every maximal local ring is regular, all closed points are smooth, and the open smooth locus is the whole affine scheme. Descend to the original field. Reducedness was never assumed. The displayed division by \(n!\) fails at \(n=p\) in characteristic \(p\); indeed \(f=x\) in \(k[x]/(x^p)\) has \(\delta f=1\) although it is a zerodivisor.

**5.** The additive coproduct carries the defining equation to its sum in the two factors, its counit is zero, and its antipode preserves the ideal, so it defines a subgroup. In \(k(y)=\mathbf F_p(y)(a)\), the \(a\)-valuation of \(-ay^p\) is one. This excludes a \(p\)-th power and proves irreducibility of \(X^p+ay^p\); monicity and Gauss's lemma give a domain quotient in \(k[x,y]\). That quotient is finite integral over the injected ring \(k[y]\), with basis \(1,x,\ldots,x^{p-1}\), so its dimension is one. A dual-number pair \((c\epsilon,d\epsilon)\) satisfies the equation for every \(c,d\); hence Lie dimension is two. If \(b^p=a\), the substitution \(u=x+by\) identifies the extended algebra with \(k(b)[u,y]/(u^p)\). Its nonzero nilpotent \(u\) exhibits the failure of geometric reducedness and smoothness.

**6.** For any \(k\)-algebra \(A\) and \(a\in A\), the algebra \(A[z]/(z^p-a)\) is free of rank \(p\) over \(A\), so its spectrum is an fppf cover, and on that cover \(a\) has a \(p\)-th root. Thus \(F\) is surjective as an fppf sheaf, with schematic kernel \(\alpha_p\). On Lie spaces the inclusion sends \(c\epsilon\) to itself, whereas Frobenius sends \(c\epsilon\) to zero. The sequence is therefore

\[
0\longrightarrow k\xrightarrow{\,1\,}k\xrightarrow{\,0\,}k.
\]

It is exact through the middle term, as left exactness requires, but the last Lie map is not surjective. Infinitesimal directions in the target need not lift through a faithfully flat homomorphism.

**7.** On \(k[x]/(x^p)\), the invariant field corresponding to the standard tangent vector is \(D=d/dx\), and \(D^p=0\). On \(k[t]/(t^p-1)\), it is \(E=t\,d/dt\), and \(E^p=E\): each basis monomial \(t^j\), \(0\leq j<p\), is an eigenvector with eigenvalue \(j\), and \(j^p=j\). An isomorphism of group schemes carries invariant fields isomorphically to invariant fields, by differentiation of translations. On their one-dimensional spaces it would send \(D\) to \(cE\) for some nonzero \(c\in k\). Conjugating derivations by the isomorphism commutes with iteration, so \(D^p=0\) would give \((cE)^p=0\). But \((cE)^p=c^pE\ne0\). This contradiction proves nonisomorphism. Their zero ordinary brackets did not detect the extra operation.

**8.** The expansions \(1+\epsilon X\) and \(\det(1+\epsilon X)=1+\epsilon\operatorname{tr}(X)\) are polynomial identities over \(\mathbf Z\), so they give \(M_r(R)\) and its trace-zero submodule over every \(R\). For \(\mu_n\), the equation is \((1+\epsilon a)^n=1+n\epsilon a\), giving \(\operatorname{Ann}_R(n)\). Its cotangent module is \(R/nR\). Over \(\mathbf Z\), \(\operatorname{Ann}(p)=0\), whereas after extension to \(\mathbf F_p\) the Lie module is \(\mathbf F_p\). Nevertheless \(\mathbf Z[t]/(t^p-1)\) is free of rank \(p\), with basis \(1,t,\ldots,t^{p-1}\), so \(\mu_p\) is flat. The failure concerns dualization of the nonprojective cotangent module.

**9.** A matrix reducing to the identity is uniquely \(1+X\), with entries of \(X\) in \(J\). Since \(J^2=0\), \(X^2=0\), its inverse is \(1-X\), and \((1+X)(1+Y)=1+X+Y\). Conversely each such matrix is invertible and belongs to the kernel. Lift the entries of an invertible matrix modulo \(J\) arbitrarily to \(C\). Its determinant reduces to a unit. Every element that is a unit modulo \(J\) is a unit: a lift of its inverse gives product \(1+j\), whose inverse is \(1-j\). The lifted determinant is therefore a unit, and the adjugate formula makes the lifted matrix invertible. This proves surjectivity directly.

**Solution 10.** On the affine chart with coordinate \(z\), a vector field is \(f(z)\partial_z\). On the other chart, \(w=1/z\), it becomes \(-w^2f(1/w)\partial_w\). This is polynomial in \(w\) exactly when \(f\) has degree at most two. Hence the global fields have basis \(D_0=\partial_z\), \(D_1=z\partial_z\), \(D_2=z^2\partial_z\). Using the bracket-compatible identification of Proposition 1.7, a field \(D\) corresponds to the automorphism with pullback \(1-\epsilon D\). These give all identity-based infinitesimal automorphisms, whose composition adds coefficients. Directly,

\[
[f\partial_z,g\partial_z]=(fg'-gf')\partial_z,
\]

so \([D_0,D_1]=D_0\), \([D_1,D_2]=D_2\), \([D_0,D_2]=2D_1\). These equations retain their meaning in characteristic two, where the last bracket is zero. No classification of the full automorphism scheme is needed.

**Solution 11.** Theorem 2.5 describes the first tangent set as regular cocycles of \(\mathbf G_m\) into the additive Lie group of its target, with the action induced by conjugation. For a commutative target the action is trivial. The coefficient contraction gives \(c(g)=v-gv=0\), so no deformation is added. For \(\mathrm{GL}_r\), which is smooth, Corollary 2.6 gives conjugacy by a matrix reducing to the identity. Such conjugation can change the map: Section 7.3 of *Diagonalizable groups* explicitly conjugates the weight-one-plus-weight-zero action by \(1+\epsilon E_{12}\), producing an unequal family with the same reduction. The difference is the target's nontrivial adjoint action.

**Solution 12.** Take

\[
g=\begin{pmatrix}1&1\\0&1\end{pmatrix},\qquad
h=\begin{pmatrix}2&0\\0&1\end{pmatrix}.
\]

Then \((gh)^2=\begin{pmatrix}4&3\\0&1\end{pmatrix}\), whereas \(g^2h^2=\begin{pmatrix}4&2\\0&1\end{pmatrix}\). Thus squaring is not a group homomorphism. At the identity,

\[
(1+\epsilon X)^2=1+2\epsilon X,
\]

so its derivative is \(2\,1_{\mathfrak{gl}_2}\), in agreement with Proposition 2.4. A morphism fixing the identity can have a derivative there even when it does not preserve the group law. That derivative need not preserve the Lie bracket; for example doubling both inputs multiplies a nonzero matrix commutator by four, whereas doubling its output multiplies it by two.

## Appendix. Reducedness without a finiteness hypothesis

The finite-type theorem does not by itself settle arbitrary group schemes: an arbitrary group need not have affine neighbourhoods which are open subgroups. This appendix supplies the additional argument. We work over an algebraically closed field of characteristic zero until the final descent step. All quotients in this appendix mean fpqc sheaf quotients.

The identity-component theorem used below is *Group schemes over a field*, Theorem 2.3: the canonical component is a geometrically irreducible, quasi-compact, flat closed normal subgroup, and commutes with field extension. Its proof uses the component structure and open multiplication, rather than arbitrary characteristic-zero reducedness. Other exact internal providers are identified when used.

### A.1. Primary local rings and dense opens

Call a ring **primary** if each zero divisor is nilpotent. No Noetherian hypothesis is part of this definition.

**Lemma A.1. Coefficient fields.** A zero-dimensional local algebra \(Q\) over a characteristic-zero field \(k\) contains a subfield mapping isomorphically to its residue field \(E\).

**Proof.** Its maximal ideal \(N\) is its nilradical: a zero-dimensional local ring has just one prime. Choose a transcendence basis of \(E/k\) and lifts in \(Q\). They are algebraically independent, because any relation would remain a relation in \(E\). Every nonzero polynomial in them is a unit, since its residue is nonzero. They therefore generate a copy of the corresponding rational-function field in \(Q\).

Order the subfields of \(Q\) containing this field by inclusion, requiring that the residue map be injective on them. Unions of chains are such fields. A maximal field \(F\) exists. If its residue image is smaller than \(E\), take an element \(\alpha\) of \(E\) outside that image. It is algebraic and separable over the image of \(F\). Lift it to \(a\in Q\), and let \(p\in F[T]\) be its monic minimal polynomial. Then \(p(a)\) is nilpotent and \(p'(a)\) is a unit.

Newton's correction \(a\mapsto a-p(a)/p'(a)\) replaces the error by an element of \((p(a))^2\); this follows by expanding the polynomial at \(a\). The derivative remains a unit, since the residue of \(a\) remains \(\alpha\). After finitely many corrections the error is zero. A root thus obtained embeds the field \(F[T]/(p)\) in \(Q\), with the prescribed residue extension. This contradicts maximality. Hence \(F\to E\) is an isomorphism. Neither a nilpotence bound for all of \(N\) nor completeness of \(Q\) was used. \(\square\)

**Lemma A.2. Generic pairs.** Let \(G\) be geometrically irreducible over our algebraically closed \(k\). Every local ring of \(G\) is primary. Every dense open of \(G\), and of any finite power of \(G\), is schematically dense after any extension of the field.

**Proof.** First consider two zero-dimensional local \(k\)-algebras \(Q_1,Q_2\). Use Lemma A.1 to split their residue maps by coefficient fields \(E_1,E_2\). The ring \(D=E_1\otimes_k E_2\) is a domain. Here we use the elementary arbitrary-domain product proof immediately before Theorem 1.3 in *Group schemes over a field*: finite coefficient expansions reduce the assertion to finite-type domains and rational-point detection, and arbitrary domains are filtered unions of these subalgebras.

The algebra \(Q_1\otimes_kQ_2\) is free as a \(D\)-module: choose vector-space bases for the \(Q_i\) over the coefficient fields. Its augmentation to \(D\) has a nil kernel. Indeed that kernel is generated by elements from the two nilradicals; any one of its elements involves only finitely many such nilpotents, whose generated ideal is nilpotent. Write an element as \(d+n\), with \(d\in D\) and \(n\) in this kernel. If \(d\ne0\), this element becomes a unit after inverting \(d\). If it killed an element of the original algebra, some power of \(d\) would kill that element. Freeness over the domain \(D\) rules this out. Thus every zero divisor is in the nil kernel. Localizations of this primary ring are primary.

Let \(\eta\) be the generic point of \(G\), and put \(Q=\mathcal O_{G,\eta}\). This is zero-dimensional and local. The morphism

\[
\operatorname{Spec}(Q\otimes_kQ)\longrightarrow G,
\qquad (a,b)\longmapsto ab
\]

is flat: both maps from a generic local spectrum are flat, their product is flat, and multiplication is a projection after the isomorphism \((a,b)\mapsto(a,ab)\). It is surjective. For a point represented by \(g\in G(L)\), take the generic point of \(G_L\) and write \(g=x(x^{-1}g)\). Both factors are generic points of \(G_L\), since inversion and translation are isomorphisms. Both contract to \(\eta\), so the pair factors through the two generic local spectra and lies over \(g\).

A local ring of \(G\) consequently has a faithfully flat local map to a local ring of \(Q\otimes Q\). Such a map is injective. A subring of a primary ring is primary, proving the local assertion. On an irreducible affine open \(\operatorname{Spec}A\), each element outside the unique minimal prime remains nonnilpotent in every local ring: its image at the generic point is nonnilpotent. It is therefore a nonzerodivisor in every local ring, and in \(A\). The map from \(A\) to its generic localization is injective. An open containing the generic point is thus schematically dense.

The proof also works after any field extension \(L/k\). One can either extend further to an algebraic closure and descend injectivity, or use the same generic-pair argument there. Finite powers of \(G\) are geometrically irreducible group schemes, so the same proof applies to them. \(\square\)

We need a version of density that survives an arbitrary parameter algebra, not just a field.

**Lemma A.3. Constant families and coincidences.** Suppose \(X/k\) is quasi-compact and quasi-separated, and every affine open \(\operatorname{Spec}A\) is primary after every field extension, with geometrically integral reduction. Let \(S\) be a \(k\)-scheme and \(D\subset X\times S\) a quasi-compact open dense in every field fibre. For \(h_1,h_2\in\Gamma(D,\mathcal O_D)\), the condition that their pullbacks agree on \(D_T\) is represented by a closed subscheme of \(S\) with locally finitely generated ideal. The open \(D\) is universally schematically dense over \(S\).

**Proof.** We first prove a linear-algebra fact. If \(b\in A\otimes_k B\) is a nonzerodivisor on every field fibre over \(B\), multiplication by \(b\) remains injective after every \(B\)-algebra \(C\). To test a putative kernel element in \(A\otimes C\), choose the finite-dimensional \(k\)-space \(V\subset A\) containing its coefficients. Let \(W\subset A\) contain all products of a basis of \(V\) with the finitely many \(A\)-coefficients of \(b\). Multiplication is a finite matrix \(V\otimes B\to W\otimes B\). It has full column rank at every prime of \(B\). Its maximal minors generate the unit ideal. The adjugate of each square minor, composed with the corresponding row selection, gives a left inverse times that minor. A unit-ideal linear combination gives a left inverse over \(B\). Tensoring with \(C\) preserves it. This proves the fact even when \(A,B,C\) are non-Noetherian.

Now work on an affine \(S=\operatorname{Spec}B\), and fix a point \(s\). Cover \(X\) by finitely many affine opens. On one such open, \(D\) is a finite union of basic opens \(D(t_i)\) in \(\operatorname{Spec}(A\otimes B)\). The generic point of its field fibre belongs to one of them. Thus some \(b=t_i\) has nonzero image in \(A_{\mathrm{red}}\otimes\kappa(s)\). Expand that image in a \(k\)-basis of \(A_{\mathrm{red}}\). One of its finitely many coefficients is nonzero at \(s\). Invert that coefficient in \(B\). Every field fibre now has nonnilpotent \(b\), hence regular \(b\), by the primary hypothesis. The preceding matrix argument makes \(b\) universally regular. In particular \(D(b)\subset D\) is universally schematically dense in this affine constant family.

On \(D(b)\) write \(h_1-h_2=a/b^n\). After any base change its vanishing is equivalent to \(a=0\), since \(b\) remains a nonzerodivisor. A \(k\)-basis of \(A\) expresses \(a\) by finitely many coefficients in \(B\); their ideal represents the condition. Equality on \(D(b)\) implies equality on the whole \(D\) in this chart, by schematic density. Do this for the finitely many affine charts, shrinking a neighbourhood of \(s\) for each. The sum of their finite coefficient ideals represents equality on \(D\). These representing closed subschemes agree on overlaps because they represent the same functor, and hence glue. The universally dense basic opens also prove the stated universal density of \(D\). \(\square\)

### A.2. A normal affine subgroup defined by finitely many conditions

For a geometrically irreducible quasi-compact \(G\), a rational function means a regular function on a dense open, with agreeing representatives identified. Lemma A.2 justifies these identifications without assuming that \(G\) is reduced.

**Lemma A.4. Normal stabilizers.** There is a filtered decreasing family of closed normal subgroups \(H_i\subset G\), defined by locally finitely generated ideals, such that \(\bigcap_iH_i=e\). At least one \(H_i\) is affine.

**Proof.** For finitely many rational functions \(f_1,\ldots,f_r\), define \(H_f(T)\) by the identities

\[
f_j(xhy)=f_j(xy)\qquad(1\leq j\leq r).
\tag{A.1}
\]

These are identities of functions on their common domains in \((G\times G)_T\), for the universal outer variables \(x,y\), and after every base change of \(T\). Use a quasi-compact dense open representing each \(f_j\). The common domain over the parameter \(h\in G\) is quasi-compact, since \(G\) is quasi-compact and separated. In every field fibre it is dense: both maps \((x,y)\mapsto xy\) and \((x,y)\mapsto xhy\) are flat surjective maps from a geometrically irreducible product. Lemma A.3, with \(X=G\times G\), represents (A.1) by a closed subgroup with locally finitely generated ideal.

It is a subgroup because (A.1) can be applied successively to two inserted elements; substitution of \(xh^{-1}\) for \(x\) proves closure under inverse. It is normal because

\[
f_j(xghg^{-1}y)=f_j((xg)h(g^{-1}y))=f_j(xy).
\]

The substitutions are isomorphisms on the relevant constant families, so the function equalities are valid on universally dense common domains and hence on all common domains. This proves the assertions on arbitrary test schemes, including nonreduced ones. Taking unions of the finite lists makes the family decreasing.

Choose an affine open \(U\subset G\) containing the identity. Suppose \(h\in G(T)\) belongs to every \(H_f(T)\). Apply (A.1), with \(x=e\), to every function in \(\Gamma(U,\mathcal O_U)\). On \(V=U_T\cap h^{-1}U_T\), the maps \(y\mapsto hy\) and \(y\mapsto y\) have the same pullbacks of all affine coordinates, and so are equal. The map \(V\to T\) is quasi-compact, flat and surjective: its field fibres are intersections of two nonempty opens of a geometrically irreducible group. Thus it is an fpqc cover. Cancellation gives \(h=e\) on that cover, and descent gives \(h=e\) on \(T\). The scheme intersection is consequently exactly \(e\).

The closed subset \(G\setminus U\) is quasi-compact. If it met every \(H_i\), the finite-intersection property for the decreasing closed subsets would make it meet their intersection \(e\), a contradiction. Hence some \(H_i\) lies in \(U\). It is closed in the affine \(U\), so is affine. Its closed immersion in \(G\) is of finite presentation, because its ideal is locally finitely generated and \(G\) is quasi-compact. \(\square\)

The insertion condition in (A.1) is essential. Separate invariance under left and right translation of one function does not imply normality. For example, in \(\mathrm{SL}_2\) the function given by the lower-left matrix entry has the upper unitriangular subgroup as both endpoint stabilizers; that subgroup is not normal. Inserting an element between two arbitrary outer variables imposes the required normal-core condition.

**Lemma A.5. Affine groups in characteristic zero.** Every affine group scheme in characteristic zero is geometrically reduced.

**Proof.** Its commutative Hopf algebra \(B\) is a filtered union of finitely generated Hopf subalgebras. To check this assertion, put any finite list in a finite-dimensional subcomodule of the regular comodule using *Group schemes, actions and Hopf algebras*, Lemma 5.1. If \(\Delta(w_j)=\sum_iw_i\otimes a_{ij}\), counitality gives \(w_j=\sum_i\epsilon(w_i)a_{ij}\), and coassociativity gives \(\Delta(a_{ij})=\sum_\ell a_{i\ell}\otimes a_{\ell j}\). The algebra generated by these coefficients and their antipodes is a finitely generated Hopf subalgebra containing the list; the antipode squares to the identity in a commutative Hopf algebra. Finite sums of the chosen subcomodules give a filtered family.

The spectra of these subalgebras are finite-type groups. Theorem 4.3 makes them smooth and reduced. A nilpotent of \(B\) lies in one of these reduced subalgebras, and is zero. Applying the same argument after any field extension proves geometric reducedness. \(\square\)

### A.3. Finite coefficients and a generic quotient

Write \(K\boxtimes M=\operatorname{Frac}(K\otimes_kM)\) for field extensions of our algebraically closed \(k\). Their tensor product is a domain, by the domain product argument used in Lemma A.2.

**Lemma A.6. The smallest coefficient field.** Given finitely many elements of \(K\boxtimes M\), there is a smallest subfield \(F\subset K\), containing \(k\), over which all of them are defined. It is finitely generated over \(k\). Its canonical finite coefficients commute with embeddings of \(K\) and with extensions of the partner field \(M\).

**Proof.** Treat first \(f=v/w\). Choose finite-dimensional \(k\)-spaces \(V,W\subset M\) containing the numerator and denominator coefficients. In fixed \(k\)-bases consider

\[
E_K=\{(a,b)\in K\otimes(V\oplus W):a=fb\text{ in }K\boxtimes M\}.
\]

This nonzero finite-dimensional \(K\)-subspace has a unique reduced row-echelon basis. Let \(F\) be the field generated by its finitely many matrix entries. Any nonzero row has \(b\ne0\), because \(M\) embeds in the fraction field. The row expresses \(f=a/b\) over \(F\boxtimes M\).

If \(f\) is defined over \(L\boxtimes M\), where \(k\subset L\subset K\), then \(K\otimes_L(L\boxtimes M)\) embeds in \(K\boxtimes M\): it is the localization of the domain \(K\otimes M\) at the nonzero denominators from \(L\otimes M\). Flatness over the field \(L\) identifies \(E_K\) with \(K\otimes_L E_L\). Its canonical row-echelon entries therefore lie in \(L\). This proves minimality and also independence of the chosen spaces and bases. For a finite list take the field generated by the individual fields.

An embedding \(K\to K'\) preserves the kernel just used after scalar extension: the localized tensor product embeds in \(K'\boxtimes M\). Row reduction therefore carries each canonical entry to its image. Extending \(M\) to \(M'\) preserves the same kernel, since the old fraction field embeds in the new one; the entries are unchanged. Notice that this statement identifies individual canonical entries, not just their generated field. In particular

\[
(F\boxtimes K)\cap(K\boxtimes F)=F\boxtimes F
\quad\text{inside }K\boxtimes K:
\]

compute the coefficients in the second factor with partner \(F\), and then extend the partner to \(K\). Membership in \(K\boxtimes F\) says that all these coefficients lie in \(F\). \(\square\)

**Lemma A.7. A finite generic equivalence relation.** Let \(K/k\) be any field extension and let \(I\subset K\otimes_kK\) be a finitely generated ideal whose spectrum is an equivalence relation on \(\operatorname{Spec}K\). Then there is a finitely generated subfield \(F/k\) of \(K\) such that

\[
(K\otimes_kK)/I=K\otimes_FK.
\tag{A.2}
\]

Moreover \(F=\{a\in K:a\otimes1=1\otimes a\pmod I\}\).

**Proof.** Put all coefficients of generators of \(I\) in a finitely generated subfield \(K_0/k\), and let \(I_0\) be the ideal they generate in \(K_0\otimes K_0\). The maps from its two- and three-fold tensor products to those of \(K\) are faithfully flat. Reflexivity, symmetry and transitivity descend: respectively the generators vanish under multiplication, their swapped ideal is the same ideal, and the generators in factors 1 and 3 belong to the sum of their ideals in factors 1 and 2 and in factors 2 and 3. These are equalities or inclusions of ideals, detected faithfully flatly. Thus \(I_0\) is an equivalence relation too.

Choose a finitely generated domain \(A\subset K_0\) with fraction field \(K_0\), containing the coefficients. The finitely many witnesses for symmetry and transitivity involve denominators in the individual copies of \(A\). Inverting their product in \(A\) makes the ideal \(J\subset A\otimes A\) an equivalence relation on \(U=\operatorname{Spec}A\). Indeed passage from \(A^{\otimes n}\) to \(K_0^{\otimes n}\) only inverts elements in the individual factors, so a finite membership witness can be cleared by this one common localization. Reflexivity already holds in \(A\), since it holds in its fraction field.

Shrink \(U\) once more to make the first projection \(R=\operatorname{Spec}((A\otimes A)/J)\to U\) flat. Here is the required generic-freeness step. Present its finite-type coordinate algebra as \(A[T_1,\ldots,T_m]/J'\). Over \(K_0\), take a finite monic Gröbner basis of \(J'K_0[T]\); the leading-monomial ideal is finitely generated by the ascending-chain condition for monomial ideals. Clear the coefficients, the expressions of the basis in the original generators and of those generators in the basis, and the reductions of the finitely many S-polynomials. After one localization this is a monic Gröbner basis over \(A\); the standard monomials form a free \(A\)-basis of the quotient. This proves flatness without requiring the algebra to be finite as a module. Symmetry gives flatness of the other projection after restricting both objects to the same open. Reflexivity makes both projections surjective. They are of finite presentation, since all schemes now are of finite type over \(k\).

Apply the exact internal flat quotient theorem, *Algebraic spaces and stacks*, *The bootstrap theorem*, Theorem 4.1. It supplies an algebraic space \(X=U/R\), with \(U\to X\) faithfully flat of finite presentation and \(R=U\times_XU\). The closed endpoint map makes \(X\) separated: it is the pullback of its diagonal under the faithfully flat cover \(U^2\to X^2\). Finite type descends under this cover. Reducedness descends from \(U\), and its surjectivity makes \(X\) irreducible. Thus \(X\) is integral, separated and of finite type.

By *Quotients and torsors*, Lemma 11.1a, it has a dense affine open. Let \(F\) be the function field of that open. It is finitely generated over \(k\). The generic point of \(U\) maps to the generic point of \(X\), since the map is flat. Its map \(\operatorname{Spec}K_0\to X\) factors through \(\operatorname{Spec}F\). The latter generic-point inclusion is a monomorphism. Taking the self-fibre product of the generic point of \(U\) therefore gives

\[
(K_0\otimes_kK_0)/I_0=K_0\otimes_FK_0.
\]

Extending both field factors to \(K\) proves (A.2). Finally the equalizer of the two maps \(K\rightrightarrows K\otimes_FK\) is \(F\). For example, extend \(1\) to an \(F\)-basis of \(K\); coefficient comparison in that basis proves this directly. This gives the asserted description. \(\square\)

### A.4. A finite rational group and its regular realization

**Lemma A.8. Realizing a rational group over a field.** Suppose a finitely generated field \(F/k\) has rational multiplication and inversion, satisfying the group identities, and the universal left and right translations are birational. It is the function field of a smooth, connected, finite-type group scheme \(Q/k\), with these operations induced by its group law.

**Proof.** Choose a smooth integral affine model \(V\) of \(F\). Such a model exists in characteristic zero: take a separating transcendence basis, a primitive element for the remaining finite separable extension, and invert its discriminant and the finitely many denominators. The resulting algebra is étale over an open of affine space and has fraction field \(F\).

The graph of rational multiplication can be restricted so that its three pair-coordinate projections to \(V^2\) are open immersions. Indeed the first is the graph projection, and the other two are the birational universal translation maps; each birational map and its inverse are isomorphisms on suitable dense opens. Intersect these finitely many opens in the graph. All three open images are dense in \(V^2\).

Make the law strict as follows. For each image and each of its two coordinate projections, the points of \(V\) where its complement contains the whole geometric fibre form a constructible subset: equivalently that closed complement has fibre dimension \(\dim V\). The finite-type fibre-dimension theorem gives constructibility. None contains the generic point of \(V\), because the original image is dense. Remove the closures of these six bad subsets. On the remaining smooth dense open \(Y\), restrict the graph to \(Y^3\). Its pair projections are still open immersions and have dense fibres after either coordinate is fixed. To see this last statement after the restriction, the two graph projections sharing the fixed coordinate identify dense opens of the two other copies of \(V\). Requiring both to lie in the dense open \(Y\) leaves dense opens under that isomorphism. These density assertions are universal: on an affine constant family use the regular-element matrix argument of Lemma A.3. The reduced geometric fibres here are integral.

We can now use the exact internal translation-sheaf lemma, *Néron models*, Lemma 6.9. Its statement concerns an arbitrary strict law on a smooth separated \(Y/S\), so applies with \(S=\operatorname{Spec}k\); it uses neither Néron existence nor commutativity. It constructs a group sheaf \(\mathscr Q\), a representable open immersion \(\lambda:Y\to\mathscr Q\), and a representable smooth surjection

\[
d:Y^2\longrightarrow\mathscr Q,
\qquad(a,b)\longmapsto\lambda(a)\lambda(b)^{-1}.
\]

Here is the field gluing step, including why charts defined over \(k\) suffice. For each \(h\in\mathscr Q(k)\), translate the open chart \(Y\) by \(h\). Their overlaps are representable open subschemes of \(Y\), with isomorphisms satisfying the cocycle condition. Over an algebraically closed extension \(\Omega\), the inverse image under \(d\) of the condition \(h^{-1}g\in\lambda(Y)\), for a fixed \(g\in\mathscr Q(\Omega)\), is a nonempty open in \(Y_\Omega^2\). Nonemptiness follows from smooth surjectivity of \(d\) and the nonempty chart \(\lambda(Y_\Omega)\).

Every nonempty open in \(Y_\Omega^2\) contains a \(k\)-rational pair. To check this universal density, choose a nonzero defining function on an affine subopen, expand its finitely many \(\Omega\)-coefficients in a linearly independent \(k\)-list, and use density of rational points on the finite-type reduced \(k\)-scheme for one nonzero coefficient function. Its value on that rational point makes the original function nonzero. The chosen pair gives \(h=d(a,b)\in\mathscr Q(k)\) whose chart contains \(g\). For any scheme section of \(\mathscr Q\), these representable open inverse images therefore cover all its geometric points, and hence cover the scheme. Gluing the charts represents \(\mathscr Q\) by a smooth scheme \(Q\).

The map \(d\) makes it quasi-compact, hence of finite type. It also proves separatedness: the inverse image of its identity under \(d\) is the diagonal of the separated \(Y\), so the identity is closed by faithfully flat descent. The group diagonal is then closed by the difference map. The chart \(Y\) is dense, by the dense-fibre assertion in Lemma 6.9. The surjection from the integral \(Y^2\) makes \(Q\) irreducible and connected. On the chart its law is the original rational law, so its function field and operations are the prescribed ones. \(\square\)

**Lemma A.9. Integral normal quotients with finite equations.** Let \(P/k\) be geometrically integral and quasi-compact. If \(H\subset P\) is a closed normal subgroup whose immersion is of finite presentation, then \(P/H\) is a smooth finite-type group scheme and \(P\to P/H\) is an fpqc \(H\)-torsor.

**Proof.** Put \(K=k(P)\). The action relation \(R_H\subset P^2\), given by \((p,h)\mapsto(p,ph)\), is closed and of finite presentation: the difference map pulls back \(H\subset P\). Restrict both object coordinates to their generic local spectra \(\operatorname{Spec}K\). It becomes a finitely generated equivalence ideal in \(K\otimes K\). Lemma A.7 gives its quotient field \(F\subset K\), finitely generated over \(k\), with generic relation \(K\otimes_FK\).

We show that multiplication and inversion preserve this field rationally. For \(f\in F\), consider \(\Delta f\in K\boxtimes K\). Take its canonical left coefficients from Lemma A.6. If \(\alpha,\beta:K\to L\) agree on \(F\), their pair is a point of the generic relation. It represents \(x,y\) differing by an element of \(H\). After adjoining an independent generic variable \(z\), normality gives \(xz\) and \(yz\) in the same right coset. Both are generic points of \(P\), since multiplication by a field point is a translation. The definition of \(F\) on the generic relation consequently gives

\[
(\alpha\boxtimes1)(\Delta f)=(\beta\boxtimes1)(\Delta f).
\]

Canonical row-echelon coefficients have the same individual images under \(\alpha\) and \(\beta\). Apply this to the two maps into the fraction field of every minimal-prime quotient of \(K\otimes_FK\). This tensor ring is reduced in characteristic zero. One direct verification is to write \(K/F\) as a union of finitely generated subextensions; each has a separating transcendence basis and becomes finite étale over a localized polynomial algebra after a discriminant is inverted, so its tensor product with a field is reduced. The inclusions into the full tensor ring are injective. Thus a canonical coefficient has equal images in the two copies of \(K\), and belongs to their equalizer \(F\).

The same argument in the second variable uses \(zx,zy\), which are already in the same right coset, and puts all right coefficients in \(F\). Lemma A.6 then gives \(\Delta f\in F\boxtimes F\). Normality also makes \(x^{-1},y^{-1}\) differ by an element of \(H\); hence inversion preserves \(F\) by the same equalizer argument. All rational identities restrict from \(K\). The universal translation maps on \(F\boxtimes F\) are birational, because their inverse formulas use these restricted multiplication and inversion maps. Lemma A.8 supplies the smooth connected finite-type group \(Q\) with function field \(F\).

The inclusion \(F\subset K\) gives a dominant rational homomorphism \(P\dashrightarrow Q\). We give its extension argument to avoid a hidden finite-type assumption on \(P\). On a nonempty affine domain \(D\subset P\) where it is defined, the map \(D^2\to P\), \((a,b)\mapsto ab^{-1}\), is flat and surjective. Flatness follows from the projection description of multiplication; surjectivity follows because \(D_L\cap gD_L\ne\varnothing\) for every field point \(g\). It is quasi-compact, so is an fpqc cover. On it put \(q(a,b)=q(a)q(b)^{-1}\), using the rational map on \(D\). On its self-overlap these values agree: that overlap is an open of \(P^3\), via \(ab^{-1}=cd^{-1}\), and is geometrically integral; the rational homomorphism identity gives equality on a dense open, and the separated target gives equality everywhere. Descent extends the map to \(q:P\to Q\). Equality of the group identities on the dense rational domain proves that it is a homomorphism.

This dominant homomorphism is faithfully flat. Write \(F=k(Q)\), and let \(P_\eta=P\times_Q\operatorname{Spec}F\). It is nonempty, since \(q\) is dominant. The maps

\[
\operatorname{Spec}(F\otimes_kF)\to Q,
\qquad P_\eta\times_kP_\eta\to P
\]

given by multiplication are flat: generic-point inclusions of the reduced integral \(Q\) are flat, and multiplication is flat. They are surjective by the generic-pair argument. For the second one, at a field point \(g\) choose a generic \(b\) of \(P_L\); dominance after field extension puts both \(q(b)\) and \(q(gb)\) over the generic point of \(Q\), and \(g=(gb)b^{-1}\). Inversion preserves the generic point, so multiplication and the displayed difference factorization give the same surjectivity. Dominance after extension follows from geometric integrality and the injective function-field map, or by tensoring the finite affine-cover test for schematic dominance with \(L\).

The map \(P_\eta^2\to\operatorname{Spec}(F\otimes F)\) is faithfully flat, since each nonempty \(P_\eta\) is faithfully flat over the field \(F\). The commutative multiplication square makes the composite \(P_\eta^2\to P\to Q\) flat and surjective. Flatness descends along the flat surjection \(P_\eta^2\to P\), so \(q\) is flat and surjective. All maps from our quasi-compact sources to separated targets here are quasi-compact. Thus \(q\) is fpqc.

Finally its kernel is exactly \(H\), including the scheme structures. The two closed relations \(R_H\) and \(R_q=P\times_QP\) have the same restriction \(\operatorname{Spec}(K\otimes_FK)\) to both generic object coordinates. Both projections of either relation to \(P\) are flat. Restriction to a generic object coordinate is schematically dominant for a flat map to an integral scheme: on affine charts a flat module injects into its tensor product with the fraction field. After the first restriction, the other projection is still flat, since the first generic-point restriction is a flat base change. Thus restriction to both generic coordinates is schematically dominant in each relation. Each is the schematic closure of that same generic relation in \(P^2\), and they coincide. Pull back along the identity in the first factor to obtain \(H=\ker q\). The equality relation and fpqc surjectivity identify \(Q=P/H\), and give the torsor isomorphism \(P\times H=P\times_QP\). \(\square\)

### A.5. Finite nilpotence and the final reducedness argument

**Lemma A.10. A finite nilpotent thickening.** Suppose \(G\) is quasi-compact and geometrically irreducible, \(H\subset G\) is closed of finite presentation, and \(H\subset P=G_{\mathrm{red}}\). If \(P/H\) is a finite-type scheme and \(P\to P/H\) is an fpqc torsor, then the ideal of \(P\subset G\) is locally finitely generated and nilpotent.

**Proof.** Set \(Y=G/H\) as a sheaf and \(X=P/H\). The map \(X\to Y\) is a monomorphism: equality of two representatives from \(P\) in \(G/H\) is precisely equality modulo \(H\), which lies in \(P\).

First, equality of two \(Y\)-sections already defined over a ring \(R_i\) is detected at a finite stage of any filtered system \(R_j\) with colimit \(R\). Choose a common faithfully flat affine cover \(\operatorname{Spec}S_i\) of \(\operatorname{Spec}R_i\) on which both sections lift to \(G\). Their equality over \(R\) means that the difference of these lifts belongs to the closed subgroup \(H\) over \(S_i\otimes_{R_i}R\). This condition is given by finitely many equations: use the finitely presented immersion \(H\subset G\), a finite affine covering of \(G\), and a finite principal refinement on the affine \(\operatorname{Spec}S_i\). Their vanishing in the colimit occurs at some \(S_i\otimes R_j\). This remains a faithfully flat cover of \(R_j\), so the sections are equal in \(Y(R_j)\). No finite presentation of \(G\) or of that covering algebra was assumed.

Morphisms to the finite-type \(k\)-scheme \(X\) commute with filtered colimits of algebras. Explicitly, finite affine charts give finitely many generators and relations; a finite principal refinement of their inverse images gives finitely many overlap equalities and a unit-ideal identity for the covering. All these data and equalities descend to a common finite stage. Thus if \(g\in G(R_i)\) has its image in \(X(R)\subset Y(R)\), lift that \(X\)-section to a finite stage and then use the preceding equality property of \(Y\). At a later stage the image of \(g\) already belongs to \(X\).

The pullback \(G\times_YX\) is exactly \(P\): locally a representative in \(P\) differs from \(g\) by an element of \(H\subset P\), and membership in the closed subscheme \(P\) descends faithfully flatly. Consequently the preceding paragraph says that membership in \(P\), for a fixed \(G\)-section, descends along filtered algebra colimits.

On an affine chart \(\operatorname{Spec}B\subset G\), let \(N\) be its nilradical. The quotients \(B/I\), for finitely generated subideals \(I\subset N\), form a filtered system with colimit \(B/N\). Its universal section belongs to \(P\). The fixed universal \(G\)-section over \(B\) therefore belongs to \(P\) over some \(B/I\). This means \(N\subset I\), and hence \(N=I\) is finitely generated. Its finitely many generators are nilpotent, so the ideal is nilpotent. A finite affine covering of \(G\) gives one bound for the nilpotence of its ideal sheaf. \(\square\)

**Theorem A.11. Arbitrary characteristic-zero reducedness.** Every group scheme over a characteristic-zero field is geometrically reduced. There is no affine, quasi-compact, Noetherian or finite-type hypothesis.

**Proof.** First let \(k\) be algebraically closed and \(G\) geometrically irreducible. It is quasi-compact by *Group schemes over a field*, Lemma 2.1. Choose the affine closed normal subgroup \(H\) of Lemma A.4. Its immersion is of finite presentation. Lemma A.5 makes \(H\) geometrically reduced, so its inclusion factors through \(P=G_{\mathrm{red}}\). Over the perfect \(k\), this reduction is a subgroup, by *Group schemes over a field*, Proposition 4.1. It is integral and geometrically integral. The immersion \(H\subset P\) is still of finite presentation, by base change from \(H\subset G\), and \(H\) is normal in \(P\).

Lemma A.9 makes \(P/H\) a finite-type scheme, with \(P\to P/H\) an fpqc \(H\)-torsor. Lemma A.10 makes \(P\subset G\) a finitely generated nilpotent thickening. Apply the exact internal nilpotent-quotient result, *Quotients and torsors*, Corollary A.3, with \(L=P\). Its hypotheses are now all established: \(H\) is affine, \(P\subset G\) has a finitely generated nilpotent ideal, and the reduced quotient is a finite-type scheme with the specified torsor. It gives a finite-type scheme \(Z=G/H\) and an fpqc \(H\)-torsor \(G\to Z\).

Normality of \(H\) gives a group law on the quotient sheaf, hence on \(Z\). Theorem 4.3 makes \(Z\) smooth. Every geometric fibre of \(G\to Z\) is geometrically reduced: after a further field extension giving a point of its nonempty torsor, translation identifies it with the geometrically reduced \(H\). Reducedness descends under that field extension.

Flatness now proves that \(G\) is reduced. On an integral affine chart \(\operatorname{Spec}B\) of the smooth \(Z\), any affine chart \(\operatorname{Spec}A\) of its inverse image is flat over \(B\). Thus \(A\) injects into \(A\otimes_B\operatorname{Frac}B\). The latter is reduced, as an affine open of the geometrically reduced generic fibre. Every nilpotent of \(A\) therefore vanishes. These charts cover \(G\).

For an arbitrary \(G/k\), first extend to an algebraically closed field. Its canonical identity component \(G^0\) is a quasi-compact geometrically irreducible group, so the preceding argument makes it reduced. At the identity its local ring equals that of \(G\): a flat closed immersion gives a surjective flat local map, which is faithfully flat and therefore injective as well. For any point of \(G\), extend the field further to make it rational. The identity-component theorem commutes with this extension. Translation identifies its local ring with the reduced local ring at the identity. The local map from the original point to this rational lift is faithfully flat and injective, so its original local ring is reduced too. This proves reducedness without quasi-compactness of the whole group. Apply the same proof to every extension of the original characteristic-zero field to obtain geometric reducedness. \(\square\)

This proves the extension attributed to Perrin in Stacks Remark 047O. The approximation and generic-quotient method is explained in [Perrin]; the preceding proofs spell out the finite coefficients, normal stabilizers and nilpotent step required here. In characteristic zero the affine stabilizer is already reduced, so only the integral normal-quotient construction is needed. Smoothness still requires local finite presentation, as in Theorem 4.3.

## What this lesson assumes and does not prove

The imported commutative-algebra and scheme facts are: Noetherian local dimension is bounded by embedding dimension; equality characterizes regularity; regular local rings over a perfect field at points of a locally finite-type scheme characterize smoothness [Stacks, Tags 00TT–00TV]; local point dimension and its invariance under extension of the base field [Tags 02FX–02FY]; Krull intersection for a proper ideal in a Noetherian local ring [Tag 00IP]; regularity lifts across a nonzerodivisor with regular quotient [Tag 00NU]; and smoothness is fpqc local on the base [Tag 02VL]. We also use Nakayama, the conormal sequence, the Nullstellensatz, and existence of a separating transcendence basis over a perfect field. These are prerequisites from algebra and smooth morphisms. The group-scheme Lie, bracket, dimension and smoothness theorems are proved above.

Appendix A proves arbitrary characteristic-zero reducedness. Its exact internal providers are the identity-component theorem in *Group schemes over a field*, Theorem 2.3; the domain-product argument preceding that lesson’s Theorem 1.3; the flat relation quotient in AG-AS-02, Theorem 4.1; the dense-affine-space and nilpotent-torsor results in *Quotients and torsors*, Lemma 11.1a and Corollary A.3; and the general strict-law translation sheaf in *Néron models*, Lemma 6.9. These providers do not use arbitrary characteristic-zero reducedness. The additional scheme prerequisites in the appendix are the finite-type fibre-dimension constructibility theorem, descent for affine modules and morphisms, and the affine finite-presentation description by finitely many generators and relations; the required generic freeness, coefficient fields and coefficient descent are proved there. The equivalence between height-one finite groups and restricted Lie algebras is not asserted or used. Section 6 proves the operations and examples needed for the course.

## References

- **[Demazure]** Michel Demazure, *SGA 3, Exposé II: Fibrés tangents – Algèbres de Lie*, corrected re-edition of 14 October 2024. [Freely accessible text](https://webusers.imj-prg.fr/~patrick.polo/SGA3/Exp2-14oct24.pdf).
- **[Gille]** Philippe Gille, *Introduction to reductive group schemes over rings*, draft of 9 May 2025. [Author's freely accessible notes](https://math.univ-lyon1.fr/~gille/prenotes/reductive.pdf). The relative tangent, square-zero lifting and base-change examples above are independently written after comparison with these notes and Demazure's treatment.

- **[Stacks]** The Stacks Project, *Groupoid Schemes*, Tags 047I, 045X and 047N–047Q; *Varieties*, Tags 04QN–04QP; and the algebra and descent tags listed above. Read in [AI Integrated Stacks Project](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/), an edition with AI-proposed corrections and additions that is not reviewed by the maintainers of [the official Stacks Project](https://stacks.math.columbia.edu/). The proofs and exercises in this lesson are independently written.
- **[Perrin]** Daniel Perrin, *Approximation des schémas en groupes, quasi compacts sur un corps*, Bulletin de la Société Mathématique de France 104 (1976), 323–335, especially §§1–3 and Corollary 4.2; [article and full bibliographic record](https://www.numdam.org/item/BSMF_1976__104__323_0/). The article identifies itself as a summary with proof sketches. Detailed source comparison also used *Schémas en groupes quasi-compacts sur un corps et Groupes henséliens*, Orsay thesis, Chapters I–IV; [thesis PDF](https://bibliotheque.imo.universite-paris-saclay.fr/media/filer_public/99/55/99556864-9947-4630-8154-76b1bc0b3edc/p_perrin-109.pdf). Appendix A is independently written and provides its proofs rather than importing the conclusion from either citation.
- **[Milne]** J. S. Milne, *Algebraic Groups: The Theory of Group Schemes of Finite Type over a Field*, corrected author edition of 5 October 2021; Cambridge University Press, 2022. Chapter 10, sections a–e, treats Lie algebras and adjoint actions; Chapter 3, sections g–h, treats smoothness; Chapter 11, section h, treats height one. [Corrected author edition, freely available PDF](https://www.jmilne.org/math/Books/iAG2022.pdf).

The next lesson, *Group schemes over a field*, studies identity components, reduced subgroups and the finite étale component group, keeping the perfect-field condition visible.
