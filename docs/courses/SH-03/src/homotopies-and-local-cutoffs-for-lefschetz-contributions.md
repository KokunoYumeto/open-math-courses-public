# Homotopies and local cutoffs for Lefschetz contributions

A local contribution can be computed on a smaller coefficient complex. The cutoff must also carry a map: restriction and extension have different directions at its boundary. We prove the two resulting trace formulas, then use them to distinguish an attracting interval endpoint from a repelling one.

*Written by GPT-6.1 Sol (OpenAI), Ultra, 2 October 2026. Author self-check recorded; not independently reviewed. New original text is public domain (CC0).*

Learn first Lefschetz traces of constructible correspondences, Closed supports and evaluated proper transport, and Perfect operations and finite microlocal coefficients. We use their actual diagonal identity, supported pullback, evaluated exceptional counit, constructible duality and finite cohomology. Ordinary interval descent, locally closed extension adjunctions and their projection/base-change maps are the exact earlier sheaf-operation prerequisites. Their transitive foundations and independent review remain open.

## A family class has no parameter integration shift

Let \(k\) be a characteristic-zero field and \(F\in D^b_{\mathbb R\text{-c}}(k_X)\), with perfect stalks. The real analytic manifold \(X\) has the standing Hausdorff, countability and uniform finite dimension hypotheses. Write \(S=\operatorname{supp}(F)\), using closed support.

Take \(I=[0,1]\), the projection \(p:X\times I\to X\), a continuous family \(f:X\times I\to X\), and a sheaf morphism

\[
 \phi:f^{-1}F\longrightarrow p^{-1}F.
 \qquad\text{(1)}
\]

For the analytic version, \(f\) is the restriction of an analytic map on \(X\times\mathbb R\). Define \(f_t(x)=f(x,t)\), \(\phi_t=i_t^{-1}\phi\), and

\[
 \widetilde Z=\{(x,t):x\in S,\ f(x,t)=x\},
 \qquad Q=p(\widetilde Z).
 \qquad\text{(2)}
\]

Assume \(\widetilde Z\) compact. In particular, \(Q\) is compact and closed.

**Theorem.** The image of \(C(\phi_t)\) in \(H_Q^0(X;\omega_X)\), and hence in \(H_c^0(X;\omega_X)\), is independent of \(t\).

**Proof.** Put \(h=(f,p):X\times I\to X^2\). Pull the supported diagonal identity of \(F\) by the ordinary supported comparison. The coefficient becomes
\[
 f^{-1}F\otimes p^{-1}D_XF
 \xrightarrow{\phi\otimes1}
 p^{-1}(F\otimes D_XF)
 \longrightarrow p^{-1}\omega_X.
 \qquad\text{(3)}
\]
Both input factors are zero off \(f^{-1}S\cap p^{-1}S\). Their coincidence support consequently refines to \(\widetilde Z\). This produces
\[
 c\in H_{\widetilde Z}^0(X\times I;p^{-1}\omega_X).
 \qquad\text{(4)}
\]
Restriction to the slice gives \(C(\phi_t)\): the ordinary units, support comparison and evaluation used in (3) restrict to the very same maps defining that class.

This construction uses the duality and diagonal comparison of \(F\) on \(X\), not duality of \(f^{-1}F\) on the family. It therefore works for a continuous \(f\), without asserting constructibility of its whole pullback. In the analytic version one may construct it on the ambient open parameter interval and restrict to \(I\). There is no integration over time in (3); its target is \(p^{-1}\omega_X\), not the dualizing complex of the parameter product.

Enlarge the support in (4) to \(Q\times I\). For any bounded complex \(H\) on \(X\), ordinary interval descent and the closed support adjunction give
\[
 \begin{aligned}
 Rp_*p^{-1}H&\simeq H,\\
 Rp_*R\Gamma_{Q\times I}p^{-1}H
 &\simeq R\Gamma_Q(Rp_*p^{-1}H)
 \simeq R\Gamma_QH.
 \end{aligned}
 \qquad\text{(5)}
\]
For the second comparison, transpose against a complex supported on \(Q\). Pullback by \(p\) has support on \(Q\times I\); the ordinary adjunction and the closed-support adjunction give the two identical Hom functors. Thus (5) identifies the actual support maps, rather than just their objects. The first comparison is ordinary descent for a constant interval fibre, including its endpoints.

Under (5), the pullback
\[
 H_Q^0(X;\omega_X)
 \xrightarrow{\ p^*\ }
 H_{Q\times I}^0(X\times I;p^{-1}\omega_X)
 \qquad\text{(6)}
\]
is an isomorphism. Every slice restriction is its inverse: restriction after pullback is the identity, since \(pi_t=\mathrm{id}\) and the ordinary triangular identity fixes that map. The restrictions of the enlarged \(c\) are therefore independent of \(t\). Compactness of \(Q\) permits forgetting to compact support and taking the normalized point trace. \(\square\)

The assertion concerns the class after its support is enlarged to the single compact set \(Q\). It does not identify the varying groups \(H_{\widetilde Z_t}^0(X;\omega_X)\) by arbitrary choices.

**Linear-family consequence.** Let \(V\) be a finite-dimensional real vector space, \(F\) a bounded conic constructible complex, \(u_t:V\to V\) a continuous linear family, and \(\phi:u^{-1}F\to p^{-1}F\) a given family morphism. If \(1\) is never an eigenvalue, then \(C_0(\phi_t)\) is constant on a connected parameter interval. On each compact subinterval the supported fixed locus is contained in \(\{0\}\times I\), so the theorem applies. The normalized point traces identify all slice classes with \(k\). This proves the continuous version without replacing a family morphism by unrelated maps on individual slices.

## Compact closure controls the boundary

A proper first map alone does not give a global compact-cohomology trace formula. Translation \(t\mapsto t+1\) on \(\mathbb R\), with constant coefficient, has no fixed point, while its compact cohomology is \(k[-1]\) with trace \(-1\). Properness of translation does not remove that contribution at infinity.

For a relatively compact cutoff, use its compact **closed support** in the ambient manifold. The trace theorem then applies to that compact coefficient. To have only the original contribution at \(x\), we must require
\(Z\cap\overline V=\{x\}\).
Deleting a boundary point from \(V\) does not by itself remove it from the closed support of an extension. This closure in the hypothesis is essential.

## The ordinary cutoff has a closed entrance and an open exit

Return to an analytic \(f:X\to X\), a morphism \(\phi:f^{-1}F\to F\), and an isolated \(x\) of
\[
 Z=S\cap\{f=\mathrm{id}\}.
 \qquad\text{(7)}
\]
Let \(V\) be a locally closed subanalytic neighbourhood of \(x\). A neighbourhood contains an ambient open neighbourhood of \(x\). Put
\[
 A=f^{-1}V,\qquad W=A\cap V,
 \qquad H=i^{-1}F,\quad i:V\hookrightarrow X.
 \qquad\text{(8)}
\]
Suppose
\[
 W\text{ is open in }V
 \quad\text{and closed in }A.
 \qquad\text{(9)}
\]
For a locally closed set \(L\), write \(F_L=k_L\otimes F\), using extension by zero. The map is
\[
 \phi_V:f^{-1}F_V=(f^{-1}F)_A
 \xrightarrow{\phi_A}F_A
 \longrightarrow F_W
 \longrightarrow F_V.
 \qquad\text{(10)}
\]
The middle arrow is closed restriction inside \(A\); the last is open extension inside \(V\). Those are exactly the two clauses of (9).

**Ordinary cutoff theorem.** The new map agrees with \(\phi\) near \(x\), so
\(C_x(\phi_V)=C_x(\phi)\).
If, in addition, \(V\) is relatively compact and \(Z\cap\overline V=\{x\}\), then
\[
 C_x(\phi)=\operatorname{str}R\Gamma(X;\phi_V).
 \qquad\text{(11)}
\]
The endomorphism on the right includes ordinary \(f\)-pullback.

**Proof.** On a sufficiently small neighbourhood of \(x\), both \(V\) and \(f^{-1}V\) contain the whole neighbourhood. Every cutoff in (10) is then the identity. The germ theorem proves the local equality.

For the global trace put \(G=F_V\). Tensor closure makes \(G\) bounded constructible with perfect stalks, and

\[
 \operatorname{supp}G\subset S\cap\overline V.
 \qquad\text{(12)}
\]

The right side is compact. The common support
\(f^{-1}\operatorname{supp}G\cap\operatorname{supp}G\)
is therefore compact as a closed subset of \(\operatorname{supp}G\). Its coincidence support lies in
\(Z\cap\overline V=\{x\}\).
The preceding correspondence trace theorem, with second map identity and coefficient \(G\), gives its global trace as that one normalized point contribution. The actual coefficient map is (10), and its germ is \(\phi\), so the contribution is \(C_x(\phi)\). This proves (11).

The deleted boundary stays in the possible closed support in (12); the closure hypothesis is the step that excludes other fixed-point contributions there. No compact-cohomology trace theorem for an arbitrary noncompact correspondence is needed. \(\square\)

## The supported cutoff reverses the two conditions

Instead suppose
\[
 W\text{ is closed in }V
 \quad\text{and open in }A.
 \qquad\text{(13)}
\]
Write \(R\Gamma_LF=Ri_{L*}i_L^!F\) for a locally closed support functor. Its natural inverse comparison and cutoff maps give
\[
 \begin{aligned}
 I_V(\phi):f^{-1}R\Gamma_VF
 &\longrightarrow R\Gamma_A(f^{-1}F)
 \xrightarrow{\phi}R\Gamma_AF\\
 &\longrightarrow R\Gamma_WF
 \longrightarrow R\Gamma_VF.
 \end{aligned}
 \qquad\text{(14)}
\]
Open restriction inside \(A\) gives the penultimate arrow; enlargement of closed support inside \(V\) gives the last. Formula (13) therefore has the opposite boundary order from (9).

**Supported cutoff theorem.** We have
\(C_x(I_V(\phi))=C_x(\phi)\).
For relatively compact \(V\) with \(Z\cap\overline V=\{x\}\),
\[
 C_x(\phi)=\operatorname{str}I_V(\phi)
 \quad\text{on }R\Gamma_V(X;F).
 \qquad\text{(15)}
\]

**Proof.** The germ equality follows exactly as before: near \(x\), the support set is the whole open neighbourhood, so the comparison and both cutoff maps are identities.

Put \(G=R\Gamma_VF=R\mathcal Hom(k_V,F)\). Internal-Hom constructibility and perfection apply to the locally closed subanalytic cutoff. Its closed support satisfies
\[
 \operatorname{supp}G\subset S\cap\overline V.
 \qquad\text{(16)}
\]
Indeed it vanishes on every open set disjoint from \(S\) or from \(\overline V\). The right side is compact, so both its global complex \(R\Gamma(X;G)=R\Gamma_V(X;F)\) and its correspondence trace factor are perfect. As in the ordinary proof, its coincidence support is contained in \(Z\cap\overline V=\{x\}\).

Apply the preceding correspondence trace theorem directly to \(G\), the self-map \(f\), and the morphism (14). Its global endomorphism is exactly the one in (15): ordinary pullback, the supported inverse comparison, \(\phi\), open support restriction, and closed support enlargement. Its sole contribution agrees with the original one by the germ equality. Thus its supertrace is \(C_x(\phi)\), proving (15). The proof retains the ambient boundary in (16) and excludes extra fixed contributions by the stated closure condition. \(\square\)

The complexes in (11) and (15) need not be isomorphic. The theorem compares their correctly induced traces with a local class under their respective boundary conditions.

## An interval endpoint distinguishes attraction from repulsion

Use the canonical map for an orientation-preserving analytic local diffeomorphism preserving a closed interval. At an endpoint \(x\), assume \(f'(x)\ne1\). Translate and, if necessary, reflect the coordinate so that the endpoint is zero and the coefficient germ is \(k_{[0,\infty)}\).

If \(0<f'(0)<1\), continuity of the derivative gives, for sufficiently small \(\epsilon>0\),
\(f([-\epsilon,\epsilon])\subset(-\epsilon,\epsilon)\).
Take \(V=[-\epsilon,\epsilon]\). Then \(W=V\) is open in \(V\) and closed in \(f^{-1}V\), so the ordinary cutoff theorem applies. Its coefficient is \(k_{[0,\epsilon]}\), with global section complex \(k\) and identity action on the constant section. Hence
\[
 C_0(\phi)=1.
 \qquad\text{(17)}
\]

If \(f'(0)>1\), choose \(V=(-\epsilon,\epsilon)\) so that \(f^{-1}V\subset V\). Then \(W=f^{-1}V\) is open in \(V\) and closed in itself, again the ordinary cutoff pattern. Its coefficient is \(k_{[0,\epsilon)}\), whose compactly supported cohomology vanishes. Indeed it is the complement of one endpoint in a closed compact interval: the restriction \(R\Gamma([0,\epsilon];k)\to k_\epsilon\) is an isomorphism, and its localization fibre is zero. Thus
\[
 C_0(\phi)=0.
 \qquad\text{(18)}
\]

The same argument applies at the other endpoint after reflecting its inward coordinate. It proves the endpoint formula from the actual cutoff complexes. Shifts multiply the result by \((-1)^r\), and a rank-\(m\) identity coefficient multiplies it by \(m\).

## Exercises with complete solutions

### A contraction and an expansion use opposite cutoffs

*Difficulty: Intermediate.*

On \(\mathbb R\), take \(F=k_{\mathbb R}[r]\), \(f(t)=at\), \(a>0\), \(a\ne1\), and the canonical coefficient map. Verify a cutoff pattern and compute \(C_0(\phi)\) for \(a<1\) and \(a>1\).

**Solution.** For \(a<1\), take closed \(V=[-1,1]\). Its inverse image is \([-1/a,1/a]\), so \(W=V\) is open in \(V\) and closed in \(f^{-1}V\). Ordinary cutoff gives the closed-interval coefficient \(k_{[-1,1]}[r]\); its global section complex is \(k[r]\), and its induced constant-section action is one. The trace is \((-1)^r\).

For \(a>1\), take open \(V=(-1,1)\). Then \(W=f^{-1}V=(-1/a,1/a)\) is open in \(V\) and closed in \(f^{-1}V\). Its compact section complex is \(k[r-1]\). Proper pullback from the larger interval to the smaller one and open return both preserve the positive compact orientation generator. Their composite is one on this complex, giving \((-1)^{r-1}\). For \(r=0\), the local contributions are \(+1,-1\). The expansion calculation uses the actual compact degree, not the stalk identity.

### A rectangular saddle has one compact orientation degree

*Difficulty: Advanced.*

Let \(f(x,y)=(2x,y/2)\), \(F=k_{\mathbb R^2}\), and \(V=(-1,1)\times[-1,1]\). Check (9), compute the cutoff trace, and identify its local contribution.

**Solution.** Here \(f^{-1}V=(-1/2,1/2)\times[-2,2]\), and
\(W=(-1/2,1/2)\times[-1,1]\).
It is open in \(V\): the first interval is open and the second is the whole relative closed factor. It is closed in \(f^{-1}V\): the first factor is the whole relative open factor and the second is closed.

Compact cohomology of \(V\) is \(k[-1]\). The open first interval contributes its positive orientation class in degree one; the closed second interval contributes its constant section in degree zero. Both positive scalings preserve these classes, as do the closed entrance and open exit maps. The induced operator is identity on \(k[-1]\), so its supertrace is \(-1\). The only fixed point is \((0,0)\), giving \(C_{(0,0)}(\phi)=-1\) by (11). This verifies a mixed-boundary example without replacing all factors by an open ball.

### The supported calculation keeps the orientation action

*Difficulty: Intermediate.*

For \(f(t)=2t\), \(F=k_{\mathbb R}\) and \(V=[-1,1]\), verify (13) and compute (15) from the localization triangle.

**Solution.** Now \(W=[-1/2,1/2]\), closed in \(V\) and open in \(A=W\). Localization for the complement of \(V\) gives the restriction map
\(k\to k\oplus k\), the diagonal, since the two exterior components are contractible. Its fibre has cohomology \(k\) in degree one, hence \(R\Gamma_V(\mathbb R;k)=k[-1]\).

Positive dilation preserves the two exterior components and their difference generator. The actual supported inverse map and support enlargement induce identity on this degree-one class. Its trace is \(-1\), so \(C_0(\phi)=-1\). The ordinary cutoff with this same closed \(V\) is not supplied by (9): \(W\) is not open in \(V\). A numerical agreement found by ignoring that failed hypothesis would not define the required cutoff morphism.

### Complete the two-endpoint calculation

*Difficulty: Advanced.*

For \(f(t)=t+\frac1{10}t(1-t)e^{-t^2}\) and \(F=k_{[0,1]}[r]\), compute the two local contributions individually. Use the global calculation in the preceding lesson as a check.

**Solution.** The derivative at zero is \(11/10>1\), so zero is repelling in the inward coordinate. Formula (18) gives \(C_0=0\). At one, the derivative is \(1-\frac1{10e}\), lying strictly between zero and one. Reflection of the inward coordinate preserves that derivative, so (17) gives \(C_1=(-1)^r\).

Their sum is \((-1)^r\), equal to the global trace on the constant interval section \(k[r]\). Each endpoint stalk still has trace \((-1)^r\), and each endpoint point-support complex is still zero. Thus the discrepancy is now resolved locally: attraction contributes the constant section; repulsion uses the vanishing half-open cutoff complex.

### A fixed point escaping to infinity defeats compact family support

*Difficulty: Advanced.*

Take \(F=k_{\mathbb R}\), \(f(x,t)=(1+t)x-1\), \(0\le t\le1\), and the canonical family coefficient map. Find the fixed locus and its local traces. Explain precisely why the family theorem does not assert constancy.

**Solution.** At \(t=0\), \(f(x,0)=x-1\) has no fixed point. For \(t>0\), its unique fixed point is \(x=1/t\). Its derivative is \(1+t>1\). Translate that fixed point to zero and use the expansion calculation of Exercise 1: its local contribution is \(-1\).

The family fixed locus is \(\{(1/t,t):0<t\le1\}\), an unbounded closed subset of \(\mathbb R\times[0,1]\). It is not compact, and its projection cannot be placed in one compact \(Q\). The passage from (4) to a common compact support and its point trace therefore fails. The family coefficient morphism is valid; the lost hypothesis is compactness of the whole supported fixed locus, not continuity or existence of a map on each slice.

### Continuous linear deformations require a single family morphism

*Difficulty: Intermediate.*

Let \(F=k_{\{0\}}[r]\) on \(\mathbb R\), \(u_t(x)=(2+t)x\), \(-1/2\le t\le1/2\), and let the family coefficient map be multiplication by a scalar \(b\in k\). Compute all local contributions. Could one instead choose \(b_t\) independently on each slice?

**Solution.** Inverse image of the point coefficient under this family is the coefficient on \(\{0\}\times I\), equal to \(p^{-1}F\). Multiplication by the one scalar \(b\) is a sheaf morphism of that constant family. Every slice has compact common support \(\{0\}\), global coefficient \(k[r]\), and trace \((-1)^r b\). Its unique local contribution is that number.

The supported fixed locus is \(\{0\}\times I\); absence of eigenvalue one and the linear-family consequence give the same constant result. An arbitrary choice of slice scalars need not assemble to a sheaf morphism. For a constant coefficient along a connected interval, a morphism acts locally constantly and hence by one fixed scalar. Separate slice maps do not meet the hypothesis (1).

## References and further reading

These are the local cutoffs and homotopy invariance of the contributions in Kashiwara's microlocal Lefschetz fixed-point formula for constructible sheaves. Both cutoff proofs use the compact ambient closed support and the exact condition \(Z\cap\overline V=\{x\}\), including its boundary. The continuous-family construction uses only the displayed units, support maps and evaluation.

Y. Matsui and K. Takeuchi, [*Microlocal study of Lefschetz fixed point formulas for higher-dimensional fixed point sets*, arXiv 0812.4480v1, 24 December 2008](https://arxiv.org/abs/0812.4480v1), §3, uses deformation and homotopy to study localization to smooth fixed components. Its component setting involves additional normal-eigenvalue and compactness conditions. Here we have proved the family and cutoff mechanisms for the stated local targets; tangent specialization and general expanding/shrinking spaces come next.
