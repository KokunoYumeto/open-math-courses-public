# The ordinary topology of the Fermat quartic

*Independent programme exposition by GPT-6 Astra (OpenAI), Ultra, 7 October2026. This new text is dedicated under CC0; cited sources retain their own terms.*

Let
\[
Y=\mathbb {CP}^{3},\qquad
X=\{[z_0:z_1:z_2:z_3]:z_0^4+z_1^4+z_2^4+z_3^4=0\}.
\tag{T1}
\]
Then \(X\) is a compact connected smooth complex surface, its **ordinary topological** fundamental group is trivial, and
\[
H^2(X;\mathbb Q)\simeq\mathbb Q^{22}.
\tag{T2}
\]
We prove the fundamental-group assertion through an actual relative cell construction for \(X\hookrightarrow Y\). The cells have dimensions at least three. Cohomological vanishing by itself would not give this assertion.

The argument is a classical positive-divisor Morse argument, written here independently. It does not use the classification of K3 surfaces, a theorem about finite étale covers, or a residual-finiteness hypothesis. The quartic is a starting surface for a later deformation argument; it does not itself have Picard group zero.

## 1. The cell change at an ordinary Morse critical point

We first give the topological step needed after the complex Hessian estimate.

Let \(M\) be a compact smooth real \(m\)-manifold with boundary, and let \(g:M\to[0,\infty)\) be smooth, zero precisely on the boundary, with nonzero inward derivative there. Suppose all interior critical points are nondegenerate. Compactness of the boundary and nonvanishing of the differential give a critical-point-free neighborhood of the boundary. Thus the critical set is a closed subset of a compact interior set; its points are isolated by nondegeneracy, so there are finitely many. The pair \((M,\partial M)\), up to homotopy relative to \(\partial M\), is obtained by adjoining one cell of dimension \(\kappa(p)\) at every critical point \(p\), where \(\kappa(p)\) is the number of negative eigenvalues of its real Hessian.

Here is the full local attachment and the passage between critical values. Write \(M_t=\{g\leq t\}\). On a compact band containing no critical point, choose a Riemannian metric and put
\[
V=-\frac{\nabla g}{\|\nabla g\|^2}.
\tag{T3}
\]
Along its flow, \(g\) decreases at unit speed. A trajectory starting in \(M_b\setminus M_a\) reaches \(g=a\) in time \(g(x)-a\). Compactness of the band ensures existence until that time. Keeping points of \(M_a\) fixed and flowing the other points for \(t(g(x)-a)\), \(0\leq t\leq1\), gives a deformation retraction \(M_b\to M_a\). Continuity across \(g=a\) follows because the stopping time tends to zero. At the boundary the corresponding positive vector field produces a collar: its height coordinate is exactly \(g\). Thus a sufficiently small positive sublevel retracts to \(\partial M\).

For clarity, the only flow fact used here is local existence, uniqueness and continuous dependence for a smooth vector field, followed by continuation on a compact set where it stays bounded in finitely many charts. On a coordinate box, its integral equation is a contraction on continuous paths for a sufficiently short time, since a bounded first derivative is a Lipschitz constant. The fixed point gives the flow; the same estimate gives continuous dependence. Differentiating that integral equation successively gives smooth dependence. A finite covering of a compact band gives a uniform positive continuation time. No completeness assumption on an open ambient manifold is being made.

First suppose there is just one critical point at the critical value \(c>0\). In a sufficiently small Morse chart,
\[
g(u,v)=c-|u|^2+|v|^2,\qquad
u\in\mathbb R^\kappa,\quad v\in\mathbb R^{m-\kappa}.
\tag{T4}
\]
The full smooth Morse-coordinate proof, Lemma4.1 supplies (T4); only its parameter-free case is used. Its elementary construction can also be recalled here. Translate the critical point to the origin. An invertible symmetric Hessian has a vector on which its quadratic form is nonzero, since otherwise polarization would make the whole form zero. Choose this vector as the first coordinate direction. The implicit function theorem solves \(\partial_1g=0\) as \(x_1=h(x')\). Put \(y=x_1-h(x')\). The integral Taylor formula, whose linear term now vanishes, reads
\[
g(h(x')+y,x')=g(h(x'),x')+y^2 A(y,x'),\qquad
A(y,x')=\int_0^1(1-t)\,\partial_1^2g(h(x')+ty,x')\,dt.
\]
The function \(A\) is smooth and has a fixed nonzero sign after shrinking. Replacing \(y\) by \(y\sqrt{|A(y,x')|}\) is a smooth coordinate change, because its derivative at the origin is nonzero. It splits off one signed square. The Hessian of the remaining function \(g(h(x'),x')\) is the Schur complement of the first Hessian entry. Its determinant is the original nonzero determinant divided by that entry, so it is again invertible. Repeating in the remaining variables gives (T4). Congruence of the Hessians under a coordinate change preserves the dimensions of their positive and negative subspaces. Thus the numbers of signed squares are precisely the original indices; no complex-coordinate normal form is asserted.

Choose \(\epsilon>0\) so small that \(c-\epsilon>0\), that this is the only critical value in \([c-\epsilon,c+\epsilon]\), and that
\(\{|u|^2+2|v|^2\leq2\epsilon\}\) lies inside the chart. Choose a smooth nonincreasing function \(\mu:[0,\infty)\to[0,\infty)\) such that
\[
\mu(0)=\tfrac32\epsilon,\qquad
-1<\mu'\leq0,\qquad
\mu(r)=0\quad(r\geq2\epsilon).
\tag{T5}
\]
Such a function is obtained by integrating backwards a smooth nonnegative function supported in \((0,2\epsilon)\), bounded strictly below one, and with integral \(3\epsilon/2\). A smoothed function close to the constant \(3/4\) on this interval, with sufficiently short end transitions, can be rescaled to have that integral while its supremum remains below one.

Set \(\rho=|u|^2+2|v|^2\), replace \(g\) in this chart by
\[
\widetilde g=g-\mu(\rho),
\tag{T6}
\]
and leave it unchanged outside the chart. Flatness of \(\mu\) at the end of its support makes this a smooth global function. Its coordinate derivatives are
\[
\partial_u\widetilde g=-2(1+\mu'(\rho))u,\qquad
\partial_v\widetilde g=2(1-2\mu'(\rho))v.
\tag{T7}
\]
Both indicated factors are strictly positive. Therefore the only critical point in the chart is the origin, and its new critical value \(c-3\epsilon/2\) lies below \(c-\epsilon\). There are no critical points of \(\widetilde g\) in the closed band \([c-\epsilon,c+\epsilon]\).

Where the function was changed, \(\rho<2\epsilon\), and consequently \(g-c=-|u|^2+|v|^2<\epsilon\). Hence
\[
\{\widetilde g\leq c+\epsilon\}
=\{g\leq c+\epsilon\}.
\tag{T8}
\]
The regular-band flow for \(\widetilde g\) retracts this set onto
\(B=\{\widetilde g\leq c-\epsilon\}\), fixing \(B\) and therefore fixing
\(A=\{g\leq c-\epsilon\}\).

We now retract \(B\), relative to \(A\), onto \(A\) with a \(\kappa\)-disk attached. For a point of \(B\setminus A\), put
\[
a=|u|^2,\qquad b=|v|^2,\qquad
b_*=\max(a-\epsilon,0).
\tag{T9}
\]
If \(b>0\), the inequality \(g>c-\epsilon\) gives \(b>b_*\). Points with \(b=0\) already lie in the core disk and will stay fixed. Keep \(u\) fixed and replace \(v\), for \(0\leq t\leq1\), by
\[
v_t=
\left(\frac{(1-t)b+t b_*}{b}\right)^{1/2}v
\quad(b>0).
\tag{T10}
\]
If \(v=0\), keep the point fixed. Fix every point of \(A\). Decreasing \(b\) decreases \(\widetilde g\), since its derivative with respect to \(b\) is \(1-2\mu'(\rho)>0\), so the homotopy stays in \(B\).

The homotopy is continuous. At \(v=0\), its displacement is bounded by \(|v|\). Approaching \(A\) from outside, \(b-b_*=g-(c-\epsilon)\) if \(a\geq\epsilon\), while \(b\leq g-(c-\epsilon)\) if \(a<\epsilon\); in either case the displacement tends to zero. Points of \(B\setminus A\) lie where \(\mu>0\), hence inside the indicated compact coordinate region. At its boundary, the same estimate and \(g-(c-\epsilon)\leq\mu(\rho)\) give continuity with the fixed homotopy outside the chart.

At \(t=1\), either \(a\geq\epsilon\), when the image belongs to \(A\), or \(a\leq\epsilon\), when \(v_1=0\). The whole disk
\[
D=\{v=0,\ |u|^2\leq\epsilon\}
\tag{T11}
\]
belongs to \(B\): the function \(a+\mu(a)\) is increasing and starts at \(3\epsilon/2>\epsilon\). Its intersection with \(A\) is exactly its boundary \(|u|^2=\epsilon\). The homotopy fixes \(A\cup D\), so it is a deformation retraction onto that union. Thus \(M_{c+\epsilon}\) is homotopy equivalent to \(A\cup_{\partial D}D\), by maps fixed on \(A\). The union is the attachment quotient: both spaces are compact Hausdorff and the embedded disk meets \(A\) exactly at its boundary.

If several critical points have value \(c\), choose disjoint Morse charts and make all these changes simultaneously. The same proof attaches their disks together. The cases \(\kappa=0\) and \(\kappa=m\) are included: \(D^0\) has empty attaching boundary, and when there are no \(v\)-coordinates the last deformation is already the identity. Interleave these attachments with the regular-band retractions. There are finitely many bands and critical points, so the relative construction is finite and involves no limiting assertion at infinity.

This proves the stated relative cell theorem. It gives the homotopy consequence of a relative handle decomposition directly, including its attaching inclusions, without assuming a handle theorem as another prerequisite.

## 2. A function on the complement with controlled behavior at the divisor

Write \(P(z)=z_0^4+z_1^4+z_2^4+z_3^4\). Its four partial derivatives have no simultaneous projective zero, so \(X\) is smooth. Explicitly, in a chart where one coordinate is one, a zero of the equation has at least one other nonzero coordinate; its partial derivative is four times the cube of that coordinate, and is nonzero. The holomorphic implicit function theorem applies in that chart. It is nonempty, for example at \([1:\zeta:0:0]\) with \(\zeta^4=-1\), and it is closed in compact \(Y\). It has complex dimension two.

The polynomial \(P\) defines a section \(s\) of \(\mathcal O_Y(4)\). With the Hermitian metric induced from the usual projective metric, its squared norm is
\[
q([z])=\frac{|P(z)|^2}{(|z_0|^2+\cdots+|z_3|^2)^4}.
\tag{T12}
\]
The formula is invariant under \(z\mapsto\lambda z\). It is smooth on \(Y\), nonnegative, and zero precisely on \(X\). On \(U=Y\setminus X\), put
\[
\phi=-\log q.
\tag{T13}
\]
This is bounded below and proper: \(q\) has a finite positive maximum on \(Y\), and
\(\{\phi\leq A\}=\{q\geq e^{-A}\}\) is compact and disjoint from \(X\).

In an affine chart, write \(w=(w_1,w_2,w_3)\) and \(p(w)\) for the polynomial section in that chart. Then
\[
\phi=4\log(1+|w|^2)-\log|p(w)|^2.
\tag{T14}
\]
On a neighborhood in which \(p\neq0\), its logarithm exists holomorphically after shrinking, so the second term has zero Levi form. The first has Levi value
\[
\mathcal L_\phi(v)
=4\frac{(1+|w|^2)|v|^2-|\sum_j\overline w_jv_j|^2}
         {(1+|w|^2)^2}
\ \geq\ \frac{4|v|^2}{(1+|w|^2)^2}>0
\quad(v\neq0).
\tag{T15}
\]
Thus \(\phi\) is strictly plurisubharmonic. No theorem identifying \(U\) as Stein is needed: the required exhaustion has just been given explicitly.

We also need a finite upper level that really bounds a neighborhood of the divisor. Choose a smooth metric on \(Y\) and its normal bundle to \(X\). A small disk bundle maps diffeomorphically to a neighborhood of \(X\) by the normal exponential map. Here is the uniform-neighborhood justification. At a zero normal vector its derivative identifies \(TX\oplus\nu X\) with \(TY|_X\), so the smooth inverse function theorem makes it a local diffeomorphism. Compactness of \(X\) gives a uniform small radius. If injectivity failed at every smaller radius, two distinct preimages tending to the zero section would have base points with a common limit in \(X\); the local inverse near that zero vector would then contradict their equal images. This proves the required tubular chart. The exponential map itself follows from the smooth geodesic ordinary differential equation, with the local-flow construction described in §1.

At \(x\in X\), \(ds_x\) induces an isomorphism from the normal real two-plane to the underlying real plane of \(\mathcal O(4)_x\). In tubular coordinates \(v\in\nu_xX\), Taylor expansion therefore gives, uniformly for \(x\in X\),
\[
q(x,v)=|ds_x(v)|^2+O(|v|^3),\qquad
dq_{(x,v)}(v\partial_v)=2|ds_x(v)|^2+O(|v|^3).
\tag{T16}
\]
Compactness and invertibility bound the leading quadratic form below by a fixed positive multiple of \(|v|^2\). For all sufficiently small nonzero \(v\), the radial derivative is positive. Choose \(\delta>0\) so small that \(\{q\leq3\delta\}\) lies in this tubular region, every normal ray reaches each of the levels \(q=\delta,2\delta,3\delta\) before leaving it, and the stated radial derivative is positive there.

Then
\[
N=\{q\leq\delta\},\qquad M=\{q\geq\delta\}
\tag{T17}
\]
are compact manifolds with common smooth boundary \(B=\{q=\delta\}\), and \(Y=N\cup_B M\). On each normal ray, \(q\) strictly increases. Radial contraction therefore retracts \(N\) to its zero section \(X\). In particular this is an actual neighborhood deformation retraction, not just an equality of cohomology.

## 3. A finite perturbation and the reversed index

Set \(R=-\log\delta\). We next make \(\phi\) Morse without moving its boundary collar. All critical points of \(\phi\) lie outside \(\{0<q\leq3\delta\}\), by (T16). Let \(K=\{q\geq2\delta\}\). A finite covering of this compact set by coordinate charts, with bump functions equal to one on smaller charts, gives finitely many smooth real functions \(w_1,\ldots,w_N\), supported in \(\{q>3\delta/2\}\), such that their differentials span every cotangent fibre near \(K\).

For \(a\) in a sufficiently small ball \(E\subset\mathbb R^N\), define
\[
\psi_a=\phi+\sum_{j=1}^N a_jw_j.
\tag{T18}
\]
There are simultaneous uniform choices of that ball with the following properties.

First, on the compact union of the supports, the strictly positive Levi form of \(\phi\) has a positive minimum eigenvalue relative to a fixed metric. A sufficiently small \(C^2\) perturbation preserves strict positivity. Outside those supports nothing changes.

Second, \(d\phi\) has a positive minimum norm on the compact transition band
\(\{3\delta/2\leq q\leq2\delta\}\). A sufficiently small \(C^1\) perturbation leaves the differential nonzero there. On \(\{q<3\delta/2\}\) it is unchanged. Thus every critical point of \(\psi_a\) lies in \(K\).

Third, arrange
\[
\left|\sum_j a_jw_j\right|<\tfrac12\log(3/2).
\tag{T19}
\]
On the support of the perturbation, \(\phi<R-\log(3/2)\), whereas near \(B\) the perturbation is zero. Outside \(M\) it is also zero and \(\phi>R\). Consequently
\[
\{\psi_a\leq R\}=M,\qquad
\psi_a|_B=R,
\tag{T20}
\]
with the original collar and its nonzero normal derivative preserved.

Choose \(a\) for which all critical points are nondegenerate. This follows from a finite-dimensional regular-value argument with its actual map. On an open neighborhood \(W\) of \(K\), set
\[
H:W\times E\longrightarrow T^*W,\qquad
H(x,a)=(x,d\psi_a(x)).
\tag{T21}
\]
Its base derivative supplies the base tangent directions and the derivatives with respect to \(a_j\) supply every vertical direction. Thus \(H\) is a submersion. The inverse image \(Z=H^{-1}(0_W)\) is a smooth manifold of dimension \(N\). Apply the smooth critical-value theorem to the projection \(Z\to E\). Regular values are dense, so one can be chosen inside the ball satisfying the preceding smallness conditions.

At a zero of \(d\psi_a\), a tangent vector \((v,b)\) belongs to \(TZ\) exactly when
\[
\operatorname{Hess}_x(\psi_a)v+\sum_j b_j\,dw_j(x)=0.
\tag{T22}
\]
Since the second term ranges over the full cotangent fibre, the projection \(TZ\to E\) is onto exactly when the Hessian is onto. Its source and target both have real dimension six, so this means invertibility. Every critical point lies in \(K\), and every one is therefore nondegenerate. The set of critical points is closed and discrete in compact \(M\), away from the boundary; it is finite.

Fix such an \(a\) and write \(\psi=\psi_a\). If \(\lambda\) is the number of negative eigenvalues of its real Hessian at a critical point, strict Levi positivity implies
\[
\lambda\leq3.
\tag{T23}
\]
Indeed, for the real Hessian \(A\) and complex structure \(J\),
\(A(v,v)+A(Jv,Jv)=4\mathcal L_\psi(v)>0\) for \(v\neq0\).
A negative subspace of dimension more than three in a real six-dimensional space meets its \(J\)-image nontrivially. Such an intersection would contain a nonzero \(v\) with both \(v\) and \(Jv\) negative, a contradiction.

Now use the **reversed** function
\[
g=R-\psi\quad\hbox{on }M.
\tag{T24}
\]
It is zero on \(B\), positive in the interior, and its inward derivative at \(B\) is positive. Its Hessian is the negative of the Hessian of \(\psi\), so its index at the same point is
\[
\kappa=6-\lambda\geq3.
\tag{T25}
\]
This reversal is essential: the original exhaustion has indices at most three; building \(Y\) from a neighborhood of \(X\) uses the complementary indices, at least three.

Apply §1 to \(g\), and glue \(N\) along \(B\) throughout the relative homotopies. They fix \(B\), hence extend by the identity on \(N\). A starting collar retracts into \(N\). It follows that the actual inclusion
\[
N\hookrightarrow Y
\tag{T26}
\]
is, up to homotopy relative to \(N\), a finite sequence of attachments of cells of dimensions at least three. All work takes place in compact \(M\). No terminal comparison with an infinite union, and no assertion about handles accumulating at \(X\), is needed.

## 4. The ordinary fundamental group

Attaching a cell of dimension \(k\geq3\) changes neither path components nor the fundamental group of the component receiving it. Its attaching sphere \(S^{k-1}\) is connected, so it cannot join distinct components. For the group calculation, cover the attachment by a collar neighborhood of the old space and an open neighborhood of the disk's interior. Their intersection retracts to \(S^{k-1}\), the second set is contractible, and the first retracts to the old space. The ordinary van Kampen theorem gives an isomorphism on fundamental groups.

Only its usual path-and-homotopy form is involved here. Subdivide a loop into finitely many subpaths in the two open sets and connect their endpoints inside the connected intersection. This expresses its class as a product of classes from the two sets. Subdividing a homotopy square into sufficiently small rectangles gives exactly the identifications of the intersection loops. Thus the group of the union is the amalgamated product. When both the disk neighborhood and the intersection are simply connected, the old group's map is an isomorphism. The spheres of dimension at least two used here are simply connected, as the same argument on two contractible hemispherical neighborhoods shows.

Projective space is connected and simply connected. For an explicit programme-compatible calculation, the characteristic map
\[
D^{2j}\subset\mathbb C^j\longrightarrow\mathbb {CP}^j,\qquad
w\longmapsto[w:\sqrt{1-|w|^2}]
\tag{T27}
\]
identifies its interior with the affine chart and attaches its boundary to \(\mathbb {CP}^{j-1}\). The induced map from the attachment quotient is a continuous bijection from a compact space to a Hausdorff space, hence a homeomorphism. Thus \(\mathbb {CP}^1\) is a two-sphere, and \(\mathbb {CP}^3\) is obtained from it by attaching a four-cell and a six-cell. These latter attachments preserve \(\pi_1\), so \(\pi_1(Y)=1\).

All cells in (T26) have dimension at least three. Since \(Y\) is connected and \(N\neq\varnothing\), preservation of components first shows that \(N\) is connected. The deformation retraction \(N\to X\) then makes \(X\) connected. With any base point \(x_0\in X\), the maps induced by the actual inclusions are isomorphisms
\[
\pi_1(X,x_0)\ \xrightarrow{\ \sim\ }\ \pi_1(N,x_0)
\ \xrightarrow{\ \sim\ }\ \pi_1(Y,x_0)=1.
\tag{T28}
\]
These are discrete topological fundamental groups of the indicated manifolds.

## 5. The number twenty-two, with the complex orientation

Let \(L=\mathcal O_Y(1)|_X\) and \(h=c_1(L)\in H^2(X;\mathbb Z)\), with \(c_1\) equal to the Euler class of the underlying positively complex-oriented real plane. The differential of the quartic section along its zero set gives an exact sequence of complex bundles
\[
0\longrightarrow TX\longrightarrow TY|_X
\xrightarrow{\,ds\,}\mathcal O_Y(4)|_X\longrightarrow0.
\tag{T29}
\]
The derivative is intrinsic at a zero of the section: a change of local frame multiplies the defining function by a nonvanishing factor, and its differentiated extra term is multiplied by that function and hence vanishes on \(X\). The partial-derivative calculation makes \(ds\) surjective. A Hermitian orthogonal complement splits the sequence as complex topological bundles; a holomorphic splitting is not needed.

The projective tangent formula and the Whitney formula, in the same positive complex convention, give
\[
c(TX)=\frac{c(TY|_X)}{c(L^{\otimes4})}
 =\frac{(1+h)^4}{1+4h}
 =1+6h^2
\quad\hbox{through degree four}.
\tag{T30}
\]
Here \(c_1(L^{\otimes4})=4h\) is the complex-line tensor formula. Explicitly the degree-two coefficient is \(4-4=0\), and the degree-four coefficient is \(6-16+16=6\).

The evaluation of \(h^2\) can be made without a separate hypersurface Gysin formula. Restrict the two coordinate sections \(z_2,z_3\) to \(X\). They form a section of \(L\oplus L\), whose zero set consists of exactly the four points
\[
[1:\zeta:0:0],\qquad \zeta^4=-1.
\tag{T31}
\]
All roots are distinct. In the affine chart \(z_0=1\), the quartic equation has derivative \(4\zeta^3\neq0\) in \(w_1=z_1/z_0\). The holomorphic implicit function theorem therefore makes \((w_2,w_3)\) local complex coordinates on \(X\) at each point. In the induced frames of \(L\), the section is precisely \((w_2,w_3)\). Its real derivative is the identity in complex-oriented source and target coordinates, so every local index is \(+1\).

The Euler product rule identifies \(e((L\oplus L)_{\mathbb R})\) with \(h^2\). Pulling its positive Thom class back by the section and evaluating the local degrees consequently gives
\[
\langle h^2,[X]\rangle=4,\qquad
\langle c_2(TX),[X]\rangle=24.
\tag{T32}
\]
This uses the actual four zeros and their orientations; there is no unspecified sign from a divisor convention.

For completeness, the equality of the latter Euler number with the ordinary Euler characteristic follows from the same Morse-cell argument already proved. On any compact smooth manifold choose finitely many coordinate-bump functions with spanning differentials. The finite-parameter argument of §3, without the Levi restriction, gives a Morse function with finitely many critical points. Apply §1 from a level below its minimum to a level above its maximum. The resulting finite cell model has one cell of dimension equal to each critical index. Pair exact sequences show that its rational homology groups are finite-dimensional and that
\(\chi=\sum_p(-1)^{\lambda(p)}\).

The gradient of that Morse function has precisely those zeros. Its derivative there is the Hessian followed by the inverse metric. The inverse metric has positive determinant, so the local index is \((-1)^{\lambda(p)}\). The local Euler-class evaluation formula therefore gives
\[
\chi(X)=\langle e(TX_{\mathbb R}),[X]\rangle
       =\langle c_2(TX),[X]\rangle=24.
\tag{T33}
\]
The relative-cell homology calculation used for the alternating sum is the elementary one for \((D^j,S^{j-1})\): excision gives one copy of the coefficient field in degree \(j\) and zero in the others, and the long exact sequence preserves the alternating sum. Thus a triangulation or finiteness theorem is not an additional input at this point.

Since \(X\) is simply connected, \(H_1(X;\mathbb Z)=0\). One can see the implication directly: a singular one-cycle is homologous, after connecting its vertices to a base point, to a sum of based loops; a null homotopy of each loop supplies a singular two-chain bounding it. Over \(\mathbb Q\), homology and cohomology have the same Betti numbers by exact vector-space duality. Poincaré duality for the closed, complex-oriented real four-manifold \(X\) gives
\[
b_0=b_4=1,\qquad b_1=b_3=0.
\tag{T34}
\]
All Betti numbers are finite by the preceding Morse construction. Substituting into (T33) yields
\[
24=b_0-b_1+b_2-b_3+b_4=2+b_2,\qquad b_2=22.
\tag{T35}
\]
This proves (T2). The same argument also records that \(H^2(X;\mathbb Z)\) is torsion-free of rank22: the universal coefficient exact sequence has zero \(\operatorname{Ext}(H_1(X;\mathbb Z),\mathbb Z)\) term, and finite generation makes \(\operatorname{Hom}(H_2(X;\mathbb Z),\mathbb Z)\) free. No Picard-group assertion follows from this fact alone.

## 6. The exact contract for the sheaf example

A surface differentiably isomorphic to \(X\) has the ordinary fundamental group and the rational second cohomology computed above. The needed differentiable local triviality has the following direct proof once the analytic family exists.

Suppose \(p:\mathcal X\to B\) is a proper holomorphic submersion between complex manifolds, with \(B\) a neighborhood of \(0\) in a complex vector space and fibre \(X_0=X\). Regard a small real coordinate box in \(B\) as a box in \(\mathbb R^r\), \(r=2\dim_{\mathbb C}B\). Choose a larger closed box still inside \(B\). Its inverse image is compact by properness. A smooth metric on a neighborhood of this compact set splits the tangent bundle into the vertical tangent space \(\ker dp\) and its orthogonal complement. Restriction of \(dp\) to that complement is an isomorphism onto the pulled-back tangent bundle of \(B\). Lift the coordinate vector fields to smooth horizontal fields \(H_1,\ldots,H_r\), so \(dp(H_j)=\partial/\partial t_j\).

Let \(\Phi_j^u\) denote their flows. Along \(\Phi_j^u\), the base point changes only its \(j\)-th coordinate, by \(u\). All paths used below remain in the larger box. The compactness of its inverse image, and the flow continuation argument in §1, ensure that these flows exist for the full prescribed times on every point of the fibre. For \(t\) in a smaller box define
\[
\Theta:X_0\times B_{\mathrm{small}}\longrightarrow
       p^{-1}(B_{\mathrm{small}}),\qquad
\Theta(x,t)=\Phi_r^{t_r}\circ\cdots\circ\Phi_1^{t_1}(x).
\tag{T36}
\]
It satisfies \(p(\Theta(x,t))=t\). Given \(y\) over \(t\), apply the inverse flows in the opposite order, namely \(\Phi_1^{-t_1}\circ\cdots\circ\Phi_r^{-t_r}\), to return it to \(X_0\). These formulas are mutual smooth inverses, by uniqueness and smooth dependence of the flows. Thus \(\Theta\) is a differentiable trivialization. The horizontal fields need not commute; the fixed order and reversed inverse order are what give the actual maps.

The fibre diffeomorphisms preserve the complex orientations: their orientation sign varies continuously with the parameter and equals \(+1\) at zero. They therefore identify the integral intersection form as well as the ordinary fundamental group and rational cohomology. This proof requires a proper submersion, not just a formal deformation. It supplies no analytic deformation family or period map, and it does not assert that the Fermat quartic has no curves.

For any connected simply connected real four-manifold \(S\) and any finite subset \(A\), the complement \(S\setminus A\) is still connected and simply connected. Paths can be detoured inside punctured coordinate balls. Reattaching disjoint four-balls along their punctured versions changes no fundamental group, because a punctured four-ball retracts to \(S^3\). Van Kampen then identifies \(\pi_1(S\setminus A)\) with \(\pi_1(S)=1\).

Every locally constant sheaf of \(\mathbb Q\)-vector spaces on this complement is therefore constant, with **no finite-dimensionality restriction**. Choose one stalk. Continuation along a path gives an isomorphism from that stalk to the endpoint stalk, by finitely many local trivializations along the compact interval. Subdividing a homotopy square shows homotopic paths give the same transport. Triviality of the ordinary fundamental group makes the isomorphism independent of path, and local trivializations show these stalk isomorphisms form a sheaf isomorphism with the constant sheaf. This argument works for an arbitrary vector space and does not replace its monodromy by a finite quotient.

Thus the later Picard-zero deformation, when supplied, retains exactly the \(\mathbb Q\) coefficient scope, the arbitrary-rank local-system assertion and the number22 used in the complex-constructible realization counterexample.

## Programme proof readings

- Finite-parameter regular values, including the smooth inverse-coordinate argument. The independent regular-value proof applies to the finite-dimensional map (T21); its Stein cohomology theorem is not used.

- Strict Levi positivity, perturbations, and the real index bound. The present explicit complement function replaces the general Stein-exhaustion construction. Its index calculation is the zero-section case of the Hessian argument in that reading.

- Smooth Morse coordinates, Lemma4.1. The proof supplies the real signed-square coordinates used in (T4); AppendixA.4 supplies the finite smooth cutoffs.

- Projective cells and the first Chern class of a tensor product. Sections2–3 give the actual cell maps and relative singular groups; Proposition6.1 gives the line-bundle tensor formula.

- Whitney multiplication, projective tangent classes, and local Euler evaluation. Theorems2.2 and formula5.1 give (T30); Lemma5.2 gives the positively oriented zero count in (T32) and (T33).

- Integral Thom classes, Euler products and coefficient duality. Theorem5.2, Theorem7.1 and Proposition8.2 supply the coefficient and oriented-bundle conventions.

- Ordinary Poincare duality. Theorem1.1 and Corollary2.1 apply to the compact oriented real four-manifold with rational coefficients.

