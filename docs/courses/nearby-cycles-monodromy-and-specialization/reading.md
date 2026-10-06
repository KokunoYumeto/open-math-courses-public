# Nearby cycles, monodromy and specialization

Six lessons construct nearby and vanishing cycles, fix monodromy and variation signs, prove proper-on-support pushforward compatibility, compare normal and conormal sections, compute quadratic tests, and identify vanishing cycles with positive real support. Forty-one exercises have complete solutions.

- [Nearby cycles and the two monodromy triangles](nearby-cycles-and-the-two-monodromy-triangles.html) · [editable source](src/nearby-cycles-and-the-two-monodromy-triangles.md)
- [Proper pushforwards of nearby and vanishing cycles](proper-pushforwards-of-nearby-and-vanishing-cycles.html) · [editable source](src/proper-pushforwards-of-nearby-and-vanishing-cycles.md)
- [Nearby cycles through the normal deformation](nearby-cycles-through-the-normal-deformation.html) · [editable source](src/nearby-cycles-through-the-normal-deformation.md)
- [Complex nearby cycles as normal and conormal sections](complex-nearby-cycles-as-normal-and-conormal-sections.html) · [editable source](src/complex-nearby-cycles-as-normal-and-conormal-sections.md)
- [Quadratic cycles and the holomorphic microsupport test](quadratic-cycles-and-the-holomorphic-microsupport-test.html) · [editable source](src/quadratic-cycles-and-the-holomorphic-microsupport-test.md)
- [Vanishing cycles as positive real support](vanishing-cycles-as-positive-real-support.html) · [editable source](src/vanishing-cycles-as-positive-real-support.md)

## A route through the calculations

Use the finite-support sequence and ramification examples to fix signs first. Follow the support carrier through pushforward, then compare the cover with normal deformation. The slit and polar computations lead to conormal sections; the covered quadratic ball supplies the degree needed for holomorphic detection. Positive real support gives a second geometric description and its own counterexample outside the complex setting.

The [source and proof guide](source-and-proof-guide.html) identifies the exact human passages checked and the programme prerequisites still required. In particular, a comparison merely stated by reference in a free paper is not counted as a supplied proof.

The proofs retain their stated finite-dimensional topology, sheaf-operation, weak constructibility, small-ball stabilization, analytic normal-cone, Fourier and microlocal coefficient-model prerequisites. Weak-coefficient arguments permit arbitrary bounded modules; the perfect subcategory is specified separately.

Download the readings, editable sources and build code · [Reuse terms](LICENSE.txt) · Provenance


# Nearby cycles and the two monodromy triangles

Following a sheaf around a punctured complex disc retains information that its stalk at the centre does not see. Nearby cycles record the limit after lifting the punctured disc to its universal cover. Vanishing cycles compare that limit with the sheaf at the centre. Two maps between these constructions measure the failure of monodromy to be the identity.

We construct these maps from one explicit two-term coefficient complex. This fixes their shifts, works with arbitrary weak coefficients, and permits ramification. David B. Massey’s freely accessible [*Notes on Perverse Sheaves and Vanishing Cycles*, version 13, §3](https://arxiv.org/html/math/9908107v13#p301), explains the coefficient-complex approach of Kashiwara–Schapira and corrects its punctured trace diagram. Here the construction is developed as a calculation with finite-support sequences: the trace, its kernel, the two-term differential, and the two factorisations of one minus deck transport are checked before they are applied to sheaves. The examples then test ramification, infinite coefficients and the failure of a product–stalk interchange. This separates the elementary coefficient calculation from the sheaf-operation prerequisites used to obtain the cycle functors. The later specialization and microlocal comparisons are separate results; they are not assumed in the construction below.

*Written by GPT-6.1 Sol (OpenAI), Ultra, October 2026. New original text is public domain (CC0).*

## The covering map and the nearby object

Let \(k\) be the course's commutative coefficient ring of finite global dimension. Let \(X\) be a finite-dimensional complex manifold and \(f:X\to\mathbb C\) a holomorphic map. Put

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

The map \(q\) is a covering over \(U\), followed by the open inclusion into \(X\). It has no fibre over \(Y\). It is a local homeomorphism, so \(q^!=q^{-1}\); both functors are exact. Its proper direct image \(q_!\) is also exact. Indeed its stalk is the direct sum over the discrete fibre, and direct sums of modules preserve exact sequences. These statements do not make its ordinary direct image exact.

Define

\[
\psi_f(F)=i^{-1}Rq_*q^{-1}F.
\tag{3}
\]

The functor depends only on \(F|_U\). It is bounded: the covering space is locally a real manifold of the same finite dimension as \(X\), and the finite-dimensional sheaf cohomological-dimension bound for ordinary direct image gives a uniform upper bound on \(Rq_*\) of a bounded complex. This is the existing finite-dimensional topology contract. Neither compactness of the fibre nor finite-dimensional coefficient stalks is used.

The stalk is not the stalk of \(q^{-1}F\) at a point over \(Y\), since no such point exists. It is the limit of the cohomology of the lifted punctured neighborhoods approaching \(Y\).

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

Proper-support base change for the square (2) gives \(f^{-1}L=q_!k_{\widetilde U}\). The already constructed internal exceptional adjunction gives

\[
\begin{split}
R\mathcal Hom_X(f^{-1}L,F)
&\simeq Rq_*R\mathcal Hom_{\widetilde U}(k_{\widetilde U},q^!F)\\
&\simeq Rq_*q^{-1}F.
\end{split}
\tag{7}
\]

We reuse its actual trace normalization, the finite-dimensional proper-support base-change bridge, and the closed-embedding supported-Hom formula. Their bounded versions suffice: the coefficient object on the covering is a sheaf in degree zero, and \(F\) is bounded. The lower proper-support/topology contracts remain explicit prerequisites. Applying \(i^{-1}\) to (7) gives a second description of (3).

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

Here the last sheaf is understood on \(\mathbb C^*\). This distinction is the trace-diagram correction explained by Massey in §3: its extension to the whole plane has target \((j_0)_!k_{\mathbb C^*}\), and the map from that extension to \(k_{\mathbb C}\) is a separate open-inclusion counit. To check exactness, let \(a\) have finite support. If \(d a=0\), then \(a_n=a_{n+1}\) for all \(n\); a finite-support constant sequence is zero. Every \(d a\) has sum zero. Conversely, if \(b\) has finite support and \(\sum_n b_n=0\), set

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

At the origin it is simply \(0\to0\to0\to k\xrightarrow{1}k\to0\). Thus a trace surjective on the punctured plane has a nonzero cokernel on the whole plane. This cokernel is responsible for the exceptional restriction in the second triangle.

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

Pull (15) and (16) back by \(f\), apply the contravariant derived internal Hom into \(F\), and restrict to \(Y\). The constant term in (15) gives \(i^{-1}F\). The point term in (16) pulls back to \(k_Y\), and the closed-support formula gives

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

Let \(X\) be a small disc, \(f(z)=z\), and \(G\) a local system on its punctured disc. A lifted punctured disc is a half-plane in the covering coordinate. It is contractible. The pulled-back local system is constant there and has no higher cohomology, by the constant-sheaf contractible-manifold cohomology contract. Therefore the nearby object is its fibre \(V\), in degree zero. This remains true for infinite modules; there is no finite-dimensional assumption in the half-plane computation.

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

For \(Rj_*k\), the punctured-disc cohomology has \(k\) in degrees zero and one and no other degrees. This follows from its circle deformation retract and the cellular cochain complex with zero differential for constant coefficients. Thus its central derived restriction is \(k\oplus k[-1]\), whereas its nearby object is still \(k\). Its costalk is zero: the localization triangle \(R\Gamma_{\{0\}}F\to F\to Rj_*j^{-1}F\) has an isomorphism as its second map when \(F=Rj_*k\). Triangle (19) now gives \(\phi\simeq k[-1]\), with variation an isomorphism. Monodromy is the identity, so canonical is zero by (21).

Finally \(j_!k\) has zero central stalk, nearby cycles \(k\), and vanishing cycles \(k[-1]\); here canonical is an isomorphism and variation is zero. Its costalk has \(k\) in degrees one and two, as in Exercise 4. The difference is the degree-one punctured-link cohomology retained by \(Rj_*\) and the central stalk retained by ordinary \(j_*\). Agreement away from the centre determines nearby cycles but does not determine vanishing cycles.

### 7. An infinite product cannot be moved through a stalk without proof
*Difficulty: Intermediate.*

For \(n\geq1\), let \(V_n\) be the vector space of finite-support rational sequences supported in \(\{n,n+1,\ldots\}\), with the restriction map \(V_n\to V_{n+1}\) deleting the entry at \(n\). Compare \(\operatorname{colim}_{n}V_n\) and \(\operatorname{colim}_{n}\prod_{r\geq1}V_n\). Use this to explain why a countable-cover boundary comparison cannot follow from exchanging products and stalk limits formally.

**Solution.** Every fixed finite-support sequence becomes zero after sufficiently many deletions. Hence \(\operatorname{colim}_{n}V_n=0\), and \(\prod_r\operatorname{colim}_{n}V_n=0\). In \(\prod_rV_1\), take its \(r\)-th component to be the sequence \(e_r\) supported at index \(r\). At stage \(n\), components with \(r<n\) are zero, but every component with \(r\geq n\) remains nonzero. No finite stage kills the product element. It thus defines a nonzero element in \(\operatorname{colim}_{n}\prod_rV_n\).

The natural map from this latter limit to the product of the individual limits is therefore not injective. A stalk is a filtered limit of neighborhoods, and a covering with countably many sheets can introduce a product in ordinary direct-image cohomology. Their exchange needs additional uniform information, such as a cofinal system of neighborhoods where the whole relevant cohomology restriction has stabilized. The later constructible-specialization proof must establish that information. The formal coefficient triangles above instead rely on the proved internal adjunction (7); no unproved product–limit exchange enters their construction.

## What remains for the specialization comparison

The general nearby and vanishing objects, their monodromy, both actual coefficient triangles, both cycle triangles and the \(1-M\) identities have been proved relative to the recorded sheaf-operation and finite-dimensional topology contracts. The examples distinguish weak coefficients, ramification, ordinary versus exceptional restrictions, and ordinary versus derived extension. The later comparison with normal specialization and microlocalization, holomorphic test recovery of microsupport, quadratic vanishing cycles and proper direct-image compatibility remain separate teaching targets. The arguments require the proper-support adjunction and base-change formulas, closed-support Hom, and finite-dimensional sheaf cohomological dimension stated above; they do not prove those underlying sheaf-operation and topology theorems.


# Proper pushforwards of nearby and vanishing cycles

A map need not be proper on its entire source for its pushforward to commute with nearby and vanishing cycles. Properness on the sheaf's support suffices. The proof must keep this support after passing to the covering or to coefficient Hom; otherwise a later base-change step can silently lose its hypothesis.

We prove the two comparisons with their actual natural maps, monodromy, and both canonical/variation triangles. We then apply them to the graph of an arbitrary holomorphic function. The proper-map comparison is stated in David B. Massey’s freely accessible [*Notes on Perverse Sheaves and Vanishing Cycles*, version 13, §3](https://arxiv.org/html/math/9908107v13#p370). Massey states the comparison for proper maps with his constructible coefficients. The stronger proper-on-closed-support assertion below is established relative to the stated ordinary adjunction and proper-support base-change theorems. Its proof follows the support carrier through each operation, identifies the comparison map, and checks its compatibility with the two coefficient triangles. Those additional steps and the broader coefficient scope are not supplied by the cited statement.

*Written by GPT-6.1 Sol (OpenAI), Ultra, October 2026. New original text is public domain (CC0).*

## Maps and zero fibres

Let \(g:Z\to X\) be holomorphic between finite-dimensional complex manifolds, and let \(h:X\to\mathbb C\) be holomorphic. Set

\[
Y_X=h^{-1}(0),\quad Y_Z=(h\circ g)^{-1}(0),
\quad i_X:Y_X\hookrightarrow X,\quad i_Z:Y_Z\hookrightarrow Z.
\]

The induced map \(g_0:Y_Z\to Y_X\) gives the cartesian square

\[
\begin{array}{ccc}
Y_Z&\xrightarrow{g_0}&Y_X\\
\scriptstyle i_Z\downarrow&&\downarrow\scriptstyle i_X\\
Z&\xrightarrow{g}&X.
\end{array}
\tag{1}
\]

Neither zero fibre is required to be smooth. All inverse images and direct images on them are sheaf operations on their underlying locally compact spaces.

Let \(F\in D^b(k_Z)\), with the same finite-global-dimension commutative ring as before. Assume \(g\) is proper on a closed support carrier \(S\) of \(F\). Thus \(F|_{Z\setminus S}=0\), and \(g|_S:S\to X\) is proper. This is the hypothesis used at every base-change step below; it permits arbitrary behaviour of \(g\) away from the support. The formal comparisons below require no constructibility of \(F\). In particular they apply to its stated weakly complex-constructible inputs, including infinite coefficient modules.

Use the coefficient sheaf \(L\), complex \(K\), deck action \(T\), and maps \(\beta,\gamma\) constructed in [Nearby cycles and the two monodromy triangles](nearby-cycles-and-the-two-monodromy-triangles.html). On \(X\) the coefficients are \(h^{-1}L,h^{-1}K\), and on \(Z\) they are \((h\circ g)^{-1}L,(h\circ g)^{-1}K\). Their inverse-image identification is exact.

## Internal Hom preserves the support carrier

For an ambient coefficient complex \(A\), put

\[
H_A(F)=R\mathcal Hom_Z(g^{-1}A,F).
\tag{2}
\]

Its restriction to \(Z\setminus S\) is zero: restriction of derived internal Hom to an open set is internal Hom of the restrictions, and the second restriction is zero. Thus \(S\) is a support carrier for \(H_A(F)\), even if \(A\) has infinite-rank stalks or is supported everywhere. This uses the support of the second Hom argument, not a claim that its first argument is perfect.

There is a canonical ordinary inverse/direct internal adjunction

\[
Rg_*H_A(F)\simeq R\mathcal Hom_X(A,Rg_*F).
\tag{3}
\]

Here is its application proof, using the existing derived ordinary adjunction. Test the left object against a variable \(E\) in the ordinary derived category:

\[
\begin{split}
\operatorname{Hom}(E,Rg_*R\mathcal Hom(g^{-1}A,F))
&\simeq\operatorname{Hom}(g^{-1}E,R\mathcal Hom(g^{-1}A,F))\\
&\simeq\operatorname{Hom}(g^{-1}E\otimes^L g^{-1}A,F)\\
&\simeq\operatorname{Hom}(g^{-1}(E\otimes^L A),F)\\
&\simeq\operatorname{Hom}(E\otimes^L A,Rg_*F)\\
&\simeq\operatorname{Hom}(E,R\mathcal Hom(A,Rg_*F)).
\end{split}
\tag{4}
\]

Exact inverse image for constant coefficients commutes with derived tensor: its stalks pull back the same flat resolutions. Yoneda gives (3). The isomorphism is natural in \(A,F\); applying the same argument on open subsets gives the internal-Hom and restriction compatibilities. For the bounded objects used here, ordinary derived adjunction has the following direct construction. The inverse-image presheaf and sheafification give the usual sheaf adjunction. Inverse image is exact because its stalk at a source point is the original stalk at its image. Its right adjoint therefore preserves injective sheaves: applying the Hom test for injectivity reduces to this exact inverse image. Resolve the second argument by a bounded-below complex of injectives and apply the sheaf adjunction degree by degree. The resulting isomorphism of Hom complexes computes the derived morphisms, since a bounded-below injective complex is homotopically injective. It is compatible with restriction and with the unit and counit inherited from sheaves. This is the ordinary part (A8) of Duality maps for constructible inverse and direct images. The existence of injective resolutions, their computation of derived morphisms, and the tensor–Hom adjunction used in (4) remain explicit algebraic prerequisites; the finite-dimensional bound below puts the resulting objects in the bounded category.

For the particular \(A=h^{-1}L\), formula (7) of the preceding lesson identifies \(H_A(F)\) with the ordinary direct image from the pulled-back covering. Its boundedness follows from finite manifold cohomological dimension. For \(A=h^{-1}K\), its coefficient triangle then gives boundedness from this covering object and \(F\). The constant and zero-fibre coefficient terms are bounded for the same reason. Thus every proper-support operation used below is on a bounded input. No unfinished unbounded proper-direct-image extension is used.

## Ordinary base change is invertible on these supports

For every bounded object \(B\) supported on \(S\), forgetting support gives an isomorphism

\[
Rg_!B\xrightarrow{\sim}Rg_*B.
\tag{5}
\]

Indeed the closed-embedding factorization \(B\simeq (a_S)_*(B|_S)\) reduces the map to proper direct image along \(g|_S\). The finite-dimensional proper-support and proper-map comparisons supply this assertion. After the base change (1), \(g_0\) is proper on \(S_0=S\cap Y_Z\), so the same assertion applies to \(i_Z^{-1}B\).

Combine (5) with the existing arbitrary proper-support base-change bridge:

\[
\begin{split}
i_X^{-1}Rg_*B
&\simeq i_X^{-1}Rg_!B\\
&\simeq R(g_0)_!i_Z^{-1}B\\
&\simeq R(g_0)_*i_Z^{-1}B.
\end{split}
\tag{6}
\]

The natural transformation is the ordinary base-change map. The support-forgetting compatibility for proper-support base change states that pulling back a properly supported section and forgetting its support agrees with first forgetting support and then applying ordinary base change. Consequently (6) establishes invertibility of the actual ordinary comparison, not merely the existence of an isomorphism with its target. The underlying soft, fibre, composition and topology primitives remain open imported proofs.

Formula (2) showed why the same properness applies after coefficient Hom. Applying (6) to \(H_A(F)\) and then (3) gives

\[
i_X^{-1}R\mathcal Hom_X(A,Rg_*F)
\simeq R(g_0)_*\,i_Z^{-1}R\mathcal Hom_Z(g^{-1}A,F).
\tag{7}
\]

Everything is natural in the coefficient argument \(A\).

## Both cycle comparisons and both triangles

Take \(A=h^{-1}L\) in (7) and use the coefficient description of nearby cycles. Take \(A=h^{-1}K\) for vanishing cycles. We obtain

\[
\psi_h(Rg_*F)\simeq R(g_0)_*\psi_{h\circ g}(F),
\qquad
\phi_h(Rg_*F)\simeq R(g_0)_*\phi_{h\circ g}(F).
\tag{8}
\]

The spaces of both sides are \(Y_X\). No extra dimension shift or orientation line appears: these are ordinary direct images and ordinary restrictions of the same coefficient Hom functors. In particular the source-normalized \([-1]\) in the two monodromy triangles stays unchanged.

For \(A=k_X\), formula (7) gives the ordinary restriction comparison

\[
i_X^{-1}Rg_*F\simeq R(g_0)_*i_Z^{-1}F.
\tag{9}
\]

For \(A=k_{Y_X}\), its inverse image is \(k_{Y_Z}\); the supported-Hom formula gives

\[
i_X^!Rg_*F\simeq R(g_0)_*i_Z^!F.
\tag{10}
\]

This proves the exceptional comparison directly from the same supported coefficient argument. It does not identify exceptional and ordinary restrictions.

The two coefficient triangles involve precisely \(k_X,h^{-1}K,h^{-1}L[1]\) and \(h^{-1}L[1],h^{-1}K,k_{Y_X}\). Since (7) is natural for every map among these coefficients, it commutes with their actual \(\beta,\gamma\) and quotient maps. Thus applying \(R(g_0)_*\) to either source monodromy triangle gives the corresponding target triangle under (8)–(10), including its canonical and variation maps. Naturality for \(T\) identifies the two monodromies. Both \(1-M\) composition identities are preserved. We did not choose an arbitrary isomorphism between two cone objects to conclude this compatibility.

## The covering proof has the same support condition

The nearby comparison can also be followed through its original covering definition. Form the cartesian map

\[
\widetilde g:\widetilde U_Z\longrightarrow\widetilde U_X,
\qquad q_X\widetilde g=gq_Z.
\]

The map \(\widetilde g\) is proper on \(q_Z^{-1}S\), the base change of the carrier. The ordinary base-change map

\[
q_X^{-1}Rg_*F\longrightarrow R\widetilde g_*q_Z^{-1}F
\tag{11}
\]

is invertible by the same proper-support/ordinary compatibility as (6). Composition of ordinary direct images gives

\[
Rq_{X*}q_X^{-1}Rg_*F
\simeq Rg_*Rq_{Z*}q_Z^{-1}F.
\tag{12}
\]

The last covering direct image is still supported on \(S\): an open set outside the closed carrier pulls back to a set where the sheaf vanishes. Therefore ordinary base change to the zero fibre is again legitimate. Restricting (12) recovers the first comparison in (8). This explains both appearances of support properness in a covering proof. Merely asserting that the covering map is proper would be incorrect; it has infinitely many sheets and no fibre at zero.

## The graph construction has a zero-extension term

For an arbitrary holomorphic \(f:Z\to\mathbb C\), let

\[
\Gamma_f:Z\longrightarrow\mathbb C\times Z,
\quad z\longmapsto(f(z),z),
\qquad t:\mathbb C\times Z\to\mathbb C.
\]

The graph is a closed embedding and hence proper. The ambient zero fibre is \(\{0\}\times Z\simeq Z\), while the original zero fibre is \(Y=f^{-1}(0)\). The induced zero-fibre graph map is the closed inclusion \(a:Y\hookrightarrow Z\). Formula (8) reads, as sheaves on that ambient \(Z\),

\[
\psi_t((\Gamma_f)_*F)\simeq a_*\psi_f(F),
\qquad
\phi_t((\Gamma_f)_*F)\simeq a_*\phi_f(F).
\tag{13}
\]

All these closed direct images are exact. Restriction to \(Y\) recovers the original cycle objects. The explicit \(a_*\) records their support and types; the two zero fibres are not silently the same space. This permits a comparison for arbitrary \(f\) to use the regular projection \(t\) in a graph ambient space, without pretending that \(df\) was nonzero on its original zero fibre. The normal-specialization and microlocalization identifications for that projection remain separate proofs.

## Exercises

### 1. Proper only on a section
*Difficulty: Intermediate.*

Let \(g:\mathbb C^2\to\mathbb C\) be \(g(x,y)=x\), let \(S=\{y=0\}\), and let \(F=k_S\). Put \(h(x)=x^2\). Verify the support hypothesis, compute \(Rg_*F\), and compute both sides of (8) at zero.

**Solution.** The whole projection is not proper, since its fibres are complex lines. Its restriction to the closed section \(S\) is an isomorphism, hence proper. The closed-supported constant sheaf therefore has \(Rg_*F=k_{\mathbb C}\) with no higher cohomology. On the source support the function is also \(x^2\). Its pulled-back punctured section has two contractible lifted components, giving nearby cycles \(k^2\), supported at the single source point \((0,0)\). Its vanishing object is \((k^2/k(1,1))[-1]\).

The map \(g_0\) sends the whole source zero fibre \(\{x=0\}\) to a point, but it is proper on the support of either cycle object, the one point \((0,0)\). Its pushforward leaves the displayed modules unchanged. The target constant sheaf with \(h=x^2\) has exactly those nearby and vanishing objects by the ramification calculation. This checks (8) for a genuinely nonproper whole-source map while retaining properness at every relevant supported stage.

### 2. A finite ramified pushforward
*Difficulty: Intermediate.*

Let \(m\) be a positive integer. Take \(g(z)=z^m\) on \(\mathbb C\), \(h(x)=x\), and \(F=k_{\mathbb C}\). Describe \(Rg_*F\) at and away from zero. Compute its cycles for \(h\), and identify the maps with the cycles for \(h\circ g\).

**Solution.** The finite map is proper. Away from zero it is an \(m\)-sheet covering, so the pushforward is a local system with fibre \(k^m\); looping permutes its sheets. At zero, the inverse image of a small disc is a disc, with constant cohomology \(k\) in degree zero and no higher terms. Thus \(Rg_*F\) is an ordinary sheaf with central stalk \(k\), generic module \(k^m\), and diagonal restriction map. There are no positive-degree direct-image cohomology sheaves, by the same local calculation everywhere.

Its nearby object for \(h\) is \(k^m\) and its vanishing object is \((k^m/k(1,\ldots,1))[-1]\). These are precisely the cycles of \(z^m\) on the source constant sheaf. The zero-fibre map is the identity of a point. Under the common sheet convention, monodromy is the same cyclic action, canonical is the quotient, and variation is the map induced by \(1-M\). This works over every allowed ring, including when its characteristic divides \(m\).

### 3. Remove support properness
*Difficulty: Advanced.*

Let \(g:\mathbb C^*\hookrightarrow\mathbb C\) be the open inclusion, \(h(x)=x\), and \(F=k_{\mathbb C^*}\). Calculate both sides of each comparison in (8). Does weak complex constructibility rescue the comparisons?

**Solution.** The source function \(h\circ g\) has empty zero fibre. Both source cycle objects are therefore zero, and the right sides of (8) are zero. On the target, \(Rg_*F=Rj_*k\). Its restriction to the punctured disc is constant, so its nearby cycles are \(k\), in degree zero. Its costalk at zero is zero by localization, while its central derived restriction has \(k\) in degrees zero and one. The second monodromy triangle therefore gives vanishing cycles \(k[-1]\). Both left sides are nonzero for a nonzero coefficient ring.

The sheaf on the source is perfect complex constructible, and the target direct image has finite complex-constructible cohomology on the punctured-disc/centre partition. Thus even this stronger coefficient property does not rescue either comparison. The inclusion is not proper on the support: sequences approaching zero escape the source over a compact neighborhood of zero. This is exactly the hypothesis missing from the theorem.

### 4. Type the graph comparison
*Difficulty: Introductory.*

For a possibly singular zero fibre \(Y=f^{-1}(0)\), identify the spaces carrying each term in (13). Prove that restriction gives the original cycles, and explain why the ambient regular projection does not force \(df\neq0\).

**Solution.** The function \(t\) is defined on \(\mathbb C\times Z\), with zero fibre \(\{0\}\times Z\), identified with \(Z\). Thus its two cycle objects on the left of (13) live on \(Z\). The function \(f\) is defined on \(Z\), so its cycles on the right before applying \(a_*\) live on \(Y\). The zero-fibre graph map is \(a:Y\hookrightarrow Z\); its exact closed pushforward puts those cycles on \(Z\), supported on \(Y\). Closed restriction satisfies \(a^{-1}a_*\simeq\mathrm{id}\), giving the original objects on \(Y\).

The derivative of \(t\) in the ambient first coordinate is nonzero everywhere. The derivative of its restriction to the graph is \(df\), which can vanish. A regular ambient projection and a ramified or critical restricted function are compatible. For \(f(z)=z^2\) the graph proof applies even though \(df(0)=0\), and its nonzero vanishing cycles are extended from the one-point original zero fibre into the ambient zero fibre.

### 5. Check the exceptional triangle at a branch point
*Difficulty: Advanced.*

For the finite map in Exercise 2, prove that the costalk of \(Rg_*k_{\mathbb C}\) at zero is \(k[-2]\). Check this directly from its variation triangle, without dividing by \(m\).

**Solution.** Formula (10) gives the pushforward of the source constant-sheaf point costalk. On the complex line the real orientation is canonical and the point has real codimension two, so that costalk is \(k[-2]\). The zero-fibre map is the identity, giving the asserted object.

For the direct check, put \(V=k^m\), \(D=k(1,\ldots,1)\) and \(Q=V/D\). Variation is \(r:Q\to V\), \(r(\overline v)=(1-M)v\), in degree one. The kernel of \(1-M\) on \(V\) is exactly \(D\), by equality of every cyclic coordinate. Thus \(r\) is injective. Its image is the kernel of the summation \(V\to k\): one inclusion follows by telescoping, and the reverse inclusion is solved by successive cyclic differences, whose consistency is exactly the zero-sum condition. Summation is surjective by one coordinate, so its cokernel is \(k\). The fibre of \(Q[-1]\xrightarrow{r}V[-1]\) has only degree-two cohomology \(k\), namely \(k[-2]\), as required. This proof includes characteristic dividing \(m\); in characteristic two at \(m=2\), the variation image is the diagonal but remains an injective image of \(Q\).

### 6. Infinite coefficients do not require a perfect Hom factor
*Difficulty: Intermediate.*

Over a field let \(V=\bigoplus_{r\geq1}k\), and replace the source constant sheaf in Exercise 2 by \(V_{\mathbb C}\). Calculate the cycle objects and explain which part of the comparison proof permits these nonperfect coefficients.

**Solution.** Each small lifted component is contractible, with constant cohomology \(V\) in degree zero. The nearby object is \(V^m\), and the central restriction is the diagonal \(V\to V^m\). Vanishing cycles are \((V^m/\operatorname{diag}V)[-1]\), and monodromy permutes the finitely many components. Canonical and variation are again the quotient and the induced \(1-M\). The diagonal splits by any coordinate projection, so the quotient is isomorphic to \(V^{m-1}\), without a finite-dimensional assumption.

The sheaf is weakly complex constructible and is not perfect, because its stalks are infinite-dimensional. Formula (4) uses ordinary adjunction and derived tensor–Hom adjunction, neither of which demands a perfect first Hom argument. Formula (2) keeps the support carrier using the second argument, regardless of its rank. Properness belongs to the finite map and its carrier. These are exactly the ingredients permitting the weak example; no finite-dimensional dual-tensor identification or perfect projection-formula assertion is substituted.

## What has been established

Both proper-on-support cycle comparisons, both monodromy-triangle comparisons, and the typed graph construction are proved for bounded inputs, with singular zero fibres and arbitrary weak coefficients allowed. The finite-dimensional proper-support, ordinary adjunction and topology primitives remain the exact imported foundations. Normal-specialization/microlocal comparisons, cycle constructibility in full generality, the holomorphic microsupport test criterion and the quadratic model remain separate results. This lesson uses the sheaf-operation and topology prerequisites specified above; it does not prove their full foundational theory.


# Nearby cycles through the normal deformation

Normal specialization follows a sheaf toward a submanifold along positive real scales. Nearby cycles follow a complex function after lifting its nonzero values to the universal cover. For a regular zero fibre these two limits agree, including for weak real-constructible sheaves. The key boundary comparison involves a countable covering. We prove its actual map using a common cofinal system of neighborhoods, rather than exchanging an infinite product with a stalk limit formally.

We retain the regular defining-function hypothesis required by the normal section. The positive-chamber specialization construction is described in the freely accessible [Fernandes–Kudomi–Takeuchi, *Characteristic cycles of real and complex constructible sheaves, revisited*, version 2, §2.4](https://arxiv.org/html/2603.14821v2#S2.SS4). Their equation (4.54) also identifies this construction with real nearby cycles of the deformation parameter. These passages specify the positive-chamber construction; they do not prove the weak real-coefficient complex-cover comparison needed here. Our route first isolates the countable-cover boundary map, checks the common shrinking neighborhoods it requires, then uses the logarithmic lift to compare the deformation with the cover. The gluing argument records the dependence on a lift of one. Its small-ball, base-change and conic-recovery inputs are stated at the points of use and remain separate prerequisite theorems. Complex-conic section and microlocalization formulas are subsequent results.

*Written by GPT-6.1 Sol (OpenAI), Ultra, October 2026. New original text is public domain (CC0).*

## The normal function and the hypothesis it needs

Let \(X\) be a finite-dimensional complex manifold, \(k\) a commutative ring of finite global dimension, and \(F\in D^b_{w\text{-}\mathbb R\text{-}c}(k_X)\). Let \(f:X\to\mathbb C\) be holomorphic, with

\[
Y=f^{-1}(0),\qquad i:Y\hookrightarrow X,
\qquad df_y\neq0\quad(y\in Y).
\tag{1}
\]

The condition makes the analytic fibre regular. Its complex normal bundle \(E=T_YX\) has a canonical fibrewise linear function

\[
\ell:E\longrightarrow\mathbb C,\qquad
\ell_y([v])=df_y(v).
\tag{2}
\]

Since \(df\) vanishes on \(T_yY\), this is well-defined. Since the normal line is one-dimensional and the derivative is nonzero, it identifies \(E\) with \(\mathbb C\times Y\). Write \(e:Y\hookrightarrow E\) for the zero section, \(\tau:E\to Y\) for the projection, \(E^*=E\setminus e(Y)\), and \(\tau^\circ:E^*\to Y\). The derivative determines the normal section

\[
s(y)=\ell_y^{-1}(1).
\tag{3}
\]

This section does not exist for a ramified defining function whose reduced zero set happens to be smooth. For example \(f(z)=z^2\) has \(df_0=0\). General cycles of a critical function still have the proper graph construction in the preceding lesson.

We will prove, with the cycle convention fixed in the first lesson,

\[
\psi_f(F)\simeq\psi_\ell(\nu_YF),
\qquad
\phi_f(F)\simeq\phi_\ell(\nu_YF).
\tag{4}
\]

Both sides live on \(Y\). A lift of \(1\) in the universal cover fixes its coordinate convention. No finite-generation, perfect-stalk or complex-constructibility assumption is made.

## Small neighborhoods control a countable cover

We first prove the boundary lemma needed in the deformation. Let \(M\) be a real analytic manifold, \(b:N\hookrightarrow M\) a closed analytic submanifold, and \(\pi:\widehat M\to M\) a covering whose fibres have a fixed countable index set locally. Let \(\pi_0:\widehat N\to N\) be its base change. For \(G\in D^b_{w\text{-}\mathbb R\text{-}c}(k_M)\), the ordinary base-change morphism

\[
b^{-1}R\pi_*\pi^{-1}G
\longrightarrow R\pi_{0*}\pi_0^{-1}b^{-1}G
\tag{5}
\]

is an isomorphism.

Fix \(x\in N\). Choose an analytic coordinate ball centred at \(x\), with \(N\) a coordinate plane, small enough to trivialize the covering. The weak inverse-image theorem makes \(b^{-1}G\) weakly constructible. The local small-ball theorem proved in the small-ball stabilization theorem stated in (6), with its compact chart cutoff, gives a cofinal family of sufficiently small balls \(B_\epsilon\) for which the actual maps

\[
R\Gamma(B_\epsilon;G)\longrightarrow G_x,
\qquad
R\Gamma(B_\epsilon\cap N;b^{-1}G)\longrightarrow G_x
\tag{6}
\]

are isomorphisms. Both assertions hold for every sufficiently small radius, so one family works for both. The restriction between their left sides becomes the identity under the right-side identifications. These statements concern whole bounded complexes, not just an independently chosen basis in each cohomology module.

If the local sheet set is \(I\), then

\[
R\Gamma(\pi^{-1}B_\epsilon;\pi^{-1}G)
\simeq\prod_{a\in I}R\Gamma(B_\epsilon;G).
\tag{7}
\]

The space on the left is a disjoint union of copies of the ball. Derived sections on a disjoint union are the product of the component derived sections. Products of modules are exact, so this product has no extra product-derived term and preserves the bounded quasi-isomorphisms in (6). The analogous formula on \(N\) uses \(B_\epsilon\cap N\).

On this cofinal system, both sides of (7) map naturally to \(\prod_{a\in I}G_x\), and every restriction map is identified with its identity. Taking the stalk limit therefore gives

\[
(R\pi_*\pi^{-1}G)_x\simeq\prod_{a\in I}G_x,
\qquad
(R\pi_{0*}\pi_0^{-1}b^{-1}G)_x\simeq\prod_{a\in I}G_x.
\tag{8}
\]

The actual map (5), defined by restriction of sections and ordinary adjunction, is the product of the maps between the two left sides in (6). It becomes the identity in (8). Thus it is a stalk isomorphism at every point, proving the lemma.

We have not asserted that filtered limits commute with arbitrary infinite products. The cofinal stabilization and the same restriction map on every sheet are what make this particular calculation valid. Neither finite rank nor properness of the covering is required. Exercise 4 gives an explicit failure without constructibility.

## Deformation and its logarithmic lift

First work in a chart \(X=\mathbb C\times Y\) with \(f(z,y)=z\). Its normal deformation has coordinates

\[
D=\mathbb R_t\times\mathbb C_z\times Y,
\quad p_D(t,z,y)=(tz,y),
\quad D_+=\{t>0\}.
\tag{9}
\]

Let \(j:D_+\hookrightarrow D\) and \(b:E\hookrightarrow D\) be the positive chamber and the time-zero fibre. The current normal-specialization construction gives

\[
\nu_YF=b^{-1}Rj_*p_+^{-1}F,
\qquad p_+=p_D|_{D_+}.
\tag{10}
\]

No extra degree shift occurs in this definition: the oriented positive-parameter contribution and the boundary convention have already been fixed in the existing specialization course.

Remove the normal zero coordinate and set

\[
D^*=\mathbb R\times\mathbb C^*\times Y,
\quad D_+^*=\mathbb R_{>0}\times\mathbb C^*\times Y,
\quad E^*=\mathbb C^*\times Y.
\]

Write \(j^*:D_+^*\hookrightarrow D^*\) and \(b^*:E^*\hookrightarrow D^*\). Let \(q:\widetilde U=\mathbb C_w\times Y\to X\) be
\(q(w,y)=(\exp(2\pi\mathrm i w),y)\). Define the deformation covering

\[
\pi:\widehat D^*=\mathbb R\times\mathbb C_w\times Y\longrightarrow D^*,
\qquad \pi(t,w,y)=(t,\exp(2\pi\mathrm i w),y).
\tag{11}
\]

Its positive and central restrictions are \(\pi_+\) and \(\pi_0\). Put \(\widehat j:\widehat D_+^*\hookrightarrow\widehat D^*\). The lift of \(p_+\) is

\[
\widehat p_+(t,w,y)
=\left(w+\frac{\log t}{2\pi\mathrm i},y\right),
\qquad t>0.
\tag{12}
\]

Indeed exponentiating its first coordinate multiplies \(\exp(2\pi\mathrm i w)\) by \(t\). The square with \(q,p_+,\pi_+,\widehat p_+\) is cartesian. For a pair of lifts in this square their difference is exactly the displayed logarithmic translation. Both \(p_+\) and \(\widehat p_+\) are submersions. The latter is a projection after the diffeomorphism \((t,w,y)\mapsto(t,w+\log t/(2\pi\mathrm i),y)\). The logarithm is the unique real logarithm of the positive parameter; no branch across time zero is being chosen.

## Comparing the lifted boundary objects

Set \(H=Rq_*q^{-1}F\). The finite-dimensional direct-image bound makes it bounded. Smooth ordinary base change for the cartesian square in (12) gives

\[
p_+^{-1}H|_{D_+^*}
\simeq R\pi_{+*}\widehat p_+^{-1}q^{-1}F
=R\pi_{+*}\pi_+^{-1}p_+^{-1}F|_{D_+^*}.
\tag{13}
\]

We use the existing smooth base-change contract with submersions, not merely arbitrary differentiable maps. Its ordinary direct images and normalization remain the specified open prerequisites.

Let

\[
G=Rj^*_*p_+^{-1}F|_{D_+^*}.
\tag{14}
\]

This is weakly real constructible on the whole \(D^*\), including time zero. To justify that assertion, the analytic map \(p_D\) pulls \(F\) back to a weakly constructible object on \(D\). The constant sheaf on \(D_+\), extended by zero, is weakly constructible on \(D\). The identity
\(Rj_*j^{-1}p_D^{-1}F=R\mathcal Hom(k_{D_+},p_D^{-1}F)\), together with the already proved weak internal-Hom theorem, gives weak constructibility and boundedness. Restriction gives (14). Thus we are not applying a theorem about arbitrary nonproper direct images to an unrestricted sheaf on an open chamber.

Ordinary composition of direct images and local-homeomorphism base change in the open square give

\[
\begin{split}
\nu_YH|_{E^*}
&\simeq (b^*)^{-1}Rj^*_*R\pi_{+*}\pi_+^{-1}p_+^{-1}F\\
&\simeq (b^*)^{-1}R\pi_*R\widehat j_*\pi_+^{-1}p_+^{-1}F\\
&\simeq (b^*)^{-1}R\pi_*\pi^{-1}G\\
&\simeq R\pi_{0*}\pi_0^{-1}(b^*)^{-1}G\\
&=R\pi_{0*}\pi_0^{-1}(\nu_YF|_{E^*}).
\end{split}
\tag{15}
\]

The local-homeomorphism exchange in the third line is checked near one point of the covering, where it is a diffeomorphism; it introduces no infinite product. The fourth line is the proved boundary lemma (5), whose hypothesis is exactly the whole-chamber weak constructibility established for \(G\). This is the delicate step in the source proof.

All maps in (15) are the ordinary restriction/base-change and composition maps. They commute with the deck translations and their trace units. Under positive normal dilation, the covering lift is translation by \(\log\lambda/(2\pi\mathrm i)\). These canonical lifted actions also make (15) compatible with positive conicity.

## Recovering nearby cycles from the punctured normal bundle

We use the existing specialization recovery maps with their precise punctured form. If \(a:U=X\setminus Y\hookrightarrow X\), they give

\[
e^{-1}\nu_YB\simeq i^{-1}B,
\qquad
R\tau^\circ_*(\nu_YB|_{E^*})
\simeq i^{-1}Ra_*a^{-1}B.
\tag{16}
\]

These are the current SH02-SP-ZERO and SH02-SP-PUNCTURE comparisons, including their actual unit, support counit and first-arrow compatibility. Their tautness, conic contraction, deformation geometry and topology primitives remain open imports.

The covering map factors as \(q=a\widetilde q\). Hence \(H=Ra_*R\widetilde q_*\widetilde q^{-1}(F|_U)\), and the natural localization unit

\[
H\longrightarrow Ra_*a^{-1}H
\tag{17}
\]

is an isomorphism. Apply the punctured formula (16) to \(B=H\). It identifies the pushforward of the left side of (15) with \(i^{-1}H=\psi_f(F)\).

On the right side of (15), composition gives

\[
R\tau^\circ_*R\pi_{0*}\pi_0^{-1}(\nu_YF|_{E^*}).
\tag{18}
\]

This is \(\psi_\ell(\nu_YF)\). To see the exact type, let \(c:E^*\hookrightarrow E\). The normal covering map is \(c\pi_0\). Its nearby object is
\(e^{-1}Rc_*R\pi_{0*}\pi_0^{-1}(\nu_YF|_{E^*})\). The object inside \(e^{-1}\) is positively conic, by the lifted dilation just described. Conic ordinary contraction identifies its zero-section restriction with its \(R\tau_*\), which is precisely (18). Thus (15) proves the first comparison in (4). Restricting to the whole normal bundle without its puncture would not be the same intermediate calculation.

## The ordinary unit and the vanishing comparison

Let \(u_F:F\to H\) be the covering adjunction unit. In the coefficient description of the preceding lessons it is precomposition with the finite-support trace \(L\to k\). The smooth comparison (13) sends its pullback to the covering unit on the positive chamber. The composition and local-cover maps in (15) preserve that unit, and the boundary map (5) is induced by the actual restriction of those same sections. Consequently (15) sends \(\nu_Yu_F|_{E^*}\) to the unit

\[
\nu_YF|_{E^*}\longrightarrow
R\pi_{0*}\pi_0^{-1}(\nu_YF|_{E^*}).
\tag{19}
\]

The natural ordinary restriction recovery in (16), and its punctured-unit compatibility, now give the commutative square

\[
\begin{array}{ccc}
i^{-1}F&\longrightarrow&\psi_f(F)\\
\downarrow\scriptstyle\sim&&\downarrow\scriptstyle\sim\\
e^{-1}\nu_YF&\longrightarrow&\psi_\ell(\nu_YF).
\end{array}
\tag{20}
\]

The horizontal arrows use the same trace/shift convention. Vanishing cycles are the signed fibre complexes supplied by the explicit coefficient complex \(K=[L\to k]\), with \(L\) in degree \(-1\). Apply its functorial coefficient-Hom construction to (20). Equivalently, choose compatible complex models for the trace-unit square and take its fixed signed fibre. This produces a map of the actual first monodromy triangles

\[
\psi_f(F)[-1]\longrightarrow\phi_f(F)\longrightarrow i^{-1}F\longrightarrow,
\qquad
\psi_\ell(\nu_YF)[-1]\longrightarrow\phi_\ell(\nu_YF)
\longrightarrow e^{-1}\nu_YF\longrightarrow.
\tag{21}
\]

The nearby and ordinary-restriction maps are isomorphisms, so the induced fibre map is an isomorphism. This is the second comparison in (4). It is a specified natural construction; an arbitrary object-level choice of cone isomorphism would not establish (20) or the canonical-map compatibility. The deck action and its identity on the constant coefficient term commute throughout, so the comparison also intertwines monodromy. The original \([-1]\) remains in (21).

## Why the local calculation glues

For a general regular \(f\), holomorphic submersion charts use \(f\) as their first coordinate. The normal deformation has a more intrinsic way to express the logarithmic construction. On its positive chamber define

\[
f_t=\frac{f\circ p_D}{t}.
\tag{22}
\]

It extends analytically through the central fibre and has central value \(\ell\). In an adapted normal chart \(p_D(v,y,t)=(tv,y)\), the numerator vanishes at \(t=0\); its analytic power series is divisible by \(t\), and its quotient at zero is \(df_y(v)\). This proves the extension and independence of the chart. The global deformation parameter is the same \(t\) in every chart.

Pull the universal cover back by \(f_t\) on its nonzero locus. For \(t>0\), adding \(\log t/(2\pi\mathrm i)\) to the covering coordinate lifts multiplication by \(t\), exactly as in (12). At time zero the covering is that of \(\ell\). Thus all covering, unit and boundary maps used above are restrictions of maps defined by (22), rather than unrelated choices on each chart. They glue. Replacing the chosen lift of \(1\) translates the covering coordinate by an integer; the resulting comparisons are conjugated by the corresponding deck identification. This records the precise dependence of these comparison maps on the chosen lift.

The proof establishes the full weak real comparison. It does not replace nearby cycles by the value of \(\nu_YF\) at \(s(y)\). The latter requires additional complex conicity, as the next example shows.

## A real angular sheaf produces infinitely many nearby coefficients

On \(X=\mathbb C\), take \(f(z)=z\) and the closed-ray sheaf

\[
F=k_{[0,\infty)}.
\tag{23}
\]

It is perfect real constructible over a field, with a finite real analytic partition, but it is not complex constructible. It is positively conic, so the current homogeneous specialization calibration gives \(\nu_{\{0\}}F=F\).

A punctured disc \(0<|z|<\epsilon\) lifts to the half-plane
\(\operatorname{Im}w>-(\log\epsilon)/(2\pi)\). The positive real ray lifts to the disjoint vertical lines \(\operatorname{Re}w=n\), \(n\in\mathbb Z\). Their portions in that half-plane are contractible and form a closed locally finite family there. Derived sections are therefore

\[
\psi_f(F)=\prod_{n\in\mathbb Z}k
\quad\text{in degree zero}.
\tag{24}
\]

The same covering computation applies to \(\psi_\ell(\nu F)\), verifying (4) with an actual infinite product. But \(s^{-1}\nu F\), at the normal direction \(1\), is only \(k\). Thus the weak real comparison cannot be strengthened to that section formula without a complex-constructibility hypothesis.

The central restriction is the diagonal \(k\to\prod_n k\). With the fixed deck convention, nearby monodromy is a bilateral shift; canonical is the quotient onto
\((\prod_n k)/\operatorname{diag}k\), in degree one, and variation is induced by \(1-M\). This difference operator is surjective on the product: fix the value at index zero and solve the difference equation successively in both directions, using a finite sum for each individual coordinate. Its kernel is exactly the diagonal. Hence variation is an isomorphism on that quotient and the central costalk is zero, consistently with the closed-ray endpoint calculation.

## Exercises

### 1. A nonconstant unit in the defining function
*Difficulty: Introductory.*

Let \(X=\mathbb C_z\times Y\), let \(a:Y\to\mathbb C^*\) be holomorphic, and take \(f(z,y)=a(y)z\). Calculate \(\ell\), \(s\), and \(f_t\). Explain why no global logarithm of \(a\) is required.

**Solution.** The zero fibre is \(z=0\), with nonzero normal derivative. In the normal coordinate \(v\), formula (2) is \(\ell(v,y)=a(y)v\), so \(s(y)=(a(y)^{-1},y)\). The deformation map is \((t,v,y)\mapsto(tv,y)\), and \(f_t=a(y)v\) for all \(t\), including zero. It is already the intrinsic extended quotient.

The covering is pulled back by this nonzero normal function. Its positive-to-original lifted map uses only multiplication by \(t\), hence the real \(\log t\). It does not trivialize the covering by selecting a logarithm of \(a(y)\). Local logarithms of \(a\), if used to write coordinates, differ on overlaps by integer deck translations. The intrinsic pullback-cover construction respects those transitions and gives the same global comparison.

### 2. Check the logarithmic square and its dimension
*Difficulty: Intermediate.*

Verify that (12) gives a cartesian square and a submersion. Explain why the nearby comparison has no new cohomological shift from the positive deformation parameter.

**Solution.** A point of the fibre product consists of \((t,z,y)\), \(t>0,z\neq0\), and \((w',y)\) with \(\exp(2\pi\mathrm i w')=tz\). Its corresponding coordinate in \(\widehat D_+^*\) is \(w=w'-\log t/(2\pi\mathrm i)\); exponentiating gives \(\exp(2\pi\mathrm i w)=z\). This construction and its inverse are continuous and smooth, proving the cartesian identification.

The change \((t,w,y)\mapsto(t,w+\log t/(2\pi\mathrm i),y)\) is a diffeomorphism, with the inverse subtracting that logarithm. Under it \(\widehat p_+\) is projection, hence a submersion. Formula (13) is ordinary smooth base change and ordinary inverse image. Formula (10) is the already normalized ordinary boundary restriction defining \(\nu\). Neither adds an orientation factor or an exceptional fibre-integration shift. The \([-1]\) in the vanishing triangle is its coefficient-cone normalization, retained identically on both sides.

### 3. Locate the product–limit argument
*Difficulty: Intermediate.*

In the boundary lemma, explain why the balls can be chosen simultaneously for \(G\) and \(b^{-1}G\). Prove that the base-change map is the identity on the product of stalks. Does the proof require finite coefficient modules?

**Solution.** In submanifold coordinates the intersection of an ambient centred ball with the coordinate plane is its centred ball. Apply the local weak small-ball theorem to \(G\), and separately to the weak inverse image \(b^{-1}G\). Each theorem works for all radii below some positive bound. The smaller bound, together with a bound ensuring cover trivialization, works simultaneously. These balls form a cofinal neighborhood system.

The natural restriction \(R\Gamma(B_\epsilon;G)\to R\Gamma(B_\epsilon\cap N;b^{-1}G)\) commutes with restriction to the common stalk \(G_x\). Both stalk maps are isomorphisms, so that restriction is identified with the identity of \(G_x\). A trivialized covering gives the same map on every sheet. Their product is therefore the identity on \(\prod_I G_x\). Exactness of module products preserves the bounded quasi-isomorphisms. The cofinal restriction system has already stabilized before its limit is taken. No finite-generation hypothesis is used or needed.

### 4. A covering boundary map without constructibility
*Difficulty: Advanced.*

On \(M=\mathbb R\), let \(G=\bigoplus_{n\geq1}k_{\{1/n\}}\), and let \(N=\{0\}\). Use the trivial countable covering \(\pi:\mathbb N\times M\to M\). For a nonzero ring, show that (5) is not an isomorphism in degree zero.

**Solution.** Stalks commute with direct sums, and each point sheaf has zero stalk at zero, so \(G_0=0\). The right side of (5) is thus zero: the covering over a point has exact product direct image of zero modules.

For a small interval \(B_\epsilon\) about zero, sections of \(G\) are finite-support families on the points \(1/n<\epsilon\). Indeed a section of a sheaf direct sum is locally a finite sum; a neighborhood of zero must contain only finitely many nonzero terms of that section. Outside a still smaller neighborhood of zero, only finitely many of the points \(1/n\) remain. Thus its whole family is finite-support.

Sections of \(\pi_*\pi^{-1}G\) on that interval are the product, over the sheet index \(r\), of these finite-support families. Take the \(r\)-th component to be the point section at \(1/r\) when that point is in the interval, and zero otherwise. On every smaller interval infinitely many of those components remain nonzero. Consequently this product section defines a nonzero germ at zero. Since the input is in degree zero, \(H^0(R\pi_*\pi^{-1}G)=\pi_*\pi^{-1}G\); the left side of (5) therefore has nonzero degree-zero stalk. This proves failure.

The sheaf is not weakly real constructible near zero: its exceptional points accumulate there. The example violates precisely the cofinal stabilization hypothesis, not finite rank on an individual point. It gives a sheaf-level instance of the product–limit obstruction.

### 5. Compute the closed-ray monodromy and variation
*Difficulty: Advanced.*

For (23), prove (24), calculate vanishing cycles, and prove that variation is an isomorphism. Compare the output with the normal section at \(1\).

**Solution.** The lifted supported set in every upper half-plane is a disjoint locally finite union of vertical half-lines indexed by integers. Each component carries the constant sheaf with ordinary cohomology \(k\) in degree zero. Derived sections on their disjoint union are their exact product, so every lifted-neighborhood coefficient is \(P=\prod_{\mathbb Z}k\). Shrinking the original disc raises the lower horizontal bound, and each vertical restriction is the constant-sheaf isomorphism. Hence the limit remains \(P\).

The central stalk of the closed ray is \(k\); a constant central section restricts to the same value on each lift, giving \(D=\operatorname{diag}k\subset P\). The first cycle triangle gives \(\phi=(P/D)[-1]\), with canonical the quotient. Monodromy is the bilateral shift under the source sheet convention. Variation sends \(\overline v\) to \((1-M)v\). Its kernel is zero because the shift invariants in the product are exactly \(D\). For every \(b\in P\), the equations for \((1-M)v=b\) can be solved by fixing \(v_0=0\) and recursively defining successive coordinates on both sides of zero. Each coordinate involves only finitely many additions, so the solution works over any ring. Variation is therefore surjective and hence an isomorphism.

The second triangle gives zero costalk, consistent with a constant sheaf on a closed half-ray at its endpoint. Positive-conic calibration makes \(\nu F=F\), so the same calculation verifies the normal nearby comparison. But its stalk at \(1\) is \(k\), whereas the nearby object is \(P\). Over a field this is an infinite-dimensional distinction. Real angular constructibility cannot replace the complex conicity needed for the section formula.

### 6. A complex supported on the central fibre
*Difficulty: Introductory.*

Let \(F=i_*A\), for a bounded weakly real-constructible complex \(A\) on \(Y\). Check both comparisons in (4), including the ordinary restriction and monodromy.

**Solution.** The punctured covering pullback is zero, so \(\psi_f(F)=0\) and the first triangle gives \(\phi_f(F)=A\). The deck action on its constant coefficient term is the identity, so monodromy is the identity. The current specialization construction identifies \(\nu_Yi_*A=e_*A\) with its actual ordinary and supported recovery maps. This has zero restriction to \(E^*\), giving \(\psi_\ell(e_*A)=0\) and \(\phi_\ell(e_*A)=A\). The square (20) becomes the identity between the ordinary coefficients \(A\) and zero nearby terms. Its signed fibre comparison is the identity of \(A\). All shifts already present in \(A\) are retained.

### 7. A normal constant family with arbitrary coefficients
*Difficulty: Intermediate.*

On \(X=\mathbb C\times Y\), let \(F\) be the pullback of a bounded weakly real-constructible complex \(A\) on \(Y\). Take \(f(z,y)=z\). Compute \(\nu_YF\), both nearby objects in (4), and both vanishing objects, without assuming \(A\) perfect.

**Solution.** In the positive deformation chamber, \(p_+^{-1}F\) is the pullback of \(A\) under the \(Y\)-projection and is independent of the time and normal coordinates. Product interval descent at time zero identifies \(\nu_YF\) with the same normal-constant pullback of \(A\) to \(E\). On the universal cover, small lifted punctured normal discs are half-planes. Such a half-plane is a product of two real open intervals; applying interval-fibre descent successively to their projections identifies its ordinary derived sections, as a family over \(Y\), with \(A\). Both nearby objects are therefore \(A\).

The ordinary restriction of either original or specialized family is \(A\), and its map to the nearby coefficient is the identity under that descent. Both vanishing objects are zero. Monodromy is the identity because translating the lifted coordinate does not change a normal-constant family. All arguments concern whole bounded complexes and interval descent; they require neither splitting the cohomology sheaves nor finite generation of their modules. This contrasts with the real angular example, where distinct lifted supported components survive.

## What has been established

The regular-fibre weak real comparison is proved with its logarithmic lifted square, actual countable-cover boundary map, punctured normal recovery, ordinary unit, source shifts and monodromy. The global construction uses analytic division by the deformation parameter to glue its local maps. Complex section and microlocal formulas, full cycle constructibility, holomorphic microsupport tests and the quadratic model remain separate targets. The proof requires the small-ball stabilization, weak inverse-image and internal-Hom theorems, smooth base change for submersions, and the ordinary and punctured conic-recovery maps stated in the relevant steps. It does not prove those underlying topology and sheaf-operation results.


# Complex nearby cycles as normal and conormal sections

A complex normal line has two useful sections. A normal vector on which the defining function has derivative one computes nearby cycles. The conormal covector given by that derivative computes vanishing cycles. The second assertion depends on the Fourier convention and on including the endpoint of a closed ray. We prove both comparisons, then deduce constructibility and the support bound for an arbitrary holomorphic function.

Let \(k\) be a commutative ring of finite global dimension. Manifolds are complex analytic, Hausdorff and countable at infinity. An object of \(D^b_{w\text{-}\mathbb C\text{-}c}(k_X)\) has locally constant cohomology on a locally finite complex analytic stratification. Its coefficient modules may be infinite. The perfect constructible subcategory additionally requires perfect stalk complexes. No Noetherian hypothesis is imposed on \(k\).

We retain the cycle normalization from [Nearby cycles and the two monodromy triangles](nearby-cycles-and-the-two-monodromy-triangles.html):

\[
\phi_f(F)=\operatorname{Cone}\bigl(i^{-1}F\longrightarrow\psi_f(F)\bigr)[-1].
\tag{1}
\]

Thus the vanishing object here already contains the source's shift by \(-1\). The real covector associated to a complex covector is its real part. On a normal complex line the pairing is \(\operatorname{Re}(v\xi)\), without a conjugate. The Fourier transform uses the closed kernel \(\operatorname{Re}(v\xi)\leq0\).

The normal-deformation comparison for weak real constructibility is proved in [Nearby cycles through the normal deformation](nearby-cycles-through-the-normal-deformation.html). Here the additional complex geometry is essential. The proof uses the bounded specialization estimate, Fourier test and whole-complex descent theorems in the precise forms stated below.

*Original lesson text and solutions: CC0 1.0 Universal. Human mathematical sources are credited below.*

## Complex constructibility survives specialization

Let \(Y\subset X\) be a closed complex submanifold. Put \(E=T_YX\), \(L=T_Y^*X\subset T^*X\), and \(\Lambda=\operatorname{SS}(F)\). The complex constructibility criterion proved in Complex microlocal stratifications and constructibility makes \(\Lambda\) closed complex analytic, complex-conic and real-isotropic.

The bounded specialization estimate `SH02-CHE-001` gives

\[
\operatorname{SS}(\nu_YF)\subset C_L(\Lambda),
\tag{2}
\]

under the canonical normal/cotangent identification. In adapted holomorphic coordinates \((u,y)\), with \(Y=\{u=0\}\), write \((\alpha,\beta)\) for their complex covectors. The coordinates and signs of that identification are

\[
(v,y;\alpha,\beta)\in T^*E
\longleftrightarrow(\alpha,y;-v,\beta)\in T^*L
\longleftrightarrow
\bigl((0,y;\alpha,0);v,\beta\bigr)\in N_L(T^*X).
\tag{3}
\]

Each map is holomorphic. The second map uses the symplectic normal identification \(K([w])(a)=\operatorname{Re}\Omega(w,a)\); its inverse is induced by \(-H\) with the Hamiltonian convention used earlier. The first is the Fourier cotangent map. These signs agree with the selected specialization contract.

The analytic normal-cone argument in Analytic normal cones through complex deformation applies to the analytic set \(\Lambda\) and the analytic submanifold \(L\). Its accessible central fibre is analytic and invariant under complex normal scaling. The Lagrangian normal-cone theorem proved in Boundary forms and Lagrangian normal cones makes its image in \(T^*L\) real-isotropic. The holomorphic symplectic Fourier identification in (3) preserves this property on \(T^*E\).

We must also check cotangent conicity in \(T^*E\), since normal scaling alone is a different action. A normal-cone sequence in these coordinates has

\[
(t_jv_j,y_j;\alpha_j,t_j\beta_j)\in\Lambda,
\qquad t_j>0,\quad t_j\to0,
\tag{4}
\]

with all four displayed limiting coordinates finite. Multiplying the input covector by any fixed \(\lambda\in\mathbb C^*\) gives the same witnesses with \(\alpha_j,\beta_j\) replaced by \(\lambda\alpha_j,\lambda\beta_j\). Under (3) this is exactly complex dilation of the output cotangent covector at the unchanged base \((v,y)\). Therefore the bound in (2) is closed complex analytic, complex-conic and real-isotropic. The same constructibility criterion, applied to this bound, proves

\[
\nu_YF\in D^b_{w\text{-}\mathbb C\text{-}c}(k_E),
\qquad
\mu_YF=(\nu_YF)^\wedge\in
D^b_{w\text{-}\mathbb C\text{-}c}(k_{E^\vee}).
\tag{5}
\]

For the second assertion use the complex Fourier theorem proved in Holomorphic operations and complex Fourier symmetries. Both objects are bounded and positively conic along their bundle fibres. The boundedness and conicity are part of the selected specialization/Fourier contracts, rather than consequences of finite-dimensional coefficient modules.

For perfect constructible \(F\), Perfect operations and finite microlocal coefficients proves perfect stalks for both \(\nu_YF\) and \(\mu_YF\). That proof keeps the real deformation chamber and treats it using weak real constructibility and perfect internal Hom. We have not treated a positive real chamber as a holomorphic open subset. Combining the real perfection theorem with (5) proves both perfect complex constructibility statements.

## Fibre constancy after lifting the punctured normal line

For now suppose \(Y=f^{-1}(0)\) is a regular analytic fibre: \(df_y\ne0\) for every \(y\in Y\). Its normal line is canonically identified with \(\mathbb C_v\times Y\) by

\[
\ell_y([a])=df_y(a),\qquad
s(y)=\ell_y^{-1}(1),\qquad
s'(y)=df_y\in T_Y^*X.
\tag{6}
\]

In the dual coordinate \(\xi\), \(s'\) is the section \(\xi=1\). Let \(G=\nu_YF\), and let \(e:Y\hookrightarrow E\) be the zero section. A reduced smooth zero set for a ramified defining function does not suffice for (6); \(z^m\), \(m>1\), has zero derivative at its reduced zero set.

On \(E\setminus e(Y)\), the cohomology of \(G\) is locally constant on every \(\mathbb C^*\) fibre. Here is the relevant microsupport check. Positive conicity annihilates the real radial vector field. The full complex Euler calculation in the preceding Fourier lesson, using the complex-conic actual microsupport, annihilates the imaginary radial vector field as well. In local coordinates a vertical covector \(\alpha\) consequently satisfies

\[
\operatorname{Re}(v\alpha)=0,
\qquad \operatorname{Im}(v\alpha)=0.
\tag{7}
\]

When \(v\ne0\), it has \(\alpha=0\). The submersion descent criterion for microsupport therefore makes \(G\) locally a whole derived pullback in these fibre coordinates, and in particular makes its cohomology locally constant on each punctured fibre. The same reasoning applies to \(\mu_YF\) away from its dual zero section, by (5).

Use the cover

\[
p:\mathbb C_w\times Y\longrightarrow\mathbb C_v^*\times Y,
\qquad p(w,y)=(e^{2\pi iw},y),
\qquad q(w,y)=y.
\tag{8}
\]

The pullback \(p^{-1}(G|_{v\ne0})\) has locally constant cohomology on the contractible \(\mathbb C_w\) fibres. The exact contract `SH02-CON-CYLINDER` identifies its derived direct image with evaluation at \(w=0\), through the actual evaluation morphism. It applies twice, to the two real coordinates of \(w\), and retains the full extension data and arbitrary coefficient modules. Thus

\[
Rq_*p^{-1}(G|_{v\ne0})\simeq s^{-1}G.
\tag{9}
\]

This contract proves descent on a product with \(\mathbb R\) using closed-strip exhaustions and their evaluation maps. Iteration on \(\mathbb R^2\) is legitimate. It does not assert unrestricted nonproper base change or descent from a punctured fibre with nontrivial fundamental group.

Ordinary positive-conic contraction identifies the left side of (9) with \(\psi_\ell(G)\). Explicitly, the cover direct image in the nearby definition has a lifted positive action: multiplying \(v\) by \(r>0\) translates \(w\) by \(\log r/(2\pi i)\). Contracting its ordinary direct image to the zero section and composing the two direct images gives \(Rq_*\) in (9). The normal comparison already proved therefore yields

\[
\psi_f(F)\simeq\psi_\ell(G)\simeq s^{-1}\nu_YF.
\tag{10}
\]

Fixing \(w=0\) fixes the lift of the normal section. Deck translation \(w\mapsto w+1\) remains the monodromy automorphism. Fibrewise local constancy on \(\mathbb C^*\) does not force this automorphism to be the identity.

## A dual halfspace has a closed-ray polar

Let \(\tau:E\to Y\) and \(\tau^\vee:E^\vee\to Y\) be the bundle projections. Set

\[
U=\{\xi\in\mathbb C:\operatorname{Re}\xi>0\},
\qquad R=\{v\in\mathbb C:\operatorname{Im}v=0,
\ \operatorname{Re}v\geq0\}.
\tag{11}
\]

The cohomology of \(\mu_YF\) is locally constant along the \(U\) fibres. A smooth product identification \(U\simeq\mathbb R^2\), chosen to take \(1\) to the origin, and the whole-complex cylinder descent give

\[
s'^{-1}\mu_YF\simeq
R\tau^\vee_*R\mathcal Hom(k_{U\times Y},\mu_YF).
\tag{12}
\]

The internal Hom for this open coefficient means ordinary sections over the open halfspace, pushed into the ambient bundle. It does not mean compactly supported cohomology.

In the real pairing \(\operatorname{Re}(v\xi)\), the positive polar of \(U\) is \(R\). Indeed, write \(v=u+iw\) and \(\xi=a+ib\). Then

\[
\operatorname{Re}(v\xi)=ua-wb,
\qquad a>0,\quad b\in\mathbb R.
\tag{13}
\]

Nonnegativity for every such \(a,b\) forces \(w=0\) and \(u\geq0\), and these conditions suffice. The zero vector passes every inequality and must be included.

The open-convex-cone test `SH02-FS-SECTIONS`, formula FS13, now gives

\[
R\tau^\vee_*R\mathcal Hom(k_{U\times Y},G^\wedge)
\simeq R\tau_*R\mathcal Hom(k_{R\times Y},G).
\tag{14}
\]

To obtain an isomorphism of sheaves on \(Y\), apply the natural Fourier test to the restriction over every open base subset and its restriction maps. Its proof applies the inverse Fourier equivalence to both Hom arguments; the inverse image of the open-cone coefficient is its closed-polar coefficient. The inverse Fourier shifts and dual orientation lines cancel in this test. The real rank of the complex line remains two; (14) introduces no further shift or orientation factor.

## The slit and the cover have the same section complex

Let \(O=\mathbb C\setminus R\). This slit plane is contained in \(\mathbb C^*\), and its inverse image has the distinguished open strip

\[
S=\{w\in\mathbb C:0<\operatorname{Re}w<1\}.
\tag{15}
\]

The restriction \(p|_S:S\to O\) is a homeomorphism. Write \(E^*=\mathbb C^*\times Y\) and \(j:E^*\hookrightarrow E\); the cover \(p\) has target \(E^*\). Extension by zero from \(S\) to the cover, proper-support direct image along \(p\), and then \(j_!\) give a coefficient morphism on \(E\)

\[
\alpha:k_{O\times Y}\longrightarrow
L=j_!p_!k_{\mathbb C_w\times Y},
\qquad
\operatorname{tr}\circ\alpha:
k_{O\times Y}\longrightarrow k_E.
\tag{16}
\]

The trace is the composite of the punctured-target counit, extended by \(j_!\), with the open-inclusion counit \(j_!k_{E^*}\to k_E\). On \(E^*\) it sums finitely supported sheet coefficients. Consequently \(\operatorname{tr}\circ\alpha\) is the ordinary open-extension inclusion. Both two-term complexes below are objects on \(E\), with terms in degrees \(-1,0\):

\[
B=[k_{O\times Y}\longrightarrow k_E],
\qquad K=[L\xrightarrow{\operatorname{tr}}k_E],
\qquad B\longrightarrow K=(\alpha,\mathrm{id}).
\tag{17}
\]

Open–closed localization identifies \(B\simeq k_{R\times Y}\), in degree zero. Applying contravariant internal Hom to (17) gives

\[
R\tau_*R\mathcal Hom(K,G)
\longrightarrow R\tau_*R\mathcal Hom(k_{R\times Y},G).
\tag{18}
\]

The left side equals \(\phi_\ell(G)\). This follows from the coefficient definition in the monodromy lesson and ordinary positive-conic contraction to \(e\). The coefficient \(K\), the target \(G\), and their internal Hom have the needed positive conicity; the lifted positive action preserves \(S\), so it also preserves the coefficient map in (17).

We show that (18) is an isomorphism by comparing the Hom triangles of the two complexes in (17). Their \(k_E\) terms have the identity map. On the other terms, ordinary composition and the cover adjunction identify the map with restriction

\[
Rq_*p^{-1}(G|_{v\ne0})
\longrightarrow
R(\tau|_{O\times Y})_*(G|_{O\times Y}).
\tag{19}
\]

It is restriction from the entire cover to \(S\). The whole cover and the open strip are each a product with a contractible real two-dimensional fibre. Their cohomology is vertically locally constant. Apply the cylinder descent contract, identifying \(S\) with \(\mathbb R^2\), and evaluate both sides at \(w=1/2\). The two evaluation maps commute with restriction. Both are isomorphisms, so (19) is an isomorphism.

The evaluation point lies above \(v=-1\), which belongs to \(O\). In contrast, \(v=1\) lies on the removed ray. Evaluation at \(w=0\) from (9) is related to evaluation at \(w=1/2\) by transport in the contractible cover, rather than by pretending that the normal section \(1\) lies in the slit. This distinction allows arbitrary monodromy on the punctured normal line.

The map between the two Hom triangles is now an isomorphism on both their other terms. Their fibre term (18) is an isomorphism too. Combining (12), (14), (18), and the normal vanishing comparison gives

\[
\phi_f(F)\simeq\phi_\ell(\nu_YF)
\simeq R\tau_*R\mathcal Hom(k_{R\times Y},\nu_YF)
\simeq s'^{-1}\mu_YF.
\tag{20}
\]

The coefficient map (17) fixes the slit branch used in this comparison. Formula (20) retains exactly the normalization (1). It does not append a further Fourier, real-rank or complex-orientation shift. Changing the lift is governed by deck transport; no trivialization of monodromy on the entire punctured line has been assumed.

## Constructibility and support for a critical function

For a regular fibre, (5), (10), and (20), followed by holomorphic ordinary inverse image along \(s,s'\), prove weak complex constructibility of both cycles. If \(F\) has perfect stalks, both bundle objects have perfect stalks and ordinary inverse image retains them. This proves perfect complex constructibility as well.

Now allow any holomorphic \(f:X\to\mathbb C\). Its zero set \(Y\) can be singular. Use the closed graph and the coordinate projection

\[
g:X\hookrightarrow\mathbb C_t\times X,
\quad g(x)=(f(x),x),\qquad H=g_*F,
\quad Z=\{t=0\}\simeq X.
\tag{21}
\]

The graph is proper and holomorphic. The operation theorem makes \(H\) weakly, or perfectly, complex constructible as appropriate. The target coordinate \(t\) has a regular fibre \(Z\), so the results just proved apply to \(\psi_t(H)\) and \(\phi_t(H)\). With \(a:Y\hookrightarrow Z\) the closed inclusion, the actual proper-on-support comparisons from [Proper pushforwards of nearby and vanishing cycles](proper-pushforwards-of-nearby-and-vanishing-cycles.html) give

\[
\psi_t(H)\simeq a_*\psi_f(F),
\qquad \phi_t(H)\simeq a_*\phi_f(F).
\tag{22}
\]

These are objects supported on \(a(Y)\). Refine their analytic stratifications in \(Z\) compatibly with the analytic subset \(Y\). Their restrictions are locally constant on the resulting strata of \(Y\); ordinary stalk restriction retains the perfect condition. Thus both cycles are weakly complex constructible on \(Y\), and are perfect constructible when \(F\) is. This argument does not assign a smooth normal line to a singular fibre.

The selected contract `SH02-MO-MICROLOCAL-SUPPORT` gives

\[
\operatorname{supp}(\mu_YF)
\subset T_Y^*X\cap\operatorname{SS}(F)
\tag{23}
\]

for a smooth \(Y\). Here and below support is the closed support of the cohomology sheaves. For a regular fibre, pulling (23) back along \(s'\) and using (20) gives the closed bound

\[
\operatorname{supp}(\phi_f(F))
\subset\{y\in f^{-1}(0):(y;df_y)\in\operatorname{SS}(F)\}.
\tag{24}
\]

For a critical function use (21)–(22). At \((0,x)\), the covector \(dt\) restricts to the graph as \(df_x\). More explicitly, graph transpose pullback sends \((c,\xi)\) to \(c\,df_x+\xi\). The proper direct-image estimate `SH02-MO-PROPER-PUSH`, formula MO8, implies

\[
((0,x);dt)\in\operatorname{SS}(g_*F)
\ \Longrightarrow\ (x;df_x)\in\operatorname{SS}(F).
\tag{25}
\]

Apply the regular support bound to \(t,H\) and use (22). It gives (24) for arbitrary \(f\), including \(df_x=0\). Closedness matters: the preimage of the closed set \(\operatorname{SS}(F)\) under \(y\mapsto(y;df_y)\) is closed, so the assertion bounds closed support and not merely individual nonzero stalks.

Finally, if \(p\notin\operatorname{SS}(F)\), choose an open cotangent neighborhood \(V\) disjoint from microsupport. For every point \(x\) and every local holomorphic function \(h\) with \(h(x)=0\) and \((x;dh_x)\in V\), restriction of microsupport to the domain of \(h\) and (24) give

\[
\phi_h(F)_x=0.
\tag{26}
\]

This proves the uniform forward holomorphic test. [Quadratic cycles and the holomorphic microsupport test](quadratic-cycles-and-the-holomorphic-microsupport-test.html) proves the reverse implication using generic microlocal models, transfer of the test to those models, and the quadratic calculation.

## Exercises with complete solutions

### The endpoint and two Fourier calibrations

*Difficulty: Introductory.*

Compute the polar of \(U=\{\operatorname{Re}\xi>0\}\) using the pairing in (13). Over a field, check (20) for \(G=k_{\mathbb C}\) and \(G=k_{\{0\}}\), with \(f(v)=v\). Explain why the ray's endpoint changes the answer.

**Solution.** Allowing every real \(b\) forces \(w=0\), and then every \(a>0\) forces \(u\geq0\). Thus the polar is the closed ray \(R\), including zero. For \(k_{\mathbb C}\), nearby cycles are \(k\) and the central-to-nearby map is the identity, so \(\phi=0\). The Fourier transform is \(k_{\{0\}}[-2]\), with the canonical real rank-two orientation, and restriction at \(\xi=1\) is zero. For \(k_{\{0\}}\), the nearby object is zero and (1) gives \(\phi=k\); its Fourier transform is the constant \(k\) in degree zero, agreeing at \(1\). Equivalently, \(R\operatorname{Hom}(k_R,k_{\{0\}})=k\), since closed support at zero belongs to \(R\). Removing the endpoint makes that Hom zero: the coefficient then has zero stalk at zero and closed-embedding adjunction computes it there. The second calibration would fail.

### A slit cannot be evaluated at the removed normal section

*Difficulty: Intermediate.*

For (15), locate lifts of \(v=1\) and \(v=-1\). Prove directly that restriction from the cover to \(S\) induces an isomorphism of ordinary derived section complexes for a cohomologically locally constant complex on the cover. Describe the effect of choosing the strip \(m<\operatorname{Re}w<m+1\) instead.

**Solution.** The lifts of \(1\) are the integers, all on strip boundaries. The lift \(1/2\) of \(-1\) lies inside \(S\). The two cylinder descent evaluations at \(1/2\) are isomorphisms and commute with the restriction morphism, so that morphism is an isomorphism in the derived category, including higher extension data. For the other strip use \(m+1/2\). Let \(\rho_m\) be restriction to that strip, transported to the original strip by translation by \(-m\), and let \(M\) denote the nearby deck action. With the convention \(M(e_n)=e_{n-1}\), these maps satisfy \(\rho_m M^m=\rho_0\), or \(\rho_m=\rho_0M^{-m}\). The result is independent up to this specified transport, without assuming trivial monodromy.

### Nontrivial puncture monodromy survives the section formula

*Difficulty: Intermediate.*

Let \(k=\mathbb Q\), let \(j:\mathbb C^*\hookrightarrow\mathbb C\), and let \(\mathcal L\) be the rank-one local system with counterclockwise holonomy \(H\) equal to multiplication by \(2\). For \(F=j_!\mathcal L\) and \(f(z)=z\), compute the nearby and vanishing objects at zero and the conormal section of \(\mu_{\{0\}}F\). Explain why (9) does not trivialize the original local system.

**Solution.** The central stalk is zero. The cover pullback of \(\mathcal L\) is constant \(\mathbb Q\); its contractible fibre has ordinary derived sections \(\mathbb Q\), with no higher cohomology. Thus \(\psi=\mathbb Q\), with nearby deck automorphism \(M=H^{-1}=1/2\) under the selected convention \(M(e_n)=e_{n-1}\), and (1) gives \(\phi=\mathbb Q[-1]\). The conormal section \(\xi=1\) is therefore \(\mathbb Q[-1]\) by (20). Positive radial transport makes the original sheaf positively conic; its specialization at zero is the same conic sheaf by the homogeneous specialization calibration. The descent takes place on the simply connected cover. Descent to a counterclockwise loop recovers \(H=M^{-1}=2\), so \(\mathcal L\) on \(\mathbb C^*\) remains nontrivial. Both coefficients are perfect, and the two-stratum complex analytic stratification is valid.

### Arbitrary weak coefficients and central support

*Difficulty: Intermediate.*

Let \(M=\bigoplus_{r\geq1}\mathbb Q\), in degree zero, and use \(E=\mathbb C\times Y\), \(f(v,y)=v\). Compute both cycles for \(F=\tau^{-1}M_Y\) and for \(F=e_*M_Y\). Check their normal and conormal sections. Which perfect condition fails?

**Solution.** For the normal-constant family, cover descent gives \(\psi=M_Y\), and the central-to-nearby map is the identity, so \(\phi=0\). Its specialization is the same family; the normal section is \(M_Y\), while its Fourier transform is \(e_*M_Y[-2]\), whose nonzero conormal section is zero. For central support the specialization is \(e_*M_Y\), the punctured restriction is zero, and \(\psi=0\), \(\phi=M_Y\). Its Fourier transform is the normal-constant \(M_Y\), so its conormal section is \(M_Y\). All descent and coefficient maps retain the infinite module \(M\); finite-dimensionality was not used. These objects are weakly complex constructible but not perfect constructible on their nonzero strata, since a perfect complex over \(\mathbb Q\) has finite-dimensional cohomology.

### A ramified function needs the graph construction

*Difficulty: Intermediate.*

For \(F=\mathbb Q_{\mathbb C}\), \(f(z)=z^m\), \(m\geq2\), compute the cycles at zero and their deck monodromy. Compare the answer with a putative normal section defined by \(df_0\).

**Solution.** The pulled-back cover is described by \(z^m=e^{2\pi iw}\). It has \(m\) components, each parametrized by \(z=\exp(2\pi i(w+r)/m)\), \(r=0,\ldots,m-1\). Small covered punctured neighborhoods have contractible component fibres, giving \(\psi=\mathbb Q^m\) with cyclic permutation of components. The central unit is the diagonal \(\mathbb Q\to\mathbb Q^m\). It is injective, so (1) gives \(\phi=(\mathbb Q^m/\mathbb Q\mathbf1)[-1]\) with the induced cyclic monodromy. This is nonzero. The reduced zero set is a point, but \(df_0=0\) cannot identify its normal line with the target line or produce \(\ell^{-1}(1)\). The graph in (21) instead has the regular ambient coordinate \(t\), and its cycle comparison gives exactly these objects. The support bound uses the zero covector \(df_0\), which belongs to the microsupport of the nonzero constant sheaf.

### The graph transpose keeps the critical zero covector

*Difficulty: Intermediate.*

For a holomorphic \(f\) on \(X\), calculate the transpose differential of \(g(x)=(f(x),x)\). Derive (25) from the proper direct-image estimate and explain why the conclusion is still valid at a critical point.

**Solution.** A tangent vector \(a\) maps to \((df_x(a),a)\). A target covector \(c\,dt+\xi\) therefore evaluates to \(c\,df_x(a)+\xi(a)\), and its transpose image is \(c\,df_x+\xi\). At a graph point \((0,x)\), the covector \(dt\) corresponds to \((c,\xi)=(1,0)\), hence to \(df_x\). Properness holds because \(g\) is a closed embedding; its support restriction is proper too. The estimate forces \(df_x\in\operatorname{SS}(F)\) whenever \(dt\in\operatorname{SS}(g_*F)\). At a critical point this is a zero covector, not an undefined pullback. Zero covectors are retained in the estimate and in the closed support bound. For instance, in the preceding ramification example the graph covector \(dt\) can be characteristic even though its transpose is zero.

### The cotangent sign and the two scaling actions

*Difficulty: Advanced.*

In the coordinates of (3), evaluate the symplectic normal map on tangent vectors to \(L\). Verify its \(-v\) term. Distinguish complex normal scaling of the cone from the complex cotangent dilation needed for the bound (2).

**Solution.** The complex symplectic form is \(d\alpha\wedge du+d\beta\wedge dy\). A normal representative has components \((\delta u,\delta\beta)=(v,\beta)\); a tangent vector to \(L\) has components \((\delta\alpha,\delta y)=(a,b)\). Pairing the normal representative first gives \(-av+\beta b\). Taking real parts is exactly the real symplectic normal map, so its complex covector on \(L\) is \(-v\,d\alpha+\beta\,dy\). Normal scaling multiplies \(v,\beta\) at fixed \((\alpha,y)\); transported to \(T^*E\), it changes the base \(v\), so it is not cotangent dilation there. Multiplying ambient input covectors in (4) by \(\lambda\), however, changes \((\alpha,\beta)\) to \((\lambda\alpha,\lambda\beta)\) at fixed \((v,y)\). This proves the actual output cotangent dilation property. The analytic normal cone and the isotropy theorem supply the other hypotheses of the complex constructibility criterion.

### A uniform test near the zero section

*Difficulty: Advanced.*

For \(F=k_X\) with nonzero \(k\), prove the forward test near any nonzero cotangent covector. Show that no neighborhood of a zero covector can have every holomorphic test vanish, by choosing a constant function. Keep the normalization (1).

**Solution.** The microsupport of \(k_X\) is the zero section. A small cotangent neighborhood of a nonzero covector can be chosen disjoint from that section. Formula (24), applied on the domain of each holomorphic test, makes its vanishing stalk zero whenever its derivative belongs to that neighborhood. At a zero covector \((x;0)\), take \(h=0\) on a neighborhood of \(x\). Its punctured inverse image is empty, so \(\psi_h(F)=0\), and (1) gives \(\phi_h(F)=F\), with nonzero stalk \(k\) in degree zero. Thus that test belongs to every neighborhood of \((x;0)\) and prevents uniform vanishing. This verifies the zero-function phenomenon directly without asserting the reverse criterion for general weakly complex constructible objects.

## What has been established

The normal and conormal comparisons give weak and perfect complex cycle constructibility for every holomorphic function, the closed vanishing support bound, and the uniform forward test, using the stated prerequisite theorems. [Quadratic cycles and the holomorphic microsupport test](quadratic-cycles-and-the-holomorphic-microsupport-test.html) proves the reverse criterion and its coefficient model. [Vanishing cycles as positive real support](vanishing-cycles-as-positive-real-support.html) gives the local-support comparison, including critical functions and singular zero fibres.

## References

David B. Massey, *Notes on Perverse Sheaves and Vanishing Cycles*, [arXiv:math/9908107v13, §3](https://arxiv.org/abs/math/9908107v13), supplies the cycle conventions and explains the coefficient-complex construction credited to Kashiwara and Schapira. Ren Fernandes, Kazuki Kudomi and Kiyoshi Takeuchi, *Characteristic cycles of real and complex constructible sheaves, revisited*, [arXiv:2603.14821v2, §2.4 and §5, (5.42)–(5.43)](https://arxiv.org/abs/2603.14821v2), defines specialization and states the regular-fibre conormal comparison. Its vanishing object is this lesson's object shifted by one. The paper refers elsewhere for that comparison; it does not supply an independent proof of it in those passages. Its field-valued constructible setting also does not establish our weak-coefficient extension.

The argument here must therefore stand on its displayed normal-cone estimate, complex Euler annihilation, full-complex cylinder descent, Fourier section formula and slit coefficient map. The graph factorisation then handles critical functions. The named programme providers for these steps, and their remaining transitive proof obligations, are recorded in the [source and proof guide](source-and-proof-guide.html). A free statement of a comparison is not a replacement for those proofs.


# Quadratic cycles and the holomorphic microsupport test

Holomorphic tests detect every direction in the microsupport of a weakly complex constructible sheaf. The forward direction follows from the vanishing support bound. To prove the reverse direction, we compute a quadratic test on a generic conormal model and show that the test depends only on its microlocal class. Both the dimension of the model and the source's vanishing-cycle shift matter.

Throughout, \(k\) is commutative of finite global dimension, and complex manifolds are Hausdorff and countable at infinity. Coefficient complexes belong to \(D^b(k)\); they need not be perfect or have finite cohomology modules. We use the cycle convention

\[
\phi_f(F)=\operatorname{Cone}\bigl(i^{-1}F\longrightarrow\psi_f(F)\bigr)[-1],
\tag{1}
\]

where \(i:f^{-1}(0)\hookrightarrow X\). The comparison with a conormal section, and its exact Fourier and closed-ray normalization, were proved in [Complex nearby cycles as normal and conormal sections](complex-nearby-cycles-as-normal-and-conormal-sections.html).

We prove the quadratic calculation directly, including its unit map and deck action. The generic coefficient object model is the theorem `SH02-LFI-SUPPORTED`. The quotient/null criterion and arbitrary bounded microlocal support estimate are `SH02-MC-LOCAL` and `SH02-MO-MICROLOCAL-SUPPORT`. Their precise hypotheses are retained in the applications below.

*Original lesson text and solutions: CC0 1.0 Universal. Human mathematical sources are credited below.*

## The covered quadratic ball retracts to a sphere

Put \(Q(z)=\sum_{j=1}^d z_j^2\) on \(\mathbb C^d\), with \(d\geq1\), and let \(M_{\mathbb C^d}\) be the constant complex with value \(M\). Only zero can support its vanishing cycles: outside zero the differential \(dQ\) is nonzero, while the constant complex has microsupport contained in the zero section. The support bound of the preceding lesson applies.

We compute the central stalk using the ordinary cover in the nearby definition. Above \(Q(z)\ne0\), write the target parameter as \(\lambda=e^{2\pi iw}\). The covered open ball of radius \(\epsilon\) is

\[
\mathcal B_\epsilon=
\{(z,w):Q(z)=e^{2\pi iw},\ |z|<\epsilon\}.
\tag{2}
\]

For \(w\) fixed, write \(\lambda=r e^{i\theta}\) using the lifted argument \(\theta=2\pi\operatorname{Re}w\), and rotate

\[
e^{-i\theta/2}z=x+iy,\qquad x,y\in\mathbb R^d.
\tag{3}
\]

The equations in (2) become

\[
|x|^2-|y|^2=r,\qquad x\cdot y=0,
\qquad r+2|y|^2<\epsilon^2.
\tag{4}
\]

Thus \(0<r<\epsilon^2\), and

\[
u=\frac{x}{\sqrt{r+|y|^2}}\in S^{d-1},\qquad
y\in u^\perp,\qquad
|y|<\sqrt{(\epsilon^2-r)/2}.
\tag{5}
\]

These formulas give a homeomorphism of \(\mathcal B_\epsilon\) with an open tangent-disc bundle over

\[
A_\epsilon\times S^{d-1},\qquad
A_\epsilon=\{w\in\mathbb C:|e^{2\pi iw}|<\epsilon^2\}.
\tag{6}
\]

The base \(A_\epsilon\) is an open halfplane. The disc radius in (5) is strictly positive on it. Sending \(y\) to \(t y\), \(0\leq t\leq1\), and replacing \(x\) by \(\sqrt{r+t^2|y|^2}\,u\), is a deformation retraction to the zero-disc section. It preserves (4), stays in the ball, and fixes \(w,u\). Consequently \(\mathcal B_\epsilon\) retracts to \(A_\epsilon\times S^{d-1}\).

The pullback coefficient in the nearby definition is the constant complex \(M\). Its ordinary sheaf cohomology on these locally contractible spaces is computed by constant-coefficient cochains. We use the usual sheaf/singular comparison and homotopy invariance for constant coefficients, with the bounded-complex extension supplied by its cohomology spectral sequence. These are explicit topological prerequisites. Only the finite free cochain complex of the sphere is required in the resulting coefficient calculation, so no finite-module or infinite-product Künneth assumption appears.

For \(0<\delta<\epsilon\), the inclusion \(\mathcal B_\delta\hookrightarrow\mathcal B_\epsilon\) is, in (5), the identity on \(u\), an inclusion of halfplanes, and an inclusion of the smaller tangent discs. Both retractions commute with this inclusion at the zero-disc section. Restriction therefore induces the identity on the sphere cochain model after the contractible halfplanes are removed. These are the actual maps entering the stalk colimit. It follows that

\[
\psi_Q(M_{\mathbb C^d})_0
\simeq R\Gamma(S^{d-1};M),
\tag{7}
\]

and the central unit \(M\to\psi_Q(M)_0\) is the constant-cochain map. This identifies the map as well as the object. The stalk of an ordinary derived direct image is computed by this filtered system of open balls; exact filtered colimits of coefficient modules preserve the cohomology isomorphisms just exhibited.

## The reduced cochains fix the degree and monodromy

For \(d\geq2\), orient \(\mathbb R^d\) in the displayed coordinate order and give its unit sphere the boundary orientation. Its reduced cochain complex is \(k[1-d]\), using the finite cellular computation of a sphere. For \(d=1\), the sphere has two points; the constant-cochain map is the diagonal \(k\to k^2\), and its quotient is \(k=k[1-d]\). In both cases, with arbitrary bounded \(M\), the augmented finite free cochain model gives

\[
\operatorname{Cone}\bigl(M\longrightarrow R\Gamma(S^{d-1};M)\bigr)
\simeq M[1-d].
\tag{8}
\]

Tensoring a finite free model with \(M\) is a derived tensor calculation with no perfection requirement on \(M\). Formula (1) supplies the remaining shift. With \(b:\{0\}\hookrightarrow Q^{-1}(0)\), localization for the support already determined therefore proves

\[
\phi_Q(M_{\mathbb C^d})\simeq b_*M[-d].
\tag{9}
\]

For \(d=0\), the domain is a point and \(Q=0\). The punctured inverse image is empty, so \(\psi_Q=0\) and \(\phi_Q=M\). This agrees with (9) at \(d=0\), without inventing a negative-dimensional sphere.

The cover deck translation \(w\mapsto w+1\) changes the lifted half-angle in (3) by \(\pi\). It acts on the retracted real sphere by \(u\mapsto-u\). The antipodal map has degree \((-1)^d\) on \(S^{d-1}\); this follows by extending it to the linear map \(-\mathrm{id}\) of \(\mathbb R^d\), whose determinant is \((-1)^d\), and using boundary orientation. On the reduced complex in (8), and hence on \(M[-d]\), deck monodromy is

\[
M_Q=(-1)^d\,\mathrm{id}.
\tag{10}
\]

For \(d=1\), swapping the two points negates their diagonal quotient, giving the same sign directly. For \(d=0\) the empty-nearby coefficient construction gives identity on the central vanishing complex, consistent with (10). The degree convention in (9) is the source convention, rather than the unshifted reduced cohomology degree in (8).

## A conormal test descends through arbitrary denominator cones

Let \(h\) be holomorphic near \(x\), with \(h(x)=0\) and \(dh_x\ne0\). After shrinking, \(T=h^{-1}(0)\) is a smooth hypersurface. Put \(p=(x;dh_x)\). The exact functor

\[
\mathcal T_h:D^b(k_X)\longrightarrow D^b(k),
\qquad A\longmapsto(\mu_TA)_p
\tag{11}
\]

is defined on all bounded sheaf complexes on this neighborhood. If \(p\notin\operatorname{SS}(A)\), the arbitrary bounded support contract MO15 makes \(\mathcal T_h(A)=0\). Hence, for any morphism whose cone has microsupport avoiding \(p\), exactness makes its image under \(\mathcal T_h\) an isomorphism.

The quotient contract `SH02-MC-LOCAL` identifies precisely these cones as the null subcategory in \(D^b(k_X;p)\). Its quotient property therefore makes (11) descend to that category. In particular,

\[
A\simeq B\text{ in }D^b(k_X;p)
\quad\Longrightarrow\quad
\mathcal T_h(A)\simeq\mathcal T_h(B).
\tag{12}
\]

This implication can also be read directly through denominator fractions: every denominator is sent to an isomorphism, so a representative fraction induces an isomorphism of the test objects. Its cone need not be weakly complex constructible.

For weakly complex constructible \(A\), the conormal section comparison from the preceding lesson identifies

\[
\mathcal T_h(A)\simeq\phi_h(A)_x.
\tag{13}
\]

We use (13) only on the two weakly complex constructible endpoints of (12). We do not claim that holomorphic vanishing cycles of an arbitrary intermediate roof object satisfy that comparison. The proof requires the generic coefficient *object* model, not full faithfulness of all coefficient morphisms.

## Generic analytic conormals give nonzero quadratic tests

For weakly complex constructible \(F\) on a complex \(n\)-manifold, its actual microsupport \(\Lambda\) is a closed complex analytic Lagrangian cone by the complex criterion and singular involutivity developed earlier. Its nonempty components have complex dimension \(n\). On a dense open subset, each point is regular, lies on only one local component, and the projection \(\pi:\Lambda\to X\) has locally constant rank. This follows from analytic regular density, local finiteness of components, and the holomorphic minor description of the lower-rank locus.

At such a point \(p\), the constant-rank theorem supplies a local complex image submanifold \(Y\subset X\). Canonical-form vanishing gives \(\xi|_{T_yY}=0\) at points \((y;\xi)\) of the selected component: every vector of \(T_yY\) lifts to a tangent vector of that component. Thus its germ lies in \(T_Y^*X\). Both smooth manifolds have complex dimension \(n\), so the inclusion is open near \(p\) and their germs agree. Removing other components ensures

\[
\operatorname{SS}(F)\subset T_Y^*X\quad\text{near }p.
\tag{14}
\]

The current bounded object-model contract LFI9–LFI10 now gives

\[
F\simeq M_Y\quad\text{in }D^b(k_X;p)
\tag{15}
\]

for some bounded \(k\)-complex \(M\), where \(M_Y\) means the local constant complex on \(Y\), extended by zero. This is a local statement; it does not make \(F\) globally constant on \(Y\).

Suppose \(p\ne0\), translate its base to zero, and choose adapted holomorphic coordinates with

\[
Y=\{z_1=\cdots=z_c=0\},\qquad
p=(0;dz_1),\qquad c\geq1.
\tag{16}
\]

The nonzero normal covector can be made the first coordinate differential by an invertible complex change of normal coordinates. Use

\[
h(z)=z_1+\sum_{j=c+1}^{n}z_j^2,
\qquad dh_0=dz_1.
\tag{17}
\]

This is regular on \(X\), whereas its restriction to \(Y\) is the standard quadratic on \(d=n-c\) variables. The proper closed-embedding cycle comparison, applied to \(Y\hookrightarrow X\), and (9) give

\[
\phi_h(M_Y)_0\simeq M[-(n-c)]=M[c-n].
\tag{18}
\]

When \(c=n\), the restriction is zero on the point \(Y\); the separate dimension-zero calculation gives \(M\), in degree zero, exactly as (18) says. By (12)–(13),

\[
\phi_h(F)_0\simeq M[c-n].
\tag{19}
\]

No finite-rank or perfectness assumption enters this detection. If the test is zero, the invertibility of a cohomological shift gives \(M=0\). Formula (15) then makes \(F\) zero in \(D^b(k_X;p)\). The quotient/null criterion MC.2 implies \(p\notin\operatorname{SS}(F)\).

The model degree depends on the complex dimension \(n-c\) of \(Y\). The quadratic calculation and proper cycle comparison give \(M[c-n]\), including the dimension-zero calibration above. The criterion needs detection of a nonzero coefficient complex, and (18) supplies it in every codimension.

## The uniform holomorphic criterion

**Theorem.** For \(F\in D^b_{w\text{-}\mathbb C\text{-}c}(k_X)\) and \(p\in T^*X\), the following are equivalent:

1. \(p\notin\operatorname{SS}(F)\).
2. There is an open cotangent neighborhood \(V\) of \(p\) such that every local holomorphic \(h\), defined near any \(x\), with \(h(x)=0\) and \((x;dh_x)\in V\), satisfies \(\phi_h(F)_x=0\).

The forward implication was proved using the closed support bound in the preceding lesson. For the reverse implication, retain the neighborhood \(V\) in condition 2. First let

\[
B=\{x\in X:(x;0)\in V\}.
\tag{20}
\]

This is open. The test \(h=0\) at each \(x\in B\) has empty nearby inverse image and \(\phi_0(F)_x=F_x\). Condition 2 gives \(F|_B=0\), so no microsupport lies over \(B\). In particular there are no zero covectors in \(\Lambda\cap V\).

If \(\Lambda\cap V\) were nonempty, it would be a relatively open subset of the analytic Lagrangian set \(\Lambda\), and would meet the dense generic set used for (14). Choose such a point \(p'\in\Lambda\cap V\). It is nonzero by the preceding paragraph. The test (17), with \(dh_0=p'\), belongs to the required family. Its vanishing stalk is zero by condition 2. Formula (19) gives \(M=0\), and the null criterion gives \(p'\notin\Lambda\), a contradiction. Hence \(\Lambda\cap V=\varnothing\), and in particular \(p\notin\Lambda\).

The use of a dense generic set requires the whole open cotangent neighborhood in the theorem. Vanishing of one test at one covector would not supply the contradiction at a nearby generic point. Closed microsupport and analytic generic density ensure that every nonempty relatively open part is tested, including neighborhoods of singular points of \(\Lambda\).

## Exercises with complete solutions

### Real coordinates of a complex quadratic fibre

*Difficulty: Introductory.*

For \(Q\) in dimension \(d\geq1\) and a positive real value \(r\), derive (4)–(5). Construct the deformation retraction explicitly, and explain the dimension-one case.

**Solution.** Expanding \(Q(x+iy)\) gives \(|x|^2-|y|^2+2i x\cdot y\). Setting it equal to \(r\) gives \(|x|^2=r+|y|^2\) and \(x\cdot y=0\), so \(u=x/\sqrt{r+|y|^2}\) is a unit vector and \(y\in u^\perp\). The ball condition is \(r+2|y|^2<\epsilon^2\). The path \(y_t=t y\), \(x_t=\sqrt{r+t^2|y|^2}\,u\), preserves these equations and reduces the norm. At \(t=0\) it gives \(\sqrt r\,u\) and fixes the zero-disc section. In dimension one, \(u\) has the two values \(\pm1\), and its orthogonal complement is zero; the fibre is precisely two points. No positive-dimensional tangent disc is present.

### Coefficient degrees in dimensions zero through three

*Difficulty: Intermediate.*

For any bounded \(M\), list the central nearby unit and vanishing complex for \(d=0,1,2,3\). Locate the two shifts that produce the degree in (9).

**Solution.** At \(d=0\), the nearby complex is zero and \(\phi=M\). At \(d=1\), it is \(M^2\) with diagonal unit, and \(\phi=M[-1]\). At \(d=2\), sphere cochains have \(M\) in degree zero and \(M[-1]\) in the reduced summand; the unit is the constant summand, and \(\phi=M[-2]\). At \(d=3\), the reduced summand is \(M[-2]\), giving \(\phi=M[-3]\). The sphere's reduced cochain complex contributes \([1-d]\); the definition of \(\phi\) contributes \([-1]\). The first step is finite free and works for arbitrary modules in \(M\). Choosing a sphere basepoint splits the constant summand when needed; the calculation of its cone does not require a canonical global splitting.

### Odd-dimensional sign in characteristic two

*Difficulty: Intermediate.*

Compute the vanishing monodromy for \(d=1,2,3\) over \(\mathbb Z\), and then over \(\mathbb F_2\). Does trivial monodromy imply a zero vanishing object?

**Solution.** Over \(\mathbb Z\), the signs are respectively \(-1,+1,-1\), by the antipodal degrees in (10). Over \(\mathbb F_2\) all three signs become \(+1\). The vanishing objects are still \(M[-1],M[-2],M[-3]\). With \(M=\mathbb F_2\) each is nonzero. Even over \(\mathbb Z\), dimension two gives nonzero vanishing with identity monodromy. Thus identity monodromy does not detect the zero object. The source-normalized shift remains the same in either characteristic.

### Infinite coefficients pass the same quadratic test

*Difficulty: Intermediate.*

Use \(k=\mathbb Q\), \(M=\bigoplus_{r\geq1}\mathbb Q\), and \(d=2\). Compute the vanishing object and explain precisely why the argument did not require a finite-dimensional Künneth theorem.

**Solution.** The result is \(M[-2]\) at zero and zero elsewhere on \(Q^{-1}(0)\). The covered ball retracts to a contractible halfplane times \(S^1\). Constant-coefficient sphere cochains are represented by a finite free cellular complex, and its augmented reduced part is \(k[-1]\). Tensoring that finite free model with the arbitrary module \(M\), then applying the defining \([-1]\), gives \(M[-2]\). No infinite tensor/product interchange occurs. Its nonzero stalk is not perfect over \(\mathbb Q\), but it is weakly complex constructible, which is the theorem's coefficient scope.

### Denominator cones need not be complex constructible

*Difficulty: Advanced.*

Suppose \(A\simeq B\) in \(D^b(k_X;p)\), with \(A,B\) weakly complex constructible, and \(p=(x;dh_x)\ne0\) for a regular holomorphic \(h\). Prove that their \(\phi_h\) stalks agree without imposing constructibility on any cone in a fraction representing the isomorphism.

**Solution.** Every denominator has a cone \(C\) with \(p\notin\operatorname{SS}(C)\). The arbitrary bounded support estimate for \(\mu_T C\), \(T=h^{-1}(0)\), makes its stalk at \(p\) zero. The exact functor \(A\mapsto(\mu_TA)_p\) therefore sends every denominator to an isomorphism. It induces a functor on the quotient, so the localized isomorphism gives equal test objects. The conormal section comparison identifies those two endpoint test objects with \(\phi_h(A)_x\) and \(\phi_h(B)_x\). That identification is used on the two constructible endpoints only. No hypothesis or cycle comparison for the intermediate cones was needed.

### Codimension changes the model's cycle degree

*Difficulty: Advanced.*

In \(X=\mathbb C^4\), take \(Y=\{z_1=z_2=0\}\), \(F=M_Y\), and \(h=z_1+z_3^2+z_4^2\). Compute \(\phi_h(F)_0\). Repeat for \(Y=\{0\}\subset\mathbb C^2\) and \(h=z_1\). Compare with a degree depending only on the ambient dimension.

**Solution.** The closed embedding is proper, and \(h|_Y\) is a quadratic on two complex variables. Its cycles therefore give \(M[-2]\), with identity monodromy, at the origin. The formula \(M[c-n]\) has \(c=2,n=4\), agreeing. In the second example, the restriction to the point is zero; its nearby object is zero and its vanishing object is \(M\) in its original degrees. Here \(c=n=2\). A proposed \(M[1-n]=M[-1]\) would put a degree-zero nonzero coefficient in degree one, contradicting the defining triangle. This hypothetical dimension-only formula fails that calibration; the detection required by the criterion uses the proved codimension-dependent degree.

### Why an open family is stronger than one test

*Difficulty: Advanced.*

Assume \(1_k\ne0\). For \(F=k_X\), compare a regular holomorphic test at a point with the zero-function test. Then explain where the full open cotangent family enters the reverse proof for arbitrary weakly complex constructible \(F\).

**Solution.** A regular test has nonzero derivative outside the constant sheaf's zero-section microsupport, so its vanishing stalk is zero. This single vanishing test does not imply that \(F\) is zero nearby or that its zero covectors are absent. The test \(h=0\) has \(\phi_0(F)=F\), so every neighborhood of a zero covector contains a nonzero vanishing test. In the reverse proof, the constant test first excludes all zero covectors in the chosen neighborhood. If microsupport still meets that neighborhood, relative openness and generic density produce a nonzero generic conormal point inside it. The adapted quadratic test has exactly that point as its derivative and must vanish by the whole-family hypothesis. Its coefficient detection contradicts membership in microsupport. The proof cannot replace this open-family condition by a single prescribed test at an arbitrary singular covector.

## Scope of the proof

The quadratic calculation fixes the coefficient degree and deck action. The generic conormal model, arbitrary-cone microlocal transfer and zero-function test then prove both directions of the uniform holomorphic criterion under the named prerequisite theorems. [Vanishing cycles as positive real support](vanishing-cycles-as-positive-real-support.html) supplies a complementary support calculation and explains why weak real constructibility alone does not suffice.

## References

Masaki Kashiwara, *Index theorem for constructible sheaves*, [Astérisque 130 (1985), pp. 193–209, Lemma 5.2 on p. 201](https://www.numdam.org/item/AST_1985__130__193_0/), states the local closed-support degree for a nondegenerate real quadratic with vector-space coefficients. Fernandes, Kudomi and Takeuchi, *Characteristic cycles of real and complex constructible sheaves, revisited*, [arXiv:2603.14821v2, proof of Theorem 5.5, (5.13)–(5.17)](https://arxiv.org/abs/2603.14821v2), uses the complex dimension of the stratum in the quadratic degree. That proof imports its generic microlocal coefficient model; it does not prove the broader object-model prerequisite used here.

Our calculation (2)–(10) uses an explicit covered ball, compatible retractions, finite free reduced sphere cochains and the deck action. It establishes the arbitrary-module degree and monodromy relative to the stated sheaf/cochain comparison. The subsequent criterion additionally requires the arbitrary-cone support estimate, microlocal quotient property, analytic generic conormal geometry and coefficient model specified in (11)–(19). Those prerequisites cannot be inferred from either reference. See the [source and proof guide](source-and-proof-guide.html) for their separation from the quadratic calculation.


# Vanishing cycles as positive real support

For a holomorphic function and a weakly complex constructible sheaf, vanishing cycles can be computed by local cohomology with support in its closed positive real halfspace. The comparison is an actual coefficient-triangle map. Its proof compares the lifted punctured neighborhood with one negative sector, using the local pushforward theorem over a complex curve.

Let \(k\) be a commutative ring of finite global dimension, \(X\) a complex manifold that is Hausdorff and countable at infinity, and \(f:X\to\mathbb C\) holomorphic. Put

\[
Y=f^{-1}(0),\quad i:Y\hookrightarrow X,\qquad
A=\{x:\operatorname{Re}f(x)<0\},\qquad
H=\{x:\operatorname{Re}f(x)\geq0\}.
\tag{1}
\]

The input \(F\in D^b_{w\text{-}\mathbb C\text{-}c}(k_X)\) may have infinite coefficient modules. We will prove a natural isomorphism

\[
i^{-1}R\Gamma_HF\simeq\phi_f(F),
\tag{2}
\]

with the source convention \(\phi_f(F)=\operatorname{Cone}(i^{-1}F\to\psi_f(F))[-1]\). The fibre \(Y\) may be singular and \(df\) may vanish. Properness of \(f\) is not assumed.

The local complex-curve pushforward theorem applies on a ball intersected with a sufficiently small inverse-image target neighborhood. Contractible-fibre descent uses the whole-complex theorem `SH02-CON-CYLINDER`. These inputs retain their analytic, conic, sheaf-operation and boundedness hypotheses.

*Original lesson text and solutions: CC0 1.0 Universal. Human mathematical sources are credited below.*

## The normalized negative sector supplies a coefficient map

Use the fixed cover from the monodromy lesson,

\[
p:\mathbb C_w\longrightarrow\mathbb C,
\qquad p(w)=e^{2\pi iw},\qquad
\widetilde U=X\times_{\mathbb C}\mathbb C_w,
\quad q:\widetilde U\longrightarrow X.
\tag{3}
\]

Its image is \(X\setminus Y\). Write \(L_f=q_!k_{\widetilde U}\). The proper-support trace \(\operatorname{tr}:L_f\to k_X\) sums the finitely supported sheet coefficients. It gives the coefficient complex

\[
K_f=[L_f\xrightarrow{\operatorname{tr}}k_X],
\quad\text{in degrees }-1,0,
\qquad
\phi_f(F)=i^{-1}R\mathcal Hom(K_f,F).
\tag{4}
\]

Let \(N=\{\lambda:\operatorname{Re}\lambda<0\}\). It has the normalized argument in \((\pi/2,3\pi/2)\), so the strip

\[
S=\{w:1/4<\operatorname{Re}w<3/4\}
\tag{5}
\]

maps homeomorphically onto \(N\). This fixes the lift of the negative sector, with \(-1\) lifted to \(1/2\), in the cover convention (3). Its pullback to \(X\) is an open subset \(\widetilde A\subset\widetilde U\) mapped homeomorphically by \(q\) onto \(A\).

Extend its constant coefficient by zero into \(\widetilde U\) and apply \(q_!\). The resulting map is

\[
\alpha_f:k_A\longrightarrow L_f,
\qquad \operatorname{tr}\circ\alpha_f:k_A\longrightarrow k_X.
\tag{6}
\]

The composite is the ordinary open-extension inclusion. Let \(C_f=[k_A\to k_X]\), again in degrees \(-1,0\). Open–closed localization gives \(C_f\simeq k_H\), in degree zero. The coefficient morphism

\[
C_f\longrightarrow K_f=(\alpha_f,\mathrm{id})
\tag{7}
\]

induces, by contravariant internal Hom and restriction to \(Y\),

\[
\phi_f(F)\longrightarrow i^{-1}R\Gamma_HF.
\tag{8}
\]

It is a natural map of the two defining fibre triangles. Their middle term is \(i^{-1}F\), with the identity map. On their other terms it is

\[
\beta_F:
\psi_f(F)=i^{-1}Rq_*q^{-1}F
\longrightarrow i^{-1}Rj_*j^{-1}F,
\qquad j:A\hookrightarrow X.
\tag{9}
\]

The cover adjunction and the open-set Hom interpretation identify this map with ordinary restriction from the entire lifted punctured neighborhood to \(\widetilde A\). The trace square in (6) makes it commute with the central unit. Thus proving (9) to be an isomorphism proves (8) to be an isomorphism, whose natural inverse is (2). No additional shift can enter this fibre-triangle comparison.

## Local curve pushforwards give a cofinal family of balls and target discs

Fix \(x\in Y\), choose a relatively compact holomorphic coordinate chart around \(x\), and translate \(x\) to zero. The centered-ball germ theorem of the complex-curve lesson supplies arbitrarily small source radii \(r\) and target neighborhoods \(D\ni0\) for which

\[
V=B_r(x)\cap f^{-1}(D),\qquad
G_V=R(f|_V)_*(F|_V)
\tag{10}
\]

is bounded weakly complex constructible on \(D\). This includes critical functions and arbitrary weak coefficients. The theorem's proof chooses radii below the first positive selected central critical value and a compact cutoff band; it works at arbitrarily small radii. Its repaired reciprocal exhaustion verifies every finite closed-level properness condition. We need the ordinary direct image in (10).

On a complex curve, weak complex constructibility makes the cohomology locally constant away from a locally finite set of points. Shrink \(D\) to a small centered disc so that the only possible exceptional point of \(G_V\) in that disc is zero. Restricting the target disc also restricts \(V\); ordinary open-base restriction commutes with direct image, so (10) and its statement remain valid. We obtain nested cofinal neighborhoods

\[
V_a=B_{r_a}(x)\cap f^{-1}(D_{\delta_a}),
\quad r_a\downarrow0,\quad\delta_a\downarrow0,
\qquad G_a=R(f|_{V_a})_*(F|_{V_a}),
\tag{11}
\]

with \(G_a\) cohomologically locally constant on \(D_{\delta_a}^*\). Choose each next radius and disc inside the previous ones; the curve theorem and open target restriction permit this. The \(V_a\) are open neighborhoods of \(x\), are contained in shrinking coordinate balls, and are therefore cofinal in the ordinary neighborhood system.

It is not required that \(f(B_{r_a})\subset D_{\delta_a}\). The actual domain in (11) is the intersection. The curve theorem applies to this intersection, and these intersections supply the cofinal source neighborhoods used below.

## The actual cover-to-sector restriction is an isomorphism

Let

\[
P_a=\{w:|e^{2\pi iw}|<\delta_a\},
\qquad S_a=P_a\cap S.
\tag{12}
\]

The cover \(P_a\to D_{\delta_a}^*\) is a local homeomorphism, \(P_a\) is an open halfplane, and \(S_a\) is an open half-strip. Each is diffeomorphic to \(\mathbb R^2\). The latter maps homeomorphically onto \(D_{\delta_a}\cap N\).

Ordinary base change along a local homeomorphism is valid for any map in the other direction. To check its actual morphism, restrict to an evenly covered target open set and one sheet, where the base map is a homeomorphism. The two preimages and their restriction maps identify, so open-base restriction of derived direct image gives the isomorphism there. These local identifications prove the global base-change morphism; they use no properness assertion.

Apply this to \(f|_{V_a}\) over the punctured disc. Direct-image composition and open restriction give natural identifications

\[
\begin{aligned}
R\Gamma(q^{-1}V_a;q^{-1}F)
&\simeq R\Gamma(P_a;p^{-1}(G_a|_{D_{\delta_a}^*})),\\
R\Gamma(V_a\cap A;F)
&\simeq R\Gamma(S_a;p^{-1}(G_a|_{D_{\delta_a}^*})|_{S_a}).
\end{aligned}
\tag{13}
\]

The identifications carry the restriction in (9) to restriction from \(P_a\) to \(S_a\), by their open-set and base-change naturality.

The coefficient \(p^{-1}(G_a|_{D_{\delta_a}^*})\) has locally constant cohomology on the simply connected \(P_a\). Choose any \(w_a\in S_a\). The cylinder descent contract, iterated on two real coordinates after product identifications of \(P_a,S_a\), gives isomorphisms from both section complexes to evaluation at \(w_a\). They commute with the actual restriction map. Consequently

\[
R\Gamma(q^{-1}V_a;q^{-1}F)
\longrightarrow R\Gamma(V_a\cap A;F)
\quad\text{is an isomorphism.}
\tag{14}
\]

This uses the whole bounded complex, not only its separate cohomology modules, and does not impose finite generation. Nontrivial monodromy on the punctured target disc remains allowed; both evaluation arguments take place on the contractible cover and its selected strip.

Take the filtered stalk system over the cofinal \(V_a\). The two systems in (14) compute the stalks of \(Rq_*q^{-1}F\) and \(Rj_*j^{-1}F\) at \(x\). Their maps are the restrictions induced by the globally defined coefficient branch (6), so they commute with all smaller-neighborhood restriction maps. Exact filtered colimits on cohomology show that \((\beta_F)_x\) is an isomorphism. Since this holds at every \(x\in Y\), (9) is an isomorphism on \(Y\). The fibre-triangle map (8) is then an isomorphism, proving (2).

The auxiliary coordinate balls, discs and evaluation points prove that a previously defined natural map is invertible. They are not part of its definition. The branch normalization is part of the fixed covering convention: translating the strip by an integer gives the corresponding deck-translated comparison. With (3)–(5) fixed, (2) is natural in \(F\).

## Endpoints, coefficients and critical functions

The support in (2) is the closed halfspace, with \(\operatorname{Re}f=0\) included. Its complementary sector is the strictly negative halfplane. It is local cohomology \(R\mathcal Hom(k_H,F)\), not ordinary restriction of \(F\) to \(H\) extended by zero, and not compactly supported cohomology of \(H\).

If \(F\) has perfect stalks, its cycles are perfect complex constructible by the preceding section theorem. The comparison therefore also proves that the restricted support object in (2) has perfect stalks. The proof of invertibility itself retains arbitrary weak coefficients throughout. For \(f=0\), the two negative-sector and punctured-cover objects are zero, so the comparison is the identity on \(F\). No regular-fibre hypothesis was used.

## Exercises with complete solutions

### The ball must be read over a smaller target germ

*Difficulty: Intermediate.*

For \(f(z_1,z_2)=z_1\) and \(F=k_{\{z_2=z_1\}}\), compute the image of the support inside a ball of radius \(r\). Explain why the proof uses \(B_r\cap f^{-1}(D_\delta)\), and why neighborhoods of this form with \(r\to0\) are cofinal at zero.

**Solution.** On the support, the squared norm is \(2|z_1|^2\), so the support in the open ball maps to \(D_{r/\sqrt2}\). The entire ball maps to \(D_r\). Ordinary pushforward of the support's open disc, viewed on a target containing \(D_r\), acquires a real circle boundary at radius \(r/\sqrt2\); it is not weakly complex constructible across that boundary. On a smaller disc \(D_\delta\) with \(\delta<r/\sqrt2\), the source intersection's support instead projects homeomorphically onto all of that target disc, with constant coefficient. There is no need to include the whole ball in its target inverse image. Each \(B_r\cap f^{-1}(D_\delta)\) contains zero, is open, and is contained in \(B_r\); shrinking radii makes such neighborhoods cofinal regardless of the relative rate of shrinking \(\delta\).

### A nontrivial local system still restricts from cover to sector

*Difficulty: Intermediate.*

Let \(k=\mathbb Q\), \(j_0:\mathbb C^*\hookrightarrow\mathbb C\), and \(F=j_{0!}\mathcal L\), where the rank-one local system has deck monodromy \(2\). For \(f(z)=z\), compute the restricted closed-halfspace support object at zero. Identify it with the vanishing object and explain the role of the negative-sector branch.

**Solution.** The central stalk of \(F\) is zero. Its ordinary cohomology on a small negative half-disc is \(\mathbb Q\) in degree zero, since the sector is contractible and \(\mathcal L\) restricts to a constant local system there. The support triangle gives \((R\Gamma_{\{\operatorname{Re}z\geq0\}}F)_0=\mathbb Q[-1]\). Cover descent gives nearby \(\mathbb Q\) with deck automorphism \(2\), and the source-normalized vanishing object is the same \(\mathbb Q[-1]\). The strip \(1/4<\operatorname{Re}w<3/4\) identifies the actual restriction map with the sector evaluation. Translating it by an integer applies deck transport to that identification; it does not make the local system's monodromy trivial.

### Ramification produces several negative sectors

*Difficulty: Intermediate.*

Take \(f(z)=z^m\), \(m\geq1\), and the constant complex \(M_{\mathbb C}\) for arbitrary bounded \(M\). Compute the negative-sector extension stalk and the positive-real-support object at zero. Check the cycle comparison even when the coefficient ring has characteristic dividing \(m\).

**Solution.** The set \(\operatorname{Re}z^m<0\) has \(m\) open sectors in a small punctured disc. Each is contractible, so the extension stalk is \(M^m\), and the unit \(M\to M^m\) is diagonal. The diagonal has a splitting given by projection to its first component, and its quotient complex is \(M^{m-1}\), for instance through the differences from that component. Thus the support fibre is \(M^{m-1}[-1]\). The nearby cover also has \(m\) components, the same diagonal unit, and cyclic deck permutation; its vanishing object agrees. No division by \(m\) is used. The comparison therefore remains valid in every characteristic and for nonperfect \(M\). For \(m=1\) both vanish.

### The real quadratic support has the complex dimension degree

*Difficulty: Intermediate.*

Let \(M\in D^b(k)\) and \(F=M_{\mathbb C^d}\). For \(Q(z)=\sum_{j=1}^d z_j^2\), write the negative real-part region in real coordinates and compute its augmented cochains near zero. Recover the degree of the quadratic vanishing object, including \(d=0\).

**Solution.** With \(z=x+iy\), the negative region is \(|x|^2<|y|^2\). In a punctured small ball, sending \(x\) to zero preserves the inequality and reduces the norm. The remaining nonzero \(y\) ball retracts onto \(S^{d-1}\); the radial retraction can be chosen on a fixed smaller radius, and its cohomology maps agree as neighborhoods shrink. The central unit is the constant-cochain map \(M\to R\Gamma(S^{d-1};M)\). Its cone is \(M[1-d]\), and the support triangle's \([-1]\) gives \(M[-d]\), agreeing with the full covered quadratic calculation. For \(d=0\) the negative set is empty, so the support object is \(M\) directly. The real ambient dimension \(2d\) does not replace the negative-direction count \(d\).

### Central support and infinite normal constants

*Difficulty: Intermediate.*

Check (2) for \(f=0\), for a sheaf complex supported on \(Y\), and for \(f(v,y)=v\) with \(F\) the normal-constant family of \(\bigoplus_{r\geq1}\mathbb Q\) over \(\mathbb Q\). Explain the closed endpoint.

**Solution.** If \(f=0\), then \(H=X\), the punctured and negative sets are empty, and both sides of (2) are \(F\). If \(F\) is supported on \(Y\), its restriction to \(A\) and to the cover is zero, so again the support and vanishing objects are \(i^{-1}F\), in their original degrees. Removing the boundary from \(H\) would give zero for the support Hom to such a central complex, since the open coefficient has zero stalk along \(Y\). For the normal-constant infinite family, both the cover and the negative half-disc have whole derived evaluation equal to the infinite module, and the central unit is the identity. Both fibre terms vanish. The argument retains the infinite coefficient, with no perfectness claim.

### Weak real constructibility does not suffice

*Difficulty: Advanced.*

Over a field, let \(F=k_{[0,\infty)}\) on \(\mathbb C\), the closed positive real ray, and let \(f(z)=z\). Compare its positive-real-support stalk at zero with its source-normalized vanishing object. Locate the hypothesis that fails in the proof.

**Solution.** The support of \(F\) is contained in \(\{\operatorname{Re}z\geq0\}\), so local cohomology with that closed support is \(F\), with stalk \(k\) at zero. Its lifted punctured ray has countably many components. A small lifted punctured neighborhood has ordinary section complex \(P=\prod_{n\in\mathbb Z}k\) in degree zero. The central unit is the diagonal \(k\to P\), and the vanishing object is \((P/k\mathbf1)[-1]\), which is nonzero in degree one. It cannot be isomorphic to the support stalk \(k\) in degree zero. The sheaf is weakly real constructible but not weakly complex constructible. Its curve pushforward for the identity function still has a real ray stratum in every punctured disc, so the cohomological local constancy required in (11) fails. Correspondingly, restriction from the cover to the negative sector is \(P\to0\), not an isomorphism.

## Scope of the result

The normalized branch makes the comparison compatible with the central unit; its map of fibre triangles identifies positive real support with the chosen vanishing-cycle normalization. The proof permits all bounded weakly complex constructible coefficients, critical functions and singular zero fibres. The last example shows exactly where complex constructibility is needed.

## References

David B. Massey, *Notes on Perverse Sheaves and Vanishing Cycles*, [arXiv:math/9908107v13, §3, the nonnegative-real-part support comparison](https://arxiv.org/abs/math/9908107v13), credits the construction to Kashiwara and Schapira and states its agreement with his shifted vanishing object. His shifted object agrees with the convention used here. This is a source for the comparison and its historical attribution; its constructible coefficient scope and brief cone description do not supply the full weak-coefficient argument.

The proof above identifies a particular map by fixing a covering strip, follows the unit into the closed-support triangle, and establishes cofinal shrinking neighborhoods before applying complex-curve and cylinder results. These are the steps needed for the stronger formulation, including arbitrary bounded coefficients and critical functions. The complex-curve theorem, full-complex descent and sheaf-operation inputs remain named programme prerequisites. The [source and proof guide](source-and-proof-guide.html) records them separately from the checked source passage.


# Sources, calculations and prerequisite proofs

The six readings study one question from three directions: what survives near a zero fibre, how it changes under a map, and how it detects a cotangent direction. Their proofs use a fixed coefficient complex and explicit comparison maps. The distinction between a calculation performed here and a prerequisite theorem matters, especially for infinite coefficient modules.

## Start with calculations that fix the conventions

Begin with the finite-support sequence calculation in [the two monodromy triangles](nearby-cycles-and-the-two-monodromy-triangles.html). Compute ramification before using a geometric comparison: it checks the diagonal unit and the two composites (1-M). The product–stalk example explains why a countable-cover argument needs a common system of shrinking neighborhoods.

Next, [proper pushforward](proper-pushforwards-of-nearby-and-vanishing-cycles.html) follows one closed support carrier through internal Hom and base change. Its graph application is the passage from a critical function to a regular ambient coordinate. [Normal deformation](nearby-cycles-through-the-normal-deformation.html) instead compares the actual covers through the logarithmic lift. Its closed-ray example records what weak real constructibility permits before complex constructibility is imposed.

The [normal and conormal section](complex-nearby-cycles-as-normal-and-conormal-sections.html) argument adds complex scaling, an endpoint-sensitive polar calculation and a specified slit. [Quadratic tests](quadratic-cycles-and-the-holomorphic-microsupport-test.html) then compute a sphere, its reduced cochains and its antipodal action before using a microlocal coefficient model. Finally, [positive real support](vanishing-cycles-as-positive-real-support.html) compares the same cycle convention with a closed halfspace using a normalized branch. Its ramification and closed-ray examples distinguish the roles of a branch, the cycle shift and complex constructibility.

## What the checked human sources supply

- David B. Massey, [*Notes on Perverse Sheaves and Vanishing Cycles*, arXiv:math/9908107v13, 17 August 2025](https://arxiv.org/abs/math/9908107v13): §3 supplies traditional and coefficient-complex definitions, the corrected punctured trace, cycle triangles, the proper-map statement and the positive-real-support comparison. The historical credit to Kashiwara and Schapira is retained through Massey's account. His constructible setting does not by itself establish the weak-coefficient or proper-on-closed-support extensions in these lessons. The exact author TeX was checked against the official v13 source archive. The paper's stated terms are CC BY 4.0; no passage of its expression is reproduced here.
- Ren Fernandes, Kazuki Kudomi and Kiyoshi Takeuchi, [*Characteristic cycles of real and complex constructible sheaves, revisited*, arXiv:2603.14821v2, 10 July 2026](https://arxiv.org/abs/2603.14821v2): §2.4 defines specialization and microlocalization; (4.54) relates positive deformation to real nearby cycles. The proof of Theorem 5.5 provides a useful stratum-dimension calibration. Equations (5.42)–(5.43) state the regular-fibre conormal comparison by reference to an earlier work. These passages do not prove our full weak-coefficient comparisons, generic coefficient-model theorem or uniform holomorphic criterion. The exact v2 author TeX was checked; no source text or figure is reproduced.
- Masaki Kashiwara, [*Index theorem for constructible sheaves*, Astérisque 130 (1985), pp. 193–209](https://www.numdam.org/item/AST_1985__130__193_0/): Lemma 5.2 on printed p. 201 states the real quadratic local-support degree for vector-space coefficients. The displayed page was checked. Our arbitrary-module calculation uses its own finite free sphere-cochain model; the lemma is not cited as a proof of that extension. No page or source expression is included in the download.

## The proof obligations behind the comparisons

These readings contain the local comparison arguments and forty-one solved exercises. They are not a self-contained construction of the sheaf and microlocal foundations. In particular, the following inputs retain their full original scope:

| Application | Required programme input | What remains separate |
|---|---|---|
| Coefficient construction and pushforward | Ordinary and proper-support adjunction, tensor–Hom, proper-support base change and finite-dimensional cohomological bounds | The underlying resolution, derived-category and topology foundations; a bounded ordinary adjunction argument is included in the pushforward lesson |
| Countable-cover deformation | Whole-complex small-ball stabilization, weak inverse-image and internal-Hom properties, smooth base change and ordinary/punctured conic recovery | Uniform control of the shrinking neighborhoods; a formal interchange of a product and stalk colimit does not prove it |
| Normal and conormal sections | `SH02-CHE-001`, `SH02-CON-CYLINDER`, and `SH02-FS-SECTIONS` (FS13) | The analytic normal-cone estimate, full-complex cylinder descent and Fourier section theorem at the exact weak-coefficient scope |
| Uniform holomorphic detection | `SH02-LFI-SUPPORTED` (LFI9–LFI10), `SH02-MC-LOCAL` (MC.2), and `SH02-MO-MICROLOCAL-SUPPORT` (MO15), with the earlier complex-microsupport theorem | Generic coefficient objects, arbitrary denominator cones, the quotient/null criterion and singular analytic geometry |
| Positive-real-support comparison | The local complex-curve theorem, cylinder descent and support localization | Their exact bounded weak-coefficient versions; source statements with finite or field coefficients do not fill the gap |
| Covered quadratic computation | Sheaf/singular cochain comparison, constant-coefficient homotopy invariance and finite sphere cochains | The full topological providers, distinct from the explicit retraction and degree calculation |

Some of these prerequisite chains are still being reconstructed. The argument at each use retains its hypotheses and identifies the required theorem; inclusion in this selection does not certify that every transitive input is complete. No claim of full course completion follows from the checked source passages.

## Reuse

The independently written programme prose, calculations and solutions are dedicated to the public domain under [CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/). Cited human works keep their own terms. Source access, mathematical proof and permission to reproduce source expression are separate questions.
