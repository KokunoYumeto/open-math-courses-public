# Hecke functors and Hecke eigensheaves

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Draft under mathematical proof repair; full proof closure pending. Public domain (CC0).*

This lesson remains under proof repair. Every cited theorem used as a mathematical input needs a complete proof here or an exact matching earlier programme proof. The historical self-check did not certify that full dependency closure.

A Hecke correspondence has an input bundle, an output bundle, and an isomorphism away from the point of modification. Its kernel carries the representation of the dual group. Composing two correspondences composes the kernels; geometric Satake identifies that composition with tensor product. The eigencondition must respect these identifications, rather than supply unrelated isomorphisms one representation at a time.

Let \(X/k\) be a smooth projective connected curve over an algebraically closed field of characteristic zero, let \(G\) be connected reductive, and put \(Y=\operatorname{Bun}_G\). The automorphic category is
\(\mathcal C=\operatorname{Dmod}_{1/2}(Y)\), defined in the [previous lesson](sheaves-and-d-modules-on-bun-g.md). Complexes are cohomologically graded.

We use right D-modules, exceptional pullback, and the tensor product
\[
M\otimes^!N=\Delta^!(M\boxtimes N).
\]
Its unit on a smooth space \(Z\) is the dualizing object \(\omega_Z=p_Z^!k\). For a flat local system \(E\) on \(X\), write \(E^\omega\) for its dualizing-normalized crystal. Over \(\mathbb C\), it corresponds to \(E[2]\) under the ordinary topological Riemann–Hilbert convention. Thus \(i_x^!E^\omega=E_x\), and
\((E\otimes E')^\omega=E^\omega\otimes^!E'^\omega\).
The moving de Rham Hecke unit will be \(F\boxtimes\omega_X=p_X^!F\), and the fixed-point functor is obtained by \(i_x^!\). These choices prevent an unrecorded curve shift.

In the finite-field portion we instead use ordinary local systems, ordinary pullback, and ordinary restriction to a point. The IC shifts, Tate factors, and Weil structures are specified in §6. This is the trace normalization; it is not an identification of all de Rham objects with arithmetic sheaves.

Our direction agrees with Lesson 1: for \(GL_n\), a positive elementary operator takes the values of \(F\) on smaller bundles \(E'\subset E\) and outputs a value at \(E\). In rank one its function operator is \(f(L)\mapsto f(L(-x))\). Some references reverse these two arrows; we will identify that difference explicitly.

## 1. The Hecke stack and its bounded pieces

An \(S\)-point of \(\operatorname{Hecke}_X\) is
\[
(P_{\mathrm{in}},P_{\mathrm{out}},x,
 \beta:P_{\mathrm{in}}|_U\simeq P_{\mathrm{out}}|_U),
\qquad
U=(X\times S)\setminus\Gamma_x .
\]
It has projections
\[
Y\xleftarrow{a}\operatorname{Hecke}_X
 \xrightarrow{b}Y\times X,
\qquad a=P_{\mathrm{in}},\quad b=(P_{\mathrm{out}},x).
                                                        \tag{1.1}
\]
Arrows are isomorphisms of both bundles commuting with \(\beta\).

Fix an output bundle and a point, and trivialize that bundle on the formal disc. A modification then corresponds to a lattice, or for general \(G\) to a point of the affine Grassmannian \(G(K_x)/G(O_x)\). Changing the trivialization acts by \(G(O_x)\); changing the parameter acts by formal-coordinate automorphisms. Thus the fibre before choosing frames is the associated Grassmannian, not a globally chosen copy with preferred coordinates.

Its dominant-coweight orbit \(\operatorname{Gr}_\lambda\) has dimension
\[
d_\lambda=\langle2\rho,\lambda\rangle.
\]
For \(GL_n\) and \(\lambda=(1^r,0^{n-r})\), the input is \(E'\subset E\) with quotient \(k_x^r\); the fibre is \(\operatorname{Gr}(r,n)\), of dimension \(r(n-r)\). The convention is fixed by this target-relative lattice description.

We use two geometric inputs. Formal-disc gluing identifies modifications with this local Grassmannian; its family form is the Beauville–Laszlo gluing theorem. For reductive \(G\), each Schubert closure is projective, and its spread over the curve gives a proper bounded Hecke projection to \(Y\times X\). Confirmed locators are [Beilinson–Drinfeld §§5.2.1–5.2.3 and 5.3.10–5.3.11](https://math.uchicago.edu/~drinfeld/langlands/QuantizationHitchin.pdf); the family gluing input was identified in Lesson 2. We use their local geometry with the assigned output convention.

There is a useful distinction between a framed and an unframed fibre. Fixing the output bundle as an object, including its identification, gives the Grassmannian; no automorphism of a modification inducing the identity on that output remains. Passing to an output isomorphism class alone also remembers the output's stabilizer. The fixed-bundle fibre is the one used for the Hecke sum.

**Example 1.1.** For a rank-\(n\) output \(E\), length-one downward modifications are the kernels of quotient lines \(E_x\twoheadrightarrow Q\). They are parameterized by the projective space of quotient lines, conventionally \(\mathbb P(E_x^*)\) as lines in the dual. For a fixed smaller input \(E'\), the possible outputs lie between \(E'\) and \(E'(x)\), so the opposite projection has a projective fibre too. Interchanging these descriptions interchanges the bundle arrows; it does not keep the rank-one formula unchanged.

## 2. The Satake kernel and the functor on the full category

Here is the precise Satake input. Geometric Satake identifies finite-dimensional representations of the Langlands dual \(\check G\) with the spherical IC category. The irreducible of highest weight \(\lambda\) corresponds to the IC object on \(\overline{\operatorname{Gr}}_\lambda\), restricting to the constant sheaf shifted by \(d_\lambda\) on its smooth orbit. Convolution realizes tensor product; fusion gives the ordinary symmetry, with its standard parity correction, and all associativity and diagonal compatibilities. In characteristic zero this has the de Rham incarnation. We import that theorem, including the descent to families and the half-twisted Hecke action; [BD §§5.3.5–5.3.6, 5.3.13–5.3.17, 5.3.21–5.3.23](https://math.uchicago.edu/~drinfeld/langlands/QuantizationHitchin.pdf) and [Gaitsgory’s outline, §4.4.3](https://arxiv.org/abs/1302.2506) give confirmed constructions. We prove the formal consequences for Hecke functors.

For \(V\in\operatorname{Rep}(\check G)\), let \(\mathcal K_V\) be the **relative Satake kernel** on the Hecke stack. Its twisting is the ratio of the output half-gerbe to the input half-gerbe. Tensoring it with an input object therefore leaves exactly the output twisting. The half twist is the one specified in GLC I §1.1; its remark on Hecke functors explains why it retains the usual representation category.

The relative normalization is part of the kernel, and is important. On a framed chart \(U\) of the output bundle and a coordinate chart of \(X\), with compatible local trivializations of the half gerbes, its local form is
\[
\omega_U\boxtimes\omega_X\boxtimes\operatorname{Sat}(V).
                                                        \tag{2.1}
\]
The relative Grassmannian factor is normalized by IC, and the base factors by dualizing objects. On a source-framed chart the orbit label is the opposite relative position, hence the dual highest weight. The two descriptions glue by the Hecke descent data. In particular \(\mathcal K_V\) is not an unshifted constant sheaf called “IC” on the whole Hecke stack.

Define
\[
H_V(F)=b_*\bigl(a^!F\otimes^!\mathcal K_V\bigr)
 \in\operatorname{Dmod}_{1/2}(Y\times X),\qquad
H_{V,x}=(1_Y\times i_x)^!H_V .                           \tag{2.2}
\]
For a direct sum of representations use the corresponding direct sum of kernels. A finite-dimensional representation has only finitely many highest weights, so its kernel has bounded relative support.

**Proposition 2.1.** Formula (2.2) defines a continuous functor on all of \(\mathcal C\), including objects that are not holonomic, and has the required output half twist.

**Proof.** Choose a bound containing the finitely many Schubert supports. On that piece, \(b\) is representable and proper. Exceptional pullback, the tensor operation with the fixed kernel, and proper direct image are defined for the full D-module categories and preserve colimits. Their twisting characters multiply as input times output/input, leaving output. These constructions satisfy smooth descent, so the result is independent of charts.

For a larger bound, extend the kernel by zero through the closed embedding. The projection formula and functoriality of proper direct image identify the two outputs. On the unbounded stack of bundles, restriction to a quasicompact open in the output is compatible with this construction by proper base change. The restriction-limit description from Lesson 3 therefore glues the local outputs on all of \(Y\times X\). No intermediate extension of a varying nonholonomic \(F\) is required: intermediate extension has already been used to construct the fixed Satake kernel. \(\square\)

**Normalization check.** The trivial representation has the delta kernel on the identity modification. On its support this is \(\omega_Y\boxtimes\omega_X\). The projection formula for that closed support gives
\[
H_{\mathbf1}(F)=F\boxtimes\omega_X,\qquad
H_{\mathbf1,x}(F)=F .                                  \tag{2.3}
\]
This verifies the moving and fixed units.

For a minuscule weight the fibre is smooth, so its IC factor is \(k[d_\lambda]\) in the topological normalization. At a fixed point, the constant input therefore gives fibre cohomology shifted by \(d_\lambda\), rather than by \(2d_\lambda\). Indeed exceptional pullback contributes the relative dualizing shift, while \(\otimes^!\) with (2.1) removes it and supplies IC. The moving point carries the additional \(\omega_X\); applying \(i_x^!\) removes that curve factor. This check is why the ordinary formula “pull back, multiply by IC, push forward” must specify its tensor and relative shifts.

## 3. Composition is convolution, with its coherences

Fix \(x\). The double Hecke stack classifies
\[
P_0\xrightarrow[\text{off }x]{\beta_1}P_1
 \xrightarrow[\text{off }x]{\beta_2}P_2.
\]
Let \(u\) forget \(P_1\) and compose the two punctured isomorphisms. Its bounded restriction is the global version of the Grassmannian convolution map.

**Theorem 3.1.** There are natural isomorphisms
\[
H_{V,x}\circ H_{W,x}\simeq H_{V\otimes W,x}.
                                                        \tag{3.1}
\]
They satisfy the monoidal associativity and unit constraints. The symmetry comes from fusion as the two modification points move together.

**Proof.** Write out the two pull-push functors. In the fibre product where the first output equals the second input, proper base change moves the second exceptional pullback across the first proper pushforward. The projection formula combines the two kernel factors. Functoriality of direct image then identifies the composition with the pull-push along the double Hecke stack, followed by \(u_*\).

On an output-framed chart, represent the last modification by \(g_V\) and the preceding one by a lattice represented by \(g_W\) in that modified frame. The resulting input lattice is represented by \(g_Vg_W\). The two kernel factors thus give the twisted external product on
\(G(K_x)\times^{G(O_x)}\operatorname{Gr}\), and \(u_*\) gives
\(\operatorname{Sat}(V)*\operatorname{Sat}(W)\).
The Satake tensor isomorphism identifies this with
\(\operatorname{Sat}(V\otimes W)\). The relative base factors in (2.1) and the half-gerbe ratios cancel at the middle bundle. This proves (3.1) locally and hence by descent.

For three modifications, either association forgets the same two middle bundles from the same triple Hecke stack. The base-change and projection-formula identifications compose to the same direct image. The Satake associator is the one obtained from that triple convolution. Its pentagon on four modifications therefore transfers to the Hecke functors. Inserting the identity modification transfers the Satake unit to (2.3).

At distinct points, modifications commute: the formal discs are disjoint, and gluing in either order produces canonically the same bundle and punctured trivialization. This supplies the interchange over \(X^2\setminus\Delta\). Fusion extends the Satake kernels across the diagonal and identifies their diagonal restriction with convolution, carrying the usual symmetry. This extends interchange to the tensor symmetry in (3.1). Its hexagon is the fusion hexagon, transported through the same kernel construction. The extension and symmetry are the imported fusion theorem; the functor identities and their transfer are the deductions just proved. \(\square\)

One should distinguish the statement at a fixed point from a mistaken composition of moving-point functors with incompatible domains. Iterating moving functors gives an object on \(Y\times X^2\). Pulling exceptionally to the diagonal produces (3.1) in the moving version. On the disjoint locus it is the external product of the two labelled operations.

For a finite nonempty set \(I\), there is correspondingly
\[
H_{(V_i),I}:\mathcal C\longrightarrow
 \operatorname{Dmod}_{1/2}(Y\times X^I).
\]
A surjection \(I\twoheadrightarrow J\) gives a diagonal \(X^J\to X^I\). On that diagonal the representation at \(j\) is
\(\bigotimes_{i\mapsto j}V_i\). This is an identification of the kernels and functors, with associativity for composites of surjections; it is more than a statement about pointwise fibres.

The Ran space is the prestack colimit of \(X^I\) under these diagonals. In the de Rham formulation one uses \((X^I)_{\mathrm{dR}}\). The spread representation category \(\operatorname{Rep}(\check G)_{\mathrm{Ran}}\) uses the same collision tensor products and disjoint-point factorization. Their pull-push construction gives its action on \(\mathcal C\). We use the nonempty, hence nonunital Ran convention of Gaitsgory’s outline §§4.1–4.4; the single-point trivial-representation unit (2.3) is still present. Contractibility of Ran and the subsequent spectral-action localization are not needed to prove (3.1).

## 4. The eigencondition as a coherent structure

Let \(\mathcal E\) be a flat \(\check G\)-bundle on \(X\). Each \(V\) gives a flat associated local system \(V_{\mathcal E}\), naturally in representation morphisms and compatibly with tensor product.

An **\(\mathcal E\)-Hecke eigenobject** is a nonzero \(F\in\mathcal C\) equipped with isomorphisms
\[
\alpha_V:H_V(F)\simeq F\boxtimes(V_{\mathcal E})^\omega
                                                        \tag{4.1}
\]
and their factorization compatibilities. They are natural in \(V\), additive, and unital. Applying \(\alpha_W\) and then \(\alpha_V\) to the double Hecke operation must agree, under (3.1), with \(\alpha_{V\otimes W}\). Over distinct points these maps commute with the permutation of points and factors; fusion supplies their compatible extension on collisions. Equivalently give the compatible \(X^I\)-versions of (4.1) for all finite sets and diagonal maps. In DG categories these agreements include higher coherent homotopies.

These conditions have consequences that weak eigen-isomorphisms lack. If \(e:V\to V\) is an idempotent, naturality makes \(\alpha_V\) intertwine its two actions. It then restricts to an eigen-isomorphism for the summand \(\operatorname{im}e\), since the categories split idempotents. Without naturality, arbitrary choices of \(\alpha_V\) can mix summands and need not define an eigenstructure for the representation category.

**Rank-one example.** Put \(G=\mathbb G_m\), and use the trivial root of its normalized determinant line from Lesson 3. For the character of weight \(m\in\mathbb Z\), the Hecke stack is the graph of
\[
c_m:Y\times X\to Y,\qquad c_m(L,x)=L(-mx).
\]
Its relative Grassmannian is a point, so (2.2) reduces to
\[
H_m(F)=c_m^!F.                                         \tag{4.2}
\]
In ordinary Betti or arithmetic normalization this is \(c_m^*F\). At a fixed point the map \(L\mapsto L(-mx)\) is an isomorphism, so its exceptional and ordinary inverse-image normalizations agree.

If \(A\) is a multiplicative rank-one local system on the Picard stack, with its unit and associative symmetric multiplication, then the bundle tensor-product map gives
\[
H_m(A)\simeq A\boxtimes
       \bigl(\operatorname{Abel}_{-m}^*A\bigr)^\omega .
\]
Here \(A\) on \(Y\) is in the ordinary-local-system normalization, as in Lesson 3. Since
\(\operatorname{Abel}_{-m}(x)=\mathcal O_X(-mx)\),
the eigenvalue for \(m=1\) is \(\operatorname{Abel}_{-1}^*A\), and for \(m\) it is its \(m\)-th tensor power. Multiplicative coherence proves the eigen-coherence, including negative weights. For a general \(F\), (4.2) is a pullback and has no such external-product decomposition.

In [FGV §1.1 and the end of §1.3](https://arxiv.org/abs/math/0012255), the larger bundle is the input, and the rank-one functor pulls back along \(L\mapsto L(x)\). That is the opposite convention. Reversing relative position reverses highest weights; on the dual group the comparison is described by the Chevalley involution. This course retains the negative Abel map and the Frobenius direction already fixed in Lesson 1.

## 5. Which representations determine an eigenstructure?

For \(GL_n\) the exterior powers \(\Lambda^r\mathrm{std}\), \(1\le r\le n\), are the elementary minuscule representations. Their Hecke correspondences have Grassmannian fibres and relative dimensions \(r(n-r)\). The determinant case has a single modification \(E(-x)\).

**Proposition 5.1.** Every finite-dimensional rational \(GL_n\)-representation is a summand of a finite sum of objects
\[
\mathrm{std}^{\otimes N}\otimes\det^{-r},\qquad N,r\ge0.
                                                        \tag{5.1}
\]
Consequently a natural tensor-compatible eigenstructure on the standard representation and determinant inverse determines it on all representations by sums and summand projectors. The elementary exterior-power eigenconditions must be equipped with these compatibilities; isolated isomorphisms do not suffice.

**Proof.** In characteristic zero rational representations of \(GL_n\) are semisimple. An irreducible has highest weight
\(\lambda_1\ge\cdots\ge\lambda_n\) with integral entries. Choose \(r\ge0\) so that \(\lambda_n+r\ge0\). Then \(\lambda+(r,\ldots,r)\) is a partition of some \(N\). The corresponding Schur module is the image of a Young idempotent in a tensor power of the standard representation. Tensor it with \(\det^{-r}\) to recover \(\lambda\); direct sums recover all finite representations.

The standard eigen-isomorphism, iterated using Theorem 3.1, gives the tensor-power eigen-isomorphism. Compatibility with permutations makes it commute with the Young idempotents, so it descends to Schur modules. Naturality gives the same restriction for any other summand projector and makes the answer independent of a chosen presentation by (5.1).

The determinant operator is invertible: at a fixed point it is pullback along \(E\mapsto E(-x)\), with inverse \(E\mapsto E(x)\). If its eigenvalue is \(\det\mathcal E\), applying the inverse operator to its eigen-isomorphism gives the eigenvalue \((\det\mathcal E)^{-1}\). The same holds in the moving family, keeping the dualizing \(X\)-normalization. Thus the determinant inverse required in (5.1) is supplied by coherent determinant data. \(\square\)

The proposition is a sufficiency statement for coherent data, not a theorem extending arbitrary unrelated exterior-power isomorphisms. [FGV §1.3](https://arxiv.org/abs/math/0012255) derives exterior powers from the standard eigencondition with symmetric-group compatibility; its proof uses the smallness of the global flag-modification map and the Springer sign summand. Our deduction above uses the stipulated tensor action and its projectors, avoiding an additional claim to prove that geometric smallness theorem here.

## 6. Trace functions and the IC sign

For this section let \(X/\mathbb F_q\) be smooth projective connected, choose \(\ell\ne\operatorname{char}(\mathbb F_q)\), and use constructible \(\overline{\mathbb Q}_\ell\)-complexes with Weil structure. Fix a square root of \(q\) to define half Tate factors. The raw spherical Haar normalization is \(\operatorname{vol}(G(O_x))=1\), and the function operator uses the downward convention of §1. We first take a rational point \(x\); the closed-place version is specified below.

At a fixed closed point \(x\), let \(k_{V,x}\) be the function of the arithmetic Satake kernel on the local Grassmannian. We normalize its Weil structure so that its trace corresponds to \(V\) under the positive normalized classical Satake isomorphism. The IC convention is explicit: on a minuscule orbit of dimension \(d\), start with
\[
\overline{\mathbb Q}_\ell[d](d/2).
\]
Its literal alternating trace is \((-1)^d q_x^{-d/2}\). Multiply its Frobenius structure by \((-1)^d\) to obtain the positive trace \(q_x^{-d/2}\). For general \(\lambda\), use the factor
\((-1)^{\langle2\rho,\lambda\rangle}\) on its IC kernel. This is monoidally compatible: tensor-product highest weights differ from the sum by coroots, and \(2\rho\) pairs evenly with coroots. Equivalently, choosing half Tate Frobenius \(-q_x^{-1/2}\) incorporates the same parity. We use the parity-adjusted structure with the fixed positive-symbol Satake convention.

**Theorem 6.1.** For an arithmetic sheaf \(F\) and its alternating trace function \(f_F\), the fixed-point Hecke functor has trace
\[
f_{H_{V,x}F}(P)
 =\sum_{z\in b_x^{-1}(P)(\mathbb F_q)}
       k_{V,x}(z)\, f_F(P_{\mathrm{in}}(z)).
                                                        \tag{6.1}
\]
Under the bundle double-quotient identification this is spherical convolution by the classical Satake element attached to \(V\), with the declared arrow and Weil normalization.

**Proof.** Use ordinary pullback and the arithmetic relative kernel in this sheaf theory. At the fixed output bundle, the bounded projection is representable and proper. Proper base change identifies its stalk with the cohomology of that fibre with coefficients in the pulled-back sheaf and kernel. The compact-support trace formula expresses its alternating Frobenius trace as the weighted point sum. Tensor-product traces multiply, giving (6.1).

Trivialize the output disc. Its input modifications become the cosets of the local spherical double cosets. Lesson 1 identifies the fixed-output sum with right convolution under Haar measure with \(K_x\)-volume one. The kernel's trace is the Satake function \(k_{V,x}\). The identification of this IC-trace function with the classical representation Satake element is the arithmetic Satake compatibility theorem, used as an input; the pull-push trace deduction is the one just proved. \(\square\)

For a closed place \(x\) of degree \(e\), distinguish two constructions. Restricting the moving functor to \(x\) gives a functor over \(k_x=\mathbb F_{q^e}\), whose trace compares functions on bundles over \(k_x\). To obtain the local Hecke operator on bundles over the original \(\mathbb F_q\), use instead the correspondence of modifications along the whole closed divisor \(x\). After base change it is the product of the modifications at its \(e\) conjugate geometric points, with the external product of their Satake kernels and cyclic Frobenius descent. Its fixed-output \(\mathbb F_q\)-points are the modifications over \(k_x\).

The cyclic trace on that descended kernel is the local trace of \(\operatorname{Frob}_x=\operatorname{Frob}_q^e\). To see the linear-algebra identity, expand a cyclic permutation with coefficient maps on a homogeneous tensor basis: a diagonal term forces the indices around the cycle to match, and the resulting graded trace is the supertrace of the composite around one factor. Normalize that local Weil structure by the parity convention above. Proper base change and the same trace formula then prove (6.1) for this closed-place correspondence, with \(q_x=q^e\). This explains why a closed-place operator is not simply an ordinary stalk of the moving object on \(\mathbb F_q\)-points.

No factor \(1/\#\operatorname{Aut}(P)\) occurs in this fixed-output fibre sum. Absolute integrals over a stack use groupoid weights, but the representable fibre here fixes \(P\) with its identification.

For \(GL_n\) and an elementary minuscule representation,
\[
f_{H_{\Lambda^r\mathrm{std},x}F}
       =q_x^{-r(n-r)/2}\,T_{r,x}f_F.                   \tag{6.2}
\]
Thus for \(GL_2\), with \(f_F=1\),
\[
f_{H_{\mathrm{std},x}F}=q_x^{-1/2}(q_x+1)
 =q_x^{1/2}+q_x^{-1/2}.                               \tag{6.3}
\]
With the unadjusted canonical Weil structure, the answer in (6.3) has a minus sign. With the raw unnormalized constant kernel, it is \(q_x+1\). These are three explicitly different normalizations. A cohomological shift supplies the sign; a Tate factor supplies the power of \(q_x\).

The arithmetic moving-point version uses the ordinary local system on \(X\) as unit and ordinary restriction to \(x\). The de Rham moving version (2.2) uses \(\omega_X\) and exceptional restriction. The fixed-point operators and the IC fibre normalization specified above are the comparison. One must not take an ordinary stalk of a dualizing-normalized moving object and silently discard its curve factor.

## 7. A convergent Eisenstein-type function and its eigenvalues

Here is a function example for which the infinite flag sum and the local Hecke calculation can both be justified. Take \(X=\mathbb P^1_{\mathbb F_q}\), a rational point \(x\), and nonzero complex numbers \(s,t\) satisfying
\[
|s/t|>q^2.
\]
For a rank-two bundle \(E\), define
\[
F_{s,t}(E)=
 \sum_{\substack{L\subset E\\ L\text{ a saturated line subbundle}}}
       s^{\deg L}\,t^{\deg(E/L)}.                       \tag{7.1}
\]
“Saturated” means that \(E/L\) is a line bundle. The sum is over actual subbundles of a fixed bundle, so two different embeddings with the same image count once. Isomorphisms of \(E\) permute these images and preserve their degrees. Thus (7.1), when convergent, is a function of the bundle's isomorphism class.

**Convergence.** A rational frame of \(E\) gives a generically invertible map \(E\to\mathcal O(D)^2\) after its finitely many poles are cleared by an effective divisor \(D\). This map is injective: its kernel is torsion and \(E\) is torsion-free. On \(\mathbb P^1\), \(\mathcal O(D)\simeq\mathcal O(N)\), where \(N=\deg D\). Every degree-\(a\) line is \(\mathcal O(a)\). If it injects into \(E\), it gives a nonzero homomorphism to \(\mathcal O(N)^2\), so \(a\le N\).

For \(a\le N\), the vector space of such homomorphisms has dimension \(2(N-a+1)\). In particular the number \(n_a(E)\) of degree-\(a\) subbundles satisfies
\[
n_a(E)\le q^{2(N-a+1)}
          =q^{2(N+1)}q^{-2a}.
\]
This bound counts all homomorphisms, hence also bounds the smaller set of saturated images. Writing \(e=\deg E\), the absolute value sum is bounded by
\[
q^{2(N+1)}|t|^e
      \sum_{a\le N}\left(\frac{|s/t|}{q^2}\right)^a .
\]
The latter is a geometric series converging toward \(a=-\infty\). This proves absolute convergence for every \(E\).

Here are the elementary projective-line computations used in the count. Every line bundle on a smooth curve has a nonzero rational section and hence is represented by its divisor, as in Lesson 1's divisor description. On \(\mathbb P^1\), a closed point of degree \(e\) on the affine chart is cut out by an irreducible polynomial \(p(t)\); its divisor is \(\operatorname{div}(p)=x-e\infty\). Thus every rational divisor is linearly equivalent to its degree times \(\infty\). A principal divisor has degree zero, since the degrees of the zeros and poles of a rational function agree. This proves \(\operatorname{Pic}(\mathbb P^1)=\mathbb Z\) over the finite field used here.

A section of \(\mathcal O(b\infty)\) is a rational function with no finite pole and a pole of order at most \(b\) at infinity. It is therefore a polynomial of degree at most \(b\). For \(b\ge0\), the basis \(1,t,\ldots,t^b\) gives \(h^0(\mathcal O(b))=b+1\); for \(b<0\) there is no nonzero section. These calculations justify the dimensions used in the series directly. No splitting theorem for arbitrary rank-two bundles is needed.

**Theorem 7.1.** The raw downward operators of Lesson 1 satisfy
\[
T_{1,x}F_{s,t}=(t^{-1}+q\,s^{-1})F_{s,t},
\qquad
T_{2,x}F_{s,t}=(st)^{-1}F_{s,t}.                       \tag{7.2}
\]

**Proof.** A length-one modification of \(E\) is
\[
K=\ker(E\longrightarrow k_x),
\]
determined by a quotient line \(\ell:E_x\twoheadrightarrow k\). A saturated line \(M\subset K\) has a unique saturation \(L\) in \(E\). Moreover \(M=L\cap K\). Indeed \((L\cap K)/M\) is torsion, whereas \(K/M\) is torsion-free. Conversely, if \(L\) is saturated in \(E\), then \(M=L\cap K\) is saturated in \(K\), because \(K/M\) injects into the line bundle \(E/L\). These constructions give a bijection between pairs \((K,M)\) in the Hecke sum and pairs \((L,\ell)\), retaining all modification multiplicities.

Put \(Q=E/L\). There are exactly two cases.

- If \(\ell\) vanishes on \(L_x\), it factors through the one-dimensional \(Q_x\). There is exactly one such quotient line. Then \(M=L\) and \(K/M=Q(-x)\). Its weight is \(t^{-1}s^{\deg L}t^{\deg Q}\).
- If \(\ell\) is nonzero on \(L_x\), there are \(q\) such quotient lines among the \(q+1\) points of \(\mathbb P(E_x^*)\). Then \(M=L(-x)\), and \(K\to Q\) is surjective, so \(K/M=Q\). Its weight is \(s^{-1}s^{\deg L}t^{\deg Q}\).

For the last surjectivity claim, work over the DVR at \(x\) and split \(E=L\oplus Q\) there. A nonzero functional on \(L_x\) lets one adjust the \(L\)-coordinate of a lift of any section of \(Q\) to make its residue lie in \(K\). Away from \(x\), the map is already surjective. In the first case the image consists instead of sections of \(Q\) vanishing at \(x\).

The finite Hecke sum consists of \(q+1\) absolutely convergent sums. The convergence bound also justifies the bijective rearrangement by \(L\). Each \(L\) now contributes the multiplier \(t^{-1}+q s^{-1}\), giving the first equation of (7.2).

For the determinant operator the only smaller bundle is \(E(-x)\). Tensoring a saturated line inclusion by \(\mathcal O(-x)\) gives a bijection between its lines and those of \(E\). Both line and quotient degrees decrease by one. Thus \(F_{s,t}(E(-x))=(st)^{-1}F_{s,t}(E)\), which proves the second equation. \(\square\)

Under the positive normalization in §6, the standard eigenvalue is
\[
q^{-1/2}(t^{-1}+q s^{-1})
       =\frac{q^{1/2}}s+\frac{q^{-1/2}}t .
\]
The unordered Satake parameters are consequently
\[
\alpha_1=q^{1/2}s^{-1},\qquad
\alpha_2=q^{-1/2}t^{-1}.
\]
Their product is \((st)^{-1}\), exactly the determinant eigenvalue. For positive real \(s,t\) in the convergence region, the function is nonzero: a nonzero generic line in \(E\), saturated over the curve, gives at least one positive summand. This example is an Eisenstein-type function obtained by summing the character \(s^{\deg L}t^{\deg Q}\) over Borel reductions. It is a direct function calculation, not a construction of a geometric Eisenstein eigensheaf. Nor can the constant function be obtained by setting \(s=t=1\) in this convergent series: that pair lies outside the proved convergence region.

## 8. Exercises and complete solutions

**Exercise 8.1 (easy).** For \(G=\mathbb G_m\), identify the Hecke functor of weight \(m\), its fixed-point inverse, and the eigenvalue on a multiplicative rank-one local system. Check the coherence for weights \(m,n\) and the direction of the trace-function formula.

**Solution 8.1.** With output \(L\), the input for weight \(m\) is \(L(-mx)\). The relative Grassmannian is a point, so the moving functor is \(c_m^!\), where \(c_m(L,x)=L(-mx)\). At a fixed point this is pullback by the isomorphism \(t_{-mx}:L\mapsto L(-mx)\); its inverse is pullback by \(t_{mx}\). Composition of the translations gives \(t_{-mx}t_{-nx}=t_{-(m+n)x}\), proving the tensor law on weights.

For a multiplicative local system \(A\), pull its multiplication isomorphism back along \((L,x)\mapsto(L,\mathcal O(-mx))\). This gives
\[
c_m^!A\simeq
 A\boxtimes(\operatorname{Abel}_{-m}^*A)^\omega .
\]
The associativity of multiplication identifies the composite for \(m,n\) with that for \(m+n\); symmetry identifies the two orders, and the unit gives weight zero. Since \(\mathcal O(-mx)\) is the \(m\)-th tensor power of \(\mathcal O(-x)\), the eigenvalue is the \(m\)-th power of \(\operatorname{Abel}_{-1}^*A\), including inverse powers.

In arithmetic ordinary normalization, multiplicativity gives \(f_A(L)=\chi(L)\) and
\[
T_m f_A(L)=\chi(L(-mx))
 =\chi(\mathcal O(-mx))\chi(L).
\]
The negative sign in the Abel map is thus forced by the input/output direction, rather than chosen independently for the sheaf and function descriptions.

**Exercise 8.2 (easy).** Describe the standard \(GL_n\) Hecke correspondence at a fixed point. Compute its fibre over a fixed output, its dimension, its change of degree, and the number of modifications at a rational point over \(\mathbb F_q\).

**Solution 8.2.** A quotient line of \(E_x\) gives \(E'=\ker(E\to k_x)\). Conversely, any subbundle with quotient \(k_x\) gives such a quotient line, uniquely up to scaling its target. In a DVR frame choose the functional to be projection onto the first residue coordinate. Then
\[
E'_x=tO_xe_1\oplus O_xe_2\oplus\cdots\oplus O_xe_n.
\]
This proves local freeness of the kernel and the relative position \((1,0,\ldots,0)\). The quotient-line parameter space is \(\mathbb P(E_x^*)\), of dimension \(n-1\); its determinant is \(\det(E')=\det(E)(-x)\), so the degree decreases by \(\deg x\). Over a rational point there are
\[
\#\mathbb P^{n-1}(\mathbb F_q)
   =\frac{q^n-1}{q-1}=1+q+\cdots+q^{n-1}
\]
modifications. The count follows by dividing the \(q^n-1\) nonzero linear functionals by the \(q-1\) possible scalars. Distinct quotient lines remain distinct modifications even if their kernels are isomorphic as abstract bundles.

**Exercise 8.3 (medium).** Explain precisely in what sense eigenconditions for \(\Lambda^r\mathrm{std}\), \(1\le r\le n\), determine the \(GL_n\) eigencondition for every rational representation. State the compatibility that must be added to isolated isomorphisms.

**Solution 8.3.** The \(r=1\) condition supplies the standard representation. The \(r=n\) condition supplies its determinant, and invertibility of the determinant Hecke translation supplies the determinant inverse, with inverse rank-one eigenvalue. Take a highest weight \(\lambda_1\ge\cdots\ge\lambda_n\), and choose \(r\ge0\) with \(\lambda_n+r\ge0\). The weight \(\lambda+(r,\ldots,r)\) is a partition of \(N=\sum_i(\lambda_i+r)\). Its Schur module is a Young-idempotent summand of \(\mathrm{std}^{\otimes N}\); twisting this summand by \(\det^{-r}\) recovers the irreducible of weight \(\lambda\). Semisimplicity supplies all representations as finite sums of these.

The eigen-isomorphism on the tensor word is obtained by iterating the standard and determinant-inverse eigenmaps through Theorem 3.1. It must commute with the symmetric-group permutations and all \(GL_n\)-equivariant maps between these tensor words, including the determinant identification
\(\Lambda^n\mathrm{std}\simeq\det\) and the evaluation \(\det\otimes\det^{-1}\to\mathbf1\). Then it commutes with Young projectors and restricts to their images. If a representation has two such presentations, the equivariant comparison maps intertwine the restricted isomorphisms, so the result is independent of the presentation. For a morphism between representations, insert their summand inclusion and projection into a map of tensor words; the same compatibility proves naturality.

Thus sufficient data are coherent tensor and factorization eigenmaps on these generators, respecting their relations. The other exterior-power maps are the antisymmetric summands of the standard tensor powers and must agree with that construction. Isolated exterior-power isomorphisms do not impose these relations. For instance, rescaling the determinant eigenmap while keeping the standard one fixed changes its comparison with the antisymmetrization of the \(n\)-fold standard eigenmap. Such data fail the determinant relation and do not define the required tensor eigenstructure.

**Exercise 8.4 (medium).** Prove \(H_{V,x}H_{W,x}\simeq H_{V\otimes W,x}\) from the two-step correspondence. Explain where associativity and symmetry enter and why equality of trace functions would not prove this categorical statement.

**Solution 8.4.** Denote the first modification by \(P_0\to P_1\), labelled by \(W\), and the second by \(P_1\to P_2\), labelled by \(V\). Form their fibre product over \(P_1\). Pulling \(H_{W,x}(F)\) back to the second correspondence and using proper base change replaces the inner pushforward by pushforward from this fibre product. The projection formula puts the pulled-back \(F\) and the two kernels into a single integrand. The output map is now the composite two-step projection to \(P_2\).

Forget \(P_1\). On a frame of \(P_2\), the relative input is \(g_Vg_WG(O_x)\), so forgetting \(P_1\) is the convolution map and its direct image of the two-kernel integrand is \(\operatorname{Sat}(V)*\operatorname{Sat}(W)\). The middle half twists have exponents \(+1/2\) and \(-1/2\) and cancel. The relative dualizing normalizations cancel through the exceptional tensor product, leaving precisely the single-kernel normalization. Geometric Satake identifies this convolution with \(\operatorname{Sat}(V\otimes W)\), proving the functor isomorphism on charts; descent proves it globally.

With three labelled modifications both associations use the same triple fibre product and forget the same intermediate bundles. The Satake associator and the functoriality of these base-change maps identify the two calculations; four modifications supply the pentagon. This supplies associativity, whereas symmetry uses the disjoint-point interchange and its fusion extension across the diagonal. The latter is the imported Satake symmetry. Trace functions could at most compare alternating Frobenius traces; different complexes can have the same trace, and traces do not retain these natural transformations or coherence diagrams.

**Exercise 8.5 (hard).** Compute the standard Hecke operator on the constant function \(1\) for \(GL_2\). Obtain the raw answer, the answer for the canonical IC Weil structure, and the answer for the positive Satake convention. Check the determinant and the resulting Satake parameters.

**Solution 8.5.** Put \(Q=q_x\). For a rational point over the field of size \(Q\), each fixed rank-two output has a projective line of quotient lines, so the raw function calculation is
\[
T_{1,x}1=(Q+1)1.
\]
Its determinant modification has one input \(E(-x)\), giving \(T_{2,x}1=1\).

For the geometric calculation, the fibre has cohomology
\[
H^0(\mathbb P^1,\overline{\mathbb Q}_\ell)
     =\overline{\mathbb Q}_\ell,\qquad
H^2(\mathbb P^1,\overline{\mathbb Q}_\ell)
     =\overline{\mathbb Q}_\ell(-1),
\]
and no other cohomology. Geometric Frobenius acts by \(1\) and \(Q\), so its alternating unshifted trace is \(1+Q\). The IC kernel is \(\overline{\mathbb Q}_\ell[1](1/2)\). The shift changes the sign and the Tate factor multiplies by \(Q^{-1/2}\), giving
\[
-Q^{-1/2}(1+Q)=-(Q^{1/2}+Q^{-1/2}).
\]
Multiplying the Weil structure by the parity \(-1\) gives the positive Satake eigenvalue \(Q^{1/2}+Q^{-1/2}\). The central determinant weight has orbit dimension zero, so its eigenvalue remains \(1\). The unordered pair \((Q^{1/2},Q^{-1/2})\) has this sum and product and is the corresponding Satake parameter. The computation applies to the constant function on every component of \(\operatorname{Bun}_2\); it makes no claim that this function is cuspidal.

## 9. What has been proved, and what is imported

We proved that the bounded relative kernels define the functors on the full automorphic category, that composition of their pull-push operations is convolution, and that the Satake associator, unit, symmetry and factorization compatibilities transfer to those functors. We formulated the strong eigencondition, proved the rank-one translation formula and the coherent \(GL_n\) representation-generation statement, and derived the function operator from the arithmetic kernel by the trace formula. The convergent rank-two flag sum and both of its elementary eigenvalues were proved directly. These are the formal and elementary results assigned to this lesson.

The deep geometric inputs remain explicit: formal-disc gluing and properness of bounded Schubert families; geometric Satake with its IC kernels, fusion, tensor equivalence and ordinary parity-corrected symmetry; descent of the kernels to the half-twisted automorphic category; the six-operation base-change and projection formulas; and the arithmetic IC-trace/classical-Satake compatibility and compact-support trace formula. This lesson does not re-prove geometric Satake, the Beauville–Laszlo theorem, or the existence of eigensheaves for general \(\check G\)-local systems. A coherent eigencondition is a definition, not an existence theorem.

The confirmed source comparisons are:

- [Beilinson–Drinfeld, *Quantization of Hitchin’s integrable system*](https://math.uchicago.edu/~drinfeld/langlands/QuantizationHitchin.pdf), §§5.2.1–5.2.6 for the Hecke stack and its local description, §§5.3.5–5.3.6 for convolution, §§5.3.10–5.3.17 for its global spread and fusion, §§5.3.21–5.3.23 for parity and the dual group, and §§5.4.1–5.4.2 for the Hecke action. The consulted draft uses a semisimple group in its Satake identification; the connected reductive formulation and half-twisted extension are the modern input below. Draft annotations in §5.3.23 are not used as proved formulas.
- [Frenkel–Gaitsgory–Vilonen, *On the geometric Langlands conjecture*](https://arxiv.org/abs/math/0012255), §§1.1–1.3, for the \(GL_n\) Hecke functor, symmetric compatibility, exterior powers and determinant. Its input is the larger bundle. Our output is the larger bundle, so its positive Abel formula is reversed here. Its geometric smallness argument is an imported result, not our representation-theoretic projector proof.
- [Gaitsgory, *Outline of the proof of the geometric Langlands conjecture for \(GL_2\)*](https://arxiv.org/abs/1302.2506), §§4.1–4.4, especially Proposition 4.4.3, for Ran diagonals, spread representations and the monoidal Satake–Hecke functor.
- [Gaitsgory–Raskin, *Proof of the geometric Langlands conjecture I*](https://arxiv.org/abs/2405.03599), §1.1 and its Hecke-functor remark, for the normalized half gerbe and its usual dual-group representation action.
- [Frenkel, *Lectures on the Langlands program and conformal field theory*](https://arxiv.org/abs/hep-th/0512172), §§3.7–3.8, for the geometric eigencondition and the passage from operators to functors. The direction and normalization used here have been reconciled above.

The [next lesson](geometric-class-field-theory.md) constructs the multiplicative rank-one local system on the Picard scheme and proves its coherent Hecke property. In the present arrow convention its eigenvalue is read along the negative Abel map.
