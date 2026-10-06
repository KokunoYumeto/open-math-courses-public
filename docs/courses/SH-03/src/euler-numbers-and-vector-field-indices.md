# Euler numbers and vector-field indices

The Euler characteristic of a compact manifold can be computed from finite cells, from duality, or from intersections of a section with the zero section. These calculations explain both the vanishing in odd dimension and the Hopf index formula. Orientation lines let the same argument work on nonorientable manifolds.

*Written by GPT-6.1 Sol (OpenAI), Ultra, 2 October 2026. Author self-check recorded; not independently reviewed. New original text is public domain (CC0).*

Learn first Perfect coefficients on compact fibres for finite compact cohomology, and Constructible costalks and Verdier duality for the dualizing orientation complex and actual duality. Continuous sections and supported cycle intersections proves the section class and its complete supported comparison. Differential sections and proper-below Euler indices proves the compact index for every continuous section. Orientations of conormal cycles and transverse intersections fixes the integral normal-first coefficient and ordered transverse sign. These are written programme proofs relative to their stated foundations; compatible triangulation and other lower foundational obligations remain open.

Throughout, manifolds have no boundary. They are real analytic, Hausdorff and countable at infinity, with the standing finite dimension bounds. The compact manifold in the main theorems has dimension \(n\). The vector-field proof accepts smooth fields, and therefore includes every analytic field in the assigned exercise.

## Finite cells give an integer independent of the field

Let \(k\) be any field and \(X\) compact. Compact constructible finiteness makes the following sum finite:

\[
 \chi_k(X)=\sum_j(-1)^j\dim_k H^j(X;k_X).
 \qquad\text{(1)}
\]

For a finite-dimensional local system \(L\) of constant rank \(r\) on a connected \(X\), we claim

\[
 \chi(X;L)=r\sum_{\sigma}(-1)^{\dim\sigma}
           =r\,\chi_k(X).
 \qquad\text{(2)}
\]

**Proof.** Choose a finite compatible triangulation of the compact manifold and filter it by its closed skeleta. The difference between successive skeleta is a finite disjoint union of open simplices. The local system on each such simplex is constant of rank \(r\); compact sections are \(k^r[-\dim\sigma]\). The closed/open localization triangles and their finite compact-section long exact sequences make Euler characteristic additive.

Adding the open-simplex contributions gives the first equality in (2). Applying the same argument to \(k_X\) gives the second. Euler additivity is an integer identity: for a finite cochain complex, the dimensions of the image of each differential occur once in each adjacent degree and cancel. No reduction of integers into \(k\) is involved.

In particular \(\chi_k(X)\) is the same integer for every field \(k\). For a disconnected compact manifold, apply the formula on each component. There are finitely many components: components are open, and compactness gives a finite subcover of their cover of \(X\). \(\square\)

Rank controls the Euler characteristic of a local system; its monodromy can still change the individual cohomology groups.

## Duality forces vanishing in odd dimension

Write \(\operatorname{or}_{X,k}\) for the orientation local system. It has rank one, whether or not it is globally trivial. The manifold dualizing complex and compact dual-sections comparison give

\[
 D_Xk_X=\operatorname{or}_{X,k}[n],\qquad
 R\Gamma(X;D_Xk_X)
    \simeq R\operatorname{Hom}_k(R\Gamma(X;k_X),k).
 \qquad\text{(3)}
\]

The second comparison uses compactness of the coefficient support; ordinary and compact sections agree here. Both complexes are perfect.

Coefficient duality reverses the finite cohomology degrees without changing the Euler characteristic. A shift by \(n\) multiplies it by \((-1)^n\). Formula (2) gives the remaining equality:

\[
 \chi_k(X)
   =(-1)^n\chi(X;\operatorname{or}_{X,k})
   =(-1)^n\chi_k(X).
 \qquad\text{(4)}
\]

**Theorem.** A compact odd-dimensional manifold without boundary satisfies

\[
 \chi_k(X)=0\qquad\text{for every field }k.
 \qquad\text{(5)}
\]

**Proof.** For odd \(n\), equation (4) says \(2\chi_k(X)=0\) in \(\mathbb Z\), so \(\chi_k(X)=0\). The orientation local system was retained throughout. The calculation is valid also in characteristic two because the dimensions and their alternating sum are integers. \(\square\)

Equivalently, the compact constructible-function duality theorem gives
\(\int_XD_X1_X\,d\chi=\int_X1_X\,d\chi\), while
\(D_X1_X=(-1)^n1_X\). The finite-dimensional argument above explains why this is an integer equality over every field.

## Turn a vector field into an admissible section

Let \(v\) be a smooth vector field on \(X\). Choose a smooth positive definite metric \(g\), and lower its tangent index:

\[
 \sigma=g^\flat(v):X\longrightarrow T^*X,\qquad
 \sigma(x)(w)=g_x(v(x),w).
 \qquad\text{(6)}
\]

Here is an explicit existence argument for \(g\). Choose finitely many coordinate neighborhoods and smaller neighborhoods covering \(X\), with closures inside the larger charts. In each chart choose a nonnegative smooth bump supported in the larger neighborhood and positive on the smaller one. Divide these bumps by their everywhere-positive sum to obtain a finite smooth partition of unity. The weighted sum of the pulled-back Euclidean metrics is smooth and positive definite. Each weighted term extends by zero outside its chart. Thus no global analytic metric is needed.

The supported-section theorem accepts continuous sections, so the smooth section (6) lies in its actual domain. Positive definiteness gives \(\sigma(x)=0\) exactly when \(v(x)=0\).

Let \(0_X\subset T^*X\) denote the zero section. Its normalized integral cycle is denoted \(\lambda_0\). In base coordinates \(x\) and cotangent coordinates \(\xi\), its coefficient is

\[
 \operatorname{sgn}(dx_1\wedge\cdots\wedge dx_n)
   \otimes
 \operatorname{sgn}(d\xi_1\wedge\cdots\wedge d\xi_n).
 \qquad\text{(7)}
\]

This is the codimension-zero case of the normalized conormal formula. The two orientation signs change together under a chart reversal, so (7) is intrinsic even on a nonorientable \(X\). Extending this integral generator to \(\mathbb Q\) gives
\(\operatorname{CC}(\mathbb Q_X)\), with the preceding characteristic-cycle normalization.

For integral coefficients put \(M=T^*X\) and \(\pi:M\to X\). The actual section unit and the ordered cup have types

\[
 \begin{aligned}
 [\sigma]&\in H^0_{\sigma(X)}(M;\pi^!\mathbb Z_X),\\
 \lambda_0&\in H^0_{0_X}(M;\pi^{-1}\omega_{X,\mathbb Z}),\\
 [\sigma]\cap\lambda_0
   &\in H^0_{\sigma(X)\cap0_X}(M;\omega_{M,\mathbb Z}).
 \end{aligned}
 \qquad\text{(8)}
\]

The first unit is normalized by \(\sigma^!\pi^!\mathbb Z_X=\mathbb Z_X\) and the closed-embedding counit. The cup uses
\(\pi^!\mathbb Z_X\otimes^L\pi^{-1}\omega_{X,\mathbb Z}\to\omega_{M,\mathbb Z}\) in this order.

## Isolated zeros carry integer local numbers

Assume that the zero set \(Z(v)\) is finite. For a zero \(a\), restrict the class in (8) to a neighborhood meeting its support only at \((a,0)\). The normalized point trace defines

\[
 \operatorname{ind}_a(v)
   =\#([\sigma]\cap\lambda_0)_{(a,0)}
   \in\mathbb Z.
 \qquad\text{(9)}
\]

Open-extension composition proves independence of the chosen small neighborhood, exactly as in the supported-section lesson.

**Theorem.** For every smooth vector field on a compact \(X\) with finitely many isolated zeros,

\[
 \chi_k(X)=\sum_{a\in Z(v)}\operatorname{ind}_a(v)
             \qquad\text{for every field }k.
 \qquad\text{(10)}
\]

**Proof.** The intersection support in (8) is the finite set
\(\{(a,0):a\in Z(v)\}\). Supported excision into disjoint small neighborhoods splits the class into its finitely many point-supported classes. Composition of traces makes its total integral the sum in (10).

Extend the normalized local orientation generators to \(\mathbb Q\). Each point trace then sends its integral local number to the same number in \(\mathbb Q\). There is no assertion here that an unrestricted ordinary direct image under a nonproper projection commutes with scalar extension: the comparison is on the finite point supports and their normalized traces.

The rational zero cycle is \(\operatorname{CC}(\mathbb Q_X)\). The already proved compact continuous-section index therefore identifies this rational total with \(\chi_{\mathbb Q}(X)\). Both sides are integers, and \(\mathbb Z\to\mathbb Q\) is injective, so their equality is an integer equality. Formula (2) gives \(\chi_k(X)=\chi_{\mathbb Q}(X)\) for any field \(k\), proving (10). \(\square\)

An empty zero set is permitted. Its supported class and its finite sum are zero, so a nowhere-zero field forces \(\chi_k(X)=0\).

## The local determinant has no extra orientation sign

Suppose that \(a\) is a nondegenerate zero. Choose a chart centered at \(a\), and write
\(v(x)=Ax+O(|x|^2)\), with \(A\) invertible, for an analytic field. For a smooth field the differentiability remainder \(o(|x|)\) suffices.

The coordinate description of the smooth graph unit has the same orientation as the analytic graph calculation. Indeed the fibre translation
\(\eta=\xi-\sigma(x)\) has determinant one and

\[
 d\eta_1\wedge\cdots\wedge d\eta_n\wedge dx
     =d\xi_1\wedge\cdots\wedge d\xi_n\wedge dx
     =\Omega.
 \qquad\text{(11)}
\]

Every other term has an additional base differential and vanishes in the full wedge. The graph unit has its base tangent orientation tensored with the fibre orientation. This calculation needs neither symmetry of \(D\sigma\) nor an isotropic graph.

Let \(G=g(a)\) be the positive definite metric matrix and \(B=D\sigma(a)\). Differentiating \(g(x)v(x)\) gives \(B=GA\), since the term involving \(Dg\) is multiplied by \(v(a)=0\). In row order \((\xi,x)\), the tangent columns for the graph followed by the zero section give

\[
 B=GA,\qquad
 [\,V_{\mathrm{graph}}\ V_{\mathrm{zero}}\,]
      =\begin{pmatrix}B&0\\ I&I\end{pmatrix},
 \qquad
 \det\begin{pmatrix}B&0\\ I&I\end{pmatrix}=\det B.
 \qquad\text{(12)}
\]

The two submanifolds are transverse exactly when \(B\) is invertible. Their integral fibre coefficients pair to one. The ordered transverse formula with
\(\Omega=d\xi\wedge dx\) consequently gives

\[
 \operatorname{ind}_a(v)
    =\operatorname{sgn}\det B
    =\operatorname{sgn}\det A,
 \qquad\text{(13)}
\]

because a positive definite \(G\) has positive determinant. This uses the graph as the first input. Reversing the two inputs would contribute \((-1)^n\); replacing \(\Omega\) by the symplectic orientation would require the factor already computed in the orientation lesson.

The formula also verifies coordinate independence directly. For a coordinate change with Jacobian \(J\) at the zero,

\[
 A'=JAJ^{-1},\qquad
 B'=J^{-t}BJ^{-1}.
 \qquad\text{(14)}
\]

The derivative of \(J\) contributes nothing because \(v(a)=0\), and the base derivative of the cotangent transition contributes nothing because \(\sigma(a)=0\). Thus \(\det A'=\det A\), and \(\det B'=(\det J)^{-2}\det B\). Both signs are unchanged, including for a reversed chart. This agrees with the two simultaneous orientation changes in (7).

**Hopf index theorem.** If every zero of \(v\) is nondegenerate, then

\[
 \chi_k(X)=\sum_{a\in Z(v)}\operatorname{sgn}\det Dv(a).
 \qquad\text{(15)}
\]

This follows from (10) and (13). In particular it proves the assigned rational-coefficient theorem on compact analytic manifolds, and gives its integer equality over every field. For a zero-dimensional compact manifold, the empty determinant is one; every point is a zero and contributes one.

## A degenerate zero is read by its Thom pullback

The definition (9) remains valid when the derivative is singular. Its local computation can be made directly from the normalized zero-section Thom class. On a coordinate neighborhood \(U\) containing only one zero, the supported section comparison identifies the local number with the image of that class under

\[
 \sigma^*:H^n_{0_U}(T^*U;\pi^{-1}\operatorname{or}_{U,\mathbb Z})
       \longrightarrow H^n_{\{a\}}(U;\operatorname{or}_{U,\mathbb Z})
       \simeq\mathbb Z.
 \qquad\text{(16)}
\]

The class in the first group is its normalized fibre Thom unit. The support pulls back to \(\{a\}\); the final isomorphism is the point trace of
\(\omega_{U,\mathbb Z}=\operatorname{or}_{U,\mathbb Z}[n]\).
The full section-intersection theorem supplies this actual pullback comparison. Thus (16) is the local degree with the paired orientation coefficient, rather than a new scalar convention.

In dimension one, the local relative group is explicitly

\[
 H^1(I,I\setminus\{0\};\mathbb Z)
       =\mathbb Z^2/\mathbb Z(1,1).
 \qquad\text{(17)}
\]

The two coordinates refer to the left and right punctured intervals. An increasing local coordinate pulls the positive Thom generator to itself. If a function defining the section is positive on both punctured intervals, the induced pullback sends a pair \((c_-,c_+)\) to
\((c_+,c_+)\), which is zero in this quotient. Such a zero has index zero.

This description also proves independence of the chosen positive metric at an isolated zero. A convex interpolation of two positive metric matrices remains positive. The corresponding sections are nonzero away from the zero, so they give a homotopy of the same relative pair maps in (16). Relative cohomology pullback is unchanged: the usual prism homotopy for the interval gives a cochain homotopy between the two maps, and preserves the punctured subspace. Hence their local numbers agree. Global metric interpolation has exactly the same zero set.

## Exercises with complete solutions

### Monodromy changes cohomology without changing Euler characteristic
*Difficulty: Introductory.*

Let \(L\) be a rank-\(r\) local system on \(S^1\), with invertible monodromy matrix \(T\) over any field. Compute its Euler characteristic without assuming that \(T=I\).

**Solution.** Cutting at one vertex gives the two-term cochain complex
\(k^r\xrightarrow{T-I}k^r\), in degrees zero and one. Thus
\(H^0=\ker(T-I)\) and \(H^1=\operatorname{coker}(T-I)\). Rank-nullity gives equal dimensions for these two spaces, and their alternating sum is zero. If \(T-I\) is invertible, both vanish; if \(T=I\), both have dimension \(r\). Both cases have the same Euler characteristic, agreeing with \(r\chi(S^1)=0\).

### Characteristic two on a nonorientable three-manifold
*Difficulty: Intermediate.*

Let \(X=S^1\times\mathbb{RP}^2\). Over a field of characteristic two, use the usual one-cell-per-dimension cell structure on \(\mathbb{RP}^2\) to compute the cohomology dimensions of \(X\). Explain why the odd-dimensional vanishing is still an integer assertion.

**Solution.** The cellular differential on \(\mathbb{RP}^2\) has the integer boundary multiplication by two in the top cell and zero in the other positive degree. Over a characteristic-two field both differentials vanish, so the dimensions in degrees zero, one and two are \(1,1,1\). The circle has one-dimensional cohomology in degrees zero and one. Finite Künneth gives dimensions
\(1,2,2,1\) on \(X\), and Euler characteristic
\(1-2+2-1=0\) in \(\mathbb Z\).
The product is nonorientable: the circle's orientation line is trivial, while that of \(\mathbb{RP}^2\) is nontrivial integrally. Its sign representation becomes trivial in characteristic two. Neither change affects its rank-one Euler formula. A scalar equation \(2z=0\) in this field alone would give no vanishing conclusion; (4) is instead an equality of integer alternating dimensions.

### A rotating field has a positive index
*Difficulty: Intermediate.*

Near the origin of \(\mathbb R^2\), take
\(v(x,y)=(-y,x)\) and the Euclidean metric. Compute its local index and check whether the associated one-form is a differential.

**Solution.** The linearization is
\(\begin{pmatrix}0&-1\\1&0\end{pmatrix}\), with determinant one, so (13) gives index \(+1\). The lowered one-form is
\(-y\,dx+x\,dy\), whose exterior derivative is
\(2\,dx\wedge dy\), not zero. It is therefore not locally a differential. The graph need not be Lagrangian, yet its supported section unit and ordered intersection are valid. Restricting the Hopf proof to gradient fields would miss this example.

### A chart reversal and a positive metric
*Difficulty: Intermediate.*

At a planar saddle take
\(A=\operatorname{diag}(-1,1)\), metric matrix
\(G=\begin{pmatrix}2&1\\1&2\end{pmatrix}\), and coordinate reversal
\(J=\operatorname{diag}(-1,1)\). Compute the signs before and after the reversal.

**Solution.** The metric is positive definite: its eigenvalues are one and three. Its determinant is three. Hence
\(B=GA=\begin{pmatrix}-2&1\\-1&2\end{pmatrix}\) has determinant \(-3\), and the index is \(-1\).
The new tangent matrix is \(A'=JAJ^{-1}=A\). The new cotangent derivative is
\(B'=J^{-t}BJ^{-1}=\begin{pmatrix}-2&-1\\1&2\end{pmatrix}\), again with determinant \(-3\). The base and fibre orientation generators both reverse; their tensor coefficient is unchanged. A local maximum with \(A=-I\) in this same two-dimensional setting would instead have determinant \(+1\) and index \(+1\).

### The two zeros of a height gradient
*Difficulty: Intermediate.*

On the unit sphere \(S^2\subset\mathbb R^3\), take the round-metric gradient of the height function \(h(p)=p_3\). Find its zeros and local indices.

**Solution.** The tangent gradient is
\(v(p)=e_3-p_3p\). Its only zeros are the north and south poles. For a tangent displacement \(w\) at either pole, \(dp_3(w)=0\), so
\(Dv(w)=-p_3w\). At the north pole the matrix on the two-dimensional tangent plane is \(-I\); at the south pole it is \(I\). Both determinants are positive, so the sum of local indices is two. The sphere's zero- and two-dimensional cell structure gives \(\chi(S^2)=2\), as required. Reversing the vector field exchanges its maximum and minimum behavior but leaves both two-dimensional determinant signs positive.

### Three projective critical points on a nonorientable surface
*Difficulty: Advanced.*

For real numbers \(a_1<a_2<a_3\), let
\(h([x])=(a_1x_1^2+a_2x_2^2+a_3x_3^2)/(x_1^2+x_2^2+x_3^2)\)
on \(\mathbb{RP}^2\). Using its descended round metric, compute the indices of its gradient.

**Solution.** On the unit sphere the gradient is
\(2(\operatorname{diag}(a_1,a_2,a_3)x-h(x)x)\). It is antipodally equivariant and descends to the projective surface. Since the eigenvalues are distinct, its zeros are exactly the three coordinate axes. In an affine projective chart near the \(i\)-th axis, the Hessian at that critical point has diagonal entries
\(2(a_j-a_i)\) for \(j\ne i\). Lowering or raising indices by the positive metric preserves the determinant sign. The three signs are respectively \(+1,-1,+1\). Their sum is one, equal to the cell Euler characteristic \(1-1+1\) of \(\mathbb{RP}^2\). No orientation of this nonorientable surface was used to assign the local integers.

### A nowhere-zero field and a boundary counterexample
*Difficulty: Intermediate.*

Compare the constant nonzero field on the flat two-torus with the field \(\partial_t\) on the closed interval \([0,1]\). Explain which Euler conclusion the theorem permits.

**Solution.** The torus has no vector-field zeros, so (10) gives Euler characteristic zero. Its cell counts \(1,2,1\) confirm this. On the interval the constant field also has no zeros, but the interval is contractible and has Euler characteristic one. It has boundary and is outside the theorem's hypotheses. Thus the interval is not a counterexample to (10); it shows why a theorem allowing boundary would need boundary data and contributions. No such extension is being assumed here.

### A degenerate circle zero has index zero
*Difficulty: Advanced.*

On \(S^1\), in the standard periodic coordinate, take
\(v(t)=(1-\cos t)\partial_t\). Compute the local index of its unique zero and compare with the Euler characteristic.

**Solution.** The only zero is \(t=0\) modulo \(2\pi\). Its derivative vanishes, so the determinant formula for nondegenerate zeros does not apply. In a small punctured interval on both sides of zero the coefficient \(1-\cos t\) is positive. For the flat metric the lowered section has the same positive coefficient. Its Thom pullback in (17) sends every pair to a diagonal pair, so the local index is zero. The general isolated-zero formula (10) therefore gives \(\chi(S^1)=0\). This agrees with its two-term cellular calculation. A zero derivative alone would not determine this local index; the signs on the two punctured sides do.

## References

The vanishing of the Euler characteristic of a compact odd-dimensional manifold and the Hopf index formula for a nondegenerate vector field are classical; their sheaf-theoretic proofs here use the index theorem of M. Kashiwara, [*Index theorem for constructible sheaves*](https://www.numdam.org/item/AST_1985__130__193_0/), Astérisque 130 (1985). The proof retains orientation local systems, supplies the integer finite-cell comparison for all fields, and applies the supported-section and compact characteristic-cycle index diagrams of the preceding lessons. The local block determinant fixes the sign for arbitrary vector fields; the Thom pullback also explains the degenerate isolated-zero example.
