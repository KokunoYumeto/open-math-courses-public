# Nearby cycles and the two monodromy triangles

Following a sheaf around a punctured complex disc retains information that its stalk at the centre does not see. Nearby cycles record the limit after lifting the punctured disc to its universal cover. Vanishing cycles compare that limit with the sheaf at the centre. Two maps between these constructions measure the failure of monodromy to be the identity.

We construct these maps from one explicit two-term coefficient complex. This fixes their shifts, works with arbitrary weak coefficients, and permits ramification. David B. Massey’s freely accessible [*Notes on Perverse Sheaves and Vanishing Cycles*, version 13, §3, pp. 25–28](https://arxiv.org/pdf/math/9908107v13#page=25), explains the coefficient-complex approach of Kashiwara–Schapira and corrects its punctured trace diagram. Here the construction is developed as a calculation with finite-support sequences: the trace, its kernel, the two-term differential, and the two factorisations of one minus deck transport are checked before they are applied to sheaves. The examples then test ramification, infinite coefficients and the failure of a product–stalk interchange. This separates the elementary coefficient calculation from the sheaf-operation prerequisites used to obtain the cycle functors. The later specialization and microlocal comparisons are separate results; they are not assumed in the construction below.

*Written by GPT-6.1 Sol (OpenAI), Ultra, October 2026. New original text is public domain (CC0).*

## The covering map and the nearby object

Let \(k\) be the course's commutative coefficient ring of finite global dimension. Let \(X\) be a Hausdorff complex manifold, countable at infinity and of uniformly finite dimension and \(f:X\to\mathbb C\) a holomorphic map. Put

\[
Y=f^{-1}(0),\qquad i:Y\hookrightarrow X,\qquad U=X\setminus Y.
\tag{1}
\]

No smoothness of the zero fibre, properness of \(f\), or constructibility of the bounded input \(F\in D^b(k_X)\) is required here. Inverse image \(i^{-1}\) is defined even when \(Y\) is singular.

Use the universal covering

\[
p:\widetilde{\mathbb C^*}=\mathbb C\longrightarrow\mathbb C,
\qquad p(w)=\exp(2\pi\mathrm i w).
\]

Its image is \(\mathbb C^*\). Form the actual cartesian space and its projection

\[
\widetilde U=X\times_{\mathbb C}\widetilde{\mathbb C^*},
\qquad q:\widetilde U\longrightarrow X.
\tag{2}
\]

The map \(q\) is a covering over \(U\), followed by the open inclusion into \(X\). It has no fibre over \(Y\). It is a local homeomorphism, so \(q^!=q^{-1}\) by the local [open-inclusion computation](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/sheaf-proof-readings/src/SH02/exceptional-operations.md#sh02-ex-embedding--open-closed-and-locally-closed-inclusions); both functors are exact. Its proper direct image \(q_!\) is also exact. Indeed the [proper-support fibre formula](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/constructible-duality-and-infinite-twists/src/duality-maps-for-constructible-inverse-and-direct-images.md#the-underived-fibre-formula-proper-image-fibre) identifies its stalk with the direct sum over the discrete fibre, and direct sums of modules preserve exact sequences. These statements do not make its ordinary direct image exact.

Define

\[
\psi_f(F)=i^{-1}Rq_*q^{-1}F.
\tag{3}
\]

The functor depends only on \(F|_U\). It is bounded: the covering space is locally a real manifold of the same finite dimension as \(X\), and the [finite-dimensional sheaf cohomological-dimension bound for ordinary direct image](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/constructible-duality-and-infinite-twists/src/duality-maps-for-constructible-inverse-and-direct-images.md#from-compact-extension-to-ordinary-cohomology-ordinary-cohomology-bound) gives a uniform upper bound on \(Rq_*\) of a bounded complex. The covering remains Hausdorff and countable at infinity, so the hypotheses of that bound apply. Neither compactness of the fibre nor finite-dimensional coefficient stalks is used.

The stalk is not the stalk of \(q^{-1}F\) at a point over \(Y\), since no such point exists. Its cohomology is the filtered colimit of the cohomology of lifted punctured neighborhoods approaching \(Y\).

## The coefficient sheaf uses a sum

Set

\[
L=p_!k_{\widetilde{\mathbb C^*}}.
\tag{4}
\]

At \(a\neq0\), choose one lift and index the other lifts by \(\mathbb Z\). Then

\[
L_a=k^{(\mathbb Z)},\qquad L_0=0.
\tag{5}
\]

The parentheses indicate finite-support sequences. On a small evenly covered open set, \(p_!\) takes the sum of the sheaves on its sheets. Finite support is essential: the trace

\[
\operatorname{tr}:L\longrightarrow k_{\mathbb C}
\tag{6}
\]

adds those finitely many entries. It is the counit of \(p_!\dashv p^{-1}\), extended by zero at the origin. At nonzero points it is surjective; at the origin its source is zero.

[Proper-support base change](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/constructible-duality-and-infinite-twists/src/duality-maps-for-constructible-inverse-and-direct-images.md#pulling-back-a-proper-support-proper-support-base-change) for the square (2) gives \(f^{-1}L=q_!k_{\widetilde U}\). The [internal exceptional adjunction (EX20)](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/sheaf-proof-readings/src/SH02/exceptional-operations.md#sh02-ex-internal--internal-adjunction-and-its-tensor-structure) gives

\[
\begin{split}
R\mathcal Hom_X(f^{-1}L,F)
&\simeq Rq_*R\mathcal Hom_{\widetilde U}(k_{\widetilde U},q^!F)\\
&\simeq Rq_*q^{-1}F.
\end{split}
\tag{7}
\]

We reuse its [actual trace normalization](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/sheaf-proof-readings/src/SH02/exceptional-operations.md#sh02-ex-adjoint--the-derived-adjunction-and-its-normalization), the [finite-dimensional proper-support base-change bridge](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/sheaf-proof-readings/src/SH02/exceptional-operations.md#sh02-ex-basechange-bridge--a-finite-dimensional-base-change-proof), and the [closed-embedding supported-Hom formula](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/sheaf-proof-readings/src/SH02/exceptional-operations.md#sh02-ex-embedding--open-closed-and-locally-closed-inclusions). Their bounded versions suffice: the coefficient object on the covering is a sheaf in degree zero, and \(F\) is bounded. The lower proper-support/topology contracts remain explicit prerequisites. Applying \(i^{-1}\) to (7) gives a second description of (3).

Although (4) uses a sum, Hom from its nonzero stalk uses a product. The sheaf-level internal adjunction (7) computes the comparison without commuting a stalk with an infinite product. It proves no general product–stalk exchange; Exercise 7 shows why such an exchange can fail. One cannot replace (4) by a product sheaf and keep the same trace.

## Deck action and its exact sequence

Fix the action on (5) by

\[
T((a_n)_n)=(a_{n+1})_n,
\qquad d=1-T.
\tag{8}
\]

Changing the chosen lift translates the indices and preserves this action. It commutes with the trace. Precomposition with \(T\) in (7) defines the nearby-cycle monodromy \(M\). This definition fixes the action before any loop is described informally as positive or negative.

On the punctured plane there is an exact sequence

\[
0\longrightarrow L\xrightarrow{\ d\ }L
\xrightarrow{\ \operatorname{tr}\ }k_{\mathbb C^*}\longrightarrow0.
\tag{9}
\]

Here the last sheaf is understood on \(\mathbb C^*\). This distinction is the trace-diagram correction explained by Massey in [§3, p. 28, “The Kashiwara–Schapira approach”](https://arxiv.org/pdf/math/9908107v13#page=28): its extension to the whole plane has target \((j_0)_!k_{\mathbb C^*}\), and the map from that extension to \(k_{\mathbb C}\) is a separate open-inclusion counit. To check exactness, let \(a\) have finite support. If \(d a=0\), then \(a_n=a_{n+1}\) for all \(n\); a finite-support constant sequence is zero. Every \(d a\) has sum zero. Conversely, if \(b\) has finite support and \(\sum_n b_n=0\), set

\[
a_n=\sum_{m\geq n}b_m.
\tag{10}
\]

The total-sum-zero condition makes \(a_n\) zero far to the left, and finite support of \(b\) makes it zero far to the right. Moreover \(a_n-a_{n+1}=b_n\). This proves that the trace kernel is the image of \(d\), over any coefficient ring. The sequence is surjective at its last term by taking a sequence with one nonzero entry.

Let \(j_0:\mathbb C^*\hookrightarrow\mathbb C\). Extending (9) by zero gives its last term \((j_0)_!k_{\mathbb C^*}\). The usual open–closed sequence then produces the exact four-term sequence on the whole plane

\[
0\longrightarrow L\xrightarrow{\ d\ }L
\xrightarrow{\ \operatorname{tr}\ }k_{\mathbb C}
\longrightarrow k_{\{0\}}\longrightarrow0.
\tag{11}
\]

At the origin it is simply \(0\to0\to0\to k\xrightarrow{1}k\to0\). Thus a trace surjective on the punctured plane has the displayed point-supported cokernel on the whole plane. This cokernel is responsible for the exceptional restriction in the second triangle.

## One two-term complex gives two triangles

Use cohomological grading, with \(H^n(A[r])=H^{n+r}(A)\). Define

\[
K=\bigl[L\xrightarrow{\ \operatorname{tr}\ }k_{\mathbb C}\bigr],
\qquad L\text{ in degree }-1,\quad k_{\mathbb C}\text{ in degree }0.
\tag{12}
\]

This is the standard cone of the trace. The deck automorphism acts by \(T\) in degree \(-1\) and by the identity in degree zero. Define the source-normalized vanishing-cycle functor by

\[
\phi_f(F)=i^{-1}R\mathcal Hom_X(f^{-1}K,F).
\tag{13}
\]

The induced precomposition action is again denoted \(M\). These objects are bounded, as also follows from the first triangle below and (3). The convention is important: \(\phi_f\) is shifted by \(-1\) from a convention which defines the vanishing object as the unshifted cone of the restriction-to-nearby map.

There are coefficient chain maps

\[
\begin{array}{ll}
\beta:K\longrightarrow L[1],&\beta^{-1}=1_L,\\
\gamma:L[1]\longrightarrow K,&\gamma^{-1}=d.
\end{array}
\tag{14}
\]

The other components are zero. The equality \(\operatorname{tr}d=0\) makes \(\gamma\) a chain map. The short exact sequence of complexes

\[
0\to k_{\mathbb C}\to K\xrightarrow{\beta}L[1]\to0
\]

gives the first distinguished triangle

\[
k_{\mathbb C}\longrightarrow K\xrightarrow{\beta}L[1]
\longrightarrow k_{\mathbb C}[1].
\tag{15}
\]

The cone of \(\gamma\) is the three-term complex with \(L,L,k_{\mathbb C}\) in degrees \(-2,-1,0\), differentials \(d\) and \(\operatorname{tr}\). By (11), its map to \(k_{\{0\}}\) is a quasi-isomorphism. Hence the second triangle is

\[
L[1]\xrightarrow{\gamma}K\longrightarrow k_{\{0\}}
\longrightarrow L[2].
\tag{16}
\]

Both triangles use actual maps. In particular replacing \(d\) by \(T-1\) would change the normalization of variation.

## Canonical and variation maps

Pull (15) and (16) back by \(f\), apply the contravariant derived internal Hom into \(F\), and restrict to \(Y\). The constant term in (15) gives \(i^{-1}F\). The point term in (16) pulls back to \(k_Y\), and the [closed-support formula (EX15)](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/sheaf-proof-readings/src/SH02/exceptional-operations.md#sh02-ex-embedding--open-closed-and-locally-closed-inclusions) gives

\[
i^{-1}R\mathcal Hom_X(k_Y,F)
=i^{-1}R\Gamma_YF\simeq i^!F.
\tag{17}
\]

We obtain the two natural distinguished triangles

\[
\psi_f(F)[-1]\xrightarrow{\ \operatorname{can}\ }\phi_f(F)
\longrightarrow i^{-1}F\longrightarrow\psi_f(F),
\tag{18}
\]

\[
i^!F\longrightarrow\phi_f(F)
\xrightarrow{\ \operatorname{var}\ }\psi_f(F)[-1]
\longrightarrow i^!F[1].
\tag{19}
\]

The maps are induced by \(\beta\) and \(\gamma\), respectively. A shift \([-1]\) puts a sheaf originally in degree zero in degree one. It is present in both domains or targets above. Ordinary restriction and exceptional restriction are different: neither \(i^!F=i^{-1}F\) nor a deletion of that shift was used.

The coefficient calculation is particularly simple:

\[
\beta\gamma=1-T\quad\text{on }L[1],
\qquad
\gamma\beta=1-T_K\quad\text{on }K.
\tag{20}
\]

For the second equality, both sides have component \(d\) on \(L\) in degree \(-1\) and zero on \(k_{\mathbb C}\) in degree zero. Contravariant Hom reverses composition, so (20) proves

\[
\operatorname{can}\operatorname{var}=1-M
\quad\text{on }\phi_f(F),
\qquad
\operatorname{var}\operatorname{can}=1-M
\quad\text{on }\psi_f(F)[-1].
\tag{21}
\]

After undoing the common shift the second identity is the same identity on nearby cycles. No injectivity, surjectivity or invertibility of either map is asserted. All maps commute with monodromy because the coefficient maps do.

## A disc calculation, including the action direction

Let \(X\) be a small disc, \(f(z)=z\), and \(G\) a local system on its punctured disc. A lifted punctured disc is a half-plane in the covering coordinate. It is contractible. The pulled-back local system is constant there and has no higher cohomology, by the [constant-coefficient homotopy-invariance proof (O1–O2)](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/constructible-duality-and-infinite-twists/src/duality-maps-for-constructible-inverse-and-direct-images.md#homotopy-invariance-from-a-proper-interval-proper-interval-homotopy). Therefore the nearby object is its fibre \(V\), in degree zero. This remains true for infinite modules; there is no finite-dimensional assumption in the half-plane computation.

For clarity, define \(H:V\to V\) to be parallel transport around the counterclockwise loop. Choose a base lift, number its translates by integers, and use the base fibre to identify \(V\). A section on the connected covering, with initial value \(v\), has value \(H^n v\) on sheet \(n\) over that base point. On finite-support sheet generators \(e_n\), (8) gives \(T e_n=e_{n-1}\). Thus precomposition acts on the initial value by

\[
Mv=H^{-1}v.
\tag{22}
\]

This inverse is a consequence of the explicit deck and precomposition conventions. If one starts with the opposite deck action, both the stated action and the corresponding \(1-M\) normalization must change together. The invariant and coinvariant modules are unchanged up to their natural invertible factor.

For a degree-zero sheaf \(F\) locally constant on the punctured disc, let \(S=F_0\). Restriction supplies a map \(c:S\to V\) with invariant image. The first triangle yields

\[
H^0\phi_f(F)=\ker c,
\qquad H^1\phi_f(F)=\operatorname{coker}c,
\qquad H^q\phi_f(F)=0\ (q\ne0,1).
\tag{23}
\]

The two-term representative has \(S\) in degree zero and \(V\) in degree one. Its differential agrees with \(c\) up to the cone/shift sign identification. Formula (23), the coefficient maps (14), and (21) do not depend on changing that identification by a minus sign. We fix canonical and variation maps by (14), rather than silently changing them to match a preferred cone formula.

For the constant sheaf on the whole disc, \(c\) is the identity; nearby cycles are constant and vanishing cycles are zero. For extension by zero of \(G\), \(S=0\), so \(\operatorname{can}:V[-1]\to\phi_f(F)\) is an isomorphism and variation corresponds to \(1-M\). For a sheaf supported at the centre, nearby cycles are zero and vanishing cycles are that sheaf in degree zero.

## Ramification separates vanishing from monodromy

Take \(f(z)=z^m\), \(m\geq1\), and \(F=k_X\) on a disc. Its lifted punctured space has \(m\) connected components, parametrized by

\[
z=\exp\bigl(2\pi\mathrm i(w+r)/m\bigr),
\qquad r\in\mathbb Z/m\mathbb Z.
\]

Each component over a small disc is a half-plane. Hence

\[
\psi_f(k_X)=k^m,
\qquad c:k\longrightarrow k^m,\quad c(a)=(a,\ldots,a).
\tag{24}
\]

Now label the components by the residue of the covering sheet index, rather than the parametrization above. The labels satisfy \(r_{\mathrm{sheet}}=-r_{\mathrm{param}}\) in \(\mathbb Z/m\mathbb Z\). Indeed the lift \(w+r_{\mathrm{param}}\) labels the root while the corresponding sheet residue is its negative. Thus the parametrization-order action \(v_r\mapsto v_{r+1}\) becomes the following sheet-order action. Under (8), monodromy is

\[
M(v)_r=v_{r-1}.
\tag{25}
\]

The diagonal map is split injective over every ring, using any one coordinate projection as a left inverse. Formula (23), now applied to (18) with (24), gives

\[
\phi_f(k_X)\simeq
\bigl(k^m/k(1,\ldots,1)\bigr)[-1].
\tag{26}
\]

Choose the quotient identification induced by canonical in the long cohomology sequence. Then canonical is the quotient map, and variation is

\[
\overline v\longmapsto(1-M)v.
\tag{27}
\]

It is well-defined since \(M\) fixes the diagonal. The two compositions are exactly (21) on the quotient and on \(k^m\). No division by \(m\), semisimplicity or characteristic-zero assumption is needed. For \(m=1\), the quotient is zero. For \(m=2\) over \(\mathbb F_2\), monodromy on the one-dimensional quotient is the identity, while variation is nonzero. Trivial monodromy on vanishing cycles therefore does not imply that they vanish.

This also shows why a later comparison using an inverse image of \(1\) under the normal derivative requires an actual regular defining function. The reduced zero set of \(z^m\) is a smooth point, but its derivative at zero vanishes when \(m>1\); there is then no such normal section. The general constructions (3) and (13) still apply. Smooth-fibre comparisons must retain their derivative hypothesis or the analytic-fibre meaning of smoothness.

## Exercises

In examples asserting a nonzero coefficient object, take the coefficient ring to be nonzero.

### 1. Prove the finite-support difference sequence
*Difficulty: Introductory.*

Over any nonzero ring, prove exactness of \(0\to k^{(\mathbb Z)}\xrightarrow{1-T}k^{(\mathbb Z)}\xrightarrow{\sum}k\to0\). Explain what fails if the two sums are replaced by products.

**Solution.** A finite-support sequence fixed by the shift is constant, hence zero. A difference has total sum zero by cancellation. Conversely for a finite-support \(b\) of total sum zero, formula (10) is finite-support and solves \((1-T)a=b\). A sequence supported at one index maps onto any chosen scalar. These facts prove every part of exactness, without dividing any scalar.

In \(k^{\mathbb Z}\), the shift has nonzero constant sequences in its kernel. An infinite arbitrary sequence has no ring-valued sum defined by the displayed trace. Consequently both injectivity and the definition of the last map fail. The finite-support condition in \(p_!\) is part of the coefficient construction, even though its derived Hom can later produce products.

### 2. Check both coefficient maps before dualizing
*Difficulty: Intermediate.*

Check that \(\gamma\) is a chain map, calculate the cone of \(\gamma\), and prove both identities (20) degree by degree. Explain why contravariance reverses the order of canonical and variation.

**Solution.** The only possible chain obstruction for \(\gamma\) is \(\operatorname{tr}(1-T)\). It is zero because summing a finite-support sequence is invariant under its shift. The cone has \(L\) in degrees \(-2\) and \(-1\), then \(k_{\mathbb C}\) in degree zero; its successive differentials are \(1-T\) and the trace. Sequence (11) shows its cohomology is only \(k_{\{0\}}\) in degree zero. The actual quotient to that point sheaf is thus a quasi-isomorphism.

The composite \(\beta\gamma\) is \(1-T\) on the only nonzero degree of \(L[1]\). The composite \(\gamma\beta\) is \(1-T\) on degree \(-1\) of \(K\), and zero on its degree-zero term. On that term \(T_K\) is the identity, so this is \(1-T_K\) in both degrees. If \(D(A)=i^{-1}R\mathcal Hom(f^{-1}A,F)\), then \(D(ab)=D(b)D(a)\). Thus canonical followed by variation dualizes \(\beta\gamma\), and variation followed by canonical dualizes \(\gamma\beta\), with the end objects exactly as in (21).

### 3. Empty coverings and central support
*Difficulty: Introductory.*

Calculate both functors when \(f\equiv0\), when \(f\) has no zeros, and when \(F=i_*A\) is supported on the zero fibre. Include monodromy and the two triangles.

**Solution.** If \(f\equiv0\), then \(Y=X\), \(\widetilde U=\varnothing\), and \(f^{-1}L=0\). The pulled-back coefficient complex is \(k_X\) in degree zero. Hence \(\psi_f(F)=0\), \(\phi_f(F)=F\), and monodromy on \(\phi\) is the identity. Both \(i^{-1}\) and \(i^!\) are identities. The triangles reduce to \(0\to F\xrightarrow{1}F\to0\) and \(F\xrightarrow{1}F\to0\to F[1]\), up to the specified triangle identifications. Both compositions in (21) are zero, as is \(1-M\).

If \(Y\) is empty, both outputs are sheaves on the empty space and hence zero. If \(F=i_*A\), its covering pullback is zero, so nearby cycles are zero. Triangle (18) gives \(\phi_f(F)\simeq A\); the closed-embedding adjunction gives \(i^!i_*A\simeq A\), so (19) gives the same conclusion. The map from the degree-zero coefficient term identifies the deck action with the identity on \(A\). Thus central support contributes degree-zero vanishing cycles and no nearby cycles, including for singular \(Y\).

### 4. Weak local systems and extension by zero
*Difficulty: Intermediate.*

Let \(G\) on a punctured disc have an arbitrary module fibre \(V\) and invertible counterclockwise transport \(H\). Compute nearby cycles and both maps for \(F=j_!G\). Give an example with \(V\) infinite-dimensional over a field.

**Solution.** Pulling back to the half-plane trivializes the local system, whose ordinary cohomology there is \(V\) in degree zero. Thus \(\psi=V\). The finite-support deck convention and precomposition give \(M=H^{-1}\), by (22). The extension by zero has zero central stalk, so (18) identifies canonical with an isomorphism \(V[-1]\simeq\phi\). Under that identification, (21) makes variation \(1-H^{-1}\). The second triangle consequently identifies the costalk with the fibre of that endomorphism of \(V[-1]\). In particular for \(H=1\) it has cohomology \(V\) in degrees one and two, consistently with supported cohomology of the punctured disc.

For \(V=\bigoplus_{n\geq1}k\) and \(H=1\), the extension by zero is weakly complex constructible on the partition into the punctured disc and its centre. It is not perfect constructible, since its nonzero open stalks are not finite-dimensional over the field. Its nearby cycles are that same infinite vector space, and its vanishing cycles are \(V[-1]\), with canonical invertible and variation zero. The construction and compositions continue to hold for these weak coefficients; a finite-rank assertion was not used.

### 5. A ramified map in characteristic two
*Difficulty: Advanced.*

For \(f(z)=z^2\) and \(k=\mathbb F_2\), compute nearby and vanishing cycles, their monodromies, canonical and variation. Check (21) and explain why an invariant vanishing cycle can have nonzero variation.

**Solution.** Nearby cycles are \(V=k^2\), with \(M(a,b)=(b,a)\). The diagonal \(D=k(1,1)\) is the image of the central stalk. Vanishing cycles are \((V/D)[-1]\), with the quotient one-dimensional. In that quotient the classes of \((1,0)\) and \((0,1)\) agree, so its induced monodromy is the identity. Canonical is the quotient \(q:V\to V/D\) in degree one. Variation sends \(\overline{(a,b)}\) to

\[
(1-M)(a,b)=(a+b,a+b).
\]

This is independent of the diagonal representative and is nonzero: the class of \((1,0)\) maps to \((1,1)\). The composite \(q\operatorname{var}\) is zero because the variation image is diagonal, agreeing with \(1-M=0\) on the quotient. The composite \(\operatorname{var}q\) is the matrix \(\left(\begin{smallmatrix}1&1\\1&1\end{smallmatrix}\right)\), exactly \(1-M\) on \(V\). An invariant quotient class need not be killed by variation; (21) only says that its variation is killed after applying canonical. Here it is a nonzero invariant nearby vector.

### 6. Ordinary and derived extension have different vanishing cycles
*Difficulty: Advanced.*

For the constant sheaf \(k\) on a punctured disc, compare \(j_*k\), \(Rj_*k\), and \(j_!k\). Compute their nearby cycles, vanishing cycles and central cohomology. Why does the first of these have zero vanishing cycles, while the other two do not?

**Solution.** The ordinary direct image \(j_*k\) is the constant sheaf on the whole disc: a small punctured disc is connected, so its degree-zero sections are \(k\). Its central stalk maps isomorphically to \(\psi=k\); (18) therefore gives \(\phi=0\).

For \(Rj_*k\), the punctured-disc cohomology has \(k\) in degrees zero and one and no other degrees. For the circle, apply the [relative-ball localization formula (O12)](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/constructible-duality-and-infinite-twists/src/duality-maps-for-constructible-inverse-and-direct-images.md#constant-coefficients-on-relative-balls-constant-relative-balls) in real dimension two. The closed disc has only degree-zero constant cohomology, and its cohomology relative to the boundary is the coefficient module in degree two. The localization sequence gives the stated two cohomology groups of the circle. Restriction to a point splits off its constant summand, giving the derived decomposition used here. The radial deformation retraction from the punctured disc to the circle preserves constant-coefficient cohomology by (O1–O2). Thus its central derived restriction is \(k\oplus k[-1]\), whereas its nearby object is still \(k\). Its costalk is zero: the [localization triangle (B4)](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/constructible-duality-and-infinite-twists/src/duality-maps-for-constructible-inverse-and-direct-images.md#closed-support-and-its-bound-closed-support-bound) \(R\Gamma_{\{0\}}F\to F\to Rj_*j^{-1}F\) has an isomorphism as its second map when \(F=Rj_*k\). Triangle (19) now gives \(\phi\simeq k[-1]\), with variation an isomorphism. Monodromy is the identity, so canonical is zero by (21).

Finally \(j_!k\) has zero central stalk, nearby cycles \(k\), and vanishing cycles \(k[-1]\); here canonical is an isomorphism and variation is zero. Its costalk has \(k\) in degrees one and two, as in Exercise 4. The difference is the degree-one punctured-link cohomology retained by \(Rj_*\) and the central stalk retained by ordinary \(j_*\). Agreement away from the centre determines nearby cycles but does not determine vanishing cycles.

### 7. An infinite product cannot be moved through a stalk without proof
*Difficulty: Intermediate.*

For \(n\geq1\), let \(V_n\) be the vector space of finite-support rational sequences supported in \(\{n,n+1,\ldots\}\), with the restriction map \(V_n\to V_{n+1}\) deleting the entry at \(n\). Compare \(\operatorname{colim}_{n}V_n\) and \(\operatorname{colim}_{n}\prod_{r\geq1}V_n\). Use this to explain why a countable-cover boundary comparison cannot follow from exchanging products and stalk colimits formally.

**Solution.** Every fixed finite-support sequence becomes zero after sufficiently many deletions. Hence \(\operatorname{colim}_{n}V_n=0\), and \(\prod_r\operatorname{colim}_{n}V_n=0\). In \(\prod_rV_1\), take its \(r\)-th component to be the sequence \(e_r\) supported at index \(r\). At stage \(n\), components with \(r<n\) are zero, but every component with \(r\geq n\) remains nonzero. No finite stage kills the product element. It thus defines a nonzero element in \(\operatorname{colim}_{n}\prod_rV_n\).

The natural map from this latter colimit to the product of the individual colimits is therefore not injective. A stalk is a filtered colimit of sections over neighborhoods, and a covering with countably many sheets can introduce a product in ordinary direct-image cohomology. Their exchange needs additional uniform information, such as a cofinal system of neighborhoods where the whole relevant cohomology restriction has stabilized. The later constructible-specialization proof must establish that information. The formal coefficient triangles above instead rely on the proved internal adjunction (7); no unproved product–colimit exchange enters their construction.

## What remains for the specialization comparison

The general nearby and vanishing objects, their monodromy, both actual coefficient triangles, both cycle triangles and the \(1-M\) identities have been proved relative to the recorded sheaf-operation and finite-dimensional topology contracts. The examples distinguish weak coefficients, ramification, ordinary versus exceptional restrictions, and ordinary versus derived extension. The later comparison with normal specialization and microlocalization, holomorphic test recovery of microsupport, quadratic vanishing cycles and proper direct-image compatibility remain separate teaching targets. The arguments require the proper-support adjunction and base-change formulas, closed-support Hom, and finite-dimensional sheaf cohomological dimension stated above; they do not prove those underlying sheaf-operation and topology theorems.


## Source and prerequisite scope

Massey’s version 13, §3, pp. 25–28, supplies the classical covering construction, monodromy and two triangles; p. 28 explains the coefficient approach of Kashiwara–Schapira and the punctured trace correction. His introductory constructible setting is narrower than the arbitrary bounded coefficients used here. The finite-support sequence calculation and the linked programme proofs of proper-support base change, internal adjunction, ordinary cohomological bounds and closed support establish the scope used in this lesson. The cone convention here is the shifted convention described on p. 28. Mathematical methods and formulas retain their source credit; the exposition and seven solutions are independently written programme text under CC0. This lesson does not prove the separate specialization comparison or certify every transitive prerequisite of its linked proofs.
