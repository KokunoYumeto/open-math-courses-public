# Analytic normal cones through complex deformation

The normal cone is defined using positive real scales, even on a complex manifold. Nevertheless, for complex analytic pieces it is a complex analytic cone. The key is to construct the complex deformation correctly and then show that every point of its central fibre can be approached with a positive real deformation parameter. Simply putting the parameter equal to zero in the original equations can introduce entire components that have no nearby nonzero-parameter points.

Let \(X\) be a complex analytic manifold, Hausdorff and countable at infinity, of complex dimension \(n\). Let \(A,B\subset X\) be locally closed analytic pieces: their ambient closures and removed frontiers are closed complex analytic. Our ordered convention is

\[
C(A,B)=C_\Delta(A\times B)\subset TX,
\qquad [(v,w)]\longmapsto v-w.
\tag{1}
\]

Thus the first member contributes with a plus sign. In a coordinate chart,

\[
(x;v)\in C(A,B)
\iff
\begin{cases}
a_j\in A,\ b_j\in B,\ a_j,b_j\to x,\\
h_j>0,\ h_j\to0,\ (a_j-b_j)/h_j\to v.
\end{cases}
\tag{2}
\]

There are no sheaf coefficients, dualizing complexes or derived shifts in this lesson. The argument proves complex analyticity and complex-scalar invariance of the ordered normal cone relative to the explicit local analytic component and real curve-selection prerequisites. The source account below identifies those classical inputs and the deformation construction.

*Written by GPT-6.1 Sol (OpenAI), Ultra, September 2026. Author self-check recorded; not independently reviewed. New original text is public domain (CC0).*

## Removing analytic components rather than adding them at the boundary

We use the fundamental local component theorem for complex analytic sets: a closed analytic set has a locally finite irreducible-component decomposition; a proper analytic subset of an irreducible component has empty interior, and the complement is dense. The underlying local Noetherian and irreducibility theory is an explicit complex-geometry prerequisite.

One consequence that we will need is elementary once those facts are given. If \(Z,H\) are closed complex analytic subsets of a complex manifold, then

\[
\overline{Z\setminus H}
=\bigcup_{Z_i\not\subset H}Z_i,
\tag{3}
\]

where \(Z_i\) are the irreducible components of \(Z\). A component contained in \(H\) contributes no point to the difference. On every other component, \(Z_i\cap H\) is proper and its complement is dense, giving that entire component in the closure. Local finiteness lets us take these closures one finite family at a time. A locally finite union of analytic components is analytic, so the left side of (3) is closed complex analytic.

The formula uses closure in the given ambient open manifold. It does not claim that an arbitrary analytic subset of an open complement has analytic closure; the subset here is specifically obtained from the closed analytic \(Z\) by deleting the closed analytic \(H\).

## A holomorphic arc obtained from real curve selection

Here is the arc statement we need. If \(D,H\) are closed complex analytic subsets of a complex manifold and \(q\in\overline{D\setminus H}\), there is a holomorphic map \(\gamma\) from a small complex disc such that

\[
\gamma(0)=q,\qquad
\gamma(s)\in D\setminus H\quad(0<|s|\ll1).
\tag{4}
\]

We prove this using the real analytic curve-selection prerequisite already stated in Subanalytic sets and limiting tangent directions. The set \(D\setminus H\) is subanalytic in the underlying real manifold. That prerequisite gives a real analytic curve through \(q\), belonging to this set for nonzero real parameters sufficiently near zero.

In complex coordinates, extend each of its real analytic coordinate functions holomorphically in the parameter. After shrinking the disc, the extension stays in the coordinate neighborhood. Every local holomorphic defining function of \(D\), composed with the extension, vanishes on a real interval. The identity theorem makes it vanish throughout the disc. Thus the extended curve lies in \(D\).

The inverse image of \(H\) is an analytic subset of the disc. It is not the entire disc, because the original nonzero real parameters avoid \(H\). Such a proper analytic subset is discrete. Shrinking at zero removes all its nonzero points near zero, proving (4). This proof uses real curve selection as a prerequisite and proves the finite-coordinate holomorphic version needed here. It does not establish a meromorphic arc with unbounded cotangent coordinates, which will require its own compactification argument later.

## The complex deformation chart and its accessible closure

Choose a complex coordinate chart \(U\subset\mathbb C^n\). In the complex open manifold

\[
\mathcal U=\{(x,v,t):x\in U,\ v\in\mathbb C^n,\ t\in\mathbb C,
\ x+tv\in U\},
\tag{5}
\]

consider the closed analytic set

\[
Z=\{(x,v,t):x\in\overline B,\ x+tv\in\overline A\}.
\tag{6}
\]

Here all closures and analytic equations are restricted to \(U\). The maps \((x,v,t)\mapsto x\) and \((x,v,t)\mapsto x+tv\) are holomorphic, which proves analyticity of (6).

Let \(A_\partial=\overline A\setminus A\) and \(B_\partial=\overline B\setminus B\). Delete from (6) the closed analytic set obtained by imposing any of

\[
t=0,\qquad x\in B_\partial,\qquad x+tv\in A_\partial.
\tag{7}
\]

Call that deleted set \(H\). The resulting difference is exactly

\[
W=Z\setminus H
=\{(x,v,t):t\ne0,\ x\in B,\ x+tv\in A\}.
\tag{8}
\]

Define the **accessible complex deformation** by

\[
D=\overline W^{\,\mathcal U},\qquad D_0=D\cap\{t=0\}.
\tag{9}
\]

Equation (3) makes \(D\) closed complex analytic: retain precisely the components of \(Z\) not contained in \(H\). Its central fibre \(D_0\) is therefore analytic in the central chart \(U\times\mathbb C^n\), identified with \(TU\).

A component that appears only at \(t=0\) is contained in \(H\) and is discarded. This is what distinguishes (9) from the naive central fibre of (6).

## Reparameterizing an arc to make the scale positive real

We prove

\[
D_0=C(A,B)|_{TU}.
\tag{10}
\]

First take a sequence from (2). For large \(j\), set

\[
x_j=b_j,\qquad v_j=(a_j-b_j)/h_j,\qquad t_j=h_j.
\tag{11}
\]

These points belong to \(W\). They tend to \((x,v,0)\), so the corresponding tangent vector belongs to \(D_0\).

For the other inclusion, take \(q=(x_0,v_0,0)\in D_0\). By (9), \(q\) is in the closure of \(W\). Apply (4) to \(D,H\) near \(q\). Since \(D\subset Z\), we have \(D\setminus H=W\); the resulting holomorphic arc can be written

\[
\gamma(s)=(x(s),v(s),\tau(s)),
\qquad \gamma(0)=q,\qquad \gamma(s)\in W\quad(s\ne0).
\tag{12}
\]

The holomorphic function \(\tau\) vanishes at zero and is not identically zero. Thus

\[
\tau(s)=s^m b(s),\qquad m\ge1,\quad b(0)\ne0.
\tag{13}
\]

After shrinking to a simply connected disc, choose a holomorphic \(m\)-th root \(c(s)\) of the nonvanishing function \(b(s)\). Put \(u=s c(s)\). Its derivative at zero is \(c(0)\ne0\), so the holomorphic inverse function theorem gives an inverse \(s=s(u)\), and

\[
\tau(s(u))=u^m.
\tag{14}
\]

For a sequence of positive real \(u_j\downarrow0\), set

\[
b_j=x(s(u_j)),\quad
a_j=x(s(u_j))+u_j^m v(s(u_j)),\quad
h_j=u_j^m>0.
\tag{15}
\]

The arc lies in \(W\) at every nonzero complex parameter, so \(b_j\in B\) and \(a_j\in A\). Both tend to \(x_0\), and their divided difference is \(v(s(u_j))\to v_0\). These are exactly the real positive-scale conditions (2). This proves (10).

The original arc parameter \(s(u_j)\) can be complex. There is no requirement that points of a complex analytic piece have real coordinates. Only the scale \(h_j\) in (2) must be positive real, which is precisely what (14) supplies. An arbitrary rotation of the original real parameter would not by itself prove (15).

## Coordinate changes and complex scalars

For a holomorphic change of base coordinates \(y=f(x)\), the deformation-coordinate change for \(t\ne0\) is

\[
(x,v,t)\longmapsto
\left(f(x),\frac{f(x+tv)-f(x)}{t},t\right).
\tag{16}
\]

The divided difference extends holomorphically at \(t=0\), with value \(df_xv\). For example, expand \(f\) in its convergent Taylor series at a local point; every term of \(f(x+tv)-f(x)\) has a factor \(t\). The inverse coordinate change has the same property, so these extensions give biholomorphic deformation charts. They carry (8) to the same intrinsic condition in the new coordinates, hence carry its closure and central fibre as well. Thus the analytic central sets in (10) glue to a complex analytic subset of \(TX\), with the usual tangent-coordinate transition at \(t=0\).

For \(\lambda\in\mathbb C^*\), the holomorphic map

\[
(x,v,t)\longmapsto(x,\lambda v,t/\lambda)
\tag{17}
\]

preserves (5), (6), (7) and (8), because the product \(tv\) is unchanged. It therefore preserves \(D\). At \(t=0\), it is multiplication by \(\lambda\) in the tangent fibre. Hence

\[
\lambda C(A,B)=C(A,B)
\qquad(\lambda\in\mathbb C^*).
\tag{18}
\]

The zero tangent vector causes no exception. We have proved that the real ordered pair normal cone of two locally closed complex analytic pieces is complex analytic and complex-conic.

Reversing the ordered pair in (2) gives \(C(B,A)=-C(A,B)\). By (18) these happen to be equal as subsets in the complex analytic case. The reversal map on a given difference vector is still \(v\mapsto-v\); equality of the resulting sets does not erase that sign from maps or later Fourier conventions.

## Exercises with complete solutions

### The naive central equations add a spurious fibre

*Difficulty: Introductory.*

Take \(X=\mathbb C\) and \(A=B=\{0\}\). Compute \(Z\), \(W\), \(D\), \(D_0\) and the actual normal cone at zero. Explain which irreducible component is removed.

**Solution.** Equations (6) are \(x=0\) and \(tv=0\). Thus \(Z\) is the union of \(\{x=0,v=0\}\), with \(t\) arbitrary, and \(\{x=0,t=0\}\), with \(v\) arbitrary. For \(t\ne0\), necessarily \(v=0\). Hence \(W=\{x=0,v=0,t\ne0\}\), its closure is \(D=\{x=0,v=0\}\), and \(D_0=\{x=0,v=0,t=0\}\). Every difference of two points of \(A=B=\{0\}\) is zero, so (2) gives just the zero tangent vector. The entire component \(\{x=0,t=0\}\) is contained in the deleted set \(H\); retaining it would incorrectly give the full tangent fibre.

### A punctured analytic piece still produces every central direction

*Difficulty: Introductory.*

Let \(A=\mathbb C\setminus\{0\}\) and \(B=\{0\}\). Compute the normal cone at zero using positive real scales, including the zero vector. Compare \(D\) with \(W\).

**Solution.** The closure/frontier pairs are \((\mathbb C,\{0\})\) for \(A\) and \((\{0\},\varnothing)\) for \(B\). With \(x=0\), (8) says \(t\ne0\) and \(tv\ne0\), so \(W=\{x=0,t\ne0,v\ne0\}\). Its closure is \(D=\{x=0\}\), with \(v,t\) arbitrary. Thus \(D_0\) is the full tangent fibre at zero.

For any \(v\ne0\), take \(h_j=1/j\), \(a_j=h_jv\) and \(b_j=0\); the divided difference is \(v\). To realize zero while staying in the punctured piece, take \(a_j=h_j^2\) and \(b_j=0\). Its divided difference is \(h_j\to0\). Removing the analytic frontier excludes points at nonzero parameter but need not exclude their accessible central limits.

### Quadratic contact has a full complex pair cone

*Difficulty: Intermediate.*

In \(\mathbb C^2\), let \(A=\{(z,z^2):z\in\mathbb C\}\) and \(B=\{(z,0):z\in\mathbb C\}\). Compute the origin fibre of \(C(A,B)\). Compare it with \(T_0A-T_0B\) and the analogous real pair cone.

**Solution.** Given \((a,b)\in\mathbb C^2\) with \(b\ne0\), choose a complex square root \(c\) of \(b\), and for real \(s>0\) put

\[
a(s)=(cs,bs^2),\qquad
b(s)=(cs-as^2,0),\qquad h(s)=s^2.
\tag{19}
\]

Both points lie in their prescribed sets and tend to zero, and the divided difference is exactly \((a,b)\). If \(b=0\), take \(a(s)=(0,0)\), \(b(s)=(-as^2,0)\), with the same positive scale. Thus every vector occurs and the fibre is \(\mathbb C^2\).

Both ordinary tangent spaces at zero are the horizontal complex line, whose difference is only \(\mathbb C\times\{0\}\). Second-order separation supplies the additional directions. For the corresponding real parabola and real line, the divided vertical difference is nonnegative, giving \(\mathbb R\times\mathbb R_{\ge0}\). Complex square roots remove that sign restriction while the scale remains positive real.

### The complex cusp has a line as its point cone

*Difficulty: Intermediate.*

Let \(A=\{(u^2,u^3):u\in\mathbb C\}\subset\mathbb C^2\) and \(B=\{0\}\). Compute the origin fibre of \(C(A,B)\), with the scale in (2) still positive real.

**Solution.** Suppose \((u_j^2/h_j,u_j^3/h_j)\) converges and \(u_j\to0\). The first coordinate is bounded, so \(|u_j^3/h_j|=|u_j|\,|u_j^2/h_j|\to0\). Every limiting vector therefore has second coordinate zero.

For any \(a\ne0\), choose a square root \(c\) of \(a\), take \(u=cs\) with real \(s\downarrow0\), and use \(h=s^2\). The divided vector is \((a,c^3s)\to(a,0)\). For the zero vector, take \(u=s\) and \(h=s\), giving \((s,s^2)\to0\). Hence the cone is \(\mathbb C\times\{0\}\). The limiting tangent directions are complex-conic even though the usual parametrization has zero first derivative at the cusp point.

### A complex parameter becomes a positive real scale

*Difficulty: Advanced.*

Suppose an arc in (12) has \(\tau(s)=is^2(1+s)\). Produce the local reparameterization (14). Explain why using only positive real \(s\) would not prove the real normal-cone inclusion.

**Solution.** On a small disc around zero choose \(c(s)=e^{i\pi/4}(1+s)^{1/2}\), where the square root has value one at zero. Then \(c(s)^2=i(1+s)\). Put \(u=s c(s)\). Its derivative at zero is \(e^{i\pi/4}\ne0\), so it has a holomorphic local inverse. The exact identity is \(\tau(s(u))=u^2\). For positive real \(u\), this is a positive real scale. The inverse satisfies \(s(u)=e^{-i\pi/4}u+O(u^2)\), which is generally complex.

For positive real \(s\), the value \(is^2(1+s)\) is imaginary, so it is not a permitted scale in (2). The holomorphic arc remains in \(W\) for small nonzero complex parameters, making the change legitimate. It is this arc property together with the exact power normalization, rather than positive conicity alone, that proves the reverse inclusion in (10).

### Deleting one analytic branch retains the right closure

*Difficulty: Advanced.*

Let \(Z=\{xy=0\}\subset\mathbb C^2\) and \(H=\{x=0\}\). Compute \(\overline{Z\setminus H}\). Then explain the role of local finiteness in (3) if infinitely many global analytic components are present.

**Solution.** The vertical branch is contained in \(H\) and is removed entirely. The horizontal branch \(\{y=0\}\) loses only its origin. Hence \(Z\setminus H=\{y=0,x\ne0\}\), and its closure is precisely the full horizontal branch. The origin returns as an accessible limit, while nonzero points of the vertical branch do not return.

Near any ambient point, a locally finite component family has only finitely many relevant members. A convergent sequence approaching that point can eventually use only those members; after a subsequence it uses one fixed component. The closure of the selected union is therefore locally the union of the closures of just those finitely many selected branches. That finite union is analytic. Without local finiteness, an infinite union can acquire unrelated accumulation sets and need not be analytic; (3) would have no such local finite reduction.

## The next geometric use

The result supplies complex analytic normal-cone geometry while preserving the positive-real definition used by microsupport. The component selection prevents false central directions, and the arc normalization explains why complex phase does not restrict the accessible tangent cone. These are the geometric ingredients needed when passing from real conormal estimates to analytic conormal covers and complex stratifications.

## Sources and the deformation argument

**Normal cones and complex deformation.** Masaki Kashiwara and Pierre Schapira, [*Microlocal Study of Sheaves*, Astérisque 128 (1985)](https://www.numdam.org/item/AST_1985__128__1_0/), §1.2, printed p. 15, defines the real normal cone through positive multiples of differences. This lesson fixes the order of the two points and uses that convention throughout. Masaki Kashiwara and Teresa Monteiro Fernandes, [*Involutivité des variétés microcaractéristiques*, Bulletin de la Société Mathématique de France 114 (1986), 393–402](https://www.numdam.org/item/10.24033/bsmf.2062.pdf), §1.2, printed p. 398, constructs the complex normal deformation using an ideal and a deformation parameter. These are classical constructions. Here the ordered-pair problem is developed directly in the finite coordinate chart (5), with the three excluded loci (7) recorded before taking closure.

**Exactly which components survive.** Jean-Pierre Demailly, [*Complex Analytic and Differential Geometry*, version of 21 June 2012](https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/agbook.pdf), Chapter II, Proposition 4.24 and Proposition 4.26, p. 98, gives density of the connected regular part of an irreducible germ and the dimension drop for a proper analytic subgerm. Theorem 5.3 and Corollary 5.4, pp. 102–103, give the locally finite global component decomposition and the precise closure-after-deletion rule used in (3). Our short proof of (3) makes that rule explicit; it does not establish the underlying local analytic algebra. In particular, arbitrary analytic subsets of an open complement are outside this rule's hypotheses.

**Recovering positive real parameters.** The holomorphic arc in (4) is obtained here from the earlier real curve-selection prerequisite, followed by the one-variable identity theorem and isolated zeros. The reparameterization (13)–(15) then writes the nonzero deformation parameter as a positive integral power. This is the step that recovers every point of the complex central fibre using the original positive real scales. It cannot be replaced by the assertion that setting the parameter equal to zero gives the correct cone. The coordinate-change calculation also keeps the ordered difference map, so exchanging the inputs negates the represented vector even though a complex cone is invariant under that negation.

**Scope of the proof.** The teaching route is the component test, the arc, the accessible deformation, positive-power recovery and coordinate compatibility. The six solved problems test inaccessible components, scaling, signs and the actual normal fibre. The arguments are independently written explanations of classical analytic geometry; the component theory, real curve selection and elementary holomorphic local theorems remain their stated prerequisites. Their full transitive proofs are not supplied by these citations.
