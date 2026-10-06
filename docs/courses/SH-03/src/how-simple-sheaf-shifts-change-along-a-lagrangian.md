# How simple-sheaf shifts change along a Lagrangian

The coefficient type of a simple sheaf can stay fixed while its numerical shift changes. A projection singularity is where the inertia correction can change. The right continuity statement follows a continuous family of auxiliary Lagrangian planes, rather than the numerical shift alone. We prove that statement, calculate a cusp including its missing boundary, and explain why the corresponding numerical shift stays constant along a connected complex Lagrangian.

Use Pure and simple sheaves from directional tests. Manifolds are finite-dimensional smooth real manifolds unless specified otherwise; \(k\) is a commutative ring of finite global dimension and \(F\in D^b(k_X)\). Coefficient complexes may have arbitrary modules. We retain the earlier local conormal object and support-test prerequisites. The ordered inertia index uses \(\omega=d\theta\). Local existence of contact kernel equivalences proves the local hypersurface contact normal form with the required auxiliary-plane condition. Pure and simple sheaves from directional tests proves the zero-covector conormal geometry. The ordered index proof proves continuity at fixed pairwise-intersection dimensions and the four-plane cocycle, including degenerate triples.

*Written by GPT-6.1 Sol (OpenAI), Ultra, September 2026. Self-checked by the writing AI. New original text is public domain (CC0).*

## Follow a transverse auxiliary plane

Let \(\Lambda\subset T^*X\) be a smooth conic Lagrangian and suppose \(\operatorname{SS}(F)\subset\Lambda\) on a neighborhood of the points considered. Let \(S\) be a connected topological space, \(p:S\to\Lambda\) continuous, and let \(\mu(s)\subset T_{p(s)}T^*X\) be a continuous family of Lagrangian planes such that

\[
\mu(s)\cap V(s)=0,\qquad
\mu(s)\cap A(s)=0,
\quad V(s)=T_{p(s)}\pi_X^{-1}(\pi_Xp(s)),
\quad A(s)=T_{p(s)}\Lambda.
\qquad\text{(1)}
\]

Choose allowed type shifts \(d(s)\), meaning
\(d(s)\equiv\dim(V(s)\cap A(s))/2\pmod{\mathbb Z}\).
Then the following is a continuity theorem for the coefficient type:

**Theorem.** If

\[
\kappa=d(s)-\frac12\tau(V(s),A(s),\mu(s))
\quad\text{is constant on }S,
\qquad\text{(2)}
\]

the isomorphism class of the type of \(F\) with shift \(d(s)\) at \(p(s)\) is constant on \(S\).

An auxiliary plane transverse to \(V\) is a graph of a symmetric Hessian. At a fixed point it can therefore be realized as the tangent graph of a test function with the prescribed value and differential. The other condition in (1) makes that test transverse to \(\Lambda\). Test independence permits use of its index in (2), without a requirement that the whole family arise from one global function.

## The conormal chart and the contact correction

**Proof.** First suppose \(\Lambda=T_M^*X\) in a small cotangent chart. Its vertical intersection has constant dimension \(c=\operatorname{codim}M\). The three pairwise intersection dimensions of \((V,A,\mu)\) are \((c,0,0)\). The proved constant-intersection continuity of the ordered index therefore makes \(\tau(V,A,\mu)\) locally constant. Equation (2) makes \(d\) locally constant too. The conormal coefficient-object model extends from a chosen point to a small cotangent neighborhood: the finitely many denominator cones in a representing isomorphism avoid that point and then avoid a smaller neighborhood. On the resulting chart \(F\simeq Q_M\) for a fixed bounded \(Q\). Its type at shift \(d\) is \(Q[c/2-d]\), which is locally constant.

Near a nonzero point of a general \(\Lambda\), use a hypersurface contact transformation \(\chi\) taking \(\Lambda\) to a conormal. Choose it so that \(\chi_*\mu(s_0)\) is also transverse to the target vertical plane. Apply the proved finite normalization to \(\Lambda\) and the auxiliary plane \(\mu(s_0)\); the latter does not contain the radial line because it is transverse to the original vertical. This supplies the required target transversality without an additional geometric input. Transversality is open, so it persists for \(s\) near \(s_0\). Write

\[
W(s)=\chi_*^{-1}(V'(s)),\qquad
d'(s)=d(s)-\frac12(n-1)-\frac12\tau(V(s),A(s),W(s)),
\qquad\text{(3)}
\]

where \(V'\) is target vertical and \(n=\dim X\). The contact type-shift theorem identifies the original type at \(d\) with the transformed type at \(d'\). The transformed auxiliary index is \(\tau(W,A,\mu)\). Hence its corrected degree is

\[
d'-\frac12\tau(W,A,\mu)
=\kappa-\frac12(n-1)-\frac12\tau(V,\mu,W).
\qquad\text{(4)}
\]

To check the sign, the cocycle for the ordered quadruple \((V,A,\mu,W)\) gives
\(\tau(V,A,W)+\tau(W,A,\mu)
=\tau(V,A,\mu)+\tau(V,\mu,W)\).
Substituting it in (3) proves (4).

The pairwise intersections in the last triple have constant dimensions: \(\mu\cap V=0\) by (1), \(\mu\cap W=0\) by the chosen target transversality, and

\[
\dim(V\cap W)=1.
\qquad\text{(5)}
\]

Here is a geometric verification of (5). The contact graph is the conormal of a hypersurface \(H\subset X'\times X\). A vector in \(V\cap W\) corresponds through the graph to a tangent conormal vector with both base components zero. In a local defining equation for \(H\), its base is fixed and only its conormal multiplier varies. This is the one-dimensional radial line. Both cotangent graph projections are local diffeomorphisms, so the correspondence between this line and \(V\cap W\) is an isomorphism. This calculation holds on the whole selected graph patch, not just at one point.

Inertia continuity applied to \((V,\mu,W)\) now makes the right side of (4) locally constant. The already proved conormal case gives locally constant transformed type, and (3) gives locally constant original type. At a zero covector use the local closed-conic conormal model directly, so the first part applies there.

We have proved local constancy on the parameter space \(S\). A locally constant map from a connected space to isomorphism classes has a single value: the inverse image of any value and its complement are both open. This last argument does not assume that \(S\) is path connected or locally connected. It completes the proof. \(\square\)

The theorem compares isomorphism classes of coefficient complexes. It does not choose a global trivialization of their orientation lines or rule out monodromy of local identifications.

## A half-open cusp and its smooth conic Lagrangian

In this example take \(k\ne0\). On \(\mathbb R^2\), use coordinates \((x,y)\) and let

\[
Z=\{x>0,-x^{3/2}\leq y<x^{3/2}\},\qquad F=k_Z.
\qquad\text{(6)}
\]

The lower boundary is included; the upper boundary and the cusp point are excluded. The standard locally closed-subset microsupport calculation for this set gives, in the region \(\eta>0\), the following full nonzero microsupport:

\[
\Lambda=\left\{
(a^2,-a^3;\tfrac32a\lambda,\lambda):
a\in\mathbb R,\ \lambda>0
\right\}.
\qquad\text{(7)}
\]

The subset calculation is a foundational microsupport input. We use its exact included/excluded boundaries, rather than a generic drawing of a closed cusp.

The relation (7) is smooth even at \(a=0\). The covector coordinates recover \(a=2\xi/(3\eta)\) and \(\lambda=\eta\), and their parameter derivative has determinant \(3\lambda/2\ne0\). It is therefore a smooth embedded two-dimensional conic manifold. Its tautological form is
\((3a\lambda/2)d(a^2)+\lambda d(-a^3)=0\).
Thus its symplectic form vanishes and its half dimension makes it Lagrangian. Its base projection, however, has a cusp.

For \(a>0\), the point is on the included lower boundary. The sheaf is locally the closed upper-side coefficient for \(h=y+x^{3/2}\), and its positive conormal is (7). Its simple shift is \(1/2\). For \(a<0\), it lies on the excluded upper boundary; locally the sheaf is the open lower-side coefficient for \(h=y-x^{3/2}\), at that function's positive conormal. Its simple shift is \(-1/2\).

## The cusp test has one cohomological degree

At \(p=(0;dy)\), the plane \(T_p\Lambda\) in (7) is the full vertical plane, while the test \(\varphi=y\) has horizontal tangent graph. They are transverse, and \(\tau_\varphi=\tau(V,V,\text{horizontal})=0\).

We calculate the raw support test instead of extrapolating a branch shift. Since \(0\notin Z\), the stalk \(F_0\) is zero. For \(j:\{y<0\}\hookrightarrow\mathbb R^2\), the support triangle gives

\[
\bigl(R\Gamma_{\{y\geq0\}}F\bigr)_0
\simeq (Rj_*j^{-1}F)_0[-1].
\qquad\text{(8)}
\]

Use the cofinal rectangles \(U_\epsilon=\{|x|<\epsilon,|y|<\epsilon^{3/2}\}\). In their negative part, the support of \(j^{-1}F\) is
\(0<x<\epsilon\), \(-x^{3/2}\leq y<0\).
It is closed relative to that negative open set. The substitution \(t=-y/x^{3/2}\) identifies it with
\((0,\epsilon)\times(0,1]\), a contractible locally contractible product. The constant-coefficient acyclicity and restriction-unit comparison give ordinary cohomology \(k\) in degree zero and no other degree. Smaller rectangles restrict its constant generator to the same generator. Thus \((Rj_*j^{-1}F)_0\simeq k\) with this actual restriction comparison, and

\[
C_y(F)\simeq k[-1].
\qquad\text{(9)}
\]

With ambient dimension two and inertia zero, the normalized type at shift \(d=0\) is \(C_y(F)[1]\simeq k\). The sheaf is simple with shift zero at the cusp. A zero ordinary stalk and a nonzero directional support test coexist because (8) also measures approach from the negative open region.

## The auxiliary index accounts for the three shifts

Take the horizontal auxiliary plane \(\mu\) along (7). It is transverse both to vertical and to \(T\Lambda\), including at the cusp. To compute its inertia, express \(T\Lambda\) as a graph over covector variations:

\[
\delta(x,y)=B_{a,\lambda}\,\delta(\xi,\eta),
\qquad
B_{a,\lambda}=\frac{a}{3\lambda}
\begin{pmatrix}4&-6a\\-6a&9a^2\end{pmatrix}.
\qquad\text{(10)}
\]

This follows by differentiating (7), solving
\(\delta a=2(\delta\xi-3a\delta\eta/2)/(3\lambda)\), and substituting into the two base variations. The matrix is \(a/(3\lambda)\) times the outer product of \((2,-3a)\) with itself. Its signature is \(\operatorname{sgn}a\), and is zero at \(a=0\).

For the ordered vertical/graph-over-covectors/horizontal triple, inertia equals the signature of \(B\). To see this directly, its quadratic form on covector vectors \(u,v\) and a horizontal vector \(w\) is
\(u^tBv+(v-u)^tw\).
Putting \(z=u-v\) rewrites it as \(v^tBv+z^t(Bv-w)\). The latter pairing is hyperbolic and contributes zero signature; the first term has signature \(B\). Therefore

\[
\tau(V,T\Lambda,\mu)=
\begin{cases}1&a>0,\\0&a=0,\\-1&a<0.
\end{cases}
\qquad
d(a)=\frac12\operatorname{sgn}a.
\qquad\text{(11)}
\]

The allowed parity also agrees: \(\dim(V\cap T\Lambda)=1\) on either regular branch and is two at the cusp. Equations (11) make \(d-\tau/2=0\) throughout. The continuity theorem consequently keeps type \(k\) fixed across all three numerical shifts. Keeping \(d=1/2\) through the cusp instead would not even satisfy the required integer parity there.

## Complex Lagrangians have no such numerical jump

Let \(X\) now be a complex manifold and \(\Lambda\subset T^*X\) a connected complex Lagrangian. Interpret the cotangent geometry through its underlying real symplectic form \(2\operatorname{Re}\sigma\), where \(\sigma\) is the complex cotangent symplectic form. For three complex Lagrangian planes their real inertia is zero. Indeed multiplication by \(i\) on all three arguments sends the real quadratic index form to its negative. It bijects its positive and negative parts, so their dimensions are equal.

Here is an explicit complex simultaneous complement. For two complex Lagrangian planes \(V,A\), put \(K=V\cap A\), \(r=\dim_{\mathbb C}K\). The quotient \(K^\sigma/K\) is symplectic, and the images of \(V,A\) are transverse Lagrangians. Choose paired bases for these images and lift them to \(V,A\). Their span \(S\) is symplectic and orthogonal to \(K\); the lifts remain in the two planes. Its symplectic orthogonal \(S^\sigma\) has dimension \(2r\) and contains \(K\) as a Lagrangian. Extend a basis of \(K\) to a symplectic basis there: choose dual vectors using nondegeneracy, then add linear combinations of the \(K\)-basis to cancel their mutual pairings. This uses division by two, valid over \(\mathbb C\). Thus symplectic coordinates \((Q',Q'';P',P'')\), with \(\dim Q''=r\), give

\[
V=\{Q'=Q''=0\},\qquad
A=\{P'=Q''=0\}.
\]

The plane \(\mu=\{P'=Q',\ P''=0\}\) is complex Lagrangian because its graph matrix is symmetric. Intersecting with \(V\) forces \(Q'=Q''=P'=P''=0\); intersecting with \(A\) does the same. This includes \(r=0\) and \(r=n\). Extend this plane continuously in a local complex symplectic frame. Transversality to both varying planes is open, so it persists after shrinking. These local families are also real Lagrangian transverse families. Their inertia is zero, so a fixed numerical shift \(d\) satisfies (2). The parity condition causes no difficulty: the real vertical intersection dimension is even, and allowed \(d\) are integral.

If \(\operatorname{SS}(F)\) is contained in \(\Lambda\) on its neighborhood and \(F\) is pure with shift \(d\) at one point, the continuity theorem makes it pure with that same shift on each such local chart. Connectedness propagates the assertion along all of \(\Lambda\). In fact its type module has the same isomorphism class throughout. This also proves the corresponding connected complex purity phenomenon, without claiming a globally chosen generator.

## Exercises with complete solutions

### Connected does not mean path connected

*Difficulty: Introductory.*

Which step in the continuity proof uses connectedness of \(S\)? Would a proof comparing only points joined by paths suffice for the stated theorem?

**Solution.** The proof first makes the type locally constant at every parameter value. The inverse image of one type class and its complement are then both open; connectedness forces one to be empty. A path comparison alone would cover only path components, which need not equal connected components for an arbitrary topological parameter space. No path-connectivity assumption is present in the theorem.

### One-dimensional excess in a hypersurface graph

*Difficulty: Intermediate.*

Why does a hypersurface contact graph give \(\dim(V\cap W)=1\), rather than zero? Explain which degree argument uses this number.

**Solution.** A vertical vector on both sides corresponds to a conormal tangent vector with fixed hypersurface base point. Its conormal multiplier can vary, giving the radial line. A hypersurface has a one-dimensional normal space, so there is exactly one such direction. Both graph projections identify it with \(V\cap W\). This constant intersection, together with the two zero intersections involving \(\mu\), makes \(\tau(V,\mu,W)\) locally constant in (4).

### A missing cusp point can have a nonzero directional type

*Difficulty: Intermediate.*

For (6), find \(F_0\), \(C_y(F)\) and its normalized type at \((0;dy)\). Explain why there is no contradiction.

**Solution.** The cusp point is excluded, hence \(F_0=0\). The negative open-region coefficient has constant cohomology \(k\); the support triangle gives \(C_y(F)=k[-1]\). Ambient dimension two, inertia zero and shift zero then give normalized type \(k[-1][1]=k\). The local support test includes the derived approach from the complement region, rather than only the ordinary stalk.

### Check the branch matrix

*Difficulty: Advanced.*

For \(a=-1\) and \(\lambda=2\), compute \(B\), its rank, its inertia signature and the simple shift predicted by (11).

**Solution.** Formula (10) gives \(B=-\tfrac16\begin{pmatrix}4&6\\6&9\end{pmatrix}\). It is the negative outer product of \((2,3)\) divided by six, with eigenvalues \(-13/6\) and zero. Its rank is one and its signature is \(-1\), so the simple shift is \(-1/2\). The radical does not change that signature; it records the vertical radial direction on the regular branch.

### A function with the wrong covector

*Difficulty: Advanced.*

For the same cusp sheaf, compute \(C_x(F)\) at zero and explain why it does not replace the \(y\)-test at \((0;dy)\).

**Solution.** On the open complement \(\{x<0\}\) the sheaf vanishes, and its ordinary stalk at zero is also zero. The support triangle therefore gives \(C_x(F)=0\). But \(dx\ne dy\), so this function does not meet the selected covector. Formula (7) has no nonzero \(dx\) direction at its cusp. Directional type is attached to a covector, not just a base point or any chosen coordinate function.

### An index reversal in the path correction

*Difficulty: Advanced.*

A family has \(d=1/2\), \(\tau(V,A,\mu)=1\) on one branch, and \(d=-1/2\), \(\tau(V,A,\mu)=-1\) on the other. Compare the corrected quantities \(d-\tau/2\) and \(d+\tau/2\).

**Solution.** The first is zero on both branches, as required for constant type. The second is one on the first branch and minus one on the second. Alternating two index planes without changing the sign in the degree rule would therefore produce a false variation by two. The ordered cocycle derivation (3)–(4) fixes the correction's sign.

## References

The change of the shift of a simple sheaf along a Lagrangian, and its relation to the inertia index, are part of Kashiwara and Schapira's theory of simple sheaves; see M. Kashiwara and P. Schapira, [*Microlocal study of sheaves*](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf), Astérisque 128 (1985), Chapter 7. The ordered-index continuity and the cocycle are proved in the linked normal-forms lesson; the complex simultaneous-complement construction, the parameter-space proof, the local multiplier calculation, the cusp relative-support and matrix calculations and the complex argument are proved here.
