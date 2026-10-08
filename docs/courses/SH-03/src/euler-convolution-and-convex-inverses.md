# Euler convolution and convex inverses

Adding two vectors pushes a function on a product back to the original vector space. When the pushforward counts fibres by Euler characteristic, this gives a convolution algebra of integer-valued constructible functions. A nonempty compact convex set determines a unit in this algebra. Its inverse remembers reflection, relative dimension and open boundary conditions.

*Lesson text: CC0. Human-source references appear below.*

Learn first Constructible functions and Euler integration, especially its bounded realizations with prescribed closed support, proper-on-support pushforward, compact Euler integration and duality. Perfect operations and finite microlocal coefficients supplies the finite supported coefficient complexes. We use the ordinary finite tensor Künneth comparison and the point-costalk comparison from those lessons and their stated sheaf-operation prerequisites. For the geometric input, use Subanalytic triangulations on analytic manifolds. The arguments below use compatible finite triangulations on compact sets, closed/open localization, and the constant-sheaf comparison on locally contractible spaces.

## Addition is proper on the relevant support

Let \(E\) be a finite-dimensional real vector space. Constructible functions are integer-valued, with locally finite subanalytic level partitions. Their **closed support** is the closure of the nonzero locus. Write

\[
 \mathcal A(E)=\Gamma_c(E;\mathcal{CF}_E),\qquad
 s:E\times E\longrightarrow E,\quad s(u,v)=u+v.
 \qquad\text{(1)}
\]

The subscript \(c\) requires compact closed support. It permits indicators of bounded open sets as well as compact closed sets.

For \(\varphi,\psi\in\mathcal A(E)\), define

\[
 \begin{aligned}
 \varphi*\psi&=s_!(\varphi\boxtimes\psi),\\
 (\varphi*\psi)(x)&=\int_E\varphi(y)\psi(x-y)\,d\chi.
 \end{aligned}
 \qquad\text{(2)}
\]

The second formula identifies the fibre \(s^{-1}(x)\) with \(E\) by \(y\mapsto(y,x-y)\). Its integrand has compact closed support. If \(K,L\) are the respective compact closed supports, the product has support in \(K\times L\). Addition is proper on that compact set, so the previously proved support-proper theorem makes the result constructible, with closed support contained in the compact set \(K+L=s(K\times L)\). Properness of addition on all of \(E\times E\) is unnecessary.

For comparison with sheaves, choose any characteristic-zero field \(k\) and the preceding bounded constructible realizations \(F_\varphi,F_\psi\), with compact closed supports \(K,L\). Stalk Künneth and proper-support base change give

\[
 \varphi*\psi
   =\chi_E\!\left(Rs_!(F_\varphi\boxtimes^L F_\psi)\right).
 \qquad\text{(3)}
\]

Here \(\boxtimes^L\) is the derived external tensor product. Its stalks and all fibre section complexes in (3) are perfect. The compact-support Grothendieck isomorphism proves independence of the representatives. The resulting statements concern integer-valued functions and do not depend on the auxiliary field.

## One interval shows the boundary mechanism

Before treating arbitrary convex sets, take \(Z=[0,1]\) on the real line. A candidate for its convolution inverse is \(-1_{(-1,0)}\). Formula (2) makes their product at \(x\) equal to
\(-\chi_c([0,1]\cap(x,x+1))\).

At \(x=0\), this intersection is \((0,1)\), whose compact Euler characteristic is \(-1\). For \(0<x<1\), it is \((x,1]\); for \(-1<x<0\), it is \([0,x+1)\). Each half-open interval has compact Euler characteristic zero: remove one endpoint from a compact interval and apply the closed/open localization sequence, subtracting \(1\) from \(1\). At \(x=\pm1\), and outside \([-1,1]\), the intersection is empty. The product is therefore \(\delta_0\).

The open boundary and the minus sign do different jobs. The sign gives the value one at the origin, while the half-open fibres force the value zero at every other possible translation. The general inverse proof will recover this cancellation by projecting a boundary portion onto a compact convex set.

## Associativity, symmetry and the unit

Euler integration is additive in each variable, so convolution is bilinear over \(\mathbb Z\).

**Theorem.** The group \(\mathcal A(E)\), with convolution, is a commutative unital \(\mathbb Z\)-algebra.

**Proof.** Choose the compactly supported realizations \(F,G,H\) of the three functions. Put
\(b(u,v,w)=(u+v,w)\), \(a(u,v,w)=(u,v+w)\), and
\(\Sigma(u,v,w)=u+v+w\). Thus \(s\circ b=s\circ a=\Sigma\).
Proper base change in the product square, followed by the projection formula, gives
\(Rb_!(F\boxtimes^L G\boxtimes^L H)\simeq Rs_!(F\boxtimes^L G)\boxtimes^L H\).
Proper-support composition identifies its subsequent image under \(s\) with
\(R\Sigma_!(F\boxtimes^L G\boxtimes^L H)\). The corresponding product square for \(a\) identifies the other parenthesization with the same object.

These maps meet the support hypotheses: the initial closed coefficient support lies in \(K\times L\times M\), and the two intermediate supports lie in \((K+L)\times M\) and \(K\times(L+M)\). All three sets are compact. Taking stalk Euler numbers in these actual comparisons gives

\[
 ((\varphi*\psi)*\eta)(x)
  =\int_{E^2}\varphi(u)\psi(v)\eta(x-u-v)\,d\chi
  =(\varphi*(\psi*\eta))(x).
 \qquad\text{(4)}
\]

This iterated integration follows from the actual composition theorem, with compact supports at both stages.

The switch \((u,v)\mapsto(v,u)\) is an analytic isomorphism commuting with addition; its pushforward interchanges the two factors. Finally, a fibre weighted by the indicator of the origin contains the one relevant point. Thus

\[
 \varphi*\psi=\psi*\varphi,\qquad
 \delta_0*\varphi=\varphi,\qquad \delta_0=1_{\{0\}}.
 \qquad\text{(5)}
\]

These identities prove the theorem. \(\square\)

The compact Euler integral is an algebra homomorphism:

\[
 \epsilon(\varphi)=\int_E\varphi\,d\chi,\qquad
 \epsilon(\varphi*\psi)=\epsilon(\varphi)\epsilon(\psi),
 \qquad \epsilon(\delta_0)=1.
 \qquad\text{(6)}
\]

Indeed the map from \(E\times E\) to a point factors through \(s\). Proper-support composition and finite Künneth turn its section complex into
\(R\Gamma_c(E;F_\varphi)\otimes_k^L R\Gamma_c(E;F_\psi)\).
The Euler characteristic of this finite tensor complex is the product of the two Euler characteristics.

## The dual of a compact convex indicator

Write \(D_E\) for the function duality from Euler integration. Its value at a point is the Euler characteristic of the costalk of a constructible realization.

For a nonempty compact convex set \(Z\subset E\), let \(L=\operatorname{aff}(Z)\), let \(d=\dim L\), and write \(\operatorname{relint}Z\) for its interior in \(L\).

**Lemma.** If \(Z\) is also subanalytic, then

\[
 D_E1_Z=(-1)^d1_{\operatorname{relint}Z}.
 \qquad\text{(7)}
\]

**Proof.** A spanning simplex inside \(Z\) shows that \(Z\) has nonempty relative interior. For \(d=0\), it is a point. The costalk of its closed-supported constant sheaf is \(k\) in degree zero by closed-embedding adjunction. Suppose \(d>0\), choose \(o\in\operatorname{relint}Z\), and choose Euclidean coordinates on its affine span.

Every ray from \(o\) meets the relative boundary exactly once. Write that boundary point as \(o+R(u)u\), for a unit vector \(u\). The function \(R\) is positive, bounded and continuous. To check continuity, if \(u_j\to u\), compactness makes every limit of \(o+R(u_j)u_j\) belong to \(Z\), giving \(\limsup R(u_j)\le R(u)\). If \(0<t<R(u)\), the point \(o+tu\) is interior: blending a small ball about \(o\) with the further endpoint gives a neighborhood inside \(Z\). Hence \(o+tu_j\in Z\) for large \(j\), giving \(\liminf R(u_j)\ge t\). Let \(t\) increase to \(R(u)\).

Radial scaling now gives a homeomorphism of pairs

\[
 (\overline B^d,S^{d-1})\longrightarrow
 (Z,Z\setminus\operatorname{relint}Z),\qquad
 ru\longmapsto o+rR(u)u.
 \qquad\text{(8)}
\]

It sends the open ball to the relative interior. Point costalks of \(k_Z\) computed in \(E\) equal the intrinsic point costalks on \(Z\), by closed-embedding supported adjunction. They are invariant under this homeomorphism. At an interior point, the local support pair is an open \(d\)-ball and its punctured ball. Its relative cohomology is \(k[-d]\): the ball contracts, and the punctured ball retracts radially to \(S^{d-1}\), whose reduced cohomology is \(k\) in degree \(d-1\). For \(d=1\), the reduced degree-zero cohomology of the two-point sphere gives the same result.

At a boundary point, a chart of the closed ball gives the local model
\(H=\{t\in\mathbb R^d:|t|<r,\ t_1\ge0\}\), with the distinguished point \(0\). Both \(H\) and \(H\setminus\{0\}\) are contractible and locally contractible. For the punctured set, choose \(a\) with \(a_1>0\) and \(|a|<r\), and contract each point along its segment to \(a\). Convexity keeps the segment in \(H\), and its first coordinate is positive at every positive contraction time, so it never passes through \(0\). The constant-sheaf comparison therefore identifies the restriction
\(R\Gamma(H;k)\to R\Gamma(H\setminus\{0\};k)\)
with \(k\to k\), the identity on constant sections. The support localization triangle makes its fibre \(R\Gamma_{\{0\}}(H;k)\) zero. Excision identifies this fibre with the point costalk. This argument is topological; it does not require the radial homeomorphism in (8) to be analytic.

The corresponding compact-section calculation on a relatively open half-box is

\[
 R\Gamma_c\!\left([0,1)\times(-1,1)^{d-1};k\right)=0.
 \qquad\text{(9)}
\]

For the half-interval factor, the localization triangle for
\([0,1)=[0,1]\setminus\{1\}\) gives \(k\to k\) on compact sections, and this map is the identity. Thus its compact cohomology vanishes; finite Künneth proves (9). This agrees with the local support calculation above. Coefficient duality preserves Euler characteristic, so the interior value is \((-1)^d\), and every boundary value is zero. Off \(Z\) the costalk is zero. This proves (7), without assuming a smooth or strictly convex boundary. \(\square\)

The sign uses relative dimension, including when \(Z\) lies in a proper affine subspace of \(E\).

## Reflection gives the inverse

Let \(-Z=\{-z:z\in Z\}\).

**Theorem.** For every nonempty compact convex subanalytic set \(Z\subset E\),

\[
 1_Z*D_E1_{-Z}=\delta_0.
 \qquad\text{(10)}
\]

**Proof.** Formula (7) and reflection identify the value of the left side at \(x\) with

\[
 (-1)^d\chi_c\!\left(Z\cap(x+\operatorname{relint}Z)\right).
 \qquad\text{(11)}
\]

At \(x=0\), the set is \(\operatorname{relint}Z\), homeomorphic to an open \(d\)-ball by (8). Its compact Euler characteristic is \((-1)^d\), so (11) is one.

Let \(x\ne0\). If \(x\) is outside the translation vector space \(L-L\), the intersection is empty. If \(d=0\), the only possible nonempty intersection would have \(x=0\), already excluded. We may therefore work in \(L\) with \(d\ge1\), choose a unit vector \(e\) along \(x\), and write \(x=te\) with \(t>0\). Set

\[
 C=Z\cap(x+Z),\qquad
 A=Z\cap\bigl(x+\partial_L Z\bigr).
 \qquad\text{(12)}
\]

Both sets are compact and subanalytic, and \(C\) is convex. If \(C\) is empty, (11) is zero. Otherwise additivity for the closed subset \(A\subset C\) gives

\[
 \chi_c\!\left(Z\cap(x+\operatorname{relint}Z)\right)
   =\chi(C)-\chi(A).
 \qquad\text{(13)}
\]

We will prove that both terms on the right are one.

Project orthogonally along \(e\) to the \((d-1)\)-dimensional vector space \(e^\perp\). Let \(P\) be the projection of \(Z\). Over \(w\in P\), the fibre of \(Z\) is a compact interval, written \([a(w),b(w)]\). Endpoints may coincide. The fibre of \(C\) is \([a(w)+t,b(w)]\) when this interval is nonempty. Hence

\[
 W=\operatorname{pr}(C)
   =\{w\in P:b(w)-a(w)\ge t\}.
 \qquad\text{(14)}
\]

As the image of the nonempty compact convex set \(C\), \(W\) is nonempty, compact and convex.

All interiors and boundaries of \(P\) are taken in \(e^\perp\). Since \(Z\) has interior in \(L\), its projection has interior in this \((d-1)\)-dimensional space.

Here is the boundary geometry needed to compute \(A\). If \(w\) is an interior point of \(P\), its fibre contains an interior point of \(Z\): choose an interior point \(z_0\) of \(Z\). When \(w=\operatorname{pr}(z_0)\), that point itself suffices. Otherwise, extend the segment in \(P\) from \(\operatorname{pr}(z_0)\) through \(w\) slightly beyond \(w\), and blend \(z_0\) with a lift of that further point. The positive coefficient of \(z_0\) keeps a small ball inside \(Z\).

Every point strictly between the two fibre endpoints is then interior. Indeed, a supporting hyperplane at such a point would have zero \(e\)-component, because both endpoints lie on its allowed side. It would induce a supporting hyperplane to \(P\) at its interior point \(w\), a contradiction. Conversely, over a boundary point of \(P\), a supporting hyperplane of \(P\) pulls back to a supporting hyperplane containing the whole fibre, so the whole fibre lies in \(\partial_L Z\).

The supporting-hyperplane fact used here has an elementary compact-convex proof. For a boundary point \(q\), choose exterior points \(q_j\to q\), and nearest points \(p_j\in Z\). Such nearest points exist by compactness. We have
\(|p_j-q_j|\le |q-q_j|\), hence \(p_j\to q\). Put
\(n_j=(q_j-p_j)/|q_j-p_j|\). For \(z\in Z\), the segment \(p_j+t(z-p_j)\) lies in \(Z\); the one-sided derivative at \(t=0\) of its squared distance to \(q_j\) is nonnegative. Thus
\(\langle n_j,z-p_j\rangle\le0\).
A convergent subsequence of the unit normals has a unit limit \(n\), giving
\(\langle n,z-q\rangle\le0\) for every \(z\in Z\). This is the required nonzero supporting normal. Apply the same argument to \(P\) when its dimension is positive; in dimension zero it has no boundary.

For \(w\in W\), these observations give the complete list

\[
 A_w=
 \begin{cases}
 \{a(w)+t\},&w\in\operatorname{int}P,\\
 [a(w)+t,b(w)],&w\in\partial P .
 \end{cases}
 \qquad\text{(15)}
\]

The upper endpoint \(b(w)+t\) of the translated interval is outside \(C_w\), since \(t>0\). Thus each fibre in (15) is nonempty and has Euler characteristic one, including a degenerate interval. In dimension \(d=1\), \(P\) is a point, its interior is itself, and its boundary is empty; the same formula applies.

No continuity of the endpoint functions \(a\) and \(b\) is needed here: \(A\) is a compact subanalytic subset, \(W\) is its image, and the projection is the restriction of a linear map. Its fibres were computed set-theoretically in (15). The projection \(A\to W\) is proper, so the already proved Euler pushforward theorem yields \(\chi(A)=\chi(W)=1\). Also \(\chi(C)=1\). A nonempty compact convex set has Euler characteristic one: its straight-segment contraction to a chosen point induces the usual prism chain homotopy on singular chains. The finite triangulation and constant-sheaf comparison identify that cohomology with the finite sheaf cohomology used here; compact and ordinary sections agree on this compact set. Equation (13) is therefore zero. This proves (10) at every \(x\). \(\square\)

The set \(A\) need not itself be convex. Proper projection and its point-or-interval fibres are what give its Euler characteristic.

The nonempty hypothesis is necessary. The empty indicator is zero, whose convolution with every function is zero. Reflection is necessary as well: a point indicator at \(a\) has inverse the point indicator at \(-a\).

## Closed convex sets add by Minkowski sum

For nonempty compact convex subanalytic sets \(C,D\), addition has fibre
\(C\cap(x-D)\). It is empty outside \(C+D\), and a nonempty compact convex set inside. Therefore

\[
 1_C*1_D=1_{C+D}.
 \qquad\text{(16)}
\]

The Minkowski sum is compact convex and subanalytic by the proper-image theorem. Applying the inverse theorem and uniqueness of inverses also gives
\(D_E1_{-(C+D)}=D_E1_{-C}*D_E1_{-D}\).
This identity includes different affine spans and point factors.

## Duality preserves convolution

Denote Verdier duality on functions by \(D_E\). Its value at \(x\) is the Euler characteristic of the point costalk of any realization. The preceding duality theorem gives \(D_E^2=1\), and preserves compact closed support.

For two realizations, the compact-section Künneth comparison on sufficiently small product neighborhoods gives the point-costalk comparison

\[
 \begin{aligned}
 i_{(x,y)}^!(F\boxtimes^L G)
   &\simeq i_x^!F\otimes_k^L i_y^!G,\\
 D_{E\times E}(\varphi\boxtimes\psi)
   &=D_E\varphi\boxtimes D_E\psi.
 \end{aligned}
 \qquad\text{(17)}
\]

Here is a local-support verification of the first line. Take relatively compact subanalytic coordinate balls \(U\) about \(x\) and \(V\) about \(y\). The complement of \((x,y)\) in their product is the union
\(((U\setminus\{x\})\times V)\cup(U\times(V\setminus\{y\}))\).
The two-open-set Mayer–Vietoris triangle and support localization identify point-supported sections with the total fibre of the square obtained by restricting in each factor. Finite constructible Künneth identifies that square with the tensor product of the two restriction arrows
\(R\Gamma(U;F)\to R\Gamma(U\setminus\{x\};F)\) and
\(R\Gamma(V;G)\to R\Gamma(V\setminus\{y\};G)\).
Over the field \(k\), taking these two finite mapping fibres gives the tensor product of their fibres. By support localization and excision these fibres are \(i_x^!F\) and \(i_y^!G\), respectively. This proves the displayed natural comparison. The compact-section version agrees with it because the maps from point supports to compact supports and then to small open neighborhoods are induced by the same inclusions of supports. All costalks are perfect. Taking Euler characteristics proves the second line; no identification of internal-Hom stalks with Hom of ordinary stalks is used.

The realization has compact closed coefficient support, so the natural comparison \(Rs_!\to Rs_*\) is an isomorphism on it. The dual-sections map
\(D_E Rs_!Q\to Rs_*D_{E\times E}Q\) is an isomorphism for the constructible perfect object \(Q=F\boxtimes^L G\). Duality has the same closed support, by its locality and biduality, so the last proper image is again \(Rs_!\). Applying (17) gives

\[
 D_E(\varphi*\psi)=D_E\varphi*D_E\psi.
 \qquad\text{(18)}
\]

Also \(D_E\delta_0=\delta_0\), since the point costalk of \(k_{\{0\}}\) is \(k\) in degree zero. Consequently duality is an involutive automorphism of the convolution algebra.

## Exercises with complete solutions

### Closed intervals and their inverses
*Difficulty: Introductory.*

For \(a\le b\) and \(c\le d\), compute
\(1_{[a,b]}*1_{[c,d]}\). Give the convolution inverse of \(1_{[a,b]}\), including the case \(a=b\).

**Solution.** The fibre is the compact interval
\([a,b]\cap[x-d,x-c]\). It is nonempty exactly when
\(a+c\le x\le b+d\), and each nonempty fibre has Euler characteristic one. Thus the product is \(1_{[a+c,b+d]}\).
If \(a<b\), the reflected interval is \([-b,-a]\), whose dual is
\(-1_{(-b,-a)}\). This is the inverse by (10). If \(a=b\), reflection gives the point \(-a\); its dual is \(\delta_{-a}\), and
\(\delta_a*\delta_{-a}=\delta_0\). The open-interval formula must not be used for this zero-dimensional case.

### Positive inputs can give negative convolution
*Difficulty: Introductory.*

For \(a<b\) and \(c<d\), compute \(1_{(a,b)}*1_{(c,d)}\).
Explain why convolution does not preserve nonnegative values.

**Solution.** Its fibre is the open interval
\((a,b)\cap(x-d,x-c)\). It is nonempty exactly when
\(a+c<x<b+d\). A nonempty bounded open interval has compact Euler characteristic \(-1\), so the answer is
\(-1_{(a+c,b+d)}\), with zero at both outer endpoints. Both input functions have only values zero and one, yet the output is negative on the sum interval. Euler integration counts cohomological degrees, not the number of points in a fibre.

### A rectangle retains two boundary signs
*Difficulty: Intermediate.*

For \(Z=[0,1]\times[0,2]\subset\mathbb R^2\), compute \(D1_Z\) and its convolution inverse. Check the product at \(x=(0,0)\) and \(x=(1/2,0)\).

**Solution.** The relative dimension is two, so
\(D1_Z=1_{(0,1)\times(0,2)}\), and the inverse is
\(1_{(-1,0)\times(-2,0)}\). At the origin the intersection in (11) is
\((0,1)\times(0,2)\); its compact Euler characteristic is
\((-1)(-1)=1\). At \((1/2,0)\) it is
\((1/2,1]\times(0,2)\). The first factor is half-open, with Euler characteristic zero by the interval localization triangle. Finite Künneth makes the product zero. Treating the first factor as a closed interval would give a wrong answer.

### Relative dimension inside a larger space
*Difficulty: Intermediate.*

Let \(Z=\{(t,0):0\le t\le2\}\subset\mathbb R^2\).
Compute its dual and inverse, and check the product away from its supporting line.

**Solution.** The relative dimension is one, so
\(D_{\mathbb R^2}1_Z=-1_{\{(t,0):0<t<2\}}\).
The inverse is
\(-1_{\{(t,0):-2<t<0\}}\). Both indicators are supported on the horizontal line, so their convolution vanishes off that line. On the line it is the one-dimensional interval calculation, equal to one only at the origin. The ambient dimension two would give the wrong dual sign; the point costalk of the closed-supported segment is computed in the segment itself.

### Why the reflection and nonempty hypotheses matter
*Difficulty: Introductory.*

Take a nonzero vector \(a\). Compare
\(\delta_a*D\delta_a\) with \(\delta_a*D\delta_{-a}\).
What happens if the convex set is empty?

**Solution.** A point costalk is concentrated in degree zero, so
\(D\delta_a=\delta_a\) and \(D\delta_{-a}=\delta_{-a}\).
The two products are \(\delta_{2a}\) and \(\delta_0\), respectively. Since \(a\ne0\), the first is not the unit. For the empty set the indicator and its dual are both zero, and their product is zero. Thus the reflected inverse theorem requires a nonempty set; it cannot be extended to the empty indicator.

### A nonconvex boundary portion with Euler characteristic one
*Difficulty: Advanced.*

Let \(Z=[0,1]^2\), \(x=(1/2,0)\), and form \(C,A\) as in (12). Describe the fibres of \(A\) under vertical projection, and compute \(\chi(A)\) without claiming that \(A\) is convex.

**Solution.** Here
\(C=[1/2,1]\times[0,1]\). The relevant portion of the boundary of
\(x+Z=[1/2,3/2]\times[0,1]\) consists of the full left edge and the bottom and top segments running from the left edge to horizontal coordinate one. Thus \(A\) is the union of three sides of this rectangle; it is not convex.
Projection to the vertical coordinate has a point fibre \(\{(1/2,w)\}\) for \(0<w<1\), and a closed interval fibre at \(w=0,1\). Every fibre has Euler characteristic one. The projection is proper, so
\(\chi(A)=\int_{[0,1]}1\,d\chi=1\).
Also \(\chi(C)=1\), and their difference in (13) is zero.

### Euler integral constrains algebraic units
*Difficulty: Intermediate.*

Show that a convolution unit must have Euler integral \(1\) or \(-1\).
Use this to show that \(2\delta_0\) has no inverse over \(\mathbb Z\).
Check the integral of the inverse of a nondegenerate closed interval.

**Solution.** If \(\varphi*\psi=\delta_0\), equation (6) gives
\(\epsilon(\varphi)\epsilon(\psi)=1\) in \(\mathbb Z\). Both integers must therefore be \(1\) or \(-1\). The integral of \(2\delta_0\) is two, so it has no convolution inverse in this integer algebra. For a closed interval its inverse is the negative indicator of the reflected open interval. The open interval has compact Euler characteristic \(-1\), so the negative indicator has integral one, as required. The necessary integral condition alone is not asserted sufficient for arbitrary functions.

### Minkowski addition and inverse multiplication
*Difficulty: Advanced.*

Prove (16) directly for compact nonempty convex subanalytic \(C,D\), even when their affine spans differ. Deduce the formula for the inverse of \(1_{C+D}\).

**Solution.** The addition fibre is
\(\{(u,v):u\in C,v\in D,u+v=x\}\), isomorphic to
\(C\cap(x-D)\). It is empty exactly when \(x\notin C+D\). Otherwise it is a nonempty compact convex set, of whatever relative dimension the fibre has, and its ordinary and compact Euler characteristic are one. This proves (16) in every affine-span configuration. Let
\(u_C=D1_{-C}\) and \(u_D=D1_{-D}\). Associativity and commutativity give
\((1_C*1_D)*(u_C*u_D)=\delta_0\).
Since \(1_C*1_D=1_{C+D}\) and its inverse is uniquely
\(D1_{-(C+D)}\) by (10), we obtain
\(D1_{-(C+D)}=D1_{-C}*D1_{-D}\).

## References

Pierre Schapira, [*Operations on constructible functions*](https://webusers.imj-prg.fr/~pierre.schapira/ResPapers/ConstFct.pdf), *Journal of Pure and Applied Algebra* 72 (1991), 83–93: Theorem 4.2, p. 91, states the compact convolution algebra, its duality compatibility and Euler integral; Examples 4.3 and 4.4 on that page give the Minkowski-sum identity and the reflected convex inverse. The duality formalism is developed in Theorem 2.5 and §3. The interval computation, local support calculation and compact projection argument above supply the details used here, including relative dimension, boundary fibres and the nonempty hypothesis.
