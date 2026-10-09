# Sheaf kernels and cotangent correspondences

A sheaf kernel describes an operation with an input variable and an output variable. Composing two such operations means eliminating a middle variable. At the level of sheaves we use a tensor product and a direct image with proper supports. At the level of cotangent bundles we match two covectors with opposite signs. This lesson explains how these two calculations fit together and why the hypotheses that connect them matter.

We assume bounded derived sheaf operations and the microsupport estimates taught in Composing sheaf operators through an intermediate space and [Transporting directional obstructions](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/sheaf-proof-readings/src/SH02/microsupport-operations.md#sh02-mo-diagonal--tensor-and-hom-on-one-manifold). Theorem 1 develops the kernel estimate in Pierre Schapira's *A short review on microlocal sheaf theory*, §2.4, equations (2.11)–(2.13), by tracing each intermediate covector through the three operation estimates in §2.3. The graph calculations, nonlinear example and solved exercises then test the distinction between a possible cotangent direction and nonzero output cohomology. The exact operation hypotheses and coefficient bounds remain explicit below.

*Written by GPT-6.1 Sol (OpenAI), Ultra, September 2026. Self-checked by the writing AI. New original text is public domain (CC0).*

## Variables and coefficient bounds

Let \(k\) be a commutative ring with identity and finite global dimension \(g\). Let \(X,Y,Z\) be finite-dimensional smooth real manifolds, Hausdorff and countable at infinity. No field, Noetherian, finite-rank or constructibility assumption is made. Write \(D^b(k_X)\) for bounded complexes of sheaves of \(k\)-modules up to quasi-isomorphism. Bounded means one finite cohomological interval works over the whole space. Our shift convention is

\[
H^j(F[s])=H^{j+s}(F).
\]

Every tensor product of complexes is derived over \(k\). The notation \(k_S\), for a closed submanifold \(S\), means the constant sheaf on \(S\) extended by its closed embedding. Properness of a map means inverse images of compact sets are compact. The functor \(Rf_!\) uses sections with support proper over the base.

For a kernel \(K\in D^b(k_{X\times Y})\), let

\[
\Phi_K(F)=Rq_{X!}(K\otimes^L q_Y^{-1}F),\qquad F\in D^b(k_Y).
\]

The output is on \(X\). Given \(L\in D^b(k_{Y\times Z})\), put

\[
K\circ_Y L
=Rq_{13!}(q_{12}^{-1}K\otimes^L q_{23}^{-1}L).
\tag{1}
\]

The ordinary composition theorem gives \(\Phi_K\Phi_L\simeq\Phi_{K\circ_Y L}\). This theorem concerns proper-support operations; it does not require the projections themselves to be proper. If \(K\in D^{[a,b]}\) and \(L\in D^{[c,d]}\), finite Tor dimension and the compact-support cohomological dimension of the fibre give

\[
K\circ_YL\in D^{[a+c-g,\,b+d+\dim Y]}(k_{X\times Z}).
\tag{2}
\]

The dimension bound in (2) is a manifold sheaf-cohomology bound. It does not require a choice of orientation. An orientation enters other formulas, such as exceptional inverse image of a submersion; it does not enter the definition (1).

## Why the input covector changes sign

Identify \(T^*(X\times Y)\) with \(T^*X\times T^*Y\). Attach to \(K\) the relation

\[
C_K=\{((x,\xi),(y,\eta)):(x,y;\xi,-\eta)\in\operatorname{SS}(K)\}.
\tag{3}
\]

This twists only the input covector. On the triple product, a covector pulled back from the first kernel has the form

\[
(x,y,z;\xi,-\eta,0).
\]

A covector pulled back from the second has the form

\[
(x,y,z;0,\eta,\zeta).
\]

Their sum is \((x,y,z;\xi,0,\zeta)\), which is horizontal for \(q_{13}\). Thus it can contribute to the direct image. If the output covector of the second kernel is denoted \(\eta\), its input covector is \(-\theta\), and the surviving pair is \(((x,\xi),(z,\theta))\). This is precisely ordinary composition of the twisted relations:

\[
C_K\circ C_L
=\{((x,\xi),(z,\theta)):
\exists(y,\eta),\ ((x,\xi),(y,\eta))\in C_K,
\ ((y,\eta),(z,\theta))\in C_L\}.
\tag{4}
\]

Relation composition records a possible covector. It does not assert that the corresponding sheaf cohomology is nonzero.

## A composition estimate with proper supports

Schapira's Theorem 2.11 supplies the submersion equality; Corollary 2.12(i) obtains the tensor estimate by pulling an external product back to the diagonal; Theorem 2.9 proves the proper-image estimate by commuting a local support test with proper direct image and evaluating on the fibre. His §2.4 combines them into the kernel estimate. The proof here expands that combination so that the zero middle covector, the support condition and the antipode can each be checked in coordinates.

We recall three microsupport facts with their hypotheses. For a submersion \(p\),

\[
\operatorname{SS}(p^{-1}F)=p_d p_\pi^{-1}\operatorname{SS}(F).
\tag{5}
\]

For bounded complexes \(A,B\) on a manifold \(M\), if
\(\operatorname{SS}(A)\cap\operatorname{SS}(B)^a\subset T_M^*M\), then

\[
\operatorname{SS}(A\otimes^LB)
\subset \operatorname{SS}(A)+\operatorname{SS}(B).
\tag{6}
\]

Here \(a\) negates a covector, and the sum is the fibrewise sum at the same base point. Under the hypothesis in (6) this sum is closed. For a smooth map \(f:M\to N\) proper on the support of \(A\),

\[
\operatorname{SS}(Rf_!A)
\subset f_\pi f_d^{-1}\operatorname{SS}(A),\qquad Rf_!A\simeq Rf_*A.
\tag{7}
\]

**Theorem 1.** Suppose the projection \(q_{13}\) is proper on

\[
S=q_{12}^{-1}\operatorname{supp}(K)
\cap q_{23}^{-1}\operatorname{supp}(L).
\tag{8}
\]

Suppose also that for every \((x,y,z)\) and every \(\eta\in T_y^*Y\),

\[
(x,y;0,\eta)\in\operatorname{SS}(K),\quad
(y,z;-\eta,0)\in\operatorname{SS}(L)
\quad\Longrightarrow\quad\eta=0.
\tag{9}
\]

Then

\[
\operatorname{SS}(K\circ_YL)
\subset\{(x,z;\xi,\zeta):
\exists(y,\eta),\ (x,y;\xi,-\eta)\in\operatorname{SS}(K),
\ (y,z;\eta,\zeta)\in\operatorname{SS}(L)\}.
\tag{10}
\]

Equivalently, \(C_{K\circ_Y L}\subset C_K\circ C_L\).

**Proof.** Set \(A=q_{12}^{-1}K\) and \(B=q_{23}^{-1}L\). The projections are submersions. Formula (5) identifies their microsupports as

\[
\begin{aligned}
\operatorname{SS}(A)
&=\{(x,y,z;\xi,\alpha,0):(x,y;\xi,\alpha)\in\operatorname{SS}(K)\},\\
\operatorname{SS}(B)
&=\{(x,y,z;0,\beta,\zeta):(y,z;\beta,\zeta)\in\operatorname{SS}(L)\}.
\end{aligned}
\]

A covector in \(\operatorname{SS}(A)\cap\operatorname{SS}(B)^a\) must have first and last components zero, with middle components \(\alpha=-\beta\). Condition (9) says that this middle component vanishes. The hypothesis of (6) therefore holds, and

\[
\operatorname{SS}(A\otimes^LB)
\subset\{(x,y,z;\xi,\alpha+\beta,\zeta):
(x,y;\xi,\alpha)\in\operatorname{SS}(K),
(y,z;\beta,\zeta)\in\operatorname{SS}(L)\}.
\]

The support of \(A\otimes^LB\) is contained in \(S\). If support is taken as its closed support, the inclusion still holds because \(S\) is closed. Properness on \(S\) implies properness on this support. Apply (7) to \(q_{13}\). Its cotangent pullback sends \((x,z;\xi,\zeta)\) to \((x,y,z;\xi,0,\zeta)\). A lift through the displayed sum must satisfy \(\alpha+\beta=0\). Write \(\alpha=-\eta\), \(\beta=\eta\). This gives (10). Negating the surviving input covector gives (4). All complexes in this calculation are bounded by finite Tor and manifold dimension, as in (2). \(\square\)

The properness condition in this theorem is about supports in the ordinary product of manifolds. A local theorem on open cotangent regions can instead impose properness of a microsupport projection. These are different hypotheses, and Theorem 1 does not assert the latter theorem.

In particular, the ordinary support condition in (8) and the pure-middle-covector exclusion in (9) are the two clauses of Schapira's (2.12). Neither is a condition on a chosen cotangent region alone. The proof uses (9) before integration, to justify an ordinary fibrewise tensor sum, and uses (8) only at the direct-image step. This order makes clear why properness cannot repair a failed noncharacteristic tensor argument.

## Graph kernels and changes of coordinates

Let \(f:Y\to X\) be a smooth map and let \(i_f:Y\hookrightarrow X\times Y\) send \(y\) to \((f(y),y)\). Its graph is closed. Define \(G_f=i_{f*}k_Y\).

**Proposition 2.** There is a natural isomorphism \(\Phi_{G_f}(F)\simeq Rf_!F\). Moreover,

\[
C_{G_f}
=\{((f(y),\xi),(y,d f_y^t\xi)):y\in Y,\ \xi\in T_{f(y)}^*X\}
\tag{11}
\]

when \(k\neq0\).

**Proof.** Projection formula for the closed embedding gives
\(G_f\otimes^Lq_Y^{-1}F\simeq i_{f*}F\), since \(q_Yi_f=\mathrm{id}_Y\). Composition of proper-support images and \(q_Xi_f=f\) give the functor statement.

The microsupport of a nonzero constant sheaf on a smooth closed submanifold is its full conormal bundle. A tangent vector to the graph is \((d f_y v,v)\). A covector \((\xi,\nu)\) annihilates every such vector exactly when
\(\nu=-d f_y^t\xi\). Twisting the second component as in (3) yields (11). \(\square\)

For the zero coefficient ring all kernels and microsupports vanish; the functor statement remains true, while the equality with a generally nonempty conormal is not asserted.

If \(f\) is a diffeomorphism, (11) is the graph of the cotangent transformation

\[
\chi_f(y,\eta)
=(f(y),(d f_y^t)^{-1}\eta).
\tag{12}
\]

It preserves the tautological one-form. Indeed, for a tangent vector at \((y,\eta)\) with base component \(v\), evaluation of the target covector on \(d f_yv\) is
\(((d f_y^t)^{-1}\eta)(d f_yv)=\eta(v)\).
Taking exterior derivatives shows that it preserves the cotangent symplectic form. It also commutes with positive scaling of covectors. This is the most direct example of a homogeneous symplectic transformation acting on sheaves.

For smooth maps \(g:Z\to Y\) and \(f:Y\to X\), the graph kernels satisfy

\[
G_f\circ_YG_g\simeq G_{fg}.
\tag{13}
\]

To verify this as a statement about kernels, the intersection of the two pulled-back graphs is parametrized by \(z\mapsto(fg(z),g(z),z)\). The two graph equations are transverse because the first equation has the identity in the \(x\) variable and the second has the identity in the \(y\) variable. Their derived tensor is the constant sheaf on this intersection: at a point its tensor is either \(k\otimes_k^Lk\simeq k\) or zero, and the multiplication map gives the isomorphism at all stalks. Projection to \((x,z)\) identifies this intersection with the closed graph of \(fg\), a proper embedding. Its direct image is \(G_{fg}\). No orientation line or cohomological shift is introduced.

## A nonlinear example

Consider the diffeomorphism

\[
f:\mathbb R^2\longrightarrow\mathbb R^2,
\qquad f(u,v)=(u,v+u^2).
\]

Write an input covector as \(a\,du+b\,dv\). Since

\[
d f^t=\begin{pmatrix}1&2u\\0&1\end{pmatrix},
\]

the transformation (12) is

\[
(u,v;a,b)\longmapsto(u,v+u^2;a-2ub,b).
\tag{14}
\]

The graph conormal in the product has coordinates
\((\xi_1,\xi_2;-\xi_1-2u\xi_2,-\xi_2)\).
Its input after twisting is \((\xi_1+2u\xi_2,\xi_2)\), which inverts to (14).
Thus the antipodal sign and the transpose have different jobs: the sign comes from relation convention; the transpose comes from differentiating the graph.

## When a possible direction disappears

Take \(X=Z=\{\mathrm{pt}\}\), \(Y=S^1\), and a field \(k\). Let \(K\) be a rank-one local system on the circle with monodromy \(\lambda\neq1\), and let \(L=k_{S^1}\). Both microsupports are the zero section, so (9) holds. The support condition is proper because the circle is compact. Their convolution is \(R\Gamma(S^1;K)\).

Cut the circle at a point and trivialize the local system on the resulting interval. Gluing the two ends imposes the map \(\lambda-1:k\to k\). The resulting cellular cochain complex is

\[
\bigl[k\xrightarrow{\lambda-1}k\bigr],
\]

in degrees zero and one. Since the differential is invertible, the convolution vanishes. The relation on the right of (10) nevertheless contains the zero covector of the point. This gives a strict inclusion without violating either hypothesis of Theorem 1. The cell calculation uses the usual cellular computation for a local system, established in algebraic topology.

## Exercises with solutions

### A scaling graph

*Difficulty: Introductory.*

Let \(f(t)=3t\) on \(\mathbb R\), with \(k\neq0\). Compute the twisted graph relation and its inverse. Show that using the untwisted conormal as if it were the graph of a transformation produces the wrong composite.

**Solution.** A graph conormal has \(\eta=-3\xi\). The twisted input is \(-\eta=3\xi\), so
\(\chi_f(t,\alpha)=(3t,\alpha/3)\).
The inverse is \((x,\xi)\mapsto(x/3,3\xi)\), exactly the cotangent lift of \(f^{-1}\). Their composite is the identity. If one uses the untwisted input, the proposed map is instead \((t,\alpha)\mapsto(3t,-\alpha/3)\). Composing this with the correct inverse gives \((t,-\alpha)\), the antipodal map, rather than the identity. This diagnoses a mismatch of conventions; a consistently untwisted calculation must insert the antipodal map explicitly at composition.

### An unbounded middle variable

*Difficulty: Intermediate.*

Take \(X=Z=\{\mathrm{pt}\}\), \(Y=\mathbb R\), and \(K=L=k_{\mathbb R}\), with \(k\neq0\). Explain which hypothesis of Theorem 1 fails and compute the convolution. Compare ordinary cohomology.

**Solution.** The cancellation condition holds because the constant sheaf has only zero covectors. The support \(S=\mathbb R\) is not proper over a point. The convolution is \(R\Gamma_c(\mathbb R;k)\simeq k[-1]\), with its nonzero cohomology in degree one. Ordinary cohomology is \(R\Gamma(\mathbb R;k)\simeq k\), in degree zero. One can calculate the compact-support group by the relative cohomology of a closed interval modulo its endpoints. This example shows why replacing \(!\) by \(*\) needs its own hypothesis.

### A failed cancellation test

*Difficulty: Intermediate.*

Take \(X=Z=\{\mathrm{pt}\}\), \(Y=\mathbb R\), and \(K=L=k_{\{0\}}\). Compute \(S\), verify properness, and test (9).

**Solution.** Suppose first that \(k\neq0\). The support intersection is the point \(0\), so it is proper. Both kernels have the full cotangent fibre over zero as microsupport. Every nonzero \(\eta\in T_0^*\mathbb R\) satisfies both clauses on the left of (9). Thus cancellation fails. In this particular example the convolution is still \(k\); failure of a sufficient hypothesis is not a proof that the conclusion is false. Theorem 1 simply provides no estimate through its noncharacteristic tensor argument in this case. If \(k=0\), every unital \(k\)-module is zero, so \(K=L=0\), both microsupports and \(S\) are empty, and the convolution is zero. The empty support is proper and (9) holds vacuously in this case.

### Shifts and inverse kernels

*Difficulty: Intermediate.*

Let \(f:Y\to X\) be a diffeomorphism and \(m\in\mathbb Z\). Find an inverse kernel for \(G_f[m]\), and determine the degrees of its action on a sheaf in degree zero.

**Solution.** Formula (13) gives
\(G_f\circ_YG_{f^{-1}}\simeq k_{\Delta_X}\) and
\(G_{f^{-1}}\circ_XG_f\simeq k_{\Delta_Y}\).
Shifts add under convolution, so the inverse kernel is \(G_{f^{-1}}[-m]\). Since a diffeomorphism has exact direct image, \(\Phi_{G_f[m]}F\simeq f_*F[m]\), whose only nonzero cohomology is in degree \(-m\) when \(F\) is a nonzero degree-zero sheaf. The inverse returns that degree to zero. No dimension correction is needed.

## References

- Pierre Schapira, [*A short review on microlocal sheaf theory*](https://webusers.imj-prg.fr/~pierre.schapira/LectNotes/MuShv.pdf), 19 January 2016: coefficient and orientation conventions, pp. 6–7; conormal and half-space examples, Example 2.5; functorial operations, Theorems 2.8–2.11 and Corollary 2.12, pp. 10–13; kernel convolution and its two hypotheses, §2.4, pp. 13–14.
- Masaki Kashiwara and Pierre Schapira, [*Microlocal Study of Sheaves*](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf), Astérisque 128 (1985), §§4.1–4.2 and §6.3. Proposition 4.2.1 and the proof of Proposition 4.2.2, pp. 64–65, supply earlier external-operation arguments; Proposition 6.3.3, pp. 110–111, gives the localized composition antecedent, whose hypotheses differ from Theorem 1 here.

**Construction and remaining prerequisites.** The human mathematical credit for the composition estimate belongs to the cited microlocal sheaf calculus. The present account orders the calculation around horizontal covectors and then checks graph kernels at stalks, derives the cotangent lift from the graph tangent space, and uses a circle local system to show that the estimate can be strict. These explicit calculations and all four solutions are retained as programme arguments; no claim of a new composition theorem is made. The source review assumes the six operations and gives only a sketch of part of its inverse-image theorem. Accordingly, this reading still depends on the linked proofs of the six-operation identities, finite Tor and manifold cohomological-dimension bounds, and microsupport estimates. Comparing the selected human passages does not close every transitive prerequisite.
