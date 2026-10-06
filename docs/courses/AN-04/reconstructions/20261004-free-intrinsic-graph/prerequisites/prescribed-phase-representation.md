# Representing the intrinsic class with a prescribed phase

The phase is given in advance. We prove that its oscillatory integral
has the intrinsic iterated regularity, and that every member of the
intrinsic class can be represented by that phase near its critical
covector. The proof includes clean phases with excess, the exact order
shift, a construction of the amplitude, and every differentiated
symbol remainder.

The free human source for the Fourier-testing method and its
normalization is [Lars Hörmander, *Fourier integral operators. I*,
Section 3.2](https://projecteuclid.org/journals/acta-mathematica/volume-127/issue-none/Fourier-integral-operators-I/10.1007/BF02392052.pdf),
especially Theorem 3.2.4 and its parameter version, printed pages
149–154. Here the clean critical-family calculation is supplied by
the earlier programme's complete stationary-phase proof. The
amplitude construction below uses the proved symbol summation
theorem. Neither a citation nor the definition of an oscillatory
class is substituted for the intrinsic proof.

## F0. Inputs, orders and support conventions

The exact earlier programme inputs are:

- [C0–C5](conic-frequency-coordinates.md): finite rank facts, critical
  maps, conic frequency coordinates and the homogeneous function \(H\);
- [P2 O0–O6](ordinary-operator-calculus.md) and
  [T0–W5](coordinate-and-wavefront-localization.md): distributions,
  proper operators, coordinate transport and directional cutoffs;
- [K0–K7](conic-parametrices-and-localization.md): asymptotic sums,
  conic inverses, full intrinsic localization and independence of
  sufficiently small cutoffs and Lagrangian extensions;
- [the graph criterion G12](../intrinsic-frequency-graphs.md), in
  both directions, at the exact \(B_{2,\infty}\) endpoint;
- [U001 Sections 4–7 and Appendix A.4–A.6](../../20261004-free-stationary-phase/stationary-phase-and-critical-manifolds.md):
  parameter Morse coordinates, all scale and parameter derivatives
  of stationary remainders, clean critical families, densities,
  compact partitions and fibre integration;
- U001's linked finite-dimensional inverse theorem, compact
  integration and Fourier inversion proofs.

Let \(x\in\mathbb R^n\), \(n\ge1\), and
\(\theta\in\mathbb R^N\setminus0\), \(N\ge1\). A real phase
\(\phi(x,\theta)\) is smooth on an open cone, is homogeneous of
degree one in \(\theta\), and has nonzero full differential.
An ordinary amplitude \(a\in S^\mu\) satisfies, on each compact
base set,
\[
 |\partial_\theta^\alpha\partial_x^\beta a(x,\theta)|
       \le C_{\alpha\beta}\langle\theta\rangle^{\mu-|\alpha|}.
 \tag{F1}
\]
For the local arguments, the amplitude has compact base support
and its base/unit-direction support lies strictly inside the
phase domain. It vanishes near \(\theta=0\). Changes confined to
a bounded frequency set give a smooth function and will be
treated explicitly at the end.

Use the normalization
\[
 \begin{gathered}
 I_\phi(a)(x)=c_{n,N}\int e^{i\phi(x,\theta)}a(x,\theta)\,d\theta,
 \qquad c_{n,N}=(2\pi)^{-(n+2N)/4},\\
 \widehat u(\xi)=\int e^{-ix\cdot\xi}u(x)\,dx .
 \end{gathered}
 \tag{F2}
\]
All integrals with nonintegrable amplitudes mean the distributional
limit constructed in F2 below.

The critical set \(C_\phi=\{\phi_\theta'=0\}\) is **clean of excess
\(e\)** when it is a smooth submanifold of dimension \(n+e\) and
\[
 T C_\phi=\ker d(\phi_\theta'),\qquad
       \operatorname{rank}d(\phi_\theta')=N-e
       \quad\hbox{on }C_\phi .
 \tag{F3}
\]
Here \(0\le e\le N\). The usual nondegenerate phase is the case
\(e=0\), for which the implicit theorem supplies the submanifold
and tangent condition directly. The word “clean” includes both
conditions in (F3); the dimension of a zero set alone is insufficient.

## F1. Clean geometry and a transverse Fourier test

The map
\[
 \kappa:C_\phi\longrightarrow T^*\mathbb R^n\setminus0,
 \qquad (x,\theta)\longmapsto(x,\phi_x')
 \tag{F4}
\]
has rank \(n\), kernel dimension \(e\), and locally maps onto an
embedded conic Lagrangian \(\Lambda\).

**Proof.** A critical tangent \((v,w)\) obeys
\(\phi_{\theta x}''v+\phi_{\theta\theta}''w=0\).
It is in \(\ker d\kappa\) precisely when \(v=0\) and
\[
 \phi_{x\theta}''w=0,\qquad
 \phi_{\theta\theta}''w=0 .
 \tag{F5}
\]
The matrix in (F5) is the transpose of \(d(\phi_\theta')\).
Its rank is \(N-e\) by (F3), so its kernel has dimension \(e\).
Rank and nullity on the \((n+e)\)-dimensional critical tangent
give rank \(n\) for \(d\kappa\).

For completeness, this constant-rank assertion yields the required
local image without importing a constant-rank theorem. In a critical
chart choose \(n\) output components of \(\kappa\) with independent
differentials. Complete them by \(e\) input coordinates to a local
coordinate system \((\lambda,t)\), using the inverse theorem.
The other output components have zero \(t\) derivatives: otherwise
the output derivative would have rank greater than \(n\).
The fundamental theorem along coordinate segments in a small product
box makes them independent of \(t\). Thus the image is a smooth
graph over \(\lambda\), and the fibres are exactly the \(t\) slices.

The full differential hypothesis gives \(\phi_x'\ne0\) on the
critical set. Euler's identity gives \(\phi=0\) there. Hence
\(\phi_x'\cdot dx=0\) on critical tangents. Differentiate this
identity in two critical coordinates and subtract; mixed
derivatives cancel, giving
\(\sum d\phi_{x_j}'\wedge dx_j=0\) on image tangents.
The image has dimension \(n\), so it is Lagrangian. Positive
dilation preserves the critical set and sends its image
\((x,\xi)\) to \((x,r\xi)\). Saturating a sufficiently small
image chart proves the conic germ assertion. \(\square\)

Apply C3–C4 to choose base coordinates in which this germ is
\[
 \Lambda=\{(H'(\xi),\xi):\xi\in\Omega\},
 \qquad H(r\xi)=rH(\xi).
 \tag{F6}
\]
Only the germ is asserted; C4 provides a global degree-one
extension after shrinking the angular cone. Use a smooth
extension at bounded frequency whenever \(e^{iH}\) is applied
to a global Fourier transform. Its high-frequency value is unchanged.

For a unit covector \(\omega\) in this cone, put
\(\Psi_\omega(x,\vartheta)=\phi(x,\vartheta)-x\cdot\omega\).
Its critical set is the fibre \(\kappa^{-1}(H'(\omega),\omega)\),
of dimension \(e\). Its full Hessian is
\[
 Q_{\rm full}=
 \begin{pmatrix}
  \phi_{xx}''&\phi_{x\vartheta}''\\
  \phi_{\vartheta x}''&\phi_{\vartheta\vartheta}''
 \end{pmatrix}.
 \tag{F7}
\]
Its kernel consists exactly of the critical tangent vectors
annihilated by \(d\kappa\). Indeed its lower equation is (F3)'s
tangent equation, and its upper equation sets the differential
of the output covector to zero. On the graph (F6), that also
sets the differential of the base point to zero. Conversely
every fibre tangent satisfies both equations. Therefore
\[
 \ker Q_{\rm full}=T(\hbox{critical fibre}),\qquad
 d:=\operatorname{rank}Q_{\rm full}=n+N-e .
 \tag{F8}
\]
The phase is clean for each \(\omega\), with critical value
\(-H(\omega)\): \(\phi=0\) and
\(\omega\cdot H'(\omega)=H(\omega)\).

These fibres have smooth common adapted charts. On \(C_\phi\)
choose \((\xi,t)\) as above, now using the independent output
coordinates \(\xi\). Homogeneity lets \(t\) be degree zero:
choose its coordinates first on \(|\xi|=1\) and extend along
positive rays. Its normalized critical parametrization is
\[
 (x,\vartheta)=Y(\omega,t,0)
       =(H'(\omega),\vartheta(\omega,t)).
 \tag{F9}
\]
Choose complementary ambient coordinates \(z\in\mathbb R^d\)
at one fibre point and subtract their critical values, which
are smooth in \((\omega,t)\). The inverse theorem gives
\(Y(\omega,t,z)\), with the critical fibres precisely \(z=0\).
To check that no equation was lost, the critical fibre already
has dimension \(e\), and its \(t\) projection is a local
diffeomorphism; shrink the chart so its inverse is the unique
one. The transverse Hessian
\(Q(\omega,t)=\partial_z^2(\Psi_\omega\circ Y)(\omega,t,0)\)
is invertible by (F8). U001 A.5 proves this also for a
nonorthogonal complement. Its signature \(\sigma\) is constant
on a connected sufficiently small chart. On compact subcharts,
the inverse Hessian, chart derivatives and
\[
 J(\omega,t,z)=|\det D_{(t,z)}Y(\omega,t,z)|
 \tag{F10}
\]
have the uniform bounds required by U001. These are actual
finite-dimensional charts, not an additional clean-normal-form
assumption.

## F2. Distributional meaning and the noncompact-frequency tails

We first justify (F2). On the compact base/unit-direction support,
split by a smooth degree-zero cutoff into a part where
\(|\phi_\theta'|\ge\epsilon\), and a part where
\(|\phi_x'|\ge c|\theta|\). Such a split exists: on the unit
section the full differential is nonzero; near
\(\phi_\theta'=0\), compactness gives a positive lower bound
for \(|\phi_x'|\), which homogeneity scales by \(|\theta|\).
Use a cutoff supported in that latter neighborhood and equal
to one on a smaller one. Its complement has the first bound.

On the first part the operator
\[
 L_\theta=\frac{\phi_\theta'}{i|\phi_\theta'|^2}\cdot\partial_\theta
       \quad\hbox{satisfies}\quad L_\theta e^{i\phi}=e^{i\phi}.
 \tag{F11}
\]
Its coefficients are homogeneous of degree zero, with
frequency derivatives of the corresponding negative degrees.
In its transpose, a derivative either hits the amplitude,
lowering its order by one, or hits a coefficient, also
lowering the total order by one. Induction gives order
\(\mu-M\) after \(M\) integrations by parts. Every fixed
base derivative adds at most its number to that order,
because it may differentiate the exponential.
Thus arbitrarily large \(M\) makes the integral and every
base derivative absolutely convergent. This contribution is
a smooth function of compact base support.

On the second part use
\(L_x=\phi_x'\cdot\partial_x/(i|\phi_x'|^2)\).
Its coefficients and all base derivatives have order \(-1\)
in \(\theta\). Transposition against a compact test function
therefore lowers the amplitude order by one per application.
For \(M>\mu+N\) the integral is absolutely convergent, bounded
by finitely many test-function seminorms. This defines a
distribution of finite order.

These definitions agree with inserting a smooth frequency
cutoff and letting its radius tend to infinity. Terms where
a frequency derivative hits that cutoff have the same
negative-order budget as derivatives of the amplitude;
choose \(M\) with an extra integrable power and use the
compact-plus-tail limit argument of U001 Q1. This proves
independence of the cutoff and justifies all integrations
by parts just used. It also proves continuity in a finite
list of amplitude seminorms for any specified distribution
seminorm. The support is contained in the amplitude's base
projection.

For Fourier reduction, discard the first, smooth part and
write \(\xi=R\omega\), \(R\ge1\). On the remaining support,
\[
 c|\theta|\le|\phi_x'|\le C|\theta|.
 \tag{F12}
\]
If \(|\theta|/R\) is sufficiently small or sufficiently
large, the reverse triangle inequality gives
\(|\phi_x'-R\omega|\ge c_1(R+|\theta|)\).
Integrate in \(x\) with
\[
 L_{x,\xi}=
   \frac{\phi_x'-\xi}{i|\phi_x'-\xi|^2}\cdot\partial_x .
 \tag{F13}
\]
Every base derivative of a coefficient is bounded by
\(C_\beta(R+|\theta|)^{-1}\). This follows by differentiating
the quotient: each differentiated \(\phi_x'\) is \(O(|\theta|)\),
and the denominator has the stated lower bound.
After \(M\) transpositions, the integral is bounded by
\[
 C_M\int_{|\theta|\ge1}
 (R+|\theta|)^{-M}\langle\theta\rangle^{\max(\mu,0)}\,d\theta
 \le C'_M R^{\max(\mu,0)+N-M}
 \tag{F14}
\]
when \(M>\max(\mu,0)+N\). The last estimate follows by
\(\theta=R\vartheta\) and the proved radial power bound.
Every fixed \(\xi\) derivative inserts bounded powers of
the compact variable \(x\), while differentiated coefficients
improve or preserve the bound. A fixed number of angular
or scale derivatives, or multiplication by \(e^{iH(\xi)}\),
costs at most a fixed power of \(R\). Increasing \(M\)
absorbs that power. Thus these tails are smoothing symbols
with all derivatives.

We are left with \(c_0\le|\vartheta|\le C_0\) after
\(\theta=R\vartheta\). This is a fixed compact integration
region in \((x,\vartheta)\). Outside small adapted
neighborhoods of the critical fibres, the gradient of
\(\Psi_\omega\) has a positive minimum on each compact
parameter set. U001's complete nonstationary estimate
applies there. This proves every far-region assertion
needed below; the compact stationary theorem is never
applied to an unbounded phase-variable domain.

It also proves
\(\operatorname{WF}(I_\phi(a))\subset\kappa(C_\phi\cap
\operatorname{cone\,supp}a)\) locally. If an output base/covector
neighborhood misses this image, insert a base cutoff there
and use the same estimates with no stationary contribution.
The Fourier criterion W1 then applies. The statement remains
valid with the closed essential support of the amplitude:
on a fixed neighborhood where it is smoothing, choose its
order as negative as required in (F14) and in the compact
estimates. Finite compact partitions give the assertion
for supports meeting several critical charts.

## F3. The full Fourier symbol and its exact leading fibre integral

Restrict the amplitude to one of the small charts in F1,
with a fixed compact normalized support. Extend \(H\)
as in (F6) and define
\[
 T_\phi a(\xi)=e^{iH(\xi)}\widehat{I_\phi(a)}(\xi),
 \qquad \delta=\frac{N-n+e}{2},\qquad r=\mu+\delta .
 \tag{F15}
\]
Then \(T_\phi a\in S^r\). On the output cone it has a full
expansion whose leading term is
\[
 \begin{aligned}
 {\cal L}_\phi a(R\omega)
  &=(2\pi)^{\,n/4-e/2} R^\delta
       \int W(\omega,t)\,
        a(H'(\omega),R\vartheta(\omega,t))\,dt,\\
 W(\omega,t)
  &=e^{i\pi\sigma/4}
       J(\omega,t,0)|\det Q(\omega,t)|^{-1/2}.
 \end{aligned}
 \tag{F16}
\]
For \(e=0\), the integral means the single value at the
isolated critical point. For every integer \(k\ge0\),
there are linear coefficient operations \(T_j\) with
\[
 \begin{gathered}
 T_0={\cal L}_\phi,\qquad T_j:S^\mu\longrightarrow S^{r-j},\\
 T_\phi a-\sum_{j<k}T_ja\in S^{r-k}.
 \end{gathered}
 \tag{F17}
\]
All assertions are continuous in the relevant finite lists
of symbol seminorms. Coefficients use only finitely many
amplitude derivatives on the critical fibre.

**Proof.** By F2, only the compact scaled integral remains.
Its prefactor is \(c_{n,N}R^N\). Its phase is \(R\Psi_\omega\)
and has \(d=n+N-e\) normal variables. U001's parameter
Morse construction and clean theorem apply in the charts
already proved to exist. The transformed amplitude
\[
 a_R(Y(\omega,t,z))
       =a(x(\omega,t,z),R\vartheta(\omega,t,z))
 \tag{F18}
\]
times the fixed smooth cutoffs and Jacobian is a symbol
of order \(\mu\) in \(R\), with every \(R\) derivative
lowering its order by one. Indeed a derivative in a
compact chart variable can create \(R\partial_\theta\),
which has order zero cost by (F1); a scale derivative
creates \(\vartheta\cdot\partial_\theta\), of order \(-1\).
The same count applies to every product-rule term.
The bounds are uniform because \(|\vartheta|\) is bounded
above and below in the scaled compact region.

After removing the critical value \(-H(\omega)\), U001
Corollary 6.1 and Theorem 7.2 give a normal factor
\((2\pi/R)^{d/2}\), signature \(e^{i\pi\sigma/4}\),
and a remainder of order \(\mu-k\) before that factor.
Thus the total power is
\[
 N-d/2=\delta,\qquad
 c_{n,N}(2\pi)^{d/2}=(2\pi)^{n/4-e/2}.
 \tag{F19}
\]
The leading quotient density is exactly
\(J|\det Q|^{-1/2}\,dt\), by U001 A.5.
This proves (F16), including its signs and constants.
Compact tangential integration preserves all remainder
bounds by U001 A.6.

For each scale derivative \(\partial_R^\ell\) and angular
derivative \(\partial_\omega^\beta\), the remainder after
the prefactor has bound \(C R^{r-k-\ell}\).
In polar coordinates each Cartesian derivative
\(\partial_{\xi_j}\) is a bounded angular coefficient
times \(\partial_R\), plus \(R^{-1}\) times an angular
derivative. Iterating this identity proves
\(C_\alpha R^{r-k-|\alpha|}\), the full ordinary-symbol
estimate. The same argument proves the coefficient bounds.
The tails in F2 have every negative order, so they
do not alter the expansion. Outside a slightly larger
output cone there are no critical points, giving rapid
decay with all derivatives. At bounded frequency the
Fourier transform of a compactly supported distribution
is smooth, by T0 and differentiation of its compact test
pairing. These observations prove the global \(S^r\)
claim and the finite-seminorm continuity. \(\square\)

The formula has a useful locality property. If the
amplitude is smoothing near all critical points over
an output angular neighborhood, every coefficient in
(F17) is smoothing there; the arbitrary remainder
order proves the same for \(T_\phi a\). This uses the
whole expansion, not only the leading coefficient.

## F4. A symbol lift for the given phase

Choose a smaller closed angular set \(\Sigma\) strictly
inside the output cone. Let \(\chi\) be a smooth angular
cutoff, equal to one on a neighborhood of \(\Sigma\),
with compact support inside that cone. There is a linear
extension operation
\[
 E:S^r(\mathbb R^n_\xi)\longrightarrow
      S^{r-\delta}(\mathbb R^n_x\times\mathbb R^N_\theta)
 \tag{F20}
\]
whose amplitudes have one fixed compact base/angular support
inside the prescribed phase chart, such that
\[
 {\cal L}_\phi(Eb)=\chi b\pmod{S^{-\infty}} .
 \tag{F21}
\]
It preserves angular essential support at the critical set.

Here is the complete construction. Near the selected
critical ray, \(\phi_x'\ne0\). Put \(\xi=\phi_x'(x,\theta)\).
Choose \(N-e\) independent components \(v\) of
\(\phi_\theta'\). Their common zero set equals \(C_\phi\)
after shrinking: both are submanifolds of the same
dimension, the selected differentials have the full
normal rank, and the inverse chart makes inclusion
an equality in a neighborhood. Choose the degree-zero
coordinates \(t\) from F1. They can be extended smoothly
off the critical set by a normalized ambient chart.
Then
\[
 (x,\theta)\longmapsto(\xi,t,v)
 \tag{F22}
\]
is a local diffeomorphism. To check its derivative, a
vector with \(dv=0\) is critical tangent; on that tangent
\((d\xi,dt)\) is an isomorphism. Thus its kernel is zero,
and dimension gives invertibility. The inverse theorem
applies. The map has weights \((1,0,0)\) under dilation
of \(\theta\); uniqueness of the inverse proves the same
weighted homogeneity for its inverse. Equivalently work
first on \(|\xi|=1\) and then dilate.

Choose a nonnegative smooth \(p(t)\) with compact support
inside the \(t\) box and \(\int p(t)\,dt=1\).
A positive bump has positive integral because it is
bounded below by a positive number on a smaller rectangle;
divide by its finite positive integral. In dimension
zero set \(p=1\). Choose a smooth compact \(\eta(v)\)
equal to one near \(v=0\). In (F22), at sufficiently
large \(R=|\xi|\), define
\[
 Eb=(2\pi)^{-n/4+e/2}
 R^{-\delta}\chi(\omega)b(\xi)
       \frac{p(t)}{W(\omega,t)}\,\eta(v),
 \qquad \omega=\xi/|\xi|.
 \tag{F23}
\]
Use an additional high-frequency cutoff and extend
by zero outside the compact normalized coordinate
box. The supports of \(p,\chi,\eta\) are strictly
inside that box, so extension is smooth. The weight
\(W\) is smooth and never zero; its reciprocal and
all needed derivatives are bounded on this compact set.
Choose the same charts for (F16) and (F23).

The scale \(R\) is comparable to \(|\theta|\) on this
support. Every frequency derivative of a degree-zero
coordinate or smooth weight costs one inverse power;
every base derivative costs no power. A frequency
derivative of \(\xi=\phi_x'\) has degree zero,
whereas a base derivative has degree one. In a
chain-rule term for \(b(\xi)\), that latter degree
exactly compensates the order lost by differentiating
\(b\). The iterated product and chain rules therefore
prove every estimate in (F20), with finite-seminorm
continuity. Substitution on \(v=0\) into (F16) cancels
the weight and the power of \(R\); \(\int p=1\)
proves (F21). The bounded-frequency modification is
smoothing. The same derivative estimates show that
if \(b\) is smoothing on an angular neighborhood,
\(Eb\) is smoothing near its critical inverse image.

## F5. Constructing an amplitude to every order

Suppose \(b\in S^r\) has angular essential support
inside \(\Sigma\). This means that on every closed
angular set outside \(\Sigma\), it has all negative
orders with all derivatives. Then there is an
amplitude \(a\in S^{r-\delta}\), with the fixed
support allowed in F4, such that
\[
 T_\phi a-b\in S^{-\infty}.
 \tag{F24}
\]

**Proof.** Set \(b_0=b\) and, recursively,
\[
 a_j=Eb_j,\qquad b_{j+1}=b_j-T_\phi a_j .
 \tag{F25}
\]
F3–F4 give \(b_{j+1}\in S^{r-j-1}\) whenever
\(b_j\in S^{r-j}\) has essential support in \(\Sigma\).
Indeed \(T_\phi Eb_j-\chi b_j\) has one lower order,
and \((1-\chi)b_j\) is smoothing, since \(\chi=1\)
on a neighborhood of that fixed closed set.

The essential-support condition also persists. On an
angular neighborhood disjoint from \(\Sigma\), the
critical jets of \(Eb_j\) are smoothing by F4, and F3's
locality statement makes \(T_\phi Eb_j\) smoothing.
Subtracting preserves this property. On compact
angular sets, finitely many such neighborhoods give
uniform seminorms. Thus the induction holds for every
\(j\), on the same \(\Sigma\) and the same amplitude
support; no endless shrinking of cones occurs.

We have \(a_j\in S^{r-\delta-j}\). Apply K1's proved
support-preserving summation theorem in the frequency
variable \(\theta\), with base variable \(x\), to obtain
\[
 a-\sum_{j<k}a_j\in S^{r-\delta-k}.
 \tag{F26}
\]
All terms have the same compact base/angular support,
so the sum keeps that support. F3's continuous order
bound sends this remainder into \(S^{r-k}\).
The finite identity from (F25) is
\(b-T_\phi\sum_{j<k}a_j=b_k\in S^{r-k}\).
Consequently \(b-T_\phi a\in S^{r-k}\) for every \(k\),
which proves (F24). This is asymptotic summation with
each remainder justified, not an infinite operator
series assumed to converge. \(\square\)

## F6. The prescribed-phase representation theorem

In the conventions of (F2), a clean phase of excess
\(e\) uses amplitude order
\[
 \boxed{\ \mu=m+\frac n4-\frac{N+e}{2}\ },
 \qquad r=\mu+\delta=m-\frac n4 .
 \tag{F27}
\]
Near a chosen critical covector, the following assertions hold.

1. Every amplitude of this order with sufficiently small
   compact base/angular support defines a distribution
   in the intrinsic class \(I^m(\Lambda)\) microlocally.
2. Every \(u\in I^m(\Lambda)\) microlocally near that
   covector can, after a sufficiently small proper
   order-zero cutoff there, be written as \(I_\phi(a)\)
   modulo a smooth function, with this same prescribed
   phase and amplitude order.
3. For \(e=0\) the order is \(m+n/4-N/2\). If instead
   a clean phase uses that nondegenerate amplitude order,
   its intrinsic order is \(m+e/2\).

**Proof of the forward assertion.** Choose the base
coordinates (F6). F3 gives \(b=T_\phi a\in S^{m-n/4}\)
and the exact Fourier identity
\(\widehat{I_\phi(a)}=e^{-iH}b\).
The reverse direction of the proved graph criterion
G12 gives intrinsic membership for the graph of the
extended \(H\). F2 confines its wavefront to the
original local phase image. A proper conic cutoff
inside the region where that graph and \(\Lambda\)
agree transfers membership by K7. Coordinate and
frame invariance is the already proved T3.
Finite amplitude partitions handle any compact
normalized support covered by such small charts;
the part away from \(C_\phi\) is smooth by F2.

**Proof of the converse.** By the microlocal hypothesis
there is an elliptic order-zero test with output in
\(I^m(\Lambda)\). K7 lets us replace it by any sufficiently
small compact proper conic cutoff \(P\) elliptic at the
chosen point. Choose its essential support inside the
phase branch and with output directions in a fixed
closed angular set \(\Sigma\) strictly inside the
frequency chart. Put \(v=Pu\). It has compact base
support, lies in \(I^m\) of the extended graph by K7,
and has wavefront directions only in \(\Sigma\).
The forward direction of G12 gives
\[
 b=e^{iH}\widehat v\in S^{m-n/4}.
 \tag{F28}
\]

We justify the essential-support assertion needed in
F5. On a closed angular set outside \(\Sigma\), every
point of the compact base support has a base cutoff
whose Fourier transform is rapidly decreasing in
a neighboring cone, by the definition of wavefront.
Choose finitely many smaller base neighborhoods and
their finite smooth partition, and finitely many
angular neighborhoods on the prescribed closed set.
W1's convolution cutoff estimate allows the partition
cutoffs; adding the finite local Fourier transforms
gives uniform rapid decay of \(\widehat v\).
For \(\partial_\xi^\alpha\widehat v\), apply the same
argument to \((-ix)^\alpha v\), which has the same
compact support and no additional wavefront by W4.
Derivatives of \(e^{iH}\) have polynomial bounds, so
the product retains every negative order there.
Thus \(b\) has angular essential support in \(\Sigma\).

F5 constructs \(a\in S^\mu\) with (F24). Multiplication
by \(e^{-iH}\) preserves Schwartz decay with all
derivatives, since the extension is smooth and its
derivatives are polynomially bounded. Fourier
inversion therefore makes \(v-I_\phi(a)\) smooth,
indeed Schwartz in this coordinate chart. This is
the claimed representation. The identities in
(F27) prove assertion 3. \(\square\)

If literal equality on a smaller base neighborhood is
needed, the smooth remainder can be absorbed into
a bounded-frequency amplitude. Let \(f(x)\) be that
remainder localized by a base cutoff. Choose a compact
frequency bump \(q(\theta)\), away from zero, with
\(\int q=1\), so that its product with this small base
support lies inside the prescribed phase domain.
Then
\[
 a_{\rm sm}(x,\theta)=c_{n,N}^{-1}
           f(x)e^{-i\phi(x,\theta)}q(\theta)
 \quad\Longrightarrow\quad I_\phi(a_{\rm sm})=f .
 \tag{F29}
\]
This amplitude is smoothing. Low frequencies thus
do not require a different phase or a lost order.
The theorem still concerns a microlocally cut off
distribution; it makes no assertion about untested
directions of the original \(u\).

### F6a. Reading a lower order on a smaller output cone

Suppose \(v=I_\phi(a)\) has the small compact support
used above, and \(b=e^{iH}\widehat v\in S^r\).
Near a chosen graph covector, \(v\) has intrinsic
order \(m-k\) if and only if \(b\) has symbol order
\(r-k\) on a sufficiently small angular cone.
Here is a proof that does not assume a new operator
transformation formula.

For the forward implication, K7 gives a compact
proper \(P\) with full symbol one near that
covector, and \(Pv\in I^{m-k}\) of the graph.
G12 gives \(e^{iH}\widehat{Pv}\in S^{r-k}\).
The wavefront of \(v\) is contained in this
frequency graph. On a smaller angular cone its
only possible base point is \(H'(\omega)\), where
the symbol of \(I-P\) is smoothing. W4 therefore
shows that \(v-Pv\) has no wavefront in any base
point with these frequency directions. It has
compact support. The finite base-cover argument
in the proof of (F28) makes its Fourier transform
rapidly decreasing there with all derivatives.
Adding this smoothing error proves the implication.

Conversely suppose \(b\) has order \(r-k\) on
an open angular cone. Choose a smooth angular
\(\chi_0\) supported strictly inside it, equal to
one on a smaller cone, and truncate it at low
frequency. Then \(b_1=\chi_0b\in S^{r-k}\)
globally, and
\(w=\mathcal F^{-1}(e^{-iH}b_1)\) belongs to
\(I^{m-k}\) by G12. The Fourier transform of
\(v-w\) vanishes in that smaller cone at high
frequency and is polynomially bounded elsewhere.
W1's convolution cutoff estimate makes every
compact base localization rapidly decreasing
on a still smaller cone. Thus \(v-w\) has no
wavefront there. A compact proper conic cutoff
\(P\), elliptic at the given covector and supported
in this cone, sends \(v-w\) to a smooth section
by W4. K6 sends \(w\) into \(I^{m-k}\).
Consequently \(Pv\in I^{m-k}\), which is the
claimed microlocal assertion. All shrinking is
finite, for the specified \(k\) and covector.

## F7. The first lower-order criterion and clean cancellation

Let \(a\in S^\mu\) be as in F6. Its contribution has
intrinsic order \(m-1\), on the tested cone, if and
only if
\[
 {\cal L}_\phi a\in S^{m-n/4-1}
 \quad\hbox{there}.
 \tag{F30}
\]
In fact F3 gives \(T_\phi a-{\cal L}_\phi a\) in
that lower order, and the two implications of F6a
identify intrinsic order with the Fourier-symbol
order on a smaller cone. This proves both directions
of (F30) without assuming a composition formula
for general Fourier-integral operators.

For a nondegenerate phase the weight in (F16) is
nonzero and there is one critical point; (F30) is
precisely that the restricted amplitude has one
lower order. For a clean phase it is the weighted
fibre integral that must have lower order.
Pointwise vanishing of the amplitude on the entire
critical fibre is sufficient but unnecessary.
All lower orders are recovered by applying (F17)
with enough terms: the exact criterion for order
\(m-k\) is that the sum of its first \(k\)
coefficients have Fourier-symbol order at most
\(m-n/4-k\). The remainder already has that order.
This states the full condition rather than
discarding lower coefficients after a leading
cancellation.

## Two models with complete solutions

**Exercise F1: a quadratic stabilization.** In one
base dimension let \(t>0\), \(s\in\mathbb R\), and
\(\phi(x,t,s)=xt+s^2/(2t)\). Determine the critical
Lagrangian, the excess, and the leading Fourier
symbol for a prescribed amplitude.

**Solution.** The critical equations are
\(x-s^2/(2t^2)=0\) and \(s/t=0\), hence \(x=s=0\).
Their differentials are independent there. Thus
\(N=2,e=0\), and the output is \((x,\xi)=(0,t)\),
with \(H=0\). At output \(\omega=1\), in variables
\((x,t,s)\), the Hessian of \(\phi-x\) is
\[
 Q=\begin{pmatrix}0&1&0\\1&0&0\\0&0&1\end{pmatrix},
 \qquad \det Q=-1,\quad \operatorname{sgn}Q=1 .
 \tag{F31}
\]
The upper two-dimensional block has one positive
and one negative direction, by the change
\((x,t)\mapsto((x+t)/\sqrt2,(x-t)/\sqrt2)\).
Here \(J=1,\delta=1/2\), so
\[
 T_\phi a(R)=(2\pi)^{1/4}e^{i\pi/4}
                   R^{1/2}a(0,R,0)
                  \pmod{S^{\mu-1/2}} .
 \tag{F32}
\]
The required amplitude order is \(\mu=m-3/4\);
the output order is \(m-1/4\). This checks the
positive Fresnel sign and the half-order gained
by adding the nondegenerate variable \(s\).

**Exercise F2: a redundant variable and cancellation.**
Keep \(t>0\), put \(\phi(x,t,s)=xt\), and restrict
\(s/t\) to a compact interval. Compute the clean
fibre weight and exhibit a nonzero amplitude
with zero distribution.

**Solution.** Now \(C_\phi=\{x=0\}\), because
\(\phi_t'=x\) and \(\phi_s'=0\).
Its dimension is two, so \(N=2,e=1\).
The output is again \((0,t)\). At \(\omega=1\)
the critical fibre has \(t=1\), with free
coordinate \(s\); the normal Hessian in \((x,t)\)
is the upper block of (F31). Its determinant
has absolute value one and its signature is
zero. Thus \(J=1,\delta=1\), and
\[
 {\cal L}_\phi a(R)
   =(2\pi)^{-1/4}R\int a(0,R,R\tau)\,d\tau .
 \tag{F33}
\]
The amplitude order required for intrinsic \(m\)
is \(m-5/4\), exactly a half-order lower than
for the nondegenerate phase in Exercise F1.

Choose a nonzero compact smooth \(g(\tau)\)
and an amplitude \(c(x,t)\), supported at \(t\ge1\)
and compactly in \(x\). Set
\(a(x,t,s)=c(x,t)g'(s/t)\).
On the support, \(s/t\) is bounded, so every
frequency derivative has its ordinary inverse
power of \(t\); this has the same symbol order
as \(c\). Yet the \(s\) integral is exactly
\(t\int g'(\tau)\,d\tau=0\), by the fundamental
theorem and compact support. Frequency truncation
followed by the distributional limit in F2
justifies this calculation, or first use
truncation in \(t\), for which it is an ordinary
compact integral. Thus \(I_\phi(a)=0\) although
the amplitude on the critical fibre need not
vanish. The cancellation is the fibre integral,
as required by (F30). \(\square\)

## Scope and remaining work

The proofs above concern ordinary symbols, real phases, finite-rank components, and local conic germs with all orders and remainders retained. They do not assert a global Maslov trivialization, the full global principal symbol sequence, or Fourier-integral composition. Those remain separate original course obligations.

*Written by GPT-6 Astra (OpenAI), Ultra, 4 October 2026.
Original exposition: CC0 to the extent rights exist.
No human-source prose, figure or original PDF is
redistributed. Linked earlier programme components
retain their own authorship, licences and notices.*
